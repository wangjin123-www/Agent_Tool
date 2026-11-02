# -*- coding: utf-8 -*-
"""语义校验：不碰表格，只对 Protocol 模型判定（检查清单源自 codegen-plan 蓝本）。

  S01 服务 id 唯一且非空          S02 消息 id 全局唯一
  S03 分节排版与方向位一致（WARN，真源=id bit15）
  S04 消息 id 高 8bit 与服务 id 对账
  S05 配对 id 双向互指            S06 method(rr) 应有配对（WARN）
  S07 struct 名唯一               S08 SI 参数类型命中 DS（struct 引用）
  S09 DS 成员/参数类型中枚举命中 PE S10 枚举名与常量名全局唯一
  S11 DS 字节区间无重叠无空洞      S12 DS Size 对账
  S13 位宽匹配标量类型            S14 开放尾成员必须是末成员 uint8[]
  S15 接口缺 transport/qos/tx_type（WARN）

S17 复合参数未建 struct 已迁至 scripts/rules/basic.py（那里带 fix，能生成 edit_request）。
"""
from ..common.log import Report
from ..model import Struct

_SCALAR_BYTES = {"uint8": 1, "uint8_t": 1, "int8": 1, "uint16": 2, "uint16_t": 2,
                 "int16": 2, "uint32": 4, "uint32_t": 4, "int32": 4}


def resolve_type(proto, raw, param_name="", enum_ref=""):
    """类型文本 → ('struct', name) / ('enum', name) / ('scalar', raw) / ('?', raw)。

    enum_ref 非空（SI P / DS K 内链命中 PE）时优先判 enum：表里这类参数 O 列写的是
    uint8 基线类型，枚举关联只体现在描述列链接上，单看 type 文本永远判不出来。
    """
    t = (raw or "").strip()
    low = t.lower()
    if enum_ref:
        return ("enum", enum_ref.strip())
    if not t:
        return ("?", t)
    if low == "struct":
        return ("struct", param_name.strip())
    if low.startswith("struct:"):
        return ("struct", t[7:].strip())
    if low.startswith("enum:"):
        return ("enum", t[5:].strip())
    if low in _SCALAR_BYTES or low == "uint8[]":
        return ("scalar", t)
    if proto.find_struct(t) is not None:
        return ("struct", t)
    if proto.find_enum(t) is not None:
        return ("enum", t)
    return ("?", t)


def validate(proto):
    rep = Report("语义校验")
    _services(proto, rep)
    _structs(proto, rep)
    _enums(proto, rep)
    _cross(proto, rep)
    return rep


