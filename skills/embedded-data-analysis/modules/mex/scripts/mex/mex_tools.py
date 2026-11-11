#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NXP MCUXpresso Config Tools .mex 配置分析工具 —— embedded-data-analysis · mex 模块

.mex 是 NXP Config Tools(S32DS 内置)的工程配置文件, 本质是分层 XML:
  configuration/tools/{pins, clocks, periphs}/...
    pins    -> pins_profile/pin_labels(引脚标签) + functions_list(功能引脚路由)
    clocks  -> clock_configurations(时钟源/输出/分频设置)
    periphs -> functional_groups/instances(外设实例) + config_set(嵌套 struct/array/setting)

参考实现:
  - Zephyr hal_nxp mcux/scripts/pinctrl/shared/mex_utils.py (ElementTree + 命名空间,
    仅 mex_configuration_14, 只取 board/processor/pins 版本) —— 本工具自行实现且
    命名空间无关(14/15 通用), 覆盖 pins/clocks/periphs 全量配置。
  - wavenumber-eng/nxp_monkey (MIT) 面向 NXP 芯片数据(KEX API), 不解析工程 .mex,
    故未采用。

无第三方依赖: 只用 Python 标准库 xml.etree.ElementTree。

用法: python mex_tools.py <子命令> <mex> [选项]

子命令:
  info     <mex>                              总览: 芯片/封装/工具版本/配置对象计数/校验问题
  pins     <mex> [--match PAT]                引脚标签表(网络名 -> pin_signal/pin_num)
  routes   <mex> [--peripheral P] [--match PAT]
                                              功能引脚路由表(函数 -> 外设信号 -> 物理引脚)
  clocks   <mex> [--config NAME] [--match PAT]
                                              时钟配置: 默认概览, --config 打印全量源/输出/设置
  instances<mex> [--match PAT] [--enabled-only]
                                              外设实例清单(类型/模式/启用/备注)
  config   <mex> --instance NAME [--match PAT]
                                              展开某外设实例的完整 config_set(路径=值)
  settings <mex> --match PAT [--instance NAME] [--limit N]
                                              全局搜索外设设置(名称或值正则)
  files    <mex> [--tool NAME]                各工具生成的工程文件清单
  problems <mex> [--level N]                  Config Tools 依赖/校验项(problem_level)
  diff     <mexA> <mexB> [--top N]            两版 .mex 配置对比
  scan     [--dir DIR]                        扫描目录找 .mex(按修改时间倒序)
