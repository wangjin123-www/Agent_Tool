NXP Semiconductors 

# Chapter 28 Slow Crystal Oscillator Digital Controller (SXOSC) 

## 28.1 Introduction 

SXOSC: 

- Controls the functioning of the analog oscillator 

- Provides a register interface for programmable features 

- Controls the power-down function of the oscillator 

## 28.2 Features 

- Generates a 32 KHz clock output in Functional Oscillator mode 

- Contains a status register, the value of which becomes 1 when the crystal stabilization time is complete 

- Contains an oscillator that can be powered down 

## 28.3 Modes of operation 

- Functional Oscillator—In this mode, the external crystal generates the clock. 

## 28.4 Functional description 

SXOSC generates control signals to configure the analog module to operate in specific modes. 

The following table shows the mode of operation available for selection and its settings. 

Table 150. Operation mode settings 

|Mode|Value ofSXOSC_CTRL[OSCON]|Output clock|
|---|---|---|
|Functional Oscillator|0 (oscillator switched off)|0 (indicates no output)|
||1 (oscillator switched on)|Crystal clock|



### 28.4.1 Clock generation in Functional Oscillator mode 

After hard reset, the crystal oscillator is switched off by default. For clock generation in Functional Oscillator mode, see Table 150. The counter logic starts counting and the stable clock starts running one clock cycle after reaching the value of SXOSC_CTRL[EOCV] x 128 counter value. The module writes 1 to SXOSC_STAT[OSC_STAT] after two module clock cycles. 

### 28.4.2 Clock stopping in Functional Oscillator mode 

To stop a stable, running clock, configure the mode as specified in Table 150. A glitch does not occur because synchronizers are used. 

## 28.5 Initialization information 

Perform the following steps to initialize SXOSC: 

1. Write an appropriate value to SXOSC_CTRL[EOCV]. 

2. Write 1 to SXOSC_CTRL[OSCON]. This enables the oscillator. The value of this field defaults to 0, which means the oscillator is off by default. 

3. Confirm the clock is stable (SXOSC_STAT[OSC_STAT] = 1) before using it. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

933 / 4640 

NXP Semiconductors 

Slow Crystal Oscillator Digital Controller (SXOSC) 

Be aware that: 

- A functional reset does not affect any mode settings. 

- Functional Oscillator is the only available mode of operation. 

- To calculate EOCV of the crystal from start-up time, use the following formula: 

EOCV = (stabilisation time in ns) ÷ (4 × 128 × time period of clock in ns). 

## 28.6 SXOSC register descriptions 

This section provides the description of registers that are used for configuring SXOSC. 

### 28.6.1 SXOSC memory map 

Addresses are provided as offsets from the module base address. You can access all the registers using 8-bit, 16-bit, or 32-bit addressing. Using external configuration signals or parameters, you can configure some of the register reset values according to the requirements of individual chips. 

SXOSC base address: 402C_C000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|Oscillator Control (SXOSC_CTRL)|32|RW|007D_0000h|
|4h|Oscillator Status (SXOSC_STAT)|32|RO|0000_0000h|



### 28.6.2 Oscillator Control (SXOSC_CTRL) 

#### Offset 

|Register|Offset|
|---|---|
|SXOSC_CTRL|0h|



#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||0|||Rese|rved|Rese|rved||||EO|CV||||
|Reset|0|0|0|0|0|0|0|0|0|1|1|1|1|1|0|1|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||||0||||Reser|ved|||0|||OSCO<br>N|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

934 / 4640 

NXP Semiconductors 

Slow Crystal Oscillator Digital Controller (SXOSC) 

#### Fields 

|Field|Function|
|---|---|
|31-28<br>—|Reserved|
|27-26<br>—|Reserved|
|25-24<br>—|Reserved|
|23-16<br>EOCV|End Of Count Value<br>Specifies the end of count value, which the oscillator stabilization counter uses for comparison whenever<br>the oscillator is switched on. This counting period ensures that SXOSC's clock signal is stable before the<br>system selects it. The oscillator counter runs on a divided crystal clock (divide by 4) and counts up to 128<br>times the EOCV value (EOCV × 128).|
||To calculate an appropriate EOCV value, the internal counter must run for at least the<br>stabilization time specified for the crystal in the data sheet. Also, it is recommended to<br>change the value of EOCV only when SXOSC is in the disabled state.<br>~~NOTE~~|
|15-8<br>—<br>7-6<br>|Reserved<br>Reserved|
|—<br>5-1|Reserved|
|—<br>0<br>OSCON|Crystal Oscillator Power-Down Control<br>Indicates the status of the crystal oscillator.<br>When disabling SXOSC, write 0 to this field and do not change other values in this register for at least 16<br>SXOSC clock cycles.<br>0b - Disabled (switched off)<br>1b - Enabled (switched on)|



### 28.6.3 Oscillator Status (SXOSC_STAT) 

#### Offset 

|Register|Offset|
|---|---|
|SXOSC_STAT|4h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

935 / 4640 

NXP Semiconductors 

Slow Crystal Oscillator Digital Controller (SXOSC) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/028_Slow_Crystal_Oscillator_Digital_Controller_-SXOSC-/S32K3XXRM_数据表.pdf-0936-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>OSC_<br>R 0<br>STAT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31|Crystal Oscillator Status|
|OSC_STAT|Indicates the output clock status of the crystal oscillator.|
||0b - Unstable|
||1b - Stable|
|30-0<br>—|Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

936 / 4640 

