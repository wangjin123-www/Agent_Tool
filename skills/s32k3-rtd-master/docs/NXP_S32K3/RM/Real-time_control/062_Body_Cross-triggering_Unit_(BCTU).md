NXP Semiconductors 

# Chapter 62 Body Cross-triggering Unit (BCTU) 

## 62.1 Chip-specific BCTU information 

### 62.1.1 BCTU configuration 

The following table lists the BCTU configuration. 

Table 362. BCTU configuration 

|Feature|Configuration|
|---|---|
|FIFO1|16 words|
|FIFO2|8 words|



### 62.1.2 Trigger sources and instances 

This chip has 1 instance of BCTU module. 

Table 363. BCTU instance 

|Instance|S32K311/S32K312/S32K322/S32K342/S32K314/S32K324/S32K344/S32K358|
|---|---|
|BCTU|Yes|



The following table lists the BCTU trigger sources. 

Table 364. BCTU Trigger sources 

|BCTU Trigger Number|Module|Source|Applicability|
|---|---|---|---|
|0|eMIOS_0|Channel_0|All|
|1|eMIOS_0|Channel_1|All|
|2|eMIOS_0|Channel_2|All|
|3|eMIOS_0|Channel_3|All|
|4|eMIOS_0|Channel_4|All|
|5|eMIOS_0|Channel_5|All|
|6|eMIOS_0|Channel_6|All|
|7|eMIOS_0|Channel_7|All|
|8|eMIOS_0|Channel_8|All|
|9|eMIOS_0|Channel_9|All|
|10|eMIOS_0|Channel_10|All|
|11|eMIOS_0|Channel_11|All|
|12|eMIOS_0|Channel_12|All|
|13|eMIOS_0|Channel_13|All|
|14|eMIOS_0|Channel_14|All|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2262 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

Table 364. BCTU Trigger sources (continued) 

|BCTU Trigger Number|Module|Source|Applicability|
|---|---|---|---|
|15|eMIOS_0|Channel_15|All|
|16|eMIOS_0|Channel_16|All|
|17|eMIOS_0|Channel_17|All|
|18|eMIOS_0|Channel_18|All|
|19|eMIOS_0|Channel_19|All|
|20|eMIOS_0|Channel_20|All|
|21|eMIOS_0|Channel_21|All|
|22|eMIOS_0|Channel_22|All|
|23|Any of the TRGMUX inp|BCTU_Trg23|All|
|24|eMIOS_1|Channel_0|All|
|25|eMIOS_1|Channel_1|All|
|26|eMIOS_1|Channel_2|All|
|27|eMIOS_1|Channel_3|All|
|28|eMIOS_1|Channel_4|All|
|29|eMIOS_1|Channel_5|All|
|30|eMIOS_1|Channel_6|All|
|31|eMIOS_1|Channel_7|All|
|32|eMIOS_1|Channel_8|All|
|33|eMIOS_1|Channel_9|All|
|34|eMIOS_1|Channel_10|All|
|35|eMIOS_1|Channel_11|All|
|36|eMIOS_1|Channel_12|All|
|37|eMIOS_1|Channel_13|All|
|38|eMIOS_1|Channel_14|All|
|39|eMIOS_1|Channel_15|All|
|40|eMIOS_1|Channel_16|All|
|41|eMIOS_1|Channel_17|All|
|42|eMIOS_1|Channel_18|All|
|43|eMIOS_1|Channel_19|All|
|44|eMIOS_1|Channel_20|All|
|45|eMIOS_1|Channel_21|All|
|46|eMIOS_1|Channel_22|All|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2263 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

Table 364. BCTU Trigger sources (continued) 

|BCTU Trigger Number|Module|Source|Applicability|
|---|---|---|---|
|47|Any of the TRGMUX inp|BCTU_Trg47|All|
|48|eMIOS_2|Channel_0|S32K358, S32K3x4|
|49|eMIOS_2|Channel_1|S32K358, S32K3x4|
|50|eMIOS_2|Channel_2|S32K358, S32K3x4|
|51|eMIOS_2|Channel_3|S32K358, S32K3x4|
|52|eMIOS_2|Channel_4|S32K358, S32K3x4|
|53|eMIOS_2|Channel_5|S32K358, S32K3x4|
|54|eMIOS_2|Channel_6|S32K358, S32K3x4|
|55|eMIOS_2|Channel_7|S32K358, S32K3x4|
|56|eMIOS_2|Channel_8|S32K358, S32K3x4|
|57|eMIOS_2|Channel_9|S32K358, S32K3x4|
|58|eMIOS_2|Channel_10|S32K358, S32K3x4|
|59|eMIOS_2|Channel_11|S32K358, S32K3x4|
|60|eMIOS_2|Channel_12|S32K358, S32K3x4|
|61|eMIOS_2|Channel_13|S32K358, S32K3x4|
|62|eMIOS_2|Channel_14|S32K358, S32K3x4|
|63|eMIOS_2|Channel_15|S32K358, S32K3x4|
|64|eMIOS_2|Channel_16|S32K358, S32K3x4|
|65|eMIOS_2|Channel_17|S32K358, S32K3x4|
|66|eMIOS_2|Channel_18|S32K358, S32K3x4|
|67|eMIOS_2|Channel_19|S32K358, S32K3x4|
|68|eMIOS_2|Channel_20|S32K358, S32K3x4|
|69|eMIOS_2|Channel_21|S32K358, S32K3x4|
|70|eMIOS_2|Channel_22|S32K358, S32K3x4|
|71|Any of the TRGMUX inp|BCTU_Trg71|S32K358, S32K3x4|



~~<mark>NOTE</mark>~~ 

You must clear triggers to BCTU after TRGMUX programming using TRGCFG_n[TRG_FLAG] bit. 

## 62.2 Introduction 

BCTU accepts ADC conversion-request trigger inputs and routes those requests to one or more ADCs. BCTU accepts the following trigger sources: 

- Hardware triggers (outputs from on-chip timer modules) 

- Software triggers through the SFTRGRn register 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2264 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

BCTU maps each trigger input to a Trigger Configuration (TRGCFG_0 - TRGCFG_71) register, which specifies the target ADC channel and other control data for the requested conversion. 

You can configure a list of ADC channels, the CL, that processes a sequence of conversions in response to a single trigger input. See the Conversion list (CL) section. 

BCTU stores each ADC conversion result for CPU access or routing to memory through DMA. 

If the same ADC is targeted by multiple triggers, priority logic selects the next trigger to process from all active trigger inputs. See Priority of simultaneous triggers. 

BCTU inputs are active-high signals. That is, a logic 1 asserts the trigger input. 

## 62.3 Features 

BCTU supports: 

- 72 trigger inputs, configured with the Trigger Configuration (TRGCFG_0 - TRGCFG_71) registers 

- Trigger outputs to 3 ADCs 

- One priority selection logic block per ADC 

- Selection multiplexers to select one trigger at a time for each ADC 

- A CL of 32 ADC channels 

- A trigger grouping block to latch the hardware triggers. BCTU clears these triggers when the ADC sends an acknowledgement for conversion completion. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2265 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

## 62.4 Block diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/062_Body_Cross-triggering_Unit_-BCTU-/S32K3XXRM_数据表.pdf-2266-03.png)


