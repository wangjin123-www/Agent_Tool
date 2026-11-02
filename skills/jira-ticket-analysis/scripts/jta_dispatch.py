#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
jta_dispatch —— 派发工具与回执/水位管理

诚实说明本模块的能力边界：
  Python 进程**无法直接调用 Claude Code 的 Agent 工具**（那是 REPL 内的能力）。
  所以真实运行时，派发动作由 Claude 会话按 prompts/orchestrator.md 执行：
      Claude 调 `jtat.py prepare` → 拿到每单的 prompt + bundle
      → Claude 用 Agent 工具逐个派发 subagent
      → subagent 写 analysis.md + receipt.json
      → Claude 调 `jtat.py finish` 汇总 + 发邮件

本模块提供：
  * prepare()：把每单的派发材料（prompt 文件、bundle、路径）落盘，供 Claude 读取
  * record_receipt()：把 subagent 的回执写入 receipt.json
  * 水位 state.json 的读写与跳过判断
  * mark_failed()：单票失败态

这样"派发"这一步的可替换性最好：手动跑（Claude 会话）、二期 headless
（claude -p 调同样的 prepare 产物）都走同一套材料。
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

import jta_env as env


# ---------------------------------------------------------------- 水位


def state_path() -> Path:
    return env.workspace_root() / "out" / "state.json"


def load_state() -> Dict[str, Any]:
    return env.read_json(state_path(), {"tickets": {}, "runs": []})


def save_state(state: Dict[str, Any]) -> None:
    env.write_json(state_path(), state)


def should_skip(ticket: Dict[str, Any], state: Dict[str, Any], analysis_md: Path) -> bool:
    """
    增量水位：updated 未变 且 报告已存在 → 跳过。
    失败的单水位不推进，因此下次会自动重试。
    """
    if not env.cfg_get("jira", "skip_if_unchanged", default=True):
        return False
    if not analysis_md.exists():
        return False
    rec = (state.get("tickets") or {}).get(ticket["key"]) or {}
    if rec.get("status") != "ok":
        return False
    return rec.get("updated") == ticket.get("updated")


def mark_ok(ticket: Dict[str, Any], commit: Optional[str], size: str = "") -> None:
    state = load_state()
    state.setdefault("tickets", {})[ticket["key"]] = {
        "updated": ticket.get("updated"),
        "commit": commit,
        "size": size,
        "status": "ok",
        "at": datetime.now().isoformat(timespec="seconds"),
    }
    state.setdefault("runs", []).append({
        "at": datetime.now().isoformat(timespec="seconds"),
        "key": ticket["key"], "result": "ok",
    })
    save_state(state)


def mark_failed(ticket_key: str, error: str) -> None:
    state = load_state()
    rec = state.setdefault("tickets", {}).setdefault(ticket_key, {})
    rec.update({"status": "failed", "error": error[:500],
                "at": datetime.now().isoformat(timespec="seconds")})
    state.setdefault("runs", []).append({
        "at": datetime.now().isoformat(timespec="seconds"),
        "key": ticket_key, "result": "failed", "error": error[:200],
    })
    save_state(state)


# ---------------------------------------------------------------- 回执


RECEIPT_TEMPLATE: Dict[str, Any] = {
    "key": "",
    "title": "",
    "project": "",
    "confidence": "",
    "size": "",
    "conclusion": "",
    "pending": 0,
    "attention": "无",
    "status": "ok",
    "error": None,
}


def write_receipt(ticket_dir: Path, **fields: Any) -> Path:
    rec = dict(RECEIPT_TEMPLATE)
    rec.update(fields)
    p = ticket_dir / "receipt.json"
    env.write_json(p, rec)
    return p


def parse_receipt_text(text: str) -> Dict[str, Any]:
    """
    从 subagent 的回执文本里解析字段。
    回执是 KEY: ... / 工程归属: ... / 复杂度: ... 这种键值行。
    """
    out: Dict[str, Any] = {}
    mapping = {
        "工程归属": "project",
        "复杂度": "size",
        "一句话结论": "conclusion",
        "待确认数": "pending",
        "报告": "report",
        "需人工注意": "attention",
        "KEY": "key",
    }
    for line in (text or "").splitlines():
        if ":" not in line and "：" not in line:
            continue
        # 中文冒号也认
        line = line.replace("：", ":", 1)
        k, _, v = line.partition(":")
        k = k.strip().lstrip("-* ").strip()
        v = v.strip()
        if k in mapping:
            key = mapping[k]
            if key == "project":
                # "S32K312 车载仪表主控平台 / 置信度 high"
                if "/" in v and "置信度" in v:
                    proj, _, conf = v.partition("置信度")
                    out["project"] = proj.strip().rstrip("/").strip()
                    out["confidence"] = conf.strip().strip("/").strip()
                else:
                    out["project"] = v
            elif key == "pending":
                try:
                    out["pending"] = int("".join(ch for ch in v if ch.isdigit()) or 0)
                except ValueError:
                    out["pending"] = 0
            else:
                out[key] = v
    return out


