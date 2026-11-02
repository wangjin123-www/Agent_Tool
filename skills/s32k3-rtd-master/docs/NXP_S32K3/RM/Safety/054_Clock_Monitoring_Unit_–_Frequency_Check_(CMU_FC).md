NXP Semiconductors 

# Chapter 54 Clock Monitoring Unit – Frequency Check (CMU_FC) 

## 54.1 Chip-specific CMU_FC information 

### 54.1.1 CMU_FC configuration 

The device consists of a robust clock monitoring architecture targeted to monitor various clock nodes to ensure device clock robustness. There are 6 clock monitoring units present in the device out of which 4 are of type CMU_FC. See 'Clock monitoring' section in Clocking chapter for details on device clock monitoring architecture. 

~~<mark>NOTE</mark>~~ 

CMU_5 is accessible by Cortex-M0+ core only. 

CMU_FC combined spec variation: The combined spec variation for CMU (used for configuring CMU_FCx.HTCR[HFREF] and CMU_FCx.HTCR[LFREF]) is the absolute sum of frequency variations of the clock sources. Refer device datasheet for frequency variations for the corresponding clock sources. 

## 54.2 Introduction 

CMU_FC ensures the clock integrity of selected clocks and allows continuous clock integrity verification. 

CMU_FC checks if the frequency of a monitored clock (monitored_clock) is within a programmable frequency range specified by the user. If the frequency is outside the specified limits, it could lead to performance, protocol, and timing failures. CMU_FC requires a clock used as a base reference for the frequency check operation. This reference clock (reference_clock) must be within documented limits for correct CMU_FC operation. 

### 54.2.1 Basic operation 

CMU_FC counts clock cycles of the monitored clock during a user programmable time duration of n clock cycles of the reference clock. There is a comparison between the final count of the monitored clock and the user programmable upper and lower threshold count limits. The control logic determines whether the cycle count is within the programmed limits. If not it sets the Frequency Higher than High frequency reference threshold event status (FHH) field or the Frequency Lower than Low frequency reference threshold event status (FLL) field in the Status Register (SR). If you enable interrupts, an interrupt asserts when the status flag sets. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1845 / 4640 

NXP Semiconductors 

Clock Monitoring Unit – Frequency Check (CMU_FC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/054_Clock_Monitoring_Unit_-_Frequency_Check_-CMU_FC-/S32K3XXRM_数据表.pdf-1846-02.png)


<!-- Start of picture text -->
Checking window<br>=<br>Enable<br>Reference counter<br>reference_clock<br>SR[FHH]<br>Control logic<br>SR[FLL]<br>monitored_cloc k Monitor counter<br>><br>High threshold<br><<br>Low threshold<br><!-- End of picture text -->

Figure 201. CMU_FC block diagram 

CMU_FC cannot detect the following: 

- Monitored clock duty cycle variations 

- Instantaneous monitored clock frequency variations that do not cross upper or lower threshold limits 

### 54.2.2 Features 

The CMU_FC features are: 

- Programmable duration of reference clock cycles 

- Initiates an event if a monitored clock frequency is higher than high frequency reference (FHH) 

- Initiates an event if a monitored clock frequency is lower than low frequency reference (FLL) 

- Timeout functionality generates an FLL event if a monitored clock stops functioning 

- Masking of FHH event interrupt 

- Masking of FLL event interrupt 

Table 266. Clock description 

|Clock|I/O|Description|
|---|---|---|
|reference_clock|I|Clock signal that the module uses as a<br>reference to evaluate monitored_clock|
|monitored_clock|I|Clock signal on which frequency check<br>is performed|
|bus_clock|I|Clock signal on which register read/write<br>operation is performed|



~~<mark>NOTE</mark>~~ 

See the Clocking chapter for details of monitored and reference clocks used on this chip. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1846 / 4640 

NXP Semiconductors 

Clock Monitoring Unit – Frequency Check (CMU_FC) 

## 54.3 Functional description 

### 54.3.1 Frequency checking 

Frequency checking starts when software writes GCR[FCE] = 1. The Run Status field SR[RS] shows 1 after frequency check operation starts. 

CMU_FC performs continuous periodic clock checking of the monitored clock. Each checking window involves the following operations: 

