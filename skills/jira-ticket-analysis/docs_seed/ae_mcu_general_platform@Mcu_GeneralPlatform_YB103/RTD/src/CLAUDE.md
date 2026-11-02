# RTD/src — NXP RTD 4.0.0 原厂驱动实现(纯 MCAL/IP 库代码,勿手改)

NXP S32K3 RTD 4.0.0_P01(S32K3_RTD_4_0_0_P01_D2311,ASR 4.7,CORTEXM)驱动实现层:108 个 .c 全部为原厂交付代码。接口头文件在 `RTD/include/`,与本目录文件成对。

## Key Files(按驱动家族分组)
- `Clock_Ip.c`(+Divider/ExtOsc/IntOsc/Pll/Gate/Selector/FracDiv/Monitor/ProgFreqSwitch/Frequency/Specific/Data/Irq 共 14 文件) - 时钟树驱动,按功能拆分;配置以 `Clock_Ip_ClockConfigType` 指针传入
- `IntCtrl_Ip.c` - 中断控制器初始化、handler 安装/使能;`*_Ip_Irq.c` 中的 ISR 都经它挂接
- `OsIf_Timer.c` / `OsIf_Timer_System*.c` / `OsIf_Interrupts.c` - 所有驱动超时/忙等的时间源抽象(Systick 变体)
- `C40_Ip.c` / `Pflash_Ip.c` / `Mem_43_INFLS.c`(+Ipw)/ `MemAcc.c` / `Fee.c` - Flash 存储栈自底向上:C40 IP → INFLS/Pflash → MemAcc → Fee(EEPROM 仿真,Fee 依赖 MemAcc)
- `FlexCAN_Ip.c` / `Lpuart_Uart_Ip.c` / `Lpi2c_Ip.c` / `Lpspi_Ip.c` / `Lpuart_Lin_Ip.c`+`Lin_Ip_Common.c` - 通信外设(CAN/UART/I2C/SPI/LIN)
- `Hse_Ip.c` + `Mu_Ip_Irq.c` - 硬件安全引擎(HSE)经 MU(消息单元)通信,配套 `HSE/` 固件工程
- `Adc_Sar_Ip.c` / `Emios_Mcl_Ip.c` / `Emios_Pwm_Ip.c` / `Emios_Icu_Ip.c` / `Dma_Ip.c` / `Siul2_Port_Ip.c` / `Siul2_Dio_Ip.c` / `Siul2_Icu_Ip.c` - ADC/定时器/PWM/ICU/DMA/IO
- `Power_Ip.c`(+CortexM7/MC_ME/MC_RGM/PMC/DCM_GPR/FLASH/AEC/Irq) - 电源模式切换,按硬件单元拆分
- `SchM_*.c`(18 个) - 无 RTE 环境下的独占区临界段实现(SchM_Enter/Exit_<MOD>_EXCLUSIVE_AREA_xx)
- `Det.c` - AUTOSAR DET 错误上报服务;`Det_stub.c` - 配套测试桩(记录/校验最近一次上报)
- `Cache_Ip.c` / `Axbs_Ip.c` / `Mscm_Ip.c` / `Sema42_Ip.c` / `Swt_Ip.c` / `Xrdc_Ip.c` / `Xbic_Ip.c` / `Wkpu_Ip.c` - Cache/总线矩阵/系统控制/硬件信号量/看门狗/访问控制/错误报告/唤醒

## Gotchas
- 每个文件头部有 vendor/ASR 版本一致性编译检查,不匹配直接 `#error "... different vendor ids"`:升级 RTD 必须整包替换 src+include,严禁单文件混搭
- MemMap 段放置模式:代码被 `#define X_START_SEC_...` / `#include "X_MemMap.h"` 成对包裹,段属性由 MemMap 头控制;手工增删代码必须保持成对结构
- 中断收不到先查两处:IntCtrl_Ip 是否安装了对应 handler、`*_Ip_Irq.c` 是否参与编译(Irq 文件常按配置条件编译)
- OsIf 依赖系统时钟:时钟未初始化前调用带超时的驱动 API 会立即异常返回
- 所有驱动运行参数来自传入的配置结构,不在本目录内;改外设行为去调用方/配置侧,不要改驱动本体
