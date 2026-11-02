#!/usr/bin/env python3
"""串口日志采集：持续读取串口写入文件，Ctrl+C 停止并输出统计。

用法:
  python capture_serial.py --list
  python capture_serial.py --port COM3 --baud 921600 --confirm --end-cond unlimited
  python capture_serial.py --port COM3 --out my.log --duration 60 --confirm --end-cond duration

结束保障(脚本级, 不依赖 AI 判断):
  - 正常结束(手动/时长/时间到/关键字命中/控制文件 stop): 主 log 改名加结束时间
    (<原名>_结束<结束时刻>.log)并归档到 output/logs/完成采集/
  - 异常中断(串口拔出/崩溃/进程被杀): 常驻看门狗 capture_watchdog.py 自动发现并
    归档 log + 发飞书邮件通知
  - 采集中要发邮件: 写控制文件(用 capture_cmd.py), 发快照副本(落 output/logs/快照/)后继续采集, 不中断
  - 告警模式(只发邮件, 绝不停止采集): --alert-on-error / --alert-on-warn /
    --alert-pattern "正则" 命中即发告警邮件(快照副本落 output/logs/告警/), 采集继续;
    --alert-cooldown N 控同类冷却

文件归档约定(logs 根目录只留"正在采集"的主 log):
  output/logs/<主log>.log              正在采集的主 log
  output/logs/完成采集/<主log>_结束<时刻>.log   采集结束归档
  output/logs/告警/..._告警HHMMSS.log   告警邮件快照副本
  output/logs/快照/..._快照HHMMSS.log   采集中手动发邮件的快照副本
  output/logs/分析/..._分析.{md,json,html}      分析产物
  output/logs/ctl/<主log>.ctl/          status.json / cmd.json / 看门狗日志

用法(采集中的外部指令):
  python capture_cmd.py <log路径> mail     # 发当前快照邮件, 采集继续
  python capture_cmd.py <log路径> stop     # 请求正常停止(会备份+统计)
  python capture_cmd.py <log路径> status   # 查看状态(是否在采/RUNNING/异常)

用法(告警只通知不停止):
  python capture_serial.py --port COM6 --baud 921600 --confirm --end-cond unlimited \
      --alert-pattern "CheckCTS.*FATAL" --alert-on-error
"""
import argparse
import json
import os
import re
import sys
import threading
import time
from datetime import datetime
from pathlib import Path

try:
    import serial
    import serial.tools.list_ports
except ImportError:
    print("错误: 缺少 pyserial, 请执行: pip install pyserial", file=sys.stderr)
    sys.exit(1)

SKILL_DIR = Path(__file__).resolve().parent.parent.parent   # scripts/capture/ -> skill 根
CONFIG_FILE = SKILL_DIR / "config" / "config.conf"


def load_log_dir():
    """读 config [log] 段的 dir 作为 log 根目录; 文件不在/没配/配空 -> 默认 <skill>/output/logs。
    所有采集主 log/告警/快照/完成采集/分析产物/ctl 都落在这个根下。"""
    default = SKILL_DIR / "output" / "logs"
    if not CONFIG_FILE.exists():
        return default
    in_log = False
    for line in CONFIG_FILE.read_text(encoding="utf-8", errors="replace").splitlines():
        s = line.strip()
        if not s or s.startswith(("#", ";")):
            continue
        if s.startswith("["):
            in_log = s.strip("[]").strip().lower() == "log"
            continue
        if not in_log or "=" not in s:
            continue
        k, v = (x.strip() for x in s.split("=", 1))
        if k.lower() == "dir" and v:
            return Path(v)
    return default


LOG_DIR = load_log_dir()
# 非主 log 一律落分类子目录, 保持 logs 根目录只留"正在采集"的主 log
ALERT_DIR_NAME = "告警"       # 告警邮件附的快照副本
SNAP_DIR_NAME = "快照"        # 采集中手动发邮件的快照副本
FINISH_DIR_NAME = "完成采集"   # 采集结束(正常/异常)归档的主 log
REPORT_DIR_NAME = "分析"       # md/json/html 分析产物
CTL_DIR_NAME = "ctl"          # status.json/cmd.json/看门狗日志


def subdir(name):
    """取(并创建) logs 下的分类子目录。"""
    d = LOG_DIR / name
    d.mkdir(parents=True, exist_ok=True)
    return d


def end_stamp():
    """结束时刻戳, 用于主 log 改名时拼接结束时间。"""
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def archive_main_log(out_path, stamp=None):
    """采集结束(正常/异常)时把主 log 改名带上结束时间, 并移入 完成采集/。

    改名=移动: 原"正在采集"文件名不再保留(下次采集重新生成新主 log)。
    命名: <原名>_结束<结束时刻>.log, 开始时间本就含在原名里。
    - 主 log 在 logs 根目录 -> 归档进 logs/完成采集/
    - 主 log 是 --out 自定义的外部路径 -> 原地改名(不搬进 skill 目录)
    stamp 可外部传入(便于先把归档路径写进 status.json 再移动)。
    返回归档后的新路径; 移动失败则原样返回原路径。"""
    name = f"{out_path.stem}_结束{stamp or end_stamp()}.log"
    under_logs = out_path.parent == LOG_DIR
    dst = (subdir(FINISH_DIR_NAME) / name) if under_logs else out_path.with_name(name)
    try:
        out_path.replace(dst)
        return dst
    except OSError as e:
        print(f"[WARN] 主 log 归档失败: {e}", file=sys.stderr, flush=True)
        return out_path


def list_ports():
    ports = list(serial.tools.list_ports.comports())
    if not ports:
        print("未发现串口设备")
        return
    print("可用串口:")
    for p in ports:
        print(f"  {p.device:<10} {p.description}")


def load_config():
    cfg = {}
    if CONFIG_FILE.exists():
        for line in CONFIG_FILE.read_text(encoding="utf-8", errors="replace").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("["):
                continue
            if "=" in line:
                k, v = line.split("=", 1)
                cfg[k.strip()] = v.strip()
    return cfg


def load_projects():
    """读 config [projects] 段: 返回 (编号 -> 工程根目录, 默认编号 or None)。
    分析结论据此定位到源码文件/函数(见 SKILL.md 工程关联)。"""
    projects, default = {}, None
    if not CONFIG_FILE.exists():
        return projects, default
    in_pj = False
    for line in CONFIG_FILE.read_text(encoding="utf-8", errors="replace").splitlines():
        s = line.strip()
        if not s or s.startswith(("#", ";")):
            continue
        if s.startswith("["):
            in_pj = s.strip("[]").strip().lower() == "projects"
            continue
        if not in_pj or "=" not in s:
            continue
        k, v = (x.strip() for x in s.split("=", 1))
        if k.lower() == "default":
            default = v or None
        elif v:
            projects[k] = v
    return projects, default


