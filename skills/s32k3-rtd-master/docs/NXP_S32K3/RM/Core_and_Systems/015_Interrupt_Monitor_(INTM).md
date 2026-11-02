NXP Semiconductors 

# Chapter 15 Interrupt Monitor (INTM) 

## 15.1 Overview 

The INTM module provides a mechanism to monitor the latency of the responses on interrupt requests to ensure that the processing of these critical interrupts executes within the expected time frame, increasing the reliability of the device. 

### 15.1.1 Block diagram 

The following block diagram shows the major registers involved in monitoring the interrupt sources. INTM_IRQSEL provides selection of the source, the INTM_MM enables the monitor, INTM_ACK captures the event when the interrupt is acknowledged, INTM_LATENCY can be programmed to trigger a monitor error when a threshold value is exceeded, INTM_STATUS is available to read the monitor error over periperhal bus. Monitor error can also be detected by ITRC. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/015_Interrupt_Monitor_-INTM-/S32K3XXRM_数据表.pdf-0508-06.png)


<!-- Start of picture text -->
INTM_MM<br>INTM_IACK<br>INTM_IRQSEL<br>IPS<br>(peripheral<br>interface)<br>INTM_LATENCY INTM_TIMER<br>monitor_error<br>IPI<br>(interrupt<br>INTM_STATUS<br>interface)<br><!-- End of picture text -->

Figure 34. INTM block diagram 

### 15.1.2 Features 

INTM supports the following features: 

- Up to 4 programmable interrupt monitors 

- Programmable interrupt source per monitor 

- Programmable 24-bit maximum latency counter per monitor 

- Timer expired status bit per monitor 

- One interrupt acknowledge for all monitors 

## 15.2 Functional description 

To monitor a subset of interrupt sources: 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

508 / 4640 

NXP Semiconductors 

Interrupt Monitor (INTM) 

1. Program INTM_IRQSEL with a value corresponding to the interrupt source number to be monitored. 

   - Only defined interrupt sources can be monitored. 

2. Program the INTM_LATENCYa registers to the maximum expected latency time for each monitored interrupt source. 

3. When ready, enable INTM_MM to monitor the registers. 

4. During the interrupt service routine, write the IRQ of the ISR to the INTM_IACK register. 

5. If the exceeds INTM_LATENCYa, then an error indication is sent to the Fault Collection Control Unit (FCCU). This information can also be seen by reading the INTM_STATUSa register. 

To clear an error condition, clear the corresponding INTM_TIMERa which interrupt source exceeded the programmed latency value. When the source is not known its recommended to clear all INTM_TIMERa. 

## 15.3 INTM register descriptions 

INTM provides a way to set a maximum timer count for the interrupt latency from interrupt request to interrupt acknowledge. The purpose of this function is to provide a mechanism to monitor the latency of interrupt sources to ensure that these critical interrupts execute within the expected time frame, increasing the reliability of the device. The hardware for this function is isolated in its own hierarchy to decrease the risk of fault interference. 

An error indication is sent to the Fault Collection Control Unit (FCCU) if the interrupt processing latency exceeds the programmed threshold of the expected latency. The error indication can be read from the Monitor status register. 

### 15.3.1 INTM memory map 

INTM base address: 4027_C000h 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|0h|Monitor Mode (INTM_MM)|32|RW|0000_0000h|
|4h|Interrupt Acknowledge (INTM_IACK)|32|WO|0000_0000h|
|8h|Interrupt Request Select 0 (INTM_IRQSEL0)|32|RW|0000_0000h|
|Ch|INTM_LATENCY0 (INTM_LATENCY0)|32|RW|0000_0000h|
|10h|Timer 0 (INTM_TIMER0)|32|RW|0000_0000h|
|14h|Status 0 (INTM_STATUS0)|32|RO|0000_0000h|
|18h|Interrupt Request Select 1 (INTM_IRQSEL1)|32|RW|0000_0000h|
|1Ch|INTM_LATENCY1 (INTM_LATENCY1)|32|RW|0000_0000h|
|20h|Timer 1 (INTM_TIMER1)|32|RW|0000_0000h|
|24h|Status 1 (INTM_STATUS1)|32|RO|0000_0000h|
|28h|Interrupt Request Select 2 (INTM_IRQSEL2)|32|RW|0000_0000h|
|2Ch|INTM_LATENCY2 (INTM_LATENCY2)|32|RW|0000_0000h|
|30h|Timer 2 (INTM_TIMER2)|32|RW|0000_0000h|
|34h|Status 2 (INTM_STATUS2)|32|RO|0000_0000h|
|38h|Interrupt Request Select 3 (INTM_IRQSEL3)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

509 / 4640 

NXP Semiconductors 

Interrupt Monitor (INTM) 

#### Table continued from the previous page... 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|3Ch|INTM_LATENCY3 (INTM_LATENCY3)|32|RW|0000_0000h|
|40h|Timer 3 (INTM_TIMER3)|32|RW|0000_0000h|
|44h|Status 3 (INTM_STATUS3)|32|RO|0000_0000h|



### 15.3.2 Monitor Mode (INTM_MM) 

#### Offset 

|Register|Offset|
|---|---|
|INTM_MM|0h|



#### Function 

Monitor mode enables the cycle count timer on a monitored interrupt request for comparison to the latency register. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/015_Interrupt_Monitor_-INTM-/S32K3XXRM_数据表.pdf-0510-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>Reserved  MM<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-1|Reserved|
|—||
|0|Monitor Mode|
|MM|This field controls whether the INTM monitors the latency of an interrupt response.|
||0b - disabled|
||1b - enabled|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

