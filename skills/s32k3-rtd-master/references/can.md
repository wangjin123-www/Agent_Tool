# FlexCAN — S32K344 RTD 0.9.0 实战教学

> 源工程: D:\wnagjin\S32K3_mydetail\详细教学(1)\详细教学\S32K3 Training-RTD\S32DSv3p4_RTDv090\S32k344_CAN_Example_090_34
> 源文件: D:\wnagjin\S32K3_mydetail\详细教学(1)\详细教学\S32K3 Training-RTD\S32DSv3p4_RTDv090\S32k344_CAN_Example_090_34\src\main.c（代码原样摘录，未经任何修改）

## 1. 外设概述

FlexCAN 是 S32K3 的 CAN 控制器（S32K344 带 6 个实例 CAN0-CAN5），支持 CAN 2.0 经典帧与 CAN FD（含 BRS 波特率切换、增强 Rx FIFO、legacy Rx FIFO、DMA 搬运）。RTD 0.9.0 中对应 Ip 层驱动 `FlexCAN_Ip`（FlexCAN_Ip.c / FlexCAN_Ip_HwAccess.c / FlexCAN_Ip_Irq.c）。

注意：本工程**没有使用 AUTOSAR MCAL 的 Can/CanIf 抽象层**，而是 `FlexCAN_Ip` 驱动 + `component/can/can_config.c` 用户封装组件（`Hal_Can_Init` / `Can_MainTask` / 各节点回调）。白板（WB）演示三路节点：CAN0 = CAN FD + 增强 Rx FIFO（中断/DMA）、CAN1 = 经典帧轮询 + 独立掩码、CAN2 = 经典帧 + legacy Rx FIFO；全部节点带 bus off 检测与手动恢复（ReadMe.txt 实证）。

## 2. 初始化与使用时序

```mermaid
flowchart TD
    A[main] --> B[Clock_Ip_Init<br/>Mcu_aClockConfigPB]
    B --> C[Siul2_Port_Ip_Init 引脚]
    C --> D["TCD->CH0_ES = 0x80000001<br/>清 DMA 错误标志位"]
    D --> E{S32K344_EVB_DEMO<br/>= STD_OFF 白板?}
    E --|是| F[Dma_Ip_Init<br/>CAN0 FIFO DMA 搬运]
    E --|否 EVB| G[跳过 DMA]
    F --> H[IntCtrl_Ip_ConfigIrqRouting<br/>+ IntCtrl_Ip_Init 中断路由]
    G --> H
    H --> I[Hal_Can_Init]
    I --> I1[My_CAN_Node_0_Init<br/>FlexCAN_Ip_Init + 冻结模式配<br/>Enhanced FIFO 过滤表 + 全局掩码 + TDC]
    I --> I2[My_CAN_Node_1_Init<br/>FlexCAN_Ip_Init + ConfigRxMb×4<br/>独立掩码 RxIndividualMask×4]
    I --> I3[My_CAN_Node_2_Init<br/>FlexCAN_Ip_Init + 冻结模式配<br/>Legacy FIFO Format A 过滤表 + 掩码循环]
    I --> I4[My_Tja1145_Init 收发器]
    I1 & I2 & I3 & I4 --> J[My_CAN_StartRec<br/>FlexCAN_Ip_Receive 逐 MB 挂收]
    J --> K[for 主循环 cnt ≥ 100000]
    K --> L[Can_MainTask]
    L --> L1["CAN0: FlexCAN_Ip_Send×2 中断方式"]
    L --> L2["CAN1: Send + MainFunctionWrite/Read 轮询"]
    L --> L3["CAN2: Send×2 + FIFO 中断接收"]
    L1 & L2 & L3 --> M[MainFunctionBusOff_Privileged<br/>×3 路 busoff 轮询]
    M --> N{BusOff 标志 = true?}
    N --|是| O[Hal_Can_RecoverBusOff<br/>等 BOFFDONEINT → 手动恢复<br/>Deinit → 重新 Init]
    N --|否| K
    P[FLEXCAN 中断] --> Q[Can0_MB_RXTXCallback<br/>RX_COMPLETE 重挂 Receive]
    P --> R[Can0_Error_Callback<br/>读 ESR1 置 BusOff 标志<br/>AbortTransfer 中止发送]
```

## 3. main.c 原样代码

源文件共 96 行，以下按逻辑段落分块摘录，与源文件逐字符一致（注意本文件混用 Tab 与 4 空格缩进，均按原样保留）。

```c
/* ===== src/main.c 第 1-43 行：文件头 + 头文件包含 ===== */
/*==================================================================================================
*   Project              : RTD AUTOSAR 4.4
*   Platform             : CORTEXM
*   Peripheral           : S32K3XX
*   Dependencies         : none
*
*   Autosar Version      : 4.4.0
*   Autosar Revision     : ASR_REL_4_4_REV_0000
*   Autosar Conf.Variant :
*   SW Version           : 0.9.0
*   Build Version        : S32K3_RTD_0_9_0__ASR_REL_4_4_REV_0000_20210326
*
*   (c) Copyright 2020 - 2021 NXP Semiconductors
*   All Rights Reserved.
*
*   NXP Confidential. This software is owned or controlled by NXP and may only be
*   used strictly in accordance with the applicable license terms. By expressly
*   accepting such terms or by downloading, installing, activating and/or otherwise
*   using the software, you are agreeing that you have read, and that you agree to
*   comply with and are bound by, such license terms. If you do not agree to be
*   bound by the applicable license terms, then you may not retain, install,
*   activate or otherwise use the software.
==================================================================================================*/

/**
*   @file main.c
*
*   @addtogroup main_module main module documentation
*   @{
*/

/* Including necessary configuration files. */
#include "Mcal.h"
#include "can_config.h"
#include "lin_config.h"
#include "Clock_Ip.h"
#include "Siul2_Dio_Ip.h"
#include "Siul2_Port_Ip.h"
#if(STD_OFF == S32K344_EVB_DEMO)
#include "Dma_Ip.h"
#endif
volatile int exit_code= 0;
/* User includes */
```

