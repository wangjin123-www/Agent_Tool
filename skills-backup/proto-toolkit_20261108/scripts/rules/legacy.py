# -*- coding: utf-8 -*-
"""聚合规则适配层：把既有 checker 接入注册表，修复路径收敛到 Rule.repair。

约定（本层唯一职责）：
  report(ctx)`       = 只读校验（checker 的 repair=False / dry=True）
  repair(ctx, sink)` = 校验并把修复意图塞进 sink（checker 的 repair=True）

「修不修」只由 rules.Rule.report 依据 dry 决定，checker 不再自己从 dry 推导修复；
写表统一由 rules.apply_fix 执行，checker 内部不直接调 feishu 写接口。
dry-run 另有 feishu 只读闸门兜底（见 common/feishu.py）。
"""
from . import Rule, register
from ..check import (validate_semantics, validate_sections, validate_links,
                     validate_enum_style, validate_param_desc, validate_merges)
from ..common.log import Report, OK, WARN


def _cov_report(ctx):
    """校验手段 A：解析覆盖率对账——有跳过行就告警并列行号，防静默丢数据。"""
    rep = Report("")
    stats = ctx.proto.source.get("parse_stats") or {}
    skipped = 0
    for sheet in sorted(stats):
        for row, reason in stats[sheet].get("skipped") or ():
            skipped += 1
            rep.add(WARN, "COV", "%s 行%d 被跳过：%s" % (sheet, row, reason))
    if not skipped:
        rep.add(OK, "COV", "解析覆盖率 100%%：%s" % "，".join(
            "%s %d 行" % (k, v.get("rows", 0)) for k, v in sorted(stats.items())) or "无统计")
    return rep


# 注册顺序 = sync 输出顺序（COV 解析层最先，其后语义；与 cli.cmd_sync 改造前一致）
register(Rule("COV", "解析覆盖率对账", rule_no=[],
              report=_cov_report))

register(Rule("SEM", "语义校验", rule_no=[],
              report=lambda ctx: validate_semantics(ctx.proto)))

register(Rule("SEC", "分节行禁用检查（规则 27 已废弃）", rule_no=[],
              report=lambda ctx: validate_sections(ctx.cfg, ctx.si, ctx.proto)))

register(Rule("LNK", "链接校验", rule_no=[8, 15, 25, 26],
              report=lambda ctx: validate_links(ctx.cfg, ctx.proto, ctx.si, ctx.ds,
                                                ctx.pe, repair=False),
              repair=lambda ctx, sink: validate_links(ctx.cfg, ctx.proto, ctx.si, ctx.ds,
                                                      ctx.pe, repair=True, sink=sink)))

register(Rule("STY", "枚举块样式", rule_no=[13],
              report=lambda ctx: validate_enum_style(ctx.cfg, ctx.proto, repair=False),
              repair=lambda ctx, sink: validate_enum_style(ctx.cfg, ctx.proto,
                                                           repair=True, sink=sink)))

register(Rule("S16", "参数描述值域检查", rule_no=[8],
              report=lambda ctx: validate_param_desc(ctx.cfg, ctx.si)))

register(Rule("MERGE", "服务块合并（SI A~D）", rule_no=[17],
              report=lambda ctx: validate_merges(dry=True, rows=ctx.si),
              repair=lambda ctx, sink: validate_merges(dry=False, rows=ctx.si, sink=sink)))
