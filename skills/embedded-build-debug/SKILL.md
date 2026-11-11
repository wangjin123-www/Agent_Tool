---
version: 2.0.0
author: wangjin0115
company: cviauto
name: embedded-build-debug
description: 嵌入式编译、烧录、调试统一工具（编译域 Keil MDK / NXP S32DS S32K3 / 云途 YCT YTM32 + 烧录域 J-Link / PEmicro 两级路由）。编译选工具链（--toolchain keil|s32ds|yct），烧录选探针（--probe jlink|pemicro），固件产物是两步之间唯一接口。当用户提到"编译"、"重编"、"烧录"、"下载"、"刷机"、"Flash"、"J-Link"、"JLink"、"PEmicro"、"Multilink"、"调试"、"HardFault"、"断言"、"MDK"、"Keil"、"UV4"、"fromelf"、"固件"、"完整流程"、"全流程"、"S32DS"、"S32K3"、"YCT"、"YTM32"、"云途"、"CMake"、"Ninja"、"yadea 八寸"、"编译检查"、"编译验证"、"语法检查"、"有没有编译错误"、"出固件"、"elf/hex/bin"、"parse"、"check"、"quick"、"clean"时触发。Keil 侧编译/摘要/占用/对比；S32DS 侧编译检查、单文件编译、完整构建出 elf/map/hex/bin；YCT 侧（GCC+CMake+Ninja，如 yadea 八寸 YTM32B1MD2）增量/全量编译、单文件编译、环境自动探测 init；J-Link 探针支持下载(Slot A)/擦除/校验/复位/寄存器内存操作/HardFault 导出；PEmicro 探针（Multilink+S32K312）支持 pegdbserver_console+gdb batch 无头下载/擦除/复位/校验。不适用于通用 C 调试或非上述工程。
argument-hint: "[--toolchain keil|s32ds|yct] [--probe jlink|pemicro] [--project <YCT工程根>] build|rebuild|check|full|quick <file>|parse|clean|download|full_download|build_and_download|erase|verify|reset|debug|flash_check|diff|jlink|probe <op>|dump_cortex|report"
allowed-tools: [Bash, Read, Edit, Grep, Glob, Write, AskUserQuestion]
tags:
   - embedded
   - build
   - flash
   - debug
   - keil
   - mdk
   - jlink
   - pemicro
   - s32ds
   - s32k3
   - arm
   - cortex-m
---

# embedded-build-debug — 编译域 × 烧录域 两级路由

**编译和烧录是两个正交维度**：编译选工具链（Keil/UV4、S32DS/GCC、YCT/GCC+CMake+Ninja），烧录选探针（J-Link、PEmicro），中间接口只有固件产物（hex/bin/elf）。上层只认统一命令；维度路由由本文件 + `scripts/mcu_build_debug.py` 完成。

## 第一步：确定两个维度（必做）

```bash
python "$SKILL_DIR/scripts/mcu_build_debug.py" [--toolchain auto|keil|s32ds|yct] [--probe auto|jlink|pemicro] [--project <YCT工程根>] <命令> [参数...]
```

| 维度 | 取值 | 识别依据 / 默认配对 | 后端目录 |
|---|---|---|---|
| 编译域 | `keil` | `*.uvprojx`、`MDK/` | `toolchains/keil/` |
| 编译域 | `s32ds` | `.cproject`、`*.mex`、`Debug_FLASH/` | `toolchains/s32ds/` |
| 编译域 | `yct` | `project.yct` + `CMakeLists.txt`（云途 YTM32，如 yadea 八寸） | `toolchains/yct/` |
| 烧录域 | `jlink` | keil/yct 工程默认；S32DS 固件也可用（需 J-Link 口） | `probes/jlink/` |
| 烧录域 | `pemicro` | s32ds 工程默认（Multilink，`*_PNE.launch`） | `probes/pemicro/` |

自动识别不唯一或识别不到时，必须显式传 `--toolchain` / `--probe`，禁止瞎选。旧参数 `--platform keil|s32ds` 仍兼容（等价 `--toolchain` + 默认探针配对）。

## 统一命令矩阵

