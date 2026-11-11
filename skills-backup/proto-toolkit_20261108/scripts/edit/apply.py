# -*- coding: utf-8 -*-
"""把 edit_request.json 落到飞书表（AI 修订规则 17/25/26/27）。

流程：读表定位 → 计划（预览）→ [确认] 写表 → 自动 sync（链接重算 + 服务块合并）
→ parse 刷新 protocol.json。
默认 dry-run 只打印计划不写表；--yes 才执行。

请求契约（ops 数组，顺序执行，同一次请求内的加 struct/枚举先于加接口落表）：
  {"kind":"add_interface","service","direction":"SOC→MCU|MCU→SOC","name","if_type",
   "desc","tx_type","msg_id","pair_id","transport","qos",
   "params":[{"name","type","io","desc"}]}
  {"kind":"add_struct","name","service","namespace","desc",
   "members":[{"byte":"0-3B","bit":"","name","type","desc"}]}
  {"kind":"add_enum","name","msg_id","values":[{"value":"0x00","c_name","desc"}]}
  {"kind":"mod_interface","name","fields":{"K":"0x8803","F":"新描述"}}   # F G H J K L M N O P Q
  {"kind":"clear_params","name","count":N}   # 规则26：清空该接口第 2~N 个参数行的 N~Q（保留行不删）
  {"kind":"delete_interface","name"}          # 级联删：SI 接口块 + 对端 + 专属 struct/enum

删除（delete_interface）是唯一会 dim-delete 行的 op，执行顺序固定放在最后、
按行号自下而上删（行号不会互相错位）。级联范围：
  1. 目标接口自身 SI 行块（接口行 + 其全部参数行）
  2. 关联 id 指向的对端接口（否则删完就留 S05 悬空配对）
  3. 只被这些接口引用的 struct（DS 整块）与枚举（PE 整块）
仍被其他接口引用的 struct/enum 保留，只在计划里提示。
"""
import json
import re

from ..common import conf, feishu
from ..parse import parse_protocol
from ..parse.sheet_reader import hex_int, parse_byte_index
from ..check.semantics import resolve_type

_MOD_COLS = conf.MOD_INTERFACE_COLUMNS   # 与写表前预检共用同一张表（见 common/conf.py）


_SCALARS = {"uint8", "uint16", "uint32", "uint8[]"}
_INLINE_VALUES = re.compile(r"(?:^|[，,；;/\s])(?:0x)?[0-9A-Fa-f]{1,4}\s*[=:：]")


def _inline_desc(text):
    return len(_INLINE_VALUES.findall(text or "")) >= 2


