NXP Semiconductors 

# Chapter 32 Reset Generation Module (MC_RGM) 

## 32.1 Chip-specific MC_RGM information 

### 32.1.1 MC_RGM configuration 

The "Reset sources—POR, Destructive, and Functional" section of the "Reset Overview" chapter provides information about MC_RGM's reset sources. The chapter also provides details about the chip's reset architecture. 

~~<mark>NOTE</mark>~~ 

The ERCTRL register configuration takes several cycles to be effective. Any further access to MC_RGM must happen after at least nine AIPS_SLOW_CLK cycles of writing to ERCTRL. 

Table 185. Register fields and applicability 

|Register|Bit field|Chips where applicable|
|---|---|---|
|Functional /External Reset Status|SWT1_RST|S32K324, S32K322, S32K358|
|Register (FES)|SWT2_RST|S32K358|
|Functional Event Reset Disable|D_SWT1_RST|S32K324, S32K322, S32K358|
|Register (FERD)|D_SWT2_RST|S32K358|



### 32.1.2 Functional reset entry timer implementation 

The default timeout value of the functional reset entry timer is 2048 clocks of MC_RGM clock (FIRC). If the RGM entry sequence hangs, then POR_WDG would trigger and the status of this functional reset entry sequence timeout is indicated at chip-level status register. The status of timeout in such case, is indicated at DCM.DCMROPP1[28]. There is no impact to the device behavior if the functional reset entry sequence gets completed within the POR_WDG timeout window. 

### 32.1.3 S32K3xx reset state machine 

The reset sequence of the S32K3xx products is depicted in the figure below: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1005 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/032_Reset_Generation_Module_-MC_RGM-/S32K3XXRM_数据表.pdf-1006-02.png)


<!-- Start of picture text -->
Power-on<br>reset event<br>Power-on<br>sequence<br>Exit from<br>Destructive Standby mode<br>reset event Destructive reset<br>sequence In case of Standby mode, only the Run<br>domain resets and the exit from POR<br>happens on Standby mode exit.<br>Functional reset Functional reset Standby mode<br>entry sequence sequence<br>Functional Enter<br>Out of reset<br>reset event Standby mode<br><!-- End of picture text -->

Figure 134. S32K3xx reset state machine 

## 32.2 Introduction 

The Reset Generation Module (MC_RGM) centralizes the different reset sources and manages the reset sequence of the chip. It provides a register interface and the reset sequencer. There are various registers available in this module to monitor and control the chip reset sequence. 

The following figure shows the block diagram of MC_RGM. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1006 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/032_Reset_Generation_Module_-MC_RGM-/S32K3XXRM_数据表.pdf-1007-02.png)


<!-- Start of picture text -->
Power-on<br>MC_ME<br>Registers<br>    Platform interface<br>MC_CGM<br>Destructive reset  n<br>Chip resets<br>External reset Software resettable<br> domains<br>Reset state<br> machine<br>Functional reset  n<br> filter<br>Destructive reset<br>Functional reset  filter<br><!-- End of picture text -->

Figure 135. MC_RGM block diagram 

## 32.3 Features 

Here are the key features of MC_RGM: 

- Support for destructive reset management 

- Support for functional reset management 

- Signaling of reset events after each reset sequence (reset status flags) 

- Configurable escalation of recurring 'functional' resets to 'destructive' reset 

- Configurable escalation of recurring 'destructive' resets to keep the chip in the reset state until the next power-on reset 

- Software controllable reset assertion 

- Pad safe state control generation 

## 32.4 Reset sources 

The different reset sources are organized in three categories: power-on, destructive, and functional. 

A power-on reset source is associated with an event typically related to power-up or low-voltage scenarios. When a power-on reset occurs, the full reset sequence is applied to the chip. This resets the full chip, including the MC_RGM, and the memory content must be considered to be unknown. 

A destructive reset source is associated with an event related to a critical, usually hardware, error or dysfunction. When a destructive reset event occurs, the full reset sequence is applied to the chip. This resets the full chip (except for a small portion, for example FIRC, JTAG interface, and the MC_RGM itself) ensuring a safe start-up state for both digital and analog modules, and the memory content must be considered to be unknown. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1007 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 

A functional reset source is associated with an event related to a less-critical, usually non-hardware, error or dysfunction. When a functional reset event occurs, a partial reset sequence is applied to the chip. In this case, most digital modules are reset normally, while the state of analog modules or specific digital modules (for example, debug modules, flash modules) as well as the system memory content is preserved. 

## 32.5 External signal description 

The MC_RGM interfaces with the RESET_B pin. 

The following table describes the signals that are connected to the I/O pad ring. 

Table 186. MC_RGM external signals 

|Signal name|Reset value|Description|
|---|---|---|
|RESET_B|0|Active low external reset|



## 32.6 RESET_B pin assertion and pin safe state control 

The MC_RGM asserts the RESET_B pin when the device is in a reset sequence, and it remains asserted until the end of the reset sequence. During this reset sequence, most of the chip's pins are safe-stated according to the values shown in the IOMUX table. Note that the safe state values may vary according to the reset sequence type. 

In addition, the MC_RGM has a feature to assert the RESET_B pin through software, without initiating a reset sequence. This is achieved by writing 1b to the ERCTRL[ERASSERT]. When this occurs, most of the chip's pins are safe-stated according to the values shown in the IOMUX table. The RESET_B assertion and pin safe-stating remain active until the end of the next reset sequence. 

