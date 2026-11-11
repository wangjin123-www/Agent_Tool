# PEmicro 探针（embedded-build-debug / probes/pemicro）

烧录/调试域的 PEmicro 实现（Multilink，S32K312）。S32DS 工程的默认探针——`Project_Settings/Debugger/*_PNE.launch`（`com.pemicro.debug.gdbjtag.pne`）就是它。统一入口在上层：`scripts/mcu_build_debug.py --probe pemicro <命令>`。

## 能力

| 探针命令 | 实现 | 说明 |
|---|---|---|
| `download <elf\|hex>` | gdb `load` | 烧录（自动擦写所需扇区）+ 复位运行 |
| `erase` | `monitor erase` | 整片擦除 + 复位 |
| `reset` | `monitor reset` | 复位 |
| `verify <elf>` | gdb `compare-sections` | 比对 ELF 段与 Flash（仅 elf） |
| `probe halt` / `go` | `monitor halt/go` | 停住/恢复 CPU（halt 后保持停住） |
| `probe regs` | `info registers` | 停住并读全部核心寄存器 |
| `probe read_mem --address 0x.. --size <N>` | `x/Nwx` | 读内存（N = 字数，4 字节/字） |
| `probe write_mem --address 0x.. --value 0x..` | `set {unsigned int}` | 写 32 位内存 |
| `dump_cortex` | `info registers` + `x/1wx` | HardFault 现场导出 + CFSR/HFSR 位域解析（**复用 J-Link 侧 analyze_fault，口径一致**） |

技术路径：**pegdbserver_console + arm-none-eabi-gdb batch**，两者都随 S32DS 安装、零新增部署。与 S32DS GUI 的 launch 用的是同一台 GDB Server，行为一致。

流程：启动 `pegdbserver_console -startserver -device=NXP_S32K312 -interface=usbmultilink -serverport=7224`（子进程）→ 端口就绪后 gdb batch 执行 `target remote → load/erase/regs/x… → detach|disconnect` → 自动关闭 server。调试类命令结尾用 `disconnect`（不恢复运行，现场保持），烧录类用 `detach`。

## 配置

`config/pemicro.conf`（从 `pemicro.conf.example` 复制，不入库）。通常全留空走自动探测；要点：

- `S32DS_ROOT`：留空自动扫 `C:/NXP/S32DS.*`、`D:/NXP/S32DS.*`
- `DEVICE`：默认 `NXP_S32K312`（launch 里的 `NXP_S32K3xx_S32K312-SECUREDEBUG` 是安全调试变体，烧录用基础名）
- `INTERFACE`：`usbmultilink`（Multilink）/ `opensda` / `usbemulator` / `netshiel`

## 典型用法

```bash
# 编译 + 烧录一条龙（s32ds full → pemicro download）
python "$SKILL_DIR/scripts/mcu_build_debug.py" build_and_download

# 单独烧录
python "$SKILL_DIR/scripts/mcu_build_debug.py" --probe pemicro download Debug_FLASH/test_prj.elf

# 命令行调试（死机排查三板斧）
python "$SKILL_DIR/scripts/mcu_build_debug.py" --probe pemicro probe regs          # PC 停哪
python "$SKILL_DIR/scripts/mcu_build_debug.py" --probe pemicro probe read_mem --address 0x20000000 --size 16
python "$SKILL_DIR/scripts/mcu_build_debug.py" --probe pemicro dump_cortex         # HardFault 现场解析
```

## 未覆盖（走 S32DS GUI）

- 断点/单步/变量监视的交互式调试：仍用 S32DS 的 `*_PNE.launch`（Debug 配置）
- 多核烧录参数（`-corenum` 等，S32K358 场景才需要）

## 二期候选

pyOCD 0.36+ 官方 PEmicro 插件（`pip install pyocd[pemicro]`，Apache-2.0）：配 S32K3 CMSIS-DFP 后 `pyocd flash -t s32k312 xxx.elf` 一条命令；Zephyr MR-CANHUBK3(S32K344) 已实证。详细调研见 [reference/pemicro-notes.md](reference/pemicro-notes.md)。
