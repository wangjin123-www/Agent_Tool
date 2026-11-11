# -*- coding: utf-8 -*-
"""服务块合并校验：Service Interface 的 A~D 列必须整块纵向合并（首行带值，其余行并入）。

块边界 = A 列有值行（服务首行）起到下一服务首行前一行（末块到最后内容行）。
插/删行不会自动扩展已有合并区，故每次写表后都要按块重算，否则界面每行重复显示
服务名/服务 id/描述/命名空间，看起来像「48 行起又是 power」。
"""
from ..common import conf, feishu
from ..common.log import Report

COLS = "ABCD"
DEFAULT_START = 6                # 数据首行（配置缺失时的兜底，真值取 si_data_start_row）


def _rows(cfg):
    return feishu.read(cfg, "service_interface", "Q")


def blocks(rows, first=DEFAULT_START):
    """[(服务名, 首行, 末行)]；末块取最后有内容的行（E 接口名 / Q 方向任一有值）。"""
    heads = []
    for i in range(first, len(rows) + 1):
        t = feishu.cell_text(feishu.cell_at(rows, i, "A"))
        if t:
            heads.append((i, t))
    last = max((i for i in range(1, len(rows) + 1)
                if any(feishu.cell_text(feishu.cell_at(rows, i, c))
                       for c in "EFGHIJKLMNOPQ")), default=0)
    out = []
    for k, (r, name) in enumerate(heads):
        end = heads[k + 1][0] - 1 if k + 1 < len(heads) else last
        if end >= r:
            out.append((name, r, end))
    return out


def merged(cfg):
    d = feishu.cli(["sheets", "+sheet-info",
                    "--spreadsheet-token", cfg["spreadsheet_token"],
                    "--sheet-id", cfg["sheets"]["service_interface"]["id"]])
    return [m["range"] for m in d["data"]["merged_cells"]]


def _expect(first, last):
    return ["%s%d:%s%d" % (c, first, c, last) for c in COLS]


def validate(dry=False, rows=None, sink=None):
    """校验服务块 A~D 合并；非 dry 时按块重做（先 unmerge 整块再逐列 merge）。

    sink 非空时只把修复意图塞进去（由 rules.apply_fix 统一写表），checker 不自己写。
    """
    cfg = conf.proto()
    rep = Report("服务块合并（SI A~D）")
    blk = blocks(rows if rows else _rows(cfg), cfg.get("si_data_start_row", DEFAULT_START))
    have = set(merged(cfg))
    bad = [(name, first, last, [r for r in _expect(first, last) if r not in have])
           for name, first, last in blk]
    bad = [b for b in bad if b[3]]
    if not bad:
        rep.ok("MERGE", "SI %d 个服务块的 A~D 纵向合并全部正确" % len(blk))
        return rep

    for name, first, last, miss in bad:
        if dry:
            rep.err("MERGE", "%s 行%d-%d 合并不全（缺 %s）" % (name, first, last, ",".join(miss)))
            continue
        _emit(sink, first, last)
        if sink is None:
            print("  → 已重做合并 %s 行%d-%d（A~D）" % (name, first, last))

    if dry:
        rep.warn("MERGE", "--dry-run：未修合并")
        return rep

    if sink is not None:
        rep.ok("MERGE", "已提交 %d 个服务块的 A~D 合并重做" % len(bad))
        return rep

    left = [r for name, first, last, _m in bad for r in _expect(first, last)
            if r not in set(merged(cfg))]
    if left:
        rep.err("MERGE", "重做后仍有未合并：%s" % ",".join(left[:6]))
    else:
        rep.ok("MERGE", "已重做 %d 个服务块的 A~D 合并" % len(bad))
    return rep


def _emit(sink, first, last):
    """写表只走一条路：有 sink 就交给调用方统一执行，自身不再触碰 feishu 写接口。"""
    if sink is not None:
        sink.setdefault("merges", []).append(
            ("service_interface", "A%d:D%d" % (first, last), _expect(first, last)))
        return
    cfg = conf.proto()
    feishu.unmerge(cfg, "service_interface", "A%d:D%d" % (first, last))
    feishu.merge(cfg, "service_interface", _expect(first, last))