def _services(proto, rep):
    seen_sid = {}
    seen_mid = {}
    for s in proto.services:
        if s.id is None:
            if s.interfaces:
                rep.err("S01", "服务 %s 缺服务 id（SI B 列）" % s.name)
        elif s.id in seen_sid:
            rep.err("S01", "服务 id 重复 0x%02X：%s 与 %s" % (s.id, seen_sid[s.id], s.name))
        else:
            seen_sid[s.id] = s.name
            rep.ok("S01", "服务 %s = 0x%02X" % (s.name, s.id))

        for itf in s.interfaces:
            tag = "%s.%s" % (s.name, itf.name)
            if itf.msg_id is None:
                rep.err("S02", "%s 消息 id 为空/非法（SI J 列）" % tag)
                continue
            if itf.msg_id in seen_mid:
                rep.err("S02", "消息 id 重复 0x%04X：%s 与 %s"
                        % (itf.msg_id, seen_mid[itf.msg_id], tag))
            else:
                seen_mid[itf.msg_id] = tag
            # S03 排版一致性：方向真源 = id bit15（0x8000=MCU→SOC / 0=SOC→MCU）；
            # 分节行只是排版分组，方向位与所在分节不符只算排版问题（WARN）
            want_dir = "MCU_TO_SOC" if itf.msg_id & 0x8000 else "SOC_TO_MCU"
            if itf.direction != want_dir:
                rep.warn("S03", "%s id=0x%04X 方向位为 %s（真源），解析兜底 %s 异常"
                         % (tag, itf.msg_id, want_dir, itf.direction))
            elif not itf.section_dir:
                rep.warn("S03", "%s 未落在任何方向分节下" % tag)
            elif itf.section_dir != want_dir:
                rep.warn("S03", "%s id=0x%04X 方向位为 %s，却排在 %s 分节下（仅排版问题）"
                         % (tag, itf.msg_id, want_dir, itf.section_dir))
            # S04 服务号
            high = (itf.msg_id >> 8) & 0x7F
            if s.id is not None and high != s.id:
                rep.err("S04", "%s id=0x%04X 高 8bit=0x%02X 与服务 id 0x%02X 不符"
                        % (tag, itf.msg_id, high, s.id))
            # S05/S06 配对
            if itf.pair_id is not None:
                peer = proto.find_interface(itf.pair_id)
                if peer is None:
                    rep.err("S05", "%s 配对 id 0x%04X 查无此消息" % (tag, itf.pair_id))
                elif peer.pair_id != itf.msg_id:
                    rep.err("S05", "%s → 0x%04X 单向指配（对方回指 %s）"
                            % (tag, itf.pair_id, "0x%04X" % peer.pair_id if peer.pair_id is not None else "空"))
                elif (itf.pair_id ^ itf.msg_id) != 0x8000:
                    rep.warn("S05", "%s 配对 0x%04X 非 ^0x8000 关系" % (tag, itf.pair_id))
            elif "rr" in (itf.type or ""):
                rep.warn("S06", "%s 类型 %s 但未填关联 id（SI K 列）" % (tag, itf.type))
            # S15 元数据
            miss = [k for k, v in (("传输层", itf.transport), ("QoS", itf.qos),
                                   ("发送类型", itf.tx_type)) if not v]
            if miss:
                rep.warn("S15", "%s 缺%s" % (tag, "/".join(miss)))


def _structs(proto, rep):
    names = set()
    for st in proto.structs:
        if st.name in names:
            rep.err("S07", "struct 名重复 %s" % st.name)
        names.add(st.name)
        if not st.members:
            rep.warn("S11", "struct %s 无成员" % st.name)
            continue
        # S11/S12/S13/S14
        covered = {}
        for idx, m in enumerate(st.members):
            if m.byte_start is None and not m.open:
                rep.err("S11", "%s.%s 字节序号非法（DS H 列）" % (st.name, m.name))
                continue
            if m.open:
                if idx != len(st.members) - 1:
                    rep.err("S14", "%s.%s 开放尾成员必须是最后一个成员" % (st.name, m.name))
                if "uint8" not in (m.type or "") or "[" not in (m.type or ""):
                    rep.warn("S14", "%s.%s 开放尾类型建议 uint8[]（现 %s）" % (st.name, m.name, m.type))
                continue
            for b in range(m.byte_start, m.byte_end + 1):
                if b in covered:
                    rep.err("S11", "%s 字节 %d 重叠：%s 与 %s"
                            % (st.name, b, covered[b], m.name))
                covered[b] = m.name
            nb = m.byte_end - m.byte_start + 1
            want = _SCALAR_BYTES.get((m.type or "").lower().replace("_t", ""))
            if want and not m.bit:
                if nb != want:
                    rep.err("S13", "%s.%s 占 %dB 但类型 %s 应 %dB"
                            % (st.name, m.name, nb, m.type, want))
            if m.bit:
                # 位宽与字节跨度对账：0-7bit→1B / 0-15bit→2B / 0-31bit→4B；
                # 非整字节位域（如 3bit）只要求 width ≤ nb*8
                bits = _bit_width(m.bit)
                if bits is None:
                    rep.warn("S13", "%s.%s bit 列 %r 无法解析" % (st.name, m.name, m.bit))
                elif bits > nb * 8:
                    rep.err("S13", "%s.%s bit 宽 %d 超出 %dB 跨度" % (st.name, m.name, bits, nb))
                elif bits == nb * 8 and nb > 1:
                    pass          # 整数倍字节成员（0-15bit/uint16 等），合法
                elif nb > 1:
                    rep.warn("S13", "%s.%s 跨 %dB 但位宽仅 %d（有填充位）" % (st.name, m.name, nb, bits))
        # 空洞检测（只查 0..max 封闭区）
        if covered:
            mx = max(covered)
            holes = [b for b in range(0, mx + 1) if b not in covered]
            if holes:
                rep.warn("S11", "%s 字节空洞：%s" % (st.name, ",".join("%dB" % b for b in holes)))
            # S12 Size 对账
            num = _leading_number(st.size)
            if num is not None and num != mx + 1 and not st.has_open:
                rep.err("S12", "%s Size=%s 但成员实占 %dB" % (st.name, st.size, mx + 1))
            elif num is not None and st.has_open and num != st.fixed_bytes:
                rep.warn("S12", "%s Size=%s 开放尾按封闭 %dB 对账不符"
                         % (st.name, st.size, st.fixed_bytes))


