# 提交规范检查基准（norm spec）

本文件是 agent 规范分析（analyze 阶段）与 execute 入口校验的唯一规范依据。
**检查的是"规范/分层/命名"，不是代码逻辑缺陷**（逻辑缺陷走 AI代码审核，不走本流程）。

工程：CDC_7255（NXP S32K312 + AUTOSAR 4.7 RTD），参考工程：6125（`6125/FreeRTOS_S32K312/CVI_McuPlatform`）。

---

## 一、分层总则（核心）

**依赖方向严格单向**：

```
L1_APP → L2_Tasks → L3_RTOS → L4_Service → L5_EcuAL → RTD
```

`L6_Public` 是**公共定义层**（类型别名、开关宏），**被各层引用、不参与依赖方向**；禁止跨层直呼、禁止反向依赖。

| 层 | 目录 | 职责 | 命名语义 | 能调用 |
|----|------|------|----------|--------|
| 应用层 | `L1_APP/` | 业务逻辑、场景决策 | **业务语义**（"为什么"） | 本层 + Tasks/Service 的 UpInf |
| 任务层 | `L2_Tasks/` | OS 任务绑定、消息表 | 任务语义 | 本层 + **经 `Tasks_LowInf` 表**访问 L3_RTOS |
| 调度层 | `L3_RTOS/` | OS1_FreeRTOS / OS2_TmrSched | OS 语义 | 下层 UpInf |
| 服务层 | `L4_Service/` | 通用服务、资源管理 | **功能语义**（"做什么"） | 本层 + EcuAL 的 UpInf |
| 外设抽象层 | `L5_EcuAL/` | 硬件抽象、RTD 封装 | **硬件编号**（"哪个引脚"） | 本层 + RTD |
| 公共层 | `L6_Public/` | 类型别名、开关宏 | 公共语义 | 无（纯头，被各层引用） |

### 层间解耦（双向接口）

- **上层经 LowInf 调下层**：上层调下层能力，走己方 `XxxLowInf`（内部转发到下层 UpInf 表）。
- **下层经 UpInf 回调上层**：下层需上报上层，走己方 `XxxUpInf` 里注册的上层回调，**不得反向 include 上层实现**。

### Task 层与 L3_RTOS 的绑定（双后端）

Task 层**只能经 `Tasks_LowInf` 函数指针表**访问 L3_RTOS，**不得直接调 FreeRTOS / 裸机 API**：

| 项 | 位置 | 说明 |
|----|------|------|
| 表实例 | `L2_Tasks/Tasks.c` `STRUCT_TASKS_LOWINF Tasks_LowInf = {...}` | 六组 `OsIf_*` 转发 |
| 声明 | `L2_Tasks/Tasks.h` `extern STRUCT_TASKS_LOWINF Tasks_LowInf;` | 上层只 include 此头 |
| 后端切换 | `L6_Public/Os_TypeDef.h` 的 `MCU_SCHED_TYPE` | `MCU_USING_FreeRTOS`(=1) → `Os1If_UpInf`；`MCU_USING_TMRSCHED`(=0) → `Os2If_UpInf`（裸机轮询） |
| 合法调用 | `Tasks_LowInf.Os_StartScheduler()` / `Tasks_LowInf.Os_GetSysTickCount()` | 上层（含 L1_APP）经表调用 |
| 边界说明 | `Tasks.c` 内 include `FreeRTOS.h`/`task.h` | 属 **OS 绑定层职责内**的实现细节（转发分支内使用），**不算违规**；但 `L1_APP`/`L4_Service` 等层**不得**直调 FreeRTOS API |

**判据一句话**：越往上越贴近业务语义，越往下越贴近硬件编号。

### 分层命名实例（LED，用户给定判例）

| 命名 | 应属层 | 理由 |
|------|--------|------|
| `红灯` / `绿灯` / `电量指示灯` | **App** | 业务语义：为什么亮 |
| `led1` / `led2` | **Service** | 功能编号：哪一个资源 |
| `gpio1` / `gpio2` | **EcuAL** | 硬件编号：哪一个引脚 |

### 7255 vs 6125 实证

| 层 | 7255 现状 | 6125 参考 | 结论 |
|----|-----------|-----------|------|
| App | `App_Power` `App_SocCom` `App_Can` `App_Candiag` | `App_Cluster` `App_Key` `App_LIN` `App_Power` `App_Mem` `App_Hse` | 都用**功能/业务名**，不用编号 |
| Task | `Task_Power` `Task_Shell` `Task_SocComm` | `Task_Power` `Task_Can` `Task_Lin` `Task_Cluster1` | 都用 Task_ 前缀 |
| Service | `Service_Board` `Service_Debug` `Service_Power` `Service_SocComm` | `Service_Board` `Service_Debug` `Service_Key` `Service_Memory` `Service_Power` | 都用**功能名** |
| EcuAL | `EcuAL_GPIO` `EcuAL_PWM` `EcuAL_UART` `EcuAL_Pit` | `EcuAL_Port` `EcuAL_Pwm` `EcuAL_Adc` `EcuAL_I2c` `EcuAL_Uart` | 都用**硬件/外设名** |
| Public | `L6_Public/*.h` | `L6_Public/Public_TypeDef/` | 纯头、无 .c |

**注意 7255 既有偏差**（不要求本次修，但新代码不得复制）：6125 EcuAL 是 `EcuAL_Port`（把 GPIO 归入 Port 抽象），7255 是 `EcuAL_GPIO`。新模块照 7255 现有风格即可，**同一工程内保持一致**优先。

---

## 二、UpInf / LowInf 接口约定（模块抽象边界）

每个可复用模块（App / Service / EcuAL）的**层间接口文件名固定三件套**（前两件必有；`LowInf` 仅在需向下调下层时建，`Cfg` 仅在需配置数据时建）：

```
Xxx/                      例：EcuAL_Spi/
├── Xxx.c / Xxx.h         实现 + 内部声明（外部不得直接 include）
├── XxxUpInf.c / .h       向上暴露的函数指针接口表（唯一对外面）
├── XxxLowInf.c / .h      本模块调用下层的适配（可选）
└── Xxx_Cfg.c / .h        配置承载：静态分配缓冲/队列/上下文（可选，见硬规则 8）
```

