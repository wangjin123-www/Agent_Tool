# -*- coding: utf-8 -*-
"""AUTOSAR ARXML 生成器：protocol.json → 标准 ARXML（DataType + Interface）。

设计：
  - 只做 **ApplicationDataType / ImplementationDataType / Interface**，不做 SWC/COM；
  - 版本、命名空间、包名、类型后缀全部来自 codegen/arxml/config/codegen_config.json；
  - 生成器只负责“结构”，不把版本差异写成配置语言；
  - 用 ElementTree 构建（ARXML 是引用图，程序化建引用比模板更稳）；
  - 生成前后做引用闭合检查，避免 DaVinci 导入时才报未解析引用。

约定（v1，AUTOSAR 4.2.2 默认）：
  - 应用类型：APPLICATION-PRIMITIVE-DATA-TYPE / APPLICATION-RECORD-DATA-TYPE /
    APPLICATION-ARRAY-DATA-TYPE；
  - 实现类型：IMPLEMENTATION-DATA-TYPE（VALUE / STRUCTURE / ARRAY）；
  - 枚举：ApplicationPrimitiveDataType + CompuMethod(TEXTTABLE)；
  - 接口：event → SenderReceiverInterface；method(rr)/method → ClientServerInterface；
  - 平台基础类型引用 /AUTOSAR_Platform/BaseTypes/<uint8|sint8|...>（由目标工具提供）。
"""
import hashlib
import json
import os
import re
import xml.etree.ElementTree as ET

from ..common import conf
from .object_view import wrap as _wrap_view

AUTOSAR_NS = "http://autosar.org/schema/r4.0"
XSI_NS = "http://www.w3.org/2001/XMLSchema-instance"

BASE_TYPES = ("uint8", "sint8", "uint16", "sint16", "uint32", "sint32")


def to_hex(v, width=4):
    """0x8802 → '0x8802'（大写、定宽）。与 v2 model.to_hex 一致。"""
    return "0x%0*X" % (width, v or 0)

_TYPE_ALIAS = {
    "uint8": "uint8", "uint8_t": "uint8",
    "int8": "sint8", "sint8": "sint8", "int8_t": "sint8", "sint8_t": "sint8",
    "uint16": "uint16", "uint16_t": "uint16",
    "int16": "sint16", "sint16": "sint16", "int16_t": "sint16", "sint16_t": "sint16",
    "uint32": "uint32", "uint32_t": "uint32",
    "int32": "sint32", "sint32": "sint32", "int32_t": "sint32", "sint32_t": "sint32",
}
REF_TAGS = {
    "TYPE-TREF", "BASE-TYPE-REF", "COMPU-METHOD-REF",
    "IMPLEMENTATION-DATA-TYPE-REF", "APPLICATION-DATA-TYPE-REF",
}


def _norm_type(t):
    """'uint8_t' / 'uint8[]' / 'int16' → 基础类型名；未知返回小写原值。"""
    t = (t or "").strip().lower()
    t = re.sub(r"\[\s*\d*\s*\]\s*$", "", t)
    return _TYPE_ALIAS.get(t, t)


def _is_array(t):
    return "[" in (t or "") or (t or "").strip().endswith("[]")


def _ident(name):
    """AUTOSAR SHORT-NAME：字母/数字/下划线，不能以数字开头，包内唯一（由 NamePool 保证）。"""
    s = re.sub(r"[^A-Za-z0-9_]", "_", name or "")
    s = re.sub(r"_+", "_", s).strip("_")
    if not s:
        s = "Unnamed"
    if s[0].isdigit():
        s = "_" + s
    return s


class _NamePool:
    """同一个包内生成唯一 SHORT-NAME。"""

    def __init__(self):
        self.used = {}

    def get(self, name):
        base = _ident(name)
        n = self.used.get(base, 0) + 1
        self.used[base] = n
        return base if n == 1 else "%s_%d" % (base, n)


def _el(parent, tag, text=None, attrs=None):
    e = ET.SubElement(parent, tag, attrs or {})
    if text is not None:
        e.text = str(text)
    return e


def _ref(parent, tag, dest, path):
    e = ET.SubElement(parent, tag, {"DEST": dest})
    e.text = path
    return e


