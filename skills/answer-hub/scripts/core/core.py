#!/usr/bin/env python3
"""answer-hub 业务层：装配后 prompt 的结构校验。只被 scripts/cmd/* 调用，禁止 import cmd。"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common.conf import root, get_output_dir   # noqa: E402
from common.log import log                  # noqa: E402

# 骨架里没替换干净的方括号/尖括号/花括号提示，一律视为占位符残留
PLACEHOLDER_PATTERNS = (
    (r"\[[^\]\n]*(?:TODO|待填|具体|说明|如[：:]|你的|xxx|placeholder|\.\.\.)[^\]\n]*\]",
     "方括号占位符"),
    (r"<[^>\n]*(?:TODO|待填|具体|说明|placeholder)[^>\n]*>", "尖括号占位符"),
    (r"\{\{[^}\n]*\}\}", "双花括号变量"),
)

# 必备结构块：多模板下小标题措辞不同，所以按关键词命中判定，不锁死标题
REQUIRED_BLOCKS = (
    ("角色声明", r"你是一位|你是一名|You are an?\b|角色[:：]"),
    ("任务说明", r"你的任务是|任务[:：]|目标是|Your task"),
    ("禁止事项", r"禁止|不要|严禁|Do not|Don'?t"),
    ("输出格式", r"输出格式|输出要求|交付格式|Output format"),
    ("项目上下文", r"项目上下文|技术栈|已有|Context|背景"),
)

MIN_CHARS = 300


def check_prompt(text):
    """校验 prompt 文本，返回 (errors, warnings)。纯函数，便于复用与测试。"""
    errors = []
    warnings = []

    for pattern, label in PLACEHOLDER_PATTERNS:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            errors.append(f"占位符未替换（{label}）：{match.group(0)}")

    for name, pattern in REQUIRED_BLOCKS:
        if not re.search(pattern, text):
            errors.append(f"缺少结构块：{name}")

    stripped = text.strip()
    if len(stripped) < MIN_CHARS:
        warnings.append(
            f"正文仅 {len(stripped)} 字符，低于建议下限 {MIN_CHARS}，确认是否交代不足"
        )
    return errors, warnings


def cmd_run(arg=None):
    """校验装配后的 prompt 文件。返回 0 = 通过，1 = 有 ERROR，2 = 用法/文件错误。"""
    if not arg:
        log("用法：python scripts/cmd/cmd_run.py <装配后prompt文件路径>")
        return 2

    src = Path(arg)
    if not src.is_absolute():
        src = root() / src
    if not src.exists():
        log(f"[ERROR] 文件不存在：{src}")
        return 2

    text = src.read_text(encoding="utf-8")
    errors, warnings = check_prompt(text)

    lines = [f"# 结构校验报告：{src.name}", f"- 字符数：{len(text.strip())}", ""]
    if errors:
        lines += [f"[ERROR] {e}" for e in errors]
    else:
        lines.append("[ERROR] 无")
    lines += [f"[WARN] {w}" for w in warnings]
    lines += ["", f"结论：{'失败，修改后重跑' if errors else '通过'}"]

    report_dir = get_output_dir()
    (report_dir / "validate-report.txt").write_text(
        "\n".join(lines) + "\n", encoding="utf-8")

    for line in lines:
        log(line)
    return 1 if errors else 0
