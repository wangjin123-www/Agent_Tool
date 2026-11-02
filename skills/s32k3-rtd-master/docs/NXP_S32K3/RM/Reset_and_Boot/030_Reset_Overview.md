NXP Semiconductors 

# Chapter 30 Reset Overview 

## 30.1 Introduction 

This chip's reset logic consists of a reset sequence that leads the chip to a fixed deterministic state after predefined reset events occur. These events can pertain to chip failure events, the chip's special operating conditions, or certain software-governed events to initiate a chip reset sequence. This chapter discusses the chip reset scheme and related topics such as: 

- Types of reset reactions 

- Reset event sources 

- Chip reset sequences 

   - POR 

   - Destructive reset 

   - Functional reset 

- RAM retention across functional reset 

- Reset pin (RESET_b) behavior 

- Debug system reset 

- Signal-level reset flow 

## 30.2 Chip reset types and reactions 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

954 / 4640 

NXP Semiconductors 

Reset Overview 

### 30.2.1 Chip reset blocks 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/030_Reset_Overview/S32K3XXRM_数据表.pdf-0955-03.png)


<!-- Start of picture text -->
PMC<br>FIRC<br>MC_RGM<br>RESET_b MDM_AP<br>MC_PCU SWT_0<br>SWT_1<br>MC_CGM Not present in S32K312<br>and S32K311.<br>SWT_2<br>MC_ME Present in S32K358<br>JTAGC CMU_FC_[3:5]<br>STCU2 CMU_FC_0<br>PLL<br>PLL_AUX<br>Present in S32K358<br>FCCU FOSU HSE_B<br><!-- End of picture text -->


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/030_Reset_Overview/S32K3XXRM_数据表.pdf-0955-04.png)


<!-- Start of picture text -->
Figure 115. Chip reset blocks<br><!-- End of picture text -->

### 30.2.2 Chip reset types 

Table 153. Chip reset types 

|Reset event type|Functional description|
|---|---|
|POR|Leads to a complete chip reset.|
|Destructive|Leads most parts of the chip, except a few modules, to reset. SRAM content is lost after this<br>reset event.|
|Functional|Leads all the communication peripherals and cores to reset. The communication protocols' sanity<br>is not guaranteed and they are assumed to be reinitialized after reset. The SRAM content, and<br>the functionality of certain modules, is preserved across functional reset.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

955 / 4640 

NXP Semiconductors 

Reset Overview 

### 30.2.3 High-level reset sequence overview 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/030_Reset_Overview/S32K3XXRM_数据表.pdf-0956-03.png)


<!-- Start of picture text -->
Functional reset event Functional reset Functional reset Functional reset Chip out of reset<br>entry sequence asserts exit sequence in Normal Run mode<br>Destructive reset<br>Destructive reset event<br>sequence<br>Power-on reset event<br>Power-on reset In case of Standby mode, only the Run domain resets<br>Standby entry sequence sequence and the exit from POR happens on Standby mode exit.<br><!-- End of picture text -->

Figure 116. High-level reset sequence overview 

#### 30.2.3.1 Reset event reactions 

Table 154. Reset event reactions 

|Reset event type|Triggered from|Reaction|
|---|---|---|
|POR|Anywhere|Moves to the beginning of the power-on sequence|
||Power-on sequence|No reset sequence change|
|Destructive reset|Anywhere in the chip operation except in<br>the power-on-sequence|Moves to the beginning of the destructive reset sequence|
||Out-of-reset|Moves to the beginning of the functional reset entry<br>sequence|
|Functional reset|||
||Anywhere within the functional reset<br>sequence|No reset sequence change|



#### 30.2.3.2 Chip action after reset event 

For each reset event, immediately after MC_RGM captures it, the chip performs these actions: 

1. Writes 1 to the corresponding reset event status fields in MC_RGM.DES and MC_RGM.FES (see the MC_RGM chapter for more information). 

2. Places its pins in their default states (see the IOMUX file attached to this document for more information). 

3. Asserts the RESET_b pin. 

~~<mark>NOTE</mark>~~ 

After self-test completes, you can configure RESET_b assertion using MC_RGM.FES[ST_DONE]. 

4. Enters the reset sequence as described in Reset event reactions, depending on the current state and reset event type. 

## 30.3 Reset sources—POR, destructive, and functional 

MC_RGM records reset events in MC_RGM.FES and MC_RGM.DES, indicating the source of functional reset events and destructive reset events, respectively. You must read these fields to identify the reset source on reset recovery. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

956 / 4640 

NXP Semiconductors 

Reset Overview 

### 30.3.1 POR sources 

Table 155. POR sources 

|Source module|Field in MC_RGM.DES|RESET_b assertion<br>Description|
|---|---|---|
|||VDD_LV POR|
|||LVR on 1.1 V supply in Standby mode|
|||LVR on 1.1 V supply in Run mode|
|||LVR on 2.5 V supply in Standby mode|
|PMC||LVR on 2.5 V supply in Run mode|
||F_POR|Always<br>LVR on VDD_HV_A supply in Standby mode|
|||LVR on VDD_HV_A supply in Run mode|
|||LVR on VDD_HV_B supply in Standby mode<sup>1</sup>|
|||LVR on VDD_HV_B supply in Run mode<sup>1</sup>|
|POR_WDG||POR_WDG timeout (see the POR_WDG chapter<br>for more information)|



1. LVR on VDD_HV_B run mode and LVR on VDD_HV_B standby mode are not present in S32K312 and S32K311. 

~~<mark>NOTE</mark>~~ 

You cannot escalate or demote POR to an interrupt. 

### 30.3.2 Stages of the POR sequence 

Table 156. Stages of the POR sequence 

|Stage|Process|
|---|---|
|PWRUP|1. Starts after a POR event (for example, a POR source assert).|
||2. Waits for the power-up sequence to complete.|
||3. Exits when all the POR sources clear.<br>4. Transitions to the FIRC_STRT stage after the procedure completes.|
|FIRC_STRT|1. Enters this stage after exiting the PWRUP stage.|
||FIRC_CLK, if enabled, becomes available after it is stable. The duration<br>depends on the clock startup time (see the chip datasheet for more<br>information). The MC_RGM state machine proceeds further after<br>FIRC_CLK is available.<br>~~NOTE~~|
||2. Transitions to the destructive reset sequence after the procedure completes.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

957 / 4640 

NXP Semiconductors 

Reset Overview 

### 30.3.3 Destructive reset sources 

Table 157. Destructive reset sources 

|Source module<sup>1</sup>|Field in MC_RGM.DES|Description|
|---|---|---|
|FOSU|FCCU_FTR|FCCU failure to react|
|STCU2|STCU_URF|STCU2 unrecoverable fault|
|MC_RGM|MC_RGM_FRE|Functional reset escalation|
|CMU_FC_0|FXOSC_FAIL|FXOSC failure|
|PLL|PLL_LOL|PLL loss of lock|
|CMU_FC_3|CORE_CLK_FAIL|Core clock failure|
|CMU_FC_4|AIPS_PLAT_CLK_FAIL|AIPS_PLAT_CLK failure|
|CMU_FC_5|HSE_CLK_FAIL|HSE_CLK failure|
|MC_CGM|SYS_DIV_FAIL|System clock dividers alignment failure|
|HSE_B|HSE_TMPR_R ST|HSE_B tamper detect reset|
|HSE_B|HSE_SNVS_RST|HSE_B SNVS tamper detection|
|MC_ME|SW_DEST|Software destructive reset|
|MDM_AP|DEBUG_DEST|Debug destructive reset|
|RESET_b pin|EXT_RST|RESET_b pin assertion|