def _desc(parent, en=None, zh=None):
    if not (en or zh):
        return
    d = _el(parent, "DESC")
    if en:
        _el(d, "L-2", en, {"L": "EN"})
    if zh:
        _el(d, "L-2", zh, {"L": "ZH"})


def _bit_rep(bit):
    """'0-7bit' → (0, 8)；'4' → (4, 1)；非法返回 None。"""
    t = (bit or "").strip().lower().replace("bit", "").strip()
    if not t:
        return None
    try:
        if "-" in t:
            a, b = (int(x) for x in t.split("-", 1))
        else:
            a = b = int(t)
    except ValueError:
        return None
    if a < 0 or b > 7 or a > b:
        return None
    return a, b - a + 1


def _sw_props(parent, base_ref=None, compu_ref=None, bit=None):
    props = _el(parent, "SW-DATA-DEF-PROPS")
    variants = _el(props, "SW-DATA-DEF-PROPS-VARIANTS")
    cond = _el(variants, "SW-DATA-DEF-PROPS-CONDITIONAL")
    if base_ref:
        _ref(cond, "BASE-TYPE-REF", "SW-BASE-TYPE", base_ref)
    if compu_ref:
        _ref(cond, "COMPU-METHOD-REF", "COMPU-METHOD", compu_ref)
    if bit:
        br = _el(cond, "SW-BIT-REPRESENTATION")
        _el(br, "BIT-POSITION", bit[0])
        _el(br, "NUMBER-OF-BITS", bit[1])
    return cond


