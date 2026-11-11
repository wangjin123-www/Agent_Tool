#!/usr/bin/env python3
"""串口日志分析: 固定格式 / 自由格式 / 自动判定 + 分析强度(低/中/高)。

三种分析方式(见 references/analysis_modes.md):
  fixed : DAB_BOX 固定格式 [ts][LEVEL][file:line] [module] msg
          -> 按 module / level / 具体内容(消息形状归一化) 三维聚合
  free  : 无结构日志(SoC/BSP 裸打印) -> 消息形状归一化去重 + 关键词分级 + 关键状态行
  auto  : 采样前若干行, 固定格式占比达阈值则用 fixed, 否则 free

分析强度 --depth(见 references/analysis_depth.md):
  low   : 只给结论 + level 计数 + 尾部行(几行以内)。适合只看"有没有炸"。
  medium: 低 + 问题热点 top10 + 高频消息 top10 + ERROR/WARN 明细各前若干行。默认。
  high  : 中 + 热点 top30 + 模块×Level 全量 + 关键状态行 + 时间分布桶 + drop 明细,
          且 HTML 中每条 WARN/ERROR 行都挂分析说明(不止热点命中的)。

万行以上策略(规模无关, 输出恒定几十~百行):
  - 计数全量累加, 不受行数影响
  - 明细只留去重后的代表行(每类上限 --keep, 由 depth 决定)
  - 热点/高频消息只取 top N(--top, 由 depth 决定)
  - 时间分布按桶聚合(high)

focus(特殊要求): --focus "正则" 时, **邮件正文只分析匹配行**(全量仍计入总数),
                 HTML 报告保持全量逐行。

代码关联(结论落到工程上):
  config/config.conf 的 [projects] 段登记"编号 = 工程根目录绝对路径", default = 默认编号。
  给了工程(或用默认工程)时:
    - 固定格式: 用热点的 file:line 直接定位工程源文件/行/所在函数
    - 任意格式: 用打印内容里的字段标识符(如 AppPowerHsmState)反查工程里对应的打印语句
    结论段据此给出"这段日志是哪个工程的哪个函数在打印 + 当前值", 而不是只报计数。
  没给工程且 config 无 default 时: 结论不关联代码, 并在结论里写明原因(需询问用户选工程)。

用法:
  python analyze_log.py <log> --mode auto --depth medium [--focus "HandShake"] \\
      [--project 2 | --project d:\\path\\to\\project] --md-out 分析.md --json-out 分析.json
  python analyze_log.py --list-projects
"""
import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

# 固定格式: [timestamp][DEBUG|INFO|WARN|ERROR][file:line] [module] message
FIXED_RE = re.compile(
    r"^\[(\d+)\](?:\[(DEBUG|INFO|WARN|ERROR|D|I|W|E)\])?\[([^\]:]+):(\d+)\]\s*\[([^\]]+)\]\s?(.*)$"
)
LEVEL_ALIAS = {"D": "DEBUG", "I": "INFO", "W": "WARN", "E": "ERROR",
               "DEBUG": "DEBUG", "INFO": "INFO", "WARN": "WARN", "ERROR": "ERROR"}
LEVEL_FIELD = re.compile(r"^\[\d+\]\[([A-Za-z]+)\]")
# 落盘行首主机时间戳(采集/Web保存时拼接): 分析前剥掉, 固定格式匹配不受影响
HOST_TS_RE = re.compile(r"^\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}\]\s?")

# 无 level 字段时的兜底判据(与 capture_serial/serial_monitor 保持一致)
ERR_PAT = re.compile(r"HardFault|CmBacktrace|ASSERT|assert|ERROR|ERR_|error|FAIL|fail|Fault|fault|panic|Panic")
WARN_PAT = re.compile(r"retry|RETRY|timeout|TIMEOUT|Timeout|WARN|\[W\]")

# drop 计数上报
DROP_RE = re.compile(r"drop_cnt\s*=\s*(\d+)")

# 关键状态行(嵌入式 bring-up 常用): 状态机/握手/供电/唤醒
STATE_PAT = re.compile(r"State|state|Status|status|mode|Mode|HandShake|handshake|wakeup|Wakeup|Pwr|pwr")

# 分析强度预设: 控制"看多深", 与行数规模解耦(见 references/analysis_depth.md)
# 铁律: ERROR/WARN 是三档共同的底线 -> err_n/warn_n/top 在三档都非 0, 任何强度都分析异常
DEPTH_PRESETS = {
    #        top  dedup  keep  err_n warn_n  states  mods  buckets  note_all
    "low":    {"top": 10, "dedup": 0,  "keep": 50,  "err_n": 20, "warn_n": 10, "states": 0,  "mods": 0,  "buckets": 0,  "note_all": False},
    "medium": {"top": 10, "dedup": 10, "keep": 200, "err_n": 20, "warn_n": 10, "states": 10, "mods": 10, "buckets": 0,  "note_all": False},
    "high":   {"top": 30, "dedup": 30, "keep": 500, "err_n": 60, "warn_n": 30, "states": 30, "mods": 0,  "buckets": 30, "note_all": True},
}
# 特殊要求(focus)优先: 有 --focus 时忽略 --depth, 改用这套配置(匹配行尽量全量分析)
FOCUS_PRESET = {"top": 50, "dedup": 50, "keep": 2000, "err_n": 200, "warn_n": 200,
                "states": 50, "mods": 20, "buckets": 0, "note_all": True}
DEPTH_CN = {"low": "低(只看异常: 结论+热点+ERROR/WARN明细)",
            "medium": "中(结论+热点+明细+高频消息+模块分布, 推荐)",
            "high": "高(全维度聚合, 耗时略长)"}
DEPTH_CN_FOCUS = "不适用(已按特殊要求执行, 强度不生效)"

