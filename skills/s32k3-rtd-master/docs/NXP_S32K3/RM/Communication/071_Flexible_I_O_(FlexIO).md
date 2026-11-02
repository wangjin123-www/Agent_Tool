NXP Semiconductors 

# Chapter 71 Flexible I/O (FlexIO) 

## 71.1 Chip-specific FlexIO information 

### 71.1.1 FlexIO instances and configuration 

The device contains one instance of FlexIO. 

FlexIO is a highly configurable module providing a wide range of functionality including: 

- Emulation of a variety of serial communication protocols like UART, I2C, SPI, SAI. It can work either as master or slave. 

- Flexible 16-bit timers with support for a variety of trigger, reset, enable and disable conditions. 

##### Table 411. FlexIO instances 

|Chip|Instance|No. of pins|No. of timers|No. of shift registers|No. of bits<br>in counter|
|---|---|---|---|---|---|
|S32K312,<br>S32K322,<br>S32K342,<br>S32K314,<br>S32K324,<br>S32K344,<br>S32K358|FlexIO|32|8|8|16|
|S32K311|FlexIO|16|8|8|16|



##### Table 412. Data rate limitation 

|FlexIO operation|Data rate limitation|
|---|---|
|Master Tx|FlexIO_clk/4|
|Slave Tx|FlexIO_clk/10|
|Master Rx|FlexIO_clk/8|
|Slave Rx|FlexIO_clk/6|



~~<mark>NOTE</mark>~~ 

FlexIO supports 32 bit accesses only. 

~~<mark>NOTE</mark>~~ 

When I2S is emulated on FlexIO, you could observe a skew between bit-clock (BCLK) and frame sync pulse amounting to 1/2 of BCLK. 

Table 413. FlexIO configuration 

|No. of pins|No. of timers|No. of shift registers|No. of bits in counter|
|---|---|---|---|
|32|8|8|16|



## 71.2 Overview 

The FlexIO is a highly configurable module providing a wide range of functionality including: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2639 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

- Emulation of a variety of serial/parallel communication protocols 

- Flexible 16-bit timers with support for a variety of trigger, reset, enable and disable conditions 

- Programmable logic blocks allowing the implementation of digital logic functions on-chip and configurable interaction of internal and external modules 

- Programmable state machine for offloading basic system control functions from CPU 

### 71.2.1 Block Diagram 

The following diagram gives a high-level overview of the configuration of FlexIO timers and shifters. 

The FlexIO uses shifters, timers and external triggers to shift data into or out of the FlexIO. The timing of the data shift is controlled by the timers, as shown in the block diagram. The timers can be configured to use generic timer functions, external triggers, or various other conditions to determine this control. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2640-09.png)


<!-- Start of picture text -->
31 SHIFTBUF0 0<br>Input Output<br>Selection Selection<br>SHIFTER0<br>31 SHIFTBUFi 0<br>FXIO_Dn FXIO_Dn<br>in out/outen<br>SHIFTERi<br>Timer<br>Selection<br>TIMER0 TIMERi<br>External Triggers<br><!-- End of picture text -->

Figure 371. FlexIO block diagram 

### 71.2.2 Features 

The FlexIO module is capable of supporting a wide range of protocols including, but not limited to: 

- UART 

- I2C 

- SPI 

- I2S 

- Camera IF 

- Motorola 68K/Intel 8080 bus 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2640 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

- PWM/Waveform generation 

- Input-capture (pulse edge interval measurement) - Example: SENT 

The following key features are provided: 

- Array of 32-bit shift registers with transmit, receive, data match, logic mode, and state modes 

- Double buffered shifter operation for continuous data transfer 

- Shifter concatenation to support large transfer sizes 

- Automatic start/stop bit generation 

- 1, 2, 4, 8, 16 or 32 multi-bit shift widths for parallel interface support 

- Interrupt, DMA or polled transmit/receive operation 

- Programmable baud rates independent of bus clock frequency 

- Highly flexible 16-bit timers with support for a variety of internal or external trigger, reset, enable and disable conditions 

- Programmable logic mode for integrating external digital logic functions on-chip or combining pin/shifter/timer functions to generate complex outputs 

- Programmable state machine for offloading basic system control functions from CPU with support for up to 8 states, 8 outputs and 3 selectable inputs per state 

- Integrated general purpose input/output registers and pin rising/falling edge interrupts to simplify software support 

## 71.3 Functional description 

### 71.3.1 Shifter operation 

Shifters are responsible for buffering and shifting data into or out of the FlexIO. The timing of shift, load and store events are controlled by the Timer assigned to the Shifter via the SHIFTCTL[TIMSEL] register. The Shifters are designed to support either DMA, interrupt or polled operation. The following block diagram provides a detailed view of the Shifter microarchitecture. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2641-19.png)


<!-- Start of picture text -->
31 SHIFTBUFi 0<br>SHIFTERi<br>out<br>SSTOP<br>SSTART<br>timer_load_data/start/stop<br>timer_store_data FXIO_D0<br>PINPOL<br>FXIO_D0 S<br>PINPOL<br>SHIFTERi<br>TIMPOL FXIO_Dn<br>INSRC<br>FXIO_Dn S SHIFTERi+1 timer_shift_pos timer_shift_neg PINWIDTH,PINSEL,<br>out PINCFG<br>PINSEL,<br>PINWIDTH S = synchronizer<br><!-- End of picture text -->

Figure 372. Shifter Microarchitecture 

##### Transmit Mode 

When configured for Transmit mode (SHIFTCTL[SMOD]=Transmit), the shifter loads data from the SHIFTBUF register and shift data out when a load event is signalled by the assigned Timer. An optional start/stop bit can also be automatically loaded before/ afterSHIFTBUFdata by configuring the SHIFTCFG[SSTART], TIMCFG[TSTART] or SHIFTCFG[SSTOP], TIMCFG[TSTOP] registers in the Shifter and Timer. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2641 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

~~<mark>NOTE</mark>~~ 

The shifter immediately loads a stop bit when the Shifter is initially configured for Transmit mode if a stop bit is enabled. 

The Shifter Status Flag (SHIFTSTAT[SSF]) and any enabled interrupts or DMA requests are set when data has been loaded from the SHIFTBUF register into the Shifter or when the Shifter is initially configured into Transmit mode. The flag clears when new data has been written into the SHIFTBUF register or a logic 1 is written to this flag. In transmit mode, any write of the SHIFTBUF register clears the corresponding Shifter Status Flag. It does not matter what is writing or the state of the DMA/interrupt enables, the flag is cleared. How the flag is set/cleared for each mode is documented in the SSF register description. 

The Shifter Error Flag (SHIFTERR[SEF]) and any enabled interrupts are set when an attempt to load data from an empty SHIFTBUF register occurs (buffer underrun). The flag can be cleared by writing it with logic 1. 

##### Receive Mode 

When configured for Receive mode (SHIFTCTL[SMOD]=Receive), the shifter shifts data in and store data into the SHIFTBUF register when a store event is signalled by the assigned Timer. Checking for a start/stop bit can be enabled before/after shifter data is sampled by configuring the SHIFTCFG[SSTART], TIMCFG[TSTART] or SHIFTCFG[SSTOP], TIMCFG[TSTOP] registers in the Shifter and Timer. 

The Shifter Status Flag (SHIFTSTAT[SSF]) and any enabled interrupts or DMA requests are set when data has been stored into the SHIFTBUF register from the Shifter. The flag clears when the data has been read from theSHIFTBUF register or a logic 1 is written to this flag. Any read of the SHIFTBUF register clears the corresponding Shifter Status Flag when Shifter is configured in Receive mode. It does not matter what is reading or the state of the DMA/interrupt enables, the flag is cleared. How the flag is set/clear for each mode is documented in the SSF register description. 

The Shifter Error Flag (SHIFTERR[SEF]) and any enabled interrupts are set when an attempt to store data into a fullSHIFTBUF register occurs (buffer overrun) or when a mismatch occurs on a start/stop bit check. The flag can be cleared by writing it with logic 1. 

##### Match Store Mode 

When configured for Match Store mode (SHIFTCTL[SMOD]=Match Store), the shifter shifts data in, check for a match result and store matched data into the SHIFTBUF register when a store event is signalled by the assigned Timer. Checking for a start/stop bit can be enabled before/after shifter data is sampled by configuring the SHIFTCFG[SSTART], TIMCFG[TSTART] or SHIFTCFG[SSTOP], TIMCFG[TSTOP] registers in the Shifter and Timer. Up to 16-bits of data can be compared using SHIFTBUF[31:16] to configure the data to be matched and SHIFTBUF[15:0] to mask the match result. 

The Shifter Status Flag (SHIFTSTAT[SSF]) and any enabled interrupts or DMA requests are set when a match occurs and matched data has been stored into the SHIFTBUF register from the Shifter. The flag clears when the matched data has been read from the SHIFTBUF register or a logic 1 is written to this flag. Any read of the SHIFTBUF register clears the corresponding Shifter Status Flag when Shifter is configured in Match Store mode. It does not matter what is reading or the state of the DMA/interrupt enables, the flag is cleared. How the flag is set/clear for each mode is documented in the SSF register description. 

The Shifter Error Flag (SHIFTERR[SEF]) and any enabled interrupts are set when an attempt to store matched data into a full SHIFTBUF register occurs (buffer overrun) or when a mismatch occurs on a start/stop bit check. The flag can be cleared by writing it with logic 1. 

##### Match Continuous Mode 

When configured for Match Continuous mode (SHIFTCTL[SMOD]=Match Continuous), the shifter shifts data in and continuously check for a match result whenever a shift event is signalled by the assigned Timer. Up to 16-bits of data can be compared using SHIFTBUF[31:16] to configure the data to be matched and SHIFTBUF[15:0] to mask the match result. 

The Shifter Status Flag (SHIFTSTAT[SSF]) and any enabled interrupts or DMA requests are set when a match occurs. The flag clears automatically as soon as there is no longer a match between Shifter data and SHIFTBUF register. The flag cannot be cleared by reading the SHIFTBUF register. 

The Shifter Error Flag (SHIFTERR[SEF]) and any enabled interrupts are set when a match occurs. The flag clears when there is a read from the SHIFTBUF register or it written with logic 1. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2642 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### State Mode 

Using State mode enables the user to implement any state machine with up to 8 states, 8 outputs and 3 selectable inputs per state. This feature allows basic control functions to be offloaded from the CPU. 

When configured for State mode (SHIFTCTL[SMOD]=State), the SHIFTBUF register is used to drive the output and compute next state values when the Shifter has been selected by the current state pointer (SHIFTSTATE[STATE]). The following diagram provides a detailed view of Shifter microarchitecture when configured for State mode. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2643-05.png)


<!-- Start of picture text -->
31 SHIFTBUFi 0<br>PINCFG,<br>{PINWIDTH,SSTART,SSTOP}<br>FXIO_D7..0<br>PINPOL<br>FXIO_D0 S SHIFTSTATE<br>STATE==i<br>nstate[2:0]<br>INSRC nstate_trigger<br>TIMSEL,<br>FXIO_Dn S SHIFTERi+1 TIMPOL<br>out<br>timer_shift_pos timer_shift_neg nstate attributes<br>PINSEL from other Shifters<br>S = synchronizer<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2643-06.png)


<!-- Start of picture text -->
Figure 373. State Microarchitecture<br><!-- End of picture text -->

When Shifter i has been selected by the current state pointer, output pins FXIO_D[7:0] are driven by SHIFTBUFi[31:24] using the configuration set by SHIFTCTLi[PINCFG]. When set, SHIFTCFGi{PWIDTH[3:0],SSTOP[1:0],SSTART[1:0]} are respectively used to disable the output drive on pins FXIO_D[7:0] for state machine applications which require less than 8 output pins. 

The next state value is computed using the 3 input pins selected by SHIFTCTLi[PINSEL] together with SHIFTBUFi[23:0]. 

~~<mark>NOTE</mark>~~ 

Each state could potentially use a different set of 3 input pins. 

The following table details how the next state value is computed when the current state pointer is pointing to Shifter i. 

Table 414. Next State computation for SHIFTSTATE[STATE]=i 

|FXIO_D[PINSEL+2]|FXIO_D[PINSEL+1]|FXIO_D[PINSEL]|Next State Value|
|---|---|---|---|
|0|0|0|SHIFTBUFi[2:0]|
|0|0|1|SHIFTBUFi[5:3]|
|0|1|0|SHIFTBUFi[8:6]|
|0|1|1|SHIFTBUFi[11:9]|
|...|...|...|...|
|1|1|1|SHIFTBUFi[23:21]|



Note that other shifters/timers could potentially be configured to drive the input pins of a given state, allowing the user to create complex combinations of shifters/timers as desired e.g. the output of a Shifter configured for logic mode could potentially be used to drive a state machine input. 

The next state transition is triggered using the Timer output selected by SHIFTCTLi[TIMSEL] with polarity controlled by SHIFTCTLi[TIMPOL]. Note that each state could potentially use a different Timer to trigger each next state transition, allowing a variety of internal/external trigger sources and clocking configurations to be used (see Timer section for more detail). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2643 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

The current state pointer defaults to Shifter 0 at reset, however it can be written by the user to select a different Shifter for the initial state. If the current state pointer selects a Shifter which is not configured for State mode, then outputs are not driven and a next state transition is never triggered. 

The Shifter Status Flag (SHIFTSTAT[SSF]) and any enabled interrupts or DMA requests are set whenever the Shifter has been selected by the current state pointer. The flag clears when the current state pointer is updated to a different Shifter. 

##### Logic Mode 

Using logic mode enables the user to implement a small amount of programmable digital logic within a FlexIO Shifter. 

When configured for Logic mode (SHIFTCTL[SMOD]=Logic), theSHIFTBUF register is used to implement a 5-input, 32-bit programmable logic look-up table. The following diagram provides a detailed view of Shifter microarchitecture when configured for Logic mode. 

The SHIFTBUFi configures the lookup table for the 4 pin inputs and the SHIFTERi can optionally be used to configure a feedback or delayed pin source as the 5th input to the look up table. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2644-08.png)


<!-- Start of picture text -->
31 SHIFTBUFi 0<br>SSTART,<br>SSTOP<br>FXIO_Dx<br>FXIO_Dx+1<br>PINCFG<br>FXIO_Dx+2<br>Logic Output FXIO_Dx+4<br>FXIO_Dx+3<br>PINPOL<br>FXIO_D0 S<br>SHIFTERi<br>TIMPOL<br>INSRC<br>FXIO_Dn S SHIFTERi+1 timer_shift_pos timer_shift_neg<br>out<br>PINSEL,<br>PINWIDTH S = synchronizer<br>MASK<br><!-- End of picture text -->

Figure 374. Logic Microarchitecture 

The look-up table is driven using 4 pin inputs (maskable using SHIFTCFG[SSTOP] and SHIFTCFG[SSTART]) plus 1 input from the internal shifter and can be configured to drive an output pin using the SHIFTCTL[PINCFG] field. Pin inputs and outputs are fixed for each logic look-up table and are not selectable. The following table lists the logic output value selected by the look-up table for Shifter 'i'. 

Table 415. Logic Look-up table for Shifter 'i' 

|SHIFTERi[0]|FXIO_D[x+3]<sup>1</sup>|FXIO_D[x+2]|FXIO_D[x+1]|FXIO_D[x]|Logic Output to<br>FXIO_D[x+4]|
|---|---|---|---|---|---|
|0|0|0|0|0|SHIFTBUFi[0]|
|0|0|0|0|1|SHIFTBUFi[1]|
|0|0|0|1|0|SHIFTBUFi[2]|
|0|0|0|1|1|SHIFTBUFi[3]|
|...|...|...|...|...|...|
|1|1|1|1|1|SHIFTBUFi[31]|



1. for Shifter i=0...3, x=i 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2644 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### for Shifter i=4...7, x=i+4 

To minimize output glitches, SHIFTCFG[SSTOP] and SHIFTCFG[SSTART] can be used to mask unused input pins. When set, {SSTOP[1:0], SSTART[1:0]} mask FXIO_D[x+3]...FXIO_D[x] inputs respectively, so that any transitions on these pins does not cause the logic output to glitch. 

Note that other shifters/timers could potentially be configured to drive the input pins of a given look-up table, allowing the user to concatenate look-up tables or create complex combinations of shifters/timers as desired. 

SHIFTCFG[PWIDTH] controls the number of delay stages introduced by the internal shifter input (SHIFTERi[0]). For example, when configured for 1-bit shift (PWIDTH=0), the internal shifter introduces a 32 Shift clock delay before passing its input (selected by SHIFTCTL[PINSEL]) to the look-up table. When configured for 32-bit shift (PWIDTH=16...31), the internal shifter introduces a 1 Shift clock delay to its input. 

