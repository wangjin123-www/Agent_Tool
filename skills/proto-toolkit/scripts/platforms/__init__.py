# -*- coding: utf-8 -*-
"""平台注册表：按 config.platform 动态加载对应平台的协议读取实现。

设计类似项目里的平台宏——每个平台在 scripts/platforms/<module>/ 下有独立一套实现，
config 里声明 module 名；换平台只改 config.platform，这里自动匹配另一套。
未注册平台直接报错并提示可用平台。
"""
import importlib

# 平台 id → 相对模块名（带前导点，importlib.import_module 第二参为 __package__）
_REGISTRY = {
    "7255": ".platform_7255",
}


def available():
    """已注册平台 id 列表。"""
    return sorted(_REGISTRY)


def is_registered(platform_id):
    return platform_id in _REGISTRY


def get_reader_class(platform_id):
    """按平台 id 取其 Reader 类；未注册则报错列出可用平台。"""
    mod_name = _REGISTRY.get(platform_id)
    if mod_name is None:
        raise ValueError(
            "未注册的平台实现: %s（已注册: %s）。\n"
            "新增平台：在 scripts/platforms/ 下加 platform_<id>/ 实现 Reader，"
            "并在此注册表登记。" % (platform_id, ", ".join(available())))
    mod = importlib.import_module(mod_name, __package__)
    return mod.Reader


def make_reader(platform_id, platform_cfg):
    """实例化指定平台的 Reader。platform_cfg 来自 conf.platform_cfg()。"""
    cls = get_reader_class(platform_id)
    return cls(platform_cfg)
