# -*- coding: utf-8 -*-
"""pull：飞书多维表格 → output/protocol.json（git 提交，可 diff 的协议快照）。

链路（v4）：
    多维表格 ──① pull──▶ protocol.json（git）──② gen──▶ C 代码

设计约定（沿用 v2 的 protocol.json 契约并适配 Bitable）：
  1. 数组稳定排序：interfaces 按 msg_id，structs/enums/services/errors 按名称，
     成员按字节序号——表内行序变化不影响 diff；
  2. 不存 record_id / 反向 index（运行时可重建，id 属平台内部坐标，diff 噪声）；
  3. 不含时间戳：表没动，重复 pull 产物逐字节相同（git diff 干净）；
  4. 每个实体带 check 字段 = 多维表格「XX正常性检测」公式原文：
     ❌=违规（gen 阻断）、⚠️=警告（提示不阻断）、✅/空=通过；
  5. msg_id / 枚举值 解析为 int 并同时存 0x 十六进制串。
"""
import json
import os
import re

from .common import conf

SCHEMA_VERSION = "4.0.0"
PROTO_JSON = "protocol.json"


class PullError(RuntimeError):
    pass


# ------------------------------------------------------------------ 值解析
def parse_int(t):
    """'0x0801'/'0801'/'129' → int；无法解析返回 None。"""
    s = (t or "").strip()
    if not s:
        return None
    try:
        if s.lower().startswith("0x"):
            return int(s, 16)
        return int(s, 10)
    except ValueError:
        pass
    if re.fullmatch(r"[0-9A-Fa-f]{1,8}", s):        # '0801' 视为十六进制
        return int(s, 16)
    return None


def to_hex(v, width=4):
    return "0x%0*X" % (width, v)


# ------------------------------------------------------------------ 变换
def _transform_member(m, warn, owner):
    out = {
        "name": m.get("name", ""),
        "type": m.get("type", ""),
        "desc": m.get("desc", ""),
        "enum_refs": m.get("enum_refs", []),
        "check": m.get("check", ""),
    }
    t = (m.get("type") or "").strip()
    open_tail = "[" in t
    out["open"] = open_tail
    base = t.split("[", 1)[0].strip().lower()
    base = re.sub(r"[（(].*?[)）]\s*$", "", base).strip()   # 剥 'uint8(枚举)' 的括号后缀
    out["base_type"] = base
    bit = parse_int(m.get("bit"))
    width_bits = bit if bit else {"uint8": 8, "uint16": 16, "uint32": 32}.get(base, 8)
    out["bit"] = bit if bit else 0
    # 数组长度：uint8[n] 的 n（表里「长度」列），非数组类型为空；open 且无长度=不定长
    arr_len = parse_int(m.get("len"))
    out["array_len"] = arr_len if open_tail else None
    byte_w = (width_bits + 7) // 8
    if open_tail:
        out["byte_start"] = parse_int(m.get("byte"))
        out["byte_end"] = None          # 长度随帧，「长度」列只是上限，不参与偏移计算
        out["nbytes"] = None
    else:
        bs = parse_int(m.get("byte"))
        if bs is None:
            warn.append("结构体 %s 成员 %s 字节序号无法解析: %r"
                        % (owner, m.get("name"), m.get("byte")))
        nbytes = byte_w * (arr_len if (open_tail and arr_len) else 1)
        out["byte_start"] = bs
        out["byte_end"] = (bs + nbytes - 1) if bs is not None else None
        out["nbytes"] = nbytes
    # 位域成员（单字节内位宽 1~7）生成访问器用
    out["is_bit"] = (not open_tail and out["bit"] is not None
                     and 1 <= out["bit"] <= 7 and out["nbytes"] == 1)
    return out


