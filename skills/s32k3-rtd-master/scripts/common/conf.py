#!/usr/bin/env python3
"""读取 config/config.conf。绝对路径只在这里定义，禁止散落到其他脚本。"""

import configparser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = ROOT / "config" / "config.conf"
FALLBACK_PATH = ROOT / "config" / "config.conf.example"

_cache = None


def load_config(path=None):
    """读配置；真实配置缺失时回退 .example。返回 ConfigParser。"""
    global _cache
    if path is None and _cache is not None:
        return _cache
    target = Path(path) if path else (CONFIG_PATH if CONFIG_PATH.exists() else FALLBACK_PATH)
    parser = configparser.ConfigParser()
    if target.exists():
        parser.read(target, encoding="utf-8")
    if path is None:
        _cache = parser
    return parser


def root():
    """skill 根目录。所有相对路径以此为基准。"""
    return ROOT