1. All destructive resets can be escalated, but only the PLL LOL destructive reset can be demoted to an interrupt (see Destructive reset event bypass for PLL LOL destructive reset bypass details). 

~~<mark>NOTE</mark>~~ 

All reset sources in the table above assert the RESET_b pin. 

### 30.3.4 Destructive sequence stage description 

Table 158. DEST0 description 

|Stage|Process|
|---|---|
|DEST0|1. Asserts reset to the entire chip, except logic running on POR.|
||2. Waits for all the destructive reset events to clear.|
||3. Waits for the minimum destructive reset assertion duration of eight FIRC_CLK cycles.|
||4. Deassets after stage completion.|



### 30.3.5 Functional reset sources 

Table 159. Functional reset sources 

|Source module|Field in|RESET_b assertion|Demotable to IRQ<sup>1</sup>|Escalation<sup>2</sup>|Description|
|---|---|---|---|---|---|
||MC_RGM.FES|||||
|FCCU soft<br>reaction<sup>3</sup>|FCCU_RST|Always|Yes<sup>4</sup>|Yes|FCCU reset<br>reaction|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

958 / 4640 

NXP Semiconductors 

Reset Overview 

Table 159. Functional reset sources (continued) 

|Source module|Field in<br>MC_RGM.FES|RESET_b assertion|Demotable to IRQ<sup>1</sup>|Escalation<sup>2</sup>|Description|
|---|---|---|---|---|---|
|STCU2|ST_DONE|Configurable|No|No|Self-test done|
|SWT_0|SWT0_RST|Always|Yes<sup>5</sup>|Yes|SWT reset request|
|SWT_1<sup>6</sup>|SWT1_RST|Always|Yes<sup>7</sup>|Yes|SWT reset request|
|SWT_2<sup>8</sup>|SWT2_RST|Always|Yes<sup>9</sup>|Yes|SWT reset request|
|PLL_AUX<sup>10</sup>|PLL_AUX_RST<sup>11</sup>|Always|Yes<sup>12</sup>|Yes|PLL reset request|
|JTAGC|JTAG_RST|Always|Yes<sup>13</sup>|No|JTAG reset|
|HSE_B|HSE_SWT_RST|Always|No|Yes|HSE_B SWT<br>timeout|
|HSE_B|HSE_BOOT_RST|Always|No|Yes|HSE_B boot reset|
|MC_ME|SW_FUNC|Always|No|Yes|Software<br>functional reset|
|MDM_AP|DEBUG_FUNC|Always|Yes<sup>14</sup>|Yes|Debug functional<br>reset|



1. See Functional reset demotion to an interrupt for more information. 

2. See Reset escalation for more information. 

3. An FCCU soft functional reset is a chip functional reset (see the FCCU chapter for more information). 

4. Controlled by MC_RGM.FERD[D_FCCU_RST]. 

5. Controlled by MC_RGM.FERD[D_SWT0_RST]. 

6. SWT_1 is not present in S32K312 and S32K311. 

7. Controlled by MC_RGM.FERD[D_SWT1_RST]. 

8. SWT_2 is only present in S32K358. 

9. Controlled by MC_RGM.FERD[D_SWT2_RST] 

10. PLL_AUX is only present in S32K358. 

11. In order to use PLL_Aux as functional reset /interrupt source, the 24th bit of Functional Reset Register (DCMRWF2) should be configured. 

12. Controlled by MC_RGM.FERD[D_PLL_AUX_RST] 

13. Controlled by MC_RGM.FERD[D_JTAG_RST]. 

14. Controlled by MC_RGM.FERD[D_DEBUG_FUNC]. 

### 30.3.6 Functional reset sequence descriptions 

Table 160. Functional reset sequence descriptions 

|Stage|Series of events|
|---|---|
||Functional reset entry sequences|
|FUNC0|This stage starts after any functional reset event.|
||The FCCU fault monitoring and CMU_Fx_n monitoring for FLL events is masked in this step to avoid any<br>false fault or reset.|
|FUNC1|In this stage, a halt sequence that includes daisy chaining of all the gaskets halts, disabling the crossbar.|
||The stage completes after the halt-handshake sequence completes.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

959 / 4640 

NXP Semiconductors 

Reset Overview 

Table 160. Functional reset sequence descriptions (continued) 

|Stage|Series of events|
|---|---|
|FUNC2|In this stage, MC_RGM triggers the MC_CGM hardware clock multiplexers to switch to FIRC_CLK.<br>• Software-based clock multiplexers do not support switching to FIRC_CLK on functional reset.<br>• If PCFS is enabled, the system clock switching can be done via PCFS.<br>This stage completes after MC_CGM switches the system clock to FIRC.|
|FUNC3|In this stage, MC_RGM triggers all the MC_CGM hardware-based clock multiplexers with PCFS enabled<br>or disabled to move their dividers to default values.<br>• Software-based clock multiplexers do not support this feature.<br>This stage completes after all the clock multiplexer dividers initialize to their corresponding default values.|
|FUNC4|In this stage, PLLDIG turns off synchronously.<br>The stage completes after PLLDIG turns off.|
|FUNC5|FXOSC_CLK switches off synchronously.<br>The FUNC4 and FUNC5 stages ensure that PLLDIG disables cleanly to ensure there are no glitches on<br>the PLLDIG clock because of reset.<br>The stage completes after FXOSC switches off.|
|FUNC6|In this stage, clocks of modules that are a part of LBIST and working on the destructive reset are enabled to<br>meet their synchronous reset requirements, if any. For the self-test logic, in self-test, the destructive reset<br>deasserts after this stage completes and after safe stating is removed.<br>In the self-test sequence, the logic, which is a part of self-test (LBIST logic) resets when<br>self-test completes. All the parts of logic in self-test (POR, destructive, and functional<br>reset) reset after self-test completes whereas the rest of the chip undergoes a functional<br>reset sequence because of self-test completion (MC_RGM.FES[ST_DONE] = 1). See the<br>Safety Overviewand STCU2 chapters for more information on the self-test operation.<br>~~NOTE~~|
|FUNC7|MC_RGM asserts the functional reset and triggers a counter running on FIRC_CLK (for up to 64 cycles)<br>to enable clocks for the modules having synchronous reset requirements.<br>Flash memory comes out of reset after this stage completes.<br>The flash memory resets after a functional reset event but comes out of reset, before the<br>rest of the modules do, at the start of the functional reset exit sequence. The rest of the<br>modules reset when the functional reset comes out of reset at the end of the functional<br>reset exit sequence. Therefore, the reset to flash memory is an early functional reset that<br>deasserts earlier than the functional reset, even if asserted at the same time.<br>~~NOTE~~|
||Functional reset exit sequences|
|FUNC8|This stage consists of flash memory and MC_RGM handshaking.<br>Flash memory indicates the completion of its initialization to MC_RGM.|
|FUNC9|DCM initiates the scanning of flash memoryDCFrecords.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

