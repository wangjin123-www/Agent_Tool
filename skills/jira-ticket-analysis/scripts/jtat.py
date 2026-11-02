#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
jtat —— 工单分析流水线统一 CLI

子命令：
  validate                      环境自检（venv 依赖 / Jira / GitLab / lark-cli / 目录可写）
  list                          只列符合条件的工单，不下载
  fetch      [--keys K1,K2]     拉工单 + 下载附件 → staging
  prepare    [--keys ...]       附件解析 + 取代码 + DBC 索引 + 组装 bundle/worker_prompt
  repo       --keys ...         只做取代码 + CLAUDE.md（调试用）
  dbc                           只做 DBC 索引（调试用）
  run        [--keys ...]       fetch + prepare（一键到"可派发"状态）
  feedback   [--keys ...] [--apply]  在工单下建子任务（附件挂全文+打标签），父单不动；记台账
  labels                        打印标签表 template/labels.md（自检可读性）
  status                        看水位
  mail-only  [--date ...]       只发邮件（用已有 receipt.json）

注意：subagent 的"派发"动作由 Claude 会话执行（见 prompts/orchestrator.md），
      本 CLI 负责的是派发前后的确定性工作。

退出码（沿用 jira-tool 约定）：
  0 成功 / 1 脚本错误 / 2 参数错误 / 3 鉴权失败 / 4 上游 API 错误 / 5 有单失败

入口：优先用工具根目录下的 jtat.cmd（自动解析工具目录与 .venv），
      或直接 <TOOL>/.venv/Scripts/python.exe <TOOL>/scripts/jtat.py …（用绝对路径即可，
      不依赖 cwd）。cwd 在工具目录内最省事（无 jira/ 同名目录遮蔽 import jira）。
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date as _date
from pathlib import Path
from typing import Any, Dict, List, Optional

import jta_env as env

# 本进程的 stdout 也必须能输出 UTF-8。
# 背景：jta_env.child_env() 只给**子进程**注入 PYTHONUTF8=1；本进程的输出编码取决于
# 控制台代码页（中文 Windows 上是 cp936），而 validate 会打印 ✓/✗ 等非 GBK 字符，
# 会直接 UnicodeEncodeError 崩掉。这里统一把本进程的 stdio 也设成 UTF-8。
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass

# 允许从任意 cwd 运行：把脚本目录加入 sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent))

import jta_attach  # noqa: E402
import jta_bundle  # noqa: E402
import jta_dbc  # noqa: E402
import jta_dispatch  # noqa: E402
import jta_feedback  # noqa: E402
import jta_fetch  # noqa: E402
import jta_labels  # noqa: E402
import jta_mail  # noqa: E402
import jta_repo  # noqa: E402

EXIT_OK, EXIT_ERR, EXIT_ARG, EXIT_AUTH, EXIT_API, EXIT_PARTIAL = 0, 1, 2, 3, 4, 5


# ---------------------------------------------------------------- validate