| 统一命令 | Keil 工具链 | S32DS 工具链 | YCT 工具链 | J-Link 探针 | PEmicro 探针 |
|---|---|---|---|---|---|
| `build` / `check` | 增量编译 + bin + 摘要 | 编译检查（`build_mode.conf`） | 增量编译（自动 configure） | — | — |
| `rebuild` | 全量重编 | `clean` + `full` | 全量重编 | — | — |
| `full` | — | 链接出 `.elf/.map/.hex/.bin` | 重 configure + 编译 + 产物清单 | — | — |
| `quick <file>` | — | 单文件编译 | 单文件编译 | — | — |
| `parse` | 解析 `build.log` | 解析 `.cproject` | — | — | — |
| `clean` | — | 清理 `output/` | 删除工程 `build/` | — | — |
| `flash_check` / `diff` / `report` | map 占用/构建对比/HTML 报告 | — | — | — | — |
| `download [file]` | — | — | — | 下载（默认 Slot A 0x8000，`--file` 覆盖） | 烧录 elf/hex + 复位（缺省取最新产物） |
| `full_download` | — | — | — | 擦除 → 下载 → 运行 | — |
| `erase` / `verify` / `reset` | — | — | — | Flash 擦除/校验/复位 | 整片擦除/ELF 比对/复位 |
| `jlink --command <op>` | — | — | — | halt/regs/read_mem/bp… | — |
| `probe <op>` | — | — | — | 转发 jlink_cmd（halt/regs/read_mem/bp…） | halt/go/regs/read_mem/write_mem |
| `dump_cortex` | — | — | — | HardFault 现场导出 | HardFault 现场导出（同口径解析） |
| `build_and_download` | 编译→下载→校验（配 jlink） | `full`→烧录（配 pemicro） | 编译→下载（配 jlink，`--file` 指定 elf） | ✓ | ✓ |
| `debug` | 交互调试指引 | — | — | 流程内 + bp 断点流 | CLI 基础调试 + GUI 断点级 |

`—` = 该维度无此能力；脚本明确报错，不会静默跳过。

## S32DS + PEmicro 工作流（本仓库主路径）

```bash
# 1) 确认选项映射与 include 路径
python "$SKILL_DIR/scripts/mcu_build_debug.py" --toolchain s32ds parse
# 2) 日常编译检查
python "$SKILL_DIR/scripts/mcu_build_debug.py" --toolchain s32ds check
# 3) 出固件
python "$SKILL_DIR/scripts/mcu_build_debug.py" --toolchain s32ds full
# 4) 烧录（Multilink 无头: pegdbserver_console + gdb batch）
python "$SKILL_DIR/scripts/mcu_build_debug.py" --probe pemicro download Debug_FLASH/test_prj_Thumb.elf
# 或一条龙
python "$SKILL_DIR/scripts/mcu_build_debug.py" build_and_download
```

- 编译产物/日志：`toolchains/s32ds/output/`；烧录技术路径与坑位见 [probes/pemicro/README.md](probes/pemicro/README.md)。
- CLI 基础调试可用：`--probe pemicro probe regs|read_mem|halt`、`--probe pemicro dump_cortex`（HardFault 解析与 J-Link 同口径）。
- 断点/单步/变量监视级交互调试仍走 S32DS GUI（`Project_Settings/Debugger/*_PNE.launch`）。

## Keil + J-Link 工作流

```bash
python "$SKILL_DIR/scripts/mcu_build_debug.py" --toolchain keil build
python "$SKILL_DIR/scripts/mcu_build_debug.py" build_and_download
python "$SKILL_DIR/scripts/mcu_build_debug.py" --toolchain keil flash_check
```

- 首次运行自动生成 `toolchains/keil/config/config.conf` 并定位 UV4/fromelf；探针配置在 `probes/jlink/config/`（JLink.exe、DEVICE、默认镜像）。
- `download` 默认 **Slot A 模式**：从 0x8000 编程应用区，跳过 Flash 选项字节区（0x400-0x7FFF）。
- 详细流程见 [toolchains/keil/README.md](toolchains/keil/README.md)、[probes/jlink/README.md](probes/jlink/README.md)。

### Keil debug 流程

1. `--toolchain keil parse`
2. AskUserQuestion 让用户选问题类型：编译失败 / HardFault / 死循环 / 变量异常 / 流程错误 / 外设问题 / Flash 占用 / 编译对比。
3. 按类型执行：
   - HardFault → `... --probe jlink dump_cortex`
   - 死循环 → `... --probe jlink jlink --command halt`，再 `--command regs`
   - 变量/外设 → `... --probe jlink jlink --command read_mem --address <地址> --size <长度>`
   - 流程 → `... --probe jlink jlink --command bp --address <地址>`
   - Flash 占用 → `--toolchain keil flash_check`
   - 编译对比 → `--toolchain keil diff <旧log路径>`