This feature is intended for use only in conjunction with self-test of the main reset domain. 

## 32.7 Functional description 

### 32.7.1 Reset state machine 

The main role of MC_RGM is the generation of the reset sequence that ensures that the correct parts of the chip are reset based on the reset source event. 

For each reset event, immediately after it is captured by the MC_RGM, the following takes place: 

1. The corresponding reset event status bit is set in the MC_RGM_DES and MC_RGM_FES registers. 

2. The pins are put into their default states 

3. The RESET_B pin is asserted. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1008 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/032_Reset_Generation_Module_-MC_RGM-/S32K3XXRM_数据表.pdf-1009-02.png)


<!-- Start of picture text -->
Power-on<br>reset event<br>Power-on<br>sequence<br>Destructive Exit from<br>reset event Destructive reset Standby mode<br>sequence<br>Functional reset Functional reset Standby mode<br>entry sequence sequence<br>Functional Enter<br>Out of reset<br>reset event Standby mode<br>Figure 136. Reset sequence<br><!-- End of picture text -->

~~<mark>NOTE</mark>~~ 

See chip-specific MC_RGM information for chip-specific reset sequence details. 

#### 32.7.1.1 Power-on reset sequence 

A reset is always generated when the power-on reset source is asserted, and it has priority over all other reset sources. Such a power-on reset forces the reset state machine to enter the power-on sequence resulting in the assertion of all reset signals. The reset state machine starts progressing when the following two conditions are verified: 

1. All the power-on reset events are cleared 

2. The MC_RGM's clock source (the FIRC) has started up and stabilized 

If a power-on reset event has occurred, the DES[F_POR] bit is set. 

The power-on reset cannot be demoted by the software. 

#### 32.7.1.2 Destructive reset sequence 

The 'Destructive reset sequence' is comprised of a number of phases, where DEST0 is the first phase and is followed by DEST1 and so forth. 

This phase is entered immediately from any phase on a power-on, standby reset sequence, or enabled destructive reset event . A destructive reset counter starts immediately on entry in the DEST0 phase . The DEST0 state is exited to the DEST1 state on the rising edge of FIRC_CLK immediately after all of the following conditions have been established: 

- the DEST0 duration time has expired 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1009 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 

- all dest_rst inputs are deasserted 

The DEST0 state is immediately exited to the power-on state after if a power-on reset event occurs. 

The reset state machine exits the destructive reset sequence and enters the functional reset sequence when: 

- All the destructive reset events are cleared. 

- All the processes that take place during the destructive reset sequence have completed. For details on completed destructive reset sequence, see "Reset process sequence" section in the Reset chapter. 

- The 'destructive' reset escalator counter has not reached the value in DRET[DRET]. 

#### 32.7.1.3 Functional reset sequence 

There are two categories of functional reset sequence, the functional reset entry sequence and the functional reset exit sequence. 

#### 32.7.1.3.1 Functional reset entry sequence 

The functional reset entry sequence is only entered when a functional reset event occurs during the idle phase. 

If a functional reset event occurs during an ongoing reset sequence, the corresponding event status flag is set, and the RESET_B pin is asserted per the reset event's configuration. However, the reset sequence is not influenced, and it continues to progress without interruption. 

No reset is asserted during the functional reset entry sequence. 

The functional reset entry sequence is exited to the DEST0 on the next clock rising edge if a destructive reset event has occurred. The sequence enters the power up sequence if a POR event occurs 

In all other cases, the sequence exits to the first stage of functional reset exit sequence. 

#### 32.7.1.3.2 Functional reset exit sequence 

The functional reset exit sequence is entered either on exit from the destructive reset sequence or on completion of the functional reset entry sequence. The reset state machine exits this sequence and enters the idle phase on verification of the following: 

- All the functional reset events are cleared. 

- All the processes that take place during the destructive reset sequence have completed. For details on completed destructive reset sequence, see "Reset process sequence" section in the Reset chapter. 

If a functional reset event occurs during an ongoing reset sequence, the corresponding event status flag is set, and the RESET_B pin is asserted per the reset event's configuration. However, the reset sequence is not influenced, and it continues to progress without interruption. 

#### 32.7.1.4 Idle phase 

This is the final phase and is entered on exit from the functional reset exit sequence . When this phase is reached, MC_RGM releases control of the system to the platform and waits for the new reset events that can trigger a reset sequence. 

### 32.7.2 Destructive resets 

A destructive reset indicates that an event has occurred after which critical register or memory content can no longer be guaranteed. 

The status flag associated with a given destructive reset event (Destructive Event Status Register (DES)) is set when the destructive reset is asserted and the power-on reset is not asserted. It is possible for multiple status bits to be set simultaneously and the software determines which reset source is the most critical for the application. 

The low-voltage detector threshold ensures that when the reset corresponding to the core supply low-voltage detect is enabled, the supply is sufficient to have the destructive event correctly propagated through the digital logic. Therefore, if a given destructive reset is enabled, MC_RGM ensures that the associated reset event is correctly triggered to the full system. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1010 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 

An enabled destructive reset triggers a reset sequence starting from the beginning of DEST0. 

### 32.7.3 External reset 

MC_RGM manages the external reset coming from RESET_B. The detection of a falling edge on RESET_B starts the reset sequence from the beginning of the destructive reset entry sequence. 

The status flag associated with the external reset falling edge event (the RGM_FES[F_EXR] bit) is set when the external reset is asserted and the power-on reset is not asserted. 

