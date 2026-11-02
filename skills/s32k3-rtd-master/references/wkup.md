# WKPU（低功耗唤醒单元） — S32K344 RTD 0.9.0 实战教学

> 源工程: D:\wnagjin\S32K3_mydetail\详细教学(1)\详细教学\S32K3 Training-RTD\S32DSv3p4_RTDv090\S32K344_Wkup_Lab_090_34
> 源文件: D:\wnagjin\S32K3_mydetail\详细教学(1)\详细教学\S32K3 Training-RTD\S32DSv3p4_RTDv090\S32K344_Wkup_Lab_090_34\src\main.c（代码原样摘录，未经任何修改）

## 1. 外设概述

WKPU（Wakeup Unit）是 S32K3 在低功耗模式下仍保持供电的唤醒管理单元，把外部引脚、LPCMP 模拟比较器、RTC 等唤醒源汇聚成中断/复位请求把 MCU 从 Standby 拉起来。RTD 0.9.0 中对应底层驱动 `Wkpu_Ip`（配置生成物挂在 Icu 命名空间下：`Wkpu_Ip_SA_BOARD_InitPeripherals_PBcfg.c`），本实验联合 `Power_Ip`（MC_ME/PMC 电源模式）、`Cmp_Ip`（LPCMP1 + 内部 DAC 1.65V 基准）、`Rtc_Ip`（API 定时触发 LPCMP）共同演示"进 Standby → 唤醒"全流程。

实验逻辑（摘自 ReadMe.md）：MCU 上电后 user LED 点亮；按 SW4(EVB)/SW3(WB) 关 LED 并进入 Standby；当 LPCMP1 通道 0/1/2（PTA0/PTA1/PTA2）输入电压大于 DAC 设定的 1.65V，或按 SW5(EVB)/SW2(WB)，MCU 自动唤醒，LED 重新点亮。

## 2. 初始化与使用时序

```mermaid
flowchart TD
    A[上电 / 复位] --> B[Power_Ip_InitPower<br/>电源 IP 初始化]
    B --> C[Clock_Ip_Init<br/>Mcu_aClockConfigPB_BOARD_BootClockRUN]
    C --> D[Siul2_Port_Ip_Init 引脚复用<br/>+ 点亮 user LED]
    D --> E{FastWkup_Config 判断<br/>MC_RGM DES ≠ 0 或 FES 外部复位?}
    E --|是·冷上电| F[Cmp_Ip_Init LPCMP1<br/>Rtc_Ip_Init + EnableInterrupt + StartTimer<br/>Wkpu_Ip_InitInterrupt 2通道<br/>Wkpu_Ip_EnableInterrupt CMP_RTC=2<br/>Wkpu_Ip_EnableInterrupt PTC20=47]
    E --|否·Standby唤醒返回| G[跳过·不重复配置]
    F --> H[主循环等待按键]
    G --> H
    H --> I{SW4/SW3 按下?}
    I --|否| H
    I --|是| J[关 LED·等待按键释放]
    J --> K[Clock_Ip_Init<br/>切换 standby 时钟配置]
    K --> L[DCM_GPR DCMRWF1<br/>清 STANDBY_IO_CONFIG_MASK]
    L --> M[WkupFlagClear<br/>RTC RTCS / LPCMP CSR·RRCSR·RRSR<br/>WKPU WISR·WISR_64 全部写1清零]
    M --> N[PMC_PrepareLowPowerEntry]
    N --> O[Power_Ip_SetMode<br/>aModeConfigPB[1] 进入 Standby]
    O --> P{唤醒事件<br/>PTA0/1/2 &gt; 1.65V 或 SW2/SW5}
    P --> Q[Fast Standby Exit<br/>DCMRWF5 指向 RAM 向量表]
    Q --> R[FastWkup_RAMInit<br/>清全部 SRAM → init_data_bss<br/>→ 重设 MSP]
    R --> S[重新调用 main<br/>LED 重新点亮]
```

关键点：**WKPU 的中断使能只在冷上电（破坏性/外部复位）时配置一次**（`FastWkup_Config` 内部判断 `MC_RGM->DES` / `MC_RGM->FES`）；从 Standby 唤醒走的是 DCMRWF5 指定的 RAM 向量表入口 `FastWkup_RAMInit`，清空 SRAM、重跑 `init_data_bss()` 后直接重入 `main()`，不走普通复位流程，也不会重复初始化 WKPU。

