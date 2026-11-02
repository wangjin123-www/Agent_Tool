NXP Semiconductors 

# Chapter 14 Enhanced Direct Memory Access (eDMA) 

## 14.1 Chip-specific eDMA information 

### 14.1.1 DMA channels 

See the following table for number of DMA channels across S32K3xx product series. 

Table 45. DMA channels 

|Chip|No. of DMA channels|
|---|---|
|S32K322/S32K342/S32K314/S32K324/S32K344|32|
|S32K311/S32K312|12|



~~<mark>NOTE</mark>~~ 

TCD_CH[12-31] are not available in K312, so the registers corresponding to these channels are not available in K312 variant. See the memory map file attached to this document for details. 

## 14.2 Overview 

The enhanced direct memory access (eDMA) controller is capable of performing complex data transfers with minimal intervention from a host processor. The hardware microarchitecture includes: 

- A DMA engine that performs: 

   - Source address and destination address calculations 

   - Data-movement operations 

- Local memory containing transfer control descriptors for each of the 32 channels 

### 14.2.1 Block diagram 

Figure 27 illustrates the components of the eDMA system, including the eDMA module (engine). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

405 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0406-01.png)


<!-- Start of picture text -->
Enhanced Direct Memory Access (eDMA)<br>eDMA system<br>Write Address<br>Write Data<br>0<br>1<br>2<br>Transfer Control<br>Descriptor (TCD)<br>n-1<br>64<br>eDMA Engine Read Data<br>Program Model/<br>Channel Arbitration<br>Read Data<br>Address Path<br>Control<br>Data Path<br>Write Data<br>Address<br>eDMA eDMA<br>Peripheral Done<br>Request<br>Figure 27. Block diagram<br>Internal Peripheral Bus<br>To/from interconnect fabric<br><!-- End of picture text -->

### 14.2.2 Block parts 

The eDMA module is partitioned into two major modules: the eDMA engine and the transfer control descriptor local memory. The eDMA engine is further partitioned into four submodules: 

Table 46. eDMA engine submodules 

|Submodule|Function|
|---|---|
|Address path|This block:|
||• Implements a primary channel and secondary (preempt) channel<br>• Manages all master bus-address calculations<br>All the channels provide the same functionality. This structure allows data transfers associated<br>with one channel to be preempted after the completion of a read/write sequence if a higher priority<br>channel activation is asserted while the primary channel is active.<br>After a channel is activated, it runs until the minor loop is completed, unless preempted by a<br>higher priority channel. This provides a mechanism (enabled by CHn_PRI[ECP]) where a large data<br>transfer can be preempted to minimize the time another channel is blocked from execution.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

406 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

Table 46. eDMA engine submodules (continued) 

|Submodule|Function|
|---|---|
||When any channel is selected to execute, the contents of itsTCDare read from local memory and<br>loaded into the address path channel x registers for a normal start and into channel y registers for<br>a preemption start. After the minor loop completes execution, the address path hardware writes the<br>new values for the TCDn_{SADDR, DADDR, CITER} back to local memory. If the major iteration<br>count is exhausted, additional processing is performed, including the final address pointer updates,<br>reloading the TCDn_CITER field, and a possible fetch of a new TCDn from memory as part of a<br>scatter/gather operation. SeeDynamic scatter/gatherfor more details.|
|Data path|This block implements the bus master read/write data path. It includes a data buffer and the<br>necessary multiplex logic to support any required data alignment. The internal read data bus is the<br>primary input, and the internal write data bus is the primary output.<br>The address and data path modules directly support the 2-stage pipelined internal bus. The address<br>path module represents the first stage of the bus pipeline (address phase), and the data path module<br>implements the second stage of the pipeline (data phase).|
|Program model/channel<br>arbitration|This block implements the first section of the eDMA programming model as well as the channel<br>arbitration logic. The programming model registers are connected to the internal peripheral bus.<br>The eDMA peripheral request inputs and interrupt request outputs are also connected to this<br>block (via control logic).|
|Control|This block provides all the control functions for the eDMA engine. For data transfers where<br>the source and destination sizes are equal, the eDMA engine performs a series of source read/<br>destination write operations until the number of bytes specified in the minor loop byte count has been<br>moved from the source to the destination.<br>For descriptors where the sizes are not equal, multiple accesses of the smaller size data are required<br>for each reference of the larger size. As an example, if the source size references 16-bit data and<br>the destination is 32-bit data, the eDMA performs two reads, then one 32-bit write.|



The transfer control descriptor local memory is further partitioned into: 

Table 47. Transfer control descriptor memory 

|Submodule|Description|
|---|---|
|Memory controller|This logic implements the required dual-ported controller, and manages accesses from the eDMA<br>engine as well as references from the internal peripheral bus. As noted earlier, in simultaneous<br>accesses, the eDMA engine is given priority and the peripheral transaction is stalled.|
|Memory array|TCD storage for each channel's transfer profile.|



### 14.2.3 Features 

The eDMA is a highly programmable data-transfer engine optimized to minimize any required intervention from the host processor. It is intended for use in applications where the data size to be transferred is statically known and not defined within the transferred data itself. The eDMA module features: 

- All data movement via dual-address transfers: read from source, write to destination 

   - Programmable source and destination addresses and transfer size 

   - Support for complex address calculations 

- Implementation that performs complex data transfers with minimal intervention from a host processor 

   - Internal data buffer, used as temporary storage for all transfers 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

407 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

   - Connections to the crossbar switch for bus mastering the data movement 

- TCD organized to support two-deep, nested transfer operations 

   - 32-byte TCD stored in local memory for each channel 

   - An inner data transfer loop defined by a minor byte transfer count 

   - An outer data transfer loop defined by a major iteration count 

- Channel activation via one of three methods: 

   - Explicit software initiation 

   - Initiation via a channel-to-channel linking mechanism for continuous transfers 

   - Peripheral-paced hardware requests, one per channel 

- Fixed-priority and round-robin channel arbitration 

- Channel completion reported via programmable interrupt requests 

   - One interrupt per channel, which can be asserted at completion of major iteration count 

   - Programmable error terminations per channel that are logically summed together to form one error interrupt to the interrupt controller 

- Programmable support for scatter/gather DMA processing 

- Support for complex data structures 

In the discussion of this module, n is used to reference the channel number. 

## 14.3 Functional description 

The operation of eDMA is described in the following subsections. 

### 14.3.1 Modes of operation 

The eDMA operates in the following modes: 

Table 48. Modes of operation 

|Mode|Description|
|---|---|
|Normal|In Normal mode, eDMA transfers data between a source and a destination. The source and<br>destination can be a memory block or an I/O block capable of operation with eDMA.<br>A service request initiates a transfer of a specific number of bytes (NBYTES) as specified in the TCD.<br>The minor loop is the sequence of read-write operations that transfers these NBYTES per service<br>request. Each service request executes one iteration of the major loop, which transfers NBYTES<br>of data.|
|Debug|eDMA operation is configurable in Debug mode via the control register:<br>• If CSR[EDBG] is cleared to 0, eDMA continues to operate.<br>• If CSR[EDBG] is set to 1, eDMA stops transferring data. If Debug mode is entered when a<br>channel is active, eDMA continues operation until the channel retires.|



### 14.3.2 eDMA basic data flow 

The basic flow of a data transfer can be partitioned into three segments. 

As shown in the following diagram, the first segment involves the channel activation: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

408 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0409-02.png)


<!-- Start of picture text -->
eDMA<br>Write address<br>Write data<br>0<br>1<br>2<br>Transfer control<br>descriptor (TCD)<br>n-1<br>64<br>eDMA engine Read data<br>Program model/<br>channel arbitration<br>Read data<br>Address path<br>Control<br>Data path<br>Write data<br>Address<br>eDMA eDMA<br>peripheral done<br>request<br>Internal peripheral bus<br>To/from crossbar switch<br><!-- End of picture text -->

Figure 28. eDMA operation, part 1 

This example uses the assertion of the eDMA peripheral request signal to request service for channel n. Channel activation via software and the TCDn_CSR[START] field follows the same basic flow as peripheral requests. The eDMA request input signal is registered internally and then routed through the eDMA engine: first through the control module, then into the program model and channel arbitration. 

In the next cycle, the channel arbitration begins using fixed-priority plus the optional round-robin algorithm. After arbitration is complete, the activated channel number is sent through the address path and converted into the required address to access the local memory for TCDn. Next, the TCD memory is accessed and the required descriptor is read from the local memory and then loaded into the eDMA engine address path's primary or secondary channel execution registers. The TCD memory is 64 bits wide to minimize the time needed to fetch the activated channel descriptor and load it into the address path registers. 

The following diagram illustrates the second part of the basic data flow: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

409 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0410-02.png)


<!-- Start of picture text -->
eDMA<br>Write address<br>Write data<br>0<br>1<br>2<br>Transfer control<br>descriptor (TCD)<br>n-1<br>64<br>eDMA engine Read data<br>Program model/<br>channel arbitration<br>Read data<br>Address path<br>Control<br>Data path<br>Write data<br>Address<br>eDMA eDMA<br>peripheral done<br>request<br>Internal peripheral bus<br>To/from crossbar switch<br><!-- End of picture text -->

Figure 29. eDMA operation, part 2 

The modules associated with the data transfer (address path, data path, and control) go through the required sequence of source reads and destination writes to perform the actual data movement. The source reads are initiated, and the fetched data is temporarily stored in the data path block until it is gated onto the internal bus during the destination write. This source read/destination write processing continues until the byte count, NBYTES, has been transferred. 

After NBYTES of data has been moved, the final phase of the basic data flow is performed. In this segment, the address path logic performs the required updates to certain fields in the appropriate TCD (for example, SADDR, DADDR, CITER). If the major iteration count is exhausted, additional operations are performed. These include the final address adjustments and reloading of the BITER field into the CITER field. Assertion of an optional interrupt request also occurs at this time, as does a possible fetch of a new TCD from memory using the scatter/gather address pointer included in the descriptor (if scatter/gather is enabled). The updates to the TCD memory and the assertion of an interrupt request are shown in the following diagram. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

410 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0411-02.png)


<!-- Start of picture text -->
eDMA<br>Write address<br>Write data<br>0<br>1<br>2<br>Transfer control<br>descriptor (TCD)<br>n-1<br>64<br>eDMA engine Read data<br>Program model/<br>channel arbitration<br>Read data<br>Address path<br>Control<br>Data path<br>Write data<br>Address<br>eDMA eDMA<br>peripheral done<br>request<br>Internal peripheral bus<br>To/from crossbar switch<br><!-- End of picture text -->

Figure 30. eDMA operation, part 3 

### 14.3.3 Fault reporting and handling 

Channel errors are reported in the Error Status register (CHn_ES) and can be caused by any of the following: 

- A configuration error, which is an illegal setting in the transfer control descriptor 

- An active channel canceled via a "cancel transfer with error" hardware or software request 

- A TCD memory error 

- An error termination to a bus master read or write cycle 

A configuration error is reported when an inconsistent state is represented by one of these factors: 

- Starting source or destination address 

- Source or destination offsets 

- Minor loop byte count 

- Transfer size 

Each of these possible causes is detailed below: 

- The addresses and offsets must be aligned on zero-modulo-transfer-sized boundaries. 

- The minor loop byte count must be a multiple of the source and destination transfer sizes. 

- All source reads and destination writes must be configured to the natural boundary of the programmed transfer size. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

411 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

~~<mark>NOTE</mark>~~ 

To aid in debugging, set the Halt After Error field in the DMA’s Control Status register, CSR[HAE]. Upon any error condition, the DMA is halted after the error is recorded. The DMA remains halted and does not process any channel service requests. After the error is fixed, the DMA may be enabled again by clearing the Halt field, CSR[HALT]. 

- If a scatter/gather operation is enabled upon channel completion, a configuration error is reported if the scatter/gather address (TCDn_DLAST_SGA) is not aligned on a 32-byte boundary. 

- If minor loop channel linking is enabled upon channel completion, a configuration error is reported when the link is attempted if the TCDn_CITER[ELINK] field does not equal the TCDn_BITER[ELINK] field. 

If enabled, all configuration error conditions, except the scatter/gather and minor-loop link errors, are reported as the channel activates and asserts an error interrupt request. A scatter/gather configuration error is reported when the scatter/gather operation begins at major loop completion if properly enabled. A minor loop channel link configuration error is reported when the link operation is serviced at minor loop completion. 

If a system bus read or write is terminated with an error, the data transfer is stopped and the appropriate bus error flag set. In this case, the state of the channel's transfer control descriptor is updated by the eDMA engine with the current source address, destination address, and current iteration count at the point of the fault. When a system bus error occurs, the channel terminates after the next transfer. Due to pipeline effect, the next transfer is already in progress when the bus error is received by the eDMA. If a bus error occurs on the last read prior to beginning the write sequence, the write executes using the data captured during the bus error. If a bus error occurs on the last write prior to switching to the next read sequence, the read sequence executes before the channel terminates due to the destination bus error. 

The occurrence of any error causes the eDMA engine to stop normal processing of the active channel immediately (it goes to its error processing states and the transaction to the system bus still has pipeline effect), and the appropriate channel field in the eDMA error register is set to 1. At the same time, the details of the error condition are loaded into the Error Status register (CHn_ES). The major loop complete indicators, setting the transfer control descriptor DONE flag, and the possible assertion of an interrupt request are not affected when an error is detected. 

After the error status has been updated, the eDMA engine continues operating by servicing the next appropriate channel. A channel that experiences an error condition is not automatically disabled. If a channel is terminated by an error and then issues another service request before the error is fixed, that channel executes and terminates with the same error condition. 

The error status fields are read-only. These error indicators are sticky and cannot be cleared. They show the last recorded error until the DMA is reset. The valid field (VLD) is used to determine if a new error condition exists. This field is the logical OR of each channel's error interrupt field (ERR). 

After the software has resolved any errors and cleared all of the error interrupt fields, the valid field is cleared to 0 but the cause of the last error is still indicated. 

### 14.3.4 Channel preemption 

The eDMA uses a priority vector value to determine the highest priority channel requesting service. 

The priority vector is a combination of: 

1. the channel's group priority, CHn_GRPRI 

2. the channel's priority level, CHn_PRI[APL] 

3. the channel number 

Priority vector = ((CHn_GRPRI << 8) + (CHn_PRI[APL] << 5 ) + CHn_*) 

A channel requesting service with the highest priority vector value will receive the next execution slot. 

An execution slot is available: 

1. immediately if the eDMA is idle 

2. when an active channel retires 

3. when valid preemption conditions exist 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

412 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

~~<mark>NOTE</mark>~~ 

Preemption is strictly priority based. Preemption is not bound by a specific group number as defined by CHn_GRPRI. 

Channel preemption is enabled on a per-channel basis by setting the CHn_PRI[ECP] field. Channel preemption allows the executing channel’s data transfers to temporarily suspend in favor of starting a higher-priority channel. After the preempting channel has completed all of its minor loop data transfers, the preempted channel is restored and resumes execution. 

After the restored channel completes one read/write sequence, it is again eligible for preemption. If any higher priority channel is requesting service, the restored channel is suspended, and the higher-priority channel is serviced. Nested preemption, that is, attempting to preempt a preempting channel, is not supported. After a preempting channel begins execution, it cannot be preempted. 

A channel’s ability to preempt another channel can be disabled by setting CHn_PRI[DPA] to 1. When a channel’s preempt ability is disabled, that channel cannot suspend a lower-priority channel’s data transfer, regardless of the lower-priority channel’s ECP setting. This allows for a pool of low-priority, large-data-moving channels to be defined. 

You can configure these low-priority channels to not preempt each other, thus preventing a low-priority channel from consuming the preempt slot normally available to a true high-priority channel. When you enable round-robin channel arbitration mode (CSR[ERCA] is set to 1), any channel with a priority level equal to 0 (CHn_PRI[APL] = 0) has preemption disabled and cannot preempt another channel. 

## 14.4 Initialization/application information 

The following sections discuss initialization of the eDMA and programming considerations. 

### 14.4.1 eDMA initialization 

To initialize the eDMA: 

1. Write to the CSR if a configuration other than the default is wanted. 

2. Write the channel priority levels to the CHn_PRI registers and group priority levels to the CHn_GRPRI registers if a configuration other than the default is wanted. 

3. Enable error interrupts in the CHn_CSR[EEI] registers if they are wanted. 

4. Write the 32-byte TCD for each channel that may request service. 

5. Enable any hardware service requests via the CHn_CSR[ERQ] registers. 

6. Request channel service via either: 

   - Software: setting TCDn_CSR[START] 

   - Hardware: slave device asserting its eDMA peripheral request signal 

After any channel requests service, a channel is selected for execution based on the arbitration and priority levels written into the programmer's model. The eDMA engine reads the entire TCD, including the TCD control and status fields, as shown in Table 49, for the selected channel into its internal address path module. 

As the TCD is read, the first transfer is initiated on the internal bus, unless a configuration error is detected. Transfers from the source, defined by TCDn_SADDR, to the destination, defined by TCD_DADDR, continue until the number of bytes specified by TCDn_NBYTES are transferred. 

When the transfer is complete, the eDMA engine's local TCDn_SADDR, TCDn_DADDR, and TCDn_CITER are written back to the main TCD memory and any minor loop channel linking is performed, if enabled. If the major loop is exhausted, then eDMA executes further post-processing, such as interrupts, major loop channel linking, and scatter/gather operations, if enabled. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

413 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

Table 49. TCD control and status (TCDn_CSR) fields 

|TCDn_CSRfield name|Description|
|---|---|
|START|Control field to start the channel explicitly when using a software-initiated DMA service (automatically<br>cleared by hardware)|
|ESDA|Control field to enable storing of the destination address to system memory after the major loop<br>completes|
|DREQ|Control field to disable hardware-initiated DMA service requests after major loop completion|
|BWC|Control field for throttling the bandwidth control of a channel|
|ESG|Control field to enable the scatter-gather feature|
|INTHALF|Control field to enable interrupt when major loop is half-complete|
|INTMAJOR|Control field to enable interrupt when major loop completes|



Table 50. Channel control and status (CHn_CSR) fields 

|CHn_CSRfield name|Description|
|---|---|
|ACTIVE|Status field indicating the channel is currently in execution|
|DONE|Status field indicating major loop completion (cleared by software when a channel begins execution)|
|EEI|Control field to enable error interrupts|
|EARQ|Control field to enable external, asynchronous wakeup event in conjunction with the ERQ field|
|ERQ|Control field to enable hardware service requests|



The following figure shows how each DMA request initiates one minor-loop transfer, or iteration, without CPU intervention. DMA arbitration can occur after each minor loop, and one level of minor loop DMA preemption is allowed. The number of minor loops in a major loop is specified by the beginning iteration count (BITER). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

414 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0415-02.png)


<!-- Start of picture text -->
Current major<br>loop iteration<br>Source or destination memory count (CITER)<br>DMA request<br>• Minor loop 3<br>•<br>•<br>DMA request<br>• Minor loop Major loop 2<br>•<br>•<br>DMA request<br>• Minor loop 1<br>•<br>•<br><!-- End of picture text -->

Figure 31. Example of multiple loop iterations 

The following figure lists the memory array terms and how the TCD settings are related. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0415-05.png)


<!-- Start of picture text -->
xADDR: (starting address) xSIZE: (size of one<br>data transfer) Minor loop<br>(NBYTES in<br>• minor loop, Offset (xOFF): number of bytes added to<br>• often the same current address after each transfer<br>• value as xSIZE) (often the same value as xSIZE)<br>Each DMA source (S) and<br>•• •• destination (D) has its own:Address (xADDR)<br>• • Size (xSIZE)<br>• • Minor loop Offset (xOFF)<br>• • Modulo (xMOD)<br>• • Last Address Adjustment (xLAST)<br>where x = S or D<br>Peripheral queues typically<br>•• Last minor loop to NBYTEShave size and offset equal<br>•<br>xLAST: Number of bytes added to<br>current address after major loop<br>(typically used to loop back)<br><!-- End of picture text -->

Figure 32. Memory array terms 

### 14.4.2 eDMA arbitration 

The eDMA uses a layered arbitration scheme composed of multiple priority levels. The eDMA uses a fixed-priority arbitration scheme with optional round-robin arbitration under specific conditions. The priorities are evaluated in the following order: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

415 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

Table 51. eDMA arbitration priorities 

|Priority|Scheme|Description|
|---|---|---|
|1 (Highest)|Arbitration group priority|Each channel is assigned an arbitration<br>group via theCHn_GRPRIregisters.<br>Priority is given to the highest value (31<br>being the highest possible value) down to<br>the lowest value (zero, the default).|
|2|Channel priority|Each channel is assigned a channel<br>priority level via theCHn_PRIregisters.<br>The channel priority is a relative priority<br>level within an arbitration group. Priority<br>is given to the highest value (seven being<br>the highest possible value) down to the<br>lowest value (zero, the default). Channel<br>priorities within each arbitration group<br>need not be unique. If multiple channels<br>have the same channel priority level, the<br>channel number will be used to determine<br>priority as defined in row three.|
|3|Channel number|When two or more channels have<br>the same arbitration group priority and<br>channel priority, the channel number<br>(CHn_NUM) is used to determine the<br>highest priority. Priority is giver to the<br>highest channel number. Lowest priority<br>is channel 0. The channel numbers are<br>static and cannot be changed in the<br>programmer's model.|
|4 (Lowest)|Round-robin|When round-robin is enabled, any<br>channel configured for round-robin<br>operation has lowest priority within an<br>arbitration group. Round-robin is enabled<br>by setting theCSR[ERCA]field to 1.<br>After being enabled, channels with a<br>channel priority of zero (CHn_PRI=0)<br>will use round-robin arbitration. Round-<br>robin arbitration will rotate the channel<br>selection among the channels requesting<br>service with CHn_PRI=0 within the<br>arbitration group. Any non-zero channel<br>within the arbitration group will continue<br>to use fixed-priority arbitration, and if<br>requesting service will be selected over<br>any round-robin channels.|



For fixed arbitration, the overall priority can be considered a number composed of three concatenated priority levels: CHn_GRPRI:CHn_PRI:CH_NUM. The largest number has the highest priority and the lowest number has the lowest priority. 

For round-robin arbitration, the priority number is CHn_GRPRI:0:X. The module rotates through the CHn_PRI=0 channels requesting service without regard to priority among these channels. Any channel within the arbitration group for which CHn_PRI is greater than 0 will be serviced before the round-robin channels. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

416 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

### 14.4.3 Programming errors 

The eDMA performs various tests on the transfer control descriptor to verify consistency in the descriptor data. 

