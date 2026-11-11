# -*- coding: utf-8 -*-
"""proto-toolkit 唯一入口（全部能力都是命令行传参，无 AI 逐项问答/无 HTML 表单）。

    python cli.py sync [--dry-run]                 ① 校验并修正协议表（链接 relink + 服务块合并）
    python cli.py parse [--lang c|java|all|none]    ③ 解析三表 → protocol.json，并按 --lang 生成代码
    python cli.py gen [--lang ...]                  ③ 只生成代码（不重解析）
    python cli.py langs                             列出已注册语言与状态
    python cli.py edit add-interface ...            ② 加接口（参数直接传，默认直写表）
    python cli.py edit add-struct ...               ② 加 struct
    python cli.py edit add-enum ...                 ② 加枚举
    python cli.py edit mod-interface ...            ② 改接口
    python cli.py edit delete-interface ...         ② 级联删接口（含对端/专属 struct/枚举）
    python cli.py edit apply <json> [--dry-run]     ② 批量落表（默认直写，--dry-run 才只出计划）
    python cli.py query <关键词> [--json]            ④ 查协议：三表关联闭包
    python cli.py console [--port 8765]             ④ 起本地控制台（utils/protocol_console.html）
    python cli.py rule                              打印「AI修订规则」子表
"""
import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if __package__ in (None, ""):
    sys.path.insert(0, os.path.dirname(_HERE))
    from scripts.common import conf, feishu
    from scripts.parse import parse_protocol, read_rule_sheet
    from scripts.gen import available as gen_available, generate as gen_generate
    from scripts.edit import apply_request
    from scripts.edit import request_builder as rb
    from scripts import rules, query
else:
    from .common import conf, feishu
    from .parse import parse_protocol, read_rule_sheet
    from .gen import available as gen_available, generate as gen_generate
    from .edit import apply_request
    from .edit import request_builder as rb
    from . import rules, query

EDIT_RUNBOOK = """\
════════════════════════════════════════════════════════════════
 能力② 修改协议 · 参数化用法（不做任何 AI 问答，全部传参）
════════════════════════════════════════════════════════════════
A. 加接口
   cli.py edit add-interface --service PowerMgr --direction "SOC→MCU" \\
       --name 接口名 --desc 描述 --if-type "method(rr)" --tx-type event \\
       --msg-id 0x0109 --pair-id 0x8109 --transport uart --qos level1 \\
       --param name=mode,type=enum:某枚举,io=IN,desc=模式
   （--param 可重复；struct 参数写 type=struct:StructName）
B. 加 struct
   cli.py edit add-struct --name Struct名 --service PowerMgr --namespace power \\
       --desc 描述 --member byte=0-1B,bit=,name=成员,type=uint16,desc=描述
C. 加枚举
   cli.py edit add-enum --name 枚举名 --msg-id 0x0109 \\
       --value value=0x00,c_name=C常量,desc=描述
D. 改接口
   cli.py edit mod-interface --name 接口名 --set K=0x0802 [--set F=新描述]
   （可改列 F 描述 G 类型 H 发送类型 J 消息id K 关联id L 传输层 M QoS N~Q 参数）
E. 删接口（级联）
   cli.py edit delete-interface --name 接口名
   会连带删：对端接口、只被这批接口引用的 struct（DS 整块）与枚举（PE 整块）。
F. 统一收尾
   以上命令默认直接写表；只想看计划加 --dry-run。
   写完会自动复跑 sync（链接重算 + 服务块 A~D 合并重算）+ parse，无需手动补跑。
   批量/复杂请求（描述含逗号）用 JSON：cli.py edit apply my.json [--dry-run]
════════════════════════════════════════════════════════════════\
"""


def _emit_report(rep, ctx, no_report=False):
    """检查结果 HTML：有 ERR/WARN 才生成；无则不生成并清掉旧报告。"""
    if no_report:
        return None
    from scripts import report
    path = report.emit(rep, ctx)
    if path:
        print("\n检查报告（%d 错误 / %d 告警）→ %s"
              % (rep.count("ERR"), rep.count("WARN"), path))
    else:
        print("\n无错误与告警，未生成检查报告")
    return path