<!-- Start of picture text -->
Priority<br>Software logic 0<br>CPU<br>trigger<br>Trigger 0 TRGCFG_0<br>ADC0<br>Trigger 1 TRGCFG_1<br>Trigger 2 TRGCFG_2<br>Priority<br>logic 2<br>TRGCFG_71<br>Trigger 71<br>ADC2<br>CL channels<br>Trigger grouping<br><!-- End of picture text -->

Figure 345. BCTU block diagram 

## 62.5 Interaction with other peripherals 

BCTU works together with timer and ADC modules on the chip. Use the Trigger Configuration registers (TRGCFG_n) to map BCTU triggers to ADC inputs. When a timer output asserts a BCTU trigger, BCTU passes the trigger to an ADC input and stores the trigger assertion until the corresponding ADC begins the requested conversion. When the ADC completes the conversion, BCTU asserts a trigger clear signal to clear both the internally stored trigger and the external trigger source if they are still asserted. Implementation illustrates the modules that interact with BCTU. 

~~<mark>NOTE</mark>~~ 

A timer trigger can remain active until the corresponding ADC initiates conversion. Therefore, another match may occur in the timer before the ADC conversion begins. BCTU does not detect this trigger overrun. Your application must look for and respond to such conditions. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2266 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

## 62.6 Implementation 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/062_Body_Cross-triggering_Unit_-BCTU-/S32K3XXRM_数据表.pdf-2267-03.png)


<!-- Start of picture text -->
Configuration and<br> software triggers Conversion results<br>CPU DMA<br>Trigger Conversion command<br>BCTU<br>eMIOS0 ADC0<br>Trigger clr Conversion result<br>Trigger Conversion command<br>eMIOS1 ADC1<br>Trigger clr Conversion result<br>Trigger Conversion command<br>eMIOS2 ADC2<br>Trigger clr Conversion result<br>Trigger<br>TRGMUX<br>72 trigger inputs<br><!-- End of picture text -->

Figure 346. Implementation 

## 62.7 Module Disable (Low Power state) 

Module Disable (MCR[MDIS]) stops the BCTU clock, resulting in reduced power consumption. 

When you disable BCTU (write 1 to MDIS), it: 

- Waits for the completion of any in-progress conversions before stopping the clock. 

- Ignores all trigger inputs. 

- Does not trigger any ADC conversion requests. 

- Maintains any asserted trigger inputs, which you can clear if necessary. 

When you re-enable BCTU (write 0 to MDIS) and Global Triggers are enabled (MCR[GTRGEN]), BCTU processes all active asserted trigger inputs and sends conversion requests to ADCs according to the priority scheme. 

## 62.8 Software reset 

You can reinitialize all BCTU registers to their reset values with Software Reset (MCR[Software_Reset]). 

Software reset does not clear any active trigger inputs, but it does put the ADC interface into the Reset state. Therefore, to avoid data incoherency, you must terminate any BCTU-triggered conversions or wait until they are complete before asserting software reset. 

## 62.9 Triggers 

### 62.9.1 Overview 

BCTU prioritizes ADC trigger inputs based on the input number: the lower the number, the higher the priority associated with it. Therefore, trigger 0 is the highest priority trigger and trigger 71 is the lowest priority. The trigger input priority scheme determines 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2267 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

which trigger takes precedence when more than one trigger occurs at the same time, or when the triggered ADC is busy with a conversion. Therefore, there are two possible scenarios for the trigger priority selection: 

- When there are no ongoing conversions 

- When a triggered ADC is executing a conversion 

BCTU supports two types of trigger sources: 

- Hardware triggers from timer modules 

- Software triggers (SFTRGRn) 

### 62.9.2 Hardware triggers 

To request an ADC conversion through the BCTU, a timer module such as eMIOS asserts its output signal, which is connected to a BCTU trigger input. When BCTU detects the asserted trigger, it routes that request to the ADCs selected in the corresponding Trigger Configuration (TRGCFG_n[ADC_SELm]). The trigger remains asserted until the requested conversion begins, at which time BCTU clears the trigger. If the timer asserts the trigger input when the trigger is already set, BCTU ignores the new trigger. If BCTU receives a new trigger input at the same time it is clearing the trigger, then the trigger remains asserted and BCTU initiates a new conversion. 

If you configure the trigger for CL, trigger assertion begins a sequence of conversions controlled by the CL Channel Address (LISTCHR_0 - LISTCHR_15) registers. In this event, BCTU clears the trigger when the last conversion in the CL begins. 

~~<mark>NOTE</mark>~~ Any new trigger input participates in the trigger priority selection scheme and therefore may not trigger the next conversion. 

### 62.9.3 Software triggers 

You assert a software trigger by writing 1 to the corresponding field of the appropriate Software Trigger (SFTRGRn) register. Similar to the hardware triggers, BCTU changes the software trigger field to 0 when the requested conversion begins. If you write 1 to the software trigger field while the conversion is still in progress, BCTU ignores the request. If you write 1 to the field at the same time BCTU is attempting to clear the trigger (change the field to 0), the trigger remains asserted and BCTU triggers a new conversion following the trigger priority criteria. 

### 62.9.4 Configure all triggers 

Global Trigger Enable (MCR[GTRGEN]) allows you to configure the BCTU trigger inputs and then activate them all at one time. 

To configure and then activate all BCTU triggers: 

1. Clear any currently active and asserted trigger inputs (write 0 to TRGFG_n[TRG_FLAG]), which also causes BCTU to assert trigger clear to the trigger sources. 

2. Disable Global Triggers (MCR[GTRGEN]). This action deactivates all trigger inputs and prevents BCTU from generating any ADC conversion requests. 

3. Configure the individual trigger inputs (see Configure individual triggers). 

4. Enable Global Triggers (MCR[GTRGEN]). This action activates all individually enabled triggers at the same time. 

### 62.9.5 Configure individual triggers 

Using Trigger Configuration (TRGCFG_0 - TRGCFG_71), for each trigger: 

- Enable the trigger (TRIGEN). 

- Specify the target ADC (ADC_SELn). 

- Specify the ADC channel (CHANNEL_VALUE_OR_LADDR). 

- Specify whether the trigger initiates a single conversion or a CL (TRS). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2268 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

- For a CL trigger, specify a pointer to the CL element (TRGCFG_x[CHANNEL_VALUE_OR_LADDR]). 

### 62.9.6 Reconfigure triggers on-the-fly 

~~<mark>NOTE</mark>~~ 

Reconfigure BCTU triggers only when the individual trigger is not active (TRG_FLAG). If TRG_FLAG is 1, the requested conversion is still in progress and it is not safe to modify the trigger configuration. 

To reconfigure a trigger on-the-fly (while BCTU is in full operation): 

1. Disable the trigger (TRIGEN) to prevent it from requesting a new conversion. 

2. Check the current state of the trigger (TRG_FLAG) to be sure no conversion or CL is in progress. 

3. When any in-progress conversion or CL completes (TRG_FLAG == 0), clear the trigger source by writing 1 to TRG_FLAG. This action ensures that only trigger inputs that assert after you reconfigure and re-enable the trigger are able to request a new conversion or CL. 

4. Reconfigure the trigger (see Configure individual triggers). 

5. Enable the trigger (TRIGEN). 

### 62.9.7 Enable software triggers 

