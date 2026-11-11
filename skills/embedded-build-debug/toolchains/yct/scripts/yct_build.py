#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""YCT(GCC + CMake + Ninja) 工具链后端 —— 云途 YTM32 系列 MCU 工程

面向 YCT 配置工具生成的 CMake 工程(如 yadea 八寸 yadea0801_app / YTM32B1MD2)。
首次使用无需手动 init: build 时自动探测本机环境, 缺什么报什么并给安装指引。

环境四件套来源(云途官网 www.ytmicro.com 下载 YCT 配置工具, 安装弹窗选"是"+终端输三次 y 一键部署, 全部自带并写 PATH):
  - CMake >= 3.16        (%APPDATA%/yt_config_tool/cmake-*/bin/)
  - arm-none-eabi-gcc    (%APPDATA%/yt_config_tool/gcc-arm-none-eabi-*/)
  - Ninja                (%APPDATA%/yt_config_tool/ninja-win/)
  - YTM32 SDK            (%APPDATA%/yt_config_tool/sdk/YTM32B1xx_*)   —— YCT 内按芯片下载

用法:
  python yct_build.py init [--project DIR]                 探测环境并写 config.conf
  python yct_build.py build|check [--project DIR]          增量编译(缺缓存自动 configure)
  python yct_build.py rebuild [--project DIR]              清理后全量重编
  python yct_build.py full [--project DIR]                 强制重新 configure + 编译 + 产物清单
  python yct_build.py clean [--project DIR]                删除 build 目录
  python yct_build.py quick <file> [--project DIR]         单文件编译(基于 compile_commands.json)
