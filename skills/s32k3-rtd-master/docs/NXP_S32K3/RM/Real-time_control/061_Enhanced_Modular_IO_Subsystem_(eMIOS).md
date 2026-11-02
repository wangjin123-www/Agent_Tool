NXP Semiconductors 

# Chapter 61 Enhanced Modular IO Subsystem (eMIOS) 

## 61.1 Chip-specific eMIOS information 

### 61.1.1 eMIOS configuration 

This chip has up to 3 instances of eMIOS that are each configured as shown in the following tables. 

Table 340. eMIOS instances 

|Instance|S32K314/S32K324/S32K344/S32K358|S32K311/S32K312/S32K322/S32K342|
|---|---|---|
|eMIOS_0|Yes|Yes|
|eMIOS_1|Yes|Yes|
|eMIOS_2|Yes|No|



Table 341. eMIOS configuration 

|Parameter|eMIOS_0|eMIOS_1|eMIOS_2|
|---|---|---|---|
|Timer width|16 bits|16 bits|16 bits|
|Number of channels|24|24|24|
|Channels configuration||See EMIOS channel configuration figure below||
|Local Channel prescaler width|4|4|4|
|Number of global<br>counter buses|2|2|2|
|Number of global prescaler|1|1|1|
|Global channel<br>prescaler width|8|8|8|



~~<mark>NOTE</mark>~~ eMIOS is clocked by CORE_CLK. 

### 61.1.2 Channel types 

The eMIOS contain 4 different types of channel, which are listed below. 

Table 342. eMIOS channel types 

|Mode Description|Name|Ch TypeX|Ch TypeY|Ch TypeG|Ch TypeH|
|---|---|---|---|---|---|
|General Purpose<br>Input / Output|GPIO|X|X|X|X|
|Single Action<br>Input Capture|SAIC|X|X|X|X|
|Single Action<br>Output Compare|SAOC|X|X|X|X|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2174 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

Table 342. eMIOS channel types (continued) 

|Mode Description|Name|Ch TypeX|Ch TypeY|Ch TypeG|Ch TypeH|
|---|---|---|---|---|---|
|Modulus Counter|MC|X||||
|Modulus Counter<br>Buffered<br>(Up / Down)|MCB|X||X||
|Input Pulse Width<br>Measurement|IPWM|||X|X|
|Input Period<br>Measurement|IPM|||X|X|
|Double Action<br>Output Compare|DAOC|||X|X|
|Output Pulse Width<br>and Frequency<br>Modulation<br>Buffered|OPWFMB|X||X||
|Center aligned<br>Output PWM<br>Buffered with<br>dead time|OPWMCB|||X||
|Output Pulse Width<br>Modulation<br>Buffered|OPWMB|X|X|X|X|
|Output Pulse Width<br>Modulation Trigger|OPWMT|X|X|X|X|
|Pulse<br>Edge Counting|PEC|||X||



###### ~~<mark>NOTE</mark>~~ 

ChType X and G has internal counters. 

Table 343. eMIOS channel configuration 

|Channel number|eMIOS0|eMIOS1|eMIOS2|
|---|---|---|---|
|CH0|X|X|X|
|CH8|X|X|X|
|CH16|X|X|X|
|CH22|X|X|X|
|CH23|X|X|X|
|CH1|G|H|H|
|CH2|G|H|H|
|CH3|G|H|H|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2175 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

Table 343. eMIOS channel configuration (continued) 

|CH4|G|H|H|
|---|---|---|---|
|CH5|G|H|H|
|CH6|G|H|H|
|CH7|G|H|H|
|CH9|H|H|H|
|CH10|H|H|H|
|CH11|H|H|H|
|CH12|H|H|H|
|CH13|H|H|H|
|CH14|H|H|H|
|CH15|H|H|H|
|CH17|Y|Y|Y|
|CH18|Y|Y|Y|
|CH19|Y|Y|Y|
|CH20|Y|Y|Y|
|CH21|Y|Y|Y|



### 61.1.3 Channel configuration 

The eMIOS channel configuration with respect to Type and Counter_bus is shown below. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2176 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2177-02.png)


<!-- Start of picture text -->
eMIOS_0 eMIOS_1 eMIOS_2<br>Ch0 Ch0 Ch0<br>Ch1 Ch1 Ch1<br>Ch2 Ch2 Ch2<br>Ch3 Ch3 Ch3<br>Ch4 Ch4 Ch4<br>Ch5 Ch5 Ch5<br>Ch6 Ch6 Ch6<br>Ch7 Ch7 Ch7<br>Ch8 Ch8 Ch8<br>Ch9 Ch9 Ch9<br>Ch10 Ch10 Ch10<br>Ch11 Ch11 Ch11<br>Ch12 Ch12 Ch12<br>Ch13 Ch13 Ch13<br>Ch14 Ch14 Ch14<br>Ch15 Ch15 Ch15<br>Ch16 Ch16 Ch16<br>Ch17 Ch17 Ch17<br>Ch18 Ch18 Ch18<br>Ch19 Ch19 Ch19<br>Ch20 Ch20 Ch20<br>Ch21 Ch21 Ch21<br>Ch22 Ch22 Ch22<br>Ch23 Ch23 Ch23<br>Chan Type_X Chan Type_Y Chan Type_G Chan Type_H<br>Counter_bus_B Counter_bus_B Counter_bus_B<br>Counter_bus_A Counter_bus_C Counter_bus_A Counter_bus_C Counter_bus_A Counter_bus_C<br>Counter_bus_F Counter_bus_D Counter_bus_F Counter_bus_D Counter_bus_F Counter_bus_D<br><!-- End of picture text -->

Figure 296. EMIOS channel types 

### 61.1.4 eMIOS disabling 

eMIOS can disable it's output using it's disable inputs. Disable inputs[3:0] are driven from the flag out bits[11:8]. 

||Disable inputs|
|---|---|
|eMIOS0 Output disable input[3:0]|trgmux_output[31:28]|
|eMIOS1 Output disable input[3:0]|trgmux_output[31:28]|
|eMIOS2 Output disable input[3:0]|trgmux_output[31:28]|



For details, see the TRGMUX connectivity file attached to this document. 

### 61.1.5 BCTU Interface 

Each eMIOS channel, with the exception of the main counterbus channel (ch[23]) is capable of triggering the BCTU. See BCTU chapter for mapping. BCTU allows triggering from as many eMIOS modes as possible. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2177 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

## 61.4 Introduction 

eMIOS provides independent channels, UCs, that you configure to generate or measure time events for different functions in different chip applications. 

eMIOS distributes these channels across a number of global and local counter buses. Each local bus is dedicated to a group of eight contiguous channels. Each channel can generate its own timebase, and each counter bus has its timebase provided by a dedicated channel. For a list of counter buses with their assigned channels and timebase sources, see Counter buses, channels, and timebase sources. 

## 61.5 Block diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2178-06.png)


<!-- Start of picture text -->
eMIOS<br>Bus D<br>IP<br>BIU All channels<br>interface<br>Channel 23 EMIOS[23]<br>Channel 22 EMIOS[22]<br>GTBE_OUT Global Channel 16 EMIOS[16]<br>registers<br>Bus C<br>Channel 15 EMIOS[15]<br>GTBE_IN All channels<br>Channel 8 EMIOS[8]<br>Bus B<br>System Global All channels<br>clock prescaler<br>Channel 7 EMIOS[7]<br>Channel 0 EMIOS[0]<br>Output disable inputs[3:0]<br>Global counter bus A<br>Output disable bus[3:0]<br>Second global counter bus F<br><!-- End of picture text -->

Figure 297. Block diagram 

## 61.6 Features 

- 24 UCs distributed across local counter buses as shown in Counter buses, channels, and timebase sources 

- Global counter bus A driven by UC23 

- Global counter bus F driven by UC22 

- Synchronized timebases shared through the counter buses 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2178 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

- Dedicated timebase for each channel, distinct from the counter buses 

- Global clock prescaler (GCP) 

- One CP per channel 

- Dedicated set of control and status registers for each UC 

- 16-bit–wide data registers 

- Shadow flag register (GFLAG) to access all channel flags with one read access 

- Ability to freeze the UC state for debug purposes 

- Motor control capability 

## 61.7 Functional description 

### 61.7.1 Reset 

eMIOS resets asynchronously. Reset affects all registers. 

On reset, UCs enter GPIO input mode. 

### 61.7.2 Counter buses, channels, and timebase sources 

Table 344. Counter buses, channels, and timebase sources 

|Counter bus|Channels|Timebase channel|
|---|---|---|
|Global bus A|All UCs|23|
|Local bus B|• UC0|0|
||• UC1<br>• UC2||
||• UC3||
||• UC4||
||• UC5||
||• UC6||
||• UC7||
|Local bus C|• UC8|8|
||• UC9||
||• UC10||
||• UC11||
||• UC12||
||• UC13||
||• UC14||
||• UC15||
|Local bus D|• UC16|16|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2179 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

Table 344. Counter buses, channels, and timebase sources (continued) 

|Counter bus|Channels|Timebase channel|
|---|---|---|
||• UC17||
||• UC18||
||• UC19||
||• UC10||
||• UC21||
||• UC22||
||• UC23||
|Global bus F|All UCs|22|



### 61.7.3 Unified channels (UC) 

#### 61.7.3.1 Overview 

Each UC contains the following: 

- Two double-buffered data registers, An and Bn, that allow up to two events—input capture, output compare, or both—to occur before software intervention is needed 

- Two comparators, A and B, that indicate when the selected counter bus is equal to the value in An and Bn 

- An internal counter (CNTn[C]) that runs in all modes except GPIO. 

You can use this counter as a local timebase or to count input events. You can use it as a timebase if CNTn[C] is not used in the current mode. 

- An output flip-flop that holds the logic level to be applied to the output pin 

- A status register, UC Status n (S0 - S23), that flags input capture and match events, indicates flag overruns and overflows, and shows the input and output pin states 

- A control register, UC Control n (C0 - C23), that controls UC operation 

You control the following operational characteristics for each UC: 

- The logic (Cn[MODE]) that specifies the behavior of the UC (see UC modes) 

- The counter bus (Cn[BSL]) that provides the timebase for all timing functions 

- The CP (Cn[UCPRE] and C2_n[UCEXTPRE]) 

- The minimum input pulse width (Cn[IF]) for the input filter that determines valid pin transitions 

- Which input edges to detect (Cn[EDSEL]) 

- Which of four output disable input signals (Cn[ODISSL]) to use for disabling outputs 

- For all output modes except GPIO, whether to disable the output flip-flop (Cn[ODIS]) 

UC block diagram illustrates the basic UC architecture. 

For a list of counter buses and their assigned channels and timebase sources, see Counter buses, channels, and timebase sources. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2180 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.2 UC block diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2181-03.png)


<!-- Start of picture text -->
UC<br>Clock Programmable<br>prescaler filter<br>UC datapath<br>UC control Comparators A and B<br>CPU Mode logic<br>DMA<br>Counter bus<br>Global counter bus A Second global counter bus F Local counter B, C, D, or E Internal counter<br><!-- End of picture text -->

Figure 298. UC block diagram 

#### 61.7.3.3 Buffered modes 

To provide smooth waveform generation even when An[A] and Bn[B] are changing, the following modes double buffer the An and Bn registers: 

- Modulus Counter Buffered (MCB) mode 

- Output Pulse Width and Frequency Modulation Buffered (OPWFMB) mode 

- Output PWM Buffered (OPWMB) mode 

These modes appear in separate sections because there are several basic differences in UC operation between them and their corresponding nonbuffered modes. 

#### 61.7.3.4 UC control and datapath 

As illustrated in UC control and datapath diagram, the UC contains control and datapath subblocks. 

The control subblock generates signals to control the multiplexers in the datapath subblock. eMIOS implements each UC mode in dedicated logic independent from the other modes. The UC modes share a set of registers allowing the storing of sequential events. 

The datapath block contains the channel A and B registers, the internal timebase, and the comparators. Multiplexers receive inputs from the control subblock to configure the datapath for the specific channel modes. This configuration consists of selecting the input of comparators and data for the register inputs. The outputs of the A and B comparators connect to the control block. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2181 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.5 UC control and datapath diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2182-03.png)


<!-- Start of picture text -->
Input<br>Input<br>filter<br>MODE<br>register Mode 0 Mode 1 Mode n<br>logic logic logic<br>MODE<br>decoder<br>General<br>purpose<br>registers<br>uc_ctrl<br>Global counter bus[A]<br>BSL[1]+logic<br> 2nd global counter bus[F]<br>Local counter bus[B/C/D/E]<br>==<br>BSL[1:0 or 0:1] lnternal<br>counter<br>A Comparator<br>AS2<br>CNT AS1<br>BSL[1]+logic<br>BS1<br>BS2 B Comparator<br>==<br>BSL[1]+logic<br>uc_datapath<br>Control signals<br><!-- End of picture text -->

Figure 299. UC control and datapath diagram 

#### 61.7.3.6 UC modes 

You can configure UCs to operate in the following modes: 

- General-Purpose Input and Output (GPIO) mode 

- Single Action Input Capture (SAIC) mode 

- Single Action Output Capture (SAOC) mode 

- Input Pulse Width Measurement (IPWM) mode 

- Input Period Measurement (IPM) Mode 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2182 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

- Double Action Output Compare (DAOC) mode 

- Pulse Edge Counting (PEC) mode 

- Modulus Counter (MC) mode 

- Modulus Counter Buffered (MCB) mode 

- Output Pulse Width and Frequency Modulation Buffered (OPWFMB) mode 

- Center Aligned Output PWM with Dead Time Insertion Buffered (OPWMCB) mode 

- Output PWM Buffered (OPWMB) mode 

- Output PWM with Trigger (OPWMT) mode 

Each channel supports a specific subset of these modes. See the chip-configuration information to see which modes each channel supports. 

#### 61.7.3.7 General-Purpose Input and Output (GPIO) mode 

#### 61.7.3.7.1 Overview 

This mode disables all UC input-capture and output-compare functions, and resets and disables the internal counter (Cn[C]). All control fields remain accessible. 

To change the UC from one operation mode to another, you must first change to GPIO mode and then change to the desired final mode. To prepare the UC for a new operation mode, you must configure AS1, BS1, AS2, and BS2 before exiting GPIO mode and entering the desired final mode (see AS1, AS2, BS1, and BS2 shadow registers). Specifically: 

- Writing to An[A] stores the same value in AS1 and AS2. 

- Writing to Bn[B] stores the same value in BS1 and BS2. 

- Writing to ALTAn[ALTA] stores a value only in AS2. 

As its name implies, GPIO mode supports both input and output submodes. See Differences for input and output submodes. 

#### 61.7.3.7.2 Differences for input and output submodes 

Table 345. Differences for input and output submodes 

|Submode|To enter submode, write this<br>value toCn[MODE]|Characteristics|
|---|---|---|
|Input|0|• You control the generation of input-capture flags withCn[EDPOL]<br>andCn[EDSEL].|
|||• You can determine the input pin status by readingSn[UCIN].|
|Output|1|• The UC performs as a single output port pin.|
|||• The value ofCn[EDPOL]permanently drives the output flip-flop.|



#### 61.7.3.8 Single Action Input Capture (SAIC) mode 

#### 61.7.3.8.1 Overview 

In this mode, when a triggering event occurs on the input pin, eMIOS: 

- Captures the selected timebase into AS2 

- Changes Sn[FLAG] to 1 to indicate that an input capture has occurred 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2183 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

An[A] returns the value of AS2. As soon as the UC enters SAIC mode after exiting GPIO mode, the channel is ready to capture events. 

eMIOS captures the events as soon as they occur. Therefore, reading An[A] always returns the value of the latest captured event. Subsequent capture events occur regardless of whether you read the previous event from An[A]. Each new capture event sets the input capture flag (writes 1 to Sn[FLAG]). 

The input capture is triggered by an edge transition on the input pin as configured by Cn[EDPOL] and Cn[EDSEL]. 

SAIC with rising edge triggering and SAIC with both edges triggering show how to use the UC for input capture. 

#### 61.7.3.8.2 SAIC submodes and MODE field values 

Table 346. SAIC submodes and MODE field values 

|Capture behavior|Cn[MODE](binary)|
|---|---|
|The UC only captures the timestamp.|000_0010|
|• The UC captures a timestamp.|100_0010|
|• AS2 bit 0 indicates the input signal level.||



#### 61.7.3.8.3 Effect of Cn[EDPOL] on edge capturing 

Table 347. Effect of Cn[EDPOL] on edge capturing 

|Cn[EDPOL]|Input signal transition|Resulting value of AS2 bit0|
|---|---|---|
|0|0→1|0|
||1→0|1|
|1|0→1|1|
||1→0|0|



#### 61.7.3.8.4 SAIC with rising edge triggering 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2184-13.png)


<!-- Start of picture text -->
C n [EDSEL] = 0<br>C n [EDPOL] = 1 Edge detect Edge detect Edge detect<br>Input signal (after input filter)<br>Selected counter bus 500h 1000h 1100h 1250h 1525h 16A0h<br>Flag output and S n [FLAG]<br>AS2 (captured; read in A n ) 0xxxxxx 1000h 1250h 16A0h<br>Figure 300. SAIC with rising edge triggering<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2184 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.8.5 SAIC with both edges triggering 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2185-03.png)


<!-- Start of picture text -->
C n [EDSEL] = 1<br>Edge detect Edge detect Edge detect<br>C n [EDPOL] = x<br>Input signal (after input filter)<br>Selected counter bus 1000h 1001h 1102h 1103h 1104h 1105h 1106h 1107h 1108h<br>Flag set event<br>Flag output and S n [FLAG]<br>Flag clear<br>AS2 (captured; read from A n ) 0xxxxxx 1000h 1103h 1108h<br><!-- End of picture text -->

Figure 301. SAIC with both edges triggering 

#### 61.7.3.9 Single Action Output Capture (SAOC) mode 

#### 61.7.3.9.1 Overview 

In this mode, eMIOS loads a match value into AS2 and then immediately transfers it to AS1 for comparison with the selected timebase. When an output-compare match occurs, eMIOS: 

- Either toggles the output flip-flop or transfers Cn[EDPOL] to the output flip-flop, as determined by Cn[EDSEL]. 

