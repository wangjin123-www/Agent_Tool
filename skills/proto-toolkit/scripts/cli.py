# -*- coding: utf-8 -*-
"""proto-toolkit 唯一入口（命令行传参，无交互问答）。

    python cli.py platform                 显示当前活动平台与已注册平台
    python cli.py read [--json]            读取并概览整个协议
    python cli.py query <关键词> [--json]  按名称/描述/消息id 搜协议实体，打印详情与关联
    python cli.py show <类型> <名称>       定向查看：service|interface|struct|enum|error
    python cli.py pull [--out <path>]      ① 多维表格 → output/protocol.json（git 提交，可 diff）
    python cli.py check [path]             ② 检查 protocol.json 检测字段（❌ 违规 / ⚠️ 警告）
    python cli.py gen [path]               ③ protocol.json → codegen/c/generated/*.h/.c
"""
import argparse
import json
import os
import sys
from datetime import datetime

_HERE = os.path.dirname(os.path.abspath(__file__))
if __package__ in (None, ""):
    sys.path.insert(0, os.path.dirname(_HERE))
    from scripts.common import conf
    from scripts import platforms
    import scripts.pull as pull
    from scripts import gen
else:
    from .common import conf
    from . import platforms
    from . import pull
    from . import gen


# ------------------------------------------------------------------ 模型加载
def _active_reader():
    key = conf.platform()
    cfg = conf.platform_cfg(key)
    return platforms.make_reader(key, cfg), key, cfg


def load_model():
    reader, key, cfg = _active_reader()
    return reader.read()


# ------------------------------------------------------------------ 渲染
def _line(label, value):
    if value in (None, "", []):
        return ""
    if isinstance(value, list):
        value = ", ".join(str(v) for v in value) if value else ""
    if not value:
        return ""
    return "  %-10s %s" % (label + ":", value)


def render_overview(m):
    c = m["counts"]
    lines = []
    lines.append("═" * 64)
    lines.append(" 平台 %s — %s" % (m["platform"], m["platform_name"]))
    s = m["source"]
    lines.append(" 数据源: %s  %s" % (s.get("type"), s.get("url") or s.get("base_token")))
    lines.append("─" * 64)
    lines.append(" 服务 %d │ 接口 %d │ 结构体 %d │ 枚举 %d（值 %d）│ 成员变量 %d │ 错误码 %d（组 %d）"
                 % (c["services"], c["interfaces"], c["structs"], c["enums"],
                    c["enum_values"], c["member_variables"], c["error_codes"], c["error_groups"]))
    lines.append("")
    lines.append(" 服务清单:")
    for svc in m["services"]:
        tag = "%s %s" % (svc["service_id"], svc["namespace"]) if (svc["service_id"] or svc["namespace"]) else ""
        lines.append("   · %-22s %-16s %d 接口  %s"
                     % (svc["name"], tag, len(svc["interface_names"]), svc["desc"]))
    lines.append("")
    lines.append(" 接口一览（按服务分组）:")
    by_svc = {}
    for i in m["interfaces"]:
        by_svc.setdefault(i["service"] or "(未归服务)", []).append(i)
    for svc in sorted(by_svc):
        lines.append("   [%s]" % svc)
        for i in by_svc[svc]:
            p = ""
            if i["param"]:
                p = " param=%s:%s" % (i["param"]["name"], i["param"]["type"])
            refs = []
            if i["struct_refs"]: refs.append("struct=" + ",".join(i["struct_refs"]))
            if i["enum_refs"]: refs.append("enum=" + ",".join(i["enum_refs"]))
            rtxt = ("  [" + " ".join(refs) + "]") if refs else ""
            lines.append("     · %-22s %-10s %-6s %s %s%s"
                         % (i["name"], i["if_type"], i["direction"], i["msg_id"], p, rtxt))
    lines.append("═" * 64)
    return "\n".join(lines)


