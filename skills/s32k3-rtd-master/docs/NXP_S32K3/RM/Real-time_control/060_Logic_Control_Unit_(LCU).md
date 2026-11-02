NXP Semiconductors 

# Chapter 60 Logic Control Unit (LCU) 

## 60.1 Chip-specific LCU information 

### 60.1.1 LCU instances 

This chip has two identical LCU instances, LCU_0 and LCU_1. 

## 60.2 Introduction 

LCU selects multiple inputs from timers, pulse width modulation (PWM) signals, and input/output (I/O) pads, and combines them using a programmable logic function to create output waveforms for use by other IPs. 

It consists of 3 LCs, each of which takes four inputs and creates four outputs using user-defined logic mapping. LCU also has 3 force inputs that can override the output logic and force a user-defined value directly on the output signals. Additionally, LCU has 2 sync inputs that can control when the inputs are updated to produce new output signals. 

LCU generates the interrupts and DMA requests based on output signals and force input signals. 

## 60.3 Feature list 

- 3 LCs with programmable logic function for generating output results 

- 12 inputs to and 12 outputs from each LC 

- Muxing to map any input to any LC 

- Independent filters for the rising and falling output states of each LC 

- Software override logic for inputs using multiple modes 

- 3 force inputs with programmable edge filtering to force output states using multiple modes 

- 2 sync inputs to control transition timing 

- Lock bit to block writes to configuration registers 

- Interrupt request generation based on output change or force event 

- DMA transfer request generation based on output change or force event 

## 60.4 Block diagram 

This figure illustrates an example implementation of LCU with: 

- Three LCs 

- Four force inputs 

- Four sync inputs 

For the number of each resource in this chip, see Feature list. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2098 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2099-02.png)


<!-- Start of picture text -->
To MUX....<br>0 0<br>l0 1 l0_DFF[0] LC0 O0_DFF[0]<br>l1 2 l1_DFF[0] O1_DFF[0]<br>l2 l2_DFF[0] O2_DFF[0]<br>3<br>l3 4 l3_DFF[0] O3_DFF[0]<br>l4 5 To I/O Pads<br>l5<br>6 sync[0] O0[0]<br>l6<br>7 sync[1] O1[0]<br>l7 8 sync[2] O2[0]<br>l8 9 sync[3] O3[0]<br>l9 force[0]<br>10<br>l10 force[1]<br>11 int_req[0]<br>l11 force[2]<br>12 dma_req[0]<br>force[3]<br>To MUX....<br>l0_DFF[1] O0_DFF[1]<br>LC1<br>l1_DFF[1] O1_DFF[1]<br>l2_DFF[1] O2_DFF[1]<br>l3_DFF[1] O3_DFF[1]<br>To I/O Pads<br>sync[0] O0[1]<br>O0_DFF[0] sync[1] O1[1]<br>13 sync[2]<br>O1_DFF[0] O2[1]<br>14 sync[3]<br>O2_DFF[0] O3[1]<br>15<br>O3_DFF[0] force[0]<br>16<br>O0_DFF[1] 17 force[1] int_req[1]<br>O1_DFF[1] 18 force[2] dma_req[1]<br>O2_DFF[1] force[3]<br>19 To MUX....<br>O3_DFF[1]<br>20<br>O0_DFF[2] 21 l0_DFF[2] LC2 O0_DFF[2]<br>O1_DFF[2] 22 l1_DFF[2] O1_DFF[2]<br>O2_DFF[2] l2_DFF[2] O2_DFF[2]<br>23<br>O3_DFF[2] 24 l3_DFF[2] O3_DFF[2]<br>To I/O Pads<br>sync[0] sync[0]<br>O0[2]<br>sync[1] sync[1]<br>O1[2]<br>sync[2] sync[2]<br>O2[2]<br>sync[3] sync[3]<br>O3[2]<br>force[0] force[0]<br>force[1] force[1]<br>int_req[2]<br>force[2] force[2]<br>dma_req[2]<br>force[3] force[3]<br><!-- End of picture text -->

Figure 254. Block diagram 

## 60.5 LC operation 

### 60.5.1 Overview 

An LC performs logic operations based on the LUT principle, as described in Logic operations. Each LC supports the following features: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2099 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

- Independent filter thresholds for the rising and falling output states support different transition delays. 

- Bypass of the output state filter by setting the filter threshold to zero. Bypassing the filter causes the aynchronous signal to propagate to the output of the LC. 

- Force logic that instantly switches an LC output to the inactive state upon external fault signal assertion. The return from the inactive state to the output state is either: 

   - Instantaneous: when LCU deasserts the force signal. 

   - Instantaneous synchronized: when LCU deasserts the force signal and then the sync input asserts. 

   - Manual: when you write 1 to the force status bit and then the LCU deasserts the force input. 

   - Manual synchronized: when you write 1 to the force status bit and LCU deasserts the force input, and then the sync input asserts. 

- Input software override logic to override external inputs by writing to the following registers: 

   - LCn Sync Control (LCn_SCTRL[SW_MODE]) 

   - Software Override Value (SWVALUE[SWVALUE]) 

   - Software Override Enable (SWEN[SWEN]) 

- Generation of interrupt requests or DMA transfer requests. 

### 60.5.2 LC diagram 

This figure illustrates an example LC implementation with: 

- One LC 

- Four force inputs 

- Four sync inputs 

For the number of each resource in this chip, see Feature list. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2100 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2101-01.png)


<!-- Start of picture text -->
Logic Control Unit (LCU)<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2101-02.png)


<!-- Start of picture text -->
LCU<br>O0_DFF[0]<br>O0_DFF[0] LC0 O1_DFF[0]<br>Q Lcu_clock O2_DFF[0]<br>l0l1l2 Lcu_clock QQ QQ 0 1023 MU I0_DFF[0]I1_DFF[0]I2_DFF[0] Q 0 O3_DFF[0]<br>l3 45 XSEL I3_DFF[0] SWOUT[0] LCO_OUTPOL[0]1 O0[0]O1O2[[00]]<br>0<br>6 LC_INPUTS[0] 0 O3[0]<br>7 LUT Rise and fall LCOUT[0]<br>8 0 0 1 block edge delay<br>0 OUTEN[0]<br>MUXSEL0[MUXSEL] 1 1 SWEN[0] LC0_FILT0[LUT_RISE_FILT]<br>LC0_FILT0[LUT_FALL_FILT]<br>1<br>SWVALUE[0] Q Q LC0_LUTCTRL0[LUTCTRL]<br>LC0_SCTRL[SW_MODE]<br>0 Q Q<br>1<br>2<br>3<br>LC0_SCTRL[SW_SYNC_SEL] Software override<br>sync[0]<br>sync[1]<br>sync[2]<br>sync[3] 0 0 1<br>To other LCs 1 1 0 1<br>1<br>LC0STS[FORCESTS[0]] 2<br>01 Q 3<br>23 Q Q LC0_FCTRL[FORCE_MODE0]<br>LC0_FCTRL[SYNC_SEL0] Q<br>Force deassertion<br>0 0<br>1<br>0 1<br>force[0] 1 Lcu_clock Q Rise and falledge delay 0 LC0_FCTRL[FORCE_SENSE0[0]]<br>force[1] Q<br>LC0_FFILT[COMB_EN[0]]<br>force[2] LC0_FFILT[FORCE_POL[0]] LC0_FFILT[FORCE_FILT]<br>force[3] Force assertion<br>To other LCs 0 0 0 0<br>FORCEOUT[0] 1 FORCEOUT[0] 1<br>int_req[0]<br>LC0_INTDMAEN[FORCE_DMA_EN[0]] LC0_INTDMAEN[FORCE_INT_EN[0]]<br>0 0 0 0<br>LCOUT[0] 1 LCOUT[0] 1<br>Lcu_clock<br>LC0_INTDMAEN[LUT_DMA_EN[0]] LC0_INTDMAEN[LUT_INT_EN[0]]<br>dma_req[0]<br>To other LCs DMA and interrupt control<br>Figure 255. LC diagram<br>FORCEOUT[0]<br><!-- End of picture text -->

### 60.5.3 Logic operations 

An LC reads its set of inputs (inputs 3, 2, 1, and 0) as a four-bit binary value, with Input 3 as the most-significant bit and Input 0 as the least-significant bit. For example, if: 

Input 0 = 0 Input 1 = 1 Input 2 = 0 Input 3 = 1 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2101 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

then the combined input value is 1010b (10 decimal). 

Each possible four-bit input value corresponds to a bit position in the LUT Control (LCn_LUTCTRLm[LUTCTRL]), as illustrated in LC LUT. For a given LC output, if the combined LC input value corresponds to a bit position in that output's LUTCTRL value that equals 1, then the LC asserts that output. 

For example, if you write 35h to LUTCTRL (shown in the Example column of the LC LUT), then the combined input values 0 (0000b), 2 (0010b), 4 (0100b), and 5 (0101b) cause assertion of the output. All other input values cause deassertion of the output. LCU processes each look-up table asynchronously. 

### 60.5.4 LC LUT 

The LUT maps the combined LC input value to a bit position in LCn_LUTCTRLm. 

Table 297. LC LUT 

|Input 3|Input 2|Input 1|Input 0|LUTCTRL bit position|Example LUTCTRL value:<br>35h|
|---|---|---|---|---|---|
|0|0|0|0|0|1|
|0|0|0|1|1|0|
|0|0|1|0|2|1|
|0|0|1|1|3|0|
|0|1|0|0|4|1|
|0|1|0|1|5|1|
|0|1|1|0|6|0|
|0|1|1|1|7|0|
|1|0|0|0|8|0|
|1|0|0|1|9|0|
|1|0|1|0|10|0|
|1|0|1|1|11|0|
|1|1|0|0|12|0|
|1|1|0|1|13|0|
|1|1|1|0|14|0|
|1|1|1|1|15|0|



### 60.5.5 LC output filters 

Each LC supports two optional digital filters, a Rise Filter (LCn_FLITm[LUT_RISE_FILT]) and a Fall Filter (LCn_FLITm[LUT_FALL_FILT]), to post-process the LUT output and delay the output signal change. 

Each filter starts accumulating clock cycles on the occurrence of the associated LUT event. The Rise Filter counts from an output assertion, and the Fall Filter counts from an output deassertion. When the number of clock cycles reaches the filter threshold (matches the specified filter value), the output flips to the new state. For example, if you specify a Rise Filter value of 100h, and the LUT event triggers an output assertion, the output signal does not assert until the 256th clock cycle after the event. 

A filter value of 0 bypasses the filter. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2102 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

## 60.6 Behavior in different chip modes of operation 

|Operation mode|Status of outputs|
|---|---|
|Normal|• Controlled byLCn_LUTCTRLmandMUXSELn|
||• Toggled based on the states of the selected inputs|
|Debug|Inactive or normal operation controlled by Debug Mode<br>Enable (DBGEN)|



## 60.7 Use-case examples 

### 60.7.1 Two-channel multiplexer 

#### 60.7.1.1 Overview 

A multiplexer (or mux) takes multiple inputs and, based on some control mechanism, passes only one of those inputs to the output. You can implement a two-channel multiplexer controlled by an external signal or a software override using three inputs and one output of a single LC, as illustrated in Logic diagram and Implementation. 

This example implementation controls the multiplexer with the SEL input signal and a software override. The software override controls the multiplexer output regardless of the SEL signal state. To use software override, you must enable it for the corresponding output (SWEN[SWEN]). You assert software override by writing 1 to the corresponding bit of the Software Override Value (SWVALUE[SWVALUE]). 

#### 60.7.1.2 Logic diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2103-10.png)


<!-- Start of picture text -->
A<br>SEL<br>Y<br>SEL<br>B<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2103-11.png)


<!-- Start of picture text -->
Figure 256. Logic diagram<br><!-- End of picture text -->

#### 60.7.1.3 Implementation 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2103-13.png)


<!-- Start of picture text -->
SEL<br>I0<br>A Y<br>I1 LC0 O0<br>B<br>I2<br>OUTEN SWVALUE<br>SWEN<br>Path delays: 2 clocks FILTx clocks<br>Figure 257. Implementation<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2103 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

#### 60.7.1.4 Connections and controls 

Table 298. Connections and controls 

|Name|Description|
|---|---|
|SEL|Input signal|
|A||
|B||
|OUTEN|Output enable|
|SWEN|Software override enable|
|SWVALUE|Software override|
|Y|Output signal|



#### 60.7.1.5 Truth table 

Table 299. Truth table 

||Inputs|||Output|
|---|---|---|---|---|
|A|B|SEL|Y||
|0|0|0|0||
|0|0|1|0||
|1|0|0|1||
|1|0|1|0||
|0|1|0|0||
|0|1|1|1||
|1|1|0|1||
|1|1|1|1||



#### 60.7.1.6 Register configuration 

Table 300. Register configuration 

|Register|I3|I2|I1|I0|O0|O1|O2|O3|
|---|---|---|---|---|---|---|---|---|
|LUTCTRL0|—|—|—|—|E4E4h|—|—|—|
|LUTCTRL1|—|—|—|—|—|0h|—|—|
|LUTCTRL2|—|—|—|—|—|—|0h|—|
|LUTCTRL3|—|—|—|—|—|—|—|0h|
|FILT0|—|—|—|—|0h|—|—|—|
|FILT1|—|—|—|—|—|0h|—|—|
|FILT2|—|—|—|—|—|—|0h|—|
|FILT3|—|—|—|—|—|—|—|0h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2104 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

Table 300. Register configuration (continued) 

