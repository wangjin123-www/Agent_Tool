# SIUL2 EIRQ（外部引脚中断 / Siul2_Icu_Ip）配置指南

> 适用：S32K3（S32K312/344…）+ RTD 4.0.0 `Siul2_Icu_Ip`。
> 训练库没有独立的 EIRQ 示例工程；本文以本工程 7255 的 PTC24/EIRQ19 心跳链实测为准，API 名与 RTD 头一致。
> 与 eMIOS ICU 区分：**EIRQ = 引脚边沿中断（只报事件）**；eMIOS ICU = 输入捕获测周期/占空比，见 `emios.md`。

## 1. 先记住三件事

1. **EIRQ 不需要 MSCR mux**：引脚 MSCR 保持 `PORT_MUX_AS_GPIO` 即可，关键是 `IBE=1`、`OBE=0`、需要时配 pull。Config Tools Pins 里把 signal 选成 `eirq, N`（N=EIRQ 通道号）。
2. **EIRQ 按 8 个一组映射到 4 条 NVIC 线**，选错组 = 回调永远不进。
3. **`Siul2_Icu_Ip_Init` 会清 `DIRER0`**：Init 之后必须对每个要用的通道调用 `Siul2_Icu_Ip_EnableInterrupt` + `Siul2_Icu_Ip_EnableNotification`，否则只有 `DISR0` 置位、不进中断。

## 2. NVIC 映射（S32K312，`S32K312_COMMON.h`）

| EIRQ 通道 | NVIC IRQ（编号） | 驱动 ISR | 处理函数 |
|---|---|---|---|
| 0–7 | `SIUL_0_IRQn`（53） | `SIUL2_EXT_IRQ_0_7_ISR` | `Siul2_Icu_Ip_ProcessInterrupt(0, SIUL2_ICU_IRQ_0)` |
| 8–15 | `SIUL_1_IRQn`（54） | `SIUL2_EXT_IRQ_8_15_ISR` | `Siul2_Icu_Ip_ProcessInterrupt(0, SIUL2_ICU_IRQ_8)` |
| 16–23 | `SIUL_2_IRQn`（55） | `SIUL2_EXT_IRQ_16_23_ISR` | `Siul2_Icu_Ip_ProcessInterrupt(0, SIUL2_ICU_IRQ_16)` |
| 24–31 | `SIUL_3_IRQn`（56） | `SIUL2_EXT_IRQ_24_31_ISR` | `Siul2_Icu_Ip_ProcessInterrupt(0, SIUL2_ICU_IRQ_24)` |

> IRQ 号以具体芯片的 `S32K3xx_COMMON.h` 为准；**向量名/分组固定**。本工程实例：ch19 → `SIUL_2_IRQn`，ch25 → `SIUL_3_IRQn`。

## 3. Config Tools 配置（三步）

### 3.1 Pins

- 选中目标引脚（Pin 页）→ Peripheral 选 `SIUL2` → Signal 选 `eirq, N`（如 PTC24 → `eirq, 19`）。
- 方向按输入；Config Tools 会生成：
  ```c
  .mux          = PORT_MUX_AS_GPIO,      /* EIRQ 不走 mux */
  .inputBuffer  = PORT_INPUT_BUFFER_ENABLED,
  .outputBuffer = PORT_OUTPUT_BUFFER_DISABLED,
  ```
- 需要上下拉就在 Pins 里配 `PUE/PUS`；不要把 EIRQ 脚配成输出（RM 明确会误触发）。

### 3.2 Peripherals → `Siul2_Icu`

在 `Siul2_Icu / IcuConfigSet` 下：

1. `IcuMaxChannel` = 实际通道数（每加一个通道 +1）。
2. `IcuChannel` 增一项：
   - `IcuChannelRef` 指向对应的 `IcuSiul2Channels_N`
   - `IcuDefaultStartEdge`：`ICU_RISING_EDGE` / `ICU_FALLING_EDGE` / `ICU_BOTH_EDGES`
   - `IcuSignalEdgeDetection` 的 notification 填回调名（如 `Icu_SocHeartbeat_callback`）
3. `IcuSiul2Channels` 增一项：
   - `IcuSiul2Channel = N`（物理 EIRQ 通道号）
   - `Icu_EXT_ISR_IFERDigitalFilter` / `Icu_EXT_ISR_IFMCDigitalFilter` 配数字滤波