## 3. main.c 原样代码

源文件共 131 行，以下按逻辑段落分块摘录，与源文件逐字符一致。

```c
/* ===== src/main.c 第 1-40 行：文件头 + 头文件包含 ===== */
/*
*   (c) Copyright 2020 NXP
*
*   NXP Confidential. This software is owned or controlled by NXP and may only be used strictly
*   in accordance with the applicable license terms.  By expressly accepting
*   such terms or by downloading, installing, activating and/or otherwise using
*   the software, you are agreeing that you have read, and that you agree to
*   comply with and are bound by, such license terms.  If you do not agree to
*   be bound by the applicable license terms, then you may not retain,
*   install, activate or otherwise use the software.
*
*   This file contains sample code only. It is not part of the production code deliverables.
*/

/*!
**  @addtogroup main_module main module documentation
**  @{
*/
/* MODULE main */


/* Including necessary configuration files. */
#include "S32K344_SIRC.h" /*!< Device Configuration Module        */
#include "S32K344_FXOSC.h" /*!< Device Configuration Module        */
#include "S32K344_SXOSC.h" /*!< Device Configuration Module        */
#include "S32K344_DCM_GPR.h" /*!< Device Configuration Module        */
#include "S32K344_MC_RGM.h" /*!< Device Configuration Module        */
#include "S32K344_MC_CGM.h" /*!< Device Configuration Module        */
#include "S32K344_RTC.h" 	/*!< Device Configuration Module        */
#include "S32K344_FIRC.h"	 /*!< Device Configuration Module        */
#include "S32K344_LPCMP.h"
#include "Clock_Ip.h"         /*!< WKPU Driver                        */
#include "Siul2_Port_Ip.h"   /*!< SIUL2 Low Level Interface Driver   */
#include "Siul2_Dio_Ip.h"    /*!< Digital Input Output Driver        */
#include "Power_Ip_Private.h"/*!< POWER Driver (MC_RGM, MC_ME, PMC)  */
#include "Wkpu_Ip.h"         /*!< WKPU Driver                        */
#include "Rtc_Ip.h"
#include "Cmp_Ip.h"
#include "check_example.h"
#include "FastWkup.h"
```

```c
/* ===== src/main.c 第 41-62 行：WkupFlagClear 唤醒标志清除 ===== */


int main(void);
static void WkupFlagClear(void);

static void WkupFlagClear(void)
{
	uint32_t WkupFlag = 0;
	uint32_t CmpFlag = 0;
	uint32_t RTCAPIFlag = 0;

	RTCAPIFlag = RTC->RTCS;
	RTC->RTCS = RTCAPIFlag;
	CmpFlag = LPCMP_1->CSR;
	LPCMP_1->CSR = CmpFlag;
	LPCMP_1->RRCSR = 0x00000000; /* Pre-set to low state all channels. */
	LPCMP_1->RRSR = 0xFF; /* 7. Clear channel flags RRSR[RR_CHnF] */
	WkupFlag = WKPU->WISR;
	WKPU->WISR = WkupFlag;      /* Write 1 to Clear WKPU flag */
	WkupFlag = WKPU->WISR_64;
	WKPU->WISR_64 = WkupFlag;   /* Write 1 to Clear WKPU_64 flag */
}
```

```c
/* ===== src/main.c 第 63-85 行：main 初始化序列（电源/时钟/引脚/FastWkup 配置） ===== */

/*!
  \brief The main function for the project.
  \details The startup initialization sequence is the following:
 * - startup asm routine
 * - main()
*/
int main(void)
{
	Power_Ip_InitPower(&Power_Ip_HwIPsConfigPB);

	Clock_Ip_Init(&Mcu_aClockConfigPB_BOARD_BootClockRUN[0]);

	/* Pins configuration. Turn-on Green led */
	Siul2_Port_Ip_Init(NUM_OF_CONFIGURED_PINS0, g_pin_mux_InitConfigArr0);

#if (1 == S32K344_EVB)
	Siul2_Dio_Ip_WriteChannel(SIUL_INST, SIUL_EVB_GPDO_BLUE1, 1U);
#else
	Siul2_Dio_Ip_WriteChannel(SIUL_INST, SIUL_WB_GPDO_GREEN0, 1U);
#endif

	FastWkup_Config();
```