```c
/* ===== src/main.c 第 44-74 行：main 初始化序列（时钟/引脚/DMA/中断/CAN） ===== */

/*!
  \brief The main function for the project.
  \details The startup initialization sequence is the following:
 * - startup asm routine
 * - main()
*/
int main(void)
{
    /* Write your code here */
	/* Initialize the clock */
	uint32_t cnt = 0;

	Clock_Ip_Init(&Mcu_aClockConfigPB[0]);

	/* initialize the port */
	Siul2_Port_Ip_Init(NUM_OF_CONFIGURED_PINS0, g_pin_mux_InitConfigArr0);

	/* Clear the ES bits in case lauterbach cmm will initialize DMA mistakely。*/
	TCD->CH0_ES = 0x80000001;

#if(STD_OFF == S32K344_EVB_DEMO)
	Dma_Ip_Init(&Dma_Ip_xDmaInitPB);
#endif // White board CAN0 will call DMA initialization

	/* Initialize the interrupt module */
    IntCtrl_Ip_ConfigIrqRouting(&intRouteConfig);
    IntCtrl_Ip_Init(&IntCtrlConfig_0);

	/* initialize the CAN module as needed */
	Hal_Can_Init();
```

```c
/* ===== src/main.c 第 75-96 行：主循环（周期调 Can_MainTask） ===== */

	for(;;)
		{
		cnt++;
		if(cnt >= 100000)
		{
			/* The main task of flexcan test */
			Can_MainTask();
			cnt = 0;
		}

			 if(exit_code != 0)
			{
				break;
			}

		}

    return exit_code;
}

/** @} */
```

### 3.1 CAN 组件代码：component/can/can_config.c（初始化 / 收发 / 回调，原样摘录）

main.c 只做框架，CAN 的初始化、收发、回调全部在 `component/can/can_config.c`（白板分支 `STD_OFF == S32K344_EVB_DEMO`）。

```c
/* ===== component/can/can_config.c 第 891-935 行：My_CAN_Node_0_Init（CAN FD + Enhanced FIFO + 全局掩码） ===== */
void My_CAN_Node_0_Init(void)
{
	FlexCAN_Ip_Init(INST_FLEXCAN_0, &FlexCAN_State0, &FlexCAN_Config0);

	/* configure the enhanced fifo if needed */
	/* enter the freeze mode */
	FlexCAN_Ip_EnterFreezeMode(INST_FLEXCAN_0);

	/* configure the FlexCAN enhanced FIFO filter table */
	FlexCAN_Ip_ConfigEnhancedRxFifo_Privileged(INST_FLEXCAN_0, &CAN_EnhancedFIFO_FilterTable[0]);

	/* exit the freeze mode */
	FlexCAN_Ip_ExitFreezeMode(INST_FLEXCAN_0);

	/* set start mode */
	FlexCAN_Ip_SetStartMode(INST_FLEXCAN_0);

	/* open the RX enhanced or legacy FIFO */
	FlexCAN_Ip_RxFifo(INST_FLEXCAN_0, &CAN0_FIFO_Received_MB);

    /* Configure the mb0-5 to receive frame */
	FlexCAN_Ip_ConfigRxMb(INST_FLEXCAN_0, CAN_NODE_0_RX_MB0, &CAN_NODE_0_RX_MB0_Config, CAN_NODE_0_RX_MB0_ID);
	FlexCAN_Ip_ConfigRxMb(INST_FLEXCAN_0, CAN_NODE_0_RX_MB1, &CAN_NODE_0_RX_MB1_Config, CAN_NODE_0_RX_MB1_ID);
	FlexCAN_Ip_ConfigRxMb(INST_FLEXCAN_0, CAN_NODE_0_RX_MB2, &CAN_NODE_0_RX_MB2_Config, CAN_NODE_0_RX_MB2_ID);
	FlexCAN_Ip_ConfigRxMb(INST_FLEXCAN_0, CAN_NODE_0_RX_MB3, &CAN_NODE_0_RX_MB3_Config, CAN_NODE_0_RX_MB3_ID);
	FlexCAN_Ip_ConfigRxMb(INST_FLEXCAN_0, CAN_NODE_0_RX_MB4, &CAN_NODE_0_RX_MB4_Config, CAN_NODE_0_RX_MB4_ID);
	FlexCAN_Ip_ConfigRxMb(INST_FLEXCAN_0, CAN_NODE_0_RX_MB5, &CAN_NODE_0_RX_MB5_Config, CAN_NODE_0_RX_MB5_ID);
	
	/* Enter the freeze mode*/
	FlexCAN_Ip_EnterFreezeMode(INST_FLEXCAN_0);

	/* Set the global mask */
	FlexCAN_Ip_SetRxMaskType(INST_FLEXCAN_0, FLEXCAN_RX_MASK_GLOBAL);
	FlexCAN_Ip_SetRxMbGlobalMask(INST_FLEXCAN_0, My_CAN_NODE_0_MB_GLBMASK);

	/* Exit the freeze mode*/
	FlexCAN_Ip_ExitFreezeMode(INST_FLEXCAN_0);

	/* Configure the TDC feature */
	My_CAN_FDTdcConfig(INST_FLEXCAN_0, true); /* Configure the CAN TDC feature */

	/* Set start mode */
	FlexCAN_Ip_SetStartMode(INST_FLEXCAN_0);

}
```

