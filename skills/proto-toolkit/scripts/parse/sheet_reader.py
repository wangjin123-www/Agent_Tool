# -*- coding: utf-8 -*-
"""三表解析：Service Interface + Data Structure + Parameter Enum → Protocol 模型。

解析规则来源：飞书「AI修订规则」子表（规则 17/25/26/29 等）与实测表结构：
  SI：三级表头（R1 中文 / R3 英文 / R5 Param 子表头），数据从 si_data_start_row 起；
      分节行 = E 列以 '▶' 开头（仅排版分组用，不是方向真源）；
      接口方向真源 = msg_id bit15（0x8000=MCU→SOC / 0=SOC→MCU）；
      A~D 服务四列被纵向合并覆盖，首行带值、后续为空 → 语义 fill-down；
      接口行 = E 非空且非分节；参数行 = E 空 且 N/O 非空（挂在当前接口下）。
  DS：C 列非空起新 struct；成员行 J 非空；H 列字节区间 '0B'/'0-3B'/'4-NB'。
  PE：A 列非空起新枚举（合并单元格首行带值），B/C/D 为值/常量名/描述。

覆盖率对账（校验手段 A）：任何「行有内容但没进模型」的情况都记入
proto.source.parse_stats.*.skipped（行号 + 原因），sync 的 COV 规则汇总告警，
杜绝静默丢行 / 错列读空 / 截断。
"""
from ..common import conf, feishu
from ..model import Protocol, Service, Interface, Param, Struct, Member, Enum, EnumItem


# ------------------------------------------------------------------ 工具
def hex_int(text):
    """'0x0801' / '0801' / '129' → int；空/非法 → None。"""
    t = (text or "").strip()
    if not t:
        return None
    try:
        return int(t, 16) if t.lower().startswith("0x") else int(t, 16 if any(c in "abcdefABCDEF" for c in t) else 10)
    except ValueError:
        return None


def parse_byte_index(text):
    """'0B'→(0,0,False) / '0-3B'→(0,3,False) / '4-NB'→(4,None,True)；非法 → None。"""
    t = (text or "").upper().replace(" ", "").replace("BYTE", "").replace("B", "")
    if not t or not t[0].isdigit():
        return None
    try:
        if "-" in t:
            a, b = t.split("-", 1)
            start = int(a)
            if b in ("N", ""):
                return (start, None, True)
            return (start, int(b), False)
        v = int(t)
        return (v, v, False)
    except ValueError:
        return None


def pe_row_names(cfg, pe_rows):
    """PE A 列非空即枚举名首行 → {行号: 枚举名}（链接解析用，不依赖 parse_pe 顺序）。"""
    col = cfg["pe_columns"]["enum_type"]
    out = {}
    for r in range(2, len(pe_rows) + 1):
        txt = feishu.cell_text(feishu.cell_at(pe_rows, r, col))
        if txt:
            out[r] = txt
    return out


def link_enum_ref(cfg, cell, names):
    """单元格内链 → 枚举名：只认指向 PE 枚举名首行（A 列）的链接。

    SI P / DS K 也挂错误码表链接（E6），靠目标 sheet 与目标列过滤掉。
    """
    if not names:
        return ""
    sheet, a1 = feishu.decode_url(feishu.cell_link(cell))
    if sheet != cfg["sheets"]["parameter_enum"]["id"] or not a1:
        return ""
    try:
        ci, ri = conf.parse_a1(a1)
    except ValueError:
        return ""
    if ci != conf.col_index(cfg["pe_columns"]["enum_type"]):
        return ""
    return names.get(ri, "")


def _dir_of(cfg, text):
    """分节行文案 → 方向常量；非分节文案返回 None。"""
    t = (text or "").strip()
    if not t.startswith(cfg["section"]["marker"]):
        return None
    if t == cfg["section"]["soc_to_mcu"] or "SOC → MCU" in t:
        return "SOC_TO_MCU"
    if t == cfg["section"]["mcu_to_soc"] or "MCU → SOC" in t:
        return "MCU_TO_SOC"
    return None