```c
/* ===== src/main.c 第 86-131 行：主循环（按键进 Standby 序列 + 唤醒后重入） ===== */

	for(;;)
	{
#if (1 == S32K344_EVB)
		/* Wait the button SW4 to be pressed... */
		if(Siul2_Dio_Ip_ReadChannel(SIUL_INST, SIUL_EVB_GPDI_SW4))
		{
			/* Wait the button SW1 to be released... */
			while(Siul2_Dio_Ip_ReadChannel(SIUL_INST, SIUL_EVB_GPDI_SW4)){}
			/* Turn-off Green led */
			Siul2_Dio_Ip_WriteChannel(SIUL_INST, SIUL_EVB_GPDO_BLUE1, 0U);
#else
		/* Wait the button SW2 to be pressed... */
		if(Siul2_Dio_Ip_ReadChannel(SIUL_INST, SIUL_WB_GPDI_SW3))
		{
			/* Wait the button SW1 to be released... */
			while(Siul2_Dio_Ip_ReadChannel(SIUL_INST, SIUL_WB_GPDI_SW3)){}
			/* Turn-off Green led */
			Siul2_Dio_Ip_WriteChannel(SIUL_INST, SIUL_WB_GPDO_GREEN0, 0U);
#endif

			/* Turn-off Green led */
			Siul2_Dio_Ip_WriteChannel(SIUL_INST, SIUL_EVB_GPDO_RED0, 0U);
			SIUL2->GPDO57 &= ~SIUL2_GPDO57_PDO_n_MASK;    /* Drive low on PTB 25 to turn-off LED D33 */

			/* Switch to FRIC clock */
			Clock_Ip_Init(&Mcu_aClockConfigPB_Board_standbyClockRun[0]);

			/* STANDBY IO configurations */
			DCM_GPR->DCMRWF1 &= ~DCM_GPR_DCMRWF1_STANDBY_IO_CONFIG_MASK;

			WkupFlagClear();

			/* Enter Standby Mode */
			PMC_PrepareLowPowerEntry();
			Power_Ip_SetMode(&Power_Ip_aModeConfigPB[1]);
		}
	}
    
    return (0U);
}

/* END main */
/*!
** @}
*/
```

### 3.1 配套代码：FastWkup.c（进睡眠前的 WKPU 配置序列 + 唤醒后入口，原样摘录）

WKPU 的实际配置不在 main.c，而在 `src/FastWkup.c` 的 `FastWkup_Config()`（main.c 调用）；唤醒后的判断/恢复路径在同文件 `FastWkup_RAMInit()`。以下为原样摘录。

