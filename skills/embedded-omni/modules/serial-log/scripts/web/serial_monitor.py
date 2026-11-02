#!/usr/bin/env python3
"""Web 实时串口监视器: 浏览器打开 http://localhost:8765 持续滚动显示。

特性:
  - 启动只起 Web 服务, 不打开串口; 串口/波特率/检测全部在网页操作
  - 网页顶部: 串口下拉+刷新 / 波特率(下拉候选[config bauds]+手填) / 自动检测波特率(检测成功回填波特率框) / 连接·断开(直连波特率框的值,不自动检测) / 查看详情
  - 背景: assets/ 目录放图片即被网页默认加载(第一张), 可覆盖换肤; 无图则纯色
  - "查看详情"弹窗: 逐项诊断为什么未连接/当前错误(串口数、目标口存在性、占用探测、最近错误)
  - 实时查看模式不写 log(数据在内存), 用网页"保存日志"按钮落盘(默认/自定义路径, 可选发飞书邮件)
  - level 全称显示: DEBUG/INFO/WARN/ERROR(按内容规则推断, 固件加 level 后优先取字段)
  - ERROR/WARN 行下方即时显示分析(内置规则库)
  - 选中行 -> "AI分析选中"按钮 -> 提交到 selection_pending.json, AI 分析后
    POST /ai_result 注入回网页显示

用法:
  python serial_monitor.py --confirm
  python serial_monitor.py --confirm --port COM6 --web-port 8766
"""
import argparse
import json
import re
import sys
import threading
import time
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "capture"))
from capture_serial import (load_config, load_log_dir, open_with_auto_baud, run_analysis,
                            detect_baud, BAUD_CANDIDATES)  # 复用 config + auto-baud + 分析链路(同域 scripts/capture/)

try:
    import serial
    import serial.tools.list_ports
except ImportError:
    print("错误: 缺少 pyserial, 请执行: python -m pip install pyserial", file=sys.stderr)
    sys.exit(1)

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

SKILL_DIR = Path(__file__).resolve().parent.parent.parent   # scripts/web/ -> skill 根
LOG_DIR = load_log_dir()   # 复用 capture_serial.load_log_dir: config [log] dir, 缺省 <skill>/output/logs
ASSETS_DIR = SKILL_DIR / "assets"        # 用户自定义素材(背景图等), 放里面即被网页加载
BG_EXT = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
          ".webp": "image/webp", ".gif": "image/gif", ".bmp": "image/bmp"}

TS_RE = re.compile(r"^\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3})\]\s?")


def get_baud_candidates():
    """波特率候选: 优先 config [serial] bauds(逗号分隔), 缺省用内置常用档。"""
    raw = load_config().get("bauds", "")
    out = []
    for x in raw.split(","):
        x = x.strip()
        if x.isdigit():
            out.append(int(x))
    return out or list(BAUD_CANDIDATES)


def list_assets():
    """assets 目录下的图片文件名(排序), 供网页选背景。"""
    if not ASSETS_DIR.exists():
        return []
    return sorted(p.name for p in ASSETS_DIR.iterdir()
                  if p.is_file() and p.suffix.lower() in BG_EXT)


def list_log_files():
    """output/logs 下的日志文件(按修改时间倒序), 供网页"打开日志"选文件。"""
    if not LOG_DIR.exists():
        return []
    out = []
    for p in LOG_DIR.iterdir():
        if p.is_file() and p.suffix.lower() in (".log", ".txt"):
            try:
                st = p.stat()
            except OSError:
                continue
            out.append({"name": p.name, "size": st.st_size, "mtime": st.st_mtime})
    out.sort(key=lambda x: x["mtime"], reverse=True)
    return out


def load_log_file(name):
    """读取 output/logs 下的日志文件, 转成与 /stream 一致的行结构,
    使网页的文件视图能复用全部过滤(仅WARN/ERROR、关键词、ASCII/HEX)。
    落盘格式为 '[YYYY-MM-DD HH:MM:SS.mmm] 正文'(行首主机时间戳, 写文件时拼接),
    此处把行首时间提取为 ts, 供网页把时间统一显示在行首。"""
    safe = Path(name).name
    fp = LOG_DIR / safe
    if not safe or not fp.is_file():
        return {"ok": False, "err": "文件不存在"}
    try:
        with open(fp, "r", encoding="utf-8", errors="replace", newline="") as fh:
            text = fh.read()
    except Exception as e:
        return {"ok": False, "err": str(e)}
    items = []
    for i, raw in enumerate(text.split("\n"), 1):
        ln = raw.rstrip("\r")
        if ln.rstrip() == "":
            continue
        ts = 0.0
        m = TS_RE.match(ln)
        if m:
            ln = ln[m.end():]
            try:
                ts = datetime.strptime(m.group(1), "%Y-%m-%d %H:%M:%S.%f").timestamp()
            except ValueError:
                ts = 0.0
        level, insight = classify(ln)
        items.append({"s": i, "ts": ts, "t": ln, "h": ln.encode("utf-8").hex(" ").upper(),
                      "l": level, "i": insight})
    return {"ok": True, "name": safe, "count": len(items), "lines": items}

# ---------------------------------------------------------------------------
# 告警规则: (正则, 级别全称, 即时分析文字)
LEVEL_RULES = [
    (r"HardFault|CmBacktrace|ASSERT|assert", "ERROR",
     "固件崩溃级事件: 建议停止采集后跑 gen_report.py 看崩溃前上下文, 检查最近改动的指针/数组越界"),
    (r"ERR_BUF_FULL|ERR_DISCONN", "ERROR",
     "USB 日志通道异常: BUF_FULL=发送队列积压(APK没接收), DISCONN=USB断开; 串口日志不受影响, 但需检查上位机连接"),
    (r"DTC_|FAULT DETECTED", "ERROR",
     "硬件故障检测(DTC): 按信号名查对应传感器/天线连接, 确认后可清故障复测"),
    (r"SendWithAck FAILED", "ERROR",
     "消息重试3次无ACK: APK侧未确认, 检查APK是否在线/协议版本是否匹配"),
    (r"ERROR|ERR_|error|fail|FAIL", "ERROR",
     "错误级日志: 关注其前后5行上下文定位触发时机"),
    (r"retry|RETRY|timeout|TIMEOUT|Timeout", "WARN",
     "重试/超时: 偶发可忽略, 短时间密集出现说明通信质量或负载异常"),
    (r"\[W\]|WARN", "WARN",
     "警告级日志: 不致命但需关注"),
    (r"Init|Success|start", "INFO",
     ""),
]

# 固件新格式带 level 字段时的直接映射
LEVEL_MAP = {"DEBUG": "DEBUG", "INFO": "INFO", "WARN": "WARN", "ERROR": "ERROR",
             "D": "DEBUG", "I": "INFO", "W": "WARN", "E": "ERROR"}


def classify(text):
    """返回 (level全称, 即时分析文字或None)。"""
    m = re.match(r"^\[\d+\]\[([A-Za-z]+)\]", text)
    if m and m.group(1).upper() in LEVEL_MAP:
        lvl = LEVEL_MAP[m.group(1).upper()]
        insight = ""
        for pattern, level, tip in LEVEL_RULES:
            if lvl == level and re.search(pattern, text):
                insight = tip
                break
        return lvl, insight or None
    for pattern, level, tip in LEVEL_RULES:
        if re.search(pattern, text):
            return level, tip or None
    return "INFO", None


# ---------------------------------------------------------------------------
history = []            # [(seq, ts, text, hexs, level, insight)]  ts=系统时间, hexs=原始字节HEX
# 网页新连接(刷新/首开, 即 since=0)时只回放最近 N 行, 避免把整段内存缓冲重放导致满屏;
# <=0 表示回放全部(旧行为)。可用 --replay-tail 覆盖。
REPLAY_TAIL = 200
# 兜底冲刷阈值(reader_loop 用): 串口静默这么久仍有残留字节 -> 补成一行;
# 残留攒到这么多字节仍无换行 -> 分块吐出。波特率错时乱码常无 0x0A, 靠这两条保证"收了就能看见"。
FLUSH_IDLE = 0.25       # 秒
FLUSH_MAX = 1024        # 字节
ai_results = []         # [{"id":n,"ts":..,"text":..}] AI注入的分析结果
selection_req = None    # {"id":n,"ts":..,"lines":[...]} 最近一次选中的行
lock = threading.Lock()
seq = 0
rx_bytes = 0            # 自本次连接起收到的原始字节数(不含成行与否), 网页据此判断"到底有没有收到"
ai_seq = 0

# 连接状态(网页控制): 启动不再打开串口, 全部由网页 /connect 触发
conn = {
    "ser": None,        # serial.Serial 或 None
    "port": "",         # 当前串口, 如 COM6
    "baud": 0,          # 实际波特率
    "open": False,      # 是否已连接
    "msg": "未连接",     # 状态描述(展示给网页)
    "err": "",          # 最近一次错误
    "thread": None,     # 读取线程
    "epoch": 0,         # 连接代数(断开后旧线程据此自杀, 防止串到新连接)
    "preset": "",       # 启动时 --port 传入的预选串口(仅作网页下拉默认)
    "connecting": False,  # 正在打开/auto-baud 中(阻塞期间拒绝重复 /connect)
}


def reader_loop(ser, epoch):
    """读取线程: ser 变化/断开(epoch 不匹配)时自行退出。

    成行策略 = 换行优先 + 兜底冲刷:
      1) 有 b"\\n" 就正常切行(设备日志的主路径);
      2) 残留字节攒够 FLUSH_MAX 仍无换行 -> 分块吐出
         (波特率错时乱码流里可能长时间没有 0x0A, 不吐就永远不显示);
      3) 残留字节自首个起停留满 FLUSH_IDLE 秒 -> 整体补成一行
         (设备只用 \\r 结尾 / 行尾被截断 / 乱码尾包)。
    计时基准是"残留首字节的时刻"而非"最后收到数据的时刻": 波特率错时字节是连续不断的,
    若按后者则永远在刷新, 一行都吐不出来。这样 行:N 会随时增长, ASCII 视图显示 \\ufffd、
    切 HEX 看原始字节, 从而"到底有没有收到"一眼可辨。
    """
    global seq, rx_bytes
    buf = b""
    buf_start = None   # buf 中首个残留字节的时刻; buf 为空时置 None
    while True:
        with lock:
            if conn["epoch"] != epoch or conn["ser"] is not ser:
                return
        try:
            data = ser.read(4096)
        except (serial.SerialException, OSError) as e:
            with lock:
                if conn["epoch"] == epoch:
                    conn["open"] = False
                    conn["err"] = f"串口断开: {e}"
                    conn["msg"] = conn["err"]
                    try:
                        ser.close()
                    except Exception:
                        pass
                    conn["ser"] = None
            print(f"[异常] 串口断开: {e}", file=sys.stderr, flush=True)
            return
        now = time.time()
        if data:
            if not buf:
                buf_start = now
            buf += data
            with lock:
                rx_bytes += len(data)   # 收到即计数: 与是否成行无关, 用于回答"到底有没有收到"
        lines = []
        while b"\n" in buf:
            ln, buf = buf.split(b"\n", 1)
            lines.append(ln)
        while len(buf) >= FLUSH_MAX:
            lines.append(buf[:FLUSH_MAX])
            buf = buf[FLUSH_MAX:]
        if buf and buf_start is not None and now - buf_start >= FLUSH_IDLE:
            lines.append(buf)
            buf = b""
        if not buf:
            buf_start = None
        for ln in lines:
            text = ln.decode("utf-8", errors="replace").rstrip("\r")
            hexs = ln.hex(" ").upper()
            level, insight = classify(text)
            with lock:
                seq += 1
                history.append((seq, time.time(), text, hexs, level, insight))
                if len(history) > 8000:
                    del history[:2000]


def get_ports():
    """列出可用串口: [{"device": "COM6", "desc": "..."}]"""
    return [{"device": p.device, "desc": (p.description or "").strip()}
            for p in serial.tools.list_ports.comports()]


def do_connect(port, baud, auto_baud):
    """网页触发连接: 打开串口(可选 auto-baud)并启动读取线程。返回 (ok, msg)。"""
    global seq, rx_bytes
    port = (port or "").strip()
    if not port:
        return False, "未选择串口"
    try:
        baud = int(baud)
    except (TypeError, ValueError):
        return False, "波特率非法"
    with lock:
        if conn["open"]:
            return False, f"已连接 {conn['port']}@{conn['baud']}, 请先断开"
        if conn["connecting"]:
            return False, "正在连接中, 请稍候(勿重复点击)"
        if _detect_busy:
            return False, "自动检测波特率进行中(约20秒), 等它结束或稍后再连接"
        conn["connecting"] = True
        conn["epoch"] += 1
        epoch = conn["epoch"]
    try:
        ser, real_baud = open_with_auto_baud(port, baud, auto_baud)
    except serial.SerialException as e:
        with lock:
            conn["open"] = False
            conn["connecting"] = False
            conn["err"] = str(e)
            conn["msg"] = f"打开失败: {e}"
        return False, f"打开串口失败: {e}"
    except Exception as e:
        with lock:
            conn["open"] = False
            conn["connecting"] = False
            conn["err"] = str(e)
            conn["msg"] = f"打开失败: {e}"
        return False, f"打开串口失败: {e}"
    with lock:
        history.clear()
        seq = 0
        rx_bytes = 0
        conn["ser"] = ser
        conn["port"] = port
        conn["baud"] = real_baud
        conn["open"] = True
        conn["connecting"] = False
        conn["err"] = ""
        conn["msg"] = f"已连接 {port} @ {real_baud}"
        t = threading.Thread(target=reader_loop, args=(ser, epoch), daemon=True)
        conn["thread"] = t
    t.start()
    return True, conn["msg"]


def do_disconnect():
    """网页触发断开: 停线程 + 关串口。返回 (ok, msg)。"""
    with lock:
        conn["epoch"] += 1
        ser = conn["ser"]
        conn["ser"] = None
        conn["open"] = False
        conn["msg"] = "已断开"
        conn["baud"] = 0
    if ser is not None:
        try:
            ser.close()
        except Exception:
            pass
    return True, "已断开"


_detect_busy = False  # 自动检测互斥: 全程约 11档×1.8s≈20s, 期间拒绝并发检测/连接(防两口输出混流、抢串口)
_detect_stop = threading.Event()  # 手动停止: 网页"停止检测"置位, detect_baud 每档开始前检查


def do_detect(port, candidates=None):
    """网页触发自动检测波特率: 复用 capture_serial.detect_baud。返回 (ok, baud|None, note)。"""
    global _detect_busy
    port = (port or "").strip()
    if not port:
        return False, None, "未选择串口"
    with lock:
        if _detect_busy:
            return False, None, "自动检测进行中(约20秒), 请等本轮结束"
        if conn["open"]:
            return False, None, f"检测需独占串口, 请先断开 {conn['port']}"
        _detect_busy = True
    _detect_stop.clear()
    try:
        b = detect_baud(port, candidates or BAUD_CANDIDATES, stop_event=_detect_stop)
    except serial.SerialException as e:
        return False, None, f"检测失败: {e}"
    except Exception as e:
        return False, None, f"检测失败: {e}"
    finally:
        with lock:
            _detect_busy = False
    if _detect_stop.is_set():
        return False, None, "已手动停止检测"
    if b is None:
        return False, None, "各档位均无有效数据(设备需正在打日志)"
    return True, b, f"检测到波特率 {b}"


def do_diag(port=None, probe=True):
    """连接诊断: 解释'为什么未连接'与当前错误, 供网页'查看详情'弹窗。

    probe=True : 附带"串口占用探测"(会真的试开一次串口, 仅弹窗用)
    probe=False: 不碰硬件(供顶部徽标高频轮询, 避免反复拉 DTR 复位 MCU)
    """
    cfg = load_config()
    with lock:
        open_now = conn["open"]
        cur_port = conn["port"]
        cur_baud = conn["baud"]
        last_err = conn["err"]
        msg = conn["msg"]
    ports = get_ports()
    devices = [p["device"] for p in ports]
    target = (port or cur_port or cfg.get("port", "") or "").strip()
    checks = []

    checks.append({
        "name": "串口服务",
        "ok": True,
        "detail": f"Web 服务运行中, 页面端口正常 (启动模式: 仅起服务, 不自动打开串口)",
    })
    checks.append({
        "name": "系统串口数量",
        "ok": bool(ports),
        "detail": (f"发现 {len(ports)} 个: {', '.join(devices)}" if ports
                   else "未发现任何串口 —— 检查 USB 线是否插好、CH340 驱动是否安装"),
    })
    if target:
        present = target in devices
        checks.append({
            "name": f"目标串口 {target}",
            "ok": present,
            "detail": (f"{target} 在系统中存在" if present
                       else f"{target} 不在系统列表里 —— 可能被拔掉/换口/COM号变了, 点'刷新'重扫"),
        })
    else:
        checks.append({
            "name": "目标串口",
            "ok": False,
            "detail": "未选择串口 —— 请在上方下拉框选择(为空则先插 USB 并点'刷新')",
        })

    if open_now:
        checks.append({
            "name": "连接状态",
            "ok": True,
            "detail": f"已连接 {cur_port} @ {cur_baud}, 正在接收数据",
        })
    else:
        checks.append({
            "name": "连接状态",
            "ok": False,
            "detail": (f"未连接。最近错误: {last_err}" if last_err
                       else "未连接(尚未点击'连接', 或被手动断开)"),
        })

    # 尝试独占打开, 判断是否被别的程序(采集进程/串口助手)占用
    # 已连接时串口正被本服务独占, 再试开必然失败 -> 会误报, 故跳过
    if probe and not open_now and target and target in devices:
        probe_ok, probe_detail = True, "串口可被本服务打开"
        try:
            _p = serial.Serial(target, int(cfg.get("baud") or 921600), timeout=0.1)
            _p.close()
        except serial.SerialException as e:
            probe_ok = False
            probe_detail = f"串口无法打开: {e} (常被其它程序占用, 可跑 find_com_holder.py {target} 查占用)"
        except Exception as e:
            probe_ok = False
            probe_detail = f"串口探测异常: {e}"
        checks.append({"name": "串口占用探测", "ok": probe_ok, "detail": probe_detail})

    ok_all = all(c["ok"] for c in checks)
    return {
        "ok": ok_all,
        "connected": open_now,
        "port": target,
        "baud": cur_baud,
        "msg": msg,
        "err": last_err,
        "config": {"port": cfg.get("port", ""), "baud": cfg.get("baud", "")},
        "assets": list_assets(),
        "checks": checks,
    }