```c
/* ===== component/can/can_config.c 第 945-971 行：My_CAN_Node_1_Init（经典帧轮询 + 独立掩码） ===== */
void My_CAN_Node_1_Init(void)
{
	FlexCAN_Ip_Init(INST_FLEXCAN_1, &FlexCAN_State1, &FlexCAN_Config1);

	/* Configure the mb0-3 to receive frame */
	FlexCAN_Ip_ConfigRxMb(INST_FLEXCAN_1, CAN_NODE_1_RX_MB0, &CAN_NODE_1_RX_MB0_Config, CAN_NODE_1_RX_MB0_ID);
	FlexCAN_Ip_ConfigRxMb(INST_FLEXCAN_1, CAN_NODE_1_RX_MB1, &CAN_NODE_1_RX_MB1_Config, CAN_NODE_1_RX_MB1_ID);
	FlexCAN_Ip_ConfigRxMb(INST_FLEXCAN_1, CAN_NODE_1_RX_MB2, &CAN_NODE_1_RX_MB2_Config, CAN_NODE_1_RX_MB2_ID);
	FlexCAN_Ip_ConfigRxMb(INST_FLEXCAN_1, CAN_NODE_1_RX_MB3, &CAN_NODE_1_RX_MB3_Config, CAN_NODE_1_RX_MB3_ID);

	/* Enter the freeze mode */
	FlexCAN_Ip_EnterFreezeMode(INST_FLEXCAN_1);

	/* Set the individual mask type */
	FlexCAN_Ip_SetRxMaskType(INST_FLEXCAN_1, FLEXCAN_RX_MASK_INDIVIDUAL);

	FlexCAN_Ip_SetRxIndividualMask(INST_FLEXCAN_1, CAN_NODE_1_RX_MB0, My_CAN_NODE_1_MB0_INDMASK);
	FlexCAN_Ip_SetRxIndividualMask(INST_FLEXCAN_1, CAN_NODE_1_RX_MB1, My_CAN_NODE_1_MB1_INDMASK);
	FlexCAN_Ip_SetRxIndividualMask(INST_FLEXCAN_1, CAN_NODE_1_RX_MB2, My_CAN_NODE_1_MB2_INDMASK);
	FlexCAN_Ip_SetRxIndividualMask(INST_FLEXCAN_1, CAN_NODE_1_RX_MB3, My_CAN_NODE_1_MB3_INDMASK);

	/* Exit the freeze mode */
	FlexCAN_Ip_ExitFreezeMode(INST_FLEXCAN_1);

	/* Set start mode */
	FlexCAN_Ip_SetStartMode(INST_FLEXCAN_1);
}
```

```c
/* ===== component/can/can_config.c 第 981-1014 行：My_CAN_Node_2_Init（经典帧 + Legacy FIFO） ===== */
void My_CAN_Node_2_Init(void)
{
	/* configure the legacy fifo if needed */
	uint8_t fifofilter_idx = 0;
	uint32_t fifofilter_maxnum = (FlexCAN_Config2.num_id_filters + 1) * 8;

	FlexCAN_Ip_Init(INST_FLEXCAN_2, &FlexCAN_State2, &FlexCAN_Config2);

	/* enter the freeze mode */
	FlexCAN_Ip_EnterFreezeMode(INST_FLEXCAN_2);

	/* Set the individual mask type */
	FlexCAN_Ip_SetRxMaskType_Privileged(INST_FLEXCAN_2, FLEXCAN_RX_MASK_INDIVIDUAL);

	/* configure the FlexCAN RxFIFO filter table */
	FlexCAN_Ip_ConfigRxFifo_Privileged(INST_FLEXCAN_2, FLEXCAN_RX_FIFO_ID_FORMAT_A, CAN2_LegacyFIFO_IdFilterTable);
	//FlexCAN_Ip_ConfigRxFifo_Privileged(INST_FLEXCAN_2, FLEXCAN_RX_FIFO_ID_FORMAT_B, CAN2_LegacyFIFO_IdFilterTable);

	/* configure the FlexCAN RxFIFO filter table ID mask */
	for(fifofilter_idx=0; fifofilter_idx < fifofilter_maxnum; fifofilter_idx++)
	{
		/* mask all the bits */
		FlexCAN_Ip_SetRxIndividualMask_Privileged(INST_FLEXCAN_2, fifofilter_idx, My_CAN_NODE_2_MB_INDMASK(fifofilter_idx));
	}

	/* Exit the freeze mode */
	FlexCAN_Ip_ExitFreezeMode(INST_FLEXCAN_2);

	/* open the RX enhanced or legacy FIFO */
	FlexCAN_Ip_RxFifo(INST_FLEXCAN_2, &CAN2_FIFO_Received_MB[0]);

	/* Set start mode */
	FlexCAN_Ip_SetStartMode(INST_FLEXCAN_2);
}
```

```c
/* ===== component/can/can_config.c 第 1092-1115 行：Hal_Can_Init（CAN 总初始化入口，main 调用） ===== */
/*FUNCTION**********************************************************************
 *
 * Function Name : My_CAN_Init
 * Description   : This function complete the CAN initialization
 *
 *END**************************************************************************/
void Hal_Can_Init(void)
{
#if(STD_ON == S32K344_EVB_DEMO)   /* Red board demo */
	My_CAN_Node_4_Init();
	My_CAN_Node_5_Init();
	My_Tja1153_Init();
#endif

#if(STD_OFF == S32K344_EVB_DEMO) /* White board demo */
	My_CAN_Node_0_Init();   /* Initialize CAN_NODE_0 */
    My_CAN_Node_1_Init();
	My_CAN_Node_2_Init();
	My_Tja1145_Init();
#endif

	/* Start receiving */
	My_CAN_StartRec();
}
```

