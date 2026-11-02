NXP Semiconductors 

# Chapter 39 Messaging Unit (MU) 

## 39.1 Chip-specific MU information 

### 39.1.1 MU instances and configuration 

This chip includes MUs for communication across the different cores. Each MU includes two interfaces, MUA and MUB. Two different processors control them for communication. 

Table 205 indicates the MUs and their interfaces present in different parts of the S32K3 chip family. The table also summarizes the implementation of this module in each chip of the S32K3 product series. 

~~<mark>NOTE</mark>~~ 

The HSE_B core controls the MUA interface of MU_0 and MU_1. Therefore, the application core cannot control the interface. 

Table 205. MU instances 

|Instance|S32K344|S32K324|S32K314<br>S32K342|S32K322|S32K312|S32K311|Use case|
|---|---|---|---|---|---|---|---|
|MU_0<br>MU_1|||Yes<br>Yes||||Communication between HSE_B<br>and application cores|
|MU_2|No|Yes|No|Yes|N|o|Communication between<br>application cores|



The base address of MU_1's MUB interface is different across the S32K3xx product series because AIPS_2 is unavailable in S32K312 and S32K311. Table 206 summarizes this difference. 

Table 206. Base-address difference in MU_1's MUB interface across S32K3xx product series 

||S32K358|S32K344|S32K324|S32K314|S32K342|S32K322|S32K312|S32K311|
|---|---|---|---|---|---|---|---|---|
|Base<br>address|||404E_|C000h|||4039_|0000h|



~~<mark>NOTE</mark>~~ For S32K342, reset value of MUA_VER and MUB_VER register is 0309_000Fh. 

## 39.2 Overview 

The Messaging Unit module (MU) enables two processors within the SoC to communicate and coordinate by passing messages (e.g. data, status and control) through the MU interface. The MU also provides the ability for one processor to signal the other processor using interrupts. 

Because the MU manages the messaging between processors potentially using different clocks, the MU must synchronize the accesses from one side to the other. The MU accomplishes synchronization using two sets of matching registers (Processor A-facing, Processor B-facing). 

### 39.2.1 Block Diagram 

The following is the MU Block Diagram: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1243 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1244-02.png)


<!-- Start of picture text -->
Processor A Processor B<br>Messaging Unit (MU)<br>Processor A  side Processor B side<br>TX / RX TX / RX<br>Registers Registers<br>Status and  Status and<br>Processor A Processor B<br>Control Control<br>Peripheral Peripheral<br>Bus Registers Registers Bus<br>Sync and Sync and<br>Control Control<br>Registers Registers<br>Generate Generate<br>Interrupts Interrupts<br>Interrupts to  Interrupts to<br>Processor A  Processor B<br>interrupt  interrupt<br>controller controller<br><!-- End of picture text -->

Figure 146. MU Block Diagram 

### 39.2.2 Features 

The MU includes the following features: 

- Memory-Mapped Registers 

   - The MU is connected as a peripheral under the Peripheral bus on Processor A-side and Processor B-side. 

- Synchronized Message Transfers between Cores 

   - For sending data or messages from one MU-side to the other MU-side, the MUA provides 4 transmit registers and 4 receive registers, the MUB provides 4 transmit registers and 4 receive registers. 

   - The transfer of data messages between cores uses transmit empty and receive full flags provided on both sides of the MU. 

   - The update of these transmit and receive flags is accomplished using a synchronization mechanism. There is inherent latency between updating the flag on one side and reflecting its status on other side. 

   - The MU has a 3 bit Flag Data Register, which can be used to send flag data between two MU sides. 

- Interprocessor Interrupts 

   - The MU has 9 interrupt sources on each side (Processor A-side, Processor B-side) that are used for signaling the other processor. The interrupts can be used for notification of RX/TX events and general-purpose signaling between the processors. There are 1 general-purpose interrupt requests available and 8 RX/TX interrupt sources. 

- MU Reset 

   - Each Processor can issue a reset to the entire MU, using a control bit (MUR) in each Processor's Control Register (CR). 

   - The MUR bit is a self-clearing bit. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1244 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

## 39.3 Functional Description 

The Messaging Unit (MU) enables two cores (Processor A or Processor B) to communicate with each other, by passing message/data information to each other, and by enabling one core to wake up the other core using interrupts. 

The messaging, control, and status registers of the Processor A and Processor B-side for the MU are mapped to the Processor A and Processor B memory as a regular peripheral. The Peripheral data bus is 32 bits wide inside the MU module. 

The messaging logic is used in conjunction with external memory. There are various messaging methods that can be used to implement a messaging protocol. Some of these messages could mean “A message of N words has been written starting at offset X in the memory,” or "The previous data block that was sent has been read." Having the messaging logic independent from the memory array is not restricted to a predefined hardware protocol. On the other hand, the software needed to manage the messaging is short and straightforward. 

Most of the messaging mechanisms are symmetric. They are duplicated and are available on both the Processor A-side and the Processor B-side. The messaging mechanisms are: 

- 4 32-bit transmit registers, which are each reflected in 4 read-only receive registers in the other processor’s side. You can use these registers to transfer 32-bit word messages or frame information of messages written to the shared memory (number of words, initial address, and message type code). 

- A write to a transmit register on the transmitter side clears a “transmitter empty” bit in the Status Register on the transmitter side, and sets a “receiver full” bit in the Status Register on the receiver side. The setting of the bit at the receiver side can optionally trigger an interrupt at the receiver side (maskable receive interrupt). 

- A read of one of the receive registers at the receiver side clears the “receiver full” bit in the Status Register at the receiver side, and sets the “transmitter empty” bit in the Status Register on the transmitter side. The setting of the “transmitter empty” bit can optionally trigger an interrupt at the transmitter side (maskable transmit interrupt). 

- 1 general purpose interrupt request flags are reflected in the General Status Register(GSR) on the receiver side. 

- 3-bit flag data is transmitted from FCR register to xFSR register with the SR[FUP] indicator bit. 

A write to a transmit register signals the receiver side that data is ready for retrieval. 

- Writing to the transmit register again without verifying that the data was retrieved is prohibited, because the transmitter side has no way of knowing the exact time that the receiver attempts to retrieve the data. 

- Before attempting to write the transmit register again, the transmitter side should wait for a “Transmitter Empty” interrupt, or should poll the “Transmitter Empty” bit in the Transmit Status Register. 

A read of a receive register signals the transmitter side that data can be written to that register. In the same way, the receiver processor should not read a receive register before receiving a “Receiver Full” interrupt or polling the “Receiver Full” bit in the Receive Status Register. 

- Reading the receive register again without verifying that the data was written is prohibited, because the receiver side has no way of knowing the exact time that the transmitter attempts to write the data. 

- Before attempting to read the receive register again, the receiver side should wait for a “Receiver Full” interrupt, or should poll the “Receiver Full” bit in the Receive Status Register. 

### 39.3.1 Event Update Timing 

Each processor’s MU messaging side (Processor A or Processor B) has a hardware mechanism to send “event update requests” to the other processor’s side. An “event” is considered when any information change should be reflected at the Status Register of the receiving processor. The event update latency is the delay between the event being ready at one processor and the resulting update at the Status Register of the other processor. 

- The minimum event latency is “1 clock of the sending side” + “2 1/2 clocks of the receiving side”. The minimum case is if there is no event pending when the new event occurs. 

- The maximum event latency is “6 clocks of the sending side” + “6 1/2 clocks of the receiving side.” The maximum case is if the event occurred just after a previous event was sent to the other side. The event update latency varies between the above-mentioned minimum and maximum latencies, depending on the time at which the subsequent event is triggered. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1245 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

### 39.3.2 Interrupts 

The MU controls one processor interrupt requests to the other processor. This section describes all the interrupts that the module generates. 

Below interrupt sources can be generated individually from the MU to the Processors. 

- 4 receive interrupts (asserted when the Processors receive full bits are set and enabled in the xRCR register) for each of the receive registers 

- 4 transmit interrupts (asserted when the Processor transmit empty bits are set and enabled in the xTCR register) for each of the transmit registers 

- 1 general purpose interrupts (asserted when the GIP bits are set and enabled in the xGIER register) 

- Core Reset Assertion interrupts(asserted when Processor goes into of Reset state and enabled in RAIE register bit) 

- MU Software/Hardware Reset assertion(asserted when MUR and HR bit are written and enabled in MURIE and HRIE register bit) 

All the interrupts are maskable in the Processor Control Register (xTCR, xRCR, xGIER, xCR and xCIER). The MU does not assume any internal priority of these interrupts. Multiple interrupts (for example, Receive 0 and Receive 1 interrupts or any of the transmit and general purpose interrupts) can be asserted at one time. The priority of these interrupts should be resolved by the interrupt controller at the chip level. 

Triggering any enabled interrupt wakes up the Processor before servicing the interrupt. 

The General Purpose Interrupt Pending GIPn bits should be cleared by the software (as part of the interrupt service routine) to de-assert the request to the interrupt controller. 

When a Processor writes to the General Interrupt bit (GIRn), the write event is synchronized to the other Processor to set the general interrupt request pending bit (GIPn). When the GIPn bit is set, and if the general purpose interrupt is enabled on the receiving Processor side (GIEn bit is set), then the transmitting Processor general purpose interrupt is issued to the receiving Processor. The receiving Processor clears this interrupt by writing a “1” on the GIPn bit. The interrupt is de-asserted as soon as the GIPn bit is written. The write event of the GIPn bit is synchronized to the other Processor. The synchronized signal clears the GIR bit. The software should not write the GIRn bit again until the GIRn bit is cleared. 

Before setting a GIRn bit, you must verify that the GIRn bit is cleared, which means that a general interrupt is not pending. Generally, setting the GIRn bit while the bit has been set to “1” is ignored, but in some cases it may issue a second interrupt. 

### 39.3.3 Resets 

The MU has below reset sources, and each reset has a different function from the MU or system perspective. 

- Asynchronous system reset: 

   - The asynchronous system reset on one MU-side resets the other MU-side, forcing all control and status registers to return to their default values, and all internal states to be cleared. 

      - ◦Exceptions to this - MUA-side asynchronous system reset: 

▪MUB_CR[MURIE] 

▪MUB_SR[MURIP] 

▪MUB_SR[MURS] 

- ◦Exceptions to this - MUB-side asynchronous system reset: 

▪MUA_CR[MURIE] 

▪MUA_SR[MURIP] 

▪MUA_SR[MURS] 

- When the asynchronous system reset on any MU-side is asserted, the MURS bit in CR register is set to "1" until the asynchronous system reset ends. Check that the MURS bit is cleared before starting any access to MU. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1246 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

- MU software reset: 

— Writing the CR[MUR] bit to "1" causes most of control and status registers to return to their default values and all internal states to be cleared. 

— The instruction immediately following assertion of the MUR bit should not write to MU registers. Such a write may be overwritten by the reset sequence and the register remains with the reset value. You should monitor the value of the SR[MURS] bit to know when the reset sequence on both processors has ended. After the reset sequence on both processors has ended, you can attempt a write to MU registers. 

~~<mark>NOTE</mark>~~ 

MUR bit assertion is a delicate operation because it affects the other side’s registers asynchronously. MUR bit assertion may cause unpredictable behavior if, for example, the other Processor is concurrently testing an MU register bit (TE bit in the other Processor TSR register). Before asserting the MUR bit, you should verify that the other Processor is not presently engaged in an MU signalling activity. 

## 39.4 External Signals 

There are no Messaging Unit signals directly available externally. 

## 39.5 Application Information 

The following are some messaging examples: 

- Passing short messages: Transmit register(s) can be used to pass short messages from one to 4 words in length for Processor A and 4 for Processor B. For example, when a four-word message is desired, only one of the registers needs to have its corresponding interrupt enable bit set at the receiver side; the message’s first three words are written to the registers whose interrupt is masked, and the fourth word is written to the other register (which triggers an interrupt at the receiver side). 

- Passing frame information: Transmit registers can be used to pass frame information for long messages written to the shared system memory. Such frame information normally includes a start address, number of words, and perhaps a message type code. 

- Passing event notices and requests: Events and requests that do not include data words can be signaled from the Processor B to the Processor A using the general interrupts, such as acknowledging that a long message was read from the shared system memory. 

- Passing fixed length data: Formatted data with a fixed length can be written in predetermined locations in the shared memory. A processor can use a general interrupt to signal the other processor that the data is ready. 

- Passing announcements: The 3 flags can be used by a processor to announce its current program state or other billboard messages to the other processor. 

### 39.5.1 Messaging Protocols using Interrupts 

The example below describes a four-word messaging sequence sent by the Processor to the other Processor. 

In this example, the first, second, and third receive interrupts are disabled, and the fourth receive interrupt is enabled. We write registers sequentially for n = 0, 1, 2, 3. For n = 0, 1, 2, the interrupts are disabled, therefore no interrupt goes to the other core (although interrupt conditions occur). For n = 3, the interrupt is enabled, and the last Receive Interrupt request is generated. 

1. Write Sequence 

   - The Processor writes the message information sequentially to its Transmit Registers 0, 1, 2. 

   - When the write to the Transmit Register 3 occurs, the RF3 bit of the xRSR is set after synchronization, and it immediately trigger the Receive Full 3 interrupt to the other Processor. 

2. Read Sequence 

   - The other Processor receives the Receive Full 3 interrupt and starts reading the message transferred from the receive registers. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1247 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

- After Receive Register 3 is read, the interrupt bit is cleared. 

The following table and diagram describe the messaging model using transmit/receive registers and interrupt messaging protocol. 

Table 207. Interrupt Messaging Protocol (Generalized) 

|Sequence|Action|Description|
|---|---|---|
|1|Processor A Data write|A data write to the TRn register by Processor A is immediately<br>reflected in the Processor B RRn register.|
|2|Clear Tx Empty bit and Set Rx Full bit|The data write to the TRn register<br>• Clears the transmitter empty bit (TEn) in the Processor A<br>Transmit Status Register<br>• Sets the receiver full bit (RFn) in the Processor B Receive<br>Status Register|
|3|Generate Receive Interrupt request|The setting of the receiver full bit (RFn) in the Receive Status<br>Register generates a Receive Interrupt request to Processor B.|
|4|Processor B Data read|After receiving the Receive Interrupt request, Processor B<br>performs a data read of the RRn register.|
|5|Clear Rx Full bit and Set Tx Empty bit|Reading the data out of the RRn register<br>• Clears the receiver full bit (RFn) in the Processor B<br>Receive Status Register<br>• Sets the transmitter empty bit (TEn) in the Processor A<br>Transmit Status Register|
|6|Generate Transmit Interrupt request|The setting of the transmitter empty bit (TEn) in the Transmit<br>Status Register generates a Transmit Interrupt request to<br>Processor A.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1248 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1249-02.png)


<!-- Start of picture text -->
Processor A Processor B<br>Messaging Unit (MU)<br>Data write Transmitter side Receiver side Data read<br>1 4<br>Tx Status Rx Status<br>2 5<br>read from 4th receive register Tx Empty TEn setclear clearset RFn Rx Full transmit registerwrite from 4th<br>triggers interrupt triggers interrupt<br>Tx Control Rx Control<br>6 TIEn Interrupt Interrupt RIEn 3<br>Enable Enable<br>Transmit Receive<br>interrupt interrupt<br>request request<br>Registers Registers<br><!-- End of picture text -->

Figure 147. Messaging Model Using Transmit and Receive Registers 

The messaging hardware can be used by software to implement messaging protocols for a wide array of message types. Full support is given for both interrupt and polling management schemes. 

### 39.5.2 Messaging Protocols using Event Interrupts 

Events and requests that do not include data words can be signaled from the Processor B to the Processor A using the two general interrupts. 

Formatted data with a fixed length can be written in predetermined locations in the shared memory. A processor can use a general purpose interrupt to signal the other processor that the data is ready. 

The 3 flags can be used by a processor to announce to the other processor the program state it is currently in, or to announce similar messages. 

The following table and diagram describe the event sequence when the Processor triggers an interrupt. 

Table 208. General Interrupt Messaging Protocol (Generalized) 

|Sequence|Action|Description|
|---|---|---|
|1|Processor A sets General Interrupt<br>request bit|Processor A sets its associated General Interrupt request bit<br>(GIRn = 1) in the General Control Register (GCR).|
|2|General Interrupt Request Pending<br>status bit is set|The General Interrupt Request Pending status bit (GIPn) in the<br>General Status Register (GSR) is set to "1".|
|3|General Interrupt request to<br>Processor B is generated|Setting the GIPn bit generates the General Interrupt request to<br>Processor B (Interrupt Request Enable bit, GIEn, must be set<br>for Processor B).|
|4|Processor B reads status register|The Processor B reads the GIPn bit in the GSR register.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1249 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

Table 208. General Interrupt Messaging Protocol (Generalized) (continued) 

|Sequence|Action|Description|
|---|---|---|
|5|Processor B services the interrupt|-|
|6|Processor B sets GIPn bit to<br>clear interrupt|The Processor B writes "1" to the corresponding GIPn bit to<br>clear the interrupt.|
|7|GIRn bit is cleared|Setting the GIPn bit to "1" clears the General Interrupt request<br>bit (GIRn) in the Processor A General Control Register (GCR).|




![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1250-04.png)


<!-- Start of picture text -->
Processor A Processor B<br>Messaging Unit (MU)<br>4<br>Read GIPn bit<br>Control Status<br>Services<br>5<br>Interrupt<br>1 set GIRn int req 2 7 set GIPn int pend 6<br>clear Write "1" to clear<br>GCR GSR<br>Register Register<br>Control<br>Interrupt GIEn 3 General Purpose<br>Enable Interrupt Request<br>GIER<br>Register<br><!-- End of picture text -->

Figure 148. Messaging Model Using a General Purpose Interrupt 

### 39.5.3 Exclusive Access to Shared Memory 

MU can be used to signal one processor about its current access to the shared memory, so that the data is not overwritten by the other processor during the exclusive memory access period. 

The following tables describe the signaling protocol that the Processor A uses to inform the Processor B about its current access (write) to the shared memory, assuming that the set of bits and registers (GIRn bit, RRn register, TRn register) are reserved to support exclusive access to the shared memory protocol. 

Table 209. How the Processor A Performs an Exclusive Access to Shared Memory 

|Sequence|Action|Description|
|---|---|---|
|1|Processor A sends GIRn request|When the Processor A wants to perform an exclusive access to|
||to Processor B using Processor A|the shared memory, the Processor A sends an GIR0 request to|
||control register|the Processor B.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1250 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

Table 209. How the Processor A Performs an Exclusive Access to Shared Memory (continued) 

|Sequence|Action|Description|
|---|---|---|
|2|Processor A sends an exclusive-<br>access request using a transmit data<br>register (TRn)|The Processor A sends an exclusive-access request<br>(command, location, and length of target access) to Processor<br>B using a selected transmit data register (TR0).|
|3|Processor A waits for a dedicated<br>interrupt from Processor B|The Processor A waits for a dedicated interrupt (as<br>an acknowledgement) triggered by the Processor B<br>before proceeding.|
|4|Processor A accesses<br>shared memory|After receiving a dedicated interrupt from the Processor B,<br>Processor A proceeds.|



Table 210. How the Processor B Scans for Transaction Information 

|Sequence|Action|Description|
|---|---|---|
|1|Processor B receives an interrupt<br>from a receive data register (RRn)|-|
|2|Processor B reads the receive data<br>register (RRn)|-|
|3|Processor B scans the receive data<br>register contents|For transaction information (whether Processor A has<br>requested an exclusive-access).|



Table 211. How the Processor B Accepts Exclusive Access by Processor A 

|Sequence|Action|Description|
|---|---|---|
|1|Processor B triggers a<br>dedicated interrupt|Processor B acknowledges the Processor A request by<br>triggering a dedicated interrupt (ack) to the Processor A.|
|2|Processor B sends a code message<br>to Processor A|Along with the acknowledge interrupt, the Processor B sends<br>a code message to the Processor A through the selected<br>transmit register (TRn). The message informs the Processor A<br>that it can exclusively access the shared memory.|



Table 212. How the Processor B Rejects Exclusive Access by Processor A 

|Sequence|Action|Description|
|---|---|---|
|1|Processor B ignores Processor A|If the Processor B does not want to give go-ahead permission|
||request for exclusive access|to the Processor A, Processor B ignores the exclusive<br>access request.|



### 39.5.4 Packet Data Transfers 

The following example describes the packet transfer sequence between the Processor B and Processor A subsystems: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1251 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

Table 213. Packet Data Transfer Sequence 

|Action|Sequence|Description|
|---|---|---|
|Processor B requests DMA|1|The Processor B sends a DMA request to initiate the packet<br>data transfer.|
|DMA data transfer|2|DMA acknowledges.|
||3|DMA starts transferring data from the specified Processor B location<br>to the specified shared memory|
||4|DMA interrupts the Processor B to signal that the packet transfer<br>has finished.|
|Processor B informs Processor A<br>that data is in shared memory|5|Using an MU Processor B-side transmit register, the Processor B<br>sends a packet information message to the Processor A to inform the<br>Processor A of the arrival of new packet data that is stored in shared<br>memory. The message contains the command, location, and length of<br>packet data information.|
|Processor A receives interrupt|6|The Processor A receives an interrupt (assuming its corresponding<br>Processor A MU-side receive interrupt is enabled), and the<br>pending processing task becomes active and processes packet data<br>from memory.|
|Processor A reads data, writes data|7|The Processor A reads or processes packet data from<br>shared memory.|
||8|The Processor A writes the result from packet processing to a<br>separate buffer.|
|Processor A informs Processor B<br>that transfer is finished|9|After the processing of the packet data finishes, the Processor A<br>informs the Processor B (using the MU Processor A-side transmit<br>register, ATRn).|
|Processor A sends interrupt to<br>Processor B (request for more data)|10|The Processor B receives the next interrupt from the Processor A, in<br>which the Processor A requests more packet data.|