- Stage 1 – Reference clock counter runs for RCCR[REF_CNT] reference clock cycles. Monitored clock counter runs in parallel for the same time duration as reference clock counter. 

- Stage 2 – After stage 1, the module compares the final monitored clock count against the programmed thresholds. 

If the monitored clock count is greater than the high threshold value in HTCR[HFREF], an FHH event occurs. 

If the monitored clock count is lower than the low threshold value in LTCR[LFREF], an FLL event occurs. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/054_Clock_Monitoring_Unit_-_Frequency_Check_-CMU_FC-/S32K3XXRM_数据表.pdf-1847-10.png)


<!-- Start of picture text -->
FHH event generation<br>High Frequency ReferenceThreshold (HFREF)<br>Monitored clock count (Typ)<br>Low Frequency ReferenceThreshold(LFREF)<br>FLL event generation<br>0<br>Clock count<br>Healthy clock zone<br><!-- End of picture text -->

Figure 202. Frequency checking HFREF and LFREF thresholds 

#### 54.3.1.1 Monitored clock lost 

If a monitored clock ceases operation before evaluation of that clock (Stage 2, see Frequency checking), CMU_FC waits for RCCR[REF_CNT] reference clock periods by extending Stage 2 before triggering an FLL event. 

- If monitored_clock is not running when enabling CMU_FC: 

Worst case FLL response time = (2 × RCCR[REF_CNT] + 12) reference_clock cycles + 15 bus_clock cycles 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1847 / 4640 

NXP Semiconductors 

Clock Monitoring Unit – Frequency Check (CMU_FC) 

- If monitored_clock stops when the CMU_FC is running: 

Worst case FLL response time = (2 × RCCR[REF_CNT] + 2) reference_clock cycles + 3 bus_clock cycles 

## 54.4 Programming guidelines 

### 54.4.1 Programming RCCR[REF_CNT] 

RCCR[REF_CNT] defines the duration of the checking operation in number of reference_clock cycles. The minimum RCCR[REF_CNT] value can be calculated using the following formula: 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/054_Clock_Monitoring_Unit_-_Frequency_Check_-CMU_FC-/S32K3XXRM_数据表.pdf-1848-07.png)


<!-- Start of picture text -->
reference_clock reference_clock<br>Minimum RCCR [REF_CNT]  = CEILING value of MAX 3 X , 8 + 5 X<br>bus_clock monitored_clock<br><!-- End of picture text -->

...where: 

- freference_clock is the frequency of the reference clock 

- fbus_clock is the frequency of the bus clock 

- fmonitored_clock is the frequency of the monitored clock 

Example to determine RCCR[REF_CNT]: 

- fbus_clock = 16 MHz 

- freference_clock = 8 MHz 

- fmonitored_clock = 48 MHz 

##### <u>Formula #1:</u> 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/054_Clock_Monitoring_Unit_-_Frequency_Check_-CMU_FC-/S32K3XXRM_数据表.pdf-1848-17.png)


<!-- Start of picture text -->
reference_clock<br>3 X<br>bus_clock<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/054_Clock_Monitoring_Unit_-_Frequency_Check_-CMU_FC-/S32K3XXRM_数据表.pdf-1848-18.png)


<!-- Start of picture text -->
Inserting the values: 3 × (8 / 16) = 1.5<br><!-- End of picture text -->

##### <u>Formula #2:</u> 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/054_Clock_Monitoring_Unit_-_Frequency_Check_-CMU_FC-/S32K3XXRM_数据表.pdf-1848-20.png)


<!-- Start of picture text -->
reference_clock<br>8 + 5 X<br>monitored_clock<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/054_Clock_Monitoring_Unit_-_Frequency_Check_-CMU_FC-/S32K3XXRM_数据表.pdf-1848-21.png)


<!-- Start of picture text -->
Inserting the values: 8 + 5 × (8 / 48) ≈ 8.83<br>MAX (1.5, 8.83): 8.83<br>CEILING value of MAX: 9<br>Therefore, minimum RCCR[REF_CNT]: 9<br><!-- End of picture text -->

Programmed RCCR[REF_CNT] value must be greater than or equal to the calculated minimum value and should be decided after considering application requirements of frequency check completion response time and overall accuracy required from CMU_FC. 