- Sets the input capture flag (changes Sn[FLAG] to 1). 

Along with the match, Sn[FLAG] becomes 1 to indicate that the output-compare match has occurred. Writing to An[A] stores the value in AS2, and reading An[A] returns the AS1 value. 

The channel internal counter in SAOC mode is free-running. It starts counting as soon as the UC enters SAOC mode. 

You can force an output-compare match by writing 1 to Cn[FORCMA]. A forced output-compare match does not set the input capture flag (Sn[FLAG]). 

When the UC enters SAOC mode after exiting GPIO mode, the output flip-flop value becomes the complement of Cn[EDPOL]. 

You select the internal or external counter bus with Cn[BSL]. 

SAOC with Cn[EDPOL] transferred to the output flip-flop shows how to perform a single output compare and transfer Cn[EDPOL] to the output flip-flop. 

SAOC toggling the output flip-flop shows how to perform a single output compare and toggle the output flip-flop at each match. 

#### 61.7.3.9.2 Preload the desired match value 

eMIOS enables matches immediately after the UC enters SAOC mode. Therefore, you must write the desired match value to AS1 before the UC enters SAOC mode. You can update AS1 at any time. This modifies the match value reflected in the channel-generated output signal. Subsequent capture events occur regardless of whether you write to An[A] again. Each new capture event sets the input capture flag (Sn[FLAG]). See SAOC with flag behavior. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2185 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.9.3 SAOC with Cn[EDPOL] transferred to the output flip-flop 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2186-03.png)


<!-- Start of picture text -->
C n [EDSEL] = 0 Update AS1 AS1 match AS1 match AS1 match<br>C n [EDPOL] = 1<br>Output flip-flop<br>Selected counter bus 500h 1000h 1100h 1000h 1100h 1000h<br>Flag  output and S n [FLAG]<br>AS1 (read from A n ) 0xxxxxx 1000h 1000h 1000h 1000h<br>AS2 = AS1 according to the OUDIS[OU n ] field<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2186-04.png)


<!-- Start of picture text -->
Figure 302. SAOC with Cn[EDPOL] transferred to the output flip-flop<br><!-- End of picture text -->

#### 61.7.3.9.4 SAOC toggling the output flip-flop 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2186-06.png)


<!-- Start of picture text -->
C n [EDSEL] = 1 Update AS1 AS1 match AS1 match AS1 match<br>C n [EDPOL] = x<br>Output flip-flop<br>Selected counter bus 500h 1000h 1100h 1000h 1100h 1000h<br>Flag output and S n [FLAG]<br>AS1 (read from A n ) 0xxxxxx 1000h 1000h 1000h 1000h<br>AS2 = AS1 according to the OUDIS[OU n ] field<br>Figure 303. SAOC toggling the output flip-flop<br><!-- End of picture text -->

#### 61.7.3.9.5 SAOC with flag behavior 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2186-08.png)


<!-- Start of picture text -->
C n [EDSEL] = 1 Output flip-flop<br>C n [EDPOL] = X<br>Selected counter bus 0h 1h 2h 0h 1h 2h 0h 1h 2h<br>System clock<br>AS1 match<br>Flag set event<br>Flag output and S n [FLAG]<br>Flag clear<br>AS2 (write to A n ) 1h<br>Figure 304. SAOC with flag behavior<br><!-- End of picture text -->

#### 61.7.3.10 Input Pulse Width Measurement (IPWM) mode 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2186 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.10.1 Overview 

This mode allows you to measure the width of a positive or negative pulse. Select whether to measure from the rising or falling edge with Edge Polarity (Cn[EDPOL]). 

The first leading edge: 

- Triggers the first input capture, which latches the count value of the selected timebase into BS2 (see AS1, AS2, BS1, and BS2 shadow registers) 

- Does not set the input-capture flag (Sn[FLAG]) 

- Enables AS2 capture 

The next trailing edge: 

- Latches the selected timebase into AS2 

- Sets the input-capture flag (Sn[FLAG]) 

- Transfers BS2 to BS1 and AS1 

eMIOS captures successive values on consecutive edges of opposite polarity. If you initiate subsequent input capture events while the input-capture flag (Sn[FLAG]) is set, eMIOS updates AS2, BS1, and AS1 with the latest captured values and keeps the flag set. 

#### 61.7.3.10.2 Coherency 

Reading An[A] updates BS1 with AS1. It also disables transfers from BS2 and BS1 until the next read of Bn[B]. 

Reading Bn updates BS1 with AS1. It also re-enables transfers from BS2 to BS1, which takes effect at the next trailing edge capture. 

Because transfers from BS2 to AS1 are never blocked, to guarantee data coherency you must read An, then read Bn. 

If you do not require coherent data, you should read Bn before you read An, although doing so requires a second read of Bn to unblock BS1 updates. 

#### 61.7.3.10.3 Timing example: measure pulse width 

This figure shows how to measure the input pulse width by subtracting BS1 from AS2. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2187-20.png)


<!-- Start of picture text -->
BS2 AS2 BS2 AS2 BS2<br>C n [EDPOL] = 1<br>Input signal (after input filter)<br>Selected counter bus 500h 1000h 1100h 1250h 1525h 16A0h<br>Flag output and S n [FLAG]<br>AS2 (read from A n ) 0xxxxxx 1100h 1525h<br>BS2 0xxxxxx 1000h 1250h 16A0h<br>AS1 0xxxxxx 1000h 1250h<br>BS1 (read from B n ) 0xxxxxx 1000h 1250h<br><!-- End of picture text -->

Figure 305. Timing example: measure pulse width 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2187 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.10.4 Timing example: AS1 and BS1 updates on channel reads 

This example illustrates AS1 and BS1 updates when you read An[A] and Bn[B]. AS1 always has coherent data related to AS2 (see Coherency). 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2188-04.png)


<!-- Start of picture text -->
Read A n Read B n<br>C n [EDPOL] = 1 BS2 AS2 BS2 AS2 BS2<br>Input signal (after input filter)<br>Selected counter bus 500h 1000h 1100h 1250h 1525h 16A0h<br>Flag output and S n [FLAG]<br>AS2 (read from A n ) 0xxxxxx 1100h 1525h<br>BS2 0xxxxxx 1000h 1250h 16A0h<br>AS1 0xxxxxx 1000h 1250h<br>BS1 (read from B n ) 0xxxxxx 1000h 1000h 1250h<br><!-- End of picture text -->

Figure 306. Timing example: BS1 and AS1 updates on channel reads 

#### 61.7.3.11 Input Period Measurement (IPM) Mode 

#### 61.7.3.11.1 Overview 

This mode allows you to measure the period of an input signal. Select whether to measure from the rising or falling edges with Edge Polarity (Cn[EDPOL]). 

The first edge of selected polarity: 

- Latches the selected timebase into AS2 and BS2 (see AS1, AS2, BS1, and BS2 shadow registers) 

- Transfers BS2 to BS1 

- Does not set the input-capture flag (Sn[FLAG]) 

The second edge of the same polarity: 

- Latches the counter bus value into AS2 and BS2 

- Transfers BS2 to BS1 and AS1 

- Sets the input-capture flag (Sn[FLAG]) 

eMIOS repeats this process for each subsequent capture. 

eMIOS captures successive values on two consecutive edges of the same polarity. The measured input signal must have a period of at least four system clock cycles to be properly captured by the synchronization logic at the channel input, even if the input filter is in bypass mode. 

#### 61.7.3.11.2 Coherency 

Reading An[A] updates BS1 with AS1, which provides coherent data in AS2 and BS1 (see Timing example: AS1 and BS1 updates on channel reads). It also disables transfers from BS2 and BS1 until the next read of Bn[B]. 

Reading Bn[B] updates BS1 with AS1. It also re-enables transfers from BS2 to BS1, which takes effect at the next edge capture. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2188 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.11.3 Timing example: measure input period 

This example illustrates how to measure the input period by subtracting BS1 from AS2. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2189-04.png)


<!-- Start of picture text -->
A A A<br>C n [EDPOL] = 1<br>Input signal (after input filter)<br>Selected counter bus 500h 1000h 1100h 1250h 1525h 16A0h<br>Flag output and S n [FLAG]<br>AS2 (read from A n ) 0xxxxxx 1000h 1250h 16A0h<br>BS2 0xxxxxx 1000h 1250h 16A0h<br>AS1 0xxxxxx 1000h 1250h<br>BS1 (read from B n ) 0xxxxxx 1000h 1250h<br><!-- End of picture text -->

Figure 307. Timing example: measure input period 

#### 61.7.3.11.4 Timing example: AS1 and BS1 updates on channel reads 

This diagram illustrates AS1 and BS1 updates when you read An[A] and Bn[B]. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2189-08.png)


<!-- Start of picture text -->
Read A n Read B n<br>C n [EDPOL] = 1 A A A<br>Input signal (after input filter)<br>Selected counter bus 500h 1000h 1100h 1250h 1525h 16A0h<br>Flag output and S n [FLAG]<br>AS2 (read from A n ) 0xxxxxx 1000h 1250h 16A0h<br>BS2 0xxxxxx 1000h 1250h 16A0h<br>AS1 0xxxxxx 1000h 1250h<br>BS1 (read from B n ) 0xxxxxx 1000h 1000h 1250h<br>Figure 308. Timing example: AS1 and BS1 updates on channel reads<br><!-- End of picture text -->

#### 61.7.3.12 Double Action Output Compare (DAOC) mode 

#### 61.7.3.12.1 Overview 

In this mode, matches on comparators A and B cause the UC to generate the leading and trailing edges of the variable pulse width output. See DAOC submodes and MODE field values. There is no restriction on the order in which A and B matches occur. 

When the UC enters DAOC mode from GPIO mode, eMIOS disables both comparators and drives the complement of Edge Polarity (Cn[EDPOL]) onto the output flip-flop. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2189 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.12.2 DAOC submodes and MODE field values 

Table 348. DAOC submodes and MODE field values 

|When set flag event occurs|Cn[MODE](binary)|
|---|---|
|Only on B matches|000_0110|
|On A or B matches|000_0111|



#### 61.7.3.12.3 Data transfer and compare 

If you enable output (write 0 to OUDIS[OUn]), on the next clock cycle the UC transfers AS2 and BS2 to AS1 and BS1 respectively (see Timing example: leading dead time insertion). If you disable output (write 1 to OUDIS[OUn]), no transfer occurs. 

eMIOS enables and disables the A and B comparators independently. It enables comparator A only after the transfer to AS1 completes, and disables comparator A on the next A match. Similarly, eMIOS enables comparator B only after the transfer to BS1 completes, and disables comparator B on the next B match. 

When a match occurs on comparator A, the output flip-flop acquires the value of Edge Polarity (Cn[EDPOL]). When a match occurs on comparator B, the output flip-flop acquires the complement of Edge Polarity (Cn[EDPOL]). 

#### 61.7.3.12.4 Differences between flag on A match and flag on A and B matches 

In the flag on B match submode (see DAOC submodes and MODE field values), the UC sets the input-capture flag (Sn[FLAG]) only for matches on the B comparator. In the flag on both A and B matches submode, it sets the flag for matches on either comparator. 

If subsequent enabled output compares occur on AS1 or BS1, the UC continues generating pulses regardless of the flag state. 

If you load both AS1 and BS1 with the same value, the B match takes precedence and the UC drives the complement of Edge Polarity (Cn[EDPOL]) onto the output flip-flop. 

#### 61.7.3.12.5 Forced operation by Cn[FORCMA] and Cn[FORCMB] 

Force Match A (Cn[FORCMA]) and Force Match B (Cn[FORCMB]) allow you to force the output flip-flop to the level corresponding to the comparator, Edge Polarity (Cn[EDPOL]) for an A match, or the complement of Edge Polarity for a B match. The force-match operations do not set the input-capture flag (Sn[FLAG]). 

#### 61.7.3.12.6 Timing example: flag on both matches 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2190-16.png)


<!-- Start of picture text -->
Update to<br>AS1 and BS1 AS1 match BS1 match AS1 match BS1 match<br>Output flip-flop<br>Selected counter bus 500h 1000h 1100h 1000h 1100h<br>Input capture flag<br>(Sn[FLAG])<br>AS1 (read from An) 0xxxxxx 1000h 1000h 1000h<br>BS1 (read from Bn) 0xxxxxx 1100h 1100h 1100h<br>AS2 mirrors AS1 if OUDIS[OUn] = 0<br>BS2 mirrors BS1 if OUDIS[OUn] = 0<br><!-- End of picture text -->

Figure 309. Timing example: flag on both matches 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2190 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2191-01.png)


<!-- Start of picture text -->
Enhanced Modular IO Subsystem (eMIOS)<br><!-- End of picture text -->

#### 61.7.3.12.7 Timing example: flag on second match 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2191-03.png)


<!-- Start of picture text -->
Update to<br>AS1 and BS1 AS1 match BS1 match AS1 match BS1 match<br>Output flip-flop<br>Selected counter bus 500h 1000h 1100h 1000h 1100h<br>Input capture flag<br>(Sn[FLAG])<br>AS1 (read from An) 0xxxxxx 1000h 1000h 1000h<br>BS1 (read from Bn) 0xxxxxx 1100h 1100h 1100h<br>AS2 mirrors AS1 if OUDIS[OUn] = 0<br>BS2 mirrors BS1 if OUDIS[OUn] = 0<br>Figure 310. Timing example: flag on second match<br><!-- End of picture text -->

#### 61.7.3.12.8 Timing example: transfer disabling 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2191-05.png)


<!-- Start of picture text -->
Write to AS2 Write to AS2 Write to AS2<br>Write to BS2 Write to BS2 Write to BS2<br>C n [EDSEL] = x<br>Output flip-flop<br>C n [EDPOL] = 1<br>Selected counter bus 0h 1h 2h 0h 1h 2h 0h 1h 2h<br>System clock<br>Enabled AS1 match<br>Enabled BS1 match<br>Flag set event<br>Flag output and S n [Flag]<br>Flag clear<br>OUDIS[OU n ]<br>AS1 (read from A n ) 1h 1h 1h<br>AS2 (write to A n ) 1h 1h 1h<br>BS1 (read from B n ) 2h 2h 2h<br>BS2 (write to B n ) 2h 2h 2h<br>Figure 311. Timing example: transfer disabling<br><!-- End of picture text -->

61.7.3.13 Pulse Edge Counting (PEC) mode 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2191 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.13.1 Overview 

This mode counts the number of pulses or edges detected on the input for a desired time window. Cn[EDSEL] and Cn[EDPOL] determine which edges the UC counts. 

Specify the window start time in AS1 and the end time in BS1. After you write to AS1, when the selected timebase matches comparator A, eMIOS resets the internal counter and starts counting input events. When the timebase matches comparator B, eMIOS: 

- Disables the internal counter. 

- Transfers the counter's content to AS2. 

- Sets the input-capture flag (changes Sn[FLAG] to 1). 

You obtain the number of detected pulses by reading Cn[C] or AS2. 

Timing example continuous and Timing example single-shot show how to use the UC in continuous or single-shot operation. 

#### 61.7.3.13.2 PEC submodes and MODE field values 

Table 349. PEC submodes and MODE field values 

|Operation|Cn[MODE](binary)|
|---|---|
|Continuous; the next match between comparator A and the selected timebase<br>resets the internal counter and enables counting again. To guarantee coherent<br>measurements when you readCn[C]afterSn[FLAG]becomes 1, you must check<br>if the timebase value is out of the time interval defined by AS1 and BS1.<br>Alternately, AS2 (available inALTAn[ALTA]) always holds the latest available<br>measurement, providing coherent data at any time after the first set-flag event.|000_1010|
|Single-shot; The next match between comparator A and the selected timebase<br>has no effect until you write toAn[A]. eMIOS also transfers theCn[C]value to AS2<br>when a match in the B comparator occurs.|000_1011|



#### 61.7.3.13.3 Timing example continuous 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2192-14.png)


<!-- Start of picture text -->
Write to AS1 and BS1 BS1 match BS1 match<br>CNT n AS1 match AS1 match<br>Number of events detected<br>Number of events detected<br>0h Time<br>Flag output and S n [FLAG]<br>Selected counter bus 90h 303h 90h 303h<br>AS1 (write to A n ) 90h 90h 90h<br>BS1 (write to B n ) 303h 303h 303h<br>AS2 (read from ALTA n ) CNT n AS2 CNT n AS2<br><!-- End of picture text -->

Figure 312. Timing example continuous 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2192 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.13.4 Timing example single-shot 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2193-03.png)


<!-- Start of picture text -->
Write to AS1 and BS1 BS1 match BS1 match<br>CNT n AS1 match AS1 match<br>Number of events detected<br>Number of events detected<br>0h Time<br>Flag output and S n [FLAG]<br>Selected counter bus 90h 303h 90h 303h<br>AS1 (write to A n ) 90h 90h 90h<br>BS1 (write to B n ) 303h 303h 303h<br>AS2 (read from ALTA n ) CNT n AS2 CNT n AS2<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2193-04.png)


<!-- Start of picture text -->
Figure 313. Timing example single-shot<br><!-- End of picture text -->

#### 61.7.3.14 Modulus Counter (MC) mode 

#### 61.7.3.14.1 Overview 

In this mode, the UC produces a timebase for a counter bus or as a general purpose timer. The internal counter (Cn[C]) counts up from the current value until it matches AS1. 

Selecting external clock source (see MC submodes and MODE field values) causes the UC to uses the input signal pin as the source. You select the triggering polarity edge using Edge Polarity (Cn[EDPOL]) and Edge Select (Cn[EDSEL]). 

You must write only non-zero values to An[A]. Writing to An[A] or the internal counter may cause a match to be missed and the counter to roll over and resume operation in the next cycle. The channel writes 0 to BS1, which is not accessible by the MCU. You can read and write BS2, but it is not used in this mode. 

#### 61.7.3.14.2 MC submodes and MODE field values 

Table 350. MC submodes and MODE field values 

|Submode or function|Cn[MODE](binary)|
|---|---|
|Internal clock source|001_0pp0<sup>1</sup>|
|External clock source|001_0pp1<sup>1</sup>|
|Internal counter reset on match start|001_0p0p<sup>1</sup>|
|Internal counter reset on match end|001_0p1p<sup>1</sup>|
|Up Count|001_00pp<sup>1</sup>|
|Up Count-Down Count|001_01pp<sup>1</sup>|



