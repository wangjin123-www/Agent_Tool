# -*- coding: utf-8 -*-
"""规则注册表：检查（sync）与修改（edit）统一调用的唯一规范层。

一条规范 = Rule：
  id        检查码（S01~S17 / SEC / LNK / MERGE / Rxx）
  title     一句话说明
  rule_no   「AI修订规则」子表序号，供 drift 对账（见 rules/drift.py）
  scope     "table"（全表检查，sync 调）/ "precheck"（未落表的 edit ops 预检）
  fixable   是否有自动修（sync --materialize 才执行，默认只报不改）

三类 Rule：
  1. 聚合规则（adapters）：把既有 checker 的 validate() 原样接入，行为不变；
  2. 细粒度规则（basic）：本层新写的判据，返回 Issue 列表，可带 fix；
  3. 预检规则（precheck）：针对 edit ops 的纯逻辑检查，写表前拦住。

调用方只有两个入口：
  run_sync(dry, materialize)  → Report（cli.py sync）
  run_precheck(ctx, ops)      → [(level, code, msg)]（edit apply 写表前）
"""
import json

from ..common import conf, feishu
from ..common.log import Report, ERR, WARN, OK, INFO
from ..parse import parse_protocol

RULES = []


class Issue:
    """一条检查结果；fix 存在时表示「规则知道怎么修」。"""

    def __init__(self, rule_id, msg, severity=WARN, rule_no=(), fix=None):
        self.rule_id = rule_id
        self.msg = msg
        self.severity = severity
        self.rule_no = tuple(rule_no)
        self.fix = fix

    def row(self):
        return (self.severity, self.rule_id, self.msg)

    def __repr__(self):
        return "Issue(%s,%s,%s)" % (self.rule_id, self.severity, self.msg[:40])


class Rule:
    def __init__(self, rid, title, rule_no=(), scope="table", fixable=False,
                 detect=None, fix=None, report=None, precheck=None, default=True,
                 repair=None):
        self.id = rid
        self.title = title
        self.rule_no = list(rule_no)
        self.scope = scope
        self.fixable = fixable
        self.default = default          # False = 需 --materialize 才参与
        self._detect = detect
        self._fix = fix
        self._report = report
        self._precheck = precheck
        self._repair = repair           # 唯一修复入口：仅非 dry 时由 report() 调用

    def detect(self, ctx, dry=True):
        return list(self._detect(ctx, dry)) if self._detect else []

    def fix(self, ctx, issues):
        if not (self.fixable and self._fix):
            return []
        return list(self._fix(ctx, issues))

    def report(self, ctx, dry=True):
        """dry → 只读校验；非 dry → 走本规则的 repair（内部校验+修+回验）。

        「修不修」由注册表这一处决定，checker 不再各自从 dry 参数推导。
        repair 回调签名统一为 repair(ctx, sink)：只把修复意图塞进 sink，
        真正的写表统一由 apply_fix 执行——checker 内部不再直接写表。
        """
        if self._repair:
            if dry:
                return self._report_only(ctx)
            sink = {}
            rep = self._repair(ctx, sink)
            for act in apply_fix(ctx, sink):
                print("  → %s %s" % (self.id, act))
            return rep
        if self._report:
            return self._report(ctx)
        rep = Report("")
        for i in self.detect(ctx, dry):
            rep.add(i.severity, i.rule_id, i.msg)
        return rep

    def _report_only(self, ctx):
        """dry 专用：只跑只读 side（repair 规则若另有 report 就用它）。"""
        if self._report:
            return self._report(ctx)
        rep = Report("")
        for i in self.detect(ctx, True):
            rep.add(i.severity, i.rule_id, i.msg)
        return rep

    def precheck(self, ctx, op):
        return list(self._precheck(ctx, op)) if self._precheck else []


def register(rule):
    RULES.append(rule)
    return rule


class Ctx:
    """一次检查的表快照 + 解析后的 Protocol（fix 后需 reload）。

    pending_structs / pending_enums：run_precheck 注入的「本批 edit ops 将新增的
    定义名」——precheck 判引用存在性时，已存在的 + 本批将新增的都算命中
    （add_struct → add_interface 引用同批新 struct 是合法序列）。
    """

    def __init__(self, cfg=None):
        self.cfg = cfg or conf.proto()
        self.pending_structs = set()
        self.pending_enums = set()
        self.reload()

    def reload(self):
        self.si = feishu.read(self.cfg, "service_interface", "Q")
        self.ds = feishu.read(self.cfg, "data_structure", "K")
        self.pe = feishu.read(self.cfg, "parameter_enum", "E")
        self.proto = parse_protocol(self.cfg, {"si": self.si, "ds": self.ds, "pe": self.pe})
        return self