To allow software triggers (SFTRGRn[SFTRGm]) to request conversions, you must enable Global Trigger Enable (MCR[GTRGEN]). If you disable Global Trigger Enable, software triggers do not initiate a conversion but asserted triggers remain asserted. However, when you enable Global Trigger Enable, any asserted software triggers initiate conversions following the priority scheme of lowest to highest trigger number. 

Software triggers operate regardless of individual Trigger Enable (TRGCFG_x[TRIGEN]). That is, writing 1 to any Software Trigger (SFTRGRn[SFTRGm]) initiates a conversion (following the priority scheme) regardless of the value of Trigger Enable. This software trigger independence supports the elimination of conflict between software and hardware triggers. 

### 62.9.8 Trigger timing 

There are four clock cycles from assertion of a BCTU trigger input to assertion of the trigger output to the ADC. For single conversions, BCTU asserts Trigger Clear back to the trigger source simultaneous to asserting the trigger to the ADC. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/062_Body_Cross-triggering_Unit_-BCTU-/S32K3XXRM_数据表.pdf-2269-17.png)


<!-- Start of picture text -->
BCTU clock<br>Trigger input<br>Trigger clear<br>ADC trigger<br>Figure 347. Trigger timing<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/062_Body_Cross-triggering_Unit_-BCTU-/S32K3XXRM_数据表.pdf-2269-18.png)


### 62.9.9 Priority of simultaneous triggers 

When more than one trigger input asserts a conversion request to the same ADC at the same time—that is, in the same BCTU clock cycle—BCTU employs a priority scheme to determine which asserted trigger to process next. BCTU prioritizes trigger inputs based on the trigger number. The lowest number, trigger 0, has the highest priority, and the highest number, trigger 71, has the lowest priority. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2269 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

If two triggers assert in the same clock cycle, BCTU gives priority to the lower numbered trigger. For example, if trigger 0 and trigger 1 both assert in the same cycle, BCTU selects trigger 0 for trigger generation. Trigger 1 remains active (pending) until the conversion requested by trigger 0 completes. See Simultaneous trigger priority management. 

If trigger 0 asserts again before the next trigger selection opportunity at the end of the current conversion, then BCTU selects it again and trigger 1 remains asserted (pending) during the next ADC conversion time frame. 

As illustrated in Trigger timing, BCTU requires four clock cycles to transmit a conversion request to an ADC if that ADC is not already executing a conversion. However, if the ADC is busy at the time of trigger assertion, BCTU requires only three clock cycles to generate the conversion request for a subsequent conversion. 

Triggers that assert in the same clock cycle but target different ADCs are not in conflict, and BCTU processes both triggers at the same time. 

### 62.9.10 Simultaneous trigger priority management 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/062_Body_Cross-triggering_Unit_-BCTU-/S32K3XXRM_数据表.pdf-2270-07.png)


<!-- Start of picture text -->
BCTU clock<br>Trigger 0<br>Trigger 1<br>ADC trigger<br>Trigger clear 0<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/062_Body_Cross-triggering_Unit_-BCTU-/S32K3XXRM_数据表.pdf-2270-08.png)


Figure 348. Simultaneous trigger priority management 

### 62.9.11 Trigger management when ADC is busy 

When a trigger input asserts a conversion request to an ADC that is already processing a conversion requested by a different trigger, the new trigger remains active (pending) until the conversion in progress completes. This behavior is the same as if the two triggers had been simultaneous (occurred in the same clock cycle). When the in-progress conversion completes, the pending trigger then competes for priority with any other active trigger for that ADC. 

## 62.10 Conversion list (CL) 

### 62.10.1 CL overview 

A CL executes a sequence of conversions on one or more target ADCs. See CL architecture and operation. It also stores information from the last conversion executed in a sequence except for the target ADC, which is stored in ADC Select n (TRGCFG_m[ADC_SELn]). 

If the Channel or CL Address (TRGCFG_x[CHANNEL_VALUE_OR_LADDR]) points to a CL element containing one or more entries: 

1. The trigger initiates a sequence of conversions starting with the target CL element. 

2. The sequence executes until the LAST channel (LISTCHR_n[LAST_y] is 1), and stops after that channel is converted. 

When you configure the CL element for Next Channel Wait For Trigger (write 1 to LISTCHR_n[NEXT_CH_WAIT_ON_TRIG_y]): 

1. BCTU clears the trigger source. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2270 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

2. CL execution pauses after the current conversion is completed. 

3. CL execution resumes when the same trigger asserts again. 

BCTU determines trigger priority before executing any CL. See Priority of simultaneous triggers. 

### 62.10.2 CL architecture and operation 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/062_Body_Cross-triggering_Unit_-BCTU-/S32K3XXRM_数据表.pdf-2271-06.png)


<!-- Start of picture text -->
CL basic element<br>TRGCFG_n[CHANNEL_VALUE_OR_LADDR] LISTCHR_n[ADC_CHL_m]<br>LISTCHR_n[NEXT_CH_WAIT_ON_TRIG_m]<br>LISTCHR_n[LAST_m]<br>LADDR = 0<br>0 ADC Channel 0 0 Converting<br>1 ADC Channel 1 0 Converting<br>2 ADC Channel 0 0 Waiting Converting<br>1 continuous list with 3 breakpoints 3 ADC Channel 1 0 Converting<br>4 ADC Channel 1 0 Waiting Converting<br>5 ADC Channel 0 0 Waiting Converting<br>6 ADC Channel 0/1 1 Converting<br>1 continuous list with 1 channel 7 ADC Channel 0/1 1<br>8 ADC Channel 0 0<br>LISTSTAR[LISTSZ] 9 ADC Channel 0 0<br>Trigger<br>Trigger clear<br><!-- End of picture text -->

Figure 349. CL architecture and operation 

### 62.10.3 CL channel rules 

CL conversion obeys the following rules: 

- The sequence of conversions executes until the Last Channel (LISTCHR_n[LAST_y] is 1). 

- A CL conversion sequence precludes other conversions on the same ADC. If the CL is waiting (LISTCHR_n[NEXT_CH_WAIT_ON_TRIG_y] is 1), BCTU cannot route a non-CL conversion to that ADC (although that ADC remains available for normal and injected conversions). 

- Two or more triggers for different ADCs may point to the same CL. This CL can drive parallel execution on the selected ADCs. 

- If the Channel or CL Address (TRGCFG_x[CHANNEL_VALUE_OR_LADDR]) does not point to a valid list address, BCTU uses address 0 by default. 

- When the CL pointer reaches the last available list address (LISTSTAR[LISTSZ] minus 1), the pointer wraps to list address 0. 

- You can select more than one ADC per trigger using the ADC Select n (TRGCFG_x[ADC_SELn]) fields, but selecting more than one ADC is valid only for multiple parallel CL operation. If you select more than one ADC for a single-conversion trigger, BCTU ignores the trigger. 

## 62.11 ADC conversion results access 

### 62.11.1 Overview 

The value of DATA_DEST determines access to ADC results. 

- DATA_DEST = 000: ADC results are available in the ADC data registers. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2271 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

- DATA_DEST = 001: ADC results are available in FIFO 1 Result Data (FIFO Result Data (FIFO1DR - FIFO2DR)). See Route conversion data to FIFO. 