|Register|I3|I2|I1|I0|O0|O1|O2|O3|
|---|---|---|---|---|---|---|---|---|
|INTDMAEN|—|—|—|—|0h||||
|OUTPOL|—|—|—|—|0h||||
|FFILT|—|—|—|—|0h||||
|FCTRL|—|—|—|—|0h||||
|SCTRL|—|—|—|—|0h||||
|MUXSEL0|—|—|—|1h|—|—|—|—|
|MUXSEL1|—|—|2h|—|—|—|—|—|
|MUXSEL2|—|3h|—|—|—|—|—|—|
|MUXSEL3|0h|—|—|—|—|—|—|—|
|SWEN|—|—|—|—|Disable<br>Enable s|software ove<br>oftware over|rride for LC0<br>ride for LC0 i|input 0: 0h<br>nput 0: 1h|
|SWVALUE|—|—|—|—|Deasser<br>Assert s|t software ov<br>oftware overr|erride for LC<br>ide for LC0 in|0 input 0: 0h<br>put 0: 1h|
|OUTEN|—|—|—|—|1h||||



#### 60.7.1.7 Waveforms 

In this figure, the SWEN and SWVALUE signals represent the states of the software override control registers. Writes to SWEN and SWVALUE have immediate impact on LC outputs, whereas LC inputs require input synchronization to prevent metastability. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2105-06.png)


<!-- Start of picture text -->
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37<br>System clock<br>A<br>B<br>Sel<br>SWEN<br>SWVALUE<br>Y<br>OUTEN<br>Figure 258. Waveforms<br><!-- End of picture text -->

### 60.7.2 Binary to Gray code converter 

#### 60.7.2.1 Overview 

Gray code, also known as reflected binary code (RBC), is a non-weighted, minimum change code. In this code, any two adjacent code numbers differ by only one bit. This code solves the problem of physical switch transitions by changing only one switch at a time, so there is never any ambiguity of position. 

You can implement binary to Gray code conversion using a single LC, as illustrated in Logic diagram and Implementation. 

In this example, the LC also generates a DMA request on each rising edge of output 3, which is bit 0 of the Gray code (G0). 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2105 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

#### 60.7.2.2 Conversion table 

Table 301. Conversion table 

|Decimal|Binary|Gray|
|---|---|---|
|0|0000|0000|
|1|0001|0001|
|2|0010|0011|
|3|0011|0010|
|4|0100|0110|
|5|0101|0111|
|6|0110|0101|
|7|0111|0100|
|8|1000|1100|
|9|1001|1101|
|10|1010|1111|
|11|1011|1110|
|12|1100|1010|
|13|1101|1011|
|14|1110|1001|
|15|1111|1000|



#### 60.7.2.3 Logic diagram 

|B0<br>B1|G0|
|---|---|
|B1<br>B2|G1|
|B2<br>B3<br>B3|G2<br>G3|



Figure 259. Logic diagram 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2106 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

#### 60.7.2.4 Implementation 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2107-03.png)


<!-- Start of picture text -->
B0 G3<br>I0 O0<br>B1 G2<br>I1 O1<br>B2 LC0 G1<br>I2 O2<br>B3 G0<br>I3 O3<br>Clock<br>Path delays: 2 clocks FILTx clocks<br>Figure 260. Implementation<br><!-- End of picture text -->

#### 60.7.2.5 Connections and controls 

Table 302. Connections and controls 

|Name|Description|
|---|---|
|B0|Bit 0 of the input binary code|
|B1|Bit 1 of the input binary code|
|B2|Bit 2 of the input binary code|
|B3|Bit 3 of the input binary code|
|G0|Bit 0 of the output Gray code|
|G1|Bit 1 of the output Gray code|
|G2|Bit 2 of the output Gray code|
|G3|Bit 3 of the output Gray code|
|Clock|System clock input|



#### 60.7.2.6 Truth table 

Table 303. Truth table 

|||Inputs||||Outputs||
|---|---|---|---|---|---|---|---|
|B3|B2|B1|B0|G3|G2|G1|G0|
|0|0|0|0|0|0|0|0|
|0|0|0|1|0|0|0|1|
|0|0|1|0|0|0|1|1|
|0|0|1|1|0|0|1|0|
|0|1|0|0|0|1|1|0|
|0|1|0|1|0|1|1|1|
|0|1|1|0|0|1|0|1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2107 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

##### Table 303. Truth table (continued) 

|||Inputs||||Outputs||
|---|---|---|---|---|---|---|---|
|B3|B2|B1|B0|G3|G2|G1|G0|
|0|1|1|1|0|1|0|0|
|1|0|0|0|1|1|0|0|
|1|0|0|1|1|1|0|1|
|1|0|1|0|1|1|1|1|
|1|0|1|1|1|1|1|0|
|1|1|0|0|1|0|1|0|
|1|1|0|1|1|0|1|1|
|1|1|1|0|1|0|0|1|
|1|1|1|1|1|0|0|0|



#### 60.7.2.7 Register configuration 

Table 304. Register configuration 

|Register|I3|I2|I1|I0|O0|O1|O2|O3|
|---|---|---|---|---|---|---|---|---|
|LUTCTRL0|—|—|—|—|FF00h|—|—|—|
|LUTCTRL1|—|—|—|—|—|FF0h|—|—|
|LUTCTRL2|—|—|—|—|—|—|3C3Ch|—|
|LUTCTRL3|—|—|—|—|—|—|—|6666h|
|FILT0|—|—|—|—|0h|—|—|—|
|FILT1|—|—|—|—|—|0h|—|—|
|FILT2|—|—|—|—|—|—|0h|—|
|FILT3|—|—|—|—|—|—|—|0h|
|INTDMAEN|—|—|—|—|800h||||
|OUTPOL|—|—|—|—|0h||||
|FFILT|—|—|—|—|0h||||
|FCTRL|—|—|—|—|0h||||
|SCTRL|—|—|—|—|0h||||
|MUXSEL0h|—|—|—|01h|—|—|—|—|
|MUXSEL1|—|—|2h|—|—|—|—|—|
|MUXSEL2|—|3h|—|—|—|—|—|—|
|MUXSEL3|4h|—|—|—|—|—|—|—|
|SWEN|—|—|—|—|0h||||
|SWVALUE|—|—|—|—|0h||||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2108 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

Table 304. Register configuration (continued) 

|Register|I3|I2|I1|I0|O0|O1|O2|O3|
|---|---|---|---|---|---|---|---|---|
|OUTEN|—|—|—|—|Fh||||



#### 60.7.2.8 Waveforms 

The LC outputs are delayed by two clock cycles because of the two-stage input synchronizers. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2109-06.png)


<!-- Start of picture text -->
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49<br>System clock<br>B3<br>B2<br>B1<br>B0<br>G3<br>G2<br>G1<br>G0<br>DMA request<br>OUTEN 0h Fh<br>Figure 261. Waveforms<br>Binary code<br>Gray code<br><!-- End of picture text -->

### 60.7.3 Manchester encoder and decoder 

#### 60.7.3.1 Overview 

Manchester encoding (also known as phase encoding) is a data-modulation technique for binary data transfer based one of these signals: 

- Analog 

- RF 

- Optical 

- High-speed-digital 

- Long-distance-digital 

The fundamental idea behind Manchester encoding is to use voltage transitions, instead of voltage levels, to represent 1s and 0s. It performs an exclusive OR of data and clock signals to encode and decode data. A high-to-low transition on the falling clock edge indicates 0. A low-to-high transition on the rising clock edge indicates 1. 

#### 60.7.3.2 Logic diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2109-17.png)


<!-- Start of picture text -->
Clock<br>PE<br>Data<br>Clock<br>Data<br>PE<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2109-18.png)


<!-- Start of picture text -->
Figure 262. Logic diagram<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2109 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

#### 60.7.3.3 Implementation 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2110-03.png)


<!-- Start of picture text -->
Data in PE<br>I0 O0<br>Encoder<br>Clock in Clock<br>I1 O1<br>LC0<br>Data out<br>I2 O2<br>Decoder<br>Clock out<br>I3 O3<br>System clock<br>Path delays: 2 clocks FILTx+1 clock FILTx clocks<br>Figure 263. Implementation<br><!-- End of picture text -->

#### 60.7.3.4 Connections and controls 

Table 305. Connections and controls 

|Name|Description|
|---|---|
|Data in|Input signal|
|Clock in||
|PE|Manchester-encoded signal from LC|
|Clock|Auxiliary signal fed to the decoder to allow Manchester decoding|
|Data out|Output signal after Manchester decoding|
|System clock|Clock frequency supplied to LC|
|Clock out|Output signal|



#### 60.7.3.5 Truth table for encoder 

Table 306. Truth table for encoder 

||Inputs|Output|
|---|---|---|
|Data in|Clock in|PE|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2110 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

#### 60.7.3.6 Truth table for decoder 

Table 307. Truth table for decoder 

||Inputs|Output|
|---|---|---|
|Clock|PE|Data out|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|0|



#### 60.7.3.7 Register configuration 

Table 308. Register configuration 

|Register|I3|I2|I1|I0|O0|O1|O2|O3|
|---|---|---|---|---|---|---|---|---|
|LUTCTRL0|—|—|—|—|6666h|—|—|—|
|LUTCTRL1|—|—|—|—|—|AAAAh|—|—|
|LUTCTRL2|—|—|—|—|—|—|FF0h|—|
|LUTCTRL3|—|—|—|—|—|—|—|FF00h|
|FILT0|—|—|—|—|0h|—|—|—|
|FILT1|—|—|—|—|—|0h|—|—|
|FILT2|—|—|—|—|—|—|0h|—|
|FILT3|—|—|—|—|—|—|—|0h|
|INTDMAEN|—|—|—|—|0h||||
|OUTPOL|—|—|—|—|0h||||
|FFILT|—|—|—|—|0h||||
|FCTRL|—|—|—|—|0h||||
|SCTRL|—|—|—|—|0h||||
|MUXSEL0|—|—|—|1h|—|—|—|—|
|MUXSEL1|—|—|2h|—|—|—|—|—|
|MUXSEL2|—|5h|—|—|—|—|—|—|
|MUXSEL3|6h|—|—|—|—|—|—|—|
|SWEN|—|—|—|—|0h||||
|SWVALUE|—|—|—|—|0h||||
|OUTEN|—|—|—|—|Fh||||



#### 60.7.3.8 Waveforms for encoder 

This figure includes the Manchester-encoded waveform (labeled PE) of the input waveform (labeled "Data in"). The PE waveform is delayed by two clock cycles because of two-stage input synchronization. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2111 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2112-02.png)


<!-- Start of picture text -->
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28<br>System clock<br>Clock in<br>Data in<br>PE<br>Clock<br>OUTEN 0h Fh<br><!-- End of picture text -->

Figure 264. Waveforms for encoder 

#### 60.7.3.9 Waveforms for decoder 

The output waveform (labeled "Data out") is delayed by four clock cycles from the input waveform (labeled "Data in") because of two-stage input synchronization. In this example, the Manchester encoder also propagates the Clock waveform that the decoder uses to reconstruct the "Data in" waveform from the Manchester-decoded waveform (labeled PE). 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2112-06.png)


<!-- Start of picture text -->
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28<br>System clock<br>PE<br>Clock<br>Data out<br>Clock out<br>OUTEN 0h Fh<br><!-- End of picture text -->

Figure 265. Waveforms for decoder 

### 60.7.4 Adjustable PWM/FM generator 

#### 60.7.4.1 Overview 

In many cases, it is useful to route an LC output back to one of its inputs, as illustrated in Implementation. In addition, you can delay outputs with a digital filter with different time constants for delaying rising and falling edges. Combining these capabilities, you can use an LC to generate output waveforms with adjustable pulse width and frequency. 

In addition to waveform generation, the software-override feature forces the generator output low or high by software. You control the override via Software Override Enable (SWEN) and Software Override Value (SWVALUE). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2112 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

#### 60.7.4.2 Implementation 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2113-03.png)


<!-- Start of picture text -->
OUT<br>I0 LC0 O0<br>System clock<br>SYNC<br>Path delays: FILTx+1 clock FILTx clocks<br>Figure 266. Implementation<br><!-- End of picture text -->

#### 60.7.4.3 Connections and controls 

Table 309. Connections and controls 

|Name|Description|
|---|---|
|I0|Delayed output routed back to LC input|
|O0 and OUT|Delayed output|
|System clock|Clock frequency supplied to LC|
|SYNC|Software override synchronization signal|



#### 60.7.4.4 Truth table 

This example generates an adjustable PWM/FM waveform according to the following table. In the table: 

- OUT is the LC output signal that is also routed to the LC input using an internal multiplexer. 

- TdH is the digital filter value to delay the rising edge of the output signal. 

- TdL is the digital filter value to delay the falling edge of the output signal. 

##### Table 310. Truth table 

|I0|OUT|
|---|---|
|0|1 delayed by TdH (seeOutput edge delays)|
|1|0 delayed by TdL (seeOutput edge delays)|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2113 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

#### 60.7.4.5 Output edge delays 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2114-03.png)


<!-- Start of picture text -->
I0<br>OUT<br>TdH TdL<br><!-- End of picture text -->

Figure 267. Output edge delays 

#### 60.7.4.6 Register configuration 

Table 311. Register configuration 

|Register|I3|I2|I1|I0|O0|O1|O2|O3|
|---|---|---|---|---|---|---|---|---|
|LUTCTRL0|—|—|—|—|1h|—|—|—|
|LUTCTRL1|—|—|—|—|—|0h|—|—|
|LUTCTRL2|—|—|—|—|—|—|0h|—|
|LUTCTRL3|—|—|—|—|—|—|—|0h|
|FILT0|—|—|—|—|1_0001h|—|—|—|
|FILT1|—|—|—|—|—|0h|—|—|
|FILT2|—|—|—|—|—|—|0h|—|
|FILT3|—|—|—|—|—|—|—|0h|
|INTDMAEN|—|—|—|—|0h||||
|OUTPOL|—|—|—|—|0h||||
|FFILT|—|—|—|—|0h||||
|FCTRL|—|—|—|—|0h||||
|SCTRL|—|—|—|—|SWVALUE<br>SWVALUE<br>sync: 1h|for input 0<br>for input 0|changes imm<br>changes on r|ediately: 0h<br>ising edge of|
|MUXSEL0|—|—|—|5h|—|—|—|—|
|MUXSEL1|—|—|0h|—|—|—|—|—|
|MUXSEL2|—|0h|—|—|—|—|—|—|
|MUXSEL3|0h|—|—|—|—|—|—|—|
|SWEN|—|—|—|—|Disable sof<br>Enable soft|tware over<br>ware overr|ride: 0h<br>ide: 1h||
|SWVALUE|—|—|—|—|Deassert s|oftware ov|erride: 0h||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2114 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

