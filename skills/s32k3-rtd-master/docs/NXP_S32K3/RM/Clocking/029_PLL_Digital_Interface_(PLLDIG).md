NXP Semiconductors 

# Chapter 29 PLL Digital Interface (PLLDIG) 

## 29.1 Chip-specific PLLDIG information 

### 29.1.1 PLL-supported accesses and frequencies 

The PLLODIV_0 and PLLODIV_1 registers support only word accesses. When you write to these registers, you must retain the default values of the reserved fields. 

PLLDIG supports a down-spread modulation of up to 160 MHz PLL PHI clock output only. 

## 29.2 Introduction 

PLL can multiply or divide the frequency of a given clock input. 

### 29.2.1 Features 

PLL includes the following features: 

- Programmable frequency modulation 

- Multiple integer dividers on PLL outputs 

- Lock detection circuitry reports when PLL achieves frequency lock 

- Continuous monitoring of lock status to report Loss of Lock (LOL) condition 

- Powering down the module for low-power operation (Power-Down mode) 

### 29.2.2 Block diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/029_PLL_Digital_Interface_-PLLDIG-/S32K3XXRM_数据表.pdf-0937-16.png)


<!-- Start of picture text -->
Loss of lock<br>lol<br>Detector<br>Lock<br>lock<br>Detector<br>PLLODIV_0[DIV]<br>divider PLL_PHI0<br>PLLDV[RDIV] 0<br>Reference PFD+CPUMP<br>Reference clock VCO divider<br>divider +FILTER vcoclkout<br>PLLODIV_1[DIV]<br>PLLDV[ODIV2]<br>divider PLL_PHI1<br>Feedback Divider<br>+ Sigma Delta<br>Modulator<br>PLLDV[MF]<br>PLLFD[MFN]<br>Register interface PLLFM[STEPNO] divider PLL_PHIn<br>PLLFM[STEPSIZE]<br>PLLODIV_n[DIV]<br><!-- End of picture text -->

Figure 113. Block diagram 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

937 / 4640 

NXP Semiconductors 

PLL Digital Interface (PLLDIG) 

The number of output dividers can vary with the module instance. See the Clocking chapter to confirm the number of PLL output dividers. 

## 29.3 Modes of operation 

Table 151. Modes of operation 

|PLLCR[PLLPD]|PLLFD[SDMEN]|PLLFM[SSCGBYP]|Description|
|---|---|---|---|
|1|x|x|PLL is disabled.|
|0|0|1|Functional mode – PLL operates in integer-only mode.<br>SeeClock configuration.|
|0|1|1|Functional mode – PLL operates in Fractional mode<br>(non-Frequency modulation). SeeClock configuration.|
|0|1|0|Functional mode – PLL operates in Frequency<br>Modulation mode. SeeFrequency modulation.|



## 29.4 Functional description 

This section explains PLL operation and configuration. 

### 29.4.1 Input clock frequency 

PLL is designed to operate over a specified input clock frequency range. PLL source frequency limits are discussed in this chip's data sheet. 

### 29.4.2 Clock configuration 

See the equations below and the corresponding register configuration that determine the relationship between VCO frequency (fVCO) and PLL reference frequency. 

- Integer-only mode: 

   - When PLLDV[RDIV] is 0: 

Equation 1. PLL VCO frequency in integer-only mode when PLLDV[RDIV] is 0 

- When PLLDV[RDIV] is not 0: 

Equation 2. PLL VCO frequency in integer-only mode when PLLDV[RDIV] is not 0 

- Fractional mode: 

   - When PLLDV[RDIV] is 0: 

Equation 3. PLL VCO frequency in Fractional mode when PLLDV[RDIV] is 0 

- When PLLDV[RDIV] is not 0: 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

938 / 4640 

NXP Semiconductors 

PLL Digital Interface (PLLDIG) 

##### Equation 4. PLL VCO frequency in Fractional mode when PLLDV[RDIV] is not 0 

See the equation below and the corresponding register configuration that determine the relationship between reference and PLL_PHIn output frequencies. 

Equation 5. PLL PHI output frequency 