- DATA_DEST = 010: ADC results are available in FIFO 2 Result Data (FIFO Result Data (FIFO1DR - FIFO2DR)). See Route conversion data to FIFO. 

You can access ADC results using flags and interrupt requests (see Access on interrupt request) or DMA (see Access on DMA request). Interrupt requests are based on Module Status (MSR) flags. ADCnDR provides the following information, with one register used for each ADC: 

- The conversion results 

- The channel that was used for the conversion 

- The trigger input that initiated the conversion 

- Whether a CL element generated the conversion 

- Whether the data was the last conversion of a CL 

### 62.11.2 Access on interrupt request 

If interrupts are enabled for ADCn Result Data (MCR[IENn] is 1) and DMAs are disabled for ADCn Result Data (MCR[DMAn] is 0), BCTU generates an interrupt request for each available conversion data in ADCnDR. Because BCTU executes conversions on different ADCs in parallel, conversion results may be available on multiple ADCs at the same time. New Data (MSR[NDATAn] is 1) indicates that new conversion data is available in the corresponding ADC Data Result (ADCnDR). To clear the New Data flag, write 1 to MSR[NDATAn_CLR]. 

### 62.11.3 Access on DMA request 

If you enable DMA requests (MCR[DMAn]): 

- You must select one channel for DMA per ADC. 

- New conversion result data (ADCnDR) generates a DMA request. 

- The DMA controller deasserts the DMA request and writes 1 to MSR[NDATAn_CLR] to clear the flag. 

When an ADC generates New Data (MSR[NDATAn]), BCTU processes the DMA request. See Clear a DMA request. 

### 62.11.4 Clear an interrupt request 

BCTU clears an interrupt request when: 

- The number of valid entries is less than or equal to the FIFOn Watermark Level (FIFOWM[WM_FIFOn]). 

- You write 1 to FIFO Watermark Interrupt Status (FIFOERR[WM_INT_FIFOn]). 

### 62.11.5 Clear a DMA request 

BCTU clears a DMA request when: 

- The number of valid entries is less than or equal to the FIFOn Watermark Level (FIFOWM[WM_FIFOn]). 

- The DMA controller sends acknowledgment to BCTU. 

### 62.11.6 Clear an error-generated interrupt request 

Clear an interrupt generated because of an error condition by writing 1 to the appropriate error flag: 

- FIFOERR[OVR_ERR_FIFO1] 

- FIFOERR[UNDR_ERR_FIFO1] 

- FIFOERR[OVR_ERR_FIFO2] 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2272 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

- FIFOERR[UNDR_ERR_FIFO2] 

### 62.11.7 Conversion data overrun 

If new ADC conversion data becomes available before you read the previous data (ADCnDR), then BCTU indicates a data overrun (MSR[DATAOVRn] is 1). 

If you enable interrupts for the ADC (MCR[IENn]), a data overrun also generates an interrupt request, regardless of the DMA request configuration. 

To clear a data overrun (MSR[DATAOVRn]), write 1 to Data Overrun Clear (MSR[DATAOVRn_CLR]). See Clear an errorgenerated interrupt request. 

### 62.11.8 Route conversion data to FIFO 

BCTU allows you to route multiple ADC conversion results to one of 2 internal data FIFOs. Any trigger source can route results to an available FIFO based on the trigger index. Each FIFO has a dedicated counter (FIFOCNTR[CNTR_FIFOn]) to indicate the number of entries in the FIFO. 

Each FIFO also has its own result data register (FIFOnDR) that contains the following information about the last conversion result routed to the FIFO. 

- ADC result data 

- Trigger source index 

- ADC number 

- ADC channel number 

### 62.11.9 Read ADC result from FIFO 

Each FIFO has DMA and interrupt interfaces. The DMA interface reads data. The interrupt interface indicates watermark and 

error conditions: 

- An overrun error (FIFOERR[OVR_ERR_FIFOn]) occurs when you attempt to write data to an already full FIFO. 

- An underrun error (FIFOERR[UNDR_ERR_FIFOn]) occurs when you attempt to read data from an empty FIFO. 

- BCTU asserts a Watermark interrupt request if the number of valid FIFO entries exceeds the watermark level (FIFOWM[WM_FIFOn]). 

You can read a FIFO: 

- by enabling DMA requests (FIFOCR[DMA_EN_FIFOn]) 

- by polling the FIFO Full status (FIFOSR[FULL_FIFOn]) 

See Configuration of DMA and interrupt behavior. 

### 62.11.10 Configuration of DMA and interrupt behavior 

Table 365. Configuration of DMA and interrupt behavior 

|FIFOCR[DMA_EN_FIFOn]|FIFOCR[IEN_FIFOn]|Condition|
|---|---|---|
|0|0|No DMA request; no interrupt request|
|0|1|Interrupt request when FIFO exceeds watermark level; interrupt<br>request on error|
|1|0|DMA request when FIFO exceeds watermark level|
|1|1|DMA request when FIFO exceeds watermark level; interrupt<br>request on error|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2273 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

## 62.12 Multiple parallel conversions (MPC) 

### 62.12.1 Overview 

The MPC mechanism allows you to execute a series of simultaneous ADC conversions by selecting more than one ADC for any CL-configured trigger. 

### 62.12.2 Configure MPC 

To configure a CL to perform MPC: 

1. Select CL for the trigger resolution (write 1 to TRGCFG_m[TRS]). 

2. Select more than one ADC for the trigger (TRGCFG_m[ADC_SELn]). 

3. Specify the CL address for the first CL element (TRGCFG_m[CHANNEL_VALUE_OR_LADDR]). 

### 62.12.3 CL address selection for MPC 

When the trigger input for the CL asserts, BCTU uses the Channel or List Address (CHANNEL_VALUE_OR_LADDR) as an index into the CL for the lowest numbered ADC selected (ADC_SELn), and each subsequent element of the CL for each remaining selected ADC. The set of selected ADC channels perform their conversions in parallel. When that set of conversions is complete, the next set of CL elements determine the next set of ADC channels to perform parallel conversions, as illustrated in: 

- Example: MPC with two ADCs 

- Example: MPC with three ADCs 

### 62.12.4 Example: MPC with two ADCs 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/062_Body_Cross-triggering_Unit_-BCTU-/S32K3XXRM_数据表.pdf-2274-15.png)


<!-- Start of picture text -->
TRGCFG<br>11 10 9 8 7 6 5 4 3 2 1 0<br>ADC_ ADC_<br>CHANNEL_VALUE_OR_LADDR<br>SEL1 SEL0<br>0 0 1 1<br>0 ADC channel num 0<br>List address = 1<br>1 ADC channel num 0 ADC0<br>Parallel<br>conversions<br>2 ADC channel num 0 ADC1<br>3 ADC channel num 0 ADC0<br>Parallel<br>conversions<br>4 ADC channel num 0 ADC1<br>5 ADC channel num 0 ADC0<br>Parallel<br>conversions<br>6 ADC channel num 0 ADC1<br>7 ADC channel num 1<br>8 ADC channel num 0<br>9 ADC channel num 0<br><!-- End of picture text -->

Figure 350. Example: MPC with two ADCs 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2274 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

### 62.12.5 Example: MPC with three ADCs 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/062_Body_Cross-triggering_Unit_-BCTU-/S32K3XXRM_数据表.pdf-2275-03.png)


