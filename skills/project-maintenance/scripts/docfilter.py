#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""docfilter.py — project-maintenance :: doc/ 目录过滤规则生成器(stdlib-only)。

职责(对应 config.conf 的 [doc_filter] 段):
  1. 分析 scan_dirs(默认 doc/)里哪些文件该被 .claudeignore 排除 → 按扩展名/路径归类
  2. 回写成 .gitignore 语法规则 → config/doc-filter.txt(回写前备份 .bak)
  3. 把规则合并进工程根 .claudeignore 的受控区段(删除旧段→插入新段,不碰其余内容)
  4. 打印决策表

双通道:
  - 用户手填:直接编辑 config/doc-filter.txt,本脚本 --render-only 只读取不分析
  - 自动分析:auto_analyze=true 时脚本自己扫 doc/ 生成规则

用法:
  python docfilter.py --repo <工程根>                  # 分析 + 回写 + 打印(不碰 .claudeignore)
  python docfilter.py --repo <工程根> --apply-ignore    # 额外合并进 .claudeignore
  python docfilter.py --repo <工程根> --render-only     # 只用 doc-filter.txt 手填内容
  python docfilter.py --repo <工程根> --json

退出码:0 成功 / 2 用法错误 / 3 找不到配置或目录
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[1]
CONFIG_DIR = SKILL_DIR / "config"

# .claudeignore 里的受控区段锚点(重跑时整段替换,不重复堆叠)
MARK_BEGIN = "# === doc/ 过滤 (project-maintenance 自动维护,勿手改本段) ==="
MARK_END = "# === /doc 过滤 ==="

# 二进制/不可读扩展名 → 必须排除(方法论 §2 规则 D:文本 vs 二进制)
DOC_BINARY_EXTS = {
    ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".ods", ".odp",
    ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp", ".ico", ".tif", ".tiff", ".svg",
    ".zip", ".7z", ".rar", ".tar", ".gz", ".tgz", ".bz2", ".xz",
    ".exe", ".dll", ".so", ".bin", ".iso", ".msi", ".db", ".sqlite", ".sqlite3",
    ".mp3", ".mp4", ".avi", ".mkv", ".mov", ".wav", ".flac", ".ogg", ".webm",
}
# 文本类扩展名 → 必须保留(方法论 §7 误判第 4 条:业务文档 .md 是理解上下文的关键)
DOC_TEXT_EXTS = {".md", ".markdown", ".txt", ".rst", ".adoc", ".text"}
BIG_TEXT_BYTES = 512 * 1024   # 单个文本文件超过此值 → 提示但不自动排除


def setup_stdout():
    try:
        if sys.stdout.encoding and sys.stdout.encoding.casefold() not in ("utf-8", "utf8"):
            sys.stdout.reconfigure(encoding="utf-8")
        if sys.stderr.encoding and sys.stderr.encoding.casefold() not in ("utf-8", "utf8"):
            sys.stderr.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass


def die(code: int, msg: str):
    print(f"ERROR({code}): {msg}", file=sys.stderr)
    sys.exit(code)


# ---------------- 配置 ----------------
def load_config(path: Path = None) -> dict:
    """读 config.conf,支持 [section] 分节;返回 {(section,key): value} + {'': 无节键}。"""
    p = path or (CONFIG_DIR / "config.conf")
    if not p.exists():
        p = CONFIG_DIR / "config.conf.example"
    cfg: dict = {}
    if not p.exists():
        return cfg
    section = ""
    for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
        s = line.strip()
        if not s or s.startswith("#") or s.startswith(";"):
            continue
        if s.startswith("[") and s.endswith("]"):
            section = s[1:-1].strip().casefold()
            continue
        if "=" not in s:
            continue
        k, _, v = s.partition("=")
        cfg[(section, k.strip().casefold())] = v.strip()
    return cfg


def cfg_get(cfg: dict, section: str, key: str, default: str = "") -> str:
    return cfg.get((section.casefold(), key.casefold()), default)


def cfg_bool(cfg: dict, section: str, key: str, default: bool = False) -> bool:
    v = cfg_get(cfg, section, key, "")
    if not v:
        return default
    return v.casefold() in ("1", "true", "yes", "on")


def cfg_list(cfg: dict, section: str, key: str, default: str = "") -> list:
    raw = cfg_get(cfg, section, key, default)
    return [x.strip().replace("\\", "/").rstrip("/") for x in raw.split(",") if x.strip()]