The Shifter Status Flag (SHIFTSTAT[SSF]) and any enabled interrupts or DMA requests are set whenever the output pin allocated to the logic look-up table has a value of 1 (after being synchronized to the FlexIO clock). The flag clears when the output pin has a value of 0. This also allows the SSF flag to be used as a trigger to a Timer if desired. 

The Shifter Error Flag (SHIFTERR[SEF]) and any enabled interrupts are set when the output pin allocated to the logic look-up table has asserted. The flag can be cleared by writing it with logic 1. 

The logic mode input pins (including pins driven by other shifters/timers) are first synchronized to the FlexIO functional clock before they are input to the programmable logic look-up table. 

### 71.3.2 Timer Operation 

The FlexIO 16-bit timers control the loading, shifting and storing of the shift registers, the counters load the contents of the compare register and decrement down to zero on the FlexIO clock. They can perform generic timer functions such as generating a clock or select output or a PWM waveform. Timers can be configured to enable in response to a trigger, pin or shifter condition; decrement always or only on a trigger or pin edge; reset in response to a trigger or pin condition; and disable on a trigger or pin condition or on a timer compare. Timers can optionally include a start condition and/or stop condition. 

Each timer operates independently, although a timer can be configured to enable or disable at the same time as the previous timer (eg: timer1 can enable or disable at the same time as timer 0) and a timer output can be used to trigger any other timer. The trigger used by each timer is configured independently and can be configured to be a timer output, shifter status flag, pin input or an external trigger input (refer to the chip-specific FlexIO information for details on the external trigger connections). The trigger configuration is separate from the pin configuration, which can be configured for input, output data or output enable. 

The Timer Configuration Register (TIMCFGn) should be configured before setting the Timer Mode (TIMOD). 

##### Timer 8-bit Baud Counter Mode 

In 8-bit Baud Counter Mode, the 16-bit counter is divided into two 8-bit counters. The lower 8-bits are used to configure the baud rate of the shift clock and the upper 8-bits are used to configure the number of shift clock edges in the transfer. When the lower 8-bits decrement to zero, the timer output is toggled and the lower 8-bits reload from the compare register. The upper 8-bits decrement when the lower 8-bits equal zero and decrement. 

Note that a timer reset event in 8-bit Baud Counter Mode only resets the lower 8-bit counter, the upper 8-bit counter is not affected and can decrement if the timer reset is configured to update the state of the timer output, and the timer output toggles as a result of the timer reset event. 

A timer compare event occurs when the upper 8-bits equal zero and decrements. The timer status flag is set on a timer compare event. 

##### Timer 8-bit High PWM Mode 

In 8-bit High PWM Mode, the 16-bit counter is divided into two 8-bit counters. The lower 8-bits are used to configure the timer output high period and the upper 8-bits are used to configure the timer output low period. The lower 8-bits decrement when the output is high. When the lower 8-bits equal zero and decrement, the timer output is cleared and the lower 8-bits are reloaded from the compare register. The upper 8-bits decrement when the output is low. When the upper 8-bits equal zero and decrement, the timer output is set and the upper 8-bits are reloaded from the compare register. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2645 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

A timer compare event occurs when the upper 8-bits equal zero and decrements. The timer status flag is set on a timer compare event. 

##### Timer 16-bit Counter Mode 

In 16-bit Counter Mode, the 16-bit counter can be used to configure either the baud rate of the shift clock (eg: TIMDEC[1:0] != 10 or 11) or the number of shift clock edges in the transfer (eg: TIMDEC[1:0] = 10 or 11). When the 16-bit counter equals zero and decrements, the timer output toggles and the counter reloads from the compare register. 

A timer compare event occurs when the 16-bit counter equals zero and decrements. The timer status flag is set on a timer compare event. 

##### Timer 16-bit Counter Disable Mode 

In 16-bit Counter Disable Mode, the 16-bit counter can be used to configure either the baud rate of the shift clock (eg: TIMDEC[1:0] != 10 or 11) or the number of shift clock edges in the transfer (eg: TIMDEC[1:0] = 10 or 11). When the 16-bit counter equals zero and decrements, the timer output toggles and the counter reloads from the compare register. 

A timer compare event occurs when the 16-bit counter equals zero and decrements. The timer status flag is set on a timer disable event. 

##### Timer 8-bit Word Counter Mode 

In 8-bit Word Counter Mode, the 16-bit counter is divided into two 8-bit counters. The lower 8-bits are used to configure the number of shift clock edges in each word and the upper 8-bits are used to configure the number number of words in the transfer. When the lower 8-bits decrement to zero, the timer output is toggled and the lower 8-bits reload from the compare register. The upper 8-bits only decrement when the lower 8-bits equal zero and decrement. 

A timer compare event occurs when the lower 8-bits equal zero and decrements. The timer status flag is set when the upper 8-bits equal zero and decrements. 

##### Timer 8-bit Low PWM Mode 

In 8-bit Low PWM Mode, the 16-bit counter is divided into two 8-bit counters. The lower 8-bits are used to configure the timer output low period and the upper 8-bits are used to configure the timer output high period. The lower 8-bits decrement when the output is low. When the lower 8-bits equal zero and decrement, the timer output is set and the lower 8-bits are reloaded from the compare register. The upper 8-bits decrement when the output is high. When the upper 8-bits equal zero and decrement, the timer output is cleared and the upper 8-bits are reloaded from the compare register. 

A timer compare event occurs when the upper 8-bits equal zero and decrements. The timer status flag is set on a timer compare event. 

##### Timer 16-bit Input Capture Mode 

In 16-bit Input Capture Mode, the 16-bit counter uses a fixed initial value of 0xFFFF to load the counter. Whenever a timer counter disable condition is detected (as configured by TIMDIS), the timer status flag is set and the inverted timer counter value is stored in the timer compare register, then the timer counter is immediately restarted from 0xFFFF. The timer output is always output on the FlexIO trigger outputs (which can also be used by other timers as an input trigger) and can also be output to a pin (PINCFG/PINPOL/PINSEL) or a shifter. 

If the timer status flag is already set, then the input capture event is missed. When the 16-bit counter equals zero and decrements, the timer output toggles and the counter reloads with 0xFFFF. The timer output can be used to count the number of counter overflows between two input capture events. Input capture mode is not intended to be used to control shift registers, it is to enable software to count the number of bits in a variable length transfer or to monitor the period or frequency of an input. 

A timer compare event occurs when the 16-bit counter equals zero and decrements. The timer status flag is set on a timer disable event. Whenever the status flag asserts, the inverted timer counter value is stored in the timer compare register. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2646 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Timer Enable and Start Bit 

When the TIMOD is configured for the desired mode, and the condition configured by timer enable (TIMENA) is detected then the following events occur. When ONETIM is set, then the timer status flag must also be clear to generate a timer enable event, otherwise the timer enable event is blocked. This can be used to enforce software intervention after each timer iteration. 

- Timer counter loads the current value of the compare Register and start decrementing as configured by TIMDEC. 

- Timer output may update to its initial state depending on the TIMOUT configuration. Shifters that are controlled by this timer do not see this as a rising edge on the timer shift clock. 

- Transmit shifters controlled by this timer either output their start bit value, or load the shift register from the shift buffer and output the first bit, as configured by SSTART. 

If the Timer start bit is enabled, the timer counter reloads with the compare register on the first rising edge of the shift clock after the timer starts decrementing. If there is no falling edge on the shift clock before the first rising edge (for example, when TIMOUT=1), a shifter that is configured to shift on falling edge and load on the first shift does not load correctly. 

##### Timer Decrement and Reset 

The Timer then generates the timer output and timer shift clock depending on the TIMOD and TIMDEC fields. The shifter clock is either equal to the timer output (when TIMDEC != 10 or 11) or equal to the decrement clock (when TIMDEC = 10 or 11). When TIMDEC is configured to decrement from a pin or trigger, the timer decrements on both rising and falling edges. 

If a Timer is configured to decrement on the FlexIO functional clock divided by 16 or 256 (when TIMDEC = 100 or 101), then a common prescaler that is shared by all Timers is used to generate the two divide ratios. This prescaler is reset when all Timers are either idle or configured to not use the prescaler (TIMDEC != 100 or 101). 

When the Timer is configured to reset as configured in the TIMRST field then the Timer counter loads the current value of the compare register again. The timer output and timer shift clock can be configured to update on timer reset, as configured by TIMOUT. This can result in a timer shift clock edge if the timer output toggles as a result of the timer reset. In 8-bit Baud Counter mode this would also decrement the upper 8-bits of the counter. 

In general, when the timer counter decrements to zero a timer compare event is triggered. The timer compare event causes the timer counter to load the contents of the timer compare register, the timer output to toggle, any configured transmit shift registers to load, and any configured receive shift registers to store. Depending on the timer mode, the timer status flag may also be set. 

##### Timer Disable and Stop Bit 

When the is Timer is configured to add a stop bit on each compare, the following additional events occur. 

- Transmit shifters controlled by this timer output their stop bit value (if configured by SSTOP). 

- Receive shifters controlled by this timer store the contents of the shift register in their shift buffer, as configured by SSTOP. 

- On the first rising edge of the shifter clock after the compare, the timer counter reloads the current value of the Compare Register. 

Transmit shifters must be configured to load on the first shift when the timer is configured to insert a stop bit on each compare. 

When the condition configured by timer disable (TIMDIS) is detected, the following events occur. 

- Timer counter reloads the current value of the Compare Register and start decrementing as configured by TIMDEC. 

- Timer output clears. Shifters that are controlled by this timer do not see this as a falling edge on the timer shift clock, but can generate a shift event if the timer shift clock would otherwise generate one. 

- Transmit shifters controlled by this timer output their stop bit value (if configured by SSTOP). 

- Receive shifters controlled by this timer store the contents of the shift register in their shift buffer, as configured by SSTOP. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2647 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

If the timer stop bit is enabled, the timer counter continues decrementing until the next rising edge of the shift clock is detected, at which point it finishes. Although the timer output is forced low during the stop bit, the timer shift clock can toggle during the stop bit, but does not generate shift events. 

A timer enable condition can be detected in the same cycle as a timer disable condition (if timer stop bit is disabled), or on the first rising edge of the shift clock after the disable condition (if stop bit is enabled). When ONETIM is set, the timer status flag must be clear before the next timer enable condition is detected. Receive shift registers with stop bit enabled store the contents of the shift register into the shift buffer and verify the state of the input data on the configured shift edge while the timer is in the stop state condition. If there is no configured edge between the timer disable and the next rising edge of the shift clock then the final store and verify do not occur. 

### 71.3.3 Pin operation 

The pin configuration for each timer and shifter can be configured to use any FlexIO pin with either polarity. Each timer and shifter can be configured as an input, output data, output enable or bidirectional output. A pin configured for output enable can be used as an open drain (with inverted polarity, since the output enable assertion would cause logic zero to be output on the pin) or to control the enable on the bidirectional output. Any timer or shifter could be configured to control the output enable for a pin where the bidirectional output data is driven by another timer or shifter. 

##### Parallel Interface 

Shifters can be configured to use multiple FlexIO pins in parallel using the SHIFTCFG[PWIDTH] field. PWIDTH is used to configure the following settings of a shifter: 

1. Number of bits shifted per Shift clock. 

2. Number of pins driven by the shifter per Shift clock (only on shifters supporting parallel transmit i.e. SHIFTER0, SHIFTER4). 

3. Number of pins sampled by the shifter per Shift clock (only on Shifter supporting parallel receive i.e. SHIFTER3, SHIFTER7). 

When configured for parallel shift, either 4, 8, 16 or 32-bits can be shifted on every Shift clock. If an adjacent shifter is selected as the input source (SHIFTCFG[INSRC]=1), the least significant 4, 8, 16 or 32-bits from the adjacent shifter is sampled on each Shift clock. 

For shifters supporting parallel receive (SHIFTER3, SHIFTER7), the shifter can be configured to sample multiple pins (SHIFTCFG[INSRC]=0), with PWIDTH and PINSEL selecting the pins as follows: FXIO_D[PINSEL+PWIDTH]:FXIO_D[PINSEL]. Note that if PWIDTH is less than the number of bits being shifted on each Shift clock, then the most significant bits are masked with 0 e.g. if PINSEL=7 and PWIDTH=6, then SHIFTER[31:24] samples {0,0,FXIO_D[12:7]} on each Shift clock. 

For shifters supporting parallel transmit (SHIFTER0, SHIFTER4), the shifter can be configured to drive multiple pins using SHIFTCTL[PINCFG], with PWIDTH and PINSEL selecting the pins as follows: FXIO_D[PINSEL+PWIDTH]:FXIO_D[PINSEL]. Note that if PWIDTH is less than the number of bits being shifted on each Shift clock, then the most significant pins are not driven e.g. if PINSEL=7 and PWIDTH=6, then SHIFTER[5:0] drives only FXIO_D[12:7] on each Shift clock. 

##### Pin Synchronization 

When configuring a pin as an input (this includes a timer trigger configured as a pin input), the input signal is first synchronized to the FlexIO clock before the signal is used by a timer or shifter. This introduces a small latency of between 0.5 to 1.5 FlexIO clock cycles when using an external pin input to generate an output or control a shifter. This sets the maximum setup time at 1.5 FlexIO clock cycles. 

If an input is used by more than one timer or shifter then the synchronization occurs once to ensure any edge is seen on the same cycle by all timers and shifters using that input. 

Note that FlexIO pins are also connected internally, configuring a FlexIO shifter or timer to output data on an unused pin makes an internal connection that allows other shifters and timer to use this pin as an input. This allows a shifter output to be used to trigger a timer or a timer output to be shifted into a shifter. This path is also synchronized to the FlexIO clock and therefore incurs a 1 cycle latency. 

So when using a Pin input as a Timer Trigger, Timer Clock or Shifter Data Input, the following synchronization delays occur: 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2648 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

1. 0.5 to 1.5 FlexIO clock cycles for external pin 

2. 1 FlexIO clock cycle for an internally driven pin 

For timing considerations such as output valid time and input setup time for specific applications (SPI Master, SPI Slave, I2C Master, I2S Master, I2S Slave) please refer to the FlexIO Application Information Section. 

##### Pin Override 

The state of any FlexIO pin can be overriden at any time by software. The Pin Output Enable register configures any pin as an output and drives that pin with the value in the Pin Output Data Register. 

Alias registers for the Pin Output Enable/Data Registers also exist, writing a logic one to an alias register updates the corresponding register bits in both the Pin Output Enable Register and the Pin Output Data Register as follows. 

- Pin Output Disable Register clears Output Enable Register and clear Output Data Register. 

- Pin Output Clear Register sets Output Enable Register and clear Output Data Register. 

- Pin Output Set Register sets Output Enable Register and set Output Data Register. 

- Pin Output Toggle Register sets Output Enable Register and toggle Output Data Register. 

##### Pin Interrupt 

The state of any FlexIO pin can be read by software at any time. Software can also configure any pin to set a status flag when either a rising and/or falling edge is detected on that pin. The pin status flag can also be configured to generate an interrupt. 

### 71.3.4 Low Power Modes 

The FlexIO remains functional during low power modes, provided the FlexIO functional clock remains enabled. 

### 71.3.5 Debug Mode 

The FlexIO remains functional in debug mode provided the Debug Enable bit (CTRL[DBGE]) is set. 

### 71.3.6 Clocks 

##### Functional clock 

The FlexIO functional clock is asynchronous to the bus clock and can remain enabled in low power modes. The FlexIO functional clock must be enabled before accessing any FlexIO registers. Provided the FlexIO functional clock is at least equal to the bus clock, the CTRL[FASTACC] bit can be set to support fast register accesses. 

##### Bus clock 

The bus clock is only used for bus accesses to the control and configuration registers. 

### 71.3.7 Reset 

##### Chip reset 

The logic and registers for the FlexIO are reset to their default state on a chip reset. 

##### Software reset 

The FlexIO implements a software reset bit in its Control Register. The CTRL[SWRST] resets all logic and registers to their default state, except for the CTRL itself. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2649 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

### 71.3.8 Interrupts and DMA Requests 

The following table illustrates the status flags that can generate the FlexIO interrupt and DMA requests. 

Table 416. FlexIO Interrupts and DMA Requests 

|Flag|Description|Interrupt|DMA Request|Low Power Wakeup|
|---|---|---|---|---|
|SSF|Shifter Status Flag.|Y|Y|Y|
|SEF|Shifter Error Flag.|Y|N|Y|
|TSF|Timer Status Flag.|Y|Y|Y|
|PSF|Pin Status Flag.|Y|N|Y|
|ETSF|External Trigger Status<br>Flag.|Y|N|Y|



### 71.3.9 Peripheral Triggers 

The connection of the FlexIO peripheral triggers with other peripherals are device specific. 

##### Output Triggers 