The channel number causing the error is recorded in the Error Status register (CHn_ES). If the error source is not removed before the next activation of the problematic channel, the error is detected and recorded again. Setting the halt after error field, CSR[HAE], will halt the DMA and prevent reoccurrence of the error. 

### 14.4.4 Arbitration mode considerations 

This section discusses arbitration considerations for eDMA. 

#### 14.4.4.1 Fixed group arbitration, fixed channel arbitration 

In this mode, eDMA selects for execution the channel service request from the highest-priority channel in the highest-priority group. If eDMA is programmed so that the channels within a high-priority group have a high number of requests or large data transfers, that group may consume all the bandwidth of the eDMA controller. That is, no lower-priority groups are serviced if there is always at least one DMA request pending on a channel in the highest-priority group when the controller arbitrates the next DMA request. The advantage of this scenario is that latency can be small for channels that need to be serviced quickly. 

#### 14.4.4.2 Fixed group arbitration, round-robin channel arbitration 

The highest-priority group with a request is serviced. Lower-priority groups are serviced if no pending requests exist in the higher-priority groups. 

Within each group, channels are serviced starting with the highest non-zero channel priority. For all channels with a channel priority programmed to 0, selection begins with the highest channel number requesting service and then rotates through to the lowest channel number requesting service. The round-robin channel arbitration can provide a fairness mechanism to lower-priority channels. 

This scenario could cause the same bandwidth consumption problem as indicated in Fixed group arbitration, fixed channel arbitration, but all the channels in the highest-priority group will be serviced. Service latency is short on the highest-priority group, but could potentially be very much longer as the group priority decreases. 

### 14.4.5 Performing DMA transfers 

This section presents examples on how to perform DMA transfers with the eDMA. 

#### 14.4.5.1 Single request 

To perform a simple transfer of n bytes of data with one activation, set the major loop to one (TCDn_CITER = TCDn_BITER = 1). The data transfer begins after the channel service request is acknowledged and the channel is selected to execute. After the transfer is complete, the CHn_CSR[DONE] field is set to 1 and an interrupt is generated if properly enabled. 

For example, the following TCD entry is configured to transfer 16 bytes of data. The eDMA is programmed for one iteration of the major loop transferring 16 bytes per iteration. The source memory has a byte-wide memory port located at 0x1000. The destination memory has a 32-bit port located at 0x2000. The address offsets are programmed in increments to match the transfer size: one byte for the source, and four bytes for the destination. The final source and destination addresses are adjusted to return to their beginning values. 

```
    TCDn_CITER = TCDn_BITER = 1
    TCDn_NBYTES = 16
    TCDn_SADDR = 0x1000
    TCDn_SOFF = 1
    TCDn_ATTR[SSIZE] = 0
    TCDn_SLAST = -16
    TCDn_DADDR = 0x2000
    TCDn_DOFF = 4
    TCDn_ATTR[DSIZE] = 2
```

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

417 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

```
    TCDn_DLAST_SGA= –16
    TCDn_CSR[INTMAJ] = 1
    TCDn_CSR[START] = 1 (should be written last after all other fields have been initialized)
    All other TCDn fields = 0
```

This generates the following event sequence: 

1. User write to the TCDn_CSR[START] field requests channel service. 

2. The channel is selected by arbitration for servicing. 

3. eDMA engine writes: 

   - CHn_CSR[DONE] = 0 

   - TCDn_CSR[START] = 0 

   - CHn_CSR[ACTIVE] = 1 

4. eDMA engine reads: channel TCD data from local memory to internal register file. 

5. The source-to-destination transfers are executed as follows: 

   - a. Read byte from location 0x1000, read byte from location 0x1001, read byte from 0x1002, read byte from 0x1003. b. Write 32 bits to location 0x2000 → first iteration of the minor loop. 

   - c. Read byte from location 0x1004, read byte from location 0x1005, read byte from 0x1006, read byte from 0x1007. 

   - d. Write 32 bits to location 0x2004 → second iteration of the minor loop. 

   - e. Read byte from location 0x1008, read byte from location 0x1009, read byte from 0x100A, read byte from 0x100B. 

   - f. Write 32 bits to location 0x2008 → third iteration of the minor loop. 

   - g. Read byte from location 0x100C, read byte from location 0x100D, read byte from 0x100E, read byte from 0x100F. 

   - h. Write 32 bits to location 0x200C → last iteration of the minor loop → major loop complete. 

6. The eDMA engine writes: TCDn_SADDR = 0x1000, TCDn_DADDR = 0x2000, TCDn_CITER = 1 (TCDn_BITER). 

7. The eDMA engine writes: CHn_CSR[ACTIVE] = 0, CHn_CSR[DONE] = 1, CHn_INT[INT] = 1. 

8. The channel retires and the eDMA goes idle or services the next channel. 

#### 14.4.5.2 Multiple requests 

The following example transfers 32 bytes via two hardware requests, but is otherwise the same as the previous example. The only fields that change are the major loop iteration count and the final address offsets. The eDMA is programmed for two iterations of the major loop, transferring 16 bytes per iteration. After the channel's hardware requests are enabled via the CHn_CSR[ERQ] register field, the slave device initiates channel service requests. 

```
     TCDn_CITER = TCDn_BITER = 2
     TCDn_SLAST = –32
     TCDn_DLAST_SGA = –32
```

This would generate the following sequence of events: 

1. First hardware (eDMA peripheral) requests channel service. 

2. The channel is selected by arbitration for servicing. 

3. eDMA engine writes: CHn_CSR[DONE] = 0, TCDn_CSR[START] = 0, CHn_CSR[ACTIVE] = 1. 

4. eDMA engine reads: channel TCDn data from local memory to internal register file. 

5. The source-to-destination transfers are executed as follows: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

418 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

   - a. Read byte from location 0x1000, read byte from location 0x1001, read byte from 0x1002, read byte from 0x1003. 

   - b. Write 32 bits to location 0x2000 → first iteration of the minor loop. 

   - c. Read byte from location 0x1004, read byte from location 0x1005, read byte from 0x1006, read byte from 0x1007. 

   - d. Write 32 bits to location 0x2004 → second iteration of the minor loop. 

   - e. Read byte from location 0x1008, read byte from location 0x1009, read byte from 0x100A, read byte from 0x100B. 

   - f. Write 32 bits to location 0x2008 → third iteration of the minor loop. 

   - g. Read byte from location 0x100C, read byte from location 0x100D, read byte from 0x100E, read byte from 0x100F. 

   - h. Write 32 bits to location 0x200C → last iteration of the minor loop. 

6. eDMA engine writes: TCDn_SADDR = 0x1010, TCDn_DADDR = 0x2010, TCDn_CITER = 1. 

7. eDMA engine writes: CHn_CSR[ACTIVE] = 0. 

8. The channel retires, which concludes one iteration of the major loop. The eDMA goes idle or services the next channel. 

9. Second hardware (eDMA peripheral) requests channel service. 

10. The channel is selected by arbitration for servicing. 

11. eDMA engine writes: CHn_CSR[DONE] = 0, TCDn_CSR[START] = 0, CHn_CSR[ACTIVE] = 1. 

12. eDMA engine reads: Channel TCD data from local memory to internal register file. 

13. The source-to-destination transfers are executed as follows: 

   - a. Read byte from location 0x1010, read byte from location 0x1011, read byte from 0x1012, read byte from 0x1013. 

   - b. Write 32 bits to location 0x2010 → first iteration of the minor loop. 

   - c. Read byte from location 0x1014, read byte from location 0x1015, read byte from 0x1016, read byte from 0x1017. 

   - d. Write 32 bits to location 0x2014 → second iteration of the minor loop. 

   - e. Read byte from location 0x1018, read byte from location 0x1019, read byte from 0x101A, read byte from 0x101B. 

   - f. Write 32 bits to location 0x2018 → third iteration of the minor loop. 

   - g. Read byte from location 0x101C, read byte from location 0x101D, read byte from 0x101E, read byte from 0x101F. 

   - h. Write 32 bits to location 0x201C → last iteration of the minor loop → major loop complete. 

14. eDMA engine writes: TCDn_SADDR = 0x1000, TCDn_DADDR = 0x2000, TCDn_CITER = 2 (TCDn_BITER). 

15. eDMA engine writes: CHn_CSR[ACTIVE] = 0, CHn_CSR[DONE] = 1, CHn_INT[INT] = 1. 

16. The channel retires, which concludes with the major loop complete. The eDMA goes idle or services the next channel. 

#### 14.4.5.3 Using the modulo feature 

The modulo feature of the eDMA allows implementation of a circular data queue in which the size of the queue is a power of 2. xMOD is a 5-bit field for the source and destination in the TCD, and it specifies which lower address bits increment from their original value after the address+offset calculation. All upper address bits remain the same as in the original value. A setting of 0 for this field disables the modulo feature. Modulo addressing applies to cases where the minor loop offset is enabled; that is, the upper address bits remain the same after the minor loop offset is added to the source or destination address. 

The following table shows how the transfer addresses are specified based on the setting of the MOD field. Here a circular buffer is created where the address wraps to the original value but the 28 upper address bits (0x1234567x) retain their original value. In this example, the source address is set to 0x12345670, the offset is set to four bytes, and the MOD field is set to four, which allows for a 2<sup>4</sup> byte (16 byte) queue size. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

419 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

Table 52. Modulo example 

|Transfer number|Address|
|---|---|
|1|0x12345670|
|2|0x12345674|
|3|0x12345678|
|4|0x1234567C|
|5|0x12345670|
|6|0x12345674|



### 14.4.6 Monitoring transfer descriptor status 

This section discusses how to monitor eDMA status. 

#### 14.4.6.1 Testing for minor loop completion 

There are two methods to test for minor loop completion when using software-initiated service requests. 

1. The first method is to read the TCDn_CITER field and test for a change. 

2. The second method, extracted from the sequence shown below, is to test the TCDn_CSR[START] field and the CHn_CSR[ACTIVE] field. The minor-loop-complete condition is indicated by both fields reading 0 after TCDn_CSR[START] is set to 1. Polling the CHn_CSR[ACTIVE] field only may be inconclusive because the active status may be missed if the channel execution is short in duration. 

The CHn_CSR and TCDn_CSR status fields execute the following sequence for a software-activated channel: 

|Stage|TCDn_CSR field|CHn_CS|R fields|State|
|---|---|---|---|---|
||START|ACTIVE|DONE||
|1|1|0|0|Initiate channel service request via software.|
|2|0|1|0|Channel is executing.|
|3a|0|0|0|Channel has completed the minor loop and is idle.|
|3b|0|0|1|Channel has completed the major loop and is idle.|



The best method to test for minor-loop completion when using hardware-initiated (that is, peripheral-initiated) service requests is to read the TCDn_CITER field and test for a change. The hardware request and acknowledge handshake signals are not visible in the programmer's model. 

The TCD status fields execute the following sequence for a hardware-activated channel: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

420 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

|Stage|TCDn_CSR field|CHn_CS|R fields|State|
|---|---|---|---|---|
||START|ACTIVE|DONE||
|1|0|0|0|Initiate channel service request via hardware (peripheral<br>request asserted).|
|2|0|1|0|Channel is executing.|
|3a|0|0|0|Channel has completed the minor loop and is idle.|
|3b|0|0|1|Channel has completed the major loop and is idle.|



For both activation types, the major-loop-complete status is explicitly indicated via the CHn_CSR[DONE] field. 

The TCDn_CSR[START] field is cleared to 0 automatically when the channel begins execution, regardless of how the channel activates. 

#### 14.4.6.2 Reading the transfer descriptors of active channels 

The eDMA reads back the true TCDn_SADDR, TCDn_DADDR, and TCDn_NBYTES values if they are read when a channel executes. The true values of SADDR, DADDR, and NBYTES are the values the eDMA engine currently uses in its internal register file, and not the values in the TCD local memory for that channel. The addresses, SADDR and DADDR, and NBYTES (which decrements to zero as the transfer progresses), can give an indication of the progress of the transfer. All other values are read back from the TCD local memory. 

#### 14.4.6.3 Checking channel preemption status 

A preemptive situation is one in which a preempt-enabled channel is executing and a higher-priority request becomes active. When round-robin channel arbitration mode is enabled, all channels with their channel priority set to 0 lose their preempt ability. Channel priorities of 0 are treated as equal, that is, they are constantly rotating, when round-robin arbitration mode is enabled. 

The CHn_CSR[ACTIVE] field for the preempted channel remains asserted throughout the preemption. The preempted channel is temporarily suspended when the preempting channel executes one major loop iteration. If two CHn_CSR[ACTIVE] fields are set simultaneously in the global TCD map, a higher-priority channel is actively preempting a lower-priority channel. 

### 14.4.7 Channel linking 

Channel linking (or chaining) is a mechanism in which one channel sets the TCDn_CSR[START] field of another channel (or itself), thus initiating a service request for that channel. When properly enabled, the eDMA engine automatically performs this operation at the major or minor loop completion. 

The minor loop channel linking occurs at the completion of the minor loop (or one iteration of the major loop). The TCDn_CITER[ELINK] field determines whether a minor loop link is requested. When enabled, the channel link is made after each iteration of the major loop except for the last. When the major loop is exhausted, only the major loop channel link fields are used to determine if a channel link should be made. For example, using an initial field setting of: 

```
     TCDn_CITER[ELINK] = 1
     TCDn_CITER[LINKCH] = 0xC
     TCDn_CITER[CITER] value = 0x4
     TCDn_CSR[MAJORELINK] = 1
     TCDn_CSR[MAJORLINKCH] = 0x7
```

executes as: 

1. Minor loop done → set TCD12_CSR[START] field 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

421 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

2. Minor loop done → set TCD12_CSR[START] field 

3. Minor loop done → set TCD12_CSR[START] field 

4. Minor loop done, major loop done→ set TCD7_CSR[START] field 

When minor loop linking is enabled (TCDn_CITER[ELINK] = 1), the TCDn_CITER[CITER] field uses a nine-bit vector to form the current iteration count. When minor loop linking is disabled (TCDn_CITER[ELINK] = 0), the TCDn_CITER[CITER] field uses a 15-bit vector to form the current iteration count. The bits associated with the TCDn_CITER[LINKCH] field are concatenated onto the CITER value to increase the range of the CITER. 

~~<mark>NOTE</mark>~~ 

The TCDn_CITER[ELINK] field and the TCDn_BITER[ELINK] field must be equal — if they are not, a configuration error is reported. The CITER and BITER vector widths must be equal to calculate the major loop halfway done interrupt point. 

The following table summarizes how a DMA channel can link to another DMA channel, that is, use another channel's TCD, at the end of a loop. 

Table 53. Channel linking parameters 

|Wanted link<br>behavior|TCD control field name|Description|
|---|---|---|
|Link at end of<br>minor loop|TCDn_CITER[ELINK]|Enable channel-to-channel linking on minor loop completion<br>(current iteration)|
||TCDn_CITER[LINKCH]|Link channel number when linking at end of minor loop (current iteration)|
|Link at end of<br>major loop|TCDn_CSR[MAJORELINK]<br>TCDn_CSR[MAJORLINKCH]|Enable channel-to-channel linking on major loop completion<br>Link channel number when linking at end of major loop|



### 14.4.8 Dynamic programming 

This section provides recommended methods to change the programming model during channel execution. 

#### 14.4.8.1 Dynamically changing the channel priority 

To change group or channel priority levels: 

1. Halt the DMA by writing 1 to the CSR[HALT] field. 

2. Change the group or channel priorities as wanted. 

3. Enable normal DMA operations by writing 0 to the CSR[HALT] field. 

#### 14.4.8.2 Dynamic channel linking 

Dynamic channel linking is the process of setting the TCDn_CSR[MAJORELINK] field during channel execution (see the diagram in TCD structure). This field is read from the TCD local memory at the end of channel execution, thus allowing you to enable the feature during channel execution. 

Because you are allowed to change the configuration during execution, you need a coherency model. Consider the scenario where you attempt to execute a dynamic channel link by enabling the TCDn_CSR[MAJORELINK] field at the same time the eDMA engine is retiring the channel. TCDn_CSR[MAJORELINK] would be set in the programmer’s model, but it would be unclear whether the actual link was made before the channel retired. 

We recommend that you use the following coherency model when executing a dynamic channel link request. 

1. Write 1 to the TCDn_CSR[MAJORELINK] field. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

422 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

2. Read back the TCDn_CSR[MAJORELINK] field. 

3. Test the TCDn_CSR[MAJORELINK] request status: 

   - If TCDn_CSR[MAJORELINK] = 1, the dynamic link attempt was successful. 

   - If TCDn_CSR[MAJORELINK] = 0, the attempted dynamic link did not succeed (the channel was already retiring). 

For this request, the TCD local memory controller forces the TCDn_CSR[MAJORELINK] field to 0 on any writes to a channel’s TCDn_CSR[7:0] after that channel’s CHn_CSR[DONE] field is set to 1, indicating the major loop is complete. 

~~<mark>NOTE</mark>~~ 

You must clear the CHn_CSR[DONE] field to 0 before writing to the TCDn_CSR[MAJORELINK] field. The CHn_CSR[DONE] field is cleared to 0 automatically by the eDMA engine after a channel begins execution. 

#### 14.4.8.3 Dynamic scatter/gather 

Scatter/gather is the process of automatically loading a new TCD into a channel. It allows a DMA channel to use multiple TCDs; this enables a DMA channel to scatter the DMA data to multiple destinations or gather it from multiple sources. When scatter/gather is enabled and the channel has finished its major loop, a new TCD is fetched from system memory and loaded into that channel’s descriptor location in the eDMA programmer’s model, thus replacing the current descriptor. 

Because you are allowed to change the configuration during execution, you need a coherency model. Consider the scenario where you attempt to execute a dynamic scatter/gather operation by enabling the TCDn_CSR[ESG] field at the same time the eDMA engine is retiring the channel. The TCDn_CSR[ESG] field would be set in the programmer’s model, but it would be unclear whether the actual scatter/gather request was honored before the channel retired. 

Two methods are recommended for executing a dynamic scatter/gather request. Whenever the TCDn_CSR is written, the TCD local memory controller forces the TCDn_CSR[ESG] field to 0 on any writes to a channel’s TCDn_CSR[7:0] after that channel’s CHn_CSR[DONE] field has been set to 1, indicating the major loop is complete. If attempting to set the ESG, ensure the DONE field is cleared to 0. 

~~<mark>NOTE</mark>~~ 

You must clear the CHn_CSR[DONE] field to 0 before writing the TCDn_CSR[MAJORELINK] or TCDn_CSR[ESG] fields. The CHn_CSR[DONE] field is cleared to 0 automatically by the eDMA engine after a channel begins execution and is set to 1 upon major loop completion. 

#### 14.4.8.3.1 Method 1 (channel not using major loop channel linking) 

For a channel not using major loop channel linking, the coherency model described here may be used for a dynamic scatter/ gather request. 

When the TCDn_CSR[MAJORELINK] field is 0, the TCDn_CSR[MAJORLINKCH] field is not used by the eDMA. In this case, the TCDn_CSR[MAJORLINKCH] bits may be used for other purposes. This method uses the TCDn_CSR[MAJORLINKCH] field as a TCDn_CSR identification (ID). 

When the descriptors are built, write a unique TCDn_CSR ID in the TCDn_CSR[MAJORLINKCH] field for each TCDn_CSR associated with a channel using dynamic scatter/gather. 

1. Write a 1 to the TCDn_CSR[DREQ] field. Should a dynamic scatter/gather attempt fail, setting the TCDn_CSR[DREQ] field to 1 will prevent future hardware activation of this channel. This stops the channel from executing with a destination address (daddr) that was calculated using a scatter/gather address (written in the next step) instead of a DLAST final offset value. 

2. Write the TCDn_DLAST_SGA field with the scatter/gather address. 

3. Write a 1 to the TCDn_CSR[ESG] field. 

4. Read back the 16-bit TCDn_CSR control/status field. 

5. Test the TCDn_CSR[ESG] request status and TCDn_CSR[MAJORLINKCH] value: 

   - If ESG = 1, the dynamic scatter/gather attempt was successful. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

423 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

- If ESG = 0 and the MAJORLINKCH (ID) did not change, the dynamic scatter/gather attempt was not successful (the channel was already retiring). 

- If ESG = 0 and the MAJORLINKCH (ID) changed, the dynamic scatter/gather attempt was successful (the new TCDn_CSR’s ESG value cleared the ESG field to 0). 

#### 14.4.8.3.2 Method 2 (channel using major loop channel linking) 

For a channel using major loop channel linking, the coherency model described here may be used for a dynamic scatter/gather request. This method uses the TCDn_DLAST_SGA field as a TCD identification (ID). 

1. Write a 1 to the TCDn_CSR[DREQ] field. Should a dynamic scatter/gather attempt fail, setting the DREQ field to 1 will prevent a future hardware activation of this channel. This stops the channel from executing with a destination address (DADDR) that was calculated using a scatter/gather address (written in the next step) instead of a DLAST final offset value. 

2. Write the TCDn_DLAST_SGA field with the scatter/gather address. 

3. Write a 1 to the TCDn_CSR[ESG] field. 

4. Read back the TCDn_CSR[ESG] field. 

5. Test the TCDn_CSR[ESG] request status: 

   - If ESG = 1, the dynamic scatter/gather attempt was successful. 

   - If ESG = 0, read the 32-bit TCDn_DLAST_SGA field. 

   - If ESG = 0 and the TCDn_DLAST_SGA did not change, the dynamic scatter/gather attempt was not successful (the channel was already retiring). 

   - If ESG = 0 and the TCDn_DLAST_SGA changed, the dynamic scatter/gather attempt was successful (the new TCDn_CSR’s ESG value cleared the ESG field to 0). 

### 14.4.9 Suspend/resume a DMA channel with active hardware service requests 

The DMA allows you to move data from memory or peripheral registers to another location in memory or to peripheral registers without CPU interaction. After the DMA and peripherals are configured and active, it is rare but supported to suspend a peripheral's service request dynamically. In this scenario, there are certain restrictions to disabling a DMA hardware service request. For coherency, you must follow a specific procedure. This section provides guidance on how to coherently suspend and resume a Direct Memory Access (DMA) channel when the DMA is triggered by a slave module such as the Serial Peripheral Interface (SPI), Sigma Delta Analog to Digital Convertor (SDADC), or other module. 

#### 14.4.9.1 Suspend an active DMA channel 

To suspend an active DMA channel: 

1. Stop the DMA service request at the peripheral first. Confirm it has been disabled by reading back the appropriate register in the peripheral. 

2. Check the DMA's Hardware Request Status (HRS) to ensure there is no service request to the DMA channel being suspended. Then disable the hardware service request by clearing the ERQ field to 0 on the appropriate DMA channel. 