def load_request(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _last_used_row(rows):
    last = 0
    for i, line in enumerate(rows, 1):
        if any(feishu.cell_text(c) for c in line):
            last = i
    return last


def _si_block(si_rows, proto, service_name):
    """返回 (service, block_begin, block_end)。分节行已废弃，块边界=服务首行~下一服务前。"""
    for i, s in enumerate(proto.services):
        if s.name == service_name:
            begin = s.si_row
            end = (proto.services[i + 1].si_row - 1) if i + 1 < len(proto.services) \
                else _last_used_row(si_rows)
            return s, begin, end
    raise ValueError("服务不存在: %s" % service_name)


def _si_insert_row(si_rows, proto, begin, end, direction):
    """无分节行时的插入锚点。

    SOC→MCU：插在服务块内第一条 MCU→SOC 接口之前（没有则块尾），保持 SOC 段在前。
    MCU→SOC：一律块尾。
    接口方向取解析结果（msg_id bit15 真源），参数行随接口整组下移。
    """
    by_row = {itf.si_row: itf for itf in proto.all_interfaces() if itf.si_row}
    first_mcu = None
    for r in range(begin + 1, end + 1):
        e = feishu.cell_text(feishu.cell_at(si_rows, r, "E"))
        if not e or e.startswith("▶"):
            continue
        itf = by_row.get(r)
        if itf is None:
            continue
        if itf.direction == "MCU_TO_SOC" and first_mcu is None:
            first_mcu = r
            break
    if direction == "SOC→MCU" and first_mcu is not None:
        return first_mcu
    return end + 1


def _itf_rows(cfg, si_rows, proto, itf):
    """接口在 SI 的完整行块 [起, 止]：接口行 + 其后全部参数行。

    终止条件：下一个接口行 / 分节行 / 服务块首行，或整表末尾。
    参数行之间若有空行也一并纳入（删除是连续区间，留下半截参数行会变成孤儿）。
    """
    start = itf.si_row
    if not start:
        raise ValueError("接口 %s 缺 SI 行号，无法定位" % itf.name)
    later = [o.si_row for o in proto.all_interfaces() if o.si_row and o.si_row > start]
    limit = min(later) if later else len(si_rows) + 1
    end = start
    for r in range(start + 1, limit):
        if feishu.cell_text(feishu.cell_at(si_rows, r, "E")):
            break                       # 下一个接口行或分节行
        if feishu.cell_text(feishu.cell_at(si_rows, r, "N")) \
           or feishu.cell_text(feishu.cell_at(si_rows, r, "O")):
            end = r
    return start, end


def _struct_rows(ds_rows, proto, st):
    """struct 在 DS 的完整行块 [起, 止]：首行到下一个 struct 之前（尾部空行裁掉）。"""
    start = st.ds_row
    if not start:
        raise ValueError("struct %s 缺 DS 行号，无法定位" % st.name)
    later = [s.ds_row for s in proto.structs if s.ds_row and s.ds_row > start]
    limit = min(later) - 1 if later else _last_used_row(ds_rows)
    return start, max(start, min(limit, _last_used_row(ds_rows)))


def _enum_rows(pe_rows, proto, en):
    """枚举在 PE 的完整行块 [起, 止]。"""
    start = en.pe_row
    if not start:
        raise ValueError("枚举 %s 缺 PE 行号，无法定位" % en.name)
    later = [e.pe_row for e in proto.enums if e.pe_row and e.pe_row > start]
    limit = min(later) - 1 if later else _last_used_row(pe_rows)
    return start, max(start, min(limit, _last_used_row(pe_rows)))


def _enum_hard_end(pe_rows, proto, en):
    """枚举块物理末行：到下一个枚举首行前，含块内缓冲空行。"""
    later = [e.pe_row for e in proto.enums if e.pe_row and e.pe_row > en.pe_row]
    return (min(later) - 1) if later else len(pe_rows)



class Plan:
    def __init__(self):
        self.inserts = []       # (sheet_key, 原始插入点, count, why) — mod 位移按原始点算
        self.insert_final = []  # (sheet_key, 最终落位行, count) — 执行插行用
        self.writes = []        # feishu writes dict
        self.unmerges = []      # (sheet_key, "A2:F5") — 重做合并前先拆
        self.merges = []        # (sheet_key, "A2:F5")
        self.deletes = []       # (sheet_key, 起始行, 行数, why) — 统一在最后自下而上删
        self.notes = []

    def add_write(self, cfg, sheet_key, row, col, value):
        if value in ("", None):
            return
        self.writes.append({
            "sheet_id": cfg["sheets"][sheet_key]["id"],
            "range": "%s%d" % (col, row),
            "cells": [[{"value": value}]],
        })

    def clear_cell(self, cfg, sheet_key, row, col):
        self.writes.append({
            "sheet_id": cfg["sheets"][sheet_key]["id"],
            "range": "%s%d" % (col, row),
            "cells": [[{"value": ""}]],
        })


def build_plan(cfg, req, rows=None, proto=None):
    """纯计算：不碰表。返回 (plan, warnings)。rows/proto 可传入复用已读快照。"""
    plan = Plan()
    warns = []
    rows = rows or {
        "si": feishu.read(cfg, "service_interface", "Q"),
        "ds": feishu.read(cfg, "data_structure", "K"),
        "pe": feishu.read(cfg, "parameter_enum", "E"),
    }
    proto = proto or parse_protocol(cfg, rows)
    # 同请求内新定义的 struct/enum 名（参数引用检查的白名单，避免同包定义误报）
    new_defs = set()
    for _op in req["ops"]:
        if _op["kind"] in ("add_struct", "add_enum"):
            new_defs.add(_op["name"])

    # 加 struct / 加枚举先做（接口参数可能引用）
    ds_last = _last_used_row(rows["ds"])
    pe_last = _last_used_row(rows["pe"])
    si_pending = []             # (op, insert_at) 位置等 struct/枚举行数算完再定
    mod_pending = []            # (target, op) mod 写入等插入点算完再统一补位移
    clear_pending = []          # (target, op) 同上
    delete_pending = []         # (target, op) 级联删，最后统一自下而上执行
    for op in req["ops"]:
        k = op["kind"]
        if k == "add_struct":
            if proto.find_struct(op["name"]):
                raise ValueError("struct 已存在: %s" % op["name"])
            r0 = ds_last + 1
            closed = open_bytes = 0
            for i, m in enumerate(op["members"]):
                r = r0 + i
                span = parse_byte_index(m["byte"])
                if span is None:
                    raise ValueError("成员 %s.%s 字节区间非法: %r" % (op["name"], m["name"], m["byte"]))
                bs, be, is_open = span
                if is_open:
                    open_bytes = bs
                else:
                    closed = max(closed, be + 1)
                plan.add_write(cfg, "data_structure", r, "G", m["byte"])
                plan.add_write(cfg, "data_structure", r, "H", m.get("bit", ""))
                plan.add_write(cfg, "data_structure", r, "I", m["name"])
                plan.add_write(cfg, "data_structure", r, "J", m["type"])
                plan.add_write(cfg, "data_structure", r, "K", m.get("desc", ""))
            n = len(op["members"])
            size = str(closed) + "+N" if open_bytes else str(closed)
            plan.add_write(cfg, "data_structure", r0, "A", op.get("service", ""))
            plan.add_write(cfg, "data_structure", r0, "B", op.get("namespace", ""))
            plan.add_write(cfg, "data_structure", r0, "C", op["name"])
            plan.add_write(cfg, "data_structure", r0, "D", op.get("desc", ""))
            plan.add_write(cfg, "data_structure", r0, "E", "struct")
            plan.add_write(cfg, "data_structure", r0, "F", size)
            # DS struct 块不做 A~F 矩形合并（会吃掉首行 C/D/E/F 值，parse 无法开新块）；
            # 现有表形态=首行带值、成员行留空
            ds_last = r0 + n - 1
            plan.notes.append("DS 追加 struct %s（%d 成员，行%d-%d，Size=%s）"
                              % (op["name"], n, r0, ds_last, size))
        elif k == "add_enum":
            if proto.find_enum(op["name"]):
                raise ValueError("枚举已存在: %s" % op["name"])
            if not op.get("msg_id"):
                raise ValueError("枚举 %s 缺消息 id（PE E 列反向链接依赖它）" % op["name"])
            r0 = pe_last + 1
            for i, v in enumerate(op["values"]):
                r = r0 + i
                plan.add_write(cfg, "parameter_enum", r, "B", v["value"])
                plan.add_write(cfg, "parameter_enum", r, "C", v["c_name"])
                plan.add_write(cfg, "parameter_enum", r, "D", v.get("desc", ""))
                plan.add_write(cfg, "parameter_enum", r, "E", op["msg_id"])
            n = len(op["values"])
            plan.add_write(cfg, "parameter_enum", r0, "A", op["name"])
            if n > 1:
                plan.merges.append(("parameter_enum", "A%d:A%d" % (r0, r0 + n - 1)))
            pe_last = r0 + n - 1
            plan.notes.append("PE 追加枚举 %s（%d 值，行%d-%d → 消息 %s）"
                              % (op["name"], n, r0, pe_last, op["msg_id"]))
        elif k == "add_enum_value":
            en = proto.find_enum(op["name"])
            if en is None:
                raise ValueError("枚举不存在: %s" % op["name"])
            start = en.pe_row
            hard_end = _enum_hard_end(rows["pe"], proto, en)
            last_val = start
            for r in range(start, hard_end + 1):
                if feishu.cell_text(feishu.cell_at(rows["pe"], r, "B")) \
                   or feishu.cell_text(feishu.cell_at(rows["pe"], r, "C")):
                    last_val = r
            # 优先填块内缓冲空行（解析层跳过全空行），没有才在块尾插一行并续 A 列合并
            target = next((r for r in range(last_val, hard_end + 1)
                           if not any(feishu.cell_text(feishu.cell_at(rows["pe"], r, c))
                                      for c in "ABCDE")), None)
            if target is None:
                target = last_val + 1
                plan.inserts.append(("parameter_enum", target, 1,
                                     "枚举 %s 块尾 +1 行" % en.name))
                plan.insert_final.append(("parameter_enum", target, 1))
                plan.unmerges.append(("parameter_enum", "A%d:A%d" % (start, last_val)))
                plan.merges.append(("parameter_enum", "A%d:A%d" % (start, target)))
            v = op["value"]
            mid = op.get("msg_id") or feishu.cell_text(feishu.cell_at(rows["pe"], last_val, "E"))
            plan.add_write(cfg, "parameter_enum", target, "B", v["value"])
            plan.add_write(cfg, "parameter_enum", target, "C", v["c_name"])
            plan.add_write(cfg, "parameter_enum", target, "D", v.get("desc", ""))
            plan.add_write(cfg, "parameter_enum", target, "E", mid)
            plan.notes.append("PE 枚举 %s 追加取值 %s %s（行%d → 消息 %s）"
                              % (en.name, v["value"], v["c_name"], target, mid))
        elif k == "delete_enum_value":
            en = proto.find_enum(op["name"])
            if en is None:
                raise ValueError("枚举不存在: %s" % op["name"])
            start = en.pe_row
            hard_end = _enum_hard_end(rows["pe"], proto, en)
            target = next((r for r in range(start, hard_end + 1)
                           if feishu.cell_text(feishu.cell_at(rows["pe"], r, "C"))
                           == op["c_name"]), None)
            if target is None:
                raise ValueError("枚举 %s 无取值 %s" % (op["name"], op["c_name"]))
            for col in "BCDE":
                plan.clear_cell(cfg, "parameter_enum", target, col)
            plan.notes.append("PE 枚举 %s 删除取值 %s（行%d，行保留为空）"
                              % (en.name, op["c_name"], target))
        elif k == "add_interface":
            si_pending.append(op)
        elif k == "mod_interface":
            target = None
            for itf in proto.all_interfaces():
                if itf.name == op["name"]:
                    target = itf
                    break
            if target is None:
                raise ValueError("接口不存在: %s" % op["name"])
            for col in op["fields"]:
                if col not in _MOD_COLS:
                    raise ValueError("改接口只允许列 %s，收到 %s" % (sorted(_MOD_COLS), col))
            mod_pending.append((target, op))
        elif k == "clear_params":
            target = next((i for i in proto.all_interfaces() if i.name == op["name"]), None)
            if target is None:
                raise ValueError("接口不存在: %s" % op["name"])
            clear_pending.append((target, op))
        elif k == "delete_interface":
            target = next((i for i in proto.all_interfaces() if i.name == op["name"]), None)
            if target is None:
                raise ValueError("接口不存在: %s" % op["name"])
            delete_pending.append((target, op))
        else:
            raise ValueError("未知 op.kind: %s" % k)

    # 加接口：先算全部插入点（原坐标），再按插入点降序执行并累计位移，行号不互相打架
    located = []
    for op in si_pending:
        svc, begin, end = _si_block(rows["si"], proto, op["service"])
        insert_at = _si_insert_row(rows["si"], proto, begin, end, op["direction"])
        located.append((insert_at, op, svc))

    # 插入点按从小到大处理：低位插入会把高位原始行整体下推。
    # 同一插入点内按 ops 顺序累计；不同插入点之间用 base_shift 累积低位插入总量。
    from itertools import groupby
    base_shift = 0
    for insert_at, group in groupby(sorted(located, key=lambda x: x[0]),
                                    key=lambda x: x[0]):
        shift = 0
        for _pos, op, svc in group:
            # 第一个参数与接口同行（表内既有写法）；只有第 2 个起才另起参数行
            n = max(1, len(op.get("params", [])))
            r = insert_at + base_shift + shift
            shift += n
            plan.inserts.append(("service_interface", insert_at, n,
                                 "%s.%s +%d 行（落位行%d）" % (op["service"], op["name"], n, r)))
            plan.insert_final.append(("service_interface", r, n))
            plan.add_write(cfg, "service_interface", r, "E", op["name"])
            plan.add_write(cfg, "service_interface", r, "F", op.get("desc", ""))
            plan.add_write(cfg, "service_interface", r, "G", op.get("if_type", ""))
            plan.add_write(cfg, "service_interface", r, "H", op.get("tx_type", ""))
            plan.add_write(cfg, "service_interface", r, "J", op["msg_id"])
            plan.add_write(cfg, "service_interface", r, "K", op.get("pair_id", ""))
            plan.add_write(cfg, "service_interface", r, "L", op.get("transport", ""))
            plan.add_write(cfg, "service_interface", r, "M", op.get("qos", ""))
            for i, p in enumerate(op.get("params", [])):
                pr = r + i                 # i=0 与接口同行，i>=1 才下移
                ptype = p["type"]
                base = ptype.split(":", 1)[1] if ":" in ptype else ptype
                if ptype.startswith("struct:"):
                    plan.add_write(cfg, "service_interface", pr, "N", base)   # 规则26：N=struct 名
                    plan.add_write(cfg, "service_interface", pr, "O", "struct")
                    # 规则26：struct 参数 P 留空
                elif ptype.startswith("enum:"):
                    plan.add_write(cfg, "service_interface", pr, "N", p["name"])
                    plan.add_write(cfg, "service_interface", pr, "O", "uint8")
                    en = proto.find_enum(base)
                    if en is not None and en.pe_row:
                        plan.writes.append(feishu.link_write(
                            cfg, "service_interface", "P%d" % pr, p.get("desc", ""),
                            "parameter_enum", "A%d" % en.pe_row))
                    else:
                        plan.add_write(cfg, "service_interface", pr, "P", p.get("desc", ""))
                        warns.append("参数 %s 引用枚举 %s 不在 PE，请先 add-enum 或分两步"
                                     % (p["name"], base))
                else:
                    plan.add_write(cfg, "service_interface", pr, "N", p["name"])
                    plan.add_write(cfg, "service_interface", pr, "O", ptype)
                    plan.add_write(cfg, "service_interface", pr, "P", p.get("desc", ""))
                    if _inline_desc(p.get("desc", "")):
                        warns.append("参数 %s 描述含内联值域，应改用 type=enum:枚举名"
                                     % p["name"])
                plan.add_write(cfg, "service_interface", pr, "Q", p.get("io", ""))
                if base not in _SCALARS and base not in new_defs \
                   and proto.find_struct(base) is None \
                   and proto.find_enum(base) is None:
                    warns.append("参数 %s 类型 %s 不在 DS/PE（确认本次请求已含定义或已存在）"
                                 % (p["name"], ptype))
            if "rr" in (op.get("if_type") or "") and not op.get("pair_id"):
                warns.append("接口 %s 是 method(rr) 但未填关联 id" % op["name"])
            params = op.get("params", [])
            if len(params) >= 2 and not any(p["type"].startswith("struct:") for p in params):
                warns.append("接口 %s 有 %d 个标量参数，规则 8/9/26 要求建 struct 单行"
                             "（先 add-struct，再用一个 type=struct:名 参数引用）"
                             % (op["name"], len(params)))
            mid = hex_int(op["msg_id"])
            if mid is None:
                warns.append("接口 %s 消息 id %r 解析失败" % (op["name"], op["msg_id"]))
            elif svc.id is not None and ((mid >> 8) & 0x7F) != svc.id:
                warns.append("接口 %s 消息 id 高 8bit 与服务 id 0x%02X 不符（check 会报错）"
                             % (op["name"], svc.id))
        base_shift += shift

    # 改接口：写入统一补插入位移（插入点在其上方/本行才下推），否则先插行后写会错格
    for target, op in mod_pending:
        shift_m = sum(cnt for _sk, pos, cnt, _w in plan.inserts
                      if _sk == "service_interface" and pos <= target.si_row)
        r_mod = target.si_row + shift_m
        for col, val in op["fields"].items():
            plan.add_write(cfg, "service_interface", r_mod, col, val)
        plan.notes.append("SI 修改接口 %s（行%d→落位行%d：%s）"
                          % (op["name"], target.si_row, r_mod,
                             ",".join("%s=%s" % kv for kv in sorted(op["fields"].items()))))

    # 清参数行（规则 26）：接口行被改成 struct 引用后，原参数行 N~Q 置空、行保留不删。
    # 接口行自身的 N/O 由同一请求的 mod_interface 覆盖，这里只清 P/Q 避免同格双写。
    mod_names = {op["name"] for _t, op in mod_pending}
    for target, op in clear_pending:
        shift_c = sum(cnt for _sk, pos, cnt, _w in plan.inserts
                      if _sk == "service_interface" and pos <= target.si_row)
        cleared = 0
        for p in target.params[:op.get("count", len(target.params))]:
            if p.si_row is None:
                continue
            cols = "PQ" if (p.si_row == target.si_row and target.name in mod_names) else "NOPQ"
            for col in cols:
                plan.clear_cell(cfg, "service_interface", p.si_row + shift_c, col)
            cleared += 1
        plan.notes.append("SI 清空接口 %s 的 %d 个参数行（行保留不删）" % (op["name"], cleared))

    # 级联删：接口 → 对端接口 → 只被这批接口引用的 struct / 枚举
    if delete_pending:
        _plan_delete(cfg, rows, proto, plan, delete_pending)
    return plan, warns


def _plan_delete(cfg, rows, proto, plan, delete_pending):
    """把 delete_interface 展开成 plan.deletes（原始行号，执行时统一补插入位移）。"""
    targets = []
    for target, _op in delete_pending:
        targets.append(target)
        peer = proto.find_interface(target.pair_id) if target.pair_id is not None else None
        if peer is not None:
            targets.append(peer)                 # 对端一起删，否则留 S05 悬空配对
    uniq, seen = [], set()
    for itf in targets:
        if id(itf) not in seen:
            seen.add(id(itf))
            uniq.append(itf)

    gone = {id(i) for i in uniq}
    refs_st, refs_en = {}, {}
    for s in proto.services:
        for itf in s.interfaces:
            for p in itf.params:
                kind, name = resolve_type(proto, p.type, p.name, p.enum_ref)
                if kind == "struct" and name:
                    refs_st.setdefault(name, []).append(itf)
                elif kind == "enum" and name:
                    refs_en.setdefault(name, []).append(itf)

    st_del, en_del = set(), set()
    for itf in uniq:
        for p in itf.params:
            kind, name = resolve_type(proto, p.type, p.name, p.enum_ref)
            if kind == "struct" and name and all(id(u) in gone for u in refs_st.get(name, [])):
                st_del.add(name)
            elif kind == "enum" and name and all(id(u) in gone for u in refs_en.get(name, [])):
                en_del.add(name)
            elif kind in ("struct", "enum") and name:
                plan.notes.append("%s %s 仍被其他接口引用，保留" % (kind, name))

    for itf in uniq:
        start, end = _itf_rows(cfg, rows["si"], proto, itf)
        plan.deletes.append(("service_interface", start, end - start + 1,
                             "接口 %s（SI 行%d-%d）" % (itf.name, start, end)))
    for name in sorted(st_del):
        st = proto.find_struct(name)
        if st is None:
            continue
        start, end = _struct_rows(rows["ds"], proto, st)
        plan.deletes.append(("data_structure", start, end - start + 1,
                             "struct %s（DS 行%d-%d）" % (name, start, end)))
    for name in sorted(en_del):
        en = proto.find_enum(name)
        if en is None:
            continue
        start, end = _enum_rows(rows["pe"], proto, en)
        plan.deletes.append(("parameter_enum", start, end - start + 1,
                             "枚举 %s（PE 行%d-%d）" % (name, start, end)))



def apply_ops(req, execute=True, force=False):
    """执行一次 edit 请求，返回结构化结果（终端打印 + 控制台 JSON 共用）。

    execute=True 直接写表（默认）；False 只出计划。写表后自动 sync + parse。
    """
    from ..rules import Ctx, run_precheck, precheck_blocked, run_sync

    cfg = conf.proto()
    ctx = Ctx(cfg)
    plan, warns = build_plan(cfg, req,
                             rows={"si": ctx.si, "ds": ctx.ds, "pe": ctx.pe},
                             proto=ctx.proto)

    print("══ 修改计划（%s）══" % ("执行" if execute else "预览 dry-run"))
    for note in plan.notes:
        print("  · " + note)
    for sheet_key, pos, cnt, why in plan.inserts:
        print("  ↑ 插入 %s 第%d行起 %d 行（%s）" % (sheet_key, pos, cnt, why))
    for sheet_key, pos, cnt, why in plan.deletes:
        print("  ✂ 删除 %s 第%d行起 %d 行（%s）" % (sheet_key, pos, cnt, why))
    for sheet_key, rng in plan.unmerges:
        print("  ⊞ 拆分 %s!%s" % (sheet_key, rng))
    for sheet_key, rng in plan.merges:
        print("  ⊟ 合并 %s!%s" % (sheet_key, rng))
    print("  ✎ 共 %d 格写入" % len(plan.writes))
    for w in warns:
        print("  ! " + w)

    result = {"execute": bool(execute),
              "plan": {"inserts": plan.inserts, "deletes": plan.deletes,
                       "merges": plan.merges, "writes": len(plan.writes),
                       "notes": plan.notes, "warnings": warns},
              "precheck": [], "blocked": False, "report": None, "sync": None}

    # 写表前预检：与 sync 共用同一套规则（scripts/rules/precheck.py）
    pre = run_precheck(ctx, req["ops"])
    if pre:
        print("\n══ 写表前预检（规则注册表）══")
        for level, code, msg in pre:
            print("  %s [%s] %s" % ("✗" if level == "ERR" else "!", code, msg))
    result["precheck"] = [{"level": lv, "code": c, "msg": m} for lv, c, m in pre]
    blocked = precheck_blocked(pre)
    result["blocked"] = blocked
    if blocked and not force:
        from ..common.log import Report
        from .. import report
        rep = Report("")
        for level, code, msg in pre:
            rep.add(level, code, msg)
        hit = report.emit(rep, ctx)
        if hit:
            print("\n检查报告 → %s" % hit)
        print("\n预检有 %d 项错误，拒绝落表（修正后重试；确要强写加 force）"
              % sum(1 for lvl, _c, _m in pre if lvl == "ERR"))
        result["report"] = hit
        return result

    if not execute:
        print("\n未写表（预览模式）")
        return result

    # 插行：位置自下而上；同一位置的多个插入必须倒序执行，
    # 否则后插的行会把先插的行顶下去，与 build_plan 里 r=pos+shift 的写格假设相反。
    for sheet_key, pos, cnt in sorted(plan.insert_final, key=lambda x: x[1]):
        feishu.insert_rows(cfg, sheet_key, pos, cnt)
    feishu.write_writes(cfg, plan.writes)
    for sheet_key, rng in plan.unmerges:
        feishu.unmerge(cfg, sheet_key, rng)
    for sheet_key, rng in plan.merges:
        feishu.merge(cfg, sheet_key, [rng])
    # 删行放最后：插入会整体下推行号，先按插入点补位移，再按行号自下而上删
    for sheet_key, pos, cnt, why in sorted(plan.deletes, key=lambda x: -x[1]):
        shift = sum(c for sk, p, c, _w in plan.inserts
                    if sk == sheet_key and p <= pos)
        feishu.delete_rows(cfg, sheet_key, pos + shift, cnt)
    print("\n══ 写表完成，自动跑完整校验（规则注册表）══")

    total, fixed, new_ctx = run_sync(dry=False, materialize=False)
    for msg in fixed:
        print("  → 已修 %s" % msg)
    code = total.dump()
    from .. import report
    hit = report.emit(total, new_ctx)
    if hit:
        print("\n检查报告（%d 错误 / %d 告警）→ %s"
              % (total.count("ERR"), total.count("WARN"), hit))
    result["report"] = hit
    result["exit_code"] = code
    result["sync"] = {"err": total.count("ERR"), "warn": total.count("WARN"),
                      "ok": total.count("OK"), "fixed": fixed}

    print("\n══ 刷新 protocol.json ══")
    p = parse_protocol()
    p.save()
    print("  revision=%s %s" % (p.source["revision"], p.counts()))
    result["revision"] = p.source["revision"]
    result["counts"] = p.counts()
    return result


def apply_request(path, execute=True, force=False):
    """命令行入口：返回退出码（0 正常 / 1 预检拦截或校验有错）。"""
    result = apply_ops(load_request(path), execute=execute, force=force)
    if result.get("blocked") and not force:
        return 1
    return result.get("exit_code", 0)