Each FlexIO Timer generates an output trigger equal to the timer output. The output trigger is not affected by the timer pin polarity configuration. 

##### Input Trigger 

FlexIO supports multiple external trigger inputs that can be used to trigger one or more FlexIO timers. If a rising edge is detected on an external trigger when the FlexIO is enabled, then the external trigger status flag is set. The external triggers are synchronized to the FlexIO functional clock and must assert for at least two cycles of the FlexIO functional clock to be sampled correctly. 

## 71.4 Application Information 

This section provides examples for a variety of FlexIO module applications. 

See the register descriptions for bitfield details. 

### 71.4.1 UART Transmit 

UART transmit can be supported using one Timer, one Shifter and one Pin (two Pins if supporting CTS). The start and stop bit insertion is handled automatically and multiple transfers can be supported using DMA controller. The timer status flag can be used to indicate when the stop bit of each word is transmitted. 

Break and idle characters require software intervention, before transmitting a break or idle character the SSTART and SSTOP fields should be altered to transmit the required state and the data to transmit must equal 0xFF or 0x00. Supporting a second stop bit requires the stop bit to be inserted into the data stream using software (and increasing the number of bits to transmit). Note that when performing byte writes to SHIFTBUFn (or SHIFTBUFBIS for transmitting MSB first), the rest of the register remains unaltered allowing an address mark bit or additional stop bit to remain undisturbed. 

FlexIO does not support automatic insertion of parity bits. 

Table 417. UART Transmit Configuration 

|Register|Value|Comments|
|---|---|---|
|SHIFTCFGn|0x0000_0032|Configure start bit of 0 and stop bit of 1.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2650 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Table 417. UART Transmit Configuration (continued) 

|Register|Value|Comments|
|---|---|---|
|SHIFTCTLn|0x0003_0002|Configure transmit using Timer 0 on<br>posedge of clock with output data on<br>Pin 0. Can invert output data by setting<br>PINPOL, or can support open drain by<br>setting PINPOL=0x1 andPINCFG=0x1.|
|TIMCMPn|0x0000_0F01|Configure 8-bit transfer with baud rate<br>of divide by 4 of the FlexIO clock. Set<br>TIMCMP[15:8] = (number of bits x 2) - 1.<br>Set TIMCMP[7:0] = (baud rate divider /<br>2) - 1.|
|TIMCFGn|0x0000_2222|Configure start bit, stop bit, enable<br>on trigger asserted and disable<br>on compare. Can support CTS by<br>configuring TIMEN=0x3.|
|TIMCTLn|0x01C0_0001|Configure dual 8-bit counter using<br>Shifter 0 status flag as inverted internal<br>trigger source. Can support CTS by<br>configuring PINSEL=0x1 (for Pin 1) and<br>PINPOL=0x1.|
|SHIFTBUFn|Data to transmit|Transmit data can be written to<br>SHIFTBUF[7:0] to initiate an 8-bit<br>transfer, use the Shifter Status Flag<br>to indicate when data can be written<br>using interrupt or DMA request. Can<br>support MSB first transfer by writing to<br>SHIFTBUFBBS[7:0]register instead.|



An alternative configuration is possible that supports slower baud rates but requires two Timers. 

Table 418. UART Transmit Configuration for Slow Baud Rate 

|Register|Value|Comments|
|---|---|---|
|SHIFTCFGn|0x0000_0032|Configure start bit of 0 and stop bit of 1.|
|SHIFTCTLn|0x0003_0002|Configure transmit using Timer 0 on<br>posedge of clock with output data on<br>Pin 0. Can invert output data by setting<br>PINPOL, or can support open drain by<br>setting PINPOL=0x1 andPINCFG=0x1.|
|TIMCMPn|0x0000_000F|Configure for 8-bit transfer. Set<br>TIMCMP[15:0] = (number of bits x 2) -<br>1.|
|TIMCFGn|0x0030_2622|Configure start bit, stop bit, enable on<br>trigger rising edge, decrement on trigger<br>and disable on compare.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2651 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

Table 418. UART Transmit Configuration for Slow Baud Rate (continued) 

|Register|Value|Comments|
|---|---|---|
|TIMCTLn|0x0740_0003|Configure 16-bit counter using Timer 1<br>output as internal trigger source.|
|TIMCMP(n+1)|0x0000_0001|Configure baud rate of divide by 4 of<br>the FlexIO clock. Set TIMCMP[15:0] =<br>(baud rate divider / 2) - 1.|
|TIMCFG(n+1)|0x0000_1200|Configure enable on trigger asserted<br>and disable on Timer 0 disable.<br>Can support CTS by configuring<br>TIMEN=0x3.|
|TIMCTL(n+1)|0x01C0_0003|Configure 16-bit counter using Shifter<br>0 status flag as inverted internal<br>trigger source. Can support CTS by<br>configuringPINSEL=0x1 (for Pin 1) and<br>PINPOL=0x1.|
|SHIFTBUFn|Data to transmit|Transmit data can be written to<br>SHIFTBUF[7:0] to initiate an 8-bit<br>transfer, use the Shifter Status Flag<br>to indicate when data can be written<br>using interrupt or DMA request. Can<br>support MSB first transfer by writing to<br>SHIFTBUFBBS[7:0]register instead.|



### 71.4.2 UART Receive 

UART receive can be supported using one Timer, one Shifter and one Pin (two Timers and two Pins if supporting RTS). The start and stop bit verification is handled automatically and multiple transfers can be supported using the DMA controller. The timer status flag can be used to indicate when the stop bit of each word is received. 

Triple voting of the received data is not supported by FlexIO, data is sampled only once in the middle of each bit. Another timer can be used to implement a glitch filter on the incoming data, another Timer can also be used to detect an idle line of programmable length. Break characters cause the error flag to set and the shifter buffer register returns 0x00. 

FlexIO does not support automatic verification of parity bits. 

Table 419. UART Receiver Configuration 

|Register|Value|Comments|
|---|---|---|
|SHIFTCFGn|0x0000_0032|Configure start bit of 0 and stop bit of 1.|
|SHIFTCTLn|0x0080_0001|Configure receive using Timer 0 on<br>negedge of clock with input data on<br>Pin 0. Can invert input data by setting<br>PINPOL.|
|TIMCMPn|0x0000_0F01<br>Table continues on the next page...|Configure 8-bit transfer with baud rate<br>of divide by 4 of the FlexIO clock. Set<br>TIMCMP[15:8] = (number of bits x 2) - 1.<br>Set TIMCMP[7:0] = (baud rate divider /<br>2) - 1.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2652 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

Table 419. UART Receiver Configuration (continued) 

|Register|Value|Comments|
|---|---|---|
|TIMCFGn|0x0204_2422|Configure start bit, stop bit, enable<br>on pin posedge and disable on<br>compare. Enable resynchronization to<br>received data with TIMOUT=0x2 and<br>TIMRST=0x4.|
|TIMCTLn|0x0000_0081|Configure dual 8-bit counter using<br>inverted Pin 0 input.|
|SHIFTBUFn|Data to receive|Received data can be read from<br>SHIFTBUFBYS[7:0], use the Shifter<br>Status Flag to indicate when data<br>can be read using interrupt or DMA<br>request. Can support MSB first transfer<br>by reading fromSHIFTBUFBIS[7:0]<br>register instead.|



The UART Receiver with RTS configuration uses a 2nd Timer to generate the RTS output. The RTS asserts when the start bit is detected and negate when the data is read from the shifter buffer register. No start bit is detected while the RTS is asserted, the received data is simply ignored. 

Table 420. UART Receiver with RTS Configuration 

|Register|Value|Comments|
|---|---|---|
|SHIFTCFGn|0x0000_0032|Configure start bit of 0 and stop bit of 1.|
|SHIFTCTLn|0x0080_0001|Configure receive using Timer 0 on<br>negedge of clock with input data on<br>Pin 0. Can invert input data by setting<br>PINPOL.|
|TIMCMPn|0x0000_0F01|Configure 8-bit transfer with baud rate<br>of divide by 4 of the FlexIO clock. Set<br>TIMCMP[15:8] = (number of bits x 2) - 1.<br>Set TIMCMP[7:0] = (baud rate divider /<br>2) - 1.|
|TIMCFGn|0x0204_2522|Configure start bit, stop bit, enable<br>on pin posedge with trigger asserted<br>and disable on compare. Enable<br>resynchronization to received data with<br>TIMOUT=0x2 and TIMRST=0x4.|
|TIMCTLn|0x02C0_0081|Configure dual 8-bit counter using<br>inverted Pin 0 input. Trigger is internal<br>using inverted Pin 1 input.|
|TIMCMP(n+1)|0x0000_FFFF|Never compare.|
|TIMCFG(n+1)|0x0030_6100|Enable on Timer N enable and disable<br>on trigger falling edge. Decrement on<br>trigger to ensure no compare.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2653 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

Table 420. UART Receiver with RTS Configuration (continued) 

|Register|Value|Comments|
|---|---|---|
|TIMCTL(n+1)|0x0143_0003|Configure 16-bit counter and output on<br>Pin 1. Trigger is internal using Shifter 0<br>flag.|
|SHIFTBUFn|Data to receive|Received data can be read from<br>SHIFTBUFBYS[7:0], use the Shifter<br>Status Flag to indicate when data<br>can be read using interrupt or DMA<br>request. Can support MSB first transfer<br>by reading fromSHIFTBUFBIS[7:0]<br>register instead.|



### 71.4.3 SPI Master 

SPI master mode can be supported using two Timers, two Shifters and four Pins. Either CPHA=0 or CPHA=1 can be supported and transfers can be supported using the DMA controller. For CPHA=1, the select can remain asserted for multiple transfers and the timer status flag can be used to indicate the end of the transfer. 

The stop bit is used to guarantee a minimum of 1 clock cycle between the slave select negating and before the next transfer. Writing to the transmit buffer by either core or DMA is used to initiate each transfer. 

###### ~~<mark>NOTE</mark>~~ 

Due to synchronization delays, the setup time for the serial input data is 1.5 FlexIO clock cycles, so the maximum baud rate is divide by 4 of the FlexIO clock frequency. 

Table 421. SPI Master (CPHA=0) Configuration 

|Register|Value|Comments|
|---|---|---|
|SHIFTCFGn|0x0000_0000|Start and stop bit disabled.|
|SHIFTCTLn|0x0083_0002|Configure transmit using Timer 0 on<br>negedge of clock with output data on<br>Pin 0.|
|SHIFTCFG(n+1)|0x0000_0000|Start and stop bit disabled.|
|SHIFTCTL(n+1)|0x0000_0101|Configure receive using Timer 0 on<br>posedge of clock with input data on Pin<br>1.|
|TIMCMPn|0x0000_3F01|Configure 32-bit transfer with baud rate<br>of divide by 4 of the FlexIO clock. Set<br>TIMCMP[15:8] = (number of bits x 2) - 1.<br>Set TIMCMP[7:0] = (baud rate divider /<br>2) - 1.|
|TIMCFGn|0x0100_2222|Configure start bit, stop bit, enable on<br>trigger high and disable on compare,<br>initial clock state is logic 0.|
|TIMCTLn|0x01C3_0201|Configure dual 8-bit counter using Pin<br>2 output (shift clock), with Shifter 0 flag|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2654 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

Table 421. SPI Master (CPHA=0) Configuration (continued) 

|Register|Value|Comments|
|---|---|---|
|||as the inverted trigger. Set PINPOL to<br>invert the output shift clock.|
|TIMCMP(n+1)|0x0000_FFFF|Never compare.|
|TIMCFG(n+1)|0x0000_1100|Enable when Timer 0 is enabled and<br>disable when Timer 0 is disabled.|
|TIMCTL(n+1)|0x0003_0383|Configure 16-bit counter (never<br>compare) using inverted Pin 3 output<br>(as slave select).|
|SHIFTBUFn|Data to transmit|Transmit data can be written to<br>SHIFTBUF, use the Shifter Status Flag<br>to indicate when data can be written<br>using interrupt or DMA request. Can<br>support MSB first transfer by writing to<br>SHIFTBUFBISregister instead.|
|SHIFTBUF(n+1)|Data to receive|Received data can be read from<br>SHIFTBUF, use the Shifter Status Flag<br>to indicate when data can be read<br>using interrupt or DMA request. Can<br>support MSB first transfer by reading<br>fromSHIFTBUFBISregister instead.|



Table 422. SPI Master (CPHA=1) Configuration 

|Register|Value|Comments|
|---|---|---|
|SHIFTCFGn|0x0000_0021|Start bit loads data on first shift.|
|SHIFTCTLn|0x0003_0002|Configure transmit using Timer 0 on<br>posedge of clock with output data on<br>Pin 0.|
|SHIFTCFG(n+1)|0x0000_0000|Start and stop bit disabled.|
|SHIFTCTL(n+1)|0x0080_0101|Configure receive using Timer 0 on<br>negedge of clock with input data on Pin<br>1.|
|TIMCMPn|0x0000_3F01|Configure 32-bit transfer with baud rate<br>of divide by 4 of the FlexIO clock. Set<br>TIMCMP[15:8] = (number of bits x 2) - 1.<br>Set TIMCMP[7:0] = (baud rate divider /<br>2) - 1.|
|TIMCFGn|0x0100_2222|Configure start bit, stop bit, enable on<br>trigger high and disable on compare,<br>initial clock state is logic 0.|
|TIMCTLn|0x01C3_0201|Configure dual 8-bit counter using Pin<br>2 output (shift clock), with Shifter 0 flag<br>as the inverted trigger. Set PINPOL|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2655 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

Table 422. SPI Master (CPHA=1) Configuration (continued) 

|Register|Value|Comments|
|---|---|---|
|||to invert the output shift clock. Set<br>TIMDIS=3 to keep slave select asserted<br>for as long as there is data in the<br>transmit buffer.|
|TIMCMP(n+1)|0x0000_FFFF|Never compare.|
|TIMCFG(n+1)|0x0000_1100|Enable when Timer 0 is enabled and<br>disable when Timer 0 is disabled.|
|TIMCTL(n+1)|0x0003_0383|Configure 16-bit counter (never<br>compare) using inverted Pin 3 output<br>(as slave select).|
|SHIFTBUFn|Data to transmit|Transmit data can be written to<br>SHIFTBUF, use the Shifter Status Flag<br>to indicate when data can be written<br>using interrupt or DMA request. Can<br>support MSB first transfer by writing to<br>SHIFTBUFBISregister instead.|
|SHIFTBUF(n+1)|Data to receive|Received data can be read from<br>SHIFTBUF, use the Shifter Status Flag<br>to indicate when data can be read<br>using interrupt or DMA request. Can<br>support MSB first transfer by reading<br>fromSHIFTBUFBISregister instead.|



### 71.4.4 SPI Slave 

SPI slave mode can be supported using one Timer, two Shifters and four Pins. Either CPHA=0 or CPHA=1 can be supported and transfers can be supported using the DMA controller. For CPHA=1, the select can remain asserted for multiple transfers and the timer status flag can be used to indicate the end of the transfer. 

The transmit data must be written to the transmit buffer register before the external slave select asserts, otherwise the shifter error flag is set. 

~~<mark>NOTE</mark>~~ 

Due to synchronization delays, the output valid time for the serial output data is 2.5 FlexIO clock cycles, so the maximum baud rate is divide by 6 of the FlexIO clock frequency. 

Table 423. SPI Slave (CPHA=0) Configuration 

|Register|Value|Comments|
|---|---|---|
|SHIFTCFGn|0x0000_0000|Start and stop bit disabled.|
|SHIFTCTLn|0x0083_0002|Configure transmit using Timer 0 on<br>falling edge of shift clock with output<br>data on Pin 0.|
|SHIFTCFG(n+1)|0x0000_0000|Start and stop bit disabled.|
||Table continues on the next page...||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2656 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

Table 423. SPI Slave (CPHA=0) Configuration (continued) 

|Register|Value|Comments|
|---|---|---|
|SHIFTCTL(n+1)|0x0000_0101|Configure receive using Timer 0 on<br>rising edge of shift clock with input data<br>on Pin 1.|
|TIMCMPn|0x0000_003F|Configure 32-bit transfer. Set<br>TIMCMP[15:0] = (number of bits x 2) -<br>1.|
|TIMCFGn|0x0120_0600|Configure enable on trigger rising<br>edge, initial clock state is logic 0 and<br>decrement on pin input.|
|TIMCTLn|0x06C0_0203|Configure 16-bit counter using Pin 2<br>input (shift clock), with Pin 3 input (slave<br>select) as the inverted trigger.|
|SHIFTBUFn|Data to transmit|Transmit data can be written to<br>SHIFTBUF, use the Shifter Status Flag<br>to indicate when data can be written<br>using interrupt or DMA request. Can<br>support MSB first transfer by writing to<br>SHIFTBUFBISregister instead.|
|SHIFTBUF(n+1)|Data to receive|Received data can be read from<br>SHIFTBUF, use the Shifter Status Flag<br>to indicate when data can be read<br>using interrupt or DMA request. Can<br>support MSB first transfer by reading<br>fromSHIFTBUFBISregister instead.|



