# -*- coding: utf-8 -*-
"""分节行禁用检查（规则 27 已废弃）。

2026-11-03 起协议表不再有「▶ SOC → MCU」/「▶ MCU → SOC」分节行：
- 方向真源 = msg_id bit15（0x8000=MCU→SOC，0=SOC→MCU）。
- 服务块边界 = 服务首行 ~ 下一服务首行前一行。
本检查只做防回归：E 列一旦再出现 '▶' 开头的分节行即报错。
"""
from ..common import feishu
from ..common.log import Report


def validate(cfg, si_rows, proto):
    rep = Report("分节行禁用检查")
    found = []
    for r in range(2, len(si_rows) + 1):
        e = feishu.cell_text(feishu.cell_at(si_rows, r, "E"))
        if e.startswith("▶"):
            found.append((r, e))
    if found:
        for r, t in found:
            rep.err("SEC", "第%d行发现已废弃分节行：%r" % (r, t))
    else:
        rep.ok("SEC", "无分节行（方向真源=msg_id bit15）")
    return rep