For example, assume the SPI is set as a master for transmitting data via a DMA service request when the TXFIFO has an empty slot. The DMA will transfer the next command and data to the TXFIFO upon the request. If you need to suspend the DMA/SPI transfer loop, perform the following steps: 

1. Disable the DMA service request at the source by writing 0 to DSPI_RSER[TFFF_RE]. Confirm that DSPI_RSER[TFFF_RE] is 0. 

2. Ensure there is no DMA service request from the SPI by verifying that HRS[HRS] is 0 for the appropriate channel. If no service request is present, disable the DMA channel by clearing the channel's ERQ field to 0. If a service request is present, wait until the request has been processed and the HRS field reads 0. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

424 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

#### 14.4.9.2 Resume a DMA channel 

To resume a DMA channel: 

1. Enable the DMA service request on the appropriate channel by setting its ERQ field to 1. 

2. Enable the DMA service request at the peripheral. 

## 14.5 Memory map/register definition 

The eDMA programming model is partitioned into three parts: 

1. The first part defines a number of registers providing overall control functions and is known as the management page. 

2. The second part corresponds to the channel (CH) control, status, and configuration. 

3. The third part corresponds to the local TCD memory. 

##### TCD memory 

Each channel requires a 32-byte transfer control descriptor for defining the data movement operation. Each TCDn definition is presented as 11 registers of 16 or 32 bits. 

##### TCD initialization 

The TCD memory is in an unknown state after reset. Only the TCD START bit is initialized to 0. Prior to activating a channel, you must initialize its TCD with the appropriate transfer profile. 

##### TCD structure 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0425-16.png)


<!-- Start of picture text -->
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>0020h SADDR<br>0024h SMOD SSIZE DMOD DSIZE SOFF<br>0028h<br>MLOFF or NBYTES NBYTES<br>002Ch SLAST<br>0030h DADDR<br>CITER or<br>0034h CITER DOFF<br>CITER.LINKCH<br>0038h DLAST_SGA<br>BITER or<br>003Ch BITER.LINKCH BITER BWC MAJOR.LINKCH<br>31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>SMLOE DMLOE<br>Reserved<br>CITER.ELINK<br>ESDA ESG DREQ START<br>BITER.ELINK Reserved Reserved Reserved MAJOR.ELINK INTHALF INTMAJOR<br><!-- End of picture text -->

Figure 33. TCD structure 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

425 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

Accesses to reserved memory and fields 

- Reading reserved fields in a register returns the value of zero. 

- Writes to reserved fields in a register are ignored. 

- Reading or writing a reserved memory location generates a bus error. 

### 14.5.1 eDMA register descriptions 

#### 14.5.1.1 eDMA memory map 

eDMA base address: 4020_C000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|Management Page Control (CSR)|32|RW|0030_0000h|
|4h|Management Page Error Status (ES)|32|RO|0000_0000h|
|8h|Management Page Interrupt Request Status (INT)|32|RO|0000_0000h|
|Ch|Management Page Hardware Request Status (HRS)|32|RO|0000_0000h|
|100h - 17Ch|Channel Arbitration Group (CH0_GRPRI - CH31_GRPRI)|32|RW|0000_0000h|



#### 14.5.1.2 Management Page Control (CSR) 

##### Offset 

|Register|Offset|
|---|---|
|CSR|0h|



##### Function 

The Management Page Control register defines the basic operating configuration of the DMA. 

Arbitration uses a two-tier priority system; group and channel priority. The eDMA assigns each channel to a priority group. Group arbitration is fixed-priority and cannot be changed. Channel arbitration uses fixed priority and may be configured to use a selective round-robin scheme for specified channels within each priority group. For fixed-priority arbitration, eDMA selects for execution the highest priority channel requesting service in the highest priority arbitration group. 

The channel priority registers assign the relative priorities within each arbitration group; see CHn_PRI. All channels with a non-zero CHn_PRI value use fixed-priority arbitration. 

When you enable round-robin arbitration, all channels with channel priority set to zero do not have a priority and, of those channels requesting service, are cycled through (from high to low channel number) without regard to priority relative to each other within the same priority group. Any channel with a non-zero CHn_PRI value automatically has a higher priority over the round-robin channels. A channel's priority group is assigned in Channel Arbitration Group (CH0_GRPRI - CH31_GRPRI). 

~~<mark>NOTE</mark>~~ 

For correct operation, changes to the CSR[ERCA, GCLC, GMRC] fields must be performed when the DMA channels are inactive; that is, when the CSR[ACTIVE] field is 0. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

426 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0427-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>ACTIV<br>R Reserved  ACTIVE_ID  Reserved<br>E<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv Reserv<br>R Reserved<br>CX  ECX  GMRC  GCLC  HALT  HAE  ed  ERCA  EDBG  ed<br>W 0 0 0<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|DMA Active Status|
|ACTIVE|0b - eDMA is idle<br>1b - eDMA is executing a channel|
|30-29<br>—<br>28-24|Reserved<br>Active Channel ID|
|ACTIVE_ID|This field identifies the channel number that is executing when the ACTIVE bit is 1.|
|23-16<br>—<br>15-10<br>—|Reserved<br>Reserved|
|9<br>CX|Cancel Transfer<br>When set to 1, this field cancels the remaining data transfer, stops the executing channel, and forces the<br>minor loop to finish. The cancel takes effect after the last write of the current read/write sequence. CX<br>clears itself to 0 after the cancel has been honored. This cancel retires the channel normally as if the<br>minor loop had been completed.<br>0b - Normal operation<br>1b - Cancel the remaining data transfer|
|8<br>ECX|Cancel Transfer With Error<br>Cancellation of the remaining data transfer is similar to that of the CX field. Execution of the the channel<br>is stopped and the minor loop is forced to finish. The cancellation takes effect after the last write of the<br>current read/write sequence. The ECX field clears itself to 0 after the cancel is honored. In addition to|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

427 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||cancelling the transfer, ECX treats the cancel as an error condition, thus updatingManagement Page<br>Error Status (ES)and generating an optional error interrupt.<br>0b - Normal operation<br>1b - Cancel the remaining data transfer|
|7<br>GMRC|Global Master ID Replication Control<br>If master ID replication is disabled, the privileged protection level (Supervisor mode) for<br>DMA transfers is used.<br>~~NOTE~~<br>0b - Master ID replication disabled for all channels<br>1b - Master ID replication available and controlled by each channel's CHn_SBR[EMI] setting|
|6<br>GCLC|Global Channel Linking Control<br>0b - Channel linking disabled for all channels<br>1b - Channel linking available and controlled by each channel's link settings|
|5<br>HALT|Halt DMA Operations<br>This field stalls the start of any new channels. Executing channels are allowed to complete. Channel<br>execution resumes when this field is cleared to 0.<br>0b - Normal operation<br>1b - Stall the start of any new channels|
|4<br>HAE|Halt After Error<br>When this field is set to 1, any error causes the HALT field to be set to 1. Then all service requests are<br>ignored until the HALT field is cleared to 0.<br>0b - Normal operation<br>1b - Any error causes the HALT field to be set to 1|
|3<br>|Reserved|
|—<br>2<br>ERCA|Enable Round Robin Channel Arbitration<br>0b - Round-robin channel arbitration disabled. Fixed priority arbitration used for channel selection<br>within each group<br>1b - Round-robin channel arbitration enabled. Round-robin arbitration used for channel selection<br>within each group|
|1<br>EDBG|Enable Debug<br>When in debug mode, the DMA stalls the start of a new channel. Executing channels are allowed to<br>complete. DMA resumes channel execution when the system exits debug mode or clears the EDBG field<br>to 0.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

428 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0429-03.png)


<!-- Start of picture text -->
Field Function<br>0b - Debug mode disabled. When in debug mode, the DMA continues to operate<br>1b - Debug mode is enabled. When in debug mode, the DMA stalls the start of a new channel<br>0 Reserved<br>—<br><!-- End of picture text -->

#### 14.5.1.3 Management Page Error Status (ES) 

##### Offset 

|Register|Offset|
|---|---|
|ES|4h|



##### Function 

The ES provides information concerning the last recorded channel error. Channel errors can be caused by: 

- An illegal setting in the transfer control descriptor 

- An error termination to a bus master read or write cycle 

- An uncorrectable error that occurred when the device was accessing the TCD SRAM 

- A "cancel transfer with error" request was made via the corresponding cancel transfer field or input signal 

Upon any error condition, the software must initialize the TCD of the channel that contains the error, as it is in an incomplete state after an error. See Fault reporting and handling for more details. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0429-15.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R VLD  Reserved  ERRCHN  0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 UCE  ECX  SAE  SOE  DAE  DOE  NCE  SGE  SBE  DBE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Valid|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

429 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|VLD|Logical OR of all ERR status fields.<br>0b - No ERR fields are set to 1<br>1b - At least one ERR field is set to 1, indicating a valid error exists that software has not cleared|
|30-29<br>—|Reserved|
|28-24<br>ERRCHN|Error Channel Number or Canceled Channel Number<br>The channel number of the last recorded error or last recorded error-canceled transfer.|
|23-10<br>—|Reserved|
|9<br>UCE|Uncorrectable TCD Error During Channel Execution<br>UCE is set to 1 only when an uncorrectable ECC error occurs on an access generated by the DMA. If a CPU<br>access to the TCD causes an uncorrectable ECC error, then that access receives a bus error response.<br>When the eDMA sees a RAM error on an IPS access (when you are accessing a TCD), it<br>reports the error as a bus abort. When the DMA engine receives a RAM error (the execution<br>engine is accessing a TCD) it is recorded in the Error Status register, ES[UCE], along with<br>the channel number.<br>~~NOTE~~|
||0b - No uncorrectable ECC error<br>1b - Last recorded error was an uncorrectable TCD RAM error|
|8<br>ECX|Transfer Canceled<br>The ECX operation is a management page function. When employed, the targeted channel's CHn_ES<br>register reports an unspecified error; that is, only the ERR field is set to 1. The management page has<br>full view of the error condition.<br>0b - No canceled transfers<br>1b - Last recorded entry was a canceled transfer by the error cancel transfer input|
|7<br>SAE|Source Address Error<br>When this field is 1, it indicates that TCDn_SADDR is inconsistent with TCDn_ATTR[SSIZE].<br>0b - No source address configuration error<br>1b - Last recorded error was a configuration error detected in the TCDn_SADDR field|
|6<br>SOE|Source Offset Error<br>When this field is 1, it indicates that TCDn_SOFF is inconsistent with TCDn_ATTR[SSIZE].<br>0b - No source offset configuration error<br>1b - Last recorded error was a configuration error detected in the TCDn_SOFF field<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

430 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|5<br>DAE|Destination Address Error<br>When this field is 1, it indicates that TCDn_DADDR is inconsistent with TCDn_ATTR[DSIZE].<br>0b - No destination address configuration error<br>1b - Last recorded error was a configuration error detected in the TCDn_DADDR field|
|4<br>DOE|Destination Offset Error<br>When this field is 1, it indicates that TCDn_DOFF is inconsistent with TCDn_ATTR[DSIZE].<br>0b - No destination offset configuration error<br>1b - Last recorded error was a configuration error detected in the TCDn_DOFF field|
|3<br>NCE|NBYTES/CITER Configuration Error<br>This error indicates that one of the following has occurred:<br>• TCDn_NBYTES is not a multiple of TCDn_ATTR[SSIZE] and TCDn_ATTR[DSIZE]<br>• TCDn_CITER[CITER] is equal to zero<br>• TCDn_CITER[ELINK] is not equal to TCDn_BITER[ELINK]<br>0b - No NBYTES/CITER configuration error<br>1b - The last recorded error was NBYTES equal to zero or a CITER not equal to BITER error.<br>Last recorded error was a configuration error detected in the TCDn_NBYTES or TCDn_CITER<br>fields|
|2<br>SGE|Scatter/Gather Configuration Error<br>When this field is 1, it indicates thatTCDn_DLAST_SGAis not on a 32-byte boundary. This field is<br>checked at the beginning of a scatter/gather operation after major loop completion ifTCDn_CSR[ESG]is<br>enabled.<br>0b - No scatter/gather configuration error<br>1b - Last recorded error was a configuration error detected in the TCDn_DLAST_SGA field|
|1|Source Bus Error|
|SBE|0b - No source bus error<br>1b - Last recorded error was a bus error on a source read|
|0|Destination Bus Error|
|DBE|0b - No destination bus error<br>1b - Last recorded error was a bus error on a destination write|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

431 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

#### 14.5.1.4 Management Page Interrupt Request Status (INT) 

##### Offset 

|Register|Offset|
|---|---|
|INT|8h|



##### Function 

This register shows the current state of the interrupt service requests for all eDMA channels. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0432-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R INT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R INT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-0|Interrupt Request Status|
|INT|The INT register presents the interrupt request status for each eDMA channel. Depending on the<br>appropriate field setting in the transfer control descriptors, the eDMA engine generates an interrupt<br>on data transfer completion or an error condition. The eDMA routes channel interrupt requests to the<br>interrupt controller. During the interrupt service routine associated with any given channel, it is the software's<br>responsibility to clear the appropriate field in the channel’s interrupt request register, CHn_INT, thus<br>negating the interrupt request.|
||0b - Interrupt request for corresponding channel not present|
||1b - Interrupt request for corresponding channel present|



#### 14.5.1.5 Management Page Hardware Request Status (HRS) 

##### Offset 

|Register|Offset|
|---|---|
|HRS|Ch|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

432 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Function 

The hardware request status register (HRS) shows the current state of the hardware service request signaling as seen by eDMA's arbitration logic. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0433-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R HRS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R HRS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Hardware Request Status|
|HRS|The HRS bit for its respective channel remains asserted for the period when a hardware request is present<br>on the channel. After the request is completed and the channel is free, the hardware automatically clears<br>the corresponding HRS bit to 0.|
||0b - Hardware service request for corresponding channel is not present|
||1b - Hardware service request for corresponding channel is present|



#### 14.5.1.6 Channel Arbitration Group (CH0_GRPRI - CH31_GRPRI) 

##### Offset 

For n = 0 to 31: 

|Register<br>CHn_GRPRI|Offset<br>100h + (n × 4h)|
|---|---|



##### Function 

The contents of this register define the arbitration group associated with each channel. Using a fixed-priority group arbitration scheme, eDMA evaluates the arbitration group priorities by numeric value from highest group number to lowest; for example, 0 is the lowest priority, 1 is the next higher priority, then 2, 3, and so on. The range of the group priority values is limited to the values of 0 through 31. Within each arbitration group, the channel priority assignment CHn_PRI determines the highest-priority channel. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

433 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||0||||||||GRPRI|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-5<br>—|Reserved|
|4-0|Arbitration Group For Channel n|
|GRPRI|Fixed-priority arbitration group number.|



### 14.5.2 TCD register descriptions 

#### 14.5.2.1 TCD memory map 

TCD base address: 4021_0000h 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|0h|Channel Control and Status (CH0_CSR)|32|RW|0000_0000h|
|4h|Channel Error Status (CH0_ES)|32|W1C|0000_0000h|
|8h|Channel Interrupt Status (CH0_INT)|32|W1C|0000_0000h|
|Ch|Channel System Bus (CH0_SBR)|32|RW|0000_8002h|
|10h|Channel Priority (CH0_PRI)|32|RW|0000_0000h|
|20h|TCD Source Address (TCD0_SADDR)|32|RW|0000_0000h|
|24h|TCD Signed Source Address Offset (TCD0_SOFF)|16|RW|0000h|
|26h|TCD Transfer Attributes (TCD0_ATTR)|16|RW|See<br>description|
|28h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD0_NBYTES_MLOFFNO)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

434 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|28h|TCD Transfer Size with Minor Loop Offsets<br>(TCD0_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|2Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD0_SLAST_SDA)|32|RW|0000_0000h|
|30h|TCD Destination Address (TCD0_DADDR)|32|RW|0000_0000h|
|34h|TCD Signed Destination Address Offset (TCD0_DOFF)|16|RW|0000h|
|36h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD0_CITER_ELINKNO)|16|RW|0000h|
|36h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD0_CITER_ELINKYES)|16|RW|0000h|
|38h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD0_DLAST_SGA)|32|RW|0000_0000h|
|3Ch|TCD Control and Status (TCD0_CSR)|16|RW|0000h|
|3Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD0_BITER_ELINKNO)|16|RW|0000h|
|3Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD0_BITER_ELINKYES)|16|RW|0000h|
|4000h|Channel Control and Status (CH1_CSR)|32|RW|0000_0000h|
|4004h|Channel Error Status (CH1_ES)|32|W1C|0000_0000h|
|4008h|Channel Interrupt Status (CH1_INT)|32|W1C|0000_0000h|
|400Ch|Channel System Bus (CH1_SBR)|32|RW|0000_8002h|
|4010h|Channel Priority (CH1_PRI)|32|RW|0000_0000h|
|4020h|TCD Source Address (TCD1_SADDR)|32|RW|0000_0000h|
|4024h|TCD Signed Source Address Offset (TCD1_SOFF)|16|RW|0000h|
|4026h|TCD Transfer Attributes (TCD1_ATTR)|16|RW|See<br>description|
|4028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD1_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|4028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD1_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|402Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD1_SLAST_SDA)|32|RW|0000_0000h|
|4030h|TCD Destination Address (TCD1_DADDR)|32|RW|0000_0000h|
|4034h|TCD Signed Destination Address Offset (TCD1_DOFF)|16|RW|0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

435 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|4036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD1_CITER_ELINKNO)|16|RW|0000h|
|4036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD1_CITER_ELINKYES)|16|RW|0000h|
|4038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD1_DLAST_SGA)|32|RW|0000_0000h|
|403Ch|TCD Control and Status (TCD1_CSR)|16|RW|0000h|
|403Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD1_BITER_ELINKNO)|16|RW|0000h|
|403Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD1_BITER_ELINKYES)|16|RW|0000h|
|8000h|Channel Control and Status (CH2_CSR)|32|RW|0000_0000h|
|8004h|Channel Error Status (CH2_ES)|32|W1C|0000_0000h|
|8008h|Channel Interrupt Status (CH2_INT)|32|W1C|0000_0000h|
|800Ch|Channel System Bus (CH2_SBR)|32|RW|0000_8002h|
|8010h|Channel Priority (CH2_PRI)|32|RW|0000_0000h|
|8020h|TCD Source Address (TCD2_SADDR)|32|RW|0000_0000h|
|8024h|TCD Signed Source Address Offset (TCD2_SOFF)|16|RW|0000h|
|8026h|TCD Transfer Attributes (TCD2_ATTR)|16|RW|See<br>description|
|8028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD2_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|8028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD2_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|802Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD2_SLAST_SDA)|32|RW|0000_0000h|
|8030h|TCD Destination Address (TCD2_DADDR)|32|RW|0000_0000h|
|8034h|TCD Signed Destination Address Offset (TCD2_DOFF)|16|RW|0000h|
|8036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD2_CITER_ELINKNO)|16|RW|0000h|
|8036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD2_CITER_ELINKYES)|16|RW|0000h|
|8038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD2_DLAST_SGA)|32|RW|0000_0000h|
|803Ch|TCD Control and Status (TCD2_CSR)|16|RW|0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

436 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|803Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD2_BITER_ELINKNO)|16|RW|0000h|
|803Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD2_BITER_ELINKYES)|16|RW|0000h|
|C000h|Channel Control and Status (CH3_CSR)|32|RW|0000_0000h|
|C004h|Channel Error Status (CH3_ES)|32|W1C|0000_0000h|
|C008h|Channel Interrupt Status (CH3_INT)|32|W1C|0000_0000h|
|C00Ch|Channel System Bus (CH3_SBR)|32|RW|0000_8002h|
|C010h|Channel Priority (CH3_PRI)|32|RW|0000_0000h|
|C020h|TCD Source Address (TCD3_SADDR)|32|RW|0000_0000h|
|C024h|TCD Signed Source Address Offset (TCD3_SOFF)|16|RW|0000h|
|C026h|TCD Transfer Attributes (TCD3_ATTR)|16|RW|See<br>description|
|C028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD3_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|C028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD3_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|C02Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD3_SLAST_SDA)|32|RW|0000_0000h|
|C030h|TCD Destination Address (TCD3_DADDR)|32|RW|0000_0000h|
|C034h|TCD Signed Destination Address Offset (TCD3_DOFF)|16|RW|0000h|
|C036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD3_CITER_ELINKNO)|16|RW|0000h|
|C036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD3_CITER_ELINKYES)|16|RW|0000h|
|C038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD3_DLAST_SGA)|32|RW|0000_0000h|
|C03Ch|TCD Control and Status (TCD3_CSR)|16|RW|0000h|
|C03Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD3_BITER_ELINKNO)|16|RW|0000h|
|C03Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD3_BITER_ELINKYES)|16|RW|0000h|
|1_0000h|Channel Control and Status (CH4_CSR)|32|RW|0000_0000h|
|1_0004h|Channel Error Status (CH4_ES)|32|W1C|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

437 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|1_0008h|Channel Interrupt Status (CH4_INT)|32|W1C|0000_0000h|
|1_000Ch|Channel System Bus (CH4_SBR)|32|RW|0000_8002h|
|1_0010h|Channel Priority (CH4_PRI)|32|RW|0000_0000h|
|1_0020h|TCD Source Address (TCD4_SADDR)|32|RW|0000_0000h|
|1_0024h|TCD Signed Source Address Offset (TCD4_SOFF)|16|RW|0000h|
|1_0026h|TCD Transfer Attributes (TCD4_ATTR)|16|RW|See<br>description|
|1_0028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD4_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|1_0028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD4_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|1_002Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD4_SLAST_SDA)|32|RW|0000_0000h|
|1_0030h|TCD Destination Address (TCD4_DADDR)|32|RW|0000_0000h|
|1_0034h|TCD Signed Destination Address Offset (TCD4_DOFF)|16|RW|0000h|
|1_0036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD4_CITER_ELINKNO)|16|RW|0000h|
|1_0036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD4_CITER_ELINKYES)|16|RW|0000h|
|1_0038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD4_DLAST_SGA)|32|RW|0000_0000h|
|1_003Ch|TCD Control and Status (TCD4_CSR)|16|RW|0000h|
|1_003Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD4_BITER_ELINKNO)|16|RW|0000h|
|1_003Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD4_BITER_ELINKYES)|16|RW|0000h|
|1_4000h|Channel Control and Status (CH5_CSR)|32|RW|0000_0000h|
|1_4004h|Channel Error Status (CH5_ES)|32|W1C|0000_0000h|
|1_4008h|Channel Interrupt Status (CH5_INT)|32|W1C|0000_0000h|
|1_400Ch|Channel System Bus (CH5_SBR)|32|RW|0000_8002h|
|1_4010h|Channel Priority (CH5_PRI)|32|RW|0000_0000h|
|1_4020h|TCD Source Address (TCD5_SADDR)|32|RW|0000_0000h|
|1_4024h|TCD Signed Source Address Offset (TCD5_SOFF)|16|RW|0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

