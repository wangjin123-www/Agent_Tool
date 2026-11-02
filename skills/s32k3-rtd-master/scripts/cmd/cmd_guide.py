#!/usr/bin/env python3
"""s32k3-rtd-master :: guide 子命令入口（薄壳：只做参数解析 + 调 core，不写业务逻辑）。

按外设关键词抽取 references 教学文档中的章节标题 + 原样代码块，
汇总成写码指导写入 output/guide_<keyword>.md。
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common.log import setup_stdout          # noqa: E402
from core.core import cmd_guide               # noqa: E402


def main():
    setup_stdout()
    parser = argparse.ArgumentParser(
        description="按外设生成写码指导（抽取教学文档章节 + 原样代码块到 output/）")
    parser.add_argument("keyword",
                        help="外设关键词，如 spi / emios / flash / wkup / can")
    args = parser.parse_args()
    return cmd_guide(args.keyword)


if __name__ == "__main__":
    sys.exit(main())