def transform(model):
    """reader 统一模型 → protocol.json dict（稳定排序、解析数值、去运行时字段）。"""
    warn = []

    services = sorted(
        ({k: s.get(k, "" if k != "interface_names" else []) for k in
          ("name", "service_id", "namespace", "desc", "interface_names", "check")}
         for s in model["services"]),
        key=lambda s: s["name"])

    interfaces = []
    for i in model["interfaces"]:
        mid = parse_int(i.get("msg_id"))
        if i.get("msg_id") and mid is None:
            warn.append("接口 %s 消息id无法解析: %r" % (i.get("name"), i.get("msg_id")))
        d = {
            "name": i.get("name", ""),
            "desc": i.get("desc", ""),
            "type": i.get("if_type", ""),
            "tx_type": i.get("tx_type", ""),
            "direction": i.get("direction", ""),
            "msg_id": mid,
            "msg_id_hex": to_hex(mid) if mid is not None else None,
            "transport": i.get("transport", ""),
            "qos": i.get("qos", ""),
            "service": i.get("service", ""),
            "struct_refs": i.get("struct_refs", []),
            "enum_refs": i.get("enum_refs", []),
            "related": i.get("related", []),
            "error_refs": i.get("error_refs", []),
            "check": i.get("check", ""),
        }
        p = i.get("param")
        d["params"] = ([{"name": p["name"], "type": p["type"], "io": p["dir"],
                         "desc": p["desc"]}] if p else [])
        interfaces.append(d)
    interfaces.sort(key=lambda x: (x["msg_id"] is None, x["msg_id"] if x["msg_id"] is not None else 0,
                                   x["name"]))

    structs = []
    for s in model["structs"]:
        members = [_transform_member(m, warn, s.get("name")) for m in s["members"]]
        members.sort(key=lambda m: (m["byte_start"] is None,
                                    m["byte_start"] if m["byte_start"] is not None else 0,
                                    m["name"]))
        structs.append({
            "name": s.get("name", ""),
            "desc": s.get("desc", ""),
            "size": s.get("size", ""),
            "members": members,
            "interface_refs": s.get("interface_refs", []),
            "error_refs": s.get("error_refs", []),
            "check": s.get("check", ""),
        })
    structs.sort(key=lambda s: s["name"])

    enums = []
    for e in model["enums"]:
        vals = []
        for v in e["values"]:
            n = parse_int(v.get("value"))
            if v.get("value") and n is None:
                warn.append("枚举 %s 值 %s 无法解析: %r"
                            % (e.get("name"), v.get("name"), v.get("value")))
            vals.append({
                "c_name": v.get("name", ""),
                "value": n,
                "value_hex": to_hex(n, 2) if n is not None else None,
                "desc": v.get("desc", ""),
                "check": v.get("check", ""),
            })
        vals.sort(key=lambda x: (x["value"] is None,
                                 x["value"] if x["value"] is not None else 0, x["c_name"]))
        enums.append({
            "name": e.get("name", ""),
            "values": vals,
            "member_refs": e.get("member_refs", []),
            "interface_refs": e.get("interface_refs", []),
            "check": e.get("check", ""),
        })
    enums.sort(key=lambda e: e["name"])

    errors = sorted(
        ({k: e.get(k, "" if k not in ("struct_refs", "interface_refs") else [])
          for k in ("group", "value", "c_name", "desc", "applies_to",
                    "struct_refs", "interface_refs", "check")}
         for e in model["errors"]),
        key=lambda e: (e["group"], e["c_name"]))

    return {
        "schema_version": SCHEMA_VERSION,
        "platform": model["platform"],
        "platform_name": model["platform_name"],
        "source": {
            "type": model["source"].get("type", "bitable"),
            "base_token": model["source"].get("base_token", ""),
            "url": model["source"].get("url", ""),
        },
        "counts": {
            "services": len(services),
            "interfaces": len(interfaces),
            "structs": len(structs),
            "enums": len(enums),
            "enum_values": sum(len(e["values"]) for e in enums),
            "member_variables": sum(len(s["members"]) for s in structs),
            "error_codes": len(errors),
        },
        "services": services,
        "interfaces": interfaces,
        "structs": structs,
        "enums": enums,
        "errors": errors,
    }, warn


# ------------------------------------------------------------------ check 判定
# 降级规则：这些检测项属于「业务上尚未定义」，不影响生成代码的正确性，故不算违规。
# 判据：空引用 → 生成物里就是没有对应条目，C/ARXML 依然合法。
# 匹配串声明在 config 的 check_rules.degraded（按表角色分域），doctor 会校验其仍存在于该表检测公式中。
_DEGRADED_FALLBACK = {"data_structure": ("引用接口为空", "子项为空")}


def _degraded_patterns():
    """从 config 读降级规则：{表角色: (匹配串, ...)}；config 缺失时用兜底常量。"""
    try:
        rules = (conf.platform_cfg().get("check_rules") or {}).get("degraded") or {}
    except Exception:
        return _DEGRADED_FALLBACK
    out = {}
    for role, items in rules.items():
        if role.startswith("_"):
            continue
        out[role] = tuple(p for p in (items or []) if p)
    return out or _DEGRADED_FALLBACK


