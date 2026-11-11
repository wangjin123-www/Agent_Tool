#!/usr/bin/env python3
"""串口日志报告邮件发送（lark-cli 飞书邮件, 复用 7255 jira-commit 的实现方式）。

收件人: 当前飞书账号邮箱(lark-cli 自动获取, 无需配置)
抄送:   config/config.conf [mail] cc = 邮箱1,邮箱2
开关:   [mail] enabled = true/false

用法:
  python send_mail.py "主题" "正文(纯文本或HTML)" 附件1 附件2 ...
  python send_mail.py --test
"""
import io
import json
import os
import re
import shutil
import subprocess
import sys
from configparser import ConfigParser
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent.parent   # scripts/common/ -> skill 根
CONFIG = SKILL_DIR / "config" / "config.conf"

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")


def load_mail_cfg():
    cfg = ConfigParser()
    if CONFIG.exists():
        cfg.read(CONFIG, encoding="utf-8")
    if not cfg.has_section("mail"):
        cfg.add_section("mail")
    return {
        "enabled": cfg.get("mail", "enabled", fallback="true").lower() != "false",
        "cc": [c.strip() for c in cfg.get("mail", "cc", fallback="").split(",") if c.strip()],
    }


def lark_cli():
    return shutil.which("lark-cli") or "lark-cli"


def get_my_email():
    try:
        out = subprocess.run(
            [lark_cli(), "mail", "user_mailboxes", "profile",
             "--params", '{"user_mailbox_id":"me"}', "--as", "user"],
            capture_output=True, text=True, timeout=30, encoding="utf-8")
        data = json.loads(out.stdout)
        if data.get("ok"):
            email = (data.get("data") or {}).get("primary_email_address") or ""
            if email:
                return email
        print(f"[WARN] 获取飞书邮箱失败: {out.stdout[:200]}", file=sys.stderr)
    except Exception as e:
        print(f"[WARN] 获取飞书邮箱异常: {e}", file=sys.stderr)
    return ""


def send(subject, body, to_email, cc_list, attach_paths):
    cmd = [lark_cli(), "mail", "+send",
           "--to", to_email, "--subject", subject, "--body", body,
           "--confirm-send", "--as", "user"]
    if cc_list:
        cmd += ["--cc", ",".join(cc_list)]
    if attach_paths:
        # lark-cli --attach 接受相对路径, 以第一个附件所在目录为 cwd
        base = os.path.dirname(os.path.abspath(attach_paths[0]))
        rels = []
        for p in attach_paths:
            try:
                rels.append(os.path.relpath(p, base))
            except ValueError:
                rels.append(os.path.basename(p))
        cmd += ["--attach", ",".join(rels)]
        cwd = base
    else:
        cwd = None
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=60,
                             encoding="utf-8", cwd=cwd)
        data = json.loads(out.stdout) if out.stdout else {}
        if data.get("ok"):
            return True, ""
        err = data.get("error") or {}
        return False, (err.get("message") or out.stdout[:200] or out.stderr[:200])
    except Exception as e:
        return False, str(e)


def html_body(text):
    # 串口日志可能夹带 \x00 等控制字符(subprocess 传参会报 embedded null character), 统一清掉
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", "", text)
    esc = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return f'<pre style="font-family:Consolas,monospace;">{esc}</pre>'


def main():
    args = sys.argv[1:]
    cfg = load_mail_cfg()
    if not cfg["enabled"]:
        print("[INFO] 邮件已关闭 (config.conf [mail] enabled=false)")
        return 0

    if args and args[0] == "--test":
        subject, body, attaches = "serial-log 邮件测试", "测试正文, 收到即配置OK", []
    elif len(args) >= 2:
        subject, body, attaches = args[0], html_body(args[1]), args[2:]
    else:
        print("用法: python send_mail.py 主题 正文 [附件...]", file=sys.stderr)
        return 1

    to = get_my_email()
    if not to:
        print("[WARN] 无法获取飞书邮箱, 放弃发送", file=sys.stderr)
        return 0

    for a in attaches:
        if not Path(a).exists():
            print(f"[WARN] 附件不存在, 已剔除: {a}", file=sys.stderr)
    attaches = [a for a in attaches if Path(a).exists()]

    ok, err = send(subject, body, to, cfg["cc"], attaches)
    if ok:
        print(f"[OK] 邮件已发送: to={to}" + (f" cc={','.join(cfg['cc'])}" if cfg["cc"] else "")
              + (f" 附件={len(attaches)}个" if attaches else ""))
        return 0
    print(f"[WARN] 发送失败: {err}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
