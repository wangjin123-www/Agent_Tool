NXP Semiconductors 

# Chapter 65 System Timer Module (STM) 

## 65.1 Chip-specific STM information 

### 65.1.1 STM instances and configuration 

This chip has up to three instances of STM, one for each Cortex-M7 core. The STM counter increments at the STM module clock frequency divided by a pre-scaled value. 

Table 372. STM instances 

|Instance|S32K358|S32K322/S32K342/S32K314/S32K324/<br>S32K344|S32K311/S32K312|
|---|---|---|---|
|STM_0|Yes|Yes|Yes|
|STM_1|Yes|Yes|No|
|STM_2|Yes|No|No|



Table 373. STM configuration 

|Instance|Description|Number of|Number of|
|---|---|---|---|
|||Channels|Registers (32-bit)|
|STM_0|Intended for Cortex-M7_0 core|4|14|
|STM_1|Intended for Cortex-M7_1 core|4|14|
|STM_2|Intended for Cortex-M7_2 core|4|14|



## 65.2 Overview 

STM supports commonly required system and application software timing functions. STM includes a 32-bit count-up timer and four 32-bit compare channels with a separate interrupt source for each channel. The timer is driven by the STM module clock divided by an 8-bit prescale value (1 to 256). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2378 / 4640 

NXP Semiconductors 

System Timer Module (STM) 

### 65.2.1 Block diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Timer/065_System_Timer_Module_-STM-/S32K3XXRM_数据表.pdf-2379-03.png)


<!-- Start of picture text -->
Clock<br>32-bit counter CNT[CNT]<br>CR[TEN] CMP0[CMP]<br>= CIR0[CIF]<br>CCR0[CEN]<br>CMP1[CMP]1<br>= CIR1[CIF]<br>CCR1[CEN]<br>CMP2[CMP]<br>= CIR2[CIF]<br>CCR2[CEN]<br>CMP3[CMP]<br>= CIR3[CIF]<br>CCR3[CEN]<br>Figure 354. Block diagram<br><!-- End of picture text -->

### 65.2.2 Features 

STM has the following features: 

- One 32-bit count-up timer with an 8-bit prescaler 

- Four 32-bit compare channels 

- An independent interrupt source for each channel 

- Ability to stop the timer in Debug mode 

## 65.3 Functional description 

### 65.3.1 Count-up timer 

STM has one 32-bit count-up timer that serves as the time base for four compare channels. When enabled, the counter increments at the module clock frequency divided by a prescaler value in the range from 1 to 256. When enabled in Normal mode, the timer increments continuously. The counter rolls over at FFFF_FFFFh to 0000_0000h with no restrictions at this boundary. 

### 65.3.2 Compare channels 

STM has four identical compare channels. Each channel includes a channel control register (CCRn), a channel interrupt register (CCRn), and a channel compare register (CMPn). When the channel is enabled and its channel compare value matches the timer count, STM sets the channel interrupt flag and generates an IRQ on that channel. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2379 / 4640 

NXP Semiconductors 

System Timer Module (STM) 

### 65.3.3 Behavior in different chip modes 

STM supports the chip modes of operation as follows: 

|Chip mode|STM behavior|
|---|---|
|Normal|When the timer is enabled (CR[TEN]= 1), the timer counts up continuously.|
|Debug|IfCR[FRZ]= 1, STM stops the timer. Otherwise, when the timer is enabled (CR[TEN]= 1), the timer<br>counts up continuously.|



### 65.3.4 Clocking 

This module has no clocking considerations. 

### 65.3.5 Interrupts 

STM can generate a channel interrupt. For information, see: 

- Compare channels 

- Respond to compare channel events 

- Channel Interrupt (CIR0 - CIR3) 

## 65.4 External signals 

This module has no external signals. 

## 65.5 Initialization 

This module does not require initialization. 

## 65.6 Application information 

### 65.6.1 Configure the timer 

1. Set the initial timer count (CNT[CNT]). 

2. Specify STM behavior in chip Debug mode (CNT[FRZ]). 

3. Set the counter prescaler (CR[CPS]). 

4. Start the timer (CR[TEN]). 

### 65.6.2 Configure the compare channels 

For each compare channel: 

1. Set the channel compare value (CMPn[CMP]). 

2. Enable the compare channel (CCRn[CEN]). 

### 65.6.3 Respond to compare channel events 

For each compare channel: 

1. Check the channel interrupt flag (CIRn[CIF]). 

2. If the channel interrupt flag is set, respond to the interrupt request. 

3. When the channel interrupt has been handled, clear the channel interrupt flag (CIRn[CIF]). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2380 / 4640 

NXP Semiconductors 

System Timer Module (STM) 

## 65.7 STM register descriptions 

The STM programming model allows only 32-bit (word) accesses. An attempted reference using a different size or to a reserved address generates a bus error termination. 

### 65.7.1 STM memory map 