960 / 4640 

NXP Semiconductors 

Reset Overview 

Table 160. Functional reset sequence descriptions (continued) 

|Stage|Series of events|
|---|---|
||This state completes after the flash memory scanning completes. See the DCF clients file attached to this<br>document for more information.|
|FUNC10|After DCM scans the DCF records from the flash memory, DCM initiates the trim loading sequence for<br>analog blocks.<br>The analog blocks are loaded with the configured trimmed values in this stage, which completes after a<br>trim-loading sequence completes.|
|FUNC11|In this stage, MG_RGM stops driving RESET_b and checks that the signal does not assert externally.<br>If you enable low-power debug, MC_RGM waits for a debug acknowledge.<br>The completion of this stage indicates that MC_RGM completed the reset sequence, deasserting the<br>functional reset to the system.|



## 30.4 Reset and boot sequence 

The chip reset sequence consists of several reset stages based on the occurrence of a particular reset event. All reset events follow the same chip reset sequence; only the entry points vary depending on the type of reset event. MC_RGM triggers each stage after the previous stage completes. These stages execute in a specific order, which ensures a deterministic state of the chip when a reset event completes. 

Figure 117 shows a high-level representation of the chip startup sequence. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

961 / 4640 

NXP Semiconductors 

Reset Overview 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/030_Reset_Overview/S32K3XXRM_数据表.pdf-0962-02.png)


<!-- Start of picture text -->
Chip power up<br>Keep chip in POR<br>No<br>Power-on reset V>VtPOR<br>Yes<br>FIRC powers on<br>Wait for FIRC stabilization<br>Destructive reset Destructive reset<br>sequence proceeds<br>Functional reset Flash memory initialization<br>Functional reset Flash memory scanning<br>sequence proceeds Trim loading<br>Chip out of reset in normal Run mode<br>Standby Yes Security functions disabled<br>exit<br>No Security functions enabled<br>Change FIRC_DIV to DIV1<br>sBAF initialization code Enable FXOSC, PLLDIG (configurable)<br>Boot header parsing<br>XRDC configurations<br>CAAM_RNG initialization<br>Debug authorization<br>Change MC_RGM.DRET to 0xF if it's '0'<br>HSE_FW verification<br>CAAM_RNG initialization<br>Secure Yes OS initialization<br>HSE_FW boot<br>RUN boot? HSE_FW initialization code<br>Application boot<br>No<br>Standby recovery initialization<br>App core VTOR change<br>sBAF enabling application core<br>HSE_FW enabling application core<br>Trigger Yes<br>self-test? Execute self-test Legend:<br>No Hardware HSE_B sBAF<br>Application core<br>Move to application HSE_B firmware  software<br>Note: HSE_FW and application sizes are considered as 128 KB each<br>Figure 117. Chip reset and boot overview<br><!-- End of picture text -->

### 30.4.1 POR 

This stage starts when the POR event occurs, that is, when a POR source asserts. The logic within the Run power domain running on POR also resets in the chip Standby entry sequence. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

962 / 4640 

NXP Semiconductors 

Reset Overview 

~~<mark>NOTE</mark>~~ 

The logic in the Standby power domain does not reset in the chip Standby mode entry sequence. 

The POR sequence consist of two stages: 

1. Power-up (PWRUP) 

2. FIRC oscillator start (FIRC_STRT) 

See POR sequence for more information and Stages of the POR sequence for POR stages and their descriptions. 

#### 30.4.1.1 POR sequence 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/030_Reset_Overview/S32K3XXRM_数据表.pdf-0963-09.png)


<!-- Start of picture text -->
Power-on reset event<br>PWRUP<br>Assert reset to all domains.<br>Wait for complete power-up.<br>All POR<br>events<br>No<br>clear?<br>Yes<br>FIRC_STRT<br>Deassert POR and enable FIRC.<br>FIRC_CLK<br>stable? No<br>Yes<br>Destructive reset<br>sequence<br><!-- End of picture text -->

Figure 118. POR flow 

### 30.4.2 Destructive reset 

The chip enters a destructive reset sequence after the POR sequence or any destructive reset event completes. Destructive reset sequence illustrates the destructive reset sequence and Destructive sequence stage description discusses the stages of destructive sequence. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

963 / 4640 

NXP Semiconductors 

Reset Overview 

#### 30.4.2.1 Destructive reset sequence 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/030_Reset_Overview/S32K3XXRM_数据表.pdf-0964-03.png)


<!-- Start of picture text -->
Destructive reset event POR sequence Standby reset<br>sequence<br>In case of Standby mode, only the Run<br>domain resets and the exit from POR<br>happens on Standby mode exit.<br>DEST0<br>Assert reset all domains except POR and debug.<br>Wait for all destructive events to clear.<br>Wait for minimum destructive reset assertion duration.<br>All destructive reset events clear.<br>Minimum destructive reset assertion duration expires.<br>Destructive reset escalation threshold not exceeded.<br>Functional reset<br>sequence<br>Figure 119. Destructive reset sequence<br><!-- End of picture text -->

#### 30.4.2.1.1 Destructive sequence stage description 

Table 161. DEST0 description 

|Stage|Process|
|---|---|
|DEST0|1. Asserts reset to the entire chip, except logic running on POR.|
||2. Waits for all the destructive reset events to clear.|
||3. Waits for the minimum destructive reset assertion duration of eight FIRC_CLK cycles.|
||4. Deassets after stage completion.|



#### 30.4.2.2 Destructive reset event bypass 

This chip supports a destructive reset event demotion mechanism that the application software configures. The destructive reset bypasses and an interrupt event occurs (demotion). Table 162 discusses details related to GPR configuration and corresponding interrupt identification. 

A successful chip operation is not guranteed if a destructive reset event is bypassed. 

Table 162. Destructive reset event bypass 

|Destructive reset event|Destructive reset event<br>description|DCM field to bypass reset event|NVIC interrupt<br>ID|
|---|---|---|---|
|MC_RGM.DES[PLL_LOL]|PLL loss of lock|DCM.DCMRWP3[9]|212|



### 30.4.3 Functional reset 

The chip enters the functional reset sequence when any of the following events occur: 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

964 / 4640 

NXP Semiconductors 

Reset Overview 

- Functional reset 

- POR or destructive reset (after the DEST0 stage completion) 

On any functional reset event, the chip starts a functional reset entry sequence before the functional reset asserts and ensures the stability of logic running on a destructive reset and POR. On a destructive reset event or POR events the functional reset entry sequence does not execute. 

The functional reset exit sequence consists of steps that ensure proper initialization of the chip after functional reset recovery. 

#### 30.4.3.1 Functional reset sequence 

