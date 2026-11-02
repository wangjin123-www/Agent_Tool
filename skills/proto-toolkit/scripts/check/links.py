# -*- coding: utf-8 -*-
"""链接校验 + 重算（能力 ①：relink 命令化，工程兜底）。

链接契约（2026-10-30 修订：消息 id 单元格一律不带链接）：
  E1 SI P 参数描述 ↔ PE A 枚举类型首行      （正向 P→A 由表内既有链接确定，反向 A→P）
  E2 DS K 成员变量描述 ↔ PE A 枚举类型首行  （正向 K→A，反向 A→K）
  E3 SI N struct 参数 ↔ DS C 数据结构名     （双向）
  E5 SI K 关联 id ↔ 对端 SI J               （双向，method(rr) 配对，规则 15）
  E6 SI P result 参数 ↔ 错误码组首行        （双向，错误码统一码表；
     result 进 struct 时改认 DS K 成员描述行 — 规则 26 与统一错误码并存）
禁止：SI J（消息 id）、PE E（Message Id）等列不得挂任何链接（stray 扫描发现即报错，
      --fix 重写为纯文本保留原文案）。

比对只认「目标 sheet_id + 目标 A1」，文案差异不算错；
repair 模式把缺失/漂移的链接按期望重写（base64 一律程序生成），并清除禁止列的链接。
"""
from ..common import feishu, conf
from ..common.log import Report, OK
from ..model import to_hex
from ..parse.sheet_reader import parse_byte_index  # noqa: F401  (复用声明)
from .semantics import resolve_type

# 允许挂链接的列（其余列一旦有链接即 stray）
_ALLOWED_COLS = {
    "service_interface": {"K", "N", "P"},
    "data_structure": {"C", "K"},
    "parameter_enum": {"A"},
    "error_code": {"A"},
}


def read_error_codes(cfg):
    """读错误码表 A~E（表缺失时返回空列表，E6 自动跳过）。"""
    if "error_code" not in (cfg.get("sheets") or {}):
        return []
    try:
        return feishu.read(cfg, "error_code", "E")
    except RuntimeError:
        return []


def _ec_group_row(cfg, ec_rows):
    """错误码表里目标组的首行 A1（默认组 COMM_RESULT → A2）；找不到返回 None。"""
    group = (cfg.get("error_code") or {}).get("group")
    if not group:
        return None
    for r in range(2, len(ec_rows) + 1):
        if feishu.cell_text(feishu.cell_at(ec_rows, r, "A")).strip() == group:
            return "A%d" % r
    return None


def _is_error_code_param(cfg, n_txt, o_txt, q_txt, p_txt):
    """SI 行是否为统一错误码参数：result / uint8 / OUT，且 P 列明示「成功」或「错误码」。

    只有写「0=成功，非0=错误码」这类通用错误码语义的行才链错误码表；
    「0=OK，1=NOK」等具体业务二值语义不算（那是枚举值域，走 PE）。
    """
    ec = cfg.get("error_code") or {}
    if (n_txt.strip() != ec.get("param_name")
            or o_txt.strip().lower() != str(ec.get("param_type")).lower()
            or q_txt.strip().upper() != "OUT"):
        return False
    kws = ec.get("param_desc_keywords") or ["成功", "错误码"]
    return any(k in (p_txt or "") for k in kws)



def _norm_a1(a1):
    return (a1 or "").strip().upper()


def _strip_refs(cfg, si_rows, ds_rows):
    """扫 SI P / DS K 的既有前向链接（→ PE A），建「枚举格 → 引用源」反查表。"""
    pe_sheet_id = cfg["sheets"]["parameter_enum"]["id"]
    refs = {}
    for r in range(2, len(si_rows) + 1):
        url = feishu.cell_link(feishu.cell_at(si_rows, r, "P"))
        s, a = feishu.decode_url(url)
        if s == pe_sheet_id and a:
            refs.setdefault(_norm_a1(a), []).append(
                ("service_interface", "P%d" % r, feishu.cell_text(feishu.cell_at(si_rows, r, "P"))))
    for r in range(2, len(ds_rows) + 1):
        url = feishu.cell_link(feishu.cell_at(ds_rows, r, "K"))
        s, a = feishu.decode_url(url)
        if s == pe_sheet_id and a:
            refs.setdefault(_norm_a1(a), []).append(
                ("data_structure", "K%d" % r, feishu.cell_text(feishu.cell_at(ds_rows, r, "K"))))
    return refs


