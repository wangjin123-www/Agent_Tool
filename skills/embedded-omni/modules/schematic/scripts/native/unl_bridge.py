#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EDA 原理图源文件分析桥 —— embedded-omni(嵌入式全能) · schematic 模块

包装 GitHub 开源工具 universal-netlist(IntelligentElectron/universal-netlist,
Apache-2.0, v1.12.2): 直接读 Cadence OrCAD .DSN / Altium .PrjPcb(.SchDoc) /
KiCad .kicad_pro 等 EDA 源文件(无需装 EDA/无需 license), 用它的
`export-json` 命令转出统一网络表 JSON(schema v2), 本脚本再在其上做检索/追网。

确定性解析全在 universal-netlist + 本脚本, AI 只做解释。
用法: python unl_bridge.py <子命令> <设计文件> [选项]

子命令:
  info   <design>                     总览: 来源格式/器件数/网络数/前缀分布
  comps  <design> [--type U|R|C] [--ref U1] [--mpn PAT]
                                     器件清单: 位号/值/MPN/描述/DNS(不贴装)
  pins   <design> --ref U1           某器件引脚表: 引脚号/引脚名/所在网络
  nets   <design> [--match PAT] [--net NAME]
                                     网络清单; --net 给出成员(位号.引脚)
  xnet   <design> --net NAME [--skip C,L]
                                     扩展网络: 穿过串阻/串容/磁珠追到驱动与负载端
  export <design> [--out F]          导出 .netlist.json(可入库/diff 的网络表快照)

design = .DSN / .PrjPcb / .kicad_pro / .netlist.json 任意一种。
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# Windows 管道下 stdout 可能是 cp936, 强制 UTF-8(与 dbc_tools 同款)
for _s in (sys.stdout, sys.stderr):
    if _s.encoding and _s.encoding.lower().replace('-', '') != 'utf8':
        try:
            _s.reconfigure(encoding='utf-8', errors='replace')
        except Exception:
            pass

MODULE_ROOT = Path(__file__).resolve().parent.parent.parent

INSTALL_HINT = (
    "缺少 universal-netlist 命令。安装(任选其一):\n"
    "  npm install -g @intelligentelectron/universal-netlist   (需 Node 20+)\n"
    "  PowerShell 一键: irm https://raw.githubusercontent.com/IntelligentElectron/universal-netlist/main/install.ps1 | iex\n"
    "  npm 走不了外网时可用: npm config set registry https://registry.npmmirror.com 后再装\n"
    "装完确认: universal-netlist --version\n"
    "二进制不在 PATH 时可设环境变量 UNL_BIN 指向 universal-netlist(.exe)"
)

DESIGN_EXTS = ('.dsn', '.prjpcb', '.schdoc', '.kicad_pro', '.kicad_sch', '.netlist.json')

# 串行元件(2 脚): 追网时穿过它们
SERIES_PREFIX = ('R', 'RS', 'FR', 'C', 'L', 'FB', 'F')
# 电源/地网: 追网到此停止
POWER_NET_RE = re.compile(
    r'(?i)^(?:[A-Z0-9_]*GND|GND[A-Z0-9_]*|AGND|DGND|PGND|VCC|VDD|VEE|VSS|VBAT|'
    r'VSUP|VIN|VOUT|VBUS|[B+]\+?|\+?\d+(?:\.\d+)?V(?:[0-9]+)?|V[A-Z0-9]*_?\d*V?\d*)$')


def find_unl() -> str:
    exe = os.environ.get('UNL_BIN')
    cand = shutil.which('universal-netlist') if exe is None else shutil.which(exe) or (Path(exe).is_file() and exe)
    if not cand:
        print(INSTALL_HINT)
        sys.exit(3)
    return cand


def export_json(design: Path) -> Path:
    unl = find_unl()
    st = design.stat()
    key = hashlib.sha1(str(design.resolve()).encode('utf-8')).hexdigest()[:12]
    cache = Path(tempfile.gettempdir()) / 'unl_bridge_cache' / f'{key}.netlist.json'
    if cache.is_file() and cache.stat().st_mtime >= st.st_mtime:
        return cache
    cache.parent.mkdir(parents=True, exist_ok=True)
    r = subprocess.run([unl, 'export-json', str(design), str(cache)],
                       capture_output=True, text=True, shell=False)
    if r.returncode != 0 or not cache.is_file():
        print(f"[错误] universal-netlist 解析失败: {design}\n{r.stdout}\n{r.stderr}")
        sys.exit(2)
    return cache


