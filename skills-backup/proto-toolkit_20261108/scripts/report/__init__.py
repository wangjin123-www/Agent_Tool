# -*- coding: utf-8 -*-
"""检查结果 HTML 报告：每次校验完自动落一份人读报告。

规则：
  - 只有存在 ERR 或 WARN 才生成（INFO 不算），否则删掉旧报告，避免「看到上一次的旧错误」；
  - 按检查码分组，每组一张问题表 + 一张真实数据实例表（从当次 ctx 快照取，不重复判据）；
  - 自包含单文件，无外链资源，双击即可看。

产物：output/check_report.html
"""
import html
import os
import re
import time

from ..common import conf
from ..common.log import ERR, WARN

PATH = "output/check_report.html"        # 相对 SKILL_DIR

# 检查码 → (判据说明, 修法)。未登记的码只显示注册表里的标题。
_HINT = {
    "S01": ("服务 id 必须存在且全局唯一（SI B 列）", "补/改 SI B 列服务 id；重复的改号"),
    "S02": ("消息 id 必须存在且全局唯一（SI J 列）", "补 J 列或改掉重复号"),
    "S03": ("方向真源 = 消息 id 的 bit15（0x8000=MCU→SOC，0=SOC→MCU）",
            "调 id 高位；分节行已废弃，不再参与方向校验"),
    "S04": ("消息 id 高 8bit 必须等于服务 id", "改 J 列高位或改 B 列服务 id"),
    "S05": ("配对 id（SI K）必须双向互指：A 指向 B，B 必须回指 A",
            "给对端 K 列回填本端 id；event 类不应配对，K 列留空"),
    "S06": ("method(rr) 类型应填关联 id", "补 SI K 列，或把类型改成 event/method"),
    "S07": ("struct 名全局唯一（DS C 列）", "重命名重复的 struct"),
    "S08": ("参数/成员引用的 struct 必须存在于 Data Structure", "先 add-struct 定义，再引用"),
    "S09": ("参数/成员引用的枚举必须存在于 Parameter Enum", "先 add-enum 定义，再引用"),
    "S10": ("枚举值合法、常量名全局唯一（PE B/C 列）", "按 0xNN 填 B 列，C 列全大写且不与其他枚举重名"),
    "S11": ("struct 成员字节序号必须从 0 连续、无空洞、无重叠、尾成员开放（DS G 列）",
            "补缺的字节区间或改起点，开放尾只能放最后一个成员"),
    "S12": ("struct Size（DS F 列）必须等于成员实际占用", "按实占字节改 F 列，开放尾写成 N+N"),
    "S13": ("成员类型与字节跨度/位宽必须自洽", "uint8 占 1B、uint16 占 2B、uint32 占 4B；位宽不得超跨度"),
    "S14": ("开放尾（NB）必须是最后一个成员且类型为 uint8[]", "调整成员顺序或改类型"),
    "S15": ("接口元数据必填：发送类型 H / 传输层 L / QoS M", "补齐 H、L、M 三列"),
    "S16": ("参数值域必须放 Parameter Enum，SI P 列只留中文描述 + 枚举链接",
            "先 add-enum 建枚举，参数改 type=enum:枚举名，P 列删掉内联值域"),
    "S17": ("同一接口有 2 个及以上标量参数时，应建 struct 单行引用（规则 8/9/26）",
            "先 add-struct，再用一个 type=struct:名 参数替换这些标量参数"),
    "R23": ("枚举取值必须是 0xNN 两位大写十六进制，常量名全大写且全局唯一",
            "按 0xNN 改写，重命名撞名的常量"),
    "LNK": ("链接一律按主键（struct 名 / 枚举首行 / 接口行）重算，不存绝对 URL",
            "sync 非 dry-run 会自动重写；无引用源的枚举会被跳过（先让它被 SI P 或 DS K 引用）"),
    "STY": ("枚举块 A~E 统一 10pt + 细边框 + 对齐", "sync 非 dry-run 自动补齐"),
    "MERGE": ("SI 每个服务块的 A~D 列必须纵向合并", "sync 非 dry-run 按块重做合并"),
    "SEC": ("分节行规则已废弃（方向真源=msg_id bit15）", "忽略；表内不应再有 ▶ 分节行"),
    "COV": ("解析覆盖率对账：三表里「有内容但没进模型」的行会被点名", "按行号补字段或修正错列"),
    "RUL": ("规则表序号 ↔ 代码检查项的覆盖对账", "属流程约束可忽略；若有对应检查需求则补 Register"),
}