def cmd_validate(_a: argparse.Namespace) -> int:
    ok = True
    print("=" * 60)
    print("环境自检")
    print("=" * 60)

    # 1) cwd 安全性
    print(f"\n[1] 运行目录")
    print(f"    tool dir : {env.TOOL_DIR}")
    print(f"    cwd      : {Path.cwd()}")
    print(f"    safe cwd : {env.safe_cwd()}")
    if env.cwd_shadows_jira():
        print("    ⚠ 当前 cwd 下有 jira/ 同名目录，会让 `import jira` 解析成命名空间包。")
        print(f"      子进程已自动改用安全 cwd，但建议你 cd 到工具目录再跑：{env.TOOL_DIR}")

    # 2) 唯一 venv 与依赖
    print(f"\n[2] venv 与依赖（唯一解释器）")
    try:
        vpy = env.venv_python()
        print(f"    venv python: {vpy}")
    except FileNotFoundError as e:
        print(f"    ✗ {e}")
        return EXIT_ERR

    import importlib
    for m in ("jira", "gitlab", "cantools", "can", "PIL", "requests"):
        try:
            mod = importlib.import_module(m)
            v = getattr(mod, "__version__", "")
            print(f"    ✓ {m:10} {v}")
        except Exception as e:  # noqa: BLE001
            print(f"    ✗ {m:10} {e}")
            ok = False

    # 3) 配置
    print(f"\n[3] 配置")
    try:
        cfg = env.load_config()
        print(f"    config    : {env.CONFIG_PATH}")
        projs = cfg.get("projects") or []
        print(f"    projects  : {len(projs)} 个")
        for p in projs:
            print(f"      - {p.get('name')}  ({p.get('gitlab',{}).get('project')}"
                  f" @ {p.get('gitlab',{}).get('branch')})")
        if not projs:
            print("    ⚠ projects 为空 —— 请填写 config.json 的 projects 段")
    except Exception as e:  # noqa: BLE001
        print(f"    ✗ 读 config 失败：{e}")
        return EXIT_ERR

    # 4) Jira 探活
    print(f"\n[4] Jira 探活")
    try:
        res = env.run_python_json(
            [env.jira_ops_script("search.py"), "--jql",
             "assignee = currentUser() ORDER BY updated desc", "--limit", "1"],
            timeout=120,
        )
        print(f"    ✓ 连通，我的工单总数 {res.get('total')}，本次返回 {res.get('returned')}")
        if res.get("issues"):
            i = res["issues"][0]
            print(f"      最新一条：{i.get('key')} {str(i.get('summary'))[:40]}")
    except Exception as e:  # noqa: BLE001
        msg = str(e)
        print(f"    ✗ Jira 探活失败：{msg[:300]}")
        if "退出码 3" in msg or "401" in msg or "403" in msg:
            print("      → 鉴权问题：检查 JIRA_PAT 环境变量或 jira-tool 的 config.json")
            return EXIT_AUTH
        ok = False

    # 5) GitLab
    print(f"\n[5] GitLab")
    pat = jta_repo.gitlab_pat()
    print(f"    PAT: {'✓ 取到（不显示）' if pat else '✗ 取不到'}")
    if not pat:
        print("      → token_source 配的是 git-credential-manager，需先让 git 记住凭据；"
              "或改用 env 方式设 GITLAB_PAT")
        ok = False
    else:
        try:
            import requests
            host = cfg.get("gitlab", {}).get("host", "").rstrip("/")
            r = requests.get(f"{host}/api/v4/version",
                             headers={"PRIVATE-TOKEN": pat}, timeout=30,
                             verify=cfg.get("gitlab", {}).get("ssl_verify", True))
            if r.status_code == 200:
                print(f"    ✓ /api/v4/version → {r.status_code}，GitLab {r.json().get('version')}")
            else:
                print(f"    ✗ /api/v4/version → {r.status_code}")
                ok = False
            # 逐工程探活 + archive 权限
            for p in cfg.get("projects") or []:
                proj = (p.get("gitlab") or {}).get("project")
                if not proj:
                    continue
                from urllib.parse import quote
                rr = requests.get(f"{host}/api/v4/projects/{quote(proj, safe='')}",
                                  headers={"PRIVATE-TOKEN": pat}, timeout=30,
                                  verify=cfg.get("gitlab", {}).get("ssl_verify", True))
                print(f"      {'✓' if rr.status_code == 200 else '✗'} 项目 {proj} → {rr.status_code}")
                if rr.status_code != 200:
                    ok = False
        except Exception as e:  # noqa: BLE001
            print(f"    ✗ GitLab 探活异常：{e}")
            ok = False

    # 6) vendor 内嵌工具（应全部相对工具目录，不该出现绝对路径）
    print(f"\n[6] 内嵌工具 vendor/")
    for label, key, required in [
        ("jira-tool ops", "jira_ops", True),
        ("frame_extractor", "frame_extractor", True),
        ("AI_canlog", "canlog_dir", True),
        ("claude-md-map", "claude_md_map", True),
        ("lark-cli", "lark_cli", False),  # 可选：不随包分发
    ]:
        p = env.cfg_path("paths", key)
        exists = bool(p) and p.exists()
        shown = env.rel_to_tool(p) if p else "(未配置)"
        if exists:
            print(f"    ✓ {label:16} {shown}")
        elif required:
            print(f"    ✗ {label:16} {shown}")
            print(f"      → 重跑 python tools/sync_vendor.py 重建 vendor/")
            ok = False
        else:
            print(f"    ○ {label:16} {shown}（可选，不发邮件可不放）")

    # 7) 目录可写
    print(f"\n[7] 目录可写")
    for label, d in [("workspace", env.workspace_root()), ("out", env.out_root())]:
        try:
            t = d / ".write_test"
            t.write_text("ok", encoding="utf-8")
            t.unlink()
            print(f"    ✓ {label:10} {d}")
        except Exception as e:  # noqa: BLE001
            print(f"    ✗ {label:10} {d} — {e}")
            ok = False
    dbc_dir = env.tool_path(env.cfg_get("dbc_dir", default="")) or (env.TOOL_DIR / "dbc")
    n_dbc = len(list(dbc_dir.rglob("*.dbc"))) if dbc_dir.exists() else 0
    print(f"    {'✓' if n_dbc else '⚠'} dbc 目录   {dbc_dir}（{n_dbc} 份 DBC）")
    if not n_dbc:
        print("      → 请把各版本 DBC 丢进这个目录，否则 BLF 无法解析")

    print("\n" + "=" * 60)
    print("结论：", "全部通过 ✓" if ok else "有问题 ✗（见上）")
    print("=" * 60)
    return EXIT_OK if ok else EXIT_ERR