def load_design(path: str):
    p = Path(path)
    if not p.is_file():
        print(f"[错误] 文件不存在: {p}")
        sys.exit(2)
    j = json.loads(export_json(p).read_text(encoding='utf-8'))
    return p, j


def pin_net(entry):
    """PinEntry: "NET" 或 {"name":..,"net":..}"""
    return entry['net'] if isinstance(entry, dict) else entry


def pin_name(entry, num):
    return entry.get('name', '') if isinstance(entry, dict) else ''


def refdes_prefix(ref: str) -> str:
    m = re.match(r'^[A-Z]+', ref)
    return m.group(0) if m else '?'


def pin_key(num: str):
    m = re.match(r'^(\d+)', num)
    return (int(m.group(1)) if m else 0, num)


def is_power(net: str) -> bool:
    return bool(POWER_NET_RE.match(net)) or net.upper() in ('GND', 'BAT+', 'B+', '3V3', '5V', '1V8')


# ---------------------------------------------------------------- 子命令
def cmd_info(a):
    p, j = load_design(a.design)
    src = j['metadata'].get('origin', {}).get('source', {})
    comps, nets = j['components'], j['nets']
    pref = {}
    for r in comps:
        pref[refdes_prefix(r)] = pref.get(refdes_prefix(r), 0) + 1
    top = ' '.join(f"{k}:{v}" for k, v in sorted(pref.items(), key=lambda kv: -kv[1])[:10])
    print(f"设计: {p}")
    print(f"来源: {src.get('vendor', '?')} {src.get('fileType', '')}  schema v{j.get('universalNetlistSchemaVersion')}")
    print(f"器件: {len(comps)}  网络: {len(nets)}")
    print(f"位号前缀 Top10: {top}")
    dns = [r for r, c in comps.items() if c.get('dns')]
    if dns:
        print(f"DNS/不贴装(Do Not Stuff): {len(dns)} 个: {' '.join(sorted(dns)[:30])}")
    print(f"网络表快照(可入库 diff): {export_json(p)}")


def cmd_comps(a):
    p, j = load_design(a.design)
    rows = []
    for ref, c in sorted(j['components'].items()):
        if a.type and refdes_prefix(ref) != a.type.upper():
            continue
        if a.ref and a.ref.upper() not in ref.upper():
            continue
        text = ' '.join(str(c.get(k, '')) for k in ('mpn', 'description', 'value'))
        if a.mpn and a.mpn.lower() not in text.lower():
            continue
        rows.append((ref, c.get('value', ''), c.get('mpn', ''), (c.get('description', '') or '')[:40],
                     'DNS' if c.get('dns') else ''))
    if not rows:
        print("无匹配器件")
        return
    print(f"{'位号':<8} {'值':<12} {'MPN':<22} 描述")
    for ref, val, mpn, desc, dns in rows:
        print(f"{ref:<8} {val[:12]:<12} {mpn[:22]:<22} {desc} {dns}")
    print(f"共 {len(rows)} 个")


def cmd_pins(a):
    p, j = load_design(a.design)
    c = j['components'].get(a.ref)
    if not c:
        print(f"[错误] 无此位号: {a.ref}(可用 comps 查)")
        sys.exit(2)
    print(f"位号 {a.ref}  值={c.get('value','')}  MPN={c.get('mpn','')}")
    print(f"{'脚':>5} {'脚名':<12} 网络")
    for num in sorted(c.get('pins', {}), key=pin_key):
        e = c['pins'][num]
        print(f"{num:>5} {pin_name(e, num):<12} {pin_net(e)}")


def cmd_nets(a):
    p, j = load_design(a.design)
    nets = j['nets']
    if a.net:
        members = nets.get(a.net)
        if members is None:
            cand = [n for n in nets if a.net.lower() in n.lower()]
            print(f"[错误] 无此网络: {a.net}" + (f"\n相近: {cand[:10]}" if cand else ""))
            sys.exit(2)
        print(f"网络 {a.net} 成员({sum(len(v) if isinstance(v, list) else 1 for v in members.values())} 脚):")
        for ref in sorted(members):
            pins = members[ref]
            pins = pins if isinstance(pins, list) else [pins]
            print(f"  {ref:<10} 脚 {','.join(pins)}")
        return
    rows = [(n, sum(len(v) if isinstance(v, list) else 1 for v in m.values()))
            for n, m in nets.items() if not a.match or a.match.lower() in n.lower()]
    if not rows:
        print("无匹配网络")
        return
    rows.sort(key=lambda x: -x[1])
    print(f"{'网络':<32} 脚数")
    for n, cnt in rows:
        print(f"{n[:32]:<32} {cnt}")
    print(f"共 {len(rows)} 个网络")


