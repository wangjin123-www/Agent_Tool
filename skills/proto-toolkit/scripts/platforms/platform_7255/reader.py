# -*- coding: utf-8 -*-
"""7255 平台协议读取实现。

数据源：飞书多维表格（config 里 7255.source）。

表结构（2026-11-09 表优化定稿，5 张表；字段名一律走 config 的 fields 语义映射）：
  服务接口     纯接口表：每行一个接口，服务信息（服务名/命名空间/服务id/服务描述）
               直接做成普通列。无接口的服务也保留一行，只是接口字段为空（待补）。
               主字段=接口名（link 引用时显示接口名）。
  数据结构     种类=结构体/枚举 两种行
  数据结构子项 子项类型=枚举值 为枚举值，其余为结构体成员
  错误码       独立表
  自动修改协议 问答录入表（不在协议模型内）

职责：把表读进内存 → 分流 → 组装成统一协议模型（platforms.base 约定的结构）。
脚本里不出现表内字段名：语义键（msg_id / arr_len …）经 schema.from_records()
按实际记录键解析为线上真实字段名，字段改名不会被静默读成空。
"""
from ...common import bitable, schema
from ...common.bitable import text, first, link_ids, resolve_links


class Reader:
    """7255 MCU&SOC 通信协议读取器。"""

    PLATFORM = "7255"

    def __init__(self, cfg):
        self.cfg = cfg                       # conf.platform_cfg('7255')
        self.src = cfg["source"]
        self.base_token = self.src["base_token"]
        self.tbl = cfg["tables"]

    # -------------------------------------------------------------- 主入口
    def read(self):
        raw = self.read_raw()
        return self._assemble(raw)

    def read_raw(self):
        """只读 API 原始记录（不解析），供 pull 落 base_raw.json。"""
        return self._read_all()

    def assemble_raw(self, raw):
        """从 raw 记录解析组装模型（离线，不联网）——解析只依赖 raw。"""
        return self._assemble(raw)

    # -------------------------------------------------------------- 读原始表
    def _read_all(self):
        raw = {}
        for role, meta in self.tbl.items():
            raw[role] = bitable.read_records(self.base_token, meta["id"])
        return raw

    # -------------------------------------------------------------- 语义键取值
    def _f(self, raw, role):
        """某表的语义键 → 真实字段名（按实际记录键就地解析，改名自动跟随）。"""
        return schema.from_records(self.tbl[role], raw.get(role) or [])

    @staticmethod
    def _g(rec, name):
        """按解析出的真实字段名取值；name 为空（未声明）时返回空。"""
        return rec.get(name) if name else None

    # -------------------------------------------------------------- 分流
    def _split(self, raw):
        """数据结构表按种类拆组，子项表按子项类型拆组，服务接口表按有无接口名拆组。"""
        fs = self._f(raw, "service_interface")
        fd = self._f(raw, "data_structure")
        fi = self._f(raw, "data_structure_item")

        si = raw.get("service_interface") or []
        ds = raw.get("data_structure") or []
        items = raw.get("data_structure_item") or []

        ifaces = [r for r in si if first(self._g(r, fs["interface_name"]))]
        empty_svc = [r for r in si if not first(self._g(r, fs["interface_name"]))]

        split = self.tbl["data_structure"].get("split") or {}
        structs = [r for r in ds if first(self._g(r, fd["kind"])) == split.get("struct")]
        enums = [r for r in ds if first(self._g(r, fd["kind"])) == split.get("enum")]

        enum_type = schema.split_value(self.tbl["data_structure_item"], "enum_value")
        members = [r for r in items if first(self._g(r, fi["item_type"])) != enum_type]
        enum_values = [r for r in items if first(self._g(r, fi["item_type"])) == enum_type]
        return ifaces, empty_svc, structs, enums, members, enum_values

    def _name_maps(self, raw):
        """各表 record_id → 显示名。

        data_structure 映射必须覆盖「数据结构」表全部记录（结构体 + 枚举）：
        接口.引用枚举 与 子项.引用枚举 都指向该表，只收结构体会导致枚举引用解析成空。
        """
        fs = self._f(raw, "service_interface")
        fd = self._f(raw, "data_structure")
        fi = self._f(raw, "data_structure_item")
        fe = self._f(raw, "error_code")

        _, _, structs, enums, members, enum_values = self._split(raw)
        ds_all = list(structs) + list(enums)

        err = {}
        for r in raw.get("error_code") or []:
            rid = r.get("record_id")
            if not rid:
                continue
            grp = first(self._g(r, fe["group"]))
            val = text(self._g(r, fe["value"]))
            cn = text(self._g(r, fe["name"]))
            err[rid] = "%s(%s/%s)" % (grp, val, cn) if (grp or val or cn) else rid

        return {
            "service_interface": {r["record_id"]: first(self._g(r, fs["interface_name"]))
                                  for r in raw.get("service_interface") or []
                                  if first(self._g(r, fs["interface_name"]))},
            "data_structure": {r["record_id"]: first(self._g(r, fd["name"])) for r in ds_all},
            "member_variable": {r["record_id"]: first(self._g(r, fi["name"])) for r in members},
            "enum_type": {r["record_id"]: first(self._g(r, fd["name"])) for r in enums},
            "enum_value": {r["record_id"]: first(self._g(r, fi["name"])) for r in enum_values},
            "error_code": err,
        }

    # -------------------------------------------------------------- 组装模型
    def _check(self, record):
        """收集字段名含检测关键字的公式值（多维表格正常性检测列）。

        约定 ❌=违规、⚠️=警告、✅ 或空=通过，语义判定在 pull/check/gen 阶段统一做。
        检测列按 config 的 conventions.check_field_keyword 发现，不写死具体列名
        （表里加检测列自动带上）。
        """
        kw = (self.cfg.get("conventions") or {}).get("check_field_keyword", "检测")
        vals = []
        for k, v in record.items():
            if k == "record_id" or kw not in k:
                continue
            t = first(v) if isinstance(v, list) else text(v)
            if t:
                vals.append(t)
        return "；".join(vals)

    def _assemble(self, raw):
        fs = self._f(raw, "service_interface")
        fd = self._f(raw, "data_structure")
        fi = self._f(raw, "data_structure_item")
        fe = self._f(raw, "error_code")

        N = self._name_maps(raw)
        ifaces_r, empty_svc_r, structs_r, enums_r, members_r, enum_values_r = self._split(raw)

        member_by_id = {r.get("record_id"): r for r in members_r}
        enum_value_by_id = {r.get("record_id"): r for r in enum_values_r}

        # ---- 服务（由接口行/空服务行聚合去重，服务属性即行上的普通列）----
        svc_order, svc_map = [], {}
        for r in list(ifaces_r) + list(empty_svc_r):
            name = first(self._g(r, fs["service_name"]))
            if not name:
                continue
            if name not in svc_map:
                svc_map[name] = {
                    "id": "",
                    "name": name,
                    "service_id": text(self._g(r, fs["service_id"])),
                    "namespace": first(self._g(r, fs["namespace"])),
                    "desc": text(self._g(r, fs["service_desc"])),
                    "interface_names": [],
                    "check": "",
                }
                svc_order.append(name)
        services = [svc_map[n] for n in svc_order]

        # ---- 接口 ----
        interfaces = []
        for r in ifaces_r:
            p_name = first(self._g(r, fs["param_name"]))
            param = None
            if p_name:
                param = {
                    "name": p_name,
                    "type": first(self._g(r, fs["param_type"])),
                    "dir": first(self._g(r, fs["param_dir"])),
                    "desc": text(self._g(r, fs["param_desc"])),
                }
            svc_name = first(self._g(r, fs["service_name"])) or ""
            interfaces.append({
                "id": r.get("record_id"),
                "name": first(self._g(r, fs["interface_name"])),
                "direction": first(self._g(r, fs["direction"])),
                "if_type": first(self._g(r, fs["if_type"])),
                "msg_id": text(self._g(r, fs["msg_id"])),
                "desc": text(self._g(r, fs["iface_desc"])),
                "tx_type": first(self._g(r, fs["tx_type"])),
                "transport": first(self._g(r, fs["transport"])),
                "qos": first(self._g(r, fs["qos"])),
                "service": svc_name,
                "param": param,
                "struct_refs": resolve_links(self._g(r, fs["struct_refs"]), N["data_structure"]),
                "enum_refs": resolve_links(self._g(r, fs["enum_refs"]), N["data_structure"]),
                "related": resolve_links(self._g(r, fs["related"]), N["service_interface"]),
                "error_refs": resolve_links(self._g(r, fs["error_refs"]), N["error_code"]),
                "check": self._check(r),
            })
            if svc_name in svc_map:
                svc_map[svc_name]["interface_names"].append(first(self._g(r, fs["interface_name"])))

        # ---- 结构体 ----
        structs = []
        for r in structs_r:
            members = []
            for mid in link_ids(self._g(r, fd["items"])):
                mr = member_by_id.get(mid)
                if not mr:
                    continue
                members.append({
                    "name": first(self._g(mr, fi["name"])),
                    "type": first(self._g(mr, fi["item_type"])),
                    "byte": text(self._g(mr, fi["byte"])),
                    "bit": text(self._g(mr, fi["bit"])),
                    "len": text(self._g(mr, fi["arr_len"])),
                    "bit_range": text(self._g(mr, fi["bit_range"])),
                    "desc": text(self._g(mr, fi["desc"])),
                    "enum_refs": resolve_links(self._g(mr, fi["enum_refs"]), N["data_structure"]),
                    "check": self._check(mr),
                })
            structs.append({
                "id": r.get("record_id"),
                "name": first(self._g(r, fd["name"])),
                "size": "",
                "desc": text(self._g(r, fd["desc"])),
                "members": members,
                "interface_refs": resolve_links(self._g(r, fd["interface_refs"]), N["service_interface"]),
                "error_refs": [],
                "check": self._check(r),
            })

        # ---- 枚举 ----
        enums = []
        for r in enums_r:
            values = []
            for vid in link_ids(self._g(r, fd["items"])):
                vr = enum_value_by_id.get(vid)
                if not vr:
                    continue
                values.append({
                    "name": first(self._g(vr, fi["name"])),
                    "value": text(self._g(vr, fi["value"])),
                    "desc": text(self._g(vr, fi["desc"])),
                    "check": self._check(vr),
                })
            enums.append({
                "id": r.get("record_id"),
                "name": first(self._g(r, fd["name"])),
                "values": values,
                "member_refs": [],
                "interface_refs": resolve_links(self._g(r, fd["interface_refs"]), N["service_interface"]),
                "check": self._check(r),
            })

        # 成员 → 枚举反向索引
        enum_by_name = {e["name"]: e for e in enums if e["name"]}
        for s in structs:
            for m in s["members"]:
                for en in m["enum_refs"]:
                    if en in enum_by_name:
                        enum_by_name[en]["member_refs"].append("%s.%s" % (s["name"], m["name"]))

        # ---- 错误码 ----
        errors = []
        for r in raw.get("error_code") or []:
            errors.append({
                "id": r.get("record_id"),
                "group": first(self._g(r, fe["group"])),
                "value": text(self._g(r, fe["value"])),
                "c_name": text(self._g(r, fe["name"])),
                "desc": text(self._g(r, fe["desc"])),
                "applies_to": text(self._g(r, fe["applies_to"])),
                "struct_refs": [],
                "interface_refs": resolve_links(self._g(r, fe["interface_refs"]), N["service_interface"]),
                "check": self._check(r),
            })

        # ---- 空服务（无接口的预留服务）不单独建列表：已并入 services，
        #      「有接口/无接口」由 interface_names 长度体现 ----

        idx = {
            "services_by_name": {s["name"]: s for s in services if s["name"]},
            "interfaces_by_name": {i["name"]: i for i in interfaces if i["name"]},
            "structs_by_name": {s["name"]: s for s in structs if s["name"]},
            "enums_by_name": {e["name"]: e for e in enums if e["name"]},
            "errors_by_group": {},
        }
        for e in errors:
            idx["errors_by_group"].setdefault(e["group"] or "(未分组)", []).append(e)

        return {
            "platform": self.PLATFORM,
            "platform_name": self.cfg.get("name", ""),
            "source": self.src,
            "counts": {
                "services": len(services),
                "interfaces": len(interfaces),
                "structs": len(structs),
                "enums": len(enums),
                "enum_values": sum(len(e["values"]) for e in enums),
                "member_variables": sum(len(s["members"]) for s in structs),
                "error_codes": len(errors),
                "error_groups": len(idx["errors_by_group"]),
            },
            "services": services,
            "interfaces": interfaces,
            "structs": structs,
            "enums": enums,
            "errors": errors,
            "index": idx,
        }