def _is_degraded(msg, patterns, role):
    """该检测原文是否命中 role 表声明的降级串（不同表的规则互不串用）。"""
    return any(p in msg for p in patterns.get(role, ()))


def check_issues(data):
    """protocol.json → (违规列表, 警告列表)。

    违规=check 含 ❌ 且不属于降级项（会阻断 gen）；
    警告=check 含 ⚠️，或含 ❌ 但命中降级规则（业务未定义，不阻断）。
    """
    bad, warn = [], []
    patterns = _degraded_patterns()

    def scan(kind, name, check, role):
        if not check:
            return
        has_err = "❌" in check
        has_warn = "⚠️" in check or "⚠" in check
        if has_err and not _is_degraded(check, patterns, role):
            bad.append((kind, name, check))
        elif has_err or has_warn:
            warn.append((kind, name, check))

    for s in data["services"]:
        scan("service", s["name"], s["check"], "service_interface")
    for i in data["interfaces"]:
        scan("interface", i["name"], i["check"], "service_interface")
    for s in data["structs"]:
        scan("struct", s["name"], s["check"], "data_structure")
        for m in s["members"]:
            scan("struct-member", "%s.%s" % (s["name"], m["name"]), m["check"],
                 "data_structure_item")
    for e in data["enums"]:
        scan("enum", e["name"], e["check"], "data_structure")
        for v in e["values"]:
            scan("enum-value", "%s.%s" % (e["name"], v["c_name"]), v["check"],
                 "data_structure_item")
    for e in data["errors"]:
        scan("error", "%s/%s" % (e["group"], e["c_name"]), e["check"], "error_code")
    return bad, warn


# ------------------------------------------------------------------ IO
def load(path=None):
    """读 protocol.json（解析后的协议模型）。"""
    path = path or _default_path()
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_any(path=None):
    """读任意协议 JSON，自动识别形态 → 统一返回 protocol.json 形态的 dict。

    - base_raw.json（顶层有 records 键）→ 内存解析成协议模型（不落盘）
    - protocol.json（顶层有 services 键）→ 直接返回
    这样 gen/check/read 都可直接吃 raw，无需中间文件。
    """
    path = path or raw_path_default()
    with open(path, "r", encoding="utf-8") as f:
        obj = json.load(f)
    if "records" in obj:
        model = model_from_raw(obj["records"], conf.platform_cfg(conf.platform()))
        data, _warn = transform(model)
        return data
    if "services" in obj:
        return obj
    raise PullError("无法识别的协议 JSON（既无 records 也无 services）: %s" % path)


def _default_path():
    return os.path.join(conf.OUTPUT_DIR, PROTO_JSON)


def save(data, path=None):
    path = path or _default_path()
    d = os.path.dirname(os.path.abspath(path))
    if d:
        os.makedirs(d, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    return path


# ------------------------------------------------------------------ raw 层
RAW_JSON = "base_raw.json"


def raw_path_default():
    return os.path.join(conf.OUTPUT_DIR, RAW_JSON)


def save_raw(raw, path=None):
    """落 API 原始记录快照（各表记录数组原样，含 record_id/link id/检测原文）。

    稳定排序：每表内记录按 record_id 排序，避免 API 返回顺序抖动造成假 diff。
    """
    path = path or raw_path_default()
    d = os.path.dirname(os.path.abspath(path))
    if d:
        os.makedirs(d, exist_ok=True)
    ordered = {}
    for role in sorted(raw):
        ordered[role] = sorted(raw[role], key=lambda r: r.get("record_id") or "")
    payload = {
        "raw_version": "1.0.0",
        "platform": conf.platform(),
        "source": conf.platform_cfg(conf.platform()).get("source", {}),
        "tables": {role: conf.platform_cfg(conf.platform())["tables"][role]["id"]
                   for role in ordered if role in conf.platform_cfg(conf.platform())["tables"]},
        "records": ordered,
        "row_counts": {k: len(v) for k, v in ordered.items()},
    }
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write("\n")
    return path


def load_raw(path=None):
    path = path or raw_path_default()
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)["records"]


def model_from_raw(raw_records, cfg):
    """raw 记录 → 平台统一模型（调用平台 reader，离线解析）。"""
    from . import platforms
    key = conf.platform()
    reader = platforms.make_reader(key, cfg)
    if hasattr(reader, "assemble_raw"):
        return reader.assemble_raw(raw_records)
    raise PullError("平台 %s 的 reader 未实现 assemble_raw()，无法从 raw 离线解析" % key)