### 39.5.5 Free the Processor from Deadlock 

During normal operations, one processor may conclude that the other processor is not working or is deadlocked. Using the SR register, the following methods are available for the processor to use to identify and correct the problem. 

Table 214. How to Free the Processor A/B from Deadlock 

|Processor Mode|Technique|Description|
|---|---|---|
|-|Processor issues an interrupt|The other Processor can interrupt the Processor by<br>issuing any one of the 9 (general purpose, receive, and<br>transmit) interrupts|
|-|Processor issues a hardware reset|If the above is not helpful, the Processor can issue a<br>hardware reset strobe to the other Processor.|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1252 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

## 39.6 Register Definition 

The MU provides transmit and receive data registers (xTR0-n, xRR0-n) for the communication between Processor A and Processor B. Some control and status registers (xCR, xSR) to the Processor A and Processor B sides for control operations (such as interrupts and reset), and for status checking of the other MU-side. Figure 149 shows the MU registers schematic. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1253-04.png)


<!-- Start of picture text -->
Processor Other<br>Processor<br>Messaging Unit (MU)<br>xCR xSR<br>xSR xCR<br>xRR0-n xTR0-n<br>xTR0-n xRR0-n<br><!-- End of picture text -->

Figure 149. MU Registers 

The detailed MU Register Definition can be found below. 

### 39.6.1 MUA register descriptions 

This section contains the detailed register descriptions for the MUA registers. 

~~<mark>NOTE</mark>~~ 

A read/write access to any illegal location and a write to a read-only register on the Processor A-side or Processor B-side of the MU generates a module transfer error acknowledge to the Processor A or Processor B. 

#### 39.6.1.1 MUA memory map 

MU_2.MUA base address: 400B_8000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|Version ID Register (VER)|32|RO|0309_000Fh|
|4h|Parameter Register (PAR)|32|RO|0301_0404h|
|8h|Control Register (CR)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1253 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|Ch|Status Register (SR)|32|W1C|See<br>description|
|100h|Flag Control Register (FCR)|32|RW|0000_0000h|
|104h|Flag Status Register (FSR)|32|RO|0000_0000h|
|110h|General Interrupt Enable Register (GIER)|32|RW|0000_0000h|
|114h|General Control Register (GCR)|32|RW|0000_0000h|
|118h|General Status Register (GSR)|32|W1C|0000_0000h|
|120h|Transmit Control Register (TCR)|32|RW|0000_0000h|
|124h|Transmit Status Register (TSR)|32|RO|0000_000Fh|
|128h|Receive Control Register (RCR)|32|RW|0000_0000h|
|12Ch|Receive Status Register (RSR)|32|RO|0000_0000h|
|200h - 20Ch|Transmit Register (TR0 - TR3)|32|RW|0000_0000h|
|280h - 28Ch|Receive Register (RR0 - RR3)|32|RO|0000_0000h|



#### 39.6.1.2 Version ID Register (VER) 

##### Offset 

|Register|Offset|
|---|---|
|VER|0h|



##### Function 

Use Version ID register to determine the version ID and feature set number of MUA. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||MA|JOR|||||||MIN|OR||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|1|1|0|0|0|0|1|0|0|1|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||FEAT|URE||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1254 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Fields 

|Field|Function|
|---|---|
|31-24|Major Version Number|
|MAJOR||
|23-16|Minor Version Number|
|MINOR||
|15-0|Feature Set Number|
|FEATURE|Each bit of the Feature Set Number bitfield specifies a different feature:<br>• If bit0 = 1: Standard features are implemented<br>• If bit1 = 1: RAIP/RAIE register bits are implemented<br>• If bit2 = 1: Core Control and Status Registers are implemented in both MUA and MUB<br>• If bit3 = 1: Expand TRn/RRn registers number<br>• Bit4-bit15: Reserved for future use|



#### 39.6.1.3 Parameter Register (PAR) 

##### Offset 

|Register|Offset|
|---|---|
|PAR|4h|



##### Function 

The PAR register defines the number of flags, transmit registers, receive registers, and the number of general interrupt requests available for the MU. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||FLAG_|WIDTH|||||||GIR_|NUM||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|1|1|0|0|0|0|0|0|0|1|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||RR_|NUM|||||||TR_N|UM||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|1|0|0|0|0|0|0|0|1|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1255 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Fields 

|Field|Function|
|---|---|
|31-24|Flag Width|
|FLAG_WIDTH|This bitfield specifies the number of flag bits in the Flag Control Register (FCR) and Flag Status Register<br>(FSR).|
|23-16|General Interrupt Request Number|
|GIR_NUM|This bitfield specifies the number of general interrupt requests available.|
|15-8|RR Number|
|RR_NUM|This bitfield specifies the number of receive registers.|
|7-0|Transmit Register Number|
|TR_NUM|This bitfield specifies the number of transmit registers.|



#### 39.6.1.4 Control Register (CR) 

##### Offset 

|Register|Offset|
|---|---|
|CR|8h|



##### Function 

The CR register controls the MU reset and MU reset interrupt enable. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1256-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>MURIE  MUR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function||
|---|---|---|
|31-2|Reserved||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1256 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|1|MUA Reset Interrupt Enable|
|MURIE|• If MURIE bit is set to "1", then MU reset interrupt request is issued to the Processor A when the<br>MUA_SR[MURIP] bit is set to "1".<br>• If MURIE is cleared, then the value of the MURIP bit is ignored and no MU reset interrupt request is<br>issued.|
||• Only system reset can reset MURIE, MU reset(MUR) cannot reset this bit.<br>0b - Disables Processor A-side MU Reset Interrupt request due to MU reset issued by MUB.<br>1b - Enables Processor A-side MU Reset Interrupt request due to MU reset issued by MUB.|
|0|MU Reset|
|MUR|• Setting MUR bit to "1" resets both the MUA-side and MUB-side, forcing all control and status<br>registers to return to their default values (except MURIE in MUA/B_CR registers, MURIP bit and<br>MURS bit in MUA/B_SR registers), and all internal states to be cleared.<br>• Before setting the MUR bit to "1", it is advisable to interrupt the Processor B, because setting the<br>MUR bit may affect the ongoing Processor B program.<br>• After setting the MUR bit, monitor the value of the MUA_SR[MURS] bit to know when the reset<br>sequence on the Processor B-side has ended.<br>• MUR bit is always read as "0".<br>• MUR bit is cleared during the MU reset sequence.<br>0b - Self clearing bit.|
||1b - Asserts the MU reset.|



#### 39.6.1.5 Status Register (SR) 

##### Offset 

|Register|Offset|
|---|---|
|SR|Ch|



##### Function 

The SR register shows the status of MU resets and the status of pending events/requests described below. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1257 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||||0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||0|||||0|RFP|TEP|GIRP|FUP|EP|MURIP|MURS|
|W|||||||||||||||W1C||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|u|



##### Fields 

|Field|Function|
|---|---|
|31-8<br>—|Reserved|
|7<br>—|Reserved|
|6<br>RFP|MUA Receive Full Pending Flag<br>• RFP bit is set to "1" when any TRn register is written by MUB to send data to MUA.<br>• After the RFP bit is set to "1", checking the RSR[RFn] bit to decide the data in which RRn register is<br>ready to be read by the MUA.<br>• RFP bit is cleared when all MUA RRn registers are read, or when the MU is reset.<br>0b - No TRn register is written by MUB.<br>1b - Any TRn register is written by MUB.|
|5<br>TEP|MUA Transmit Empty Pending<br>• TEP bit is set to "1" when TCR[TIEn] bit is set and the corresponding RRn register is read by MUB.<br>• After the TEP bit is set to "1", checking the TSR[TEn] bit to decide the data in which TRn register is<br>ready to be written by the MUA.<br>• TEP bit is cleared when all MUA TRn register are written.<br>• TEP bit is set to "0" when the MU resets.<br>0b - RRn register is not read by MUB.<br>1b - Any RRn register is read by MUB.|
|4<br>GIRP|MUA General Interrupt Pending<br>• GIRP bit is set to "1" when any general interrupt request is sent from the MUB side to the MUA side.<br>Reading the GSR[GIPn] bit can know which general interrupt request is received.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1258 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function<br>• GIRP bit is cleared when all GIPn bits in MUA_GSR register are cleared.<br>• GIRP bit is cleared when the MU resets.<br>0b - No general interrupt request is sent from MUB.<br>1b - Any general interrupt request is sent from MUB.|
|---|---|
|3<br>FUP|MUA Flags Update Pending<br>• FUP bit is set to "1" when the MUA side sends a Flags Update request to the MUB side.<br>• A Flags Update request is generated when there is a change to the Fn[2:0] bits of the MUA_FCR<br>register. No flag update changes are allowed while the FUP bit is set to "1". Any write to the Fn[2:0]<br>bits of the MUA_FCR register, while the FUP bit is set to "1", does not generate a Flags Update<br>event, and the Fn[2:0] bits stays unchanged.<br>• Writing the FCR register doesn't set FUP bit immediately if there is any event pending(SR[EP] is<br>"1").<br>• FUP bit is cleared when this Flags Update request is internally acknowledged (the flag is updated)<br>from the MUB side, or during MU reset.<br>0b - No pending update flags(initiated by MUA) are in process<br>1b - Pending update flags(initiated by MUA) are in process|
|2<br>EP|MUA Side Event Pending<br>• An "event" is any hardware message that is reflected in the status register on the MUB side (for<br>example, "transmit register 0 written"). During normal operations, the update mechanism for the EP<br>bit works automatically.<br>• EP bit is set to "1" when the MUA side sends an event update request to the MUB side.<br>• EP bit is cleared by hardware automatically when the event update acknowledge is received.<br>• To ensure events have been posted to MUB, verify that the EP bit is cleared. If EP bit is set to "1",<br>wait and continue to poll the EP bit.<br>• The EP bit is cleared when the MU resets.<br>0b - The MUA side event is not pending.<br>1b - The MUA side event is pending.|
|1<br>MURIP|MU Reset Interrupt Pending<br>• MURIP bit signals Processor A that Processor B initiated a MU reset by setting the MUB_CR[MUR]<br>bit.<br>• MURIP bit is set to "1" after Processor B initiated a MU reset. If the interrupt is enabled by the<br>MURIE bit, the Processor A MU reset interrupt request is issued when the Processor B set MUR bit<br>in MUB_CR.<br>• Writing "1" to clear the MURIP bit, which also clears MU reset interrupt request.<br>• Only system reset can reset MURIP. MU reset cannot reset this bit.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1259 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Processor B did not issue MU reset.|
||1b - Processor B issued MU reset.|
|0|MUA and MUB Reset State|
|MURS|• The MURS bit is set to "1" during any system reset or any MU reset from MUA-side or MUB-side.|
||• The MURS bit is cleared when the reset sequence on both MUA and MUB side ends. After issuing<br>any of the reset events mentioned previously,verify that the MURS bit is cleared before starting any<br>access.|
||0b - MUA and MUB are out of reset.|
||1b - MUA or MUB is in reset state.|



#### 39.6.1.6 Flag Control Register (FCR) 

##### Offset 

|Register|Offset|
|---|---|
|FCR|100h|



##### Function 

The FCR register contains read-write flags that reflect the MUB_FSR[Fn] bits. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||||0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||||||0|||||||F2|F1|F0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-3<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1260 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|2-0|MUA to MUB Flag n|
|Fn|• n = 0 to 2|
||• Fn bit is a read-write flag that reflects the MUB_FSR[Fn] bits.|
||• Fn bits are cleared when the MU resets.<br>• Write 0 to an Fn bit - Clears the Fn bit in the MUB_FSR register.<br>• Write 1 to an Fn bit - Sets the Fn bit in the MUB_FSR register.|
||0b - Clears the Fn bit in the FSR register.<br>1b - Sets the Fn bit in the FSR register.|



#### 39.6.1.7 Flag Status Register (FSR) 

##### Offset 

|Register|Offset|
|---|---|
|FSR|104h|



##### Function 

The FSR register contains flags that reflect the values written to the Fn bit of the MUB_FCR register. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1261-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 F2  F1  F0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-3<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1261 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|2-0|MUB to MUA Side Flag n|
|Fn|• n = 0 to 2|
||• Fn bit is the MUA side flag that reflects the values written to the Fn bit in the MUB_FCR register.|
||• Every time that the Fn bit in the MUB_FCR register is written, the Fn bit in the MUB FCR register write<br>event updates the Fn bit in the MUA_FSR register after the event update latency.<br>• If a 0 is read from an Fn bit - Fn bit in the MUB_FCR is 0.<br>• If a 1 is read from an Fn bit - Fn bit in the MUB_FCR is 1.<br>0b - Fn bit in the MUB FCR register is written 0.|
||1b - Fn bit in the MUB FCR register is written 1.|



#### 39.6.1.8 General Interrupt Enable Register (GIER) 

##### Offset 

|Register|Offset|
|---|---|
|GIER|110h|



##### Function 

The GIER register contains the MUA general purpose interrupt enables. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||0|||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||0||||||||GIE0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-1<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1262 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|0-0|MUA General Purpose Interrupt Enable n|
|GIEn|• There are 1 General Purpose Interrupts (n = 0 to 0)|
||• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor A when the GIPn bit<br>in the MUA GSR register is set to "1".|
||• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.|
||0b - Disables MUA General Interrupt n.|
||1b - Enables MUA General Interrupt n.|



#### 39.6.1.9 General Control Register (GCR) 

##### Offset 

|Register|Offset|
|---|---|
|GCR|114h|



##### Function 

The GCR register contains the MUA general purpose interrupt requests. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1263-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>GIR0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-1<br>—|Reserved|
|0-0|MUA General Purpose Interrupt Request n|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1263 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|GIRn|• There are 1 General Purpose Interrupts (n = 0 to 0)<br>• Writing "1" to the GIRn bit sets the MUB_GSR[GIPn] bit on the MUB-side. If the MUB_GIER[GIEn]<br>bit is set to "1" on the MUB-side, a General Purpose Interrupt n request is triggered to Processor B.<br>• The GIRn bit is cleared if the MUB_GSR[GIPn] bit is cleared by writing "1", thereby signalling the<br>MUA that the interrupt was accepted (cleared by the software).<br>• Writing "0" to the GIRn bit is ignored.<br>• To ensure proper operations, you must verify that the GIRn bit is cleared (meaning that there is no<br>pending interrupt) before setting it (GIRn bit).<br>• GIRn bit is cleared when the MU resets.<br>0b - MUA General Interrupt n is not requested to the MUB.<br>1b - MUA General Interrupt n is requested to the MUB.|



#### 39.6.1.10 General Status Register (GSR) 

##### Offset 

|Register|Offset|
|---|---|
|GSR|118h|



##### Function 

The GSR register contains the status of the MUA general interrupt pending requests. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0||||||||GIP0|
|W||||||||||||||||W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field<br>Function|
|---|
|31-1<br>Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1264 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|0-0|MUA General Interrupt Request Pending n|
|GIPn|• There are 1 General Purpose Interrupts (n = 0 to 0)<br>• GIPn bit signals the MUA that the MUB_GCR[GIRn] bit was set from "0" to "1". If the<br>MUA_GIER[GIEn] bit is set to "1", a General Interrupt n request is issued to Processor A.<br>• The GIPn bit is cleared by writing "1". Writing "0" is ignored.<br>• GIPn bit is cleared when the MU resets.<br>• After GIPn bit is cleared, the General Interrupt n request(if the MUA_GIER[GIEn] bit is set to "1") is<br>cleared on the MUA side.|
||0b - MUA general purpose interrupt n is not pending.<br>1b - MUA general purpose interrupt n is pending.|



#### 39.6.1.11 Transmit Control Register (TCR) 

##### Offset 

|Register|Offset|
|---|---|
|TCR|120h|



##### Function 

The TCR register contains the MUA transmit interrupt enables. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||0|||||||||
|Reset<br>Bits|0<br>15|0<br>14|0<br>13|0<br>12|0<br>11|0<br>10|0<br>9|0<br>8|0<br>7|0<br>6|0<br>5|0<br>4|0<br>3|0<br>2|0<br>1|0<br>0|
|R<br>W||||||0|||||||TIE3|TIE2|TIE1|TIE0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1265 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Fields 

|Field|Function|
|---|---|
|31-4|Reserved|
|—||
|3-0|MUA Transmit Interrupt Enable n|
|TIEn|• There are 4 Transmit Interrupts (n = 0 to 3)<br>• If TIEn bit is set to "1", then an MUA Transmit Interrupt n request is issued when the MUA_TSR[TEn]<br>bit is set to "1".<br>• If TIEn bit is cleared, then the value of the TEn bit is ignored and no MUA Transmit Interrupt n<br>request is issued.|
||• TIEn bit is cleared when the MU resets.|
||0b - Disables MUA Transmit Interrupt n. (default)<br>1b - Enables MUA Transmit Interrupt n.|



#### 39.6.1.12 Transmit Status Register (TSR) 

##### Offset 

|Register|Offset|
|---|---|
|TSR|124h|



##### Function 

The TSR register shows whether the MUA transmit registers are empty or not. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1266-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 TE3  TE2  TE1  TE0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1266 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Fields 

|Field|Function|
|---|---|
|31-4|Reserved|
|—||
|3-0|MUA Transmit Register n Empty|
|TEn|• There are 4 Transmit Registers (n = 0 to 3)<br>• The TEn bit is set to "1" after the MUB RRn register is read on the MUB side.<br>• After the TEn bit is set to "1", it signals the MUA side that the MUA TRn register is ready<br>to be written on the MUA side, and a Transmit n interrupt is issued on the MUA side (if the<br>MUA_TCR[TIEn] bit is set to "1").<br>• TEn bit is cleared after the MUA TRn register is written on the MUA side.<br>• After TEn bit is cleared, the Transmit n interrupt(if the MUA_TCR[TIEn] bit is set to "1") is cleared on<br>the MUA side.<br>• TEn bit is set to "1" when the MU resets.<br>0b - MUA TRn register is not empty.<br>1b - MUA TRn register is empty.|



#### 39.6.1.13 Receive Control Register (RCR) 

##### Offset 

|Register|Offset|
|---|---|
|RCR|128h|



##### Function 

The RCR register contains the MUA receive interrupt enables. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||0|||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||0|||||||RIE3|RIE2|RIE1|RIE0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1267 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Fields 

|Field|Function|
|---|---|
|31-4|Reserved|
|—||
|3-0|MUA Receive Interrupt Enable n|
|RIEn|• There are 4 Transmit Interrupts (n = 0 to 3)<br>• If RIEn bit is set to "1", then an MUA Receive Interrupt n request is issued when the MUA_RSR[RFn]<br>bit is set to "1".<br>• If RIEn bit is cleared, then the value of the RFn bit is ignored and no MUA Receive Interrupt n<br>request is issued.|
||• RIEn bit is cleared when the MU resets.|
||0b - Disables MUA Receive Interrupt n.<br>1b - Enables MUA Receive Interrupt n.|



#### 39.6.1.14 Receive Status Register (RSR) 

##### Offset 

|Register|Offset|
|---|---|
|RSR|12Ch|



##### Function 

The RSR register shows whether the MUA receive registers are full or not. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||||0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||0|||||||RF3|RF2|RF1|RF0|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1268 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Fields 

|Field|Function|
|---|---|
|31-4|Reserved|
|—||
|3-0|MUA Receive Register n Full|
|RFn|• There are 4 Receive Registers (n = 0 to 3)<br>• The RFn bit is set to "1" when the MUB TRn register is written on the MUB side.<br>• After the RFn bit is set to "1", the RFn bit signals the MUA side that new data in the MUA RRn<br>register is ready to be read by the MUA, and a Receive n interrupt is issued on the MUA side (if the<br>MUA_RCR[RIEn] has been set to "1").<br>• RFn bit is cleared when the MUA RRn register is read, or when the MU is reset.<br>• After RFn bit is cleared, the Receive n interrupt(if the MUA_RCR[RIEn] has been set to "1") is<br>cleared on the MUA side.<br>0b - MUA RRn register is not full.<br>1b - MUA RRn register has received data from MUB TRn register and is ready to be read by the<br>MUA.|



#### 39.6.1.15 Transmit Register (TR0 - TR3) 

##### Offset 

|Register|Offset|
|---|---|
|TR0|200h|
|TR1|204h|
|TR2|208h|
|TR3|20Ch|



##### Function 

##### MUA Transmit Data. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||TR_D|ATA||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||TR_D|ATA||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1269 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Fields 

- Field Function 31-0 MUA Transmit Data 

- TR_DATA • Data written to the TRn register is reflected in the MUB Receive Register n (RRn). The TRn and RRn registers are not double-buffered, a write to the TRn register overrides the data readable at the RRn register. 

- • A write to the transmit register clears the MUA_TSR[TEn] bit on the transmitter side, and sets the MUB_RSR[RFn] bit on the receiver side. 

- • TRn register can be written only when the MUA_TSR[TEn] bit is set to "1". • Reading the TRn register returns all zeros. 

#### 39.6.1.16 Receive Register (RR0 - RR3) 

##### Offset 

|Register|Offset|
|---|---|
|RR0|280h|
|RR1|284h|
|RR2|288h|
|RR3|28Ch|



##### Function 

##### MUA Receive Data. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1270-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RR_DATA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RR_DATA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-0|MUA Receive Data|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1270 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