# ---------------------------------------------------------------- list


def cmd_list(a: argparse.Namespace) -> int:
    cfg = env.load_config()
    jql = a.jql or cfg["jira"]["jql"]
    res = jta_fetch.search_tickets(jql=jql, limit=a.limit)
    print(f"JQL: {jql}")
    print(f"total={res.get('total')} returned={res.get('returned')} transferred={res.get('truncated')}")
    for i in res.get("issues", []):
        comps = ",".join(c.get("name", "") for c in (i.get("components") or []))
        print(f"  {i.get('key'):22} {(i.get('status') or {}).get('name',''):8} "
              f"{(i.get('priority') or {}).get('name',''):4} [{comps}] {str(i.get('summary'))[:40]}")
    return EXIT_OK


# ---------------------------------------------------------------- fetch / prepare / run


def _date_dir(a: argparse.Namespace) -> Path:
    """
    解析产物日期目录。
    `--date 2026-09-13` 只给日期名 → 落在 out_root 下；
    给绝对/相对路径 → 直接用（但一律 resolve，避免相对路径在别处被误解）。
    """
    if getattr(a, "date", None):
        pd = Path(a.date)
        d = pd if pd.is_absolute() or len(pd.parts) > 1 else (env.out_root() / pd)
    else:
        d = env.out_root() / _date.today().isoformat()
    d = d.resolve()
    d.mkdir(parents=True, exist_ok=True)
    return d


def _keys(a: argparse.Namespace) -> Optional[List[str]]:
    if getattr(a, "keys", None):
        return [s.strip() for s in a.keys.split(",") if s.strip()]
    return None


def cmd_fetch(a: argparse.Namespace) -> int:
    out = jta_fetch.fetch(_keys(a), jql=getattr(a, "jql", None),
                          limit=getattr(a, "limit", None),
                          date_dir=_date_dir(a))
    print(json.dumps({k: v for k, v in out.items() if k != "tickets"},
                     ensure_ascii=False, indent=2))
    for t in out["tickets"]:
        print(f"  ✓ {t['key']} {t['summary'][:40]} 附件{t['attachments_total']}"
              f"（失败{len(t['attachments_failed'])}）")
    return EXIT_PARTIAL if out["errors"] else EXIT_OK