438 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|1_4026h|TCD Transfer Attributes (TCD5_ATTR)|16|RW|See<br>description|
|1_4028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD5_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|1_4028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD5_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|1_402Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD5_SLAST_SDA)|32|RW|0000_0000h|
|1_4030h|TCD Destination Address (TCD5_DADDR)|32|RW|0000_0000h|
|1_4034h|TCD Signed Destination Address Offset (TCD5_DOFF)|16|RW|0000h|
|1_4036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD5_CITER_ELINKNO)|16|RW|0000h|
|1_4036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD5_CITER_ELINKYES)|16|RW|0000h|
|1_4038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD5_DLAST_SGA)|32|RW|0000_0000h|
|1_403Ch|TCD Control and Status (TCD5_CSR)|16|RW|0000h|
|1_403Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD5_BITER_ELINKNO)|16|RW|0000h|
|1_403Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD5_BITER_ELINKYES)|16|RW|0000h|
|1_8000h|Channel Control and Status (CH6_CSR)|32|RW|0000_0000h|
|1_8004h|Channel Error Status (CH6_ES)|32|W1C|0000_0000h|
|1_8008h|Channel Interrupt Status (CH6_INT)|32|W1C|0000_0000h|
|1_800Ch|Channel System Bus (CH6_SBR)|32|RW|0000_8002h|
|1_8010h|Channel Priority (CH6_PRI)|32|RW|0000_0000h|
|1_8020h|TCD Source Address (TCD6_SADDR)|32|RW|0000_0000h|
|1_8024h|TCD Signed Source Address Offset (TCD6_SOFF)|16|RW|0000h|
|1_8026h|TCD Transfer Attributes (TCD6_ATTR)|16|RW|See<br>description|
|1_8028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD6_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|1_8028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD6_NBYTES_MLOFFYES)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

439 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|1_802Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD6_SLAST_SDA)|32|RW|0000_0000h|
|1_8030h|TCD Destination Address (TCD6_DADDR)|32|RW|0000_0000h|
|1_8034h|TCD Signed Destination Address Offset (TCD6_DOFF)|16|RW|0000h|
|1_8036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD6_CITER_ELINKNO)|16|RW|0000h|
|1_8036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD6_CITER_ELINKYES)|16|RW|0000h|
|1_8038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD6_DLAST_SGA)|32|RW|0000_0000h|
|1_803Ch|TCD Control and Status (TCD6_CSR)|16|RW|0000h|
|1_803Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD6_BITER_ELINKNO)|16|RW|0000h|
|1_803Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD6_BITER_ELINKYES)|16|RW|0000h|
|1_C000h|Channel Control and Status (CH7_CSR)|32|RW|0000_0000h|
|1_C004h|Channel Error Status (CH7_ES)|32|W1C|0000_0000h|
|1_C008h|Channel Interrupt Status (CH7_INT)|32|W1C|0000_0000h|
|1_C00Ch|Channel System Bus (CH7_SBR)|32|RW|0000_8002h|
|1_C010h|Channel Priority (CH7_PRI)|32|RW|0000_0000h|
|1_C020h|TCD Source Address (TCD7_SADDR)|32|RW|0000_0000h|
|1_C024h|TCD Signed Source Address Offset (TCD7_SOFF)|16|RW|0000h|
|1_C026h|TCD Transfer Attributes (TCD7_ATTR)|16|RW|See<br>description|
|1_C028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD7_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|1_C028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD7_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|1_C02Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD7_SLAST_SDA)|32|RW|0000_0000h|
|1_C030h|TCD Destination Address (TCD7_DADDR)|32|RW|0000_0000h|
|1_C034h|TCD Signed Destination Address Offset (TCD7_DOFF)|16|RW|0000h|
|1_C036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD7_CITER_ELINKNO)|16|RW|0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

440 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|1_C036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD7_CITER_ELINKYES)|16|RW|0000h|
|1_C038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD7_DLAST_SGA)|32|RW|0000_0000h|
|1_C03Ch|TCD Control and Status (TCD7_CSR)|16|RW|0000h|
|1_C03Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD7_BITER_ELINKNO)|16|RW|0000h|
|1_C03Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD7_BITER_ELINKYES)|16|RW|0000h|
|2_0000h|Channel Control and Status (CH8_CSR)|32|RW|0000_0000h|
|2_0004h|Channel Error Status (CH8_ES)|32|W1C|0000_0000h|
|2_0008h|Channel Interrupt Status (CH8_INT)|32|W1C|0000_0000h|
|2_000Ch|Channel System Bus (CH8_SBR)|32|RW|0000_8002h|
|2_0010h|Channel Priority (CH8_PRI)|32|RW|0000_0000h|
|2_0020h|TCD Source Address (TCD8_SADDR)|32|RW|0000_0000h|
|2_0024h|TCD Signed Source Address Offset (TCD8_SOFF)|16|RW|0000h|
|2_0026h|TCD Transfer Attributes (TCD8_ATTR)|16|RW|See<br>description|
|2_0028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD8_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|2_0028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD8_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|2_002Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD8_SLAST_SDA)|32|RW|0000_0000h|
|2_0030h|TCD Destination Address (TCD8_DADDR)|32|RW|0000_0000h|
|2_0034h|TCD Signed Destination Address Offset (TCD8_DOFF)|16|RW|0000h|
|2_0036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD8_CITER_ELINKNO)|16|RW|0000h|
|2_0036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD8_CITER_ELINKYES)|16|RW|0000h|
|2_0038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD8_DLAST_SGA)|32|RW|0000_0000h|
|2_003Ch|TCD Control and Status (TCD8_CSR)|16|RW|0000h|
|2_003Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD8_BITER_ELINKNO)|16|RW|0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

441 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|2_003Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD8_BITER_ELINKYES)|16|RW|0000h|
|2_4000h|Channel Control and Status (CH9_CSR)|32|RW|0000_0000h|
|2_4004h|Channel Error Status (CH9_ES)|32|W1C|0000_0000h|
|2_4008h|Channel Interrupt Status (CH9_INT)|32|W1C|0000_0000h|
|2_400Ch|Channel System Bus (CH9_SBR)|32|RW|0000_8002h|
|2_4010h|Channel Priority (CH9_PRI)|32|RW|0000_0000h|
|2_4020h|TCD Source Address (TCD9_SADDR)|32|RW|0000_0000h|
|2_4024h|TCD Signed Source Address Offset (TCD9_SOFF)|16|RW|0000h|
|2_4026h|TCD Transfer Attributes (TCD9_ATTR)|16|RW|See<br>description|
|2_4028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD9_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|2_4028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD9_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|2_402Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD9_SLAST_SDA)|32|RW|0000_0000h|
|2_4030h|TCD Destination Address (TCD9_DADDR)|32|RW|0000_0000h|
|2_4034h|TCD Signed Destination Address Offset (TCD9_DOFF)|16|RW|0000h|
|2_4036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD9_CITER_ELINKNO)|16|RW|0000h|
|2_4036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD9_CITER_ELINKYES)|16|RW|0000h|
|2_4038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD9_DLAST_SGA)|32|RW|0000_0000h|
|2_403Ch|TCD Control and Status (TCD9_CSR)|16|RW|0000h|
|2_403Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD9_BITER_ELINKNO)|16|RW|0000h|
|2_403Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD9_BITER_ELINKYES)|16|RW|0000h|
|2_8000h|Channel Control and Status (CH10_CSR)|32|RW|0000_0000h|
|2_8004h|Channel Error Status (CH10_ES)|32|W1C|0000_0000h|
|2_8008h|Channel Interrupt Status (CH10_INT)|32|W1C|0000_0000h|
|2_800Ch|Channel System Bus (CH10_SBR)|32|RW|0000_8002h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

442 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|2_8010h|Channel Priority (CH10_PRI)|32|RW|0000_0000h|
|2_8020h|TCD Source Address (TCD10_SADDR)|32|RW|0000_0000h|
|2_8024h|TCD Signed Source Address Offset (TCD10_SOFF)|16|RW|0000h|
|2_8026h|TCD Transfer Attributes (TCD10_ATTR)|16|RW|See<br>description|
|2_8028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD10_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|2_8028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD10_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|2_802Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD10_SLAST_SDA)|32|RW|0000_0000h|
|2_8030h|TCD Destination Address (TCD10_DADDR)|32|RW|0000_0000h|
|2_8034h|TCD Signed Destination Address Offset (TCD10_DOFF)|16|RW|0000h|
|2_8036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD10_CITER_ELINKNO)|16|RW|0000h|
|2_8036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD10_CITER_ELINKYES)|16|RW|0000h|
|2_8038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD10_DLAST_SGA)|32|RW|0000_0000h|
|2_803Ch|TCD Control and Status (TCD10_CSR)|16|RW|0000h|
|2_803Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD10_BITER_ELINKNO)|16|RW|0000h|
|2_803Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD10_BITER_ELINKYES)|16|RW|0000h|
|2_C000h|Channel Control and Status (CH11_CSR)|32|RW|0000_0000h|
|2_C004h|Channel Error Status (CH11_ES)|32|W1C|0000_0000h|
|2_C008h|Channel Interrupt Status (CH11_INT)|32|W1C|0000_0000h|
|2_C00Ch|Channel System Bus (CH11_SBR)|32|RW|0000_8002h|
|2_C010h|Channel Priority (CH11_PRI)|32|RW|0000_0000h|
|2_C020h|TCD Source Address (TCD11_SADDR)|32|RW|0000_0000h|
|2_C024h|TCD Signed Source Address Offset (TCD11_SOFF)|16|RW|0000h|
|2_C026h|TCD Transfer Attributes (TCD11_ATTR)|16|RW|See<br>description|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

443 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|2_C028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD11_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|2_C028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD11_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|2_C02Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD11_SLAST_SDA)|32|RW|0000_0000h|
|2_C030h|TCD Destination Address (TCD11_DADDR)|32|RW|0000_0000h|
|2_C034h|TCD Signed Destination Address Offset (TCD11_DOFF)|16|RW|0000h|
|2_C036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD11_CITER_ELINKNO)|16|RW|0000h|
|2_C036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD11_CITER_ELINKYES)|16|RW|0000h|
|2_C038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD11_DLAST_SGA)|32|RW|0000_0000h|
|2_C03Ch|TCD Control and Status (TCD11_CSR)|16|RW|0000h|
|2_C03Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD11_BITER_ELINKNO)|16|RW|0000h|
|2_C03Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD11_BITER_ELINKYES)|16|RW|0000h|
|20_0000h|Channel Control and Status (CH12_CSR)|32|RW|0000_0000h|
|20_0004h|Channel Error Status (CH12_ES)|32|W1C|0000_0000h|
|20_0008h|Channel Interrupt Status (CH12_INT)|32|W1C|0000_0000h|
|20_000Ch|Channel System Bus (CH12_SBR)|32|RW|0000_8002h|
|20_0010h|Channel Priority (CH12_PRI)|32|RW|0000_0000h|
|20_0020h|TCD Source Address (TCD12_SADDR)|32|RW|0000_0000h|
|20_0024h|TCD Signed Source Address Offset (TCD12_SOFF)|16|RW|0000h|
|20_0026h|TCD Transfer Attributes (TCD12_ATTR)|16|RW|See<br>description|
|20_0028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD12_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|20_0028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD12_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|20_002Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD12_SLAST_SDA)|32|RW|0000_0000h|
|20_0030h|TCD Destination Address (TCD12_DADDR)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

444 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|20_0034h|TCD Signed Destination Address Offset (TCD12_DOFF)|16|RW|0000h|
|20_0036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD12_CITER_ELINKNO)|16|RW|0000h|
|20_0036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD12_CITER_ELINKYES)|16|RW|0000h|
|20_0038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD12_DLAST_SGA)|32|RW|0000_0000h|
|20_003Ch|TCD Control and Status (TCD12_CSR)|16|RW|0000h|
|20_003Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD12_BITER_ELINKNO)|16|RW|0000h|
|20_003Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD12_BITER_ELINKYES)|16|RW|0000h|
|20_4000h|Channel Control and Status (CH13_CSR)|32|RW|0000_0000h|
|20_4004h|Channel Error Status (CH13_ES)|32|W1C|0000_0000h|
|20_4008h|Channel Interrupt Status (CH13_INT)|32|W1C|0000_0000h|
|20_400Ch|Channel System Bus (CH13_SBR)|32|RW|0000_8002h|
|20_4010h|Channel Priority (CH13_PRI)|32|RW|0000_0000h|
|20_4020h|TCD Source Address (TCD13_SADDR)|32|RW|0000_0000h|
|20_4024h|TCD Signed Source Address Offset (TCD13_SOFF)|16|RW|0000h|
|20_4026h|TCD Transfer Attributes (TCD13_ATTR)|16|RW|See<br>description|
|20_4028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD13_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|20_4028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD13_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|20_402Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD13_SLAST_SDA)|32|RW|0000_0000h|
|20_4030h|TCD Destination Address (TCD13_DADDR)|32|RW|0000_0000h|
|20_4034h|TCD Signed Destination Address Offset (TCD13_DOFF)|16|RW|0000h|
|20_4036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD13_CITER_ELINKNO)|16|RW|0000h|
|20_4036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD13_CITER_ELINKYES)|16|RW|0000h|
|20_4038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD13_DLAST_SGA)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

445 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|20_403Ch|TCD Control and Status (TCD13_CSR)|16|RW|0000h|
|20_403Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD13_BITER_ELINKNO)|16|RW|0000h|
|20_403Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD13_BITER_ELINKYES)|16|RW|0000h|
|20_8000h|Channel Control and Status (CH14_CSR)|32|RW|0000_0000h|
|20_8004h|Channel Error Status (CH14_ES)|32|W1C|0000_0000h|
|20_8008h|Channel Interrupt Status (CH14_INT)|32|W1C|0000_0000h|
|20_800Ch|Channel System Bus (CH14_SBR)|32|RW|0000_8002h|
|20_8010h|Channel Priority (CH14_PRI)|32|RW|0000_0000h|
|20_8020h|TCD Source Address (TCD14_SADDR)|32|RW|0000_0000h|
|20_8024h|TCD Signed Source Address Offset (TCD14_SOFF)|16|RW|0000h|
|20_8026h|TCD Transfer Attributes (TCD14_ATTR)|16|RW|See<br>description|
|20_8028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD14_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|20_8028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD14_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|20_802Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD14_SLAST_SDA)|32|RW|0000_0000h|
|20_8030h|TCD Destination Address (TCD14_DADDR)|32|RW|0000_0000h|
|20_8034h|TCD Signed Destination Address Offset (TCD14_DOFF)|16|RW|0000h|
|20_8036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD14_CITER_ELINKNO)|16|RW|0000h|
|20_8036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD14_CITER_ELINKYES)|16|RW|0000h|
|20_8038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD14_DLAST_SGA)|32|RW|0000_0000h|
|20_803Ch|TCD Control and Status (TCD14_CSR)|16|RW|0000h|
|20_803Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD14_BITER_ELINKNO)|16|RW|0000h|
|20_803Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD14_BITER_ELINKYES)|16|RW|0000h|
|20_C000h|Channel Control and Status (CH15_CSR)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

446 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|20_C004h|Channel Error Status (CH15_ES)|32|W1C|0000_0000h|
|20_C008h|Channel Interrupt Status (CH15_INT)|32|W1C|0000_0000h|
|20_C00Ch|Channel System Bus (CH15_SBR)|32|RW|0000_8002h|
|20_C010h|Channel Priority (CH15_PRI)|32|RW|0000_0000h|
|20_C020h|TCD Source Address (TCD15_SADDR)|32|RW|0000_0000h|
|20_C024h|TCD Signed Source Address Offset (TCD15_SOFF)|16|RW|0000h|
|20_C026h|TCD Transfer Attributes (TCD15_ATTR)|16|RW|See<br>description|
|20_C028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD15_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|20_C028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD15_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|20_C02Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD15_SLAST_SDA)|32|RW|0000_0000h|
|20_C030h|TCD Destination Address (TCD15_DADDR)|32|RW|0000_0000h|
|20_C034h|TCD Signed Destination Address Offset (TCD15_DOFF)|16|RW|0000h|
|20_C036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD15_CITER_ELINKNO)|16|RW|0000h|
|20_C036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD15_CITER_ELINKYES)|16|RW|0000h|
|20_C038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD15_DLAST_SGA)|32|RW|0000_0000h|
|20_C03Ch|TCD Control and Status (TCD15_CSR)|16|RW|0000h|
|20_C03Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD15_BITER_ELINKNO)|16|RW|0000h|
|20_C03Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD15_BITER_ELINKYES)|16|RW|0000h|
|21_0000h|Channel Control and Status (CH16_CSR)|32|RW|0000_0000h|
|21_0004h|Channel Error Status (CH16_ES)|32|W1C|0000_0000h|
|21_0008h|Channel Interrupt Status (CH16_INT)|32|W1C|0000_0000h|
|21_000Ch|Channel System Bus (CH16_SBR)|32|RW|0000_8002h|
|21_0010h|Channel Priority (CH16_PRI)|32|RW|0000_0000h|
|21_0020h|TCD Source Address (TCD16_SADDR)|32|RW|0000_0000h|
|21_0024h|TCD Signed Source Address Offset (TCD16_SOFF)|16|RW|0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

447 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|21_0026h|TCD Transfer Attributes (TCD16_ATTR)|16|RW|See<br>description|
|21_0028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD16_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|21_0028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD16_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|21_002Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD16_SLAST_SDA)|32|RW|0000_0000h|
|21_0030h|TCD Destination Address (TCD16_DADDR)|32|RW|0000_0000h|
|21_0034h|TCD Signed Destination Address Offset (TCD16_DOFF)|16|RW|0000h|
|21_0036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD16_CITER_ELINKNO)|16|RW|0000h|
|21_0036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD16_CITER_ELINKYES)|16|RW|0000h|
|21_0038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD16_DLAST_SGA)|32|RW|0000_0000h|
|21_003Ch|TCD Control and Status (TCD16_CSR)|16|RW|0000h|
|21_003Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD16_BITER_ELINKNO)|16|RW|0000h|
|21_003Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD16_BITER_ELINKYES)|16|RW|0000h|
|21_4000h|Channel Control and Status (CH17_CSR)|32|RW|0000_0000h|
|21_4004h|Channel Error Status (CH17_ES)|32|W1C|0000_0000h|
|21_4008h|Channel Interrupt Status (CH17_INT)|32|W1C|0000_0000h|
|21_400Ch|Channel System Bus (CH17_SBR)|32|RW|0000_8002h|
|21_4010h|Channel Priority (CH17_PRI)|32|RW|0000_0000h|
|21_4020h|TCD Source Address (TCD17_SADDR)|32|RW|0000_0000h|
|21_4024h|TCD Signed Source Address Offset (TCD17_SOFF)|16|RW|0000h|
|21_4026h|TCD Transfer Attributes (TCD17_ATTR)|16|RW|See<br>description|
|21_4028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD17_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|21_4028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD17_NBYTES_MLOFFYES)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

448 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|21_402Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD17_SLAST_SDA)|32|RW|0000_0000h|
|21_4030h|TCD Destination Address (TCD17_DADDR)|32|RW|0000_0000h|
|21_4034h|TCD Signed Destination Address Offset (TCD17_DOFF)|16|RW|0000h|
|21_4036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD17_CITER_ELINKNO)|16|RW|0000h|
|21_4036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD17_CITER_ELINKYES)|16|RW|0000h|
|21_4038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD17_DLAST_SGA)|32|RW|0000_0000h|
|21_403Ch|TCD Control and Status (TCD17_CSR)|16|RW|0000h|
|21_403Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD17_BITER_ELINKNO)|16|RW|0000h|
|21_403Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD17_BITER_ELINKYES)|16|RW|0000h|
|21_8000h|Channel Control and Status (CH18_CSR)|32|RW|0000_0000h|
|21_8004h|Channel Error Status (CH18_ES)|32|W1C|0000_0000h|
|21_8008h|Channel Interrupt Status (CH18_INT)|32|W1C|0000_0000h|
|21_800Ch|Channel System Bus (CH18_SBR)|32|RW|0000_8002h|
|21_8010h|Channel Priority (CH18_PRI)|32|RW|0000_0000h|
|21_8020h|TCD Source Address (TCD18_SADDR)|32|RW|0000_0000h|
|21_8024h|TCD Signed Source Address Offset (TCD18_SOFF)|16|RW|0000h|
|21_8026h|TCD Transfer Attributes (TCD18_ATTR)|16|RW|See<br>description|
|21_8028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD18_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|21_8028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD18_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|21_802Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD18_SLAST_SDA)|32|RW|0000_0000h|
|21_8030h|TCD Destination Address (TCD18_DADDR)|32|RW|0000_0000h|
|21_8034h|TCD Signed Destination Address Offset (TCD18_DOFF)|16|RW|0000h|
|21_8036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD18_CITER_ELINKNO)|16|RW|0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

449 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|21_8036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD18_CITER_ELINKYES)|16|RW|0000h|
|21_8038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD18_DLAST_SGA)|32|RW|0000_0000h|
|21_803Ch|TCD Control and Status (TCD18_CSR)|16|RW|0000h|
|21_803Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD18_BITER_ELINKNO)|16|RW|0000h|
|21_803Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD18_BITER_ELINKYES)|16|RW|0000h|
|21_C000h|Channel Control and Status (CH19_CSR)|32|RW|0000_0000h|
|21_C004h|Channel Error Status (CH19_ES)|32|W1C|0000_0000h|
|21_C008h|Channel Interrupt Status (CH19_INT)|32|W1C|0000_0000h|
|21_C00Ch|Channel System Bus (CH19_SBR)|32|RW|0000_8002h|
|21_C010h|Channel Priority (CH19_PRI)|32|RW|0000_0000h|
|21_C020h|TCD Source Address (TCD19_SADDR)|32|RW|0000_0000h|
|21_C024h|TCD Signed Source Address Offset (TCD19_SOFF)|16|RW|0000h|
|21_C026h|TCD Transfer Attributes (TCD19_ATTR)|16|RW|See<br>description|
|21_C028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD19_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|21_C028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD19_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|21_C02Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD19_SLAST_SDA)|32|RW|0000_0000h|
|21_C030h|TCD Destination Address (TCD19_DADDR)|32|RW|0000_0000h|
|21_C034h|TCD Signed Destination Address Offset (TCD19_DOFF)|16|RW|0000h|
|21_C036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD19_CITER_ELINKNO)|16|RW|0000h|
|21_C036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD19_CITER_ELINKYES)|16|RW|0000h|
|21_C038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD19_DLAST_SGA)|32|RW|0000_0000h|
|21_C03Ch|TCD Control and Status (TCD19_CSR)|16|RW|0000h|
|21_C03Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD19_BITER_ELINKNO)|16|RW|0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

