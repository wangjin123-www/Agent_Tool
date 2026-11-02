#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""链接 map 文件分析工具 —— embedded-omni(嵌入式全能) · mapfile 模块

基于 GitHub 开源库 mapfile-parser(Decompals/mapfile-parser, MIT, Rust 后端,
支持 GNU ld / clang lld / Metrowerks ld 三种 map 格式, 自动识别), pip 直装。
在它之上做嵌入式常用的查询: 存储区占用/符号定位/谁吃了 Flash/两版 map 对比。

本模块【不按芯片分类】: map 格式由工具链决定(与芯片无关), 存储区语义由 map
内嵌的 Memory Configuration 给出(region 名/origin/length 都在文件里), 无需芯片库。
首个实测: S32K312 + S32DS ARM GCC 10.2 (GNU ld map)。

确定性解析全在库+本脚本, AI 只做解释。
用法: python map_tools.py <子命令> <map> [选项]

子命令:
  info    <map>                     总览: 工具链/存储区(MEMORY)/段(segment)布局
  regions <map>                     存储区表: region/origin/length/已用/剩余
  symbols <map> --match PAT [--exact NAME]
                                  符号查询: 地址/大小/段/所在 .o(排查"这个变量在哪")
  largest <map> [--top N] [--ram]  最大的输入节(哪块代码最吃 Flash/RAM)
  objects <map> [--top N] [--match PAT]
                                  按 .o 文件聚合大小(哪个模块最占)
  diff    <mapA> <mapB> [--top N]  两版 map 对比: 新增/删除/变大/变小 TopN
  scan    [--dir DIR]              扫描目录找 .map(按修改时间倒序)
