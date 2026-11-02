NXP Semiconductors 

# Chapter 72 CAN (FlexCAN) 

72.1 Chip-specific FlexCAN information 

### 72.1.1 FlexCAN instances and configuration 

This chip contains up to 8 instances of FlexCAN: 

- FlexCAN_0 

- FlexCAN_1 

- FlexCAN_2 

- FlexCAN_3 

- FlexCAN_4 

- FlexCAN_5 

- FlexCAN_6 

- FlexCAN_7 

~~<mark>NOTE</mark>~~ 

The availability of 'Interrupt Masks 3 Register (IMASK3)' and 'Interrupt Flags 3 Register (IFLAG3)' registers for an instance depends upon the number of message buffers supported. See Table 435 for details. 

Table 435. FlexCAN configuration and instances 

|Chip|Instances|Flexible<br>Data Rate<br>(CAN FD)<br>protocol<br>specification<br>and CAN<br>protocol.|Number of<br>message<br>buffers<br>(assuming<br>8B payload)|Rx FIFO ID<br>Filtering|ECC|External tick<br>time|DMA|Enhanced<br>RX FIFO<br>feature<br>(size)|
|---|---|---|---|---|---|---|---|---|
|S32K358|FlexCAN_0|Yes|96|Yes|Yes|Yes<br>(PIT_RTI_2)|Yes|Yes (20)|
||FlexCAN_1|Yes|96|Yes|Yes|Yes<br>(PIT_RTI_2)|Yes|Yes (20)|
||FlexCAN_2|Yes|96|Yes|Yes|Yes<br>(PIT_RTI_2)|Yes|Yes (20)|
||FlexCAN_3|Yes|64|Yes|Yes|Yes<br>(PIT_RTI_2)|Yes|No|
||FlexCAN_4|Yes|64|Yes|Yes|Yes<br>(PIT_RTI_2)|Yes|No|
||FlexCAN_5|Yes|64|Yes|Yes|Yes<br>(PIT_RTI_2)|Yes|No|
||FlexCAN_6|Yes|64|Yes|Yes|Yes<br>(PIT_RTI_2)|Yes|No|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2716 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table 435. FlexCAN configuration and instances (continued) 

|Chip|Instances|Flexible<br>Data Rate<br>(CAN FD)<br>protocol<br>specification<br>and CAN<br>protocol.|<br>Number of<br>message<br>buffers<br>(assuming<br>8B payload)|Rx FIFO ID<br>Filtering|<br>ECC|External tick<br>time|DMA|Enhanced<br>RX FIFO<br>feature<br>(size)|
|---|---|---|---|---|---|---|---|---|
||FlexCAN_7|Yes|64|Yes|Yes|Yes<br>(PIT_RTI_2)|Yes|No|
|S32K314,<br>S32K324,<br>|FlexCAN_0|Yes|96|Yes|Yes|Yes<br>(PIT_RTI_2)|Yes|Yes (20)|
|S32K344|FlexCAN_1|Yes|64|Yes|Yes|Yes<br>(PIT_RTI_2)|Yes|No|
||FlexCAN_2|Yes|64|Yes|Yes|Yes<br>(PIT_RTI_2)|Yes|No|
||FlexCAN_3|Yes|32|Yes|Yes|Yes<br>(PIT_RTI_2)|Yes|No|
||FlexCAN_4|Yes|32|Yes|Yes|Yes<br>(PIT_RTI_2)|Yes|No|
||FlexCAN_5|Yes|32|Yes|Yes|Yes<br>(PIT_RTI_2)|Yes|No|
|S32K322,<br>S32K342|FlexCAN_0|Yes|64|Yes|Yes|Yes<br>(PIT_RTI_2)|Yes|Yes (20)|
||FlexCAN_1|Yes|64|Yes|Yes|Yes<br>(PIT_RTI_2)|Yes|No|
||FlexCAN_2|Yes|64|Yes|Yes|Yes<br>(PIT_RTI_2)|Yes|No|
||FlexCAN_3|Yes|32|Yes|Yes|Yes<br>(PIT_RTI_2)|Yes|No|
|S32K312|FlexCAN_0|Yes|64|Yes|Yes|Yes<br>(PIT_RTI_1)|Yes|Yes (20)|
||FlexCAN_1|Yes|64|Yes|Yes|Yes<br>(PIT_RTI_1)|Yes|No|
||FlexCAN_2|Yes|64|Yes|Yes|Yes<br>(PIT_RTI_1)|Yes|No|
||FlexCAN_3|Yes|32|Yes|Yes|Yes<br>(PIT_RTI_1)|Yes|No|
||FlexCAN_4|Yes|32|Yes|Yes|Yes<br>(PIT_RTI_1)|Yes|No|
||FlexCAN_5|Yes|32|Yes|Yes|Yes<br>(PIT_RTI_1)|Yes|No|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2717 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table 435. FlexCAN configuration and instances (continued) 

|Chip|Instances|Flexible<br>Data Rate<br>(CAN FD)<br>protocol<br>specification<br>and CAN<br>protocol.|Number of<br>message<br>buffers<br>(assuming<br>8B payload)|Rx FIFO ID<br>Filtering|ECC|External tick<br>time|DMA|Enhanced<br>RX FIFO<br>feature<br>(size)|
|---|---|---|---|---|---|---|---|---|
|S32K311|FlexCAN_0|Yes|64|Yes|Yes|Yes<br>(PIT_RTI_1)|Yes|Yes (20)|
||FlexCAN_1|Yes|64|Yes|Yes|Yes<br>(PIT_RTI_1)|Yes|No|
||FlexCAN_2|Yes|64|Yes|Yes|Yes<br>(PIT_RTI_1)|Yes|No|



~~<mark>NOTE</mark>~~ 

See attached interrupt map file for the vector numbers for the CAN instances and their corresponding interrupt sources. 

### 72.1.2 FlexCAN error injection 

##### Error injection address mapping 

Use the following table to convert from the memory map address to the location in the physical FlexCAN RAM (where pairs of values are provided, the first is the address for MCR[FDEN] negated, the second is for MCR[FDEN] asserted): 

|RAM contents|Memory map|||Injection addres|s||
|---|---|---|---|---|---|---|
|—|—|FlexCAN0|FlexCAN0|FlexCAN1/2|FlexCAN3|FlexCAN4/5|
|||S32K344|S32K342|S32K3xx|S32K344|S32K344|
|||S32K324|S32K322||S32K324|S32K324|
|||S32K314|S32K312||S32K314|S32K314|
||||S32K311||S32K342|S32K312|
||||||S32K322||
||||||S32K312||
|FlexCAN Registers|—|Not mapped|Not mapped|Not mapped|Not mapped|Not mapped|
|MBs|0080h|0000h|0000h|0000h|0000h|0000h|
|RXIMRs|0880h|600h|400h|400h|200h|200h|
|RXIFR_0|0A80h|780h|500h|500h|280h|280h|
|RXIFR_1|0A84h|784h|504h|504h|284h|284h|
|RXIFR_2|0A88h|788h|508h|508h|288h|288h|
|RXIFR_3|0A8Ch|78Ch|50Ch|50Ch|28Ch|28Ch|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2718 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|RAM contents|Memory map|||Injection addre|ss||
|---|---|---|---|---|---|---|
|RXIFR_4|0A90h|790h|510h|510h|290h|290h|
|RXIFR_5|0A94h|794h|514h|514h|294h|294h|
|Reserved|0A98h|—|—|—|—|—|
|RXMGMASK|0AA0h|7A0h|520h|520h|2A0h|2A0h|
|RXFGMASK|0AA4h|7A4h|524h|524h|2A4h|2A4h|
|RX14MASK|0AA8h|7A8h|528h|528h|2A8h|2A8h|
|RX15MASK|0AACh|7ACh|52Ch|52Ch|2ACh|2Ach|
|Tx_SMB|0AB0h/0F28h|7B0h|530h|530h|2B0h|2B0h|
|Rx_SMB0|0AC0h/0F70h|7C0h/7F8h|540h/578h|540h/578h|2C0h/2F8h|2C0h/2F8h|
|Rx_SMB1|0AD0h/0FB8h|7D0h/840h|550h/5C0h|550h/5C0h|2D0h/340h|2D0h/340h|
|Rx_SMB0_TIME_STA<br>MP|0C20h|888h|608h|608h|388h|388h|
|Rx_SMB1_TIME_STA<br>MP|0C24h|88Ch|60Ch|60Ch|38Ch|38Ch|
|HR_TIME_STAMP|0C30h|890h|610h|610h|390h|390h|
|Enhanced RX FIFO|2000h|A10h|710h|—|—|—|
|ERFFEL|3000h|1050h|D50h|—|—|—|



##### FlexCAN memory initialization 

All FlexCAN memory must be initialized before starting its operation in order to have the parity bits in memory properly updated. CTRL2[WRMFRZ] grants write access to all memory positions that require initialization. 

These locations are as listed in this table from 080h–ADFh and from C20h–31FFh.: 

|Chip|Instance|Offset address ranges to be initialized|
|---|---|---|
|S32K344, S32K324, S32K314|FlexCAN0|080h–ADFh; C20h–31FFh|
||FlexCAN1–FlexCAN5|080h–ADFh; C20h–FFFh|
|S32K342, S32K322|FlexCAN0|080h–ADFh; C20h–31FFh|
||FlexCAN1–FlexCAN3|080h–ADFh; C20h–FFFh|
|S32K312|FlexCAN0|080h–DFh; C20h–31FFh|
||FlexCAN1–FlexCAN5|080h–ADFh; C20h–FFFh|
|S32K311|FlexCAN0|080h–ADFh; C20h–31FFh|
||FlexCAN1–FlexCAN2|080h–ADFh; C20h–FFFh|



~~<mark>NOTE</mark>~~ 

The reset value of CAN0_CTRL2 register for S32K312 and S32K342 is 0080_0000h. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2719 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

### 72.1.3 Reset value of MDIS bit 

The CAN_MCR[MDIS] bit is set to 1 when the module is reset. Therefore, FlexCAN module is disabled following a reset. For details of CAN_MCR[MDIS] register refer to "CAN register description" section. 

### 72.1.4 CAN Timestamp Implementation 

FlexCAN uses Ethernet Media Access Controller (EMAC) and System Timer Module (STM_0) counters as time source. For details see 'FlexCAN timestamp implementation' section in Clocking chapter. 

#### 72.1.4.1 Considerations while using FlexCAN timestamp in S32K344 

While using FlexCAN timestamp feature, the message buffers should be unlocked within each 20 CAN bits. A failure to do so while using FlexCAN timestamp feature alongwith FlexCAN RX FIFO or enhanced RX FIFO might result in timestamp information being missed. 

### 72.1.5 CAN clock setup 

For clock setup, see Clocking chapter. 

## 72.2 Overview 

The FlexCAN module is a communication controller implementing the CAN protocol according to the ISO 11898-1:2015 standard and CAN 2.0 B protocol specifications. 

The CAN protocol was primarily designed to be used as a vehicle serial data bus, meeting the specific real-time processing and reliable operation requirements in the EMI environment of a vehicle. The FlexCAN module is a full implementation of the CAN protocol specification, the CAN with Flexible Data rate (CAN FD) protocol, and the CAN 2.0 version B protocol, which supports both standard and extended message frames and long payloads. 

~~<mark>NOTE</mark>~~ Legacy Rx FIFO cannot be used in FD mode. 

~~<mark>NOTE</mark>~~ In CAN FD mode, the Enhanced Rx FIFO feature should be used instead of Legacy Rx FIFO. 

### 72.2.1 Block diagram 

A general block diagram is shown in Figure 376, which describes the main subblocks implemented in the FlexCAN module. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2720 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2721-02.png)


<!-- Start of picture text -->
Peripheral Bus Interface<br>Address, Data, Clocks, Interrupts<br>Bus InterfaceUnit<br>Message<br>BIU<br>Buffers<br>Registers (MBs)<br>   Controller   RAM<br>Host Interface (CHI)<br>Tx Rx<br>Arbitration Matching<br>Protocol Engine (PE)<br>CAN Tx CAN Rx FlexCAN<br>CAN Transceiver<br>CAN Bus<br><!-- End of picture text -->

Figure 376. FlexCAN block diagram 

The Protocol Engine (PE) submodule manages the serial communication on the CAN bus: 

- Requesting RAM access for receiving and transmitting message frames 

- Validating received messages 

- Performing error handling 

- Detecting CAN FD messages 

The Controller Host Interface (CHI) submodule manages message buffer selection for reception and transmission, taking care of arbitration and ID matching algorithms for both CAN FD and non-CAN FD message formats. 

The Bus Interface Unit (BIU) submodule controls access to and from the internal interface bus, in order to establish connection to the CPU and to other blocks. Clocks, address and data buses, interrupt outputs, DMA and test signals are accessed through the BIU. 

### 72.2.2 Features 

The FlexCAN module includes these distinctive features: 

- Full implementation of the CAN with Flexible Data Rate (CAN FD) protocol specification and CAN protocol specification, Version 2.0 B 

   - Standard data frames 

   - Extended data frames 

   - Zero to sixty four bytes data length 

   - Programmable bit rate (see the chip-specific FlexCAN information for the specific maximum rate configuration) 

   - Content-related addressing 

- Compliant with the ISO 11898-1:2015 standard 

- Flexible mailboxes configurable to store 0 to 8, 16, 32, or 64 bytes data length 

- Each mailbox configurable as receive or transmit, all supporting standard and extended messages 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2721 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

- Individual Rx Mask registers per mailbox 

- Full-featured legacy Rx FIFO with storage capacity for up to six frames and automatic internal pointer handling with DMA support 

- Full-featured enhanced Rx FIFO with storage capacity for up to 20 CAN FD frames and automatic internal pointer handling with DMA support 

- Transmission abort capability 

- Flexible message buffers (MBs), totaling 96 message buffers of 8 bytes data length each, configurable as Rx or Tx 

- RAM not used by reception or transmission structures can be used as general purpose RAM space 

- Listen-Only mode capability 

- Programmable Loop-Back mode supporting self-test operation 

- Programmable transmission priority scheme: lowest ID, lowest buffer number, or highest priority 

- Time stamp based on 32-bit free running timer, with an optional external time tick 

- Global network time, synchronized by a specific message 

- Maskable interrupts 

- Independence from the transmission medium (an external transceiver is assumed) 

- Short latency time due to an arbitration scheme for high-priority messages 

- Low power mode 

- Transceiver delay compensation feature when transmitting CAN FD messages at faster data rates 

- Remote request frames may be managed automatically or by software 

- CAN bit time settings and configuration bits can only be written in Freeze mode 

- Tx mailbox status (Lowest priority buffer or empty buffer) 

- Identifier Acceptance Filter Hit Indicator (IDHIT) register for received frames 

- SYNCH bit available in Error in Status 1 register to indicate that the module is synchronous with CAN bus 

- CRC status for transmitted message 

- Legacy Rx FIFO Global Mask register 

- Selectable priority between mailboxes and Rx FIFO during matching process 

- Powerful legacy Rx FIFO ID filtering, capable of matching incoming IDs against either 128 extended, 256 standard, or 512 partial (8 bit) IDs, with up to 32 individual masking capability 

- Powerful Enhanced Rx FIFO ID filtering, capable of matching incoming IDs against either 64 extended or 128 standard ID filter elements with three filtering schemes: mask + filter, range, and two filters without mask. 

- 100% backward compatibility with previous FlexCAN version 

- Supports detection and correction of errors in memory read accesses 

Each byte of FlexCAN memory is associated to 5 parity bits, and the error correction mechanism ensures that in this 13-bit word, errors in one bit can be corrected (correctable errors) and errors in 2 bits can be detected but not corrected (non-correctable errors). 

## 72.3 Functional description 

The FlexCAN module is a CAN protocol engine with a very flexible mailbox system for transmitting and receiving CAN frames. The mailbox system is composed of a set of message buffers (MB) that store configuration and control data, time stamp, message ID, and data (see Message buffer structure). The memory corresponding to the first 38 MBs can be configured to support a Legacy 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2722 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

FIFO reception scheme with a powerful ID filtering mechanism, capable of checking incoming frames against a table of IDs (up to 128 extended IDs or 256 standard IDs or 512 8-bit ID slices), with individual mask register for up to 32 ID filter table elements. 

For Classical CAN frames, simultaneous reception through Legacy FIFO and mailbox is supported. For CAN FD frames, reception is supported through mailboxes and Enhanced Rx FIFO. For mailbox reception, a matching algorithm makes it possible to store received frames only into MBs that have the same ID programmed in the ID field. A masking scheme makes it possible to match the ID programmed on the MB with a range of IDs on received CAN frames. For transmission, an arbitration algorithm decides the prioritization of MBs to be transmitted based on the message ID (optionally augmented by 3 local priority bits) or the MB ordering. 

Before proceeding with the functional description, an important concept must be explained. A message buffer is said to be active at a given time if it can participate in both the matching and arbitration processes. An Rx MB with a 0b code is inactive (see Table 469). Similarly, a Tx MB with a 1000b or 1001b code is also inactive (see Table 470). 

The FlexCAN module is also able to receive and transmit messages in CAN FD format. The message buffers are sized to adequately store the quantity of data bytes selected by the FDCTRL[MBDSRn] fields. The quantity of FD MBs available for a given quantity of data bytes is described in the FDCTRL register. See also FlexCAN memory partition for CAN FD. 

### 72.3.1 Modes of operation 

The FlexCAN module has these functional modes: 

- Normal mode (User or Supervisor): 

In Normal mode, the module operates receiving and/or transmitting message frames, errors are managed normally, and all CAN Protocol functions are enabled. User and Supervisor modes differ in the access to some restricted control registers. 

- Freeze mode: 

Freeze mode is enabled when MCR[FRZ] is asserted. If enabled, Freeze mode is entered when MCR[HALT] is set or when is requested at chip level and MCR[FRZ_ACK ] is asserted by the FlexCAN. In this mode, no transmission or reception of frames is done and synchronicity to the CAN bus is lost. See Freeze mode for more information. 

- Loop-Back mode: 

The module enters this mode when CTRL1[LPB] is asserted. In this mode, FlexCAN performs an internal loop back that can be used for self-test operation. The bit stream output of the transmitter is internally fed back to the receiver input. The Rx CAN input pin is ignored and the Tx CAN output goes to the recessive state (logic '1'). FlexCAN behaves as it normally does when transmitting and treats its own transmitted message as a message received from a remote node. In this mode, FlexCAN ignores the bit sent during the ACK slot in the CAN frame acknowledge field to ensure proper reception of its own message. Both transmit and receive interrupts are generated. 

- Listen-Only mode: 

The module enters this mode when CTRL1[LOM] is asserted. In this mode, transmission is disabled, all error counters are frozen, and the module operates in a CAN Error Passive mode. Only messages acknowledged by another CAN station will be received. If FlexCAN detects a message that has not been acknowledged, it will flag a BIT0 error (without changing the REC), as if it was trying to acknowledge the message. 

- CAN FD Active mode: 

In this mode, FlexCAN is capable of transmitting and receiving all messages formatted according to the CAN FD Standard (2.0) and 2.0B Protocol in an interleaved fashion. The CPU can set the FlexCAN into CAN FD Active mode by configuring MCR[FDEN] in Freeze mode. 

It is important to know which features are available in CAN FD active mode. This table lists the differences between FD and classical modes. 

Table 436. Differences between CAN classical and CAN FD 

|Feature|CAN classical|CAN FD|
|---|---|---|
|Legacy Rx FIFO DMA|Yes|No|
||Table continues on the next page...||



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2723 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table 436. Differences between CAN classical and CAN FD (continued) 

|Feature|CAN classical|CAN FD|
|---|---|---|
|Legacy Rx FIFO|Yes|No|
|Enhanced Rx FIFO DMA|Yes|Yes|
|Enhanced Rx FIFO|Yes|Yes|



For low-power operation, the FlexCAN module has: 

- Module Disable mode: 

This low-power mode is entered when MCR[MDIS] is asserted by the CPU and MCR[LPM_ACK] is asserted by FlexCAN. When disabled, the module issues a request to disable the clocks to the CAN Protocol Engine and Controller Host Interface submodules. Exit from this mode is done by negating MCR[MDIS]. See Module Disable mode for more information. 

#### 72.3.1.1 Modes of operation details 

The FlexCAN module has functional modes and low-power modes. See Modes of operation for an introductory description of all the modes of operation. The following sub-sections contain functional details on Freeze mode and the low-power modes. 

~~<mark>CAUTION</mark>~~ 

"Permanent Dominant" failure on CAN Bus line is not supported by FlexCAN. If a Low-Power request or Freeze mode request is done during a "Permanent Dominant", the corresponding acknowledge can never be asserted. 

#### 72.3.1.1.1 Freeze mode 

This mode is requested either by the CPU through the assertion of MCR[HALT] or when the chip is put into Debug mode. In both cases it is also necessary that MCR[FRZ] be asserted and the module not be in a low-power mode. This mode is also requested by FlexCAN through the automatic assertion of both MCR[HALT] and MCR[FRZ] when MECR[NCEFAFRZ] is set and a non-correctable error is detected in a memory read access performed by FlexCAN internal processes (see Response to errors). 

The acknowledgement is obtained through the assertion by the FlexCAN of MECR[FRZ_ACK]. The CPU must only consider the FlexCAN in Freeze mode when both request and acknowledgement conditions are satisfied. 

When Freeze mode is requested, FlexCAN does the following: 

- Waits to be in either Intermission, Passive Error, Bus Off, or Idle state. 

- Waits for all internal activities like arbitration, matching, move-in, and move-out to finish. A pending move-in does not prevent entering Freeze mode. 

- Ignores the Rx input pin and drives the Tx pin as recessive. 

- Stops the prescaler, thus halting all CAN protocol activities. 

- Grants write access to the Error Counters register, which is read-only in other modes. 

- Sets MCR[NOTRDY] and MCR[FRZACK]. 

After requesting Freeze mode, the user must wait for MCR[FRZ_ACK] to be asserted before executing any other action; otherwise FlexCAN may operate in an unpredictable way. In Freeze mode, all memory-mapped registers are accessible. 

Exiting Freeze mode is done in one of the following ways: 

- CPU negates MCR[FRZ]. 

- The chip is removed from Debug mode and/or the HALT bit is negated. 

MCR[FRZ_ACK] is negated after the protocol engine recognizes the negation of the freeze request. When out of Freeze mode, FlexCAN tries to resynchronize to the CAN bus by waiting for 11 consecutive recessive bits. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2724 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

#### 72.3.1.1.2 Module Disable mode 

This low-power mode is normally used to temporarily disable a complete FlexCAN block, with no power consumption. It is requested by the CPU through the assertion of MCR[MDIS], and the acknowledgement is obtained through the assertion by the FlexCAN of MCR[LPMACK]. The CPU must only consider the FlexCAN in Disable mode when both request and acknowledgement conditions are satisfied. 

If the module is disabled during Freeze mode, it requests to disable the clocks to the PE and CHI submodules, sets MCR[LPMACK] and negates MCR[FRZACK]. 

If the module is disabled during transmission or reception, FlexCAN does the following: 

- Waits to be in either Idle or Bus Off state, or else waits for the third bit of Intermission and then checks it to be recessive. 

- Waits for all internal activities like arbitration, matching, move-in, and move-out to finish. A pending move-in is not taken into account. 

- Ignores its Rx input pin and drives its Tx pin as recessive. 

- Shuts down the clocks to the PE and CHI submodules 

- Sets MCR[NOTRDY] and MCR[LPMACK]. 

The Bus Interface Unit continues to operate, enabling the CPU to access memory-mapped registers, except the Rx Mailboxes Global Mask registers, the Rx Buffer 14 Mask register, the Rx Buffer 15 Mask register, the Legacy Rx FIFO Global Mask register. The Legacy Rx FIFO Information register, the message buffers, the Rx Individual Mask registers, and the reserved words within RAM may not be accessed when the module is in Disable mode. Exiting from this mode is done by negating the MDIS bit by the CPU, which causes the FlexCAN to request to resume the clocks and negate the LPMACK bit after the CAN protocol engine recognizes the negation of disable mode requested by the CPU. 

### 72.3.2 Transmit process 

To transmit a CAN frame, the CPU must prepare a message buffer for transmission by executing the following procedure: 

1. Check whether the respective interrupt bit is set and clear it. 

2. If the MB is active (transmission pending), write the ABORT code (1001b) to the CODE field of the Control and Status word to request an abort of the transmission. 

3. Wait for the corresponding IFLAG bit to be asserted by polling the IFLAG register, or by the interrupt request if enabled by the respective IMASK bit. 

4. Read back the CODE field to check if the transmission was aborted or transmitted (see Transmission abort mechanism). 

5. Clear the corresponding interrupt flag. 

6. Write the ID register (containing the local priority if enabled via MCR[LPRIO_EN]). 

7. Write payload data bytes. 

8. Configure the Control and Status word with the desired configuration. 

   - a. Set ID type via MB_CS[IDE]. 

   - b. Set Remote Transmission Request (if needed) via MB_CS[RTR]. 

   - c. If MCR[FDEN] is enabled, also configure the MB_CS[EDL] and MB_CS[BRS] fields. For details about the relationship between the written value and transmitted value of the MB_CS[ESI] field, see Table 447.<sup>[7]</sup> 

   - d. Set Data Length Code in bytes via MB_CS[DLC]. See Table 472 for detailed information. 

   - e. Activate the message buffer to transmit the CAN frame by setting MB_CS[CODE] to Ch. 

- [7] The ESI field does not need to be written, and will automatically be transmitted dominant by error active nodes and recessive by error passive nodes. Note that there is an exception if the FlexCAN is operating as a network gateway: In that case, the CPU writes the MB_CS[ESI] bit according to the error status of the node which sent the message. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2725 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

~~<mark>NOTE</mark>~~ 

It is strongly recommended that all the fields in MB_CS word be configured in only one 32-bit write operation to maximize software performance. If the fields are configured in separate writes, the MB_CS[CODE] must be the last write in the C/S word. 

When the MB is activated, it participates in the arbitration process and is eventually transmitted according to its priority. When the DLC value stored in the MB selected for transmission is larger than the respective MB payload size, FlexCAN adds the necessary number of bytes with constant CCh pattern to complete the expected DLC. 

At the end of the successful transmission: 

- The value of the free running timer is written into the Time Stamp field. 

- The CODE field in the Control and Status word is updated. 

- Both CRC and FDCRC registers are updated. 

- A status flag is set in the Interrupt Flag register. 

- An interrupt is generated if allowed by the corresponding Interrupt Mask Register bit. 

The new CODE field after transmission depends on the code that was used to activate the MB (see Table 469 and Table 470 in Message buffer structure). 

When the Abort feature is enabled (MCR[AEN] is asserted), after the Interrupt flag is asserted for a mailbox configured as transmit buffer, the mailbox is blocked. Therefore the CPU is not able to update it until the Interrupt Flag is negated by the CPU. This means that the CPU must clear the corresponding IFLAG bit before starting to prepare this MB for a new transmission or reception. 

~~<mark>NOTE</mark>~~ 

If backwards compatibility is desired (MCR[AEN] is negated), write the INACTIVE code (1000b) to the CODE field to inactivate the MB. However, in this case the pending frame may be transmitted without notification (see Mailbox inactivation). 

### 72.3.3 Arbitration process 

The arbitration process scans the mailboxes, searching for the Tx mailbox that holds the message to be sent in the next opportunity. This mailbox is called the arbitration winner. 

The scan starts from the lowest number mailbox and runs toward the higher ones. 

The arbitration process is triggered in the following events: 

- From the CRC field of the CAN frame. The start point depends on the value of CTRL2[TASD]. 

- During the Error Delimiter field of a CAN frame. 

- During the Overload Delimiter field of a CAN frame. 

- When the winner is inactivated and the CAN bus has still not reached the first bit of the Intermission field. 

- When there is a CPU write to the C/S word of a winner MB and the CAN bus has still not reached the first bit of the Intermission field. 

- When CHI is in Idle state and the CPU writes to the C/S word of any MB. 

- When FlexCAN exits Bus Off state. 

- Upon leaving Freeze mode or Low Power mode. 

If the arbitration process does not manage to evaluate all mailboxes before the CAN bus has reached the first bit of the Intermission field, the temporary arbitration winner is invalidated and the FlexCAN will not compete for the CAN bus in the next opportunity. 

The arbitration process selects the winner among the active Tx mailboxes at the end of the scan according to the settings of both CTRL1[LBUF] and MCR[LPRIOEN]. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2726 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

#### 72.3.3.1 Lowest-number mailbox first 

If CTRL1[LBUF] is asserted, the first (lowest number) active Tx mailbox found is the arbitration winner. MCR[LPRIOEN] has no effect when CTRL1[LBUF] is asserted. 

#### 72.3.3.2 Highest-priority mailbox first 

If CTRL1[LBUF] is negated, then the arbitration process searches the active Tx mailbox with the highest priority, which means that this mailbox’s frame would have a higher probability to win the arbitration on CAN bus when multiple external nodes compete for the bus at the same time. 

The sequence of bits considered for this arbitration is called the arbitration value of the mailbox. The highest-priority Tx mailbox is the one that has the lowest arbitration value among all Tx mailboxes. 

If two or more mailboxes have equivalent arbitration values, the mailbox with the lowest number is the arbitration winner. 

The composition of the arbitration value depends on the MCR[LPRIOEN] setting. 

#### 72.3.3.2.1 Local priority disabled 

If MCR[LPRIOEN] is negated the arbitration value is built in the exact sequence of bits as they would be transmitted in a CAN frame (see the following table) in such a way that the local priority is disabled. 

Table 437. Composition of the arbitration value when local priority is disabled 

|Format||Mailbo|x arbitration value|(32 bits)||
|---|---|---|---|---|---|
|Standard (IDE = 0)|Standard ID (11|RTR (1 bit)|IDE (1 bit)|- (18 bits)|- (1 bit)|
||bits)|||||
|Extended (IDE = 1)|Extended ID[28:18]<br>(11 bits)|SRR (1 bit)|IDE (1 bit)|Extended ID[17:0]<br>(18 bits)|RTR (1 bit)|



#### 72.3.3.2.2 Local priority enabled 

To enable local priority, MCR[LPRIOEN] must be asserted. In this case the mailbox PRIO field is included at the very left of the arbitration value (see the following table). 

Table 438. Composition of the arbitration value when local priority is enabled 

|Format|||Mailbox arbitratio|n value (35 bits)|||
|---|---|---|---|---|---|---|
|Standard (IDE =<br>0)|PRIO (3 bits)|Standard ID (11<br>bits)|RTR (1 bit)|IDE (1 bit)|- (18 bits)|- (1 bit)|
|Extended (IDE<br>= 1)|PRIO (3 bits)|Extended<br>ID[28:18] (11<br>bits)|SRR (1 bit)|IDE (1 bit)|Extended<br>ID[17:0] (18<br>bits)|RTR (1 bit)|



Because the PRIO field is the most significant part of the arbitration value, mailboxes with low PRIO values have higher priority than mailboxes with high PRIO values regardless of the rest of their arbitration values. 

Note that the PRIO field is not part of the frame on the CAN bus. Its purpose is only to affect the internal arbitration process. 

#### 72.3.3.3 Arbitration process (continued) 

After the arbitration winner is found, its content is copied to a hidden auxiliary MB called Tx Serial Message Buffer (Tx SMB), which has the same structure as a normal MB but is not user accessible. This operation is called move-out and after it is done, write access to the C/S word of the corresponding MB is blocked (if MCR[AEN] is asserted). Write access is restored in the following events: 

- After the MB is transmitted and the corresponding IFLAG bit is cleared by the CPU. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2727 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

- FlexCAN enters Freeze mode or Bus Off. 

- FlexCAN loses the bus arbitration or there is an error during the transmission. 

At the first opportunity window on the CAN bus, the message on the Tx SMB is transmitted according to the CAN protocol rules. 

Arbitration process can be triggered in the following situations: 

- During Rx and Tx frames from CAN CRC field to end of frame. CTRL2[TASD] value may be changed to optimize the arbitration start point. 

- During CAN Bus Off state from TX_ERR_CNT=124 to 128. CTRL2[TASD] value may be changed to optimize the arbitration start point. 

- During C/S write by CPU in Bus Idle. First C/S write starts arbitration process, and a second C/S write during this same arbitration restarts the process. If other C/S writes are performed, Tx arbitration process is pending. If there is no arbitration winner after the arbitration process has finished, then the TX arbitration machine begins a new arbitration process. If there is a pending arbitration and Bus Idle state starts, then an arbitration process is triggered. In this case the first and second C/S write in Bus Idle will not restart the arbitration process. It is possible that there is not enough time to finish arbitration in Wait For Bus Idle state and the next state is Idle. In this case the scan is not interrupted, and it is completed during Bus Idle state. During this arbitration C/S write does not cause arbitration restart. 

- Arbitration winner deactivation during a valid arbitration window. 

- Upon exiting Freeze mode (first bit of the Wait For Bus Idle state). If there is a re-synchronization during Wait For Bus Idle, the arbitration process is restarted. 

Arbitration process stops in the following situations: 

- All mailboxes were scanned. 

- A Tx active mailbox is found if lowest buffer feature is enabled. 

- Arbitration winner inactivation or abort during any arbitration process. 

- There was not enough time to finish Tx arbitration process (for instance, when a deactivation was performed near the end of frame). In this case arbitration process is pending. 

- Error or overload flag in the bus. 

- Low Power or Freeze mode request in Idle state. 

Arbitration is considered pending as described below: 

- It was not possible to finish arbitration process in time. 

- C/S write during arbitration if write is performed in a MB whose number is lower than the Tx arbitration pointer. 

- Any C/S write if there is no Tx arbitration process in progress. 

- Rx Match has just updated a Rx code to Tx code. 

- Entering Bus Off state. 

C/S write during arbitration has the following effect: 

- If C/S write is performed in the arbitration winner, a new process is restarted immediately. 

- If C/S write is performed in a MB whose number is higher than the Tx arbitration pointer, the ongoing arbitration process will scan this MB as normal. 

### 72.3.4 Receive process 

To be able to receive CAN frames into a mailbox, the CPU must prepare it for reception by executing the following steps: 

1. If the mailbox is active (either Tx or Rx) inactivate the mailbox (see Mailbox inactivation), preferably with a safe inactivation (see Transmission abort mechanism). 

2. Write the ID word into the mailbox. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2728 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

3. Write the EMPTY code (0100b) to the CODE field of the Control and Status word to activate the mailbox. No setup is required for EDL, BRS, and ESI bits—they are overwritten by the respective bit fields in the received message. 

After the MB is activated, it will be able to receive frames that match the programmed filter. At the end of a successful reception, the mailbox is updated by the move-in process (see Move-in) as follows: 

1. The received data field (8 bytes at most for Classical CAN message format and up to 64 bytes for CAN FD message format) is stored. 

2. The received Identifier field is stored. 

3. The value of the Free Running Timer at the time of the second bit of frame's Identifier field is written into the mailbox's Time Stamp field. 

4. The received SRR, IDE, RTR, EDL, BRS, ESI, and DLC fields are stored. 

5. The CODE field in the Control and Status word is updated (see Table 469 and Table 470 in Section Message buffer structure). 

6. A status flag is set in the Interrupt Flag Register and an interrupt is generated if allowed by the corresponding Interrupt Mask Register bit. 

The recommended way for the CPU to service (read) the frame received in a mailbox is by the following procedure: 

1. Read the Control and Status word of that mailbox. 

2. Check if the BUSY bit is deasserted, indicating that the mailbox is locked. Repeat step 1) while it is asserted. See Mailbox lock mechanism. 

3. Read the contents of the mailbox. After the mailbox is locked, its contents won't be modified by FlexCAN move-in processes. See Move-in. 

4. Acknowledge the proper flag at IFLAG registers. 

5. Read the free running timer to unlock the mailbox. 

The CPU should poll for frame reception by the status flag bit for the specific mailbox in one of the IFLAG registers and not by the CODE field of that mailbox. Polling the CODE field does not work because after a frame is received and the CPU services the mailbox (by reading the C/S word followed by unlocking the mailbox), the CODE field will not return to EMPTY. It will remain FULL, as explained in Table 469. If the CPU tries to work around this behavior by writing to the C/S word to force an EMPTY code after reading the mailbox without a prior safe inactivation, a newly received frame matching the filter of that mailbox may be lost. 

~~<mark>CAUTION</mark>~~ In summary: never do polling by reading directly the C/S word of the mailboxes. Instead, read the IFLAG registers. 

Note that the received frame's Identifier field is always stored in the matching mailbox, thus the contents of the ID field in a mailbox may change if the match was due to masking. When MCR[SRXDIS] is asserted, FlexCAN will not store frames transmitted by itself in any MB, even if it contains a matching Rx mailbox, and no interrupt flag or interrupt signal will be generated. Otherwise, when MCR[SRXDIS] is deasserted, FlexCAN can receive frames transmitted by itself if a matching Rx mailbox exists. 

To be able to receive CAN frames through the Legacy Rx FIFO, the CPU must enable and configure the Legacy Rx FIFO during Freeze mode (see Legacy Rx FIFO). Upon receiving the Frames Available in Legacy Rx FIFO interrupt (see the description of IFLAG1[BUF5I] "Frames available in Legacy Rx FIFO"), the CPU should service the received frame using the following procedure: 

1. Read the Control and Status word (optional: needed only if a mask was used for IDE and RTR bits). 

2. Read the ID field (optional: needed only if a mask was used). 

3. Read the data field. 

4. Read the RXFIR register. (This step is optional, and is executed only if the IDHIT (Identifier Acceptance Filter Hit Indicator) is required in the application.) 

5. Clear the Frames Available in Legacy Rx FIFO interrupt by writing one to IFLAG1[BUF5I] (mandatory: releases the MB and allows the CPU to read the next Rx FIFO entry). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2729 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

When MCR[DMA] is asserted, upon receiving a frame in Legacy FIFO, IFLAG1[BUF5I] generates a DMA request and does not generate a CPU interrupt (see Legacy Rx FIFO under DMA operation). The IMASK1 bits in Legacy Rx FIFO region are not used. 

The DMA controller must service the received frame using the following procedure: 

1. Read the Control and Status word (read 80h address, optional). 

2. Read the ID field (read 84h address, optional). 

3. Read all data bytes (start read at 88h address, optional). 

4. Read the last data bytes (read 8Ch address is mandatory). 

### 72.3.5 Matching process 

The matching process scans the MB memory looking for Rx MBs programmed with the same ID as the one received from the CAN bus. If the Legacy Rx or Enhanced Rx FIFO is enabled, the priority of scanning can be selected between mailboxes and FIFO filters. The matching starts from the lowest number message buffer toward the higher ones. If no match is found within the first structure then the other is scanned subsequently. In the event that the FIFO is full, the matching algorithm always looks for a matching MB outside the FIFO region. 

For enhanced Rx FIFO see Enhanced Rx FIFO. 

For legacy Rx FIFO see Legacy Rx FIFO. 

As the frame is being received, it is stored in a hidden auxiliary MB called Rx Serial Message Buffer (Rx SMB). 

The matching process start point depends on the following conditions: 

- If the received frame is a remote frame, the start point is the CRC field of the frame. 

- If the received frame is a data frame with DLC field equal to zero, the start point is the CRC field of the frame. 

- If the received frame is a data frame with DLC field different than zero, the start point is the DATA field of the frame. 

If a matching ID is found in the FIFO table or in one of the mailboxes, the contents of the Rx SMB are transferred to the FIFO or to the matched mailbox by the move-in process. If any CAN protocol error is detected then no match results are transferred to the FIFO or to the matched mailbox at the end of reception. 

The matching process scans all matching elements of both Rx FIFO (if enabled) and the active Rx mailboxes (CODE is EMPTY, FULL, OVERRUN, or RANSWER) in search of a successful comparison with the matching elements of the Rx SMB that is receiving the frame on the CAN bus. The Rx SMB has the same structure as a mailbox. The reception structures (Rx FIFO or mailboxes) associated with the matching elements that had a successful comparison are the matched structures. The matching winner is selected at the end of the scan among those matched structures and depends on conditions described ahead. See the following table. 

Table 439. Matching architecture 

|Structure|SMB[RTR]|CTRL2[RRS]|CTRL2[EACE<br>N]|MB[IDE]|MB[RTR]|MB[ID<sup>1</sup>]|MB[CODE]|
|---|---|---|---|---|---|---|---|
|Mailbox|0|—|0|cmp<sup>2</sup>|no_cmp<sup>3</sup>|cmp_msk<sup>4</sup>|EMPTY or<br>FULL or<br>OVERRUN|
|Mailbox|0|—|1|cmp_msk|cmp_msk|cmp_msk|EMPTY or<br>FULL or<br>OVERRUN|
|Mailbox|1|0|—|cmp|no_cmp|cmp|RANSWER|
|Mailbox|1|1|0|cmp|no_cmp|cmp_msk|EMPTY or<br>FULL or<br>OVERRUN|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2730 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table 439. Matching architecture (continued) 

|Structure|SMB[RTR]|CTRL2[RRS]|CTRL2[EACE<br>N]|MB[IDE]|MB[RTR]|MB[ID<sup>1</sup>]|MB[CODE]|
|---|---|---|---|---|---|---|---|
|Mailbox|1|1|1|cmp_msk|cmp_msk|cmp_msk|EMPTY or<br>FULL or<br>OVERRUN|
|Legacy Rx<br>FIFO<sup>5</sup>|—|—|—|cmp_msk|cmp_msk|cmp_msk|—|



1. For mailbox structure, If SMB[IDE] is asserted, the ID is 29 bits (ID Standard + ID Extended). If SMB[IDE] is negated, the ID is only 11 bits (ID Standard). For Legacy Rx FIFO structure, the ID depends on IDAM. 

2. cmp: Compares the Rx SMB contents with the MB contents regardless the masks. 

3. no_cmp: The Rx SMB contents are not compared with the MB contents. 

4. cmp_msk: Compares the Rx SMB contents with MB contents taking into account the masks. 

5. SMB[IDE] and SMB[RTR] are not taken into account when IDAM is type C. 

~~<mark>NOTE</mark>~~ For Enhanced Rx FIFO, see Enhanced Rx FIFO matching process. 

A reception structure is free-to-receive when any of the following conditions is satisfied: 

- The CODE field of the mailbox is EMPTY. 

- The CODE field of the mailbox is either FULL or OVERRUN and it has already been serviced (the C/S word was read by the CPU and unlocked as described in Mailbox lock mechanism). 

- The CODE field of the mailbox is either FULL or OVERRUN and an inactivation (see Mailbox inactivation) is performed. 

- The Legacy Rx FIFO or Enhanced Rx FIFO is not full. 

The scan order for mailboxes and Legacy Rx FIFO is from the matching element with lowest number to the higher ones. 

The matching winner search for mailboxes is affected by MCR[IRMQ]. If it is negated, the matching winner is the first matched mailbox regardless if it is free-to-receive or not. If it is asserted, the matching winner is selected according to the priority below: 

1. the first free-to-receive matched mailbox; 

2. the last non free-to-receive matched mailbox. 

It is possible to select the priority of scan between mailboxes and Legacy Rx FIFO or Enhanced Rx FIFO with CTRL2[MRP]. 

If the selected priority is Rx FIFO first: 

- If the Rx FIFO is a matched structure and is free-to-receive, then the Rx FIFO is the matching winner regardless of the scan for mailboxes. 

- Otherwise (the Rx FIFO is not a matched structure or is not free-to-receive), then the matching winner is searched among mailboxes as described above. 

If the selected priority is mailboxes first: 

- If a free-to-receive matched mailbox is found, it is the matching winner regardless of the scan for Rx FIFO. 

- If no matched mailbox is found, then the matching winner is searched in the scan for the Rx FIFO. 

- If both conditions above are not satisfied and a non–free-to-receive matched mailbox is found, then the matching winner determination is conditioned by MCR[IRMQ]: 

   - If MCR[IRMQ] is negated, the matching winner is the first matched mailbox. 

   - If MCR[IRMQ] is asserted, the matching winner is the Rx FIFO if it is a free-to-receive matched structure; otherwise, the matching winner is the last non–free-to-receive matched mailbox. 

See the following table for a summary of matching possibilities. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2731 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table 440. Matching possibilities and resulting reception structures 

|RFENor<br>ERFEN|IRMQ|MRP|Matched in MB|Matched in<br>FIFO|Reception<br>structure|Description|
|---|---|---|---|---|---|---|
|||No FIFO, on<br>|ly MB, match is al<br>|ways MB first<br>|||
|0|0|X<sup>1</sup>|None<sup>2</sup>|—<sup>3</sup>|None|Frame lost by<br>no match|
|0|0|X|Free<sup>4</sup>|—|First MB||
|0|1|X|None|—|None|Frame lost by<br>no match|
|0|1|X|Free|—|First MB||
|0|1|X|Not free|—|Last MB|Overrun|
||FI|FO enabled, no m|atch in FIFO is as i|f FIFO does not e<br>|xist||
|1|0|X|None|None<sup>5</sup>|None|Frame lost by<br>no match|
|1|0|X|Free|None|First MB||
|1|1|X|None|None|None|Frame lost by<br>no match|
|1|1|X|Free|None|First MB||
|1|1|X|Not free|None|Last MB|Overrun|
|||FIFO|enabled, Queue di|sabled|||
|1|0|0|X|Not full<sup>6</sup>|FIFO||
|1|0|0|None|Full<sup>7</sup>|None|Frame lost by<br>FIFO full (FIFO<br>overflow)|
|1|0|0|Free|Full|First MB||
|1|0|0|Not free|Full|First MB||
|1|0|1|None|Not full|FIFO||
|1|0|1|None|Full|None|Frame lost by<br>FIFO full (FIFO<br>overflow)|
|1|0|1|Free|X|First MB||
|1|0|1|Not free|X|First MB|Overrun|
|||FIFO|enabled, queue en|abled|||
|1|1|0|X|Not full|FIFO||
|1|1|0|None|Full|None|Frame lost by<br>FIFO full (FIFO<br>overflow)|
|1|1|0|Free|Full|First MB||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2732 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table 440. Matching possibilities and resulting reception structures (continued) 

|RFENor<br>ERFEN|IRMQ|MRP|Matched in MB|Matched in<br>FIFO|Reception<br>structure|Description|
|---|---|---|---|---|---|---|
|1|1|0|Not free|Full|Last MB|Overrun|
|1|1|1|None|Not full|FIFO||
|1|1|1|Free|X|First MB||
|1|1|1|Not free|Not full|FIFO||
|1|1|1|Not free|Full|Last MB|Overrun|



1. This is a don't care condition. 

2. Matched in MB "None" means that the frame has not matched any MB (free-to-receive or non–free-to-receive). 

3. This is a forbidden condition. 

4. Matched in MB "Free" means that the frame matched at least one MB free-to-receive regardless of whether it has matched MBs non-free-to-receive. 

5. Matched in FIFO "None" means that the frame has not matched any filter in FIFO. It is as if the FIFO didn't exist (CTRL2[RFEN]=0 and ERFCR[ERFEN]=0). 

6. Matched in FIFO "Not full" means that the frame has matched a FIFO filter and has empty slots to receive it. 

7. Matched in FIFO "Full" means that the frame has matched a FIFO filter but couldn't store it because it has no empty slots to receive it. 

If a non-safe mailbox inactivation (see Mailbox inactivation) occurs during matching process and the mailbox inactivated is the temporary matching winner, then the temporary matching winner is invalidated. The matching elements scan is not stopped nor restarted—it continues normally. The consequence is that the current matching process works as if the matching elements compared before the inactivation did not exist, therefore a message may be lost. 

Suppose, for example, that the FIFO is disabled, IRMQ is enabled, there are two MBs with the same ID, and FlexCAN starts receiving messages with that ID. Let us say that these MBs are the second and the fifth in the array. When the first message arrives, the matching algorithm finds the first match in MB number 2. The code of this MB is EMPTY, so the message is stored there. When the second message arrives, the matching algorithm finds MB number 2 again, but it is not "free-to-receive", so it keeps looking, finds MB number 5 and stores the message there. If yet another message with the same ID arrives, the matching algorithm finds out that there are no matching MBs that are "free-to-receive", so it decides to overwrite the last matched MB, which is number 5. In doing so, it sets the CODE field of the MB to indicate OVERRUN. 

The ability to match the same ID in more than one MB can be exploited to implement a reception queue (in addition to the full featured FIFO) to allow more time for the CPU to service the MBs. By programming more than one MB with the same ID, received messages are queued into the MBs. The CPU can examine the Time Stamp field of the MBs to determine the order in which the messages arrived. 

Matching to a range of IDs is possible by using ID acceptance masks. FlexCAN supports individual masking per MB (see the description of Rx Individual Mask Registers (RXIMR0 - RXIMR95)). During the matching algorithm, if a mask bit is asserted, then the corresponding ID bit is compared. If the mask bit is negated, the corresponding ID bit is a "don't care". Note that the Individual Mask Registers are implemented in RAM, so they are not initialized out of reset. Also, they can only be programmed when the module is in Freeze mode; otherwise, they are blocked by hardware. 

FlexCAN also supports an alternate masking scheme with only four mask registers (RXFGMASK, RXMGMASK, RX14MASK, and RX15MASK) for backwards compatibility with legacy applications. This alternate masking scheme is enabled when the IRMQ bit in the MCR register is negated. 

### 72.3.6 Move process 

There are two types of move process: move-in and move-out. 

#### 72.3.6.1 Move-in 

The move-in process is the copy of a message received by an Rx SMB to an Rx mailbox or FIFO that has matched it. If the move destination is the Legacy Rx FIFO, attributes of the message are also copied to the CAN_RXFIR FIFO. Each Rx SMB has its own 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2733 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

move-in process, but only one is performed at a given time as described ahead. The move-in starts only when the message held by the Rx SMB has a corresponding matching winner (see Matching process) and all of the following conditions are true: 

- The CAN bus has either reached or already gone past: 

   - The second bit of Intermission field next to the frame that carried the message that is in the Rx SMB. 

   - The first bit of an overload frame next to the frame that carried the message that is in the Rx SMB. 

- There is no ongoing matching process. 

- The destination mailbox is not locked by the CPU. 

- There is no ongoing move-in process from another Rx SMB. If more than one move-in process is to be started at the same time, both are performed and the newest substitutes for the oldest. 

The term pending move-in is used throughout the documentation and stands for a move-to-be that still does not satisfy all of the aforementioned conditions. 

The move-in is cancelled and the Rx SMB is able to receive another message if any of the following conditions is satisfied: 

- The destination mailbox is inactivated after the CAN bus has reached the first bit of Intermission field next to the frame that carried the message and its matching process has finished. 

- There is a previous pending move-in to the same destination mailbox. 

- The Rx SMB is receiving a frame transmitted by the FlexCAN itself and self-reception is disabled (MCR[SRXDIS] is asserted). 

- Any CAN protocol error is detected. 

Note that the pending move-in is not cancelled if the module enters Freeze or Low-Power mode. It stays on hold, only waiting for Freeze and Low-Power mode to be exited and the module to be unlocked. If an MB is unlocked during Freeze mode, the move-in happens immediately. 

The move-in process is the execution by the FlexCAN of the following steps: 

1. Push IDHIT into the RXFIR FIFO if the message is destined for the Legacy Rx FIFO. 

2. Read all data words from the Rx SMB in accordance with the selected payload size for the Rx storage element. 

3. Write all data words to the Rx mailbox in accordance with the selected payload size for the Rx storage element. If the data size of the storage element is smaller than the original payload size described in the message's DLC field, the payload is truncated and the high order bytes that do not fit the destination size are lost. 

4. Read the Control/Status and ID words from the Rx SMB. 

5. Write Control/Status and ID words to the Rx mailbox, and update the CODE field. 

The move-in process is not atomic, in such a way that it is immediately cancelled by the inactivation of the destination mailbox (see Mailbox inactivation). In this case the mailbox may remain partially updated, thus incoherent. The exception is if the move-in destination is a Legacy or Enhanced Rx FIFO message buffer; then the process cannot be cancelled. 

The BUSY Bit (least significant bit of the CODE field) of the destination message buffer is asserted while the move-in is being performed to alert the CPU that the message buffer content is temporarily incoherent. 

#### 72.3.6.2 Move-out 

The move-out process is the copy of the content from a Tx Mailbox to the Tx SMB when a message for transmission is available (see Arbitration process). The move-out occurs in the following conditions: 

- The first bit of Intermission field 

- During Bus Off state when TX Error Counter is in the 124 to 128 range 

- During Bus Idle state 

- During Wait For Bus Idle state 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2734 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

The move-out process is not atomic. Only the CPU has priority to access the memory concurrently out of Bus Idle state. In Bus Idle, the move-out has the lowest priority to the concurrent memory accesses. 

### 72.3.7 Data coherence 

In order to maintain data coherency and FlexCAN proper operation, the CPU must obey the rules described in Transmit process and Receive process. 

#### 72.3.7.1 Transmission abort mechanism 

The abort mechanism provides a safe way to request the abort of a pending transmission. A feedback mechanism is provided to inform the CPU if the transmission was aborted or if the frame could not be aborted and was transmitted instead. 

Two primary conditions must be fulfilled in order to abort a transmission: 

- MCR[AEN] must be asserted. 

- The first CPU action must be the writing of abort code (1001b) into the CODE field of the Control and Status word. 

Active MBs configured for transmission must be aborted first before they can be updated. If the abort code is written to a Mailbox that is currently being transmitted or to a Mailbox that was already loaded into the Tx SMB for transmission, the write operation is blocked and the transmission is not disturbed. However, the abort request is captured and kept pending until one of the following conditions is satisfied: 

- The module loses the bus arbitration. 

- There is an error during the transmission. 

- The module is put into Freeze mode. 

- The module enters Bus Off state. 

- There is an overload frame. 

If none of the conditions above are reached: 

- The MB is transmitted correctly. 

- The interrupt flag is set in the IFLAG register. 

- An interrupt to the CPU is generated (if enabled). 

The abort request is automatically cleared when the interrupt flag is set. On the other hand, if only one of the above conditions is reached, the frame is not transmitted; therefore: 

- The abort code is written into the CODE field. 

- The interrupt flag is set in the IFLAG. 

- An interrupt is (optionally) generated to the CPU. 

If the CPU writes the abort code before the transmission begins internally, then the write operation is not blocked; therefore, the MB is updated and the interrupt flag is set. In this way the CPU only needs to read the abort code to make sure the active MB was safely inactivated. Although the AEN bit is asserted and the CPU wrote the abort code, in this case the MB is inactivated and not aborted, because the transmission did not start yet. One Mailbox is aborted only when the abort request is captured and kept pending until one of the previous conditions is satisfied. 

#### 72.3.7.2 Mailbox inactivation 

Inactivation is a mechanism provided to protect the mailbox against updates by the FlexCAN internal processes, thus allowing the CPU to rely on mailbox data coherence after having updated it, even in Normal mode. 

Inactivation of transmission mailboxes must be performed just when MCR[AEN] is deasserted. 

If a mailbox is inactivated, it participates in neither the arbitration process nor the matching process until it is reactivated. See Transmit process and Receive process for more detailed instructions on how to inactivate and reactivate a mailbox. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2735 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

To inactivate a mailbox, the CPU must update its CODE field to INACTIVE (either 0b or 1000b). 

Because you will not be able to synchronize the CODE field update with the FlexCAN internal processes, an inactivation can have the following consequences: 

- A frame in the bus that matches the filtering of the inactivated Rx mailbox may be lost without notice, even if there are other mailboxes with the same filter. 

- A frame containing the message within the inactivated Tx mailbox may be transmitted without setting the respective IFLAG. 

In order to perform a safe inactivation and avoid the above consequences for Tx mailboxes, the CPU must use the transmission abort mechanism (see Transmission abort mechanism). 

The inactivation automatically unlocks the mailbox (see Mailbox lock mechanism). 

~~<mark>NOTE</mark>~~ 

Message buffers that are part of the Legacy Rx FIFO or Enhanced Rx FIFO cannot be inactivated. There is no write protection on the Legacy FIFO region by FlexCAN. CPU must maintain data coherency in the Legacy FIFO region when RFEN is asserted. 

#### 72.3.7.3 Mailbox lock mechanism 

Other than mailbox inactivation, FlexCAN has another data coherence mechanism for the receive process. When the CPU reads the Control and Status word of an Rx MB with codes FULL or OVERRUN, FlexCAN assumes that the CPU wants to read the whole MB in an atomic operation, and therefore it sets an internal lock flag for that MB. The lock is released when the CPU reads the free running timer (global unlock operation), or when it reads the Control and Status word of another MB regardless of its code. A CPU write into the C/S word also unlocks the MB, but this procedure is not recommended for normal unlock use because it cancels a pending move and potentially may lose a received message. The MB locking prevents a new frame from being written into the MB while the CPU is reading it. 

~~<mark>NOTE</mark>~~ 

The locking mechanism applies only to Rx MBs that are not part of the Legacy Rx FIFO and have a code different than INACTIVE (0b) or EMPTY<sup>[1]</sup> (0100b). Also, Tx MBs cannot be locked. 

Suppose, for example, that the Legacy Rx FIFO is disabled and the second and the fifth MBs of the array are programmed with the same ID, and FlexCAN has already received and stored messages into these two MBs. Suppose now that the CPU decides to read MB number 5 and at the same time another message with the same ID is arriving. When the CPU reads the Control and Status word of MB number 5, this MB is locked. The new message arrives and the matching algorithm finds out that there are no free-to-receive MBs, so it decides to override MB number 5. However, this MB is locked, so the new message cannot be written there. It will remain in the Rx SMB waiting for the MB to be unlocked, and only then will be written to the MB. 

If the MB is not unlocked in time and yet another new message with the same ID arrives, then the new message overwrites the one on the Rx SMB and there will be no indication of lost messages either in the CODE field of the MB or in the Error and Status Register. 

While the message is being moved in from the Rx SMB to the MB, the BUSY bit on the CODE field is asserted. If the CPU reads the Control and Status word and finds out that the BUSY bit is set, it should defer accessing the MB until the BUSY bit is negated. 

~~<mark>NOTE</mark>~~ 

If the BUSY bit is asserted or if the MB is empty, then reading the Control and Status word does not lock the MB. 

Inactivation takes precedence over locking. If the CPU inactivates a locked Rx MB, then its lock status is negated and the MB is marked as invalid for the current matching round. Any pending message on the Rx SMB will not be transferred anymore to the MB. An MB is unlocked when the CPU reads the Free Running Timer Register (see Free Running Timer (TIMER)), or the C/S word of another MB. 

- [1] In previous FlexCAN versions, reading the C/S word locked the MB even if it was EMPTY. This behavior is maintained when the IRMQ bit is negated. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2736 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Lock and unlock mechanisms have the same functionality in both Normal and Freeze modes. 

An unlock during Normal or Freeze mode results in the move-in of the pending message. However, the move-in is postponed if an unlock occurs during a low power mode (see Modes of operation), and it takes place only when the module returns to Normal or Freeze modes. 

### 72.3.8 Enhanced Rx FIFO 

FlexCAN supports an enhanced Rx FIFO engine which can store up to 20 CAN FD messages. The region 2000h–204Fh contains the output of the FIFO which should be read by the CPU. The enhanced Rx FIFO is enabled by setting EFRCR[ERFEN]. Although FlexCAN has two FIFO options, Legacy Rx FIFO and Enhanced Rx FIFO, they cannot be enabled at the same time. Refer to Legacy Rx FIFO to find detailed information about Legacy Rx FIFO. 

The enhanced Rx FIFO has a watermark which is configured by setting EFRCR[ERFWM]. If EFRCR[ERFWM] is set, the CPU is notified only if a minimum number of messages is stored in the FIFO. When the number of stored messages is greater than the value in EFRCR[ERFWM], ERFSR[ERFWMI] is set by the hardware. Optionally, an interrupt or a DMA transfer can be triggered if MCR[DMA] or ERFIER[ERFWMIIE] are set, respectively. 

For the Enhanced Rx FIFO to receive, the CPU must execute the configuration procedure below. The same procedure must be done if the CPU needs to change any of the configuration of the Enhanced RX FIFO. 

1. Enter Freeze mode. 

2. Enable Enhanced Rx FIFO by setting ERFCR[ERFEN], if it is not already enabled.<sup>[8]</sup> 

3. Write one to ERFSR[ERFCLR] to reset Enhanced Rx FIFO engine. 

4. Clear EFRSR[ERFUFW], EFRSR[ERFOVF], EFRSR[ERFWMI], and EFRSR[ERFDA], if they are set. 

5. Write EFRCR[NFE] to configure the total number of enhanced Rx FIFO filter elements to be used in Enhanced Rx FIFO reception. 

6. Write ERFCR[NEXIF] to configure the number of extended ID and standard ID filter elements to be used in Enhanced Rx FIFO reception.<sup>[9]</sup> 

7. Configure the Enhanced Rx FIFO watermark by writing ERFCR[ERFWM]. If MCR[DMA] is set, ERFCR[ERFWM] should be configures as 0x0. 

8. If interrupts will be used, set the interrupt enables in the ERIER register. 

9. If DMA will be used, set MCR[DMA] to enable DMA operation and write ERFCR[DMALW] to configure the number of words to transfer for each Enhanced Rx FIFO data element. 

10. Configure the filter elements by writing in the ERFFELn registers.<sup>[10]</sup> 

11. Leave Freeze mode. 

There are two types of Enhanced Rx FIFO filter elements that can be stored in ERFFELn registers: extended-ID filter element and standard-ID filter element. Each extended-ID filter element is stored in two ERFFELn registers while each standard-ID filter element is stored in one ERFFELn register. The total number of Enhanced RX FIFO filter elements is defined by ERFCR[NFE]. 

In addition, the filter memory space can be split into two regions: one for extended-ID filter elements and another for standard-ID filter elements, according to ERFCR[NEXIF]. The figure below shows how the Enhanced Rx filter elements are defined. Detailed information about the Enhanced Rx FIFO matching process and filter element formats can be found in Enhanced Rx FIFO matching process. 

- [8] MCR[RFEN] must be cleared so that Enhanced Rx FIFO is enabled. 

- [9] NEXIF ≤ NFE + 1. 

- [10] ERFFELn registers are implemented in RAM; thus they must be explicitly initialized prior to any reception. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2737 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2738-01.png)


<!-- Start of picture text -->
CAN (FlexCAN)<br>3000h<br>Extended ID<br>Filter Element<br>NEXIF<br>Standard ID<br>Filter Element<br>NFE<br>Last ERFFEL<br>Address<br>Figure 377. Number of enhanced Rx FIFO filter elements<br><!-- End of picture text -->

#### 72.3.8.1 Enhanced Rx FIFO matching process 

When ERFCR[ERFEN] is enabled, FlexCAN scans the ERFFELn memory region. If at least one filter element satisfies the matching criteria, then the CAN message content is transfered to the enhanced RX FIFO memory. 

~~<mark>NOTE</mark>~~ 

If multiple filters match the incoming message ID, then the first matching filter found by the matching process must be indicated in IDHIT. 

Each ERFFELn register can store one standard filter element. The matching criteria are defined by ERFFELn[FSCH] in this way: 

- If FSCH = b00, the filter scheme is based on mask and filter. A CAN message matches a standard ID filter element only if these criteria are reached: 

   1. CAN message is base frame format (IDE = 0) 

   2. (ID[n] = STD ID filter [n]) or (STD ID Mask[n] =0) for each bit n from 0 to 10 

   3. (RTR = RTR Filter) or (RTR MASK = 0) 

In this explanation, RTR and ID are the Remote Transmit Request field and the ID from a CAN message, respectively. 

If FSCH = b00, the filters and masks are defined as shown in this table. 

Table 441. Standard ID filter element with filter + mask scheme (FSCH = b00) 

|31|30|29|28|27|26||16|15<br>12|11|10|0|
|---|---|---|---|---|---|---|---|---|---|---|---|
|FSCH|=b00|Rese|rved|RTR<br>filter||STD ID filter||Reserved|RTR<br>mask||STD ID mask|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2738 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

- If FSCH = b01, the filter scheme is based on range. A CAN message matches a standard ID filter element only if these criteria are reached: 

   1. CAN message is base frame format (IDE = 0) 

   2. ID ≥ STD ID Filter1 

   3. ID ≤ STD ID Filter2 

   4. (RTR = RTR filter) or (RTR MASK = 0) 

RTR and ID are the Remote Transmit Request bit and ID from a CAN message, respectively. If FSCH = b01, the filters and mask are defined as shown in this table. 

Table 442. Standard ID filter element with range scheme (FSCH = b01) 

|31<br>30|29|28|27|26||16|15<br>12|11|10|0|
|---|---|---|---|---|---|---|---|---|---|---|
|FSCH=b01|Rese|rved|RTRfil<br>ter||STD ID Filter2||Reserved|RTR<br>mask||STD ID Filter1|



- If FSCH = b10, the filter scheme is based on two filters without masks. A CAN message matches a standard ID filter element only if these criteria are reached: 

   1. CAN message is base frame format (IDE = 0) 

   2. (ID[n] = STD ID Filter1[n]) or (ID[n] = STD ID Filter2[n]) for each bit n from 0 to 10 

   3. (RTR = RTR Filter1) or (RTR = RTR Filter2) 

RTR and ID are the Remote Transmit Request bit and ID from a CAN message, respectively. If FSCH = b10, the filters are defined as shown in this table. 

Table 443. Standard ID filter element with 2-filter scheme (FSCH = b10) 

|31|30|29|28|27|26|16|15<br>12|11|10<br>0|
|---|---|---|---|---|---|---|---|---|---|
|FSCH|=b10|Rese|rved|RTR<br>Filter<br>2||STD ID Filter2|Reserved|RTR<br>Filter<br>1|STD ID Filter1|



Each pair of ERFFELn registers can store one extended filter element. The matching criteria are defined by ERFFELn[FSCH] in this way: 

- If FSCH = b00, the filter scheme is based on mask and filter. A CAN message matches an extended ID filter element only if these criteria are reached: 

   1. CAN message is extended frame format (IDE = 1) 

   2. (ID[n] = EXT ID filter [n]) or (EXT ID Mask[n] =0) for each bit n from 0 to 28 

   3. (RTR = RTR Filter) or (RTR MASK = 0) 

If FSCH = b00, the filters and masks are defined as shown in this table. 

Table 444. Extended ID filter element with filter + mask scheme (FSCH = b00) 

|31<br>30|29|28|0|
|---|---|---|---|
|FSCH|RTR<br>filter||EXT ID filter|
|Reserved|RTR<br>mask||EXT ID mask|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2739 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

- If FSCH = b01, the filter scheme is based on range. A CAN message matches an extended ID filter element only if the following criteria are reached: 

   1. CAN message is extended frame format (IDE = 1) 

   2. ID ≥ EXT ID Filter1 

   3. ID ≤ EXT ID Filter2 

   4. (RTR = RTR Filter) or (RTR MASK = 0) 

If FSCH = b01, the filters and masks are defined as shown in this table. 

Table 445. Extended ID filter element with range scheme (FSCH = b01) 

|31<br>30|29|28|0|
|---|---|---|---|
|FSCH|RTR<br>filter||EXT ID Filter2|
|Reserved|RTR<br>mask||EXT ID filter 1|



- If FSCH = b10, the filter scheme is based on two filters without masks. A CAN message matches an extended ID filter element only if these criteria are reached: 

   1. CAN message is extended frame format (IDE = 1) 

   2. (ID[n] = EXT ID Filter1[n]) or (ID[n] = EXT ID Filter2[n]) for each bit n from 0 to 28 

   3. (RTR = RTR Filter1) or (RTR = RTR Filter2) 

If FSCH = b10, the filters and masks are defined as shown in this table. 

Table 446. Extended ID filter element with 2-filter scheme (FSCH = b10) 

|31<br>30|29|28|0|
|---|---|---|---|
|FSCH|RTR<br>Filter2||EXT ID Filter2|
|Reserved|RTR<br>Filter1||EXT ID filter 1|



#### 72.3.8.2 Enhanced Rx FIFO under DMA operation 

The DMA feature is enabled by asserting both ERF[ERFEN] and MCR[DMA]. The DMA controller can read the received message by reading a message buffer structure at the Enhanced FIFO output port at the address range defined in Enhanced Rx FIFO structure. 

~~<mark>NOTE</mark>~~ 

FlexCAN supports 32-bit access only for DMA transfers. 

The CPU should not access the Enhanced FIFO output port address range during DMA operation, so that the FIFO engine operates properly. Before enabling MCR[DMA], the CPU must service Enhanced Rx FIFO status bits. Otherwise, these bits may show that the FIFO has data to be serviced, and mistakenly generate a DMA request. Before disabling MCR[DMA], the CPU must first clear the ERFUFW, ERFOVF, ERMWMI, and ERFDA fields in the ERFSR register, and then clear the Enhanced RX FIFO engine by writing one to ERFSR[ERFCLR]. 

ERFSR[ERFDA] is set by the hardware when there is one frame available to be read from the Enhanced Rx FIFO. Upon receiving the request, the DMA controller can read the message in the Enhanced Rx FIFO output. Each message reading process must end by the address defined in ERFCR[DMALW]. 

The following rules must be obeyed for Enhanced Rx FIFO DMA operation: 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2740 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

- Because a DMA transfer cannot be dynamically changed, ERFCR[DMALW] should be programmed so that the Enhanced Rx FIFO element can store the largest CAN message present on the CAN bus. 

- Data bytes are valid according to the DLC field. See Table 472. 

Each time one message is read from FIFO by the DMA controller, ERFSR[ERFDA] is cleared by FlexCAN and set again if there is at least one message stored in the FIFO. 

For example, suppose that the maximum number of bytes in the data field of a CAN frame for a certain application is eight, and high-resolution time stamp is enabled. In that case the last Enhanced RX FIFO address offset can be found in Table 481 and Table 482. Using this address offset, ERFCR[DMALW] can be determined like this: 

- Maximum number of data bytes = 8 

- HR TIME STAMP enabled 

- Last address offset = TS_OFF = 2014h 

- DMALW = 5 

#### 72.3.8.3 Enhanced Rx FIFO clear operation 

When ERFCR[ERFEN] is set, the CPU can clear the Enhanced Rx FIFO by writing one into ERFSR[ERFCLR]. The clear operation resets the internal FIFO pointers although the FIFO content stored in RAM is not changed. This operation can only be performed in Freeze mode and is blocked by hardware in other modes. This operation does not clear the ERFUFW, ERFOVF, ERFDA, and ERFWMI fields in EFRSR. Consequently the CPU must service all these fields before executing the clear FIFO task. 

### 72.3.9 Legacy Rx FIFO 

The Legacy Rx FIFO is receive-only and is enabled by asserting MCR[RFEN]. The reset value of this bit is zero to maintain software backward compatibility with previous versions of the module that did not have the Legacy FIFO feature. 

~~<mark>CAUTION</mark>~~ Legacy Rx FIFO must not be enabled when CAN FD feature is enabled. 

The Legacy FIFO is 6-message deep. The memory region occupied by the Legacy FIFO structure (both message buffers and Legacy FIFO engine) is described in Legacy Rx FIFO structure. The CPU can read the received messages sequentially, in the order they were received, by repeatedly reading a message buffer structure at the output of the Legacy FIFO. 

IFLAG1[BUF5I] (Frames available in Legacy Rx FIFO) is asserted when there is at least one frame available to be read from the Legacy FIFO. An interrupt is generated if it is enabled by the corresponding mask bit. Upon receiving the interrupt, the CPU can read the message (accessing the output of the Legacy FIFO as a message buffer) and the RXFIR register, and then clear the interrupt. If there are more messages in the Legacy FIFO the act of clearing the interrupt updates the output of the Legacy FIFO with the next message and updates RXFIR with the attributes of that message, reissuing the interrupt to the CPU. Otherwise, the flag remains negated. The output of the Legacy FIFO is valid only while IFLAG1[BUF5I] is asserted. 

IFLAG1[BUF6I] (Legacy Rx FIFO Warning) is asserted when the number of unread messages within the Legacy Rx FIFO is increased to five from four due to the reception of a new one, meaning that the Legacy Rx FIFO is almost full. The flag remains asserted until the CPU clears it. 

IFLAG1[BUF7I] (Legacy Rx FIFO Overflow) is asserted when an incoming message was lost because the Legacy Rx FIFO is full. Note that the flag will not be asserted when the Legacy Rx FIFO is full and the message was captured by a Mailbox. The flag remains asserted until the CPU clears it. 

Clearing one of those three flags does not affect the state of the other two. 

An interrupt is generated if an IFLAG bit is asserted and the corresponding mask bit is asserted too. 

A powerful filtering scheme is provided to accept only frames intended for the target application, reducing the interrupt servicing workload. The filtering criteria is specified by programming a table of up to 128 32-bit registers, according to CTRL2[RFFN] setting, that can be configured to one of the following formats (see also Legacy Rx FIFO structure): 

- Format A: 128 IDAFs (extended or standard IDs including IDE and RTR) 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2741 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

- Format B: 256 IDAFs (standard IDs or extended 14-bit ID slices including IDE and RTR) 

- Format C: 512 IDAFs (standard or extended 8-bit ID slices) 

~~<mark>NOTE</mark>~~ 

A chosen format is applied to all entries of the filter table. It is not possible to mix formats within the table. 

Every frame available in the Legacy Rx FIFO has a corresponding IDHIT (Identifier Acceptance Filter Hit Indicator) that can be read in the IDHIT field from C/S word, as shown in the Legacy Rx FIFO Structure description. Another way the CPU can obtain this information is by accessing the RXFIR register. RXFIR[IDHIT] refers to the message at the output of the Legacy FIFO and is valid while the IFLAG1[BUF5I] flag is asserted. The RXFIR register must be read only before clearing the flag, which guarantees that the information refers to the correct frame within the Legacy FIFO. 

Up to 32 elements of the filter table are individually affected by the Individual Mask Registers (RXIMRx), according to the setting of CTRL2[RFFN], allowing very powerful filtering criteria to be defined. If MCR[IRMQ] is negated, then the Legacy Rx FIFO filter table is affected by RXFGMASK. 

~~<mark>NOTE</mark>~~ For more information about the difference between FD and non-FD regarding this feature, see Table 436. 

#### 72.3.9.1 Legacy Rx FIFO under DMA operation 

The receive-only Legacy FIFO can support DMA. This feature is enabled by asserting both MCR[RFEN] and MCR[DMA]. The reset value of MCR[DMA] is zero to maintain backward compatibility with previous versions of the module that did not have the DMA feature. 

The DMA controller can read the received message by reading a message buffer structure at the Legacy FIFO output port at the 

80h–8Ch address range. 

~~<mark>NOTE</mark>~~ 

FlexCAN supports 32-bit access only for DMA transfers. 

When MCR[DMA] is asserted the CPU must not access the Legacy FIFO output port address range. Before enabling MCR[DMA], the CPU must service the IFLAGs asserted in the Legacy Rx FIFO region. Otherwise, these IFLAGs may show that the FIFO has data to be serviced, and mistakenly generate a DMA request. Before disabling MCR[DMA], the CPU must perform a clear Legacy FIFO operation. 

IFLAG1[BUF5I] (Frames available in Legacy Rx FIFO) is asserted when there is at least one frame available to be read from the FIFO. Consequently a DMA request is generated simultaneously. Upon receiving the request, the DMA controller can read the message (accessing the output of the Legacy FIFO as a message buffer). The DMA reading process must end by reading address 8Ch, which clears IFLAG1[BUF5I] and updates both the FIFO output with the next message (if FIFO is not empty) and the RXFIR register with the attributes of the new message. If there are more messages stored in the FIFO, IFLAG1[BUF5I] will be re-asserted and another DMA request is issued. Otherwise, the flag remains negated. 

~~<mark>NOTE</mark>~~ RXFIR register contents cannot be read after DMA completes the Legacy FIFO read. The IDHIT information is also available in the C/S word at address 080h (see Legacy Rx FIFO structure. 

IFLAG1[BUF6I] and IFLAG1[BUF7I] are not used when the DMA feature is enabled. 

When FlexCAN is working with DMA, the CPU does not receive any Legacy Rx FIFO interruption and must not clear the related IFLAGs. In addition, the related IMASKs are not used to mask the generation of DMA requests. 

~~<mark>NOTE</mark>~~ 

For more information about the difference between FD and non-FD regarding this feature, see Table 436. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2742 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

#### 72.3.9.2 Clear Legacy FIFO operation 

When MCR[RFEN] is asserted, the clear Legacy FIFO operation is a feature used to empty Legacy FIFO contents. With MCR[RFEN] asserted the Clear FIFO occurs when the CPU writes one in IFLAG1[BUF0I]. This operation can only be performed in Freeze mode and is blocked by hardware in other modes. This operation does not clear the FIFO IFLAGs; consequently the CPU must service all FIFO IFLAGs before executing the clear FIFO task. 

When Legacy Rx FIFO is working with DMA, the clear FIFO operation clears IFLAG1[BUF5I] and the DMA request is canceled. 

~~<mark>CAUTION</mark>~~ 

Clear Legacy FIFO operation does not clear IFLAGs, except when MCR[DMA] is asserted; in this case only IFLAG1[BUF5I] is cleared. 

### 72.3.10 CAN protocol related features 

This section describes the CAN protocol related features. 

#### 72.3.10.1 CAN FD ISO compliance 

The CAN FD protocol has been improved to increase the failure detection capability that was in the original CAN FD protocol, which is also called non-ISO CAN FD, by CAN in Automation (CiA). A three-bit stuff counter and a parity bit have been introduced in the improved CAN FD protocol, now called ISO CAN FD. The CRC calculation has also been modified. All these improvements make the ISO CAN FD protocol incompatible with the non-FD CAN FD protocol. The non-ISO CAN FD is still supported by FlexCAN so that it can be used mainly during an intermediate phase, for evaluation and development purposes. 

Therefore, it is strongly recommended to configure FlexCAN to the ISO CAN FD protocol by setting the ISOCANFDEN field in the CTRL2 register. 

#### 72.3.10.2 CAN FD frames 

The ISO 11898-1:2015 standard specifies the Classical Frame format compliant to ISO 11898-1:2003 (2003) and introduces the CAN Flexible Data Rate Frame format. The Classical Frame format allows bit rates up to 1 Mbit/s and payloads up to 8 bytes per frame. The Flexible Data Rate Frame format allows bit rates higher than 1 Mbit/s and payloads longer than 8 bytes per frame. FlexCAN can receive and transmit CAN FD messages interleaved with Classical CAN messages. 

There are three additional control bits in the CAN FD frame. The Extended Data Length (EDL) bit enables a longer data payload with different data length coding. The Bit Rate Switch (BRS) bit decides whether the bit rate is switched inside a CAN FD format frame. The Error State Indicator (ESI) flag is transmitted dominant by error active nodes, and recessive by error passive nodes. There are no Remote Frames (see Remote frames) in the CAN FD format. A message configured to transmit a Remote Frame is always sent out in the Classical CAN format. When an FD frame is received and matches a mailbox, the RTR bit in the receiving message buffer is negated. The RTR bit must be considered in classical frames only. 

CAN FD messages may be formatted as long frames where the data field exceeds 8 bytes, and may range from 12 up to 64 bytes. They can also be configured to support bit rate switching, where the control field, the data field, and the CRC field of a CAN frame are transmitted with a higher bit rate than the beginning and the end of the frame. Messages in Classical CAN format are limited to transport a maximum payload of 8 bytes at nominal rate. The following figure illustrates the message formats for Classical and FD frames with either standard or extended ID. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2743 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2744-02.png)


<!-- Start of picture text -->
CAN Standard Format<br>S R I<br>R<br>O ID STANDARD T D DLC<br>0<br>F R E<br>Arbitration Field Control Field<br>CAN FD Standard Format<br>Arbitration Phas e Data Phase<br>S R I E r B E<br>O ID STANDARD R D D e R S DLC<br>F S E L s S I<br>Arbitration Field Control Field<br>CAN Extended Format<br>S S I R<br>R R<br>O ID STANDARD R D ID EXTENDED T 1 0  DLC<br>F R E R<br>Arbitration Field Control Field<br>CAN FD Extended Format<br>Arbitration Phase Data Phase<br>S S I R E r B E<br>O ID STANDARD R D ID EXTENDED R D e R S DLC<br>F R E S L s S I<br>Arbitration Field Control Field<br><!-- End of picture text -->

##### Figure 378. CAN message formats 

The ability to receive and transmit CAN FD messages is enabled by MCR[FDEN]. Either a recessive R0 bit in CAN frames with 11-bit identifiers or a recessive R1 bit in CAN frames with 29-bit identifiers are decoded as an EDL bit (not a reserved one). A CAN FD frame is recognized by a recessive EDL bit, and a Classical CAN frame is recognized by a dominant EDL bit. The BRS bit specifies whether this frame switches the bit rate in its data phase. A long frame is decoded in accordance with the DLC field value (see DLC definition in Message buffer structure). 

CAN FD messages can be transmitted with two different bit rates. The first part of a CAN FD frame, from the Start Of Frame (SOF) bit until the Bit Rate Switch (BRS) bit, also called the arbitration phase, is transmitted with the nominal bit rate based on a set of nominal CAN bit timing configuration values. The second part, from the BRS bit until the CRC Delimiter bit, also named the data phase, is transmitted with the data bit rate defined by a second set of CAN data bit timing configuration values. Finally, from the CRC Delimiter until the Intermission bits, the transmission returns to nominal bit rate. In CAN FD frames with bit rate switching, the bit timing is changed inside the frame at the sample point of the BRS bit if this bit is recessive. Before the BRS bit, in the CAN FD arbitration phase, the nominal CAN bit timing is used as defined by the CBT register (also by CTRL1 register for backward compatibility). Upon detecting a recessive BRS bit, the CAN data bit timing is used as defined by the FDCBT register. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2744 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

~~<mark>NOTE</mark>~~ 

If the length of the time quantum in the nominal bit timing and the length of the time quantum in the data bit timing are not identical, a quantization error of up to one time quantum of the arbitration phase may be present as a phase error. This situation can occur after the switch from arbitration to data phase and will last until the next synchronization event. Thus, the length of the time quantum should be the same in nominal and data bit timing in order to minimize the chance of error frames on the CAN bus, and to optimize the clock tolerance in networks that use FD frames. 

FDCTRL[FDRATE] enables the transmission of all frames with bit rate switching if the BRS bit in the selected Tx MB is set. If FDRATE is negated, the transmission is performed at nominal rate regardless of the BRS bit value. FDCTRL[FDRATE] can be written any time but takes effect only for the next message transmitted or received. 

The nominal bit timing is resumed at either the sample point of the CRC Delimiter bit or when an error is detected, whichever occurs first. The following figure describes the mechanism for entering and leaving the data phase when BRS bit is recessive. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2745-06.png)


<!-- Start of picture text -->
CAN FD Frame<br>Arbitration Phase Data Phase Arbitration Phase<br>C A<br>R C<br>S B C A K S<br>O ID R DATA CRC D C D EOF O<br>F S E K E F<br>L L<br>Arbitration Field Control Field Data Field CRC Field<br>BRS Bit CRC Delimiter Bit<br>S S<br>Y Y<br>PROPSEG PSEG1 FPSEG2 FPROPSEG FPSEG1 PSEG2<br>N N<br>C C<br>Sample Point Sample Point<br>Nominal Bit Time Data Bit Time<br>S S<br>Y Y<br>PROPSEG PSEG1 PSEG2 FPROPSEG FPSEG1 FPSEG2<br>N N<br>C C<br>Sample Point Sample Point<br><!-- End of picture text -->

Figure 379. Bit rate switching mechanism for CAN FD messages 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2745 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

~~<mark>NOTE</mark>~~ 

In Classical CAN frames, the CRC delimiter is one single recessive bit. In CAN FD frames, the CRC delimiter may consist of one or two recessive bits. FlexCAN sends only one recessive bit as the CRC delimiter, but it accepts two recessive bits before the edge from recessive to dominant that starts the acknowledge slot. As a receiver, FlexCAN sends its acknowledge bit after the first CRC delimiter bit. In CAN FD frames, FlexCAN accepts a two-bit dominant ACK slot as a valid ACK to compensate for phase shifts between the receivers. 

The maximum configurable bit rate in the CAN FD data phase depends on the clock frequency of CAN_PE subblock. For example, with a CAN_PE clock frequency of 40 MHz and the shortest configurable bit time of 5 time quanta, the bit rate in the data phase is 8 Mbit/s.<sup>[11]</sup> 

The value of the ESI bit is determined either by the transmitter's error state at the start of the transmission, if the frame is originated in the FlexCAN node, or by the original transmitting node in case FlexCAN is acting as a gateway for the message. If the transmitter is error passive, ESI is transmitted recessive; otherwise, it is transmitted dominant. The permutations of the relationship between the written value and the transmitted value of the ESI are shown in this table. 

Table 447. Written versus transmitted values of ESI field 

|FlexCAN fault confinement status at<br>start of frame|ESI bit Of Tx MB|Transmitted ESI|
|---|---|---|
|Error active|0|0 (Error Active)|
|Error passive|0|1 (Error Passive)|
|Error active|1|1 (Error Passive)|
|Error passive|1|1 (Error Passive)|



There are different CRC polynomials for different CAN frame formats. The first polynomial, CRC_15, is used for all frames in Classical CAN format. The second, CRC_17, is used for frames in CAN FD format with a data field up to sixteen bytes long. The third, CRC_21, is used for frames in CAN FD format with a data field longer than sixteen bytes. Each polynomial results in a Hamming distance of 6. At the start of the frame, all three CRC polynomials are calculated concurrently. The CRC sequence to be transmitted is selected by the values of the EDL bit and the DLC bit field. When receiving a message, FlexCAN decodes EDL and DLC to select the adequate CRC polynomial to check for a CRC error. 

In CAN FD format frames, stuff bits are included in the bit stream for CRC calculation. In Classical CAN format frames, stuff bits are not included. After the transmission of the last bit relevant to the CRC calculation, the FDCRC register stores the calculated CRC for the transmitted message, with the adequate length in accordance to the type of message, for both CAN FD and non-FD messages. The CRCR register reports a valid CRC for Classical CAN messages only. 

In CAN FD format frames, the CAN bit stuffing method is changed for the CRC sequence so that the stuff bits are inserted at fixed positions. When FlexCAN is transmitting a CAN FD frame, a fixed stuff bit is inserted just before the first bit of the CRC sequence, even if the last bits of the preceding field do not fulfill the CAN stuff condition. Additional stuff bits are inserted after each fourth bit of the CRC sequence. The value of any fixed stuff bit is the inverse value of its preceding bit. When FlexCAN is receiving a CAN FD frame, it discards the fixed stuff bits from the bit stream for the CRC check. A stuff error is detected if the fixed stuff bit has the same value as its preceding bit. 

FlexCAN detects errors in CAN FD frames the same way as in Classical CAN frames. The error counters RXERRCNT and TXERRCNT in the ECR register accumulate the counts of Rx and Tx errors, respectively, for both FD and non-FD frames indiscriminately. There are two extra error counters (RXERRCNT_FAST and TXERRCNT_FAST) that accumulate Rx and Tx errors occurring in the data phase of CAN FD frames with the BRS bit set only. The rules for updating the error counters are the same for both CAN FD and non-FD frames (see ECR register). 

Error Flags BITERR1, BITERR0, ACKERR, CRCERR, FRMERR, and STFERR in the ESR1 register report errors in both CAN FD and non-FD frames. They also generate the ERRINT interrupt if CTRL1[ERRMSK] is asserted. The ESR1 register has additional error flags (BITERR1_FAST, BITERR0_FAST, CRCERR_FAST, FRMERR_FAST, and STFERR_FAST) to individually indicate 

> [11] The frequency used in this example may not be supported on this chip; it is shown only to demonstrate how the maximum configurable bit rate is calculated. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2746 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

the occurrence of errors in the data phase of CAN FD frames with the BRS bit set. There is no ACKERR detected in the data phase of a CAN FD frame. Fault confinement status reported in ESR1[FLTCONF] is the same for both CAN FD and Classical CAN frames, and is based on RXERRCNT and TXERRCNT error counters only. Information contained in RXERRCNT_FAST and TXERRCNT_FAST counters may be considered as status to help detect the error nature related to the bit rate value. 

When FlexCAN is in the data phase, either transmitting or receiving a CAN FD message, and detects an error, it immediately switches back to the arbitration phase and to the nominal rate to start an error flag. 

Resynchronization and hard synchronization occur in CAN FD frames in the same way as in Classical CAN ones. Additionally, a hard synchronization is also performed at the recessive to dominant edge from EDL to R0 in CAN FD format frames. FlexCAN does not resynchronize while transmitting in the CAN FD data phase. 

#### 72.3.10.3 Transceiver delay compensation 

The CAN FD protocol allows the transmission and reception of data at a higher bit rate than the nominal rate used in the arbitration phase when the message's BRS bit is set. This feature enables the use of rates up to 8 Mbps. 

During the data phase of a CAN FD frame, the transmitter detects a bit error if it cannot receive its own latest transmitted bit at the sample point of that bit. When bit rate switching is enabled (BRS bit is asserted), the length of the CAN bit time in the data phase can become shorter than the transceiver's loop delay, thus impeding the correct comparison between the transmitted bit and the received bit within the current CAN bit time interval. 

Note that the TDC process defines a secondary sample point where the transmitted bit is correctly compared with the received bit in order to check for bit errors. 

The TDC mechanism can be enabled by FDCTRL[TDCEN] or ETDC[ETDCEN] and is effective only during the data phase of FD frames having the BRS bit set. It has no effect either on non-FD frames, or on FD frames transmitted at normal bit rate. The TDC is active from the sample point of the BRS bit until the sample point of the CRC Delimiter bit, provided the respective message under transmission has the BRS bit set. When it is active, a comparison is done between the real received bit and the delayed transmitted bit, where the delay is calculated based on the measured transceiver loop delay. 

~~<mark>NOTE</mark>~~ 

The actual value of the CRC Delimiter bit is disregarded by transmitters using the transceiver delay compensation mechanism. A global error at the end of the CRC field will cause the receivers to send error frames that the transmitter will detect during Acknowledge or End of Frame. 

For every transmitted FD frame having the BRS bit set, the delay measurement is triggered by the transition from the recessive EDL bit to the dominant R0 bit (as shown in the next figure). The loop delay is measured in Protocol Engine (PE) clock periods (CANCLK, see Protocol timing), from the transmitted EDL-R0 edge to the received EDL-R0 edge. The position of the secondary sample point is defined by the measured loop delay time added to an offset value specified in FDCTRL[TDCOFF] or ETDC[ETDCOFF]. FDCTRL[TDCVAL] or ETDC[ETDCVAL] stores the result of this calculation. The TDCVAL and ETDCVAL value saturates at its maximum value of 63 CANCLK and 255 CANCLK when the delay measurement is too long. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2747-13.png)


<!-- Start of picture text -->
Arbitration Phase Data Phase<br>E r B E<br>Tx output D e R S DLC<br>L s S I<br>Loop delay Rate Switch Point<br>E r B E<br>Rx input D e R S DLC<br>L s S I<br>Arbitration Phase Data Phase<br>Figure 380. Transceiver loop delay measurement<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2747 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

The measured loop delay is not enough to be used to define the secondary sample point because it relates to the CAN bit edges. The transceiver delay compensation offset TDCOFF or ETDCOFF is used to shift the secondary sample point from the edge to an intermediate point inside the bit time, far away from its edges. Therefore, the TDCOFF or ETDCOFF value cannot be larger than the CAN bit duration in the data phase. 

If the secondary sample point is set very near the CAN bit edge (SYNC field), then problems may occur during the bit sampling in the data phase. For the TDC to work reliably, the offset has to use optimal settings. To be sure the bit sampling is performed in the best region, the TDC offset should be configured as shown in this equation: 

Offset = (FPSEG1 + FPROPSEG + 2) x (FPRESDIV + 1) or Offset = (DTSEG1 + 2) x (EDPRESDIV + 1), if ETDCEN 

The following figure shows the SSP position when these settings are used. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2748-06.png)


<!-- Start of picture text -->
TX output<br>SSP<br>RX input<br>TDC measurement TDC Offset<br>SSP position<br>Figure 381. SSP position with optimal values<br>TX output<br>SSP<br>RX input<br>TDC Offset<br>SSP position<br>Figure 382. SSP position—TDC measurement disabled by ETDCEN and TDMDIS<br><!-- End of picture text -->

Alternatively, if CTRL2[BTE] and ETDC[ETDCEN] are set, the TDMDIS bit can be set to disable the transceiver delay measurement. In this case, the SSP position is defined only by the ETDCOFF field. Figure 382 shows the secondary sample point position when the transceiver delay measurement is disabled. 

During the data phase of CAN FD frames with bit rate switching enabled, at the onset of every Tx CAN bit, the transmitted Tx bit value is temporarily stored in a buffer and a time countdown based on FDCTRL[TDCVAL] or ETDC[ETDCVAL] is started which ends with the comparison of the received Rx bit (delayed by the external loop delay plus the specified offset) with the stored Tx bit. If a bit error is detected at the secondary sample point, the FlexCAN issues an error flag to the CAN bus at the next sample point. 

During the arbitration phase the delay compensation is always disabled. The maximum delay which can be compensated by the FlexCAN's transceiver delay compensation during the data phase is 3 CAN bit times – 2 Tq. Beyond this limit, the FDCTRL[TDCFAIL] or ETDC[ETDCFAIL] flag is set to indicate when the transceiver delay compensation mechanism is out of range, unable to compensate the transceiver loop delay. 

#### 72.3.10.4 Remote frames 

A remote frame is a special kind of frame. You can program a mailbox to be a remote request frame by configuring the mailbox as Transmit with the RTR bit set to one. After the remote request frame is transmitted successfully, the mailbox becomes a receive message buffer, with the same ID as before. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2748 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

When a remote request frame is received by FlexCAN, it can be treated in four ways, depending on remote request storing (CTRL2[RRS]) and Rx FIFO Enable (MCR[RFEN]): 

- If RRS is negated the frame's ID is compared to the IDs of the transmit message buffers with the CODE field 1010b. If there is a matching ID, then this mailbox frame will be transmitted. Note that if the matching mailbox has the RTR bit set, then FlexCAN will transmit a remote frame as a response. The received remote request frame is not stored in a receive buffer. It is only used to trigger a transmission of a frame in response. The mask registers are not used in remote frame matching, and all ID bits (except RTR) of the incoming received frame should match. In the case that a remote request frame is received and matches a mailbox, this message buffer immediately enters the internal arbitration process, but is considered as a normal Tx mailbox, with no higher priority. The data length of this frame is independent of the DLC field in the remote frame that initiated its transmission. 

- If RRS is asserted the frame's ID is compared to the IDs of the receive mailboxes with the CODE field 0100b, 0010b, or 0110b. If there is a matching ID, then this mailbox will store the remote frame in the same fashion of a data frame. No automatic remote response frame will be generated. The mask registers are used in the matching process. 

- If RFEN is asserted FlexCAN will not generate an automatic response for remote request frames that match the Legacy FIFO filtering criteria. If the remote frame matches one of the target IDs, it will be stored in the Legacy FIFO and presented to the CPU. Note that for filtering formats A and B, it is possible to select whether remote frames are accepted or not. For format C, remote frames are always accepted (if they match the ID). Remote request frames are considered as normal frames, and generate a Legacy FIFO overflow when a successful reception occurs and the Legacy FIFO is already full. 

- If ERFEN is set, FlexCAN will not generate an automatic response for remote request frames that match the Enhanced Rx FIFO filtering criteria. Remote Request Frames are considered normal frames, and generate an Enhanced Rx FIFO overflow when a successful reception occurs and Enhanced Rx FIFO is already full. 

~~<mark>NOTE</mark>~~ 

There is no remote frame in the CAN FD format. The RTR bit is replaced by a fixed dominant RRS bit. FlexCAN receives and transmits remote frames in the Classical CAN format. 

#### 72.3.10.5 Overload frames 

FlexCAN does transmit overload frames when the following conditions are detected on the CAN bus: 

- Detection of a dominant bit in the first/second bit of Intermission 

- Detection of a dominant bit at the 7th bit (last) of End of Frame field (Rx frames) 

- Detection of a dominant bit at the 8th bit (last) of Error Frame Delimiter or Overload Frame Delimiter 

#### 72.3.10.6 Message buffer time stamp 

The value of the free running timer is sampled at the beginning of the Identifier field on the CAN bus, and is stored at the end of move-in in the TIME STAMP field of message buffer, providing network behavior with respect to time. 

When CTRL2[TIMER_SRC] is asserted, the free running timer is continuously clocked by an external time tick. 

When CTRL2[TIMER_SRC] is negated, the free running timer is clocked by the FlexCAN bit-clock, which defines the baud rate on the CAN bus. During a message transmission/reception, it increments by one for each bit that is received or transmitted. When there is no message on the bus, it counts using the previously programmed baud rate. 

The free running timer is not incremented during Disable and Freeze modes. It can be reset upon a specific frame reception, enabling network time synchronization. See the TSYN description in Control 1 register (CTRL1). 

Alternatively, by configuring the MTSBASE field of the Control 2 register (CTRL2), the time stamp of the message buffer can capture the lower or higher 16 bits of the high-resolution dedicated counter. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2749 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

#### 72.3.10.7 High resolution time stamp 

The high-resolution time stamp, HR_TIME_STAMP, uses a dedicated timer with a 32-bit counter operating in free running mode. The high-resolution time stamp is enabled by the TSTAMPCAP field of the Control 2 register (CTRL2). When this field is not zero , the dedicated 32-bit counter value is captured during a valid CAN frame and stored in the HR_TIME_STAMP register. 

Each HR_TIME_STAMPn corresponds to a specific message buffer. For example, HR_TIME_STAMP0 stores the 32-bit time stamp associated with message buffer 0, HR_TIME_STAMP1 stores the 32-bit time stamp associated with message buffer 1, and so on. 

The counter value is captured according to the TSTAMPCAP field of the Control 2 register (CTRL2). For classical CAN frames, the capture points can be the start of frame bit or the point in time a CAN frame is considered valid, which is the seventh bit of end of frame for transmission and the sixth bit of end of frame for reception. For CAN FD frames, the capture points can be the start of frame, the point in time a CAN FD frame is considered valid, or the res bit of a CAN FD frame. 

The 16-bit time stamp of the message buffer can be configured to capture the lower or higher 16 bits of the high-resolution timer. This configuration is made by CTRL2[MBTSBASE]. 

#### 72.3.10.8 Protocol timing 

The following figure shows the structure of the clock generation circuitry that feeds the CAN Protocol Engine (PE) submodule. 

~~<mark>NOTE</mark>~~ Please see the clock distribution chapter (module clocks table) to identify the proper clock source. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2750-10.png)


<!-- Start of picture text -->
Oscillator Clock CANCLK Sclock<br>Prescaler<br>(Tq)<br><!-- End of picture text -->

Figure 383. CAN engine clocking scheme 

The FlexCAN module supports a variety of means to set up bit timing parameters that are required by the CAN protocol. The Control 1 register (CTRL1) has various fields used to control bit timing parameters: PRESDIV, PROPSEG, PSEG1, PSEG2, and RJW. 

The CAN Bit Timing register (CBT) extends the range of the CAN bit timing variables in CTRL1. The CAN FD Bit Timing register (FDCBT) provides a second set of CAN bit timing variables to be applied at the data phase of CAN FD frames with the Bit Rate Switch (BRS) set. 

The Enhanced Nominal CAN bit timing register (ENCBT) extends the range of CAN bit timing variables in CBT. The Enhanced Data Phase CAN bit timing register (EDCBT) extends the range of CAN bit timing variables in FDCBT. When using ENCBT and EDCBT, the bit timing nominal and data phase serial clock (Sclock) dividers must be programed in the Enhanced CAN Bit Timing Prescalers register (EPRS). 

~~<mark>NOTE</mark>~~ When the CAN FD feature is enabled, always set CBT[BTF] or CTRL2[BTE] and configure the CAN bit timing variables in CBT or ENCBT. See CAN Bit Timing Register (CBT) or Enhanced Nominal CAN Bit Timing (ENCBT). 

The PRESDIV field (as well as its extended range EPRESDIV (or ENPRESDIV) and FDPRESDIV (or EDPRESDIV) for the data phase bits of CAN FD messages) defines the prescaler value (see the equation below) that generates the serial clock (Sclock), whose period defines the time quantum used to compose the CAN waveform. A time quantum (Tq) is the atomic unit of time managed by the CAN engine. It is the smallest time unit for all configuration values. 

(PRESDIV + 1) Tq = fCANCLK 

Equation 12. Time quantum 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2750 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

The bit rate, which defines the rate the CAN message is either received or transmitted, is given by the formula: 

CAN Bit Time = (Number of Time Quanta in 1 bit time) * Tq 

1 Bit Rate = CAN Bit Time 

Equation 13. CAN bit time and baud rate 

A bit time is subdivided into three segments<sup>[1]</sup> (see Figure 385, Figure 386 and Table 448): 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2751-07.png)


<!-- Start of picture text -->
NRZ Signal<br>Time Segment 1 Time Segment 2<br>SYNC_SEG<br>(NTSEG1 + 1) (NTSEG2 + 1)<br>1 2 ... 256 2 ... 128<br>8 ... 385 Time Quanta<br>= 1 Bit Time<br>Tq Tq<br>Transmit Point Sample Point<br>(single or triple sampling)<br>NRZ Signal<br>Time Segment 1 Time Segment 2<br>SYNC_SEG<br>(DTSEG1 + 1) (DTSEG2 + 1)<br>1 2 ... 32 2 ... 16<br>5 ... 49 Time Quanta<br>= 1 Bit Time<br>Transmit Point Sample Point<br>(single sampling)<br><!-- End of picture text -->

Figure 384. Segments within the bit timing (example using ENCBT and EDCBT bit timing variables) 

- SYNC_SEG: This segment has a fixed length of one time quantum. Signal edges are expected to happen within this section. 

- Time Segment 1: This segment includes the propagation segment and the phase segment 1 of the CAN standard. It can be programmed by setting CTRL1[PROPSEG] and CTRL1[PSEG1] so that their sum (plus 2) is in the range of 2 to 16 time quanta. When CBT[BTF] is asserted, FlexCAN uses EPROPSEG and EPSEG1 fields from CBT register so that their 

- [1] For further explanation of the underlying concepts, see ISO 11898-1 :2015. See also the CAN 2.0A/B protocol specification for bit timing. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2751 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

sum (plus 2) is in the range of 2 to 96 time quanta. For messages in CAN FD format with the BRS bit set, FlexCAN uses FDPROPSEG and FDPSEG1 from FDCBT instead, so that their sum (plus 1) is in the range of 2 to 39 time quanta. 

If CTRL2[BTE] is set, FlexCAN uses ENCBT[NTSEG1] to configure time segment 1 in the range of 2 to 256 time quanta. For the data phase in CAN FD messages with BRS set, EDCBT[DTSEG1] must be used for configuring time segment 1 in the range of 2 to 32 time quanta. 

- Time Segment 2: This segment represents the phase segment 2 of the CAN standard. It can be programmed by setting CTRL1[PSEG2] (plus 1) to be 2 to 8 time quanta long. When CBT[BTF] is asserted, FlexCAN uses EPSEG2 fields of CBT register so that its value (plus 1) is in the range of 2 to 32 time quanta. For messages in CAN FD format with the BRS bit set, FlexCAN uses FDPSEG2 from FDCBT instead, so that its value (plus 1) is in the range of 2 to 8 time quanta. The time segment 2 cannot be smaller than the Information Processing Time (IPT), which value is 2 time quanta in FlexCAN. 

If CTRL2[BTE] is set, FlexCAN uses ENCBT[NTSEG2] to configure time segment 2 in the range of 2 to 128 time quanta. For the data phase in CAN FD messages with BRS set, EDCBT[DTSEG2] must be used for configuring time segment 2 in the range of 2 to 16 time quanta. 

~~<mark>NOTE</mark>~~ 

The bit time defined by the above time segments must not be smaller than five time quanta. For bit time calculations, use an Information Processing Time (IPT) of two, which is the value implemented in the FlexCAN module. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2752-08.png)


<!-- Start of picture text -->
NRZ Signal<br>Time Segment 1 Time Segment 2<br>SYNC_SEG<br>(PROPSEG + PSEG1 + 2) (PSEG2 + 1)<br>1 2 ... 16 2 ... 8<br>8 ... 25 Time Quanta<br>= 1 Bit Time<br>Tq Tq<br>Transmit Point Sample Point<br>(single or triple sampling)<br><!-- End of picture text -->

Figure 385. Segments within the bit time (example using CTRL1 bit timing variables for Classical CAN format) 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2752 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2753-02.png)


<!-- Start of picture text -->
NRZ Signal<br>Time Segment 1 Time Segment 2<br>SYNC_SEG<br>(EPROPSEG + EPSEG1 + 2) (EPSEG2 + 1)<br>1 2 ... 96 2 ... 32<br>8 ... 129 Time Quanta<br>= 1 Bit Time<br>Tq Tq<br>Transmit Point Sample Point<br>(single or triple sampling)<br>NRZ Signal<br>Time Segment 1 Time Segment 2<br>SYNC_SEG<br>(FPROPSEG + FPSEG1 + 1) (FPSEG2 + 1)<br>1 2 ... 39 2 ... 8<br>5 ... 48 Time Quanta<br>= 1 Bit Time<br>Transmit Point Sample Point<br>(single sampling)<br><!-- End of picture text -->

Figure 386. Segments within the bit time (example using CBT and FDCBT bit timing variables for CAN FD format) 

Table 448. Time segment syntax 

|Syntax|Description|
|---|---|
|SYNC_SEG|System expects transitions to occur on the bus during this period.|
|TSEG1|Corresponds to the sum of PROPSEG and PSEG1.|
|TSEG2|Corresponds to the PSEG2 value.|
|Transmit point|A node in transmit mode transfers a new value to the CAN bus at this point.|
|Sample point|A node samples the bus at this point. If the three samples per bit option is selected, then this point<br>marks the position of the third sample.|



The following table gives some examples of the CAN compliant segment settings for Classical CAN format (Bosch CAN 2.0B) (non-FD) messages. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2753 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table 449. Bosch CAN 2.0B standard compliant bit time segment settings 

|Time segment 1|Time segment 2|Re-synchronization jump width|
|---|---|---|
|5 .. 10|2|1 .. 2|
|4 .. 11|3|1 .. 3|
|5 .. 12|4|1 .. 4|
|6 .. 13|5|1 .. 4|
|7 .. 14|6|1 .. 4|
|8 .. 15|7|1 .. 4|
|9 .. 16|8|1 .. 4|



~~<mark>NOTE</mark>~~ 

The user must ensure the bit time settings are in compliance with the CAN Protocol standard (ISO 11898-1:2015). 

Whenever CAN bit is used as a measure of time duration (for example, estimating the occurrence of a CAN bit event in a message), the number of peripheral clocks in one CAN bit (NumClkBit) can be calculated as: 

fSYS NumClkBit = x (PRESDIV + 1) x (PROPSEG + PSEG1 + PSEG2 + 4) fCANCLK 

Equation 14. Number of peripheral clocks per CAN bit when CTRL2[BTE] = 0 

or, if CTRL2[BTE] = 1: 

fSYS NumClkBit = x (ENPRESDIV + 1) x (NTSEG1 + NTSEG2 + 3) fCANCLK 

Equation 15. Number of peripheral clocks per CAN bit when CTRL2[BTE] = 1 

where: 

- NumClkBit is the number of peripheral clocks in one CAN bit. 

- fCANCLK is the Protocol Engine (PE) Clock (see Figure 383), in Hz. 

- fSYS is the frequency of operation of the system (CHI) clock, in Hz. 

- PSEG1 is the value in CTRL1[PSEG1] field. 

- PSEG2 is the value in CTRL1[PSEG2] field. 

- PROPSEG is the value in CTRL1[PROPSEG] field. 

- PRESDIV is the value in CTRL1[PRESDIV] field. 

- ENPRESDIV is the value in EPRS[ENPRESDIV] field. 

- NTSEG1 is the value in ENCBT[NTSEG1] field. 

- NTSEG2 is the value in ENCBT[NTSEG2] field. 

The formula above is also applicable to the alternative CAN bit timing variables described in the CAN Bit Timing register (CBT) or the Enhanced Nominal CAN bit timing (ENCBT) register and also to the CAN FD Bit Timing register (FDCBT) or the Enhanced Nominal CAN bit timing register(ENCBT). 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2754 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

For example, 180 CAN bits = (180 x NumClkBit) peripheral clock periods. 

#### 72.3.10.9 Arbitration and matching timing 

During normal reception and transmission, the matching, arbitration, move-in, and move-out processes are executed during certain time windows inside the CAN frame, as shown in the following figures. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2755-05.png)


<!-- Start of picture text -->
Start Move<br>(bit 2)<br>DLC DATA and/or CRC EOF Interm<br>Move-in<br>Matching Window (26 to 90 CAN bits) Window<br>Figure 387. Matching and move-in time windows<br>Start Arbitration Arb Start Move<br>(delayed by TASD) Process (bit 1)<br>CRC EOF Interm<br>Move-out<br>Window<br>Arbitration Window (25 CAN bits)<br>Figure 388. Arbitration and move-out time windows<br>BusOff<br>0 1 2 3 ... 123 124 125 126 ... 128<br>TASD Arb Move-out<br>Count Process Window<br>Internal Counter<br>counting 128 occurrences of 11 recessive CAN bits<br>Figure 389. Arbitration at the end of bus off and move-out time windows<br><!-- End of picture text -->

~~<mark>NOTE</mark>~~ 

In the preceding figures, the matching and arbitration timing does not take into account the delay caused by the concurrent memory access due to the CPU or other internal FlexCAN subblocks. 

#### 72.3.10.10 Tx arbitration start delay 

CTRL2[TASD] (Tx Arbitration Start Delay) is a variable that indicates the number of CAN bits used by FlexCAN to delay the Tx arbitration process start point from the first bit of CRC field of the current frame. This variable can be written only in Freeze mode because it is blocked by hardware in other modes. 

The transmission performance is impacted by the ability of the CPU to reconfigure message buffers (MBs) for transmission after the end of the internal arbitration process, where FlexCAN finds the winner MB for transmission (see Arbitration process). If the arbitration ends too early before the first bit of Intermission field, then there is a chance that the CPU reconfigures some Tx MBs and the winner MB is no longer the best candidate to be transmitted. 

TASD is useful to optimize the transmission performance by defining the arbitration start point, as shown in the next figure, based on factors such as: 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2755 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

- Peripheral-to-oscillator clock ratio 

- CAN bit timing variables that determine the CAN bit rate 

- Number of message buffers (MBs) in use by the matching and arbitration processes 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2756-05.png)


<!-- Start of picture text -->
Data bit rate when CAN FD is enabled Nominal bit rate<br>9 last CAN bits<br>Arbitration<br>start point<br>A S<br>C O<br>CRC K EOF Intermission F<br>Arbitration<br>Process<br>TASD countdown<br>Arbitration window (25 to 31 CAN bits)<br><!-- End of picture text -->

Figure 390. Optimal Tx Arbitration start point 

The duration of an arbitration process, in terms of CAN bits, is directly proportional to the number of available MBs and to the CAN bit rate, and inversely proportional to the peripheral clock frequency. 

The optimal arbitration timing is that in which the last MB is scanned just before the first bit of the Intermission field of a CAN frame. For instance, if there are few MBs and the peripheral/oscillator clock ratio is high and the CAN baud rate is low, then the arbitration can be placed closer to the frame's end, adding more delay to its start point, and vice-versa. 

If TASD is set to 0 then the arbitration start is not delayed and more time is reserved for arbitration. On the other hand, if TASD is close to 24 then the CPU can configure a Tx MB later and less time is reserved for arbitration. If too little time is reserved for arbitration the FlexCAN may be not be able to find a winner MB in time to be transmitted with the best chance to win the bus arbitration against external nodes on the CAN bus. 

The optimal TASD value can be calculated as follows: 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2756-11.png)


<!-- Start of picture text -->
For CAN FD frames and (MAXMB + 1) ≤ NMBEND<br>2 * (MAXMB + 1 ) + 4<br>TASD = 31 -<br>CPCBN<br>For CAN FD frames and (MAXMB + 1) > NMBEND<br>2 * (MAXMB + 1 ) - NMBEND<br>TASD = 22 -<br>CPCBF<br>For non-FD frames<br>2 * (MAXMB + 1 ) + 4<br>TASD = 25 -<br>CPCB<br>Equation 16. Optimal value for TASD<br><!-- End of picture text -->

where: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2756 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2757-02.png)


<!-- Start of picture text -->
(9 * CPCBN) - 4<br>NMBEND =<br>2<br>fCANCLK<br>BITRATEN =<br> [1 + (EPSEG1 + 1) + (EPSEG2 + 1) + (EPROPSEG + 1) ] x (EPRESDIV + 1)<br>fCANCLK<br>BITRATEF =<br> [1 + (FPSEG1 + 1) + (FPSEG2 + 1) + FPROPSEG] x (FPRESDIV + 1)<br>fSYS<br>CPCBN =<br>BITRATEN<br>fSYS<br>CPCBF =<br>BITRATEF<br>CPCB = CPCBN<br>Equation 17. Variables used in TASD calculation<br><!-- End of picture text -->

- MAXMB is the value in CTRL1[MAXMB]. 

- NMBEND is the number of message buffers that can be scanned by the arbitration process during the 9 last CAN bits at the end of a frame (see the figure above). 

- BITRATEN is the CAN bit rate in bits per second calculated by the nominal CAN bit time variables. 

- BITRATEF is the CAN bit rate in bits per second calculated by the data CAN bit time variables. 

- CPCBN is the number of peripheral clocks per CAN bit in nominal bit rate for CAN FD frames. 

- CPCBF is the number of peripheral clocks per CAN bit in data bit rate for CAN FD frames. 

- CPCB is the number of peripheral clocks per CAN bit for non-FD frames. 

- fCANCLK is the oscillator clock, in Hz. 

- fSYS is the peripheral clock, in Hz. 

- EPSEG1 is the value in CBT[EPSEG1] (CTRL1[PSEG1] can also be used). 

- EPSEG2 is the value in CBT[EPSEG2] (CTRL1[PSEG2] can also be used). 

- EPROPSEG is the value in CBT[EPROPSEG] (CTRL1[PROPSEG] can also be used). 

- EPRESDIV is the value in CBT[EPRESDIV] (CTRL1[PRESDIV] can also be used). 

- FPSEG1 is the value in FDCBT[FPSEG1]. 

- FPSEG2 is the value in FDCBT[FPSEG2]. 

- FPROPSEG is the value in FDCBT[FPROPSEG]. 

- FPRESDIV is the value in FDCBT[FPRESDIV]. 

- NTSEG1 is the value in ENCBT[NTSEG1]. 

- NTSEG2 is the value in ENCBT[NTSEG2]. 

- ENPRESDIV is the value in EPRS[ENPRESDIV]. 

- DTSEG1 is the value in EDCBT[DTSEG1]. 

- DTSEG2 is the value in EDCBT[DTSEG2]. 

- EDPRESDIV is the value in EPRS[EDPRESDIV]. 

If CTRL2[BTE] is set, then: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2757 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

fCANCLK BITRATEN = [1 + (NTSEG1 + 1) + (NTSEG2 + 1)] x (ENPRESDIV + 1) 

Equation 18. Nominal baud rate when CTRL2[BTE] = 1 

fCANCLK BITRATEF = [1 + (DTSEG1 + 1) + (DTSEG2 + 1)] x (EDPRESDIV + 1) 

Equation 19. Fast baud rate when CTRL2[BTE] = 1 

See also Protocol timing for more details. 

The following tables give the TASD value calculated for some configuration cases. 

##### Case 1: 

- Clock ratio = 2:1 (example: peripheral clock 80 MHz and oscillator clock 40 MHz) 

- Bit rate in arbitration phase = 1 Mbaud 

##### Table 450. TASD values: 

|Number of message buffers|TASD value|Maximum bit rate in data phase (MBd)|
|---|---|---|
|16|24|Invalid|
|32|24|8.0|
|64|23|8.0|
|96|22|8.0|



##### Case 2: 

- Clock ratio = 1:1 (example: peripheral clock 40 MHz and oscillator clock 40 MHz) 

- Bit rate in arbitration phase = 1 Mbaud 

##### Table 451. TASD values: 

|Number of message buffers|TASD value|Maximum bit rate in data phase (MBd)|
|---|---|---|
|16|24|Invalid|
|32|23|6.67|
|54|22|5.0|
|64|21|3.33|
|96|20|1.6|



##### Case 3: 

- Clock ratio = 2:1 (example: peripheral clock 40 MHz and oscillator clock 20 MHz) 

- Bit rate in arbitration phase = 1 Mbaud 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2758 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table 452. TASD values: 

|Number of message buffers|TASD value|Maximum bit rate in data phase (MBd)|
|---|---|---|
|16|24|Invalid|
|32|23|4.0|
|54|22|4.0|
|64|21|3.33|
|96|20|1.54|



### 72.3.11 Clocks 

The following table describes the clock sources for FlexCAN. Please see chip clocking chapter for clock setting, configuration and gating information. 

Table 453. FlexCAN clocks 

|Clock name|Description|
|---|---|
|ipg_clk|Peripheral clock|
|ipg_clk_chi|Control Host Interface (CHI) clock|
|ipg_clk_pe|Protocol Engine (PE) clock|
|ipg_clk_pe_nogate|Protocol Engine clock (no gating)|
|ipg_clk_s|Peripheral access clock|



#### 72.3.11.1 Clock domains and restrictions 

The FlexCAN module has two clock domains asynchronous to each other: 

- The bus domain feeds the Control Host Interface (CHI) submodule. 

- The oscillator domain feeds the CAN Protocol Engine (PE) submodule. 

When the two domains are connected to clocks with different frequencies and/or phases, there are restrictions on the frequency relationship between the two clock domains. In the case of asynchronous operation, the bus domain clock frequency must always be greater than the oscillator domain clock frequency. 

~~<mark>NOTE</mark>~~ 

Asynchronous operation with a 1:1 ratio between peripheral and oscillator clocks is not allowed. 

When doing matching and arbitration, FlexCAN needs to scan the whole message buffer memory during the time slot of one CAN frame, comprised of a number of CAN bits. In order to have sufficient time to do that, the following requirements must be observed: 

- The peripheral clock frequency cannot be smaller than the oscillator clock frequency. 

- There must be a minimum number of peripheral clocks per CAN bit, as specified in the table shown below. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2759 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table 454. Minimum number of peripheral clocks per CAN bit for Classical CAN format 

|Number of mailboxes|Value of MCR[RFEN]|Value of ERFCR[ERFEN]|Minimum number of<br>peripheral clocks per CAN bit|
|---|---|---|---|
|16|0|0|16|
|32|0|0|16|
|64|0|0|25|
|96|0|0|37|
|16|1|0|16|
|32|1|0|17|
|64|1|0|30|
|96|1|0|42|
|16|0|1|16|
|32|0|1|19|
|64|0|1|31|
|96|0|1|42|



For classical frame format, the minimum number of peripheral clocks per CAN bit specified in the preceding table determines the minimum peripheral clock frequency for a given number of mailboxes and for an expected CAN bit rate. The CAN bit rate depends on the number of time quanta in a CAN bit, which can be defined by adjusting one or more of the bit timing values contained in either the Control 1 register (CTRL1) or CAN Bit Time register (CBT) or Enhanced Nominal CAN bit timing register (ENCBT). The time quantum (Tq) is defined in Protocol timing. The minimum number of time quanta per CAN bit must be 8; therefore, the oscillator clock frequency should be at least 8 times the CAN bit rate. 

For CAN FD frame format, there are some constraints that need to be satisfied. The number of peripheral clocks per CAN bit in nominal bit rate (NumClkNomBit) can be calculated by the equation below. 

|NumClkNomBit =|fSYS<br>fCANCLK|x (PRESDIV + 1) x (PROPSEG + PSEG1 + PSEG2 + 4)|
|---|---|---|
|=|fSYS<br>NomBitRate||



Equation 20. Number of peripheral clocks per nominal CAN bit 

where PRESDIV, PSEG1, and PSEG2 are CAN bit time values in CTRL1 register. Alternatively, EPRESDIV, EPSEG1, and EPSEG2 values in CBT register or the values of EPRS[ENPRESDIV], ENCBT[NTSEG1], and ENCBT[NTSEG2] can be used instead. NumClkNomBit can also be calculated as a function of the expected nominal bit rate used in the arbitration phase (NomBitRate), as shown in the equation above. 

The number of CAN bits in the data phase of an FD frame with the BRS bit set (fast CAN bits, in short) depends on the number of data bytes in the payload. The number of fast CAN bits (NumOfFastBits) can be determined in the table below. The fewer the number of data bytes, the fewer the number of fast CAN bits, and less time is available for FlexCAN to scan the whole message buffer memory during the internal matching and arbitration processes. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2760 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table 455. Number of fast CAN bits in a CAN FD frame 

|Minimum number of data bytes|DLC field|NumOfFastBits|
|---|---|---|
|0|0h|21|
|1|1h|29|
|2|2h|37|
|3|3h|45|
|4|4h|53|
|5|5h|61|
|6|6h|69|
|7|7h|77|
|8|8h|85|
|12|9h|117|
|16|Ah|149|
|20|Bh|186|
|24|Ch|218|
|32|Dh|282|
|48|Eh|410|
|64|Fh|538|



The critical part of a CAN FD frame is during the data phase, where the CAN bit rate is faster than in the arbitration phase. The minimum number of peripheral clocks per fast CAN bit (MinNumClkFastBit) can be calculated to guarantee that enough time is available for FlexCAN to scan the message buffer memory during reception and transmission. The equation below calculates this constraint. 

|MinNumClkFastBitA=<br>(8.5 x MaxNumOfMb)|+ [ERFEN x(2 x NFE + 4)] + 64 -(9 x NumClkNomBit)<br>NumOfFastBits|
|---|---|



Equation 21. Minimum number of peripheral clocks per fast CAN bit for FlexCAN scan process 

where MaxNumOfMb is the maximum number of available mailboxes defined in MCR[MAXMB]. NFE and ERFEN are the fields defined in ERFCR register. 

The clock domain crossing circuit between the CHI and PE subblocks also imposes a minimum number of peripheral clocks per fast CAN bit for the handshake mechanism to work properly without losing status information through the interface, as shown in the equation below. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2761 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

fSYS MinNumClkFastBitB = 3 x 1 + fCANCLK 

Equation 22. Minimum number of peripheral clocks per fast CAN bit for FlexCAN clock domain interface 

Therefore, the minimum number of peripheral clocks per fast CAN bit (MinNumClkFastBit) is determined by the larger of the two values calculated above. 

MinNumClkFastBit = Maximum ( MinNumClkFastBitA, MinNumClkFastBitB ) 

Equation 23. Minimum number of peripheral clocks per fast CAN bit 

Then, the maximum CAN bit rate in the data phase of CAN FD frames (DataBitRateMAX) can be calculated as below. 

|DataBitrateMAX=<br>ROUNDUP|fCANCLK<br>MinNumClkFastBit x fCANCLK<br>fSYS|
|---|---|



Equation 24. Maximum achievable baud rate for data phase 

The peripheral and oscillator clock frequencies, the maximum number of mailboxes, and the expected nominal bit rate affect the maximum data bit rate attainable by FlexCAN in CAN FD mode. Also, the data bit rate depends on the minimum payload size of FD frames used in a given application. 

To illustrate how the CAN FD bit rate is affected by the configuration of FlexCAN variables, an application example with the peripheral and oscillator clock frequencies set to 50 MHz and 40 MHz, respectively, is considered. 

1. Considering the nominal bit rate as 1 Mbps, the number of peripheral clocks per CAN bit in nominal bit rate is calculated as below. 

50 x 10<sup>6</sup> NumClkNomBit = = 50 1 x 10<sup>6</sup> 

Equation 25. Calculation example for number of peripheral clocks per nominal CAN bit 

2. The number of fast CAN bits (NumOfFastBits) is determined in the table presented above. For example, if the minimum payload in FD frames is 8 bytes, then there are 85 CAN bits in the data phase. 

3. Assuming the maximum number of mailboxes is 96, and Enhanced Rx FIFO is disabled, the minimum number of peripheral clocks per fast CAN bit (MinNumClkFastBit) can be calculated. 

(8.5 x 96) + 64 - (9 x 50) MinNumClkFastBitA = = 5.06 85 

Equation 26. Calculation example for number of peripheral clocks per fast CAN bit for FlexCAN scan process 

50 MinNumClkFastBitB = 3 x 1 + 40 = 6.75 

Equation 27. Calculation example for number of peripheral clocks per fast CAN bit for FlexCAN clock domain interface 

MinNumClkFastBit = Maximum (5.06, 6.75) = 6.75 

Equation 28. Calculation example for number of peripheral clocks per fast CAN bit 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2762 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

4. The maximum CAN bit rate in the data phase can finally be found. 

|DataBitRateMAX=<br>40<br>ROUNDUP|x 10<sup>6</sup><br>6.75 x 40 x 10<sup>6</sup><br>50 x 10<sup>6</sup>|= 6.667 Mbps|
|---|---|---|



Equation 29. Calculation example for maximum achievable baud rate 

As demonstrated in this example, even though the oscillator clock frequency (40 MHz) is adequate to generate a data rate of 8 Mbps in CAN FD mode, the specific FlexCAN configuration limits this rate to 6.667 Mbps. This limitation is mainly due to the low peripheral clock frequency that imposes the MinNumClkFastBitB bound. 

The table below shows the maximum data rate for CAN FD with Enhanced RX FIFO disabled according to clock frequencies, payload size, and number of available mailboxes. See in this table that, for some cases, if the number of available mailboxes is reduced, the FlexCAN can then achieve a data rate up to 8 Mbps. 

Table 456. Maximum CAN bit rate in data phase on CAN FD frames with Enhanced Rx FIFO disabled 

|Peripheral clock<br>frequency (MHz)|Payload size|Number of<br>available mailboxes|Maximum data rate (Mbps)|
|---|---|---|---|
|40|8|94|6.667|
|40|8|114|5.0|
|40|12|117|6.667|
|40|12|128|5.714|
|50|12 to 64|128|6.667|
|60|8|126|8.0|
|60|12|128|8.0|
|67|6|128|8.0|
|80|3|128|8.0|
|100|0|128|8.0|



### 72.3.12 Reset 

You can reset FlexCAN in the following ways: 

1. Chip level hard reset, which resets all memory-mapped registers asynchronously. 

2. MCR[SOFTRST], which resets some of the memory-mapped registers synchronously. See Table 459 to see what registers are affected by soft reset. 

Soft reset is synchronous and has to follow an internal request/acknowledge procedure across clock domains. Therefore, it may take some time to fully propagate its effects. MCR[SOFTRST] remains asserted while soft reset is pending, so software can poll this bit to know when the reset has completed. Also, soft reset cannot be applied while clocks are shut down in a low-power mode. The low-power mode should be exited and the clocks resumed before applying soft reset. 

When the module is enabled (MCR[MDIS] negated), FlexCAN automatically enters Freeze mode. In Freeze mode, FlexCAN is un-synchronized to the CAN bus, MCR[HALT] and MCR[FRZ] are set, the internal state machines are disabled, then MCR[FRZACK] and MCR[NOTRDY] are set. The Tx pin is in recessive state and FlexCAN does not initiate any transmission or 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2763 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

reception of CAN frames. Note that the message buffers and the Rx Individual Mask registers are not affected by reset, so they are not automatically initialized. 

### 72.3.13 Interrupts 

The module has many interrupt sources: interrupts due to message buffers and interrupts due to the ORed interrupts from MBs, Bus Off, Bus Off Done, Error, Error Fast (errors detected in the data phase of CAN FD format messages with the BRS bit set), Tx Warning, and Rx Warning. 

Each one of the message buffers can be an interrupt source, if its corresponding IMASK bit is set. There is no distinction between Tx and Rx interrupts for a particular buffer, under the assumption that the buffer is initialized for either transmission or reception. Each of the buffers has an assigned flag bit in the IFLAG registers. The bit is set when the corresponding buffer completes a successful transfer and is cleared when the CPU writes one to it (unless another interrupt is generated at the same time). 

~~<mark>NOTE</mark>~~ 

It must be guaranteed that the CPU clears only the bit causing the current interrupt. For this reason, bit manipulation instructions (BSET) must not be used to clear interrupt flags. These instructions may cause accidental clearing of interrupt flags which are set after entering the current interrupt service routine. 

If the Legacy Rx FIFO is enabled (MCR[RFEN] = 1) and DMA is disabled (MCR[DMA] = 0), the interrupts corresponding to MBs 0 to 7 have different meanings. Bit 7 of the IFLAG1 register becomes the "Legacy FIFO Overflow" flag; bit 6 becomes the "Legacy FIFO Warning" flag, bit 5 becomes the "Frames Available in Legacy FIFO" flag and bits 4-0 are unused. See the description of Interrupt Flags 1 Register (IFLAG1) for more information. 

If both Legacy Rx FIFO and DMA are enabled (MCR[RFEN] and MCR[DMA] = 1) the FlexCAN does not generate any Legacy FIFO interrupt. Bit 5 of the IFLAG1 register still indicates "Frames Available in Legacy FIFO" and generates a DMA request. Bits 7, 6, 4-0 are unused. 

~~<mark>CAUTION</mark>~~ 

Legacy FIFO cannot be enabled when CAN FD feature is enabled. 

For a combined interrupt where multiple MB interrupt sources are OR'd together, the interrupt is generated when any of the associated MBs (or FIFO, if applicable) generates an interrupt. In this case, the CPU must read the IFLAG registers to determine which MB or FIFO source caused the interrupt. 

The following interrupt sources generate interrupts like the MB interrupt sources, and can be read from ESR1 register 

- Bus Off 

- Bus Off Done 

- Error 

- Error Fast 

- Tx Warning 

- Rx Warning 

The Bus Off, Error, Tx Warning, and Rx Warning interrupt mask bits are located in the CTRL1 register. 

### 72.3.14 Bus interface 

CPU access to FlexCAN registers is subject to the following rules: 

- Unrestricted read and write access to supervisor registers (registers identified with S/U in Table 459 in Supervisor Mode or with S only) results in an access error. 

- Read and write access to implemented reserved address space results in an access error. 

- Write access to positions whose bits are all currently read-only results in an access error. If at least one of the bits is not read-only then no access error is issued. Write permission to positions or some of their bits can change depending on the mode of operation or transitory state. See register and field descriptions for details. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2764 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

- Read and write access to unimplemented address space results in access error. 

- Read and write access to RAM located positions during Low Power mode results in an access error. 

- It is possible for the RXIMR memory region to be considered as general purpose memory and available for access. There are two ways of doing this: 

   1. If MCR[IRMQ] is cleared, the individual masks (RXIMR) are disabled. In this case the RXIMR memory region is considered as general purpose memory. 

   2. If MCR[MAXMB] is programmed with a value smaller than the available number of MBs, then the unused memory space can be used as general purpose RAM space. Note that reserved words within RAM cannot be used. As an example, suppose FlexCAN's RAM can support up to 16 MBs, CTRL2[RFFN] is 0h, and MCR[MAXMB] is programmed with zero. The maximum number of MBs in this case becomes one. The RAM starts at 0080h, and the space 0080h–008Fh is used by the one MB. The memory space 0090h–017Fh is available. The space 0180h– 087Fh is reserved. The space 0880h–0883h is used by the one individual mask and the available memory in the mask registers space would be 0884h–08BFh. From 08C0h–09DFh there are reserved words for internal use which cannot be used as general purpose RAM. As a general rule, free memory space for general purpose depends only on MAXMB. 

   3. If MCR[FDEN] is enabled, general purpose memory can be used out of Freeze mode only. 

##### Table 457. Access permissions 

|Supervisor access||0||||1||
|---|---|---|---|---|---|---|---|
|Supervisor mode - MCR[SUPV]<br>= 1||0||1||any||
|Modes of operation|Normal|Freeze|Low power|*|Normal|Freeze|Low power|
|MCR|bus error|bus error|bus error|bus error|read/write|read/write|read/write|
|CTRL1|read/write|read write|read/write|bus error|read/write|read/write|read/write|
|TIMER|read/write|read/write|read/write|bus error|read/write|read/write|read/write|
|TCR|bus error|bus error|bus error|bus error|bus error|bus error|bus error|
|RXMGMASK<sup>1</sup>|bus error for<br>write<br>operation|read/write|bus error<br>for write<br>operation|bus error|bus error<br>for write<br>operation|read/write|bus error<br>for write<br>operation|
|RX14MASK<sup>1</sup>|bus error for<br>write<br>operation|read/write|bus error<br>for write<br>operation|bus error|bus error<br>for write<br>operation|read/write|bus error<br>for write<br>operation|
|RX15MASK<sup>1</sup>|bus error for<br>write<br>operation|read/write|bus error<br>for write<br>operation|bus error|bus error<br>for write<br>operation|read/write|bus error<br>for write<br>operation|
|ECR|bus error for<br>write<br>operation|read/write|bus error for<br>write<br>operation|bus error|bus error<br>for write<br>operation|read/write|bus error<br>for write<br>operation|
|ESR1|read/write|read/write|read/write|bus error|read/write|read/write|read/write|
|IMASK2|read/write|read/write|read/write|bus error|read/write|read/write|read/write|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2765 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table 457. Access permissions (continued) 

|Supervisor access<br>Supervisor mode - MCR[SUPV]<br>= 1||0<br>0||1||1<br>any||
|---|---|---|---|---|---|---|---|
|Modes of operation|Normal|Freeze|Low power|*|Normal|Freeze|Low power|
|IMASK1|read/write|read/write|read/write|bus error|read/write|read/write|read/write|
|IFLAG2|read/write|read/write|read/write|bus error|read/write|read/write|read/write|
|IFLAG1|read/write|read/write|read/write|bus error|read/write|read/write|read/write|
|CTRL2|read/write|read/write|read/write|bus error|read/write|read/write|read/write|
|ESR2|read/write|read/write|read/write|bus error|read/write|read/write|read/write|
|CRCR|bus error for<br>write<br>operation|bus error<br>for write<br>operation|bus error for<br>write<br>operation|bus error|bus error<br>for write<br>operation|bus error<br>for write<br>operation|bus error<br>for write<br>operation|
|RXFGMASK<sup>1</sup>|bus error for<br>write<br>operation|read/write|bus error<br>for write<br>operation|bus error|bus error<br>for write<br>operation|read/write|bus error<br>for write<br>operation|
|RXFIR<sup>1</sup>|bus error for<br>write<br>operation|bus error<br>for write<br>operation|bus error<br>for write<br>operation|bus error|bus error<br>for write<br>operation|bus error<br>for write<br>operation|bus error<br>for write<br>operation|
|CBT|bus error for<br>write<br>operation|read/write|bus error<br>for write<br>operation|bus error|bus error<br>for write<br>operation|read/write|bus error<br>for write<br>operation|
|DBG1|bus error for<br>write<br>operation|bus error<br>for write<br>operation|bus error<br>for write<br>operation|bus error<br>for write<br>operation|bus error<br>for write<br>operation|bus error<br>for write<br>operation|bus error<br>for write<br>operation|
|DBG2|bus error for<br>write<br>operation|bus error<br>for write<br>operation|bus error<br>for write<br>operation|bus error<br>for write<br>operation|bus error<br>for write<br>operation|bus error<br>for write<br>operation|bus error<br>for write<br>operation|
|IMASK3|read/write|read/write|read/write|bus error|read/write|read/write|read/write|
|IFLAG3|read/write|read/write|read/write|bus error|read/write|read/write|read/write|
|MB<sup>1</sup> <sup>2</sup>|read/write|read/write|read/write|bus error|read/write|read/write|read/write|
|Legacy FIFO header<sup>1</sup>|read/write|read/write|read/write|bus error|read/write|read/write|read/write|
|Legacy FIFO reserved space<sup>1</sup>|bus error|bus error|bus error|bus error|bus error|bus error|bus error|
|Legacy FIFO filters<sup>1</sup>|read/write|read/write|read/write|bus error|read/write|read/write|read/write|
|RXIMR<sup>1</sup>|bus error|read/write|bus error|bus error|bus error|read/write|bus error|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2766 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table 457. Access permissions (continued) 

|Supervisor access<br>Supervisor mode - MCR[SUPV]<br>= 1||0<br>0||1||1<br>any||
|---|---|---|---|---|---|---|---|
|Modes of operation|Normal|Freeze|Low power|*|Normal|Freeze|Low power|
|MECR|read/write|read/write|read/write|bus error|read/write|read/write|read/write|
|ERRIAR|read/write|read/write|read/write|bus error|read/write|read/write|read/write|
|ERRIDPR|read/write|read/write|read/write|bus error|read/write|read/write|read/write|
|ERRIPPR|read/write|read/write|read/write|bus error|read/write|read/write|read/write|
|RERRAR<sup>3</sup>|read/write|read/write|read/write|bus error|read/write|read/write|read/write|
|RERRDR<sup>3</sup>|read/write|read/write|read/write|bus error|read/write|read/write|read/write|
|RERRSYNR<sup>3</sup>|read/write|read/write|read/write|bus error|read/write|read/write|read/write|
|ERRSR|read/write|read/write|read/write|bus error|read/write|read/write|read/write|
|FDCTRL|read/write|read/write|read/write|bus error|read/write|read/write|read/write|
|FDCBT|read/write<sup>3</sup>|read/write|read/write<sup>3</sup>|bus error|read/write<sup>3</sup>|read/write|read/write<sup>3</sup>|
|FDCRC|bus error for<br>write<br>operation|bus error<br>for write<br>operation|bus error<br>for write<br>operation|bus error|bus error<br>for write<br>operation|bus error<br>for write<br>operation|bus error<br>for write<br>operation|
|ERFCR|read/write<sup>3</sup>|read/write|read/write<sup>3</sup>|bus error|read/write<sup>3</sup>|read/write|read/write<sup>3</sup>|
|ERFIER|read/write|read/write|read/write|bus error|read/write|read/write|read/write|
|ERFSR|read/write|read/write|read/write|bus error|read/write|read/write|read/write|
|HR_TIME_STAMP|read/write|read/write|read/write|bus error|read/write|read/write|read/write|
|Enhanced Rx FIFO header<sup>4</sup>|bus error for<br>write<br>operation|bus error<br>for write<br>operation|bus error<br>for write<br>operation|bus error|bus error<br>for write<br>operation|bus error<br>for write<br>operation|bus error<br>for write<br>operation|
|Enhanced Rx FIFO reserved<br>space<sup>4</sup>|bus error|bus error|bus error|bus error|bus error|bus error|bus error|
|ERFFEL|bus error for<br>write<br>operation|read/write|bus error<br>for write<br>operation|bus error|bus error<br>for write<br>operation|read/write|bus error<br>for write<br>operation|
|General purpose RAM<sup>1</sup>|read/write|read/write|read/write|bus error|read/write|read/write|read/write|
|Reserved space (used)<sup>1</sup>|bus error|bus error|bus error|bus error|bus error|bus error|bus error|
|Reserved space (empty)<sup>1</sup>|bus error|bus error|bus error|bus error|bus error|bus error|bus error|



1. Access in low power is only possible if RAM_clk and ipg_clk are enabled. 

2. If MCR[RFEN] = 1, see Legacy FIFO access rules below. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2767 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

3. Write operation has no effect. 

4. Enhanced Rx FIFO must not be accessed if MCR[RFEN] is set. 

### 72.3.15 Detection and correction of memory errors 

~~<mark>NOTE</mark>~~ 

All FlexCAN memory must be initialized before starting its operation in order to have the parity bits in memory properly updated. CTRL2[WRMFRZ] grants write access to all memory positions that require initialization, ranging from 080h–ADFh and from C20h–31FFh. The RXMGMASK, RX14MASK, RX15MASK, and RXFGMASK registers need to be initialized as well. MCR[RFEN] and ERF[ERFEN] must not be set during memory initialization. 

FlexCAN supports detection and correction of errors in memory read accesses. Each byte of FlexCAN memory is associated to five parity bits that ensure a Hamming distance of four. The error correction mechanism ensures that in this 13-bit word, errors in one bit can be corrected (correctable errors) and errors in two bits can be detected but not corrected (non-correctable errors). Errors in more than two bits may not be detected. In case of non-correctable errors, the corrupted data is not changed by the error correction logic. When a read access is performed, the parity bits are used to calculate a syndrome, which indicates the error in each byte. 

FlexCAN detects a noncorrectable error in the event either an all-zeros or an all-ones read occurs. See description of Error Report Syndrome Register (RERRSYNR). 

Memory errors are indicated to the host through status register (Error Status Register (ERRSR)) and bus transfer errors, and reported through report registers (Error Report Address register (RERRAR), Error Report Data register (RERRDR) and Error Report Syndrome register (RERRSYNR)). 

The error detection and correction mechanism can be activated or not, controlled by MECR[ECCDIS]. When disabled, updates on indications and reporting registers are stopped, but the parity bits are still calculated and written along with data in memory write operations to ensure that memory has consistent parity bits associated with the data. 

To avoid accidentally changing the critical error correction configuration, this protocol must be followed to enable the update of the Memory Error Control register (MECR): 

1. By default, CTRL2[ECRWRE] is zero and MECR[ECRWRDIS] is one. 

2. Set CTRL2[ECRWRE]. 

3. Clear MECR[ECRWRDIS]. 

4. All writes to Memory Error Control register (MECR) must keep MECR[ECRWRDIS] cleared. 

5. After configuration is done, lock the Memory Error Control register (MECR) by either setting MECR[ECRWRDIS] or clearing CTRL2[ECRWRE]. 

#### 72.3.15.1 Sources of the memory access 

The FlexCAN memory can be accessed by two major sources (or requestors): 

- Host (CPU): the largest word accessed is 32-bit. 

- FlexCAN internal processes (Rx matching, Tx arbitration, move-in on reception, move-out on transmission): the largest word accessed is 64-bit. 

The way that noncorrectable errors are indicated and reported depends on the source of access. 

#### 72.3.15.2 Error indication 

Memory errors are indicated by flags HANCEIF, FANCEIF, and CEIF in the Error Status Register (ERRSR). Noncorrectable errors detected in memory reads requested by the host are indicated separately than the ones detected in requests by FlexCAN internal processes. FlexCAN makes no distinction of the source of the access when correctable errors are detected. There are three independent flags for these three cases, and each flag will raise an interrupt unless it is masked by mask bits in Memory Error Control Register (MECR). If both noncorrectable and correctable errors are found in different bytes in the same read operation, both flags are set. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2768 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

A noncorrectable error detected in host access is also indicated as a bus transfer error. A bus wait request may be asserted to extend the memory transaction to the moment the report registers are updated. This indication cannot be masked. If the flag bit ERRSR[HANCEIF] is not masked, the same noncorrectable error will raise a bus transfer error and an interrupt request. 

Each indication flag has one overrun flag in Error Status Register (ERRSR). The overrun flags do not request interrupts. Overrun flags for noncorrectable errors indicate that other errors of the same nature were detected after current error being treated; overrun flags for correctable errors indicate that other errors of the same nature were detected before the current error being treated. 

This is the recommended handling sequence for error indication: 

1. Get error report information from report registers. 

2. Use this information to take proper measures in the application. 

3. Clear the HANCEIF, FANCEIF, and CEIF flags. 

4. If the overrun flag is active: 

   - a. Alert application that at least one error could not be managed. 

   - b. Clear the overrun flag. 

The FlexCAN internal processes can access memory in transactions larger than 32 bits. For the indication, this kind of access is considered a consecutive sequence of 32-bit accesses. If errors are found in two or more 32-bit words the interrupt and overrun flags are set simultaneously. 

#### 72.3.15.3 Error reporting 

The report registers Error Report Address register (RERRAR), Error Report Data register (RERRDR), and Error Report Syndrome register (RERRSYNR) provide detailed information about the address read, raw data, and syndrome read with error, and are indicated by the flags described in Error indication. The address, data, and syndrome registers are updated simultaneously along with the error flags, according to these rules: 

1. If either of the two non-correctable error flags is currently set, the report registers are not updated (the previous non-correctable error reporting is preserved). 

2. Otherwise (either no error flag is currently set or only the correctable error flag is currently set), the report registers are updated according to the new error; or according to the most severe of new errors if non-correctable and correctable errors are simultaneously detected. 

Reporting of errors detected in accesses larger than 32-bit follows the rules described in Error indication and in the description of Error Report Address Register (RERRAR). 

The address reported in RERRAR and defined in ERRIAR are not the same listed in the module memory map. The relation between the reported addresses and the respective ones in the module memory map is shown in the description of Error Injection Address Register (ERRIAR). 

Addresses reported when reading memory portions organized as FIFOs, such as the Legacy Rx FIFO Structure, Enhanced RX FIFO Structure and the Rx FIFO Information Register (RXFIR), refer to the address of the specific entry accessed in the FIFO, not to the FIFO base address. 

To assure coherence of the error report registers it is necessary to turn off the report update by setting MECR[RERRDIS] before reading the report registers. 

#### 72.3.15.4 Response to errors 

Correctable errors have no consequence on FlexCAN operation because affected data is corrected before its use by the host or FlexCAN internal processes. 

For host-initiated reads, a noncorrectable error may affect the host, but does not affect FlexCAN operation. 

Non-correctable errors detected on memory reads requested by the FlexCAN internal processes may result in incorrect operation depending on the state of MECR[NCEFAFRZ], as follows: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2769 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

- During reception (either matching or move-in processes), when a noncorrectable error occurs, an incorrect destination may be selected to store the incoming frame, a corrupted frame may be stored in the correct destination, or both. If MECR[NCEFAFRZ] is set, FlexCAN stops operation automatically and enters in Freeze mode to prevent corrupted data from being treated as valid by FlexCAN internal processes. When MECR[NCEFAFRZ] is negated, FlexCAN continues working and a corrupted frame is received. 

- During arbitration process, when a noncorrectable error occurs, either a non-highest priority Tx message buffer may be mistakenly selected for transmission or its data may be corrupted. If MECR[NCEFAFRZ] is set, FlexCAN stops operation automatically and enters Freeze mode before starting the move-out. When MECR[NCEFAFRZ] is negated, FlexCAN proceeds to move-out with a corrupted frame that will be transmitted on the CAN bus. 

- During move-out process, when a noncorrectable error occurs, a corrupted frame is copied from the selected Tx MB that won the arbitration to the Tx SMB for transmission. If MECR[NCEFAFRZ] is set, FlexCAN stops operation automatically and enters Freeze mode before starting the transmission. When MECR[NCEFAFRZ] is negated, the corrupted frame is transferred from the Tx SMB to the Protocol Engine (PE) sub-block and is transmitted on the CAN bus. 

- A noncorrectable error can also be detected beyond the move-out process, when Tx data is read from Tx SMB (buffer located in RAM) to be transferred to the PE subblock for transmission. In this case, a frame with corrupted ID and/or data is transmitted on the CAN bus. 

To prevent the frame from being successfully received by the external nodes, FlexCAN inverts all bits in the CRC field (CRC sequence plus CRC delimiter), and transmits an error flag just after CRC delimiter as a result of self-detecting a Bit1 error and a form error due to the CRC field inversion. When MECR[NCEFAFRZ] is set, FlexCAN stops operation automatically and enters Freeze mode just after the error frame. When MECR[NCEFAFRZ] is negated, FlexCAN may attempt to re-transmit the same frame, as long as no other higher priority Tx MB is subsequently configured for transmission. 

In the event the noncorrectable error persists, FlexCAN eventually reaches the Bus Off state because of consecutive error detections. ECR[TXERRCNT] is updated every time FlexCAN inverts the CRC field, causing errors as described above. 

When MECR[NCEFAFRZ] is set and FlexCAN enters Freeze mode, only the CPU can cause FlexCAN to exit Freeze mode and resume Normal mode. The assertion of MECR[NCEFAFRZ] is the only way to prevent corrupted frames from being transmitted on the CAN bus up to the move-out internal process. 

The error report registers can provide information to the application for customized management of these situations. 

#### 72.3.15.5 Error injection 

The error injection registers ERRIAR, ERRIDPR, and ERRIPPR are used to inject errors in memory reads in order to force errors and consequently update the indication and reporting registers. The relation between the error injection addresses and the respective ones in the module memory map is shown in the description of Error Injection Address Register (ERRIAR). 

The injection is done by flipping the data and parity bits correspondent to the bits in 1 in ERRIDPR and ERRIPPR. Injection can be selected specifically for memory accesses requested by the host or by FlexCAN internal processes. 

In case of accesses larger than 32-bits, the EXTERRIE bit in Memory Error Control register (MECR) extends the injection pattern, replicating it in 32-bit words to fill the width of the access. 

~~<mark>NOTE</mark>~~ 

It is very unlikely, but error injection may correct a bit with error. This will not raise the error flags and reports as expected. 

To ensure coherence among error injection registers and avoid spurious error injections, MECR[HAERRIE] and MECR[FAERRIE] must be cleared when configuring the memory injection registers. 

## 72.4 FlexCAN signal descriptions 

The FlexCAN module has two I/O signals connected to the external chip pins. These signals are summarized in the following table and described in more detail in the next subsections. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2770 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table 458. FlexCAN signal descriptions 

|Signal||Description|I/O|
|---|---|---|---|
|CAN Rx|CAN receive pin||Input|
|CAN Tx|CAN transmit pin||Output|



### 72.4.1 CAN Rx 

This pin is the receive pin from the CAN bus transceiver. Dominant state is represented by logic level 0. Recessive state is represented by logic level 1. 

### 72.4.2 CAN Tx 

This pin is the transmit pin to the CAN bus transceiver. Dominant state is represented by logic level 0. Recessive state is represented by logic level 1. 

## 72.5 Initialization/application information 

This section provides instructions for initializing the FlexCAN module. 

### 72.5.1 FlexCAN initialization sequence 

For any configuration change/initialization it is required that FlexCAN be put into Freeze mode (see Freeze mode). Note that the module needs to be initialized after every reset. 

The following is a generic initialization sequence applicable to the FlexCAN module: 

1. Initialize the Module Configuration register (MCR). 

   - a. Enable the individual filtering per MB and reception queue features by setting IRMQ. 

   - b. Enable the warning interrupts by setting WRNEN. 

   - c. If required, disable frame self reception by setting SRXDIS. 

   - d. Enable the Legacy Rx FIFO by setting RFEN or the Enhanced Rx FIFO by setting ERFEN. 

   - e. If Legacy Rx FIFO or Enhanced Rx FIFO is enabled and DMA is required, set DMA. 

   - f. Enable the abort mechanism by setting AEN. 

   - g. Enable the local priority feature by setting LPRIOEN. 

2. Initialize the Control 1 register (CTRL1) and optionally the CAN Bit Timing register (CBT). Initialize also the CAN FD CAN Bit Timing register (FDCBT). 

   - a. Determine the bit timing parameters: PROPSEG, PSEG1, PSEG2, and RJW. 

   - b. Optionally determine the bit timing parameters: EPROPSEG, EPSEG1, EPSEG2, and ERJW. 

   - c. Determine the CAN FD bit timing parameters: FPROPSEG, FPSEG1, FPSEG2, and FRJW. 

   - d. Determine the bit rate by programming the PRESDIV field and optionally the EPRESDIV field. 

   - e. Determine the CAN FD bit rate by programming the FPRESDIV field. 

   - f. Determine the internal arbitration mode (LBUF). 

3. All FlexCAN memory must be initialized if Error Code Correction (ECC) is enabled. See Detection and correction of memory errors. 

4. Initialize the message buffers. 

   - a. The control and status word of all message buffers must be initialized. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2771 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

   - b. If Rx FIFO was enabled, the ID filter table must be initialized. 

   - c. Other entries in each message buffer should be initialized as required. 

5. Initialize the Rx Individual Mask registers (RXIMRn). 

6. Set required interrupt mask bits in 

   - IMASK registers (for all MB interrupts) 

   - CTRL1 / CTRL2 registers (for Bus Off and Error interrupts) 

7. Negate MCR[HALT]. 

After the last step listed above, FlexCAN attempts to synchronize to the CAN bus. 

## 72.6 Memory map/register definition 

This section describes the registers and data structures in the FlexCAN module. The base address of the module depends on the particular memory map of the chip. 

### 72.6.1 FlexCAN memory mapping 

The address space occupied by FlexCAN has 128 bytes for registers starting at the module base address, followed by embedded RAM starting at address offset 0080h. 

Each individual register is identified by its complete name and the corresponding mnemonic . The access type can be Supervisor (S) or Unrestricted (U). Most of the registers can be configured to have either Supervisor or Unrestricted access by programming MCR[SUPV]. These registers are identified as S/U in the Access column of Table 459. 

~~<mark>NOTE</mark>~~ 

An invalid register access will result in a bus error. This includes reading a write-only register, writing a read-only register, or accessing an invalid address. 

Table 459. Register access and reset information 

|Register|Access type|Affected by<br>hard reset|Affected by<br>soft reset|
|---|---|---|---|
|Module Configuration Register (MCR)|S|Yes|Yes|
|Control 1 Register (CTRL1)|S/U|Yes|No|
|Free Running Timer Register (TIMER)|S/U|Yes|Yes|
|Rx Mailboxes Global Mask Register (RXMGMASK)|S/U|No|No|
|Rx Buffer 14 Mask Register (RX14MASK)|S/U|No|No|
|Rx Buffer 15 Mask Register (RX15MASK)|S/U|No|No|
|Error Counter Register (ECR)|S/U|Yes|Yes|
|Error and Status 1 Register (ESR1)|S/U|Yes|Yes|
|Interrupt Masks 2 Register (IMASK2)|S/U|Yes|Yes|
|Interrupt Masks 1 Register (IMASK1)|S/U|Yes|Yes|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2772 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table 459. Register access and reset information (continued) 

|Register|Access type|Affected by<br>hard reset|Affected by<br>soft reset|
|---|---|---|---|
|Interrupt Flags 2 Register (IFLAG2)|S/U|Yes|Yes|
|Interrupt Flags 1 Register (IFLAG1)|S/U|Yes|Yes|
|Control 2 Register (CTRL2)|S/U|Yes|No|
|Error and Status 2 Register (ESR2)|S/U|Yes|Yes|
|CRC Register (CRCR)|S/U|Yes|Yes|
|Rx FIFO Global Mask Register (RXFGMASK)|S/U|No|No|
|Rx FIFO Information Register (RXFIR)|S/U|No|No|
|CAN Bit Timing Register (CBT)|S/U|Yes|No|
|Interrupt Masks 3 Register (IMASK3)|S/U|Yes|Yes|
|Interrupt Flags 3 Register (IFLAG3)|S/U|Yes|Yes|
|Message buffers|S/U|No|No|
|Rx Individual Mask Registers|S/U|No|No|
|Memory Error Control Register (MECR)|S/U|Yes|Yes|
|Error Injection Address Register (ERRIAR)|S/U|Yes|Yes|
|Error Injection Data Pattern Register (ERRIDPR)|S/U|Yes|Yes|
|Error Injection Parity Pattern Register (ERRIPPR)|S/U|Yes|Yes|
|Error Report Address Register (RERRAR)|S/U|Yes|Yes|
|Error Report Data Register (RERRDR)|S/U|Yes|Yes|
|Error Report Syndrome Register (RERRSYNR)|S/U|Yes|Yes|
|Error Status Register (ERRSR)|S/U|Yes|Yes|
|Enhanced CAN Bit Timing Prescalers (EPRS)|S/U|Yes|No|
|Enhanced Nominal CAN Bit Timing (ENCBT)|S/U|Yes|No|
|Enhanced Data Phase CAN bit Timing (EDCBT)|S/U|Yes|No|
|Enhanced Transceiver Delay Compensation (ETDC)|S/U|Yes|No|
|CAN FD Control Register (FDCTRL)|S/U|Yes|No|
|CAN FD Bit Timing Register (FDCBT)|S/U|Yes|No|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2773 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table 459. Register access and reset information (continued) 

|Register|Access type|Affected by<br>hard reset|Affected by<br>soft reset|
|---|---|---|---|
|CAN FD CRC Register (FDCRC)|S/U|Yes|Yes|
|Enhanced Rx FIFO Control Register (ERFCR)|S/U|Yes|Yes|
|Enhanced Rx FIFO Interrupt Enable Register (ERFIER)|S/U|Yes|Yes|
|Enhanced Rx FIFO Status Register (ERFSR)|S/U|Yes|Yes|
|High Resolution Time Stamp (HR_TIME_STAMP)|S/U|No|No|
|Enhanced Rx FIFO|S/U|No|No|
|Enhanced Rx FIFO Filter Element (ERFFEL)|S/U|No|No|



The FlexCAN module can store CAN messages for transmission and reception using mailboxes and Rx FIFO structures. 

### 72.6.2 CAN register descriptions 

The table below shows the FlexCAN memory map. 

The address range from offset 80h–67Fh allocates the ninety-six 128-bit message buffers (MBs). 

The memory maps for the message buffers are in FlexCAN message buffer memory map. 

The address range from offset 2000h–204Ch allocates the Enhanced Rx FIFO output, and the address range from offset 2050h–263Ch allocates the rest of Enhanced RX FIFO 19 elements. 

The memory map for the Enhanced Rx FIFO is in Enhanced Rx FIFO structure. 

#### 72.6.2.1 CAN memory map 

CAN_0 base address: 4030_4000h CAN_1 base address: 4030_8000h CAN_2 base address: 4030_C000h CAN_3 base address: 4031_0000h CAN_4 base address: 4031_4000h CAN_5 base address: 4031_8000h CAN_6 base address: 4031_C000h CAN_7 base address: 4032_0000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|Module Configuration Register (MCR)|32|RW|D890_000Fh|
|4h|Control 1 Register (CTRL1)|32|RW|0000_0000h|
|8h|Free Running Timer (TIMER)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2774 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|10h|Rx Mailboxes Global Mask Register (RXMGMASK)|32|RW|See<br>description|
|14h|Rx 14 Mask Register (RX14MASK)|32|RW|See<br>description|
|18h|Rx 15 Mask Register (RX15MASK)|32|RW|See<br>description|
|1Ch|Error Counter (ECR)|32|RW|0000_0000h|
|20h|Error and Status 1 Register (ESR1)|32|R2C|0000_0000h|
|24h|Interrupt Masks 2 Register (IMASK2)|32|RW|0000_0000h|
|28h|Interrupt Masks 1 Register (IMASK1)|32|RW|0000_0000h|
|2Ch|Interrupt Flags 2 Register (IFLAG2)|32|W1C|0000_0000h|
|30h|Interrupt Flags 1 Register (IFLAG1)|32|W1C|0000_0000h|
|34h|Control 2 Register (CTRL2)|32|RW|See<br>description|
|38h|Error and Status 2 Register (ESR2)|32|RO|0000_0000h|
|44h|CRC Register (CRCR)|32|RO|0000_0000h|
|48h|Legacy Rx FIFO Global Mask Register (RXFGMASK)|32|RW|See<br>description|
|4Ch|Legacy Rx FIFO Information Register (RXFIR)|32|RO|See<br>description|
|50h|CAN Bit Timing Register (CBT)|32|RW|0000_0000h|
|6Ch|Interrupt Masks 3 Register (IMASK3)|32|RW|0000_0000h|
|74h|Interrupt Flags 3 Register (IFLAG3)|32|W1C|0000_0000h|
|880h - 9FCh|Rx Individual Mask Registers (RXIMR0 - RXIMR95)|32|RW|See<br>description|
|AE0h|Memory Error Control Register (MECR)|32|RW|800C_0080h|
|AE4h|Error Injection Address Register (ERRIAR)|32|RW|0000_0000h|
|AE8h|Error Injection Data Pattern Register (ERRIDPR)|32|RW|0000_0000h|
|AECh|Error Injection Parity Pattern Register (ERRIPPR)|32|RW|0000_0000h|
|AF0h|Error Report Address Register (RERRAR)|32|RO|0000_0000h|
|AF4h|Error Report Data Register (RERRDR)|32|RO|0000_0000h|
|AF8h|Error Report Syndrome Register (RERRSYNR)|32|RO|0000_0000h|
|AFCh|Error Status Register (ERRSR)|32|W1C|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2775 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|BF0h|Enhanced CAN Bit Timing Prescalers (EPRS)|32|RW|0000_0000h|
|BF4h|Enhanced Nominal CAN Bit Timing (ENCBT)|32|RW|0000_0000h|
|BF8h|Enhanced Data Phase CAN bit Timing (EDCBT)|32|RW|0000_0000h|
|BFCh|Enhanced Transceiver Delay Compensation (ETDC)|32|RW|0000_0000h|
|C00h|CAN FD Control Register (FDCTRL)|32|RW|8000_0100h|
|C04h|CAN FD Bit Timing Register (FDCBT)|32|RW|0000_0000h|
|C08h|CAN FD CRC Register (FDCRC)|32|RO|0000_0000h|
|C0Ch|Enhanced Rx FIFO Control Register (ERFCR)|32|RW|0000_0000h|
|C10h|Enhanced Rx FIFO Interrupt Enable Register (ERFIER)|32|RW|0000_0000h|
|C14h|Enhanced Rx FIFO Status Register (ERFSR)|32|WORZ|0000_0000h|
|C30h - DACh|High Resolution Time Stamp (HR_TIME_STAMP0 -<br>HR_TIME_STAMP95)|32|RW|See<br>description|
|3000h -<br>31FCh|Enhanced Rx FIFO Filter Element (ERFFEL0 - ERFFEL127)|32|RW|See<br>description|



#### 72.6.2.2 Module Configuration Register (MCR) 

##### Offset 

|Register|Offset|
|---|---|
|MCR|0h|



##### Function 

This register defines global system configurations, such as the module operation modes and the maximum message buffer configuration. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2776 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2777-02.png)


<!-- Start of picture text -->
Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>NOTR FRZA LPMA<br>R<br>MDIS  FRZ  RFEN  HALT  DY  Reserv SOFT CK  SUPV  Reserv WRNE CK  Reserv Reserv SRXDI IRMQ<br>ed  RST  ed  N  ed  ed  S<br>W<br>Reset 1 1 0 1 1 0 0 0 1 0 0 1 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 LPRIO 0 0<br>DMA  AEN  FDEN  IDAM  MAXMB<br>EN<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Module Disable|
|MDIS|This bit controls whether FlexCAN is enabled or not. When disabled, FlexCAN disables the clocks to the<br>CAN Protocol Engine and Controller Host Interface submodules. This bit is not affected by soft reset.<br>0b - Enable the FlexCAN module.<br>1b - Disable the FlexCAN module.|
|30<br>FRZ|Freeze Enable<br>The FRZ bit specifies the FlexCAN behavior when MCR[HALT] is set or when Debug mode is requested<br>at chip level. When FRZ is asserted, FlexCAN is enabled to enter Freeze mode. Negation of this bit field<br>causes FlexCAN to exit from Freeze mode. This bit is set by hardware when a non-correctable error is<br>detected (MECR[NCEFAFRZ] is asserted).<br>0b - Not enabled to enter Freeze mode.<br>1b - Enabled to enter Freeze mode.|
|29<br>RFEN|Legacy Rx FIFO Enable<br>This bit controls whether the Legacy Rx FIFO feature is enabled or not. When RFEN is set, MBs 0 to 5 cannot<br>be used for normal reception and transmission because the corresponding memory region (80h–DCh) is<br>used by the FIFO engine as well as additional MBs (up to 32, depending on CTRL2[RFFN] setting) which are<br>used as Legacy Rx FIFO ID filter table elements. RFEN also impacts the definition of the minimum number<br>of peripheral clocks per CAN bit as described inTable 454. This bit can be written in Freeze mode only,<br>because it is blocked by hardware in other modes.<br>This bit cannot be set when CAN FD operation is enabled (see FDEN bit).<br>~~NOTE~~<br>RFEN bit must not be set if ERFCR[ERFEN] is set.<br>~~NOTE~~|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2777 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table continued from the previous page... 

|Field|Function<br>T|he descriptions of the field settings vary by module instance.<br>~~NOTE~~|
|---|---|---|
||Instance|Field value and description|
||CAN_0|0b - Legacy Rx FIFO not enabled.<br>1b - Legacy Rx FIFO enabled.|
||CAN_1|0b - Legacy Rx FIFO not enabled.<br>1b - Legacy Rx FIFO enabled.|
||CAN_2|0b - Legacy Rx FIFO not enabled.<br>1b - Legacy Rx FIFO enabled.|
||CAN_3|0b - Rx FIFO not enabled.<br>1b - Rx FIFO enabled.|
||CAN_4|0b - Rx FIFO not enabled.<br>1b - Rx FIFO enabled.|
||CAN_5|0b - Rx FIFO not enabled.<br>1b - Rx FIFO enabled.|
||CAN_6|0b - Rx FIFO not enabled.<br>1b - Rx FIFO enabled.|
||CAN_7|0b - Rx FIFO not enabled.<br>1b - Rx FIFO enabled.|
|28<br>HALT|Halt FlexCAN<br>Assertion of this bit puts th<br>the message buffers and t<br>performed by FlexCAN bef<br>in a low power mode. The<br>MECR[NCEFAFRZ] is ass<br>0b - No Freeze mod<br>1b - Enters Freeze|e FlexCAN module into Freeze mode. The CPU should clear it after initializing<br>he Control registers CTRL1 and CTRL2. No reception or transmission is<br>ore this bit is cleared. Freeze mode cannot be entered when FlexCAN is<br>HALT bit is set by hardware when a non-correctable error is detected and<br>erted.<br>e request.<br>mode if the FRZ bit is asserted.|
|27|FlexCAN Not Ready||
|NOTRDY|This read-only bit indicates<br>FlexCAN has exited these|that FlexCAN is either in Disable mode or Freeze mode. It is negated when<br>modes. This bit is not affected by soft reset.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2778 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - FlexCAN module is either in Normal mode, Listen-Only mode, or Loop-Back mode.<br>1b - FlexCAN module is either in Disable mode or Freeze mode.|
|26<br>—|Reserved<br>When writing to this field, always write the reset value.|
|25<br>SOFTRST|Soft Reset<br>When SOFTRST is asserted, FlexCAN resets its internal state machines and some of the memory-<br>mapped registers.<br>SOFTRST can be asserted directly by the CPU when it writes to the MCR register. Because soft reset<br>is synchronous and has to follow a request/acknowledge procedure across clock domains, it may take<br>some time to fully propagate its effect. The SOFTRST bit remains asserted when reset is pending, and is<br>automatically negated when reset completes. Therefore, software can poll this bit to know when the soft<br>reset has completed.<br>Soft reset cannot be applied when clocks are shut down in a low power mode. The module should be first<br>removed from low power mode, and then soft reset can be applied. This bit is not affected by soft reset.<br>0b - No reset request.<br>1b - Resets the registers affected by soft reset.|
|24|Freeze Mode Acknowledge|
|FRZACK|This read-only bit indicates that FlexCAN is in Freeze mode and its prescaler is stopped. The Freeze mode<br>request cannot be granted until current transmission or reception processes have finished. Therefore the<br>software can poll the FRZACK bit to know when FlexCAN has actually entered Freeze mode. If Freeze mode<br>request is negated, then this bit is negated after the FlexCAN prescaler is running again. If Freeze mode is<br>requested when FlexCAN is in a low power mode, then the FRZACK bit will be set only when the low-power<br>mode is exited. SeeFreeze mode. This bit is not affected by soft reset.<br>FRZACK will be asserted within 178 CAN bits from the Freeze mode request by the CPU,<br>and negated within 2 CAN bits after the Freeze mode request removal (seeProtocol timing).<br>~~NOTE~~|
||0b - FlexCAN not in Freeze mode, prescaler running.<br>1b - FlexCAN in Freeze mode, prescaler stopped.|
|23|Supervisor Mode|
|SUPV|This bit configures the FlexCAN to be either in Supervisor or User mode. The registers affected by this<br>bit are marked as S/U in the "Access type" column ofTable 459. Reset value of this bit is 1, so the<br>affected registers start with Supervisor access allowance only. This bit can be written only in Freeze<br>mode because it is blocked by hardware in other modes.<br>0b - FlexCAN is in User mode. Affected registers allow both Supervisor and Unrestricted<br>accesses.<br>1b - FlexCAN is in Supervisor mode. Affected registers allow only Supervisor access. Unrestricted<br>access behaves as though the access was done to an unimplemented register location.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2779 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|22<br>—|Reserved<br>When writing to this field, always write the reset value.|
|21<br>WRNEN|Warning Interrupt Enable<br>When asserted, this bit enables the generation of the TWRNINT and RWRNINT flags in the Error and<br>Status Register 1 (ESR1). If WRNEN is negated, the TWRNINT and RWRNINT flags will always be zero,<br>independent of the values of the error counters, and no warning interrupt will ever be generated. This bit<br>can be written in Freeze mode only, because it is blocked by hardware in other modes.<br>0b - TWRNINT and RWRNINT bits are zero, independent of the values in the error counters.<br>1b - TWRNINT and RWRNINT bits are set when the respective error counter transitions from less<br>than 96 to greater than or equal to 96.|
|20<br>LPMACK|Low-Power Mode Acknowledge<br>This read-only bit indicates that FlexCAN is in a low-power mode (Disable mode). A low-power mode cannot<br>be entered until all current transmission or reception processes have finished, so the CPU can poll the<br>LPMACK bit to know when FlexCAN has actually entered low power mode. This bit is not affected by<br>soft reset.<br>LPMACK will be asserted within 180 CAN bits from the low-power mode request by the<br>CPU, and negated within 2 CAN bits after the low-power mode request removal (see<br>Protocol timing).<br>~~NOTE~~<br>0b - FlexCAN is not in a low-power mode.<br>1b - FlexCAN is in a low-power mode.|
|19<br>—|Reserved<br>When writing to this field, always write the reset value.|
|18<br>—|Reserved<br>When writing to this field, always write the reset value.|
|17<br>SRXDIS|Self Reception Disable<br>This bit defines whether FlexCAN is allowed to receive frames transmitted by itself. If this bit is asserted,<br>frames transmitted by the module will not be stored in any MB, regardless if the MB is programmed with<br>an ID that matches the transmitted frame, and no interrupt flag or interrupt signal will be generated due<br>to the frame reception. This bit can be written only in Freeze mode because it is blocked by hardware in<br>other modes.<br>0b - Self-reception enabled.<br>1b - Self-reception disabled.|
|16<br>IRMQ|Individual Rx Masking And Queue Enable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2780 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field|Function<br>This bit indicates whether Rx matching process will be based either on individual masking and queue<br>or on masking scheme with RXMGMASK, RX14MASK, RX15MASK, and RXFGMASK. This bit can be<br>written in Freeze mode only because it is blocked by hardware in other modes.<br>0b - Individual Rx masking and queue feature are disabled. For backward compatibility with<br>legacy applications, the reading of C/S word locks the MB even if it is EMPTY.<br>1b - Individual Rx masking and queue feature are enabled.|
|---|---|
|15<br>DMA|DMA Enable<br>DMA controls whether the DMA feature is enabled or not. The DMA feature can only be used in Legacy Rx<br>FIFO or Enhanced Rx FIFO, so consequently MCR[RFEN] or ERFCR[ERFEN] must be asserted. When<br>DMA and RFEN are set, IFLAG1[BUF5I] generates the DMA request and no RX FIFO interrupt is generated.<br>This bit can be written in Freeze mode only as it is blocked by hardware in other modes.<br>The descriptions of the field settings vary by module instance.<br>~~NOTE~~|
||Instance<br>Field value and description|
||CAN_0<br>0b - DMA feature for Legacy RX FIFO or Enhanced Rx FIFO disabled.<br>1b - DMA feature for Legacy RX FIFO or Enhanced Rx FIFO enabled.|
||CAN_1<br>0b - DMA feature for Legacy RX FIFO or Enhanced Rx FIFO disabled.<br>1b - DMA feature for Legacy RX FIFO or Enhanced Rx FIFO enabled.|
||CAN_2<br>0b - DMA feature for Legacy RX FIFO or Enhanced Rx FIFO disabled.<br>1b - DMA feature for Legacy RX FIFO or Enhanced Rx FIFO enabled.|
||CAN_3<br>0b - DMA feature for RX FIFO disabled.<br>1b - DMA feature for RX FIFO enabled.|
||CAN_4<br>0b - DMA feature for RX FIFO disabled.<br>1b - DMA feature for RX FIFO enabled.|
||CAN_5<br>0b - DMA feature for RX FIFO disabled.<br>1b - DMA feature for RX FIFO enabled.|
||CAN_6<br>0b - DMA feature for RX FIFO disabled.<br>1b - DMA feature for RX FIFO enabled.|
||CAN_7<br>0b - DMA feature for RX FIFO disabled.<br>1b - DMA feature for RX FIFO enabled.|
|14|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2781 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—<br>13<br>LPRIOEN|Local Priority Enable<br>This bit is provided for backwards compatibility with legacy applications. It controls whether the local<br>priority feature is enabled or not. It is used to expand the ID used during the arbitration process. With<br>this expanded ID concept, the arbitration process is done based on the full 32-bit word, but the actual<br>transmitted ID still has 11-bit for standard frames and 29-bit for extended frames. This bit can be written<br>only in Freeze mode because it is blocked by hardware in other modes.<br>0b - Local Priority disabled.<br>1b - Local Priority enabled.|
|12<br>AEN|Abort Enable<br>When asserted, this bit enables the Tx abort mechanism. This mechanism guarantees a safe procedure for<br>aborting a pending transmission, so that no frame is sent in the CAN bus without notification. This bit can<br>be written only in Freeze mode because it is blocked by hardware in other modes.<br>When MCR[AEN] is asserted, only the abort mechanism (seeTransmission abort<br>mechanism) must be used for updating mailboxes configured for transmission.<br>~~NOTE~~|
||Writing the Abort code into Rx mailboxes can cause unpredictable results when MCR[AEN]<br>is asserted.<br>~~CAUTION~~|
||0b - Abort disabled.<br>1b - Abort enabled.|
|11<br>FDEN|CAN FD operation enable<br>This bit enables the CAN with Flexible Data rate (CAN FD) operation. This bit can be written in Freeze<br>mode only.<br>FlexCAN is able to transmit FD frame format according to ISO 11898-1:2015.<br>~~NOTE~~|
||The Legacy Rx FIFO Enable (RFEN) bit cannot be set if FDEN is asserted.<br>~~NOTE~~<br>0b - CAN FD is disabled. FlexCAN is able to receive and transmit messages in CAN 2.0 format.<br>1b - CAN FD is enabled. FlexCAN is able to receive and transmit messages in both CAN FD and<br>CAN 2.0 formats.|
|10<br>—|Reserved|
|9-8|ID Acceptance Mode|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2782 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|IDAM|This 2-bit field identifies the format of the Legacy Rx FIFO ID filter table elements. Note that all elements of<br>the table are configured at the same time by this field (they are all the same format). See Legacy Rx FIFO<br>structure. This field can be written only in Freeze mode because it is blocked by hardware in other modes.<br>00b - Format A: One full ID (standard and extended) per ID filter table element.<br>01b - Format B: Two full standard IDs or two partial 14-bit (standard and extended) IDs per ID<br>filter table element.<br>10b - Format C: Four partial 8-bit standard IDs per ID filter table element.<br>11b - Format D: All frames rejected.|
|7<br>—|Reserved|
|6-0<br>MAXMB|Number Of The Last Message Buffer<br>This 7-bit field defines the number of the last message buffers that will take part in the matching and<br>arbitration processes. The reset value (0Fh) is equivalent to a 16 MB configuration. This field can be written<br>only in Freeze mode because it is blocked by hardware in other modes.<br>Number of the last MB = MAXMB<br>MAXMB must be programmed with a value smaller than or equal to the number of available<br>message buffers, as described inFlexCAN memory partition for CAN FD.<br>~~NOTE~~<br>Additionally, the definition of MAXMB value must take into account the region of MBs occupied by Legacy<br>Rx FIFO and its ID filters table space defined by CTRL2[RFFN]. MAXMB also impacts the definition of the<br>minimum number of peripheral clocks per CAN bit as described inTable 454.|



#### 72.6.2.3 Control 1 Register (CTRL1) 

##### Offset 

|Register|Offset|
|---|---|
|CTRL1|4h|



##### Function 

This Register is defined for specific FlexCAN control features related to the CAN bus, such as bit rate, programmable sampling point within an Rx bit, Loop Back mode, Listen-Only mode, Bus Off recovery behavior, and interrupt enabling (Bus-Off, Error, Warning). It also determines the division factor for the clock prescaler. 

The CAN bit timing variables (PRESDIV, PROPSEG, PSEG1, PSEG2, and RJW) can also be configured in the CBT register, which extends the range of all these variables. If CBT[BTF] is set, PRESDIV, PROPSEG, PSEG1, PSEG2, and RJW fields of CTRL1 become read only. 

If CTRL2[BTE] is set, then the PRESDIV, PROPSEG, PSEG1, PSEG2, and RJW fields in the CTRL1 register are not used by the hardware, are read as zero, and a write operation to them has no effect. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2783 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

~~<mark>NOTE</mark>~~ 

When the CAN FD feature is enabled, do not use the PRESDIV, RJW, PSEG1, PSEG2, and PROPSEG fields of the CTRL1 register for CAN bit timing. Instead use the CBT register's EPRESDIV, ERJW, EPSEG1, EPSEG2, and EPROPSEG fields. 

~~<mark>NOTE</mark>~~ 

The CAN bit variables in CTRL1 and in CBT are stored in the same register. 

The contents of this register are not affected by soft reset. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2784-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>PRESDIV  RJW  PSEG1  PSEG2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R BOFF ERRM Reserv TWRN RWRN Reserv Reserv BOFF<br>LPB  SMP  TSYN  LBUF  LOM  PROPSEG<br>W MSK  SK  ed  MSK  MSK  ed  ed  REC<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-24|Prescaler Division Factor|
|PRESDIV|This 8-bit field defines the ratio between the PE clock frequency and the serial clock (Sclock) frequency. The<br>Sclock period defines the time quantum of the CAN protocol. For the reset value, the Sclock frequency is<br>equal to the PE clock frequency. The maximum value of this field is FFh, which gives a minimum Sclock<br>frequency equal to the PE clock frequency divided by 256. SeeProtocol timingfor more information. This<br>field can be written only in Freeze mode because it is blocked by hardware in other modes.<br>Sclock frequency = PE clock frequency / (PRESDIV + 1).|
|23-22<br>RJW|Resync Jump Width<br>This 2-bit field defines the maximum number of time quanta that a bit time can be changed by one<br>resynchronization. One time quantum is equal to the Sclock period. The valid programmable values are 0–3.<br>SeeProtocol timingfor more information. This field can be written only in Freeze mode because it is blocked<br>by hardware in other modes.<br>Resync Jump Width = RJW + 1.|
|21-19<br>PSEG1|Phase Segment 1<br>This 3-bit field defines the length of phase segment 1 in the bit time. The valid programmable values are 0–7.<br>SeeProtocol timingfor more information. This field can be written only in Freeze mode because it is blocked<br>by hardware in other modes.<br>Phase Buffer Segment1 = (PSEG1 + 1) × Time-Quanta.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2784 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|18-16<br>PSEG2|Phase Segment 2<br>This 3-bit field defines the length of phase segment 2 in the bit time. The valid programmable values are 1–7.<br>SeeProtocol timingfor more information. This field can be written only in Freeze mode because it is blocked<br>by hardware in other modes.<br>Phase Buffer Segment 2 = (PSEG2 + 1) × Time-Quanta.|
|15|Bus Off Interrupt Mask|
|BOFFMSK|This bit provides a mask for the Bus Off interrupt ESR1[BOFFINT].<br>0b - Bus Off interrupt disabled.<br>1b - Bus Off interrupt enabled.|
|14<br>ERRMSK|Error Interrupt Mask<br>This bit provides a mask for the Error interrupt ESR1[ERRINT].<br>0b - Error interrupt disabled.<br>1b - Error interrupt enabled.|
|13|Reserved|
|—|This field is writeable only if the module is disabled. Otherwise the access type is read-only.<br>~~NOTE~~|
|12<br>LPB|Loop Back Mode<br>This bit configures FlexCAN to operate in Loop-Back mode. In this mode, FlexCAN performs an internal loop<br>back that can be used for self-test operation. The bit stream output of the transmitter is fed back internally<br>to the receiver input. The Rx CAN input pin is ignored and the Tx CAN output goes to the recessive state<br>(logic 1). FlexCAN behaves as it normally does when transmitting, and treats its own transmitted message<br>as a message received from a remote node.<br>In this mode, FlexCAN ignores the bit sent during the ACK slot in the CAN frame acknowledge field,<br>generating an internal acknowledge bit to ensure proper reception of its own message. Both transmit and<br>receive interrupts are generated. This bit can be written only in Freeze mode because it is blocked by<br>hardware in other modes.<br>In this mode, MCR[SRXDIS] cannot be asserted because this will impede the self-reception<br>of a transmitted message.<br>~~NOTE~~<br>FDCTRL[TDCEN] and ETDC[ETDCEN] must be disabled when LPB is asserted.<br>~~NOTE~~<br>0b - Loop Back disabled.<br>1b - Loop Back enabled.|
|11|Tx Warning Interrupt Mask|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2785 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|TWRNMSK|This bit provides a mask for the Tx Warning interrupt associated with the TWRNINT flag in the Error<br>and Status Register 1 (ESR1). This bit is read as zero when MCR[WRNEN] is negated. This bit can be<br>written only if MCR[WRNEN] is asserted.<br>0b - Tx Warning interrupt disabled.<br>1b - Tx Warning interrupt enabled.|
|10<br>RWRNMSK|Rx Warning Interrupt Mask<br>This bit provides a mask for the Rx Warning interrupt associated with the RWRNINT flag in the Error and<br>Status Register 1 (ESR1). This bit is read as zero when MCR[WRNEN] bit is negated. This bit can be<br>written only if MCR[WRNEN] bit is asserted.<br>0b - Rx Warning interrupt disabled.<br>1b - Rx Warning interrupt enabled.|
|9<br>—<br>8<br>—|Reserved<br>Reserved|
|7<br>SMP|CAN Bit Sampling<br>This bit defines the sampling mode of CAN bits at the Rx input. It can be written in Freeze mode only,<br>because it is blocked by hardware in other modes.<br>For proper operation, to assert SMP it is necessary to guarantee a minimum value of two<br>TQs in CTRL1[PSEG1] (or CBT[EPSEG1]).This bit cannot be asserted when CAN FD is<br>enabled (MCR[FDEN] = 1).<br>~~NOTE~~<br>0b - Just one sample is used to determine the bit value.<br>1b - Three samples are used to determine the value of the received bit: the regular one (sample<br>point) and two preceding samples; a majority rule is used.|
|6<br>BOFFREC|Bus Off Recovery<br>This bit defines how FlexCAN recovers from Bus Off state. If this bit is negated, automatic recovering<br>from Bus Off state occurs according to the CAN Specification 2.0B. If the bit is asserted, automatic<br>recovering from Bus Off is disabled and the module remains in Bus Off state until the bit is negated by<br>the user. If the negation occurs before 128 sequences of 11 recessive bits are detected on the CAN bus,<br>then Bus Off recovery happens as if the BOFFREC bit had never been asserted. If the negation occurs<br>after 128 sequences of 11 recessive bits occurred, then FlexCAN will resynchronize to the bus by waiting<br>for 11 recessive bits before joining the bus. After negation, the BOFFREC bit can be reasserted again<br>during Bus Off, but it will be effective only the next time the module enters Bus Off. If BOFFREC was<br>negated when the module entered Bus Off, asserting it during Bus Off will not be effective for the current<br>Bus Off recovery.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2786 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field|Function<br>See Bus off in the CAN Protocol standard (ISO 11898-1:2015) for details.<br>~~NOTE~~<br>0b - Automatic recovering from Bus Off state enabled.<br>1b - Automatic recovering from Bus Off state disabled.|
|---|---|
|5<br>TSYN|Timer Sync<br>This bit enables a mechanism that resets the free running timer each time a message is received in message<br>buffer 0. This feature provides means to synchronize multiple FlexCAN stations with a special “SYNC”<br>message, that is, global network time. If MCR[RFEN] is set (Legacy Rx FIFO enabled), the first available<br>mailbox, according to CTRL2[RFFN] setting, is used for timer synchronization instead of MB0. This bit can<br>be written in Freeze mode only because it is blocked by hardware in other modes.<br>0b - Timer sync feature disabled<br>1b - Timer sync feature enabled|
|4<br>LBUF|Lowest Buffer Transmitted First<br>This bit defines the ordering mechanism for message buffer transmission. When asserted,<br>MCR[LPRIOEN] does not affect the priority arbitration. This bit can be written in Freeze mode only,<br>because it is blocked by hardware in other modes.<br>0b - Buffer with highest priority is transmitted first.<br>1b - Lowest number buffer is transmitted first.|
|3<br>LOM|Listen-Only Mode<br>This bit configures FlexCAN to operate in Listen-Only mode. In this mode, transmission is disabled, all<br>error counters described in the ECR register are frozen, and the module operates in a CAN Error Passive<br>mode. Only messages acknowledged by another CAN station will be received. If FlexCAN detects a<br>message that has not been acknowledged, it will flag a BIT0 error without changing the receive error counter<br>(ECR[RXERRCNT]), as if it was trying to acknowledge the message.<br>Listen-Only mode is acknowledged by the state of ESR1[FLTCONF] indicating Passive Error. There can be<br>some delay between the Listen-Only mode request and acknowledge.<br>This bit can be written in Freeze mode only because it is blocked by hardware in other modes.<br>0b - Listen-Only mode is deactivated.<br>1b - FlexCAN module operates in Listen-Only mode.|
|2-0<br>PROPSEG|Propagation Segment<br>This 3-bit field defines the length of the propagation segment in the bit time. The valid programmable values<br>are 0–7. This field can be written only in Freeze mode because it is blocked by hardware in other modes.<br>Propagation segment time = (PROPSEG + 1) × time-quanta.<br>Time-quantum = one Sclock period.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2787 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

#### 72.6.2.4 Free Running Timer (TIMER) 

##### Offset 

|Register|Offset|
|---|---|
|TIMER|8h|



##### Function 

This register represents a 16-bit free-running counter that can be read and written by the CPU. The timer starts from 0h after Reset, counts linearly to FFFFh, and wraps around. 

When CTRL2[TIMER_SRC] is asserted, the timer is continuously incremented by an external time tick. The time tick must be synchronous to the peripheral clock, with a minimum pulse width of one clock cycle. 

When CTRL2[TIMER_SRC] is negated, the timer is incremented by the CAN bit clock, which defines the baud rate on the CAN bus. During a message transmission/reception, it increments by one for each bit that is received or transmitted. When there is no message on the bus, it counts using the previously programmed baud rate. The timer is not incremented during Disable and Freeze modes. 

The timer value is captured when the second bit of the identifier field of any frame is on the CAN bus. This captured value is written into the time stamp entry in a message buffer after a successful reception or transmission of a message. 

If CTRL1[TSYN] is asserted, the timer is reset whenever a message is received in the first available mailbox, according to CTRL2[RFFN] setting. 

The CPU can write to this register anytime. However, if the write occurs at the same time that the timer is being reset by a reception in the first mailbox, then the write value is discarded. 

Reading this register affects the mailbox unlocking procedure (see Mailbox lock mechanism). 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2788-14.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>TIMER<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16<br>—|Reserved|
|15-0|Timer Value|
|TIMER|Contains the free-running counter value.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2788 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

#### 72.6.2.5 Rx Mailboxes Global Mask Register (RXMGMASK) 

##### Offset 

|Register|Offset|
|---|---|
|RXMGMASK|10h|



##### Function 

This register is located in RAM. 

RXMGMASK is provided for legacy application support. 

- When MCR[IRMQ] is negated, RXMGMASK is always in effect (the bits in the MG field will mask the mailbox filter bits). 

- When MCR[IRMQ] is asserted, RXMGMASK has no effect (the bits in the MG field will not mask the mailbox filter bits). 

RXMGMASK is used to mask the filter fields of all Rx MBs, excluding MBs 14-15, which have individual mask registers. This register can only be written in Freeze mode as it is blocked by hardware in other modes. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2789-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>MG<br>W<br>Reset u u u u u u u u u u u u u u u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>MG<br>W<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

Fields 

|Field|Function|||||||
|---|---|---|---|---|---|---|---|
|31-0|Rx Mailboxes|Global Mask Bits||||||
|MG|These bits mas<br>as the two mos<br>word of the ma|k the mailbox filte<br>t significant MG bit<br>ilbox. The followin|r bits. Note that th<br>s affect the fields<br>g table shows in|e alignment w<br>RTR and IDE,<br>detail which M|ith the ID word<br>which are loca<br>G bits mask e|of the mailbox<br>ted in the Cont<br>ach mailbox fi|is not perfect<br>rol and Status<br>lter field.|
||SMB[RTR]<sup>1</sup>|CTRL2[RRS]|CTRL2[EACE<br>||Mailbox f|ilter fields||
||||N]|MB[RTR]|MB[IDE]|MB[ID]|Reserved|
||0|—|0|note<sup>2</sup>|note<sup>3</sup>|MG[28:0]|MG[31:29]|
||0|—|1|MG[31]|MG[30]|MG[28:0]|MG[29]|
||1|0|—|—|—|—|MG[31:0]|
||1|1|0|—|—|MG[28:0]|MG[31:29]|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2789 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

|Field|Function||||||
|---|---|---|---|---|---|---|
||SMB[RTR]<sup>1</sup><br>CTRL2[RRS]|CTRL2[EACE<br>||Mailbox f|ilter fields||
|||N]|MB[RTR]|MB[IDE]|MB[ID]|Reserved|
||1<br>1|1|MG[31]|MG[30]|MG[28:0]|MG[29]|
||1. RTR bit of the incoming fram<br>(Rx SMB).<br>2. If CTRL2[EACEN] is negate<br>incoming frame.<br>3. If CTRL2[EACEN] is negate<br>incoming frame.<br>0b - The corresponding b<br>1b - The corresponding b|e. It is saved int<br>d, the RTR bit of<br>d, the IDE bit of m<br>it in the filter is "d<br>it in the filter is ch|o an auxiliary<br>mailbox is nev<br>ailbox is alw<br>on't care."<br>ecked.|MB called Rx s<br>er compared w<br>ays compared|erial message<br>ith the RTR b<br>with the IDE bi|buffer<br>it of the<br>t of the|



#### 72.6.2.6 Rx 14 Mask Register (RX14MASK) 

##### Offset 

|Register|Offset|
|---|---|
|RX14MASK|14h|



##### Function 

This register is located in RAM. 

RX14MASK is provided for legacy application support. When MCR[IRMQ] is asserted, RX14MASK has no effect. 

RX14MASK is used to mask the filter fields of message buffer 14. 

This register can only be programmed when the module is in Freeze mode as it is blocked by hardware in other modes. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2790-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>RX14M<br>W<br>Reset u u u u u u u u u u u u u u u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>RX14M<br>W<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2790 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Fields 

|Field|Function|
|---|---|
|31-0|Rx Buffer 14 Mask Bits|
|RX14M|Each mask bit masks the corresponding mailbox 14 filter field in the same way that RXMGMASK masks<br>other mailboxes' filters. See the description of the RXMGMASK register.|
||0b - The corresponding bit in the filter is "don't care."|
||1b - The corresponding bit in the filter is checked.|



#### 72.6.2.7 Rx 15 Mask Register (RX15MASK) 

##### Offset 

|Register|Offset|
|---|---|
|RX15MASK|18h|



##### Function 

This register is located in RAM. 

RX15MASK is provided for legacy application support. When MCR[IRMQ] is asserted, RX15MASK has no effect. 

RX15MASK is used to mask the filter fields of message buffer 15. 

This register can be programmed only when the module is in Freeze mode because it is blocked by hardware in other modes. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2791-13.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>RX15M<br>W<br>Reset u u u u u u u u u u u u u u u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>RX15M<br>W<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Rx Buffer 15 Mask Bits|
|RX15M|Each mask bit masks the corresponding mailbox 15 filter field in the same way that RXMGMASK masks<br>other mailboxes' filters. See the description of the RXMGMASK register.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2791 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

|Field|Function|
|---|---|
||0b - The corresponding bit in the filter is "don't care."|
||1b - The corresponding bit in the filter is checked.|



#### 72.6.2.8 Error Counter (ECR) 

##### Offset 

|Register|Offset|
|---|---|
|ECR|1Ch|



##### Function 

This register has four 8-bit fields reflecting the value of the FlexCAN error counters: 

- Transmit Error Counter (TXERRCNT field) 

- Receive Error Counter (RXERRCNT field) 

- Transmit Error Counter for errors detected in the data phase of CAN FD messages with the BRS bit set (TXERRCNT_FAST field) 

- Receive Error Counter for errors detected in the data phase of CAN FD messages with the BRS bit set (RXERRCNT_FAST field) 

The TXERRCNT and RXERRCNT counters take into account all errors in both CAN FD and non-FD message formats. TXERRCNT_FAST and RXERRCNT_FAST are dedicated to count only the errors that occur in the data phase of CAN FD frames with the BRS bit set. 

The Fault Confinement state (ESR1[FLTCONF]) is updated based on TXERRCNT and RXERRCNT counters only. TXERRCNT and RXERRCNT counters can be written in Freeze mode only. TXERRCNT_FAST and RXERRCNT_FAST counters are read-only except in Freeze mode when the CPU can write value zero. The rules for increasing and decreasing these counters are described in the CAN protocol and are completely implemented in the FlexCAN module. 

The following are the basic rules for FlexCAN bus state transitions: 

- If the value of TXERRCNT or RXERRCNT becomes greater than or equal to 128, ESR1[FLTCONF] is updated to reflect Error Passive state. 

- If the FlexCAN state is Error Passive, and either TXERRCNT or RXERRCNT decrements to a value less than or equal to 127 when the other already satisfies this condition, ESR1[FLTCONF] is updated to reflect Error Active state. 

- If the value of TXERRCNT becomes greater than 255, ESR1[FLTCONF] is updated to reflect Bus Off state, and an interrupt may be issued. The value of TXERRCNT is then reset to zero. 

- If FlexCAN is in Bus Off state, then TXERRCNT is cascaded together with another internal counter to count the 128th occurrences of 11 consecutive recessive bits on the bus. Hence, TXERRCNT is reset to zero and counts in a manner where the internal counter counts 11 such bits and then wraps around when incrementing the TXERRCNT. When TXERRCNT reaches the value of 128, ESR1[FLTCONF] is updated to be Error Active and both error counters are reset to zero. At any instance of dominant bit following a stream of less than 11 consecutive recessive bits, the internal counter resets itself to zero without affecting the TXERRCNT value. The TXERRCNT_FAST counter is frozen during Bus Off. 

- If during system startup only one node is operating, then its TXERRCNT increases in each message it is trying to transmit, as a result of acknowledge errors (indicated by the ACKERR bit in the Error and Status Register). After the transition to Error Passive state, TXERRCNT does not increment anymore by acknowledge errors. Therefore the device never goes to the Bus Off state. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2792 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

- If RXERRCNT increases to a value greater than 127, it is not incremented further, even if more errors are detected when being a receiver. At the next successful message reception, the counter is set to a value between 119 and 127 to return to Error Active state. 

- TXERRCNT_FAST and RXERRCNT_FAST error counter values increment and decrement based on errors detected only in the data phase of CAN FD frames with the BRS bit set, following the same increment and decrement rules as TXERRCNT and RXERRCNT counters. These counters do not wrap around and get stuck at their maximum value (255). They stop counting and keep their values frozen when FlexCAN is in Bus Off state. They are reset when FlexCAN leaves Bus Off state and restart counting after FlexCAN returns to Error Active state. 

~~<mark>NOTE</mark>~~ 

See Fault confinement in the CAN Protocol standard (ISO 11898-1:2015) for details. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||RXERRC|NT_FAST|||||||TXERRCN|T_FAST||||
|W||||0||||||||0|||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||RXER|RCNT|||||||TXERR|CNT||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-24|Receive Error Counter for fast bits|
|RXERRCNT_F<br>AST|Receive error counter for errors detected in the data phase of received CAN FD messages with the BRS bit<br>set. The RXERRCNT_FAST counter is read-only except in Freeze mode, where the CPU can write an 8-bit<br>zero value only.|
|23-16|Transmit Error Counter for fast bits|
|TXERRCNT_FA<br>ST|Transmit error counter for errors detected in the data phase of transmitted CAN FD messages with the BRS<br>bit set. The TXERRCNT_FAST counter is read-only except in Freeze mode, where the CPU can write an<br>8-bit zero value only.|
|15-8|Receive Error Counter|
|RXERRCNT|Receive error counter for all errors detected in received messages. The RXERRCNT counter is read-<br>only except in Freeze mode, where it can be written by the CPU.|
|7-0|Transmit Error Counter|
|TXERRCNT|Transmit error counter for all errors detected in transmitted messages. The TXERRCNT counter is<br>read-only except in Freeze mode, where it can be written by the CPU.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2793 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

#### 72.6.2.9 Error and Status 1 Register (ESR1) 

##### Offset 

|Register|Offset|
|---|---|
|ESR1|20h|



##### Function 

This register reports various error conditions detected in the reception and transmission of a CAN frame, some general status of the device, and is the source of some interrupts to the CPU. The reported error conditions are: 

~~<mark>NOTE</mark>~~ Reading Host can clear these field. 

- Errors detected in CAN frames of any format: 

   - BIT1ERR 

   - BIT0ERR 

   - ACKKERR 

   - CRCERR 

   - FRMERR 

   - STFERR 

- Errors detected in the data phase of CAN FD frames with the BRS bit set only: 

   - BIT1ERR_FAST 

   - BIT0ERR_FAST 

   - CRCERR_FAST 

   - FRMERR_FAST 

   - STFERR_FAST 

An error detected in a single CAN frame may be reported by one or more error flags. Also, error reporting is cumulative, in case more error events happen in the next frames when the CPU does not attempt to read this register. 

##### Status bits: 

- TXWRN 

- RXWRN 

- IDLE 

- TX 

- FLTCONF 

- RX 

- SYNCH 

Interrupt bits: 

- BOFFINT 

- BOFFDONEINT 

- ERRINT 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2794 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

- ERRINT_FAST 

- TWRNINT 

- RWRNINT 

It is recommended that the CPU use the following procedure when servicing interrupt requests generated by these bits: 

1. Read this register to capture all error condition and status bits. This action clears the respective bits that were set since the last read access. 

2. Write 1 to clear the interrupt bit that has triggered the interrupt request. 

3. Write 1 to clear the ERR_OVR bit, if it is set. 

Starting from all error flags cleared, a first error event sets either the ERRINT or the ERRINT_FAST (provided the corresponding mask bit is asserted). If other error events in subsequent frames happen before the CPU serves the interrupt request, the ERR_OVR bit is set to indicate that errors from different frames have accumulated. 

Table 460. Can bus status 

|SYNCH|IDLE|TX|RX|FlexCAN state|
|---|---|---|---|---|
|0|0|0|0|Not synchronized to<br>CAN bus|
|1|1|x|x|Idle|
|1|0|1|0|Transmitting|
|1|0|0|1|Receiving|



~~<mark>NOTE</mark>~~ 

See Fault confinement in the CAN Protocol standard (ISO 11898-1:2015) for details. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2795-15.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>BIT1E BIT0E CRCE FRME STFE ERRO ERRIN BOFF SYNC TWRN RWRN<br>R 0 0<br>RR... RR... RR_... RR_... RR_... VR  T_... DON... H  INT  INT<br>W W1C W1C W1C W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>BIT1E BIT0E ACKE CRCE FRME STFE TXWR RXWR BOFFI ERRIN<br>R IDLE  TX  FLTCONF  RX  0<br>RR  RR  RR  RR  RR  RR  N  N  NT  T<br>W W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31|Bit1 Error in the Data Phase of CAN FD frames with the BRS bit set|
||This bit indicates when an inconsistency occurs between the transmitted and the received bit in the data|
||phase of CAN FD frames with the BRS bit set.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2795 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|BIT1ERR_FAS<br>T|After a read operation, the field's value clears to 0.<br>0b - No such occurrence.<br>1b - At least one bit sent as recessive is received as dominant.|
|30<br>BIT0ERR_FAS<br>T|Bit0 Error in the Data Phase of CAN FD frames with the BRS bit set<br>This bit indicates when an inconsistency occurs between the transmitted and the received bit in the data<br>phase of CAN FD frames with the BRS bit set.<br>After a read operation, the field's value clears to 0.<br>0b - No such occurrence.<br>1b - At least one bit sent as dominant is received as recessive.|
|29<br>—|Reserved|
|28<br>CRCERR_FAS<br>T|Cyclic Redundancy Check Error in the CRC field of CAN FD frames with the BRS bit set<br>This bit indicates that a CRC error has been detected by the receiver node in the CRC field of CAN FD<br>frames with the BRS bit set, that is, the calculated CRC is different from the received.<br>After a read operation, the field's value clears to 0.<br>0b - No such occurrence.<br>1b - A CRC error occurred since last read of this register.|
|27<br>FRMERR_FAS<br>T|Form Error in the Data Phase of CAN FD frames with the BRS bit set<br>This bit indicates that a form error has been detected by the receiver node in the data phase of CAN FD<br>frames with the BRS bit set, that is, a fixed-form bit field contains at least one illegal bit.<br>After a read operation, the field's value clears to 0.<br>0b - No such occurrence.<br>1b - A form error occurred since last read of this register.|
|26<br>STFERR_FAST|Stuffing Error in the Data Phase of CAN FD frames with the BRS bit set<br>This bit indicates that a stuffing error has been detected in the data phase of CAN FD frames with the<br>BRS bit set.<br>After a read operation, the field's value clears to 0.<br>0b - No such occurrence.<br>1b - A stuffing error occurred since last read of this register.|
|25-22<br>—<br>21|Reserved<br>Error Overrun|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2796 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table continued from the previous page... 

|Field<br>ERROVR|Function<br>This bit indicates that an error condition occurred when any error flag is already set. This bit is cleared by<br>writing it to 1.<br>0b - Overrun has not occurred.<br>1b - Overrun has occurred.|
|---|---|
|20|Error interrupt for errors detected in Data Phase of CAN FD frames with BRS bit set|
|ERRINT_FAST|This bit indicates that at least one of the error bits detected in the data phase of CAN FD frames with the<br>BRS bit set (BIT1ERR_FAST, BIT0ERR_FAST, CRCERR_FAST, FRMERR_FAST, or STFERR_FAST)<br>is set. If the corresponding mask bit CTRL2[ERRMSK_FAST] is set, an interrupt is generated to the<br>CPU. This bit is cleared by writing it to 1. Writing 0 has no effect.<br>0b - No such occurrence.<br>1b - Indicates setting of any error bit detected in the data phase of CAN FD frames with the BRS<br>bit set.|
|19|Bus Off Done Interrupt|
|BOFFDONEINT|This bit is set when the Tx Error Counter (TXERRCNT) has finished counting 128 occurrences of 11<br>consecutive recessive bits on the CAN bus and is ready to leave Bus Off. If the corresponding mask<br>bit in the Control 2 Register (BOFFDONEMSK) is set, an interrupt is generated to the CPU. This bit is<br>cleared by writing it to 1. Writing 0 has no effect.<br>0b - No such occurrence.<br>1b - FlexCAN module has completed Bus Off process.|
|18<br>SYNCH|CAN Synchronization Status<br>This read-only flag indicates whether the FlexCAN is synchronized to the CAN bus and able to participate<br>in the communication process. It is set and cleared by the FlexCAN. See the table in the overall ESR1<br>register description.<br>0b - FlexCAN is not synchronized to the CAN bus.<br>1b - FlexCAN is synchronized to the CAN bus.|
|17<br>TWRNINT|Tx Warning Interrupt Flag<br>If MCR[WRNEN] is asserted, TWRNINT is set when the TXWRN flag transitions from 0 to 1, meaning<br>that the Tx error counter reached 96. If the corresponding mask bit in the Control 1 Register<br>(CTRL1[TWRNMSK]) is set, an interrupt is generated to the CPU. This bit is cleared by writing it to 1. When<br>MCR[WRNEN] is negated, this flag is masked. CPU must clear this flag before disabling MCR[WRNEN].<br>Otherwise it will be set when MCR[WRNEN] is set again. Writing 0 has no effect. This flag is not generated<br>during Bus Off state. This bit is not updated during Freeze mode.<br>0b - No such occurrence.<br>1b - The Tx error counter transitioned from less than 96 to greater than or equal to 96.|
|16<br>RWRNINT|Rx Warning Interrupt Flag<br>If MCR[WRNEN] is asserted, RWRNINT is set when the RXWRN flag transitions from 0 to 1, meaning<br>that the Rx error counters reached 96. If the corresponding mask bit in the Control 1 Register|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2797 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field|Function<br>(CTRL1[RWRNMSK]) is set, an interrupt is generated to the CPU. This bit is cleared by writing it to<br>1. When WRNEN is negated, this flag is masked. CPU must clear this flag before disabling the bit. Otherwise<br>it will be set when WRNEN is set again. Writing 0 has no effect. This bit is not updated during Freeze mode.<br>0b - No such occurrence.<br>1b - The Rx error counter transitioned from less than 96 to greater than or equal to 96.|
|---|---|
|15<br>BIT1ERR|Bit1 Error<br>This bit indicates when an inconsistency occurs between the transmitted and the received bit in a non-CAN<br>FD message or in the arbitration or data phase of a CAN FD message.<br>This bit is not set by a transmitter in case of arbitration field or ACK slot, or in case of a node<br>sending a passive error flag that detects dominant bits.<br>~~NOTE~~<br>After a read operation, the field's value clears to 0.<br>0b - No such occurrence.<br>1b - At least one bit sent as recessive is received as dominant.|
|14|Bit0 Error|
|BIT0ERR|This bit indicates when an inconsistency occurs between the transmitted and the received bit in a non-CAN<br>FD message or in the arbitration or data phase of a CAN FD message.<br>After a read operation, the field's value clears to 0.<br>0b - No such occurrence.<br>1b - At least one bit sent as dominant is received as recessive.|
|13<br>ACKERR|Acknowledge Error<br>This bit indicates that an Acknowledge Error has been detected by the transmitter node, that is, a dominant<br>bit has not been detected during the ACK SLOT.<br>After a read operation, the field's value clears to 0.<br>0b - No such occurrence.<br>1b - An ACK error occurred since last read of this register.|
|12|Cyclic Redundancy Check Error|
|CRCERR|This bit indicates that aCyclic Redundancy Check(CRC) error has been detected by the receiver node<br>either in a non-FD message or in the arbitration or data phase of a frame in CAN FD format, that is, the<br>calculated CRC is different from the received.<br>After a read operation, the field's value clears to 0.<br>0b - No such occurrence.|
|11|1b - A CRC error occurred since last read of this register.<br>Form Error|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2798 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|FRMERR|This bit indicates that a form error has been detected in a non-FD message or else in an FD message's<br>arbitration or data phase by the receiver node, that is, a fixed-form bit field contains at least one illegal bit.<br>After a read operation, the field's value clears to 0.<br>0b - No such occurrence.<br>1b - A Form Error occurred since last read of this register.|
|10<br>STFERR|Stuffing Error<br>This bit indicates that astuffing errorhas been detected in a non-FD message or else in an FD message's<br>arbitration or data phase by the receiver node.<br>After a read operation, the field's value clears to 0.<br>0b - No such occurrence.<br>1b - A stuffing error occurred since last read of this register.|
|9<br>TXWRN|TX Error Warning<br>This bit indicates when repetitive errors are occurring during message transmission and is affected by the<br>value of TXERRCNT in ECR register only. This bit is not updated during Freeze mode.<br>After a read operation, the field's value clears to 0.<br>0b - No such occurrence.<br>1b - TXERRCNT is greater than or equal to 96.|
|8|Rx Error Warning|
|RXWRN|This bit indicates when repetitive errors are occurring during message reception and is affected by the value<br>of RXERRCNT in ECR register only. This bit is not updated during Freeze mode.<br>After a read operation, the field's value clears to 0.<br>0b - No such occurrence.<br>1b - RXERRCNT is greater than or equal to 96.|
|7<br>IDLE|IDLE<br>This bit indicates when CAN bus is in IDLE state. See the table in the overall ESR1 register description.<br>0b - No such occurrence.<br>1b - CAN bus is now IDLE.|
|6<br>TX|FlexCAN In Transmission<br>This bit indicates if FlexCAN is transmitting a message. See the table in the overall ESR1<br>register description.<br>0b - FlexCAN is not transmitting a message.|
||1b - FlexCAN is transmitting a message.|
|5-4|Fault Confinement State|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2799 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|FLTCONF|This 2-bit field indicates the confinement state of the FlexCAN module.<br>If CTRL1[LOM] is asserted, after a delay that depends on the CAN bit timing, ESR1[FLTCONF] will indicate<br>Error Passive. The very same delay affects the way that ESR1[FLTCONF] reflects an update to ECR<br>register by the CPU. It may be necessary to wait up to one CAN bit time to get them coherent again.<br>This bit field is affected by soft reset, but if the LOM bit is asserted, its reset value lasts just one CAN bit.<br>After this time, ESR1[FLTCONF] reports Error Passive.<br>00b - Error Active<br>01b - Error Passive<br>1xb - Bus Off|
|3<br>RX|FlexCAN In Reception<br>This bit indicates if FlexCAN is receiving a message. See the table in the overall ESR1 register description.<br>0b - FlexCAN is not receiving a message.<br>1b - FlexCAN is receiving a message.|
|2<br>BOFFINT|Bus Off Interrupt<br>This bit is set when FlexCAN enters Bus Off state. If the corresponding mask bit in the Control Register<br>1 (CTRL1[BOFFMSK]) is set, an interrupt is generated to the CPU. This bit is cleared by writing it to 1.<br>Writing 0 has no effect.<br>0b - No such occurrence.<br>1b - FlexCAN module entered Bus Off state.|
|1<br>ERRINT|Error Interrupt<br>This bit indicates that at least one of the error bits (BIT1ERR, BIT0ERR, ACKERR, CRCERR, FRMERR,<br>or STFERR) is set. If the corresponding mask bit CTRL1[ERRMSK] is set, an interrupt is generated to the<br>CPU. This bit is cleared by writing it to 1. Writing 0 has no effect.<br>0b - No such occurrence.<br>1b - Indicates setting of any error bit in the Error and Status register.|
|0<br>—|Reserved|



#### 72.6.2.10 Interrupt Masks 2 Register (IMASK2) 

##### Offset 

|Register|Offset|
|---|---|
|IMASK2|24h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2800 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Function 

This register allows any number of a range of the 32 message buffer interrupts to be enabled or disabled for MB63 to MB32. It contains one interrupt mask bit per buffer, enabling the CPU to determine which buffer generates an interrupt after a successful transmission or reception, that is, when the corresponding IFLAG2 bit is set. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2801-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>BUF63TO32M<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>BUF63TO32M<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Buffer MBi Mask|
|BUF63TO32M|Each bit enables or disables the corresponding FlexCAN message buffer interrupt for MB63 to MB32.|
||Setting or clearing a bit in the IMASK2 Register can assert or negate an interrupt request,<br>if the corresponding IFLAG2 bit is set.<br>~~NOTE~~|
||0b - The corresponding buffer interrupt is disabled.|
||1b - The corresponding buffer interrupt is enabled.|



#### 72.6.2.11 Interrupt Masks 1 Register (IMASK1) 

##### Offset 

|Register|Offset|
|---|---|
|IMASK1|28h|



##### Function 

This register allows any number of a range of the 32 message buffer interrupts to be enabled or disabled for MB31 to MB0. It contains one interrupt mask bit per buffer, enabling the CPU to determine which buffer generates an interrupt after a successful transmission or reception, that is, when the corresponding IFLAG1 bit is set. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2801 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2802-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>BUF31TO0M<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>BUF31TO0M<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Buffer MBi Mask|
|BUF31TO0M|Each bit enables or disables the corresponding FlexCAN message buffer interrupt for MB31 to MB0.|
||~~NOTE~~|
||Setting or clearing a bit in the IMASK1 Register can assert or negate an interrupt request,<br>if the corresponding IFLAG1 bit is set.|
||0b - The corresponding buffer interrupt is disabled.|
||1b - The corresponding buffer interrupt is enabled.|



#### 72.6.2.12 Interrupt Flags 2 Register (IFLAG2) 

##### Offset 

|Register|Offset|
|---|---|
|IFLAG2|2Ch|



##### Function 

This register defines the flags for the 32 message buffer interrupts for MB63 to MB32. It contains one interrupt flag bit per buffer. Each successful transmission or reception sets the respective IFLAG2 bit. If the corresponding IMASK2 bit is set, an interrupt will be generated. The interrupt flag must be cleared by writing 1 to it. Writing 0 has no effect. 

Before updating MCR[MAXMB], CPU must service the IFLAG2 bits whose MB value is greater than the MAXMB to be updated; otherwise, they will remain set and be inconsistent with the number of MBs available. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2802 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||BUF63|TO32I||||||||
|W||||||||W|1C||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||BUF63|TO32I||||||||
|W||||||||W|1C||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-0|Buffer MBi Interrupt|
|BUF63TO32I|Each bit flags the corresponding FlexCAN message buffer interrupt for MB63 to MB32.|
||0b - The corresponding buffer has no occurrence of successfully completed transmission or<br>reception.|
||1b - The corresponding buffer has successfully completed transmission or reception.|



#### 72.6.2.13 Interrupt Flags 1 Register (IFLAG1) 

##### Offset 

|Register|Offset|
|---|---|
|IFLAG1|30h|



##### Function 

This register defines the flags for the 32 message buffer interrupts for MB31 to MB0. It contains one interrupt flag bit per buffer. Each successful transmission or reception sets the corresponding IFLAG1 bit. If the corresponding IMASK1 bit is set, an interrupt will be generated. The interrupt flag must be cleared by writing 1 to it. Writing 0 has no effect. There is an exception when DMA for Legacy Rx FIFO is enabled, as described below. 

The BUF7I to BUF5I flags are also used to represent Legacy FIFO interrupts when the Legacy Rx FIFO is enabled. When MCR[RFEN] is set and MCR[DMA] is negated, the function of the eight least significant interrupt flags changes: BUF7I, BUF6I, and BUF5I indicate operating conditions of the Legacy FIFO , BUF0I is used to empty Legacy FIFO, and BUF4I to BUF1I bits are reserved. 

Before enabling MCR[RFEN], the CPU must service the IFLAG bits asserted in the Legacy Rx FIFO region; see Legacy Rx FIFO. Otherwise, these IFLAG bits will mistakenly show the related MBs now belonging to Legacy FIFO as having contents to be serviced. When MCR[RFEN] is negated, the Legacy FIFO flags must be cleared. The same care must be taken when a CTRL2[RFFN] value is selected, extending Legacy Rx FIFO filters beyond MB7. For example, when RFFN is 8h, the MB0–23 range is occupied by Legacy Rx FIFO filters and related IFLAG bits must be cleared. 

When both the MCR[RFEN] and MCR[DMA] bits are asserted (DMA feature for Legacy Rx FIFO enabled), the function of the eight least significant interrupt flags (BUF7I–BUF0I) are changed to support the DMA operation. BUF7I and BUF6I are not 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2803 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

used, as well as BUF4I–BUF1I. BUF5I indicates operating condition of Legacy FIFO, and BUF0I is used to empty Legacy FIFO. Moreover, BUF5I does not generate a CPU interrupt, but generates a DMA request. IMASK1 bits in Legacy Rx FIFO region are not considered when bit MCR[DMA] is enabled. In addition the CPU must not clear the flag BUF5I when DMA is enabled. Before enabling MCR[DMA], the CPU must service the IFLAGs asserted in the Legacy Rx FIFO region. When MCR[DMA] is negated, the Legacy FIFO must be empty. Legacy FIFO must be disabled when MCR[FDEN] is enabled. 

Before updating MCR[MAXMB], CPU must service the IFLAG1 bits whose MB value is greater than the MCR[MAXMB] to be updated; otherwise, they will remain set and be inconsistent with the number of MBs available. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||BUF|31TO8I||||||||
|W||||||||W|1C||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||BUF3|1TO8I||||BUF7I|BUF6I|BUF5I||BUF4T|O1I||BUF0I|
|W||||W|1C||||W1C|W1C|W1C||W1C|||W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-8|Buffer MBi Interrupt|
|BUF31TO8I|Each bit flags the corresponding FlexCAN message buffer interrupt for MB31 to MB8.<br>0b - The corresponding buffer has no occurrence of successfully completed transmission or<br>reception.<br>1b - The corresponding buffer has successfully completed transmission or reception.|
|7<br>BUF7I|Buffer MB7 Interrupt Or Legacy Rx FIFO Overflow<br>When MCR[RFEN] is cleared (Legacy Rx FIFO disabled), this bit flags the interrupt for MB7.<br>This flag is cleared by the FlexCAN whenever MCR[RFEN] is changed by CPU writes.<br>~~NOTE~~|
||The BUF7I flag represents Legacy Rx FIFO overflow when MCR[RFEN] is set. In this case, the flag indicates<br>that a message was lost because the Legacy Rx FIFO is full. Note that the flag will not be asserted when<br>the Legacy Rx FIFO is full and the message was captured by a mailbox.|
||The descriptions of the field settings vary by module instance.<br>~~NOTE~~|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2804 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field<br>Function||
|---|---|
|Instance|Field value and description|
|CAN_0|0b - No occurrence of MB7 completing transmission/reception when<br>MCR[RFEN]=0, or of Legacy Rx FIFO overflow when MCR[RFEN]=1<br>1b - MB7 completed transmission/reception when MCR[RFEN]=0, or<br>Legacy Rx FIFO overflow when MCR[RFEN]=1|
|CAN_1|0b - No occurrence of MB7 completing transmission/reception when<br>MCR[RFEN]=0, or of Legacy Rx FIFO overflow when MCR[RFEN]=1<br>1b - MB7 completed transmission/reception when MCR[RFEN]=0, or<br>Legacy Rx FIFO overflow when MCR[RFEN]=1|
|CAN_2|0b - No occurrence of MB7 completing transmission/reception when<br>MCR[RFEN]=0, or of Legacy Rx FIFO overflow when MCR[RFEN]=1<br>1b - MB7 completed transmission/reception when MCR[RFEN]=0, or<br>Legacy Rx FIFO overflow when MCR[RFEN]=1|
|CAN_3|0b - No occurrence of MB7 completing transmission/reception when<br>MCR[RFEN]=0, or of Rx FIFO overflow when MCR[RFEN]=1<br>1b - MB7 completed transmission/reception when MCR[RFEN]=0, or Rx<br>FIFO overflow when MCR[RFEN]=1|
|CAN_4|0b - No occurrence of MB7 completing transmission/reception when<br>MCR[RFEN]=0, or of Rx FIFO overflow when MCR[RFEN]=1<br>1b - MB7 completed transmission/reception when MCR[RFEN]=0, or Rx<br>FIFO overflow when MCR[RFEN]=1|
|CAN_5|0b - No occurrence of MB7 completing transmission/reception when<br>MCR[RFEN]=0, or of Rx FIFO overflow when MCR[RFEN]=1<br>1b - MB7 completed transmission/reception when MCR[RFEN]=0, or Rx<br>FIFO overflow when MCR[RFEN]=1|
|CAN_6|0b - No occurrence of MB7 completing transmission/reception when<br>MCR[RFEN]=0, or of Rx FIFO overflow when MCR[RFEN]=1<br>1b - MB7 completed transmission/reception when MCR[RFEN]=0, or Rx<br>FIFO overflow when MCR[RFEN]=1|
|CAN_7|0b - No occurrence of MB7 completing transmission/reception when<br>MCR[RFEN]=0, or of Rx FIFO overflow when MCR[RFEN]=1<br>1b - MB7 completed transmission/reception when MCR[RFEN]=0, or Rx<br>FIFO overflow when MCR[RFEN]=1|
|6<br>Buffer MB6 Interrupt Or L|egacy Rx FIFO Warning|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2805 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field<br>BUF6I|Function<br>When MCR[RFEN] is cleared (Legacy Rx FIFO disabled), this bit flags the interrupt for MB6.<br>This flag is cleared by the FlexCAN whenever MCR[RFEN] is changed by CPU writes.<br>~~NOTE~~<br>The BUF6I flag represents Legacy Rx FIFO warning when MCR[RFEN] is set. In this case, the flag indicates<br>when the number of unread messages within the Legacy Rx FIFO is increased to five from four due to the<br>reception of a new one, meaning that the Legacy Rx FIFO is almost full. Note that if the flag is cleared when<br>the number of unread messages is greater than four, it does not assert again until the number of unread<br>messages within the Legacy Rx FIFO is decreased to be equal to or less than four.<br>The descriptions of the field settings vary by module instance.<br>~~NOTE~~|
|---|---|
||Instance<br>Field value and description|
||CAN_0<br>0b - No occurrence of MB6 completing transmission/reception when<br>MCR[RFEN]=0, or of Legacy Rx FIFO almost full when MCR[RFEN]=1<br>1b - MB6 completed transmission/reception when MCR[RFEN]=0, or<br>Legacy Rx FIFO almost full when MCR[RFEN]=1|
||CAN_1<br>0b - No occurrence of MB6 completing transmission/reception when<br>MCR[RFEN]=0, or of Legacy Rx FIFO almost full when MCR[RFEN]=1<br>1b - MB6 completed transmission/reception when MCR[RFEN]=0, or<br>Legacy Rx FIFO almost full when MCR[RFEN]=1|
||CAN_2<br>0b - No occurrence of MB6 completing transmission/reception when<br>MCR[RFEN]=0, or of Legacy Rx FIFO almost full when MCR[RFEN]=1<br>1b - MB6 completed transmission/reception when MCR[RFEN]=0, or<br>Legacy Rx FIFO almost full when MCR[RFEN]=1|
||CAN_3<br>0b - No occurrence of MB6 completing transmission/reception when<br>MCR[RFEN]=0, or of Rx FIFO almost full when MCR[RFEN]=1<br>1b - MB6 completed transmission/reception when MCR[RFEN]=0, or Rx<br>FIFO almost full when MCR[RFEN]=1|
||CAN_4<br>0b - No occurrence of MB6 completing transmission/reception when<br>MCR[RFEN]=0, or of Rx FIFO almost full when MCR[RFEN]=1<br>1b - MB6 completed transmission/reception when MCR[RFEN]=0, or Rx<br>FIFO almost full when MCR[RFEN]=1|
||CAN_5<br>0b - No occurrence of MB6 completing transmission/reception when<br>MCR[RFEN]=0, or of Rx FIFO almost full when MCR[RFEN]=1<br>1b - MB6 completed transmission/reception when MCR[RFEN]=0, or Rx<br>FIFO almost full when MCR[RFEN]=1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2806 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||Instance<br>Field value and description|
||CAN_6<br>0b - No occurrence of MB6 completing transmission/reception when<br>MCR[RFEN]=0, or of Rx FIFO almost full when MCR[RFEN]=1<br>1b - MB6 completed transmission/reception when MCR[RFEN]=0, or Rx<br>FIFO almost full when MCR[RFEN]=1|
||CAN_7<br>0b - No occurrence of MB6 completing transmission/reception when<br>MCR[RFEN]=0, or of Rx FIFO almost full when MCR[RFEN]=1<br>1b - MB6 completed transmission/reception when MCR[RFEN]=0, or Rx<br>FIFO almost full when MCR[RFEN]=1|
|5<br>BUF5I|Buffer MB5 Interrupt Or Frames available in Legacy Rx FIFO<br>When MCR[RFEN] is cleared (Legacy Rx FIFO disabled), this field flags the interrupt for MB5.<br>This flag is cleared by the FlexCAN whenever MCR[RFEN] is changed by CPU writes.<br>~~NOTE~~<br>When MCR[RFEN] is set (Legacy Rx FIFO enabled), the BUF5I flag represents "Frames available in Legacy<br>Rx FIFO" and indicates that at least one frame is available to be read from the Legacy Rx FIFO. When the<br>MCR[DMA] bit is enabled, this flag generates a DMA request and the CPU must not clear this bit by writing<br>1 in BUF5I.<br>The descriptions of the field settings vary by module instance.<br>~~NOTE~~|
||Instance<br>Field value and description|
||CAN_0<br>0b - No occurrence of MB5 completing transmission/reception<br>when MCR[RFEN]=0, or of frame(s) available in the Legacy FIFO,<br>when MCR[RFEN]=1<br>1b - MB5 completed transmission/reception when MCR[RFEN]=0, or<br>frame(s) available in the Legacy Rx FIFO when MCR[RFEN]=1. It<br>generates a DMA request in case of MCR[RFEN] and MCR[DMA]<br>are enabled.|
||CAN_1<br>0b - No occurrence of MB5 completing transmission/reception<br>when MCR[RFEN]=0, or of frame(s) available in the Legacy FIFO,<br>when MCR[RFEN]=1<br>1b - MB5 completed transmission/reception when MCR[RFEN]=0, or<br>frame(s) available in the Legacy Rx FIFO when MCR[RFEN]=1. It<br>generates a DMA request in case of MCR[RFEN] and MCR[DMA]<br>are enabled.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2807 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field<br>Function||
|---|---|
|Instance|Field value and description|
|CAN_2|0b - No occurrence of MB5 completing transmission/reception<br>when MCR[RFEN]=0, or of frame(s) available in the Legacy FIFO,<br>when MCR[RFEN]=1<br>1b - MB5 completed transmission/reception when MCR[RFEN]=0, or<br>frame(s) available in the Legacy Rx FIFO when MCR[RFEN]=1. It<br>generates a DMA request in case of MCR[RFEN] and MCR[DMA]<br>are enabled.|
|CAN_3|0b - No occurrence of MB5 completing transmission/reception<br>when MCR[RFEN]=0, or of frame(s) available in the FIFO,<br>when MCR[RFEN]=1<br>1b - MB5 completed transmission/reception when MCR[RFEN]=0, or<br>frame(s) available in the Rx FIFO when MCR[RFEN]=1. It generates a<br>DMA request in case of MCR[RFEN] and MCR[DMA] are enabled.|
|CAN_4|0b - No occurrence of MB5 completing transmission/reception<br>when MCR[RFEN]=0, or of frame(s) available in the FIFO,<br>when MCR[RFEN]=1<br>1b - MB5 completed transmission/reception when MCR[RFEN]=0, or<br>frame(s) available in the Rx FIFO when MCR[RFEN]=1. It generates a<br>DMA request in case of MCR[RFEN] and MCR[DMA] are enabled.|
|CAN_5|0b - No occurrence of MB5 completing transmission/reception<br>when MCR[RFEN]=0, or of frame(s) available in the FIFO,<br>when MCR[RFEN]=1<br>1b - MB5 completed transmission/reception when MCR[RFEN]=0, or<br>frame(s) available in the Rx FIFO when MCR[RFEN]=1. It generates a<br>DMA request in case of MCR[RFEN] and MCR[DMA] are enabled.|
|CAN_6|0b - No occurrence of MB5 completing transmission/reception<br>when MCR[RFEN]=0, or of frame(s) available in the FIFO,<br>when MCR[RFEN]=1<br>1b - MB5 completed transmission/reception when MCR[RFEN]=0, or<br>frame(s) available in the Rx FIFO when MCR[RFEN]=1. It generates a<br>DMA request in case of MCR[RFEN] and MCR[DMA] are enabled.|
|CAN_7|0b - No occurrence of MB5 completing transmission/reception<br>when MCR[RFEN]=0, or of frame(s) available in the FIFO,<br>when MCR[RFEN]=1<br>1b - MB5 completed transmission/reception when MCR[RFEN]=0, or<br>frame(s) available in the Rx FIFO when MCR[RFEN]=1. It generates a<br>DMA request in case of MCR[RFEN] and MCR[DMA] are enabled.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2808 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|4-1|Buffer MBi Interrupt Or Reserved|
|BUF4TO1I|When MCR[RFEN] is cleared (Legacy Rx FIFO disabled), these bits flag the interrupts for MB4 to MB1.<br>These flags are cleared by the FlexCAN whenever MCR[RFEN] is changed by CPU writes.<br>~~NOTE~~<br>The BUF4TO1I flags are reserved when MCR[RFEN] is set.<br>0b - The corresponding buffer has no occurrence of successfully completed transmission or<br>reception when MCR[RFEN]=0.<br>1b - The corresponding buffer has successfully completed transmission or reception when<br>MCR[RFEN]=0.|
|0<br>BUF0I|Buffer MB0 Interrupt Or Clear Legacy FIFO bit<br>When MCR[RFEN] is cleared (Legacy Rx FIFO disabled), this field flags the interrupt for MB0. If the Legacy<br>Rx FIFO is enabled, this bit is used to trigger the clear Legacy FIFO operation. This operation empties<br>Legacy FIFO contents. Before performing this operation the CPU must service all Legacy FIFO related<br>IFLAGs. When MCR[DMA] is enabled this operation also clears the BUF5I flag and consequently aborts the<br>DMA request. The clear Legacy FIFO operation occurs when the CPU writes 1 in BUF0I. It is only allowed<br>in Freeze mode and is blocked by hardware in other conditions.<br>0b - The corresponding buffer has no occurrence of successfully completed transmission or<br>reception when MCR[RFEN]=0.<br>1b - The corresponding buffer has successfully completed transmission or reception when<br>MCR[RFEN]=0.|



#### 72.6.2.14 Control 2 Register (CTRL2) 

##### Offset 

|Register|Offset|
|---|---|
|CTRL2|34h|



##### Function 

This register complements Control1 register, providing control bits for memory write access in Freeze mode, for extending Legacy FIFO filter quantity, and to adjust the operation of internal FlexCAN processes like matching and arbitration. 

The contents of this register are not affected by soft reset. 

This table shows how the Legacy Rx FIFO filter structure is determined by the value of CTRL2[RFFN]. See the CTRL2[RFFN] field description for more information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2809 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table 461. Legacy Rx FIFO filter: possible structures 

|RFFN[3:0]|Number of<br>LegacyRx<br>FIFO filter<br>elements|Message buffers<br>occupied byLegacy<br>Rx FIFO and ID filter<br>table|Remaining available<br>mailboxes|LegacyRx FIFO ID filter<br>table elements affected<br>by Rx individual masks|LegacyRx FIFO ID filter<br>table elements affected<br>byLegacyRx FIFO<br>global mask|
|---|---|---|---|---|---|
|0h|8|MB 0-7|MB 8-95|Elements 0-7|none|
|1h|16|MB 0-9|MB 10-95|Elements 0-9|Elements 10-15|
|2h|24|MB 0-11|MB 12-95|Elements 0-11|Elements 12-23|
|3h|32|MB 0-13|MB 14-95|Elements 0-13|Elements 14-31|
|4h|40|MB 0-15|MB 16-95|Elements 0-15|Elements 16-39|
|5h|48|MB 0-17|MB 18-95|Elements 0-17|Elements 18-47|
|6h|56|MB 0-19|MB 20-95|Elements 0-19|Elements 20-55|
|7h|64|MB 0-21|MB 22-95|Elements 0-21|Elements 22-63|
|8h|72|MB 0-23|MB 24-95|Elements 0-23|Elements 24-71|
|9h|80|MB 0-25|MB 26-95|Elements 0-25|Elements 26-79|
|Ah|88|MB 0-27|MB 28-95|Elements 0-27|Elements 28-87|
|Bh|96|MB 0-29|MB 30-95|Elements 0-29|Elements 30-95|
|Ch|104|MB 0-31|MB 32-95|Elements 0-31|Elements 32-103|
|Dh|112|MB 0-33|MB 34-95|Elements 0-31|Elements 32-111|
|Eh|120|MB 0-35|MB 36-95|Elements 0-31|Elements 32-119|
|Fh|128|MB 0-37|MB 38-95|Elements 0-31|Elements 32-127|



##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23<br>22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|ERRM<br>SK_...|BOFF<br>DON...|ECRW<br>RE|WRMF<br>RZ||RF|FN|||TASD|||MRP|RRS|EACE<br>N|
|Reset|||||||See|Register|reset values.|||||||
|Bits|15|14|13|12|11|10|9|8|7<br>6|5|4|3|2|1|0|
|R<br>W|TIMER<br>_S...|PREX<br>CEN|BTE|ISOCA<br>NF...|EDFLT<br>DIS|0|MBTS|BASE|TSTAMPCAP||||0|||
|Reset|||||||See|Register|reset values.|||||||



##### Register reset values 

|Register|Reset value|
|---|---|
|CTRL2|CAN_0–CAN_2: 0060_0000h|
||CAN_3–CAN_7: 0080_0000h|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2810 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Fields 

|Field|Function|
|---|---|
|31<br>ERRMSK_FAS<br>T|Error Interrupt Mask for errors detected in the data phase of fast CAN FD frames<br>This bit provides a mask for the ERRINT_FAST interrupt in ESR1 register.<br>0b - ERRINT_FAST error interrupt disabled.<br>1b - ERRINT_FAST error interrupt enabled.|
|30<br>BOFFDONEMS<br>K|Bus Off Done Interrupt Mask<br>This bit provides a mask for the bus off done interrupt in ESR1 register.<br>0b - Bus off done interrupt disabled.<br>1b - Bus off done interrupt enabled.|
|29<br>ECRWRE|Error-correction Configuration Register Write Enable<br>This bit enables the MECR register to be updated. This bit is automatically set to 0 if the protocol described<br>inDetection and correction of memory errorsis not followed.<br>0b - Disable update.<br>1b - Enable update.|
|28<br>WRMFRZ|Write-Access To Memory In Freeze Mode<br>Enable unrestricted write access to FlexCAN memory in Freeze mode. This bit can only be written in Freeze<br>mode and has no effect out of Freeze mode.<br>MCR[RFEN] must not be set during FlexCAN memory initialization.<br>0b - Maintain the write access restrictions.<br>1b - Enable unrestricted write access to FlexCAN memory.|
|27-24<br>RFFN|Number Of Legacy Rx FIFO Filters<br>This 4-bit field defines the number of Rx Legacy FIFO filters, as shown inTable 461. The maximum<br>selectable number of filters is determined by the chip. This field can only be written in Freeze mode as it is<br>blocked by hardware in other modes. This field must not be programmed with values that cause the number<br>of message buffers occupied by Legacy Rx FIFO and Legacy Rx FIFO ID Filter to exceed the number of<br>mailboxes present, as defined by MCR[MAXMB].|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2811 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

Field Function ~~<mark>NOTE</mark>~~ Each group of eight filters occupies a memory space equivalent to two message buffers, which means that the more filters are implemented the fewer mailboxes will be available. Considering that the Legacy Rx FIFO occupies the memory space originally reserved for MB0-5, RFFN should be programmed with a value corresponding to a number of filters not greater than the number of available memory words, which can be calculated as follows: (SETUP_MB - 6) × 4 where SETUP_MB is the smaller of the parameter NUMBER_OF_MB and MCR[MAXMB]. The number of remaining mailboxes available will be: (SETUP_MB - 8) - (RFFN × 2) If the number of Legacy Rx FIFO filters programmed through RFFN exceeds the SETUP_MB value (memory space available), then the exceeding ones will not be functional. 

~~<mark>NOTE</mark>~~ • The number of the last remaining available mailboxes is defined by the smaller of NUMBER_OF_MB minus 1 and MCR[MAXMB]. • If Rx Individual Mask registers are not enabled then all Legacy Rx FIFO filters are affected by the Legacy Rx FIFO Global Mask. 23-19 Tx Arbitration Start Delay TASD This 5-bit field indicates how many CAN bits the Tx arbitration process start point can be delayed from the first bit of CRC field on CAN bus. See Tx arbitration start delay for more details. This field can be written only in Freeze mode because it is blocked by hardware in other modes. 18 Mailboxes Reception Priority MRP If this bit is set the matching process starts from the mailboxes and if no match occurs the matching continues on the Legacy Rx FIFO or Enhanced RX FIFO . This bit can be written only in Freeze mode because it is blocked by hardware in other modes. 

~~<mark>NOTE</mark>~~ 

The descriptions of the field settings vary by module instance. 

|Instance|Field value and description|
|---|---|
|CAN_0|0b - Matching starts from Legacy Rx FIFO or Enhanced Rx FIFO and<br>continues on mailboxes.|
||1b - Matching starts from mailboxes and continues on Legacy Rx FIFO<br>or Enhanced Rx FIFO.|
|CAN_1|0b - Matching starts from Legacy Rx FIFO or Enhanced Rx FIFO and<br>continues on mailboxes.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2812 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||Instance<br>Field value and description|
||1b - Matching starts from mailboxes and continues on Legacy Rx FIFO<br>or Enhanced Rx FIFO.|
||CAN_2<br>0b - Matching starts from Legacy Rx FIFO or Enhanced Rx FIFO and<br>continues on mailboxes.<br>1b - Matching starts from mailboxes and continues on Legacy Rx FIFO<br>or Enhanced Rx FIFO.|
||CAN_3<br>0b - Matching starts from Rx FIFO and continues on mailboxes.<br>1b - Matching starts from mailboxes and continues on Rx FIFO.|
||CAN_4<br>0b - Matching starts from Rx FIFO and continues on mailboxes.<br>1b - Matching starts from mailboxes and continues on Rx FIFO.|
||CAN_5<br>0b - Matching starts from Rx FIFO and continues on mailboxes.<br>1b - Matching starts from mailboxes and continues on Rx FIFO.|
||CAN_6<br>0b - Matching starts from Rx FIFO and continues on mailboxes.<br>1b - Matching starts from mailboxes and continues on Rx FIFO.|
||CAN_7<br>0b - Matching starts from Rx FIFO and continues on mailboxes.<br>1b - Matching starts from mailboxes and continues on Rx FIFO.|
|17<br>RRS|Remote Request Storing<br>If this bit is asserted a remote request frame is submitted to a matching process and stored in the<br>corresponding message buffer in the same fashion as a data frame. No automatic remote response frame<br>will be generated.<br>If this bit is negated the remote request frame is submitted to a matching process and an automatic remote<br>response frame is generated if a message buffer with CODE = 1010b is found with the same ID.<br>This bit can be written only in Freeze mode because it is blocked by hardware in other modes.<br>0b - Remote response frame is generated.<br>1b - Remote request frame is stored.|
|16|Entire Frame Arbitration Field Comparison Enable For Rx Mailboxes|
|EACEN|This bit controls the comparison of IDE and RTR bits within Rx mailbox filters with their corresponding<br>bits in the incoming frame by the matching process. This bit does not affect matching for Legacy Rx FIFO<br>or Enhanced Rx FIFO. This bit can be written only in Freeze mode because it is blocked by hardware in<br>other modes.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2813 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Rx mailbox filter’s IDE bit is always compared and RTR is never compared despite mask bits.<br>1b - Enables the comparison of both Rx mailbox filter’s IDE and RTR bit with their corresponding<br>bits within the incoming frame. Mask bits do apply.|
|15<br>TIMER_SRC|Timer Source<br>Selects the time tick source used for incrementing the free running timer counter. This bit can be written<br>in Freeze mode only.<br>0b - The free running timer is clocked by the CAN bit clock, which defines the baud rate on the<br>CAN bus.<br>1b - The free running timer is clocked by an external time tick. The period can be either adjusted<br>to be equal to the baud rate on the CAN bus, or a different value as required. See the device-<br>specific section for details about the external time tick.|
|14<br>PREXCEN|Protocol Exception Enable<br>This bit enables the protocol exception feature.<br>This field is writable only in Freeze mode.<br>See Protocol exception event in the CAN Protocol standard (ISO 11898-1:2015) for details.<br>~~NOTE~~|
||0b - Protocol exception is disabled.<br>1b - Protocol exception is enabled.|
|13<br>BTE|Bit Timing Expansion enable<br>This field enables the use of the EPRS, EDCBT and ENCBT registers to configure the CAN bit timing<br>segments, instead of using the bit timing fields of CBT, FDCBT, and CTRL1 registers.<br>If CTRL2[BTE] is set:<br>• PRESDIV, PROPSEG, PSEG1, PSEG2, and RJW fields in CTRL1 register are read as zero, and a<br>write operation in them has no effect.<br>• EPRESDIV, ERJW, EPROPSEG, EPSEG1, and EPSEG2 fields in the CBT register, and the FDCBT<br>register, are read as zero and a write operation to them has no effect.<br>• The ETDCOFF, ETDCEN, ETDCFAIL, and ETDCVAL fields of the ETDC register are used by<br>FlexCAN instead of TDCOFF, TDCEN, TDCFAIL, and TDCVAL fields in FDCTRL register, which are<br>read as zero, and a write operation in them has no effect.<br>• ETDC[TDMDIS] can be used for disabling transceiver delay measurement.<br>0b - CAN Bit timing expansion is disabled.<br>1b - CAN bit timing expansion is enabled.|
|12|ISO CAN FD Enable|
|ISOCANFDEN|This field enables the CAN FD protocol according to ISO specification (ISO 11898-1:2015) (seeCAN FD<br>ISO compliance).<br>This field is writable only in Freeze mode.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2814 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field|Function<br>FlexCAN is able to transmit FD frame format according to CAN Protocol standard<br>(ISO 11898-1:2015).<br>~~NOTE~~<br>0b - FlexCAN operates using the non-ISO CAN FD protocol.<br>1b - FlexCAN operates using the ISO CAN FD protocol (ISO 11898-1:2015).|
|---|---|
|11<br>EDFLTDIS|Edge Filter Disable<br>This bit disables the edge filter used during the bus integration state.<br>When the Edge Filter is enabled, two consecutive nominal time quanta with dominant bus state are required<br>to detect an edge that causes synchronization. When synchronization occurs, the counting of the sequence<br>of eleven consecutive recessive bits is restarted. The edge filter prevents the dominant pulses that are<br>shorter than a nominal bit time (present during the data phase of an FD frame) from being mistaken for an<br>idle condition.<br>This field is writable only in Freeze mode.<br>See Bus Integration state in the CAN Protocol standard (ISO 11898-1:2015) for details.<br>~~NOTE~~<br>0b - Edge filter is enabled<br>1b - Edge filter is disabled|
|10<br>—|Reserved|
|9-8<br>MBTSBASE|Message Buffer Time Stamp Base<br>This field selects which time base is used for capturing the 16-bit TIME_STAMP field of the message<br>buffer register.<br>There are three time base options:<br>1. TIMER<br>2. Lower 16 bits of high resolution time base<br>3. Upper 16 bits of high resolution time base<br>This field can be written in Freeze Mode only.<br>00b - Message buffer time stamp base is TIMER<br>01b - Message buffer time stamp base is lower 16 bits of high resolution timer<br>10b - Message buffer time stamp base is upper 16 bits of high resolution timer<br>11b - Reserved|
|7-6|Time Stamp Capture Point|
|TSTAMPCAP|This field configures the point in time when a 32-bit time base is captured during a CAN frame and stored<br>in the high resolution time stamp register (HR_TIME_STAMP).|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2815 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||For classical CAN frames, capture points can be the start of frame bit or the point in time a CAN frame is<br>considered valid, which is the 7th bit of end of frame for transmission and the 6th bit of the end of frame for<br>reception. For CAN FD frames, the high resolution time stamp can be captured at the start of frame, the point<br>in time a CAN FD frame is considered valid, or the res bit.<br>This field can be written in Freeze mode only.<br>00b - The high resolution time stamp capture is disabled<br>01b - The high resolution time stamp is captured in the end of the CAN frame<br>10b - The high resolution time stamp is captured in the start of the CAN frame<br>11b - The high resolution time stamp is captured in the start of frame for classical CAN frames<br>and in res bit for CAN FD frames|
|5-0<br>—|Reserved|



#### 72.6.2.15 Error and Status 2 Register (ESR2) 

##### Offset 

|Register|Offset|
|---|---|
|ESR2|38h|



##### Function 

This register reports some general status information. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||0||||||||LPTM||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|0|VPS|IMB|||||||0|||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2816 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Fields 

|Field<br>31-23<br>—|Function<br>Reserved|
|---|---|
|22-16<br>LPTM|Lowest Priority Tx Mailbox<br>If ESR2[VPS] is asserted, this field indicates the lowest number inactive mailbox (see the ESR2[IMB]<br>bit description). If there is no inactive mailbox then the mailbox indicated depends on the value of<br>CTRL1[LBUF]. If CTRL1[LBUF] is negated, then the mailbox indicated is the one that has the greatest<br>arbitration value (seeHighest-priority mailbox first). If CTRL1[LBUF] is asserted then the mailbox indicated<br>is the highest number active Tx mailbox. If a Tx mailbox is being transmitted it is not considered in LPTM<br>calculation. If ESR2[IMB] is not asserted and a frame is transmitted successfully, LPTM is updated with its<br>mailbox number.|
|15<br>—<br>14<br>VPS|Reserved<br>Valid Priority Status<br>This bit indicates whether ESR2[IMB] and ESR2[LPTM] contents are currently valid or not. It is asserted<br>upon every complete Tx arbitration process unless the CPU writes to Control and Status word of a mailbox<br>that has already been scanned, that is, it is behind Tx Arbitration Pointer, during the Tx arbitration process.<br>If there is no inactive mailbox and only one Tx mailbox that is being transmitted then VPS is not asserted.<br>This bit is negated upon the start of every Tx arbitration process or upon a write to Control and Status word<br>of any mailbox.<br>ESR2[VPS] is not affected by any CPU write into Control Status (C/S) of an MB that is<br>blocked by abort mechanism. When MCR[AEN] is asserted, the abort code write in C/S<br>of an MB that is being transmitted (pending abort), or any write attempt into a Tx MB with<br>IFLAG set is blocked.<br>~~NOTE~~<br>0b - Contents of IMB and LPTM are invalid.<br>1b - Contents of IMB and LPTM are valid.|
|13<br>IMB|Inactive Mailbox<br>If ESR2[VPS] is asserted, this bit indicates whether there is any inactive mailbox (CODE field is either 1000b<br>or 0b). This bit is asserted in the following cases:<br>• During arbitration, if an ESR2[LPTM] is found and it is inactive.<br>• If ESR2[IMB] is not asserted and a frame is transmitted successfully.<br>This bit is always cleared in start of arbitration (seeArbitration process).<br>ESR2[LPTM] mechanism has the following behavior: if an MB is successfully transmitted<br>and ESR2[IMB]=0 (no inactive mailbox), then ESR2[VPS] and ESR2[IMB] are asserted and<br>the index related to the MB just transmitted is loaded into ESR2[LPTM].<br>~~NOTE~~<br>0b - If ESR2[VPS] is asserted, the ESR2[LPTM] is not an inactive mailbox.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2817 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - If ESR2[VPS] is asserted, there is at least one inactive mailbox. LPTM content is the number<br>of the first one.|
|12-0<br>—|Reserved|



#### 72.6.2.16 CRC Register (CRCR) 

##### Offset 

|Register|Offset|
|---|---|
|CRCR|44h|



##### Function 

This register provides information about the CRC of transmitted messages for non-FD messages. This register only reports the 15 low order bits of CRC calculations for messages in CAN FD format that require either 17 or 21 bits. For CAN FD format frames, the FDCRC register must be used. This register is updated at the same time the Tx interrupt flag is asserted. 

~~<mark>NOTE</mark>~~ See CRC sequence calculation in the CAN Protocol standard (ISO 11898-1:2015) for details. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||0||||||||MBCRC||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|0||||||||TXCRC||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-23<br>—|Reserved|
|22-16|CRC Mailbox|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2818 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|MBCRC|This field indicates the number of the mailbox corresponding to the value in CRCR[TXCRC] field.|
|15|Reserved|
|—||
|14-0|Transmitted CRC value|
|TXCRC|This field indicates the CRC value of the last transmitted message for non-FD frames. For FD frames, CRC<br>value is reported in FDCRC register.|



#### 72.6.2.17 Legacy Rx FIFO Global Mask Register (RXFGMASK) 

##### Offset 

|Register|Offset|
|---|---|
|RXFGMASK|48h|



##### Function 

This register is located in RAM. 

If Legacy Rx FIFO is enabled, RXFGMASK is used to mask the Legacy Rx FIFO ID filter table elements that do not have a corresponding RXIMR according to CTRL2[RFFN] field setting. 

This register can only be written in Freeze mode as it is blocked by hardware in other modes. 

The following table shows how the FGM bits correspond to each IDAF field. 

Table 462. Correspondence of Legacy Rx FIFO global mask bits to IDF fields 

|LegacyRx FIFO<br>|||Identifier acc|eptance filter fields|||
|---|---|---|---|---|---|---|
|ID filter table|||||||
|elements format<br>(MCR[IDAM])|RTR|IDE|RXIDA|RXIDB<sup>1</sup>|RXIDC<sup>2</sup>|Reserved|
|A|FGM[31]|FGM[30]|FGM[29:1]|—|—|FGM[0]|
|B|FGM[31],<br>FGM[15]|FGM[30],<br>FGM[14]|—|FGM[29:16],<br>FGM[13:0]||—|
|C|—|—||—|FGM[31:24],<br>FGM[23:16],<br>FGM[15:8],<br>FGM[7:0]||



1. If MCR[IDAM] is equivalent to format B, only the fourteen most significant bits of the identifier of the incoming frame are compared with the Legacy Rx FIFO filter. 

2. If MCR[IDAM] is equivalent to format C, only the eight most significant bits of the identifier of the incoming frame are compared with the Legacy Rx FIFO filter. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2819 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2820-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>FGM<br>W<br>Reset u u u u u u u u u u u u u u u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>FGM<br>W<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Legacy Rx FIFO Global Mask Bits|
|FGM|These bits mask the ID filter table elements bits in a perfect alignment.|
||0b - The corresponding bit in the filter is "don’t care."|
||1b - The corresponding bit in the filter is checked.|



#### 72.6.2.18 Legacy Rx FIFO Information Register (RXFIR) 

##### Offset 

|Register|Offset|
|---|---|
|RXFIR|4Ch|



##### Function 

RXFIR provides information on Legacy Rx FIFO. 

This register is the port through which the CPU accesses the output of the Legacy RXFIR FIFO located in RAM. The Legacy RXFIR FIFO is written by the FlexCAN whenever a new message is moved into the Legacy Rx FIFO. Also, its output is updated whenever the output of the Legacy Rx FIFO is updated with the next message. See Legacy Rx FIFO for instructions on reading this register. 

~~<mark>NOTE</mark>~~ 

RXFIR can be written only during memory initialization, due to the error code correction (ECC) feature. In every other case the register is read-only. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2820 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||0||||||||IDHIT|||||
|W|||||||||||||||||
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|



##### Fields 

|Field|Function|
|---|---|
|31-9|Reserved|
|—||
|8-0|Identifier Acceptance Filter Hit Indicator|
|IDHIT|This field indicates which Identifier Acceptance filter was hit by the received message that is in the output<br>of the Legacy Rx FIFO. If multiple filters match the incoming message ID then the first matching IDAF<br>found (lowest number) by the matching process is indicated. This field is valid only when IFLAG1[BUF5I]<br>is asserted.|



#### 72.6.2.19 CAN Bit Timing Register (CBT) 

##### Offset 

|Register|Offset|
|---|---|
|CBT|50h|



##### Function 

This register is an alternative way to store the CAN bit timing variables described in CTRL1 register. EPRESDIV, EPROPSEG, EPSEG1, EPSEG2, and ERJW are extended versions of PRESDIV, PROPSEG, PSEG1, PSEG2, and RJW fields respectively. 

The BTF bit selects the use of the timing variables defined in this register. 

The contents of this register are not affected by soft reset. 

|~~NOTE~~|
|---|
|The CAN bit variables in CTRL1 and in CBT are stored in the same register.|
|~~NOTE~~|
|When the CAN FD feature is enabled (MCR[FDEN] is set), always set CBT[BTF].|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2821 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

~~<mark>NOTE</mark>~~ 

The user must ensure bit time settings and protocol engine tolerance are in compliance with the CAN Protocol standard (ISO 11898-1:2015). 

~~<mark>NOTE</mark>~~ 

If CTRL2[BTE] is set, EPRESDIV, ERJW, EPROPSEG, EPSEG1, and EPSEG2 fields are read as zero, and a write operation into them has no effect. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|BTF|||||EPRE|SDIV|||||||ERJW|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||EPRO|PSEG|||||EPSEG1|||||EPSEG2|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31<br>BTF|Bit Timing Format Enable<br>Enables the use of extended CAN bit timing fields EPRESDIV, EPROPSEG, EPSEG1, EPSEG2. and<br>ERJW replacing the CAN bit timing variables defined in CTRL1 register. This field can be written in<br>Freeze mode only.<br>0b - Extended bit time definitions disabled.<br>1b - Extended bit time definitions enabled.|
|30-21|Extended Prescaler Division Factor|
|EPRESDIV|This 10-bit field defines the ratio between the PE clock frequency and the serial clock (Sclock) frequency<br>when CBT[BTF] is asserted, otherwise it has no effect. It extends the CTRL1[PRESDIV] value range.<br>The Sclock period defines the time quantum of the CAN protocol. For the reset value, the Sclock frequency is<br>equal to the PE clock frequency (seeProtocol timing). This field can be written only in Freeze mode because<br>it is blocked by hardware in other modes.<br>Sclock frequency = PE clock frequency / (EPRESDIV + 1)|
|20-16<br>ERJW|Extended Resync Jump Width<br>This 5-bit field defines the maximum number of time quanta that a bit time can be changed by one<br>re-synchronization when CBT[BTF] bit is asserted, otherwise it has no effect. It extends the CTRL1[RJW]<br>value range.<br>One time quantum is equal to the Sclock period. This field can be written only in Freeze mode because it is<br>blocked by hardware in other modes.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2822 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||Resync Jump Width = ERJW + 1.|
|15-10<br>EPROPSEG|Extended Propagation Segment<br>This 6-bit field defines the length of the propagation segment in the bit time when CBT[BTF] bit is asserted,<br>otherwise it has no effect. It extends the CTRL1[PROPSEG] value range. This field can be written only in<br>Freeze mode because it is blocked by hardware in other modes.<br>Propagation Segment Time = (EPROPSEG + 1) × Time-Quanta.<br>Time-Quantum = one Sclock period.|
|9-5<br>EPSEG1|Extended Phase Segment 1<br>This 5-bit field defines the length of phase segment 1 in the bit time when CBT[BTF] bit is asserted,<br>otherwise it has no effect. It extends the CTRL1[PSEG1] value range. This field can be written only in Freeze<br>mode because it is blocked by hardware in other modes.<br>Phase Buffer Segment 1 = (EPSEG1 + 1) × Time-Quanta.<br>Time-Quantum = one Sclock period.|
|4-0<br>EPSEG2|Extended Phase Segment 2<br>This 5-bit field defines the length of phase segment 2 in the bit time when CBT[BTF] bit is asserted,<br>otherwise it has no effect. It extends the CTRL1[PSEG2] value range. This field can be written only in Freeze<br>mode because it is blocked by hardware in other modes.<br>Phase Buffer Segment 1 = (EPSEG2 + 1) × Time-Quanta.<br>Time-Quantum = one Sclock period.|



#### 72.6.2.20 Interrupt Masks 3 Register (IMASK3) 

##### Offset 

|Register|Offset|
|---|---|
|IMASK3|6Ch|



##### Function 

This register allows any number of a range of the 32 message buffer interrupts to be enabled or disabled for MB95 to MB64. It contains one interrupt mask bit per buffer, enabling the CPU to determine which buffer generates an interrupt after a successful transmission or reception, that is, when the corresponding IFLAG3 bit is set. 

~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2823 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

||Instance|Register supported|Register not supported|
|---|---|---|---|
|CAN_0||IMASK3|—|
|CAN_1||IMASK3|—|
|CAN_2||IMASK3|—|
|CAN_3||—|IMASK3|
|CAN_4||—|IMASK3|
|CAN_5||—|IMASK3|
|CAN_6||—|IMASK3|
|CAN_7||—|IMASK3|



|Diagram|||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|R<br>W||||||||BUF95|TO64M||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||BUF95|TO64M||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Fields|||||||||||||||||



|Field|Function|
|---|---|
|31-0|Buffer MBi Mask|
|BUF95TO64M|Each bit enables or disables the corresponding FlexCAN message buffer interrupt for MB95 to MB64. When<br>CAN FD is enabled, the MB range is defined in accordance with the MBDSRs bit fields of FDCTRL register.|
||Setting or clearing a bit in the IMASK3 Register can assert or negate an interrupt request,<br>if the corresponding IFLAG3 bit is set.<br>~~NOTE~~|
||0b - The corresponding buffer interrupt is disabled.|
||1b - The corresponding buffer interrupt is enabled.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2824 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

#### 72.6.2.21 Interrupt Flags 3 Register (IFLAG3) 

##### Offset 

|Register|Offset|
|---|---|
|IFLAG3|74h|



##### Function 

This register defines the flags for the 32 message buffer interrupts for MB95 to MB64. It contains one interrupt flag bit per buffer. Each successful transmission or reception sets the corresponding IFLAG3 bit. If the corresponding IMASK3 bit is set, an interrupt will be generated. The interrupt flag must be cleared by writing 1 to it. Writing 0 has no effect. 

Before updating MCR[MAXMB] field, CPU must service the IFLAG3 bits whose MB value is greater than the MAXMB to be updated; otherwise, they will remain set and be inconsistent with the number of MBs available. 

~~<mark>NOTE</mark>~~ Each module instance supports a different number of registers. 

|||Insta|nce||||Regis|ter sup|ported|||Re|gister n|ot sup|ported||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|CAN_0||||||IFLAG3|||||—||||||
|CAN_1||||||IFLAG3|||||—||||||
|CAN_2||||||IFLAG3|||||—||||||
|CAN_3||||||—|||||IFLAG|3|||||
|CAN_4||||||—|||||IFLAG|3|||||
|CAN_5||||||—|||||IFLAG|3|||||
|CAN_6||||||—|||||IFLAG|3|||||
|CAN_7||||||—|||||IFLAG|3|||||
|Diagram<br>Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|R||||||||BUF9|5TO64||||||||
|W||||||||W|1C||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||BUF9|5TO64||||||||
|W||||||||W|1C||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Diagram 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2825 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Fields 

|Field|Function|
|---|---|
|31-0|Buffer MBi Interrupt|
|BUF95TO64|Each bit flags the corresponding FlexCAN message buffer interrupt for MB95 to MB64.When CAN FD is<br>enabled, the MB range is defined in accordance to the MBDSRs bit fields of FDCTRL register.|
||0b - The corresponding buffer has no occurrence of successfully completed transmission or<br>reception.|
||1b - The corresponding buffer has successfully completed transmission or reception.|



#### 72.6.2.22 Rx Individual Mask Registers (RXIMR0 - RXIMR95) 

##### Offset 

For n = 0 to 95: 

|Register<br>RXIMRn|Offset<br>880h + (n × 4h)|
|---|---|



##### Function 

The RX Individual Mask registers are used to store the acceptance masks for ID filtering in Rx MBs and the Legacy Rx FIFO. 

When the Legacy Rx FIFO is disabled (MCR[RFEN] bit is negated), an individual mask is provided for each available Rx mailbox on a one-to-one correspondence. When the Legacy Rx FIFO is enabled (MCR[RFEN] bit is asserted), an individual mask is provided for each Legacy Rx FIFO ID filter table element on a one-to-one correspondence depending on the setting of CTRL2[RFFN] (see Legacy Rx FIFO). 

RXIMR0 stores the individual mask associated with either MB0 or ID filter table element 0, RXIMR1 stores the individual mask associated with either MB1 or ID filter table element 1, and so on. 

RXIMR registers can only be accessed by the CPU when the module is in Freeze mode; otherwise, they are blocked by hardware. These registers are not affected by reset. They are located in RAM and must be explicitly initialized prior to any reception. 

It is possible for the RXIMR memory region to be accessed as general purpose memory. See Bus interface for more information. 

~~<mark>NOTE</mark>~~ Each module instance supports a different number of registers. 

||Instance|Register supported|Register not supported|
|---|---|---|---|
|CAN_0||RXIMR0–RXIMR95|—|
|CAN_1||RXIMR0–RXIMR95|—|
|CAN_2||RXIMR0–RXIMR95|—|
|CAN_3||RXIMR0–RXIMR63|RXIMR64–RXIMR95|
|CAN_4||RXIMR0–RXIMR63|RXIMR64–RXIMR95|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2826 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

||Instance|Register supported|Register not supported|
|---|---|---|---|
|CAN_5||RXIMR0–RXIMR63|RXIMR64–RXIMR95|
|CAN_6||RXIMR0–RXIMR63|RXIMR64–RXIMR95|
|CAN_7||RXIMR0–RXIMR63|RXIMR64–RXIMR95|



##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2827-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>MI<br>W<br>Reset See Register reset values.<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>MI<br>W<br>Reset See Register reset values.<br><!-- End of picture text -->

##### Register reset values 

|Register|Reset value|
|---|---|
|RXIMR0–RXIMR63|CAN_0–CAN_7: undefined|
|RXIMR64–RXIMR95|CAN_0–CAN_2: undefined|
||CAN_3–CAN_7: Register not supported|



##### Fields 

|Field|Function|
|---|---|
|31-0|Individual Mask Bits|
|MI|Each individual mask bit masks the corresponding bit in both the mailbox filter and Legacy Rx FIFO ID filter<br>table element in distinct ways.|
||For mailbox filters, see the RXMGMASK register description.|
||For Legacy Rx FIFO ID filter table elements, see the RXFGMASK register description.|
||0b - The corresponding bit in the filter is "don't care."|
||1b - The corresponding bit in the filter is checked.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2827 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

#### 72.6.2.23 Memory Error Control Register (MECR) 

##### Offset 

|Register|Offset|
|---|---|
|MECR|AE0h|



##### Function 

This register contains control bits for memory error detection and correction (ECC). 

~~<mark>NOTE</mark>~~ When bit CTRL2[ECRWRE] is 0, writes in this register are blocked, except in the ECRWRDIS bit. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|ECRW||||||0||||||HANC|FANC|0|CEI_|
|W|RDIS||||||||||||EI_...|EI_...||MSK|
|Reset|1|0|0|0|0|0|0|0|0|0|0|0|1|1|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|HAER|FAER|EXTE||0||RERR|ECCDI|NCEF||||0||||
|W|RIE|RIE|RRIE||||DIS|S|AFRZ||||||||
|Reset|0|0|0|0|0|0|0|0|1|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|Error Configuration Register Write Disable|
|ECRWRDIS|Disables writes on this register.|
||This bit is automatically set to 1 (disabled) when CTRL2[ECRWRE] is enabled. The protocol described in<br>sectionDetection and correction of memory errorsmust be followed.<br>0b - Write is enabled.<br>1b - Write is disabled.|
|30-20|Reserved|
|—||
|19|Host Access With Non-Correctable Errors Interrupt Mask|
|HANCEI_MSK|Enables the interrupt in case of non-correctable errors detected in memory reads issued by the host (CPU).<br>0b - Interrupt is disabled.|
||1b - Interrupt is enabled.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2828 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>FANCEI_MSK|FlexCAN Access With Non-Correctable Errors Interrupt Mask<br>Enables the interrupt in case of non-correctable errors detected in memory reads issued by the FlexCAN<br>internal processes.<br>0b - Interrupt is disabled.<br>1b - Interrupt is enabled.|
|17<br>—|Reserved|
|16<br>CEI_MSK|Correctable Errors Interrupt Mask<br>Enables the interrupt in case of correctable errors detected in memory reads issued by the host or FlexCAN<br>internal processes.<br>0b - Interrupt is disabled.<br>1b - Interrupt is enabled.|
|15<br>HAERRIE|Host Access Error Injection Enable<br>Enables the injection of errors only in memory reads issued by the host (CPU).<br>0b - Injection is disabled.<br>1b - Injection is enabled.|
|14<br>FAERRIE|FlexCAN Access Error Injection Enable<br>Enables the injection of errors only in memory reads issued by the FlexCAN internal processes.<br>0b - Injection is disabled.<br>1b - Injection is enabled.|
|13<br>EXTERRIE|Extended Error Injection Enable<br>Memory accesses performed by internal FlexCAN processes are 64-bit. This bit extends the error injection<br>on 32-bit memory accesses to the complementary 32-bit word using the same 32-bit error injection data<br>and parity words. SeeError Injection Data Pattern Register (ERRIDPR)andError Injection Parity Pattern<br>Register (ERRIPPR).<br>0b - Error injection is applied only to the 32-bit word.<br>1b - Error injection is applied to the 64-bit word.|
|12-10<br>—|Reserved|
|9<br>RERRDIS|Error Report Disable<br>Disables the update of the error report registers. The update of error-related flags and the generation of bus<br>transfer errors are still active.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2829 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||When reading the report registers, this bit must be set to assure coherence on the<br>consecutive register reads.<br>~~NOTE~~<br>0b - Enable updates of the error report registers.<br>1b - Disable updates of the error report registers.|
|8<br>ECCDIS|Error Correction Disable<br>Disables completely the memory detection and correction mechanism. Besides disabling the error report<br>mechanism, it also stops the update of the error-related flags and generation of bus transfer errors. The<br>parity bits continue being calculated and written into memory on write transactions.<br>0b - Enable memory error correction.<br>1b - Disable memory error correction.|
|7<br>NCEFAFRZ|Non-Correctable Errors In FlexCAN Access Put Device In Freeze Mode<br>Determines the response when a non-correctable error is detected in a memory read performed by FlexCAN<br>internal processes. In this case, entering Freeze mode prevents corrupted data from being treated as valid<br>by FlexCAN internal processes.<br>0b - Keep normal operation.<br>1b - Put FlexCAN in Freeze mode (see section "Freeze mode").|
|6-0<br>—|Reserved|



#### 72.6.2.24 Error Injection Address Register (ERRIAR) 

##### Offset 

|Register|Offset|
|---|---|
|ERRIAR|AE4h|



##### Function 

This register holds the address where error is to be injected. 

Use the following table to convert from the memory map address to the location in the physical FlexCAN RAM (where pairs of values are provided, the first is the address for MCR[FDEN] negated, the second is for MCR[FDEN] asserted): 

Table 463. Error injection address for Classical CAN format 

|RAM contents<br>FlexCAN registers|Injection address<br>Not mapped|Memory map<br>—|
|---|---|---|



##### Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2830 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table 463. Error injection address for Classical CAN format (continued) 

|RAM contents|Injection address|Memory map|
|---|---|---|
|MBs|0000h|0080h|
|RXIMRs|600h|0880h|
|RXFIR_0|780h|0A80h|
|RXFIR_1|784h|0A84h|
|RXFIR_2|788h|0A88h|
|RXFIR_3|78Ch|0A8Ch|
|RXFIR_4|790h|0A90h|
|RXFIR_5|794h|0A94h|
|Reserved|—|0A98h|
|RXMGMASK|7A0h|0AA0h|
|RXFGMASK|7A4h|0AA4h|
|RX14MASK|7A8h|0AA8h|
|RX15MASK|7ACh|0AACh|
|Tx_SMB|7B0h|0AB0h / 0F28h|
|Rx_SMB0|7C0h / 7F8h|0AC0h / 0F70h|
|Rx_SMB1|7D0h / 840h|0AD0h / 0FB8h|
|Rx_SMB0_TIME_STAMP|888h|0C20h|
|Rx_SMB1_TIME_STAMP|88Ch|0C24h|
|HR_TIME_STAMP|890h|0C30h|
|Enhanced RX FIFO|A10h|2000h|
|ERFFEL|1050h|3000h|



~~<mark>NOTE</mark>~~ 

For RXFIR, Enhanced RX FIFO, and HR_TIME_STAMP addresses, you must inject ECC errors in host access only. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2831-07.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 INJADDR_L<br>INJADDR_H<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2831 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Fields 

|Field|Function|
|---|---|
|31-14|Reserved|
|—||
|13-2|Error Injection Address High|
|INJADDR_H|This read-write field defines the twelve most significant bits of the physical RAM address where error is<br>to be injected (see table above).|
|1-0|Error Injection Address Low|
|INJADDR_L|This read-only field defines the two least significant bits of the physical RAM address where error is to be<br>injected. They ensure that the address is on a thirty-two-bit boundary.|



#### 72.6.2.25 Error Injection Data Pattern Register (ERRIDPR) 

##### Offset 

|Register|Offset|
|---|---|
|ERRIDPR|AE8h|



##### Function 

Holds the error pattern to be injected in the data word read from memory. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||DF|LIP||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||DF|LIP||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-0|Data flip pattern|
|DFLIP|Bits set to 1 in the flip pattern cause the corresponding data bit in the word read from memory to invert.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2832 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

#### 72.6.2.26 Error Injection Parity Pattern Register (ERRIPPR) 

##### Offset 

|Register|Offset|
|---|---|
|ERRIPPR|AECh|



##### Function 

Holds the error pattern to be injected in parity bits read from memory along with data word. 

Bits set to 1 in the flip pattern cause the corresponding parity bit in the word read from memory to invert. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2833-09.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0<br>PFLIP3  PFLIP2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>PFLIP1  PFLIP0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-29<br>—|Reserved|
|28-24<br>PFLIP3|Parity Flip Pattern For Byte 3 (most significant)|
|23-21<br>—|Reserved|
|20-16|Parity Flip Pattern For Byte 2|
|PFLIP2||
|15-13<br>—|Reserved|
|12-8|Parity Flip Pattern For Byte 1|
|PFLIP1||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2833 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|7-5<br>—|Reserved|
|4-0|Parity Flip Pattern For Byte 0 (Least Significant)|
|PFLIP0||



#### 72.6.2.27 Error Report Address Register (RERRAR) 

##### Offset 

|Register|Offset|
|---|---|
|RERRAR|AF0h|



##### Function 

Reports the address used for an access in which an error (correctable or non-correctable) was detected, and also reports the identification of the source of that access. 

This address is always reported using a 32-bit alignment. Non-aligned accesses (ERRADDR[1:0] non-0) are reported with the address aligned and data is reported in RERRDR accordingly shifted. In case of errors detected in accesses larger than 32-bit (as performed by FlexCAN internal processes), the address of the 32-bit word which the error was detected is reported. In case of errors detected in more than one 32-bit word, only the least significant address is reported. 

Table 464. Source of memory access 

|SAID[2:0]|Error during...|
|---|---|
|0|Move-out FlexCAN access|
|1|Move-in|
|2|Tx Arbitration|
|3|Rx Matching|
|4|Move-out Host access|
|5-7|Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2834 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||0||||NCE|||0||||SAID||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|0||||||||ERRA|DDR|||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-25<br>—|Reserved|
|24<br>NCE|Non-Correctable Error<br>Indicates that the report is due to a non-correctable error.<br>0b - Reporting a correctable error<br>1b - Reporting a non-correctable error|
|23-19<br>—|Reserved|
|18-16<br>SAID|SAID<br>SAID[2] — Identification of the requester of the memory read request:<br>• 0 = Requested by FlexCAN internal processes<br>• 1 = Requested by host (CPU)<br>SAID[1] — Details of FlexCAN operation:<br>• 0 = Move<br>• 1 = Scanning<br>SAID[0] — Operation that requested the memory read:<br>• 0 = Transmission<br>• 1 = Reception<br>For more information seeTable 464.|
|15-14<br>—|Reserved|
|13-0|Address Where Error Detected|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2835 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|ERRADDR|See the description of the Error Injection Address Register (ERRIAR).|



#### 72.6.2.28 Error Report Data Register (RERRDR) 

##### Offset 

|Register|Offset|
|---|---|
|RERRDR|AF4h|



##### Function 

Reports the raw data (unmodified by the correction performed by ECC logic) read from memory with error. The value reported does not represent the transient values of the BUSY bit (see Table 469) when reading a message buffer. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2836-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RDATA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RDATA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Raw data word read from memory with error|
|RDATA||



#### 72.6.2.29 Error Report Syndrome Register (RERRSYNR) 

##### Offset 

|Register|Offset|
|---|---|
|RERRSYNR|AF8h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2836 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Function 

Holds the syndrome detected in a memory read with error. It also reports the bytes which were read in this 32-bit read transaction. Each SYNDn field indicates the type of error and which bit in byte (n) is affected by the error. (SYND3 corresponds to the most significant byte in the data word read from memory; SYND0 corresponds to the least significant.) 

Table 465. Syndrome definition 

|SYNDn (hex)|Type|Bit affected|
|---|---|---|
|00|—|none (no error)|
|01|Code|0|
|02|Code|1|
|04|Code|2|
|07|Data|5|
|08|Code|3|
|0E|Data|7|
|10|Code|4|
|13|Data|2|
|15|Data|6|
|16|Data|1|
|19|Data|3|
|1A|Data|4|
|1C|Data|0|
|06|—|All-zeros non-correctable error|
|1F|—|All-ones non-correctable error|
|All others|—|Non-correctable error|



Each BEn field indicates which byte in the 32-bit word reported was effectively read. The syndrome bits are calculated for all bytes, even for the non-read ones. Errors detected in non-read bytes are indicated (see Error indication) and reported (see Error reporting). 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2837-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R BE3  0 SYND3  BE2  0 SYND2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R BE1  0 SYND1  BE0  0 SYND0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2837 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Fields 

|Field|Function|
|---|---|
|31<br>BE3|Byte Enabled For Byte 3 (most significant)<br>0b - The byte was not read.<br>1b - The byte was read.|
|30-29<br>—|Reserved|
|28-24|Error Syndrome For Byte 3 (most significant)|
|SYND3|SeeTable 465.|
|23<br>BE2|Byte Enabled For Byte 2<br>0b - The byte was not read.<br>1b - The byte was read.|
|22-21<br>—|Reserved|
|20-16<br>SYND2|Error Syndrome For Byte 2<br>SeeTable 465.|
|15<br>BE1|Byte Enabled For Byte 1<br>0b - The byte was not read.<br>1b - The byte was read.|
|14-13<br>—|Reserved|
|12-8|Error Syndrome for Byte 1|
|SYND1|SeeTable 465.|
|7<br>BE0|Byte Enabled For Byte 0 (least significant)<br>0b - The byte was not read.<br>1b - The byte was read.|
|6-5<br>—|Reserved|
|4-0|Error Syndrome For Byte 0 (least significant)|
|SYND0|SeeTable 465.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2838 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

#### 72.6.2.30 Error Status Register (ERRSR) 

##### Offset 

|Register|Offset|
|---|---|
|ERRSR|AFCh|



##### Function 

Holds the status bits of the error correction and detection operations. These flags can be cleared by writing 1 to them. Writing 0 has no effect. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||0|||||||HANC<br>EIF|FANC<br>EIF|0|CEIF|
|W|||||||||||||W1C|W1C||W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||0|||||||HANC<br>EIOF|FANC<br>EIOF|0|CEIOF|
|W|||||||||||||W1C|W1C||W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-20|Reserved|
|—||
|19|Host Access With Non-Correctable Error Interrupt Flag|
|HANCEIF|Indicates that a non-correctable error was detected in a memory read initiated by host. A bus transfer error<br>is asserted for that access. If MECR[HANCEI_MSK] is set, the interrupt is asserted.<br>0b - No non-correctable errors were detected in host accesses so far.<br>1b - A non-correctable error was detected in a host access.|
|18|FlexCAN Access With Non-Correctable Error Interrupt Flag|
|FANCEIF|Indicates that a non-correctable error was detected in a memory read initiated by FlexCAN internal<br>processes. If MECR[FANCEI_MSK] is set, the interrupt is asserted.<br>0b - No non-correctable errors were detected in FlexCAN accesses so far.<br>1b - A non-correctable error was detected in a FlexCAN access.|
|17|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2839 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|16<br>CEIF|Correctable Error Interrupt Flag<br>Indicates that a correctable error was detected in a memory read. If MECR[CEI_MSK] is set, the interrupt<br>is asserted.<br>0b - No correctable errors were detected so far.<br>1b - A correctable error was detected.|
|15-4<br>—<br>3<br>HANCEIOF|Reserved<br>Host Access With Non-Correctable Error Interrupt Overrun Flag<br>Indicates that a non-correctable error was detected in a memory read initiated by host when HANCEIF was<br>set. No interrupt is associated with this flag. SeeError indication.<br>0b - No overrun on non-correctable errors in host access<br>1b - Overrun on non-correctable errors in host access|
|2<br>FANCEIOF|FlexCAN Access With Non-Correctable Error Interrupt Overrun Flag<br>Indicates that a non-correctable error was detected in a memory read initiated by FlexCAN internal<br>processes when FANCEIF was set. No interrupt is associated to this flag. SeeError indication.<br>0b - No overrun on non-correctable errors in FlexCAN access<br>1b - Overrun on non-correctable errors in FlexCAN access|
|1<br>—<br>0<br>CEIOF|Reserved<br>Correctable Error Interrupt Overrun Flag<br>Indicates that a correctable error was detected in a memory read when CEIF was set. No interrupt is<br>associated to this flag. SeeError indication.<br>0b - No overrun on correctable errors<br>1b - Overrun on correctable errors|



#### 72.6.2.31 Enhanced CAN Bit Timing Prescalers (EPRS) 

##### Offset 

|Register|Offset|
|---|---|
|EPRS|BF0h|



##### Function 

This register defines the CAN bit timing prescalers for the nominal phase and data phase when CTRL2[BTE] is set. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2840 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

This register is used by the hardware only if CTRL2[BTE] is set; otherwise a write operation has no effect and all fields are read as zero. 

This register can be written only in Freeze mode because it is blocked by hardware in other modes. 

The contents of this register are not affected by soft reset. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||Rese|rved|||||||EDPR|ESDIV|||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||Rese|rved|||||||ENPR|ESDIV|||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-26<br>—|Reserved|
|25-16|Extended Data Phase Prescaler Division Factor|
|EDPRESDIV|This field defines the ratio between the PE clock frequency and the serial clock (Sclock) frequency in the<br>data phase of a CAN FD message when CTRL2[BTE] is set.<br>The Sclock period defines the time quantum of the CAN FD protocol for the data bit rate.<br>Sclock frequency = PE clock frequency / (EDPRESDIV + 1).<br>To minimize errors when processing FD frames, use the same value for ENPRESDIV and<br>EDPRESDIV. For more details see the first NOTE in sectionCAN FD frames.<br>~~NOTE~~|
|15-10<br>—|Reserved|
|9-0|Extended Nominal Prescaler Division Factor|
|ENPRESDIV|This field defines the ratio between the PE clock frequency and the serial clock (Sclock) frequency when<br>CTRL2[BTE] is set; otherwise it reads as zero and a write operation has no effect.<br>The Sclock period defines the time quantum of the CAN protocol in the nominal phase. For the reset value,<br>the Sclock frequency is equal to the PE clock frequency (seeProtocol timing).<br>Sclock frequency = PE clock frequency / (ENPRESDIV + 1)|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2841 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

#### 72.6.2.32 Enhanced Nominal CAN Bit Timing (ENCBT) 

##### Offset 

|Register|Offset|
|---|---|
|ENCBT|BF4h|



##### Function 

This register provides an alternative way to store the CAN bit timing variables described in the CTRL1 and CBT registers, to get higher CAN bit timing resolution. 

This register is used by the hardware only if CTRL2[BTE] is set; otherwise a write operation has no effect and all fields are read as zero. 

The contents of this register are not affected by soft reset. 

This register can be written only in Freeze mode because it is blocked by hardware in other modes. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2842-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved  NRJW  Reserved  NTSEG2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>NTSEG2  Reserved  NTSEG1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-29|Reserved|
|—||
|28-22|Nominal Resynchronization Jump Width|
|NRJW|This field defines the maximum number of time quanta that a nominal bit time can be changed by one<br>resynchronization when CTRL2[BTE] bit is asserted; otherwise it has no effect.<br>One time quantum is equal to the Sclock period.<br>Nominal Resync Jump Width = NRJW + 1.|
|21-19|Reserved|
|—||
|18-12|Nominal Time Segment 2|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2842 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|NTSEG2|This field defines the length of Time Segment 2 in the nominal bit time when CTRL2[BTE] is set; otherwise<br>it has no effect.<br>Nominal Time Segment 2 = (NTSEG2 + 1) × Time-Quanta.<br>Time-Quantum = one Sclock period.|
|11-8<br>—<br>7-0|Reserved<br>Nominal Time Segment 1|
|NTSEG1|This field defines the length of Time Segment 1 in the bit time when CTRL2[BTE] is set; otherwise it has<br>no effect.<br>Nominal Time Segment 1 = (NTSEG1 + 1) × Time-Quanta.<br>Time-Quantum = one Sclock period.|



#### 72.6.2.33 Enhanced Data Phase CAN bit Timing (EDCBT) 

##### Offset 

|Register|Offset|
|---|---|
|EDCBT|BF8h|



##### Function 

This register provides an alternative way to store the data phase CAN bit timing variables described in the FDCBT register to achieve higher CAN bit timing resolution. 

This register is used by the hardware only if CTRL2[BTE] is set; otherwise a write operation has no effect and all fields are read as zero. 

The contents of this register are not affected by soft reset. 

This register can be written only in Freeze mode because it is blocked by hardware in other modes. 

~~<mark>NOTE</mark>~~ 

The user must ensure bit time settings and protocol engine tolerance are in compliance with the CAN Protocol standard (ISO 11898-1:2015). 

~~<mark>NOTE</mark>~~ 

DTSEG1 must be at least two time quanta. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2843 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||Rese|rved||||DRJ|W||||Rese|rved|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||DTS|EG2|||||Reserved||||||DTSEG1|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-26|Reserved|
|—||
|25-22<br>DRJW|Data Phase Resynchronization Jump Width<br>This field defines the maximum number of time quanta that a data phase bit time can be changed by one<br>resynchronization when CTRL2[BTE] is set; otherwise it has no effect.<br>Data Phase Resync Jump Width = DRJW + 1.|
|21-16<br>—<br>15-12<br>DTSEG2|Reserved<br>Data Phase Time Segment 2<br>This field defines the length of time segment 2 in the data phase bit time when CTRL2[BTE] is set; otherwise<br>it has no effect.<br>Data Phase Time Segment 2 = (DTSEG2 + 1) x Time-Quanta.<br>Time-Quantum = one Sclock period.|
|11-5<br>—|Reserved|
|4-0<br>DTSEG1|Data Phase Segment 1<br>This field defines the length of time segment 1 in the data phase bit time when CTRL2[BTE] is set; otherwise<br>it has no effect.<br>Data Phase Time Segment 1 = (NTSEG1 + 1) x Time-Quanta.<br>Time-Quantum = one Sclock period.|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2844 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

#### 72.6.2.34 Enhanced Transceiver Delay Compensation (ETDC) 

##### Offset 

|Register|Offset|
|---|---|
|ETDC|BFCh|



##### Function 

This register contains extended versions of the fields FDCTRL[TDCOFF] and FDCTRL[TDCVAL]. This register is used by the hardware only if CTRL2[BTE] is set; otherwise, a write operation has no effect and all fields are read as zero. 

~~<mark>NOTE</mark>~~ See Transmitter delay compensation in the CAN Protocol standard (ISO 11898-1:2015) for details. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2845-09.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R ETDC TDMDI<br>Reserved  ETDCOFF<br>W EN  S<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>ETDC<br>R ETDCVAL<br>FAIL<br>Reserved<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Transceiver Delay Compensation Enable|
|ETDCEN|This bit can be used for enabling and disabling the TDC feature. It can be written in Freeze mode only.|
||Refer to Transmitter delay compensation in the CAN Protocol standard (ISO 11898-1:2015)<br>for details.<br>~~NOTE~~|
||TDC must be disabled when the Loop Back Mode is enabled (see CTRL1[LPB] register).<br>~~NOTE~~|
||0b - TDC is disabled|
||1b - TDC is enabled|
|30|Transceiver Delay Measurement Disable|
|TDMDIS||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2845 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field|Function<br>This bit can be used for disabling the transceiver delay measurement. When the TDC measurement is<br>disabled, the secondary sample point position is determined only by the enhanced TDC offset (ETDCOFF)<br>field. Otherwise, if the TCD measurement is enabled, then the secondary sample point position is<br>determined by the sum of the transceiver delay measurement plus the enhanced TDC offset.<br>This field is not affected by soft reset.<br>This bit can be enabled only if CTRL2[BTE] is set.<br>~~NOTE~~<br>0b - TDC measurement is enabled<br>1b - TDC measurement is disabled|
|---|---|
|29-23<br>—|Reserved|
|22-16<br>ETDCOFF|Enhanced Transceiver Delay Compensation Offset<br>This field contains the offset value to be added to the measured transceiver's loop delay in order to define<br>the position of the delayed comparison point when bit rate switching is active. SeeTransceiver delay<br>compensationfor more details on how the loop delay measurement is performed.<br>ETDCOFF can be written in Freeze mode only. Its value can be defined in protocol engine (PE) clock<br>periods (CANCLK, seeProtocol timingfor more details), and must be selected to be smaller than the CAN<br>bit duration in the data bit rate for proper operation.<br>ETDCOFF must not be configured as zero.<br>~~NOTE~~<br>If CTRL2[BTE] is set after a chip level hard reset, ETCDOFF is read as 1h.<br>~~NOTE~~|
|15<br>ETDCFAIL|Transceiver Delay Compensation Fail<br>This bit indicates when the Transceiver Delay Compensation (TDC) mechanism is out of range, unable<br>to compensate the transceiver's loop delay and successfully compare the delayed received bits to the<br>transmitted ones (seeTransceiver delay compensation). ETDCFAIL sets in the first time FlexCAN detects<br>the out of range condition. The CPU needs to write 1 to clear it.<br>0b - Measured loop delay is in range.<br>1b - Measured loop delay is out of range.|
|14-8<br>—|Reserved|
|7-0<br>ETDCVAL|Enhanced Transceiver Delay Compensation Value<br>This register contains the ETDCOFF field added to the measured value of the transceiver loop delay in the<br>latest transmitted CAN FD frame, with BRS equal to recessive.<br>This field is only updated by the hardware if ETDC[ETDCEN] is set.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2846 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table continued from the previous page... 

Field Function This field is affected by soft reset. ~~<mark>NOTE</mark>~~ If TDMDIS is set, ETDCVAL stores ETDCOFF only. 

#### 72.6.2.35 CAN FD Control Register (FDCTRL) 

##### Offset 

|Register|Offset|
|---|---|
|FDCTRL|C00h|



##### Function 

This register contains control bits for the CAN FD operation. It also defines the data size of message buffers allocated in different partitions of RAM (memory blocks) as described in the table below. 

When an 8-byte payload is selected: 

- Block R0 allocates MB0 to MB31. 

- Block R1 allocates MB32 to MB63. 

- Block R2 allocates MB64 to MB95. 

When a payload larger than 8 bytes is selected, the maximum number of MBs in a block is limited as described below: 

Table 466. Number of message buffers 

|Payload size|Maximum number of message buffers per RAM block|
|---|---|
|8 bytes|32|
|16 bytes|21|
|32 bytes|12|
|64 bytes|7|



~~<mark>NOTE</mark>~~ 

One memory block fits exactly 32 MBs with an 8-byte payload. For other possible payload sizes, empty memory may exist between the last MB in a block and the beginning of the next block. This empty memory corresponds to less than one MB, and must not be used. 

The contents of this register are not affected by soft reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2847 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2848-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R FDRA Reserv Reserv Reserv<br>Reserved  Reserved  MBDSR2  MBDSR1  MBDSR0<br>W TE  ed  ed  ed<br>Reset 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>TDCF<br>R TDCVAL<br>TDCE AIL  Reserv TDCOFF  Reserved<br>N  ed<br>W W1C<br>Reset 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Bit Rate Switch Enable|
|FDRATE|This bit enables the effect of the Bit Rate Switch (BRS bit) during the data phase of Tx messages.<br>The CPU can write this bit any time. However, its effect turns active only when the CAN bus is in Wait for<br>Bus Idle, Bus Idle, or Bus Off state, or when the current frame under reception or transmission reaches the<br>interframe space.<br>By negating FDCTRL[FDRATE], the CPU can force all bits in CAN FD messages to be transmitted in<br>nominal bit rate, no matter what the value is in the BRS bit of the Tx MBs.<br>0b - Transmit a frame in nominal rate. The BRS bit in the Tx MB has no effect.<br>1b - Transmit a frame with bit rate switching if the BRS bit in the Tx MB is recessive.|
|30-27<br>—<br>26-25<br>—|Reserved<br>Reserved|
|24<br>—<br>23-22<br>MBDSR2|Reserved<br>Message Buffer Data Size for Region 2<br>This two-bit field selects the data size (8, 16, 32, or 64 bytes) for region R2 of message buffers allocated<br>in RAM.<br>It can be written in Freeze mode only.<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>~~NOTE~~|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2848 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field|Function||
|---|---|---|
||Instance<br>Field supported in|Field not supported in|
||CAN_0<br>FDCTRL|—|
||CAN_1<br>FDCTRL|—|
||CAN_2<br>FDCTRL|—|
||CAN_3<br>—|FDCTRL|
||CAN_4<br>—|FDCTRL|
||CAN_5<br>—|FDCTRL|
||CAN_6<br>—|FDCTRL|
||CAN_7<br>—|FDCTRL|
||00b - Selects 8 bytes per message buffer.<br>01b - Selects 16 bytes per message buffer.<br>10b - Selects 32 bytes per message buffer.<br>11b - Selects 64 bytes per message buffer.||
|21<br>—|Reserved||
|20-19<br>MBDSR1|Message Buffer Data Size for Region 1<br>This two-bit field selects the data size (8, 16, 32, or 64 bytes) for re<br>in RAM.<br>It can be written in Freeze mode only.<br>00b - Selects 8 bytes per message buffer.<br>01b - Selects 16 bytes per message buffer.<br>10b - Selects 32 bytes per message buffer.<br>11b - Selects 64 bytes per message buffer.|gion R1 of message buffers allocated|
|18<br>—|Reserved||
|17-16<br>MBDSR0|Message Buffer Data Size for Region 0<br>This two-bit field selects the data size (8, 16, 32, or 64 bytes) for re<br>in RAM.<br>It can be written in Freeze mode only.<br>Table continues on the next page...|gion R0 of message buffers allocated|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2849 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||00b - Selects 8 bytes per message buffer.<br>01b - Selects 16 bytes per message buffer.<br>10b - Selects 32 bytes per message buffer.<br>11b - Selects 64 bytes per message buffer.|
|15<br>TDCEN|Transceiver Delay Compensation Enable<br>This bit can be used to enable and disable the TDC feature. It can be written in Freeze mode only.<br>See Transmitter delay compensation in the CAN Protocol standard (ISO 11898-1:2015)<br>for details.<br>~~NOTE~~|
||TDC must be disabled when Loop Back mode is enabled (see CTRL1[LPB]).<br>~~NOTE~~|
||If CTRL2[BTE] is set, TDCEN is read as zero and a write operation has no effect.<br>~~NOTE~~|
||0b - TDC is disabled<br>1b - TDC is enabled|
|14<br>TDCFAIL|Transceiver Delay Compensation Fail<br>This bit indicates when the Transceiver Delay Compensation (TDC) mechanism is out of range, unable<br>to compensate the transceiver's loop delay and successfully compare the delayed received bits to the<br>transmitted ones (seeTransceiver delay compensation). TDCFAIL sets in the first time FlexCAN detects<br>the out of range condition. The CPU needs to write one to clear it.<br>If CTRL2[BTE] is set, TDCFAIL is read as zero and a write operation has no effect.<br>~~NOTE~~<br>0b - Measured loop delay is in range.<br>1b - Measured loop delay is out of range.|
|13<br>—|Reserved|
|12-8<br>TDCOFF|Transceiver Delay Compensation Offset<br>This bit field contains the offset value to be added to the measured transceiver's loop delay in order to<br>define the position of the delayed comparison point when bit rate switching is active. SeeTransceiver delay<br>compensationfor more details on how the loop delay measurement is performed.<br>TDCOFF can be written in Freeze mode only. Its value can be defined in Protocol Engine (PE) Clock periods<br>(CANCLK, seeProtocol timingfor more details), and must be selected to be smaller than the CAN bit<br>duration in the data bit rate for proper operation.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2850 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2851-03.png)


<!-- Start of picture text -->
Field Function<br>  NOTE<br>If CTRL2[BTE] is set, TDCOFF is read as zero and a write operation has no effect.<br>  NOTE<br>It is not recommended to have TDCOFF equal to zero.<br>7-6 Reserved<br>—<br>5-0 Transceiver Delay Compensation Value<br>TDCVAL This register contains the value of the transceiver loop delay measured from the transmitted EDL to R0<br>transition edge to the respective received one added to the TDCOFF value specified in the FDCTRL<br>register. This value is an integer multiple of the Protocol Engine (PE) Clock period (CANCLK).<br>  NOTE<br>If CTRL2[BTE] is set, TDCVAL is read as zero.<br>See Protocol timing for more details on how the loop delay measurement is performed.<br><!-- End of picture text -->

#### 72.6.2.36 CAN FD Bit Timing Register (FDCBT) 

##### Offset 

|Register|Offset|
|---|---|
|FDCBT|C04h|



##### Function 

This register stores the CAN bit timing variables used in the data phase of CAN FD messages when the FDCTRL[FDRATE] is set, compatible with CAN FD specification. FPRESDIV, FPROPSEG, FPSEG1, FPSEG2, and FRJW are used to define the time quantum duration, the number of time quanta per CAN bit, and the sample point position for the data bit rate portion of a CAN FD message with the BRS bit set. 

The contents of this register are not affected by soft reset. 

~~<mark>NOTE</mark>~~ 

The sum of the Fast Propagation Segment (FPROPSEG) and Fast Phase Segment 1 (FPSEG1) must be at least two time quanta. 

|~~NOTE~~|
|---|



The user must ensure bit time settings and protocol engine tolerance are in compliance with the CAN Protocol standard (ISO 11898-1:2015). 

~~<mark>NOTE</mark>~~ 

If CTRL2[BTE] is set, the FDCBT register is read as zero and a write operation has no effect. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2851 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2852-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserv<br>Reserved  FPRESDIV  FRJW<br>W ed<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserv<br>FPROPSEG  Reserved  FPSEG1  Reserved  FPSEG2<br>W ed<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29-20|Fast Prescaler Division Factor|
|FPRESDIV|This 10-bit field defines the ratio between the PE clock frequency and the serial clock (Sclock) frequency in<br>the data bit rate portion of a CAN FD message with the BRS bit set.<br>The Sclock period defines the time quantum of the CAN FD protocol for the data bit rate. This field can be<br>written only in Freeze mode because it is blocked by hardware in other modes.<br>Sclock frequency = PE clock frequency / (FPRESDIV + 1).<br>To minimize errors when processing FD frames, use the same value for FPRESDIV<br>and PRESDIV (in CBT or CTRL1). For more details see the first NOTE in sectionCAN<br>FD frames.<br>~~NOTE~~|
|19<br>—<br>18-16<br>FRJW|Reserved<br>Fast Resync Jump Width<br>This 3-bit field defines the maximum number of time quanta that a bit time can be changed by one<br>resynchronization in the data bit rate portion of a CAN FD message with the BRS bit set.<br>One time quantum is equal to the Sclock period. This field can be written only in Freeze mode because it is<br>blocked by hardware in other modes.<br>Resync Jump Width = FSJW + 1.|
|15<br>—|Reserved|
|14-10|Fast Propagation Segment|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2852 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|FPROPSEG|This 5-bit field defines the length of the propagation segment in the bit time in the data bit rate portion of a<br>CAN FD message with the BRS bit set. This field can be written only in Freeze mode because it is blocked<br>by hardware in other modes.<br>Propagation Segment Time = FPROPSEG × Time-Quanta.<br>Time-Quantum = one Sclock period.|
|9-8<br>—<br>7-5<br>FPSEG1|Reserved<br>Fast Phase Segment 1<br>This 3-bit field defines the length of phase segment 1 in the bit time in the data bit rate portion of a CAN<br>FD message with the BRS bit set. This field can be written only in Freeze mode because it is blocked by<br>hardware in other modes.<br>Phase Segment 1 = (FPSEG1 + 1) × Time-Quanta.<br>Time-Quantum = one Sclock period.|
|4-3<br>—|Reserved|
|2-0<br>FPSEG2|Fast Phase Segment 2<br>This 3-bit field defines the length of phase segment 2 in the data bit rate portion of a CAN FD message<br>with the BRS bit set. This field can be written only in Freeze mode because it is blocked by hardware in<br>other modes.<br>Phase Segment 2 = (FPSEG2 + 1) × Time-Quanta.<br>Time-Quantum = one Sclock period.|



#### 72.6.2.37 CAN FD CRC Register (FDCRC) 

##### Offset 

|Register|Offset|
|---|---|
|FDCRC|C08h|



##### Function 

This register provides information about the CRC of transmitted messages. 

FlexCAN uses different CRC polynomials for different frame formats, as shown below. 

The CRC_15 polynomial is used for all frames in CAN format. The CRC_17 polynomial is used for frames in CAN FD format with a DATA FIELD up to sixteen bytes. The CRC_21 polynomial is used for frames in CAN FD format with a DATA FIELD longer than sixteen bytes. Each polynomial shown below results in a Hamming distance of 6. This register is updated at the same time the Tx Interrupt flag is asserted. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2853 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

CRC_15 = C599h:  (x<sup>15</sup> + x<sup>14</sup> + x<sup>10</sup> + x<sup>8</sup> + x<sup>7</sup> + x<sup>4</sup> + x<sup>3</sup> + 1) CRC_17 = 3685Bh:  (x<sup>17</sup> + x<sup>16</sup> + x<sup>14</sup> + x<sup>13</sup> + x<sup>11</sup> + x<sup>6</sup> + x<sup>4</sup> + x<sup>3</sup> + x<sup>1</sup> + 1) CRC_21 = 302899h:  (x<sup>21</sup> + x<sup>20</sup> + x<sup>13</sup> + x<sup>11</sup> + x<sup>7</sup> + x<sup>4</sup> + x<sup>3</sup> + 1) Equation 30. CRC polynomial used on CAN frame 

~~<mark>NOTE</mark>~~ See CRC sequence calculation in the CAN Protocol standard (ISO 11898-1:2015) for details. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|Reserv|||F|D_MBCR|C||||Reserved|||FD|_TXCRC|||
|W|ed||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||FD_TX|CRC||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31<br>—|Reserved|
|30-24|CRC Mailbox Number for FD_TXCRC|
|FD_MBCRC|This field indicates the number of the mailbox corresponding to the value in the FD_TXCRC field, for both<br>FD and non-FD frames.<br>It reports the same information as in CRCR[MBCRC].|
|23-21<br>—|Reserved|
|20-0|Extended Transmitted CRC value|
|FD_TXCRC|This 21-bit field contains the CRC value calculated over the most recent transmitted message. Different<br>CRC polynomials are used for different frame formats. A 15-bit polynomial, CRC_15, is used for all frames in<br>CAN format. The second 17-bit polynomial, CRC_17, is used for frames in CAN FD format with a data field<br>up to sixteen bytes long. The third 21-bit polynomial, CRC_21, is used for frames in CAN FD format with a<br>data field longer than sixteen bytes.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2854 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||For CRC_15 and CRC_17, the 6 most significant bits and the 4 most significant bits are reported as<br>zeros, respectively.|
||For CRC_15, this register has the same content as CRC register.|



#### 72.6.2.38 Enhanced Rx FIFO Control Register (ERFCR) 

Offset 

|Register|Offset|
|---|---|
|ERFCR|C0Ch|



##### Function 

This register defines the Enhanced Rx FIFO configuration. 

This register can be written only in Freeze mode. 

All the contents of this register are affected by soft reset. 

~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

||Instance|Register supported|Register not supported|
|---|---|---|---|
|CAN_0||ERFCR|—|
|CAN_1||ERFCR|—|
|CAN_2||ERFCR|—|
|CAN_3||—|ERFCR|
|CAN_4||—|ERFCR|
|CAN_5||—|ERFCR|
|CAN_6||—|ERFCR|
|CAN_7||—|ERFCR|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2855 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2856-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R ERFE<br>DMALW  Reserved  NEXIF<br>W N<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>Reserved  NFE  Reserved  ERFWM<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31<br>ERFEN|Enhanced Rx FIFO enable<br>This field enables the Enhanced Rx FIFO.|
||ERFEN must not be set if MCR[RFEN] is set.<br>~~NOTE~~<br>0b - Enhanced Rx FIFO is disabled<br>1b - Enhanced Rx FIFO is enabled|
|30-26|DMA Last Word|
|DMALW|This field defines the last DMA address for each Enhanced RX FIFO element.<br>The table shows the number of elements and the last address for each Enhanced Rx FIFO element<br>according to the value of DMALW.<br><br> <br>|
||DMALW<br>Number of 32-bit<br>words transferred<br>Last FIFO address|
||0<br>1<br>2000h|
||1<br>2<br>2004h|
||2<br>3<br>2008h|
||3<br>4<br>200Ch|
||4<br>5<br>2010h|
||5<br>6<br>2014h|
||6<br>7<br>2018h|
||7<br>8<br>201Ch|
||8<br>9<br>2020h|
||9<br>10<br>2024h|
||10<br>11<br>2028h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2856 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

|Field|Function|||
|---|---|---|---|
||DMALW|Number of 32-bit<br>words transferred<br>|Last FIFO address|
||11|12|202Ch|
||12|13|2030h|
||13|14|2034h|
||14|15|2038h|
||15|16|203Ch|
||16|17|2040h|
||17|18|2044h|
||18|19|2048h|
||19|20|204Ch|
||Undefined|DMALW values in the table are reserved and must not b<br>~~NOTE~~|e used.|
|25-23<br>—<br>22-16|Reserved<br>Number of Extended ID Filter|Elements||
|NEXIF|This field defines the number<br>matching process.<br>NEXIF must be less than or e<br>The number of standard ID fil<br>The table shows the number<br>if all the filter elements are us|of extended ID filter elements used during the En<br>qual to NFE + 1.<br>ter elements is 2 × (NFE – NEXIF + 1).<br>of extended ID filters and standard ID filters availa<br>ed.|hanced Rx FIFO<br>ble for Enhanced Rx FIFO|
||NEXIF|NFE<br>Number of Extended ID<br>filter elements|Number of Standard ID<br>filter elements|
||0|63<br>0|128|
||1|63<br>1|126|
||2|63<br>2|124|
||3|63<br>3|122|
||4|63<br>4|120|
||5|63<br>5|118|
||6|63<br>6|116|
||7|63<br>7|114|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2857 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

|Field<br>Function||||
|---|---|---|---|
|NEXIF|NFE|Number of Extended ID<br>filter elements|Number of Standard ID<br>filter elements|
|8|63|8|112|
|9|63|9|110|
|10|63|10|108|
|11|63|11|106|
|12|63|12|104|
|13|63|13|102|
|14|63|14|100|
|15|63|15|98|
|16|63|16|96|
|17|63|17|94|
|18|63|18|92|
|19|63|19|90|
|20|63|20|88|
|21|63|21|86|
|22|63|22|84|
|23|63|23|82|
|24|63|24|80|
|25|63|25|78|
|26|63|26|76|
|27|63|27|74|
|28|63|28|72|
|29|63|29|70|
|30|63|30|68|
|31|63|31|66|
|32|63|32|64|
|33|63|33|62|
|34|63|34|60|
|35|63|35|58|
|36|63|36|56|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2858 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field<br>Function||||
|---|---|---|---|
|NEXIF|NFE|Number of Extended ID<br>filter elements|Number of Standard ID<br>filter elements|
|37|63|37|54|
|38|63|38|52|
|39|63|39|50|
|40|63|40|48|
|41|63|41|46|
|42|63|42|44|
|43|63|43|42|
|44|63|44|40|
|45|63|45|38|
|46|63|46|36|
|47|63|47|34|
|48|63|48|32|
|49|63|49|30|
|50|63|50|28|
|51|63|51|26|
|52|63|52|24|
|53|63|53|22|
|54|63|54|20|
|55|63|55|18|
|56|63|56|16|
|57|63|57|14|
|58|63|58|12|
|59|63|59|10|
|60|63|60|8|
|61|63|61|6|
|62|63|62|4|
|63|63|63|2|
|64|63|64|0|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2859 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field|Function|||
|---|---|---|---|
|15-14<br>—|Reserved|||
|13-8<br>NFE|Number of Enhanced Rx FIF<br>This field defines the total nu<br>according to the table.|O Filter Elements<br>mber of filter elements used during the en|hanced RX FIFO matching process|
||NFE|Maximum number of Extended ID<br>filter elements (NEXIF = NFE + 1)|Maximum number of standard ID<br>filter elements (NEXIF = 0)|
||0|1|2|
||1|2|4|
||2|3|6|
||3|4|8|
||4|5|10|
||5|6|12|
||6|7|14|
||7|8|16|
||8|9|18|
||9|10|20|
||10|11|22|
||11|12|24|
||12|13|26|
||13|14|28|
||14|15|30|
||15|16|32|
||16|17|34|
||17|18|36|
||18|19|38|
||19|20|40|
||20|21|42|
||21|22|44|
||22|23|46|
||23|24|48|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2860 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field<br>Function|||
|---|---|---|
|NFE|Maximum number of Extended ID<br>filter elements (NEXIF = NFE + 1)|Maximum number of standard ID<br>filter elements (NEXIF = 0)|
|24|25|50|
|25|26|52|
|26|27|54|
|27|28|56|
|28|29|58|
|29|30|60|
|30|31|62|
|31|32|64|
|32|33|66|
|33|34|68|
|34|35|70|
|35|36|72|
|36|37|74|
|37|38|76|
|38|39|78|
|39|40|80|
|40|41|82|
|41|42|84|
|42|43|86|
|43|44|88|
|44|45|90|
|45|46|92|
|46|47|94|
|47|48|96|
|48|49|98|
|49|50|100|
|50|51|102|
|51|52|104|
|52|53|106|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2861 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

|Field|Function|||
|---|---|---|---|
||NFE|Maximum number of Extended ID<br>filter elements (NEXIF = NFE + 1)|Maximum number of standard ID<br>filter elements (NEXIF = 0)|
||53|54|108|
||54|55|110|
||55|56|112|
||56|57|114|
||57|58|116|
||58|59|118|
||59|60|120|
||60|61|122|
||61|62|124|
||62|63|126|
||63|64|128|
|7-5<br>—|Reserved|||
|4-0<br>ERFWM|Enhanced Rx FIFO Watermark<br>This field defines the minimum n<br>number is reached, then ERFSR[<br>Minimum number of CAN messa<br>If MCR[D|umber of CAN messages stored in the<br>ERFWMI] is set.<br>ges = ERFWM + 1.<br>MA] is set, ERFWM field should be configu<br>~~NOTE~~|Enhanced RX FIFO. When that<br>res as 0x0.|



#### 72.6.2.39 Enhanced Rx FIFO Interrupt Enable Register (ERFIER) 

##### Offset 

|Register|Offset|
|---|---|
|ERFIER|C10h|



##### Function 

This register contains the interrupt enables for the Enhanced Rx FIFO. 

This register is affected by soft reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2862 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

|||Instan|ce|||Regis|ter sup|ported||Re|gister not supp|orted||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|CAN_0|||||ERFIER|||||—||||
|CAN_1|||||ERFIER|||||—||||
|CAN_2|||||ERFIER|||||—||||
|CAN_3|||||—|||||ERFIER||||
|CAN_4|||||—|||||ERFIER||||
|CAN_5|||||—|||||ERFIER||||
|CAN_6|||||—|||||ERFIER||||
|CAN_7|||||—|||||ERFIER||||
|Diagram<br>Bits|31|30|29|28|27<br>26|25|24|23|22|21<br>20|19<br>18|17|16|
|R<br>W|ERFU<br>FWIE|ERFO<br>VFIE|ERFW<br>MIIE|ERFD<br>AIE|||||Rese|rved||||
|Reset|0|0|0|0|0<br>0|0|0|0|0|0<br>0|0<br>0|0|0|
|Bits|15|14|13|12|11<br>10|9|8|7|6|5<br>4|3<br>2|1|0|
|R<br>W|Reserv<br>ed|||||||Reserved||||||
|Reset|0|0|0|0|0<br>0|0|0|0|0|0<br>0|0<br>0|0|0|



##### Diagram 

##### Fields 

|Field|Function|
|---|---|
|31|Enhanced Rx FIFO Underflow Interrupt Enable|
|ERFUFWIE|This field enables interrupt for ERFSR[ERFUFW].|
||0b - Enhanced Rx FIFO Underflow interrupt is disabled|
||1b - Enhanced Rx FIFO Underflow interrupt is enabled|
|30|Enhanced Rx FIFO Overflow Interrupt Enable|
|ERFOVFIE|This field enables interrupt for ERFSR[ERFOVF].|
||0b - Enhanced Rx FIFO Overflow is disabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2863 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table continued from the previous page... 

|Field|Function<br>1b - Enhanced Rx FIFO Overflow is enabled|
|---|---|
|29<br>ERFWMIIE|Enhanced Rx FIFO Watermark Indication Interrupt Enable<br>This field enables interrupt for ERFSR[ERFWMI].<br>0b - Enhanced Rx FIFO Watermark interrupt is disabled<br>1b - Enhanced Rx FIFO Watermark interrupt is enabled|
|28<br>ERFDAIE|Enhanced Rx FIFO Data Available Interrupt Enable<br>This field enables interrupt for ERFSR[ERFDA].<br>0b - Enhanced Rx FIFO Data Available interrupt is disabled<br>1b - Enhanced Rx FIFO Data Available interrupt is enabled|
|27-16<br>—|Reserved|
|15<br>—|Reserved|
|14-0<br>—|Reserved|



#### 72.6.2.40 Enhanced Rx FIFO Status Register (ERFSR) 

##### Offset 

|Register|Offset|
|---|---|
|ERFSR|C14h|



##### Function 

This register contains the status bits of the Enhanced RX FIFO including error indications and a clear FIFO bit. This register is affected by soft reset. 

~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

||Instance|Register supported|Register not supported|
|---|---|---|---|
|CAN_0||ERFSR|—|
|CAN_1||ERFSR|—|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2864 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2865-03.png)


<!-- Start of picture text -->
Instance Register supported Register not supported<br>CAN_2 ERFSR —<br>CAN_3 — ERFSR<br>CAN_4 — ERFSR<br>CAN_5 — ERFSR<br>CAN_6 — ERFSR<br>CAN_7 — ERFSR<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>ERFU ERFO ERFW ERFD<br>R 0 0 ERFE  ERFF<br>FW  VF  MI  A<br>ERFC<br>W W1C W1C W1C W1C<br>LR<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv<br>R 0 ERFEL<br>ed<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Enhanced Rx FIFO Underflow|
|ERFUFW|This field indicates that an underflow condition occurred in the enhanced Rx FIFO.<br>This field generates an interrupt if ERFIER[ERFUFWIE] is set.<br>0b - No such occurrence<br>1b - Enhanced Rx FIFO underflow|
|30|Enhanced Rx FIFO Overflow|
|ERFOVF|This field indicates that an overflow condition occurred in the Enhanced Rx FIFO.<br>This field generates an interrupt if ERFIER[ERFOVFIE] is set.|
||0b - No such occurrence|
||1b - Enhanced Rx FIFO overflow|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2865 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|29<br>ERFWMI|Enhanced Rx FIFO Watermark Indication<br>This field is set by the hardware if the number of messages available in the Enhanced Rx FIFO is greater<br>than the watermark defined in ERFCR[ERFWM].<br>This field generates an interrupt if ERFIER[ERFWMIIE] is set.<br>0b - No such occurrence<br>1b - The number of messages in FIFO is greater than the watermark|
|28<br>ERFDA|Enhanced Rx FIFO Data Available<br>This field is set by the hardware when there is at least one message stored in the ERX FIFO.<br>This field generates an interrupt if ERFIER[ERFDAIE] is set.<br>0b - No such occurrence<br>1b - There is at least one message stored in Enhanced Rx FIFO|
|27<br>ERFCLR|Enhanced Rx FIFO Clear<br>Writing one to this field during Freeze mode clears Enhanced Rx FIFO content.<br>Writing out of Freeze mode or writing zero to this field has no effect.<br>0b - No effect<br>1b - Clear Enhanced Rx FIFO content|
|26-18<br>—|Reserved|
|17<br>ERFE|Enhanced Rx FIFO empty<br>This field indicates that Enhanced Rx FIFO is empty.<br>0b - Enhanced Rx FIFO is not empty<br>1b - Enhanced Rx FIFO is empty|
|16<br>ERFF|Enhanced Rx FIFO full<br>This field indicates that Enhanced Rx FIFO is full.<br>0b - Enhanced Rx FIFO is not full<br>1b - Enhanced Rx FIFO is full|
|15<br>—|Reserved|
|14-6<br>—<br>5-0|Reserved<br>Enhanced Rx FIFO Elements|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2866 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|ERFEL|This field indicates the number of CAN messages stored in the Enhanced Rx FIFO.|



#### 72.6.2.41 High Resolution Time Stamp (HR_TIME_STAMP0 - HR_TIME_STAMP95) 

##### Offset 

For n = 0 to 95: 

|Register|Offset|
|---|---|
|HR_TIME_STAMPn|C30h + (n × 4h)|



##### Function 

The High Resolution Time Stamp registers are used for storing a copy of a 32-bit timer at the start or end of a CAN frame. 

HRST0 stores the 32-bit time stamp associated with MB0, HRSTS1 stores the the 32-bit time stamp associated with MB1, and so on. 

These registers are not affected by reset. 

~~<mark>NOTE</mark>~~ 

These registers must not be written out of Freeze mode. 

Table 467. High Resolution Time Stamp register operation 

|TSTAMPCAP|Captured time base|Capture point|
|---|---|---|
|b00|None|None|
|b01|32 bits of high-resolution on-chip timer|Seventh bit of the end of frame field for<br>transmission and sixth bit of the end of<br>frame field for reception.|
|b10|32 bits of high-resolution on-chip timer|Start of frame.|
|b11|32 bits of high-resolution on-chip timer|Start of frame for classical CAN frame<br>format and res bit for CAN FD frame<br>format.|



~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

||Instance|Register supported|Register not supported|
|---|---|---|---|
|CAN_0||HR_TIME_STAMP0–HR_TIME_STAMP95|—|
|CAN_1||HR_TIME_STAMP0–HR_TIME_STAMP95|—|
|CAN_2||HR_TIME_STAMP0–HR_TIME_STAMP95|—|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2867 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table continued from the previous page... 

||Instance|Register supported|Register not supported|
|---|---|---|---|
|CAN_3||HR_TIME_STAMP0–HR_TIME_STAMP63|HR_TIME_STAMP64–HR_TIME_STAMP95|
|CAN_4||HR_TIME_STAMP0–HR_TIME_STAMP63|HR_TIME_STAMP64–HR_TIME_STAMP95|
|CAN_5||HR_TIME_STAMP0–HR_TIME_STAMP63|HR_TIME_STAMP64–HR_TIME_STAMP95|
|CAN_6||HR_TIME_STAMP0–HR_TIME_STAMP63|HR_TIME_STAMP64–HR_TIME_STAMP95|
|CAN_7||HR_TIME_STAMP0–HR_TIME_STAMP63|HR_TIME_STAMP64–HR_TIME_STAMP95|



##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2868-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>TS<br>W<br>Reset See Register reset values.<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>TS<br>W<br>Reset See Register reset values.<br><!-- End of picture text -->

##### Register reset values 

|Register|Reset value|
|---|---|
|HR_TIME_STAMP0–HR_TIME_STAMP63|CAN_0–CAN_7: undefined|
|HR_TIME_STAMP64–HR_TIME_STAMP95|CAN_0–CAN_2: undefined|
||CAN_3–CAN_7: Register not supported|



##### Fields 

|Field|Function|
|---|---|
|31-0|High Resolution Time Stamp|
|TS|HR_TIME_STAMP register which captures the copy of timestamp of corresponding MB always captures<br>32-bit timer value.|



#### 72.6.2.42 Enhanced Rx FIFO Filter Element (ERFFEL0 - ERFFEL127) 

##### Offset 

For n = 0 to 127: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2868 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

|Register<br>ERFFELn|Offset<br>3000h + (n × 4h)|
|---|---|



##### Function 

These registers are used for storing the filter elements of the Enhanced Rx FIFO. 

For standard ID filtering, each ERFFEL register stores one filter element. For extended ID filtering, each pair of ERFFEL registers stores one filter element. 

ERFFEL registers can be written only in Freeze mode; otherwise, they are blocked by hardware. These registers are not affected by reset. They are located in RAM and must be explicitly initialized prior to any reception. 

~~<mark>NOTE</mark>~~ Each module instance supports a different number of registers. 

||Instance|Register supported|Register not supported|
|---|---|---|---|
|CAN_0||ERFFEL0–ERFFEL127|—|
|CAN_1||ERFFEL0–ERFFEL127|—|
|CAN_2||ERFFEL0–ERFFEL127|—|
|CAN_3||—|ERFFEL0–ERFFEL127|
|CAN_4||—|ERFFEL0–ERFFEL127|
|CAN_5||—|ERFFEL0–ERFFEL127|
|CAN_6||—|ERFFEL0–ERFFEL127|
|CAN_7||—|ERFFEL0–ERFFEL127|



##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2869-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>FEL<br>W<br>Reset u u u u u u u u u u u u u u u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>FEL<br>W<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2869 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Fields 

|Field|Function|
|---|---|
|31-0|Filter Element Bits|
|FEL|Each filter element is used during the match process and, if the matching criteria are met, a message is|
||stored in the Enhanced Rx FIFO.|



### 72.6.3 Message buffer structure 

The message buffer structure used by the FlexCAN module is represented in the following figure. Both extended (29-bit identifier) and standard (11-bit identifier) frames used in the CAN specification (Version 2.0 Part B) are represented. Each individual MB is formed by 16, 24, 40, or 72 bytes, depending on the quantity of data bytes allocated for the message payload: 8, 16, 32, or 64 data bytes, respectively. 

The memory area 80h–67Fh is used by the mailboxes. When CAN FD is enabled, the exact address for each MB depends on the size of its payload. See FlexCAN memory partition for CAN FD for more detailed information. 

Table 468. Message buffer structure — example with 64-byte payload 

||31|30<br>29<br>28|27<br>24<br>2|3<br>22|21<br>20<br>19<br>18<br>17<br>|16<br>15<br>8|7<br>0|
|---|---|---|---|---|---|---|---|
|0h|EDL|BRS<br>ESI|CODE|SRR|IDE<br>RTR<br>DLC|TIME|STAMP|
|4h||PRIO|ID (s|tandard/e|xtended)|ID (extende|d)|
|8h||Data byte 0|||Data byte 1|Data byte 2|Data byte 3|
|Ch||Data byte 4|||Data byte 5|Data byte 6|Data byte 7|
|10h||Data byte 8|||Data byte 9|Data byte 10|Data byte 11|
|14h||Data byte 12|||Data byte 13|Data byte 14|Data byte 15|
|18h||Data byte 16|||Data byte 17|Data byte 18|Data byte 19|
|1Ch||Data byte 20|||Data byte 21|Data byte 22|Data byte 23|
|20h||Data byte 24|||Data byte 25|Data byte 26|Data byte 27|
|24h||Data byte 28|||Data byte 29|Data byte 30|Data byte 31|
|28h||Data byte 32|||Data byte 33|Data byte 34|Data byte 35|
|2Ch||Data byte 36|||Data byte 37|Data byte 38|Data byte 39|
|30h||Data byte 40|||Data byte 41|Data byte 42|Data byte 43|
|34h||Data byte 44|||Data byte 45|Data byte 46|Data byte 47|
|38h||Data byte 48|||Data byte 49|Data byte 50|Data byte 51|
|3Ch||Data byte 52|||Data byte 53|Data byte 54|Data byte 55|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2870 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table 468. Message buffer structure — example with 64-byte payload (continued) 

|40h|Data byte 56|Data byte 57|Data byte 58|Data byte 59|
|---|---|---|---|---|
|44h|Data byte 60<br>= Unimplemented or reserved|Data byte 61|Data byte 62|Data byte 63|



##### EDL — Extended Data Length 

This bit distinguishes between CAN format and CAN FD format frames. The EDL bit must not be set for message buffers configured to RANSWER with code field 1010b (see table below). 

BRS — Bit Rate Switch 

This bit defines whether the bit rate is switched inside a CAN FD format frame. 

ESI — Error State Indicator 

This bit indicates if the transmitting node is error active or error passive. 

CODE — Message Buffer Code 

This 4-bit field can be accessed (read or write) by the CPU and by the FlexCAN module itself, as part of the message buffer matching and arbitration process. The encoding is shown in Table 469 and Table 470. See Functional description for additional information. 

Table 469. Message buffer code for Rx buffers 

|CODE description|Rx code BEFORE<br>receive new frame|SRV<sup>1</sup>|Rx code<br>AFTER successful<br>reception<sup>2</sup>|RRS<sup>3</sup>|Comment|
|---|---|---|---|---|---|
|0000b: INACTIVE<br>— MB is not<br>active.|INACTIVE|—|—|—|MB does not<br>participate in the<br>matching process.|
|0100b: EMPTY —<br>MB is active and<br>empty.|EMPTY|—|FULL|—|When a frame<br>is received<br>successfully (after<br>theMove-in<br>process), the<br>CODE field<br>is automatically<br>updated to FULL.|
|0010b: FULL —<br>MB is full.|FULL|Yes|FULL|—|The act of<br>reading the C/S<br>word followed by<br>unlocking the MB<br>(SRV) does not<br>make the code<br>return to EMPTY.<br>It remains FULL.<br>If a new frame is<br>moved to the MB<br>after the MB was<br>serviced, the code<br>still remains FULL.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2871 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table 469. Message buffer code for Rx buffers (continued) 

|CODE description|Rx code BEFORE<br>receive new frame|SRV<sup>1</sup>|Rx code<br>AFTER successful<br>reception<sup>2</sup>|RRS<sup>3</sup>|Comment|
|---|---|---|---|---|---|
||||||SeeMatching<br>processfor<br>matching details<br>related to FULL<br>code.|
|||No|OVERRUN|—|If the MB is FULL<br>and a new frame<br>is moved to this<br>MB before the<br>CPU services it,<br>the CODE field<br>is automatically<br>updated to<br>OVERRUN. See<br>Matching process<br>for details about<br>overrun behavior.|
|0110b: OVERRUN<br>— MB is being<br>overwritten into a<br>full buffer.|OVERRUN|Yes|FULL|—|If the CODE<br>field indicates<br>OVERRUN and<br>CPU has serviced<br>the MB, when<br>a new frame is<br>moved to the MB<br>then the code<br>returns to FULL.|
|||No|OVERRUN|—|If the CODE field<br>already indicates<br>OVERRUN, and<br>another new frame<br>must be moved,<br>the MB will<br>be overwritten<br>again, and the<br>code will remain<br>OVERRUN. See<br>Matching process<br>for details about<br>overrun behavior.|
|1010b:<br>RANSWER<sup>4</sup>—<br>A frame was<br>configured to|RANSWER|—|TANSWER(1110b)|0|A Remote Answer<br>was configured<br>to recognize a<br>remote request|
|recognize a|||||frame received.|
|Remote Request<br>frame and transmit|||||After that an MB<br>is set to transmit|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2872 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table 469. Message buffer code for Rx buffers (continued) 

|CODE description|Rx code BEFORE<br>receive new frame|SRV<sup>1</sup>|Rx code<br>AFTER successful<br>reception<sup>2</sup>|RRS<sup>3</sup>|Comment|
|---|---|---|---|---|---|
|a Response frame<br>in return.<sup>5</sup>|||||a response<br>frame. The code<br>is automatically<br>changed to<br>TANSWER<br>(1110b). See<br>Matching process<br>for details. If<br>CTRL2[RRS] is<br>negated, transmit<br>a response frame<br>whenever a remote<br>request frame with<br>the same ID is<br>received.|
|||—|—|1|This code is<br>ignored during<br>matching and<br>arbitration process.<br>SeeMatching<br>processfor details.|
|CODE[0]=1: BUSY<br>|BUSY<sup>6</sup>|—|FULL|—|Indicates that<br>|
|— FlexCAN is<br>updating the<br>contents of the<br>MB. The CPU<br>must not access<br>the MB.||—|OVERRUN|—|the MB is<br>being updated. It<br>will be negated<br>automatically and<br>does not interfere<br>with the next<br>CODE.|



1. SRV: Serviced MB. MB was read and unlocked by reading TIMER or other MB. 

2. A frame is considered a successful reception after the frame to be moved to MB (move-in process). See Move-in for details. 

3. Remote Request Stored bit, see "Control 2 register (CTRL2)" for details. 

4. Code 1010b is not considered Tx and an MB with this code should not be aborted. 

5. Code 1010b must be used in message buffers configured in CAN FD format, having the EDL bit set. 

6. Note that for Tx MBs, the BUSY bit should be ignored upon read, except when AEN bit is set in the MCR register. If this bit is asserted, the corresponding MB does not participate in the matching process. 

Table 470. Message buffer code for Tx buffers 

|CODE Description|Tx Code BEFORE tx<br>frame|MB RTR|Tx Code<br>AFTER successful<br>transmission|Comment|
|---|---|---|---|---|
|1000b: INACTIVE —<br>MB is not active|INACTIVE|—|—|MB does not<br>participate in arbitration<br>process.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2873 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table 470. Message buffer code for Tx buffers (continued) 

|CODE Description|Tx Code BEFORE tx<br>frame|MB RTR|Tx Code<br>AFTER successful<br>transmission|Comment|
|---|---|---|---|---|
|1001b: ABORT — MB<br>is aborted|ABORT|—|—|MB does not<br>participate in arbitration<br>process.|
|1100b: DATA — MB is<br>a Tx data frame (MB<br>RTR must be 0)|DATA|0|INACTIVE|Transmit data frame<br>unconditionally once.<br>After transmission,<br>the MB automatically<br>returns to the<br>INACTIVE state.|
|1100b: REMOTE —<br>MB is a Tx Remote<br>Request frame (MB<br>RTR must be 1)|REMOTE|1|EMPTY|Transmit remote<br>request frame<br>unconditionally once.<br>After transmission,<br>the MB automatically<br>becomes an Rx Empty<br>MB with the same ID.|
|1110b: TANSWER<br>— MB is a Tx<br>Response frame from<br>an incoming Remote<br>Request frame|TANSWER|—|RANSWER|This is an intermediate<br>code that is<br>automatically written<br>to the MB by the<br>CHI as a result of<br>a match to a remote<br>request frame. The<br>remote response frame<br>will be transmitted<br>unconditionally once,<br>and then the code<br>will automatically return<br>to RANSWER (1010b).<br>The CPU can also<br>write this code with<br>the same effect. The<br>remote response frame<br>can be either a<br>data frame or another<br>remote request frame<br>depending on the RTR<br>bit value. SeeMatching<br>processandArbitration<br>processfor details.|



SRR — Substitute Remote Request 

Fixed recessive bit, used only in extended format. It must be set to one by the user for transmission (Tx Buffers) and will be stored with the value received on the CAN bus for Rx receiving buffers. It can be received as either recessive or dominant. If FlexCAN receives this bit as dominant, then it is interpreted as an arbitration loss. 

1 = Recessive value is compulsory for transmission in extended format frames 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2874 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

0 = Dominant is not a valid value for transmission in extended format frames 

##### IDE — ID Extended Bit 

This field identifies whether the frame format is standard or extended. 

1 = Frame format is extended 

0 = Frame format is standard 

RTR — Remote Transmission Request 

This bit affects the behavior of remote frames and is part of the reception filter. See Table 469, Table 470, and the description of the RRS field in Control 2 register (CTRL2) for additional details. 

If FlexCAN transmits this bit as '1' (recessive) and receives it as '0' (dominant), it is interpreted as an arbitration loss. If this bit is transmitted as '0' (dominant), then if it is received as '1' (recessive), the FlexCAN module treats it as a bit error. If the value received matches the value transmitted, it is considered a successful bit transmission. 

1 = Indicates the current MB may have a remote request frame to be transmitted if MB is Tx. If the MB is Rx then incoming remote request frames may be stored. 

0 = Indicates the current MB has a data frame to be transmitted. In Rx MB it may be considered in matching processes. 

~~<mark>NOTE</mark>~~ When configuring CAN FD frames, the RTR bit must be negated. 

##### DLC — Length of Data in Bytes 

This 4-bit field is the length (in bytes) of the Rx or Tx data, which is located in offset 8h–Fh of the MB space (see Table 468). In reception, this field is written by the FlexCAN module, copied from the DLC (Data Length Code) field of the received frame. In transmission, this field is written by the CPU and corresponds to the DLC field value of the frame to be transmitted. When RTR = 1, the frame to be transmitted is a remote frame and does not include the data field, regardless of the DLC field (see Table 472). 

TIME STAMP — Free-Running Counter Time Stamp 

This 16-bit field is a copy of the Free-Running Timer, captured for Tx and Rx frames at the time when the beginning of the Identifier field appears on the CAN bus. 

Table 471. Time stamp operation 

|TSTAMPCAP|MBTSBASE|TIMER_SOURCE|Captured time base|Capture point|
|---|---|---|---|---|
|b00|bxx|0|CAN_TIMER<br>incremented by CAN<br>bit clock|Second bit of<br>identifier field|
|b00|bxx|1|CAN_TIMER<br>incremented by on-chip<br>timer clock|Second bit of<br>identifier field|
|bxx|b00|0|CAN_TIMER<br>incremented by CAN<br>bit clock|Second bit of<br>identifier field|
|bxx|b00|1|CAN_TIMER<br>incremented by on-chip<br>timer clock|Second bit of<br>identifier field|
|b01|b01|x|Lower 16 bits of high-<br>resolution on-chip timer|Seventh bit of the<br>end of frame field for<br>transmission and sixth|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2875 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table 471. Time stamp operation (continued) 

|TSTAMPCAP|MBTSBASE|TIMER_SOURCE|Captured time base|Capture point|
|---|---|---|---|---|
|||||bit of the end of frame<br>field for reception|
|b01|b10|x|Upper 16 bits of high-<br>resolution on-chip timer|Seventh bit of the<br>end of frame field for<br>transmission and sixth<br>bit of the end of frame<br>field for reception|
|b10|b01|x|Lower 16 bits of high-<br>resolution on-chip timer|Start of frame|
|b10|b10|x|Upper 16 bits of high-<br>resolution on-chip timer|Start of frame|
|b11|b01|x|Lower 16 bits of high-<br>resolution on-chip timer|Start of frame for<br>classical CAN frame<br>format and res bit for<br>CAN FD frame format|
|b11|b10|x|Upper 16 bits of high-<br>resolution on-chip timer|Start of frame for<br>classical CAN frame<br>format and res bit for<br>CAN FD frame format|



##### PRIO — Local priority 

This 3-bit field is used only when MCR[LPRIO_EN] is set, and it only makes sense for Tx mailboxes. These bits are not transmitted. They are appended to the regular ID to define the transmission priority. See Arbitration process. 

##### ID — Frame Identifier 

In standard frame format, only the 11 most significant bits (28 to 18) are used for frame identification in both receive and transmit cases. The 18 least significant bits are ignored. In extended frame format, all bits are used for frame identification in both receive and transmit cases. 

##### DATA BYTE 0 to 63 — Data Field 

Up to sixty four bytes can be used for a data frame, depending on the size of payload selected for the message buffers. 

For Rx frames, the data is stored as it is received from the CAN bus. DATA BYTE (n) is valid only if n is less than DLC as shown in the table below. 

Table 472. DATA BYTEs validity 

|DLC|Valid DATA BYTEs|
|---|---|
|0|none|
|1|DATA BYTE 0|
|2|DATA BYTE 0 to 1|
|3|DATA BYTE 0 to 2|
|4|DATA BYTE 0 to 3|
|5|DATA BYTE 0 to 4|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2876 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table 472. DATA BYTEs validity (continued) 

|DLC|Valid DATA BYTEs|
|---|---|
|6|DATA BYTE 0 to 5|
|7|DATA BYTE 0 to 6|
|8|DATA BYTE 0 to 7|
|9|DATA BYTE 0 to 11|
|10|DATA BYTE 0 to 15|
|11|DATA BYTE 0 to 19|
|12|DATA BYTE 0 to 23|
|13|DATA BYTE 0 to 31|
|14|DATA BYTE 0 to 47|
|15|DATA BYTE 0 to 63|



### 72.6.4 FlexCAN memory partition for CAN FD 

When CAN FD is enabled, the FlexCAN RAM can be partitioned in blocks of 512 bytes. Each block can accommodate a number of message buffers which depends on the configuration provided by FDCTRL[MBDSRn] bit fields as shown in table below. 

Table 473. RAM partition 

|RAM block|Number of MBs with 8 bytes<br>(default range)|Size control bit field in<br>FDCTRL register|Number of MBs of different<br>sizes, per block|
|---|---|---|---|
|0|0 to 31|MBDSR0|MBDSR0=00, 32 MBs with 8<br>bytes payload<br>MBDSR0=01, 21 MBs with 16<br>bytes payload<br>MBDSR0=10, 12 MBs with 32<br>bytes payload<br>MBDSR0=11, 7 MBs with 64<br>bytes payload|
|1|32 to 63|MBDSR1|MBDSR1=00, 32 MBs with 8<br>bytes payload<br>MBDSR1=01, 21 MBs with 16<br>bytes payload<br>MBDSR1=10, 12 MBs with 32<br>bytes payload<br>MBDSR1=11, 7 MBs with 64<br>bytes payload|
|2|64 to 95|MBDSR2|MBDSR2=00, 32 MBs with 8<br>bytes payload<br>MBDSR2=01, 21 MBs with 16<br>bytes payload|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2877 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table 473. RAM partition (continued) 

|RAM block|Number of MBs with 8 bytes<br>(default range)|Size control bit field in<br>FDCTRL register|Number of MBs of different<br>sizes, per block|
|---|---|---|---|
||||MBDSR2=10, 12 MBs with 32<br>bytes payload<br>MBDSR2=11, 7 MBs with 64<br>bytes payload|



When payload sizes of 16, 32, or 64 bytes are configured in some or all RAM blocks, the total number of MBs and its respective number order may differ from the default configuration of 8 bytes. For example, suppose Block0 is configured to 8 bytes payload, Block1 to 16 bytes, Block2 to 32 bytes, Then the following table indicates how the message buffers will be arranged in RAM. 

Table 474. RAM partition example 

|RAM block|Payload size|Number of MBs in the RAM<br>block|Message buffer range|
|---|---|---|---|
|0|FDCTRL[MBDSR0]=00, 8<br>bytes payload|32|0 to 31|
|1|FDCTRL[MBDSR1]=01, 16<br>bytes payload|21|32 to 52|
|2|FDCTRL[MBDSR2]=10, 32<br>bytes payload|12|53 to 64|



### 72.6.5 FlexCAN message buffer memory map 

The FlexCAN memory buffers are allocated in memory according to the tables below. 

Table 475. 8-byte message buffers 

|Address offset (hex)|MBDSR=b00<br>8-byte payload|
|---|---|
|0080|MB0|
|0090|MB1|
|00A0|MB2|
|00B0|MB3|
|00C0|MB4|
|00D0|MB5|
|00E0|MB6|
|00F0|MB7|
|0100|MB8|
|0110|MB9|
|0120|MB10|
|0130|MB11|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2878 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table 475. 8-byte message buffers (continued) 

|Address offset (hex)|MBDSR=b00<br>8-byte payload|
|---|---|
|0140|MB12|
|0150|MB13|
|0160|MB14|
|0170|MB15|
|0180|MB16|
|0190|MB17|
|01A0|MB18|
|01B0|MB19|
|01C0|MB20|
|01D0|MB21|
|01E0|MB22|
|01F0|MB23|
|0200|MB24|
|0210|MB25|
|0220|MB26|
|0230|MB27|
|0240|MB28|
|0250|MB29|
|0260|MB30|
|0270|MB31|
|0280|MB32|
|0290|MB33|
|02A0|MB34|
|02B0|MB35|
|02C0|MB36|
|02D0|MB37|
|02E0|MB38|
|02F0|MB39|
|0300|MB40|
|0310|MB41|
|0320|MB42|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2879 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table 475. 8-byte message buffers (continued) 

|Address offset (hex)|MBDSR=b00<br>8-byte payload|
|---|---|
|0330|MB43|
|0340|MB44|
|0350|MB45|
|0360|MB46|
|0370|MB47|
|0380|MB48|
|0390|MB49|
|03A0|MB50|
|03B0|MB51|
|03C0|MB52|
|03D0|MB53|
|03E0|MB54|
|03F0|MB55|
|0400|MB56|
|0410|MB57|
|0420|MB58|
|0430|MB59|
|0440|MB60|
|0450|MB61|
|0460|MB62|
|0470|MB63|
|0480|MB64|
|0490|MB65|
|04A0|MB66|
|04B0|MB67|
|04C0|MB68|
|04D0|MB69|
|04E0|MB70|
|04F0|MB71|
|0500|MB72|
|0510|MB73|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2880 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table 475. 8-byte message buffers (continued) 

|Address offset (hex)|MBDSR=b00<br>8-byte payload|
|---|---|
|0520|MB74|
|0530|MB75|
|0540|MB76|
|0550|MB77|
|0560|MB78|
|0570|MB79|
|0580|MB80|
|0590|MB81|
|05A0|MB82|
|05B0|MB83|
|05C0|MB84|
|05D0|MB85|
|05E0|MB86|
|05F0|MB87|
|0600|MB88|
|0610|MB89|
|0620|MB90|
|0630|MB91|
|0640|MB92|
|0650|MB93|
|0660|MB94|
|0670|MB95|



Table 476. 16-byte message buffers 

|Address offset (hex)|MBDSR=b01|
|---|---|
||16-byte payload|
|0080|MB0|
|0098|MB1|
|00B0|MB2|
|00C8|MB3|
|00E0|MB4|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2881 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table 476. 16-byte message buffers (continued) 

|Address offset (hex)|MBDSR=b01<br>16-byte payload|
|---|---|
|00F8|MB5|
|0110|MB6|
|0128|MB7|
|0140|MB8|
|0158|MB9|
|0170|MB10|
|0188|MB11|
|01A0|MB12|
|01B8|MB13|
|01D0|MB14|
|01E8|MB15|
|0200|MB16|
|0218|MB17|
|0230|MB18|
|0248|MB19|
|0260|MB20|
|0280|MB21|
|0298|MB22|
|02B0|MB23|
|02C8|MB24|
|02E0|MB25|
|02F8|MB26|
|0310|MB27|
|0328|MB28|
|0340|MB29|
|0358|MB30|
|0370|MB31|
|0388|MB32|
|03A0|MB33|
|03B8|MB34|
|03D0|MB35|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2882 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table 476. 16-byte message buffers (continued) 

|Address offset (hex)|MBDSR=b01<br>16-byte payload|
|---|---|
|03E8|MB36|
|0400|MB37|
|0418|MB38|
|0430|MB39|
|0448|MB40|
|0460|MB41|
|0480|MB42|
|0498|MB43|
|04B0|MB44|
|04C8|MB45|
|04E0|MB46|
|04F8|MB47|
|0510|MB48|
|0528|MB49|
|0540|MB50|
|0558|MB51|
|0570|MB52|
|0588|MB53|
|05A0|MB54|
|05B8|MB55|
|05D0|MB56|
|05E8|MB57|
|0600|MB58|
|0618|MB59|
|0630|MB60|
|0648|MB61|
|0660|MB62|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2883 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table 477. 32-byte message buffers 

|Address offset (hex)|MBDSR=b10<br>32-byte payload|
|---|---|
|0080|MB0|
|00A8|MB1|
|00D0|MB2|
|00F8|MB3|
|0120|MB4|
|0148|MB5|
|0170|MB6|
|0198|MB7|
|01C0|MB8|
|01E8|MB9|
|0210|MB10|
|0238|MB11|
|0280|MB12|
|02A8|MB13|
|02D0|MB14|
|02F8|MB15|
|0320|MB16|
|0348|MB17|
|0370|MB18|
|0398|MB19|
|03C0|MB20|
|03E8|MB21|
|0410|MB22|
|0438|MB23|
|0480|MB24|
|04A8|MB25|
|04D0|MB26|
|04F8|MB27|
|0520|MB28|
|0548|MB29|
|0570|MB30|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2884 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table 477. 32-byte message buffers (continued) 

|Address offset (hex)|MBDSR=b10|
|---|---|
||32-byte payload|
|0598|MB31|
|05C0|MB32|
|05E8|MB33|
|0610|MB34|
|0638|MB35|



Table 478. 64-byte message buffers 

|Address offset (hex)|MBDSR=b11<br>64-byte payload|
|---|---|
|0080|MB0|
|00C8|MB1|
|0110|MB2|
|0158|MB3|
|01A0|MB4|
|01E8|MB5|
|0230|MB6|
|0280|MB7|
|02C8|MB8|
|0310|MB9|
|0358|MB10|
|03A0|MB11|
|03E8|MB12|
|0430|MB13|
|0480|MB14|
|04C8|MB15|
|0510|MB16|
|0558|MB17|
|05A0|MB18|
|05E8|MB19|
|0630|MB20|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2885 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

### 72.6.6 Legacy Rx FIFO structure 

When MCR[RFEN] is set, the memory area 80h–DCh (which is normally occupied by MBs 0–5) is used by the reception Legacy FIFO engine. 

The region 80h–8Ch contains the output of the Legacy Rx FIFO which must be read by the CPU as a message buffer. This output contains the oldest message that has been received but not yet read. The region 90h–DCh is reserved for internal use of the Legacy Rx FIFO engine. 

An additional memory area, which starts at E0h and may extend up to 2DCh (normally occupied by MBs 6–37) depending on the CTRL2[RFFN] field setting, contains the ID filter table (configurable from 8 to 128 table elements) that specifies filtering criteria for accepting frames into the Legacy Rx FIFO. 

Out of reset, the ID filter table flexible memory area defaults to E0h and extends only to FCh, which corresponds to MBs 6 to 7 for RFFN = 0, for backward compatibility with previous versions of FlexCAN. 

The following shows the Legacy Rx FIFO data structure. 

Table 479. Legacy Rx FIFO structure 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2886-09.png)


<!-- Start of picture text -->
31 28 24 23 22 21 20 19 18 17 16 15 8 7 0<br>80h IDHIT SRR IDE RTR DLC TIME STAMP<br>84h ID standard ID extended<br>88h Data byte 0 Data byte 1 Data byte 2 Data byte 3<br>8Ch Data byte 4 Data byte 5 Data byte 6 Data byte 7<br>90h–DCh Reserved<br>E0h ID filter table element 0<br>E4h ID filter table element 1<br>E8h– ID filter table elements 2 to 125<br>2D4h<br>2D8h ID filter table element 126<br>2DCh ID filter table element 127<br>= Unimplemented or reserved<br><!-- End of picture text -->

Each ID filter table element occupies an entire 32-bit word and can be compounded by one, two, or four Identifier Acceptance Filters (IDAF) depending on the MCR[IDAM] field setting. The following figures show the IDAF indexation. 

The following table shows the three different formats of the ID table elements. Note that all elements of the table must have the same format. See Legacy Rx FIFO for more information. 

Table 480. ID table structure 

|Format|31|30|29|24|23|16|15<br>14|13|8<br>7<br>1<br>0|
|---|---|---|---|---|---|---|---|---|---|
|A|RTR|IDE|||||RXIDA|||



##### Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2886 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### Table 480. ID table structure (continued) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2887-03.png)


<!-- Start of picture text -->
(standard = 29–19, extended = 29–1)<br>B RTR IDE RXIDB_0 RTR IDE RXIDB_1<br>(standard = 29–19, extended = 29–16) (standard = 13–3, extended = 13–0)<br>C RXIDC_0 RXIDC_1 RXIDC_2 RXIDC_3<br>(std/ext = 31–24) (std/ext = 23–16) (std/ext = 15–8) (std/ext = 7–0)<br>= Unimplemented or Reserved<br><!-- End of picture text -->

##### RTR — Remote frame 

This bit specifies if remote frames are accepted into the Legacy FIFO if they match the target ID. 

- 1 = Remote frames can be accepted and data frames are rejected 

- 0 = Remote frames are rejected and data frames can be accepted 

##### IDE — Extended frame 

Specifies whether extended or standard frames are accepted into the Legacy FIFO if they match the target ID. 

1 = Extended frames can be accepted and standard frames are rejected 

- 0 = Extended frames are rejected and standard frames can be accepted 

RXIDA — Rx frame identifier (Format A) 

Specifies an ID to be used as acceptance criteria for the Legacy FIFO. In the standard frame format, only the 11 most significant bits (29 to 19) are used for frame identification. In the extended frame format, all bits are used. 

RXIDB_0, RXIDB_1 — Rx frame identifier (Format B) 

Specifies an ID to be used as acceptance criteria for the Legacy FIFO. In the standard frame format, the 11 most significant bits (a full standard ID) (29 to 19 and 13 to 3) are used for frame identification. In the extended frame format, all 14 bits of the field are compared to the 14 most significant bits of the received ID. 

RXIDC_0, RXIDC_1, RXIDC_2, RXIDC_3 — Rx frame identifier (Format C) 

Specifies an ID to be used as acceptance criteria for the Legacy FIFO. In both standard and extended frame formats, all 8 bits of the field are compared to the 8 most significant bits of the received ID. 

IDHIT — Identifier acceptance filter hit indicator 

This 9-bit field indicates which identifier acceptance filter was hit by the received message that is in the output of the Legacy Rx FIFO. See Legacy Rx FIFO for more information. 

### 72.6.7 Enhanced Rx FIFO structure 

When ERFCR[ERFEN] is set, the Enhanced Rx FIFO is enabled. The region 2000h–204Ch contains the output of the Enhanced Rx FIFO which must be read by the CPU as a message buffer. This output contains the oldest message that has been received but not yet read. The following table shows the Enhanced Rx FIFO data structure. 

##### Table 481. Enhanced RX FIFO Structure 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/072_CAN_-FlexCAN-/S32K3XXRM_数据表.pdf-2887-23.png)


<!-- Start of picture text -->
31 30 29 28 24 23 22 21 20 19 18 17 16 15 8 7 6 0<br>2000h EDL BRS ESI RESERVED SRR IDE RTR DLC TIME STAMP LEGACY<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2887 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table 481. Enhanced RX FIFO Structure (continued) 

|2004h|RESERVED<br>I|D (STANDARD/EXTENDED)|ID (EXTEND|ED)|
|---|---|---|---|---|
|2008h|Data byte 0|Data byte 1|Data byte 2|Data byte 3|
|200Ch|Data byte 4|Data byte 5|Data byte 6|Data byte 7|
|2010h|Data byte 8|Data byte 9|Data byte 10|Data byte 11|
|2014h|Data byte 12|Data byte 13|Data byte 14|Data byte 15|
|2018h|Data byte 16|Data byte 17|Data byte 18|Data byte 19|
|201Ch|Data byte 20|Data byte 21|Data byte 22|Data byte 23|
|2020h|Data byte 24|Data byte 25|Data byte 26|Data byte 27|
|2024h|Data byte 28|Data byte 29|Data byte 30|Data byte 31|
|2028h|Data byte 32|Data byte 33|Data byte 34|Data byte 35|
|202Ch|Data byte 36|Data byte 37|Data byte 38|Data byte 39|
|2030h|Data byte 40|Data byte 41|Data byte 42|Data byte 43|
|2034h|Data byte 44|Data byte 45|Data byte 46|Data byte 47|
|2038h|Data byte 48|Data byte 49|Data byte 50|Data byte 51|
|203Ch|Data byte 52|Data byte 53|Data byte 54|Data byte 55|
|2040h|Data byte 56|Data byte 57|Data byte 58|Data byte 59|
|2044h|Data byte 60|Data byte 61|Data byte 62|Data byte 63|
|IH_OFF||RESERVED||ID HIT|
|TS_OFF||HR TIME STAMP|||
|2050h|||||
|...<br>263Ch||19 Enhanced FIFO Elements (RESERVED)|||



~~<mark>NOTE</mark>~~ 

ID HIT offset and high resolution time stamp offset are changed dynamically according to data length code (DLC) as shown in Table 482. 

Table 482. ID HIT offset and high resolution time stamp offset 

|Data Length Code (DLC)|ID HIT offset (IH_OFF)|High resolution time stamp<br>offset (TS_OFF)|
|---|---|---|
|0|2008h|200Ch|
|1–4|200Ch|2010h|
|5–8|2010h|2014h|
|9|2014h|2018h|
|10|2018h|201Ch|
|11|201Ch|2020h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2888 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

Table 482. ID HIT offset and high resolution time stamp offset (continued) 

|Data Length Code (DLC)|ID HIT offset (IH_OFF)|High resolution time stamp<br>offset (TS_OFF)|
|---|---|---|
|12|2020h|2024h|
|13|2028h|202Ch|
|14|2038h|203Ch|
|15|2048h|204Ch|



##### EDL — Extended Data Length 

This bit distinguishes between classical CAN format and CAN FD format frames. 

- 0 – Classical CAN frame format 

- 1 – CAN FD frame format 

##### BRS — Bit Rate Switch 

This bit defines whether the bit rate is switched inside a CAN FD format frame. 

- 0 – Bit rate is not switched in a CAN FD frame 

- 1 – Bit rate is switched in a CAN FD frame 

ESI — Error State Indicator 

This bit indicates if the transmitting node is error active or error passive. This bit is meaningful only if EDL = 1. 

- 0 – Transmitting node is error active 

- 1 – Transmitting node is error passive 

SRR — Substitute Remote Request 

Fixed recessive bit, used only in extended format. Transmitting nodes always send it as recessive and receiving nodes can receive it as either recessive or dominant. If FlexCAN receives this bit as dominant, then it is interpreted as an arbitration loss. 

##### IDE — ID Extended Bit 

This field identifies whether the frame format is standard or extended. 

- 0 – Frame format is standard 

- 1 – Frame format is extended 

RTR — Remote Frame 

- 0 = Indicates the current frame is a data frame 

- 1 = Indicates the current frame is remote request 

DLC — Data Length Code 

This 4-bit field defines the number of bytes in the data field of a CAN frame (Data byte 0 to Data byte 63 ). When RTR = 1, the frame is a remote request and does not include the data field, regardless of the DLC field. Refer to Table 472 for more details. 

LEGACY TIME STAMP — 16-bit Time Stamp 

This 16-bit field is a copy of the Free-Running Timer, captured during the CAN frame. See Table 471 to find more details about legacy time stamp operation. 

##### ID — Frame Identifier 

In base frame format, only the 11 most significant bits are used for frame identification. The 18 least significant bits are ignored. In extended frame format, all bits are used for frame identification. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2889 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

##### DATA BYTE 0 to 63 — Data Field 

Up to sixty four bytes can be stored in the data field. 

##### IDHIT — Identifier Acceptance Filter Hit Indicator 

This field indicates which Enhanced Rx FIFO Filter Element (ERFFELn) was hit by the received message that is in the output of the Enhanced Rx FIFO. For each filter region, standard-ID filter space and extended-ID filter space, there is an independent index starting from zero. Table 483 shows how IDHIT is written by FlexCAN according to each filter element. 

##### Table 483. IDHIT for Enhanced Rx FIFO 

|Enhanced Rx FIFO filter element<br>— ERFFEL|ID HIT value|Filter element type|
|---|---|---|
|ERFFEL0|0|Extended-ID|
|ERFFEL1|1|Extended-ID|
|.<br>.<br>.|.<br>.<br>.|Extended-ID|
|ERFFEL(m–1)|m–1|Extended-ID|
|ERFFEL(m)|0|Standard-ID|
|ERFFEL(m+1)|1|Standard-ID|
|.<br>.<br>.|.<br>.<br>.|Standard-ID|
|ERFFEL(2n–m+1)|2x(n–m)+1|Standard-ID|



~~<mark>NOTE</mark>~~ Where m = NEXIF and n = NFE. If NEXIF = 0, only standard-ID filter elements exist, and if NEXIF > NFE, then only extended-ID filter elements exist. 

HR TIME STAMP — High-resolution Time Stamp 

32-bit time base captured during the CAN frame. When CTRL2[TSTAMPCAP] is different from zero, a 32-bit time base is captured from a dedicated on-chip timer which operates in free running mode. See TSTAMPCAP field description in Control 2 Register (CTRL2) to find more details about capture point configuration of the high-resolution time stamp. 

## 72.7 Glossary 

Active message buffer A message buffer is active if it can participate in the current matching or arbitration process. Bus interface unit FlexCAN submodule responsible for the interface to the CPU. Bus off See CAN Specification.<sup>[230]</sup> CAN Controller Area Network, a serial communication protocol defined in CAN Specification<sup>[230]</sup> and ISO International Standard.<sup>[231]</sup> 

- [12] Controller Area Network – CAN Specification Version 2.0 Part A, Part B, Robert Bosch GmbH, 1991. 

- [13] ISO International Standard – ISO 11898 First Edition 1993 Road Vehicles – Interchange of Digital Information – Controller Area Network (CAN) for high-speed Communication. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2890 / 4640 

NXP Semiconductors 

CAN (FlexCAN) 

|CHI|Controller-host interface, a FlexCAN submodule responsible for message buffer matching and<br>arbitration algorithms.|
|---|---|
|CRC|Cyclic redundancy check|
|Dominant bit|A dominant bit wins the arbitration on the CAN bus. It is transmitted as 0.|
|Doze mode|A system low-power mode where the CPU bus remains active and a global Doze mode request<br>is sent to all peripherals asking them to enter low power mode.|
|Error active|See CAN Specification.<sup>[230]</sup>|
|Error frame|See CAN Specification.<sup>[230]</sup>|
|Error passive|See CAN Specification.<sup>[230]</sup>|
|Form error|See CAN Specification.<sup>[230]</sup>|
|Hard reset|A reset coming from an external pin and/or following power-on. It resets everything.|
|Idle|See CAN Specification.<sup>[230]</sup>|
|Information processing time|See CAN Specification.<sup>[230]</sup>|
|Intermission|See CAN Specification.<sup>[230]</sup>|
|Matching elements|Data used in the matching process, such as ID, filter, mask, etc.|
|MB|SeeMessage buffer.|
|Message buffer|Internal FlexCAN data structure containing bytes received from, or to be transmitted to, the<br>CAN line, as well as information about this data.|
|Overload frame|See CAN Specification.<sup>[230]</sup>|
|Phase buffer segment|See CAN Specification.<sup>[230]</sup>|
|Recessive bit|A recessive bit loses the arbitration on the CAN bus. It is transmitted as 1.|
|Sclock|Serial clock. Obtained by dividing the clock feeding the CAN engine (oscillator or bus clock) by<br>a prescaler factor. The Sclock period defines the time quantum for CAN protocol timing.|
|Soft reset|Global reset typically used by peripherals to reinitialize some of its registers, but not all of them.|
|Stop mode|A system low-power mode in which all chip clocks are stopped for maximum power savings.|
|Stuffing error|See CAN Specification.<sup>[230]</sup>|
|Time quantum|This is equal to the Sclock period. It is the minimum time period used to compose the CAN<br>protocol bit timing.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2891 / 4640 