def prepare_one(ticket_dir: Path, projects: List[Dict[str, Any]],
                dbc_index: Optional[str],
                assigned: Dict[str, Any]) -> Dict[str, Any]:
    """对单票做：读 ticket.json → 附件解析 → 取代码 → 组装 bundle + prompt。"""
    key = ticket_dir.name
    data = env.read_json(ticket_dir / "ticket.json", {})
    issue = data.get("issue", {})

    # 1) 附件解析
    ev = jta_attach.process_ticket(ticket_dir)

    # 2) 时间线索（给 digest 定位窗口）
    texts = [issue.get("description") or ""]
    for c in issue.get("comments") or []:
        texts.append(c.get("body") or "")
    hints = jta_attach.extract_time_hints(*texts)
    id_hints = jta_attach.extract_id_hints(*texts)
    if id_hints:
        env.log(f"  工单点名的 ID: {', '.join(id_hints)}")

    # 3) 对每个帧日志解析产物补 digest（按目录成组解析，产物名来自目录名）
    for p in ev.get("parsers", []):
        if p.get("tool") != "frame_extractor" or not p.get("ok"):
            continue
        for produced in p.get("produced", []):
            if not produced.endswith("_frames.jsonl"):
                continue
            jsonl = Path(produced)
            if jsonl.exists():
                jta_attach.build_frames_digest(
                    jsonl, jsonl.parent / f"{jsonl.stem}_digest.md",
                    hint_times=hints, focus_ids=id_hints)

    jta_attach.build_evidence_index(ticket_dir, ev, hint_times=hints)

    # 4) 取代码
    repo: Optional[Dict[str, Any]] = None
    claude_md: Optional[str] = None
    assigned_project = assigned.get("project") or ""
    proj_cfg = next((p for p in projects if p.get("name") == assigned_project), None)
    if proj_cfg:
        gl = proj_cfg.get("gitlab") or {}
        repo = jta_repo.ensure_code(gl.get("project", ""), gl.get("branch", ""),
                                    proj_cfg.get("analysis_scope"))
        repo["scope"] = proj_cfg.get("analysis_scope")
        if repo.get("ok"):
            md = jta_repo.prepare_claude_md(repo)
            claude_md = md.get("root_claude_md")
            jta_repo.snapshot_claude_md(repo)

    # 5) DBC 选择（AI 在派发时定；这里给默认候选 + 索引）
    dbc_choice = ""
    if ev.get("blf"):
        if ev.get("dbc"):
            dbc_choice = (f"优先用工单附件自带 DBC `{ev['dbc'][0]['file']}`（现场版本，最权威）；"
                          f"索引见 {dbc_index}（AI 判断，非人工指定）")
        else:
            dbc_choice = f"请按索引 {dbc_index} 选择（依据 A/B/C 时间新者优先，D 命中率决胜）"

    # 6) bundle + prompt
    jta_bundle.build_bundle_md(
        ticket_dir, ticket_key=key, issue=issue, projects=projects,
        assigned=assigned, repo=repo, claude_md=claude_md,
        dbc_index=dbc_index, dbc_choice=dbc_choice, evidence=ev,
        hint_times=hints, status="等待派发 subagent",
    )
    prompt = jta_bundle.build_ticket_worker_prompt(
        ticket_dir, ticket_key=key, title=issue.get("summary", ""),
        jira_url=issue.get("url", ""), projects=projects, assigned=assigned,
        repo=repo, claude_md=claude_md, dbc_index=dbc_index, dbc_choice=dbc_choice,
        analysis_scope=(proj_cfg or {}).get("analysis_scope", ""), hint_times=hints,
    )
    env.write_text(ticket_dir / "worker_prompt.md", prompt)

    return {"key": key, "evidence": ev, "repo": repo, "claude_md": claude_md,
            "hints": hints, "id_hints": id_hints, "assigned": assigned}


