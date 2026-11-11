# -*- coding: utf-8 -*-
"""细粒度规则：既有 checker 未覆盖、或能直接给出「怎么修」的规范。

S17 复合参数建 struct（规则 8/9/26）
    detect 产出 Issue，Issue.fix 就是可直接喂给 `edit apply` 的 ops：
    add_struct → clear_params（清空原多参数行）→ mod_interface（N=struct / O=struct）。
    `sync --emit-fix out.json` 把全部 Issue.fix 拼成一个 edit_request 落盘，
    再由 `edit apply out.json --yes` 走同一条写表路径（规则层单一真源）。

R23 枚举取值格式（规则 23）
    PE B 列必须是 0xNN 两位大写十六进制；0x0 / 0 / 0x0a 等一律可自动改写，
    随 `sync --materialize` 执行。
"""
import json
import re

from . import Rule, Issue, register
from ..common import feishu
from ..common.log import OK, WARN
from ..model import to_hex
from ..check.semantics import resolve_type
from ..parse.sheet_reader import hex_int

_BYTES = {"uint8": 1, "uint8_t": 1, "int8": 1, "uint16": 2, "uint16_t": 2,
          "int16": 2, "uint32": 4, "uint32_t": 4, "int32": 4}
_VALUE_RE = re.compile(r"^0x[0-9A-F]{2}$")


def _camel(name):
    parts = [p for p in re.split(r"[^0-9A-Za-z]+|_", name or "") if p]
    return "".join(p[:1].upper() + p[1:] for p in parts)


def _snake(name):
    s = re.sub(r"(?<=[a-z0-9])([A-Z])", r"_\1", name or "")
    return re.sub(r"_+", "_", s).strip("_").lower()


# ── S17 复合参数建 struct ──────────────────────────────────────────────
def _struct_ops(service, itf, params):
    """把一组标量参数推导成 add_struct + clear_params + mod_interface 三个 op。"""
    st_name = _camel(itf.name.replace("Mtd", "").replace("Evt", ""))
    members, byte = [], 0
    for p in params:
        nb = _BYTES[(p.type or "").lower()]
        members.append({
            "byte": "%dB" % byte if nb == 1 else "%d-%dB" % (byte, byte + nb - 1),
            "bit": "",
            "name": _snake(p.name),
            "type": p.type.split(":")[-1],
            "desc": p.desc or p.name,
        })
        byte += nb
    desc = "%s（%s）" % (itf.desc or itf.name, to_hex(itf.msg_id) if itf.msg_id else "")
    return [
        {"kind": "add_struct", "name": st_name, "service": service.name,
         "namespace": service.namespace or "", "desc": desc, "members": members},
        {"kind": "clear_params", "name": itf.name, "count": len(params)},
        {"kind": "mod_interface", "name": itf.name,
         "fields": {"N": st_name, "O": "struct", "P": ""}},
    ], st_name, members


def _r17_detect(ctx, dry=True):
    proto = ctx.proto
    out = []
    for s in proto.services:
        for itf in s.interfaces:
            if len(itf.params) < 2:
                continue
            if "struct" in [resolve_type(proto, p.type, p.name, p.enum_ref)[0] for p in itf.params]:
                continue
            params = [p for p in itf.params if p.name]
            if len(params) < 2:
                continue
            bad = [p for p in params if (p.type or "").lower() not in _BYTES]
            if bad:
                out.append(Issue(
                    "S17", "%s.%s 有 %d 个参数但类型非标量（%s），需人工建 struct"
                    % (s.name, itf.name, len(params),
                       "/".join("%s:%s" % (p.name, p.type) for p in bad)),
                    WARN, rule_no=(8, 9, 26)))
                continue
            ops, st_name, members = _struct_ops(s, itf, params)
            out.append(Issue(
                "S17",
                "%s.%s 有 %d 个标量参数（%s），规则 8/9/26 要求建 struct 单行；"
                "可修：%s{%s}（sync --emit-fix 生成 edit_request）"
                % (s.name, itf.name, len(params), "/".join(p.name for p in params),
                   st_name, ", ".join(m["name"] for m in members)),
                WARN, rule_no=(8, 9, 26), fix={"ops": ops}))
    if not out:
        out.append(Issue("S17", "未发现未建 struct 的复合参数", OK))
    return out


