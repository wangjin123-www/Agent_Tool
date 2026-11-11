#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""嵌入式编译/烧录/调试统一入口 —— embedded-build-debug

两个正交维度，两级路由：
  编译域 toolchains/   选工具链: keil(UV4) | s32ds(GCC) | yct(YTM32 GCC+CMake+Ninja)  -> 产物 .axf/.elf/.hex/.bin
  烧录域 probes/       选探针:   jlink(J-Link) | pemicro(Multilink)
两步之间的唯一接口是固件产物文件(hex/bin/elf)，探针层不关心是谁编译的。

维度选择:
  --toolchain auto|keil|s32ds|yct   编译域(默认 auto: 按工程文件识别)
  --probe     auto|jlink|pemicro    烧录域(默认 auto: keil/yct工程->jlink, s32ds工程->pemicro)
  --project  PATH                   [yct] 目标工程根(缺省取 yct config.conf 的 PROJECT_DIR)
  --platform  keil|s32ds            旧参数, 等价 --toolchain 并采用默认探针配对

用法:
  python mcu_build_debug.py [--toolchain ...] [--probe ...] <command> [args...]

编译域命令(路由到 toolchains/):
  build/check/rebuild   编译(增量/检查/全量)
  full                  [s32ds] 链接出 .elf/.map/.hex/.bin
  quick <file>          [s32ds] 单文件编译
  parse/clean           解析/清理
  flash_check/diff/report  [keil] map占用/构建对比/HTML报告

烧录域命令(路由到 probes/):
  download [file]       下载固件(jlink: Slot A 模式可 --file 覆盖; pemicro: 需文件参数)
  full_download         [jlink] 擦除->下载->运行
  erase/verify/reset    Flash 操作
  jlink --command <op>  [jlink] halt/regs/read_mem/bp...
  dump_cortex           [jlink] HardFault 现场导出

跨域命令(统一入口编排):
  build_and_download    编译 -> 下载(+校验)
  debug                 交互调试指引
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    if _s.encoding and _s.encoding.lower().replace('-', '') != 'utf8':
        try:
            _s.reconfigure(encoding='utf-8', errors='replace', line_buffering=True)
        except Exception:
            pass

SKILL_ROOT = Path(__file__).resolve().parent.parent
TOOLCHAIN_DIR = SKILL_ROOT / 'toolchains'
PROBE_DIR = SKILL_ROOT / 'probes'

# 编译域: 命令 -> (keil 后端命令, s32ds 后端命令, yct 后端命令); None = 该工具链不支持
BUILD_MAP = {
    'build':        ('build', 'check', 'build'),
    'check':        ('build', 'check', 'build'),
    'rebuild':      ('rebuild', 'rebuild', 'rebuild'),   # s32ds rebuild 由入口组合 clean+full
    'full':         (None, 'full', 'full'),
    'quick':        (None, 'quick', 'quick'),
    'parse':        ('parse', 'parse', None),
    'clean':        (None, 'clean', 'clean'),
    'flash_check':  ('flash_check', None, None),
    'diff':         ('diff', None, None),
    'report':       ('report', None, None),
}
# 烧录域: 命令 -> (jlink 后端命令, pemicro 后端命令)
PROBE_MAP = {
    'download':      ('download', 'download'),
    'full_download': ('full_download', None),
    'erase':         ('erase', 'erase'),
    'verify':        ('verify', 'verify'),
    'reset':         ('reset', 'reset'),
    'jlink':         ('jlink', None),
    'probe':         ('jlink', 'probe'),       # 通用探针操作入口: probe halt/regs/read_mem/...
    'dump_cortex':   ('dump_cortex', 'dump_cortex'),
}
CROSS_CMDS = {'build_and_download', 'debug'}
ALL_COMMANDS = sorted(set(BUILD_MAP) | set(PROBE_MAP) | CROSS_CMDS)

# 默认探针配对(仅 auto 时): Keil/YCT 工程配 J-Link, S32DS 工程配 PEmicro
DEFAULT_PROBE = {'keil': 'jlink', 's32ds': 'pemicro', 'yct': 'jlink'}
TOOLCHAIN_IDX = {'keil': 0, 's32ds': 1, 'yct': 2}


def die(msg):
    print(f"[错误] {msg}")
    sys.exit(2)


def find_repo_root(start):
    """按工程文件定位仓库根。不能只找 .git: .claude/ 下可能是独立 git 仓库。"""
    for p in (start, *start.parents):
        if (p / '.cproject').exists() or (p / 'MDK').is_dir():
            return p
        if list(p.glob('*.mex')) or list(p.glob('*.uvprojx')):
            return p
    return Path.cwd()