450 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|21_C03Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD19_BITER_ELINKYES)|16|RW|0000h|
|22_0000h|Channel Control and Status (CH20_CSR)|32|RW|0000_0000h|
|22_0004h|Channel Error Status (CH20_ES)|32|W1C|0000_0000h|
|22_0008h|Channel Interrupt Status (CH20_INT)|32|W1C|0000_0000h|
|22_000Ch|Channel System Bus (CH20_SBR)|32|RW|0000_8002h|
|22_0010h|Channel Priority (CH20_PRI)|32|RW|0000_0000h|
|22_0020h|TCD Source Address (TCD20_SADDR)|32|RW|0000_0000h|
|22_0024h|TCD Signed Source Address Offset (TCD20_SOFF)|16|RW|0000h|
|22_0026h|TCD Transfer Attributes (TCD20_ATTR)|16|RW|See<br>description|
|22_0028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD20_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|22_0028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD20_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|22_002Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD20_SLAST_SDA)|32|RW|0000_0000h|
|22_0030h|TCD Destination Address (TCD20_DADDR)|32|RW|0000_0000h|
|22_0034h|TCD Signed Destination Address Offset (TCD20_DOFF)|16|RW|0000h|
|22_0036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD20_CITER_ELINKNO)|16|RW|0000h|
|22_0036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD20_CITER_ELINKYES)|16|RW|0000h|
|22_0038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD20_DLAST_SGA)|32|RW|0000_0000h|
|22_003Ch|TCD Control and Status (TCD20_CSR)|16|RW|0000h|
|22_003Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD20_BITER_ELINKNO)|16|RW|0000h|
|22_003Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD20_BITER_ELINKYES)|16|RW|0000h|
|22_4000h|Channel Control and Status (CH21_CSR)|32|RW|0000_0000h|
|22_4004h|Channel Error Status (CH21_ES)|32|W1C|0000_0000h|
|22_4008h|Channel Interrupt Status (CH21_INT)|32|W1C|0000_0000h|
|22_400Ch|Channel System Bus (CH21_SBR)|32|RW|0000_8002h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

451 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|22_4010h|Channel Priority (CH21_PRI)|32|RW|0000_0000h|
|22_4020h|TCD Source Address (TCD21_SADDR)|32|RW|0000_0000h|
|22_4024h|TCD Signed Source Address Offset (TCD21_SOFF)|16|RW|0000h|
|22_4026h|TCD Transfer Attributes (TCD21_ATTR)|16|RW|See<br>description|
|22_4028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD21_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|22_4028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD21_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|22_402Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD21_SLAST_SDA)|32|RW|0000_0000h|
|22_4030h|TCD Destination Address (TCD21_DADDR)|32|RW|0000_0000h|
|22_4034h|TCD Signed Destination Address Offset (TCD21_DOFF)|16|RW|0000h|
|22_4036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD21_CITER_ELINKNO)|16|RW|0000h|
|22_4036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD21_CITER_ELINKYES)|16|RW|0000h|
|22_4038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD21_DLAST_SGA)|32|RW|0000_0000h|
|22_403Ch|TCD Control and Status (TCD21_CSR)|16|RW|0000h|
|22_403Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD21_BITER_ELINKNO)|16|RW|0000h|
|22_403Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD21_BITER_ELINKYES)|16|RW|0000h|
|22_8000h|Channel Control and Status (CH22_CSR)|32|RW|0000_0000h|
|22_8004h|Channel Error Status (CH22_ES)|32|W1C|0000_0000h|
|22_8008h|Channel Interrupt Status (CH22_INT)|32|W1C|0000_0000h|
|22_800Ch|Channel System Bus (CH22_SBR)|32|RW|0000_8002h|
|22_8010h|Channel Priority (CH22_PRI)|32|RW|0000_0000h|
|22_8020h|TCD Source Address (TCD22_SADDR)|32|RW|0000_0000h|
|22_8024h|TCD Signed Source Address Offset (TCD22_SOFF)|16|RW|0000h|
|22_8026h|TCD Transfer Attributes (TCD22_ATTR)|16|RW|See<br>description|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

452 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|22_8028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD22_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|22_8028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD22_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|22_802Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD22_SLAST_SDA)|32|RW|0000_0000h|
|22_8030h|TCD Destination Address (TCD22_DADDR)|32|RW|0000_0000h|
|22_8034h|TCD Signed Destination Address Offset (TCD22_DOFF)|16|RW|0000h|
|22_8036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD22_CITER_ELINKNO)|16|RW|0000h|
|22_8036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD22_CITER_ELINKYES)|16|RW|0000h|
|22_8038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD22_DLAST_SGA)|32|RW|0000_0000h|
|22_803Ch|TCD Control and Status (TCD22_CSR)|16|RW|0000h|
|22_803Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD22_BITER_ELINKNO)|16|RW|0000h|
|22_803Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD22_BITER_ELINKYES)|16|RW|0000h|
|22_C000h|Channel Control and Status (CH23_CSR)|32|RW|0000_0000h|
|22_C004h|Channel Error Status (CH23_ES)|32|W1C|0000_0000h|
|22_C008h|Channel Interrupt Status (CH23_INT)|32|W1C|0000_0000h|
|22_C00Ch|Channel System Bus (CH23_SBR)|32|RW|0000_8002h|
|22_C010h|Channel Priority (CH23_PRI)|32|RW|0000_0000h|
|22_C020h|TCD Source Address (TCD23_SADDR)|32|RW|0000_0000h|
|22_C024h|TCD Signed Source Address Offset (TCD23_SOFF)|16|RW|0000h|
|22_C026h|TCD Transfer Attributes (TCD23_ATTR)|16|RW|See<br>description|
|22_C028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD23_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|22_C028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD23_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|22_C02Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD23_SLAST_SDA)|32|RW|0000_0000h|
|22_C030h|TCD Destination Address (TCD23_DADDR)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

453 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|22_C034h|TCD Signed Destination Address Offset (TCD23_DOFF)|16|RW|0000h|
|22_C036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD23_CITER_ELINKNO)|16|RW|0000h|
|22_C036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD23_CITER_ELINKYES)|16|RW|0000h|
|22_C038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD23_DLAST_SGA)|32|RW|0000_0000h|
|22_C03Ch|TCD Control and Status (TCD23_CSR)|16|RW|0000h|
|22_C03Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD23_BITER_ELINKNO)|16|RW|0000h|
|22_C03Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD23_BITER_ELINKYES)|16|RW|0000h|
|23_0000h|Channel Control and Status (CH24_CSR)|32|RW|0000_0000h|
|23_0004h|Channel Error Status (CH24_ES)|32|W1C|0000_0000h|
|23_0008h|Channel Interrupt Status (CH24_INT)|32|W1C|0000_0000h|
|23_000Ch|Channel System Bus (CH24_SBR)|32|RW|0000_8002h|
|23_0010h|Channel Priority (CH24_PRI)|32|RW|0000_0000h|
|23_0020h|TCD Source Address (TCD24_SADDR)|32|RW|0000_0000h|
|23_0024h|TCD Signed Source Address Offset (TCD24_SOFF)|16|RW|0000h|
|23_0026h|TCD Transfer Attributes (TCD24_ATTR)|16|RW|See<br>description|
|23_0028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD24_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|23_0028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD24_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|23_002Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD24_SLAST_SDA)|32|RW|0000_0000h|
|23_0030h|TCD Destination Address (TCD24_DADDR)|32|RW|0000_0000h|
|23_0034h|TCD Signed Destination Address Offset (TCD24_DOFF)|16|RW|0000h|
|23_0036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD24_CITER_ELINKNO)|16|RW|0000h|
|23_0036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD24_CITER_ELINKYES)|16|RW|0000h|
|23_0038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD24_DLAST_SGA)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

454 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|23_003Ch|TCD Control and Status (TCD24_CSR)|16|RW|0000h|
|23_003Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD24_BITER_ELINKNO)|16|RW|0000h|
|23_003Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD24_BITER_ELINKYES)|16|RW|0000h|
|23_4000h|Channel Control and Status (CH25_CSR)|32|RW|0000_0000h|
|23_4004h|Channel Error Status (CH25_ES)|32|W1C|0000_0000h|
|23_4008h|Channel Interrupt Status (CH25_INT)|32|W1C|0000_0000h|
|23_400Ch|Channel System Bus (CH25_SBR)|32|RW|0000_8002h|
|23_4010h|Channel Priority (CH25_PRI)|32|RW|0000_0000h|
|23_4020h|TCD Source Address (TCD25_SADDR)|32|RW|0000_0000h|
|23_4024h|TCD Signed Source Address Offset (TCD25_SOFF)|16|RW|0000h|
|23_4026h|TCD Transfer Attributes (TCD25_ATTR)|16|RW|See<br>description|
|23_4028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD25_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|23_4028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD25_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|23_402Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD25_SLAST_SDA)|32|RW|0000_0000h|
|23_4030h|TCD Destination Address (TCD25_DADDR)|32|RW|0000_0000h|
|23_4034h|TCD Signed Destination Address Offset (TCD25_DOFF)|16|RW|0000h|
|23_4036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD25_CITER_ELINKNO)|16|RW|0000h|
|23_4036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD25_CITER_ELINKYES)|16|RW|0000h|
|23_4038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD25_DLAST_SGA)|32|RW|0000_0000h|
|23_403Ch|TCD Control and Status (TCD25_CSR)|16|RW|0000h|
|23_403Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD25_BITER_ELINKNO)|16|RW|0000h|
|23_403Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD25_BITER_ELINKYES)|16|RW|0000h|
|23_8000h|Channel Control and Status (CH26_CSR)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

455 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|23_8004h|Channel Error Status (CH26_ES)|32|W1C|0000_0000h|
|23_8008h|Channel Interrupt Status (CH26_INT)|32|W1C|0000_0000h|
|23_800Ch|Channel System Bus (CH26_SBR)|32|RW|0000_8002h|
|23_8010h|Channel Priority (CH26_PRI)|32|RW|0000_0000h|
|23_8020h|TCD Source Address (TCD26_SADDR)|32|RW|0000_0000h|
|23_8024h|TCD Signed Source Address Offset (TCD26_SOFF)|16|RW|0000h|
|23_8026h|TCD Transfer Attributes (TCD26_ATTR)|16|RW|See<br>description|
|23_8028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD26_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|23_8028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD26_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|23_802Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD26_SLAST_SDA)|32|RW|0000_0000h|
|23_8030h|TCD Destination Address (TCD26_DADDR)|32|RW|0000_0000h|
|23_8034h|TCD Signed Destination Address Offset (TCD26_DOFF)|16|RW|0000h|
|23_8036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD26_CITER_ELINKNO)|16|RW|0000h|
|23_8036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD26_CITER_ELINKYES)|16|RW|0000h|
|23_8038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD26_DLAST_SGA)|32|RW|0000_0000h|
|23_803Ch|TCD Control and Status (TCD26_CSR)|16|RW|0000h|
|23_803Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD26_BITER_ELINKNO)|16|RW|0000h|
|23_803Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD26_BITER_ELINKYES)|16|RW|0000h|
|23_C000h|Channel Control and Status (CH27_CSR)|32|RW|0000_0000h|
|23_C004h|Channel Error Status (CH27_ES)|32|W1C|0000_0000h|
|23_C008h|Channel Interrupt Status (CH27_INT)|32|W1C|0000_0000h|
|23_C00Ch|Channel System Bus (CH27_SBR)|32|RW|0000_8002h|
|23_C010h|Channel Priority (CH27_PRI)|32|RW|0000_0000h|
|23_C020h|TCD Source Address (TCD27_SADDR)|32|RW|0000_0000h|
|23_C024h|TCD Signed Source Address Offset (TCD27_SOFF)|16|RW|0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

456 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|23_C026h|TCD Transfer Attributes (TCD27_ATTR)|16|RW|See<br>description|
|23_C028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD27_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|23_C028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD27_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|23_C02Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD27_SLAST_SDA)|32|RW|0000_0000h|
|23_C030h|TCD Destination Address (TCD27_DADDR)|32|RW|0000_0000h|
|23_C034h|TCD Signed Destination Address Offset (TCD27_DOFF)|16|RW|0000h|
|23_C036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD27_CITER_ELINKNO)|16|RW|0000h|
|23_C036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD27_CITER_ELINKYES)|16|RW|0000h|
|23_C038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD27_DLAST_SGA)|32|RW|0000_0000h|
|23_C03Ch|TCD Control and Status (TCD27_CSR)|16|RW|0000h|
|23_C03Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD27_BITER_ELINKNO)|16|RW|0000h|
|23_C03Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD27_BITER_ELINKYES)|16|RW|0000h|
|24_0000h|Channel Control and Status (CH28_CSR)|32|RW|0000_0000h|
|24_0004h|Channel Error Status (CH28_ES)|32|W1C|0000_0000h|
|24_0008h|Channel Interrupt Status (CH28_INT)|32|W1C|0000_0000h|
|24_000Ch|Channel System Bus (CH28_SBR)|32|RW|0000_8002h|
|24_0010h|Channel Priority (CH28_PRI)|32|RW|0000_0000h|
|24_0020h|TCD Source Address (TCD28_SADDR)|32|RW|0000_0000h|
|24_0024h|TCD Signed Source Address Offset (TCD28_SOFF)|16|RW|0000h|
|24_0026h|TCD Transfer Attributes (TCD28_ATTR)|16|RW|See<br>description|
|24_0028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD28_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|24_0028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD28_NBYTES_MLOFFYES)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

457 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|24_002Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD28_SLAST_SDA)|32|RW|0000_0000h|
|24_0030h|TCD Destination Address (TCD28_DADDR)|32|RW|0000_0000h|
|24_0034h|TCD Signed Destination Address Offset (TCD28_DOFF)|16|RW|0000h|
|24_0036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD28_CITER_ELINKNO)|16|RW|0000h|
|24_0036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD28_CITER_ELINKYES)|16|RW|0000h|
|24_0038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD28_DLAST_SGA)|32|RW|0000_0000h|
|24_003Ch|TCD Control and Status (TCD28_CSR)|16|RW|0000h|
|24_003Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD28_BITER_ELINKNO)|16|RW|0000h|
|24_003Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD28_BITER_ELINKYES)|16|RW|0000h|
|24_4000h|Channel Control and Status (CH29_CSR)|32|RW|0000_0000h|
|24_4004h|Channel Error Status (CH29_ES)|32|W1C|0000_0000h|
|24_4008h|Channel Interrupt Status (CH29_INT)|32|W1C|0000_0000h|
|24_400Ch|Channel System Bus (CH29_SBR)|32|RW|0000_8002h|
|24_4010h|Channel Priority (CH29_PRI)|32|RW|0000_0000h|
|24_4020h|TCD Source Address (TCD29_SADDR)|32|RW|0000_0000h|
|24_4024h|TCD Signed Source Address Offset (TCD29_SOFF)|16|RW|0000h|
|24_4026h|TCD Transfer Attributes (TCD29_ATTR)|16|RW|See<br>description|
|24_4028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD29_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|24_4028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD29_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|24_402Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD29_SLAST_SDA)|32|RW|0000_0000h|
|24_4030h|TCD Destination Address (TCD29_DADDR)|32|RW|0000_0000h|
|24_4034h|TCD Signed Destination Address Offset (TCD29_DOFF)|16|RW|0000h|
|24_4036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD29_CITER_ELINKNO)|16|RW|0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

458 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|24_4036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD29_CITER_ELINKYES)|16|RW|0000h|
|24_4038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD29_DLAST_SGA)|32|RW|0000_0000h|
|24_403Ch|TCD Control and Status (TCD29_CSR)|16|RW|0000h|
|24_403Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD29_BITER_ELINKNO)|16|RW|0000h|
|24_403Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD29_BITER_ELINKYES)|16|RW|0000h|
|24_8000h|Channel Control and Status (CH30_CSR)|32|RW|0000_0000h|
|24_8004h|Channel Error Status (CH30_ES)|32|W1C|0000_0000h|
|24_8008h|Channel Interrupt Status (CH30_INT)|32|W1C|0000_0000h|
|24_800Ch|Channel System Bus (CH30_SBR)|32|RW|0000_8002h|
|24_8010h|Channel Priority (CH30_PRI)|32|RW|0000_0000h|
|24_8020h|TCD Source Address (TCD30_SADDR)|32|RW|0000_0000h|
|24_8024h|TCD Signed Source Address Offset (TCD30_SOFF)|16|RW|0000h|
|24_8026h|TCD Transfer Attributes (TCD30_ATTR)|16|RW|See<br>description|
|24_8028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD30_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|24_8028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD30_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|24_802Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD30_SLAST_SDA)|32|RW|0000_0000h|
|24_8030h|TCD Destination Address (TCD30_DADDR)|32|RW|0000_0000h|
|24_8034h|TCD Signed Destination Address Offset (TCD30_DOFF)|16|RW|0000h|
|24_8036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD30_CITER_ELINKNO)|16|RW|0000h|
|24_8036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD30_CITER_ELINKYES)|16|RW|0000h|
|24_8038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD30_DLAST_SGA)|32|RW|0000_0000h|
|24_803Ch|TCD Control and Status (TCD30_CSR)|16|RW|0000h|
|24_803Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD30_BITER_ELINKNO)|16|RW|0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

459 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|24_803Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD30_BITER_ELINKYES)|16|RW|0000h|
|24_C000h|Channel Control and Status (CH31_CSR)|32|RW|0000_0000h|
|24_C004h|Channel Error Status (CH31_ES)|32|W1C|0000_0000h|
|24_C008h|Channel Interrupt Status (CH31_INT)|32|W1C|0000_0000h|
|24_C00Ch|Channel System Bus (CH31_SBR)|32|RW|0000_8002h|
|24_C010h|Channel Priority (CH31_PRI)|32|RW|0000_0000h|
|24_C020h|TCD Source Address (TCD31_SADDR)|32|RW|0000_0000h|
|24_C024h|TCD Signed Source Address Offset (TCD31_SOFF)|16|RW|0000h|
|24_C026h|TCD Transfer Attributes (TCD31_ATTR)|16|RW|See<br>description|
|24_C028h|TCD Transfer Size Without Minor Loop Offsets<br>(TCD31_NBYTES_MLOFFNO)|32|RW|0000_0000h|
|24_C028h|TCD Transfer Size with Minor Loop Offsets<br>(TCD31_NBYTES_MLOFFYES)|32|RW|0000_0000h|
|24_C02Ch|TCD Last Source Address Adjustment / Store DADDR Address<br>(TCD31_SLAST_SDA)|32|RW|0000_0000h|
|24_C030h|TCD Destination Address (TCD31_DADDR)|32|RW|0000_0000h|
|24_C034h|TCD Signed Destination Address Offset (TCD31_DOFF)|16|RW|0000h|
|24_C036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD31_CITER_ELINKNO)|16|RW|0000h|
|24_C036h|TCD Current Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD31_CITER_ELINKYES)|16|RW|0000h|
|24_C038h|TCD Last Destination Address Adjustment / Scatter Gather Address<br>(TCD31_DLAST_SGA)|32|RW|0000_0000h|
|24_C03Ch|TCD Control and Status (TCD31_CSR)|16|RW|0000h|
|24_C03Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Disabled) (TCD31_BITER_ELINKNO)|16|RW|0000h|
|24_C03Eh|TCD Beginning Major Loop Count (Minor Loop Channel Linking<br>Enabled) (TCD31_BITER_ELINKYES)|16|RW|0000h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

460 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

#### 14.5.2.2 Channel Control and Status (CH0_CSR - CH31_CSR) 

##### Offset 

|Register|Offset|
|---|---|
|CH0_CSR|0h|
|CH1_CSR|4000h|
|CH2_CSR|8000h|
|CH3_CSR|C000h|
|CH4_CSR|1_0000h|
|CH5_CSR|1_4000h|
|CH6_CSR|1_8000h|
|CH7_CSR|1_C000h|
|CH8_CSR|2_0000h|
|CH9_CSR|2_4000h|
|CH10_CSR|2_8000h|
|CH11_CSR|2_C000h|
|CH12_CSR|20_0000h|
|CH13_CSR|20_4000h|
|CH14_CSR|20_8000h|
|CH15_CSR|20_C000h|
|CH16_CSR|21_0000h|
|CH17_CSR|21_4000h|
|CH18_CSR|21_8000h|
|CH19_CSR|21_C000h|
|CH20_CSR|22_0000h|
|CH21_CSR|22_4000h|
|CH22_CSR|22_8000h|
|CH23_CSR|22_C000h|
|CH24_CSR|23_0000h|
|CH25_CSR|23_4000h|
|CH26_CSR|23_8000h|
|CH27_CSR|23_C000h|
|CH28_CSR|24_0000h|
|CH29_CSR|24_4000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

461 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Register|Offset|
|---|---|
|CH30_CSR|24_8000h|
|CH31_CSR|24_C000h|



##### Function 

This register contains several fields related to hardware and interrupt requests, configuration, and status for the given channel. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0462-07.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>ACTIV<br>R DONE<br>E<br>W W1C 0<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>EBW  EEI  EARQ  ERQ<br>W 0<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31|Channel Active|
|ACTIVE|The ACTIVE field indicates the channel was selected by arbitration and is executing the prescribed<br>transfers. The eDMA sets it to 1 when channel service begins, and clears it to 0 as the minor loop<br>completes or when any error condition is detected. Except for dynamic scatter/gather or dynamic<br>channel linking, you must not modify the transfer control descriptor when a channel is active.|
|30|Channel Done|
|DONE|The DONE field indicates the eDMA has completed the major loop. The eDMA engine sets this field as<br>the CITER count reaches zero. If enabled, the eDMA generates an interrupt request corresponding to this<br>completed channel. The software clears it, or the hardware clears it when the channel is activated.<br>This field must be cleared to 0 before writing the MAJORELINK or ESG fields.<br>~~NOTE~~|
|29-4|Reserved|
|—<br>3<br>EBW|Enable Buffered Writes|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

