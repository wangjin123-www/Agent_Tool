NXP Semiconductors 

# Chapter 55 Clock Monitoring Unit – Frequency Meter (CMU_FM) 

## 55.1 Chip-specific CMU_FM information 

### 55.1.1 CMU_FM configuration 

The device consists of a robust clock monitoring architecture targeted to monitor various clock nodes to ensure device clock robustness. There are 6 clock monitoring units present in the device out of which 2 are of type CMU_FM. See 'Clock monitoring' section in Clocking chapter for details on device clock monitoring architecture. 

~~<mark>NOTE</mark>~~ 

CMU metering interrupt is not generated if the clock which is being metered is lost. A timeout status flag, CMU.SR[FMTO] is updated in this case. 

- ~~<mark>NOTE</mark>~~ 

Software must ensure that CMU1 interrupt is serviced within POR_WDG timeout. In absence of CMU1 interrupt servicing, the POR_WDG detects this as an FIRC failure and initiates a POR recovery. 

## 55.2 Introduction 

CMU_FM measures the frequency of the metered clock (metered_clock) using another clock as reference. This reference clock (reference_clock) must be within documented limits for correct CMU_FM operation. CMU_FM operation is only guaranteed if a reference clock is within normal operating parameters. 

### 55.2.1 Basic operation 

The CMU_FM counts the clock cycles of a metered clock in the user programmable time duration n number of clock cycles of the reference clock. After completion of a metered clock operation, a register field sets, indicating the operation has completed. The count of the metered clock also updates in the Status Register (SR) after completion of a metered clock operation. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/055_Clock_Monitoring_Unit_-_Frequency_Meter_-CMU_FM-/S32K3XXRM_数据表.pdf-1860-13.png)


<!-- Start of picture text -->
Metering window<br>Enable<br>Reference counter<br>reference_clock<br>Control logic SR[FMC]<br>metered_cloc k Meter counter<br>Figure 203. Block diagram<br><!-- End of picture text -->

### 55.2.2 Features 

Features of the CMU_FM are: 

- Programmable duration of reference_clock cycles 

- Maskable interrupt generation when frequency metering completes 

- Timeout feature indicates loss of metered_clock 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1860 / 4640 

NXP Semiconductors 

Clock Monitoring Unit – Frequency Meter (CMU_FM) 

Table 268. Clock description 

|Clock|I/O|Description|
|---|---|---|
|reference_clock|I|Clock signal that the module uses as a<br>reference to evaluate metered_clock|
|metered_clock|I|Clock signal on which frequency<br>metering is performed|
|bus_clock|I|Clock signal on which register read/write<br>operation is performed|



~~<mark>NOTE</mark>~~ See the Clocking chapter for details of metered and reference clocks used on this chip. 

## 55.3 Functional description 

The frequency meter operation initiates when software writes GCR[FME] = 1. When the operation starts, hardware writes SR[RS] = 1. Safety critical applications must poll SR[RS] to determine when metering operation starts. 

Frequency metering window involves these operations: 

1. Stage 1 — The reference clock counter runs for RCCR[REF_CNT] cycles of reference_clock. The metered clock counter runs in parallel for the same time duration as the reference_clock counter. 

2. Stage 2 — At the end of stage 1, SR[FMC] = 1, SR[MET_CNT] updates with the metered_clock count, and CMU_FM writes GCR[FME] = 0. 

## 55.4 Programming guidelines 

### 55.4.1 Programming RCCR[REF_CNT] 

RCCR[REF_CNT] defines the duration of the metering operation in number of reference_clock cycles. The minimum RCCR[REF_CNT] value can be calculated using the following formula: 

_reference_clock reference_clock_ **Minimum RCCR [REF_CNT]** = CEILING value of MAX 3 X , 8 + 5 X _bus_clock monitored_clock_ 

...where: 

- freference_clock is the frequency of the reference clock 

- fbus_clock is the frequency of the bus clock 

- fmetering_clock is the frequency of the metered clock 

Example to determine RCCR[REF_CNT]: 

- fbus_clock = 16 MHz 

- freference_clock = 8 MHz 

- fmetered_clock = 48 MHz 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1861 / 4640 

NXP Semiconductors 

Clock Monitoring Unit – Frequency Meter (CMU_FM) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/055_Clock_Monitoring_Unit_-_Frequency_Meter_-CMU_FM-/S32K3XXRM_数据表.pdf-1862-02.png)


<!-- Start of picture text -->
Formula #1:<br>reference_clock<br>3 X<br>bus_clock<br><!-- End of picture text -->

|Inserting the values:|3 × (8 / 16) = 1.5||
|---|---|---|
|Formula #2:||6 + 4 X<br>_reference_clock_<br>_metered_clock_|
|Inserting the values:|6 + 4 × (8 / 48) ≈ 6.67||
|MAX (1.5, 6.67):|6.67||
|CEILING value of MAX:|7||
|Therefore, minimumRCCR[REF_CNT]:|7||



Programmed RCCR[REF_CNT] value must be greater than or equal to the calculated minimum value and should be decided after considering application requirements of frequency metering completion response time and overall accuracy required from CMU_FM. 

- Higher values of RCCR[REF_CNT] results in longer metering window, leading to better accuracy in metered clock measurement. 

- Lower values of RCCR[REF_CNT] results in shorter metering window, leading to faster FMC response, but higher inaccuracy in reported result. 

### 55.4.2 Module programming sequence 

The recommended programming sequence of CMU_FM is: 

1. In any order, complete the following: 

   - Program RCCR[REF_CNT] to define the frequency metering window duration in reference_clock cycles. 

   - Program IER[FMCIE] to enable interrupt. 