def save_config(port, baud):
    """只更新 [serial] 段的 port/baud, 保留其他段([mail]/[projects]), 避免冲掉工程注册表。"""
    lines = CONFIG_FILE.read_text(encoding="utf-8").splitlines() if CONFIG_FILE.exists() else []
    out, done, in_serial = [], False, False
    for line in lines:
        s = line.strip()
        if s.startswith("["):
            if in_serial and not done:
                out += [f"port = {port}", f"baud = {baud}"]
                done = True
            in_serial = s.strip("[]").strip().lower() == "serial"
        if in_serial and re.match(r"^(port|baud)\s*=", s):
            continue
        out.append(line)
    if in_serial and not done:
        out += [f"port = {port}", f"baud = {baud}"]
        done = True
    if not done:
        out = ["# serial-log skill 配置(不入库)", "[serial]", f"port = {port}", f"baud = {baud}"] + out
    CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_FILE.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")


BAUD_CANDIDATES = [9600, 19200, 38400, 57600, 115200, 230400, 460800, 921600, 1000000, 1500000, 2000000]
# auto-baud 检测顺序: 常用档优先(间歇日志下窗口有限, 高频档先试)
AUTO_BAUD_ORDER = [115200, 921600, 57600, 38400, 19200, 9600, 230400, 460800, 1000000, 1500000, 2000000]


def detect_baud(port, candidates=None, stop_event=None):
    """试错法检测波特率: 正确波特率下数据为可打印 ASCII, 错误波特率下为乱码。
    前提: 设备正在持续输出日志, 静默设备无法检测。
    stop_event: threading.Event, 每档开始前检查, 置位即中止(粒度=1档, 最坏等1.8s)。"""
    best = None
    best_score = 0.0
    print(f"检测波特率: {port} (设备需正在打日志)")
    for baud in (candidates or BAUD_CANDIDATES):
        if stop_event is not None and stop_event.is_set():
            print("  [停止] 用户请求停止检测")
            break
        try:
            ser = serial.Serial(port, baud, timeout=0.2, inter_byte_timeout=0.05)
        except serial.SerialException as e:
            print(f"  {baud:>7}: 打开失败 {e}")
            continue
        time.sleep(0.3)
        data = b""
        deadline = time.time() + 1.5
        while time.time() < deadline and len(data) < 2048:
            data += ser.read(512)
        ser.close()
        if not data:
            print(f"  {baud:>7}: 无数据")
            continue
        printable = sum(1 for b in data if 32 <= b < 127 or b in (9, 10, 13))
        ratio = printable / len(data)
        newlines = data.count(b"\n")
        # 评分: 可打印率为主, 换行结构加分
        score = ratio + min(newlines / 20.0, 0.5)
        print(f"  {baud:>7}: {len(data)}B 可打印率={ratio:.0%} 换行={newlines}")
        if ratio > 0.95 and newlines >= 2 and score > best_score:
            best_score = score
            best = baud
    if best:
        print(f"最佳波特率: {best}")
    else:
        print("未检测到有效波特率(设备可能没在打日志, 或波特率不在候选列表)")
    return best


# 实时告警规则: (正则, 告警标签) --watch 时逐行检测, 命中打 [ALERT] 标记(只上屏, 不写文件)
WATCH_RULES = [
    (r"HardFault|CmBacktrace|assert|Assert|ASSERT", "CRASH"),
    (r"drop_cnt|丢弃", "DROP"),
    (r"DTC|FAULT DETECTED", "FAULT"),
    (r"\[E\]|ERROR|ERR_[A-Z]|error", "ERROR"),
    (r"\[W\]|WARN", "WARN"),
    (r"FAIL|fail|retry|RETRY", "FAIL"),
    (r"timeout|TIMEOUT|Timeout", "TIMEOUT"),
]


def watch_line(text, counters):
    """对一行日志做规则检测, 返回告警标签或 None。"""
    for pattern, tag in WATCH_RULES:
        if re.search(pattern, text):
            counters[tag] = counters.get(tag, 0) + 1
            return tag
    return None


def open_with_auto_baud(port, baud, auto):
    """打开串口; auto 模式下先验证给定波特率(5秒窗口内数据须为可打印文本),
    无数据或乱码则自动逐档检测并切换。返回 (serial对象, 实际波特率)。"""

    def _probe(ser, seconds):
        """收 seconds 秒, 返回数据"""
        t2 = time.time() + seconds
        buf = b""
        while time.time() < t2:
            buf += ser.read(512)
        return buf

    def _looks_valid(data):
        """有效日志判据: 足量 + 高可打印率 + 有换行结构(防欠采样乱码误判)"""
        if len(data) < 32:
            return False
        printable = sum(1 for b in data if 32 <= b < 127 or b in (9, 10, 13))
        return printable / len(data) >= 0.95 and data.count(b"\n") >= 2

    # inter_byte_timeout 必须设: Windows 下只设 timeout 时, read(N) 会一直阻塞到攒满 N 字节
    # (实测 timeout=1 时 read(4096) 耗时 42s, 期间网页/文件看不到任何数据; 加上间隔超时后 0.05s 即返回)
    ser = serial.Serial(port, baud, timeout=1, inter_byte_timeout=0.05)
    if not auto:
        return ser, baud

    # 先按给定波特率收 5 秒并校验内容(收得到字节≠波特率对, 欠采样乱码也是字节)
    first = _probe(ser, 5.0)
    if _looks_valid(first):
        print(f"[auto-baud] {baud}bps 数据有效, 直接使用")
        ser.reset_input_buffer()
        return ser, baud
    ser.close()
    reason = "收到乱码(波特率疑似不对)" if first else "无数据"
    print(f"[auto-baud] {baud}bps 5秒内{reason}, 自动检测中(设备需正在打日志)...", flush=True)

    for cand in AUTO_BAUD_ORDER:
        if cand == baud:
            continue
        try:
            ser = serial.Serial(port, cand, timeout=0.2, inter_byte_timeout=0.05)
        except serial.SerialException:
            continue
        # 窗口 4 秒: 设备日志可能是间歇突发(几秒一批), 短窗口会漏检
        data = _probe(ser, 4.0)
        if _looks_valid(data):
            # 二次确认: 再收 2.5 秒仍有效才算(单窗口偶然通过会误切)
            ser.reset_input_buffer()
            if _looks_valid(_probe(ser, 2.5)):
                print(f"[auto-baud] 检测到波特率 {cand}(两次确认), 已自动切换(原 {baud} {reason})", flush=True)
                return ser, cand
        ser.close()
    print("[auto-baud] 各档位均无有效数据, 按原波特率重试(设备可能没在打日志)", flush=True)
    return serial.Serial(port, baud, timeout=1, inter_byte_timeout=0.05), baud