1. p = Adjust parameters for submodes and options. See Unified channels (UC). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2193 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.14.3 Up Count submode 

Table 351. Up Count submode operation 

|Counter reset timing<sup>1</sup>||Cn[MOD|E]|
|---|---|---|---|
||Bit 1|External clock (Bit 0 = 1)|Internal clock (Bit 0 = 0)|
|Reset on match start|0|When the AS1 match occurs, the UC:<br>• Writes 0 to the internal counter.<br>• Sets the input-capture flag<br>(Sn[FLAG]).<br>• Increments the internal counter at the<br>next input event, resulting in a short<br>zero count.|When the AS1 match occurs, the UC:<br>• Writes 0 to the internal counter.<br>• Sets the input-capture flag<br>(Sn[FLAG]).<br>• Maintains the internal counter at 0 on<br>the next prescaler tick after the match.<br>• Resumes counting on the next<br>prescaler tick.|
|||SeeTimebase with the fastest prescaler rat<br>match start and internal clock.|ioandTimebase generation with clear on|
|Clear on match end|1|When the next input event after the AS1<br>match occurs, the UC:<br>• Writes 0 to the internal counter.<br>• Sets the input-capture flag<br>(Sn[FLAG]).|When the next internal counter tick after the<br>AS1 match occurs, the UC:<br>• Writes 0 to the internal counter.<br>• Sets the input-capture flag<br>(Sn[FLAG]).|
|||SeeTimebase with the fastest prescaler rat<br>match end.|ioandTimebase generation with clear on|



1. If you select internal clock source and a prescaler value of 1 for the internal counter, the behavior is the same for both submodes. 

See Timing example: Up Count submode. 

#### 61.7.3.14.4 Timing example: Up Count submode 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2194-08.png)


<!-- Start of picture text -->
Match AS1 Match AS1 Match AS1 Match AS1<br>CNT n Write to AS2 Write to AS2<br>FF_FFFFh<br>303h<br>200h<br>0h Time<br>Flag output and S n [FLAG]<br>AS1 (read from A n ) 0xxxxxx 303h 303h 303h 200h 200h<br>Figure 314. Timing example: Up Count submode<br><!-- End of picture text -->

#### 61.7.3.14.5 Up Count-Down Count submode operation 

In Up Count-Down Count submode: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2194 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

- When the internal counter matches AS1, the counter begins decrementing and the UC sets the input-capture flag (Sn[FLAG]). 

- When the internal counter matches BS1, the counter begins incrementing and, if in clear on match end operation (Cn[1] = 1), the UC sets the input-capture flag (Sn[FLAG]). 

See Timing example: Up Count-Down Count submode. 

#### 61.7.3.14.6 Timing example: Up Count-Down Count submode 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2195-06.png)


<!-- Start of picture text -->
Match AS1 Match BS1 (= 0) Match AS1 Match BS1 (= 0)<br>CNT n Write to AS2 Write to AS2<br>FF_FFFFh<br>303h<br>200h<br>0h Time<br>AS1 (read from A n ) 0h 303h 303h 200h 200h 200h<br>Flag output and S n [FLAG]<br><!-- End of picture text -->

Figure 315. Timing example: Up Count-Down Count submode 

#### 61.7.3.14.7 Up Count with delayed reload operation 

When the internal counter matches AS1 in the Up Count submode or BS1 in the Up Count-Down Count submode, the UC asserts the counter bus reload signal. You can read the counter bus reload signal in the following modes: 

- Output PWM Buffered (OPWMB) mode 

- Output Pulse Width and Frequency Modulation Buffered (OPWFMB) mode 

- Center Aligned Output PWM with Dead Time Insertion Buffered (OPWMCB) mode 

You can use the Reload Signal Output Delay Interval (C2n[UCRELDEL_INT]) to cause the UC to assert the reload signal only after a specified number of match events (from 2 to 32). 

See Timing example: Up Count mode with delayed reload. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2195 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.14.8 Timing example: Up Count mode with delayed reload 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2196-03.png)


<!-- Start of picture text -->
CNT n<br>Match AS1<br>6h<br>Write to AS2<br>4h<br>1h<br>Time<br>AS2 6h<br>AS1 4h<br>AS1 or BS1 reload signal or cb_reload_n<br>C2_ n [UCRELDEL_INT] = 1b<br>AS1 or BS1 reload signal or cb_reload_n<br>C2_ n [UCRELDEL_INT] = 11b<br>AS1 or BS1 reload signal or cb_reload_n<br>C2_ n [UCRELDEL_INT] = 0b<br><!-- End of picture text -->

Figure 316. Timing example: Up Count mode with delayed reload 

#### 61.7.3.15 Modulus Counter Buffered (MCB) mode 

#### 61.7.3.15.1 Overview 

In this mode, the UC generates a timebase that can be shared with other channels through the internal counter buses. AS1 is double-buffered, so you can change AS2 at any time with smooth transitions. The UC updates AS1 at the counter period boundary, which is when the internal counter (CNTn[C]) transitions to 1h. 

Selecting external clock (see MCB submodes and MODE field values) causes the UC to use the input signal as the source. You select the triggering edge with Edge Polarity (Cn[EDPOL]) and Edge Select (Cn[EDSEL]). 

You must ensure the internal counter is in the range from 1h to the AS1 value; otherwise, the An[A] match does not occur and this causes the internal counter to wrap at the maximum counter value (FFFFh for a 16-bit counter). After a counter wrap occurs, the UC resets the counter to 1h and resumes normal operation. 

~~<mark>NOTE</mark>~~ 

Do not write 1h to the internal counter when the UC is in Freeze state. Doing so can cause the match to be missed 

and the counter to overflow. 

#### 61.7.3.15.2 MCB submodes and MODE field values 

Table 352. MCB submodes and MODE field values 

|Submode or function|Cn[MODE](binary)|
|---|---|
|Internal clock source|101_0pp0b<sup>1</sup>|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2196 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

Table 352. MCB submodes and MODE field values (continued) 

|Submode or function|Cn[MODE](binary)|
|---|---|
|External clock source|101_0pp1b<sup>1</sup>|
|Up Count|101_000p<sup>1</sup>|
|Reserved|101_001p<sup>1</sup>|
|Up Count-Down Count|101_01pp<sup>1</sup>|
|Flag set only on match start|101_010p<sup>1</sup>|
|Flags also set at counter period boundary|101_011p<sup>1</sup>|



1. p = Adjust parameters for submodes and options. See Unified channels (UC). 

#### 61.7.3.15.3 Up Count submode 

In the Up Count submode: 

- The internal counter (CNTn[C]) starts counting up (incrementing) from its current value. 

- When the internal counter matches AS1 and a clock tick occurs (either prescaled clock or input pin event), the UC resets the internal counter to 1h. 

- The UC sets the input-capture flag (Sn[FLAG]) one system clock cycle after the match occurs. 

You must write only values greater than 1h to AS1. 

The boundary between counter period n and period n+1 occurs when the UC changes the internal counter from the AS1 value in period n to 1h in period n+1. AS1 defines the counter period. 

The UC asserts the AS1 load signal (which has a duration of one system clock cycle) at the last system clock cycle of a counter period. This causes the UC to update AS1 with AS2 at the period boundary, at the same time that it resets the counter to 1h. Therefore, any value you write to AS2 during period n updates AS1 at the next period boundary and the UC uses it in period n+1. See Timing example: Up Count submode. 

You can use Output Update Disable (OUDIS) to delay the update of AS1 for synchronization. 

The UC sets the input-capture flag (Sn[FLAG]) at the period boundary. See Timing example: Up Count submode flag assertion. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2197 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.15.4 Timing example: Up Count submode 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2198-03.png)


<!-- Start of picture text -->
Counter period  n Counter period Counter period  n +2<br>n +1<br>Match AS1 Match AS1 Match AS1<br>Internal counter Write to AS2 Write to AS2<br>8<br>8h<br>6<br>6h<br>4<br>4h<br>2h<br>1h Time<br>Counter = AS1<br>AS1 load signal<br>AS1 value 8h 4h 6h<br>AS2 value 8h 4h 6h<br>Prescaler ratio = 2<br>Figure 317. Timing example: Up Count submode<br><!-- End of picture text -->

#### 61.7.3.15.5 Timing example: Up Count submode flag assertion 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2198-05.png)


<!-- Start of picture text -->
Counter period  n Counter period  n +1 Counter period  n +2<br>Match AS1 Match AS1 Match AS1<br>CNT n Write to AS2 Write to AS2<br>7h<br>6h<br>5h<br>1h Time<br>Flag set event<br>Flag output and Sn[FLAG]<br>Flag clear<br>AS2 5h 7h<br>AS1 6h 5h 7h 7h<br>Prescaler ratio = 1<br><!-- End of picture text -->

Figure 318. Timing example: Up Count submode flag assertion 

#### 61.7.3.15.6 Up Count-Down Count submode 

In Up Count-Down Count submode: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2198 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

- The counter period is: (2 x AS1) – 2. The counter changes direction at AS1 match and counts down (decrements) until it reaches 1h, then counts up (increments) again. 

- BS1 generates a match to start the internal counter incrementing, and BS1 cannot be changed in this submode. 

The UC updates AS1 at the counter period boundary. If you write AS2 (write An[A]) during period n, the UC uses this new value in period n+1 for AS1 match. You can disable updates of AS1 (OUDIS[OUn]). See Timing example: Up Count-Down Count submode. 

The UC sets the input-capture flag (Sn[FLAG]) at AS1 match start, and may also do so at the period boundary. See Overview and Timing example: Up Count-Down Count submode flag assertion. 

#### 61.7.3.15.7 Timing example: Up Count-Down Count submode 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2199-07.png)


<!-- Start of picture text -->
Counter period  n Counter period  n +1 Counter period  n +2<br>Match AS1 Match AS1<br>CNT n Write to AS2 Write to AS2<br>6h<br>5h<br>1h Time<br>Counter = 2<br>AS1 load signal<br>AS1 6h 5h 6h<br>AS2 6h 5h 6h<br>Prescaler ratio = 2<br><!-- End of picture text -->

Figure 319. Timing example: Up Count-Down Count submode 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2199 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.15.8 Timing example: Up Count-Down Count submode flag assertion 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2200-03.png)


<!-- Start of picture text -->
Counter period  n Counter period  n +1 Counter period  n +2<br>Match AS1 Match AS1<br>CNT n Write to AS2 Write to AS2<br>7h<br>6h<br>5h<br>1h Time<br>Flag set event<br>Flag output and Sn[FLAG]<br>Flag clear<br>AS2 5h 7h<br>AS1 6h 5h 7h<br>Prescaler ratio = 1<br><!-- End of picture text -->

Figure 320. Timing example: Up Count-Down Count submode flag assertion 

#### 61.7.3.15.9 Up Count mode with delayed reload operation 

When the internal counter matches AS1 in the Up Count submode or 1h in the Up Count-Down Count submode (see MCB submodes and MODE field values), the UC asserts the counter bus reload signal. You can read the counter bus reload signal in the following modes: 

- Output PWM Buffered (OPWMB) mode 

- Output Pulse Width and Frequency Modulation Buffered (OPWFMB) mode 

- Center Aligned Output PWM with Dead Time Insertion Buffered (OPWMCB) mode 

You can use the Reload Signal Output Delay Interval (C2[UCRELDEL_INT]) to cause the UC to assert the reload signal only after a specified number of match events (from 2 to 32). 

See Timing example: Up Count mode with delayed reload. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2200 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.15.10 Timing example: Up Count mode with delayed reload 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2201-03.png)


<!-- Start of picture text -->
CNT n [C]<br>6h<br>Write to AS2 Match AS1<br>4h<br>1h<br>Time<br>AS2 6h<br>AS1 4h 6h<br>AS1/BS1 reload signal or cb_reload_n<br>C2_ n [UCRELDEL_INT] = 1b<br>AS1 or BS1 reload signal or cb_reload_n<br>C2_ n [UCRELDEL_INT] = 11b<br>AS1 or BS1 reload signal or cb_reload_n<br>C2_ n [UCRELDEL_INT] = 0b<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2201-04.png)


<!-- Start of picture text -->
Figure 321. Timing example: Up Count mode with delayed reload<br><!-- End of picture text -->

#### 61.7.3.16 Output Pulse Width and Frequency Modulation Buffered (OPWFMB) mode 

#### 61.7.3.16.1 Overview 

In this mode, the UC produces an output signal that has: 

- A duty cycle determined by AS1. 

- A period of BS1. 

The double-buffered AS1 and BS1 registers produce smooth duty-cycle and period transitions when you change AS1 and BS1 during runtime. 

See Table 359 for the values that you must write to Cn[MODE] to enter this mode. 

To provide smooth and consistent channel operation: 

- AS1 and BS1 are both double-buffered to allow smooth signal generation when changing the register values. 

- There is a delay from the AS1 match to the output pin transition (see AS1 and BS1 match timing). 

- The internal counter ranges from 1h to BS1. When you write to BS1, you must write only values greater than 1h. Writing 0h or 1h leads to unpredictable results. 

When a match on comparator A occurs, the UC drives Cn[EDPOL] onto the output flip-flop. When a match on comparator B occurs, the UC drives the complement of Cn[EDPOL] onto the output flip-flop. A BS1 match also causes the internal counter to transition to 1h, thus restarting the counter cycle. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2201 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

The UC automatically selects the internal channel counter as the timebase when you select this mode. The mode supports duty cycles ranging from 0% to 100%. 

#### 61.7.3.16.2 OPWFMB submodes and MODE field values 

Table 353. OPWFMB submodes and MODE field values 

|Match behavior|Cn[MODE](binary)|
|---|---|
|When BS1 matches the selected counter|101_1000|
|When AS1 or BS1 match the selected counter|101_1010|



#### 61.7.3.16.3 Avoid counter wrapping 

When the UC enters OPWFMB mode, the output flip-flop acquires the value of Cn[EDPOL]. If the UC transitions from GPIO to OPWFMB mode when the internal counter value is not within the range 1h–BS1, then the B match never occurs. Because the match never occurs, the internal counter wraps at the maximum counter value—FFFFh for a 16-bit counter. When the counter wrap occurs, the counter returns to 1h and normal OPWFMB operation resumes. Therefore, to avoid this counter wrapping, ensure that the counter value is within the range 1h–BS1 before the UC enters OPWFMB mode. 

#### 61.7.3.16.4 AS1 and BS1 match timing 

As illustrated in Timing example: AS1 and BS1 match, the output pin transition occurs when the AS1 or BS1 match signal deasserts, as indicated by the AS1 match negative-edge detection signal. If you write 4h to AS1, the output pin transitions 4 counter increments plus one system clock cycle after the counter period starts. 

#### 61.7.3.16.5 Timing example: AS1 and BS1 match 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2202-11.png)


<!-- Start of picture text -->
System clock<br>Prescaler<br>8<br>CNT n<br>5<br>4<br>1<br>Time<br>AS1 4h<br>BS1 8h<br>Match AS1 negative-edge detection<br>AS1 match<br>AS1 match<br>negative-edge detection<br>Match BS1<br>negative-edge detection<br>BS1 match<br>BS1 match<br>negative-edge detection<br>Output pin<br>Prescaler ratio = 2  C n [EDPOL] = 0<br><!-- End of picture text -->

Figure 322. Timing example: AS1 and BS1 match 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2202 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.16.6 0% duty cycle 

Timing example: AS1 = 0 illustrates the generated output signal when AS1 = 0, which results in a 0% duty cycle. 

Because the internal counter never reaches zero in this situation, the UC infers a match as if AS1 = 1h. However, it is the positive edge of the match signal that triggers the output pin transition instead of the negative edge, which is what happens when AS1 = 1h. The AS1 positive-edge match signal from period n+1 occurs at the same time as the BS1 negative-edge match signal from period n. This timing allows the AS1 positive-edge match to mask the BS1 negative-edge match when they occur at the same time. As a result, no transition occurs on the output flip-flop and the UC generates a 0% duty cycle. 

#### 61.7.3.16.7 Timing example: AS1 = 0 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2203-06.png)


<!-- Start of picture text -->
Write to AS2 Counter period  n Counter period  n +1<br>System clock<br>Prescaler<br>CNT n 5<br>4<br>1 1<br>Time<br>AS1 4h 0h<br>AS2 0h<br>BS1 8h<br>AS1 match<br>AS1 match Match AS1 positive-edge detection<br>positive-edge detection<br>Match AS1 negative-edge detection<br>AS1 match<br>negative-edge detection<br>BS1 match<br>BS1 match Match BS1 negative-edge detection<br>negative-edge detection<br>Output pin No transition at this point<br>Prescaler ratio = 2 C n [EDPOL] = 0<br><!-- End of picture text -->

Figure 323. Timing example: AS1 = 0 

#### 61.7.3.16.8 Loading AS1 and BS1 

As illustrated in Timing example: AS1 and BS1 update and FLAGs, AS1 and BS1 both use the same signal, generated at the last system clock cycle of a counter period. Therefore, eMIOS updates AS1 and BS1 with AS2 and BS2 values, respectively, at the same time that it changes the internal counter (CNTn[C]) to 1h. This event is the counter period boundary. The load signal pulse lasts for one system clock cycle. If you write AS2 and BS2 within counter period n, their values are available in AS1 and BS1, respectively, at the first clock cycle of counter period n+1. The UC then uses these new values for matches at counter period n+1. You can use Output Update Disable (OUDIS) to delay updating AS1 and BS1 for synchronization purposes. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2203 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.16.9 Timing example: AS1 and BS1 update and FLAGs 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2204-03.png)


<!-- Start of picture text -->
Counter period  n Counter period  n +1 Counter period  n +2<br>Write to AS2 Write to AS2<br>Match AS1 Match BS1 Match AS1 Match BS1 Match BS1<br>lnternal counter<br>Write to BS2<br>8h<br>6h<br>4h<br>Due to BS1 match 2h<br>1h<br>counter period  n -1<br>Output pin<br>Flag set event<br>Flag output and S n [FLAG]<br>Flag clear<br>AS1 or BS1 load signal<br>AS1 2h 4h 6h<br>AS2 2h 4h 6h<br>BS1 8h 6h<br>C n [EDPOL] = 0 BS2 8h 6h<br>Prescaler ratio = 4<br><!-- End of picture text -->

