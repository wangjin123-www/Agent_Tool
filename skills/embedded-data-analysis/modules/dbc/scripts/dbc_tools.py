#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DBC / CAN 数据库分析工具 —— embedded-data-analysis(嵌入式数据分析) · dbc 模块

确定性工作全在本脚本（基于 cantools），AI 只做解释。
用法: python dbc_tools.py <子命令> <dbc文件> [选项]

子命令:
  info      <dbc>                     总览: 节点/报文/信号统计、版本、周期报文占比
  messages  <dbc> [--id X] [--msg S] [--node S] [--rx-node S]
                                     报文清单: ID(hex/dec)/名字/DLC/发送者/周期/接收者
  signals   <dbc> --msg NAME|ID      信号明细: bit起始/长度/字节序/缩放/偏移/单位/范围/值表
  decode    <dbc> --msg NAME|ID --data "01 AB ..."
                                     原始数据字节 -> 物理值(含符号值翻译)
  encode    <dbc> --msg NAME|ID --set Signal=v1,Signal2=v2
                                     物理值 -> 原始数据字节(hex, 带回读校验)
  dump      <dbc> [--format table|json|csv] [--out FILE]
                                     全量导出(默认文本表格)
  c-code    <dbc> [--out DIR] [--no-float] [--use-float] [--node NAME]
                                     生成 C 解析代码(进程内调 cantools c_source.generate, 供 MCU 端)
  scan      [--dir DIR]              扫描目录下的 .dbc 文件