def render_interface(i, m):
    L = []
    L.append("═ 接口: %s" % i["name"])
    L.append(_line("服务", i["service"]))
    L.append(_line("方向", i["direction"]))
    L.append(_line("类型", i["if_type"]))
    L.append(_line("消息id", i["msg_id"]))
    L.append(_line("发送类型", i["tx_type"]))
    L.append(_line("传输层", i["transport"]))
    L.append(_line("QoS", i["qos"]))
    L.append(_line("描述", i["desc"]))
    if i["param"]:
        p = i["param"]
        L.append("  参数:")
        L.append("    · %-16s %-8s %-5s %s" % (p["name"], p["type"], p["dir"], p["desc"]))
    if i["struct_refs"]:
        L.append("  引用结构体:")
        for sn in i["struct_refs"]:
            st = m["index"]["structs_by_name"].get(sn)
            extra = ("（%d 成员）" % len(st["members"])) if st else ""
            L.append("    · %s%s" % (sn, extra))
    if i["enum_refs"]:
        L.append("  引用枚举:")
        for en in i["enum_refs"]:
            e = m["index"]["enums_by_name"].get(en)
            extra = ("（%d 值）" % len(e["values"])) if e else ""
            L.append("    · %s%s" % (en, extra))
    if i["related"]:
        L.append("  关联接口: " + ", ".join(i["related"]))
    if i["error_refs"]:
        L.append("  关联错误码: " + ", ".join(i["error_refs"]))
    return "\n".join(x for x in L if x != "")


def render_struct(s, m):
    L = ["═ 结构体: %s" % s["name"]]
    L.append(_line("描述", s["desc"]))
    if s["members"]:
        L.append("  成员变量:")
        for mb in s["members"]:
            er = " → enum:%s" % ",".join(mb["enum_refs"]) if mb["enum_refs"] else ""
            arr = (" [n=%s bit=%s]" % (mb.get("len"), mb.get("bit_range"))
                   if mb.get("len") else "")
            L.append("    · byte=%-6s bit=%-5s %-16s %-10s %s%s%s"
                     % (mb["byte"], mb["bit"], mb["name"], mb["type"], mb["desc"], arr, er))
    if s["interface_refs"]:
        L.append("  被接口引用: " + ", ".join(s["interface_refs"]))
    return "\n".join(x for x in L if x != "")


def render_enum(e, m):
    L = ["═ 枚举: %s" % e["name"]]
    if e["values"]:
        L.append("  取值:")
        for v in e["values"]:
            L.append("    · %-6s = %-22s %s" % (v["value"], v["name"], v["desc"]))
    else:
        L.append("  （无取值记录）")
    if e["member_refs"]:
        L.append("  被成员变量引用: " + ", ".join(e["member_refs"]))
    if e["interface_refs"]:
        L.append("  被接口引用: " + ", ".join(e["interface_refs"]))
    return "\n".join(x for x in L if x != "")


def render_error(e, m):
    L = ["═ 错误码: %s(%s/%s)" % (e["group"], e["value"], e["c_name"])]
    L.append(_line("描述", e["desc"]))
    L.append(_line("适用消息", e["applies_to"]))
    if e["struct_refs"]:
        L.append("  引用结构体: " + ", ".join(e["struct_refs"]))
    if e["interface_refs"]:
        L.append("  引用接口: " + ", ".join(e["interface_refs"]))
    return "\n".join(x for x in L if x != "")


def render_service(s, m):
    L = ["═ 服务: %s" % s["name"]]
    L.append(_line("服务id", s["service_id"]))
    L.append(_line("命名空间", s["namespace"]))
    L.append(_line("描述", s["desc"]))
    if s["interface_names"]:
        L.append("  接口列表:")
        for nm in s["interface_names"]:
            it = m["index"]["interfaces_by_name"].get(nm)
            extra = ("  %s %s" % (it["direction"], it["msg_id"])) if it else ""
            L.append("    · %-22s%s" % (nm, extra))
    return "\n".join(x for x in L if x != "")