def detect_toolchain(repo):
    if list(repo.glob('*.uvprojx')) or (repo / 'MDK').is_dir():
        return 'keil'
    if (repo / '.cproject').exists() or list(repo.glob('*.mex')):
        return 's32ds'
    if (repo / 'project.yct').exists() and (repo / 'CMakeLists.txt').exists():
        return 'yct'
    return None


def run(cmd):
    print(f"[run] {' '.join(str(x) for x in cmd)}")
    try:
        return subprocess.call([str(x) for x in cmd])
    except FileNotFoundError:
        die(f"找不到可执行文件: {cmd[0]}")


def find_bash():
    """定位可用的 bash: 优先 Git Bash, 跳过 System32 下的 WSL bash(常因 vhdx 挂载失败不可用)。"""
    cands = [r'C:\Program Files\Git\bin\bash.exe',
             r'C:\Program Files (x86)\Git\bin\bash.exe',
             r'D:\Program Files\Git\bin\bash.exe']
    for c in cands:
        if Path(c).exists():
            return c
    which = shutil.which('bash')
    if which and 'system32' not in which.lower():
        return which
    return 'bash'


def parse_bash_conf(path):
    """读 key=value 形式配置(工具链/探针 config.conf 共用此格式)。"""
    conf = {}
    if Path(path).exists():
        for line in Path(path).read_text(encoding='utf-8', errors='replace').splitlines():
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                conf[k.strip()] = v.strip().strip('"').strip("'")
    return conf


def latest_image(repo, toolchain):
    """跨域命令用: 找该工具链最新产物(elf 优先, 其次 hex)。"""
    if toolchain == 's32ds':
        dirs = [repo / 'Debug_FLASH', TOOLCHAIN_DIR / 's32ds' / 'output']
        for ext in ('*.elf', '*.hex'):
            files = []
            for d in dirs:
                if d.is_dir():
                    files += [f for f in d.rglob(ext) if f.is_file()]
            if files:
                return max(files, key=lambda f: f.stat().st_mtime)
        return None
    # keil: 从工具链配置读镜像路径(HEX 在探针配置, 但 keil 产物路径由工具链配置决定)
    conf = parse_bash_conf(TOOLCHAIN_DIR / 'keil' / 'config' / 'config.conf')
    if not conf:
        conf = parse_bash_conf(TOOLCHAIN_DIR / 'keil' / 'config' / 'config.conf.example')
    mdk = conf.get('MDK_DIR', 'MDK')
    sub = conf.get('OUTPUT_SUBDIR', 'output/debug')
    name = conf.get('TARGET_NAME', '')
    if name:
        for ext in ('.axf', '.hex', '.bin'):
            f = repo / mdk / sub / (name + ext)
            if f.is_file():
                return f
    return None


def run_build(toolchain, cmd, extra, project=None):
    if toolchain == 'keil':
        backend = BUILD_MAP[cmd][0]
        script = TOOLCHAIN_DIR / 'keil' / 'scripts' / 'keil_build.sh'
        return run([find_bash(), script, backend, *extra])
    if toolchain == 'yct':
        backend = BUILD_MAP[cmd][2]
        script = TOOLCHAIN_DIR / 'yct' / 'scripts' / 'yct_build.py'
        args = [sys.executable, script, backend]
        if project:
            args += ['--project', str(project)]
        return run([*args, *extra])
    backend = BUILD_MAP[cmd][1]
    script = TOOLCHAIN_DIR / 's32ds' / 'scripts' / 's32ds_compile.py'
    if cmd == 'rebuild':  # s32ds: clean + full
        rc = run([sys.executable, script, 'clean'])
        if rc != 0:
            return rc
        return run([sys.executable, script, 'check', '--mode', 'full', *extra])
    return run([sys.executable, script, backend, *extra])


def run_probe(probe, cmd, extra):
    if probe == 'jlink':
        backend = PROBE_MAP[cmd][0]
        script = PROBE_DIR / 'jlink' / 'scripts' / 'jlink_entry.sh'
        return run([find_bash(), script, backend, *extra])
    if cmd == 'probe':
        # pemicro: extra[0] 即子操作(halt/go/regs/read_mem/write_mem)，由 pemicro_ops argparse 校验
        if not extra:
            die("probe 需要子操作: halt|go|regs|read_mem|write_mem [--address ... --size|--value ...]")
        script = PROBE_DIR / 'pemicro' / 'scripts' / 'pemicro_ops.py'
        return run([sys.executable, script, *extra])
    backend = PROBE_MAP[cmd][1]
    script = PROBE_DIR / 'pemicro' / 'scripts' / 'pemicro_ops.py'
    return run([sys.executable, script, backend, *extra])


