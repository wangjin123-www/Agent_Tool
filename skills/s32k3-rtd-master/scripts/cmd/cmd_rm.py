#!/usr/bin/env python3
"""s32k3-rtd-master :: rm 子命令入口（薄壳：只做参数解析 + 调 core，不写业务逻辑）。

按关键词在 S32K3xx RM/DS 手册 markdown 库中定位模块文件（含页码范围与 Grep 建议）。
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common.log import setup_stdout          # noqa: E402
from core.core import cmd_rm                 # noqa: E402


def main():
    setup_stdout()
    parser = argparse.ArgumentParser(
        description="按关键词定位 S32K3xx RM 手册模块文件 / DS 数据手册")
    parser.add_argument("keyword", nargs="?", default=None,
                        help="模块或主题关键词，如 wkpu / mc_cgm / flash / lpuart / 电气参数；"
                             "留空列出章节概览")
    args = parser.parse_args()
    return cmd_rm(args.keyword)


if __name__ == "__main__":
    sys.exit(main())
