NXP Semiconductors 

# Chapter 59 Low Power Comparator (LPCMP) 

## 59.1 Chip-specific LPCMP information 

### 59.1.1 Instantiation information 

Table 292. LPCMP instances 

|Chip|Instance|No. of external inputs|
|---|---|---|
|K358, K3x4|LPCMP_0|8|
||LPCMP_1|4|
||LPCMP_2|4|
|K312, K342|LPCMP_0|8|
||LPCMP_1|4|
|K311|LPCMP_0|8|



### 59.1.2 LPCMP input output connections 

See the IOMUX file attached to this document for pin/pad assignments corresponding to CMP pins. 

The LPCMP channels can be used as a wakeup source in trigger mode to wakeup the device from standby mode. 

### 59.1.3 LPCMP-DAC "vrefh0" and "vrefh1" references 

The 8-bit DAC sub-block supports selection of "vrefh0" and "vrefh1" by CMPx_DCR[VRSEL]. For this device, the references are connected as follows: 

- vrefh0 (External Reference): VDD_HV_A 

- vrefh1 (Internal Reference): 1.2 V PMC bandgap reference 

~~<mark>NOTE</mark>~~ 

1.2 V internal reference voltage is not available in Standby mode. 

### 59.1.4 LPCMP window control 

The window mode operation of all the comparator instances in the chip can be enabled/disabled by the TRGMUX. See the TRGMUX connectivity file attached to this document for details. 

~~<mark>NOTE</mark>~~ 

Window signal must be of minimum 4 cycle pulse for window mode to function. 

### 59.1.5 Comparator Trigger Mode 

The comparator modules in the device support trigger mode operation as described in 'Trigger Mode' section. Device can operate in trigger mode in both standby and run mode to continuously scan the input channels. The main features of the device trigger mode operation are: 

- Round robin clock: RTC_CLK 

- Round robin trigger source: RTC_API 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2058 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

~~<mark>NOTE</mark>~~ 

It must be ensured that the RTC_CLK period is greater than the comparison time corresponding to the value of C0[PMODE]. It is also required to not select the internal reserved channels, if available on the package, for trigger mode operation by INPSEL and INNSEL. See the IOMUX file attached to this document for the pins available in various packages supported for the device. 

~~<mark>NOTE</mark>~~ 

Only SIRC and SXOSC are supported as RTC_CLK for trigger mode operation. The LPCMP initialization delay is not supported by RRCR0[RR_INITMOD] with FXOSC or FIRC as RTC_CLK. 

~~<mark>NOTE</mark>~~ 

In run mode, the generated trigger is delayed by 3 RTC_CLK cycles before being given to comparator trigger input. 

### 59.1.6 Interaction with RTC API to cause wakeup 

LPCMP can be used for waking up the chip from standby. For this, RTC-API and LPCMP must be configured before entering into standby mode as per below shown figure. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/059_Low_Power_Comparator_-LPCMP-/S32K3XXRM_数据表.pdf-2059-10.png)


<!-- Start of picture text -->
RTC-API CMP<br>Software<br>Configure CMPx for round robin operation<br>Configure CMP_x.RRCR0[RR_EN] to put CMP_x<br>in trigger mode/round robin mode and configure<br>RTC.APIVAL  for trigger mode/round robin period<br>Enter into STANDBY mode<br>On time-out, RTC-API sends a<br>trigger to CMP_x to start round<br>robin operation periodically<br>Sample the configured inputs<br>and stores the results<br>Unequal Compares<br>the result with previous<br>result stored<br>Wakeup from STANDBY mode Equal<br>Device stays in STANDBY mode<br>and CMP_x waits for next trigger.<br><!-- End of picture text -->

Figure 235. LPCMP-RTC interaction 

In the trigger mode operation, only the continuous mode is supported. None of the window/filter/sample functions should be used. Refer to the "Functional Modes" section for details on comparator modes of operation. 

Register configurations before entering Standby mode for LPCMP trigger mode operation: 

1. Configure RTC.APIVAL to set the period of the round robin operation. 

2. Execute standby mode entry. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2059 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

## 59.2 Overview 

The Low Power Comparator (LPCMP) module provides a circuit for comparing two analog input voltages. It comprises a comparator (CMP), a DAC and an analog mux (ANMUX). See Block diagram for details. 

CMP can operate across the full range of the supply voltage, known as rail-to-rail operation. 

DAC is a 256-tap resistor ladder network that provides a selectable voltage reference for applications requiring a voltage reference. The 256-tap resistor ladder network divides the supply reference Vin into 256 voltage levels. A 8-bit digital signal input selects the output voltage level, which varies from Vin to Vin/256. Vin can be selected from two voltage sources, vrefh0 and vrefh1. See the chip-specific LPCMP information for the source of vrefh0 and vrefh1. 

~~<mark>NOTE</mark>~~ 

The LPCMP's internal DAC output is available as an on-chip internal signal only and is not available for an external device pin. 

ANMUX allows software to select an analog input signal from among eight channel options. One channel option is the DAC output. Other device resources are connected to the other channels; see the chip-specific LPCMP information section for details. ANMUX can operate across the full range of the supply voltage. 

### 59.2.1 Block diagram 

The following figure shows the LPCMP block diagram includes the CMP, DAC, and ANMUX modules. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2060 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/059_Low_Power_Comparator_-LPCMP-/S32K3XXRM_数据表.pdf-2061-02.png)


<!-- Start of picture text -->
VRSEL<br>       vrefh0             vrefh1<br>DAC_DATA<br>0 MUX 1<br>Vin<br>DAC_EN<br>DAC output<br>DAC<br>PSEL[2:0]<br>RR_CH x N Round-<br>robin<br>FIXCH[2:0] Switch 1 0 RR_EN<br>INPSEL[1:0]<br>Reference Input 0<br>Reference InReference InReference Inputput 3put 2 1 011000010001 CMP<br>Reference InpReference InReference Input 4put 6ut 5 101100110 0100 INP SAMPLE/WINDOW input<br>Reference Input 7 111 DMA_REQ<br>ANMUX<br>000 CMP and Filter Window  IRQ<br>001 Control CMPO<br>010<br>011 INM<br>01<br>100<br>101 00<br>110<br>111<br>From 1 0 RR_EN<br>Round-robin<br>Switch MSEL[2:0] INMSEL[1:0]<br>MUX<br>Resistor Ladder<br>PMUX INPMUX<br>MMUX<br>INMMUX<br><!-- End of picture text -->

Figure 236. Block Diagram 

### 59.2.2 Features 

The features of the LPCMP module include: 

- Two 8-to-1 channel MUXes to select input signal from eight channels 

- Multiple operation modes to produce a wide range of outputs such as: 

   - Sampled 

   - Windowed, which is ideal for certain PWM zero-crossing-detection applications 

   - Digitally Filtered 

- Advanced feature for window and sample 

   - WINDOW/SAMPLE signal can be inverted 

   - Window can be closed by CMPO rising, falling or both edges 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2061 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

   - User can define CMPO level, when window is closed 

- Selectable performance levels: low power (speed) mode, high power (speed) mode 

- Programmable hysteresis control 

- Selectable inversion on comparator output 

- External hysteresis can be used at the same time that the output filter is used for internal functions 

- Interrupt and DMA support 

- Trigger mode 

- Includes a 8-bit resolution DAC 

- Selectable supply reference source for DAC 

## 59.3 Functional Description 

### 59.3.1 Functional Block Diagram 

The following figure shows the functional block diagram. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/059_Low_Power_Comparator_-LPCMP-/S32K3XXRM_数据表.pdf-2062-14.png)


<!-- Start of picture text -->
Internal Bus<br>To open PAD for CMPO<br>INP DMA_REQ<br>+<br>Interrupt<br>Polarity Window Filter<br>- COUT_RAW Select Control Block Control/DMA  IRQ<br>INM<br>COUT<br>To other SOC functions<br>WINDOW/SAMPLE<br>1<br>0 CMPO to PAD<br>Bus Clock Divided Bus Clock<br>Clock 0 COUTA<br>1<br>Prescaler<br>FILT_PER<br>SAMPLE_EN COUT_SEL<br>CMP_NPMD CMP_HPMD HYSTCTR CMP_EN COUT_INV WINDOW_EN FILT_CNT COUT CFR/F_IE DMA_EN CFR/F COUT_PEN<br>Sampling Clock<br><!-- End of picture text -->