# ------------------------------------------------------------------ pull / check / gen
def cmd_pull(out_path=None, raw_path=None, from_raw=None, emit_model=False):
    """① 多维表格 API → base_raw.json（原始记录快照，唯一提交物）
       ② 内存解析 → 直接供 check/gen 使用（默认不落 protocol.json）

    只落一份 JSON：raw 是唯一真源，解析在内存里做，避免两份文件重复维护。
    需要人工 review 解析结果时加 --model 才额外导出 protocol.json。
    """
    if from_raw:
        raw = pull.load_raw(from_raw)
        model = pull.model_from_raw(raw, conf.platform_cfg(conf.platform()))
        data, warn = pull.transform(model)
        print("解析（离线重放，源 %s）" % from_raw)
    else:
        # 联网：一次 API 读取 → raw 快照 → 内存解析（raw 与解析同源，不重复请求）
        key = conf.platform()
        cfg = conf.platform_cfg(key)
        reader = platforms.make_reader(key, cfg)
        try:
            raw = reader.read_raw()
        except Exception as e:
            # 表 id 失效是最常见的联网失败原因，直接指路 doctor 而不是抛原始报错
            raise RuntimeError(
                "读取多维表格失败：%s\n"
                "表 id 可能已失效（Base 重建表会换 id）。先跑：\n"
                "  python scripts/cli.py doctor --fix      按表名重解析失效 id\n"
                "  python scripts/cli.py doctor            仅体检不改" % str(e)[:300])
        rpath = pull.save_raw(raw, raw_path)
        model = reader.assemble_raw(raw)
        data, warn = pull.transform(model)
        print("pull → %s（原始记录快照，唯一提交物）" % rpath)

    if emit_model:
        print("      → %s（--model 导出的解析视图，供人工 review）"
              % pull.save(data, out_path))

    c = data["counts"]
    print(" 服务 %d │ 接口 %d │ 结构体 %d │ 枚举 %d（值 %d）│ 成员 %d │ 错误码 %d"
          % (c["services"], c["interfaces"], c["structs"], c["enums"],
             c["enum_values"], c["member_variables"], c["error_codes"]))
    bad, warns = pull.check_issues(data)
    for kind, name, msg in bad:
        print(" ❌ %s %s: %s" % (kind, name, msg))
    for kind, name, msg in warns:
        print(" ⚠️ %s %s: %s" % (kind, name, msg))
    for w in warn:
        print(" ⚠️ 解析: %s" % w)
    if bad:
        print("（%d 条违规：检测未通过，gen 将阻断；用 fix 自动修复或去表里改）" % len(bad))
    if not bad and not warns and not warn:
        print(" 检测全部通过，无解析警告")
    return 0


def cmd_gen(path=None, langs=None, fresh=False):
    if fresh:
        print("--fresh：先联网拉取最新快照…")
        rc = cmd_pull()
        if rc != 0:
            print("pull 失败，中止 gen")
            return rc
        path = None
    if path is None:
        raw_path = pull.raw_path_default()
        if os.path.exists(raw_path):
            mtime = datetime.fromtimestamp(os.path.getmtime(raw_path))
            print("本地快照：%s（文件修改于 %s）"
                  % (raw_path, mtime.strftime("%Y-%m-%d %H:%M:%S")))
            print("  协议有更新请先 `pull`，或用 `gen --fresh` 先拉最新再生成")
    data = pull.load_any(path)
    bad, warns = pull.check_issues(data)
    if bad:
        print("gen 阻断：检测未通过，共 %d 条 ❌ 违规，先修正后重新 pull：" % len(bad))
        for kind, name, msg in bad:
            print("  ❌ %s %s: %s" % (kind, name, msg))
        return 1
    if warns:
        for kind, name, msg in warns:
            print("⚠️ %s %s: %s" % (kind, name, msg))
    result = gen.generate(langs, data)
    if not result:
        print("未指定可生成语言（--lang none）")
        return 0
    skipped = result.pop("_skipped", None)
    print("gen 完成（检测通过，%d 条警告）：" % len(warns))
    for lang, paths in result.items():
        print(" [%s]" % lang)
        for p in paths:
            print("  → %s" % p)
    if skipped:
        print(" 跳过未就绪语言: %s" % ", ".join(skipped))
    return 0


def cmd_langs():
    print("已注册语言（codegen/config/languages.json）：")
    for lang, name, status in gen.available():
        print("  %-8s %-16s %s" % (lang, name, status))
    print("默认语言: %s" % conf.languages().get("default", "c"))
    return 0


# ------------------------------------------------------------------ fix（自动修复多维表格）
def cmd_doctor(fix=False):
    """体检 config 的表坐标/字段/检测规则与线上 Base 是否一致；--fix 回写失效坐标与字段名。"""
    try:
        from . import doctor
    except ImportError:
        from scripts import doctor

    if fix:
        changes = doctor.autofix()
        if not changes:
            print("无需修复：表 id 与字段名均有效")
        for kind, role, key, old, new in changes:
            print("  已修正 %-14s %-22s %-12s %s → %s" % (kind, role, key, old, new))
        if changes:
            print("（已写回 config，建议 git diff 确认后再 pull）")

    issues = doctor.verify()
    if not issues:
        print("体检通过：表 id / 字段语义 / link 目标 / split / 降级规则均与线上一致")
        return 0
    n_err = 0
    for level, role, key, msg in issues:
        print("%s %-20s %-14s %s" % ("❌" if level == "ERROR" else "⚠️", role, key, msg))
        n_err += (level == "ERROR")
    print()
    print("结论：%d 个错误 / %d 个提示" % (n_err, len(issues) - n_err))
    if n_err:
        print("处理：表 id 或字段改名可试 `--fix`；表被删/改名、检测公式改写需人工更新 config")
        return 1
    return 0


