#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""原理图 PDF 文本层分析工具 —— embedded-data-analysis(嵌入式数据分析) · schematic 模块

只处理"从 EDA 导出的带文本层 PDF 原理图"(OrCAD/Altium/KiCad 导出的 PDF 均可):
  位号(R14/U1)、网络标号(CAN_STB/BAT+)、器件值(厚膜电阻,...) 都在 PDF 文本层里,
  本脚本把它们抓出来做检索/清点/BOM; **不含连线连通性**(PDF 里导线是矢量线段,
  端点与引脚的几何归属属图形识别, 本模块不实现 —— 要精确网络表请用 EDA 源文件
  走 native 侧 universal-netlist)。

基于 PyMuPDF(本机已装 1.28.x)。确定性提取全在本脚本, AI 只做解释。
用法: python sch_pdf_tools.py <子命令> <pdf> [选项]

子命令:
  info   <pdf>                     总览: 每页器件/网络/值文本统计, 无文本层(扫描图)告警
  comps  <pdf> [--page N] [--type R|U|C] [--ref R14] [--out csv]
                                  位号清单(含启发式就近关联的器件值)
  nets   <pdf> [--match PAT] [--page N]
                                  网络标号清单(信号名/电源名), 跨页聚合去重
  find   <pdf> <关键字> [--all]   定位任意文本: 页码+坐标(找"这条网络在哪页")
  bom    <pdf> [--out csv]        按器件值聚合的简易 BOM(值/数量/位号)
  scan   [--dir DIR]              扫描目录找原理图 PDF(按修改时间倒序)