Table 311. Register configuration (continued) 

|Register|I3|I2|I1|I0|O0<br>O1<br>O2|O3|
|---|---|---|---|---|---|---|
||||||Assert software override: 1h||
|OUTEN|—|—|—|—|1h||



#### 60.7.4.7 Waveforms for immediate software override 

In this figure, the SWEN and SWVALUE signals represent the states of the software override control registers. Writes to Software Override Enable (SWEN) and Software Override Value (SWVALUE) have immediate impact on LC outputs, whereas LC inputs require input synchronization to prevent metastability. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2115-06.png)


<!-- Start of picture text -->
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51<br>System clock<br>LUT_RISE_FILT 1h<br>LUT_FALL_FILT 1h 3h<br>SWEN<br>SWVALUE<br>OUTEN<br>SYNC<br>OUT<br><!-- End of picture text -->

Figure 268. Waveforms for immediate software override 

#### 60.7.4.8 Waveforms for synced software override 

In this example, software override control is synced with the rising edges of the SYNC waveform. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2115-10.png)


<!-- Start of picture text -->
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51<br>System clock<br>LUT_RISE_FILT 1h<br>LUT_FALL_FILT 1h 3h<br>SWEN<br>SWVALUE<br>OUTEN<br>SYNC<br>OUT<br><!-- End of picture text -->

Figure 269. Waveforms for synced software override 

### 60.7.5 SR latch 

#### 60.7.5.1 Overview 

An SR latch is the simplest bistable device and a fundamental component of data storage. 

This example implementation uses one LC that includes an internal feedback path configured by the internal multiplexer, as illustrated in Implementation. Output Q responds to inputs S (set) and R (reset). It changes with a delay of two clock cycles—the time required for the S and R signal inputs to pass through the internal two-stage synchronizers. This example implementation bypasses the Q digital filter; therefore, the loop of Q back to the input experiences a delay of one clock cycle." See Waveforms. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2115 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

#### 60.7.5.2 Implementation 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2116-03.png)


<!-- Start of picture text -->
I0<br>S Q<br>I1 LC0 O0<br>R<br>I2<br>System clock<br>Path delays: 2 clocks FILTx+1 clock FILTx clocks<br>Figure 270. Implementation<br><!-- End of picture text -->

#### 60.7.5.3 Connections and controls 

Table 312. Connections and controls 

|Name|Description|
|---|---|
|S|Set input|
|R|Reset input|
|Q|Both an output signal and an input that feeds back to LC0|
|System clock|Clock frequency supplied to LC|



#### 60.7.5.4 Truth table 

Table 313. Truth table 

||Inputs||Output|State|
|---|---|---|---|---|
|R|S|Q|Q||
|0|0|0|0|Latch|
|0|0|1|1|Latch|
|0|1|0|1|Set|
|0|1|1|1|Set|
|1|0|0|0|Reset|
|1|0|1|0|Reset|
|1|1|0|0|Not allowed|
|1|1|1|0||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2116 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

#### 60.7.5.5 Register configuration 

Table 314. Register configuration 

|Register|I3|I2|I1|I0|O0|O1|O2|O3|
|---|---|---|---|---|---|---|---|---|
|LUTCTRL0|—|—|—|—|1h|—|—|—|
|LUTCTRL1|—|—|—|—|—|0h|—|—|
|LUTCTRL2|—|—|—|—|—|—|0h|—|
|LUTCTRL3|—|—|—|—|—|—|—|0h|
|FILT0|—|—|—|—|0h|—|—|—|
|FILT1|—|—|—|—|—|0h|—|—|
|FILT2|—|—|—|—|—|—|0h|—|
|FILT3|—|—|—|—|—|—|—|0h|
|INTDMAEN|—|—|—|—|0h||||
|OUTPOL|—|—|—|—|0h||||
|FFILT|—|—|—|—|0h||||
|FCTRL|—|—|—|—|0h||||
|SCTRL|—|—|—|—|0h||||
|MUXSEL0|—|—|—|5h|—|—|—|—|
|MUXSEL1|—|—|2h|—|—|—|—|—|
|MUXSEL2|—|3h|—|—|—|—|—|—|
|MUXSEL3|0h|—|—|—|—|—|—|—|
|SWEN|—|—|—|—|0h||||
|SWVALUE|—|—|—|—|0h||||
|OUTEN|—|—|—|—|1h||||



#### 60.7.5.6 Waveforms 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2117-06.png)


<!-- Start of picture text -->
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29<br>System clock<br>S<br>R<br>Q<br>OUTEN 1h<br>Figure 271. Waveforms<br><!-- End of picture text -->

### 60.7.6 D flip-flop 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2117 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

#### 60.7.6.1 Overview 

A D flip-flop stores and outputs whatever logic level is applied to its data terminal at the time its clock input goes high. 

You can implement a D flip-flop element using an LC as illustrated in Implementation. On a clock rising edge, the LC either asserts or deasserts the Q output based on the D input. 

The Q output and CLKO digital filters are bypassed. Therefore, the states of these variables are fed to inputs with a delay of one clock cycle. See Waveforms. 

#### 60.7.6.2 Implementation 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2118-07.png)


<!-- Start of picture text -->
D Q<br>I0 O0<br>CLK CLKO<br>I1 O1<br>LC0<br>I2 O2<br>I3 O3<br>System clock<br>Path delays: 2 clocks FILTx+1 clock FILTx clocks<br>Figure 272. Implementation<br><!-- End of picture text -->

#### 60.7.6.3 Connections and controls 

Table 315. Connections and controls 

|Name|Description|
|---|---|
|D|Input signal|
|CLK|Input clock|
|Q|Output signal; holds the logic state of the last Q output|
|CLKO|Holds the logic state of the last CLK input|



#### 60.7.6.4 Truth table 

Table 316. Truth table 

|||Inputs|||Outputs|State|
|---|---|---|---|---|---|---|
|CLKO|Q|CLK|D|Q|CLKO||
|0|0|0|0|0|0|Hold|
|0|0|0|1|0|0|Hold|
|0|0|1|0|0|1|Reset|
|0|0|1|1|1|1|Set|
|0|1|0|0|1|0|Hold|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2118 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

Table 316. Truth table (continued) 

|||Inputs|||Outputs|State|
|---|---|---|---|---|---|---|
|CLKO|Q|CLK|D|Q|CLKO||
|0|1|0|1|1|0|Hold|
|0|1|1|0|0|1|Reset|
|0|1|1|1|1|1|Set|
|1|0|0|0|0|0|Hold|
|1|0|0|1|0|0|Hold|
|1|0|1|0|0|1|Hold|
|1|0|1|1|0|1|Hold|
|1|1|0|0|1|0|Hold|
|1|1|0|1|1|0|Hold|
|1|1|1|0|1|1|Hold|
|1|1|1|1|1|1|Hold|



#### 60.7.6.5 Register configuration 

Table 317. Register configuration 

|Register|I3|I2|I1|I0|O0|O1|O2|O3|
|---|---|---|---|---|---|---|---|---|
|LUTCTRL0|—|—|—|—|F0B8h|—|—|—|
|LUTCTRL1|—|—|—|—|—|CCCCh|—|—|
|LUTCTRL2|—|—|—|—|—|—|0h|—|
|LUTCTRL3|—|—|—|—|—|—|—|0h|
|FILT0|—|—|—|—|0h|—|—|—|
|FILT1|—|—|—|—|—|0h|—|—|
|FILT2|—|—|—|—|—|—|0h|—|
|FILT3|—|—|—|—|—|—|—|0h|
|INTDMAEN|—|—|—|—|0h||||
|OUTPOL|—|—|—|—|0h||||
|FFILT|—|—|—|—|0h||||
|FCTRL|—|—|—|—|0h||||
|SCTRL|—|—|—|—|0h||||
|MUXSEL0|—|—|—|1h|—|—|—|—|
|MUXSEL1|—|—|2h|—|—|—|—|—|
|MUXSEL2|—|5h|—|—|—|—|—|—|
|MUXSEL3|6h|—|—|—|—|—|—|—|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2119 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

Table 317. Register configuration (continued) 

|Register|I3|I2|I1|I0|O0|O1|O2|O3|
|---|---|---|---|---|---|---|---|---|
|SWEN|—|—|—|—|0h||||
|SWVALUE|—|—|—|—|0h||||
|OUTEN|—|—|—|—|3h||||



#### 60.7.6.6 Waveforms 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2120-05.png)


<!-- Start of picture text -->
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35<br>System clock<br>D<br>CLK<br>Q<br>OUTEN 3h<br><!-- End of picture text -->

Figure 273. Waveforms 

### 60.7.7 JK flip-flop 

#### 60.7.7.1 Overview 

A JK flip-flop is a gated SR latch (see SR latch) with an added clock input circuit that prevents the illegal or invalid output condition that can occur when both SR-latch inputs (S and R) are asserted. 

Truth table for JK flip-flop presents the four possible input combinations for a JK flip-flop. All output changes occur at the clock rising edge. 

You can create a JK flip-flop using two LCs, as illustrated in Implementation. The first LC detects rising edges of the CLK clock input (see Truth table for LC0). The second LC processes J and K inputs at every rising clock edge (see Truth table for LC1). 

Output Q and CLKO digital filters are bypassed. Therefore, the states of these variables are fed to inputs with a delay of one clock cycle (see Waveforms). 

#### 60.7.7.2 Implementation 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2120-14.png)


<!-- Start of picture text -->
CLK CLK0 J Q<br>I0 O0 I0 O0<br>EDGE K<br>I1 O1 I1 O1<br>LC0 LC1<br>I2 O2 I2 O2<br>I3 O3 I3 O3<br>System clock<br>Path delays: 2 clocks FILTx+1 clock FILTx clocks<br><!-- End of picture text -->

Figure 274. Implementation 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2120 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

#### 60.7.7.3 Truth table for JK flip-flop 

Table 318. Truth table for JK flip-flop 

|J|K|State|
|---|---|---|
|0|0|Hold|
|1|0|Set|
|0|1|Clear|
|1|1|Toggle|



#### 60.7.7.4 Truth table for LC0 

Table 319. Truth table for LC0 

||Inputs||Outputs|State|
|---|---|---|---|---|
|CLKO|CLK|CLKO|EDGE||
|0|0|0|0|No edge|
|0|1|1|1|Edge detected|
|1|0|0|0|No edge|
|1|1|1|0|No edge|



#### 60.7.7.5 Truth table for LC1 

Table 320. Truth table for LC1 

|||Inputs||Output|State|
|---|---|---|---|---|---|
|EDGE|Q|J|K|Q||
|0|0|X|X|0|Hold|
|0|1|X|X|1|Hold|
|1|0|0|0|0|Hold|
|1|1|0|0|1|Hold|
|1|X|1|0|1|Set|
|1|X|0|1|0|Clear|
|1|0|1|1|1|Toggle|
|1|1|1|1|0|Toggle|



#### 60.7.7.6 Register configuration for LC0 

Table 321. Register configuration for LC0 

|Register|I3|I2|I1|I0|O0|O1|O2|O3|
|---|---|---|---|---|---|---|---|---|
|LUTCTRL0|—|—|—|—|Ah|—|—|—|
|LUTCTRL1|—|—|—|—|—|2h|—|—|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2121 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

Table 321. Register configuration for LC0 (continued) 

|Register|I3|I2|I1|I0|O0|O1|O2|O3|
|---|---|---|---|---|---|---|---|---|
|LUTCTRL2|—|—|—|—|—|—|0h|—|
|LUTCTRL3|—|—|—|—|—|—|—|0h|
|FILT0|—|—|—|—|0h|—|—|—|
|FILT1|—|—|—|—|—|0h|—|—|
|FILT2|—|—|—|—|—|—|0h|—|
|FILT3|—|—|—|—|—|—|—|0h|
|INTDMAEN|—|—|—|—|0h||||
|OUTPOL|—|—|—|—|0h||||
|FFILT|—|—|—|—|0h||||
|FCTRL|—|—|—|—|0h||||
|SCTRL|—|—|—|—|0h||||
|MUXSEL0|—|—|—|1h|—|—|—|—|
|MUXSEL1|—|—|9h|—|—|—|—|—|
|MUXSEL2|—|0h|—|—|—|—|—|—|
|MUXSEL3|0h|—|—|—|—|—|—|—|
|SWEN|—|—|—|—|0h||||
|SWVALUE|—|—|—|—|0h||||
|OUTEN|—|—|—|—|3h||||



#### 60.7.7.7 Register configuration for LC1 

Table 322. Register configuration for LC1 

|Register|I3|I2|I1|I0|O0|O1|O2|O3|
|---|---|---|---|---|---|---|---|---|
|LUTCTRL0|—|—|—|—|3AF0h|—|—|—|
|LUTCTRL1|—|—|—|—|—|0h|—|—|
|LUTCTRL2|—|—|—|—|—|—|0h|—|
|LUTCTRL3|—|—|—|—|—|—|—|0h|
|FILT0|—|—|—|—|0h|—|—|—|
|FILT1|—|—|—|—|—|0h|—|—|
|FILT2|—|—|—|—|—|—|0h|—|
|FILT3|—|—|—|—|—|—|—|0h|
|INTDMAEN|—|—|—|—|0h||||
|OUTPOL|—|—|—|—|0h||||
|FFILT|—|—|—|—|0h||||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2122 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

