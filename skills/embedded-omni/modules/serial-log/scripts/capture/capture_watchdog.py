#!/usr/bin/env python3
"""采集看门狗: 独立进程监视 capture_serial.py 心跳, 异常中断时自动备份 log + 发飞书邮件。

为什么需要它(防幻觉):
  AI 用 StopCommand/杀进程/终端关闭/进程崩溃时, capture_serial.py 里的收尾代码
  (备份 + 异常邮件)根本不会执行。看门狗是独立进程, 只依赖 status.json 心跳,
  不需要 AI 判断, 也不需要采集进程活着。

判据(全部基于文件, 不看 AI 说法):
  - status.json 不存在            -> 采集从未启动, 退出
  - state=DONE / ABNORMAL         -> 采集已收尾(可能已发过邮件), 退出
  - state=RUNNING 且 pid 已消失   -> 异常中断(崩溃/被杀) -> 备份 + 发邮件
  - state=RUNNING 但心跳超时       -> 进程假死/被挂起       -> 备份 + 发邮件

用法(由 capture_serial.py 自动拉起, 一般不用手跑):
  python capture_watchdog.py <ctl目录>
"""
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent.parent   # scripts/capture/ -> skill 根

HEARTBEAT_TIMEOUT = 15   # 秒, 心跳超时视为假死
POLL_INTERVAL = 2        # 秒


def pid_alive(pid):
    """跨平台判断 pid 是否存活。"""
    if not pid:
        return False
    if sys.platform == "win32":
        import ctypes
        # PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
        h = ctypes.windll.kernel32.OpenProcess(0x1000, False, int(pid))
        if not h:
            return False
        code = ctypes.c_ulong()
        ok = ctypes.windll.kernel32.GetExitCodeProcess(h, ctypes.byref(code))
        ctypes.windll.kernel32.CloseHandle(h)
        # STILL_ACTIVE = 259
        return bool(ok) and code.value == 259
    try:
        os.kill(int(pid), 0)
        return True
    except (OSError, ProcessLookupError):
        return False


def read_status(ctl_dir):
    f = ctl_dir / "status.json"
    if not f.exists():
        return None
    try:
        return json.loads(f.read_text(encoding="utf-8"))
    except Exception:
        return None


def log(ctl_dir, msg):
    """同时打屏(被重定向到 watchdog.log)并追加到独立日志。"""
    line = f"[{datetime.now():%H:%M:%S}] {msg}"
    print(line, flush=True)
    try:
        with open(ctl_dir / "watchdog_events.log", "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError:
        pass


def backup_and_notify(ctl_dir, st, reason):
    """异常收尾: 把主 log 改名加结束时间并归档到 logs/完成采集/ 后发异常邮件。"""
    log_path = Path(st.get("log", ""))
    if not log_path.exists():
        log(ctl_dir, f"异常({reason}) 但日志文件不存在: {log_path}")
        return
    name = f"{log_path.stem}_结束{datetime.now():%Y%m%d_%H%M%S}.log"
    finish_dir = log_path.parent / "完成采集"
    dst = (finish_dir / name) if log_path.parent.name == "logs" else log_path.with_name(name)
    backup = dst
    try:
        dst.parent.mkdir(parents=True, exist_ok=True)
        log_path.replace(dst)
        log(ctl_dir, f"异常({reason}) 已归档: {backup}")
    except OSError as e:
        log(ctl_dir, f"异常({reason}) 归档失败: {e}; 保持原文件")
        backup = log_path

    # 写异常终态(带 who=watchdog), 采集进程若还在收尾可看到并避免重复发信
    try:
        tmp = ctl_dir / "status.json.tmp"
        tmp.write_text(json.dumps({
            "state": "ABNORMAL_WATCHDOG", "who": "watchdog", "reason": reason,
            "log": str(log_path), "backup": str(backup),
            "lines": st.get("lines"), "bytes": st.get("bytes"),
            "warn": st.get("warn"), "error": st.get("error"),
            "heartbeat": time.time(),
        }, ensure_ascii=False, indent=2), encoding="utf-8")
        tmp.replace(ctl_dir / "status.json")
    except OSError:
        pass

    import subprocess
    subject = f"[异常中断] 串口采集 {st.get('port')}@{st.get('baud')} ({reason})"
    body = (f"采集进程异常中断(看门狗判定, 非正常结束)\n"
            f"判定依据: {reason}\n"
            f"最后心跳: {datetime.fromtimestamp(st.get('heartbeat', time.time())):%Y-%m-%d %H:%M:%S}\n"
            f"已收: {st.get('lines')} 行 / {st.get('bytes')} 字节\n"
            f"WARN: {st.get('warn')} 行   ERROR: {st.get('error')} 行\n"
            f"已备份为: {backup}\n"
            f"时间: {datetime.now():%Y-%m-%d %H:%M:%S}")
    try:
        r = subprocess.run(
            [sys.executable, str(SKILL_DIR / "scripts" / "common" / "send_mail.py"), subject, body, str(backup)],
            capture_output=True, text=True, timeout=90, encoding="utf-8", errors="replace")
        log(ctl_dir, f"异常邮件: {(r.stdout or r.stderr or '').strip()[:200]}")
    except Exception as e:
        log(ctl_dir, f"异常邮件发送失败: {e}")


def main():
    if len(sys.argv) < 2:
        print("用法: python capture_watchdog.py <ctl目录>", file=sys.stderr)
        return 1
    ctl_dir = Path(sys.argv[1])
    log(ctl_dir, f"看门狗启动, 监视 {ctl_dir}")

    while True:
        st = read_status(ctl_dir)
        if st is None:
            log(ctl_dir, "无 status.json, 退出(采集未启动)")
            return 0
        state = st.get("state")
        if state in ("DONE",):
            log(ctl_dir, f"采集正常结束({st.get('end_reason')}), 看门狗退出")
            return 0
        if state in ("ABNORMAL", "ABNORMAL_WATCHDOG"):
            log(ctl_dir, f"采集已按异常收尾, 看门狗退出(state={state})")
            return 0
        # state == RUNNING
        pid = st.get("pid")
        if pid and not pid_alive(pid):
            backup_and_notify(ctl_dir, st, "采集进程已消失(崩溃/被强杀)")
            return 0
        hb_age = time.time() - float(st.get("heartbeat", 0))
        if hb_age > HEARTBEAT_TIMEOUT:
            backup_and_notify(ctl_dir, st, f"心跳超时 {hb_age:.0f}s(进程假死)")
            return 0
        time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    sys.exit(main())