Functional reset flow illustrates the functional reset flow and Functional reset sequence descriptions discusses the functional reset stages and their descriptions. 

Stages FUNC0 to FUNC6 present the functional reset entry sequence. It occurs on any functional reset event before the functional reset. In other words, when a functional reset event occurs, MC_RGM holds the asserted reset and executes the functional reset entry sequence. After the sequence completes, MC_RGM resets the chip, which remains in Run mode during the functional reset entry sequence. 

Stages FUNC7 to FUNC11 present the functional reset exit sequence, which occurs after a functional reset event before deasserting the chip reset. This includes handshaking with the flash memory and analog blocks, ensuring correct operation after reset exit. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

965 / 4640 

NXP Semiconductors 

Reset Overview 

#### 30.4.3.1.1 Functional reset flow 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/030_Reset_Overview/S32K3XXRM_数据表.pdf-0966-03.png)


<!-- Start of picture text -->
Destructive<br>Functional reset<br>reset event<br>event<br>or sequence<br>FUNC0<br>Disable safety features<br>FUNC7<br>Assert functional reset<br>Revive system clock<br>FUNC1 Wait for 64 FIRC cycles<br>Initiate crossbar disable<br>Minimum functional reset duration completed<br>Crossbar disable process completed FUNC8<br>Initiate flash memory reset<br>FUNC2<br>recovery handshake<br>Initiate PCFS<br>Switch clock to FIRC Flash memory reset recovery process completed<br>Clock switching to FIRC completed FUNC9<br>Initiate flash memory<br>FUNC3<br>scanning by DCM<br>Initiate default clock configuration<br>Flash memory scanning completed<br>Default clock configurations completed<br>FUNC10<br>FUNC4<br>Iintiate trim loading<br>Disable PLL of analog modules<br>PLL disabled Trim loading of analog modules completed<br>FUNC5 FUNC11<br>Disable FXOSC Stop driving RESET_b and<br>wait for debug acknowledge if<br>FXOSC disabled LP_DEBUG is enabled<br>FUNC6 RESET_b pin deasserted<br>Debug acknowledge done for LP_DEBUG if enabled<br>Initiate sync reset clocks<br>Out<br>of<br>reset<br>Figure 120. Functional reset flow<br><!-- End of picture text -->

#### 30.4.3.2 FUNC9 and FUNC10 stage bypass for faster Standby mode exit 

The chip supports optional bypassing of the FUNC9 and FUNC10 (only FIRC and PMC phases) stages on Standby mode exit to considerably reduce the Standby mode exit duration. This feature is recommended only for Standby mode exit and must be configured on: 

- Standby mode entry sequence 

- SW3 

- Disabled on Standby mode exit 

See the "Faster Standby recovery" section in the "Power Management" chapter for more information. 

#### 30.4.3.3 Standby reset sequence 

The logic within Run domain is reset additionally apart from the reset sequence in the chip standby entry sequence, wherein all the resets assert (POR, destructive, and functional) to the Run domain logic. The chip standby entry sequence does not have any impact on the logic in Standby power domain. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

966 / 4640 

NXP Semiconductors 

Reset Overview 

Wake-up from Standby mode removes the resets to the Run domain in the standby entry sequence. 

See the "Peripheral reset status" section in the "Reset Overview" chapter for the logic present in Run domain. 

#### 30.4.3.4 Reset function redirection 

Resets may escalate or demote to an IRQ, depending on the chip configuration. 

#### 30.4.3.4.1 Functional reset demotion to an interrupt 

This chip supports the reset sequence demotion feature for functional resets. You can configure a functional reset to create an interrupt instead of a reset (see the MC_RGM chapter for details). 

#### 30.4.3.4.2 Reset escalation 

The chip supports the reset escalation feature. If multiple functional or destructive resets occur, the related reset can escalate to a higher priority reset sequence (see the "Functional reset escalation" and "Destructive reset escalation" sections in the MC_RGM chapter). 

#### 30.4.3.4.2.1 Destructive reset escalation 

You can enable destructive reset escalation by configuring a DCF client. You must also configure the destructive count threshold in MC_RGM.DRET (see "Destructive Reset Escalation Enable Register (DEST_RST_ESC):dcf_client_dest_rst_esc" in the DCF file attached to this document). The escalation event can individually be enabled or disabled for each reset source, and the fields in the dcf_client_dest_rst_esc register correspond with the fields in MC_RGM.DES register. 

After being configured, MC_RGM immediately asserts a destructive reset escalation when the destructive event count reaches the threshold count in MC_RGM.DRET[DRET]. When the destructive and escalation reset assert, the reset sequence immediately enters the DEST0 state. The reset sequencing remains in DEST0 until a POR event occurs. If enabled, the destructive reset escalation counter increments with each destructive reset event. The application software clears the destructive reset escalation counter by writing any value to MC_RGM.DRET[DRET]. 

~~<mark>NOTE</mark>~~ 

You can configure GPR settings to allow demotion of destructive resets to interrupts instead of escalation (DCMRWP3[DEST_RST9_AS_IPI]). See Destructive reset event bypass for more information. 

## 30.5 Reset timing diagram 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/030_Reset_Overview/S32K3XXRM_数据表.pdf-0967-16.png)


<!-- Start of picture text -->
Power-on reset (active-low) b<br>FIRC startup and setting time<br>FIRC_CLK b i FIRC trimming j<br>≈ 20 FIRC cycles<br>Destructive reset (active low) c<br>Flash memory reset (active-low) ≈ 64 FIRC cycles d<br>Flash memory reset recovery time < 15 µs<br>Flash memory reset recovery done e Analog modules (for example, FIRC) trimming<br>Flash memory scanning start f Trimming done<br>Flash memory scanning time ≈ 10 µs<br>Flash memory scanning complete g<br>Start trim loading<br>FIRC, PMC, ADC, TempSense, and so on h<br>Trim loading done k<br>Reset pin goes high<br>RESET_b l<br>Chip out of reset in Run mode<br>Functional reset (active-low) m<br><!-- End of picture text -->

Figure 121. Reset timing diagram 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

967 / 4640 

NXP Semiconductors 

Reset Overview 

## 30.6 Chip status after reset deassertion 

Table 163. Chip status after reset deassertion 

|Function or feature|After POR deassertion|After destructive<br>reset deassertion|After functional reset deassertion|
|---|---|---|---|
|Clock sources|• FIRC_CLK and<br>SIRC_CLK on<br>• Others off|• FIRC_CLK and<br>SIRC_CLK on<br>• Others off|• FIRC_CLK and<br>SIRC_CLK on<br>• SXOSC_CLK same as<br>before functional reset<br>• FXOSC_CLK and<br>PLL_PHIn_CLK off|
|Clock selection|FIRC_CLK|FIRC_CLK|FIRC_CLK|
|Clock dividers|Default configuration|Default configuration|Default configuration|
|Reset status flags|MC_RGM.DES[F_POR] equals<br>1, others equal 0|MC_RGM.DES[F_DR_n] equals<br>1, others equal 0|MC_RGM.FES[F_FR_n] equals<br>1, others equal 0|
|MC_ME<br>previous mode|Reset|Reset|Reset|
|FCCU<br>fault information|Cleared|Cleared|Retained|
|HSE_B RAM|Initialized|Initialized|Initialized|
|SRAM content|Invalid|Invalid|Retained|
|DCF configurations<br>in DCM|Reset value|Existing loaded value (reset<br>value after POR)|Reloaded from flash memory|
|Cores|All off|All off|HSE_B core on, others off|
|Logic on POR<sup>1</sup>|Out of reset with<br>default configuration|Out of reset with<br>default configuration|Out of reset with<br>default configuration|
|Logic on destructive<br>reset<sup>1</sup>|Under reset with<br>default configuration|Out of reset with<br>default configuration|Out of reset with<br>default configuration|
|Logic on functional<br>reset<sup>1</sup>|Under reset with<br>default configuration|Under reset with<br>default configuration|Out of reset with<br>default configuration|