def dump_history(path):
    with lock:
        items = list(history)
    with open(path, "w", encoding="utf-8") as f:
        for _, ts, text, _, _, _ in items:
            stamp = datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            f.write("[" + stamp + "] " + text.rstrip("\r") + "\n")
    return len(items)


def level_counts():
    """统计 WARN/ERROR 行数与明细(供 AI 汇报"先告诉我是否有error,warn")。"""
    with lock:
        items = list(history)
    warns = [t for _, _, t, _, l, _ in items if l == "WARN"]
    errs = [t for _, _, t, _, l, _ in items if l == "ERROR"]
    return {"total": len(items), "warn": len(warns), "error": len(errs),
            "error_lines": errs[-50:], "warn_lines": warns[-50:]}


# ---------------------------------------------------------------------------
HTML = """<!DOCTYPE html><html><head><meta charset="utf-8">
<title>Serial Monitor</title>
<style>
body{font-family:Consolas,monospace;margin:0;color:#ccc;
background:#0e1116 var(--bg) center/cover fixed no-repeat}
body::before{content:'';position:fixed;inset:0;z-index:-1;
background:linear-gradient(180deg,rgba(10,12,16,.82),rgba(10,12,16,.90))}
#bar{position:fixed;top:0;left:0;right:0;background:rgba(20,24,30,.85);backdrop-filter:blur(6px);
border-bottom:1px solid #2a3340;padding:8px 12px;display:flex;gap:14px;align-items:center;font-size:13px;z-index:2;flex-wrap:wrap}
#log{padding:6px 12px;font-size:13px;line-height:1.45;white-space:pre-wrap;word-break:break-all}
.lv{font-weight:bold;margin-right:4px;border-radius:2px;padding:0 3px}
.DEBUG{color:#8a93a3}.INFO{color:#8fd694}.WARN{color:#ffb038}.ERROR{color:#ff6b6b}
.insight{color:#7cc7ff;font-style:italic;padding-left:48px;font-size:12px}
.sel{background:rgba(38,79,120,.75);border-radius:2px}
.ts{color:#6b7480;margin-right:6px;font-size:12px}
.ln{color:#5a6472;margin-right:8px;font-size:12px;display:inline-block;min-width:46px;text-align:right;user-select:none}
.hex{color:#8fd6a0;font-family:Consolas,monospace;font-size:12px}
mark{background:#ffd54a;color:#1a1a1a;border-radius:2px;padding:0 1px}
#filteropts{display:none;gap:6px;align-items:center}
#filteropts.on{display:inline-flex}
#filteropts button{font-size:11px;padding:2px 8px}
#filtertag{display:none;font-size:12px;color:#ffd54a;cursor:pointer;user-select:none;
background:rgba(120,100,20,.25);border:1px solid rgba(255,213,74,.45);border-radius:10px;padding:1px 8px}
#filtertag.on{display:inline-block}
#btnReHelp{font-size:15px;line-height:1;padding:3px 9px;font-weight:bold}
#reHelp{display:none;position:absolute;top:100%;left:8px;z-index:60;width:500px;max-width:94vw;
background:rgba(28,34,44,.98);border:1px solid #3a4656;border-radius:10px;padding:12px 14px;
box-shadow:0 8px 28px rgba(0,0,0,.55);font-size:12px;color:#cdd6e0;text-align:left}
#reHelp.on{display:block}
.reHead{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}
.reHead b{font-size:13px;color:#ffd54a}
.reClose{padding:1px 8px;font-size:12px}
#reHelp table{border-collapse:collapse;width:100%;margin-bottom:8px}
#reHelp td{padding:2px 6px;border-bottom:1px solid #2c3542;vertical-align:top}
#reHelp td:first-child{font-family:Consolas,monospace;color:#ffd54a;white-space:nowrap}
.reEx code{display:block;margin:3px 0;padding:3px 8px;background:#151a22;border:1px solid #2c3542;
border-radius:6px;cursor:pointer;font-family:Consolas,monospace;color:#8fd3ff;white-space:nowrap;
overflow:hidden;text-overflow:ellipsis}
.reEx code:hover{border-color:#7cc7ff}
.reSub{color:#9ab;margin:6px 0 2px}
.reNote{color:#8892a0;margin-top:8px;border-top:1px solid #2c3542;padding-top:6px;line-height:1.5}
.aires{background:rgba(27,42,27,.85);border-left:3px solid #6c6;color:#9e9;
padding:4px 10px;margin:2px 0 8px;font-size:12px;white-space:pre-wrap}
button{background:rgba(45,52,62,.9);color:#d8dde5;border:1px solid #46536a;padding:3px 12px;cursor:pointer;font-size:12px;border-radius:4px}
button:hover{background:#3d4655}
button:disabled{opacity:.45;cursor:not-allowed}
input[type=text],select{background:rgba(35,42,52,.92);color:#d8dde5;border:1px solid #46536a;padding:3px 8px;font-size:12px;border-radius:4px}
label{font-size:12px;cursor:pointer}
#connmsg{font-size:12px}
.badge{font-size:12px;padding:2px 9px;border-radius:10px;cursor:pointer;user-select:none;
border:1px solid transparent;white-space:nowrap}
.badge.good{color:#6ec97a;background:rgba(60,120,70,.22);border-color:rgba(110,201,122,.45)}
.badge.warn{color:#ffb038;background:rgba(150,100,20,.25);border-color:rgba(255,176,56,.5)}
.badge.err{color:#ff6b6b;background:rgba(150,50,50,.25);border-color:rgba(255,107,107,.5)}
.badge.dead{color:#8a93a3;background:rgba(80,88,100,.25);border-color:rgba(140,150,165,.4)}
.ok{color:#6ec97a}.bad{color:#ff6b6b}
#diag{display:none;position:fixed;inset:0;z-index:10;background:rgba(0,0,0,.55)}
#diagbox{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
width:min(680px,92vw);max-height:80vh;overflow:auto;background:#161b22;border:1px solid #46536a;
border-radius:8px;padding:16px 20px;font-size:13px;box-shadow:0 12px 40px rgba(0,0,0,.6)}
#diagbox h3{margin:0 0 10px;font-size:14px;color:#d8dde5}
.chk{display:flex;gap:10px;padding:7px 0;border-bottom:1px dashed #2a3340}
.chk .ico{flex:0 0 18px;font-weight:bold}
.chk .nm{flex:0 0 130px;color:#aab4c2}
.chk .dt{flex:1;color:#c3ccd8;word-break:break-all}
.chk.ok .ico{color:#6ec97a}.chk.no .ico{color:#ff6b6b}
#diagbox pre{background:#0d1117;border:1px solid #2a3340;border-radius:4px;padding:8px;overflow:auto;font-size:12px;color:#9fb0c3}
#logmodal{display:none;position:fixed;inset:0;z-index:10;background:rgba(0,0,0,.55)}
#logbox{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
width:min(560px,92vw);max-height:80vh;overflow:auto;background:#161b22;border:1px solid #46536a;
border-radius:8px;padding:16px 20px;font-size:13px;box-shadow:0 12px 40px rgba(0,0,0,.6)}
#logbox h3{margin:0 0 10px;font-size:14px;color:#d8dde5}
.logitem{display:flex;justify-content:space-between;align-items:center;gap:10px;padding:8px 4px;
border-bottom:1px dashed #2a3340;cursor:pointer}
.logitem:hover{background:rgba(70,83,106,.3)}
.logitem .nm{color:#c3ccd8;word-break:break-all}
.logitem .mt{color:#8a93a3;font-size:12px;white-space:nowrap}
/* ---- 串口发送面板 ---- */
#sendFab{position:fixed;right:18px;bottom:18px;z-index:6;background:#2d6cdf;color:#fff;border:none;
border-radius:22px;padding:10px 18px;font-size:13px;cursor:pointer;box-shadow:0 4px 14px rgba(0,0,0,.5)}
#sendFab:hover{background:#3b7bef}
#sendPanel{display:none;position:fixed;right:14px;bottom:64px;z-index:7;width:min(540px,94vw);max-height:80vh;
overflow:auto;background:#161b22;border:1px solid #46536a;border-radius:8px;padding:14px 16px;font-size:13px;
box-shadow:0 12px 40px rgba(0,0,0,.6)}
#sendPanel h3{margin:0 0 8px;font-size:14px;color:#d8dde5}
#sendPanel .sec{border-top:1px dashed #2a3340;padding:8px 0}
#sendPanel input[type=text]{background:#0d1117;color:#c3ccd8;border:1px solid #333f52;border-radius:4px;
padding:4px 6px;font-family:Consolas,monospace}
#sendPanel select{background:#0d1117;color:#c3ccd8;border:1px solid #333f52;border-radius:4px;padding:3px}
.cmdbtn{display:inline-block;margin:3px 4px 3px 0;background:#233047;color:#c3ccd8;border:1px solid #3a4b66;
border-radius:4px;padding:3px 10px;cursor:pointer;font-size:12px}
.cmdbtn:hover{background:#2d3f5e}
.cmdbtn .pv{display:block;font-size:10px;color:#7c8ba1;font-family:Consolas,monospace}
#sendst{font-size:12px;color:#8a93a3;word-break:break-all}
#quickmodal{display:none;position:fixed;inset:0;z-index:11;background:rgba(0,0,0,.55)}
#quickbox{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
width:min(740px,94vw);max-height:84vh;overflow:auto;background:#161b22;border:1px solid #46536a;
border-radius:8px;padding:16px 20px;font-size:13px;box-shadow:0 12px 40px rgba(0,0,0,.6)}
#quickbox h3{margin:0 0 8px;font-size:14px;color:#d8dde5}
.qtab{display:inline-block;padding:4px 12px;cursor:pointer;border:1px solid #3a4b66;border-radius:4px 4px 0 0;
background:#1a2230;color:#aab4c2;margin-right:4px}
.qtab.on{background:#2d6cdf;color:#fff}
.frow{display:flex;gap:8px;align-items:center;margin:4px 0}
.frow .fn{flex:0 0 92px;color:#aab4c2}
.frow input,.frow select{flex:1;background:#0d1117;color:#c3ccd8;border:1px solid #333f52;border-radius:4px;
padding:3px 6px;font-family:Consolas,monospace}
.qdel{color:#ff6b6b;cursor:pointer;margin-left:6px}
.qop{color:#4ea1ff;cursor:pointer;margin-left:8px}
.treeroot{color:#8fb7ff;margin:6px 0 2px}
.crumbline{font-size:11px;color:#7c8ba1;margin-top:4px}
.qcrumb{color:#4ea1ff;cursor:pointer}
#qnav select{background:#0d1117;color:#c3ccd8;border:1px solid #333f52;border-radius:4px;
 padding:3px 4px;margin:2px 4px 2px 0;max-width:150px}
.pblock{border:1px solid #2a3648;border-radius:6px;padding:8px;margin:8px 0;background:#0d1117}
.frow.editing{background:#1b2a44;border-radius:4px;outline:1px solid #2d6cdf}
/* 协议字段编辑表格: 固定列宽 + 整行可横向滚动, 避免值列被挤成竖排 */
.feditwrap{overflow-x:auto;overflow-y:hidden;padding-bottom:3px;margin-top:6px}
.fedit{display:flex;gap:6px;align-items:center;margin:4px 0;min-width:max-content}
/* border-box + min-width:0 + 统一高度: 让 cell 的 flex-basis 就是它的实际占宽.
   input/select 默认 min-width:auto, 会被自身默认宽(约160px)顶开 flex-basis,
   导致列宽失控、逐列向右错位 —— 必须显式 min-width:0 把 flex-basis 变成硬约束.
   border-box 则保证 padding/border 不会额外撑宽. */
.fedit input,.fedit select,.fedit .fauto{box-sizing:border-box;min-width:0;height:26px;font-size:12px;
font-family:Consolas,monospace}
.fedit input,.fedit select{background:#0d1117;color:#c3ccd8;border:1px solid #333f52;border-radius:4px;
padding:0 6px}
.fedit .fb{flex:0 0 26px;min-width:0;color:#8a93a3;font-size:12px;text-align:center}
.fedit .fauto{color:#6e7787;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;line-height:24px;
border:1px dashed #2b3240;border-radius:3px;padding:0 6px}
.fedit .fcell{flex:0 0 auto}
.fedit .frange{flex:0 0 380px;min-width:0;display:flex;gap:6px;align-items:center}
.fhead{margin:2px 0 3px;padding-bottom:2px;border-bottom:1px solid #1f2937}
.fhead span{color:#7c8ba1;font-size:12px;line-height:1.6;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
#qmBody button[disabled]{opacity:.45;cursor:not-allowed}
/* ---- 页面内自绘弹窗(替代原生 alert/confirm/prompt) ---- */
#uidlg{display:none;position:fixed;inset:0;z-index:30;background:rgba(0,0,0,.55)}
#uidlg.on{display:block}
#uidlgbox{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
width:min(540px,92vw);max-height:80vh;overflow:auto;background:#161b22;border:1px solid #46536a;
border-radius:8px;padding:16px 20px;font-size:13px;box-shadow:0 12px 40px rgba(0,0,0,.6)}
#uidlgmsg{white-space:pre-wrap;word-break:break-word;color:#c3ccd8;line-height:1.55}
#uidlgin{display:none;width:100%;box-sizing:border-box;margin-top:10px;min-height:72px;
background:#0d1117;color:#c3ccd8;border:1px solid #333f52;border-radius:4px;padding:6px 8px;
font-family:Consolas,monospace;font-size:13px;resize:vertical}
#uidlgbtns{display:flex;gap:8px;justify-content:flex-end;margin-top:14px}
#uidlgbtns button.primary{background:#2d6cdf;border-color:#2d6cdf;color:#fff}
#uidlgbtns button.primary:hover{background:#3b7bef}
</style></head><body>
<div id="bar">
 <span>串口:</span>
 <select id="port" style="min-width:150px"></select>
 <button onclick="loadPorts()" title="重新扫描串口">刷新</button>
 <span>波特率:</span>
 <select id="baudlist" onchange="document.getElementById('baud').value=this.value" style="min-width:110px">
  <option value="">选择...</option>
 </select>
 <input type="text" id="baud" value="921600" size="8" title="可直接手填任意波特率">
 <button id="btnDetect" onclick="detectBaud()" title="试错法自动检测(设备需正在打日志)">自动检测波特率</button>
 <button id="btnConn" onclick="toggleConn()">连接</button>
 <span id="connmsg" class="bad">未连接</span>
 <button onclick="showDiag()" title="查看为什么未连接 / 当前错误详情">查看详情</button>
 <span id="diagbadge" class="badge" onclick="showDiag()" title="点开查看详情">检测中…</span>
</div>
<div id="bar2" style="position:fixed;top:47px;left:0;right:0;background:#151515;border-bottom:1px solid #333;
padding:6px 12px;display:flex;gap:14px;align-items:center;font-size:13px;z-index:2;flex-wrap:wrap">
 <span id="stats"></span>
 <button id="btnScroll" onclick="toggleScroll()">自动滚动:开</button>
 <button onclick="clearLog()">清屏</button>
 <button onclick="dumpLog()" title="把内存中的日志保存到文件">保存日志</button>
 <button onclick="showLogs()" title="查看已保存的日志文件, 选中即在下方显示">打开日志</button>
 <button onclick="submitSel()" title="先点选若干日志行再点此">AI分析选中</button>
 <button onclick="clearSel()" title="取消全部选中">取消选中</button>
 <span id="selcount" style="font-size:12px;color:#7CFC00"></span>
 <span id="fileview" style="display:none;color:#ffd479">
  正在查看文件: <b id="fvname"></b>
  <button onclick="closeFileView()" title="关闭文件视图, 回到实时打印">取消</button>
 </span>
 <label><input type="checkbox" id="onlyWarn" onchange="rebuild()">仅WARN/ERROR</label>
 <label title="每行显示方式">显示
  <select id="viewMode" onchange="rebuild()">
   <option value="ascii">ASCII</option>
   <option value="hex">HEX</option>
   <option value="both">ASCII+HEX</option>
  </select>
 </label>
 <input type="text" id="filter" placeholder="关键词/正则 回车搜索" size="14"
  onkeydown="if(event.key==='Enter'){event.preventDefault();applyFilter();}">
 <button id="btnReHelp" title="正则表达式: 符号说明与示例" onclick="toggleReHelp()">⋮</button>
 <label title="在每行左侧显示行号(文件本身不含行号)"><input type="checkbox" id="showLineNo" onchange="rebuild()" checked>行号</label>
 <label title="只匹配完整单词, 两侧不能是字母/数字/下划线"><input type="checkbox" id="matchWhole" onchange="rebuild()">全词匹配</label>
 <label title="区分大小写(不勾选则不区分)"><input type="checkbox" id="matchCase" onchange="rebuild()">区分大小写</label>
 <span id="filteropts">
  <button id="btnHl" onclick="setFilter('highlight')" title="全部行照显示, 命中的词黄底高亮">高亮关键词</button>
  <button id="btnOnly" onclick="setFilter('only')" title="只保留命中该词的行">只显示关键词</button>
  <button onclick="clearFilter()" title="清空关键词, 恢复正常显示">取消</button>
 </span>
 <span id="filtertag" onclick="clearFilter()" title="点此取消过滤"></span>
 <span id="hitcount" style="font-size:12px;color:#7cc7ff"></span>
 <span id="noscroll" style="color:#fa0;display:none">自动滚动已关(仍在接收)</span>
 <div id="reHelp">
  <div class="reHead">
   <label><input type="checkbox" id="reModeChk" onchange="setReMode(this.checked)"> <b>正则模式</b>（关键词按正则表达式运行）</label>
   <button class="reClose" onclick="toggleReHelp(false)">✕</button>
  </div>
  <table>
   <tr><td>.</td><td>任意 1 个字符</td><td>.* / .+</td><td>任意串(可空) / 至少 1 字符</td></tr>
   <tr><td>\\d</td><td>数字 0-9</td><td>\\w</td><td>字母/数字/下划线</td></tr>
   <tr><td>\\s</td><td>空白(空格/Tab)</td><td>\\b</td><td>单词边界</td></tr>
   <tr><td>[a-z]</td><td>字符范围集合</td><td>[^x]</td><td>除 x 以外</td></tr>
   <tr><td>^</td><td>行首</td><td>$</td><td>行尾</td></tr>
   <tr><td>x|y</td><td>x 或 y</td><td>( )</td><td>分组</td></tr>
   <tr><td>x?</td><td>0 或 1 次</td><td>x+ / x{2,4}</td><td>≥1 次 / 2~4 次</td></tr>
   <tr><td>(?i)</td><td>写在开头=忽略大小写</td><td>\\.</td><td>转义, 匹配点号本身</td></tr>
  </table>
  <div class="reSub">示例（点击填入搜索框）：</div>
  <div class="reEx">
   <code data-re="\\[(ERROR|WARN)\\]" title="匹配级别段(固定格式 [级别][文件:行号])">\\[(ERROR|WARN)\\]  ← 只看 ERROR/WARN 级别行</code>
   <code data-re="\\[[\\w.]+\\.c:\\d+\\]" title="匹配文件名:行号段">\\[[\\w.]+\\.c:\\d+\\]  ← 按 文件.c:行号 定位来源</code>
   <code data-re="temp[=:] ?\\d+" title="temp=85 或 temp:85">temp[=:] ?\\d+  ← 匹配参数与数值</code>
   <code data-re="0x[0-9A-Fa-f]{4}" title="4 位十六进制">0x[0-9A-Fa-f]{4}  ← 匹配 4 位十六进制</code>
   <code data-re="\\bCRC\\b.*fail" title="CRC 词边界 + 任意串 + fail">\\bCRC\\b.*fail  ← 词边界+后缀条件</code>
   <code data-re="(?i)fan \\d+ (error|stall)" title="内嵌忽略大小写">(?i)fan \\d+ (error|stall)  ← 忽略大小写匹配</code>
  </div>
  <div class="reNote">正则模式下「全词匹配」不生效（请自行用 \\b）；大小写仍由「区分大小写」控制；
   语法非法时自动按字面量匹配不会报错。开关状态本机记忆。</div>
 </div>
</div>
<div id="aires"></div>
<div id="log"></div>
<div id="diag" onclick="if(event.target===this)hideDiag()">
 <div id="diagbox">
  <h3>连接详情 / 诊断 <span id="diagsum"></span></h3>
  <div id="diagchecks"></div>
  <h3 style="margin-top:14px">原始状态</h3>
  <pre id="diagraw"></pre>
  <div style="text-align:right;margin-top:12px">
   <button onclick="showDiag()">重新检测</button>
   <button onclick="hideDiag()">关闭</button>
  </div>
 </div>
</div>
<div id="logmodal" onclick="if(event.target===this)hideLogs()">
 <div id="logbox">
  <h3>已保存的日志文件 <span id="logsum" style="font-size:12px;color:#8a93a3"></span></h3>
  <div id="loglist"><div style="color:#8a93a3">加载中...</div></div>
  <div style="text-align:right;margin-top:12px">
   <button onclick="refreshLogs()">刷新</button>
   <button onclick="hideLogs()">关闭</button>
  </div>
 </div>
</div>

<button id="sendFab" onclick="toggleSend()">发送</button>
<div id="sendPanel">
 <h3>串口发送
  <span style="float:right"><button onclick="openQm()">管理快捷指令</button>
  <button onclick="toggleSend()">收起</button></span>
 </h3>
 <div class="sec">
  <b>手动发送</b><br>
  <label><input type="radio" name="sndmode" value="hex" checked onchange="sndModeChg()">HEX</label>
  <label><input type="radio" name="sndmode" value="ascii" onchange="sndModeChg()">ASCII</label>
  <label title="发送内容末尾追加 0D 0A"><input type="checkbox" id="sndcrlf" checked>回车(\r\n)</label><br>
  <input type="text" id="snddata" size="44" placeholder="hex 如 5A A5 00 07 00 00 00 01 08 02 32 BA"
   onkeydown="if(event.key==='Enter')sendManual()" style="margin-top:4px">
  <button onclick="sendManual()">发送</button>
 </div>
 <div class="sec">
  <b>快捷指令</b>
  <div id="qnav" style="margin-top:4px"></div>
  <div id="qcrumb" class="crumbline"></div>
  <div id="cmdlist" style="margin-top:6px"></div>
 </div>
 <div class="sec"><span id="sendst"></span></div>
</div>

<div id="quickmodal" onclick="if(event.target===this)closeQm()">
 <div id="quickbox">
  <h3>管理快捷指令
   <span style="float:right"><button onclick="undoQuick()" title="回退到上一次保存前的配置">回退上一步</button>
   <button onclick="closeQm()">关闭</button></span>
  </h3>
  <span class="qtab on" id="tabBtnCmd" onclick="qmTab('cmd')">指令</span>
  <span class="qtab" id="tabBtnProj" onclick="qmTab('proj')">项目/分组</span>
  <span class="qtab" id="tabBtnProto" onclick="qmTab('proto')">协议</span>
  <div id="qmBody" style="margin-top:8px"></div>
 </div>
</div>
<div id="uidlg">
 <div id="uidlgbox">
  <div id="uidlgmsg"></div>
  <textarea id="uidlgin" spellcheck="false"></textarea>
  <div id="uidlgbtns"></div>
 </div>
</div>
<script>
let paused=false,last=0,lastAi=0,sel=new Set(),presetPort='',busy=false;
let allLines=[],filtMode='',filtKw='';
let liveLines=[],fileLines=[],fileView=null;
let anchor=null;
function netErr(e){
 return /Failed to fetch|NetworkError|Load failed/i.test(String(e))
  ?'连不上后端进程 —— 很可能是运行 python 的黑色命令行窗口被关掉/按了 Ctrl+C。请重新双击 嵌入式全能选手.bat 启动后刷新本页'
  :('错误: '+e);
}
/* ---- 页面内自绘弹窗 ----
   Trae 预览(webview)宿主会接管原生 alert/confirm/prompt 并触发自身
   React error #185(渲染死循环), 浏览器则一切正常。故统一改用页面内自绘
   弹窗, 语义与原生的对齐:
     uiAlert(msg)            -> Promise<undefined>
     uiConfirm(msg)          -> Promise<boolean>
     uiPrompt(msg, def)      -> Promise<string|null>   (取消=null)
   多个弹窗按调用顺序排队, 不会互相覆盖。 */
let _dlgQ=[],_dlgOn=false,_dlgCur=null;
function _dlgShow(opt){
 return new Promise(res=>{_dlgQ.push({opt:opt,res:res});_dlgNext();});
}
function _dlgNext(){
 if(_dlgOn||!_dlgQ.length)return;
 const it=_dlgQ.shift(),opt=it.opt;
 _dlgOn=true;
 const dlg=document.getElementById('uidlg');
 const msg=document.getElementById('uidlgmsg');
 const inp=document.getElementById('uidlgin');
 const btns=document.getElementById('uidlgbtns');
 msg.textContent=(opt.msg==null?'':String(opt.msg));
 inp.style.display=opt.kind==='prompt'?'block':'none';
 const dv=(opt.value==null?'':String(opt.value));
 inp.value=dv;
 inp.rows=Math.min(14,Math.max(3,dv.split('\\n').length+1));
 btns.innerHTML='';
 const done=v=>{
  dlg.classList.remove('on');_dlgOn=false;_dlgCur=null;
  it.res(v);
  setTimeout(_dlgNext,0);
 };
 _dlgCur={kind:opt.kind,done:done,inp:inp};
 const mk=(label,val,primary)=>{
  const b=document.createElement('button');
  b.textContent=label;if(primary)b.className='primary';
  b.onclick=()=>done(val);return b;};
 if(opt.kind==='alert'){
  btns.appendChild(mk(opt.okText||'确定',undefined,true));
 }else if(opt.kind==='confirm'){
  btns.appendChild(mk(opt.cancelText||'取消',false,false));
  btns.appendChild(mk(opt.okText||'确定',true,true));
 }else{
  btns.appendChild(mk(opt.cancelText||'取消',null,false));
  btns.appendChild(mk(opt.okText||'确定',inp.value,true));
 }
 dlg.classList.add('on');
 const focusEl=opt.kind==='prompt'?inp:btns.querySelector('.primary');
 if(focusEl){focusEl.focus();if(focusEl.select&&opt.kind==='prompt')focusEl.select();}
}
function uiAlert(msg){return _dlgShow({kind:'alert',msg:msg});}
function uiConfirm(msg){return _dlgShow({kind:'confirm',msg:msg});}
function uiPrompt(msg,def){return _dlgShow({kind:'prompt',msg:msg,value:def});}
document.addEventListener('keydown',e=>{
 if(!_dlgOn||!_dlgCur)return;
 if(e.key==='Escape'){e.preventDefault();e.stopPropagation();
  _dlgCur.done(_dlgCur.kind==='prompt'?null:false);return;}
 if(e.key!=='Enter')return;
 // 原生的 prompt 是单行输入框, 回车即确定; 这里保持一致:
 // prompt 下 Shift+Enter 换行, 直接回车确定; alert/confirm 回车即确定
 if(_dlgCur.kind==='prompt'&&e.shiftKey)return;
 e.preventDefault();e.stopPropagation();
 _dlgCur.done(_dlgCur.kind==='prompt'?_dlgCur.inp.value:true);
},true);
function toggleScroll(){paused=!paused;
 document.getElementById('noscroll').style.display=paused?'inline':'none';
 document.getElementById('btnScroll').textContent=paused?'自动滚动:关':'自动滚动:开';}
async function dumpLog(){
 const p=await uiPrompt('保存日志到:\\n留空 = 默认 output/logs/serial_时间戳_完成采集.log\\n或输入自定义完整路径','');
 if(p===null)return;
 const doMail=await uiConfirm('是否同时发送到飞书邮箱?\\n确定=发送(收件人为你自己) 取消=只保存');
 let am='',dm='',fc='',pj='';
 if(doMail){
  am=await uiPrompt('分析方式(邮件正文用):\\n1=固定格式分析(fixed)  2=自由格式分析(free)\\n3=AI按日志当前格式自动判定(auto, 推荐)\\n分析方式:', '3');
  if(am===null)am='';
  am={'1':'fixed','2':'free','3':'auto'}[am.trim()]||'';
  fc=await uiPrompt('是否有特殊要求?(可选)\\n填正则则严格按此要求分析(如 HandShake), 邮件正文只分析匹配行, HTML 报告仍为全量\\n此时不再需要选强度; 留空=无特殊要求','');
  if(fc===null)fc='';
  fc=fc.trim();
  if(!fc){
   dm=await uiPrompt('分析强度:\\n1=低(只看异常: 结论+热点+ERROR/WARN明细)  2=中(中等, 推荐)  3=高(全维度聚合)\\n(三档都必然分析 ERROR 与 WARN)\\n分析强度:', '2');
   if(dm===null)dm='';
   dm={'1':'low','2':'medium','3':'high'}[dm.trim()]||'medium';
  }else{dm='';}
  pj=await uiPrompt('关联哪个工程?(结论据此定位到源码文件/函数)\\n填 config [projects] 的编号(如 1/2), 留空=用 config 的 default;\\n若 config 无 default 且留空, 本次结论不关联工程代码','');
  if(pj===null)pj='';
  pj=pj.trim();
 }
 const r=await fetch('/dump',{method:'POST',
  headers:{'Content-Type':'application/json'},
  body:JSON.stringify({path:p.trim(),mail:doMail,analysis_mode:am,depth:dm,focus:fc.trim(),project:pj})});
 const j=await r.json();
 let msg=j.ok?('已保存 '+j.lines+' 行到:\\n'+j.path+'\\nWARN: '+j.warn+'  ERROR: '+j.error):('保存失败: '+(j.err||''));
 if(j.ok&&j.html)msg+=('\\n报告: '+j.html);
 if(j.ok&&doMail)msg+=('\\n邮件: '+(j.mail_ok===true?'已发送':('失败 '+(j.mail_err||''))));
 await uiAlert(msg);}
function clearLog(){sel.clear();anchor=null;
 if(fileView){fileLines=[];allLines=fileLines;}else{liveLines=[];allLines=liveLines;}
 document.getElementById('log').innerHTML='';updateHits();updateSelCount();}
function escRe(s){return s.replace(/[.*+?^${}()|[\\]\\\\]/g,'\\\\$&');}
let reMode=false;try{reMode=localStorage.getItem('slReMode')==='1';}catch(e){}
function makeRe(){
 if(!filtKw)return null;
 const icase=!document.getElementById('matchCase').checked;
 const flags=icase?'gi':'g';
 if(reMode){
  try{return new RegExp(filtKw,flags);}catch(e){}   // 语法非法 → 回退字面量
 }
 let pat=escRe(filtKw);
 if(document.getElementById('matchWhole').checked)pat='\\\\b'+pat+'\\\\b';  // 正则模式忽略全词(自行用\\b)
 try{return new RegExp(pat,flags);}catch(e){return null;}
}
// ---------- 正则帮助面板 ----------
function toggleReHelp(force){
 const p=document.getElementById('reHelp');
 const on=(typeof force==='boolean')?force:!p.classList.contains('on');
 p.classList.toggle('on',on);
 if(on)document.getElementById('reModeChk').checked=reMode;
}
function setReMode(on){
 reMode=!!on;
 try{localStorage.setItem('slReMode',reMode?'1':'0');}catch(e){}
 if(filtKw)refreshTag();
 rebuild();
}
function useRe(el){
 document.getElementById('filter').value=el.dataset.re;
 toggleReHelp(false);
 applyFilter();
}
function refreshTag(){
 const tag=document.getElementById('filtertag');
 if(filtKw&&filtMode)
  tag.textContent=(filtMode==='highlight'?'高亮: ':'只显示: ')+filtKw+filterFlags()+'  ✕';
}
document.addEventListener('click',e=>{
 const p=document.getElementById('reHelp');
 if(!p||!p.classList.contains('on'))return;
 if(p.contains(e.target)||e.target.closest('#btnReHelp'))return;
 toggleReHelp(false);
});
function appendAscii(row,j,match){
 if(filtMode==='highlight'&&match){
  const hr=makeRe();let lastIdx=0,m;
  while((m=hr.exec(j.t))!==null){
   if(m[0]===''){hr.lastIndex++;continue;}
   if(m.index>lastIdx)row.appendChild(document.createTextNode(j.t.slice(lastIdx,m.index)));
   const mk=document.createElement('mark');mk.textContent=m[0];row.appendChild(mk);
   lastIdx=m.index+m[0].length;
  }
  if(lastIdx<j.t.length)row.appendChild(document.createTextNode(j.t.slice(lastIdx)));
 }else{
  row.appendChild(document.createTextNode(j.t));
 }
}
function makeRow(j){
 const re=makeRe();
 const match=re?re.test(j.t):false;
 if(filtMode==='only'&&filtKw&&!match)return null;
 if(document.getElementById('onlyWarn').checked&&!(j.l==='WARN'||j.l==='ERROR'))return null;
 const row=document.createElement('div');
 const showNo=document.getElementById('showLineNo');
 if(showNo&&showNo.checked&&j.s!==undefined){
  const no=document.createElement('span');no.className='ln';no.textContent=String(j.s);
  row.appendChild(no);
 }
 if(j.ts){
  const ts=document.createElement('span');ts.className='ts';
  ts.textContent=new Date(j.ts*1000).toLocaleTimeString('zh-CN',{hour12:false})+'.'+
   String(Math.floor(j.ts*1000)%1000).padStart(3,'0');
  row.appendChild(ts);
 }
 const lv=document.createElement('span');
 lv.className='lv '+j.l;lv.textContent=j.l;
 row.appendChild(lv);
 const mode=(document.getElementById('viewMode')||{value:'ascii'}).value;
 if(mode==='hex'){
  const hx=document.createElement('span');hx.className='hex';
  hx.textContent=j.h||'(空)';row.appendChild(hx);
 }else{
  appendAscii(row,j,match);
  if(mode==='both'){
   const hx=document.createElement('span');hx.className='hex';
   hx.textContent='   ['+(j.h||'')+']';row.appendChild(hx);
  }
 }
 if(sel.has(j.s))row.classList.add('sel');
 row.onclick=(e)=>{
  if(e.shiftKey&&anchor!==null){rangeSelect(anchor,j.s);}
  else if(e.ctrlKey||e.metaKey){sel.add(j.s);row.classList.add('sel');anchor=j.s;updateSelCount();}
  else{if(sel.has(j.s))sel.delete(j.s);else sel.add(j.s);
   row.classList.toggle('sel',sel.has(j.s));anchor=j.s;updateSelCount();}
 };
 return row;
}
function rangeSelect(a,b){
 const ia=allLines.findIndex(x=>x.s===a),ib=allLines.findIndex(x=>x.s===b);
 if(ia<0||ib<0){sel.add(b);rebuild();anchor=b;return;}
 const lo=Math.min(ia,ib),hi=Math.max(ia,ib);
 for(let i=lo;i<=hi;i++)sel.add(allLines[i].s);
 rebuild();
 updateSelCount();
}
function appendOne(j){
 const row=makeRow(j);
 if(!row)return;
 const log=document.getElementById('log');log.appendChild(row);
 if(j.i){const s=document.createElement('div');s.className='insight';
  s.textContent='AI: '+j.i;log.appendChild(s);}
 while(log.childNodes.length>20000)log.removeChild(log.firstChild);
}
function updateSelCount(){
 const el=document.getElementById('selcount');
 if(!el)return;
 el.textContent=sel.size>0?('已选 '+sel.size+' 行'):'';
}
function clearSel(){
 sel.clear();anchor=null;
 document.querySelectorAll('.sel').forEach(e=>e.classList.remove('sel'));
 updateSelCount();
}
function updateHits(){
 const el=document.getElementById('hitcount');
 if(!filtKw){el.textContent='';return;}
 let n=0;
 for(const j of allLines){
  const re=makeRe();
  if(re&&re.test(j.t))n++;
 }
 el.textContent='命中 '+n+' / '+allLines.length+' 行';
}
function render(j){
 liveLines.push(j);
 if(liveLines.length>20000)liveLines.shift();
 if(fileView)return;             // 文件视图下仍在后台缓冲实时行, 但不打断当前显示
 allLines=liveLines;
 appendOne(j);
 updateHits();
 if(!paused)window.scrollTo(0,document.body.scrollHeight);
}
function rebuild(){
 document.getElementById('log').innerHTML='';
 for(const j of allLines)appendOne(j);
 updateHits();
 layoutBars();
 if(!paused)window.scrollTo(0,document.body.scrollHeight);
}
function applyFilter(){
 const kw=document.getElementById('filter').value.trim();
 if(!kw){clearFilter();return;}
 filtKw=kw;
 document.getElementById('filteropts').classList.add('on');
 updateHits();
}
function filterFlags(){
 let s='';
 if(reMode)s+=' 正则';
 if(document.getElementById('matchWhole').checked&&!reMode)s+=' 全词';
 if(document.getElementById('matchCase').checked)s+=' 区分大小写';
 return s;
}
function setFilter(mode){
 const kw=document.getElementById('filter').value.trim();
 if(!kw){clearFilter();return;}
 filtMode=mode;filtKw=kw;
 refreshTag();
 document.getElementById('filtertag').classList.add('on');
 rebuild();
}
function clearFilter(){
 filtMode='';filtKw='';
 document.getElementById('filter').value='';
 document.getElementById('filteropts').classList.remove('on');
 document.getElementById('filtertag').classList.remove('on');
 rebuild();
}
async function poll(){
 for(;;){
  try{
   const r=await fetch('/stream?since='+last);
   const reader=r.body.getReader();const dec=new TextDecoder();let buf='';
   for(;;){
    const{done,value}=await reader.read();if(done)break;
    buf+=dec.decode(value);const parts=buf.split('\\n\\n');buf=parts.pop();
    for(const p of parts){
     if(!p.startsWith('data:'))continue;
     const j=JSON.parse(p.slice(5));
     if(j.st!==undefined)document.getElementById('stats').textContent=j.st;
     if(j.t===undefined)continue;
     last=j.s;
     render(j);
    }}
  }catch(e){await new Promise(r=>setTimeout(r,1000));}
 }
}
async function pollAi(){
 for(;;){
  try{
   const r=await fetch('/ai_results?after='+lastAi);
   const list=await r.json();
   for(const a of list){lastAi=a.id;
    const d=document.createElement('div');d.className='aires';
    d.textContent='【AI分析 '+new Date(a.ts*1000).toLocaleTimeString()+'】\\n'+a.text;
    document.getElementById('aires').appendChild(d);
    document.getElementById('aires').appendChild(document.createElement('br'));}
  }catch(e){}
  await new Promise(r=>setTimeout(r,3000));
 }
}
async function submitSel(){
 if(sel.size===0){await uiAlert('先点击选中若干日志行(选中行变蓝)');return;}
 const lines=[];
 for(const j of allLines)if(sel.has(j.s))lines.push(j.t);
 const n=lines.length;
 await fetch('/selection',{method:'POST',
 headers:{'Content-Type':'application/json'},
 body:JSON.stringify({lines:lines})});
 sel.clear();
 document.querySelectorAll('.sel').forEach(e=>e.classList.remove('sel'));
 updateSelCount();
 await uiAlert('已提交 '+n+' 行, 请在TRAE对话里让AI分析(selection_pending.json)');
}
async function loadBauds(){
 try{
  const r=await fetch('/bauds');const list=await r.json();
  const s=document.getElementById('baudlist');
  if(s.options.length>1)return;
  for(const b of list){const o=document.createElement('option');o.value=b;o.textContent=b;s.appendChild(o);}
 }catch(e){}
}
async function loadBg(){
 try{
  const r=await fetch('/bg');const j=await r.json();
  if(j.url)document.body.style.setProperty('--bg','url("'+j.url+'")');
 }catch(e){}
}
function fmtSize(n){return n<1024?(n+' B'):(n<1048576?(Math.round(n/1024)+' KB'):(n/1048576).toFixed(1)+' MB');}
function layoutBars(){
 const b1=document.getElementById('bar'),b2=document.getElementById('bar2');
 const h1=b1.offsetHeight;
 b2.style.top=h1+'px';
 document.body.style.paddingTop=(h1+b2.offsetHeight+8)+'px';
}
async function showLogs(){
 document.getElementById('logmodal').style.display='block';
 await refreshLogs();
}
function hideLogs(){document.getElementById('logmodal').style.display='none';}
async function refreshLogs(){
 const box=document.getElementById('loglist');
 box.innerHTML='<div style="color:#8a93a3">加载中...</div>';
 try{
  const r=await fetch('/logs');const list=await r.json();
  document.getElementById('logsum').textContent='('+list.length+' 个)';
  box.innerHTML='';
  if(!list.length){box.innerHTML='<div style="color:#8a93a3">output/logs 下暂无日志文件, 先点"保存日志"</div>';return;}
  for(const f of list){
   const d=document.createElement('div');d.className='logitem';
   const nm=document.createElement('span');nm.className='nm';nm.textContent=f.name;
   const mt=document.createElement('span');mt.className='mt';
   mt.textContent=fmtSize(f.size)+'  '+new Date(f.mtime*1000).toLocaleString();
   d.appendChild(nm);d.appendChild(mt);
   d.onclick=()=>openLogFile(f.name);
   box.appendChild(d);
  }
 }catch(e){box.innerHTML='<div class="bad">加载失败: '+netErr(e)+'</div>';}
}
async function openLogFile(name){
 hideLogs();
 try{
  const r=await fetch('/logfile?name='+encodeURIComponent(name));const j=await r.json();
  if(!j.ok){await uiAlert('打开失败: '+(j.err||''));return;}
  fileLines=(j.lines||[]).map((x,i)=>({s:i+1,ts:x.ts||0,t:x.t,h:x.h,l:x.l,i:x.i}));
  fileView=name;allLines=fileLines;sel.clear();anchor=null;
  document.getElementById('fvname').textContent=name+' ('+fileLines.length+' 行)';
  document.getElementById('fileview').style.display='inline';
  rebuild();
  updateSelCount();
 }catch(e){await uiAlert('打开失败。'+netErr(e));}
}
function closeFileView(){
 fileView=null;allLines=liveLines;sel.clear();anchor=null;
 document.getElementById('fileview').style.display='none';
 rebuild();
 updateSelCount();
}
async function showDiag(){
 const box=document.getElementById('diagbox');
 document.getElementById('diagchecks').innerHTML='<div class="chk"><span class="nm">检测中...</span></div>';
 document.getElementById('diagraw').textContent='';
 document.getElementById('diagsum').textContent='';
 document.getElementById('diag').style.display='block';
 try{
  const r=await fetch('/diag');const j=await r.json();
  const wrap=document.getElementById('diagchecks');wrap.innerHTML='';
  for(const c of j.checks){
   const d=document.createElement('div');d.className='chk '+(c.ok?'ok':'no');
   d.innerHTML='<span class="ico">'+(c.ok?'✓':'✗')+'</span>'+
    '<span class="nm">'+c.name+'</span><span class="dt"></span>';
   d.querySelector('.dt').textContent=c.detail;
   wrap.appendChild(d);
  }
  document.getElementById('diagsum').innerHTML=j.ok
   ?'<span class="ok">· 一切正常</span>':'<span class="bad">· 存在 '+j.checks.filter(c=>!c.ok).length+' 项异常</span>';
  document.getElementById('diagraw').textContent=JSON.stringify(
   {connected:j.connected,port:j.port,baud:j.baud,msg:j.msg,err:j.err,config:j.config},null,2);
 }catch(e){
  const dead=/Failed to fetch|NetworkError|Load failed/i.test(String(e));
  document.getElementById('diagchecks').innerHTML=
   '<div class="chk no"><span class="ico">✗</span><span class="nm">'+(dead?'服务已停止':'请求失败')+'</span>'+
   '<span class="dt">'+(dead
     ?'连不上后端进程 —— 很可能是那个运行 python 的黑色命令行窗口被关掉/按了 Ctrl+C。请重新双击 嵌入式全能选手.bat 启动后刷新本页'
     :('错误: '+e))+'</span></div>';
  document.getElementById('diagsum').innerHTML=dead
   ?'<span class="bad">· 后端未运行</span>':'';
  document.getElementById('diagraw').textContent='';
 }
}
function hideDiag(){document.getElementById('diag').style.display='none';}
async function refreshDiagBadge(){
 const b=document.getElementById('diagbadge');
 try{
  const r=await fetch('/diag_sum');const j=await r.json();
  if(j.bad===0){b.className='badge good';b.textContent='✓ 正常';b.title='诊断全部通过, 点开查看详情';}
  else{b.className='badge '+(j.bad>1?'err':'warn');
   b.textContent='⚠ '+j.bad+' 项异常';b.title='发现 '+j.bad+' 项异常, 点开查看详情';}
 }catch(e){
  b.className='badge dead';b.textContent='· 服务未运行';b.title='连不上后端进程';
 }
}
async function loadPorts(){
 const sel=document.getElementById('port');const keep=sel.value||presetPort;
 try{
  const r=await fetch('/ports');const list=await r.json();
  sel.innerHTML='';
  if(!list.length){const o=document.createElement('option');o.value='';o.textContent='(未发现串口)';sel.appendChild(o);}
  for(const p of list){const o=document.createElement('option');o.value=p.device;
   o.textContent=p.desc?(p.device+' - '+p.desc):p.device;sel.appendChild(o);}
  if(keep)for(const o of sel.options)if(o.value===keep){sel.value=keep;break;}
 }catch(e){}
}
function setConn(open,msg,ok){
 const el=document.getElementById('connmsg');
 el.textContent=msg;el.className=ok?'ok':'bad';
 document.getElementById('btnConn').textContent=open?'断开':'连接';
 document.getElementById('btnDetect').disabled=open;
 document.getElementById('btnConn').disabled=busy;
 layoutBars();
}
function syncPortUi(port,baud){
 /* 把下拉框/波特率框同步到"当前实际连接的口", 避免顶部状态已连接、下拉框却停在别的口 */
 if(!port)return;
 const selEl=document.getElementById('port');
 if(selEl.value!==port){
  let hit=false;
  for(const o of selEl.options)if(o.value===port){hit=true;break;}
  if(!hit){const o=document.createElement('option');o.value=port;o.textContent=port+' (已连接)';selEl.appendChild(o);}
  selEl.value=port;
 }
 const b=document.getElementById('baud');
 if(baud&&document.activeElement!==b)b.value=baud;
}
async function refreshConn(){
 if(busy)return;
 try{const r=await fetch('/conn');const j=await r.json();
  if(j.preset)presetPort=j.preset;
  if(j.open)syncPortUi(j.port,j.baud);
  setConn(j.open,(j.open?('已连接 '+j.port+' @ '+j.baud):(j.err?j.err:j.msg)),j.open||!j.err);}catch(e){}
}
async function toggleConn(){
 if(busy)return;
 const btn=document.getElementById('btnConn');
 const isOpen=btn.textContent==='断开';
 busy=true;btn.disabled=true;
 try{
  if(isOpen){
   const r=await fetch('/disconnect',{method:'POST'});const j=await r.json();
   setConn(false,j.msg||'已断开',true);
  }else{
   const port=document.getElementById('port').value;
   if(!port){await uiAlert('未发现/未选择串口, 请点"刷新"');return;}
   const baud=document.getElementById('baud').value.trim()||'921600';
   setConn(false,'连接中...',true);
   const r=await fetch('/connect',{method:'POST',
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify({port:port,baud:baud,auto_baud:false})});
   const j=await r.json();
   setConn(j.ok,j.msg||(j.err||''),j.ok);
   if(!j.ok)await uiAlert('连接失败: '+(j.msg||j.err||''));
  }
 }catch(e){setConn(false,'连接失败',false);await uiAlert('连接失败。'+netErr(e));}
 finally{busy=false;btn.disabled=false;refreshDiagBadge();}
}
let detectRunning=false;
async function detectBaud(){
 const btn=document.getElementById('btnDetect');
 if(detectRunning){          /* 停止态: 点击即请求中止 */
  btn.textContent='停止中...';btn.disabled=true;
  try{await fetch('/detect_stop',{method:'POST'});}catch(e){}
  return;                    /* 原检测请求的响应到达后由 finally 恢复按钮 */
 }
 const port=document.getElementById('port').value;
 if(!port){await uiAlert('未发现/未选择串口, 请点"刷新"');return;}
 detectRunning=true;btn.textContent='停止检测';btn.disabled=false;   /* 保持可点=可停 */
 try{
  const r=await fetch('/detect_baud',{method:'POST',
   headers:{'Content-Type':'application/json'},body:JSON.stringify({port:port})});
  const j=await r.json();
  if(j.ok){document.getElementById('baud').value=j.baud;setConn(false,j.msg,true);
   await uiAlert('检测成功: '+j.baud+' bps\\n已自动填入波特率输入框, 点"连接"即可');}
  else{await uiAlert((j.msg||j.err||''));}
 }catch(e){await uiAlert('检测失败。'+netErr(e));}
 detectRunning=false;btn.textContent='自动检测波特率';btn.disabled=false;
}
/* ================= 串口发送 + 快捷指令 ================= */
let QUICK=null,qmTabCur='cmd';
function escx(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;');}
function toggleSend(){
 const p=document.getElementById('sendPanel');
 p.style.display=(p.style.display==='block')?'none':'block';
 if(p.style.display==='block'&&!QUICK)loadQuick();
}
function sndMode(){const r=document.querySelector('input[name=sndmode]:checked');return r?r.value:'hex';}
function sndModeChg(){
 document.getElementById('snddata').placeholder=(sndMode()==='hex')
  ?'hex 如 5A A5 00 07 00 00 00 01 08 02 32 BA':'ascii 如 hello';
}
function txLog(text){
 const d=document.createElement('div');
 d.style.cssText='color:#7cc7ff;white-space:pre-wrap';
 d.textContent='[TX] '+text;
 const lg=document.getElementById('log');lg.appendChild(d);
 if(!paused)lg.scrollTop=lg.scrollHeight;
}
async function doSend(mode,data,crlf){
 const st=document.getElementById('sendst');
 try{
  const r=await fetch('/send',{method:'POST',headers:{'Content-Type':'application/json'},
   body:JSON.stringify({mode:mode,data:data,crlf:!!crlf})});
  const j=await r.json();
  if(j.ok){st.innerHTML='<span class="ok">已发送 '+j.n+' 字节</span>';
   txLog(mode==='hex'?j.hex:(data+(crlf?'\\r\\n':'')));}
  else{st.innerHTML='<span class="bad">发送失败: '+escx(j.msg||'')+'</span>';}
 }catch(e){st.innerHTML='<span class="bad">发送失败: '+netErr(e)+'</span>';}
}
async function sendManual(){
 const data=document.getElementById('snddata').value.trim();
 if(!data){await uiAlert('请输入发送内容');return;}
 doSend(sndMode(),data,document.getElementById('sndcrlf').checked);
}
/* ---- 快捷指令: 任意层级递归分组 ---- */
function loadQuick(){
 return fetch('/quick').then(r=>r.json()).catch(e=>({protocols:{},groups:{}}))
  .then(j=>{QUICK=j;normalizeQuick();
   if(!Object.keys(QUICK.groups).length)QUICK.groups={project:[],other:[]};
   if(!qPath.length||!QUICK.groups[qPath[0]])qPath=[Object.keys(QUICK.groups)[0]];
   renderNav();});
}
function migrateProto(p){
 if(!p||!p.fields)return p;
 const fw=f=>{const n=parseInt(f.len);return (n===-1||isNaN(n))?0:n;};
 let vi=-1;p.fields.forEach((f,i)=>{if(f.len===-1)vi=i;});
 p.fields.forEach((f,i)=>{
  if(f.role)return;
  if(f.auto==='len_plus'){
   const plus=parseInt(f.plus)||0;let frm='',to='',off=plus;
   if(vi>i&&p.fields[i+1]){
    const seg=p.fields.slice(i+1,vi+1);
    const s=seg.reduce((a,g)=>a+fw(g),0);
    if(s<=plus){frm=p.fields[i+1].name;to=p.fields[vi].name;off=plus-s;}}
   if(!frm&&vi>=0){frm=to=p.fields[vi].name;}
   f.role='len';f.from=frm;f.to=to;f.offset=off;delete f.auto;delete f.plus;
  }else if(f.auto==='checksum'){
   const off=((p.checksum||{}).from)||0;
   let acc=0,i0=0;
   for(let k=0;k<i;k++){const w=fw(p.fields[k]);
    if(acc<=off&&off<acc+Math.max(w,1)){i0=k;break;}acc+=w;}
   let i1=Math.max(i-1,0);if(i1<i0)i0=i1;
   f.role='sum';f.len=1;f.alg='sum_neg';f.from=(p.fields[i0]||{}).name;f.to=(p.fields[i1]||{}).name;delete f.auto;}});
 /* 存量 role=sum 无算法的补默认 */
 p.fields.forEach(f=>{if(f&&f.role==='sum'&&!f.alg)f.alg='sum_neg';});
 delete p.checksum;return p;
}
const SUM_ALGS=[['sum_neg','累加取反+1'],['sum','累加和'],['xor','逐字节异或']];
function algName(a){const h=SUM_ALGS.filter(x=>x[0]===(a||'sum_neg'))[0];return h?h[1]:'累加取反+1';}
/* 帧结构串: 按 fields 实际顺序生成, 字段增删自动同步, 不写死 */
function frameStr(proto){
 return (proto.fields||[]).map(f=>f.name+'('+(f.len===-1?'变长':((f.len||1)+'B'))+')').join('|');
}
/* 说明里的占位符: {frame}帧结构 {len}长度公式 {sum}校验公式 {fields}字段清单 {name}协议名 */
function expandDesc(proto,name,text){
 let s=String(text==null?'':text);
 const rp=(k,v)=>{s=s.split('{'+k+'}').join(v);};
 const brief=f=>f.name+'('+(f.len===-1?'变长':((f.len||1)+'B'))+')';
 rp('frame',frameStr(proto));
 rp('name',name||'');
 rp('fields',(proto.fields||[]).map(brief).join(' '));
 rp('len',(proto.fields||[]).filter(f=>f.role==='len')
  .map(f=>f.name+'='+f.from+'..'+f.to+(f.offset?('+'+f.offset):'')).join('; ')||'—');
 rp('sum',(proto.fields||[]).filter(f=>f.role==='sum')
  .map(f=>f.name+'='+f.from+'..'+f.to+'('+algName(f.alg)+')').join('; ')||'—');
 return s;
}
const DESC_PH=['{frame}','{len}','{sum}','{fields}','{name}'];
function descPhTip(p){
 return {'{frame}':'按当前字段顺序自动生成的帧结构, 如 SYNC(2B)|ACK(1B)|LEN(2B)|...',
  '{len}':'所有 LEN 角色字段的长度算法, 如 LEN=MODE..PARAM',
  '{sum}':'所有 SUM 角色字段的校验算法, 如 SUM=ACK..PARAM(累加取反+1)',
  '{fields}':'字段清单(一行), 如 SYNC(2B) ACK(1B) LEN(2B) ...',
  '{name}':'协议名'}[p]||'';
}
function insDesc(p){
 const el=document.getElementById('epDesc');if(!el)return;
 const a=(el.selectionStart==null?el.value.length:el.selectionStart);
 const b=(el.selectionEnd==null?el.value.length:el.selectionEnd);
 el.value=el.value.slice(0,a)+p+el.value.slice(b);
 el.focus();el.selectionStart=el.selectionEnd=a+p.length;
 pvDesc();
}
function pvDesc(){
 const el=document.getElementById('epDesc'),pv=document.getElementById('epDescPv');
 if(!el||!pv)return;
 const proto=QUICK.protocols[epEdit];
 if(!proto){pv.textContent='';return;}
 // 用编辑框里当前的字段名生成预览, 还没保存也能看到效果(不改动 proto 本身)
 const snap={fields:(proto.fields||[]).map((f,i)=>{
  const e=document.getElementById('fd_'+i+'_name');
  return Object.assign({},f,{name:(e&&e.value.trim())||f.name});})};
 const t=expandDesc(snap,epEdit,el.value);
 pv.textContent=(t?('预览: '+t):'预览: (说明为空)');
}
function normalizeQuick(){
 QUICK.protocols=QUICK.protocols||{};QUICK.groups=QUICK.groups||{};
 const walk=ns=>(ns||[]).forEach(n=>{
  if(!n.children&&n.subgroups)n.children=n.subgroups;
  delete n.subgroups;n.cmds=n.cmds||[];n.children=n.children||[];walk(n.children);});
 Object.keys(QUICK.groups).forEach(k=>walk(QUICK.groups[k]));
 Object.keys(QUICK.protocols).forEach(k=>migrateProto(QUICK.protocols[k]));
}
function nodeAtPath(sec,path){
 let list=QUICK.groups[sec]||[],n=null;
 for(const i of path){n=list[i];if(!n)return null;list=n.children||[];}
 return n;}
function pathNamesOf(sec,path){
 let list=QUICK.groups[sec]||[],ns=[];
 for(const i of path){const n=list[i];if(!n)break;ns.push(n.name);list=n.children||[];}
 return ns;}
function effProtoAt(sec,path){
 let list=QUICK.groups[sec]||[],p=null;
 for(const i of path){const n=list[i];if(!n)break;
  if('protocol' in n)p=n.protocol||null;list=n.children||[];}
 return p;}
function curNode(){return qPath.length>1?nodeAtPath(qPath[0],qPath.slice(1)):null;}
function effProto(){return effProtoAt(qPath[0],qPath.slice(1));}
function pathText(){const ns=pathNamesOf(qPath[0],qPath.slice(1));
 return qPath[0]+(ns.length?' / '+ns.join(' / '):'');}
function listAt(path){
 if(path.length===1)return QUICK.groups[path[0]]||[];
 const p=nodeAtPath(path[0],path.slice(1));
 return (p&&p.children)||[];}
function renderNav(){
 const nav=document.getElementById('qnav');nav.innerHTML='';
 const secs=Object.keys(QUICK.groups);
 if(!secs.length){nav.textContent='无分组';document.getElementById('cmdlist').textContent='';return;}
 if(!qPath.length||secs.indexOf(qPath[0])<0)qPath=[secs[0]];
 const s0=document.createElement('select');
 secs.forEach(k=>{const o=document.createElement('option');o.value=k;
  o.textContent=(k==='project')?'1.project':(k==='other')?'2.other':k;
  if(k===qPath[0])o.selected=true;s0.appendChild(o);});
 s0.onchange=()=>{qPath=[s0.value];resetCmdEdit();renderNav();};
 nav.appendChild(s0);
 for(let d=1;d<16;d++){
  const list=listAt(qPath.slice(0,d));
  const cur=(d<qPath.length)?qPath[d]:null;
  if(!list||(!list.length&&cur===null))break;
  const s=document.createElement('select');
  if(cur===null){const o=document.createElement('option');o.value='';o.textContent='▸ 选择下级';s.appendChild(o);}
  list.forEach((n,i)=>{const o=document.createElement('option');o.value=i;
   if(n.children&&n.children.length)o.textContent=n.name+' ▾';else o.textContent=n.name;
   if(i===cur)o.selected=true;s.appendChild(o);});
  s.onchange=()=>{
   qPath=(s.value==='')?qPath.slice(0,d):qPath.slice(0,d).concat([parseInt(s.value)]);
   resetCmdEdit();renderNav();};
  nav.appendChild(s);
  if(cur===null)break;
 }
 renderCrumb();renderCmds();
}
function resetCmdEdit(){
 qmEditIdx=-1;
 if(document.getElementById('quickmodal').style.display==='block')qmRender();
}
function renderCrumb(){
 const ns=pathNamesOf(qPath[0],qPath.slice(1));
 let h='<span class="qcrumb" onclick="qGo(0)">'+escx(qPath[0])+'</span>';
 ns.forEach((n,i)=>{h+=' / <span class="qcrumb" onclick="qGo('+(i+1)+')">'+escx(n)+'</span>';});
 h+='&nbsp;<span style="color:#5f6b7d">(共 '+ns.length+' 级, 末级下拉可继续下钻)</span>';
 document.getElementById('qcrumb').innerHTML=h;
}
function qGo(d){qPath=qPath.slice(0,d+1);resetCmdEdit();renderNav();}
function renderCmds(){
 const box=document.getElementById('cmdlist');box.innerHTML='';
 const n=curNode();
 if(!n){box.innerHTML='<span style="color:#8a93a3">根层: 用上面下拉进入分组; 点「管理快捷指令」→分组 可新建任意层级分组</span>';return;}
 const p=effProto();
 const head=document.createElement('div');head.className='crumbline';
 head.textContent='本分组指令 '+((n.cmds||[]).length)+' 条'+(p?(' · 协议: '+p):' · 手动无协议');
 box.appendChild(head);
 (n.cmds||[]).forEach(c=>{
  const b=document.createElement('span');b.className='cmdbtn';b.textContent=c.name;
  b.onclick=()=>quickSend(c);box.appendChild(b);
  if(p&&c.fields){
   fetch('/preview',{method:'POST',headers:{'Content-Type':'application/json'},
    body:JSON.stringify({proto:p,fields:c.fields})}).then(r=>r.json()).then(j=>{
    if(j.ok){const pv=document.createElement('span');pv.className='pv';pv.textContent=j.hex;
     b.appendChild(pv);b.title=j.hex;}});
  }else if(c.data){
   const pv=document.createElement('span');pv.className='pv';
   pv.textContent=(c.mode||'hex')+': '+c.data;b.appendChild(pv);
  }
  box.appendChild(document.createElement('div'));
 });
}
async function quickSend(c){
 const crlf=document.getElementById('sndcrlf').checked,p=effProto();
 if(p&&c.fields){
  try{
   const r=await fetch('/preview',{method:'POST',headers:{'Content-Type':'application/json'},
    body:JSON.stringify({proto:p,fields:c.fields})});
   const j=await r.json();
   if(!j.ok){document.getElementById('sendst').innerHTML=
    '<span class="bad">组帧失败: '+escx(j.msg||'')+'</span>';return;}
   doSend('hex',j.hex,crlf);
  }catch(e){document.getElementById('sendst').innerHTML='<span class="bad">'+netErr(e)+'</span>';}
 }else{doSend(c.mode||'hex',c.data||'',crlf);}
}
let qPath=[];
let qmEditMode=false,qmEditIdx=-1;
/* ---- 管理弹窗 ---- */
function openQm(){document.getElementById('quickmodal').style.display='block';qmRender();}
function closeQm(){document.getElementById('quickmodal').style.display='none';}
function qmTab(t){qmTabCur=t;
 document.getElementById('tabBtnCmd').classList.toggle('on',t==='cmd');
 document.getElementById('tabBtnProj').classList.toggle('on',t==='proj');
 document.getElementById('tabBtnProto').classList.toggle('on',t==='proto');
 qmRender();}
function qmRender(){
 const b=document.getElementById('qmBody');
 if(!QUICK){b.textContent='快捷数据未加载';return;}
 if(qmTabCur==='cmd'){
  const n=curNode(),p=effProto();
  let h='<div class="frow"><span class="fn">目标分组</span><span style="flex:1;color:#8fb7ff">'+escx(pathText())+'</span>'
   +'<span class="qop" onclick="openQmTab(&quot;proj&quot;)">改/建分组</span></div>';
  if(!n){b.innerHTML=h+'<div style="color:#8a93a3;margin-top:8px">当前在根层, 先在"分组"页建分组后再进来</div>';return;}
  const editing=(qmEditIdx>=0),ec=editing?n.cmds[qmEditIdx]:null;
  h+='<div style="margin-top:8px"><b>已有指令</b>'
   +'<span class="qop" onclick="toggleCmdMode()">'+(qmEditMode?'退出管理':'管理指令')+'</span></div><div>';
  (n.cmds||[]).forEach((c,i)=>{
   h+='<div class="frow'+(qmEditIdx===i?' editing':'')+'"><span class="fn">'+escx(c.name)+'</span>'
    +'<span style="color:#7c8ba1;font-size:12px">'
    +(c.fields?escx(JSON.stringify(c.fields)):escx((c.mode||'hex')+': '+c.data))+'</span>'
    +(qmEditMode?('<span class="qop" onclick="editCmd('+i+')">'+(qmEditIdx===i?'编辑中':'编辑')+'</span>'):'')
    +'<span class="qdel" onclick="delCmd('+i+')">删除</span></div>';});
  h+='</div><div style="margin-top:10px"><b>'
   +(editing?('修改指令: '+escx(ec.name)):(qmEditMode?'修改指令 <span style="color:#8a93a3;font-weight:400">— 点上方「编辑」选一条</span>':'新建指令'))
   +'</b></div>'
   +'<div class="frow"><span class="fn">名称</span><input type="text" id="ncName" placeholder="如 7255_fan_0" value="'
   +(ec?escx(ec.name):'')+'"></div>';
  if(p){
   const proto=QUICK.protocols[p];
   (proto&&proto.fields||[]).forEach(f=>{
    if(f.auto||f.role){   // 固定值/自动字段不用填, 但仍列出让人看到它会生成什么
     const d=(f.role==='len')?('长度='+escx(f.from||'?')+'..'+escx(f.to||'?')+(f.offset?(' +'+f.offset):''))
      :(f.role==='sum')?('校验='+escx(f.from||'?')+'..'+escx(f.to||'?')+'('+algName(f.alg)+')')
      :('固定值 '+escx(f.value||''));
     h+='<div class="frow"><span class="fn">'+escx(f.name)
      +(f.len===-1?'(变长)':'('+f.len+'B)')+'</span>'
      +'<span style="flex:1;color:#8a93a3;font-size:12px;border:1px dashed #2b3240;border-radius:3px;padding:4px 6px">'
      +'自动生成: '+d+'</span></div>';
     return;
    }
    let dv=(f.name==='SYNC'&&f.value)?f.value:'';
    if(ec&&ec.fields&&ec.fields[f.name]!==undefined)dv=ec.fields[f.name];
    h+='<div class="frow"><span class="fn">'+escx(f.name)
     +(f.len===-1?'(变长hex)':'('+f.len+'B)')+'</span>'
     +'<input type="text" id="nf_'+escx(f.name)+'" value="'+escx(dv)+'" placeholder="hex 字节"></div>';});
   h+='<div class="frow"><span class="fn">组帧预览</span><span id="ncPv" style="color:#7c8ba1;font-family:Consolas,monospace">填完后自动显示</span></div>';
  }else{
   const em=(ec&&ec.mode)||'hex',ed=(ec&&ec.data)||'';
   h+='<div class="frow"><span class="fn">类型</span><select id="ncMode">'
    +['hex','ascii'].map(m=>'<option value="'+m+'"'+(m===em?' selected':'')+'>'+m+'</option>').join('')
    +'</select></div>'
    +'<div class="frow"><span class="fn">数据</span><input type="text" id="ncData" value="'+escx(ed)+'" placeholder="hex 如 5A A5 ... 或 ascii 文本"></div>';
  }
  h+='<div style="margin-top:6px">'
   +(qmEditMode
     ?'<button onclick="saveCmd()"'+(editing?'':' disabled title="还没选中要改的指令: 请先点上方某条指令后的「编辑」"')+'>保存指令</button>'
      +(editing?'':'<span style="color:#c9a227;font-size:12px;margin-left:8px">请先点上方某条指令后的「编辑」选中要改的那条; 要新建指令请点「退出管理」</span>')
      +' <button onclick="cancelEdit()">取消</button>'
     :'<button onclick="addCmd()">添加指令</button>')
   +'</div>';
  b.innerHTML=h;
  if(p){
   (QUICK.protocols[p].fields||[]).forEach(f=>{
    if(f.auto||f.role)return;
    const el=document.getElementById('nf_'+f.name);
    if(el)el.addEventListener('input',ncPreview);});
   ncPreview();
  }
 }else if(qmTabCur==='proj'){
  const secs=Object.keys(QUICK.groups);
  const curSec=qPath.length?qPath[0]:(secs[0]||'project');
  let h='<div style="margin-top:6px"><b>新建分组 (任意层级)</b></div>'
    +'<div class="frow"><span class="fn">所属层级</span><select id="nsParent" style="flex:1">'
    +'<option value="">(新建顶层分组)</option>';
   secs.forEach(k=>{
    h+='<option value="'+escx(k)+'"'+((k===curSec)?' selected':'')+'>'+escx(k)+' (顶层)</option>';
    const rec=(ns,path)=>{(ns||[]).forEach((nd,i)=>{
     const np=path.concat([i]);
     h+='<option value="'+escx(k+'|'+np.join('.'))+'">'+escx('　'.repeat(path.length+1)+'└ '+nd.name)+'</option>';
     rec(nd.children,np);});};
    rec(QUICK.groups[k],[]);});
   h+='</select></div>'
   +'<div class="frow"><span class="fn">分组名</span><input type="text" id="nsName" placeholder="如 风扇测试"></div>'
   +'<div class="frow"><span class="fn">协议</span><select id="nsProto" style="flex:1"><option value="">(继承上级)</option>'
   +Object.keys(QUICK.protocols||{}).map(k=>'<option value="'+escx(k)+'">'+escx(k)+'</option>').join('')
   +'<option value="__none__">(手动/无协议)</option></select></div>'
   +'<div style="margin-top:4px"><button onclick="addNode()">添加分组</button></div>'
   +'<div style="margin-top:12px"><b>全部分组树</b></div>';
  secs.forEach(k=>{
   h+='<div class="treeroot">'+escx(k)+'</div>';
   const rec=(ns,path)=>{
    (ns||[]).forEach((nd,i)=>{
     const np=path.concat([i]);
     h+='<div class="frow" style="padding-left:'+(12+path.length*16)+'px">'
      +'<span class="fn">'+escx(nd.name)+'</span>'
      +'<span style="color:#7c8ba1;font-size:12px">'
      +((nd.protocol)?('协议: '+escx(nd.protocol)+' · '):'')
      +((nd.children||[]).length?((nd.children||[]).length+' 个子分组 · '):'')
      +((nd.cmds||[]).length+' 条指令')+'</span>'
      +'<span class="qop" onclick="qJump(&quot;'+escx(k)+'&quot;,['+np.join(',')+'])">定位</span>'
      +'<span class="qdel" onclick="delNode(&quot;'+escx(k)+'&quot;,['+np.join(',')+'])">删除</span></div>';
     rec(nd.children,np);});
   };
   rec(QUICK.groups[k],[]);});
  b.innerHTML=h;
 }else{
  let h='<div style="margin-top:6px"><b>新建协议</b></div>'
   +'<div class="frow"><span class="fn">协议名</span><input type="text" id="nprName" placeholder="如 魏桥协议V2"></div>'
   +'<div class="frow"><span class="fn">模板</span><select id="nprTpl"><option value="">空白</option>'
   +Object.keys(QUICK.protocols||{}).map(k=>'<option value="'+escx(k)+'">复制 '+escx(k)+'</option>').join('')
   +'</select></div>'
   +'<div style="margin-top:4px"><button onclick="addProto()">添加协议</button></div>'
   +'<div style="margin-top:12px"><b>查看协议</b> <span style="color:#8a93a3;font-weight:400">— 下拉选中后按回车显示, 可同时显示多个对比</span></div>'
   +'<div class="frow"><span class="fn">选择协议</span><select id="epName" onkeydown="epKey(event)">'
   +'<option value="">— 选择后回车 —</option>'
   +Object.keys(QUICK.protocols||{}).map(k=>'<option value="'+escx(k)+'">'+escx(k)+'</option>').join('')
   +'</select>'
   +(epShow.length?' <span style="color:#7c8ba1">已显示 '+epShow.length+' 个</span>':'')
   +'</div>';
  epShow.forEach(name=>{
   const proto=QUICK.protocols[name];if(!proto)return;
   const editing=(epEdit===name);
   h+='<div class="pblock">'
    +'<div class="frow" style="margin-bottom:4px"><b style="flex:0 0 auto">'+escx(name)+'</b>'
    +(editing
      ?'<span class="qop" onclick="saveProtoEdit()">保存修改</span>'
       +'<span class="qop" onclick="cancelProtoEdit()">取消编辑</span>'
      :'<span class="qop" onclick="editProto(&quot;'+escx(name)+'&quot;)">编辑</span>')
    +'<span class="qdel" onclick="delProto(&quot;'+escx(name)+'&quot;)">删除</span>'
    +'<span class="qop" style="margin-left:auto" onclick="delShowProto(&quot;'+escx(name)+'&quot;)">取消显示</span></div>';
   if(editing){
    h+='<div class="frow"><span class="fn">说明</span><input type="text" id="epDesc" value="'+escx(proto.desc||'')+'" oninput="pvDesc()" placeholder="描述这个协议, 可插入下方占位符"></div>'
     +'<div class="frow"><span class="fn"></span><span style="flex:1;color:#7c8ba1;font-size:12px">占位符(点击插入): '
     +DESC_PH.map(p=>'<span class="qop" style="margin-right:10px" onclick="insDesc(&quot;'+p+'&quot;)" title="'+escx(descPhTip(p))+'">'+p+'</span>').join('')
     +'</span></div>'
     +'<div class="frow"><span class="fn"></span><span id="epDescPv" style="flex:1;color:#8a93a3;font-size:12px;line-height:1.6;border:1px dashed #2b3240;border-radius:3px;padding:4px 6px"></span></div>'
     +'<div style="margin-top:6px">字段(类型: 手填=发指令时输入 / const=固定值; 角色: LEN=算区间字节数 / SUM=算区间校验):</div>';
    const allNames=(proto.fields||[]).map(f=>f.name);
    const optOf=(sel)=>allNames.map(n=>'<option value="'+escx(n)+'"'+(n===sel?' selected':'')+'>'+escx(n)+'</option>').join('');
    // 列宽常量: 表头与数据行共用, 保证逐列对齐 (合计 916px + 6*6 gap)
    const COL=[96,64,180,88,100,368,20];
    const W=i=>'flex:0 0 '+COL[i]+'px';
    h+='<div class="feditwrap"><div class="fedit fhead">'
     +'<span style="'+W(0)+'">字段名</span>'
     +'<span style="'+W(1)+'">长度(B)</span>'
     +'<span style="'+W(2)+'">值 / 自动生成</span>'
     +'<span style="'+W(3)+'">类型</span>'
     +'<span style="'+W(4)+'">角色</span>'
     +'<span style="'+W(5)+'">区间 (LEN/SUM)</span>'
     +'<span style="'+W(6)+'"></span></div>';
    (proto.fields||[]).forEach((f,i)=>{
     const role=f.role||'';
     const autoDesc=(role==='len')
       ?('长度='+escx(f.from||'?')+'..'+escx(f.to||'?')+(f.offset?(' +'+f.offset):''))
       :(role==='sum')?('校验='+escx(f.from||'?')+'..'+escx(f.to||'?')+'('+algName(f.alg)+')')
       :(f.auto==='const')?('固定值 '+escx(f.value||''))
       :(f.auto?escx(f.auto):'');
     h+='<div class="fedit">'
      +'<input style="'+W(0)+'" type="text" value="'+escx(f.name)+'" id="fd_'+i+'_name">'
      +'<input style="'+W(1)+'" type="text" value="'+f.len+'" id="fd_'+i+'_len" title="字节数,-1=变长">'
      +(role
        ?'<span class="fauto" style="'+W(2)+'" title="'+escx(autoDesc)+'">自动: '+autoDesc+'</span>'
        :'<input style="'+W(2)+'" type="text" value="'+escx(f.value||'')+'" id="fd_'+i+'_val" placeholder="默认值hex">')
      +'<select style="'+W(3)+'" id="fd_'+i+'_auto"'+(role?' disabled':'')+'>'
      +['','const'].map(a=>'<option'+(a===(f.auto||'')?' selected':'')+' value="'+a+'">'+(a||'手填')+'</option>').join('')
      +'</select>'
      +'<select style="'+W(4)+'" id="fd_'+i+'_role" onchange="setRole('+i+',this.value)">'
      +[['','自定义'],['len','LEN 长度'],['sum','SUM 校验']].map(r=>'<option'+(r[0]===role?' selected':'')+' value="'+r[0]+'">'+r[1]+'</option>').join('')
      +'</select>'
      +'<span class="frange" style="'+W(5)+'">';
     if(role==='len'){
      // offset 只在非 0 时才有存在意义(区间外还有未建模字节); 为 0 时只留一个占位, 点击才展开
      h+='<span class="fb">从</span><select style="flex:0 0 96px" id="fd_'+i+'_from">'+optOf(f.from)+'</select>'
       +'<span class="fb">到</span><select style="flex:0 0 96px" id="fd_'+i+'_to">'+optOf(f.to)+'</select>'
       +(f.offset
         ?'<input style="flex:0 0 58px" type="text" value="'+f.offset+'" id="fd_'+i+'_off" title="区间字节数 + N">'
         :'<span class="fb" style="flex:0 0 58px;cursor:pointer;border:1px dashed #2b3240;border-radius:3px" id="fd_'+i+'_offbtn" onclick="showOff('+i+')" title="区间外还有未建模字节时, 在此加偏移量">+偏移</span>');
     }else if(role==='sum'){
      h+='<span class="fb">从</span><select style="flex:0 0 88px" id="fd_'+i+'_from">'+optOf(f.from)+'</select>'
       +'<span class="fb">到</span><select style="flex:0 0 88px" id="fd_'+i+'_to">'+optOf(f.to)+'</select>'
       +'<select style="flex:0 0 116px" id="fd_'+i+'_alg" title="CHECKSUM 计算方法">'
       +SUM_ALGS.map(a=>'<option'+(a[0]===(f.alg||'sum_neg')?' selected':'')+' value="'+a[0]+'">'+a[1]+'</option>').join('')
       +'</select>';
     }
     h+='</span><span class="qdel" style="'+W(6)+';margin:0" onclick="delField('+i+')">×</span></div>';});
    h+='<div class="fedit"><button onclick="addField()">+字段</button>'
     +'<select style="'+W(4)+'" id="fdNewRole">'
     +[['','自定义'],['len','LEN 长度'],['sum','SUM 校验']].map(r=>'<option value="'+r[0]+'">'+r[1]+'</option>').join('')
     +'</select></div></div>';
   }else{
    h+='<div class="frow"><span class="fn">说明</span><span style="color:#c3ccd8">'+escx(expandDesc(proto,name,proto.desc)||'—')+'</span></div>';
    const fdesc=f=>{
     const role=f.role||'';
     if(role==='len')return', 长度='+escx(f.from||'?')+'..'+escx(f.to||'?')+(f.offset?(' +'+(f.offset)):'');
     if(role==='sum')return', 校验='+escx(f.from||'?')+'..'+escx(f.to||'?')+'('+algName(f.alg)+')';
     if(f.auto==='const')return', 常量 '+escx(f.value||'');
     if(f.auto)return', '+escx(f.auto);
     return', 默认 '+escx(f.value||'—');};
    h+='<div class="frow" style="align-items:flex-start"><span class="fn">字段</span><div style="flex:1;color:#c3ccd8;font-family:Consolas,monospace;font-size:12px;line-height:1.7">'
     +(proto.fields||[]).map(f=>'<span style="color:#7ee787">'+escx(f.name)+'</span>('+(f.len===-1?'变长':f.len+'B')
       +fdesc(f)+')').join('<br>')
     +'</div></div>';
   }
   h+='</div>';
  });
  b.innerHTML=h;
  if(qmTabCur==='proto'&&epEdit)pvDesc();   // 进编辑态先渲染一次说明预览
 }
}
let epShow=[],epEdit='';
function openQmTab(t){openQm();if(t)qmTab(t);}
async function ncPreview(){
 const p=effProto();if(!p)return;
 const fields={};
 (QUICK.protocols[p].fields||[]).forEach(f=>{
  if(f.auto||f.role)return;const el=document.getElementById('nf_'+f.name);
  if(el&&el.value.trim())fields[f.name]=el.value.trim();});
 try{
  const r=await fetch('/preview',{method:'POST',headers:{'Content-Type':'application/json'},
   body:JSON.stringify({proto:p,fields:fields})});
  const j=await r.json();
  const el=document.getElementById('ncPv');
  if(el)el.textContent=j.ok?j.hex:('错误: '+(j.msg||''));
 }catch(e){}
}
async function addCmd(){
 const n=curNode(),p=effProto(),name=document.getElementById('ncName').value.trim();
 if(!n){await uiAlert('当前在根层, 请先在下拉里进入某个分组');return;}
 if(!name){await uiAlert('请填指令名称');return;}
 if(p){
  const fields={};
  (QUICK.protocols[p].fields||[]).forEach(f=>{
   if(f.auto||f.role)return;const el=document.getElementById('nf_'+f.name);
   fields[f.name]=(el&&el.value.trim())||'';});
  n.cmds=n.cmds||[];n.cmds.push({name:name,fields:fields});
 }else{
  const d=document.getElementById('ncData').value.trim();
  if(!d){await uiAlert('请填数据');return;}
  n.cmds=n.cmds||[];
  n.cmds.push({name:name,mode:document.getElementById('ncMode').value,data:d});
 }
 qmEditIdx=-1;
 saveQuick();
}
/* 管理指令: 编辑态 */
async function toggleCmdMode(){
 const n=curNode();
 if(!qmEditMode){qmEditMode=true;qmEditIdx=-1;}
 else if(qmEditIdx>=0&&n&&n.cmds[qmEditIdx]&&n.cmds[qmEditIdx].name!==document.getElementById('ncName').value.trim()){
  if(!await uiConfirm('放弃正在编辑的指令改动?'))return;
  qmEditMode=false;qmEditIdx=-1;
 }else{qmEditMode=false;qmEditIdx=-1;}
 qmRender();
}
function editCmd(i){qmEditIdx=i;qmRender();}
function cancelEdit(){qmEditIdx=-1;qmRender();}
/* 保存指令: 覆盖正在编辑的那条 */
async function saveCmd(){
 const n=curNode(),p=effProto();
 if(!n||!qmEditMode){return;}
 if(qmEditIdx<0||!n.cmds[qmEditIdx]){await uiAlert('请先点上方「编辑」选择要修改的指令');return;}
 const name=document.getElementById('ncName').value.trim();
 if(!name){await uiAlert('请填指令名称');return;}
 if(p){
  const fields={};
  (QUICK.protocols[p].fields||[]).forEach(f=>{
   if(f.auto||f.role)return;const el=document.getElementById('nf_'+f.name);
   fields[f.name]=(el&&el.value.trim())||'';});
  n.cmds[qmEditIdx]={name:name,fields:fields};
 }else{
  const d=document.getElementById('ncData').value.trim();
  if(!d){await uiAlert('请填数据');return;}
  n.cmds[qmEditIdx]={name:name,mode:document.getElementById('ncMode').value,data:d};
 }
 qmEditIdx=-1;
 saveQuick();
}
async function delCmd(i){
 const n=curNode();if(!n||!n.cmds)return;
 const c=n.cmds[i];if(!c)return;
 const body=c.fields?Object.keys(c.fields).map(k=>k+'='+c.fields[k]).join(' ')
  :((c.mode||'hex')+': '+c.data);
 if(!await uiConfirm('删除指令「'+c.name+'」?\\n内容: '+body+'\\n此操作保存后生效(可用「回退上一步」撤销)。'))return;
 n.cmds.splice(i,1);
 if(qmEditIdx>=n.cmds.length)qmEditIdx=n.cmds.length-1;
 saveQuick();}
function pathLabel(sec,path){
 const ns=pathNamesOf(sec,path);return sec+(ns.length?' / '+ns.join(' / '):'');
}
/* 在任意层级新建分组: 父级由 nsParent 决定, 空=新建顶层分组 */
async function addNode(){
 const name=document.getElementById('nsName').value.trim();
 if(!name){await uiAlert('请填分组名');return;}
 let proto=document.getElementById('nsProto').value;
 if(proto==='')proto=undefined; else if(proto==='__none__')proto=null;
 const pv=document.getElementById('nsParent').value;
 if(!pv){
  let k=name,i=1;while(QUICK.groups[k]&&QUICK.groups[k].length)k=name+'_'+(++i);
  const nd={name:name,children:[],cmds:[]};
  if(proto!==undefined)nd.protocol=proto;
  QUICK.groups[k]=[nd];
  qPath=[k,0];saveQuick();return;
 }
 const ix=pv.indexOf('|');
 let sec,path;
 if(ix<0){sec=pv;path=[];}else{sec=pv.slice(0,ix);path=pv.slice(ix+1).split('.').map(Number);}
 let list=(path.length?((nodeAtPath(sec,path)||{}).children):QUICK.groups[sec]);
 if(!list){await uiAlert('父级不存在');return;}
 const nd={name:name,children:[],cmds:[]};
 if(proto!==undefined)nd.protocol=proto;
 list.push(nd);
 qPath=[sec].concat(path).concat([list.length-1]);
 saveQuick();
}
function qJump(sec,path){qPath=[sec].concat(path);renderNav();closeQm();}
async function delNode(sec,path){
 const n=nodeAtPath(sec,path);
 if(!n){return;}
 // 统计整个子树(含深层)的分组数与指令数
 let sub=0,cmds=0;
 const cnt=nd=>{(nd.children||[]).forEach(c=>{sub++;cmds+=(c.cmds||[]).length;cnt(c);});};
 cmds+=(n.cmds||[]).length;cnt(n);
 if(!await uiConfirm('删除分组「'+pathLabel(sec,path)+'」?\\n将一并删除其下全部内容: 子分组 '+sub+' 个 / 指令 '+cmds+' 条\\n此操作保存后生效(可用「回退上一步」撤销)。'))return;
 const list=(path.length===1?QUICK.groups[sec]:(nodeAtPath(sec,path.slice(0,-1)).children));
 list.splice(path[path.length-1],1);
 qPath=[sec].concat(path.slice(0,-1));
 if(!qPath.length||!QUICK.groups[qPath[0]])qPath=[];
 saveQuick();
}
/* 协议Tab: 多选查看 + 点编辑进入修改 */
function epKey(e){
 if(e.key==='Enter'){addShowProto(e.target.value);e.target.value='';}
}
function addShowProto(v){
 if(!v||!QUICK.protocols[v])return;
 if(epShow.indexOf(v)<0)epShow.push(v);
 qmRender();
}
function delShowProto(v){
 const i=epShow.indexOf(v);if(i>=0)epShow.splice(i,1);
 if(epEdit===v)epEdit='';
 qmRender();
}
function editProto(v){
 if(!QUICK.protocols[v])return;
 if(epEdit&&epEdit!==v)collectProtoEdit();  // 之前编辑中的输入先落回内存(不丢)
 epEdit=v;qmRender();
}
function cancelProtoEdit(){epEdit='';qmRender();}
function saveProtoEdit(){
 if(!epEdit)return;
 collectProtoEdit();
 const done=epEdit;epEdit='';
 saveQuick().then(()=>{epEdit='';qmRender();});
}
async function addProto(){
 const name=document.getElementById('nprName').value.trim();
 if(!name){await uiAlert('请填协议名');return;}
 if(QUICK.protocols[name]){await uiAlert('协议已存在');return;}
 const tpl=document.getElementById('nprTpl').value;
 QUICK.protocols[name]=tpl?JSON.parse(JSON.stringify(QUICK.protocols[tpl]))
  :{desc:'',fields:[{name:'DATA',len:-1}],checksum:{from:0}};
 if(epShow.indexOf(name)<0)epShow.push(name);
 epEdit=name;
 saveQuick().then(()=>{qmRender();});
}
async function delProto(v){
 v=(v===undefined)?epEdit:v;
 if(!v||!QUICK.protocols[v])return;
 // 找出绑定该协议的分组, 一并列在确认框里
 const refs=[];
 const rec=(ns,p)=>{(ns||[]).forEach(n=>{if(n.protocol===v)refs.push(p.concat(n.name));rec(n.children,p.concat(n.name));});};
 Object.keys(QUICK.groups||{}).forEach(k=>rec(QUICK.groups[k],[k]));
 let msg='删除协议「'+v+'」?';
 if(refs.length){
  msg+='\\n注意: 以下 '+refs.length+' 个分组绑定着它(删除后这些分组的手填指令将无法组帧):\\n  '
   +refs.slice(0,6).map(p=>p.join('/')).join('\\n  ')
   +(refs.length>6?('\\n  …等 '+refs.length+' 个'):'');
 }
 msg+='\\n此操作保存后生效(可用「回退上一步」撤销)。';
 if(!await uiConfirm(msg))return;
 delete QUICK.protocols[v];
 const i=epShow.indexOf(v);if(i>=0)epShow.splice(i,1);
 if(epEdit===v)epEdit='';
 saveQuick().then(()=>{qmRender();});
}
function showOff(i){
 // 把「+偏移」占位就地换成输入框; 不重渲染, 以免 offset 仍为 0 又被收回去
 const el=document.getElementById('fd_'+i+'_offbtn');if(!el)return;
 const inp=document.createElement('input');
 inp.type='text';inp.id='fd_'+i+'_off';inp.value='0';
 inp.style.cssText='flex:0 0 58px';
 inp.title='区间字节数 + N';
 el.replaceWith(inp);inp.focus();inp.select();
}
function setRole(i,role){
 const proto=QUICK.protocols[epEdit];if(!proto||!proto.fields[i])return;
 collectProtoEdit();
 const f=proto.fields[i];
 if(!role){delete f.role;delete f.from;delete f.to;delete f.offset;delete f.alg;}
 else if(role==='len'){
  f.role='len';f.len=(f.len===-1?2:f.len)||2;delete f.auto;delete f.alg;
  if(!f.from||!f.to){const ns=proto.fields.map(x=>x.name);
   f.from=f.from||ns[Math.max(i-2,0)]||ns[0];f.to=f.to||ns[Math.max(i-1,0)]||ns[0];}
  delete f.offset;   // 默认 0 且不显示; 需要时点「+偏移」再展开
 }else{
  f.role='sum';f.len=1;delete f.auto;
  if(!f.alg)f.alg='sum_neg';   // 默认保持现有协议用的算法
  if(!f.from||!f.to){const ns=proto.fields.map(x=>x.name);
   f.from=f.from||ns[Math.max(i-2,0)]||ns[0];f.to=f.to||ns[Math.max(i-1,0)]||ns[0];}
  delete f.offset;
 }
 qmRender();
}
function addField(){
 const proto=QUICK.protocols[epEdit];if(!proto)return;
 collectProtoEdit();
 proto.fields=proto.fields||[];
 const role=(document.getElementById('fdNewRole')||{}).value||'';
 const name=(role==='len'?'LEN':(role==='sum'?'SUM':'F'+proto.fields.length));
 const ns=proto.fields.map(f=>f.name);
 const nf={name:name,len:(role==='sum'?1:(role==='len'?2:1)),value:''};
 if(role==='len'){nf.role='len';nf.from=ns[ns.length-1]||name;nf.to=nf.from;}
 else if(role==='sum'){nf.role='sum';nf.alg='sum_neg';nf.from=ns[0]||name;nf.to=ns[ns.length-1]||name;}
 proto.fields.push(nf);qmRender();}
async function delField(i){
 const proto=QUICK.protocols[epEdit];if(!proto||!proto.fields)return;
 const el=document.getElementById('fd_'+i+'_name');
 const nm=(el&&el.value.trim())||((proto.fields[i]||{}).name);
 let extra='';
 // 该字段被别的自动字段的区间引用时, 一并提示
 const refs=(proto.fields||[]).filter((f,j)=>j!==i&&(f.from===nm||f.to===nm)).map(f=>f.name);
 if(refs.length)extra='\\n注意: 字段「'+refs.join('、')+'」的区间引用了它, 删除后这些区间会失效。';
 if(!await uiConfirm('删除字段「'+nm+'」?\\n该协议所有指令的这个字段输入将失效。'+extra+'\\n此操作保存后生效(可用「回退上一步」撤销)。'))return;
 collectProtoEdit();
 proto.fields.splice(i,1);qmRender();}
function collectProtoEdit(){
 const proto=QUICK.protocols[epEdit];if(!proto||!document.getElementById('epDesc'))return;
 proto.desc=document.getElementById('epDesc').value;
 proto.fields.forEach((f,i)=>{
  const g=id=>document.getElementById('fd_'+i+'_'+id);
  f.name=(g('name').value.trim())||f.name;
  f.len=parseInt(g('len').value)||f.len;
  if(g('val'))f.value=g('val').value.trim();
  if(f.role==='len'||f.role==='sum'){
   if(g('from')&&g('from').value)f.from=g('from').value;
   if(g('to')&&g('to').value)f.to=g('to').value;
   if(f.role==='len'){  // offset 为 0 视为无偏移, 不落盘也不显示
    if(g('off')){const v=parseInt(g('off').value)||0;if(v)f.offset=v;else delete f.offset;}
    delete f.alg;}
   else{if(g('alg')&&g('alg').value)f.alg=g('alg').value;else f.alg=f.alg||'sum_neg';delete f.offset;}
   delete f.auto;
  }else{delete f.role;delete f.from;delete f.to;delete f.offset;delete f.alg;
   f.auto=g('auto').value||undefined;}});
 delete proto.checksum;}
/* 回退上一步: 后端 quick_send.json.bak 是每次保存前的快照,
   回退=当前与备份交换(再点一次可撤销本次回退) */
async function undoQuick(){
 let j;
 try{const r=await fetch('/quick_backup');j=await r.json();}
 catch(e){await uiAlert('获取备份失败: '+netErr(e));return;}
 if(!j.ok){await uiAlert(j.msg||'没有可回退的备份');return;}
 const t=j.bak_time?new Date(j.bak_time*1000).toLocaleString():'未知时间';
 if(!await uiConfirm('回退到上一步配置?\\n备份时间: '+t+'\\n\\n回退后将:\\n  '+j.diff.join('\\n  ')
  +'\\n\\n确定回退? (再点一次「回退上一步」可撤销本次回退)'))return;
 try{
  const r=await fetch('/quick_restore',{method:'POST'});
  const k=await r.json();
  if(!k.ok){await uiAlert('回退失败: '+(k.msg||''));return;}
  QUICK=k.data;normalizeQuick();qPath=[];resetCmdEdit();renderNav();qmRender();
 }catch(e){await uiAlert('回退失败: '+netErr(e));}
}
async function saveQuick(){
 if(qmTabCur==='proto')collectProtoEdit();
 try{
  const r=await fetch('/quick',{method:'POST',headers:{'Content-Type':'application/json'},
   body:JSON.stringify(QUICK)});
  const j=await r.json();
  if(!j.ok){await uiAlert('保存失败: '+(j.msg||''));return;}
  QUICK=j.data;normalizeQuick();renderNav();qmRender();
 }catch(e){await uiAlert('保存失败: '+netErr(e));}
}
poll();pollAi();loadPorts();loadBauds();loadBg();refreshConn();refreshDiagBadge();loadQuick();
layoutBars();
window.addEventListener('resize',layoutBars);
setInterval(refreshConn,3000);
setInterval(refreshDiagBadge,5000);
document.addEventListener('keydown',e=>{if(e.key==='Escape'){hideDiag();hideLogs();}});
</script></body></html>"""