```c
/* ===== component/can/can_config.c 第 1198-1237 行：My_CAN_StartRec（逐 MB 挂收） ===== */
/*FUNCTION**********************************************************************
 *
 * Function Name : My_CAN_StartRec
 * Description   : This function start the CAN 0-3 module receiving
 *
 *END**************************************************************************/
void My_CAN_StartRec(void)
{
#if(STD_OFF == S32K344_EVB_DEMO)  // White board demo start receiving.
	/* Open the CAN node 0 RxMb0-5 to receive by interrupt */
	FlexCAN_Ip_Receive(CAN_NODE_0, CAN_NODE_0_RX_MB0, &My_CAN_NODE_0_Received_MB[0], false);
	FlexCAN_Ip_Receive(CAN_NODE_0, CAN_NODE_0_RX_MB1, &My_CAN_NODE_0_Received_MB[1], false);
	FlexCAN_Ip_Receive(CAN_NODE_0, CAN_NODE_0_RX_MB2, &My_CAN_NODE_0_Received_MB[2], false);
	FlexCAN_Ip_Receive(CAN_NODE_0, CAN_NODE_0_RX_MB3, &My_CAN_NODE_0_Received_MB[3], false);
	FlexCAN_Ip_Receive(CAN_NODE_0, CAN_NODE_0_RX_MB4, &My_CAN_NODE_0_Received_MB[4], false);
	FlexCAN_Ip_Receive(CAN_NODE_0, CAN_NODE_0_RX_MB5, &My_CAN_NODE_0_Received_MB[5], false);

	/* Open the CAN node 1 RxMb0-3 to receive by polling */
	FlexCAN_Ip_Receive(CAN_NODE_1, CAN_NODE_1_RX_MB0, &My_CAN_NODE_1_Received_MB[0], true);
	FlexCAN_Ip_Receive(CAN_NODE_1, CAN_NODE_1_RX_MB1, &My_CAN_NODE_1_Received_MB[1], true);
	FlexCAN_Ip_Receive(CAN_NODE_1, CAN_NODE_1_RX_MB2, &My_CAN_NODE_1_Received_MB[2], true);
	FlexCAN_Ip_Receive(CAN_NODE_1, CAN_NODE_1_RX_MB3, &My_CAN_NODE_1_Received_MB[3], true);

#endif

#if(STD_ON == S32K344_EVB_DEMO)// Red board demo start receiving.
	/* Open the CAN node 4 RxMb0-3 to receive by interrupt */
	FlexCAN_Ip_Receive(CAN_NODE_4, CAN_NODE_4_RX_MB0, &My_CAN_NODE_4_Received_MB[0], false);
	FlexCAN_Ip_Receive(CAN_NODE_4, CAN_NODE_4_RX_MB1, &My_CAN_NODE_4_Received_MB[1], false);
	FlexCAN_Ip_Receive(CAN_NODE_4, CAN_NODE_4_RX_MB2, &My_CAN_NODE_4_Received_MB[2], false);
	FlexCAN_Ip_Receive(CAN_NODE_4, CAN_NODE_4_RX_MB3, &My_CAN_NODE_4_Received_MB[3], false);

    /* Open the CAN node 5 RxMb0-3 to receive by polling */
	FlexCAN_Ip_Receive(CAN_NODE_5, CAN_NODE_5_RX_MB0, &My_CAN_NODE_5_Received_MB[0], true);
	FlexCAN_Ip_Receive(CAN_NODE_5, CAN_NODE_5_RX_MB1, &My_CAN_NODE_5_Received_MB[1], true);
	FlexCAN_Ip_Receive(CAN_NODE_5, CAN_NODE_5_RX_MB2, &My_CAN_NODE_5_Received_MB[2], true);
	FlexCAN_Ip_Receive(CAN_NODE_5, CAN_NODE_5_RX_MB3, &My_CAN_NODE_5_Received_MB[3], true);
#endif

}
```

```c
/* ===== component/can/can_config.c 第 467-522 行：Can0_MB_RXTXCallback（接收/发送完成回调） ===== */
/*FUNCTION**********************************************************************
 *
 * Function Name : CAN_NODE_0_MB_RXTXCallback
 * Description   : This function implement the CAN TX/RX complete callback
 *
 *END**************************************************************************/
void Can0_MB_RXTXCallback(uint8 instance, Flexcan_Ip_EventType eventType,
                  uint32 buffIdx, Flexcan_Ip_StateType * flexcanState)
{
	(void)instance;
	(void)flexcanState;

	switch(eventType)
	{
#if(FEATURE_CAN_HAS_DMA_ENABLE)
	case FLEXCAN_EVENT_DMA_COMPLETE:
#endif
		case FLEXCAN_EVENT_ENHANCED_RXFIFO_COMPLETE:
			/* Reopen the RX enhanced FIFO and put the received data in MyFIFO_Received_MB */
			FlexCAN_Ip_RxFifo(instance, &CAN0_FIFO_Received_MB);
			break;

		case FLEXCAN_EVENT_ENHANCED_RXFIFO_WATERMARK:
		case FLEXCAN_EVENT_ENHANCED_RXFIFO_OVERFLOW:
		case FLEXCAN_EVENT_ENHANCED_RXFIFO_UNDERFLOW:
			break;

		case FLEXCAN_EVENT_RX_COMPLETE:
			switch(buffIdx)
			{
			case CAN_NODE_0_RX_MB0:
				/* Reset the RX MB0 state to BUSY to receive next new message */
				FlexCAN_Ip_Receive(CAN_NODE_0, CAN_NODE_0_RX_MB0, &My_CAN_NODE_0_Received_MB[0], false);
				break;
			case CAN_NODE_0_RX_MB1:
				FlexCAN_Ip_Receive(CAN_NODE_0, CAN_NODE_0_RX_MB1, &My_CAN_NODE_0_Received_MB[1], false);
				break;
			case CAN_NODE_0_RX_MB2:
				FlexCAN_Ip_Receive(CAN_NODE_0, CAN_NODE_0_RX_MB2, &My_CAN_NODE_0_Received_MB[2], false);
				break;
			case CAN_NODE_0_RX_MB3:
				FlexCAN_Ip_Receive(CAN_NODE_0, CAN_NODE_0_RX_MB3, &My_CAN_NODE_0_Received_MB[3], false);
				break;
			case CAN_NODE_0_RX_MB4:
				FlexCAN_Ip_Receive(CAN_NODE_0, CAN_NODE_0_RX_MB4, &My_CAN_NODE_0_Received_MB[4], false);
				break;
			case CAN_NODE_0_RX_MB5:
				FlexCAN_Ip_Receive(CAN_NODE_0, CAN_NODE_0_RX_MB5, &My_CAN_NODE_0_Received_MB[5], false);
				break;
			default:
				break;
			}
		default:
			break;
	}
}
```