class _Builder:
    def __init__(self, proto, gcfg):
        self.proto = proto
        self.gcfg = gcfg
        self.cfg = gcfg["arxml"]
        self.scope = gcfg["scope"]
        self.naming = gcfg["naming"]
        self.behaviour = gcfg["behaviour"]

        self.ns = self.cfg["namespace"]
        self.prefix = self.cfg["package_prefix"].rstrip("/")
        self.platform = self.cfg["platform_types_package"].rstrip("/")
        self.dt_pkg = "%s/%s" % (self.prefix, self.naming["datatype_package"])
        self.if_pkg = "%s/%s" % (self.prefix, self.naming["interface_package"])
        self.map_pkg = "%s/%s" % (self.prefix, self.naming["mapping_package"])
        self.impl_suffix = self.naming["implementation_type_suffix"]
        self.array_suffix = self.naming["array_type_suffix"]
        self.open_max = int(self.naming.get("open_array_max_elements", 255))

        self.dt_names = _NamePool()
        self.if_names = _NamePool()

        self.struct_orig = {s.name for s in proto.structs}
        self.enum_orig = {e.name for e in proto.enums}
        self.used_bases = self._collect_bases()

        # ---- 应用类型/实现类型名字（先定名，后面所有引用都用它） ----
        self.base_name = {b: self.dt_names.get(b) for b in sorted(self.used_bases)}
        self.base_impl = {b: self.dt_names.get(self.base_name[b] + self.impl_suffix)
                          for b in sorted(self.used_bases)}

        self.enum_name, self.enum_impl, self.enum_cm = {}, {}, {}
        for e in proto.enums:
            app = self.dt_names.get(e.name)
            self.enum_name[e.name] = app
            self.enum_impl[e.name] = self.dt_names.get(app + self.impl_suffix)
            self.enum_cm[e.name] = self.dt_names.get(app + "_CompuMethod")

        self.struct_name, self.struct_impl = {}, {}
        for s in proto.structs:
            app = self.dt_names.get(s.name)
            self.struct_name[s.name] = app
            self.struct_impl[s.name] = self.dt_names.get(app + self.impl_suffix)

        # 开放尾/数组类型的名字：(struct, member) -> (app, impl)
        self.array_name = {}
        for s in proto.structs:
            for m in s.members:
                if m.open or _is_array(m.type):
                    base = "%s_%s%s" % (self.struct_name[s.name], _ident(m.name),
                                        self.array_suffix)
                    app = self.dt_names.get(base)
                    self.array_name[(s.name, m.name)] = (
                        app, self.dt_names.get(app + self.impl_suffix))

        self.defined = set()
        self.mapping = []        # (app_path, app_dest, impl_path)

    # ------------------------------------------------------------------ 收集
    def _collect_bases(self):
        used = set()
        for p in self.proto.all_interfaces():
            for param in p.params:
                t = _norm_type(param.type)
                if t in BASE_TYPES:
                    used.add(t)
        for s in self.proto.structs:
            for m in s.members:
                t = _norm_type(m.type)
                if t in BASE_TYPES:
                    used.add(t)
        used.add("uint8")       # 枚举/空事件 dummy 的底座
        return used

    def _platform_base(self, base):
        return "%s/BaseTypes/%s" % (self.platform, base)

    def _app_path(self, key, kind):
        if kind == "base":
            return "%s/%s" % (self.dt_pkg, self.base_name[key]), "APPLICATION-PRIMITIVE-DATA-TYPE"
        if kind == "enum":
            return "%s/%s" % (self.dt_pkg, self.enum_name[key]), "APPLICATION-PRIMITIVE-DATA-TYPE"
        if kind == "struct":
            return "%s/%s" % (self.dt_pkg, self.struct_name[key]), "APPLICATION-RECORD-DATA-TYPE"
        if kind == "array":
            return "%s/%s" % (self.dt_pkg, self.array_name[key][0]), "APPLICATION-ARRAY-DATA-TYPE"
        raise ValueError(kind)

    def _impl_path(self, key, kind):
        if kind == "base":
            return "%s/%s" % (self.dt_pkg, self.base_impl[key])
        if kind == "enum":
            return "%s/%s" % (self.dt_pkg, self.enum_impl[key])
        if kind == "struct":
            return "%s/%s" % (self.dt_pkg, self.struct_impl[key])
        if kind == "array":
            return "%s/%s" % (self.dt_pkg, self.array_name[key][1])
        raise ValueError(kind)

    def _resolve_member(self, s, m):
        """成员 -> (app_path, app_dest, impl_path, app_category)。"""
        if m.open or _is_array(m.type):
            key = (s.name, m.name)
            app, dest = self._app_path(key, "array")
            return app, dest, self._impl_path(key, "array"), "ARRAY"
        if m.enum_ref and m.enum_ref in self.enum_orig:
            app, dest = self._app_path(m.enum_ref, "enum")
            return app, dest, self._impl_path(m.enum_ref, "enum"), "VALUE"
        t = _norm_type(m.type)
        if t in BASE_TYPES:
            app, dest = self._app_path(t, "base")
            return app, dest, self._impl_path(t, "base"), "VALUE"
        if m.type in self.struct_orig:
            app, dest = self._app_path(m.type, "struct")
            return app, dest, self._impl_path(m.type, "struct"), "STRUCTURE"
        # 兜底：未知类型按 uint8 处理，不让引用断掉
        app, dest = self._app_path("uint8", "base")
        return app, dest, self._impl_path("uint8", "base"), "VALUE"

    def _resolve_param(self, p):
        if p.enum_ref and p.enum_ref in self.enum_orig:
            return self._app_path(p.enum_ref, "enum")
        if p.type == "struct":
            name = p.name if p.name in self.struct_orig else None
            if name:
                return self._app_path(name, "struct")
        t = _norm_type(p.type)
        if t in BASE_TYPES:
            return self._app_path(t, "base")
        if p.type in self.struct_orig:
            return self._app_path(p.type, "struct")
        return self._app_path("uint8", "base")

    # ------------------------------------------------------------------ 包结构
    def _make_root(self):
        ET.register_namespace("", self.ns)
        ET.register_namespace("xsi", XSI_NS)
        attrs = {
            "{%s}schemaLocation" % XSI_NS:
                "%s %s" % (self.ns, self.cfg["schema_location"]),
        }
        if self.cfg.get("schema_attribute"):
            attrs["S"] = self.cfg["schema_attribute"]
        root = ET.Element("AUTOSAR", attrs)
        # 我们的子元素都用无前缀标签构建；显式声明默认命名空间，保证
        # 反序列化后所有元素都落在 AUTOSAR namespace 内。
        root.set("xmlns", self.ns)
        pkgs = _el(root, "AR-PACKAGES")
        cur = pkgs
        for seg in [x for x in self.prefix.split("/") if x]:
            pkg = _el(cur, "AR-PACKAGE")
            _el(pkg, "SHORT-NAME", seg)
            cur = _el(pkg, "AR-PACKAGES")
        return root, cur

    @staticmethod
    def _leaf(parent_pkgs, name):
        pkg = _el(parent_pkgs, "AR-PACKAGE")
        _el(pkg, "SHORT-NAME", name)
        return pkg, _el(pkg, "ELEMENTS")

    # ------------------------------------------------------------------ DataType
    def _gen_base(self, elems, b):
        app_name, impl_name = self.base_name[b], self.base_impl[b]
        base_ref = self._platform_base(b)

        app = _el(elems, "APPLICATION-PRIMITIVE-DATA-TYPE")
        _el(app, "SHORT-NAME", app_name)
        _el(app, "CATEGORY", "VALUE")
        _sw_props(app, base_ref=base_ref)

        impl = _el(elems, "IMPLEMENTATION-DATA-TYPE")
        _el(impl, "SHORT-NAME", impl_name)
        _el(impl, "CATEGORY", "VALUE")
        _sw_props(impl, base_ref=base_ref)

        self.defined.add("%s/%s" % (self.dt_pkg, app_name))
        self.defined.add("%s/%s" % (self.dt_pkg, impl_name))
        self.mapping.append(("%s/%s" % (self.dt_pkg, app_name),
                             "APPLICATION-PRIMITIVE-DATA-TYPE",
                             "%s/%s" % (self.dt_pkg, impl_name)))

    def _gen_enum(self, elems, e):
        app_name = self.enum_name[e.name]
        impl_name = self.enum_impl[e.name]
        cm_name = self.enum_cm[e.name]
        base_ref = self._platform_base("uint8")
        cm_path = "%s/%s" % (self.dt_pkg, cm_name)

        cm = _el(elems, "COMPU-METHOD")
        _el(cm, "SHORT-NAME", cm_name)
        _el(cm, "CATEGORY", "TEXTTABLE")
        i2p = _el(cm, "COMPU-INTERNAL-TO-PHYS")
        scales = _el(i2p, "COMPU-SCALES")
        seen = set()
        items = [i for i in e.items if i.value is not None]
        if not items:
            items = [type("_I", (), {"value": 0, "c_name": "UNDEFINED", "desc": ""})()]
        for item in items:
            if item.value in seen:
                continue
            seen.add(item.value)
            sc = _el(scales, "COMPU-SCALE")
            _el(sc, "LOWER-LIMIT", item.value, {"INTERVAL-TYPE": "CLOSED"})
            _el(sc, "UPPER-LIMIT", item.value, {"INTERVAL-TYPE": "CLOSED"})
            const = _el(sc, "COMPU-CONST")
            _el(const, "VT", item.c_name or str(item.value))

        app = _el(elems, "APPLICATION-PRIMITIVE-DATA-TYPE")
        _el(app, "SHORT-NAME", app_name)
        _el(app, "CATEGORY", "VALUE")
        _sw_props(app, base_ref=base_ref, compu_ref=cm_path)

        impl = _el(elems, "IMPLEMENTATION-DATA-TYPE")
        _el(impl, "SHORT-NAME", impl_name)
        _el(impl, "CATEGORY", "VALUE")
        _sw_props(impl, base_ref=base_ref, compu_ref=cm_path)

        self.defined.add("%s/%s" % (self.dt_pkg, app_name))
        self.defined.add("%s/%s" % (self.dt_pkg, impl_name))
        self.defined.add(cm_path)
        self.mapping.append(("%s/%s" % (self.dt_pkg, app_name),
                             "APPLICATION-PRIMITIVE-DATA-TYPE",
                             "%s/%s" % (self.dt_pkg, impl_name)))

    def _gen_array(self, elems, s, m):
        app_name, impl_name = self.array_name[(s.name, m.name)]
        base_app = "%s/%s" % (self.dt_pkg, self.base_name["uint8"])
        base_impl = "%s/%s" % (self.dt_pkg, self.base_impl["uint8"])

        app = _el(elems, "APPLICATION-ARRAY-DATA-TYPE")
        _el(app, "SHORT-NAME", app_name)
        _el(app, "CATEGORY", "ARRAY")
        element = _el(app, "ELEMENT")
        ae = _el(element, "APPLICATION-ARRAY-ELEMENT")
        _el(ae, "SHORT-NAME", "Element")
        _ref(ae, "TYPE-TREF", "APPLICATION-PRIMITIVE-DATA-TYPE", base_app)
        _el(ae, "MAX-NUMBER-OF-ELEMENTS", self.open_max)

        impl = _el(elems, "IMPLEMENTATION-DATA-TYPE")
        _el(impl, "SHORT-NAME", impl_name)
        _el(impl, "CATEGORY", "ARRAY")
        subs = _el(impl, "SUB-ELEMENTS")
        ie = _el(subs, "IMPLEMENTATION-DATA-TYPE-ELEMENT")
        _el(ie, "SHORT-NAME", "Element")
        _el(ie, "CATEGORY", "TYPE_REFERENCE")
        _ref(ie, "IMPLEMENTATION-DATA-TYPE-REF", "IMPLEMENTATION-DATA-TYPE", base_impl)
        _el(ie, "ARRAY-SIZE", self.open_max)

        self.defined.add("%s/%s" % (self.dt_pkg, app_name))
        self.defined.add("%s/%s" % (self.dt_pkg, impl_name))
        self.mapping.append(("%s/%s" % (self.dt_pkg, app_name),
                             "APPLICATION-ARRAY-DATA-TYPE",
                             "%s/%s" % (self.dt_pkg, impl_name)))

    def _gen_struct(self, elems, s):
        app_name = self.struct_name[s.name]
        impl_name = self.struct_impl[s.name]

        app = _el(elems, "APPLICATION-RECORD-DATA-TYPE")
        _el(app, "SHORT-NAME", app_name)
        _el(app, "CATEGORY", "STRUCTURE")
        app_elems = _el(app, "ELEMENTS")
        for m in s.members:
            app_path, app_dest, _impl_path, category = self._resolve_member(s, m)
            ae = _el(app_elems, "APPLICATION-RECORD-ELEMENT")
            _el(ae, "SHORT-NAME", _ident(m.name))
            if self.behaviour.get("emit_desc", True):
                _desc(ae, en=self._member_desc(m), zh=m.desc)
            _el(ae, "CATEGORY", category)
            _ref(ae, "TYPE-TREF", app_dest, app_path)

        impl = _el(elems, "IMPLEMENTATION-DATA-TYPE")
        _el(impl, "SHORT-NAME", impl_name)
        _el(impl, "CATEGORY", "STRUCTURE")
        subs = _el(impl, "SUB-ELEMENTS")
        for m in s.members:
            _app_path, _app_dest, impl_path, _category = self._resolve_member(s, m)
            ie = _el(subs, "IMPLEMENTATION-DATA-TYPE-ELEMENT")
            _el(ie, "SHORT-NAME", _ident(m.name))
            if self.behaviour.get("emit_desc", True):
                _desc(ie, en=self._member_desc(m), zh=m.desc)
            _el(ie, "CATEGORY", "TYPE_REFERENCE")
            bit = None
            if (self.behaviour.get("emit_bit_representation", True)
                    and m.bit and m.byte_start is not None
                    and m.byte_end is not None
                    and m.byte_start == m.byte_end):
                bit = _bit_rep(m.bit)
            if bit:
                _sw_props(ie, bit=bit)
            _ref(ie, "IMPLEMENTATION-DATA-TYPE-REF", "IMPLEMENTATION-DATA-TYPE",
                 impl_path)

        self.defined.add("%s/%s" % (self.dt_pkg, app_name))
        self.defined.add("%s/%s" % (self.dt_pkg, impl_name))
        self.mapping.append(("%s/%s" % (self.dt_pkg, app_name),
                             "APPLICATION-RECORD-DATA-TYPE",
                             "%s/%s" % (self.dt_pkg, impl_name)))

    @staticmethod
    def _member_desc(m):
        parts = []
        if m.byte_start is not None:
            if m.open or m.byte_end is None:
                parts.append("byte %s..N(open)" % m.byte_start)
            elif m.byte_end == m.byte_start:
                parts.append("byte %s" % m.byte_start)
            else:
                parts.append("byte %s-%s" % (m.byte_start, m.byte_end))
        if m.bit:
            parts.append("bit %s" % m.bit)
        return "; ".join(parts)

    # ------------------------------------------------------------------ Interfaces
    def _gen_interface(self, elems, itf):
        name = self.if_names.get(itf.name)
        is_cs = "method" in (itf.type or "").lower()

        en = "msg_id=%s; direction=%s; type=%s; tx_type=%s; transport=%s; qos=%s" % (
            to_hex(itf.msg_id or 0), itf.direction, itf.type, itf.tx_type,
            itf.transport, itf.qos)
        if itf.pair_id is not None:
            en = "pair_id=%s; " % to_hex(itf.pair_id) + en

        if is_cs:
            node = _el(elems, "CLIENT-SERVER-INTERFACE")
            _el(node, "SHORT-NAME", name)
            if self.behaviour.get("emit_desc", True):
                _desc(node, en=en, zh=itf.desc)
            ops = _el(node, "OPERATIONS")
            op = _el(ops, "CLIENT-SERVER-OPERATION")
            _el(op, "SHORT-NAME", name)
            if itf.params:
                args = _el(op, "ARGUMENTS")
                for p in itf.params:
                    app_path, app_dest = self._resolve_param(p)
                    arg = _el(args, "ARGUMENT-DATA-PROTOTYPE")
                    _el(arg, "SHORT-NAME", _ident(p.name))
                    if self.behaviour.get("emit_desc", True):
                        _desc(arg, en="io=%s" % (p.io or "NONE"), zh=p.desc)
                    _ref(arg, "TYPE-TREF", app_dest, app_path)
                    _el(arg, "DIRECTION", self._direction(p.io))
        else:
            node = _el(elems, "SENDER-RECEIVER-INTERFACE")
            _el(node, "SHORT-NAME", name)
            if self.behaviour.get("emit_desc", True):
                _desc(node, en=en, zh=itf.desc)
            data_elems = _el(node, "DATA-ELEMENTS")
            for p in itf.params:
                app_path, app_dest = self._resolve_param(p)
                v = _el(data_elems, "VARIABLE-DATA-PROTOTYPE")
                _el(v, "SHORT-NAME", _ident(p.name))
                if self.behaviour.get("emit_desc", True):
                    _desc(v, en="io=%s" % (p.io or "NONE"), zh=p.desc)
                _ref(v, "TYPE-TREF", app_dest, app_path)
            if not itf.params and self.behaviour.get("emit_dummy_for_empty_event", True):
                v = _el(data_elems, "VARIABLE-DATA-PROTOTYPE")
                _el(v, "SHORT-NAME", "Dummy")
                _desc(v, en="no payload (protocol event has no parameters)",
                      zh="协议事件无参数，占位")
                _ref(v, "TYPE-TREF", "APPLICATION-PRIMITIVE-DATA-TYPE",
                     "%s/%s" % (self.dt_pkg, self.base_name["uint8"]))

        self.defined.add("%s/%s" % (self.if_pkg, name))

    @staticmethod
    def _direction(io):
        io = (io or "").strip().upper()
        return io if io in ("IN", "OUT", "INOUT") else "INOUT"

    # ------------------------------------------------------------------ Mapping
    def _gen_mapping(self, elems):
        node = _el(elems, "DATA-TYPE-MAPPING-SET")
        _el(node, "SHORT-NAME", "Protocol_MappingSet")
        maps = _el(node, "DATA-TYPE-MAPS")
        for app_path, app_dest, impl_path in self.mapping:
            m = _el(maps, "DATA-TYPE-MAP")
            _ref(m, "APPLICATION-DATA-TYPE-REF", app_dest, app_path)
            _ref(m, "IMPLEMENTATION-DATA-TYPE-REF", "IMPLEMENTATION-DATA-TYPE", impl_path)

    # ------------------------------------------------------------------ 校验
    def _check_refs(self, root):
        bad = []
        for e in root.iter():
            tag = e.tag.rsplit("}", 1)[-1]
            if tag not in REF_TAGS:
                continue
            path = (e.text or "").strip()
            if not path:
                bad.append("%s: 空引用" % tag)
            elif path.startswith(self.prefix + "/"):
                if path not in self.defined:
                    bad.append("%s: 未定义 %s" % (tag, path))
            elif path.startswith(self.platform + "/"):
                pass        # 平台类型由目标工具提供
            else:
                bad.append("%s: 未知包 %s" % (tag, path))
        if bad:
            raise SystemExit("ARXML 引用检查失败（%d 条）：\n  %s"
                             % (len(bad), "\n  ".join(bad[:20])))

    # ------------------------------------------------------------------ 入口
    def build(self):
        root, parent_pkgs = self._make_root()

        if self.scope.get("datatypes", True):
            dt_pkg, dt_elems = self._leaf(parent_pkgs, self.naming["datatype_package"])
            for b in sorted(self.used_bases):
                self._gen_base(dt_elems, b)
            for e in self.proto.enums:
                self._gen_enum(dt_elems, e)
            for s in self.proto.structs:
                for m in s.members:
                    if m.open or _is_array(m.type):
                        self._gen_array(dt_elems, s, m)
            for s in self.proto.structs:
                self._gen_struct(dt_elems, s)

        if self.scope.get("interfaces", True):
            if_pkg, if_elems = self._leaf(parent_pkgs, self.naming["interface_package"])
            for itf in self.proto.all_interfaces():
                self._gen_interface(if_elems, itf)

        if self.scope.get("datatypes", True):
            map_pkg, map_elems = self._leaf(parent_pkgs, self.naming["mapping_package"])
            self._gen_mapping(map_elems)

        try:
            ET.indent(root, space="  ")
        except AttributeError:      # Python < 3.9
            pass

        data1 = ET.tostring(root, encoding="utf-8", xml_declaration=True)
        data2 = ET.tostring(root, encoding="utf-8", xml_declaration=True)
        if hashlib.md5(data1).hexdigest() != hashlib.md5(data2).hexdigest():
            raise SystemExit("ARXML 渲染不确定（两次序列化不一致）")

        if self.behaviour.get("reference_check", True):
            self._check_refs(root)
        return data1