**硬规则**：

1. **跨层调用只能走 UpInf**。上层 `#include` 下层时，只允许 `XxxUpInf.h`；直接 include `Xxx.h`（内部头）或 `XxxLowInf.h` 一律违规。
2. **UpInf 头暴露的符号**：
   - 函数指针结构体 `STRUCT_<模块>_UPINF` + 全局实例 `extern STRUCT_<模块>_UPINF <模块>_UpInf;`
   - 或直接函数原型 `<模块>UpInf_Init/Deinit/MainFunction` 等
3. **函数名前缀必须与文件名一致**，且体现方向：UpInf 侧 `<模块>UpInf_*`，LowInf 侧 `<模块>LowInf_*`。
4. 结构化接口体命名：`STRUCT_APP_KEY_UPINF`（大写下划线）对应文件 `App_KeyUpInf.h`。
5. 函数指针宏别名（如 `DIO_INF1_WRITE_PIN`）必须定义在 **UpInf 头**内，供上层用语义宏调用。
6. **禁止跨模块共用全局变量**。模块 A 的代码（`.c`）**不得 `extern` 模块 B 的全局变量**，无论同层还是跨层——
   读写 B 的状态必须走 B 的 **UpInf 暴露的 `Get*` / `Set*` 接口**。
   全局变量是自己的实现细节，`extern` 别人等于绕过 UpInf 直接抓内部状态，换实现/加桩立刻断链。

   ```c
   /* ✗ 反例：L1_APP 直接抓 L4_Service 的全局量 */
   extern uint32_t SrvCan_RecvCounter;              /* App_PowerHsm.c */
   if (SrvCan_RecvCounter > 0) { ... }

   /* ✓ 正例：Service_CanComm 在 UpInf 暴露取值接口 */
   /* Service_CanCommUpInf.h */
   STRUCT_SERVICE_CANCOMM_UPINF {
       uint32_t (*GetRecvCounter)(void);
   };
   extern STRUCT_SERVICE_CANCOMM_UPINF Service_CanCommUpInf;
   /* 调用方 */
   if (Service_CanCommUpInf.GetRecvCounter() > 0) { ... }
   ```

   例外（不报）：① 变量本身就在**公共层 `L6_Public/`** 且经该层头文件正式声明（如 `Public_DataTypes.h` 的 `gCDC_CarType`）——
   公共层本身就是共享面；② 同一模块目录内的 `.c` 之间 `extern` 内部变量（属模块内聚，非跨模块）。

7. **别的模块要用本模块的能力，只能走本模块 UpInf；不得走"中间层"**。「中间层」= 模块的**核心层/实现层**，包括：
   ① 核心实现头（`Xxx.h`）里声明的实现函数（如 `Service_DebugLog.h` 的 `Service_DebugLog_LogById`）；
   ② **裸函数原型**——`extern <返回类型> <模块函数>(...);` 后直接调用（既没 include 对方 UpInf 头，也不经函数指针表）；
   ③ 绕过接口表的裸宏。
   唯一合法调用面 = `Xxx_UpInf.FuncName(...)`（函数指针表），或 UpInf 头里展开成表调用的语法糖宏。

   ```c
   /* ✗ 反例1：L4 直接 extern 裸原型调 L2 的函数（Service_SocCommLowInf.c:223/242） */
   extern uint8_t App_Power_GetPwrHsmState(void);
   pwmtemp = App_Power_GetPwrHsmState();        /* 绕过 App_Power_UpInf 表 */

   /* ✗ 反例2：模块实现头被外部直调 */
   #include "Service_DebugLog.h"                 /* 核心层实现头，非 UpInf 头 */
   Service_DebugLog_LogById(&tbl, id, __FILE__, __LINE__, x);   /* 绕过 Service_DebugUpInf */

   /* ✓ 正例：经目标模块 UpInf 表 */
   #include "App_PowerUpInf.h"
   pwmtemp = App_Power_UpInf.AppPower_UpInf_GetPwrHsmState();
   ```

   例外（不报）：① 调用方与目标**同一模块目录**内的 `.c` 互调（模块内聚）；
   ② 目标模块**尚无 UpInf 表**且本次首次引入（首笔提交须同时建表，后续 diff 按 N-12 严查）；
   ③ 已显式注记的平台级反向引用例外（如 `EcuAL_SpiLowInf.c` → `Service_SocCommUpInf`）。

8. **接口表一律用函数指针 struct 承载**，实例名 `<模块>_UpInf`（或 `<模块>UpInf`），注册时用
   **指定初始化器 `.成员 = 函数`**（顺序无关、加槽不改调用方）。
   - 类型命名两派并存，**新代码优先 `_t` 后缀**：`Service_SocCommUpInf_t`（7255 新式）、
     `EcuAL_SpiUpInf_t`（7255 新式）；存量 `STRUCT_XXX_UPINF`（`Service_Board_UpInf`、
     `STRUCT_SRV_BOARD_UPINF`）与 `STRUCT_APP_KEY_UPINF` 按 §二 硬规则 4 保留，**不算违规**。
   - 实例名：`Service_SocCommUpInf_t Service_SocCommUpInf;`、`EcuAL_SpiUpInf_t EcuAL_SpiUpInf;`。

   ```c
   /* XxxUpInf.h */
   typedef struct {
       void    (*Init)(void);
       void    (*MainFunction)(void);
       bool    (*PushRxData)(uint8_t id, uint8_t* data, uint8_t num);
   } Service_SocCommUpInf_t;
   extern Service_SocCommUpInf_t Service_SocCommUpInf;

   /* XxxUpInf.c —— 指定初始化器，禁按位置顺序裸填 */
   Service_SocCommUpInf_t Service_SocCommUpInf =
   {
       .SocCommUpInf_Init = Service_SocCommUpInf_Init,
       .MainFunction      = Service_SocCommUpInf_MainFunction,
       .PushRxData        = Service_SocCommUpInf_PushRxData,
   };
   ```