Figure 324. Timing example: AS1 and BS1 update and FLAGs 

#### 61.7.3.16.10 Flag generation 

Timing example: AS1 and BS1 update and FLAGs assumes that both the channel and global prescalers are 1h (divide ratio of 2), causing the internal counter to transition every four system clock cycles. You can configure flags to be generated only on BS1 matches when bit 1 of Cn[MODE] is 0, or on both AS1 and BS1 matches when that bit is 1. Because the BS1 flag occurs at the period boundary, you can use this flag to indicate that the AS2 or BS2 data written in period n has been loaded to AS1 or BS1, respectively, thereby generating matches in period n+1. Flag operation is synchronous, which means the flag sets one system clock cycle after the set-flag event. 

#### 61.7.3.16.11 Output disable 

As illustrated in Timing example: active output disabled, the output-disable feature in OPWFMB mode forces the channel output flip-flop to the value of Cn[EDPOL]. This functionality supports applications that use active-high signals and a high-to-low transition at an AS1 match. In this case, you must write 0 to Cn[EDPOL]. You also must configure the internal counter to transition on every system clock cycle (write 0 to both GCP and CP). 

The output-disable feature operates synchronously, meaning that the assertion of the Output Disable input signal causes the channel output flip-flop to transition to Cn[EDPOL] at the next system clock cycle. If the Output Disable input pin deasserts, the output-signal transition occurs at the next AS1 or BS1 match. 

Timing example: active output disabled assumes that the Output Disable input is enabled (using Cn[ODIS]) and selected (using Cn[ODISSL]). See UC Control n (C0 - C23) for a detailed description of the ODIS and ODISSL fields that enable and select the Output Disable inputs, respectively. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2204 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.16.12 Timing example: active output disabled 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2205-03.png)


<!-- Start of picture text -->
Cycle  n Cycle  n +1 Cycle  n +2<br>Match AS2 Match AS1<br>Match AS1 Match BS1 Match AS1 Match BS1 Match BS1<br>Internal counter<br>Write to BS2<br>8h<br>6h<br>4h<br>Due to BS1 match<br>2h<br>cycle  n -1 1h Time<br>Output pin<br>Flag set event<br>Flag output and S n [FLAG]<br>Flag clear event<br>Output disable<br>AS1 2h 4h 6h<br>AS2 2h 4h 6h<br>BS1 8h 6h<br>BS2 8h 6h<br>EDPOL = 0<br>Prescaler ratio = 1<br><!-- End of picture text -->

Figure 325. Timing example: active output disabled 

#### 61.7.3.16.13 Force match 

Force Match A (Cn[FORCMA]) and Force Match B (Cn[FORCMB]) allow you to force the output flip-flop to the level corresponding to a match on comparators A or B, respectively. Similarly to a BS1 match, Force Match B changes the internal counter to 1h. The force-match operations do not set the input-capture flag (Sn[FLAG]). 

#### 61.7.3.16.14 100% and 0% duty cycles 

Timing example: from 100% to 0% duty cycle illustrates the generation of 100% and 0% duty-cycle signals. Initially, AS1 = 8h and BS1 = 8h. In this case, a BS1 match has precedence over an AS1 match—therefore, the output flip-flop acquires the complement of Cn[EDPOL]. This configuration corresponds to a 100% duty-cycle signal. The same output signal can be generated for any AS1 value greater than or equal to BS1. 

If AS1 is 0, the UC generates a 0% duty-cycle signal. In this case, the BS1 = 8h match from period 8 occurs at the same time as the AS1 = 0h match from period 9. See Timing example: AS1 = 0 for AS1 and BS1 match generation. In this case, an AS1 match has precedence over a BS1 match, and the output signal transitions to Cn[EDPOL]. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2205 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.16.15 Timing example: from 100% to 0% duty cycle 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2206-03.png)


<!-- Start of picture text -->
Counter Counter Counter Counter Counter Counter Counter Counter Counter<br>CNT n period 1 period 2 period 3 period 4 period 5 period 6 period 7 period 8 period 9<br>8h<br>1h<br>Output pin 100 % 0 %<br>AS1 8h 7h 6h 5h 4h 3h 2h 1h 0h<br>AS2 7h 6h 5h 4h 3h 2h 1h 0h<br>BS1 8h<br>C n [EDPOL] = 0<br>Prescaler ratio = 1<br><!-- End of picture text -->

Figure 326. Timing example: from 100% to 0% duty cycle 

#### 61.7.3.17 Center Aligned Output PWM with Dead Time Insertion Buffered (OPWMCB) mode 

#### 61.7.3.17.1 Overview 

In this mode, the UC generates a center-aligned PWM pulse with dead time insertion in the leading or trailing edge. See OPWMCB functions and MODE field values. AS1 and BS1 are double-buffered to allow smooth output signal generation when you change the AS2 or BS2 values. 

When the UC enters OPWMCB mode from GPIO mode: 

- The UC drives the complement of Edge Polarity (Cn[EDPOL]) on the output flip-flop. 

- Select the timebase using Bus Select (Cn[BSL]). The timebase you select must be running in Up Count-Down Count mode. See Timing example: Up Count submode flag assertion. You must start the MCB timebase after the UC enters OPWMCB mode to avoid missing a match on the first duty cycle. 

- Store the ideal duty cycle for the PWM signal in AS1 (write to An[A]), which the UC compares with the selected timebase. 

- Store the dead time value in BS1 (write to Bn[B]), which the UC compares with the internal counter (CNTn[C]). 

The internal counter may use the internal prescaler ratio, while the selected timebase may use a different prescaler ratio. The UC always resets the internal counter to 1h when an AS1 match occurs. 

As in OPWMB and OPWFMB modes, the UC generates the match signal which compares the selected timebase with AS1 or BS1. When the UC deasserts the channel's combinational comparator output signal, it uses the match signal to assert or negate the channel's output flip-flop. See Timing example: AS1 and BS1 match for an illustration of the delay from match to output flip-flop transition in OPWFMB mode. The operation of OPWMCB mode is similar to OPWFMB mode with respect to match behavior and output pin transition. 

See Entering OPWMCB mode. 

#### 61.7.3.17.2 OPWMCB functions and MODE field values 

Table 354. OPWMCB functions and mode field values 

|Function|Cn[MODE](binary)|
|---|---|
|Insert trailing edge dead time with duty cycle determined by<br>BS1 + AS1|101_11p0<sup>1</sup>|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2206 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

Table 354. OPWMCB functions and mode field values (continued) 

|Function|Cn[MODE](binary)|
|---|---|
|Insert leading edge dead time with duty cycle determined by<br>BS1 – AS1|101_11p1<sup>1</sup>|
|Assert the input capture flag (Sn[FLAG]) on the trailing edge<br>of the output PWM signal|101_110p<sup>1</sup>|
|Assert the input capture flag (Sn[FLAG]) on both edges of the<br>output PWM signal|101_111p<sup>1</sup>|



1. p = Adjust parameters for submodes and options. See Unified channels (UC). 

#### 61.7.3.17.3 Entering OPWMCB mode 

To enter OPWMCB mode (this procedure assumes the channel is initially in GPIO mode): 

1. Disable the GCP (write 0 to MCR[GPREN]). 

2. For the timebase (MCB) channel: 

   - a. Disable the CP (write 0 to Cn[UCPREN]). 

   - b. Initialize the internal counter (write 1h to CNTn[C]). 

   - c. Initialize the A data (write appropriate value to An[A]). 

   - d. Configure the UC for MCB Up Count-Down Count mode (write 101_01xyb to Cn[MODE], where x = 0 for flag set on match start or x = 1 for flag set at period boundary, and y = 0 for internal clock source or y = 1 for external clock source). 

   - e. Select the CP ratio (Cn[UCPRE]). 

   - f. Enable the CP (write 1 to Cn[UCPREN]). 

3. For the OPWMCB channel: 

   - a. Disable the CP (write 0 to Cn[UCPREN]). 

   - b. Initialize the A data (write appropriate value to An[A]). 

   - c. Initialize the B data (write appropriate value to Bn[B]). 

   - d. Select the timebase input (Cn[BSL]). 

   - e. Configure the UC for MCB Up Count-Down Count mode (write 101_01xyb to Cn[MODE], where x = 0 for flag set on match start or x = 1 for flag set at period boundary, and y = 0 for internal clock source or y = 1 for external clock source). 

   - f. Select the CP ratio (Cn[UCPRE]). 

   - g. Enable the CP (write 1 to Cn[UCPREN]). 

4. Enable the GPC (write 1 to MCR[GPREN]). 

#### 61.7.3.17.4 Timing example: AS1 and BS1 load 

When the selected counter bus transitions from 2h to 1h: 

- The UC loads AS1 and BS1 as shown in the following figure. 

- This event defines the counter period boundary. 

The UC loads the values you write to AS2 or BS2 within period n into AS1 or BS1, respectively, and uses them to generate matches in period n+1. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2207 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2208-01.png)


<!-- Start of picture text -->
Enhanced Modular IO Subsystem (eMIOS)<br>Counter period  n Counter period  n+1 Counter period  n+2<br>Selected<br>counter bus Write to AS2 Write to BS2 Write to BS2 Write to AS2<br>6h<br>5h<br>1h Time<br>System clock<br>Selected counter == 2<br>AS1 or BS1 load signal<br>AS1 value 20h 15h 16h<br>AS2 value 20h 15h 16h<br>BS1 value 4h 5h 6h<br>BS2 value 4h 5h 6h<br>Prescaler ratio = 2<br>Figure 327. Timing example: AS1 and BS1 load<br><!-- End of picture text -->

#### 61.7.3.17.5 Operation sequence with leading edge dead time insertion 

When operating with leading edge dead time insertion: 

1. When the first AS1 match occurs, the UC writes 1h to the internal counter. 

2. When a match between BS1 and the internal timebase occurs, the UC drives the value of Edge Polarity (Cn[EDPOL]) on the output flip-flop. 

3. When the next match between AS1 and the selected timebase occurs, the UC drives the complement of Edge Polarity (Cn[EDPOL]) on the output flip-flop. 

The UC repeats the above sequence continuously. 

You must not allow the internal counter to reach 0h as the result of a rollover. To avoid this, you must not write a value greater than 

2 x ((external Count Up limit) – An[A]) 

into Bn[B]. 

See Timing example: leading dead time insertion. 

#### 61.7.3.17.6 Timing example: leading dead time insertion 

This example illustrates two cycles of a center-aligned PWM signal. AS1 and BS1 values change within the same period, which allows you to change the duty cycle and dead time values at the same time. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2208 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2209-01.png)


<!-- Start of picture text -->
Enhanced Modular IO Subsystem (eMIOS)<br>Write to AS2<br>Selected Write to BS2<br>counter bus<br>20h<br>15h<br>13h<br>1h Time<br>AS1 value 15h 13h<br>AS2 value 15h 13h<br>BS1 value 2h 4h<br>BS2 value 2h 4h<br>Internal<br>time base Internal counter<br>becomes<br>1 on AS1 match<br>4h<br>2h<br>1h Time<br>Dead time Dead time<br>Output flip-flop<br>Flag output and S n [FLAG]<br>C n [EDPOL] = 1<br>Figure 328. Timing example: leading dead time insertion<br><!-- End of picture text -->

#### 61.7.3.17.7 Operation sequence with trailing edge dead time insertion 

When operating with trailing edge dead time insertion: 

1. When the first match between AS1 and the selected timebase occurs, the UC: 

   - a. Drives the value of Edge Polarity (Cn[EDPOL]) on the output flip-flop. 

   - b. Writes the internal counter (CNTn[C]) to 1h. 

2. When the second match between AS1 and the selected timebase occurs, the UC: 

   - a. Writes the internal counter to 1h. 

   - b. Enables BS1 matches. 

3. When a match between BS1 and the selected timebase occurs, the UC drives the the complement of Edge Polarity (Cn[EDPOL]) on the output flip-flop. 

The UC repeats this sequence continuously. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2209 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.17.8 Timing example: trailing dead time insertion 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2210-03.png)


<!-- Start of picture text -->
Write to AS2<br>Selected Write to BS2<br>counter bus<br>20h<br>15h<br>13h<br>1h Time<br>AS1 value 15h 13h<br>AS2 value 15h 13h<br>BS1 value 2h 4h<br>BS2 value 2h 4h<br>Internal<br>time base<br>Internal counter<br>becomes<br>1 on AS1 match<br>4h<br>2h<br>1h Time<br>Dead time Dead time<br>Output flip-flop<br>Flag output and S n [FLAG]<br>C n [EDPOL] = 1<br><!-- End of picture text -->

Figure 329. Timing example: trailing dead time insertion 

#### 61.7.3.17.9 Force match 

Force Match A (Cn[FORCMA]) and Force Match B (Cn[FORCMB]) allow you to force the output flip-flop to the level corresponding to a match on comparators A or B, respectively. If subsequent matches occur on comparators A and B, the UC continues to generate PWM pulses regardless of the input capture flag (Sn[FLAG]). The force-match operations do not set the input-capture flag (Sn[FLAG]). 

When you select leading edge dead time insertion: 

- Force Match A drives the complement of Edge Polarity (Cn[EDPOL]) on the output flip-flop. 

- Force Match B drives the value of Edge Polarity (Cn[EDPOL]) on the output flip-flop. 

When you select trailing edge dead time insertion: 

- Force Match A drives the value of Edge Polarity (Cn[EDPOL]) on the output flip-flop. 

- Force Match B drives the complement of Edge Polarity (Cn[EDPOL]) on the output flip-flop. 

Force Match operation does not write 1h to the internal timebase. 

Force Match operation does not set the input-capture flag. 

When you assert Force Match A and Force Match B at the same time, the UC drives the complement of Edge Polarity (Cn[EDPOL]) on the output flip-flop. This is the equivalent of saying that Force Match A has precedence over Force Match B when you select leading edge dead time insertion, and Force Match B has precedence over Force Match A when you select trailing edge dead time insertion. 

Force Match A and Force Match B have the same output transition behavior in both Freeze state and unfrozen state. 

#### 61.7.3.17.10 Duty cycle 

You generate a duty cycle from 0% to 100% by writing appropriate values to AS1 and BS1 relative to the period of the external timebase. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2210 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

To generate a 100% duty cycle waveform: 

- Select trailing edge dead time insertion (see OPWMCB functions and MODE field values). 

- Write 1h to Edge Polarity (Cn[EDPOL]). 

- The BS1 match must occur on or after the counter period boundary (external counter = 1). 

You can also generate a 100% duty cycle waveform by writing 1h to AS1. However, if you do this before the UC enters OPWMCB mode, a 100% duty cycle may not occur in the first PWM period depending upon the pin state at mode entry. 

To generate a 0% duty cycle waveform: 

- AS1 must be greater than the maximum value of the selected counter period. 

- The pin must start the current period with the complement value of Edge Polarity (Cn[EDPOL]). If starting at 100% duty cycle, you can change Edge Polarity (Cn[EDPOL]) to its complement by forcing the pin (see Force match). 

You must write only non-zero values to AS1. If you write the maximum value of the external counter given by 

(external counter period)/2 

to AS1, the UC constantly drives the value of Edge Polarity (Cn[EDPOL]) on the output flip-flop. 

UC logic prevents matches from one period propagating to the next period. In trailing edge dead time insertion, the UC masks out BS1 matches that occur late in period n, so matches in period n+1 are unaffected and the output flip-flop does not transition. 

#### 61.7.3.17.11 Timing example: duty cycle 

To generate a 100% duty cycle output waveform, write 4h to AS1 and 3h to BS1, as illustrated in this diagram. In this case, the trailing edge is at the boundary of counter period n+1, which actually belongs to period n+2 and therefore does not cause the output flip-flip to transition. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2211-16.png)


<!-- Start of picture text -->
Selected Counter period  n Counter period  n +1 Counter period  n +2<br>counter bus Write to AS2<br>20h<br>Time<br>1h<br>AS1 value 15h 4h<br>AS2 value 15h 4h<br>BS1 value 3h<br>BS2 value 3h<br>Internal<br>time base<br>3h<br>1h Time<br>Dead time Dead time Dead time<br>Output flip-flop<br><!-- End of picture text -->

Figure 330. Timing example: duty cycle 

#### 61.7.3.17.12 Output disable 

You can use Output Update Disable (write 0 to OUDIS[OUn]) to disable AS1 and BS1 updates. This allows you to update AS1 and BS1 in the same counter period and synchronize the loading of these registers with the loading of AS1 or BS1 in other channels. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2211 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

Asserting Output Update Disable drives the complement of Edge Polarity (Cn[EDPOL]) on output flip-flop. The internal channel matches continue to occur, and therefore the UC continues to set flags. 

When you deassert Output Update Disable, the output flip-flop is again controlled by AS1 and BS1 matches. The UC transitions the output flip-flop only on system clock edges. 

#### 61.7.3.18 Output PWM Buffered (OPWMB) mode 

#### 61.7.3.18.1 Overview 

In this mode, the UC produces PWM pulses with programmable leading and trailing edge placement. You must select an external counter driven in MCB Up mode from one of the counter buses. AS1 and BS1 define the first and second edges, respectively. Cn[EDPOL] defines the output signal polarity. If Cn[EDPOL] = 0, a negative edge occurs when AS1 matches the selected counter bus and a positive edge occurs when BS1 matches the selected counter bus. 

See OPWMB submodes and MODE field values for the values that you must write to Cn[MODE] to enter this mode. 

AS1 and BS1 are double-buffered and updated from AS2 and BS2, respectively, at the cycle boundary. The load operation is similar to the one that occurs in OPWFMB mode. See Timing example: AS1 and BS1 update and FLAGs for more information about AS1 and BS1 updates. 

When the UC enters OPWMB mode, the UC drives Cn[EDPOL] on the output flip-flop. 

These rules apply to OPWMB mode: 

- If the AS1 and BS1 matches occur at the same time within the same counter period, the BS1 match has precedence over the AS1 match. 

- An AS1 = 0 match in period n has precedence over a BS1 match in period n-1. 

- The UC masks out AS1 matches if they occur after a BS1 match within the same period. 

