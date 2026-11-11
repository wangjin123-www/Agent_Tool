#!/usr/bin/env python3
"""解析链接脚本获取Flash地址范围"""
import re, sys, os, argparse
from pathlib import Path

def parse_sct(content):
    """解析Keil sct文件"""
    # 匹配 LR_IROM1 0x00008000 0x00038000
    pattern = r'LR_IROM1\s+(0x[0-9A-Fa-f]+)\s+(0x[0-9A-Fa-f]+)'
    match = re.search(pattern, content)
    if match:
        return int(match.group(1), 16), int(match.group(2), 16)
    return None, None

def parse_ld(content):
    """解析GCC ld文件"""
    # 匹配 MEMORY 中的 FLASH 或 ROM
    flash_pattern = r'(?:FLASH|ROM|ROM\s*\(\s*rx\s*\))\s*:\s*ORIGIN\s*=\s*(0x[0-9A-Fa-f]+),\s*LENGTH\s*=\s*(0x[0-9A-Fa-f]+|\d+K?\d*)'
    match = re.search(flash_pattern, content, re.IGNORECASE)
    if match:
        origin = int(match.group(1), 16)
        length = match.group(2)
        if 'K' in length.upper():
            length = int(length.upper().replace('K', '')) * 1024
        elif 'M' in length.upper():
            length = int(length.upper().replace('M', '')) * 1024 * 1024
        else:
            length = int(length, 16) if length.startswith('0x') else int(length)
        return origin, length
    return None, None

def parse_linker_script(file_path):
    """解析链接脚本文件"""
    path = Path(file_path)
    if not path.exists():
        # 尝试默认路径
        default_paths = [
            Path("MDK/config/linker/HC32F460xE.sct"),
            Path("GCC/config/linker/HC32F460xE.ld"),
        ]
        for p in default_paths:
            if p.exists():
                path = p
                break

    if not path.exists():
        return None, None, f"文件不存在: {file_path}"

    content = path.read_text(encoding='utf-8', errors='ignore')

    if path.suffix.lower() == '.sct':
        addr, size = parse_sct(content)
    elif path.suffix.lower() == '.ld':
        addr, size = parse_ld(content)
    else:
        # 尝试两种格式
        addr, size = parse_sct(content)
        if addr is None:
            addr, size = parse_ld(content)

    if addr is not None and size is not None:
        end_addr = addr + size
        return addr, end_addr, None
    return None, None, "无法解析地址范围"

def main():
    p = argparse.ArgumentParser()
    p.add_argument('file', nargs='?', default='', help='链接脚本文件路径')
    p.add_argument('--json', action='store_true', help='输出JSON格式')
    args = p.parse_args()

    addr, end_addr, error = parse_linker_script(args.file)

    if error:
        print(error, file=sys.stderr)
        sys.exit(1)

    if args.json:
        import json
        print(json.dumps({
            "flash_start": f"0x{addr:08X}",
            "flash_end": f"0x{end_addr:08X}",
            "flash_size": end_addr - addr
        }))
    else:
        print(f"0x{addr:08X}", f"0x{end_addr:08X}")

if __name__ == '__main__':
    main()