# ---------------------------------------------------------------- 派发材料


def write_summary(date_dir: Path, skipped_by_limit: int = 0) -> Path:
    """
    从各单 receipt.json 生成当日 SUMMARY.md。
    由脚本生成而不是靠编排者手写：保证失败/跳过/超限的单**不会被静默省略**。
    """
    rows: List[Dict[str, Any]] = []
    failed: List[Dict[str, str]] = []
    pending_missing: List[str] = []

    for d in sorted(p for p in date_dir.iterdir() if p.is_dir()):
        if not (d / "ticket.json").exists() and not (d / "receipt.json").exists():
            continue
        rp = d / "receipt.json"
        if not rp.exists():
            # 尚未分析（或 subagent 没写回执）
            pending_missing.append(d.name)
            continue
        try:
            r = env.read_json(rp, {})
        except Exception as e:  # noqa: BLE001
            failed.append({"key": d.name, "error": f"回执解析失败: {e}"})
            continue
        if r.get("status") == "failed":
            failed.append({"key": r.get("key", d.name), "error": r.get("error", "未知")})
            continue
        rows.append(r)

    L: List[str] = [f"# 工单分析汇总 {date_dir.name}", ""]
    total = len(rows) + len(failed) + len(pending_missing)
    L.append(f"共 {total} 单：成功 {len(rows)} / 失败 {len(failed)}"
             + (f" / 待分析 {len(pending_missing)}" if pending_missing else "")
             + (f"（另有 {skipped_by_limit} 单因数量上限未分析）" if skipped_by_limit else ""))
    L.append("")

    if rows:
        L.append("| KEY | 标题 | 工程归属(置信度) | 工作量 | 一句话结论 | 待确认 | 报告 |")
        L.append("|---|---|---|---|---|---|---|")
        for r in rows:
            L.append(
                f"| {r.get('key','')} | {r.get('title','')} "
                f"| {r.get('project','')} ({r.get('confidence','')}) "
                f"| {r.get('size','')} | {r.get('conclusion','')} "
                f"| {r.get('pending',0)} | [analysis.md]({r.get('key','')}/analysis.md) |"
            )
        L.append("")

    notes = [f"{r.get('key')}: {r['attention']}" for r in rows
             if r.get("attention") and r["attention"] != "无"]
    L.append("## 需要你留意")
    L.append("")
    if notes:
        for n in notes:
            L.append(f"- {n}")
    else:
        L.append("- （无）")
    L.append("")
    if failed:
        L.append("### 分析失败（下次运行会自动重试）")
        L.append("")
        for f in failed:
            L.append(f"- **{f['key']}** — {f['error']}")
        L.append("")
    if pending_missing:
        L.append(f"### 待分析（未产出回执）：{', '.join(pending_missing)}")
        L.append("")
    if skipped_by_limit:
        L.append(f"### 因数量上限未分析：另有 {skipped_by_limit} 单")
        L.append("")

    out = date_dir / "SUMMARY.md"
    env.write_text(out, "\n".join(L))
    return out


def prepare_dispatch_materials(date_dir: Path) -> Dict[str, Any]:
    """
    收集每单的派发材料，写 <date_dir>/_dispatch.json 与逐单 dispatch.md，
    供 Claude 读取后用 Agent 工具派发。
    """
    items: List[Dict[str, Any]] = []
    for d in sorted(p for p in date_dir.iterdir() if p.is_dir()):
        bundle = d / "bundle.md"
        prompt = d / "worker_prompt.md"
        if not bundle.exists():
            continue
        items.append({
            "key": d.name,
            "dir": str(d),
            "bundle": str(bundle),
            "prompt": str(prompt) if prompt.exists() else None,
            "analysis": str(d / "analysis.md"),
            "receipt": str(d / "receipt.json"),
            "has_prompt": prompt.exists(),
        })

    out = {"date_dir": str(date_dir), "items": items}
    env.write_json(date_dir / "_dispatch.json", out)
    return out


if __name__ == "__main__":
    import argparse
    import json as _json

    ap = argparse.ArgumentParser(description="派发材料与水位")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("prepare", help="收集派发材料")
    p1.add_argument("date_dir")

    p2 = sub.add_parser("receipt", help="写入一条回执")
    p2.add_argument("ticket_dir")
    p2.add_argument("--json", help="回执 JSON 字符串")

    p3 = sub.add_parser("state", help="查看水位")

    a = ap.parse_args()
    if a.cmd == "prepare":
        print(_json.dumps(prepare_dispatch_materials(Path(a.date_dir)),
                          ensure_ascii=False, indent=2))
    elif a.cmd == "receipt":
        fields = _json.loads(a.json) if a.json else {}
        print(write_receipt(Path(a.ticket_dir), **fields))
    elif a.cmd == "state":
        print(_json.dumps(load_state(), ensure_ascii=False, indent=2))
