#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
send_mail.py - jira-commit 完成通知：飞书邮件（替代原 notify.ps1 弹窗）

使用 lark-cli 发送飞书邮件：
  收件人 = 当前飞书账号邮箱（lark-cli 自动获取，无需配置）
  抄送   = config/notification/email_cc 列表（用户可在 jira_commit_config.json 中添加）

用法（由 generate_report.py 调用，也可手动测试）:
  python script/send_mail.py analyze "jira-commit 分析完成" "已生成 2 个任务，预览见 commit_preview.md"
  python script/send_mail.py execute  "jira-commit 执行完成" "详情见 commit_report.html"
  python script/send_mail.py test     "测试主题" "测试正文"

场景说明（scene）:
  analyze - 正文附任务清单表（从 tasks.json 读取）
  execute - 正文附 JIRA 链接与 4 步手动操作清单；附件自动附带 commit_report.html（存在即附，lark-cli --attach）
  test    - 联调测试

失败仅打印 WARN 到 stderr，不影响主流程（与原弹窗行为一致）。
"""
import html
import io
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import jira_paths

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


# ---------------------------------------------------------------- 配置读取
def load_config():
    cfg_file = jira_paths.get_config_file()
    if not os.path.exists(cfg_file):
        return {}
    with open(cfg_file, encoding='utf-8') as fh:
        return json.load(fh)


def get_email_cc(config):
    """读取抄送人列表（config.notification.email_cc），返回邮箱列表"""
    notification = config.get('notification') or {}
    cc = notification.get('email_cc') or []
    if isinstance(cc, str):
        cc = [cc]
    # 过滤占位符/空白，去重（保持顺序）
    seen, result = set(), []
    for addr in cc:
        addr = str(addr).strip()
        if not addr or '❗️' in addr or '填写' in addr:
            continue
        if addr not in seen:
            seen.add(addr)
            result.append(addr)
    return result


# ---------------------------------------------------------------- 飞书 CLI
def _lark_cli():
    """解析 lark-cli 可执行文件路径。

    Windows 下 npm 全局安装的 CLI 是 .cmd shim，subprocess 用裸命令名
    调用会因 CreateProcess 无法解析而抛 WinError 2，须经 shutil.which
    拿到完整路径（如 lark-cli.CMD）。
    """
    return shutil.which('lark-cli') or 'lark-cli'


def get_my_email():
    """自动获取当前飞书账号邮箱（lark-cli mail user_mailboxes profile）"""
    try:
        out = subprocess.run(
            [_lark_cli(), 'mail', 'user_mailboxes', 'profile',
             '--params', '{"user_mailbox_id":"me"}', '--as', 'user'],
            capture_output=True, text=True, timeout=30, encoding='utf-8')
        data = json.loads(out.stdout)
        if data.get('ok'):
            email = (data.get('data') or {}).get('primary_email_address') or ''
            if email:
                return email
        print(f"[WARN] 获取飞书邮箱失败: {out.stdout[:200]} {out.stderr[:200]}",
              file=sys.stderr)
    except Exception as e:
        print(f"[WARN] 获取飞书邮箱异常: {e}", file=sys.stderr)
    return ''


def send_lark_mail(subject, body_html, to_email, cc_emails, attach_paths=None, workdir=None):
    """调用 lark-cli mail +send 发送邮件（--confirm-send 直接发送）

    attach_paths: 附件文件路径列表。lark-cli --attach 仅接受相对路径，
                  故按 workdir（缺省 cwd）转成相对路径，并以 workdir 作为子进程 cwd。
    workdir: 子进程工作目录，同时是附件相对路径的基准目录。
    """
    cmd = [_lark_cli(), 'mail', '+send',
           '--to', to_email,
           '--subject', subject,
           '--body', body_html,
           '--confirm-send',
           '--as', 'user']
    if cc_emails:
        cmd += ['--cc', ','.join(cc_emails)]
    if attach_paths:
        base = workdir or os.getcwd()
        rels = []
        for p in attach_paths:
            try:
                rels.append(os.path.relpath(p, base))
            except ValueError:      # 跨盘符无法相对化，退回文件名
                rels.append(os.path.basename(p))
        cmd += ['--attach', ','.join(rels)]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True,
                             timeout=60, encoding='utf-8', cwd=workdir)
        data = json.loads(out.stdout) if out.stdout else {}
        if data.get('ok'):
            return True, ''
        err = data.get('error') or {}
        # stdout 非 JSON（如参数错误）时补上 stderr，否则错误信息为空
        msg = err.get('message') or out.stdout[:300] or out.stderr[:300]
        return False, f"{msg} {err.get('hint', '')}".strip()
    except Exception as e:
        return False, str(e)


# ---------------------------------------------------------------- 邮件内容构造
def _esc(s):
    return html.escape(str(s)) if s else ''


def _now():
    from datetime import datetime
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def load_tasks():
    f = Path(jira_paths.get_output_dir()) / 'tasks.json'
    if not f.exists():
        return []
    try:
        with open(f, encoding='utf-8') as fh:
            return (json.load(fh) or {}).get('tasks', [])
    except Exception:
        return []


def build_analyze_body(message):
    """analyze 场景：正文 + 任务清单表"""
    tasks = load_tasks()
    jira_base = (load_config().get('jira_url') or '').rstrip('/')
    rows = ''
    for t in tasks:
        jira = t.get('jira_key') or ''
        if jira and '://' in jira_base:
            jira_html = f'<a href="{_esc(jira_base)}/browse/{_esc(jira)}">{_esc(jira)}</a>'
        else:
            jira_html = _esc(jira) or '待创建'
        rows += (f'<tr><td>{jira_html}</td>'
                 f'<td>{_esc(t.get("title_cn", t.get("title", "")))}</td>'
                 f'<td>{_esc(t.get("type", ""))}</td>'
                 f'<td>{_esc(t.get("difficulty", ""))}</td>'
                 f'<td>{_esc(t.get("impact", ""))}</td></tr>')

    table = ''
    if rows:
        table = ('<table border="1" cellpadding="6" cellspacing="0" '
                 'style="border-collapse:collapse;font-size:13px;">'
                 '<tr style="background:#f0f4ff;"><th>JIRA</th><th>任务</th>'
                 '<th>类型</th><th>难度</th><th>影响等级</th></tr>'
                 f'{rows}</table>')

    return (f'<p>{_esc(message).replace(chr(10), "<br>")}</p>{table}'
            f'<p style="color:#888;font-size:12px;">'
            f'预览文件: {_esc(Path(jira_paths.get_output_dir()) / "commit_preview.md")}<br>'
            f'jira-commit · {_esc(_now())}</p>')


def build_execute_body(message, html_report_path):
    """execute 场景：正文 + JIRA 链接 + 4 步手动操作清单"""
    tasks = load_tasks()
    jira_base = (load_config().get('jira_url') or '').rstrip('/')
    links = []
    for t in tasks:
        jira = t.get('jira_key') or ''
        if jira and '://' in jira_base:
            links.append((jira, t.get('title_cn', t.get('title', '')),
                          f"{jira_base}/browse/{jira}"))

    jira_html = ''
    if links:
        items = ''.join(
            f'<li><a href="{_esc(url)}">{_esc(key)}</a> - {_esc(title)}</li>'
            for key, title, url in links)
        jira_html = (f'<h3>本次创建的 JIRA（请手动打到「待验证」）</h3>'
                     f'<ul>{items}</ul>')

    report_html = ''
    if html_report_path and Path(html_report_path).exists():
        report_html = (f'<p>完整指引报告: '
                       f'<a href="file:///{str(html_report_path).replace(os.sep, "/")}">'
                       f'commit_report.html</a></p>')

    return (f'<p>{_esc(message).replace(chr(10), "<br>")}</p>'
            f'<h3>后续手动步骤</h3>'
            f'<ol>'
            f'<li>手动提交和 push commit（先 git pull origin main 再 push）</li>'
            f'<li>手动把 JIRA 任务打到「待验证」</li>'
            f'<li>在 GitLab 提 merge request</li>'
            f'<li>如有必要手动打 tag</li>'
            f'</ol>'
            f'{jira_html}{report_html}'
            f'<p style="color:#888;font-size:12px;">jira-commit · {_esc(_now())}</p>')


# ---------------------------------------------------------------- main
def main():
    scene = sys.argv[1] if len(sys.argv) > 1 else 'test'
    title = sys.argv[2] if len(sys.argv) > 2 else 'jira-commit 通知'
    message = sys.argv[3] if len(sys.argv) > 3 else ''

    config = load_config()

    # 开关：notification.email_enabled，缺省 true
    notification = config.get('notification') or {}
    if notification.get('email_enabled') is False:
        print("[INFO] 邮件通知已关闭（config.notification.email_enabled=false），跳过发送")
        return 0

    # 1. 收件人：自动获取当前飞书账号邮箱
    to_email = get_my_email()
    if not to_email:
        print("[WARN] 无法获取飞书邮箱，跳过邮件通知", file=sys.stderr)
        return 0

    # 2. 抄送：config.notification.email_cc
    cc_emails = get_email_cc(config)

    # 3. 正文按场景构造
    out_dir = jira_paths.get_output_dir()
    attach = None
    if scene == 'analyze':
        body = build_analyze_body(message)
    elif scene == 'execute':
        body = build_execute_body(message, os.path.join(out_dir, 'commit_report.html'))
        # 附件：生成物 commit_report.html 存在即附
        report_path = os.path.join(out_dir, 'commit_report.html')
        if os.path.exists(report_path):
            attach = [report_path]
    else:
        body = f'<p>{_esc(message).replace(chr(10), "<br>")}</p>'

    # 4. 发送（附件走相对路径：子进程 cwd 设为产物目录，相对路径即纯文件名）
    ok, err = send_lark_mail(title, body, to_email, cc_emails, attach, workdir=out_dir)
    if ok:
        print(f"[OK] 飞书邮件已发送: 收件人={to_email}"
              + (f", 抄送={','.join(cc_emails)}" if cc_emails else ""))
        return 0
    print(f"[WARN] 飞书邮件发送失败: {err}", file=sys.stderr)
    return 0  # 通知失败不阻断主流程


if __name__ == '__main__':
    sys.exit(main())
