# -*- coding: utf-8 -*-
"""C 语言生成器：protocol.json → Jinja2 模板 → codegen/c/generated/。

原则（蓝本 04/05 段）：
  - 模板零逻辑：分支/映射全部在 Python 里算好再交给模板；
  - StrictUndefined：模板引用了未提供的变量直接报错；
  - 确定性：同一 protocol.json 两次渲染逐字节相同（渲染两次自检）；
  - 不用 C 位域：bit 成员生成 Get/Set 访问器（掩码式），跨编译器可移植。
"""
import hashlib
import os

from ..common import conf
from ..model import Protocol, to_hex

try:
    import jinja2
except ImportError:      # pragma: no cover
    raise SystemExit("缺少 jinja2：先跑 utils\\setup_env.ps1，"
                     "并用 utils\\.venv\\Scripts\\python.exe 执行本脚本")

_CTYPE = {"uint8": "uint8_t", "uint8_t": "uint8_t", "int8": "sint8_t",
          "uint16": "uint16_t", "uint16_t": "uint16_t", "int16": "sint16_t",
          "uint32": "uint32_t", "uint32_t": "uint32_t", "int32": "sint32_t"}
_BIT_FULL = 0xFF


def _bits_mask(bit_text):
    """'0-7bit'→(0xFF, 8) / '4'→(0x10, 1) / '0-3'→(0x0F, 4)。"""
    t = (bit_text or "").strip().replace(" ", "").lower().rstrip("bit")
    if not t:
        return _BIT_FULL, 8
    try:
        if "-" in t:
            a, b = sorted(int(x) for x in t.split("-", 1))
        else:
            a = b = int(t)
        mask = sum(1 << i for i in range(a, b + 1))
        return mask, (b - a + 1)
    except ValueError:
        return _BIT_FULL, 8


def _is_bit_member(m):
    return bool(m.bit) and not m.open and (m.byte_end == m.byte_start)


def build_view(proto, cfg):
    h = cfg["header"]
    sp = h["struct_prefix"]
    cp = h["cmd_enum_prefix"]
    rx, tx = [], []
    for itf in proto.all_interfaces():
        entry = {
            "name": itf.name,
            "enum": cp + itf.name,
            "id": itf.msg_id,
            "id_hex": to_hex(itf.msg_id),
            "handler": sp + itf.name + h["handler_suffix"],
            "type": itf.type,
            "tx_type": itf.tx_type,
            "params": [dict(p.__dict__) for p in itf.params],
            "service": None,
        }
        (rx if itf.direction == "SOC_TO_MCU" else tx).append(entry)

    structs = []
    for st in proto.structs:
        ms = []
        for m in st.members:
            mm = {"name": m.name, "type": m.type, "desc": m.desc,
                  "open": m.open, "bit": m.bit,
                  "byte_start": m.byte_start, "byte_end": m.byte_end}
            mm["ctype"] = _CTYPE.get((m.type or "").lower().replace("_t", ""), "uint8_t")
            if m.open:
                mm["ctype"] = "uint8_t"
            mm["is_bit"] = _is_bit_member(m)
            if mm["is_bit"]:
                mask, width = _bits_mask(m.bit)
                mm["mask"] = to_hex(mask, 2)
                mm["shift"] = (m.bit or "0").split("-")[0].strip() or "0"
            ms.append(mm)
        structs.append({
            "name": st.name, "c_name": sp + st.name, "desc": st.desc,
            "service": st.service, "size": st.size,
            "nbytes": st.fixed_bytes, "has_open": st.has_open,
            "members": ms,
            "is_raw": any(x["is_bit"] for x in ms),
        })

    enums = []
    for e in proto.enums:
        enums.append({"name": e.name, "c_name": sp + e.name,
                      "vals": [{"c_name": i.c_name, "value": i.value,
                                "value_hex": to_hex(i.value, 2), "desc": i.desc}
                               for i in e.items]})

    return {"rx": rx, "tx": tx, "structs": structs, "enums": enums}


def generate(proto, gcfg, root):
    """渲染 C 代码。proto=Protocol 实例，gcfg=本语言配置，root=codegen/c 绝对路径。"""
    tmpl_dir = os.path.join(root, "templates")
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(tmpl_dir),
        undefined=jinja2.StrictUndefined,
        trim_blocks=True, lstrip_blocks=True, keep_trailing_newline=True)

    view = build_view(proto, gcfg)
    common = {
        "revision": proto.source.get("revision"),
        "spreadsheet": proto.source.get("spreadsheet"),
        "counts": proto.counts(),
    }
    out_dir = conf.output_path(gcfg["output_dir"])
    os.makedirs(out_dir, exist_ok=True)

    written = []
    for key, fname in gcfg["file_names"].items():
        tmpl = env.get_template(key + ".j2")
        guard = gcfg["header"]["include_guard_prefix"] + \
            os.path.splitext(fname)[0].upper().replace("-", "_") + "_H"
        text1 = tmpl.render(files=gcfg["file_names"], header=gcfg["header"],
                            behaviour=gcfg["behaviour"], guard=guard, **view, **common)
        text2 = tmpl.render(files=gcfg["file_names"], header=gcfg["header"],
                            behaviour=gcfg["behaviour"], guard=guard, **view, **common)
        if hashlib.md5(text1.encode()).hexdigest() != hashlib.md5(text2.encode()).hexdigest():
            raise SystemExit("模板渲染不确定：" + fname)
        path = os.path.join(out_dir, fname)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text1)
        written.append(path)
    return written