def cmd_fix(dry_run=True, raw_path=None):
    """自动修复多维表格：R1 消息id / R2 枚举值 / R3 select 选项 / R4 类型别名 / R5 双向回填。

    基于 raw 快照计算差异（不重复读表两次）。--dry-run 只列计划（默认）。
    """
    try:
        from . import fix
    except ImportError:
        from scripts import fix

    key = conf.platform()
    cfg = conf.platform_cfg(key)
    raw = pull.load_raw(raw_path)
    plan = fix.build_plan(cfg, raw)

    print("修复计划（%s）：" % ("预览 dry-run" if dry_run else "执行"))
    print(" " + plan.summary())
    for note in plan.notes:
        print(" ⚠️ 需人工: %s" % note)

    if plan.empty():
        print(" 无需修复")
        return 0
    if dry_run:
        print("（未写表；加 --apply 执行）")
        return 0

    nf, nr = fix.apply_plan(cfg, plan)
    print("已写表：字段 %d 个 / 记录 %d 条" % (nf, nr))
    print("建议复核：python scripts/cli.py pull")
    return 0


# ------------------------------------------------------------------ 命令
def cmd_platform():
    key = conf.platform()
    cfg = conf.platform_cfg(key)
    print("活动平台: %s — %s" % (key, cfg.get("name", "")))
    print("数据源:   %s" % (cfg.get("source", {}).get("url") or cfg.get("source", {})))
    print("实现模块: platforms/%s" % cfg.get("module", ""))
    print("已注册实现: %s" % ", ".join(platforms.available()))
    print("已配置平台: %s" % ", ".join(sorted(conf.platforms())))
    return 0


def _dump_json(m, tag):
    os.makedirs(conf.OUTPUT_DIR, exist_ok=True)
    path = os.path.join(conf.OUTPUT_DIR, tag)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(m, f, ensure_ascii=False, indent=2)
    return path


def cmd_read(as_json=False, from_raw=None):
    m = pull.model_from_raw(pull.load_raw(from_raw), conf.platform_cfg(conf.platform())) \
        if from_raw else load_model()
    print(render_overview(m))
    if as_json:
        path = _dump_json(m, "protocol_read.json")
        print("\nJSON 快照 → %s" % path)
    return 0


def cmd_query(keyword, as_json=False):
    kw = keyword.strip().lower()
    m = load_model()
    hits = []
    for i in m["interfaces"]:
        if kw in (i["name"] or "").lower() or kw in (i["desc"] or "").lower() \
                or kw in (i["msg_id"] or "").lower():
            hits.append(("interface", i["name"]))
    for s in m["structs"]:
        if kw in (s["name"] or "").lower() or kw in (s["desc"] or "").lower():
            hits.append(("struct", s["name"]))
    for e in m["enums"]:
        if kw in (e["name"] or "").lower():
            hits.append(("enum", e["name"]))
    for s in m["services"]:
        if kw in (s["name"] or "").lower() or kw in (s["desc"] or "").lower():
            hits.append(("service", s["name"]))
    for er in m["errors"]:
        if kw in (er["group"] or "").lower() or kw in (er["c_name"] or "").lower() \
                or kw in (er["value"] or "").lower():
            hits.append(("error", "%s/%s" % (er["group"], er["c_name"])))

    if not hits:
        print("未找到匹配: %s" % keyword)
        return 1
    print("命中 %d 项（关键词: %s）\n" % (len(hits), keyword))
    for kind, nm in hits:
        if kind == "interface":
            print(render_interface(m["index"]["interfaces_by_name"][nm], m)); print()
        elif kind == "struct":
            print(render_struct(m["index"]["structs_by_name"][nm], m)); print()
        elif kind == "enum":
            print(render_enum(m["index"]["enums_by_name"][nm], m)); print()
        elif kind == "service":
            print(render_service(m["index"]["services_by_name"][nm], m)); print()
        elif kind == "error":
            grp, cn = nm.split("/", 1)
            for er in m["errors"]:
                if er["group"] == grp and er["c_name"] == cn:
                    print(render_error(er, m)); print()
                    break
    if as_json:
        path = _dump_json({"keyword": keyword, "hits": hits}, "query_result.json")
        print("JSON 结果 → %s" % path)
    return 0


