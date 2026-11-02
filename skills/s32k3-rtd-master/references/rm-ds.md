# S32K3xx 手册库（RM + DS）检索指南

本 skill 的第二知识源：两份官方手册已转成 markdown 并随 skill 分发在 `docs/NXP_S32K3/`（layout 路径，寄存器位域图保留「png 截图 + 可检索 picture text」双份）。职责分工：**训练库答"怎么写码"，手册库答"寄存器/参数是什么"**。

## 1. 文档位置与分工

| 问题类型 | 查哪里 | 路径（相对 skill 根） |
|---|---|---|
| 寄存器/位域/外设功能/时钟/电源模式/低功耗 | **RM**（119 个模块文件） | `docs/NXP_S32K3/RM/<章>/<编号>_<模块>.md` |
| 电气参数/绝对最大额定/功耗电流/ESD/封装/去耦/热特性 | **DS**（单文件） | `docs/NXP_S32K3/S32K3xxDS_数据手册.md` |
| 外设基地址总表 | RM | `RM/3_Memory_Map/3.7_AIPS-Lite_memory_map.md` |
| 引脚复用/pad | RM | `RM/4_Signal_Multiplexing/4.4_Signal_Multiplexing_sheet.md` |
| 型号差异（312/344/358…） | RM | `RM/2_Introduction/2.5_Feature_comparison.md` |

注意：源 PDF 文件名与内容**交叉**——「S32K3XXRM 数据表.pdf」实为 Reference Manual（4640 页），「S32K3xxDS 参考手册.pdf」实为 Data Sheet（130 页）。markdown 产物已按真实内容命名。

## 2. RM 内部结构与 Grep 模式

每个模块文件结构固定：`x.1 芯片特化信息 → x.2 引言 → x.4 功能描述 → x.7 memory map 与寄存器`。

| 要查 | Grep 模式（在模块文件内） | 命中形态 |
|---|---|---|
| 某寄存器完整描述 | `####.*\b(NSR|MCR|PCR)\b`（换实际缩写） | `#### 46.7.1.2 NMI Status Flag Register (NSR)` |
| 模块基地址 | `base address` | `WKPU base address: 402B_4000h` |
| 全部寄存器偏移/复位值 | 在 memory map 小节 Read 表格 | `\|14h\|...Register (WISR)\|32\|W1C\|0000_0000h\|` |
| 位域定义 | `^Bits ` 或寄存器缩写 | `Bits 31 30 ...` + `R`/`W` + `Reset u u ...` |
| 某信号/通道连接 | 信号名，如 `WKPU[27]`、`EIRQ\[2\]` | 连接表 |
| 跨模块找寄存器 | 先用 `cmd_rm.py <关键词>` 定位模块文件，不要全局 Grep 8.7MB | — |

位域 picture text 紧跟图片引用行，以 `<!-- End of picture text -->` 结束：`Bits 31 30 ... 16` / `R 字段名` / `Reset 0 0 ...`。回答位域用表格搬 picture text 结构；展示图形引用 png。

页脚形如 `1578 / 4640`（PDF 物理页），配合下方地图的页码列可反查定位。

## 3. 图片路径规则（坑）

md 内图片引用为绝对 posix 路径（随 skill 分发后已全部改写到 skill 内）：
`D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/<章>/<模块名清洗后>/<PDF名>-<页码4位>-<序号2位>.png`

模块目录名经过清洗：`(` `)` `[` `]` 与 U+2010~2015/U+2212 → `-`，空格 → `_`。例：`009_System_Integration_Unit_Lite2_(SIUL2).md` 的图在 `009_System_Integration_Unit_Lite2_-SIUL2-/`。DS 的图在 `images_DS/`（目录名无清洗问题）。

## 4. 本工程特化（CDC_7255 = S32K312）

- PMC 三份型号文档，S32K312 用 `RM/Modes_and_Power_Management/042_Power_Management_Controller_(PMC_for_S32K312).md`（不是 041/043）。
- STANDBY 低功耗链查 `044_Mode_Entry_(MC_ME).md` + `046_Wakeup_Unit_(WKPU).md`；工程实证 ACC=PTE2=`WKPU[27]`，唤醒沿=下降沿，唤醒=破坏性复位，唤醒源查 `WKPU->WISR`。
- 时钟链查 `RM/Clocking/024_Clock_Generation_Module_(MC_CGM).md`；standby 用 `Clock_Ip_aClockConfig[1]`（FIRC 48MHz）。
- RTD 驱动 API 用法/写码 → 走本 skill 训练库（TOPIC_RULES + references/<外设>.md）；手册层才查 RM/DS。