MC_RGM asserts the external reset if the reset sequence is triggered by one of the following: 

- A power-on reset 

- A destructive reset event 

- A functional reset event 

In this case, external reset is asserted until all conditions for the exiting functional reset sequence have been met, with the exception of the RESET_B assertion check 

### 32.7.4 Functional resets 

A functional reset indicates that an event has occurred after which it can be guaranteed that critical register and memory content is still intact. 

The status flag associated with a given functional reset event (Functional /External Reset Status Register (FES)) is set when the functional reset is asserted and the power-on reset is not asserted. It is possible for multiple status bits to be set simultaneously and the software determines which reset source is the most critical for the application. 

An enabled functional reset triggers a reset sequence starting from the beginning of the functional reset entry sequence. 

### 32.7.5 Functional reset entry timer 

The purpose of Functional Reset Entry Timer feature is to indicate any scenario wherein functional reset entry sequence does not get completed in prerequisite time . 

When FRENTC[FRET_EN] is enabled, the functional reset entry timer starts from functional reset event point and gets terminated if the functional reset entry sequence is successfully completed or when it reached to the timeout value . It gets cleared on any destructive or POR reset events. 

The timeout value is controlled by FRENTC[FRET_TIMEOUT]. The FRENTC[FRET_TIMEOUT] value should be greater than zero. If configured as zero, the default timeout value 2048 gets used. 

### 32.7.6 Alternate event generation 

MC_RGM provides alternative events to be generated on reset source assertion. When a reset source is asserted, MC_RGM normally enters the reset sequence. Alternatively, it is possible for some reset source events to be converted from a reset to an interrupt request issued to the core. Alternate event selection for a given reset source is made through the RGM_FERD register as shown in the following table. 

Table 187. Functional Reset Disable Register (RGM_FERD) field descriptions 

|RGM bit FERD value|Generated event|
|---|---|
|0|Reset|
|1|Interrupt request|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1011 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 

The alternate event is cleared by deasserting the source of the request (that is, at the reset source that caused the alternate request) and also clearing the appropriate RGM_FES status bit. 

### 32.7.7 External reset assertion control 

The software indicates to the MC_RGM that the RESET_B is to be asserted by writing to the ERASSERT bit in the RGM_ERCTRL register. When this bit is set by the software, RESET_B gets asserted. Setting of this field does not impact the reset sequence in any way. 

An example where the ERASSERT bit could be set by the software is when entering the self test sequence, during which RESET_B is to be asserted. This indicates the chip is not available in the functional mode although a reset sequence is not in progress. The deassertion of RESET_B is not controlled by the software. Instead, the RESET_B pin remains asserted until the next time the chip exits a reset sequence. 

ERASSERT bit is also cleared during the reset sequence. 

### 32.7.8 Functional reset escalation 

Functional reset escalation can be used to generate a destructive reset if a number of functional resets is occurred between software writes to the RGM_FRET register. This function is enabled by writing a non-zero value to the FRET field of this register. 

After the functional reset escalation is enabled, MC_RGM increases a counter on each functional reset that causes a reset sequence to be initiated (which means, entrance into FUNC0 from the IDLE phase). This counter is cleared on a write of any value to the RGM_FRET register and on any power-on or destructive reset. If the counter reaches the value in the FRET field of the RGM_FRET register, MC_RGM asserts a destructive reset. 

The following figure shows the functional reset escalation counter. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/032_Reset_Generation_Module_-MC_RGM-/S32K3XXRM_数据表.pdf-1012-11.png)


<!-- Start of picture text -->
1<br>0<br>destructive reset<br>write to RGM_FRET 1 0<br>functional reset<br>functional reset event<br>count<br>destructive<br>=<br>reset event<br>RGM_FRET<br>register<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/032_Reset_Generation_Module_-MC_RGM-/S32K3XXRM_数据表.pdf-1012-12.png)


<!-- Start of picture text -->
Figure 137. Functional reset escalation counter<br><!-- End of picture text -->

~~<mark>NOTE</mark>~~ 

Functional counter increments for each reset source for which escalation is enabled. For details, see "Reset sources" table in the Reset chapter. 

### 32.7.9 Destructive reset escalation 

Destructive reset escalation can be used to keep the chip in the reset state until the power-on triggers a reset sequence if a number of destructive resets are occurred between software writes to the RGM_DRET register. This function is enabled by writing a non-zero value to the DRET field of this register. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1012 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 

After destructive reset escalation is enabled, MC_RGM increases a counter on each destructive reset that is enabled to increment the escalator. . This causes a reset sequence to be initiated (that is, entrance into DEST0 from the idle phase) or an ongoing reset sequence to restart (that is, entrance into DEST0 from any other reset phase). This counter is cleared on a write of any value to the RGM_DRET register and on any power-on reset. If the counter reaches the value in the DRET field of the RGM_DRET register, MC_RGM enters reset DEST0 and stays there until the next power-on reset occurs . 

The following figure shows the destructive reset escalation counter. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/032_Reset_Generation_Module_-MC_RGM-/S32K3XXRM_数据表.pdf-1013-04.png)


<!-- Start of picture text -->
1<br>0<br>power-on reset<br>write to RGM_DRET 1 0<br>destructive reset<br>destructive reset event<br>count<br>= stay in reset phase DEST0<br>RGM_DRET<br>register<br><!-- End of picture text -->

Figure 138. Destructive reset escalation counter 

~~<mark>NOTE</mark>~~ 

