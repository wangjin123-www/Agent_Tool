#!/usr/bin/env python3
"""解析Keil编译日志，输出结构化JSON"""
import sys, re, json
from pathlib import Path

def parse(log_path):
    text = Path(log_path).read_text(encoding='utf-8', errors='ignore')

    errors = []
    warnings = []
    summary_re = re.compile(r'\d+\s+Error\(s\),\s*\d+\s+Warning\(s\)')
    for line in text.split('\n'):
        s = line.strip()
        if summary_re.search(s):
            continue
        if re.search(r'\berror\b', s, re.IGNORECASE):
            errors.append(s)
        elif re.search(r'\bwarning\b', s, re.IGNORECASE):
            warnings.append(s)

    mem = {}
    for key in ['Code', 'RO-data', 'RW-data', 'ZI-data']:
        m = re.search(rf'{re.escape(key)}=(\d+)', text)
        mem[key] = int(m.group(1)) if m else 0

    time_m = re.search(r'Build Time Elapsed:\s+(\d+):(\d+):(\d+)', text)
    compile_time = int(time_m.group(1))*3600 + int(time_m.group(2))*60 + int(time_m.group(3)) if time_m else 0

    success_line = re.search(r'(\d+)\s+Error\(s\),\s*(\d+)\s+Warning\(s\)', text)
    success = success_line and success_line.group(1) == '0'

    target_m = re.search(r"Build target '([^']+)'", text)
    compiler_m = re.search(r'ARM Compiler (V\d+\S+)', text)

    return {
        'success': success,
        'errors': errors,
        'warnings': warnings,
        'error_count': len(errors),
        'warning_count': len(warnings),
        'memory': mem,
        'compile_time_sec': compile_time,
        'target': target_m.group(1) if target_m else 'Unknown',
        'compiler': compiler_m.group(1) if compiler_m else 'Unknown',
    }

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python parse_build_log.py <build.log>", file=sys.stderr)
        sys.exit(1)
    print(json.dumps(parse(sys.argv[1]), ensure_ascii=False, indent=2))
