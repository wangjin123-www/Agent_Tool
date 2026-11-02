#!/usr/bin/env python3
"""
Quick validation script for skills - minimal version

除 frontmatter 基础校验外，还检查本仓约定：
1. SKILL.md 是纯路由器，含 frontmatter 不超过 SKILL_MD_MAX_LINES 行
2. SKILL.md 里引用的相对路径（scripts/...、references/...）真实存在
3. scripts/ 固定三层 cmd/core/common；core 层禁止 import cmd
"""

import sys
import os
import re
import yaml
from pathlib import Path

# SKILL.md 行数上限：超出说明流程细节该下沉到 scripts/references
SKILL_MD_MAX_LINES = 120

# 相对路径引用：scripts/xxx.py、references/xxx.md（带或不带 ./ 前缀）
REL_PATH_RE = re.compile(r'(?:\./)?((?:scripts|references)/[\w./-]+\.\w+)')

# core 层反向依赖 cmd 的迹象：from cmd import / import cmd.xxx
CORE_REVERSE_IMPORT_RE = re.compile(r'^\s*(?:from\s+cmd[\w.]*\s+import|import\s+cmd[\w.]*)', re.M)


def check_router_body(skill_path, content):
    """校验 SKILL.md 是否守本仓约定：行数上限 + 引用路径存在 + 分层合规。

    返回 warning 字符串列表（不致命，仅提示）。
    """
    warnings = []
    body_lines = len(content.splitlines())
    if body_lines > SKILL_MD_MAX_LINES:
        warnings.append(
            f"SKILL.md is {body_lines} lines (> {SKILL_MD_MAX_LINES}); "
            f"move step-by-step detail into scripts/ or references/"
        )

    # 引用的相对路径必须存在，避免 SKILL.md 指向幽灵文件
    referenced = set(REL_PATH_RE.findall(content))
    for rel in sorted(referenced):
        if not (skill_path / rel).exists():
            warnings.append(f"SKILL.md references missing path: {rel}")

    # scripts/ 固定三层，单向依赖 cmd -> core -> common
    scripts_dir = skill_path / 'scripts'
    if scripts_dir.is_dir():
        missing_layers = [
            name for name in ('cmd', 'core', 'common')
            if not (scripts_dir / name).is_dir()
        ]
        if missing_layers:
            warnings.append(
                "scripts/ is missing fixed layer dir(s): "
                + ', '.join(missing_layers)
            )
        core_dir = scripts_dir / 'core'
        if core_dir.is_dir():
            for py in core_dir.rglob('*.py'):
                if CORE_REVERSE_IMPORT_RE.search(py.read_text(encoding='utf-8', errors='replace')):
                    warnings.append(
                        f"core layer imports cmd (dependency must be one-way "
                        f"cmd -> core -> common): {py.relative_to(skill_path)}"
                    )

    return warnings


def validate_skill(skill_path):
    """Basic validation of a skill"""
    skill_path = Path(skill_path)

    # Check SKILL.md exists
    skill_md = skill_path / 'SKILL.md'
    if not skill_md.exists():
        return False, "SKILL.md not found"

    # Read and validate frontmatter (utf-8: SKILL.md 常含中文，Windows 默认 GBK 会解码失败)
    content = skill_md.read_text(encoding='utf-8')
    if not content.startswith('---'):
        return False, "No YAML frontmatter found"

    # Extract frontmatter
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return False, "Invalid frontmatter format"

    frontmatter_text = match.group(1)

    # Parse YAML frontmatter
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
        if not isinstance(frontmatter, dict):
            return False, "Frontmatter must be a YAML dictionary"
    except yaml.YAMLError as e:
        return False, f"Invalid YAML in frontmatter: {e}"

    # Define allowed properties: the house spec (§2.4.2) plus Claude Code extensions.
    # 'tools' is accepted as an alias for 'allowed-tools'.
    ALLOWED_PROPERTIES = {
        'name', 'description', 'version', 'author', 'company', 'category',
        'argument-hint', 'allowed-tools', 'tools', 'context', 'tags',
        'license', 'metadata',
    }

    # Check for unexpected properties (excluding nested keys under metadata)
    unexpected_keys = set(frontmatter.keys()) - ALLOWED_PROPERTIES
    if unexpected_keys:
        return False, (
            f"Unexpected key(s) in SKILL.md frontmatter: {', '.join(sorted(unexpected_keys))}. "
            f"Allowed properties are: {', '.join(sorted(ALLOWED_PROPERTIES))}"
        )

    # Check required fields
    if 'name' not in frontmatter:
        return False, "Missing 'name' in frontmatter"
    if 'description' not in frontmatter:
        return False, "Missing 'description' in frontmatter"

    # Extract name for validation
    name = frontmatter.get('name', '')
    if not isinstance(name, str):
        return False, f"Name must be a string, got {type(name).__name__}"
    name = name.strip()
    if name:
        # Check naming convention (hyphen-case: lowercase with hyphens)
        if not re.match(r'^[a-z0-9-]+$', name):
            return False, f"Name '{name}' should be hyphen-case (lowercase letters, digits, and hyphens only)"
        if name.startswith('-') or name.endswith('-') or '--' in name:
            return False, f"Name '{name}' cannot start/end with hyphen or contain consecutive hyphens"
        # Check name length (max 64 characters per spec)
        if len(name) > 64:
            return False, f"Name is too long ({len(name)} characters). Maximum is 64 characters."

    # Extract and validate description
    description = frontmatter.get('description', '')
    if not isinstance(description, str):
        return False, f"Description must be a string, got {type(description).__name__}"
    description = description.strip()
    if description:
        # Check for angle brackets
        if '<' in description or '>' in description:
            return False, "Description cannot contain angle brackets (< or >)"
        # Check description length (max 1024 characters per spec)
        if len(description) > 1024:
            return False, f"Description is too long ({len(description)} characters). Maximum is 1024 characters."

    # Validate context (loading mode)
    context = frontmatter.get('context')
    if context is not None:
        if not isinstance(context, str) or context not in ('pull', 'push'):
            return False, f"'context' must be 'pull' or 'push', got {context!r}"

    # Validate tags (YAML list)
    tags = frontmatter.get('tags')
    if tags is not None and not isinstance(tags, list):
        return False, f"'tags' must be a YAML list, got {type(tags).__name__}"

    # Warn (do not fail) about house-spec fields that are missing
    warnings = []
    for field in ('version', 'author', 'company', 'category', 'tags'):
        if field not in frontmatter or not frontmatter.get(field):
            warnings.append(field)
    if warnings:
        warnings = [f"missing recommended spec 2.4.2 field(s): {', '.join(warnings)}"]

    # House conventions for the generated SKILL.md and scripts layout
    warnings += check_router_body(skill_path, content)

    if warnings:
        listed = '\n  - '.join(warnings)
        return True, f"Skill is valid! (warning(s):\n  - {listed})"

    return True, "Skill is valid!"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python quick_validate.py <skill_directory>")
        sys.exit(1)
    
    valid, message = validate_skill(sys.argv[1])
    print(message)
    sys.exit(0 if valid else 1)