```c
/* ===== component/can/can_config.c 第 525-555 行：Can0_Error_Callback（bus off 错误回调） ===== */
/*FUNCTION**********************************************************************
 *
 * Function Name : CAN_NODE_0_Error_Callback
 * Description   : This function implement the CAN Error callback, it realize the
 *                 process of how to manual recovery from bus off state.
 *
 *END**************************************************************************/
void Can0_Error_Callback(uint8 instance, Flexcan_Ip_EventType eventType,
                  uint32 buffIdx, Flexcan_Ip_StateType * flexcanState)
{
	(void)buffIdx;
	(void)flexcanState;
	/* ESR1 register temporary value */
	uint32_t temp_ESR1_RegVal   = 0;

	/* Get ESR1 register value */
	temp_ESR1_RegVal   =  FlexCAN_Ip_GetErrorStatus(instance);

	if((eventType == FLEXCAN_EVENT_ERROR) || (eventType == FLEXCAN_EVENT_BUSOFF))
	{
		if(FLEXCAN_ESR1_BOFFINT_MASK & temp_ESR1_RegVal)
		{
			/* Set the bus off flag */
			CAN_NODE_0_BusOff_Flag = true;

			/* Abort the transmission first*/
			FlexCAN_Ip_AbortTransfer(instance, CAN_NODE_0_TX_MB0);
			FlexCAN_Ip_AbortTransfer(instance, CAN_NODE_0_TX_MB1);
		}
	}
}
```

