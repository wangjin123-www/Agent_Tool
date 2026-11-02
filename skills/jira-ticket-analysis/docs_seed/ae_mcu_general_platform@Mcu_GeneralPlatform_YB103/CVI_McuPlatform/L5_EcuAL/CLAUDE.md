# L5_EcuAL(ECU 抽象层:把 RTD/MCAL IP 驱动封装成统一外设接口,供 L4_Services 通过 UpInf 表调用)

## Architecture
```
L5_EcuAL/
  EcuAL_Mcu/         # 时钟/电源模式/复位原因/CAN 唤醒(Clock_Ip+Power_Ip+Wkpu_Ip+Siul2_Icu_Ip)
  EcuAL_Port/        # 引脚复用与 DIO(Siul2_Port_Ip+Siul2_Dio_Ip;含 111 项引脚索引表)
  EcuAL_Interrupt/   # IRQ 使能/关闭(IntCtrl_Ip)
  EcuAL_Adc/         # ADC 组 0/1 采样(Adc_sar_Ip)
  EcuAL_Can/         # CAN0/CAN1 收发与收发 ISR 回调(FlexCAN_Ip)
  EcuAL_Uart/        # LPUART 串口(Lpuart_Uart_Ip+DMA 双缓冲;另拆 Buffer/Cfg/Types)
  EcuAL_Lin/         # LIN 主/从(LpUart_Lin_Ip;Master/Slave LowInf 分文件)
  EcuAL_I2c/         # I2C 主/从(Lpi2c_Ip;Master/Slave LowInf 分文件)
  EcuAL_I2cSim/      # GPIO 位模拟 I2C(SCL/SDA 方向+电平软件控制)
  EcuAL_Spi/         # SPI(Lpspi_Ip+Dma_Ip)
  EcuAL_Pwm/         # PWM/输入捕获(Emios_Pwm_Ip+Emios_Mcl_Ip+Emios_Icu_Ip)
  EcuAL_Timer/       # 7 路定时器(Gpt+Mcl)
  EcuAL_DMA/         # DMA 管理(Dma_Ip+Dma_Mux_Ip)
  EcuAL_Fls/         # Flash:块读写走 Fee,裸 PFlash 扇区擦写走 C40_Ip
  EcuAL_RTC/         # RTC 时间/闹钟(Rtc_Ip)
  EcuAL_Watchdog/    # 喂狗(Swt_Ip;须周期调 EcuAL_Wdg_MainFunction)
  EcuAL_Hse/         # HSE 桥接(引用仓库根 HSE/HSE_SRC 主机驱动+Hse_Ip)
```

## Key Pattern(每子模块三层函数指针表)
- `EcuAL_Xxx.c/h`:业务接口,定义 `EcuAL_Xxx_Impl` 表(静态初始化)
- `EcuAL_XxxLowInf.c/h`:直接包 RTD IP 驱动,定义 `EcuAL_Xxx_LowInf` 表
- `EcuAL_XxxUpInf.c/h`:对上暴露 `EcuAL_Xxx_UpInf` 表
- 下行:Impl → NULL 检查 → LowInf;中断上行:IsrCallback → NULL 检查 → UpInf → L4
- L4_Services 消费约定:通过 UpInf 表(如 `EcuAL_Port_UpInf.EalPort_UpInf_UartInit(...)`),不直调函数

## Gotchas
- 工程宏条件编译:`PROJECT_WEIQIAO_YB103/WY113` 与 `PROJECT_WEIQIAO_WB101` 决定 UART 通道数(2/3)、缓冲大小(2048/512 vs 1024/256);WB101 下逻辑通道 2 重映射到 LPUART5(PTB27/28,`ECUAL_PDC_UART_CHANNEL=5`)
- 引脚运行时可复用:EcuAL_PortLowInf.c 持有 `g_pin_mux_InitConfigArr_*` 表,按 DevMuxMode 在 GPIO/UART/CAN/LIN/SPI 模式间切换(如 CAN0 RX 有 GPIO/CAN/EIRQ 三态);引脚身份用 `INIT_PINARR_INDEX_*` 索引 Config Tools 生成的 `g_pin_mux_InitConfigArr_PortContainer_0_BOARD_InitPeripherals`
- 存在 L5→L4/L3 反向 include:`EcuAL_LinLowInf_Master.c` 引 L4 Service_DebugUpInf 与 FreeRTOS,`EcuAL_CanLowInf.c` 引 Service_Board_Port;新增代码勿扩散此模式
- 新增外设 API 必须同步扩展 Impl/LowInf/UpInf 三张表,漏一张上层即不可达
- UART 应用缓冲 `ECUAL_UART_MAX_BUFFER_SIZE` 必须为 2 的幂(环形缓冲要求);RX 用 rxdata_a/b 双缓冲供 DMA 与应用并行
- ADC 逻辑通道号 ≠ 物理通道号,转换查 `EcuAL_AdcLowInf.c` 的 `Eal_AdcGroupX_Channel[]` 表
- `EcuAL_I2c_Slave.h` 重复声明了 MasterInit/MasterDeinit(复制粘贴产物,非笔误勿删)