Table 424. SPI Slave (CPHA=1) Configuration 

|Register|Value|Comments|
|---|---|---|
|SHIFTCFGn|0x0000_0001|Shifter configured to load on first shift<br>and stop bit disabled.|
|SHIFTCTLn|0x0003_0002|Configure transmit using Timer 0 on<br>rising edge of shift clock with output<br>data on Pin 0.|
|SHIFTCFG(n+1)|0x0000_0000|Start and stop bit disabled.|
|SHIFTCTL(n+1)|0x0080_0101|Configure receive using Timer 0 on<br>falling edge of shift clock with input data<br>on Pin 1.|
|TIMCMPn|0x0000_003F|Configure 32-bit transfer. Set<br>TIMCMP[15:0] = (number of bits x 2) -<br>1.|
|TIMCFGn|0x0120_6602|Configure start bit, enable on trigger<br>rising edge, disable on trigger falling<br>edge, initial clock state is logic 0 and<br>decrement on pin input.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2657 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

Table 424. SPI Slave (CPHA=1) Configuration (continued) 

|Register|Value|Comments|
|---|---|---|
|TIMCTLn|0x06C0_0203|Configure 16-bit counter using Pin 2<br>input (shift clock), with Pin 3 input (slave<br>select) as the inverted trigger.|
|SHIFTBUFn|Data to transmit|Transmit data can be written to<br>SHIFTBUF, use the Shifter Status Flag<br>to indicate when data can be written<br>using interrupt or DMA request. Can<br>support MSB first transfer by writing to<br>SHIFTBUFBISregister instead.|
|SHIFTBUF(n+1)|Data to receive|Received data can be read from<br>SHIFTBUF, use the Shifter Status Flag<br>to indicate when data can be read<br>using interrupt or DMA request. Can<br>support MSB first transfer by reading<br>fromSHIFTBUFBISregister instead.|



### 71.4.5 I2C Master 

I2C master mode can be supported using two Timers, two Shifters and two Pins. One timer is used to generate the SCL output and one timer is used to control the shifters. The two shifters are used to transmit and receive for every word, when receiving the transmitter must transmit 0xFF to tristate the output. FlexIO inserts a stop bit after every word to generate/verify the ACK/NACK. FlexIO waits for the first write to the transmit data buffer before enabling SCL generation. Data transfers can be supported using the DMA controller and the shifter error flag sets on transmit underrun or receive overflow. 

The first timer generates the bit clock for the entire packet (START to Repeated START/STOP), so the compare register needs to be programmed with the total number of clock edges in the packet (minus one). The timer supports clock stretching using the reset counter when pin equal to output (although this increases both the clock high and clock low periods by at least 1 FlexIO clock cycle each). The second timer uses the SCL input pin to control the transmit/receive shift registers, this enforces an SDA data hold time by an extra 2 FlexIO clock cycles. 

Both the transmit and receive shifters need to be serviced for each word in the transfer, the transmit shifter must transmit 0xFF when receiving and the receive shifter returns the data actually present on the SDA pin. The transmit shifter loads 1 additional word on the last falling edge of SCL pin, this word should be 0x00 if generating a STOP condition or 0xFF if generating a repeated START condition. During the last word of a master-receiver transfer, the transmit SSTOP bit should be set by software to generate a NACK. 

The receive shift register asserts an error interrupt if a NACK is detected, but software is responsible for generating the STOP or repeated START condition. If a NACK is detected during master-transmit, the interrupt routine should immediately write the transmit shifter register with 0x00 (if generating STOP) or 0xFF (if generating repeated START). Software should then wait for the next rising edge on SCL and then disable both timers. The transmit shifter should then be disabled after waiting the setup delay for a repeated START or STOP condition. 

~~<mark>NOTE</mark>~~ 

Due to synchronization delays, the data valid time for the transmit output is 2 FlexIO clock cycles, so the maximum baud rate is divide by 6 of the FlexIO clock frequency. 

The I2C master data valid is delayed 2 cycles because the clock output is passed through a synchronizer before clocking the transmit/receive shifter (to guarantee some SDA hold time). Since the SCL output is synchronous with FlexIO clock, the synchronization delay is 1 cycle and then 1 cycle to generate the output. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2658 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Table 425. I2C Master Configuration 

|Register|Value|Comments|
|---|---|---|
|SHIFTCFGn|0x0000_0032|Start bit enabled (logic 0) and stop bit<br>enabled (logic 1).|
|SHIFTCTLn|0x0101_0082|Configure transmit using Timer 1 on<br>rising edge of clock with inverted output<br>enable (open drain output) on Pin 0.|
|SHIFTCFG(n+1)|0x0000_0020|Start bit disabled and stop bit enabled<br>(logic 0) for ACK/NACK detection.|
|SHIFTCTL(n+1)|0x0180_0001|Configure receive using Timer 1 on<br>falling edge of clock with input data on<br>Pin 0.|
|TIMCMPn|0x0000_2501|Configure 2 word transfer with baud rate<br>of divide by 4 of the FlexIO clock. Set<br>TIMCMP[15:8] = (number of words x<br>18) + 1. Set TIMCMP[7:0] = (baud rate<br>divider / 2) - 1.|
|TIMCFGn|0x0102_2222|Configure start bit, stop bit, enable on<br>trigger high, disable on compare, reset<br>if output equals pin. Initial clock state is<br>logic 0 and is not affected by reset.|
|TIMCTLn|0x01C1_0101|Configure dual 8-bit counter using Pin<br>1 output enable (SCL open drain), with<br>Shifter 0 flag as the inverted trigger.|
|TIMCMP(n+1)|0x0000_000F|Configure 8-bit transfer. Set<br>TIMCMP[15:0] = (number of bits x 2) -<br>1.|
|TIMCFG(n+1)|0x0020_1112|Enable when Timer 0 is enabled,<br>disable when Timer 0 is disabled,<br>enable start bit and stop bit at end of<br>each word, decrement on pin input.|
|TIMCTL(n+1)|0x01C0_0183|Configure 16-bit counter using inverted<br>Pin 1 input (SCL).|
|SHIFTBUFn|Data to transmit|Transmit data can be written to<br>SHIFTBUFBBS[7:0], use the Shifter<br>Status Flag to indicate when data<br>can be written using interrupt or DMA<br>request.|
|SHIFTBUF(n+1)|Data to receive|Received data can be read from<br>SHIFTBUFBIS[7:0], use the Shifter<br>Status Flag to indicate when data can<br>be read using interrupt or DMA request.|



### 71.4.6 I2S Master 

I2S master mode can be supported using two Timers, two Shifters and four Pins. One timer is used to generate the bit clock and control the shifters and one timer is used to generate the frame sync. FlexIO waits for the first write to the transmit data buffer 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2659 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

before enabling bit clock and frame sync generation. Data transfers can be supported using the DMA controller and the shifter error flag sets on transmit underrun or receive overflow. 

The bit clock frequency is an even integer divide of the FlexIO clock frequency, and the initial frame sync assertion occurs at the same time as the first bit clock edge. The timer uses the start bit to ensure the frame sync is generated one clock cycle before the first output data. 

###### ~~<mark>NOTE</mark>~~ 

Due to synchronization delays, the setup time for the receiver input is 1.5 FlexIO clock cycles, so the maximum baud rate is divide by 4 of the FlexIO clock frequency. 

Table 426. I2S Master Configuration 

|Register|Value|Comments|
|---|---|---|
|SHIFTCFGn|0x0000_0001|Load transmit data on first shift and stop<br>bit disabled.|
|SHIFTCTLn|0x0003_0002|Configure transmit using Timer 0 on<br>rising edge of clock with output data on<br>Pin 0.|
|SHIFTCFG(n+1)|0x0000_0000|Start and stop bit disabled.|
|SHIFTCTL(n+1)|0x0080_0101|Configure receive using Timer 0 on<br>falling edge of clock with input data on<br>Pin 1.|
|TIMCMPn|0x0000_3F01|Configure 32-bit transfer with baud rate<br>of divide by 4 of the FlexIO clock. Set<br>TIMCMP[15:8] = (number of bits x 2) - 1.<br>Set TIMCMP[7:0] = (baud rate divider /<br>2) - 1.|
|TIMCFGn|0x0000_0202|Configure start bit, enable on trigger<br>high and never disable. Initial clock<br>state is logic 1.|
|TIMCTLn|0x01C3_0281|Configure dual 8-bit counter using<br>inverted Pin 2 output (bit clock), with<br>Shifter 0 flag as the inverted trigger.<br>Clear PINPOL to invert the polarity of<br>the output shift clock.|
|TIMCMP(n+1)|0x0000_007F|Configure 32-bit transfer with baud rate<br>of divide by 4 of the FlexIO clock. Set<br>TIMCMP[15:0] = (number of bits x baud<br>rate divider) - 1.|
|TIMCFG(n+1)|0x0000_0100|Enable when Timer 0 is enabled and<br>never disable.|
|TIMCTL(n+1)|0x0003_0383|Configure 16-bit counter using inverted<br>Pin 3 output (as frame sync). Clear<br>PINPOL to invert the polarity of the<br>output frame sync|
|SHIFTBUFn|Data to transmit|Transmit data can be written to<br>SHIFTBUFBIS, use the Shifter Status|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2660 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

Table 426. I2S Master Configuration (continued) 

|Register|Value|Comments|
|---|---|---|
|||Flag to indicate when data can be<br>written using interrupt or DMA request.<br>Can support LSB first transfer by writing<br>to SHIFTBUF register instead.|
|SHIFTBUF(n+1)|Data to receive|Received data can be read from<br>SHIFTBUFBIS, use the Shifter Status<br>Flag to indicate when data can be read<br>using interrupt or DMA request. Can<br>support LSB first transfer by reading<br>from SHIFTBUF register instead.|



### 71.4.7 I2S Slave 

I2S slave mode can be supported using three Timers, two Shifters and four Pins (for single transmit and single receive, other combinations of transmit and receive are possible). 

The transmit data must be written to the transmit buffer register before the external frame sync asserts, otherwise the shifter error flag is set. 

~~<mark>NOTE</mark>~~ 

Due to synchronization delays, the output valid time for the serial output data is 2.5 FlexIO clock cycles, so the maximum baud rate is divide by 6 of the FlexIO clock frequency. 

The output valid time of I2S slave is max 2.5 cycles because there is a maximum 1.5 cycle delay on the clock synchronization plus 1 cycle to output the data 

Timer 2 detects the falling edge of frame sync (start of new frame) and asserts output until rising edge of bit clock (when frame sync is normally sampled). Timer 0 detects rising edge of bit clock with Timer 2 output asserted and asserts output for length of frame. Timer 1 detects falling edge of bit clock with Timer 0 output asserted and controls shift registers for 32-bit transfers. 

##### Table 427. I2S Slave Configuration 

|Register|Value|Comments|
|---|---|---|
|SHIFTCFGn|0x0000_0000|Start and stop bit disabled.|
|SHIFTCTLn|0x0103_0002|Configure transmit using Timer 1 on<br>rising edge of shift clock with output<br>data on Pin 0.|
|SHIFTCFG(n+1)|0x0000_0000|Start and stop bit disabled.|
|SHIFTCTL(n+1)|0x0180_0101|Configure receive using Timer 1 on<br>falling edge of shift clock with input data<br>on Pin 1.|
|TIMCMPn|0x0000_007F|Configure two 32-bit transfers per<br>frame. Set TIMCMP[15:0] = (number of<br>bits x 4) - 1.|
|TIMCFGn|0x0020_2500|Configure enable on pin rising edge<br>(inverted bit clock) with trigger high<br>(Timer 2) and disable on compare, initial|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2661 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Table 427. I2S Slave Configuration (continued) 

|Register|Value|Comments|
|---|---|---|
|||clock state is logic 1 and decrement on<br>pin input (bit clock).|
|TIMCTLn|0x0B40_0203|Configure 16-bit counter using Pin 2<br>input (bit clock), with Timer 2 output as<br>the trigger.|
|TIMCMP(n+1)|0x0000_003F|Configure 32-bit transfers. Set<br>TIMCMP[15:0] = (number of bits x 2) -<br>1.|
|TIMCFG(n+1)|0x0020_2500|Configure enable on pin (bit clock) rising<br>edge with trigger (Timer 0) high and<br>disable on compare, initial clock state is<br>logic 1 and decrement on pin input (bit<br>clock).|
|TIMCTL(n+1)|0x0340_0283|Configure 16-bit counter using inverted<br>Pin 2 input (bit clock), with Timer 0<br>output as the trigger.|
|TIMCMP(n+2)|0x0000_0000|Compare on zero (first edge).|
|TIMCFG(n+2)|0x0020_6400|Configure enable on inverted pin (frame<br>sync) rising edge and disable on trigger<br>falling edge (bit clock), initial clock state<br>is logic 1 and decrement on inverted pin<br>input (frame sync).|
|TIMCTL(n+2)|0x04C0_0383|Configure 16-bit counter using inverted<br>Pin 3 input (frame sync), with Pin 2<br>inverted input (bit clock) as the trigger.|
|SHIFTBUFn|Data to transmit|Transmit data can be written to<br>SHIFTBUFBIS, use the Shifter Status<br>Flag to indicate when data can be<br>written using interrupt or DMA request.<br>Can support LSB first transfer by writing<br>to SHIFTBUF register instead.|
|SHIFTBUF(n+1)|Data to receive|Received data can be read from<br>SHIFTBUFBIS, use the Shifter Status<br>Flag to indicate when data can be read<br>using interrupt or DMA request. Can<br>support LSB first transfer by reading<br>from SHIFTBUF register instead.|



### 71.4.8 SENT Receiver 

SENT receiver can be supported by using one Timer and one Pin. The Timer is configured as Input-Capture mode, and captures the conter value at falling edge of the Pin input. Once the counter value is captured, the counter is automatically restarted from counter value 0. Therefore, the captured value is always indicating the period between previous falling edge and current falling edge. CPU interrupt or DMA trigger can be configured at each capture of the counter, and the entire SENT frame decoding with the latest tick width adustment is performed by CPU software. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2662 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

Table 428. SENT Receiver Configuration 

|Register|Value|Comments|
|---|---|---|
|TIMCMPn|-|Counter value at the falling edge of the<br>Pin is stored in this register.|
|TIMCFGn|0x0000_6000|Timer always enabled, Timer disabled<br>on Trigger falling edge, Decrement<br>counter on FlexIO clock.|
|TIMCTLn|0xnn40_0007|Single 16-bit input capture mode, Timer<br>pin input and output are selected by<br>PINSEL, Timer pin output disabled,<br>Internal trigger selected, Select Pin nn<br>as Trigger.|



### 71.4.9 Camera Interface 

Camera Interface can be supported using one Timer, one or more Shifters and multiple Pins. Multiple transfers can be supported using DMA controller. 

The example below describes FlexIO configuration for interfacing to an 8-bit CMOS sensor with PCLK, VSYNC, HREF and D[7:0] outputs. The example uses a 128-bit buffer to capture 16-pixels of image data before interrupt or DMA transfer, however a bigger or smaller buffer may be used depending on system DMA performance and FlexIO resource usage by other applications. Note that additional timers may be used to track number of pixels per row and number of rows per frame or HREF/VSYNC may be assigned as GPIO interrupts for software tracking. 

Table 429. Camera Interface Configuration for 8-bit CMOS sensor 

|Register|Value|Comments|
|---|---|---|
|SHIFTCFGn...n+2<sup>1</sup>|0x0007_0100|Configure 8-bit parallel shift in from<br>adjacent shifter.|
|SHIFTCFGn+3|0x0007_0000|Configure 8-bit parallel shift in from pins<br>FXIO_D[7:0] (D[7:0]).|
|SHIFTCTLn...n+3|0x0080_0001|Configure receive using Timer 0 on<br>negedge of clock.|
|TIMCMPn|0x0000_001F|Configure 16-pixel (8 bits/pixel x<br>16 pixels = 128-bits) transfer. Set<br>TIMCMP[15:0] = (number of pixels x 2) -<br>1.|
|TIMCFGn|0x0120_6600|Configure enable on trigger (HREF)<br>rising edge and disable on trigger falling<br>edge, initial Shift clock state is logic 0<br>and decrement on PCLK input.|
|TIMCTLn|0x12C0_0803|Configure 16-bit counter using<br>FXIO_D[8] input (PCLK), with<br>FXIO_D[9] input (HREF) as the inverted<br>trigger.|
|SHIFTBUFn...n+3|Data to receive|Received data can be read from<br>SHIFTBUFn...n+3, use the Shifter<br>Status Flag to indicate when data can<br>be read using interrupt or DMA request.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2663 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### 1. n=0 or 4 

