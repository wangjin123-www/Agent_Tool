# -*- coding: utf-8 -*-
"""配置加载：表格坐标 / 列映射 / 色板 / 代码生成输出的唯一来源。

脚本内禁止出现 token、sheet_id、列字母、输出路径等魔法值。
"""
import json
import os

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONFIG_DIR = os.path.join(SKILL_DIR, "config")
CODEGEN_DIR = os.path.join(SKILL_DIR, "codegen")
OUTPUT_DIR = os.path.join(SKILL_DIR, "output")
PROTO_JSON = os.path.join(OUTPUT_DIR, "protocol.json")

# mod_interface 允许修改的 SI 列（改接口只动非主键列）：
# 落表引擎（edit/apply.py）与写表前预检（rules/precheck.py）共用本表，
# 避免两处各写一份导致「导出即被自己的预检拒绝」。
MOD_INTERFACE_COLUMNS = {
    "F": "if_desc", "G": "if_type", "H": "tx_type",
    "J": "msg_id", "K": "pair_id", "L": "transport", "M": "qos",
    "N": "param_name", "O": "param_type", "P": "param_desc", "Q": "param_dir",
}


def _read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def proto():
    """协议表配置 config/proto_config.json"""
    return _read_json(os.path.join(CONFIG_DIR, "proto_config.json"))


def codegen():
    """C 代码生成配置 codegen/c/config/codegen_config.json（默认语言 c）"""
    return codegen_lang("c")


def languages():
    """语言注册表 codegen/config/languages.json"""
    return _read_json(os.path.join(CODEGEN_DIR, "config", "languages.json"))


def lang_entry(lang):
    """取某语言注册项；不存在直接报错并列出可用语言。"""
    langs = languages()["languages"]
    if lang not in langs:
        raise ValueError("未注册的语言: %s（可用: %s）" % (lang, ", ".join(sorted(langs))))
    return langs[lang]


def codegen_lang(lang):
    """某语言的生成配置（路径以 languages.json 的 config 为准）。"""
    return _read_json(output_path(lang_entry(lang)["config"]))


def lang_root(lang):
    """某语言的资产根目录（内含 config/ templates/ generated/）。"""
    return output_path(lang_entry(lang)["root"])


def ensure_output():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    return OUTPUT_DIR


def rel(*parts):
    return os.path.join(SKILL_DIR, *parts)


def sheets(cfg, key):
    """取子表 id：sheets(cfg, 'data_structure')['id']"""
    return cfg["sheets"][key]


def col_index(letter):
    """'A'→0, 'Q'→16, 'AA'→26"""
    n = 0
    for ch in letter.upper():
        n = n * 26 + (ord(ch) - ord("A") + 1)
    return n - 1


def col_letter(idx):
    """col_index 的逆：0→'A', 16→'Q'（列号↔字母只此一份实现）。"""
    s = ""
    idx += 1
    while idx:
        idx, rem = divmod(idx - 1, 26)
        s = chr(ord("A") + rem) + s
    return s


def parse_a1(ref):
    """'J24' → (col_index, row_1based)"""
    ref = (ref or "").strip().upper()
    letters = "".join(c for c in ref if c.isalpha())
    digits = "".join(c for c in ref if c.isdigit())
    if not letters or not digits:
        raise ValueError("非法 A1 坐标: %r" % ref)
    return col_index(letters), int(digits)


def output_path(rel_or_abs):
    """配置里的相对路径一律相对 SKILL_DIR 解析，绝对路径原样返回。"""
    if os.path.isabs(rel_or_abs):
        return rel_or_abs
    return os.path.normpath(os.path.join(SKILL_DIR, rel_or_abs))
