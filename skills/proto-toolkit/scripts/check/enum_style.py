# -*- coding: utf-8 -*-
"""Parameter Enum 枚举块样式/边框校验与修复。

标准（对齐 OTA_UPGRADE_STS 既有块）：
  A 列：10pt / 加粗 / 左对齐 / 文本格式 / 垂直居中 / 四周细边框
  B 列：10pt / 居中 / 文本格式 / 垂直居中 / 四周细边框
  C、D：10pt / 左对齐 / 文本格式 / 垂直居中 / 四周细边框
  E 列：10pt / 居中 / 文本格式 / 垂直居中 / 四周细边框

add_enum 只写值 + 合并 A 列，不带样式；sync 在这里补边框，保证新枚举块
和既有块视觉一致。
"""
from ..common import feishu
from ..common.log import Report, OK

BORDER = {"style": "solid", "weight": "thin", "color": "#1F2329"}


def _block_styles(start, end):
    return [
        {"range": "A%d:A%d" % (start, end), "font_size": 10, "font_weight": "bold",
         "horizontal_alignment": "left", "number_format": "@",
         "vertical_alignment": "middle", "border": BORDER},
        {"range": "B%d:B%d" % (start, end), "font_size": 10,
         "horizontal_alignment": "center", "number_format": "@",
         "vertical_alignment": "middle", "border": BORDER},
        {"range": "C%d:C%d" % (start, end), "font_size": 10,
         "horizontal_alignment": "left", "number_format": "@",
         "vertical_alignment": "middle", "border": BORDER},
        {"range": "D%d:D%d" % (start, end), "font_size": 10,
         "horizontal_alignment": "left", "number_format": "@",
         "vertical_alignment": "middle", "border": BORDER},
        {"range": "E%d:E%d" % (start, end), "font_size": 10,
         "horizontal_alignment": "center", "number_format": "@",
         "vertical_alignment": "middle", "border": BORDER},
    ]


def _block_end(proto, idx):
    en = proto.enums[idx]
    if idx + 1 < len(proto.enums):
        return proto.enums[idx + 1].pe_row - 1
    return en.pe_row + max(len(en.items), 1) - 1


def _has_standard_style(row):
    """首行 A~E 是否都有边框 + 标准对齐/加粗。"""
    if len(row) < 5:
        return False
    want = [("left", True), ("center", False), ("left", False),
            ("left", False), ("center", False)]
    for i, (align, bold) in enumerate(want):
        c = row[i] if isinstance(row[i], dict) else {}
        if not c.get("border_styles"):
            return False
        st = c.get("cell_styles") or {}
        if st.get("horizontal_alignment") != align:
            return False
        if bold and st.get("font_weight") != "bold":
            return False
    return True


def validate(cfg, proto, repair=False, sink=None):
    rep = Report("枚举块样式（%s）" % ("不一致即补边框" if repair else "只读"))
    if not proto.enums:
        rep.info("STY", "无枚举块")
        return rep

    last = max(_block_end(proto, i) for i in range(len(proto.enums)))
    rows = feishu.read_range(cfg, "parameter_enum", "A1:E%d" % last, include="value,style")

    bad = []
    for i, en in enumerate(proto.enums):
        start = en.pe_row
        end = _block_end(proto, i)
        row = rows[start - 1] if start - 1 < len(rows) else []
        if not _has_standard_style(row):
            bad.append((en.name, start, end))

    if not bad:
        rep.ok("STY", "全部枚举块边框/样式一致")
        return rep

    for name, start, end in bad:
        if repair:
            _emit(cfg, sink, start, end)
            rep.warn("STY", "%s（A%d:E%d）缺边框/样式 → 已补齐" % (name, start, end))
        else:
            rep.err("STY", "%s（A%d:E%d）缺边框/样式" % (name, start, end))
    return rep


def _emit(cfg, sink, start, end):
    """写表只走一条路：有 sink 就交给调用方统一执行，没有才自己写。"""
    styles = _block_styles(start, end)
    if sink is not None:
        sink.setdefault("styles", []).append(("parameter_enum", styles))
    else:
        feishu.apply_styles(cfg, "parameter_enum", styles)