def cmd_prepare(a: argparse.Namespace) -> int:
    date_dir = _date_dir(a)
    cfg = env.load_config()
    projects = cfg.get("projects") or []

    # 需要哪些单：优先用已 fetch 的目录；--keys 指定则过滤
    keys = _keys(a)
    dirs = [d for d in sorted(date_dir.iterdir()) if d.is_dir() and (d / "ticket.json").exists()]
    if keys:
        dirs = [d for d in dirs if d.name in keys]
    if not dirs:
        print(f"没有可处理的工单目录（{date_dir}）。先跑 fetch。", file=sys.stderr)
        return EXIT_ARG

    # DBC 索引（所有单共用一份）
    dbc_index = None
    dbc_dir = env.tool_path(env.cfg_get("dbc_dir", default="")) or (env.TOOL_DIR / "dbc")
    if dbc_dir.exists() and list(dbc_dir.rglob("*.dbc")):
        out_md = env.workspace_root() / "dbc_index.md"
        entries = jta_dbc.index_all(dbc_dir)
        jta_dbc.write_index(entries, out_md)
        dbc_index = str(out_md)
        env.log(f"DBC 索引 {len(entries)} 份 → {out_md}")
    else:
        env.log("dbc 目录里没有 DBC（若工单带 BLF 将无法完整解析）")

    # 工程归属：优先用 Claude 复核过的 _assignments.json；
    # 没有就退回占位（并由 orchestrator 提示 Claude 复核）
    assignments_file = date_dir / "_assignments.json"
    reviewed = env.read_json(assignments_file, {}) if assignments_file.exists() else {}

    # 工程归属：由 Claude 按 orchestrator.md 第一步判断。
    # 已复核过的（confidence 不是空且非占位）保留，其余给占位。
    assignments: Dict[str, Dict[str, Any]] = {}
    for d in dirs:
        prev = reviewed.get(d.name) or {}
        if prev.get("project"):
            assignments[d.name] = prev  # 保留 Claude 的复核结果
        else:
            assignments[d.name] = {
                "project": projects[0]["name"] if len(projects) == 1 else "",
                "confidence": "low" if len(projects) == 1 else "",
                "reason": ("config 里只有一个工程，暂按它处理，待 Claude 复核"
                           if len(projects) == 1 else "待 Claude 判断（见 orchestrator.md 第一步）"),
            }
    env.write_json(assignments_file, assignments)
    unreviewed = [k for k, v in assignments.items()
                  if v.get("reason", "").startswith(("config 里只有", "待 Claude"))]
    if unreviewed:
        env.log(f"⚠ 以下单的工程归属尚未由 Claude 复核：{', '.join(unreviewed)}"
                f"（见 orchestrator.md 第一步）")
    else:
        env.log("工程归属已全部复核")

    results = []
    failures = []
    for d in dirs:
        try:
            env.log(f"—— 处理 {d.name} ——")
            r = prepare_one(d, projects, dbc_index, assignments.get(d.name, {}))
            results.append(r)
            env.log(f"  {d.name} 就绪")
        except Exception as e:  # noqa: BLE001
            env.log(f"  {d.name} 处理失败：{e}")
            failures.append({"key": d.name, "error": str(e)})
            jta_dispatch.mark_failed(d.name, str(e))
            jta_dispatch.write_receipt(d, key=d.name, status="failed", error=str(e))

    mats = jta_dispatch.prepare_dispatch_materials(date_dir)
    print(json.dumps({"date_dir": str(date_dir), "ready": len(results),
                      "failed": failures, "dispatch": mats["items"]},
                     ensure_ascii=False, indent=2)[:4000])
    return EXIT_PARTIAL if failures else EXIT_OK