```c
/* ===== component/can/can_config.c 第 1313-1413 行：Can_MainTask（主循环收发 + bus off 恢复） ===== */
/*FUNCTION**********************************************************************
 *
 * Function Name : Can_MainTask
 * Description   : This function start the can main task.
 *
 *END**************************************************************************/
void Can_MainTask(void)
{
#if(STD_OFF == S32K344_EVB_DEMO)
	/************************************************************************
	* CAN node 0: CAN FD enhanced fifo with interrupt and global mask
	*************************************************************************/
	/* TX_MB0 send test */
	FlexCAN_Ip_Send(CAN_NODE_0, CAN_NODE_0_TX_MB0, \
			&CAN_NODE_0_TX_MB0_Config, CAN_NODE_0_TX_MB0_ID, (uint8 *)&dummyData );

	/* TX_MB1 send test */
	FlexCAN_Ip_Send(CAN_NODE_0, CAN_NODE_0_TX_MB1, \
			&CAN_NODE_0_TX_MB1_Config, CAN_NODE_0_TX_MB1_ID, (uint8 *)&dummyData );

	/* CAN bus off judgement API */
	FlexCAN_Ip_MainFunctionBusOff_Privileged(CAN_NODE_0);

	/* CAN bus off recovery API */
	if(true == CAN_NODE_0_BusOff_Flag)
	{
		Hal_Can_RecoverBusOff(CAN_NODE_0);
	}

	/************************************************************************
	* CAN node 1 (CAN instance 1): CAN 2.0 with polling
	*************************************************************************/
	/* CAN node 1 poll the tx buffer */
	FlexCAN_Ip_Send(CAN_NODE_1, CAN_NODE_1_TX_MB0, &CAN_NODE_1_TX_MB0_Config, \
	        CAN_NODE_1_TX_MB0_ID, (uint8 *)&dummyData );
	FlexCAN_Ip_MainFunctionWrite(CAN_NODE_1, CAN_NODE_1_TX_MB0);

	FlexCAN_Ip_Send(CAN_NODE_1, CAN_NODE_1_TX_MB1, &CAN_NODE_1_TX_MB1_Config, \
	        CAN_NODE_1_TX_MB1_ID, (uint8 *)&dummyData );
	FlexCAN_Ip_MainFunctionWrite(CAN_NODE_1, CAN_NODE_1_TX_MB1);

	/* CAN node 1 poll the received buffer */
	FlexCAN_Ip_MainFunctionRead(CAN_NODE_1, CAN_NODE_1_RX_MB0);
	FlexCAN_Ip_MainFunctionRead(CAN_NODE_1, CAN_NODE_1_RX_MB1);
	FlexCAN_Ip_MainFunctionRead(CAN_NODE_1, CAN_NODE_1_RX_MB2);
	FlexCAN_Ip_MainFunctionRead(CAN_NODE_1, CAN_NODE_1_RX_MB3);

	/* CAN bus off judgement API */
	FlexCAN_Ip_MainFunctionBusOff_Privileged(CAN_NODE_1);

	/* CAN bus off recovery API */
	if(true == CAN_NODE_1_BusOff_Flag)
	{
		Hal_Can_RecoverBusOff(CAN_NODE_1);
	}

	/************************************************************************
	* CAN node 2 (CAN instance 2): CAN 2.0 with legacy fifo
	*************************************************************************/
	/* CAN node 2 interrupt send */
	FlexCAN_Ip_Send(CAN_NODE_2, CAN_NODE_2_TX_MB0, &CAN_NODE_2_TX_MB0_Config, \
	        CAN_NODE_2_TX_MB0_ID, (uint8 *)&dummyData );

	FlexCAN_Ip_Send(CAN_NODE_2, CAN_NODE_2_TX_MB1, &CAN_NODE_2_TX_MB1_Config, \
	        CAN_NODE_2_TX_MB1_ID, (uint8 *)&dummyData );

	/* CAN bus off judgement API */
	FlexCAN_Ip_MainFunctionBusOff_Privileged(CAN_NODE_2);

	/* CAN bus off recovery API */
	if(true == CAN_NODE_2_BusOff_Flag)
	{
		Hal_Can_RecoverBusOff(CAN_NODE_2);
	}
#endif  // End of white board CAN demo project main task


#if(STD_ON == S32K344_EVB_DEMO) // Red board CAN main task
	/************************************************************************
	* CAN node 4 (EVB CAN 1): CAN 2.0 with interrupt
	*************************************************************************/
	FlexCAN_Ip_Send(CAN_NODE_4, CAN_NODE_4_TX_MB0, &CAN_NODE_4_TX_MB0_Config, \
			CAN_NODE_4_TX_MB0_ID, (uint8 *)&dummyData );

	FlexCAN_Ip_Send(CAN_NODE_4, CAN_NODE_4_TX_MB1, &CAN_NODE_4_TX_MB1_Config, \
			CAN_NODE_4_TX_MB1_ID, (uint8 *)&dummyData );

    /************************************************************************
	* CAN node 5 (EVB CAN 0): CAN 2.0 with polling
	*************************************************************************/
	FlexCAN_Ip_Send(CAN_NODE_5, CAN_NODE_5_TX_MB0, &CAN_NODE_5_TX_MB0_Config, \
			CAN_NODE_5_TX_MB0_ID, (uint8 *)&dummyData );
	FlexCAN_Ip_MainFunctionWrite(CAN_NODE_5, CAN_NODE_5_TX_MB0);

	FlexCAN_Ip_MainFunctionRead(CAN_NODE_5, CAN_NODE_5_RX_MB0);
	FlexCAN_Ip_MainFunctionRead(CAN_NODE_5, CAN_NODE_5_RX_MB1);
	FlexCAN_Ip_MainFunctionRead(CAN_NODE_5, CAN_NODE_5_RX_MB2);
	FlexCAN_Ip_MainFunctionRead(CAN_NODE_5, CAN_NODE_5_RX_MB3);
#endif  // End of red board CAN demo project main task

}
```

## 4. API 速查

以下 API 均为本工程实际调用（`instance` = `INST_FLEXCAN_0/1/2`，白板）：

| API | 作用 | 关键参数 |
|---|---|---|
| `FlexCAN_Ip_Init(instance, state, config)` | 初始化 FlexCAN 实例（MB 数、FD、波特率、回调、传输方式） | `&FlexCAN_State0/1/2`（驱动状态）；`&FlexCAN_Config0/1/2`（生成配置） |
| `FlexCAN_Ip_EnterFreezeMode / ExitFreezeMode(instance)` | 进/出冻结模式，改掩码/过滤表/FD 参数前必须冻结 | 实例号 |
| `FlexCAN_Ip_ConfigRxMb(instance, mbIdx, info, msgId)` | 配置某个 Rx MB 的格式与 ID | MB 号（如 12-17）；`Flexcan_Ip_DataInfoType*`（fd_enable/msg_id_type/enable_brs/is_polling）；报文 ID |
| `FlexCAN_Ip_SetRxMaskType(instance, type)` | 掩码模式选择 | `FLEXCAN_RX_MASK_GLOBAL` / `FLEXCAN_RX_MASK_INDIVIDUAL` |
| `FlexCAN_Ip_SetRxMbGlobalMask(instance, mask)` | 设置 Rx 全局掩码（CAN0 用 0xFFFFFFFF 全比对） | 32 位掩码 |
| `FlexCAN_Ip_SetRxIndividualMask(instance, mbIdx, mask)` | 设置 MB/FIFO 元素独立掩码（CAN1/CAN2 用） | 掩码含 IDE/RTR 位（`IDE_MASK(1)\|RTR_MASK(1)`） |
| `FlexCAN_Ip_ConfigEnhancedRxFifo_Privileged(instance, table)` | 配置增强 Rx FIFO 过滤表（CAN0） | `CAN_EnhancedFIFO_FilterTable`（range/one-id/two-id 过滤元素） |
| `FlexCAN_Ip_ConfigRxFifo_Privileged(instance, format, table)` | 配置 legacy Rx FIFO 过滤表（CAN2） | `FLEXCAN_RX_FIFO_ID_FORMAT_A/B`；`CAN2_LegacyFIFO_IdFilterTable[8]` |
| `FlexCAN_Ip_SetStartMode(instance)` | 脱离冻结、启动收发 | 实例号 |
| `FlexCAN_Ip_Receive(instance, mbIdx, buff, isPolling)` | 挂 MB 收报文（中断/轮询二选一） | `false`=中断方式（CAN0）；`true`=轮询（CAN1，配合 MainFunctionRead） |
| `FlexCAN_Ip_RxFifo(instance, buff)` | 打开/重开 Rx FIFO 收报文 | `Flexcan_Ip_MsgBuffType*` 接收缓冲 |
| `FlexCAN_Ip_Send(instance, mbIdx, info, msgId, data)` | 发送报文 | TX MB 号（10/11 等）；`DataInfoType`（data_length/fd_padding）；数据指针 `&dummyData` |
| `FlexCAN_Ip_MainFunctionWrite(instance, mbIdx)` | 轮询推进发送 | 仅轮询节点需要（CAN1/CAN5） |
| `FlexCAN_Ip_MainFunctionRead(instance, mbIdx)` | 轮询推进接收 | 仅轮询节点需要 |
| `FlexCAN_Ip_MainFunctionBusOff_Privileged(instance)` | 轮询处理 bus off 事件 | 各节点每周期调用 |
| `FlexCAN_Ip_GetErrorStatus(instance)` | 读 ESR1 错误状态寄存器 | 判断 `FLEXCAN_ESR1_BOFFINT_MASK` / `BOFFDONEINT_MASK` |
| `FlexCAN_Ip_AbortTransfer(instance, mbIdx)` | 中止某 MB 的发送（bus off 时） | TX MB 号 |
| `FlexCAN_Ip_Deinit / SetStopMode(instance)` | 反初始化/停机（bus off 恢复流程用） | 实例号 |
| `FlexCAN_Ip_GetTDCValue / GetBitrateFD / SetTDCOffset_Privileged` | CAN FD TDC（收发器延迟补偿）配置 | `My_CAN_FDTdcConfig` 封装 |
| `IntCtrl_Ip_ConfigIrqRouting / IntCtrl_Ip_Init` | 中断路由与控制器初始化（FlexCAN ISR 到核） | `&intRouteConfig`；`&IntCtrlConfig_0` |
| `Dma_Ip_Init(&Dma_Ip_xDmaInitPB)` | DMA 初始化（白板 CAN0 FIFO 搬运用） | 生成配置 |