462 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||When buffered writes are enabled, all writes except for the last write sequence of the minor loop are<br>signaled by the eDMA as bufferable.<br>0b - Buffered writes on system bus disabled. Buffered writes on system bus disabled<br>1b - Buffered writes on system bus enabled. Bufferable write signal asserted on all system bus<br>writes except during last write sequence|
|2<br>EEI|Enable Error Interrupt<br>The EEI field enables the error interrupt signal for the channel. The DMA error indicator and the error<br>interrupt enable flag must be asserted before an error interrupt request for a given channel is asserted to<br>the interrupt controller.<br>0b - Error signal for corresponding channel does not generate error interrupt<br>1b - Assertion of error signal for corresponding channel generates error interrupt request|
|1|Enable Asynchronous DMA Request In Stop Mode For Channel|
|EARQ|The enable asynchronous DMA request field (EARQ) does not affect DMA operations. When set to 1,<br>this field allows the hardware service request enable field (ERQ) to propagate out of the DMA to the<br>power controller. When cleared to 0, this field masks the hardware service request enable field to the<br>power controller.<br>0b - Disable asynchronous DMA request for the channel<br>1b - Enable asynchronous DMA request for the channel|
|0<br>ERQ|Enable DMA Request<br>Disable a channel's hardware service request at the source before clearing the channel's ERQ field.<br>The DMA hardware request input signal and the enable request field (ERQ) must be asserted before a<br>channel's hardware service request is accepted. The state of the eDMA enable request field does not<br>affect a channel service request made explicitly through software or channel linking. The state of the<br>ERQ field does not affect the channel's START field.<br>0b - DMA hardware request signal for corresponding channel disabled<br>1b - DMA hardware request signal for corresponding channel enabled|



#### 14.5.2.3 Channel Error Status (CH0_ES - CH31_ES) 

##### Offset 

|Register|Offset|
|---|---|
|CH0_ES|4h|
|CH1_ES|4004h|
|CH2_ES|8004h|
|CH3_ES|C004h|
|CH4_ES|1_0004h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

463 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

Table continued from the previous page... 

|Register|Offset|
|---|---|
|CH5_ES|1_4004h|
|CH6_ES|1_8004h|
|CH7_ES|1_C004h|
|CH8_ES|2_0004h|
|CH9_ES|2_4004h|
|CH10_ES|2_8004h|
|CH11_ES|2_C004h|
|CH12_ES|20_0004h|
|CH13_ES|20_4004h|
|CH14_ES|20_8004h|
|CH15_ES|20_C004h|
|CH16_ES|21_0004h|
|CH17_ES|21_4004h|
|CH18_ES|21_8004h|
|CH19_ES|21_C004h|
|CH20_ES|22_0004h|
|CH21_ES|22_4004h|
|CH22_ES|22_8004h|
|CH23_ES|22_C004h|
|CH24_ES|23_0004h|
|CH25_ES|23_4004h|
|CH26_ES|23_8004h|
|CH27_ES|23_C004h|
|CH28_ES|24_0004h|
|CH29_ES|24_4004h|
|CH30_ES|24_8004h|
|CH31_ES|24_C004h|



##### Function 

The ES provides information concerning the last recorded channel error. Channel errors can be caused by: 

- An illegal setting in the transfer control descriptor 

- An error termination to a bus master read or write cycle 

The ERR field signals the presence of an error for the channel. The eDMA engine signals the occurrence of an error condition by setting the appropriate field in this register. The outputs of this register are enabled by the contents of the CHn_CSR[EEI] field, 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

464 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

then logically summed across all channels to form an error interrupt request, which may be routed to the interrupt controller. In addition, this enabled error status is logically OR'd onto the channel done interrupt, CHn_INT[INT], thus forming a done or error interrupt on a per channel basis. 

During the execution of the interrupt service routine associated with any DMA errors, it is software's responsibility to clear the appropriate bit, negating the error-interrupt request. The normal DMA channel completion indicators (setting the transfer control descriptor DONE flag and the possible assertion of an interrupt request) are not affected when eDMA detects an error. The contents of this ERR register field can also be polled because a non-zero value indicates the presence of a channel error, regardless of the state of the EEI mask. 

The state of any given channel's error indicators is affected by writes to this register. Writing a 1 to the ERR field clears the channel's error status, and writing a 0 has no effect. 

An unspecified error, where only the ERR field is set to 1, indicates that either a transfer was cancelled with an error or else an uncorrectable TCD error occurred. The Management Page Error Status register has full view of the error condition. 

See Fault reporting and handling for more details. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0465-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R ERR  Reserved<br>W W1C 0<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved  SAE  SOE  DAE  DOE  NCE  SGE  SBE  DBE<br>W 0<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Error In Channel|
|ERR|0b - An error in this channel has not occurred<br>1b - An error in this channel has occurred|
|30-8|Reserved|
|—||
|7|Source Address Error|
|SAE|TCDn_SADDR is inconsistent with TCDn_ATTR[SSIZE].|
||0b - No source address configuration error|
||1b - Last recorded error was a configuration error detected in the TCDn_SADDR field|
|6|Source Offset Error|
|SOE|TCDn_SOFF is inconsistent with TCDn_ATTR[SSIZE].|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

465 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - No source offset configuration error<br>1b - Last recorded error was a configuration error detected in the TCDn_SOFF field|
|5<br>DAE|Destination Address Error<br>TCDn_DADDR is inconsistent with TCDn_ATTR[DSIZE].<br>0b - No destination address configuration error<br>1b - Last recorded error was a configuration error detected in the TCDn_DADDR field|
|4|Destination Offset Error|
|DOE|TCDn_DOFF is inconsistent with TCDn_ATTR[DSIZE].<br>0b - No destination offset configuration error<br>1b - Last recorded error was a configuration error detected in the TCDn_DOFF field|
|3|NBYTES/CITER Configuration Error|
|NCE|This error indicates that one of the following has occurred:<br>• TCDn_NBYTES is not a multiple of TCDn_ATTR[SSIZE] and TCDn_ATTR[DSIZE]<br>• TCDn_CITER[CITER] is equal to zero<br>• TCDn_CITER[ELINK] is not equal to TCDn_BITER[ELINK]<br>0b - No NBYTES/CITER configuration error<br>1b - Last recorded error was a configuration error detected in the TCDn_NBYTES or<br>TCDn_CITER fields|
|2|Scatter/Gather Configuration Error|
|SGE|When this field is 1, it indicates thatTCDn_DLAST_SGAis not on a 32-byte boundary. This field is<br>checked at the beginning of a scatter/gather operation after major loop completion ifTCDn_CSR[ESG]is<br>enabled.<br>0b - No scatter/gather configuration error<br>1b - Last recorded error was a configuration error detected in the TCDn_DLAST_SGA field|
|1|Source Bus Error|
|SBE|0b - No source bus error<br>1b - Last recorded error was bus error on source read|
|0|Destination Bus Error|
|DBE|0b - No destination bus error<br>1b - Last recorded error was bus error on destination write|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

466 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

#### 14.5.2.4 Channel Interrupt Status (CH0_INT - CH31_INT) 

##### Offset 

|Register|Offset|
|---|---|
|CH0_INT|8h|
|CH1_INT|4008h|
|CH2_INT|8008h|
|CH3_INT|C008h|
|CH4_INT|1_0008h|
|CH5_INT|1_4008h|
|CH6_INT|1_8008h|
|CH7_INT|1_C008h|
|CH8_INT|2_0008h|
|CH9_INT|2_4008h|
|CH10_INT|2_8008h|
|CH11_INT|2_C008h|
|CH12_INT|20_0008h|
|CH13_INT|20_4008h|
|CH14_INT|20_8008h|
|CH15_INT|20_C008h|
|CH16_INT|21_0008h|
|CH17_INT|21_4008h|
|CH18_INT|21_8008h|
|CH19_INT|21_C008h|
|CH20_INT|22_0008h|
|CH21_INT|22_4008h|
|CH22_INT|22_8008h|
|CH23_INT|22_C008h|
|CH24_INT|23_0008h|
|CH25_INT|23_4008h|
|CH26_INT|23_8008h|
|CH27_INT|23_C008h|
|CH28_INT|24_0008h|
|CH29_INT|24_4008h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

467 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Register|Offset|
|---|---|
|CH30_INT|24_8008h|
|CH31_INT|24_C008h|



##### Function 

The INT field signals the presence of an interrupt request for the channel. Depending on the appropriate bit setting in the transfe control descriptors, the eDMA engine generates an interrupt on data transfer completion or an error condition. 

The outputs of this register are directly routed to the interrupt controller. During the interrupt service routine associated with any given channel, it is the software's responsibility to clear the appropriate bit, negating the interrupt request. On writes to INT, a 1 clears the channel's interrupt request. A zero has no effect on the channel's current interrupt status. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0468-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 INT<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-1<br>—|Reserved|
|0|Interrupt Request|
|INT|0b - Interrupt request for corresponding channel cleared|
||1b - Interrupt request for corresponding channel active|



#### 14.5.2.5 Channel System Bus (CH0_SBR - CH31_SBR) 

##### Offset 

|Register|Offset|
|---|---|
|CH0_SBR|Ch|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

468 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

Table continued from the previous page... 

|Register|Offset|
|---|---|
|CH1_SBR|400Ch|
|CH2_SBR|800Ch|
|CH3_SBR|C00Ch|
|CH4_SBR|1_000Ch|
|CH5_SBR|1_400Ch|
|CH6_SBR|1_800Ch|
|CH7_SBR|1_C00Ch|
|CH8_SBR|2_000Ch|
|CH9_SBR|2_400Ch|
|CH10_SBR|2_800Ch|
|CH11_SBR|2_C00Ch|
|CH12_SBR|20_000Ch|
|CH13_SBR|20_400Ch|
|CH14_SBR|20_800Ch|
|CH15_SBR|20_C00Ch|
|CH16_SBR|21_000Ch|
|CH17_SBR|21_400Ch|
|CH18_SBR|21_800Ch|
|CH19_SBR|21_C00Ch|
|CH20_SBR|22_000Ch|
|CH21_SBR|22_400Ch|
|CH22_SBR|22_800Ch|
|CH23_SBR|22_C00Ch|
|CH24_SBR|23_000Ch|
|CH25_SBR|23_400Ch|
|CH26_SBR|23_800Ch|
|CH27_SBR|23_C00Ch|
|CH28_SBR|24_000Ch|
|CH29_SBR|24_400Ch|
|CH30_SBR|24_800Ch|
|CH31_SBR|24_C00Ch|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

469 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Function 

The Channel System Bus register places identification and attribute information on the system bus interface for the eDMA. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||Rese<br>0|rved<br>|||||||ATTR||EMI|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|PAL||||||0|||||||MI|D||
|W|||||||||||||||||
|Reset|1|0|0|0|0|0|0|0|0|0|0|0|0|0|1|0|



##### Fields 

|Field|Function|
|---|---|
|31-20|Reserved|
|—||
|19-17|Attribute Output|
|ATTR|DMA's system bus attribute output value.|
|16|Enable Master ID Replication|
|EMI|The eDMA master ID replication field allows the eDMA to use the same protection level and system bus ID<br>of the master programming the eDMA's TCD. When enabled, the eDMA uses the master ID and protection<br>level stored in theCHn_SBRregisters, instead of the eDMA's default values. When a master (for example<br>a core) programs a TCD, its master ID and protection level are captured when the TCDn_CSR control<br>attributes are written. A scatter/gather operation does not affect theCHn_SBRregisters. You can write the<br>EMI only ifCSR[GMRC]= 1, which means Global Master ID Replication Control is enabled; otherwise, the<br>EMI is forced to zero.<br>If master ID replication is disabled, the privileged protection level (Supervisor mode) for<br>DMA transfers is used.<br>~~NOTE~~|
||0b - Master ID replication is disabled<br>1b - Master ID replication is enabled|
|15|Privileged Access Level|
|PAL|This field controls DMA's protection level on the system bus when the channel is active.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

470 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||When you enable master ID replication, the value captured in this register is the privilege<br>level of the core or other master writing the channel's transfer control descriptor, which is the<br>lower byte of TCDn_CSR.<br>~~NOTE~~|
||0b - User protection level for DMA transfers<br>1b - Privileged protection level for DMA transfers|
|14-4<br>—|Reserved|
|3-0|Master ID|
|MID|This field controls the DMA's master ID on the system bus when the channel is active.<br>The ID captured in this register reflects the master ID of the core or other master writing the<br>channel's control attributes, which are in the lower byte of TCDn_CSR.<br>~~NOTE~~|



#### 14.5.2.6 Channel Priority (CH0_PRI - CH31_PRI) 

##### Offset 

|Register|Offset|
|---|---|
|CH0_PRI|10h|
|CH1_PRI|4010h|
|CH2_PRI|8010h|
|CH3_PRI|C010h|
|CH4_PRI|1_0010h|
|CH5_PRI|1_4010h|
|CH6_PRI|1_8010h|
|CH7_PRI|1_C010h|
|CH8_PRI|2_0010h|
|CH9_PRI|2_4010h|
|CH10_PRI|2_8010h|
|CH11_PRI|2_C010h|
|CH12_PRI|20_0010h|
|CH13_PRI|20_4010h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

471 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Register|Offset|
|---|---|
|CH14_PRI|20_8010h|
|CH15_PRI|20_C010h|
|CH16_PRI|21_0010h|
|CH17_PRI|21_4010h|
|CH18_PRI|21_8010h|
|CH19_PRI|21_C010h|
|CH20_PRI|22_0010h|
|CH21_PRI|22_4010h|
|CH22_PRI|22_8010h|
|CH23_PRI|22_C010h|
|CH24_PRI|23_0010h|
|CH25_PRI|23_4010h|
|CH26_PRI|23_8010h|
|CH27_PRI|23_C010h|
|CH28_PRI|24_0010h|
|CH29_PRI|24_4010h|
|CH30_PRI|24_8010h|
|CH31_PRI|24_C010h|



##### Function 

The contents of these registers define unique priorities associated with each channel within the same channel group. Channel grouping is programmed via Channel Arbitration Group (CH0_GRPRI - CH31_GRPRI). 

The channel priorities within a group are evaluated by numeric value; for example, 0 is the lowest priority, 1 is the next higher priority, then 2, 3, and so on. Software must program the channel priorities with unique values; otherwise, channel numbers with the same, non-zero value, will be selected based on channel number with the higher channel number having higher priority. 

If more than one channel in a group has an arbitration priority level value of zero, then the arbitration mode field CSR[ERCA] is used to determine the arbitration scheme for all channels with APL=0 within a group. 

When you enable round-robin channel arbitration (CSR[ERCA] = 1), all channels with APL=0 within a group will use a round-robin arbitration scheme, which rotates among these channels requesting service without regard to priority. Round-robin provides a fairness mechanism within an arbitration group. 

When you enable fixed-priority channel arbitration (CSR[ERCA] = 0), eDMA selects channels with APL=0 based on channel number, with the higher channel number having higher priority. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

472 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|ECP|DPA|||||||Reser<br>0|ved|||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||||||Reserved<br>0||||||||APL||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|Enable Channel Preemption|
|ECP|0b - Channel cannot be suspended by a higher-priority channel's service request|
||1b - Channel can be temporarily suspended by a higher-priority channel's service request|
|30|Disable Preempt Ability|
|DPA|0b - Channel can suspend a lower-priority channel|
||1b - Channel cannot suspend any other channel, regardless of channel priority|
|29-3|Reserved|
|—||
|2-0|Arbitration Priority Level|
|APL|Channel priority level for arbitration within the assigned arbitration group.|



#### 14.5.2.7 TCD Source Address (TCD0_SADDR - TCD31_SADDR) 

##### Offset 

|Register|Offset|
|---|---|
|TCD0_SADDR|20h|
|TCD1_SADDR|4020h|
|TCD2_SADDR|8020h|
|TCD3_SADDR|C020h|
|TCD4_SADDR|1_0020h|
|TCD5_SADDR|1_4020h|
|TCD6_SADDR|1_8020h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

473 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

Table continued from the previous page... 

|Register|Offset|
|---|---|
|TCD7_SADDR|1_C020h|
|TCD8_SADDR|2_0020h|
|TCD9_SADDR|2_4020h|
|TCD10_SADDR|2_8020h|
|TCD11_SADDR|2_C020h|
|TCD12_SADDR|20_0020h|
|TCD13_SADDR|20_4020h|
|TCD14_SADDR|20_8020h|
|TCD15_SADDR|20_C020h|
|TCD16_SADDR|21_0020h|
|TCD17_SADDR|21_4020h|
|TCD18_SADDR|21_8020h|
|TCD19_SADDR|21_C020h|
|TCD20_SADDR|22_0020h|
|TCD21_SADDR|22_4020h|
|TCD22_SADDR|22_8020h|
|TCD23_SADDR|22_C020h|
|TCD24_SADDR|23_0020h|
|TCD25_SADDR|23_4020h|
|TCD26_SADDR|23_8020h|
|TCD27_SADDR|23_C020h|
|TCD28_SADDR|24_0020h|
|TCD29_SADDR|24_4020h|
|TCD30_SADDR|24_8020h|
|TCD31_SADDR|24_C020h|



Function 

This register contains the address for the read transactions. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

474 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0475-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>SADDR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>SADDR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Source Address|
|SADDR|Memory address pointing to the source data.|



#### 14.5.2.8 TCD Signed Source Address Offset (TCD0_SOFF - TCD31_SOFF) 

##### Offset 

|Register|Offset|
|---|---|
|TCD0_SOFF|24h|
|TCD1_SOFF|4024h|
|TCD2_SOFF|8024h|
|TCD3_SOFF|C024h|
|TCD4_SOFF|1_0024h|
|TCD5_SOFF|1_4024h|
|TCD6_SOFF|1_8024h|
|TCD7_SOFF|1_C024h|
|TCD8_SOFF|2_0024h|
|TCD9_SOFF|2_4024h|
|TCD10_SOFF|2_8024h|
|TCD11_SOFF|2_C024h|
|TCD12_SOFF|20_0024h|
|TCD13_SOFF|20_4024h|
|TCD14_SOFF|20_8024h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

475 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Register|Offset|
|---|---|
|TCD15_SOFF|20_C024h|
|TCD16_SOFF|21_0024h|
|TCD17_SOFF|21_4024h|
|TCD18_SOFF|21_8024h|
|TCD19_SOFF|21_C024h|
|TCD20_SOFF|22_0024h|
|TCD21_SOFF|22_4024h|
|TCD22_SOFF|22_8024h|
|TCD23_SOFF|22_C024h|
|TCD24_SOFF|23_0024h|
|TCD25_SOFF|23_4024h|
|TCD26_SOFF|23_8024h|
|TCD27_SOFF|23_C024h|
|TCD28_SOFF|24_0024h|
|TCD29_SOFF|24_4024h|
|TCD30_SOFF|24_8024h|
|TCD31_SOFF|24_C024h|



##### Function 

This register contains the sign-extended value added to Source Address register after each read transaction. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0476-07.png)


<!-- Start of picture text -->
Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>SOFF<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|15-0|Source Address Signed Offset|
|SOFF|Sign-extended offset applied to the current source address to form the next-state value as each source<br>read is completed.|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

476 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

#### 14.5.2.9 TCD Transfer Attributes (TCD0_ATTR - TCD31_ATTR) 

##### Offset 

|Register|Offset|
|---|---|
|TCD0_ATTR|26h|
|TCD1_ATTR|4026h|
|TCD2_ATTR|8026h|
|TCD3_ATTR|C026h|
|TCD4_ATTR|1_0026h|
|TCD5_ATTR|1_4026h|
|TCD6_ATTR|1_8026h|
|TCD7_ATTR|1_C026h|
|TCD8_ATTR|2_0026h|
|TCD9_ATTR|2_4026h|
|TCD10_ATTR|2_8026h|
|TCD11_ATTR|2_C026h|
|TCD12_ATTR|20_0026h|
|TCD13_ATTR|20_4026h|
|TCD14_ATTR|20_8026h|
|TCD15_ATTR|20_C026h|
|TCD16_ATTR|21_0026h|
|TCD17_ATTR|21_4026h|
|TCD18_ATTR|21_8026h|
|TCD19_ATTR|21_C026h|
|TCD20_ATTR|22_0026h|
|TCD21_ATTR|22_4026h|
|TCD22_ATTR|22_8026h|
|TCD23_ATTR|22_C026h|
|TCD24_ATTR|23_0026h|
|TCD25_ATTR|23_4026h|
|TCD26_ATTR|23_8026h|
|TCD27_ATTR|23_C026h|
|TCD28_ATTR|24_0026h|
|TCD29_ATTR|24_4026h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

477 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Register|Offset|
|---|---|
|TCD30_ATTR|24_8026h|
|TCD31_ATTR|24_C026h|



##### Function 

This register contains size and option modulo addressing information for source and destination addresses. 

##### Diagram 

|Bits|15|14|13|12|11|10<br>9<br>8|7<br>6<br>5<br>4|3|2<br>1<br>0|
|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||SMOD|||SSIZE|DMOD||DSIZE|
|Reset|u|u|u|u|u|u<br>u<br>u|u<br>u<br>u<br>u|u|u<br>u<br>u|



##### Fields 

|Field|Function|
|---|---|
|15-11|Source Address Modulo|
|SMOD|This field defines a specific address range, which is the value after the SADDR + SOFF calculation is<br>performed on the original register value. Setting this field makes it easy to implement a circular data queue.<br>For data queues requiring power-of-2-sized bytes, the queue must start at a 0-modulo-size address and<br>the SMOD field must be set to the appropriate value for the queue, freezing the required number of upper<br>address bits.<br>The value programmed into this field specifies the number of lower address bits that are allowed to change.<br>For a circular queue application, you typically set TCDn_SOFF[SOFF] to the transfer size to implement<br>post-increment addressing, with the SMOD function constraining the addresses to a 0-modulo-size range.<br>0_0000b - Source address modulo feature disabled|
||0_0001b - Source address modulo feature enabled for any non-zero value [1-31]|
|10-8|Source Data Transfer Size|
|SSIZE|000b - 8-bit<br>001b - 16-bit|
||010b - 32-bit|
||011b - 64-bit|
||100b - 16-byte|
||101b - 32-byte|
||110b - 64-byte|
||111b - Reserved|
|7-3|Destination Address Modulo|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

478 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|DMOD|See the SMOD definition.|
|2-0|Destination Data Transfer Size|
|DSIZE|See the SSIZE definition.|



- 14.5.2.10 TCD Transfer Size Without Minor Loop Offsets (TCD0_NBYTES_MLOFFNO - TCD31_NBYTES_MLOFFNO) 

##### Offset 

|Register|Offset|
|---|---|
|TCD0_NBYTES_MLOFF<br>NO|28h|
|TCD1_NBYTES_MLOFF<br>NO|4028h|
|TCD2_NBYTES_MLOFF<br>NO|8028h|
|TCD3_NBYTES_MLOFF<br>NO|C028h|
|TCD4_NBYTES_MLOFF<br>NO|1_0028h|
|TCD5_NBYTES_MLOFF<br>NO|1_4028h|
|TCD6_NBYTES_MLOFF<br>NO|1_8028h|
|TCD7_NBYTES_MLOFF<br>NO|1_C028h|
|TCD8_NBYTES_MLOFF<br>NO|2_0028h|
|TCD9_NBYTES_MLOFF<br>NO|2_4028h|
|TCD10_NBYTES_MLOF<br>FNO|2_8028h|
|TCD11_NBYTES_MLOF<br>FNO|2_C028h|
|TCD12_NBYTES_MLOF<br>FNO|20_0028h|
|TCD13_NBYTES_MLOF<br>FNO|20_4028h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