2. Write GCR[FME] = 1 to start frequency metering operation. Writes to RCCR and IER are disabled after GCR[FME] = 1. Attempting a write to any of them after GCR[FME] = 1 generates a bus transfer error. 

3. To reconfigure RCCR and IER or to stop frequency metering operation, wait for SR[RS] = 1, then write GCR[FME] = 0. 

Upon completion of metering operations: 

- Hardware writes SR[FMC] = 1 

- SR[MET_CNT] updates with metered count value 

- Hardware writes GCR[FME] = 0 

## 55.5 CMU_FM register descriptions 

### 55.5.1 CMU_FM memory map 

This section describes the address order of all the CMU_FM registers. Each description includes a standard register diagram and associated field descriptions. 

CMU_1 base address: 402B_C020h 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1862 / 4640 

NXP Semiconductors 

Clock Monitoring Unit – Frequency Meter (CMU_FM) 

CMU_2 base address: 402B_C040h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|Global Configuration Register (GCR)|32|RW|0000_0000h|
|4h|Reference Count Configuration Register (RCCR)|32|RW|0000_0000h|
|8h|Status Register (SR)|32|W1C|0000_0000h|
|Ch|Interrupt Enable Register (IER)|32|RW|0000_0000h|



### 55.5.2 Global Configuration Register (GCR) 

#### Offset 

|Register|Offset|
|---|---|
|GCR|0h|



#### Function 

Controls module level configurations such as enabling frequency metering. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/055_Clock_Monitoring_Unit_-_Frequency_Meter_-CMU_FM-/S32K3XXRM_数据表.pdf-1863-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>FME<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-1|Reserved|
|—||
|0|Frequency Meter Enable|
|FME|Starts or stops frequency metering. FME is disabled by default. Software can enable FME at any time.<br>To stop the ongoing operation, write 0 to FME only whenSR[RS]= 1. FME automatically clears upon<br>frequency metering completion or timeout event.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1863 / 4640 

NXP Semiconductors 

Clock Monitoring Unit – Frequency Meter (CMU_FM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Stops frequency metering|
||1b - Starts frequency metering|



### 55.5.3 Reference Count Configuration Register (RCCR) 

#### Offset 

|Register|Offset|
|---|---|
|RCCR|4h|



#### Function 

Programs reference count duration of the frequency meter window. 

~~<mark>NOTE</mark>~~ Write to RCCR only when GCR[FME] = 0. A bus transfer error results if software writes RCCR when GCR[FME] = 1. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/055_Clock_Monitoring_Unit_-_Frequency_Meter_-CMU_FM-/S32K3XXRM_数据表.pdf-1864-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>REF_CNT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-16|Reserved|
|—||
|15-0|Reference Clock Count|
|REF_CNT|Total number of counts of reference_clock for which frequency metering runs. This field defines the<br>duration of one frequency metering window. SeeProgramming RCCR[REF_CNT]for RCCR calculation.|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1864 / 4640 

NXP Semiconductors 

Clock Monitoring Unit – Frequency Meter (CMU_FM) 

### 55.5.4 Status Register (SR) 

#### Offset 

|Register|Offset|
|---|---|
|SR|8h|



#### Function 

Provides the internal status of the module and metered clock count. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/055_Clock_Monitoring_Unit_-_Frequency_Meter_-CMU_FM-/S32K3XXRM_数据表.pdf-1865-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R MET_CNT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R MET_CNT  0 RS  Reserved  FMTO  FMC<br>W W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-8|Meter Clock Count|
|MET_CNT|This field stores the count value of the metered clock cycles when frequency metering operation is<br>complete, in other words,SR[FMC]= 1. CMU_FM has a maximum deviation of ± 3 metered_clock cycles<br>over the ideal metered_clock cycles expected by the user.|
|7-5<br>—<br>4<br>RS|Reserved<br>Run Status<br>Shows the running status of module internal operation. After enabling the frequency metering operation<br>(GCR[FME]= 1), there is a fixed delay before this field shows running status. If the system wants<br>to disable the frequency metering operation, then the software should read this register and write<br>GCR[FME]= 0 only when this field is 1.<br>0b - Frequency meter stopped<br>1b - Frequency meter running|
|3-2<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1865 / 4640 

NXP Semiconductors 

Clock Monitoring Unit – Frequency Meter (CMU_FM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|1|Frequency Meter Time Out|
|FMTO|Sets if there is a loss of metered clock during the metering operation. After metering window, the module<br>waits for a timeout duration ofRCCR[REF_CNT]cycles before writing one to this field.GCR[FME]= 0<br>andSR[FMC]= 0 when FMTO = 1. Writing one clears this field.|
|0|Frequency Meter Operation Complete|
|FMC|On completion of frequency metering operation, FMC = 1,SR[MET_CNT]field updates, andGCR[FME]<br>clears. Writing one clears this field.|



### 55.5.5 Interrupt Enable Register (IER) 

#### Offset 

|Register|Offset|
|---|---|
|IER|Ch|



#### Function 

Enables CMU_FM interrupts. 

~~<mark>NOTE</mark>~~ 

Write IER only when GCR[FME] = 0. A bus transfer error results if software writes IER when GCR[FME] = 1. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/055_Clock_Monitoring_Unit_-_Frequency_Meter_-CMU_FM-/S32K3XXRM_数据表.pdf-1866-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>FMCIE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-1<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1866 / 4640 

NXP Semiconductors 

Clock Monitoring Unit – Frequency Meter (CMU_FM) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|0|Frequency Meter Complete Interrupt Enable|
|FMCIE|This bit is used to enable/disable Frequency Meter complete interrupt at the module boundary.|
||0b - Frequency Meter complete interrupt is disabled|
||1b - Frequency Meter complete interrupt is enabled|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1867 / 4640 

