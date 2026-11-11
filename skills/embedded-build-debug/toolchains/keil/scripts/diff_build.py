#!/usr/bin/env python3
"""对比两次编译的size差异"""
import sys, json
from parse_build_log import parse

def diff(old_log, new_log):
    old = parse(old_log)
    new = parse(new_log)

    result = {'memory_diff': {}, 'warnings': {}, 'errors': {}}
    for key in ['Code', 'RO-data', 'RW-data', 'ZI-data']:
        o = old['memory'].get(key, 0)
        n = new['memory'].get(key, 0)
        d = n - o
        if d != 0:
            result['memory_diff'][key] = {'old': o, 'new': n, 'delta': d}

    result['warnings'] = {'old': old['warning_count'], 'new': new['warning_count'], 'delta': new['warning_count'] - old['warning_count']}
    result['errors'] = {'old': old['error_count'], 'new': new['error_count'], 'delta': new['error_count'] - old['error_count']}
    result['compile_time'] = {'old': old['compile_time_sec'], 'new': new['compile_time_sec']}
    return result

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("用法: python diff_build.py <old_build.log> <new_build.log>", file=sys.stderr)
        sys.exit(1)
    print(json.dumps(diff(sys.argv[1], sys.argv[2]), ensure_ascii=False, indent=2))
