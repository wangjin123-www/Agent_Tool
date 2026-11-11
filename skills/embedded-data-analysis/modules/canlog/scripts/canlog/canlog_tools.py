#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CAN 总线日志(BLF/ASC/TRC/CSV)分析工具 —— embedded-data-analysis(嵌入式数据分析) · canlog 模块

读: python-can(GitHub hardbyte/python-can, BLFReader/ASCWriter 等, Vector BLF 标准实现)
解: cantools(GitBox/cantools, DBC 物理值解码)
波形: cantools 自带 `cantools plot`(matplotlib 波形引擎, -o 可存 PNG) —— 本工具把日志转成
      candump 流喂给它, 波形图由 cantools 本身绘制, 不是自造轮子
表: stdout 表格 + CSV/XLSX 导出(openpyxl)

确定性解析全在库+本脚本, AI 只做解释。
用法: python canlog_tools.py <子命令> <log> [选项]

子命令:
  info    <log>                       总览: 帧数/时长/通道/ID 分布(Top+N+周期)/错误帧
  frames  <log> [--id 0x1A5] [--ch N] [--limit N]
                                    原始帧清单(时间/通道/ID/DLC/数据hex)
  decode  <log> --dbc X.dbc [--id X] [--signals a,b] [--limit N]
                                    帧物理值解码表(含值表符号翻译)
  export  <log> --dbc X.dbc [--format csv|xlsx] [--layout long|wide] [--out F]
                                    全量信号导出(long=透视友好, wide=一帧一行)
  plot    <log> --dbc X.dbc --signals "a,b[:fmt] - c" [--out F.png] [--style S]
                                    波形图(cantools plot 引擎; 无 --out 开交互窗口)
  convert <log> --to asc|blf|csv [--out F]
                                    日志格式互转
  scan    [--dir DIR]                扫描目录找 .blf/.asc/.trc/.canlog