class Handler(BaseHTTPRequestHandler):
    def handle(self):
        """客户端在请求还没读完/回写前就断开(刷新、关页、切网)会抛
        ConnectionReset/Aborted 10054/10053; 这是常态, 不该刷屏打崩线程。"""
        try:
            super().handle()
        except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError, OSError):
            return

    def _send(self, body, ctype, code=200, cache=None):
        """统一回写: 客户端中途断开是常态(如连接耗时长时用户刷新/关页),
        绝不能让它冒泡成 ConnectionAbortedError 打崩请求线程。"""
        try:
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            if cache:
                self.send_header("Cache-Control", cache)
            self.end_headers()
            self.wfile.write(body)
        except (ConnectionAbortedError, BrokenPipeError, ConnectionResetError, OSError):
            return

    def _json(self, obj, code=200):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self._send(body, "application/json; charset=utf-8", code)

    def do_GET(self):
        if self.path == "/" or self.path.startswith("/index"):
            self._send(HTML.encode("utf-8"), "text/html; charset=utf-8")
        elif self.path.startswith("/stream"):
            q = self.path.split("since=", 1)
            since = int(q[1]) if len(q) > 1 and q[1].isdigit() else 0
            try:
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream")
                self.send_header("Cache-Control", "no-cache")
                self.end_headers()
            except (ConnectionAbortedError, BrokenPipeError, ConnectionResetError, OSError):
                return
            cur = since
            # since=0 表示网页新连接(首开/刷新): 只回放最近 REPLAY_TAIL 行,
            # 避免整段内存缓冲重放导致刷新后满屏; since>0 为增量, 行为不变。
            if since == 0 and REPLAY_TAIL > 0:
                with lock:
                    cur = max(0, seq - REPLAY_TAIL)
            try:
                while True:
                    with lock:
                        items = [h for h in history if h[0] > cur]
                        stats = f"行:{seq} 收:{rx_bytes}B"
                    if items:
                        chunk = "".join(
                            f"data: {json.dumps({'s': s, 'ts': ts, 't': t, 'h': h, 'l': l, 'i': i, 'st': stats}, ensure_ascii=False)}\n\n"
                            for s, ts, t, h, l, i in items)
                        self.wfile.write(chunk.encode("utf-8"))
                        self.wfile.flush()
                        cur = items[-1][0]
                    else:
                        self.wfile.write(f"data: {json.dumps({'st': stats})}\n\n".encode("utf-8"))
                        self.wfile.flush()
                    time.sleep(0.3)
            except (BrokenPipeError, ConnectionAbortedError, ConnectionResetError, OSError):
                return
        elif self.path.startswith("/stats"):
            # 统计(供 AI 汇报"先告诉我是否有 error/warn")
            c = level_counts()
            with lock:
                c["reader_err"] = conn["err"] or None
                c["conn"] = {"open": conn["open"], "port": conn["port"], "baud": conn["baud"]}
                c["rx_bytes"] = rx_bytes   # 已收字节(波特率错时也会 >0, 用于区分"没收到"和"收到没显示")
            self._json(c)
        elif self.path.startswith("/ports"):
            # 可用串口列表(网页下拉)
            self._json(get_ports())
        elif self.path.startswith("/bauds"):
            # 波特率候选(config [serial] bauds); 网页下拉用, 输入框仍可手填
            self._json(get_baud_candidates())
        elif self.path.startswith("/logs"):
            # 已保存的日志文件列表(output/logs), 供网页"打开日志"选文件
            self._json(list_log_files())
        elif self.path.startswith("/logfile"):
            # 读取指定日志文件, 转成与 /stream 一致的行结构
            q = self.path.split("name=", 1)
            name = q[1].split("&")[0] if len(q) > 1 else ""
            try:
                from urllib.parse import unquote
                name = unquote(name)
            except Exception:
                pass
            self._json(load_log_file(name))
        elif self.path.startswith("/bg"):
            # 默认背景: 取 assets 目录第一张图, 没有则空(前端回退纯色)
            imgs = list_assets()
            self._json({"url": ("/assets/" + imgs[0]) if imgs else "",
                        "all": imgs})
        elif self.path.startswith("/assets/"):
            # 静态素材(背景图等), 禁止路径穿越
            name = self.path.split("/assets/", 1)[1].split("?")[0]
            safe = Path(name).name
            fp = ASSETS_DIR / safe
            if safe and fp.is_file() and fp.suffix.lower() in BG_EXT:
                self._send(fp.read_bytes(), BG_EXT[fp.suffix.lower()], cache="max-age=60")
            else:
                self._send(b"", "text/plain; charset=utf-8", 404)
        elif self.path.startswith("/diag_sum"):
            # 顶部徽标轻量轮询: 只回异常计数, 不碰硬件(probe=False)
            d = do_diag(None, probe=False)
            self._json({"ok": d["ok"], "bad": len([c for c in d["checks"] if not c["ok"]]),
                        "total": len(d["checks"]), "connected": d["connected"]})
        elif self.path.startswith("/diag"):
            # 连接诊断: 为什么未连接 / 当前错误详情(网页"查看详情")
            q = self.path.split("port=", 1)
            p = q[1].split("&")[0] if len(q) > 1 else None
            self._json(do_diag(p))
        elif self.path.startswith("/conn"):
            # 当前连接状态(网页轮询)
            with lock:
                self._json({"open": conn["open"], "port": conn["port"],
                            "baud": conn["baud"], "msg": conn["msg"], "err": conn["err"],
                            "preset": conn["preset"]})
        elif self.path.startswith("/quick_backup"):
            # 回退预览: .bak 与当前的差异摘要
            self._json(quick_backup())
        elif self.path.startswith("/quick"):
            # 快捷发送配置(协议+分组+指令)
            self._json(load_quick())
        elif self.path.startswith("/ai_results"):
            q = self.path.split("after=", 1)
            after = int(q[1]) if len(q) > 1 and q[1].isdigit() else 0
            with lock:
                items = [a for a in ai_results if a["id"] > after]
            self._json(items)
        elif self.path.startswith("/selection_pending"):
            with lock:
                self._json(selection_req or {})
        else:
            self._send(b"", "text/plain; charset=utf-8", 404)

    def do_POST(self):
        global ai_seq, selection_req
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length)
        if self.path == "/connect":
            # 网页"连接": {"port": "COM6", "baud": 921600, "auto_baud": false}
            # auto_baud 默认 false：连接只用输入框波特率直连；检测是"自动检测波特率"按钮的事
            try:
                req = json.loads(raw.decode("utf-8"))
            except Exception:
                req = {}
            ok, msg = do_connect(req.get("port", ""), req.get("baud", 921600),
                                 bool(req.get("auto_baud", False)))
            self._json({"ok": ok, "msg": msg})
        elif self.path == "/disconnect":
            ok, msg = do_disconnect()
            self._json({"ok": ok, "msg": msg})
        elif self.path == "/detect_baud":
            # 网页"自动检测波特率": {"port": "COM6"}
            try:
                req = json.loads(raw.decode("utf-8"))
            except Exception:
                req = {}
            ok, baud, msg = do_detect(req.get("port", ""))
            self._json({"ok": ok, "baud": baud, "msg": msg})
        elif self.path == "/detect_stop":
            # 网页"停止检测"(检测中按钮变为停止态): 置位事件, detect_baud 下一档开始前退出
            _detect_stop.set()
            self._json({"ok": True, "msg": "停止请求已下发(最迟1.8秒内生效)"})
        elif self.path == "/ai_result":
            # AI 注入分析结果: {"text": "..."}
            try:
                text = json.loads(raw.decode("utf-8")).get("text", "")
            except Exception:
                text = raw.decode("utf-8", errors="replace")
            with lock:
                ai_seq += 1
                ai_results.append({"id": ai_seq, "ts": time.time(), "text": text})
            self._json({"ok": True, "id": ai_seq})
        elif self.path == "/selection":
            # 网页提交选中行: {"lines": [...]}
            try:
                lines = json.loads(raw.decode("utf-8")).get("lines", [])
            except Exception:
                lines = []
            with lock:
                ai_seq += 1
                selection_req = {"id": ai_seq, "ts": time.time(), "lines": lines}
            (LOG_DIR).mkdir(parents=True, exist_ok=True)
            (LOG_DIR / "selection_pending.json").write_text(
                json.dumps(selection_req, ensure_ascii=False, indent=2), encoding="utf-8")
            self._json({"ok": True, "file": str(LOG_DIR / "selection_pending.json")})
        elif self.path == "/send":
            # 发送: {"mode":"hex"|"ascii","data":"...","crlf":bool}
            try:
                req = json.loads(raw.decode("utf-8"))
            except Exception:
                req = {}
            ok, msg, n, hexs = do_send_data(req.get("mode", "hex"),
                                            req.get("data", ""), bool(req.get("crlf")))
            self._json({"ok": ok, "msg": msg, "n": n, "hex": hexs})
        elif self.path == "/preview":
            # 协议组帧预览(不发送): {"proto":"协议名","fields":{...}}
            try:
                req = json.loads(raw.decode("utf-8"))
            except Exception:
                req = {}
            proto = load_quick()["protocols"].get(req.get("proto", ""))
            if not proto:
                self._json({"ok": False, "msg": f"协议不存在: {req.get('proto')}"})
            else:
                try:
                    frame = build_frame(proto, req.get("fields", {}))
                    self._json({"ok": True,
                                "hex": " ".join(f"{x:02X}" for x in frame)})
                except Exception as e:
                    self._json({"ok": False, "msg": f"组帧失败: {e}"})
        elif self.path == "/quick_restore":
            # 回退上一步: 当前与 .bak 交换
            ok, ret = quick_restore()
            self._json({"ok": ok, "msg": "" if ok else str(ret), "data": ret if ok else None})
        elif self.path == "/quick":
            # 保存快捷发送配置(整包)
            try:
                req = json.loads(raw.decode("utf-8"))
            except Exception:
                req = None
            if req is None:
                self._json({"ok": False, "msg": "JSON 解析失败"})
                return
            ok, ret = save_quick(req)
            self._json({"ok": ok, "msg": "" if ok else str(ret), "data": ret if ok else None})
        elif self.path == "/dump":
            # 网页"保存日志"按钮: {"path": ""=默认或自定义路径, "mail": bool,
            #                      "analysis_mode": fixed|free|auto|"", "depth": low|medium|high,
            #                      "focus": 正则, "project": config [projects] 编号|工程路径}
            try:
                req = json.loads(raw.decode("utf-8"))
            except Exception:
                req = {}
            path = req.get("path", "")
            do_mail = bool(req.get("mail"))
            a_mode = (req.get("analysis_mode") or "").strip()
            a_focus = (req.get("focus") or "").strip() or None
            a_project = (req.get("project") or "").strip() or None
            # 铁律: 有特殊要求时严格按用户要求分析, 强度不生效
            a_depth = None if a_focus else ((req.get("depth") or "medium").strip() or "medium")
            resp = {}
            try:
                if path:
                    target = Path(path)
                else:
                    target = LOG_DIR / f"serial_{datetime.now():%Y%m%d_%H%M%S}_完成采集.log"
                target.parent.mkdir(parents=True, exist_ok=True)
                n = dump_history(target)
                c = level_counts()
                resp.update({"ok": True, "path": str(target), "lines": n,
                             "warn": c["warn"], "error": c["error"]})
            except Exception as e:
                self._json({"ok": False, "err": str(e)})
                return
            # 分析: 邮件发送时按用户选的 方式/强度/特殊要求/关联工程 出 正文摘要 + HTML 报告
            analysis_text, html_path = (None, None)
            if do_mail and a_mode:
                analysis_text, html_path = run_analysis(target, a_mode, a_focus,
                                                        None, None, a_depth, a_project)
                if html_path:
                    resp["html"] = str(html_path)
            if do_mail:
                # dump 后发飞书邮件: 附件 = 日志 + 分析 HTML; 正文 = 分析摘要
                import subprocess
                subject = f"串口日志 {target.name} ({n}行)"
                body = (f"来自 Web 监视器保存并发送\n文件: {target}\n行数: {n}\n"
                        f"WARN: {c['warn']}  ERROR: {c['error']}\n"
                        f"时间: {datetime.now():%Y-%m-%d %H:%M:%S}\n" + "-" * 30 + "\n"
                        + (analysis_text if analysis_text else
                           "（未选分析方式, 未附分析结果；可手动跑 analyze_log.py）"))
                attaches = [str(target)]
                if html_path:
                    attaches.append(str(html_path))
                try:
                    r = subprocess.run(
                        [sys.executable, str(SKILL_DIR / "scripts" / "common" / "send_mail.py"),
                         subject, body] + attaches,
                        capture_output=True, text=True, timeout=120,
                        encoding="utf-8", errors="replace")
                    resp["mail_ok"] = ("[OK]" in (r.stdout or ""))
                    resp["mail_err"] = (r.stderr or "")[:200] if not resp["mail_ok"] else ""
                except Exception as e:
                    resp["mail_ok"] = False
                    resp["mail_err"] = str(e)[:200]
            self._json(resp)
        else:
            self._send(b"", "text/plain; charset=utf-8", 404)

    def log_message(self, *args):
        pass