1. For the list of peripherals affected by POR, destructive reset, and functional reset events, see Module reset status. 

## 30.7 Module reset status 

Table 164. Module reset status 

|Module instances<sup>1</sup>|Destructive|Functional|Power domain<sup>2</sup>|Part of LBIST<sup>3</sup>|
|---|---|---|---|---|
|MC_RGM|Y|Y|Standby|No|
|PRAMC|Y|Y|Run|Yes|
|PFC|Y|Y|Run|Yes|
|SIUL_VIRTWRAPPER_PDAC0|Y|Y|Run|No|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

968 / 4640 

NXP Semiconductors 

Reset Overview 

Table 164. Module reset status (continued) 

|Module instances<sup>1</sup>|Destructive|Functional|Power domain<sup>2</sup>|Part of LBIST<sup>3</sup>|
|---|---|---|---|---|
|SIUL_VIRTWRAPPER_PDAC1|Y|Y|Run|No|
|SIUL_VIRTWRAPPER_PDAC2|Y|Y|Run|No|
|SIUL_VIRTWRAPPER_PDAC3|Y|Y|Run|No|
|SIUL_VIRTWRAPPER_PDAC4<sup>4</sup>|Y|Y|Run|No|
|DCM|Y|Y|Run and Standby<sup>5</sup>|No|
|TRGMUX|Y|Y|Run|No|
|WKPU|Y|Y|Standby|No|
|CMU_Fx_[0:5]|Y|Y|Run|CMU 0-3: No<br>CMU 1-2: Yes<br>CMU 4-5: Yes|
|FIRC|Y<sup>6</sup>|Y<sup>6</sup>|Standby|No|
|FXOSC|Y|Y|Standby|No|
|MC_CGM<sup>7</sup>|Y|N|Run|No|
|MC_ME|Y|Y|Run|No|
|PLL|Y|Y|Run|No|
|PLL_AUX<sup>4</sup>|Y|Y|Run|No|
|Configuration GPR|Y|Y|Run|No|
|eMIOS 0-2|Y|Y|Run|No|
|PIT_0|Y|Y|Standby<sup>8</sup>|No|
|PIT_[1:2]|Y|Y|Run|No|
|FlexCAN_[0:5]|Y|Y|Run|No|
|FlexCAN_[6:7]<sup>4</sup>|Y|Y|Run|No|
|FlexIO|Y|Y|Run|No|
|LPUART_[0:15]|Y|Y|Run|No|
|LPI2C_[0:1]|Y|Y|Run|No|
|I3C0|Y|Y|Run|No|
|LPSPI_[0:5]|Y|Y|Run|No|
|QuadSPI|Y|Y|Run|No|
|SAI_[0:1]|Y|Y|Run|No|
|uSDHC<sup>4</sup>|Y|Y|Run|No|
|ADC_[0:2]|Y|Y<sup>11</sup>|Run|No|
|LPCMP_[0:2]|Y|Y|Standby|No|
|TempSense|Y|Y<sup>11</sup>|Run|No|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

969 / 4640 

NXP Semiconductors 

Reset Overview 

Table 164. Module reset status (continued) 

|Module instances<sup>1</sup>|Destructive|Functional|Power domain<sup>2</sup>|Part of LBIST<sup>3</sup>|
|---|---|---|---|---|
|CRC|Y|Y|Run|Yes|
|FCCU (+FOSU)|Y|N|Run|Yes|
|STCU2|Y|N|Run|No|
|HSE_B MUA-MUB|Y|Y|Run|No|
|MU_2 MUA-MUB<sup>4</sup>|Y|Y|Run|No|
|JDC|Y<sup>9</sup>|Y<sup>9</sup>|Run|No|
|DMAMUX_[0:1]|Y|Y|Run|No|
|PMC|Y<sup>10</sup>|N|Standby|No|
|Flash memory|Y|Y<sup>11</sup>|Run|No|
|SIRC|Y<sup>6</sup>|Y<sup>6</sup>|Standby|No|
|SXOSC|Y<sup>12</sup>|N|Standby|No|
|BCTU|Y|Y|Run|No|
|LCU[0:1]|Y|Y|Run|No|
|RTC|Y|N<sup>13</sup>|Standby|No|
|EMAC|Y|Y|Run|No|
|GMAC<sup>4</sup>|Y|Y|Run|No|
|HSE_B|Y|Y|Run|No|
|SWT_0|Y|Y|Standby|No|
|SWT_1|Y|Y|Run|Yes|
|SWT_2<sup>4</sup>|Y|Y|Run|Yes|
|STM_0|Y|Y|Run|No|
|STM_1|Y|Y|Run|No|
|STM_2<sup>4</sup>|Y|Y|Run|No|
|MSCM|Y|Y|Run|No|
|ERM_0|Y|Y|Run|Yes|
|ERM_1<sup>4</sup>|Y|Y|Run|Yes|
|EIM_0|Y|Y|Run|Yes|
|EIM_1<sup>4</sup>|Y|Y|Run|Yes|
|EIM_2<sup>4</sup>|Y|Y|Run|Yes|
|eDMA|Y|Y|Run|Yes|
|JTAGC|N|N|Run|No|
|MDM_AP|Y|N|Run|No|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

970 / 4640 

NXP Semiconductors 

Reset Overview 

Table 164. Module reset status (continued) 

|Module instances<sup>1</sup>|Destructive|Functional|Power domain<sup>2</sup>|Part of LBIST<sup>3</sup>|
|---|---|---|---|---|
|APB_AP|Y|N|Run|No|
|Cortex-M7_0|Y|Y<sup>14</sup>|Run|No|
|Cortex-M7_1|Y|Y<sup>14</sup>|Run|No|
|Cortex-M7_2<sup>4</sup>|Y|Y|Run|No|
|Cortex-M7_0 AHB-AP|Y|N|Run|No|
|Cortex-M7_0 AHB-AP|Y|N|Run|No|
|MC_PCU|Y|N|Standby|No|
|Legends:|||||
|Y|T|he entire module re|sets on this particular r|eset.|
|Y|Only a|portion of the modu|le resets on this particu|lar reset.|
|N|No|portion of the modul|e resets on this particul|ar reset|