def end_time_to_duration(end_str):
    """'HH:MM' 结束时间点 -> 距今秒数(已过则算明天)。"""
    from datetime import timedelta
    h, m = map(int, end_str.strip().split(":"))
    now = datetime.now()
    target = now.replace(hour=h, minute=m, second=0, microsecond=0)
    if target <= now:
        target += timedelta(days=1)
    return max(1, int((target - now).total_seconds()))


def notify_abnormal_mail(reason, out_path, line_count, byte_count, port, baud, warn=0, err=0):
    """异常中断自动发飞书邮件(失败仅打印, 不影响退出)。"""
    import subprocess
    subject = f"[异常] 串口采集中断 {port}@{baud}"
    body = (f"采集异常中断, 未达预定结束条件\n原因: {reason}\n"
            f"已收: {line_count} 行 / {byte_count} 字节\n"
            f"WARN: {warn} 行   ERROR: {err} 行\n日志: {out_path}\n"
            f"时间: {datetime.now():%Y-%m-%d %H:%M:%S}")
    try:
        r = subprocess.run(
            [sys.executable, str(SKILL_DIR / "scripts" / "common" / "send_mail.py"), subject, body, str(out_path)],
            capture_output=True, text=True, timeout=90, encoding="utf-8", errors="replace")
        print(f"[异常邮件] {r.stdout.strip()}", flush=True)
    except Exception as e:
        print(f"[异常邮件] 发送失败: {e}", file=sys.stderr, flush=True)


def notify_alert_mail(kind, hit_line, context_lines, out_path, line_count, byte_count,
                      port, baud, warn=0, err=0, alert_total=1):
    """告警邮件(只通知, 绝不停止采集)。

    触发场景: 采集中读到 ERROR / WARN / 用户指定正则(如 CheckCTS.*FATAL) 的行。
    与"结束条件"不同: 本函数仅发邮件, 采集循环继续跑, 不备份不退出。
    附件 = 当前日志快照副本; 正文 = 命中类型 + 命中行 + 最近上下文 + 进度。
    返回 (ok, msg)。"""
    import shutil
    import subprocess
    snap = subdir(ALERT_DIR_NAME) / f"{out_path.stem}_告警{datetime.now():%H%M%S}.log"
    try:
        if out_path.exists():
            shutil.copy2(out_path, snap)
        else:
            snap = None
    except OSError as e:
        snap = None
        print(f"[告警邮件] 快照复制失败: {e}", file=sys.stderr, flush=True)
    ctx = "\n".join(context_lines[-25:])
    subject = f"[告警] 串口日志命中 {kind} {port}@{baud} (第{alert_total}次)"
    body = (f"后台采集命中告警条件(采集仍在进行, 未停止)\n"
            f"命中类型: {kind}\n"
            f"命中行: {hit_line[:300]}\n"
            + "-" * 30 + f"\n最近上下文:\n{ctx}\n" + "-" * 30 + "\n"
            f"进度: {line_count} 行 / {byte_count} 字节\n"
            f"ERROR: {err} 行   WARN: {warn} 行   累计告警: {alert_total} 次\n"
            f"日志: {out_path}\n"
            f"时间: {datetime.now():%Y-%m-%d %H:%M:%S}")
    attaches = [str(snap)] if snap else []
    try:
        r = subprocess.run(
            [sys.executable, str(SKILL_DIR / "scripts" / "common" / "send_mail.py"), subject, body] + attaches,
            capture_output=True, text=True, timeout=90, encoding="utf-8", errors="replace")
        ok = "[OK]" in (r.stdout or "")
        return ok, (r.stdout or r.stderr or "").strip()[:200]
    except Exception as e:
        return False, str(e)


def run_analysis(out_path, mode, focus, top, keep, depth="medium", project=None):
    """调 analyze_log.py 出摘要(md) + 结构化结果(json), gen_report 出 HTML。
    depth=None 表示"有特殊要求, 强度不生效", 此时不传 --depth。
    project: config [projects] 的工程编号或工程根目录; 传 None 则 analyze_log 用 config default。
    返回 (md_text, html_path) ; 任一步失败返回 (None, None) 并打印原因。"""
    import subprocess
    rep = subdir(REPORT_DIR_NAME)
    md = rep / (out_path.stem + "_分析.md")
    js = rep / (out_path.stem + "_分析.json")
    html = rep / (out_path.stem + "_分析.html")
    try:
        cmd = [sys.executable, "-u", str(SKILL_DIR / "scripts" / "analyze" / "analyze_log.py"), str(out_path),
               "--mode", mode,
               "--md-out", str(md), "--json-out", str(js)]
        if depth:
            cmd += ["--depth", depth]
        if top:
            cmd += ["--top", str(top)]
        if keep:
            cmd += ["--keep", str(keep)]
        if focus:
            cmd += ["--focus", focus]
        if project:
            cmd += ["--project", str(project)]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300,
                           encoding="utf-8", errors="replace")
        if r.returncode != 0:
            print(f"[分析] 失败: {(r.stderr or r.stdout or '').strip()[:300]}", file=sys.stderr, flush=True)
            return None, None
        r2 = subprocess.run(
            [sys.executable, "-u", str(SKILL_DIR / "scripts" / "analyze" / "gen_report.py"), str(out_path),
             "--analysis", str(js), "--out", str(html)],
            capture_output=True, text=True, timeout=300, encoding="utf-8", errors="replace")
        if r2.returncode != 0:
            print(f"[分析] HTML 生成失败: {(r2.stderr or r2.stdout or '').strip()[:300]}",
                  file=sys.stderr, flush=True)
            html = None
        md_text = md.read_text(encoding="utf-8") if md.exists() else None
        strength = "不生效(按特殊要求)" if focus else depth
        print(f"[分析] 方式={mode} 强度={strength}" + (f" 特殊要求=/{focus}/" if focus else "")
              + (f" 工程={project}" if project else "")
              + f" -> {md.name}" + (f", {html.name}" if html else ""), flush=True)
        return md_text, html
    except Exception as e:
        print(f"[分析] 异常: {e}", file=sys.stderr, flush=True)
        return None, None