### 71.4.10 Motorola 68K/Intel 8080 Bus Interface 

The Motorola 68K and Intel 8080 bus are two parallel interfaces commonly used by Smart/Asynchronous LCD controllers. In conjunction with GPIO, FlexIO is able to drive these interfaces using one Timer and one Shifter, although additional Shifters could be used to support large transfers via the DMA controller. 

The configuration below provides an example of how to drive a 16-bit 68K or 8080 bus. For a 8080 bus, two GPIO are used to drive the nCS and RS pins. For a 68K bus, an additional GPIO is required to drive the RDWR pin. 

Table 430. Motorola 68K/Intel 8080 Write Configuration 

|Register|Value|Comments|
|---|---|---|
|SHIFTCFG0...7|0x000F_0100|Configure 16-bit parallel shift in from<br>adjacent shifter.|
|SHIFTCTL0|0x0003_0002|Configure transmit using Timer 0 on<br>posedge of clock with data output to<br>FXIO_D[15:0].|
|SHIFTCTL1...7|0x0000_0002|Configure transmit using Timer 0 on<br>posedge of clock.|
|TIMCMP0|0x0000_0101 (1-beat)<br>0x0000_1F01 (16-beats)|Configure 1 or 16-beat transfer with<br>baud rate of divide by 4 of the FlexIO<br>clock. Set TIMCMP[15:8] = (number of<br>beats x 2) - 1. Set TIMCMP[7:0] = (baud<br>rate divider / 2) - 1.|
|TIMCFG0|0x0000_2200|Configure enable on trigger high and<br>disable on compare. Timer output high<br>on enable.|
|TIMCTL0|0x01C3_1001 (Motorola 68K, 1-beat)<br>0x1DC3_1001 (Motorola 68K, 16-beats)<br>0x01C3_1081 (Intel 8080, 1-beat)<br>0x1DC3_1081 (Intel 8080, 16-beats)|Configure dual 8-bit counter using<br>FXIO_D[16] output (EN pin for 68K,<br>nWR pin for 8080), with Shifter 0 (1-<br>beat) or Shifter 7 (16-beats) flag as the<br>inverted trigger.|
|SHIFTBUF0...7|Data to transmit|Transmit data can be written to<br>SHIFTBUF0 (1-beat) or SHIFTBUF0...7<br>(16-beats) to initiate a transfer, use the<br>Shifter Status Flag to indicate when<br>data can be written using interrupt or<br>DMA request.|



Table 431. Motorola 68K/Intel 8080 Read Configuration 

|Register|Value|Comments|
|---|---|---|
|SHIFTCFG0...6|0x000F_0100|Configure 16-bit parallel shift in from<br>adjacent shifter.|
|SHIFTCFG7|0x000F_0000|Configure 16-bit parallel shift in from<br>pin.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2664 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

Table 431. Motorola 68K/Intel 8080 Read Configuration (continued) 

|Register|Value|Comments|
|---|---|---|
|SHIFTCTL0...7|0x0080_0001|Configure receive using Timer 0 on<br>negedge of clock with data input from<br>FXIO_D[15:0].|
|TIMCMP0|0x0000_0101 (1-beat)<br>0x0000_1F01 (16-beats)|Configure 1 or 16-beat transfer with<br>baud rate of divide by 4 of the FlexIO<br>clock. Set TIMCMP[15:8] = (number of<br>beats x 2) - 1. Set TIMCMP[7:0] = (baud<br>rate divider / 2) - 1.|
|TIMCFG0|0x0000_2220|Configure stop_bit, enable on trigger<br>high and disable on compare. Timer<br>output high on enable.|
|TIMCTL0|0x1DC3_1001 (Motorola 68K, 1 beat)<br>0x01C3_1001 (Motorola 68K, 16 beats)<br>0x1DC3_1181 (Intel 8080, 1 beat)<br>0x01C3_1181 (Intel 8080, 16 beats)|Configure dual 8-bit counter using either<br>FXIO_D[16] output (EN pin for 68K) or<br>FXIO_D[17] output (nRD pin for 8080),<br>with Shifter 7 flag (1-beat) or Shifter 0<br>flag (16-beats) as the inverted trigger.|
|SHIFTBUF0...7|Data received|Received data can be read from<br>SHIFTBUF0 (1-beat) or SHIFTBUF0...7<br>(16-beats), use the Shifter Status Flag<br>to indicate when data can be read using<br>interrupt or DMA request.|



In general, any operation to a 68K/8080 bus slave begins with a register write cycle followed by one or more data read or write cycles. To accomplish this, the following program flow should be used: 

1. Configure FlexIO with 1-beat write configuration 

2. Configure GPIO to assert nCS, RS pins (and deassert RDWR pin for 68K) 

3. Write register index data to SHIFTBUF0[15:0] 

4. Configure GPIO to deassert RS pin (and assert RDWR pin for 68K data read) 

5. Configure FlexIO with desired read or write configuration (e.g. 1 or 16-beats) 

6. Use the Shifter Status Flag to trigger interrupt or DMA driven data transfers to/from SHIFTBUF registers 

7. Configure GPIO to deassert nCS pin 

### 71.4.11 Low Power State Machine 

The configuration below details a hypothetical state machine example to illustrate the flexibility allowed when using Shifter state mode. 

In this example, FlexIO waits for the FXIO_D[2] pin to assert and then drives a complementary square wave output at a frequency of FLEXIO_CLK/131072 on the FXIO_D[1:0] pins while the comparator output is asserted (This assumes comparator is connected to external trigger 15. See the chip-specific FlexIO information for actual FlexIO trigger mappings). The state diagram below shows the states and transitions implemented by this example. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2665 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2666-02.png)


<!-- Start of picture text -->
STATE0<br>FXIO_D[2]=0<br>FXIO_D[1:0]=00<br>FXIO_D[2]=0 FXIO_D[2]=1<br>STATE1<br>CMP=0<br>FXIO_D[1:0]=01<br>CMP=1<br>STATE2<br>FXIO_D[1:0]=10<br>Figure 375. State Diagram<br><!-- End of picture text -->

##### Table 432. State Machine Configuration 

|Register|Value|Comments|
|---|---|---|
|SHIFTCFG0...2|0x0000_0003|Enable FXIO_D[1:0] as outputs.|
|SHIFTCTL0|0x0080_0206|Configure for State mode using<br>FXIO_D[4:2] as inputs to select next<br>state and Timer0 output low to trigger<br>next state.|
|SHIFTBUF0|0x0020_8208|State0: Drive FXIO_D[1:0]=00, transition<br>to State0 if FXIO_D[2]=0, State1 if<br>FXIO_D[2]=1.|
|SHIFTCTL1|0x0000_0206|Configure for State mode using<br>FXIO_D[4:2] as inputs to select next<br>state and Timer0 output high to trigger<br>next state.|
|SHIFTBUF1|0x0140_8408|State1: Drive FXIO_D[1:0]=01, transition<br>to State0 if FXIO_D[2]=0, State1<br>if CMP=0, State2 if CMP=1<br>(FXIO_D[3]=1)|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2666 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

Table 432. State Machine Configuration (continued) 

|Register|Value|Comments|
|---|---|---|
|SHIFTCTL2|0x0080_0206|Configure for State mode using<br>FXIO_D[4:2] as inputs to select next<br>state and Timer0 output low to trigger<br>next state.|
|SHIFTBUF2|0x0224_9249|State2: Drive FXIO_D[1:0]=10, transition<br>to State1 when Timer0 output low|
|TIMCMP0|0x0000_FFFF|Configure baud rate of divide by 131072<br>of the FlexIO clock. Set TIMCMP[7:0] =<br>(baud rate divider / 2) - 1.|
|TIMCFG0|0x0000_0000|Configure timer always enabled.|
|TIMCTL0|0x0000_0003|Configure single 16-bit counter.|
|TIMCFG1|0x0010_7600|Configure timer enabled on trigger rising<br>edge, disabled on trigger falling edge,<br>decrement on trigger edge.|
|TIMCTL1|0x0F03_0303|Configure timer output enabled<br>on FXIO_D[3], external trigger 15<br>(comparator output) selected.|



### 71.4.12 Keypad Interface 

The Keypad Interface can support a 3x4 keypad matrix using 3 timers and 3 shifters, although a larger matrix could be supported using additional shifters. The configuration is designed for 4 columns which are configured as active low open drain pins, and 3 rows which are configured as input pins with pullup resistors enabled. 

One shifter is configured in logic mode and is configured to assert its output when any of the row inputs are low, indicating a key is pressed. A timer is used to filter the shifter output to ensure the key is pressed for a minimum amount of time before performing the column scan. 

Another shifter is configured for parallel transmit, this shifter is used to scan each column when a key press is detected. Whenever not scanning, the shifter output is configured to assert all active low open drain column outputs to detect any keypress. A dedicated timer is used to control the transmit shifter. 

The last shifter is configured for parallel receive, this shifter is used to capture the result of the column scanning for software to decode which key or keys was pressed. This configuration captures the state of both row and colum pins for each scan, although the row state could also be deduced by the shift order. A dedicated timer is used to control the receive shifter, it shifts at half the frequency of the transmit shifter. 

Once the result of the key scan is available in the receive shifter register, FlexIO continues to monitor the row inputs and can trigger multiple scans from the one key press. To support deboucing, software can decide how many consecutive scans should be considered a single key press. 

Since the pins used in logic mode are fixed per shifter, and the shifters that support parallel shifts are limited, this configuration is restricted in what pins and shifters it can use. Increasing the matrix beyond 4 row inputs requires multiple shifters in logic mode and increasing beyond 4 column outputs requires concatenating transmit shifters to create a larger shift register. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2667 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Table 433. Keypad Interface Configuration 