# ── R23 枚举取值格式 ─────────────────────────────────────────────────
def _pe_value_cells(ctx):
    """[(枚举名, C 常量名, B 列行号, B 列原文)]；A 列按块填充（首行带值）。"""
    col_a = ctx.cfg["pe_columns"]["enum_type"]
    col_b = ctx.cfg["pe_columns"]["value"]
    col_c = ctx.cfg["pe_columns"]["c_name"]
    out, cur = [], ""
    for r in range(2, len(ctx.pe) + 1):
        a = feishu.cell_text(feishu.cell_at(ctx.pe, r, col_a)).strip()
        if a:
            cur = a
        b = feishu.cell_text(feishu.cell_at(ctx.pe, r, col_b)).strip()
        c = feishu.cell_text(feishu.cell_at(ctx.pe, r, col_c)).strip()
        if b or c:
            out.append((cur, c, r, b))
    return out


def _value_int(text):
    """统一走 parse.hex_int（0x 前缀 / 含 hex 字母按 16 进制，与 msg id 列同判），再兜底小数文本。"""
    v = hex_int(text)
    if v is not None:
        return v
    try:
        return int(float(str((text or "").strip())))
    except ValueError:
        return None


def _r23_detect(ctx, dry=True):
    out = []
    for ename, cname, row, raw in _pe_value_cells(ctx):
        if _VALUE_RE.match(raw):
            continue
        v = _value_int(raw)
        if v is None:
            out.append(Issue("R23", "PE!B%d %s.%s 取值 %r 无法解析" % (row, ename, cname, raw),
                             WARN, rule_no=(23,)))
            continue
        want = "0x%02X" % v
        out.append(Issue(
            "R23", "PE!B%d %s.%s 取值 %r 应为 %s（0xNN 两位大写）"
            % (row, ename, cname, raw, want),
            WARN, rule_no=(23,),
            fix={"cells": [("parameter_enum", "B%d" % row, want)]}))
    if not out:
        out.append(Issue("R23", "枚举取值格式全部为 0xNN", OK))
    return out


def _r23_fix(ctx, issues):
    writes = []
    for iss in issues:
        for sheet_key, a1, val in iss.fix["cells"]:
            writes.append({"sheet_id": ctx.cfg["sheets"][sheet_key]["id"],
                           "range": a1, "cells": [[{"value": val}]]})
    if writes:
        feishu.write_writes(ctx.cfg, writes)
    return ["改写 %d 个枚举取值格" % len(writes)]


def _note(detect):
    def _report(ctx):
        from ..common.log import Report
        rep = Report("")
        for iss in detect(ctx, True):
            rep.add(iss.severity, iss.rule_id, iss.msg)
        return rep
    return _report


register(Rule("S17", "复合参数建 struct（规则 8/9/26）", rule_no=[8, 9, 26],
              report=_note(_r17_detect)))
register(Rule("R23", "枚举取值格式（规则 23）", rule_no=[23], fixable=True,
              default=False, report=_note(_r23_detect), fix=_r23_fix))


def emit_fix(ctx, path):
    """把全部带 fix.ops 的 Issue 拼成一个 edit_request.json。返回 (path, op 数)。"""
    import os

    from ..common import conf
    path = conf.output_path(path)
    ops = []
    for iss in _r17_detect(ctx):
        if iss.fix and "ops" in iss.fix:
            ops.extend(iss.fix["ops"])
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"ops": ops}, f, ensure_ascii=False, indent=2)
    return path, len(ops)