def cmd_sync(dry=False, materialize=False, emit_fix=None, freeze_rules=False,
             no_report=False):
    "① 校验并修正：按 scripts/rules 注册表逐条跑（语义 + 分节 + 链接 + 样式 + 合并 + 规则对账）。"
    if freeze_rules:
        n = rules.freeze()
        print("规则快照已刷新：%d 条 → config/rule_snapshot.json" % n)
    total, fixed, ctx = rules.run_sync(dry=dry, materialize=materialize)
    for msg in fixed:
        print("  → 已修 %s" % msg)
    code = total.dump()
    _emit_report(total, ctx, no_report)
    if emit_fix:
        path, n = rules.emit_fix(ctx, emit_fix)
        print("\n可自动修的改动已导出 → %s（%d 个 op，用 cli.py edit apply 执行）" % (path, n))
    proto = ctx.proto
    print("protocol: %d 服务 / %d 接口 / %d struct / %d 枚举  (revision=%s)"
          % (proto.counts()["services"], proto.counts()["interfaces"],
             proto.counts()["structs"], proto.counts()["enums"], proto.source["revision"]))
    return code


def _run_gen(langs, proto=None):
    result = gen_generate(langs=langs, proto=proto)
    if not result:
        print("未生成任何语言（--lang none）：仅输出 protocol.json")
        return 0
    for lang, paths in result.items():
        for p in paths:
            print("生成[%s] → %s" % (lang, p))
    return 0


def cmd_parse(lang=None):
    proto = parse_protocol()
    path = proto.save()
    c = proto.counts()
    print("解析完成 → %s" % path)
    print("  服务 %d / 接口 %d / struct %d / 枚举 %d / revision %s"
          % (c["services"], c["interfaces"], c["structs"], c["enums"], proto.source["revision"]))
    return _run_gen(lang, proto=proto)


def cmd_langs():
    print("可用语言（--lang 取值）：")
    for name, label, status in gen_available():
        print("  %-6s %-6s %s" % (name, status, label))
    return 0


def cmd_rule():
    rows = read_rule_sheet()
    for i, line in enumerate(rows, 1):
        texts = [feishu.cell_text(c) for c in line]
        if any(texts):
            print("%3d | %s" % (i, " | ".join(t for t in texts if t)))
    return 0


def _edit_parser():
    p = argparse.ArgumentParser(prog="cli.py edit", add_help=True)
    sub = p.add_subparsers(dest="sub")
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--dry-run", action="store_true",
                        help="只打印计划不写表（默认直接写表）")
    common.add_argument("--force", action="store_true", help="预检有 ERR 也强写")

    ai = sub.add_parser("add-interface", help="加接口", parents=[common])
    ai.add_argument("--service", required=True)
    ai.add_argument("--direction", default="SOC→MCU")
    ai.add_argument("--name", required=True)
    ai.add_argument("--desc", default="")
    ai.add_argument("--if-type", default="event")
    ai.add_argument("--tx-type", default="event")
    ai.add_argument("--msg-id", required=True)
    ai.add_argument("--pair-id", default="")
    ai.add_argument("--transport", default="uart")
    ai.add_argument("--qos", default="level1")
    ai.add_argument("--param", action="append", metavar="name=..,type=..")

    st = sub.add_parser("add-struct", help="加 struct", parents=[common])
    st.add_argument("--name", required=True)
    st.add_argument("--service", default="")
    st.add_argument("--namespace", default="")
    st.add_argument("--desc", default="")
    st.add_argument("--member", action="append", metavar="byte=..,name=..,type=..")

    en = sub.add_parser("add-enum", help="加枚举", parents=[common])
    en.add_argument("--name", required=True)
    en.add_argument("--msg-id", required=True)
    en.add_argument("--value", action="append", metavar="value=..,c_name=..")

    ev = sub.add_parser("add-enum-value", help="给已有枚举追加取值", parents=[common])
    ev.add_argument("--name", required=True)
    ev.add_argument("--msg-id", default="")
    ev.add_argument("--value", required=True, metavar="value=..,c_name=..")

    edv = sub.add_parser("delete-enum-value", help="删除已有枚举取值", parents=[common])
    edv.add_argument("--name", required=True)
    edv.add_argument("--c-name", required=True)

    md = sub.add_parser("mod-interface", help="改接口", parents=[common])
    md.add_argument("--name", required=True)
    md.add_argument("--set", action="append", metavar="列=值")

    rm = sub.add_parser("delete-interface", help="级联删接口", parents=[common])
    rm.add_argument("--name", required=True)

    ap = sub.add_parser("apply", help="批量落表", parents=[common])
    ap.add_argument("json")
    return p