def expected_links(cfg, proto, si_rows, ds_rows, pe_rows):
    """返回期望链接表：{(sheet_key, 'A1'): (target_sheet_key, target_a1, text)}"""
    exp = {}
    refs = _strip_refs(cfg, si_rows, ds_rows)

    # E1/E2 参数/成员 ↔ 枚举（反向目标 = 引用源：参数描述优先于成员描述）
    for en in proto.enums:
        if en.pe_row is None:
            continue
        a1 = "A%d" % en.pe_row
        src = refs.get(a1, [])
        if not src:
            continue                    # 无引用源的枚举由 validate 单独告警
        tgt_key, tgt_a1, _text = src[0]
        exp[("parameter_enum", a1)] = (tgt_key, tgt_a1, en.name)
        for sk, sa1, stext in src:
            exp[(sk, sa1)] = ("parameter_enum", a1, stext)

    # E3 struct：SI N ↔ DS C（双向；规则 26 定的是 C 列数据结构名）
    ds_by_name = {st.name: st for st in proto.structs}
    for itf in proto.all_interfaces():
        for p in itf.params:
            kind, name = resolve_type(proto, p.type, p.name, p.enum_ref)
            if kind != "struct" or p.si_row is None:
                continue
            st = proto.find_struct(name)
            if st is None:
                continue
            exp[("service_interface", "N%d" % p.si_row)] = (
                "data_structure", "C%d" % st.ds_row, name)
            exp.setdefault(("data_structure", "C%d" % st.ds_row),
                           ("service_interface", "N%d" % p.si_row, st.name))
    # 表中 struct 参数常与接口同行（N/O 与 E 同行，parse 不建 Param 对象），按原始行补
    for r in range(2, len(si_rows) + 1):
        n_txt = feishu.cell_text(feishu.cell_at(si_rows, r, "N")).strip()
        o_txt = feishu.cell_text(feishu.cell_at(si_rows, r, "O")).strip()
        if o_txt.lower() != "struct" and n_txt not in ds_by_name:
            continue
        st = ds_by_name.get(n_txt)
        if st is None or st.ds_row is None:
            continue
        exp[("service_interface", "N%d" % r)] = ("data_structure", "C%d" % st.ds_row, n_txt)
        exp.setdefault(("data_structure", "C%d" % st.ds_row),
                       ("service_interface", "N%d" % r, st.name))

    # E5 SI K 关联 id ↔ 对端 SI J
    for itf in proto.all_interfaces():
        if itf.pair_id is None or itf.si_row is None:
            continue
        peer = proto.find_interface(itf.pair_id)
        if peer is None or peer.si_row is None:
            continue
        exp[("service_interface", "K%d" % itf.si_row)] = (
            "service_interface", "J%d" % peer.si_row, to_hex(itf.pair_id))

    # E6 SI P result 参数 ↔ 错误码组首行（统一错误码表）
    ec_rows = read_error_codes(cfg)
    ec_a1 = _ec_group_row(cfg, ec_rows) if ec_rows else None
    if ec_a1:
        group = (cfg.get("error_code") or {}).get("group")
        for r in range(2, len(si_rows) + 1):
            n_txt = feishu.cell_text(feishu.cell_at(si_rows, r, "N"))
            o_txt = feishu.cell_text(feishu.cell_at(si_rows, r, "O"))
            q_txt = feishu.cell_text(feishu.cell_at(si_rows, r, "Q"))
            p_txt = feishu.cell_text(feishu.cell_at(si_rows, r, "P"))
            if not _is_error_code_param(cfg, n_txt, o_txt, q_txt, p_txt):
                continue
            exp[("service_interface", "P%d" % r)] = (
                "error_code", ec_a1, p_txt or "错误码定义 →")
            exp.setdefault(("error_code", ec_a1),
                           ("service_interface", "P%d" % r, group))
        # E6 扩展：result 进了 struct 时（规则 26），改认 DS K 成员描述行
        ec = cfg.get("error_code") or {}
        kws = ec.get("param_desc_keywords") or ["成功", "错误码"]
        for r in range(2, len(ds_rows) + 1):
            m_txt = feishu.cell_text(feishu.cell_at(ds_rows, r, "I")).strip()
            k_txt = feishu.cell_text(feishu.cell_at(ds_rows, r, "J")).strip()
            l_txt = feishu.cell_text(feishu.cell_at(ds_rows, r, "K"))
            if m_txt != ec.get("param_name") or k_txt.lower() != str(ec.get("param_type")).lower():
                continue
            if not any(k in (l_txt or "") for k in kws):
                continue
            exp[("data_structure", "K%d" % r)] = (
                "error_code", ec_a1, l_txt or "错误码定义 →")
            exp.setdefault(("error_code", ec_a1),
                           ("data_structure", "K%d" % r, group))
    return exp