# ---------------------------------------------------------------------------
# 快捷发送: 协议组帧 + 串口发送 (config/quick_send.json)
QUICK_FILE = SKILL_DIR / "config" / "quick_send.json"
QUICK_BAK = SKILL_DIR / "config" / "quick_send.json.bak"

QUICK_DEFAULT = {
    "protocols": {
        "魏桥协议": {
            "desc": "7255 MCU-SOC UART 帧: {frame}; {len}, {sum}",
            "fields": [
                {"name": "SYNC", "len": 2, "value": "5A A5", "auto": "const"},
                {"name": "ACK", "len": 1, "value": "00"},
                {"name": "LEN", "len": 2, "role": "len", "from": "MODE", "to": "PARAM"},
                {"name": "MODE", "len": 1, "value": "00"},
                {"name": "CMD", "len": 2},
                {"name": "PARAM", "len": -1},
                {"name": "SUM", "len": 1, "role": "sum", "from": "ACK", "to": "PARAM", "alg": "sum_neg"},
            ],
        }
    },
    "groups": {"project": [], "other": []},
}

# 旧版兼容: subgroups -> children (任意层级递归分组)
#           len_plus/checksum -> role=len/sum + 字段区间(从字段A到字段B)


def _fw(f):
    """字段的固定字节宽度(变长字段按 0 计, 仅用于旧格式换算字节偏移)"""
    try:
        n = int(f.get("len", 1))
    except Exception:
        return 1
    return n if n > 0 else 0