- The UC loads any value that you write to AS2 or BS2 in period n into AS1 and BS1 at the following period boundary (assuming that the corresponding OUn field of Output Update Disable (OUDIS) is 0). Therefore, the UC uses the new values for AS1 and BS1 matches in period n+1. 

Timing example: 100% to 0% duty cycle illustrates a waveform changing from 100% to 0% duty cycle. In this example, BS1 is programmed to the same value as the period of the external selected timebase. If you write a value smaller than 8h to BS1, you cannot achieve a 0% duty cycle by only changing AS1. Because BS1 matches have precedence over AS1 matches, the flag output transitions to the complement of Cn[EDPOL] at a BS1 match. For another example, if you write 9h to BS1, a BS1 match does not occur, and the UC generates a 0% duty-cycle signal. 

#### 61.7.3.18.2 OPWMB submodes and MODE field values 

Table 355. OPWMB submodes and MODE field values 

|When FLAG generation occurs|Cn[MODE](binary)|
|---|---|
|At a BS1 match|110_0000|
|At an AS1 or BS1 match|110_0010|



#### 61.7.3.18.3 Force match 

Force Match A (Cn[FORCMA]) and Force Match B (Cn[FORCMB]) allow you to force the output flip-flop to the level corresponding to a match on comparators A or B, respectively. If subsequent matches occur on comparators A and B, the UC continues to generate PWM pulses regardless of the input capture flag (Sn[FLAG]). The force-match operations do not set the input-capture flag (Sn[FLAG]). 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2212 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.18.4 Matches and flag operation 

Timing example: matches and flags illustrates the operation of OPWMB mode with an emphasis on AS1 and BS1 matches and the transition of the channel output pin. The output pin transitions are based on the negative edges of the AS1 and BS1 match signals. AS1 becomes zero in period n+1. In this case, the UC uses the match positive edge instead of the negative edge to transition the output flip-flop. 

#### 61.7.3.18.5 Timing example: matches and flags 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2213-05.png)


<!-- Start of picture text -->
Counter period  n Counter period  n +1<br>Write to AS2<br>Clock<br>Prescaler<br>Selected 8<br>counter bus<br>6 6<br>4<br>1 1<br>Time<br>AS1 4h 0h<br>AS2 0h<br>BS1 6h<br>AS1 match<br>Match AS1 positive-edge detection<br>AS1 match positive-edge detection<br>Match AS1<br>AS1 match negative-edge detection negative-edge detection<br>BS1 match<br>Match BS1<br>BS1 match negative-edge detection negative-edge detection<br>Output pin<br>C n [EDPOL] = 0<br>Flag set event<br>Flag output and S n [FLAG]<br>Figure 331. Timing example: matches and flags<br><!-- End of picture text -->

#### 61.7.3.18.6 0% duty cycle 

Timing example: 0% duty cycle illustrates the channel operation for a 0% duty cycle. The AS1 match positive-edge signal occurs at the same time as the BS1 = 8h negative-edge signal. In this case, the AS1 match has precedence over the BS1 match, causing the output pin to remain at the value of Cn[EDPOL] and generating a 0% duty-cycle signal. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2213 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.18.7 Timing example: 0% duty cycle 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2214-03.png)


<!-- Start of picture text -->
Counter period  n Counter period  n +1<br>Write to AS2<br>Clock<br>Prescaler<br>Selected 8 8<br>counter bus<br>4<br>1 1<br>Time<br>AS1 4h 0h<br>AS2 0h<br>BS1 8h<br>AS1 match<br>Match AS1 positive-edge detection<br>AS1 match positive-edge detection<br>Match AS1<br>AS1 match negative-edge detection negative-edge detection<br>BS1 match<br>BS1 match negative-edge detection Match BS1 negative-edge detection<br>Output pin<br>C n [EDPOL] = 0<br>Flag set event<br>Flag output and S n [FLAG]<br><!-- End of picture text -->

Figure 332. Timing example: 0% duty cycle 

#### 61.7.3.18.8 Active output disabled 

Timing example: active output disabled illustrates the operation of the OPWMB mode with an emphasis on the assertion of the output-disable signal. The output disable forces a transition in the output pin to the value of Cn[EDPOL]. The deassertion of the output-disable signal allows the output pin to transition at the following AS1 or BS1 match. The output disable does not modify the behavior of Sn[FLAG]. A delay of one system clock cycle exists between the assertion of the output-disable signal and the transition of the output pin to Cn[EDPOL]. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2214 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.18.9 Timing example: active output disabled 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2215-03.png)


<!-- Start of picture text -->
Counter period  n Counter period  n +1 Counter period  n +2<br>Match AS1 Match BS1 Match AS1 Match BS1 Match BS1<br>Selected Write to AS2 Write to BS2 Write to AS2<br>counter bus<br>8h<br>6h<br>4h<br>2h<br>Due to BS1 match 1h Time<br>Counter period  n -1<br>Output pin<br>Flag set event<br>Flag output and S n [FLAG]<br>Flag clear<br>Output disable<br>AS1 2h 4h 6h<br>AS2 2h 4h 6h<br>BS1 8h 6h<br>BS2 8h 6h<br>C n [EDPOL] = 0<br><!-- End of picture text -->

Figure 333. Timing example: active output disabled 

#### 61.7.3.18.10 Changing from 100% to 0% duty cycle 

Timing example: 100% to 0% duty cycle illustrates a waveform changing from 100% to 0% duty cycle. In this example, BS1 has the same value as the period of the external selected timebase. If you write a value smaller than 8h to BS1, you cannot achieve a 0% duty cycle by only changing AS1. Because BS1 matches have precedence over AS1 matches, the output pin transitions to the complement of Cn[EDPOL] at a BS1 match. For another example, if you write 9h to BS1, a BS1 match does not occur, and the UC generates a 0% duty-cycle signal. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2215 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.18.11 Timing example: 100% to 0% duty cycle 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2216-03.png)


<!-- Start of picture text -->
Selected Counter   Counter   Counter   Counter   Counter   Counter   Counter   Counter   Counter<br>counter bus period 1 period 2 period 3 period 4 period 5 period 6 period 7 period 8 period 9<br>Output pin 100% 0%<br>AS1 8h 7h 6h 5h 4h 3h 2h 1h 0h<br>AS2 7h 6h 5h 4h 3h 2h 1h 0h<br>BS1<br>C n [EDPOL] = 0<br>Prescaler = 1<br><!-- End of picture text -->

Figure 334. Timing example: 100% to 0% duty cycle 

#### 61.7.3.19 Output PWM with Trigger (OPWMT) mode 

#### 61.7.3.19.1 Overview 

In this mode, the UC generates PWM pulses where the period does not change while the UC outputs the signal, but the duty cycle changes. When the duty cycle changes, it must not create glitches. The mode supports multiple UCs executing in the same mode and sharing a common timebase. Each UC can have a fixed PWM leading-edge position with respect to the other UCs. It can also generate a trigger signal at any point in the period. eMIOS can output this trigger signal to initiate activity in other parts of the chip—for example, to start ADC conversions. 

You must select an external counter, driven in either MC Up or MCB Up mode (see Modulus Counter Buffered (MCB) mode), from one of the counter buses. 

AS1 in OPWMT mode, AS2 in OPWMT mode, and BS1 and BS2 in OPWMT mode describe the configuration and behavior of the individual shadow registers in this mode. 

To account for the shift in the AS1-defined leading edge of the waveform, the BS1-defined trailing edge may roll over into the next period. This means that a match against BS1 does not have to be qualified by a match in AS1. This also means that if you incorrectly write a value less than AS1 to BS1, the output persists over a period boundary until the UC encounters the BS1 value. 

This mode provides a buffered update of the trailing edge by updating BS1 with BS2 contents only at a match of AS1. 

The positive edges of the AS1, BS1, and AS2 match signals drive the output pin and flag transitions. See Timing example: matches and flags for details on positive-edge matches. 

The UC sets the input capture flag (Sn[FLAG]) only at an AS2 match. An AS1, BS1, or BS2 match has no effect on the flag. 

When the UC enters OPWMT mode, it drives the complement of Cn[EDPOL] on the output flip-flop. 

Timing example: OPWMT illustrates the UC running in OPWMT mode with trigger-event generation and duty-cycle update after the next-period update. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2216 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.19.2 Timing example: OPWMT 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2217-03.png)


<!-- Start of picture text -->
Match AS1 Match BS1 Match BS1<br>Match AS2 Match AS2<br>Write to AS1<br>Selected counter bus and BS2 Write to BS2 Match AS1<br>11FFh<br>1000h<br>700h<br>500h<br>400h<br>0h Time<br>Output flip-flop<br>Flag output and S n [FLAG]<br>AS1 (read from A n ) 400h<br>BS1 (read from B n ) 0xxxxxxx 1000h 700h<br>BS2 (write to B n ) 1000h 700h<br>AS2 500h<br><!-- End of picture text -->

Figure 335. Timing example: OPWMT 

#### 61.7.3.19.3 AS1 in OPWMT mode 

AS1 defines the leading edge of the PWM pulse output, and therefore the beginning of the PWM period. Using this fact, you can ensure that, when using a shared timebase, the leading edges of multiple UCs in OPWMT mode occur at specific times with respect to the other UCs. You can also introduce a fixed offset for each UC, which is particularly useful in the generation of lighting control signals. For this application, to reduce or eliminate noise generation, you can shift the PWM pulse of each UC with respect to the selected timebase by adjusting the AS1 value for each channel. The value you write to AS1 must be within the range of the selected timebase. Shadow registers (AS1, AS2, BS1, and BS2) loaded with 0h do not produce matches if the channel driving the timebase is in MCB mode. 

AS1 is not buffered, because the shift of a PWM channel must not change while the UC generates the PWM signal. If you modify AS1, it updates immediately and one PWM pulse could be lost. 

The UC compares AS1 to the selected timebase. When a match on AS1 occurs, the UC drives Cn[EDPOL] on the output flip-flop. When a match occurs on comparator B, the UC drives the complement of Cn[EDPOL] on the output flip-flop. 

#### 61.7.3.19.4 AS2 in OPWMT mode 

AS2 defines the generation of a trigger event within the PWM period. The value you write to AS2 must be within the range of the selected timebase—otherwise the UC does not generate a trigger. A match on the comparator asserts the input-capture flag, but the match has no effect on the PWM output signal generation. The typical setup to obtain a trigger with a flag is to enable DMA and drive the DMA acknowledgement or DMA completion input high. 

AS2 is not buffered, and therefore the UC updates it immediately. If the UC is running when you make a change, this could cause either of the following: 

- The loss of one trigger event 

- The generation of two trigger events within the same period 

You access AS2 by reading or writing ALTAn[ALTA]. 

#### 61.7.3.19.5 BS1 and BS2 in OPWMT mode 

You access BS1 and BS2 using Bn[B]: 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2217 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

- When you read Bn[B], you read BS1. 

- When you write to Bn[B], you write to BS2. 

BS1 defines the trailing edge of the PWM pulse output, and therefore the duty cycle of the PWM signal. To synchronize the BS1 update with the PWM signal and to ensure a correct output pulse generation, the BS2→BS1 transfer occurs at every AS1 match. This behavior is the same as in OPWM mode with next-period update. 

Output Update Disable (OUDIS) affects transfers between BS2 and BS1 only. 

#### 61.7.3.19.6 Force match 

At any time, Force Match A (Cn[FORCMA]) and Force Match B (Cn[FORCMB]) allow you to force the output flip-flop to the level corresponding to a match on AS1 or BS1, respectively. Similarly to a BS1 match, Force Match B changes the internal counter to 1h. The force-match operations do not set the input-capture flag (Sn[FLAG]). Any match resulting from writing 1 to FORCMA or FORCMB has priority over any simultaneous match regarding output pin transitions. BS2→BS1 transfer at an A match is not inhibited by writing 1 simultaneously to both FORCMA or FORCMB. If you write 1 to both FORCMA and FORCMB simultaneously, the output pin acquires the complement of Cn[EDPOL], as if AS1 and BS1 had the same value. FORCMA assertion causes the UC to process the BS2→BS1 transfer as a regular A match comparison and not due to FORCMA assertion, regardless of FORCMB assertion. If subsequent matches occur on comparators AS1 and B, the UC continues to generate PWM pulses, regardless of the state of Sn[FLAG]. 

#### 61.7.3.19.7 Duty cycle 

To achieve 0% duty cycle, you must write the same value to AS1 and BS2. When a simultaneous match on comparators A and B occurs, the UC drives the complement of Cn[EDPOL] on the output flip-flop at every period. 

To achieve 100% duty cycle, you must write a value to BS1 that is greater than the maximum value of the selected timebase. The maximum counter value for the timebase is FF_FFFEh for a 24-bit counter and FFFEh for a 16-bit counter. When a match on comparator AS1 occurs, the UC drives Cn[EDPOL] on the output flip-flop at every period. The match at comparator A still triggers the BS2→BS1 transfer. 

Timing example: 0% duty cycle illustrates the UC running in OPWMT mode with trigger-event generation and a 0% duty cycle. 

Timing example: 100% duty cycle illustrates the UC running in OPWMT mode with trigger-event generation and a 100% duty cycle. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2218 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.19.8 Timing example: 0% duty cycle 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2219-03.png)


<!-- Start of picture text -->
Match AS1 Match BS1 Match BS1<br>Match AS2 Match AS2<br>Write to AS1<br>Selected counter bus and BS2 Write to BS2 Match AS1<br>11FFh<br>1000h<br>500h<br>400h<br>0h Time<br>Output flip-flop<br>Flag output and S n [FLAG]<br>AS1 (read from A n ) 400h<br>BS1 (read from B n ) 0xxxxxxx 1000h 400h<br>BS2 (write to B n ) 1000h 400h<br>AS2 500h<br><!-- End of picture text -->

Figure 336. Timing example: 0% duty cycle 

#### 61.7.3.19.9 Timing example: 100% duty cycle 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2219-06.png)


<!-- Start of picture text -->
Match AS1 Match BS1 Match BS1 does not occur<br>Match AS2 Match AS2<br>Write to AS1<br>Selected counter bus and BS2 Write to BS2 Match AS1<br>11FFh<br>1000h<br>500h<br>400h<br>0h Time<br>Output flip-flop<br>Flag output and S n [FLAG]<br>AS1 (read from A n ) 400h<br>BS1 (read from B n ) 0xxxxxxx 1000h 1200h<br>BS2 (write to B n ) 1000h 1200h<br>AS2 500h<br>Figure 337. Timing example: 100% duty cycle<br><!-- End of picture text -->

#### 61.7.3.19.10 Output disable 

As with other UC modes, OPWMT mode implements the output-disable function. When Cn[ODIS] = 1, assertion of the output-disable input causes the UC to drive Cn[EDPOL] on the output. Other than the fixed output, the UC continues to operate normally. When the output-disable signal deasserts, the UC returns to full normal operation. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2219 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.20 Programmable input filter (PIF) 

#### 61.7.3.20.1 Overview 

The PIF specifies the minimum input pulse width, in clock cycles, that can pass through the filter. It supports bypass operation (Cn[IF]), with the input signal synchronized before arriving at the digital filter, or from 2 to 16 clock cycles in powers of 2. 

#### 61.7.3.20.2 Counter 

The PIF is a 5-bit programmable up counter. The selected clock source increments the up counter after the number of clock cycles specified by the input filter (Cn[IF]0. 

The system clock synchronizes the input signal. When this signal changes state, the counter begins incrementing. As long as the new signal state is stable, the counter continues incrementing. If the counter overflows, eMIOS validates the new signal value. In this case, it transmits the value as a pulse edge to the edge detector. If the opposite edge appears on the signal before validation (overflow), eMIOS resets the counter. At the next transition, the counter starts incrementing again. A glitch does not occur on the edge detector for any pulse shorter than the full range of the masked counter. 

Neither Freeze state nor deasserted GTBE disables the filter. 

#### 61.7.3.20.3 UC PIF logic 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2220-10.png)


<!-- Start of picture text -->
Cn[IF]<br>FCK 3 2 1 0<br>System clock<br>clk<br>Prescaled clock<br>5-bit up counter Filter out<br>Input pin<br>Synchronizer<br>Clock<br><!-- End of picture text -->

Figure 338. UC PIF logic 

#### 61.7.3.20.4 Timing example: UC PIF at 4 cycles 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2220-13.png)


<!-- Start of picture text -->
Selected clock<br>Input pin<br>5-bit counter<br>Time<br>Filter out<br>Figure 339. Timing example: UC PIF at 4 cycles<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2220-14.png)


<!-- Start of picture text -->
Time<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2220 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.3.21 UC clock prescaler (CP) 

eMIOS divides the GCP output signal by the UC CP (Cn[UCPRE] + 1) to generate a clock enable for the UC internal counter. See Global clock prescaler (GCP). You enable the UC CP by writing 1 to Cn[UCPREN]. If you disable the CP (write 0 to the same field), eMIOS stops the UC internal counter. 

To ensure safe operation and avoid glitches, you must perform the following steps to change the UC CP: 

1. Disable the GCP (write 0 to MCR[GPREN]). 

2. Disable the UC CP (write 0 to Cn[UCPREN]). 

