NXP Semiconductors 

# Chapter 49 Error Reporting Module (ERM) 

## 49.1 Chip-specific ERM information 

### 49.1.1 ERM instances 

This chip supports up to two instances of ERM: 

- ERM_0 

- ERM_1 

Table 239. ERM instances 

|Instances|S32K358|S32K322/S32K324/S32K344/S32K342/S32K312/S32K311/S32K314|
|---|---|---|
|ERM_0|Yes|Yes|
|ERM_1|Yes|No|



### 49.1.2 ERM channel mapping 

ERM provides information on memory events associated with ECC and parity. It also provides you an option to enable interrupt notification for these events. 

Table 240. ERM_0 channel mapping 

|Channel #|Module|Captured status|
|---|---|---|
|00|SRAM0|Single-bit error, multi-bit error, syndrome, absolute error address<br>aligned to double-word (64-bit) boundary|
|01|SRAM1<sup>1</sup>|Single-bit error, multi-bit error, syndrome, absolute error<br>address+18000h aligned to double-word (64-bit) boundary<sup>2</sup>|
|02|Cortex-M7_0 I-cache tag RAM|Single-bit error, multi-bit error<sup>3</sup>|
|03|Cortex-M7_0 I-cache data RAM|Single-bit error, multi-bit error<sup>3</sup>|
|04|Cortex-M7_0 D-cache tag RAM|Single-bit error, multi-bit error<sup>3</sup>|
|05|Cortex-M7_0 D-cache data RAM|Single-bit error, multi-bit error<sup>3</sup>|
|06|Cortex-M7_1 I-cache tag RAM<sup>4</sup>|Single-bit error, multi-bit error<sup>3</sup>|
|07|Cortex-M7_1 I-cache data RAM|Single-bit error, multi-bit error<sup>3</sup>|
|08|Cortex-M7_1 D-cache tag RAM|Single-bit error, multi-bit error<sup>3</sup>|
|09|Cortex-M7_1 D-cache data RAM|Single-bit error, multi-bit error<sup>3</sup>|
|10|Cortex-M7_0 ITCM|Single-bit error, multi-bit error, syndrome, offset error address|
|11|Cortex-M7_0 D0TCM|Single-bit error, multi-bit error, syndrome, offset error address|
|12|Cortex-M7_0 D1TCM|Single-bit error, multi-bit error, syndrome, offset error address<sup>5</sup>|
|13|Cortex-M7_1 ITCM|Single-bit error, multi-bit error, syndrome, offset error address|
|14|Cortex-M7_1 D0TCM|Single-bit error, multi-bit error, syndrome, offset error address|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1672 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

Table 240. ERM_0 channel mapping (continued) 

|Channel #|Module|Captured status|
|---|---|---|
|15|Cortex-M7_1 D1TCM|Single-bit error, multi-bit error, syndrome, offset error address<sup>5</sup>|
|16|DMA TCD|Single-bit error, multi-bit error, syndrome, offset error address<sup>6</sup>|
|17|Flash memory port p0|Single-bit error, multi-bit error, absolute error address|
|18|Flash memory port p1|Single-bit error, multi-bit error, absolute error address|
|19|Flash memory port p2<sup>7</sup>|Single-bit error, multi-bit error, absolute error address|



1. SRAM1 is not available for the S32K342, S32K312, and S32K311 product variants. 

2. The size of SRAM0 is 160 KB, and therefore, to align addresses to the next power of 2, an address space of 256 KB is reserved for error reporting. However, SRAM0 and SRAM1 are in contiguous locations in the memory map. So, you must subtract 18000h (256 KB-160 KB = 96 KB that corresponds to 18000h) from the reported address to get an absolute address. See the "Memory and Memory Interfaces" chapter for SRAM details on different S32K3xx variants. 

3. The cache controller does not report error addresses and syndrome. 

4. Cortex-M7_1 and its associated RAM and caches are not available in the S32K312 and S32K311 product variants. 

5. For address reporting, bit 2 of the address is masked because this bit decides whether the access (read or write) is for D0TCM or D1TCM. For example, if the offset address is 0h or 8h, it is routed to D0TCM, but if the offset address is 4h or Ch, it is routed to D1TCM. The errors that are latched for these offset addresses are as follows: 

   - Offset 0h : Address 0h is latched into the ERM channel corresponding to D0TCM. 

   - Offset 4h : Address 0h is latched into the ERM channel corresponding to D1TCM. 

   - Offset 8h : Address 8h is latched into the ERM channel corresponding to D0TCM. 

   - Offset Ch : Address 8h is latched into the ERM channel corresponding to D1TCM. 

6. Bits [31:10] and [2:0] are always 0 because they are not connected. 

Bits [9:5] indicate the corresponding TCD out of all the 32 implemented TCDs. 

Bits [4:3] indicate an offset of TCDs with respect to a 64-bit aligned boundary. 

   - If [4:3] is 00, it indicates that an error is on offset address 20h. 

   - If [4:3] is 01, it indicates that an error is on offset address 28h. 

   - If [4:3] is 10, it indicates that an error is on offset address 30h. 

   - If [4:3] is 11, it indicates that an error is on offset address 38h. 

7. Flash memory port p2 is not applicable for the S32K312 and S32K311 product variants. 

~~<mark>NOTE</mark>~~ 

Table 241 is aplicable for S32K358 only. 

Table 241. ERM_1 channel mapping 

|Channel #|Module|Captured status|
|---|---|---|
|0|SRAM2|single-bit error, multi-bit error, syndrome, absolute error<br>address aligned to double, word (64-bit) boundary|
|1|-|-|
|2|CM7_2 I-cache tag RAM|single-bit error, multi-bit error|
|3|CM7_2 I-cache data RAM|single-bit error, multi-bit error|
|4|CM7_2 D-cache tag RAM|single-bit error, multi-bit error|
|5|CM7_2 D-cache data RAM|single-bit error, multi-bit error|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1673 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

Table 241. ERM_1 channel mapping (continued) 

|Channel #|Module|Captured status|
|---|---|---|
|6|-|-|
|7|-|-|
|8|-|-|
|9|-|-|
|10|CM7_2 ITCM|single-bit error, multi-bit error, syndrome, offset error address|
|11|CM7_2 D0TCM|single-bit error, multi-bit error, syndrome, offset error address|
|12|CM7_2 D1TCM|single-bit error, multi-bit error, syndrome, offset error address|
|13|-|-|
|14|-|-|
|15|-|-|
|16|-|-|
|17|flash memory port p3|single-bit error, multi-bit error, syndrome, offset error address|
|18|-|-|
|19|-|-|
|20|-|-|
|21|-|-|
|22|-|-|
|23|-|-|



~~<mark>NOTE</mark>~~ 

For S32K358, you have to enable both the ERM instance even if you are only using the one otherwise software might hang during interrupt subroutine. 

## 49.2 Overview 

The Error Reporting Module (ERM) provides information and optional interrupt notification on memory error events associated with ECC and parity. The ERM collects error events on memory accesses for memory arrays, such as flash memory, system RAM, or peripheral RAMs. ERM supports various channels for memory sources where each ERM channel is associated with a different memory module. See the chip-specific ERM information for details about supported memory sources and specific memory channel assignments. If memory supports ECC then ERM syndrome and error address information is captured along with error event. ERM does not receive this information in case of cache or memory with parity along with error event. 

### 49.2.1 Features 

The ERM includes these features: 

- Optional interrupt notification on captured error events 

- Capturing of address and syndrome information on single-bit correction and non-correctable ECC events 

- Support for error event capturing for memory sources, with individual reporting fields and interrupt configuration per memory channel 

- Recording the count value of the number of corrected error events 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1674 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

## 49.3 Functional description 

### 49.3.1 Single-bit correction events 

