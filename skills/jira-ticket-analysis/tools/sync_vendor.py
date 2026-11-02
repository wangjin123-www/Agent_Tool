#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
sync_vendor —— 把外部工具搬进本工具的 vendor/，让本工具自包含

为什么需要这个脚本：
  本工具以前靠 config.json 的 paths 块用绝对路径引用外部工具（jira-tool、
  AI_Log_parsing、AI_canlog、claude-md-map），换机器/换目录就全挂，也没法打包。
  现在改成把它们的**源码**拷进 vendor/，运行时用相对路径解析。

这是整个工具里**唯一**允许出现绝对路径的地方，而且只在开发期跑一次
（上游工具更新时重跑刷新）。运行时不存在任何外部路径依赖。

用法：
    python tools/sync_vendor.py            # 按 vendor/sources.json 搬运
    python tools/sync_vendor.py --check    # 只体检，不拷贝
    python tools/sync_vendor.py --list     # 看当前 vendor/ 里有什么

前置：把 vendor/sources.example.json 复制成 vendor/sources.json 并填好本机源路径。
      sources.json 进 .gitignore，不进包（它是机器相关的）。

注意：公司 DLP 会给部分 .py 加 %TSD-Header 密文头，但**对 Python 进程透明解密** ——
      实测 shutil.copy2 / zipfile 读到的都是明文，所以拷进来的源码是可用的。
      但 shell 的 head/cat/grep 会看到密文，别被吓到。
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, List

TOOL_DIR = Path(__file__).resolve().parent.parent
VENDOR_DIR = TOOL_DIR / "vendor"
SOURCES = VENDOR_DIR / "sources.json"
SOURCES_EXAMPLE = VENDOR_DIR / "sources.example.json"

# 搬运时永远跳过的东西
SKIP_DIRS = {"__pycache__", ".git", ".pytest_cache", ".mypy_cache"}
SKIP_SUFFIXES = {".pyc", ".pyo"}


def _ignore(_dir: str, names: List[str]) -> List[str]:
    return [n for n in names if n in SKIP_DIRS or Path(n).suffix in SKIP_SUFFIXES]


def load_sources() -> Dict[str, Any]:
    if not SOURCES.exists():
        raise SystemExit(
            f"缺少 {SOURCES}\n"
            f"请先复制模板并填好本机源路径：\n"
            f'  copy "{SOURCES_EXAMPLE}" "{SOURCES}"\n'
            f"（sources.json 是机器相关的，已进 .gitignore，不进分发包）"
        )
    raw = SOURCES.read_text(encoding="utf-8")
    return json.loads("\n".join(
        ln for ln in raw.splitlines() if not ln.lstrip().startswith("//")
    ))


def copy_entry(name: str, spec: Dict[str, Any], *, check: bool) -> Dict[str, Any]:
    """搬一个条目。返回体检结果。"""
    src_root = Path(spec["src"])
    dest_root = TOOL_DIR / spec["dest"]
    include = spec.get("include") or ["."]
    optional = bool(spec.get("optional"))

    result: Dict[str, Any] = {
        "name": name, "src": str(src_root), "dest": str(dest_root),
        "optional": optional, "copied": [], "missing": [], "skipped": False,
    }

    if not src_root.exists():
        if optional:
            result["skipped"] = True
            result["reason"] = "可选依赖，源不存在（正常，按需手动放入）"
            return result
        result["missing"].append(str(src_root))
        return result

    for item in include:
        src = src_root / item
        if not src.exists():
            result["missing"].append(str(src))
            continue
        dest = dest_root / item
        if check:
            result["copied"].append(f"{item} (would copy)")
            continue
        if src.is_dir():
            dest.mkdir(parents=True, exist_ok=True)
            shutil.copytree(src, dest, dirs_exist_ok=True, ignore=_ignore)
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)
        result["copied"].append(item)
    return result


def reset_canlog_config() -> None:
    """
    canlog_config.json 由 AI_canlog 自己写入，带机器绝对路径（output_root + history）。
    搬进来后必须重置，否则留着会误导（虽然 jta_attach 总是传 --out 覆盖它）。
    """
    cfg = VENDOR_DIR / "canlog" / "canlog_config.json"
    if not cfg.exists():
        return
    try:
        data = json.loads(cfg.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return
    data.pop("history", None)
    # output_root 是相对 AI_canlog 根目录的 "output"；搬到 vendor/ 后仍相对 canlog_tool 的父目录，
    # 所以保持相对写法即可，绝不留绝对路径
    data["output_root"] = "output"
    cfg.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def write_gitignore_for_vendor() -> None:
    """vendor/ 下自带的 .gitignore：确保机器相关文件不被提交。"""
    VENDOR_DIR.mkdir(parents=True, exist_ok=True)
    (VENDOR_DIR / ".gitignore").write_text(
        "# 机器相关，不进版本库也不进分发包\n"
        "sources.json\n"
        "jira-tool/scripts/config.json\n"
        "lark-cli/*.exe\n"
        "\n# 上游工具自带的缓存\n"
        "__pycache__/\n"
        "canlog/output/\n",
        encoding="utf-8",
    )


def main() -> int:
    ap = argparse.ArgumentParser(description="把外部工具搬进 vendor/，让本工具自包含")
    ap.add_argument("--check", action="store_true", help="只体检不拷贝")
    ap.add_argument("--list", action="store_true", help="列出 vendor/ 现有内容")
    a = ap.parse_args()

    if a.list:
        if not VENDOR_DIR.exists():
            print("vendor/ 还不存在")
            return 0
        for p in sorted(VENDOR_DIR.rglob("*")):
            if p.is_file() and "__pycache__" not in p.parts:
                rel = p.relative_to(VENDOR_DIR)
                print(f"  {str(rel):55} {p.stat().st_size:>9,} B")
        return 0

    sources = load_sources()
    print(f"TOOL_DIR : {TOOL_DIR}")
    print(f"模式     : {'体检（不拷贝）' if a.check else '搬运'}")
    print("=" * 66)

    all_ok = True
    for name, spec in sources.items():
        if name.startswith("//"):
            continue  # 允许 JSON 里写 // 注释行
        r = copy_entry(name, spec, check=a.check)
        if r["missing"]:
            all_ok = False
            print(f"✗ {name}")
            for m in r["missing"]:
                print(f"    缺失: {m}")
        elif r["skipped"]:
            print(f"○ {name:16} 跳过（{r['reason']}）")
        else:
            verb = "待拷贝" if a.check else "已搬入"
            print(f"✓ {name:16} {verb} {len(r['copied'])} 项 → {r['dest']}")

    if not a.check and all_ok:
        reset_canlog_config()
        write_gitignore_for_vendor()
        print("-" * 66)
        print("已重置 vendor/canlog/canlog_config.json（去 history、output_root 改相对）")
        print("已写 vendor/.gitignore")

    print("=" * 66)
    print("结论：", "全部就绪 ✓" if all_ok else "有缺失 ✗（见上）")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