Table 322. Register configuration for LC1 (continued) 

|Register|I3|I2|I1|I0|O0|O1|O2|O3|
|---|---|---|---|---|---|---|---|---|
|FCTRL|—|—|—|—|0h||||
|SCTRL|—|—|—|—|0h||||
|MUXSEL4|—|—|—|5h|—|—|—|—|
|MUXSEL5|—|—|6h|—|—|—|—|—|
|MUXSEL6|—|Dh|—|—|—|—|—|—|
|MUXSEL7|Ah|—|—|—|—|—|—|—|
|SWEN|—|—|—|—|0h||||
|SWVALUE|—|—|—|—|0h||||
|OUTEN|—|—|—|—|10h||||



#### 60.7.7.8 Waveforms 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2123-05.png)


<!-- Start of picture text -->
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34<br>System clock<br>CLK<br>EDGE<br>J<br>K<br>EDGE<br>Q<br>OUTEN 13h<br>LC0<br>LC1<br><!-- End of picture text -->

Figure 275. Waveforms 

### 60.7.8 Incremental encoder 

#### 60.7.8.1 Overview 

An incremental encoder provides A and B pulse outputs in the form of 90-degree shifted waveforms (see Outputs). The decoding circuit processes these waveforms to detect the rotor position and the direction of rotation. 

This example implementation requires two LCs (see Implementation): 

- LC0 provides pulse streams on CW or CCW output at every A and B signal edge. If the encoder rotation is CW (A signal leading), then pulses appear at the CW output. If the encoder rotation is CCW (B signal leading), then pulses appear at the CCW output. Two pulse counters accumulate these pulse streams to provide the actual absolute encoder position in the respective direction of rotation. 

- LC1 then uses the LC0 outputs to detect the direction of the rotation. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2123 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

#### 60.7.8.2 Outputs 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2124-03.png)


<!-- Start of picture text -->
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20<br>A<br>B<br>DIR CW CCW<br>Figure 276. Outputs<br>60.7.8.3 Implementation<br>A AO<br>I0 O0<br>B  BO<br>I1 O1<br>LC0 CW DIR<br>I2 O2 I0 O0<br>CCW PULSE<br>I3 O3 I1 O1<br>DIR LC1<br>I2 O2<br>I3 O3<br>System clock<br>Path delays: 2 clocks FILTx+1 clock FILTx clocks<br>Figure 277. Implementation<br><!-- End of picture text -->

#### 60.7.8.4 Truth table for pulse generation 

Table 323. Truth table for pulse generation 

|||Inputs||||Outputs||
|---|---|---|---|---|---|---|---|
|BO|AO|B|A|AO|BO|CW|CCW|
|0|0|0|0|0|0|—|—|
|0|0|0|1|1|0|1|—|
|0|0|1|0|0|1|—|1|
|0|0|1|1|1|1|||
|0|1|0|0|0|0|—|1|
|0|1|0|1|1|0|||
|0|1|1|0|0|1|—|—|
|0|1|1|1|1|1|1|—|
|1|0|0|0<br>Table conti|0<br>nues on the nex|0<br>t page...|1||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2124 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

##### Table 323. Truth table for pulse generation (continued) 

|||Inputs||||Outputs||
|---|---|---|---|---|---|---|---|
|BO|AO|B|A|AO|BO|CW|CCW|
|1|0|0|1|1|0|—|—|
|1|0|1|0|0|1|—|—|
|1|0|1|1|1|1|—|1|
|1|1|0|0|0|0|||
|1|1|0|1|1|0|—|1|
|1|1|1|0|0|1|1|—|
|1|1|1|1|1|1|—|—|



#### 60.7.8.5 Truth table for decoding direction of rotation 

In this table: 

- DIR = 0 represents a CCW direction. 

- DIR = 1 represents a CW direction. 

Table 324. Truth table for decoding direction of rotation 

||Inputs||Output|
|---|---|---|---|
|DIR|CCW|CW|DIR|
|0|0|0|0|
|0|0|1|1|
|0|1|0|0|
|0|1|1|1|
|1|0|0|1|
|1|0|1|1|
|1|1|0|0|
|1|1|1|1|



#### 60.7.8.6 Register configuration for LC0 

Table 325. Register configuration for LC0 

|Register|I3|I2|I1|I0|O0|O1|O2|O3|
|---|---|---|---|---|---|---|---|---|
|LUTCTRL0|—|—|—|—|AAAAh|—|—|—|
|LUTCTRL1|—|—|—|—|—|CCCCh|—|—|
|LUTCTRL2|—|—|—|—|—|—|4182h|—|
|LUTCTRL3|—|—|—|—|—|—|—|2814h|
|FILT0|—|—|—|—|1_0001h|—|—|—|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2125 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

Table 325. Register configuration for LC0 (continued) 

|Register|I3|I2|I1|I0|O0|O1|O2|O3|
|---|---|---|---|---|---|---|---|---|
|FILT1|—|—|—|—|—|1_0001h|—|—|
|FILT2|—|—|—|—|—|—|0h|—|
|FILT3|—|—|—|—|—|—|—|0h|
|INTDMAEN|—|—|—|—|0h||||
|OUTPOL|—|—|—|—|0h||||
|FFILT|—|—|—|—|0h||||
|FCTRL|—|—|—|—|0h||||
|SCTRL|—|—|—|—|0h||||
|MUXSEL0|—|—|—|1h|—|—|—|—|
|MUXSEL1|—|—|2h|—|—|—|—|—|
|MUXSEL2|—|9h|—|—|—|—|—|—|
|MUXSEL3|Ah|—|—|—|—|—|—|—|
|SWEN|—|—|—|—|0h||||
|SWVALUE|—|—|—|—|0h||||
|OUTEN|—|—|—|—|Fh||||



#### 60.7.8.7 Register configuration for LC1 

Table 326. Register configuration for LC1 

|Register|I3|I2|I1|I0|O0|O1|O2|O3|
|---|---|---|---|---|---|---|---|---|
|LUTCTRL0|—|—|—|—|BAh|—|—|—|
|LUTCTRL1|—|—|—|—|—|0h|—|—|
|LUTCTRL2|—|—|—|—|—|—|0h|—|
|LUTCTRL3|—|—|—|—|—|—|—|0h|
|FILT0|—|—|—|—|0h|—|—|—|
|FILT1|—|—|—|—|—|0h|—|—|
|FILT2|—|—|—|—|—|—|0h|—|
|FILT3|—|—|—|—|—|—|—|0h|
|INTDMAEN|—|—|—|—|0h||||
|OUTPOL|—|—|—|—|0h||||
|FFILT|—|—|—|—|0h||||
|FCTRL|—|—|—|—|0h||||
|SCTRL|—|—|—|—|0h||||
|MUXSEL4|—|—|—|Bh|—|—|—|—|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2126 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

Table 326. Register configuration for LC1 (continued) 

|Register|I3|I2|I1|I0|O0|O1|O2|O3|
|---|---|---|---|---|---|---|---|---|
|MUXSEL5|—|—|Ch|—|—|—|—|—|
|MUXSEL6|—|Dh|—|—|—|—|—|—|
|MUXSEL7|0h|—|—|—|—|—|—|—|
|SWEN|—|—|—|—|0h||||
|SWVALUE|—|—|—|—|0h||||
|OUTEN|—|—|—|—|10h||||



#### 60.7.8.8 Waveforms 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2127-05.png)


<!-- Start of picture text -->
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57<br>System clock<br>A<br>B<br>CW<br>CCW<br>PULSE<br>DIR CW CCW<br>OUTEN 1Fh<br><!-- End of picture text -->

Figure 278. Waveforms 

### 60.7.9 AC motor PWM controller 

#### 60.7.9.1 Overview 

Driving a three-phase AC motor requires dedicated PWMs to perform: 

- Complementary signal generation 

- Dead time insertion 

- Fault-state assertion 

- Manual or automatic fault recovery 

LCU enhances basic timer functionality with the necessary complementary features available only on dedicated motor control PWMs. 

Implementation for AC motor controller shows all input and output signals of LCU in a typical three-phase motor control application. 

TdH is the time delay preceding each rising edge of the complementary PWM output signals. See Truth table for details. 

Fault signals are routed from analog comparators or external protection circuits to protect power switches against damage caused by overcurrent. Any active fault must immediately change all PWM outputs to the inactive state. Force logic causes PWM outputs to transition to the inactive state upon an external fault event. See Truth table for details. 

The dead time is one clock cycle. On a fault event, both PWM outputs transition to the inactive state (logic 0). When the fault event deasserts, both PWM signals start operating according to FORCE_MODE = 00 (cleared on force deassertion). See Waveforms for force cleared on force deassertion for details. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2127 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

#### 60.7.9.2 Implementation for AC motor controller 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2128-03.png)


<!-- Start of picture text -->
PWMA_T<br>LC0 PWMA_B<br>TMR0<br>PWMB_T<br>TMR1<br>LCU PWMB_B<br>TMR2<br>PWMC_T<br>LC1 PWMC_B<br>System clock SYNC<br>FAULT0 FAULT2<br>FAULT1<br>Path delays: 2 clocks FILTx clocks<br><!-- End of picture text -->

Figure 279. Implementation for AC motor controller 

#### 60.7.9.3 Implementation for controlling one phase of AC motor controller 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2128-06.png)


<!-- Start of picture text -->
PWMA_T<br>O0<br>TMR0<br>I0 LC0<br>PWMA_B<br>O1<br>System clock SYNC<br>FAULT<br>Path delays: 2 clocks FILTx clocks<br><!-- End of picture text -->

Figure 280. Implementation for controlling one phase of AC motor controller 

#### 60.7.9.4 Connections and controls 

Table 327. Connections and controls 

|Name|Description|
|---|---|
|TMRn|Synchronized timer input signals|
|System clock|Clock supplied to the LC|
|FAULTn|Fault signal (seeOverview)|
|SYNC|Sync signal for optional automatic fault recovery|
|PWMx_T|PWM output signal for controlling top power switch|
|PWMx_B|PWM output signal for controlling bottom power switch|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2128 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

#### 60.7.9.5 Truth table 

Table 328. Truth table 

|Input|O|utputs|
|---|---|---|
|TMR0|PWMA_T|PWMB_B|
|0|0|1 delayed by TdH (seeOutput edge delays)|
|1|1 delayed by TdH (seeOutput edge delays)|0|



#### 60.7.9.6 Register configuration 

Table 329. Register configuration 

|Register|I3|I2|I1|I0|O0|O1|O2|O3|
|---|---|---|---|---|---|---|---|---|
|LUTCTRL0|—|—|—|—|2h|—|—|—|
|LUTCTRL1|—|—|—|—|—|1h|—|—|
|LUTCTRL2|—|—|—|—|—|—|0h|—|
|LUTCTRL3|—|—|—|—|—|—|—|0h|
|FILT0|—|—|—|—|1_0000h|—|—|—|
|FILT1|—|—|—|—|—|1_0000h|—|—|
|FILT2|—|—|—|—|—|—|0h|—|
|FILT3|—|—|—|—|—|—|—|0h|
|INTDMAEN|—|—|—|—|0h||||
|OUTPOL|—|—|—|—|0h||||
|FFILT|—|—|—|—|100_0000h||||
|FCTRL|—|—|—|—|0h||||
|SCTRL|—|—|—|—|Software syn<br>immediate fo<br>Software syn|c on rising e<br>r 3 and 1: 10<br>c on rising e|dge for inp<br>1h<br>dge for all f|uts 2 and 0,<br>our inputs: 1111h|
|MUXSEL0|—|—|—|01h|—|—|—|—|
|MUXSEL1|—|—|0h|—|—|—|—|—|
|MUXSEL2|—|0h|—|—|—|—|—|—|
|MUXSEL3|0h|—|—|—|—|—|—|—|
|SWEN|—|—|—|—|0h||||
|SWVALUE|—|—|—|—|0h||||
|OUTEN|—|—|—|—|3h||||



#### 60.7.9.7 Waveforms for force cleared on force deassertion 

This example shows two behaviors, depending on the Force Clearing mode (LC0_FCTRL[FORCE_MODE0]). 

00b - Both PWM signals start normal operation when the fault event deasserts. See Waveforms for force cleared on force deassertion for details. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2129 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

01b - Both PWM signals start normal operation on rising sync after the fault event deasserts. See Waveforms for force cleared on rising sync after force deassertion for details. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2130-03.png)


<!-- Start of picture text -->
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38<br>System clock<br>TMR<br>FAULT<br>SYNC<br>PWM_T<br>PWM_B<br>OUTEN<br><!-- End of picture text -->

Figure 281. Waveforms for force cleared on force deassertion 

#### 60.7.9.8 Waveforms for force cleared on rising sync after force deassertion 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2130-06.png)


<!-- Start of picture text -->
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38<br>System clock<br>TMR<br>FAULT<br>SYNC<br>PWM_T<br>PWM_B<br>OUTEN<br><!-- End of picture text -->

Figure 282. Waveforms for force cleared on rising sync after force deassertion 

### 60.7.10 AC motor double-switching controller 

#### 60.7.10.1 Overview 

The simplest method of obtaining motor winding currents is to measure the current in each phase by placing a shunt resistor in two or three inverter legs (phases). 

This example implementation of an AC motor drive for low-cost and high-volume applications uses a single shunt on the DC bus return path, as illustrated in AC motor power stage schematic. LCU supports double-switching by XORing two timer channel outputs. The implementation uses two LCs arranged to perform double switching, dead time generation, and the processing of three external fault signals. 

#### 60.7.10.2 Double-switching 

