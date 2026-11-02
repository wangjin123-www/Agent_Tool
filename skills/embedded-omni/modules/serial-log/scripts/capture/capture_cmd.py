#!/usr/bin/env python3
"""采集控制工具: 向正在运行的 capture_serial.py 下指令(不改动采集进程本身)。

关键语义(用户强调, 违反=事故):
  mail  -> 只发"当前快照"邮件, 采集**继续**, 绝不停止采集
  stop  -> 正常停止采集(采集进程会统计+归档主 log 到 logs/完成采集/<名>_结束<时刻>.log)
  status-> 查看采集是否在跑 / 最后状态(不打断)

用法:
  python capture_cmd.py <log路径或.ctl目录> mail [备注] \\
      [--analysis-mode fixed|free|auto] [--depth low|medium|high] [--focus 正则] [--project 编号|路径]
  python capture_cmd.py <log路径或.ctl目录> stop [备注]
  python capture_cmd.py <log路径或.ctl目录> status
  python capture_cmd.py --list                # 列出所有当前在采集的任务

--analysis-mode / --depth / --focus / --project: 本次邮件正文的分析方式/强度/特殊要求/关联工程(见 references/)。
  人工触发(手动停止/中途中发)时, AI 必须先问用户这几项再传进来;
  不传则用采集进程启动时的默认(启动参数里的 --analysis-mode/--analysis-depth/--project)。
  --project 不传: 用 config [projects] 的 default; 也没有则 AI 必须问用户,
  用户不回答 -> 本次分析结果与结论都不关联工程代码。
  铁律: 有 --focus(特殊要求) 时严格按用户要求分析, --depth 不生效, 也不用问强度。
"""
import json
import os
import re
import sys
import time
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent.parent   # scripts/capture/ -> skill 根
CONFIG_FILE = SKILL_DIR / "config" / "config.conf"


def load_log_dir():
    """读 config [log] 段的 dir 作为 log 根目录; 文件不在/没配/配空 -> 默认 <skill>/output/logs。
    与 capture_serial.load_log_dir 同逻辑(本脚本不 import capture_serial, 避免拉起 pyserial 依赖)。"""
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
CTL_DIR = LOG_DIR / "ctl"   # 控制目录统一收在 logs/ctl/(与 capture_serial.ctl_dir_for 一致)


def resolve_ctl(arg):
    """把用户给的 log 路径 / ctl 目录 / 日志名 归一为 ctl 目录。
    新约定: 控制目录统一在 logs/ctl/<log名>.ctl; 兼容旧的 <log同目录>/<log名>.ctl。"""
    p = Path(arg)
    if p.suffix == ".ctl":
        return p
    cand = CTL_DIR / (p.stem + ".ctl")
    if cand.exists():
        return cand
    sib = p.with_name(p.stem + ".ctl")
    return sib if sib.exists() else cand


def pid_alive(pid):
    if not pid:
        return False
    if sys.platform == "win32":
        import ctypes
        h = ctypes.windll.kernel32.OpenProcess(0x1000, False, int(pid))
        if not h:
            return False
        code = ctypes.c_ulong()
        ok = ctypes.windll.kernel32.GetExitCodeProcess(h, ctypes.byref(code))
        ctypes.windll.kernel32.CloseHandle(h)
        return bool(ok) and code.value == 259
    try:
        os.kill(int(pid), 0)
        return True
    except (OSError, ProcessLookupError):
        return False


def read_status(ctl):
    f = ctl / "status.json"
    if not f.exists():
        return None
    try:
        return json.loads(f.read_text(encoding="utf-8"))
    except Exception:
        return None


def find_active():
    """扫描 logs/ctl/*.ctl(兼容旧 logs/*.ctl), 返回还在采集的 [(ctl目录, status)]。"""
    out = []
    cands = []
    if CTL_DIR.exists():
        cands += sorted(CTL_DIR.glob("*.ctl"))
    if LOG_DIR.exists():
        cands += sorted(LOG_DIR.glob("*.ctl"))
    for ctl in cands:
        st = read_status(ctl)
        if st and st.get("state") == "RUNNING" and pid_alive(st.get("pid")):
            out.append((ctl, st))
    return out