4. `IcuHwInterruptConfigList` 增一项：
   - `IcuIsrHwId = SIUL2_0_IRQ_CH_N`
   - `IcuIsrEnable = true`

### 3.3 Peripherals → `IntCtrl_Ip`

在 `IntCtrlConfig_0 / PlatformIsrConfig` 增一项：

| 字段 | 值（以 EIRQ19 为例） |
|---|---|
| `IsrName` | 按第 2 节选：ch16–23 → `SIUL_2_IRQn`；ch24–31 → `SIUL_3_IRQn` |
| `IsrEnabled` | `true` |
| `IsrPriority` | 按系统优先级（本工程 SIUL_2 = 2） |
| `IsrHandler` | 对应组 ISR：`SIUL2_EXT_IRQ_16_23_ISR` / `SIUL2_EXT_IRQ_24_31_ISR` |

## 4. 生成后必须核对的文件

| 生成物 | 期望内容 |
|---|---|
| `generate/include/Siul2_Icu_Ip_Cfg.h` | `#define SIUL2_ICU_IRQ_CH_N_ISR_USED` |
| `generate/include/Siul2_Icu_Ip_Defines.h` | `SIUL2_ICU_IP_NUM_OF_CHANNELS_USED` = 通道数；`SIUL2_ICU_IP_INITIAL_INDEX_OF_CHANNELS` 里通道 N 有非 255 索引 |
| `generate/include/Siul2_Icu_Ip_SA_PBcfg.h` | `ChannelConfig_PB[通道数 U]` |
| `generate/src/Siul2_Icu_Ip_SA_PBcfg.c` | 通道 N 的 `hwChannel`、边沿、`&回调名`、`numChannels` |
| `generate/include/IntCtrl_Ip_Cfg.h` | `extern void SIUL2_EXT_IRQ_x_y_ISR(void);` |
| `generate/src/IntCtrl_Ip_Cfg.c` | `{SIUL_x_IRQn, TRUE, 优先级, SIUL2_EXT_IRQ_x_y_ISR}`，入口计数 +1 |

## 5. RTD 初始化代码

```c
/* 1) NVIC：先让 interrupt controller 认识这条 IRQ（IntCtrlConfig_0 里已生成） */
IntCtrl_Ip_Init(&IntCtrlConfig_0);

/* 2) IP 初始化：会清 DIRER0，必须一次把 PBcfg 通道配好 */
(void)Siul2_Icu_Ip_Init(0U, &Siul2_Icu_Ip_0_Config_PB);

/* 3) 逐个通道使能：DIRER0 + notificationEnable */
Siul2_Icu_Ip_EnableInterrupt(0U, ch);
Siul2_Icu_Ip_EnableNotification(0U, ch);
```

回调注册关系：

- PBcfg 的 `Siul2ChannelNotification` 是 `void (*)(void)` 类型 → 对应 `Icu_SocHeartbeat_callback(void)` 这类无参回调。
- `Siul2_Icu_Ip_ProcessInterrupt` → `Siul2_Icu_Ip_ReportEvents` 分派规则：
  1. `callback != NULL` → 先调 HLD callback（带 `(param, FALSE)`）；
  2. 否则 `Siul2ChannelNotification != NULL && notificationEnable == TRUE` → 调 notification。
- 所以 **`EnableNotification` 不能漏**；用了 HLD `callback` 时 notification 不会走。

## 6. 寄存器自检（调试器直接看）

| 寄存器 | 期望 |
|---|---|
| `MSCR[pin]` | `IBE=1`、`OBE=0`、`PUE/PUS` 按硬件 |
| `IREER0[ch]` / `IFEER0[ch]` | 上升沿/下降沿二选一（或都置 = 双边沿） |
| `IFER0[ch]` / `IFMCR[ch]` | 数字滤波使能/计数值（滤波需要 IRC 时钟） |
| `DIRSR0[ch]` | `0`=中断，`1`=DMA |
| `DIRER0[ch]` | `1`（中断使能） |
| `DISR0[ch]` | 引脚出现匹配边沿时置 1，写 1 清除 |
| NVIC `ISER` | 对应 `SIUL_x_IRQn` 位 = 1 |

## 7. 调试顺序（回调不进时）

1. 拉低/拉高引脚制造边沿 → 看 `DISR0[ch]` 是否置位。
   - 不置位：MSCR 的 `IBE/OBE`、边沿寄存器 `IREER0/IFEER0`、引脚是否真的在动（示波器）。
