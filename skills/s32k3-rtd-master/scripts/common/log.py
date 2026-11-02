#!/usr/bin/env python3
"""统一 UTF-8 输出：Windows 控制台默认 GBK，中文/emoji 会编码失败。"""

import sys


def setup_stdout():
    """把 stdout/stderr 切成 UTF-8。每个 cmd 入口先调一次。"""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def log(*parts):
    """统一打印：立即 flush，避免后台运行时看不到输出。"""
    setup_stdout()
    print(*parts, flush=True)
