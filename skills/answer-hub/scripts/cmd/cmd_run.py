#!/usr/bin/env python3
"""answer-hub :: 结构校验入口（薄壳：只做参数解析 + 调 core，不写业务逻辑）。"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common.log import setup_stdout          # noqa: E402
from core.core import cmd_run                # noqa: E402


def main():
    setup_stdout()
    parser = argparse.ArgumentParser(
        description="answer-hub :: 校验装配后的 prompt 结构")
    parser.add_argument(
        "input", nargs="?",
        help="装配后 prompt 文件路径（相对 skill 根目录或绝对路径）")
    args = parser.parse_args()
    return cmd_run(args.input)


if __name__ == "__main__":
    sys.exit(main())
