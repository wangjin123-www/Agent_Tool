# -*- coding: utf-8 -*-
"""fix：自动修复多维表格（可确定性推导的问题才修，语义类一律只报告）。

设计原则
--------
1. **只修能确定性推导的**：值格式规范化、选项缺失补齐——都有唯一正确答案。
   需要人工判断的（如「这个服务该归属哪些接口」）只报告，不猜。
2. **修前必看 raw**：所有修复基于 pull 落下的 base_raw.json 计算差异，
   再通过 lark-cli 写回多维表格；写回后再 pull 一次验证。
3. **--dry-run 只列计划**：默认预览，加 --apply 才真正写表。
4. **幂等**：修完再跑 diff 为空。

字段名一律走 config 的字段语义映射（schema.from_records），脚本内不写表内字段名。

支持的修复项
------------
R1 消息id 规范化     '801'/'0x801'/'0x0801' → '0x0801'（4 位大写十六进制）
R2 枚举值 规范化     '1'/'0x1' → '0x01'（2 位大写十六进制）
R3 select 选项缺失   记录值不在字段选项内 → 补选项（不删已有选项）
R4 子项类型别名      'uint8_t'/'int8' → 规范名（uint8/sint8/...）
"""
import re

from .common import bitable, schema
from .common.bitable import text, first


class FixError(RuntimeError):
    pass


# ------------------------------------------------------------------ 规范化工具
_HEX16 = re.compile(r"^(?:0[xX])?([0-9A-Fa-f]{1,4})$")
_HEX8 = re.compile(r"^(?:0[xX])?([0-9A-Fa-f]{1,2})$")

_TYPE_ALIAS = {
    "uint8_t": "uint8", "int8": "sint8", "int8_t": "sint8", "sint8_t": "sint8",
    "uint16_t": "uint16", "int16": "sint16", "int16_t": "sint16", "sint16_t": "sint16",
    "uint32_t": "uint32", "int32": "sint32", "int32_t": "sint32", "sint32_t": "sint32",
}


def norm_msg_id(v):
    """'801' / '0x801' / '0x0801' → '0x0801'；非法返回 None。"""
    s = text(v)
    m = _HEX16.match(s)
    if not m:
        return None
    return "0x%04X" % int(m.group(1), 16)


def norm_enum_value(v):
    """'1' / '0x1' → '0x01'；非法返回 None。"""
    s = text(v)
    m = _HEX8.match(s)
    if not m:
        return None
    return "0x%02X" % int(m.group(1), 16)


def norm_type_name(v):
    """子项类型别名 → 规范名；带 [n] 后缀保留后缀。"""
    s = first(v) if isinstance(v, list) else text(v)
    if not s:
        return None
    base, _, suffix = s.partition("[")
    fixed = _TYPE_ALIAS.get(base.strip().lower())
    if not fixed:
        return None
    return fixed + ("[" + suffix if suffix else "")


# ------------------------------------------------------------------ 修复计划
class Plan(object):
    """一次 fix 的计划：逐项记录要写什么，dry-run 时只打印。"""

    def __init__(self):
        self.field_updates = {}     # (table_id, field_id) -> 新的完整字段 JSON
        self.record_updates = {}    # table_id -> {record_id: {字段: 值}}
        self.notes = []             # 人工提示（不修）
        self.counts = {}            # 修复项 → 数量

    def add_field(self, table_id, field_id, field_json, label):
        if (table_id, field_id) not in self.field_updates:
            self.field_updates[(table_id, field_id)] = field_json
        self._bump(label)

    def add_record(self, table_id, record_id, cells, label):
        self.record_updates.setdefault(table_id, {}).setdefault(record_id, {}).update(cells)
        self._bump(label)

    def _bump(self, label):
        self.counts[label] = self.counts.get(label, 0) + 1

    def empty(self):
        return not self.field_updates and not self.record_updates

    def summary(self):
        if not self.counts:
            return "无可自动修复项"
        return "；".join("%s ×%d" % (k, v) for k, v in sorted(self.counts.items()))