When a single-bit correction event on Memory n is detected, the ERM: 

- Records the event by changing the value of the applicable Status Register bit SRx[SBCn] to 1. 

- Increments the correctable error count value (until the counter reaches its maximum value): CORR_ERR_CNTn[COUNT]. 

- Records the corresponding access address that initiated the event in the Memory n Error Address Register: EARn (if this register is present for the channel). 

- Stores the corresponding ECC syndrome in the Memory n Error Syndrome Register: SYNn (if this register is present for the channel). This register identifies the bit position of the corrected data on single-bit data inversion. 

The ERM holds event information only for the last reported event. 

To clear the record of an event, write 1 to SRx[SBCn] to change its value to 0. 

To reset the correctable error count value, write all zeros to CORR_ERR_CNTn[COUNT]. 

Optional interrupt notification for single-bit correction events 

The ERM provides an option to generate an interrupt notification upon the report of a single-bit correction event. This sequence describes how to use the option: 

1. To enable interrupt notification for single-bit correction events on Memory n, set CRx[ESCIEn] to 1. 

2. Subsequently, when a single-bit correction event on Memory n is detected, the ERM: 

   - Records the event and address, and stores the ECC syndrome as usual. 

   - Additionally sends an interrupt notification corresponding to the event. 

3. To clear both the record of an event and the corresponding interrupt notification, write 1 to SRx[SBCn] to change its value to 0. 

### 49.3.2 Non-correctable error events 

When a non-correctable ECC error event on Memory n is detected, the ERM: 

- Records the event by changing the value of the applicable Status Register bit: SRx[NCEn] to 1. 

- Records the corresponding access address that initiated the event in the Memory n Error Address Register: EARn (if this register is present for the channel). 

- Stores the corresponding ECC syndrome in the Memory n Error Syndrome Register: SYNn (if this register is present for the channel). 

   - In the event of a non-correctable address bit inversion, SYNn identifies the pertinent address bit position. 

   - In the event of a non-correctable, multi-bit data inversion, the syndrome value does not provide any additional diagnostic information. 

The ERM holds event information only for the last reported event. 

To clear the record of an event, write 1 to SRx[NCEn] to change its value to 0. 

Optional interrupt notification for non-correctable error events 

The ERM provides an option to generate an interrupt notification upon the report of a non-correctable ECC event. This sequence describes how to use the option: 

1. To enable interrupt notifications for non-correctable error events on Memory n, set CRx[ENCIEn] to 1. 

2. Subsequently, when a non-correctable error event on Memory n is detected, the ERM: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1675 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

   - Records the event and address and stores the ECC syndrome as usual. 

   - Additionally sends an interrupt notification corresponding to the event. 

3. To clear both the record of an event and the corresponding interrupt notification, write 1 to SRx[NCEn] to change its value to 0. 

## 49.4 Initialization 

For each ERM channel supporting memory with ECC, prepare the corresponding memory array before enabling ERM interrupts about errors for that memory. 

1. Initialize the memory to a known value so that the correct corresponding ECC codeword is stored. 

2. During the memory's initialization, if the ERM captures information about any ECC error event, clear the corresponding SRx[SBCn] or SRx[NCEn] field that stores the record of the event. 

3. Program the applicable CRx[ESCIEn] and CRx[ENCIEn] fields to enable ERM interrupts as desired. 

## 49.5 ERM register descriptions 

You can access the programming model: 

- Only in supervisor mode 

- Using only 32-bit (word) accesses 

Any of the following attempted references to the programming model generates an error termination: 

- In user mode 

- Using non-32-bit access sizes 

~~<mark>NOTE</mark>~~ 

- See the chip-specific ERM information for details on Memory channel mapping. 

- To access the channel registers, corresponding channel clocks must be enabled. 

### 49.5.1 ERM memory map 

ERM_0 base address: 4025_C000h 

ERM_1 base address: 4000_C000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|ERM Configuration Register 0 (CR0)|32|RW|0000_0000h|
|4h|ERM Configuration Register 1 (CR1)|32|RW|0000_0000h|
|8h|ERM Configuration Register 2 (CR2)|32|RW|0000_0000h|
|10h|ERM Status Register 0 (SR0)|32|W1C|0000_0000h|
|14h|ERM Status Register 1 (SR1)|32|W1C|0000_0000h|
|18h|ERM Status Register 2 (SR2)|32|W1C|0000_0000h|
|100h|ERM Memory 0 Error Address Register (EAR0)|32|RO|0000_0000h|
|104h|ERM Memory 0 Syndrome Register (SYN0)|32|RO|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1676 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|108h|ERM Memory 0 Correctable Error Count Register<br>(CORR_ERR_CNT0)|32|ROWZ|0000_0000h|
|110h|ERM Memory 1 Error Address Register (EAR1)|32|RO|0000_0000h|
|114h|ERM Memory 1 Syndrome Register (SYN1)|32|RO|0000_0000h|
|118h|ERM Memory 1 Correctable Error Count Register<br>(CORR_ERR_CNT1)|32|ROWZ|0000_0000h|
|128h|ERM Memory 2 Correctable Error Count Register<br>(CORR_ERR_CNT2)|32|ROWZ|0000_0000h|
|138h|ERM Memory 3 Correctable Error Count Register<br>(CORR_ERR_CNT3)|32|ROWZ|0000_0000h|
|148h|ERM Memory 4 Correctable Error Count Register<br>(CORR_ERR_CNT4)|32|ROWZ|0000_0000h|
|158h|ERM Memory 5 Correctable Error Count Register<br>(CORR_ERR_CNT5)|32|ROWZ|0000_0000h|
|168h|ERM Memory 6 Correctable Error Count Register<br>(CORR_ERR_CNT6)|32|ROWZ|0000_0000h|
|178h|ERM Memory 7 Correctable Error Count Register<br>(CORR_ERR_CNT7)|32|ROWZ|0000_0000h|
|188h|ERM Memory 8 Correctable Error Count Register<br>(CORR_ERR_CNT8)|32|ROWZ|0000_0000h|
|198h|ERM Memory 9 Correctable Error Count Register<br>(CORR_ERR_CNT9)|32|ROWZ|0000_0000h|
|1A0h|ERM Memory 10 Error Address Register (EAR10)|32|RO|0000_0000h|
|1A4h|ERM Memory 10 Syndrome Register (SYN10)|32|RO|0000_0000h|
|1A8h|ERM Memory 10 Correctable Error Count Register<br>(CORR_ERR_CNT10)|32|ROWZ|0000_0000h|
|1B0h|ERM Memory 11 Error Address Register (EAR11)|32|RO|0000_0000h|
|1B4h|ERM Memory 11 Syndrome Register (SYN11)|32|RO|0000_0000h|
|1B8h|ERM Memory 11 Correctable Error Count Register<br>(CORR_ERR_CNT11)|32|ROWZ|0000_0000h|
|1C0h|ERM Memory 12 Error Address Register (EAR12)|32|RO|0000_0000h|
|1C4h|ERM Memory 12 Syndrome Register (SYN12)|32|RO|0000_0000h|
|1C8h|ERM Memory 12 Correctable Error Count Register<br>(CORR_ERR_CNT12)|32|ROWZ|0000_0000h|
|1D0h|ERM Memory 13 Error Address Register (EAR13)|32|RO|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1677 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|1D4h|ERM Memory 13 Syndrome Register (SYN13)|32|RO|0000_0000h|
|1D8h|ERM Memory 13 Correctable Error Count Register<br>(CORR_ERR_CNT13)|32|ROWZ|0000_0000h|
|1E0h|ERM Memory 14 Error Address Register (EAR14)|32|RO|0000_0000h|
|1E4h|ERM Memory 14 Syndrome Register (SYN14)|32|RO|0000_0000h|
|1E8h|ERM Memory 14 Correctable Error Count Register<br>(CORR_ERR_CNT14)|32|ROWZ|0000_0000h|
|1F0h|ERM Memory 15 Error Address Register (EAR15)|32|RO|0000_0000h|
|1F4h|ERM Memory 15 Syndrome Register (SYN15)|32|RO|0000_0000h|
|1F8h|ERM Memory 15 Correctable Error Count Register<br>(CORR_ERR_CNT15)|32|ROWZ|0000_0000h|
|200h|ERM Memory 16 Error Address Register (EAR16)|32|RO|0000_0000h|
|204h|ERM Memory 16 Syndrome Register (SYN16)|32|RO|0000_0000h|
|208h|ERM Memory 16 Correctable Error Count Register<br>(CORR_ERR_CNT16)|32|ROWZ|0000_0000h|
|210h|ERM Memory 17 Error Address Register (EAR17)|32|RO|0000_0000h|
|218h|ERM Memory 17 Correctable Error Count Register<br>(CORR_ERR_CNT17)|32|ROWZ|0000_0000h|
|220h|ERM Memory 18 Error Address Register (EAR18)|32|RO|0000_0000h|
|228h|ERM Memory 18 Correctable Error Count Register<br>(CORR_ERR_CNT18)|32|ROWZ|0000_0000h|
|230h|ERM Memory 19 Error Address Register (EAR19)|32|RO|0000_0000h|
|238h|ERM Memory 19 Correctable Error Count Register<br>(CORR_ERR_CNT19)|32|ROWZ|0000_0000h|