9. **配置与实现分离**：模块的配置数据（静态分配的缓冲、队列、上下文、参数表）放
   `Xxx_Cfg.c/.h`，与实现文件 `Xxx.c` 分开；**实时性敏感**的配置数据须放 `.dtcm_data` 段
   （`__attribute__((section(".dtcm_data")))`，工程已有宏别名 `DTCM_DATA_SECTION`，
   定义在 `L6_Public/Public_DataTypes.h:28-29`）。
   - 正例：`Service_CommTp_Cfg.c` 静态分配 `RxQueueData`/`TxQueueData`/`RxPduBuffer`
     （均 `.dtcm_data` 段）+ `RxFrameQueue`/`TxFrameQueue`/`ReassemblyContext`/`CommTp_Config`；
     `EcuAL_UartCfg.c` 承载 `UartChannelConfig[]` 通道表；`EcuAL_Uart.c` 控制块
     `EcuAL_UartCtrl` 亦在 `.dtcm_data` 段。
   - 反例：在 `Xxx.c` 实现文件里就地 `static` 定义大块缓冲/队列（与实现耦合、无法按产品裁剪）。

10. **EcuAL 模块三层链必须完整：`XxxUpInf`（对外）→ `Xxx.c`（核心）→ `XxxLowInf`（向下）**。
    模块只要封装 RTD（或其它下层驱动），就必须建 LowInf 层，且：
    ① **LowInf 是唯一允许 include RTD 驱动头、直调 RTD API 的层**
       （`IntCtrl_Ip_*` / `Siul2_*` / `Lpuart_*` / `Adc_Sar_*` / `Emios_*` 等）；
    ② **核心层 `Xxx.c` 只 include 本模块 `XxxLowInf.h`，判空转发**，不得直调 RTD；
    ③ **UpInf 表成员必须是 `XxxUpInf.c` 内的 `static` 包装函数**（命名 `<模块>UpInf_*`），
       包装函数再调核心层；不得在表里直挂核心层函数，也不跨过核心层直连 LowInf
       （照 `Service_SocCommUpInf` 用户裁定 2026-10-05；存量直挂旧表不追溯，新增/改动的表按此）。
    - 反例（2026-11-05）：`EcuAL_Interrupt` 初版只有 UpInf + 核心两层，核心直接
      `IntCtrl_Ip_Init` / `Siul2_Icu_Ip_*`，UpInf 表直挂核心；已补
      `EcuAL_InterruptLowInf.c/.h`，并把表成员改为 `EcuAL_InterruptUpInf_*` static 包装。
    - 存量例外（不追溯）：`EcuAL_GPIO`（Dio 视野，核心直调 `Siul2_Dio_Ip_*`，无 LowInf）、
      `EcuAL_PIT`（单层 1ms 时基，直调 RTD）。新增代码不得再以它们为由跳过 LowInf。

### 证据（6125）

- `EcuAL_Port/EcuAL_PortUpInf.h`：`STRUCT_ECUAL_PORT_UPINF` + `extern EcuAL_Port_UpInf`，含 `EcuAL_DioUpInf_WritePin1` 等，并在头尾给 `DIO_INF1_WRITE_PIN` 宏别名。
- `App_Key/App_KeyUpInf.h`：`STRUCT_APP_KEY_UPINF` + `App_Key_UpInf`，函数 `App_KeyUpInf_Init/Deinit/MainFunction`。

---

## 三、命名规范

### 3.1 文件命名

| 类型 | 规则 | 正例 | 反例 |
|------|------|------|------|
| 模块主文件 | `<层前缀>_<模块名>.c/.h` | `EcuAL_Pwm.c` `Service_Board.c` `App_Power.c` | `pwm.c` `board.c` `power.c` |
| UpInf | `<模块名>UpInf.c/.h` | `EcuAL_PwmUpInf.h` | `EcuAL_Pwm_UpInf.h` `pwm_up.h` |
| LowInf | `<模块名>LowInf.c/.h` | `EcuAL_PwmLowInf.c` | `EcuAL_PwmLow.c` |
| 配置 | `<模块名>_Cfg.c/.h`（`Service_CommTp_Cfg.*`、`EcuAL_GPIO_Cfg.*`）或 `<模块名>Cfg.c/.h`（`EcuAL_UartCfg.*` 7255 现状，两者并存、同模块内一致） | `Service_CommTp_Cfg.c` `EcuAL_GPIO_Cfg.c` | `cfg_pwm.c` |
| 任务 | `Task_<名>.c/.h` + `Inf`/`Event`/`Msg` 后缀 | `Task_PowerMsg.c` | `powerTask.c` |
| 头文件保护 | `_<大写下划线>_H` | `_ECUAL_PORT_UPINF_H` | `ECUAL_PORT_H`（缺下划线） |

### 3.2 函数命名

- 前缀 = 模块名（大驼峰），分隔用下划线：`EcuAL_PwmUpInf_SetPeriod()`。
- 方向词：`Init` / `Deinit` / `MainFunction` / `Set*` / `Get*` / `Is*`。
- 内部函数加 `loc_` / `static`：`loc_GpioPinConfig[]`（7255 现状）。
- **禁止**无前缀裸函数名（`init()` `writePin()`）。
- **跨层通知**：底层上报给上层的事件回调，一律以 `xxxNotification` 结尾 —— `EcuAL_Spi_TransmitFinishNotification` / `EcuAL_Uart_ErrorNotification` / `EcuAL_Spi_MRQNotification`。**禁**用 `_Callback` / `_Handler` / `_Indication` / `_IRQ` 等另起名。
- **数据搬运对偶**：一进一出两个方向成对命名 —— `PushRxData`（数据**向下流入**底层）/ `PullTxData`（上层**向上取走**）。**每层同名直传**：各层只换模块前缀、语义名不变（`CommTp_PushRxData` → `Service_SocCommUpInf_PushRxData` → `EcuAL_SpiLowInf_PushRxData`），**禁**二次命名（`RxDataIn` / `WriteRxBuf` / `GetTxFrame` 等自创名）。
- **注意（勿改）**：`EcuAL_PwmUnInf_SetPwmPeriod`（UnInf 少 p）是已知真实拼写，属历史遗留，**不作为本次规范问题上报**。

### 3.3 变量命名

