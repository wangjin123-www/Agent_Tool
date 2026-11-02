# generate(NXP RTD 4.0 / EB tresos 生成的外设配置层,随仓提交且含手改)

## Commands
| Command | Description |
|---------|-------------|
| (无) | 本目录只含生成代码,不单独构建;编译由上层 IDE/Project_Settings 工程统一执行 |

## Architecture
```
generate/
  include/   # 各 IP 的 *_Cfg.h / *_CfgDefines.h / *_PBcfg.h,外加 FreeRTOSConfig.h、modules.h
  src/       # 对应 *_Cfg.c(静态配置)与 *_PBcfg.c / *_Sa_PBcfg.c(外设实例配置)
```

## Key Files
- `include/modules.h` - 模块使能总表(USE_*_MODULE)与 AUTOSAR 版本一致性宏
- `include/FreeRTOSConfig.h` - RTOS 参数:120MHz CPU 时钟、1kHz tick、12 级优先级、20KB 堆、静态+动态分配
- `include/Clock_Ip_Cfg.h` + `src/Clock_Ip_Cfg.c` - 时钟树(FXOSC 16MHz → PLL → CORE_CLK 120MHz)与外设时钟源
- `include/IntCtrl_Ip_Cfg.h` + `src/IntCtrl_Ip_Cfg.c` - 中断向量映射与优先级分组
- `src/Lpuart_Uart_Ip_Sa_PBcfg.c` + `src/Dma_Ip_PBcfg.c` + `src/Dma_Mux_Ip_PBcfg.c` - UART0+DMA 链路配置(近期改动集中地)

## Gotchas
- 生成代码随 git 提交且被手工修改(git 历史证实 IntCtrl/DMA/UART 生成文件随 feature 提交直接改动);仓库内没有 tresos 工程 —— 任何"重新生成"都会覆盖手改,改配置前先 `git log -p` 确认手改内容。
- `modules.h` 的 `USE_ZIPWIRE_MODULE` 值是未展开的 tresos 模板宏 `$Macro_IsModuleUsed("Zipwire")$`,一旦该宏进入编译路径会直接编译失败。
- `USE_<MODULE>_MODULE` 只反映 AUTOSAR 模块层(FEE/RM/MemAcc 为 STD_ON,ADC/SPI/MCU 等为 STD_OFF),不代表 IP 驱动不存在;判断 IP 驱动(Adc_Sar_Ip、Lpspi_Ip 等)以 *_Cfg 文件与上层引用为准。
- `configCPU_CLOCK_HZ`(120MHz)必须与 `Clock_Ip_Cfg.c` 的 CORE_CLK 频率一致;改时钟两处同步,否则 tick 周期漂移。
- OsIf 时基用 SysTick(`OSIF_USE_SYSTICK`=STD_ON,含 `S32K312_SYSTICK.h`),与 FreeRTOS tick 相关改动需联动检查。
