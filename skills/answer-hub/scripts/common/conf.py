#!/usr/bin/env python3
"""读取 config/config.conf。绝对路径只在这里定义，禁止散落到其他脚本。"""

import configparser
import os
import subprocess
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


def get_output_dir():
    """产物目录（对齐 jira-commit 的做法）。

    优先级：
      1. 环境变量 ANSWER_HUB_OUTPUT_DIR（调用方显式指定）
      2. 当前目录在 git 仓库内 → <仓库根>/.answer-hub/output
      3. 仓库外 → 回退本 skill 的 output/

    返回前会创建目录。
    """
    env = os.environ.get("ANSWER_HUB_OUTPUT_DIR")
    if env:
        out_dir = Path(env)
    else:
        try:
            result = subprocess.run(
                ["git", "rev-parse", "--show-toplevel"],
                cwd=Path.cwd(),
                capture_output=True,
                text=True,
                timeout=5,
                check=False,
            )
            repo_root = result.stdout.strip()
        except (OSError, subprocess.SubprocessError):
            repo_root = ""

        if repo_root:
            out_dir = Path(repo_root) / ".answer-hub" / "output"
        else:
            out_dir = ROOT / "output"

    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir
