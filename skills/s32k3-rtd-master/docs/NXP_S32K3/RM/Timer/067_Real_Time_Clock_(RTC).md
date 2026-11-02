NXP Semiconductors 

# Chapter 67 Real Time Clock (RTC) 

## 67.1 Chip-specific RTC information 

### 67.1.1 RTC instances and configuration 

The chip contains one instance of RTC (Real Time Clock) timer and API (Autonomous Periodic Interrupt) timer, where both can perform 32-bit comparisons. 

The RTC is present in always ON domain, hence available in RUN mode as well as in STANDBY mode. Both RTC and API timers can generate interrupts as well as wakeup from low power modes. 

RTC supports a resolution of 1μs with high speed internal oscillator clock (1/48MHz (FIRC) * 48 (RTC counter) = 1μs) 

This chip supports seamless RTC operation across functional reset with the clock sources SIRC and SXOSC. 

   - ~~<mark>NOTE</mark>~~ 

- SXOSC is not present in K311, thus RTC will run from SIRC clock. 

API has the capability to change the Timer compare value (APIVAL) independently without stopping the timer. 

API can also be used in conjunction with the Comparator module. In STANDBY mode configuration, the API is configured to generate a START / NEXT type signal to inform the Comparator module that a 'compare' must be carried out. 

##### Table 376. RTC instances 

|Module|S32K311/S32K312/S32K322/S32K342/S32K314/S32K324/S32K344/S32K358|
|---|---|
|RTC|Yes|



## 67.4 Introduction 

The Real-Time Clock (RTC) is a free-running counter used for time keeping applications. The RTC can be configured to generate an interrupt at a pre-defined interval independent of the mode of operation (run mode or low power mode). If in a low power mode, the RTC interval is reached, the RTC first generates a wakeup and then asserts the interrupt request. The RTC also supports an API function used to generate a periodic wakeup request to exit a low-power mode or an interrupt request. 

### 67.4.1 Features 

RTC features include: 

- 32-bit counter 

- Selectable counter clock sources (IRCs and OSCs) 

   - Clock source 0 

   - Clock source 1 

   - Clock source 2 

   - Clock source 3 

- Optional 512 prescaler and optional 32 prescaler to run the 32 bit counter. 

- RTC interrupt with interrupt enable. 

- Counter runs in all modes of operation. 

- RTC counter is reset when the counter is disabled by software and by reset to RTC block. 

- Autonomous periodic interrupt support includes: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2408 / 4640 

NXP Semiconductors 

Real Time Clock (RTC) 

   - 32-bit compare value to support range of wakeup intervals/interrupts 

   - API logic has a separate enable to support changing compare value while RTC is running 

   - API interrupt with interrupt enable 

   - Operates in all modes 

   - API compare value can be modified while RTC is running 

- Optional interrupt for RTC match, API match, and RTC rollover. 

### 67.4.2 Block diagram 

The following figure shows Clock gating for RTC clocks. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Timer/067_Real_Time_Clock_-RTC-/S32K3XXRM_数据表.pdf-2409-10.png)


<!-- Start of picture text -->
(cnten & clksel== 2’b11)<br>en<br>Clock source 3<br>C.G.<br>CELL<br>(cnten & clksel== 2’b10)<br>en<br>Clock source 2<br>C.G.<br>CELL<br>(cnten & clksel== 2’b01) 0<br>0<br>Clock source 1 CELLC.G. en CELLC.G.en div 512 1 CELLC.G. div 32 1 rtc_clock 32 bit counterreset<br>en<br>div512en<br>(cnten & clksel== 2’b00) div32en<br>en<br>Clock source 0<br>C.G.<br>CELL<br>Figure 359. Clock gating for RTC clocks<br>3<br>2<br>1<br>0 CNTEN<br>CLKSEL[1:0]<br><!-- End of picture text -->

The following figure shows the block diagram of RTC. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2409 / 4640 

NXP Semiconductors 

Real Time Clock (RTC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Timer/067_Real_Time_Clock_-RTC-/S32K3XXRM_数据表.pdf-2410-02.png)


<!-- Start of picture text -->
RTCCNT<br>sync APIVAL<br>32-0<br>+<br>APIENor reset offset reg load<br>CNTEN<br>32-0<br>== API wakeup<br>sync<br>APIF<br>rtc_clock 32 bit counter API<br>32-0 APIIE interrupt<br>== RTCVAL<br>RTC wakeup<br>ROVREN sync RTC Rollover wakeup<br>sync RTCF RTC cnt_or_rlovr<br>RTCIE<br>RTC interrupt<br>ROVRF<br>RTCIE<br><!-- End of picture text -->

Figure 360. Block diagram 

### 67.4.3 Modes of operation 

#### 67.4.3.1 Functional mode 

There are two functional modes of operation for RTC: normal operation and low-power mode. In normal operation, all RTC registers can be read or written . The RTC/API and associated interrupts are optionally enabled. In low-power mode, the bus interface is disabled. The RTC/API is enabled (if enabled prior to entry into low-power mode). 

#### 67.4.3.2 Debug mode 

On entering into the debug mode, the RTC counter freezes on the last valid count if the FRZEN is set. On exit from debug mode, counter continues from the frozen value. 

## 67.5 Functional description 

### 67.5.1 RTC 

The RTC consists of a 32-bit free running counter enabled with the CNTEN bit (CNTEN, when negated, asynchronously resets the counter and synchronously enables the counter when enabled). After disabling CNTEN, RTCVAL, APIVAL,  needs to be written again for desired functionality. The value of the counter may be read via the RTC Counter register (RTCCNT) register. Note that because of clock synchronization, the RTC Counter register (RTCCNT) value may represent a previous counter value. The difference between the counter and the read value depends on the ratio of counter clock and bus clock. Maximum possible difference between the two is 6 count values. 

The clock source to the counter is selected with the CLKSEL field, which gives four options for clocking the RTC/API. The four clock sources are assumed to be on these:Clock source 0, Clock source 1, Clock source 2, and Clock source 3. The output of the clock mux can be optionally divided by a combination of 512 and 32 to give various count periods for different clock sources. Note that the CNTEN bit should be disabled when the RTC/API clock source is switched. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2410 / 4640 

NXP Semiconductors 

Real Time Clock (RTC) 

When the RTC Counter register (RTCCNT) counter value for counter bits 31-0 match the 32-bit value in the RTCVAL field, then the RTCF interrupt flag bit is set (after proper clock synchronization). If the RTCIE interrupt enable bit is set, then the RTC interrupt request is generated. RTC Compare value register (RTCVAL) register can be written only when INV_RTC bit is clear. Initially INV_RTC=0, and hence RTC Compare value register (RTCVAL) can be written once and hence INV_RTC gets set. This bit can now be cleared only by enabling the RTC counter. After the counter is enabled, RTC Compare value register (RTCVAL) can be written anytime, until RTC is disabled again. RTC Compare value register (RTCVAL) is first synchronized to the RTC clock domain, therefore, if RTC Compare value register (RTCVAL) is updated at the point where a counter match is due to happen in the next 2-3 RTC clocks because of previous RTC Compare value register (RTCVAL), the RTCF flag is set. However, if the RTC Compare value register (RTCVAL) is updated at the point where no counter match is due as per the previous RTC Compare value register (RTCVAL), the RTCF flag is set when the counter matches the new RTC Compare value register (RTCVAL). If there is a match when in the low-power mode, then the RTC first generates a wakeup request to force a wakeup to run mode,and then the RTCF flag is set. 

If RTC Compare value register (RTCVAL) is updated just after counter match, new RTC Compare value register (RTCVAL) value should not be within next 6 RTC counter values. 

A rollover wakeup and/or interrupt can be generated when the RTC transitions from a count of 0xFFFF_FFFF to 0x0000_0000. The rollover flag is enabled by setting the ROVREN bit. If RTCIE is enabled, an interrupt request is generated for an RTC counter rollover. If system is in low power mode, RTC counter rollover with this bit causes a wakeup from the low-power mode. 

Both rollover wakeup and RTC wakeup gets asynchronously de-asserted with disabling of CNTEN. 

All the flags and counter values are synchronized with the Bus clock. It is assumed that the Bus clock and RTC clock selected through CLKSEL follows the below relation: 

Bus clock >= (1.5 * RTC clock )/(div_factor) 

- if both DIV32EN and DIV512EN bits are disabled, div_factor = 1 

- if DIV32EN=1 and DIV512EN=0, div_factor = 32 

- if DIV32EN=0 and DIV512EN=1, div_factor = 512 

- if both DIV32EN and DIV512EN bits are enabled, div_factor = 512*32 = 16384 

In case, RTC wakeup's are used as a wakeup source, Bus clock should be disabled after enabling the required wakeup and ensuring sufficient time gap (few Bus clock or RTC clock cycles, whichever is slower) between Bus clock disabling and wakeup event. 

### 67.5.2 API functional description 

Setting APIEN bit enables the autonomous interrupt function. The 32-bit APIVAL field selects the time interval for triggering an interrupt and/or wakeup event. Because the RTC is a free-running counter, the APIVAL is added to the current count to calculate an offset. When the counter reaches the offset count, an interrupt and/or wakeup request is generated. Then the offset value is recalculated and again re-triggers a new request when the new value is reached. API function is enabled only when CNTEN and APIEN bits are asserted and APIVAL is non-zero. Also, APIVAL can be updated anytime. After APIVAL is updated, the first API interrupt is generated according to the previous value. From the second interrupt onwards, the API interrupt is generated with the new APIVAL. When a compare is reached, the APIF interrupt flag bit is set (after proper clock synchronization). If the APIIE interrupt enable bit is set, then the API interrupt request is generated. If there is a match while being in the low-power mode, then the API first generates a wakeup request to force a wakeup into normal operation, and then the APIF flag is set. 

When the CNTEN is de-asserted, the API function is reset , though wakeup API is not asynchronously de-asserted with CNTEN. If APIEN is disabled when counter matches the offset, APIF can be missed. 

## 67.6 Recommended programming flow 

1. Program RTCVAL register with the value greater than 4 if RTCF related functionality is required. 

2. Program APIVAL register with the value greater than 4 if API functionality is required. 

3. Program all fields (as required) of RTC Control register (RTCC) register with CNTEN=1. After setting CNTEN field, counter starts running and RTC/API functionality will be active as per the configurations. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2411 / 4640 

NXP Semiconductors 

Real Time Clock (RTC) 

4. If RTCVAL or APIVAL needs to be updated during run, check corresponding INV_RTC or INV_API bit is cleared before writing and do meet all the restrictions of the corresponding register. 

5. If CLKSEL or DIV32EN or DIV512EN needs to be updated, first update RTC Control register (RTCC) register with CNTEN=0 (when all INV_RTC or INV_API are 0) keeping other field values same. Wait for minimum 3 RTC clock cycles so that CNTEN will be synchronized to RTC clock domain. Then write the RTC Control register (RTCC) register with new configuration required with CNTEN=1. 

## 67.7 RTC register descriptions 

The RTC registers are listed in this section. 

~~<mark>NOTE</mark>~~ 

Address offset - 0x18h should not be accessed by application as corresponding feature/s are not available. Therefore, transfer error will not be generated at this offset. 

~~<mark>NOTE</mark>~~ 

XFR error will be generated when RTCSUPV is accessed in user mode, any other register is accessed in user mode when SUPV bit is set, write attempt is made for RTCCNT register and any register accessed out of address range. 

### 67.7.1 RTC memory map 

RTC base address: 4028_8000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|RTC Supervisor control register (RTCSUPV)|32|RW|8000_0000h|
|4h|RTC Control register (RTCC)|32|RW|0000_0000h|
|8h|RTC Status register (RTCS)|32|W1C|0000_0000h|
|Ch|RTC Counter register (RTCCNT)|32|RO|0000_0000h|
|10h|API Compare value register (APIVAL)|32|RW|0000_0000h|
|14h|RTC Compare value register (RTCVAL)|32|RW|0000_0000h|



### 67.7.2 RTC Supervisor control register (RTCSUPV) 

##### Offset 

|Register|Offset|
|---|---|
|RTCSUPV|0h|



##### Function 

The RTCSUPV register contains the SUPV bit that determines whether other registers are accessible in supervisor mode or user mode. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2412 / 4640 

NXP Semiconductors 

Real Time Clock (RTC) 

~~<mark>NOTE</mark>~~ 

You can access this register only in Supervisor mode, and you must write a value only to the SUPV field of the register. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Timer/067_Real_Time_Clock_-RTC-/S32K3XXRM_数据表.pdf-2413-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>SUPV<br>W<br>Reset 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|RTC Supervisor Bit.|
|SUPV|0b - All registers are accessible in both user as well as supervisor mode.|
||1b - All other registers are accessible in the supervisor mode only.|
|30-0<br>—|Reserved|



### 67.7.3 RTC Control register (RTCC) 

##### Offset 

|Register|Offset|
|---|---|
|RTCC|4h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2413 / 4640 

NXP Semiconductors 

Real Time Clock (RTC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22||21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|CNTE<br>N|RTCIE|FRZE<br>N|ROVR<br>EN|||||||0|||||||
|Reset|0|0|0|0|0|0|0|0|0|0||0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6||5|4|3|2|1|0|
|R<br>W|APIEN|APIIE|CLK|SEL|DIV51<br>2EN|DIV32<br>EN||||||0|||||TRIG_<br>EN|
|Reset|0|0|0|0|0|0|0|0|0|0||0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|Counter Enable|
|CNTEN|The CNTEN bit enables the RTC counter. Setting CNTEN bit to 0b has the effect of asynchronously resetting<br>(synchronous reset negation) all the RTC and API logic. This allows RTC configuration and clock source<br>selection to be updated without causing synchronization issues.<br>CNTEN should be disabled whenINV_RTC,INV_APIare cleared.<br>~~NOTE~~<br>0b - Counter disabled<br>1b - Counter enabled|
|30<br>RTCIE|RTC Interrupt Enable.<br>The RTCIE bit enables interrupts requests to the system if RTCF is asserted.<br>0b - RTC interrupts disabled.<br>1b - RTC interrupts enabled.|
|29<br>FRZEN|Freeze Enable Bit<br>The counter freezes on entering the debug mode on the last valid count value if the FRZEN bit is set. After<br>passing of the debug mode counter starts from the frozen value. This bit should not be changed when debug<br>mode is enabled.<br>0b - Counter does not freeze in debug mode.<br>1b - Counter freezes in debug mode.|
|28<br>ROVREN|Counter Roll Over wakeup/Interrupt Enable.<br>The ROVREN bit enables wakeup and interrupt requests when the RTC has rolled over from 0xFFFF_FFFF<br>to 0x0000_0000. The RTCIE bit must also be set in order to generate an interrupt from a counter rollover.<br>0b - RTC rollover wakeup/interrupt disabled<br>1b - RTC rollover wakeup/interrupt enabled.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2414 / 4640 

NXP Semiconductors 

Real Time Clock (RTC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|27-16<br>—|Reserved|
|15<br>APIEN|Autonomous Periodic Interrupt Enable.<br>The APIEN bit enables the autonomous periodic interrupt function. Setting this bit to 0b, asynchronously<br>disables API wakeup output of RTC as well.<br>0b - API disabled.<br>1b - API enabled.|
|14<br>APIIE|API Interrupt Enable.<br>The APIIE bit enables interrupts requests to the system ifAPIFis asserted.<br>0b - API interrupts disabled.<br>1b - API interrupts enabled.|
|13-12<br>CLKSEL|Clock select<br>The CLKSEL[1:0] bits select the clock source for the RTC. CLKSEL may only be updated when CNTEN is<br>0. The user should ensure that oscillator is enabled before selecting it as a clock source for RTC.<br>Refer the RTC clocking section in the Clocking chapter of this document.<br>~~NOTE~~<br>00b - Clock source 0<br>01b - Clock source 1<br>10b - Clock source 2<br>11b - Clock source 3|
|11<br>DIV512EN|Divide by 512 enable<br>The DIV512EN bit enables the 512 clock divider. DIV512EN may only be updated when CNTEN is 0.<br>0b - Divide by 512 is disabled.<br>1b - Divide by 512 is enabled.|
|10<br>DIV32EN|Divide by 32 enable.<br>The DIV32EN bit enables the 32 clock divider. DIV32EN may only be updated when CNTEN is 0.<br>0b - Divide by 32 is disabled<br>1b - Divide by 32 is enabled|
|9-1<br>—|Reserved|
|0<br>TRIG_EN|Trigger enable for Analog Comparator|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2415 / 4640 

NXP Semiconductors 

Real Time Clock (RTC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||This bit (TRIG_EN) when set will de-assert the wakeup_api on the next RTC clock (required for ACMP<br>when bus clock is disabled).|
||If API wakeup is asserted with TRIG_EN set, and bus clock enabled, setting of RTCS[APIF]<br>may be missed.<br>~~NOTE~~|



### 67.7.4 RTC Status register (RTCS) 

##### Offset 

|Register|Offset|
|---|---|
|RTCS|8h|



##### Function 

~~<mark>NOTE</mark>~~ 

W1C has priority over setting of the RTCF, APIF and ROVRF bits, in case both clearing and setting occurs at the same time. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Timer/067_Real_Time_Clock_-RTC-/S32K3XXRM_数据表.pdf-2416-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>INV_ INV_ Reserv<br>R 0 RTCF  0<br>RTC  API  ed<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>ROVR<br>R 0 APIF  0 0<br>F<br>W W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29|RTC Interrupt Flag|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2416 / 4640 

NXP Semiconductors 

Real Time Clock (RTC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|RTCF|The RTCF bit indicates that the RTC counter has reached the counter value matchingRTC Compare value<br>register (RTCVAL). RTCF is cleared by writing a 1 to RTCF. Writing a 0 to RTCF has no effect.<br>0b - RTC counter is not equal to RTCVAL.<br>1b - RTC counter matches RTCVAL.|
|28-19<br>—|Reserved|
|18<br>INV_RTC|Invalid RTC write<br>This bit returns value 1 after a value is written to the RTCVAL register and the synchronization process<br>is in progress. During this synchronization period, any attempt to write to the RTCVAL register again is<br>ignored. Synchronization will complete only whenCNTENis set.|
|17<br>INV_API|Invalid APIVAL write<br>This bit returns value 1 after a value is written to the APIVAL register and the synchronization process<br>is in progress. During this synchronization period, any attempt to write to the APIVAL register again is<br>ignored. Synchronization will complete only whenCNTENis set.|
|16<br>—|Reserved|
|15-14<br>—<br>13<br>APIF|Reserved<br>API Interrupt Flag.<br>The APIF bit indicates that the RTC counter has reached the counter value matching API offset value. APIF<br>is cleared by writing a 1 to APIF. Writing a 0 to APIF has no effect.<br>0b - Counter is not equal to API offset value.<br>1b - Counter matches the API offset value.|
|12-11<br>—|Reserved|
|10<br>ROVRF|Counter Roll Over Interrupt Flag.<br>The ROVRF bit indicates that the RTC has rolled over from 0xFFFF_FFFF to 0x0000_0000. ROVRF is<br>cleared by writing a 1 to ROVRF.<br>0b - RTC has not rolled over<br>1b - RTC has rolled over|
|9-0<br>—|Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2417 / 4640 

NXP Semiconductors 

Real Time Clock (RTC) 

### 67.7.5 RTC Counter register (RTCCNT) 

##### Offset 

|Register|Offset|
|---|---|
|RTCCNT|Ch|



##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Timer/067_Real_Time_Clock_-RTC-/S32K3XXRM_数据表.pdf-2418-06.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RTCCNT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RTCCNT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|RTC Counter Value|
|RTCCNT|Because of clock synchronization, the RTCCNT value may represent a previous counter value.|



### 67.7.6 API Compare value register (APIVAL) 

##### Offset 

|Register|Offset|
|---|---|
|APIVAL|10h|



##### Function 

The APIVAL offset bits are compared to the RTC counter bits and if a match occurs, an interrupt/wakeup request is asserted. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2418 / 4640 

NXP Semiconductors 

Real Time Clock (RTC) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Timer/067_Real_Time_Clock_-RTC-/S32K3XXRM_数据表.pdf-2419-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>APIVAL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>APIVAL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|API Compare Value.|
|APIVAL|APIVAL bits are added to the current count to calculate an offset. The APIVAL offset bits are compared to<br>the RTC counter bits and if a match occurs, an interrupt/wakeup request is asserted.<br>API functionality is active only when APIVAL is non zero. The first API interrupt takes two<br>more cycles because of synchronization of APIVAL to RTC clock. After that, interrupts are<br>periodic in nature and it takes APIVAL+1 cycles. The Minimum supported value of APIVAL<br>is 4. This is because of synchronization.<br>~~NOTE~~|



### 67.7.7 RTC Compare value register (RTCVAL) 

##### Offset 

|Register|Offset|
|---|---|
|RTCVAL|14h|



##### Function 

The RTCVAL bits are compared to the RTC counter bits and if a match occurs, RTCF is set. The minimum value of RTCVAL should be 4. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2419 / 4640 

NXP Semiconductors 

###### Real Time Clock (RTC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Timer/067_Real_Time_Clock_-RTC-/S32K3XXRM_数据表.pdf-2420-02.png)


<!-- Start of picture text -->
Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>RTCVAL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>RTCVAL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-0|RTC Compare Value.|
|RTCVAL|The RTCVAL bits are compared to the RTC counter bits and if a match occurs, RTCF is set.|



## 67.8 Glossary 

API Autonomous Periodic Interrupt IRCs Internal RC Oscillator OSCs Oscillator 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2420 / 4640 

