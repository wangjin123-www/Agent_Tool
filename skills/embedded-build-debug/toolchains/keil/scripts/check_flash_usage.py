#!/usr/bin/env python3
"""解析map文件，输出Flash/RAM占用JSON"""
import sys, re, json
from pathlib import Path

def parse_map(map_path, flash_kb=256, ram_kb=192):
    text = Path(map_path).read_text(encoding='utf-8', errors='ignore')

    mem = {}
    for key in ['Code', 'RO-data', 'RW-data', 'ZI-data']:
        m = re.search(rf'{re.escape(key)}\s+(\d+)', text)
        mem[key] = int(m.group(1)) if m else 0

    flash_bytes = mem.get('Code', 0) + mem.get('RO-data', 0)
    ram_bytes = mem.get('RW-data', 0) + mem.get('ZI-data', 0)
    flash_used_kb = flash_bytes / 1024
    ram_used_kb = ram_bytes / 1024

    return {
        'flash_total_kb': flash_kb,
        'flash_used_kb': round(flash_used_kb, 1),
        'flash_percent': round(flash_used_kb / flash_kb * 100, 1),
        'ram_total_kb': ram_kb,
        'ram_used_kb': round(ram_used_kb, 1),
        'ram_percent': round(ram_used_kb / ram_kb * 100, 1),
        'sections': {k: v for k, v in mem.items()},
        'warning_flash': flash_used_kb / flash_kb > 0.9,
        'warning_ram': ram_used_kb / ram_kb > 0.9,
    }

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python check_flash_usage.py <map_file> [flash_kb] [ram_kb]", file=sys.stderr)
        sys.exit(1)
    flash_kb = int(sys.argv[2]) if len(sys.argv) > 2 else 256
    ram_kb = int(sys.argv[3]) if len(sys.argv) > 3 else 192
    print(json.dumps(parse_map(sys.argv[1], flash_kb, ram_kb), ensure_ascii=False, indent=2))