Desctructive counter increments for each reset source for which escalation is enabled. For details, see "Reset sources" table in the Reset chapter. 

## 32.8 MC_RGM register descriptions 

### 32.8.1 MC RGM Register Map memory map 

MC_RGM base address: 4028_C000h 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|0h|Destructive Event Status Register (DES)|32|W1C|0000_0001h|
|8h|Functional /External Reset Status Register (FES)|32|W1C|0000_0000h|
|Ch|Functional Event Reset Disable Register (FERD)|32|RWONC<br>E|0000_0000h|
|10h|Functional Bidirectional Reset Enable Register (FBRE)|32|RW|0000_0000h|
|14h|Functional Reset Escalation Counter Register (FREC)|32|W1C|0000_0000h|
|18h|Functional Reset Escalation Threshold Register (FRET)|32|RW|0000_000Fh|
|1Ch|Destructive Reset Escalation Threshold Register (DRET)|32|RW|0000_0000h|
|20h|External Reset Control Register (ERCTRL)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1013 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 

Table continued from the previous page... 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|24h|Reset During Standby Status Register (RDSS)|32|W1C|0000_0000h|
|28h|Functional Reset Entry Timeout Control Register (FRENTC)|32|RW|0000_0001h|



### 32.8.2 Destructive Event Status Register (DES) 

##### Offset 

|Register|Offset|
|---|---|
|DES|0h|



##### Function 

This register contains the status of the 'destructive' reset sources. It can be accessed in read/write in supervisor mode. It can be accessed in read-only in the user mode. Register bits are cleared on write '1'. This register is reset only on power-on reset. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|0|DEBU<br>G_D...|SW_<br>DEST|0|0|0|0|0|0|0|0|0|0|HSE_<br>SNV...|HSE_T<br>MP...|0|
|W||W1C|W1C|||||||||||W1C|W1C||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|SYS_<br>DIV...|HSE_<br>CLK...|0|AIPS_<br>PL...|0|CORE<br>_CL...|PLL_<br>LOL|FXOS<br>C_F...|0|MC_R<br>GM_...|0|STCU<br>_URF|FCCU<br>_FTR|0|0|F_<br>POR|
|W|W1C|W1C||W1C||W1C|W1C|W1C||W1C||W1C|W1C|||W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|



##### Fields 

|Field|Function|
|---|---|
|31|Reserved|
|—||
|30|Flag for 'Destructive' Reset DEBUG_DEST|
|DEBUG_DEST|0b - 'Destructive' reset event DEBUG_DEST has not occurred since either the last clear or the<br>last power-on reset assertion.|
||1b - 'Destructive' reset event DEBUG_DEST has occurred.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1014 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|29<br>SW_DEST|Flag for 'Destructive' Reset SW_DEST<br>0b - 'Destructive' reset event SW_DEST has not occurred since either the last clear or the last<br>power-on reset assertion.<br>1b - 'Destructive' reset event SW_DEST has occurred.|
|28|Reserved|
|—<br>27<br>—|Reserved|
|26<br>—|Reserved|
|25<br>—<br>24<br>—<br>23<br>—|Reserved<br>Reserved<br>Reserved|
|22<br>—|Reserved|
|21|Reserved|
|—<br>20<br>—|Reserved|
|19<br>—|Reserved|
|18<br>HSE_SNVS_RS<br>T|Flag for 'Destructive' Reset HSE_SNVS_RST<br>0b - 'Destructive' reset event HSE_SNVS_RST has not occurred since either the last clear or the<br>last power-on reset assertion.<br>1b - 'Destructive' reset event HSE_SNVS_RST has occurred.|
|17|Flag for 'Destructive' Reset HSE_TMPR_RST|
|HSE_TMPR_R<br>ST|0b - 'Destructive' reset event HSE_TMPR_RST has not occurred since either the last clear or the<br>last power-on reset assertion.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1015 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 

Table continued from the previous page... 