- Field Function 

- RR_DATA • Reflects the data written to MUB Transmit Register (TRn). • Reading the RRn register clears the MUA_RSR[RFn] bit on the receiver side, and sets the MUB_TSR[TEn] bit on the transmitter side. 

- • RRn register can be read only when the MUB_RSR[RFn] bit is set to "1". Reading before MUB_RSR[RFn]=1 may result in reading incorrect data. Therefore, polling the MUB_RSR[RFn] bit to confirm it is set to "1" before reading RRn is required. 

- • Writing to the RRn register generates an error response to the MUA. 

### 39.6.2 MUB register descriptions 

This section contains the detailed register descriptions for the MUB registers. 

~~<mark>NOTE</mark>~~ 

A read/write access to any illegal location and a write to a read-only register on the Processor A-side or Processor B-side of the MU generates a module transfer error acknowledge to the Processor A or Processor B. 

#### 39.6.2.1 MUB memory map 

MU_0.MUB base address: 4038_C000h 

MU_1.MUB base address: 404E_C000h 

MU_2.MUB base address: 400B_C000h 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|0h|Version ID Register (VER)|32|RO|0309_000Fh|
|4h|Parameter Register (PAR)|32|RO|See<br>description|
|8h|Control Register (CR)|32|RW|0000_0000h|
|Ch|Status Register (SR)|32|W1C|See<br>description|
|10h|Core Control Register 0 (CCR0)|32|RW|0000_0000h|
|18h|Core Sticky Status Register 0 (CSSR0)|32|W1C|See<br>description|
|100h|Flag Control Register (FCR)|32|RW|0000_0000h|
|104h|Flag Status Register (FSR)|32|RO|0000_0000h|
|110h|General Interrupt Enable Register (GIER)|32|RW|0000_0000h|
|114h|General Control Register (GCR)|32|RW|0000_0000h|
|118h|General Status Register (GSR)|32|W1C|0000_0000h|
|120h|Transmit Control Register (TCR)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1271 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|124h|Transmit Status Register (TSR)|32|RO|0000_000Fh|
|128h|Receive Control Register (RCR)|32|RW|0000_0000h|
|12Ch|Receive Status Register (RSR)|32|RO|0000_0000h|
|200h - 20Ch|Transmit Register (TR0 - TR3)|32|RW|0000_0000h|
|280h - 28Ch|Receive Register (RR0 - RR3)|32|RO|0000_0000h|



#### 39.6.2.2 Version ID Register (VER) 

##### Offset 

|Register|Offset|
|---|---|
|VER|0h|



##### Function 

Use Version ID register to determine the version ID and feature set number of MUB. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||MAJ|OR|||||||MIN|OR||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|1|1|0|0|0|0|1|0|0|1|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||FEAT|URE||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|



Fields 

|Field|Function|
|---|---|
|31-24|Major Version Number|
|MAJOR||
|23-16|Minor Version Number|
|MINOR||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1272 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|15-0|Feature Set Number|
|FEATURE|Each bit of the Feature Set Number bitfield specifies a different feature:|
||• If bit0 = 1: Standard features are implemented|
||• If bit1 = 1: RAIP/RAIE register bits are implemented|
||• If bit2 = 1: Core Control and Status Registers are implemented in both MUA and MUB|
||• If bit3 = 1: Expand TRn/RRn registers number|
||• Bit4-bit15: Reserved for future use|



#### 39.6.2.3 Parameter Register (PAR) 

##### Offset 

|Register|Offset|
|---|---|
|PAR|4h|



##### Function 

The PAR register defines the number of flags, transmit registers, receive registers, and the number of general interrupt requests available for the MU. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1273-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R FLAG_WIDTH  GIR_NUM<br>W<br>Reset See Register reset values.<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RR_NUM  TR_NUM<br>W<br>Reset See Register reset values.<br><!-- End of picture text -->

##### Register reset values 

|Register|Reset value|
|---|---|
|PAR|MU_0.MUB,MU_1.MUB: 2020_0404h|
||MU_2.MUB: 0301_0404h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1273 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Fields 

|Field|Function|
|---|---|
|31-24|Flag Width|
|FLAG_WIDTH|This bitfield specifies the number of flag bits in the Flag Control Register (FCR) and Flag Status Register<br>(FSR).|
|23-16|General Interrupt Request Number|
|GIR_NUM|This bitfield specifies the number of general interrupt requests available.|
|15-8|RR Number|
|RR_NUM|This bitfield specifies the number of receive registers.|
|7-0|Transmit Register Number|
|TR_NUM|This bitfield specifies the number of transmit registers.|



#### 39.6.2.4 Control Register (CR) 

##### Offset 

|Register|Offset|
|---|---|
|CR|8h|



##### Function 

The CR register controls the MU reset and MU reset interrupt enable. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1274-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>MURIE  MUR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function||
|---|---|---|
|31-2|Reserved||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1274 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|1|MUB Reset Interrupt Enable|
|MURIE|• If MURIE bit is set to "1", then MU reset interrupt request is issued to the Processor B when the<br>MUB_SR[MURIP] bit is set to "1".<br>• If MURIE is cleared, then the value of the MURIP bit is ignored and no MU reset interrupt request is<br>issued.|
||• Only system reset can reset MURIE, MU reset(MUR) cannot reset this bit.<br>0b - Disables Processor B-side MU Reset Interrupt request due to MU reset issued by MUA.<br>1b - Enables Processor B-side MU Reset Interrupt request due to MU reset issued by MUA.|
|0|MU Reset|
|MUR|• Setting MUR bit to "1" resets both the MUB-side and MUA-side, forcing all control and status<br>registers to return to their default values (except in MUB/A_CCR0 registers, MURIE in MUB/A_CR<br>registers, MURIP bit and MURS bit in MUB/A_SR registers), and all internal states to be cleared.<br>• Before setting the MUR bit to "1", it is advisable to interrupt the Processor A, because setting the<br>MUR bit may affect the ongoing Processor A program.<br>• After setting the MUR bit, monitor the value of the MUB_SR[MURS] bit to know when the reset<br>sequence on the Processor A-side has ended.<br>• MUR bit is always read as "0".<br>• MUR bit is cleared during the MU reset sequence.<br>0b - Self clearing bit.|
||1b - Asserts the MU reset.|



#### 39.6.2.5 Status Register (SR) 

##### Offset 

|Register|Offset|
|---|---|
|SR|Ch|



##### Function 

The SR register shows the status of MU resets and the status of pending events/requests described below. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1275 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||||0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||0|||||0|RFP|TEP|GIRP|FUP|EP|MURIP|MURS|
|W|||||||||||||||W1C||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|u|



##### Fields 

|Field|Function|
|---|---|
|31-8<br>—|Reserved|
|7<br>—|Reserved|
|6<br>RFP|MUB Receive Full Pending Flag<br>• RFP bit is set to "1" when any TRn register is written by MUA to send data to MUB.<br>• After the RFP bit is set to "1", checking the RSR[RFn] bit to decide the data in which RRn register is<br>ready to be read by the MUB.<br>• RFP bit is cleared when all MUB RRn registers are read, or when the MU is reset.<br>0b - No TRn register is written by MUA.<br>1b - Any TRn register is written by MUA.|
|5<br>TEP|MUB Transmit Empty Pending<br>• TEP bit is set to "1" when TCR[TIEn] bit is set and the corresponding RRn register is read by MUA.<br>• After the TEP bit is set to "1", checking the TSR[TEn] bit to decide the data in which TRn register is<br>ready to be written by the MUB.<br>• TEP bit is cleared when all MUB TRn register are written.<br>• TEP bit is set to "0" when the MU resets.<br>0b - RRn register is not read by MUA.<br>1b - Any RRn register is read by MUA.|
|4<br>GIRP|MUB General Interrupt Pending<br>• GIRP bit is set to "1" when any general interrupt request is sent from the MUA side to the MUB side.<br>Reading the GSR[GIPn] bit can know which general interrupt request is received.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1276 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function<br>• GIRP bit is cleared when all GIPn bits in MUB_GSR register are cleared.<br>• GIRP bit is cleared when the MU resets.<br>0b - No general interrupt request is sent from MUA.<br>1b - Any general interrupt request is sent from MUA.|
|---|---|
|3<br>FUP|MUB Flags Update Pending<br>• FUP bit is set to "1" when the MUB side sends a Flags Update request to the MUA side.<br>• A Flags Update request is generated when there is a change to the Fn[31:0] bits of the MUB_FCR<br>register. No flag update changes are allowed while the FUP bit is set to "1". Any write to the Fn[31:0]<br>bits of the MUB_FCR register, while the FUP bit is set to "1", does not generate a Flags Update<br>event, and the Fn[31:0] bits stays unchanged.<br>• Writing the FCR register doesn't set FUP bit immediately if there is any event pending(SR[EP] is<br>"1").<br>• FUP bit is cleared when this Flags Update request is internally acknowledged (the flag is updated)<br>from the MUA side, or during MU reset.<br>0b - No pending update flags(initiated by MUB) are in process<br>1b - Pending update flags(initiated by MUB) are in process|
|2<br>EP|MUB Side Event Pending<br>• An "event" is any hardware message that is reflected in the status register on the MUA side (for<br>example, "transmit register 0 written"). During normal operations, the update mechanism for the EP<br>bit works automatically.<br>• EP bit is set to "1" when the MUB side sends an event update request to the MUA side.<br>• EP bit is cleared by hardware automatically when the event update acknowledge is received.<br>• To ensure events have been posted to MUA, verify that the EP bit is cleared. If EP bit is set to "1",<br>wait and continue to poll the EP bit.<br>• The EP bit is cleared when the MU resets.<br>0b - The MUB side event is not pending.<br>1b - The MUB side event is pending.|
|1<br>MURIP|MU Reset Interrupt Pending<br>• MURIP bit signals Processor B that Processor A initiated a MU reset by setting the MUA_CR[MUR]<br>bit.<br>• MURIP bit is set to "1" after Processor A initiated a MU reset. If the interrupt is enabled by the<br>MURIE bit, the Processor B MU reset interrupt request is issued when the Processor A set MUR bit<br>in MUA_CR.<br>• Writing "1" to clear the MURIP bit, which also clears MU reset interrupt request.<br>• Only system reset can reset MURIP. MU reset cannot reset this bit.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1277 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Processor A did not issue MU reset.|
||1b - Processor A issued MU reset.|
|0|MUA and MUB Reset State|
|MURS|• The MURS bit is set to "1" during any system reset or any MU reset from MUA-side or MUB-side.|
||• The MURS bit is cleared when the reset sequence on both MUA and MUB side ends. After issuing<br>any of the reset events mentioned previously,verify that the MURS bit is cleared before starting any<br>access.|
||0b - MUA and MUB are out of reset.|
||1b - MUA or MUB is in reset state.|



#### 39.6.2.6 Core Control Register 0 (CCR0) 

##### Offset 

|Register|Offset|
|---|---|
|CCR0|10h|



##### Function 

The CCR0 enables the MUB to control the Processor on the MUA-side. 

~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

||Instance|Register supported|Register not supported|
|---|---|---|---|
|MU_0.MUB||CCR0|—|
|MU_1.MUB||CCR0|—|
|MU_2.MUB||—|CCR0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1278 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Diagram 

|Bits<br>R|31|30<br>29|28|27|26|25|24<br>0|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|W||||||||||||||||
|Reset|0|0<br>0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14<br>13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||0|||||0||0|0|0|0|NMI|
|W||||||||||||||||
|Reset|0|0<br>0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Fields<br>|Field|Function||||||||||||||
||31-7<br>—<br>6-5<br>—<br>4<br>—<br>3<br>—<br>2<br>—<br>1<br>—<br>0<br>NMI|Reserved<br>Reserved<br>Reserved<br>Reserved<br>Reserved<br>Reserved<br>MUA Non-m<br>• When<br>• NMI bit<br>MUB c<br>• The NM<br>0b -<br>1b -|askab<br>NMI bit<br>is clea<br>an initi<br>I bit is<br>Non-m<br>Non-m|le Inter<br>is set t<br>red afte<br>ate anot<br>cleare<br>askabl<br>askabl|rupt Re<br>o "1", it<br>r the M<br>her no<br>d when<br>e interru<br>e interru|quest<br>initiates<br>UA_CS<br>n-maska<br>the MU<br>pt is no<br>pt is iss|a Non-M<br>SR0[NM<br>ble inter<br>resets.<br>t issued<br>ued to th|askab<br>IC] bit<br>rupt to<br>to the<br>e Pro|le Interr<br>is writte<br>the MU<br>Process<br>cessor A|upt to<br>n to "1<br>A.<br>or A b<br>by th|the Pro<br>". After<br>y the Pr<br>e Proce|cessor A.<br>the NMI b<br>ocessor B<br>ssor B.|it is c<br>.|leared,|the|



##### Fields 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1279 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

#### 39.6.2.7 Core Sticky Status Register 0 (CSSR0) 

##### Offset 

|Register|Offset|
|---|---|
|CSSR0|18h|



##### Function 

The CSSR0 register shows the status of interrupts pending (W1C). 

The reset value is chip-specific. 

~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

||Instance|Register supported|Register not supported|
|---|---|---|---|
|MU_0.MUB||CSSR0|—|
|MU_1.MUB||CSSR0|—|
|MU_2.MUB||—|CSSR0|



##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1280-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 0 0 0 0 0 0 NMIC<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 u<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-8<br>—|Reserved|
|7<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1280 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|6|Reserved|
|—||
|5|Reserved|
|—<br>4|Reserved|
|—<br>3|Reserved|
|—<br>2|Reserved|
|—||
|1|Reserved|
|—<br>0<br>NMIC|Processor B Non-Maskable-Interrupt Clear<br>• NMIC bit is used by the MUB-side Non-Maskable Interrupt service routine to clear the non-maskable<br>interrupt from MUA-side.<br>• Writing NMIC bit as "1" signals the MUA to clear the MUA_CCR0[NMI] bit, thus de-asserting the<br>interrupt and enabling the NMI bit to receive another interrupt.<br>• The NMIC bit is always read as "0", therefore NMIC bit cannot be polled. The NMIC bit can only<br>be used as part of the interrupt service routine, in which the NMIC bit should only be written as "1"<br>once.<br>• The NMIC bit is cleared when the MU resets.<br>0b - Default|
||1b - Writing "1" clears the MUA_CCR0[NMI] bit.|



#### 39.6.2.8 Flag Control Register (FCR) 

##### Offset 

|Register|Offset|
|---|---|
|FCR|100h|



##### Function 

The FCR register contains read-write flags that reflect the MUA_FSR[Fn] bits. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1281 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1282-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>F31  F30  F29  F28  F27  F26  F25  F24  F23  F22  F21  F20  F19  F18  F17  F16<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>F15  F14  F13  F12  F11  F10  F9  F8  F7  F6  F5  F4  F3  F2  F1  F0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function||
|---|---|---|
|31<br>F31|MUB to MUA Flag n<br>• n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br>• Fn bits are cleared when the MU resets.<br>• Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register.<br>• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register.<br>This field is not supported in every instance. The following table<br>supported registers.<br>~~NOTE~~|includes only|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>FCR|—|
||MU_1.MUB<br>FCR|—|
||MU_2.MUB<br>—|FCR|
||0b - Clears the Fn bit in the FSR register.<br>1b - Sets the Fn bit in the FSR register.||
|30<br>F30|MUB to MUA Flag n<br>• n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br>• Fn bits are cleared when the MU resets.<br>• Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register.<br>• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register.||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1282 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1283-03.png)


<!-- Start of picture text -->
Field Function<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB FCR —<br>MU_1.MUB FCR —<br>MU_2.MUB — FCR<br>0b - Clears the Fn bit in the FSR register.<br>1b - Sets the Fn bit in the FSR register.<br>29 MUB to MUA Flag n<br>F29 • n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br>• Fn bits are cleared when the MU resets.<br>• Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register.<br>• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB FCR —<br>MU_1.MUB FCR —<br>MU_2.MUB — FCR<br>0b - Clears the Fn bit in the FSR register.<br>1b - Sets the Fn bit in the FSR register.<br>28 MUB to MUA Flag n<br>F28 • n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1283 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

Field Function 

- Fn bits are cleared when the MU resets. 

- Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register. 

- Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|FCR|—|
|MU_1.MUB|FCR|—|
|MU_2.MUB|—|FCR|



0b - Clears the Fn bit in the FSR register. 1b - Sets the Fn bit in the FSR register. 27 MUB to MUA Flag n F27 • n = 0 to 31 

- Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits. 

- Fn bits are cleared when the MU resets. 

- Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register. 

• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register. ~~<mark>NOTE</mark>~~ This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|FCR|—|
|MU_1.MUB|FCR|—|
|MU_2.MUB|—|FCR|



0b - Clears the Fn bit in the FSR register. 

1b - Sets the Fn bit in the FSR register. 

26 MUB to MUA Flag n 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1284 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function||
|---|---|---|
|F26|• n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br>• Fn bits are cleared when the MU resets.<br>• Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register.<br>• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register.<br>This field is not supported in every instance. The following table<br>supported registers.<br>~~NOTE~~<br><br>|includes only<br>|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>FCR|—|
||MU_1.MUB<br>FCR|—|
||MU_2.MUB<br>—|FCR|
||0b - Clears the Fn bit in the FSR register.<br>1b - Sets the Fn bit in the FSR register.||
|25<br>F25|MUB to MUA Flag n<br>• n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br>• Fn bits are cleared when the MU resets.<br>• Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register.<br>• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register.<br>This field is not supported in every instance. The following table<br>supported registers.<br>~~NOTE~~|includes only|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>FCR|—|
||MU_1.MUB<br>FCR|—|
||MU_2.MUB<br>—|FCR|



0b - Clears the Fn bit in the FSR register. 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1285 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1286-03.png)


<!-- Start of picture text -->
Field Function<br>1b - Sets the Fn bit in the FSR register.<br>24 MUB to MUA Flag n<br>F24 • n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br>• Fn bits are cleared when the MU resets.<br>• Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register.<br>• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB FCR —<br>MU_1.MUB FCR —<br>MU_2.MUB — FCR<br>0b - Clears the Fn bit in the FSR register.<br>1b - Sets the Fn bit in the FSR register.<br>23 MUB to MUA Flag n<br>F23 • n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br>• Fn bits are cleared when the MU resets.<br>• Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register.<br>• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB FCR —<br>MU_1.MUB FCR —<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1286 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1287-03.png)


<!-- Start of picture text -->
Field Function<br>Instance Field supported in Field not supported in<br>MU_2.MUB — FCR<br>0b - Clears the Fn bit in the FSR register.<br>1b - Sets the Fn bit in the FSR register.<br>22 MUB to MUA Flag n<br>F22 • n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br>• Fn bits are cleared when the MU resets.<br>• Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register.<br>• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB FCR —<br>MU_1.MUB FCR —<br>MU_2.MUB — FCR<br>0b - Clears the Fn bit in the FSR register.<br>1b - Sets the Fn bit in the FSR register.<br>21 MUB to MUA Flag n<br>F21 • n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br>• Fn bits are cleared when the MU resets.<br>• Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register.<br>• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1287 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function||
|---|---|---|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>FCR|—|
||MU_1.MUB<br>FCR|—|
||MU_2.MUB<br>—|FCR|
||0b - Clears the Fn bit in the FSR register.<br>1b - Sets the Fn bit in the FSR register.||
|20<br>F20|MUB to MUA Flag n<br>• n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br>• Fn bits are cleared when the MU resets.<br>• Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register.<br>• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register.<br>This field is not supported in every instance. The following table<br>supported registers.<br>~~NOTE~~|includes only|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>FCR|—|
||MU_1.MUB<br>FCR|—|
||MU_2.MUB<br>—|FCR|
||0b - Clears the Fn bit in the FSR register.<br>1b - Sets the Fn bit in the FSR register.||
|19<br>F19|MUB to MUA Flag n<br>• n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br>• Fn bits are cleared when the MU resets.<br>• Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register.||
||• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register.||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1288 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1289-03.png)


<!-- Start of picture text -->
Field Function<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB FCR —<br>MU_1.MUB FCR —<br>MU_2.MUB — FCR<br>0b - Clears the Fn bit in the FSR register.<br>1b - Sets the Fn bit in the FSR register.<br>18 MUB to MUA Flag n<br>F18 • n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br>• Fn bits are cleared when the MU resets.<br>• Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register.<br>• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB FCR —<br>MU_1.MUB FCR —<br>MU_2.MUB — FCR<br>0b - Clears the Fn bit in the FSR register.<br>1b - Sets the Fn bit in the FSR register.<br>17 MUB to MUA Flag n<br>F17 • n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1289 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

Field Function 

- Fn bits are cleared when the MU resets. 

- Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register. 

- Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|FCR|—|
|MU_1.MUB|FCR|—|
|MU_2.MUB|—|FCR|



0b - Clears the Fn bit in the FSR register. 1b - Sets the Fn bit in the FSR register. 16 MUB to MUA Flag n F16 • n = 0 to 31 

- Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits. 

- Fn bits are cleared when the MU resets. 

- Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register. 

• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register. ~~<mark>NOTE</mark>~~ This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|FCR|—|
|MU_1.MUB|FCR|—|
|MU_2.MUB|—|FCR|



0b - Clears the Fn bit in the FSR register. 

1b - Sets the Fn bit in the FSR register. 