_FALLBACK_TITLE = "检查项"

# 语义检查码的短标题（S01~S17 由 SEM 统一产出，不在规则注册表里，需自带名字）
_NAME = {
    "S01": "服务 id 唯一", "S02": "消息 id 唯一", "S03": "方向位与分节排版",
    "S04": "消息 id 高 8bit 对账", "S05": "配对双向互指", "S06": "method 缺配对",
    "S07": "struct 名唯一", "S08": "struct 引用存在", "S09": "枚举引用存在",
    "S10": "枚举名/常量名唯一", "S11": "字节区间连续", "S12": "struct Size 对账",
    "S13": "类型与字节/位宽自洽", "S14": "开放尾成员位置", "S15": "接口元数据必填",
    "S16": "参数值域应建枚举", "S17": "复合参数应建 struct",
}

_CSS = """
:root{--bg:#f6f7f9;--card:#fff;--txt:#1f2329;--dim:#646a73;--line:#e5e6eb;
--err:#d4380d;--errbg:#fff1e8;--warn:#ad6800;--warnbg:#fffbe6;--ok:#237804}
*{box-sizing:border-box}
body{margin:0;padding:32px 24px 64px;background:var(--bg);color:var(--txt);
font:14px/1.6 -apple-system,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif}
.wrap{max-width:1180px;margin:0 auto}
h1{font-size:22px;margin:0 0 4px}
.sub{color:var(--dim);font-size:13px;margin-bottom:20px}
.cards{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:22px}
.card{background:var(--card);border:1px solid var(--line);border-radius:8px;
padding:12px 18px;min-width:120px}
.card .n{font-size:22px;font-weight:600;line-height:1.2}
.card .k{font-size:12px;color:var(--dim)}
.card.err .n{color:var(--err)}.card.warn .n{color:var(--warn)}.card.ok .n{color:var(--ok)}
.toc{background:var(--card);border:1px solid var(--line);border-radius:8px;
padding:14px 18px;margin-bottom:22px}
.toc a{display:inline-block;margin:0 14px 6px 0;color:#0958d9;text-decoration:none;
font-size:13px;font-family:ui-monospace,Consolas,monospace}
.toc a:hover{text-decoration:underline}
section{background:var(--card);border:1px solid var(--line);border-radius:8px;
padding:18px 20px 20px;margin-bottom:18px}
h2{font-size:16px;margin:0 0 10px;display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.code{font-family:ui-monospace,Consolas,monospace;background:#eef1f5;border-radius:4px;
padding:1px 7px;font-size:13px}
.badge{font-size:12px;border-radius:10px;padding:1px 9px;font-weight:500}
.badge.err{background:var(--errbg);color:var(--err)}
.badge.warn{background:var(--warnbg);color:var(--warn)}
.hint{margin:0 0 4px;font-size:13px;color:var(--dim)}
.hint b{color:var(--txt);font-weight:600}
h3{font-size:13px;color:var(--dim);font-weight:600;margin:16px 0 8px;
letter-spacing:.3px;text-transform:uppercase}
table{width:100%;border-collapse:collapse;font-size:13px}
th,td{border:1px solid var(--line);padding:6px 9px;text-align:left;vertical-align:top}
th{background:#f2f4f7;font-weight:600;font-size:12px;color:#333;white-space:nowrap}
td.num{color:var(--dim);width:38px;text-align:right}
td.lv{white-space:nowrap;width:52px;font-weight:600}
td.lv.err{color:var(--err)}td.lv.warn{color:var(--warn)}
td.miss{background:var(--errbg);color:var(--err);font-weight:600}
.mono{font-family:ui-monospace,Consolas,monospace}
footer{color:var(--dim);font-size:12px;text-align:center;margin-top:28px}
"""


def _esc(v):
    return html.escape("" if v is None else str(v))