# ---------------------------------------------------------------------------
# 代码关联: config/[projects] 工程注册表 -> 用 file:line 或打印字段反查源码
SKILL_DIR = Path(__file__).resolve().parent.parent.parent   # scripts/analyze/ -> skill 根
CONFIG_FILE = SKILL_DIR / "config" / "config.conf"
SRC_EXT = {".c", ".h", ".cpp", ".hpp", ".cc", ".hxx"}

# 打印语句判据(只在打印行上做字段反查, 避免命中变量声明/赋值)
PRINT_RE = re.compile(r"printf|Printf|PRINTF|printk|_log|Log\(|LOG\(|puts|MCU_Print")
IDENT_RE = re.compile(r"\b[A-Za-z_][A-Za-z0-9_]{4,}\b")
IDENT_STOP = {
    "debug", "error", "warn", "warning", "info", "printf", "sprintf", "print",
    "value", "count", "state", "status", "index", "false", "true", "null",
    "failed", "success", "timeout", "retry", "result", "handle", "buffer",
}
FUNC_DEF_RE = re.compile(r"^[A-Za-z_][\w \t\*]*?\**\s*([A-Za-z_]\w*)\s*\(")
FUNC_KW = {"if", "for", "while", "switch", "return", "sizeof", "else", "do", "case", "typedef"}

# 阶段语义(按文件名/函数名关键词推断, 只作提示, 明确标注依据)
SEMANTIC_HINTS = [
    (r"Handshake|HandShake|SocComm|SocCom", "MCU<->SoC 握手/通信"),
    (r"PowerHsm|HsmState|Power_Hsm|PwrHsm", "电源状态机(上电/唤醒/休眠)"),
    (r"Power|Pwr", "电源管理"),
    (r"Dtc|Fault|HwFault", "故障诊断(DTC)"),
    (r"CmBacktrace|HardFault|Assert|assert", "崩溃/断言回溯"),
    (r"Can|CanNm|AsrNm", "CAN 通信"),
    (r"Com_|_Com|Can_", "通信收发"),
    (r"Adc|InAmp|Volt|Curr", "模拟量采样(电压/电流)"),
    (r"Flash|Nvm|Ea_|Eeprom", "非易失存储"),
    (r"Iap|Boot|Upgrade|Update", "升级/引导"),
    (r"Hsm|State|Fsm", "状态机"),
    (r"Diag|Dcm|Dem", "诊断服务"),
]
INDEX_CACHE = {}


def load_projects():
    """读 config [projects] 段: 返回 (编号->工程根目录, 默认编号 or None)。
    路径按原样保留(Windows 反斜杠不转义), 只去首尾空白。"""
    projects, default = {}, None
    if not CONFIG_FILE.exists():
        return projects, default
    in_projects = False
    for line in CONFIG_FILE.read_text(encoding="utf-8", errors="replace").splitlines():
        s = line.strip()
        if not s or s.startswith(("#", ";")):
            continue
        if s.startswith("["):
            in_projects = s.strip("[]").strip().lower() == "projects"
            continue
        if not in_projects or "=" not in s:
            continue
        k, v = (x.strip() for x in s.split("=", 1))
        if k.lower() == "default":
            default = v or None
        elif v:
            projects[k] = v
    return projects, default


def resolve_project(arg):
    """--project 的值(编号|绝对路径|空) -> (根目录 Path 或 None, 描述)。
    空值用 config 默认工程; 都没有则返回 (None, 原因) -> 结论不关联代码。"""
    projects, default = load_projects()
    key = arg or default
    if not key:
        return None, "未指定工程且 config [projects] 无 default"
    if key in projects:
        tag = "" if arg else "(config 默认)"
        return Path(projects[key]), f"{key}{tag} = {projects[key]}"
    p = Path(key)
    if p.is_dir():
        return p, f"{key}(直接路径)"
    return None, f"{key}(config 无此编号且不是有效目录)"


def project_index(root):
    """工程源码索引: 小写文件名 -> [路径], 构建一次后缓存。"""
    idx = INDEX_CACHE.get(str(root))
    if idx is not None:
        return idx
    idx = defaultdict(list)
    try:
        for p in root.rglob("*"):
            if p.suffix.lower() in SRC_EXT and p.is_file():
                idx[p.name.lower()].append(p)
    except OSError:
        pass
    INDEX_CACHE[str(root)] = idx
    return idx


def enclosing_function(path, lineno, lines=None):
    """向上找最近的函数定义(顶格行): 返回 (函数名, 定义行号)。找不到返回 (None, None)。"""
    try:
        lines = lines if lines is not None else path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return None, None
    start = min(lineno, len(lines))
    for i in range(start - 1, max(-1, start - 400), -1):
        s = lines[i].rstrip()
        if not s.endswith((")", ",", "{")):
            continue
        m = FUNC_DEF_RE.match(s)
        if m and m.group(1) not in FUNC_KW and " " in s.split("(")[0].strip():
            return m.group(1), i + 1
    return None, None


def _rel(path, root):
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def locate_fixed(root, loc, msg=None):
    """固定格式热点 'Service_Com.c:1239' -> 工程内源码位置(文件/行/所在函数/源码行/所属模块)。
    msg(该热点的日志样本行)非空时做**接口名无关的内容验真**(src_msg_affinity):
    同名文件多候选时优先取内容匹配的候选; 验真失败 -> content_match=False, 供上层降级,
    防止跨工程同名文件(如两工程都有 APP_Power.c)把注释行/无关行当成打印出处。"""
    fname, _, lineno = loc.rpartition(":")
    if not lineno.isdigit():
        return None
    cands = project_index(root).get(Path(fname).name.lower()) or []
    if not cands:
        return None
    n = int(lineno)
    hits = []
    for path in cands[:5]:                      # 同名文件多候选, 最多验 5 个
        try:
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        src = lines[n - 1].strip() if 0 < n <= len(lines) else ""
        func, _ = enclosing_function(path, n, lines)
        hit = {"loc": loc, "file": _rel(path, root), "line": n, "func": func,
               "src": src, "out_of_range": not src, "multi": len(cands) > 1,
               "module": module_of(_rel(path, root))}
        hit["content_match"] = (src_msg_affinity(src, msg)
                                if msg is not None else None)
        hits.append(hit)
        if hit["content_match"]:                # 内容验真通过即停, 不再看其余候选
            break
    if not hits:
        return None
    verified = next((h for h in hits if h["content_match"]), hits[0])
    return verified