The double-switching technique requires: 

- Six synchronized timer pulses 

- Three fault signals 

- Six PWM outputs for controlling top and bottom power switches 

- A sync signal for automatic fault recovery 

Waveforms for double-switching technique example applies the PWM switching cycle to an AC motor to reconstruct currents in three phases using a single DC bus shunt resistor (RSH). It applies the non-zero switching vectors 100, 110, and 101 to the power switches, which sample currents IA[0], -IC[0], -IC[1], and IA[1]. Because the durations (T1) of active vectors 110 and 101 are the same, it also applies the zero switching vector (000) with durations T2 and T3 in the middle of the switching cycle to 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2130 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

allow phase current reconstruction. This technique can only be used by PWM modules targeted at motor control and power conversion applications. 

#### 60.7.10.3 Fault inputs and deadtime insertion 

Fault signals are routed from analog comparators or external protection circuits to protect power switches against damage caused by overcurrent. You must program the Combinational Force Path (LCn_FFILT[COMB_EN]) to enable an active fault input to immediately force all PWM outputs to the inactive state. 

#### 60.7.10.4 Deadtime insertion 

In Waveforms for generation of PWM complementary signals using an LC, the PWMA_T output is generated by XORing timer outputs TMR0 and TMR1. The PWMA_B output is complementary to PWMA_T. Digital filters insert a dead time of one system clock cycle to delay the rising edges of both PWM signals. 

#### 60.7.10.5 Fault events 

Waveforms for force cleared on force deassertion shows the reaction to the fault event. On a fault event, both the PWM outputs transition to the inactive state (logic 0). When fault event deasserts, both the PWM signals start operating according to FORCE_MODE = 00 (cleared on force deassertion). 

Alternatively, after the fault event deasserts, fault clearing can be performed according to FORCE_MODE = 01 (cleared on rising sync force deassertion). See Waveforms for force cleared on rising sync after force deassertion for details. 

#### 60.7.10.6 AC motor power stage schematic 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2131-11.png)


<!-- Start of picture text -->
IDC<br>PWMA_T PWMB_T PWMC_T<br>CDC<br>IA IB IC<br>PWMA_B PWMB_B PWMC_B<br>RSH<br>Phase B<br>AC motor<br>Phase A Phase C<br><!-- End of picture text -->

Figure 283. AC motor power stage schematic 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2131 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

#### 60.7.10.7 Waveforms for double-switching technique example 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2132-03.png)


<!-- Start of picture text -->
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19<br>Lcu_clk i j k l<br>UA<br>UB<br>UC<br>PWMA_T g T3 h<br>PWMA_B Sample IA[0] Sample IA[0]<br>PWMB_T Sample -IC[0]a T1 b T2 c Sample -IC[1]<br>PWMB_B<br>PWMC_T d T1 e T3 f<br>PWMC_B<br>IA m I A[0] n I A[1]<br>IB<br>IC o-I C[0] p-I C[1]<br>IA (IA[0]+IA[1])/2 I A=<br>IB I B=-IA-IC<br>IC (IC[0]+IC[1])/2 I C=<br>Phase voltages<br>Power switches<br>ADC sampling<br>Computing<br><!-- End of picture text -->

Figure 284. Waveforms for double-switching technique example 

#### 60.7.10.8 Implementation for AC motor double-switching controller 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2132-06.png)


<!-- Start of picture text -->
TMR0 PWMA_T<br>TMR1 LC0 PWMA_B<br>TMR2 PWMB_T<br>TMR3 LCU PWMB_B<br>TMR4 PWMC_T<br>TMR5 LC1 PWMC_B<br>System clock SYNC<br>FAULT0 FAULT2<br>FAULT1<br>Path delays: 2 clocks FILTx clocks<br><!-- End of picture text -->

Figure 285. Implementation for AC motor double-switching controller 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2132 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

#### 60.7.10.9 Implementation for controlling one phase 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2133-03.png)


<!-- Start of picture text -->
TMR0 PWMA_T<br>I0 O0<br>LC0<br>TMR1 PWMA_B<br>I1 O1<br>System clock SYNC<br>FAULT<br>Path delays: 2 clocks FILTx clocks<br><!-- End of picture text -->

Figure 286. Implementation for controlling one phase 

#### 60.7.10.10 Connections and controls 

Table 330. Connections and controls 

|Name|Description|
|---|---|
|TMRn|Synchronized timer input signals|
|System clock|Clock supplied to the LC|
|FAULTn|Fault signal (seeImplementation for AC motor double-<br>switching controllerfor more details)|
|SYNC|Sync signal for optional automatic fault recovery|
|PWMx_T|PWM output signal for controlling top power switch|
|PWMx_B|PWM output signal for controlling bottom power switch|



#### 60.7.10.11 Truth table 

Table 331. Truth table 

||Inputs|Ou|tputs|
|---|---|---|---|
|TMR1|TMR0|PWMA_T|PWMB_B|
|0|0|0|1 delayed by TdH (seeOutput edge delays)|
|0|1|1 delayed by TdH (seeOutput edge delays)|0|
|1|0|1 delayed by TdH (seeOutput edge delays)|0|
|1|1|0|1 delayed by TdH (seeOutput edge delays)|
|0|0|0|0|
|0|1|0|0|
|1|0|0|0|
|1|1|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2133 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

#### 60.7.10.12 Register configuration 

Table 332. Register configuration 

|Register|I3|I2|I1|I0|O0|O1|O2|O3|
|---|---|---|---|---|---|---|---|---|
|LUTCTRL0|—|—|—|—|6h|—|—|—|
|LUTCTRL1|—|—|—|—|—|9h|—|—|
|LUTCTRL2|—|—|—|—|—|—|0h|—|
|LUTCTRL3|—|—|—|—|—|—|—|0h|
|FILT0|—|—|—|—|1_0000h|—|—|—|
|FILT1|—|—|—|—|—|1_0000h|—|—|
|FILT2|—|—|—|—|—|—|0h|—|
|FILT3|—|—|—|—|—|—|—|0h|
|INTDMAEN|—|—|—|—|0h||||
|OUTPOL|—|—|—|—|0h||||
|FFILT|—|—|—|—|100_0000h||||
|FCTRL|—|—|—|—|Force inputs<br>and 1 do no<br>All four inpu|2 and 0 affe<br>t affect ouput<br>ts affect outp|ct output 0, bu<br>0: 101h<br>ut 0: 1111h|t force inputs 3|
|SCTRL|—|—|—|—|0h||||
|MUXSEL0|—|—|—|1h|—|—|—|—|
|MUXSEL1|—|—|2h|—|—|—|—|—|
|MUXSEL2|—|0h|—|—|—|—|—|—|
|MUXSEL3|0h|—|—|—|—|—|—|—|
|SWEN|—|—|—|—|0h||||
|SWVALUE|—|—|—|—|0h||||
|OUTEN|—|—|—|—|3h||||



#### 60.7.10.13 Waveforms for generation of PWM complementary signals using an LC 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2134-06.png)


<!-- Start of picture text -->
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39<br>System clock<br>SYNC<br>TMR0<br>TMR1<br>FAULT<br>PWMA_T<br>PWMA_B<br>OUTEN<br><!-- End of picture text -->

Figure 287. Waveforms for generation of PWM complementary signals using an LC 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2134 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

#### 60.7.10.14 Waveforms for force cleared on force deassertion 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2135-03.png)


<!-- Start of picture text -->
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39<br>System clock<br>SYNC<br>TMR0<br>TMR1<br>FAULT<br>PWMA_T<br>PWMA_B<br>OUTEN<br><!-- End of picture text -->

Figure 288. Waveforms for force cleared on force deassertion 

#### 60.7.10.15 Waveforms for force cleared on rising sync after force deassertion 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2135-06.png)


<!-- Start of picture text -->
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39<br>System clock<br>SYNC<br>TMR0<br>TMR1<br>FAULT<br>PWMA_T<br>PWMA_B<br>OUTEN<br><!-- End of picture text -->

Figure 289. Waveforms for force cleared on rising sync after force deassertion 

### 60.7.11 Brushless DC (BLDC) motor PWM controller 

#### 60.7.11.1 Overview 

You can use LCU to replace the mechanical commutator in the BLDC motor control application with Hall-sensor position measurement. 

In this example implementation, LC0 receives the direction (DIR) and Hall A, Hall B, and Hall C sensor output states, and from those inputs generates the switching states S1, S2, and S3. LC1 and LC2 convert the switching states to PWM or on-off signals for controlling power switches, as illustrated in Waveforms for BLDC motor control technique. 

BLDC motor power stage schematic and BLDC motor electrical arrangement illustrate a three-phase BLDC motor power stage with switching pulses and phase currents controlling motor rotation in the CCW direction. The state of the Hall sensors is 010. As the rotor shaft rotates, Hall sensors track the motor position. You accelerate or decelerate the motor by controlling the width of the PWM signal. You can include one or more faults (force inputs) to force power switches instantaneously into the inactive state if there is an overcurrent. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2135 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

#### 60.7.11.2 Implementation 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2136-03.png)


<!-- Start of picture text -->
S1 Q1H<br>I0 O0<br>S2 Q1L<br>I1 O1<br>S3 LC1 Q2H<br>I2 O2<br>PWM Q2L<br>I3 O3<br>HALL A S1 Q3H<br>I0 O0 I0 O0<br>HALL B S2 Q3L<br>I1 O1 I1 O1<br>HALL C LC0 S3 LC2<br>I2 O2 I2 O2<br>DIR<br>I3 O3 I3 O3<br>System clock<br>Fault<br>Path delays: 2 clocks FILTx+1 clock FILTx clocks<br>Figure 290. Implementation<br><!-- End of picture text -->

#### 60.7.11.3 BLDC motor power stage schematic 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2136-05.png)


<!-- Start of picture text -->
A<br>IDC<br>Q1H Q2H Q3H<br>IA<br>CDC<br>IC<br>Q1L Q2L Q3L<br>C B<br>BLDC motor<br>Figure 291. BLDC motor power stage schematic<br>Hall C Hall B<br>Hall A<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2136 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

#### 60.7.11.4 BLDC motor electrical arrangement 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2137-03.png)


<!-- Start of picture text -->
100<br>A<br>120° 60°<br>101 110<br>180° 0° = 360°<br>C 010 B<br>001 010<br>240° 300°<br>Hall C Hall B<br>Hall A<br><!-- End of picture text -->

Figure 292. BLDC motor electrical arrangement 

#### 60.7.11.5 Waveforms for BLDC motor control technique 

This figure illustrates the basic waveforms for controlling a BLDC motor with stator windings and Hall sensors arranged according to BLDC motor electrical arrangement. Configure the external hardware (motor or sensor) so that it can produce these waveforms; then you can configure LCU. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2137 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2138-02.png)


<!-- Start of picture text -->
0 30 60 90 120 150 180 210 240 270 300 330 360<br>Hall A<br>Hall B<br>Hall C<br>Hall states 110 100 101 001 011 010<br>Direction [DIR]<br>Phases [ABC] −+NC NC+− +NC− +−NC NC−+ −NC+<br>Q1H OFF OFF OFF OFF<br>Q1L ON OFF OFF OFF OFF ON<br>Q2H OFF OFF OFF OFF<br>Q2L OFF OFF OFF ON ON OFF<br>Q3H OFF OFF OFF OFF<br>Q3L OFF ON ON OFF OFF OFF<br>Direction [DIR]<br>Phases [ABC] +−NC NC−+ −NC+ −+NC NC+− +NC−<br>Q1H OFF OFF OFF OFF<br>Q1L OFF OFF ON ON OFF OFF<br>Q2H OFF OFF OFF OFF<br>Q2L ON ON OFF OFF OFF OFF<br>Q3H OFF OFF OFF OFF<br>Q3L OFF OFF OFF OFF ON ON<br>Hall sensors<br>CW direction [360→0]<br>CCW direction [0→360]<br><!-- End of picture text -->

Figure 293. Waveforms for BLDC motor control technique 

#### 60.7.11.6 Connections and controls 

Table 333. Connections and controls 

|Input-output group<br>Name|Description|
|---|---|
|LC0 inputs<br>HALL A|Hall sensor A output state|
|HALL B|Hall sensor B output state|
|HALL C|Hall sensor C output state|
|DIR|Direction of shaft rotation, as illustrated inWaveforms for reversing BLDC<br>motor.|
|LC1 and LC2 inputs<br>S1|Switching state 1 (output 0 from LC0)|
|S2|Switching state 2 (output 1 from LC0)|
|S2|Switching state 3 (output 2 from LC0)|
|PWM|Output from PWM|
|LC0, LC1, and LC2 inputs<br>Clock|LCU clock input|
|Fault|Optional fault input|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2138 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

Table 333. Connections and controls (continued) 

|Input-output group|Name|Description|
|---|---|---|
|LC1 outputs|Q1H<br>Q1L|Motor control switch outputs, as illustrated inBLDC motor electrical<br>arrangement|
||Q2H||
||Q2L||
|LC2 outputs|Q3H||
||Q3L||



#### 60.7.11.7 Truth table for generating switching states 

This table includes all Hall sensor states, even those that never occur because of sensor displacement by 120°. 

Table 334. Truth table for generating switching states 

||I|nputs|||Outpu|ts|Comments|
|---|---|---|---|---|---|---|---|
|DIR|Hall C|Hall B|Hall A|S1|S2|S3||
|0|0|0|0|0|0|0|Not used|
|0|0|0|1|1|0|0|Hall states|
|0|0|1|0|0|1|0|Hall states|
|0|0|1|1|1|1|0|Hall states|
|0|1|0|0|0|0|1|Hall states|
|0|1|0|1|1|0|1|Hall states|
|0|1|1|0|0|1|1|Hall states|
|0|1|1|1|0|0|0|Not used|
|1|0|0|0|0|0|0|Not used|
|1|0|0|1|0|1|1|Complement of Hall states|
|1|0|1|0|1|0|1|Complement of Hall states|
|1|0|1|1|0|0|1|Complement of Hall states|
|1|1|0|0|1|1|0|Complement of Hall states|
|1|1|0|1|0|1|0|Complement of Hall states|
|1|1|1|0|1|0|0|Complement of Hall states|
|1|1|1|1|0|0|0|Not used|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2139 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