def cmd_feedback(a: argparse.Namespace) -> int:
    """
    回写 analysis.md → 在该工单下建子任务（附件挂全文 + 标签），父单不动；记台账。
    """
    date_dir = _date_dir(a)
    keys = _keys(a)
    dirs = [d for d in sorted(date_dir.iterdir())
            if d.is_dir() and (d / "analysis.md").exists()]
    if keys:
        dirs = [d for d in dirs if d.name in keys]
    if not dirs:
        print(f"没有可回写的工单（{date_dir} 下缺 analysis.md，先派发 subagent 写报告）。",
              file=sys.stderr)
        return EXIT_ARG
    if not a.apply:
        env.log("dry-run 预览：只打印将写什么，不写 Jira；确认后加 --apply 实跑")

    # 标签表是唯一词表；读不到明文就直接停，别让所有单退化成"待归类"
    try:
        jta_labels.load_table()
    except Exception as e:  # noqa: BLE001
        print(f"✗ 标签表不可用，回写中止：{e}", file=sys.stderr)
        return EXIT_ARG

    ledger = jta_feedback.load_ledger()
    results: List[Dict[str, Any]] = []
    ok_keys: List[str] = []
    for d in dirs:
        env.log(f"—— 回写 {d.name} ——")
        try:
            r = jta_feedback.feedback_one(
                d, apply=a.apply, ledger=None if a.force else ledger,
                subtask_type=a.subtask_type, refresh_type=a.refresh_type,
                no_check_required=a.no_check_required)
            results.append(r)
            # partial 也入账：下次会因 status != ok 而重试（旧逻辑会把 partial 永久锁死）
            if a.apply and r.get("status") in ("ok", "partial"):
                ledger = [e for e in ledger if e.get("key") != d.name]
                ledger.append({k: r.get(k) for k in jta_feedback.LEDGER_FIELDS})
                ok_keys.append(d.name)
        except Exception as e:  # noqa: BLE001
            env.log(f"  {d.name} 回写失败：{e}")
            results.append({"key": d.name, "status": "failed", "error": str(e)[:300]})

    if a.apply and ok_keys:
        md = jta_feedback.write_ledger(ledger)
        env.log(f"台账 → {md}（本次新增 {len(ok_keys)} 单：{', '.join(ok_keys)}）")

    print(json.dumps({"date_dir": str(date_dir), "apply": a.apply,
                      "results": results}, ensure_ascii=False, indent=2)[:4000])
    return EXIT_OK if all(r.get("status") != "failed" for r in results) else EXIT_PARTIAL


def cmd_labels(_a: argparse.Namespace) -> int:
    """打印标签表 —— 既是给人看的词表，也是 DLP 明文可读性的自检。"""
    try:
        rows = jta_labels.load_table()
    except Exception as e:  # noqa: BLE001
        print(f"✗ 标签表不可用：{e}", file=sys.stderr)
        return EXIT_ARG
    print(f"标签表：{jta_labels.TABLE_PATH}")
    by_cat: Dict[str, List[str]] = {}
    for r in rows:
        by_cat.setdefault(r["category"], []).append(r["label"])
    for cat, labels in by_cat.items():
        print(f"\n[{cat}] {len(labels)} 个")
        print("  " + "  ".join(labels))
    print(f"\n合计 {len(rows)} 个标签。回写时每单最多取 "
          f"{jta_labels.MAX_LABELS} 个（含「{jta_labels.LABEL_DONE}」）。")
    return EXIT_OK


def cmd_run(a: argparse.Namespace) -> int:
    """
    一键：fetch → prepare → summary（到"可派发"状态为止）。
    不含 subagent 派发与发邮件 —— 那两步由 Claude 会话执行/确认。
    """
    rc = cmd_fetch(a)
    if rc not in (EXIT_OK, EXIT_PARTIAL):
        return rc
    rc2 = cmd_prepare(a)
    # 即便 prepare 有失败，也生成 SUMMARY，保证失败单不丢失
    try:
        date_dir = _date_dir(a)
        fs = env.read_json(date_dir / "_fetch_summary.json", {}) or {}
        out = jta_dispatch.write_summary(date_dir, fs.get("skipped_by_limit", 0))
        env.log(f"SUMMARY → {out}")
    except Exception as e:  # noqa: BLE001
        env.log(f"SUMMARY 生成失败：{e}")
    return max(rc, rc2) if rc != rc2 else rc