STM_0 base address: 4027_4000h 

STM_1 base address: 4047_4000h 

STM_2 base address: 4047_8000h 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|0h|Control (CR)|32|RW|0000_0000h|
|4h|Count (CNT)|32|RW|0000_0000h|
|10h|Channel Control (CCR0)|32|RW|0000_0000h|
|14h|Channel Interrupt (CIR0)|32|W1C|0000_0000h|
|18h|Channel Compare (CMP0)|32|RW|0000_0000h|
|20h|Channel Control (CCR1)|32|RW|0000_0000h|
|24h|Channel Interrupt (CIR1)|32|W1C|0000_0000h|
|28h|Channel Compare (CMP1)|32|RW|0000_0000h|
|30h|Channel Control (CCR2)|32|RW|0000_0000h|
|34h|Channel Interrupt (CIR2)|32|W1C|0000_0000h|
|38h|Channel Compare (CMP2)|32|RW|0000_0000h|
|40h|Channel Control (CCR3)|32|RW|0000_0000h|
|44h|Channel Interrupt (CIR3)|32|W1C|0000_0000h|
|48h|Channel Compare (CMP3)|32|RW|0000_0000h|



### 65.7.2 Control (CR) 

#### Offset 

|Register|Offset|
|---|---|
|CR|0h|



#### Function 

Contains fields for the prescale value, freeze control, and timer enable. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2381 / 4640 

NXP Semiconductors 

System Timer Module (STM) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||||0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||CP|S||||||0||||FRZ|TEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-16<br>—|Reserved|
|15-8<br>CPS|Counter Prescaler<br>Selects the module clock divide value for the prescaler (1–256).<br>• 00h - Divide module clock by 1<br>• 01h - Divide module clock by 2<br>• ...<br>• FFh - Divide module clock by 256|
|7-2<br>—<br>1|Reserved<br>Freeze|
|FRZ|Stops the timer when the chip enters Debug mode.<br>When the chip enters Debug mode, it notifies STM, which in turn uses this field to determine<br>timer operation.<br>~~NOTE~~|
||0b - Timer runs in Debug mode<br>1b - Timer stops in Debug mode|
|0|Timer Enable|
|TEN|Enables the module timer.<br>0b - Disabled<br>1b - Enabled|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2382 / 4640 

NXP Semiconductors 

System Timer Module (STM) 

### 65.7.3 Count (CNT) 

#### Offset 

|Register|Offset|
|---|---|
|CNT|4h|



#### Function 

Holds the timer count value. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Timer/065_System_Timer_Module_-STM-/S32K3XXRM_数据表.pdf-2383-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>CNT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>CNT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-0|Timer Count|
|CNT|The time base for all compare channels. When enabled, the timer count increments at the rate of the<br>module clock divided by the prescale value.|



### 65.7.4 Channel Control (CCR0 - CCR3) 

#### Offset 

|Register|Offset|
|---|---|
|CCR0|10h|
|CCR1|20h|
|CCR2|30h|
|CCR3|40h|



#### Function 

Enables channel n of the timer. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2383 / 4640 

NXP Semiconductors 

System Timer Module (STM) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||0||||||||CEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-1<br>—|Reserved|
|0|Channel Enable|
|CEN|0b - Disabled|
||1b - Enabled|



### 65.7.5 Channel Interrupt (CIR0 - CIR3) 

#### Offset 

|Register|Offset|
|---|---|
|CIR0|14h|
|CIR1|24h|
|CIR2|34h|
|CIR3|44h|



#### Function 

Indicates and clears the interrupt flag for channel n of the timer. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2384 / 4640 

NXP Semiconductors 

System Timer Module (STM) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Timer/065_System_Timer_Module_-STM-/S32K3XXRM_数据表.pdf-2385-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 CIF<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-1<br>—|Reserved|
|0|Channel Interrupt Flag|
|CIF|Indicates the channel IRQ is asserted due to a match on the channel.|
||0b - Read: IRQ is not asserted. Write: No effect.|
||1b - Read: IRQ is asserted. Write: Clear the flag.|



### 65.7.6 Channel Compare (CMP0 - CMP3) 

#### Offset 

|Register|Offset|
|---|---|
|CMP0|18h|
|CMP1|28h|
|CMP2|38h|
|CMP3|48h|



#### Function 

The compare value for channel n. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2385 / 4640 

NXP Semiconductors 

##### System Timer Module (STM) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Timer/065_System_Timer_Module_-STM-/S32K3XXRM_数据表.pdf-2386-02.png)


<!-- Start of picture text -->
Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>CMP<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>CMP<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-0|Channel Compare|
|CMP|If the channel is enabled (CCRn[CEN]), when the timer count (CNT) matches this value, STM asserts the|
||channel IRQ and sets the channel interrupt flag (CIRn[CIF]).|



## 65.8 Glossary 

IRQ Interrupt request 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2386 / 4640 