510 / 4640 

NXP Semiconductors 

Interrupt Monitor (INTM) 

### 15.3.3 Interrupt Acknowledge (INTM_IACK) 

#### Offset 

|Register|Offset|
|---|---|
|INTM_IACK|4h|



#### Function 

This register is written by the interrupt service routine when it acknowledges the interrupt processing. This write operation must provide the number of the processed interrupt, which is compared with the interrupt request number in each INTM_IRQSELa register and stops the corresponding INTM_TIMERa when it found a match. 

#### Diagram 

|Bits<br>R<br>W|31|30|29|28|27|26|25|24<br>Rese|23<br>rved|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||Rese|rved|||||||IR|Q|||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-10<br>—|Reserved|
|9-0|This field is used to specify the interrupt request number to stop INTM_TIMERa.|
|IRQ||



### 15.3.4 Interrupt Request Select a (INTM_IRQSEL0 - INTM_IRQSEL3) 

#### Offset 

|Register|Offset|
|---|---|
|INTM_IRQSEL0|8h|
|INTM_IRQSEL1|18h|
|INTM_IRQSEL2|28h|
|INTM_IRQSEL3|38h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

511 / 4640 

NXP Semiconductors 

Interrupt Monitor (INTM) 

#### Function 

These registers are used to indicate which interrupt request is to be monitored or checked. The mnemonic is of the form INTM_IRQSELa, where ‘a’ is the monitor instance. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||Rese|rved||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||Rese|rved|||||||IR|Q|||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-10<br>—|Reserved|
|9-0<br>IRQ|This field helps you select the interrupt request number to monitor.|



### 15.3.5 INTM_LATENCYa (INTM_LATENCY0 - INTM_LATENCY3) 

#### Offset 

|Register|Offset|
|---|---|
|INTM_LATENCY0|Ch|
|INTM_LATENCY1|1Ch|
|INTM_LATENCY2|2Ch|
|INTM_LATENCY3|3Ch|



#### Function 

These registers are used to indicate the maximum time before an error signal is asserted for a detected interrupt request to interrupt acknowledge. The mnemonic is of the form INTM_LATENCYa, where ‘a’ is the monitor instance. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

512 / 4640 

NXP Semiconductors 

Interrupt Monitor (INTM) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/015_Interrupt_Monitor_-INTM-/S32K3XXRM_数据表.pdf-0513-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved  LAT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>LAT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-24|Reserved|
|—||
|23-0<br>LAT|This field helps you select the maximum number of INTM clock cycles allowed for the monitored<br>interrupt request.<br>Maximum programmed value should not exceed 0xFF_FFFD to allow for proper timer error capture.|



### 15.3.6 Timer a (INTM_TIMER0 - INTM_TIMER3) 

#### Offset 

|Register|Offset|
|---|---|
|INTM_TIMER0|10h|
|INTM_TIMER1|20h|
|INTM_TIMER2|30h|
|INTM_TIMER3|40h|



#### Function 

These registers are used to count the number of INTM clock cycles for a detected interrupt request to an acknowledged interrupt processing. If the INTM_LATENCYa register is non-zero, the monitor error is not asserted, and if there is a zero to one transition on the monitored interrupt request, the INTM_TIMERa register is reset to one. As long as the INTM_LATENCYa register is non-zero and the monitor error is not asserted and the timer is enabled, the timer increments. 

Following are the conditions for the timer being enabled: 

- INTM_MM=1 and there was a zero-to-one transition on the monitored interrupt source 

Following are the conditions for disabling the INTM_TIMERa: 

- Reset 

- INTM_MM=1 and monitor error 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

513 / 4640 

NXP Semiconductors 

Interrupt Monitor (INTM) 

- INTM_MM=1 and monitored interrupt request is not asserted 

- Interrupt acknowledge for corresponding interrupt request 

- Once the timer is enabled, setting INTM_MM=0 will not disable it 

The mnemonic is of the form INTM_TIMERa, where ‘a’ is the monitor instance. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||Rese|rved|||||||TIM|ER||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||TIM|ER||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-24<br>—|Reserved|
|23-0|This field is used to count the number of INTM clock cycles up to 24 bits of resolution.|
|TIMER||



### 15.3.7 Status a (INTM_STATUS0 - INTM_STATUS3) 

#### Offset 

|Register|Offset|
|---|---|
|INTM_STATUS0|14h|
|INTM_STATUS1|24h|
|INTM_STATUS2|34h|
|INTM_STATUS3|44h|



#### Function 

These registers define the monitor status. They indicate whether the INTM_TIMERa value has exceeded the INTM_LATENCYa value. The monitor status can be cleared by clearing the corresponding INTM_TIMERa register. The mnemonic is of the form INTM_STATUSa, where ‘a’ is the monitor instance. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

514 / 4640 

NXP Semiconductors 

Interrupt Monitor (INTM) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/015_Interrupt_Monitor_-INTM-/S32K3XXRM_数据表.pdf-0515-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>STATU<br>R<br>S<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-1|Reserved|
|—||
|0|Monitor status|
|STATUS|This field indicates whether INTM_TIMER value has exceeded the INTM_LATENCY value.|
||0b - INTM_TIMER value has not exceeded the INTM_LATENCY value.|
||1b - INTM_TIMER value has exceeded the INTM_LATENCY value.|



## 15.4 Glossary 

INTM_TIMERa Timer corresponding to channel of INTM ITRC Intrusion and tamper response controller 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

515 / 4640 