|Field|Function<br>1b - 'Destructive' reset event HSE_TMPR_RST has occurred.|
|---|---|
|16<br>—|Reserved|
|15<br>SYS_DIV_FAIL|Flag for 'Destructive' Reset SYS_DIV_FAIL<br>0b - 'Destructive' reset event SYS_DIV_FAIL has not occurred since either the last clear or the<br>last power-on reset assertion.<br>1b - 'Destructive' reset event SYS_DIV_FAIL has occurred.|
|14<br>HSE_CLK_FAIL|Flag for 'Destructive' Reset HSE_CLK_FAIL<br>0b - 'Destructive' reset event HSE_CLK_FAIL has not occurred since either the last clear or the<br>last power-on reset assertion.<br>1b - 'Destructive' reset event HSE_CLK_FAIL has occurred.|
|13<br>—<br>12<br>AIPS_PLAT_CL<br>K_FAIL|Reserved<br>Flag for 'Destructive' Reset AIPS_PLAT_CLK_FAIL<br>0b - 'Destructive' reset event AIPS_PLAT_CLK_FAIL has not occurred since either the last clear<br>or the last power-on reset assertion.<br>1b - 'Destructive' reset event AIPS_PLAT_CLK_FAIL has occurred.|
|11<br>—<br>10<br>CORE_CLK_FA<br>IL|Reserved<br>Flag for 'Destructive' Reset CORE_CLK_FAIL<br>0b - 'Destructive' reset event CORE_CLK_FAIL has not occurred since either the last clear or the<br>last power-on reset assertion.<br>1b - 'Destructive' reset event CORE_CLK_FAIL has occurred.|
|9<br>PLL_LOL|Flag for 'Destructive' Reset PLL_LOL<br>0b - 'Destructive' reset event PLL_LOL has not occurred since either the last clear or the last<br>power-on reset assertion.<br>1b - 'Destructive' reset event PLL_LOL has occurred.|
|8<br>FXOSC_FAIL|Flag for 'Destructive' Reset FXOSC_FAIL<br>0b - 'Destructive' reset event FXOSC_FAIL has not occurred since either the last clear or the last<br>power-on reset assertion.<br>1b - 'Destructive' reset event FXOSC_FAIL has occurred.|
|7<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1016 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|6|Flag for 'Destructive' Reset MC_RGM_FRE|
|MC_RGM_FRE|0b - 'Destructive' reset event MC_RGM_FRE has not occurred since either the last clear or the<br>last power-on reset assertion.<br>1b - 'Destructive' reset event MC_RGM_FRE has occurred.|
|5<br>—<br>4<br>STCU_URF|Reserved<br>Flag for 'Destructive' Reset STCU_URF<br>0b - 'Destructive' reset event STCU_URF has not occurred since either the last clear or the last<br>power-on reset assertion.<br>1b - 'Destructive' reset event STCU_URF has occurred.|
|3<br>FCCU_FTR|Flag for 'Destructive' Reset FCCU_FTR<br>0b - 'Destructive' reset event FCCU_FTR has not occurred since either the last clear or the last<br>power-on reset assertion.<br>1b - 'Destructive' reset event FCCU_FTR has occurred.|
|2<br>—<br>1<br>—<br>0<br>F_POR|Reserved<br>Reserved<br>Flag for power-on reset<br>All reset status in the FES and DES registers must be ignored at power up if this field is set.<br>~~NOTE~~<br>0b - No power-on event has occurred since the last clear.<br>1b - A power-on event has occurred.|



### 32.8.3 Functional /External Reset Status Register (FES) 

##### Offset 

|Register|Offset|
|---|---|
|FES|8h|



##### Function 

This register contains the status of the 'functional' and external reset sources. It can be accessed in read/write, either in supervisor mode. It can be accessed in read-only in the user mode. Register bits are cleared on write '1' if the triggering event has already been cleared at the source.This register is reset only on power-on reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1017 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 

###### ~~<mark>NOTE</mark>~~ 

The status of this register must be ignored if the fields of Destructive Event Status Register (DES) other than DES[F_POR] are set. In this case, a destructive reset had occurred while functional reset source was active. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|0|DEBU<br>G_F...|SW_<br>FUNC|0|0|0|0|0|0|0|0|HSE_<br>BOO...|0|0|0|HSE_<br>SWT...|
|W||W1C|W1C|||||||||W1C||||W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|0|0|0|PLL_<br>AUX|0|0|JTAG_<br>RST|SWT2<br>_RST|SWT1<br>_RST|SWT0<br>_RST|0|ST_<br>DONE|FCCU<br>_RST|0|0|F_EXR|
|W||||W1C|||W1C|W1C|W1C|W1C||W1C|W1C|||W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31<br>—|Reserved|
|30<br>DEBUG_FUNC|Flag for 'Functional' Reset DEBUG_FUNC<br>0b - 'Functional' reset event DEBUG_FUNC has not occurred since either the last clear or the last<br>power-on reset assertion.<br>1b - 'Functional' reset event DEBUG_FUNC has occurred.|
|29<br>SW_FUNC|Flag for 'Functional' Reset SW_FUNC<br>0b - 'Functional' reset event SW_FUNC has not occurred since either the last clear or the last<br>power-on reset assertion.<br>1b - 'Functional' reset event SW_FUNC has occurred.|
|28<br>—|Reserved|
|27<br>—|Reserved|
|26<br>—|Reserved|
|25<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1018 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|24<br>—|Reserved|
|23<br>|Reserved|
|—<br>22|Reserved|
|—<br>21|Reserved|
|—<br>20|Flag for 'Functional' Reset HSE_BOOT_RST|
|HSE_BOOT_R<br>ST|0b - 'Functional' reset event HSE_BOOT_RST has not occurred since either the last clear or the<br>last power-on reset assertion.<br>1b - 'Functional' reset event HSE_BOOT_RST has occurred.|
|19<br>—|Reserved|
|18<br>—<br>17<br>—<br>16<br>HSE_SWT_RS<br>T|Reserved<br>Reserved<br>Flag for 'Functional' Reset HSE_SWT_RST<br>0b - 'Functional' reset event HSE_SWT_RST has not occurred since either the last clear or the<br>last power-on reset assertion.<br>1b - 'Functional' reset event HSE_SWT_RST has occurred.|
|15<br>—|Reserved|
|14<br>—|Reserved|
|13<br>|Reserved|
|—<br>12<br>PLL_AUX|Flag for 'Functional' Reset PLL_AUX<br>0b - 'Functional' reset event PLL_AUX has not occurred since either the last clear or the last<br>power-on reset assertion.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1019 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 

Table continued from the previous page... 

