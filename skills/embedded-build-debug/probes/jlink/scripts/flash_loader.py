#!/usr/bin/env python3
"""参数化Flash下载脚本，支持完整流程和验证"""
import argparse, subprocess, sys, tempfile, os, json
from pathlib import Path

def load_config(config_file):
    """加载配置文件"""
    config = {}
    if os.path.exists(config_file):
        with open(config_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    config[key.strip()] = value.strip().strip('"').strip("'")
    return config

def run_jlink(jlink, device, commands, timeout=60):
    """执行J-Link命令"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.jlink', delete=False, encoding='utf-8') as f:
        f.write('\n'.join(commands))
        tmp = f.name

    try:
        result = subprocess.run(
            [jlink, '-device', device, '-if', 'SWD', '-speed', '4000', '-CommanderScript', tmp],
            capture_output=True, text=True, timeout=timeout
        )
        return result.stdout, result.stderr, result.returncode
    finally:
        os.unlink(tmp)

def erase_range(jlink, device, addr, size):
    """擦除指定地址范围"""
    addr_hex = f"0x{addr:X}"
    print(f'\n=== 擦除Flash ===')
    print(f'地址: {addr_hex}')
    print(f'大小: {size:,} 字节 ({size//1024} KB)')

    commands = [
        'connect',
        f'erase {addr_hex} {size}',
        'q'
    ]
    stdout, stderr, code = run_jlink(jlink, device, commands, timeout=120)

    if 'Erasing done' in stdout or 'O.K.' in stdout:
        print('[OK] 擦除成功\n')
        return True
    else:
        print('[ERROR] 擦除失败\n', file=sys.stderr)
        return False

def hex_extract(hex_path, start_addr):
    """从 Intel HEX 中提取 start_addr 及之后的数据，返回 (bin_bytes, min_addr, max_addr_end)。"""
    data = {}
    upper = 0
    for line in open(hex_path, 'r', errors='ignore'):
        line = line.strip()
        if not line.startswith(':'):
            continue
        try:
            count = int(line[1:3], 16)
            addr = int(line[3:7], 16)
            typ = int(line[7:9], 16)
        except (ValueError, IndexError):
            continue
        if typ == 4:  # Extended Linear Address
            upper = int(line[9:13], 16) << 16
        elif typ == 2:  # Extended Segment Address
            upper = int(line[9:13], 16) << 4
        elif typ == 0:  # Data
            payload = bytes.fromhex(line[9:9 + count * 2])
            base = upper + addr
            for i, b in enumerate(payload):
                data[base + i] = b
        elif typ == 1:  # EOF
            break

    if not data:
        return b'', 0, 0

    lo = min(data)
    hi = max(data) + 1
    if hi <= start_addr:
        return b'', lo, hi

    # 只保留 start_addr 之后的数据
    keep_lo = max(lo, start_addr)
    size = hi - keep_lo
    out = bytearray(size)
    for a in range(keep_lo, hi):
        out[a - keep_lo] = data.get(a, 0xFF)
    return bytes(out), keep_lo, hi


def download_file(jlink, device, file_path, verify=True, slot_a=False):
    """下载文件到Flash"""
    file_path = os.path.abspath(file_path)
    file_size = os.path.getsize(file_path) if os.path.exists(file_path) else 0
    ext = os.path.splitext(file_path)[1].lower()

    print(f'\n=== 下载固件 ===')
    print(f'文件: {os.path.basename(file_path)}')
    print(f'路径: {file_path}')
    print(f'大小: {file_size:,} 字节 ({file_size//1024} KB)')
    print(f'设备: {device}')

    tmp_bin = None
    try:
        if slot_a:
            # Slot A 模式：只烧 0x8000 起（对应 Keil -FS08000），不碰 Flash 选项字节区 (0x400-0x7FFF)
            slot_a_base = 0x8000
            if ext == '.hex':
                bin_bytes, lo, hi = hex_extract(file_path, slot_a_base)
                if not bin_bytes:
                    print(f'[ERROR] hex 中 0x{slot_a_base:X} 之后无数据', file=sys.stderr)
                    return False
                with tempfile.NamedTemporaryFile(mode='wb', suffix='.bin', delete=False) as f:
                    f.write(bin_bytes)
                    tmp_bin = f.name
                load_cmd = f'loadbin "{tmp_bin}" 0x{slot_a_base:X}'
                verify_cmd = f'verifybin "{tmp_bin}" 0x{slot_a_base:X}'
                print(f'[INFO] Slot A 模式: 从 0x{slot_a_base:X} 开始编程 '
                      f'({len(bin_bytes):,} 字节, 0x{lo:X}-0x{hi:X})')
                print(f'[INFO] 跳过 Flash 选项字节区 (0x400-0x7FFF)')
            else:
                # bin 文件直接用
                load_cmd = f'loadbin {file_path} 0x{slot_a_base:X}'
                verify_cmd = f'verifybin {file_path} 0x{slot_a_base:X}'
        elif ext == '.hex':
            load_cmd = f'loadfile {file_path}'
            verify_cmd = f'verifyfile {file_path}'
        elif ext == '.bin':
            load_cmd = f'loadbin {file_path} 0x8000'  # 默认地址，可通过参数修改
            verify_cmd = f'verifybin {file_path} 0x8000'
        else:
            print(f'不支持的文件格式: {ext}', file=sys.stderr)
            return False

        commands = ['connect', 'r', 'h', load_cmd]
        if verify:
            commands.append(verify_cmd)
        commands.extend(['r', 'g', 'q'])

        stdout, stderr, code = run_jlink(jlink, device, commands, timeout=120)

        if 'O.K.' in stdout:
            print('[OK] 下载成功\n')
            return True
        else:
            print('[ERROR] 下载失败\n', file=sys.stderr)
            print(stderr, file=sys.stderr)
            return False
    finally:
        if tmp_bin and os.path.exists(tmp_bin):
            os.unlink(tmp_bin)

def read_flash(jlink, device, addr, size, output_file):
    """读取Flash内容"""
    print(f'\n=== 读取Flash ===')
    print(f'地址: 0x{addr:08X}')
    print(f'大小: {size:,} 字节')

    commands = [
        'connect',
        'r',
        'h',
        f'savebin {output_file} 0x{addr:08X} {size}',
        'q'
    ]

    stdout, stderr, code = run_jlink(jlink, device, commands, timeout=120)

    if os.path.exists(output_file):
        read_size = os.path.getsize(output_file)
        print(f'[OK] 读取成功: {output_file} ({read_size:,} 字节)\n')
        return True
    else:
        print('[ERROR] 读取失败\n', file=sys.stderr)
        return False

def verify_flash(jlink, device, file_path, flash_addr):
    """验证Flash内容与文件一致"""
    import hashlib

    print(f'\n=== 验证Flash ===')

    # 计算文件哈希
    with open(file_path, 'rb') as f:
        file_hash = hashlib.md5(f.read()).hexdigest()

    # 读取Flash
    temp_bin = tempfile.mktemp(suffix='.bin')
    if not read_flash(jlink, device, flash_addr, os.path.getsize(file_path), temp_bin):
        return False

    # 计算Flash哈希
    with open(temp_bin, 'rb') as f:
        flash_data = f.read()
        # 可能Flash读取的大小和文件不同，只比较文件大小部分
        flash_hash = hashlib.md5(flash_data[:os.path.getsize(file_path)]).hexdigest()

    os.unlink(temp_bin)

    if file_hash == flash_hash:
        print('[OK] 验证成功：Flash内容与文件一致\n')
        return True
    else:
        print('[ERROR] 验证失败：Flash内容与文件不一致\n', file=sys.stderr)
        return False

def full_flow(jlink, device, file_path, linker_script, config_dir, file_type=None):
    """完整流程：擦除→下载→运行→验证"""
    print('\n' + '='*50)
    print('       完整下载流程')
    print('='*50)

    # 解析链接脚本获取地址范围
    import subprocess
    parse_script = os.path.join(config_dir, 'scripts', 'parse_linker.py')
    result = subprocess.run(['python', parse_script, linker_script, '--json'],
                          capture_output=True, text=True, timeout=10)

    if result.returncode != 0:
        print(f'无法解析链接脚本: {linker_script}', file=sys.stderr)
        return False

    flash_info = json.loads(result.stdout)
    flash_start = int(flash_info['flash_start'], 16)
    flash_end = int(flash_info['flash_end'], 16)
    flash_size = flash_info['flash_size']

    print(f'\nFlash地址范围: 0x{flash_start:08X} - 0x{flash_end:08X}')
    print(f'Flash大小: {flash_size:,} 字节 ({flash_size//1024} KB)\n')

    # 选择文件类型
    if not file_type:
        try:
            print('请选择固件文件类型:')
            print('1. HEX (推荐，包含地址信息)')
            print('2. BIN (纯二进制，需要指定地址)')
            choice = input('请输入 [1/2]: ').strip()
            file_type = 'hex' if choice == '1' else 'bin'
        except (EOFError, OSError):
            # 非交互模式，默认使用 hex
            print('非交互模式，默认使用 HEX 文件\n')
            file_type = 'hex'

    # 步骤1: 擦除
    if not erase_range(jlink, device, flash_start, flash_size):
        return False

    # 步骤2: 下载
    if not download_file(jlink, device, file_path, verify=True):
        return False

    # 步骤3: 运行
    print('=== 启动MCU ===')
    stdout, stderr, code = run_jlink(jlink, device, ['connect', 'r', 'g', 'q'], timeout=10)
    if code == 0:
        print('[OK] MCU已启动运行\n')
    else:
        print('[WARN] 启动可能失败，请手动复位\n')

    # 步骤4: 验证
    # 注意：这里跳过验证，因为MCU已经在运行，读取可能会干扰
    print('[INFO] 跳过Flash验证（MCU正在运行）\n')

    print('='*50)
    print('       完整流程完成')
    print('='*50 + '\n')
    return True

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--jlink', required=True)
    p.add_argument('--device', required=True)
    p.add_argument('--file', help='hex/bin文件路径')
    p.add_argument('--config', default='', help='配置文件路径')
    p.add_argument('--linker', default='', help='链接脚本路径')
    p.add_argument('--addr', default='', help='bin文件下载地址')
    p.add_argument('--erase', action='store_true', help='擦除后下载')
    p.add_argument('--verify', action='store_true', help='下载后校验')
    p.add_argument('--reset', action='store_true', help='下载后复位运行')
    p.add_argument('--full', action='store_true', help='完整流程')
    p.add_argument('--file-type', choices=['hex', 'bin'], help='文件类型')
    p.add_argument('--slot-a', action='store_true', help='Slot A 模式: 只从 0x8000 开始编程，跳过 Flash 选项字节区')
    args = p.parse_args()

    # 加载配置
    config = load_config(args.config)

    # 完整流程
    if args.full:
        linker_script = args.linker or config.get('LINKER_SCRIPT', 'MDK/config/linker/HC32F460xE.sct')
        file_type = args.file_type

        if not file_type:
            # 询问文件类型
            try:
                print('\n请选择固件文件类型:')
                print('1. HEX (推荐，包含地址信息)')
                print('2. BIN (纯二进制，需要指定地址)')
                choice = input('请输入 [1/2]: ').strip()
                file_type = 'hex' if choice == '1' else 'bin'
            except (EOFError, OSError):
                # 非交互模式，默认使用 hex
                print('\n非交互模式，默认使用 HEX 文件')
                file_type = 'hex'

        if file_type == 'hex':
            file_path = config.get('HEX_PATH', 'MDK/output/debug/DAB.hex')
        else:
            file_path = config.get('BIN_PATH', 'MDK/output/debug/DAB.bin')

        # 使用 SKILL_DIR 环境变量
        skill_dir = os.environ.get(
            'SKILL_DIR', '.claude/skills/embedded-build-debug/probes/jlink')
        return 0 if full_flow(args.jlink, args.device, file_path, linker_script, skill_dir, file_type) else 1

    # 常规下载流程
    if not args.file:
        print('错误: 需要 --file 参数', file=sys.stderr)
        sys.exit(1)

    ok = download_file(args.jlink, args.device, args.file, verify=args.verify, slot_a=args.slot_a)
    if not ok:
        return 1

    if args.reset:
        stdout, stderr, code = run_jlink(args.jlink, args.device, ['connect', 'r', 'g', 'q'], timeout=10)
        if code == 0:
            print('[OK] MCU已启动运行\n')
        else:
            print('[WARN] 启动可能失败，请手动复位\n')
    return 0

if __name__ == '__main__':
    main()