def _titles():
    """检查码 → 标题：语义码取自带短名，其余复用规则注册表，不另存一份。"""
    names = dict(_NAME)
    try:
        from ..rules import RULES
        for r in RULES:
            names.setdefault(r.id, r.title)
    except Exception:                       # 注册表导入失败不应影响出报告
        pass
    return names


# --------------------------------------------------------------- 实例数据
def _hit_names(msg, proto):
    """从问题文案里认出涉及的对象（接口全名优先，其次 struct / 枚举名）。"""
    itfs, structs, enums = [], [], []
    rest = msg
    for s in proto.services:
        for itf in s.interfaces:
            full = "%s.%s" % (s.name, itf.name)
            if full in rest:
                itfs.append(itf)
                rest = rest.replace(full, " ")     # 已认出的接口名不再参与后续匹配
    if not itfs:                            # 文案里只有短名时兜底
        for s in proto.services:
            for itf in s.interfaces:
                if len(itf.name) >= 6 and itf.name in rest:
                    itfs.append(itf)
                    rest = rest.replace(itf.name, " ")
    for st in proto.structs:
        if st.name and len(st.name) >= 3 and st.name in rest:
            structs.append(st)
    for e in proto.enums:
        if e.name and len(e.name) >= 3 and e.name in rest:
            enums.append(e)
    return itfs, structs, enums


def _cell(v, flag=False):
    if v in (None, "", []):
        return '<td class="miss">（空）</td>' if flag else "<td>—</td>"
    return "<td>%s</td>" % _esc(v)


def _hex(v, width=4):
    return ("0x%0*X" % (width, v)) if isinstance(v, int) else ""


def _peer(proto, pair_id):
    if pair_id is None:
        return None
    for s in proto.services:
        for p in s.interfaces:
            if p.msg_id == pair_id:
                return p
    return None


def _itf_rows(proto, rows, seen):
    """接口字段明细：把判定相关的列全摊开，空列标红（列数与表头严格一致）。"""
    out = []
    for itf in rows:
        if id(itf) in seen:
            continue
        seen.add(id(itf))
        peer = _peer(proto, itf.pair_id)
        out.append(
            "<tr><td class='mono'>%s</td><td class='mono'>%s</td><td class='mono'>%s</td>"
            "<td>%s</td>%s%s%s<td class='mono'>%s</td><td class='mono'>%s</td>"
            "<td>%d</td></tr>" % (
                _esc(itf.name), _esc(_hex(itf.msg_id)),
                _esc("MCU→SOC" if (itf.msg_id or 0) & 0x8000 else "SOC→MCU"),
                _esc(itf.type or ""),
                _cell(itf.tx_type, True), _cell(itf.transport, True), _cell(itf.qos, True),
                _esc(_hex(itf.pair_id) or "—"),
                _esc(_hex(peer.pair_id) if peer and peer.pair_id is not None else "空"),
                len(itf.params)))
    return out


def _itf_table(proto, itfs):
    if not itfs:
        return ""
    seen = set()
    body = _itf_rows(proto, itfs, seen)
    if not body:
        return ""
    return ("<h3>实例数据 · 接口</h3><table><thead><tr><th>接口</th><th>消息id</th>"
            "<th>方向(bit15)</th><th>类型</th><th>发送类型H</th><th>传输层L</th><th>QoS M</th>"
            "<th>配对K</th><th>对端回指</th><th>参数数</th></tr></thead><tbody>%s</tbody></table>"
            % "".join(body))