def notify_end_mail(end_reason, out_path, line_count, byte_count, port, baud,
                    warn=0, err=0, elapsed=0.0, analysis_text=None, html_path=None):
    """预设结束条件(时长/结束时间/命中关键字)达成后的完成邮件, 自动发送。
    附件 = 完成采集日志 + 分析 HTML; 正文 = 脚本生成的分析摘要。"""
    import subprocess
    subject = f"[已完成] 串口采集结束 {port}@{baud} ({line_count}行)"
    head = (f"采集按预设结束条件正常结束\n结束条件: {end_reason}\n"
            f"时长: {elapsed:.0f}s  已收: {line_count} 行 / {byte_count} 字节\n"
            f"ERROR: {err} 行   WARN: {warn} 行\n"
            f"时间: {datetime.now():%Y-%m-%d %H:%M:%S}\n"
            + "-" * 30 + "\n")
    body = head + (analysis_text if analysis_text else
                   "（分析未生成, 请查看附件日志; 可手动跑 analyze_log.py）")
    attaches = [str(out_path)]
    if html_path:
        attaches.append(str(html_path))
    try:
        r = subprocess.run(
            [sys.executable, str(SKILL_DIR / "scripts" / "common" / "send_mail.py"), subject, body] + attaches,
            capture_output=True, text=True, timeout=90, encoding="utf-8", errors="replace")
        print(f"[结束邮件] {r.stdout.strip()}", flush=True)
    except Exception as e:
        print(f"[结束邮件] 发送失败: {e}", file=sys.stderr, flush=True)


def send_mail_snapshot(out_path, line_count, byte_count, warn, err, req_note="",
                       analysis_mode=None, analysis_depth="medium", focus=None,
                       analysis_top=None, analysis_keep=None, project=None):
    """采集进行中发邮件: 复制当前 log 副本作附件, 采集不中断。
    可选: 按 analysis_mode/depth/focus 生成分析摘要进正文 + HTML 报告作第二附件。
    analysis_depth=None 表示有特殊要求(强度不生效)。
    project: 关联工程编号/路径(不传用 config default)。
    返回 (ok, msg)。"""
    import shutil
    import subprocess
    snap = subdir(SNAP_DIR_NAME) / f"{out_path.stem}_快照{datetime.now():%H%M%S}.log"
    try:
        if out_path.exists():
            shutil.copy2(out_path, snap)
    except OSError as e:
        return False, f"复制快照失败: {e}"

    analysis_text, html_path = (None, None)
    if analysis_mode:
        analysis_text, html_path = run_analysis(snap, analysis_mode, focus,
                                                analysis_top, analysis_keep, analysis_depth,
                                                project)

    subject = f"[采集中] 串口日志快照 {out_path.name} ({line_count}行)"
    head = (f"采集仍在进行, 本邮件为当前进度快照(采集未停止)\n"
            f"已收: {line_count} 行 / {byte_count} 字节\n"
            f"ERROR: {err} 行   WARN: {warn} 行\n"
            f"日志: {out_path}\n快照: {snap}\n"
            + (f"备注: {req_note}\n" if req_note else "")
            + f"时间: {datetime.now():%Y-%m-%d %H:%M:%S}\n" + "-" * 30 + "\n")
    body = head + (analysis_text if analysis_text else "（未指定分析方式, 未附分析结果）")
    attaches = [str(snap)]
    if html_path:
        attaches.append(str(html_path))
    try:
        r = subprocess.run(
            [sys.executable, str(SKILL_DIR / "scripts" / "common" / "send_mail.py"), subject, body] + attaches,
            capture_output=True, text=True, timeout=120, encoding="utf-8", errors="replace")
        ok = "[OK]" in (r.stdout or "")
        return ok, (r.stdout or r.stderr or "").strip()[:200]
    except Exception as e:
        return False, str(e)


def ctl_dir_for(out_path):
    """控制目录: logs/ctl/<log名>.ctl, 存放 status.json / cmd.json / 看门狗日志。
    (统一收进 ctl/ 子目录, 不散落在 logs 根目录)"""
    return subdir(CTL_DIR_NAME) / (out_path.stem + ".ctl")


def write_status(ctl_dir, state, info):
    """原子写 status.json(看门狗/外部工具据此判断是否异常中断)。

    健壮性修复: 采集心跳(写)/看门狗(读+异常时写)/capture_cmd 查询(读)三方并发
    碰同一文件, Windows 下 replace 覆盖被占文件报 WinError 5。对策:
    - tmp 名带 pid, 不与看门狗的 status.json.tmp 撞名
    - replace 失败重试 3 次(间隔 0.2s)
    - 仍失败只警告不抛异常: 写心跳失败绝不能杀采集主循环
      (终态 DONE/ABNORMAL 写失败时, 看门狗按 pid 消失/心跳超时兜底)
    """
    ctl_dir.mkdir(parents=True, exist_ok=True)
    data = {"state": state, "heartbeat": time.time(), "pid": os.getpid()}
    data.update(info)
    tmp = ctl_dir / f"status.json.tmp.{os.getpid()}"
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    dst = ctl_dir / "status.json"
    err = None
    for i in range(3):
        try:
            tmp.replace(dst)
            return
        except OSError as e:
            err = e
            if i < 2:
                time.sleep(0.2)
    print(f"[警告] status.json 写入失败(已重试3次): {err}; 不影响采集, 继续运行",
          file=sys.stderr, flush=True)
    try:
        tmp.unlink()
    except OSError:
        pass


def read_status(ctl_dir):
    f = ctl_dir / "status.json"
    if not f.exists():
        return None
    try:
        return json.loads(f.read_text(encoding="utf-8"))
    except Exception:
        return None


def start_watchdog(ctl_dir):
    """以独立进程启动看门狗: 采集进程异常消失(拔线/崩溃/被杀)时自动备份+发邮件。
    独立进程=不依赖 AI 判断, 也不随本进程终端一起死。"""
    import subprocess
    flags = 0
    if sys.platform == "win32":
        flags = 0x00000008 | 0x00000200  # DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP
    logf = open(ctl_dir / "watchdog.log", "a", encoding="utf-8")
    try:
        subprocess.Popen(
            [sys.executable, "-u", str(SKILL_DIR / "scripts" / "capture" / "capture_watchdog.py"), str(ctl_dir)],
            creationflags=flags, close_fds=True, cwd=str(SKILL_DIR),
            stdin=subprocess.DEVNULL, stdout=logf, stderr=logf)
        print(f"[看门狗] 已启动(异常中断将自动备份并发邮件): {ctl_dir}", flush=True)
    except Exception as e:
        print(f"[看门狗] 启动失败, 异常将无邮件通知: {e}", file=sys.stderr, flush=True)