def _enums(proto, rep):
    seen_type = set()
    seen_cname = {}
    for e in proto.enums:
        if e.name in seen_type:
            rep.err("S10", "枚举类型名重复 %s" % e.name)
        seen_type.add(e.name)
        for it in e.items:
            if it.value is None:
                rep.err("S10", "%s.%s 值非法（PE B 列）" % (e.name, it.c_name))
            if not it.c_name:
                rep.warn("S10", "%s 存在无 C 常量名的项" % e.name)
                continue
            if it.c_name in seen_cname:
                rep.err("S10", "枚举常量名全局重复 %s（%s / %s）"
                        % (it.c_name, seen_cname[it.c_name], e.name))
            seen_cname[it.c_name] = e.name


def _cross(proto, rep):
    # S08 SI 参数 struct 引用 + S09 枚举引用（enum_ref = P 列内链，优先于 type 文本）
    for s in proto.services:
        for itf in s.interfaces:
            for p in itf.params:
                kind, name = resolve_type(proto, p.type, p.name, p.enum_ref)
                tag = "%s.%s(%s)" % (itf.name, p.name, p.type)
                if kind == "struct" and proto.find_struct(name) is None:
                    rep.err("S08", "%s 引用 struct %s 不在 Data Structure" % (tag, name))
                elif kind == "enum" and proto.find_enum(name) is None:
                    rep.err("S09", "%s 引用枚举 %s 不在 Parameter Enum" % (tag, name))
                elif kind == "?":
                    rep.warn("S08", "%s 类型无法归类（非标量/非已知 struct/enum）" % tag)
    # DS 成员类型里的枚举引用（enum_ref = K 列内链）
    for st in proto.structs:
        for m in st.members:
            t = (m.type or "").strip()
            if m.enum_ref:
                if proto.find_enum(m.enum_ref) is None:
                    rep.err("S09", "%s.%s 引用枚举 %s 不在 Parameter Enum"
                            % (st.name, m.name, m.enum_ref))
                continue
            if not t or t.lower() in _SCALAR_BYTES or t.lower() == "uint8[]":
                continue
            if proto.find_struct(t) is not None:
                continue
            if proto.find_enum(t) is not None:
                continue
            rep.warn("S09", "%s.%s 类型 %s 未命中 DS/PE" % (st.name, m.name, t))


def _bit_width(bit_text):
    """'0-7bit'/'0-15bit'/'4' → 位宽；空 → None。"""
    t = (bit_text or "").strip().replace(" ", "").lower().rstrip("bit")
    if not t:
        return None
    try:
        if "-" in t:
            a, b = t.split("-", 1)
            return abs(int(b) - int(a)) + 1
        return 1
    except ValueError:
        return None


def _leading_number(size_text):
    t = (size_text or "").strip()
    num = ""
    for ch in t:
        if ch.isdigit():
            num += ch
        elif num:
            break
    return int(num) if num else None