def _struct_table(structs, seen):
    out = ["<h3>实例数据 · struct 成员</h3>",
           "<table><thead><tr><th>struct</th><th>成员</th><th>字节</th><th>bit</th>"
           "<th>类型</th><th>描述</th></tr></thead><tbody>"]
    n = 0
    for st in structs:
        if id(st) in seen:
            continue
        seen.add(id(st))
        if not st.members:
            out.append("<tr><td class='mono'>%s</td><td colspan='5' class='miss'>"
                       "（无成员）</td></tr>" % _esc(st.name))
            continue
        for m in st.members[:8]:
            n += 1
            span = ("%d-NB" % m.byte_start) if m.open else (
                "%d" % m.byte_start if m.byte_end == m.byte_start
                else "%d-%dB" % (m.byte_start, m.byte_end))
            out.append("<tr><td class='mono'>%s</td><td>%s</td><td class='mono'>%s</td>"
                       "<td class='mono'>%s</td><td>%s</td><td>%s</td></tr>"
                       % (_esc(st.name), _esc(m.name), _esc(span), _esc(m.bit or "—"),
                          _esc(m.type), _esc(m.desc or "")))
        if len(st.members) > 8:
            out.append("<tr><td class='mono'>%s</td><td colspan='5'>… 另有 %d 个成员</td></tr>"
                       % (_esc(st.name), len(st.members) - 8))
    out.append("</tbody></table>")
    return "".join(out) if n or len(structs) else ""


def _enum_table(enums, seen):
    out = ["<h3>实例数据 · 枚举取值</h3>",
           "<table><thead><tr><th>枚举</th><th>PE行</th><th>取值</th><th>C 常量</th>"
           "<th>描述</th></tr></thead><tbody>"]
    n = 0
    for e in enums:
        if id(e) in seen:
            continue
        seen.add(id(e))
        if not e.items:
            out.append("<tr><td class='mono'>%s</td><td>—</td><td colspan='3' class='miss'>"
                       "（无取值）</td></tr>" % _esc(e.name))
            continue
        for it in e.items[:8]:
            n += 1
            out.append("<tr><td class='mono'>%s</td><td class='mono'>A%s</td>"
                       "<td class='mono'>%s</td><td>%s</td><td>%s</td></tr>"
                       % (_esc(e.name), _esc(e.pe_row or "—"), _esc(_hex(it.value, 2)),
                          _esc(it.c_name or ""), _esc(it.desc or "")))
        if len(e.items) > 8:
            out.append("<tr><td class='mono'>%s</td><td colspan='4'>… 另有 %d 个取值</td></tr>"
                       % (_esc(e.name), len(e.items) - 8))
    out.append("</tbody></table>")
    return "".join(out) if n or len(enums) else ""


_A1 = re.compile(r"SI!([A-Z]{1,2})(\d+)")


def _si_cell_table(ctx, msgs):
    """问题文案里点了 SI!P20 这类坐标的，直接把该格真实内容摊出来。"""
    from ..common import feishu
    hits = []
    for _lv, msg in msgs:
        for col, row in _A1.findall(msg):
            key = (col, int(row))
            if key not in hits:
                hits.append(key)
    if not hits:
        return ""
    out = ["<h3>实例数据 · 问题单元格</h3>",
           "<table><thead><tr><th>坐标</th><th>当前内容</th><th>所在接口</th>"
           "</tr></thead><tbody>"]
    for col, row in hits:
        text = feishu.cell_text(feishu.cell_at(ctx.si, row, col))
        owner = ""
        for s in ctx.proto.services:
            for itf in s.interfaces:
                if itf.si_row is not None and itf.si_row <= row <= itf.si_row + len(itf.params):
                    owner = "%s.%s" % (s.name, itf.name)
        flag = " class='miss'" if not text else ""
        out.append("<tr><td class='mono'>%s!%s%d</td><td%s>%s</td><td>%s</td></tr>"
                   % (_esc("SI"), _esc(col), row, flag,
                      _esc(text) if text else "（空）", _esc(owner or "—")))
    out.append("</tbody></table>")
    return "".join(out)


def _evidence(ctx, msgs, code=""):
    """该检查码涉及的对象的真实数据表（仅展示，不重复判定）。"""
    itfs, structs, enums = [], [], []
    for _lv, msg in msgs:
        a, b, c = _hit_names(msg, ctx.proto)
        itfs += a
        structs += b
        enums += c
    if code in ("S05", "S06", "S03", "S04"):
        for itf in list(itfs):              # 配对/方向类问题把对端也摊出来
            peer = _peer(ctx.proto, itf.pair_id)
            if peer is not None:
                itfs.append(peer)
    seen = set()
    return (_itf_table(ctx.proto, itfs) + _struct_table(structs, seen)
            + _enum_table(enums, seen) + _si_cell_table(ctx, msgs))


