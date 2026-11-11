# -*- coding: utf-8 -*-
"""config 体检：核对 proto_config.json 的表坐标 / 字段语义 / 检测规则与线上 Base 是否一致。

动机（2026-11-09）：
  - Base 重建「服务接口」表后 id 变化，一次性脚本硬编码旧 id，lark-cli 只回 not_found；
  - 表里字段改名（`数组长度` → `长度`）后脚本静默读到空，数组长度丢失且不报错。

铁律：表坐标与字段名永远从 config 取（conf.tables() / conf.table(role) / schema.declared()），
      任何脚本禁止硬编码 tbl/vew/fld 开头 id，禁止硬编码表内字段名；先 doctor 再动手。
"""
import json

from .common import bitable, conf, schema


def verify(cfg=None, base_token=None):
    """返回 issues 列表：[(level, role, key, message)]，level ∈ ERROR/WARN。"""
    cfg = cfg if cfg is not None else conf.platform_cfg()
    base_token = base_token or cfg["source"]["base_token"]

    online = {t["id"]: t for t in bitable.list_tables(base_token)}
    by_name = {t["name"]: t["id"] for t in online.values()}
    issues = []

    # ---- 表 id ----
    for role, meta in (cfg.get("tables") or {}).items():
        tid, name = meta.get("id", ""), meta.get("name", "")
        if tid in online:
            real = online[tid]["name"]
            if name and real != name:
                issues.append(("WARN", role, "table",
                               "表名不一致：config=%r 线上=%r（id 正确，仅提示）" % (name, real)))
            continue
        if name and name in by_name:
            issues.append(("ERROR", role, "table",
                           "表 id %s 已失效（线上同名表「%s」现在是 %s）"
                           % (tid, name, by_name[name])))
        else:
            issues.append(("ERROR", role, "table",
                           "表 id %s 线上不存在，且找不到同名表「%s」（表被删或改名）" % (tid, name)))

    # ---- 字段语义 / link 目标 / split / label ----
    fields_by_role = {}
    for role, meta in (cfg.get("tables") or {}).items():
        if meta.get("id") in online:
            try:
                fields_by_role[role] = bitable.list_fields(base_token, meta["id"])
            except bitable.BitableError as e:
                issues.append(("ERROR", role, "fields", "字段读取失败：%s" % str(e)[:200]))
    _resolved, sch_issues, _sug = schema.resolve_platform(cfg, fields_by_role, base_token)
    issues += sch_issues

    # ---- 检测字段 / 降级规则 ----
    good = {r: fields_by_role.get(r, []) for r in fields_by_role}
    issues += schema.check_degraded(cfg, good)
    for role, fields in good.items():
        if not any(f.get("type") == "formula" for f in fields):
            issues.append(("WARN", role, "check", "该表没有检测公式字段（检测职责缺失）"))
    return issues


def autofix(base_token=None):
    """按表名重解析失效表 id，按线上字段重写语义键的首选字段名。

    返回 [(kind, role, key, 旧值, 新值)]。
    """
    full = conf.load()
    key = full["platform"]
    cfg = full["platforms"][key]
    base_token = base_token or cfg["source"]["base_token"]

    online = {t["id"]: t for t in bitable.list_tables(base_token)}
    by_name = {t["name"]: t["id"] for t in online.values()}

    changes = []
    for role, meta in (cfg.get("tables") or {}).items():
        tid, name = meta.get("id"), meta.get("name")
        if tid in online or not name or name not in by_name:
            continue
        new_id = by_name[name]
        if new_id != tid:
            meta["id"] = new_id
            changes.append(("table_id", role, "id", tid, new_id))

    fields_by_role = {r: bitable.list_fields(base_token, m["id"])
                      for r, m in cfg["tables"].items() if m.get("id") in online}
    _resolved, _issues, suggestions = schema.resolve_platform(cfg, fields_by_role, base_token)

    for role, sug in suggestions.items():
        meta = cfg["tables"][role]
        for skey, new_name in sug.items():
            cur = meta["fields"][skey]
            old_first = cur[0] if isinstance(cur, list) else cur
            # 保留旧名作候选（防止两边都合法时误判），新名提到首位
            rest = [c for c in (cur if isinstance(cur, list) else [cur]) if c != new_name]
            meta["fields"][skey] = [new_name] + rest
            changes.append(("field", role, skey, old_first, new_name))

    if changes:
        with open(conf.CONFIG_PATH, "w", encoding="utf-8", newline="\n") as f:
            json.dump(full, f, ensure_ascii=False, indent=2)
            f.write("\n")
    return changes
