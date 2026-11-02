# -*- coding: utf-8 -*-
"""edit 写表前预检（scope="precheck"）：拿还没落表的 op 跑同一批判据。

写前拦住比写完再让 sync 报便宜。ERR → apply 拒绝落表（--force 可越过）。
"""
import re

from . import Rule, Issue, register
from ..common import conf
from ..common.log import WARN, ERR
from ..parse.sheet_reader import parse_byte_index
from ..check.semantics import resolve_type

_SCALARS = {"uint8", "uint8_t", "int8", "uint16", "uint16_t", "int16",
            "uint32", "uint32_t", "int32"}
_INLINE = re.compile(r"(?:^|[，,；;/\s])(?:0x)?[0-9A-Fa-f]{1,4}\s*[=:：]")
_VALUE = re.compile(r"^0x[0-9A-F]{2}$")


def _val_bytes(t):
    t = (t or "").lower()
    return {"uint8": 1, "uint8_t": 1, "int8": 1, "uint16": 2, "uint16_t": 2,
            "int16": 2, "uint32": 4, "uint32_t": 4, "int32": 4}.get(t)


def _missing_ref(ctx, kind, name):
    """引用存在性：与 sync 的 S08/S09 同源判据——已存在的 + 本批将新增的都算命中。

    「SI 有参数但 DS 没有该 struct」必须在写表前拦（precheck），而不是落表后
    等 sync 报 S08。同批 add_struct → add_interface 引用新 struct 是合法序列。
    """
    if kind == "struct":
        if ctx.proto.find_struct(name) is not None or name in ctx.pending_structs:
            return None
        return "struct %s 不在 Data Structure（也不在本批 add_struct）" % name
    if kind == "enum":
        if ctx.proto.find_enum(name) is not None or name in ctx.pending_enums:
            return None
        return "枚举 %s 不在 Parameter Enum（也不在本批 add_enum）" % name
    return None


def _if_(ctx, op):
    """add_interface：复合参数必须建 struct；struct/enum 引用必须存在（规则 8/9/26，同 S08/S09）。"""
    if op.get("kind") != "add_interface":
        return []
    params = op.get("params") or []
    scalars = [p for p in params if not (p.get("type") or "").startswith(("struct:", "enum:"))]
    if len(params) >= 2 and len(scalars) == len(params):
        return [Issue("S17", "接口 %s 有 %d 个标量参数（%s），规则 8/9/26 要求建 struct 单行："
                             "先 add_struct，再用一个 type=struct:名 参数引用"
                       % (op["name"], len(params), "/".join(p["name"] for p in params)),
                       ERR, rule_no=(8, 9, 26))]
    out = []
    for p in params:
        kind, name = resolve_type(ctx.proto, p.get("type") or "", p.get("name") or "")
        if kind in ("struct", "enum"):
            miss = _missing_ref(ctx, kind, name)
            if miss:
                code = "S08" if kind == "struct" else "S09"
                out.append(Issue(code, "接口 %s 参数 %s：%s，先补定义再引用"
                                 % (op["name"], p.get("name") or name, miss),
                                 ERR, rule_no=(26,)))
            continue
        if _INLINE.search(p.get("desc") or "") and len(_INLINE.findall(p.get("desc") or "")) >= 2:
            out.append(Issue("S16", "接口 %s 参数 %s 描述含内联值域，应改用 type=enum:枚举名"
                             % (op["name"], p["name"]), WARN, rule_no=(8,)))
    return out


