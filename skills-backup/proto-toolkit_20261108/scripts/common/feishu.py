# -*- coding: utf-8 -*-
"""lark-cli 封装：读范围 / 写范围 / 合并 / 样式 / 跳转链接。

所有飞书交互都走这里，业务层不直接 subprocess。
"""
import base64
import json
import os
import shutil
import subprocess

from . import conf

MAX_WRITE_BATCH = 100          # +cells-set --writes 单次上限
MAX_READ_ROWS = 2000           # 单表读满的安全阀；超限报错而不是静默截断

_INFO_CACHE = {}               # spreadsheet_token → workbook-info 的 sheets 列表

# 写表闸门：--dry-run 时由 rules.run_sync 置位，任何写操作直接抛错。
# 目的是让「只读」由结构保证，而不是靠每个 checker 自觉传 repair=False。
_READ_ONLY = False

_WRITE_CMDS = ("+cells-set", "+cells-clear", "+cells-unmerge", "+styles-put",
               "+dim-insert", "+dim-delete", "+dim-append")


class ReadOnlyError(RuntimeError):
    """--dry-run 下试图写表。"""


def set_read_only(flag):
    global _READ_ONLY
    prev = _READ_ONLY
    _READ_ONLY = bool(flag)
    return prev


def is_read_only():
    return _READ_ONLY


def _guard(cmd):
    if _READ_ONLY and cmd in _WRITE_CMDS:
        raise ReadOnlyError("--dry-run 只读模式禁止写表：%s" % cmd)


# ------------------------------------------------------------------ 底层调用
def cli(args, timeout=180, input_text=None):
    """调用 lark-cli，返回解析后的 JSON。

    Windows 下 lark-cli 是 npm 的 .CMD shim，裸名会触发 WinError 2，
    必须先 shutil.which 解析成绝对路径；协议表在用户空间，统一走 --as user。
    """
    exe = shutil.which("lark-cli") or "lark-cli"
    args = list(args)
    if "--as" not in args:
        args += ["--as", "user"]
    if len(args) > 1 and args[0] == "sheets":
        _guard(args[1])
    cmd = [exe] + args
    proc = subprocess.run(cmd, capture_output=True, text=True,
                          encoding="utf-8", errors="replace", timeout=timeout,
                          input=input_text)
    if proc.returncode != 0:
        raise RuntimeError("lark-cli 失败(%d): %s\n%s"
                           % (proc.returncode, " ".join(cmd), (proc.stderr or "")[:2000]))
    out = (proc.stdout or "").strip()
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        raise RuntimeError("lark-cli 输出非 JSON:\n" + out[:2000])


def revision(cfg):
    """表格当前 revision（用于 protocol.json 的 source.revision 快照与并发编辑检测）。"""
    d = cli(["sheets", "+workbook-info", "--spreadsheet-token", cfg["spreadsheet_token"]])
    return d["data"].get("revision") or d["data"].get("version")


def _grid(cfg):
    """workbook-info 的子表网格信息（按 token 缓存，一次运行只取一遍）。"""
    token = cfg["spreadsheet_token"]
    if token not in _INFO_CACHE:
        d = cli(["sheets", "+workbook-info", "--spreadsheet-token", token])
        _INFO_CACHE[token] = d["data"]["sheets"]
    return _INFO_CACHE[token]


def grid_rows(rows_meta, sheet_id):
    """从 workbook-info 的 sheets 数组里取某表网格行数。

    兼容两种返回口径：新版平铺 row_count / 旧版 grid_properties.row_count。
    """
    for s in rows_meta:
        if (s.get("sheet_id") or s.get("sheetId")) == sheet_id:
            g = s.get("grid_properties") or {}
            return (s.get("row_count") or s.get("rowCount")
                    or g.get("row_count") or g.get("rowCount") or 0)
    return 0


def sheet_rows(cfg, sheet_key):
    """子表实际网格行数（读满用；不是「有内容行数」）。"""
    return sheet_rows_by_id(cfg, cfg["sheets"][sheet_key]["id"])


def sheet_rows_by_id(cfg, sheet_id):
    """按裸 sheet_id 取网格行数（legacy 引擎等无 sheets 结构的调用方共用）。"""
    return grid_rows(_grid(cfg), sheet_id)