|Field|Function<br>1b - 'Functional' reset event PLL_AUX has occurred.|
|---|---|
|11<br>—|Reserved|
|10<br>—|Reserved|
|9<br>JTAG_RST|Flag for 'Functional' Reset JTAG_RST<br>0b - 'Functional' reset event JTAG_RST has not occurred since either the last clear or the last<br>power-on reset assertion.<br>1b - 'Functional' reset event JTAG_RST has occurred.|
|8<br>SWT2_RST|Flag for 'Functional' Reset SWT2_RST<br>0b - 'Functional' reset event SWT2_RST has not occurred since either the last clear or the last<br>power-on reset assertion.<br>1b - 'Functional' reset event SWT2_RST has occurred.|
|7|Flag for 'Functional' Reset SWT1_RST|
|SWT1_RST|0b - 'Functional' reset event SWT1_RST has not occurred since either the last clear or the last<br>power-on reset assertion.<br>1b - 'Functional' reset event SWT1_RST has occurred.|
|6<br>SWT0_RST|Flag for 'Functional' Reset SWT0_RST<br>0b - 'Functional' reset event SWT0_RST has not occurred since either the last clear or the last<br>power-on reset assertion.<br>1b - 'Functional' reset event SWT0_RST has occurred.|
|5<br>—|Reserved|
|4<br>ST_DONE|Flag for 'Functional' Reset ST_DONE<br>0b - 'Functional' reset event ST_DONE has not occurred since either the last clear or the last<br>power-on reset assertion.<br>1b - 'Functional' reset event ST_DONE has occurred.|
|3|Flag for 'Functional' Reset FCCU_RST|
|FCCU_RST|0b - 'Functional' reset event FCCU_RST has not occurred since either the last clear or the last<br>power-on reset assertion.<br>1b - 'Functional' reset event FCCU_RST has occurred.|
|2<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1020 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|1|Reserved|
|—||
|0|Flag for External Reset|
|F_EXR|External reset is a source of destructive reset.|
||0b - No external reset event has occurred since either the last clear or the last power-on reset<br>assertion.|
||1b - An external reset event has occurred.|



### 32.8.4 Functional Event Reset Disable Register (FERD) 

##### Offset 

|Register|Offset|
|---|---|
|FERD|Ch|



##### Function 

This register provides dedicated fields to disable functional reset sources. When any of these reset sources are disabled, the associated functional event is demoted to trigger an interrupt request. The register can be read and written to in Supervisor mode and only read in User mode. Each byte can be written to only once after a destructive or power-on reset and this register is reset only on power-on and any destructive reset. 

~~<mark>NOTE</mark>~~ 

It is important to clear the Functional /External Reset Status Register (FES) before writing 1 to any of the fields in this register. Otherwise a interrupt request may occur. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/032_Reset_Generation_Module_-MC_RGM-/S32K3XXRM_数据表.pdf-1021-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>D_DE<br>W BUG...<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 0 0 0 0 0 0 0 0<br>D_JTA D_SW D_SW D_SW D_FC Reserv<br>W G_... T2_... T1_... T0_... CU_... ed<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1021 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 

##### Fields 

|Field<br>31<br>—|Function<br>Reserved|
|---|---|
|30<br>D_DEBUG_FU<br>NC|DEBUG_FUNC Disable Control<br>0b - Functional reset event DEBUG_FUNC triggers a reset sequence.<br>1b - Functional reset event DEBUG_FUNC generates an interrupt request.|
|29<br>—|Reserved|
|28<br>—|Reserved|
|27<br>—|Reserved|
|26<br>—|Reserved|
|25<br>—|Reserved|
|24<br>—|Reserved|
|23<br>—|Reserved|
|22<br>—|Reserved|
|21<br>—|Reserved|
|20<br>—|Reserved|
|19<br>—|Reserved|
|18<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1022 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 

Table continued from the previous page... 

|Field<br>17<br>—|Function<br>Reserved|
|---|---|
|16<br>—|Reserved|
|15<br>—|Reserved|
|14<br>—|Reserved|
|13<br>—|Reserved|
|12|Reserved|
|—<br>11<br>—|Reserved|
|10<br>—<br>9|Reserved<br>JTAG_RST Disable Control|
|D_JTAG_RST|0b - Functional reset event JTAG_RST triggers a reset sequence.<br>1b - Functional reset event JTAG_RST generates an interrupt request.|
|8|SWT2_RST Disable Control|
|D_SWT2_RST|0b - Functional reset event SWT2_RST triggers a reset sequence.<br>1b - Functional reset event SWT2_RST generates an interrupt request.|
|7|SWT1_RST Disable Control|
|D_SWT1_RST|0b - Functional reset event SWT1_RST triggers a reset sequence.<br>1b - Functional reset event SWT1_RST generates an interrupt request.|
|6|SWT0_RST Disable Control|
|D_SWT0_RST|0b - Functional reset event SWT0_RST triggers a reset sequence.<br>1b - Functional reset event SWT0_RST generates an interrupt request.|
|5<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1023 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|4|Reserved|
|—||
|3|FCCU_RST Disable Control|
|D_FCCU_RST|0b - Functional reset event FCCU_RST triggers a reset sequence.<br>1b - Functional reset event FCCU_RST generates an interrupt request.|
|2<br>—|Reserved|
|1|Reserved|
|—||
|0<br>—|Reserved|



### 32.8.5 Functional Bidirectional Reset Enable Register (FBRE) 

##### Offset 

|Register|Offset|
|---|---|
|FBRE|10h|



##### Function 