_BUILDERS = {
    "add-interface": rb.add_interface,
    "add-struct": rb.add_struct,
    "add-enum": rb.add_enum,
    "add-enum-value": rb.add_enum_value,
    "delete-enum-value": rb.delete_enum_value,
    "mod-interface": rb.mod_interface,
    "delete-interface": rb.delete_interface,
}


def cmd_edit(argv):
    if not argv:
        print(EDIT_RUNBOOK)
        return 0
    args = _edit_parser().parse_args(argv)
    execute = not getattr(args, "dry_run", False)
    if args.sub == "apply":
        return apply_request(args.json, execute=execute, force=args.force)
    builder = _BUILDERS.get(args.sub)
    if builder is None:
        print(EDIT_RUNBOOK)
        return 0
    ops = [builder(args)]
    path = rb.save_request(ops, getattr(args, "out", None))
    print("已生成请求 → %s" % path)
    return apply_request(path, execute=execute, force=getattr(args, "force", False))


def cmd_query(argv):
    """④ 查协议：关键词 → 三表关联闭包。--json 落 output/query_result.json。"""
    if not argv:
        return _usage("cli.py query <关键词> [--json]")
    kw = next((a for a in argv if not a.startswith("-")), "")
    if not kw:
        return _usage("cli.py query <关键词> [--json]")
    result = query.search(kw)
    print(query.render_text(result))
    if "--json" in argv:
        print("\n已落盘 → %s" % query.dump(result))
    return 0


def cmd_console(argv):
    """④ 起本地控制台：托管 utils/protocol_console.html + JSON API。"""
    from scripts import console_server
    return console_server.serve(port=int(_opt(argv, "--port") or 8765))


def _opt(argv, name, default=None):
    if name in argv:
        i = argv.index(name)
        return argv[i + 1] if i + 1 < len(argv) else default
    for a in argv:
        if a.startswith(name + "="):
            return a.split("=", 1)[1]
    return default


def _usage(text):
    print("用法: " + text)
    return 2


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    cmd = args[0]

    if cmd == "sync":
        return cmd_sync(dry="--dry-run" in args or "--dry" in args,
                        materialize="--materialize" in args,
                        emit_fix=_opt(args, "--emit-fix"),
                        freeze_rules="--freeze-rules" in args,
                        no_report="--no-report" in args)
    if cmd == "edit":
        return cmd_edit(args[1:])
    if cmd == "query":
        return cmd_query(args[1:])
    if cmd == "console":
        return cmd_console(args[1:])
    if cmd == "parse":
        return cmd_parse(lang=_opt(args, "--lang"))
    if cmd == "gen":
        lang = _opt(args, "--lang") or next((a for a in args[1:] if not a.startswith("-")), None)
        return _run_gen(lang)
    if cmd == "langs":
        return cmd_langs()
    if cmd == "rule":
        return cmd_rule()
    print("未知命令: %s\n%s" % (cmd, __doc__))
    return 2


if __name__ == "__main__":
    sys.exit(main())