"""
import argparse
import os
import sys
from pathlib import Path

# Windows 管道下 stdout 可能是 cp936, 强制 UTF-8 防打印中文/单位炸编码
for _s in (sys.stdout, sys.stderr):
    if _s.encoding and _s.encoding.lower().replace('-', '') != 'utf8':
        try:
            _s.reconfigure(encoding='utf-8', errors='replace')
        except Exception:
            pass

INSTALL_HINT = (
    "缺少 cantools 库。安装: python -m pip install cantools\n"
    "公司网/国内网慢可用镜像: python -m pip install cantools -i https://pypi.tuna.tsinghua.edu.cn/simple"
)


def _patch_entry_points():
    """环境容错(2026-10-26 实测): 本机 python 的 grpcio/grpcio_tools/setuptools
    dist-info 元数据是 GBK 编码, python-can 导入时扫 entry_points 按 UTF-8 读会炸.
    包一层容错: 坏元数据的 dist 跳过(只影响 can 硬件接口插件的发现, 不影响 DBC 解析).
    根治 = 用管理员把那几个 dist-info/*.txt 转存 UTF-8, 或修好后 pip --force-reinstall 对应包.
    """
    import importlib.metadata as md
    if getattr(md, '_omni_patched', False):
        return
    orig = md.entry_points

    def _safe(*a, **kw):
        try:
            return orig(*a, **kw)
        except UnicodeDecodeError:
            print('[环境提示] 检测到 GBK 编码的包元数据(已容错跳过, 不影响本工具); '
                  '根治可重装 grpcio/grpcio-tools/setuptools', file=sys.stderr)
            return md.EntryPoints([])

    md.entry_points = _safe
    md._omni_patched = True


_patch_entry_points()
try:
    import cantools
except ImportError:
    print(INSTALL_HINT)
    sys.exit(3)


# ---------------------------------------------------------------- 基础工具
def sniff_encoding(path: Path) -> str:
    """国产 DBC 常见 GBK 编码(注释/值表含中文): 字节不是合法 UTF-8 就按 GBK 读"""
    raw = path.read_bytes()
    try:
        raw.decode('utf-8')
        return 'utf-8'
    except UnicodeDecodeError:
        return 'gbk'


def load_db(path: str, encoding: str = None):
    p = Path(path)
    if not p.is_file():
        print(f"[错误] 文件不存在: {p}")
        sys.exit(2)
    enc = encoding or sniff_encoding(p)
    try:
        db = cantools.database.load_file(str(p), encoding=enc)
        if enc != 'utf-8':
            print(f"[提示] 检测到非 UTF-8 编码, 已按 {enc} 解析(可 --encoding 覆盖)", file=sys.stderr)
        return db
    except Exception as e:
        print(f"[错误] DBC 解析失败(encoding={enc}): {p}\n{type(e).__name__}: {e}")
        sys.exit(2)


def fmt_id(msg) -> str:
    """帧 ID: 0x1A0 (扩展帧加标记)"""
    ext = "29bit" if getattr(msg, 'is_extended_frame', False) else "11bit"
    return f"0x{msg.frame_id:03X}({msg.frame_id}) {ext}"


def fmt_order(sig) -> str:
    return "Motorola" if sig.byte_order == 'big_endian' else "Intel"


def fmt_choices(sig, limit=8) -> str:
    """值表(信号取值 -> 含义), 截断显示"""
    if not sig.choices:
        return ""
    items = list(sig.choices.items())
    head = ", ".join(f"{k}={v}" for k, v in items[:limit])
    return head + (f" …(+{len(items) - limit})" if len(items) > limit else "")


def fmt_mux(sig) -> str:
    if sig.is_multiplexer:
        return "Muxer"
    if getattr(sig, 'multiplexer_signal', None):
        vals = getattr(sig, 'multiplexer_ids', None)
        rng = f"={','.join(str(v) for v in vals)}" if vals else ""
        return f"Mux({sig.multiplexer_signal}{rng})"
    return ""


def resolve_msg(db, ref: str):
    """--msg 参数解析: 报文名(精确/唯一前缀) 或 ID(0x1A0/416)"""
    ref = ref.strip()
    # 1) 名字精确命中
    for m in db.messages:
        if m.name == ref:
            return m
    # 2) 当 ID 用(0x.. / 十进制)
    try:
        fid = int(ref, 0)
        return db.get_message_by_frame_id(fid)
    except Exception:
        pass
    # 3) 名字唯一子串
    hits = [m for m in db.messages if ref.lower() in m.name.lower()]
    if len(hits) == 1:
        return hits[0]
    if len(hits) > 1:
        print(f"[错误] '{ref}' 模糊命中 {len(hits)} 个报文, 请给全名或 ID:")
        for m in hits[:20]:
            print(f"  {fmt_id(m)}  {m.name}")
        sys.exit(1)
    print(f"[错误] 找不到报文: '{ref}' (既不是报文名也不是帧 ID)")
    sys.exit(1)


def parse_hex_data(s: str, expect_len: int) -> bytes:
    """'01 AB 03' / '01AB03' / '0x01,0xAB' -> bytes; 长度须等于 DLC"""
    cleaned = s.replace('0x', '').replace('0X', '').replace(',', ' ').replace(':', ' ')
    cleaned = cleaned.replace('-', ' ').strip()
    try:
        data = bytes.fromhex(cleaned.replace(' ', ''))
    except ValueError:
        print(f"[错误] 数据不是合法 hex: {s!r}")
        sys.exit(1)
    if len(data) != expect_len:
        print(f"[错误] 数据 {len(data)} 字节 != 报文 DLC {expect_len} 字节")
        sys.exit(1)
    return data


def parse_set_values(kv_str: str) -> dict:
    """'A=1,B=2.5,C=On' -> {'A':1,'B':2.5,'C':'On'}; 数值自动转 int/float, 其余按符号值"""
    out = {}
    for part in kv_str.split(','):
        part = part.strip()
        if not part:
            continue
        if '=' not in part:
            print(f"[错误] --set 格式: '{part}' 缺 '=' (正确如 Signal1=1,Signal2=On)")
            sys.exit(1)
        k, v = part.split('=', 1)
        k, v = k.strip(), v.strip()
        try:
            out[k] = int(v, 0)
            continue
        except ValueError:
            pass
        try:
            out[k] = int(v, 10)
            continue
        except ValueError:
            pass
        try:
            out[k] = float(v)
            continue
        except ValueError:
            pass
        out[k] = v  # 符号值(值表里的含义字符串)
    return out


# ---------------------------------------------------------------- 子命令
def cmd_info(args):
    db = load_db(args.dbc, getattr(args, "encoding", None))
    msgs = db.messages
    n_sigs = sum(len(m.signals) for m in msgs)
    n_ext = sum(1 for m in msgs if getattr(m, 'is_extended_frame', False))
    n_cyc = sum(1 for m in msgs if m.cycle_time)
    j1939 = [m for m in msgs if getattr(m, 'pgn', None)]
    print(f"数据库 : {Path(args.dbc).name}")
    print(f"版本   : {db.version or '(未标注)'}")
    print(f"节点   : {len(db.nodes)} 个 -> {', '.join(n.name for n in db.nodes) or '(无)'}")
    print(f"报文   : {len(msgs)} 条 (扩展帧 {n_ext} / 标准帧 {len(msgs) - n_ext})"
          + (f" [含 J1939 PGN 报文 {len(j1939)} 条]" if j1939 else ""))
    print(f"信号   : {n_sigs} 个 (平均 {n_sigs / len(msgs):.1f} 个/报文)" if msgs else "信号   : 0")
    print(f"周期   : {n_cyc} 条带发送周期, 其余为事件/未知")
    # 多路复用报文单列
    mux = [m.name for m in msgs if m.is_multiplexed]
    if mux:
        print(f"复用   : {len(mux)} 条多路复用报文 (如 {', '.join(mux[:5])})")
    # 发送最多的节点 Top3
    send_stat = {}
    for m in msgs:
        for s in (m.senders or ['(未标注)']):
            send_stat[s] = send_stat.get(s, 0) + 1
    top = sorted(send_stat.items(), key=lambda x: -x[1])[:3]
    if top:
        print("节点发报 Top3 : " + " | ".join(f"{k}: {v}条" for k, v in top))
    print(f"文件   : {Path(args.dbc).resolve()}")


def cmd_messages(args):
    db = load_db(args.dbc, getattr(args, "encoding", None))
    rows = db.messages
    if args.id is not None:
        rows = [m for m in rows if m.frame_id == args.id]
    if args.msg:
        rows = [m for m in rows if args.msg.lower() in m.name.lower()]
    if args.node:
        rows = [m for m in rows
                if args.node.lower() in ' '.join(m.senders or []).lower()
                or args.node.lower() in ' '.join(m.receivers or []).lower()]
    if args.rx_node:
        rows = [m for m in rows if args.rx_node.lower() in ' '.join(m.receivers or []).lower()]
    if not rows:
        print("[提示] 无匹配报文(检查 --id/--msg/--node 过滤条件)")
        return
    w = max((len(m.name) for m in rows), default=10)
    print(f"共 {len(rows)} 条报文:")
    print(f"{'ID':<20} {'名字':<{w}}  DLC 周期ms 发送者")
    print("-" * (30 + w))
    for m in sorted(rows, key=lambda x: x.frame_id):
        senders = ','.join(m.senders or ['?'])
        cyc = str(m.cycle_time) if m.cycle_time else '-'
        name_mux = m.name + (' [Mux]' if m.is_multiplexed else '')
        print(f"{fmt_id(m):<20} {name_mux:<{w}}  {m.length:<3} {cyc:<6} {senders}")


def cmd_signals(args):
    db = load_db(args.dbc, getattr(args, "encoding", None))
    m = resolve_msg(db, args.msg)
    print(f"报文: {m.name}  ID={fmt_id(m)}  DLC={m.length}"
          + (f"  周期={m.cycle_time}ms" if m.cycle_time else "")
          + (f"  发送: {','.join(m.senders)}" if m.senders else ""))
    if m.comment:
        print(f"说明: {str(m.comment).strip()[:120]}")
    if not m.signals:
        print("[提示] 该报文无信号定义")
        return
    nw = max(len(s.name) for s in m.signals)
    print(f"\n{'信号':<{nw}}  bit起/长   字节序    缩放        偏移        单位  范围                接收者")
    print("-" * (nw + 100))
    for s in m.signals:
        rng = f"{s.minimum}..{s.maximum}" if s.minimum is not None else ""
        recv = ','.join(s.receivers or ['?'])
        scale = str(s.scale) if s.scale is not None else '1'
        offset = str(s.offset) if s.offset is not None else '0'
        print(f"{s.name:<{nw}}  {s.start:<3}/{s.length:<5} {fmt_order(s):<9}  {scale:<11} {offset:<11} "
              f"{(s.unit or ''):<5} {rng:<20} {recv}")
        mux = fmt_mux(s)
        choices = fmt_choices(s)
        if mux:
            print(f"{'':<{nw}}  + {mux}")
        if choices:
            print(f"{'':<{nw}}  + 值表: {choices}")


def cmd_decode(args):
    db = load_db(args.dbc, getattr(args, "encoding", None))
    m = resolve_msg(db, args.msg)
    data = parse_hex_data(args.data, m.length)
    print(f"报文: {m.name}  ID={fmt_id(m)}  DLC={m.length}")
    print(f"数据: {data.hex(' ').upper()}")
    try:
        values = m.decode(data, decode_choices=not args.raw, scaling=True)
    except Exception as e:
        print(f"[错误] 解码失败: {type(e).__name__}: {e}")
        sys.exit(1)
    nw = max(len(k) for k in values)
    print(f"\n{'信号':<{nw}} = 值")
    print("-" * (nw + 40))
    for k, v in values.items():
        sig = next(s for s in m.signals if s.name == k)
        unit = f" {sig.unit}" if sig.unit else ""
        if isinstance(v, float) and v == int(v):
            v_out = int(v)
        else:
            v_out = v
        raw = ''
        if args.raw or True:
            try:
                raw_v = m.decode(data, decode_choices=False, scaling=False)[k]
                raw = f"  (raw {raw_v})"
            except Exception:
                pass
        print(f"{k:<{nw}} = {v_out}{unit}{raw}")


def cmd_encode(args):
    db = load_db(args.dbc, getattr(args, "encoding", None))
    m = resolve_msg(db, args.msg)
    vals = parse_set_values(args.set)
    sig_names = {s.name for s in m.signals}
    unknown = [k for k in vals if k not in sig_names]
    if unknown:
        print(f"[错误] 报文 {m.name} 无这些信号: {', '.join(unknown)}")
        print("现有信号: " + ', '.join(s.name for s in m.signals))
        sys.exit(1)
    strict = not args.loose
    if not strict:
        # 预填缺省信号(含 mux 选择信号, 否则多路复用报文 encode 直接 KeyError):
        # initial_value -> minimum -> 0
        missing = []
        for s in m.signals:
            if s.name in vals:
                continue
            default = getattr(s, 'initial_value', None)
            if default is None:
                default = s.minimum if s.minimum is not None else 0
            vals[s.name] = default
            missing.append(s.name)
        if missing:
            print(f"[loose] 未给出的 {len(missing)} 个信号按默认值(initial/min/0)编码: "
                  + ', '.join(missing[:10]) + (" …" if len(missing) > 10 else ""))
    try:
        data = m.encode(vals, scaling=True, padding=False, strict=strict)
    except Exception as e:
        print(f"[错误] 编码失败(检查取值范围/符号值拼写): {type(e).__name__}: {e}")
        print(f"提示: 严格模式要求给全所有信号; 加 --loose 可让未给出的信号按默认值编码")
        sys.exit(1)
    print(f"报文: {m.name}  ID={fmt_id(m)}  DLC={m.length}")
    print(f"输入: {args.set}")
    print(f"数据: {data.hex(' ').upper()}")
    # 回读校验(让用户敢直接用): 按物理数值比对, 不受符号翻译影响
    def _eq(a, b):
        try:
            return abs(float(a) - float(b)) < 1e-9
        except (TypeError, ValueError):
            return str(a) == str(b)
    try:
        back = m.decode(data, decode_choices=True, scaling=True)
        back_num = m.decode(data, decode_choices=False, scaling=True)
        diffs = {}
        for k in vals:
            if k not in back_num:
                continue
            if _eq(vals[k], back_num[k]):
                continue
            if isinstance(vals[k], str) and str(back.get(k)) == vals[k]:
                continue  # 用户给符号值(如 On), 解码回同一符号 = 一致
            diffs[k] = (vals[k], back_num[k])
        note = f"(回读不一致: {diffs})" if diffs else "(回读一致)"
        print(f"回读: {note}" + ("  " + ", ".join(f"{k}={v}" for k, v in back.items())))
    except Exception:
        pass


def cmd_dump(args):
    db = load_db(args.dbc, getattr(args, "encoding", None))
    rows = []
    for m in sorted(db.messages, key=lambda x: x.frame_id):
        for s in m.signals:
            rows.append({
                'message': m.name, 'id_hex': f"0x{m.frame_id:03X}", 'id_dec': m.frame_id,
                'dlc': m.length, 'cycle_ms': m.cycle_time or '',
                'senders': '|'.join(m.senders or []),
                'signal': s.name, 'start_bit': s.start, 'length': s.length,
                'byte_order': fmt_order(s), 'signed': int(s.is_signed),
                'scale': s.scale, 'offset': s.offset, 'unit': s.unit or '',
                'minimum': s.minimum, 'maximum': s.maximum,
                'receivers': '|'.join(s.receivers or []), 'mux': fmt_mux(s) or '',
                'value_table': fmt_choices(s, limit=1000),
            })
    fmt = args.format
    out = args.out
    if fmt == 'json':
        payload = {
            'file': str(Path(args.dbc).resolve()), 'version': db.version,
            'nodes': [n.name for n in db.nodes], 'message_count': len(db.messages),
            'signals': rows,
        }
        text = __import__('json').dumps(payload, ensure_ascii=False, indent=2)
    elif fmt == 'csv':
        import csv
        import io as _io
        buf = _io.StringIO()
        if rows:
            w = csv.DictWriter(buf, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
        text = buf.getvalue()
    else:  # table
        if not rows:
            text = "(无信号)"
        else:
            hdr = ['id_hex', 'message', 'signal', 'start_bit', 'length', 'byte_order',
                   'scale', 'offset', 'unit', 'mux']
            widths = {c: max(len(str(r[c])) for r in rows) for c in hdr}
            text = '  '.join(c.ljust(widths[c]) for c in hdr) + '\n'
            text += '  '.join('-' * widths[c] for c in hdr) + '\n'
            for r in rows:
                text += '  '.join(str(r[c]).ljust(widths[c]) for c in hdr) + '\n'
    if out:
        Path(out).parent.mkdir(parents=True, exist_ok=True)
        Path(out).write_text(text, encoding='utf-8-sig' if fmt == 'csv' else 'utf-8')
        print(f"已导出 {len(rows)} 行信号 -> {Path(out).resolve()}")
    else:
        print(text)


def cmd_c_code(args):
    db = load_db(args.dbc, getattr(args, "encoding", None))
    out_dir = Path(args.out) if args.out else Path(args.dbc).parent / \
        (Path(args.dbc).stem + '_gen')
    out_dir.mkdir(parents=True, exist_ok=True)
    # 进程内调官方同款生成器(避免 `python -m cantools` 子进程在本机 GBK 元数据环境下导入失败)
    from cantools.database.can.c_source import camel_to_snake_case, generate
    name = args.name or camel_to_snake_case(Path(args.dbc).stem)
    fh, fc = name + '.h', name + '.c'
    header, source, _, _ = generate(
        db, name, fh, fc, name + '_fuzzer.c',
        floating_point_numbers=not args.no_float,
        bit_fields=False,
        use_float=args.use_float,
        node_name=args.node,
        use_round=False)
    (out_dir / fh).write_text(header, encoding='utf-8')
    (out_dir / fc).write_text(source, encoding='utf-8')
    print(f"生成: {out_dir / fh}  ({(out_dir / fh).stat().st_size} bytes)")
    print(f"生成: {out_dir / fc}  ({(out_dir / fc).stat().st_size} bytes)")
    print("落地建议: .h/.c 可直接拷入 MCU 工程(纯 C、无动态内存、MISRA 友好);"
          "默认 double 缩放, 无 FPU 加 --no-float、要 float 加 --use-float 重生成")


def cmd_scan(args):
    root = Path(args.dir or '.')
    if not root.is_dir():
        print(f"[错误] 目录不存在: {root}")
        sys.exit(2)
    hits = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames
                       if d not in ('.git', 'node_modules', '__pycache__', '.metadata')]
        for fn in filenames:
            if fn.lower().endswith('.dbc'):
                p = Path(dirpath) / fn
                hits.append(p)
    if not hits:
        print(f"[提示] {root} 下未找到 .dbc (cantools 也支持 .arxml/.kcd, 本扫描只列 .dbc)")
        return
    hits.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    print(f"共 {len(hits)} 个 .dbc (按修改时间倒序):")
    import time
    for p in hits:
        sz = p.stat().st_size
        mt = time.strftime('%Y-%m-%d %H:%M', time.localtime(p.stat().st_mtime))
        print(f"  {mt}  {sz:>10,} B  {p}")


# ---------------------------------------------------------------- 入口
def main():
    ap = argparse.ArgumentParser(description='DBC / CAN 数据库分析工具(embedded-data-analysis·dbc模块)',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=__doc__.split('子命令:')[-1])
    sub = ap.add_subparsers(dest='cmd', required=True)

    # 公共参数: <dbc> + --encoding(国产 DBC 常见 GBK, 默认自动嗅探)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument('dbc')
    common.add_argument('--encoding', default=None,
                        help='DBC 文件编码(默认自动嗅探: 非 UTF-8 按 GBK)')

    p = sub.add_parser('info', parents=[common], help='总览统计')
    p.set_defaults(func=cmd_info)

    p = sub.add_parser('messages', parents=[common], help='报文清单(可过滤)')
    p.add_argument('--id', type=lambda x: int(x, 0), default=None, help='按帧ID过滤, 0x1A0 或 416')
    p.add_argument('--msg', default=None, help='按报文名(子串, 不区分大小写)')
    p.add_argument('--node', default=None, help='按节点(发送或接收)')
    p.add_argument('--rx-node', dest='rx_node', default=None, help='仅按接收节点')
    p.set_defaults(func=cmd_messages)

    p = sub.add_parser('signals', parents=[common], help='某报文的信号明细')
    p.add_argument('--msg', required=True, help='报文名或帧ID(0x1A0/416)')
    p.set_defaults(func=cmd_signals)

    p = sub.add_parser('decode', parents=[common], help='原始数据字节 -> 物理值')
    p.add_argument('--msg', required=True, help='报文名或帧ID')
    p.add_argument('--data', required=True, help='hex 字节, 如 "01 AB 03" 或 "01AB03"')
    p.add_argument('--raw', action='store_true', help='raw value: decode without value-table translation')
    p.set_defaults(func=cmd_decode)

    p = sub.add_parser('encode', parents=[common], help='物理值 -> 原始数据字节')
    p.add_argument('--msg', required=True, help='报文名或帧ID')
    p.add_argument('--set', required=True, help='信号=值 逗号分隔, 如 EngSpeed=1500,State=On')
    p.add_argument('--loose', action='store_true',
                   help='宽松模式: 未给出的信号按默认值编码(默认严格=必须给全)')
    p.set_defaults(func=cmd_encode)

    p = sub.add_parser('dump', parents=[common], help='全量导出')
    p.add_argument('--format', choices=['table', 'json', 'csv'], default='table')
    p.add_argument('--out', default=None, help='输出文件(不填则打印到终端)')
    p.set_defaults(func=cmd_dump)

    p = sub.add_parser('c-code', parents=[common], help='生成 C 解析代码')
    p.add_argument('--out', default=None, help='输出目录(默认 <dbc同目录>/<名>_gen/)')
    p.add_argument('--name', default=None, help='生成的 .h/.c 基名(默认取 DBC 文件名 snake_case)')
    p.add_argument('--no-float', dest='no_float', action='store_true', help='禁用浮点(定点缩放, 无 FPU 用)')
    p.add_argument('--use-float', dest='use_float', action='store_true', help='用 float 替代 double')
    p.add_argument('--node', default=None, help='只生成该节点收发的报文')
    p.set_defaults(func=cmd_c_code)

    p = sub.add_parser('scan', help='扫描 .dbc 文件')
    p.add_argument('--dir', default='.', help='扫描根目录(默认当前)')
    p.set_defaults(func=cmd_scan)

    args = ap.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
