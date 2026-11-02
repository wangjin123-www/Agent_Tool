#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
jta_bundle —— 组装每单 subagent 的输入包

产出（在 <ticket_dir>/ 下）：
  bundle.md      给 subagent 的总入口（含工程归属、代码位置、DBC 选择、证据索引指向）
  receipt.json   占位（由 subagent 填写或由 dispatch 写失败态）

关键：bundle.md 里**只放摘要与指针，不放日志正文**。
     日志细节留在 evidence/ 里，由 subagent 按 INDEX.md 的阅读顺序自己取。
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional

import jta_env as env
import jta_attach
import jta_labels


def projects_block(projects: List[Dict[str, Any]]) -> str:
    """把全部候选工程渲染成给 AI 看的描述块。"""
    L: List[str] = []
    for i, p in enumerate(projects, 1):
        L.append(f"{i}. **{p.get('name','')}**")
        L.append(f"   - 描述：{p.get('desc','')}")
        gl = p.get("gitlab") or {}
        L.append(f"   - 仓库：`{gl.get('project','')}` @ `{gl.get('branch','')}`")
        if p.get("analysis_scope"):
            L.append(f"   - 分析范围：`{p['analysis_scope']}`")
        if p.get("dbc_hint"):
            L.append(f"   - DBC 线索：{p['dbc_hint']}")
    return "\n".join(L) if L else "（config.projects 为空，请先填写）"


def build_bundle_md(
    ticket_dir: Path,
    *,
    ticket_key: str,
    issue: Dict[str, Any],
    projects: List[Dict[str, Any]],
    assigned: Dict[str, Any],
    repo: Optional[Dict[str, Any]],
    claude_md: Optional[str],
    dbc_index: Optional[str],
    dbc_choice: str,
    evidence: Dict[str, Any],
    hint_times: List[str],
    status: str,
) -> Path:
    L: List[str] = []
    L.append(f"# 分析输入包 {ticket_key}")
    L.append("")
    L.append(f"> {issue.get('summary','')}")
    L.append(f"> 状态: {(issue.get('status') or {}).get('name','-')} | "
             f"优先级: {(issue.get('priority') or {}).get('name','-')}")
    comps = ", ".join(c.get("name", "") for c in (issue.get("components") or [])) or "-"
    L.append(f"> 项目: {(issue.get('project') or {}).get('name','-')} | 组件: {comps}")
    L.append("")

    L.append("## 你要读的文件（按顺序）")
    L.append("")
    L.append(f"1. `{ticket_dir.name}/ticket.md` — 工单正文 + 评论（图片引用已替换为本地路径）")
    L.append(f"2. `{ticket_dir.name}/evidence/INDEX.md` — 证据索引（**必读**，告诉你该怎么读大文件）")
    if claude_md:
        L.append(f"3. `{claude_md}` — 代码库 CLAUDE.md 入口")
    L.append("")
    L.append("**不要整读** `*_frames.jsonl`（可达 10MB+）。需要细节用 Grep 定向搜。")
    L.append("")

    L.append("## 工程归属判断")
    L.append("")
    L.append(f"- 判定：**{assigned.get('project','（未判定）')}**")
    L.append(f"- 置信度：{assigned.get('confidence','-')}")
    L.append(f"- 理由：{assigned.get('reason','-')}")
    L.append("")
    L.append("全部候选工程（若你认为判错了，在第 9 节提改判建议并给依据，**不要自己换仓库重跑**）：")
    L.append("")
    L.append(projects_block(projects))
    L.append("")

    if repo and repo.get("ok"):
        L.append("## 代码工作区")
        L.append("")
        L.append(f"- 仓库：`{repo.get('project')}`")
        L.append(f"- 分支：`{repo.get('branch')}`")
        L.append(f"- commit：`{repo.get('sha8')}`（完整 `{repo.get('sha')}`）")
        L.append(f"- 取码方式：{repo.get('method')}")
        L.append(f"- 源码目录：`{repo.get('src')}`")
        if repo.get("scope"):
            L.append(f"- 分析范围：只在这个子目录内找代码 → `{repo['scope']}`")
        L.append("")
        L.append("> 这是工具自己的工作区快照，**没有 .git**，不是 git 工作树。"
                 "不要尝试 git 操作，也不要修改任何代码。")
        L.append("")
    else:
        L.append("## 代码工作区")
        L.append("")
        L.append("**无代码可读**（取码失败或该工单未匹配到工程）。"
                 "请仅基于工单文本与附件证据分析，并在报告中明确标注「未经代码验证」。")
        if repo and repo.get("error"):
            L.append("")
            L.append(f"失败原因：{repo['error'][:300]}")
        L.append("")

    if claude_md:
        L.append("## CLAUDE.md")
        L.append("")
        L.append(f"入口：`{claude_md}`")
        L.append("")
        L.append("**先读根 CLAUDE.md 的架构地图定位模块，再读相关模块的 CLAUDE.md（尤其 Gotchas）**，"
                 "然后才去 Grep/Read 源码。CLAUDE.md 里的已知结论要复用，不要重新发现。")
        L.append("")

    L.append("## DBC")
    L.append("")
    if dbc_index:
        L.append(f"- 索引：`{dbc_index}`")
    L.append(f"- 选择结果：{dbc_choice or '（本单无 BLF 附件，无需 DBC）'}")
    L.append("")

    L.append("## 证据摘要")
    L.append("")
    L.append(f"- 图片：{len(evidence.get('images', []))} 张" +
             ("（**每张都要 Read 看，抄下可读文字/数值**）" if evidence.get("images") else ""))
    L.append(f"- 日志：{len(evidence.get('logs', []))} 个"
             f"（其中 5AA5 帧日志 {sum(1 for g in evidence.get('logs',[]) if g.get('kind')=='log5aa5')} 个）")
    L.append(f"- BLF：{len(evidence.get('blf', []))} 个")
    L.append(f"- 压缩包：{len(evidence.get('archives', []))} 个（已解包并重新分类）")
    if evidence.get("video"):
        L.append(f"- 视频：{len(evidence['video'])} 个 —— **未分析**，不要推测其内容，"
                 "只在报告里记一行")
    if evidence.get("unknown"):
        L.append(f"- 未识别：{len(evidence['unknown'])} 个（未解析）")
    L.append("")
    if hint_times:
        L.append(f"**工单时间线索**：{', '.join(hint_times)} —— digest 已按这些时间做了窗口提取，优先看。")
        L.append("")
    for n in evidence.get("notes", []):
        L.append(f"- ⚠ {n}")
    L.append("")

    L.append("## 当前状态")
    L.append("")
    L.append(f"`{status}`")
    L.append("")

    out = ticket_dir / "bundle.md"
    env.write_text(out, "\n".join(L))
    return out