"""
import argparse
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

# Windows 管道下 stdout 可能是 cp936, 强制 UTF-8(与 mapfile/canlog 模块同款)
for _s in (sys.stdout, sys.stderr):
    if _s.encoding and _s.encoding.lower().replace('-', '') != 'utf8':
        try:
            _s.reconfigure(encoding='utf-8', errors='replace')
        except Exception:
            pass

MODULE_ROOT = Path(__file__).resolve().parent.parent.parent


# --------------------------------------------------------------------------
# XML 读取(命名空间无关, mex_configuration_14/15 通用)
# --------------------------------------------------------------------------
def lname(tag):
    """去掉 {namespace} 前缀, 只留本地标签名"""
    return tag.rsplit('}', 1)[-1] if '}' in tag else tag


def text_of(e):
    return (e.text or '').strip() if e is not None else ''


class Mex:
    def __init__(self, path):
        self.path = Path(path)
        if not self.path.is_file():
            die(f"文件不存在: {self.path}")
        try:
            self.tree = ET.parse(str(self.path))
        except ET.ParseError as e:
            die(f"不是合法 XML: {self.path}\n{e}")
        except OSError as e:
            die(f"无法读取: {self.path}\n{e}")
        self.root = self.tree.getroot()
        if lname(self.root.tag) != 'configuration':
            die(f"根元素不是 <configuration>, 可能不是 Config Tools .mex: {self.path}\n"
                f"实际根元素: {lname(self.root.tag)}")
        tag = self.root.tag
        self.namespace = tag[1:].split('}', 1)[0] if tag.startswith('{') else ''
        self.schema = self.namespace.rsplit('/', 1)[-1] if self.namespace else '(无命名空间)'
        self.uuid = self.root.get('uuid', '')
        self.version = self.root.get('version', '')
        tools_el = self._kid(self.root, 'tools')
        self.tools = {lname(c.tag): c for c in tools_el} if tools_el is not None else {}

    # ---- 元素导航 ----
    @staticmethod
    def _kids(e, name):
        if e is None:
            return []
        return [c for c in e if lname(c.tag) == name]

    def _kid(self, e, name):
        ks = self._kids(e, name)
        return ks[0] if ks else None

    def _path(self, e, path):
        cur = e
        for part in path.split('/'):
            cur = self._kid(cur, part)
            if cur is None:
                return None
        return cur

    def _paths(self, e, path):
        parts = path.split('/')
        cur = e
        for part in parts[:-1]:
            cur = self._kid(cur, part)
            if cur is None:
                return []
        return self._kids(cur, parts[-1])

    def tool(self, name):
        return self.tools.get(name)

    # ---- pins ----
    def pin_labels(self):
        out = []
        pp = self._kid(self.tool('pins'), 'pins_profile')
        for el in self._paths(pp, 'pin_labels/pin_label'):
            ident = el.get('identifier', '') or ''
            out.append({
                'pin_num': el.get('pin_num', ''),
                'pin_signal': el.get('pin_signal', ''),
                'label': el.get('label', ''),
                'identifier': ident,
                'identifiers': [x for x in ident.split(';') if x],
            })
        return out

    def routing(self):
        out = []
        fl = self.tool('pins')
        for fn in self._paths(fl, 'functions_list/function'):
            fname = fn.get('name', '')
            for pin in self._paths(fn, 'pins/pin'):
                feats = {}
                for pf in self._paths(pin, 'pin_features/pin_feature'):
                    feats[pf.get('name', '')] = pf.get('value', '')
                out.append({
                    'function': fname,
                    'peripheral': pin.get('peripheral', ''),
                    'signal': pin.get('signal', ''),
                    'pin_num': pin.get('pin_num', ''),
                    'pin_signal': pin.get('pin_signal', ''),
                    'features': feats,
                })
        return out

    # ---- clocks ----
    def clock_configs(self):
        out = []
        for cc in self._paths(self.tool('clocks'),
                              'clock_configurations/clock_configuration'):
            item = {
                'name': cc.get('name', ''),
                'description': text_of(self._kid(cc, 'description')),
                'sources': [{
                    'id': s.get('id', ''), 'value': s.get('value', ''),
                    'enabled': s.get('enabled', '')}
                    for s in self._paths(cc, 'clock_sources/clock_source')],
                'outputs': [{
                    'id': o.get('id', ''), 'value': o.get('value', '')}
                    for o in self._paths(cc, 'clock_outputs/clock_output')],
                'settings': [{
                    'id': s.get('id', ''), 'value': s.get('value', '')}
                    for s in self._paths(cc, 'clock_settings/setting')],
                'deps': self._deps(cc, f"Clocks:{cc.get('name', '')}"),
            }
            out.append(item)
        return out

    def _deps(self, e, default_source):
        out = []
        for d in self._paths(e, 'dependencies/dependency'):
            feats = {}
            for f in self._kids(d, 'feature'):
                vals = [text_of(x) for x in f.iter() if lname(x.tag) == 'data']
                feats[f.get('name', '')] = vals[0] if vals else ''
            out.append({
                'resourceType': d.get('resourceType', ''),
                'resourceId': d.get('resourceId', ''),
                'description': d.get('description', ''),
                'problem_level': d.get('problem_level', ''),
                'source': d.get('source', '') or default_source,
                'features': feats,
            })
        return out

    # ---- periphs ----
    def functional_groups(self):
        groups = []
        for g in self._paths(self.tool('periphs'),
                             'functional_groups/functional_group'):
            insts = []
            for i in self._paths(g, 'instances/instance'):
                insts.append({
                    'name': i.get('name', ''),
                    'type': i.get('type_id', ''),
                    'mode': i.get('mode', ''),
                    'enabled': i.get('enabled', ''),
                    'comment': i.get('comment', ''),
                    'config_set': self._kid(i, 'config_set'),
                })
            groups.append({
                'name': g.get('name', ''),
                'core': g.get('core', ''),
                'called_from_default_init': g.get('called_from_default_init', ''),
                'instances': insts,
            })
        return groups

    def instances(self):
        return [inst for g in self.functional_groups() for inst in g['instances']]

    def find_instance(self, name):
        exact = [i for i in self.instances() if i['name'] == name]
        if exact:
            return exact[0]
        low = name.lower()
        partial = [i for i in self.instances() if low in i['name'].lower()]
        return partial[0] if len(partial) == 1 else None

    # ---- files / problems ----
    def generated_files(self):
        out = []
        for tname, tool in self.tools.items():
            for f in self._paths(tool, 'generated_project_files/file'):
                out.append({
                    'tool': tname,
                    'path': f.get('path', ''),
                    'update_enabled': f.get('update_enabled', ''),
                })
        return out

    def dependencies(self):
        out = []
        for tname, tool in self.tools.items():
            if tname == 'clocks':
                continue  # 每个 clock_configuration 内单独收集, 带 config 名
            out.extend(self._deps(tool, tname))
        for c in self.clock_configs():
            out.extend(c['deps'])
        return out


def flatten_settings(e, prefix=''):
    """config_set 的 struct/array/setting 递归展开 -> [(路径, 值)]

    路径示例:
      Wkpu.IcuConfigSet.IcuChannel[0].IcuChannelId
      POWER.PowerConfigSet.PowerConfig[0].PowerMode
    """
    out = []
    if e is None:
        return out
    for c in e:
        tag = lname(c.tag)
        if tag == 'setting':
            key = c.get('name') or c.get('id') or '?'
            out.append((f"{prefix}.{key}".lstrip('.'), c.get('value', '')))
        elif tag == 'struct':
            nm = c.get('name', '')
            if prefix and re.fullmatch(r'\d+', nm or ''):
                out.extend(flatten_settings(c, f"{prefix}[{nm}]"))
            else:
                newp = f"{prefix}.{nm}".lstrip('.') if nm else prefix
                out.extend(flatten_settings(c, newp))
        elif tag == 'array':
            nm = c.get('name', '')
            newp = f"{prefix}.{nm}".lstrip('.') if nm else prefix
            for gc in c:
                gtag = lname(gc.tag)
                if gtag == 'struct':
                    idx = gc.get('name', '')
                    if re.fullmatch(r'\d+', idx or ''):
                        out.extend(flatten_settings(gc, f"{newp}[{idx}]"))
                    else:
                        sub = f"{newp}.{idx}".lstrip('.') if idx else newp
                        out.extend(flatten_settings(gc, sub))
                elif gtag == 'setting':
                    key = gc.get('name') or gc.get('id') or '?'
                    out.append((f"{newp}.{key}" if newp else key,
                                gc.get('value', '')))
                elif gtag == 'array':
                    out.extend(flatten_settings(gc, newp))
    return out


# --------------------------------------------------------------------------
# 输出
# --------------------------------------------------------------------------
def dw(s):
    """终端显示宽度(CJK 按 2 计)"""
    return sum(2 if unicodedata.east_asian_width(ch) in 'WF' else 1 for ch in str(s))


def pad(s, width):
    s = str(s)
    return s + ' ' * max(0, width - dw(s))


def clip(s, n=70):
    s = str(s).replace('\n', ' ')
    return s if dw(s) <= n else s[:max(1, n - 1)] + '…'


def table(headers, rows, max_width=70):
    if not rows:
        print('(无匹配)')
        return
    cells = [[clip('' if v is None else v, max_width) for v in r] for r in rows]
    widths = [dw(h) for h in headers]
    for r in cells:
        for i, v in enumerate(r):
            widths[i] = max(widths[i], dw(v))
    print('  '.join(pad(h, widths[i]) for i, h in enumerate(headers)).rstrip())
    print('  '.join('-' * widths[i] for i in range(len(headers))))
    for r in cells:
        print('  '.join(pad(v, widths[i]) for i, v in enumerate(r)).rstrip())


def die(msg):
    print(f"[错误] {msg}")
    sys.exit(2)


def rx(pattern):
    try:
        return re.compile(pattern, re.I)
    except re.error as e:
        die(f"正则无效 {pattern!r}: {e}")


def matches(pat, *fields):
    return any(pat.search(str(f)) for f in fields)


# --------------------------------------------------------------------------
# 子命令
# --------------------------------------------------------------------------
def cmd_info(mex, _args):
    common = mex._kid(mex.root, 'common')
    core = mex._kid(common, 'cores')
    core_el = mex._kid(core, 'core')
    print(f"文件      : {mex.path.resolve()}")
    print(f"大小      : {mex.path.stat().st_size:,} B")
    print(f"处理器    : {text_of(mex._kid(common, 'processor'))}")
    print(f"封装      : {text_of(mex._kid(common, 'package'))}")
    print(f"芯片数据包: {text_of(mex._kid(common, 'mcu_data'))}")
    if core_el is not None:
        print(f"内核      : {core_el.get('id', '')} ({core_el.get('name', '')})")
    print(f"XML 模型  : {mex.schema}  (root version={mex.version}, uuid={mex.uuid})")
    desc = text_of(mex._kid(common, 'description'))
    if desc:
        print(f"描述      : {desc}")
    print()

    print('工具:')
    rows = []
    for tname, tool in mex.tools.items():
        nfiles = len(mex._paths(tool, 'generated_project_files/file'))
        rows.append((tname, tool.get('name', ''), tool.get('version', '') or '-',
                     tool.get('enabled', ''), nfiles))
    table(['key', '工具', '版本', '启用', '生成文件'], rows)
    print()

    labels = mex.pin_labels()
    routes = mex.routing()
    clocks = mex.clock_configs()
    insts = mex.instances()
    n_settings = sum(len(flatten_settings(i['config_set'], i['name'])) for i in insts)
    deps = mex.dependencies()
    levels = {}
    for d in deps:
        levels[d['problem_level']] = levels.get(d['problem_level'], 0) + 1
    print('配置对象:')
    print(f"  引脚标签      : {len(labels)} 条 / 唯一信号 {len({x['pin_signal'] for x in labels})} 个")
    print(f"  功能路由      : {len({r['function'] for r in routes})} 个函数 / {len(routes)} 条引脚")
    print(f"  时钟配置      : {len(clocks)} 个 ({', '.join(c['name'] for c in clocks) or '-'})")
    print(f"  外设实例      : {len(insts)} 个 (启用 {sum(1 for i in insts if i['enabled'] == 'true')})")
    print(f"  外设设置项    : {n_settings} 条 (config_set 展开)")
    print(f"  校验依赖      : {len(deps)} 条  " +
          ' '.join(f"level{k}={v}" for k, v in sorted(levels.items())))


def cmd_pins(mex, args):
    pat = rx(args.match) if args.match else None
    rows = []
    for p in mex.pin_labels():
        if pat and not matches(pat, p['pin_num'], p['pin_signal'], p['label'],
                               p['identifier']):
            continue
        rows.append((p['pin_num'], p['pin_signal'], p['label'], p['identifier']))
    table(['pin_num', 'pin_signal', 'label', 'identifier'], rows)


def cmd_routes(mex, args):
    pat = rx(args.match) if args.match else None
    per = rx(args.peripheral) if args.peripheral else None
    rows = []
    for r in mex.routing():
        if pat and not matches(pat, r['function'], r['peripheral'], r['signal'],
                               r['pin_signal']):
            continue
        if per and not per.search(r['peripheral']):
            continue
        f = r['features']
        rows.append((r['function'], r['peripheral'], r['signal'], r['pin_num'],
                     r['pin_signal'], f.get('direction', ''), f.get('identifier', '')))
    table(['function', 'peripheral', 'signal', 'pin_num', 'pin_signal',
           'direction', 'identifier'], rows)


def cmd_clocks(mex, args):
    pat = rx(args.match) if args.match else None
    for c in mex.clock_configs():
        if args.config and args.config.lower() not in c['name'].lower():
            continue
        print(f"=== {c['name']} ===")
        if c['description']:
            print(f"说明: {c['description']}")
        if not args.config:
            print(f"时钟源 {len(c['sources'])} / 输出 {len(c['outputs'])} / "
                  f"设置 {len(c['settings'])}")
            rows = []
            for s in c['sources']:
                if pat and not matches(pat, s['id'], s['value']):
                    continue
                rows.append((s['id'], s['value'], s['enabled']))
            if rows:
                print('时钟源:')
                table(['source', 'value', 'enabled'], rows)
            keys = ('CORE_CLK', 'AIPS_PLAT_CLK', 'AIPS_SLOW_CLK', 'CLKOUT_RUN_CLK',
                    'CLKOUT_STANDBY_CLK', 'FXOSC_CLK', 'SXOSC_CLK', 'PLL_PHI0_CLK')
            rows = []
            for o in c['outputs']:
                if pat and not matches(pat, o['id'], o['value']):
                    continue
                if not args.match and not any(k in o['id'] for k in keys):
                    continue
                rows.append((o['id'], o['value']))
            if rows:
                print('关键输出:' if not args.match else '输出:')
                table(['output', 'value'], rows)
            print()
            continue
        print('\n时钟源:')
        table(['source', 'value', 'enabled'],
              [(s['id'], s['value'], s['enabled']) for s in c['sources']
               if not pat or matches(pat, s['id'], s['value'])])
        print('\n时钟输出:')
        table(['output', 'value'],
              [(o['id'], o['value']) for o in c['outputs']
               if not pat or matches(pat, o['id'], o['value'])])
        print('\n时钟设置:')
        table(['setting', 'value'],
              [(s['id'], s['value']) for s in c['settings']
               if not pat or matches(pat, s['id'], s['value'])])
        if c['deps']:
            print(f"\n校验依赖: {len(c['deps'])} 条(problems 子命令看详情)")
        print()


def cmd_instances(mex, args):
    pat = rx(args.match) if args.match else None
    rows = []
    for g in mex.functional_groups():
        for i in g['instances']:
            if args.enabled_only and i['enabled'] != 'true':
                continue
            if pat and not matches(pat, g['name'], i['name'], i['type'], i['mode'],
                                   i['comment']):
                continue
            rows.append((g['name'], i['name'], i['type'], i['mode'],
                         i['enabled'], i['comment']))
    table(['group', 'instance', 'type', 'mode', 'enabled', 'comment'], rows)


def cmd_config(mex, args):
    inst = mex.find_instance(args.instance)
    if inst is None:
        names = ', '.join(i['name'] for i in mex.instances())
        die(f"找不到实例 {args.instance!r}。可用: {names}")
    pat = rx(args.match) if args.match else None
    settings = flatten_settings(inst['config_set'], inst['name'])
    print(f"实例: {inst['name']}  type={inst['type']}  mode={inst['mode']}  "
          f"enabled={inst['enabled']}")
    if inst['comment']:
        print(f"备注: {inst['comment']}")
    print(f"设置项: {len(settings)} 条\n")
    rows = [(p, v) for p, v in settings if not pat or matches(pat, p, v)]
    table(['setting path', 'value'], rows, max_width=100)


def cmd_settings(mex, args):
    pat = rx(args.match)
    rows = []
    for inst in mex.instances():
        if args.instance and args.instance.lower() not in inst['name'].lower():
            continue
        for p, v in flatten_settings(inst['config_set'], inst['name']):
            if matches(pat, p, v):
                rows.append((inst['name'], p, v))
    print(f"匹配 {len(rows)} 条(显示前 {min(len(rows), args.limit)} 条)")
    table(['instance', 'setting path', 'value'], rows[:args.limit], max_width=100)


def cmd_files(mex, args):
    tool = args.tool.lower() if args.tool else None
    rows = [(f['tool'], f['path'], f['update_enabled'])
            for f in mex.generated_files()
            if not tool or f['tool'].lower() == tool]
    print(f"生成文件 {len(rows)} 个:\n")
    table(['tool', 'path', 'update'], rows)


def cmd_problems(mex, args):
    deps = mex.dependencies()
    if args.level is not None:
        deps = [d for d in deps if d['problem_level'] == str(args.level)]
    deps.sort(key=lambda d: (d['problem_level'], d['source']))
    print(f"校验依赖 {len(deps)} 条:")
    rows = []
    for d in deps:
        feats = ', '.join(f"{k}={v}" for k, v in d['features'].items())
        rows.append((d['problem_level'], d['source'], d['resourceType'],
                     d['resourceId'], d['description'], feats))
    table(['level', 'source', 'resType', 'resourceId', 'description', 'features'],
          rows, max_width=60)


def _facts(mex):
    f = {}
    for p in mex.pin_labels():
        f[f"pin_label[{p['pin_signal']}]"] = f"{p['label']} | {p['identifier']}"
    for r in mex.routing():
        k = f"route[{r['function']}][{r['peripheral']}:{r['signal']}]"
        f[k] = f"{r['pin_signal']} pin{r['pin_num']}"
    for c in mex.clock_configs():
        pre = f"clock[{c['name']}]"
        for s in c['sources']:
            f[f"{pre}.source[{s['id']}]"] = s['value']
        for o in c['outputs']:
            f[f"{pre}.output[{o['id']}]"] = o['value']
        for s in c['settings']:
            f[f"{pre}.setting[{s['id']}]"] = s['value']
    for i in mex.instances():
        pre = f"periph[{i['name']}]"
        f[pre] = f"type={i['type']} mode={i['mode']} enabled={i['enabled']}"
        for p, v in flatten_settings(i['config_set'], i['name']):
            f[f"{pre}.{p}"] = v
    for g in mex.generated_files():
        f[f"file[{g['tool']}][{g['path']}]"] = g['update_enabled']
    return f


def cmd_diff(mex, args):
    other = Mex(args.mex_b)
    fa, fb = _facts(mex), _facts(other)
    added = [k for k in fb if k not in fa]
    removed = [k for k in fa if k not in fb]
    changed = [k for k in fb if k in fa and fa[k] != fb[k]]
    print(f"A: {mex.path.resolve()}")
    print(f"B: {other.path.resolve()}")
    print(f"新增 {len(added)} / 删除 {len(removed)} / 修改 {len(changed)}\n")
    if changed:
        print(f"--- 修改 (Top {args.top}) ---")
        for k in changed[:args.top]:
            print(k)
            print(f"  A: {fa[k]}")
            print(f"  B: {fb[k]}")
        print()
    if added:
        print(f"--- 新增 (Top {args.top}) ---")
        for k in added[:args.top]:
            print(f"+ {k} = {fb[k]}")
        print()
    if removed:
        print(f"--- 删除 (Top {args.top}) ---")
        for k in removed[:args.top]:
            print(f"- {k} = {fa[k]}")


def cmd_scan(_mex, args):
    root = Path(args.dir)
    if not root.is_dir():
        die(f"目录不存在: {root}")
    files = sorted(root.rglob('*.mex'), key=lambda p: p.stat().st_mtime, reverse=True)
    print(f"在 {root.resolve()} 下找到 {len(files)} 个 .mex:\n")
    rows = []
    for p in files:
        st = p.stat()
        rows.append((datetime.fromtimestamp(st.st_mtime).strftime('%Y-%m-%d %H:%M'),
                     f"{st.st_size:,}", str(p)))
    table(['修改时间', '大小(B)', 'path'], rows, max_width=100)


# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(
        prog='mex_tools.py',
        description='NXP MCUXpresso Config Tools .mex 配置分析(无第三方依赖)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__)
    sub = ap.add_subparsers(dest='cmd', required=True)

    def add(name, fn, help_):
        p = sub.add_parser(name, help=help_)
        if name != 'scan':
            p.add_argument('mex', help='.mex 文件路径')
        p.set_defaults(func=fn)
        return p

    add('info', cmd_info, '总览')
    p = add('pins', cmd_pins, '引脚标签表')
    p.add_argument('--match', help='正则过滤 pin_num/pin_signal/label/identifier')
    p = add('routes', cmd_routes, '功能引脚路由表')
    p.add_argument('--peripheral', help='正则过滤外设名')
    p.add_argument('--match', help='正则过滤 function/peripheral/signal/pin_signal')
    p = add('clocks', cmd_clocks, '时钟配置')
    p.add_argument('--config', help='只看某时钟配置(子串匹配), 并打印全量源/输出/设置')
    p.add_argument('--match', help='正则过滤 source/output/setting 的 id 或 value')
    p = add('instances', cmd_instances, '外设实例清单')
    p.add_argument('--match', help='正则过滤 group/instance/type/mode/comment')
    p.add_argument('--enabled-only', action='store_true', help='只看 enabled=true')
    p = add('config', cmd_config, '展开某外设实例的 config_set')
    p.add_argument('--instance', required=True, help='实例名(精确或唯一子串)')
    p.add_argument('--match', help='正则过滤设置路径或值')
    p = add('settings', cmd_settings, '全局搜索外设设置')
    p.add_argument('--match', required=True, help='正则过滤设置路径或值')
    p.add_argument('--instance', help='只搜某实例')
    p.add_argument('--limit', type=int, default=200, help='最多显示条数(默认 200)')
    p = add('files', cmd_files, '生成文件清单')
    p.add_argument('--tool', help='只看某工具(pins/clocks/periphs)')
    p = add('problems', cmd_problems, '校验依赖')
    p.add_argument('--level', type=int, help='只看某 problem_level')
    p = sub.add_parser('diff', help='两版 .mex 对比')
    p.add_argument('mex', help='基线 .mex')
    p.add_argument('mex_b', help='对比 .mex')
    p.add_argument('--top', type=int, default=50, help='每类最多显示条数(默认 50)')
    p.set_defaults(func=cmd_diff)
    p = sub.add_parser('scan', help='扫描目录找 .mex')
    p.add_argument('--dir', default='.', help='扫描目录(默认当前目录)')
    p.set_defaults(func=cmd_scan)

    args = ap.parse_args()
    if args.cmd == 'scan':
        args.func(None, args)
        return
    mex = Mex(args.mex)
    args.func(mex, args)


if __name__ == '__main__':
    main()