# ------------------------------------------------------------------ SI
def parse_si(cfg, rows, proto, en_names=None):
    cols = cfg["si_columns"]
    start = cfg["si_data_start_row"]
    stats = proto.source["parse_stats"]["si"]
    en_names = en_names or {}
    cur_service = None
    cur_direction = None
    cur_itf = None

    for rownum in range(start, len(rows) + 1):
        c = {k: feishu.cell_text(feishu.cell_at(rows, rownum, v)) for k, v in cols.items()}
        if not any(c.values()):
            continue
        stats["rows"] += 1
        # 枚举引用真源 = P 列内链（指向 PE 枚举名首行），与错误码链接共存靠目标过滤
        en_ref = link_enum_ref(cfg, feishu.cell_at(rows, rownum, cols["param_desc"]), en_names)

        e_text = c["if_name"]
        direction = _dir_of(cfg, e_text)
        if direction is not None:
            cur_direction = direction
            cur_itf = None          # 分节行终结上一接口的参数区
            # 空服务块：A~D 合并值可能落在本行，仍走下面的服务判定
        elif e_text.startswith(cfg["section"]["marker"]):
            stats["skipped"].append(
                (rownum, "分节行文案无法识别方向：%r（不产数据，A~D 服务值若在此行会丢）" % e_text))
            continue
        elif e_text:
            cur_itf = None          # 新接口行终结上一接口的参数区

        # A~D fill-down：带值即切换/确立当前服务上下文
        if c["service_name"] or c["service_id"]:
            sid = hex_int(c["service_id"])
            if cur_service is None or (c["service_name"] and c["service_name"] != cur_service.name) \
               or (sid is not None and cur_service.id is not None and sid != cur_service.id):
                cur_service = Service()
                cur_service.name = c["service_name"]
                cur_service.id = sid
                cur_service.desc = c["service_desc"]
                cur_service.namespace = c["namespace"]
                cur_service.si_row = rownum
                proto.services.append(cur_service)
            elif not cur_service.name:
                cur_service.name = c["service_name"]
            elif sid is not None and cur_service.id is None:
                cur_service.id = sid

        if direction is not None:
            continue                # 分节行不产数据

        if e_text:
            # 接口行
            itf = Interface()
            itf.name = e_text
            itf.desc = c["if_desc"]
            itf.type = c["if_type"]
            itf.tx_type = c["tx_type"]
            itf.msg_id = hex_int(c["msg_id"])
            # 方向真源 = msg_id bit15（0x8000=MCU→SOC / 0=SOC→MCU）；
            # 分节行只是排版分组，记入 section_dir 供 S03 排版校验用
            itf.section_dir = cur_direction
            itf.direction = ("MCU_TO_SOC" if itf.msg_id & 0x8000 else "SOC_TO_MCU") \
                if itf.msg_id is not None else cur_direction    # id 缺失时分节位置兜底（S02 会报）
            itf.pair_id = hex_int(c["pair_id"])
            itf.transport = c["transport"]
            itf.qos = c["qos"]
            itf.si_row = rownum
            if cur_service is None:
                cur_service = Service()
                cur_service.si_row = rownum
                proto.services.append(cur_service)
            cur_service.interfaces.append(itf)
            cur_itf = itf
            # 表里既有写法：接口行本身可携带第一个参数（N/O/P/Q 与 E 同行）
            if c["param_name"] or c["param_type"]:
                p = Param()
                p.name = c["param_name"]
                p.type = c["param_type"]
                p.desc = c["param_desc"]
                p.io = c["param_dir"]
                p.si_row = rownum
                p.enum_ref = en_ref
                itf.params.append(p)
        elif c["param_name"] or c["param_type"]:
            # 参数行（含规则 26 的 struct 行：N=struct 名 / O=struct）
            if cur_itf is None:
                stats["skipped"].append(
                    (rownum, "参数行无所属接口（E 列空且上方无接口行）：N=%r O=%r"
                     % (c["param_name"], c["param_type"])))
                continue
            p = Param()
            p.name = c["param_name"]
            p.type = c["param_type"]
            p.desc = c["param_desc"]
            p.io = c["param_dir"]
            p.si_row = rownum
            p.enum_ref = en_ref
            cur_itf.params.append(p)