# ---------------- 分析 ----------------
def analyze(root: Path, scan_dirs: list) -> dict:
    """扫 scan_dirs,按扩展名归类。返回 {bins:{ext:[rel..]}, big_text:[rel..], kept:int}。"""
    bins: dict = {}
    big_text: list = []
    kept = 0
    for d in scan_dirs:
        base = root / d
        if not base.is_dir():
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = sorted(x for x in dirnames if not x.startswith(".git"))
            for f in sorted(filenames):
                fp = Path(dirpath) / f
                ext = fp.suffix.casefold()
                rel = fp.relative_to(root).as_posix()
                if f.casefold() in ("thumbs.db", "desktop.ini"):
                    bins.setdefault("os-junk", []).append(rel)
                    continue
                if ext in DOC_BINARY_EXTS:
                    bins.setdefault(ext, []).append(rel)
                elif ext in DOC_TEXT_EXTS or not ext:
                    kept += 1
                    try:
                        if fp.stat().st_size > BIG_TEXT_BYTES:
                            big_text.append(rel)
                    except OSError:
                        pass
                else:
                    kept += 1   # 未知扩展名保守保留,不猜
    return {"bins": bins, "big_text": big_text, "kept": kept}


def render_rules(analysis: dict) -> list:
    """二进制归类 → 自动生成区规则行(按扩展名合并,不逐文件列)。"""
    lines = [
        "# ==== 自动生成区(docfilter.py 分析 scan_dirs 后重写,勿手改) ====",
    ]
    exts = sorted(e for e in analysis["bins"] if e.startswith("."))
    if exts or "os-junk" in analysis["bins"]:
        lines.append("# 二进制文档 → 排除(进上下文也是乱码)")
    for e in exts:
        lines.append(f"*{e}")
    if "os-junk" in analysis["bins"]:
        lines += ["Thumbs.db", "desktop.ini"]
    lines += [
        "# 例外:业务文档必须保留(见方法论 §7 误判第 4 条)",
        "!**/CLAUDE.md",
        "!**/*.md",
    ]
    return lines


GEN_MARK = "# ==== 自动生成区"


def split_handwritten(rules_file: Path) -> list:
    """读现有规则文件,返回手填区行(自动生成区锚点之前的全部内容)。

    - 新格式(含 GEN_MARK 锚点):锚点之前 = 手填区,原样保留。
    - 老格式(无锚点):非注释的有效规则行视作用户手填,全部保留进手填区
      (宁可与分析结果重复去重,也不丢用户手写内容)。
    文件不存在 → 返回带说明的空手填区骨架。
    """
    header = [
        "# doc/ 目录过滤规则 —— .gitignore 语法,一行一条",
        "# 路径相对工程根;支持目录(doc/xxx/)、文件(doc/a/b.pdf)、通配(*.tmp)、取反(!path)",
        "# 不支持绝对路径。锚点「自动生成区」以下由 docfilter.py 维护,手改会被覆盖;",
        "# 要手填规则写在锚点上方任意位置即可,脚本永不改动。",
        "",
    ]
    if not rules_file.exists():
        return header
    old = rules_file.read_text(encoding="utf-8", errors="replace").splitlines()
    for i, ln in enumerate(old):
        if ln.startswith(GEN_MARK):
            return old[:i] if old[:i] else header
    # 老格式:无锚点 → 有效规则行升级为手填区
    keep = [ln for ln in old if ln.strip() and not ln.startswith("#")]
    return header + keep + [""] if keep else header


def write_back(rules_file: Path, gen_lines: list) -> str:
    """回写规则文件(备份 .bak):手填区保留 + 生成区重写。返回 'written'/'unchanged'。"""
    new = "\n".join(split_handwritten(rules_file) + gen_lines).rstrip() + "\n"
    if rules_file.exists() and rules_file.read_text(encoding="utf-8", errors="replace") == new:
        return "unchanged"
    if rules_file.exists():
        shutil.copy2(rules_file, rules_file.with_suffix(rules_file.suffix + ".bak"))
    rules_file.parent.mkdir(parents=True, exist_ok=True)
    rules_file.write_text(new, encoding="utf-8", newline="\n")
    return "written"