def parse_opt(args, name, choices=None):
    """从参数列表取 --name value; 不存在返回 None。choices 非空时校验。"""
    if name in args:
        i = args.index(name)
        if i + 1 >= len(args):
            print(f"错误: {name} 缺参数值", file=sys.stderr)
            sys.exit(1)
        v = args[i + 1]
        if choices and v not in choices:
            print(f"错误: {name} 只能是 {'/'.join(choices)}", file=sys.stderr)
            sys.exit(1)
        return v
    return None


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("--list", "-l"):
        act = find_active()
        if not act:
            print("当前没有正在进行的后台采集")
            return 0
        print(f"正在采集 {len(act)} 个任务:")
        for ctl, st in act:
            hb = time.time() - float(st.get("heartbeat", 0))
            print(f"  {st.get('log')}")
            print(f"    {st.get('port')}@{st.get('baud')} pid={st.get('pid')} "
                  f"行={st.get('lines')} WARN={st.get('warn')} ERROR={st.get('error')} "
                  f"心跳={hb:.0f}s前")
        return 0

    # 抽出选项后, 剩余作为 <路径> <指令> [备注]
    a_mode = parse_opt(args, "--analysis-mode", ["fixed", "free", "auto"])
    a_depth = parse_opt(args, "--depth", ["low", "medium", "high"])
    a_focus = parse_opt(args, "--focus")
    a_project = parse_opt(args, "--project")
    if a_focus is not None:
        try:
            re.compile(a_focus)
        except re.error as e:
            print(f"错误: --focus 正则非法: {e}", file=sys.stderr)
            return 1
        # 铁律: 有特殊要求时严格按用户要求分析, 强度不参与
        if a_depth:
            print("[提示] 已给 --focus(特殊要求): 按你的要求严格分析, --depth 不生效(已忽略)")
            a_depth = None
    skip = set()
    for name in ("--analysis-mode", "--depth", "--focus", "--project"):
        if name in args:
            i = args.index(name)
            skip.update({i, i + 1})
    rest = [v for i, v in enumerate(args) if i not in skip]

    if len(rest) < 2:
        print("用法: python capture_cmd.py <log路径|.ctl目录> mail|stop|status [备注] "
              "[--analysis-mode fixed|free|auto] [--depth low|medium|high] [--focus 正则] "
              "[--project 编号|工程路径]",
              file=sys.stderr)
        return 1

    ctl = resolve_ctl(rest[0])
    cmd = rest[1].lower()
    note = rest[2] if len(rest) > 2 else ""

    st = read_status(ctl)
    if st is None:
        print(f"错误: 找不到状态文件 {ctl / 'status.json'} (路径不对, 或采集未启动)", file=sys.stderr)
        return 1

    state = st.get("state")
    if cmd == "status":
        alive = pid_alive(st.get("pid"))
        print(json.dumps(st, ensure_ascii=False, indent=2))
        print(f"进程存活: {alive}")
        if state == "RUNNING" and not alive:
            print("!!! 状态=RUNNING 但进程已消失: 异常中断, 看门狗应已备份并发邮件, 请查 watchdog_events.log")
        return 0

    if state != "RUNNING" or not pid_alive(st.get("pid")):
        print(f"错误: 当前没有在运行的采集(state={state}, pid={st.get('pid')}, "
              f"存活={pid_alive(st.get('pid'))})", file=sys.stderr)
        return 1

    if cmd not in ("mail", "stop"):
        print("错误: 指令只能是 mail 或 stop", file=sys.stderr)
        return 1

    ctl.mkdir(parents=True, exist_ok=True)
    payload = {"cmd": cmd, "note": note, "ts": time.time()}
    if a_mode:
        payload["analysis_mode"] = a_mode
    if a_depth:
        payload["depth"] = a_depth
    if a_focus is not None:
        payload["focus"] = a_focus
    if a_project:
        payload["project"] = a_project
    tmp = ctl / "cmd.json.tmp"
    tmp.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
    tmp.replace(ctl / "cmd.json")

    ana = []
    if a_mode:
        ana.append(f"方式={a_mode}")
    if a_project:
        ana.append(f"工程={a_project}")
    if a_focus:
        ana.append(f"特殊要求=/{a_focus}/(严格按此分析, 强度不生效)")
    elif a_depth:
        ana.append(f"强度={a_depth}")
    ana_desc = ("  本次分析: " + " ".join(ana)) if ana else "  本次分析: 用启动时默认"

    if cmd == "mail":
        print("已请求发送快照邮件: 采集继续运行, 不会停止")
        print(ana_desc)
        print(f"[提示] 邮件正文含: 行={st.get('lines')} WARN={st.get('warn')} ERROR={st.get('error')}")
    else:
        print("已请求停止采集: 采集进程会统计 WARN/ERROR 并归档到 logs/完成采集/")
        print("停止后如需邮件: AI 会先用 analyze_log.py 对备份 log 出分析, 再问你是否发送")
    return 0


if __name__ == "__main__":
    sys.exit(main())