<!-- Start of picture text -->
TRGCFG<br>11 10 9 8 7 6 5 4 3 2 1 0<br>ADC_ ADC_ ADC_<br>CHANNEL_VALUE_OR_LADDR<br>SEL2 SEL1 SEL0<br>0 1 1 1<br>List address = 0<br>0 ADC channel num 0 ADC0<br>Parallel<br>1 ADC channel num 0 ADC1<br>conversions<br>2 ADC channel num 0 ADC2<br>3 ADC channel num 0 ADC0<br>Parallel<br>4 ADC channel num 0 ADC1<br>conversions<br>5 ADC channel num 0 ADC2<br>6 ADC channel num 0<br>7 ADC channel num 1<br>8 ADC channel num 0<br>9 ADC channel num 0<br><!-- End of picture text -->

Figure 351. Example: MPC with three ADCs 

### 62.12.6 MPC priority rules 

MPC follows the same priority rules as for single conversions, which is based on the trigger input number: the lower the trigger, the higher the priority. However, MPC cannot start until all ADCs selected for the CL are available; that is, they are not currenlty engaged in conversion. For example, if a trigger input asserts for a CL using ADC0 and ADC1, BCTU does not initiate the CL until ADC0 and ADC1 are both available. 

Also, if ADC0 is available but there is a higher priority trigger for ADC1, the MPC does not start. If trigger inputs assert for two MPCs that have at least one ADC in common, the lower trigger number has higher priority. A priority conflict occurs only when separate requested CLs have at least one ADC in common. If the MPCs use different ADCs, there is no conflict and the MPCs execute at the same time. 

## 62.13 Interrupts and DMA requests 

Table 366. Interrupts and DMA requests 

|Event|Enable interrupt|Enable DMA<br>request|Description|
|---|---|---|---|
|Trigger Flag|MCR[TRGEN]|—|Interrupt request on assertion of Trigger Flag (MSR[TRGF])|
|ADC Data<br>Ready|MCR[IENn]|MCR[DMAn]|Interrupt or DMA request when ADC result data is available<br>(ADCnDR)|
|CL Last|MCR[LIST_IEN]|—|Interrupt request when the last conversion of any CL executes|
|FIFO<br>Watermark|FIFOCR[IEN_FI<br>FOn]|FIFOCR[DMA_<br>EN_FIFOn]|Interrupt or DMA request when the number of valid FIFO entries<br>exceeds the FIFO|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2275 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

## 62.14 BCTU register descriptions 

All BCTU registers are 32 bits wide. 8-bit write operations are allowed. The BCTU module does not include any coherence mechanism, so application software must ensure coherency. 

~~<mark>NOTE</mark>~~ 

- You must always write 0 to reserved writable registers and fields. Read accesses of reserved registers and fields do not return meaningful data. 

- For registers with write protection, if protection is active and you attempt to write to those registers, register content is unaffected and BCTU issues a transfer error. 

### 62.14.1 BCTU memory map 

BCTU base address: 4008_4000h 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|0h|Module Configuration (MCR)|32|RW|0000_0000h|
|8h|Module Status (MSR)|32|WORZ|0000_0000h|
|18h - 134h|Trigger Configuration (TRGCFG_0 - TRGCFG_71)|32|RW|0000_0000h|
|228h|Write Protection (WRPROT)|32|RW|0000_0000h|
|22Ch|Software Trigger 1 (SFTRGR1)|32|RW|0000_0000h|
|230h|Software Trigger 2 (SFTRGR2)|32|RW|0000_0000h|
|234h|Software Trigger 3 (SFTRGR3)|32|RW|0000_0000h|
|23Ch - 244h|ADCn Result Data (ADC0DR - ADC2DR)|32|RO|0000_0000h|
|24Ch|CL Size Status (LISTSTAR)|32|RO|0000_0020h|
|250h - 28Ch|CL Channel Address (LISTCHR_0 - LISTCHR_15)|32|RW|0000_0000h|
|450h - 454h|FIFO Result Data (FIFO1DR - FIFO2DR)|32|RO|0000_0000h|
|460h|FIFO Control (FIFOCR)|32|RW|0000_0000h|
|464h|FIFO Watermark Configuration (FIFOWM)|32|RW|0000_0000h|
|468h|FIFO Error/Status (FIFOERR)|32|W1C|0000_0000h|
|46Ch|FIFO Status (FIFOSR)|32|RO|0000_0000h|
|470h|FIFO Counter (FIFOCNTR)|32|RO|0000_0000h|



### 62.14.2 Module Configuration (MCR) 

#### Offset 

|Register|Offset|
|---|---|
|MCR|0h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2276 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

#### Function 

Configures the following aspects of BCTU behavior: 

- Low power 

- Debug 

- Trigger control 

- DMA control 

- Interrupt control 

Access: User read/write 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/062_Body_Cross-triggering_Unit_-BCTU-/S32K3XXRM_数据表.pdf-2277-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0 0<br>GTRG<br>Softwa MDIS  FRZ  EN  DMA2  DMA1  DMA0<br>W<br>r...<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 TRGE 0 LIST_ 0<br>IEN2  IEN1  IEN0<br>N  IEN<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31|Software Reset|
|Software_Reset|Asserts soft reset, which initializes all BCTU registers and internal state machines to their reset values.<br>0b - Deasserts<br>1b - Asserts|
|30<br>MDIS|Module Disable<br>Disables BCTU by putting it in Low Power state (seeModule Disable (Low Power state)).<br>0b - Enable (normal operation)<br>1b - Disable (low-power operation)|
|29|Debug Freeze|
|FRZ|Disables all hardware trigger inputs but leaves the software trigger enabled. Debug Freeze isolates<br>BCTU from external triggers and allows you to manually trigger a conversion and read the conversion<br>result.|
||0b - Disables<br>1b - Enables|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2277 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|28-27<br>—|Reserved|
|26|Global Trigger Enable|
|GTRGEN|Enables all individually enabled trigger inputs at the same time. For any given input trigger to be active, you<br>must both enable the individual trigger (TRGCFG_n[TRIGEN]) and Global Trigger Enable.<br>SeeConfigure all triggers.<br>0b - Disable<br>1b - Enable|
|25-19<br>—|Reserved|
|18-16<br>DMAn|Enable ADCnDR DMA<br>Enables DMA operation when new data is available inADCnDR.<br>0b - Disable<br>1b - Enable|
|15-8<br>—<br>7<br>TRGEN|Reserved<br>Trigger Interrupt Request Enable<br>Enables an interrupt request on a Trigger Flag (MSR[TRGF]).<br>0b - Disable<br>1b - Enable|
|6<br>—|Reserved|
|5<br>LIST_IEN|CL Interrupt Enable<br>Enables an interrupt request for the last conversion in a CL (bothADCnDR[LIST]andADCnDR[LAST]<br>are 1).<br>0b - Disable<br>1b - Enable|
|4-3<br>—|Reserved|
|2-0<br>IENn|Interrupt Enable For ADCnDR|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2278 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||Enables an interrupt request when BCTU writes a new conversion result to ADC Data (ADCnDR). Also<br>enables an interrupt request on an overrun in ADCnDR, which indicates the previous data has been<br>overwritten by a new conversion result. See also MSR[NDATAn] and MSR[DATAOVRn]].|
||Enabling ADCnDR DMA (DMAn field) disables the interrupt for new data in ADCnDR, but the interrupt for<br>ADCnDR data overrun remains enabled.|
||0b - Disable|
||1b - Enable|