def take_cmd(ctl_dir):
    """取走外部指令文件(capture_cmd.py 写入), 返回完整请求 dict 或 None。"""
    f = ctl_dir / "cmd.json"
    if not f.exists():
        return None
    try:
        req = json.loads(f.read_text(encoding="utf-8"))
    except Exception:
        req = {}
    try:
        f.unlink()
    except OSError:
        pass
    return req


LEVEL_RE = re.compile(r"^\[\d+\]\[([A-Za-z]+)\]")
LEVEL_MAP = {"DEBUG": "DEBUG", "INFO": "INFO", "WARN": "WARN", "ERROR": "ERROR",
             "D": "DEBUG", "I": "INFO", "W": "WARN", "E": "ERROR"}
# 无 level 字段时的兜底判据(与 serial_monitor 保持一致)
WARN_PAT = re.compile(r"retry|RETRY|timeout|TIMEOUT|Timeout|WARN|\[W\]")
ERR_PAT = re.compile(r"HardFault|CmBacktrace|ASSERT|assert|ERROR|ERR_|[Ee]rror|FAIL|fail")


def stamp_prefix():
    """落盘行首主机时间戳: [YYYY-MM-DD HH:MM:SS.mmm] (仅写文件时拼接, 与 Web 保存格式一致)"""
    now = datetime.now()
    return f"[{now:%Y-%m-%d %H:%M:%S}.{now.microsecond // 1000:03d}] ".encode("ascii")


def classify_line(text):
    """返回 'DEBUG'/'INFO'/'WARN'/'ERROR'。固定格式优先取 level 字段, 否则按关键词兜底。"""
    m = LEVEL_RE.match(text)
    if m and m.group(1).upper() in LEVEL_MAP:
        return LEVEL_MAP[m.group(1).upper()]
    if ERR_PAT.search(text):
        return "ERROR"
    if WARN_PAT.search(text):
        return "WARN"
    return "INFO"


