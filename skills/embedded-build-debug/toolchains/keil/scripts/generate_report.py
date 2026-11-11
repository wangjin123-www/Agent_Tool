#!/usr/bin/env python3
"""生成调试HTML报告"""
import sys, json
from datetime import datetime
from pathlib import Path

def read_file(p):
    try:
        return Path(p).read_text(encoding='utf-8', errors='ignore')
    except:
        return ''

def generate(output_dir):
    d = Path(output_dir)
    build_log = read_file(d / 'build_log.txt')
    errors_log = read_file(d / 'errors.log')
    core_dump = read_file(d / 'core_dump.txt')
    build_summary = read_file(d / 'build_summary.json')

    summary = json.loads(build_summary) if build_summary.strip() else {}
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>Keil Debug Report - {now}</title>
<style>
body {{ font-family: 'Segoe UI', sans-serif; background: #1a1a2e; color: #eee; margin: 20px; }}
.card {{ background: #16213e; border-radius: 8px; padding: 20px; margin-bottom: 16px; }}
h1 {{ color: #0f3460; background: #e94560; padding: 16px; border-radius: 8px; }}
h2 {{ color: #e94560; border-bottom: 1px solid #e94560; padding-bottom: 8px; }}
pre {{ background: #0f3460; padding: 16px; border-radius: 4px; overflow-x: auto; }}
.ok {{ color: #4ecca3; }} .err {{ color: #e94560; }} .warn {{ color: #f9ed69; }}
table {{ border-collapse: collapse; width: 100%; }}
th, td {{ padding: 8px 12px; text-align: left; border-bottom: 1px solid #333; }}
th {{ background: #0f3460; }}
</style>
</head>
<body>
<h1>Keil Debug Report</h1>
<p>{now}</p>

<div class="card">
<h2>Build Summary</h2>
<table>
<tr><th>Item</th><th>Value</th></tr>
<tr><td>Success</td><td class="{'ok' if summary.get('success') else 'err'}">{'YES' if summary.get('success') else 'NO'}</td></tr>
<tr><td>Errors</td><td class="err">{summary.get('error_count', 'N/A')}</td></tr>
<tr><td>Warnings</td><td class="warn">{summary.get('warning_count', 'N/A')}</td></tr>
<tr><td>Compile Time</td><td>{summary.get('compile_time_sec', 'N/A')}s</td></tr>
<tr><td>Target</td><td>{summary.get('target', 'N/A')}</td></tr>
</table>
</div>

<div class="card">
<h2>Memory Usage</h2>
<table>
<tr><th>Section</th><th>Bytes</th></tr>
"""
    for k, v in summary.get('memory', {}).items():
        html += f"<tr><td>{k}</td><td>{v}</td></tr>\n"
    html += """</table>
</div>

<div class="card">
<h2>Errors</h2>
<pre>""" + (errors_log or 'No errors') + """</pre>
</div>

<div class="card">
<h2>Core Dump</h2>
<pre>""" + (core_dump or 'No core dump') + """</pre>
</div>

<div class="card">
<h2>Full Build Log</h2>
<pre>""" + (build_log[:10000] or 'No log') + """</pre>
</div>
</body>
</html>"""

    out = d / f'debug_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.html'
    out.write_text(html, encoding='utf-8')
    print(f'Report: {out}')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python generate_report.py <output_dir>", file=sys.stderr)
        sys.exit(1)
    generate(sys.argv[1])