"""
import argparse
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

# Windows 管道下 stdout 可能是 cp936, 强制 UTF-8(与 dbc_tools 同款)
for _s in (sys.stdout, sys.stderr):
    if _s.encoding and _s.encoding.lower().replace('-', '') != 'utf8':
        try:
            _s.reconfigure(encoding='utf-8', errors='replace')
        except Exception:
            pass

MODULE_ROOT = Path(__file__).resolve().parent.parent.parent

try:
    from mapfile_parser import MapFile
except ImportError:
    print("缺少 mapfile-parser 库(GitHub: Decompals/mapfile-parser)。安装:\n"
          "  python -m pip install mapfile-parser\n"
          "国内网慢: python -m pip install mapfile-parser -i https://pypi.tuna.tsinghua.edu.cn/simple")
    sys.exit(3)

# 非镜像内容的节/段, 统计大小时跳过
NOIMAGE_RE = re.compile(r'^\.(ARM\.attributes|comment|debug_.*|gnu\..*|stack|untitled)', re.I)
# RAM 侧特征(粗略): .bss/.data/非 flash 地址由 regions 判断更准, 这里只给 --ram 快捷过滤
RAM_SECTION_RE = re.compile(r'^\.(bss|data|noinit|sbss|sdata)', re.I)


def load(map_path: str):
    p = Path(map_path)
    if not p.is_file():
        print(f"[错误] 文件不存在: {p}")
        sys.exit(2)
    m = MapFile()
    try:
        m.readMapFile(str(p))
    except Exception as e:
        print(f"[错误] map 解析失败: {p}\n{type(e).__name__}: {e}")
        sys.exit(2)
    raw = p.read_text(encoding='utf-8', errors='replace')
    return p, m, raw


def parse_memory_config(raw: str):
    """GNU ld map 的 Memory Configuration 表 -> [(name, origin, length)]"""
    mc = re.search(r'Memory Configuration(.*?)(?:Linker script and memory map|Linker script|$)', raw, re.S)
    if not mc:
        return []
    out = []
    for line in mc.group(1).splitlines():
        mm = re.match(r'^(\S+)\s+(0x[0-9a-fA-F]+)\s+(0x[0-9a-fA-F]+)', line.strip())
        if mm and mm.group(1) != 'Name':
            out.append((mm.group(1), int(mm.group(2), 16), int(mm.group(3), 16)))
    return out


def detect_toolchain(raw: str) -> str:
    if 'Archive member included to satisfy reference' in raw and 'Linker script and memory map' in raw:
        return 'GNU ld (GCC/binutils)'
    if 'IAR Linker' in raw or 'MODULES' in raw and '*** IAR' in raw:
        return 'IAR ilinkarm (mapfile-parser 不支持, 本工具不可用)'
    if 'ARM Linker' in raw or 'armlink' in raw:
        return 'ARM armlink/armclang (mapfile-parser 不支持, 本工具不可用)'
    if 'clang' in raw.lower() or 'lld' in raw.lower():
        return 'clang lld (可能支持)'
    return '未知(可能不支持)'


def fmt_sz(n) -> str:
    n = n or 0
    if n >= 1024:
        return f"{n} ({n/1024:.1f}K)"
    return str(n)


def region_of(regions, addr):
    for name, origin, length in regions:
        if origin <= addr < origin + length:
            return name
    return '?'


def iter_sections(m):
    """(segment, section) 生成器"""
    for seg in m:
        for sec in seg:
            yield seg, sec


def obj_label(sec) -> str:
    fp = str(sec.filepath or '')
    fp = fp.replace('\\', '/')
    fp = re.sub(r'^\./', '', fp)
    return fp


# ---------------------------------------------------------------- 子命令
def cmd_info(a):
    p, m, raw = load(a.map)
    print(f"文件: {p}")
    print(f"工具链: {detect_toolchain(raw)}")
    regions = parse_memory_config(raw)
    if regions:
        print(f"\n存储区(Memory Configuration, {len(regions)} 个):")
        for name, origin, length in regions:
            print(f"  {name:<16} origin=0x{origin:08X}  length=0x{length:X} ({length//1024}K)")
    print(f"\n段(segment, {len(m)} 个, 只列非零):")
    tot_syms = 0
    for seg in m:
        nsecs = len(seg)
        nsyms = sum(len(list(sec)) for _, sec in [(seg, s) for s in seg])
        tot_syms += nsyms
        if seg.size:
            print(f"  {seg.name:<16} 0x{(seg.vram or 0):08X}..0x{(seg.vram or 0)+(seg.size or 0):08X} "
                  f"size={fmt_sz(seg.size)}  sections={nsecs}")
    print(f"\n符号总数: {tot_syms}")
    print("提示: regions 看占用率, largest 看谁最吃 Flash, symbols 查符号位置")


def cmd_regions(a):
    p, m, raw = load(a.map)
    regions = parse_memory_config(raw)
    if not regions:
        print("[提示] 未找到 Memory Configuration(非 GNU ld map?), 改看 info 的 segment 布局")
        return
    # 用输入节大小(排除非镜像节/fill)累加到所在 region
    used = defaultdict(int)
    for seg, sec in iter_sections(m):
        if sec.isFill or NOIMAGE_RE.match(str(sec.sectionType or '')):
            continue
        used[region_of(regions, sec.vram or 0)] += sec.size or 0
    print(f"{'region':<16} {'origin':>10} {'length':>9} {'已用':>12} {'剩余':>12}  使用率")
    for name, origin, length in regions:
        u = used.get(name, 0)
        pct = u / length * 100 if length else 0
        bar = '#' * int(pct / 5) + '-' * (20 - int(pct / 5))
        print(f"{name:<16} 0x{origin:08X} 0x{length:>7X} {fmt_sz(u):>12} {fmt_sz(length-u):>12}  {pct:5.1f}% [{bar}]")
    print("[说明] 已用=输入节累加(排除 fill/调试节), 与链接器汇报可能有对齐差额")


def cmd_symbols(a):
    p, m, raw = load(a.map)
    hits = []
    for seg, sec in iter_sections(m):
        for sym in sec:
            name = str(sym.name or '')
            if name.startswith('$_static_symbol'):
                continue
            if a.exact:
                if name == a.exact:
                    hits.append((seg, sec, sym))
            elif a.match and a.match.lower() in name.lower():
                hits.append((seg, sec, sym))
    if not hits:
        where = f"--exact {a.exact}" if a.exact else f"--match {a.match}"
        print(f"未找到符号: {where}")
        sys.exit(1)
    print(f"{'地址':>10} {'大小':>6}  {'段':<12} {'输入节':<18} 所在 .o")
    for seg, sec, sym in hits[:a.max or 40]:
        st = str(sec.sectionType or '')[:16]
        print(f"0x{(sym.vram or 0):08X} {fmt_sz(sym.size):>6}  {seg.name:<12} {st:<18} {obj_label(sec)}")
        print(f"           符号: {sym.name}")
    if len(hits) > (a.max or 40):
        print(f"…共 {len(hits)} 个, 用 --max 放宽")


def cmd_largest(a):
    p, m, raw = load(a.map)
    rows = []
    for seg, sec in iter_sections(m):
        if sec.isFill or NOIMAGE_RE.match(str(sec.sectionType or '')):
            continue
        if a.ram and not RAM_SECTION_RE.match(str(sec.sectionType or '')):
            continue
        rows.append((sec.size or 0, seg.name, str(sec.sectionType or ''), obj_label(sec)))
    rows.sort(reverse=True)
    if not rows:
        print("无匹配输入节")
        return
    n = a.top or 20
    print(f"{'大小':>12}  {'段':<10} {'输入节':<22} .o 文件")
    for size, segname, st, obj in rows[:n]:
        print(f"{fmt_sz(size):>12}  {segname:<10} {st:<22} {obj}")


def cmd_objects(a):
    p, m, raw = load(a.map)
    agg = defaultdict(int)
    for seg, sec in iter_sections(m):
        if sec.isFill or NOIMAGE_RE.match(str(sec.sectionType or '')):
            continue
        agg[obj_label(sec)] += sec.size or 0
    rows = [(v, k) for k, v in agg.items() if not a.match or a.match.lower() in k.lower()]
    rows.sort(reverse=True)
    if not rows:
        print("无匹配对象文件")
        return
    total = sum(v for v, _ in rows)
    n = a.top or 25
    print(f"{'大小':>12}  {'占比':>6}  .o 文件")
    for v, k in rows[:n]:
        pct = v / total * 100 if total else 0
        print(f"{fmt_sz(v):>12}  {pct:5.1f}%  {k}")
    print(f"共 {len(rows)} 个对象文件, 合计 {fmt_sz(total)}")


def cmd_diff(a):
    pa, ma, _ = load(a.mapA)
    pb, mb, _ = load(a.mapB)

    def index(m):
        d = {}
        for seg, sec in iter_sections(m):
            for sym in sec:
                name = str(sym.name or '')
                if name.startswith('$_static_symbol'):
                    continue
                key = (name, obj_label(sec))
                d[key] = (sym.vram or 0, sym.size or 0, seg.name)
        return d

    da, db = index(ma), index(mb)
    added = [(k, v) for k, v in db.items() if k not in da]
    removed = [(k, v) for k, v in da.items() if k not in db]
    grown, shrunk = [], []
    for k in da.keys() & db.keys():
        delta = db[k][1] - da[k][1]
        if delta > 0:
            grown.append((delta, k, da[k][1], db[k][1]))
        elif delta < 0:
            shrunk.append((delta, k, da[k][1], db[k][1]))
    grown.sort(reverse=True)
    shrunk.sort()
    n = a.top or 15
    print(f"A: {pa.name}  符号 {len(da)}")
    print(f"B: {a.mapB}  符号 {len(db)}")
    print(f"\n净变化: 新增 {len(added)} / 删除 {len(removed)} / 变大 {len(grown)} / 变小 {len(shrunk)}")
    delta_total = sum(v[1] for _, v in db.items()) - sum(v[1] for _, v in da.items())
    print(f"符号大小合计变化: {delta_total:+d} 字节(粗略, 含只增不减的对齐效应)")
    print(f"\n[变大 Top{n}]")
    for delta, k, sa, sb in grown[:n]:
        print(f"  {delta:+8d}  {sa}->{sb}  {k[0]}  ({k[1]})")
    print(f"\n[变小 Top{n}]")
    for delta, k, sa, sb in shrunk[:n]:
        print(f"  {delta:+8d}  {sa}->{sb}  {k[0]}  ({k[1]})")
    print(f"\n[新增 Top{n}(按大小)]")
    for k, v in sorted(added, key=lambda x: -x[1][1])[:n]:
        print(f"  {v[1]:8d}  0x{v[0]:08X}  {k[0]}  ({k[1]})")
    print(f"\n[删除 Top{n}(按原大小)]")
    for k, v in sorted(removed, key=lambda x: -x[1][1])[:n]:
        print(f"  {v[1]:8d}  {k[0]}  ({k[1]})")


def cmd_scan(a):
    root = Path(a.dir or '.')
    out = []
    for dirpath, _, files in os.walk(root):
        if 'node_modules' in dirpath:
            continue
        for f in files:
            if f.lower().endswith('.map'):
                q = Path(dirpath) / f
                out.append((q.stat().st_mtime, q))
    out.sort(reverse=True)
    if not out:
        print(f"未找到 .map: {root}")
        return
    import time
    for mt, q in out[:30]:
        print(f"{time.strftime('%Y-%m-%d %H:%M', time.localtime(mt))}  {q}")


def main():
    ap = argparse.ArgumentParser(description='链接 map 文件分析(基于 mapfile-parser; GNU ld/lld/Metrowerks)')
    sub = ap.add_subparsers(dest='cmd', required=True)

    p = sub.add_parser('info', help='总览: 工具链/存储区/段')
    p.add_argument('map'); p.set_defaults(fn=cmd_info)

    p = sub.add_parser('regions', help='存储区占用率')
    p.add_argument('map'); p.set_defaults(fn=cmd_regions)

    p = sub.add_parser('symbols', help='符号查询')
    p.add_argument('map')
    p.add_argument('--match', help='符号名子串(不分大小写)')
    p.add_argument('--exact', help='符号名精确匹配')
    p.add_argument('--max', type=int, help='最多显示条数(默认40)')
    p.set_defaults(fn=cmd_symbols)

    p = sub.add_parser('largest', help='最大的输入节')
    p.add_argument('map')
    p.add_argument('--top', type=int, help='默认20')
    p.add_argument('--ram', action='store_true', help='只看 RAM 侧节(.bss/.data等)')
    p.set_defaults(fn=cmd_largest)

    p = sub.add_parser('objects', help='按 .o 聚合大小')
    p.add_argument('map')
    p.add_argument('--top', type=int, help='默认25')
    p.add_argument('--match', help='路径子串过滤')
    p.set_defaults(fn=cmd_objects)

    p = sub.add_parser('diff', help='两版 map 对比')
    p.add_argument('mapA'); p.add_argument('mapB')
    p.add_argument('--top', type=int, help='默认15')
    p.set_defaults(fn=cmd_diff)

    p = sub.add_parser('scan', help='扫描目录找 .map')
    p.add_argument('--dir'); p.set_defaults(fn=cmd_scan)

    a = ap.parse_args()
    a.fn(a)


if __name__ == '__main__':
    main()