def merge_claudeignore(ci: Path, rules_lines: list) -> str:
    """把规则合并进 .claudeignore 受控区段(整段替换,去重)。返回 'created'/'updated'/'unchanged'。"""
    body: list = []
    for ln in rules_lines:
        if ln.strip() and not ln.startswith("#") and ln not in body:
            body.append(ln)
    block = [MARK_BEGIN] + body + [MARK_END]
    if ci.exists():
        old = ci.read_text(encoding="utf-8", errors="replace").splitlines()
    else:
        old = []
    kept: list = []
    i, found, old_block = 0, False, []
    while i < len(old):
        if old[i].strip() == MARK_BEGIN:
            found = True
            j = i
            while j < len(old) and old[j].strip() != MARK_END:
                old_block.append(old[j])
                j += 1
            if j < len(old):
                old_block.append(old[j])
            i = j + 1
            continue
        kept.append(old[i])
        i += 1
    if found and old_block == block:
        return "unchanged"
    out_lines = kept
    while out_lines and not out_lines[-1].strip():
        out_lines.pop()
    out_lines += [""] + block
    ci.parent.mkdir(parents=True, exist_ok=True)
    ci.write_text("\n".join(out_lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    return "updated" if found else "created"


def main(argv: list) -> int:
    setup_stdout()
    ap = argparse.ArgumentParser(prog="docfilter.py", description="doc/ 过滤规则生成器")
    ap.add_argument("--repo", help="工程根目录(默认当前目录)")
    ap.add_argument("--config", help="config.conf 路径(默认 skill 自带)")
    ap.add_argument("--apply-ignore", action="store_true",
                    help="额外把规则合并进工程根 .claudeignore")
    ap.add_argument("--render-only", action="store_true",
                    help="不分析,只用 doc-filter.txt 现有手填内容")
    ap.add_argument("--no-write", action="store_true", help="只打印不回写")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    root = Path(args.repo).resolve() if args.repo else Path.cwd().resolve()
    if not root.is_dir():
        die(3, f"工程根不存在: {root}")
    cfg = load_config(Path(args.config) if args.config else None)

    scan_dirs = cfg_list(cfg, "doc_filter", "scan_dirs", "doc")
    rules_name = cfg_get(cfg, "doc_filter", "file", "doc-filter.txt")
    auto = cfg_bool(cfg, "doc_filter", "auto_analyze", True)
    writeback = cfg_bool(cfg, "doc_filter", "writeback", True) and not args.no_write
    rules_file = CONFIG_DIR / rules_name

    missing = [d for d in scan_dirs if not (root / d).is_dir()]
    if missing:
        die(3, f"scan_dirs 不存在于工程根: {', '.join(missing)}(检查 config.conf [doc_filter] scan_dirs)")

    if args.render_only or not auto:
        # 手填通道:只读现有规则
        lines = rules_file.read_text(encoding="utf-8", errors="replace").splitlines() \
            if rules_file.exists() else []
        gen_lines: list = []
        analysis = {"bins": {}, "big_text": [], "kept": 0}
        src = "hand-filled"
    else:
        # 分析通道:手填区保留 + 生成区按扫描结果重写
        analysis = analyze(root, scan_dirs)
        gen_lines = render_rules(analysis)
        lines = split_handwritten(rules_file) + gen_lines
        src = "analyzed"

    wb_status = "skipped"
    if writeback and src == "analyzed":
        wb_status = write_back(rules_file, gen_lines)

    ci_status = "skipped"
    ci_path = root / ".claudeignore"
    if args.apply_ignore:
        ci_status = merge_claudeignore(ci_path, lines)

    if args.json:
        print(json.dumps({
            "repo": str(root), "scan_dirs": scan_dirs, "source": src,
            "rules_file": str(rules_file), "writeback": wb_status,
            "claudeignore": ci_status,
            "binary_exts": sorted(e for e in analysis["bins"] if e.startswith(".")),
            "binary_files": sum(len(v) for v in analysis["bins"].values()),
            "kept_text_files": analysis["kept"],
            "big_text": analysis["big_text"],
        }, ensure_ascii=False))
        return 0

    print(f"repo={root}")
    print(f"scan_dirs={', '.join(scan_dirs)}  规则来源={src}  规则文件={rules_file}")
    print("-" * 72)
    if src == "analyzed":
        bins = analysis["bins"]
        print(f"{'扩展名':<14}{'文件数':>7}   示例")
        for e in sorted(bins, key=lambda k: -len(bins[k])):
            sample = bins[e][0] if bins[e] else ""
            print(f"{e:<14}{len(bins[e]):>7}   {sample[:52]}")
        print(f"{'(文本/保留)':<14}{analysis['kept']:>7}   (含 .md,不排除)")
        if analysis["big_text"]:
            print(f"\n提示: {len(analysis['big_text'])} 个文本文件 >{BIG_TEXT_BYTES // 1024}KB"
                  f"(建议人工判断是否拆分,本轮未自动排除):")
            for f in analysis["big_text"][:5]:
                print(f"    {f}")
    else:
        print(f"手填规则共 {len([x for x in lines if x.strip() and not x.startswith('#')])} 条")
    print("-" * 72)
    print(f"规则回写: {wb_status}    .claudeignore 合并: {ci_status}")
    if ci_status != "skipped":
        print(f"  → {ci_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
