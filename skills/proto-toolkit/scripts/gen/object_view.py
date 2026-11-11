# -*- coding: utf-8 -*-
"""protocol.json dict → 对象视图适配（兼容 v2 生成器的对象接口）。

v4 的 protocol.json 是扁平 dict（services / interfaces / structs / enums），
而 v2 的生成器（如 lang_arxml）按对象属性访问（proto.structs[i].members[j].byte_start、
itf.msg_id、proto.all_interfaces()）。本模块提供一层只读包装，不改生成器即可复用。

字段映射（v4 → v2 对象）：
  interfaces[].msg_id  → Interface.msg_id / msg_id_hex
  interfaces[].service → 挂到 Service.interfaces（v2 是 services→interfaces 嵌套）
  members[].byte_start/byte_end/open/bit/base_type → Member 同名字段
  enums[].values       → Enum.items（EnumItem.value / value_hex / c_name / desc）
  errors[]             → 仅 v4 有；v2 生成器不消费（保留属性以防用到）
"""
from ..pull import to_hex


class _O(object):
    """通用只读对象：dict 键 → 属性。"""

    def __init__(self, d):
        self.__dict__.update(d)


class Param(_O):
    pass


class Member(_O):
    @property
    def nbytes(self):
        if self.open or self.byte_start is None or self.byte_end is None:
            return None
        return self.byte_end - self.byte_start + 1

    @property
    def bit(self):
        return self.__dict__.get("_bit", "")


class Struct(_O):
    @property
    def fixed_bytes(self):
        vals = [m.byte_end for m in self.members
                if not getattr(m, "open", False) and getattr(m, "byte_end", None) is not None]
        return (max(vals) + 1) if vals else 0

    @property
    def has_open(self):
        return any(getattr(m, "open", False) for m in self.members)


class EnumItem(_O):
    pass


class Enum(_O):
    @property
    def items(self):
        return self.values


class Interface(_O):
    @property
    def params(self):
        return self.__dict__.get("_params", [])

    @property
    def pair_id(self):
        return self.__dict__.get("_pair_id")


class Service(_O):
    pass


class _Proto(object):
    """顶层协议对象：v2 生成器需要的 all_interfaces() / structs / enums。"""

    def __init__(self, data):
        self.source = data.get("source", {})
        self.structs = [_struct_obj(s) for s in data.get("structs", [])]
        self.enums = [_enum_obj(e) for e in data.get("enums", [])]
        self.errors = [_err_obj(e) for e in data.get("errors", [])]
        self.services = _build_services(data)

    def all_interfaces(self):
        for s in self.services:
            for itf in s.interfaces:
                yield itf

    def counts(self):
        return {"services": len(self.services),
                "interfaces": sum(len(s.interfaces) for s in self.services),
                "structs": len(self.structs), "enums": len(self.enums)}


# ------------------------------------------------------------------ 各类构造
def _member_obj(m):
    o = Member({
        "name": m.get("name", ""),
        "type": m.get("type", ""),
        "desc": m.get("desc", ""),
        "byte_start": m.get("byte_start"),
        "byte_end": m.get("byte_end"),
        "open": bool(m.get("open")),
        "enum_ref": ",".join(m.get("enum_refs") or []),
        "base_type": m.get("base_type", ""),
        "array_len": m.get("array_len"),
    })
    o.__dict__["_bit"] = str(m.get("bit") or "")
    return o


def _struct_obj(s):
    o = Struct({
        "name": s.get("name", ""),
        "service": "、".join(s.get("interface_refs") or []),
        "namespace": "",
        "desc": s.get("desc", ""),
        "category": "struct",
        "size": s.get("size", ""),
    })
    o.members = [_member_obj(m) for m in s.get("members", [])]
    return o


def _enum_obj(e):
    o = Enum({"name": e.get("name", "")})
    o.values = [EnumItem({
        "value": v.get("value"),
        "value_hex": v.get("value_hex") or "0x00",
        "c_name": v.get("c_name", ""),
        "desc": v.get("desc", ""),
    }) for v in e.get("values", [])]
    return o


def _err_obj(e):
    return _O({
        "group": e.get("group", ""),
        "value": e.get("value", ""),
        "c_name": e.get("c_name", ""),
        "desc": e.get("desc", ""),
        "applies_to": e.get("applies_to", ""),
    })


def _iface_obj(i):
    o = Interface({
        "name": i.get("name", ""),
        "desc": i.get("desc", ""),
        "type": i.get("type", ""),
        "tx_type": i.get("tx_type", ""),
        "direction": i.get("direction", ""),
        "msg_id": i.get("msg_id"),
        "msg_id_hex": i.get("msg_id_hex") or "0x0000",
        "transport": i.get("transport", ""),
        "qos": i.get("qos", ""),
    })
    o.__dict__["_params"] = [Param({
        "name": p.get("name", ""),
        "type": p.get("type", ""),
        "desc": p.get("desc", ""),
        "io": p.get("io", ""),
        "enum_ref": "",
    }) for p in (i.get("params") or [])]
    return o


def _build_services(data):
    """v4 接口各自带 service 名 → 归组为 v2 的 services[].interfaces。"""
    svc_meta = {s["name"]: s for s in data.get("services", [])}
    grouped = {}
    for i in data.get("interfaces", []):
        grouped.setdefault(i.get("service") or "(未归服务)", []).append(_iface_obj(i))
    out = []
    for name, ifaces in sorted(grouped.items()):
        meta = svc_meta.get(name, {})
        sid = meta.get("service_id") or ""
        try:
            sid_int = int(sid, 16) if sid.lower().startswith("0x") else int(sid)
        except (ValueError, AttributeError):
            sid_int = None
        o = Service({
            "name": name,
            "id": sid_int,
            "id_hex": to_hex(sid_int, 2) if sid_int is not None else "0x00",
            "desc": meta.get("desc", ""),
            "namespace": meta.get("namespace", ""),
        })
        o.interfaces = ifaces
        out.append(o)
    return out


def wrap(data):
    """dict → 对象视图。"""
    return _Proto(data)
