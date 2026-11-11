#!/usr/bin/env python3
"""记录编译历史，输出趋势JSON"""
import sys, json
from pathlib import Path
from datetime import datetime

def append(build_log_path, history_file):
    from parse_build_log import parse
    info = parse(build_log_path)

    entry = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'success': info['success'],
        'errors': info['error_count'],
        'warnings': info['warning_count'],
        'memory': info['memory'],
        'compile_time_sec': info['compile_time_sec'],
    }

    hist = []
    hpath = Path(history_file)
    if hpath.exists():
        try:
            hist = json.loads(hpath.read_text(encoding='utf-8'))
        except:
            hist = []

    hist.append(entry)
    hpath.write_text(json.dumps(hist, ensure_ascii=False, indent=2), encoding='utf-8')

    recent = hist[-10:]
    print(json.dumps({
        'total_builds': len(hist),
        'last_10': recent,
        'current': entry,
    }, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("用法: python log_history.py <build.log> <history.json>", file=sys.stderr)
        sys.exit(1)
    append(sys.argv[1], sys.argv[2])