15 MUB to MUA Flag n 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1290 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function||
|---|---|---|
|F15|• n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br>• Fn bits are cleared when the MU resets.<br>• Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register.<br>• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register.<br>This field is not supported in every instance. The following table<br>supported registers.<br>~~NOTE~~<br><br>|includes only<br>|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>FCR|—|
||MU_1.MUB<br>FCR|—|
||MU_2.MUB<br>—|FCR|
||0b - Clears the Fn bit in the FSR register.<br>1b - Sets the Fn bit in the FSR register.||
|14<br>F14|MUB to MUA Flag n<br>• n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br>• Fn bits are cleared when the MU resets.<br>• Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register.<br>• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register.<br>This field is not supported in every instance. The following table<br>supported registers.<br>~~NOTE~~|includes only|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>FCR|—|
||MU_1.MUB<br>FCR|—|
||MU_2.MUB<br>—|FCR|



0b - Clears the Fn bit in the FSR register. 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1291 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1292-03.png)


<!-- Start of picture text -->
Field Function<br>1b - Sets the Fn bit in the FSR register.<br>13 MUB to MUA Flag n<br>F13 • n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br>• Fn bits are cleared when the MU resets.<br>• Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register.<br>• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB FCR —<br>MU_1.MUB FCR —<br>MU_2.MUB — FCR<br>0b - Clears the Fn bit in the FSR register.<br>1b - Sets the Fn bit in the FSR register.<br>12 MUB to MUA Flag n<br>F12 • n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br>• Fn bits are cleared when the MU resets.<br>• Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register.<br>• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB FCR —<br>MU_1.MUB FCR —<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1292 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1293-03.png)


<!-- Start of picture text -->
Field Function<br>Instance Field supported in Field not supported in<br>MU_2.MUB — FCR<br>0b - Clears the Fn bit in the FSR register.<br>1b - Sets the Fn bit in the FSR register.<br>11 MUB to MUA Flag n<br>F11 • n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br>• Fn bits are cleared when the MU resets.<br>• Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register.<br>• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB FCR —<br>MU_1.MUB FCR —<br>MU_2.MUB — FCR<br>0b - Clears the Fn bit in the FSR register.<br>1b - Sets the Fn bit in the FSR register.<br>10 MUB to MUA Flag n<br>F10 • n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br>• Fn bits are cleared when the MU resets.<br>• Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register.<br>• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1293 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function||
|---|---|---|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>FCR|—|
||MU_1.MUB<br>FCR|—|
||MU_2.MUB<br>—|FCR|
||0b - Clears the Fn bit in the FSR register.<br>1b - Sets the Fn bit in the FSR register.||
|9<br>F9|MUB to MUA Flag n<br>• n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br>• Fn bits are cleared when the MU resets.<br>• Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register.<br>• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register.<br>This field is not supported in every instance. The following table<br>supported registers.<br>~~NOTE~~|includes only|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>FCR|—|
||MU_1.MUB<br>FCR|—|
||MU_2.MUB<br>—|FCR|
||0b - Clears the Fn bit in the FSR register.<br>1b - Sets the Fn bit in the FSR register.||
|8<br>F8|MUB to MUA Flag n<br>• n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br>• Fn bits are cleared when the MU resets.<br>• Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register.||
||• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register.||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1294 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function<br>This field is not supported in every instance. The following table<br>supported registers.<br>~~NOTE~~<br><br>|includes only<br>|
|---|---|---|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>FCR|—|
||MU_1.MUB<br>FCR|—|
||MU_2.MUB<br>—|FCR|
||0b - Clears the Fn bit in the FSR register.<br>1b - Sets the Fn bit in the FSR register.||
|7<br>F7|MUB to MUA Flag n<br>• n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br>• Fn bits are cleared when the MU resets.<br>• Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register.<br>• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register.<br>This field is not supported in every instance. The following table<br>supported registers.<br>~~NOTE~~|includes only|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>FCR|—|
||MU_1.MUB<br>FCR|—|
||MU_2.MUB<br>—|FCR|
||0b - Clears the Fn bit in the FSR register.<br>1b - Sets the Fn bit in the FSR register.||
|6|MUB to MUA Flag n||
|F6|• n = 0 to 31||
||• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1295 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

Field Function 

- Fn bits are cleared when the MU resets. 

- Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register. 

- Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|FCR|—|
|MU_1.MUB|FCR|—|
|MU_2.MUB|—|FCR|



- 0b - Clears the Fn bit in the FSR register. 

1b - Sets the Fn bit in the FSR register. 

5 MUB to MUA Flag n 

- F5 • n = 0 to 31 

   - Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits. 

   - Fn bits are cleared when the MU resets. 

   - Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register. 

• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register. ~~<mark>NOTE</mark>~~ This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|FCR|—|
|MU_1.MUB|FCR|—|
|MU_2.MUB|—|FCR|



- 0b - Clears the Fn bit in the FSR register. 

1b - Sets the Fn bit in the FSR register. 

4 MUB to MUA Flag n 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1296 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function||
|---|---|---|
|F4|• n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br>• Fn bits are cleared when the MU resets.<br>• Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register.<br>• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register.<br>This field is not supported in every instance. The following table<br>supported registers.<br>~~NOTE~~<br><br>|includes only<br>|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>FCR|—|
||MU_1.MUB<br>FCR|—|
||MU_2.MUB<br>—|FCR|
||0b - Clears the Fn bit in the FSR register.<br>1b - Sets the Fn bit in the FSR register.||
|3<br>F3|MUB to MUA Flag n<br>• n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br>• Fn bits are cleared when the MU resets.<br>• Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register.<br>• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register.<br>This field is not supported in every instance. The following table<br>supported registers.<br>~~NOTE~~|includes only|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>FCR|—|
||MU_1.MUB<br>FCR|—|
||MU_2.MUB<br>—|FCR|



0b - Clears the Fn bit in the FSR register. 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1297 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - Sets the Fn bit in the FSR register.|
|2<br>F2|MUB to MUA Flag n<br>• n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br>• Fn bits are cleared when the MU resets.<br>• Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register.<br>• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register.<br>0b - Clears the Fn bit in the FSR register.<br>1b - Sets the Fn bit in the FSR register.|
|1<br>F1|MUB to MUA Flag n<br>• n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br>• Fn bits are cleared when the MU resets.<br>• Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register.<br>• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register.<br>0b - Clears the Fn bit in the FSR register.<br>1b - Sets the Fn bit in the FSR register.|
|0<br>F0|MUB to MUA Flag n<br>• n = 0 to 31<br>• Fn bit is a read-write flag that reflects the MUA_FSR[Fn] bits.<br>• Fn bits are cleared when the MU resets.<br>• Write 0 to an Fn bit - Clears the Fn bit in the MUA_FSR register.<br>• Write 1 to an Fn bit - Sets the Fn bit in the MUA_FSR register.<br>0b - Clears the Fn bit in the FSR register.<br>1b - Sets the Fn bit in the FSR register.|



#### 39.6.2.9 Flag Status Register (FSR) 

##### Offset 

|Register|Offset|
|---|---|
|FSR|104h|



##### Function 

The FSR register contains flags that reflect the values written to the Fn bit of the MUA_FCR register. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1298 / 4640 

NXP Semiconductors 

###### Messaging Unit (MU) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1299-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R F31  F30  F29  F28  F27  F26  F25  F24  F23  F22  F21  F20  F19  F18  F17  F16<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R F15  F14  F13  F12  F11  F10  F9  F8  F7  F6  F5  F4  F3  F2  F1  F0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

- Field Function 31 MUA to MUB Side Flag n 

- F31 • n = 0 to 31 • Fn bit is the MUB side flag that reflects the values written to the Fn bit in the MUA_FCR register. • Every time that the Fn bit in the MUA_FCR register is written, the Fn bit in the MUA FCR register write event updates the Fn bit in the MUB_FSR register after the event update latency. 

- • If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0. • If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

||Instance|Field supported in|Field not supported in|
|---|---|---|---|
||MU_0.MUB|FSR|—|
||MU_1.MUB|FSR|—|
||MU_2.MUB|—|FSR|
||0b - Fn bit in the MUA<br>1b - Fn bit in the MUA|FCR register is written 0.<br>FCR register is written 1.||
|30<br>F30|MUA to MUB Side Flag n<br>• n = 0 to 31<br>• Fn bit is the MUB side fla<br>• Every time that the Fn bit i<br>event updates the Fn bit i|g that reflects the values written to th<br>n the MUA_FCR register is written, t<br>n the MUB_FSR register after the ev|e Fn bit in the MUA_FCR register.<br>he Fn bit in the MUA FCR register write<br>ent update latency.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1299 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1300-03.png)


<!-- Start of picture text -->
Field Function<br>• If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0.<br>• If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB FSR —<br>MU_1.MUB FSR —<br>MU_2.MUB — FSR<br>0b - Fn bit in the MUA FCR register is written 0.<br>1b - Fn bit in the MUA FCR register is written 1.<br>29 MUA to MUB Side Flag n<br>F29 • n = 0 to 31<br>• Fn bit is the MUB side flag that reflects the values written to the Fn bit in the MUA_FCR register.<br>• Every time that the Fn bit in the MUA_FCR register is written, the Fn bit in the MUA FCR register write<br>event updates the Fn bit in the MUB_FSR register after the event update latency.<br>• If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0.<br>• If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB FSR —<br>MU_1.MUB FSR —<br>MU_2.MUB — FSR<br>0b - Fn bit in the MUA FCR register is written 0.<br>1b - Fn bit in the MUA FCR register is written 1.<br>28 MUA to MUB Side Flag n<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1300 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

- Field Function F28 • n = 0 to 31 • Fn bit is the MUB side flag that reflects the values written to the Fn bit in the MUA_FCR register. • Every time that the Fn bit in the MUA_FCR register is written, the Fn bit in the MUA FCR register write event updates the Fn bit in the MUB_FSR register after the event update latency. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1301-04.png)


<!-- Start of picture text -->
• n = 0 to 31<br>• Fn bit is the MUB side flag that reflects the values written to the Fn bit in the MUA_FCR register.<br>• Every time that the Fn bit in the MUA_FCR register is written, the Fn bit in the MUA FCR register write<br>event updates the Fn bit in the MUB_FSR register after the event update latency.<br>• If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0.<br>• If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB FSR —<br>MU_1.MUB FSR —<br>MU_2.MUB — FSR<br>0b - Fn bit in the MUA FCR register is written 0.<br>1b - Fn bit in the MUA FCR register is written 1.<br>MUA to MUB Side Flag n<br>• n = 0 to 31<br>• Fn bit is the MUB side flag that reflects the values written to the Fn bit in the MUA_FCR register.<br>• Every time that the Fn bit in the MUA_FCR register is written, the Fn bit in the MUA FCR register write<br>event updates the Fn bit in the MUB_FSR register after the event update latency.<br>• If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0.<br>• If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB FSR —<br>MU_1.MUB FSR —<br>MU_2.MUB — FSR<br><!-- End of picture text -->

- 0b - Fn bit in the MUA FCR register is written 0. 1b - Fn bit in the MUA FCR register is written 1. 

- 27 MUA to MUB Side Flag n 

- F27 • n = 0 to 31 • Fn bit is the MUB side flag that reflects the values written to the Fn bit in the MUA_FCR register. • Every time that the Fn bit in the MUA_FCR register is written, the Fn bit in the MUA FCR register write event updates the Fn bit in the MUB_FSR register after the event update latency. 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1301 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

Field Function 0b - Fn bit in the MUA FCR register is written 0. 1b - Fn bit in the MUA FCR register is written 1. 26 MUA to MUB Side Flag n F26 • n = 0 to 31 

- Fn bit is the MUB side flag that reflects the values written to the Fn bit in the MUA_FCR register. 

- Every time that the Fn bit in the MUA_FCR register is written, the Fn bit in the MUA FCR register write event updates the Fn bit in the MUB_FSR register after the event update latency. 

- If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0. 

- If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|FSR|—|
|MU_1.MUB|FSR|—|
|MU_2.MUB|—|FSR|



0b - Fn bit in the MUA FCR register is written 0. 1b - Fn bit in the MUA FCR register is written 1. 25 MUA to MUB Side Flag n 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1302-12.png)


<!-- Start of picture text -->
MUA to MUB Side Flag n<br>• n = 0 to 31<br>• Fn bit is the MUB side flag that reflects the values written to the Fn bit in the MUA_FCR register.<br>• Every time that the Fn bit in the MUA_FCR register is written, the Fn bit in the MUA FCR register write<br>event updates the Fn bit in the MUB_FSR register after the event update latency.<br>• If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0.<br>• If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB FSR —<br><!-- End of picture text -->

- F25 • n = 0 to 31 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1302 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function||
|---|---|---|
||Instance<br>Field supported in|Field not supported in|
||MU_1.MUB<br>FSR|—|
||MU_2.MUB<br>—|FSR|
||0b - Fn bit in the MUA FCR register is written 0.<br>1b - Fn bit in the MUA FCR register is written 1.||
|24<br>F24|MUA to MUB Side Flag n<br>• n = 0 to 31<br>• Fn bit is the MUB side flag that reflects the values written to th<br>• Every time that the Fn bit in the MUA_FCR register is written, t<br>event updates the Fn bit in the MUB_FSR register after the ev<br>• If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0.<br>• If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1.<br>This field is not supported in every instance. The following ta<br>supported registers.<br>~~NOTE~~|e Fn bit in the MUA_FCR register.<br>he Fn bit in the MUA FCR register write<br>ent update latency.<br>ble includes only|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>FSR|—|
||MU_1.MUB<br>FSR|—|
||MU_2.MUB<br>—|FSR|
||0b - Fn bit in the MUA FCR register is written 0.<br>1b - Fn bit in the MUA FCR register is written 1.||
|23<br>F23|MUA to MUB Side Flag n<br>• n = 0 to 31<br>• Fn bit is the MUB side flag that reflects the values written to th<br>• Every time that the Fn bit in the MUA_FCR register is written, t<br>event updates the Fn bit in the MUB_FSR register after the ev<br>• If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0.<br>• If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1.|e Fn bit in the MUA_FCR register.<br>he Fn bit in the MUA FCR register write<br>ent update latency.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1303 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1304-03.png)


<!-- Start of picture text -->
Field Function<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB FSR —<br>MU_1.MUB FSR —<br>MU_2.MUB — FSR<br>0b - Fn bit in the MUA FCR register is written 0.<br>1b - Fn bit in the MUA FCR register is written 1.<br>22 MUA to MUB Side Flag n<br>F22 • n = 0 to 31<br>• Fn bit is the MUB side flag that reflects the values written to the Fn bit in the MUA_FCR register.<br>• Every time that the Fn bit in the MUA_FCR register is written, the Fn bit in the MUA FCR register write<br>event updates the Fn bit in the MUB_FSR register after the event update latency.<br>• If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0.<br>• If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB FSR —<br>MU_1.MUB FSR —<br>MU_2.MUB — FSR<br>0b - Fn bit in the MUA FCR register is written 0.<br>1b - Fn bit in the MUA FCR register is written 1.<br>21 MUA to MUB Side Flag n<br>F21 • n = 0 to 31<br>• Fn bit is the MUB side flag that reflects the values written to the Fn bit in the MUA_FCR register.<br><!-- End of picture text -->

||Instance<br>Field supported in|Field not supported in|
|---|---|---|
||MU_0.MUB<br>FSR|—|
||MU_1.MUB<br>FSR|—|
||MU_2.MUB<br>—|FSR|
||0b - Fn bit in the MUA FCR register is written 0.<br>1b - Fn bit in the MUA FCR register is written 1.||
|21|MUA to MUB Side Flag n||
|F21|• n = 0 to 31<br>• Fn bit is the MUB side flag that reflects the values written to th<br>Table continues on the next page...|e Fn bit in the MUA_FCR register.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1304 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

- Field Function • Every time that the Fn bit in the MUA_FCR register is written, the Fn bit in the MUA FCR register write event updates the Fn bit in the MUB_FSR register after the event update latency. 

   - If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0. 

   - If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|FSR|—|
|MU_1.MUB|FSR|—|
|MU_2.MUB|—|FSR|



- 0b - Fn bit in the MUA FCR register is written 0. 

1b - Fn bit in the MUA FCR register is written 1. 

20 

F20 

MUA to MUB Side Flag n 

- n = 0 to 31 

- Fn bit is the MUB side flag that reflects the values written to the Fn bit in the MUA_FCR register. 

- Every time that the Fn bit in the MUA_FCR register is written, the Fn bit in the MUA FCR register write event updates the Fn bit in the MUB_FSR register after the event update latency. 

- If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0. 

- If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|FSR|—|
|MU_1.MUB|FSR|—|
|MU_2.MUB|—|FSR|



0b - Fn bit in the MUA FCR register is written 0. 

1b - Fn bit in the MUA FCR register is written 1. 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1305 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

Field Function 19 MUA to MUB Side Flag n F19 • n = 0 to 31 

- Fn bit is the MUB side flag that reflects the values written to the Fn bit in the MUA_FCR register. 

- Every time that the Fn bit in the MUA_FCR register is written, the Fn bit in the MUA FCR register write event updates the Fn bit in the MUB_FSR register after the event update latency. 

- If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0. 

- If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|FSR|—|
|MU_1.MUB|FSR|—|
|MU_2.MUB|—|FSR|



- 0b - Fn bit in the MUA FCR register is written 0. 

1b - Fn bit in the MUA FCR register is written 1. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1306-13.png)


<!-- Start of picture text -->
MUA to MUB Side Flag n<br>• n = 0 to 31<br>• Fn bit is the MUB side flag that reflects the values written to the Fn bit in the MUA_FCR register.<br>• Every time that the Fn bit in the MUA_FCR register is written, the Fn bit in the MUA FCR register write<br>event updates the Fn bit in the MUB_FSR register after the event update latency.<br>• If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0.<br>• If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB FSR —<br>MU_1.MUB FSR —<br><!-- End of picture text -->

18 MUA to MUB Side Flag n 

- F18 • n = 0 to 31 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1306 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1307-03.png)


<!-- Start of picture text -->
Field Function<br>Instance Field supported in Field not supported in<br>MU_2.MUB — FSR<br>0b - Fn bit in the MUA FCR register is written 0.<br>1b - Fn bit in the MUA FCR register is written 1.<br>17 MUA to MUB Side Flag n<br>F17 • n = 0 to 31<br>• Fn bit is the MUB side flag that reflects the values written to the Fn bit in the MUA_FCR register.<br>• Every time that the Fn bit in the MUA_FCR register is written, the Fn bit in the MUA FCR register write<br>event updates the Fn bit in the MUB_FSR register after the event update latency.<br>• If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0.<br>• If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB FSR —<br>MU_1.MUB FSR —<br>MU_2.MUB — FSR<br>0b - Fn bit in the MUA FCR register is written 0.<br>1b - Fn bit in the MUA FCR register is written 1.<br>16 MUA to MUB Side Flag n<br>F16 • n = 0 to 31<br>• Fn bit is the MUB side flag that reflects the values written to the Fn bit in the MUA_FCR register.<br>• Every time that the Fn bit in the MUA_FCR register is written, the Fn bit in the MUA FCR register write<br>event updates the Fn bit in the MUB_FSR register after the event update latency.<br>• If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0.<br>• If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br><!-- End of picture text -->

##### Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1307 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function||
|---|---|---|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>FSR|—|
||MU_1.MUB<br>FSR|—|
||MU_2.MUB<br>—|FSR|
||0b - Fn bit in the MUA FCR register is written 0.<br>1b - Fn bit in the MUA FCR register is written 1.||
|15<br>F15|MUA to MUB Side Flag n<br>• n = 0 to 31<br>• Fn bit is the MUB side flag that reflects the values written to th<br>• Every time that the Fn bit in the MUA_FCR register is written, t<br>event updates the Fn bit in the MUB_FSR register after the ev<br>• If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0.<br>• If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1.<br>This field is not supported in every instance. The following ta<br>supported registers.<br>~~NOTE~~|e Fn bit in the MUA_FCR register.<br>he Fn bit in the MUA FCR register write<br>ent update latency.<br>ble includes only|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>FSR|—|
||MU_1.MUB<br>FSR|—|
||MU_2.MUB<br>—|FSR|
||0b - Fn bit in the MUA FCR register is written 0.<br>1b - Fn bit in the MUA FCR register is written 1.||
|14<br>F14|MUA to MUB Side Flag n<br>• n = 0 to 31<br>• Fn bit is the MUB side flag that reflects the values written to th<br>• Every time that the Fn bit in the MUA_FCR register is written, t<br>event updates the Fn bit in the MUB_FSR register after the ev<br>• If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0.|e Fn bit in the MUA_FCR register.<br>he Fn bit in the MUA FCR register write<br>ent update latency.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1308 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1309-03.png)


<!-- Start of picture text -->
Field Function<br>• If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB FSR —<br>MU_1.MUB FSR —<br>MU_2.MUB — FSR<br>0b - Fn bit in the MUA FCR register is written 0.<br>1b - Fn bit in the MUA FCR register is written 1.<br>13 MUA to MUB Side Flag n<br>F13 • n = 0 to 31<br>• Fn bit is the MUB side flag that reflects the values written to the Fn bit in the MUA_FCR register.<br>• Every time that the Fn bit in the MUA_FCR register is written, the Fn bit in the MUA FCR register write<br>event updates the Fn bit in the MUB_FSR register after the event update latency.<br>• If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0.<br>• If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB FSR —<br>MU_1.MUB FSR —<br>MU_2.MUB — FSR<br>0b - Fn bit in the MUA FCR register is written 0.<br>1b - Fn bit in the MUA FCR register is written 1.<br>12 MUA to MUB Side Flag n<br>F12 • n = 0 to 31<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1309 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

##### Field 

##### Function 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1310-05.png)