### 62.14.3 Module Status (MSR) 

#### Offset 

|Register|Offset|
|---|---|
|MSR|8h|



#### Function 

Indicates the status of various BCTU functions, including: 

- Whether conversion data is available for each ADC 

- CL operation, such as the last conversion command executed in a CL 

- Whether BCTU triggered any of the ADCs 

All flag fields become 0 upon assertion of a low-power (software) or clock-stop (hardware) request. You can turn off individual flags by writing 1 to the field. 

Access: User read/write 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/062_Body_Cross-triggering_Unit_-BCTU-/S32K3XXRM_数据表.pdf-2279-15.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0 0 0 0 0 0 0 0 0 0 0 0<br>TRGF LIST2_ LIST1_ LIST0_ DATA DATA DATA NDAT NDAT NDAT<br>W<br>_CLR  L... L... L... OVR... OVR... OVR... A2_... A1_... A0_...<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>LIST2_ LIST1_ LIST0_ DATA DATA DATA NDAT NDAT NDAT<br>R TRGF  0 0 0<br>L... L... L... OVR2  OVR1  OVR0  A2  A1  A0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2279 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

#### Fields 

|Field|Function|
|---|---|
|31<br>TRGF_CLR|TRGF Clear<br>Changes Trigger Flag (TRGF) to 0.<br>0b - No action<br>1b - Changes to 0|
|30-27<br>—|Reserved|
|26-24<br>LISTn_Last_CL<br>R|CL n Last Clear<br>Changes CL n Last (LISTn_Last) to 0.<br>0b - No action<br>1b - Changes to 0|
|23<br>—|Reserved|
|22-20<br>DATAOVRn_CL<br>R|DATAOVRn Clear<br>Changes Data Overrun n (DATAOVRn) to 0.<br>0b - No action<br>1b - Changes to 0|
|19<br>—|Reserved|
|18-16<br>NDATAn_CLR|New Data Clear<br>Changes New Data n (NDATAn) to 0.<br>0b - No action<br>1b - Changes to 0|
|15<br>TRGF|Trigger Flag<br>Indicates at least one ADC was triggered.<br>0b - No ADC triggered<br>1b - An ADC was triggered|
|14-11<br>—|Reserved|
|10-8<br>LISTn_Last|CL n Last Conversion<br>Indicates that ADCn has executed the last conversion in a CL.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2280 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Last conversion not complete<br>1b - Last conversion complete|
|7<br>—<br>6-4|Reserved<br>Data Overrun n|
|DATAOVRn|Indicates that the data in ADCn has been overwritten with new data.<br>0b - Data not overwritten<br>1b - Data overwritten|
|3<br>—|Reserved|
|2-0<br>NDATAn|New Data n<br>Indicates that new conversion data is available for ADCn.<br>0b - Not available<br>1b - Available|



### 62.14.4 Trigger Configuration (TRGCFG_0 - TRGCFG_71) 

#### Offset 

For a = 0 to 71: 

|Register<br>TRGCFG_a|Offset<br>18h + (a × 4h)|
|---|---|



#### Function 

Configures the corresponding trigger: 

- Specifies the target ADC and ADC channel to use for conversion. 

- Specifies whether to use a CL or a single ADC conversion command. 

Access: User read/write 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2281 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/062_Body_Cross-triggering_Unit_-BCTU-/S32K3XXRM_数据表.pdf-2282-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0<br>LOOP  DATA_DEST<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>TRG_<br>R TRIGE FLAG  0 ADC_ ADC_ ADC_ 0<br>TRS  CHANNEL_VALUE_OR_LADDR<br>N  SEL2  SEL1  SEL0<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31|Loop|
|LOOP|Specifies that the current trigger executes in a loop; that is, the triggered conversion repeats until you<br>disable Loop. Each loop-triggered conversion wins the priority evaluation among all pending triggers, and<br>executes only if it is the highest-priority triggered conversion at the moment the conversion starts.<br>0b - Disable|
||1b - Enable|
|30-28|Data Destination|
|DATA_DEST|Specifies the destination for storing the conversion results. You can route each ADC's conversion result to<br>either of the following:<br>• ADC-specific data registers<br>• One of the available FIFOs<br>BCTU routes conversion results to different destinations based on the trigger index that requested the<br>conversion. You cannot duplicate the same data in more than one destination.<br>000b - ADC-specific data registers<br>001b - FIFO1|
||010b - FIFO2<br>011b - Reserved|
||All other values are reserved.|
|27-24<br>—<br>23-16<br>—|Reserved<br>Reserved|
|15|Trigger Enable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2282 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

#### Table continued from the previous page... 

|Field<br>TRIGEN|Function<br>Enables hardware input triggers to initiate ADC conversions. This field does not affect software triggers.<br>0b - Disable<br>1b - Enable|
|---|---|
|14<br>TRG_FLAG|Trigger Flag<br>Indicates the trigger input is asserted and an ADC conversion is in progress. When the conversion<br>completes, BCTU changes this field to 0. Writing 1 to this field causes the input trigger event to<br>clear when the in-progress conversion completes, and prevents this trigger from initiating a new ADC<br>conversion until the input trigger is asserted again.<br>This field behaves differently for read and write operations.<br>~~NOTE~~<br>When reading<br>0b - No ongoing ADC conversion initiated<br>1b - Ongoing ADC conversion initiated<br>When writing<br>0b - No action<br>1b - Changes to 0|
|13<br>TRS|Trigger Resolution<br>Selects single conversion or CL conversions.<br>0b - Single conversion<br>1b - CL conversions|
|12-11|Reserved|
|—<br>10-8<br>ADC_SELn|ADC Select n<br>Selects ADC n for conversion.<br>0b - Deselects<br>1b - Selects|
|7<br>—|Reserved|
|6-0|Channel or CL Address|
|CHANNEL_VAL<br>UE_OR_LADD<br>R|Depending on the value ofTRS:<br>• 0: Specifies the ADC channel for conversion<br>• 1: Specifies the address of the first CL position to execute|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2283 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

### 62.14.5 Write Protection (WRPROT) 

#### Offset 

|Register|Offset|
|---|---|
|WRPROT|228h|



#### Function 

Enables write protection at reset exit. To allow writes to protected registers, you must write a special code into PROTEC_CODE. There are two codes to remove protection: one that permanently disables the protection; one that disables protection during one write cycle to a protected register, after which the protection code returns to the initial (protected) value of 0000b. 

#### Access: User read/write 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/062_Body_Cross-triggering_Unit_-BCTU-/S32K3XXRM_数据表.pdf-2284-09.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>PROTEC_CODE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-4|Reserved|
|—||
|3-0|Protection Code|
|PROTEC_COD<br>E|Controls the protection of write-protected registers.<br>You can write this field only in Normal mode (MCR[MDIS]is 0).<br>~~NOTE~~|
||0000b - Enable protection|
||1001b - Disable protection for one write cycle|
||1010b - Disable protection permanently|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2284 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

### 62.14.6 Software Trigger 1 (SFTRGR1) 

#### Offset 

|Register|Offset|
|---|---|
|SFTRGR1|22Ch|