### 49.5.2 ERM Configuration Register 0 (CR0) 

#### Offset 

|Register|Offset|
|---|---|
|CR0|0h|



#### Function 

This 32-bit control register configures the interrupt notification capability for available channels. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1678 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/049_Error_Reporting_Module_-ERM-/S32K3XXRM_数据表.pdf-1679-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R ESCIE ENCIE 0 ESCIE ENCIE 0 ESCIE ENCIE 0 ESCIE ENCIE 0<br>W 0  0  1  1  2  2  3  3<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R ESCIE ENCIE 0 ESCIE ENCIE 0 ESCIE ENCIE 0 ESCIE ENCIE 0<br>W 4  4  5  5  6  6  7  7<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31|ESCIE0|
|ESCIE0|Enable Memory 0 Single Correction Interrupt Notification<br>This field is initialized by hardware reset.<br>0b - Interrupt notification of Memory 0 single-bit correction events is disabled.<br>1b - Interrupt notification of Memory 0 single-bit correction events is enabled.|
|30|ENCIE0|
|ENCIE0|Enable Memory 0 Non-Correctable Interrupt Notification<br>This field is initialized by hardware reset.<br>0b - Interrupt notification of Memory 0 non-correctable error events is disabled.<br>1b - Interrupt notification of Memory 0 non-correctable error events is enabled.|
|29-28<br>—<br>27|Reserved<br>ESCIE1|
|ESCIE1|Enable Memory 1 Single Correction Interrupt Notification<br>This field is initialized by hardware reset.<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>~~NOTE~~|
||Instance<br>Field supported in<br>Field not supported in|
||ERM_0<br>CR0<br>—|
||ERM_1<br>—<br>CR0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1679 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 

|Field|Function<br>0b - Interrupt notification of Memory 1 single-bit correction events is disabled.<br>1b - Interrupt notification of Memory 1 single-bit correction events is enabled.|
|---|---|
|26|ENCIE1|
|ENCIE1|Enable Memory 1 Non-Correctable Interrupt Notification<br>This field is initialized by hardware reset.<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>~~NOTE~~|
||Instance<br>Field supported in<br>Field not supported in|
||ERM_0<br>CR0<br>—|
||ERM_1<br>—<br>CR0|
||0b - Interrupt notification of Memory 1 non-correctable error events is disabled.<br>1b - Interrupt notification of Memory 1 non-correctable error events is enabled.|
|25-24<br>—|Reserved|
|23|ESCIE2|
|ESCIE2|Enable Memory 2 Single Correction Interrupt Notification<br>This field is initialized by hardware reset.<br>0b - Interrupt notification of Memory 2 single-bit correction events is disabled.<br>1b - Interrupt notification of Memory 2 single-bit correction events is enabled.|
|22|ENCIE2|
|ENCIE2|Enable Memory 2 Non-Correctable Interrupt Notification<br>This field is initialized by hardware reset.<br>0b - Interrupt notification of Memory 2 non-correctable error events is disabled.<br>1b - Interrupt notification of Memory 2 non-correctable error events is enabled.|
|21-20<br>—|Reserved|
|19|ESCIE3|
|ESCIE3|Enable Memory 3 Single Correction Interrupt Notification|
||This field is initialized by hardware reset.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1680 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Interrupt notification of Memory 3 single-bit correction events is disabled.<br>1b - Interrupt notification of Memory 3 single-bit correction events is enabled.|
|18|ENCIE3|
|ENCIE3|Enable Memory 3 Non-Correctable Interrupt Notification<br>This field is initialized by hardware reset.<br>0b - Interrupt notification of Memory 3 non-correctable error events is disabled.<br>1b - Interrupt notification of Memory 3 non-correctable error events is enabled.|
|17-16<br>—|Reserved|
|15|ESCIE4|
|ESCIE4|Enable Memory 4 Single Correction Interrupt Notification<br>This field is initialized by hardware reset.<br>0b - Interrupt notification of Memory 4 single-bit correction events is disabled.<br>1b - Interrupt notification of Memory 4 single-bit correction events is enabled.|
|14|ENCIE4|
|ENCIE4|Enable Memory 4 Non-Correctable Interrupt Notification<br>This field is initialized by hardware reset.<br>0b - Interrupt notification of Memory 4 non-correctable error events is disabled.|
||1b - Interrupt notification of Memory 4 non-correctable error events is enabled.|
|13-12<br>—|Reserved|
|11|ESCIE5|
|ESCIE5|Enable Memory 5 Single Correction Interrupt Notification<br>This field is initialized by hardware reset.<br>0b - Interrupt notification of Memory 5 single-bit correction events is disabled.<br>1b - Interrupt notification of Memory 5 single-bit correction events is enabled.|
|10|ENCIE5|
|ENCIE5|Enable Memory 5 Non-Correctable Interrupt Notification<br>This field is initialized by hardware reset.<br>0b - Interrupt notification of Memory 5 non-correctable error events is disabled.<br>1b - Interrupt notification of Memory 5 non-correctable error events is enabled.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1681 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/049_Error_Reporting_Module_-ERM-/S32K3XXRM_数据表.pdf-1682-03.png)


<!-- Start of picture text -->
Field Function<br>9-8 Reserved<br>—<br>7 ESCIE6<br>ESCIE6 Enable Memory 6 Single Correction Interrupt Notification<br>This field is initialized by hardware reset.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 CR0 —<br>ERM_1 — CR0<br>0b - Interrupt notification of Memory 6 single-bit correction events is disabled.<br>1b - Interrupt notification of Memory 6 single-bit correction events is enabled.<br>6 ENCIE6<br>ENCIE6 Enable Memory 6 Non-Correctable Interrupt Notification<br>This field is initialized by hardware reset.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 CR0 —<br>ERM_1 — CR0<br>0b - Interrupt notification of Memory 6 non-correctable error events is disabled.<br>1b - Interrupt notification of Memory 6 non-correctable error events is enabled.<br>5-4 Reserved<br>—<br>3 ESCIE7<br>ESCIE7 Enable Memory 7 Single Correction Interrupt Notification<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1682 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/049_Error_Reporting_Module_-ERM-/S32K3XXRM_数据表.pdf-1683-03.png)