def row_count(cfg, sheet_key):
    """子表当前行数（用于判断是否需要 --prune）。"""
    return sheet_rows(cfg, sheet_key)


# ------------------------------------------------------------------ 单元格模型
def cell_text(cell):
    """取单元格显示文本：普通值优先，其次 rich_text 首段。"""
    if not cell:
        return ""
    v = cell.get("value")
    if v is not None:
        return str(v).strip()
    rt = cell.get("rich_text") or []
    if rt:
        return (rt[0].get("text") or "").strip()
    return ""


def cell_link(cell):
    """取单元格内嵌超链接 URL（rich_text 首段 link）。"""
    if not cell:
        return ""
    rt = cell.get("rich_text") or []
    if rt:
        return rt[0].get("link") or ""
    return ""


def cell_at(rows, row_1based, col_letter):
    """按 A1 语义取格：rows 是从第 1 行起的二维数组。"""
    ci = conf.col_index(col_letter)
    ri = row_1based - 1
    if ri < 0 or ri >= len(rows):
        return {}
    line = rows[ri]
    if ci >= len(line):
        return {}
    return line[ci] or {}


# ------------------------------------------------------------------ 读
def read(cfg, sheet_key, last_col, last_row=None):
    """整块读取子表 A1:<last_col><last_row>，返回二维 cells 数组。

    last_row 缺省时按该子表实际网格行数读满——不设固定上限，避免表长过 300 行
    后静默截断（截断后解析出来的协议会少接口且没人报错）。
    """
    if last_row is None:
        last_row = sheet_rows(cfg, sheet_key)
    if last_row > MAX_READ_ROWS:
        raise RuntimeError("%s 网格 %d 行超过单次读取上限 %d：请先确认表结构或调整 MAX_READ_ROWS"
                           % (sheet_key, last_row, MAX_READ_ROWS))
    rng = "A1:%s%d" % (last_col, max(last_row, 1))
    cells = cells_get(cfg, cfg["sheets"][sheet_key]["id"], rng)
    # 读满后裁掉尾部全空行：网格常留大量空行，不裁会让解析循环白跑
    while cells and not any(cell_text(c) for c in (cells[-1] or [])):
        cells.pop()
    return cells


def cells_get(cfg, sheet_id, rng, include="value"):
    """+cells-get 底层（裸 sheet_id 版）：read_range / legacy 引擎共用。"""
    d = cli(["sheets", "+cells-get",
             "--spreadsheet-token", cfg["spreadsheet_token"],
             "--sheet-id", sheet_id,
             "--range", rng,
             "--include", include,
             "--format", "json"])
    return d["data"]["ranges"][0]["cells"]


def read_range(cfg, sheet_key, rng, include="value"):
    """读任意范围（如 'G2:G40'）；include='value,style' 时带回样式。"""
    return cells_get(cfg, cfg["sheets"][sheet_key]["id"], rng, include)


# ------------------------------------------------------------------ 链接
def b64(a1):
    """飞书 range 参数：base64(A1) 去掉尾部 '=' 填充。"""
    return base64.b64encode(a1.encode()).decode().rstrip("=")


def jump_url_by_id(cfg, a1, sheet_id):
    """跳转 URL（裸 sheet_id 版）：legacy 引擎与 jump_url 共用。"""
    return "https://%s/sheets/%s?range=%s&sheet=%s" % (
        cfg["host"], cfg["spreadsheet_token"], b64(a1), sheet_id)


def jump_url(cfg, a1, sheet_key):
    return jump_url_by_id(cfg, a1, cfg["sheets"][sheet_key]["id"])


def decode_url(url):
    """从跳转链接里解出 (sheet_id, A1)；解不出返回 ('', '')。"""
    if not url:
        return "", ""
    sheet = ""
    rng = ""
    if "range=" in url:
        rng = url.split("range=")[1].split("&")[0]
    if "sheet=" in url:
        sheet = url.split("sheet=")[1].split("&")[0]
    try:
        a1 = base64.b64decode(rng + "=" * (-len(rng) % 4)).decode()
    except Exception:
        a1 = ""
    return sheet, a1


