# -*- coding: utf-8 -*-
"""协议查询：关键词 → 三表关联闭包（终端、控制台共用同一份结果契约）。

匹配对象（大小写不敏感）：
  接口    name 包含 / desc 包含 / msg_id 或 pair_id 命中关键词里的 id
  struct  name 包含
  枚举    name 包含 / 任一取值 c_name 包含

关系闭包（迭代到不动点，最多 4 轮）：
  接口 → 参数类型 struct:/enum: → 带出定义（struct 连带成员）
  接口 → pair_id → 对端接口
  struct/enum → 反查所有引用它的接口

每条记录都带 sheet + 行号 + 飞书跳转链接，屏幕上看到就能直接跳过去。
"""
import json
import os
import re

from ..common import conf, feishu
from ..check.semantics import resolve_type
from ..model import to_hex
from ..parse import parse_protocol

_HEX = re.compile(r"^0x[0-9a-f]+$")
_DEC = re.compile(r"^\d+$")
_HEX4 = re.compile(r"^[0-9a-f]{1,8}$")


def _ids_of(low):
    """关键词里可能的 id：'0x801' / '801' / '2049' → {2049}。纯字母名不算 id。"""
    if _HEX.match(low):
        return {int(low, 16)}
    if _DEC.match(low):
        return {int(low, 10)}
    if _HEX4.match(low) and any(c.isdigit() for c in low):
        return {int(low, 16)}
    return set()


def _hex(v):
    return to_hex(v) if v is not None else ""


def _jump(cfg, sheet_key, row):
    if not row:
        return ""
    return feishu.jump_url(cfg, "A%d" % row, sheet_key)


def _refs(proto):
    """反向索引：struct 名 / 枚举名 → 引用它的接口列表。"""
    st, en = {}, {}
    for s in proto.services:
        for itf in s.interfaces:
            for p in itf.params:
                kind, name = resolve_type(proto, p.type, p.name, p.enum_ref)
                if kind == "struct" and name:
                    st.setdefault(name, []).append(itf)
                elif kind == "enum" and name:
                    en.setdefault(name, []).append(itf)
    return st, en


def _owners(proto):
    """接口对象 id → 所属 Service。"""
    out = {}
    for s in proto.services:
        for itf in s.interfaces:
            out[id(itf)] = s
    return out


# ------------------------------------------------------------------ 对象序列化
def _param_obj(proto, p):
    kind, name = resolve_type(proto, p.type, p.name, p.enum_ref)
    d = {"name": p.name, "type": p.type, "desc": p.desc, "io": p.io,
         "row": p.si_row, "ref_kind": kind, "ref_name": name if kind in ("struct", "enum") else ""}
    return d


def _itf_obj(cfg, proto, owners, itf):
    svc = owners.get(id(itf))
    peer = proto.find_interface(itf.pair_id) if itf.pair_id is not None else None
    return {
        "name": itf.name,
        "service": svc.name if svc else "",
        "namespace": svc.namespace if svc else "",
        "direction": itf.direction,
        "section_dir": itf.section_dir,
        "msg_id": itf.msg_id, "msg_id_hex": _hex(itf.msg_id),
        "pair_id": itf.pair_id, "pair_id_hex": _hex(itf.pair_id),
        "type": itf.type, "tx_type": itf.tx_type,
        "transport": itf.transport, "qos": itf.qos,
        "desc": itf.desc,
        "sheet": "service_interface", "row": itf.si_row,
        "jump": _jump(cfg, "service_interface", itf.si_row),
        "params": [_param_obj(proto, p) for p in itf.params],
        "peer": ({"name": peer.name, "msg_id_hex": _hex(peer.msg_id),
                  "row": peer.si_row,
                  "jump": _jump(cfg, "service_interface", peer.si_row)}
                 if peer is not None else None),
        "close_peer": (not peer or peer.pair_id != itf.msg_id) if itf.pair_id is not None else None,
    }


def _struct_obj(cfg, st, users):
    return {
        "name": st.name, "service": st.service, "namespace": st.namespace,
        "desc": st.desc, "size": st.size,
        "fixed_bytes": st.fixed_bytes, "has_open": st.has_open,
        "sheet": "data_structure", "row": st.ds_row,
        "jump": _jump(cfg, "data_structure", st.ds_row),
        "members": [{"name": m.name, "type": m.type, "bit": m.bit,
                     "byte_start": m.byte_start, "byte_end": m.byte_end,
                     "open": m.open, "row": m.ds_row, "desc": m.desc,
                     "enum_ref": m.enum_ref}
                    for m in st.members],
        "used_by": [{"name": i.name, "msg_id_hex": _hex(i.msg_id), "row": i.si_row}
                    for i in users],
    }


def _enum_obj(cfg, en, users, proto):
    used_rows = {}
    for itf in users:
        for p in itf.params:
            kind, name = resolve_type(proto, p.type, p.name, p.enum_ref)
            if kind == "enum" and name == en.name:
                used_rows[id(itf)] = p.si_row
    return {
        "name": en.name, "sheet": "parameter_enum", "row": en.pe_row,
        "jump": _jump(cfg, "parameter_enum", en.pe_row),
        "items": [{"value": it.value, "value_hex": _hex(it.value), "c_name": it.c_name,
                   "desc": it.desc} for it in en.items],
        "used_by": [{"name": i.name, "msg_id_hex": _hex(i.msg_id), "row": i.si_row,
                     "param_row": used_rows.get(id(itf))}
                    for i in users],
    }


