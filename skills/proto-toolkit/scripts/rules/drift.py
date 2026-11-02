# -*- coding: utf-8 -*-
"""规则表对账（P2）：代码里的 rule_no ↔ 飞书「AI修订规则」子表，防双源漂移。

三个判据：
  1. 代码声明了 rule_no，但规则表里没有该序号 → ERR（代码引用了不存在的规则）
  2. 规则表新增了序号，但没有 Rule 覆盖 → WARN（新规则未落地到检查器）
  3. 规则表 C 列（规则正文）相对快照有变化 → WARN（判据可能已改，需复核检查器）

快照存 config/rule_snapshot.json：{序号: sha1(规则正文)}。
`sync --freeze-rules` 才刷新快照（确认检查器已跟上规则表后执行）。
"""
import hashlib

from . import Rule, Issue, register, RULES, read_snapshot, write_snapshot
from ..common import feishu
from ..common.log import OK, WARN, ERR


def _rule_rows(ctx):
    """[(序号, 规则正文 sha1)]；A 列序号 / C 列规则正文（AI 必须遵守）。"""
    try:
        rows = feishu.read(ctx.cfg, "rule", "F")
    except RuntimeError:
        return None
    out = []
    for r in range(2, len(rows) + 1):
        no = feishu.cell_text(feishu.cell_at(rows, r, "A")).strip()
        body = feishu.cell_text(feishu.cell_at(rows, r, "C")).strip()
        if not no.isdigit():
            continue
        out.append((int(no), hashlib.sha1(body.encode("utf-8")).hexdigest()))
    return out


def _covered_nos():
    nos = set()
    for r in RULES:
        nos.update(r.rule_no)
    return nos


def _detect(ctx, dry=True):
    rows = _rule_rows(ctx)
    if rows is None:
        return [Issue("RUL", "读不到「AI修订规则」子表，跳过对账", WARN)]
    table_nos = {no for no, _h in rows}
    covered = _covered_nos()
    snap = read_snapshot()
    out = []

    missing = sorted(covered - table_nos)
    if missing:
        out.append(Issue("RUL", "检查器引用了规则表里不存在的规则号：%s"
                         % ",".join(map(str, missing)), ERR))

    uncovered = sorted(table_nos - covered)
    if uncovered:
        out.append(Issue("RUL", "规则表有 %d 条规则未被任何检查项覆盖：%s（如属流程约束可忽略）"
                         % (len(uncovered), ",".join(map(str, uncovered))), WARN))

    if snap:
        changed = sorted(no for no, h in rows if snap.get(str(no)) not in (None, h))
        if changed:
            out.append(Issue("RUL", "规则正文已变更（序号 %s），检查器判据需复核；"
                                    "确认后 sync --freeze-rules 刷新快照"
                             % ",".join(map(str, changed)), WARN))
    if not out:
        out.append(Issue("RUL", "规则表 %d 条，检查器覆盖 %d 条，快照一致"
                         % (len(table_nos), len(covered & table_nos)), OK))
    return out


def _report(ctx):
    from ..common.log import Report
    rep = Report("")
    for iss in _detect(ctx, True):
        rep.add(iss.severity, iss.rule_id, iss.msg)
    return rep


def freeze(ctx=None):
    """把当前规则表正文 hash 写成快照。返回写入条数。只读规则表，不读三表。"""
    if ctx is None:
        from ..common import conf
        ctx = type("RuleCtx", (), {"cfg": conf.proto()})()
    rows = _rule_rows(ctx) or []
    # 只快照已覆盖的序号，避免新规则一出现就天天告警
    covered = _covered_nos()
    data = {str(no): h for no, h in rows if no in covered}
    write_snapshot(data)
    return len(data)


register(Rule("RUL", "规则表对账", rule_no=[], report=_report))
