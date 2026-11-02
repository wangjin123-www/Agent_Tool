NXP Semiconductors 

# Chapter 64 Software Watchdog Timer (SWT) 

## 64.1 Chip-specific SWT information 

### 64.1.1 SWT instances and configuration 

This chip supports up to three instances of SWT, one for each Cortex-M7 core. 

Table 370. SWT instances 

|Instance|S32K358|S32K322/S32K324|S32K311/S32K312/S32K314/S32K342/S32K344|
|---|---|---|---|
|SWT_0|Yes|Yes|Yes|
|SWT_1|Yes|Yes|No|
|SWT_2|Yes|No|No|



##### Table 371. SWT configuration 

|Instance|Core|Reset type|Clock Source|SWT_MIN_TO<br>(100μs)|SWT_TO_RST (25ms)|
|---|---|---|---|---|---|
|SWT_0<sup>1</sup>|Cortex-M7_0|Functional Reset -<br>RAM retention|SIRC (32K)|3|320h|
|SWT_1|Cortex-M7_1|Functional Reset -<br>RAM retention|SIRC (32K)|3|320h|
|SWT_2|Cortex-M7_2|Functional Reset -<br>RAM retention|SIRC (32K)|3|320h|



1. SWT_0 supports operation in STANDBY mode. 

###### ~~<mark>NOTE</mark>~~ 

When using SWT as a wakeup source from standby, software should ensure proper value of timeout such that SWT timeout doesn't get expired again (after wakeup till standby exit is completed). The timeout should be programmed to a value greater than the time till standby exit is complete (sum of standby exit time and the time till software disables padkeeping). 

~~<mark>NOTE</mark>~~ 

The "Reset only the SWT" feature using SWT_RRR[RRF] is supported only when SWT reset reaction is demoted to interrupt within MC_RGM. 

Protect SWT from service by non-core masters 

You must program protection for the SWT registers so that only core masters can service SWT. 

When an SWT timeout takes place, the logic generating a reset to the system runs off the slow internal RC oscillator (32KHz). It could therefore take the SWT almost 31.25μs to reset the system, after timeout, leaving more time for runaway code to execute. The register interface clock of SWT is running from AIPS_SLOW_CLK, see Clocking chapter for more details. The register interface clock is responsible for generating the abort for invalid access while the counter clock is responsible for generating the SWT reset request. Since there is a synchronization happening between the register interface clock and counter clock domains before generating the SWT reset request, thus the generation of the reset request can take a number of register interface clock cycles after an invalid access is done. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2362 / 4640 

NXP Semiconductors 

Software Watchdog Timer (SWT) 

Clock source 

SWT is clocked by SIRC only. 

## 64.2 Introduction 

The Software Watchdog Timer (SWT) is a 32-bit window watchdog timer that enables the system to recover from situations such as: 

- Software trapped in a loop 

- A bus transaction failing to terminate 

In regular operation, SWT requires periodic execution of a watchdog servicing operation. The servicing operation resets the timer to a specified timeout period. If this servicing action does not occur before the timer expires, SWT generates an interrupt or a hardware reset request. 

You can configure SWT to generate a reset request or an interrupt on the initial timeout. SWT always generates a reset request on a second consecutive timeout. 

## 64.3 Features 

SWT has the following features: 

- 32-bit countdown timer 

- Selection of regular or window servicing 

- Selection of reset request or interrupt on an initial timeout 

- Selection of fixed or keyed service sequence 

- Master access protection 

- Hard and soft configuration lock bits 

## 64.4 Initialize the SWT 

To initialize the SWT, you must do the following: 

- Select the clock source (if there are more than one possible sources). 

- Set the timeout period. 

- Control timeout behavior. There are two options: 

   - Select reset request on timeout, or 

   - Select interrupt on initial timeout. 

You must initialize all registers before enabling SWT (CR[WEN]). You can initialize the registers in any sequence. 

### 64.4.1 Select the clock source 

See the chip-specific SWT information to find the clock source that drives the countdown timer. 

### 64.4.2 Set the timeout period 