def issues_of(rep):
    """Report → Issue 列表（聚合规则转细粒度时用）。"""
    return [Issue(code, msg, level) for level, code, msg in rep.rows]


def apply_fix(ctx, fix):
    """执行修复意图（本层是唯一允许写表的规则入口）。

    checker 只把「要写什么」塞进 sink，由这里统一落到飞书；形态三种：
      writes  → feishu.write_writes 的 write 列表
      styles  → [(sheet_key, [style, ...])]
      merges  → [(sheet_key, unmerge_range, [merge_range, ...])]
    dry-run 时不写：feishu 的只读闸门会直接抛 ReadOnlyError。
    """
    acts = []
    writes = list(fix.get("writes") or [])
    if writes:
        feishu.write_writes(ctx.cfg, writes)
        acts.append("写 %d 处" % len(writes))
    for sheet_key, styles in fix.get("styles") or ():
        feishu.apply_styles(ctx.cfg, sheet_key, styles)
        acts.append("样式 %s ×%d" % (sheet_key, len(styles)))
    for sheet_key, unmerge_rng, merge_rngs in fix.get("merges") or ():
        feishu.unmerge(ctx.cfg, sheet_key, unmerge_rng)
        feishu.merge(ctx.cfg, sheet_key, merge_rngs)
        acts.append("合并 %s %s" % (sheet_key, unmerge_rng))
    return acts


def by_scope(scope="table", materialize=False):
    out = []
    for r in RULES:
        if r.scope != scope:
            continue
        if not r.default and not materialize:
            continue
        out.append(r)
    return out


def run_sync(dry=False, materialize=False):
    """sync 入口：先跑可修的规则（非 dry 且 materialize），再全量校验。

    返回 (Report, fixed_msgs, ctx)。只读一遍表（Ctx 复用），修完自动 reload。
    dry 时开启写表闸门：任何 checker 误写表都会抛 ReadOnlyError，而不是悄悄生效。
    """
    ctx = Ctx()
    prev = feishu.set_read_only(dry)     # legacy 引擎同用这把闸门（其 cli 已是 feishu.cli）
    try:
        fixed = []
        if not dry and materialize:
            for r in by_scope("table", materialize=True):
                if not r.fixable:
                    continue
                targets = [i for i in r.detect(ctx, dry=False) if i.fix]
                if not targets:
                    continue
                for msg in r.fix(ctx, targets):
                    fixed.append("[%s] %s" % (r.id, msg))
                ctx.reload()

        total = None
        for r in by_scope("table", materialize=materialize):
            rep = r.report(ctx, dry)
            if total is None:
                total = rep
            else:
                total.merge(rep)
        return (total or Report("校验")), fixed, ctx
    finally:
        feishu.set_read_only(prev)


def run_precheck(ctx, ops, force=False):
    """edit 写表前预检：返回 [(level, code, msg)]；有 ERR 且非 force 时应拒绝落表。

    先扫一遍本批 ops，把将新增的 struct/enum 名挂到 ctx.pending_*——
    判据与 sync 的 S08/S09 同源，但把「同批先定义后引用」视为合法。
    """
    for op in ops:
        if op.get("kind") == "add_struct":
            ctx.pending_structs.add(op.get("name") or "")
        elif op.get("kind") == "add_enum":
            ctx.pending_enums.add(op.get("name") or "")
    out = []
    for r in by_scope("precheck"):
        for op in ops:
            for iss in r.precheck(ctx, op):
                out.append(iss.row())
    return out


def precheck_blocked(rows):
    return any(level == ERR for level, _code, _msg in rows)


def snapshot_path():
    return conf.rel("config", "rule_snapshot.json")


def read_snapshot():
    try:
        with open(snapshot_path(), "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def write_snapshot(data):
    with open(snapshot_path(), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True)


# 注册顺序即输出顺序（语义排首位，保持 sync 现有标题与分组不变）
from . import legacy   # noqa: E402,F401
from . import basic    # noqa: E402,F401
from . import drift    # noqa: E402,F401
from . import precheck as _precheck  # noqa: E402,F401

from .basic import emit_fix      # noqa: E402,F401
from .drift import freeze        # noqa: E402,F401