def migrate_proto(p):
    """旧自动字段迁移为区间语义: len_plus -> role=len(+offset), checksum -> role=sum. 幂等"""
    if not isinstance(p, dict):
        return p
    fs = [f for f in (p.get("fields") or []) if isinstance(f, dict)]
    names = [f.get("name") for f in fs]
    varidx = None
    for i, f in enumerate(fs):
        if f.get("len") == -1:
            varidx = i
    for i, f in enumerate(fs):
        auto = f.get("auto")
        if f.get("role") or auto not in ("len_plus", "checksum"):
            continue
        if auto == "len_plus":
            plus = int(f.get("plus", 0) or 0)
            frm = to = ""
            offset = plus
            # 优先给一个好懂的区间: LEN 之后第一个字段 ~ 变长字段, 偏移扣掉中间静态字节
            if varidx is not None and varidx > i and names[i + 1]:
                seg = fs[i + 1:varidx + 1]
                s = sum(_fw(g) for g in seg if g.get("len") != -1)
                if s <= plus:
                    frm, to, offset = names[i + 1], names[varidx], plus - s
            if not frm and varidx is not None:
                frm = to = names[varidx]
            f["role"], f["from"], f["to"], f["offset"] = "len", frm, to, offset
            f.pop("plus", None)
            f.pop("auto", None)
        else:
            off = int((p.get("checksum") or {}).get("from", 0) or 0)
            acc, i0 = 0, 0
            for k, g in enumerate(fs[:i]):
                w = _fw(g)
                if acc <= off < acc + max(w, 1):
                    i0 = k
                    break
                acc += w
            i1 = i - 1 if i > 0 else 0
            if i1 < i0:
                i0 = i1
            f["role"], f["from"], f["to"] = "sum", names[i0], names[i1]
            f["len"] = 1          # 旧格式 checksum 固定写 1 字节
            f["alg"] = "sum_neg"  # 旧格式 checksum 就是「累加取反+1」
            f.pop("auto", None)
    # 已是 role=sum 但没写算法的(旧存量), 补默认
    for f in fs:
        if f.get("role") == "sum" and not f.get("alg"):
            f["alg"] = "sum_neg"
    p.pop("checksum", None)
    return p