4. 修复后重新编译/下载，询问"问题是否解决？"；是 → `... report` 结束，否 → 回到第 2 步。

## YCT + J-Link 工作流（云途 YTM32，如 yadea 八寸）

```bash
# 0) 新机器一次性环境体检 + 固化配置（自动探测，缺什么打什么指引）
python "$SKILL_DIR/toolchains/yct/scripts/yct_build.py" init --project <YCT工程根>
# 1) 日常增量编译（build.ninja 缺失时自动 cmake configure）
python "$SKILL_DIR/scripts/mcu_build_debug.py" --toolchain yct --project <YCT工程根> build
# 2) 烧录（产物在 <工程根>/build/*.elf，J-Link DEVICE 需为 YTM32B1MD2）
python "$SKILL_DIR/scripts/mcu_build_debug.py" --probe jlink download --file <工程根>/build/yadea0801_app.elf
```

- 环境只需一步：云途官网 https://www.ytmicro.com 装 **YCT 配置工具**，安装时终端弹窗一键部署 CMake/Ninja/GCC 并写 PATH，SDK 在 YCT 内按芯片下载；之后 `build` 零配置可用。
- 本后端不绑定 skill 所在仓库（工程路径走 `--project`），整个 skill 目录拷到其他仓库/机器即可复用。
- 详细说明见 [toolchains/yct/README.md](toolchains/yct/README.md)。

## 关键规则（两域共通）

| 规则 | 原因 |
|---|---|
| 统一入口优先：先跑 `mcu_build_debug.py`，不要直接调后端脚本 | 保持命令语义一致；后端脚本路径可随技能目录搬移 |
| 维度识别不了就显式 `--toolchain` / `--probe` | 避免把 Keil 工程按 S32DS 编译（反之亦然） |
| 探针层只吃产物文件（hex/bin/elf），不读工具链配置 | 编译域/烧录域可自由组合（如 S32DS 编译 + J-Link 烧录） |
| 编译失败先区分"代码错"与"生成物过期/依赖缺失" | `.mex` 改后未重新生成、`modules.h` 开关、RTD 版本基线都会伪装成语法错 |
| S32DS 告警 ≠ 失败 | 只有带 `error:` 的行计入失败；已知良性告警见 platform-notes |
| DLP 透明加密环境：编译/取证用 Python 链路 | bash/grep 可能读到密文；S32DS full 模式的回放机制就是为此设计 |
| Windows 控制台强制 UTF-8 | cp936 会炸中文日志 |

## 目录结构

```
embedded-build-debug/
├── SKILL.md                    # 本文件: 两级路由与工作流
├── README.md                   # 维度矩阵与快速上手
├── scripts/
│   └── mcu_build_debug.py      # 统一入口(维度识别 + 命令路由)
├── toolchains/                 # ① 编译域（选工具链）
│   ├── keil/                   # UV4 + fromelf → .axf/.bin
│   ├── s32ds/                  # GCC → .elf/.hex/.bin
│   └── yct/                    # 云途 YTM32: GCC+CMake+Ninja → .elf（工程路径解耦, --project）
└── probes/                     # ② 烧录/调试域（选探针）
    ├── jlink/                  # JLink Commander 脚本化(Slot A/擦除/HardFault)
    └── pemicro/                # pegdbserver_console + gdb batch(Multilink/S32K3)
```

## 迁移说明（v1 → v2）

- v1 的 `platforms/` 拆为 `toolchains/`（编译）+ `probes/`（烧录）：`--platform keil` 下原先捆绑的 download/erase/verify/reset/jlink/dump_cortex 全部移入 `probes/jlink`。
- 原命令全部兼容；`--platform keil|s32ds` 等价 `--toolchain` + 默认探针配对。
- 新增：PEmicro 无头烧录（原"S32DS 只能 GUI 烧录"的限制解除）、跨域组合（如 `--toolchain s32ds --probe jlink download --file <hex>`）。
- 原 `keil_debug.sh` 拆为 `toolchains/keil/scripts/keil_build.sh`（编译域）+ `probes/jlink/scripts/jlink_entry.sh`（烧录域）。
