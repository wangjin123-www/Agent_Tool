#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
jta_feedback —— 分析结果回写成**子任务** + 台账。

对每个已有 analysis.md 的工单：
  1. 建子任务：summary = 【分析】<原父单标题>，description = 一句话结论 + 关键假设
  2. 附件：整份 analysis.md 作为子任务的一个附件 <父单key>-分析报告.md
     **不发评论** —— JIRA Server 的评论按 wiki 标记渲染，Markdown 正文贴进去
     会显示成字面的 ## / ** ；做成 .md 附件反倒是干净的可下载文件
  3. 标签：已分析,<标签表内的词 ≤2 个>，随建单的 --labels 一并落盘；仅当复用
     旧子任务时才用 update_issue.py --add-labels --notify 补打
     —— 词表见 template/labels.md，由 jta_labels 收敛；表外词一律丢弃
  4. 台账：workspace/out/ledger.json + ledger.md（防重复回写）

**父单不动**：不发评论、不改标题、不打标签、不改状态。所有产出都落在子任务上。

门禁：默认 dry-run（只打印将写什么，不写 Jira）；jtat feedback --apply 才实跑。
      已在台账里的单默认跳过，--force 重写。
写操作全部经 vendor/jira-tool 的 ops 脚本（自带 --dry-run / 幂等防呆），
本模块不直接 import jira 库写数据。
"""

from __future__ import annotations

import json
import re
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional

import jta_env as env
import jta_fetch
import jta_labels

SUBTASK_PREFIX = "【分析】"

# AERDM 建子任务时 REST 强制要求的自定义字段（createmeta 不返回 allowed_values，
# 只能写死字段 id；取值见 _required_fields）
F_STAGE = "customfield_10310"   # 所处阶段（option，接受 {"value": "EVT"}）
F_OWNER = "customfield_10447"   # 责任人（multiuserpicker，接受 [{"name": "..."}]）

STAGE_DEFAULT = "EVT"
DUE_DAYS_DEFAULT = 7

# 子任务类型探测结果的缓存（避免每单都打一次 createmeta）
_TYPE_CACHE = "subtask_types.json"

# 落进台账的字段。定义在这里而不是调用方 —— 白名单和产出字段必须一起改，
# 否则新增字段会被静默丢掉（历史上就踩过）。
LEDGER_FIELDS = ("key", "at", "title", "subtask", "labels", "conclusion",
                 "method", "status", "error", "update_error")


# ---------------------------------------------------------------- 台账


def ledger_json_path() -> Path:
    return env.out_root() / "ledger.json"


def load_ledger() -> List[Dict[str, Any]]:
    return env.read_json(ledger_json_path(), []) or []


def write_ledger(entries: List[Dict[str, Any]]) -> Path:
    """ledger.json（机器读）+ ledger.md（人读的台账表）。"""
    env.write_json(ledger_json_path(), entries)
    lines = [
        "# 已分析工单台账",
        "",
        "| 日期 | 工单 | 子任务 | 标题 | 标签 | 一句话结论 | 回写方式 |",
        "|---|---|---|---|---|---|---|",
    ]
    for e in entries:
        conclusion = (e.get("conclusion") or "").replace("|", "\\|")
        lines.append(
            f"| {(e.get('at') or '')[:10]} | {e.get('key', '')} | "
            f"{e.get('subtask', '')} | "
            f"{(e.get('title') or '').replace('|', '\\|')} | "
            f"{','.join(e.get('labels') or [])} | {conclusion} | "
            f"{e.get('method', '')} |"
        )
    md = env.out_root() / "ledger.md"
    env.write_text(md, "\n".join(lines) + "\n")
    return md


# ---------------------------------------------------------------- 从报告提取


def parse_labels(text: str) -> Dict[str, Any]:
    """
    报告头部 `> labels: a, b, c` 行 → 收敛到标签表内的词。
    返回 {"labels": [...], "dropped": [...表外词]}。
    """
    m = re.search(r"^>\s*labels:\s*(.+)$", text, re.M)
    cands = re.split(r"[,，;；]", m.group(1)) if m else []
    return jta_labels.filter_labels(cands)


def extract_conclusion(text: str) -> str:
    """第 0 节「一句话结论」→ 单行文本（台账/描述用，截 200 字）。"""
    m = re.search(r"^## 0\..*?\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not m:
        return ""
    return " ".join(m.group(1).split())[:200]


def extract_hypotheses(text: str, *, limit: int = 3) -> List[str]:
    """第 3 节「根因假设」的前若干条 → 列表（子任务描述用）。"""
    m = re.search(r"^## 3\..*?\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not m:
        return []
    out: List[str] = []
    for ln in m.group(1).splitlines():
        s = ln.strip()
        if not s.startswith(("-", "*")) and not re.match(r"^\d+[.、)]", s):
            continue
        s = re.sub(r"^[-*]\s*|^\d+[.、)]\s*", "", s)
        s = s.replace("**", "").strip()
        if not s or len(s) <= 4:
            continue
        if len(s) > 120:
            # 尽量断在标点上，别把词切一半（这段会直接显示在 JIRA 子任务描述里）
            cut = max(s.rfind(c, 0, 120) for c in "。；，,;：")
            s = (s[:cut] if cut > 40 else s[:120]).rstrip() + "…"
        out.append(s)
        if len(out) >= limit:
            break
    return out


def _json_arg(obj: Dict[str, Any]) -> str:
    """--data 的 JSON 参数（不落盘，直接作为单个 argv 传给子进程）。"""
    return json.dumps(obj, ensure_ascii=False)


def _skip_required_check(override: bool = False) -> bool:
    """
    是否给 create_issue.py 加 --no-check-required。

    为什么需要：create_issue.py 在**非 dry-run** 下发现 createmeta 声称的必填字段没填时
    会直接 arg_fail(退出码 2) 拒绝创建。而 AERDM 的「所处阶段/责任人/开始时间」被标成
    required、allowed_values 却是 null、实测最近 12 张单（含本工具自己建的任务）这三个
    字段**全是空**——即该 required 标记是过时的，不跳过就完全建不出子任务。
    """
    if override:
        return True
    return bool(env.cfg_get("feedback", "skip_required_check", default=False))


def _required_fields(issue: Dict[str, Any]) -> Dict[str, Any]:
    """
    建子任务时 JIRA 强制要求的四个字段。

    AERDM 实测（2026-09-16）：不带这四个字段，REST 直接 HTTP 400
    「经办人/责任人/所处阶段/到期日 是必填项」。而 createmeta 既不返回 allowed_values，
    现存旧子任务里这些字段又基本都是空的（说明它们是后来才被设为必填的），所以只能：
      * assignee / 责任人 ← 父单经办人，其次 config.feedback.assignee
      * 所处阶段           ← config.feedback.stage（默认 EVT；合法值见 labels 之外的
                              JIRA 字段配置：EVT/DVT/PVT/MP/测试阶段/送样）
      * 到期日             ← 父单到期日；已过期则今天 + config.feedback.due_days（默认 7）
    """
    cfg = env.cfg_get("feedback", default=None) or {}
    out: Dict[str, Any] = {}

    owner = (issue.get("assignee") or {}).get("name") or cfg.get("assignee") or ""
    if owner:
        out["assignee"] = {"name": owner}
        out[F_OWNER] = [{"name": owner}]

    stage = cfg.get("stage", STAGE_DEFAULT)
    if stage:
        out[F_STAGE] = {"value": stage}

    today = date.today()
    parent_due = str(issue.get("duedate") or "")[:10]
    keep = False
    if parent_due:
        try:
            keep = date.fromisoformat(parent_due) >= today
        except ValueError:
            keep = False
    if keep:
        out["duedate"] = parent_due
    else:
        try:
            days = int(cfg.get("due_days", DUE_DAYS_DEFAULT))
        except (TypeError, ValueError):
            days = DUE_DAYS_DEFAULT
        out["duedate"] = (today + timedelta(days=days)).isoformat()
    return out


def _extra_fields() -> Dict[str, Any]:
    """
    config.feedback.extra_fields —— 建子任务时额外补的 fields（原样并入 --data）。

    AERDM 的 createmeta 把「所处阶段/责任人/到期日」标成 required，但真实子任务里
    这些多为空，通常不阻塞；万一某个项目真要，就在这里按 Jira 字段名或 id 补。
    """
    extra = env.cfg_get("feedback", "extra_fields", default=None)
    return extra if isinstance(extra, dict) else {}


# ---------------------------------------------------------------- Jira 操作


def _ops(args: List[str], timeout: int = 120) -> Dict[str, Any]:
    """跑一个 jira-tool ops 脚本（venv python），stdout 当 JSON。失败抛异常。"""
    return env.run_python_json(args, timeout=timeout)


def resolve_subtask_type(project: str, override: Optional[str] = None,
                         *, refresh: bool = False) -> str:
    """
    找该项目的子任务 issue 类型名。优先参数/config，其次探测并缓存。

    缓存放 workspace/out/subtask_types.json（按项目 key 分桶）。
    探测不到就抛 —— 宁可停，也不要瞎创建一个普通任务挂在父单外面。
    """
    if override:
        return override
    cfg_type = env.cfg_get("feedback", "subtask_type", default=None)
    if cfg_type:
        return str(cfg_type)
    cache_path = env.out_root() / _TYPE_CACHE
    cache = {} if refresh else (env.read_json(cache_path, {}) or {})
    if cache.get(project):
        return cache[project]

    data = _ops([env.jira_ops_script("createmeta.py"), "--project", project,
                 "--list-types", "--compact"])
    subs = [t for t in (data.get("issue_types") or []) if t.get("subtask")]
    if not subs:
        raise RuntimeError(
            f"项目 {project} 没有可用的子任务类型，无法建分析子任务。\n"
            f"  可在 config.json 的 feedback.subtask_type 里显式指定。")
    # 取第一个（Jira 默认子任务类型唯一；有多个时按名称稳定排序，避免每次不同）
    name = sorted(subs, key=lambda t: t.get("name") or "")[0].get("name") or ""
    cache[project] = name
    env.write_json(cache_path, cache)
    return name


def find_subtask(parent_key: str) -> Optional[Dict[str, Any]]:
    """查父单下是否已有分析子任务（summary 以 【分析】 开头）。"""
    data = _ops([env.jira_ops_script("search.py"),
                 "--jql", f"parent = {parent_key}",
                 "--fields", "key,summary,status",
                 "--limit", "50", "--compact"], timeout=90)
    for it in data.get("issues") or []:
        if (it.get("summary") or "").startswith(SUBTASK_PREFIX):
            return it
    return None


def attachment_exists(subtask_key: str, filename: str) -> bool:
    """
    子任务上是否已有同名附件（幂等第 ③ 层：认文件名）。

    报告正文不再走评论，所以幂等从"评论头标记"改成"附件同名检测"。
    文件名是确定的 `<父单 key>-分析报告.md`，重跑时认它即可。
    """
    try:
        data = _ops([env.jira_ops_script("attachments.py"), "list", subtask_key,
                     "--compact"], timeout=90)
    except Exception:  # noqa: BLE001 — 读不到就当作没有，顶多多传一份重复附件
        return False
    return any((a.get("filename") or "") == filename
               for a in data.get("attachments") or [])


def _build_description(conclusion: str, hyps: List[str], att_name: str) -> str:
    """子任务描述：一句话结论 + 关键假设（全文不放这儿 —— 在附件里）。"""
    L = ["h3. 一句话结论", conclusion or "（报告未给出结论，见附件全文）", ""]
    if hyps:
        L.append("h3. 关键假设")
        L += [f"* {h}" for h in hyps]
    L += ["", "h3. 完整报告", f"见本子任务附件 {att_name}（自动回写）。"]
    return "\n".join(L)


# ---------------------------------------------------------------- 回写主流程


def feedback_one(ticket_dir: Path, *, apply: bool = False,
                 ledger: Optional[List[Dict[str, Any]]] = None,
                 subtask_type: Optional[str] = None,
                 refresh_type: bool = False,
                 no_check_required: bool = False) -> Dict[str, Any]:
    """
    单票回写。返回结果字典（status: ok / partial / planned / skipped / failed）。
    dry-run（apply=False）时只走 ops 的 --dry-run，不写 Jira。
    """
    key = ticket_dir.name
    text = (ticket_dir / "analysis.md").read_text(encoding="utf-8")
    picked = parse_labels(text)
    labels = picked["labels"]
    conclusion = extract_conclusion(text)
    hyps = extract_hypotheses(text)
    att_name = f"{key}-分析报告.md"   # 描述里要引用，附件上传也要用，故提前定名

    if ledger is not None and any(
            e.get("key") == key and e.get("status") == "ok" for e in ledger):
        env.log(f"  {key} 已在台账中且回写成功，跳过（--force 可重写）")
        return {"key": key, "status": "skipped"}

    issue = jta_fetch.get_issue(key)
    cur_title = issue.get("summary", "")
    project = key.rsplit("-", 1)[0]
    summary = SUBTASK_PREFIX + cur_title

    dry = [] if apply else ["--dry-run"]
    result: Dict[str, Any] = {
        "key": key, "applied": apply, "labels": labels,
        "dropped_labels": picked["dropped"],
        "title": cur_title, "summary": summary, "conclusion": conclusion,
    }
    if picked["dropped"]:
        env.log(f"  {key} 丢弃表外标签：{', '.join(picked['dropped'])}"
                f"（如需保留请先加进 template/labels.md）")

    # 1) 找 / 建子任务
    existing = find_subtask(key)
    if existing:
        sub_key = existing["key"]
        result["subtask"] = sub_key
        result["subtask_existed"] = True
        env.log(f"  {key} 已有子任务 {sub_key}，复用")
    else:
        try:
            itype = resolve_subtask_type(project, subtask_type, refresh=refresh_type)
        except Exception as e:  # noqa: BLE001
            return {"key": key, "status": "failed",
                    "error": f"子任务类型探测失败：{str(e)[:200]}"}
        result["subtask_type"] = itype
        skip_req = _skip_required_check(no_check_required)
        result["skip_required_check"] = skip_req
        create_args = [
            env.jira_ops_script("create_issue.py"),
            "--project", project, "--type", itype,
            "--summary", summary,
            "--description", _build_description(conclusion, hyps, att_name),
            "--labels", ",".join(labels),
            # 顺序：必填字段默认值 → config 显式覆盖 → parent 兜底（parent 不可被覆盖）
            "--data", _json_arg({**_required_fields(issue), **_extra_fields(),
                                 "parent": {"key": key}}),
            "--compact",
            *(["--no-check-required"] if skip_req else []),
        ]
        try:
            cr = _ops([*create_args, *dry])
        except Exception as e:  # noqa: BLE001
            return {"key": key, "status": "failed",
                    "error": f"建子任务失败：{str(e)[:200]}"}
        # 只留可读的要点：ops 的完整返回里塞着整份字段元数据，
        # 原样带出去会把 stdout 的 4000 字配额吃光、把结论挤掉。
        miss = [m.get("name") for m in (cr.get("missing_required") or [])]
        result["create"] = {
            "dry_run": cr.get("dry_run"), "skipped": cr.get("skipped"),
            "issue_type": (cr.get("issue_type") or {}).get("name"),
            "fields": (cr.get("payload") or {}).get("fields"),
            "key": cr.get("key"), "url": cr.get("url"),
            "missing_required": miss,
        }
        if miss:
            # createmeta 说必填、但真实子任务里这些多为空 → 通常不阻塞，别硬拦
            env.log(f"  JIRA 声明必填但未提供：{', '.join(miss)}"
                    f"（实际多为空、通常不阻塞；若 --apply 报 400 就在 "
                    f"config.feedback.extra_fields 里补）")
        sub_key = cr.get("key") or (cr.get("issue") or {}).get("key")
        if not sub_key:
            if not apply:
                # dry-run 下没有真 key，附件/标签只能停在"计划"层面
                result["status"] = "planned"
                result["method"] = "dry-run"
                result["planned"] = {
                    "create": f"新建子任务 {summary}（类型 {itype}）",
                    "attachment": f"把分析全文传成该子任务的附件 {att_name}",
                    "labels": f"给该子任务打标签 {','.join(labels)}",
                }
                result["at"] = f"{datetime.now():%Y-%m-%d %H:%M}"
                return result
            return {"key": key, "status": "failed",
                    "error": f"建子任务未返回 key：{cr}"}
        result["subtask"] = sub_key
        result["subtask_existed"] = False
        env.log(f"  {key} 新建子任务 {sub_key}")

    # 2) 报告 → 子任务的附件。**不发评论**：JIRA Server 的评论按 wiki 标记渲染，
    #    而 analysis.md 是 Markdown，贴进评论会显示成字面的 ## / ** ；
    #    做成 .md 附件反倒是干净的可下载文件。
    att = ticket_dir / f"{key}-分析报告.md"
    env.write_text(
        att,
        f"> 自动回写 by jira-ticket-analysis · {datetime.now():%Y-%m-%d %H:%M}\n"
        f"> 父单：{key}（父单未做改动）\n\n{text}",
    )
    if apply and attachment_exists(sub_key, att.name):
        env.log(f"  {sub_key} 已有附件 {att.name}，跳过上传")
        result["method"] = "attachment-exists"
    else:
        try:
            result["attachment"] = _ops(
                [env.jira_ops_script("attachments.py"), "add", sub_key,
                 "--file", str(att), "--filename", att.name, *dry])
            result["method"] = "attachment"
        except Exception as e:  # noqa: BLE001
            result["attachment_error"] = str(e)[:200]
            result["status"] = "partial"
            result["at"] = f"{datetime.now():%Y-%m-%d %H:%M}"
            return result

    # 3) 标签：建单时已随 create 的 --labels 落盘，只有"复用旧子任务"才需补打
    if result.get("subtask_existed"):
        try:
            # --notify 必须带：update_issue.py 默认 notify=False，会给 PUT 拼上
            # ?notifyUsers=false，而 JIRA Server 只允许管理员抑制通知 → 403
            # （AERDM 实测退出码 4）。带上它即走默认通知行为，不再 403。
            r = _ops([env.jira_ops_script("update_issue.py"), sub_key,
                      "--add-labels", ",".join(labels), "--notify", *dry])
            result["update"] = {"skipped": r.get("skipped"),
                                "changed": r.get("changed")}
        except Exception as e:  # noqa: BLE001
            result["update_error"] = str(e)[:200]
            result["status"] = "partial"
            result["at"] = f"{datetime.now():%Y-%m-%d %H:%M}"
            return result
    else:
        result["update"] = {"skipped": True, "reason": "labels-set-on-create"}

    # dry-run 什么都没写，别报 ok（与"新建"分支的 planned 保持一致）
    result["status"] = "ok" if apply else "planned"
    result["at"] = f"{datetime.now():%Y-%m-%d %H:%M}"
    return result
