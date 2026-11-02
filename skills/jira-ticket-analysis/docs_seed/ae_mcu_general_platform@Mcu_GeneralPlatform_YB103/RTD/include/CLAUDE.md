# RTD/include(NXP S32K3 RTD IP 驱动层公共头文件库)

NXP 官方 RTD 驱动包的对外头文件(179 个),覆盖 ADC/CAN/UART/SPI/I2C/DMA/时钟/电源/存储/安全等外设的 IP 层 API 与类型。版本基线见各头文件 Build Version:`S32K3_RTD_4_0_0_P01_D2311`(AUTOSAR 4.7)。NXP 版权文件,禁止手改。

## Architecture
```
RTD/include/
  <外设>_Ip.h              # 各 IP 驱动主 API(初始化/收发/控制)
  <外设>_Ip_Types.h        # 对应类型与配置结构体
  <外设>_Ip_Irq.h          # 中断服务函数声明(对接向量表)
  <外设>_Ip_HwAccess.h     # 寄存器级访问内联
  <外设>_Ip_TrustedFunctions.h  # 用户模式可信调用封装
  SchM_*.h                 # BSW 调度器样例桩(官方注明 sample code)
  Det.h / Det_stub.h       # AUTOSAR 开发错误跟踪及其桩
  OsIf_*.h                 # OS 抽象/延时定时器(Systick/Custom 两种变体)
```

## Key Files
- `RTD/include/Clock_Ip.h` - 时钟树配置 API;芯片派生参数拆在 `Clock_Ip_Derivative_001..009.h`
- `RTD/include/FlexCAN_Ip.h` - CAN 驱动;服务函数名见 `FlexCAN_Ip_Irq.h`
- `RTD/include/Siul2_Port_Ip.h` / `Siul2_Dio_Ip.h` - 引脚复用与 GPIO
- `RTD/include/Lpuart_Uart_Ip.h` / `Lpspi_Ip.h` / `Lpi2c_Ip.h` - LPUART/LPSPI/LPI2C 串行族
- `RTD/include/C40_Ip.h` / `Pflash_Ip.h` / `Mem_43_INFLS.h` / `Fee.h` - 闪存与存储栈
- `RTD/include/Power_Ip.h` - 电源/复位;子模块拆分(MC_ME/MC_RGM/PMC/DCM_GPR/FLASH 等)
- `RTD/include/Hse_Ip.h` - 硬件安全引擎接口(与 HSE/ 目录配套)
- `RTD/include/IntCtrl_Ip.h` - 中断控制器(NVIC)配置

## Gotchas
- 本目录只有 IP 层公共头,**不含任何 `*_Ip_Cfg.h`/`*_Ip_Defines.h`**——配置头由 `generate/include/`(34 个)和 `board/`(2 个,含 `Siul2_Port_Ip_Cfg.h`)提供;编译 include 路径必须同时覆盖 `RTD/include/`、`generate/include/`、`board/` 三处。
- `Std_Types.h`/`Devassert.h`/`MemMap.h` 不在 RTD/ 内(全仓唯一副本在 `CVI_McuPlatform/L4_Services/Service_Canbus/Service_CanAsrNm/Can_AsrNM/`),同样依赖 include 路径解析,新建编译目标时最易漏配。
- `*_Ip_Irq.h` 声明的服务函数名(如 `FlexCAN_IRQHandler`)必须与 `Project_Settings/` 启动文件向量表一致;增删外设中断需两处同步。
- 头间有版本一致性校验宏(VENDOR_ID/AR_RELEASE_*),不同 RTD 版本的文件混用会直接编译失败;升级 RTD 时整目录替换。
- `SchM_*.h` 官方声明为样例代码、非生产交付;真正的临界区/排产由平台层实现,勿在其中写业务逻辑。
