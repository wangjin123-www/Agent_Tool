# Keil 工具链（embedded-build-debug / toolchains/keil）

编译域的 Keil MDK 实现（UV4 命令行编译 + fromelf 出 bin + 结构化摘要）。**统一入口在上层**：`scripts/mcu_build_debug.py --toolchain keil <命令>`；烧录/调试走 `probes/jlink`，本目录不管探针。

## 命令映射

| 工具链命令 | 本后端脚本 | 说明 |
|---|---|---|
| `build` / `check` | `keil_build.sh build` | 增量编译 + fromelf 生成 bin + JSON 摘要 |
| `rebuild` | `keil_build.sh rebuild` | 清中间物后全量编译 |
| `parse` | `keil_build.sh parse` | 解析 `MDK/build.log` 输出 JSON 摘要 |
| `flash_check` | `keil_build.sh flash_check` | 解析 map，输出 Flash/RAM 占用 |
| `diff` | `keil_build.sh diff` | 两次构建体积对比 |
| `report` | `keil_build.sh report` | 生成 HTML 调试报告 |

编译+烧录一条龙：`mcu_build_debug.py build_and_download`（keil build → jlink download，由统一入口串联）。

## 配置

首次运行 `init_env.sh` 会把 `config/config.conf.example` 复制为 `config/config.conf`（不入库），并自动定位 `UV4`、`fromelf`（找不到时交互询问并写回）。

```bash
UV4="D:/keil/UV4/UV4.exe"
FROMELF="D:/keil/ARM/ARMCC/bin/fromelf.exe"
UV4_TARGET="hc32f460petb_Debug"   # uvprojx 中的 TargetName
MDK_DIR="MDK"                      # 相对仓库根
UVPROJX="hc32f460petb.uvprojx"
TARGET_NAME="DAB"
OUTPUT_SUBDIR="output/debug"       # MDK 下产物子目录(.axf/.bin/.map)
```

烧录设备名、镜像路径等探针配置见 `probes/jlink/config/`。

## 脚本

| 脚本 | 用途 |
|---|---|
| `keil_build.sh` | 工具链调度入口（build/rebuild/parse/flash_check/diff/report） |
| `init_env.sh` | 配置加载 + UV4/fromelf 路径探测 |
| `parse_build_log.py` | 编译日志 → JSON（错误/内存/耗时） |
| `check_flash_usage.py` | map → Flash/RAM 占用 |
| `diff_build.py` | 两次编译体积差异 |
| `generate_html_report.py` / `generate_report.py` | HTML 报告 |
| `generate_build_summary.py` / `generate_debug_report.py` | 摘要/调试报告生成 |
| `log_history.py` | 编译历史 |

## 前置条件

- Keil MDK 已安装，`UV4.exe` 可用
- Python 3
- 目标板/探针相关条件见 `probes/jlink/README.md`