"""
import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    if _s.encoding and _s.encoding.lower().replace('-', '') != 'utf8':
        try:
            _s.reconfigure(encoding='utf-8', errors='replace', line_buffering=True)
        except Exception:
            pass

BACKEND_DIR = Path(__file__).resolve().parent.parent
CONF_PATH = BACKEND_DIR / 'config' / 'config.conf'
YCT_HOME = Path(os.environ.get('APPDATA', '')) / 'yt_config_tool'
YCT_URL = 'https://www.ytmicro.com (工具链页 -> YCT 配置工具; 安装选"是"+输三次 y 一键部署 CMake/Ninja/GCC 并写 PATH, YCT 内下载芯片 SDK)'


def die(msg, hint=''):
    print(f"[yct][错误] {msg}")
    if hint:
        print(f"[yct][指引] {hint}")
    sys.exit(2)


def info(msg):
    print(f"[yct] {msg}")


def parse_conf(path):
    conf = {}
    if Path(path).exists():
        for line in Path(path).read_text(encoding='utf-8', errors='replace').splitlines():
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                conf[k.strip()] = v.strip().strip('"').strip("'")
    return conf


def which(prog):
    from shutil import which as _w
    return _w(prog)


def first_existing(*cands):
    """返回第一个真实存在的路径, 脏配置(文件已不在)自动跳过。"""
    for c in cands:
        if c and Path(c).exists():
            return str(c)
    return ''


def detect_project_chip(project):
    """从工程 CMakeLists.txt 提取芯片系列(如 YTM32B1MC0); 提取不到返回空串。"""
    if not project:
        return ''
    cmake = Path(project) / 'CMakeLists.txt'
    if not cmake.exists():
        return ''
    txt = cmake.read_text(encoding='utf-8', errors='replace')
    m = re.search(r'"(?:CPU_)?(YTM32B1[A-Z0-9]+)"', txt)
    return m.group(1) if m else ''


def detect_project_arm_cpu(project):
    """从工程 CMakeLists.txt 提取 -DARM_CPU=...(如 cortex-m33+nodsp); 提取不到返回空串。"""
    if not project:
        return ''
    cmake = Path(project) / 'CMakeLists.txt'
    if not cmake.exists():
        return ''
    txt = cmake.read_text(encoding='utf-8', errors='replace')
    m = re.search(r'-DARM_CPU=["\']?([a-zA-Z0-9_+\-]+)', txt)
    return m.group(1) if m else ''


def detect_env(conf, project):
    """探测四件套 + 工程; 返回 (env, missing[(key, 指引)])。探测到的路径即时可用。"""
    env, missing = {}, []

    cm = list(YCT_HOME.glob('cmake-*/bin/cmake.exe')) if YCT_HOME.is_dir() else []
    env['CMAKE'] = first_existing(conf.get('CMAKE'), which('cmake.exe') or which('cmake'),
                                  str(sorted(cm)[-1]) if cm else '',
                                  'C:/Program Files/CMake/bin/cmake.exe')
    if not env['CMAKE']:
        missing.append(('CMAKE', f'安装 YCT 并在安装弹窗选"是"+终端输三次 y(一键部署 CMake/Ninja/GCC 并写 PATH): {YCT_URL}'))

    g = list(YCT_HOME.glob('gcc-arm-none-eabi-*/bin/arm-none-eabi-gcc.exe')) if YCT_HOME.is_dir() else []
    gcc_dir = first_existing(conf.get('GCC_DIR'), str(sorted(g)[-1].parent) if g else '')
    if not gcc_dir:
        w = which('arm-none-eabi-gcc.exe')
        gcc_dir = str(Path(w).parent) if w else ''
    if not gcc_dir or not (Path(gcc_dir) / 'arm-none-eabi-gcc.exe').exists():
        missing.append(('GCC_DIR', f'安装 YCT: {YCT_URL}; 或自装 arm-none-eabi-gcc 后把 bin 目录写入 GCC_DIR'))
    else:
        env['GCC_DIR'] = gcc_dir

    n = list(YCT_HOME.glob('ninja*/ninja.exe')) if YCT_HOME.is_dir() else []
    env['NINJA'] = first_existing(conf.get('NINJA'), str(sorted(n)[-1]) if n else '', which('ninja.exe'))
    if not env['NINJA']:
        missing.append(('NINJA', f'安装 YCT: {YCT_URL}; 或 github ninja-build/release 下载单文件'))

    chip = detect_project_chip(project)
    sdk_home = YCT_HOME / 'sdk'
    s = list(sdk_home.glob(f'{chip}*')) if (chip and sdk_home.is_dir()) else []
    env['SDK_DIR'] = first_existing(conf.get('SDK_DIR'), str(sorted(s)[-1]) if s else '')
    if not env['SDK_DIR']:
        chip_hint = f'{chip} ' if chip else '对应芯片 '
        missing.append(('SDK_DIR', f'安装 YCT 并在 YCT 中下载 {chip_hint}SDK: {YCT_URL}'))

    env['PROJECT_DIR'] = str(project) if project else conf.get('PROJECT_DIR', '')
    if not env['PROJECT_DIR'] or not (Path(env['PROJECT_DIR']) / 'CMakeLists.txt').exists():
        missing.append(('PROJECT_DIR', '用 --project 指定 YCT 工程根(含 CMakeLists.txt/project.yct), 或 init --project 后写入配置'))
    env['ARM_CPU'] = conf.get('ARM_CPU') or detect_project_arm_cpu(project) or 'cortex-m33'
    return env, missing


def load_env(project=None, require_project=True):
    """读 config.conf + 探测; 缺关键组件直接 die。"""
    conf = parse_conf(CONF_PATH)
    env, missing = detect_env(conf, Path(project).resolve() if project else None)
    warn = [m for m in missing if m[0] == 'SDK_DIR']   # SDK 可选: 工程常内嵌 platform, 不依赖外部 SDK_DIR
    fatal0 = [m for m in missing if m[0] != 'SDK_DIR']
    if require_project:
        fatal = fatal0
    else:
        fatal = [m for m in fatal0 if m[0] != 'PROJECT_DIR']
    for k, hint in warn:
        info(f"提示 {k} 未自动匹配(可选, 不阻断编译)")
        info(f"  -> {hint}")
    if fatal:
        for k, hint in fatal:
            info(f"缺失 {k}")
            info(f"  -> {hint}")
        die('环境不完整。先处理以上缺项, 再跑 init 写入 config.conf',
            f'工具统一来源: 云途官网 {YCT_URL}')
    return env


def make_run_env(env):
    """PATH 最前置 gcc/ninja 目录。

    GCC_DIR 必须在最前面: 链接/objcopy 环节有裸名调用(arm-none-eabi-size / objcopy),
    若 PATH 里存在其他 objcopy(如 D:/software/bin 的 x86 版)会先命中, 报 Invalid bfd target。
    CMAKE 目录不入 PATH: 其同级常混有宿主工具, 会遮蔽交叉工具链。
    """
    r = os.environ.copy()
    prefix = []
    if env.get('GCC_DIR'):
        prefix.append(env['GCC_DIR'])
    if env.get('NINJA'):
        prefix.append(str(Path(env['NINJA']).parent))
    if prefix:
        r['PATH'] = os.pathsep.join(prefix) + os.pathsep + r.get('PATH', '')
    return r


def run(cmd, renv, **kw):
    print(f"[run] {' '.join(str(c) for c in cmd)}")
    try:
        return subprocess.call([str(c) for c in cmd], env=renv, **kw)
    except FileNotFoundError:
        die(f"找不到可执行文件: {cmd[0]}")


# DLP 透明加密拦截特征: gcc 读到密文时首行报 '%' token / stray '##' / stray '\xxx'
_DLP_SIG = re.compile(r"stray '\\|expected identifier or '\(? *before '%' token")


def _ninja_cmdlines(env, renv, build_dir):
    """用 ninja 干跑(-n -v)枚举待执行命令, 不真正编译。"""
    dry = subprocess.run([env['NINJA'], '-C', str(build_dir), '-n', '-v'],
                         env=renv, capture_output=True, text=True, errors='replace')
    cmds = []
    for line in (dry.stdout or '').splitlines():
        m = re.match(r'^\[\d+/\d+\]\s+(.*)$', line)
        if m:
            cmds.append(m.group(1).strip())
    return cmds


def _run_without_ninja(env, renv, build_dir):
    """python 直驱模式: 逐条执行 ninja 列出的命令, 进程链中不出现 ninja.exe。

    背景: 本机 DLP 透明加密环境下, ninja.exe 一旦处于 python 子孙链中, gcc 读源文件
    会拿到密文(stray '\\xxx' 报错); 而 python 直接拉起 gcc/cmd 读到的是明文。
    """
    cmds = _ninja_cmdlines(env, renv, build_dir)
    if not cmds:
        info('无待执行任务')
        return 0
    info(f'待执行 {len(cmds)} 条命令(python 直驱, 不经 ninja)')
    for i, c in enumerate(cmds, 1):
        info(f'[{i}/{len(cmds)}] {c[:160]}{"..." if len(c) > 160 else ""}')
        rc = subprocess.call(c, shell=True, cwd=str(build_dir), env=renv)
        if rc != 0:
            info(f'第 {i} 条命令失败, rc={rc}')
            return rc
    return 0


def run_ninja(env, renv, build_dir):
    """执行 ninja; 命中 DLP 拦截时自动降级为 python 直驱。"""
    p = subprocess.run([env['NINJA'], '-C', str(build_dir)], env=renv,
                       capture_output=True, text=True, errors='replace')
    out = (p.stdout or '') + (p.stderr or '')
    print(out, end='')
    if p.returncode == 0:
        return 0
    if not _DLP_SIG.search(out):
        return p.returncode
    info('命中 DLP 透明加密拦截(ninja 在 python 子孙链中, gcc 读到密文), 改用 python 直驱')
    return _run_without_ninja(env, renv, build_dir)


def do_init(ns):
    conf = parse_conf(CONF_PATH)
    env, missing = detect_env(conf, Path(ns.project).resolve() if ns.project else None)
    optional = [m for m in missing if m[0] == 'SDK_DIR']   # SDK 可选: 工程常内嵌 platform, 不依赖外部 SDK_DIR
    required = [m for m in missing if m[0] != 'SDK_DIR']
    info('环境探测结果:')
    for k in ('CMAKE', 'GCC_DIR', 'NINJA', 'SDK_DIR', 'PROJECT_DIR', 'ARM_CPU'):
        if k in dict(required):
            mark = '缺失'
        elif k in dict(optional):
            mark = '可选'
        else:
            mark = 'OK '
        info(f"  [{mark}] {k} = {env.get(k, '')}")
    if required:
        info('缺项指引:')
        for k, hint in required:
            info(f"  {k}: {hint}")
    if optional:
        info('可选提示(不阻断编译):')
        for k, hint in optional:
            info(f"  {k}: {hint}")
    lines = ['# yct 工具链配置(init 自动生成, 可手改)',
             '# 工具来源: 云途官网 https://www.ytmicro.com -> YCT 配置工具(安装选"是"+三次 y 一键部署 cmake/gcc/ninja; YCT 内下载 SDK)']
    for k in ('CMAKE', 'GCC_DIR', 'NINJA', 'SDK_DIR', 'PROJECT_DIR', 'ARM_CPU'):
        if env.get(k):
            lines.append(f'{k}="{env[k]}"')
    CONF_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONF_PATH.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    info(f'已写入 {CONF_PATH}')
    return 0 if not required else 1


def configure(env, renv, fresh=False):
    proj = Path(env['PROJECT_DIR'])
    tc = proj / 'cmake' / 'gcc.cmake'
    if not tc.exists():
        die(f'工程缺少工具链文件 {tc}', '确认 --project 指向 YCT 生成的 CMake 工程根')
    if fresh and (proj / 'build').exists():
        import shutil
        shutil.rmtree(proj / 'build')
    # 显式钉死交叉工具: cmake 会从 PATH 猜 objcopy/size, 若命中了宿主同名工具
    # (如 D:/software/bin/objcopy.exe)会把绝对路径写进 build.ninja, 链接尾段报
    # "Invalid bfd target", 事后改 PATH 无法纠正, 必须在 configure 期指定。
    gcc_bin = Path(env['GCC_DIR'])
    tools = {}
    for var, name in (('CMAKE_OBJCOPY', 'arm-none-eabi-objcopy.exe'),
                      ('CMAKE_SIZE', 'arm-none-eabi-size.exe'),
                      ('CMAKE_AR', 'arm-none-eabi-gcc-ar.exe'),
                      ('CMAKE_RANLIB', 'arm-none-eabi-ranlib.exe'),
                      ('CMAKE_OBJDUMP', 'arm-none-eabi-objdump.exe')):
        p = gcc_bin / name
        if p.exists():
            tools[var] = str(p)
    return run([env['CMAKE'], '-S', str(proj), '-B', str(proj / 'build'), '-G', 'Ninja',
                f'-DCMAKE_TOOLCHAIN_FILE={tc}', f"-DARM_CPU={env['ARM_CPU']}",
                f"-DCMAKE_MAKE_PROGRAM={env['NINJA']}",
                *[f'-D{k}={v}' for k, v in tools.items()]], renv)


def report_artifacts(env):
    proj = Path(env['PROJECT_DIR'])
    found = []
    for pat in ('*.elf', '*.hex', '*.bin', '*.axf'):
        found += [f for f in (proj / 'build').glob(pat) if f.is_file()]
    if not found:
        return
    info('产物:')
    for f in sorted(found):
        info(f"  {f}  ({f.stat().st_size / 1024:.1f} KB)")


def do_build(env, renv, force_full=False):
    proj = Path(env['PROJECT_DIR'])
    if force_full or not (proj / 'build' / 'build.ninja').exists():
        rc = configure(env, renv, fresh=force_full)
        if rc != 0:
            return rc
    rc = run_ninja(env, renv, proj / 'build')
    if rc == 0:
        report_artifacts(env)
    return rc


def do_clean(env):
    import shutil
    proj = Path(env['PROJECT_DIR'])
    if (proj / 'build').exists():
        shutil.rmtree(proj / 'build')
        info(f'已删除 {proj / "build"}')
    else:
        info('build 目录不存在, 无需清理')
    return 0


def do_quick(env, renv, ns):
    cc = Path(env['PROJECT_DIR']) / 'build' / 'compile_commands.json'
    if not cc.exists():
        info('无 compile_commands.json, 先跑一次 build 生成')
        rc = do_build(env, renv)
        if rc != 0:
            return rc
    # 相对路径按工程根解析(如 app/main.c), 绝对路径原样
    given = Path(ns.file)
    if not given.is_absolute():
        given = Path(env['PROJECT_DIR']) / given
    target = str(given.resolve()).lower()
    for entry in json.loads(cc.read_text(encoding='utf-8', errors='replace')):
        if str(Path(entry['file']).resolve()).lower() == target:
            info(f"单文件编译: {entry['file']}")
            return subprocess.call(entry['command'], shell=True,
                                   cwd=str(Path(env['PROJECT_DIR']) / 'build'), env=renv)
    die(f'compile_commands.json 中找不到 {ns.file}')


def main():
    ap = argparse.ArgumentParser(prog='yct_build.py',
                                 description='YCT(GCC+CMake+Ninja) 工具链后端')
    ap.add_argument('command', choices=['init', 'build', 'check', 'rebuild', 'full', 'clean', 'quick'])
    ap.add_argument('file', nargs='?', help='[quick] 单文件路径')
    ap.add_argument('--project', default=None, help='YCT 工程根目录(默认取 config.conf 的 PROJECT_DIR)')
    ns = ap.parse_args()
    if ns.command == 'quick' and not ns.file:
        ap.error('quick 需要文件参数')

    if ns.command == 'init':
        return do_init(ns)

    env = load_env(project=ns.project, require_project=True)
    renv = make_run_env(env)

    if ns.command in ('build', 'check'):
        return do_build(env, renv)
    if ns.command == 'rebuild':
        return do_build(env, renv, force_full=True)
    if ns.command == 'full':
        rc = configure(env, renv, fresh=True)
        return rc if rc else do_build(env, renv)
    if ns.command == 'clean':
        return do_clean(env)
    if ns.command == 'quick':
        return do_quick(env, renv, ns)
    ap.error(f'未知命令 {ns.command}')


if __name__ == '__main__':
    sys.exit(main())