## 5. 配置生成物

| 文件 | 管什么 |
|---|---|
| `component/can/can_config.c` / `can_config.h` | **用户层封装（非生成物）**：节点初始化、MB/掩码/FIFO 的运行时配置、收发主任务、回调函数、bus off 恢复；`S32K344_EVB_DEMO` 板型开关 |
| `generate/src/FlexCAN_Ip_Sa_BOARD_InitPeripherals_PBcfg.c` | `FlexCAN_State0/1/2` 驱动状态结构 + `FlexCAN_Config0/1/2` 三份 Ip 级配置：MB 数（21/64/16）、FD 使能、payload 档位、正常/FD 波特率时序、传输类型（`FLEXCAN_RXFIFO_USING_DMA`/`INTERRUPTS`）、回调函数挂接 |
| `generate/include/FlexCAN_Ip_Sa_BOARD_InitPeripherals_PBcfg.h` | 实例号宏 `INST_FLEXCAN_0=0U` / `INST_FLEXCAN_1=1U` / `INST_FLEXCAN_2=2U` |
| `generate/include/FlexCAN_Ip_Cfg.h` | 特性宏：`FEATURE_CAN_HAS_DMA_ENABLE`、`FEATURE_CAN_HAS_ENHANCED_RX_FIFO`、`FEATURE_CANx_MAX_MB_NUM`、`CAN_TIMEOUT_DURATION` 等 |
| `generate/src/IntCtrl_Ip_Cfg.c`（+ `include/IntCtrl_Ip_Cfg.h`） | 中断路由表 `intRouteConfig`、中断控制器配置 `IntCtrlConfig_0`（FlexCAN 各 ISR 的使能与分发） |
| `generate/src/Dma_Ip_BOARD_InitPeripherals_PBcfg.c` + `Dma_Ip_Cfg.c` | DMA 通道配置（白板 CAN0 增强 FIFO DMA 搬运，`DMA_IP_HW_CH_0`） |
| `board/Clock_Ip_Cfg.c` / `Clock_Ip_PBcfg.c` | 系统时钟与 CAN 模块时钟（波特率分频的基准） |
| `board/Siul2_Port_Ip_Cfg.c` | CAN TX/RX 引脚复用 `g_pin_mux_InitConfigArr0` |
| `phy/TJA1145/`、`phy/TJA1153/` | CAN 收发器驱动（白板 TJA1145 / EVB TJA1153，经 LpSPI 配置） |
| `component/lin/lin_config.c` | LIN 组件配置（被 main.c include，本 CAN 演示非主线） |

`FlexCAN_Config0` 结构体原样摘录（`generate/src/FlexCAN_Ip_Sa_BOARD_InitPeripherals_PBcfg.c` 第 104-185 行，CAN FD + 增强 FIFO + DMA 代表例）：