Figure 237. Functional Block Diagram 

In the block diagram: 

- Two analog input voltages applied to INP and INM are compared. COUT_RAW is high when the INP input voltage is greater than the INM input, and is low when the INP input voltage is less than the INM input. 

- This COUT_RAW signal can be inverted if CCR1[COUT_INV] is enabled. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2062 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

- If CCR1[WINDOW_EN] is enabled, the optionally inverted comparator output COUT_RAW is sampled on every bus clock when window is enabled to generate COUTA. Sampling does NOT occur when window is disabled. This feature can be used to ignore the comparator output during time periods in which the input voltages are not valid. This is especially useful when implementing zero-crossing-detection for certain PWM applications. 

- The window control block can be bypassed if CCR1[WINDOW_EN] is disabled. 

- The filter block acts as a simple sampler if CCR1[FILT_CNT] is set to 0x01. 

- The filter block acts as a filter based on multiple samples when CCR1[FILT_CNT] is set greater than 0x01. 

   - If CCR1[SAMPLE_EN] = 1, the external SAMPLE input is used as the sampling clock. 

   - If CCR1[SAMPLE_EN] = 0, the divided bus clock is used as the sampling clock. 

- The filter block can be bypassed when not in use. 

```
Bypass_Filter_Block = (FILT_CNT == 0x00) |  (~SAMPLE_EN & (FILT_PER == 0x00))
```

- Both COUTA and COUT can be configured as module output CMPO by configuring the CCR1[COUT_SEL] bit and are used for different purposes within the system. 

- The optionally filtered COUT can be read directly through register bit CSR[COUT]. 

- The SAMPLE/WINDOW signal can be inverted by setting CCR1[WINDOW_INV]. 

- The SAMPLE/WINDOW signal can be closed by CMPO's falling edge or rising edge or both edge by setting CCR1[WINDOW_CLS] in window mode. 

- In the window mode, when window is closed, COUTA value can be defined as CCR1[COUTA_OW] by setting CCR1[COUTA_OWEN]. If CCR1[COUTA_OWEN] is not set, COUTA holds the last sampled value when window is closed 

~~<mark>NOTE</mark>~~ See the chip configuration section for the source of SAMPLE/WINDOW input. 

### 59.3.2 Functional Modes 

The comparator window and filter features can be combined as shown in the following table. Individual modes are discussed below the table. 

Table 293. Functional modes 

