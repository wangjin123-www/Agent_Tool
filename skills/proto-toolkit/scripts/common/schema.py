# -*- coding: utf-8 -*-
"""字段语义解析层：config 的 semantic_key ↔ 线上真实字段名。

设计
----
脚本里不写任何表内字段名，只写语义键（如 `msg_id` / `arr_len`）；
真实字段名统一声明在 config 的 `tables.<role>.fields`：
    "msg_id": ["消息id(16进制)", "消息id"]      # 候选名，按顺序兜底

两个用途：
  1. 运行时：`declared()` / `pick_field()` 提供候选名列表，取值时逐个兜底，
     字段改名只要命中任一候选就不会静默读到空；
  2. 体检时：`resolve_table()` 拿线上 `+field-list` 结果核对声明，
     声明的名字都不存在时尝试按「名字包含关系」唯一推断，供 doctor --fix 回写。

禁止在脚本里硬编码字段名——一律走本模块。
"""
from . import bitable

_LEVEL_ERROR = "ERROR"
_LEVEL_WARN = "WARN"


class SchemaError(RuntimeError):
    pass


# ------------------------------------------------------------------ 声明读取
def declared(meta, key):
    """config 里某语义键的候选字段名列表（str → [str]，list 原样）。"""
    fields = meta.get("fields") or {}
    if key not in fields:
        raise SchemaError("表「%s」的 fields 未声明语义键: %s（已声明: %s）"
                          % (meta.get("name", "?"), key,
                             ", ".join(sorted(fields)) or "无"))
    v = fields[key]
    return [v] if isinstance(v, str) else list(v)


def declared_any(meta, key):
    """同上，但未声明时返回空列表（用于可选字段）。"""
    try:
        return declared(meta, key)
    except SchemaError:
        return []


def split_value(meta, key):
    """取 split 的拆分值（如 enum_value=枚举值）；缺失直接报错，不用兜底常量。

    兜底会让「表里改了选项名」变成静默错分——宁可失败也不猜。
    """
    v = (meta.get("split") or {}).get(key)
    if not v:
        raise SchemaError("表「%s」的 split.%s 未配置（分流值不写默认值）"
                          % (meta.get("name", "?"), key))
    return v


def pick_field(record, meta, key):
    """按语义键取值：候选名依次兜底，返回 (值, 实际命中字段名)。

    未声明该键时返回 (None, "")。
    """
    for n in declared_any(meta, key):
        if n in record and record.get(n) not in (None, "", []):
            return record.get(n), n
    return None, ""


def field_name(meta, key):
    """语义键 → 首选字段名（写入时用；运行时不保证该名线上存在，写入前建议体检）。"""
    cands = declared(meta, key)
    return cands[0] if cands else ""


def from_records(meta, rows):
    """按实际记录键解析语义键 → 真实字段名（不额外调 API）。

    记录里包含该表全部列（空值列也在），因此改名后能就地纠正，无需联网体检。
    某键的候选名全都没出现（表为空等）时退回首选名。
    """
    keys = set()
    for r in rows or []:
        keys.update(r.keys())
    keys.discard("record_id")
    out = {}
    for skey in (meta.get("fields") or {}):
        cands = declared(meta, skey)
        out[skey] = next((c for c in cands if c in keys), cands[0])
    return out


# ------------------------------------------------------------------ 线上快照
def online_fields(base_token, tables):
    """读取各表线上字段：{role: [field dict]}。field dict 含 name/type/id/link_table/options。"""
    out = {}
    for role, meta in (tables or {}).items():
        tid = meta.get("id")
        if not tid:
            continue
        out[role] = bitable.list_fields(base_token, tid)
    return out


# ------------------------------------------------------------------ 核对与推断
def _score(old, new):
    """候选推断打分：包含关系 > 前后缀公共长度。不相关返回 0。"""
    if not old or not new:
        return 0
    if old == new:
        return 100
    if old in new or new in old:
        return 60 + min(len(old), len(new))
    common = 0
    for a, b in zip(old, new):
        if a != b:
            break
        common += 1
    return common if common >= 2 else 0


