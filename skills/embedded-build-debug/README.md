# embedded-build-debug

嵌入式 **编译 / 烧录 / 调试** 统一技能。编译与烧录是两个正交维度，两级路由：

| 维度 | 后端 | 工程识别 / 硬件 | 能力 |
|---|---|---|---|
| 编译域 | Keil MDK（`toolchains/keil`） | `*.uvprojx` / `MDK/` | 编译、bin 生成、结构化摘要、Flash 占用、构建对比、HTML 报告 |
| 编译域 | NXP S32DS（`toolchains/s32ds`） | `.cproject` / `*.mex` | 编译检查、单文件编译、完整构建出 `.elf/.map/.hex/.bin` |
| 烧录域 | J-Link（`probes/jlink`） | J-Link 探针 | 下载（Slot A）、擦除、校验、复位、寄存器/内存操作、HardFault 导出 |
| 烧录域 | PEmicro（`probes/pemicro`） | Multilink（`*_PNE.launch`） | 无头下载、整片擦除、复位、ELF 校验（pegdbserver_console + gdb batch） |

两步之间唯一接口是固件产物（hex/bin/elf）——**任何工具链 × 任何探针可自由组合**（如 S32DS 编译 + J-Link 烧录）。

## 快速上手

```bash
SKILL_DIR="$(git rev-parse --show-toplevel)/.claude/skills/embedded-build-debug"
python "$SKILL_DIR/scripts/mcu_build_debug.py" --help
```

维度会自动识别（keil 工程→jlink、s32ds 工程→pemicro 默认配对）；不确定时显式指定：

```bash
python "$SKILL_DIR/scripts/mcu_build_debug.py" --toolchain s32ds check
python "$SKILL_DIR/scripts/mcu_build_debug.py" --toolchain keil build
python "$SKILL_DIR/scripts/mcu_build_debug.py" --probe pemicro download Debug_FLASH/test_prj_Thumb.elf
python "$SKILL_DIR/scripts/mcu_build_debug.py" build_and_download      # 编译 → 烧录一条龙
```

## 命令矩阵

| 统一命令 | Keil | S32DS | J-Link | PEmicro |
|---|---|---|---|---|
| `build` / `check` | 增量编译 + bin | 编译检查 | — | — |
| `rebuild` / `full` / `quick` | 全量重编 | `clean+full` / 出固件 / 单文件 | — | — |
| `parse` / `clean` | 日志解析 | 选项解析 / 清理 | — | — |
| `flash_check` / `diff` / `report` | 占用/对比/报告 | — | — | — |
| `download` [file] | — | — | Slot A 下载 | 烧录 + 复位 |
| `full_download` | — | — | 擦除→下载→运行 | — |
| `erase` / `verify` / `reset` | — | — | Flash 操作 | 擦除/校验/复位 |
| `jlink` / `probe <op>` | — | — | 调试操作（halt/regs/read_mem/bp…） | halt/regs/read_mem/write_mem |
| `dump_cortex` | — | — | HardFault 导出 | HardFault 导出（同口径） |
| `build_and_download` | ✓(配 jlink) | ✓(配 pemicro) | ✓ | ✓ |
| `debug` | 交互调试流程 | — | 流程内 | 用 S32DS GUI |

## 目录

```
embedded-build-debug/
├── SKILL.md                 # 两级路由与工作流(技能入口)
├── README.md                # 本文件
├── scripts/mcu_build_debug.py
├── toolchains/              # ① 编译域
│   ├── keil/                # UV4 + fromelf
│   └── s32ds/               # S32DS GCC(含 platform-notes)
└── probes/                  # ② 烧录/调试域
    ├── jlink/               # JLink Commander 脚本化
    └── pemicro/             # pegdbserver_console + gdb batch(含调研笔记)
```

维度细节：

- Keil：[toolchains/keil/README.md](toolchains/keil/README.md)
- S32DS：[toolchains/s32ds/README.md](toolchains/s32ds/README.md)、[platform-notes.md](toolchains/s32ds/reference/platform-notes.md)
- J-Link：[probes/jlink/README.md](probes/jlink/README.md)
- PEmicro：[probes/pemicro/README.md](probes/pemicro/README.md)、[pemicro-notes.md](probes/pemicro/reference/pemicro-notes.md)

## 环境

- Windows（Git Bash / PowerShell 均可；脚本内部按 UTF-8 输出）
- Keil 侧：Keil MDK（UV4）、fromelf；J-Link 驱动（烧录/调试时）
- S32DS 侧：S32 Design Studio 3.x、ARM GCC 10.2；PEmicro 驱动（Multilink）
- 路径均自动探测，各有 config 可覆盖
- Python 3

## 迁移说明

v1（`platforms/` 捆绑"平台"）→ v2（`toolchains/` + `probes/` 两级正交）。原 `keil-debug`、`s32ds-compile` 技能及 v1 命令全部兼容；详细差异见 [SKILL.md](SKILL.md) 迁移说明。
