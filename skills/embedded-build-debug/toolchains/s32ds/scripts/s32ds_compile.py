#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S32DS compile checker for the CDC_7255 project (NXP S32K312, ARM GCC).

Parses the Eclipse .cproject managed-build configuration and compiles every
C source with the exact flags S32DS would use -- no GUI, no workspace.

Commands:
    check [options]     build per config/build_mode.conf:
                          compile -> compile all sources (parallel), no link
                          full    -> full build via Debug_FLASH/makefile
                              (.elf/.map/.hex + objcopy .bin)
    full [options]      explicit full build (same as check with mode=full)
    quick <file.c>      compile a single file with the same flag set
    parse [options]     print the resolved command line (gcc/-I/-D/flags)
    clean               remove the output directory

Mode priority: --mode compile|full > config/build_mode.conf > default compile.
Compile-check mode is -c only, objects land in <skill>/output/obj; full mode
runs the S32DS-generated makefile in Debug_FLASH (incremental) and never
touches <skill>/output except for the build log.

Paths (S32DS install, toolchain, SDK) are auto-detected; override them by
copying config/sdk_paths.conf.example to config/sdk_paths.conf.
"""

import argparse
import glob
import json
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

# The Windows console is usually GBK; compiler output may carry un-mappable
# bytes (e.g. DLP-ciphertext noise). Never let printing crash the report.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent              # <repo>/.claude/skills/embedded-build-debug/toolchains/s32ds


def _find_repo_root(start):
    """向上找工程根: 优先 .cproject / *.mex, 再退到 .git。
    不能只找 .git: .claude/ 下可能是独立 git 仓库, 会误停。"""
    for p in (start, *start.parents):
        if (p / '.cproject').exists() or list(p.glob('*.mex')):
            return p
    for p in (start, *start.parents):
        if (p / '.git').exists():
            return p
    return start.parents[5]


REPO_ROOT = _find_repo_root(SCRIPT_DIR)
OUTPUT_DIR = SKILL_DIR / "output"
OBJ_DIR = OUTPUT_DIR / "obj"
CPROJECT = REPO_ROOT / ".cproject"
# DLP note: .cproject is encrypted even for whitelisted readers (python/Read),
# unlike repo .c/.h. Workaround: `git show :.cproject > <plaintext copy>` (git
# reads blobs as plaintext) and point S32DS_CPROJECT at the copy. Default
# behavior is unchanged when the env var is unset.
import os as _os
if _os.environ.get("S32DS_CPROJECT"):
    CPROJECT = Path(_os.environ["S32DS_CPROJECT"])
PROJECT_FILE = REPO_ROOT / ".project"

# ---------------------------------------------------------------------------
# .cproject option mapping (superClass -> gcc flag). Verified against this
# project's .cproject; `parse` reports anything unmapped.
# ---------------------------------------------------------------------------
BOOL_FLAGS = {
    "gnu.c.compiler.option.warnings.pedantic": "-pedantic",
    "gnu.c.compiler.option.warnings.extrawarn": "-Wextra",
    "com.freescale.s32ds.cross.gnu.tool.c.compiler.option.warnings.unused": "-Wunused",
    "com.freescale.s32ds.cross.gnu.tool.c.compiler.option.optimization.unsignedbitfields": "-funsigned-bitfields",
    "com.freescale.s32ds.cross.gnu.tool.c.compiler.option.optimization.nocommon": "-fno-common",
    "com.freescale.s32ds.cross.gnu.tool.c.compiler.option.optimization.functionsections": "-ffunction-sections",
    "com.freescale.s32ds.cross.gnu.tool.c.compiler.option.optimization.datasections": "-fdata-sections",
}
ENUM_SUPERCLASSES = {
    "gnu.c.compiler.option.optimization.level",
    "com.nxp.s32ds.cle.arm.mbs.arm32.bare.gnu.9.2.tool.c.compiler.option.dialect.std",
    "com.nxp.s32ds.cle.arm.mbs.arm32.bare.tool.c.compiler.option.target.mcpu",
    "com.nxp.s32ds.cle.arm.mbs.arm32.bare.tool.c.compiler.option.target.instructionset",
    "com.nxp.s32ds.cle.arm.mbs.arm32.bare.tool.c.compiler.option.target.fpu.abi",
    "com.nxp.s32ds.cle.arm.mbs.arm32.bare.tool.c.compiler.option.target.fpu.unit",
}
STRING_FLAGS = {
    "gnu.c.compiler.option.optimization.flags",
    "com.freescale.s32ds.cross.gnu.tool.c.compiler.option.warnings.other",
    "gnu.c.compiler.option.misc.other",
}
# gnu.c.optimization.level.<x> -> -O<x>
OPT_LEVEL = {"none": "0", "quick": "1", "most": "2", "full": "3", "size": "s"}
# options belonging to other tools (cpp/linker/assembler/...) -- not our business
IGNORED_PREFIXES = (
    "gnu.cpp.", "gnu.both.asm.", "gnu.c.link.", "gnu.cpp.link.",
    "com.nxp.s32ds.cle.arm.mbs.arm32.bare.tool.cpp.compiler",
    "com.nxp.s32ds.cle.arm.mbs.arm32.bare.tool.c.linker",
    "com.nxp.s32ds.cle.arm.mbs.arm32.bare.tool.cpp.linker",
    "com.nxp.s32ds.cle.arm.mbs.arm32.bare.tool.archiver",
    "com.nxp.s32ds.cle.arm.mbs.arm32.bare.tool.assembler",
    "com.nxp.s32ds.cle.arm.mbs.arm32.bare.tool.createflash",
    "com.nxp.s32ds.cle.arm.mbs.arm32.bare.tool.createlisting",
    "com.nxp.s32ds.cle.arm.mbs.arm32.bare.tool.printsize",
    "com.freescale.s32ds.cross.gnu.c.preprocessor",
    "com.freescale.s32ds.cross.gnu.cpp.preprocessor",
    "com.freescale.s32ds.cross.gnu.disassembler",
)
IGNORED = {
    "gnu.c.compiler.option.debugging.level", "gnu.c.compiler.option.debugging.other",
    "gnu.c.compiler.option.debugging.format",
    "com.nxp.s32ds.cle.arm.mbs.arm32.bare.tool.c.compiler.option.target.libraries",
    "com.nxp.s32ds.cle.arm.mbs.arm32.bare.tool.c.compiler.option.target.sysroot",
    "com.nxp.s32ds.cle.arm.mbs.arm32.bare.tool.c.compiler.option.target.endianness",
    "com.freescale.s32ds.cross.gnu.tool.c.compiler.option.optimization.functionsections",
    "com.freescale.s32ds.cross.gnu.tool.c.compiler.option.optimization.datasections",
}
# NOTE: gnu.c.compiler.option.include.paths / preprocessor.def.symbols are NOT
# in IGNORED on purpose -- build_flag_context extracts them BEFORE the IGNORED
# check; adding them here would silently drop every -I and -D.

# resolved SDK dirs (globals set in main(), used by resolve_eclipse_vars)
BASE_SDK = None
PLATFORM_SDK = None


def die(msg):
    print(f"[s32ds] ERROR: {msg}", file=sys.stderr)
    sys.exit(2)


# ---------------------------------------------------------------------------
# Path auto-detection (config/sdk_paths.conf overrides)
# ---------------------------------------------------------------------------
def load_config():
    conf = {}
    path = SKILL_DIR / "config" / "sdk_paths.conf"
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                conf[k.strip()] = v.strip()
    return conf


def load_build_mode():
    """config/build_mode.conf -> 'compile' | 'full' (default compile)."""
    path = SKILL_DIR / "config" / "build_mode.conf"
    mode = "compile"
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            if k.strip() == "mode":
                mode = v.strip()
    if mode not in ("compile", "full"):
        die(f"config/build_mode.conf: invalid mode '{mode}' (expected compile|full)")
    return mode


def find_s32ds_root(conf):
    if conf.get("S32DS_ROOT"):
        p = Path(conf["S32DS_ROOT"])
        if p.is_dir():
            return p
        die(f"config S32DS_ROOT does not exist: {p}")
    for p in sorted(glob.glob("C:/NXP/S32DS.*"), reverse=True):
        if Path(p, "S32DS", "build_tools").is_dir():
            return Path(p)
    die("S32DS install not found (globbed C:/NXP/S32DS.*). "
        "Copy config/sdk_paths.conf.example to config/sdk_paths.conf and set S32DS_ROOT.")


def find_toolchain(s32ds_root, conf):
    if conf.get("TOOLCHAIN_BIN"):
        gcc = Path(conf["TOOLCHAIN_BIN"], "arm-none-eabi-gcc.exe")
        if gcc.is_file():
            return gcc
        die(f"config TOOLCHAIN_BIN has no arm-none-eabi-gcc.exe: {conf['TOOLCHAIN_BIN']}")
    hint = None                       # toolchain version from .cproject id (gnu.10.2)
    m = re.search(r"gnu\.(\d+\.\d+)", CPROJECT.read_text(encoding="utf-8", errors="replace"))
    if m:
        hint = m.group(1)
    tools = Path(s32ds_root, "S32DS", "build_tools")
    cands = sorted(tools.glob(f"gcc_v{hint}")) if hint else []
    if not cands:
        cands = sorted(tools.glob("gcc_v*"), reverse=True)
    for base in cands:
        for gcc in base.glob("gcc-*/bin/arm-none-eabi-gcc.exe"):
            return gcc
    die(f"ARM GCC toolchain not found under {tools}")


def find_sdk_dirs(s32ds_root, conf):
    rtd = Path(s32ds_root, "S32DS", "software", "PlatformSDK_S32K3", "RTD")
    base = platform_sdk = None
    if conf.get("SDK_BASENXP") and Path(conf["SDK_BASENXP"]).is_dir():
        base = Path(conf["SDK_BASENXP"])
    if conf.get("SDK_PLATFORM") and Path(conf["SDK_PLATFORM"]).is_dir():
        platform_sdk = Path(conf["SDK_PLATFORM"])
    if base is None:
        for mcal in sorted(rtd.glob("BaseNXP_*/include/Mcal.h")):
            base = mcal.parents[1]
            break
    if platform_sdk is None:
        for h in sorted(rtd.glob("Platform_*/startup/include/system.h")):
            platform_sdk = h.parents[2]
            break
    if base is None or platform_sdk is None:
        die(f"PlatformSDK_S32K3 RTD dirs not found under {rtd}. "
            "Set SDK_BASENXP/SDK_PLATFORM in config/sdk_paths.conf.")
    return base, platform_sdk


def find_make(s32ds_root):
    """S32DS ships GNU make inside build_tools/msys32."""
    for mk in sorted((Path(s32ds_root, "S32DS", "build_tools") / "msys32" / "usr" / "bin").glob("make.exe")):
        return mk
    die(f"make.exe not found under {s32ds_root}/S32DS/build_tools/msys32/usr/bin "
        "(full mode needs it to drive Debug_FLASH/makefile)")


# ---------------------------------------------------------------------------
# .cproject parsing
# ---------------------------------------------------------------------------
def read_project_name():
    try:
        return ET.parse(PROJECT_FILE).getroot().findtext("name", "").strip()
    except Exception:
        return ""


def pick_configuration(config_name):
    tree = ET.parse(CPROJECT)
    names, cfg = [], None
    for c in tree.getroot().iter("configuration"):
        n = c.get("name", "")
        names.append(n)
        if n == config_name:
            cfg = c
    if cfg is None:
        die(f"configuration '{config_name}' not found in .cproject. Available: {', '.join(names)}")
    return cfg, names


def build_flag_context(cfg):
    """Extract (include_paths, defines, flags, unmapped) from one configuration."""
    includes, defines, flags, unmapped = [], [], [], []
    for opt in cfg.iter("option"):
        sup = opt.get("superClass") or ""
        val = opt.get("value")
        if sup.startswith(IGNORED_PREFIXES) or sup in IGNORED:
            continue
        if sup.startswith("gnu.c.compiler.option.include.paths"):
            for lv in opt.findall("listOptionValue"):
                if lv.get("value"):
                    includes.append(lv.get("value"))
            continue
        if sup.startswith("gnu.c.compiler.option.preprocessor.def.symbols"):
            for lv in opt.findall("listOptionValue"):
                if lv.get("value"):
                    defines.append(lv.get("value"))
            continue
        if sup in BOOL_FLAGS:
            if val == "true":
                flags.append(BOOL_FLAGS[sup])
            continue
        if sup in ENUM_SUPERCLASSES and val:
            last = val.rsplit(".", 1)[-1]      # "gnu.c.optimization.level.size" -> "size"
            if sup.endswith("optimization.level"):
                flags.append("-O" + OPT_LEVEL.get(last, last))
            elif sup.endswith("instructionset"):
                flags.append("-m" + last)                    # thumb -> -mthumb
            elif sup.endswith("dialect.std"):
                flags.append("-std=" + last)                 # c99 -> -std=c99
            elif sup.endswith("target.mcpu"):
                flags.append("-mcpu=" + last)                # cortex-m7
            elif sup.endswith("fpu.abi"):
                flags.append("-mfloat-abi=" + last)          # hard
            elif sup.endswith("fpu.unit"):
                flags.append("-mfpu=" + last)                # fpv5-sp-d16
            continue
        if sup in STRING_FLAGS and val:
            flags.extend(val.split())
            continue
        if val not in (None, "", "false") and not list(opt):
            unmapped.append(f"{sup} = {val}")
    return includes, defines, flags, unmapped


def resolve_eclipse_vars(paths):
    """Resolve Eclipse variables against the repo root / SDK dirs."""
    out = []
    for p in paths:
        # &quot; is XML-decoded to a literal " by ElementTree; drop both forms.
        p = p.strip().strip('"').replace("&quot;", "").strip()
        if not p:
            continue
        p = p.replace("${ProjDirPath}", str(REPO_ROOT))
        # ${workspace_loc:/${ProjName}/<rest>} or ${workspace_loc:/${ProjName>}
        # -> repo_root/<rest>  (the project root IS the repo root).
        # Note the nested ${ProjName} must be matched literally -- a loose
        # [^/}]+ eats up to the first '}', leaving a stray '}' behind.
        p = re.sub(r"\$\{workspace_loc:/\$\{ProjName\}/?([^}]*)\}",
                   lambda m: str(REPO_ROOT / m.group(1)), p)
        p = p.replace("${BASE_PLATFORMSDK_S32K3}", str(BASE_SDK))
        p = p.replace("${PLATFORM_PLATFORMSDK_S32K3}", str(PLATFORM_SDK))
        if "${" in p:          # unresolved: keep as-is, gcc ignores missing dirs
            print(f"[s32ds] WARN: unresolved Eclipse variable kept: {p}")
        if not re.match(r"^[A-Za-z]:[/\\]", p):     # relative -> against repo root
            p = str((REPO_ROOT / p).resolve())
        out.append(p.replace("\\", "/"))
    seen, res = set(), []      # dedupe, keep order
    for p in out:
        if p not in seen:
            seen.add(p)
            res.append(p)
    return res


def discover_sources(cfg):
    """All .c files under sourceEntries, honoring 'excluding' patterns."""
    files = []
    for entry in cfg.iter("entry"):
        if entry.get("kind") != "sourcePath":
            continue
        base = REPO_ROOT / entry.get("name", "")
        if not base.is_dir():
            continue
        pats = [p.strip() for p in (entry.get("excluding") or "").split("|") if p.strip()]
        for c in base.rglob("*.c"):
            rel = c.relative_to(base).as_posix()
            if any(rel == pat or rel.startswith(pat + "/") for pat in pats):
                continue
            files.append(c)
    return sorted(set(files))      # dedupe (overlapping entries) + sort


# ---------------------------------------------------------------------------
# Compile
# ---------------------------------------------------------------------------
def compile_one(gcc, flags, includes, defines, src):
    rel = src.relative_to(REPO_ROOT).as_posix()
    stem = rel[:-2].replace("/", "_")
    obj = OBJ_DIR / f"{stem}.o"
    errfile = OBJ_DIR / f"{stem}.err"
    cmd = [str(gcc)] + flags
    cmd += [f"-I{p}" for p in includes]
    cmd += [f"-D{d}" for d in defines]
    cmd += [str(src), "-o", str(obj)]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=300)
        stderr, rc = (r.stderr or ""), r.returncode
    except subprocess.TimeoutExpired:
        stderr, rc = "compile timeout (300s)", 1
    errfile.write_text(stderr, encoding="utf-8", errors="replace")
    nwarn = len(re.findall(r"warning:", stderr))
    # DLP transparent encryption: gcc (not whitelisted) reads project files as
    # '%TSD-Header' ciphertext. Detect it so we can say so instead of dumping
    # hundreds of 'stray '\NNN'' errors.
    dlp = "%TSD-Header" in stderr[:4096]
    return {"file": rel, "rc": rc, "warnings": nwarn, "stderr": stderr, "dlp": dlp}


DLP_BANNER = (
    "DLP TRANSPARENT ENCRYPTION BLOCKS gcc: project files are read as\n"
    "'%TSD-Header' ciphertext by non-whitelisted processes (gcc/bash).\n"
    "  - whitelist arm-none-eabi-gcc.exe in the DLP client, or\n"
    "  - exclude the repo path from DLP monitoring,\n"
    "then rerun. Python/Read/Edit/IDE read the files fine; only gcc is blocked.")


def cmd_check(args, ctx):
    files = ctx["sources"]
    print(f"config   : {args.config}")
    print(f"gcc      : {ctx['gcc']}")
    print(f"sources  : {len(files)} .c files (compile-only, -j{args.jobs})")
    OBJ_DIR.mkdir(parents=True, exist_ok=True)
    for f in OBJ_DIR.glob("*.err"):
        f.unlink()

    results = []
    with ThreadPoolExecutor(max_workers=args.jobs) as ex:
        futs = [ex.submit(compile_one, ctx["gcc"], ctx["flags"], ctx["includes"],
                          ctx["defines"], s) for s in files]
        for done, fut in enumerate(futs, 1):
            results.append(fut.result())
            if done % 20 == 0 or done == len(futs):
                print(f"  ... {done}/{len(futs)}")

    failed = [r for r in results if r["rc"] != 0]
    dlp_hits = [r for r in failed if r["dlp"]]
    if dlp_hits and len(dlp_hits) * 2 >= len(failed):
        print("=" * 60)
        print(DLP_BANNER)
        print(f"(example: {dlp_hits[0]['file']})")
        sys.exit(3)
    warn_files = [r for r in results if r["warnings"] > 0 and r["rc"] == 0]
    print("=" * 60)
    for r in failed:
        print(f"FAIL: {r['file']}")
        for line in [l for l in r["stderr"].splitlines() if "error:" in l][:8]:
            print(f"      {line}")
    print("=" * 60)
    print(f"TOTAL={len(results)}  FAIL={len(failed)}  WARN_FILES={len(warn_files)}")
    summary = {
        "config": args.config, "gcc": str(ctx["gcc"]), "total": len(results),
        "fail": len(failed), "warn_files": len(warn_files),
        "dlp": bool(dlp_hits),
        "failed": [{"file": r["file"],
                    "errors": [l for l in r["stderr"].splitlines() if "error:" in l]}
                   for r in failed],
        "warnings": {r["file"]: r["warnings"] for r in warn_files},
    }
    (OUTPUT_DIR / "summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"summary  : {OUTPUT_DIR / 'summary.json'}")
    print("ALL COMPILE OK" if not failed else "COMPILE FAILED")
    sys.exit(0 if not failed else 1)


def _make_dryrun_cmds(make, build_dir, jobs, env):
    """`make -n all` -> exact command list (make does the mtime/.d math).

    DLP note: gcc spawned BY make reads project files as ciphertext (the DLP
    whitelist follows the parent-process chain and make.exe is not on it),
    so we never let make execute anything -- we replay its printed commands
    from python, whose gcc children are whitelisted (proven by `quick`).
    """
    r = subprocess.run([str(make), "-C", str(build_dir), f"-j{jobs}", "-n", "all"],
                       capture_output=True, text=True,
                       encoding="utf-8", errors="replace", env=env, timeout=120)
    if r.returncode != 0:
        print((r.stdout or "") + (r.stderr or ""))
        die(f"make -n failed (rc={r.returncode}) -- cannot compute the build plan")
    cmds = []
    for ln in ((r.stdout or "") + (r.stderr or "")).splitlines():
        s = ln.rstrip()
        if not s or s.startswith("make:") or s.startswith("echo "):
            continue
        if s.startswith("make ["):          # parallel job banner
            continue
        cmds.append(s)
    return cmds


def cmd_full(args, ctx):
    """Full build: let `make -n` compute the exact incremental plan from the
    S32DS-generated makefile, then replay each command from python (DLP-safe:
    gcc children of python read plaintext) and finish with a .bin objcopy."""
    build_dir = REPO_ROOT / args.config
    makefile = build_dir / "makefile"
    if not makefile.is_file():
        die(f"{makefile} not found -- open the project in S32DS and build once "
            "so the generated makefile/*.args exist, then retry full mode")
    project = read_project_name() or "firmware"
    elf = build_dir / f"{project}.elf"

    make = find_make(ctx["s32ds_root"])
    gcc_bin = ctx["gcc"].parent
    msys_bin = make.parent
    env = dict(_os.environ)
    env["PATH"] = f"{gcc_bin};{msys_bin};" + env.get("PATH", "")

    cmds = _make_dryrun_cmds(make, build_dir, args.jobs, env)
    print(f"config   : {args.config}")
    print(f"make     : {make} (dry-run plan only; commands replayed from python)")
    print(f"gcc      : {ctx['gcc']}")
    print(f"plan     : {len(cmds)} commands (incremental, serial)")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    log_lines, failed = [], None
    for i, cmd in enumerate(cmds, 1):
        r = subprocess.run(cmd, shell=True, cwd=str(build_dir), env=env,
                           capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=1800)
        log_lines.append(f"$ {cmd}\n{r.stdout or ''}{r.stderr or ''}")
        tail = (r.stderr or r.stdout or "").strip().splitlines()
        for ln in tail[-6:]:
            print(f"  {ln}")
        print(f"  [{i}/{len(cmds)}] rc={r.returncode}")
        if r.returncode != 0:
            failed = cmd
            break
    out_text = "\n".join(log_lines)
    (OUTPUT_DIR / "build_full.log").write_text(out_text, encoding="utf-8", errors="replace")

    if "%TSD-Header" in out_text:
        print("=" * 60)
        print(DLP_BANNER)
        sys.exit(3)
    if failed is not None:
        print("=" * 60)
        print(f"BUILD FAILED at: {failed}")
        print(f"full log: {OUTPUT_DIR / 'build_full.log'}")
        sys.exit(1)
    if not elf.is_file():
        die(f"make plan produced no {elf} (check makefile targets)")

    # makefile has no .bin rule -- add a raw binary pass (objcopy is next to gcc).
    binfile = build_dir / f"{project}.bin"
    objcopy = gcc_bin / "arm-none-eabi-objcopy.exe"
    size = gcc_bin / "arm-none-eabi-size.exe"
    rb = subprocess.run([str(objcopy), "-O", "binary", str(elf), str(binfile)],
                        capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)
    if rb.returncode != 0:
        print(f"[s32ds] ERROR: objcopy failed: {rb.stderr}")
        sys.exit(1)
    rs = subprocess.run([str(size), "--format=berkeley", str(elf)],
                        capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)
    print("=" * 60)
    if rs.returncode == 0 and rs.stdout.strip():
        print(rs.stdout.strip())
    import datetime
    for name in (f"{project}.elf", f"{project}.map", f"{project}.hex", f"{project}.bin"):
        p = build_dir / name
        if p.is_file():
            st = p.stat()
            print(f"  {name:<16} {st.st_size:>12,} bytes  "
                  f"{datetime.datetime.fromtimestamp(st.st_mtime):%Y-%m-%d %H:%M:%S}")
        else:
            print(f"  {name:<16} MISSING")
    print(f"log      : {OUTPUT_DIR / 'build_full.log'}")
    print("BUILD OK")
    sys.exit(0)


def cmd_quick(args, ctx):
    src = Path(args.file)
    if not src.is_absolute():
        src = REPO_ROOT / src
    if not src.is_file():
        die(f"file not found: {src}")
    OBJ_DIR.mkdir(parents=True, exist_ok=True)
    r = compile_one(ctx["gcc"], ctx["flags"], ctx["includes"], ctx["defines"], src)
    if r["dlp"]:
        print(DLP_BANNER)
        sys.exit(3)
    if r["rc"] == 0:
        print(f"OK: {r['file']}  (warnings: {r['warnings']})")
        sys.exit(0)
    print(f"FAIL: {r['file']}")
    print(r["stderr"])
    sys.exit(1)


def cmd_parse(args, ctx):
    print(f"config   : {args.config}")
    print(f"repo     : {REPO_ROOT}")
    print(f"gcc      : {ctx['gcc']}")
    print(f"flags    : {' '.join(ctx['flags'])}")
    print(f"defines  : {' '.join('-D' + d for d in ctx['defines'])}")
    print("includes :")
    for p in ctx["includes"]:
        print(f"  {'[ok] ' if Path(p).is_dir() else '[MISS]'} {p}")
    print(f"sources  : {len(ctx['sources'])} .c files")
    for s in ctx["sources"]:
        print(f"  {s.relative_to(REPO_ROOT).as_posix()}")
    if ctx["unmapped"]:
        print("unmapped .cproject options (verify manually):")
        for u in ctx["unmapped"]:
            print(f"  {u}")
    else:
        print("unmapped .cproject options: none")


def cmd_clean(_args, _ctx):
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
        print("cleaned:", OUTPUT_DIR)
    else:
        print("nothing to clean")


COMMANDS = {"check": cmd_check, "full": cmd_full, "quick": cmd_quick,
            "parse": cmd_parse, "clean": cmd_clean}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=sorted(COMMANDS))
    ap.add_argument("file", nargs="?", help="source file for 'quick'")
    ap.add_argument("--config", default="Debug_FLASH",
                    help=".cproject configuration name (default: Debug_FLASH)")
    ap.add_argument("-j", "--jobs", type=int, default=8, help="parallel jobs (default 8)")
    ap.add_argument("--mode", choices=["compile", "full"], default=None,
                    help="override config/build_mode.conf for 'check' "
                         "(compile = -c only, full = elf/map/hex/bin)")
    args = ap.parse_args()
    if args.command == "quick" and not args.file:
        die("quick requires a source file argument")

    conf = load_config()
    s32ds_root = find_s32ds_root(conf)
    gcc = find_toolchain(s32ds_root, conf)
    global BASE_SDK, PLATFORM_SDK
    BASE_SDK, PLATFORM_SDK = find_sdk_dirs(s32ds_root, conf)

    # mode resolution: --mode > config/build_mode.conf > compile
    mode = args.mode or load_build_mode()
    if args.command == "check" and mode == "full":
        args.command = "full"

    cfg, _names = pick_configuration(args.config)
    includes_raw, defines, flags, unmapped = build_flag_context(cfg)
    includes = resolve_eclipse_vars(includes_raw)
    sources = discover_sources(cfg)

    ctx = {"gcc": gcc, "flags": flags, "includes": includes, "s32ds_root": s32ds_root,
           "defines": defines, "sources": sources, "unmapped": unmapped}
    COMMANDS[args.command](args, ctx)


if __name__ == "__main__":
    main()