When configuring PLL, you must not violate the maximum system clock frequency or maximum and minimum VCO frequency specification of PLL (see this chip's data sheet for frequency limits). 

You must disable PLL by writing 1 to PLLCR[PLLPD] before any PLL configuration or input clock are modified. 

You must disable PLL by writing 1 to PLLCR[PLLPD] for at least 5 μs before writing 0 to PLLCR[PLLPD] to enable PLL. 

The recommended procedure to program PLL and enter Normal mode is shown in Initialization information. 

### 29.4.3 Loss of lock (LOL) 

PLL provides LOL indication. The LOL indication can only be generated when PLL is in Functional mode (see Modes of operation). When PLL detects a LOL, it asserts its LOL event output. 

PLL does not detect loss of reference clock. If the reference clock stops after PLL achieves lock, PLL continues to indicate lock. It is assumed that monitoring of PLL's reference clock that is done outside PLL is enabled while PLL is in operation. 

PLL LOL is intended for detection of gross failures. Use CMUs for accurate frequency monitoring. 

### 29.4.4 Frequency modulation 

In Frequency Modulation mode, PLL generates a frequency-modulated clock. The modulation depth and modulation frequency are calculated using the equations shown in Frequency modulation programming. 

Write 1 to PLLFM[SPREADCTL] to select down-spread modulation. See Figure 114 that shows an example of downspread modulation. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/029_PLL_Digital_Interface_-PLLDIG-/S32K3XXRM_数据表.pdf-0939-16.png)


<!-- Start of picture text -->
Modulation frequency ( f MOD)<br>nominal VCO frequency ( f pll_VCO)<br>Modulation Depth (MD)<br>Down spread<br><!-- End of picture text -->

Figure 114. Frequency modulation 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

939 / 4640 

NXP Semiconductors 

PLL Digital Interface (PLLDIG) 

#### 29.4.4.1 Frequency modulation programming 

Modulation depth and modulation frequency programming uses step number (PLLFM[STEPNO]) and step size (PLLFM[STEPSIZE]). The table below shows variables used during calculations when programming PLL for frequency modulation. 

Table 152. Variables for configuring modulation depth and frequency 

|Variable|Description|
|---|---|
|fREF|Input clock frequency|
|fMOD|Expected modulation frequency|
|MD|Expected modulation depth in percentage|
|LDF|Loop division factor|
|fpll_VCO|Nominal VCO frequency|



Use the following equations to configure PLL for frequency modulation. 

Equation 6. LDF 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/029_PLL_Digital_Interface_-PLLDIG-/S32K3XXRM_数据表.pdf-0940-08.png)


Equation 7. Step number 

Equation 8. Step size 

Frequency modulation is only possible if the condition shown in Equation 9 is met. 

Equation 9. Requirement to achieve FM 

You must write 0 to PLLFM[SSCGBYP] and write 1 to PLLFD[SDMEN] to enable frequency modulation. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/029_PLL_Digital_Interface_-PLLDIG-/S32K3XXRM_数据表.pdf-0940-14.png)


Equation 10. Maximum possible modulation depth when PLL[RDIV] is 0 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/029_PLL_Digital_Interface_-PLLDIG-/S32K3XXRM_数据表.pdf-0940-16.png)


Equation 11. Maximum possible modulation depth when PLL[RDIV] is not 0 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

940 / 4640 

NXP Semiconductors 

PLL Digital Interface (PLLDIG) 

~~<mark>CAUTION</mark>~~ 

The effective modulation depth may differ from the intended modulation depth because of rounding operations applied to PLLFM[STEPSIZE] and PLLFM[STEPNO]. 

## 29.5 Initialization information 

Perform the following steps to initialize PLL: 

1. Confirm that PLLODIV_n[DE] is 0 for all dividers. 

2. Confirm that PLLCR[PLLPD] is 1. 

3. Program the following as needed: 

   - PLLDV 

   - PLLFD 

   - PLLFM to the desired value 

4. Program PLLDV[ODIV2] and PLLODIV_n[DIV] to the desired values. 

5. Wait for the PLL reference clock to be stable. 

6. Write 0 to PLLCR[PLLPD]. 

7. Wait for PLLSR[LOCK] to be 1. 

8. Write 1 to PLLODIV_n[DE]. 

Perform the following steps to shut down PLL: 

1. Write 0 to PLLODIV_n[DE] for all dividers. 

2. Write 1 to PLLCR[PLLPD]. 

## 29.6 PLLDIG register descriptions 

