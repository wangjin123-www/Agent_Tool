# -*- coding: utf-8 -*-
"""C 代码生成器：protocol.json → 模板 → codegen/c/generated/。

原则（沿袭 v2 备份 skill 的 lang_c）：
  - 模板零逻辑：分支/映射全部在 Python 里算好再交给模板；
  - StrictUndefined：模板引用了未提供的变量直接报错；
  - 确定性：同一 protocol.json 两次渲染逐字节相同（渲染两次自检）；
  - 不用 C 位域：bit 成员生成 Get/Set 访问器（掩码式），跨编译器可移植。

差异（v4）：输入是 pull 产出的 protocol.json（dict），检测关卡由多维表格
「正常性检测」字段承担（gen 前统一跑 pull.check_issues，含 ❌ 即阻断）。
"""
import hashlib
import json
import os
import re

import jinja2

from ..common import conf

_CTYPE = {"uint8": "uint8_t", "int8": "sint8_t",
          "uint16": "uint16_t", "int16": "sint16_t",
          "uint32": "uint32_t", "int32": "sint32_t"}


def _mask_of(bit):
    """位宽 N(1~7) → 起始位 0 的掩码。同字节多成员位域起始位由调用方累加。"""
    return (1 << bit) - 1


def build_view(data, gcfg):
    """protocol.json dict → 模板视图（全部 Python 侧算好）。

    命名（2026-11-09 定案，方案 A）：
      - 类型名直接用表内名：结构体 Xxx_t、枚举 Xxx_E（不带 struct_prefix）
      - 成员/参数名直接用表内名：lowerCamelCase
      - 枚举值直接用表内名：EnumName_VALUE（带枚举名前缀）
      - Pack/Unpack 与命令处理函数保留 helper_prefix（Proto_），避免与业务符号冲突
      - 命令 id 枚举保留 cmd_enum_prefix（PROTO_CMD_）
    """
    h = gcfg["header"]
    hp = h.get("helper_prefix", "")
    cp = h["cmd_enum_prefix"]

    rx, tx = [], []
    for itf in data["interfaces"]:
        mid = itf.get("msg_id")
        entry = {
            "name": itf["name"],
            "enum": cp + itf["name"],
            "id": mid,
            "id_hex": itf.get("msg_id_hex") or "0x0000",
            "handler": hp + itf["name"] + h["handler_suffix"],
            "type": itf.get("type", ""),
            "tx_type": itf.get("tx_type", ""),
            "params": itf.get("params", []),
            "service": itf.get("service", ""),
        }
        # 方向真源 = msg_id bit15 (0x8000=MCU→SOC)
        (tx if (mid or 0) & 0x8000 else rx).append(entry)

    structs = []
    for st in data["structs"]:
        ms = []
        bit_cursor = {}                      # byte_start → 已占用 bit 数（同字节多位域累加）
        for m in st["members"]:
            mm = dict(m)
            mm["ctype"] = _CTYPE.get(m.get("base_type", ""), "uint8_t")
            if m.get("open"):
                mm["ctype"] = "uint8_t"
            if m.get("is_bit"):
                used = bit_cursor.get(m["byte_start"], 0)
                mm["mask"] = "0x%02X" % _mask_of(m["bit"])
                mm["shift"] = str(used)
                bit_cursor[m["byte_start"]] = used + m["bit"]
            ms.append(mm)
        fixed = [m["byte_end"] for m in ms
                 if not m.get("open") and m.get("byte_end") is not None]
        nbytes = (max(fixed) + 1) if fixed else 0
        structs.append({
            "name": st["name"], "c_name": st["name"],
            "fname": hp + re.sub(r"_(t|E)$", "", st["name"]),
            "desc": st.get("desc", ""), "size": st.get("size", ""),
            "service": "、".join(st.get("interface_refs", [])),
            "nbytes": nbytes,
            "has_open": any(m.get("open") for m in ms),
            "members": ms,
            "is_raw": any(m.get("is_bit") for m in ms),
        })

    enums = []
    for e in data["enums"]:
        enums.append({
            "name": e["name"], "c_name": e["name"],
            "vals": [{"c_name": v["c_name"], "value": v["value"],
                      "value_hex": v.get("value_hex") or "0x00",
                      "desc": v.get("desc", "")} for v in e["values"]],
        })

    return {"rx": rx, "tx": tx, "structs": structs, "enums": enums}


def generate(data, gcfg=None):
    """渲染全部 C 产物，返回写入路径列表。"""
    root = conf.lang_root("c")
    if gcfg is None:
        gcfg = conf.codegen_lang("c")

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.join(root, "templates")),
        undefined=jinja2.StrictUndefined,
        trim_blocks=True, lstrip_blocks=True, keep_trailing_newline=True)

    view = build_view(data, gcfg)
    common = {
        # v2 模板的 {{ spreadsheet }} / {{ revision }} 沿用，指向 Bitable 源
        "spreadsheet": "%s（Bitable %s）" % (data.get("platform_name", ""),
                                            data.get("source", {}).get("base_token", "")),
        "revision": data.get("schema_version", ""),
        "counts": data.get("counts", {}),
    }

    out_dir = conf.output_path(gcfg["output_dir"])
    os.makedirs(out_dir, exist_ok=True)

    written = []
    for key, fname in gcfg["file_names"].items():
        tmpl = env.get_template(key + ".j2")
        guard = gcfg["header"]["include_guard_prefix"] + \
            os.path.splitext(fname)[0].upper().replace("-", "_") + "_H"
        kw = dict(files=gcfg["file_names"], header=gcfg["header"],
                  behaviour=gcfg.get("behaviour", {}), guard=guard, **view, **common)
        text1 = tmpl.render(**kw)
        text2 = tmpl.render(**kw)
        if hashlib.md5(text1.encode("utf-8")).hexdigest() != \
                hashlib.md5(text2.encode("utf-8")).hexdigest():
            raise SystemExit("模板渲染不确定: %s" % fname)
        path = os.path.join(out_dir, fname)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text1)
        written.append(path)
    return written