| 类型 | 规则 | 正例 |
|------|------|------|
| 局部 | 小驼峰或下划线 | `pinIndex` `uart_channel` |
| 全局/静态 | `g_` 或 `loc_` 前缀（按工程现状） | `loc_GpioPinConfig` |
| **类型别名** | **`<模块前缀>_<语义>_t`** | `CommTp_FrameQueue_t` `Service_SocComm_SendInfo_t` `EcuAL_UartBuffer_t` |
| **配置宏 / 常量宏** | **`<模块前缀>_` + 全大写下划线** | `SERVICE_COMMTP_MAX_FRAME_LEN` `ECUAL_UART_BAUDRATE_115200` |
| **枚举值** | **全大写下划线**（带模块/语义前缀） | `COMMTP_RECEIVE_IDLE` `SPI_STATUS_IDLE` |
| **结构体成员** | **小写下划线（统一下划线式）** | `head` `tail` `is_full` `pdu_len` `expected_sn` `is_first_frame_received` |
| **指针变量** | **加 `p` 前缀** | `pRxFrameQueue[SERVICE_COMMTP_CHANNEL_NUM]` `pSendInfo` |
| **接口表类型** | **`<模块>UpInf_t`（新代码优先 `_t`）** | `Service_SocCommUpInf_t` `EcuAL_SpiUpInf_t`（存量 `STRUCT_XXX_UPINF` 合法） |
| **接口表实例** | **`<模块>_UpInf`** | `Service_SocCommUpInf` `EcuAL_SpiUpInf` `Service_Board_UpInf` |
| 枚举类型名 | `r_<模块>_FuncName`（7255 现状） | `r_gpio_FuncName` |

- **MISRA 相关**：`stdint.h` 定长类型；禁用 `int/char/short/long` 裸类型（`PlatformTypes.h` 的 `uint8/uint16/boolean` 属工程约定，允许）。
- 禁止魔法数字，需定义宏。

---

## 四、检查规则表（无独立脚本，由 agent 依据本表逐条判定）

| Rule ID | 名称 | 层 | 严重度 | 机器可判 | 检查方法 |
|---------|------|----|--------|----------|----------|
| N-01 | 文件命名前缀与所在层一致 | 全部 | warn | 是 | 新增/改名文件路径层 vs 文件名前缀 |
| N-02 | UpInf/LowInf 文件命名成对 | App/Service/EcuAL | warn | 是 | `Xxx.c` 存在则 `XxxUpInf.*` 应存在 |
| N-03 | 函数名前缀 = 模块名 | 全部 | warn | 是 | diff 新增函数定义名 vs 文件名 |
| N-04 | 跨层 include 只允许 UpInf | 全部 | error | 是 | diff 中 `#include` 下层路径非 UpInf → 报错 |
| N-05 | 层归属语义一致 | App/Service/EcuAL | warn | 半 | 业务词出现在 EcuAL / 硬件编号出现在 App → 报警 |
| N-06 | 头文件保护宏规范 | 全部 | info | 是 | 新 .h 缺 `#ifndef _<大写下划线>_H`（如 `_SERVICE_DEBUGLOG_H`）；`__XXX_H__` / `XXX_H_` 两种写法均不合规，与 §3.1 同名行一致 |
| N-07 | 无裸类型 / 有 stdint | 全部 | info | 是 | 新增 `int`/`char` 声明 |
| N-08 | 新模块必须有 UpInf（对外接口） | App/Service/EcuAL | warn | 是 | 新模块目录无 `*UpInf.*` |
| N-09 | commit 消息格式合规 | - | error | 是 | 首行 `[type][JIRA]中文标题` + what/why/how/影响等级/建议测试范围 |
| N-10 | 生成物改动须与 test_prj.mex 同步 | - | error | 是 | diff 命中 `generate/` `board/` 时必须同时有 `test_prj.mex` 对应改动；只改生成物不改 mex → 报错（`Debug_FLASH/` 仍禁改） |
| N-11 | 禁止跨模块 extern 全局变量 | 全部 | error | 是 | diff 新增 `extern <类型> <变量>;` 且变量定义在**其它模块** → 报错，改用对方 UpInf 的 Get/Set |
| N-12 | 跨模块调用只许走对方 UpInf（禁中间层） | 全部 | error | 是 | diff 新增 `extern <类型> <模块函数>(...);` 裸原型调用、或 include 对方实现头（`Xxx.h`，非 `XxxUpInf.h`）后直调 `Xxx_*` 函数 → 报错，改用 `Xxx_UpInf.Func()` |
| N-13 | 标识符命名合规（枚举值/类型/宏/成员/指针） | 全部 | warn | 是 | 见下「N-13 子规则」，任一命中即报警 |
| N-14 | 跨层通知与数据搬运命名 | 全部 | warn | 是 | 见下「N-14 子规则」，任一命中即报警 |
| N-15 | 接口表 struct + 三件套文件 + 配置实现分离 | App/Service/EcuAL | warn | 是 | 见下「N-15 子规则」，任一命中即报警 |
| N-16 | 分层单向依赖 / 层间解耦 / 跨模块内部访问 | 全部 | warn | 是 | 见下「N-16 子规则」，任一命中即报警 |
| N-17 | SOC 通信发送统一走 SendCmd（禁手工传通道） | L1_APP | error | 是 | 见下「N-17 子规则」，任一命中即报错 |
| N-18 | cmd 号唯一真源（清单+枚举生成，禁硬编码 #define） | L1_APP | warn | 是 | 见下「N-18 子规则」，任一命中即报警 |
| N-19 | EcuAL 模块三层链完整（UpInf → 核心 → LowInf） | L5_EcuAL | error | 是 | 见下「N-19 子规则」，任一命中即报错 |

**severity 语义**：`error` 必须改（阻断提交）；`warn` 建议改；`info` 仅提示。

### 反例/正例