## 5. 119 文件地图（页码=PDF 物理页）

## 1_About_This_Manual

| 文件 | 页码 | 标题 |
|---|---|---|
| `1.3_Module_descriptions.md` | 7-9 | 1.3 Module descriptions |
| `1.4_Register_descriptions.md` | 10-10 | 1.4 Register descriptions |
| `1.5_Conventions.md` | 11-12 | 1.5 Conventions |
| `1.7_Glossary.md` | 13-13 | 1.7 Glossary |

## 2_Introduction

| 文件 | 页码 | 标题 |
|---|---|---|
| `2.2_S32K3xx_Series_Introduction.md` | 14-14 | 2.2 S32K3xx Series Introduction |
| `2.3_Feature_summary.md` | 15-19 | 2.3 Feature summary |
| `2.4_Block_diagram.md` | 20-20 | 2.4 Block diagram |
| `2.5_Feature_comparison.md` | 21-24 | 2.5 Feature comparison |
| `2.6_Glossary.md` | 25-25 | 2.6 Glossary |

## 3_Memory_Map

| 文件 | 页码 | 标题 |
|---|---|---|
| `3.3_Access-related_details_of_the_memory_types_used_in_this_chip.md` | 26-26 | 3.3 Access-related details of the memory types used in this chip |
| `3.7_AIPS-Lite_memory_map.md` | 27-27 | 3.7 AIPS-Lite memory map |
| `3.9_PPB_memory_map.md` | 28-28 | 3.9 PPB memory map |
| `3.10_Glossary.md` | 29-29 | 3.10 Glossary |

## 4_Signal_Multiplexing

| 文件 | 页码 | 标题 |
|---|---|---|
| `4.2_Pad_description.md` | 30-31 | 4.2 Pad description |
| `4.4_Signal_Multiplexing_sheet.md` | 32-34 | 4.4 Signal Multiplexing sheet |
| `4.5_Pin_States.md` | 35-39 | 4.5 Pin States |
| `4.6_Glossary.md` | 40-41 | 4.6 Glossary |

## Core_and_Systems

| 文件 | 页码 | 标题 |
|---|---|---|
| `005_Cortex-M7_Overview.md` | 42-46 | 5 Cortex-M7 Overview |
| `006_Miscellaneous_Control_Module_(MCM).md` | 47-65 | 6 Miscellaneous Control Module (MCM) |
| `007_Miscellaneous_System_Control_Module_(MSCM).md` | 66-122 | 7 Miscellaneous System Control Module (MSCM) |
| `008_Virtualization_Wrapper_(VIRT_WRAPPER).md` | 123-214 | 8 Virtualization Wrapper (VIRT_WRAPPER) |
| `009_System_Integration_Unit_Lite2_(SIUL2).md` | 215-367 | 9 System Integration Unit Lite2 (SIUL2) |
| `010_Touch_Sensing_Pin_Coupling_(TSPC).md` | 368-376 | 10 Touch Sensing Pin Coupling (TSPC) |
| `011_Crossbar_Switch_(AXBS).md` | 377-391 | 11 Crossbar Switch (AXBS) |
| `012_Peripheral_Bridge_(AIPS_Lite).md` | 392-393 | 12 Peripheral Bridge (AIPS_Lite) |
| `013_Direct_Memory_Access_Multiplexer_(DMAMUX).md` | 394-404 | 13 Direct Memory Access Multiplexer (DMAMUX) |
| `014_Enhanced_Direct_Memory_Access_(eDMA).md` | 405-507 | 14 Enhanced Direct Memory Access (eDMA) |
| `015_Interrupt_Monitor_(INTM).md` | 508-515 | 15 Interrupt Monitor (INTM) |
| `016_Semaphores2_(SEMA42).md` | 516-524 | 16 Semaphores2 (SEMA42) |
| `017_Crossbar_Integrity_Checker_(XBIC).md` | 525-543 | 17 Crossbar Integrity Checker (XBIC) |
| `018_Extended_Resource_Domain_Controller_(XRDC).md` | 544-624 | 18 Extended Resource Domain Controller (XRDC) |

## Memories_and_Memory_Overview