def capture(port, baud, out, duration, echo=False, watch=False, stats_interval=10, auto_baud=False,
            stop_pattern=None, watchdog=True, analysis_mode=None, focus=None,
            analysis_top=None, analysis_keep=None, analysis_depth="medium", project=None,
            alert_on_error=False, alert_on_warn=False, alert_pattern=None, alert_cooldown=60):
    ser, real_baud = open_with_auto_baud(port, baud, auto_baud)
    baud = real_baud
    out_path = Path(out) if out else LOG_DIR / f"serial_{datetime.now():%Y%m%d_%H%M%S}.log"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    ctl_dir = ctl_dir_for(out_path)
    ctl_dir.mkdir(parents=True, exist_ok=True)
    if watchdog:
        start_watchdog(ctl_dir)
    write_status(ctl_dir, "RUNNING",
                 {"port": port, "baud": baud, "log": str(out_path), "end_reason": None,
                  "start": time.time()})

    mode = []
    if echo:
        mode.append("回显")
    if watch:
        mode.append("实时告警")
    mode_desc = "+".join(mode) if mode else "只存文件"
    end_desc = []
    if duration > 0:
        end_desc.append(f"时长{duration}s")
    if stop_pattern:
        end_desc.append(f"命中'{stop_pattern}'")
    print(f"开始采集({mode_desc}): {port} @ {baud}, 输出: {out_path}")
    print(f"结束条件: {(' + '.join(end_desc)) if end_desc else '仅手动停止'}", flush=True)
    if analysis_mode:
        mode_cn = {"fixed": "固定格式", "free": "自由格式", "auto": "自动判定"}[analysis_mode]
        if focus:
            print(f"结束分析: {mode_cn}  特殊要求只分析 /{focus}/ (严格按此分析, 强度不生效; HTML 仍全量)",
                  flush=True)
        else:
            depth_cn = {"low": "低(只看异常)", "medium": "中", "high": "高"}.get(analysis_depth, analysis_depth)
            print(f"结束分析: {mode_cn}  强度: {depth_cn} (ERROR/WARN 必分析)", flush=True)

    line_count = 0
    byte_count = 0
    alert_total = 0
    counters = {}
    warn_count = 0
    err_count = 0
    err_lines = []
    warn_lines = []
    start = time.time()
    last_stats = start
    last_hb = 0.0
    buf = bytearray()
    normal_end = False   # 正常结束(手动/时长/关键字命中)
    auto_end = False     # 预设结束条件达成(时长/结束时间/命中关键字) -> 结束后自动发完成邮件
    end_reason = "手动停止"
    pat_re = re.compile(stop_pattern) if stop_pattern else None
    pat_hit = None
    # 告警检测(只发邮件, 绝不停止): ERROR/WARN/用户指定正则, 每类独立冷却防刷屏
    alert_re = re.compile(alert_pattern) if alert_pattern else None
    alert_last = {}
    alert_mail_total = 0
    alert_ctx = []       # 最近若干行, 命中时作邮件上下文
    hb_info = {"port": port, "baud": baud, "log": str(out_path), "end_reason": None,
               "start": start}
    try:
        with open(out_path, "wb") as f:
            while duration <= 0 or (time.time() - start) < duration:
                # 心跳(1s一次): 看门狗据此判断进程是否假死
                now = time.time()
                if now - last_hb >= 1.0:
                    last_hb = now
                    hb_info.update({"lines": line_count, "bytes": byte_count,
                                    "warn": warn_count, "error": err_count})
                    write_status(ctl_dir, "RUNNING", hb_info)
                # 外部指令(capture_cmd.py): mail=发快照邮件但继续采集; stop=正常停止
                req = take_cmd(ctl_dir)
                if req:
                    cmd = req.get("cmd")
                    note = req.get("note", "")
                    # 指令可覆盖本次分析方式/强度/特殊要求(人工触发时由 AI 询问后传入)
                    c_mode = req.get("analysis_mode") or analysis_mode
                    c_focus = req.get("focus") if req.get("focus") is not None else focus
                    # 铁律: 有特殊要求时严格按用户要求分析, 强度不生效
                    c_depth = None if c_focus else (req.get("depth") or analysis_depth)
                    c_project = req.get("project") or project
                    if cmd == "mail":
                        f.flush()
                        ok, msg = send_mail_snapshot(out_path, line_count, byte_count,
                                                     warn_count, err_count, note,
                                                     analysis_mode=c_mode, analysis_depth=c_depth,
                                                     focus=c_focus, analysis_top=analysis_top,
                                                     analysis_keep=analysis_keep,
                                                     project=c_project)
                        print(f"[采集中邮件] {'已发送' if ok else '失败'}: {msg}", flush=True)
                    elif cmd == "stop":
                        normal_end = True
                        end_reason = "外部指令停止"
                        break

                data = ser.read(4096)
                if not data:
                    now = time.time()
                    if watch and stats_interval > 0 and now - last_stats >= stats_interval:
                        last_stats = now
                        print(f"[STATS] {int(now - start)}s 行={line_count} 字节={byte_count} 告警={alert_total} {counters}")
                    continue
                byte_count += len(data)
                line_count += data.count(b"\n")
                buf += data
                # 按换行切分, 保留不完整尾行
                if b"\n" in buf:
                    *lines, buf = buf.split(b"\n")
                    for ln in lines:
                        f.write(stamp_prefix() + ln + b"\n")
                        text = ln.decode("utf-8", errors="replace")
                        alert_ctx.append(text)
                        if len(alert_ctx) > 50:
                            del alert_ctx[:-50]
                        lv = classify_line(text)
                        if lv == "ERROR":
                            err_count += 1
                            if len(err_lines) < 50:
                                err_lines.append(text)
                        elif lv == "WARN":
                            warn_count += 1
                            if len(warn_lines) < 50:
                                warn_lines.append(text)
                        # 告警检测(只发邮件, 绝不停止采集): 三类各自独立冷却
                        if alert_on_error or alert_on_warn or alert_re:
                            kind = None
                            if alert_re and alert_re.search(text):
                                kind = f"指定关键字 /{alert_pattern}/"
                            elif alert_on_error and lv == "ERROR":
                                kind = "ERROR"
                            elif alert_on_warn and lv == "WARN":
                                kind = "WARN"
                            if kind:
                                key = kind[:20]
                                now_a = time.time()
                                if now_a - alert_last.get(key, 0) >= alert_cooldown:
                                    alert_last[key] = now_a
                                    alert_mail_total += 1
                                    print(f"[ALERT-MAIL] 命中 {kind}, 已触发告警邮件(采集继续): {text[:120]}",
                                          flush=True)
                                    threading.Thread(
                                        target=notify_alert_mail,
                                        args=(kind, text, list(alert_ctx), out_path,
                                              line_count, byte_count, port, baud,
                                              warn_count, err_count, alert_mail_total),
                                        daemon=True).start()
                        if watch:
                            tag = watch_line(text, counters)
                            if tag:
                                alert_total += 1
                                print(f"[ALERT][{tag}] {text}")
                            elif echo:
                                sys.stdout.buffer.write(ln + b"\n")
                                sys.stdout.flush()
                        elif echo:
                            sys.stdout.buffer.write(ln + b"\n")
                            sys.stdout.flush()
                        if pat_re and pat_hit is None and pat_re.search(text):
                            pat_hit = text
                    f.flush()
                    if pat_hit is not None:
                        # 命中结束条件: 再收 1 秒尾数据后正常收尾
                        end_reason = f"命中关键字: {pat_hit[:80]}"
                        tail_deadline = time.time() + 1.0
                        while time.time() < tail_deadline:
                            d2 = ser.read(4096)
                            if d2:
                                buf += d2
                                byte_count += len(d2)
                                line_count += d2.count(b"\n")
                                while b"\n" in buf:
                                    l2, buf = buf.split(b"\n", 1)
                                    f.write(stamp_prefix() + l2 + b"\n")
                        f.flush()
                        normal_end = True
                        auto_end = True   # 预设结束条件达成 -> 自动发完成邮件
                        break
                elif len(buf) > 4096:
                    # 保护: 波特率错误时乱码无换行, 强制落盘防数据滞留内存
                    f.write(stamp_prefix() + bytes(buf))
                    f.flush()
                    buf = bytearray()
                    now = time.time()
                    if watch and stats_interval > 0 and now - last_stats >= stats_interval:
                        last_stats = now
                        print(f"[STATS] {int(now - start)}s 行={line_count} 字节={byte_count} 告警={alert_total} {counters}")
            else:
                normal_end = True
                auto_end = True   # 时长达标 -> 自动发完成邮件
                end_reason = f"达到时长 {duration}s"
    except KeyboardInterrupt:
        normal_end = True
        end_reason = "手动停止(Ctrl+C)"
    except serial.SerialException as e:
        end_reason = f"串口异常: {e}"
        print(f"[异常] {end_reason}", file=sys.stderr, flush=True)
    except Exception as e:
        # 其他意外异常(OSError/进程被杀以外的一切): 同样走异常邮件通知
        end_reason = f"未预期异常 {type(e).__name__}: {e}"
        print(f"[异常] {end_reason}", file=sys.stderr, flush=True)
    finally:
        if buf:
            with open(out_path, "ab") as f:
                f.write(stamp_prefix() + bytes(buf))
        ser.close()

    elapsed = time.time() - start
    print("-" * 50, flush=True)
    print(f"采集结束({end_reason}): {out_path}")
    print(f"行数: {line_count}  字节: {byte_count}  时长: {elapsed:.1f}s  速率: {byte_count / max(elapsed, 0.001):.0f} B/s")
    print(f"ERROR: {err_count} 行   WARN: {warn_count} 行", flush=True)
    for t in err_lines[-10:]:
        print(f"  [ERROR] {t[:160]}", flush=True)
    for t in warn_lines[-10:]:
        print(f"  [WARN ] {t[:160]}", flush=True)
    if watch:
        print(f"告警总数: {alert_total}  明细: {counters}")

    if normal_end:
        # 正常结束: 主 log 改名加结束时间并归档到 完成采集/; 先写终态让看门狗退出(不重复发异常邮件)
        stamp = end_stamp()
        backup = subdir(FINISH_DIR_NAME) / f"{out_path.stem}_结束{stamp}.log"
        write_status(ctl_dir, "DONE",
                     {"end_reason": end_reason, "lines": line_count, "bytes": byte_count,
                      "warn": warn_count, "error": err_count, "log": str(out_path),
                      "backup": str(backup), "pid": os.getpid()})
        out_path = archive_main_log(out_path, stamp)
        print(f"已归档: {out_path}", flush=True)
        # 预设结束条件达成(时长/结束时间/命中关键字) -> 自动发完成邮件(附 log + 分析HTML)
        # 手动停止(Ctrl+C / capture_cmd stop)不发, 由 AI 先报 ERROR/WARN 再问用户
        if auto_end:
            analysis_text, html_path = (None, None)
            if analysis_mode:
                analysis_text, html_path = run_analysis(out_path, analysis_mode, focus,
                                                        analysis_top, analysis_keep, analysis_depth,
                                                        project)
            notify_end_mail(end_reason, out_path, line_count, byte_count, port, baud,
                            warn=warn_count, err=err_count, elapsed=elapsed,
                            analysis_text=analysis_text, html_path=html_path)
    else:
        # 异常中断(如串口拔出): 主 log 同样归档(带结束时间), 写异常终态, 再自行发邮件通知
        stamp = end_stamp()
        backup = subdir(FINISH_DIR_NAME) / f"{out_path.stem}_结束{stamp}.log"
        write_status(ctl_dir, "ABNORMAL",
                     {"end_reason": end_reason, "lines": line_count, "bytes": byte_count,
                      "warn": warn_count, "error": err_count, "log": str(out_path),
                      "backup": str(backup), "pid": os.getpid()})
        out_path = archive_main_log(out_path, stamp)
        notify_abnormal_mail(end_reason if end_reason != "手动停止" else "未知异常",
                             out_path, line_count, byte_count, port, baud,
                             warn=warn_count, err=err_count)
    return baud


