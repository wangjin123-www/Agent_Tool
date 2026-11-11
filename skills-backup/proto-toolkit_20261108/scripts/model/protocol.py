# -*- coding: utf-8 -*-
"""protocol.json 数据模型与序列化。

契约约定（与 .answer-hub/output/protocol-codegen-plan/output.html 对齐）：
  1. 全部数组保序（表内顺序即数组顺序）；
  2. id 存两份：整数 + "0xNNNN"（大写十六进制 4 位）；
  3. source.revision 必填（写回时的 revision 快照）；
  4. 不存任何链接 URL，只存主键（struct 名 / msg id / row），链接是绝对坐标，
     插删行即失效，一律由 check 阶段按主键重算；
  5. 不含时间戳——表没动，重复 parse 产物逐字节相同（git diff 干净）。
"""
import json
import os

from ..common import conf
from .jsonschema_lite import validate as schema_validate

SCHEMA_VERSION = "1.1.0"       # 1.1.0：接口新增 section_dir；source 新增 parse_stats


class SchemaError(RuntimeError):
    """protocol.json 违反 config/protocol.schema.json 契约（校验手段 B）。"""


def _check_schema(data, where):
    """按 config/protocol.schema.json 校验；违规即抛 SchemaError。"""
    schema_path = conf.rel("config", "protocol.schema.json")
    with open(schema_path, "r", encoding="utf-8") as f:
        errs = schema_validate(data, json.load(f))
    if errs:
        raise SchemaError("protocol.json 契约校验失败（%s）：%s"
                          % (where, "; ".join(errs[:10])))


def to_hex(v, width=4):
    """0x8802 → '0x8802'（大写、定宽）。"""
    return "0x%0*X" % (width, v)


class Protocol:
    def __init__(self):
        self.schema_version = SCHEMA_VERSION
        self.source = {
            "spreadsheet": "",      # 表名
            "spreadsheet_token": "",
            "revision": None,       # 解析时的表格 revision 快照
        }
        self.services = []          # [Service]
        self.structs = []           # [Struct]
        self.enums = []             # [Enum]

    # ------------------------------------------------------------ 统计
    def all_interfaces(self):
        for s in self.services:
            for itf in s.interfaces:
                yield itf

    def find_interface(self, msg_id):
        for itf in self.all_interfaces():
            if itf.msg_id == msg_id:
                return itf
        return None

    def find_struct(self, name):
        for s in self.structs:
            if s.name == name:
                return s
        return None

    def find_enum(self, name):
        for e in self.enums:
            if e.name == name:
                return e
        return None

    def counts(self):
        n_if = sum(len(s.interfaces) for s in self.services)
        return {"services": len(self.services), "interfaces": n_if,
                "structs": len(self.structs), "enums": len(self.enums)}

    # ------------------------------------------------------------ 序列化
    def to_dict(self):
        return {
            "schema_version": self.schema_version,
            "source": dict(self.source),
            "services": [s.to_dict() for s in self.services],
            "structs": [s.to_dict() for s in self.structs],
            "enums": [e.to_dict() for e in self.enums],
        }

    @classmethod
    def from_dict(cls, d):
        p = cls()
        p.schema_version = d["schema_version"]
        p.source = d["source"]
        p.services = [Service.from_dict(x) for x in d["services"]]
        p.structs = [Struct.from_dict(x) for x in d["structs"]]
        p.enums = [Enum.from_dict(x) for x in d["enums"]]
        return p

    def save(self, path=None):
        path = path or conf.PROTO_JSON
        data = self.to_dict()
        _check_schema(data, "save 前")          # 校验手段 B：落盘前拦
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return path

    @classmethod
    def load(cls, path=None):
        path = path or conf.PROTO_JSON
        if not os.path.exists(path):
            raise FileNotFoundError("protocol.json 不存在，先跑 parse: " + path)
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        _check_schema(data, "load 时")          # 校验手段 B：保护 gen 等下游
        return cls.from_dict(data)


class Service:
    def __init__(self):
        self.name = ""
        self.id = None              # 0x01
        self.desc = ""
        self.namespace = ""
        self.si_row = None          # 块首行（写回 SI 定位用，不参与语义）
        self.interfaces = []        # [Interface]

    def to_dict(self):
        return {"name": self.name, "id": self.id, "id_hex": to_hex(self.id, 2),
                "desc": self.desc, "namespace": self.namespace,
                "interfaces": [i.to_dict() for i in self.interfaces]}

    @classmethod
    def from_dict(cls, d):
        s = cls()
        s.name, s.id, s.desc, s.namespace = d["name"], d["id"], d.get("desc", ""), d.get("namespace", "")
        s.interfaces = [Interface.from_dict(x) for x in d["interfaces"]]
        return s


