#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
pack —— 把工具打成可分发的 zip

产物是一个**解压即用**的目录（除了 .venv 和两个机器相关的可选件）。
解压方拿到后只需要：
  1) 建 venv：uv venv --python 3.12 .venv && uv pip install -r requirements.txt
  2) 填 Jira 凭据：复制 vendor/jira-tool/scripts/config.example.json → config.json 并填 PAT
     （或改用环境变量 JIRA_PAT / JIRA_SERVER）
  3) 想发邮件的话，把 lark-cli.exe 放进 vendor/lark-cli/

**绝不进包**的东西（这是本脚本存在的主要理由）：
  * .venv/                     —— 42MB，且含机器相关的解释器路径
  * workspace/                 —— 运行时产物（代码快照 265MB / 报告 / 水位）
  * vendor/**/__pycache__/     —— 字节码缓存
  * vendor/jira-tool/scripts/config.json   —— **含真实 Jira PAT**
  * vendor/lark-cli/*.exe      —— 49MB
  * vendor/sources.json        —— 含本机绝对路径
  * config.json 的真实邮箱等   —— 用 config.example.json 代替

用法：
    python tools/pack.py                 # 产出 dist/jira-ticket-analysis-<日期>.zip
    python tools/pack.py --out X.zip
    python tools/pack.py --list          # 只列出会打进去的文件，不产包
    python tools/pack.py --no-date       # 文件名不带日期（可复现）

打包后会做一次**自检**：扫描 zip 内所有文本文件，确认没有泄漏
机器相关的绝对路径与 PAT。发现泄漏直接报错退出。

（自检规则本身见下面的 LEAK_PATTERNS / SECRET_KEY_RE；少数"用途就是记录源位置"
的文档文件在 LEAK_ALLOWLIST 里豁免。）
"""

from __future__ import annotations

import argparse
import datetime as _dt
import re
import sys
import zipfile
from pathlib import Path
from typing import Iterator, List, Tuple

TOOL_DIR = Path(__file__).resolve().parent.parent
DIST_DIR = TOOL_DIR / "dist"

# 目录名：整棵子树都不进包
EXCLUDE_DIRS = {
    ".venv", "workspace", "dist", "__pycache__", ".git",
    ".pytest_cache", ".mypy_cache", "output",
}
# 相对工具根的路径：精确排除
EXCLUDE_FILES = {
    "vendor/jira-tool/scripts/config.json",   # 含真实 PAT
    "vendor/sources.json",                    # 含本机绝对路径
}
# 后缀：不进包
EXCLUDE_SUFFIXES = {".pyc", ".pyo", ".exe", ".zip"}

# 自检：这些模式不该出现在包内的文本文件里
LEAK_PATTERNS = [
    (re.compile(rb"[Cc]:[\\/]Users[\\/]"), "Windows 用户目录绝对路径"),
    (re.compile(rb"[Dd]:[\\/](LZY_project|projects)[\\/]"), "本机项目绝对路径"),
]
# PAT 形态：jira-tool config.json 里的 token 是长 base64-ish 串
SECRET_KEY_RE = re.compile(rb'"(token|password|pat)"\s*:\s*"[^"]{16,}"', re.IGNORECASE)

# 允许出现示例绝对路径的文件（它们的**用途**就是记录源位置，属于文档）
LEAK_ALLOWLIST = {
    "jira-ticket-analysis/vendor/sources.example.json",
    "jira-ticket-analysis/vendor/lark-cli/README.md",
    "jira-ticket-analysis/docs_seed/README.md",
    "jira-ticket-analysis/tools/pack.py",
    "jira-ticket-analysis/tools/sync_vendor.py",
    "jira-ticket-analysis/vendor/.gitignore",
}

# DLP 密文头只可能在**文件开头** —— 代码/文档里提到这个字符串是正常的，不算泄漏。
# 所以只查前 64 字节，而不是全文搜索（全文搜索会把自己的检测代码也命中）。
DLP_MARKER = b"%TSD-Header"

TEXT_SUFFIXES = {
    ".py", ".md", ".json", ".txt", ".cfg", ".ini", ".toml", ".cmd", ".bat",
    ".sh", ".ps1", ".yml", ".yaml", ".example", ".gitignore",
}


def iter_files() -> Iterator[Path]:
    """遍历该进包的文件。"""
    for p in sorted(TOOL_DIR.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(TOOL_DIR)
        if any(part in EXCLUDE_DIRS for part in rel.parts):
            continue
        rel_posix = rel.as_posix()
        if rel_posix in EXCLUDE_FILES:
            continue
        if p.suffix.lower() in EXCLUDE_SUFFIXES:
            continue
        # .venv 里的东西已由 EXCLUDE_DIRS 挡掉；这里再挡一次 .IPGSD 之类
        if p.name.endswith((".IPGSD", ".py.IPGSD")):
            continue
        yield p


def is_text(p: Path) -> bool:
    if p.suffix.lower() in TEXT_SUFFIXES:
        return True
    return p.name in {".gitignore", "LICENSE", "NOTICE"} or p.name.startswith(".git")


def selfcheck(zip_path: Path) -> List[Tuple[str, str]]:
    """
    扫 zip 内文本文件找泄漏。返回 [(成员名, 命中说明)]。
    注意：用 zipfile 读到的内容是**明文**（DLP 对 Python 透明），
    所以这里能可靠地检查真实内容。
    """
    issues: List[Tuple[str, str]] = []
    with zipfile.ZipFile(zip_path) as z:
        for info in z.infolist():
            if info.is_dir():
                continue
            name = info.filename
            if Path(name).suffix.lower() not in TEXT_SUFFIXES and not name.endswith(
                ("/.gitignore", "/LICENSE")
            ):
                continue
            try:
                data = z.read(info)
            except Exception:  # noqa: BLE001
                continue

            # DLP 密文：只看文件头。否则会命中"提到这个字符串"的正常代码与文档。
            if data[:64].startswith(DLP_MARKER):
                issues.append((name, "文件开头是 DLP 密文头 —— 读到的不是源码"))
                continue  # 密文内容没法做其它检查

            # 凭据：任何文件都不允许，无豁免
            m2 = SECRET_KEY_RE.search(data)
            if m2:
                line = data[:m2.start()].count(b"\n") + 1
                issues.append((name, f"疑似凭据（第 {line} 行）: {m2.group(0)[:40]!r}"))

            # 绝对路径：文档类文件豁免（它们的用途就是记录源位置）
            if name in LEAK_ALLOWLIST:
                continue
            for rx, why in LEAK_PATTERNS:
                m = rx.search(data)
                if m:
                    line = data[:m.start()].count(b"\n") + 1
                    issues.append((name, f"{why}（第 {line} 行）: {m.group(0)[:60]!r}"))
    return issues


def main() -> int:
    ap = argparse.ArgumentParser(description="把工具打成可分发的 zip")
    ap.add_argument("--out", help="输出 zip 路径（默认 dist/jira-ticket-analysis-<日期>.zip）")
    ap.add_argument("--list", action="store_true", help="只列出会进包的文件")
    ap.add_argument("--no-date", action="store_true", help="文件名不带日期")
    a = ap.parse_args()

    files = list(iter_files())

    if a.list:
        total = 0
        for p in files:
            size = p.stat().st_size
            total += size
            print(f"  {p.relative_to(TOOL_DIR).as_posix():60} {size:>9,} B")
        print("-" * 74)
        print(f"共 {len(files)} 个文件，{total/1024/1024:.2f} MB（压缩前）")
        return 0

    DIST_DIR.mkdir(parents=True, exist_ok=True)
    if a.out:
        out = Path(a.out)
    else:
        stamp = "" if a.no_date else f"-{_dt.date.today().isoformat()}"
        out = DIST_DIR / f"jira-ticket-analysis{stamp}.zip"

    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for p in files:
            z.write(p, f"jira-ticket-analysis/{p.relative_to(TOOL_DIR).as_posix()}")

    size_mb = out.stat().st_size / 1024 / 1024
    print(f"已产出：{out}")
    print(f"  {len(files)} 个文件，{size_mb:.2f} MB")

    print("\n自检（扫描包内文本文件是否泄漏绝对路径 / 凭据）…")
    issues = selfcheck(out)
    if issues:
        print(f"  ✗ 发现 {len(issues)} 处问题：")
        for name, why in issues[:40]:
            print(f"      {name}\n        {why}")
        print("\n  打包中止：请修掉后再打。")
        out.unlink(missing_ok=True)
        return 1
    print("  ✓ 未发现绝对路径或凭据泄漏")

    print(f"\n解压方需要做的三件事：")
    print(f"  1) uv venv --python 3.12 .venv && uv pip install -r requirements.txt")
    print(f"  2) cp vendor/jira-tool/scripts/config.example.json vendor/jira-tool/scripts/config.json")
    print(f"     （填 Jira PAT；或改用环境变量 JIRA_PAT / JIRA_SERVER）")
    print(f"  3) 要发邮件的话，把 lark-cli.exe 放进 vendor/lark-cli/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