"""
import argparse
import os
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

# Windows 管道下 stdout 可能是 cp936, 强制 UTF-8(与 dbc_tools 同款)
for _s in (sys.stdout, sys.stderr):
    if _s.encoding and _s.encoding.lower().replace('-', '') != 'utf8':
        try:
            _s.reconfigure(encoding='utf-8', errors='replace')
        except Exception:
            pass

MODULE_ROOT = Path(__file__).resolve().parent.parent.parent

INSTALL_HINTS = []
try:
    import can  # python-can
except ImportError:
    INSTALL_HINTS.append(
        "缺少 python-can。安装: python -m pip install python-can\n"
        "国内镜像: python -m pip install python-can -i https://pypi.tuna.tsinghua.edu.cn/simple")
try:
    import cantools
except ImportError:
    INSTALL_HINTS.append(
        "缺少 cantools。安装: python -m pip install cantools\n"
        "国内镜像: python -m pip install cantools -i https://pypi.tuna.tsinghua.edu.cn/simple")
if INSTALL_HINTS:
    print('\n'.join(INSTALL_HINTS))
    sys.exit(3)

LOG_EXTS = {'.blf', '.asc', '.trc', '.canlog', '.csv'}


def sniff_encoding(path: Path) -> str:
    raw = path.read_bytes()
    try:
        raw.decode('utf-8')
        return 'utf-8'
    except UnicodeDecodeError:
        return 'gbk'


def load_log(path: str):
    """返回 (messages 列表, format 名)"""
    p = Path(path)
    if not p.is_file():
        print(f"[错误] 文件不存在: {p}")
        sys.exit(2)
    ext = p.suffix.lower()
    fmt = {'blf': 'BLF', 'asc': 'ASC', 'trc': 'TRC', 'csv': 'CSV', 'canlog': 'candump'}.get(ext.lstrip('.'), '?')
    try:
        if ext == '.blf':
            reader = can.BLFReader(str(p))
        elif ext == '.asc':
            reader = can.ASCReader(str(p))
        elif ext == '.trc':
            reader = can.TRCReader(str(p))
        elif ext == '.csv':
            reader = can.CSVReader(str(p))
        else:
            reader = can.LogReader(str(p))
        msgs = list(reader)
    except Exception as e:
        print(f"[错误] 日志解析失败({fmt}): {p}\n{type(e).__name__}: {e}")
        sys.exit(2)
    return p, msgs, fmt


def load_dbc(dbc_path):
    p = Path(dbc_path)
    if not p.is_file():
        print(f"[错误] DBC 不存在: {p}")
        sys.exit(2)
    try:
        return cantools.database.load_file(str(p), encoding=sniff_encoding(p))
    except Exception as e:
        print(f"[错误] DBC 解析失败: {p}\n{type(e).__name__}: {e}")
        sys.exit(2)


def parse_id(s):
    return int(s, 16) if s.lower().startswith('0x') else int(s, 0)


# ---------------------------------------------------------------- 子命令
def cmd_info(a):
    p, msgs, fmt = load_log(a.log)
    if not msgs:
        print("空日志(0 帧)")
        return
    t0, t1 = msgs[0].timestamp, msgs[-1].timestamp
    dur = t1 - t0
    ids = Counter(m.arbitration_id for m in msgs)
    chs = Counter(getattr(m, 'channel', None) for m in msgs)
    err = sum(1 for m in msgs if m.is_error_frame)
    print(f"文件: {p}  格式: {fmt}")
    print(f"帧数: {len(msgs)}  时长: {dur:.3f}s  平均负载: {len(msgs)/dur if dur else 0:.0f} 帧/s")
    print(f"首帧时间戳: {t0:.6f}  末帧: {t1:.6f}")
    print(f"通道: {', '.join(str(c) for c in chs)}   错误帧: {err}")
    print(f"\nID 分布(共 {len(ids)} 个, Top15):")
    print(f"{'ID':>10} {'帧数':>7} {'估算周期':>10} {'扩展帧':>5}")
    for fid, cnt in ids.most_common(15):
        # 估算周期: 相邻两帧间隔的中位数太贵, 用 时长/帧数 的倒数
        period = dur / cnt if cnt > 1 else 0
        ps = f"{period*1000:.0f}ms" if period else '-'
        ext = next(m.is_extended_id for m in msgs if m.arbitration_id == fid)
        print(f"0x{fid:08X} {cnt:>7} {ps:>10} {'29bit' if ext else '11bit':>5}")


def cmd_frames(a):
    p, msgs, fmt = load_log(a.log)
    fid = parse_id(a.id) if a.id else None
    rows = []
    for m in msgs:
        if fid is not None and m.arbitration_id != fid:
            continue
        if a.ch is not None and getattr(m, 'channel', None) != a.ch:
            continue
        rows.append(m)
    if not rows:
        print("无匹配帧")
        return
    n = a.limit or 30
    print(f"{'时间':>12} {'ch':>3} {'ID':>10} {'DLC':>3} 数据")
    for m in rows[:n]:
        ts = m.timestamp - msgs[0].timestamp
        print(f"{ts:>12.6f} {str(getattr(m,'channel','-'))[:3]:>3} 0x{m.arbitration_id:08X} {len(m.data):>3} {m.data.hex(' ').upper()}")
    if len(rows) > n:
        print(f"…共 {len(rows)} 帧(用 --limit 放宽)")


def _iter_decoded(msgs, db, want_id=None, want_signals=None):
    """yield (rel_ts, msg_obj, {sig: value})"""
    t0 = msgs[0].timestamp if msgs else 0
    for m in msgs:
        if want_id is not None and m.arbitration_id != want_id:
            continue
        try:
            msg = db.get_message_by_frame_id(m.arbitration_id)
        except KeyError:
            continue
        try:
            vals = msg.decode(m.data, decode_choices=True, scaling=True)
        except Exception:
            continue
        if want_signals:
            vals = {k: v for k, v in vals.items() if k in want_signals}
        yield m.timestamp - t0, msg, vals


def cmd_decode(a):
    p, msgs, fmt = load_log(a.log)
    db = load_dbc(a.dbc)
    want_id = parse_id(a.id) if a.id else None
    want_signals = set(a.signals.split(',')) if a.signals else None
    n = a.limit or 25
    shown = 0
    total = 0
    print(f"{'时间':>10} {'报文':<28} 信号=值")
    for ts, msg, vals in _iter_decoded(msgs, db, want_id, want_signals):
        total += 1
        if shown >= n:
            continue
        pairs = ' '.join(f"{k}={v}" for k, v in vals.items())
        print(f"{ts:>10.6f} {msg.name[:28]:<28} {pairs}")
        shown += 1
    if total > shown:
        print(f"…共 {total} 帧可解码(用 --limit 放宽; --id/--signals 过滤)")
    if total == 0:
        print("[提示] 0 帧可解码: 日志里的 ID 与 DBC 不匹配? 先 info 看 ID 分布, 再对照 DBC")


def _cell(v):
    """cantools 值表翻译返回 NamedSignalValue 对象, openpyxl 不认 —— 统一成数值或 str"""
    if isinstance(v, (int, float)):
        return v
    return str(v)


def _rows_long(msgs, db):
    for ts, msg, vals in _iter_decoded(msgs, db):
        for k, v in vals.items():
            yield [f"{ts:.6f}", getattr(msg, 'frame_id', ''), msg.name, k, _cell(v)]


def _rows_wide(msgs, db):
    cols = []
    seen = set()
    for ts, msg, vals in _iter_decoded(msgs, db):
        key = (msg.name, tuple(vals.keys()))
        if key not in seen:
            seen.add(key)
            cols.extend(f"{msg.name}.{k}" for k in vals)
    for ts, msg, vals in _iter_decoded(msgs, db):
        row = {f"{msg.name}.{k}": _cell(v) for k, v in vals.items()}
        yield [f"{ts:.6f}", msg.name] + [row.get(c, '') for c in cols], cols


def cmd_export(a):
    p, msgs, fmt = load_log(a.log)
    db = load_dbc(a.dbc)
    out = a.out or (str(p) + ('.xlsx' if a.format == 'xlsx' else '.signals.csv'))
    if a.layout == 'long':
        header = ['timestamp_s', 'frame_id', 'message', 'signal', 'value']
        data = list(_rows_long(msgs, db))
    else:
        gen = _rows_wide(msgs, db)
        first = next(gen, None)
        if first is None:
            print("0 帧可解码, 未导出")
            sys.exit(1)
        row0, cols = first
        header = ['timestamp_s', 'message'] + cols
        data = [row0] + [r for r, _ in gen]
    if not data:
        print("0 帧可解码, 未导出")
        sys.exit(1)
    if a.format == 'xlsx':
        try:
            from openpyxl import Workbook
        except ImportError:
            print("缺少 openpyxl: python -m pip install openpyxl")
            sys.exit(3)
        wb = Workbook(write_only=True)
        ws = wb.create_sheet('signals')
        ws.append(header)
        for r in data:
            ws.append(r)
        wb.save(out)
    else:
        import csv
        with open(out, 'w', newline='', encoding='utf-8-sig') as f:
            csv.writer(f).writerows([header] + data)
    print(f"已导出: {out}  ({len(data)} 行, {a.layout} 布局)")


def cmd_plot(a):
    p, msgs, fmt = load_log(a.log)
    db = load_dbc(a.dbc)
    # 日志 -> candump 文本流
    t0 = msgs[0].timestamp
    lines = []
    for m in msgs:
        lines.append(f"({m.timestamp:.6f}) ch{getattr(m, 'channel', 1)} {m.arbitration_id:X}#{m.data.hex()}")
    payload = '\n'.join(lines) + '\n'
    # cantools plot 信号语法: "Msg.sig[:fmt]" 可用 * ? 通配, '-' 分子图, ',' 分纵轴 —— 按空白切分原样透传
    sig_args = a.signals.split()
    cmd = [sys.executable, '-m', 'cantools', 'plot', a.dbc] + sig_args
    env = dict(os.environ)
    if a.out:
        cmd += ['-o', a.out]
        env['MPLBACKEND'] = 'Agg'       # 无窗口, savefig 即出
    if a.style:
        cmd += ['--style', a.style]
    r = subprocess.run(cmd, input=payload, capture_output=True, text=True,
                       encoding='utf-8', errors='replace', env=env, shell=False)
    print(r.stdout, end='')
    if r.returncode != 0:
        print(r.stderr, file=sys.stderr)
        print(f"[错误] cantools plot 失败(exit {r.returncode}); 信号语法: 'Msg.sig[:fmt]' 空格分隔, '-' 分子图, 详见 python -m cantools plot --help")
        sys.exit(2)
    if a.out:
        print(f"波形已保存: {a.out}")
    else:
        print("[提示] 未给 --out, 上一步应已弹出交互窗口(需本地图形环境)")


def cmd_convert(a):
    p, msgs, fmt = load_log(a.log)
    out = a.out or str(p.with_suffix('.' + a.to))
    if a.to == 'asc':
        with can.ASCWriter(out) as w:
            for m in msgs:
                w.on_message_received(m)
    elif a.to == 'blf':
        with can.BLFWriter(out) as w:
            for m in msgs:
                w.on_message_received(m)
    elif a.to == 'csv':
        with can.CSVWriter(out, append=False) as w:
            for m in msgs:
                w.on_message_received(m)
    else:
        print(f"不支持的 --to: {a.to}")
        sys.exit(2)
    print(f"已转换: {fmt} -> {a.to.upper()}  {out}  ({len(msgs)} 帧)")


def cmd_scan(a):
    root = Path(a.dir or '.')
    out = []
    for dirpath, _, files in os.walk(root):
        if 'node_modules' in dirpath:
            continue
        for f in files:
            if Path(f).suffix.lower() in LOG_EXTS:
                q = Path(dirpath) / f
                out.append((q.stat().st_mtime, q))
    out.sort(reverse=True)
    if not out:
        print(f"未找到 CAN 日志: {root}")
        return
    import time
    for mt, q in out[:30]:
        print(f"{time.strftime('%Y-%m-%d %H:%M', time.localtime(mt))}  {q}")


def main():
    ap = argparse.ArgumentParser(description='CAN 日志(BLF/ASC/TRC)分析: python-can 读 + cantools 解码/波形 + 表格导出')
    sub = ap.add_subparsers(dest='cmd', required=True)

    p = sub.add_parser('info', help='总览')
    p.add_argument('log'); p.set_defaults(fn=cmd_info)

    p = sub.add_parser('frames', help='原始帧清单')
    p.add_argument('log')
    p.add_argument('--id', help='按 arbitration id 过滤(0x1A5 或 421)')
    p.add_argument('--ch', help='按通道过滤')
    p.add_argument('--limit', type=int)
    p.set_defaults(fn=cmd_frames)

    p = sub.add_parser('decode', help='物理值解码表')
    p.add_argument('log'); p.add_argument('--dbc', required=True)
    p.add_argument('--id')
    p.add_argument('--signals', help='逗号分隔信号名过滤')
    p.add_argument('--limit', type=int)
    p.set_defaults(fn=cmd_decode)

    p = sub.add_parser('export', help='导出 CSV/XLSX')
    p.add_argument('log'); p.add_argument('--dbc', required=True)
    p.add_argument('--format', choices=['csv', 'xlsx'], default='csv')
    p.add_argument('--layout', choices=['long', 'wide'], default='long')
    p.add_argument('--out')
    p.set_defaults(fn=cmd_export)

    p = sub.add_parser('plot', help='波形图(cantools plot 引擎)')
    p.add_argument('log'); p.add_argument('--dbc', required=True)
    p.add_argument('--signals', required=True,
                   help="cantools 语法: 'PEPS_StartrequestValid BCM_DoorLockStsFrntLe:b-o', '-' 分子图")
    p.add_argument('--out', help='输出 PNG 等文件(不给则开交互窗口)')
    p.add_argument('--style', help='matplotlib 样式(--list-styles 查看)')
    p.set_defaults(fn=cmd_plot)

    p = sub.add_parser('convert', help='格式互转')
    p.add_argument('log')
    p.add_argument('--to', choices=['asc', 'blf', 'csv'], required=True)
    p.add_argument('--out')
    p.set_defaults(fn=cmd_convert)

    p = sub.add_parser('scan', help='扫描 CAN 日志')
    p.add_argument('--dir'); p.set_defaults(fn=cmd_scan)

    a = ap.parse_args()
    a.fn(a)


if __name__ == '__main__':
    main()