| 文件 | 页码 | 标题 |
|---|---|---|
| `019_Memory_and_Memory_Interfaces.md` | 625-632 | 19 Memory and Memory Interfaces |
| `020_Embedded_Flash_Memory_(c40asf).md` | 633-706 | 20 Embedded Flash Memory (c40asf) |
| `021_Flash_Memory_Controller_(PFLASH).md` | 707-733 | 21 Flash Memory Controller (PFLASH) |
| `022_RAM_Controller_(PRAMC).md` | 734-739 | 22 RAM Controller (PRAMC) |

## Clocking

| 文件 | 页码 | 标题 |
|---|---|---|
| `023_Clocking.md` | 740-815 | 23 Clocking |
| `024_Clock_Generation_Module_(MC_CGM).md` | 816-920 | 24 Clock Generation Module (MC_CGM) |
| `025_Fast_Internal_RC_Oscillator_(FIRC).md` | 921-923 | 25 Fast Internal RC Oscillator (FIRC) |
| `026_Slow_Internal_RC_Oscillator_(SIRC).md` | 924-926 | 26 Slow Internal RC Oscillator (SIRC) |
| `027_Fast_Crystal_Oscillator_Digital_Controller_(FXOSC).md` | 927-932 | 27 Fast Crystal Oscillator Digital Controller (FXOSC) |
| `028_Slow_Crystal_Oscillator_Digital_Controller_(SXOSC).md` | 933-936 | 28 Slow Crystal Oscillator Digital Controller (SXOSC) |
| `029_PLL_Digital_Interface_(PLLDIG).md` | 937-953 | 29 PLL Digital Interface (PLLDIG) |

## Reset_and_Boot

| 文件 | 页码 | 标题 |
|---|---|---|
| `030_Reset_Overview.md` | 954-978 | 30 Reset Overview |
| `031_Boot_Overview.md` | 979-1004 | 31 Boot Overview |
| `032_Reset_Generation_Module_(MC_RGM).md` | 1005-1033 | 32 Reset Generation Module (MC_RGM) |
| `033_Power-on_Reset_Watchdog_(POR_WDG).md` | 1034-1036 | 33 Power-on Reset Watchdog (POR_WDG) |

## Security_and_Device_GPRs

| 文件 | 页码 | 标题 |
|---|---|---|
| `034_Security_Overview.md` | 1037-1038 | 34 Security Overview |
| `035_Hardware_Security_Engine_(HSE_B).md` | 1039-1061 | 35 Hardware Security Engine (HSE_B) |
| `036_Device_Configuration_Format_(DCF)_records.md` | 1062-1066 | 36 Device Configuration Format (DCF) records |
| `037_Device_Configuration_Module_General-Purpose_Registers_(DCM_GPR).md` | 1067-1196 | 37 Device Configuration Module General-Purpose Registers (DCM_GPR) |
| `038_Device_Configuration_Module_(DCM).md` | 1197-1242 | 38 Device Configuration Module (DCM) |
| `039_Messaging_Unit_(MU).md` | 1243-1379 | 39 Messaging Unit (MU) |

## Modes_and_Power_Management

| 文件 | 页码 | 标题 |
|---|---|---|
| `040_Power_Management.md` | 1380-1400 | 40 Power Management |
| `041_Power_Management_Controller_(PMC_for_S32K34x,_S32K32x_and_S32K314).md` | 1401-1412 | 41 Power Management Controller (PMC for S32K34x, S32K32x and S32K314) |
| `042_Power_Management_Controller_(PMC_for_S32K312).md` | 1413-1425 | 42 Power Management Controller (PMC for S32K312) |
| `043_Power_Management_Controller_(PMC_for_S32K358).md` | 1426-1440 | 43 Power Management Controller (PMC for S32K358) |
| `044_Mode_Entry_Module_(MC_ME).md` | 1441-1567 | 44 Mode Entry Module (MC_ME) |
| `045_Power_Control_Unit_(MC_PCU).md` | 1568-1570 | 45 Power Control Unit (MC_PCU) |
| `046_Wakeup_Unit_(WKPU).md` | 1571-1596 | 46 Wakeup Unit (WKPU) |

## Safety