#### 60.7.11.8 Truth table for generating switching pulses for phases A and B 

Table 335. Truth table for generating switching pulses for phases A and B 

|||Inputs|||O|utputs||Comments|
|---|---|---|---|---|---|---|---|---|
|PWM|S3|S2|S1|Q1H|Q1L|Q2H|Q2L||
|0|0|0|0|0|0|0|0|Not used|
|0|0|0|1|0|0|0|0|—|
|0|0|1|0|0|1|0|0|—|
|0|0|1|1|0|1|0|0|—|
|0|1|0|0|0|0|0|1|—|
|0|1|0|1|0|0|0|0|—|
|0|1|1|0|0|0|0|1|—|
|0|1|1|1|0|0|0|0|Not used|
|1|0|0|0|0|0|0|0|Not used|
|1|0|0|1|0|0|1|0|—|
|1|0|1|0|0|1|0|0|—|
|1|0|1|1|0|1|1|0|—|
|1|1|0|0|1|0|0|1|—|
|1|1|0|1|1|0|0|0|—|
|1|1|1|0|0|0|0|1|—|
|1|1|1|1|0|0|0|0|Not used|



#### 60.7.11.9 Truth table for generating switching pulses for phase C 

Table 336. Truth table for generating switching pulses for phase C 

|||Inputs|||Outputs|Comments|
|---|---|---|---|---|---|---|
|PWM|S3|S2|S1|Q3H|Q3L||
|0|0|0|0|0|0|Not used|
|0|0|0|1|0|1|—|
|0|0|1|0|0|0|—|
|0|0|1|1|0|0|—|
|0|1|0|0|0|0|—|
|0|1|0|1|0|1|—|
|0|1|1|0|0|0|—|
|0|1|1|1|0|0|Not used|
|1|0|0|0|0|0|Not used|
|1|0|0|1|0|1|—|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2140 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

Table 336. Truth table for generating switching pulses for phase C (continued) 

|||Inputs|||Outputs|Comments|
|---|---|---|---|---|---|---|
|PWM|S3|S2|S1|Q3H|Q3L||
|1|0|1|0|1|0|—|
|1|0|1|1|0|0|—|
|1|1|0|0|0|0|—|
|1|1|0|1|0|1|—|
|1|1|1|0|1|0|—|
|1|1|1|1|0|0|Not used|



#### 60.7.11.10 Configuration for generating switching states 

Table 337. Configuration for generating switching states 

|Register|I3|I2|I1|I0|O0|O1|O2|O3|
|---|---|---|---|---|---|---|---|---|
|LUTCTRL0|—|—|—|—|542Ah|—|—|—|
|LUTCTRL1|—|—|—|—|—|324Ch|—|—|
|LUTCTRL2|—|—|—|—|—|—|E70h|—|
|LUTCTRL3|—|—|—|—|—|—|—|0h|
|FILT0|—|—|—|—|0h|—|—|—|
|FILT1|—|—|—|—|—|0h|—|—|
|FILT2|—|—|—|—|—|—|0h|—|
|FILT3|—|—|—|—|—|—|—|0h|
|INTDMAEN|—|—|—|—|0h||||
|OUTPOL|—|—|—|—|0h||||
|FFILT|—|—|—|—|0h||||
|FCTRL|—|—|—|—|0h||||
|SCTRL|—|—|—|—|0h||||
|MUXSEL0|—|—|—|1h|—|—|—|—|
|MUXSEL1|—|—|2h|—|—|—|—|—|
|MUXSEL2|—|3h|—|—|—|—|—|—|
|MUXSEL3|4h|—|—|—|—|—|—|—|
|SWEN|—|—|—|—|0h||||
|SWVALUE|—|—|—|—|0h||||
|OUTEN|—|—|—|—|7h||||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2141 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

#### 60.7.11.11 Configuration for switching pulses for phases A and B 

Table 338. Configuration for switching pulses for phases A and B 

|Register|I3|I2|I1|I0|O0|O1|O2|O3|
|---|---|---|---|---|---|---|---|---|
|LUTCTRL0|—|—|—|—|3000h|—|—|—|
|LUTCTRL1|—|—|—|—|—|C0Ch|—|—|
|LUTCTRL2|—|—|—|—|—|—|A00h|—|
|LUTCTRL3|—|—|—|—|—|—|—|5050h|
|FILT0|—|—|—|—|0h|—|—|—|
|FILT1|—|—|—|—|—|0h|—|—|
|FILT2|—|—|—|—|—|—|0h|—|
|FILT3|—|—|—|—|—|—|—|0h|
|INTDMAEN|—|—|—|—|0h||||
|OUTPOL|—|—|—|—|0h||||
|FFILT|—|—|—|—|F00_0000h||||
|FCTRL|—|—|—|—|101_0101h||||
|SCTRL|—|—|—|—|0h||||
|MUXSEL4|—|—|—|Dh|—|—|—|—|
|MUXSEL5|—|—|Eh|—|—|—|—|—|
|MUXSEL6|—|Fh|—|—|—|—|—|—|
|MUXSEL7|8h|—|—|—|—|—|—|—|
|SWEN|—|—|—|—|0h||||
|SWVALUE|—|—|—|—|0h||||
|OUTEN|—|—|—|—|F0h||||



#### 60.7.11.12 Configuration for switching pulses for phase C 

Table 339. Configuration for switching pulses for phase C 

|Register|I3|I2|I1|I0|O0|O1|O2|O3|
|---|---|---|---|---|---|---|---|---|
|LUTCTRL0|—|—|—|—|4400h|—|—|—|
|LUTCTRL1|—|—|—|—|—|2222h|—|—|
|LUTCTRL2|—|—|—|—|—|—|0h|—|
|LUTCTRL3|—|—|—|—|—|—|—|0h|
|FILT0|—|—|—|—|0h|—|—|—|
|FILT1|—|—|—|—|—|0h|—|—|
|FILT2|—|—|—|—|—|—|0h|—|
|FILT3|—|—|—|—|—|—|—|0h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2142 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

Table 339. Configuration for switching pulses for phase C (continued) 

|Register|I3|I2|I1|I0|O0<br>O1|O2|O3|
|---|---|---|---|---|---|---|---|
|INTDMAEN|—|—|—|—|0h|||
|OUTPOL|—|—|—|—|0h|||
|FFILT|—|—|—|—|0300_0000h|||
|FCTRL|—|—|—|—|101h|||
|SCTRL|—|—|—|—|0h|||
|MUXSEL8|—|—|—|Dh|—<br>—|—|—|
|MUXSEL9|—|—|Eh|—|—<br>—|—|—|
|MUXSEL10|—|Fh|—|—|—<br>—|—|—|
|MUXSEL11|8h|—|—|—|—<br>—|—|—|
|SWEN|—|—|—|—|0h|||
|SWVALUE|—|—|—|—|0h|||
|OUTEN|—|—|—|—|300h|||



#### 60.7.11.13 Waveforms for reversing BLDC motor 

This figure illustrates the waveforms for controlling a reversing BLDC motor. The DIR input indicates the direction of rotation: 

- Logic 0 for CW rotation 

- Logic 1 for CCW rotation 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2143-08.png)


<!-- Start of picture text -->
System clock<br>PWM<br>Hall A<br>Hall B<br>Hall C<br>Hall States 010b 011b 001b 101b 100b 110b 100b 101b 001b 011b 010b<br>FAULT<br>DIR<br>S 010b 011b 001b 101b 100b 110b 001b 011b 010b 110b 100b<br>Q1H<br>Q1L<br>Q2H<br>Q2L<br>Q3H<br>Q3L<br>OUTEN 00h 3F7h<br>Inputs<br>Outputs<br><!-- End of picture text -->

Figure 294. Waveforms for reversing BLDC motor 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2143 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

#### 60.7.11.14 Waveforms for reversing BLDC motor with fault assertion 

This figure illustrates the waveforms for the reaction to an external fault in addition to reversing the BLDC motor. On the occurrence of an external fault event, the power switches transition to the inactive state (logic 0). Two clock cycles after external fault deassertion, the power switches start operating normally. 

Switching state outputs S1, S2, and S3, generated by LC0, receive an additional delay of one clock cycle on their way to the inputs of other LCs (digital filters bypassed). 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2144-05.png)


<!-- Start of picture text -->
System clock<br>PWM<br>Hall A<br>Hall B<br>Hall C<br>Hall States 010b 011b 001b 101b 100b 110b 100b 101b 001b 011b 010b<br>FAULT<br>DIR<br>S 010b 011b 001b 101b 100b 110b 001b 011b 010b 110b 100b<br>Q1H<br>Q1L<br>Q2H<br>Q2L<br>Q3H<br>Q3L<br>OUTEN 00h 3F7h<br>Inputs<br>Outputs<br><!-- End of picture text -->

Figure 295. Waveforms for reversing BLDC motor with fault assertion 

## 60.8 Registers 

### 60.8.1 Mapping of 16-bit input, output, and state fields 

This table maps inputs, outputs, or states to the bit positions in the following 16-bit fields: 

- SWEN[SWEN] 

- SWVALUE[SWVALUE] 

- OUTEN[OUTEN] 

- LCIN[LC_INPUTS] 

- SWOUT[SWOUT] 

- LCOUT[LCOUT] 

- FORCEOUT[FORCEOUT] 

- FORCESTS[FORCESTS] 

- DBGEN[DBGEN] 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2144 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

|LC|Input, output, or state|Bit|
|---|---|---|
|0|0|0|
||1|1|
||2|2|
||3|3|
|1|0|4|
||1|5|
||2|6|
||3|7|
|2|0|8|
||1|9|
||2|10|
||3|11|
|3|0|12|
||1|13|
||2|14|
||3|15|



## 60.9 LCU register descriptions 

~~<mark>NOTE</mark>~~ 

Access to address offset 2A4h does not generate a transfer error. 

### 60.9.1 LCU memory map 

LCU_0 base address: 4009_8000h 

LCU_1 base address: 4009_C000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|LC 0 Output 0 LUT Control (LC0_LUTCTRL0)|32|RW|0000_0000h|
|4h|LC 0 Output 1 LUT Control (LC0_LUTCTRL1)|32|RW|0000_0000h|
|8h|LC 0 Output 2 LUT Control (LC0_LUTCTRL2)|32|RW|0000_0000h|
|Ch|LC 0 Output 3 LUT Control (LC0_LUTCTRL3)|32|RW|0000_0000h|
|10h|LC 0 Output 0 Filter (LC0_FILT0)|32|RW|0000_0000h|
|14h|LC 0 Output 1 Filter (LC0_FILT1)|32|RW|0000_0000h|
|18h|LC 0 Output 2 Filter (LC0_FILT2)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2145 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|1Ch|LC 0 Output 3 Filter (LC0_FILT3)|32|RW|0000_0000h|
|20h|LC 0 Interrupt and DMA Enable (LC0_INTDMAEN)|32|RW|0000_0000h|
|24h|LC 0 Status (LC0_STS)|32|W1C|0000_0000h|
|28h|LC 0 Output Polarity Control (LC0_OUTPOL)|32|RW|0000_0000h|
|2Ch|LC 0 Force Filter (LC0_FFILT)|32|RW|0000_0000h|
|30h|LC 0 Force Control (LC0_FCTRL)|32|RW|0000_0000h|
|34h|LC 0 Sync Control (LC0_SCTRL)|32|RW|0000_0000h|
|40h|LC 1 Output 0 LUT Control (LC1_LUTCTRL0)|32|RW|0000_0000h|
|44h|LC 1 Output 1 LUT Control (LC1_LUTCTRL1)|32|RW|0000_0000h|
|48h|LC 1 Output 2 LUT Control (LC1_LUTCTRL2)|32|RW|0000_0000h|
|4Ch|LC 1 Output 3 LUT Control (LC1_LUTCTRL3)|32|RW|0000_0000h|
|50h|LC 1 Output 0 Filter (LC1_FILT0)|32|RW|0000_0000h|
|54h|LC 1 Output 1 Filter (LC1_FILT1)|32|RW|0000_0000h|
|58h|LC 1 Output 2 Filter (LC1_FILT2)|32|RW|0000_0000h|
|5Ch|LC 1 Output 3 Filter (LC1_FILT3)|32|RW|0000_0000h|
|60h|LC 1 Interrupt and DMA Enable (LC1_INTDMAEN)|32|RW|0000_0000h|
|64h|LC 1 Status (LC1_STS)|32|W1C|0000_0000h|
|68h|LC 1 Output Polarity Control (LC1_OUTPOL)|32|RW|0000_0000h|
|6Ch|LC 1 Force Filter (LC1_FFILT)|32|RW|0000_0000h|
|70h|LC 1 Force Control (LC1_FCTRL)|32|RW|0000_0000h|
|74h|LC 1 Sync Control (LC1_SCTRL)|32|RW|0000_0000h|
|80h|LC 2 Output 0 LUT Control (LC2_LUTCTRL0)|32|RW|0000_0000h|
|84h|LC 2 Output 1 LUT Control (LC2_LUTCTRL1)|32|RW|0000_0000h|
|88h|LC 2 Output 2 LUT Control (LC2_LUTCTRL2)|32|RW|0000_0000h|
|8Ch|LC 2 Output 3 LUT Control (LC2_LUTCTRL3)|32|RW|0000_0000h|
|90h|LC 2 Output 0 Filter (LC2_FILT0)|32|RW|0000_0000h|
|94h|LC 2 Output 1 Filter (LC2_FILT1)|32|RW|0000_0000h|
|98h|LC 2 Output 2 Filter (LC2_FILT2)|32|RW|0000_0000h|
|9Ch|LC 2 Output 3 Filter (LC2_FILT3)|32|RW|0000_0000h|
|A0h|LC 2 Interrupt and DMA Enable (LC2_INTDMAEN)|32|RW|0000_0000h|
|A4h|LC 2 Status (LC2_STS)|32|W1C|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2146 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|A8h|LC 2 Output Polarity Control (LC2_OUTPOL)|32|RW|0000_0000h|
|ACh|LC 2 Force Filter (LC2_FFILT)|32|RW|0000_0000h|
|B0h|LC 2 Force Control (LC2_FCTRL)|32|RW|0000_0000h|
|B4h|LC 2 Sync Control (LC2_SCTRL)|32|RW|0000_0000h|
|200h - 22Ch|Mux Select (MUXSEL0 - MUXSEL11)|32|RW|0000_0000h|
|280h|Configuration (CFG)|32|RW|0303_0280h|
|284h|Software Override Enable (SWEN)|32|RW|0000_0000h|
|288h|Software Override Value (SWVALUE)|32|RW|0000_0000h|
|28Ch|Output Enable (OUTEN)|32|RW|0000_0000h|
|290h|Logic Inputs (LCIN)|32|RO|0000_0000h|
|294h|Overridden Inputs (SWOUT)|32|RO|0000_0000h|
|298h|Logic Outputs (LCOUT)|32|RO|0000_0000h|
|29Ch|Forced Outputs (FORCEOUT)|32|RO|0000_0000h|
|2A0h|Force Status (FORCESTS)|32|W1C|0000_0000h|
|2A8h|Debug Mode Enable (DBGEN)|32|RW|0000_0000h|