<!-- Start of picture text -->
• Fn bit is the MUB side flag that reflects the values written to the Fn bit in the MUA_FCR register.<br>• Every time that the Fn bit in the MUA_FCR register is written, the Fn bit in the MUA FCR register write<br>event updates the Fn bit in the MUB_FSR register after the event update latency.<br>• If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0.<br>• If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB FSR —<br>MU_1.MUB FSR —<br>MU_2.MUB — FSR<br>0b - Fn bit in the MUA FCR register is written 0.<br>1b - Fn bit in the MUA FCR register is written 1.<br>11 MUA to MUB Side Flag n<br>F11 • n = 0 to 31<br>• Fn bit is the MUB side flag that reflects the values written to the Fn bit in the MUA_FCR register.<br>• Every time that the Fn bit in the MUA_FCR register is written, the Fn bit in the MUA FCR register write<br>event updates the Fn bit in the MUB_FSR register after the event update latency.<br>• If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0.<br>• If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB FSR —<br>MU_1.MUB FSR —<br>MU_2.MUB — FSR<br>0b - Fn bit in the MUA FCR register is written 0.<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1310 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1311-03.png)


<!-- Start of picture text -->
Field Function<br>1b - Fn bit in the MUA FCR register is written 1.<br>10 MUA to MUB Side Flag n<br>F10 • n = 0 to 31<br>• Fn bit is the MUB side flag that reflects the values written to the Fn bit in the MUA_FCR register.<br>• Every time that the Fn bit in the MUA_FCR register is written, the Fn bit in the MUA FCR register write<br>event updates the Fn bit in the MUB_FSR register after the event update latency.<br>• If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0.<br>• If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB FSR —<br>MU_1.MUB FSR —<br>MU_2.MUB — FSR<br>0b - Fn bit in the MUA FCR register is written 0.<br>1b - Fn bit in the MUA FCR register is written 1.<br>9 MUA to MUB Side Flag n<br>F9 • n = 0 to 31<br>• Fn bit is the MUB side flag that reflects the values written to the Fn bit in the MUA_FCR register.<br>• Every time that the Fn bit in the MUA_FCR register is written, the Fn bit in the MUA FCR register write<br>event updates the Fn bit in the MUB_FSR register after the event update latency.<br>• If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0.<br>• If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB FSR —<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1311-04.png)


<!-- Start of picture text -->
Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1311 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function||
|---|---|---|
||Instance<br>Field supported in|Field not supported in|
||MU_1.MUB<br>FSR|—|
||MU_2.MUB<br>—|FSR|
||0b - Fn bit in the MUA FCR register is written 0.<br>1b - Fn bit in the MUA FCR register is written 1.||
|8<br>F8|MUA to MUB Side Flag n<br>• n = 0 to 31<br>• Fn bit is the MUB side flag that reflects the values written to th<br>• Every time that the Fn bit in the MUA_FCR register is written, t<br>event updates the Fn bit in the MUB_FSR register after the ev<br>• If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0.<br>• If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1.<br>This field is not supported in every instance. The following ta<br>supported registers.<br>~~NOTE~~|e Fn bit in the MUA_FCR register.<br>he Fn bit in the MUA FCR register write<br>ent update latency.<br>ble includes only|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>FSR|—|
||MU_1.MUB<br>FSR|—|
||MU_2.MUB<br>—|FSR|
||0b - Fn bit in the MUA FCR register is written 0.<br>1b - Fn bit in the MUA FCR register is written 1.||
|7<br>F7|MUA to MUB Side Flag n<br>• n = 0 to 31<br>• Fn bit is the MUB side flag that reflects the values written to th<br>• Every time that the Fn bit in the MUA_FCR register is written, t<br>event updates the Fn bit in the MUB_FSR register after the ev<br>• If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0.<br>• If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1.|e Fn bit in the MUA_FCR register.<br>he Fn bit in the MUA FCR register write<br>ent update latency.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1312 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function||||
|---|---|---|---|---|
|||This field is not suppor<br>supported registers.|ted in every instance. The following ta<br>~~NOTE~~|ble includes only|
|||Instance|Field supported in|Field not supported in|
||MU_0.MUB||FSR|—|
||MU_1.MUB||FSR|—|
||MU_2.MUB||—|FSR|



- 0b - Fn bit in the MUA FCR register is written 0. 1b - Fn bit in the MUA FCR register is written 1. 

- 6 MUA to MUB Side Flag n 

- F6 • n = 0 to 31 • Fn bit is the MUB side flag that reflects the values written to the Fn bit in the MUA_FCR register. • Every time that the Fn bit in the MUA_FCR register is written, the Fn bit in the MUA FCR register write event updates the Fn bit in the MUB_FSR register after the event update latency. 

- • If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0. 

• If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1. ~~<mark>NOTE</mark>~~ This field is not supported in every instance. The following table includes only supported registers. 

||Instance<br>Field supported in|Field not supported in|
|---|---|---|
||MU_0.MUB<br>FSR|—|
||MU_1.MUB<br>FSR|—|
||MU_2.MUB<br>—|FSR|
||0b - Fn bit in the MUA FCR register is written 0.<br>1b - Fn bit in the MUA FCR register is written 1.||
|5|MUA to MUB Side Flag n||
|F5|• n = 0 to 31<br>• Fn bit is the MUB side flag that reflects the values written to th|e Fn bit in the MUA_FCR register.|
||Table continues on the next page...||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1313 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

- Field Function • Every time that the Fn bit in the MUA_FCR register is written, the Fn bit in the MUA FCR register write event updates the Fn bit in the MUB_FSR register after the event update latency. 

   - If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0. 

   - If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|FSR|—|
|MU_1.MUB|FSR|—|
|MU_2.MUB|—|FSR|



- 0b - Fn bit in the MUA FCR register is written 0. 

1b - Fn bit in the MUA FCR register is written 1. 

4 

F4 

MUA to MUB Side Flag n 

- n = 0 to 31 

- Fn bit is the MUB side flag that reflects the values written to the Fn bit in the MUA_FCR register. 

- Every time that the Fn bit in the MUA_FCR register is written, the Fn bit in the MUA FCR register write event updates the Fn bit in the MUB_FSR register after the event update latency. 

- If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0. 

- If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|FSR|—|
|MU_1.MUB|FSR|—|
|MU_2.MUB|—|FSR|



0b - Fn bit in the MUA FCR register is written 0. 

1b - Fn bit in the MUA FCR register is written 1. 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1314 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|3|MUA to MUB Side Flag n|
|F3|• n = 0 to 31<br>• Fn bit is the MUB side flag that reflects the values written to the Fn bit in the MUA_FCR register.<br>• Every time that the Fn bit in the MUA_FCR register is written, the Fn bit in the MUA FCR register write<br>event updates the Fn bit in the MUB_FSR register after the event update latency.<br>• If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0.<br>• If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1.<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>~~NOTE~~|
||Instance<br>Field supported in<br>Field not supported in|
||MU_0.MUB<br>FSR<br>—|
||MU_1.MUB<br>FSR<br>—|
||MU_2.MUB<br>—<br>FSR|
||0b - Fn bit in the MUA FCR register is written 0.<br>1b - Fn bit in the MUA FCR register is written 1.|
|2<br>F2|MUA to MUB Side Flag n<br>• n = 0 to 31<br>• Fn bit is the MUB side flag that reflects the values written to the Fn bit in the MUA_FCR register.<br>• Every time that the Fn bit in the MUA_FCR register is written, the Fn bit in the MUA FCR register write<br>event updates the Fn bit in the MUB_FSR register after the event update latency.<br>• If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0.<br>• If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1.<br>0b - Fn bit in the MUA FCR register is written 0.<br>1b - Fn bit in the MUA FCR register is written 1.|
|1<br>F1|MUA to MUB Side Flag n<br>• n = 0 to 31<br>• Fn bit is the MUB side flag that reflects the values written to the Fn bit in the MUA_FCR register.<br>• Every time that the Fn bit in the MUA_FCR register is written, the Fn bit in the MUA FCR register write<br>event updates the Fn bit in the MUB_FSR register after the event update latency.<br>• If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1315 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||• If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1.<br>0b - Fn bit in the MUA FCR register is written 0.<br>1b - Fn bit in the MUA FCR register is written 1.|
|0|MUA to MUB Side Flag n|
|F0|• n = 0 to 31<br>• Fn bit is the MUB side flag that reflects the values written to the Fn bit in the MUA_FCR register.<br>• Every time that the Fn bit in the MUA_FCR register is written, the Fn bit in the MUA FCR register write<br>event updates the Fn bit in the MUB_FSR register after the event update latency.<br>• If a 0 is read from an Fn bit - Fn bit in the MUA_FCR is 0.<br>• If a 1 is read from an Fn bit - Fn bit in the MUA_FCR is 1.<br>0b - Fn bit in the MUA FCR register is written 0.<br>1b - Fn bit in the MUA FCR register is written 1.|



#### 39.6.2.10 General Interrupt Enable Register (GIER) 

##### Offset 

|Register|Offset|
|---|---|
|GIER|110h|



##### Function 

The GIER register contains the MUB general purpose interrupt enables. 

##### Diagram 

|Bits<br>R<br>W|31<br>GIE31|30<br>GIE30|29<br>GIE29|28<br>GIE28|27<br>GIE27|26<br>GIE26|25<br>GIE25|24<br>GIE24|23<br>GIE23|22<br>GIE22|21<br>GIE21|20<br>GIE20|19<br>GIE19|18<br>GIE18|17<br>GIE17|16<br>GIE16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|GIE15|GIE14|GIE13|GIE12|GIE11|GIE10|GIE9|GIE8|GIE7|GIE6|GIE5|GIE4|GIE3|GIE2|GIE1|GIE0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1316 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Fields 

|Field|Function|
|---|---|
|31|MUB General Purpose Interrupt Enable n|
|GIE31|• There are 32 General Purpose Interrupts (n = 0 to 31)|
||• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".|



- If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued. 

- GIEn bit is cleared when the MU resets. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|GIER|—|
|MU_1.MUB|GIER|—|
|MU_2.MUB|—|GIER|



- 0b - Disables MUB General Interrupt n. 

- 1b - Enables MUB General Interrupt n. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1317 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

- Field Function 30 MUB General Purpose Interrupt Enable n 

- GIE30 • There are 32 General Purpose Interrupts (n = 0 to 31) • If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit in the MUB GSR register is set to "1". 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1318-04.png)


<!-- Start of picture text -->
30 MUB General Purpose Interrupt Enable n<br>GIE30 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>29 MUB General Purpose Interrupt Enable n<br>GIE29 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1318 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1319-03.png)


<!-- Start of picture text -->
Field Function<br>1b - Enables MUB General Interrupt n.<br>28 MUB General Purpose Interrupt Enable n<br>GIE28 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>27 MUB General Purpose Interrupt Enable n<br>GIE27 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1319 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1320-03.png)


<!-- Start of picture text -->
Field Function<br>Instance Field supported in Field not supported in<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>26 MUB General Purpose Interrupt Enable n<br>GIE26 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>25 MUB General Purpose Interrupt Enable n<br>GIE25 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1320-04.png)


<!-- Start of picture text -->
26 MUB General Purpose Interrupt Enable n<br>GIE26 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>25 MUB General Purpose Interrupt Enable n<br>GIE25 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1320 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1321-03.png)


<!-- Start of picture text -->
Field Function<br>Instance Field supported in Field not supported in<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>24 MUB General Purpose Interrupt Enable n<br>GIE24 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>23 MUB General Purpose Interrupt Enable n<br>GIE23 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br><!-- End of picture text -->

##### Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1321 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1322-03.png)


<!-- Start of picture text -->
Field Function<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>22 MUB General Purpose Interrupt Enable n<br>GIE22 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>21 MUB General Purpose Interrupt Enable n<br>GIE21 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1322 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1323-03.png)


<!-- Start of picture text -->
Field Function<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>20 MUB General Purpose Interrupt Enable n<br>GIE20 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>19 MUB General Purpose Interrupt Enable n<br>GIE19 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1323 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1324-03.png)


<!-- Start of picture text -->
Field Function<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>18 MUB General Purpose Interrupt Enable n<br>GIE18 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>17 MUB General Purpose Interrupt Enable n<br>GIE17 • There are 32 General Purpose Interrupts (n = 0 to 31)<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1324-04.png)


<!-- Start of picture text -->
18 MUB General Purpose Interrupt Enable n<br>GIE18 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>17 MUB General Purpose Interrupt Enable n<br>GIE17 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1324 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

- Field Function • If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit in the MUB GSR register is set to "1". 

|• If GIEn<br>• GIEn b|is cleared, then the va<br>it is cleared when the|lue of the GIPn bit is ignored and n<br>MU resets.|o General Interrupt n request is issued.|
|---|---|---|---|
||This field is not suppor<br>supported registers.|ted in every instance. The following ta<br>~~NOTE~~|ble includes only|
||Instance|Field supported in|Field not supported in|
|MU_0.MUB||GIER|—|
|MU_1.MUB||GIER|—|
|MU_2.MUB||—|GIER|



0b - Disables MUB General Interrupt n. 1b - Enables MUB General Interrupt n. 16 MUB General Purpose Interrupt Enable n GIE16 • There are 32 General Purpose Interrupts (n = 0 to 31) 

- If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit in the MUB GSR register is set to "1". 

- If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued. 

- GIEn bit is cleared when the MU resets. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

||Instance<br>Field supported in|Field not supported in|
|---|---|---|
||MU_0.MUB<br>GIER|—|
||MU_1.MUB<br>GIER|—|
||MU_2.MUB<br>—|GIER|
||0b - Disables MUB General Interrupt n.||
||1b - Enables MUB General Interrupt n.||
|15|MUB General Purpose Interrupt Enable n||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1325 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

- Field Function 

- GIE15 • There are 32 General Purpose Interrupts (n = 0 to 31) • If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit in the MUB GSR register is set to "1". 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1326-04.png)


<!-- Start of picture text -->
• There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>MUB General Purpose Interrupt Enable n<br>• There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br><!-- End of picture text -->

0b - Disables MUB General Interrupt n. 1b - Enables MUB General Interrupt n. 14 MUB General Purpose Interrupt Enable n GIE14 • There are 32 General Purpose Interrupts (n = 0 to 31) • If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit in the MUB GSR register is set to "1". 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1326 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

- Field Function 13 MUB General Purpose Interrupt Enable n 

- GIE13 • There are 32 General Purpose Interrupts (n = 0 to 31) • If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit in the MUB GSR register is set to "1". 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1327-04.png)


<!-- Start of picture text -->
MUB General Purpose Interrupt Enable n<br>• There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>MUB General Purpose Interrupt Enable n<br>• There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br><!-- End of picture text -->

- 0b - Disables MUB General Interrupt n. 1b - Enables MUB General Interrupt n. 

- 12 MUB General Purpose Interrupt Enable n 

- GIE12 • There are 32 General Purpose Interrupts (n = 0 to 31) • If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit in the MUB GSR register is set to "1". 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1327 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1328-03.png)


<!-- Start of picture text -->
Field Function<br>1b - Enables MUB General Interrupt n.<br>11 MUB General Purpose Interrupt Enable n<br>GIE11 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>10 MUB General Purpose Interrupt Enable n<br>GIE10 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1328 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1329-03.png)


<!-- Start of picture text -->
Field Function<br>Instance Field supported in Field not supported in<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>9 MUB General Purpose Interrupt Enable n<br>GIE9 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>8 MUB General Purpose Interrupt Enable n<br>GIE8 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1329-04.png)


<!-- Start of picture text -->
9 MUB General Purpose Interrupt Enable n<br>GIE9 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>8 MUB General Purpose Interrupt Enable n<br>GIE8 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1329 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1330-03.png)


<!-- Start of picture text -->
Field Function<br>Instance Field supported in Field not supported in<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>7 MUB General Purpose Interrupt Enable n<br>GIE7 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>6 MUB General Purpose Interrupt Enable n<br>GIE6 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br><!-- End of picture text -->

##### Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1330 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1331-03.png)


<!-- Start of picture text -->
Field Function<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>5 MUB General Purpose Interrupt Enable n<br>GIE5 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>4 MUB General Purpose Interrupt Enable n<br>GIE4 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1331 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1332-03.png)


<!-- Start of picture text -->
Field Function<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>3 MUB General Purpose Interrupt Enable n<br>GIE3 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>2 MUB General Purpose Interrupt Enable n<br>GIE2 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1332 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1333-03.png)


<!-- Start of picture text -->
Field Function<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>1 MUB General Purpose Interrupt Enable n<br>GIE1 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".<br>• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.<br>• GIEn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GIER —<br>MU_1.MUB GIER —<br>MU_2.MUB — GIER<br>0b - Disables MUB General Interrupt n.<br>1b - Enables MUB General Interrupt n.<br>0 MUB General Purpose Interrupt Enable n<br>GIE0 • There are 32 General Purpose Interrupts (n = 0 to 31)<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1333 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||• If a GIEn bit is set to "1", then a General Interrupt n request is issued to Processor B when the GIPn bit<br>in the MUB GSR register is set to "1".|
||• If GIEn is cleared, then the value of the GIPn bit is ignored and no General Interrupt n request is issued.|
||• GIEn bit is cleared when the MU resets.|
||0b - Disables MUB General Interrupt n.|
||1b - Enables MUB General Interrupt n.|



#### 39.6.2.11 General Control Register (GCR) 

##### Offset 

|Register|Offset|
|---|---|
|GCR|114h|



##### Function 

The GCR register contains the MUB general purpose interrupt requests. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1334-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>GIR31  GIR30  GIR29  GIR28  GIR27  GIR26  GIR25  GIR24  GIR23  GIR22  GIR21  GIR20  GIR19  GIR18  GIR17  GIR16<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>GIR15  GIR14  GIR13  GIR12  GIR11  GIR10  GIR9  GIR8  GIR7  GIR6  GIR5  GIR4  GIR3  GIR2  GIR1  GIR0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|MUB General Purpose Interrupt Request n|
|GIR31|• There are 32 General Purpose Interrupts (n = 0 to 31)|
||• Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the MUA-side. If the MUA_GIER[GIEn]<br>bit is set to "1" on the MUA-side, a General Purpose Interrupt n request is triggered to Processor A.|
||• The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by writing "1", thereby signalling the<br>MUB that the interrupt was accepted (cleared by the software).|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1334 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1335-03.png)


