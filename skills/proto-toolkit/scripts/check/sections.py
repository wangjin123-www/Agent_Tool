# -*- coding: utf-8 -*-
"""分节行完整性校验（AI 修订规则 29）：

每个服务块内必须有且仅有两条方向分节行，先「▶ SOC → MCU · 下发/请求」
后「▶ MCU → SOC · 上报/应答」，文案一字不得改写；分节行只填 E 列。
块范围 = 本服务首行（含）到下一服务首行前一行为止（末块到末数据行）。

注意：分节行只是排版分组（表格好看），方向语义真源 = msg_id bit15
（见 check/semantics.py 的 S03），本规则不再判方向归属。
"""
from ..common import feishu
from ..common.log import Report


def _last_data_row(rows):
    last = 0
    for i, line in enumerate(rows, 1):
        if any(feishu.cell_text(c) for c in line):
            last = i
    return last


def validate(cfg, si_rows, proto):
    rep = Report("分节行校验")
    sec = cfg["section"]
    last_row = _last_data_row(si_rows)

    spans = []
    for i, s in enumerate(proto.services):
        begin = s.si_row
        end = (proto.services[i + 1].si_row - 1) if i + 1 < len(proto.services) else last_row
        spans.append((s, begin, end))

    for s, begin, end in spans:
        found = []
        for r in range(begin, end + 1):
            e = feishu.cell_text(feishu.cell_at(si_rows, r, "E"))
            if e.startswith(sec["marker"]):
                found.append((r, e))
        label = s.name or ("行%d 起的块" % begin)
        if len(found) != 2:
            rep.err("SEC", "%s 块内分节行 %d 条（应 2 条）：%s"
                    % (label, len(found), "; ".join(t for _, t in found) or "无"))
            continue
        (r1, t1), (r2, t2) = found
        if t1 != sec["soc_to_mcu"]:
            rep.err("SEC", "%s 第 1 条分节行文案不符：%r" % (label, t1))
        if t2 != sec["mcu_to_soc"]:
            rep.err("SEC", "%s 第 2 条分节行文案不符：%r" % (label, t2))
        # 分节行只填 E 列（A~D 为服务块纵向合并覆盖，属正常，不查）
        for r, t in found:
            dirty = [c for c in "FGHIJKLMNOPQ"
                     if feishu.cell_text(feishu.cell_at(si_rows, r, c))]
            if dirty:
                rep.warn("SEC", "%s 行%d 分节行在 %s 列有多余内容" % (label, r, ",".join(dirty)))
        # 方向归属不再在此判（与 parse 同源、永不失败）：真源 bit15 的排版
        # 一致性由语义层 S03 统一报告，本规则只管分节行自身的表格规范
        n_if = len(s.interfaces)
        rep.ok("SEC", "%s：分节行 @%d/@%d，接口 %d 条" % (label, r1, r2, n_if))
        if n_if == 0:
            rep.info("SEC", "%s 为空服务块（占位）" % label)
    return rep