### 60.9.2 LC n Output m LUT Control (LC0_LUTCTRL0 - LC2_LUTCTRL3) 

##### Offset 

For n = 0 to 2; m = 0 to 3: 

|Register|Offset|
|---|---|
|LCn_LUTCTRLm|0h + (n × 40h) + (m × 4h)|



Function 

See LUTCTRL. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2147 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2148-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>LUTCTRL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16|Reserved|
|—||
|15-0|LUT Control|
|LUTCTRL|Specifies the LUT positions, based on the combined LC input value, that result in assertion of this output.<br>For more information, seeLogic operations.|



### 60.9.3 LC n Output m Filter (LC0_FILT0 - LC2_FILT3) 

##### Offset 

For n = 0 to 2; m = 0 to 3: 

|Register|Offset|
|---|---|
|LCn_FILTm|10h + (n × 40h) + (m × 4h)|



##### Function 

Specifies the rising- and falling-edge thresholds for the LC output filters. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||LUT_RI|SE_FILT||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||LUT_FA|LL_FILT||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2148 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

##### Fields 

|Field|Function|
|---|---|
|31-16|Rise Filter|
|LUT_RISE_FIL<br>T|Specifies the number of consecutive clock cycles the filter output must be logic 1 before the output signal<br>goes high.|
||0000_0000_0000_0000b - Bypass filter|
||All other values - Filter threshold|
|15-0|Fall Filter|
|LUT_FALL_FIL<br>T|Specifies the number of consecutive clock cycles the filter output must be logic 0 before the output signal<br>goes low.|
||0000_0000_0000_0000b - Bypass filter|
||All other values - Filter threshold|



### 60.9.4 LC n Interrupt and DMA Enable (LC0_INTDMAEN - LC2_INTDMAEN) 

##### Offset 

|Register|Offset|
|---|---|
|LC0_INTDMAEN|20h|
|LC1_INTDMAEN|60h|
|LC2_INTDMAEN|A0h|



##### Function 

Enables interrupt and DMA requests for LUT and force events. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||0||||FORCE_|DMA_EN|||0||||FORCE|_INT_EN||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||0||||LUT_D|MA_EN|||0||||LUT_I|NT_EN||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2149 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

##### Fields 

|Field|Function||
|---|---|---|
|31-28<br>|Reserved||
|—<br>27-24<br>FORCE_DMA_<br>EN|Force DMA Enable<br>Enables the generation of a DMA requ<br>For each bit:<br>0b - Disable<br>1b - Enable<br>Mapping of bits:|est when a force event occurs (LCn_STS[FORCESTS]).|
||Output|Register bit|
||0|24|
||1|25|
||2|26|
||3|27|
|23-20<br>—|Reserved||
|19-16|Force Interrupt Enable||
|FORCE_INT_E<br>N|Enables the generation of an interrupt<br>For each bit:<br>0b - Disable<br>1b - Enable<br>Mapping of bits:|request when a force event occurs (LCn_STS[FORCESTS]).|
||Output|Register bit|
||0|16|
||1|17|
||2|18|
||3|19|
|15-12<br>—|Reserved||
|11-8|LUT DMA Enable||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2150 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

##### Table continued from the previous page... 

|Field|Function||
|---|---|---|
|LUT_DMA_EN|Enables the generation of a DMA req<br>For each bit:<br>0b - Disable<br>1b - Enable<br>Mapping of bits:|uest when an LUT event occurs (LCn_STS[LUT_STS]).|
||Output|Register bit|
||0|8|
||1|9|
||2|10|
||3|11|
|7-4|Reserved||
|—<br>3-0<br>LUT_INT_EN|LUT Interrupt Enable<br>Enables the generation of an interrup<br>For each bit:|t request when an LUT event occurs (LCn_STS[LUT_STS]).|
||0b - Disable<br>1b - Enable<br>Mapping of bits:||
||Output|Register bit|
||0|0|
||1|1|
||2|2|
||3|3|



### 60.9.5 LC n Status (LC0_STS - LC2_STS) 

##### Offset 

|Register|Offset||
|---|---|---|
|LC0_STS|24h||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2151 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

Table continued from the previous page... 

|Register|Offset|
|---|---|
|LC1_STS|64h|
|LC2_STS|A4h|



##### Function 

Indicates the occurrence of LUT and force events. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||0|||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||0||||FORC|ESTS|||0||||LUT_|STS||
|W||||||W1|C|||||||W|1C||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function||
|---|---|---|
|31-12<br>—|Reserved||
|11-8|Force Event||
|FORCESTS|Indicates that a force event has occurred<br>For each bit:|on the associated output.|
||0b - No event<br>1b - Event occurred<br>Mapping of bits:||
||Output|Register bit|
||0|8|
||1|9|
||2|10|
||3|11|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2152 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

##### Table continued from the previous page... 

|Field|Function||
|---|---|---|
||When you enable DMA for a force output (LC<br>on that output, LCU generates a DMA reque<br>bit to 0, or you can write 1 to the bit.<br>You can also change these bits to 0 by writin<br>bits (FORCESTS[FORCESTS]).<br>The timing of status clearing depends on the|n_INTDMAEN[FORCE_DMA_EN]) and a force event occurs<br>st. The resulting DMA done signal causes LCU to change the<br>g to the corresponding Force Status<br>selected Force Mode (LCn_FCTRL[FORCE_MODEm]).|
|7-4<br>—<br>3-0<br>LUT_STS|Reserved<br>LUT Event<br>Indicates that an LUT event has occurred for<br>For each bit:<br>0b - No event<br>1b - Event occurred<br>Mapping of bits:|the associated LC output.|
||Output|Register bit|
||0|0|
||1|1|
||2|2|
||3|3|
||When you enable DMA for an LUT event on<br>event occurs on that output, LCU generates<br>to change the bit to 0.<br>When you enable interrupt request for an outp<br>on that output, LCU generates an interrupt re|an output (LCn_INTDMAEN[LUT_DMA_EN]) and an LUT<br>a DMA request. The resulting DMA done signal causes LCU<br>ut (LCn_INTDMAEN[LUT_INT_EN]) and an LUT event occurs<br>quest. Write 1 to the bit to change it to 0.|



### 60.9.6 LC n Output Polarity Control (LC0_OUTPOL - LC2_OUTPOL) 

##### Offset 

|Register|Offset|
|---|---|
|LC0_OUTPOL|28h|
|LC1_OUTPOL|68h|
|LC2_OUTPOL|A8h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2153 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

##### Function 

##### Specifies the polarity of the LC outputs. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||0||||||||OUT|POL||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function||
|---|---|---|
|31-4<br>—|Reserved||
|3-0|Output Polarity||
|OUTPOL|Specifies the polarity of the outputs.<br>For each bit:||
||0b - Not inverted||
||1b - Inverted<br>Mapping of bits:||
||Output|Bit|
||0|0|
||1|1|
||2|2|
||3|3|



### 60.9.7 LC n Force Filter (LC0_FFILT - LC2_FFILT) 

##### Offset 

|Register|Offset||
|---|---|---|
|LC0_FFILT|2Ch||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2154 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

##### Table continued from the previous page... 

|Register|Offset|
|---|---|
|LC1_FFILT|6Ch|
|LC2_FFILT|ACh|



##### Function 

##### Controls the force filter for this LC. 

##### Diagram 

|Bits|31|30|29|28|27|26|25<br>24|23|22|21|20|19|18<br>17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||COMB_|FORCE||0||COMB_EN|||0|||FORCE_POL|
|Reset|0|0|0|0|0|0|0<br>0|0|0|0|0|0|0<br>0<br>0|
|Bits|15|14|13|12|11|10|9<br>8|7|6|5|4|3|2<br>1<br>0|
|R<br>W|||||0||||||FORCE|_FILT||
|Reset|0|0|0|0|0|0|0<br>0|0|0|0|0|0|0<br>0<br>0|



##### Fields 

|Field|Function||
|---|---|---|
|31-28|Combined Sensed Force Input||
|COMB_FORCE|Indicates the combined value of force inputs to each<br>For each bit:<br>0b - Logic low<br>1b - Logic high<br>Mapping of bits:<br>|output.<br>|
||Output|Bit|
||0|28|
||1|29|
||2|30|
||3|31|
|27<br>—|Reserved||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2155 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|26-24|Combinational Force Path (CFP) Enable|
|COMB_EN|Enables an active force input to combinationally affect the LC outputs. When CFP is not enabled, force<br>inputs must be synchronized and then optionally filtered. When you enable CFP (write 1 to one of these bits),<br>the corresponding force input bypasses synchronization and filtering and immediately affects the LC output.<br>The Force Filter (FORCE_FILT) is still in effect. Force inputs that do not meet the pulse width requirements<br>for synchronization and filtering are not registered in Force Status (FORCESTS) and you do not need to<br>write 1 to change the bit to 0.<br>CFP provides a safety factor when the LC outputs drive a motor and immediate response is required. In<br>some topologies, an oscillation can result if the assertion of the force input causes the LC output to turn off.<br>This situation in turn leads to deassertion of the force input and the output turning back on. In general, you<br>must disable CFP unless the LCU outputs drive a motor or similar safety-critical application, which requires<br>an immediate response without synchronization delays.|
|23-19<br>—|Reserved|
|18-16|Force Input Polarity|
|FORCE_POL|Specifies the polarity of the force inputs to this LC.<br>For each bit:<br>0b - Not inverted<br>1b - Inverted<br>Mapping of bits:|
||Input<br>Bit|
||0<br>16|
||1<br>17|
||2<br>18|
||3<br>19|
|15-8<br>—|Reserved|
|7-0|Force Filter|
|FORCE_FILT|Specifies the count, in clock cycles, that a force input must remain at a given logic state before the filtered<br>force input switches state.<br>0000_0000b - Bypass filter<br>All other values - Filter threshold|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2156 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

### 60.9.8 LC n Force Control (LC0_FCTRL - LC2_FCTRL) 

##### Offset 

|Register|Offset|
|---|---|
|LC0_FCTRL|30h|
|LC1_FCTRL|70h|
|LC2_FCTRL|B0h|



##### Function 