1. All the modules listed in this table are reset on a POR event. See the memory map file attached to this document for the availability of modules across various parts in the S32K3xx family. 

2. The modules in the RUN domain get reset on standby exit. The modules in STANDBY domain are not impacted by standby exit and retain their contents. However in case of standby exit via functional reset or destructive reset event, the corresponding flops within the STANDBY domain modules will also get reset. 

3. The modules in the LBIST logic get reset on selftest completion. 

4. Present in S32K358 only. 

5. Flash memory scanning logic is available in the Run domain. GPRs and LC decode logic are available in Standby domain. 

6. All memory-mapped registers are on functional reset. The trimming logic is on destructive reset. Rest of counter and other stuff is on POR. 

7. During functional reset stages FUNC2 and FUNC3 (see the Functional reset sequence descriptions for functional reset stage descriptions), MC_CGM.MUX_n_CSC and MC_CGM.MUX_n_DIV_m are automatically set to their default values. The default value of the MC_CGM.MUX_n_CSC[SELCTL] selects FIRC_CLK as the source clock for all multiplexers. The default value of the MC_CGM.MUX_n_DIV_m is register instance specific (see the "MC_CGM register descriptions" section in the Clock Generation Module (MC_CGM) chapter). 

8. Only PIT_0 supports the RTI feature, and exists in the Standby domain. 

9. The system domain is reset on functional reset. A POR will reset it completely. 

10. PMC registers are reset on a destructive reset except PMC.LVSC, which is reset only by own PMC.LVSC[PORF] flag. The LVR and POR logic is reset on an LVR or own PORF (see PMC.CONFIG and PMC.LVSC descriptions for details). 

11. Reset on a functional reset; however, reset recovery occurs before the chip functional reset recovery, at the functional reset exit sequence start, for proper trim scanning and loading. 

12. SXOSC is reset on a destructive reset so that the RTC operates properly across a functional reset. 

13. RTC operates during a functional reset. 

14. The functional reset maps to nSYSRESET to Arm Cortex-M7 and the destructive reset maps to nPORESET to Arm Cortex-M7. See the Cortex-M7 TRM for further description on part of logic on different domains within Cortex-M7. 

## 30.8 System RAM retention across functional reset 

System RAM retains content during functional reset through the crossbar halt handshake. The system crossbar halts during the functional reset entry sequence. Therefore, the accesses do not cause any content corruption (see Functional reset sequence for more information). 

Follow this sequence for the crossbar halt handshake (see Halt handshake using the daisy-chaining method for gasket locations): 

1. Send a halt request to the HSE_B AXBS, DMA AXBS, and EMAC IAHB bridges in parallel. 

2. Wait for a halt acknowledgement from HSE_AXBS and DMA AXBS. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

971 / 4640 

NXP Semiconductors 

Reset Overview 

3. Send a halt request to the DMA IAHB and HSE_B IAHB gaskets. 

4. Wait for a halt acknowledgement from all the gaskets listed in the aforementioned steps. 

5. Send a halt request to the system AXBS. 

6. Wait for a halt acknowledgement from the system AXBS. 

7. Send a halt request to a peripheral AXBS. 

8. Wait for a halt acknowledgement from a peripheral AXBS. 

9. Send a halt request to the TCM IAHB and QSPI IAHB gaskets. 

10. Wait for a halt acknowledgement from all the gaskets listed in the aforementioned steps. 

11. Send a halt request to the AIPS0 IAHB and AIPS1 IAHB gaskets. 

12. Wait for a acknowledgement from all of the gaskets listed in the aforementioned steps. 

13. Send a halt request to TCM AXBS. 

14. Wait for a halt acknowledgement from TCM AXBS. 

After this halt sequence completes, the crossbar halt acknowledgement sequence also completes and the chip proceeds to the FUNC1 stage in the functional reset entry sequence. 

~~<mark>NOTE</mark>~~ 

RAM retention is supported across the functional reset event for system RAMs only and not for HSE_B or peripheral memories. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

972 / 4640 

NXP Semiconductors 

Reset Overview 

### 30.8.1 Halt handshake using the daisy-chaining method 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/030_Reset_Overview/S32K3XXRM_数据表.pdf-0973-03.png)


<!-- Start of picture text -->
PLL=240/160 MHz 8-40 MHz FXOSC CORE_CLK PLAT_AIPS_CLK HSE_CLK<br>eDMA3 HSE<br>32ch CM0+<br>DIV DIV DIV AHB AHB<br>64-bit 64-bit<br>160 MHz 120 MHz 80 MHz<br>MDAC1 MDAC3<br>EMAC<br>I-CACHE 8 KB Cortex-M7_0 Cortex-M7_1 I-CACHE 8 KB ADDRGEN ADDRGEN<br>I-TCM D-CACHE 8 KB0 64-bit NVICMPU DSPFPU NVICMPU DSPFPU 64-bit D-CACHE 8 KB0 I-TCM MDAC5 AHB32-bit RDATAwDATAGENCHK RDATAwDATAGENCHK<br>32 KB 1 1 32 KB 1:2 32:64<br>M0 1:2<br>D-TCM 32 KB 01 32-bit Primary core (checker’s) coreSecondary 32-bit 01 D-TCM 32 KB ADDRGEN AXBS_Lite S0 S1 XBIC AHB<br>RDATA splitter<br>D-TCM 32 KB 01 32-bit 32-bit 01 D-TCM 32 KB wDATAGENCHK 1:1 bypass<br>Decoupled = 0Lockstep = 1 XHB400 XHB400 Decoupled = 0Lockstep = 1 ADDRGEN<br>RDATA<br>Optional lockstep MDAC0 MDAC4 CHK<br>AHB_32_64 wDATAGEN<br>AHB_32_64 ADDRGEN<br>RDATA<br>ADDR ADDR CHK<br>GEN GEN wDATA<br>RDATA RDATA GEN<br>CHK CHK<br>wDATA wDATA<br>GEN GEN<br>S0M0 S4 S1 M4 S2 XBICM3 S6M2 M1 S3 AXBS (64-bit)S5 System AXBS64-bit @ 160 MHz S0 M0 XBICM3 M1S1 AXBS_LiteM2 S2(64-bit) Peripheral AXBS64-bit @ 160 MHz<br>2:1 2:1<br>MRC0 MRC1 MRC2<br>ADDR ADDR ADDR ADDR ADDR ADDRCHK 2:1 ADDRCHK ADDRCHK ADDRCHK<br>CHK CHK CHK CHK CHK RDATA RDATA RDATA RDATA<br>RDATA RDATA RDATA RDATA RDATA GEN ADDR GEN GEN GEN<br>GEN GEN GEN GEN GEN wDATA CHK wDATA wDATA wDATA<br>wDATA wDATA CHK RDATA CHK CHK CHK<br>LEGEND  P0 P2 P1 CHK CHK GEN<br>APB v3AXI64AHB64 64-bit + ECCPFLASH x256 64-bit + ECC*PRAM0 P0 64-bit + ECC*PRAM1 P0 1:1 64:32RDATAADDRGEN wDATACHK PDAC0AIPS0 PDAC1AIPS1 PDAC2AIPS2<br>Fixed gasketsAHB32IPBUS C-FLASH 1 MB 32 MHz ADDRCHK SRAM0 160 KBx72 SRAM1 160 KBx72 wDATAsplitterGENCHKAHB XBIC 120 MHz QSPI AHB& CODEDATA Fast off platf.Peripherals On platformOff platformPeripheralsPeripherals Off platformOn platformPeripheralsPeripheralsMU HSE_1<br>ECC gasketsConfigurablegaskets C-FLASH 1 MB D-FLASH 128 KB ADDRCHK wDATARDATAGENCHK MU HSE_0 MU_AMU_B<br>RDATA<br>GEN * ECC data and address encode<br>wDATA<br>INTERNAL USE ONLY CHK<br>AHBS 32-bit AXI 64-bit AHBP 32-bit AHBS 32-bit AXI 64-bit AHBP 32-bit<br><!-- End of picture text -->