# --------------------------------------------------------------- 主渲染
def render(rep, ctx, produced_at=None):
    errs = [r for r in rep.rows if r[0] == ERR]
    warns = [r for r in rep.rows if r[0] == WARN]
    titles = _titles()

    groups, index = [], {}
    for level, code, msg in rep.rows:
        if level not in (ERR, WARN):
            continue
        if code not in index:
            index[code] = len(groups)
            groups.append((code, []))
        groups[index[code]][1].append((level, msg))

    c = ctx.proto.counts()
    toc = "".join(
        '<a href="#%s">%s · %s（%d）</a>' % (
            _esc(code), _esc(code), _esc(titles.get(code) or _FALLBACK_TITLE), len(msgs))
        for code, msgs in groups)

    parts = [
        "<!DOCTYPE html><html lang='zh-CN'><head><meta charset='utf-8'>",
        "<meta name='viewport' content='width=device-width,initial-scale=1'>",
        "<title>协议表检查报告</title><style>%s</style></head><body><div class='wrap'>" % _CSS,
        "<h1>协议表检查报告</h1>",
        "<div class='sub'>生成时间 %s ｜ revision=%s ｜ %d 服务 / %d 接口 / %d struct / %d 枚举</div>"
        % (_esc(produced_at or time.strftime("%Y-%m-%d %H:%M:%S")),
           _esc(ctx.proto.source.get("revision", "—")),
           c["services"], c["interfaces"], c["structs"], c["enums"]),
        "<div class='cards'>",
        "<div class='card err'><div class='n'>%d</div><div class='k'>错误</div></div>" % len(errs),
        "<div class='card warn'><div class='n'>%d</div><div class='k'>告警</div></div>" % len(warns),
        "<div class='card ok'><div class='n'>%d</div><div class='k'>通过</div></div>"
        % rep.count("OK"),
        "<div class='card'><div class='n'>%d</div><div class='k'>检查项</div></div>" % len(groups),
        "</div>",
        "<div class='toc'>%s</div>" % toc,
    ]

    for code, msgs in groups:
        n_err = sum(1 for lv, _m in msgs if lv == ERR)
        n_warn = sum(1 for lv, _m in msgs if lv == WARN)
        badges = ""
        if n_err:
            badges += "<span class='badge err'>%d 错误</span>" % n_err
        if n_warn:
            badges += "<span class='badge warn'>%d 告警</span>" % n_warn
        hint = _HINT.get(code, ("", ""))
        parts.append("<section id='%s'><h2><span class='code'>%s</span>%s%s</h2>"
                     % (_esc(code), _esc(code),
                        _esc(titles.get(code) or _FALLBACK_TITLE), badges))
        if hint[0]:
            parts.append("<p class='hint'><b>判据</b>：%s</p>" % _esc(hint[0]))
        if hint[1]:
            parts.append("<p class='hint'><b>修法</b>：%s</p>" % _esc(hint[1]))
        parts.append("<h3>问题清单</h3><table><thead><tr><th>#</th><th>级别</th>"
                     "<th>问题</th></tr></thead><tbody>")
        for i, (level, msg) in enumerate(msgs, 1):
            lv = "err" if level == ERR else "warn"
            parts.append("<tr><td class='num'>%d</td><td class='lv %s'>%s</td><td>%s</td></tr>"
                         % (i, lv, "错误" if level == ERR else "告警", _esc(msg)))
        parts.append("</tbody></table>")
        parts.append(_evidence(ctx, msgs, code))
        parts.append("</section>")

    parts.append("<footer>proto-toolkit · 由 cli.py sync / edit apply 自动生成，"
                 "无错误与告警时不生成</footer></div></body></html>")
    return "".join(p for p in parts if p)


def emit(rep, ctx, path=None):
    """有 ERR/WARN 时写报告并返回路径；否则删除旧报告并返回 None。"""
    has_issue = any(r[0] in (ERR, WARN) for r in rep.rows)
    target = conf.output_path(path or PATH)
    if not has_issue:
        if os.path.exists(target):
            os.remove(target)
        return None
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(render(rep, ctx))
    return target
