#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""port_scan.py — 移植分析用的目录扫描器。

盘点文件/行数/本地 include 依赖，输出 markdown 表。
设计要点：公司 DLP 透明加密下 bash/grep 读到密文，Python 直读是明文——
本脚本即利用这一点做可靠盘点；若个别文件仍读到密文，标 [CIPHER] 不崩溃。

用法:
  python port_scan.py <目录>... [--depth N] [--ext .c,.h] [--deps]
                      [--grep PATTERN] [--sort lines|path] [--json]

  --depth N    相对根目录的最大层级（默认 8）
  --ext        只统计这些扩展名（默认 .c,.h）
  --deps       解析本地 include（"..." 形式）落点: 文件内 / 缺失 / 外部目录
  --grep RE    额外列出各文件中匹配该正则的行（如 --grep "_LOWINF_EN"）
  --sort       path(默认,目录序) 或 lines(行数降序)
  --json       输出 JSON 而非 markdown
"""
import argparse
import json
import os
import re
import sys

INCLUDE_RE = re.compile(r'^\s*#include\s*"([^"]+)"', re.M)
CIPHER_MARK = b"%TSD-Header"
NON_PRINTABLE_RATIO = 0.30


def _decode(raw: bytes) -> str:
    for enc in ("utf-8-sig", "utf-8", "gbk"):
        try:
            return raw.decode(enc)
        except (UnicodeDecodeError, LookupError):
            continue
    return raw.decode("latin-1")


def _is_cipher(raw: bytes, text: str) -> bool:
    if CIPHER_MARK in raw[:512]:
        return True
    if not text:
        return False
    bad = sum(1 for ch in text if not ch.isprintable() and ch not in "\t\n\r")
    return bad / len(text) > NON_PRINTABLE_RATIO


def scan_file(path: str, grep_re: re.Pattern | None) -> dict:
    info = {"path": path, "lines": 0, "cipher": False, "includes": [], "grep_hits": []}
    try:
        with open(path, "rb") as f:
            raw = f.read()
    except OSError as e:
        info["cipher"] = True
        info["error"] = str(e)
        return info
    text = _decode(raw)
    if _is_cipher(raw, text):
        info["cipher"] = True
        return info
    info["lines"] = text.count("\n") + (0 if text.endswith("\n") or not text else 1)
    info["includes"] = INCLUDE_RE.findall(text)
    if grep_re is not None:
        info["grep_hits"] = [
            f"{i + 1}: {line.strip()}"
            for i, line in enumerate(text.splitlines())
            if grep_re.search(line)
        ]
    return info


def walk(root: str, exts: set, depth: int) -> list:
    root = os.path.abspath(root)
    out = []
    for dirpath, dirnames, filenames in os.walk(root):
        rel_dir = os.path.relpath(dirpath, root)
        if rel_dir != "." and rel_dir.count(os.sep) + 1 > depth:
            dirnames[:] = []
            continue
        dirnames[:] = [d for d in dirnames if d not in (".git", ".claude", "output")]
        for name in sorted(filenames):
            if exts and os.path.splitext(name)[1].lower() not in exts:
                continue
            out.append(os.path.join(dirpath, name))
    return out


def main():
    ap = argparse.ArgumentParser(description="扫描目录: 文件/行数/include 依赖盘点")
    ap.add_argument("roots", nargs="+", help="待扫描目录(可多个)")
    ap.add_argument("--depth", type=int, default=8)
    ap.add_argument("--ext", default=".c,.h")
    ap.add_argument("--deps", action="store_true", help="解析本地 include 落点")
    ap.add_argument("--grep", default=None, help="列出匹配正则的行")
    ap.add_argument("--sort", choices=["path", "lines"], default="path")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass

    exts = {e.strip().lower() for e in args.ext.split(",") if e.strip()}
    grep_re = re.compile(args.grep) if args.grep else None

    records = []
    for root in args.roots:
        if not os.path.isdir(root):
            print(f"[WARN] 目录不存在: {root}", file=sys.stderr)
            continue
        base = os.path.abspath(root)
        for p in walk(root, exts, args.depth):
            info = scan_file(p, grep_re)
            info["path"] = os.path.relpath(p, base)
            info["root"] = base
            records.append(info)

    if args.sort == "lines":
        records.sort(key=lambda r: -r["lines"])
    else:
        records.sort(key=lambda r: (r["root"], r["path"].lower()))

    if args.json:
        print(json.dumps(records, ensure_ascii=False, indent=1))
        return

    total_lines = sum(r["lines"] for r in records)
    n_cipher = sum(1 for r in records if r["cipher"])
    for root in dict.fromkeys(r["root"] for r in records):
        subset = [r for r in records if r["root"] == root]
        n = len(subset)
        print(f"## 扫描: {root} — {n} 文件, {sum(r['lines'] for r in subset)} 行"
              + (f" ({sum(1 for r in subset if r['cipher'])} 密文)" if any(r['cipher'] for r in subset) else ""))
        print()
        print("| 文件 | 行数 | 本地 include |")
        print("|---|---|---|")
        for r in subset:
            inc = ", ".join(dict.fromkeys(r["includes"][:6])) or "—"
            if len(r["includes"]) > 6:
                inc += f" …(+{len(r['includes']) - 6})"
            mark = " **[CIPHER]**" if r["cipher"] else ""
            print(f"| `{r['path']}`{mark} | {r['lines']} | {inc} |")
        print()
    print(f"**合计**: {len(records)} 文件, {total_lines} 行"
          + (f", {n_cipher} 个密文文件(需用 Read 工具读)" if n_cipher else ""))

    if grep_re is not None:
        print()
        print("## grep 命中")
        for r in records:
            if r["grep_hits"]:
                print(f"\n`{r['path']}`:")
                for h in r["grep_hits"]:
                    print(f"  {h}")

    if args.deps:
        print()
        print("## include 落点")
        by_name = {os.path.basename(r["path"]): r["path"] for r in records}
        missing, ext_inc = {}, {}
        for r in records:
            full = os.path.join(r["root"], r["path"])
            d = os.path.dirname(full)
            for inc in r["includes"]:
                if os.path.exists(os.path.join(d, inc)):
                    continue
                base = os.path.basename(inc)
                if base in by_name:
                    ext_inc.setdefault(inc, []).append(r["path"])
                else:
                    missing.setdefault(inc, []).append(r["path"])
        print("\n跨目录 include(依赖闭包候选,按被引次数排序):")
        for inc, users in sorted(ext_inc.items(), key=lambda kv: -len(kv[1])):
            print(f"  {inc}  ← {len(users)} 处引用, 如 {users[0]}")
        print("\n工程内未找到(外部库/RTD/需另扫):")
        for inc in sorted(missing):
            print(f"  {inc}  ← {missing[inc][0]}")


if __name__ == "__main__":
    main()