```c
/* ===== src/FastWkup.c 第 8-76 行：RAM 向量表 + FastWkup_RAMInit（唤醒后入口） ===== */
#include "FastWkup.h"
#include "S32K344_DCM_GPR.h"
#include "S32K344_MC_RGM.h"
#include "Cmp_Ip.h"
#include "Wkpu_Ip.h"
#include "Rtc_Ip.h"


#ifdef STANDBY_RAM
extern uint32 __INT_SRAM_START;
extern uint32 __INT_SRAM_SIZE;
extern uint32 __Stack_start_c0;
extern const uint32_t __Standby_Stack_start;

extern void init_data_bss(void);
extern int main(void);
extern void undefined_handler(void);
/******************************************************************************/
/* Global Variables                                                           */
/******************************************************************************/
__attribute__ ((section(".m_interrupt_ram"))) volatile uint32_t VectorTable[] =
{
	(const uint32_t )&__Standby_Stack_start,
    (const uint32_t )((uint32_t *)&FastWkup_RAMInit),
    (const uint32_t )((uint32_t *)&undefined_handler),
    (const uint32_t )((uint32_t *)&undefined_handler),
    (const uint32_t )((uint32_t *)&undefined_handler),
    (const uint32_t )((uint32_t *)&undefined_handler),
    (const uint32_t )((uint32_t *)&undefined_handler),
    (const uint32_t )((uint32_t *)&undefined_handler),
    (const uint32_t )((uint32_t *)&undefined_handler),
    (const uint32_t )((uint32_t *)&undefined_handler),
    (const uint32_t )((uint32_t *)&undefined_handler),
    (const uint32_t )((uint32_t *)&undefined_handler),
    (const uint32_t )((uint32_t *)&undefined_handler),
    (const uint32_t )((uint32_t *)&undefined_handler),
    (const uint32_t )((uint32_t *)&undefined_handler),
    (const uint32_t )((uint32_t *)&undefined_handler)
};


void FastWkup_RAMInit(void)
{
	/* STANDBY IO configurations */
	DCM_GPR->DCMRWF1 |= DCM_GPR_DCMRWF1_STANDBY_IO_CONFIG_MASK;

	register uint32_t Cnt;
	register long long *pDest;

	(*(volatile uint32_t *)0x402902B4) = (1 << 21); //PTA29 OBE enable
	(*(volatile uint8_t *)0x4029131E) = 1; //PTA29 output 1

	Cnt = (( uint32_t)(&__INT_SRAM_SIZE)) / 8U;
	pDest = ( long long *)(&__INT_SRAM_START);
	while (Cnt--)
	{
		*pDest = ( long long)0;
		pDest++;
	}

	init_data_bss();

	/* set up stack; r13 SP*/
	__asm("ldr  r0, =__Stack_start_c0");
	__asm("msr MSP, r0");

	main();
}
#endif
```

```c
/* ===== src/FastWkup.c 第 77-113 行：FastWkup_Config（WKPU/LPCMP/RTC 唤醒源配置） ===== */

void FastWkup_Config(void)
{
#ifdef STANDBY_RAM
	 if ((MC_RGM->DES != 0) ||  /* Any destructive reset occurred? */
		((MC_RGM->FES & MC_RGM_FES_F_EXR_MASK) != 0)) /* External reset occurred? */
	{
		DCM_GPR->DCMRWF5 = (uint32_t )VectorTable |  /* Vector table address for Fast Standby Exit */
						   0x00000001UL;             /* Enable Fast Standby Exit */
		DCM_GPR->DCMRWF2 |= 0x00000040UL |  /* Bypass SIRC trimming on standby exit */
							DCM_GPR_DCMRWF2_PMC_TRIM_RGM_DCF__BYP_STDBY_EXT_MASK |  /* bypass the PMC trimming and RGM DCF loading on standby exit */
							DCM_GPR_DCMRWF2_FIRC_TRIM_BYP_STDBY_EXT_MASK |  /* Bypass FIRC trimming on standby exit */
							DCM_GPR_DCMRWF2_DCM_SCAN_BYP_STDBY_EXT_MASK;  /* bypass the DCM scanning on standby exit */
		MC_RGM->DES = MC_RGM->DES;  /* Write 1 to clear any destructive reset flag */
		MC_RGM->FES = MC_RGM_FES_F_EXR_MASK;  /* Write 1 to clear external  reset flag */

		/* LPCMP configuration */
		Cmp_Ip_Init(CMP1_INST, &Cmp_Ip_0_Config_PB_BOARD_INITPERIPHERALS);

		/* RTC configuration */
		Rtc_Ip_Init(RTC_INST, &RTC_0_InitConfig_PB);
		RTC->RTCC |= RTC_RTCC_TRIG_EN(1);  /* TRIG_EN=1: Trigger for Analog Comparator enabled */
		Rtc_Ip_EnableInterrupt(RTC_INST, RTC_IP_API_INTERRUPT);
		Rtc_Ip_StartTimer(RTC_INST, RTC_TRIGGER_LPCMP_TIME);

		/* WKPU configuration */
		Wkpu_Ip_InitInterrupt(WKPU_INST, &Wkpu_Ip_Config_PB_BOARD_INITPERIPHERALS);
		Wkpu_Ip_EnableInterrupt(WKPU_INST, WKPU_SRC_CMP_RTC);
#if (1 == S32K344_EVB)
		Wkpu_Ip_EnableInterrupt(WKPU_INST, WKPU_EVB_SRC_PTB19_42);
#else
		Wkpu_Ip_EnableInterrupt(WKPU_INST, WKPU_WB_SRC_PTC20_47);
#endif

	}
#endif
}
```