- N-04 反例：`L1_APP/App_Power/App_Power.c` 里 `#include "EcuAL_Uart.h"` → 应为 `EcuAL_UartUpInf.h`。
- N-05 反例：`L5_EcuAL/` 下出现 `RedLight_On()` → 业务语义应在 App；`L1_APP/` 下出现 `gpio3_set()` → 硬件编号应在 EcuAL。
- N-10 反例：只改 `generate/src/*_PBcfg.c` / `board/Siul2_Port_Ip_Cfg.h` 而不改 `test_prj.mex` → Config Tools 重新生成时按 mex 旧配置覆盖。实例（2026-11-05）：PTC24/EIRQ19 + ICU ch19 + IntCtrl `SIUL_2` 只落在生成物，重新生成后回退成 GPIO、ICU 仅 ch25、IntCtrl 无 `SIUL_2`，心跳中断链整体失效。
- N-11 反例：`L1_APP/APP_Power/App_PowerHsm.c:49` 直接 `extern uint32_t SrvCan_RecvCounter;`（该量定义在 `L4_Service/Service_Canbus/Service_CanComm/Service_CanCommLowinf.c:29`）→ 属跨模块抓别人的全局变量，应改由 `Service_CanCommUpInf` 提供 `GetRecvCounter()` 取值。
- N-12 反例：`L4_Service/Service_SocComm/Service_SocCommLowInf.c:223` 写 `extern uint8_t App_Power_GetPwrHsmState(void);`、:242 直接调用 → 绕过 `App_Power_UpInf` 表抓 L2 函数，**连 include 都没写**（比 N-04 更隐蔽：N-04 查 include，N-12 查裸原型/直调）；正例见 §二 硬规则 7。

**N-04 与 N-12 的边界**：N-04 管 **include 谁**（跨层只许 `XxxUpInf.h`）；N-12 管 **怎么调**（不论 include 什么，跨模块调别人函数只能经对方 UpInf 表）。同一处违例可两条都报，也可只报更贴合的一条。

### N-13 子规则（标识符命名，逐条对照 diff 新增标识符）

| # | 对象 | 规则 | 正例 | 反例 |
|---|------|------|------|------|
| 1 | 枚举值 | 全大写下划线，带模块/语义前缀 | `COMMTP_RECEIVE_IDLE` `SPI_STATUS_IDLE` | `CommTpIdle` `spiIdle` |
| 2 | 类型别名 | `<模块前缀>_<语义>_t` | `CommTp_FrameQueue_t` `Service_SocComm_SendInfo_t` `EcuAL_UartBuffer_t` | `FrameQueue`（无 `_t`）`frame_queue_t`（无模块前缀） |
| 3 | 配置宏/常量宏 | `<模块前缀>_` + 全大写下划线 | `SERVICE_COMMTP_MAX_FRAME_LEN` `ECUAL_UART_BAUDRATE_115200` | `MAX_FRAME_LEN`（无模块前缀）`Service_Commtp_MaxFrameLen` |
| 4 | 结构体成员 | **小写下划线式**（禁小驼峰；`is_*` 前缀表布尔） | `head` `tail` `is_full` `pdu_len` `expected_sn` `is_first_frame_received` | `isFull`（小驼峰，应为 `is_full`）`PduLen`（大驼峰） |
| 5 | 指针变量 | 加 `p` 前缀 | `pRxFrameQueue[SERVICE_COMMTP_CHANNEL_NUM]` `pSendInfo` | `rxFrameQueue` `sendInfo` |

- 判据：diff **新增/改名**的标识符才对照；存量历史遗留（如 `EcuAL_GPIO.h:42` 枚举类型名 `r_gpio_FuncName`、`Service_CommTp.h` 存量成员 `isFull`）**不作为本次问题上报**，仅在新代码继续沿用错误风格时报警。
- 子规则 2 例外：**UpInf 接口体** `STRUCT_XXX_UPINF`（如 `STRUCT_ECUAL_PORT_UPINF` `STRUCT_APP_KEY_UPINF`）按 §二 硬规则 4 用大写下划线，**不套用 `_t` 后缀**；其 typedef 出的表变量仍叫 `Xxx_UpInf`（如 `EcuAL_Port_UpInf`）。
- 严重度 `warn`（建议改）；本表 5 项任一项在新代码中命中即产出一条 N-13 建议，`detail` 注明命中的子规则编号。

### N-14 子规则（跨层通知 / 数据搬运命名，对照 diff 新增函数）

| # | 对象 | 规则 | 正例 | 反例 |
|---|------|------|------|------|
| 1 | 跨层通知回调 | 以 `Notification` 结尾（底层上报上层） | `EcuAL_Spi_TransmitFinishNotification` `EcuAL_Spi_ErrorNotification` `EcuAL_Spi_MRQNotification` `EcuAL_Uart_RxNotification` | `..._TransmitFinishCallback` `..._ErrHandler` `..._TxIrq` |
| 2 | 数据搬运入向 | `PushRxData`（数据向下流入底层） | `CommTp_PushRxData` `Service_SocCommUpInf_PushRxData` `EcuAL_SpiLowInf_PushRxData` | `RxDataIn` `WriteRxBuf` `RecvFrame` |
| 3 | 数据搬运出向 | `PullTxData`（上层向上取走） | `CommTp_PullTxData` `Service_SocCommUpInf_PullTxData` `EcuAL_SpiLowInf_PullTxData` | `GetTxFrame` `FetchTxData` `TxDataOut` |
| 4 | 每层同名直传 | 同一条搬运链各层只换模块前缀，语义名**不换** | `CommTp_PushRxData` → `Service_SocCommUpInf_PushRxData` → `EcuAL_SpiLowInf_PushRxData` | 同一链上换个层改叫 `WriteRxBuf` / `RecvPdu` |

- 判据：diff **新增/改名**的**函数名**才对照；存量 `_Callback`（如 `App_PowerHsm.c:1970` `App_Power_WakeMsgJudge_Callback`、`Service_AsrNmUpInf.h:76` `SrcAsrNm_UpInf_WakeMsgJudge_Callback`、`Sys_Service.c:111` `IIC1_Master_Callback`）属**历史遗留，不上报**；但**跨层通知**语义的新函数必须用 `Notification`，不得新起 `_Callback`。
- **与 N-13 边界**：N-13 管标识符**构词**（大小写/前缀/后缀格式）；N-14 管**语义命名约定**（通知后缀、搬运对偶、逐层同名）。同一函数违规可两条都报。
- 严重度 `warn`（建议改）；`detail` 注明命中的子规则编号。

### N-15 子规则（接口表 struct / 三件套 / 配置分离，对照 diff 新增文件与新增接口体）

