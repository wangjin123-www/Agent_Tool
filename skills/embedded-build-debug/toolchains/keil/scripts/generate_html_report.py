#!/usr/bin/env python3
"""生成Keil调试统一HTML报告"""
import sys, json, re
from pathlib import Path
from datetime import datetime

def load_json(path):
    try:
        return json.loads(Path(path).read_text(encoding='utf-8'))
    except:
        return {}

def generate_html(output_dir):
    out = Path(output_dir)
    summary = load_json(out / 'build_summary.json')
    history = load_json(out / 'history.json')
    errors_path = out / 'errors.log'

    # 检查Flash占用
    map_file = out.parent / 'MDK' / 'output' / 'debug' / 'DAB.map'
    flash_info = {}
    if map_file.exists():
        from check_flash_usage import parse_map
        flash_info = parse_map(str(map_file), 256, 192)

    # 状态样式
    success = summary.get('success', False)
    status_color = '#10b981' if success else '#ef4444'
    status_text = '编译成功' if success else '编译失败'
    error_count = summary.get('error_count', 0)
    warning_count = summary.get('warning_count', 0)

    # 内存数据
    mem = summary.get('memory', {})
    code_size = mem.get('Code', 0)
    ro_size = mem.get('RO-data', 0)
    rw_size = mem.get('RW-data', 0)
    zi_size = mem.get('ZI-data', 0)
    flash_total = code_size + ro_size
    ram_total = rw_size + zi_size

    # 历史数据（最近20次）
    builds = history.get('last_10', []) if isinstance(history, dict) else (history[-20:] if isinstance(history, list) else [])
    trend_points = []
    for b in builds[-20:]:
        m = b.get('memory', {})
        flash = m.get('Code', 0) + m.get('RO-data', 0)
        trend_points.append(flash)

    # 错误列表
    errors = summary.get('errors', [])
    warnings = summary.get('warnings', [])

    html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Keil调试报告 - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #f5f5f5; padding: 20px; }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        .header {{ background: white; border-radius: 8px; padding: 20px; margin-bottom: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        .status {{ display: inline-block; padding: 8px 16px; border-radius: 20px; color: white; font-weight: bold; font-size: 18px; }}
        .status.success {{ background: {status_color}; }}
        .status.fail {{ background: #ef4444; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 20px; }}
        .card {{ background: white; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        .card h3 {{ font-size: 14px; color: #666; margin-bottom: 10px; text-transform: uppercase; letter-spacing: 0.5px; }}
        .stat-value {{ font-size: 32px; font-weight: bold; color: #1f2937; }}
        .stat-unit {{ font-size: 14px; color: #9ca3af; margin-left: 4px; }}
        .progress-bar {{ height: 8px; background: #e5e7eb; border-radius: 4px; overflow: hidden; margin-top: 10px; }}
        .progress-fill {{ height: 100%; background: #3b82f6; transition: width 0.3s; }}
        .progress-fill.warning {{ background: #f59e0b; }}
        .progress-fill.danger {{ background: #ef4444; }}
        .error-list {{ max-height: 300px; overflow-y: auto; }}
        .error-item {{ padding: 10px; margin: 5px 0; background: #fee2e2; border-left: 4px solid #ef4444; border-radius: 4px; font-family: monospace; font-size: 12px; }}
        .warning-item {{ padding: 10px; margin: 5px 0; background: #fef3c7; border-left: 4px solid #f59e0b; border-radius: 4px; font-family: monospace; font-size: 12px; }}
        .empty {{ padding: 20px; text-align: center; color: #9ca3af; }}
        .chart {{ height: 200px; display: flex; align-items: flex-end; gap: 4px; padding-top: 20px; }}
        .chart-bar {{ flex: 1; background: #3b82f6; border-radius: 2px 2px 0 0; min-width: 8px; transition: height 0.3s; position: relative; }}
        .chart-bar:hover {{ background: #2563eb; }}
        .timestamp {{ font-size: 12px; color: #9ca3af; margin-top: 10px; }}
        .section {{ margin-bottom: 20px; }}
        .section-title {{ font-size: 16px; font-weight: bold; margin-bottom: 15px; color: #1f2937; }}
        .badge {{ display: inline-block; padding: 2px 8px; border-radius: 10px; font-size: 12px; margin-left: 10px; }}
        .badge.error {{ background: #fee2e2; color: #dc2626; }}
        .badge.warning {{ background: #fef3c7; color: #d97706; }}
        .memory-table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
        .memory-table th {{ text-align: left; padding: 8px; border-bottom: 2px solid #e5e7eb; color: #666; font-size: 12px; }}
        .memory-table td {{ padding: 8px; border-bottom: 1px solid #f3f4f6; font-size: 14px; }}
        .memory-table .num {{ text-align: right; font-family: monospace; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1 style="margin-bottom: 10px;">Keil MDK 编译报告</h1>
            <div style="display: flex; align-items: center; gap: 20px;">
                <span class="status {'success' if success else 'fail'}">{status_text}</span>
                <span class="timestamp">生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</span>
                <span class="timestamp">目标: {summary.get('target', 'Unknown')}</span>
                <span class="timestamp">编译器: {summary.get('compiler', 'Unknown')}</span>
            </div>
        </div>

        <div class="grid">
            <div class="card">
                <h3>编译结果</h3>
                <div style="display: flex; align-items: baseline; gap: 10px;">
                    <span class="stat-value">{error_count}</span>
                    <span class="stat-unit">错误</span>
                </div>
                <div style="display: flex; align-items: baseline; gap: 10px; margin-top: 10px;">
                    <span class="stat-value">{warning_count}</span>
                    <span class="stat-unit">警告</span>
                </div>
                <div class="timestamp">耗时: {summary.get('compile_time_sec', 0)}秒</div>
            </div>

            <div class="card">
                <h3>Flash占用</h3>
                <div style="display: flex; align-items: baseline;">
                    <span class="stat-value">{flash_info.get('flash_used_kb', 0)}</span>
                    <span class="stat-unit">/ {flash_info.get('flash_total_kb', 256)} KB</span>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill {'danger' if flash_info.get('warning_flash') else ''}" style="width: {flash_info.get('flash_percent', 0)}%"></div>
                </div>
                <div class="timestamp">{flash_info.get('flash_percent', 0)}%</div>
            </div>

            <div class="card">
                <h3>RAM占用</h3>
                <div style="display: flex; align-items: baseline;">
                    <span class="stat-value">{flash_info.get('ram_used_kb', 0)}</span>
                    <span class="stat-unit">/ {flash_info.get('ram_total_kb', 192)} KB</span>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill {'danger' if flash_info.get('warning_ram') else ''}" style="width: {flash_info.get('ram_percent', 0)}%"></div>
                </div>
                <div class="timestamp">{flash_info.get('ram_percent', 0)}%</div>
            </div>

            <div class="card">
                <h3>内存分布</h3>
                <table class="memory-table">
                    <tr><th>类型</th><th class="num">大小</th></tr>
                    <tr><td>Code</td><td class="num">{code_size}</td></tr>
                    <tr><td>RO-data</td><td class="num">{ro_size}</td></tr>
                    <tr><td>RW-data</td><td class="num">{rw_size}</td></tr>
                    <tr><td>ZI-data</td><td class="num">{zi_size}</td></tr>
                </table>
            </div>
        </div>

        <div class="grid">
            <div class="card" style="grid-column: span 2;">
                <h3>编译历史趋势 (Flash大小)</h3>
                <div class="chart">
'''

    # 添加趋势图
    if trend_points:
        max_val = max(trend_points) if trend_points else 1
        for i, val in enumerate(trend_points):
            height = (val / max_val * 100) if max_val > 0 else 0
            html += f'<div class="chart-bar" style="height: {height}%;" title="{val} bytes"></div>'
    else:
        html += '<div class="empty">暂无历史数据</div>'

    html += f'''
                </div>
                <div class="timestamp">最近{len(trend_points)}次编译</div>
            </div>
        </div>

        <div class="section">
            <div class="section-title">
                错误列表
                <span class="badge error">{len(errors)}</span>
            </div>
            <div class="card error-list">
'''

    if errors:
        for err in errors[:50]:
            html += f'<div class="error-item">{err}</div>'
        if len(errors) > 50:
            html += f'<div class="empty">... 还有 {len(errors)-50} 条错误</div>'
    else:
        html += '<div class="empty">无错误</div>'

    html += '''
            </div>
        </div>

        <div class="section">
            <div class="section-title">
                警告列表
                <span class="badge warning">''' + str(len(warnings)) + '''</span>
            </div>
            <div class="card error-list">
'''

    if warnings:
        for warn in warnings[:50]:
            html += f'<div class="warning-item">{warn}</div>'
        if len(warnings) > 50:
            html += f'<div class="empty">... 还有 {len(warnings)-50} 条警告</div>'
    else:
        html += '<div class="empty">无警告</div>'

    html += '''
            </div>
        </div>
    </div>
</body>
</html>'''

    report_path = out / 'report.html'
    report_path.write_text(html, encoding='utf-8')
    print(json.dumps({'report_path': str(report_path), 'success': True}, ensure_ascii=False))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python generate_html_report.py <output_dir>", file=sys.stderr)
        sys.exit(1)
    generate_html(sys.argv[1])