def _load_schema(root):
    path = os.path.join(root, "config", "codegen_config.schema.json")
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _schema_validate(data, schema):
    """极简 JSON Schema 校验（仅 codegen_config 用到的关键字），无第三方依赖。"""
    errs = []

    def walk(node, sch, path_):
        if not isinstance(sch, dict):
            return
        t = sch.get("type")
        if t == "object" and not isinstance(node, dict):
            errs.append("%s: 应为 object" % (path_ or "$"))
            return
        if t == "array" and not isinstance(node, list):
            errs.append("%s: 应为 array" % (path_ or "$"))
            return
        for k in sch.get("required", []):
            if not isinstance(node, dict) or k not in node:
                errs.append("%s: 缺少必填项 %r" % (path_ or "$", k))
        if isinstance(node, dict):
            for k, sub in (sch.get("properties") or {}).items():
                if k in node:
                    walk(node[k], sub, "%s.%s" % (path_, k) if path_ else k)
        if t == "string" and sch.get("pattern") and isinstance(node, str):
            if not re.search(sch["pattern"], node):
                errs.append("%s: 不匹配 pattern %r" % (path_ or "$", sch["pattern"]))
        if isinstance(node, list) and isinstance(sch.get("items"), dict):
            for idx, it in enumerate(node):
                walk(it, sch["items"], "%s[%d]" % (path_, idx))

    walk(data, schema, "")
    return errs


def generate(data, gcfg):
    """生成 ARXML（v4 入口：data=protocol.json dict）；返回写出的文件路径列表。"""
    root = conf.lang_root("arxml")
    schema = _load_schema(root)
    if schema:
        errs = _schema_validate(gcfg, schema)
        if errs:
            raise SystemExit("ARXML 配置不合法（codegen_config.json）：%s"
                             % "; ".join(errs[:10]))
    if gcfg["scope"].get("swc") or gcfg["scope"].get("com"):
        raise SystemExit("ARXML v1 只支持 scope.datatypes/interfaces；"
                         "swc/com 需后续版本实现，请先置 false")

    proto = _wrap_view(data)
    out = _Builder(proto, gcfg).build()
    out_dir = conf.output_path(gcfg["output_dir"])
    os.makedirs(out_dir, exist_ok=True)
    fname = (gcfg.get("file_names") or {}).get("arxml", "Protocol.arxml")
    path = os.path.join(out_dir, fname)
    with open(path, "wb") as f:
        f.write(out)
    return [path]
