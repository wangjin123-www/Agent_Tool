# -*- coding: utf-8 -*-
"""多语言代码生成调度：按 codegen/config/languages.json 分发到 scripts/gen/lang_<lang>.py。

每个语言生成器约定签名：generate(data, gcfg) -> list[str]（写出的文件路径）。
data = pull 产出的 protocol.json dict；gcfg = 该语言的 codegen_config.json。
新增语言 = 建 codegen/<lang>/（config/templates/generated）+ 写 scripts/gen/lang_<lang>.py
        + 在 codegen/config/languages.json 加一条，不改本文件。
"""
import importlib

from ..common import conf


def available():
    """[(lang, name, status)]，按注册表顺序。"""
    langs = conf.languages()["languages"]
    return [(k, v.get("name", k), v.get("status", "todo")) for k, v in langs.items()]


def resolve_languages(spec):
    """参数 → 待生成语言列表。
    None → 注册表 default；'all' → 全部 ready；'c,arxml' → 逗号分隔；'none' → []
    """
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
        conf.lang_entry(name)              # 未注册即报错
        out.append(name)
    return out


def _generator(lang):
    entry = conf.lang_entry(lang)["entry"]
    return importlib.import_module("%s.%s" % (__package__, entry))


def generate(langs=None, data=None):
    """按语言生成代码，返回 {lang: [paths]}。"""
    targets = resolve_languages(langs)
    if not targets:
        return {}
    if data is None:
        from .. import pull
        data = pull.load()
    result = {}
    skipped = {}
    for lang in targets:
        entry = conf.lang_entry(lang)
        if entry.get("status") != "ready":
            skipped[lang] = entry.get("status", "todo")
            continue
        result[lang] = _generator(lang).generate(data, conf.codegen_lang(lang))
    if skipped:
        result["_skipped"] = ["%s(%s)" % (k, v) for k, v in skipped.items()]
    return result
