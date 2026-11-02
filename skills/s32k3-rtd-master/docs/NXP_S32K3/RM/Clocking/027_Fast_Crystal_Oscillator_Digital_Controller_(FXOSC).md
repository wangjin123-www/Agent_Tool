NXP Semiconductors 

# Chapter 27 Fast Crystal Oscillator Digital Controller (FXOSC) 

## 27.1 Chip-specific FXOSC information 

### 27.1.1 Chip-specific FXOSC information 

For S32K3x4: For bypass mode applications, the EXTAL pin should be driven low when FXOSC is in off/disabled state. 

- While initializing FXOSC: When the FXOSC is used in Bypass mode, the external clock source can only be enabled after the FXOSC is enabled. 

- While disabling FXOSC: When the FXOSC is used in Bypass mode, the external clock source must already be inactive before disabling the FXOSC. 

## 27.2 Introduction 

### 27.2.1 Overview 

This module provides the fast crystal oscillator to the chip. 

### 27.2.2 Features 

FXOSC features are as follows: 

- Status register shows current module state. 

- Control register can: 

   - Select a mode of operation: 

◦Crystal mode 

◦Single-Input Bypass mode using EXTAL clock input 

- Disable the module (Power-Down mode) 

## 27.3 Functional description 

The table below shows configuration settings for the different FXOSC modes set by the CTRL register: 

Table 149. FXOSC operation mode settings 

|Mode|CTRL[OSCON]|CTRL[OSC_BYP]|CTRL[COMP_EN]|FXOSC_CLK|
|---|---|---|---|---|
|Power-Down mode|0|X|X|0|
|Crystal mode|1|0|1|Crystal clock|
|Single-Input Bypass<br>mode|1|1|0|EXTAL|



Power-Down mode is the FXOSC default condition after any reset: POR, Destructive, or Functional. 

### 27.3.1 Clock generation in Crystal mode 

Counter logic and FXOSC_CLK start when counter value reaches EOCV × 128. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

927 / 4640 

NXP Semiconductors 

Fast Crystal Oscillator Digital Controller (FXOSC) 

### 27.3.2 Clock generation in Single-Input Bypass mode 

This mode bypasses the oscillator and uses a single-input external clock (EXTAL input) for FXOSC_CLK. 

## 27.4 Initialization information 

#### Initializing FXOSC 

Initialize FXOSC as follows: 

1. Write the desired value to CTRL[OSC_BYP] and CTRL[COMP_EN] to select an operation mode as shown in Table 149. 

   - ~~<mark>NOTE</mark>~~ 

FXOSC must be disabled when the operation mode is modified. 

2. Configure CTRL[GM_SEL]. 

   - In Crystal mode configure the transconductance based on the module specification in the chip data sheet. 

   - In Single-Input Bypass mode write 0000b to this field. 

      - ~~<mark>NOTE</mark>~~ 

In Crystal mode FXOSC will not function with zero transconductance (GM_SEL = 0000b). 

3. Set CRTL[EOCV] calculating the value as follows: 

   - EOCV (in decimal) = (stabilization time in ns) ÷ (4×128×(period of clock in ns)) 

4. Write 1 to CRTL[OSCON] to enable FXOSC. 

5. Confirm the clock is stable (STAT[OSC_STAT] = 1) before using it. 

#### Disabling FXOSC 

Write 0 to CRTL[OSCON] to disable FXOSC when FXOSC_CLK is running and stable. 

FXOSC enters Power-down mode after at least four crystal clocks. No glitches occur during the transition to Power-Down mode because synchronizers are used. 

~~<mark>NOTE</mark>~~ 

After disabling FXOSC: 

- Wait for at least 2μs before enabling FXOSC again. 

- You must not change other values in FXOSC registers for at least 16 FXOSC_CLK cycles. 

## 27.5 FXOSC register descriptions 

This section provides the descriptions of all registers used for configuring the FXOSC. 

### 27.5.1 FXOSC memory map 

Use 8-bit, 16-bit, or 32-bit addressing to access registers. 

FXOSC base address: 402D_4000h 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

928 / 4640 

NXP Semiconductors 

Fast Crystal Oscillator Digital Controller (FXOSC) 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|FXOSC Control Register (CTRL)|32|RW|019D_00C0h|
|4h|Oscillator Status Register (STAT)|32|RO|0000_0000h|