def cmd_show(kind, name):
    m = load_model()
    kind = kind.lower()
    name_l = name.strip().lower()

    def _pick(d):
        exact = d.get(name)
        if exact:
            return exact
        for k, v in d.items():
            if name_l in (k or "").lower():
                return v
        return None

    if kind in ("service", "svc"):
        s = _pick(m["index"]["services_by_name"]); print(render_service(s, m) if s else "未找到服务: %s" % name)
    elif kind in ("interface", "if"):
        i = _pick(m["index"]["interfaces_by_name"]); print(render_interface(i, m) if i else "未找到接口: %s" % name)
    elif kind in ("struct", "structure", "ds"):
        s = _pick(m["index"]["structs_by_name"]); print(render_struct(s, m) if s else "未找到结构体: %s" % name)
    elif kind in ("enum",):
        e = _pick(m["index"]["enums_by_name"]); print(render_enum(e, m) if e else "未找到枚举: %s" % name)
    elif kind in ("error", "err"):
        found = [er for er in m["errors"]
                 if name_l in (er["group"] or "").lower()
                 or name_l in (er["c_name"] or "").lower()
                 or name_l in (er["value"] or "").lower()]
        if not found:
            print("未找到错误码: %s" % name); return 1
        for er in found:
            print(render_error(er, m)); print()
    else:
        print("未知类型: %s（可选: service|interface|struct|enum|error）" % kind)
        return 2
    return 0


def main():
    parser = argparse.ArgumentParser(prog="cli.py", description="读懂通信协议（飞书多维表格）",
                                     add_help=True)
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("platform", help="显示活动平台与已注册平台")

    p_read = sub.add_parser("read", help="读取并概览整个协议")
    p_read.add_argument("--json", action="store_true", help="同时落盘 JSON 快照到 output/")
    p_read.add_argument("--from-raw", default=None, help="不联网，从 base_raw.json 离线读取")

    p_q = sub.add_parser("query", help="按关键词搜协议实体")
    p_q.add_argument("keyword")
    p_q.add_argument("--json", action="store_true", help="同时落盘 JSON 结果")

    p_show = sub.add_parser("show", help="定向查看某个实体")
    p_show.add_argument("kind", help="service|interface|struct|enum|error")
    p_show.add_argument("name")

    p_pull = sub.add_parser("pull", help="多维表格 → base_raw.json（唯一提交物；解析在内存完成；自带 ❌/⚠️ 统计，check 已并入）")
    p_pull.add_argument("--raw", default=None, help="base_raw.json 输出路径，缺省 output/base_raw.json")
    p_pull.add_argument("--from-raw", default=None, help="不联网，从已有 base_raw.json 离线重放")
    p_pull.add_argument("--model", action="store_true",
                        help="额外导出解析视图 protocol.json（供人工 review，默认不落）")
    p_pull.add_argument("--out", default=None,
                        help="配合 --model 的 protocol.json 输出路径，缺省 output/protocol.json")

    p_gen = sub.add_parser("gen", help="解析并生成代码；可直接传 base_raw.json")
    p_gen.add_argument("path", nargs="?", default=None, help="base_raw.json 或 protocol.json 路径")
    p_gen.add_argument("--lang", default=None,
                       help="语言：c|arxml|java|all|none（缺省按注册表 default）")
    p_gen.add_argument("--fresh", action="store_true",
                       help="先 pull 拉最新快照再 gen（避免用旧快照）")

    sub.add_parser("langs", help="列出已注册语言与状态")

    p_fix = sub.add_parser("fix", help="自动修复多维表格（默认只预览，加 --apply 写表）")
    p_fix.add_argument("--apply", action="store_true", help="真正写表（缺省只预览）")
    p_fix.add_argument("--raw", default=None, help="base_raw.json 路径，缺省 output/base_raw.json")

    p_doc = sub.add_parser("doctor", help="体检 config 表坐标与线上 Base 是否一致")
    p_doc.add_argument("--fix", action="store_true", help="按表名自动重解析失效的表 id")

    args = parser.parse_args()
    if not args.cmd:
        parser.print_help()
        return 0
    try:
        if args.cmd == "platform":
            return cmd_platform()
        if args.cmd == "read":
            return cmd_read(as_json=args.json, from_raw=args.from_raw)
        if args.cmd == "query":
            return cmd_query(args.keyword, as_json=args.json)
        if args.cmd == "show":
            return cmd_show(args.kind, args.name)
        if args.cmd == "pull":
            return cmd_pull(args.out, args.raw, args.from_raw, args.model)
        if args.cmd == "gen":
            return cmd_gen(args.path, args.lang, args.fresh)
        if args.cmd == "langs":
            return cmd_langs()
        if args.cmd == "fix":
            return cmd_fix(dry_run=not args.apply, raw_path=args.raw)
        if args.cmd == "doctor":
            return cmd_doctor(fix=args.fix)
    except ValueError as e:
        print("配置错误:", e)
        return 2
    except Exception as e:
        print("执行失败:", e)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