```c
/* ===== include/FastWkup.h 第 8-34 行：唤醒源/实例宏定义（原样摘录） ===== */
#ifndef FASTWKUP_H_
#define FASTWKUP_H_

#include "Std_Types.h"

#define S32K344_EVB			(0U)

#define SIUL_INST      		    0U    /*!< SIUL2 instance used - 0                */
#define SIUL_EVB_GPDO_RED0 		29U   /*!< SIUL2 GPDO offset for PTA29 (LED_RED)  */
#define SIUL_EVB_GPDO_BLUE1 	140U  /*!< SIUL2 GPDO offset for PTE12 (LED_BLUE)  */
#define SIUL_EVB_GPDI_SW4  		58U   /*!< SIUL2 GPDI offset for PTB26 (USER_SW4) */
#define WKPU_EVB_SRC_PTB19_42 	42U   /*!< PTB19 wake up source */

#define SIUL_WB_GPDO_GREEN0 	168U /*!< SIUL2 GPDO offset for PTF8 (LED_GREEN D28)  */
#define SIUL_WB_GPDI_SW3  		85U  /*!< SIUL2 GPDI offset for PTC21 (USER_SW3) */
#define WKPU_WB_SRC_PTC20_47 	47U  /*!< PTB19 wake up source */

#define WKPU_INST      			0U   /*!< WKPU instance used - 0                */
#define WKPU_SRC_CMP_RTC 		2U   /*!< CMP&RTC wake up source */

#define CMP1_INST      			1U   /*!< CMP instance used - 1                */

#define RTC_INST        		0U   /*!< RTC instance used - 0  */
#define RTC_TRIGGER_LPCMP_TIME	(3200u) //API Compare Value = 100ms / 31.25us = 3200

extern void FastWkup_RAMInit(void);
extern void FastWkup_Config(void);
```

## 4. API 速查

以下 API 均为本工程 main.c / FastWkup.c 中实际调用：

| API | 作用 | 关键参数 |
|---|---|---|
| `Wkpu_Ip_InitInterrupt(instance, config)` | 按 PBcfg 初始化 WKPU 唤醒通道（滤波、上拉、边沿、回调） | `WKPU_INST`(0)；`&Wkpu_Ip_Config_PB_BOARD_INITPERIPHERALS`（2 通道：hwCh 2=LPCMP、hwCh 47=PTC20，均上升沿+滤波+上拉） |
| `Wkpu_Ip_EnableInterrupt(instance, wkpuSrc)` | 使能某路唤醒源中断 | `WKPU_SRC_CMP_RTC`(2)=LPCMP&RTC 合成源；WB 板 `WKPU_WB_SRC_PTC20_47`(47)、EVB 板 `WKPU_EVB_SRC_PTB19_42`(42) |
| `Cmp_Ip_Init(instance, config)` | 初始化 LPCMP（含内部 DAC 1.65V 基准） | `CMP1_INST`(1)；`&Cmp_Ip_0_Config_PB_BOARD_INITPERIPHERALS` |
| `Rtc_Ip_Init(instance, config)` | 初始化 RTC | `RTC_INST`(0)；`&RTC_0_InitConfig_PB` |
| `Rtc_Ip_EnableInterrupt(instance, irqType)` | 使能 RTC API（比较）中断 | `RTC_IP_API_INTERRUPT` |
| `Rtc_Ip_StartTimer(instance, timeout)` | 启动 RTC API 计时 | `RTC_TRIGGER_LPCMP_TIME`(3200，100ms/31.25us) |
| `Power_Ip_InitPower(config)` | 电源 IP（MC_ME/MC_RGM/PMC）初始化 | `&Power_Ip_HwIPsConfigPB` |
| `Power_Ip_SetMode(config)` | 切换电源模式（进 Standby） | `&Power_Ip_aModeConfigPB[1]`（[1] 即 Standby 模式配置） |
| `PMC_PrepareLowPowerEntry()` | 进低功耗前 PMC 准备 | 无 |
| `Clock_Ip_Init(config)` | 时钟初始化；进 Standby 前切换到 standby 时钟配置 | `Mcu_aClockConfigPB_BOARD_BootClockRUN`（RUN）/ `Mcu_aClockConfigPB_Board_standbyClockRun`（Standby 前，切 FIRC） |
| `Siul2_Port_Ip_Init(numPins, pinCfg)` | 引脚复用初始化 | `NUM_OF_CONFIGURED_PINS0`, `g_pin_mux_InitConfigArr0` |
| `Siul2_Dio_Ip_WriteChannel(inst, ch, val)` | 写 GPIO（LED） | `SIUL_INST`(0)；GPDO 偏移见 FastWkup.h |
| `Siul2_Dio_Ip_ReadChannel(inst, ch)` | 读 GPIO（按键） | `SIUL_INST`(0)；GPDI 偏移见 FastWkup.h |

