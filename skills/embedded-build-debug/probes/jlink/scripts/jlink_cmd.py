#!/usr/bin/env python3
"""通用JLink交互脚本，动态生成.jlink并执行"""
import argparse, subprocess, sys, tempfile, os
from pathlib import Path

COMMANDS = {
    'halt':    ['h'],
    'go':      ['g'],
    'regs':    ['r', 'regs'],
    'reset':   ['r'],
    'step':    ['step'],
}

def build_script(args):
    lines = ['connect']
    if args.command in COMMANDS:
        lines.extend(COMMANDS[args.command])
    elif args.command == 'read_mem':
        lines.extend(['r', f'mem32 {args.address} {args.size}'])
    elif args.command == 'write_mem':
        lines.extend(['r', f'w4 {args.address} {args.value}'])
    elif args.command == 'bp':
        lines.extend(['r', f'bp {args.address}'])
    elif args.command == 'read_reg':
        lines.extend(['r', f'reg {args.register}'])
    lines.append('q')
    return '\n'.join(lines)

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--jlink', required=True)
    p.add_argument('--device', required=True)
    p.add_argument('--command', required=True,
                   choices=['halt','go','regs','reset','step','read_mem','write_mem','bp','read_reg'])
    p.add_argument('--address', default='0x20000000')
    p.add_argument('--size', default='0x40')
    p.add_argument('--value', default='0x0')
    p.add_argument('--register', default='')
    args = p.parse_args()

    script = build_script(args)

    with tempfile.NamedTemporaryFile(mode='w', suffix='.jlink', delete=False, encoding='utf-8') as f:
        f.write(script)
        tmp = f.name

    try:
        result = subprocess.run(
            [args.jlink, '-device', args.device, '-if', 'SWD', '-speed', '4000', '-CommanderScript', tmp],
            capture_output=True, text=True, timeout=30
        )
        print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        sys.exit(result.returncode)
    finally:
        os.unlink(tmp)

if __name__ == '__main__':
    main()