<!-- Start of picture text -->
Field Function<br>• Writing "0" to the GIRn bit is ignored.<br>• To ensure proper operations, you must verify that the GIRn bit is cleared (meaning that there is no<br>pending interrupt) before setting it (GIRn bit).<br>• GIRn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GCR —<br>MU_1.MUB GCR —<br>MU_2.MUB — GCR<br>0b - MUB General Interrupt n is not requested to the MUA.<br>1b - MUB General Interrupt n is requested to the MUA.<br>30 MUB General Purpose Interrupt Request n<br>GIR30 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the MUA-side. If the MUA_GIER[GIEn]<br>bit is set to "1" on the MUA-side, a General Purpose Interrupt n request is triggered to Processor A.<br>• The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by writing "1", thereby signalling the<br>MUB that the interrupt was accepted (cleared by the software).<br>• Writing "0" to the GIRn bit is ignored.<br>• To ensure proper operations, you must verify that the GIRn bit is cleared (meaning that there is no<br>pending interrupt) before setting it (GIRn bit).<br>• GIRn bit is cleared when the MU resets.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GCR —<br>MU_1.MUB GCR —<br>MU_2.MUB — GCR<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1335 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function||
|---|---|---|
||Instance<br>Field supported in|Field not supported in|
||0b - MUB General Interrupt n is not requested to the MUA.<br>1b - MUB General Interrupt n is requested to the MUA.||
|29<br>GIR29|MUB General Purpose Interrupt Request n<br>• There are 32 General Purpose Interrupts (n = 0 to 31)<br>• Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the M<br>bit is set to "1" on the MUA-side, a General Purpose Interrupt n r<br>• The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by w<br>MUB that the interrupt was accepted (cleared by the software).<br>• Writing "0" to the GIRn bit is ignored.<br>• To ensure proper operations, you must verify that the GIRn bit is<br>pending interrupt) before setting it (GIRn bit).<br>• GIRn bit is cleared when the MU resets.<br>This field is not supported in every instance. The following table<br>supported registers.<br>~~NOTE~~|UA-side. If the MUA_GIER[GIEn]<br>equest is triggered to Processor A.<br>riting "1", thereby signalling the<br>cleared (meaning that there is no<br>includes only|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>GCR|—|
||MU_1.MUB<br>GCR|—|
||MU_2.MUB<br>—|GCR|
||0b - MUB General Interrupt n is not requested to the MUA.<br>1b - MUB General Interrupt n is requested to the MUA.||
|28<br>GIR28|MUB General Purpose Interrupt Request n<br>• There are 32 General Purpose Interrupts (n = 0 to 31)<br>• Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the M<br>bit is set to "1" on the MUA-side, a General Purpose Interrupt n r<br>• The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by w<br>MUB that the interrupt was accepted (cleared by the software).<br>• Writing "0" to the GIRn bit is ignored.<br>• To ensure proper operations, you must verify that the GIRn bit is<br>pending interrupt) before setting it (GIRn bit).|UA-side. If the MUA_GIER[GIEn]<br>equest is triggered to Processor A.<br>riting "1", thereby signalling the<br>cleared (meaning that there is no|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1336 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function<br>• GIRn bit is cleared when the MU resets.<br>This field is not supported in every instance. The following table<br>supported registers.<br>~~NOTE~~|includes only|
|---|---|---|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>GCR|—|
||MU_1.MUB<br>GCR|—|
||MU_2.MUB<br>—|GCR|
||0b - MUB General Interrupt n is not requested to the MUA.<br>1b - MUB General Interrupt n is requested to the MUA.||
|27<br>GIR27|MUB General Purpose Interrupt Request n<br>• There are 32 General Purpose Interrupts (n = 0 to 31)<br>• Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the M<br>bit is set to "1" on the MUA-side, a General Purpose Interrupt n r<br>• The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by w<br>MUB that the interrupt was accepted (cleared by the software).<br>• Writing "0" to the GIRn bit is ignored.<br>• To ensure proper operations, you must verify that the GIRn bit is<br>pending interrupt) before setting it (GIRn bit).<br>• GIRn bit is cleared when the MU resets.<br>This field is not supported in every instance. The following table<br>supported registers.<br>~~NOTE~~|UA-side. If the MUA_GIER[GIEn]<br>equest is triggered to Processor A.<br>riting "1", thereby signalling the<br>cleared (meaning that there is no<br>includes only|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>GCR|—|
||MU_1.MUB<br>GCR|—|
||MU_2.MUB<br>—|GCR|



- 0b - MUB General Interrupt n is not requested to the MUA. 

1b - MUB General Interrupt n is requested to the MUA. 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1337 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

- Field Function 26 MUB General Purpose Interrupt Request n 

- GIR26 • There are 32 General Purpose Interrupts (n = 0 to 31) • Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the MUA-side. If the MUA_GIER[GIEn] bit is set to "1" on the MUA-side, a General Purpose Interrupt n request is triggered to Processor A. 

- • The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by writing "1", thereby signalling the MUB that the interrupt was accepted (cleared by the software). 

- • Writing "0" to the GIRn bit is ignored. • To ensure proper operations, you must verify that the GIRn bit is cleared (meaning that there is no pending interrupt) before setting it (GIRn bit). 

- • GIRn bit is cleared when the MU resets. ~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

||Instance<br>Field supported in|Field not supported in|
|---|---|---|
||MU_0.MUB<br>GCR|—|
||MU_1.MUB<br>GCR|—|
||MU_2.MUB<br>—|GCR|
||0b - MUB General Interrupt n is not requested to the MUA.<br>1b - MUB General Interrupt n is requested to the MUA.||
|25<br>GIR25|MUB General Purpose Interrupt Request n<br>• There are 32 General Purpose Interrupts (n = 0 to 31)<br>• Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the M<br>bit is set to "1" on the MUA-side, a General Purpose Interrupt n r<br>• The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by<br>MUB that the interrupt was accepted (cleared by the software).<br>• Writing "0" to the GIRn bit is ignored.<br>• To ensure proper operations, you must verify that the GIRn bit is<br>pending interrupt) before setting it (GIRn bit).<br>• GIRn bit is cleared when the MU resets.<br>This field is not supported in every instance. The following tabl<br>supported registers.<br>~~NOTE~~|UA-side. If the MUA_GIER[GIEn]<br>equest is triggered to Processor A.<br>writing "1", thereby signalling the<br>cleared (meaning that there is no<br>e includes only|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1338 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function||
|---|---|---|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>GCR|—|
||MU_1.MUB<br>GCR|—|
||MU_2.MUB<br>—|GCR|
||0b - MUB General Interrupt n is not requested to the MUA.<br>1b - MUB General Interrupt n is requested to the MUA.||
|24<br>GIR24|MUB General Purpose Interrupt Request n<br>• There are 32 General Purpose Interrupts (n = 0 to 31)<br>• Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the M<br>bit is set to "1" on the MUA-side, a General Purpose Interrupt n r<br>• The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by<br>MUB that the interrupt was accepted (cleared by the software).<br>• Writing "0" to the GIRn bit is ignored.<br>• To ensure proper operations, you must verify that the GIRn bit is<br>pending interrupt) before setting it (GIRn bit).<br>• GIRn bit is cleared when the MU resets.<br>This field is not supported in every instance. The following table<br>supported registers.<br>~~NOTE~~|UA-side. If the MUA_GIER[GIEn]<br>equest is triggered to Processor A.<br>writing "1", thereby signalling the<br>cleared (meaning that there is no<br>includes only|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>GCR|—|
||MU_1.MUB<br>GCR|—|
||MU_2.MUB<br>—<br>0b - MUB General Interrupt n is not requested to the MUA.<br>1b - MUB General Interrupt n is requested to the MUA.|GCR|
|23<br>GIR23|MUB General Purpose Interrupt Request n<br>• There are 32 General Purpose Interrupts (n = 0 to 31)<br>• Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the M<br>bit is set to "1" on the MUA-side, a General Purpose Interrupt n r<br>Table continues on the next page...|UA-side. If the MUA_GIER[GIEn]<br>equest is triggered to Processor A.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1339 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

- Field Function • The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by writing "1", thereby signalling the MUB that the interrupt was accepted (cleared by the software). 

   - Writing "0" to the GIRn bit is ignored. 

   - To ensure proper operations, you must verify that the GIRn bit is cleared (meaning that there is no pending interrupt) before setting it (GIRn bit). 

   - GIRn bit is cleared when the MU resets. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|GCR|—|
|MU_1.MUB|GCR|—|
|MU_2.MUB|—|GCR|



0b - MUB General Interrupt n is not requested to the MUA. 1b - MUB General Interrupt n is requested to the MUA. 

22 

MUB General Purpose Interrupt Request n 

- GIR22 • There are 32 General Purpose Interrupts (n = 0 to 31) 

   - Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the MUA-side. If the MUA_GIER[GIEn] bit is set to "1" on the MUA-side, a General Purpose Interrupt n request is triggered to Processor A. 

   - The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by writing "1", thereby signalling the MUB that the interrupt was accepted (cleared by the software). 

   - Writing "0" to the GIRn bit is ignored. 

   - To ensure proper operations, you must verify that the GIRn bit is cleared (meaning that there is no pending interrupt) before setting it (GIRn bit). 

   - GIRn bit is cleared when the MU resets. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|GCR|—|
|MU_1.MUB|GCR|—|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1340 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function||
|---|---|---|
||Instance<br>Field supported in|Field not supported in|
||MU_2.MUB<br>—|GCR|
||0b - MUB General Interrupt n is not requested to the MUA.<br>1b - MUB General Interrupt n is requested to the MUA.||
|21<br>GIR21|MUB General Purpose Interrupt Request n<br>• There are 32 General Purpose Interrupts (n = 0 to 31)<br>• Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the M<br>bit is set to "1" on the MUA-side, a General Purpose Interrupt n r<br>• The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by w<br>MUB that the interrupt was accepted (cleared by the software).<br>• Writing "0" to the GIRn bit is ignored.<br>• To ensure proper operations, you must verify that the GIRn bit is<br>pending interrupt) before setting it (GIRn bit).<br>• GIRn bit is cleared when the MU resets.<br>This field is not supported in every instance. The following table<br>supported registers.<br>~~NOTE~~|UA-side. If the MUA_GIER[GIEn]<br>equest is triggered to Processor A.<br>riting "1", thereby signalling the<br>cleared (meaning that there is no<br>includes only|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>GCR|—|
||MU_1.MUB<br>GCR|—|
||MU_2.MUB<br>—|GCR|
||0b - MUB General Interrupt n is not requested to the MUA.<br>1b - MUB General Interrupt n is requested to the MUA.||
|20<br>GIR20|MUB General Purpose Interrupt Request n<br>• There are 32 General Purpose Interrupts (n = 0 to 31)<br>• Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the M<br>bit is set to "1" on the MUA-side, a General Purpose Interrupt n r<br>• The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by w<br>MUB that the interrupt was accepted (cleared by the software).<br>• Writing "0" to the GIRn bit is ignored.|UA-side. If the MUA_GIER[GIEn]<br>equest is triggered to Processor A.<br>riting "1", thereby signalling the|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1341 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

- Field Function • To ensure proper operations, you must verify that the GIRn bit is cleared (meaning that there is no pending interrupt) before setting it (GIRn bit). 

   - GIRn bit is cleared when the MU resets. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|GCR|—|
|MU_1.MUB|GCR|—|
|MU_2.MUB|—|GCR|



- 0b - MUB General Interrupt n is not requested to the MUA. 

1b - MUB General Interrupt n is requested to the MUA. 

MUB General Purpose Interrupt Request n 

19 MUB General Purpose Interrupt Request n GIR19 • There are 32 General Purpose Interrupts (n = 0 to 31) 

- Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the MUA-side. If the MUA_GIER[GIEn] bit is set to "1" on the MUA-side, a General Purpose Interrupt n request is triggered to Processor A. 

- The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by writing "1", thereby signalling the MUB that the interrupt was accepted (cleared by the software). 

- Writing "0" to the GIRn bit is ignored. 

- To ensure proper operations, you must verify that the GIRn bit is cleared (meaning that there is no pending interrupt) before setting it (GIRn bit). 

- GIRn bit is cleared when the MU resets. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|GCR|—|
|MU_1.MUB|GCR|—|
|MU_2.MUB|—|GCR|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1342 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function<br>0b - MUB General Interrupt n is not requested to the MUA.<br>1b - MUB General Interrupt n is requested to the MUA.|
|---|---|
|18<br>GIR18|MUB General Purpose Interrupt Request n<br>• There are 32 General Purpose Interrupts (n = 0 to 31)<br>• Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the MUA-side. If the MUA_GIER[GIEn]<br>bit is set to "1" on the MUA-side, a General Purpose Interrupt n request is triggered to Processor A.<br>• The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by writing "1", thereby signalling the<br>MUB that the interrupt was accepted (cleared by the software).<br>• Writing "0" to the GIRn bit is ignored.<br>• To ensure proper operations, you must verify that the GIRn bit is cleared (meaning that there is no<br>pending interrupt) before setting it (GIRn bit).<br>• GIRn bit is cleared when the MU resets.<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>~~NOTE~~|
||Instance<br>Field supported in<br>Field not supported in|
||MU_0.MUB<br>GCR<br>—|
||MU_1.MUB<br>GCR<br>—|
||MU_2.MUB<br>—<br>GCR|
||0b - MUB General Interrupt n is not requested to the MUA.<br>1b - MUB General Interrupt n is requested to the MUA.|
|17<br>GIR17|MUB General Purpose Interrupt Request n<br>• There are 32 General Purpose Interrupts (n = 0 to 31)<br>• Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the MUA-side. If the MUA_GIER[GIEn]<br>bit is set to "1" on the MUA-side, a General Purpose Interrupt n request is triggered to Processor A.<br>• The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by writing "1", thereby signalling the<br>MUB that the interrupt was accepted (cleared by the software).<br>• Writing "0" to the GIRn bit is ignored.<br>• To ensure proper operations, you must verify that the GIRn bit is cleared (meaning that there is no<br>pending interrupt) before setting it (GIRn bit).<br>• GIRn bit is cleared when the MU resets.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1343 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function<br>This field is not supported in every instance. The following table<br>supported registers.<br>~~NOTE~~<br><br>|includes only<br>|
|---|---|---|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>GCR|—|
||MU_1.MUB<br>GCR|—|
||MU_2.MUB<br>—|GCR|
||0b - MUB General Interrupt n is not requested to the MUA.<br>1b - MUB General Interrupt n is requested to the MUA.||
|16<br>GIR16|MUB General Purpose Interrupt Request n<br>• There are 32 General Purpose Interrupts (n = 0 to 31)<br>• Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the M<br>bit is set to "1" on the MUA-side, a General Purpose Interrupt n r<br>• The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by<br>MUB that the interrupt was accepted (cleared by the software).<br>• Writing "0" to the GIRn bit is ignored.<br>• To ensure proper operations, you must verify that the GIRn bit is<br>pending interrupt) before setting it (GIRn bit).<br>• GIRn bit is cleared when the MU resets.<br>This field is not supported in every instance. The following table<br>supported registers.<br>~~NOTE~~<br><br>|UA-side. If the MUA_GIER[GIEn]<br>equest is triggered to Processor A.<br>writing "1", thereby signalling the<br>cleared (meaning that there is no<br>includes only<br>|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>GCR|—|
||MU_1.MUB<br>GCR|—|
||MU_2.MUB<br>—|GCR|
||0b - MUB General Interrupt n is not requested to the MUA.<br>1b - MUB General Interrupt n is requested to the MUA.||
|15|MUB General Purpose Interrupt Request n<br>Table continues on the next page...||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1344 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

- Field Function 

- GIR15 • There are 32 General Purpose Interrupts (n = 0 to 31) • Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the MUA-side. If the MUA_GIER[GIEn] bit is set to "1" on the MUA-side, a General Purpose Interrupt n request is triggered to Processor A. 

   - The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by writing "1", thereby signalling the MUB that the interrupt was accepted (cleared by the software). 

   - Writing "0" to the GIRn bit is ignored. 

   - To ensure proper operations, you must verify that the GIRn bit is cleared (meaning that there is no pending interrupt) before setting it (GIRn bit). 

   - GIRn bit is cleared when the MU resets. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

||Instance|Field supported in|Field not supported in|
|---|---|---|---|
||MU_0.MUB|GCR|—|
||MU_1.MUB|GCR|—|
||MU_2.MUB|—|GCR|
||0b - MUB General Inter<br>1b - MUB General Inter|rupt n is not requested to the MUA.<br>rupt n is requested to the MUA.||
|14|MUB General Purpose Interru|pt Request n||
|GIR14|• There are 32 General Pur<br>• Writing "1" to the GIRn bit<br>bit is set to "1" on the MU<br>• The GIRn bit is cleared if t<br>MUB that the interrupt wa|pose Interrupts (n = 0 to 31)<br>sets the MUA_GSR[GIPn] bit on the M<br>A-side, a General Purpose Interrupt n r<br>he MUA_GSR[GIPn] bit is cleared by<br>s accepted (cleared by the software).|UA-side. If the MUA_GIER[GIEn]<br>equest is triggered to Processor A.<br>writing "1", thereby signalling the|



- Writing "0" to the GIRn bit is ignored. 

- To ensure proper operations, you must verify that the GIRn bit is cleared (meaning that there is no pending interrupt) before setting it (GIRn bit). 

- • GIRn bit is cleared when the MU resets. ~~<mark>NOTE</mark>~~ 

- This field is not supported in every instance. The following table includes only supported registers. 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1345 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function||
|---|---|---|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>GCR|—|
||MU_1.MUB<br>GCR|—|
||MU_2.MUB<br>—|GCR|
||0b - MUB General Interrupt n is not requested to the MUA.<br>1b - MUB General Interrupt n is requested to the MUA.||
|13<br>GIR13|MUB General Purpose Interrupt Request n<br>• There are 32 General Purpose Interrupts (n = 0 to 31)<br>• Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the M<br>bit is set to "1" on the MUA-side, a General Purpose Interrupt n r<br>• The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by<br>MUB that the interrupt was accepted (cleared by the software).<br>• Writing "0" to the GIRn bit is ignored.<br>• To ensure proper operations, you must verify that the GIRn bit is<br>pending interrupt) before setting it (GIRn bit).<br>• GIRn bit is cleared when the MU resets.<br>This field is not supported in every instance. The following table<br>supported registers.<br>~~NOTE~~|UA-side. If the MUA_GIER[GIEn]<br>equest is triggered to Processor A.<br>writing "1", thereby signalling the<br>cleared (meaning that there is no<br>includes only|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>GCR|—|
||MU_1.MUB<br>GCR|—|
||MU_2.MUB<br>—<br>0b - MUB General Interrupt n is not requested to the MUA.<br>1b - MUB General Interrupt n is requested to the MUA.|GCR|
|12<br>GIR12|MUB General Purpose Interrupt Request n<br>• There are 32 General Purpose Interrupts (n = 0 to 31)<br>• Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the M<br>bit is set to "1" on the MUA-side, a General Purpose Interrupt n r<br>Table continues on the next page...|UA-side. If the MUA_GIER[GIEn]<br>equest is triggered to Processor A.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1346 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

- Field Function • The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by writing "1", thereby signalling the MUB that the interrupt was accepted (cleared by the software). 

   - Writing "0" to the GIRn bit is ignored. 

   - To ensure proper operations, you must verify that the GIRn bit is cleared (meaning that there is no pending interrupt) before setting it (GIRn bit). 

   - GIRn bit is cleared when the MU resets. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|GCR|—|
|MU_1.MUB|GCR|—|
|MU_2.MUB|—|GCR|



0b - MUB General Interrupt n is not requested to the MUA. 1b - MUB General Interrupt n is requested to the MUA. 

11 MUB General Purpose Interrupt Request n 

- GIR11 • There are 32 General Purpose Interrupts (n = 0 to 31) 

   - Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the MUA-side. If the MUA_GIER[GIEn] bit is set to "1" on the MUA-side, a General Purpose Interrupt n request is triggered to Processor A. 

   - The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by writing "1", thereby signalling the MUB that the interrupt was accepted (cleared by the software). 

   - Writing "0" to the GIRn bit is ignored. 

   - To ensure proper operations, you must verify that the GIRn bit is cleared (meaning that there is no pending interrupt) before setting it (GIRn bit). 

   - GIRn bit is cleared when the MU resets. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|GCR|—|
|MU_1.MUB|GCR|—|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1347 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function||
|---|---|---|
||Instance<br>Field supported in|Field not supported in|
||MU_2.MUB<br>—|GCR|
||0b - MUB General Interrupt n is not requested to the MUA.<br>1b - MUB General Interrupt n is requested to the MUA.||
|10<br>GIR10|MUB General Purpose Interrupt Request n<br>• There are 32 General Purpose Interrupts (n = 0 to 31)<br>• Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the M<br>bit is set to "1" on the MUA-side, a General Purpose Interrupt n r<br>• The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by w<br>MUB that the interrupt was accepted (cleared by the software).<br>• Writing "0" to the GIRn bit is ignored.<br>• To ensure proper operations, you must verify that the GIRn bit is<br>pending interrupt) before setting it (GIRn bit).<br>• GIRn bit is cleared when the MU resets.<br>This field is not supported in every instance. The following table<br>supported registers.<br>~~NOTE~~|UA-side. If the MUA_GIER[GIEn]<br>equest is triggered to Processor A.<br>riting "1", thereby signalling the<br>cleared (meaning that there is no<br>includes only|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>GCR|—|
||MU_1.MUB<br>GCR|—|
||MU_2.MUB<br>—<br>0b - MUB General Interrupt n is not requested to the MUA.<br>1b - MUB General Interrupt n is requested to the MUA.|GCR|
|9<br>GIR9|MUB General Purpose Interrupt Request n<br>• There are 32 General Purpose Interrupts (n = 0 to 31)<br>• Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the M<br>bit is set to "1" on the MUA-side, a General Purpose Interrupt n r<br>• The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by w<br>MUB that the interrupt was accepted (cleared by the software).<br>• Writing "0" to the GIRn bit is ignored.|UA-side. If the MUA_GIER[GIEn]<br>equest is triggered to Processor A.<br>riting "1", thereby signalling the|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1348 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

- Field Function • To ensure proper operations, you must verify that the GIRn bit is cleared (meaning that there is no pending interrupt) before setting it (GIRn bit). 

   - GIRn bit is cleared when the MU resets. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|GCR|—|
|MU_1.MUB|GCR|—|
|MU_2.MUB|—|GCR|



- 0b - MUB General Interrupt n is not requested to the MUA. 

1b - MUB General Interrupt n is requested to the MUA. 

MUB General Purpose Interrupt Request n 

8 MUB General Purpose Interrupt Request n GIR8 • There are 32 General Purpose Interrupts (n = 0 to 31) 

- Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the MUA-side. If the MUA_GIER[GIEn] bit is set to "1" on the MUA-side, a General Purpose Interrupt n request is triggered to Processor A. 

- The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by writing "1", thereby signalling the MUB that the interrupt was accepted (cleared by the software). 

- Writing "0" to the GIRn bit is ignored. 

- To ensure proper operations, you must verify that the GIRn bit is cleared (meaning that there is no pending interrupt) before setting it (GIRn bit). 

- GIRn bit is cleared when the MU resets. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|GCR|—|
|MU_1.MUB|GCR|—|
|MU_2.MUB|—|GCR|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1349 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - MUB General Interrupt n is not requested to the MUA.<br>1b - MUB General Interrupt n is requested to the MUA.|
|7<br>GIR7|MUB General Purpose Interrupt Request n<br>• There are 32 General Purpose Interrupts (n = 0 to 31)<br>• Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the MUA-side. If the MUA_GIER[GIEn]<br>bit is set to "1" on the MUA-side, a General Purpose Interrupt n request is triggered to Processor A.<br>• The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by writing "1", thereby signalling the<br>MUB that the interrupt was accepted (cleared by the software).<br>• Writing "0" to the GIRn bit is ignored.<br>• To ensure proper operations, you must verify that the GIRn bit is cleared (meaning that there is no<br>pending interrupt) before setting it (GIRn bit).<br>• GIRn bit is cleared when the MU resets.<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>~~NOTE~~|
||Instance<br>Field supported in<br>Field not supported in|
||MU_0.MUB<br>GCR<br>—|
||MU_1.MUB<br>GCR<br>—|
||MU_2.MUB<br>—<br>GCR|
||0b - MUB General Interrupt n is not requested to the MUA.<br>1b - MUB General Interrupt n is requested to the MUA.|
|6<br>GIR6|MUB General Purpose Interrupt Request n<br>• There are 32 General Purpose Interrupts (n = 0 to 31)<br>• Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the MUA-side. If the MUA_GIER[GIEn]<br>bit is set to "1" on the MUA-side, a General Purpose Interrupt n request is triggered to Processor A.<br>• The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by writing "1", thereby signalling the<br>MUB that the interrupt was accepted (cleared by the software).<br>• Writing "0" to the GIRn bit is ignored.<br>• To ensure proper operations, you must verify that the GIRn bit is cleared (meaning that there is no<br>pending interrupt) before setting it (GIRn bit).<br>• GIRn bit is cleared when the MU resets.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1350 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function<br>This field is not supported in every instance. The following table<br>supported registers.<br>~~NOTE~~<br><br>|includes only<br>|
|---|---|---|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>GCR|—|
||MU_1.MUB<br>GCR|—|
||MU_2.MUB<br>—|GCR|
||0b - MUB General Interrupt n is not requested to the MUA.<br>1b - MUB General Interrupt n is requested to the MUA.||
|5<br>GIR5|MUB General Purpose Interrupt Request n<br>• There are 32 General Purpose Interrupts (n = 0 to 31)<br>• Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the M<br>bit is set to "1" on the MUA-side, a General Purpose Interrupt n r<br>• The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by w<br>MUB that the interrupt was accepted (cleared by the software).<br>• Writing "0" to the GIRn bit is ignored.<br>• To ensure proper operations, you must verify that the GIRn bit is<br>pending interrupt) before setting it (GIRn bit).<br>• GIRn bit is cleared when the MU resets.<br>This field is not supported in every instance. The following table<br>supported registers.<br>~~NOTE~~<br><br>|UA-side. If the MUA_GIER[GIEn]<br>equest is triggered to Processor A.<br>riting "1", thereby signalling the<br>cleared (meaning that there is no<br>includes only<br>|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>GCR|—|
||MU_1.MUB<br>GCR|—|
||MU_2.MUB<br>—|GCR|
||0b - MUB General Interrupt n is not requested to the MUA.<br>1b - MUB General Interrupt n is requested to the MUA.||
|4|MUB General Purpose Interrupt Request n<br>Table continues on the next page...||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1351 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

##### Field Function GIR4 • There are 32 General Purpose Interrupts (n = 0 to 31) 

- Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the MUA-side. If the MUA_GIER[GIEn] bit is set to "1" on the MUA-side, a General Purpose Interrupt n request is triggered to Processor A. 

- The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by writing "1", thereby signalling the MUB that the interrupt was accepted (cleared by the software). 

- Writing "0" to the GIRn bit is ignored. 

- To ensure proper operations, you must verify that the GIRn bit is cleared (meaning that there is no pending interrupt) before setting it (GIRn bit). 

- GIRn bit is cleared when the MU resets. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|GCR|—|
|MU_1.MUB|GCR|—|
|MU_2.MUB|—|GCR|



0b - MUB General Interrupt n is not requested to the MUA. 1b - MUB General Interrupt n is requested to the MUA. 

- 3 MUB General Purpose Interrupt Request n 

- GIR3 • There are 32 General Purpose Interrupts (n = 0 to 31) • Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the MUA-side. If the MUA_GIER[GIEn] bit is set to "1" on the MUA-side, a General Purpose Interrupt n request is triggered to Processor A. 

   - The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by writing "1", thereby signalling the MUB that the interrupt was accepted (cleared by the software). 

   - Writing "0" to the GIRn bit is ignored. 

   - To ensure proper operations, you must verify that the GIRn bit is cleared (meaning that there is no pending interrupt) before setting it (GIRn bit). 

   - GIRn bit is cleared when the MU resets. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1352 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function||
|---|---|---|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>GCR|—|
||MU_1.MUB<br>GCR|—|
||MU_2.MUB<br>—|GCR|
||0b - MUB General Interrupt n is not requested to the MUA.<br>1b - MUB General Interrupt n is requested to the MUA.||
|2<br>GIR2|MUB General Purpose Interrupt Request n<br>• There are 32 General Purpose Interrupts (n = 0 to 31)<br>• Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the M<br>bit is set to "1" on the MUA-side, a General Purpose Interrupt n r<br>• The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by<br>MUB that the interrupt was accepted (cleared by the software).<br>• Writing "0" to the GIRn bit is ignored.<br>• To ensure proper operations, you must verify that the GIRn bit is<br>pending interrupt) before setting it (GIRn bit).<br>• GIRn bit is cleared when the MU resets.<br>This field is not supported in every instance. The following tabl<br>supported registers.<br>~~NOTE~~|UA-side. If the MUA_GIER[GIEn]<br>equest is triggered to Processor A.<br>writing "1", thereby signalling the<br>cleared (meaning that there is no<br>e includes only|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>GCR|—|
||MU_1.MUB<br>GCR|—|
||MU2MUB<br>—|GCR|
||_.<br>0b - MUB General Interrupt n is not requested to the MUA.<br>1b - MUB General Interrupt n is requested to the MUA.||
|1<br>GIR1|MUB General Purpose Interrupt Request n<br>• There are 32 General Purpose Interrupts (n = 0 to 31)<br>• Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the M<br>bit is set to "1" on the MUA-side, a General Purpose Interrupt n r<br>Table continues on the next page...|UA-side. If the MUA_GIER[GIEn]<br>equest is triggered to Processor A.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1353 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

- Field Function • The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by writing "1", thereby signalling the MUB that the interrupt was accepted (cleared by the software). 

- • Writing "0" to the GIRn bit is ignored. 

||• To ensure proper operations, you must verify that the GIRn bit is<br>pending interrupt) before setting it (GIRn bit).<br>• GIRn bit is cleared when the MU resets.<br>This field is not supported in every instance. The following tabl<br>supported registers.<br>~~NOTE~~<br><br>|cleared (meaning that there is no<br>e includes only<br>|
|---|---|---|
||Instance<br>Field supported in|Field not supported in|
||MU_0.MUB<br>GCR|—|
||MU_1.MUB<br>GCR|—|
||MU_2.MUB<br>—|GCR|
||0b - MUB General Interrupt n is not requested to the MUA.<br>1b - MUB General Interrupt n is requested to the MUA.||
|0<br>GIR0|MUB General Purpose Interrupt Request n<br>• There are 32 General Purpose Interrupts (n = 0 to 31)<br>• Writing "1" to the GIRn bit sets the MUA_GSR[GIPn] bit on the M<br>bit is set to "1" on the MUA-side, a General Purpose Interrupt n r<br>• The GIRn bit is cleared if the MUA_GSR[GIPn] bit is cleared by<br>MUB that the interrupt was accepted (cleared by the software).<br>• Writing "0" to the GIRn bit is ignored.<br>• To ensure proper operations, you must verify that the GIRn bit is<br>pending interrupt) before setting it (GIRn bit).<br>• GIRn bit is cleared when the MU resets.<br>0b - MUB General Interrupt n is not requested to the MUA.<br>1b - MUB General Interrupt n is requested to the MUA.|UA-side. If the MUA_GIER[GIEn]<br>equest is triggered to Processor A.<br>writing "1", thereby signalling the<br>cleared (meaning that there is no|



#### 39.6.2.12 General Status Register (GSR) 

##### Offset 

|Register|Offset|
|---|---|
|GSR|118h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1354 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Function 

The GSR register contains the status of the MUB general interrupt pending requests. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|GIP31|GIP30|GIP29|GIP28|GIP27|GIP26|GIP25|GIP24|GIP23|GIP22|GIP21|GIP20|GIP19|GIP18|GIP17|GIP16|
|W|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|GIP15|GIP14|GIP13|GIP12|GIP11|GIP10|GIP9|GIP8|GIP7|GIP6|GIP5|GIP4|GIP3|GIP2|GIP1|GIP0|
|W|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|MUB General Interrupt Request Pending n|
|GIP31|• There are 32 General Purpose Interrupts (n = 0 to 31)|
||• GIPn bit signals the MUB that the MUA_GCR[GIRn] bit was set from "0" to "1". If the|
||MUB_GIER[GIEn] bit is set to "1", a General Interrupt n request is issued to Processor B.|



- The GIPn bit is cleared by writing "1". Writing "0" is ignored. 

- GIPn bit is cleared when the MU resets. 

- After GIPn bit is cleared, the General Interrupt n request(if the MUB_GIER[GIEn] bit is set to "1") is cleared on the MUB side. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

||Instance<br>Field supported in|Field not supported in|
|---|---|---|
||MU_0.MUB<br>GSR|—|
||MU_1.MUB<br>GSR|—|
||MU_2.MUB<br>—|GSR|
||0b - MUB general purpose interrupt n is not pending.||
||1b - MUB general purpose interrupt n is pending.||
|30|MUB General Interrupt Request Pending n||
|GIP30|• There are 32 General Purpose Interrupts (n = 0 to 31)||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1355 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

- Field Function • GIPn bit signals the MUB that the MUA_GCR[GIRn] bit was set from "0" to "1". If the MUB_GIER[GIEn] bit is set to "1", a General Interrupt n request is issued to Processor B. 

   - The GIPn bit is cleared by writing "1". Writing "0" is ignored. 

   - GIPn bit is cleared when the MU resets. 

   - After GIPn bit is cleared, the General Interrupt n request(if the MUB_GIER[GIEn] bit is set to "1") is cleared on the MUB side. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|GSR|—|
|MU_1.MUB|GSR|—|
|MU_2.MUB|—|GSR|



0b - MUB general purpose interrupt n is not pending. 1b - MUB general purpose interrupt n is pending. 

29 MUB General Interrupt Request Pending n GIP29 • There are 32 General Purpose Interrupts (n = 0 to 31) 

- GIPn bit signals the MUB that the MUA_GCR[GIRn] bit was set from "0" to "1". If the MUB_GIER[GIEn] bit is set to "1", a General Interrupt n request is issued to Processor B. 

- The GIPn bit is cleared by writing "1". Writing "0" is ignored. 

- GIPn bit is cleared when the MU resets. 

- After GIPn bit is cleared, the General Interrupt n request(if the MUB_GIER[GIEn] bit is set to "1") is cleared on the MUB side. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|GSR|—|
|MU_1.MUB|GSR|—|
|MU_2.MUB|—|GSR|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1356 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function|||
|---|---|---|---|
||Instance|Field supported in|Field not supported in|
||0b - MUB general purpos<br>1b - MUB general purpos|e interrupt n is not pending.<br>e interrupt n is pending.||
|28<br>GIP28|MUB General Interrupt Request<br>• There are 32 General Purpo<br>• GIPn bit signals the MUB tha<br>MUB_GIER[GIEn] bit is set t<br>• The GIPn bit is cleared by w<br>• GIPn bit is cleared when the<br>• After GIPn bit is cleared, the<br>cleared on the MUB side.<br>This field is not suppor<br>supported registers.|Pending n<br>se Interrupts (n = 0 to 31)<br>t the MUA_GCR[GIRn] bit was se<br>o "1", a General Interrupt n reques<br>riting "1". Writing "0" is ignored.<br>MU resets.<br>General Interrupt n request(if the<br>ted in every instance. The following ta<br>~~NOTE~~|t from "0" to "1". If the<br>t is issued to Processor B.<br>MUB_GIER[GIEn] bit is set to "1") is<br>ble includes only|
||Instance|Field supported in|Field not supported in|
||MU_0.MUB|GSR|—|
||MU_1.MUB|GSR|—|
||MU_2.MUB|—|GSR|
||0b - MUB general purpos<br>1b - MUB general purpos|e interrupt n is not pending.<br>e interrupt n is pending.||
|27<br>GIP27|MUB General Interrupt Request<br>• There are 32 General Purpo<br>• GIPn bit signals the MUB tha<br>MUB_GIER[GIEn] bit is set t<br>• The GIPn bit is cleared by w<br>• GIPn bit is cleared when the<br>• After GIPn bit is cleared, the<br>cleared on the MUB side.<br>This field is not suppor<br>supported registers.|Pending n<br>se Interrupts (n = 0 to 31)<br>t the MUA_GCR[GIRn] bit was se<br>o "1", a General Interrupt n reques<br>riting "1". Writing "0" is ignored.<br>MU resets.<br>General Interrupt n request(if the<br>ted in every instance. The following ta<br>~~NOTE~~|t from "0" to "1". If the<br>t is issued to Processor B.<br>MUB_GIER[GIEn] bit is set to "1") is<br>ble includes only|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1357 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1358-03.png)