def normalize_quick(data):
    def walk(ns):
        for n in ns or []:
            if not isinstance(n, dict):
                continue
            if "children" not in n and "subgroups" in n:
                n["children"] = n["subgroups"]
            n.pop("subgroups", None)
            n.setdefault("cmds", [])
            n.setdefault("children", [])
            walk(n["children"])
    for k in list((data.get("groups") or {}).keys()):
        walk(data["groups"][k])
    for k in list((data.get("protocols") or {}).keys()):
        migrate_proto(data["protocols"][k])
    return data


def load_quick():
    try:
        return normalize_quick(json.loads(QUICK_FILE.read_text(encoding="utf-8")))
    except Exception:
        return json.loads(json.dumps(QUICK_DEFAULT, ensure_ascii=False))


def save_quick(data):
    if not isinstance(data, dict) or "protocols" not in data or "groups" not in data:
        return False, "数据结构不合法(需 protocols+groups)"
    normalize_quick(data)
    QUICK_FILE.parent.mkdir(parents=True, exist_ok=True)
    # 写前把旧版快照到 .bak, 供「回退上一步」
    if QUICK_FILE.exists():
        try:
            QUICK_BAK.write_text(QUICK_FILE.read_text(encoding="utf-8"), encoding="utf-8")
        except Exception:
            pass
    QUICK_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return True, data