|Register|Value|Comments|
|---|---|---|
|SHIFTCFG0|0x0003_0032|Start bit enabled (logic 0) and stop bit<br>enabled (logic 1), configired for 4-bit<br>shift.|
|SHIFTCTL0|0x0101_0402|Configure transmit using Timer 1 on<br>rising edge of clock generating open<br>drain output on Pins [7:4] (column<br>outputs).|
|SHIFTBUF0|0x0804_0201|Static data containing the column scan<br>pattern, each column is scanned one-<br>hot with deadtime inbetween.|
|SHIFTCFG1|0x0000_0020|In logic mode, mask input 3.|
|SHIFTCTL1|0x0000_0007|Configure logic mode.|
|SHIFTBUF1|0x07ff_07ff|Static data configuring logic mode LUT.<br>Output asserts if pins [3:1] are logic 0.|
|SHIFTCFG3|0x0007_0000|Configured for 8-bit shift.|
|SHIFTCTL3|0x0280_0001|Configure receive using Timer 2 on<br>falling edge of clock with input data on<br>Pins [7:0] (both rows and columns, pin 0<br>is don't care).|
|TIMCMP0|0x0000_00ff|Configures pre-scanning glitch filter to<br>256 FlexIO clock cycles. For different<br>filter cycles, set TIMCMP[15:0] = (filter<br>cycles) - 1.|
|TIMCFG0|0x0103_6600|Configure enable on trigger rising edge<br>and disable on trigger falling edge. Initial<br>clock state is logic 0 and is not affected<br>by reset.|
|TIMCTL0|0x0540_0003|Configure 16-bit counter using Shifter 1<br>flag (logic state) as trigger.|
|TIMCMP1|0x0000_0f3f|Configure 8 shifts (twice for each<br>column) at column scan rate of divide<br>by 128. For different scan frequency, set<br>TIMCMP[7:0] = (scan divider / 2) - 1.|
|TIMCFG1|0x0020_2622|Enable on trigger rising edge, disable<br>on compare, start and stop bits are<br>enabled.|
|TIMCTL1|0x0340_0001|Configure dual 8-bit counter using Timer<br>0 output as the trigger.|
|TIMCMP2|0x0000_0801|Configure 4 shifts at half the frequency<br>of Timer 1 trigger.|
|TIMCFG2|0x0110_2100|Enable on Timer 1 enable, disable on<br>compare, decrement on trigger input|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2668 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

Table 433. Keypad Interface Configuration (continued) 

|Register|Value|Comments|
|---|---|---|
|||with output initially negated and not<br>affected by reset|
|TIMCTL2|0x0740_0001|Configure dual 8-bit counter using Timer<br>1 output as the trigger.|
|SHIFTBUF3|Keypad Scan Result|Keypad scan result can be read from<br>SHIFTBUF3, each byte is the result of<br>one scan with both row and column pin<br>state from the scan (note that pin 0 is<br>not used). Use the Shifter Status Flag to<br>indicate when data can be written using<br>interrupt or DMA request.|



## 71.5 FlexIO Signal Descriptions 

Table 434. 

|Signal|Description|I/O|
|---|---|---|
|FXIO_Dn (n=0...31)|Bidirectional FlexIO Shifter and Timer<br>pin inputs/outputs|I/O|



## 71.6 Memory Map and Registers 

### 71.6.1 FLEXIO register descriptions 

~~<mark>NOTE</mark>~~ 

An invalid register access results in a bus error. This includes reading a write-only register, writing a read-only register or accessing an invalid address. 

#### 71.6.1.1 FLEXIO memory map 

FlexIO base address: 4032_4000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|Version ID Register (VERID)|32|RO|0201_0003h|
|4h|Parameter Register (PARAM)|32|RO|0420_0808h|
|8h|FlexIO Control Register (CTRL)|32|RW|0000_0000h|
|Ch|Pin State Register (PIN)|32|RO|0000_0000h|
|10h|Shifter Status Register (SHIFTSTAT)|32|W1C|0000_0000h|
|14h|Shifter Error Register (SHIFTERR)|32|W1C|0000_0000h|
|18h|Timer Status Register (TIMSTAT)|32|W1C|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2669 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|20h|Shifter Status Interrupt Enable (SHIFTSIEN)|32|RW|0000_0000h|
|24h|Shifter Error Interrupt Enable (SHIFTEIEN)|32|RW|0000_0000h|
|28h|Timer Interrupt Enable Register (TIMIEN)|32|RW|0000_0000h|
|30h|Shifter Status DMA Enable (SHIFTSDEN)|32|RW|0000_0000h|
|38h|Timer Status DMA Enable (TIMERSDEN)|32|RW|0000_0000h|
|40h|Shifter State Register (SHIFTSTATE)|32|RW|0000_0000h|
|48h|Trigger Status Register (TRGSTAT)|32|W1C|0000_0000h|
|4Ch|External Trigger Interrupt Enable Register (TRIGIEN)|32|RW|0000_0000h|
|50h|Pin Status Register (PINSTAT)|32|W1C|0000_0000h|
|54h|Pin Interrupt Enable Register (PINIEN)|32|RW|0000_0000h|
|58h|Pin Rising Edge Enable Register (PINREN)|32|RW|0000_0000h|
|5Ch|Pin Falling Edge Enable Register (PINFEN)|32|RW|0000_0000h|
|60h|Pin Output Data Register (PINOUTD)|32|RW|0000_0000h|
|64h|Pin Output Enable Register (PINOUTE)|32|RW|0000_0000h|
|68h|Pin Output Disable Register (PINOUTDIS)|32|WORZ|0000_0000h|
|6Ch|Pin Output Clear Register (PINOUTCLR)|32|WORZ|0000_0000h|
|70h|Pin Output Set Register (PINOUTSET)|32|WORZ|0000_0000h|
|74h|Pin Output Toggle Register (PINOUTTOG)|32|WORZ|0000_0000h|
|80h - 9Ch|Shifter Control N Register (SHIFTCTL0 - SHIFTCTL7)|32|RW|0000_0000h|
|100h - 11Ch|Shifter Configuration N Register (SHIFTCFG0 - SHIFTCFG7)|32|RW|0000_0000h|
|200h - 21Ch|Shifter Buffer N Register (SHIFTBUF0 - SHIFTBUF7)|32|RW|0000_0000h|
|280h - 29Ch|Shifter Buffer N Bit Swapped Register (SHIFTBUFBIS0 -<br>SHIFTBUFBIS7)|32|RW|0000_0000h|
|300h - 31Ch|Shifter Buffer N Byte Swapped Register (SHIFTBUFBYS0 -<br>SHIFTBUFBYS7)|32|RW|0000_0000h|
|380h - 39Ch|Shifter Buffer N Bit Byte Swapped Register (SHIFTBUFBBS0 -<br>SHIFTBUFBBS7)|32|RW|0000_0000h|
|400h - 41Ch|Timer Control N Register (TIMCTL0 - TIMCTL7)|32|RW|0000_0000h|
|480h - 49Ch|Timer Configuration N Register (TIMCFG0 - TIMCFG7)|32|RW|0000_0000h|
|500h - 51Ch|Timer Compare N Register (TIMCMP0 - TIMCMP7)|32|RW|0000_0000h|
|680h - 69Ch|Shifter Buffer N Nibble Byte Swapped Register (SHIFTBUFNBS0 -<br>SHIFTBUFNBS7)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2670 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|700h - 71Ch|Shifter Buffer N Half Word Swapped Register (SHIFTBUFHWS0 -<br>SHIFTBUFHWS7)|32|RW|0000_0000h|
|780h - 79Ch|Shifter Buffer N Nibble Swapped Register (SHIFTBUFNIS0 -<br>SHIFTBUFNIS7)|32|RW|0000_0000h|
|800h - 81Ch|Shifter Buffer N Odd Even Swapped Register (SHIFTBUFOES0 -<br>SHIFTBUFOES7)|32|RW|0000_0000h|
|880h - 89Ch|Shifter Buffer N Even Odd Swapped Register (SHIFTBUFEOS0 -<br>SHIFTBUFEOS7)|32|RW|0000_0000h|
|900h - 91Ch|Shifter Buffer N Halfword Byte Swapped Register (SHIFTBUFHBS0 -<br>SHIFTBUFHBS7)|32|RW|0000_0000h|



#### 71.6.1.2 Version ID Register (VERID) 

##### Offset 

|Register|Offset|
|---|---|
|VERID|0h|



##### Function 

Contains the version of the FlexIO. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2671-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R MAJOR  MINOR<br>W<br>Reset 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R FEATURE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-24|Major Version Number|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2671 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|MAJOR|This read only field returns the major version number for the module specification.|
|23-16|Minor Version Number|
|MINOR|This read only field returns the minor version number for the module specification.|
|15-0|Feature Specification Number|
|FEATURE|This read only field returns the feature set number.|
||0000_0000_0000_0000b - Standard features implemented.|
||0000_0000_0000_0001b - Supports state, logic and parallel modes.|
||0000_0000_0000_0010b - Supports pin control registers.|
||0000_0000_0000_0011b - Supports state, logic and parallel modes; plus pin control registers.|



#### 71.6.1.3 Parameter Register (PARAM) 

##### Offset 

|Register|Offset|
|---|---|
|PARAM|4h|



##### Function 

Contains the number of shifters, timers, pins, and triggers. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||TRIG|GER|||||||PI|N||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|1|0|0|0|0|1|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||TIM|ER|||||||SHIF|TER||||
|W|||||||||||||||||
|Reset|0|0|0|0|1|0|0|0|0|0|0|0|1|0|0|0|



Fields 

|Field|Function||
|---|---|---|
|31-24|Trigger Number||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2672 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|TRIGGER|Number of external triggers implemented.|
|23-16|Pin Number|
|PIN|Number of Pins implemented.|
|15-8|Timer Number|
|TIMER|Number of Timers implemented.|
|7-0|Shifter Number|
|SHIFTER|Number of Shifters implemented.|



#### 71.6.1.4 FlexIO Control Register (CTRL) 

##### Offset 

|Register|Offset|
|---|---|
|CTRL|8h|



##### Function 

Control register. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2673-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R 0<br>ed  DBGE<br>W 0<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 FASTA SWRS FLEXE<br>W CC  T  N<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31<br>—|Any write value to this bit must be zero.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2673 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|30<br>DBGE|Debug Enable<br>Enables FlexIO operation in Debug mode.<br>0b - FlexIO is disabled in debug modes.<br>1b - FlexIO is enabled in debug modes|
|29-3<br>—<br>2|Reserved<br>Fast Access|
|FASTACC|Enables fast register accesses to FlexIO registers, but requires the FlexIO functional clock to be at least<br>equal to the frequency of the bus clock.<br>0b - Configures for normal register accesses to FlexIO<br>1b - Configures for fast register accesses to FlexIO|
|1<br>SWRST|Software Reset<br>The FlexIO Control Register is not affected by the software reset, all other logic in the FlexIO is affected<br>by the software reset and all other register accesses are ignored until this bit is cleared. This register bit<br>remains set until cleared by software, and the reset has cleared in the FlexIO clock domain.<br>0b - Software reset is disabled<br>1b - Software reset is enabled, all FlexIO registers except the Control Register are reset.|
|0|FlexIO Enable|
|FLEXEN|Determines if the FlexIO is enabled or disabled.<br>0b - FlexIO module is disabled.<br>1b - FlexIO module is enabled.|



#### 71.6.1.5 Pin State Register (PIN) 

##### Offset 

|Register|Offset|
|---|---|
|PIN|Ch|



##### Function 

Reports status of the Pin Data Input. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2674 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2675-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R PDI<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R PDI<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Pin Data Input|
|PDI|Returns the input data on each of the FlexIO pins.|



#### 71.6.1.6 Shifter Status Register (SHIFTSTAT) 

##### Offset 

|Register|Offset|
|---|---|
|SHIFTSTAT|10h|



##### Function 

Shifter status flags. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||0|||||||SS|F||||
|W||||||||||||W1|C||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2675 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Fields 

|Field|Function|
|---|---|
|31-8|Reserved|
|—||
|7-0|Shifter Status Flag|
|SSF|The shifter status flag is updated when one of the following events occurs:<br>ForSMOD=Receive, the status flag is set when SHIFTBUF has been loaded with data from Shifter<br>(SHIFTBUF is full), and the status flag is cleared when SHIFTBUF register is read.<br>ForSMOD=Transmit, the status flag is set when SHIFTBUF data has been transferred to the Shifter<br>(SHIFTBUF is empty) or when initially configured for SMOD=Transmit, and the status flag is cleared when<br>the SHIFTBUF register is written.<br>ForSMOD=Match Store, the status flag is set when a match has occured between SHIFTBUF and Shifter,<br>and the status flag is cleared when the SHIFTBUF register is read.<br>ForSMOD=Match Continuous, returns the current match result between the SHIFTBUF and Shifter. The<br>status flag cannot be cleared by reading SHIFTBUF.<br>ForSMOD=State, the status flag for a shifter sets when it is selected by the current state pointer.<br>ForSMOD=Logic, returns the current value of the programmable logic block output.<br>The status flag can also be cleared by writing a logic one to the flag for all modes except Match Continuous/<br>State /Logic.<br>0b - Status flag is clear.<br>1b - Status flag is set.|



#### 71.6.1.7 Shifter Error Register (SHIFTERR) 

##### Offset 

|Register|Offset|
|---|---|
|SHIFTERR|14h|



##### Function 

This register reports shifter error flags. Write one to clear. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2676 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||0|||||||SE|F||||
|W||||||||||||W1|C||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-8|Reserved|
|—||
|7-0|Shifter Error Flags|
|SEF|The shifter error flag is set when one of the following events occurs:<br>ForSMOD=Receive, indicates Shifter was ready to store new data into SHIFTBUF before the previous data<br>was read from SHIFTBUF (SHIFTBUF Overrun), or indicates that the received start or stop bit does not<br>match the expected value.<br>ForSMOD=Transmit, indicates Shifter was ready to load new data from SHIFTBUF before new data had<br>been written into SHIFTBUF (SHIFTBUF Underrun).<br>ForSMOD=Match Store, indicates a match event occured before the previous match data was read from<br>SHIFTBUF (SHIFTBUF Overrun).<br>ForSMOD=Match Continuous, the error flag is set when a match has occured between SHIFTBUF<br>and Shifter.<br>ForSMOD=Logic, the error flag is set when the output of the programmable logic block has asserted.<br>Can be cleared by writing logic one to the flag. For SMOD=Match Continuous, can also be cleared when the<br>SHIFTBUF register is read.<br>0b - Shifter Error Flag is clear.|
||1b - Shifter Error Flag is set.|



#### 71.6.1.8 Timer Status Register (TIMSTAT) 

##### Offset 

|Register|Offset|
|---|---|
|TIMSTAT|18h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2677 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Function 

This register reports timer status flags. Write one to clear. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||0|||||||TS|F||||
|W||||||||||||W1|C||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-8|Reserved|
|—||
|7-0|Timer Status Flags|
|TSF|The timer status flag sets depending on the timer mode, and can be cleared by writing logic one to the flag.<br>In 8-bit baud counter mode, the timer status flag is set when the upper 8-bit counter equals zero<br>and decrements.<br>In 8-bit high PWM mode, the timer status flag is set when the upper 8-bit counter equals zero<br>and decrements.<br>In 16-bit counter mode, the timer status flag is set when the 16-bit counter equals zero and decrements.<br>In 16-bit counter disable mode, the timer status flag is set when a timer disable event is detected.<br>In 8-bit word counter mode, the timer status flag is set when the upper 8-bit counter equals zero<br>and decrements.<br>In 8-bit low PWM mode, the timer status flag is set when the upper 8-bit counter equals zero<br>and decrements.<br>In 16-bit input capture mode, the timer status flag is set when a timer disable event is detected and the timer<br>status flag is clear. In this mode, the timer compare register should only be read when the timer status flag<br>is set.|
||0b - Timer Status Flag is clear.<br>1b - Timer Status Flag is set.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2678 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

#### 71.6.1.9 Shifter Status Interrupt Enable (SHIFTSIEN) 

##### Offset 

|Register|Offset|
|---|---|
|SHIFTSIEN|20h|



##### Function 

Enables for Shifter Status Interrupts. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2679-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>SSIE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-8<br>—|Reserved|
|7-0|Shifter Status Interrupt Enable|
|SSIE|Enables interrupt generation when correspondingSSFis set.|
||0b - Shifter Status Flag interrupt disabled.<br>1b - Shifter Status Flag interrupt enabled.|



#### 71.6.1.10 Shifter Error Interrupt Enable (SHIFTEIEN) 

##### Offset 

|Register|Offset|
|---|---|
|SHIFTEIEN|24h|



Function 

Enables for Shifter Error Interrupts. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2679 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2680-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>SEIE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-8<br>—|Reserved|
|7-0|Shifter Error Interrupt Enable|
|SEIE|Enables interrupt generation when correspondingSEFis set.<br>0b - Shifter Error Flag interrupt disabled.<br>1b - Shifter Error Flag interrupt enabled.|



#### 71.6.1.11 Timer Interrupt Enable Register (TIMIEN) 

##### Offset 

|Register|Offset|
|---|---|
|TIMIEN|28h|



Function 

Enables for Timer Status Interrupts. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2680 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2681-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>TEIE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-8<br>—|Reserved|
|7-0|Timer Status Interrupt Enable|
|TEIE|Enables interrupt generation when correspondingTSFis set.|
||0b - Timer Status Flag interrupt is disabled.<br>1b - Timer Status Flag interrupt is enabled.|



#### 71.6.1.12 Shifter Status DMA Enable (SHIFTSDEN) 

##### Offset 

|Register|Offset|
|---|---|
|SHIFTSDEN|30h|



Function 

Enables for Shifter DMA requests. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2681 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2682-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>SSDE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-8<br>—|Reserved|
|7-0|Shifter Status DMA Enable|
|SSDE|Enables DMA request generation when correspondingSSFis set.|
||0b - Shifter Status Flag DMA request is disabled.|
||1b - Shifter Status Flag DMA request is enabled.|



#### 71.6.1.13 Timer Status DMA Enable (TIMERSDEN) 

##### Offset 

|Register|Offset|
|---|---|
|TIMERSDEN|38h|



##### Function 

Enables for DMA requests when Timer Status Flag is set. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2682 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||||0|||||||TS|DE||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-8|Reserved|
|—||
|7-0|Timer Status DMA Enable|
|TSDE|Enables DMA request generation when correspondingTSFis set.<br>When the Timer Status DMA request is enabled, reading or writing a Timer Compare Register clears the<br>corresponding Timer Status Register. The DMA must therefore read or write the Timer Compare Register<br>as part of the DMA transfer, otherwise the DMA request remains asserted.<br>0b - Timer Status Flag DMA request is disabled.|
||1b - Timer Status Flag DMA request is enabled.|



#### 71.6.1.14 Shifter State Register (SHIFTSTATE) 

##### Offset 

|Register|Offset|
|---|---|
|SHIFTSTATE|40h|



##### Function 

Contains the pointer to keep track of the current shifter. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2683 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||||||0||||||||STATE||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-3|Reserved|
|—||
|2-0|Current State Pointer|
|STATE|The current state field maintains a pointer to keep track of the current Shifter (configured for State mode)<br>enabled to drive outputs and compute the next state. Reading this register when the state pointer is updating<br>can result in the incorrect state returned.|
||This bitfield is writable and the value written overrides the current state.|



#### 71.6.1.15 Trigger Status Register (TRGSTAT) 

##### Offset 

|Register|Offset|
|---|---|
|TRGSTAT|48h|



##### Function 

External Trigger Status Flags. Write one to clear. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2684 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||0||||||||ETS|F||
|W||||||||||||||W1|C||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-4|Reserved|
|—||
|3-0|External Trigger Status Flags|
|ETSF|The external trigger status flag is set when a rising edge is detected on the corresponding external<br>trigger input.|
||0b - External Trigger Status Flag is clear|
||1b - External Trigger Status Flag is set|



#### 71.6.1.16 External Trigger Interrupt Enable Register (TRIGIEN) 

##### Offset 

|Register|Offset|
|---|---|
|TRIGIEN|4Ch|



Function 

Enables for external trigger interrupts. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2685 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2686-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>TRIE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-4<br>—|Reserved|
|3-0|External Trigger Interrupt Enable|
|TRIE|Enables interrupt generation when correspondingETSFis set.|
||0b - External Trigger Status Flag interrupt is disabled.|
||1b - External Trigger Status Flag interrupt is enabled.|



#### 71.6.1.17 Pin Status Register (PINSTAT) 

##### Offset 

|Register|Offset|
|---|---|
|PINSTAT|50h|



##### Function 

Pin Status Flags. Write one to clear. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2686 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2687-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R PSF<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R PSF<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Pin Status Flags|
|PSF|The pin status flag is set when a rising edge (if configured) or falling edge (if configured) is detected on the<br>corresponding pin, as configured by pin.|
||0b - Pin Status Flag is clear|
||1b - Pin Status Flag is set|



#### 71.6.1.18 Pin Interrupt Enable Register (PINIEN) 

##### Offset 

|Register|Offset|
|---|---|
|PINIEN|54h|



##### Function 

Enables for pin status interrupts. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||PS|IE||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||PS|IE||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2687 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Fields 

|Field|Function|
|---|---|
|31-0|Pin Status Interrupt Enable|
|PSIE|Enables interrupt generation when correspondingPSFis set.|
||0b - Pin Status Flag interrupt is disabled.|
||1b - Pin Status Flag interrupt is enabled.|



#### 71.6.1.19 Pin Rising Edge Enable Register (PINREN) 

##### Offset 

|Register|Offset|
|---|---|
|PINREN|58h|



##### Function 

Enables for pin status flag on rising edge. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||PR|E||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||PR|E||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-0|Pin Rising Edge|
|PRE|When set, the pin status flag is set whenever a rising edge is detected on the pin.|
||0b - Pin Status Flag does not set when a pin rising edge is detected.|
||1b - Pin Status Flag does set when a pin rising edge is detected.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2688 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

#### 71.6.1.20 Pin Falling Edge Enable Register (PINFEN) 

##### Offset 

|Register|Offset|
|---|---|
|PINFEN|5Ch|



##### Function 

Enables for pin status flag on falling edge. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2689-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>PFE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>PFE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Pin Falling Edge|
|PFE|When set, the pin status flag is set whenever a falling edge is detected on the pin.|
||0b - Pin Status Flag does not set when a pin falling edge is detected.|
||1b - Pin Status Flag does set when a pin falling edge is detected.|



#### 71.6.1.21 Pin Output Data Register (PINOUTD) 

##### Offset 

|Register|Offset|
|---|---|
|PINOUTD|60h|



##### Function 

Data Out when direct pin output in enabled. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2689 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2690-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>OUTD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>OUTD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Output Data|
|OUTD|Configures the value driven on the corresponding pin when direct pin output is enabled.|
||0b - Logic zero is driven on the pin when direct pin output is enabled.|
||1b - Logic one is driven on the pin when direct pin output is enabled.|



#### 71.6.1.22 Pin Output Enable Register (PINOUTE) 

##### Offset 

|Register|Offset|
|---|---|
|PINOUTE|64h|



##### Function 

Enables for pin output. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||OU|TE||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||OU|TE||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2690 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Fields 

|Field|Function|
|---|---|
|31-0|Output Enable|
|OUTE|Enables direct output on the corresponding pin.|
||0b - Pin is controlled by timer/shifter configuration.|
||1b - Pin is an output and driven with value ofPINOUTDregister.|



#### 71.6.1.23 Pin Output Disable Register (PINOUTDIS) 

##### Offset 

|Register|Offset|
|---|---|
|PINOUTDIS|68h|



##### Function 

##### Disable for pin output. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2691-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W OUTDIS<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W OUTDIS<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Output Disable|
|OUTDIS|Configures correponding pins to disable direct output.|
||0b - No effect.|
||1b - CorrespondingPINOUTDandPINOUTEbits are cleared.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2691 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

#### 71.6.1.24 Pin Output Clear Register (PINOUTCLR) 

##### Offset 

|Register|Offset|
|---|---|
|PINOUTCLR|6Ch|



Function Clears pin output. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2692-07.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W OUTCLR<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W OUTCLR<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Output Clear|
|OUTCLR|Configures correponding pins to output zero.|
||0b - No effect.|
||1b - CorrespondingPINOUTDis cleared andPINOUTEis set.|



#### 71.6.1.25 Pin Output Set Register (PINOUTSET) 

##### Offset 

|Register|Offset|
|---|---|
|PINOUTSET|70h|



Function sets pin output. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2692 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2693-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W OUTSET<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W OUTSET<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Output Set|
|OUTSET|Configures correponding pins to output logic one.|
||0b - No effect.|
||1b - CorrespondingPINOUTDis set andPINOUTEis set.|



#### 71.6.1.26 Pin Output Toggle Register (PINOUTTOG) 

##### Offset 

|Register|Offset|
|---|---|
|PINOUTTOG|74h|



##### Function 

Toggles pin output. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2693-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W OUTTOG<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W OUTTOG<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2693 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Fields 

|Field|Function|
|---|---|
|31-0|Output Toggle|
|OUTTOG|Configures corresponding pins to toggle.|
||0b - No effect.|
||1b - CorrespondingPINOUTDis inverted andPINOUTEis set.|



#### 71.6.1.27 Shifter Control N Register (SHIFTCTL0 - SHIFTCTL7) 

##### Offset 

For a = 0 to 7: 

|Register<br>SHIFTCTLa|Offset<br>80h + (a × 4h)|
|---|---|



##### Function 

Control for Shift Register N 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2694-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 TIMPO 0<br>TIMSEL  PINCFG<br>L<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 PINPO 0<br>PINSEL  SMOD<br>L<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved|
|—||
|26-24|Timer Select|
|TIMSEL|Selects which Timer is used for controlling the logic/shift register and generating the Shift clock.<br>TIMSEL=i selects TIMERi.|
|23|Timer Polarity|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2694 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|TIMPOL|Determines the shift occurs on the positive edge or negative edge of the shift clock.<br>0b - Shift on posedge of Shift clock<br>1b - Shift on negedge of Shift clock|
|22-18<br>—|Reserved|
|17-16<br>PINCFG|Shifter Pin Configuration<br>For pins configured as an output (PINCFG=11), this field takes effect when the register is written.<br>When initially configuring PINCFG=0x11, FlexIO may briefly drive the pin low. To avoid this,<br>software can configure PINCFG=0x10 along with the rest of the control register and then<br>perform a subsequent write to set PINCFG=0x11.<br>~~NOTE~~<br>00b - Shifter pin output disabled<br>01b - Shifter pin open drain or bidirectional output enable<br>10b - Shifter pin bidirectional output data<br>11b - Shifter pin output|
|15-13<br>—|Reserved|
|12-8<br>PINSEL|Shifter Pin Select<br>Selects which pin is used by the Shifter input or output. PINSEL=i selects the FXIO_Di pin. For pins<br>configured as an output (PINCFG=11), this field takes effect when the register is written.|
|7<br>PINPOL|Shifter Pin Polarity<br>For pins configured as an output (PINCFG=11), this field takes effect when the register is written.<br>0b - Pin is active high<br>1b - Pin is active low|
|6-3<br>—|Reserved|
|2-0<br>SMOD|Shifter Mode<br>Configures the mode of the Shifter.<br>000b - Disabled.<br>001b - Receive mode. Captures the current Shifter content into the SHIFTBUF on expiration of<br>the Timer.<br>010b - Transmit mode. Load SHIFTBUF contents into the Shifter on expiration of the Timer.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2695 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||011b - Reserved.|
||100b - Match Store mode. Shifter data is compared to SHIFTBUF content on expiration of the<br>Timer.|
||101b - Match Continuous mode. Shifter data is continuously compared to SHIFTBUF contents.|
||110b - State mode. SHIFTBUF contents are used for storing programmable state attributes.|
||111b - Logic mode. SHIFTBUF contents are used for implementing programmable logic look up<br>table.|



#### 71.6.1.28 Shifter Configuration N Register (SHIFTCFG0 - SHIFTCFG7) 

##### Offset 

For a = 0 to 7: 

|Register<br>SHIFTCFGa|Offset<br>100h + (a × 4h)|
|---|---|



##### Function 

Contains configuration bit fields for Shifter Register N. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||0||||||||PWIDTH||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R||0||SSIZE|0||LATST|INSRC|0|0|SS|OP||0|SSTART|
|W||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



##### Fields 

|Field|Function||
|---|---|---|
|31-21<br>—|Reserved||
|20-16|Parallel Width||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2696 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|PWIDTH|For all Shifters, this register field configures the number of bits to be shifted on each Shift clock as follows:<br>1-bit shift for PWIDTH=0<br>2-bit shift for PWIDTH=1<br>4-bit shift for PWIDTH=2...3<br>8-bit shift for PWIDTH=4...7<br>16-bit shift for PWIDTH=8...15<br>32-bit shift for PWIDTH=16...31<br>For Shifters which support parallel transmit (SHIFTER0, SHIFTER4, ...) or parallel receive (SHIFTER3,<br>SHIFTER7, ...), this register field, together with SHIFTCTL[PINSEL], also selects the pins to be driven or<br>sampled on each Shift clock as follows:<br>• FXIO_D[PINSEL+PWIDTH]:FXIO_D[PINSEL]<br>Shifters which do not support parallel transmit or parallel receive only support parallel shift whenINSRC=1.<br>ForSMOD=State, this field is used to disable state outputs. SeeState Mode sectionfor more detail.|
|15-13<br>—|Reserved|
|12<br>SSIZE|Shifter Size<br>Configures the size of the Shift Registers.<br>A 24-bit shift register shifts data into bits [23:0] only and does not update bits [31:24] during shift operations.<br>When shift register is configured for 24-bit, configuring PWIDTH=8..15 performs a 12-bit shift and<br>PWIDTH=16..31 performs a 24-bit shift.<br>0b - Shift register is 32-bit.<br>1b - Shift register is 24-bit.|
|11-10<br>—<br>9<br>LATST|Reserved<br>Late Store<br>Configures what happens when a receive or match shift register is configured to both shift and store on<br>the same cycle.<br>0b - Shift register stores the pre-shift register state.<br>1b - Shift register stores the post-shift register state.|
|8<br>INSRC|Input Source<br>Selects the input source for the shifter. Configuring INSRC=1 is not supported for the last shifter.<br>0b - Pin<br>1b - Shifter N+1 Output<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2697 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|7<br>—|Reserved|
|6<br>|Reserved|
|—<br>5-4<br>SSTOP|Shifter Stop bit<br>ForSMOD=Transmit, this field allows automatic stop bit insertion if the selected timer has also enabled a<br>stop bit.<br>ForSMOD=Receive or Match Store, this field allows automatic stop bit checking if the selected timer has<br>also enabled a stop bit.<br>ForSMOD=State, this field is used to disable state outputs. See 'State Mode' section for more detail.<br>ForSMOD=Logic, this field is used to mask logic pin inputs. See 'Logic Mode' section for more detail.<br>00b - Stop bit disabled for transmitter/receiver/match store<br>01b - Stop bit disabled for transmitter/receiver/match store, receiver/match store will store receive<br>data on the configured shift edge when timer in stop condition<br>10b - Transmitter outputs stop bit value 0 on store, receiver/match store sets error flag if stop bit<br>is not 0, receiver/match store will also store receive data on the configured shift edge when timer<br>in stop condition<br>11b - Transmitter outputs stop bit value 1 on store, receiver/match store sets error flag if stop bit<br>is not 1, receiver/match store will also store receive data on the configured shift edge when timer<br>in stop condition|
|3-2<br>—|Reserved|
|1-0<br>SSTART|Shifter Start bit<br>ForSMOD=Transmit, this field allows automatic start bit insertion if the selected timer has also enabled a<br>start bit.<br>ForSMOD=Receive or Match Store, this field allows automatic start bit checking if the selected timer has<br>also enabled a start bit.<br>ForSMOD=State, this field is used to disable state outputs. See 'State Mode' section for more detail.<br>ForSMOD=Logic, this field is used to mask logic pin inputs. See 'Logic Mode' section for more detail.<br>00b - Start bit disabled for transmitter/receiver/match store, transmitter loads data on enable<br>01b - Start bit disabled for transmitter/receiver/match store, transmitter loads data on first shift<br>10b - Transmitter outputs start bit value 0 before loading data on first shift, receiver/match store<br>sets error flag if start bit is not 0<br>11b - Transmitter outputs start bit value 1 before loading data on first shift, receiver/match store<br>sets error flag if start bit is not 1|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2698 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

#### 71.6.1.29 Shifter Buffer N Register (SHIFTBUF0 - SHIFTBUF7) 

##### Offset 

For a = 0 to 7: 

|Register<br>SHIFTBUFa|Offset<br>200h + (a × 4h)|
|---|---|



Function Contains Shift buffer data. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2699-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>SHIFTBUF<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>SHIFTBUF<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Shift Buffer|
|SHIFTBUF|Shift buffer data is used for a variety of functions depending on theSMODsetting:<br>For SMOD=Receive, Shifter data is transferred into SHIFTBUF at the expiration of Timer. The SHIFTBUF<br>register should only be read when the corresponding shifter status flag is set, indicating new Shifter data<br>is available.|
||For SMOD=Transmit, SHIFTBUF data is transferred into the Shifter before the Timer begins.<br>For SMOD=Match Store, SHIFTBUF[31:16] contains the data to be matched with the Shifter contents and<br>SHIFTBUF[15:0] can be used to mask the match result (1=mask, 0=no mask). The Match is checked when<br>the Timer expires and Shifter data [31:16] is written to SHIFTBUF[31:16] whenever a match event occurs.<br>The SHIFTBUF register should only be read when the corresponding shifter status flag is set, indicating new<br>Shifter data is available.<br>For SMOD=Match Continuous, SHIFTBUF[31:16] contains the data to be matched with the Shifter contents<br>and SHIFTBUF[15:0] can be used to mask the match result (1=mask, 0=no mask).<br>For SMOD=Logic, SHIFTBUF[31:0] is used to implement a 5-input, 32-bit programmable logic look-up table.<br>SeeLogic Mode sectionfor more detail.<br>For SMOD=State, SHIFTBUF[31:24] is used to drive the output value when this shifter is selected by the<br>current state pointer and SHIFTBUF[23:0] is used to configure the value of the next state transition. See<br>State Mode sectionfor more detail.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2699 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

#### 71.6.1.30 Shifter Buffer N Bit Swapped Register (SHIFTBUFBIS0 - SHIFTBUFBIS7) 

##### Offset 

For a = 0 to 7: 

|Register<br>SHIFTBUFBISa|Offset<br>280h + (a × 4h)|
|---|---|



##### Function 

SHIFTBUF register contents, but contents of this register are bit swapped. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2700-09.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>SHIFTBUFBIS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>SHIFTBUFBIS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Shift Buffer|
|SHIFTBUFBIS|Alias to SHIFTBUF register, except reads/writes to this register are bit swapped. Reads return<br>SHIFTBUF[0:31].|



#### 71.6.1.31 Shifter Buffer N Byte Swapped Register (SHIFTBUFBYS0 - SHIFTBUFBYS7) 

##### Offset 

For a = 0 to 7: 

|Register<br>SHIFTBUFBYSa|Offset<br>300h + (a × 4h)|
|---|---|



##### Function 

SHIFTBUF register contents, but contents of this register are byte swapped. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2700 / 4640 

NXP Semiconductors 

###### Flexible I/O (FlexIO) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2701-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>SHIFTBUFBYS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>SHIFTBUFBYS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Shift Buffer|
|SHIFTBUFBYS|Alias to SHIFTBUF register, except reads/writes to this register are byte swapped. Reads return<br>{ SHIFTBUF[7:0], SHIFTBUF[15:8], SHIFTBUF[23:16], SHIFTBUF[31:24] }.|



#### 71.6.1.32 Shifter Buffer N Bit Byte Swapped Register (SHIFTBUFBBS0 - SHIFTBUFBBS7) 

##### Offset 

For a = 0 to 7: 

|Register<br>SHIFTBUFBBSa|Offset<br>380h + (a × 4h)|
|---|---|



##### Function 

Contains SHIFTBUF register data, but is bit swapped within each byte. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||SHIFTB|UFBBS||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||SHIFTB|UFBBS||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2701 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Fields 

|Field|Function|
|---|---|
|31-0|Shift Buffer|
|SHIFTBUFBBS|Alias to SHIFTBUF register, except reads/writes to this register are bit swapped within each byte. Reads<br>return { SHIFTBUF[24:31], SHIFTBUF[16:23], SHIFTBUF[8:15], SHIFTBUF[0:7] }.|



#### 71.6.1.33 Timer Control N Register (TIMCTL0 - TIMCTL7) 

##### Offset 

For a = 0 to 7: 

|Register<br>TIMCTLa|Offset<br>400h + (a × 4h)|
|---|---|



##### Function 

Timer Control for Timer N. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2702-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 TRGP TRGS 0<br>TRGSEL  PINCFG<br>W OL  RC<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 PINPO PININ ONETI 0<br>PINSEL  TIMOD<br>W L  S  M<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-30|Reserved|
|—||
|29-24|Trigger Select|
|TRGSEL|The valid values for TRGSEL depends on the FLEXIO_PARAM register.|
||• When TRGSRC = 1, the valid values for N depends on PIN, TIMER, SHIFTER fields in the<br>FLEXIO_PARAM register.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2702 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Table continued from the previous page... 

|Field|Function<br>• When TRGSRC = 0, the valid values for N depends on TRIGGER field in FLEXIO_PARAM register.<br>Refer to the chip-specific FlexIO information for external trigger selection.<br>For a pin, N=0 to 31. For a Shifter, N=0 to 7. For a Timer, N=0 to 7.<br>~~NOTE~~<br>When TRGSRC = 0 the trigger selection is configured as follows:<br>• N - External trigger N input<br>When TRGSRC = 1 the internal trigger can be configured to select an input pin as follows:<br>• 2*N - Pin N input<br>When TRGSRC = 1 the internal trigger can be configured to select a shifter/timer signal as follows:<br>• 4*N+1 - Shifter N status flag<br>• 4*N+3 - Timer N trigger output<br>In other words, the expanded internal trigger selection (TRGSRC = 1) is as follows:<br>• 0000 = Pin 0<br>• 0001 = Shifter 0 Flag<br>• 0010 = Pin 1<br>• 0011 = Timer 0 Trigger<br>• 0100 = Pin 2<br>• 0101 = Shifter 1 Flag<br>• 0110 = Pin 3<br>• 0111 = Timer 1 Trigger<br>• ...<br>• This continues up to the Pin 31, Shifter 7 and Timer 7.|
|---|---|
|23<br>TRGPOL|Trigger Polarity<br>Determines if the trigger is active high or active low.<br>0b - Trigger active high<br>1b - Trigger active low|
|22<br>TRGSRC|Trigger Source<br>Determines if the trigger source is external or internal.<br>0b - External trigger selected<br>1b - Internal trigger selected|
|21-18<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2703 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|17-16<br>PINCFG|Timer Pin Configuration<br>Configures the direction of the Timer pin. For pins configured as an output (PINCFG=11), this field takes<br>effect when the register is written.<br>When initially configuring PINCFG=0x11, FlexIO may briefly drive the pin low. To avoid this,<br>software can configure PINCFG=0x10 along with the rest of the control register and then<br>perform a subsequent write to set PINCFG=0x11.<br>~~NOTE~~<br>00b - Timer pin output disabled<br>01b - Timer pin open drain or bidirectional output enable<br>10b - Timer pin bidirectional output data<br>11b - Timer pin output|
|15-13<br>—<br>12-8<br>PINSEL|Reserved<br>Timer Pin Select<br>Selects which pin is used by the Timer input or output. PINSEL=i selects the FXIO_Di pin. For pins<br>configured as an output (PINCFG=11), this field takes effect when the register is written.|
|7<br>PINPOL|Timer Pin Polarity<br>For pins configured as an output (PINCFG=11), this field takes effect when the register is written.<br>0b - Pin is active high<br>1b - Pin is active low|
|6|Timer Pin Input Select|
|PININS|When set, the timer input pin is a different pin from the timer output pin. PINSEL must select an even<br>numbered pin when this bit is set, so the output pin is even numbered and input pin is odd numbered.<br>0b - Timer pin input and output are selected by PINSEL.<br>1b - Timer pin input is selected by PINSEL+1, timer pin output remains selected by PINSEL.|
|5|Timer One Time Operation|
|ONETIM|When set, configures the timer to perform a single enable/disable iteration, after which software must<br>clear the timer status flag for the timer to be enabled again.<br>0b - The timer enable event is generated as normal.<br>1b - The timer enable event is blocked unless timer status flag is clear.|
|4-3<br>—|Reserved|
|2-0|Timer Mode|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2704 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|TIMOD|In 8-bit baud counter mode, the lower 8-bits of the counter and compare register are used to configure the<br>baud rate of the timer shift clock, and the upper 8-bits are used to configure the shifter bit count.<br>In 8-bit PWM high mode, the lower 8-bits of the counter and compare register are used to configure the high<br>period of the timer shift clock, and the upper 8-bits are used to configure the low period of the timer shift<br>clock. The shifter bit count is configured using another timer or external signal.<br>In 16-bit counter mode, the full 16-bits of the counter and compare register are used to configure either the<br>baud rate of the shift clock or the shifter bit count.<br>In 16-bit counter disable mode, the full 16-bits of the counter and compare register are used to configure<br>either the baud rate of the shift clock or the shifter bit count.<br>In 8-bit word counter mode, the lower 8-bits of the counter and compare register are used to configure the<br>shifter bit count, and the upper 8-bits are used to configure the shifter word count.<br>In 8-bit PWM low mode, the lower 8-bits of the counter and compare register are used to configure the low<br>period of the timer shift clock and the upper 8-bits are used to configure the high period of the timer shift<br>clock. The shifter bit count is configured using another timer or external signal.<br>In 16-bit input capture mode, the inverted value of 16-bit counter is latched into the compare register when<br>a timer counter disable condition is detected (as configured byTIMDIS). This also sets the timer status flag.<br>The timer counter is immediately restarted from 0xFFFF<br>000b - Timer Disabled.<br>001b - Dual 8-bit counters baud mode.<br>010b - Dual 8-bit counters PWM high mode.<br>011b - Single 16-bit counter mode.<br>100b - Single 16-bit counter disable mode.<br>101b - Dual 8-bit counters word mode.<br>110b - Dual 8-bit counters PWM low mode.<br>111b - Single 16-bit input capture mode.|



#### 71.6.1.34 Timer Configuration N Register (TIMCFG0 - TIMCFG7) 

##### Offset 

For a = 0 to 7: 

|Register<br>TIMCFGa|Offset<br>480h + (a × 4h)|
|---|---|



##### Function 

The options to enable or disable the timer using the Timer N-1 enable or disable are reserved when N is evenly divisible by 4 (eg: Timer 0). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2705 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

~~<mark>NOTE</mark>~~ 

The pin and trigger level/edges specified below refer to the signal state after being modified by the PINPOL or TRGPOL setting in the TIMCTL register. For example, "Trigger low" means a trigger is actually at logic level 1 if the TRGPOL is set to 1 (active low). 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2706-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0 0<br>TIMOUT  TIMDEC  TIMRST<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 0 0 TSTA 0<br>TIMDIS  TIMENA  TSTOP<br>RT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-26<br>—|Reserved|
|25-24|Timer Output|
|TIMOUT|Configures the initial state of the Timer Output and whether it is affected by the Timer reset.<br>00b - Timer output is logic one when enabled and is not affected by timer reset<br>01b - Timer output is logic zero when enabled and is not affected by timer reset<br>10b - Timer output is logic one when enabled and on timer reset<br>11b - Timer output is logic zero when enabled and on timer reset|
|23<br>—|Reserved|
|22-20<br>TIMDEC|Timer Decrement<br>Configures the source of the Timer decrement and the source of the Shift clock.<br>000b - Decrement counter on FlexIO clock, Shift clock equals Timer output.<br>001b - Decrement counter on Trigger input (both edges), Shift clock equals Timer output.<br>010b - Decrement counter on Pin input (both edges), Shift clock equals Pin input.<br>011b - Decrement counter on Trigger input (both edges), Shift clock equals Trigger input.<br>100b - Decrement counter on FlexIO clock divided by 16, Shift clock equals Timer output.<br>101b - Decrement counter on FlexIO clock divided by 256, Shift clock equals Timer output.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2706 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Table continued from the previous page... 

|Field|Function<br>110b - Decrement counter on Pin input (rising edge), Shift clock equals Pin input.<br>111b - Decrement counter on Trigger input (rising edge), Shift clock equals Trigger input.|
|---|---|
|19<br>—|Reserved|
|18-16<br>TIMRST|Timer Reset<br>Configures the condition that causes the timer counter (and optionally the timer output) to be reset. In<br>8-bit counter mode, the timer reset only resets the lower 8-bits that configure the baud rate. In all other<br>modes, the timer reset resets the full 16-bits of the counter.<br>000b - Timer never reset<br>001b - Timer reset on Timer Output high.<br>010b - Timer reset on Timer Pin equal to Timer Output<br>011b - Timer reset on Timer Trigger equal to Timer Output<br>100b - Timer reset on Timer Pin rising edge<br>101b - Reserved<br>110b - Timer reset on Trigger rising edge<br>111b - Timer reset on Trigger rising or falling edge|
|15<br>—|Reserved|
|14-12<br>TIMDIS|Timer Disable<br>Configures the condition that causes the Timer to be disabled and stop decrementing.<br>000b - Timer never disabled<br>001b - Timer disabled on Timer N-1 disable<br>010b - Timer disabled on Timer compare (upper 8-bits match and decrement)<br>011b - Timer disabled on Timer compare (upper 8-bits match and decrement) and Trigger Low<br>100b - Timer disabled on Pin rising or falling edge<br>101b - Timer disabled on Pin rising or falling edge provided Trigger is high<br>110b - Timer disabled on Trigger falling edge<br>111b - Reserved|
|11<br>—|Reserved|
|10-8|Timer Enable|
|TIMENA|Configures the condition that causes the Timer to be enabled and start decrementing.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2707 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||000b - Timer always enabled<br>001b - Timer enabled on Timer N-1 enable<br>010b - Timer enabled on Trigger high<br>011b - Timer enabled on Trigger high and Pin high<br>100b - Timer enabled on Pin rising edge<br>101b - Timer enabled on Pin rising edge and Trigger high<br>110b - Timer enabled on Trigger rising edge<br>111b - Timer enabled on Trigger rising or falling edge|
|7-6<br>—<br>5-4<br>TSTOP|Reserved<br>Timer Stop Bit<br>The stop bit can be added on a timer compare (between each word) or on a timer disable. When stop bit<br>is enabled, configured shifters output the contents of the stop bit when the timer is disabled. When stop<br>bit is enabled on timer disable, the timer remains disabled until the next rising edge of the shift clock. If<br>configured for both timer compare and timer disable, only one stop bit is inserted on timer disable.<br>00b - Stop bit disabled<br>01b - Stop bit is enabled on timer compare<br>10b - Stop bit is enabled on timer disable<br>11b - Stop bit is enabled on timer compare and timer disable|
|3-2<br>—|Reserved|
|1<br>TSTART|Timer Start Bit<br>When start bit is enabled, configured shifters outputs the contents of the start bit when the timer is<br>enabled and the timer counter reloads from the compare register on the first rising edge of the shift clock.<br>0b - Start bit disabled<br>1b - Start bit enabled|
|0<br>—|Reserved|



#### 71.6.1.35 Timer Compare N Register (TIMCMP0 - TIMCMP7) 

Offset 

For a = 0 to 7: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2708 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

|Register<br>TIMCMPa|Offset<br>500h + (a × 4h)|
|---|---|



##### Function 

##### Contains the timer compare value. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2709-06.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>CMP<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16|Reserved|
|—||
|15-0|Timer Compare Value|
|CMP|The timer compare value is loaded into the timer counter when the timer is first enabled, when the timer is<br>reset and when the timer decrements down to zero.<br>In 8-bit baud counter mode, the lower 8-bits configure the baud rate divider equal to (CMP[7:0] + 1) * 2. The<br>upper 8-bits configure the number of bits in each word equal to (CMP[15:8] + 1) / 2.<br>In 8-bit PWM high mode, the lower 8-bits configure the high period of the output to (CMP[7:0] + 1) and the<br>upper 8-bits configure the low period of the output to (CMP[15:8] + 1).<br>In 16-bit counter mode, the compare value can be used to generate the baud rate divider (if shift clock source<br>is timer output) to equal (CMP[15:0] + 1) * 2. When the shift clock source is a pin or trigger input, the compare<br>register is used to set the number of bits in each word equal to (CMP[15:0] + 1) / 2.<br>In 16-bit counter disable mode, the compare value can be used to generate the baud rate divider (if shift<br>clock source is timer output) to equal (CMP[15:0] + 1) * 2. When the shift clock source is a pin or trigger input,<br>the compare register is used to set the number of bits in each word equal to (CMP[15:0] + 1) / 2.<br>In 8-bit word counter mode, the lower 8-bits configure the number of bits in each word equal to (CMP[7:0]<br>+ 1) / 2. The upper 8-bits configure the number of words to transfer equal to (CMP[15:8] + 1) / 2.<br>In 8-bit PWM low mode, the lower 8-bits configure the low period of the output to (CMP[7:0] + 1) and the<br>upper 8-bits configure the high period of the output to (CMP[15:8] + 1).|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2709 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||In 16-bit input capture mode, the compare register is updated with the inverse of the timer counter value<br>whenever the timer status flag is set. The timer compare register should only be read when the timer status<br>flag is set.|



#### 71.6.1.36 Shifter Buffer N Nibble Byte Swapped Register (SHIFTBUFNBS0 - SHIFTBUFNBS7) 

##### Offset 

For a = 0 to 7: 

|Register<br>SHIFTBUFNBSa|Offset<br>680h + (a × 4h)|
|---|---|



##### Function 

SHIFTBUF register contents, but contents of this register are nibble swapped within each byte. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||SHIFTB|UFNBS||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||SHIFTB|UFNBS||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-0|Shift Buffer|
|SHIFTBUFNBS|Alias to SHIFTBUF register, except reads/writes to this register are nibble swapped within each|
||byte. Reads return { SHIFTBUF[27:24], SHIFTBUF[31:28], SHIFTBUF[19:16], SHIFTBUF[23:20],<br>SHIFTBUF[11:8], SHIFTBUF[15:12], SHIFTBUF[3:0], SHIFTBUF[7:4] }.|



#### 71.6.1.37 Shifter Buffer N Half Word Swapped Register (SHIFTBUFHWS0 - SHIFTBUFHWS7) 

##### Offset 

For a = 0 to 7: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2710 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

|Register<br>SHIFTBUFHWSa|Offset<br>700h + (a × 4h)|
|---|---|



##### Function 

SHIFTBUF register contents, but contents of this register are half word swapped. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2711-06.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>SHIFTBUFHWS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>SHIFTBUFHWS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Shift Buffer|
|SHIFTBUFHWS|Alias to SHIFTBUF register, except reads/writes to this register are half word swapped. Reads return<br>{ SHIFTBUF[15:0], SHIFTBUF[31:16] }.|



#### 71.6.1.38 Shifter Buffer N Nibble Swapped Register (SHIFTBUFNIS0 - SHIFTBUFNIS7) 

##### Offset 

For a = 0 to 7: 

|Register<br>SHIFTBUFNISa|Offset<br>780h + (a × 4h)|
|---|---|



##### Function 

SHIFTBUF register contents, but contents of this register are nibble swapped. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2711 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2712-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>SHIFTBUFNIS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>SHIFTBUFNIS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Shift Buffer|
|SHIFTBUFNIS|Alias to SHIFTBUF register, except reads/writes to this register are nibble swapped. Reads<br>return { SHIFTBUF[3:0], SHIFTBUF[7:4], SHIFTBUF[11:8], SHIFTBUF[15:12], SHIFTBUF[19:16],<br>SHIFTBUF[23:20], SHIFTBUF[27:24], SHIFTBUF[31:28] }.|



#### 71.6.1.39 Shifter Buffer N Odd Even Swapped Register (SHIFTBUFOES0 - SHIFTBUFOES7) 

##### Offset 

For a = 0 to 7: 

|Register<br>SHIFTBUFOESa|Offset<br>800h + (a × 4h)|
|---|---|



##### Function 

SHIFTBUF register contents, but contents of this register have odd and even bits partioned separately. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||SHIFTB|UFOES||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||SHIFTB|UFOES||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2712 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

##### Fields 

|Field|Function|
|---|---|
|31-0|Shift Buffer|
|SHIFTBUFOES|Alias to SHIFTBUF register, except reads/writes to this register have the odd and even bits partitioned<br>separately. Only 32-bit accesses are supported to this register. Reads return { SHIFTBUF[31],<br>SHIFTBUF[29],<br>SHIFTBUF[27],SHIFTBUF[25],SHIFTBUF[23],SHIFTBUF[21],SHIFTBUF[19],SHIFTBUF[17],SHIFTBUF[<br>15],SHIFTBUF[13],SHIFTBUF[11],SHIFTBUF[9], SHIFTBUF[7], SHIFTBUF[5], SHIFTBUF[3],<br>SHIFTBUF[1], SHIFTBUF[30], SHIFTBUF[28], SHIFTBUF[26], SHIFTBUF[24], SHIFTBUF[22],<br>SHIFTBUF[20], SHIFTBUF[18], SHIFTBUF[16], SHIFTBUF[14], SHIFTBUF[12], SHIFTBUF[10],<br>SHIFTBUF[8], SHIFTBUF[6], SHIFTBUF[4], SHIFTBUF[2], SHIFTBUF[0] }.|



#### 71.6.1.40 Shifter Buffer N Even Odd Swapped Register (SHIFTBUFEOS0 - SHIFTBUFEOS7) 

##### Offset 

For a = 0 to 7: 

|Register<br>SHIFTBUFEOSa|Offset<br>880h + (a × 4h)|
|---|---|



##### Function 

SHIFTBUF register contents, but contents of this register have even and odd bits partioned separately. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||SHIFTB|UFEOS||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||SHIFTB|UFEOS||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-0|Shift Buffer|
|SHIFTBUFEOS|Alias to SHIFTBUF register, except reads/writes to this register have the even and odd bits partitioned|
||separately. Only 32-bit accesses are supported to this register. Reads return { SHIFTBUF[30],|
||SHIFTBUF[28], SHIFTBUF[26], SHIFTBUF[24], SHIFTBUF[22], SHIFTBUF[20], SHIFTBUF[18],|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2713 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

|Field|Function|
|---|---|
||SHIFTBUF[16], SHIFTBUF[14], SHIFTBUF[12], SHIFTBUF[10], SHIFTBUF[8], SHIFTBUF[6],<br>SHIFTBUF[4], SHIFTBUF[2], SHIFTBUF[0], SHIFTBUF[31], SHIFTBUF[29],<br>SHIFTBUF[27],SHIFTBUF[25],SHIFTBUF[23],SHIFTBUF[21],SHIFTBUF[19],SHIFTBUF[17],SHIFTBUF[<br>15],SHIFTBUF[13],SHIFTBUF[11],SHIFTBUF[9], SHIFTBUF[7], SHIFTBUF[5], SHIFTBUF[3],<br>SHIFTBUF[1] }.|



#### 71.6.1.41 Shifter Buffer N Halfword Byte Swapped Register (SHIFTBUFHBS0 - SHIFTBUFHBS7) 

##### Offset 

For a = 0 to 7: 

|Register<br>SHIFTBUFHBSa|Offset<br>900h + (a × 4h)|
|---|---|



##### Function 

SHIFTBUF register contents, but contents of this register are halfword byte swapped. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/071_Flexible_I_O_-FlexIO-/S32K3XXRM_数据表.pdf-2714-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>SHIFTBUFHBS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>SHIFTBUFHBS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Shift Buffer|
|SHIFTBUFHBS|Alias to SHIFTBUF register, except reads/writes to this register are halfword byte swapped. Reads return<br>{ SHIFTBUF[23:16], SHIFTBUF[31:24], SHIFTBUF[7:0], SHIFTBUF[15:8] }.|



## 71.7 Glossary 

Baud rate Number of bits transmitted or received per second by the LPUART 

Break character Break character is generated when the transmitter is holding the data line at the space level for at least 1 character time 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2714 / 4640 

NXP Semiconductors 

Flexible I/O (FlexIO) 

Idle character Idle character is generated when the transmitter is holding the data line at logic 1 for at least 1 character time PWM Pulse Width Modulation 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2715 / 4640 