| # | 对象 | 规则 | 正例 | 反例 |
|---|------|------|------|------|
| 1 | 层间接口表 | 必须是**函数指针 struct**（非散落函数原型集合） | `Service_SocCommUpInf_t` `EcuAL_SpiUpInf_t` | UpInf 头里只丢一堆裸函数原型、无表实例 |
| 2 | 表实例注册 | **指定初始化器 `.成员 = 函数`**，禁按位置顺序裸填 | `EcuAL_SpiUpInf = { .Init = EcuAL_Spi_Init, .DeInit = EcuAL_Spi_DeInit }` | `EcuAL_SpiUpInf = { EcuAL_Spi_Init, EcuAL_Spi_DeInit }`（加槽即错位） |
| 3 | 接口文件名三件套 | `Xxx.h`(实现) + `XxxUpInf.h/.c`(向上表) + `XxxLowInf.h/.c`(向下调) 固定成对 | `EcuAL_Spi.h` / `EcuAL_SpiUpInf.*` / `EcuAL_SpiLowInf.*` | `EcuAL_Spi_Up.h`（下划线分隔）、只有 `XxxUpInf.h` 无 `.c` |
| 4 | 配置与实现分离 | 配置数据（静态缓冲/队列/上下文/参数表）落 `Xxx_Cfg.c/.h`，不混进 `Xxx.c` | `Service_CommTp_Cfg.c` 放队列与上下文、`EcuAL_UartCfg.c` 放通道表 | 在 `Xxx.c` 里就地 `static` 定义大块队列/缓冲 |
| 5 | 实时数据段放置 | 实时性敏感配置数据须 `.dtcm_data` 段 | `__attribute__((section(".dtcm_data"))) QueueData_t RxQueueData[...]`；SOC 通信**子命令表**（`AppRxSub_*`/`AppTxSub_*`，TX 表含 `TxInfo.TxStatus` 被 `TxProcessFuc` 每 10ms 周期读+写，对齐 6125 YB103） | 敏感队列放普通 `.bss`（访问慢、易被搬走）；子命令表漏 `.dtcm_data` |

- 判据：对照 **diff 新增的模块/文件/接口体**；存量 `STRUCT_XXX_UPINF`（`STRUCT_SRV_BOARD_UPINF`、`STRUCT_APP_KEY_UPINF`、`STRUCT_ECUAL_PWM_UPINF`）按 §二 硬规则 4 属合法旧式，**不上报**；`EcuAL_Uart` 的 `STRUCT_EcuAL_UARTUp_INF_t`/`STRUCT_EcuAL_UART_INF_t` 亦为存量。
- 子规则 5 与子规则 4 常同现：新增队列若在 `_Cfg.c` 且未加 `.dtcm_data`，可两条都报。
- 与 N-02 边界：N-02 只查 `XxxUpInf.*` **是否存在**（成对性）；N-15 查三件套**命名/结构/职责**是否合规。
- 严重度 `warn`（建议改）；`detail` 注明命中的子规则编号。

### N-16 子规则（分层单向依赖 / 层间解耦 / 跨模块内部访问）

对照 **diff 新增的 include / 调用 / 函数定义 / 数据访问**：

| # | 对象 | 规则 | 正例 | 反例 |
|---|------|------|------|------|
| 1 | 层间依赖方向 | 严格单向 `L1_APP → L2_Tasks → L3_RTOS → L4_Service → L5_EcuAL → RTD`；`L6_Public` 被各层引用、不参与方向 | 上层 include 下层 UpInf 头 | 反向依赖（L4→L3、L4→L2）或跨层直呼 |
| 2 | Task 层访问 RTOS | 只能经 `Tasks_LowInf` 表；**不得直调 FreeRTOS / 裸机 API** | `Tasks_LowInf.Os_GetSysTickCount()` | 非 `L2_Tasks` 层 include `FreeRTOS.h`/`task.h` 或直调 `vTask*`/`xQueue*`/Os2 裸机 API |
| 3 | 层间解耦 | 上层经 **LowInf** 调下层；下层经 **UpInf** 回调上层 | 上层 `XxxLowInf` 转发 → 下层 UpInf 表；下层走己方 UpInf 注册回调 | 下层反向 include 上层实现头后直调 |
| 4 | 跨模块内部数据 | 模块内部数据只经**公有 API** 访问，禁直接操作内部结构 | `CommTp_ReceiveAndUnpack()` 等公有 API | 经 Service_SocComm 直接操作 CommTp 队列 `queue->head` / `queue->tail` |
| 5 | 模块内部函数 | 非公有 API 的内部函数一律 `static` | `CommTp_PackSingleFrame` `CommTp_UnpackFirstFrame` `CommTp_FrameQueue_Enqueue`/`Dequeue` | 内部实现函数无 `static`（导出成全局符号，可被外部绕过公有 API 直调） |
| 6 | 反向引用例外 | 确有必要的反向引用，**须在文件头显式注记为例外** | `EcuAL_SpiLowInf.c:21-31` 头注释注记 L5→L4 例外（`Service_SocCommUpInf.h` 数据上行桥接） | 反向 include / extern 无任何例外注记 |

- 子规则 2 边界：`L2_Tasks/Tasks.c` 内 include `FreeRTOS.h`/`task.h` 属 **OS 绑定层职责内**的实现细节（转发分支 `MCU_SCHED_TYPE` 内使用），**不报**；报警对象是 `L1_APP`/`L4_Service`/`L5_EcuAL` 等层直调 OS API。
- 子规则 5 与 N-08 边界：N-08 查新模块**有没有** UpInf；N-16 子规则 5 查模块**内部函数是否收敛为 static**。
- 与 N-04 / N-12 边界：N-04 管 include 谁、N-12 管跨模块怎么调；N-16 管**层间方向**与**模块内部封装**，同一处违例可多条并报，也可只报最贴合的一条。
- **存量偏差（列为待整改清单，只约束今后新增，不强制本次修）**：
  - `L4_Service/Service_Debug/Service_DebugLog.c:3` → `#include "..\..\L2_Tasks\Tasks.h"`（L4→L2 反向）
  - `L4_Service/Service_SocComm/Service_SocComm.c:28` → `#include "..\..\L3_RTOS\OS1_FreeRTOS\Os1_UpInf\OsIf_Task.h"`（L4→L3 反向）
  - `L3_RTOS/OS2_TmrSched/Os2_UpInf/Os2If_UpInf.c:24` → `#include "Timer_Counter.h"`（L3→L4 反向）
  - L4 各文件大面积 `Tasks_LowInf.Os_DelayMs(...)`（`Service_Board.c`、`Service_DebugLog.c`、`Sys_Service.c` 等，L4→L2 表调用）