Provides control of the force inputs. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19<br>18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|SYNC_|SEL3|FORCE_<br>3|MODE<br>||FORCE_|SENSE3||SYNC_|SEL2|FORCE_<br>2|MODE<br>|FORCE_|SENSE2||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3<br>2|1|0|
|R<br>W|SYNC_|SEL1|FORCE_<br>1|MODE<br>||FORCE_|SENSE1||SYNC_|SEL0|FORCE_<br>0|MODE<br>|FORCE_|SENSE0||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-30|Sync Select|
|SYNC_SEL3|Selects which sync input to use for output 3 of this LC.<br>00b - Sync input 0|
||01b - Sync input 1|
||10b - Reserved<br>11b - Reserved|
|29-28|Force Clearing Mode|
|FORCE_MODE<br>3|Specifies the timing for clearing force events for output 3 in this LC.<br>00b - Deassertion. Cleared on deassertion of force inputs|
||01b - Rising sync after deassertion. Cleared on rising sync after deassertion of force inputs<br>10b - Writing 1 after deassertion. Cleared by writing 1 to the correctLCn_STS[FORCESTS]or<br>FORCESTS[FORCESTS]bits after deassertion of force inputs|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2157 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||11b - Rising sync after writing 1 and deassertion. Cleared on rising sync after writing 1 to the<br>correctLCn_STS[FORCESTS]orFORCESTS[FORCESTS]bits and deassertion of force inputs|
|27-24|Force Input Sensitivity|
|FORCE_SENS<br>E3|Selects which force inputs affect output 3 of this LC.<br>For each bit:<br>0b - Does not affect<br>1b - Affects<br>Mapping of bits:<br><br>|
||Input<br>Bit|
||0<br>24|
||1<br>25|
||2<br>26|
||Reserved<br>27|
||Example: 011b selects force inputs 0 and 1, but not 2.|
|23-22<br>SYNC_SEL2|Sync Select<br>Selects which sync input to use for output 2 of this LC.<br>00b - Sync input 0<br>01b - Sync input 1<br>10b - Reserved<br>11b - Reserved|
|21-20|Force Clearing Mode|
|FORCE_MODE<br>2|Specifies the timing for clearing force events for output 2 in this LC.<br>00b - Deassertion. Cleared on deassertion of force inputs<br>01b - Rising sync after deassertion. Cleared on rising sync after deassertion of force inputs<br>10b - Writing 1 after deassertion. Cleared by writing 1 to the correctLCn_STS[FORCESTS]or<br>FORCESTS[FORCESTS]bits after deassertion of force inputs<br>11b - Rising sync after writing 1 and deassertion. Cleared on rising sync after writing 1 to the<br>correctLCn_STS[FORCESTS]orFORCESTS[FORCESTS]bits and deassertion of force inputs|
|19-16|Force Input Sensitivity|
|FORCE_SENS<br>E2|Selects which force inputs affect output 2 of this LC.<br>For each bit:|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2158 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Does not affect<br>1b - Affects<br>Mapping of bits:<br><br>|
||Input<br>Bit|
||0<br>16|
||1<br>17|
||2<br>18|
||Reserved<br>19|
||Example: 011b selects force inputs 0 and 1, but not 2.|
|15-14|Sync Select|
|SYNC_SEL1|Selects which sync input to use for output 1 of this LC.<br>00b - Sync input 0<br>01b - Sync input 1<br>10b - Reserved|
||11b - Reserved|
|13-12|Force Clearing Mode|
|FORCE_MODE<br>|Specifies the timing for clearing force events for output 1 in this LC.|
|1|00b - Deassertion. Cleared on deassertion of force inputs<br>01b - Rising sync after deassertion. Cleared on rising sync after deassertion of force inputs<br>10b - Writing 1 after deassertion. Cleared by writing 1 to the correctLCn_STS[FORCESTS]or<br>FORCESTS[FORCESTS]bits after deassertion of force inputs<br>11b - Rising sync after writing 1 and deassertion. Cleared on rising sync after writing 1 to the<br>correctLCn_STS[FORCESTS]orFORCESTS[FORCESTS]bits and deassertion of force inputs|
|11-8|Force Input Sensitivity|
|FORCE_SENS<br>E1|Selects which force inputs affect output 1 of this LC.<br>For each bit:<br>0b - Does not affect<br>1b - Affects<br>Mapping of bits:|
||Input<br>Bit|
||0<br>8|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2159 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||Input<br>Bit|
||1<br>9|
||2<br>10|
||Reserved<br>11|
||Example: 011b selects force inputs 0 and 1, but not 2.|
|7-6<br>SYNC_SEL0|Sync Select<br>Selects which sync input to use for output 0 of this LC.<br>00b - Sync input 0<br>01b - Sync input 1<br>10b - Reserved<br>11b - Reserved|
|5-4|Force Clearing Mode|
|FORCE_MODE|Specifies the timing for clearing force events for output 0 in this LC.|
|0|00b - Deassertion. Cleared on deassertion of force inputs<br>01b - Rising sync after deassertion. Cleared on rising sync after deassertion of force inputs<br>10b - Writing 1 after deassertion. Cleared by writing 1 to the correctLCn_STS[FORCESTS]or<br>FORCESTS[FORCESTS]bits after deassertion of force inputs<br>11b - Rising sync after writing 1 and deassertion. Cleared on rising sync after writing 1 to the<br>correctLCn_STS[FORCESTS]orFORCESTS[FORCESTS]bits and deassertion of force inputs|
|3-0|Force Input Sensitivity|
|FORCE_SENS<br>E0|Selects which force inputs affect output 0 of this LC.<br>For each bit:<br>0b - Does not affect<br>1b - Affects<br>Mapping of bits:|
||Input<br>Bit|
||0<br>0|
||1<br>1|
||2<br>2|
||Reserved<br>3|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2160 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||Input<br>Bit|
||Example: 011b selects force inputs 0 and 1, but not 2.|



### 60.9.9 LC n Sync Control (LC0_SCTRL - LC2_SCTRL) 

##### Offset 

|Register|Offset|
|---|---|
|LC0_SCTRL|34h|
|LC1_SCTRL|74h|
|LC2_SCTRL|B4h|



##### Function 

Controls the software sync behavior. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2161-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>SW_SYNC_SEL  SW_MODE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-10<br>—|Reserved|
|9-8|Software Sync Select|
|SW_SYNC_SE<br>L|Selects which sync input to use for software synced mode.<br>00b - Sync input 0|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2161 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2162-03.png)


<!-- Start of picture text -->
Field Function<br>01b - Sync input 1<br>10b - Reserved<br>11b - Reserved<br>7-4 Reserved<br>—<br>3-0 Software Sync Mode<br>SW_MODE Specifies the software sync mode for the inputs to this LC. When Software Override is enabled (SWEN),<br>these bits control whether Software Override Value (SWVALUE) changes occur immediately or on the rising<br>edge of the selected sync pulse.<br>For each bit:<br>0b - Immediate<br>1b - On rising edge of sync<br>Mapping of bits:<br>Input Bit<br>0 0<br>1 1<br>Reserved 2<br>Reserved 3<br><!-- End of picture text -->

### 60.9.10 Mux Select (MUXSEL0 - MUXSEL11) 

##### Offset 

For a = 0 to 11: 

|Register<br>MUXSELa|Offset<br>200h + (a × 4h)|
|---|---|



##### Function 

Selects the sources for inputs to the LCs. 

|Register|LC|Input|
|---|---|---|
|MUXSEL0|0|0|
|MUXSEL1||1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2162 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

##### Table continued from the previous page... 

|Register|LC<br>Input|
|---|---|
|MUXSEL2|2|
|MUXSEL3|3|
|MUXSEL4|1<br>0|
|MUXSEL5|1|
|MUXSEL6|2|
|MUXSEL7|3|
|MUXSEL8|2<br>0|
|MUXSEL9|1|
|MUXSEL10|2|
|MUXSEL11|3|



|Diagram<br>Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||||0|||||||MUX|SEL||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-8|Reserved|
|—||
|7-0|Mux Select|
|MUXSEL|Selects the source of the LC input.|
||All LU_IN inputs go through a two-stage synchronizer, but the LU_OUT signals fed back to this mux do not<br>have this two-stage delay because they are already synchronous to LCU clock.<br>0000_0000b - Logic 0<br>0000_0001b-0000_1100b - LU_IN0 to LU_IN11<br>0000_1101b-0001_1000b - LU_OUT0 to LU_OUT11<br>All other values are reserved.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2163 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

### 60.9.11 Configuration (CFG) 

##### Offset 

|Register|Offset|
|---|---|
|CFG|280h|



##### Function 

Indicates the LCU configuration, and provides write protection. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||N|UM_LOG|IC_CELLS|||||||NUM_F|ORCES||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|1|1|0|0|0|0|0|0|1|1|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||NUM_S|YNCS||||INCL_<br>MU...|||0||||WP|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|1|0|1|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-24|LCs|
|NUM_LOGIC_C<br>ELLS|Indicates the number of LCs.|
|23-16|Force Inputs|
|NUM_FORCES|Indicates the number of force inputs for each LC.|
|15-8|Sync Inputs|
|NUM_SYNCS|Indicates the number of sync inputs for each LC.|
|7|Input Muxing|
|INCL_MUXES|Indicates whether LCU supports input muxing.<br>0b - Not supported<br>1b - Supported|
|6-1<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2164 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|0|Write Protect|
|WP|Turns on write protection for all LCU registers exceptSWVALUE,LCn_STS, andFORCESTS.|
||~~NOTE~~|
||You can only write 1 to this field; you cannot turn off write protection after you turn it on.|



### 60.9.12 Software Override Enable (SWEN) 

##### Offset 

|Register|Offset|
|---|---|
|SWEN|284h|



##### Function 

Enables overrides for LC inputs. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2165-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>SWEN<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-12<br>—|Reserved|
|11-0|Software Override Enable|
|SWEN|Enables software override of LC inputs.|
||For each bit:|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2165 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Disable|
||1b - Enable|
||Mapping of bits: SeeMapping of 16-bit input, output, and state fields.|



### 60.9.13 Software Override Value (SWVALUE) 

##### Offset 

|Register|Offset|
|---|---|
|SWVALUE|288h|



##### Function 

Specifies the software override value for each LC input. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2166-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>SWVALUE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-12|Reserved|
|—||
|11-0|Software Override Value|
|SWVALUE|Specifies the software override value for each LC input.|
||For each bit:|
||0b - 0|
||1b - 1|
||Mapping of bits: SeeMapping of 16-bit input, output, and state fields.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2166 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

### 60.9.14 Output Enable (OUTEN) 

##### Offset 

|Register|Offset|
|---|---|
|OUTEN|28Ch|



##### Function 

##### Enables LC outputs. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/060_Logic_Control_Unit_-LCU-/S32K3XXRM_数据表.pdf-2167-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>OUTEN<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-12|Reserved|
|—||
|11-0|Output Enables|
|OUTEN|Enables LC outputs.|
||For each bit:|
||0b - Disable|
||1b - Enable|
||Mapping of bits: SeeMapping of 16-bit input, output, and state fields.|



### 60.9.15 Logic Inputs (LCIN) 

##### Offset 

|Register|Offset|
|---|---|
|LCIN|290h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2167 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

##### Function 

Indicates states of LC inputs. 

If you write to this register, LCU generates a bus transfer error. 

##### Diagram 

|Bits|31|30||29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||||0|||||||||
|W||||||||||||||||||
|Reset|0|0||0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14||13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||0||||||||LC_IN|PUTS||||||
|W||||||||||||||||||
|Reset|0|0||0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-12|Reserved|
|—||
|11-0|Logic Inputs|
|LC_INPUTS|Indicates states of LC inputs.|
||For each bit:|
||0b - 0|
||1b - 1|
||Mapping of bits: SeeMapping of 16-bit input, output, and state fields.|



### 60.9.16 Overridden Inputs (SWOUT) 

##### Offset 

|Register|Offset|
|---|---|
|SWOUT|294h|



##### Function 

Indicates states of LC inputs or states of software-overridden inputs, depending upon the state of the corresponding SWEN bit. If you write to this register, LCU generates a bus transfer error. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2168 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||0||||||||SWO|UT||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-12|Reserved|
|—<br>11-0|Overridden Inputs|
|SWOUT|Indicates states of LC inputs or software-overridden inputs.<br>For each bit, when the corresponding SWEN bit is 0:<br>0b - LC input is 0|
||1b - LC input is 1<br>For each bit, when the corresponding SWEN bit is 1:<br>0b - Software-overridden input is 0<br>1b - Software-overridden input is 1<br>Mapping of bits: SeeMapping of 16-bit input, output, and state fields.|



### 60.9.17 Logic Outputs (LCOUT) 

##### Offset 

|Register|Offset|
|---|---|
|LCOUT|298h|



##### Function 

Indicates states of LC outputs. 

If you write to this register, LCU generates a bus transfer error. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2169 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||0||||||||LCO|UT||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-12|Reserved|
|—||
|11-0|Logic Outputs|
|LCOUT|Indicates states of LC outputs.|
||For each bit:|
||0b - 0|
||1b - 1|
||Mapping of bits: SeeMapping of 16-bit input, output, and state fields.|



### 60.9.18 Forced Outputs (FORCEOUT) 

##### Offset 

|Register|Offset|
|---|---|
|FORCEOUT|29Ch|



##### Function 

Indicates the current state of the force outputs for all LCU logic outputs. Writing to this register generates a bus transfer error. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2170 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||0||||||||FORC|EOUT||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-12|Reserved|
|—||
|11-0|Forced Outputs|
|FORCEOUT|Indicates the current state of force outputs for the logic outputs.<br>For each bit:|
||0b - Not asserted|
||1b - Asserted|
||Mapping of bits: SeeMapping of 16-bit input, output, and state fields.|



### 60.9.19 Force Status (FORCESTS) 

##### Offset 

|Register|Offset|
|---|---|
|FORCESTS|2A0h|



Function See FORCESTS. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2171 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

##### Diagram 

|Bits|31|30||29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||||0|||||||||
|W||||||||||||||||||
|Reset|0|0||0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14||13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||0||||||||FORC|ESTS||||||
|W|||||||||||W1|C||||||
|Reset|0|0||0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-12|Reserved|
|—||
|11-0|Force Status|
|FORCESTS|Indicates the current force states of all LCs, mirrored fromLCn_STS[FORCESTS]. Change these bits to 0<br>by writing 1 to them or to the corresponding bit in the specificLCn_STSregister. This field allows you to<br>simultaneously change FORCESTS bits to 0 across multiple LCs.<br>For each bit:|
||0b - Not in force state|
||1b - Read: In force state — Write: Clear force state bit|
||Mapping of bits: SeeMapping of 16-bit input, output, and state fields.|



### 60.9.20 Debug Mode Enable (DBGEN) 

##### Offset 

|Register|Offset|
|---|---|
|DBGEN|2A8h|



##### Function 

Enables outputs to continue operation when the chip is in Debug mode. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2172 / 4640 

NXP Semiconductors 

Logic Control Unit (LCU) 

##### Diagram 

|Bits|31|30||29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||||0|||||||||
|W||||||||||||||||||
|Reset|0|0||0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14||13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||0||||||||DBG|EN||||||
|Reset|0|0||0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-12|Reserved|
|—||
|11-0|Debug Mode Enable|
|DBGEN|Enables outputs to continue operation in Debug mode.<br>For each bit:|
||0b - Inactive|
||1b - Continue normal operation|
||Mapping of bits: SeeMapping of 16-bit input, output, and state fields.|



## 60.10 Glossary 

CCW Counterclockwise CW Clockwise LC Logic cell LUT Lookup table 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2173 / 4640 

