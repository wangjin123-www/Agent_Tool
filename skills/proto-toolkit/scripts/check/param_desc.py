# -*- coding: utf-8 -*-
"""SI 参数描述（P 列）值域内联检查。

规则：参数值域必须放 Parameter Enum；SI P 列只放中文描述，并链到 PE 枚举首行。
若 P 列文本里出现「0=… 1=…」「0x00:… 0x01:…」这类内联值域：
  - 没有链接 → WARN S16（应改用枚举）
  - 已有链接 → WARN S16（值域已进枚举，P 列可只留描述）
只报不改；脚本无法推断该建哪个枚举。
"""
import re

from ..common import feishu
from ..common.log import Report, OK

# 0= / 1= / 0x00: / 0： 等，至少两处才判定为内联值域
_INLINE = re.compile(r"(?:^|[，,；;/\s])(?:0x)?[0-9A-Fa-f]{1,4}\s*[=:：]")


def has_inline_values(text):
    if not text:
        return False
    return len(_INLINE.findall(text)) >= 2


def validate(cfg, si_rows):
    rep = Report("参数描述值域检查")
    bad = 0
    for r in range(2, len(si_rows) + 1):
        cell = feishu.cell_at(si_rows, r, "P")
        text = feishu.cell_text(cell)
        if not has_inline_values(text):
            continue
        bad += 1
        has_link = bool(feishu.cell_link(cell))
        if has_link:
            rep.warn("S16", "SI!P%d 含内联值域但已有枚举链接，建议 P 只留描述：%s"
                     % (r, text[:60]))
        else:
            rep.warn("S16", "SI!P%d 含内联值域且无枚举链接，应改用 Parameter Enum：%s"
                     % (r, text[:60]))
    if not bad:
        rep.ok("S16", "P 列未发现内联值域")
    return rep