STR_LIT_RE = re.compile(r'"((?:[^"\\\n]|\\.)*)"')
FMT_SPEC_RE = re.compile(r'%[-+ #0]*\d*(?:\.\d+)?(?:hh|h|ll|l|L|z|j|t)?[diouxXeEfgGaAcspn]')


def src_msg_affinity(src_line, msg, min_len=3):
    """接口名无关的'源码行 <-> 日志消息'验真: 打印语句的字符串字面量按格式符(%d/%s/...)
    切成字面段, 所有字面段(>=min_len)按顺序出现在 msg 中(实参替换了格式符)即认定同源。
    不依赖 printf/LOG_INFO 等接口名——接口改名不影响验真。"""
    if not src_line or not msg:
        return False
    for lit in STR_LIT_RE.findall(src_line):
        # 还原常见转义(日志侧 \r\n 已被行处理剥掉)
        lit = lit.replace("\\r", "").replace("\\n", "") \
                 .replace("\\t", " ").replace('\\"', '"')
        segs = [s for s in FMT_SPEC_RE.split(lit) if len(s.strip()) >= min_len]
        if not segs:
            continue
        pos, ok = 0, True
        for seg in segs:
            i = msg.find(seg, pos)
            if i < 0:
                ok = False
                break
            pos = i + len(seg)
        if ok:
            return True
    return False


def module_of(rel_path):
    """相对路径 -> 模块标识: 取距文件最近的两级目录(层级/模块)。
    L1_APP/APP_Tuner/APP_Tuner.c -> L1_APP/APP_Tuner
    目录只有一级则取一级; 根目录文件 -> '(root)'。"""
    dirs = Path(rel_path).as_posix().split("/")[:-1]
    if not dirs:
        return "(root)"
    return "/".join(dirs[-2:]) if len(dirs) >= 2 else dirs[-1]


def find_callers(root, func, max_hits=5):
    """全工程搜 func( 的调用点(排除定义行/原型声明), 返回 [{file,line,caller,src}]。
    用于异常热点的跨模块因果补链: ERROR 打印点所在函数往往不是触发者。"""
    if not func:
        return []
    idx = project_index(root)
    call_re = re.compile(r"\b" + re.escape(func) + r"\s*\(")
    out = []
    for paths in idx.values():
        for p in paths:
            if len(out) >= max_hits:
                break
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            if func not in text:               # 粗筛: 调用处必含函数名
                continue
            lines = text.splitlines()
            for i, s in enumerate(lines, 1):
                if len(out) >= max_hits:
                    break
                if not call_re.search(s):
                    continue
                d = FUNC_DEF_RE.match(s)
                if d and d.group(1) == func:
                    continue                    # 定义行
                if s.rstrip().endswith(";") and d:
                    continue                    # 原型声明(.h)
                caller, _ = enclosing_function(p, i, lines)
                out.append({"file": _rel(p, root), "line": i, "caller": caller,
                            "src": s.strip()[:120]})
    return out


def module_context(hot_counter, hot_meta, file_mod, module, keep=3):
    """按代码模块聚合全量热点(未被 top 裁剪), 给"该模块在干什么"的上下文。
    file_mod: fname -> module 的映射(调用方预建)。返回 None 表示模块内证据不足(<2 个不同 loc)。"""
    locs = [(loc, cnt) for loc, cnt in hot_counter.items()
            if file_mod.get(loc.rpartition(":")[0]) == module]
    if not locs:
        return None
    locs.sort(key=lambda kv: (_lv_rank(hot_meta[kv[0]]["level"]), -kv[1]))
    levels = Counter(hot_meta[l]["level"] for l, _ in locs)
    ts_all = [hot_meta[l][k] for l, _ in locs for k in ("first_ts", "last_ts")
              if hot_meta[l][k] is not None]
    return {
        "module": module,
        "hotspots": len(locs),
        "lines": sum(cnt for _, cnt in locs),
        "levels": dict(levels),
        "first_ts": min(ts_all) if ts_all else None,
        "last_ts": max(ts_all) if ts_all else None,
        "top_locs": [{"loc": l, "count": c, "level": hot_meta[l]["level"]}
                     for l, c in locs[:keep]],
        "samples": [hot_meta[l]["sample"][:120] for l, _ in locs[:keep]],
    }


def extract_tokens(samples, limit=5):
    """从代表行里提字段标识符(如 AppPowerHsmState), 供在工程里反查打印语句。"""
    cnt = Counter()
    for s in samples:
        for t in set(IDENT_RE.findall(s)):
            if t.lower() not in IDENT_STOP:
                cnt[t] += 1
    return [t for t, _ in cnt.most_common(limit)]


def grep_project(root, tokens, max_per_token=1):
    """在工程源码(仅打印行)里搜字段, 返回 {token: [{file,line,func,src}]}。每个文件只读一次。"""
    if not tokens:
        return {}
    idx = project_index(root)
    res = defaultdict(list)
    for paths in idx.values():
        for p in paths:
            if all(len(res[t]) >= max_per_token for t in tokens):
                break
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            if not any(t in text for t in tokens):
                continue
            lines = text.splitlines()
            for i, s in enumerate(lines, 1):
                if not PRINT_RE.search(s):
                    continue
                for t in tokens:
                    if t in s and len(res[t]) < max_per_token:
                        func, _ = enclosing_function(p, i, lines)
                        res[t].append({"token": t, "file": _rel(p, root), "line": i,
                                       "func": func, "src": s.strip()})
    return dict(res)


