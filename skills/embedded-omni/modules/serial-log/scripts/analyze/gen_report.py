#!/usr/bin/env python3
"""生成带分析的 HTML 日志报告(邮件附件)。

输入: log 文件 + analyze_log.py 的结构化结果(--analysis), 可选 stats.json
输出: report_时间戳.html

--analysis 接受两种 JSON:
  A. analyze_log.py 的输出(推荐): 自动据此生成结论文字 + 逐行 WARN/ERROR 分析块
  B. 旧式 {"summary": "...", "by_line": {"行前缀": "分析"}}   (兼容, summary 优先)

报告特性: level 颜色区分(DEBUG灰/INFO绿/WARN橙/ERROR红)、浏览器 Ctrl+F 检索、
         每条 WARN/ERROR 后面紧跟黄色分析块、顶部统计+结论。
         全量逐行输出(万行级照常, 不做截断, 供人工检索)。

用法:
  python gen_report.py <log文件> --analysis analysis.json [--stats stats.json] [--out report.html]
"""
import argparse
import html
import json
import re
import sys
from datetime import datetime
from pathlib import Path

# 与 serial_monitor.py 保持一致的级别推断
LEVEL_RULES = [
    (r"HardFault|CmBacktrace|ASSERT|assert", "ERROR"),
    (r"ERR_BUF_FULL|ERR_DISCONN", "ERROR"),
    (r"DTC_|FAULT DETECTED", "ERROR"),
    (r"SendWithAck FAILED", "ERROR"),
    (r"ERROR|ERR_|error|fail|FAIL", "ERROR"),
    (r"retry|RETRY|timeout|TIMEOUT|Timeout", "WARN"),
    (r"\[W\]|WARN", "WARN"),
]
LEVEL_MAP = {"DEBUG": "DEBUG", "INFO": "INFO", "WARN": "WARN", "ERROR": "ERROR",
             "D": "DEBUG", "I": "INFO", "W": "WARN", "E": "ERROR"}
FIELD_RE = re.compile(r"^\[\d+\]\[([A-Za-z]+)\]")
# 落盘行首主机时间戳: 匹配/统计前剥掉, 展示时保留
HOST_TS_RE = re.compile(r"^\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}\]\s?")


def classify(text):
    m = FIELD_RE.match(text)
    if m and m.group(1).upper() in LEVEL_MAP:
        return LEVEL_MAP[m.group(1).upper()]
    for pattern, level in LEVEL_RULES:
        if re.search(pattern, text):
            return level
    return "INFO"


def line_key(text):
    """去掉时间戳后的前80字符, 作为与 analysis.json 匹配的 key。"""
    t = re.sub(r"^\[\d+\]", "", text)
    return t[:80].strip()


def shape_key(text):
    """与 analyze_log.normalize_shape 一致的消息形状 key(去时间戳/hex/数字)。"""
    t = re.sub(r"^\[\d+\]", "", text)
    t = re.sub(r"0x[0-9a-fA-F]+", "0xH", t)
    t = re.sub(r"\b\d+\b", "N", t)
    return re.sub(r"\s+", " ", t).strip()[:120]