寄存器级操作（本工程直接访问，不走 Ip API）：`WKPU->WISR` / `WKPU->WISR_64`（写 1 清唤醒标志）、`LPCMP_1->CSR/RRCSR/RRSR`、`RTC->RTCS/RTCC`、`DCM_GPR->DCMRWF1/DCMRWF2/DCMRWF5`、`MC_RGM->DES/FES`。

## 5. 配置生成物

| 文件 | 管什么 |
|---|---|
| `generate/src/Wkpu_Ip_SA_BOARD_InitPeripherals_PBcfg.c`（+ `generate/include/Wkpu_Ip_SA_BOARD_InitPeripherals_PBcfg.h`） | WKPU 通道配置结构体：`Wkpu_Ip_ChannelConfig_PB_BOARD_INITPERIPHERALS[2]` 与 `Wkpu_Ip_Config_PB_BOARD_INITPERIPHERALS`，被 `Wkpu_Ip_InitInterrupt` 使用 |
| `generate/include/Wkpu_Ip_Defines.h` | WKPU 特性宏：`WKPU_IP_NUM_OF_CHANNELS`(64)、中断请求支持等 |
| `generate/src/Cmp_Ip_SA_BOARD_InitPeripherals_PBcfg.c` | LPCMP1 配置 `Cmp_Ip_0_Config_PB_BOARD_INITPERIPHERALS`（含 DAC 基准电压） |
| `generate/src/Rtc_Ip_BOARD_InitPeripherals_PBcfg.c` | RTC 配置 `RTC_0_InitConfig_PB` |
| `generate/src/Power_Ip_BOARD_InitPeripherals_PBcfg.c` | 电源模式配置数组 `Power_Ip_aModeConfigPB`（[1] = Standby）与 `Power_Ip_HwIPsConfigPB` |
| `board/Clock_Ip_BOARD_BootClockRUN_PBcfg.c` | RUN 模式时钟配置 |
| `board/Clock_Ip_Board_standbyClockRun_PBcfg.c` | 进 Standby 前的降级时钟配置（FIRC） |
| `board/Siul2_Port_Ip_Cfg.c` | 引脚复用表 `g_pin_mux_InitConfigArr0` |
| `Project_Settings/Linker_Files/linker_flash_standby.ld` | Standby 链接脚本，定义 `.m_interrupt_ram` 段——`FastWkup.c` 的 RAM 向量表放在该段，Fast Standby Exit 从这里取 `FastWkup_RAMInit` 入口 |

WKPU 通道配置结构体原样摘录（`generate/src/Wkpu_Ip_SA_BOARD_InitPeripherals_PBcfg.c` 第 123-172 行）：