# ------------------------------------------------------------------ 写
def write_cells(cfg, sheet_key, rng, cells):
    """写一块二维 cells（维度必须与 range 严格一致）。

    cells 走 stdin（--cells -）：大块内容进命令行会撞 Windows 32K 长度上限，
    且内联 JSON 可能被 shell 破坏。
    """
    cli(["sheets", "+cells-set",
         "--spreadsheet-token", cfg["spreadsheet_token"],
         "--sheet-id", cfg["sheets"][sheet_key]["id"],
         "--range", rng,
         "--cells", "-"], input_text=json.dumps(cells, ensure_ascii=False))


def write_writes(cfg, writes, out_dir=None):
    """批量写多块：writes = [{sheet_id, range, cells}, ...]，按 100 条/批切分。"""
    out_dir = out_dir or conf.ensure_output()
    n = 0
    for i in range(0, len(writes), MAX_WRITE_BATCH):
        batch = writes[i:i + MAX_WRITE_BATCH]
        path = os.path.join(out_dir, "_writes_%02d.json" % (i // MAX_WRITE_BATCH + 1))
        with open(path, "w", encoding="utf-8") as f:
            json.dump(batch, f, ensure_ascii=False)
        # --writes @file 只接受「当前目录内的相对路径」；用 stdin 规避绝对路径限制
        cli(["sheets", "+cells-set",
             "--spreadsheet-token", cfg["spreadsheet_token"],
             "--writes", "-"], input_text=json.dumps(batch, ensure_ascii=False))
        n += len(batch)
    return n


def link_write(cfg, sheet_key, a1, text, target_sheet_key, target_a1):
    """生成一条富文本链接写入项。"""
    return {
        "sheet_id": cfg["sheets"][sheet_key]["id"],
        "range": a1,
        "cells": [[{"rich_text": [{"type": "link", "text": text,
                                   "link": jump_url(cfg, target_a1, target_sheet_key)}]}]],
    }


def unmerge(cfg, sheet_key, rng):
    try:
        cli(["sheets", "+cells-unmerge",
             "--spreadsheet-token", cfg["spreadsheet_token"],
             "--sheet-id", cfg["sheets"][sheet_key]["id"], "--range", rng])
    except RuntimeError as e:
        if "merge" not in str(e).lower():
            raise


def merge(cfg, sheet_key, ranges):
    if not ranges:
        return
    spec = {"styles": [{"name": cfg["sheets"][sheet_key]["name"],
                        "cell_merges": [{"range": r} for r in ranges]}]}
    path = os.path.join(conf.ensure_output(), "_merges.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(spec, f, ensure_ascii=False)
    cli(["sheets", "+styles-put",
         "--spreadsheet-token", cfg["spreadsheet_token"], "--styles", "-"],
        input_text=json.dumps(spec, ensure_ascii=False))


def apply_styles(cfg, sheet_key, styles):
    """批量套用 cell_styles；+styles-put 单次展开上限 100，按 90 项切分。"""
    name = cfg["sheets"][sheet_key]["name"]
    for i in range(0, len(styles), 90):
        spec = {"styles": [{"name": name, "cell_styles": styles[i:i + 90]}]}
        cli(["sheets", "+styles-put",
             "--spreadsheet-token", cfg["spreadsheet_token"], "--styles", "-"],
            input_text=json.dumps(spec, ensure_ascii=False))
    return len(styles)


def insert_rows(cfg, sheet_key, position, count, inherit_style=True):
    """在 position 行之前插入 count 行（新行占据 position 起，原行下推）。
    lark-cli +dim-insert 无 --dimension：--position 数字=行，字母=列；
    --inherit-style before|after 选样式继承侧，默认 after。"""
    args = ["sheets", "+dim-insert",
            "--spreadsheet-token", cfg["spreadsheet_token"],
            "--sheet-id", cfg["sheets"][sheet_key]["id"],
            "--position", str(position), "--count", str(count)]
    if inherit_style:
        args += ["--inherit-style", "before"]
    cli(args)


def delete_rows(cfg, sheet_key, position, count):
    """删除 [position, position+count) 行（1-based 闭区间，不可逆）。
    +dim-delete 用 --range "N:M"，高风险需 --yes。"""
    rng = "%d:%d" % (position, position + count - 1)
    args = ["sheets", "+dim-delete",
            "--spreadsheet-token", cfg["spreadsheet_token"],
            "--sheet-id", cfg["sheets"][sheet_key]["id"],
            "--range", rng, "--yes"]
    cli(args)
