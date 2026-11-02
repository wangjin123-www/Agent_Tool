#!/usr/bin/env python3
"""查 COM 口被哪个进程占用, 可选结束占用进程。

判定顺序(以"真被占用"为准, 杜绝按进程名瞎报):
  1. Sysinternals handle64.exe (util/ 目录) 按注册表映射的 NT 设备名搜句柄 -> 真凶(精确, 无副作用)
  2. 句柄查不到时, 用 pyserial 独占打开做金标准判定:
       能打开   -> 串口未被占用(直接下结论, 不再拿进程名瞎猜)
       打开被拒 -> 真被占, 只是没定位到持有进程
      (--no-probe 可跳过, 纯句柄模式)
  3. 仅在"打开被拒且句柄查不到"时, 才把进程名匹配常见串口工具的进程列为
     **未验证参考**(明确标注不一定是它), 绝不再当成占用者

用法:
  python find_com_holder.py COM6              # 查占用(句柄优先)
  python find_com_holder.py COM6 --kill       # 结束查到的真凶(只杀句柄命中的)
  python find_com_holder.py COM6 --no-probe   # 跳过打开测试, 纯句柄查询
"""
import argparse
import re
import subprocess
from pathlib import Path

UTIL_DIR = Path(__file__).resolve().parent.parent.parent / "util"   # scripts/common/ -> skill 根/util

# 常见会占串口的进程名关键词(只作"未验证参考", 不构成占用结论)
KNOWN_HOLDERS = [
    "串口", "uartassist", "uart", "sscom", "xcom", "putty", "securecrt",
    "vofa", "mobaxterm", "data center", "totalphase", "firetool",
    "comassistant", "serialport", "serial_debug", "ttyterm", "tera term",
]


def list_processes():
    """返回 [(pid, name, cmdline)], 用 CIM 拿命令行, 拿不到则退回空表。"""
    procs = []
    try:
        r = subprocess.run(
            ["powershell", "-NoProfile", "-Command",
             "Get-CimInstance Win32_Process | Select-Object ProcessId,Name,CommandLine | "
             "ConvertTo-Csv -NoTypeInformation"],
            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60,
        )
        import csv, io
        for row in csv.DictReader(io.StringIO(r.stdout)):
            try:
                procs.append((int(row["ProcessId"]), row["Name"] or "", row["CommandLine"] or ""))
            except (ValueError, KeyError):
                continue
    except Exception:
        pass
    return procs


def find_by_name():
    """按进程名关键词匹配常见串口工具, 返回 [(pid, name, cmdline)]。
    注意: 这是**未验证参考**, 命中不等于它占用了串口。"""
    hits = []
    for pid, name, cmdline in list_processes():
        low = name.lower()
        if any(k in low for k in KNOWN_HOLDERS):
            hits.append((pid, name, cmdline))
    return hits


def com_to_nt_name(com):
    """COMx -> NT 设备名末段(如 Serial19/VCP0), 读注册表 SERIALCOMM 映射。"""
    try:
        import winreg
    except ImportError:
        return None
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DEVICEMAP\SERIALCOMM")
    except OSError:
        return None
    try:
        i = 0
        while True:
            try:
                nt_name, com_name, _ = winreg.EnumValue(key, i)
            except OSError:
                return None
            if com_name.upper() == com.upper():
                return nt_name.rsplit("\\", 1)[-1]
            i += 1
    finally:
        winreg.CloseKey(key)


