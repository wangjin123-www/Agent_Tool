#!/usr/bin/env python3
"""s32k3-rtd-master 业务层：核心逻辑。只被 scripts/cmd/* 调用，禁止 import cmd。

数据来源：
- 训练库根路径（绝对路径）来自 config/config.conf 的 [paths].training_root
- 教学文档为 references/*.md（按外设分篇，代码原样摘录）
本层只做确定性的索引 / 定位 / 抽取，不做任何"改写代码"的动作。
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common.conf import load_config, root          # noqa: E402
from common.log import log                          # noqa: E402

# 项目名(小写) -> references 文档 的映射规则；按顺序匹配，首个命中生效。
# 顺序有意为之：lpspi/flexiospi 必须在 dma 之前（LPSPI_WithDMA 含 "dma"）。
TOPIC_RULES = [
    (("wkup", "wakeup"), "wkup.md"),
    (("can",), "can.md"),
    (("emios",), "emios.md"),
    (("c40",), "flash.md"),
    (("fls",), "flash.md"),
    (("fee",), "flash.md"),
    (("adc", "bctu"), "adc.md"),
    (("lpspi", "flexiospi"), "spi.md"),
    (("iic", "lpi2c"), "iic.md"),
    (("lin",), "lin.md"),
    (("uart",), "uart.md"),
    (("rtc",), "rtc.md"),
    (("intctrl", "siul2_icu", "pit_stm", "osif"), "timing.md"),
    (("edma", "dma"), "dma.md"),
    (("crc", "trgmux", "lcu", "swt"), "misc1.md"),
    (("sent", "flexio", "hse", "gmac", "sai"), "misc2.md"),
]


def _training_root():
    """从 config 读训练库根路径。缺失则返回 None。"""
    cfg = load_config()
    raw = cfg.get("paths", "training_root", fallback="").strip()
    return Path(raw) if raw else None


def _ref_dir():
    return root() / "references"


def _doc_for(name):
    """项目目录名 -> references 文档名；无匹配返回 None。"""
    low = name.lower()
    for keys, doc in TOPIC_RULES:
        if any(k in low for k in keys):
            return doc
    return None


def _projects(troot):
    """扫描训练库下所有含 .cproject 的工程目录。"""
    if not troot or not troot.exists():
        return []
    return sorted(
        (d for d in troot.iterdir() if d.is_dir() and (d / ".cproject").exists()),
        key=lambda p: p.name.lower(),
    )


def _all_ref_docs():
    return sorted(p.name for p in _ref_dir().glob("*.md"))


def _match_ref_docs(keyword):
    """关键词匹配 references 文档：先按 stem 精确/前缀，再全文命中。"""
    kw = keyword.lower()
    docs = []
    for p in _ref_dir().glob("*.md"):
        if kw in p.stem.lower():
            docs.append(p)
    if not docs:
        for p in _ref_dir().glob("*.md"):
            try:
                if kw in p.read_text(encoding="utf-8", errors="ignore").lower():
                    docs.append(p)
            except OSError:
                continue
    return sorted(docs, key=lambda p: p.name)


# ---------------------------------------------------------------- list

def cmd_list(arg=None):
    """列出训练库外设工程索引；arg 为关键词时做过滤。"""
    troot = _training_root()
    if not troot:
        log("[ERR] 未配置训练库路径：请在 config/config.conf 的 [paths].training_root 填写绝对路径")
        return 2
    if not troot.exists():
        log(f"[ERR] 训练库路径不存在: {troot}")
        return 2

    projects = _projects(troot)
    kw = (arg or "").strip().lower()
    rows = []
    for d in projects:
        if kw and kw not in d.name.lower():
            continue
        rows.append((d.name, _doc_for(d.name) or "-", str(d)))

    log(f"训练库: {troot}")
    log(f"工程数: {len(rows)}" + (f"（关键词过滤: {arg}）" if kw else ""))
    log("")
    log(f"{'工程目录':<40} {'教学文档':<14} 路径")
    log("-" * 110)
    for name, doc, path in rows:
        log(f"{name:<40} {doc:<14} {path}")
    log("")
    log("references 文档清单: " + ", ".join(_all_ref_docs()))
    return 0


# -------------------------------------------------------------- lookup

def cmd_lookup(arg=None):
    """定位某外设对应的训练工程路径 + 教学文档路径。"""
    if not arg:
        log("用法: python scripts/cmd/cmd_lookup.py <外设关键词>  例: wkpu / can / adc / flash")
        return 1
    kw = arg.strip().lower()

    troot = _training_root()
    hits = [d for d in _projects(troot) if kw in d.name.lower()]
    docs = _match_ref_docs(arg.strip())

    log(f"关键词: {arg}")
    log("")
    log("== 训练工程 ==")
    if hits:
        for d in hits:
            log(f"  {d}")
            for f in ("src/main.c", "src\\main.c"):
                mc = d / f
                if mc.exists():
                    n = len(mc.read_text(encoding="utf-8", errors="ignore").splitlines())
                    log(f"      main.c: {mc}  ({n} 行)")
                    break
    else:
        log("  (无匹配工程)")

    log("")
    log("== 教学文档 ==")
    if docs:
        for p in docs:
            n = len(p.read_text(encoding="utf-8", errors="ignore").splitlines())
            log(f"  {p}  ({n} 行)")
    else:
        log("  (无匹配文档)")
    return 0 if (hits or docs) else 1


# --------------------------------------------------------------- guide

_CODE_FENCE = re.compile(r"^\s*```")


def _extract_doc(path):
    """抽取 markdown 的章节标题与 fenced code 块，保持原文顺序。"""
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    items = []
    in_code = False
    buf = []
    for ln in lines:
        if _CODE_FENCE.match(ln):
            if not in_code:
                in_code = True
                buf = [ln]
            else:
                buf.append(ln)
                items.append(("code", "\n".join(buf)))
                in_code = False
                buf = []
            continue
        if in_code:
            buf.append(ln)
        elif re.match(r"^#{1,4}\s+", ln):
            items.append(("head", ln))
    return items


def cmd_guide(arg=None):
    """按外设抽取教学文档中的标题 + 原样代码块，生成写码指导到 output/。"""
    if not arg:
        log("用法: python scripts/cmd/cmd_guide.py <外设关键词>  例: spi / emios / flash / wkup")
        return 1
    docs = _match_ref_docs(arg.strip())
    if not docs:
        log(f"[ERR] 未找到与 '{arg}' 相关的教学文档。可用: " + ", ".join(_all_ref_docs()))
        return 1

    troot = _training_root()
    hits = [d for d in _projects(troot) if arg.strip().lower() in d.name.lower()]

    out_dir = root() / "output"
    out_dir.mkdir(exist_ok=True)
    out_file = out_dir / f"guide_{arg.strip().lower()}.md"

    parts = [f"# 写码指导: {arg}", ""]
    if hits:
        parts += ["## 参考工程", ""]
        parts += [f"- {d}" for d in hits]
        parts += [""]

    code_total = 0
    for doc in docs:
        items = _extract_doc(doc)
        n_code = sum(1 for k, _ in items if k == "code")
        code_total += n_code
        parts += [f"## 来源文档: {doc.name}  ({doc})", ""]
        parts += [f"> 共 {n_code} 个原样代码块", ""]
        for kind, payload in items:
            if kind == "head":
                parts += [payload, ""]
            else:
                parts += [payload, ""]

    out_file.write_text("\n".join(parts), encoding="utf-8")
    log(f"关键词: {arg}")
    log(f"命中文档: " + ", ".join(d.name for d in docs))
    log(f"参考工程: " + (", ".join(d.name for d in hits) if hits else "(无)"))
    log(f"抽取原样代码块: {code_total} 个")
    log(f"写码指导已写出: {out_file}")
    return 0


# ----------------------------------------------------------------- rm (手册)

# 这些主题在 DS 数据手册，不在 RM —— 命中时提示改查 DS 单文件。
_DS_HINTS = ("电压", "电流", "电气", "封装", "esd", "去耦", "热特性", "thermal",
             "absolute", "rating", "功耗", "supply", "ordering", "电源参数")

_RM_ROW = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*(\d+)-(\d+)\s*\|\s*(.+?)\s*\|$")
_RM_MAP_TITLE = "## 5. 119 文件地图"


def _docs_root():
    """手册库根目录：config [paths].docs_root > skill 内 docs/NXP_S32K3 > 工程旧路径 doc/NXP_S32K3。"""
    cfg = load_config()
    raw = cfg.get("paths", "docs_root", fallback="").strip()
    cands = []
    if raw:
        cands.append(Path(raw))
    cands.append(root() / "docs" / "NXP_S32K3")            # 手册库随 skill 分发（正主）
    cands.append(root().parents[2] / "doc" / "NXP_S32K3")  # 兼容工程内旧位置
    for p in cands:
        if p.exists():
            return p
    return None


def _rm_map():
    """解析 references/rm-ds.md 地图 -> [(chapter, file, start, end, title)]。"""
    src = _ref_dir() / "rm-ds.md"
    if not src.exists():
        return []
    rows, chapter, in_map = [], "", False
    for ln in src.read_text(encoding="utf-8", errors="ignore").splitlines():
        if ln.startswith(_RM_MAP_TITLE):
            in_map = True
            continue
        if not in_map:
            continue
        m = re.match(r"^##\s+(.+?)\s*$", ln)
        if m and m.group(1).isascii():      # 地图区内的 ## 均为章名（Clocking/Timer 等可无下划线）
            chapter = m.group(1)
            continue
        m = _RM_ROW.match(ln)
        if m:
            rows.append((chapter, m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)))
    return rows


def cmd_rm(arg=None):
    """在 S32K3xx RM/DS 手册 markdown 库中定位模块文件（页码 + Grep 建议）。"""
    droot = _docs_root()
    if not droot:
        log("[ERR] 手册库不存在：doc/NXP_S32K3 缺失，或 config.conf [paths].docs_root 配置错误")
        return 2

    rows = _rm_map()
    if not rows:
        log("[ERR] references/rm-ds.md 地图缺失或无可解析行")
        return 2

    if not arg:
        from collections import OrderedDict
        by = OrderedDict()
        for ch, _f, _a, _b, _t in rows:
            by.setdefault(ch, []).append(_f)
        log(f"手册库: {droot}")
        log(f"RM 模块文件: {len(rows)}；DS 单文件: S32K3xxDS_数据手册.md")
        log("")
        for ch, fs in by.items():
            log(f"  {ch:<34} {len(fs)} 文件")
        log("")
        log("用法: python scripts/cmd/cmd_rm.py <关键词>  例: wkpu / mc_cgm / lpuart / flash")
        return 0

    kw = arg.strip().lower()
    if kw in ("wkup", "wakeup"):          # 常用别名归一到 RM 模块名
        kw = "wkpu"

    hits = [r for r in rows if kw in r[1].lower() or kw in r[4].lower()]
    log(f"关键词: {arg}")
    log("")
    log("== RM 模块文件 ==")
    if hits:
        for ch, f, a, b, t in hits[:30]:
            exists = (droot / "RM" / ch / f).exists()
            log(f"  RM/{ch}/{f}  p{a}-{b}  {t}" + ("" if exists else "  [文件缺失!]"))
        if len(hits) > 30:
            log(f"  ...另有 {len(hits) - 30} 个命中")
        log("")
        log("== 下一步 Grep（在命中文件内） ==")
        log("  寄存器描述:  ####.*\\b<缩写>\\b   例 (WIFEER)")
        log("  模块基地址:  base address")
        log("  位域定义:    ^Bits ")
    else:
        log("  (无匹配；换模块标准名，如 siul2 / mc_me / mc_cgm / emios / flexcan)")

    if any(h in kw for h in _DS_HINTS):
        log("")
        log("== DS 提示 ==")
        log(f"  该主题属器件级参数，改查 {droot / 'S32K3xxDS_数据手册.md'}（Grep 关键词直接搜）")
    return 0 if hits else 1