When you enable SWT, it loads the greater of the specified watchdog timeout period or the minimum timeout period into an internal 32-bit countdown timer every time you perform a valid service operation. 

To set the watchdog timeout period: 

- Write the desired timeout period to TO[WTO]. 

The minimum timeout period is 3 clock cycles. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2363 / 4640 

NXP Semiconductors 

Software Watchdog Timer (SWT) 

### 64.4.3 Control timeout behavior 

SWT can respond to a timeout in one of two ways: 

- Generate an immediate reset request on any timeout. 

- Generate an interrupt and load the countdown timer on an initial timeout, then generate a reset request on a subsequent timeout. 

#### 64.4.3.1 Select reset request on timeout 

To configure SWT to generate an immediate reset request on any timeout: 

- Write 0 to CR[ITR]. 

#### 64.4.3.2 Select interrupt on initial timeout 

To configure SWT to generate an interrupt on an initial timeout: 

- Write 1 to CR[ITR]. 

In this configuration, on the initial timeout: 

- SWT loads the countdown timer with the timeout period (TO[WTO]). 

- SWT indicates the interrupt with the timeout interrupt flag (IR[TIF]). 

- If a second consecutive timeout occurs before writing the service sequence for the first timeout, SWT generates a reset request. 

You clear the interrupt flag by writing 1 to IR[TIF]. 

### 64.4.4 Configure locking and unlocking 

You can lock the SWT configuration with either a hard lock or a soft lock. When either lock is in effect, CR, TO, WN, and SK are read-only. 

#### 64.4.4.1 Enable the hard lock 

To enable the hard lock: 

- Write 1 to CR[HLK]. 

Hard lock is disabled only by a reset. 

#### 64.4.4.2 Enable the soft lock 

To enable the soft lock: 

- Write 1 to CR[SLK]. 

#### 64.4.4.3 Unlock the soft lock 

To unlock the soft lock: 

1. Write C520h to SR[WSC]. 

2. Write D928h to SR[WSC]. 

This unlock sequence: 

- Ignores service sequence writes. 

- Recognizes the unlock sequence regardless of previous writes. 

- Recognizes the unlock sequence regardless of the time between writes. 

- Does not require CR[WEN] to be 1. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2364 / 4640 

NXP Semiconductors 

Software Watchdog Timer (SWT) 

You can write this unlock sequence at any time. 

~~<mark>NOTE</mark>~~ 

It is possible for a keyed service sequence to unlock soft lock. See Avoid soft unlock for the procedure to handle this situation. 

#### 64.4.4.4 Avoid soft unlock 

When SWT operates in keyed sequence service, the sequence of service keys generated by the pseudorandom generator includes the unlock keys for soft lock. If one or more service routines use both unlock keys in the proper order, 0xC520 followed at any future time by 0xD928, SWT unlocks soft lock (CR[SLK] = 0). The unlock sequence logic ignores any service keys other than the unlock keys, so the unlock keys don’t have to be inserted consecutively. If the second unlock key is also the second key of a service operation, unlock occurs before the service operation completes. 

To avoid unlock: 

If the service routine writes a key value of C520h to SR[WSC] as a key of the service operation, then do the following: 

1. Complete the service operation. 

2. Complete the unlock sequence by writing the second unlock key, D928h, to SR[WSC]. 

3. Reinitiate the soft lock (CR[SLK] = 1). 

### 64.4.5 Select behavior on an invalid access 

SWT can respond to an invalid access one of two ways: 

- Generate a bus error. 

- Generate a bus error and, if SWT is enabled, a reset request. 

To select how SWT responds to an invalid access: 

- Write the appropriate value to CR[RIA]. 

## 64.5 Enable the SWT 

To enable the SWT: 

- Write 1 to CR[WEN]. 

## 64.6 Initiate service operations 

When enabled, SWT requires periodic execution of a servicing operation. 

SWT can operate in one of the following service sequence modes: 

- Fixed service sequence 

- Keyed service sequence 

### 64.6.1 Initiate a fixed service sequence 

