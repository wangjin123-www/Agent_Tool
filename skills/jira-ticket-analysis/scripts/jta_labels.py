#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
jta_labels —— 标签表（template/labels.md）的加载与校验。

标签表是**唯一词表**：分析结果里出现的标签必须能在表里找到，否则丢弃并记一笔，
避免 JIRA 自由标签发散。表本身是人维护的 Markdown 表格，本模块只读不写。

DLP 注意：公司文件对 bash/grep 是密文、对 Python 是明文。这里做一次嗅探 ——
万一读到密文，宁可报错也不要静默返回空词表（那会把所有单都打成"待归类"）。
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Dict, List

import jta_env as env

TABLE_PATH = env.TOOL_DIR / "template" / "labels.md"

LABEL_DONE = "已分析"
LABEL_FALLBACK = "待归类"
MAX_LABELS = 3

# 密文特征：DLP 透明加密的文件头，以及坏解码产生的替换字符
_CIPHER_MARKS = ("%TSD-Header", "�")


def _parse_table(text: str) -> List[Dict[str, Any]]:
    """Markdown 表格行 → [{label, category, purpose, keywords}]。

    只认 `## 模块类 / ## 现象类 / ## 系统类` 三个小节下的表；
    表头行与 `|---|` 分隔行跳过。第 1 列是标签本身。
    """
    rows: List[Dict[str, Any]] = []
    category = ""
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("## "):
            category = s[3:].strip()
            continue
        if not s.startswith("|") or not category:
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 2 or set(cells[0]) <= set("-: "):
            continue
        label = cells[0].strip("`").strip()
        if not label or label in ("标签",):
            continue
        rows.append({
            "label": label,
            "category": category,
            "purpose": cells[1] if len(cells) > 1 else "",
            "keywords": cells[2] if len(cells) > 2 else "",
        })
    return rows


def load_table(*, strict: bool = True) -> List[Dict[str, Any]]:
    """读标签表。strict=True 时读不到/读到密文/解析为空 → 抛异常。"""
    p = TABLE_PATH
    if not p.exists():
        if strict:
            raise FileNotFoundError(
                f"标签表不存在：{p}\n"
                f"  分析结果无法打标签，请先创建 template/labels.md")
        return []
    raw = p.read_bytes()
    # 密文嗅探：先按 utf-8 解，解不通或含密文头/替换字符都视为不可用
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("utf-8", errors="replace")
    if any(m in text for m in _CIPHER_MARKS):
        if strict:
            raise ValueError(
                f"标签表读到的是密文（DLP 透明加密）：{p}\n"
                f"  请确认该文件未被加密策略拦截，否则回写会全部退化为「{LABEL_FALLBACK}」。")
        return []

    rows = _parse_table(text)
    if strict and not rows:
        raise ValueError(f"标签表解析为空（表格格式可能被改动）：{p}")
    return rows


def known_labels() -> List[str]:
    """表内全部标签词。"""
    return [r["label"] for r in load_table()]


def render_for_prompt(max_chars: int = 1600) -> str:
    """压缩成一行行「标签(触发词)」，供塞进 worker 提示词。"""
    rows = load_table()
    by_cat: Dict[str, List[str]] = {}
    for r in rows:
        kw = f"({r['keywords']})" if r["keywords"] else ""
        by_cat.setdefault(r["category"], []).append(f"{r['label']}{kw}")
    out = "\n".join(f"- {c}: {' '.join(v)}" for c, v in by_cat.items())
    if len(out) > max_chars:
        out = out[:max_chars].rsplit(" ", 1)[0] + " …（表太长已截断，见 template/labels.md）"
    return out


def filter_labels(candidates: List[str], *, keep: int = MAX_LABELS) -> Dict[str, Any]:
    """
    把 AI 给的候选标签收敛到表内词。

    返回 {"labels": 最终标签（含"已分析"，≤keep 个）, "dropped": 表外被丢弃的词}。
    表外词一律丢弃 —— 不在 JIRA 里留自由标签；一个都没匹配上补「待归类」。
    """
    allowed = set(known_labels())
    picked: List[str] = []
    dropped: List[str] = []
    for t in candidates:
        t = t.strip()
        if not t or t == LABEL_DONE or t in picked:
            continue
        if t in allowed:
            picked.append(t)
        else:
            dropped.append(t)
    picked = picked[:max(0, keep - 1)]  # 给"已分析"留位
    if not picked:
        picked = [LABEL_FALLBACK]
    return {"labels": [LABEL_DONE, *picked], "dropped": dropped}