|Mode<br>#|CMP_EN|WINDOW_<br>EN|SAMPLE_<br>EN|FILT_CNT|FILT_PER|Operation|Maximum latency<sup>1</sup>|
|---|---|---|---|---|---|---|---|
|1|0|X|X|X|X|See theDisabled<br>Mode (#1).|N/A|
|2A|1|0|X|0x00|X|See theContinuous|TPD|
|2B|1|0|0|X|0x00|Mode (#2A & 2B).||
|3A|1|0|1|0x01|X|See theSampled, Non-|TPD+ TSAMPLE+ 3Tper|
|3B|1|0|0|0x01|> 0x00|Filtered Mode (#3A<br>& 3B).|TPD+ (FILT_PER * Tper)<br>+ 3Tper|
|4A|1|0|1|> 0x01|X||TPD+ (FILT_CNT *<br>TSAMPLE) + 3Tper|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2063 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

Table 293. Functional modes (continued) 

|Mode<br>#|CMP_EN|WINDOW_<br>EN|SAMPLE_<br>EN|FILT_CNT|FILT_PER|Operation|Maximum latency<sup>1</sup>|
|---|---|---|---|---|---|---|---|
|4B|1|0|0|> 0x01|> 0x00|See theSampled,<br>Filtered Mode (#4A<br>& 4B).|TPD+ (FILT_CNT *<br>FILT_PER x Tper) + 3Tper|
|5A|1|1|0|0x00|X|See theWindowed|TPD+ 2Tper|
|5B|1|1|0|X|0x00|Mode (#5A & 5B).||
|6|1|1|0|0x01|> 0x00|See theWindowed/<br>Resampled Mode (#6).|TPD+ (FILT_PER * Tper)<br>+ 3Tper|
|7|1|1|0|> 0x01|> 0x00|See theWindowed/<br>Filtered Mode (#7).|TPD+ (FILT_CNT *<br>FILT_PER x Tper) + 3Tper|



All other combinations of CMP_EN, WINDOW_EN, SAMPLE_EN, FILT_CNT, FILT_PER are illegal. 

1. TPD represents the intrinsic delay of the analog component plus the polarity select logic. TSAMPLE is the clock period of the external sample clock. Tper is the period of the bus clock. 

#### 59.3.2.1 Disabled Mode (#1) 

In disabled mode, the analog comparator is non-functional and consumes no power. CSR[COUT] and CMPO is same as CCR1[COUT_INV] in this mode. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2064 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

59.3.2.2 Continuous Mode (#2A & 2B) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/059_Low_Power_Comparator_-LPCMP-/S32K3XXRM_数据表.pdf-2065-03.png)


<!-- Start of picture text -->
Internal Bus<br>0 To open PAD for CMPO<br>INP DMA_REQ<br>+<br>Interrupt<br>Polarity Window Filter<br>- COUT_RAW Select Control Block Control/DMA  IRQ<br>INM<br>COUT<br>To other SOC functions<br>WINDOW/SAMPLE<br>1<br>0 CMPO to PAD<br>Bus Clock Divided Bus Clock<br>Clock 0 COUTA<br>1<br>Prescaler<br>FILT_PER<br>0<br>0x00 (#2B)<br>SAMPLE_EN COUT_SEL<br>CMP_NPMD CMP_HPMD HYSTCTR CMP_EN COUT_INV WINDOW_EN FILT_CNT COUT CFR/F_IE DMA_EN CFR/F COUT_PEN<br>(#2A)0x00<br>Sampling Clock<br><!-- End of picture text -->

Figure 238. Comparator Operation in Continuous Mode 

In this mode, COUT_RAW may be optionally inverted, but is not subject to external sampling or filtering. Both window control and filter blocks are completely bypassed. CSR[COUT] is updated continuously. The path from comparator input pins to output pin is operating in combinational(unclocked) mode. COUT and COUTA are identical. 

For cases where a comparator is used to drive a fault input, for example, for a motor-control module such as FTM, it should generally be configured to operate in continuous mode so that an external fault can immediately pass through the comparator to the target fault circuitry. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2065 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

#### 59.3.2.3 Sampled, Non-Filtered Mode (#3A & 3B) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/059_Low_Power_Comparator_-LPCMP-/S32K3XXRM_数据表.pdf-2066-03.png)


<!-- Start of picture text -->
Internal Bus<br>To open PAD for CMPO<br>0 0x01<br>INP DMA_REQ<br>+<br>Interrupt<br>Polarity Window Filter<br>- COUT_RAW Select Control Block Control/DMA  IRQ<br>INM<br>COUT<br>To other SOC functions<br>WINDOW/SAMPLE<br>1<br>0 CMPO to PAD<br>Bus Clock Divided Bus Clock<br>Clock 0 COUTA<br>1<br>Prescaler<br>FILT_PER<br>1<br>SAMPLE_EN COUT_SEL<br>CMP_NPMD CMP_HPMD HYSTCTR CMP_EN COUT_INV WINDOW_EN FILT_CNT COUT CFR/F_IE DMA_EN CFR/F COUT_PEN<br>Sampling Clock<br><!-- End of picture text -->

Figure 239. Sampled, Non-Filtered (#3A): Sampling Point Externally Driven 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2066 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/059_Low_Power_Comparator_-LPCMP-/S32K3XXRM_数据表.pdf-2067-02.png)


<!-- Start of picture text -->
Internal Bus<br>To open PAD for CMPO<br>0 0x01<br>INP DMA_REQ<br>+<br>Interrupt<br>Polarity Window Filter<br>- COUT_RAW Select Control Block Control/DMA  IRQ<br>INM<br>COUT<br>To other SOC functions<br>WINDOW/SAMPLE<br>1<br>0 CMPO to PAD<br>Bus Clock Divided Bus Clock<br>Clock 0 COUTA<br>1<br>Prescaler<br>FILT_PER<br>0<br>>0x00<br>SAMPLE_EN COUT_SEL<br>CMP_NPMD CMP_HPMD HYSTCTR CMP_EN COUT_INV WINDOW_EN FILT_CNT COUT CFR/F_IE DMA_EN CFR/F COUT_PEN<br>Sampling Clock<br><!-- End of picture text -->

Figure 240. Sampled, Non-Filtered (#3B): Sampling Interval Internally Derived 

In this mode, the path from analog inputs to COUTA is combinational(unclocked). Windowing control is completely bypassed. COUTA is sampled whenever a rising edge is detected on the sampling clock. 

The only difference in operation between sampled, non-filtered (#3A) and sampled, non-filtered (#3B) is in how the clock to the filter block is derived. In #3A, the clock to filter block is externally derived while in #3B, the clock to filter block is internally derived. 

The filter block has no other function than sample/hold of the comparator output in this mode. 

The following figure illustrates comparator operation in this mode, assuming that the polarity select is set to non-inverting state. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/059_Low_Power_Comparator_-LPCMP-/S32K3XXRM_数据表.pdf-2067-08.png)


<!-- Start of picture text -->
COUT_RAW<br>COUT<br>Sample Point<br>Figure 241. Sampled, Non-Filtered Mode Timing Diagram<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2067 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

#### 59.3.2.4 Sampled, Filtered Mode (#4A & 4B) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/059_Low_Power_Comparator_-LPCMP-/S32K3XXRM_数据表.pdf-2068-03.png)


<!-- Start of picture text -->
Internal Bus<br>To open PAD for CMPO<br>0 >0x01<br>INP DMA_REQ<br>+<br>Interrupt<br>Polarity Window Filter<br>- COUT_RAW Select Control Block Control/DMA  IRQ<br>INM<br>COUT<br>To other SOC functions<br>WINDOW/SAMPLE<br>1<br>0 CMPO to PAD<br>Bus Clock Divided Bus Clock<br>Clock 0 COUTA<br>1<br>Prescaler<br>FILT_PER<br>1<br>SAMPLE_EN COUT_SEL<br>CMP_NPMD CMP_HPMD HYSTCTR CMP_EN COUT_INV WINDOW_EN FILT_CNT COUT CFR/F_IE DMA_EN CFR/F COUT_PEN<br>Sampling Clock<br><!-- End of picture text -->

Figure 242. Sampled, Filtered (#4A): Sampling Point Externally Driven 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2068 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/059_Low_Power_Comparator_-LPCMP-/S32K3XXRM_数据表.pdf-2069-02.png)


<!-- Start of picture text -->
Internal Bus<br>0 >0x01 To open PAD for CMPO<br>INP DMA_REQ<br>+<br>Interrupt<br>Polarity Window Filter<br>- COUT_RAW Select Control Block Control/DMA  IRQ<br>INM<br>COUT<br>To other SOC functions<br>WINDOW/SAMPLE<br>1<br>0 CMPO to PAD<br>Bus Clock Divided Bus Clock<br>Clock 0 COUTA<br>1<br>Prescaler<br>FILT_PER<br>0<br>>0x00<br>SAMPLE_EN COUT_SEL<br>CMP_NPMD CMP_HPMD HYSTCTR CMP_EN COUT_INV WINDOW_EN FILT_CNT COUT CFR/F_IE DMA_EN CFR/F COUT_PEN<br>Sampling Clock<br><!-- End of picture text -->

Figure 243. Sampled, Filtered (#4B): Sampling Point Internally Derived 

In this mode, the path from analog inputs to COUTA is combinational(unclocked). Windowing control is completely bypassed. COUTA is sampled whenever a rising edge is detected on the sampling clock. 

The only difference in operation between sampled, non-filtered (#3A) and sampled, filtered (#4A) is that, now, CCR1[FILT_CNT]>1, which activates filter operation. 

The only difference in operation between sampled, non-filtered (#3B) and sampled, filtered (#4B) is that now, CCR1[FILT_CNT]>1, which activates filter operation. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2069 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

#### 59.3.2.5 Windowed Mode (#5A & 5B) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/059_Low_Power_Comparator_-LPCMP-/S32K3XXRM_数据表.pdf-2070-03.png)


<!-- Start of picture text -->
Internal Bus<br>1 To open PAD for CMPO<br>INP DMA_REQ<br>+<br>Interrupt<br>Polarity Window Filter<br>- COUT_RAW Select Control Block Control/DMA  IRQ<br>INM<br>COUT<br>To other SOC functions<br>WINDOW/SAMPLE<br>1<br>0 CMPO to PAD<br>Bus Clock Divided Bus Clock<br>Clock 0 COUTA<br>1<br>Prescaler<br>FILT_PER<br>0<br>0x00 (#5B)<br>SAMPLE_EN COUT_SEL<br>Figure 244. Windowed Mode<br>CMP_NPMD CMP_HPMD HYSTCTR CMP_EN COUT_INV WINDOW_EN FILT_CNT COUT CFR/F_IE DMA_EN CFR/F COUT_PEN<br>0x00 (#5A)<br>Sampling Clock<br><!-- End of picture text -->

In this mode, COUTA is clocked by the bus clock whenever window is enabled. The last latched value is held when window is disabled. The filter block is bypassed. 

The following figure illustrates comparator operation in this mode, ignoring latency of the analog comparator, polarity select, and window control block. It also assumes that the polarity select is set to non-inverting state. 

In actual operation, COUTA may lag the analog inputs by up to two bus clock cycles plus the combinational path delay through the comparator and polarity select logic. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/059_Low_Power_Comparator_-LPCMP-/S32K3XXRM_数据表.pdf-2070-07.png)


<!-- Start of picture text -->
WINDOW<br>COUT_RAW<br>COUTA<br>Figure 245. Windowed Mode Timing Diagram<br><!-- End of picture text -->

If CCR1[COUTA_OWEN] is set, user can define COUTA level as CCR1[COUTA_OW], when window is closed. Following figures show this case. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2070 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/059_Low_Power_Comparator_-LPCMP-/S32K3XXRM_数据表.pdf-2071-01.png)


<!-- Start of picture text -->
Low Power Comparator (LPCMP)<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/059_Low_Power_Comparator_-LPCMP-/S32K3XXRM_数据表.pdf-2071-02.png)


<!-- Start of picture text -->
WINDOW<br>COUT_RAW<br>COUTA<br>User defined lelvel(COUTA_OW=0)<br><!-- End of picture text -->

Figure 246. Windowed Mode Timing Diagram With User Defined Value 0 outside WINDOW 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/059_Low_Power_Comparator_-LPCMP-/S32K3XXRM_数据表.pdf-2071-04.png)


<!-- Start of picture text -->
WINDOW<br>COUT_RAW<br>COUTA<br>User defined lelvel(COUTA_OW=1)<br><!-- End of picture text -->

Figure 247. Windowed Mode Timing Diagram With User Defined Value 1 outside WINDOW 

~~<mark>NOTE</mark>~~ 

Obviously, when the window is open, COUT_A will switch from COUTA_OW to COUT_RAW. When the window is closed, COUT_A will switch from COUT_RAW to COUTA_OW. This may generate unnecessary transition flags, CFR or CFF. User needs to choose COUTA_OW carefully according to the actual application, and select the appropriate flag CFR or CFF to generate interrupt. 

If CCR1[WINDOW_CLS] is set, user can define the CMPO event (rising, falling or both edges, selected by CCR1[EVT_SEL]) to close the window. The external WINDOW signal has to go to zero and back to one to enable the internal window again. Following figure shows an example that CMPO rising edge close the internal window. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/059_Low_Power_Comparator_-LPCMP-/S32K3XXRM_数据表.pdf-2071-09.png)


<!-- Start of picture text -->
WINDOW<br>COUT_RAW<br>CMPO<br>WINDOW_INTERNAL<br>CMPO rising edge causes internal window close<br><!-- End of picture text -->

Figure 248. Windowed Mode Timing Diagram With CMPO Rising Edge Close Window 

If CCR1[WINDOW_INV] is set, user can invert the window signal before it is used. The following figure shows this case. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2071 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/059_Low_Power_Comparator_-LPCMP-/S32K3XXRM_数据表.pdf-2072-02.png)


<!-- Start of picture text -->
CCR1[WINDOW_INV]<br>WINDOW<br>WINDOW_INTERNAL<br>COUT_RAW<br>COUTA<br><!-- End of picture text -->

Figure 249. Windowed Mode Timing Diagram With WINDOW Signal Inverted. 

#### 59.3.2.6 Windowed/Resampled Mode (#6) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/059_Low_Power_Comparator_-LPCMP-/S32K3XXRM_数据表.pdf-2072-05.png)


<!-- Start of picture text -->
Internal Bus<br>1 0x01 To open PAD for CMPO<br>INP DMA_REQ<br>+<br>Interrupt<br>Polarity Window Filter<br>- COUT_RAW Select Control Block Control/DMA  IRQ<br>INM<br>COUT<br>To other SOC functions<br>WINDOW/SAMPLE<br>1<br>0 CMPO to PAD<br>Bus Clock Divided Bus Clock<br>Clock 0 COUTA<br>1<br>Prescaler<br>FILT_PER<br>0<br>>0x00<br>SAMPLE_EN COUT_SEL<br>Figure 250. Windowed/Resampled Mode<br>CMP_NPMD CMP_HPMD HYSTCTR CMP_EN COUT_INV WINDOW_EN FILT_CNT COUT CFR/F_IE DMA_EN CFR/F COUT_PEN<br>Sampling Clock<br><!-- End of picture text -->

This mode of operation results in an unfiltered string of comparator samples where the interval between the samples is determined by CCR1[FILT_PER] and the bus clock rate. Configuration for this mode is virtually identical to that for the windowed/filtered mode shown in the next section. The only difference is that the value of CCR1[FILT_CNT] in this mode must be 1. 

The following figure uses the same input stimulus shown in Figure 245, and adds resampling of COUTA to generate COUT. Samples are taken at the time points indicated by the arrows in the figure. Again, prop delays and latency are ignored for the sake of clarity. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2072 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/059_Low_Power_Comparator_-LPCMP-/S32K3XXRM_数据表.pdf-2073-01.png)


<!-- Start of picture text -->
Low Power Comparator (LPCMP)<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/059_Low_Power_Comparator_-LPCMP-/S32K3XXRM_数据表.pdf-2073-02.png)


<!-- Start of picture text -->
WINDOW<br>COUT_RAW<br>COUTA<br>Sample Point<br>COUT<br><!-- End of picture text -->

Figure 251. Windowed/Resampled Mode Operation 

This example was generated solely to demonstrate operation of the comparator in windowed/resampled mode, and does not reflect any specific application. Depending upon the sampling rate and window placement, COUT may not see zero-crossing events detected by the analog comparator. Sampling period and/or window placement must be carefully considered for a given application. 

#### 59.3.2.7 Windowed/Filtered Mode (#7) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/059_Low_Power_Comparator_-LPCMP-/S32K3XXRM_数据表.pdf-2073-06.png)


<!-- Start of picture text -->
Internal Bus<br>1 >0x01 To open PAD for CMPO<br>INP DMA_REQ<br>+<br>Interrupt<br>Polarity Window Filter<br>- COUT_RAW Select Control Block Control/DMA  IRQ<br>INM<br>COUT<br>To other SOC functions<br>WINDOW/SAMPLE<br>1<br>0 CMPO to PAD<br>Bus Clock Divided Bus Clock<br>Clock 0 COUTA<br>1<br>Prescaler<br>FILT_PER<br>0<br>>0x00<br>SAMPLE_EN COUT_SEL<br>CMP_NPMD CMP_HPMD HYSTCTR CMP_EN COUT_INV WINDOW_EN FILT_CNT COUT CFR/F_IE DMA_EN CFR/F COUT_PEN<br>Sampling Clock<br><!-- End of picture text -->

Figure 252. Windowed/Filtered Mode 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2073 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

The only difference in operation between Windowed/Resampled Mode (#6) and Windowed/Filtered Mode (#7) is that, now, CCR1[FILT_CNT]>1, which activates filter operation. 

This is the most complex mode of operation for the comparator block, as it utilizes both windowing and filtering features. It also has the highest latency of any of the modes. This can be approximated: up to 2 peripheral clock synchronization in the window function + ((CCR1[FILT_CNT] X CCR1[FILT_PER]) + 1) X peripheral clock for the filter function. 

### 59.3.3 Round Robin Trigger mode 

The Round Robin Trigger mode is enabled with RRCR0[RR_EN] and CCR0[CMP_EN]. A trigger event initiates a comparison sequence. The next trigger event should not come before the current sequence completes. 

The reference channel for either the plus side MUX or the minus side MUX is selected by RRCR1[RR_FIXP] and RRCR1[FIXCH]. The active channels are selected by RRCR1[RR_CHnEN]. 

When a trigger comes, the analog comparator is enabled. After the comparison sequence completes, the analog comparator is disabled again. The analog stabilization time is controlled by RRCR0[RR_INITMOD]. Make sure that the (RR_INITMOD*round robin clock period) should be longer than the initialization delay in the chip data sheet. 

When the stabilization process completes, the round robin manner comparison sequence begins. After the configurable number of operation clocks defined by RRCR0[RR_NSAM], the comparison result is sampled for the selected active channel. 

After all the active channels are sampled/compared, if the comparison result changes from its pre-programmed state, the corresponding flag in RRSR[RR_CHnF] is set. The pre-programmed state for each channel is configured by writing to RRCSR[RR_CHnOUT] field. RRCSR[RR_CHnOUT] is updated to store the last comparison result for each channel. If any flag in RRSR[RR_CHnF] is set, flag CSR[RRF] will be set. If IER[RRF_IE] is set, an asynchronous interrupt is asserted. Note that these flags do not support generating a DMA transfer event. 

The following diagram shows the basic flow of this mode. In the diagram, RRCR1[RR_CH1EN], RRCR1[RR_CH3EN], and RRCR1[RR_CH4EN] are set, so channels #1, #3, and #4 are selected for round robin depended on their priority setting. RRCR0[RR_NSAM] is set to 2'b01, so one clock later the comparison result of the selected channel is sampled. When channel #4 is compared, the result is sampled, and round robin ends. If any of the comparison results from channel #1, #3, or #4 changed from their programmed value (written to RRCSR[RR_CH1OUT], RRCSR[RR_CH3OUT], and RRCSR[RR_CH4OUT]), an interrupt is generated. Software can then poll the RRSR[RR_CHnF] to see which channel input(s) changed value. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/059_Low_Power_Comparator_-LPCMP-/S32K3XXRM_数据表.pdf-2074-11.png)


<!-- Start of picture text -->
Round Robin<br>Clock<br>Round Robin<br>Trigger RR_INITMOD<br>Round Robin<br>Start NSAM NSAM NSAM<br>CMP(and possible DAC)<br>Enable<br>Active Channel  IDLE CH1 CH3 CH4<br>Select State<br>Sample Channel<br>Comparision Resul t<br>Channel<br>RR_CH1OUT RR_CH1/3OUT RR_CH1/3/4OUT<br>Results<br>Possible<br>Interrupt<br><!-- End of picture text -->

Figure 253. Trigger Mode 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2074 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

The table below shows the channel decode in both functional mode and trigger mode. Other cases not in the table are illegal. 

Table 294. CMP Channel Decode in Functional Mode and Trigger mode 

|Mode|RR_E<br>N|PSEL[2:<br>0]|MSEL[2:<br>0]|INPSEL[1:<br>0]|INMSEL[1<br>:0]|FIX<br>P|FIXCH[2<br>:0]|RR_CH<br>xN|INP|INM|CMP<br>Behavior|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Function<br>al Mode|0|x<sup>1</sup>|0~7|0|1|x|x|x|DAC|Channel<br>decoded<br>from<br>MSEL[2:<br>0]|Channel<br>0~7 can<br>be<br>compared<br>with DAC|
|||0~7|x|1|0|x|x|x|Channel<br>decoded<br>from<br>PSEL[2:0<br>]|DAC|Channel<br>0~7 can<br>be<br>compared<br>with DAC|
|||0~7|0~7|1|1|x|x|x|Channel<br>decoded<br>from<br>PSEL[2:0<br>]|Channel<br>decoded<br>from<br>MSEL[2:<br>0]|Channel<br>0~7 can<br>be<br>compared<br>with<br>channel<br>0~7<sup>2</sup>|
|Trigger<br>Mode|1|x|x|0|1|0|x|0~7|DAC|Channel<br>sweep<br>(RR_CHx<br>N)|Channel<br>0~7 can<br>be swept<br>with DAC|
|||x|x|1|0|1|x|0~7|Channel<br>sweep<br>(RR_CHx<br>N)|DAC|Channel<br>0~7 can<br>be swept<br>with DAC|
|||x|x|1|1|0|0~7|0~7|Channel<br>fixed by<br>FIXCH[2:<br>0]|Channel<br>sweep<br>(RR_CHx<br>N)|Channel<br>0~7 can<br>be swept<br>with a<br>fixed<br>channel(0<br>~7)<sup>3</sup>|
|||x|x|1|1|1|0~7|0~7|Channel<br>sweep<br>(RR_CHx<br>N)|Channel<br>fixed by<br>FIXCH[2:<br>0]|Channel<br>0~7 can<br>be swept<br>with a<br>fixed<br>channel(0<br>~7)<sup>3</sup>|



> 1. "x" means "don't care" 

> 2. PSEL should not be same as MSEL. 

3. Channel in the sweep side should not be same as the fixed side. 

##### Trigger Mode Programming Recommendation 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2075 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

Configure the Trigger Mode as follows. Register fields in the same register can be configured at the same time. 

1. Configure the comparison cycles by RRCR0[RR_NSAM]. Note: It is a mandatory request that the round robin cycling period must be set longer than the time that all the active channels complete the specified comparison cycles set by RRCR0[RR_NSAM]. 

2. Configure CMP initialization delay by RRCR0[RR_INITMOD] Note: In programming the RRCR0[RR_INITMOD] registers, the RR_INITMOD x round robin clock period must be longer than the initialization delay, which can be referred from the chip data sheet. 

3. Configure the RRCR1[FIXP] to select the fixed port of CMP and 

   - a. If using one input channel to compare with other channels, configure the RRCR1[FIXCH] to select the fixed channel 

   - b. If using DAC output to compare with input channels, configure the CCR2[INPSEL] or CCR2[INMSEL](according to RRCR1[FIXP] )to select the DAC output 

4. Configure channels for comparison by RRCR1[RR_CHnEN] 

5. Write RRCSR[RR_CHnOUT] to define the pre-set state of channel n. 

6. Clear channel flags RRSR[RR_CHnF] 

7. Enable round robin interrupt by IER[RRF_IE] (disable IER[CFR_IE] and IER[CFF_IE]) 

8. Enable round robin mode by RRCR0[RR_EN] 

9. Enable comparator by CCR0[CMP_EN] 

### 59.3.4 Low-Pass Filter 

The low-pass filter operates on the unfiltered, optionally inverted comparator output COUTA and generates the filtered and synchronized output COUT. Both COUTA and COUT can be configured as module outputs and are used for different purposes within the system. 

Synchronization and edge detection are always used to determine status register bit values. They also apply to COUT for all sampling and windowed modes. Filtering can be performed using an internal timebase defined by CCR1[FILT_PER], or using an external SAMPLE input to determine sample time. 

The need for digital filtering and the amount of filtering is dependent on user requirements. Filtering can become more useful in the absence of an external hysteresis circuit. Without external hysteresis, high-frequency oscillations can be generated at COUTA when the selected INM and INP input voltages differ by less than the offset voltage of the differential comparator. 

#### 59.3.4.1 Enabling Filter Modes 

Filter modes can be enabled by: 

- Setting CCR1[FILT_CNT] > 0x01 and 

- Setting CCR1[FILT_PER] to a nonzero value or setting CCR1[SAMPLE_EN]=1 

If using the divided bus clock to drive the filter, it samples COUTA every CCR1[FILT_PER] bus clock cycles. 

If CCR1[SAMPLE_EN]=1, the filter samples COUTA on each positive transition of the SAMPLE input. The output state of the filter changes when all the consecutive CCR1[FILT_CNT] samples agree that the output value has changed. 

#### 59.3.4.2 Latency issues 

Program the value of CCR1[FILT_PER] or SAMPLE period such that the sampling period is just longer than the period of the expected noise to ensure that a given noise spike corrupts only one sample. The value of CCR1[FILT_CNT] must be chosen to reduce the probability of noisy samples causing an incorrect transition to be recognized. The probability of an incorrect transition is defined as the probability of an incorrect sample raised to the power of CCR1[FILT_CNT]. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2076 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

The values of CCR1[FILT_PER] or SAMPLE period and CCR1[FILT_CNT] must also be traded off against the desire for minimal latency in recognizing actual comparator output transitions. The probability of detecting an actual output change within the nominal latency is the probability of a correct sample raised to the power of CCR1[FILT_CNT]. 

Table 293 summarizes maximum latency values for the various modes of operation in the absence of noise. Filtering latency is restarted each time an actual output transition is masked by noise. 

### 59.3.5 Low Power Mode Operation 

The following table shows the false mode operation of the LPCMP module. 

Table 295. Low Power Mode Operation 

|Mode of Operation|Description|
|---|---|
|false|LPCMP can operate only in continuous mode or trigger mode.|



### 59.3.6 DMA 

When DMA support is enabled by setting CCR1[DMA_EN] and the interrupt is enabled by setting IER[CFR_IE], IER[CFF_IE], or both, the corresponding change on COUT forces a DMA transfer request rather than a CPU interrupt instead. When the DMA has completed the transfer, it sends a transfer completing indicator signal that de-asserts the DMA transfer request and clears the flags (both CSR[CFR] and CSR[CFF]) to allow a subsequent change on comparator output to occur and force another DMA request. 

### 59.3.7 Clocking 

LPCMP requires the following clocks to operate: 

- Bus clock is used for register access and window/filter function. 

- Round robin clock for trigger mode. 

### 59.3.8 Resets 

The global chip reset signal resets LPCMP. 

### 59.3.9 Interrupts 

When corresponding interrupt enable register bit is set, flags CSR[CFR], CSR[CFF], CSR[RRF] can generate interrupt, assuming the DMA enable bit is not set. The interrupt is de-asserted by clearing either the flag or the interrupt enable register bit. 

## 59.4 External Signals 

Table 296. External Signal Descriptions 

|Signal|Description|I/O|
|---|---|---|
|CMPO|Filtered or unfiltered comparator output|O|
|Input_Analog_Channels|Analog input channels(Refer to the chip-specific information for the<br>connections)|I|
|VREFH_EXT|External reference voltage for the CMP-DAC(Refer to the chip-<br>specific information for the connections)|I|



## 59.5 Initialization 

To enable LPCMP, configure the control registers (CCR1, CCR2, DCR, and so on) before setting CCR0[CMP_EN]. To disable the module, clear CCR0[CMP_EN]. Switching operation modes or changing control register bits on the fly (when CCR0[CMP_EN] 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2077 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

is 1) may cause noise on the COUT or COUTA signals. To avoid unwanted signal noise, be sure to disable the module before switching modes or changing control bits. 

The time required to stabilize COUT is the power-on delay of the comparators plus the largest propagation delay from a selected analog source through the analog comparator, windowing function, and filter. See the data sheet for power-on delays of the comparators. The delay caused by windowing and filter function is specified in the Table 293. 

During operation, the propagation delay of the selected data paths must always be considered. It can take many bus clock cycles for COUT and CSR[CFR]/CSR[CFF] to reflect an input change or a configuration change to one of the components involved in the data path. 

## 59.6 Application Information 

### 59.6.1 Round-robin clock(RCLK) frequency requirement 

##### (1) RCLK High Frequency Limit 

RCLK high frequency limit depends on two facts: 

1. The analog CMP and DAC initialization time(See the chip data sheet for the initialization time.) 

   - Register field RR_INITMOD provides a maximum 63 RCLK cycles for the analog CMP and DAC initialization. 

   - Rclk must be slow enough to satisfy: 63 * (1/fRCLK) > Tinialization, where fRCLK is in MHz, and Tinializationis in microsecond. 

   - so fRCLK < 63 / Tinialization 

   - Example: Tinialization = 40 microsecond, then fRCLK should be smaller than 1.575MHz. 

2. The analog CMP propagation delay(See the chip datasheet for the CMP propagation delay.) 

   - Register field NSAM field provides a maximum 4 RCLK cycles for the analog CMP propagation delay. 

   - Rclk must be slow enough to satisfy: 4 * (1/fRCLK) > Tpropagation, where fRCLK is in MHz, and Tpropagation is in microsecond. 

   - so fRCLK < 4 / Tpropagation 

   - Example: Tpropagation = 0.1 microsecond, then fRCLK should be smaller than 40 MHz. 

##### (2) RCLK Low Frequency Limit 

In theory, RCLK frequency has no low limit. But the lower the RCLK frequency, the longer the scan time. Therefore, the lower limit of the RCLK frequency depends on the system application. 

## 59.7 LPCMP register descriptions 

The memory map comprises of 32-bit aligned registers which can be accessed via 8-, 16- or 32-bit reads and 32-bit write. Attempted accesses using unsupported write data sizes, writes to read-only resources, or to reserved spaces are terminated with an error. Read access to reserved address will also generate a transfer error and the read data bus will show all 0s. 

### 59.7.1 LPCMP memory map 

LPCMP_0 base address: 4037_0000h 

LPCMP_1 base address: 4037_4000h 

LPCMP_2 base address: 404E_8000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|Version ID Register (VERID)|32|RO|0100_0001h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2078 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|4h|Parameter Register (PARAM)|32|RO|0000_0002h|
|8h|Comparator Control Register 0 (CCR0)|32|RW|0000_0002h|
|Ch|Comparator Control Register 1 (CCR1)|32|RW|0000_0000h|
|10h|Comparator Control Register 2 (CCR2)|32|RW|0000_0000h|
|18h|DAC Control Register (DCR)|32|RW|0000_0000h|
|1Ch|Interrupt Enable Register (IER)|32|RW|0000_0000h|
|20h|Comparator Status Register (CSR)|32|W1C|0000_0000h|
|24h|Round Robin Control Register 0 (RRCR0)|32|RW|0000_0000h|
|28h|Round Robin Control Register 1 (RRCR1)|32|RW|0000_0000h|
|2Ch|Round Robin Control and Status Register (RRCSR)|32|RW|0000_0000h|
|30h|Round Robin Status Register (RRSR)|32|W1C|0000_0000h|



### 59.7.2 Version ID Register (VERID) 

##### Offset 

|Register|Offset|
|---|---|
|VERID|0h|



##### Function 

Contains version numbers for the module design and feature set. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||MA|JOR|||||||MIN|OR||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|1|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||FEAT|URE||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2079 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

##### Fields 

|Field|Function|
|---|---|
|31-24|Major Version Number|
|MAJOR|Returns the major version number for the module design.|
|23-16|Minor Version Number|
|MINOR|Returns the minor version number for the module design.|
|15-0|Feature Specification Number|
|FEATURE|Returns the feature set number.|
||0000_0000_0000_0001b - Round robin feature|



### 59.7.3 Parameter Register (PARAM) 

##### Offset 

|Register|Offset|
|---|---|
|PARAM|4h|



##### Function 

Contains parameter values that are implemented in the module. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||Rese|rved||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||Rese|rved|||||||DAC|_RES||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|0|



##### Fields 

|Field|Function|
|---|---|
|31-4<br>—|Reserved|
|3-0|DAC Resolution|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2080 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|DAC_RES|Indicates the DAC resolution supported by this implementation.<br>0000b - 4 bit DAC|
||0001b - 6 bit DAC|
||0010b - 8 bit DAC|
||0011b - 10 bit DAC|
||0100b - 12 bit DAC|
||0101b - 14 bit DAC|
||0110b - 16 bit DAC|



### 59.7.4 Comparator Control Register 0 (CCR0) 

##### Offset 

|Register|Offset|
|---|---|
|CCR0|8h|



##### Function 

Contains configuration options for enabling the analog comparator and the DAC. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||0|||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||||0|||||||LINKE|CMP_|CMP_|
|W||||||||||||||N|STO...|EN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|0|



##### Fields 

|Field|Function||
|---|---|---|
|31-3<br>—|Reserved|Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2081 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|2<br>LINKEN|CMP-to-DAC Link Enable<br>Controls the link from the CMP enable to the DAC enable.<br>0b - Disable the CMP-to-DAC link: enabling or disabling the DAC is independent from enabling or<br>disabling the CMP.<br>1b - Enable the CMP-to-DAC link: the DAC enable/disable is controlled by the CMP_EN bit<br>instead of DCR[DAC_EN]. Also, when the CMP is auto-disabled because software selects the<br>same signal for both the plus and minus comparator inputs, the DAC is disabled too.|
|1|Comparator false Mode Enable|
|CMP_STOP_E<br>N|Allows software to enable the analog comparator or the DAC when the device is in false mode.<br>CMP_STOP_EN has no effect in trigger mode.<br>~~NOTE~~|
||0b - Disable the analog comparator regardless of CMP_EN.<br>1b - Allow the analog comparator to be enabled by CMP_EN.|
|0<br>CMP_EN|Comparator Enable<br>Enables the analog comparator.<br>When CCR0[LINKEN]=1, CMP_EN also controls the enabling/disabling of the DAC instead<br>of DCR[DAC_EN].<br>~~NOTE~~|
||0b - Disable (The analog logic remains off and consumes no power.)<br>1b - Enable|



### 59.7.5 Comparator Control Register 1 (CCR1) 

##### Offset 

|Register|Offset|
|---|---|
|CCR1|Ch|



##### Function 

Contains configuration options for comparator operation, such as enabling Sampling or Windowing mode. 

~~<mark>NOTE</mark>~~ 

Sampling and Windowing modes cannot both be enabled at the same time. Sampling mode takes precedence over Windowing mode. If software attempts to set both SAMPLE_EN and WINDOW_EN, only SAMPLE_EN is set. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2082 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/059_Low_Power_Comparator_-LPCMP-/S32K3XXRM_数据表.pdf-2083-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>FILT_PER  FILT_CNT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 WIND WIND COUT COUT COUT COUT COUT DMA_ SAMP WIND<br>EVT_SEL<br>W OW_... OW_... A_OW  A_O... _PEN  _SEL  _INV  EN  LE_... OW_...<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-24|Filter Sample Period|
|FILT_PER|Specifies the sampling period (in bus clock cycles) of the comparator output filter. Programming FILT_PER<br>to 0x00 bypasses the filter. Filter programming and latency details are provided in the functional<br>description section.<br>FILT_PER has no effect in Sampling mode (CCR1[SAMPLE_EN]=1).<br>~~NOTE~~|
|23-19|Reserved|
|—<br>18-16|Filter Sample Count|
|FILT_CNT|Specifies the number of consecutive samples that must agree before the comparator ouput filter accepts<br>the sample as a new valid output state. For information regarding filter programming and latency, see the<br>functional description section.<br>000b - Filter is bypassed: COUT = COUTA<br>001b - 1 consecutive sample (Comparator output is simply sampled.)<br>010b - 2 consecutive samples<br>011b - 3 consecutive samples<br>100b - 4 consecutive samples<br>101b - 5 consecutive samples<br>110b - 6 consecutive samples<br>111b - 7 consecutive samples|
|15-14<br>—|Reserved|
|13-12|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2083 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|11-10<br>EVT_SEL|CMPO Event Select<br>Selects which CMPO signal edge (rising, falling, or both) defines a CMPO event.<br>Valid only in Windowing mode.<br>~~NOTE~~|
||00b - Rising edge<br>01b - Falling edge<br>1xb - Both edges|
|9|CMPO Event Window Close|
|WINDOW_CLS|Enables a CMPO event (defined as a CMPO rising edge, falling edge, or both) to close an active window.<br>See the EVT_SEL field to configure the CMPO event.<br>The WINDOW signal has to go to zero and back to one again to re-activate the window.<br>Valid only in Windowing mode.<br>~~NOTE~~<br>0b - CMPO event cannot close the window<br>1b - CMPO event can close the window|
|8<br>WINDOW_INV|WINDOW/SAMPLE Signal Invert<br>Inverts the WINDOW/SAMPLE signal.<br>0b - Do not invert<br>1b - Invert|
|7<br>COUTA_OW|COUTA Output Level for Closed Window<br>Defines the COUTA signal value when the window is closed.<br>Valid only in Windowing mode and when COUTA_OWEN=1.<br>~~NOTE~~<br>0b - COUTA is 0<br>1b - COUTA is 1|
|6<br>COUTA_OWEN|COUTA_OW Enable<br>Enables the COUTA signal value to be defined by the COUTA_OW bit when the window is closed.<br>Valid only in Windowing mode.<br>~~NOTE~~<br>0b - COUTA holds the last sampled value|
||1b - COUTA is defined by the COUTA_OW bit|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2084 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|5<br>COUT_PEN|Comparator Output Pin Enable<br>Enables the comparator output to become an available signal option for a selected package pin.<br>0b - Not available<br>1b - Available|
|4<br>COUT_SEL|Comparator Output Select<br>Selects which comparator output option, COUT or COUTA, to use for CMPO.<br>0b - Use COUT (filtered)<br>1b - Use COUTA (unfiltered)|
|3<br>COUT_INV|Comparator Invert<br>Selects the polarity of the analog comparator function, affecting the value driven to the COUT output (on<br>both the device pin and as CSR[COUT]) when CCR0[CMP_EN] is 0.<br>COUT_INV has no effect in trigger mode.<br>~~NOTE~~<br>0b - Do not invert<br>1b - Invert|
|2<br>DMA_EN|DMA Enable<br>Enables DMA transfers triggered from the LPCMP module. When DMA_EN and the corresponding<br>interrupt enable bit are set, a DMA request is asserted when CFR or CFF is set.<br>0b - Disable<br>1b - Enable|
|1<br>SAMPLE_EN|Sampling Enable<br>Enables Sampling mode.<br>0b - Disable<br>1b - Enable|
|0<br>WINDOW_EN|Windowing Enable<br>Enables Windowing mode.<br>Valid only when SAMPLE_EN=0.<br>~~NOTE~~|
||0b - Disable<br>1b - Enable|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2085 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

### 59.7.6 Comparator Control Register 2 (CCR2) 

##### Offset 

|Register|Offset|
|---|---|
|CCR2|10h|



##### Function 

Contains configuration options for comparator operation, such as selecting the plus and minus comparator inputs and the hysteresis levels. 

~~<mark>NOTE</mark>~~ 

When an inappropriate operation selects the same signal for both the plus and minus comparator inputs, the analog comparator automatically shuts down (regardless of CMP_EN) to prevent itself from becoming a noise generator. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/059_Low_Power_Comparator_-LPCMP-/S32K3XXRM_数据表.pdf-2086-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0 0 0<br>INMSEL  INPSEL  MSEL  PSEL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 OFFS 0 CMP_<br>HYSTCTR<br>ET  HPMD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-30|Reserved|
|—||
|29-28|Input Minus Select|
|INMSEL|Selects the minus input of the comparator.|
||These selections connect directly to the minus input of the comparator.<br>~~NOTE~~|
||00b - IN0: from the 8-bit DAC output|
||01b - IN1: from the analog 8-1 mux|
||10b - Reserved|
||11b - Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2086 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/059_Low_Power_Comparator_-LPCMP-/S32K3XXRM_数据表.pdf-2087-03.png)


<!-- Start of picture text -->
Field Function<br>27-26 Reserved<br>—<br>25-24 Input Plus Select<br>INPSEL Selects the plus input of the comparator.<br>  NOTE<br>These selections connect directly to the plus input of the comparator.<br>00b - IN0: from the 8-bit DAC output<br>01b - IN1: from the analog 8-1 mux<br>10b - Reserved<br>11b - Reserved<br>23 Reserved<br>—<br>22-20 Minus Input MUX Select<br>MSEL Selects the input used for the negative mux. See the chip-specific LPCMP information to get the<br>detailed connections.<br>  NOTE<br>MSEL has no effect in trigger mode.<br>000b - Input 0<br>001b - Input 1<br>010b - Input 2<br>011b - Input 3<br>100b - Input 4<br>101b - Input 5<br>110b - Input 6<br>111b - Input 7<br>19 Reserved<br>—<br>18-16 Plus Input MUX Select<br>PSEL Selects the input used for the positive mux. See the chip-specific LPCMP information to get the<br>detailed connections.<br>  NOTE<br>PSEL has no effect in trigger mode.<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2087 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||000b - Input 0<br>001b - Input 1<br>010b - Input 2<br>011b - Input 3<br>100b - Input 4<br>101b - Input 5<br>110b - Input 6<br>111b - Input 7|
|15-6<br>—|Reserved|
|5-4|Comparator Hysteresis Control|
|HYSTCTR|Selects the level of internally generated hysteresis for the comparator output. See the chip data sheet to get<br>the specific values for each hysteresis level.<br>00b - Level 0|
||01b - Level 1|
||10b - Level 2|
||11b - Level 3|
|3|Reserved|
|—||
|2<br>OFFSET|Comparator Offset Control<br>Selects the level of internally generated voltage offset for the comparator output. See the chip data sheet<br>to get the specific values for each offset level.<br>0b - Level 0: The hysteresis selected by HYSTCTR is valid for both directions (rising and falling).<br>1b - Level 1: Hysteresis does not apply when INP (input-plus) crosses INM (input-minus) in the<br>rising direction or when INM crosses INP in the falling direction. Hysteresis still applies for INP<br>crossing INM in the falling direction.|
|1|Reserved|
|—<br>0|CMP High Power Mode Select|
|CMP_HPMD|Selects Low or High Power(Speed) mode for the comparator.<br>0b - Low power(speed) comparison mode|
||1b - High power(speed) comparison mode|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2088 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

### 59.7.7 DAC Control Register (DCR) 

##### Offset 

|Register|Offset|
|---|---|
|DCR|18h|



##### Function 

Contains configuration options for enabling the DAC. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||0||||||||DAC_|DATA||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|0|||0||||VRSE|||0||||0|DAC_|
|W||||||||L||||||||EN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-24|Reserved|
|—||
|23-16|DAC Output Voltage Select|
|DAC_DATA|Selects the DAC output (DACO) voltage from one of 256 distinct levels. The DACO range is from Vin/256<br>to Vin:<br>DACO = (Vin/256) * (DAC_DATA + 1)|
|15<br>—|Reserved|
|14-9<br>—|Reserved|
|8|DAC Reference High Voltage Source Select|
|VRSEL|Selects the high voltage reference source for the Vin supply of the DAC's resistor ladder network. See<br>the chip-specific LPCMP information for the source of vrefh0 and vrefh1.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2089 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - vrefh0|
||1b - vrefh1|
|7-2|Reserved|
|—<br>1|Reserved|
|—<br>0|DAC Enable|
|DAC_EN|Enables the DAC. When disabled, the DAC is powered down to conserve power.|
||0b - Disable|
||1b - Enable|



### 59.7.8 Interrupt Enable Register (IER) 

##### Offset 

|Register|Offset|
|---|---|
|IER|1Ch|



##### Function 

Provides enable bits for the comparator and round-robin flag interrupts. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||||||||0||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||||0|||||||RRF_|CFF_|CFR_|
|W||||||||||||||IE|IE|IE|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2090 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

##### Fields 

|Field|Function|
|---|---|
|31-3|Reserved|
|—<br>2|Round-Robin Flag Interrupt Enable|
|RRF_IE|Enables the Round-Robin Flag interrupt.<br>0b - Disable<br>1b - Enable: Assert an interrupt when the comparison result changes for a given channel.|
|1<br>CFF_IE|Comparator Flag Falling Interrupt Enable<br>Enables the Comparator Flag Falling interrupt.<br>0b - Disable<br>1b - Enable: Assert an interrupt when CFF is set.|
|0|Comparator Flag Rising Interrupt Enable|
|CFR_IE|Enables the Comparator Flag Rising interrupt.<br>0b - Disable<br>1b - Enable: Assert an interrupt when CFR is set.|



### 59.7.9 Comparator Status Register (CSR) 

##### Offset 

|Register|Offset|
|---|---|
|CSR|20h|



##### Function 

##### Provides the COUT, and CFF, CFR, RRF flags. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||0|||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||0||||COUT|||0|||RRF|CFF|CFR|
|W||||||||||||||W1C|W1C|W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2091 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

##### Fields 

|Field|Function|
|---|---|
|31-9<br>—|Reserved|
|8|Analog Comparator Output|
|COUT|Returns the current value of the analog comparator output, when read. The field is reset to 0 and reads<br>as CCR1[COUT_INV] when the analog comparator module is disabled, that is, when CCR0[CMP_EN] =<br>0. Writing to this field is ignored.|
|7-3|Reserved|
|—<br>2<br>RRF|Round-Robin Flag<br>Detects when any channel's last comparison result is different from the pre-set value in trigger mode. To<br>clear RRF, write 1 to it. RRF is cleared when CCR0[CMP_EN] or RRCR0[RR_EN] is not set.<br>0b - Not detected<br>1b - Detected|
|1<br>CFF|Analog Comparator Flag Falling<br>Detects when a falling edge on COUT occurs. CFF is cleared by writing 1 to it when CCR1[DMA_EN]<br>is disabled. If CCR1[DMA_EN] is enabled, the flag is automatically cleared when DMA is done. CFF is<br>cleared when CCR0[CMP_EN] is not set.<br>0b - Not detected<br>1b - Detected|
|0<br>CFR|Analog Comparator Flag Rising<br>Detects when a rising edge on COUT occurs. CFR is cleared by writing 1 to it when CCR1[DMA_EN]<br>is disabled. If CCR1[DMA_EN] is enabled, the flag is automatically cleared when DMA is done. CFR is<br>cleared when CCR0[CMP_EN] is not set.<br>0b - Not detected<br>1b - Detected|



### 59.7.10 Round Robin Control Register 0 (RRCR0) 

##### Offset 

|Register|Offset|
|---|---|
|RRCR0|24h|



##### Function 

Contains configuration options for round robin operation, such as enabling it and specifying the initialization delay. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2092 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

##### Diagram 

|Bits|31||30|29|28|27|26|25|24|23||22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||0|||||0||||RR_INI|TMOD|||
|Reset|0||0|0|0|0|0|0|0|0||0|0|0|0|0|0|0|
|Bits|15||14|13|12|11|10|9|8|7||6|5|4|3|2|1|0|
|R||0||0||0||RRN|SAM||||0||||0|RR_|
|W||||||||_||||||||||EN|
|Reset|0||0|0|0|0|0|0|0|0||0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-24|Reserved|
|—||
|23-22|Reserved|
|—||
|21-16|Initialization Delay Modulus|
|RR_INITMOD|Specifies the number of round-robin clock cycles used to determine the comparator and DAC initialization<br>delay as specified in the chip datasheet. The initiallization delay is calculated as: RR_INITMOD * (round-<br>robin clock period).<br>For example, if the initialization delay is 80us and the round-robin clock is 100kHz, program RR_INITMOD<br>to be 80us/10us = 8.<br>00_0000b - 63 cycles (same as 111111b)<br>00_0001b-11_1111b - 1 to 63 cycles|
|15-14<br>—|Reserved|
|13-12<br>—|Reserved|
|11-10<br>—|Reserved|
|9-8<br>RR_NSAM|Number of Sample Clocks<br>Specifies how many round-robin clock cycles to wait after the active channel is scanned before sampling<br>the channel's comparison result. After the next cycle of the round-robin clock, the sampling takes place<br>RR_NSAM clocks later.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2093 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||00b - 0 clocks|
||01b - 1 clocks|
||10b - 2 clocks|
||11b - 3 clocks|
|7-2<br>—|Reserved|
|1<br>—|Reserved|
|0|Round-Robin Enable|
|RR_EN|Enables round-robin operation.|
||0b - Disable|
||1b - Enable|



### 59.7.11 Round Robin Control Register 1 (RRCR1) 

##### Offset 

|Register|Offset|
|---|---|
|RRCR1|28h|



##### Function 

Contains configuration options for round robin operation, such as enabling individual channels to participate. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/059_Low_Power_Comparator_-LPCMP-/S32K3XXRM_数据表.pdf-2094-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0<br>FIXCH  FIXP<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 RR_C RR_C RR_C RR_C RR_C RR_C RR_C RR_C<br>W H7EN  H6EN  H5EN  H4EN  H3EN  H2EN  H1EN  H0EN<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2094 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

##### Fields 

|Field|Function|
|---|---|
|31-23<br>—|Reserved|
|22-20|Fixed Channel Select|
|FIXCH|Selects which channel in the mux port to fix for a given trigger mode application.<br>000b - Channel 0<br>001b - Channel 1<br>010b - Channel 2|
||011b - Channel 3|
||100b - Channel 4|
||101b - Channel 5<br>110b - Channel 6|
||111b - Channel 7|
|19-17<br>—|Reserved|
|16<br>FIXP|Fixed Port<br>Fixes (locks) an analog mux port (Plus or Minus) for trigger mode. The inputs to the non-fixed port are<br>swept during each round.<br>0b - Fix the Plus port. Sweep only the inputs to the Minus port.<br>1b - Fix the Minus port. Sweep only the inputs to the Plus port.|
|15-8<br>—|Reserved|
|7-0<br>RR_CHnEN|Channel n Input Enable in Trigger Mode<br>Enables channel n of the non-fixed mux port to have its voltage value checked when in trigger mode.<br>RR_CHnEN has no effect when the same channel is selected as the reference voltage.<br>~~NOTE~~|
||0b - Disable<br>1b - Enable|



### 59.7.12 Round Robin Control and Status Register (RRCSR) 

##### Offset 

|Register|Offset|
|---|---|
|RRCSR|2Ch|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2095 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

##### Function 

Contains the latest comparison results of the individual channels with the fixed mux port. It also allows software to define the pre-set state for each channel. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/059_Low_Power_Comparator_-LPCMP-/S32K3XXRM_数据表.pdf-2096-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 RR_C RR_C RR_C RR_C RR_C RR_C RR_C RR_C<br>W H7O... H6O... H5O... H4O... H3O... H2O... H1O... H0O...<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-8|Reserved|
|—<br>7-0|Comparison Result for Channel n|
|RR_CHnOUT|Reading RR_CHnOUT returns the latest comparison result for channel n.|
||Writing RR_CHnOUT defines the pre-set state for channel n.|



### 59.7.13 Round Robin Status Register (RRSR) 

##### Offset 

|Register|Offset|
|---|---|
|RRSR|30h|



##### Function 

Contains individual channel flags indicating when a channel's last comparison result is different from its pre-set value. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2096 / 4640 

NXP Semiconductors 

Low Power Comparator (LPCMP) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||||0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||0|||||RR_<br>CH7F|RR_<br>CH6F|RR_<br>CH5F|RR_<br>CH4F|RR_<br>CH3F|RR_<br>CH2F|RR_<br>CH1F|RR_<br>CH0F|
|W|||||||||W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-8|Reserved|
|—||
|7-0|Channel n Input Changed Flag|
|RR_CHnF|Indicates when the corresponding channel's last comparison result is different from its pre-set value.|
||To clear a flag, write a 1 to it.<br>~~NOTE~~|
||0b - Not different|
||1b - Different|



## 59.8 Glossary 

CMP Comparator DAC Digital-to-analog convertor ANMUX Analog multiplexer 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2097 / 4640 