- Higher values of RCCR[REF_CNT] results in longer measurement window, leading to better accuracy in monitored clock check. 

- Lower values of RCCR[REF_CNT] results in shorter measurement window, leading to faster FHH and FLL event response, but higher inaccuracy in reported result. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1848 / 4640 

NXP Semiconductors 

Clock Monitoring Unit – Frequency Check (CMU_FC) 

For measurement window calculation, see step 8 in Programming HFREF and LFREF 

### 54.4.2 Programming HFREF and LFREF 

You must consider the following when programming HFREF/LFREF: 

- Tolerable monitored clock frequency variation 

- Maximum reference clock frequency variation 

- Inherent module inaccuracy 

CMU_FC has an expected maximum deviation of ± 3 monitored_clock cycles (CMU_FCVAR+ = 3, CMU_FCVAR- = –3). 

The following procedure shows how to calculate optimum values for HTCR[HFREF] and LTCR[LFREF] (numbers shown are from example in table): 

1. Determine the ideal monitored_clock frequency (fmonitored_clock (ideal), 48 MHz). 

2. Determine the specified variation of the monitored_clock (1.1%). 

3. Calculate monitored_clock frequency variation: . 

_monitored_clock_ 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/054_Clock_Monitoring_Unit_-_Frequency_Check_-CMU_FC-/S32K3XXRM_数据表.pdf-1849-14.png)


<!-- Start of picture text -->
X step 2<br><!-- End of picture text -->

   - fmonitored_clock (max) = 48 MHz × (1 + (1.1 ÷ 100)) = 48.53 MHz 

   - fmonitored_clock (min)= 48 MHz × (1 – (1.1 ÷ 100)) = 47.47 MHz 

4. Determine the ideal reference_clock frequency (freference_clock (ideal), 8 MHz). 

5. Determine the specified variation of the reference_clock (3.3%). 

6. Calculate ideal reference_clock frequency variation: 

_reference_clock_ 

##### X step 5 

   - freference_clock (max) = 8 MHz × (1 + (3.3 ÷ 100)) = 8.26 MHz 

   - freference_clock (min) = 8 MHz × (1 – (3.3 ÷ 100)) = 7.74 MHz 

7. Select the value of RCCR[REF_CNT] needed (80). See Programming RCCR[REF_CNT]. 

8. Calculate ideal measurement window: 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/054_Clock_Monitoring_Unit_-_Frequency_Check_-CMU_FC-/S32K3XXRM_数据表.pdf-1849-26.png)


<!-- Start of picture text -->
_<br>reference_clock<br><!-- End of picture text -->

   - 80 ÷ 8 MHz = 10000 ns 

9. Calculate ideal monitored_clock count: 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/054_Clock_Monitoring_Unit_-_Frequency_Check_-CMU_FC-/S32K3XXRM_数据表.pdf-1849-29.png)


<!-- Start of picture text -->
_<br>reference_clock<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/054_Clock_Monitoring_Unit_-_Frequency_Check_-CMU_FC-/S32K3XXRM_数据表.pdf-1849-30.png)


<!-- Start of picture text -->
monitored_clock<br><!-- End of picture text -->

   - 80 ÷ 8 MHz × 48 MHz = 480.00 (round off this value, 480 in this case) 

10. Calculate high threshold value (HTCR[HFREF]): 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1849 / 4640 

NXP Semiconductors 

Clock Monitoring Unit – Frequency Check (CMU_FC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/054_Clock_Monitoring_Unit_-_Frequency_Check_-CMU_FC-/S32K3XXRM_数据表.pdf-1850-02.png)


<!-- Start of picture text -->
monitored_clock<br>Ceiling value of<br>reference_clock<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/054_Clock_Monitoring_Unit_-_Frequency_Check_-CMU_FC-/S32K3XXRM_数据表.pdf-1850-03.png)


<!-- Start of picture text -->
_ _ +<br><!-- End of picture text -->

   - HTCR[HFREF] = Ceiling(48.53 MHz ÷ 7.74 MHz × 80 + 3) = 505 

11. Calculate low threshold value (LTCR[LFREF]): 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/054_Clock_Monitoring_Unit_-_Frequency_Check_-CMU_FC-/S32K3XXRM_数据表.pdf-1850-06.png)