# ------------------------------------------------------------------ 主入口
def search(keyword, proto=None, cfg=None, limit=200):
    """返回结构化结果（可直接 json.dumps）。"""
    cfg = cfg or conf.proto()
    proto = proto or parse_protocol(cfg)
    kw = (keyword or "").strip()
    low = kw.lower()
    ids = _ids_of(low)

    owners = _owners(proto)
    st_refs, en_refs = _refs(proto)
    st_index = {s.name: s for s in proto.structs if s.name}
    en_index = {e.name: e for e in proto.enums if e.name}

    itfs, structs, enums = [], set(), set()
    if low:
        for s in proto.services:
            for itf in s.interfaces:
                if (low in itf.name.lower() or low in (itf.desc or "").lower()
                        or (itf.msg_id is not None and itf.msg_id in ids)
                        or (itf.pair_id is not None and itf.pair_id in ids)):
                    itfs.append(itf)
        for name in st_index:
            if low in name.lower():
                structs.add(name)
        for e in proto.enums:
            if low in (e.name or "").lower() or any(low in (it.c_name or "").lower()
                                                    for it in e.items):
                enums.add(e.name)

    # 关系闭包：接口 ↔ struct/枚举 互相带出，迭代到不动点
    have = {id(i) for i in itfs}
    for _round in range(4):
        changed = False
        for itf in list(itfs):
            for p in itf.params:
                kind, name = resolve_type(proto, p.type, p.name, p.enum_ref)
                if kind == "struct" and name in st_index and name not in structs:
                    structs.add(name)
                    changed = True
                elif kind == "enum" and name in en_index and name not in enums:
                    enums.add(name)
                    changed = True
        for name in list(structs) + list(enums):
            for itf in st_refs.get(name, []) + en_refs.get(name, []):
                if id(itf) not in have:
                    have.add(id(itf))
                    itfs.append(itf)
                    changed = True
        if not changed:
            break

    itf_objs = [_itf_obj(cfg, proto, owners, i) for i in itfs[:limit]]
    st_objs = [_struct_obj(cfg, st_index[n], st_refs.get(n, []))
               for n in sorted(structs)[:limit] if n in st_index]
    en_objs = [_enum_obj(cfg, en_index[n], en_refs.get(n, []), proto)
               for n in sorted(enums)[:limit] if n in en_index]

    return {
        "keyword": kw,
        "ids": sorted(ids),
        "summary": {"interfaces": len(itf_objs), "structs": len(st_objs),
                    "enums": len(en_objs),
                    "params": sum(len(i["params"]) for i in itf_objs)},
        "revision": proto.source.get("revision"),
        "sheets": {k: {"id": v["id"], "name": v["name"]} for k, v in cfg["sheets"].items()},
        "interfaces": itf_objs,
        "structs": st_objs,
        "enums": en_objs,
    }


def dump(result, path=None):
    """落盘（默认 output/query_result.json），返回路径。"""
    path = conf.output_path(path or os.path.join("output", "query_result.json"))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    return path


# ------------------------------------------------------------------ 终端渲染
def render_text(r):
    s = r["summary"]
    out = ["查询 %r → 接口 %d / struct %d / 枚举 %d（revision=%s）"
           % (r["keyword"], s["interfaces"], s["structs"], s["enums"], r["revision"])]

    for i in r["interfaces"]:
        out.append("")
        out.append("● 接口 %s.%s  %s  [%s]  SI!%s"
                   % (i["service"], i["name"], i["msg_id_hex"],
                      "MCU→SOC" if (i["msg_id"] or 0) & 0x8000 else "SOC→MCU",
                      i["row"]))
        out.append("    %s · %s · %s · %s"
                   % (i["desc"] or "-", i["type"] or "-",
                      i["transport"] or "-", i["qos"] or "-"))
        for k, label in (("msg_id_hex", "消息 id"), ("pair_id_hex", "关联 id")):
            if i[k]:
                out.append("    %s: %s" % (label, i[k]))
        if i["peer"]:
            out.append("    对端: %s %s（SI!%s）%s"
                       % (i["peer"]["name"], i["peer"]["msg_id_hex"], i["peer"]["row"],
                          "" if not i["close_peer"] else "  ← 对端未回指（S05）"))
        for p in i["params"]:
            ref = "  → %s:%s" % (p["ref_kind"], p["ref_name"]) if p["ref_name"] else ""
            out.append("      参数 %-14s %-18s %-4s SI!%s%s"
                       % (p["name"], p["type"], p["io"] or "-", p["row"] or "-", ref))

    for st in r["structs"]:
        out.append("")
        out.append("◆ struct %s（%sB%s）DS!%s  %s"
                   % (st["name"], st["fixed_bytes"], "+N" if st["has_open"] else "",
                      st["row"], st["desc"] or ""))
        for m in st["members"]:
            span = "%s-%sB" % (m["byte_start"], m["byte_end"]) if m["byte_end"] is not None \
                else "%s-NB" % m["byte_start"]
            out.append("      %-8s %-14s %-8s %s"
                       % (span, m["name"], m["type"], m["desc"] or ""))
        out.append("    被引用: %s" % (", ".join("%s %s" % (u["msg_id_hex"], u["name"])
                                                for u in st["used_by"]) or "无"))

    for en in r["enums"]:
        out.append("")
        out.append("◇ 枚举 %s（%d 值）PE!%s" % (en["name"], len(en["items"]), en["row"]))
        for it in en["items"]:
            out.append("      %-6s %-28s %s" % (it["value_hex"], it["c_name"], it["desc"] or ""))
        out.append("    被引用: %s" % (", ".join("%s %s" % (u["msg_id_hex"], u["name"])
                                                for u in en["used_by"]) or "无"))

    if not (r["interfaces"] or r["structs"] or r["enums"]):
        out.append("\n未命中任何接口 / struct / 枚举")
    return "\n".join(out)