```c
const Flexcan_Ip_ConfigType FlexCAN_Config0  = {
    /* Number Of Message Buffer used .max_num_mb  */
    (uint8)21,
    /*Can Hw filter count* .num_id_filters*- aici exista variatna sa generez toate filtrele si sa referentiezi tu in cod */
    FLEXCAN_RX_FIFO_ID_FILTERS_8,
    /* Legacy FIFO ENABLED .is_rx_fifo_needed*/
    (boolean)FALSE,
#if (FEATURE_CAN_HAS_ENHANCED_RX_FIFO == STD_ON)
    /* The number of standard ID filter elements */
    2U,
    /* The number of extended ID filter elements */
    1U,
    /* The number of enhanced Rx FIFO watermark */
    1U,
    /* The Enhanced Rx FIFO feature is enabled or not. */
    (boolean)TRUE,
#endif
#if (FEATURE_CAN_HAS_HR_TIMER == STD_ON)
    /* TimeStamp Structure Configuration */
    {
        /* timeStampSurce Timer Source */
        FLEXCAN_CAN_CLK_TIMESTAMP_SRC,
        /* msgBuffTimeStampType Timestamp MB Type  */
        FLEXCAN_MSGBUFFTIMESTAMP_TIMER,
        /* hrConfigType Timestamp HR capture configuration */
        FLEXCAN_TIMESTAMPCAPTURE_DISABLE,
        /* hrSrc HT Timer Source */
        FLEXCAN_HRTIMERSRC_MAC,
    },
#endif
    FLEXCAN_NORMAL_MODE,
     /*ctrlOptions*/
    (uint32)(CAN_FD_ISO_U32 | \
    \
    0U),
     /* Can FD RamBlock specified *//*.payload*/
    {
      FLEXCAN_PAYLOAD_SIZE_64,
      FLEXCAN_PAYLOAD_SIZE_64,
      FLEXCAN_PAYLOAD_SIZE_64
    },
        /*Can FD enabled .fd_enable*/
        (boolean)TRUE,
        /*Enhance CBT support . extCbtEnable*/
        (boolean)FALSE,
        /*BRS for FD .bitRateSwitch*/
        (boolean)TRUE,
        /*values for normal baudrate .bitrate*/
        {   /* Prop Seg */
            (4U),
            /* Phase Seg 1 */
            (1U),
            /* Phase Seg 2*/
            (1U),
            /* Pre Divider */
            (15U),
            /* Resync jump width */
            (1U)
        },
            /*values for FD baudrate .bitrate*/
        {   /* Prop Seg */
            (11U),
            /* Phase Seg 1 */
            (3U),
            /* Phase Seg 2*/
            (3U),
            /* Pre Divider */
            (1U),
            /* Resync jump width */
            (3U)
        },
        /*transfer_type*/
        FLEXCAN_RXFIFO_USING_DMA,
#if (FEATURE_CAN_HAS_DMA_ENABLE == STD_ON)
     /* DMA channel number used for transfers. */
        DMA_IP_HW_CH_0,
  #endif
    /* Controller Callback */
    Can0_MB_RXTXCallback,
    /* Error Callback */
    Can0_Error_Callback
    };
```

## 6. 常见坑

1. **板型宏必须先对**：`component/can/can_config.h` 中 `#define S32K344_EVB_DEMO (STD_OFF)`（当前为白板）。切 EVB 改 `STD_ON` 后整套节点定义（NODE_0/1/2 ↔ NODE_4/5）、DMA 分支全部跟着变（ReadMe.txt 实证）。
2. **换 mex 重新生成的两个雷**（ReadMe.txt 原文实证）：① 切换板型 mex 重新生成时**不要**重新生成 `Lpuart_Lin_Ip_Cfg.h`（RTD bug）；② 白板切 EVB 时应**删除全部 DMA 生成文件**。
3. **轮询节点必须配套 MainFunction**：CAN1/CAN5 发送后要调 `FlexCAN_Ip_MainFunctionWrite`，接收要周期调 `FlexCAN_Ip_MainFunctionRead`，否则 MB 状态机不推进（Can_MainTask 实证）。`FlexCAN_Ip_Receive` 的第 4 参 `isPolling` 决定该 MB 走中断还是轮询。
4. **中断接收的 MB 收完一帧必须在回调里重挂**：`FLEXCAN_EVENT_RX_COMPLETE` 分支对每个 buffIdx 重新调 `FlexCAN_Ip_Receive(..., false)` 复位 MB 为 BUSY，否则只收到第一帧（Can0_MB_RXTXCallback 实证）。增强 FIFO 同理在 `FLEXCAN_EVENT_ENHANCED_RXFIFO_COMPLETE` 里重开 `FlexCAN_Ip_RxFifo`。
5. **改运行配置必须包在 Freeze 里**：掩码、过滤表、TDC 等都在 `EnterFreezeMode`/`ExitFreezeMode` 之间写，且初始化尾部要 `SetStartMode` 才开始收发（三个 Node_Init 实证）。
6. **bus off 手动恢复链路**：Error 回调读 ESR1 确认 `BOFFINT` → 置 `CAN_NODE_x_BusOff_Flag` + `AbortTransfer` 中止在途发送 → 主循环 `MainFunctionBusOff_Privileged` → `Hal_Can_RecoverBusOff` 等 `BOFFDONEINT`（128 次 11 连续隐性位）→ `Deinit` → 按节点重新 Init。开了 `CAN_BUSOFF_RECOVERY_MANUAL`（can_config.h 默认 STD_ON）。
7. **增强 FIFO 过滤表长度与初始化数不一致**：`Enhanced_FIFO_FilterNum` 定义为 4，但 `CAN_EnhancedFIFO_FilterTable` 只显式初始化 3 项（与 `FlexCAN_Config0` 的 2 std + 1 ext 对应），第 4 项零填充；改过滤表时注意同步（can_config.c 第 92-118 行实证）。
8. **legacy FIFO 与 CAN FD 互斥**：can_config.h 原文注释 "legacy fifo can not be activate when enable CANFD"，CAN2 走 legacy FIFO 所以是经典帧（can_config.h 第 160 行实证）。
9. **调试器可能误配 DMA**：main 里 `TCD->CH0_ES = 0x80000001` 先清 DMA 通道错误位，注释明说 "in case lauterbach cmm will initialize DMA mistakely"（main.c 第 62-63 行实证）。
10. **退出主循环靠全局 `exit_code`**：`volatile int exit_code = 0;` 非 0 时 break；示例默认死循环（main.c 第 42/86-89 行实证）。