| 文件 | 页码 | 标题 |
|---|---|---|
| `047_Safety_Overview.md` | 1597-1606 | 47 Safety Overview |
| `048_Error_Injection_Module_(EIM).md` | 1607-1671 | 48 Error Injection Module (EIM) |
| `049_Error_Reporting_Module_(ERM).md` | 1672-1717 | 49 Error Reporting Module (ERM) |
| `050_Fault_Collection_and_Control_Unit_(FCCU).md` | 1718-1777 | 50 Fault Collection and Control Unit (FCCU) |
| `051_Self-test_General-Purpose_Registers_(SELFTEST_GPR).md` | 1778-1781 | 51 Self-test General-Purpose Registers (SELFTEST_GPR) |
| `052_Self-Test_Control_Unit_(STCU2).md` | 1782-1832 | 52 Self-Test Control Unit (STCU2) |
| `053_Register_Protection_(REG_PROT).md` | 1833-1844 | 53 Register Protection (REG_PROT) |
| `054_Clock_Monitoring_Unit_–_Frequency_Check_(CMU_FC).md` | 1845-1859 | 54 Clock Monitoring Unit – Frequency Check (CMU_FC) |
| `055_Clock_Monitoring_Unit_–_Frequency_Meter_(CMU_FM).md` | 1860-1867 | 55 Clock Monitoring Unit – Frequency Meter (CMU_FM) |
| `056_Cyclic_Redundancy_Check_(CRC).md` | 1868-1878 | 56 Cyclic Redundancy Check (CRC) |

## Real-time_control

| 文件 | 页码 | 标题 |
|---|---|---|
| `057_Power_Conversion_and_Motor_Control_(PCMC).md` | 1879-1895 | 57 Power Conversion and Motor Control (PCMC) |
| `058_Analog-to-Digital_Converter_(ADC).md` | 1896-2057 | 58 Analog-to-Digital Converter (ADC) |
| `059_Low_Power_Comparator_(LPCMP).md` | 2058-2097 | 59 Low Power Comparator (LPCMP) |
| `060_Logic_Control_Unit_(LCU).md` | 2098-2173 | 60 Logic Control Unit (LCU) |
| `061_Enhanced_Modular_IO_Subsystem_(eMIOS).md` | 2174-2261 | 61 Enhanced Modular IO Subsystem (eMIOS) |
| `062_Body_Cross-triggering_Unit_(BCTU).md` | 2262-2299 | 62 Body Cross-triggering Unit (BCTU) |
| `063_Trigger_MUX_(TRGMUX).md` | 2300-2361 | 63 Trigger MUX (TRGMUX) |

## Timer

| 文件 | 页码 | 标题 |
|---|---|---|
| `064_Software_Watchdog_Timer_(SWT).md` | 2362-2377 | 64 Software Watchdog Timer (SWT) |
| `065_System_Timer_Module_(STM).md` | 2378-2386 | 65 System Timer Module (STM) |
| `066_Periodic_Interrupt_Timer_(PIT).md` | 2387-2407 | 66 Periodic Interrupt Timer (PIT) |
| `067_Real_Time_Clock_(RTC).md` | 2408-2420 | 67 Real Time Clock (RTC) |

## Communication

| 文件 | 页码 | 标题 |
|---|---|---|
| `068_Low_Power_Serial_Peripheral_Interface_(LPSPI).md` | 2421-2470 | 68 Low Power Serial Peripheral Interface (LPSPI) |
| `069_Low_Power_Inter-Integrated_Circuit_(LPI2C).md` | 2471-2529 | 69 Low Power Inter-Integrated Circuit (LPI2C) |
| `070_Improved_Inter-Integrated_Circuit_(I3C).md` | 2530-2638 | 70 Improved Inter-Integrated Circuit (I3C) |
| `071_Flexible_I_O_(FlexIO).md` | 2639-2715 | 71 Flexible I/O (FlexIO) |
| `072_CAN_(FlexCAN).md` | 2716-2891 | 72 CAN (FlexCAN) |
| `073_Synchronous_Audio_Interface_(SAI).md` | 2892-2939 | 73 Synchronous Audio Interface (SAI) |
| `074_Ethernet_Media_Access_Controller_(EMAC)_part1.md` | 2940-3136 | 74 Ethernet Media Access Controller (EMAC) (part 1) |
| `074_Ethernet_Media_Access_Controller_(EMAC)_part2.md` | 3137-3333 | 74 Ethernet Media Access Controller (EMAC) (part 2) |
| `074_Ethernet_Media_Access_Controller_(EMAC)_part3.md` | 3334-3528 | 74 Ethernet Media Access Controller (EMAC) (part 3) |
| `075_Gigabit_Ethernet_Media_Access_Controller_(GMAC)_part1.md` | 3529-3699 | 75 Gigabit Ethernet Media Access Controller (GMAC) (part 1) |
| `075_Gigabit_Ethernet_Media_Access_Controller_(GMAC)_part2.md` | 3700-3870 | 75 Gigabit Ethernet Media Access Controller (GMAC) (part 2) |
| `075_Gigabit_Ethernet_Media_Access_Controller_(GMAC)_part3.md` | 3871-4041 | 75 Gigabit Ethernet Media Access Controller (GMAC) (part 3) |
| `075_Gigabit_Ethernet_Media_Access_Controller_(GMAC)_part4.md` | 4042-4210 | 75 Gigabit Ethernet Media Access Controller (GMAC) (part 4) |
| `076_Low_Power_Universal_Asynchronous_Receiver_Transmitter_(LPUART).md` | 4211-4287 | 76 Low Power Universal Asynchronous Receiver/Transmitter (LPUART) |
| `077_Quad_Serial_Peripheral_Interface_(QuadSPI).md` | 4288-4429 | 77 Quad Serial Peripheral Interface (QuadSPI) |
| `078_Ultra_Secured_Digital_Host_Controller_(uSDHC).md` | 4430-4547 | 78 Ultra Secured Digital Host Controller (uSDHC) |

