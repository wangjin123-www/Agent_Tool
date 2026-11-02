#!/usr/bin/env python3
"""s32k3-rtd-master :: lookup 子命令入口（薄壳：只做参数解析 + 调 core，不写业务逻辑）。

按外设关键词定位训练工程路径（含 main.c 行数）与对应的 references 教学文档。
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common.log import setup_stdout          # noqa: E402
from core.core import cmd_lookup              # noqa: E402


def main():
    setup_stdout()
    parser = argparse.ArgumentParser(
        description="按关键词定位 S32K3 外设的训练工程路径与教学文档")
    parser.add_argument("keyword",
                        help="外设关键词，如 wkpu / can / adc / flash / emios / spi")
    args = parser.parse_args()
    return cmd_lookup(args.keyword)


if __name__ == "__main__":
    sys.exit(main())