### 27.5.2 FXOSC Control Register (CTRL) 

#### Offset 

|Register|Offset|
|---|---|
|CTRL|0h|



#### Function 

#### Configures FXOSC operation. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/027_Fast_Crystal_Oscillator_Digital_Controller_-FXOSC-/S32K3XXRM_数据表.pdf-0929-09.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>OSC_ Reserv COMP<br>Reserved  EOCV<br>W BYP  ed  _EN<br>Reset 0 0 0 0 0 0 0 1 1 0 0 1 1 1 0 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>Reserv OSCO<br>GM_SEL  ALC_D<br>W ed  N<br>Reset 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31|Oscillator bypass|
|OSC_BYP|Bypasses the internal oscillator.|
||0b - Internal oscillator not bypassed<br>1b - Internal oscillator bypassed|
|30<br>—|Reserved|
|29-26<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

929 / 4640 

NXP Semiconductors 

Fast Crystal Oscillator Digital Controller (FXOSC) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|25<br>—|Reserved|
|24<br>COMP_EN|Comparator enable<br>Enables or disables the comparator.<br>• For Crystal mode set this field to 1.<br>• For Single-Input Bypass mode set this field to 0.<br>0b - Comparator disabled<br>1b - Comparator enabled|
|23-16<br>EOCV|End of count value<br>Specifies the end-of-count.<br>The oscillator counter runs on the crystal clock divided by 4 and counts up to EOCV ✕ 128. This counting<br>period ensures that the external oscillator clock signal is stable before the system selects FXOSC as<br>a source.|
||• You must set EOCV to the appropriate value to allow clock and duty cycle to stabilize<br>and guarantee that OSC_STAT becomes set within the crystal startup time.<br>— In Crystal mode, EOCV value must to be calculated to appropriate value based<br>on the crystal specification using the equation inInitializing FXOSC.<br>— In Single-Input Bypass mode, EOCV value is irrelevant. FXOSC holds the<br>counter in reset.<br>• Before modifying EOCV, FXOSC must be disabled.<br>~~NOTE~~|
|15-8<br>—<br>7-4<br>GM_SEL|Reserved<br>Crystal overdrive protection<br>Selects the transconductance applied by the FXOSC amplifier. This setting depends on<br>crystal specification.<br>• In Crystal mode FXOSC will not function with zero transconductance<br>(GM_SEL = 0000b).<br>• For details on how to set this field, seeInitializing FXOSC.<br>~~NOTE~~|
||0000b - 0x<br>0001b - 0.1004x<br>0010b - 0.2009x<br>0011b - 0.3013x|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

930 / 4640 

NXP Semiconductors 

Fast Crystal Oscillator Digital Controller (FXOSC) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||0100b - 0.2343x|
||0101b - 0.3348x<br>0110b - 0.4345x<br>0111b - 0.5349x<br>1000b - 0.4679x<br>1001b - 0.5684x|
||1010b - 0.6681x|
||1011b - 0.7678x<br>1100b - 0.7016x<br>1101b - 0.8013x<br>1110b - 0.9003x<br>1111b - 1x|
|3<br>—|Reserved|
|2|Automatic level controller enable|
|ALC_D|0b - Enables automatic level controller<br>1b - Disables automatic level controller|
|1<br>—|Reserved|
|0|Crystal oscillator power-down control|
|OSCON|Enables or disables FXOSC|
||0b - Disables FXOSC<br>1b - Enables FXOSC|



### 27.5.3 Oscillator Status Register (STAT) 

#### Offset 

|Register|Offset|
|---|---|
|STAT|4h|



Function 

Shows current state of FXOSC. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

931 / 4640 

NXP Semiconductors 

Fast Crystal Oscillator Digital Controller (FXOSC) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/027_Fast_Crystal_Oscillator_Digital_Controller_-FXOSC-/S32K3XXRM_数据表.pdf-0932-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>OSC_<br>R 0<br>STAT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31|Crystal oscillator status|
|OSC_STAT|Indicates the crystal oscillator status.|
||OSC_STAT value is is not valid if transconductance is set to 0.<br>~~NOTE~~|
||0b - Crystal oscillator is off or on but not stable.|
||1b - Crystal oscillator is on and providing a stable clock.|
|30-0<br>—|Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

932 / 4640 