To initiate the fixed service sequence: 

1. Select the fixed servicing mode (write 00b to CR[SMD]). 

2. Write A602h to SR[WSC]. 

3. Write B480h to SR[WSC]. 

There is no timing requirement between the two writes. The service sequence logic ignores unlock-sequence writes. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2365 / 4640 

NXP Semiconductors 

Software Watchdog Timer (SWT) 

### 64.6.2 Initiate a keyed service sequence 

To initiate the keyed service sequence: 

1. Select the keyed servicing mode (write 01b to CR[SMD]). 

2. Read the initial service key from SK[SK]. 

3. Calculate the next service key using the provided equation. 

4. Write that service key to SR[WSC]. 

5. Repeat steps 2 through 4 one time. 

See Service key generation for information about service keys. 

### 64.6.3 Select window service mode 

In window service mode, you must write the service sequence only when the watchdog timer is less than the window start value (WN[WST]). If you write the service sequence outside of this window, the access is invalid and generates a bus error or reset request depending on the Reset on Invalid Access setting (CR[RIA]). 

For example, if the timeout period is 5000 and the window start value is 1000, you must write the service sequence during the last 20% of the timeout period. 

Synchronization logic in SWT causes a slight delay in the opening of the window. This delay can be up to three system clock cycles plus four counter clock cycles. 

To select window service mode: 