3. Specify the new prescaler value (write CP – 1 to Cn[GPRE]. 

4. Enable the UC CP (write 1 to Cn[UCPREN]). 

5. Enable the GCP (write 1 to MCR[GPREN]). 

### 61.7.4 Peripheral bus interface unit (BIU) 

The BIU provides the interface between the IIB and the peripheral bus, which allows communication among all submodules and the IP interface. The BIU supports 8-, 16-, and 32-bit accesses performed over a 32-bit data bus in a single clock cycle. 

### 61.7.5 Global clock prescaler (GCP) 

eMIOS divides the system clock by the GCP (MCR[GPRE] + 1) and routes the resulting prescaled clock output to the channel CPs. You enable the GCP by writing 1 to MCR[GPREN]. If you disable the GCP (write 0 to the same field), eMIOS clears the prescaler counter and stops the prescaler clock. 

To ensure safe operation and avoid glitches, you must perform the following steps to change the GCP: 

1. Disable the GCP (write 0 to MCR[GPREN]). 

2. Specify the new prescaler value (write GCP – 1 to MCR[GPRE]. 

3. Enable the GCP (write 1 to MCR[GPREN]). 

### 61.7.6 Freeze and chip Debug mode 

#### 61.7.6.1 Enter and exit Freeze state 

When the chip is in Debug mode (the chip Debug signal is asserted), you can freeze individual UCs. For the effects of Freeze state on eMIOS functions, see Freeze effects. 

To put a channel in Freeze state, you must meet all of the following conditions: 

- The chip must assert Debug. 

- Prepare eMIOS for the Freeze state (write 1 to MCR[FRZ]). 

- Enable Freeze for each channel you want to freeze: 

   - Write 1 to Cn[FREN]. 

A channel exits Freeze state when any of the following conditions occur: 

- The chip deasserts Debug. 

- You take eMIOS out of the Freeze state (write 0 to MCR[FRZ]). 

- You disable Freeze for the channel: 

   - write 0 to Cn[FREN]. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2221 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

#### 61.7.6.2 Freeze effects 

|Function|Effects of freeze|
|---|---|
|GCP|No effect|
|UC|• Halts counter, capture, and compare operation.|
||• Freezes UC in its current state.|
||• Makes all registers accessible.<br>• In output modes, force match remains operational, allowing software to force the output to the<br>desired level.<br>• In input modes, the UC ignores input events.|
||• When eMIOS exits Freeze state then UC operations resume, but they may be inconsistent until<br>the UC reenters GPIO mode.|
|STAC|No effect|
|BIU|No effect|



## 61.8 Initialization information 

When initializing eMIOS, take the following considerations into account. 

For eMIOS behavior on reset, see Reset. 

Before changing the UC operating mode, you must: 

1. Put the UC in GPIO mode (write 0b or 1b to Cn[MODE]). 

2. Write the correct values for the next operating mode to An and Bn. 

3. Put the UC in the new operating mode (write the appropriate value to Cn[MODE]). 

If you change a UC from one mode to another without performing this procedure, the first operation cycle of the selected timebase can be random; that is, matches can occur in random time because you did not update An and Bn with correct values before the timebase matches the previous contents of either register. 

When you enable interrupts, any interrupt service routine must clear the flag before exiting. 

## 61.9 Application information 

### 61.9.1 Overview 

All output operation modes can generate correlated output signals. You can disable updates of the output signals for each UC (OUDIS). 

To guarantee that incrementing of the internal counters of correlated channels occurs in the same clock cycle, you must configure the internal CPs before enabling the GCP. If you configure the internal CPs after enabling the GCP, the internal counters may increment in the same ratio, but at different clock cycles. 

You should drive the Output Disable Input signals with the flag signals of some UCs running in SAIC mode. When an output disable condition happens, the interrupt service routine must process the output channels before processing the channels running SAIC. This sequence avoids glitches in the output pins. 

### 61.9.2 Timebase generation 

In the MC and OPWFM modes with internal clock sources, you can modify the internal counter rate by configuring the CP ratio. Timebase with the fastest prescaler ratio illustrates a timebase with a prescaler ratio of one. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2222 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

~~<mark>NOTE</mark>~~ 

The buffered modes, MCB and OPWFMB, behave differently. 

If the prescaler ratio is greater than one or you select an external clock, the internal counter behaves in one of four different ways depending on the channel mode: 

- In MC mode with Clear on Match Start and External Clock: Timebase generation with clear on match start and external clock. 

- In MC mode with Clear on Match Start and Internal Clock source: Timebase generation with clear on match start and internal clock. 

- In MC mode with Clear on Match End: Timebase generation with clear on match end. 

- In OPWFM mode: Timebase generation with clear on match start and internal clock. The internal counter clears at the start of the match signal, skips the next prescaled clock edge, and then increments in the subsequent prescaled clock edge. 

### 61.9.3 Timebase with the fastest prescaler ratio 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2223-10.png)


<!-- Start of picture text -->
C n [UCPRE] = 0b (Prescaler = 1)<br>System clock<br>Input event or prescaler clock enable = 1<br>See note 1<br>Internal counter 1 2 3 0 1 2 3 0 1 2 3 0 1 2 3 0 1 2 3 0 1 2 3<br>Match value = 3<br>Set flag event<br>S n [FLAG]<br>Clear flag event<br>Note 1: When a match occurs, eMIOS resets the internal counter<br>in the first cycle, which starts another period.<br><!-- End of picture text -->

Figure 340. Timebase with fastest prescaler ratio 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2223 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

### 61.9.4 Timebase generation with clear on match start and external clock 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2224-03.png)


<!-- Start of picture text -->
System clock<br>Input event<br>Internal counter 1 2 3 0 1 2 3 0 1 2<br>See note 1<br>Match value = 3<br>Set flag event<br>S n [FLAG]<br>Clear flag event<br><!-- End of picture text -->

Note 1: When a match occurs, eMIOS resets the internal counter in the first clock cycle. The counter starts counting at the next edge of the prescaler clock enable. 

Figure 341. Timebase generation with clear on match start and external clock 

### 61.9.5 Timebase generation with clear on match start and internal clock 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2224-07.png)


<!-- Start of picture text -->
Prescaler = 3 (C n [UCPRE] = 10b)<br>System clock<br>Prescaer enabled (C n [UCPREN] = 1b)<br>Internal counter 1 2 3 0 0 1 2 3 0 0<br>See note 1<br>Match value = 3<br>Set flag event<br>S n [FLAG]<br>Clear flag event<br>Note 1: When a match occurs, eMIOS clears the internal counter in the first clock cycle.<br>The counter starts counting again only after the second edge of the prescaled clock.<br><!-- End of picture text -->

Figure 342. Timebase generation with clear on match start and internal clock 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2224 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

### 61.9.6 Timebase generation with clear on match end 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2225-03.png)


<!-- Start of picture text -->
System clock<br>Input event or prescaler clock enable<br>Internal counter 1 2 3 0 1 2 3 0<br>See note 1<br>Match value = 3<br>Set flag event<br>S n [FLAG]<br>Clear flag event<br><!-- End of picture text -->

Note 1: The match occurs only when the input event or prescaler clock enable is active. When the match occurs, eMIOS resets the internal counter immediately. 

Figure 343. Timebase generation with clear on match end 

### 61.9.7 Coherent accesses 

Reading An[A] again in the same period as the last read of Bn[B] results in incoherent results if the last read of Bn[B] occurred after a disabled BS2→BS1 transfer. 

### 61.9.8 Initializing channels and modes 

Perform the following basic steps for output mode startup. This procedure assumes the channels are initially in GPIO mode: 

1. Disable the GPC (write 0 to MCR[GPREN]). 

2. For each timebase UC: 

   - a. Disable the CP (write 0 to Cn[UCPREN]). 

   - b. Write an initial value to the internal counter (CNTn[C]). 

   - c. Write initial values to An[A] and Bn[B]. 

   - d. Configure the UC for MC or MCB Up mode (write the appropriate value to Cn[MODE]). 

   - e. Select the CP ratio (Cn[UCPRE]). 

   - f. Enable the CP (write 1 to Cn[UCPREN]). 

3. For each output UC: 

   - a. Disable the CP (write 0 to Cn[UCPREN]). 

   - b. Write initial values to An[A] and Bn[B]. 

   - c. Select the timebase input (Cn[BSL]). 

   - d. Specify the output mode (write the appropriate value to Cn[MODE]). 

   - e. Select the same CP ratio as the timebase UC (Cn[UCPRE]). 

   - f. Enable the CP (write 1 to Cn[UCPREN]). 

4. Enable the GPC (write 1 to MCR[GPREN]). 

5. Enable GBTE (write 1 to MCR[GBTE]). 

The timebase channel and the output channel may be the same for some applications such as in OPWFM or OPWFMB mode, or whenever the output channel drives the timebase itself. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2225 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

You may configure flags at any time. 

## 61.10 Memory maps and registers 

### 61.10.1 Overall address map organization 

All address locations not explicitly mentioned in this table are reserved. When you access an absent register, absent channel, or reserved address space, the transfer terminates with an error. 

Table 356. Overall address map organization 

|Base address (hex)|Description|
|---|---|
|0|Module Configuration (MCR)|
|4|Global Flag (GFLAG)|
|8|Output Update Disable (OUDIS)|
|C|Disable Channel (UCDIS)|
|20|Channels 0–7|
|120|Channels 8–15|
|220|Channels 16–23|



### 61.10.2 UC memory overview 

Table 357. UC memory overview 

|Offset from UC n base<br>address (hex)|Description|
|---|---|
|0|UC A n (A0 - A23)|
|4|UC B n (B0 - B23)|
|8|UC Counter n (CNT0 - CNT23)|
|C|UC Control n (C0 - C23)|
|10|UC Status n (S0 - S23)|
|14|Alternate Address n (ALTA0 - ALTA23)|
|18|UC Control 2 n (C2_0 - C2_23)|
|1C–1F|Reserved|



### 61.10.3 AS1, AS2, BS1, and BS2 shadow registers 

When you use eMIOS UC modes, you rely heavily on four shadow registers: 

- AS1 

- AS2 

- BS1 

- BS2 

You use An[A], Bn[B], and ALTAn[ALTA] to access these shadow registers: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2226 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

- Each instance of An[A] has a separate associated instance of AS1 and AS2. In some UC modes, you also use ALTAn[ALTA] to access AS2. 

- Each instance of Bn[B] has a separate associated instance of BS1 and BS2. 

See Relationship between An, Bn, ALTAn, and shadow registers. 

Each UC mode uses the AS1-AS2 and BS1-BS2 shadow register pairs for various match and capture functions, as described in Unified channels (UC). 

A reset clears all shadow registers. 

Assignment of values for An[A], Bn[B], and ALTAn[ALTA] describes how you write to and read from the shadow registers for all operation modes. Values not listed are reserved. For more information, see Unified channels (UC). 

### 61.10.4 Relationship between An, Bn, ALTAn, and shadow registers 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2227-09.png)


<!-- Start of picture text -->
A n  register array A shadow registers ALTA n  register array B n  register array B shadow registers<br>AS1 BS1<br>A0 ALTA0 B0<br>AS2 BS2<br>AS1 BS1<br>A1 ALTA1 B1<br>AS2 BS2<br>AS1 BS1<br>A2 ALTA2 B2<br>AS2 BS2<br>AS1 BS1<br>A3 ALTA3 B3<br>AS2 BS2<br>AS1 BS1<br>A4 ALTA4 B4<br>AS2 BS2<br>... ... ...<br>AS1 BS1<br>A n ALTA n B n<br>AS2 BS2<br><!-- End of picture text -->

Figure 344. Relationship between An, Bn, ALTAn, and shadow registers 

### 61.10.5 Assignment of values for An[A], Bn[B], and ALTAn[ALTA] 

This table describes how you write to and read from the following registers for all operation modes: 

- UC A n (A0 - A23) 

- UC B n (B0 - B23) 

- Alternate Address n (ALTA0 - ALTA23) 

Values not listed are reserved. For more information, see Unified channels (UC). 

Table 358. Assignment of values for An[A], Bn[B], and ALTAn[ALTA] 

||||Register ac|cess||||
|---|---|---|---|---|---|---|---|
|Operation mode|An||Bn||AL|T|An|
||Write|Read|Write|Read|Write||Read|
|GPIO|AS1 and AS2<sup>1</sup>|AS1|BS1 and BS2<sup>2</sup>|BS1|AS2||AS2|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2227 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

Table 358. Assignment of values for An[A], Bn[B], and ALTAn[ALTA] (continued) 

||||Register|access|||
|---|---|---|---|---|---|---|
|Operation mode|A|n|B|n|AL|TAn|
||Write|Read|Write|Read|Write|Read|
|SAIC<sup>3</sup>|—|AS2|BS2|BS2|—|—|
|SAOC<sup>3</sup>|AS2|AS1|BS2|BS2|—|—|
|IPWM|—|AS2|—|BS1|—|—|
|IPM|—|AS2|—|BS1|—|—|
|DAOC|AS2|AS1|BS2|BS1|—|—|
|PEA|AS1|AS2|—|BS1|—|—|
|PEC<sup>3</sup>|AS1|AS1|BS1|BS1|—|AS2|
|WPTA|AS1|AS1|BS1|BS1|—|AS2|
|MC<sup>3</sup>|AS2|AS1|BS2|BS2|—|—|
|OPWFM|AS2|AS1|BS2|BS1|—|—|
|OPWMC|AS2|AS1|BS2|BS1|—|—|
|OPWM|AS2|AS1|BS2|BS1|—|—|
|OPWMT|AS1|AS1|BS2|BS1|AS2|AS2|
|MCB<sup>3</sup>|AS2|AS1|BS2|BS1|—|—|
|OPWFMB|AS2|AS1|BS2|BS1|—|—|
|OPWMCB|AS2|AS1|BS2|BS1|—|—|
|OPWMB|AS2|AS1|BS2|BS1|—|—|



> 1. This operation writes the same value to AS1 and AS2. 

2. This operation writes the same value to BS1 and BS2. 

3. These modes do not require UC B n (B0 - B23), but you can still use it to access BS2. 

### 61.10.6 eMIOS register descriptions 

All control registers are 32 bits wide. Data fields are 16 bits wide. There are 24 UCs, as mapped in Counter buses, channels, and timebase sources. 

#### 61.10.6.1 eMIOS memory map 

eMIOS_0 base address: 4008_8000h 

eMIOS_1 base address: 4008_C000h 

eMIOS_2 base address: 4009_0000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|Module Configuration (MCR)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2228 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|4h|Global Flag (GFLAG)|32|RO|0000_0000h|
|8h|Output Update Disable (OUDIS)|32|RW|0000_0000h|
|Ch|Disable Channel (UCDIS)|32|RW|0000_0000h|
|20h|UC A 0 (A0)|32|RW|0000_0000h|
|24h|UC B 0 (B0)|32|RW|0000_0000h|
|28h|UC Counter 0 (CNT0)|32|RW|0000_0000h|
|2Ch|UC Control 0 (C0)|32|RW|0000_0000h|
|30h|UC Status 0 (S0)|32|W1C|See<br>description|
|34h|Alternate Address 0 (ALTA0)|32|RW|0000_0000h|
|38h|UC Control 2 0 (C2_0)|32|RW|0000_0000h|
|40h|UC A 1 (A1)|32|RW|0000_0000h|
|44h|UC B 1 (B1)|32|RW|0000_0000h|
|48h|UC Counter 1 (CNT1)|32|RW|0000_0000h|
|4Ch|UC Control 1 (C1)|32|RW|0000_0000h|
|50h|UC Status 1 (S1)|32|W1C|See<br>description|
|54h|Alternate Address 1 (ALTA1)|32|RW|0000_0000h|
|58h|UC Control 2 1 (C2_1)|32|RW|0000_0000h|
|60h|UC A 2 (A2)|32|RW|0000_0000h|
|64h|UC B 2 (B2)|32|RW|0000_0000h|
|68h|UC Counter 2 (CNT2)|32|RW|0000_0000h|
|6Ch|UC Control 2 (C2)|32|RW|0000_0000h|
|70h|UC Status 2 (S2)|32|W1C|See<br>description|
|74h|Alternate Address 2 (ALTA2)|32|RW|0000_0000h|
|78h|UC Control 2 2 (C2_2)|32|RW|0000_0000h|
|80h|UC A 3 (A3)|32|RW|0000_0000h|
|84h|UC B 3 (B3)|32|RW|0000_0000h|
|88h|UC Counter 3 (CNT3)|32|RW|0000_0000h|
|8Ch|UC Control 3 (C3)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2229 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|90h|UC Status 3 (S3)|32|W1C|See<br>description|
|94h|Alternate Address 3 (ALTA3)|32|RW|0000_0000h|
|98h|UC Control 2 3 (C2_3)|32|RW|0000_0000h|
|A0h|UC A 4 (A4)|32|RW|0000_0000h|
|A4h|UC B 4 (B4)|32|RW|0000_0000h|
|A8h|UC Counter 4 (CNT4)|32|RW|0000_0000h|
|ACh|UC Control 4 (C4)|32|RW|0000_0000h|
|B0h|UC Status 4 (S4)|32|W1C|See<br>description|
|B4h|Alternate Address 4 (ALTA4)|32|RW|0000_0000h|
|B8h|UC Control 2 4 (C2_4)|32|RW|0000_0000h|
|C0h|UC A 5 (A5)|32|RW|0000_0000h|
|C4h|UC B 5 (B5)|32|RW|0000_0000h|
|C8h|UC Counter 5 (CNT5)|32|RW|0000_0000h|
|CCh|UC Control 5 (C5)|32|RW|0000_0000h|
|D0h|UC Status 5 (S5)|32|W1C|See<br>description|
|D4h|Alternate Address 5 (ALTA5)|32|RW|0000_0000h|
|D8h|UC Control 2 5 (C2_5)|32|RW|0000_0000h|
|E0h|UC A 6 (A6)|32|RW|0000_0000h|
|E4h|UC B 6 (B6)|32|RW|0000_0000h|
|E8h|UC Counter 6 (CNT6)|32|RW|0000_0000h|
|ECh|UC Control 6 (C6)|32|RW|0000_0000h|
|F0h|UC Status 6 (S6)|32|W1C|See<br>description|
|F4h|Alternate Address 6 (ALTA6)|32|RW|0000_0000h|
|F8h|UC Control 2 6 (C2_6)|32|RW|0000_0000h|
|100h|UC A 7 (A7)|32|RW|0000_0000h|
|104h|UC B 7 (B7)|32|RW|0000_0000h|
|108h|UC Counter 7 (CNT7)|32|RW|0000_0000h|
|10Ch|UC Control 7 (C7)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2230 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|110h|UC Status 7 (S7)|32|W1C|See<br>description|
|114h|Alternate Address 7 (ALTA7)|32|RW|0000_0000h|
|118h|UC Control 2 7 (C2_7)|32|RW|0000_0000h|
|120h|UC A 8 (A8)|32|RW|0000_0000h|
|124h|UC B 8 (B8)|32|RW|0000_0000h|
|128h|UC Counter 8 (CNT8)|32|RW|0000_0000h|
|12Ch|UC Control 8 (C8)|32|RW|0000_0000h|
|130h|UC Status 8 (S8)|32|W1C|See<br>description|
|134h|Alternate Address 8 (ALTA8)|32|RW|0000_0000h|
|138h|UC Control 2 8 (C2_8)|32|RW|0000_0000h|
|140h|UC A 9 (A9)|32|RW|0000_0000h|
|144h|UC B 9 (B9)|32|RW|0000_0000h|
|14Ch|UC Control 9 (C9)|32|RW|0000_0000h|
|150h|UC Status 9 (S9)|32|W1C|See<br>description|
|154h|Alternate Address 9 (ALTA9)|32|RW|0000_0000h|
|158h|UC Control 2 9 (C2_9)|32|RW|0000_0000h|
|160h|UC A 10 (A10)|32|RW|0000_0000h|
|164h|UC B 10 (B10)|32|RW|0000_0000h|
|16Ch|UC Control 10 (C10)|32|RW|0000_0000h|
|170h|UC Status 10 (S10)|32|W1C|See<br>description|
|174h|Alternate Address 10 (ALTA10)|32|RW|0000_0000h|
|178h|UC Control 2 10 (C2_10)|32|RW|0000_0000h|
|180h|UC A 11 (A11)|32|RW|0000_0000h|
|184h|UC B 11 (B11)|32|RW|0000_0000h|
|18Ch|UC Control 11 (C11)|32|RW|0000_0000h|
|190h|UC Status 11 (S11)|32|W1C|See<br>description|
|194h|Alternate Address 11 (ALTA11)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2231 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|198h|UC Control 2 11 (C2_11)|32|RW|0000_0000h|
|1A0h|UC A 12 (A12)|32|RW|0000_0000h|
|1A4h|UC B 12 (B12)|32|RW|0000_0000h|
|1ACh|UC Control 12 (C12)|32|RW|0000_0000h|
|1B0h|UC Status 12 (S12)|32|W1C|See<br>description|
|1B4h|Alternate Address 12 (ALTA12)|32|RW|0000_0000h|
|1B8h|UC Control 2 12 (C2_12)|32|RW|0000_0000h|
|1C0h|UC A 13 (A13)|32|RW|0000_0000h|
|1C4h|UC B 13 (B13)|32|RW|0000_0000h|
|1CCh|UC Control 13 (C13)|32|RW|0000_0000h|
|1D0h|UC Status 13 (S13)|32|W1C|See<br>description|
|1D4h|Alternate Address 13 (ALTA13)|32|RW|0000_0000h|
|1D8h|UC Control 2 13 (C2_13)|32|RW|0000_0000h|
|1E0h|UC A 14 (A14)|32|RW|0000_0000h|
|1E4h|UC B 14 (B14)|32|RW|0000_0000h|
|1ECh|UC Control 14 (C14)|32|RW|0000_0000h|
|1F0h|UC Status 14 (S14)|32|W1C|See<br>description|
|1F4h|Alternate Address 14 (ALTA14)|32|RW|0000_0000h|
|1F8h|UC Control 2 14 (C2_14)|32|RW|0000_0000h|
|200h|UC A 15 (A15)|32|RW|0000_0000h|
|204h|UC B 15 (B15)|32|RW|0000_0000h|
|20Ch|UC Control 15 (C15)|32|RW|0000_0000h|
|210h|UC Status 15 (S15)|32|W1C|See<br>description|
|214h|Alternate Address 15 (ALTA15)|32|RW|0000_0000h|
|218h|UC Control 2 15 (C2_15)|32|RW|0000_0000h|
|220h|UC A 16 (A16)|32|RW|0000_0000h|
|224h|UC B 16 (B16)|32|RW|0000_0000h|
|228h|UC Counter 16 (CNT16)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2232 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|22Ch|UC Control 16 (C16)|32|RW|0000_0000h|
|230h|UC Status 16 (S16)|32|W1C|See<br>description|
|234h|Alternate Address 16 (ALTA16)|32|RW|0000_0000h|
|238h|UC Control 2 16 (C2_16)|32|RW|0000_0000h|
|240h|UC A 17 (A17)|32|RW|0000_0000h|
|244h|UC B 17 (B17)|32|RW|0000_0000h|
|24Ch|UC Control 17 (C17)|32|RW|0000_0000h|
|250h|UC Status 17 (S17)|32|W1C|See<br>description|
|254h|Alternate Address 17 (ALTA17)|32|RW|0000_0000h|
|258h|UC Control 2 17 (C2_17)|32|RW|0000_0000h|
|260h|UC A 18 (A18)|32|RW|0000_0000h|
|264h|UC B 18 (B18)|32|RW|0000_0000h|
|26Ch|UC Control 18 (C18)|32|RW|0000_0000h|
|270h|UC Status 18 (S18)|32|W1C|See<br>description|
|274h|Alternate Address 18 (ALTA18)|32|RW|0000_0000h|
|278h|UC Control 2 18 (C2_18)|32|RW|0000_0000h|
|280h|UC A 19 (A19)|32|RW|0000_0000h|
|284h|UC B 19 (B19)|32|RW|0000_0000h|
|28Ch|UC Control 19 (C19)|32|RW|0000_0000h|
|290h|UC Status 19 (S19)|32|W1C|See<br>description|
|294h|Alternate Address 19 (ALTA19)|32|RW|0000_0000h|
|298h|UC Control 2 19 (C2_19)|32|RW|0000_0000h|
|2A0h|UC A 20 (A20)|32|RW|0000_0000h|
|2A4h|UC B 20 (B20)|32|RW|0000_0000h|
|2ACh|UC Control 20 (C20)|32|RW|0000_0000h|
|2B0h|UC Status 20 (S20)|32|W1C|See<br>description|
|2B4h|Alternate Address 20 (ALTA20)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2233 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|2B8h|UC Control 2 20 (C2_20)|32|RW|0000_0000h|
|2C0h|UC A 21 (A21)|32|RW|0000_0000h|
|2C4h|UC B 21 (B21)|32|RW|0000_0000h|
|2CCh|UC Control 21 (C21)|32|RW|0000_0000h|
|2D0h|UC Status 21 (S21)|32|W1C|See<br>description|
|2D4h|Alternate Address 21 (ALTA21)|32|RW|0000_0000h|
|2D8h|UC Control 2 21 (C2_21)|32|RW|0000_0000h|
|2E0h|UC A 22 (A22)|32|RW|0000_0000h|
|2E4h|UC B 22 (B22)|32|RW|0000_0000h|
|2E8h|UC Counter 22 (CNT22)|32|RW|0000_0000h|
|2ECh|UC Control 22 (C22)|32|RW|0000_0000h|
|2F0h|UC Status 22 (S22)|32|W1C|See<br>description|
|2F4h|Alternate Address 22 (ALTA22)|32|RW|0000_0000h|
|2F8h|UC Control 2 22 (C2_22)|32|RW|0000_0000h|
|300h|UC A 23 (A23)|32|RW|0000_0000h|
|304h|UC B 23 (B23)|32|RW|0000_0000h|
|308h|UC Counter 23 (CNT23)|32|RW|0000_0000h|
|30Ch|UC Control 23 (C23)|32|RW|0000_0000h|
|310h|UC Status 23 (S23)|32|W1C|See<br>description|
|314h|Alternate Address 23 (ALTA23)|32|RW|0000_0000h|
|318h|UC Control 2 23 (C2_23)|32|RW|0000_0000h|



#### 61.10.6.2 Module Configuration (MCR) 

##### Offset 

|Register|Offset|
|---|---|
|MCR|0h|



##### Function 

Configures eMIOS operation. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2234 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2235-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R 0<br>Reserv MDIS  FRZ  GTBE  ed  GPRE<br>ed  N<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>GPRE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Reserved|
|—|Write only the reset value to this field.|
|30|Module Disable|
|MDIS|Disables eMIOS by stopping the clock.<br>When you disable eMIOS, its clock stops, it consumes less power, and you can access only the<br>following registers:<br>• Module Configuration (MCR)<br>• Output Update Disable (OUDIS)<br>• Disable Channel (UCDIS)|
||0b - Enable|
||1b - Disable|
|29|Freeze|
|FRZ|Prepares eMIOS to enter Freeze state (seeFreeze and chip Debug mode). eMIOS does not enter Freeze<br>state until both of the following conditions occur:<br>• The chip asserts Debug mode.<br>• You enable Freeze for each UC (write 1 toCn[FREN]).<br>A channel remains frozen until one or more of the following occur:<br>• You force eMIOS to exit the Freeze state (write 0 to FRZ).<br>• The chip deasserts Debug mode.<br>• You disable Freeze for that UC (write 0 toCn[FREN]).<br>0b - Exit Freeze state<br>1b - Enter Freeze state|
|28|Global Timebase Enable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2235 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|GTBE|Asserts the GTBE_OUT signal. If GTBE_OUT is connected to the GTBE_IN input of one or more eMIOS<br>instances, asserting the signal turns on the internal counters of those eMIOS instances simultaneously.<br>The GTBE_IN input enables (asserted) or disables (deasserted) the internal counters.<br>~~NOTE~~<br>0b - Deassert GTBE_OUT<br>1b - Assert GTBE_OUT|
|27<br>—|Reserved|
|26<br>GPREN|Global Prescaler Enable<br>Enables the global prescaler counter. Disabling the global prescaler clears the prescaler counter and stops<br>the prescaler clock.<br>0b - Disable<br>1b - Enable|
|25-16<br>—<br>15-8<br>GPRE|Reserved<br>Global Prescaler<br>Specifies the global clock prescaler. Write the desired clock divide ratio minus 1. For example, for a divide<br>ratio of 8, write 111b. The prescaler can range from 1 (0b) to 256 (11111111b).|
|7-0<br>—|Reserved|



#### 61.10.6.3 Global Flag (GFLAG) 

##### Offset 

|Register|Offset|
|---|---|
|GFLAG|4h|



##### Function 

Groups the flag fields from all channels into one register to improve interrupt handling. 

For UCs, each field mirrors the corresponding channel flag (Sn[FLAG]). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2236 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|0|0|0|0|0|0|0|0|F23|F22|F21|F20|F19|F18|F17|F16|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|F15|F14|F13|F12|F11|F10|F9|F8|F7|F6|F5|F4|F3|F2|F1|F0|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31<br>—|Reserved|
|30<br>—|Reserved|
|29<br>—|Reserved|
|28<br>—|Reserved|
|27<br>—|Reserved|
|26<br>—|Reserved|
|25<br>—|Reserved|
|24<br>—|Reserved|
|23<br>F23|Mirror of UC 23 FLAG|
|22<br>F22|Mirror of UC 22 FLAG<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2237 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

Table continued from the previous page... 

|Field|Function||
|---|---|---|
|21|Mirror of|UC 21 FLAG|
|F21|||
|20|Mirror of|UC 20 FLAG|
|F20|||
|19|Mirror of|UC 19 FLAG|
|F19|||
|18|Mirror of|UC 18 FLAG|
|F18|||
|17|Mirror of|UC 17 FLAG|
|F17|||
|16|Mirror of|UC 16 FLAG|
|F16|||
|15|Mirror of|UC 15 FLAG|
|F15|||
|14|Mirror of|UC 14 FLAG|
|F14|||
|13|Mirror of|UC 13 FLAG|
|F13|||
|12|Mirror of|UC 12 FLAG|
|F12|||
|11|Mirror of|UC 11 FLAG|
|F11|||
|10|Mirror of|UC 10 FLAG|
|F10|||
|9|Mirror of|UC 9 FLAG|
|F9|||
|8|Mirror of|UC 8 FLAG|
|F8|||
|7|Mirror of|UC 7 FLAG|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2238 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|F7||
|6<br>F6|Mirror of UC 6 FLAG|
|5|Mirror of UC 5 FLAG|
|F5||
|4<br>F4|Mirror of UC 4 FLAG|
|3<br>F3|Mirror of UC 3 FLAG|
|2<br>F2|Mirror of UC 2 FLAG|
|1<br>F1|Mirror of UC 1 FLAG|
|0<br>F0|Mirror of UC 0 FLAG|



#### 61.10.6.4 Output Update Disable (OUDIS) 

##### Offset 

|Register|Offset|
|---|---|
|OUDIS|8h|



##### Function 

Disables transfers from AS2 to AS1 and BS2 to BS1 on a per-channel basis. This applies to any channel operating in MC, MCB, or any output mode that writes to AS2 and BS2. 

When a field is 0, transfers on that channel occur immediately or in the next period, depending on the operation mode. Unless that mode's description states otherwise, the transfer occurs immediately. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2239 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|0|0|0|0|0|0|0|0|OU23|OU22|OU21|OU20|OU19|OU18|OU17|OU16|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|OU15|OU14|OU13|OU12|OU11|OU10|OU9|OU8|OU7|OU6|OU5|OU4|OU3|OU2|OU1|OU0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31<br>—|Reserved|
|30<br>—|Reserved|
|29<br>—|Reserved|
|28<br>—|Reserved|
|27<br>—|Reserved|
|26<br>—|Reserved|
|25<br>—|Reserved|
|24<br>—|Reserved|
|23|Channel 23 Output Update Disable|
|OU23|0b - Enable<br>1b - Disable|
|22|Channel 22 Output Update Disable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2240 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|OU22|0b - Enable<br>1b - Disable|
|21|Channel 21 Output Update Disable|
|OU21|0b - Enable<br>1b - Disable|
|20|Channel 20 Output Update Disable|
|OU20|0b - Enable<br>1b - Disable|
|19|Channel 19 Output Update Disable|
|OU19|0b - Enable<br>1b - Disable|
|18|Channel 18 Output Update Disable|
|OU18|0b - Enable<br>1b - Disable|
|17|Channel 17 Output Update Disable|
|OU17|0b - Enable<br>1b - Disable|
|16|Channel 16 Output Update Disable|
|OU16|0b - Enable<br>1b - Disable|
|15<br>OU15|Channel 15 Output Update Disable<br>0b - Enable<br>1b - Disable|
|14|Channel 14 Output Update Disable|
|OU14|0b - Enable<br>1b - Disable|
|13|Channel 13 Output Update Disable|
|OU13|0b - Enable<br>1b - Disable|
|12|Channel 12 Output Update Disable|
|OU12|0b - Enable<br>1b - Disable<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2241 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|11|Channel 11 Output Update Disable|
|OU11|0b - Enable<br>1b - Disable|
|10|Channel 10 Output Update Disable|
|OU10|0b - Enable<br>1b - Disable|
|9<br>OU9|Channel 9 Output Update Disable<br>0b - Enable<br>1b - Disable|
|8<br>OU8|Channel 8 Output Update Disable<br>0b - Enable<br>1b - Disable|
|7<br>OU7|Channel 7 Output Update Disable<br>0b - Enable<br>1b - Disable|
|6<br>OU6|Channel 6 Output Update Disable<br>0b - Enable<br>1b - Disable|
|5<br>OU5|Channel 5 Output Update Disable<br>0b - Enable<br>1b - Disable|
|4<br>OU4|Channel 4 Output Update Disable<br>0b - Enable<br>1b - Disable|
|3|Channel 3 Output Update Disable|
|OU3|0b - Enable<br>1b - Disable|
|2|Channel 2 Output Update Disable|
|OU2|0b - Enable<br>1b - Disable|
|1<br>OU1|Channel 1 Output Update Disable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2242 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Enable|
||1b - Disable|
|0|Channel 0 Output Update Disable|
|OU0|0b - Enable|
||1b - Disable|



#### 61.10.6.5 Disable Channel (UCDIS) 

##### Offset 

|Register|Offset|
|---|---|
|UCDIS|Ch|



##### Function 

Allows you to disable a UC by stopping its clock. Each field controls the clock for the corresponding UC. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|0|0|0|0|0|0|0|0|UCDIS|UCDIS|UCDIS|UCDIS|UCDIS|UCDIS|UCDIS|UCDIS|
|W|||||||||23|22|21|20|19|18|17|16|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|UCDIS<br>15|UCDIS<br>14|UCDIS<br>13|UCDIS<br>12|UCDIS<br>11|UCDIS<br>10|UCDIS<br>9|UCDIS<br>8|UCDIS<br>7|UCDIS<br>6|UCDIS<br>5|UCDIS<br>4|UCDIS<br>3|UCDIS<br>2|UCDIS<br>1|UCDIS<br>0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31<br>—|Reserved|
|30<br>—|Reserved|
|29|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2243 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

Table continued from the previous page... 

|Field|Function||
|---|---|---|
|—<br>28<br>—|Reserved||
|27<br>—|Reserved||
|26<br>—|Reserved||
|25<br>—|Reserved||
|24<br>—|Reserved||
|23|Disable UC|23|
|UCDIS23|0b -<br>1b -|Enable<br>Disable|
|22|Disable UC|22|
|UCDIS22|0b -<br>1b -|Enable<br>Disable|
|21|Disable UC|21|
|UCDIS21|0b -|Enable|
||1b -|Disable|
|20|Disable UC|20|
|UCDIS20|0b -<br>1b -|Enable<br>Disable|
|19|Disable UC|19|
|UCDIS19|0b -<br>1b -|Enable<br>Disable|
|18|Disable UC|18|
|UCDIS18|0b -|Enable|
||1b -|Disable|
|17|Disable UC|17|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2244 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

Table continued from the previous page... 

|Field|Function||
|---|---|---|
|UCDIS17|0b -<br>1b -|Enable<br>Disable|
|16|Disable UC|16|
|UCDIS16|0b -<br>1b -|Enable<br>Disable|
|15|Disable UC|15|
|UCDIS15|0b -<br>1b -|Enable<br>Disable|
|14|Disable UC|14|
|UCDIS14|0b -<br>1b -|Enable<br>Disable|
|13|Disable UC|13|
|UCDIS13|0b -<br>1b -|Enable<br>Disable|
|12|Disable UC|12|
|UCDIS12|0b -<br>1b -|Enable<br>Disable|
|11|Disable UC|11|
|UCDIS11|0b -<br>1b -|Enable<br>Disable|
|10|Disable UC|10|
|UCDIS10|0b -|Enable|
||1b -|Disable|
|9|Disable UC|9|
|UCDIS9|0b -|Enable|
||1b -|Disable|
|8|Disable UC|8|
|UCDIS8|0b -|Enable|
||1b -|Disable|
|7|Disable UC|7|
|UCDIS7|0b -<br>1b -|Enable<br>Disable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2245 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|6|Disable UC 6|
|UCDIS6|0b - Enable<br>1b - Disable|
|5|Disable UC 5|
|UCDIS5|0b - Enable|
||1b - Disable|
|4|Disable UC 4|
|UCDIS4|0b - Enable|
||1b - Disable|
|3|Disable UC 3|
|UCDIS3|0b - Enable|
||1b - Disable|
|2|Disable UC 2|
|UCDIS2|0b - Enable|
||1b - Disable|
|1|Disable UC 1|
|UCDIS1|0b - Enable|
||1b - Disable|
|0|Disable UC 0|
|UCDIS0|0b - Enable|
||1b - Disable|



#### 61.10.6.6 UC A n (A0 - A23) 

##### Offset 

For n = 0 to 23: 

|Register|Offset|
|---|---|
|An|20h + (n × 20h)|



##### Function 

Accesses the AS1 and AS2 shadow registers for each UC, depending on the selected UC mode. See AS1, AS2, BS1, and BS2 shadow registers. 

For information about how you write to and read from An, Bn, and ALTAn for all UC modes, see Assignment of values for An[A], Bn[B], and ALTAn[ALTA]. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2246 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2247-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>A<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16<br>—|Reserved|
|15-0|A|
|A|See the register description.|



#### 61.10.6.7 UC B n (B0 - B23) 

##### Offset 

For n = 0 to 23: 

|Register<br>Bn|Offset<br>24h + (n × 20h)|
|---|---|



##### Function 

Accesses the BS1 and BS2 shadow registers for each UC, depending on the selected UC mode. See AS1, AS2, BS1, and BS2 shadow registers. 

For information about how you write to and read from An, Bn, and ALTAn for all UC modes, see Assignment of values for An[A], Bn[B], and ALTAn[ALTA]. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2247 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2248-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>B<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16<br>—|Reserved|
|15-0|B|
|B|See the register description.|



#### 61.10.6.8 UC Counter n (CNT0 - CNT23) 

##### Offset 

|Register|Offset|
|---|---|
|CNT0|28h|
|CNT1|48h|
|CNT2|68h|
|CNT3|88h|
|CNT4|A8h|
|CNT5|C8h|
|CNT6|E8h|
|CNT7|108h|
|CNT8|128h|
|CNT16|228h|
|CNT22|2E8h|
|CNT23|308h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2248 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

##### Function 

##### Indicates the value of the UC internal counter. 

When eMIOS is in GPIO mode or the UC is frozen, this register is read-write. For all other modes, this register is read-only. When entering some UC modes, eMIOS automatically clears this register. See Unified channels (UC) for details. 

The following modes use the UC counter: 

- Output Pulse Width and Frequency Modulation Buffered (OPWFMB) mode 

- Center Aligned Output PWM with Dead Time Insertion Buffered (OPWMCB) mode 

- Pulse Edge Counting (PEC) mode 

- Modulus Counter (MC) mode 

- Modulus Counter Buffered (MCB) mode 

All other modes not in this list do not use the internal counter. 

~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

|||Insta|nce||||Regis|ter supp|orted|Reg|ister n|ot sup|ported||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|eMIOS_0||||||CNT0–CN<br>CNT16<br>CNT22–C|T8<br>NT23|||—|||||
|eMIOS_1||||||CNT0<br>CNT8<br>CNT16<br>CNT22–C|NT23|||CNT1–CNT7|||||
|eMIOS_2||||||CNT0<br>CNT8<br>CNT16<br>CNT22–C|NT23|||CNT1–CNT7|||||
|Diagram|||||||||||||||
|Bits|31|30|29|28|27|26|25|24|23<br>22|21<br>20|19|18|17|16|
|R||||||||0|||||||
|W|||||||||||||||
|Reset|||||||See|Register|reset values.||||||
|Bits|15|14|13|12|11|10|9|8|7<br>6|5<br>4|3|2|1|0|
|R<br>W||||||||C|||||||



Reset 

See Register reset values. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2249 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

##### Register reset values 

|Register|Reset value|
|---|---|
|CNT0|eMIOS_0–eMIOS_2: 0000_0000h|
|CNT1–CNT7|0000_0000h|
|CNT8–CNT23|eMIOS_0–eMIOS_2: 0000_0000h|
|CNT9–CNT15|Register not supported|
|CNT17–CNT21|Register not supported|



##### Fields 

|Field|Function|
|---|---|
|31-16<br>—|Reserved|
|15-0|Internal Counter Value|
|C|Indicates the value of the internal counter.|



#### 61.10.6.9 UC Control n (C0 - C23) 

##### Offset 

For n = 0 to 23: 

|Register|Offset|
|---|---|
|Cn|2Ch + (n × 20h)|



Function 

Controls UC operation. 

Table 359. MODE field values 

|UC mode|MODE (binary)|
|---|---|
|GPIO (input)|000_0000|
|GPIO (output)|000_0001|
|SAIC|000_0010|
|SAIC with edge capturing|100_0010|
|SAOC|000_0011|
|IPWM|000_0100|
|IPM|000_0101|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2250 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

Table 359. MODE field values (continued) 

|UC mode|MODE (binary)|
|---|---|
|DAOC (with FLAG = 1 on B match)|000_0110|
|DAOC (with FLAG = 1 on A and B match)|000_0111|
|PEC (continuous)|000_1010|
|PEC (single shot)|000_1011|
|Reserved|000_1111|
|MC (up counter with clear on match start)|001_000p<sup>1</sup>|
|MC (up counter with clear on match end)|001_001p<sup>1</sup>|
|MC (up/down counter)|001_01pp<sup>1</sup>|
|Reserved|010_0100–010_0101|
|OPWMT|010_0110|
|Reserved|010_0111–100_1111|
|MCB (up counter)|101_000p<sup>1</sup>|
|Reserved|101_001p|
|MCB (up or down counter)|101_01pp<sup>1</sup>|
|OPWFMB|101_10p0<sup>1</sup>|
|Reserved|101_10p1|
|OPWMCB (with trailing edge dead time)|101_11p0<sup>1</sup>|
|OPWMCB (with leading edge dead time)|101_11p1<sup>1</sup>|
|OPWMB|110_00p0<sup>1</sup>|
|Reserved|110_0001–111_1111|



1. p = Adjust parameters for the mode of operation. See Unified channels (UC) for details. 

Table 360. Edge Polarity (EDPOL) settings 

|For these modes:|EDPOL does this:|and EDPOL values mean:|
|---|---|---|
|Input|Selects which edge triggers the internal counter, an<br>input capture, or the input capture flag. IfEDPOL<br>does not appear in the UC mode description, it has<br>no effect on UC operation.|0b - Trigger on a falling edge<br>1b - Trigger on a rising edge|
|Output|Selects the logic level on the output pin.|0b - A match on comparator A deasserts the<br>output flip-flop, while a match on comparator<br>B sets it<br>1b - A match on comparator A asserts the<br>output flip-flop, while a match on comparator<br>B clears it|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2251 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

Table 361. Edge Select (EDSEL) settings 

|For these modes:|EDSEL does this:|and EDSEL values mean:|
|---|---|---|
|Input|Selects whether the internal counter is triggered by<br>both edges of a pulse or by a single edge as defined<br>byEDPOL. If EDSEL does not appear in the UC<br>mode description, it has no effect on UC operation.|0b - Single-edge triggering on edge<br>specified inEDPOL<br>1b - Both-edges triggering|
|GPIO in|Selects whether an edge asserts the input capture<br>flag (Sn[FLAG]).|0b - SetsSn[FLAG]on the edge specified<br>inEDPOL<br>1b - Does not setSn[FLAG]|
|SAOC|Selects the behavior of the output flip-flop at each<br>match.|0b - Drive theEDPOLvalue on the<br>output flip-flop<br>1b - Toggle output flip-flop|



##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2252-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R UCPR 0 0<br>FREN  ODIS  ODISSL  UCPRE  DMA  IF  FCK  FEN<br>EN<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>EDSE EDPO<br>BSL  MODE<br>FORC FORC L  L<br>W<br>MA  MB<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Freeze Enable|
|FREN|Enables putting the UC in Freeze state. SeeFreeze and chip Debug mode.<br>0b - Disable|
||1b - Enable|
|30|Output Disable|
|ODIS|Disables the output pin when running any of the output modes except GPIO.<br>When you assert ODIS:|
||• If the selected Output Disable Input signal asserts, the output pin reflects:<br>— For OPWFMB and OPWMB modes, EDPOL (seeOutput Pulse Width and Frequency<br>Modulation Buffered (OPWFMB) modeandOutput PWM Buffered (OPWMB) mode).|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2252 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||— For all other modes, the complement of EDPOL, but the UC continues to operate normally—it<br>continues to generate flags and matches.<br>• If the selected Output Disable Input signal deasserts, the output pin operates normally.<br>0b - Enables output pin (the output pin operates normally)<br>1b - Disables output pin|
|29-28<br>ODISSL|Output Disable Select<br>Selects one of four output disable input signals.<br>00b - 0<br>01b - 1<br>10b - 2|
||11b - 3|
|27-26<br>UCPRE|Prescaler<br>Selects the clock divider value for the UC internal prescaler.|
||The two least-significant bits ofC2_n[UCEXTPRE]mirror UCPRE. Any write to UCPRE also<br>affects UCEXTPRE.<br>~~NOTE~~|
||00b - 1|
||01b - 2<br>10b - 3<br>11b - 4|
|25|Prescaler Enable|
|UCPREN|Enables the prescaler counter.<br>0b - Disable (no clock)<br>1b - Enable|
|24<br>DMA|Direct Memory Access<br>Selects whether the input capture flag (Sn[FLAG]) or overrun (Sn[OVR]) triggers an interrupt or<br>DMA request.<br>0b - Interrupt request<br>1b - DMA request|
|23<br>—|Reserved|
|22-19|Input Filter|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2253 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

##### Table continued from the previous page... 

|Field<br>IF|Function<br>Selects the minimum input pulse width, in filter clock cycles, that can pass through the input filter. This field<br>does not apply to output modes.<br>The filter latency—the difference in time between the input and the response—is three clock edges.<br>0000b - Bypassed; the input signal is synchronized before arriving at the digital filter<br>0001b - 2 cycles<br>0010b - 4 cycles<br>0100b - 8 cycles<br>1000b - 16 cycles<br>All other values are reserved.|
|---|---|
|18<br>FCK|Filter Clock Select<br>Selects the clock source for the programmable input filter.<br>0b - Prescaled clock<br>1b - eMIOS module clock|
|17<br>FEN|Flag Enable<br>Enables the input capture flag (Sn[FLAG]) to generate an interrupt request or a DMA request, as selected<br>inDMA.<br>0b - Disable<br>1b - Enable|
|16-14<br>—|Reserved|
|13|Force Match A|
|FORCMA|For output modes, asserting Force Match A causes the comparator to report a successful comparison on<br>comparator A regardless of whether a comparison actually occurred. It does not set the input capture flag<br>(Sn[FLAG]). This field always reads 0. This bit is meaningful for every output operation mode that uses<br>comparator A. Otherwise it has no effect.<br>0b - No effect<br>1b - Force a match at comparator A|
|12|Force Match B|
|FORCMB|For output modes, asserting Force Match B causes the comparator to report a successful comparison on<br>comparator B regardless of whether a comparison actually occurred. It does not set the input capture flag<br>(Sn[FLAG]does not become 1). This field always reads 0.<br>This field applies only if the UC is in one of the following output modes.<br>• Single Action Output Capture (SAOC) mode<br>• Double Action Output Compare (DAOC) mode|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2254 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||• Output Pulse Width and Frequency Modulation Buffered (OPWFMB) mode<br>• Center Aligned Output PWM with Dead Time Insertion Buffered (OPWMCB) mode<br>• Output PWM Buffered (OPWMB) mode<br>• Output PWM with Trigger (OPWMT) mode<br>This field has no effect in all other modes.<br>0b - No effect|
||1b - Force a match at comparator B|
|11<br>—<br>10-9<br>BSL|Reserved<br>Bus Select<br>Selects one of the counter buses or the internal counter for the UC.<br>Not all chips support all counter buses. See the chip-specific eMIOS information for details.<br>00b -<br>• Channels 0-22: counter bus A<br>• Channel 23: reserved<br>01b -<br>• Channels 1-7: counter bus B<br>• Channels 9-15: counter bus C<br>• Channels 17-23: counter bus D<br>• Channels 25-31: counter bus E<br>• Channels 0, 8, 16, 24: reserved<br>10b -<br>• Channels 0-21, 23: counter bus F<br>• Channel 22: reserved<br>11b - Internal counter for all channels|
|8|Edge Selection|
|EDSEL|Controls several functions as shown inTable 361.|
|7|Edge Polarity|
|EDPOL|Controls several functions as shown inTable 360.|
|6-0|Mode Selection|
|MODE|Selects the UC mode as shown inTable 359.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2255 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

##### Table continued from the previous page... 

|Field|Function||
|---|---|---|
|||If you write a reserved value to this field, the results are unpredictable.<br>~~NOTE~~|
|||When you change the value of MODE, you must first enter GPIO mode to reset the UC's<br>internal functions. Failure to do this can result in invalid and unexpected output compare or<br>input capture results or incorrectly set input capture flags (Sn[FLAG]).|



#### 61.10.6.10 UC Status n (S0 - S23) 

##### Offset 

For n = 0 to 23: 

|Register<br>Sn|Offset<br>30h + (n × 20h)|
|---|---|



##### Function 

Indicates the status of the UC input-output signals and the overflow condition of the internal counter. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2256-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R OVR  0<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>UCOU<br>R OVFL  0 UCIN  FLAG<br>T<br>W W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 u 1 0 0<br><!-- End of picture text -->

1. Reset value is undefined. 

##### Fields 

|Field|Function|
|---|---|
|31|Overrun|
|OVR|Indicates that FLAG generation occurred when FLAG was already 1.|
||Return OVR to 0 by writing 1 to either OVR or FLAG.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2256 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2257-03.png)


<!-- Start of picture text -->
Field Function<br>  NOTE<br>This field behaves differently for read and write operations.<br>When reading<br>0b - No overrun<br>1b - Overrun<br>When writing<br>0b - No overrun<br>1b - Return OVR to 0<br>30-16 Reserved<br>—<br>15 Overflow<br>OVFL Indicates that an overflow has occurred in the internal counter.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>eMIOS_0 S0–S8 S9–S15<br>S16 S17–S21<br>S22–S23<br>eMIOS_1 S0 S1–S7<br>S8 S9–S15<br>S16 S17–S21<br>S22–S23<br>eMIOS_2 S0 S1–S7<br>S8 S9–S15<br>S16 S17–S21<br>S22–S23<br>  NOTE<br>This field behaves differently for read and write operations.<br>When reading<br>0b - No overflow<br>1b - Overflow<br>When writing<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2257 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - No overflow<br>1b - Return OVFL to 0|
|14-3<br>—|Reserved|
|2<br>UCIN|UC Input Pin<br>Indicates the input pin state after the input pin has been filtered and synchronized.<br>0b - Negated|
||1b - Asserted|
|1|UC Output Pin|
|UCOUT|Indicates the output pin state.<br>0b - Negated<br>1b - Asserted|
|0<br>FLAG|Flag<br>Indicates that an input capture or a match event in the comparators has occurred.<br>This field behaves differently for read and write operations.<br>~~NOTE~~<br>When reading<br>0b - No event<br>1b - Event has occurred<br>When writing<br>0b - No event|
||1b - Clear the flag (FLAG returns to 0)|



#### 61.10.6.11 Alternate Address n (ALTA0 - ALTA23) 

##### Offset 

For n = 0 to 23: 

|Register<br>ALTAn|Offset<br>34h + (n × 20h)|
|---|---|



##### Function 

Provides an alternate address to access AS2 shadow registers in these restricted modes: 

- General-Purpose Input and Output (GPIO) mode 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2258 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

- Pulse Edge Counting (PEC) mode 

- Output PWM with Trigger (OPWMT) mode 

In these modes, you can use An[A] together with with ALTAn[ALTA] to access both AS1 and AS2. Assignment of values for An[A], Bn[B], and ALTAn[ALTA] summarizes the ALTAn writing and reading accesses for all ALTAn operation modes. 

In modes that do not require this register, any write access is ignored and any read access returns unspecified data. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2259-07.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>ALTA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16<br>—|Reserved|
|15-0|Alternate Address|
|ALTA|See the register description.|



#### 61.10.6.12 UC Control 2 n (C2_0 - C2_23) 

##### Offset 

For n = 0 to 23: 

|Register<br>C2_n|Offset<br>38h + (n × 20h)|
|---|---|



##### Function 

Provides additional controls for the UC. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2259 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2260-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>UCEXTPRE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 UCPR Reserved<br>UCRELDEL_INT<br>W ECLK<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-20|Reserved|
|—||
|19-16|Extended Prescaler|
|UCEXTPRE|Specifies the clock divider for the internal UC prescaler. Write the desired divider value minus 1. For<br>example, for a divider of 1, write 0.<br>The two least-significant bits of UCEXTPRE mirrorCn[UCPRE]. Any write operation to<br>UCEXTPRE also affects UCPRE.<br>~~NOTE~~|
|15|Reserved|
|—||
|14<br>UCPRECLK|Prescaler Clock Source<br>Selects the clock source for the internal prescaler.<br>0b - Prescaled clock|
||1b - eMIOS module clock|
|13-5<br>—|Reserved|
|4-0<br>UCRELDEL_IN<br>T|Reload Signal Output Delay Interval<br>Specifies the delay interval, in counter bus reload events, between each assertion of AS1-BS1 reload inMC<br>andMCBmodes.<br>00000b - Every event<br>00001b - Every 2nd event|
||00010b - Every 3rd event|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2260 / 4640 

NXP Semiconductors 

Enhanced Modular IO Subsystem (eMIOS) 

Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2261-03.png)


<!-- Start of picture text -->
Field Function<br>. . .<br>11111b - Every 32nd event<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/061_Enhanced_Modular_IO_Subsystem_-eMIOS-/S32K3XXRM_数据表.pdf-2261-04.png)


<!-- Start of picture text -->
61.11 Glossary<br>BIU IP bus interface unit<br>CP Clock prescaler<br>GCP Global clock prescaler<br>IIB Internal interface bus<br>PIF Programmable input filter<br>UC Unified channel<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2261 / 4640 