def summarize(struct):
    """据 analyze_log.py 结果自动生成结论文字(无需 AI 参与)。
    结论口径与 analyze_log.fmt_md 的"== 结论 =="段一致: 先给工程关联 + 人话结论, 再给代码证据。"""
    mode_cn = {"fixed": "固定格式分析(module / level / 内容聚合)",
               "free": "自由格式分析(消息形状去重 + 关键词分级)"}.get(
        struct.get("mode", ""), "分析")
    L = [f"分析方式: {mode_cn}"]
    if struct.get("mode_requested") == "auto":
        L.append(f"(自动判定: 固定格式占比 {struct.get('fixed_ratio', 0):.0%})")
    if struct.get("focus_override"):
        L.append("分析强度: 不适用(已按特殊要求执行, 强度不生效; ERROR/WARN 仍全部分析)")
    elif struct.get("depth_cn"):
        L.append(f"分析强度: {struct['depth_cn']}")
    L.append(f"总量 {struct.get('total_lines', 0)} 行, 解析固定格式 {struct.get('parsed_fixed', 0)} 行, "
             f"其他 {struct.get('unparsed', 0)} 行")
    if struct.get("ts_min") is not None:
        span = (struct["ts_max"] - struct["ts_min"]) / 1000.0
        L.append(f"时间戳 {struct['ts_min']} ~ {struct['ts_max']} ms (跨度 {span:.1f}s)")
    if struct.get("focus"):
        L.append(f"特殊要求: 只分析匹配 /{struct['focus']}/ 的行, 命中 {struct.get('scope_lines', 0)} 行; "
                 f"本 HTML 仍为全量逐行")

    # ---- 结论: 与 analyze_log.build_conclusion 同口径(工程关联 + 人话判断 + 代码证据) ----
    where = struct.get("stages") or []
    stage_note = f", 主要阶段: {' / '.join(where)} (按文件名/函数名判断)" if where else ""
    if struct.get("project_linked"):
        L.append(f"关联工程: {struct.get('project_desc', '')}")
    else:
        L.append(f"未关联工程({struct.get('project_desc', '')}) -> 结论只基于日志本身; "
                 f"如需定位到源码/函数, 请在 config [projects] 写 default 或带 --project <编号|路径> 重跑。")
    ea, wa = struct.get("err_all", 0), struct.get("warn_all", 0)
    if ea == 0 and wa == 0:
        L.append(f"【结论】未发现 ERROR / WARN(按规则判定){stage_note}; 这段日志是设备正常输出。")
    elif ea:
        L.append(f"【结论】共 {ea} 行 ERROR / {wa} 行 WARN{stage_note}; "
                 f"存在 ERROR, 优先看下面已定位到源码的热点。")
    else:
        L.append(f"【结论】无 ERROR, {wa} 行 WARN{stage_note}; 未致命但需关注。")

    body = [x for x in (struct.get("body_samples") or []) if x][:3]
    if body:
        L.append("日志主体(最高频打印, 即判定依据): " + " | ".join(body))
    elif struct.get("hotspots"):
        L.append("日志主体(最高频打印位置): "
                 + " | ".join(h["loc"] for h in struct["hotspots"][:3]))

    links = struct.get("code_links") or []
    if links:
        L.append("固定格式热点已定位到工程源码(file:line -> 文件:行, 所在函数):")
        for k in links[:5]:
            fn = f", 函数 {k['func']}()" if k.get("func") else ""
            extra = "  [日志行号超出该文件长度, 版本可能不一致]" if k.get("out_of_range") else ""
            via = f"  [定位: {k['via']}]" if k.get("via") else ""
            L.append(f"  {k['loc']} -> {k['file']}:{k['line']}{fn}{via}{extra}")
            if k.get("src"):
                L.append(f"        源码: {k['src'][:120]}")
            for c in (k.get("callers") or [])[:3]:
                cf = f" 函数 {c['caller']}()" if c.get("caller") else ""
                L.append(f"        调用方: {c['file']}:{c['line']}{cf}  <- 异常触发链, 跨模块看这里")
    tlinks = struct.get("token_links") or []
    if tlinks:
        L.append("日志打印字段在工程源码中的出处(按字段名检索打印语句):")
        for k in tlinks[:6]:
            fn = f", 函数 {k['func']}()" if k.get("func") else ""
            via = f"  [定位: {k['via']}]" if k.get("via") else ""
            L.append(f"  {k['token']} -> {k['file']}:{k['line']}{fn}{via}")
            if k.get("src"):
                L.append(f"        源码: {k['src'][:120]}")
    mctx = struct.get("module_contexts") or []
    if mctx:
        L.append("模块上下文(热点所在模块在干什么, 供逻辑范围定位):")
        for c in mctx:
            lv = " ".join(f"{k}={v}" for k, v in
                          sorted(c["levels"].items(), key=lambda kv: -kv[1]))
            L.append(f"  {c['module']}: {c['hotspots']} 个热点 / {c['lines']} 行 ({lv})")
            for s in c.get("samples", [])[:2]:
                L.append(f"        例: {s[:110]}")
    if struct.get("project_linked") and not links and not tlinks:
        L.append("未能把日志对到工程源码: 可能是第三方库/RTD生成代码打印, 或日志文本与当前工程版本不一致"
                 "(固定格式需 file:line 匹配, 自由格式需打印字段名能检索到)。")

    if struct.get("drop_lines"):
        L.append(f"注意: 出现 {len(struct['drop_lines'])} 处 drop_cnt 上报, 固件有日志被丢弃, "
                 f"检查锁竞争/波特率。")
    if struct.get("hotspots"):
        codelink_by_loc = {k["loc"]: k for k in links}
        L.append("问题热点(ERROR 优先):")
        for h in struct["hotspots"][:5]:
            L.append(f"  [{h['level']}] {h['loc']} x {h['count']}")
            k = codelink_by_loc.get(h["loc"])
            if k:
                fn = f", 函数 {k['func']}()" if k.get("func") else ""
                via = f"  [定位: {k['via']}]" if k.get("via") else ""
                L.append(f"        代码: {k['file']}:{k['line']}{fn}{via}")
    return "\n".join(L)


