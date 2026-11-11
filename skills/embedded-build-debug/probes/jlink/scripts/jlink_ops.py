#!/usr/bin/env python3
"""J-Link 探针基础操作: erase / verify / reset（复用 flash_loader 的执行器）"""
import argparse, json, subprocess, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from flash_loader import run_jlink, erase_range, verify_flash


def flash_range(linker):
    """链接脚本 -> (flash_start, flash_size)；解析失败返回 None"""
    if not linker:
        return None
    script = Path(__file__).parent / 'parse_linker.py'
    try:
        r = subprocess.run([sys.executable, str(script), linker, '--json'],
                           capture_output=True, text=True, timeout=15)
        if r.returncode != 0:
            return None
        info = json.loads(r.stdout)
        return int(info['flash_start'], 16), info['flash_size']
    except Exception:
        return None


def main():
    p = argparse.ArgumentParser(description='J-Link 探针: erase/verify/reset')
    p.add_argument('op', choices=['erase', 'verify', 'reset'])
    p.add_argument('--jlink', required=True)
    p.add_argument('--device', required=True)
    p.add_argument('--file', default='', help='verify 用: hex/bin 文件')
    p.add_argument('--linker', default='', help='链接脚本, 解析 Flash 范围')
    a = p.parse_args()

    if a.op == 'reset':
        out, err, code = run_jlink(a.jlink, a.device, ['connect', 'r', 'g', 'q'], timeout=15)
        print(out)
        if err:
            print(err, file=sys.stderr)
        sys.exit(code)

    rng = flash_range(a.linker)

    if a.op == 'erase':
        if rng:
            start, size = rng
            ok = erase_range(a.jlink, a.device, start, size)
        else:
            print('[INFO] 未提供/无法解析链接脚本, 执行整片擦除')
            out, err, code = run_jlink(a.jlink, a.device, ['connect', 'erase', 'q'], timeout=120)
            print(out)
            ok = 'O.K.' in out or 'Erasing done' in out
        sys.exit(0 if ok else 1)

    # verify
    if not a.file:
        print('错误: verify 需要 --file <hex|bin>', file=sys.stderr)
        sys.exit(2)
    base = rng[0] if rng else 0x8000
    ok = verify_flash(a.jlink, a.device, a.file, base)
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