# ------------------------------------------------------------------ DS
def parse_ds(cfg, rows, proto, en_names=None):
    cols = cfg["ds_columns"]
    stats = proto.source["parse_stats"]["ds"]
    en_names = en_names or {}
    cur = None
    for rownum in range(2, len(rows) + 1):
        c = {k: feishu.cell_text(feishu.cell_at(rows, rownum, v)) for k, v in cols.items()}
        if not any(c.values()):
            cur = None if not c["name"] else cur
            if not c["name"] and not c["member"]:
                continue
        stats["rows"] += 1
        if c["name"]:
            cur = Struct()
            cur.name = c["name"]
            cur.service = c["service_name"]
            cur.namespace = c["namespace"]
            cur.desc = c["desc"]
            cur.category = c["category"]
            cur.size = c["size"]
            cur.ds_row = rownum
            proto.structs.append(cur)
        if c["member"]:
            if cur is None:
                stats["skipped"].append(
                    (rownum, "成员行无所属 struct（C 列空或被空行切断）：J=%r" % c["member"]))
                continue
            # struct 首行可同时携带第一个成员（C=struct 名 + J=成员 同行）
            span = parse_byte_index(c["byte_index"])
            m = Member()
            m.name = c["member"]
            m.type = c["type"]
            m.desc = c["member_desc"]
            m.bit = c["bit"]
            m.ds_row = rownum
            # 成员枚举引用真源 = K 列内链（指向 PE 枚举名首行）
            m.enum_ref = link_enum_ref(
                cfg, feishu.cell_at(rows, rownum, cols["member_desc"]), en_names)
            if span is None:
                m.byte_start = m.byte_end = None
            else:
                m.byte_start, m.byte_end, m.open = span
            cur.members.append(m)


# ------------------------------------------------------------------ PE
def parse_pe(cfg, rows, proto):
    cols = cfg["pe_columns"]
    stats = proto.source["parse_stats"]["pe"]
    cur = None
    for rownum in range(2, len(rows) + 1):
        c = {k: feishu.cell_text(feishu.cell_at(rows, rownum, v)) for k, v in cols.items()}
        if not any(c.values()):
            continue
        stats["rows"] += 1
        if c["enum_type"]:
            cur = Enum()
            cur.name = c["enum_type"]
            cur.pe_row = rownum
            proto.enums.append(cur)
        elif c["c_name"] or c["value"]:
            if cur is None:
                stats["skipped"].append(
                    (rownum, "枚举值行无所属枚举（A 列空）：B=%r C=%r" % (c["value"], c["c_name"])))
                continue
            item = EnumItem()
            v = c["value"]
            try:
                item.value = int(str(v), 16) if str(v).strip().lower().startswith("0x") else int(float(str(v)))
            except ValueError:
                item.value = None
            item.c_name = c["c_name"]
            item.desc = c["desc"]
            cur.items.append(item)


# ------------------------------------------------------------------ 汇总
def parse_protocol(cfg=None, rows=None):
    """读三表 → Protocol（不写任何东西）。

    rows 可传已读好的 {"si": [...], "ds": [...], "pe": [...]} 复用（check 全流程
    只读一遍表）；缺哪张读哪张。
    """
    cfg = cfg or conf.proto()
    rows = rows or {}
    proto = Protocol()
    proto.source["spreadsheet"] = cfg["spreadsheet_name"]
    proto.source["spreadsheet_token"] = cfg["spreadsheet_token"]
    proto.source["revision"] = feishu.revision(cfg)
    proto.source["parse_stats"] = {          # 校验手段 A：覆盖率对账（COV 规则汇总）
        "si": {"rows": 0, "skipped": []},
        "ds": {"rows": 0, "skipped": []},
        "pe": {"rows": 0, "skipped": []},
    }

    si_rows = rows.get("si") or feishu.read(cfg, "service_interface", "Q")
    ds_rows = rows.get("ds") or feishu.read(cfg, "data_structure", "K")
    pe_rows = rows.get("pe") or feishu.read(cfg, "parameter_enum", "E")

    # 先建 PE 行号→枚举名映射：SI P / DS K 的内链目标只给行号，要靠它换名字
    en_names = pe_row_names(cfg, pe_rows)
    parse_si(cfg, si_rows, proto, en_names)
    parse_ds(cfg, ds_rows, proto, en_names)
    parse_pe(cfg, pe_rows, proto)
    return proto


def read_rule_sheet(cfg=None):
    """读「AI修订规则」子表原文（人读参考，不参与程序判定）。"""
    cfg = cfg or conf.proto()
    return feishu.read(cfg, "rule", "F")