<!-- Start of picture text -->
Field Function<br>This field is initialized by hardware reset.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 CR0 —<br>ERM_1 — CR0<br>0b - Interrupt notification of Memory 7 single-bit correction events is disabled.<br>1b - Interrupt notification of Memory 7 single-bit correction events is enabled.<br>2 ENCIE7<br>ENCIE7 Enable Memory 7 Non-Correctable Interrupt Notification<br>This field is initialized by hardware reset.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 CR0 —<br>ERM_1 — CR0<br>0b - Interrupt notification of Memory 7 non-correctable error events is disabled.<br>1b - Interrupt notification of Memory 7 non-correctable error events is enabled.<br>1-0 Reserved<br>—<br><!-- End of picture text -->

### 49.5.3 ERM Configuration Register 1 (CR1) 

#### Offset 

|Register|Offset|
|---|---|
|CR1|4h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1683 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Function 

This 32-bit control register configures the interrupt notification capability for available channels. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|ESCIE|ENCIE|0||ESCIE|ENCIE||0|ESCIE|ENCIE||0|ESCIE|ENCIE|0|
|W|8|8|||9|9|||10|10|||11|11||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R|ESCIE|ENCIE|0||ESCIE|ENCIE||0|ESCIE|ENCIE||0|ESCIE|ENCIE|0|
|W|12|12|||13|13|||14|14|||15|15||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



#### Fields 

|Field|Function||
|---|---|---|
|31|ESCIE8||
|ESCIE8|Enable Memory 8 Single Correction Interrupt Notification<br>This field is initialized by hardware reset.<br>This field is not supported in every instance. The following ta<br>supported registers.<br>~~NOTE~~|ble includes only|
||Instance<br>Field supported in|Field not supported in|
||ERM_0<br>CR1|—|
||ERM_1<br>—|CR1|
||0b - Interrupt notification of Memory 8 single-bit correction e<br>1b - Interrupt notification of Memory 8 single-bit correction e|vents is disabled.<br>vents is enabled.|
|30|ENCIE8||
|ENCIE8|Enable Memory 8 Non-Correctable Interrupt Notification<br>This field is initialized by hardware reset.<br>This field is not supported in every instance. The following ta<br>supported registers.<br>~~NOTE~~|ble includes only|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1684 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/049_Error_Reporting_Module_-ERM-/S32K3XXRM_数据表.pdf-1685-03.png)


<!-- Start of picture text -->
Field Function<br>Instance Field supported in Field not supported in<br>ERM_0 CR1 —<br>ERM_1 — CR1<br>0b - Interrupt notification of Memory 8 non-correctable error events is disabled.<br>1b - Interrupt notification of Memory 8 non-correctable error events is enabled.<br>29-28 Reserved<br>—<br>27 ESCIE9<br>ESCIE9 Enable Memory 9 Single Correction Interrupt Notification<br>This field is initialized by hardware reset.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 CR1 —<br>ERM_1 — CR1<br>0b - Interrupt notification of Memory 9 single-bit correction events is disabled.<br>1b - Interrupt notification of Memory 9 single-bit correction events is enabled.<br>26 ENCIE9<br>ENCIE9 Enable Memory 9 Non-Correctable Interrupt Notification<br>This field is initialized by hardware reset.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 CR1 —<br>ERM_1 — CR1<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1685 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||Instance<br>Field supported in<br>Field not supported in|
||0b - Interrupt notification of Memory 9 non-correctable error events is disabled.<br>1b - Interrupt notification of Memory 9 non-correctable error events is enabled.|
|25-24<br>—|Reserved|
|23<br>ESCIE10|ESCIE10<br>Enable Memory 10 Single Correction Interrupt Notification<br>This field is initialized by hardware reset.<br>0b - Interrupt notification of Memory 10 single-bit correction events is disabled.<br>1b - Interrupt notification of Memory 10 single-bit correction events is enabled.|
|22<br>ENCIE10|ENCIE10<br>Enable Memory 10 Non-Correctable Interrupt Notification<br>This field is initialized by hardware reset.<br>0b - Interrupt notification of Memory 10 non-correctable error events is disabled.<br>1b - Interrupt notification of Memory 10 non-correctable error events is enabled.|
|21-20<br>—|Reserved|
|19<br>ESCIE11|ESCIE11<br>Enable Memory 11 Single Correction Interrupt Notification<br>This field is initialized by hardware reset.<br>0b - Interrupt notification of Memory 11 single-bit correction events is disabled.<br>1b - Interrupt notification of Memory 11 single-bit correction events is enabled.|
|18<br>ENCIE11|ENCIE11<br>Enable Memory 11 Non-Correctable Interrupt Notification<br>This field is initialized by hardware reset.<br>0b - Interrupt notification of Memory 11 non-correctable error events is disabled.<br>1b - Interrupt notification of Memory 11 non-correctable error events is enabled.|
|17-16<br>—<br>15|Reserved<br>ESCIE12|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1686 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/049_Error_Reporting_Module_-ERM-/S32K3XXRM_数据表.pdf-1687-03.png)


<!-- Start of picture text -->
Field Function<br>ESCIE12 Enable Memory 12 Single Correction Interrupt Notification<br>This field is initialized by hardware reset.<br>0b - Interrupt notification of Memory 12 single-bit correction events is disabled.<br>1b - Interrupt notification of Memory 12 single-bit correction events is enabled.<br>14 ENCIE12<br>ENCIE12 Enable Memory 12 Non-Correctable Interrupt Notification<br>This field is initialized by hardware reset.<br>0b - Interrupt notification of Memory 12 non-correctable error events is disabled.<br>1b - Interrupt notification of Memory 12 non-correctable error events is enabled.<br>13-12 Reserved<br>—<br>11 ESCIE13<br>ESCIE13 Enable Memory 13 Single Correction Interrupt Notification<br>This field is initialized by hardware reset.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 CR1 —<br>ERM_1 — CR1<br>0b - Interrupt notification of Memory 13 single-bit correction events is disabled.<br>1b - Interrupt notification of Memory 13 single-bit correction events is enabled.<br>10 ENCIE13<br>ENCIE13 Enable Memory 13 Non-Correctable Interrupt Notification<br>This field is initialized by hardware reset.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1687 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/049_Error_Reporting_Module_-ERM-/S32K3XXRM_数据表.pdf-1688-03.png)


<!-- Start of picture text -->
Field Function<br>Instance Field supported in Field not supported in<br>ERM_0 CR1 —<br>ERM_1 — CR1<br>0b - Interrupt notification of Memory 13 non-correctable error events is disabled.<br>1b - Interrupt notification of Memory 13 non-correctable error events is enabled.<br>9-8 Reserved<br>—<br>7 ESCIE14<br>ESCIE14 Enable Memory 14 Single Correction Interrupt Notification<br>This field is initialized by hardware reset.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 CR1 —<br>ERM_1 — CR1<br>0b - Interrupt notification of Memory 14 single-bit correction events is disabled.<br>1b - Interrupt notification of Memory 14 single-bit correction events is enabled.<br>6 ENCIE14<br>ENCIE14 Enable Memory 14 Non-Correctable Interrupt Notification<br>This field is initialized by hardware reset.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 CR1 —<br>ERM_1 — CR1<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1688 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/049_Error_Reporting_Module_-ERM-/S32K3XXRM_数据表.pdf-1689-03.png)