"""
import argparse
import csv
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

# Windows 管道下 stdout 可能是 cp936, 强制 UTF-8 防打印中文炸编码(与 dbc_tools 同款)
for _s in (sys.stdout, sys.stderr):
    if _s.encoding and _s.encoding.lower().replace('-', '') != 'utf8':
        try:
            _s.reconfigure(encoding='utf-8', errors='replace')
        except Exception:
            pass

try:
    import pymupdf  # 1.28 起 import fitz 已弃用
except ImportError:
    print("缺少 pymupdf 库。安装: python -m pip install pymupdf\n"
          "国内网慢: python -m pip install pymupdf -i https://pypi.tuna.tsinghua.edu.cn/simple")
    sys.exit(3)

# 模块自定位约定(scripts/<分类>/ 恰三层到模块根), 本脚本暂不依赖模块内相对资源, 留作规范锚点
MODULE_ROOT = Path(__file__).resolve().parent.parent.parent

# ---------------------------------------------------------------- 提取规则
# 位号: 字母前缀 + 数字 (R14/C19/RP8/CP120/Q2/TP9/COC1/A-27PIN 之外)
REFDES_RE = re.compile(r'^[A-Z]{1,4}\d{1,4}[A-Z]?$')
# 网络标号: 含 _ / + / - 等分隔符, 或常见电源名; 排除位号/纯字母坐标区/纯数字/含中文
POWER_NAMES = {'GND', 'AGND', 'DGND', 'PGND', 'VCC', 'VDD', 'VEE', 'VSS', 'VBAT', 'BAT+', 'B+', '5V', '3V3', '1V8'}
NET_RE = re.compile(r'^[A-Za-z][A-Za-z0-9]+(?:[_/+\-.][A-Za-z0-9]+)+$|^[A-Z][A-Z0-9]*[+\-]$')
ZONE_JUNK = re.compile(r'^[A-Z]?\d{0,2}$')  # 图框分区号 "D" "1" "8" "D1" 等
CJK_RE = re.compile(r'[\u4e00-\u9fff]')
# 器件值文本: 含中文(国产库值行是"厚膜电阻,1/16W,390kohm,±1%,0402,SMD"), 或数值+单位
VALUE_RE = re.compile(
    r'\d\s*(?:ohm|Ω|uF|µF|nF|pF|mH|uH|µH|kHz|MHz|V\b|mA|A\b|W\b)|[±%]', re.IGNORECASE)

MIN_TEXT_CHARS = 200  # 低于此判定该页基本无文本层(可能是扫描图)

PDF_EXTS = ('.pdf',)


def has_cjk(s: str) -> bool:
    return bool(CJK_RE.search(s))


def is_value_text(s: str) -> bool:
    # 中文值行(国产库)形如 "厚膜电阻,1/16W,390kohm,±1%,0402,SMD": 有 ASCII 数字+半角逗号;
    # 图纸上的中文注释("此处静态电流I"/布局说明)通常无数字或用全角逗号, 据此排除
    if has_cjk(s):
        return bool(re.search(r'\d', s) and ',' in s)
    if ',' in s and VALUE_RE.search(s):
        return True
    if re.fullmatch(r'\d+(?:\.\d+)?(?:k|m|u|µ|n|p)?(?:F|H|Ω|ohm|R|V)', s, re.IGNORECASE):
        return True
    return False


def load_pages(pdf_path: str):
    """返回 [(page_no, [word...])], word = (x0,y0,x1,y1,text,block,line,wordno)

    保留 block/line/wordno 三元组是为了恢复 PDF 写入时的文本块顺序(阅读顺序),
    OrCAD 导出 PDF 里"位号 -> 值"在块顺序上严格相邻, 是值关联的主依据。
    """
    p = Path(pdf_path)
    if not p.is_file():
        print(f"[错误] 文件不存在: {p}")
        sys.exit(2)
    doc = pymupdf.open(str(p))
    pages = []
    for i, page in enumerate(doc, start=1):
        words = [tuple(w[:8]) for w in page.get_text('words')]
        pages.append((i, words))
    doc.close()
    return p.name, pages


def classify(words):
    """一页内的词分三类: refdes / nets / values

    refdes/nets 按文本去重(同页同名出现两次算一个);
    值文本【不去重】——同值器件在一页出现 N 次, 就有 N 个独立属性块。
    """
    refdes, nets, values = [], [], []
    seen_r, seen_n = set(), set()
    for w in words:
        t = w[4].strip()
        if not t:
            continue
        if REFDES_RE.match(t):
            if t not in seen_r:
                refdes.append(w); seen_r.add(t)
        elif is_value_text(t):
            values.append(w)
        elif (NET_RE.match(t) and not ZONE_JUNK.match(t) and not has_cjk(t)
              and not REFDES_RE.match(t) and 3 <= len(t) <= 40 and t.count('/') <= 2):
            if t not in seen_n:
                nets.append(w); seen_n.add(t)
    return refdes, nets, values


def associate(pages_words):
    """位号 -> 值 关联: 按 PDF 文本块顺序(EDA 写出顺序)配对

    实测 OrCAD 层次图导出 PDF: 符号属性块内"位号"后紧跟"值文本", 几何上却可能
    相距 50~70pt 且与邻居交叉 —— 几何就近关联不可靠, 阅读顺序配对才可靠。
    规则: 顺序扫描, 记住最近一个位号; 遇到值文本挂给该位号并清空, 下个值等下个位号。
    """
    confirmed = {}
    for pno, words in pages_words:
        ordered = sorted(words, key=lambda w: (w[5], w[6], w[7]))
        cur = None
        for w in ordered:
            t = w[4].strip()
            if not t:
                continue
            if REFDES_RE.match(t):
                cur = t
                confirmed.setdefault((pno, t), '')
            elif is_value_text(t):
                if cur is not None and confirmed[(pno, cur)] == '':
                    confirmed[(pno, cur)] = t
                    cur = None
    return confirmed


# ---------------------------------------------------------------- 子命令
def cmd_info(a):
    name, pages = load_pages(a.pdf)
    print(f"文件: {a.pdf}")
    print(f"页数: {len(pages)}")
    print(f"{'页':>4} {'字符':>6} {'位号':>5} {'网络':>5} {'值文本':>6}")
    tot_r = tot_n = tot_v = low_pages = 0
    assoc = associate(pages)
    for pno, words in pages:
        refdes, nets, values = classify(words)
        nchars = sum(len(w[4]) for w in words)
        if nchars < MIN_TEXT_CHARS:
            low_pages += 1
        tot_r += len(refdes); tot_n += len(nets); tot_v += len(values)
        print(f"{pno:>4} {nchars:>6} {len(refdes):>5} {len(nets):>5} {len(values):>6}")
    print(f"合计: 位号 {tot_r}, 网络标号 {tot_n}(跨页未去重), 值文本 {tot_v}, 关联到值的位号 {sum(1 for v in assoc.values() if v)}")
    if low_pages:
        print(f"[警告] {low_pages} 页文本量极低 —— 可能是扫描图/图片型 PDF, 本工具不适用(文本层提取前提)")
    if tot_r == 0 and tot_n == 0:
        print("[警告] 全文未提取到位号与网络标号, 请确认这是 EDA 导出的文本型 PDF")


def cmd_comps(a):
    name, pages = load_pages(a.pdf)
    assoc = associate(pages)
    rows = []
    for pno, words in pages:
        if a.page and pno != a.page:
            continue
        refdes, _, _ = classify(words)
        for r in sorted(refdes, key=lambda w: w[4]):
            ref = r[4]
            prefix = re.match(r'^[A-Z]+', ref).group(0)
            if a.type and prefix != a.type.upper():
                continue
            if a.ref and a.ref.upper() not in ref:
                continue
            rows.append((pno, ref, assoc.get((pno, ref), '')))
    if not rows:
        print("无匹配位号")
        return
    width = max(len(r[2]) for r in rows)
    width = min(width, 60)
    print(f"{'页':>3} {'位号':<8} 值(阅读顺序关联, 启发式)")
    for pno, ref, val in rows:
        val = val if len(val) <= width else val[:width - 1] + '…'
        print(f"{pno:>3} {ref:<8} {val}")
    print(f"共 {len(rows)} 个位号")
    if a.out:
        _write_csv(a.out, ['page', 'refdes', 'value'], rows)
        print(f"已导出: {a.out}")


def cmd_nets(a):
    name, pages = load_pages(a.pdf)
    agg = defaultdict(set)   # net -> {pages}
    coords = defaultdict(list)
    for pno, words in pages:
        if a.page and pno != a.page:
            continue
        _, nets, _ = classify(words)
        for w in nets:
            if a.match and a.match.lower() not in w[4].lower():
                continue
            agg[w[4]].add(pno)
            coords[w[4]].append(f"p{pno}({w[0]:.0f},{w[1]:.0f})")
    if not agg:
        print("无匹配网络标号")
        return
    print(f"{'网络标号':<32} 页")
    for net in sorted(agg, key=lambda n: (-len(coords[n]), n)):
        pages_str = ','.join(str(p) for p in sorted(agg[net]))
        pos = coords[net]
        extra = f"  x{len(pos)}" if len(pos) > 1 else ""
        print(f"{net:<32} {pages_str}{extra}")
    print(f"共 {len(agg)} 个网络标号(同名跨页已聚合; 含同名多处出现, 也可能含误报的普通文字)")


def cmd_find(a):
    name, pages = load_pages(a.pdf)
    kw = a.keyword.lower()
    hits = 0
    for pno, words in pages:
        for w in words:
            if kw in w[4].lower():
                print(f"p{pno:>3} ({w[0]:7.1f},{w[1]:7.1f})  {w[4]}")
                hits += 1
                if not a.all and hits >= 60:
                    print("…(截断, 加 --all 看全部)")
                    return
    if hits == 0:
        print(f"未找到: {a.keyword}")
    else:
        print(f"共 {hits} 处")


def cmd_bom(a):
    name, pages = load_pages(a.pdf)
    assoc = associate(pages)
    groups = defaultdict(list)
    no_value = []
    for (pno, ref), vtext in assoc.items():
        if vtext:
            groups[vtext].append(ref)
        else:
            no_value.append(ref)
    if not groups:
        print("未能聚合出 BOM(检查文本层/值文本规则)")
        return
    rows = []
    for vtext, refs in sorted(groups.items(), key=lambda kv: -len(kv[1])):
        refs_n = sorted(refs, key=lambda r: (re.sub(r'\d+', '', r), int(re.search(r'\d+', r).group(0))))
        rows.append((vtext, len(refs), ' '.join(refs_n[:20]) + (' …' if len(refs_n) > 20 else '')))
    print(f"{'数量':>4}  值")
    for vtext, cnt, refs in rows:
        v = vtext if len(vtext) <= 58 else vtext[:57] + '…'
        print(f"{cnt:>4}  {v}")
        print(f"      {refs}")
    print(f"共 {len(rows)} 种值, {sum(r[1] for r in rows)} 个位号(值关联为启发式, 以 EDA 源文件为准)")
    print(f"另有 {len(no_value)} 个位号未关联到值(连接器/跨页链接标签等), 不计入上表")
    if a.out:
        _write_csv(a.out, ['value', 'count', 'refdes'], [(r[0], r[1], r[2]) for r in rows])
        print(f"已导出: {a.out}")


def cmd_scan(a):
    root = Path(a.dir or '.')
    out = []
    for dirpath, _, files in os.walk(root):
        for f in files:
            if f.lower().endswith(PDF_EXTS):
                p = Path(dirpath) / f
                out.append((p.stat().st_mtime, p))
    out.sort(reverse=True)
    if not out:
        print(f"未找到 PDF: {root}")
        return
    for mt, p in out[:30]:
        import time
        print(f"{time.strftime('%Y-%m-%d %H:%M', time.localtime(mt))}  {p}")
    print(f"共 {len(out)} 个(显示前 30, 原理图与否需 info 判别)")


def _write_csv(path, header, rows):
    with open(path, 'w', newline='', encoding='utf-8-sig') as f:
        csv.writer(f).writerows([header] + [list(r) for r in rows])


def main():
    ap = argparse.ArgumentParser(description='原理图 PDF 文本层分析(位号/网络标号/值/BOM; 不含连线连通性)')
    sub = ap.add_subparsers(dest='cmd', required=True)

    p = sub.add_parser('info', help='总览')
    p.add_argument('pdf'); p.set_defaults(fn=cmd_info)

    p = sub.add_parser('comps', help='位号清单(含就近值)')
    p.add_argument('pdf')
    p.add_argument('--page', type=int)
    p.add_argument('--type', help='前缀过滤: R/C/U/Q...')
    p.add_argument('--ref', help='位号子串过滤')
    p.add_argument('--out', help='导出 csv(utf-8 BOM)')
    p.set_defaults(fn=cmd_comps)

    p = sub.add_parser('nets', help='网络标号清单')
    p.add_argument('pdf')
    p.add_argument('--match', help='子串过滤(不分大小写)')
    p.add_argument('--page', type=int)
    p.set_defaults(fn=cmd_nets)

    p = sub.add_parser('find', help='定位任意文本')
    p.add_argument('pdf'); p.add_argument('keyword')
    p.add_argument('--all', action='store_true', help='不限 60 条')
    p.set_defaults(fn=cmd_find)

    p = sub.add_parser('bom', help='按值聚合 BOM')
    p.add_argument('pdf'); p.add_argument('--out', help='导出 csv')
    p.set_defaults(fn=cmd_bom)

    p = sub.add_parser('scan', help='扫描目录找 PDF')
    p.add_argument('--dir'); p.set_defaults(fn=cmd_scan)

    a = ap.parse_args()
    a.fn(a)


if __name__ == '__main__':
    main()