- Write 1 to (CR[WND]. 

## 64.7 Reset only the SWT 

When a timeout triggers a reset request and the application does not require a system reset, you can make the SWT instance reset itself rather than the whole system. 

To make a timeout reset request trigger only an SWT reset (rather than the whole system), write 1 to the Reset Request Flag (RRR[RRF]). 

This action causes SWT to: 

- Clear the reset request. 

- If an interrupt request also occurred, clear the interrupt request (IR[TIF]). 

- Reset and restart the SWT. 

For systems with multiple SWT instances, this feature allows you to reset an individual SWT instance, avoiding the widespread impact of a system reset. 

## 64.8 Test SWT operation 

When you disable SWT, it loads the current countdown timer into CO[CNT]. When you enable SWT, it clears this register. You can use CO[CNT] to perform a software self-test of SWT. 

To test SWT operation: 

1. Enable the SWT (CR[WEN] = 1). 

2. Do not service SWT for a fixed period of time that is less than the timeout value. 

3. Disable the SWT (CR[WEN] = 0). 

4. Read the value in CO[CNT] to determine whether the internal countdown timer is working properly. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2366 / 4640 

NXP Semiconductors 

Software Watchdog Timer (SWT) 

~~<mark>NOTE</mark>~~ 

The value shown in CO[CNT] can lag behind the actual internal timer up to six system clock cycles plus eight counter clock cycles. 

## 64.9 Functional description 

### 64.9.1 Behavior in different chip and core modes 

SWT supports the core modes of operation as follows: 

|Core mode|SWT behavior|
|---|---|
|Normal|When SWT is enabled (CR[WEN]= 1), the SWT timer counts down continuously.|
|Debug|IfCR[FRZ]= 1, SWT stops the timer; otherwise, the timer continues to run.|
|Stop or Standby|IfCR[STP]= 1, SWT stops the timer; otherwise, the timer continues to run.|



### 64.9.2 Register access latency 

Accesses to SWT registers occur with no peripheral bus wait states. The peripheral bus bridge may add 1 or more system wait states. However, due to synchronization logic in the SWT design, recognition of the service sequence or configuration changes may require up to three system clock cycles plus seven counter clock cycles. 

### 64.9.3 Service key generation 

SWT generates service keys with the pseudorandom key generator defined by the following equation. 

Figure 353. Pseudorandom key generator 

This algorithm generates a sequence of 2<sup>16</sup> different key values before repeating. In keyed service sequence mode, each time you write a valid key to SR[WSC], SWT updates SK[SK] with the next key. 

For example, if the previous service key (SK[SK]) is 100h, then the next service sequence keys are 1103h followed by 2136h. 

## 64.10 SWT register descriptions 

The SWT programming model allows only 32-bit (word) accesses. 

Any of the following attempted accesses are invalid: 

- Non-32-bit accesses 

- Writes to read-only registers 

- Writes of incorrect values to SR when SWT is enabled 

- Accesses to reserved addresses 

- Accesses by masters without permission 

You control how SWT responds to an invalid access with CR[RIA]. 

### 64.10.1 SWT memory map 

SWT_0 base address: 4027_0000h 

SWT_1 base address: 4046_C000h 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2367 / 4640 

NXP Semiconductors 

Software Watchdog Timer (SWT) 

##### SWT_2 base address: 4047_0000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|Control (CR)|32|RW|FF00_010Ah|
|4h|Interrupt (IR)|32|W1C|0000_0000h|
|8h|Timeout (TO)|32|RW|0000_0320h|
|Ch|Window (WN)|32|RW|0000_0000h|
|10h|Service (SR)|32|WORZ|0000_0000h|
|14h|Counter Output (CO)|32|RO|0000_0000h|
|18h|Service Key (SK)|32|RW|0000_0000h|
|1Ch|Event Request (RRR)|32|W1C|0000_0000h|



### 64.10.2 Control (CR) 

##### Offset 

|Register|Offset|
|---|---|
|CR|0h|



##### Function 

Contains fields for configuring and controlling SWT. The register is read-only if either hard lock or soft lock is enabled (either HLK or SLK is 1). 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|MAP0|MAP1|MAP2|MAP3|MAP4|MAP5|MAP6|MAP7|||||0||||
|Reset|1|1|1|1|1|1|1|1|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||0|||SMD||RIA|WND|ITR|HLK|SLK|Reserv<br>ed|STP|FRZ|WEN|
|Reset|0|0|0|0|0|0|0|1|0|0|0|0|1|0|1|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2368 / 4640 

NXP Semiconductors 

Software Watchdog Timer (SWT) 

##### Fields 

|Field|Function|
|---|---|
|31|Master Access Protection 0|
|MAP0|The platform bus master assignments are chip-specific.<br>The number of this field corresponds to the XRDC DIDs of the bus master. MAP0 corresponds to XRDC<br>DIDs 0 and 8.<br>0b - Access disabled<br>1b - Access enabled|
|30<br>MAP1|Master Access Protection 1<br>See the description for MAP0. MAP1 corresponds to XRDC DIDs 1 and 9.<br>0b - Access disabled<br>1b - Access enabled|
|29|Master Access Protection 2|
|MAP2|See the description for MAP0. MAP2 corresponds to XRDC DIDs 2 and 10.<br>0b - Access disabled<br>1b - Access enabled|
|28|Master Access Protection 3|
|MAP3|See the description for MAP0. MAP3 corresponds to XRDC DIDs 3 and 11.<br>0b - Access disabled<br>1b - Access enabled|
|27<br>MAP4|Master Access Protection 4<br>See the description for MAP0. MAP4 corresponds to XRDC DIDs 4 and 12.<br>0b - Access disabled<br>1b - Access enabled|
|26|Master Access Protection 5|
|MAP5|See the description for MAP0. MAP5 corresponds to XRDC DIDs 5 and 13.<br>0b - Access disabled<br>1b - Access enabled|
|25|Master Access Protection 6|
|MAP6|See the description for MAP0. MAP6 corresponds to XRDC DIDs 6 and 14.<br>0b - Access disabled<br>1b - Access enabled|
|24|Master Access Protection 7<br>See the description for MAP0. MAP7 corresponds to XRDC DIDs 7 and 15.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2369 / 4640 

NXP Semiconductors 

Software Watchdog Timer (SWT) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|MAP7|0b - Access disabled<br>1b - Access enabled|
|23-11<br>—|Reserved|
|10-9<br>SMD|Service Mode<br>00b - Fixed Service Sequence. To service the watchdog, write the fixed sequence 0xA602,<br>0xB480 to SR.<br>01b - Keyed Service Sequence. To service the watchdog, write two pseudorandom key values to<br>SR.<br>10b - Reserved. Do not use this value. Writing this value can cause the watchdog to not be<br>serviced.<br>11b - Reserved. Do not use this value. Writing this value can cause the watchdog not to be<br>serviced.|
|8<br>RIA|Reset on Invalid Access<br>Controls how SWT responds to an invalid access.|
||For a description of how this chip implements SWT reset requests resulting from SWT<br>invalid accesses, see the chip-specific SWT information.<br>~~NOTE~~|
||0b - Generate a bus error<br>1b - Generate a bus error and reset request. If SWT is enabled (WEN= 1), generate a bus error<br>and a reset request; otherwise, generate a bus error.|
|7|Window Mode|
|WND|Specify regular or window mode operation.<br>0b - Regular mode. Can execute service sequence at any time<br>1b - Window mode. Can execute service sequence only when the timeout counter is less than the<br>value inWN|
|6|Interrupt Then Reset Request|
|ITR|For a description of how this chip implements SWT reset requests and interrupt requests<br>resulting from SWT timeouts, see the chip-specific SWT information.<br>~~NOTE~~|
||0b - Generate a reset request on a timeout<br>1b - Generate an interrupt on an initial timeout; generate a reset request on a second consecutive<br>timeout|
|5|Hard Lock|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2370 / 4640 

NXP Semiconductors 

Software Watchdog Timer (SWT) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|HLK|Indicates that the hard lock is enabled. You cannot directly write 0 to this field. This field becomes 0 only after<br>a reset.<br>0b - CR, TO, WN, and SK are read/write registers if SLK is also 0<br>1b - CR, TO, WN, and SK are read-only registers|
|4<br>SLK|Soft Lock<br>Indicates that the soft lock is enabled. You cannot directly write 0 to this field. Clear this field by writing the<br>unlock sequence to the service register.<br>0b - CR, TO, WN, and SK are read/write registers if HLK is also 0<br>1b - CR, TO, WN, and SK are read-only registers|
|3<br>—<br>2<br>STP|Reserved<br>Stop Mode Control<br>Controls the watchdog timer when the chip enters Stop or Standby mode.|
||This field is not supported in every instance. The following table includes only<br>supported registers.<br>~~NOTE~~|
||Instance<br>Field supported in<br>Field not supported in|
||SWT_0<br>CR<br>—|
||SWT_1<br>—<br>CR|
||SWT_2<br>—<br>CR|
||0b - Timer continues<br>1b - Timer stops|
|1<br>FRZ|Debug Mode Control<br>Controls the watchdog timer when the core enters Debug mode.<br>0b - Timer continues<br>1b - Timer stops|
|0<br>WEN|Watchdog Enable<br>Enables or disables SWT.<br>The reset value is 0. Therefore, after reset, you must enable SWT to start the countdown timer.<br>0b - Disabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2371 / 4640 

NXP Semiconductors 

Software Watchdog Timer (SWT) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - Enabled|



### 64.10.3 Interrupt (IR) 

##### Offset 

|Register|Offset|
|---|---|
|IR|4h|



##### Function 

The timeout interrupt flag. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Timer/064_Software_Watchdog_Timer_-SWT-/S32K3XXRM_数据表.pdf-2372-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 TIF<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-1<br>—|Reserved|
|0|Timeout Interrupt Flag|
|TIF|Write 1 to this field to clear the flag and interrupt. Writing a 0 has no effect.|
||0b - No interrupt request|
||1b - Interrupt request due to an initial timeout|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2372 / 4640 

NXP Semiconductors 

Software Watchdog Timer (SWT) 

### 64.10.4 Timeout (TO) 

##### Offset 

|Register|Offset|
|---|---|
|TO|8h|



##### Function 

Contains the 32-bit timeout period. The register is read-only if either hard lock or soft lock is enabled (CR[HLK] or CR[SLK] is 1). 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Timer/064_Software_Watchdog_Timer_-SWT-/S32K3XXRM_数据表.pdf-2373-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>WTO<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>WTO<br>W<br>Reset 0 0 0 0 0 0 1 1 0 0 1 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Watchdog Timeout|
|WTO|Watchdog timeout period in clock cycles. When software writes a service sequence or enables SWT, SWT|
||loads the internal 32-bit countdown timer with this value or 3h, whichever is greater.|



### 64.10.5 Window (WN) 

##### Offset 

|Register|Offset|
|---|---|
|WN|Ch|



##### Function 

Contains the 32-bit window start value. SWT clears this register on reset. The register is read-only if either hard lock or soft lock is enabled (CR[HLK] or CR[SLK] is 1). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2373 / 4640 

NXP Semiconductors 

Software Watchdog Timer (SWT) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Timer/064_Software_Watchdog_Timer_-SWT-/S32K3XXRM_数据表.pdf-2374-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>WST<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>WST<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Window Start Value|
|WST|When you enable window mode (CR[WND]), you can write the service sequence only when the internal<br>timer is less than this value.|



### 64.10.6 Service (SR) 

##### Offset 

|Register|Offset|
|---|---|
|SR|10h|



##### Function 

##### Initiates the service operation and resets the watchdog timer. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Timer/064_Software_Watchdog_Timer_-SWT-/S32K3XXRM_数据表.pdf-2374-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W WSC<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2374 / 4640 

NXP Semiconductors 

Software Watchdog Timer (SWT) 

##### Fields 

|Field|Function|
|---|---|
|31-16|Reserved|
|—||
|15-0|Watchdog Service Code|
|WSC|Use this field to service the watchdog and to unlock the Soft Lock (CR[SLK]).<br>To service the watchdog: If SWT is in keyed service mode (CR[SMD]), write two pseudorandom key values<br>to WSC (seeService key generationfor details). Otherwise, write the following values to WSC, in the<br>order shown:<br>1. A602h|
||2. B480h|
||To unlock the Soft Lock (CR[SLK]), write the following values to WSC, in the order shown:<br>1. C520h|
||2. D928h|
||When read, WSC always returns zero.|



### 64.10.7 Counter Output (CO) 

##### Offset 

|Register|Offset|
|---|---|
|CO|14h|



##### Function 

##### Shows the value of the internal timer when SWT is disabled. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||CN|T||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||CN|T||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2375 / 4640 

NXP Semiconductors 

Software Watchdog Timer (SWT) 

##### Fields 

|Field|Function|
|---|---|
|31-0|Watchdog Count|
|CNT|When SWT is disabled (CR[WEN]is 0), CNT shows the value of the internal timer. When SWT is enabled|
||(CR[WEN]is 1), it writes 0 to CNT. Values in this field can lag behind the internal timer value up to six|
||system clock cycles plus eight counter clock cycles. Therefore, the CNT value that is read immediately after<br>disabling SWT may be higher than the actual value of the internal timer.|



### 64.10.8 Service Key (SK) 

##### Offset 

|Register|Offset|
|---|---|
|SK|18h|



##### Function 

Holds the previous (or initial) service key value. This register is read-only if either hard lock or soft lock is enabled (CR[HLK] or CR[SLK] is 1). 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||0|||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||SK|||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-16|Reserved|
|—||
|15-0|Service Key|
|SK|Holds the previous (or initial) service key value used inInitiate a keyed service sequence. IfCR[SMD]is 01b,<br>the next key value to write toSRis (17 * SK + 3) mod 2<sup>16</sup>.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2376 / 4640 

NXP Semiconductors 

Software Watchdog Timer (SWT) 

### 64.10.9 Event Request (RRR) 

##### Offset 

|Register|Offset|
|---|---|
|RRR|1Ch|



##### Function 

Contains the timeout reset request flag. See the chip-specific information for the specific event associated with this flag. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Timer/064_Software_Watchdog_Timer_-SWT-/S32K3XXRM_数据表.pdf-2377-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 RRF<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-1<br>—|Reserved|
|0|Reset Request Flag|
|RRF|Write 1 to clear the flag and request. Writing 0 has no effect.|
||0b - No reset request|
||1b - Any reset request initiated|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2377 / 4640 