Figure 122. Halt handshake using the daisy-chaining method 

## 30.9 Pad state during reset and after reset 

SIUL2 controls the GPIO functionality. It sets to its default state on a functional reset, and ensures that every pad initializes to its default state (see the default configurations and reset states of the chip's GPIO in the IOMUX file attached to this document). 

## 30.10 Reset pin 

This chip contains a bidirectional reset pin (RESET_b) indicating the reset state. RESET_b multiplexes with the other functions on port PTA5 (see the IOMUX file attached to this document). 

The DCF configuration controls the multiplexing capabilities of RESET_b. The default configuration of the RESET_b port is that of a dedicated reset signal (for example, not multiplexed. See the DCF clients file attached to this document for more information). 

The RESET_b pin offers the following uses if you configure it for the reset functionality: 

- Acts as an external destructive reset source 

- Acts as an indicator for the chip reset sequence for both functional and destructive reset sequences 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

973 / 4640 

NXP Semiconductors 

Reset Overview 

~~<mark>NOTE</mark>~~ 

MC_RGM.FES[F_EXR] captures an externally sourced RESET_b assertion for a destructive reset. 

The RESET_b pin also indicates an internally asserted reset to external modules. It has a weak internal pullup. In normal Run mode, it keeps the chip out of reset. 

### 30.10.1 Reset pin control during self-test 

You can write 1 to MC_RGM.ERCTRL[ERASSERT] to assert RESET_b (writes only in Supervisor mode), before LBIST or MBIST executes. MC_RGM then asserts RESET_b and tristates the GPIO pins placing them in a safe state. Tristating GPIO ensures a safe state for the chip pins when LBIST or MBIST executes. Following BIST, the chip executes a reset sequence. The chip configures again for the application software, before executing the safety function. MC_RGM.ERCTRL[ERASSERT] clears on a functional reset. See Figure 8 for an illustration. 

~~<mark>NOTE</mark>~~ 

Writing 1 to SIUL2.MSCRn[SMC] enables the GPIO pins and the chip continues its normal I/O functionality. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/030_Reset_Overview/S32K3XXRM_数据表.pdf-0974-09.png)


<!-- Start of picture text -->
Configure self-test<br>Write<br>MC_RGM.ERCTRL[ERASSERT]<br>Initiate self-test<br><!-- End of picture text -->

Figure 123. Reset pin control before self-test 

Multiple chip configuration scenarios cause RESET_b to react differently after self-test completion: 

- You can write 1 to MC_RGM.ERCTRL[ERASSERT] causing RESET_b to assert. This assertion does not impact the reset sequence, and the reset indicates that the chip is not available in Functional mode (although the chip is not in reset sequence). 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/030_Reset_Overview/S32K3XXRM_数据表.pdf-0974-13.png)


<!-- Start of picture text -->
Reset Run Reset Run<br>Chip operation mode Reset Self-test configuration Self-test Reset after self-test Normal application run<br>MC_RGM.ERCTRL[ERASSERT]<br>RESET_b<br><!-- End of picture text -->

Figure 124. Reaction when MC_RGM.ERCTRL[ERASSERT] = 1 

- If MC_RGM.ERCTRL[ERASSERT] = 0 (the default value), the RESET_b pin goes low after self-test completes. After self-test, the chip undergoes a functional reset in which the chip hardware writes 0 to MC_RGM.ERCTRL[ERASSERT]. The RESET_b pin goes high after the reset deasserts. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

974 / 4640 

NXP Semiconductors 

Reset Overview 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/030_Reset_Overview/S32K3XXRM_数据表.pdf-0975-02.png)


<!-- Start of picture text -->
Reset Run Reset Run<br>Chip operation mode Reset Self-test configuration Self-test Reset after self-test Normal application run<br>MC_RGM.ERCTRL[ERASSERT]<br>RESET_b<br><!-- End of picture text -->

Figure 125. Reaction when MC_RGM.ERCTRL[ERASSERT] = 0 

- If MC_RGM.ERCTRL[ERASSERT] = 0 (the default value), but you write 1 to MC_RGM.FBRE[ST_DONE], the RESET_b pin does not assert after self-test completes. 

||Reset<br>|Run<br>|Re<br> <br>|set<br>|Run<br>|
|---|---|---|---|---|---|
|Chip operation mode|Reset|Self-test configuration|Reset aft<br>Self-test|er self-test|Normal application run|
|MC_RGM.ERCTRL[ERASSERT]||||||
|RESET_b||||||



Figure 126. Reaction when MC_RGM.ERCTRL[ERASSERT] = 0 and MC_RGM.FBRE[ST_DONE] = 1 

## 30.11 Reset control in Lockstep mode 

In Lockstep mode, a two-cycle delayed lockstep implementation controls the reset to both the application cores, Cortex-M7_0 and Cortex-M7_1. This lockstep implementation means Cortex-M7_0 starts two clock cycles before Cortex-M7_1. You can configure the dcf_client_utest_misc[LOCSTEP_EN] field to control the lockstep (see the DCF clients file attached to this document for more information). 

The Cortex-M7 cores consist of two reset domains: 

- PORESETn (see PORESETn control in Lockstep mode) 

- SYSRESETn (see SYSRESETn control in lockstep) 

~~<mark>NOTE</mark>~~ Lockstep feature is only available in S32K342, S32K344 and S32K358. For S32K358, Cortex-M7_0 and CortexM7_1 are in lockstep. 

### 30.11.1 PORESETn control in Lockstep mode 

PORESETn includes debug modules that work across chip warm resets. The PORESETn domain resets on any destructive reset event. PORESETn deasserts after two cycles of reset deassertion synchronization delay, as soon as destructive reset sequence exits. In Lockstep mode, the reset deassertion to Cortex-M7_1 is further delayed by two CORE_CLK cycles as shown in PORESETn control in Lockstep mode. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

975 / 4640 

NXP Semiconductors 

Reset Overview 

#### 30.11.1.1 PORESETn control in Lockstep mode 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/030_Reset_Overview/S32K3XXRM_数据表.pdf-0976-03.png)