<!-- Start of picture text -->
Field Function<br>Instance Field supported in Field not supported in<br>MU_0.MUB GSR —<br>MU_1.MUB GSR —<br>MU_2.MUB — GSR<br>0b - MUB general purpose interrupt n is not pending.<br>1b - MUB general purpose interrupt n is pending.<br>26 MUB General Interrupt Request Pending n<br>GIP26 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• GIPn bit signals the MUB that the MUA_GCR[GIRn] bit was set from "0" to "1". If the<br>MUB_GIER[GIEn] bit is set to "1", a General Interrupt n request is issued to Processor B.<br>• The GIPn bit is cleared by writing "1". Writing "0" is ignored.<br>• GIPn bit is cleared when the MU resets.<br>• After GIPn bit is cleared, the General Interrupt n request(if the MUB_GIER[GIEn] bit is set to "1") is<br>cleared on the MUB side.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GSR —<br>MU_1.MUB GSR —<br>MU_2.MUB — GSR<br>0b - MUB general purpose interrupt n is not pending.<br>1b - MUB general purpose interrupt n is pending.<br>25 MUB General Interrupt Request Pending n<br>GIP25 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• GIPn bit signals the MUB that the MUA_GCR[GIRn] bit was set from "0" to "1". If the<br>MUB_GIER[GIEn] bit is set to "1", a General Interrupt n request is issued to Processor B.<br>• The GIPn bit is cleared by writing "1". Writing "0" is ignored.<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1358 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

Field Function 

- GIPn bit is cleared when the MU resets. 

- After GIPn bit is cleared, the General Interrupt n request(if the MUB_GIER[GIEn] bit is set to "1") is cleared on the MUB side. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|GSR|—|
|MU_1.MUB|GSR|—|
|MU_2.MUB|—|GSR|



- 0b - MUB general purpose interrupt n is not pending. 

- 1b - MUB general purpose interrupt n is pending. 

24 

GIP24 

MUB General Interrupt Request Pending n 

- There are 32 General Purpose Interrupts (n = 0 to 31) 

- GIPn bit signals the MUB that the MUA_GCR[GIRn] bit was set from "0" to "1". If the MUB_GIER[GIEn] bit is set to "1", a General Interrupt n request is issued to Processor B. 

- The GIPn bit is cleared by writing "1". Writing "0" is ignored. 

- GIPn bit is cleared when the MU resets. 

- After GIPn bit is cleared, the General Interrupt n request(if the MUB_GIER[GIEn] bit is set to "1") is cleared on the MUB side. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|GSR|—|
|MU_1.MUB|GSR|—|
|MU_2.MUB|—|GSR|



- 0b - MUB general purpose interrupt n is not pending. 

1b - MUB general purpose interrupt n is pending. 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1359 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

Field Function 23 MUB General Interrupt Request Pending n GIP23 • There are 32 General Purpose Interrupts (n = 0 to 31) 

- GIPn bit signals the MUB that the MUA_GCR[GIRn] bit was set from "0" to "1". If the MUB_GIER[GIEn] bit is set to "1", a General Interrupt n request is issued to Processor B. 

- The GIPn bit is cleared by writing "1". Writing "0" is ignored. 

- GIPn bit is cleared when the MU resets. 

- After GIPn bit is cleared, the General Interrupt n request(if the MUB_GIER[GIEn] bit is set to "1") is cleared on the MUB side. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

||Instance|Field supported in|Field not supported in|
|---|---|---|---|
||MU_0.MUB|GSR|—|
||MU_1.MUB|GSR|—|
||MU_2.MUB|—|GSR|
||0b - MUB general purp<br>1b - MUB general purp|ose interrupt n is not pending.<br>ose interrupt n is pending.||
|22<br>GIP22|MUB General Interrupt Reque<br>• There are 32 General Pur<br>• GIPn bit signals the MUB<br>MUB_GIER[GIEn] bit is s<br>• The GIPn bit is cleared by|st Pending n<br>pose Interrupts (n = 0 to 31)<br>that the MUA_GCR[GIRn] bit was set<br>et to "1", a General Interrupt n reques<br>writing "1". Writing "0" is ignored.|from "0" to "1". If the<br>t is issued to Processor B.|




![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1360-11.png)


<!-- Start of picture text -->
MUB General Interrupt Request Pending n<br>• There are 32 General Purpose Interrupts (n = 0 to 31)<br>• GIPn bit signals the MUB that the MUA_GCR[GIRn] bit was set from "0" to "1". If the<br>MUB_GIER[GIEn] bit is set to "1", a General Interrupt n request is issued to Processor B.<br>• The GIPn bit is cleared by writing "1". Writing "0" is ignored.<br>• GIPn bit is cleared when the MU resets.<br>• After GIPn bit is cleared, the General Interrupt n request(if the MUB_GIER[GIEn] bit is set to "1") is<br>cleared on the MUB side.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GSR —<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1360 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1361-03.png)


<!-- Start of picture text -->
Field Function<br>Instance Field supported in Field not supported in<br>MU_1.MUB GSR —<br>MU_2.MUB — GSR<br>0b - MUB general purpose interrupt n is not pending.<br>1b - MUB general purpose interrupt n is pending.<br>21 MUB General Interrupt Request Pending n<br>GIP21 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• GIPn bit signals the MUB that the MUA_GCR[GIRn] bit was set from "0" to "1". If the<br>MUB_GIER[GIEn] bit is set to "1", a General Interrupt n request is issued to Processor B.<br>• The GIPn bit is cleared by writing "1". Writing "0" is ignored.<br>• GIPn bit is cleared when the MU resets.<br>• After GIPn bit is cleared, the General Interrupt n request(if the MUB_GIER[GIEn] bit is set to "1") is<br>cleared on the MUB side.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GSR —<br>MU_1.MUB GSR —<br>MU_2.MUB — GSR<br>0b - MUB general purpose interrupt n is not pending.<br>1b - MUB general purpose interrupt n is pending.<br>20 MUB General Interrupt Request Pending n<br>GIP20 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• GIPn bit signals the MUB that the MUA_GCR[GIRn] bit was set from "0" to "1". If the<br>MUB_GIER[GIEn] bit is set to "1", a General Interrupt n request is issued to Processor B.<br>• The GIPn bit is cleared by writing "1". Writing "0" is ignored.<br>• GIPn bit is cleared when the MU resets.<br>• After GIPn bit is cleared, the General Interrupt n request(if the MUB_GIER[GIEn] bit is set to "1") is<br>cleared on the MUB side.<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1361 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1362-03.png)


<!-- Start of picture text -->
Field Function<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GSR —<br>MU_1.MUB GSR —<br>MU_2.MUB — GSR<br>0b - MUB general purpose interrupt n is not pending.<br>1b - MUB general purpose interrupt n is pending.<br>19 MUB General Interrupt Request Pending n<br>GIP19 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• GIPn bit signals the MUB that the MUA_GCR[GIRn] bit was set from "0" to "1". If the<br>MUB_GIER[GIEn] bit is set to "1", a General Interrupt n request is issued to Processor B.<br>• The GIPn bit is cleared by writing "1". Writing "0" is ignored.<br>• GIPn bit is cleared when the MU resets.<br>• After GIPn bit is cleared, the General Interrupt n request(if the MUB_GIER[GIEn] bit is set to "1") is<br>cleared on the MUB side.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GSR —<br>MU_1.MUB GSR —<br>MU_2.MUB — GSR<br>0b - MUB general purpose interrupt n is not pending.<br>1b - MUB general purpose interrupt n is pending.<br>18 MUB General Interrupt Request Pending n<br>GIP18 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1362 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

- Field Function • GIPn bit signals the MUB that the MUA_GCR[GIRn] bit was set from "0" to "1". If the MUB_GIER[GIEn] bit is set to "1", a General Interrupt n request is issued to Processor B. 

   - The GIPn bit is cleared by writing "1". Writing "0" is ignored. 

   - GIPn bit is cleared when the MU resets. 

   - After GIPn bit is cleared, the General Interrupt n request(if the MUB_GIER[GIEn] bit is set to "1") is cleared on the MUB side. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|GSR|—|
|MU_1.MUB|GSR|—|
|MU_2.MUB|—|GSR|



0b - MUB general purpose interrupt n is not pending. 1b - MUB general purpose interrupt n is pending. 17 MUB General Interrupt Request Pending n GIP17 • There are 32 General Purpose Interrupts (n = 0 to 31) 

- GIPn bit signals the MUB that the MUA_GCR[GIRn] bit was set from "0" to "1". If the MUB_GIER[GIEn] bit is set to "1", a General Interrupt n request is issued to Processor B. 

- The GIPn bit is cleared by writing "1". Writing "0" is ignored. 

- GIPn bit is cleared when the MU resets. 