<!-- Start of picture text -->
monitored_clock<br>Floor value of  reference_clock _ - _ -<br><!-- End of picture text -->

- LTCR[LFREF] = Floor(47.47 MHz ÷ 8.26 MHz × 80 – 3) = 456 

##### Table 267. HTCR[HFREF] and LTCR[LFREF] calculation example 

|Property|Value|Unit|
|---|---|---|
|Bus clock frequency (fbus_clock)|16|MHz|
|Monitored clock frequency (fmonitored_clock(ideal))|48|MHz|
|Specified variation of monitored clock|1.1|%|
|Monitored clock frequency (maximum after specified variation,<br>fmonitored_clock(max))|48.53|MHz|
|Monitored clock frequency (minimum after specified variation,<br>fmonitored_clock(min))|47.47|MHz|
|Reference clock frequency (freference_clock(ideal))|8|MHz|
|Specified variation of reference clock|3.3|%|
|Reference clock frequency (maximum after specified variation,<br>freference_clock(max))|8.26|MHz|
|Reference clock frequency (minimum after specified variation,<br>freference_clock(min))|7.74|MHz|
|Minimum reference count (RCCR[REF_CNT])|9|—|
|Programmed reference count (RCCR[REF_CNT])<br>(must be ≥ minimum RCCR[REF_CNT])|80|—|
|Measurement window|10000.00|ns|
|Calculated monitored clock count|480.00|—|
|Calculated monitored clock Count (rounded)|480|—|
|Module positive variation (CMU_FCVAR+)|3|—|
|Module negative variation (CMU_FCVAR-)|-3|—|
|Programmed higher threshold (HTCR[HFREF])|505|—|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1850 / 4640 

NXP Semiconductors 

Clock Monitoring Unit – Frequency Check (CMU_FC) 

Table 267. HTCR[HFREF] and LTCR[LFREF] calculation example (continued) 

|Property|Value|Unit|
|---|---|---|
|Programmed lower threshold (LTCR[LFREF])|456|—|



### 54.4.3 Module programming sequence 

The recommended programming sequence for CMU_FCfrequency checking is: 

1. In any order, complete the following: 

   - Program RCCR[REF_CNT] to define the frequency measuring window duration in reference_clock cycles. 

   - Program LTCR[LFREF] and HTCR[HFREF] to set the permissible frequency range of the monitored_clock. 

   - Program IER to enable interrupt. 

2. Write GCR[FCE] = 1 to start the frequency check operation. 

~~<mark>NOTE</mark>~~ When GCR[FCE] = 1, you must not write to RCCR, HTCR, LTCR, or IER. Attempting to do so generates a bus transfer error. 

3. To reconfigure RCCR, LTCR, HTCR , and IER or to stop frequency check operation, wait for SR[RS] = 1, then write GCR[FCE] = 0. 

## 54.5 CMU_FC register descriptions 

### 54.5.1 CMU_FC memory map 

This section describes the address order of all the CMU_FC registers. Each description includes a standard register diagram and associated field descriptions. 

CMU_0 base address: 402B_C000h 

CMU_3 base address: 402B_C060h 

CMU_4 base address: 402B_C080h 

CMU_5 base address: 402B_C0A0h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|Global Configuration Register (GCR)|32|RW|0000_0000h|
|4h|Reference Count Configuration Register (RCCR)|32|RW|0000_0000h|
|8h|High Threshold Configuration Register (HTCR)|32|RW|00FF_FFFFh|
|Ch|Low Threshold Configuration Register (LTCR)|32|RW|0000_0000h|
|10h|Status Register (SR)|32|W1C|0000_0000h|
|14h|Interrupt Enable Register (IER)|32|RW|0000_0000h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1851 / 4640 

NXP Semiconductors 

Clock Monitoring Unit – Frequency Check (CMU_FC) 

### 54.5.2 Global Configuration Register (GCR) 

##### Offset 

|Register|Offset|
|---|---|
|GCR|0h|



##### Function 

Controls module level configurations such as enabling frequency check. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/054_Clock_Monitoring_Unit_-_Frequency_Check_-CMU_FC-/S32K3XXRM_数据表.pdf-1852-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>FCE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-1|Reserved|
|—||
|0|Frequency Check Enable|
|FCE|Starts or stops frequency checking. FCE is disabled by default. Software can enable FCE at any time. To<br>stop the ongoing operation, write 0 to FCE only whenSR[RS]= 1.|
||0b - Stops frequency checking|
||1b - Starts frequency checking|