- 严重度 `warn`（建议改）；`detail` 注明命中的子规则编号。

### N-17 子规则（SOC 通信发送入口统一，对照 diff 新增调用）

**架构前提（7255 用户裁定 2026-09-30）**：
1. **一 cmd 一通道**：同一 cmd 只登记在一个通道的 TX 表（`AppTxCmdProcess[]` 下标 = 通道号）；
2. **单通道装配**：`App_SocComm_Config.ChannelNum=1u`（CH0=UART），`SERVICE_SOCCOMM_CHANNEL_NUM=2u` 仅为数组上限；
3. **IVI/IC 分发由 SOC 侧负责**（SOC IC 收到后转发 IVI），MCU 无双通道双发需求（6125 时代 IVI=CH0/IC=CH1 双发的写法已废弃）。

在此前提下 **SendCmd 全场景适用**（含 echo 应答：来源通道 = 归属通道恒成立）。

| # | 对象 | 规则 | 正例 | 反例 |
|---|------|------|------|------|
| 1 | 业务发送入口 | 只允许 `MCU_SOC_*_CMD_Send*()` 封装函数或 `App_SocComLowInf_SendCmd(cmd,TxCtl)`，通道由 TX 表反查（`App_SocComStrCfg_FindTxCmd`） | `MCU_SOC_0X8101_CMD_SendMuteState()`；`(void)App_SocComLowInf_SendCmd(MCU_SOC_0X8FFF_CMD, ...)` | `MCU_SOC_0X8101_CMD_Fun(PDUR_COM_CHANNEL_0, cmd, ctl)` 业务代码直调 `_Fun` 传通道 |
| 2 | cmd↔通道绑定唯一真源 | 只在 `App_SocComStrCfg_*` 的 TX 表定义；调用点禁出现发送通道字面量 | `TX_SUBCMD_STRUCT(MCU_SOC_0X8005_CMD, ...)` 登记 | 业务调用处写 `PDUR_COM_CHANNEL_x` 作发送通道（握手/心跳等**非 cmd 接口**除外） |
| 3 | echo/应答路径 | RX 回调内同样走 SendCmd 查表回发 | `SOC_MCU_0x0FFF_CMD_Fun` 内 `(void)App_SocComLowInf_SendCmd(MCU_SOC_0X8FFF_CMD, ...)` | RX 回调内 `MCU_SOC_0X8FFF_CMD_Fun(channel, ...)` 直调下传收帧通道 |

**例外（不报）**：
- `_Fun` 系列（`MCU_SOC_*_CMD_Fun` / `SOC_MCU_*_CMD_Fun`）的**形参 channel 本身**——签名由 L4 `TxSubCmdFunc_t`/`RxSubCmdFunc` 函数指针类型锁定（`Service_SocComm_Types.h`），且 6125 移植约定"签名逐字一致"，形参保留、由框架/SendCmd 填充；
- `Service_SocComm.c` 内部框架调度（`TxProcessFuc` 周期/ACK 重发带 channel 回调）属 L4 职责；
- 非 cmd 类接口（`SetHandshake`/心跳监视等）直接使用 `PDUR_COM_CHANNEL_x`。

- 判据：diff **新增的调用语句**；存量已收敛（141 行 echo 已改 SendCmd，PowerHsm 双发已收敛）。
- 严重度 `error`（用户裁定"必须经过封装"，阻断提交）；`detail` 注明命中的子规则编号。

### N-18 子规则（cmd 号唯一真源：清单 + 枚举生成，2026-10-01 用户裁定）

**机制**：7255 的 cmd 常量由 X-macro **清单**经**枚举**生成（`App_SocComSysCmd.h`）：清单 `RX_LIST_CH0/CH1`、`TX_LIST_CH0/CH1` 是 cmd 号的**唯一真源**，
`RX_ENUM_ENTRY`/`TX_ENUM_ENTRY` 展开成 `enum { name = val, ... }`。
未登记的名字**不存在** → 调用点 `App_SocComUpInf.SendCmd(名, ...)` 编译期直接报 `undeclared identifier`，
而非拖到运行期查表打 `SOC_WARN_TX_NOT_REG`。`App_SocComStrCfg_7255.c` 的 `DupCheck`（`switch(0u){ case 名: ... }`）另做编译期重复值查重。

对照 **diff 新增/改动的 cmd 常量、清单条目、命令装配与调用点**：

| # | 对象 | 规则 | 正例 | 反例 |
|---|------|------|------|------|
| 1 | cmd 常量定义 | 只由清单枚举生成，**禁**再写 `#define <cmd名> <值>`（同值两处 = 真源分裂） | 清单加行 `X(MCU_SOC_0X8101_CMD, 0x8101u, ...)` | `#define MCU_SOC_0X8101_CMD 0x8101u` |
| 2 | 新增命令落点 | 只改两处：① 清单加一行（枚举随清单自动生成）；② `App_SocComSysCmd.c` 实现 `<名>_Fun` | 清单 + `MCU_SOC_0X8101_CMD_Fun` | 另在 .h/.c 补 `#define`（第三处真源） |
| 3 | 调用点用名不用数 | 业务发送必须写**清单名**，禁裸数值——裸数值绕过编译期检查（枚举靠"名字不存在"拦截） | `App_SocComUpInf.SendCmd(MCU_SOC_0X8101_CMD, ...)` | `App_SocComUpInf.SendCmd(0x8101u, ...)` |
| 4 | 清单条目签名 | RX：`X(名, 值)`；TX：`X(名, 值, txType, ack, cyc, status, seccomflag)`——属性须写全，勿漏项 | `X(MCU_SOC_0X8FFF_CMD, 0x8FFFu, FRAME_TYPE_IMMEDIATELY, ACK_NO, APP_SOCCOM_TX_CYC_2S, APP_SOCCOM_TX_STATUS_IDLE, APP_SOCCOM_SEC_COM_OFF)` | 沿用旧签名 `X(名, txType, ...)`（缺数值，枚举生成不了） |