# ------------------------------------------------------------------ 各项修复
def _fix_select_options(cfg, raw, plan):
    """R3：记录里的值不在 select 字段选项内 → 补选项。

    安全策略（2026-11-09 事故复盘）：选项基集必须用 +field-search-options 取全量，
    不能用 field-get 的 options（会被截断到 50 条，全量 PUT 会删掉未返回的选项并清空记录值）。
    """
    bt = cfg["source"]["base_token"]
    for role, meta in cfg["tables"].items():
        tid = meta["id"]
        try:
            fields = bitable.list_fields(bt, tid)
        except bitable.BitableError:
            continue
        records = raw.get(role) or []
        for f in fields:
            if f.get("type") != "select":
                continue
            fname = f["name"]
            used = set()
            for r in records:
                vals = r.get(fname)
                for v in (vals if isinstance(vals, list) else []):
                    if isinstance(v, str) and v.strip():
                        used.add(v.strip())
            if not used:
                continue
            try:
                base = [o["name"] for o in bitable.field_options_all(bt, tid, f["id"])]
            except Exception:
                plan.notes.append(
                    "%s.%s 无法枚举全部选项（+field-search-options 失败），跳过，避免误删选项"
                    % (meta.get("name", role), fname))
                continue
            missing = sorted(used - set(base))
            if not missing:
                continue
            merged = base + missing
            body = {"name": fname, "type": "select",
                    "multiple": bool(f.get("multiple")),
                    "options": [{"name": n} for n in merged]}
            plan.add_field(tid, f["id"], body,
                           "R3 补选项 %s.%s(+%d)" % (meta.get("name", role), fname, len(missing)))


def _fix_msg_id(cfg, raw, plan):
    """R1：接口行消息id 统一 '0xNNNN'。"""
    meta = cfg["tables"].get("service_interface")
    if not meta:
        return
    F = schema.from_records(meta, raw.get("service_interface") or [])
    for r in raw.get("service_interface") or []:
        if not first(r.get(F["interface_name"])):      # 接口名空 = 预留服务行，无消息id
            continue
        cur = text(r.get(F["msg_id"]))
        if not cur:
            continue
        fixed = norm_msg_id(cur)
        if fixed is None:
            plan.notes.append("接口 %s 消息id 无法解析: %r（需人工修）"
                              % (first(r.get(F["interface_name"])), cur))
            continue
        if fixed != cur:
            plan.add_record(meta["id"], r["record_id"], {F["msg_id"]: fixed},
                            "R1 消息id 规范化")


def _fix_enum_value(cfg, raw, plan):
    """R2：枚举值子项的「值」统一 '0xNN'。"""
    meta = cfg["tables"].get("data_structure_item")
    if not meta:
        return
    F = schema.from_records(meta, raw.get("data_structure_item") or [])
    enum_type = schema.split_value(meta, "enum_value")
    for r in raw.get("data_structure_item") or []:
        if first(r.get(F["item_type"])) != enum_type:
            continue
        cur = text(r.get(F["value"]))
        if not cur:
            continue
        fixed = norm_enum_value(cur)
        if fixed is None:
            plan.notes.append("枚举值 %s 的值无法解析: %r（需人工修）"
                              % (first(r.get(F["name"])), cur))
            continue
        if fixed != cur:
            plan.add_record(meta["id"], r["record_id"], {F["value"]: fixed}, "R2 枚举值规范化")


def _fix_type_alias(cfg, raw, plan):
    """R4：子项类型别名规范化（uint8_t → uint8 等）。"""
    meta = cfg["tables"].get("data_structure_item")
    if not meta:
        return
    F = schema.from_records(meta, raw.get("data_structure_item") or [])
    enum_type = schema.split_value(meta, "enum_value")
    for r in raw.get("data_structure_item") or []:
        if first(r.get(F["item_type"])) == enum_type:
            continue
        cur = first(r.get(F["item_type"]))
        if not cur:
            continue
        fixed = norm_type_name(cur)
        if fixed and fixed != cur:
            plan.add_record(meta["id"], r["record_id"], {F["item_type"]: [fixed]},
                            "R4 类型别名规范化")


def _fix_backlinks(cfg, raw, plan):
    """R5：服务行与接口行的归属关系人工确认提示。

    合并表后旧的双向字段「接口列表 / 所属服务」已取消，只剩单向自关联 归属服务，
    没有可确定性推导的反链差异，故本项只保留占位，不做写操作。
    """
    return


# ------------------------------------------------------------------ 执行
def build_plan(cfg, raw):
    plan = Plan()
    _fix_msg_id(cfg, raw, plan)
    _fix_enum_value(cfg, raw, plan)
    _fix_type_alias(cfg, raw, plan)
    _fix_select_options(cfg, raw, plan)
    _fix_backlinks(cfg, raw, plan)
    return plan


def apply_plan(cfg, plan):
    """真正写表：字段 PUT（select 选项）、记录批量更新。返回 (字段数, 记录数)。"""
    bt = cfg["source"]["base_token"]
    nf = 0
    for (tid, fid), body in plan.field_updates.items():
        bitable.field_update(bt, tid, fid, body)
        nf += 1
    nr = 0
    for tid, updates in plan.record_updates.items():
        if updates:
            nr += bitable.record_update_batch(bt, tid, updates)
    return nf, nr