This section provides the memory map and detailed descriptions of registers used for configuring PLL. The table below shows the memory map. Addresses are given as offsets from the module base address. All registers are accessed using 8-bit, 16-bit, or 32-bit addressing. 

### 29.6.1 PLLDIG memory map 

PLL base address: 402E_0000h 

PLL_AUX base address: 402E_4000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|PLL Control (PLLCR)|32|RW|8000_0000h|
|4h|PLL Status (PLLSR)|32|W1C|0000_0300h|
|8h|PLL Divider (PLLDV)|32|RW|0C3F_1032h|
|Ch|PLL Frequency Modulation (PLLFM)|32|RW|4000_0000h|
|10h|PLL Fractional Divider (PLLFD)|32|RW|0000_0000h|
|18h|PLL Calibration Register 2 (PLLCAL2)|32|RW|0006_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

941 / 4640 

NXP Semiconductors 

PLL Digital Interface (PLLDIG) 

Table continued from the previous page... 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|80h - 84h|PLL Output Divider (PLLODIV_0 - PLLODIV_1)|32|RW|0000_0000h|
|88h|PLL Output Divider (PLLODIV_2)|32|RW|0000_0000h|



### 29.6.2 PLL Control (PLLCR) 

##### Offset 

|Register|Offset|
|---|---|
|PLLCR|0h|



##### Function 

Configures PLL functionality. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/029_PLL_Digital_Interface_-PLLDIG-/S32K3XXRM_数据表.pdf-0942-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>PLLPD<br>W<br>Reset 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|PLL Power Down|
|PLLPD|Powers down or powers up PLL.|
||0b - Powered up|
||1b - Powered down|
|30-0<br>—|Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

942 / 4640 

NXP Semiconductors 

PLL Digital Interface (PLLDIG) 

### 29.6.3 PLL Status (PLLSR) 

##### Offset 

|Register|Offset|
|---|---|
|PLLSR|4h|



##### Function 

##### Shows the PLL status. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/029_PLL_Digital_Interface_-PLLDIG-/S32K3XXRM_数据表.pdf-0943-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 Reserved  0 LOL  LOCK  0<br>W W1C<br>Reset 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-11<br>—|Reserved|
|10-8<br>—|Reserved|
|7-4<br>—|Reserved|
|3<br>LOL|Loss-Of-Lock Flag<br>Indicates the current PLL lock status.<br>0b - No loss of lock detected<br>1b - Loss of lock detected|
|2|Lock Status|
|LOCK|Indicates that PLL has acquired lock.|
||0b - Unlocked|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

943 / 4640 

NXP Semiconductors 

PLL Digital Interface (PLLDIG) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - Locked|
|1-0<br>—|Reserved|



### 29.6.4 PLL Divider (PLLDV) 

##### Offset 

|Register|Offset|
|---|---|
|PLLDV|8h|



##### Function 

Divides input clocks for PLL output generation. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/029_PLL_Digital_Interface_-PLLDIG-/S32K3XXRM_数据表.pdf-0944-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0<br>ODIV2  Reserved<br>W<br>Reset 0 0 0 0 1 1 0 0 0 0 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>RDIV  MFI<br>W<br>Reset 0 0 0 1 0 0 0 0 0 0 1 1 0 0 1 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31<br>—|Reserved|
|30-25|Output frequency divider for raw PLL clock.|
|ODIV2|6-bit field determining the VCO clock post divider for driving the PHI output clock.|
||000000 – Divide by 1|
||000001 – Divide by 1|
||000010 – Divide by 2|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

944 / 4640 

NXP Semiconductors 

PLL Digital Interface (PLLDIG) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||000011 – Divide by 3<br>000100 – Divide by 4<br>.......<br>111111 – Divide by 63|
|24-22<br>—|Reserved|
|21-16<br>—|Reserved|
|15|Reserved|
|—||
|14-12|Input Clock Predivider|
|RDIV|Sets the input clock divider.<br>The output of the predivider circuit generates the PLL loop reference clock.<br>000b - Divide by 1<br>001b - Divide by 1|
||010b - Divide by 2<br>011b - Divide by 3|
||100b - Divide by 4<br>101b - Divide by 5<br>110b - Divide by 6|
||111b - Divide by 7|
|11-8|Reserved|
|—||
|7-0|Integer Portion Of Loop Divider|
|MFI|Sets the value of the divider in the PLL feedback loop.<br>The value specified establishes the multiplication factor applied to the reference frequency. Write the divider<br>value to this field, where the chosen value does not violate VCO frequency specifications.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