def build_ticket_worker_prompt(
    ticket_dir: Path,
    *,
    ticket_key: str,
    title: str,
    jira_url: str,
    projects: List[Dict[str, Any]],
    assigned: Dict[str, Any],
    repo: Optional[Dict[str, Any]],
    claude_md: Optional[str],
    dbc_index: Optional[str],
    dbc_choice: str,
    analysis_scope: str,
    hint_times: List[str],
) -> str:
    """读 prompts/ticket_worker.md 并替换占位符，返回可直接派发的 prompt。"""
    tpl_path = env.TOOL_DIR / "prompts" / "ticket_worker.md"
    tpl = env.read_text(tpl_path)

    # 标签表读不到（缺失/被 DLP 拦成密文）时降级为"只打已分析"——
    # 词表都读不到就无从"补词"，此时宁可少打标签，也不要让 worker 凭空造词。
    try:
        label_table = jta_labels.render_for_prompt()
        label_table_path = str(jta_labels.TABLE_PATH)
    except Exception as e:  # noqa: BLE001
        label_table = (f"（标签表不可用：{str(e)[:120]}）\n"
                       f"本单只输出：{jta_labels.LABEL_DONE}")
        label_table_path = "（标签表不可用，本单不要补词，只打 已分析）"

    repo_src = (repo or {}).get("src") or "(无代码)"
    repl = {
        "{{TICKET_DIR}}": str(ticket_dir),
        "{{TICKET_KEY}}": ticket_key,
        "{{TITLE}}": title,
        "{{JIRA_URL}}": jira_url,
        "{{PROJECTS}}": projects_block(projects),
        "{{ASSIGNED_PROJECT}}": assigned.get("project", "（未判定）"),
        "{{ASSIGNED_CONFIDENCE}}": assigned.get("confidence", "-"),
        "{{ASSIGNED_REASON}}": assigned.get("reason", "-"),
        "{{REPO_SRC}}": repo_src,
        "{{REPO_PROJECT}}": (repo or {}).get("project", "-"),
        "{{REPO_BRANCH}}": (repo or {}).get("branch", "-"),
        "{{REPO_SHA}}": (repo or {}).get("sha8", "-"),
        "{{CLAUDE_MD}}": claude_md or "(无)",
        "{{ANALYSIS_SCOPE}}": analysis_scope or "(整个仓库)",
        "{{DBC_INDEX}}": dbc_index or "(无)",
        "{{DBC_CHOICE}}": dbc_choice or "（本单无 BLF，无需 DBC）",
        "{{TIME_HINTS}}": ", ".join(hint_times) if hint_times else "（无）",
        "{{LABEL_TABLE}}": label_table,
        "{{LABEL_TABLE_PATH}}": label_table_path,
    }
    for k, v in repl.items():
        tpl = tpl.replace(k, str(v))
    return tpl
