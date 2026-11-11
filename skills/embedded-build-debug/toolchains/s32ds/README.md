# S32DS 工具链（embedded-build-debug / toolchains/s32ds）

编译域的 NXP S32 Design Studio（S32K3）命令行实现。**统一入口在上层**：`scripts/mcu_build_debug.py --toolchain s32ds <命令>`；本目录不单独作为技能。烧录/调试走 `probes/pemicro`（默认配对）或 `probes/jlink`。

## 能力

| 工具链命令 | 本后端脚本 | 说明 |
|---|---|---|
| `build` / `check` | `s32ds_compile.py check` | 按 `config/build_mode.conf` 的 mode 执行 |
| `full` | `s32ds_compile.py full` | 完整构建，产出 `.elf/.map/.hex/.bin`（与 GUI 同路径） |
| `rebuild` | `clean` + `check --mode full` | 由统一入口组合 |
| `quick <file>` | `s32ds_compile.py quick` | 只编译单个文件 |
| `parse` | `s32ds_compile.py parse` | 从 `.cproject` 解析编译选项 |
| `clean` | `s32ds_compile.py clean` | 清理 `output/` |

烧录：`mcu_build_debug.py --probe pemicro download <elf>`（Multilink，无头）；或 `build_and_download` 一条龙。

## 快速开始

```bash
SKILL_DIR="$(git rev-parse --show-toplevel)/.claude/skills/embedded-build-debug"
python "$SKILL_DIR/scripts/mcu_build_debug.py" --toolchain s32ds parse
python "$SKILL_DIR/scripts/mcu_build_debug.py" --toolchain s32ds check
python "$SKILL_DIR/scripts/mcu_build_debug.py" --toolchain s32ds quick src/App/App_Power.c
python "$SKILL_DIR/scripts/mcu_build_debug.py" --toolchain s32ds full
python "$SKILL_DIR/scripts/mcu_build_debug.py" --probe pemicro download Debug_FLASH/test_prj_Thumb.elf
```

也可直接双击 `utils/build.bat` 交互选 1（编译检查）/ 2（完整构建）。

## 构建模式

`config/build_mode.conf`（本机生效，已 gitignore）：

```ini
mode = compile   # compile=仅编译检查 | full=完整构建出固件
```

`check --mode full` 可临时覆盖。

## 关键约束

- **full 模式绝不直接执行 `make`**：脚本用 `make -n` 取计划、Python 逐条回放命令。DLP 白名单按进程链放行，`make → gcc` 会读到密文（退出码 3）。
- 选项来源是 `.cproject` 的 `Debug_FLASH` 配置；先 `parse` 确认 include 无 `[MISS]` 再 `check`。
- 工具链/SDK 路径自动探测；失败时复制 `config/sdk_paths.conf.example` 为 `config/sdk_paths.conf` 显式指定。
- 产物与日志在 `output/`（gitignore），不要提交。
- 详细坑位与良性告警清单见 [reference/platform-notes.md](reference/platform-notes.md)。

## 目录

```
toolchains/s32ds/
├── scripts/s32ds_compile.py     # 后端实现
├── utils/build.bat              # 交互式构建入口
├── config/
│   ├── build_mode.conf          # 本机模式(忽略入库)
│   ├── build_mode.conf.example
│   └── sdk_paths.conf.example
├── reference/platform-notes.md
└── output/                      # 编译产物(已 gitignore)
```
