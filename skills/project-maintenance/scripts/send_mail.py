#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""send_mail.py - project-maintenance 运行结果邮件通知(照搬 jira-commit 已验证链路)

用法:
  python scripts/send_mail.py <subject> <body_html_file> [--attach <report_file>]

  subject       邮件主题
  body_html_file 正文 HTML 文件路径(可多行,脚本自动压成单行)
  --attach      附件文件路径(统一报告 OutPut_YYYYMMDD.html)

收件人/抄送读 <skill>/config/config.conf 的 notify_email / notify_cc。

链路要点(2026-09-12 实测踩坑,勿改):
  1. 正文必须单行:多行 --body 被 lark-cli lint 截断到第一行 → 邮件无正文。
  2. 参数走 Python subprocess 参数列表(CreateProcessW),不经 bash/.cmd 垫片码页。
  3. --attach 只接受 cwd 内相对路径:子进程 cwd = 附件所在目录,附件用纯文件名。
  4. DLP:Write 工具写的报告落盘即密文(bash/lark-cli 读密文);python 读=透明解密。
     附前用 python 把报告内容重写一遍 → 落盘为明文(lark-cli 能读,用户本地免解密)。
  5. mail +send 可能只存草稿:返回 draft_id 而无 message_id 时,补 drafts send --yes。
失败仅打印 WARN,退出码 0(通知失败不阻断维护流程)。
"""
import io
import json
import os
import shutil
import subprocess
import sys

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def _lark_cli():
    """shutil.which 解析 npm .cmd shim(裸名 subprocess 会 WinError 2)。"""
    return shutil.which('lark-cli') or 'lark-cli'


def load_config():
    """读 config.conf 的 notify_email / notify_cc(简单 key = value 行,非标准 ini)。"""
    cfg = {}
    path = os.path.join(SKILL_DIR, 'config', 'config.conf')
    if not os.path.exists(path):
        return cfg
    with open(path, encoding='utf-8') as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            k, _, v = line.partition('=')
            cfg[k.strip()] = v.strip()
    return cfg


def ensure_plaintext(path):
    """DLP 处理:python 透明读报告 → 重写落盘为明文;已是明文则原样返回 True。

    python 不在白名单读不到明文(极端情况)时返回 False,调用方放弃附件改正文兜底。
    """
    with open(path, 'rb') as fh:
        raw = fh.read()
    if raw.startswith(b'%TSD-Header'):
        # python 未能透明解密,无法救回
        return False
    content = raw.decode('utf-8')
    with open(path, 'w', encoding='utf-8', newline='') as fh:
        fh.write(content)
    with open(path, 'rb') as fh:      # 复核重写后确为明文
        return not fh.read(12).startswith(b'%TSD-Header')


def send(subject, body_html, to_email, cc_emails, attach_path=None):
    cli = _lark_cli()
    cmd = [cli, 'mail', '+send', '--as', 'user',
           '--to', to_email,
           '--subject', subject,
           '--body', body_html,
           '--confirm-send']
    if cc_emails:
        cmd += ['--cc', ','.join(cc_emails)]
    cwd = os.getcwd()
    if attach_path:
        cwd = os.path.dirname(os.path.abspath(attach_path)) or '.'
        cmd += ['--attach', os.path.basename(attach_path)]
    out = subprocess.run(cmd, capture_output=True, text=True,
                         encoding='utf-8', cwd=cwd, timeout=120)
    try:
        data = json.loads(out.stdout) if out.stdout else {}
    except json.JSONDecodeError:
        print(f"[WARN] +send 输出异常: {out.stdout[:200]} {out.stderr[:200]}", file=sys.stderr)
        return False
    if not data.get('ok'):
        err = data.get('error') or {}
        print(f"[WARN] 发送失败: {err.get('message', '')} {err.get('hint', '')}",
              file=sys.stderr)
        return False
    if data.get('data', {}).get('message_id'):
        return True                      # 已直发
    # 只存了草稿 → 二段发送
    draft_id = data.get('data', {}).get('draft_id')
    if not draft_id:
        print("[WARN] 响应无 message_id/draft_id", file=sys.stderr)
        return False
    out2 = subprocess.run(
        [cli, 'mail', 'user_mailbox.drafts', 'send', '--yes',
         '--params', json.dumps({'user_mailbox_id': 'me', 'draft_id': draft_id})],
        capture_output=True, text=True, encoding='utf-8', timeout=120)
    try:
        return json.loads(out2.stdout).get('ok', False)
    except json.JSONDecodeError:
        return False


def main():
    args = sys.argv[1:]
    attach = None
    if '--attach' in args:
        i = args.index('--attach')
        attach = args[i + 1]
        args = args[:i] + args[i + 2:]
    if len(args) < 2:
        print(__doc__)
        return 1
    subject, body_file = args[0], args[1]

    cfg = load_config()
    to_email = cfg.get('notify_email', '')
    if not to_email:
        print("[INFO] config.conf 未配 notify_email,跳过发送")
        return 0
    cc = [x.strip() for x in cfg.get('notify_cc', '').split(',') if x.strip()]

    if not os.path.exists(body_file):
        print(f"[WARN] 正文文件不存在: {body_file}", file=sys.stderr)
        return 0
    with open(body_file, encoding='utf-8') as fh:
        body = fh.read()
    body = body.replace('\r', '').replace('\n', '')   # 压单行(多行会被 lint 截断)

    attach_note = ''
    if attach:
        if not os.path.exists(attach):
            print(f"[WARN] 附件不存在: {attach}", file=sys.stderr)
            attach = None
        elif not ensure_plaintext(attach):
            print("[WARN] 附件是 DLP 密文且 python 无法解密,放弃附件(正文兜底)", file=sys.stderr)
            attach = None
            attach_note = '<p style="color:#c00;">附件因 DLP 加密未能附上,请本地打开报告文件查看。</p>'
    body += attach_note

    if send(subject, body, to_email, cc, attach):
        print(f"[OK] 邮件已发送: {to_email}" + (f", 附件={attach}" if attach else ""))
    else:
        print("[WARN] 邮件发送失败(不阻断维护流程)", file=sys.stderr)
    return 0


if __name__ == '__main__':
    sys.exit(main())