def stray_links(cfg, exp, si_rows, ds_rows, pe_rows, ec_rows=None):
    """扫描 SI/DS/PE/错误码 中不该挂链接的格：返回 [(sheet_key, a1, text, cur_sheet, cur_a1)]。"""
    sheets = {
        "service_interface": si_rows,
        "data_structure": ds_rows,
        "parameter_enum": pe_rows,
    }
    if ec_rows:
        sheets["error_code"] = ec_rows
    out = []
    for sheet_key, rows in sheets.items():
        allowed = _ALLOWED_COLS[sheet_key]
        for r in range(2, len(rows) + 1):
            line = rows[r - 1] if r - 1 < len(rows) else []
            for ci, cell in enumerate(line):
                if not cell:
                    continue
                url = feishu.cell_link(cell)
                if not url:
                    continue
                col = conf.col_letter(ci)
                a1 = "%s%d" % (col, r)
                if col in allowed and (sheet_key, a1) in exp:
                    continue
                cur_sheet, cur_a1 = feishu.decode_url(url)
                out.append((sheet_key, a1, feishu.cell_text(cell), cur_sheet, cur_a1))
    return out


def _plain_write(cfg, sheet_key, a1, text):
    return {"sheet_id": cfg["sheets"][sheet_key]["id"],
            "range": a1, "cells": [[{"value": text}]]}


def validate(cfg, proto, si_rows, ds_rows, pe_rows, repair=False, sink=None):
    rep = Report("链接校验（%s）" % ("relink 修复模式" if repair else "只读"))

    exp = expected_links(cfg, proto, si_rows, ds_rows, pe_rows)
    ec_rows = read_error_codes(cfg)
    sheet_rows = {
        "service_interface": si_rows,
        "data_structure": ds_rows,
        "parameter_enum": pe_rows,
    }
    if ec_rows:
        sheet_rows["error_code"] = ec_rows

    fixes = []
    for (sheet_key, a1), (tgt_key, tgt_a1, text) in sorted(exp.items()):
        ci, ri = conf.parse_a1(a1)
        cell = feishu.cell_at(sheet_rows[sheet_key], ri, conf.col_letter(ci))
        url = feishu.cell_link(cell)
        cur_sheet, cur_a1 = feishu.decode_url(url)
        want_sheet = cfg["sheets"][tgt_key]["id"]
        if cur_sheet == want_sheet and _norm_a1(cur_a1) == _norm_a1(tgt_a1):
            rep.ok("LNK", "%s!%s → %s" % (sheet_key, a1, tgt_a1))
            continue
        problem = "缺链接" if not url else "漂移(现指向 %s!%s)" % (cur_sheet, cur_a1)
        if repair:
            fixes.append(feishu.link_write(cfg, sheet_key, a1, text, tgt_key, tgt_a1))
            rep.warn("LNK", "%s!%s %s → 已重算写入 %s" % (sheet_key, a1, problem, tgt_a1))
        else:
            rep.err("LNK", "%s!%s %s，期望 → %s!%s" % (sheet_key, a1, problem, tgt_key, tgt_a1))

    # 枚举无引用源 → 无法建反链
    refs = _strip_refs(cfg, si_rows, ds_rows)
    for en in proto.enums:
        if en.pe_row is not None and not refs.get("A%d" % en.pe_row):
            rep.warn("LNK", "枚举 %s（PE A%d）无引用源（SI P / DS K 均未链向它），跳过反链" % (en.name, en.pe_row))

    # 禁止列上的多余链接
    strays = stray_links(cfg, exp, si_rows, ds_rows, pe_rows, ec_rows)
    for sheet_key, a1, text, cur_sheet, cur_a1 in strays:
        if repair:
            fixes.append(_plain_write(cfg, sheet_key, a1, text))
            rep.warn("LNK", "%s!%s 不应有链接（原指向 %s!%s）→ 已清为纯文本" % (sheet_key, a1, cur_sheet, cur_a1))
        else:
            rep.err("LNK", "%s!%s 不应有链接（现指向 %s!%s，消息 id 列须为纯文本）"
                    % (sheet_key, a1, cur_sheet, cur_a1))

    if repair and fixes:
        _emit(cfg, sink, fixes)
        rep.add(OK, "LNK", "relink 完成：重写/清理 %d 条链接" % len(fixes))
    elif repair:
        rep.add(OK, "LNK", "relink 完成：无漂移，0 条重写")
    return rep


def _emit(cfg, sink, writes):
    """写表只走一条路：有 sink 就交给调用方统一执行，没有才自己写。"""
    if sink is not None:
        sink.setdefault("writes", []).extend(writes)
    else:
        feishu.write_writes(cfg, writes)


def relink(cfg, proto, si_rows, ds_rows, pe_rows):
    """直接重算写回全部期望链接（不比对，强制覆盖）。"""
    rep = Report("强制 relink")
    exp = expected_links(cfg, proto, si_rows, ds_rows, pe_rows)
    writes = []
    for (sheet_key, a1), (tgt_key, tgt_a1, text) in sorted(exp.items()):
        writes.append(feishu.link_write(cfg, sheet_key, a1, text, tgt_key, tgt_a1))
    feishu.write_writes(cfg, writes)
    rep.add(OK, "LNK", "强制 relink：写入 %d 条链接" % len(writes))
    return rep