```c
/*
 *  @brief    PB_BOARD_INITPERIPHERALS WKPU Channels Configuration
 */
const Wkpu_Ip_ChannelConfigType Wkpu_Ip_ChannelConfig_PB_BOARD_INITPERIPHERALS[2U] =
{
    /** @brief IcuWkpu_Channel_0_LPCMP */
    {
        /** @brief Wkpu HW Channel used by the Icu channel */
        2U,
        /** @brief Wkpu HW Channel Filter enable */
        TRUE,
        /** @brief Wkpu HW Channel Pullup enable */
        TRUE,
        /** @brief Wkpu Default Start Edge*/
        WKPU_IP_RISING_EDGE,
        /** @brief Wkpu Channel Callback  */
        &Wkpu_Ip_ReportEvents,
        NULL_PTR,    /* Notification function */
        /** @brief Wkpu Callback Param1*/
        2U
            }
,
    /** @brief IcuWkpu_Channel_1_PTC20 */
    {
        /** @brief Wkpu HW Channel used by the Icu channel */
        47U,
        /** @brief Wkpu HW Channel Filter enable */
        TRUE,
        /** @brief Wkpu HW Channel Pullup enable */
        TRUE,
        /** @brief Wkpu Default Start Edge*/
        WKPU_IP_RISING_EDGE,
        /** @brief Wkpu Channel Callback  */
        &Wkpu_Ip_ReportEvents,
        NULL_PTR,    /* Notification function */
        /** @brief Wkpu Callback Param1*/
        47U
            }

};
/*
 *  @brief    PB_BOARD_INITPERIPHERALS Default WKPU IP Configuration
 */
const Wkpu_Ip_IrqConfigType Wkpu_Ip_Config_PB_BOARD_INITPERIPHERALS = 
{
    /** @brief Number of Wkpu channels in the Icu configuration */
    (uint8)2U,
    /** @brief Pointer to the array of Wkpu channel configurations */
    &Wkpu_Ip_ChannelConfig_PB_BOARD_INITPERIPHERALS
};
```

## 6. 常见坑

1. **进 Standby 前必须清干净全部唤醒标志（W1C）**。`WkupFlagClear()` 依次清 `RTC->RTCS`、`LPCMP_1->CSR`（回写）、`LPCMP_1->RRCSR`（预置低）、`LPCMP_1->RRSR`(0xFF)、`WKPU->WISR`、`WKPU->WISR_64`，且调用位置在 `Power_Ip_SetMode` 之前——漏掉任何一路残留标志，休眠序列不完整（main.c 第 117-121 行顺序实证）。
2. **进 Standby 前要切换时钟并放开 STANDBY_IO 配置**：先 `Clock_Ip_Init(&Mcu_aClockConfigPB_Board_standbyClockRun[0])`（注释：Switch to FRIC clock），再 `DCM_GPR->DCMRWF1 &= ~DCM_GPR_DCMRWF1_STANDBY_IO_CONFIG_MASK`；唤醒后 `FastWkup_RAMInit` 里反向置回 `|= MASK`（main.c 第 112-115 行、FastWkup.c 第 51-52 行实证）。
3. **WKPU/LPCMP/RTC 只在冷上电配置一次**：`FastWkup_Config()` 内部判断 `MC_RGM->DES != 0`（破坏性复位）或 `FES` 外部复位才执行，并随后清掉 DES/FES；从 Standby 唤醒重入 main 时该条件不成立，直接跳过。
4. **唤醒路径会清空全部 SRAM**：Fast Standby Exit 后执行 `FastWkup_RAMInit()`——`while(Cnt--) *pDest = 0;` 把整块内部 SRAM 清零，再 `init_data_bss()` 重新加载 .data/.bss、重设 MSP、重调 `main()`。睡眠前的全局变量值唤醒后全部丢失，不能用于跨睡眠传递状态（FastWkup.c 第 60-74 行实证）。
5. **板型切换要同时改两处**：`include/FastWkup.h` 中 `S32K344_EVB`（本工程当前为 0，即 WB 板），以及换用 `S32K344_WB_Wkup_Lab.mex` / `S32K344_EVB_Wkup_Lab.mex` 重新生成代码（ReadMe.md 实证）。WKPU 唤醒源通道号随板型不同：WB=47(PTC20)，EVB=42(PTB19)。
6. **按键进 Standby 前等按键释放**：`while(Siul2_Dio_Ip_ReadChannel(...)){}` 防止按住键时长信号干扰休眠（main.c 第 94/102 行实证）。
7. **编译目标必须选 Debug_Fast_Wkup_FLASH**（ReadMe.md 实证；对应 standby 链接脚本与 STANDBY_RAM 宏编译配置）。
8. 唤醒阈值由 LPCMP 内部 DAC 设定为 1.65V：LPCMP1 通道 0/1/2（PTA0/PTA1/PTA2）输入电压大于 1.65V 才触发；RTC API 每 3200 tick（100ms）触发一次 LPCMP 采样（ReadMe.md + FastWkup.h `RTC_TRIGGER_LPCMP_TIME` 注释实证）。