def _short(s, n=26):
    t = ("(空)" if s is None or s == "" else str(s)).replace("\n", " ").replace("\r", " ")
    return t if len(t) <= n else t[:n] + "…"


def _field_desc(f):
    parts = []
    L = f.get("len")
    parts.append("变长" if L == -1 else str(L) + "B")
    role = f.get("role")
    if role == "len":
        parts.append("LEN=" + str(f.get("from")) + ".." + str(f.get("to"))
                     + (("+" + str(f.get("offset"))) if f.get("offset") else ""))
    elif role == "sum":
        parts.append("SUM=" + str(f.get("from")) + ".." + str(f.get("to"))
                     + "(" + SUM_ALG_NAME.get(f.get("alg") or "sum_neg", "sum_neg") + ")")
    elif f.get("auto"):
        parts.append("auto=" + str(f["auto"])
                     + ("+" + str(f.get("plus", 0)) if f["auto"] == "len_plus" else ""))
    if f.get("value"):
        parts.append("默认 " + str(f["value"]))
    return ", ".join(parts)


def _proto_diff(name, cur, bak):
    """单协议逐字段比对(当前 -> 备份)"""
    out = []
    p = "协议「" + str(name) + "」"
    if (cur.get("desc") or "") != (bak.get("desc") or ""):
        out.append(p + "说明: " + _short(cur.get("desc")) + " → " + _short(bak.get("desc")))
    cc = {f.get("name"): f for f in (cur.get("fields") or []) if isinstance(f, dict)}
    bc = {f.get("name"): f for f in (bak.get("fields") or []) if isinstance(f, dict)}
    for fn, cf in cc.items():
        bf = bc.get(fn)
        if bf is None:
            out.append(p + "删除字段「" + str(fn) + "」(" + _field_desc(cf) + ")")
        elif cf != bf:
            out.append(p + "字段「" + str(fn) + "」: " + _field_desc(cf) + " → " + _field_desc(bf))
    for fn in bc:
        if fn not in cc:
            out.append(p + "恢复字段「" + str(fn) + "」(" + _field_desc(bc[fn]) + ")")
    return out