**例外/边界（不报）**：
- `App_SocComSysCmd.h` 内 `RX_ENUM_ENTRY`/`TX_ENUM_ENTRY` 等**清单展开宏自身**的 `#define` 不属"硬编码 cmd"；
- 非 cmd 类常量宏（`APP_SOCCOMM_ECHO_PARAM_MAX_LEN` 等）照旧 `#define`；
- 原 `MCU_SOC_0X*_CMD_H` 高字节宏已随本机制删除；高字节改由组表条目 `cmd_h = (uint8_t)((cmd) >> 8u)` 现算，新增代码**禁**再引入 `_CMD_H` 宏。

**已知拦不住的一处（明确记录，不算违规）**：`App_SocComUpInf.SendCmd` 是**函数指针**调用，`cmd` 为普通 `uint16_t` 入参，C 语言无编译期可检查语法位置——
故本机制只拦**名字**，`SendCmd(0x9999u, ...)` 这类**裸数值**绕不过（子规则 3 是人工/agent 判据，非编译器保证）。
若要连裸数值也编译期拦截，须改用宏入口 + 负长度数组断言（`sizeof(char[cond?1:-1])`），但那要求 SendCmd 不再挂函数指针表，与 §二 UpInf 接口表约定冲突，**未采纳**。

- 判据：diff **新增/改动的 cmd 相关行**；存量已收敛（11 个硬编码 `#define` 已删，清单上移 `App_SocComSysCmd.h`）。
- 严重度 `warn`（建议改，不阻断提交）；`detail` 注明命中的子规则编号。

### N-19 子规则（EcuAL 模块三层链完整，对照 diff 新增/改动的 L5 模块文件）

EcuAL 模块封装 RTD 时必须三层齐全：`XxxUpInf.*`（对外表）→ `Xxx.c/.h`（核心）→ `XxxLowInf.*`（向下适配）。

| # | 对象 | 规则 | 正例 | 反例 |
|---|------|------|------|------|
| 1 | LowInf 存在性 | 核心层调 RTD 的模块必须有 `XxxLowInf.c/.h` | `EcuAL_McuLowInf.*` `EcuAL_PortLowInf.*` `EcuAL_InterruptLowInf.*` | 只有 `Xxx.c` + `XxxUpInf.*`，核心直接包 RTD |
| 2 | RTD 调用落点 | RTD 驱动头 include 与 API 调用只允许出现在 `XxxLowInf.c` | `EcuAL_InterruptLowInf.c` 调 `IntCtrl_Ip_Init` / `Siul2_Icu_Ip_*` | `EcuAL_Interrupt.c` 里直接 `#include "IntCtrl_Ip.h"` 并调用 |
| 3 | 核心层职责 | 核心 `Xxx.c` 只 include `XxxLowInf.h`，判空/直接转发 | `EcuAL_Interrupt.c` → `EcuAL_Interrupt_LowInf.EalInterrupt_LowInf_*()` | 核心层把 RTD 调用与业务逻辑混写 |
| 4 | UpInf 表接线 | 表成员由 `XxxUpInf.c` 内 `static` 包装函数（`<模块>UpInf_*`）注册，包装函数再调核心层；不直挂核心函数、不跨层直连 LowInf | `EcuAL_InterruptUpInf.c` 的 `.Init = EcuAL_InterruptUpInf_Init`（static → `EcuAL_Interrupt_Init`） | `.Init = EcuAL_Interrupt_Init`（直挂核心）或 `.Init = EcuAL_InterruptLowInf_Init`（跨层） |

- 判据：对照 **diff 新增/改动的 L5 模块 .c/.h**；检查核心层 .c 是否出现 RTD 驱动头 include 或 RTD API 调用，以及 UpInf 表成员名是否为 `<模块>UpInf_*` 包装。
- 存量例外（不追溯）：`EcuAL_GPIO`（Dio 视野，核心直调 `Siul2_Dio_Ip_*`）、`EcuAL_PIT`（单层时基，直调 RTD）；已直挂核心的旧表（`EcuAL_Port` / `EcuAL_Mcu`）不追溯。新增模块/文件及改动的接口表不得引用这些例外。
- 与 N-15 边界：N-15 查三件套**文件命名/存在性**；N-19 查**调用链职责**（RTD 只出现在 LowInf、核心不得直调）。
- 严重度 `error`（用户裁定 2026-11-05：分层缺失会重复出现，阻断提交）；`detail` 注明命中的子规则编号。

---

## 五、流程约束（供 agent 与 HTML 使用）

1. **agent 分析基准**：规范分析在 **analyze 阶段**做（与生成 tasks.json 同批，读同一份 diff），
   agent 用 `git diff HEAD -- <变更所在目录>`，结果写 `$OUTPUT/norm_analysis.json`
   （`files` 仅记录分析覆盖范围，不参与校验；analyze 后用户改文件无需重新分析）。
2. **execute 入口硬门禁**（两道，任一不过 `[ERROR]` 直接退出，HTML 都不生成）：
   - **结构**：norm_analysis.json 缺失/空/损坏/缺 `suggestions` 键 → 提示重跑 analyze；
     空 `suggestions: []` 合法（无违规）
   - **人工确认完成**：每条 suggestion 的 `status` 必须为 `checked`；有未确认（`open`）→
     报出未确认 ID 并退出。校验通过 → 分析结果**只读内嵌** commit_report.html（**无服务**）。
3. **建议三态由人工推进**：`open`（analyze 生成）→ 人工处理：认可就按建议改代码后把
   `status` 改为 `checked`；认为建议不对则**从数组删除该条**（删了就不算违规），
   并跑 **`/jira-commit norm`** 交互同步更新规范三件套（norm_spec.md / 相关 CLAUDE.md / memory）。
   **norm_analysis.json 是唯一状态源**，由**人工编辑**，页面与脚本都**不写回**。
4. **门禁**：execute 前必须全部 `checked`（或建议已删空），否则 generate_report 拒绝执行。
5. **写评论**：手动——页面「一键复制」分析结果（按点分条）→
   「打开本分支提交列表」（GitLab `/-/commits/<分支>`，支持 ref；`/-/commit/<id>` 只接受 SHA，传分支名會 404。push 后列表顶端即本次合并 commit）→ 点进顶端 commit 粘贴为评论。
