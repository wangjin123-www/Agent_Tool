NXP Semiconductors 

# Chapter 6 Miscellaneous Control Module (MCM) 

## 6.1 Chip-specific MCM information 

### 6.1.1 MCM instances and configuration 

This chip supports up to three instances of MCM: 

- MCM_0 

- MCM_1 

- MCM_2 

Table 29. MCM instances 

|Instances|S32K358|S32K322/S32K324/S32K344/S32K342|S32K312/S32K311/S32K314|
|---|---|---|---|
|MCM_0|Yes|Yes|Yes|
|MCM_1|Yes|Yes|No|
|MCM_2|Yes|No|No|



Table 30. Memories 

|Memory|Single core CM7_0 and<br>CM7_1|Dual core CM7_0 and<br>CM7_1|CM7_2 core Single<br>Only in S32K358|Lockstep for CM7_0<br>and CM7_1|
|---|---|---|---|---|
|Icache|16 KB|16 KB (per core)|16 KB|16 KB|
|Dcache|16 KB|16 KB (per core)|16 KB|16 KB|
|ITCM|32 KB|32 KB (per core)|64 KB|64 KB|
|DTCM|64 KB|64 KB (per core)|128 KB|128 KB|



## 6.2 Introduction 

The Miscellaneous Control Module (MCM) provides miscellaneous control functions and contains Cortex-M7 local memory descriptors. For more information on core related registers, refer to CM7 overview chapter. 

### 6.2.1 Features 

The MCM includes the following features: 

- Program-visible information on the platform configuration and revision 

- Floating Point Exception monitor and interrupt control 

- Local memory descriptors: 

   - ITCM 

   - D0TCM 

   - D1TCM 

   - ICACHE 

   - DCACHE 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

47 / 4640 

NXP Semiconductors 

Miscellaneous Control Module (MCM) 

## 6.3 Functional description 

### 6.3.1 Interrupts 

MCM generates an interrupt if any of the following are true: 

- FPU input denormal interrupt is enabled (FIDCE) and an input is denormalized (FIDC). 

- FPU inexact interrupt is enabled (FIXCE) and a number is inexact (FIXC). 

- FPU underflow interrupt is enabled (FUFCE) and an underflow occurs (FUFC). 

- FPU overflow interrupt is enabled (FOFCE) and an overflow occurs (FOFC). 

- FPU divide-by-zero interrupt is enabled (FDZCE) and a divide-by-zero occurs (FDZC). 

- FPU invalid operation interrupt is enabled (FDZCE) and an invalid operation occurs (FDZC). 

- Write abort interrupt is enabled (WABE) and a write abort occurs (CM7 WABORTS INDICATOR). 

##### Determining interrupt source 

To determine the exact source of the interrupt for Cortex-M7 core, qualify the interrupt status flags with the corresponding interrupt enable fields. 

- MCM_ISCR[31:16] && MCM_ISCR[15:0] 

- Search the result for asserted flags, which indicate the exact interrupt sources. 

## 6.4 Memory map/register descriptions 

The memory map and register descriptions below describe the registers using byte addresses. 

~~<mark>NOTE</mark>~~ Writing in read-only registers at 0x0 results in a bus error. 

### 6.4.1 MCM register descriptions 

#### 6.4.1.1 MCM memory map 

MCM_0_CM7 base address: E008_0000h 

MCM_1_CM7 base address: E008_0000h 

MCM_2_CM7 base address: E008_0000h 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|0h|SoC-defined Platform Revision (PLREV)|16|RO|0000h|
|2h|Processor Core Type (PCT)|16|RO|AC70h|
|Ch|Core Platform Control (CPCR)|32|RW|0000_0200h|
|10h|Interrupt Status and Control (ISCR)|32|RW|0000_0000h|
|400h|Local Memory Descriptor 0 (LMEM_DESC_0)|32|RW|See<br>description|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

48 / 4640 

NXP Semiconductors 

Miscellaneous Control Module (MCM) 

##### Table continued from the previous page... 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|404h - 408h|Local Memory Descriptor a (LMEM_DESC_1 - LMEM_DESC_2)|32|RW|See<br>description|
|40Ch|Local Memory Descriptor 3 (LMEM_DESC_3)|32|RW|8526_4000h|
|410h|Local Memory Descriptor 4 (LMEM_DESC_4)|32|RW|8544_6000h|



