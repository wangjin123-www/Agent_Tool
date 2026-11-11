# -*- coding: utf-8 -*-
"""多语言代码生成调度：按 codegen/config/languages.json 分发到 scripts/gen/lang_<lang>.py。

每个语言生成器约定签名：generate(proto, gcfg, root) -> list[str]（写出的文件路径）。
"""
import importlib

from ..common import conf
from ..model import Protocol


def available():
    """[(lang, name, status)]，按注册表顺序。"""
    langs = conf.languages()["languages"]
    return [(k, v.get("name", k), v.get("status", "todo")) for k, v in langs.items()]


def resolve_languages(spec):
    """把用户参数解析成待生成语言列表。
    spec: None → 注册表 default；'all' → 全部 ready；'c,java' → 逗号分隔；单值 → [单值]"""
    langs = conf.languages()["languages"]
    if spec in (None, ""):
        spec = conf.languages().get("default", "c")
    if spec == "all":
        return [k for k, v in langs.items() if v.get("status") == "ready"]
    if spec == "none":
        return []
    out = []
    for name in str(spec).split(","):
        name = name.strip().lower()
        if not name:
            continue
        conf.lang_entry(name)          # 未注册即报错
        out.append(name)
    return out


def _generator(lang):
    entry = conf.lang_entry(lang)["entry"]
    return importlib.import_module("%s.%s" % (__package__, entry))


def generate(langs=None, proto=None):
    """按语言生成代码，返回 {lang: [paths]}。"""
    targets = resolve_languages(langs)
    if not targets:
        return {}
    if proto is None:
        gcfg = conf.codegen_lang(targets[0])
        proto = Protocol.load(conf.output_path(gcfg["protocol_json"]))
    result = {}
    for lang in targets:
        gcfg = conf.codegen_lang(lang)
        root = conf.lang_root(lang)
        result[lang] = _generator(lang).generate(proto, gcfg, root)
    return result
