# -*- coding: utf-8 -*-
"""配置加载：平台宏 + 各平台数据源（飞书多维表格）坐标的唯一来源。

脚本内禁止出现 base_token、table_id、字段名等魔法值——全部来自 config/proto_config.json。
换平台 = 改 config.platform；实现按 scripts/platforms/<module> 匹配另一套，类似项目里的平台宏。
"""
import json
import os

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONFIG_PATH = os.path.join(SKILL_DIR, "config", "proto_config.json")
OUTPUT_DIR = os.path.join(SKILL_DIR, "output")
CODEGEN_DIR = os.path.join(SKILL_DIR, "codegen")


def _read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load():
    """整个 config：{ platform, platforms: { <id>: { name, module, source, tables } } }"""
    return _read_json(CONFIG_PATH)


def platform():
    """当前活动平台 id（config.platform）。"""
    return load()["platform"]


def platforms():
    """所有已配置平台的 dict。"""
    return load()["platforms"]


def platform_cfg(name=None):
    """取某平台配置；name 缺省取当前活动平台。不存在直接报错并列出可用平台。"""
    cfg = load()
    key = name or cfg["platform"]
    plats = cfg["platforms"]
    if key not in plats:
        raise ValueError("未配置的平台: %s（可用: %s）" % (key, ", ".join(sorted(plats))))
    return plats[key]


def source(name=None):
    """当前平台数据源坐标。"""
    return platform_cfg(name)["source"]


def tables(name=None):
    """当前平台表坐标 dict：{ role: {id, name, label_key, fields} }。"""
    return platform_cfg(name)["tables"]


def table(role, name=None):
    """取某张表坐标：table('service_interface')['id']。"""
    t = tables(name)
    if role not in t:
        raise ValueError("平台 %s 未配置表角色: %s（可用: %s）"
                         % (name or platform(), role, ", ".join(sorted(t))))
    return t[role]


def conventions(name=None):
    """表内约定：检测列关键字、问答表状态机取值等。"""
    return platform_cfg(name).get("conventions") or {}


def qa_state(key, name=None):
    """问答表状态取值（pending/created/failed）；未配置时退回中文默认值。"""
    defaults = {"pending": "待处理", "created": "已创建", "failed": "失败"}
    return (conventions(name).get("qa_states") or {}).get(key, defaults.get(key, ""))


def ensure_output():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    return OUTPUT_DIR


def rel(*parts):
    return os.path.join(SKILL_DIR, *parts)


# ------------------------------------------------------------------ 代码生成注册表
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


def output_path(rel_or_abs):
    """配置里的相对路径一律相对 SKILL_DIR 解析，绝对路径原样返回。"""
    if os.path.isabs(rel_or_abs):
        return rel_or_abs
    return os.path.normpath(os.path.join(SKILL_DIR, rel_or_abs))