#### Function 

Allows you to trigger conversions on the associated triggers. 

To use a software trigger, you must first disable the corresponding hardware trigger (TRGCFG_x[TRIGEN]). 

BCTU writes 0 to a software trigger field on completion of the triggered conversion. 

Access: User read/write; this register is write protected by Write Protection (WRPROT). If protection is enabled, writes to this register generate a transfer error and do not modify its content. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|SFTR<br>G31|SFTR<br>G30|SFTR<br>G29|SFTR<br>G28|SFTR<br>G27|SFTR<br>G26|SFTR<br>G25|SFTR<br>G24|SFTR<br>G23|SFTR<br>G22|SFTR<br>G21|SFTR<br>G20|SFTR<br>G19|SFTR<br>G18|SFTR<br>G17|SFTR<br>G16|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|SFTR<br>G15|SFTR<br>G14|SFTR<br>G13|SFTR<br>G12|SFTR<br>G11|SFTR<br>G10|SFTR<br>G9|SFTR<br>G8|SFTR<br>G7|SFTR<br>G6|SFTR<br>G5|SFTR<br>G4|SFTR<br>G3|SFTR<br>G2|SFTR<br>G1|SFTR<br>G0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-0|Software Trigger m|
|SFTRGm|Starts an ADC conversion.|
||0b - No effect|
||1b - Trigger conversion|



### 62.14.7 Software Trigger 2 (SFTRGR2) 

#### Offset 

|Register|Offset|
|---|---|
|SFTRGR2|230h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2285 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

#### Function 

Allows you to trigger conversions on the associated triggers. 

To use a software trigger, you must first disable the corresponding hardware trigger (TRGCFG_n[TRIGEN]). 

BCTU writes 0 to a software trigger field on completion of the triggered conversion. 

Access: User read/write; this register is write protected by Write Protection (WRPROT). If protection is enabled, writes to this register generate a transfer error and do not modify its content. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/062_Body_Cross-triggering_Unit_-BCTU-/S32K3XXRM_数据表.pdf-2286-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R SFTR SFTR SFTR SFTR SFTR SFTR SFTR SFTR SFTR SFTR SFTR SFTR SFTR SFTR SFTR SFTR<br>W G63  G62  G61  G60  G59  G58  G57  G56  G55  G54  G53  G52  G51  G50  G49  G48<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R SFTR SFTR SFTR SFTR SFTR SFTR SFTR SFTR SFTR SFTR SFTR SFTR SFTR SFTR SFTR SFTR<br>W G47  G46  G45  G44  G43  G42  G41  G40  G39  G38  G37  G36  G35  G34  G33  G32<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-0|Software Trigger m|
|SFTRGm|Starts an ADC conversion.|
||0b - No effect|
||1b - Trigger conversion|



### 62.14.8 Software Trigger 3 (SFTRGR3) 

#### Offset 

|Register|Offset|
|---|---|
|SFTRGR3|234h|



#### Function 

Allows you to trigger conversions on the associated triggers. 

To use a software trigger, you must first disable the corresponding hardware trigger (TRGCFG_n[TRIGEN]). 

BCTU writes 0 to a software trigger field on completion of the triggered conversion. 

Access: User read/write; this register is write protected by Write Protection (WRPROT). If protection is enabled, writes to this register generate a transfer error and do not modify its content. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2286 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||||0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||0|||||SFTR|SFTR|SFTR|SFTR|SFTR|SFTR|SFTR|SFTR|
|W|||||||||G71|G70|G69|G68|G67|G66|G65|G64|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-8<br>—|Reserved|
|7-0|Software Trigger m|
|SFTRGm|Starts an ADC conversion.|
||0b - No effect|
||1b - Trigger conversion|



### 62.14.9 ADCn Result Data (ADC0DR - ADC2DR) 

#### Offset 

|Register|Offset|
|---|---|
|ADC0DR|23Ch|
|ADC1DR|240h|
|ADC2DR|244h|



#### Function 

Provides ADC conversion result data. Also indicates the ADC channel used in that conversion, the trigger source that initiated it, and whether conversion was initiated from a CL. 

Access: User read 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2287 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||TRG_SRC|||||||CH||||LIST|LAST|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|0|||||||A|DC_DATA||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-25|Trigger Source|
|TRG_SRC|Contains the trigger number used to trigger the conversion.|
|24-18|Channel|
|CH|Contains the ADC channel used for the conversion.|
|17<br>LIST|List<br>Indicates whether the conversion was part of a CL or a single conversion trigger.<br>0b - Single conversion<br>1b - CL|
|16<br>LAST|Last<br>For CL conversions, indicates this conversion result is the last conversion of the CL.<br>0b - Not the last conversion of a CL, or not a CL conversion<br>1b - Last conversion of a CL|
|15<br>—|Reserved|
|14-0|ADC Data|
|ADC_DATA|Contains the data from the conversion.|



### 62.14.10 CL Size Status (LISTSTAR) 

#### Offset 

|Register|Offset|
|---|---|
|LISTSTAR|24Ch|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2288 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

#### Function 

Indicates the size of the CL. Each element of the CL contains the channel number used in one conversion. Access: User read 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/062_Body_Cross-triggering_Unit_-BCTU-/S32K3XXRM_数据表.pdf-2289-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 LISTSZ<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-8<br>—|Reserved|
|7-0|CL Size|
|LISTSZ|Indicates the size of the CL in number of elements.|



### 62.14.11 CL Channel Address (LISTCHR_0 - LISTCHR_15) 

#### Offset 

For m = 0 to 15: 

|Register|Offset|
|---|---|
|LISTCHR_m|250h + (m × 4h)|



#### Function 

Configures these attributes for two CL elements: 

- ADC channel number to use for conversion 

- Whether the element is the last element of a CL 

Access: User read/write 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2289 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/062_Body_Cross-triggering_Unit_-BCTU-/S32K3XXRM_数据表.pdf-2290-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R LAST_ NEXT_ 0 0 0<br>ADC_CH_y<br>W y  CH...<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R LAST_ NEXT_ 0 0 0<br>ADC_CHL_y_plus_1<br>W y_... CH...<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31<br>LAST_y|Last Channel<br>Specifies this element as the last channel in the CL.<br>0b - Not last<br>1b - Last channel in CL|
|30<br>NEXT_CH_WAI<br>T_ON_TRIG_y|Next Channel Wait For Trigger<br>Instructs CL execution to stop after executing the current ADC channel. Execution begins again when<br>the same trigger, which started the CL, reoccurs.<br>If this is the last channel in the CL (LAST_y), you must write 0 to this field.<br>~~NOTE~~<br>0b - CL executes continuously<br>1b - CL stops executing|
|29-28<br>—|Reserved|
|27-24<br>—|Reserved|
|23<br>—|Reserved|
|22-16<br>ADC_CH_y|ADC Channel Selection<br>Specifies the ADC channel to use for the y element of the CL, where y equals (2 x m).|
|15|Last Channel Plus 1|
|LAST_y_plus_1|Specifies this element as the next-to-last channel in the CL.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2290 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Not next-to-last<br>1b - Next-to-last channel in CL|
|14<br>NEXT_CH_WAI<br>T_ON_TRIG_y_<br>plus_1|Next Channel Wait For Trigger Plus 1<br>Instructs CL execution to stop after executing the current ADC channel. Execution begins again when<br>the same trigger, which started the CL, reoccurs.<br>If this is the last channel in the CL (LAST_y_plus_1), you must write 0 to this field.<br>~~NOTE~~<br>0b - CL executes continuously<br>1b - CL stops executing|
|13-12<br>—|Reserved|
|11-8<br>—|Reserved|
|7<br>—|Reserved|
|6-0|ADC Channel Selection Plus 1|
|ADC_CHL_y_pl<br>us_1|Specifies the ADC channel to use for the (y + 1) element of the CL, where y equals (2 x m).|