class Interface:
    def __init__(self):
        self.name = ""
        self.desc = ""
        self.type = ""              # method(rr) / method / event
        self.tx_type = ""           # 事件 / 周期
        self.direction = ""         # SOC_TO_MCU / MCU_TO_SOC（真源 = msg_id bit15，0x8000=MCU→SOC）
        self.section_dir = ""       # 已废弃：恒为空，兼容旧 protocol.json
        self.msg_id = None          # 0x0801
        self.pair_id = None         # 0x8802 或 None
        self.transport = ""
        self.qos = ""
        self.params = []            # [Param]
        self.si_row = None

    @property
    def direction_hex(self):
        """方向位：SOC→MCU 高位为 0，MCU→SOC 高位为 0x8x（方向真源就是它）。"""
        return (self.msg_id or 0) & 0x8000

    def to_dict(self):
        d = {"name": self.name, "desc": self.desc, "type": self.type,
             "tx_type": self.tx_type, "direction": self.direction,
             "section_dir": self.section_dir,
             "msg_id": self.msg_id, "msg_id_hex": to_hex(self.msg_id)}
        if self.pair_id is not None:
            d["pair_id"] = self.pair_id
            d["pair_id_hex"] = to_hex(self.pair_id)
        if self.transport:
            d["transport"] = self.transport
        if self.qos:
            d["qos"] = self.qos
        if self.params:
            d["params"] = [p.to_dict() for p in self.params]
        return d

    @classmethod
    def from_dict(cls, d):
        i = cls()
        i.name, i.desc = d["name"], d.get("desc", "")
        i.type, i.tx_type, i.direction = d.get("type", ""), d.get("tx_type", ""), d["direction"]
        i.section_dir = d.get("section_dir", "")
        i.msg_id, i.pair_id = d["msg_id"], d.get("pair_id")
        i.transport, i.qos = d.get("transport", ""), d.get("qos", "")
        i.params = [Param.from_dict(x) for x in d.get("params", [])]
        return i


class Param:
    def __init__(self):
        self.name = ""
        self.type = ""              # uint8 / uint16 / uint32 / enum:XXX / struct:XXX / uint8[]
        self.desc = ""
        self.io = ""                # IN / OUT / NONE（Q 列）
        self.enum_ref = ""          # P 列内链命中的枚举名（type 仍留 uint8，C 侧不变）
        self.si_row = None

    def to_dict(self):
        d = {"name": self.name, "type": self.type}
        if self.desc:
            d["desc"] = self.desc
        if self.io:
            d["io"] = self.io
        if self.enum_ref:
            d["enum_ref"] = self.enum_ref
        return d

    @classmethod
    def from_dict(cls, d):
        p = cls()
        p.name, p.type = d["name"], d["type"]
        p.desc, p.io = d.get("desc", ""), d.get("io", "")
        p.enum_ref = d.get("enum_ref", "")
        return p


class Struct:
    def __init__(self):
        self.name = ""
        self.service = ""
        self.namespace = ""
        self.desc = ""
        self.category = ""
        self.size = ""              # '6' / '4+N'（原文本，含开放尾）
        self.members = []           # [Member]
        self.ds_row = None          # struct 首行

    @property
    def fixed_bytes(self):
        """封闭成员覆盖到的最大字节 + 1（开放尾不计）。"""
        return 1 + max((m.byte_end for m in self.members if not m.open and m.byte_end is not None), default=-1)

    @property
    def has_open(self):
        return any(m.open for m in self.members)

    def to_dict(self):
        return {"name": self.name, "service": self.service, "namespace": self.namespace,
                "desc": self.desc, "category": self.category or "struct", "size": self.size,
                "members": [m.to_dict() for m in self.members]}

    @classmethod
    def from_dict(cls, d):
        s = cls()
        for k in ("name", "service", "namespace", "desc", "category", "size"):
            setattr(s, k, d.get(k, ""))
        s.members = [Member.from_dict(x) for x in d["members"]]
        return s


class Member:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.desc = ""
        self.byte_start = None      # 0
        self.byte_end = None        # 3（单字节 0B → 0..0）
        self.bit = ""               # '0-7' / ''（开放尾为空）
        self.open = False           # '4-NB' 开放尾
        self.enum_ref = ""          # K 列内链命中的枚举名
        self.ds_row = None

    @property
    def nbytes(self):
        return (self.byte_end - self.byte_start + 1) if (self.byte_end is not None and not self.open) else None

    def to_dict(self):
        d = {"name": self.name, "type": self.type, "byte_start": self.byte_start,
             "byte_end": self.byte_end, "open": self.open}
        if self.bit:
            d["bit"] = self.bit
        if self.desc:
            d["desc"] = self.desc
        if self.enum_ref:
            d["enum_ref"] = self.enum_ref
        return d

    @classmethod
    def from_dict(cls, d):
        m = cls()
        m.name, m.type = d["name"], d["type"]
        m.byte_start, m.byte_end = d["byte_start"], d["byte_end"]
        m.bit, m.open = d.get("bit", ""), d.get("open", False)
        m.desc = d.get("desc", "")
        m.enum_ref = d.get("enum_ref", "")
        return m


class Enum:
    def __init__(self):
        self.name = ""
        self.items = []             # [EnumItem]
        self.pe_row = None          # 枚举名首行

    def to_dict(self):
        return {"name": self.name, "items": [i.to_dict() for i in self.items]}

    @classmethod
    def from_dict(cls, d):
        e = cls()
        e.name = d["name"]
        e.items = [EnumItem.from_dict(x) for x in d["items"]]
        return e


class EnumItem:
    def __init__(self):
        self.value = None
        self.c_name = ""
        self.desc = ""

    def to_dict(self):
        d = {"value": self.value, "value_hex": to_hex(self.value, 2), "c_name": self.c_name}
        if self.desc:
            d["desc"] = self.desc
        return d

    @classmethod
    def from_dict(cls, d):
        i = cls()
        i.value, i.c_name, i.desc = d["value"], d["c_name"], d.get("desc", "")
        return i
