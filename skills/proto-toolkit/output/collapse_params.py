# -*- coding: utf-8 -*-
"""把 add_interface 误写成「接口一行 + 参数下一行」的块，压回表内既有写法：
第一个参数与接口同行（N/O/P/Q），第 2 个起才占用下一行。
做法：先按原坐标把参数整体上移一行，再一次性删除每组最后多出的参数行。
"""
import json
import io
import subprocess
import shutil
import sys

TOKEN = "YrK8sncCThe8UstV0yBcvkjQnMR"
EXE = shutil.which("lark-cli")
SRC = "si_block_style.json"
DRY = "--yes" not in sys.argv


def load():
    rows = json.load(io.open(SRC, encoding="utf-8"))["ranges"][0]["cells"]
    out = {}
    for i, r in enumerate(rows, 7):
        out[i] = r
    return out


def txt(cell):
    if not isinstance(cell, dict):
        return ""
    return str(cell.get("value") or "")


def collect(rows):
    groups = []
    cur = None
    for rn in sorted(rows):
        r = rows[rn]
        e = txt(r[4])
        n = txt(r[13]) if len(r) > 13 else ""
        o = txt(r[14]) if len(r) > 14 else ""
        if e and not e.startswith("▶"):
            cur = {"if": e, "r": rn, "if_n": n, "params": []}
            groups.append(cur)
        elif cur is not None and not e and (n or o):
            cur["params"].append(rn)
    return [g for g in groups if g["params"] and not g["if_n"]]


def cell_out(c):
    d = {}
    if isinstance(c, dict):
        if c.get("value") is not None:
            d["value"] = c["value"]
        if c.get("rich_text"):
            d["rich_text"] = c["rich_text"]
        if c.get("cell_styles"):
            d["cell_styles"] = c["cell_styles"]
        if c.get("border_styles"):
            d["border_styles"] = c["border_styles"]
    if "value" not in d and "rich_text" not in d:
        d["value"] = ""
    return d


def main():
    rows = load()
    groups = collect(rows)
    writes, deletes = [], []
    for g in groups:
        r = g["r"]
        n = len(g["params"])
        block = []
        for j in range(n):
            src = rows[g["params"][j]]
            block.append([cell_out(src[13]), cell_out(src[14]),
                          cell_out(src[15]), cell_out(src[16])])
        writes.append({"sheet_id": "88c520",
                       "range": "N%d:Q%d" % (r, r + n - 1),
                       "cells": block})
        deletes.append(r + n)          # 每组最后多出的参数行
    print("groups", len(groups), "writes", len(writes), "deletes", len(deletes))
    for g, d in zip(groups, deletes):
        print("  %s row%d params=%s delete row%d" % (g["if"], g["r"], g["params"], d))
    if DRY:
        print("dry-run；加 --yes 执行")
        return
    # 1) 参数整体上移一行（此时还没删行，坐标稳定）
    p = subprocess.run([EXE, "sheets", "+cells-set", "--spreadsheet-token", TOKEN,
                        "--writes", "-", "--as", "user", "--format", "json"],
                       input=json.dumps(writes, ensure_ascii=False),
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    print("write rc", p.returncode, (p.stdout or "")[:200])
    if p.returncode != 0:
        return
    # 2) 一次性删除多出的行（CLI 自动按降序）
    ranges = json.dumps(["%d:%d" % (d, d) for d in deletes])
    p = subprocess.run([EXE, "sheets", "+dim-delete", "--spreadsheet-token", TOKEN,
                        "--sheet-id", "88c520", "--ranges", ranges, "--yes",
                        "--as", "user", "--format", "json"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    print("delete rc", p.returncode, (p.stdout or "")[:300])


if __name__ == "__main__":
    main()