def cmd_all(a: argparse.Namespace) -> int:
    """
    全流程：fetch → prepare → summary → 派发（需 Claude）→ mail。
    本命令只做到 summary + 可选发信；派发必须由 Claude 用 Agent 工具完成，
    所以这里会在需要派发时**明确提示**，不假装能自动派发。
    """
    rc = cmd_run(a)
    date_dir = _date_dir(a)
    mats = jta_dispatch.prepare_dispatch_materials(date_dir)
    ready = [i for i in mats["items"] if i["has_prompt"]]
    if ready:
        print("\n" + "=" * 60)
        print(f"有 {len(ready)} 单已就绪，等待派发 subagent：")
        for i in ready:
            print(f"  - {i['key']}  prompt: {i['prompt']}")
        print("\n下一步（必须由 Claude 会话执行，见 prompts/orchestrator.md）：")
        print("  对每单用 Agent 工具派 general-purpose subagent，prompt 取对应的 worker_prompt.md；")
        print("  一次一单、顺序执行。subagent 会写 analysis.md 与 receipt.json。")
        print("  全部完成后：")
        print(f'    jtat.py summary --date {date_dir.name}')
        print(f'    jtat.py mail-only --date {date_dir.name}')
        print("=" * 60)
    if getattr(a, "send", False):
        rc3 = cmd_mail(a)
        rc = max(rc, rc3) if rc != rc3 else rc
    return rc


def cmd_repo(a: argparse.Namespace) -> int:
    cfg = env.load_config()
    projects = cfg.get("projects") or []
    out = []
    for p in projects:
        gl = p.get("gitlab") or {}
        env.log(f"取代码 {gl.get('project')} @ {gl.get('branch')} …")
        r = jta_repo.ensure_code(gl.get("project", ""), gl.get("branch", ""),
                                 p.get("analysis_scope"))
        r["scope"] = p.get("analysis_scope")
        if r.get("ok"):
            md = jta_repo.prepare_claude_md(r)
            r["claude_md"] = md
            jta_repo.snapshot_claude_md(r)
        out.append(r)
    print(json.dumps(out, ensure_ascii=False, indent=2)[:4000])
    return EXIT_OK if all(x.get("ok") for x in out) else EXIT_ERR


def cmd_dbc(a: argparse.Namespace) -> int:
    d = Path(a.dir) if a.dir else env.tool_path(env.cfg_get("dbc_dir", default=""))
    if not d.exists():
        print(f"DBC 目录不存在：{d}", file=sys.stderr)
        return EXIT_ARG
    entries = jta_dbc.index_all(d)
    out = env.workspace_root() / "dbc_index.md"
    jta_dbc.write_index(entries, out)
    print(f"索引 {len(entries)} 份 → {out}")
    for e in entries:
        print(f"  {e['file']}  日期={e['effective_date']}  版本={e['effective_version']}"
              f"  报文={e['message_count']}")
    return EXIT_OK


def cmd_status(a: argparse.Namespace) -> int:
    st = jta_dispatch.load_state()
    print(json.dumps(st, ensure_ascii=False, indent=2)[:3000])
    return EXIT_OK


def cmd_summary(a: argparse.Namespace) -> int:
    """从 receipt.json 生成 SUMMARY.md（发邮件前跑）。"""
    date_dir = _date_dir(a)
    fs = env.read_json(date_dir / "_fetch_summary.json", {}) or {}
    out = jta_dispatch.write_summary(date_dir, fs.get("skipped_by_limit", 0))
    print(f"SUMMARY → {out}")
    print(out.read_text(encoding="utf-8")[:2000])
    return EXIT_OK


def cmd_mail(a: argparse.Namespace) -> int:
    date_dir = _date_dir(a)
    # 发信前确保 SUMMARY 存在且是最新的（失败/跳过不会被漏掉）
    fs = env.read_json(date_dir / "_fetch_summary.json", {}) or {}
    jta_dispatch.write_summary(date_dir, fs.get("skipped_by_limit", 0))
    r = jta_mail.send_daily(date_dir, dry_run=a.dry_run)
    print(json.dumps(r, ensure_ascii=False, indent=2)[:3000])
    return EXIT_OK if r.get("ok") or r.get("dry_run") else EXIT_ERR


