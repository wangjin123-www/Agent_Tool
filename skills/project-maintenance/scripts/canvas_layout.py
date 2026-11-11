#!/usr/bin/env python3
"""JSON Canvas (.canvas) 检查/自动布局工具。

用法:
  python canvas_layout.py check <file.canvas>
  python canvas_layout.py layout <file.canvas> [--out <file.canvas>] [--direction TB|LR]

check:
  - 校验 JSON Canvas 基本结构（id 唯一、边端点存在、side 合法）
  - 估算 text 节点的最小尺寸，文本可能溢出时告警
  - 检测节点重叠、group 与外部节点重叠、group 相互重叠
  - 估算边标签占位框，检测标签压在其它节点上的情况
  - 过长边标签告警（建议缩短或把条件详情移到正文/备注节点）

layout:
  - 先按文本内容自动调整 text 节点尺寸
  - group 内的节点按内部边做分层布局（DFS 断环 + 最长路径 rank）
  - group 之间与未分组节点横向排列；group 框按子节点重新计算
  - 自动选择边 fromSide/toSide

布局规则参考:
  - JSON Canvas 1.0: https://github.com/obsidianmd/jsoncanvas
  - Canvas Positioning Toolkit（网格自动排列、行高取最高卡片）:
    https://github.com/valleytheknight/Canvas-Positioning-Toolkit
  - Flashcard Canvas（树形 Tidy 布局）:
    https://github.com/jcesguerram/flashcard-canvas
  - AgriciDaniel/claude-obsidian canvas skill（自动定位、零重叠校验）:
    https://github.com/AgriciDaniel/claude-obsidian

注意: layout 面向流程图/状态机图；固定色带式架构图请只用 check，
      不要用 layout 打乱人工排好的分层色带。
"""
import argparse
import json
import re
import sys
from collections import defaultdict, deque
from pathlib import Path

PAD = 40                 # group 内边距
GROUP_LABEL_H = 40       # group 顶部标签预留高度
H_GAP = 100              # 同层节点水平间距
V_GAP = 140              # 层间垂直间距（给边标签留空间）
TOP_GAP = 240            # group / 顶层节点之间的间距
MIN_TEXT_W, MIN_TEXT_H = 240, 80
MAX_TEXT_W = 680
LABEL_MAX_UNITS = 24     # CJK 记 2 unit；约 12 个汉字。长条件放节点/图例
LABEL_PAD_X = 16
LABEL_PAD_Y = 8
EDGE_COLOR_ONEWAY = "4"  # 单向边：绿
EDGE_COLOR_TWOWAY = "6"  # 双向边（A→B + B→A 成对）：紫
SIDES = {"top", "right", "bottom", "left"}
CJK_RE = re.compile(r"[⺀-鿿＀-￯]")


def units(text: str) -> int:
    return sum(2 if CJK_RE.match(ch) else 1 for ch in text)


def label_size(text: str) -> tuple:
    """Obsidian 边标签的粗估尺寸（CJK 14px、ASCII 8px，另加背景内边距）。"""
    cjk = sum(1 for ch in text if CJK_RE.match(ch))
    ascii_cnt = len(text) - cjk
    return max(40, cjk * 14 + ascii_cnt * 8 + LABEL_PAD_X), 20 + LABEL_PAD_Y


def est_text_size(text: str) -> tuple:
    """按 14px 字号粗估 text 节点需要的宽高（CJK 2 units，ASCII 1 unit）。"""
    lines = text.split("\n") or [""]
    max_units = max(units(line) for line in lines)
    width = max(MIN_TEXT_W, min(MAX_TEXT_W, max_units * 8 + 40))
    height = max(MIN_TEXT_H, len(lines) * 24 + 32)
    return int(width), int(height)


def rect(n):
    return (n["x"], n["y"], n["x"] + n["width"], n["y"] + n["height"])


def overlap(a, b, margin=0):
    return not (
        a[2] + margin <= b[0]
        or b[2] + margin <= a[0]
        or a[3] + margin <= b[1]
        or b[3] + margin <= a[1]
    )


def center(n):
    return (n["x"] + n["width"] / 2, n["y"] + n["height"] / 2)


def side_point(n, side):
    """节点某一边的中点；未指定 side 时退回节点中心。"""
    cx, cy = center(n)
    if side == "top":
        return (cx, n["y"])
    if side == "bottom":
        return (cx, n["y"] + n["height"])
    if side == "left":
        return (n["x"], cy)
    if side == "right":
        return (n["x"] + n["width"], cy)
    return (cx, cy)