### 54.5.3 Reference Count Configuration Register (RCCR) 

##### Offset 

|Register|Offset|
|---|---|
|RCCR|4h|



##### Function 

Programs reference count duration of the frequency check window. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1852 / 4640 

NXP Semiconductors 

Clock Monitoring Unit – Frequency Check (CMU_FC) 

~~<mark>NOTE</mark>~~ 

Write to RCCR only when GCR[FCE] = 0. A bus transfer error results if software writes RCCR when GCR[FCE] = 1. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||||||||0||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||REF|_CNT||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-16|Reserved|
|—||
|15-0|Reference clock count|
|REF_CNT|Total number of counts of reference_clock for which frequency check runs. This field defines the duration<br>of one frequency check window. SeeProgramming RCCR[REF_CNT]for RCCR calculation.|



### 54.5.4 High Threshold Configuration Register (HTCR) 

##### Offset 

|Register|Offset|
|---|---|
|HTCR|8h|



##### Function 

Determines the high threshold limit of the monitored clock counter. 

~~<mark>NOTE</mark>~~ 

Write HTCR only when GCR[FCE] = 0. A bus transfer error results if software writes HTCR when GCR[FCE] = 1. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1853 / 4640 

NXP Semiconductors 

Clock Monitoring Unit – Frequency Check (CMU_FC) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/054_Clock_Monitoring_Unit_-_Frequency_Check_-CMU_FC-/S32K3XXRM_数据表.pdf-1854-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>HFREF<br>W<br>Reset 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>HFREF<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-24<br>—|Reserved|
|23-0|High frequency reference threshold|
|HFREF|HFREF determines the high reference value for the monitored clock frequency.|
||SeeProgramming HFREF and LFREFfor HFREF calculation.|
||Do not program HFREF to a value greater than 0x00FFFFFC.<br>~~NOTE~~|



### 54.5.5 Low Threshold Configuration Register (LTCR) 

##### Offset 

|Register|Offset|
|---|---|
|LTCR|Ch|



##### Function 

Determines the low threshold limit of the monitored clock counter. 

~~<mark>NOTE</mark>~~ 

Write LTCR only when GCR[FCE] = 0. A bus transfer error results if software writes LTCR when GCR[FCE] = 1. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1854 / 4640 

NXP Semiconductors 

Clock Monitoring Unit – Frequency Check (CMU_FC) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/054_Clock_Monitoring_Unit_-_Frequency_Check_-CMU_FC-/S32K3XXRM_数据表.pdf-1855-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>LFREF<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>LFREF<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-24<br>—|Reserved|
|23-0|Low Frequency Reference Threshold|
|LFREF|LFREF determines the low reference value for the monitored clock frequency.|
||SeeProgramming HFREF and LFREFfor LFREF calculation.|
||Do not program LFREF to a value less than 0x00000003.<br>~~NOTE~~|



### 54.5.6 Status Register (SR) 

##### Offset 

|Register|Offset|
|---|---|
|SR|10h|



Function 

Provides the internal status of the module. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1855 / 4640 

NXP Semiconductors 

