# -*- coding: utf-8 -*-
"""lark-cli 多维表格（base）只读封装：列表 / 字段 / 记录。

所有飞书交互走这里，平台层不直接 subprocess。
本 skill 只做「看懂协议」，故只提供读操作，无写操作。
"""
import json
import os
import shutil
import subprocess
import tempfile

MAX_READ_ROWS = 2000          # 单表读满的安全阀；超限报错而不是静默截断


class BitableError(RuntimeError):
    pass


def cli(args, timeout=180):
    """调用 lark-cli，返回 stdout 文本。统一走 --as user。"""
    exe = shutil.which("lark-cli") or "lark-cli"
    args = list(args)
    if "--as" not in args:
        args += ["--as", "user"]
    proc = subprocess.run([exe] + args, capture_output=True, text=True,
                          encoding="utf-8", errors="replace", timeout=timeout)
    if proc.returncode != 0:
        raise BitableError("lark-cli 失败(%d): %s\n%s"
                           % (proc.returncode, " ".join(args), (proc.stderr or "")[:2000]))
    return proc.stdout or ""


def list_tables(base_token):
    """返回 [{id, name, records_count}, ...]。"""
    out = cli(["base", "+table-list", "--base-token", base_token])
    return json.loads(out)["data"]["tables"]


def list_fields(base_token, table_id):
    """返回 [{id, name, type, ...}, ...]。"""
    out = cli(["base", "+field-list", "--base-token", base_token, "--table-id", table_id])
    return json.loads(out)["data"]["fields"]


def read_records(base_token, table_id, field_names=None):
    """读整张表全部记录，返回 [ {record_id, 字段名: 值, ...}, ... ]。

    field_names 缺省读所有字段；显式传则只读这些（避免公式列等噪声）。
    记录写入临时 ndjson 再解析，规避 stdout 长度限制。
    """
    fd, path = tempfile.mkstemp(suffix=".ndjson")
    os.close(fd)
    try:
        args = ["base", "+record-list",
                "--base-token", base_token,
                "--table-id", table_id,
                "--format", "ndjson",
                "--output", path,
                "--overwrite"]
        for f in (field_names or []):
            args += ["--field-id", f]
        cli(args)
        rows = []
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    rows.append(json.loads(line))
        if len(rows) >= MAX_READ_ROWS:
            raise BitableError("表 %s 记录数 %d 达到单次读取上限 %d：请确认表结构或调大 MAX_READ_ROWS"
                               % (table_id, len(rows), MAX_READ_ROWS))
        return rows
    finally:
        try:
            os.remove(path)
        except OSError:
            pass


# ------------------------------------------------------------------ 写操作（fix 兜底 / 对话直录新增记录用）
def record_create(base_token, table_id, records):
    """批量建记录，返回 [record_id,...]。records = [{字段: 值}, ...]。

    值形态：text→"str"；number→数字；select→["选项"]（新选项飞书自动创建）；
    link→[{"id":"recXxx"}]。
    """
    fd, path = tempfile.mkstemp(suffix=".json")
    os.close(fd)
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"records": records}, f, ensure_ascii=False)
        out = cli(["base", "+record-batch-create",
                   "--base-token", base_token,
                   "--table-id", table_id,
                   "--json", "@" + path])
        d = json.loads(out)
        return d["data"]["record_id_list"]
    finally:
        try:
            os.remove(path)
        except OSError:
            pass


def record_update_batch(base_token, table_id, update_records):
    """批量更新：update_records = {record_id: {字段: 值}, ...}，返回更新数。"""
    if not update_records:
        return 0
    fd, path = tempfile.mkstemp(suffix=".json")
    os.close(fd)
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"update_records": update_records}, f, ensure_ascii=False)
        out = cli(["base", "+record-batch-update",
                   "--base-token", base_token,
                   "--table-id", table_id,
                   "--json", "@" + path])
        d = json.loads(out)
        return len(d["data"].get("record_id_list") or [])
    finally:
        try:
            os.remove(path)
        except OSError:
            pass


# ------------------------------------------------------------------ select 选项维护
def field_get(base_token, table_id, field_id):
    out = cli(["base", "+field-get", "--base-token", base_token,
               "--table-id", table_id, "--field-id", field_id])
    return json.loads(out)["data"]["field"]