def cmd_xnet(a):
    p, j = load_design(a.design)
    nets, comps = j['nets'], j['components']
    if a.net not in nets:
        cand = [n for n in nets if a.net.lower() in n.lower()]
        print(f"[错误] 无此网络: {a.net}" + (f"\n相近: {cand[:10]}" if cand else ""))
        sys.exit(2)
    skip = set(x.strip().upper() for x in (a.skip or '').split(',') if x.strip())
    visited, found = set(), {}

    def expand(net):
        if net in visited:
            return
        visited.add(net)
        members = nets.get(net, {})
        for ref, pins in members.items():
            plist = pins if isinstance(pins, list) else [pins]
            c = comps.get(ref, {})
            pfx = refdes_prefix(ref)
            if len(plist) == 2 and len(c.get('pins', {})) == 2 and pfx in SERIES_PREFIX and pfx not in skip:
                # 串行元件: 穿过去继续追
                other = pin_net(c['pins'][plist[0] if pin_net(c['pins'][plist[0]]) == net else plist[1]])
                found[ref] = c
                if not is_power(other):
                    expand(other)
            else:
                found[ref] = c

    if is_power(a.net):
        print(f"[提示] {a.net} 疑似电源/地网, 追网通常无意义; 只列直达器件")
    expand(a.net)
    print(f"扩展网络起点: {a.net}")
    print(f"途经网络: {', '.join(sorted(visited))}")
    print(f"涉及器件 {len(found)} 个:")
    for ref in sorted(found):
        c = found[ref]
        conns = []
        for num in sorted(c.get('pins', {}), key=pin_key):
            e = c['pins'][num]
            if pin_net(e) in visited:
                conns.append(f"{num}→{pin_net(e)}")
        print(f"  {ref:<10} {c.get('value',''):<10} {' '.join(conns)}")
    print("[说明] 追网规则: 穿过 2 脚 R/C/L/FB/保险丝; 电源地停止; 与 universal-netlist "
          "MCP 版 query_xnet 的 power-rail 判定可能有差异, 结论以交叉核对为准")


def cmd_export(a):
    p = Path(a.design)
    if not p.is_file():
        print(f"[错误] 文件不存在: {p}")
        sys.exit(2)
    out = Path(a.out) if a.out else Path.cwd() / (p.stem + '.netlist.json')
    unl = find_unl()
    r = subprocess.run([unl, 'export-json', str(p), str(out)], capture_output=True, text=True, shell=False)
    if r.returncode != 0:
        print(f"[错误] 导出失败:\n{r.stdout}\n{r.stderr}")
        sys.exit(2)
    print(f"已导出: {out}")


def main():
    ap = argparse.ArgumentParser(description='EDA 原理图源文件分析桥(基于 universal-netlist)')
    sub = ap.add_subparsers(dest='cmd', required=True)

    p = sub.add_parser('info', help='总览'); p.add_argument('design'); p.set_defaults(fn=cmd_info)

    p = sub.add_parser('comps', help='器件清单')
    p.add_argument('design')
    p.add_argument('--type', help='前缀过滤')
    p.add_argument('--ref', help='位号子串')
    p.add_argument('--mpn', help='MPN/描述子串')
    p.set_defaults(fn=cmd_comps)

    p = sub.add_parser('pins', help='器件引脚表')
    p.add_argument('design'); p.add_argument('--ref', required=True)
    p.set_defaults(fn=cmd_pins)

    p = sub.add_parser('nets', help='网络清单/成员')
    p.add_argument('design')
    p.add_argument('--match', help='网络名子串')
    p.add_argument('--net', help='精确网络名, 列成员')
    p.set_defaults(fn=cmd_nets)

    p = sub.add_parser('xnet', help='扩展网络追网')
    p.add_argument('design')
    p.add_argument('--net', required=True)
    p.add_argument('--skip', help='追网跳过的前缀, 逗号分隔(如 C,L)')
    p.set_defaults(fn=cmd_xnet)

    p = sub.add_parser('export', help='导出 .netlist.json')
    p.add_argument('design'); p.add_argument('--out')
    p.set_defaults(fn=cmd_export)

    a = ap.parse_args()
    a.fn(a)


if __name__ == '__main__':
    main()