def infer_stages(texts):
    """按关键词把文件名/函数名映射成"当前在跑什么"(依据名字, 供参考, 不编造)。
    每条文本只取第一个命中的语义(避免堆叠), 再按命中次数排序取前几项,
    使日志里反复出现的阶段(如握手/通信)优先进入结论。"""
    hit = Counter()
    order = {}
    for txt in texts:
        for i, (pat, cn) in enumerate(SEMANTIC_HINTS):
            if re.search(pat, txt):
                hit[cn] += 1
                order.setdefault(cn, i)
                break
    ranked = sorted(hit.items(), key=lambda kv: (-kv[1], order[kv[0]]))
    return [cn for cn, _ in ranked[:4]]


def build_conclusion(r):
    """结论正文: 先给人话判断(当前在跑什么/有没有问题), 再给"结论-代码"对应证据。"""
    L = []
    if r.get("project_linked"):
        L.append(f"关联工程: {r['project_desc']}")
    else:
        L.append(f"未关联工程({r.get('project_desc', '')}) -> 本结论只基于日志本身; "
                 f"如需定位到源码/函数, 请在 config [projects] 写 default 或带 --project <编号|路径> 重跑。")

    where = r.get("stages") or []
    src_note = ""
    if where:
        src_note = f", 主要阶段: {' / '.join(where)} (按文件名/函数名判断)"
    if r["err_all"]:
        L.append(f"【结论】共 {r['err_all']} 行 ERROR / {r['warn_all']} 行 WARN{src_note}; "
                 f"存在 ERROR, 优先看下面已定位到源码的热点。")
    elif r["warn_all"]:
        L.append(f"【结论】无 ERROR, {r['warn_all']} 行 WARN{src_note}; 未致命但需关注。")
    else:
        L.append(f"【结论】未发现 ERROR/WARN{src_note}; 这段日志是设备正常输出。")

    # "当前到底在打什么": 用最高频打印(自由格式)或热点位置(固定格式)说清楚
    body = [x for x in (r.get("body_samples") or []) if x][:3]
    if body:
        L.append("日志主体(最高频打印, 即判定依据): " + " | ".join(body))
    elif r.get("hotspots"):
        L.append("日志主体(最高频打印位置): "
                 + " | ".join(h["loc"] for h in r["hotspots"][:3]))

    links = r.get("code_links") or []
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
    tlinks = r.get("token_links") or []
    if tlinks:
        L.append("日志打印字段在工程源码中的出处(按字段名检索打印语句):")
        for k in tlinks[:6]:
            fn = f", 函数 {k['func']}()" if k.get("func") else ""
            via = f"  [定位: {k['via']}]" if k.get("via") else ""
            L.append(f"  {k['token']} -> {k['file']}:{k['line']}{fn}{via}")
            if k.get("src"):
                L.append(f"        源码: {k['src'][:120]}")
    mctx = r.get("module_contexts") or []
    if mctx:
        L.append("模块上下文(热点所在模块在干什么, 供逻辑范围定位):")
        for c in mctx:
            lv = " ".join(f"{k}={v}" for k, v in
                          sorted(c["levels"].items(), key=lambda kv: -kv[1]))
            L.append(f"  {c['module']}: {c['hotspots']} 个热点 / {c['lines']} 行 ({lv})")
            for s in c.get("samples", [])[:2]:
                L.append(f"        例: {s[:110]}")
    if r.get("project_linked") and not links and not tlinks:
        L.append("未能把日志对到工程源码: 可能是第三方库/RTD生成代码打印, 或日志文本与当前工程版本不一致"
                 "(固定格式需 file:line 匹配, 自由格式需打印字段名能检索到)。")
    if r.get("modules"):
        top = list(r["modules"].items())[:3]
        if top:
            L.append("模块分布(前3): " + ", ".join(f"{m} {c} 行" for m, c in top))
    if r.get("drop_lines"):
        L.append(f"另有 {len(r['drop_lines'])} 处 drop_cnt 上报: 固件有日志被丢弃, 检查锁竞争/波特率。")
    return L


def _lv_rank(lvl):
    """排序权重: ERROR 最前, 其次 WARN, 再 INFO/DEBUG(热点只看异常优先级)。"""
    return {"ERROR": 0, "WARN": 1, "INFO": 2, "DEBUG": 3}.get(lvl, 2)


def classify_text(text):
    """返回 DEBUG/INFO/WARN/ERROR: 固定格式优先取 level 字段, 否则关键词兜底。"""
    m = LEVEL_FIELD.match(text)
    if m and m.group(1).upper() in LEVEL_ALIAS:
        return LEVEL_ALIAS[m.group(1).upper()]
    if ERR_PAT.search(text):
        return "ERROR"
    if WARN_PAT.search(text):
        return "WARN"
    return "INFO"