2. `DISR0` 置位但不进 ISR → 查 `DIRER0[ch]`、NVIC `ISER`、向量表里 `SIUL_x_IRQn` 的 handler 是否是该组 ISR。
3. 进 ISR 但不回调 → `notificationEnable` 未置位 / PBcfg 的 `Siul2ChannelNotification` 为空 / HLD `callback` 抢先。
4. 编译链接自检：
   ```bash
   arm-none-eabi-nm <obj>/RTD_src_Siul2_Icu_Ip_Irq.o | grep SIUL2_EXT_IRQ
   arm-none-eabi-nm <obj>/generate_src_IntCtrl_Ip_Cfg.o | grep SIUL2_EXT_IRQ
   arm-none-eabi-nm <obj>/generate_src_Siul2_Icu_Ip_SA_PBcfg.o | grep Icu_
   ```
   ISR 应为 `T`，IntCtrl/PBcfg 对 ISR/回调应为 `U`。

## 8. 常见坑

1. **组号/IRQ 选错**：ch19 是 16–23 组 → `SIUL_2_IRQn` + `SIUL2_EXT_IRQ_16_23_ISR`；ch25 是 24–31 组 → `SIUL_3_IRQn` + `SIUL2_EXT_IRQ_24_31_ISR`。按“引脚号”去猜 IRQ 必错。
2. **`Siul2_Icu_Ip_Init` 清 `DIRER0`**：初始化后再 `EnableInterrupt`；多个模块分时初始化时，重 Init 必须把已登记通道重新使能。
3. **`Siul2_Icu_Ip_DeInit(instance)` 是实例级**：会把所有已初始化通道一起关掉；只想关本通道用 `DisableInterrupt` + `DisableNotification`。
4. **MSCR mux 不是 EIRQ**：`PORT_MUX_AS_GPIO` 是正确形态（本工程 PTB11/EIRQ25、PTC24/EIRQ19 均如此）；Pins 工具的 `signal: 'eirq, N'` 只是工具标签。
5. **生成物与 mex 不同步**：只改 `board/`、`generate/` 不改 `test_prj.mex`，Config Tools 下次生成会整体回退；Config Tools 打开工程时手改 mex 会被内存模型覆盖（2026-11-05 实测）。先改 mex（或 GUI）再生成。
6. **数字滤波依赖 IRC 时钟**：RM 明确“滤波需要内部振荡器；时钟不可用时使能滤波会关掉中断”。

## 9. 本工程实例：PTC24 / EIRQ19 SoC 心跳

| 环节 | 落点 |
|---|---|
| Pins | `board/Siul2_Port_Ip_Cfg.c`：pin 88 `signal: 'eirq, 19'`，MSCR `IBE=1/OBE=0` |
| ICU 通道 | `generate/src/Siul2_Icu_Ip_SA_PBcfg.c`：ch19、`SIUL2_ICU_FALLING_EDGE`、`&Icu_SocHeartbeat_callback` |
| ISR | `generate/include/Siul2_Icu_Ip_Cfg.h`：`SIUL2_ICU_IRQ_CH_19_ISR_USED` → `SIUL2_EXT_IRQ_16_23_ISR` |
| NVIC | `generate/src/IntCtrl_Ip_Cfg.c`：`{SIUL_2_IRQn, TRUE, 2U, SIUL2_EXT_IRQ_16_23_ISR}` |
| 登记 | `Service_BoardInitBeforePwrOn()` → `EcuAL_Interrupt_UpInf.IcuInit(ECUAL_INTERRUPT_ICU_CH_SOC_HEARTBEAT)` |
| 回调 | `Service_Board.c`：`Icu_SocHeartbeat_callback()` 只做 `s_SocHeartbeatIrqCnt++` |
| 消费 | `App_PowerHsm` HALF_RUN：计数 > 0 → 心跳到达；2000×5ms=10s 超时 → `SocOffAndMcuReset()` |

一次下降沿的完整链路：

```text
PTC24 下降沿 → IFEER0[19] → DISR0[19] → DIRER0[19] → SIUL_2_IRQn
→ SIUL2_EXT_IRQ_16_23_ISR → Siul2_Icu_Ip_ProcessInterrupt(0, SIUL2_ICU_IRQ_16)
→ Siul2_Icu_Ip_ReportEvents(19) → Icu_SocHeartbeat_callback()
```