<!-- Start of picture text -->
D Q<br>RSL<br>clk<br>Cortex-M7_1 PORESET n<br>Lockstep enable<br>(from UTEST_DCF_MISC_CLIENT)<br>Cortex-M7_0 PORESET n<br>D Q D Q<br>RSL<br>clk clk<br>Two-cycle lockstep<br>Destructive reset<br>CORE_CLK<br><!-- End of picture text -->

Figure 127. PORESETn control in Lockstep mode 

### 30.11.2 SYSRESETn control in lockstep 

Most of the components within the Cortex-M7 cores reside in the SYSRESETn domain, except the debug modules. These components reset on any functional reset event. The SYSRESETn reset remains gated even if it exits the functional reset until MC_ME.PRTN0_COREn_PCONF[CCE] enables the core clocks. The debugger can hold the core's SYSRESETn domain in reset, as described in section Application core debug from first instruction. 

After a chip's functional reset deasserts, the core clocks are functional, and there is no gating from the debugger, the application core's SYSRESETn is released after a two-cycle reset deassertion synchronizer delay. In Lockstep mode, the reset deassertion to Cortex-M7_1 is delayed by two CORE_CLK cycles, as shown in SYSRESETn control in Lockstep mode. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

976 / 4640 

NXP Semiconductors 

Reset Overview 

#### 30.11.2.1 SYSRESETn control in Lockstep mode 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/030_Reset_Overview/S32K3XXRM_数据表.pdf-0977-03.png)


<!-- Start of picture text -->
D Q<br>RSL<br>clk<br>SDA_AP[RST_RELEASE_CM7_1]<br>(Reset value=1)<br>D Q<br>CCTL_CM7_1<br>PRTN0_CORE1_PCONF[CCE] in MC_ME D Q 8 cycle delay* clk<br>(Reset value=0)<br>clk dbg_pwrup_req<br>CORE_CLK Cortex-M7_1 SYSRSTn<br>Functional reset Lockstep enable<br>(from UTEST_DCF_MISC_CLIENT)<br>Cortex-M7_0 SYSRSTn<br>D Q D Q<br>RSL<br>clk clk<br>SDA_AP[RST_RELEASE_CM7_0]<br>(Reset value=1) Two-cycle lockstep<br>D Q<br>CCTL_CM7_0<br>PRTN0_CORE0_PCONF[CCE] in MC_ME D Q 8 cycle delay* clk<br>(Reset value=0)<br>clk dbg_pwrup_req<br>CORE_CLK<br>Functional reset<br><!-- End of picture text -->

Figure 128. SYSRESETn control in Lockstep mode 

## 30.12 Application core debug from first instruction 

The chip supports application core debug starting on the first instruction. This is supported on any functional reset and through a RESET_b pin destructive reset for debug from destructive reset onwards using the following sequence (see SYSRESETn control in lockstep for more information on implementation). 

### 30.12.1 Debug from first instruction on power-up or destructive reset onwards 

1. When RESET_b is held low, the chip goes through a destructive reset sequence. 

2. When you pull down the RESET_b pin, the chip goes through a destructive reset sequence, exits from the destructive reset, and remains in functional reset, until the reset pin is released. 

3. When the RESET_b pin remains pulled down, the debugger configures SDA_AP.SDAAPRSTCTRL[RSTRELTLCM70], SDA_AP.SDAAPRSTCTRL[RSTRELTLCM71] and SDA_AP.SDAAPRSTCTRL[RSTRELTLCM72] according to the requirements. To enable debug from first instruction, you write 0 to these fields. To disable, you write 1. By default, the debug disables from the first instruction. 

4. On releasing the reset pin, the chip exits from the functional reset sequence and HSE_B starts executing. 

5. The PORESETn deassertion occurs for the application cores simultaneously (in case of lockstep, Cortex-M7_1 PORESETn deasserts after a two-cycle delay). The corresponding core clock enable gates the deassertion of SYSRESETn to cores. The SYSRESETn to the cores deasserts as follows. 

6. On the basis of whether the debugger authentication is performed via challenge, response, or neither of them, you can consider these scenarios: 

   - a. Debugger not connected (DBG_PWRUP_REQ = 0): 

      - i. BAF or FW writes to the clock enable control field in MC_ME for application cores, that is, to MC_ME.PRTN0_CORE0_PCONF[CCE] for Cortex-M7_0, MC_ME.PRTN0_CORE1_PCONF[CCE] for 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

977 / 4640 

NXP Semiconductors 

Reset Overview 

Cortex-M7_1 and MC_ME.PRTN0_CORE2_PCONF[CCE] for Cortex-M7_2 or to all the three fields as required. 

ii. The clock enables in the subsequent clock cycle. 

   - iii. SYSRESETn deasserts after ten clock cycles (adding eight clock cycles of delay ensures that reset always deasserts when the clock is available; two cycle of reset deassertion delay). In case of lockstep, Cortex-M7_1 reset is delayed by two additional clock cycles. 

- b. Debugger connected (DBG_PWRUP_REQ = 1): 

   - i. BAF or FW writes to the clock enable control field in MC_ME for application cores, that is, to MC_ME.PRTN0_CORE0_PCONF[CCE] for Cortex-M7_0,MC_ME.PRTN0_CORE1_PCONF[CCE] for Cortex-M7_1 and MC_ME.PRTN0_CORE2_PCONF[CCE] for Cortex-M7_2 or to all the three fields as required. 

ii. The clock is enabled. 

- iii. The debugger waits for sometime (at least ten clock cycles) 

   - and then writes 1 to SDA_AP.SDAAPRSTCTRL[RSTRELTLCM70] for Cortex-M7_0, SDA_AP.SDAAPRSTCTRL[RSTRELTLCM71] for Cortex-M7_1 and SDA_AP.SDAAPRSTCTRL[RSTRELTLCM72] for Cortex-M7_2, for releasing SYSRESETn of the corresponding core. 

- iv. SYSRESETn deasserts after ten clock cycles (adding eight clock cycles of delay ensures that the reset always deaserts when the clock is available; two cycle of RSL delay). In case of lockstep, the Cortex-M7_1 reset is delayed by two additional clock cycles. 

~~<mark>NOTE</mark>~~ 

- Cortex-M7_1 is not available in S32K314, S32K312, and S32K311. 

- Cortex-M7_2 is only available in S32K358. 

### 30.12.2 Debug from first instruction on functional reset onwards 

If you enable debug, on functional reset, the debug connection is retained. That is because the complete debug infrastructure is on destructive reset domain. 

### 30.12.3 Debug on standby exit by wake-up or functional reset 

If you enable debug before standby entry, then the Standby domain stores the final status. The configuration for reset release is reset (SDA_AP.SDAAPRSTCTRL[RSTRELTLCM70], SDA_AP.SDAAPRSTCTRL[RSTRELTLCM71] and SDA_AP.SDAAPRSTCTRL[RSTRELTLCM72]. The reset value of the three fields is 1), which defaults to debug from the first instruction disabled. 

You must configure the reset release on standby exit. It uses MC_RGM's low-power debug protocol before ungating the reset deassertion. 

## 30.13 Glossary 

DCF Device configuration format POR Power-on reset 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

978 / 4640 