479 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

Table continued from the previous page... 

|Registe|r|Offset|
|---|---|---|
|TCD14_<br>FNO|NBYTES_MLOF|20_8028h|
|TCD15_<br>FNO|NBYTES_MLOF|20_C028h|
|TCD16_<br>FNO|NBYTES_MLOF|21_0028h|
|TCD17_<br>FNO|NBYTES_MLOF|21_4028h|
|TCD18_<br>FNO|NBYTES_MLOF|21_8028h|
|TCD19_<br>FNO|NBYTES_MLOF|21_C028h|
|TCD20_<br>FNO|NBYTES_MLOF|22_0028h|
|TCD21_<br>FNO|NBYTES_MLOF|22_4028h|
|TCD22_<br>FNO|NBYTES_MLOF|22_8028h|
|TCD23_<br>FNO|NBYTES_MLOF|22_C028h|
|TCD24_<br>FNO|NBYTES_MLOF|23_0028h|
|TCD25_<br>FNO|NBYTES_MLOF|23_4028h|
|TCD26_<br>FNO|NBYTES_MLOF|23_8028h|
|TCD27_<br>FNO|NBYTES_MLOF|23_C028h|
|TCD28_<br>FNO|NBYTES_MLOF|24_0028h|
|TCD29_<br>FNO|NBYTES_MLOF|24_4028h|
|TCD30_<br>FNO|NBYTES_MLOF|24_8028h|
|TCD31_<br>FNO|NBYTES_MLOF|24_C028h|



Function 

The TCDn_NBYTES field defines the number of bytes to transfer per service request. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

480 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

Minor loop offsets are address offset values added to the final source address (TCDn_SADDR), or destination address (TCDn_DADDR), upon minor loop completion. Minor loop completion is when the channel has finished the service request and has transferred NBYTES. When minor loop offsets are enabled, the minor loop offset value (TCDn_NBYTES_MLOFFYES[MLOFF]) is added to the final source address (TCDn_SADDR), to the final destination address (TCDn_DADDR), or to both, prior to the addresses being written back to the TCD. If the major loop is complete, the minor loop offset is ignored and the major loop address offsets (TCDn_SLAST_SDA and TCDn_DLAST_SGA) are used to compute the next TCDn_SADDR and TCDn_DADDR values. 

When minor loop mapping is enabled (SMLOE or DMLOE is 1), TCDn_NBYTES_MLOFFNO/TCDn_NBYTES_MLOFFYES is redefined. A portion of TCDn_NBYTES_MLOFFNO/TCDn_NBYTES_MLOFFYES is used to specify multiple fields: 

- A source enable bit (SMLOE) to specify the minor loop offset must be applied to the source address (TCDn_SADDR) upon minor loop completion 

- A destination enable bit (DMLOE) to specify the minor loop offset must be applied to the destination address (TCDn_DADDR) upon minor loop completion 

- The sign extended minor loop offset value (MLOFF) 

The same offset value (MLOFF) is used for both source and destination minor loop offsets. When either minor loop offset is enabled (SMLOE set or DMLOE set), the NBYTES field is reduced to 10 bits. If both minor loop offsets are disabled (SMLOE cleared and DMLOE cleared), the NBYTES field is a 30-bit vector. 

One of two register profiles (this register or TCDn_NBYTES_MLOFFYES), defines the number of bytes to transfer per request. Which register to use depends on whether source or destination minor loop mapping is enabled. 

TCDn_NBYTES_MLOFFNO/TCDn_NBYTES_MLOFFYES is defined as follows: 

- If SMLOE = 0 and DMLOE = 0, then see the TCDn_NBYTES_MLOFFNO register description. 

- If either SMLOE or DMLOE is 1, then see the TCDn_NBYTES_MLOFFYES register description. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0481-13.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R SMLO DMLO<br>NBYTES<br>W E  E<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>NBYTES<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31|Source Minor Loop Offset Enable|
|SMLOE|Selects whether the minor loop offset is applied to the source address upon minor loop completion.|
||0b - Minor loop offset not applied to SADDR|
||1b - Minor loop offset applied to SADDR|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

481 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|30|Destination Minor Loop Offset Enable|
|DMLOE|Selects whether the minor loop offset is applied to the destination address upon minor loop completion.<br>0b - Minor loop offset not applied to DADDR<br>1b - Minor loop offset applied to DADDR|
|29-0|Number of Bytes To Transfer Per Service Request|
|NBYTES|Number of bytes to be transferred for each service request of the channel.<br>When a channel activates, the module loads the appropriate TCD contents into the eDMA engine and<br>performs the appropriate reads and writes until the byte transfer count has been reached. This process is<br>normally an indivisible operation and cannot be halted. It can, however, be stalled by using the bandwidth<br>control field, or via preemption.<br>After the byte count is exhausted, the SADDR and DADDR values are written back into the TCD memory,<br>and the major loop iteration count (CITER) is decremented by one and written back to the TCD memory. If<br>the major iteration count is complete, additional processing is performed.|



#### 14.5.2.11 TCD Transfer Size with Minor Loop Offsets (TCD0_NBYTES_MLOFFYES - TCD31_NBYTES_MLOFFYES) 

##### Offset 

|Regist|er|Offset|
|---|---|---|
|TCD0_<br>YES|NBYTES_MLOFF|28h|
|TCD1_<br>YES|NBYTES_MLOFF|4028h|
|TCD2_<br>YES|NBYTES_MLOFF|8028h|
|TCD3_<br>YES|NBYTES_MLOFF|C028h|
|TCD4_<br>YES|NBYTES_MLOFF|1_0028h|
|TCD5_<br>YES|NBYTES_MLOFF|1_4028h|
|TCD6_<br>YES|NBYTES_MLOFF|1_8028h|
|TCD7_<br>YES|NBYTES_MLOFF|1_C028h|
|TCD8_<br>YES|NBYTES_MLOFF|2_0028h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

482 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

Table continued from the previous page... 

|Register|Offset|
|---|---|
|TCD9_NBYTES_MLOFF<br>YES|2_4028h|
|TCD10_NBYTES_MLOF<br>FYES|2_8028h|
|TCD11_NBYTES_MLOF<br>FYES|2_C028h|
|TCD12_NBYTES_MLOF<br>FYES|20_0028h|
|TCD13_NBYTES_MLOF<br>FYES|20_4028h|
|TCD14_NBYTES_MLOF<br>FYES|20_8028h|
|TCD15_NBYTES_MLOF<br>FYES|20_C028h|
|TCD16_NBYTES_MLOF<br>FYES|21_0028h|
|TCD17_NBYTES_MLOF<br>FYES|21_4028h|
|TCD18_NBYTES_MLOF<br>FYES|21_8028h|
|TCD19_NBYTES_MLOF<br>FYES|21_C028h|
|TCD20_NBYTES_MLOF<br>FYES|22_0028h|
|TCD21_NBYTES_MLOF<br>FYES|22_4028h|
|TCD22_NBYTES_MLOF<br>FYES|22_8028h|
|TCD23_NBYTES_MLOF<br>FYES|22_C028h|
|TCD24_NBYTES_MLOF<br>FYES|23_0028h|
|TCD25_NBYTES_MLOF<br>FYES|23_4028h|
|TCD26_NBYTES_MLOF<br>FYES|23_8028h|
|TCD27_NBYTES_MLOF<br>FYES|23_C028h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

483 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Register|Offset|
|---|---|
|TCD28_NBYTES_MLOF<br>FYES|24_0028h|
|TCD29_NBYTES_MLOF<br>FYES|24_4028h|
|TCD30_NBYTES_MLOF<br>FYES|24_8028h|
|TCD31_NBYTES_MLOF<br>FYES|24_C028h|



##### Function 

The TCDn_NBYTES field defines the number of bytes to transfer per service request. 

Minor loop offset is an address offset value added to the final source address (TCDn_SADDR) or destination address (TCDn_DADDR) upon minor loop completion. Minor loop completion occurs when the channel has finished the service request and has transferred NBYTES. Minor loop offsets are enabled by setting either the source enable bit (SMLOE) or the destination enable bit (DMLOE). 

The source enable bit (SMLOE) specifies the minor loop offset value (MLOFF) that is to be applied to the source address (TCDn_SADDR) upon minor loop completion. The destination enable bit (DMLOE) specifies the minor loop offset (MLOFF) that is to be applied to the destination address (TCDn_DADDR) upon minor loop completion. 

If the major loop is complete, the minor loop offsets are ignored and the major loop address offsets (TCDn_SLAST_SDA and TCDn_DLAST_SGA) are used to compute the next TCDn_SADDR and TCDn_DADDR values. 

When you enable the minor loop offset overlay (either SMLOE or DMLOE is 1), eDMA redefines TCDn_NBYTES_MLOFFNO/ TCDn_NBYTES_MLOFFYES. A portion of TCDn_NBYTES_MLOFFNO/TCDn_NBYTES_MLOFFYES specifies the signextended minor loop offset value (MLOFF). The same offset value (MLOFF) applies to both source and destination minor loop offsets. When the minor loop offset is enabled, you must align it to the transfer size of the source or destination it is associated with. When either minor loop offset is enabled (SMLOE set or DMLOE set), the NBYTES field is reduced to 10 bits. If both minor loop offsets are disabled (SMLOE cleared and DMLOE cleared), the NBYTES field is a 30-bit vector. 

One of two register profiles (this register or TCDn_NBYTES_MLOFFNO) defines the number of bytes to transfer per request. Which register to use depends on whether source or destination minor loop mapping is enabled. 

TCDn_NBYTES_MLOFFYES is defined as follows: 

- If either minor loop offset is enabled (SMLOE or DMLOE = 1), then see the TCDn_NBYTES_MLOFFYES register description. 

- If SMLOE and DMLOE are both 0, then see the TCDn_NBYTES_MLOFFNO register description. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

484 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0485-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R SMLO DMLO<br>MLOFF<br>W E  E<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>MLOFF  NBYTES<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Source Minor Loop Offset Enable|
|SMLOE|Selects whether the minor loop offset is applied to the source address upon minor loop completion.<br>0b - Minor loop offset not applied to SADDR<br>1b - Minor loop offset applied to SADDR|
|30<br>DMLOE|Destination Minor Loop Offset Enable<br>Selects whether the minor loop offset is applied to the destination address upon minor loop completion.<br>0b - Minor loop offset not applied to DADDR<br>1b - Minor loop offset applied to DADDR|
|29-10|Minor Loop Offset|
|MLOFF|If SMLOE or DMLOE is 1, this field represents a sign-extended offset applied to the source or destination<br>address to form the next-state value after the minor loop completes.|
|9-0|Number of Bytes To Transfer Per Service Request|
|NBYTES|The number of bytes to be transferred in each service request of the channel.<br>As a channel activates, the module loads the appropriate TCD contents into the eDMA engine and performs<br>the appropriate reads and writes until the minor byte transfer count has been reached. This is an indivisible<br>operation and cannot be halted. It can, however, be stalled by using the bandwidth control field, or<br>via preemption.<br>After the minor count is exhausted, the SADDR and DADDR values are written back into the TCD memory,<br>and the major iteration count is decremented and restored to the TCD memory. If the major iteration count<br>is complete, additional processing is performed.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

485 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

- 14.5.2.12 TCD Last Source Address Adjustment / Store DADDR Address (TCD0_SLAST_SDA - TCD31_SLAST_SDA) 

##### Offset 

|Register|Offset|
|---|---|
|TCD0_SLAST_SDA|2Ch|
|TCD1_SLAST_SDA|402Ch|
|TCD2_SLAST_SDA|802Ch|
|TCD3_SLAST_SDA|C02Ch|
|TCD4_SLAST_SDA|1_002Ch|
|TCD5_SLAST_SDA|1_402Ch|
|TCD6_SLAST_SDA|1_802Ch|
|TCD7_SLAST_SDA|1_C02Ch|
|TCD8_SLAST_SDA|2_002Ch|
|TCD9_SLAST_SDA|2_402Ch|
|TCD10_SLAST_SDA|2_802Ch|
|TCD11_SLAST_SDA|2_C02Ch|
|TCD12_SLAST_SDA|20_002Ch|
|TCD13_SLAST_SDA|20_402Ch|
|TCD14_SLAST_SDA|20_802Ch|
|TCD15_SLAST_SDA|20_C02Ch|
|TCD16_SLAST_SDA|21_002Ch|
|TCD17_SLAST_SDA|21_402Ch|
|TCD18_SLAST_SDA|21_802Ch|
|TCD19_SLAST_SDA|21_C02Ch|
|TCD20_SLAST_SDA|22_002Ch|
|TCD21_SLAST_SDA|22_402Ch|
|TCD22_SLAST_SDA|22_802Ch|
|TCD23_SLAST_SDA|22_C02Ch|
|TCD24_SLAST_SDA|23_002Ch|
|TCD25_SLAST_SDA|23_402Ch|
|TCD26_SLAST_SDA|23_802Ch|
|TCD27_SLAST_SDA|23_C02Ch|
|TCD28_SLAST_SDA|24_002Ch|
|TCD29_SLAST_SDA|24_402Ch|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

486 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Register|Offset|
|---|---|
|TCD30_SLAST_SDA|24_802Ch|
|TCD31_SLAST_SDA|24_C02Ch|



##### Function 

This register contains the value added to the source address when the major loop is complete. When the store destination address option is enabled, this field provides a pointer to memory for storing the final destination address. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0487-07.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>SLAST_SDA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>SLAST_SDA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Last Source Address Adjustment / Store DADDR Address|
|SLAST_SDA|Source last address adjustment or the system memory address for destination address (DADDR) storage.<br>If (TCDn_CSR[ESDA] = 0), then:<br>• Adjustment value is added to the source address at the completion of the major iteration count.<br>This value can be used to restore the source address to the initial value or adjust the address to<br>reference the next data structure.<br>• This field uses two's complement notation for the final source address adjustment.<br>Otherwise:<br>• This address points to the 32-bit-aligned memory location where the destination address (DADDR)<br>is to be stored in system memory. By saving the final destination address in system memory via<br>the ESDA feature, you are able to compute the size of a variable destination data buffer by simply<br>subtracting the beginning DADDR from the final, saved DADDR. This feature is used together with<br>the scatter/gather operation to prevent the loss of the final DADDR, which is overwritten during the<br>scatter/gather operation.|
||The "Store Destination Address" (SDA) value must be a 32-bit-aligned location because the eDMA<br>forces the lower two address bits of the SLAST_SDA field to zero when ESDA is enabled. The module<br>performs this write operation when the major loop is done; that is, when the major iteration count<br>(CITER) decrements to zero.|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

487 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

#### 14.5.2.13 TCD Destination Address (TCD0_DADDR - TCD31_DADDR) 

##### Offset 

|Register|Offset|
|---|---|
|TCD0_DADDR|30h|
|TCD1_DADDR|4030h|
|TCD2_DADDR|8030h|
|TCD3_DADDR|C030h|
|TCD4_DADDR|1_0030h|
|TCD5_DADDR|1_4030h|
|TCD6_DADDR|1_8030h|
|TCD7_DADDR|1_C030h|
|TCD8_DADDR|2_0030h|
|TCD9_DADDR|2_4030h|
|TCD10_DADDR|2_8030h|
|TCD11_DADDR|2_C030h|
|TCD12_DADDR|20_0030h|
|TCD13_DADDR|20_4030h|
|TCD14_DADDR|20_8030h|
|TCD15_DADDR|20_C030h|
|TCD16_DADDR|21_0030h|
|TCD17_DADDR|21_4030h|
|TCD18_DADDR|21_8030h|
|TCD19_DADDR|21_C030h|
|TCD20_DADDR|22_0030h|
|TCD21_DADDR|22_4030h|
|TCD22_DADDR|22_8030h|
|TCD23_DADDR|22_C030h|
|TCD24_DADDR|23_0030h|
|TCD25_DADDR|23_4030h|
|TCD26_DADDR|23_8030h|
|TCD27_DADDR|23_C030h|
|TCD28_DADDR|24_0030h|
|TCD29_DADDR|24_4030h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

488 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Register|Offset|
|---|---|
|TCD30_DADDR|24_8030h|
|TCD31_DADDR|24_C030h|



##### Function 

This register contains the address for the write transactions. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0489-07.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>DADDR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>DADDR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-0|Destination Address|
|DADDR|Memory address pointing to the destination data.|



#### 14.5.2.14 TCD Signed Destination Address Offset (TCD0_DOFF - TCD31_DOFF) 

##### Offset 

|Register|Offset|
|---|---|
|TCD0_DOFF|34h|
|TCD1_DOFF|4034h|
|TCD2_DOFF|8034h|
|TCD3_DOFF|C034h|
|TCD4_DOFF|1_0034h|
|TCD5_DOFF|1_4034h|
|TCD6_DOFF|1_8034h|
|TCD7_DOFF|1_C034h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

489 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Register|Offset|
|---|---|
|TCD8_DOFF|2_0034h|
|TCD9_DOFF|2_4034h|
|TCD10_DOFF|2_8034h|
|TCD11_DOFF|2_C034h|
|TCD12_DOFF|20_0034h|
|TCD13_DOFF|20_4034h|
|TCD14_DOFF|20_8034h|
|TCD15_DOFF|20_C034h|
|TCD16_DOFF|21_0034h|
|TCD17_DOFF|21_4034h|
|TCD18_DOFF|21_8034h|
|TCD19_DOFF|21_C034h|
|TCD20_DOFF|22_0034h|
|TCD21_DOFF|22_4034h|
|TCD22_DOFF|22_8034h|
|TCD23_DOFF|22_C034h|
|TCD24_DOFF|23_0034h|
|TCD25_DOFF|23_4034h|
|TCD26_DOFF|23_8034h|
|TCD27_DOFF|23_C034h|
|TCD28_DOFF|24_0034h|
|TCD29_DOFF|24_4034h|
|TCD30_DOFF|24_8034h|
|TCD31_DOFF|24_C034h|



##### Function 

This register contains the sign-extended value added to Destination Address register after each write transaction. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

490 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0491-03.png)


<!-- Start of picture text -->
Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>DOFF<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|15-0|Destination Address Signed Offset|
|DOFF|Sign-extended offset that is applied to the current destination address to form the next-state value as<br>each destination write is completed.|



14.5.2.15 TCD Current Major Loop Count (Minor Loop Channel Linking Disabled) (TCD0_CITER_ELINKNO - TCD31_CITER_ELINKNO) 

##### Offset 

|Register|Offset|
|---|---|
|TCD0_CITER_ELINKNO|36h|
|TCD1_CITER_ELINKNO|4036h|
|TCD2_CITER_ELINKNO|8036h|
|TCD3_CITER_ELINKNO|C036h|
|TCD4_CITER_ELINKNO|1_0036h|
|TCD5_CITER_ELINKNO|1_4036h|
|TCD6_CITER_ELINKNO|1_8036h|
|TCD7_CITER_ELINKNO|1_C036h|
|TCD8_CITER_ELINKNO|2_0036h|
|TCD9_CITER_ELINKNO|2_4036h|
|TCD10_CITER_ELINKN<br>O|2_8036h|
|TCD11_CITER_ELINKN<br>O|2_C036h|
|TCD12_CITER_ELINKN<br>O|20_0036h|
|TCD13_CITER_ELINKN<br>O|20_4036h|
|TCD14_CITER_ELINKN<br>O|20_8036h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

491 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

Table continued from the previous page... 

|Registe|r|Off|set|
|---|---|---|---|
|TCD15_<br>O|CITER_ELINKN|20_|C036h|
|TCD16_|CITER_ELINKN|21_|0036h|
|O||||
|TCD17_|CITER_ELINKN|21_|4036h|
|O||||
|TCD18_<br>O|CITER_ELINKN|21_|8036h|
|TCD19_<br>O|CITER_ELINKN|21_|C036h|
|TCD20_<br>O|CITER_ELINKN|22_|0036h|
|TCD21_<br>O|CITER_ELINKN|22_|4036h|
|TCD22_<br>O|CITER_ELINKN|22_|8036h|
|TCD23_<br>O|CITER_ELINKN|22_|C036h|
|TCD24_<br>O|CITER_ELINKN|23_|0036h|
|TCD25_<br>O|CITER_ELINKN|23_|4036h|
|TCD26_<br>O|CITER_ELINKN|23_|8036h|
|TCD27_<br>O|CITER_ELINKN|23_|C036h|
|TCD28_<br>O|CITER_ELINKN|24_|0036h|
|TCD29_<br>O|CITER_ELINKN|24_|4036h|
|TCD30_<br>O|CITER_ELINKN|24_|8036h|
|TCD31_<br>O|CITER_ELINKN|24_|C036h|



##### Function 

If TCDn_CITER[ELINK] is 0, the TCDn_CITER register is defined as follows. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

492 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0493-03.png)


<!-- Start of picture text -->
Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>ELINK  CITER<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|15|Enable Link|
|ELINK|As the channel completes the minor loop, this flag enables linking to another channel as defined by the<br>relevant LINKCH field. The link target channel initiates a channel service request via an internal mechanism<br>that sets the TCDn_CSR[START] bit of the specified channel to 1.<br>If channel linking is disabled, the CITER value is extended to 15 bits in place of a link channel number. If the<br>major loop is exhausted, this link mechanism is suppressed in favor of MAJORELINK channel linking.<br>This field must be equal to the BITER[ELINK] field; otherwise, a configuration error<br>is reported.<br>~~NOTE~~|
||0b - Channel-to-channel linking disabled<br>1b - Channel-to-channel linking enabled|
|14-0<br>CITER|Current Major Iteration Count<br>This 9-bit (ELINK = 1) or 15-bit (ELINK = 0) count represents the current major loop count for the channel.<br>It is decremented each time the channel finishes a service request and is written back to TCD memory.<br>After the major iteration count is exhausted, the channel performs a number of operations — for example,<br>final source and destination address calculations — and optionally generates an interrupt to signal channel<br>completion before reloading the CITER field from the Beginning Iteration Count (BITER) field.<br>When the CITER field is initially loaded by software, it must be set to the same value as that<br>contained in the BITER field.<br>~~NOTE~~|
||If the channel is configured to execute a single service request, the initial values of BITER<br>and CITER should be 0x0001.<br>~~NOTE~~|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

493 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

#### 14.5.2.16 TCD Current Major Loop Count (Minor Loop Channel Linking Enabled) (TCD0_CITER_ELINKYES - TCD31_CITER_ELINKYES) 

##### Offset 