def field_options_all(base_token, table_id, field_id):
    """分页取 select 字段的全部选项（绕过 field-get 的 50 条截断）。"""
    out = cli(["base", "+field-search-options", "--base-token", base_token,
               "--table-id", table_id, "--field-id", field_id,
               "--limit", "200"])
    d = json.loads(out)["data"]
    return d.get("options") or []


def field_update(base_token, table_id, field_id, field_json):
    fd, path = tempfile.mkstemp(suffix=".json")
    os.close(fd)
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(field_json, f, ensure_ascii=False)
        out = cli(["base", "+field-update", "--base-token", base_token,
                   "--table-id", table_id, "--field-id", field_id,
                   "--json", "@" + path, "--yes"])
        return json.loads(out)
    finally:
        try:
            os.remove(path)
        except OSError:
            pass


def ensure_select_options(base_token, table_id, field_name, values):
    """确保 select 字段选项含全部 values，缺的追加。返回实际新增的值列表。

    【高危警告】field-get 对选项多的字段会截断（truncated=true，只返回前 50 个）。
    若直接用返回的 options 做全量 PUT，会删掉未返回的选项并清空用它们的记录值
    （2026-11-09 实际事故：71 选项被砍到 50，21 条记录接口名被清空）。

    安全策略：选项基集 = `+field-search-options --limit 200` 取回的全部选项
    （绕开 field-get 截断）∪ 目标新值，再整体 PUT。
    """
    vals = [v for v in (values or []) if v]
    if not vals:
        return []
    f = field_get(base_token, table_id, field_name)
    if f.get("type") != "select":
        return []

    # 必须用分页接口拿全量选项；field-get 的 options 会被截断到 50 条
    try:
        base = [o["name"] for o in field_options_all(base_token, table_id, f["id"])]
    except Exception:
        raise BitableError(
            "字段「%s」无法枚举全部选项（+field-search-options 失败），"
            "拒绝全量 PUT 以免误删选项" % field_name)
    if not base and f.get("options"):
        base = [o["name"] for o in f.get("options")]

    merged = []
    for n in base + vals:
        if n and n not in merged:
            merged.append(n)
    added = [v for v in vals if v not in base]
    if not added:
        return []
    body = {"name": f["name"], "type": "select",
            "multiple": bool(f.get("multiple")),
            "options": [{"name": n} for n in merged]}
    field_update(base_token, table_id, f["id"], body)
    return added


# ------------------------------------------------------------------ 值归一化
def text(v):
    """文本字段 → 去空白字符串；None/非字符串 → ''。"""
    if v is None:
        return ""
    if isinstance(v, str):
        return v.strip()
    return str(v).strip()


def first(v):
    """单选字段（array<string>）→ 首个值；文本 → 原样；空 → ''。"""
    if isinstance(v, list):
        return v[0].strip() if v else ""
    return text(v)


def link_ids(v):
    """链接字段（array<{id}>）→ [record_id, ...]。"""
    if isinstance(v, list):
        return [x.get("id") for x in v if isinstance(x, dict) and x.get("id")]
    return []


def pick(record, names):
    """按候选字段名依次取值，返回第一个非空值；全空返回 ''。

    表里字段可能被改名带后缀（如 消息id → 消息id(16进制)），
    候选名顺序由 config 的 field_aliases 决定，写回时也用实际命中的那个名字。
    """
    for n in names:
        v = record.get(n)
        if v is None or v == "" or v == []:
            continue
        return v
    return ""


def pick_name(record, names):
    """返回实际命中的字段名（用于写回）；未命中返回候选首个。"""
    for n in names:
        v = record.get(n)
        if v is None or v == "" or v == []:
            continue
        return n
    return list(names)[0] if names else ""


def display_name_map(records, label_field):
    """从记录列表建 record_id → 显示名 映射（label_field 兼容文本/单选）。"""
    m = {}
    for r in records:
        rid = r.get("record_id")
        if not rid:
            continue
        m[rid] = first(r.get(label_field))
    return m


def resolve_links(raw_value, name_map):
    """把链接字段的 id 列表解析成目标显示名列表（保持顺序，去空）。"""
    out = []
    for rid in link_ids(raw_value):
        nm = name_map.get(rid)
        if nm:
            out.append(nm)
    return out