def find_by_handle(com):
    """用 handle64.exe 按设备名搜句柄(精确, 首次运行自动接受 EULA)。
    返回 [(pid, name)]; 工具缺失/权限不足/超时 -> 空表。"""
    exe = None
    for name in ("handle64.exe", "handle.exe", "handle64a.exe"):
        p = UTIL_DIR / name
        if p.exists():
            exe = p
            break
    if exe is None:
        return []
    nt_name = com_to_nt_name(com)
    if not nt_name:
        return []
    try:
        r = subprocess.run(
            [str(exe), "-accepteula", "-nobanner", "-a", nt_name],
            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=90,
        )
    except (subprocess.TimeoutExpired, OSError):
        return []
    holders = []
    seen = set()
    for ln in r.stdout.splitlines():
        m = re.match(r"^(.+?)\s+pid:\s*(\d+)\s+type:\s*File.*Device", ln)
        if m:
            pid = int(m.group(2))
            if pid not in seen:
                seen.add(pid)
                holders.append((pid, m.group(1).strip()))
    return holders


def com_exists(com):
    """用 pyserial 端口列表判断串口是否存在; 无法判断返回 None。"""
    try:
        import serial.tools.list_ports as lp
    except ImportError:
        return None
    for p in lp.comports():
        if (p.device or "").upper() == com.upper():
            return True
    return False


def port_probe(com):
    """独占打开串口做金标准判定(打开即关, 不读数据)。
    返回 (state, detail): 'free'(未被占用) / 'busy'(被占用) / 'missing'(不存在) / 'unknown'。"""
    try:
        import serial
    except ImportError:
        return "unknown", "缺少 pyserial, 无法做打开测试"
    if com_exists(com) is False:
        return "missing", "系统中不存在该串口"
    try:
        s = serial.Serial(com, 9600, timeout=0.05)
        s.close()
        return "free", "可独占打开"
    except Exception as e:
        msg = str(e)
        low = msg.lower()
        if "permissionerror" in low or "拒绝访问" in msg or "access is denied" in low:
            return "busy", "打开被拒(已被占用)"
        return "unknown", msg


def kill_holders(holders):
    for pid, name in holders:
        r = subprocess.run(["taskkill", "/F", "/PID", str(pid)],
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        print(f"  {'已结束' if r.returncode == 0 else '结束失败'}: {name} (pid {pid})")


def main():
    ap = argparse.ArgumentParser(description="查/杀 COM 口占用进程(句柄优先, 不按进程名瞎报)")
    ap.add_argument("com", help="串口号, 如 COM6")
    ap.add_argument("--kill", action="store_true", help="结束查到的真凶(仅句柄命中的进程)")
    ap.add_argument("--no-probe", action="store_true", help="跳过串口打开测试(纯句柄模式, 无任何副作用)")
    args = ap.parse_args()

    # 第一层: 句柄查询, 精确且无副作用
    exact = find_by_handle(args.com)
    if exact:
        print(f"{args.com} 被以下进程占用(句柄精确命中):")
        for pid, name in exact:
            print(f"  {name} (pid {pid})")
        if args.kill:
            kill_holders(exact)
        else:
            print("加 --kill 可结束占用进程")
        return

    # 第二层: 句柄查不到 -> 用打开测试判定"到底有没有被占", 不猜进程名
    if not args.no_probe:
        state, detail = port_probe(args.com)
        if state == "free":
            print(f"{args.com}: 未被占用({detail})。句柄查询未发现持有进程。")
            return
        if state == "missing":
            print(f"{args.com}: {detail}(检查是否插好线 / COM号是否因拔插变了)")
            return
        reason = detail
    else:
        reason = "已跳过打开测试"

    # 第三层: 真被占但没定位到持有进程 -> 进程名匹配仅作未验证参考
    print(f"{args.com}: 未能定位到具体持有进程({reason})。")
    suspects = find_by_name()
    if suspects:
        print("  以下进程名匹配常见串口工具, 仅供参考(未验证句柄, 不一定是它):")
        for pid, name, cmdline in suspects:
            extra = f"  <- {cmdline[:80]}" if cmdline else ""
            print(f"    {name} (pid {pid}){extra}")
    else:
        print("  可能原因: handle64 需管理员权限运行 / 占用进程不在已知进程名列表 / 串口驱动异常")


if __name__ == "__main__":
    main()