def _cmd_diff(path, cur, bak):
    """单指令逐字段比对(当前 -> 备份)"""
    out = []
    pre = "指令「" + str(path) + "」"
    cd, bd = cur.get("data"), bak.get("data")
    if (cur.get("mode"), cd) != (bak.get("mode"), bd):
        out.append(pre + "内容: " + _short(cd) + "(" + str(cur.get("mode") or "hex") + ")"
                   + " → " + _short(bd) + "(" + str(bak.get("mode") or "hex") + ")")
    cf = cur.get("fields") or {}
    bf = bak.get("fields") or {}
    for k in cf:
        if k not in bf:
            out.append(pre + "删除字段「" + str(k) + "」(值 " + _short(cf[k]) + ")")
        elif cf[k] != bf[k]:
            out.append(pre + "字段「" + str(k) + "」: " + _short(cf[k]) + " → " + _short(bf[k]))
    for k in bf:
        if k not in cf:
            out.append(pre + "恢复字段「" + str(k) + "」= " + _short(bf[k]))
    return out


def diff_quick(cur, bak):
    """以 当前 -> 备份 视角列差异(回退后发生什么), 逐项具体到字段/值"""
    items = []
    for k in cur.get("protocols", {}):
        if k not in bak.get("protocols", {}):
            items.append("删除协议「" + str(k) + "」(回退后不再存在, 其下 "
                         + str(len((cur["protocols"][k].get("fields") or []))) + " 个字段一并消失)")
        elif cur["protocols"][k] != bak["protocols"][k]:
            items += _proto_diff(k, cur["protocols"][k], bak["protocols"][k])
    for k in bak.get("protocols", {}):
        if k not in cur.get("protocols", {}):
            items.append("恢复协议「" + str(k) + "」(含 "
                         + str(len((bak["protocols"][k].get("fields") or []))) + " 个字段)")

    def walk(cnodes, bnodes, prefix):
        cmap = {n.get("name"): n for n in cnodes or [] if isinstance(n, dict)}
        bmap = {n.get("name"): n for n in bnodes or [] if isinstance(n, dict)}
        for name, cn in cmap.items():
            bn = bmap.get(name)
            path = "/".join(prefix + [str(name)])
            if bn is None:
                n_c = len(cn.get("cmds") or [])
                n_g = len(cn.get("children") or [])
                items.append("删除分组「" + path + "」(含 " + str(n_c) + " 条指令, "
                             + str(n_g) + " 个子分组)")
                continue
            if cn.get("protocol") != bn.get("protocol"):
                items.append("分组「" + path + "」协议绑定: " + str(cn.get("protocol") or "(无)")
                             + " → " + str(bn.get("protocol") or "(无)"))
            cc = {c.get("name"): c for c in cn.get("cmds") or [] if isinstance(c, dict)}
            bc = {c.get("name"): c for c in bn.get("cmds") or [] if isinstance(c, dict)}
            for n2 in cc:
                if n2 not in bc:
                    items.append("删除指令「" + path + "/" + str(n2) + "」")
                elif cc[n2] != bc[n2]:
                    items += _cmd_diff(path + "/" + str(n2), cc[n2], bc[n2])
            for n2 in bc:
                if n2 not in cc:
                    items.append("恢复指令「" + path + "/" + str(n2) + "」")
            walk(cn.get("children"), bn.get("children"), prefix + [str(name)])
        for name, bn in bmap.items():
            if name not in cmap:
                items.append("恢复分组「" + "/".join(prefix + [str(name)]) + "」(含 "
                             + str(len(bn.get("cmds") or [])) + " 条指令)")

    for sec in ("project", "other"):
        walk(cur.get("groups", {}).get(sec), bak.get("groups", {}).get(sec), [sec])

    if not items:
        items = ["无差异(当前配置与备份相同) — 回退不会改变任何内容"]
    return items[:15] + (["…等共 %d 项差异" % len(items)] if len(items) > 15 else [])


def quick_backup():
    """读取 .bak 并生成与当前的差异摘要"""
    if not QUICK_BAK.exists():
        return {"ok": False, "msg": "还没有备份(第一次保存配置后才有)"}
    try:
        bak = normalize_quick(json.loads(QUICK_BAK.read_text(encoding="utf-8")))
    except Exception as e:
        return {"ok": False, "msg": "备份文件损坏: %s" % e}
    return {"ok": True,
            "bak_time": QUICK_BAK.stat().st_mtime,
            "diff": diff_quick(load_quick(), bak)}


def quick_restore():
    """回退 = 当前与备份交换(可再次回退撤销)"""
    if not QUICK_BAK.exists():
        return False, "没有可回退的备份"
    try:
        bak = normalize_quick(json.loads(QUICK_BAK.read_text(encoding="utf-8")))
    except Exception as e:
        return False, "备份文件损坏: %s" % e
    cur_text = QUICK_FILE.read_text(encoding="utf-8") if QUICK_FILE.exists() else None
    QUICK_FILE.write_text(json.dumps(bak, ensure_ascii=False, indent=2), encoding="utf-8")
    if cur_text is not None:
        QUICK_BAK.write_text(cur_text, encoding="utf-8")
    return True, bak


def parse_hex(s):
    s = (s or "").replace(" ", "").replace(",", "").replace("0x", "")
    if len(s) % 2:
        raise ValueError("hex 长度为奇数")
    return bytes.fromhex(s)


# SUM 校验算法(alg): sum_neg=累加取反+1(默认,现有协议用这个) / sum=累加和 / xor=逐字节异或
SUM_ALGS = ("sum_neg", "sum", "xor")
SUM_ALG_NAME = {"sum_neg": "累加取反+1", "sum": "累加和", "xor": "逐字节异或"}


def sum_calc(alg, seg, n):
    """按算法算校验值, 结果按 n 字节大端"""
    if alg == "xor":
        v = 0
        for b in seg:
            v ^= b
    elif alg == "sum":
        v = sum(seg)
    else:                     # sum_neg: 累加后取反+1(二补), 等价 (-sum)&0xFF
        v = -sum(seg)
    return (v & ((1 << (8 * n)) - 1)).to_bytes(n, "big")


def build_frame(proto, fields):
    """按协议字段表组帧.
    每字段二选一:
      手填  -> 用发指令时输入的 fields[名], 空则用协议默认 value
      const -> 固定用协议 value
    另可标记自动字段(role):
      role=len -> 值为「from..to 区间的实际字节数 + offset」, 按 len 字节大端写
      role=sum -> 值为「from..to 区间的校验值」, 算法见 alg(默认 sum_neg), 按 len 字节大端写
    区间按字段表从前往后取, from/to 都是字段名."""
    fields = fields or {}
    fl = [f for f in proto.get("fields", []) if isinstance(f, dict)]
    idx = {}
    for i, f in enumerate(fl):
        nm = str(f.get("name"))
        if nm not in idx:
            idx[nm] = i

    def raw_val(f):
        return (fields.get(f["name"]) or f.get("value") or "").strip()

    # 先定每字段字节数, 用于区间定位(自动字段按声明的 len 计)
    size = []
    for f in fl:
        if f.get("role") in ("len", "sum"):
            size.append(max(int(f.get("len", 1) or 1), 1))
        elif f.get("auto") == "const":
            size.append(len(parse_hex(f.get("value", ""))))
        else:
            size.append(len(parse_hex(raw_val(f))))

    def region(f):
        i0 = idx.get(str(f.get("from")))
        i1 = idx.get(str(f.get("to")))
        if i0 is None or i1 is None or i1 < i0:
            return None
        return i0, i1

    out = bytearray()
    for f in fl:
        role = f.get("role")
        if role == "len":
            rg = region(f)
            n = 0 if rg is None else sum(size[rg[0]:rg[1] + 1])
            v = max(n + int(f.get("offset", 0) or 0), 0)
            out += v.to_bytes(max(int(f.get("len", 1) or 1), 1), "big")
        elif role == "sum":
            rg = region(f)
            n = max(int(f.get("len", 1) or 1), 1)
            if rg is None:
                out += bytes(n)
            else:
                seg = out[sum(size[:rg[0]]):sum(size[:rg[1] + 1])]
                out += sum_calc(f.get("alg") or "sum_neg", seg, n)
        elif f.get("auto") == "const":
            out += parse_hex(f.get("value", ""))
        else:
            out += parse_hex(raw_val(f))
    return bytes(out)


def do_send_data(mode, data, crlf):
    ser = conn["ser"]
    if ser is None or not getattr(ser, "is_open", False):
        return False, "未连接串口, 请先在上方点\"连接\"", 0, ""
    try:
        if mode == "hex":
            b = parse_hex(data)
        else:
            b = (data or "").encode("utf-8", errors="replace")
        if crlf:
            b += b"\r\n"
        n = ser.write(b)
        try:
            ser.flush()
        except Exception:
            pass
        return True, "", n, " ".join(f"{x:02X}" for x in b)
    except ValueError as e:
        return False, f"HEX 格式错误: {e}", 0, ""
    except Exception as e:
        return False, str(e), 0, ""


def main():
    global REPLAY_TAIL
    cfg = load_config()
    ap = argparse.ArgumentParser(description="Web 实时串口监视器")
    ap.add_argument("--port", default="",
                    help="(可选)仅作启动后预选串口; 不传则在网页下拉选择")
    ap.add_argument("--baud", type=int, default=int(cfg.get("baud") or 921600),
                    help="(可选)网页波特率输入框的默认值")
    ap.add_argument("--web-port", type=int, default=8765, help="Web 端口, 默认 8765")
    ap.add_argument("--replay-tail", type=int, default=None,
                    help="网页刷新/首开时只回放最近 N 行(默认 200); <=0 表示回放全部")
    ap.add_argument("--confirm", action="store_true",
                    help="门禁: 必须已向用户确认采集意图后才可启动")
    ap.add_argument("--no-browser", action="store_true", help="不自动打开浏览器")
    args = ap.parse_args()

    if args.replay_tail is not None:
        REPLAY_TAIL = args.replay_tail

    if not args.confirm:
        print("拒绝启动: 未确认采集意图。", file=sys.stderr)
        print("AI 必须先向用户确认【1.模式(实时查看/后台写入) 2.日志输出位置】两项,", file=sys.stderr)
        print("用户明确答复后, 才允许带 --confirm 参数重启本命令。", file=sys.stderr)
        sys.exit(1)

    # 启动只起 Web 服务, 不打开串口; 串口/波特率/检测全部由网页操作
    conn["preset"] = (args.port or "").strip()

    srv = ThreadingHTTPServer(("0.0.0.0", args.web_port), Handler)
    url = f"http://localhost:{args.web_port}"
    print(f"监视器已启动: {url}")
    print(f"串口操作请在网页进行(下拉选串口 / 填波特率 / 自动检测 / 连接)")
    _imgs = list_assets()
    print(f"背景素材: {ASSETS_DIR} ({'加载 ' + _imgs[0] if _imgs else '为空, 放图片进该目录即可换背景'})")
    print(f"统计接口: {url}/stats", flush=True)
    if not args.no_browser:
        import webbrowser
        threading.Thread(target=lambda: (time.sleep(0.8), webbrowser.open(url)),
                         daemon=True).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        srv.server_close()
        with lock:
            ser = conn["ser"]
        if ser is not None:
            try:
                ser.close()
            except Exception:
                pass
        if conn["err"]:
            print(f"[异常] {conn['err']}", file=sys.stderr)
        print("\n停止(未保存, 如需留档请在网页点'保存日志'后停止)")


if __name__ == "__main__":
    main()
