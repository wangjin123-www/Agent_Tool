#!/usr/bin/env python3
"""s32k3-rtd-master :: list 子命令入口（薄壳：只做参数解析 + 调 core，不写业务逻辑）。

列出训练库（config/config.conf 的 training_root）下所有外设示例工程的索引，
每条标注它对应的 references 教学文档。
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common.log import setup_stdout          # noqa: E402
from core.core import cmd_list                # noqa: E402


def main():
    setup_stdout()
    parser = argparse.ArgumentParser(
        description="列出 S32K344 RTD 训练库的外设示例工程索引（可带关键词过滤）")
    parser.add_argument("keyword", nargs="?",
                        help="可选：按关键词过滤工程名，如 wkup / can / spi / flash")
    args = parser.parse_args()
    return cmd_list(args.keyword)


if __name__ == "__main__":
    sys.exit(main())