#### 6.4.1.2 SoC-defined Platform Revision (PLREV) 

##### Offset 

|Register|Offset|
|---|---|
|PLREV|0h|



##### Function 

The PLREV is a 16-bit read-only register specifying an SoC-defined platform revision number. The state of this register is defined by a platform input signal; it can only be read from the IPS programming model. Any attempted write is ignored. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/006_Miscellaneous_Control_Module_-MCM-/S32K3XXRM_数据表.pdf-0049-10.png)


<!-- Start of picture text -->
Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R PLREV<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|15-0|The PLREV[15:0] field is specified by a platform input signal to define a software-visible revision number.|
|PLREV||



#### 6.4.1.3 Processor Core Type (PCT) 

##### Offset 

|Register|Offset|
|---|---|
|PCT|2h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

49 / 4640 

NXP Semiconductors 

Miscellaneous Control Module (MCM) 

##### Function 

The PCT is a 16-bit read-only register specifying the architecture of the processor core within the platform on the device. The state of this register is defined by a module input signal, which can only be read from the IPS programming model. Any attempted write is ignored. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/006_Miscellaneous_Control_Module_-MCM-/S32K3XXRM_数据表.pdf-0050-05.png)


<!-- Start of picture text -->
Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R PCT<br>W<br>Reset 1 0 1 0 1 1 0 0 0 1 1 1 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|15-0|This MCM design supports the Arm Cortex M7 core. The following value identifies this core complex.|
|PCT|1010_1100_0111_0000b - Arm Cortex M7|



#### 6.4.1.4 Core Platform Control (CPCR) 

##### Offset 

|Register|Offset|
|---|---|
|CPCR|Ch|



##### Function 

CR defines the arbitration and protection schemes for the two system RAM arrays. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/006_Miscellaneous_Control_Module_-MCM-/S32K3XXRM_数据表.pdf-0050-14.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R CM7_A<br>Reserved  Reserved<br>W HB...<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv Reserv<br>R Reserved<br>ed  ed<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

50 / 4640 

NXP Semiconductors 

Miscellaneous Control Module (MCM) 

##### Fields 

|Field|Function|
|---|---|
|31-28<br>—<br>27<br>CM7_AHBSPRI|Reserved<br>AHB Slave Priority<br>This field indicates the access priority on the AHBS port of the Cortex-M7.<br>This setting has no effect unless enabled by AHBSCR[CTL]<sup>1</sup>of the CM7 core.<br>~~NOTE~~<br>0b - Uses a round-robin arbitration scheme<br>1b - AHB-slave access has priority over a core access|
|26-11<br>—|Reserved|
|10<br>—|Reserved|
|9<br>—|Reserved|
|8-0<br>—|Reserved|



1. For more information see Cortex-M7 documentation: Arm Cortex-M7 Processor Technical Reference Manual at www.arm.com. 

#### 6.4.1.5 Interrupt Status and Control (ISCR) 

##### Offset 

|Register|Offset|
|---|---|
|ISCR|10h|



##### Function 

The MCM_ISCR register defines the configuration of, and reports status for, a number of core-related interrupt exception conditions. It includes: 

- Enable and status fields associated with the core's floating-point exceptions 

- Bus errors associated with the core's cache write buffer 

The individual event indicators are first qualified with their exception enables, and then logically summed to form an interrupt request sent to the core's NVIC. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

51 / 4640 

NXP Semiconductors 

Miscellaneous Control Module (MCM) 

Bits 15-8 are read-only indicator flags based on the processor's FPSCR register. Attempted writes to these fields are ignored. When these flags are 1, they retain this value until software clears the corresponding FPSCR field. For more information see Cortex-M7 documentation: Arm Cortex-M7 Processor Technical Reference Manual at www.arm.com. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|FIDCE|0||FIXCE|FUFC|FOFC|FDZC|FIOCE||0|WABE|||0|||
|W|||||E|E|E||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|FIDC|0||FIXC|FUFC|FOFC|FDZC|FIOC|0|WABS<br>O|WABS|||0|||
|W|||||||||||W1C||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31<br>FIDCE|FPU Input Denormal Interrupt Enable<br>0b - Disable interrupt<br>1b - Enable interrupt|
|30-29<br>—|Reserved|
|28<br>FIXCE|FPU Inexact Interrupt Enable<br>0b - Disable interrupt<br>1b - Enable interrupt|
|27<br>FUFCE|FPU Underflow Interrupt Enable<br>0b - Disable interrupt<br>1b - Enable interrupt|
|26<br>FOFCE|FPU Overflow Interrupt Enable<br>0b - Disable interrupt<br>1b - Enable interrupt|
|25<br>FDZCE|FPU Divide-by-Zero Interrupt Enable<br>0b - Disable interrupt<br>1b - Enable interrupt|
|24<br>FIOCE|FPU Invalid Operation Interrupt Enable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