def notes_from_struct(struct):
    """把 analyze_log 的热点/去重结果转成 shape -> 分析说明。"""
    notes = {}
    for h in struct.get("hotspots", []):
        notes[shape_key(h["sample"])] = (
            f"该位置共命中 {h['count']} 次, 级别 {h['level']}, 模块 {h['module']}; "
            f"首次 [{h['first_ts']}] 末次 [{h['last_ts']}]")
    for d in struct.get("dedup", []):
        notes.setdefault(d["shape"], f"该消息共出现 {d['count']} 次")
    notes.update(struct.get("notes_by_shape", {}))
    return notes


TPL = """<!DOCTYPE html><html><head><meta charset="utf-8">
<title>串口日志分析报告 __LOG__</title>
<style>
body{font-family:'Microsoft YaHei',Consolas,monospace;background:#1e1e1e;color:#d4d4d4;margin:0;padding:16px}
h1{font-size:18px;color:#fff} h2{font-size:15px;color:#9cdcfe;margin-top:20px}
.meta{color:#888;font-size:12px}
.lv{font-weight:bold;display:inline-block;width:64px;border-radius:3px;padding:0 4px;margin-right:6px;text-align:center}
.DEBUG{background:#444;color:#aaa}.INFO{background:#1a3a1a;color:#9acd9a}
.WARN{background:#4a3200;color:#fa0}.ERROR{background:#4a1a1a;color:#ff5f5f}
pre{white-space:pre-wrap;word-break:break-all;margin:0;line-height:1.5}
.row{padding:1px 4px}
.ai{background:#3a3210;border-left:3px solid #ffd700;color:#ffd700;
padding:4px 10px;margin:2px 0 6px 70px;font-size:13px;white-space:pre-wrap}
.summary{background:#13202c;border-left:4px solid #4fc1ff;padding:10px 14px;margin:10px 0;white-space:pre-wrap}
table{border-collapse:collapse;font-size:13px}td,th{border:1px solid #444;padding:4px 10px}
</style></head><body>
<h1>串口日志分析报告</h1>
<p class="meta">文件: __LOG__ | 行数: __TOTAL__ | 生成: __TIME__ | 检索: Ctrl+F</p>
__STATS__
<div class="summary"><b>分析总结:</b>
__SUMMARY__</div>
<h2>日志明细（WARN/ERROR 后附分析）</h2>
__BODY__
</body></html>"""


def esc(s):
    return html.escape(str(s), quote=False)


def build_stats_html(stats):
    if not stats:
        return ""
    rows = "".join(
        f"<tr><td>{esc(l)}</td><td>{c}</td></tr>"
        for l, c in sorted(stats.get("levels", {}).items()))
    hot = "".join(
        f"<tr><td>{esc(k)}</td><td>{v}</td></tr>"
        for k, v in list(stats.get("hotspots", {}).items())[:10])
    return f"""<h2>统计</h2>
<table><tr><th>Level</th><th>条数</th></tr>{rows}</table>
<p/><table><tr><th>WARN/ERROR 热点 top10</th><th>次数</th></tr>{hot}</table>"""


def build_stats_from_struct(struct):
    """用 analyze_log.py 的结果拼统计表(无需额外 stats.json)。"""
    lv = struct.get("levels_all") or {}
    rows = "".join(f"<tr><td>{esc(l)}</td><td>{c}</td></tr>"
                   for l in ("ERROR", "WARN", "INFO", "DEBUG") if (c := lv.get(l)))
    mods = struct.get("modules") or {}
    mrows = "".join(f"<tr><td>{esc(m)}</td><td>{c}</td></tr>"
                    for m, c in list(mods.items())[:15])
    hot = "".join(
        f"<tr><td>{esc(h['loc'])}</td><td>{esc(h['level'])}</td><td>{h['count']}</td></tr>"
        for h in struct.get("hotspots", [])[:10])
    dedup = "".join(
        f"<tr><td>{d['count']}</td><td>{esc(d['level'])}</td><td>{esc(d['sample'][:110])}</td></tr>"
        for d in struct.get("dedup", [])[:10])
    return f"""<h2>统计</h2>
<table><tr><th>Level</th><th>条数(全量)</th></tr>{rows}</table>
<p/><table><tr><th>位置</th><th>级别</th><th>次数</th></tr>{hot}</table>
<p/><table><tr><th>模块</th><th>条数</th></tr>{mrows}</table>
<p/><table><tr><th>次数</th><th>级别</th><th>高频消息(形状去重)</th></tr>{dedup}</table>"""