|Register|Offset|
|---|---|
|TCD0_CITER_ELINKYE<br>S|36h|
|TCD1_CITER_ELINKYE<br>S|4036h|
|TCD2_CITER_ELINKYE<br>S|8036h|
|TCD3_CITER_ELINKYE<br>S|C036h|
|TCD4_CITER_ELINKYE<br>S|1_0036h|
|TCD5_CITER_ELINKYE<br>S|1_4036h|
|TCD6_CITER_ELINKYE<br>S|1_8036h|
|TCD7_CITER_ELINKYE<br>S|1_C036h|
|TCD8_CITER_ELINKYE<br>S|2_0036h|
|TCD9_CITER_ELINKYE<br>S|2_4036h|
|TCD10_CITER_ELINKY<br>ES|2_8036h|
|TCD11_CITER_ELINKY<br>ES|2_C036h|
|TCD12_CITER_ELINKY<br>ES|20_0036h|
|TCD13_CITER_ELINKY<br>ES|20_4036h|
|TCD14_CITER_ELINKY<br>ES|20_8036h|
|TCD15_CITER_ELINKY<br>ES|20_C036h|
|TCD16_CITER_ELINKY<br>ES|21_0036h|
|TCD17_CITER_ELINKY<br>ES|21_4036h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

494 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

Table continued from the previous page... 

|Register|Offset|
|---|---|
|TCD18_CITER_ELINKY<br>ES|21_8036h|
|TCD19_CITER_ELINKY<br>ES|21_C036h|
|TCD20_CITER_ELINKY<br>ES|22_0036h|
|TCD21_CITER_ELINKY<br>ES|22_4036h|
|TCD22_CITER_ELINKY<br>ES|22_8036h|
|TCD23_CITER_ELINKY<br>ES|22_C036h|
|TCD24_CITER_ELINKY<br>ES|23_0036h|
|TCD25_CITER_ELINKY<br>ES|23_4036h|
|TCD26_CITER_ELINKY<br>ES|23_8036h|
|TCD27_CITER_ELINKY<br>ES|23_C036h|
|TCD28_CITER_ELINKY<br>ES|24_0036h|
|TCD29_CITER_ELINKY<br>ES|24_4036h|
|TCD30_CITER_ELINKY<br>ES|24_8036h|
|TCD31_CITER_ELINKY<br>ES|24_C036h|



##### Function 

If TCDn_CITER[ELINK] is 1, the TCDn_CITER register is defined as follows. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

495 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0496-02.png)


<!-- Start of picture text -->
Diagram<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv<br>R<br>ELINK  ed  LINKCH  CITER<br>W 0<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|15|Enable Link|
|ELINK|As the channel completes the minor loop, this flag enables linking to another channel as defined by the<br>relevant LINKCH field. When enabled, an internal mechanism sets the TCDn_CSR[START] field of the<br>specified channel (LINKCH) upon minor loop completion.<br>If channel linking is disabled, the CITER value is extended to 15 bits in place of a link channel number. If the<br>major loop is exhausted, this link mechanism is suppressed in favor of MAJORELINK channel linking.<br>This field must be equal to the BITER[ELINK] field; otherwise, a configuration error<br>is reported.<br>~~NOTE~~|
||0b - Channel-to-channel linking disabled<br>1b - Channel-to-channel linking enabled|
|14|Reserved|
|—<br>13-9|Minor Loop Link Channel Number|
|LINKCH|If channel-to-channel linking is enabled (ELINK = 1), then after the minor loop is exhausted the eDMA<br>engine initiates a channel service request to the channel defined by this field by writing that channel’s<br>TCDn_CSR[START] field to 1.|
|8-0<br>CITER|Current Major Iteration Count<br>This 9-bit (ELINK = 1) or 15-bit (ELINK = 0) count represents the current major loop count for the channel.<br>It is decremented each time the channel finishes a service request and is written back to the TCD memory.<br>After the major iteration count is exhausted, the channel performs a number of operations — for example,<br>final source and destination address calculations — and optionally generates an interrupt to signal channel<br>completion before reloading the CITER field from the Beginning Iteration Count (BITER) field.<br>When the CITER field is initially loaded by software, it must be set to the same value as that<br>contained in the BITER field.<br>~~NOTE~~<br>If the channel is configured to execute a single service request, the initial values of BITER<br>and CITER should be 0x0001.<br>~~NOTE~~|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

496 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

#### 14.5.2.17 TCD Last Destination Address Adjustment / Scatter Gather Address (TCD0_DLAST_SGA - TCD31_DLAST_SGA) 

##### Offset 

|Register|Offset|
|---|---|
|TCD0_DLAST_SGA|38h|
|TCD1_DLAST_SGA|4038h|
|TCD2_DLAST_SGA|8038h|
|TCD3_DLAST_SGA|C038h|
|TCD4_DLAST_SGA|1_0038h|
|TCD5_DLAST_SGA|1_4038h|
|TCD6_DLAST_SGA|1_8038h|
|TCD7_DLAST_SGA|1_C038h|
|TCD8_DLAST_SGA|2_0038h|
|TCD9_DLAST_SGA|2_4038h|
|TCD10_DLAST_SGA|2_8038h|
|TCD11_DLAST_SGA|2_C038h|
|TCD12_DLAST_SGA|20_0038h|
|TCD13_DLAST_SGA|20_4038h|
|TCD14_DLAST_SGA|20_8038h|
|TCD15_DLAST_SGA|20_C038h|
|TCD16_DLAST_SGA|21_0038h|
|TCD17_DLAST_SGA|21_4038h|
|TCD18_DLAST_SGA|21_8038h|
|TCD19_DLAST_SGA|21_C038h|
|TCD20_DLAST_SGA|22_0038h|
|TCD21_DLAST_SGA|22_4038h|
|TCD22_DLAST_SGA|22_8038h|
|TCD23_DLAST_SGA|22_C038h|
|TCD24_DLAST_SGA|23_0038h|
|TCD25_DLAST_SGA|23_4038h|
|TCD26_DLAST_SGA|23_8038h|
|TCD27_DLAST_SGA|23_C038h|
|TCD28_DLAST_SGA|24_0038h|
|TCD29_DLAST_SGA|24_4038h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

497 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

Table continued from the previous page... 

|Register|Offset|
|---|---|
|TCD30_DLAST_SGA|24_8038h|
|TCD31_DLAST_SGA|24_C038h|



##### Function 

This register contains the value added to the destination address when the major loop is complete. When the Scatter/Gather option is enabled, this field provides a pointer to memory for fetching a transfer control descriptor to reprogram the channel. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0498-07.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>DLAST_SGA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>DLAST_SGA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Last Destination Address Adjustment / Scatter Gather Address|
|DLAST_SGA|Adjustment of the last destination address or the memory address for the next transfer control descriptor to<br>be loaded into this channel (scatter/gather).<br>If (TCDn_CSR[ESG] = 0) then:<br>• Adjustment value is added to the destination address at the completion of the major iteration count.<br>This value can apply to restore the destination address to the initial value or adjust the address to<br>reference the next data structure.<br>• This field uses two's complement notation for the final destination address adjustment.<br>Otherwise:<br>• This address points to the beginning of a 0-modulo 32-byte region containing the next transfer<br>control descriptor to be loaded into this channel. This channel reload is performed as the major<br>iteration count completes. The scatter/gather address must be 0-modulo 32-byte, or else a<br>configuration error is reported.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

498 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

#### 14.5.2.18 TCD Control and Status (TCD0_CSR - TCD31_CSR) 

##### Offset 

|Register|Offset|
|---|---|
|TCD0_CSR|3Ch|
|TCD1_CSR|403Ch|
|TCD2_CSR|803Ch|
|TCD3_CSR|C03Ch|
|TCD4_CSR|1_003Ch|
|TCD5_CSR|1_403Ch|
|TCD6_CSR|1_803Ch|
|TCD7_CSR|1_C03Ch|
|TCD8_CSR|2_003Ch|
|TCD9_CSR|2_403Ch|
|TCD10_CSR|2_803Ch|
|TCD11_CSR|2_C03Ch|
|TCD12_CSR|20_003Ch|
|TCD13_CSR|20_403Ch|
|TCD14_CSR|20_803Ch|
|TCD15_CSR|20_C03Ch|
|TCD16_CSR|21_003Ch|
|TCD17_CSR|21_403Ch|
|TCD18_CSR|21_803Ch|
|TCD19_CSR|21_C03Ch|
|TCD20_CSR|22_003Ch|
|TCD21_CSR|22_403Ch|
|TCD22_CSR|22_803Ch|
|TCD23_CSR|22_C03Ch|
|TCD24_CSR|23_003Ch|
|TCD25_CSR|23_403Ch|
|TCD26_CSR|23_803Ch|
|TCD27_CSR|23_C03Ch|
|TCD28_CSR|24_003Ch|
|TCD29_CSR|24_403Ch|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

499 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Register|Offset|
|---|---|
|TCD30_CSR|24_803Ch|
|TCD31_CSR|24_C03Ch|



##### Function 

This register is used to enable optional features. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0500-07.png)


<!-- Start of picture text -->
Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>Reserv MAJO INTHA INTMA STAR<br>BWC  MAJORLINKCH  ESDA  ESG  DREQ<br>W 0 ed  REL... LF  JOR  T<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|15-14|Bandwidth Control|
|BWC|Throttles the amount of bus bandwidth consumed by the eDMA. Generally, as the eDMA processes the<br>minor loop, it continuously generates read/write sequences until the minor count is exhausted. This field<br>forces eDMA to stall after the completion of each read/write access, to control the bus request bandwidth<br>seen by the system bus interconnect.|
||If the source and destination sizes are equal, this field is ignored between the first and<br>second transfers and after the last write of each minor loop. This behavior is a side effect of<br>reducing start-up latency.<br>~~NOTE~~|
||00b - No eDMA engine stalls|
||01b - Enable eDMA master high-priority elevation (HPE) mode. No eDMA engine stalls.<br>10b - eDMA engine stalls for 4 cycles after each R/W|
||11b - eDMA engine stalls for 8 cycles after each R/W|
|13|Reserved|
|—||
|12-8|Major Loop Link Channel Number|
|MAJORLINKCH|If (MAJORELINK = 0) then:<br>• No channel-to-channel linking, or chaining, is performed after the major loop counter is exhausted.<br>Otherwise:<br>• After the major loop counter is exhausted, the eDMA engine initiates a channel service request at<br>the channel defined by this field by setting that channel’s TCDn_CSR[START] field to 1.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

500 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|7|Enable Store Destination Address|
|ESDA|As the channel completes the major loop by either the current iteration counter (CITER) decrementing to 0,<br>this field enables writing the destination address (DADDR) to the address stored in the SLAST_SDA field.<br>The value written to system memory is the last DADDR value prior to the DLAST_SGA offset being applied,<br>or overwritten by an enabled scatter/gather operation. When the SDA bit is 1, SLAST_SDA contains the<br>write pointer instead of the final source address offset. Because this is a pointer and not a final offset, a last<br>source address offset of zero is applied to SADDR instead of the SLAST_SGA value.<br>0b - Ability to store destination address to system memory disabled<br>1b - Ability to store destination address to system memory enabled|
|6<br>—|Reserved|
|5|Enable Link When Major Loop Complete|
|MAJORELINK|As the channel completes the major loop, this flag enables linking to another channel defined by<br>MAJORLINKCH. The link target channel initiates a channel service request via an internal mechanism that<br>sets the TCDn_CSR[START] field of the specified channel.<br>To support the dynamic linking coherency model, this field is forced to 0 if written when<br>TCDn_CSR[DONE] is 1.<br>~~NOTE~~|
||0b - Channel-to-channel linking disabled<br>1b - Channel-to-channel linking enabled|
|4<br>ESG|Enable Scatter/Gather Processing<br>As the channel completes the major loop, this flag enables scatter/gather processing in the current channel.<br>If enabled, the eDMA engine usesTCDn_DLAST_SGAas a memory pointer to a 0-modulo 32-bit address<br>containing a 32-byte data structure, which is loaded as the transfer control descriptor into local memory.<br>To support the dynamic scatter/gather coherency model, this field is forced to 0 if written<br>when TCDn_CSR[DONE] is 1.<br>~~NOTE~~|
||0b - Current channel’s TCD is normal format<br>1b - Current channel’s TCD specifies scatter/gather format.|
|3<br>DREQ|Disable Request<br>If this flag is 1, the eDMA hardware automatically clears the corresponding ERQ bit when the current<br>major iteration count reaches 0.<br>0b - No operation. Channel’s ERQ field not affected<br>1b - Clear the ERQ field to 0 upon major loop completion, thus disabling hardware service<br>requests. Channel’s ERQ field cleared to 0 when major loop complete|
|2|Enable Interrupt If Major Counter Half-complete<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

501 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|INTHALF|If this flag is 1, the channel generates an interrupt request by setting the appropriate field in the INT<br>register to 1 when the current major iteration count reaches the halfway point. Specifically, the comparison<br>performed by the eDMA engine is (CITER = (BITER/2)). This halfway point interrupt request is provided to<br>support double-buffered, also known as ping-pong, schemes, or other types of data movement where the<br>processor needs an early indication of the transfer’s progress.<br>If BITER = 1, do not use INTHALF; use INTMAJOR instead.<br>~~NOTE~~<br>0b - Halfway point interrupt disabled<br>1b - Halfway point interrupt enabled|
|1<br>INTMAJOR|Enable Interrupt If Major count complete<br>If this flag is 1, the channel generates an interrupt request by setting the appropriate field in the INT<br>register to 1 when the current major iteration count (CITER) reaches 0.<br>0b - End-of-major loop interrupt disabled<br>1b - End-of-major loop interrupt enabled|
|0<br>START|Channel Start<br>If this flag is 1, the channel is requesting service. The eDMA hardware automatically clears this flag to 0<br>after the channel begins execution.<br>0b - Channel not explicitly started<br>1b - Channel explicitly started via a software-initiated service request|



14.5.2.19 TCD Beginning Major Loop Count (Minor Loop Channel Linking Disabled) (TCD0_BITER_ELINKNO - TCD31_BITER_ELINKNO) 

##### Offset 

|Register|Offset|
|---|---|
|TCD0_BITER_ELINKNO|3Eh|
|TCD1_BITER_ELINKNO|403Eh|
|TCD2_BITER_ELINKNO|803Eh|
|TCD3_BITER_ELINKNO|C03Eh|
|TCD4_BITER_ELINKNO|1_003Eh|
|TCD5_BITER_ELINKNO|1_403Eh|
|TCD6_BITER_ELINKNO|1_803Eh|
|TCD7_BITER_ELINKNO|1_C03Eh|
|TCD8_BITER_ELINKNO|2_003Eh|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

502 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

Table continued from the previous page... 

|Registe|r|Offset|
|---|---|---|
|TCD9_B|ITER_ELINKNO|2_403Eh|
|TCD10_<br>O|BITER_ELINKN|2_803Eh|
|TCD11_<br>O|BITER_ELINKN|2_C03Eh|
|TCD12_<br>O|BITER_ELINKN|20_003Eh|
|TCD13_<br>O|BITER_ELINKN|20_403Eh|
|TCD14_<br>O|BITER_ELINKN|20_803Eh|
|TCD15_<br>O|BITER_ELINKN|20_C03Eh|
|TCD16_<br>O|BITER_ELINKN|21_003Eh|
|TCD17_<br>O|BITER_ELINKN|21_403Eh|
|TCD18_<br>O|BITER_ELINKN|21_803Eh|
|TCD19_<br>O|BITER_ELINKN|21_C03Eh|
|TCD20_<br>O|BITER_ELINKN|22_003Eh|
|TCD21_<br>O|BITER_ELINKN|22_403Eh|
|TCD22_<br>O|BITER_ELINKN|22_803Eh|
|TCD23_<br>O|BITER_ELINKN|22_C03Eh|
|TCD24_<br>O|BITER_ELINKN|23_003Eh|
|TCD25_<br>O|BITER_ELINKN|23_403Eh|
|TCD26_<br>O|BITER_ELINKN|23_803Eh|
|TCD27_<br>O|BITER_ELINKN|23_C03Eh|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

503 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Table continued from the previous page... 

|Register|Offset|
|---|---|
|TCD28_BITER_ELINKN<br>O|24_003Eh|
|TCD29_BITER_ELINKN<br>O|24_403Eh|
|TCD30_BITER_ELINKN<br>O|24_803Eh|
|TCD31_BITER_ELINKN<br>O|24_C03Eh|



##### Function 

If the TCDn_BITER[ELINK] field is 0, the TCDn_BITER register is defined as follows. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0504-07.png)


<!-- Start of picture text -->
Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>ELINK  BITER<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|15|Enables Link|
|ELINK|As the channel completes the minor loop, this flag enables linking to another channel as defined by<br>BITER[LINKCH]. The link target channel initiates a channel service request via an internal mechanism that<br>sets the TCDn_CSR[START] field of the specified channel. If channel linking is disabled, the BITER value<br>extends to 15 bits in place of a link channel number. If the major loop is exhausted, this link mechanism is<br>suppressed in favor of the MAJORELINK channel linking.<br>When the software loads the TCD, this field must be set equal to the corresponding CITER<br>field; otherwise, a configuration error is reported. As the major iteration count is exhausted,<br>eDMA reloads the contents of this field into the CITER field.<br>~~NOTE~~|
||0b - Channel-to-channel linking disabled<br>1b - Channel-to-channel linking enabled|
|14-0|Starting Major Iteration Count|
|BITER|As the transfer control descriptor is first loaded by software, this 9-bit (ELINK = 1) or 15-bit (ELINK = 0) field<br>must be set equal to the value in the CITER field. As the major iteration count is exhausted, eDMA reloads<br>the contents of this field into the CITER field. If the channel is configured to execute a single service request,<br>the initial values of BITER and CITER must be 0x0001.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

504 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

#### 14.5.2.20 TCD Beginning Major Loop Count (Minor Loop Channel Linking Enabled) (TCD0_BITER_ELINKYES - TCD31_BITER_ELINKYES) 

##### Offset 

|Register|Offset|
|---|---|
|TCD0_BITER_ELINKYE<br>S|3Eh|
|TCD1_BITER_ELINKYE<br>S|403Eh|
|TCD2_BITER_ELINKYE<br>S|803Eh|
|TCD3_BITER_ELINKYE<br>S|C03Eh|
|TCD4_BITER_ELINKYE<br>S|1_003Eh|
|TCD5_BITER_ELINKYE<br>S|1_403Eh|
|TCD6_BITER_ELINKYE<br>S|1_803Eh|
|TCD7_BITER_ELINKYE<br>S|1_C03Eh|
|TCD8_BITER_ELINKYE<br>S|2_003Eh|
|TCD9_BITER_ELINKYE<br>S|2_403Eh|
|TCD10_BITER_ELINKY<br>ES|2_803Eh|
|TCD11_BITER_ELINKY<br>ES|2_C03Eh|
|TCD12_BITER_ELINKY<br>ES|20_003Eh|
|TCD13_BITER_ELINKY<br>ES|20_403Eh|
|TCD14_BITER_ELINKY<br>ES|20_803Eh|
|TCD15_BITER_ELINKY<br>ES|20_C03Eh|
|TCD16_BITER_ELINKY<br>ES|21_003Eh|
|TCD17_BITER_ELINKY<br>ES|21_403Eh|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

505 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

Table continued from the previous page... 

|Register|Offset|
|---|---|
|TCD18_BITER_<br>ES|ELINKY<br>21_803Eh|
|TCD19_BITER_<br>ES|ELINKY<br>21_C03Eh|
|TCD20_BITER_<br>ES|ELINKY<br>22_003Eh|
|TCD21_BITER_<br>ES|ELINKY<br>22_403Eh|
|TCD22_BITER_<br>ES|ELINKY<br>22_803Eh|
|TCD23_BITER_<br>ES|ELINKY<br>22_C03Eh|
|TCD24_BITER_<br>ES|ELINKY<br>23_003Eh|
|TCD25_BITER_<br>ES|ELINKY<br>23_403Eh|
|TCD26_BITER_<br>ES|ELINKY<br>23_803Eh|
|TCD27_BITER_<br>ES|ELINKY<br>23_C03Eh|
|TCD28_BITER_<br>ES|ELINKY<br>24_003Eh|
|TCD29_BITER_<br>ES|ELINKY<br>24_403Eh|
|TCD30_BITER_<br>ES|ELINKY<br>24_803Eh|
|TCD31_BITER_<br>ES|ELINKY<br>24_C03Eh|



Function 

If the TCDn_BITER[ELINK] field is set, the TCDn_BITER register is defined as follows. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

506 / 4640 

NXP Semiconductors 

Enhanced Direct Memory Access (eDMA) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/014_Enhanced_Direct_Memory_Access_-eDMA-/S32K3XXRM_数据表.pdf-0507-03.png)


<!-- Start of picture text -->
Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv<br>R<br>ELINK  ed  LINKCH  BITER<br>W 0<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|15|Enable Link|
|ELINK|As the channel completes the minor loop, this flag enables linking to another channel as defined by<br>BITER[LINKCH]. The link target channel initiates a channel service request via an internal mechanism that<br>sets the TCDn_CSR[START] field of the specified channel. If channel linking disables, the BITER value<br>extends to 15 bits in place of a link channel number. If the major loop is exhausted, this link mechanism is<br>suppressed in favor of the MAJORELINK channel linking.<br>When the software loads the TCD, this field must be set equal to the corresponding CITER<br>field; otherwise, a configuration error is reported. As the major iteration count is exhausted,<br>eDMA reloads the contents of this field into the CITER field.<br>~~NOTE~~|
||0b - Channel-to-channel linking disabled<br>1b - Channel-to-channel linking enabled|
|14<br>—<br>13-9|Reserved<br>Link Channel Number|
|LINKCH|If channel-to-channel linking is enabled (ELINK = 1), then after the minor loop is exhausted, the eDMA<br>engine initiates a channel service request at the channel defined by this field by setting that channel’s<br>TCDn_CSR[START] field.<br>When the software loads the TCD, this field must be set equal to the corresponding CITER<br>field; otherwise, a configuration error is reported. As the major iteration count is exhausted,<br>eDMA reloads the contents of this field into the CITER field.<br>~~NOTE~~|
|8-0|Starting Major Iteration Count|
|BITER|As the transfer control descriptor is first loaded by software, this 9-bit (ELINK = 1) or 15-bit (ELINK = 0) field<br>must be set equal to the value in the CITER field. As the major iteration count is exhausted, eDMA reloads<br>the contents of this field into the CITER field. If the channel is configured to execute a single service request,<br>the initial values of BITER and CITER must be 0x0001.|



## 14.6 Glossary 

TCD Transfer control descriptor 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

507 / 4640 