52 / 4640 

NXP Semiconductors 

Miscellaneous Control Module (MCM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Disable interrupt<br>1b - Enable interrupt|
|23-22<br>—|Reserved|
|21<br>WABE|TCM Write Abort Interrupt Enable<br>0b - Disable interrupt<br>1b - Enable Interrupt|
|20-16<br>—|Reserved|
|15<br>FIDC|FPU Input Denormal Interrupt Status<br>This read-only field is a copy of the core's FPSCR[IDC] field. It indicates that an input denormalized<br>number has been detected in the processor's FPU. When this field is 1, it retains this value until software<br>clears the FPSCR[IDC] field.<br>0b - No interrupt<br>1b - Interrupt occurred|
|14-13<br>—|Reserved|
|12<br>FIXC|FPU Inexact Interrupt Status<br>This read-only field is a copy of the core's FPSCR[IXC] field. It indicates that an inexact number has<br>been detected in the processor's FPU. When this field is 1, it retains this value until software clears the<br>FPSCR[IXC] field.<br>0b - No interrupt<br>1b - Interrupt occurred|
|11<br>FUFC|FPU Underflow Interrupt Status<br>This read-only field is a copy of the core's FPSCR[UFC] field. It indicates that an underflow has been<br>detected in the processor's FPU. When this field is 1, it retains this value until software clears the<br>FPSCR[UFC] field.<br>0b - No interrupt<br>1b - Interrupt occurred|
|10<br>FOFC|FPU Overflow Interrupt Status<br>This read-only field is a copy of the core's FPSCR[OFC] field. It indicates that an overflow has been<br>detected in the processor's FPU. When this field is 1, it retains this value until software clears the<br>FPSCR[OFC] field.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

53 / 4640 

NXP Semiconductors 

Miscellaneous Control Module (MCM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - No interrupt<br>1b - Interrupt occurred|
|9<br>FDZC|FPU Divide-by-Zero Interrupt Status<br>This read-only field is a copy of the core's FPSCR[DZC] field. It indicates that a divide-by-zero operation<br>has been detected in the processor's FPU. When this field is 1, it retains this value until software clears<br>the FPSCR[DZC] field.<br>0b - No interrupt<br>1b - Interrupt occurred|
|8<br>FIOC|FPU Invalid Operation Interrupt Status<br>This read-only field is a copy of the core's FPSCR[IOC] field. It indicates that an illegal operation has<br>been detected in the processor's FPU. When this field is 1, it retains this value until software clears the<br>FPSCR[IOC] field.<br>0b - No interrupt<br>1b - Interrupt occurred|
|7<br>|Reserved|
|—<br>6<br>WABSO|Write Abort on Slave Overrun<br>The overrun conditions are reported only if WABE=1.<br>0b - No write abort overrun<br>1b - Write abort overrun occurred|
|5<br>WABS|Write Abort on Slave<br>This field indicates when a write abort has occurred on the AHBS interface.<br>0b - No write abort occurred on AHBS interface<br>1b - Write abort occurred on AHBS interface|
|4-0<br>—|Reserved|



#### 6.4.1.6 Local Memory Descriptor 0 (LMEM_DESC_0) 

##### Offset 

|Register|Offset|
|---|---|
|LMEM_DESC_0|400h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

54 / 4640 

NXP Semiconductors 

Miscellaneous Control Module (MCM) 

##### Function 

~~<mark>NOTE</mark>~~ 

The DESC_a registers map to the LMEMs like this: 

- DESC_0: ITCM 

- DESC_1: D0TCM 

- DESC_2: D1TCM 

- DESC_3: ICACHE 

- DESC_4: DCACHE 

~~<mark>NOTE</mark>~~ 

The reserved bits can be read and written (instead of read as zero and write ignored). Setting any of these bits does not have any functional impact. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/006_Miscellaneous_Control_Module_-MCM-/S32K3XXRM_数据表.pdf-0055-13.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>LMSZ<br>R LMV  LMSZ  WY  DPW<br>H  Reserv<br>Reserved<br>ed<br>W<br>Reset See Register reset values.<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R MT  Reserved<br>Reserved  Reserved<br>W<br>Reset See Register reset values.Register reset values..<br><!-- End of picture text -->

See Register reset values.Register reset values.. 

##### Register reset values 

|Register|Reset value|
|---|---|
|LMEM_DESC_0|MCM_0_CM7,MCM_1_CM7: 8606_0000h|
||MCM_2_CM7: 8706_0000h|



##### Fields 

|Field|Function|
|---|---|
|31|Local Memory Valid|
|LMV|This read-only field defines the validity (presence) of the local memory.|
||0b - LMEMn not present|
||1b - LMEMn present|
|30-29|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

55 / 4640 

NXP Semiconductors 

Miscellaneous Control Module (MCM) 

Table continued from the previous page... 

|Field<br>|Function|
|---|---|
|—<br>28|LMEM Size Hole|
|LMSZH|This field is used for local memories that are not fully populated (that is, local memories that include a<br>memory "hole" in the upper 25 % of the address range).<br>0b - LMEMn is a power-of-2 capacity<br>1b - LMEMn is not a power-of-2, with capacity of 0.75 x LMSZ|
|27-24<br>LMSZ|Local Memory Size<br>0000b - 0 KB<br>0001b - 1 KB<br>0010b - 2 KB|
||0011b - 4 KB|
||0100b - 8 KB|
||0101b - 16 KB|
||0110b - 32 KB<br>0111b - 64 KB|
||1000b - 128 KB<br>1001b - 256 KB|
||1010b - 512 KB|
||1011b - 1024 KB|
||1100b - 2048 KB|
||1101b - 4096 KB<br>1110b - 8192 KB|
||1111b - 16384 KB|
|23-20<br>WY|Level 1 Cache Ways<br>0000b - No cache<br>0010b - 2-way set associative|
||0100b - 4-way set associative|
|19-17|Data Path Width|
|DPW|LMEM data path width. This read-only field defines the width of the local memory.<br>000b-001b - Reserved<br>010b - LMEMn is 32-bits wide|
||011b - LMEMn is 64-bits wide<br>100b-111b - Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

56 / 4640 

NXP Semiconductors 

Miscellaneous Control Module (MCM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|16<br>—|Reserved|
|15-13|Memory Type|
|MT|000b - ITCM<br>001b - DTCM|
||010b - ICACHE|
||011b - DCACHE|
|12-4<br>—|Reserved|
|3-2<br>—|Reserved|
|1-0<br>—|Reserved|



#### 6.4.1.7 Local Memory Descriptor a (LMEM_DESC_1 - LMEM_DESC_2) 

##### Offset 

|Register|Offset|
|---|---|
|LMEM_DESC_1|404h|
|LMEM_DESC_2|408h|



Function 

- ~~<mark>NOTE</mark>~~ 

- The DESC_a registers map to the LMEMs like this: • DESC_0: ITCM • DESC_1: D0TCM • DESC_2: D1TCM • DESC_3: ICACHE • DESC_4: DCACHE 

~~<mark>NOTE</mark>~~ 

The reserved bits can be read and written (instead of read as zero and write ignored). Setting any of these bits does not have any functional impact. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

57 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/006_Miscellaneous_Control_Module_-MCM-/S32K3XXRM_数据表.pdf-0058-01.png)


<!-- Start of picture text -->
Miscellaneous Control Module (MCM)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>LMSZ<br>R LMV  LMSZ  WY  DPW<br>H  Reserv<br>Reserved<br>ed<br>W<br>Reset See Register reset values.<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R MT  Reserved<br>Reserved  Reserved<br>W<br>Reset See Register reset values.<br><!-- End of picture text -->

##### Register reset values 

|Register|Reset value|
|---|---|
|LMEM_DESC_1–LMEM_DESC_2|MCM_0_CM7,MCM_1_CM7: 8604_2000h|
||MCM_2_CM7: 8704_2000h|



##### Fields 

|Field|Function|
|---|---|
|31<br>LMV|Local Memory Valid<br>This read-only field defines the validity (presence) of the local memory.<br>0b - LMEMn not present<br>1b - LMEMn present|
|30-29<br>—|Reserved|
|28|LMEM Size Hole|
|LMSZH|This field is used for local memories that are not fully populated (that is, local memories that include a<br>memory "hole" in the upper 25 % of the address range).<br>0b - LMEMn is a power-of-2 capacity<br>1b - LMEMn is not a power-of-2, with capacity of 0.75 x LMSZ|
|27-24<br>LMSZ|Local Memory Size<br>0000b - 0 KB<br>0001b - 1 KB<br>0010b - 2 KB<br>0011b - 4 KB|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

58 / 4640 

NXP Semiconductors 

Miscellaneous Control Module (MCM) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0100b - 8 KB<br>0101b - 16 KB<br>0110b - 32 KB<br>0111b - 64 KB<br>1000b - 128 KB<br>1001b - 256 KB<br>1010b - 512 KB<br>1011b - 1024 KB<br>1100b - 2048 KB<br>1101b - 4096 KB<br>1110b - 8192 KB<br>1111b - 16384 KB|
|23-20<br>WY|Level 1 Cache Ways<br>0000b - No cache<br>0010b - 2-way set associative<br>0100b - 4-way set associative|
|19-17<br>DPW|Data Path Width<br>LMEM data path width. This read-only field defines the width of the local memory.<br>000b-001b - Reserved<br>010b - LMEMn is 32-bits wide<br>011b - LMEMn is 64-bits wide<br>100b-111b - Reserved|
|16<br>—|Reserved|
|15-13<br>MT|Memory Type<br>000b - ITCM<br>001b - DTCM<br>010b - ICACHE<br>011b - DCACHE|
|12-4<br>—|Reserved|
|3-2|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

59 / 4640 

NXP Semiconductors 

Miscellaneous Control Module (MCM) 

##### Table continued from the previous page... 

|Field<br>—<br>1-0<br>—|Function<br>Reserved|
|---|---|



#### 6.4.1.8 Local Memory Descriptor 3 (LMEM_DESC_3) 

##### Offset 

|Register|Offset|
|---|---|
|LMEM_DESC_3|40Ch|



##### Function 

~~<mark>NOTE</mark>~~ 

The DESC_a registers map to the LMEMs like this: 

- DESC_0: ITCM 

- DESC_1: D0TCM 

- DESC_2: D1TCM 

- DESC_3: ICACHE 

- DESC_4: DCACHE 

~~<mark>NOTE</mark>~~ 

The reserved bits can be read and written (instead of read as zero and write ignored). Setting any of these bits does not have any functional impact. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/006_Miscellaneous_Control_Module_-MCM-/S32K3XXRM_数据表.pdf-0060-18.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>LMSZ<br>R LMV  LMSZ  WY  DPW<br>H  Reserv<br>Reserved<br>ed<br>W<br>Reset 1 0 0 0 0 1 0 1 0 0 1 0 0 1 1 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R MT  Reserved<br>Reserved  Reserved<br>W<br>Reset 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

60 / 4640 

NXP Semiconductors 

Miscellaneous Control Module (MCM) 

##### Fields 

|Field|Function|
|---|---|
|31|Local Memory Valid|
|LMV|This read-only field defines the validity (presence) of the local memory.<br>0b - LMEMn not present<br>1b - LMEMn present|
|30-29<br>—|Reserved|
|28<br>LMSZH|LMEM Size Hole<br>This field is used for local memories that are not fully populated (that is, local memories that include a<br>memory "hole" in the upper 25 % of the address range).<br>0b - LMEMn is a power-of-2 capacity<br>1b - LMEMn is not a power-of-2, with capacity of 0.75 x LMSZ|
|27-24<br>LMSZ|Local Memory Size<br>0000b - 0 KB<br>0001b - 1 KB|
||0010b - 2 KB<br>0011b - 4 KB<br>0100b - 8 KB<br>0101b - 16 KB<br>0110b - 32 KB|
||0111b - 64 KB<br>1000b - 128 KB|
||1001b - 256 KB<br>1010b - 512 KB<br>1011b - 1024 KB<br>1100b - 2048 KB<br>1101b - 4096 KB<br>1110b - 8192 KB<br>1111b - 16384 KB|
|23-20<br>WY|Level 1 Cache Ways<br>0000b - No cache<br>0010b - 2-way set associative|
||0100b - 4-way set associative|
|19-17|Data Path Width|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

61 / 4640 

NXP Semiconductors 

Miscellaneous Control Module (MCM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|DPW|LMEM data path width. This read-only field defines the width of the local memory.<br>000b-001b - Reserved<br>010b - LMEMn is 32-bits wide<br>011b - LMEMn is 64-bits wide<br>100b-111b - Reserved|
|16<br>—|Reserved|
|15-13<br>MT|Memory Type<br>000b - ITCM<br>001b - DTCM<br>010b - ICACHE<br>011b - DCACHE|
|12-4<br>—|Reserved|
|3-2<br>—|Reserved|
|1-0<br>—|Reserved|



#### 6.4.1.9 Local Memory Descriptor 4 (LMEM_DESC_4) 

##### Offset 

|Register|Offset|
|---|---|
|LMEM_DESC_4|410h|



Function 

- ~~<mark>NOTE</mark>~~ 

- The DESC_a registers map to the LMEMs like this: • DESC_0: ITCM • DESC_1: D0TCM • DESC_2: D1TCM • DESC_3: ICACHE • DESC_4: DCACHE 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

62 / 4640 

NXP Semiconductors 

Miscellaneous Control Module (MCM) 

~~<mark>NOTE</mark>~~ 

The reserved bits can be read and written (instead of read as zero and write ignored). Setting any of these bits does not have any functional impact. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/006_Miscellaneous_Control_Module_-MCM-/S32K3XXRM_数据表.pdf-0063-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>LMSZ<br>R LMV  LMSZ  WY  DPW<br>H  Reserv<br>Reserved<br>ed<br>W<br>Reset 1 0 0 0 0 1 0 1 0 1 0 0 0 1 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R MT  Reserved<br>Reserved  Reserved<br>W<br>Reset 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Local Memory Valid|
|LMV|This read-only field defines the validity (presence) of the local memory.<br>0b - LMEMn not present<br>1b - LMEMn present|
|30-29<br>—<br>28|Reserved<br>LMEM Size Hole|
|LMSZH|This field is used for local memories that are not fully populated (that is, local memories that include a<br>memory "hole" in the upper 25 % of the address range).<br>0b - LMEMn is a power-of-2 capacity<br>1b - LMEMn is not a power-of-2, with capacity of 0.75 x LMSZ|
|27-24<br>LMSZ|Local Memory Size<br>0000b - 0 KB<br>0001b - 1 KB<br>0010b - 2 KB<br>0011b - 4 KB<br>0100b - 8 KB<br>0101b - 16 KB<br>0110b - 32 KB|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

63 / 4640 

NXP Semiconductors 

Miscellaneous Control Module (MCM) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0111b - 64 KB<br>1000b - 128 KB<br>1001b - 256 KB<br>1010b - 512 KB<br>1011b - 1024 KB<br>1100b - 2048 KB<br>1101b - 4096 KB<br>1110b - 8192 KB<br>1111b - 16384 KB|
|23-20<br>WY|Level 1 Cache Ways<br>0000b - No cache<br>0010b - 2-way set associative<br>0100b - 4-way set associative|
|19-17<br>DPW|Data Path Width<br>LMEM data path width. This read-only field defines the width of the local memory.<br>000b-001b - Reserved<br>010b - LMEMn is 32-bits wide<br>011b - LMEMn is 64-bits wide<br>100b-111b - Reserved|
|16<br>—|Reserved|
|15-13<br>MT|Memory Type<br>000b - ITCM<br>001b - DTCM<br>010b - ICACHE<br>011b - DCACHE|
|12-4<br>—|Reserved|
|3-2<br>—|Reserved|
|1-0|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

64 / 4640 

NXP Semiconductors 

Miscellaneous Control Module (MCM) 

Table continued from the previous page... 

|Field<br>Function<br>—|
|---|



## 6.5 Glossary 

ITCM Instruction Tightly Coupled Memory DTCM Data Tightly Coupled Memory ICACHE Instruction Cache Memory DCACHE Data Cache Memory 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

65 / 4640 