This register enables the generation of an external reset on 'functional' reset. It can be accessed in read/write, in supervisor mode. It can be accessed in read-only in user mode. This register is reset only on power-on and any 'destructive' reset. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/032_Reset_Generation_Module_-MC_RGM-/S32K3XXRM_数据表.pdf-1024-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>BE_D BE_S BE_H BE_H<br>R 0 0 0 0 0 0 0 0 0 0 0 0<br>EBU... W_F... SE_... SE_...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>BE_PL BE_JT BE_S BE_S BE_S BE_FC<br>R 0 0 0 0 0 0 0 0<br>L_... AG... WT2... WT1... WT0... BE_ST CU... Reserv<br>_D... ed<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1024 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 

##### Fields 

|Field<br>31<br>—|Function<br>Reserved|
|---|---|
|30|Bidirectional Reset Enables for 'Functional' Reset DEBUG_FUNC|
|BE_DEBUG_FU<br>NC|0b - External reset pin is asserted on a 'Functional' reset DEBUG_FUNC event if the reset is<br>enabled.<br>1b - External reset pin is not asserted on a 'functional' reset DEBUG_FUNC event.|
|29<br>BE_SW_FUNC|Bidirectional Reset Enables for 'Functional' Reset SW_FUNC<br>0b - External reset pin is asserted on a 'Functional' reset SW_FUNC event if the reset is enabled.<br>1b - External reset pin is not asserted on a 'functional' reset SW_FUNC event.|
|28<br>—|Reserved|
|27|Reserved|
|—<br>26<br>—|Reserved|
|25<br>—|Reserved|
|24|Reserved|
|—<br>23<br>—|Reserved|
|22|Reserved|
|—<br>21<br>—<br>20<br>BE_HSE_BOOT<br>_RST|Reserved<br>Bidirectional Reset Enables for 'Functional' Reset HSE_BOOT_RST<br>0b - External reset pin is asserted on a 'Functional' reset HSE_BOOT_RST event if the reset is<br>enabled.<br>1b - External reset pin is not asserted on a 'functional' reset HSE_BOOT_RST event.|
|19|Reserved<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1025 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|—<br>18<br>—|Reserved|
|17<br>—|Reserved|
|16|Bidirectional Reset Enables for 'Functional' Reset HSE_SWT_RST|
|BE_HSE_SWT_<br>RST|0b - External reset pin is asserted on a 'Functional' reset HSE_SWT_RST event if the reset is<br>enabled.<br>1b - External reset pin is not asserted on a 'functional' reset HSE_SWT_RST event.|
|15<br>—|Reserved|
|14<br>—|Reserved|
|13<br>—|Reserved|
|12<br>BE_PLL_AUX|Bidirectional Reset Enables for 'Functional' Reset PLL_AUX<br>0b - External reset pin is asserted on a 'Functional' reset PLL_AUX event if the reset is enabled.<br>1b - External reset pin is not asserted on a 'functional' reset PLL_AUX event.|
|11<br>—<br>10<br>—|Reserved<br>Reserved|
|9|Bidirectional Reset Enables for 'Functional' Reset JTAG_RST|
|BE_JTAG_RST|0b - External reset pin is asserted on a 'Functional' reset JTAG_RST event if the reset is enabled.<br>1b - External reset pin is not asserted on a 'functional' reset JTAG_RST event.|
|8|Bidirectional Reset Enables for 'Functional' Reset SWT2_RST|
|BE_SWT2_RST|0b - External reset pin is asserted on a 'Functional' reset SWT2_RST event if the reset is enabled.<br>1b - External reset pin is not asserted on a 'functional' reset SWT2_RST event.|
|7|Bidirectional Reset Enables for 'Functional' Reset SWT1_RST|
|BE_SWT1_RST|0b - External reset pin is asserted on a 'Functional' reset SWT1_RST event if the reset is enabled.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1026 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - External reset pin is not asserted on a 'functional' reset SWT1_RST event.|
|6<br>BE_SWT0_RST|Bidirectional Reset Enables for 'Functional' Reset SWT0_RST<br>0b - External reset pin is asserted on a 'Functional' reset SWT0_RST event if the reset is enabled.<br>1b - External reset pin is not asserted on a 'functional' reset SWT0_RST event.|
|5<br>—<br>4<br>BE_ST_DONE|Reserved<br>Bidirectional Reset Enables for 'Functional' Reset ST_DONE<br>0b - External reset pin is asserted on a 'Functional' reset ST_DONE event if the reset is enabled.<br>1b - External reset pin is not asserted on a 'functional' reset ST_DONE event.|
|3<br>BE_FCCU_RST|Bidirectional Reset Enables for 'Functional' Reset FCCU_RST<br>0b - External reset pin is asserted on a 'Functional' reset FCCU_RST event if the reset is enabled.<br>1b - External reset pin is not asserted on a 'functional' reset FCCU_RST event.|
|2<br>—|Reserved|
|1<br>—|Reserved|
|0<br>—|Reserved|



### 32.8.6 Functional Reset Escalation Counter Register (FREC) 

##### Offset 

|Register|Offset|
|---|---|
|FREC|14h|



##### Function 

This register provides the current count of functional reset escalation counter. It can be accessed in read/write, either in supervisor mode. It can be accessed in read in the user mode. This register is reset only on power-on reset or destructive reset. This register is also reset when you reconfigure the FREC field to Fh. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1027 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/032_Reset_Generation_Module_-MC_RGM-/S32K3XXRM_数据表.pdf-1028-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 FREC<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-4<br>—|Reserved|
|3-0|Functional' Reset Escalation Counter|
|FREC|This bit field provides the value of functional reset escalation counter.|