def main():
    ap = argparse.ArgumentParser(description="串口日志采集")
    ap.add_argument("--list", action="store_true", help="列出可用串口")
    ap.add_argument("--port", help="串口号, 如 COM3")
    ap.add_argument("--baud", type=int, help="波特率, 默认 921600")
    ap.add_argument("--detect-baud", action="store_true", help="自动检测波特率(设备需正在打日志)")
    ap.add_argument("--echo", action="store_true", help="边存文件边实时回显到屏幕(供AI实时分析)")
    ap.add_argument("--watch", action="store_true", help="实时告警模式: 逐行规则检测, 命中打[ALERT]标记, 周期打[STATS]摘要(可与--echo同用)")
    ap.add_argument("--stats-interval", type=int, default=10, help="[STATS]摘要间隔秒数, 默认10, 0=关闭")
    ap.add_argument("--out", help="输出文件路径, 默认 output/logs/serial_时间戳.log")
    ap.add_argument("--duration", type=int, default=0, help="采集时长(秒), 0=不限")
    ap.add_argument("--end-time", help="结束时间点 HH:MM(24h, 已过算明天), 与--duration 二选一")
    ap.add_argument("--stop-pattern", help="结束条件: 读到匹配该正则的日志行后停止(可组合)")
    ap.add_argument("--save-config", action="store_true", help="保存本次串口/波特率到 config.conf")
    ap.add_argument("--confirm", action="store_true",
                    help="门禁: 必须已向用户确认采集意图(模式+输出位置)后才可启动")
    ap.add_argument("--auto-baud", action="store_true",
                    help="启动后5秒无数据自动逐档检测波特率并切换(强烈建议默认加此参数)")
    ap.add_argument("--end-cond", choices=["unlimited", "duration", "end-time", "stop-pattern"],
                    help="门禁: 必须明确告知用户并选定结束条件(第四问), 缺省拒绝启动")
    ap.add_argument("--no-watchdog", action="store_true",
                    help="不启动看门狗(默认启动: 异常中断自动备份+发邮件)")
    ap.add_argument("--analysis-mode", choices=["fixed", "free", "auto"],
                    help="门禁: 结束时分析方式(第五问) fixed/free/auto, 必须显式声明")
    ap.add_argument("--analysis-depth", choices=["low", "medium", "high"],
                    help="分析强度(第七问) low/medium/high: 仅在没有特殊要求(--focus)时才需要; "
                         "三档都必然分析 ERROR/WARN(见 references/analysis_depth.md)")
    ap.add_argument("--focus", help="第六问(可选): 特殊要求, 只分析匹配该正则的行(邮件正文); HTML 仍全量; 有此项时强度不生效")
    ap.add_argument("--alert-on-error", action="store_true",
                    help="告警: 采集中读到 ERROR 行即发邮件提醒(采集继续, 不停止)")
    ap.add_argument("--alert-on-warn", action="store_true",
                    help="告警: 采集中读到 WARN 行即发邮件提醒(采集继续, 不停止)")
    ap.add_argument("--alert-pattern",
                    help="告警: 采集中读到匹配该正则的行即发邮件提醒(采集继续, 不停止), 如 \"CheckCTS.*FATAL\"")
    ap.add_argument("--alert-cooldown", type=int, default=60,
                    help="同类告警邮件最小间隔秒数, 默认60, 防刷屏")
    ap.add_argument("--project",
                    help="关联工程: config [projects] 的编号(如 2)或工程根目录绝对路径; "
                         "不传则用 config 的 default; 都没有则不按工程分析(结论不关联代码)")
    ap.add_argument("--list-projects", action="store_true",
                    help="列出 config [projects] 登记的工程与默认工程后退出")
    ap.add_argument("--analysis-top", type=int, help="分析展示热点/高频条数(默认由强度决定)")
    ap.add_argument("--analysis-keep", type=int, help="分析明细保留上限(默认由强度决定)")
    args = ap.parse_args()

    if args.list:
        list_ports()
        return
    if args.list_projects:
        projects, default = load_projects()
        if not projects:
            print(f"config 未登记任何工程: {CONFIG_FILE}")
            return
        print(f"工程注册表: {CONFIG_FILE}")
        for k, v in projects.items():
            print(f"  {k} = {v}" + ("  <- 默认" if k == default else ""))
        print("默认工程: " + (default or "(未设置 -> 每次分析需询问用哪个工程)"))
        return
    if not args.port:
        print("错误: 需要 --port 或 --list", file=sys.stderr)
        sys.exit(1)

    # 工程关联门禁: config [projects] 有 default 就直接用(分析与结论都按工程来);
    # 没有 default 则 AI 必须先问用户用哪个工程, 用户不回答 -> 不按工程分析(结论不关联代码)
    projects, pj_default = load_projects()
    proj = args.project or pj_default
    if proj:
        where = projects.get(proj)
        if where:
            print(f"[工程] 关联 {proj} = {where}" + ("" if args.project else "  (config 默认)"))
        else:
            print(f"[工程] 关联 {proj} (直接路径, 或 config 无此编号)")
    else:
        print("[工程] config [projects] 无 default 且未传 --project:")
        print("       AI 必须先问用户【本次分析关联哪个工程】, 用户答复后带 --project <编号|路径> 重启;")
        print("       用户不回答 -> 分析结果与结论都不关联工程代码。候选工程见 --list-projects")

    # --detect-baud 是查询性质, 不需要门禁; 真正进入采集前必须已确认
    if args.detect_baud:
        cfg = load_config()
        port = args.port or cfg.get("port", "")
        baud = args.baud or int(cfg.get("baud", 921600))
        detected = detect_baud(port)
        if detected is None:
            sys.exit(1)
        print(f"提示: 确认采集时用 --baud {detected}")
        return

    if not args.confirm:
        print("拒绝启动: 未确认采集意图。", file=sys.stderr)
        print("AI 必须先向用户确认【1.模式(实时查看/后台写入) 2.日志输出位置(默认/自定义)】两项,", file=sys.stderr)
        print("用户明确答复后, 才允许带 --confirm 参数重启本命令。", file=sys.stderr)
        sys.exit(1)

    # 第四问硬门禁: 结束条件必须显式声明, 缺省拒绝启动(防 AI 跳过交互后无限跑飞)
    if not args.end_cond:
        print("拒绝启动: 未声明结束条件。", file=sys.stderr)
        print("AI 必须先问用户第四问【结束条件】并选定其一后带上对应参数重启:", file=sys.stderr)
        print("  --end-cond unlimited    (不限, 直到用户主动停止)", file=sys.stderr)
        print("  --end-cond duration     (配 --duration 秒)", file=sys.stderr)
        print("  --end-cond end-time     (配 --end-time HH:MM)", file=sys.stderr)
        print("  --end-cond stop-pattern (配 --stop-pattern \"正则\")", file=sys.stderr)
        sys.exit(1)
    if args.end_cond == "duration" and args.duration <= 0:
        print("错误: --end-cond duration 需同时给 --duration 秒数", file=sys.stderr)
        sys.exit(1)
    if args.end_cond == "end-time" and not args.end_time:
        print("错误: --end-cond end-time 需同时给 --end-time HH:MM", file=sys.stderr)
        sys.exit(1)
    if args.end_cond == "stop-pattern" and not args.stop_pattern:
        print("错误: --end-cond stop-pattern 需同时给 --stop-pattern \"正则\"", file=sys.stderr)
        sys.exit(1)
    if args.end_cond == "unlimited":
        print("[门禁] 结束条件=不限: 进程不会自行结束, 只能靠用户要求停止或异常中断。")

    # 第五/六/七问硬门禁: 分析方式必须声明; 强度仅在"没有特殊要求"时才需要
    # 铁律: 有 --focus(特殊要求) 时, 严格按用户要求分析, 强度不生效 -> 不再要求 --analysis-depth
    auto_mail_end = args.end_cond in ("duration", "end-time", "stop-pattern")
    need = [("--analysis-mode(分析方式, 第五问)", args.analysis_mode)]
    if not args.focus:
        need.append(("--analysis-depth(分析强度, 第七问)", args.analysis_depth))
    missing = [k for k, v in need if not v]
    if auto_mail_end and missing:
        print(f"拒绝启动: 未声明 {' 和 '.join(missing)}。", file=sys.stderr)
        print("设了预设结束条件(时长/结束时间/命中关键字)则结束时自动发邮件, 邮件正文需要分析结果,", file=sys.stderr)
        print("AI 必须先问用户分析方式, 并带齐参数重启:", file=sys.stderr)
        print("  --analysis-mode fixed   固定格式分析(按 module/level/内容聚合, 适合 [ts][LEVEL][file:line][module])", file=sys.stderr)
        print("  --analysis-mode free    自由格式分析(消息形状去重+关键词分级, 适合无结构裸打印)", file=sys.stderr)
        print("  --analysis-mode auto    让脚本采样判定(固定格式占比>=50%用 fixed, 否则 free)", file=sys.stderr)
        print("  --analysis-depth low|medium|high   结束分析强度(第七问, 仅当没有特殊要求时才问):", file=sys.stderr)
        print("      low=只看异常(结论+热点+ERROR/WARN明细)  medium=中等(推荐)  high=全维度聚合+逐行挂分析", file=sys.stderr)
        print("      (三档都必然分析 ERROR 与 WARN, 强度只影响其他章节多少)", file=sys.stderr)
        print("  --focus \"正则\"           特殊要求(第六问, 可选): 有则严格按此分析,", file=sys.stderr)
        print("      邮件正文只分析匹配行 / 强度参数失效不作要求 / HTML 仍为全量", file=sys.stderr)
        print("  定义详见 references/analysis_depth.md 与 references/analysis_modes.md", file=sys.stderr)
        sys.exit(1)
    if args.focus:
        # 有特殊要求: 强度不参与, 不校验其取值
        args.analysis_depth = None
    elif args.analysis_depth is None:
        args.analysis_depth = "medium"   # unlimited 场景(不自动发邮件)给个默认, 手动发时再问
    if args.focus:
        try:
            re.compile(args.focus)
        except re.error as e:
            print(f"错误: --focus 正则非法: {e}", file=sys.stderr)
            sys.exit(1)
        print(f"[门禁] 特殊要求 --focus /{args.focus}/ 已生效: 严格按此分析, 分析强度不生效; HTML 报告仍为全量。")

    if args.alert_pattern:
        try:
            re.compile(args.alert_pattern)
        except re.error as e:
            print(f"错误: --alert-pattern 正则非法: {e}", file=sys.stderr)
            sys.exit(1)
    if args.alert_on_error or args.alert_on_warn or args.alert_pattern:
        parts = []
        if args.alert_on_error:
            parts.append("ERROR")
        if args.alert_on_warn:
            parts.append("WARN")
        if args.alert_pattern:
            parts.append(f"关键字/{args.alert_pattern}/")
        print(f"[门禁] 告警模式已开启: 命中 {' + '.join(parts)} 即发邮件(采集继续, 不停止); "
              f"同类冷却 {args.alert_cooldown}s")

    cfg = load_config()
    port = args.port or cfg.get("port", "")
    baud = args.baud or int(cfg.get("baud", 921600))

    duration = args.duration
    if args.end_time:
        if duration > 0:
            print("错误: --end-time 与 --duration 只能二选一", file=sys.stderr)
            sys.exit(1)
        try:
            duration = end_time_to_duration(args.end_time)
            print(f"结束时间 {args.end_time} -> 还剩 {duration}s")
        except ValueError:
            print("错误: --end-time 格式应为 HH:MM", file=sys.stderr)
            sys.exit(1)

    try:
        real_baud = capture(port, baud, args.out, duration,
                            echo=args.echo, watch=args.watch, stats_interval=args.stats_interval,
                            auto_baud=args.auto_baud, stop_pattern=args.stop_pattern,
                            watchdog=not args.no_watchdog,
                            analysis_mode=args.analysis_mode, focus=args.focus,
                            analysis_top=args.analysis_top, analysis_keep=args.analysis_keep,
                            analysis_depth=args.analysis_depth, project=args.project or proj,
                            alert_on_error=args.alert_on_error, alert_on_warn=args.alert_on_warn,
                            alert_pattern=args.alert_pattern, alert_cooldown=args.alert_cooldown)
        baud = real_baud  # auto-baud 切换后保存实际波特率
    except serial.SerialException as e:
        print(f"错误: {e}", file=sys.stderr)
        sys.exit(1)

    if args.save_config:
        save_config(port, baud)


if __name__ == "__main__":
    main()