def main():
    ap = argparse.ArgumentParser(description="生成带AI分析的HTML日志报告")
    ap.add_argument("log", help="日志文件")
    ap.add_argument("--analysis", required=True, help="analyze_log.py 的结构化结果 JSON(或旧式 summary/by_line)")
    ap.add_argument("--stats", help="stats.json (可选, 旧式输入时用)")
    ap.add_argument("--out", help="输出 html 路径, 默认 output/logs/report_时间戳.html")
    ap.add_argument("--max-lines", type=int, default=20000,
                    help="HTML 逐行展示上限, 默认2万行(超出截断并提示, log 附件仍完整); 0=不限制")
    args = ap.parse_args()

    log_path = Path(args.log)
    if not log_path.exists():
        print(f"错误: 文件不存在 {log_path}", file=sys.stderr)
        sys.exit(1)

    analysis = {}
    try:
        analysis = json.loads(Path(args.analysis).read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[WARN] analysis 读取失败({e}), 报告将不含分析", file=sys.stderr)

    stats = {}
    if args.stats:
        try:
            stats = json.loads(Path(args.stats).read_text(encoding="utf-8"))
        except Exception:
            stats = {}

    # 两种输入: analyze_log.py 结构化结果 / 旧式 {summary, by_line}
    is_struct = "total_lines" in analysis or "dedup" in analysis
    if is_struct:
        by_line = {}
        notes = notes_from_struct(analysis)
        summary_text = summarize(analysis)
        stats_html = build_stats_from_struct(analysis)
        note_all = True   # 铁律: 无论哪个强度, WARN/ERROR 每一行都要挂分析说明
    else:
        by_line = analysis.get("by_line", {})
        notes = {}
        summary_text = analysis.get("summary", "（无）")
        stats_html = build_stats_html(stats)
        note_all = False

    body_parts = []
    total = 0
    max_lines = args.max_lines
    truncated = 0
    with open(log_path, "rb") as f:
        for raw in f:
            total += 1
            text = raw.decode("utf-8", errors="replace").lstrip("\ufeff").rstrip("\r\n")
            text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", "", text)
            if not text.strip():
                continue
            disp = text                                    # 展示保留行首主机时间戳
            text = HOST_TS_RE.sub("", text, count=1)      # 匹配/统计用剥掉前缀
            if max_lines and total > max_lines:
                truncated += 1
                continue
            lvl = classify(text)
            body_parts.append(
                f'<div class="row"><span class="lv {lvl}">{lvl}</span>'
                f'<pre style="display:inline">{esc(disp)}</pre></div>')
            if lvl in ("WARN", "ERROR"):
                tip = notes.get(shape_key(text))
                if tip is None:
                    key = line_key(text)
                    for k, v in by_line.items():
                        if k[:60] in key or key[:60] in k:
                            tip = v
                            break
                if tip is None and note_all:
                    tip = ("未进入热点/高频榜(属偶发异常); 该行所在形状未重复出现, "
                           "建议结合上下文与上一次成功握手对比定位。")
                if tip:
                    body_parts.append(f'<div class="ai">分析: {esc(tip)}</div>')
    if truncated:
        body_parts.append(f'<div class="meta">（已按 --max-lines {max_lines} 截断, '
                          f'另有 {truncated} 行未展示; 完整内容见 .log 附件）</div>')

    out = Path(args.out) if args.out else log_path.parent / f"report_{datetime.now():%Y%m%d_%H%M%S}.html"
    page = (TPL.replace("__LOG__", str(log_path))
            .replace("__TOTAL__", str(total))
            .replace("__TIME__", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            .replace("__STATS__", stats_html)
            .replace("__SUMMARY__", esc(summary_text))
            .replace("__BODY__", "\n".join(body_parts)))
    out.write_text(page, encoding="utf-8")
    print(f"报告已生成: {out} ({total} 行)")


if __name__ == "__main__":
    main()