<!-- Start of picture text -->
Field Function<br>Instance Field supported in Field not supported in<br>0b - Interrupt notification of Memory 14 non-correctable error events is disabled.<br>1b - Interrupt notification of Memory 14 non-correctable error events is enabled.<br>5-4 Reserved<br>—<br>3 ESCIE15<br>ESCIE15 Enable Memory 15 Single Correction Interrupt Notification<br>This field is initialized by hardware reset.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 CR1 —<br>ERM_1 — CR1<br>0b - Interrupt notification of Memory 15 single-bit correction events is disabled.<br>1b - Interrupt notification of Memory 15 single-bit correction events is enabled.<br>2 ENCIE15<br>ENCIE15 Enable Memory 15 Non-Correctable Interrupt Notification<br>This field is initialized by hardware reset.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 CR1 —<br>ERM_1 — CR1<br>0b - Interrupt notification of Memory 15 non-correctable error events is disabled.<br>1b - Interrupt notification of Memory 15 non-correctable error events is enabled.<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1689 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|1-0<br>—|Reserved|



### 49.5.4 ERM Configuration Register 2 (CR2) 

#### Offset 

|Register|Offset|
|---|---|
|CR2|8h|



#### Function 

This 32-bit control register configures the interrupt notification capability for available channels. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/049_Error_Reporting_Module_-ERM-/S32K3XXRM_数据表.pdf-1690-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R ESCIE ENCIE 0 ESCIE ENCIE 0 ESCIE ENCIE 0 ESCIE ENCIE 0<br>W 16  16  17  17  18  18  19  19<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 0 0<br>Reserved  Reserved  Reserved  Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31|ESCIE16|
|ESCIE16|Enable Memory 16 Single Correction Interrupt Notification|
||This field is initialized by hardware reset.|
||This field is not supported in every instance. The following table includes only<br>supported registers.<br>~~NOTE~~|



|ERM_0|Instance|Field supported in<br>CR2|Field not supported in<br>—|
|---|---|---|---|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1690 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

|Field|Function|
|---|---|
||Instance<br>Field supported in<br>Field not supported in|
||ERM_1<br>—<br>CR2|
||0b - Interrupt notification of Memory 16 single-bit correction events is disabled.<br>1b - Interrupt notification of Memory 16 single-bit correction events is enabled.|
|30<br>ENCIE16|ENCIE16<br>Enable Memory 16 Non-Correctable Interrupt Notification<br>This field is initialized by hardware reset.<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>~~NOTE~~|
||Instance<br>Field supported in<br>Field not supported in|
||ERM_0<br>CR2<br>—|
||ERM_1<br>—<br>CR2<br>0b - Interrupt notification of Memory 16 non-correctable error events is disabled.<br>1b - Interrupt notification of Memory 16 non-correctable error events is enabled.|
|29-28<br>—|Reserved|
|27<br>ESCIE17|ESCIE17<br>Enable Memory 17 Single Correction Interrupt Notification<br>This field is initialized by hardware reset.<br>0b - Interrupt notification of Memory 17 single-bit correction events is disabled.<br>1b - Interrupt notification of Memory 17 single-bit correction events is enabled.|
|26<br>ENCIE17|ENCIE17<br>Enable Memory 17 Non-Correctable Interrupt Notification<br>This field is initialized by hardware reset.<br>0b - Interrupt notification of Memory 17 non-correctable error events is disabled.<br>1b - Interrupt notification of Memory 17 non-correctable error events is enabled.|
|25-24<br>—|Reserved<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1691 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/049_Error_Reporting_Module_-ERM-/S32K3XXRM_数据表.pdf-1692-03.png)


<!-- Start of picture text -->
Field Function<br>23 ESCIE18<br>ESCIE18 Enable Memory 18 Single Correction Interrupt Notification<br>This field is initialized by hardware reset.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 CR2 —<br>ERM_1 — CR2<br>0b - Interrupt notification of Memory 18 single-bit correction events is disabled.<br>1b - Interrupt notification of Memory 18 single-bit correction events is enabled.<br>22 ENCIE18<br>ENCIE18 Enable Memory 18 Non-Correctable Interrupt Notification<br>This field is initialized by hardware reset.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 CR2 —<br>ERM_1 — CR2<br>0b - Interrupt notification of Memory 18 non-correctable error events is disabled.<br>1b - Interrupt notification of Memory 18 non-correctable error events is enabled.<br>21-20 Reserved<br>—<br>19 ESCIE19<br>ESCIE19 Enable Memory 19 Single Correction Interrupt Notification<br>This field is initialized by hardware reset.<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1692 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/049_Error_Reporting_Module_-ERM-/S32K3XXRM_数据表.pdf-1693-03.png)


<!-- Start of picture text -->
Field Function<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 CR2 —<br>ERM_1 — CR2<br>0b - Interrupt notification of Memory 19 single-bit correction events is disabled.<br>1b - Interrupt notification of Memory 19 single-bit correction events is enabled.<br>18 ENCIE19<br>ENCIE19 Enable Memory 19 Non-Correctable Interrupt Notification<br>This field is initialized by hardware reset.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 CR2 —<br>ERM_1 — CR2<br>0b - Interrupt notification of Memory 19 non-correctable error events is disabled.<br>1b - Interrupt notification of Memory 19 non-correctable error events is enabled.<br>17-16 Reserved<br>—<br>15-14 Reserved<br>—<br>13-12 Reserved<br>—<br>11-10 Reserved<br>—<br>9-8 Reserved<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1693 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

Table continued from the previous page... 

|Field<br>—|Function|
|---|---|
|7-6<br>—|Reserved|
|5-4<br>—|Reserved|
|3-2<br>—|Reserved|
|1-0<br>—|Reserved|



### 49.5.5 ERM Status Register 0 (SR0) 

#### Offset 

|Register|Offset|
|---|---|
|SR0|10h|



#### Function 

This 32-bit status register reports error events for available channels. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|SBC0|NCE0|0||SBC1|NCE1||0|SBC2|NCE2|0||SBC3|NCE3|0|
|W|W1C|W1C|||W1C|W1C|||W1C|W1C|||W1C|W1C||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R|SBC4|NCE4|0||SBC5|NCE5||0|SBC6|NCE6|0||SBC7|NCE7|0|
|W|W1C|W1C|||W1C|W1C|||W1C|W1C|||W1C|W1C||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1694 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Fields 

|Field|Function||
|---|---|---|
|31|SBC0||
|SBC0|Memory 0 Single-Bit Correction Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding int<br>is enabled.<br>0b - No single-bit correction event on Memory 0 detected.<br>1b - Single-bit correction event on Memory 0 detected.|errupt notification, if CR0[ESCIE0]|
|30|NCE0||
|NCE0|Memory 0 Non-Correctable Error Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding int<br>is enabled.<br>0b - No non-correctable error event on Memory 0 detected.<br>1b - Non-correctable error event on Memory 0 detected.|errupt notification, if CR0[ENCIE0]|
|29-28<br>—|Reserved||
|27<br>SBC1|SBC1<br>Memory 1 Single-Bit Correction Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding int<br>is enabled.<br>This field is not supported in every instance. The following tabl<br>supported registers.<br>~~NOTE~~|errupt notification, if CR0[ESCIE1]<br>e includes only|
||Instance<br>Field supported in|Field not supported in|
||ERM_0<br>SR0|—|
||ERM_1<br>—|SR0|
||0b - No single-bit correction event on Memory 1 detected.||
||1b - Single-bit correction event on Memory 1 detected.||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1695 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 