# ---------------------------------------------------------------- main


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(
        prog="jtat", description="Jira 工单 → 代码感知分析 → 邮件 流水线")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("validate", help="环境自检").set_defaults(fn=cmd_validate)

    p = sub.add_parser("list", help="只列工单")
    p.add_argument("--jql"); p.add_argument("--limit", type=int, default=20)
    p.set_defaults(fn=cmd_list)

    def add_common(sp):
        sp.add_argument("--keys", help="逗号分隔的工单 key")
        sp.add_argument("--jql", help="覆盖 JQL")
        sp.add_argument("--limit", type=int, help="最多几张")
        sp.add_argument("--date", help="产物日期目录 YYYY-MM-DD（默认今天）")
        return sp

    add_common(sub.add_parser("fetch", help="拉工单+附件")).set_defaults(fn=cmd_fetch)
    add_common(sub.add_parser("prepare", help="解析附件+取代码+组装 bundle")).set_defaults(fn=cmd_prepare)
    add_common(sub.add_parser("run", help="fetch+prepare+summary")).set_defaults(fn=cmd_run)

    pa = add_common(sub.add_parser("all", help="run + 提示派发（可 --send 发信）"))
    pa.add_argument("--send", action="store_true", help="派发完成后自动发邮件")
    pa.set_defaults(fn=cmd_all)

    pr = sub.add_parser("repo", help="只取代码+CLAUDE.md"); pr.set_defaults(fn=cmd_repo)

    pd = sub.add_parser("dbc", help="只做 DBC 索引")
    pd.add_argument("--dir"); pd.set_defaults(fn=cmd_dbc)

    sub.add_parser("status", help="看水位").set_defaults(fn=cmd_status)

    ps = sub.add_parser("summary", help="从 receipt 生成 SUMMARY.md")
    ps.add_argument("--date"); ps.set_defaults(fn=cmd_summary)

    pm = sub.add_parser("mail-only", help="只发邮件")
    pm.add_argument("--date"); pm.add_argument("--dry-run", action="store_true")
    pm.set_defaults(fn=cmd_mail)

    pf = add_common(sub.add_parser(
        "feedback", help="在工单下建子任务：附件挂全文 + 打标签（父单不动）+ 台账"))
    pf.add_argument("--apply", action="store_true", help="实跑（默认 dry-run 预览）")
    pf.add_argument("--force", action="store_true", help="台账里已成功的单也重写")
    pf.add_argument("--subtask-type", help="覆盖子任务类型名（默认自动探测并缓存）")
    pf.add_argument("--refresh-type", action="store_true", help="重探子任务类型（忽略缓存）")
    pf.add_argument("--no-check-required", action="store_true",
                    help="建子任务时跳过必填 preflight（AERDM 的 customfield 必填标记已过时，"
                         "不跳过会以退出码 2 拒绝创建；等价于 config.feedback.skip_required_check）")
    pf.set_defaults(fn=cmd_feedback)

    sub.add_parser("labels", help="打印标签表（template/labels.md），自检可读性"
                   ).set_defaults(fn=cmd_labels)

    a = ap.parse_args(argv)

    # cwd 安全检查：cwd 下若有 jira/ 同名目录，会让 `import jira` 解析成命名空间包
    try:
        if env.cwd_shadows_jira():
            print(f"✗ 当前 cwd（{Path.cwd()}）下有 jira/ 同名目录，"
                  f"会让 `import jira` 解析成命名空间包。\n"
                  f"  请 cd 到工具目录再跑：{env.TOOL_DIR}\n"
                  f"  （注：子进程已自动用安全 cwd，但本进程内的 import 仍会被遮蔽）",
                  file=sys.stderr)
            return EXIT_ARG
    except OSError:
        pass

    try:
        return a.fn(a)
    except FileNotFoundError as e:
        print(f"✗ {e}", file=sys.stderr)
        return EXIT_ERR
    except RuntimeError as e:
        msg = str(e)
        print(f"✗ {msg}", file=sys.stderr)
        if "退出码 3" in msg or "401" in msg or "403" in msg:
            return EXIT_AUTH
        if "退出码 4" in msg:
            return EXIT_API
        return EXIT_ERR


if __name__ == "__main__":
    sys.exit(main())