def _enum_(ctx, op):
    """add_enum：B 列必须 0xNN 两位大写；C 列常量名全局唯一（规则 23）。"""
    if op.get("kind") != "add_enum":
        return []
    out = []
    seen = {}
    for e in ctx.proto.enums:
        for it in e.items:
            if it.c_name:
                seen[it.c_name] = e.name
    for v in op.get("values") or []:
        raw = str(v.get("value", "")).strip()
        if not _VALUE.match(raw):
            out.append(Issue("R23", "枚举 %s 取值 %r 应为 0xNN 两位大写十六进制"
                             % (op["name"], raw), ERR, rule_no=(23,)))
        c = v.get("c_name") or ""
        if not c:
            out.append(Issue("R23", "枚举 %s 有取值 %r 缺 C 常量名" % (op["name"], raw),
                             ERR, rule_no=(23,)))
        elif c in seen:
            out.append(Issue("R23", "枚举常量名 %s 已被 %s 使用（C 命名空间全局唯一）"
                             % (c, seen[c]), ERR, rule_no=(23,)))
        elif not re.match(r"^[A-Z][A-Z0-9_]*$", c):
            out.append(Issue("R23", "枚举常量名 %s 应为全大写+下划线（规则 23）" % c,
                             WARN, rule_no=(23,)))
    if not op.get("msg_id"):
        out.append(Issue("R23", "枚举 %s 缺消息 id（PE E 列反向链接依赖它）" % op["name"],
                         ERR, rule_no=(25, 26)))
    return out


def _struct_(ctx, op):
    """add_struct：字节序号必须从 0 连续、类型与跨度一致（规则 26 / S11~S13）。"""
    if op.get("kind") != "add_struct":
        return []
    out = []
    expect = 0
    for i, m in enumerate(op.get("members") or []):
        span = parse_byte_index(m.get("byte", ""))
        if span is None:
            out.append(Issue("S11", "struct %s 成员 %s 字节区间非法 %r"
                             % (op["name"], m["name"], m.get("byte")), ERR, rule_no=(26,)))
            continue
        bs, be, is_open = span
        if bs != expect:
            out.append(Issue("S11", "struct %s 成员 %s 起始字节 %dB，应接上一成员为 %dB"
                             % (op["name"], m["name"], bs, expect), ERR, rule_no=(26,)))
        if is_open and i != len(op["members"]) - 1:
            out.append(Issue("S14", "struct %s 开放尾成员 %s 必须是最后一个"
                             % (op["name"], m["name"]), ERR, rule_no=(26,)))
        if not is_open:
            want = _val_bytes(m.get("type"))
            if want and be - bs + 1 != want:
                out.append(Issue("S13", "struct %s 成员 %s 占 %dB，类型 %s 应 %dB"
                                 % (op["name"], m["name"], be - bs + 1, m.get("type"), want),
                                 ERR, rule_no=(26,)))
            expect = be + 1
        if not m.get("name"):
            out.append(Issue("S11", "struct %s 第 %d 个成员缺成员名" % (op["name"], i + 1),
                             ERR, rule_no=(26,)))
    return out


def _mod_(ctx, op):
    """mod_interface：只允许改非主键列，消息 id/关联 id 成对改（规则 10/15）；
    N 列指向 struct 时该 struct 必须存在（同 S08，含本批 add_struct）。"""
    if op.get("kind") != "mod_interface":
        return []
    out = []
    fields = op.get("fields") or {}
    if "J" in fields and "K" not in fields:
        out.append(Issue("SEC", "改接口 %s 的消息 id 后需同步核对关联 id（规则 15）"
                         % op["name"], WARN, rule_no=(15,)))
    allowed = conf.MOD_INTERFACE_COLUMNS
    for col in fields:
        if col not in allowed:
            out.append(Issue("SEC", "改接口 %s 不允许列 %s（仅 %s）"
                             % (op["name"], col, " ".join(sorted(allowed))), ERR,
                             rule_no=(16,)))
    if "N" in fields and str(fields.get("O", "")).lower() == "struct":
        miss = _missing_ref(ctx, "struct", (fields["N"] or "").strip())
        if miss:
            out.append(Issue("S08", "改接口 %s：%s" % (op["name"], miss), ERR, rule_no=(26,)))
    return out


def _precheck(ctx, op):
    return _if_(ctx, op) + _enum_(ctx, op) + _struct_(ctx, op) + _mod_(ctx, op)


register(Rule("PRE", "写表前预检", rule_no=[8, 9, 15, 16, 23, 25, 26],
              scope="precheck", precheck=_precheck))
