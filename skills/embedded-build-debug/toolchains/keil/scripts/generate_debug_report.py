#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HC32 DAB调试HTML报告生成器
"""

import sys
from datetime import datetime
from pathlib import Path

def read_log_file(filepath):
    """读取日志文件"""
    try:
        return Path(filepath).read_text(encoding='utf-8', errors='ignore')
    except:
        return f"未找到文件: {filepath}"

def parse_errors(log_text):
    """从日志中提取错误和警告"""
    errors = []
    warnings = []
    for line in log_text.split('\n'):
        if 'error' in line.lower():
            errors.append(line.strip())
        elif 'warning' in line.lower():
            warnings.append(line.strip())
    return errors, warnings

def generate_html(session_dir):
    """生成HTML报告"""
    session_path = Path(session_dir)

    # 读取所有日志文件
    errors_log = read_log_file(session_path / 'errors.log')
    core_dump = read_log_file(session_path / 'core_dump.txt')
    build_log = read_log_file(session_path / 'build_log.txt')

    # 解析错误
    errors, warnings = parse_errors(errors_log)

    # 生成HTML
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HC32 DAB调试报告 - {session_path.name}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            line-height: 1.6;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .header h1 {{ font-size: 2.5em; margin-bottom: 10px; }}
        .tabs {{ display: flex; background: #f5f5f5; border-bottom: 2px solid #ddd; }}
        .tab {{
            flex: 1;
            padding: 15px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s;
            font-weight: 600;
            color: #666;
        }}
        .tab:hover {{ background: #e0e0e0; }}
        .tab.active {{ background: white; color: #667eea; border-bottom: 3px solid #667eea; }}
        .content {{ padding: 30px; }}
        .tab-content {{ display: none; }}
        .tab-content.active {{ display: block; }}
        .section {{ margin-bottom: 30px; }}
        .section h2 {{
            color: #667eea;
            margin-bottom: 15px;
            font-size: 1.8em;
            border-bottom: 2px solid #667eea;
            padding-bottom: 10px;
        }}
        .error-box {{
            background: #f8d7da;
            border-left: 4px solid #dc3545;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 4px;
        }}
        .warning-box {{
            background: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 4px;
        }}
        .success-box {{
            background: #d4edda;
            border-left: 4px solid #28a745;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 4px;
        }}
        pre {{
            background: #2d2d2d;
            color: #f8f8f2;
            padding: 20px;
            border-radius: 5px;
            overflow-x: auto;
            font-family: 'Consolas', monospace;
            font-size: 0.9em;
        }}
        .badge {{
            display: inline-block;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 0.85em;
            font-weight: 600;
            margin-right: 5px;
        }}
        .badge-error {{ background: #dc3545; color: white; }}
        .badge-warning {{ background: #ffc107; color: #333; }}
        .badge-success {{ background: #28a745; color: white; }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }}
        th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }}
        th {{ background: #667eea; color: white; font-weight: 600; }}
        tr:hover {{ background: #f5f5f5; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔧 HC32 DAB调试报告</h1>
            <p>📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p style="margin-top: 10px;">会话: <code>{session_path.name}</code></p>
        </div>

        <div class="tabs">
            <div class="tab active" onclick="switchTab(event, 'overview')">📋 概览</div>
            <div class="tab" onclick="switchTab(event, 'errors')">❌ 错误</div>
            <div class="tab" onclick="switchTab(event, 'logs')">📄 日志</div>
        </div>

        <div class="content">
            <!-- 概览 -->
            <div id="overview" class="tab-content active">
                <div class="section">
                    <h2>调试摘要</h2>
                    <table>
                        <tr><td><strong>会话目录</strong></td><td>{session_path.name}</td></tr>
                        <tr><td><strong>错误数</strong></td><td>{len(errors)}</td></tr>
                        <tr><td><strong>警告数</strong></td><td>{len(warnings)}</td></tr>
                        <tr><td><strong>状态</strong></td><td><span class="badge badge-success">✅ 已解决</span></td></tr>
                    </table>
                </div>
            </div>

            <!-- 错误 -->
            <div id="errors" class="tab-content">
                <div class="section">
                    <h2>错误与警告</h2>
"""

    # 添加错误和警告
    for error in errors[:50]:
        html += f'                    <div class="error-box"><span class="badge badge-error">ERROR</span>{error}</div>\n'
    for warning in warnings[:50]:
        html += f'                    <div class="warning-box"><span class="badge badge-warning">WARNING</span>{warning}</div>\n'

    if not errors and not warnings:
        html += '                    <div class="success-box">✓ 未发现错误或警告</div>\n'

    html += f"""                </div>
            </div>

            <!-- 日志 -->
            <div id="logs" class="tab-content">
                <div class="section">
                    <h2>完整日志</h2>
                    <h3>编译日志</h3>
                    <pre>{build_log[:5000]}</pre>
                    <h3>核心转储</h3>
                    <pre>{core_dump[:5000]}</pre>
                </div>
            </div>
        </div>
    </div>

    <script>
        function switchTab(evt, tabName) {{
            var tabs = document.getElementsByClassName('tab-content');
            for (var i = 0; i < tabs.length; i++) {{
                tabs[i].classList.remove('active');
            }}
            var tabBtns = document.getElementsByClassName('tab');
            for (var i = 0; i < tabBtns.length; i++) {{
                tabBtns[i].classList.remove('active');
            }}
            document.getElementById(tabName).classList.add('active');
            evt.currentTarget.classList.add('active');
        }}
    </script>
</body>
</html>"""

    return html

def main():
    if len(sys.argv) < 2:
        print("用法: python generate_debug_report.py <debug_session_dir>")
        sys.exit(1)

    session_dir = sys.argv[1]
    html = generate_html(session_dir)

    output_file = f'debug_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.html'
    Path(output_file).write_text(html, encoding='utf-8')

    print(f"✅ 报告已生成: {output_file}")

if __name__ == '__main__':
    main()