def main():
    ap = argparse.ArgumentParser(
        prog='mcu_build_debug.py',
        description='嵌入式编译/烧录/调试统一入口(编译域 toolchains + 烧录域 probes 两级路由)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__)
    ap.add_argument('--toolchain', choices=['auto', 'keil', 's32ds', 'yct'], default='auto',
                    help='编译域工具链(默认 auto 按工程识别)')
    ap.add_argument('--probe', choices=['auto', 'jlink', 'pemicro'], default='auto',
                    help='烧录域探针(默认 auto: keil/yct工程->jlink, s32ds工程->pemicro)')
    ap.add_argument('--project', default=None,
                    help='[yct] 目标 YCT/CMake 工程根(缺省取 yct config.conf 的 PROJECT_DIR)')
    ap.add_argument('--platform', choices=['keil', 's32ds'], default=None,
                    help='[旧参数] 等价 --toolchain, 并采用默认探针配对')
    ap.add_argument('command', nargs='?', help='统一命令, 见下方列表')
    ap.add_argument('args', nargs=argparse.REMAINDER, help='透传给后端的参数')
    ns = ap.parse_args()

    if not ns.command:
        ap.print_help()
        return 0

    cmd = ns.command
    if cmd not in ALL_COMMANDS:
        die(f"未知命令 {cmd!r}。可用: {', '.join(ALL_COMMANDS)}")

    repo = Path(ns.project).resolve() if ns.project else find_repo_root(SKILL_ROOT)
    toolchain = ns.toolchain
    if ns.platform:
        if toolchain not in ('auto', ns.platform):
            die(f"--platform {ns.platform} 与 --toolchain {toolchain} 冲突")
        toolchain = ns.platform
    if toolchain == 'auto':
        toolchain = detect_toolchain(repo)
        if toolchain is None:
            die("无法自动识别工具链: 仓库内没有 *.uvprojx/MDK(keil)、.cproject/*.mex(s32ds)、"
                "project.yct+CMakeLists.txt(yct)。请用 --toolchain keil|s32ds|yct 指定。")
    probe = ns.probe
    if probe == 'auto':
        probe = DEFAULT_PROBE[toolchain]
    print(f"[toolchain] {toolchain}  [probe] {probe}  (repo: {repo})")

    extra = ns.args

    # ---- 跨域命令 ----
    if cmd == 'build_and_download':
        build_cmd = 'full' if toolchain == 's32ds' else 'build'
        rc = run_build(toolchain, build_cmd, [], project=ns.project)
        if rc != 0:
            return rc
        if probe == 'pemicro':
            image = latest_image(repo, toolchain)
            if image is None:
                die("找不到可烧录的产物(s32ds: Debug_FLASH/*.elf|hex)。先跑 full 构建。")
            return run_probe(probe, 'download', [str(image)])
        # jlink: 后端配置里有默认镜像, extra 可透传 --file 覆盖
        return run_probe(probe, 'download', extra)

    if cmd == 'debug':
        print(f"debug 是交互流程: 按 SKILL.md 的 debug 步骤(parse -> 选择问题类型 -> probe/dump_cortex)。")
        print("两探针均支持 CLI 基础调试: probe halt/regs/read_mem/write_mem + dump_cortex；")
        print("断点/单步级交互调试: jlink 用 bp 断点流, pemicro 用 S32DS GUI (*_PNE.launch)。")
        return 0

    # ---- 编译域 ----
    if cmd in BUILD_MAP:
        idx = TOOLCHAIN_IDX[toolchain]
        if BUILD_MAP[cmd][idx] is None:
            avail = ', '.join(k for k, v in BUILD_MAP.items() if v[idx])
            die(f"{toolchain} 不支持命令 {cmd!r}。该工具链可用: {avail}")
        return run_build(toolchain, cmd, extra, project=ns.project)

    # ---- 烧录域 ----
    idx = 0 if probe == 'jlink' else 1
    if PROBE_MAP[cmd][idx] is None:
        die(f"探针 {probe} 不支持命令 {cmd!r}。"
            f"可用: {', '.join(k for k, v in PROBE_MAP.items() if v[idx])}")
    if probe == 'pemicro' and cmd in ('download', 'verify') and not extra:
        image = latest_image(repo, toolchain)
        if image is not None:
            extra = [str(image)]
    return run_probe(probe, cmd, extra)


if __name__ == '__main__':
    sys.exit(main())