|Field<br>26<br>NCE1|Function<br>NCE1<br>Memory 1 Non-Correctable Error Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding int<br>is enabled.<br>This field is not supported in every instance. The following tabl<br>supported registers.<br>~~NOTE~~|errupt notification, if CR0[ENCIE1]<br>e includes only|
|---|---|---|
||Instance<br>Field supported in|Field not supported in|
||ERM_0<br>SR0|—|
||ERM_1<br>—|SR0|
||0b - No non-correctable error event on Memory 1 detected.<br>1b - Non-correctable error event on Memory 1 detected.||
|25-24<br>—|Reserved||
|23<br>SBC2|SBC2<br>Memory 2 Single-Bit Correction Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding int<br>is enabled.<br>0b - No single-bit correction event on Memory 2 detected.<br>1b - Single-bit correction event on Memory 2 detected.|errupt notification, if CR0[ESCIE2]|
|22<br>NCE2|NCE2<br>Memory 2 Non-Correctable Error Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding int<br>is enabled.<br>0b - No non-correctable error event on Memory 2 detected.<br>1b - Non-correctable error event on Memory 2 detected.|errupt notification, if CR0[ENCIE2]|
|21-20<br>—|Reserved||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1696 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|19<br>SBC3|SBC3<br>Memory 3 Single-Bit Correction Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR0[ESCIE3]<br>is enabled.<br>0b - No single-bit correction event on Memory 3 detected.<br>1b - Single-bit correction event on Memory 3 detected.|
|18<br>NCE3|NCE3<br>Memory 3 Non-Correctable Error Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR0[ENCIE3]<br>is enabled.<br>0b - No non-correctable error event on Memory 3 detected.<br>1b - Non-correctable error event on Memory 3 detected.|
|17-16<br>—|Reserved|
|15<br>SBC4|SBC4<br>Memory 4 Single-Bit Correction Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR0[ESCIE4]<br>is enabled.<br>0b - No single-bit correction event on Memory 4 detected.<br>1b - Single-bit correction event on Memory 4 detected.|
|14<br>NCE4|NCE4<br>Memory 4 Non-Correctable Error Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR0[ENCIE4]<br>is enabled.<br>0b - No non-correctable error event on Memory 4 detected.<br>1b - Non-correctable error event on Memory 4 detected.|
|13-12<br>—<br>11|Reserved<br>SBC5|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1697 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|SBC5|Memory 5 Single-Bit Correction Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR0[ESCIE5]<br>is enabled.<br>0b - No single-bit correction event on Memory 5 detected.<br>1b - Single-bit correction event on Memory 5 detected.|
|10<br>NCE5|NCE5<br>Memory 5 Non-Correctable Error Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR0[ENCIE5]<br>is enabled.<br>0b - No non-correctable error event on Memory 5 detected.<br>1b - Non-correctable error event on Memory 5 detected.|
|9-8<br>—|Reserved|
|7<br>SBC6|SBC6<br>Memory 6 Single-Bit Correction Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR0[ESCIE6]<br>is enabled.<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>~~NOTE~~|
||Instance<br>Field supported in<br>Field not supported in|
||ERM_0<br>SR0<br>—|
||ERM_1<br>—<br>SR0|
||0b - No single-bit correction event on Memory 6 detected.<br>1b - Single-bit correction event on Memory 6 detected.|
|6<br>NCE6|NCE6<br>Memory 6 Non-Correctable Error Event<br>This field is initialized by hardware reset.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1698 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/049_Error_Reporting_Module_-ERM-/S32K3XXRM_数据表.pdf-1699-03.png)


<!-- Start of picture text -->
Field Function<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR0[ENCIE6]<br>is enabled.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 SR0 —<br>ERM_1 — SR0<br>0b - No non-correctable error event on Memory 6 detected.<br>1b - Non-correctable error event on Memory 6 detected.<br>5-4 Reserved<br>—<br>3 SBC7<br>SBC7 Memory 7 Single-Bit Correction Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR0[ESCIE7]<br>is enabled.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 SR0 —<br>ERM_1 — SR0<br>0b - No single-bit correction event on Memory 7 detected.<br>1b - Single-bit correction event on Memory 7 detected.<br>2 NCE7<br>NCE7 Memory 7 Non-Correctable Error Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR0[ENCIE7]<br>is enabled.<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1699 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/049_Error_Reporting_Module_-ERM-/S32K3XXRM_数据表.pdf-1700-03.png)


<!-- Start of picture text -->
Field Function<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 SR0 —<br>ERM_1 — SR0<br>0b - No non-correctable error event on Memory 7 detected.<br>1b - Non-correctable error event on Memory 7 detected.<br>1-0 Reserved<br>—<br><!-- End of picture text -->

### 49.5.6 ERM Status Register 1 (SR1) 

#### Offset 

|Register|Offset|
|---|---|
|SR1|14h|



#### Function 

This 32-bit status register reports error events for available channels. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21||20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|SBC8|NCE8|0||SBC9|NCE9||0|SBC10|NCE10||0||SBC11|NCE11|0|
|W|W1C|W1C|||W1C|W1C|||W1C|W1C||||W1C|W1C||
|Reset|0|0|0|0|0|0|0|0|0|0|0||0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5||4|3|2|1<br>0|
|R|SBC12|NCE12|0||SBC13|NCE13||0|SBC14|NCE14||0||SBC15|NCE15|0|
|W|W1C|W1C|||W1C|W1C|||W1C|W1C||||W1C|W1C||
|Reset|0|0|0|0|0|0|0|0|0|0|0||0|0|0|0<br>0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1700 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Fields 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/049_Error_Reporting_Module_-ERM-/S32K3XXRM_数据表.pdf-1701-03.png)


<!-- Start of picture text -->
Field Function<br>31 SBC8<br>SBC8 Memory 8 Single-Bit Correction Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ESCIE8]<br>is enabled.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 SR1 —<br>ERM_1 — SR1<br>0b - No single-bit correction event on Memory 8 detected.<br>1b - Single-bit correction event on Memory 8 detected.<br>30 NCE8<br>NCE8 Memory 8 Non-Correctable Error Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ENCIE8]<br>is enabled.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 SR1 —<br>ERM_1 — SR1<br>0b - No non-correctable error event on Memory 8 detected.<br>1b - Non-correctable error event on Memory 8 detected.<br>29-28 Reserved<br>—<br>27 SBC9<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1701 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/049_Error_Reporting_Module_-ERM-/S32K3XXRM_数据表.pdf-1702-03.png)


<!-- Start of picture text -->
Field Function<br>SBC9 Memory 9 Single-Bit Correction Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ESCIE9]<br>is enabled.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 SR1 —<br>ERM_1 — SR1<br>0b - No single-bit correction event on Memory 9 detected.<br>1b - Single-bit correction event on Memory 9 detected.<br>26 NCE9<br>NCE9 Memory 9 Non-Correctable Error Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ENCIE9]<br>is enabled.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 SR1 —<br>ERM_1 — SR1<br>0b - No non-correctable error event on Memory 9 detected.<br>1b - Non-correctable error event on Memory 9 detected.<br>25-24 Reserved<br>—<br>23 SBC10<br>SBC10 Memory 10 Single-Bit Correction Event<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1702 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 

|Field|Function<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ESCIE10]<br>is enabled.<br>0b - No single-bit correction event on Memory 10 detected.<br>1b - Single-bit correction event on Memory 10 detected.|
|---|---|
|22<br>NCE10|NCE10<br>Memory 10 Non-Correctable Error Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ENCIE10]<br>is enabled.<br>0b - No non-correctable error event on Memory 10 detected.<br>1b - Non-correctable error event on Memory 10 detected.|
|21-20<br>—<br>19<br>SBC11|Reserved<br>SBC11<br>Memory 11 Single-Bit Correction Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ESCIE11]<br>is enabled.<br>0b - No single-bit correction event on Memory 11 detected.<br>1b - Single-bit correction event on Memory 11 detected.|
|18<br>NCE11|NCE11<br>Memory 11 Non-Correctable Error Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ENCIE11]<br>is enabled.<br>0b - No non-correctable error event on Memory 11 detected.<br>1b - Non-correctable error event on Memory 11 detected.|
|17-16<br>—|Reserved|
|15<br>SBC12|SBC12<br>Memory 12 Single-Bit Correction Event<br>This field is initialized by hardware reset.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1703 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 

