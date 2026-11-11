#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PEmicro 探针无头烧录/调试（S32K3 + Multilink）。

实现路径: pegdbserver_console(PEmicro GDB Server CLI) + arm-none-eabi-gdb batch。
两者都随 S32DS 安装，零新增部署；路径自动探测，可用 config/pemicro.conf 覆盖。
调研结论与来源见 ../reference/pemicro-notes.md。

命令:
  download <elf|hex>   烧录(gdb load, 自动擦写) + 复位运行
  erase                整片擦除(monitor erase) + 复位
  reset                复位(monitor reset)
  verify <elf>         比对 ELF 段与 Flash(gdb compare-sections, 仅支持 elf)

用法:
  python pemicro_ops.py download Debug_FLASH/test_prj.elf
  python pemicro_ops.py erase
  python pemicro_ops.py reset
  python pemicro_ops.py verify Debug_FLASH/test_prj.elf [--device NXP_S32K312] [--port 7224]
"""
import argparse
import glob
import re
import socket
import subprocess
import sys
import time
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    if _s.encoding and _s.encoding.lower().replace('-', '') != 'utf8':
        try:
            _s.reconfigure(encoding='utf-8', errors='replace')
        except Exception:
            pass

PROBE_DIR = Path(__file__).resolve().parent.parent


def die(msg):
    print(f"[pemicro] ERROR: {msg}", file=sys.stderr)
    sys.exit(2)


def load_conf():
    conf = {}
    path = PROBE_DIR / 'config' / 'pemicro.conf'
    if path.exists():
        for line in path.read_text(encoding='utf-8').splitlines():
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                conf[k.strip()] = v.strip().strip('"').strip("'")
    return conf


def find_s32ds_root(conf):
    if conf.get('S32DS_ROOT'):
        p = Path(conf['S32DS_ROOT'])
        if p.is_dir():
            return p
        die(f"config S32DS_ROOT 不存在: {p}")
    for drive in ('C:', 'D:'):
        for p in sorted(glob.glob(f"{drive}/NXP/S32DS.*"), reverse=True):
            # 完整安装: <root>/eclipse/plugins(IDE+调试插件); 命令行安装: <root>/S32DS/build_tools
            if Path(p, 'eclipse', 'plugins').is_dir() or Path(p, 'S32DS', 'build_tools').is_dir():
                return Path(p)
    die("未找到 S32DS 安装目录（扫过 C:/NXP/S32DS.* 与 D:/NXP/S32DS.*）。"
        "复制 config/pemicro.conf.example 为 config/pemicro.conf 并设置 S32DS_ROOT。")


def find_pegdbserver(root, conf):
    if conf.get('PEGDBSERVER'):
        p = Path(conf['PEGDBSERVER'])
        if p.is_file():
            return p
        die(f"config PEGDBSERVER 不存在: {p}")
    plugins = Path(root, 'eclipse', 'plugins')
    import re
    best, best_ver = None, (0, 0, 0)
    for plug in plugins.glob('com.pemicro.debug.gdbjtag.pne*'):
        m = re.search(r'(\d+)\.(\d+)\.(\d+)', plug.name)
        ver = tuple(int(x) for x in m.groups()) if m else (0, 0, 0)
        for name in ('pegdbserver_console.exe', 'pegdbserver_console'):
            for sub in ('win32', 'lin64', ''):
                exe = plug / sub / name if sub else plug / name
                if exe.is_file() and ver >= best_ver:
                    best, best_ver = exe, ver
    if best:
        return best
    die(f"pegdbserver_console 不在 {plugins}/com.pemicro.debug.gdbjtag.pne*/ 下，"
        "请在 config/pemicro.conf 设置 PEGDBSERVER。")


def find_gdb(root, conf):
    if conf.get('GDB'):
        p = Path(conf['GDB'])
        if p.is_file():
            return p
        die(f"config GDB 不存在: {p}")
    import re
    best, best_ver = None, (0, 0)
    for g in Path(root, 'S32DS', 'build_tools').glob('gcc_v*/gcc-*/bin/arm-none-eabi-gdb.exe'):
        m = re.search(r'gcc_v(\d+)\.(\d+)', str(g.parent.parent.parent.name))
        ver = tuple(int(x) for x in m.groups()) if m else (0, 0)
        if g.is_file() and ver >= best_ver:
            best, best_ver = g, ver
    if best:
        return best
    die(f"arm-none-eabi-gdb.exe 不在 {root}/S32DS/build_tools/gcc_v*/ 下，"
        "请在 config/pemicro.conf 设置 GDB。")


class GdbServer:
    """pegdbserver_console 子进程: 端口就绪后进入 gdb, 退出时关闭。"""

    def __init__(self, exe, device, interface, port):
        self.argv = [str(exe), '-startserver', f'-device={device}',
                     f'-interface={interface}', f'-serverport={port}']
        self.port = port
        self.proc = None

    def __enter__(self):
        print('[run]', ' '.join(self.argv))
        self.proc = subprocess.Popen(
            self.argv, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, errors='replace')
        deadline = time.time() + 20
        while time.time() < deadline:
            if self.proc.poll() is not None:
                out = self.proc.stdout.read() if self.proc.stdout else ''
                die('pegdbserver_console 提前退出:\n' + out)
            s = socket.socket()
            s.settimeout(1)
            try:
                s.connect(('127.0.0.1', self.port))
                return self
            except OSError:
                time.sleep(0.5)
            finally:
                s.close()
        self._stop()
        die(f'pegdbserver 端口 {self.port} 20s 内未就绪：检查探针连接/供电/接口类型'
            f'（config INTERFACE 当前配置见 pemicro.conf）。')

    def _stop(self):
        if self.proc and self.proc.poll() is None:
            self.proc.terminate()
            try:
                self.proc.wait(5)
            except Exception:
                self.proc.kill()

    def __exit__(self, *exc):
        self._stop()
        return False


def run_gdb(gdb, port, gdb_cmds, timeout=300, keep_halted=False):
    """keep_halted=True 时结尾用 disconnect(不恢复运行)，默认 detach(恢复运行)。"""
    argv = [str(gdb), '-batch', '-nx',
            '-ex', 'set confirm off',
            '-ex', f'target remote 127.0.0.1:{port}']
    for c in gdb_cmds:
        argv += ['-ex', c]
    tail = 'disconnect' if keep_halted else 'detach'
    argv += ['-ex', tail, '-ex', 'quit']
    print('[run]', ' '.join(argv))
    try:
        r = subprocess.run(argv, capture_output=True, text=True,
                           encoding='utf-8', errors='replace', timeout=timeout)
    except FileNotFoundError:
        die(f"找不到 gdb: {gdb}")
    print(r.stdout)
    if r.stderr:
        print(r.stderr, file=sys.stderr)
    return r


# ---- 命令行调试（对齐 probes/jlink 的 jlink_cmd） ----
# 位域解析复用 J-Link 侧实现，保持两探针分析口径一致
sys.path.insert(0, str(PROBE_DIR.parent / 'jlink' / 'scripts'))
from dump_cortex import CORTEX_REGS, analyze_fault  # noqa: E402

RE_GDB_REG = re.compile(r'^\s*(\w+)\s+(0x[0-9A-Fa-f]+)')
RE_GDB_MEM = re.compile(r'(0x[0-9A-Fa-f]+):\s*(0x[0-9A-Fa-f]+)')


def parse_int(s):
    try:
        return int(s, 0)  # 支持 0x.. / 十进制
    except ValueError:
        die(f"数值格式错误: {s!r}（支持 0x 十六进制或十进制）")


def cmd_dump_cortex(gdb, port):
    """HardFault 现场导出：核心寄存器 + CFSR/HFSR 位域解析（口径同 J-Link dump_cortex）。"""
    mem_cmds = [f'x/1wx {addr}' for addr in CORTEX_REGS.values()]
    r = run_gdb(gdb, port, ['monitor halt', 'info registers'] + mem_cmds, keep_halted=True)
    if r.returncode != 0:
        sys.exit(r.returncode)
    out = r.stdout
    regs = {}
    for line in out.splitlines():
        m = RE_GDB_REG.match(line)
        if m:
            regs[m.group(1).upper()] = m.group(2)
    mems = {m.group(1).upper(): m.group(2) for m in RE_GDB_MEM.finditer(out)}
    addr_map = {v.upper(): k for k, v in CORTEX_REGS.items()}
    fault_regs = {addr_map.get(addr, addr): val for addr, val in mems.items()}

    print('=== Cortex-M 异常状态 ===')
    print('\n--- 核心寄存器 ---')
    for name in ['PC', 'LR', 'SP', 'XPSR', 'R0', 'R1', 'R2', 'R3', 'R12']:
        if name in regs:
            print(f'  {name:6s} = {regs[name]}')
    print('\n--- 异常寄存器 ---')
    for name, val in fault_regs.items():
        print(f'  {name:6s} = {val}')
    cfsr = fault_regs.get('CFSR', '0x00000000')
    hfsr = fault_regs.get('HFSR', '0x00000000')
    reasons = analyze_fault(cfsr, hfsr)
    if reasons:
        print('\n--- 异常分析 ---')
        for reason in reasons:
            print(f'  * {reason}')
    else:
        print('\n--- 无异常 ---')


def main():
    ap = argparse.ArgumentParser(description='PEmicro 探针: 烧录 + 命令行调试')
    ap.add_argument('op', choices=['download', 'erase', 'reset', 'verify',
                                   'halt', 'go', 'regs', 'read_mem', 'write_mem', 'dump_cortex'])
    ap.add_argument('file', nargs='?', help='elf(hex) 文件路径')
    ap.add_argument('--device', default='')
    ap.add_argument('--interface', default='')
    ap.add_argument('--port', type=int, default=0)
    ap.add_argument('--address', default='', help='read_mem/write_mem 目标地址')
    ap.add_argument('--size', default='16', help='read_mem 读取字数(4字节/字)')
    ap.add_argument('--value', default='', help='write_mem 写入值(32位)')
    a = ap.parse_args()

    conf = load_conf()
    root = find_s32ds_root(conf)
    server_exe = find_pegdbserver(root, conf)
    gdb = find_gdb(root, conf)
    device = a.device or conf.get('DEVICE', 'NXP_S32K312')
    interface = a.interface or conf.get('INTERFACE', 'usbmultilink')
    port = a.port or int(conf.get('PORT', '7224') or 7224)
    print(f"[pemicro] device={device} interface={interface} port={port}")
    print(f"[pemicro] server={server_exe}")
    print(f"[pemicro] gdb={gdb}")

    if a.op in ('download', 'verify'):
        if not a.file:
            die(f"{a.op} 需要文件参数，例: pemicro_ops.py {a.op} Debug_FLASH/test_prj.elf")
        f = Path(a.file)
        if not f.is_file():
            die(f"文件不存在: {f.resolve()}")
        f = f.resolve()

    # 调试命令参数校验（提前到起 server 前，失败不占探针）
    if a.op in ('read_mem', 'write_mem') and not a.address:
        die(f"{a.op} 需要 --address 0x....")
    if a.op == 'write_mem' and not a.value:
        die("write_mem 需要 --value 0x....")

    with GdbServer(server_exe, device, interface, port):
        if a.op == 'download':
            r = run_gdb(gdb, port, ['monitor halt', f'load {f}', 'monitor reset'])
            ok = r.returncode == 0 and 'Load failed' not in r.stdout and 'Error' not in r.stdout
            print('[OK] 下载成功并复位运行' if ok else '[ERROR] 下载失败')
            sys.exit(0 if ok else 1)
        if a.op == 'erase':
            r = run_gdb(gdb, port, ['monitor erase', 'monitor reset'])
            ok = r.returncode == 0
            print('[OK] 整片擦除完成' if ok else '[ERROR] 擦除失败')
            sys.exit(0 if ok else 1)
        if a.op == 'reset':
            r = run_gdb(gdb, port, ['monitor reset'])
            sys.exit(r.returncode)
        if a.op == 'verify':
            if f.suffix.lower() != '.elf':
                die('verify 仅支持 .elf（gdb compare-sections 依赖段信息）')
            r = run_gdb(gdb, port, ['monitor halt', 'compare-sections'], keep_halted=True)
            ok = r.returncode == 0 and 'MIS-MATCH' not in r.stdout
            print('[OK] Flash 与 ELF 一致' if ok else '[ERROR] 存在不一致段')
            sys.exit(0 if ok else 1)

        # ---- 调试命令 ----
        if a.op == 'halt':
            r = run_gdb(gdb, port, ['monitor halt'], keep_halted=True)
            sys.exit(r.returncode)
        if a.op == 'go':
            r = run_gdb(gdb, port, ['monitor go'])
            sys.exit(r.returncode)
        if a.op == 'regs':
            r = run_gdb(gdb, port, ['monitor halt', 'info registers'], keep_halted=True)
            sys.exit(r.returncode)
        if a.op == 'read_mem':
            n = parse_int(a.size)
            r = run_gdb(gdb, port, ['monitor halt', f'x/{n}wx {a.address}'], keep_halted=True)
            sys.exit(r.returncode)
        if a.op == 'write_mem':
            addr = parse_int(a.address)
            val = parse_int(a.value)
            if not 0 <= val <= 0xFFFFFFFF:
                die('write_mem 值必须 32 位以内')
            r = run_gdb(gdb, port,
                        ['monitor halt', f'set {{unsigned int}}{addr} = {val}'],
                        keep_halted=True)
            sys.exit(r.returncode)
        # dump_cortex
        cmd_dump_cortex(gdb, port)


if __name__ == '__main__':
    main()