945 / 4640 

NXP Semiconductors 

PLL Digital Interface (PLLDIG) 

### 29.6.5 PLL Frequency Modulation (PLLFM) 

##### Offset 

|Register|Offset|
|---|---|
|PLLFM|Ch|



##### Function 

Configures PLL frequency modulation parameters. 

~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

|||Instan|ce||||Regis|ter sup|ported|||Re|gister n|ot supp|orted||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|PLL|||||PL|LFM|||||—||||||
|PLL_AUX|||||—||||||PLLF|M|||||
|Diagram<br>Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|R|0|SSCG|SPRE||0||||||STEP|IZE|||||
|W||BYP|ADC...||||||||||||||
|Reset|0|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||0||||||||STEPNO||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Diagram 

##### Fields 

|Field|Function|
|---|---|
|31|Reserved|
|—||
|30|Frequency Modulation (Spread Spectrum Clock Generation) Bypass|
|SSCGBYP|Bypasses frequency modulation.|
||0b - Not bypassed|
||1b - Bypassed|
|29|Modulation Type Selection|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

946 / 4640 

NXP Semiconductors 

PLL Digital Interface (PLLDIG) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|SPREADCTL|Indicates that the modulation is spread below the nominal frequency. You must write 1 to this field.<br>0b - Reserved<br>1b - Spread below nominal frequency|
|28-26<br>—|Reserved|
|25-16|Frequency Modulation Step Size|
|STEPSIZE|Provides the step size for modulation depth and frequency in Frequency Modulation mode (see<br>Frequency modulation).|
|15-11<br>—|Reserved|
|10-0|Number Of Steps Of Modulation Period Or Frequency Modulation|
|STEPNO|Provides the number of steps to achieve modulation depth in Frequency Modulation mode (see<br>Frequency modulation).|



### 29.6.6 PLL Fractional Divider (PLLFD) 

##### Offset 

|Register|Offset|
|---|---|
|PLLFD|10h|



##### Function 

Enables and configures frequency modulation. 

~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

||Instance|Register supported||Register not supported|
|---|---|---|---|---|
|PLL||PLLFD|—||
|PLL_AUX||—|PLLFD||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

947 / 4640 

NXP Semiconductors 

PLL Digital Interface (PLLDIG) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/029_PLL_Digital_Interface_-PLLDIG-/S32K3XXRM_数据表.pdf-0948-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 SDME 0 0 Reserv<br>SDM2  SDM3  Reserved<br>W N  ed<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>MFN<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31<br>—|Reserved|
|30|Fractional Mode Enable|
|SDMEN|Enables Fractional mode.<br>0b - Disabled<br>1b - Enabled|
|29<br>SDM2|Fractional Mode Configuration<br>When you are in the fractional mode (SDMEN = 1), write 1 to this field.<br>If SDMEN = 1, this field must be wrtiten 1.<br>~~NOTE~~|
|28<br>SDM3|Fractional Mode Configuration<br>When you are in the fractional mode (SDMEN = 1), write 1 to this field.<br>If SDMEN = 1, this field must be wrtiten 1.<br>~~NOTE~~|
|27-22<br>|Reserved|
|—<br>21-18<br>—|Reserved|
|17<br>—|Reserved|
|16|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

948 / 4640 

NXP Semiconductors 

PLL Digital Interface (PLLDIG) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|15|Reserved|
|—||
|14-0|Numerator Of Fractional Loop Division Factor|
|MFN|Sets the numerator of the fractional loop division factor.|
||You must write a value of less than 18432 to this field. When Fractional mode is disabled, you must write<br>000_0000_0000_0000b to this field.|



### 29.6.7 PLL Calibration Register 2 (PLLCAL2) 

##### Offset 

|Register|Offset|
|---|---|
|PLLCAL2|18h|



~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

||Instance|Register supported||Register not supported|
|---|---|---|---|---|
|PLL||PLLCAL2|—||
|PLL_AUX||—|PLLCAL2||