## Debug

| 文件 | 页码 | 标题 |
|---|---|---|
| `079_Debug_Subsystem.md` | 4548-4592 | 79 Debug Subsystem |
| `080_JTAG_Controller_(JTAGC).md` | 4593-4601 | 80 JTAG Controller (JTAGC) |
| `081_JTAG_Data_Communication_(JDC).md` | 4602-4610 | 81 JTAG Data Communication (JDC) |

## Analog

| 文件 | 页码 | 标题 |
|---|---|---|
| `082_Temperature_Sensor_(TempSense).md` | 4611-4617 | 82 Temperature Sensor (TempSense) |

## A_General_Changes

| 文件 | 页码 | 标题 |
|---|---|---|
| `A.1_General_changes.md` | 4618-4618 | A.1 General changes |

## B_Release_notes

| 文件 | 页码 | 标题 |
|---|---|---|
| `Miscellaneous_System_Control_Module_(MSCM).md` | 4619-4619 |  Miscellaneous System Control Module (MSCM) |
| `System_Integration_Unit_Lite2_(SIUL2).md` | 4620-4620 |  System Integration Unit Lite2 (SIUL2) |
| `Direct_Memory_Access_Multiplexer_(DMAMUX).md` | 4621-4621 |  Direct Memory Access Multiplexer (DMAMUX) |
| `Extended_Resource_Domain_Controller_(XRDC).md` | 4622-4622 |  Extended Resource Domain Controller (XRDC) |
| `Clock_Generation_Module_(MC_CGM).md` | 4623-4623 |  Clock Generation Module (MC_CGM) |
| `B.31_Boot_Overview_changes.md` | 4624-4624 | B.31 Boot Overview changes |
| `B.37_Chip-specific_DCM_information_changes.md` | 4625-4625 | B.37 Chip-specific DCM information changes |
| `B.43_PMC_changes.md` | 4626-4626 | B.43 PMC changes |
| `Error_Reporting_Module_(ERM).md` | 4627-4627 |  Error Reporting Module (ERM) |
| `Register_Protection_(REG_PROT).md` | 4628-4628 |  Register Protection (REG_PROT) |
| `B.57_PCMC_changes.md` | 4629-4629 | B.57 PCMC changes |
| `Enhanced_Modular_IO_Subsystem_(eMIOS).md` | 4630-4630 |  Enhanced Modular IO Subsystem (eMIOS) |
| `System_Timer_Module_(STM).md` | 4631-4631 |  System Timer Module (STM) |
| `Low_Power_Inter-Integrated_Circuit_(LPI2C).md` | 4632-4632 |  Low Power Inter-Integrated Circuit (LPI2C) |
| `Improved_Inter-Integrated_Circuit_(I3C).md` | 4633-4633 |  Improved Inter-Integrated Circuit (I3C) |
| `Synchronous_Audio_Interface_(SAI).md` | 4634-4634 |  Synchronous Audio Interface (SAI) |
| `Quad_Serial_Peripheral_Interface_(QuadSPI).md` | 4635-4636 |  Quad Serial Peripheral Interface (QuadSPI) |
| `B.82_TEMPSENSE_module_changes.md` | 4637-4640 | B.82 TEMPSENSE module changes |