def inside(n, g):
    cx, cy = center(n)
    return g["x"] <= cx <= g["x"] + g["width"] and g["y"] <= cy <= g["y"] + g["height"]


def classify_edges(data):
    """返回 (one_way_ids, two_way_ids)。

    同一对节点同时存在 A→B 与 B→A 时视为双向；两条边都归为双向。
    其余（含同向重复边）为单向。
    """
    pairs = defaultdict(list)
    for e in data.get("edges", []):
        a, b = e.get("fromNode"), e.get("toNode")
        if a is None or b is None:
            continue
        pairs[tuple(sorted((a, b)))].append(e)
    one_way, two_way = set(), set()
    for es in pairs.values():
        dirs = {(e.get("fromNode"), e.get("toNode")) for e in es}
        target = two_way if len(dirs) >= 2 else one_way
        for e in es:
            if e.get("id") is not None:
                target.add(e["id"])
    return one_way, two_way


def colorize(data):
    """按单向/双向统一边颜色；返回 data。"""
    one_way, two_way = classify_edges(data)
    for e in data.get("edges", []):
        if e.get("id") in two_way:
            e["color"] = EDGE_COLOR_TWOWAY
        elif e.get("id") in one_way:
            e["color"] = EDGE_COLOR_ONEWAY
    return data