def resolve_table(meta, fields):
    """核对一张表的字段声明。

    返回 (resolved, issues, suggestions)：
      resolved    {semantic_key: 实际字段名}
      issues      [(level, key, message)]
      suggestions {semantic_key: 推断出的新字段名}（供 --fix 回写）
    """
    have = {f["name"]: f for f in fields}
    resolved, issues, suggestions = {}, [], {}
    taken = set()

    for key in (meta.get("fields") or {}):
        cands = declared(meta, key)
        hit = next((c for c in cands if c in have), None)
        if hit:
            resolved[key] = hit
            taken.add(hit)
            if hit != cands[0]:
                issues.append((_LEVEL_WARN, key,
                               "首选名「%s」不在表里，已按候选回退到「%s」（建议 doctor --fix 更新首选名）"
                               % (cands[0], hit)))
            continue

        # 声明的名字全都不存在：按命名包含关系唯一推断
        pool = [n for n in have if n not in taken]
        scored = sorted(((_score(cands[0], n), n) for n in pool), reverse=True)
        best = [n for sc, n in scored if sc > 0][:2]
        if len(best) == 1:
            resolved[key] = best[0]
            suggestions[key] = best[0]
            taken.add(best[0])
            issues.append((_LEVEL_ERROR, key,
                           "字段「%s」线上不存在，疑似改名为「%s」（doctor --fix 可回写）"
                           % (cands[0], best[0])))
        else:
            issues.append((_LEVEL_ERROR, key,
                           "字段「%s」线上不存在，且无法唯一推断（现有字段：%s）"
                           % (" / ".join(cands), "、".join(sorted(have)) or "无")))

    # link 字段：类型与目标表必须对得上
    for key, target_role in (meta.get("links") or {}).items():
        fname = resolved.get(key) or next((c for c in declared_any(meta, key) if c in have), "")
        if not fname:
            continue
        f = have.get(fname)
        if not f:
            continue
        if f.get("type") != "link":
            issues.append((_LEVEL_ERROR, key,
                           "字段「%s」应为 link 类型，线上是 %s" % (fname, f.get("type"))))
            continue
        want = ((meta.get("_tables") or {}).get(target_role) or {}).get("id")
        got = f.get("link_table")
        if want and got and got != want:
            issues.append((_LEVEL_ERROR, key,
                           "字段「%s」指向 %s，config 里 %s 表是 %s"
                           % (fname, got, target_role, want)))

    # split：字段必须存在，且拆分值必须是其合法选项
    split = meta.get("split") or {}
    if split.get("field"):
        fname = resolved.get(split["field"], "")
        f = have.get(fname)
        if not f:
            issues.append((_LEVEL_ERROR, split["field"],
                           "split 字段「%s」线上不存在" % fname))
        else:
            opts = {o.get("name") for o in (f.get("options") or [])}
            for key in ("service", "interface", "struct", "enum", "enum_value"):
                val = split.get(key)
                if val and opts and val not in opts:
                    issues.append((_LEVEL_ERROR, split["field"],
                                   "split.%s=「%s」不是「%s」的选项（现有：%s）"
                                   % (key, val, fname, "、".join(sorted(opts)))))

    # label_key：必须已声明且线上存在
    lk = meta.get("label_key")
    if lk:
        fname = resolved.get(lk, "")
        if lk not in (meta.get("fields") or {}):
            issues.append((_LEVEL_ERROR, lk, "label_key 未在 fields 里声明"))
        elif not fname or fname not in have:
            issues.append((_LEVEL_ERROR, lk,
                           "label_key 指向的字段「%s」线上不存在" % fname))

    return resolved, issues, suggestions


def resolve_platform(cfg, fields_by_role=None, base_token=None):
    """核对整平台：返回 (resolved{role:{key:name}}, issues[(level,role,key,msg)], suggestions{role:{key:name}})。"""
    base_token = base_token or cfg["source"]["base_token"]
    tables = cfg["tables"]
    for role, meta in tables.items():
        meta["_tables"] = tables                 # links 校验需要目标表 id
    if fields_by_role is None:
        fields_by_role = online_fields(base_token, tables)

    resolved, issues, suggestions = {}, [], {}
    for role, meta in tables.items():
        r, iss, sug = resolve_table(meta, fields_by_role.get(role) or [])
        resolved[role] = r
        suggestions[role] = sug
        issues += [(_lvl, role, key, msg) for _lvl, key, msg in iss]
    return resolved, issues, suggestions


# ------------------------------------------------------------------ 降级规则核对
def formula_text(meta, fields):
    """该表所有 formula 字段的表达式拼一起（用于校验降级规则子串是否还成立）。"""
    return "\n".join(f.get("expression") or "" for f in fields if f.get("type") == "formula")


def check_degraded(cfg, fields_by_role):
    """校验 check_rules.degraded 的子串仍能在对应表的检测公式里找到。

    公式改写会让降级规则静默失效（gen 突然被阻断），故必须体检。
    """
    rules = (cfg.get("check_rules") or {}).get("degraded") or {}
    issues = []
    for role, patterns in rules.items():
        if role.startswith("_"):
            continue
        meta = cfg["tables"].get(role)
        if not meta:
            issues.append((_LEVEL_ERROR, role, "degraded",
                           "check_rules.degraded 指向未配置的表角色 %s" % role))
            continue
        expr = formula_text(meta, fields_by_role.get(role) or [])
        for p in patterns:
            if p not in expr:
                issues.append((_LEVEL_ERROR, role, "degraded",
                               "降级规则「%s」在该表检测公式里已找不到（公式被改写，"
                               "会导致 gen 误阻断，请同步 config）" % p))
    return issues