### 32.8.7 Functional Reset Escalation Threshold Register (FRET) 

##### Offset 

|Register|Offset|
|---|---|
|FRET|18h|



##### Function 

This register sets the threshold for 'functional' reset escalation to a 'destructive' reset. It can be accessed in read/write, either in supervisor mode. It can be accessed in read-only in the user mode. Writing a non-zero value to the FRET field enables the 'functional' reset escalation function. Writing any value to this register resets the 'functional' reset counter. See Functional reset escalation for details on the 'functional' reset escalation function. This register is reset only on power-on and any 'destructive' reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1028 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/032_Reset_Generation_Module_-MC_RGM-/S32K3XXRM_数据表.pdf-1029-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>FRET<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-4|Reserved|
|—||
|3-0|'Functional' Reset Escalation Threshold|
|FRET|If the value of this field is 0, the 'functional' reset escalation function is disabled. Any other value is<br>the number of 'functional' resets that causes a 'destructive' reset if the FRET register isn't written to<br>beforehand.|



### 32.8.8 Destructive Reset Escalation Threshold Register (DRET) 

##### Offset 

|Register|Offset|
|---|---|
|DRET|1Ch|



##### Function 

This register sets the threshold for 'destructive' reset escalation to keeping the chip in the reset state until the next power-on reset triggers a new reset sequence. It can be accessed in read/write, either in supervisor mode. It can be accessed in read-only in the user mode. Writing a non-zero value to the DRET field enables the 'destructive' reset escalation function. Writing any value to this register resets the 'destructive' reset counter. See Destructive reset escalation for details on the 'destructive' reset escalation function. This register is reset only on power-on reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1029 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/032_Reset_Generation_Module_-MC_RGM-/S32K3XXRM_数据表.pdf-1030-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>DRET<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-4|Reserved|
|—||
|3-0|'Destructive' Reset Escalation Threshold|
|DRET|If the value of this field is 0, the 'destructive' reset escalation function is disabled. Any other value is<br>the number of 'destructive' resets which keeps the chip in the reset state until the next power-on reset<br>triggers a new reset sequence if the DRET register isn't written to beforehand.|



### 32.8.9 External Reset Control Register (ERCTRL) 

##### Offset 

|Register|Offset|
|---|---|
|ERCTRL|20h|



##### Function 

This register allows software to control the assertion of External reset pin. It can be accessed in read/write, in supervisor mode. It can be accessed in read-only in the user mode. This register is reset on all resets. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1030 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0||||||||ERAS|
|W||||||||||||||||SERT|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-1|Reserved|
|—||
|0|ERASSERT|
|ERASSERT|Setting ERASSERT to 1b also safe states most of the chip's pins. See the IOMUX table for<br>each pin's safe state value. Software must use the ERASSERT bit for this purpose only as<br>part of the main reset domain self-test entry procedure. Using it at any other time may result<br>in unpredictable system behavior.<br>~~NOTE~~|
||0b - No change|
||1b - External reset is asserted|



### 32.8.10 Reset During Standby Status Register (RDSS) 

##### Offset 

|Register|Offset|
|---|---|
|RDSS|24h|



##### Function 

This register provides status of whether a reset event occurred during standby mode. Register bits are cleared on write '1'. This register is reset only on power-on reset. 

|~~NOTE~~|
|---|



On exiting a reset sequence after standby exit, the software must perform a read operation on MC_ME[PREV_MODE] and RDSS register. If any bit of the RDSS register is set, the software must ignore the status reported by MC_ME[PREV_MODE] register otherwise the status of MC_ME[PREV_MODE] register reports the device status. 

If MC_ME indicates last mode as RESET, then perform a reset exit in software else a standby exit. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1031 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/032_Reset_Generation_Module_-MC_RGM-/S32K3XXRM_数据表.pdf-1032-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>FES_ DES_<br>R 0<br>RES  RES<br>W W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-2|Reserved|
|—||
|1|FES_RES|
|FES_RES|0b - No functional reset event occurred during standby mode.|
||1b - Functional reset event occurred during standby mode.|
|0|DES_RES|
|DES_RES|0b - No destructive reset event occurred during standby mode.|
||1b - Destructive reset event occurred during standby mode.|



### 32.8.11 Functional Reset Entry Timeout Control Register (FRENTC) 

##### Offset 

|Register|Offset|
|---|---|
|FRENTC|28h|



##### Function 

This register provides control for functional reset entry timeout counter. This register is reset on power-on and destructive reset events. This is a word accessible register. Byte accesses are not allowed on this register. 

~~<mark>NOTE</mark>~~ This field should be set a value greater than one. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1032 / 4640 

NXP Semiconductors 

Reset Generation Module (MC_RGM) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/032_Reset_Generation_Module_-MC_RGM-/S32K3XXRM_数据表.pdf-1033-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>FRET_TIMEOUT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R FRET_<br>FRET_TIMEOUT<br>W EN<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-1|Functional Reset Entry Timer Value|
|FRET_TIMEOU<br>T|This field allows to override the timeout duration of the functional reset entry timer. The counter value is<br>in terms of the Fast IRC clock cycles (typical clock frequency of 48 MHz). A non zero value of this field<br>would indicate the timer value to be used during the functional reset entry sequence.|
|0|Functional Reset Entry Timer Enable/Disable|
|FRET_EN|0b - Functional reset entry timer is disabled.|
||1b - Functional reset entry timer is enabled|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1033 / 4640 