def load(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return data


def save(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def validate(data):
    issues = []
    nodes = data.get("nodes", [])
    edges = data.get("edges", [])
    ids = set()
    for n in nodes:
        for key in ("id", "type", "x", "y", "width", "height"):
            if key not in n:
                issues.append(f"节点 {n.get('id', '?')} 缺字段 {key}")
        if n.get("id") in ids:
            issues.append(f"节点 id 重复: {n.get('id')}")
        ids.add(n.get("id"))
        if n.get("type") not in ("text", "group", "file", "link"):
            issues.append(f"节点 {n.get('id')} type 非法: {n.get('type')}")
    for e in edges:
        for key in ("id", "fromNode", "toNode"):
            if key not in e:
                issues.append(f"边 {e.get('id', '?')} 缺字段 {key}")
        if e.get("fromNode") not in ids:
            issues.append(f"边 {e.get('id')} fromNode 不存在: {e.get('fromNode')}")
        if e.get("toNode") not in ids:
            issues.append(f"边 {e.get('id')} toNode 不存在: {e.get('toNode')}")
        for side_key in ("fromSide", "toSide"):
            if side_key in e and e[side_key] not in SIDES:
                issues.append(f"边 {e.get('id')} {side_key} 非法: {e.get(side_key)}")
    return issues


def check(data):
    issues = validate(data)
    one_way, two_way = classify_edges(data)
    for e in data.get("edges", []):
        kind = "双向" if e.get("id") in two_way else "单向"
        expected = EDGE_COLOR_TWOWAY if kind == "双向" else EDGE_COLOR_ONEWAY
        if e.get("color") != expected:
            issues.append(
                f"边 {e.get('id')} 为{kind}边，颜色应为 {expected}，"
                f"当前 {e.get('color', '未设置')}（跑 colorize 自动上色）"
            )

    nodes = [n for n in data.get("nodes", []) if n.get("type") != "group"]
    groups = [n for n in data.get("nodes", []) if n.get("type") == "group"]

    # text 尺寸
    for n in nodes:
        if n.get("type") != "text":
            continue
        ew, eh = est_text_size(n.get("text", ""))
        if n["width"] < ew or n["height"] < eh:
            issues.append(
                f"节点 {n['id']} 文本可能溢出: 当前 {n['width']}x{n['height']}, "
                f"建议 >= {ew}x{eh}"
            )

    # 非 group 节点互撞
    for i, a in enumerate(nodes):
        for b in nodes[i + 1:]:
            if overlap(rect(a), rect(b)):
                issues.append(f"节点重叠: {a['id']} <-> {b['id']}")

    # group 互撞
    for i, a in enumerate(groups):
        for b in groups[i + 1:]:
            if overlap(rect(a), rect(b)):
                issues.append(f"group 重叠: {a['id']} <-> {b['id']}")

    # group 与不属于它的节点相撞
    for g in groups:
        for n in nodes:
            if overlap(rect(g), rect(n)) and not inside(n, g):
                issues.append(f"group {g['id']} 压到外部节点 {n['id']}")

    # 边标签粗估占位（标签在两端中心连线的中点）
    node_by_id = {n["id"]: n for n in data.get("nodes", [])}
    label_boxes = []
    for e in data.get("edges", []):
        label = e.get("label", "")
        if not label:
            continue
        if units(label) > LABEL_MAX_UNITS:
            issues.append(
                f"边 {e['id']} 标签过长（{units(label)} units），"
                f"建议 <= {LABEL_MAX_UNITS}（约 12 汉字）：改用 T1/T2 短编号 + 图例节点，"
                f"或把条件写进节点正文"
            )
        s, t = node_by_id.get(e.get("fromNode")), node_by_id.get(e.get("toNode"))
        if not s or not t:
            continue
        sx, sy = side_point(s, e.get("fromSide"))
        tx, ty = side_point(t, e.get("toSide"))
        lw, lh = label_size(label)
        box = (min(sx, tx) + abs(tx - sx) / 2 - lw / 2,
               min(sy, ty) + abs(ty - sy) / 2 - lh / 2,
               min(sx, tx) + abs(tx - sx) / 2 + lw / 2,
               min(sy, ty) + abs(ty - sy) / 2 + lh / 2)
        for n in nodes:
            if n["id"] in (e.get("fromNode"), e.get("toNode")):
                continue
            if overlap(box, rect(n), margin=8):
                issues.append(f"边 {e['id']} 标签可能压到节点 {n['id']}")
        label_boxes.append((e["id"], box))

    # 边标签之间互相重叠（双向边同一走廊时最常见）
    for i, (id_a, box_a) in enumerate(label_boxes):
        for id_b, box_b in label_boxes[i + 1:]:
            if overlap(box_a, box_b, margin=8):
                issues.append(f"边标签重叠: {id_a} <-> {id_b}")
    return issues


def _layout_set(members, edges, direction="TB"):
    """对一组节点做 DFS 断环 + 最长路径分层，返回 {id:(x,y)}。"""
    if not members:
        return {}
    ids = {n["id"] for n in members}
    adj = defaultdict(list)
    for e in edges:
        if e.get("fromNode") in ids and e.get("toNode") in ids:
            adj[e["fromNode"]].append(e["toNode"])

    color = {}
    post = []
    forward = []

    def dfs(u):
        color[u] = 1
        for v in adj[u]:
            if color.get(v) == 1:      # 回边，断开
                continue
            forward.append((u, v))
            if color.get(v, 0) == 0:
                dfs(v)
        color[u] = 2
        post.append(u)

    for n in members:
        if color.get(n["id"], 0) == 0:
            dfs(n["id"])

    rank = {n["id"]: 0 for n in members}
    for u in reversed(post):
        for a, b in forward:
            if a == u:
                rank[b] = max(rank[b], rank[u] + 1)

    groups_by_rank = defaultdict(list)
    for n in members:
        groups_by_rank[rank[n["id"]]].append(n)

    pos = {}
    if direction == "LR":
        col_w = {r: max(n["width"] for n in groups_by_rank[r])
                 for r in groups_by_rank}
        x_of = {}
        x_cursor = 0
        for r in sorted(groups_by_rank):
            x_of[r] = x_cursor
            x_cursor += col_w[r] + H_GAP
        for r in sorted(groups_by_rank):
            row = sorted(groups_by_rank[r], key=lambda n: (n["y"], n["x"], n["id"]))
            y_cursor = 0
            for n in row:
                pos[n["id"]] = (x_of[r], y_cursor)
                y_cursor += n["height"] + V_GAP
    else:
        y_cursor = 0
        for r in sorted(groups_by_rank):
            row = sorted(groups_by_rank[r], key=lambda n: (n["x"], n["id"]))
            row_h = max(n["height"] for n in row)
            x_cursor = 0
            for n in row:
                pos[n["id"]] = (x_cursor, y_cursor)
                x_cursor += n["width"] + H_GAP
            y_cursor += row_h + V_GAP
    return pos


def layout(data, direction="TB"):
    nodes = data.get("nodes", [])
    edges = data.get("edges", [])
    groups = [n for n in nodes if n.get("type") == "group"]
    content = [n for n in nodes if n.get("type") != "group"]

    # 按文本内容修正尺寸
    for n in content:
        if n.get("type") == "text":
            n["width"], n["height"] = est_text_size(n.get("text", ""))

    # group 归属：取包含节点中心的最小 group
    member_of = {}
    for n in content:
        candidates = [g for g in groups if inside(n, g)]
        if candidates:
            g = min(candidates, key=lambda x: x["width"] * x["height"])
            member_of[n["id"]] = g["id"]

    members = defaultdict(list)
    for n in content:
        members[member_of.get(n["id"])].append(n)

    # group 内部布局
    group_local = {}
    for g in groups:
        ms = members.get(g["id"], [])
        pos = _layout_set(ms, edges, "TB")
        if not ms:
            continue
        min_x = min(pos[n["id"]][0] for n in ms)
        min_y = min(pos[n["id"]][1] for n in ms)
        max_x = max(pos[n["id"]][0] + n["width"] for n in ms)
        max_y = max(pos[n["id"]][1] + n["height"] for n in ms)
        group_local[g["id"]] = {
            "members": ms,
            "pos": pos,
            "w": max_x - min_x + 2 * PAD,
            "h": max_y - min_y + 2 * PAD + GROUP_LABEL_H,
            "min_x": min_x,
            "min_y": min_y,
        }

    # 顶层排列：先 group（按原 x），再未分组节点（按原 x）
    items = list(groups) + members.get(None, [])
    items.sort(key=lambda n: (0 if n.get("type") == "group" else 1, n["x"], n["y"]))
    x_cursor = 0
    y_cursor = 0
    for item in items:
        if item.get("type") == "group":
            gl = group_local.get(item["id"])
            if not gl:
                item["x"], item["y"] = x_cursor, y_cursor
                x_cursor += item["width"] + TOP_GAP
                continue
            item["x"], item["y"] = x_cursor, y_cursor
            item["width"], item["height"] = gl["w"], gl["h"]
            for n in gl["members"]:
                px, py = gl["pos"][n["id"]]
                n["x"] = item["x"] + PAD + (px - gl["min_x"])
                n["y"] = item["y"] + PAD + GROUP_LABEL_H + (py - gl["min_y"])
            x_cursor += item["width"] + TOP_GAP
        else:
            item["x"], item["y"] = x_cursor, y_cursor
            x_cursor += item["width"] + TOP_GAP

    # 无 group 时对所有节点分层
    if not groups:
        pos = _layout_set(content, edges, direction)
        for n in content:
            n["x"], n["y"] = pos[n["id"]]

    # 归一化到正坐标
    all_nodes = data.get("nodes", [])
    min_x = min(n["x"] for n in all_nodes)
    min_y = min(n["y"] for n in all_nodes)
    for n in all_nodes:
        n["x"] -= min_x
        n["y"] -= min_y

    # 自动选边方向
    node_by_id = {n["id"]: n for n in all_nodes}
    for e in data.get("edges", []):
        s, t = node_by_id.get(e.get("fromNode")), node_by_id.get(e.get("toNode"))
        if not s or not t:
            continue
        dx = center(t)[0] - center(s)[0]
        dy = center(t)[1] - center(s)[1]
        if abs(dx) >= abs(dy):
            if dx >= 0:
                e["fromSide"], e["toSide"] = "right", "left"
            else:
                e["fromSide"], e["toSide"] = "left", "right"
        else:
            if dy >= 0:
                e["fromSide"], e["toSide"] = "bottom", "top"
            else:
                e["fromSide"], e["toSide"] = "top", "bottom"
    return colorize(data)


def main():
    parser = argparse.ArgumentParser(description="Obsidian JSON Canvas 检查/自动布局")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_check = sub.add_parser("check", help="检查重叠、文本溢出、过长边标签")
    p_check.add_argument("file")
    p_layout = sub.add_parser("layout", help="自动布局（流程图/状态机图）")
    p_layout.add_argument("file")
    p_layout.add_argument("--out")
    p_layout.add_argument("--direction", choices=("TB", "LR"), default="TB")
    p_color = sub.add_parser("colorize", help="按单向/双向统一边颜色（不改坐标）")
    p_color.add_argument("file")
    p_color.add_argument("--out")
    args = parser.parse_args()

    data = load(args.file)
    if args.cmd == "colorize":
        out = args.out or args.file
        save(out, colorize(data))
        print(f"colorize written: {out}")
        issues = check(data)
        for msg in issues:
            print("WARN " + msg)
        return 0
    if args.cmd == "check":
        issues = check(data)
        for msg in issues:
            print("WARN " + msg)
        print("OK" if not issues else f"{len(issues)} issue(s)")
        return 0 if not issues else 1

    data = layout(data, args.direction)
    out = args.out or args.file
    save(out, data)
    print(f"layout written: {out}")
    issues = check(data)
    for msg in issues:
        print("WARN " + msg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