- After GIPn bit is cleared, the General Interrupt n request(if the MUB_GIER[GIEn] bit is set to "1") is cleared on the MUB side. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|GSR|—|
|MU_1.MUB|GSR|—|
|MU_2.MUB|—|GSR|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1363 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function|||
|---|---|---|---|
||Instance|Field supported in|Field not supported in|
||0b - MUB general purpos<br>1b - MUB general purpos|e interrupt n is not pending.<br>e interrupt n is pending.||
|16<br>GIP16|MUB General Interrupt Request<br>• There are 32 General Purpo<br>• GIPn bit signals the MUB tha<br>MUB_GIER[GIEn] bit is set t<br>• The GIPn bit is cleared by w<br>• GIPn bit is cleared when the<br>• After GIPn bit is cleared, the<br>cleared on the MUB side.<br>This field is not suppor<br>supported registers.|Pending n<br>se Interrupts (n = 0 to 31)<br>t the MUA_GCR[GIRn] bit was se<br>o "1", a General Interrupt n reques<br>riting "1". Writing "0" is ignored.<br>MU resets.<br>General Interrupt n request(if the<br>ted in every instance. The following ta<br>~~NOTE~~|t from "0" to "1". If the<br>t is issued to Processor B.<br>MUB_GIER[GIEn] bit is set to "1") is<br>ble includes only|
||Instance|Field supported in|Field not supported in|
||MU_0.MUB|GSR|—|
||MU_1.MUB|GSR|—|
||MU_2.MUB|—|GSR|
||0b - MUB general purpos<br>1b - MUB general purpos|e interrupt n is not pending.<br>e interrupt n is pending.||
|15<br>GIP15|MUB General Interrupt Request<br>• There are 32 General Purpo<br>• GIPn bit signals the MUB tha<br>MUB_GIER[GIEn] bit is set t<br>• The GIPn bit is cleared by w<br>• GIPn bit is cleared when the<br>• After GIPn bit is cleared, the<br>cleared on the MUB side.<br>This field is not suppor<br>supported registers.|Pending n<br>se Interrupts (n = 0 to 31)<br>t the MUA_GCR[GIRn] bit was se<br>o "1", a General Interrupt n reques<br>riting "1". Writing "0" is ignored.<br>MU resets.<br>General Interrupt n request(if the<br>ted in every instance. The following ta<br>~~NOTE~~|t from "0" to "1". If the<br>t is issued to Processor B.<br>MUB_GIER[GIEn] bit is set to "1") is<br>ble includes only|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1364 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1365-03.png)


<!-- Start of picture text -->
Field Function<br>Instance Field supported in Field not supported in<br>MU_0.MUB GSR —<br>MU_1.MUB GSR —<br>MU_2.MUB — GSR<br>0b - MUB general purpose interrupt n is not pending.<br>1b - MUB general purpose interrupt n is pending.<br>14 MUB General Interrupt Request Pending n<br>GIP14 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• GIPn bit signals the MUB that the MUA_GCR[GIRn] bit was set from "0" to "1". If the<br>MUB_GIER[GIEn] bit is set to "1", a General Interrupt n request is issued to Processor B.<br>• The GIPn bit is cleared by writing "1". Writing "0" is ignored.<br>• GIPn bit is cleared when the MU resets.<br>• After GIPn bit is cleared, the General Interrupt n request(if the MUB_GIER[GIEn] bit is set to "1") is<br>cleared on the MUB side.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GSR —<br>MU_1.MUB GSR —<br>MU_2.MUB — GSR<br>0b - MUB general purpose interrupt n is not pending.<br>1b - MUB general purpose interrupt n is pending.<br>13 MUB General Interrupt Request Pending n<br>GIP13 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• GIPn bit signals the MUB that the MUA_GCR[GIRn] bit was set from "0" to "1". If the<br>MUB_GIER[GIEn] bit is set to "1", a General Interrupt n request is issued to Processor B.<br>• The GIPn bit is cleared by writing "1". Writing "0" is ignored.<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1365 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

Field Function 

- GIPn bit is cleared when the MU resets. 

- After GIPn bit is cleared, the General Interrupt n request(if the MUB_GIER[GIEn] bit is set to "1") is cleared on the MUB side. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|GSR|—|
|MU_1.MUB|GSR|—|
|MU_2.MUB|—|GSR|



- 0b - MUB general purpose interrupt n is not pending. 

- 1b - MUB general purpose interrupt n is pending. 

12 

GIP12 

MUB General Interrupt Request Pending n 

- There are 32 General Purpose Interrupts (n = 0 to 31) 

- GIPn bit signals the MUB that the MUA_GCR[GIRn] bit was set from "0" to "1". If the MUB_GIER[GIEn] bit is set to "1", a General Interrupt n request is issued to Processor B. 

- The GIPn bit is cleared by writing "1". Writing "0" is ignored. 

- GIPn bit is cleared when the MU resets. 

- After GIPn bit is cleared, the General Interrupt n request(if the MUB_GIER[GIEn] bit is set to "1") is cleared on the MUB side. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|GSR|—|
|MU_1.MUB|GSR|—|
|MU_2.MUB|—|GSR|



- 0b - MUB general purpose interrupt n is not pending. 

1b - MUB general purpose interrupt n is pending. 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1366 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

Field Function 11 MUB General Interrupt Request Pending n GIP11 • There are 32 General Purpose Interrupts (n = 0 to 31) 

- GIPn bit signals the MUB that the MUA_GCR[GIRn] bit was set from "0" to "1". If the MUB_GIER[GIEn] bit is set to "1", a General Interrupt n request is issued to Processor B. 

- The GIPn bit is cleared by writing "1". Writing "0" is ignored. 

- GIPn bit is cleared when the MU resets. 

- After GIPn bit is cleared, the General Interrupt n request(if the MUB_GIER[GIEn] bit is set to "1") is cleared on the MUB side. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

||Instance|Field supported in|Field not supported in|
|---|---|---|---|
||MU_0.MUB|GSR|—|
||MU_1.MUB|GSR|—|
||MU_2.MUB|—|GSR|
||0b - MUB general purp<br>1b - MUB general purp|ose interrupt n is not pending.<br>ose interrupt n is pending.||
|10<br>GIP10|MUB General Interrupt Reque<br>• There are 32 General Pur<br>• GIPn bit signals the MUB<br>MUB_GIER[GIEn] bit is s<br>• The GIPn bit is cleared by|st Pending n<br>pose Interrupts (n = 0 to 31)<br>that the MUA_GCR[GIRn] bit was set<br>et to "1", a General Interrupt n reques<br>writing "1". Writing "0" is ignored.|from "0" to "1". If the<br>t is issued to Processor B.|




![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1367-11.png)


<!-- Start of picture text -->
MUB General Interrupt Request Pending n<br>• There are 32 General Purpose Interrupts (n = 0 to 31)<br>• GIPn bit signals the MUB that the MUA_GCR[GIRn] bit was set from "0" to "1". If the<br>MUB_GIER[GIEn] bit is set to "1", a General Interrupt n request is issued to Processor B.<br>• The GIPn bit is cleared by writing "1". Writing "0" is ignored.<br>• GIPn bit is cleared when the MU resets.<br>• After GIPn bit is cleared, the General Interrupt n request(if the MUB_GIER[GIEn] bit is set to "1") is<br>cleared on the MUB side.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GSR —<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1367 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1368-03.png)


<!-- Start of picture text -->
Field Function<br>Instance Field supported in Field not supported in<br>MU_1.MUB GSR —<br>MU_2.MUB — GSR<br>0b - MUB general purpose interrupt n is not pending.<br>1b - MUB general purpose interrupt n is pending.<br>9 MUB General Interrupt Request Pending n<br>GIP9 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• GIPn bit signals the MUB that the MUA_GCR[GIRn] bit was set from "0" to "1". If the<br>MUB_GIER[GIEn] bit is set to "1", a General Interrupt n request is issued to Processor B.<br>• The GIPn bit is cleared by writing "1". Writing "0" is ignored.<br>• GIPn bit is cleared when the MU resets.<br>• After GIPn bit is cleared, the General Interrupt n request(if the MUB_GIER[GIEn] bit is set to "1") is<br>cleared on the MUB side.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GSR —<br>MU_1.MUB GSR —<br>MU_2.MUB — GSR<br>0b - MUB general purpose interrupt n is not pending.<br>1b - MUB general purpose interrupt n is pending.<br>8 MUB General Interrupt Request Pending n<br>GIP8 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• GIPn bit signals the MUB that the MUA_GCR[GIRn] bit was set from "0" to "1". If the<br>MUB_GIER[GIEn] bit is set to "1", a General Interrupt n request is issued to Processor B.<br>• The GIPn bit is cleared by writing "1". Writing "0" is ignored.<br>• GIPn bit is cleared when the MU resets.<br>• After GIPn bit is cleared, the General Interrupt n request(if the MUB_GIER[GIEn] bit is set to "1") is<br>cleared on the MUB side.<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1368 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1369-03.png)


<!-- Start of picture text -->
Field Function<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GSR —<br>MU_1.MUB GSR —<br>MU_2.MUB — GSR<br>0b - MUB general purpose interrupt n is not pending.<br>1b - MUB general purpose interrupt n is pending.<br>7 MUB General Interrupt Request Pending n<br>GIP7 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• GIPn bit signals the MUB that the MUA_GCR[GIRn] bit was set from "0" to "1". If the<br>MUB_GIER[GIEn] bit is set to "1", a General Interrupt n request is issued to Processor B.<br>• The GIPn bit is cleared by writing "1". Writing "0" is ignored.<br>• GIPn bit is cleared when the MU resets.<br>• After GIPn bit is cleared, the General Interrupt n request(if the MUB_GIER[GIEn] bit is set to "1") is<br>cleared on the MUB side.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GSR —<br>MU_1.MUB GSR —<br>MU_2.MUB — GSR<br>0b - MUB general purpose interrupt n is not pending.<br>1b - MUB general purpose interrupt n is pending.<br>6 MUB General Interrupt Request Pending n<br>GIP6 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1369 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

- Field Function • GIPn bit signals the MUB that the MUA_GCR[GIRn] bit was set from "0" to "1". If the MUB_GIER[GIEn] bit is set to "1", a General Interrupt n request is issued to Processor B. 

   - The GIPn bit is cleared by writing "1". Writing "0" is ignored. 

   - GIPn bit is cleared when the MU resets. 

   - After GIPn bit is cleared, the General Interrupt n request(if the MUB_GIER[GIEn] bit is set to "1") is cleared on the MUB side. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|GSR|—|
|MU_1.MUB|GSR|—|
|MU_2.MUB|—|GSR|



0b - MUB general purpose interrupt n is not pending. 1b - MUB general purpose interrupt n is pending. 

5 MUB General Interrupt Request Pending n 

- GIP5 • There are 32 General Purpose Interrupts (n = 0 to 31) 

   - GIPn bit signals the MUB that the MUA_GCR[GIRn] bit was set from "0" to "1". If the MUB_GIER[GIEn] bit is set to "1", a General Interrupt n request is issued to Processor B. 

   - The GIPn bit is cleared by writing "1". Writing "0" is ignored. 

   - GIPn bit is cleared when the MU resets. 

   - After GIPn bit is cleared, the General Interrupt n request(if the MUB_GIER[GIEn] bit is set to "1") is cleared on the MUB side. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

|Instance|Field supported in|Field not supported in|
|---|---|---|
|MU_0.MUB|GSR|—|
|MU_1.MUB|GSR|—|
|MU_2.MUB|—|GSR|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1370 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 

|Field|Function|||
|---|---|---|---|
||Instance|Field supported in|Field not supported in|
||0b - MUB general purpose<br>1b - MUB general purpose|interrupt n is not pending.<br>interrupt n is pending.||
|4<br>GIP4|MUB General Interrupt Request<br>• There are 32 General Purpo<br>• GIPn bit signals the MUB tha<br>MUB_GIER[GIEn] bit is set t<br>• The GIPn bit is cleared by wr<br>• GIPn bit is cleared when the<br>• After GIPn bit is cleared, the<br>cleared on the MUB side.<br>This field is not suppor<br>supported registers.|Pending n<br>se Interrupts (n = 0 to 31)<br>t the MUA_GCR[GIRn] bit was set<br>o "1", a General Interrupt n reques<br>iting "1". Writing "0" is ignored.<br>MU resets.<br>General Interrupt n request(if the<br>ted in every instance. The following tab<br>~~NOTE~~|from "0" to "1". If the<br>t is issued to Processor B.<br>MUB_GIER[GIEn] bit is set to "1") is<br>le includes only|
||Instance|Field supported in|Field not supported in|
||MU_0.MUB|GSR|—|
||MU_1.MUB|GSR|—|
||MU_2.MUB|—|GSR|
||0b - MUB general purpose<br>1b - MUB general purpose|interrupt n is not pending.<br>interrupt n is pending.||
|3<br>GIP3|MUB General Interrupt Request<br>• There are 32 General Purpo<br>• GIPn bit signals the MUB tha<br>MUB_GIER[GIEn] bit is set t<br>• The GIPn bit is cleared by wr<br>• GIPn bit is cleared when the<br>• After GIPn bit is cleared, the<br>cleared on the MUB side.<br>This field is not suppor<br>supported registers.|Pending n<br>se Interrupts (n = 0 to 31)<br>t the MUA_GCR[GIRn] bit was set<br>o "1", a General Interrupt n reques<br>iting "1". Writing "0" is ignored.<br>MU resets.<br>General Interrupt n request(if the<br>ted in every instance. The following tab<br>~~NOTE~~|from "0" to "1". If the<br>t is issued to Processor B.<br>MUB_GIER[GIEn] bit is set to "1") is<br>le includes only|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1371 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1372-03.png)


<!-- Start of picture text -->
Field Function<br>Instance Field supported in Field not supported in<br>MU_0.MUB GSR —<br>MU_1.MUB GSR —<br>MU_2.MUB — GSR<br>0b - MUB general purpose interrupt n is not pending.<br>1b - MUB general purpose interrupt n is pending.<br>2 MUB General Interrupt Request Pending n<br>GIP2 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• GIPn bit signals the MUB that the MUA_GCR[GIRn] bit was set from "0" to "1". If the<br>MUB_GIER[GIEn] bit is set to "1", a General Interrupt n request is issued to Processor B.<br>• The GIPn bit is cleared by writing "1". Writing "0" is ignored.<br>• GIPn bit is cleared when the MU resets.<br>• After GIPn bit is cleared, the General Interrupt n request(if the MUB_GIER[GIEn] bit is set to "1") is<br>cleared on the MUB side.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GSR —<br>MU_1.MUB GSR —<br>MU_2.MUB — GSR<br>0b - MUB general purpose interrupt n is not pending.<br>1b - MUB general purpose interrupt n is pending.<br>1 MUB General Interrupt Request Pending n<br>GIP1 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• GIPn bit signals the MUB that the MUA_GCR[GIRn] bit was set from "0" to "1". If the<br>MUB_GIER[GIEn] bit is set to "1", a General Interrupt n request is issued to Processor B.<br>• The GIPn bit is cleared by writing "1". Writing "0" is ignored.<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1372 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1373-03.png)


<!-- Start of picture text -->
Field Function<br>• GIPn bit is cleared when the MU resets.<br>• After GIPn bit is cleared, the General Interrupt n request(if the MUB_GIER[GIEn] bit is set to "1") is<br>cleared on the MUB side.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>MU_0.MUB GSR —<br>MU_1.MUB GSR —<br>MU_2.MUB — GSR<br>0b - MUB general purpose interrupt n is not pending.<br>1b - MUB general purpose interrupt n is pending.<br>0 MUB General Interrupt Request Pending n<br>GIP0 • There are 32 General Purpose Interrupts (n = 0 to 31)<br>• GIPn bit signals the MUB that the MUA_GCR[GIRn] bit was set from "0" to "1". If the<br>MUB_GIER[GIEn] bit is set to "1", a General Interrupt n request is issued to Processor B.<br>• The GIPn bit is cleared by writing "1". Writing "0" is ignored.<br>• GIPn bit is cleared when the MU resets.<br>• After GIPn bit is cleared, the General Interrupt n request(if the MUB_GIER[GIEn] bit is set to "1") is<br>cleared on the MUB side.<br>0b - MUB general purpose interrupt n is not pending.<br>1b - MUB general purpose interrupt n is pending.<br><!-- End of picture text -->

#### 39.6.2.13 Transmit Control Register (TCR) 

##### Offset 

|Register|Offset|
|---|---|
|TCR|120h|



##### Function 

The TCR register contains the MUB transmit interrupt enables. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1373 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||0|||||||TIE3|TIE2|TIE1|TIE0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-4|Reserved|
|—||
|3-0|MUB Transmit Interrupt Enable n|
|TIEn|• There are 4 Transmit Interrupts (n = 0 to 3)<br>• If TIEn bit is set to "1", then an MUB Transmit Interrupt n request is issued when the MUB_TSR[TEn]<br>bit is set to "1".|
||• If TIEn bit is cleared, then the value of the TEn bit is ignored and no MUB Transmit Interrupt n<br>request is issued.|
||• TIEn bit is cleared when the MU resets.|
||0b - Disables MUB Transmit Interrupt n. (default)|
||1b - Enables MUB Transmit Interrupt n.|



#### 39.6.2.14 Transmit Status Register (TSR) 

##### Offset 

|Register|Offset|
|---|---|
|TSR|124h|



##### Function 

The TSR register shows whether the MUB transmit registers are empty or not. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1374 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||||0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||0|||||||TE3|TE2|TE1|TE0|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|



##### Fields 

|Field|Function|
|---|---|
|31-4|Reserved|
|—||
|3-0|MUB Transmit Register n Empty|
|TEn|• There are 4 Transmit Registers (n = 0 to 3)<br>• The TEn bit is set to "1" after the MUA RRn register is read on the MUA side.<br>• After the TEn bit is set to "1", it signals the MUB side that the MUB TRn register is ready<br>to be written on the MUB side, and a Transmit n interrupt is issued on the MUB side (if the<br>MUB_TCR[TIEn] bit is set to "1").<br>• TEn bit is cleared after the MUB TRn register is written on the MUB side.<br>• After TEn bit is cleared, the Transmit n interrupt(if the MUB_TCR[TIEn] bit is set to "1") is cleared on<br>the MUB side.<br>• TEn bit is set to "1" when the MU resets.<br>0b - MUB TRn register is not empty.<br>1b - MUB TRn register is empty.|



#### 39.6.2.15 Receive Control Register (RCR) 

##### Offset 

|Register|Offset|
|---|---|
|RCR|128h|



##### Function 

The RCR register contains the MUB receive interrupt enables. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1375 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||0|||||||RIE3|RIE2|RIE1|RIE0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-4|Reserved|
|—||
|3-0|MUB Receive Interrupt Enable n|
|RIEn|• There are 4 Transmit Interrupts (n = 0 to 3)<br>• If RIEn bit is set to "1", then an MUB Receive Interrupt n request is issued when the MUB_RSR[RFn]<br>bit is set to "1".|
||• If RIEn bit is cleared, then the value of the RFn bit is ignored and no MUB Receive Interrupt n<br>request is issued.|
||• RIEn bit is cleared when the MU resets.|
||0b - Disables MUB Receive Interrupt n.|
||1b - Enables MUB Receive Interrupt n.|



#### 39.6.2.16 Receive Status Register (RSR) 

##### Offset 

|Register|Offset|
|---|---|
|RSR|12Ch|



##### Function 

The RSR register shows whether the MUB receive registers are full or not. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1376 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||||0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||0|||||||RF3|RF2|RF1|RF0|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-4|Reserved|
|—||
|3-0|MUB Receive Register n Full|
|RFn|• There are 4 Receive Registers (n = 0 to 3)<br>• The RFn bit is set to "1" when the MUA TRn register is written on the MUA side.<br>• After the RFn bit is set to "1", the RFn bit signals the MUB side that new data in the MUB RRn<br>register is ready to be read by the MUB, and a Receive n interrupt is issued on the MUB side (if the<br>MUB_RCR[RIEn] has been set to "1").<br>• RFn bit is cleared when the MUB RRn register is read, or when the MU is reset.<br>• After RFn bit is cleared, the Receive n interrupt(if the MUB_RCR[RIEn] has been set to "1") is<br>cleared on the MUB side.<br>0b - MUB RRn register is not full.<br>1b - MUB RRn register has received data from MUA TRn register and is ready to be read by the<br>MUB.|



#### 39.6.2.17 Transmit Register (TR0 - TR3) 

##### Offset 

|Register|Offset|
|---|---|
|TR0|200h|
|TR1|204h|
|TR2|208h|
|TR3|20Ch|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1377 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Function 

##### MUB Transmit Data. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/039_Messaging_Unit_-MU-/S32K3XXRM_数据表.pdf-1378-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>TR_DATA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>TR_DATA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

- Field Function 31-0 MUB Transmit Data 

- TR_DATA • Data written to the TRn register is reflected in the MUA Receive Register n (RRn). The TRn and RRn registers are not double-buffered, a write to the TRn register overrides the data readable at the RRn register. 

- • A write to the transmit register clears the MUB_TSR[TEn] bit on the transmitter side, and sets the MUA_RSR[RFn] bit on the receiver side. 

- • TRn register can be written only when the MUB_TSR[TEn] bit is set to "1". • Reading the TRn register returns all zeros. 

#### 39.6.2.18 Receive Register (RR0 - RR3) 

##### Offset 

|Register|Offset|
|---|---|
|RR0|280h|
|RR1|284h|
|RR2|288h|
|RR3|28Ch|



Function 

MUB Receive Data. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1378 / 4640 

NXP Semiconductors 

Messaging Unit (MU) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||RR_D|ATA||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||RR_D|ATA||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-0|MUB Receive Data|
|RR_DATA|• Reflects the data written to MUA Transmit Register (TRn).|
||• Reading the RRn register clears the MUB_RSR[RFn] bit on the receiver side, and sets the<br>MUA_TSR[TEn] bit on the transmitter side.|



- RRn register can be read only when the MUA_RSR[RFn] bit is set to "1". Reading before MUA_RSR[RFn]=1 may result in reading incorrect data. Therefore, polling the MUA_RSR[RFn] bit to confirm it is set to "1" before reading RRn is required. 

- Writing to the RRn register generates an error response to the MUB. 

## 39.7 Glossary 

EP Event Pending GIR General purpose Interrupt Request GIP General purpose Interrupt Pending MUR Messaging Unit Reset NMI Non-Maskable Interrupt RF Receiver Full RFP Receive Full Pending TE Transmitter Empty TEP Transmit Empty Pending 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1379 / 4640 

