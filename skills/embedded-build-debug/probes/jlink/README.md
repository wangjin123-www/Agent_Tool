# J-Link 探针（embedded-build-debug / probes/jlink）

烧录/调试域的 J-Link 实现。**与编译工具链解耦**：只要拿到 hex/bin 镜像就能烧，不关心是 Keil 还是 S32DS 编译出来的。统一入口在上层：`scripts/mcu_build_debug.py --probe jlink <命令>`。

## 命令

| 探针命令 | 实现 | 说明 |
|---|---|---|
| `download [--file <hex/bin>]` | `flash_loader.py --slot-a` | 默认 Slot A 模式：从 0x8000 编程应用区，跳过 Flash 选项字节区（0x400-0x7FFF） |
| `full_download` | `flash_loader.py --full` | 擦除 → 下载 → 运行（范围来自链接脚本） |
| `erase` | `jlink_ops.py erase` | 按链接脚本范围擦除；无链接脚本时整片擦除 |
| `verify` | `jlink_ops.py verify` | 读回 Flash 与镜像比对（MD5） |
| `reset` | `jlink_ops.py reset` | 复位并运行 |
| `jlink --command <op>` | `jlink_cmd.py` | halt/go/regs/step/read_mem/write_mem/bp/read_reg |
| `dump_cortex` | `dump_cortex.py` | HardFault 现场导出 + CFSR/HFSR 位域分析 |

接口固定 SWD @ 4000kHz（沿用原 keil-debug 行为；要改在 `flash_loader.py`/`jlink_cmd.py` 的 `run_jlink` 里改）。

## 配置

`config/config.conf`（首次运行自动从 `config.conf.example` 生成，不入库）：

```bash
JLINK="D:/keil/ARM/Segger/JLink.exe"   # 自动探测: Keil 自带 Segger / SEGGER 官方目录
DEVICE="HC32F460PETB"                   # J-Link 设备名; S32K312 也受支持(需 SEGGER V6.89c+)
HEX_PATH="MDK/output/debug/DAB.hex"     # 默认镜像(相对仓库根), download 时可被 --file 覆盖
BIN_PATH="MDK/output/debug/DAB.bin"
LINKER_SCRIPT="MDK/config/linker/HC32F460xE.sct"  # erase/full_download 解析范围用
```

烧 S32DS 出的固件：`--probe jlink download --file Debug_FLASH/xxx.hex`（前提板上有 J-Link 接口且 `DEVICE` 改成对应 S32K3 型号）。

## 脚本

| 脚本 | 用途 |
|---|---|
| `jlink_entry.sh` | 探针调度入口 |
| `init_env.sh` | 配置加载 + JLink.exe 路径探测 |
| `flash_loader.py` | 参数化下载（hex/bin、Slot A、校验、完整流程） |
| `jlink_ops.py` | erase/verify/reset（复用 flash_loader 执行器） |
| `jlink_cmd.py` | 通用 J-Link 单步操作 |
| `dump_cortex.py` | Cortex-M 异常现场导出 |
| `parse_linker.py` | 链接脚本 → Flash 地址范围 |

## 生态参考（2026-11 调研）

**直接可用（二期升级方向）：**

- [square/pylink](https://github.com/square/pylink)（434★, Apache-2.0, 活跃）：J-Link C SDK 的 Python 封装，flash/erase/verify/regs/RTT/SWO 全 API。`pip install pylink` 后可替换手写 JLinkExe 脚本解析。
- [cortex-crash](https://pypi.org/project/cortex-crash/)（PyPI）：CFSR 解码 + addr2line 硬件栈展开 + 生成捕获桩；`dump_cortex` 的升级候选（自写解码逻辑也仅百行级，配 addr2line 用）。

**架构/形态参照：**

- [zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)（787★）：keil 技能 → jlink 技能的分层与本探针架构一致，子命令设计可参考。
- [Adancurusul/embedded-debugger-mcp](https://github.com/adancurusul/embedded-debugger-mcp)（213★）：probe-rs/OpenOCD 的 MCP+CLI+skill 三件套，含 `diagnose_fault`/`unwind_exception`，异常诊断流程可借鉴。
- [Klievan/jlink-mcp](https://github.com/Klievan/jlink-mcp)（43★）：J-Link/OpenOCD/BlackMagic 多探针 MCP，含 Cortex-M fault 解码；多探针抽象思路与本 skill `probes/` 层同构。

**按需直调：**

- [XIVN1987/DAPCmdr](https://github.com/XIVN1987/DAPCmdr)（61★, MIT）：JLink/DAPLink 通用命令行，含 HardFault 诊断 + SVD 寄存器解析。
- [z3oya/rttsh](https://github.com/z3oya/rttsh)（57★）：可脚本化 RTT 终端（自称 AI-ready），RTT 日志流子模块候选。
- 国产闭环参照：notnameuse/embedded-debug-skill（52★）、Rance-OwO/Serial-Agent（46★），"编译→烧录→串口→AI 分析"闭环，MIT。

**固件侧互补：**

- [armink/CmBacktrace](https://github.com/armink/CmBacktrace)（2198★）：固件侧 HardFault 捕获事实标准（需植入目标代码），与 `dump_cortex`（探针侧）互补。

## 前置条件

- J-Link 驱动已装（JLink.exe 可定位）
- 目标板已上电、探针已连接
- Python 3