Clock Monitoring Unit – Frequency Check (CMU_FC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||||0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||0||||||RS|Reser|ved|FHH|FLL|
|W|||||||||||||||W1C|W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-5|Reserved|
|—||
|4|Run Status|
|RS|Shows the running status of module internal operation. After enabling the frequency check operation<br>(GCR[FCE]= 1), there is a fixed delay before this field shows running status. If the system wants<br>to disable the frequency check operation, then the software should read this register and write<br>GCR[FCE]= 0 only when this field is 1.<br>0b - Frequency check stopped<br>1b - Frequency check running|
|3-2<br>—|Reserved|
|1|Frequency higher than high frequency reference threshold event status|
|FHH|Hardware writes 1 to FHH when the monitored clock frequency becomes higher than the high threshold<br>value inHTCR[HFREF]. FHH clears when software writes 1.<br>0b - No FHH event<br>1b - FHH event occurred|
|0<br>FLL|Frequency lower than low frequency reference threshold event status<br>Hardware writes 1 to FLL when the monitored clock frequency becomes lower than the low threshold<br>value inLTCR[LFREF]. FLL clears when software writes 1.<br>0b - No FLL event|
||1b - FLL event occurred|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1856 / 4640 

NXP Semiconductors 

Clock Monitoring Unit – Frequency Check (CMU_FC) 

### 54.5.7 Interrupt Enable Register (IER) 

Offset 

|Register|Offset|
|---|---|
|IER|14h|



##### Function 

Enables CMU_FC interrupts. 

~~<mark>NOTE</mark>~~ 

Write IER only when GCR[FCE] = 0. A bus transfer error results if software writes IER when GCR[FCE] = 1. 

Enable only either asynchronous FHH event interrupt or synchronous FHH event interrupt at a time. 

For example: 

- If IER[FHHIE] is set to 1 then set IER[FHHAIE] to 0. 

- If IER[FHHAIE] is set to 1 then set IER[FHHIE] to 0. 

Enable only either asynchronous FLL event interrupt or synchronous FLL event interrupt at a time. 

For example: 

- If IER[FLLIE] is set to 1 then set IER[FLLAIE] to 0. 

- If IER[FLLAIE] is set to 1 then set IER[FLLIE] to 0. 

See Clocking chapter for interrupt usage information based on CMU_FC instances. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||0||||0|0||0||0|0||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||0|||||||FHHAI<br>E|FLLAI<br>E|FHHIE|FLLIE|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function|
|---|---|
|31-24<br>—|Reserved|
|23|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1857 / 4640 

NXP Semiconductors 

Clock Monitoring Unit – Frequency Check (CMU_FC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|—<br>22<br>—|Reserved|
|21-20<br>—|Reserved|
|19-18<br>—|Reserved|
|17-16<br>—<br>15-4<br>—<br>3<br>FHHAIE|Reserved<br>Reserved<br>Frequency Higher than High Frequency Reference Threshold Asynchronous Interrupt Enable<br>FHHAIE enables FHH asynchronous interrupt at the module boundary.<br>0b - Asynchronous FHH event interrupt disabled<br>1b - Asynchronous FHH event interrupt enabled|
|2<br>FLLAIE|Frequency Lower than Low Frequency Reference Threshold Asynchronous Interrupt Enable<br>FLLAIE enables FLL asynchronous interrupt at the module boundary.<br>0b - Asynchronous FLL event interrupt disabled<br>1b - Asynchronous FLL event interrupt enabled|
|1<br>FHHIE|Frequency Higher than High Frequency Reference Threshold Synchronous Interrupt Enable<br>FHHIE enables an FHH synchronous interrupt at the module boundary.<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>~~NOTE~~|
||Instance<br>Field supported in<br>Field not supported in|
||CMU_0<br>IER<br>—|
||CMU_3<br>—<br>IER<br>CMU_4<br>—<br>IER|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1858 / 4640 

NXP Semiconductors 

Clock Monitoring Unit – Frequency Check (CMU_FC) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/054_Clock_Monitoring_Unit_-_Frequency_Check_-CMU_FC-/S32K3XXRM_数据表.pdf-1859-03.png)


<!-- Start of picture text -->
Field Function<br>Instance Field supported in Field not supported in<br>CMU_5 — IER<br>0b - Synchronous FHH event interrupt disabled<br>1b - Synchronous FHH event interrupt enabled<br>0 Frequency Lower than Low Frequency Reference Threshold Synchronous Interrupt Enable<br>FLLIE FLLIE enables an FLL synchronous interrupt at the module boundary.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>CMU_0 IER —<br>CMU_3 — IER<br>CMU_4 — IER<br>CMU_5 — IER<br>0b - Synchronous FLL event interrupt disabled<br>1b - Synchronous FLL event interrupt enabled<br><!-- End of picture text -->

## 54.6 Glossary 

FHH The state that the monitored clock frequency is higher than the high frequency reference. FHH is also the name of the register field that indicates this state. 

FHH event The event that the module triggers when it detects FHH. 

FLL The state that the monitored clock frequency is lower than the lower frequency reference. FLL is also the name of the register field that indicates this state. 

FLL event The event that the module triggers when it detects FLL. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1859 / 4640 

