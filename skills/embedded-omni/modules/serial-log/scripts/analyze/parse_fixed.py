#!/usr/bin/env python3
"""固定格式串口日志解析统计（DAB_BOX 格式）。

格式(level 全称): [timestamp][DEBUG|INFO|WARN|ERROR][file:line] [module] message
兼容: 旧格式无 level 字段 / 旧缩写 [D][I][W][E]

用法:
  python parse_fixed.py <log文件>
  python parse_fixed.py <log文件> --min-level WARN
  python parse_fixed.py <log文件> --module COM IAP
  python parse_fixed.py <log文件> --errors-only
  python parse_fixed.py <log文件> --report report.md
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

LOG_RE = re.compile(
    r"^\[(\d+)\](?:\[(DEBUG|INFO|WARN|ERROR|D|I|W|E)\])?\[([^\]:]+):(\d+)\]\s*\[([^\]]+)\]\s?(.*)$"
)
DROP_RE = re.compile(r"drop_cnt\s*=\s*(\d+)")
# 落盘行首主机时间戳(采集/Web保存时拼接): 解析前剥掉
HOST_TS_RE = re.compile(r"^\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}\]\s?")

# 归一化: 缩写 -> 全称
LEVEL_ALIAS = {"D": "DEBUG", "I": "INFO", "W": "WARN", "E": "ERROR",
               "DEBUG": "DEBUG", "INFO": "INFO", "WARN": "WARN", "ERROR": "ERROR"}
LEVEL_ORDER = {"DEBUG": 0, "INFO": 1, "WARN": 2, "ERROR": 3}
LEVEL_ABBR = {"DEBUG": "D", "INFO": "I", "WARN": "W", "ERROR": "E"}


def parse(path, min_level=None, modules=None):
    stats = {
        "total": 0,          # 总行数
        "parsed": 0,         # 固定格式解析成功
        "legacy": 0,         # 旧格式（无 level）
        "unparsed": 0,       # 无法解析
        "levels": Counter(), # level 分布（含 N/A）
        "modules": Counter(),
        "hotspots": Counter(),  # WARN/ERROR 的 file:line 计数
        "warn_err": [],         # WARN/ERROR 明细 [(ts, lvl, file, line, module, msg)]
        "drop_lines": [],       # drop_cnt 行
        "ts_min": None,
        "ts_max": None,
        "unparsed_samples": [],
    }
    path = Path(path)
    if not path.exists():
        print(f"错误: 文件不存在 {path}", file=sys.stderr)
        sys.exit(1)

    with open(path, "rb") as f:
        for raw in f:
            stats["total"] += 1
            line = raw.decode("utf-8", errors="replace").rstrip("\r\n")
            line = HOST_TS_RE.sub("", line, count=1)
            if not line.strip():
                continue
            m = LOG_RE.match(line)
            if not m:
                stats["unparsed"] += 1
                if len(stats["unparsed_samples"]) < 5:
                    stats["unparsed_samples"].append(line[:120])
                continue

            ts, lvl, file, lineno, module, msg = m.groups()
            ts = int(ts)
            stats["ts_min"] = ts if stats["ts_min"] is None else min(stats["ts_min"], ts)
            stats["ts_max"] = ts if stats["ts_max"] is None else max(stats["ts_max"], ts)

            if lvl is None:
                stats["legacy"] += 1
                lvl_key = "N/A"
            else:
                lvl_key = LEVEL_ALIAS[lvl]  # 归一化为全称
            stats["parsed"] += 1

            # 过滤
            if min_level is not None:
                if lvl_key == "N/A":
                    continue
                if LEVEL_ORDER[lvl_key] < min_level:
                    continue
            if modules and module not in modules:
                continue

            stats["levels"][lvl_key] += 1
            stats["modules"][module] += 1

            dm = DROP_RE.search(msg)
            if dm:
                stats["drop_lines"].append((ts, int(dm.group(1))))

            if lvl_key in ("WARN", "ERROR"):
                stats["hotspots"][f"{file}:{lineno}"] += 1
                if len(stats["warn_err"]) < 10000:
                    stats["warn_err"].append((ts, lvl_key, file, lineno, module, msg))
    return stats


def fmt_report(stats, path, errors_only=False):
    lines = []
    ap = lines.append
    ap(f"# 串口日志分析报告")
    ap("")
    ap(f"- 文件: `{path}`")
    if stats["ts_min"] is not None:
        span = stats["ts_max"] - stats["ts_min"]
        ap(f"- 时间戳范围: {stats['ts_min']} ~ {stats['ts_max']} (跨度 {span} ms)")
    ap(f"- 总行数: {stats['total']}  解析成功: {stats['parsed']}  无法解析: {stats['unparsed']}")
    ap("")

    if stats["unparsed"] > 0:
        ap("## 无法解析的行（前5条样本）")
        ap("")
        ap("```")
        for s in stats["unparsed_samples"]:
            ap(s)
        ap("```")
        ap("")

    if errors_only:
        ap("## WARN/ERROR 明细")
        ap("")
        if not stats["warn_err"]:
            ap("无")
        else:
            ap("```")
            for ts, lvl, file, lineno, module, msg in stats["warn_err"][:200]:
                ap(f"[{ts}][{lvl}][{file}:{lineno}] [{module}] {msg}")
            if len(stats["warn_err"]) > 200:
                ap(f"... 共 {len(stats['warn_err'])} 条, 仅显示前 200 条")
            ap("```")
        return "\n".join(lines)

    ap("## Level 分布")
    ap("")
    ap("| level | 条数 |")
    ap("|-------|------|")
    for lvl in ("DEBUG", "INFO", "WARN", "ERROR", "N/A"):
        cnt = stats["levels"].get(lvl, 0)
        if cnt:
            ap(f"| {lvl}{' (旧格式无level)' if lvl == 'N/A' else ''} | {cnt} |")
    ap("")

    ap("## 模块分布")
    ap("")
    ap("| module | 条数 |")
    ap("|--------|------|")
    for mod, cnt in stats["modules"].most_common():
        ap(f"| {mod} | {cnt} |")
    ap("")

    ap("## WARN/ERROR 热点 top10")
    ap("")
    if stats["hotspots"]:
        ap("| 位置 | 次数 |")
        ap("|------|------|")
        for loc, cnt in stats["hotspots"].most_common(10):
            ap(f"| {loc} | {cnt} |")
    else:
        ap("无 WARN/ERROR")
    ap("")

    ap("## drop counter")
    ap("")
    if stats["drop_lines"]:
        for ts, cnt in stats["drop_lines"][-10:]:
            ap(f"- [{ts}ms] drop_cnt={cnt}")
        ap("")
        ap(f"日志共出现 {len(stats['drop_lines'])} 次 drop 上报, 固件有日志被丢弃, 检查锁竞争/波特率")
    else:
        ap("无 drop_cnt 上报")
    ap("")

    ap("## WARN/ERROR 明细（前50条）")
    ap("")
    if stats["warn_err"]:
        ap("```")
        for ts, lvl, file, lineno, module, msg in stats["warn_err"][:50]:
            ap(f"[{ts}][{lvl}][{file}:{lineno}] [{module}] {msg}")
        ap("```")
    else:
        ap("无")
    return "\n".join(lines)


def main():
    ap_ = argparse.ArgumentParser(description="固定格式串口日志解析统计")
    ap_.add_argument("log", help="日志文件路径")
    ap_.add_argument("--min-level", choices=["DEBUG", "INFO", "WARN", "ERROR", "D", "I", "W", "E"],
                     help="最低级别过滤(全称或缩写)")
    ap_.add_argument("--module", nargs="+", help="只统计指定模块, 如 --module COM IAP")
    ap_.add_argument("--errors-only", action="store_true", help="只输出 WARN/ERROR 明细")
    ap_.add_argument("--report", help="报告输出到文件(默认打印到屏幕)")
    ap_.add_argument("--json-out", help="统计结果输出为 JSON(供 gen_report/AI 使用)")
    args = ap_.parse_args()

    min_level = LEVEL_ORDER[LEVEL_ALIAS[args.min_level]] if args.min_level else None
    stats = parse(args.log, min_level, set(args.module) if args.module else None)
    report = fmt_report(stats, args.log, args.errors_only)

    if args.report:
        Path(args.report).write_text(report, encoding="utf-8")
        print(f"报告已写入: {args.report}")
    else:
        print(report)

    if args.json_out:
        payload = {
            "file": str(args.log),
            "total": stats["total"], "parsed": stats["parsed"], "unparsed": stats["unparsed"],
            "levels": dict(stats["levels"]),
            "modules": dict(stats["modules"]),
            "hotspots": dict(stats["hotspots"]),
            "warn_err": [
                {"ts": t, "level": l, "file": f, "line": n, "module": m, "msg": s}
                for t, l, f, n, m, s in stats["warn_err"]
            ],
            "drop_lines": [list(d) for d in stats["drop_lines"]],
            "ts_min": stats["ts_min"], "ts_max": stats["ts_max"],
        }
        Path(args.json_out).write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"统计JSON已写入: {args.json_out}")


if __name__ == "__main__":
    main()
