#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
jta_dbc —— DBC 索引与选择辅助

用户只需要把各版本 DBC 丢进 config.dbc_dir，本模块负责：
  1. 轻量索引：抽出每份 DBC 的 VERSION、CM_ 注释、报文 ID/名称列表、版本日期，
     产出 dbc_index.md（**不整读大文件**，只用 cantools + 文本扫描）。
  2. 从工单文本里抽"问题版本名"与时间线索。
  3. 提供 CAN ID 命中率计算，供 AI 做最终裁决。

选择逻辑由 **AI 判断**，本模块只给材料（用户明确要求 AI 自行判断，不写死规则）：
  依据 A 工单里的问题版本名/日期
  依据 B DBC 文件名里的版本号与日期
  依据 C 工单描述/组件/车型
  依据 D 日志里实际出现的 CAN ID 命中率
  规则：A/B/C 先选候选，**时间新者优先**；无法区分时用 D 决胜；
        时间新与命中率冲突 → 以命中率为准，但在报告里写出冲突。
"""

from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

import jta_env as env

# 文件名里的日期：20260722 / 2026-07-22 / 2026_07_22
DATE_PATTERNS = [
    re.compile(r"(20\d{2})(\d{2})(\d{2})"),
    re.compile(r"(20\d{2})[-_/](\d{2})[-_/](\d{2})"),
]
# 版本号：V2.4 / v2.4 / V1.0.1
VERSION_RE = re.compile(r"[Vv](\d+(?:\.\d+)*)")
# DBC 内部 VERSION "..." 行
DBC_VERSION_LINE_RE = re.compile(r'^\s*VERSION\s+"([^"]*)"', re.MULTILINE)


def extract_date(text: str) -> Optional[str]:
    """从字符串里抽第一个日期，返回 YYYY-MM-DD。"""
    ds = extract_dates(text)
    return ds[0] if ds else None


def extract_dates(text: str) -> List[str]:
    """
    抽出字符串里**所有**日期（升序去重）。

    为什么需要"所有"：一个文件常同时打包多个车型的矩阵，
    例如 `WB101_IHU_CAN矩阵_V2.4_20260722-&&-WB102_IHU_CAN矩阵_V2.2_20260805.dbc`
    同时含 WB101 的 2026-07-22 与 WB102 的 2026-08-05。
    取第一个会把 WB102 的更新日期丢掉 —— 而工单组件可能正是 WB102。
    """
    found: List[str] = []
    for pat in DATE_PATTERNS:
        for m in pat.finditer(text):
            y, mo, d = m.group(1), m.group(2), m.group(3)
            try:
                found.append(f"{int(y):04d}-{int(mo):02d}-{int(d):02d}")
            except ValueError:
                continue
    # 去重 + 升序
    return sorted(set(found))


def extract_versions(text: str) -> List[str]:
    return VERSION_RE.findall(text or "")


def index_one_dbc(path: Path) -> Dict[str, Any]:
    """
    索引单份 DBC。优先用 cantools 读（准确），失败则退化纯文本扫描。
    只抽元数据与 ID 集合，不把全库载入内存做重活。
    """
    name_dates = extract_dates(path.name)
    info: Dict[str, Any] = {
        "file": path.name,
        "path": str(path),
        "bytes": path.stat().st_size,
        "name_date": name_dates[0] if name_dates else None,
        "name_dates": name_dates,          # 全部日期（多车型打包时会有多个）
        "name_date_latest": name_dates[-1] if name_dates else None,
        "name_versions": extract_versions(path.name),
        "internal_version": None,
        "internal_date": None,
        "message_count": 0,
        "message_ids": [],
        "message_names": [],
        "read_method": None,
        "error": None,
    }

    # 内部 VERSION 行 + CM_ 注释里的日期（纯文本，快）
    try:
        head = path.read_text(encoding="utf-8", errors="replace")[:200_000]
    except OSError:
        try:
            head = path.read_text(encoding="gbk", errors="replace")[:200_000]
        except OSError as e:
            info["error"] = str(e)
            return info

    m = DBC_VERSION_LINE_RE.search(head)
    if m:
        info["internal_version"] = m.group(1).strip()
        info["internal_date"] = extract_date(m.group(1))

    # cantools 精确读取
    try:
        import cantools  # type: ignore
        db = cantools.database.load_file(str(path))
        info["message_count"] = len(db.messages)
        info["message_ids"] = sorted({m_.frame_id for m_ in db.messages})
        info["message_names"] = [m_.name for m_ in db.messages][:500]
        if not info["internal_version"] and getattr(db, "version", None):
            info["internal_version"] = str(db.version)
            info["internal_date"] = info["internal_date"] or extract_date(str(db.version))
        info["read_method"] = "cantools"
    except Exception as e:  # noqa: BLE001
        info["read_method"] = "text"
        info["error"] = f"cantools 读取失败，退化文本扫描：{e}"
        # 文本兜底：抓 BO_ <id> <name>: 行
        ids = []
        names = []
        for mm in re.finditer(r"^\s*BO_\s+(\d+)\s+(\S+)\s*:", head, re.MULTILINE):
            ids.append(int(mm.group(1)))
            names.append(mm.group(2))
        info["message_ids"] = sorted(set(ids))
        info["message_names"] = names[:500]
        info["message_count"] = len(info["message_ids"])

    # 车型 → (版本, 日期) 配对，供"依据 C 按组件/车型匹配"直接用。
    # 例：WB101_IHU_CAN矩阵_V2.4_20260722-&&-WB102_IHU_CAN矩阵_V2.2_20260805.dbc
    #   → {"WB101": {"version": "2.4", "date": "2026-07-22"},
    #      "WB102": {"version": "2.2", "date": "2026-08-05"}}
    info["model_versions"] = extract_model_versions(path.name)

    # 有效日期：文件名优先（发布习惯），否则内部。
    # 多车型打包时取**最新**的那个日期 —— 工单组件可能是较新的那个车型。
    info["effective_date"] = (info["name_date_latest"] or info["internal_date"])
    # 版本也要把全部列出来（多车型时不止一个）
    info["effective_version"] = (", ".join(info["name_versions"]) if info["name_versions"]
                                 else info["internal_version"])
    return info


# 车型代号：字母+数字（WB101 / WB102 / YB103 …）
MODEL_RE = re.compile(r"([A-Za-z]{1,3}\d{3})")
# 一段 "WB101_IHU_CAN矩阵_V2.4_20260722"
MODEL_SEGMENT_RE = re.compile(
    r"([A-Za-z]{1,3}\d{3})\S*?[Vv](\d+(?:\.\d+)*)[_\-]?(20\d{6})", re.IGNORECASE
)


def extract_model_versions(filename: str) -> Dict[str, Dict[str, str]]:
    """从文件名里抽 车型 → {version, date} 映射。抽不到返回 {}。"""
    out: Dict[str, Dict[str, str]] = {}
    for m in MODEL_SEGMENT_RE.finditer(filename):
        model, ver, ymd = m.group(1).upper(), m.group(2), m.group(3)
        try:
            date = f"{ymd[:4]}-{ymd[4:6]}-{ymd[6:]}"
        except Exception:  # noqa: BLE001
            date = None
        out[model] = {"version": ver, "date": date}
    return out


def index_all(dbc_dir: Optional[Path] = None) -> List[Dict[str, Any]]:
    d = Path(dbc_dir) if dbc_dir else env.tool_path(env.cfg_get("dbc_dir", default=""))
    if not d.exists():
        return []
    out = []
    for p in sorted(d.rglob("*.dbc")):
        env.log(f"  索引 DBC {p.name} …")
        out.append(index_one_dbc(p))
    return out


def write_index(entries: List[Dict[str, Any]], out_md: Path, hint: Optional[str] = None) -> Path:
    L: List[str] = ["# DBC 索引（供 AI 选择用）", ""]
    L.append(f"> 由 `jta_dbc.py` 自动生成于 {datetime.now():%Y-%m-%d %H:%M}")
    if hint:
        L.append(f"> 工程线索: {hint}")
    L.append("")
    if not entries:
        L.append("**目录里没有 DBC 文件。** 请把各版本 DBC 放进 `config.dbc_dir`。")
        env.write_text(out_md, "\n".join(L))
        return out_md

    L.append("## 总览")
    L.append("")
    L.append("| 文件 | 文件名日期(全部) | 有效日期(最新) | 版本 | 报文数 | 读取方式 |")
    L.append("|---|---|---|---|---|---|")
    for e in entries:
        L.append(
            f"| `{e['file']}` | {', '.join(e.get('name_dates') or []) or '-'} "
            f"| **{e.get('name_date_latest') or e['internal_date'] or '-'}** "
            f"| {e.get('effective_version') or '-'} | {e['message_count']} | {e['read_method']} |"
        )
    L.append("")

    # 车型 → 版本/日期 配对表（依据 C 直接查这张表）
    pairs = [(e["file"], m, v) for e in entries
             for m, v in (e.get("model_versions") or {}).items()]
    if pairs:
        L.append("## 车型 → 版本 / 日期（依据 C 直接查这里）")
        L.append("")
        L.append("| 文件 | 车型 | 版本 | 日期 |")
        L.append("|---|---|---|---|")
        for f, m, v in pairs:
            L.append(f"| `{f}` | **{m}** | {v.get('version','-')} | {v.get('date','-')} |")
        L.append("")
        L.append("> 工单组件（如 `WB102（柴油）`）对应哪个车型，就在上表找那一行，")
        L.append("> 再用它的日期做「时间新者优先」比较。")
        L.append("")

    L.append("## 选择依据（AI 用）")
    L.append("")
    L.append("- **依据 A**：工单里写的「问题版本名/日期」→ 与下表「有效日期/版本」对比")
    L.append("- **依据 B**：DBC 文件名里的版本号与日期")
    L.append("- **依据 C**：工单描述/组件/车型（如 `WB102（柴油）`）→ 看哪些文件的名称/内部注释含该车型")
    L.append("- **依据 D**：日志里实际出现的 CAN ID 与各文件 `message_ids` 求命中率")
    L.append("")
    L.append("**规则**：A/B/C 选候选后**时间新者优先**；无法区分用 D 决胜；")
    L.append("时间新与命中率冲突时**以命中率为主**，并在报告里写明冲突。")
    L.append("")

    L.append("## 逐份明细")
    L.append("")
    for e in entries:
        L.append(f"### `{e['file']}`")
        L.append("")
        L.append(f"- 路径: `{e['path']}`")
        L.append(f"- 体积: {e['bytes']:,} B")
        L.append(f"- 文件名日期: {e['name_date'] or '（未识别）'}")
        L.append(f"- 文件名版本: {', '.join(e['name_versions']) or '（无）'}")
        L.append(f"- 内部 VERSION: {e['internal_version'] or '（无）'}")
        L.append(f"- 有效日期(选择用): **{e['effective_date'] or '（未识别）'}**")
        L.append(f"- 报文数: {e['message_count']}（读取方式 {e['read_method']}）")
        if e.get("error"):
            L.append(f"- ⚠ {e['error']}")
        ids = e.get("message_ids") or []
        if ids:
            shown = ", ".join(f"0x{i:X}" for i in ids[:60])
            more = f" … 共 {len(ids)}" if len(ids) > 60 else ""
            L.append(f"- 报文 ID: {shown}{more}")
            names = e.get("message_names") or []
            if names:
                L.append(f"- 报文名示例: {', '.join(names[:25])}")
        L.append("")

    env.write_text(out_md, "\n".join(L))
    return out_md


# ---------------------------------------------------------------- 命中率


def collect_can_ids_from_evidence(ticket_dir: Path) -> Set[int]:
    """
    从单票的证据里收集实际出现的 CAN 报文 ID。
    来源：canlog 产物 CSV 文件名（形如 0x121_VCU_31.csv）、UNKNOWN_IDS.md、
          以及工单文本里出现的 0xXXX / 3D5 这类十六进制串。
    """
    ids: Set[int] = set()

    # 1) canlog 输出目录里的 CSV 文件名
    for p in ticket_dir.rglob("0x*.csv"):
        m = re.match(r"0x([0-9A-Fa-f]+)", p.name)
        if m:
            ids.add(int(m.group(1), 16))

    # 2) 工单文本里的十六进制 ID（3D5 / 0x583 / 583）
    for f in ("ticket.md", "ticket.json"):
        fp = ticket_dir / f
        if not fp.exists():
            continue
        txt = env.read_text(fp)
        for m in re.finditer(r"\b0x([0-9A-Fa-f]{1,4})\b", txt):
            ids.add(int(m.group(1), 16))
        for m in re.finditer(r"\b([0-9A-F]{3})\b", txt):
            try:
                ids.add(int(m.group(1), 16))
            except ValueError:
                pass
    return ids


def hit_rate(can_ids: Set[int], dbc_ids: List[int]) -> float:
    if not can_ids or not dbc_ids:
        return 0.0
    s = set(dbc_ids)
    return len(can_ids & s) / len(can_ids)


def rank_by_hit_rate(can_ids: Set[int], entries: List[Dict[str, Any]]) -> List[Tuple[str, float]]:
    return sorted(
        ((e["file"], hit_rate(can_ids, e.get("message_ids") or [])) for e in entries),
        key=lambda x: -x[1],
    )


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description="DBC 索引")
    ap.add_argument("--dir", help="DBC 目录（默认 config.dbc_dir）")
    ap.add_argument("--out", help="输出 md 路径")
    a = ap.parse_args()
    entries = index_all(Path(a.dir) if a.dir else None)
    out = Path(a.out) if a.out else (env.workspace_root() / "dbc_index.md")
    write_index(entries, out)
    env.log(f"索引 {len(entries)} 份 DBC → {out}")
