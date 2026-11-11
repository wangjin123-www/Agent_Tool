# -*- coding: utf-8 -*-
"""从命令行参数拼 edit_request.json（替代 HTML 表单，全部靠脚本传参）。

每个 --param / --member / --value 是一个逗号分隔的 key=value 串：
    --param name=mode,type=enum:SMOKE_TEST_ENUM,io=IN,desc=模式
    --member byte=0-1B,bit=,name=mode,type=uint16,desc=模式
    --value value=0x00,c_name=SMOKE_A,desc=冒烟A
    --set K=0x0802
值内不要带英文逗号；带逗号的描述请改用 edit apply <json> 传文件。
"""
import json
import os

from ..common import conf


def kv(spec):
    """'name=mode,type=uint8' → {'name': 'mode', 'type': 'uint8'}"""
    out = {}
    for part in (spec or "").split(","):
        part = part.strip()
        if not part:
            continue
        if "=" not in part:
            raise ValueError("参数片段缺少 '=': %r（应写成 key=value 逗号分隔）" % part)
        k, v = part.split("=", 1)
        out[k.strip()] = v.strip()
    return out


def add_interface(args):
    params = [kv(p) for p in (args.param or [])]
    for p in params:
        for req in ("name", "type"):
            if not p.get(req):
                raise ValueError("--param 缺 %s: %r" % (req, p))
        p.setdefault("io", "IN")
        p.setdefault("desc", "")
    return {"kind": "add_interface",
            "service": args.service, "direction": args.direction,
            "name": args.name, "if_type": args.if_type, "desc": args.desc or "",
            "tx_type": args.tx_type, "msg_id": args.msg_id,
            "pair_id": args.pair_id or "", "transport": args.transport,
            "qos": args.qos, "params": params}


def add_struct(args):
    members = [kv(m) for m in (args.member or [])]
    for m in members:
        for req in ("byte", "name", "type"):
            if not m.get(req):
                raise ValueError("--member 缺 %s: %r" % (req, m))
        m.setdefault("bit", "")
        m.setdefault("desc", "")
    return {"kind": "add_struct", "name": args.name, "service": args.service,
            "namespace": args.namespace, "desc": args.desc or "",
            "members": members}


def add_enum(args):
    values = [kv(v) for v in (args.value or [])]
    for v in values:
        for req in ("value", "c_name"):
            if not v.get(req):
                raise ValueError("--value 缺 %s: %r" % (req, v))
        v.setdefault("desc", "")
    return {"kind": "add_enum", "name": args.name,
            "msg_id": args.msg_id, "values": values}


def add_enum_value(args):
    v = kv(args.value)
    for req in ("value", "c_name"):
        if not v.get(req):
            raise ValueError("--value 缺 %s: %r" % (req, v))
    v.setdefault("desc", "")
    return {"kind": "add_enum_value", "name": args.name,
            "msg_id": args.msg_id, "value": v}


def delete_enum_value(args):
    return {"kind": "delete_enum_value", "name": args.name,
            "c_name": args.c_name}


def mod_interface(args):
    fields = {}
    for s in (args.set or []):
        item = kv(s)
        if len(item) != 1:
            raise ValueError("--set 只接受一个 key=value: %r" % s)
        fields.update(item)
    if not fields:
        raise ValueError("--set 至少要给一个列值，如 --set K=0x0802")
    return {"kind": "mod_interface", "name": args.name, "fields": fields}


def delete_interface(args):
    """级联删：接口 + 对端 + 只被这批接口引用的 struct/enum（展开在 apply 内）。"""
    return {"kind": "delete_interface", "name": args.name}


def save_request(ops, path=None):
    path = path or os.path.join(conf.ensure_output(), "edit_request.json")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump({"ops": ops}, f, ensure_ascii=False, indent=2)
    return path