##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/029_PLL_Digital_Interface_-PLLDIG-/S32K3XXRM_数据表.pdf-0949-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>Reserved  Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>Reserved  ULKCTL  Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

949 / 4640 

NXP Semiconductors 

PLL Digital Interface (PLLDIG) 

##### Fields 

|Field|Function|
|---|---|
|31-22<br>—<br>21-19<br>—<br>18-16<br>—<br>15-9<br>—|Reserved<br>Reserved<br>Reserved<br>Reserved|
|8-7<br>ULKCTL|Unlock Control Accuracy<br>Defines the accuracy necessary to achieve unlock.<br>The lock counter determines unlock if the number of VCO clock cycles in the window of reference cycles is<br>outside the number of cycles defined by this field.<br>00b - Unlock range = Expected value ± 9 (recommended when PLLFM[SSCGBYP] = 1). Unlock<br>range = Expected value ± 9 (recommended whenPLLFM[SSCGBYP]= 1)<br>01b - Unlock range = Expected value ± 17 (recommended when PLLFM[SSCGBYP] = 0). Unlock<br>range = Expected value ± 17 (recommended whenPLLFM[SSCGBYP]= 0)<br>10b - Unlock range = Expected value ± 33<br>11b - Unlock range = Expected value ± 5|
|6-0<br>—|Reserved|



### 29.6.8 PLL Output Divider (PLLODIV_0 - PLLODIV_1) 

##### Offset 

|Register|Offset|
|---|---|
|PLLODIV_0|80h|
|PLLODIV_1|84h|



##### Function 

Controls the PLL output clock divider settings. 

This divider has a 50% duty cycle. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

950 / 4640 

NXP Semiconductors 

PLL Digital Interface (PLLDIG) 

~~<mark>NOTE</mark>~~ 

These registers support only word accesses. Other write accesses lead to the following: 

- Unpredictable behavior 

- No transfer error generated 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|DE||||0|||||||DI|V|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R<br>W||||||||0|||||||Reserved|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



##### Fields 

|Field|Function|
|---|---|
|31|Divider Enable|
|DE|Enables PLL output divider. Divider must be disabled before disabling PLL.<br>0b - Disabled<br>1b - Enabled|
|30-24<br>—|Reserved|
|23-16|Division Value|
|DIV|Provides the division value for the output clock divider. The clock period of the clock after division is<br>DIV + 1 times the time period of the divider input clock.<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>~~NOTE~~|
||Instance<br>Field supported in<br>Field not supported in|
||PLL<br>PLLODIV_0–PLLODIV_1<br>—|
||PLL_AUX<br>PLLODIV_0–PLLODIV_1[20–16]<br>PLLODIV_0–PLLODIV_1[23–21]|
|15-2|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

951 / 4640 

NXP Semiconductors 

PLL Digital Interface (PLLDIG) 

##### Table continued from the previous page... 

|Field<br>—|Function|
|---|---|
|1-0|Reserved|
|—|Do not write any value other than the reset value.|



### 29.6.9 PLL Output Divider (PLLODIV_2) 

##### Offset 

|Register|Offset|
|---|---|
|PLLODIV_2|88h|



##### Function 

Controls the PLL output clock divider settings. 

This divider has a 50% duty cycle. 

~~<mark>NOTE</mark>~~ 

These registers support only word accesses. Other write accesses lead to the following: 

- Unpredictable behavior 

- No transfer error generated 

~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/029_PLL_Digital_Interface_-PLLDIG-/S32K3XXRM_数据表.pdf-0952-16.png)


<!-- Start of picture text -->
Instance Register supported Register not supported<br>PLL — PLLODIV_2<br>PLL_AUX PLLODIV_2 —<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>DE  DIV<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

952 / 4640 

NXP Semiconductors 

PLL Digital Interface (PLLDIG) 

##### Fields 

|Field|Function|
|---|---|
|31|Divider Enable|
|DE|Enables PLL output divider. Divider must be disabled before disabling PLL.<br>0b - Disabled<br>1b - Enabled|
|30-21<br>—|Reserved|
|20-16<br>DIV|Division Value<br>Provides the division value for the output clock divider. The clock period of the clock after division is<br>DIV + 1 times the time period of the divider input clock.|
|15-2<br>—|Reserved|
|1-0|Reserved|
|—|Do not write any value other than the reset value.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

953 / 4640 