### 62.14.12 FIFO Result Data (FIFO1DR - FIFO2DR) 

#### Offset 

|Register|Offset|
|---|---|
|FIFO1DR|450h|
|FIFO2DR|454h|



#### Function 

Contains the ADC conversion result and information about the conversion: 

- ADC channel 

- Trigger source 

- ADC number 

Access: User read 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2291 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||TRG_SRC|||||||CH||||ADC|_NUM|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|0|||||||A|DC_DATA||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-25|Trigger Source|
|TRG_SRC|Indicates the trigger number used to trigger the conversion.|
|24-18|Channel|
|CH|Indicates the ADC channel used for the conversion.|
|17-16|ADC Number|
|ADC_NUM|Indicates the ADC used for conversion.<br>00b - ADC 0|
||01b - ADC 1|
||10b - ADC 2|
||11b - ADC 3|
|15<br>—|Reserved|
|14-0|ADC Data|
|ADC_DATA|Contains the conversion data.|



### 62.14.13 FIFO Control (FIFOCR) 

#### Offset 

|Register|Offset|
|---|---|
|FIFOCR|460h|



#### Function 

Provides control of FIFO-specific DMA, interrupts, and error interrupts. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2292 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

#### Access: User read/write 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||0|||0|0|DMA_|DMA_||0|||0|0|IEN_FI|IEN_FI|
|W|||||||EN_...|EN_...|||||||F...|F...|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-28|Reserved|
|—||
|27|Reserved|
|—<br>26|Reserved|
|—<br>25-24|FIFOn DMA Enable|
|DMA_EN_FIFO<br>n|Enables a DMA request when the number of valid FIFO entries is greater than the watermark level for<br>that FIFO.<br>0b - Disable|
||1b - Enable|
|23-20<br>—|Reserved|
|19<br>—|Reserved|
|18<br>—|Reserved|
|17-16<br>IEN_FIFOn|FIFOn Interrupt Enable<br>Enables an interrupt request if the number of valid FIFO entries is greater than the watermark level for<br>the FIFO.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2293 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Disable|
||1b - Enable|
|15-0<br>—|Reserved|



### 62.14.14 FIFO Watermark Configuration (FIFOWM) 

#### Offset 

|Register|Offset|
|---|---|
|FIFOWM|464h|



#### Function 

Specifies the FIFO watermark levels. If the number of active FIFO entries exceeds the watermark level, a DMA or interrupt request can be generated. See FIFO Control (FIFOCR). 

Access: User read/write 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/062_Body_Cross-triggering_Unit_-BCTU-/S32K3XXRM_数据表.pdf-2294-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>WM_FIFO2  WM_FIFO1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-24<br>—|Reserved|
|23-16<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2294 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|15-11<br>—|Reserved|
|10-8|FIFO2 Watermark Level|
|WM_FIFO2|Specifies the watermark level for FIFO2.|
|7-4<br>—|Reserved|
|3-0|FIFO1 Watermark Level|
|WM_FIFO1|Specifies the watermark level for FIFO1.|



### 62.14.15 FIFO Error/Status (FIFOERR) 

#### Offset 

|Register|Offset|
|---|---|
|FIFOERR|468h|



#### Function 

Allows you to clear FIFO error and status flags. Each FIFO has its own error and status flags that can be configured to generate an interrupt. FIFO Status (FIFOSR) maintains the status of these flags. BCTU writes a 1 to these flags, and you must then clear them using FIFOERR. 

#### Access: User read/write 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/062_Body_Cross-triggering_Unit_-BCTU-/S32K3XXRM_数据表.pdf-2295-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>UNDR OVR_ UNDR OVR_ WM_I WM_I<br>R 0 0 0 0<br>_ER... ERR... _ER... ERR... NT_... NT_...<br>W W1C W1C W1C W1C W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2295 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

#### Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29-28<br>—|Reserved|
|27<br>UNDR_ERR_FI<br>FO2|Underrun Error Flag<br>Indicates you have attempted to read from an empty FIFO.<br>0b - No underrun<br>1b - Underrun|
|26<br>OVR_ERR_FIF<br>O2|Overrun Error Flag<br>Indicates you have attempted to write to a full FIFO.<br>0b - No overrun<br>1b - Overrun|
|25<br>UNDR_ERR_FI<br>FO1|Underrun Error Flag<br>Indicates you have attempted to read from an empty FIFO.<br>0b - No underrun<br>1b - Underrun|
|24<br>OVR_ERR_FIF<br>O1|Overrun Error Flag<br>Indicates you have attempted to write to a full FIFO.<br>0b - No overrun<br>1b - Overrun|
|23-20<br>—|Reserved|
|19-18<br>—|Reserved|
|17-16<br>WM_INT_FIFOn|FIFO Watermark Interrupt Status<br>Indicates the number of active entries in FIFOn exceeds the watermark level.<br>0b - Does not exceed watermark<br>1b - Exceeds watermark|
|15-0<br>—|Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2296 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

### 62.14.16 FIFO Status (FIFOSR) 

#### Offset 

|Register|Offset|
|---|---|
|FIFOSR|46Ch|



#### Function 

#### Contains the FIFO-full flags. 

Access: User read 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/062_Body_Cross-triggering_Unit_-BCTU-/S32K3XXRM_数据表.pdf-2297-09.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>FULL_ FULL_<br>R 0<br>FI... FI...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-2<br>—|Reserved|
|1-0|FIFO Full|
|FULL_FIFOn|Indicates the FIFO is full.|
||0b - Not full|
||1b - Full|



### 62.14.17 FIFO Counter (FIFOCNTR) 

#### Offset 

|Register|Offset|
|---|---|
|FIFOCNTR|470h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2297 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

#### Function 

Indicates the number of active entries in each FIFO. 

Access: User read 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||0|||||||0|||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||0||||CNTR_|FIFO2|||0|||CN|TR_FIFO|1||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-24<br>—|Reserved|
|23-16<br>—|Reserved|
|15-12<br>—|Reserved|
|11-8|FIFO2 Counter|
|CNTR_FIFO2|Indicates the number of active entries in FIFO2.|
|7-5<br>—|Reserved|
|4-0|FIFO1 Counter|
|CNTR_FIFO1|Indicates the number of active entries in FIFO1.|



## 62.15 Glossary 

CL Conversion list. The set of ADC channels, configured through the CL Channel Address (LISTCHR_0 - LISTCHR_15) registers, used for performing multiple sequential conversions initiated by a single trigger. 

MPC Multiple parallel conversions PSI Parallel side interface RWB Read/write bus 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2298 / 4640 

NXP Semiconductors 

Body Cross-triggering Unit (BCTU) 

#### WDATA Write Data bus 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2299 / 4640 