|Field|Function||
|---|---|---|
||Write 1 to clear this field. This write also clears the corresponding inte<br>is enabled.<br>0b - No single-bit correction event on Memory 12 detected.<br>1b - Single-bit correction event on Memory 12 detected.|rrupt notification, if CR1[ESCIE12]|
|14|NCE12||
|NCE12|Memory 12 Non-Correctable Error Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding inte<br>is enabled.<br>0b - No non-correctable error event on Memory 12 detected.<br>1b - Non-correctable error event on Memory 12 detected.|rrupt notification, if CR1[ENCIE12]|
|13-12<br>—|Reserved||
|11<br>SBC13|SBC13<br>Memory 13 Single-Bit Correction Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding inte<br>is enabled.<br>This field is not supported in every instance. The following table<br>supported registers.<br>~~NOTE~~|rrupt notification, if CR1[ESCIE13]<br>includes only|
||Instance<br>Field supported in|Field not supported in|
||ERM_0<br>SR1|—|
||ERM_1<br>—|SR1|
||0b - No single-bit correction event on Memory 13 detected.<br>1b - Single-bit correction event on Memory 13 detected.||
|10<br>NCE13|NCE13<br>Memory 13 Non-Correctable Error Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding inte<br>is enabled.<br>Table continues on the next page...|rrupt notification, if CR1[ENCIE13]|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1704 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/049_Error_Reporting_Module_-ERM-/S32K3XXRM_数据表.pdf-1705-03.png)


<!-- Start of picture text -->
Field Function<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 SR1 —<br>ERM_1 — SR1<br>0b - No non-correctable error event on Memory 13 detected.<br>1b - Non-correctable error event on Memory 13 detected.<br>9-8 Reserved<br>—<br>7 SBC14<br>SBC14 Memory 14 Single-Bit Correction Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ESCIE14]<br>is enabled.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 SR1 —<br>ERM_1 — SR1<br>0b - No single-bit correction event on Memory 14 detected.<br>1b - Single-bit correction event on Memory 14 detected.<br>6 NCE14<br>NCE14 Memory 14 Non-Correctable Error Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ENCIE14]<br>is enabled.<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1705 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/049_Error_Reporting_Module_-ERM-/S32K3XXRM_数据表.pdf-1706-03.png)


<!-- Start of picture text -->
Field Function<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 SR1 —<br>ERM_1 — SR1<br>0b - No non-correctable error event on Memory 14 detected.<br>1b - Non-correctable error event on Memory 14 detected.<br>5-4 Reserved<br>—<br>3 SBC15<br>SBC15 Memory 15 Single-Bit Correction Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ESCIE15]<br>is enabled.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 SR1 —<br>ERM_1 — SR1<br>0b - No single-bit correction event on Memory 15 detected.<br>1b - Single-bit correction event on Memory 15 detected.<br>2 NCE15<br>NCE15 Memory 15 Non-Correctable Error Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ENCIE15]<br>is enabled.<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1706 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/049_Error_Reporting_Module_-ERM-/S32K3XXRM_数据表.pdf-1707-03.png)


<!-- Start of picture text -->
Field Function<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 SR1 —<br>ERM_1 — SR1<br>0b - No non-correctable error event on Memory 15 detected.<br>1b - Non-correctable error event on Memory 15 detected.<br>1-0 Reserved<br>—<br><!-- End of picture text -->

### 49.5.7 ERM Status Register 2 (SR2) 

#### Offset 

|Register|Offset|
|---|---|
|SR2|18h|



#### Function 

This 32-bit status register reports error events for available channels. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|SBC16|NCE16|0||SBC17|NCE17||0|SBC18|NCE18||0|SBC19|NCE19||0|
|W|W1C|W1C|||W1C|W1C|||W1C|W1C|||W1C|W1C|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||0||||0||||0||||0|||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1707 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Fields 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/049_Error_Reporting_Module_-ERM-/S32K3XXRM_数据表.pdf-1708-03.png)


<!-- Start of picture text -->
Field Function<br>31 SBC16<br>SBC16 Memory 16 Single-Bit Correction Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR2[ESCIE16]<br>is enabled.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 SR2 —<br>ERM_1 — SR2<br>0b - No single-bit correction event on Memory 16 detected.<br>1b - Single-bit correction event on Memory 16 detected.<br>30 NCE16<br>NCE16 Memory 16 Non-Correctable Error Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR2[ENCIE16]<br>is enabled.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 SR2 —<br>ERM_1 — SR2<br>0b - No non-correctable error event on Memory 16 detected.<br>1b - Non-correctable error event on Memory 16 detected.<br>29-28 Reserved<br>—<br>27 SBC17<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1708 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|SBC17|Memory 17 Single-Bit Correction Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR2[ESCIE17]<br>is enabled.<br>0b - No single-bit correction event on Memory 17 detected.<br>1b - Single-bit correction event on Memory 17 detected.|
|26<br>NCE17|NCE17<br>Memory 17 Non-Correctable Error Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR2[ENCIE17]<br>is enabled.<br>0b - No non-correctable error event on Memory 17 detected.<br>1b - Non-correctable error event on Memory 17 detected.|
|25-24<br>—<br>23<br>SBC18|Reserved<br>SBC18<br>Memory 18 Single-Bit Correction Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR2[ESCIE18]<br>is enabled.<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>~~NOTE~~|
||Instance<br>Field supported in<br>Field not supported in|
||ERM_0<br>SR2<br>—|
||ERM_1<br>—<br>SR2|
||0b - No single-bit correction event on Memory 18 detected.<br>1b - Single-bit correction event on Memory 18 detected.|
|22|NCE18|
|NCE18|Memory 18 Non-Correctable Error Event<br>This field is initialized by hardware reset.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1709 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/049_Error_Reporting_Module_-ERM-/S32K3XXRM_数据表.pdf-1710-03.png)


<!-- Start of picture text -->
Field Function<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR2[ENCIE18]<br>is enabled.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 SR2 —<br>ERM_1 — SR2<br>0b - No non-correctable error event on Memory 18 detected.<br>1b - Non-correctable error event on Memory 18 detected.<br>21-20 Reserved<br>—<br>19 SBC19<br>SBC19 Memory 19 Single-Bit Correction Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR2[ESCIE19]<br>is enabled.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 SR2 —<br>ERM_1 — SR2<br>0b - No single-bit correction event on Memory 19 detected.<br>1b - Single-bit correction event on Memory 19 detected.<br>18 NCE19<br>NCE19 Memory 19 Non-Correctable Error Event<br>This field is initialized by hardware reset.<br>Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR2[ENCIE19]<br>is enabled.<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1710 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/049_Error_Reporting_Module_-ERM-/S32K3XXRM_数据表.pdf-1711-03.png)


<!-- Start of picture text -->
Field Function<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>ERM_0 SR2 —<br>ERM_1 — SR2<br>0b - No non-correctable error event on Memory 19 detected.<br>1b - Non-correctable error event on Memory 19 detected.<br>17-16 Reserved<br>—<br>15-12 Reserved<br>—<br>11-8 Reserved<br>—<br>7-4 Reserved<br>—<br>3-0 Reserved<br>—<br><!-- End of picture text -->

### 49.5.8 ERM Memory a Error Address Register (EAR0 - EAR19) 

#### Offset 

|Register|Offset|
|---|---|
|EAR0|100h|
|EAR1|110h|
|EAR10|1A0h|
|EAR11|1B0h|
|EAR12|1C0h|
|EAR13|1D0h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1711 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 

|Register|Offset|
|---|---|
|EAR14|1E0h|
|EAR15|1F0h|
|EAR16|200h|
|EAR17|210h|
|EAR18|220h|
|EAR19|230h|



#### Function 

Each ERM Memory n Error Address Register is a 32-bit register for capturing the address of the last ECC event in Memory n, where n denotes the memory channel. Any attempted write to EARn is ignored. 