def normalize_shape(text):
    """把一行归一化为"消息形状"key: 去时间戳/去 hex/去数字, 用于跨行去重计数。"""
    t = re.sub(r"^\[\d+\]", "", text)
    t = re.sub(r"0x[0-9a-fA-F]+", "0xH", t)
    t = re.sub(r"\b\d+\b", "N", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t[:120]


def detect_mode(sample):
    """采样判定: 固定格式占比 >= 0.5 用 fixed, 否则 free。"""
    total = parsed = 0
    for text in sample:
        total += 1
        if FIXED_RE.match(text):
            parsed += 1
    if total == 0:
        return "free", 0.0
    ratio = parsed / total
    return ("fixed" if ratio >= 0.5 else "free"), ratio


CTRL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")


def clean(s):
    """去掉串口乱码/空字节等控制字符: 否则进入邮件正文会被 subprocess 拒绝(embedded null character)。"""
    return CTRL_RE.sub("", s)


def analyze(path, mode="auto", focus=None, top=None, keep=None, sample_n=2000, depth="medium",
            project=None):
    """depth: low/medium/high 决定 top/keep/明细条数/是否全量挂分析(见 DEPTH_PRESETS)。
    铁律1: 有 focus(特殊要求) 时, **强度不生效**, 改用 FOCUS_PRESET 严格按用户要求分析。
    铁律2: 无论哪个强度, ERROR/WARN 都必须分析(err_n/warn_n/top 在三档均非 0)。
    project: 工程编号(|config 编号)或绝对路径; 空=用 config [projects] default;
             两者都没有 -> 结论不关联代码(project_linked=False)。"""
    mode_requested = mode
    depth_requested = depth
    if focus:
        # 特殊要求优先于强度: 用户说了只看什么, 就按他的要求做, 不再受 low/medium/high 裁剪
        dcfg = dict(FOCUS_PRESET)
        depth_effective = None
    else:
        dcfg = dict(DEPTH_PRESETS.get(depth, DEPTH_PRESETS["medium"]))
        depth_effective = depth
    if top is None:
        top = dcfg["top"]
    if keep is None:
        keep = dcfg["keep"]
    focus_re = re.compile(focus) if focus else None

    sample = []
    with open(path, "rb") as f:
        for raw in f:
            s = HOST_TS_RE.sub("", clean(raw.decode("utf-8", errors="replace")
                                         .lstrip("\ufeff").rstrip("\r\n")), count=1)
            if s.strip():
                sample.append(s)
            if len(sample) >= sample_n:
                break
    fixed_ratio = 0.0
    if mode == "auto":
        mode, fixed_ratio = detect_mode(sample)

    levels_all = Counter()
    levels_scope = Counter()
    modules = Counter()
    level_by_module = defaultdict(Counter)
    shapes = Counter()                 # 去重: shape -> 次数
    shape_meta = {}                    # shape -> {level, module, sample, first_ts, last_ts}
    hotspots = Counter()               # file:line -> 次数
    hotspot_meta = {}
    buckets = Counter()                # 时间桶(1s) -> 行数, high 用
    err_scope, warn_scope = [], []
    state_lines = {}
    drop_lines = []
    tail = []
    total = parsed = unparsed = scope_lines = 0
    err_all = warn_all = 0
    ts_min = ts_max = None

    with open(path, "rb") as f:
        for raw in f:
            total += 1
            text = HOST_TS_RE.sub("", clean(raw.decode("utf-8", errors="replace")
                                          .lstrip("\ufeff").rstrip("\r\n")), count=1)
            tail.append(text[:200])
            if len(tail) > 5:
                tail.pop(0)
            if not text.strip():
                continue

            ts = None
            m = FIXED_RE.match(text)
            if m:
                parsed += 1
                ts, lvl_field, fname, lineno, module, msg = m.groups()
                ts = int(ts)
                ts_min = ts if ts_min is None else min(ts_min, ts)
                ts_max = ts if ts_max is None else max(ts_max, ts)
                lvl = LEVEL_ALIAS[lvl_field] if lvl_field else classify_text(msg)
                loc = f"{fname}:{lineno}"
            else:
                unparsed += 1
                module = "-"
                msg = text
                loc = None
                lvl = classify_text(text)

            levels_all[lvl] += 1
            if lvl == "ERROR":
                err_all += 1
            elif lvl == "WARN":
                warn_all += 1

            dm = DROP_RE.search(text)
            if dm:
                drop_lines.append((ts, int(dm.group(1)), text[:120]))
                if len(drop_lines) > 20:
                    drop_lines.pop(0)

            in_scope = focus_re.search(text) is not None if focus_re else True
            if not in_scope:
                continue
            scope_lines += 1
            levels_scope[lvl] += 1
            modules[module] += 1
            level_by_module[module][lvl] += 1

            shape = normalize_shape(msg if parsed else text)
            shapes[shape] += 1
            meta = shape_meta.get(shape)
            if meta is None:
                shape_meta[shape] = {"level": lvl, "module": module, "sample": text[:200],
                                     "first_ts": ts, "last_ts": ts}
            else:
                meta["last_ts"] = ts
                if lvl == "ERROR" or (lvl == "WARN" and meta["level"] not in ("ERROR",)):
                    meta["level"] = lvl
                    meta["sample"] = text[:200]

            if loc:
                hotspots[loc] += 1
                hm = hotspot_meta.get(loc)
                if hm is None:
                    hotspot_meta[loc] = {"level": lvl, "count": 1, "first_ts": ts, "last_ts": ts,
                                         "sample": text[:200], "module": module}
                else:
                    hm["count"] += 1
                    hm["last_ts"] = ts
                    if lvl == "ERROR" and hm["level"] != "ERROR":
                        hm["level"] = lvl
                        hm["sample"] = text[:200]

            if lvl == "ERROR" and len(err_scope) < keep:
                err_scope.append(text[:200])
            elif lvl == "WARN" and len(warn_scope) < keep:
                warn_scope.append(text[:200])

            if STATE_PAT.search(text) and len(text) > 8:
                state_lines[normalize_shape(text)] = text[:200]
            if dcfg["buckets"] and ts is not None:
                buckets[ts // 1000] += 1

    # 热点排序: ERROR 优先, 再按次数
    hot_list = []
    for loc, cnt in hotspots.most_common(200):
        hm = hotspot_meta[loc]
        hot_list.append({"loc": loc, "level": hm["level"], "count": cnt,
                         "first_ts": hm["first_ts"], "last_ts": hm["last_ts"],
                         "sample": hm["sample"], "module": hm["module"]})
    hot_list.sort(key=lambda x: (_lv_rank(x["level"]), -x["count"]))
    hot_list = hot_list[:top]

    dedup = []
    for shape, cnt in shapes.most_common(max(1, dcfg["dedup"]) * 3):
        meta = shape_meta[shape]
        dedup.append({"count": cnt, "level": meta["level"], "module": meta["module"],
                      "shape": shape, "sample": meta["sample"],
                      "first_ts": meta["first_ts"], "last_ts": meta["last_ts"]})
    dedup.sort(key=lambda x: (_lv_rank(x["level"]), -x["count"]))
    dedup = dedup[:dcfg["dedup"]]

    # 时间分布桶: 只保留行数最高的若干秒(high), 避免输出爆炸
    bucket_list = []
    if dcfg["buckets"] and buckets:
        base = min(buckets)
        for sec in sorted(buckets)[:dcfg["buckets"]]:
            bucket_list.append({"t": f"+{sec - base}s", "lines": buckets[sec]})
        peak = max(buckets.items(), key=lambda kv: kv[1])
        bucket_list.append({"t": f"峰值 +{peak[0] - base}s", "lines": peak[1]})

    # ---- 代码关联: 模块漏斗定位 ----
    # ERROR/WARN 热点: 无条件全局反查 + 调用方检索(异常常是跨模块因果, 不走漏斗)
    # 常规热点: file:line -> 模块 -> 模块内上下文(>=2 个不同 loc 才算"模块内定位")
    #           证据不足 -> 全局兜底(grep_project)
    root, project_desc = resolve_project(project)
    code_links, token_links, module_contexts = [], [], []
    if root:
        # 预建 fname -> 代码模块 映射(工程索引一次查询, 缓存复用)
        file_mod = {}
        for loc in hotspots:
            fname = loc.rpartition(":")[0]
            if fname in file_mod:
                continue
            cands = project_index(root).get(Path(fname).name.lower()) or []
            file_mod[fname] = module_of(_rel(cands[0], root)) if cands else None

        # 模块上下文: 热点行数最多的前 3 个模块(fixed 有 loc 才有意义)
        if hotspots:
            mod_lines = Counter()
            for loc, cnt in hotspots.items():
                m = file_mod.get(loc.rpartition(":")[0])
                if m:
                    mod_lines[m] += cnt
            for m, _ in mod_lines.most_common(3):
                ctx = module_context(hotspots, hotspot_meta, file_mod, m)
                if ctx:
                    module_contexts.append(ctx)

        for h in hot_list:
            hit = locate_fixed(root, h["loc"], msg=h.get("sample"))
            if not hit:
                continue
            hit["count"] = h["count"]
            hit["level"] = h["level"]
            mod = hit["module"]
            if hit["content_match"] is False and not hit["out_of_range"]:
                # 内容验真失败: 命中的行不是打印语句/文本不同源 -> 疑同名文件误命中,
                # 不再宣称"模块内定位", 也不挂调用方(避免在错误代码上编因果链)
                hit["via"] = "内容不符(疑同名文件误命中)"
                code_links.append(hit)
                continue
            if h["level"] in ("ERROR", "WARN"):
                # 铁律延伸: 异常无条件全局, 并补调用方(跨模块优先, 根因往往不在打印点模块)
                hit["via"] = "异常全局反查"
                callers = find_callers(root, hit.get("func"))
                hit["callers"] = sorted(
                    callers,
                    key=lambda c: module_of(c["file"]) == mod)   # 跨模块 False<同模块 True
            else:
                # locate_fixed 已命中工程文件且行有效 = 模块内定位; 行号失效才走全局兜底
                hit["via"] = "全局兜底" if hit["out_of_range"] else f"模块内({mod})"
            code_links.append(hit)
        samples = [d["sample"] for d in dedup] or [v for v in state_lines.values()][:5]
        tokens = extract_tokens(samples + err_scope[:5] + warn_scope[:5], limit=5)
        found = grep_project(root, tokens, max_per_token=3)
        seen = set()
        for t in tokens:
            hits = found.get(t, [])
            # free 反查按命中文件模块分组: 同模块 >=2 个命中优先(消除跨模块同名打印歧义)
            by_mod = defaultdict(list)
            for it in hits:
                by_mod[module_of(it["file"])].append(it)
            pick, via = [], "全局兜底"
            for m, its in by_mod.items():
                if len(its) >= 2:
                    pick, via = its[:2], f"模块内({m})"
                    break
            if not pick and hits:
                pick = hits[:1]
            for it in pick:
                it["via"] = via
                key = (it["file"], it["line"])       # 同一处打印只报一次
                if key in seen:
                    continue
                seen.add(key)
                token_links.append(it)
    related = [x for k in code_links for x in (k.get("file"), k.get("func")) if x] \
        + [x for k in token_links for x in (k.get("file"), k.get("func")) if x]
    stages = infer_stages(related + list(modules.keys()) + [s for s in tail]
                          + [v for v in state_lines.values()])

    # 结论里"当前在打什么"的判定依据: 最高频打印(自由格式取消息样本, 固定格式取热点位置)
    body_samples = []
    for d in dedup[:3]:
        txt = (d.get("sample") or d.get("shape") or "").strip()
        if txt:
            body_samples.append(txt[:80])
    if not body_samples:
        body_samples = [f"{h['loc']} {h['sample'].strip()[:60]}" for h in hot_list[:3]]

    result = {
        "file": str(path),
        "mode": mode,
        "mode_requested": mode_requested,
        "depth": depth_requested,
        "depth_effective": depth_effective,          # None = 被 focus 覆盖
        "focus_override": bool(focus),               # True 时强度不生效
        "depth_cn": DEPTH_CN_FOCUS if focus else DEPTH_CN.get(depth_requested, ""),
        "fixed_ratio": round(fixed_ratio, 3),
        "focus": focus,
        "project": project,
        "project_root": str(root) if root else None,
        "project_desc": project_desc,
        "project_linked": bool(root),
        "code_links": code_links[:10],
        "token_links": token_links[:10],
        "module_contexts": module_contexts[:3],
        "stages": stages,
        "body_samples": body_samples,
        "total_lines": total,
        "parsed_fixed": parsed,
        "unparsed": unparsed,
        "scope_lines": scope_lines,
        "levels_all": dict(levels_all),
        "levels_scope": dict(levels_scope),
        "modules": dict(modules.most_common(50)),
        "level_by_module": {k: dict(v) for k, v in
                            sorted(level_by_module.items(), key=lambda kv: -sum(kv[1].values()))[:20]},
        "hotspots": hot_list,
        "dedup": dedup,
        "err_scope": err_scope[:keep],
        "warn_scope": warn_scope[:keep],
        "err_all": err_all,
        "warn_all": warn_all,
        "ts_min": ts_min,
        "ts_max": ts_max,
        "drop_lines": [[t, c, s] for t, c, s in drop_lines],
        "state_lines": [v for v in list(dict.fromkeys(state_lines.values()))[:max(1, dcfg["states"])]]
        if dcfg["states"] else [],
        "buckets": bucket_list,
        "tail": tail,
        "generated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    # 供 HTML 逐行分析块使用的形状 -> 说明 映射
    notes = {}
    for h in hot_list:
        notes[normalize_shape(h["sample"])] = (
            f"该处共命中 {h['count']} 次(首次 [{h['first_ts']}] 末次 [{h['last_ts']}]), "
            f"级别 {h['level']}, 模块 {h['module']}")
    for d in dedup:
        notes.setdefault(d["shape"], f"该消息共出现 {d['count']} 次" +
                         (f"(首 [{d['first_ts']}] 末 [{d['last_ts']}])" if d["first_ts"] is not None else ""))
    result["notes_by_shape"] = notes
    result["note_all"] = dcfg["note_all"]   # high: HTML 中每条 WARN/ERROR 都挂说明
    return result


def fmt_md(r):
    """生成邮件正文摘要(纯文本 markdown-ish), 规模无关。
    强度 low/medium/high 决定章节多少(见 references/analysis_depth.md)。
    铁律: 有特殊要求(focus)时强度不生效; 且任何强度下 ERROR/WARN 明细都必出。"""
    L = []
    ap = L.append
    if r.get("focus_override"):
        dcfg = dict(FOCUS_PRESET)          # 特殊要求优先, 强度不参与裁剪
    else:
        dcfg = DEPTH_PRESETS.get(r.get("depth", "medium"), DEPTH_PRESETS["medium"])
    mode_cn = {"fixed": "固定格式分析(module/level/内容聚合)",
               "free": "自由格式分析(消息形状去重 + 关键词分级)"}[r["mode"]]
    ap("【串口日志分析】")
    ap(f"文件: {Path(r['file']).name}")
    ap(f"方式: {mode_cn}" + (f"   自动判定(固定格式占比 {r['fixed_ratio']:.0%})"
                            if r["mode_requested"] == "auto" else ""))
    if r.get("focus_override"):
        ap("强度: 不适用(已按你的特殊要求执行, 强度不生效)")
    else:
        ap(f"强度: {r.get('depth_cn', r.get('depth', ''))}")
    span = f"{r['ts_min']} ~ {r['ts_max']} ms (跨度 {(r['ts_max'] - r['ts_min']) / 1000:.1f} s)" \
        if r["ts_min"] is not None else "无时间戳"
    ap(f"总量: {r['total_lines']} 行   时段: {span}")
    if r["focus"]:
        ap(f"特殊要求: 只分析匹配 /{r['focus']}/ 的行 -> 命中 {r['scope_lines']} 行"
           f"(全量仍计入上方总数; HTML 附报告为全量)")
    ap("")

    la, ls = r["levels_all"], r["levels_scope"]
    ap("== 结论 ==")
    for line in build_conclusion(r):
        ap(line)
    if r["focus"] and (la.get("ERROR") or la.get("WARN")):
        ap(f"(全量口径: ERROR {r['err_all']} / WARN {r['warn_all']}; "
           f"范围内 ERROR {ls.get('ERROR', 0)} / WARN {ls.get('WARN', 0)})")
    ap("")

    ap(f"== Level 分布({'分析范围' if r['focus'] else '全量'}) ==")
    dist = ls if r["focus"] else la
    for lvl in ("ERROR", "WARN", "INFO", "DEBUG"):
        if dist.get(lvl):
            ap(f"  {lvl:<6} {dist[lvl]}")
    if r["focus"] and any(la.get(x) for x in ("ERROR", "WARN")):
        ap(f"  (全量对照: ERROR {la.get('ERROR', 0)} / WARN {la.get('WARN', 0)})")
    ap("")

    if r["hotspots"]:
        ap("== 问题热点(file:line, 按 ERROR 优先/次数排序) ==")
        codelink_by_loc = {k["loc"]: k for k in r.get("code_links", [])}
        for h in r["hotspots"]:
            ts = f"首 [{h['first_ts']}] 末 [{h['last_ts']}]" if h["first_ts"] is not None else ""
            ap(f"  [{h['level']}] {h['loc']}  共 {h['count']} 次  {ts}")
            ap(f"        代表: {h['sample'][:160]}")
            k = codelink_by_loc.get(h["loc"])
            if k:
                fn = f"  函数 {k['func']}()" if k.get("func") else ""
                mod = f"  模块 {k['module']}" if k.get("module") else ""
                ap(f"        代码: {k['file']}:{k['line']}{fn}{mod}  [定位: {k.get('via', '-')}]")
                if k.get("src"):
                    ap(f"        源码: {k['src'][:140]}")
                for c in (k.get("callers") or [])[:2]:
                    cf = f" 函数 {c['caller']}()" if c.get("caller") else ""
                    ap(f"        调用方: {c['file']}:{c['line']}{cf}")
        ap("")

    if r["dedup"]:
        ap("== 高频消息(形状去重, top) ==")
        for d in r["dedup"]:
            ap(f"  x{d['count']:<6} [{d['level']}] {d['sample'][:150]}")
        ap("")

    if dcfg["mods"] and r["mode"] == "fixed" and r["level_by_module"]:
        ap("== 模块 × Level(异常优先) ==")
        for mod, cnts in list(r["level_by_module"].items())[:dcfg["mods"]]:
            txt = " ".join(f"{k}={v}" for k, v in sorted(cnts.items(), key=lambda kv: -kv[1]))
            ap(f"  {mod:<20} {txt}")
        ap("")

    if dcfg["buckets"] and r.get("buckets"):
        ap("== 时间分布(每秒行数, 供判断是否有卡顿/突发) ==")
        for b in r["buckets"]:
            ap(f"  {b['t']:<12} {b['lines']} 行")
        ap("")

    if r["state_lines"]:
        ap(f"== 关键状态行(状态机/握手/供电/唤醒, 末次, 最多 {dcfg['states']} 条) ==")
        for s in r["state_lines"]:
            ap(f"  {s[:160]}")
        ap("")

    if r["err_scope"]:
        n = min(dcfg["err_n"], len(r["err_scope"]))
        ap(f"== ERROR 明细(前 {n} / 共 {ls.get('ERROR', 0)} 行) ==")
        for s in r["err_scope"][:n]:
            ap(f"  {s[:180]}")
        ap("")
    if dcfg["warn_n"] and r["warn_scope"]:
        n = min(dcfg["warn_n"], len(r["warn_scope"]))
        ap(f"== WARN 明细(前 {n} / 共 {ls.get('WARN', 0)} 行) ==")
        for s in r["warn_scope"][:n]:
            ap(f"  {s[:180]}")
        ap("")

    if r["tail"]:
        ap("== 尾部 5 行(判断是否卡死/掉线) ==")
        for s in r["tail"]:
            ap(f"  {s[:180]}")
        ap("")
    ap(f"生成: {r['generated']}   详细逐行报告见邮件 HTML 附件")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description="串口日志分析(固定/自由/自动)")
    ap.add_argument("log", nargs="?", help="日志文件")
    ap.add_argument("--list-projects", action="store_true",
                    help="列出 config [projects] 登记的工程与默认工程")
    ap.add_argument("--mode", choices=["fixed", "free", "auto"], default="auto",
                    help="分析方式: fixed=固定格式, free=自由格式, auto=按日志格式自动判定(默认)")
    ap.add_argument("--focus", help="特殊要求: 只分析匹配该正则的行(邮件正文), HTML 仍为全量; 有此参数时 --depth 不生效")
    ap.add_argument("--depth", choices=["low", "medium", "high"], default=None,
                    help="分析强度: low=只看异常(结论+热点+ERROR/WARN明细), medium=中等(默认), high=全维度聚合"
                         " (见 references/analysis_depth.md; 三档都必然分析 ERROR/WARN; 有 --focus 时本参数失效)")
    ap.add_argument("--project",
                    help="关联工程: config [projects] 里的编号(如 2)或工程根目录绝对路径; "
                         "不传则用 config 的 default; 都没有则不按工程分析(结论不关联代码)")
    ap.add_argument("--top", type=int, help="热点/高频消息展示条数(默认由 --depth 决定)")
    ap.add_argument("--keep", type=int, help="明细保留上限(默认由 --depth 决定)")
    ap.add_argument("--md-out", help="邮件正文摘要输出路径")
    ap.add_argument("--json-out", help="结构化结果输出路径(供 gen_report 生成 HTML)")
    ap.add_argument("--print", action="store_true", help="同时打印摘要到屏幕")
    args = ap.parse_args()

    if args.list_projects:
        projects, default = load_projects()
        if not projects:
            print(f"config 未登记任何工程: {CONFIG_FILE}")
            return
        print(f"工程注册表: {CONFIG_FILE}")
        for k, v in projects.items():
            mark = "  <- 默认" if k == default else ""
            print(f"  {k} = {v}{mark}")
        print("默认工程: " + (default or "(未设置 -> 每次分析需询问用哪个工程)"))
        return

    if not args.log:
        print("错误: 需要 <日志文件> (或用 --list-projects 查看工程注册表)", file=sys.stderr)
        sys.exit(1)
    p = Path(args.log)
    if not p.exists():
        print(f"错误: 文件不存在 {p}", file=sys.stderr)
        sys.exit(1)
    # 铁律: 没有特殊要求时才需要强度; 没给也不报错(unlimited 场景兜底 medium)
    if not args.focus and not args.depth:
        args.depth = "medium"
    try:
        r = analyze(p, args.mode, args.focus, args.top, args.keep, depth=args.depth,
                    project=args.project)
    except re.error as e:
        print(f"错误: --focus 正则非法: {e}", file=sys.stderr)
        sys.exit(1)

    md = fmt_md(r)
    if args.md_out:
        Path(args.md_out).write_text(md, encoding="utf-8")
        print(f"摘要已写入: {args.md_out}")
    if args.json_out:
        Path(args.json_out).write_text(json.dumps(r, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"结构化结果已写入: {args.json_out}")
    if args.print or not (args.md_out or args.json_out):
        print(md)
    strength = "不生效(按特殊要求)" if r.get("focus_override") else r["depth"]
    proj = r["project_root"] if r.get("project_linked") else f"未关联({r.get('project_desc', '')})"
    print(f"[分析] 方式={r['mode']} 强度={strength} 总行={r['total_lines']} 分析范围={r['scope_lines']} "
          f"ERROR={r['err_all']} WARN={r['warn_all']} 工程={proj}")


if __name__ == "__main__":
    main()