~~<mark>NOTE</mark>~~ Each module instance supports a different number of registers. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/049_Error_Reporting_Module_-ERM-/S32K3XXRM_数据表.pdf-1712-07.png)


<!-- Start of picture text -->
Instance Register supported Register not supported<br>ERM_0 EAR0–EAR1 —<br>EAR10–EAR19<br>ERM_1 EAR0 EAR1<br>EAR10–EAR12 EAR13–EAR16<br>EAR17 EAR18–EAR19<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R EAR<br>W<br>Reset See Register reset values.<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R EAR<br>W<br>Reset See Register reset values.<br><!-- End of picture text -->

#### Register reset values 

|Register|Reset value|
|---|---|
|EAR0|ERM_0,ERM_1: 0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1712 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 

|Register|Reset value|
|---|---|
|EAR1|0000_0000h|
|EAR2–EAR9|Register not supported|
|EAR10–EAR12|ERM_0,ERM_1: 0000_0000h|
|EAR13–EAR16|0000_0000h|
|EAR17|ERM_0,ERM_1: 0000_0000h|
|EAR18–EAR19|0000_0000h|



#### Fields 

|Field|Function|
|---|---|
|31-0|EAR|
|EAR|Memory n Error Address — This field contains the faulting system address of the last recorded ECC event<br>on Memory n.|



### 49.5.9 ERM Memory a Syndrome Register (SYN0 - SYN16) 

#### Offset 

|Register|Offset|
|---|---|
|SYN0|104h|
|SYN1|114h|
|SYN10|1A4h|
|SYN11|1B4h|
|SYN12|1C4h|
|SYN13|1D4h|
|SYN14|1E4h|
|SYN15|1F4h|
|SYN16|204h|



#### Function 

The ERM Memory n Syndrome Register is a 32-bit register for capturing the calculated syndrome of the last ECC event on Memory n, where n denotes the memory channel. Any attempted write to SYNn is ignored. The syndrome value identifies the pertinent bit position on a correctable, single-bit data inversion or a non-correctable, single-bit address inversion. The syndrome value does not provide any additional diagnostic information on non-correctable, multi-bit inversions. 

Each module instance supports a different number of registers. 

~~<mark>NOTE</mark>~~ 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1713 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/049_Error_Reporting_Module_-ERM-/S32K3XXRM_数据表.pdf-1714-02.png)


<!-- Start of picture text -->
Instance Register supported Register not supported<br>ERM_0 SYN0–SYN1 —<br>SYN10–SYN16<br>ERM_1 SYN0 SYN1<br>SYN10–SYN12 SYN13–SYN16<br><!-- End of picture text -->

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/049_Error_Reporting_Module_-ERM-/S32K3XXRM_数据表.pdf-1714-04.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R SYNDROME  0<br>W<br>Reset See Register reset values.<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W<br>Reset See Register reset values.<br><!-- End of picture text -->

#### Register reset values 

|Register|Reset value|
|---|---|
|SYN0|ERM_0,ERM_1: 0000_0000h|
|SYN1|0000_0000h|
|SYN2–SYN9|Register not supported|
|SYN10–SYN12|ERM_0,ERM_1: 0000_0000h|
|SYN13–SYN16|0000_0000h|



#### Fields 

|Field|Function|
|---|---|
|31-24|SYNDROME|
|SYNDROME|Memory n Syndrome — This field contains the ECC syndrome associated with the last recorded ECC event<br>on Memory n.|
|23-0<br>—|Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1714 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

### 49.5.10 ERM Memory a Correctable Error Count Register (CORR_ERR_CNT0 - CORR_ERR_CNT19) 

#### Offset 

|Registe|r|Offset|
|---|---|---|
|CORR_|ERR_CNT0|108h|
|CORR_|ERR_CNT1|118h|
|CORR_|ERR_CNT2|128h|
|CORR_|ERR_CNT3|138h|
|CORR_|ERR_CNT4|148h|
|CORR_|ERR_CNT5|158h|
|CORR_|ERR_CNT6|168h|
|CORR_|ERR_CNT7|178h|
|CORR_|ERR_CNT8|188h|
|CORR_|ERR_CNT9|198h|
|CORR_|ERR_CNT10|1A8h|
|CORR_|ERR_CNT11|1B8h|
|CORR_|ERR_CNT12|1C8h|
|CORR_|ERR_CNT13|1D8h|
|CORR_|ERR_CNT14|1E8h|
|CORR_|ERR_CNT15|1F8h|
|CORR_|ERR_CNT16|208h|
|CORR_|ERR_CNT17|218h|
|CORR_|ERR_CNT18|228h|
|CORR_|ERR_CNT19|238h|



#### Function 

Each 32-bit ERM Memory n Correctable Error Count Register records the count value of the number of correctable ECC error events for Memory n, where n denotes the memory channel. 

~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

||Instance|Register supported|Register not supported|
|---|---|---|---|
|ERM_0||CORR_ERR_CNT0–CORR_ERR_CNT1|—|
|||CORR_ERR_CNT2–CORR_ERR_CNT5||
|||CORR_ERR_CNT6–CORR_ERR_CNT9||
|||CORR_ERR_CNT10–CORR_ERR_CNT12||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1715 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/049_Error_Reporting_Module_-ERM-/S32K3XXRM_数据表.pdf-1716-03.png)


<!-- Start of picture text -->
Instance Register supported Register not supported<br>CORR_ERR_CNT13–CORR_ERR_CNT16<br>CORR_ERR_CNT17<br>CORR_ERR_CNT18–CORR_ERR_CNT19<br>ERM_1 CORR_ERR_CNT0–CORR_ERR_CNT17 CORR_ERR_CNT1<br>CORR_ERR_CNT6–CORR_ERR_CNT9<br>CORR_ERR_CNT13–CORR_ERR_CNT16<br>CORR_ERR_CNT18–CORR_ERR_CNT19<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/049_Error_Reporting_Module_-ERM-/S32K3XXRM_数据表.pdf-1716-04.png)


<!-- Start of picture text -->
Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved<br>W 0<br>Reset See Register reset values.<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved  COUNT<br>W 0 0<br>Reset See Register reset values.<br><!-- End of picture text -->

#### Register reset values 

|Register|Reset value|
|---|---|
|CORR_ERR_CNT0|ERM_0,ERM_1: 0000_0000h|
|CORR_ERR_CNT1|0000_0000h|
|CORR_ERR_CNT2–CORR_ERR_CNT5|ERM_0,ERM_1: 0000_0000h|
|CORR_ERR_CNT2–CORR_ERR_CNT19|Register not supported|
|CORR_ERR_CNT6–CORR_ERR_CNT9|0000_0000h|
|CORR_ERR_CNT10–CORR_ERR_CNT12|ERM_0,ERM_1: 0000_0000h|
|CORR_ERR_CNT13–CORR_ERR_CNT16|0000_0000h|
|CORR_ERR_CNT17|ERM_0,ERM_1: 0000_0000h|
|CORR_ERR_CNT18–CORR_ERR_CNT19|0000_0000h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1716 / 4640 

NXP Semiconductors 

Error Reporting Module (ERM) 

#### Fields 

|Field|Function|
|---|---|
|31-8|Reserved|
|—||
|7-0|Memory n Correctable Error Count|
|COUNT|For each correctable error event, the ERM increments this field's error count value until the counter reaches<br>its maximum value FFh. COUNT field description can be updated as required. COUNT value will stop once<br>it reaches maximum value FFh and will not wrap even if error occurs.|
||Read this field to determine the correctable error count value so far.|
||Write all zeros to this field to reset the counter. Writing non-zero (or partial zero) values has no effect.|



## 49.6 Glossary 

#### ECC 

Error correction code 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1717 / 4640 

