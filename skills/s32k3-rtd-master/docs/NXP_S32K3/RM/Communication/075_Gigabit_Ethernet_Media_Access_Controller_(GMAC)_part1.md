NXP Semiconductors 

# Chapter 75 Gigabit Ethernet Media Access Controller (GMAC) 

75.1 Chip-specific GMAC information 

### 75.1.1 GMAC instances and configuration 

This chip supports up to 1 instance of GMAC IP. 

Table 555. GMAC instances 

|Instance|K3x1 / K3x2 / K3x4|K358|
|---|---|---|
|GMAC|No|Yes|



~~<mark>NOTE</mark>~~ 

DWC_EQOS refer to the Synopsys GMAC IP. 

~~<mark>NOTE</mark>~~ 

The description for some GMAC registers include references to configurations of the Synopsis Ethernet MAC IP. Refer to MAC_HW_Feature registers for the specific features available in this chip. 

~~<mark>NOTE</mark>~~ 

GMAC operates only in Clock options A and B, since the module clock becomes lower than the protocol clock (RMII/MII clocks) in other modes. 

Following key features are supported: 

- This chip supports MII/RMII/RGMII interfaces. 

- 4 bit MII interface operating at 2.5/25/50 Mhz, MII can run at 10/100/200 Mbps. 

- 2 bit RMII interface operating at 50 MHz, RMII can run at 10/100 Mbps 

- 4 bit MII-Lite interface operating at 2.5/25 MHz 

- 4 bit RGMII interface operation at 125 MHz in DDR mode 

- 4 PPS are supported using DMA trigger 

- Supports 4-bit Reduced Gigabit MII (RGMII) operating at 125 MHz 

- The Ethernet module supports a data rate of 1Gbps (1000 Mbps) 

- MTL Receive FIFO size 16384 bytes 

- MTL Transmit FIFO size 16384 bytes 

~~<mark>NOTE</mark>~~ 

The DMA referred within GMAC chapter refers to the internal GMAC DMA engine and not the device AXBS master DMA. 

~~<mark>NOTE</mark>~~ 

Register access beyond 8k address space is not supported and will generate a transfer error. 

~~<mark>NOTE</mark>~~ 

Always use store and forward mode if possible. In cut through mode, if multiple masters are active then there is chance (even in round robin arbitration mode) that GMAC DMA may starve for data resulting in insufficient data in TX FIFO leading to Tx underflow. To avoid this, increase MTL_TxQ0_Operation_Mode[TTC] value as needed. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3529 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

The table below provides the information on the specific configuration utilized for the S32K3x4 and K342 devices. 

Table 556. Specific configuration information 

|Application Interface||
|---|---|
|Application interface configuration|EQOS-AHB|
|Data width|64|
|Endian mode|Little Endian|
|Address width|32|
|CSR interfcae|APB3 interface|
|General feature||
|Mode of operation|10/100/1000|
|Enable double VLAN processing|Yes|
|Enable Que/channel based VLAN tag<br>inertion on Tx|Yes|
|Enable SA and VLAN insertion on Tx|Enabled by default|
|Buffer management||
|MTL Receive FIFO size in bytes|16384|
|MTL Receive FIFO size in bytes|16384|
|Enable debug memory access|Yes|
|Use single port memory|Yes|
|PHY interface||
|Enable RGMII, RMII only|Enable RGMII, Enable RMII,<br>GMII/MII default|
|Enabled signel phy interface|No|
|Enable MDIO interface|Yes|
|Filtering||
|Enable Additional 1-31 MAC<br>address registers|2|
|Enable Address Filter Hash Table|Yes|
|Hash Table Size|256|
|Enable VLAN Hash table based filtering|Yes|
|Extended Rx VLAN Filter Enable|Yes|
|Number of VLAN tag Filters|32|
|Enable Layer3 and Layer4 Packet Filter|Yes|
|Number of layer3 and Layer 4<br>packet filters|8|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3530 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 556. Specific configuration information (continued) 

||Enable Flexible Programmable<br>Receive Parser|Yes|
|---|---|---|
||Maximum Packet Header Size<br>for Parsing|256|
||Maximum Entries of Parser Look up table|64|
||Packet duplication support|Yes|
|IEEE 1588 timestamp|||
||Enable IEEE 1588 Time stamp support|Enabled by default|
||IEEE 1588 System Time Support|Both option|
||Add IEEE 1588 Higher word register|Yes|
||Enable IEEE 1588 sub nanoseconds<br>time stamp support|Yes|
||Add IEEE 1588 Auxilary snapshot|No|
||Enable Flexible Pulse Per<br>Seconds Output|Yes|
||Number of pulse per Second outputs|4|
||Enable PTP Timestamp offload feature|No|
||Enable One Step timestamp for PTP<br>over UDP/IP feature|No|
||Enable One Step timestamp feature|Yes|
|Multiple queue support|||
||Number of transmit Queue|3|
||Number of recieve Queue|3|
||Enable data center Bridging|Yes|
||Enable Audo Video Bridging|Yes|
||Enable support for AV in Tx queue 1|Yes|
||Enable support for AV in Tx queue 2|Yes|
||Enable support for AV in Tx queue 3|No|
||Enable support for AV in Tx queue 4|No|
||Number of DMA Channel on the<br>receive side|3|
|Time sensitive networking|||
||Enable Enhancement to<br>Schedule traffic(EST)|Yes|
||Width of Time Interval Field in the Gate<br>Control List|24|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3531 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 556. Specific configuration information (continued) 

||Depth of Gate Control List|256|
|---|---|---|
||Enable Frame Pre-emption support|Yes|
|Time based scheduling|||
||Enable time based Scheduling|Yes|
|TCP/IP offloading features|||
||Enable receive TCP/IP<br>Checksum Check|Enabled by default|
||Enable transmit TCP/IP<br>Checksum offload|Enabled by default|
||Enable support for Tx COE in Tx queue 0|Yes|
||Enable support for Tx COE in Tx queue 1|Yes|
||Enable support for Tx COE in Tx queue 2|Yes|
||Enable support for Tx COE in Tx queue 3|No|
||Enable support for Tx COE in Tx queue 4|No|
||Enable TCP Segmentation offloading for<br>TCP/IP|No|
||Enable Split Header Feature|Yes|
||Enable IPv4 ARP offload|Yes|
|RMON counters|||
||Enable MAC<br>Management Counters(MMC)|Yes|
||Enable the MAC Management Counters<br>for Reciever TCP/IP Checksum offload|No|
|Automotive safety feature|||
||Enable all automotive safety feature|Yes|



## 75.4 Introduction 

This section and all its sub-sections are Synopsys Proprietary. Used with permission. 

##### GMAC: 

- Supports the 10/100/1000 Mbps application in compliance with IEEE802.3-2015 specifications 

- Can support advanced applications such as time-sensitive networking and AVB 

- Supports a MAC core that has prominent features such as a flexible receive parser, media clock recovery and generation, and safety 

### 75.4.1 Features 

GMAC supports these features in addition to the default feature defined in the IEEE802.3 specification: 

- MII (10/100 Mbps), RMII (10/100 Mbps), and RGMII (1000 Mbps) 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3532 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

- Time-aware shaper (IEEE802.1bv), time synchronization (IEEE802.1AS-rev), and frame preemption (IEEE802.1Qbu) for time-sensitive networking 

- Media clock recovery and generation for AVB 

- AMBA 2.0 for AHB master and APB3 interface 

- RMII specification version 1.2 from RMII consortium 

- RGMII specification version 2.6 from HP/Marvell 

- Separate interface for transmit, receive, and control paths 

- Two-buffer ring 

- Broadcast and multicast packet duplication 

- Full-duplex flow control operations (IEEE 802.3x pause packet and priority flow control) 

- Network statistics with MAC management (RMON) counters 

- Flexibility to control the pulse per second (PPS) output signal 

- MDIO clause 22 and clause 45 interface for configuration and management of the PHY device 

- Preamble and SFD insertion and deletion 

- Automatic CRC and pad generation/stripping option 

- Option to disable CRC checking 

- Programmable insert packet gap 

- Source address insertion or replacement 

- VLAN insertion, replacement, and deletion in transmitted packets with per-packet or static-global control, insertion, replacement, and deletion of up to two VLAN tags, insertion, replacement, and deletion of queue or channel-based VLAN tags 

- IEEE802.1Q VLAN tag detection and an option to delete the tags in the receive packets 

- Programmable safety watchdog timeout limits 

- Flexible address filtering modes that allow: 

   - Up to two additional 48-bit perfect DA filters with masks for each byte 

   - Up to two 48-bit SA comparison checks with masks for each byte 

   - 64-bit hash filter for multicast and unicast DA addresses 

   - Option to pass all multi-cast addressed packets 

   - Promiscuous mode to pass all packets without any filtering for network monitoring 

   - Passing of all incoming packets (according to filter) with a status report 

- Additional packet filtering that is based on: 

   - Virtual local area network (VLAN) tag—perfect match and hash-based filtering, which is based on either outer or inner VLAN tag, is possible 

   - Layer 3 and layer 4—TCP or UDP over IPv4 or IPv6 

   - Extended VLAN tag—filtering based on four filter selections 

### 75.4.2 Functional block diagram 

This figure shows the GMAC block diagram. GMAC has four main blocks to perform all the functions. 

- The AHB interface is connected to all DMA channels. 

- The DMA arbiter helps in the arbitration of all paths (transmit and receive) in DMA channels. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3533 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

- Each channel has a separate set of control and status registers (CSRs) for managing the transmit and receive functions, descriptor handling, and interrupt handling. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3534-03.png)


<!-- Start of picture text -->
Transmit<br>memory<br>Transmit MTL transmit RGMII, RMII,<br>MAC<br>DMA FIFO or SGMII<br>transmit<br>channel control interface<br>Receive MTL receive<br>AHB MAC<br>interface DMA FIFO receive GMII<br>channel control<br>CSR<br>DMA MTL  MAC Core<br>channel CSR CSR<br>APB<br>interace DMA MTL<br>AHB<br>Receive<br>memory<br>DMA arbiter Select<br><!-- End of picture text -->

Figure 429. System-level block diagram 

## 75.5 Architecture 

This section and all its sub-sections are Synopsys Proprietary. Used with permission. 

The section describes GMAC interfaces, protocols, and functionality. These are its main blocks: 

- AHB master and APB3 slave interface 

- DMA controller 

- MTL 

- MAC 

- Interrupts 

### 75.5.1 AHB master and CSR slave (APB3) interface 

The 32-bit APB3 slave interface: 

- Provides access to DMA, MTL, and MAC control and status registers (CSRs) 

- Supports the 32-bit write and read transfers to these CSRs 

- Supports single- and all-burst transfers, and an OKAY response 

The DMA block uses the AHB master interface to interact with the external world. The AHB master interface: 

- Controls data transfer 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3534 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

- Is AMBA 2.0-compliant with no restrictions 

- Supports 64-bit data transfer 

- Supports single and INCR transfers 

- Supports burst-length modes such as Fixed, Unspecified, and Mixed 

### 75.5.2 DMA inclusions 

DMA controller: 

- Includes independent transmit (Tx) and receive (Rx) engines, and a CSR space. The transmit engine transfers data from the system memory to the MTL interface, whereas the receive engine transfers data from the MTL interface to the system memory. 

- Is designed for packet-oriented data transfers such as packets in Ethernet. 

- Communicates with the host through CSR, descriptor lists, and data buffers. 

##### DMA descriptors 

DMA supports up to three transmit and three receive descriptor lists (or DMA channels). The base address of each list is written to the respective transmit and receive descriptor list address registers. A descriptor list is forward linked and the next descriptor is always considered at a fixed offset to the current one, and DMA_CH0_Control[DSL] contols the offset. The number of descriptors in the list is programmed using the respective DMA_CH0_TxDesc_Ring_Length and DMA_CH0_RxDesc_Ring_Length registers. After the DMA processes the last descriptor in the list, it automatically jumps to the descriptor in the list address register to create a descriptor ring. 

GMAC supports the ring structure for DMA descriptors. For more information, see Descriptors . 

The DMA engine uses descriptors to efficiently move data from source to destination with minimal host intervention, and the DMA controller can be programmed to interrupt the host in certain situations. These situations may include packet transmit and receive transfer completion and other normal or error conditions. 

The descriptor lists reside in the physical memory address space of the application. Each descriptor can point to a maximum of two buffers in the system memory, enabling two buffers to be used and physically addressed rather than contiguous buffers in the memory. 

##### Data buffers 

A data buffer resides in the application physical memory space and consists of an entire packet or part of a packet but cannot exceed a single packet. Buffers contain only data. The buffer status is maintained in the descriptor. Data chaining refers to packets that span multiple data buffers. However, a single descriptor cannot span multiple packets. The DMA skips to the data buffer of the next packet when an EOP is detected. 

The next few sections discuss DMA controller. 

#### 75.5.2.1 DMA controller bus burst access 

DMA engines attempt to transfer data in a burst of the maximum size programmed using DMA_CH0_Tx_Control[TxPBL] and DMA_CH0_Rx_Control[RxPBL] of the respective DMAs, which always access the receive and transmit descriptors in the maximum possible (limited by PBL or 16 * 8/bus width) burst length for 16 bytes to be read. The burst transfers that the DMA initates can be split into multiple burst transfers according to the AHB requirements and settings specified in (DMA_SysBus_Mode). 

The transmit DMA initiates a data transfer only when sufficient space is available in the MTL transmit queue to accommodate either of these: 

- Bytes corresponding to the configured burst (PBL * bus_width/8) 

- Remaining bytes in the transmit buffer without EOP 

- Number of bytes till EOP 

The receive DMA initiates a data transfer in these conditions: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3535 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

- Sufficient data is available in the MTL receive queue to accommodate the configured burst 

- EOP (when it is less than the configured burst length) is detected in the receive queue 

DMA indicates the start address and the number of transfers required to the AHB master interface. When the interface is configured for fixed-length burst, it transfers data by using the best combination of the INCR4, INCR8, or INCR16 and SINGLE transactions. If EOP is reached before the fixed burst ends on the AHB interface, DMA performs dummy transfers to complete the fixed burst. Otherwise, DMA_SysBus_Mode[FB] becomes 0. The DMA transfers the data using undefined length (INCR) and SINGLE transactions. 

When the AHB interface is configured for address-aligned beats, both DMA engines ensure that the first-burst transfer that AHB initates is less than or equal to the size of the configured PBL value, and the subsequent beats start at an address aligned to this value. The DMA can only align the address for beats up to size 16 (for PBL > 16) for the AHB interface because it does not support more than INCR16. 

#### 75.5.2.2 DMA application data buffer alignment 

The transmit and receive data buffers do not have any restrictions on start address alignment. For example, in systems with 32-bit memory, the start address for buffers can be aligned to any of the four bytes. However, the DMA always initiates write transfers with an address aligned to the bus width and dummy data (old data) in the invalid byte lanes. The process of write transfer typically happens during the beginning or end of an Ethernet packet transfer. The software driver must discard the dummy bytes based on the start address of the buffer and size of the packet. 

Table 557. Data buffer alignment examples 

|Examples||
|---|---|
|Buffer read|If the transmit buffer address is FF2h (for a 32-bit data bus) and 15 bytes need to be transferred, the DMA reads<br>five full words from address FF0h. However, when DMA transfers data to the MTL transmit queue, the extra<br>bytes (the first two bytes) are dropped or ignored. Similarly, the last 3 bytes of the last transfer are also ignored.<br>The DMA always ensures that it transfers a full 32-bit data to the MTL transmit queue, unless it is the end of<br>the packet.|
|Buffer write|If the receive buffer address is FF2h (for a 64-bit data bus) and 16 bytes of a received packet need to be<br>transferred, the DMA writes 3 full words from address FF0h. However, the first 2 bytes of the first transfer and<br>the last 6 bytes of the third transfer have dummy data. The DMA considers the offset address only if it is the first<br>receive buffer of the packet. It ignores the offset address and performs full-word writes for the middle and last<br>receive buffers of the packet.|



#### 75.5.2.3 DMA buffer size calculations 

DMA does not update the size fields in the transmit and receive descriptors. It updates only the status fields (RDES and TDES) of the descriptors. The driver performs the size calculations. 

The transmit DMA transfers the exact number of bytes (as the buffer size field of TDES2 indicates) to MAC. If a descriptor is marked as first (TDES3[FD] = 1), the DMA marks the first transfer from the buffer as SOP, and if the descriptor is marked as last (TDES3[LD]), the DMA marks the last transfer from that data buffer as EOP to the MTL. 

The receive DMA transfers data to a buffer until the buffer is full or MTL sends the end of packet. When TDES3[FD] = 1, the amount of valid data in a buffer is accurately indicated by the buffer size fields in (DMA_CH0_Rx_Control) minus the data buffer pointer offset. The offset is 0 when the data buffer pointer is aligned to the data bus width. If a descriptor is marked as last, the buffer may not be full (as indicated by DMA_CH0_Rx_Control[RBSZ_13_y] and DMA_CH0_Rx_Control[RBSZ_x_0]). To compute the amount of valid data in this final buffer, the driver must read the packet length (PL fields of RDES3[14:0]) and subtract the sum of the buffer sizes of the preceding buffers in this packet. The receive DMA always transfers the start of the next packet with a new descriptor. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3536 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### 75.5.2.4 DMA arbiter 

The arbiter inside the DMA module performs the arbitration between the transmit and receive channel accesses to the AHB master interface. These two types of arbitrations are supported: 

- Round-robin: If DMA_Mode[DA] = 0 and both transmit and receive DMAs simultaneously request access, the arbiter allocates the data bus in ratio sets defined in DMA_Mode[PR]. 

- Fixed-priority: If DMA_Mode[DA] = 1, receive DMA is always prioritized over transmit DMA for data access by default. If DMA_Mode[TXPR] = 1, transmit DMA is prioritized over receive DMA as explained in Table 574. 

### 75.5.3 MTL 

MTL provides the FIFO memory interface to buffer and regulate the packets between system memory and MAC. It also enables data to be transferred between the system clock and MAC clock domains. The MTL layer has two data paths: transmit path and receive path. MTL communicates with the host through ATI on the transmit path and through ARI on the receive path. 

#### 75.5.3.1 Transmit path 

The internal DMA: 

- Handles all transactions for the transmit path through ATI. 

- Pushes the Ethernet packet reads from system memory to the corresponding queue. 

The Ethernet packet, then, pops out and is transfered to MAC when the queue reaches its threshold (Threshold mode) or if the complete packet is in the queue (Store-and-Forward mode). When EOP is transferred, the status of the transmission is taken from MAC and transferred back to the internal DMA. 

#### 75.5.3.1.1 Transmit control word 

This control information related to packet transmission is provided as part of the control word through the ATI interface: 

- Packet length (if DCB is enabled with WFQ scheduling algorithm) 

- CRC pad control 

- Source address insertion control 

- VLAN insertion and replacement control and VLAN tag for outer and inner VLAN tags 

- TCP/IP checksum insertion control 

- One-step timestamping control correction 

- Transmit timestamp enable 

#### 75.5.3.1.2 Transmit operation 

These two modes of operation trigger data read towards MAC: 

- Threshold (or cut-through) mode: This is the default mode. In this mode, as soon as the number of bytes in the queue crosses the configured threshold level (or when the end of packet is written before the threshold is crossed), the data is ready to be popped out and forwarded to MAC. The threshold level is configured by using MTL_TxQ0_Operation_Mode[TTC]. 

- Store-and-Forward mode: In this mode, MTL pops the packet out to MAC only when one or more of the following conditions are true: 

   - A complete packet is stored in the queue. 

   - The transmit FIFO becomes almost full. 

   - The ATI watermark becomes low. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3537 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

The watermark becomes low when the requested queue is not spacious enough to accommodate the requested burst length on ATI. Therefore, MTL, when operating in Store-and-Forward mode, allows packet transmission even if the packet length is bigger than the transmit queue size. 

You can flush the complete content of the transmit queue by writing 1 to MTL_TxQ0_Operation_Mode[FTQ] or MTL_TxQ1_Operation_Mode[FTQ], depending on the queue. Doing so initializes the queue pointers to the default state. The FTQ field returns to 0 by itself. If you write 1 to the FTQ field during a packet transfer from MTL to MAC, MTL stops further transfers because MTL considers the queue to be empty. Therefore, an underflow event occurs at the MAC transmitter. 

#### 75.5.3.1.3 Initialization flow 

After reset, MTL is ready to manage the data flow between DMA and MAC. 

- With single-transmit queue configurations, there are no initialization requirements for enabling MTL. 

- With multiple-transmit queue configurations, initialize the queue size for each of the queues by programming MTL_TxQ0_Operation_Mode[TQS] corresponding to a transmit queue. Also, initialize the MAC block. Internal DMA controllers must be individually enabled through their respective CSRs. 

#### 75.5.3.2 Receive path 

MAC sends packets to the MTL receive module and pushes them into the receive queue. MTL indicates the status (fill level) of the queue to the application or DMA when it crosses the configured receive threshold (MTL_RxQ0_Operation_Mode[RTC]), or when the MTL receive module receives the complete packet in Store-and-Forward mode. MTL also indicates the fill level of the queue so that DMA can initiate preconfigured burst transfers to the AHB interface. 

#### 75.5.3.2.1 Receive operation 

During a receive operation, MTL is MAC's slave. This is the general sequence of events: 

1. When MAC receives a packet, it indicates the availability of receive data. 

2. MAC indicates the SOP and EOP delimiters. 

3. MTL accepts the data and pushes it into the corresponding receive queue. 

4. When MAC transfers EOP to the MTL receive module, MAC also drives the status word that MTL pushes into the corresponding receive queue. 

5. MTL takes the data out of the queue and sends it to DMA depending on these modes: 

   - Threshold mode 

   - Store-and-Forward mode 

The sections that follow discuss these modes. 

#### 75.5.3.2.1.1 Threshold mode 

In Threshold (default) mode, MTL reads the data and indicates its availability to the application or DMA when one of these occurs: 

- Data bytes equal to the threshold amount are written to the receive queue (to MTL_RxQ0_Operation_Mode[RTC] and MTL_RxQ1_Operation_Mode[RTC]). 

- A full packet of data is received into the queue. 

#### 75.5.3.2.1.2 Store-and-Forward mode 

In this mode (when MTL_RxQ0_Operation_Mode[RSF] = 1), the initial receive queue locations are reserved for the status words before writing the SOP. A packet is read out only after it is completely written into the receive queue. In this mode, all error packets are dropped (if configured through MTL_RxQ0_Operation_Mode[FEP]) in such a way that only valid packets are read and forwarded to the application. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3538 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### 75.5.3.2.2 Multi-packet receive operation 

In Threshold mode, the packet status is available immediately after the packet data. In Store-and-Forward mode, the packet data is available after the packet status. MTL is capable of storing any number of packets in the queue as long as it is not full. 

If MAC receives a packet when the corresponding receive queue is full, MTL ignores that packet and overflow pulse generates on the corresponding receive queue. In addition, MTL increments the overflow counter in (MTL_RxQ0_Missed_Packet_Overflow_Cnt) for the corresponding queue. 

#### 75.5.3.2.3 Error handling in receive operation 

MTL performs these actions if the MTL receive queue is full before it receives the EOP data from MAC: 

1. Declares an overflow 

2. Drops the whole packet (including the status word) 

3. Increments the overflow counter in DMA ((MTL_RxQ0_Missed_Packet_Overflow_Cnt)) 

This is true even if MTL_RxQ0_Operation_Mode[FEP] is 1. 

If the start address of such a packet is already transferred to the read controller, the rest of the packet is dropped and a dummy EOP is written to the queue along with the status word with overflow status. The status indicates a partial packet because of overflow. In such packets, the Packet Length field is invalid. If the MTL receive queue is configured to operate in the Store-and-Forward mode and the length of the received packet is more than the queue size, overflow occurs and all such packets are dropped. 

The MTL receive control logic can filter errors and undersized packets, if enabled by using MTL_RxQ0_Operation_Mode[FEP] and MTL_RxQ0_Operation_Mode[FUP]. If the start address of one such packet is already transferred to the receive queue read controller, the packet is not filtered. The start address of the packet is transferred to the read controller after the packet crosses the receive threshold defined using MTL_RxQ0_Operation_Mode[RTC]. 

If the MTL receive queue is configured to operate in Store-and-Forward mode, all error packets can be filtered and dropped. For the application or DMA to flush the error packet being read from the queue, it must assert the flush signal. MTL then stops transferring data to the application (DMA). It internally reads the rest of the packet and drops it. MTL then starts transferring the next packet, if it's available. 

### 75.5.4 MAC 

MAC can support the MII and RMII PHY interface and it consists of: 

- MTI 

- MRI 

- MCI 

#### 75.5.4.1 MAC transmission 

The MAC transmission process is as follows: 

1. The transmission initiates when MTL pushes in data with the SOP signal asserted. 

2. After the SOP signal is detected, MAC accepts the data and begins transmitting to RMII or MII. 

3. After the EOP signal is transferred to MAC, it performs one of these steps: 

   - Completes normal packet transmission and sends the transmission status to MTL 

   - Sends retry requests if a normal collision (in Half-Duplex mode) occurs during transmission, and until one of the following is true: 

      - Packet is successfully transmitted. 

      - Maximum retry requests have expired. When this happens, MAC aborts the packet transmission with "excessive collision transmit" status. MAC accepts and drops all further data until it receives the next SOP. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3539 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

The MTL block must retransmit the same packet from SOP on observing a retry request (in the status) from MAC. 

   - If any one of the following happens, MAC aborts the packet transmission: 

      - No carrier (Half-Duplex mode) 

      - Loss of carrier (Half-Duplex mode) 

      - Excessive deferral (Half-Duplex mode) 

      - Late collisions (Half-Duplex mode) 

      - Jabber 

      - MAC accepts and drops all further data until it receives the next SOP 

4. MAC issues an underflow status if MTL is not able to provide data continuously during transmission. Until the next SOP is received, MAC accepts and drops all further data. 

5. During the normal transfer of a packet from MTL, if MAC receives an SOP without getting an EOP for the previous packet, it ignores the SOP and considers the new packet as a continuation of the previous packet. 

#### 75.5.4.2 MAC reception 

The receive operation initiates as follows: 

1. MAC detects a state-of-frame data on RMII or MII. 

2. MAC strips the preamble and SFD before processing an Ethernet packet. 

3. The MAC AFM: 

   - Checks the header fields (SA and DA) of an incoming packet for filtering 

   - Verifies the CRC contained in the packet's FCS field 

4. MAC's AFM checks the header fields (SA and DA) of an incoming packet for filtering. 

5. FCS verifies the CRC of the received packet. 

6. MAC stores the received packet in a shallow buffer until address filtering is performed. 

7. AFM drops the packet if it fails the address filter. 

### 75.5.5 Interrupts 

GMAC supports interrupt coalescing, which reduces the number of interrupts generated by the module and reduces the CPU load. (MAC_Interrupt_Status) captures various interrupt events. If the interrupt enable field of an interrupt is 1, the corresponding interrupt generates based on the event status in the Status registers. The Interrupt mode (INTM) field decides whether the interrupt signal is a level signal or pulse signal. See the following table and interrupt map file attached to this document for details. 

Table 558. Interrupt request 

|Interrupt request|Interrupt Enable / Mask Register|Interrupt Flag Register|
|---|---|---|
|Common interrupt|(MAC_Interrupt_Enable)|(MAC_Interrupt_Status)|
||(MMC_Rx_Interrupt_Mask)|(MMC_Rx_Interrupt)|
||(MMC_Tx_Interrupt_Mask)|(MMC_Tx_Interrupt)|
||(MMC_FPE_Tx_Interrupt_Mask)|(MMC_FPE_Tx_Interrupt)|
||(MMC_FPE_Rx_Interrupt_Mask)|(MMC_FPE_Rx_Interrupt)|
||(MTL_DBG_CTL)|(MTL_DBG_STS)|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3540 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 558. Interrupt request (continued) 

|Interrupt request|Interrupt Enable / Mask Register|Interrupt Flag Register|
|---|---|---|
||(MTL_EST_Intr_Enable)|(MTL_EST_Status)|
||(MTL_RXP_Interrupt_Control_Status)|(MTL_RXP_Interrupt_Control_Status)|
||(MTL_Q0_Interrupt_Control_Status)|(MTL_Q0_Interrupt_Control_Status)|
||(MTL_Q1_Interrupt_Control_Status)|(MTL_Q1_Interrupt_Control_Status)|
||(DMA_CH0_Interrupt_Enable)(transfer complete<br>interrupts only)|DMA_CH0_Interrupt_Status|
||(DMA_CH1_Interrupt_Enable)(transfer complete<br>interrupts only)|DMA_CH1_Interrupt_Status|
|||(DMA_Interrupt_Status)<br>(First level status. Indicates major<br>block event source: DMA channel, MTL<br>or MAC)|
|||(MTL_Interrupt_Status)<br>(Status summary for MTL block<br>interrupts: Rx Parser, EST, FIFO Debug,<br>Queue 1/Queue 0)|
|Tx interrupt 0/1|(DMA_CH0_Tx_Control)|(DMA_CH0_Status)|
||(DMA_CH0_Interrupt_Enable)||
||(DMA_CH1_Tx_Control)|(DMA_CH1_Status)|
||(DMA_CH1_Interrupt_Enable)||
|Rx interrupt 0/1|(DMA_CH0_Rx_Control)|(DMA_CH0_Status)|
||(DMA_CH0_Interrupt_Enable)||
||(DMA_CH1_Rx_Control)|(DMA_CH1_Status)|
||(DMA_CH1_Interrupt_Enable)||
|Safety interrupt|(MTL_ECC_Interrupt_Enable)|(MTL_ECC_Interrupt_Status)|
|||(MTL_Safety_Interrupt_Status)|
||(MTL_DPP_Control)|(MAC_DPP_FSM_Interrupt_Status)|
||(MAC_FSM_Control)||



These are the interrupt output signals that are synchronous to the CSR clock. 

- Sbd_intr_o – common interrupt 

- Sbd_perch_tx_intr_o[max_dma_ch] – interrupt per transmit channel 

- Sbd_perch_rx_intr_o [max_dma_ch] – interrupt per receive channel 

~~<mark>NOTE</mark>~~ 

max_dma_ch = number of transmit/receive queues, which is 2 

The sbd_intr_o common interrupt is a level signal. When it is asserted, a corresponding interrupt event source can be found in (DMA_Interrupt_Status), which is a read-only register that contains the event source fields corresponding to each DMA channel 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3541 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

(transmit and receive queue pair), MAC transaction layer, and MAC blocks. You must then read the following registers and look for the fields that are 1: 

- (MAC_Interrupt_Status) 

- (MTL_Interrupt_Status) 

- (DMA_CH0_Status) 

The sbd_intr_o interrupt deasserts only when all the enabled interrupt events are clear in their respective status registers, and correspondingly, all the fields in (DMA_Interrupt_Status) are 0. (DMA_CH0_Status) captures all the interrupt events of that transmit DMA and receive DMA channel pair. 

(DMA_CH0_Interrupt_Enable) contains the corresponding enable fields for each of the interrupt events. These are the two groups of interrupts in the DMA channel: 

- Normal—DMA_CH0_Status[NIS] indicates this interrupt, which is used for events that occur during the normal transfer of packets (TI, RI, TBU). 

- Abnormal—DMA_CH0_Status[AIS] indicates this interrupt, which is used for error events. 

Interrupts are not queued. If the same interrupt event occurs again before the driver responds to the previous one, no additional interrupts generate. 

The common sbd_intr_o output signal asserts for the transfer complete interrupts only when the corresponding interrupts are enabled in (DMA_CH0_Interrupt_Enable). 

GMAC also supports these per-channel transfer-complete interrupt signals: 

- sbd_perch_tx_intr_o[max_dma_ch] (transmit per channel interrupts) 

- sbd_perch_rx_intr_o[max_dma_ch] (receive per channel interrupts) 

The behavior of the RI/TI/sbd_perch_tx_intr_o[]/sbd_perch_rx_intr_o[] changes depends on the configuration specified in DMA_Mode[INTM]. This table explains the transfer complete interrupt behavior. 

Table 559. Transfer complete interrupt behavior 

|Interrupt<br>mode|Behavior of sbd_perch_tx_intr_o[] and sbd_perch_rx_intr_o[]|Behavior of the TI/RI<br>interrupts and sbd_intr_o|
|---|---|---|
|INTM = 1|In this mode, these signals indicate the values of the<br>correspondingDMA_CH0_Status[RI]andDMA_CH0_Status[TI]fields when<br>DMA_CH0_Status[RI]andDMA_CH0_Status[TI]are 1, respectively.<br>Therefore, they are level signals that you clear by writing 1 to these fields.<br>The signals do not assert whenDMA_CH0_Status[RI]orDMA_CH0_Status[TI]<br>is 0.|DMA_CH0_Status[RI]and<br>DMA_CH0_Status[TI]are<br>configured as explained.<br>For any RI/TI events:<br>• The sbd_intr_o signal<br>does not assert.<br>• DMA_CH0_Status[NIS]<br>remains 0.|
|INTM = 2|In this mode, RI/TI are queued and indicate the values of the corresponding<br>DMA_CH0_Status[RI]andDMA_CH0_Status[TI]fields when any of these<br>fields is 1. RI and TI are level signals that you clear by writing 1 to these<br>fields. However, the fields become 1 again if another TI/RI event is detected<br>beforeDMA_CH0_Status[RI]andDMA_CH0_Status[TI]become 1 for the<br>previous event.|DMA_CH0_Status[RI]<br>andDMA_CH0_Status[TI]<br>become 1 whenever the<br>transfer complete event is<br>detected and are reset<br>whenever the software driver<br>changes them to 0 by<br>writing 1. However, if another<br>transfer complete event is|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3542 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 559. Transfer complete interrupt behavior (continued) 

|detected before the software|
|---|
|changes it to 0 (services it),|
|GMAC automatically writes|
|1 to these fields again. The|
|generation of the sbd_intr_o|
|signal; however, is not based|
|onDMA_CH0_Status[RI]|
|orDMA_CH0_Status[TI].|



## 75.6 Signal descriptions 

This section and all its sub-sections are Synopsys Proprietary. Used with permission. 

### 75.6.1 Module signals 

This table provides port/signal names and their descriptions. See the IOMUX file attached to this document for details. 

Table 560. Module signals 

|Port Name|I/O|Description|
|---|---|---|
|clk_tx_i|I|MAC Transmitter Clock.<br>The external PHY or PLL provides this transmission clock. This is 312.5 MHz<br>in 2.5 Gbps mode, 125 MHz in 1 Gbps mode, 25 MHz in 100 Mbps mode,<br>2.5 MHz in 10 Mbps mode. All transmission signals generated by the MAC<br>are synchronous to this clock. This clock is required for all PHY interfaces.|
|clk_rx_i|I|MAC Receiver Clock.<br>The external PHY provides this receive clock for RGMII, GMII, MII, and RMII<br>interfaces. This clock is 312.5 MHz in 2.5 Gbps mode, 125 MHz in 1 Gbps<br>mode, 25 MHz in 100 Mbps mode, 2.5 MHz in 10 Mbps mode. All RGMII,<br>GMII, and MII receive signals received by the MAC are synchronous to this<br>clock. This clock input is required for all PHY interfaces.|
|clk_rmii_i|I|RMII Clock.<br>This is the 50-MHz clock used by the RMII interface. When the RMII<br>interface is selected, the clk_rx_i clock should be 25 or 2.5 MHz and it should<br>be derived from this clock.|
|clk_ptp_ref_i|I|PTP Reference Clock.<br>This reference clock, provided by an external oscillator or a timing source, is<br>used for the timestamp logic.|
|ptp_pps_o[3:0]|O|Pulse Per Second.<br>This signal is high based on the PPS mode selected in the<br>MAC_PPS_Control register. When PPS is programmed in Media Clock<br>recovery Mode, this port indicates the recovered clock. See the device<br>IOMUX sheet for details on the number of these signals available.|
|mcg_pst_trig_i[3:0]|I|Media Clock Generation Trigger Input|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3543 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 560. Module signals (continued) 

|Port Name|I/O|Description|
|---|---|---|
|||Trigger Input to the DUT to capture presentation time. Based on<br>presentation control value of MAC_PPS_Control register, this signal can be<br>pulse or level signal. Width of this IO changes with the configured number<br>of PPS instances. See the device IOMUX sheet for details on the number of<br>these signals available.|
|phy_intf_sel_i[2:0]|I|PHY Interface Select.<br>This signal selects the PHY interface of the MAC:<br>• 000: GMII or MII<br>• 001: RGMII<br>• 100: RMII<br>This signal is sampled only during reset assertion, and it is ignored after that.<br>The reset is generated internally in the IP, and it gets activated when either<br>the input reset (pwr_on_rst_n) or the software reset is asserted.|
|phy_txen_o|O|PHY Transmit Data Enable.<br>The MAC drives this signal. This signal has multiple functions depending on<br>the selected PHY interface as described in the following list:<br>• GMII/MII: When high, indicates that valid data is being transmitted on<br>the phy_txd_o bus. Synchronous to: clk_tx_i<br>• RMII: When high, indicates that valid data is being transmitted on the<br>phy_txd_o bus. Synchronous to: clk_rmii_i<br>• RGMII: This signal is the control signal (rgmii_tctl) for the Transmit<br>data, and it is driven on both edges of the clock. Synchronous to:<br>clk_tx_i, clk_tx_180_i|
|phy_txer_o|O|PHY Transmit Error.<br>The MAC drives this signal. It has multiple functions depending on the<br>selected PHY interface as described in the following list:<br>• GMII: When this signal is high, it indicates a Transmit error or carrier<br>extension on the phy_txd_o bus. Synchronous to:clk_tx_i<br>• MII, RMII, RGMII: Not used and tied to low. According to the IEEE<br>standard, the TX_ER signal (phy_txer_o signal in the GMAC) is optional<br>in the MII mode. However, if you have enabled the Energy Efficient<br>Ethernet feature, the phy_txer_o signal is required.|
|phy_txd_o[7:0]|O<br>Tab|PHY Transmit Data.<br>This is a group of transmit data signals driven by the MAC. It has multiple<br>functions depending on the selected PHY interface as described in the<br>following list:<br>• GMII: All eight bits provide the GMII transmit data byte. The data<br>is valid only when the phy_txen_o and phy_txer_o signals are high.<br>Synchronous to: clk_tx_i<br>le continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3544 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 560. Module signals (continued) 

|Port Name|I/O<br>Description|
|---|---|
||• MII: Bits[3:0] provide the MII transmit data nibble. The data is valid only<br>when the phy_txen_o and phy_txer_o signals are high. Synchro-nous<br>to: clk_tx_i<br>• RGMII: Bits[3:0] provide the RGMII transmit data. The data bus changes<br>with both rising and falling edges of the transmit clock (clk_tx_i). The<br>data is valid only when the phy_txen_o signal is high. Synchronous to:<br>clk_tx_i and clk_tx_180_i<br>• RMII: Bits[1:0] provide the RMII transmit data. The data is valid only<br>when the phy_txen_o signal is high. Synchronous to: clk_rmii_i|
|phy_crs_i|I<br>PHY CRS.<br>This signal is valid only in the GMII or MII mode. The PHY drives this signal<br>high when the Transmit or Receive medium is not idle. The PHY drives this<br>signal low when both Transmit and Receive mediums are idle. This signal is<br>not synchronous to any clock.|
|phy_col_i|I<br>PHY Collision.<br>This signal is valid only in the GMII or MII mode. The PHY drives this<br>signal high when a collision is detected on the medium. This signal is not<br>synchronous to any clock.|
|phy_rxdv_i|I<br>PHY Receive Data Valid.<br>The PHY drives this signal. It has multiple functions depending on the<br>selected PHY interface as described in the following list:<br>• GMII or MII: Indicates that the data on the phy_rxd_i bus is valid. It<br>remains high continuously from the first recovered byte or nibble of<br>the packet through the final recovered byte or nibble of the packet.<br>Synchronous to: clk_rx_i<br>• RGMII: This is the Receive control signal that is used to qualify the<br>data received phy_rxd_i. This signal is sampled both edges of the clock.<br>Synchronous to: clk_rx_i, clk_rx_180_i<br>• RMII: Contains the crs and data valid information of the Receive<br>interface. Synchronous to: clk_rmii_i|
|phy_rxer_i|I<br>PHY Receive Error.<br>The PHY drives this signal. It has multiple functions depending on the<br>selected PHY interface as described in the following list:<br>• GMII or MII: Indicates an error or carrier extension (in GMII) in the<br>received packet the phy_rxd_i bus. Synchronous to: clk_rx_i<br>• RGMII, RMII: This signal is not used.|
|phy_rxd_i[7:0]|I<br>PHY Receive Data.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3545 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 560. Module signals (continued) 

|Port Name|I/O|Description|
|---|---|---|
|||This is a group of data signals received from the PHY. It has multiple<br>functions depending on the selected PHY interface as described in the<br>following list:<br>• GMII: All eight bits provide the GMII receive data byte. The data is valid<br>only when the phy_rxdv_i and phy_rxer_i signals are high. Synchronous<br>to: clk_rx_i<br>• MII: Bits [3:0] provide the MII receive data nibble. The data is valid only<br>when the phy_rxdv_i and phy_rxer_i signals are high. Synchro-nous<br>to: clk_rx_i<br>• RGMII: Bits [3:0] provide the RGMII receive data. The data bus is<br>sampled with both rising and falling edges of the receive clock (clk_rx_i).<br>The data is valid only when the phy_rxdv_i signal is high. Synchronous<br>to: clk_rx_i, clk_rx_180_i<br>• RMII: Bits [1:0] provide the RMII receive data. he data is valid only when<br>the phy_rxdv_i signal is high. Synchronous to: clk_rmii_i|
|gmii_mdc_o|O|Management Data Clock.<br>The MAC provides timing reference for the gmii_mdi_i and gmii_mdo_o<br>signals on GMII or MII through this aperiodic clock. This clock is generated<br>from the application clock through a clock divider controlled by CR field of<br>MAC_MDIO_Address register.|
|gmii_mdi_i|I|Management Data In.<br>The PHY generates this signal to transfer register data during a read<br>operation. This signal is driven synchronously with the gmii_mdc_o clock.|
|gmii_mdo_o|O|Management Data Out.<br>The MAC uses this signal to transfer control and data information to<br>the PHY.|



## 75.7 GMAC register descriptions 

### 75.7.1 GMAC memory map 

~~<mark>NOTE</mark>~~ 

This chip has 16 KB allocated per Ethernet controller for configuration space. GMAC uses only 8 KB of this memory and the remaining 8 KB is reserved for future use. Writing to the reserved memory may lead to unintended behavior. 

GMAC base address: 4048_4000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|(MAC_Configuration)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3546 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|4h|(MAC_Ext_Configuration)|32|RW|0000_0000h|
|8h|(MAC_Packet_Filter)|32|RW|0000_0000h|
|Ch|(MAC_Watchdog_Timeout)|32|RW|0000_0000h|
|10h|(MAC_Hash_Table_Reg0)|32|RW|0000_0000h|
|14h|(MAC_Hash_Table_Reg1)|32|RW|0000_0000h|
|18h|(MAC_Hash_Table_Reg2)|32|RW|0000_0000h|
|1Ch|(MAC_Hash_Table_Reg3)|32|RW|0000_0000h|
|20h|(MAC_Hash_Table_Reg4)|32|RW|0000_0000h|
|24h|(MAC_Hash_Table_Reg5)|32|RW|0000_0000h|
|28h|(MAC_Hash_Table_Reg6)|32|RW|0000_0000h|
|2Ch|(MAC_Hash_Table_Reg7)|32|RW|0000_0000h|
|50h|(MAC_VLAN_Tag_Ctrl)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Data)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter0)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter1)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter10)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter11)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter12)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter13)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter14)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter15)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter16)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter17)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter18)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter19)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter2)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter20)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter21)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter22)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter23)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter24)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3547 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|54h|(MAC_VLAN_Tag_Filter25)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter26)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter27)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter28)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter29)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter3)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter30)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter31)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter4)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter5)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter6)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter7)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter8)|32|RW|0000_0000h|
|54h|(MAC_VLAN_Tag_Filter9)|32|RW|0000_0000h|
|58h|(MAC_VLAN_Hash_Table)|32|RW|0000_0000h|
|60h|(MAC_VLAN_Incl)|32|RW|0000_0000h|
|60h|(MAC_VLAN_Incl0)|32|RW|0000_0000h|
|60h|(MAC_VLAN_Incl1)|32|RW|0000_0000h|
|60h|(MAC_VLAN_Incl2)|32|RW|0000_0000h|
|60h|(MAC_VLAN_Incl3)|32|RW|0000_0000h|
|60h|(MAC_VLAN_Incl4)|32|RW|0000_0000h|
|60h|(MAC_VLAN_Incl5)|32|RW|0000_0000h|
|60h|(MAC_VLAN_Incl6)|32|RW|0000_0000h|
|60h|(MAC_VLAN_Incl7)|32|RW|0000_0000h|
|64h|(MAC_Inner_VLAN_Incl)|32|RW|0000_0000h|
|70h|(MAC_Q0_Tx_Flow_Ctrl)|32|RW|0000_0000h|
|74h|(MAC_Q1_Tx_Flow_Ctrl)|32|RW|0000_0000h|
|78h|(MAC_Q2_Tx_Flow_Ctrl)|32|RW|0000_0000h|
|90h|(MAC_Rx_Flow_Ctrl)|32|RW|0000_0000h|
|94h|(MAC_RxQ_Ctrl4)|32|RW|0000_0000h|
|98h|(MAC_TxQ_Prty_Map0)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3548 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|A0h|(MAC_RxQ_Ctrl0)|32|RW|0000_0000h|
|A4h|(MAC_RxQ_Ctrl1)|32|RW|0000_0000h|
|A8h|(MAC_RxQ_Ctrl2)|32|RW|0000_0000h|
|B0h|(MAC_Interrupt_Status)|32|RO|0000_0000h|
|B4h|(MAC_Interrupt_Enable)|32|RW|0000_0000h|
|B8h|(MAC_Rx_Tx_Status)|32|RO|0000_0000h|
|F8h|(MAC_PHYIF_Control_Status)|32|RW|0000_0000h|
|110h|(MAC_Version)|32|RO|0000_1052h|
|114h|(MAC_Debug)|32|RO|0000_0000h|
|11Ch|(MAC_HW_Feature0)|32|RO|0E09_5337h|
|120h|(MAC_HW_Feature1)|32|RO|431B_29E7h|
|124h|(MAC_HW_Feature2)|32|RO|0408_2082h|
|128h|(MAC_HW_Feature3)|32|RO|2C37_1635h|
|140h|(MAC_DPP_FSM_Interrupt_Status)|32|RW|0000_0000h|
|148h|(MAC_FSM_Control)|32|RW|0000_0000h|
|14Ch|(MAC_FSM_ACT_Timer)|32|RW|0000_0000h|
|150h|(SCS_REG1)|32|RW|0000_0000h|
|200h|(MAC_MDIO_Address)|32|RW|0000_0000h|
|204h|(MAC_MDIO_Data)|32|RW|0000_0000h|
|210h|(MAC_ARP_Address)|32|RW|0000_0000h|
|230h|(MAC_CSR_SW_Ctrl)|32|RW|0000_0000h|
|234h|(MAC_FPE_CTRL_STS)|32|RW|0000_0000h|
|238h|(MAC_Ext_Cfg1)|32|RW|0002_0002h|
|240h|(MAC_Presn_Time_ns)|32|RO|0000_0000h|
|244h|(MAC_Presn_Time_Updt)|32|RW|0000_0000h|
|300h|(MAC_Address0_High)|32|RW|8000_FFFFh|
|304h|(MAC_Address0_Low)|32|RW|FFFF_FFFFh|
|308h|(MAC_Address1_High)|32|RW|0000_FFFFh|
|30Ch|(MAC_Address1_Low)|32|RW|FFFF_FFFFh|
|310h|(MAC_Address2_High)|32|RW|0000_FFFFh|
|314h|(MAC_Address2_Low)|32|RW|FFFF_FFFFh|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3549 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|700h|(MMC_Control)|32|RW|0000_0000h|
|704h|(MMC_Rx_Interrupt)|32|RO|0000_0000h|
|708h|(MMC_Tx_Interrupt)|32|RO|0000_0000h|
|70Ch|(MMC_Rx_Interrupt_Mask)|32|RW|0000_0000h|
|710h|(MMC_Tx_Interrupt_Mask)|32|RW|0000_0000h|
|714h|(Tx_Octet_Count_Good_Bad)|32|RO|0000_0000h|
|718h|(Tx_Packet_Count_Good_Bad)|32|RO|0000_0000h|
|71Ch|(Tx_Broadcast_Packets_Good)|32|RO|0000_0000h|
|720h|(Tx_Multicast_Packets_Good)|32|RO|0000_0000h|
|724h|(Tx_64Octets_Packets_Good_Bad)|32|RO|0000_0000h|
|728h|(Tx_65To127Octets_Packets_Good_Bad)|32|RO|0000_0000h|
|72Ch|(Tx_128To255Octets_Packets_Good_Bad)|32|RO|0000_0000h|
|730h|(Tx_256To511Octets_Packets_Good_Bad)|32|RO|0000_0000h|
|734h|(Tx_512To1023Octets_Packets_Good_Bad)|32|RO|0000_0000h|
|738h|(Tx_1024ToMaxOctets_Packets_Good_Bad)|32|RO|0000_0000h|
|73Ch|(Tx_Unicast_Packets_Good_Bad)|32|RO|0000_0000h|
|740h|(Tx_Multicast_Packets_Good_Bad)|32|RO|0000_0000h|
|744h|(Tx_Broadcast_Packets_Good_Bad)|32|RO|0000_0000h|
|748h|(Tx_Underflow_Error_Packets)|32|RO|0000_0000h|
|74Ch|(Tx_Single_Collision_Good_Packets)|32|RO|0000_0000h|
|750h|(Tx_Multiple_Collision_Good_Packets)|32|RO|0000_0000h|
|754h|(Tx_Deferred_Packets)|32|RO|0000_0000h|
|758h|(Tx_Late_Collision_Packets)|32|RO|0000_0000h|
|75Ch|(Tx_Excessive_Collision_Packets)|32|RO|0000_0000h|
|760h|(Tx_Carrier_Error_Packets)|32|RO|0000_0000h|
|764h|(Tx_Octet_Count_Good)|32|RO|0000_0000h|
|768h|(Tx_Packet_Count_Good)|32|RO|0000_0000h|
|76Ch|(Tx_Excessive_Deferral_Error)|32|RO|0000_0000h|
|770h|(Tx_Pause_Packets)|32|RO|0000_0000h|
|774h|(Tx_VLAN_Packets_Good)|32|RO|0000_0000h|
|778h|(Tx_OSize_Packets_Good)|32|RO|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3550 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|780h|(Rx_Packets_Count_Good_Bad)|32|RO|0000_0000h|
|784h|(Rx_Octet_Count_Good_Bad)|32|RO|0000_0000h|
|788h|(Rx_Octet_Count_Good)|32|RO|0000_0000h|
|78Ch|(Rx_Broadcast_Packets_Good)|32|RO|0000_0000h|
|790h|(Rx_Multicast_Packets_Good)|32|RO|0000_0000h|
|794h|(Rx_CRC_Error_Packets)|32|RO|0000_0000h|
|798h|(Rx_Alignment_Error_Packets)|32|RO|0000_0000h|
|79Ch|(Rx_Runt_Error_Packets)|32|RO|0000_0000h|
|7A0h|(Rx_Jabber_Error_Packets)|32|RO|0000_0000h|
|7A4h|(Rx_Undersize_Packets_Good)|32|RO|0000_0000h|
|7A8h|(Rx_Oversize_Packets_Good)|32|RO|0000_0000h|
|7ACh|(Rx_64Octets_Packets_Good_Bad)|32|RO|0000_0000h|
|7B0h|(Rx_65To127Octets_Packets_Good_Bad)|32|RO|0000_0000h|
|7B4h|(Rx_128To255Octets_Packets_Good_Bad)|32|RO|0000_0000h|
|7B8h|(Rx_256To511Octets_Packets_Good_Bad)|32|RO|0000_0000h|
|7BCh|(Rx_512To1023Octets_Packets_Good_Bad)|32|RO|0000_0000h|
|7C0h|(Rx_1024ToMaxOctets_Packets_Good_Bad)|32|RO|0000_0000h|
|7C4h|(Rx_Unicast_Packets_Good)|32|RO|0000_0000h|
|7C8h|(Rx_Length_Error_Packets)|32|RO|0000_0000h|
|7CCh|(Rx_Out_Of_Range_Type_Packets)|32|RO|0000_0000h|
|7D0h|(Rx_Pause_Packets)|32|RO|0000_0000h|
|7D4h|(Rx_FIFO_Overflow_Packets)|32|RO|0000_0000h|
|7D8h|(Rx_VLAN_Packets_Good_Bad)|32|RO|0000_0000h|
|7DCh|(Rx_Watchdog_Error_Packets)|32|RO|0000_0000h|
|7E0h|(Rx_Receive_Error_Packets)|32|RO|0000_0000h|
|7E4h|(Rx_Control_Packets_Good)|32|RO|0000_0000h|
|8A0h|(MMC_FPE_Tx_Interrupt)|32|RO|0000_0000h|
|8A4h|(MMC_FPE_Tx_Interrupt_Mask)|32|RW|0000_0000h|
|8A8h|(MMC_Tx_FPE_Fragment_Cntr)|32|RO|0000_0000h|
|8ACh|(MMC_Tx_Hold_Req_Cntr)|32|RO|0000_0000h|
|8C0h|(MMC_FPE_Rx_Interrupt)|32|RO|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3551 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|8C4h|(MMC_FPE_Rx_Interrupt_Mask)|32|RW|0000_0000h|
|8C8h|(MMC_Rx_Packet_Assembly_Err_Cntr)|32|RO|0000_0000h|
|8CCh|(MMC_Rx_Packet_SMD_Err_Cntr)|32|RO|0000_0000h|
|8D0h|(MMC_Rx_Packet_Assembly_OK_Cntr)|32|RO|0000_0000h|
|8D4h|(MMC_Rx_FPE_Fragment_Cntr)|32|RO|0000_0000h|
|900h|(MAC_L3_L4_Control0)|32|RW|0000_0000h|
|904h|(MAC_Layer4_Address0)|32|RW|0000_0000h|
|910h|(MAC_Layer3_Addr0_Reg0)|32|RW|0000_0000h|
|914h|(MAC_Layer3_Addr1_Reg0)|32|RW|0000_0000h|
|918h|(MAC_Layer3_Addr2_Reg0)|32|RW|0000_0000h|
|91Ch|(MAC_Layer3_Addr3_Reg0)|32|RW|0000_0000h|
|930h|(MAC_L3_L4_Control1)|32|RW|0000_0000h|
|934h|(MAC_Layer4_Address1)|32|RW|0000_0000h|
|940h|(MAC_Layer3_Addr0_Reg1)|32|RW|0000_0000h|
|944h|(MAC_Layer3_Addr1_Reg1)|32|RW|0000_0000h|
|948h|(MAC_Layer3_Addr2_Reg1)|32|RW|0000_0000h|
|94Ch|(MAC_Layer3_Addr3_Reg1)|32|RW|0000_0000h|
|960h|(MAC_L3_L4_Control2)|32|RW|0000_0000h|
|964h|(MAC_Layer4_Address2)|32|RW|0000_0000h|
|970h|(MAC_Layer3_Addr0_Reg2)|32|RW|0000_0000h|
|974h|(MAC_Layer3_Addr1_Reg2)|32|RW|0000_0000h|
|978h|(MAC_Layer3_Addr2_Reg2)|32|RW|0000_0000h|
|97Ch|(MAC_Layer3_Addr3_Reg2)|32|RW|0000_0000h|
|990h|(MAC_L3_L4_Control3)|32|RW|0000_0000h|
|994h|(MAC_Layer4_Address3)|32|RW|0000_0000h|
|9A0h|(MAC_Layer3_Addr0_Reg3)|32|RW|0000_0000h|
|9A4h|(MAC_Layer3_Addr1_Reg3)|32|RW|0000_0000h|
|9A8h|(MAC_Layer3_Addr2_Reg3)|32|RW|0000_0000h|
|9ACh|(MAC_Layer3_Addr3_Reg3)|32|RW|0000_0000h|
|9C0h|(MAC_L3_L4_Control4)|32|RW|0000_0000h|
|9C4h|(MAC_Layer4_Address4)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3552 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|9D0h|(MAC_Layer3_Addr0_Reg4)|32|RW|0000_0000h|
|9D4h|(MAC_Layer3_Addr1_Reg4)|32|RW|0000_0000h|
|9D8h|(MAC_Layer3_Addr2_Reg4)|32|RW|0000_0000h|
|9DCh|(MAC_Layer3_Addr3_Reg4)|32|RW|0000_0000h|
|9F0h|(MAC_L3_L4_Control5)|32|RW|0000_0000h|
|9F4h|(MAC_Layer4_Address5)|32|RW|0000_0000h|
|A00h|(MAC_Layer3_Addr0_Reg5)|32|RW|0000_0000h|
|A04h|(MAC_Layer3_Addr1_Reg5)|32|RW|0000_0000h|
|A08h|(MAC_Layer3_Addr2_Reg5)|32|RW|0000_0000h|
|A0Ch|(MAC_Layer3_Addr3_Reg5)|32|RW|0000_0000h|
|A20h|(MAC_L3_L4_Control6)|32|RW|0000_0000h|
|A24h|(MAC_Layer4_Address6)|32|RW|0000_0000h|
|A30h|(MAC_Layer3_Addr0_Reg6)|32|RW|0000_0000h|
|A34h|(MAC_Layer3_Addr1_Reg6)|32|RW|0000_0000h|
|A38h|(MAC_Layer3_Addr2_Reg6)|32|RW|0000_0000h|
|A3Ch|(MAC_Layer3_Addr3_Reg6)|32|RW|0000_0000h|
|A50h|(MAC_L3_L4_Control7)|32|RW|0000_0000h|
|A54h|(MAC_Layer4_Address7)|32|RW|0000_0000h|
|A60h|(MAC_Layer3_Addr0_Reg7)|32|RW|0000_0000h|
|A64h|(MAC_Layer3_Addr1_Reg7)|32|RW|0000_0000h|
|A68h|(MAC_Layer3_Addr2_Reg7)|32|RW|0000_0000h|
|A6Ch|(MAC_Layer3_Addr3_Reg7)|32|RW|0000_0000h|
|A70h|(MAC_Indir_Access_Ctrl)|32|RW|0000_0000h|
|A74h|(MAC_Indir_Access_Data)|32|RW|0000_0000h|
|A74h|(MAC_TMRQ_Regs0)|32|RW|0000_0000h|
|A74h|(MAC_TMRQ_Regs1)|32|RW|0000_0000h|
|A74h|(MAC_TMRQ_Regs2)|32|RW|0000_0000h|
|A74h|(MAC_TMRQ_Regs3)|32|RW|0000_0000h|
|A74h|(MAC_TMRQ_Regs4)|32|RW|0000_0000h|
|A74h|(MAC_TMRQ_Regs5)|32|RW|0000_0000h|
|A74h|(MAC_TMRQ_Regs6)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3553 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|A74h|(MAC_TMRQ_Regs7)|32|RW|0000_0000h|
|B00h|(MAC_Timestamp_Control)|32|RW|0000_2000h|
|B04h|(MAC_Sub_Second_Increment)|32|RW|0000_0000h|
|B08h|(MAC_System_Time_Seconds)|32|RO|0000_0000h|
|B0Ch|(MAC_System_Time_Nanoseconds)|32|RO|0000_0000h|
|B10h|(MAC_System_Time_Seconds_Update)|32|RW|0000_0000h|
|B14h|(MAC_System_Time_Nanoseconds_Update)|32|RW|0000_0000h|
|B18h|(MAC_Timestamp_Addend)|32|RW|0000_0000h|
|B1Ch|(MAC_System_Time_Higher_Word_Seconds)|32|RW|0000_0000h|
|B20h|(MAC_Timestamp_Status)|32|RO|0000_0000h|
|B30h|(MAC_Tx_Timestamp_Status_Nanoseconds)|32|RO|0000_0000h|
|B34h|(MAC_Tx_Timestamp_Status_Seconds)|32|RO|0000_0000h|
|B50h|(MAC_Timestamp_Ingress_Asym_Corr)|32|RW|0000_0000h|
|B54h|(MAC_Timestamp_Egress_Asym_Corr)|32|RW|0000_0000h|
|B58h|(MAC_Timestamp_Ingress_Corr_Nanosecond)|32|RW|0000_0000h|
|B5Ch|(MAC_Timestamp_Egress_Corr_Nanosecond)|32|RW|0000_0000h|
|B60h|(MAC_Timestamp_Ingress_Corr_Subnanosec)|32|RW|0000_0000h|
|B64h|(MAC_Timestamp_Egress_Corr_Subnanosec)|32|RW|0000_0000h|
|B68h|(MAC_Timestamp_Ingress_Latency)|32|RO|0000_0000h|
|B6Ch|(MAC_Timestamp_Egress_Latency)|32|RO|0000_0000h|
|B70h|(MAC_PPS_Control)|32|RW|0000_0000h|
|B80h|(MAC_PPS0_Target_Time_Seconds)|32|RW|0000_0000h|
|B84h|(MAC_PPS0_Target_Time_Nanoseconds)|32|RW|0000_0000h|
|B88h|(MAC_PPS0_Interval)|32|RW|0000_0000h|
|B8Ch|(MAC_PPS0_Width)|32|RW|0000_0000h|
|B90h|(MAC_PPS1_Target_Time_Seconds)|32|RW|0000_0000h|
|B94h|(MAC_PPS1_Target_Time_Nanoseconds)|32|RW|0000_0000h|
|B98h|(MAC_PPS1_Interval)|32|RW|0000_0000h|
|B9Ch|(MAC_PPS1_Width)|32|RW|0000_0000h|
|BA0h|(MAC_PPS2_Target_Time_Seconds)|32|RW|0000_0000h|
|BA4h|(MAC_PPS2_Target_Time_Nanoseconds)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3554 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|BA8h|(MAC_PPS2_Interval)|32|RW|0000_0000h|
|BACh|(MAC_PPS2_Width)|32|RW|0000_0000h|
|BB0h|(MAC_PPS3_Target_Time_Seconds)|32|RW|0000_0000h|
|BB4h|(MAC_PPS3_Target_Time_Nanoseconds)|32|RW|0000_0000h|
|BB8h|(MAC_PPS3_Interval)|32|RW|0000_0000h|
|BBCh|(MAC_PPS3_Width)|32|RW|0000_0000h|
|C00h|(MTL_Operation_Mode)|32|RW|0000_0000h|
|C08h|(MTL_DBG_CTL)|32|RW|0000_0000h|
|C0Ch|(MTL_DBG_STS)|32|RW|0000_0018h|
|C10h|(MTL_FIFO_Debug_Data)|32|RW|0000_0000h|
|C20h|(MTL_Interrupt_Status)|32|RO|0000_0000h|
|C30h|(MTL_RxQ_DMA_Map0)|32|RW|0000_0000h|
|C40h|(MTL_TBS_CTRL)|32|RW|0000_0000h|
|C50h|(MTL_EST_Control)|32|RW|0000_0000h|
|C54h|(MTL_EST_Ext_Control)|32|RW|0000_0000h|
|C58h|(MTL_EST_Status)|32|RW|0000_0000h|
|C60h|(MTL_EST_Sch_Error)|32|RW|0000_0000h|
|C64h|(MTL_EST_Frm_Size_Error)|32|RW|0000_0000h|
|C68h|(MTL_EST_Frm_Size_Capture)|32|RO|0000_0000h|
|C70h|(MTL_EST_Intr_Enable)|32|RW|0000_0000h|
|C80h|(MTL_EST_GCL_Control)|32|RW|0000_0000h|
|C84h|(MTL_EST_GCL_Data)|32|RW|0000_0000h|
|C90h|(MTL_FPE_CTRL_STS)|32|RW|0000_0000h|
|C94h|(MTL_FPE_Advance)|32|RW|0000_0000h|
|CA0h|(MTL_RXP_Control_Status)|32|RW|803F_003Fh|
|CA4h|(MTL_RXP_Interrupt_Control_Status)|32|RW|0000_0000h|
|CA8h|(MTL_RXP_Drop_Cnt)|32|RO|0000_0000h|
|CACh|(MTL_RXP_Error_Cnt)|32|RO|0000_0000h|
|CB0h|(MTL_RXP_Indirect_Acc_Control_Status)|32|RW|0000_0000h|
|CB4h|(MTL_RXP_Indirect_Acc_Data)|32|RO|0000_0000h|
|CB8h|(MTL_RXP_Bypass_Cnt)|32|RO|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3555 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|CC0h|(MTL_ECC_Control)|32|RW|0000_000Fh|
|CC4h|(MTL_Safety_Interrupt_Status)|32|RO|0000_0000h|
|CC8h|(MTL_ECC_Interrupt_Enable)|32|RW|0000_1111h|
|CCCh|(MTL_ECC_Interrupt_Status)|32|RW|0000_0000h|
|CD0h|(MTL_ECC_Err_Sts_Rctl)|32|RW|0000_0000h|
|CD4h|(MTL_ECC_Err_Addr_Status)|32|RO|0000_0000h|
|CD8h|(MTL_ECC_Err_Cntr_Status)|32|RO|0000_0000h|
|CE0h|(MTL_DPP_Control)|32|RW|0000_0003h|
|CE4h|(MTL_DPP_ECC_EIC)|32|RW|0000_0000h|
|D00h|(MTL_TxQ0_Operation_Mode)|32|RW|0000_0000h|
|D04h|(MTL_TxQ0_Underflow)|32|RO|0000_0000h|
|D08h|(MTL_TxQ0_Debug)|32|RO|0000_0000h|
|D14h|(MTL_TxQ0_ETS_Status)|32|RO|0000_0000h|
|D18h|(MTL_TxQ0_Quantum_Weight)|32|RW|0000_0000h|
|D2Ch|(MTL_Q0_Interrupt_Control_Status)|32|RW|0000_0000h|
|D30h|(MTL_RxQ0_Operation_Mode)|32|RW|0000_0000h|
|D34h|(MTL_RxQ0_Missed_Packet_Overflow_Cnt)|32|RO|0000_0000h|
|D38h|(MTL_RxQ0_Debug)|32|RO|0000_0000h|
|D3Ch|(MTL_RxQ0_Control)|32|RW|0000_0000h|
|D40h|(MTL_TxQ1_Operation_Mode)|32|RW|0000_0000h|
|D44h|(MTL_TxQ1_Underflow)|32|RO|0000_0000h|
|D48h|(MTL_TxQ1_Debug)|32|RO|0000_0000h|
|D50h|(MTL_TxQ1_ETS_Control)|32|RW|0000_0000h|
|D54h|(MTL_TxQ1_ETS_Status)|32|RO|0000_0000h|
|D58h|(MTL_TxQ1_Quantum_Weight)|32|RW|0000_0000h|
|D5Ch|(MTL_TxQ1_SendSlopeCredit)|32|RW|0000_0000h|
|D60h|(MTL_TxQ1_HiCredit)|32|RW|0000_0000h|
|D64h|(MTL_TxQ1_LoCredit)|32|RW|0000_0000h|
|D6Ch|(MTL_Q1_Interrupt_Control_Status)|32|RW|0000_0000h|
|D70h|(MTL_RxQ1_Operation_Mode)|32|RW|0000_0000h|
|D74h|(MTL_RxQ1_Missed_Packet_Overflow_Cnt)|32|RO|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3556 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|D78h|(MTL_RxQ1_Debug)|32|RO|0000_0000h|
|D7Ch|(MTL_RxQ1_Control)|32|RW|0000_0000h|
|D80h|(MTL_TxQ2_Operation_Mode)|32|RW|0000_0000h|
|D84h|(MTL_TxQ2_Underflow)|32|RO|0000_0000h|
|D88h|(MTL_TxQ2_Debug)|32|RO|0000_0000h|
|D90h|(MTL_TxQ2_ETS_Control)|32|RW|0000_0000h|
|D94h|(MTL_TxQ2_ETS_Status)|32|RO|0000_0000h|
|D98h|(MTL_TxQ2_Quantum_Weight)|32|RW|0000_0000h|
|D9Ch|(MTL_TxQ2_SendSlopeCredit)|32|RW|0000_0000h|
|DA0h|(MTL_TxQ2_HiCredit)|32|RW|0000_0000h|
|DA4h|(MTL_TxQ2_LoCredit)|32|RW|0000_0000h|
|DACh|(MTL_Q2_Interrupt_Control_Status)|32|RW|0000_0000h|
|DB0h|(MTL_RxQ2_Operation_Mode)|32|RW|0000_0000h|
|DB4h|(MTL_RxQ2_Missed_Packet_Overflow_Cnt)|32|RO|0000_0000h|
|DB8h|(MTL_RxQ2_Debug)|32|RO|0000_0000h|
|DBCh|(MTL_RxQ2_Control)|32|RW|0000_0000h|
|1000h|(DMA_Mode)|32|RW|0000_0000h|
|1004h|(DMA_SysBus_Mode)|32|RW|0000_0000h|
|1008h|(DMA_Interrupt_Status)|32|RO|0000_0000h|
|100Ch|(DMA_Debug_Status0)|32|RO|0000_0000h|
|1050h|(DMA_TBS_CTRL0)|32|RW|0000_0000h|
|1054h|(DMA_TBS_CTRL1)|32|RW|0000_0000h|
|1058h|(DMA_TBS_CTRL2)|32|RW|0000_0000h|
|105Ch|(DMA_TBS_CTRL3)|32|RW|0000_0000h|
|1080h|(DMA_Safety_Interrupt_Status)|32|RO|0000_0000h|
|1100h|(DMA_CH0_Control)|32|RW|0000_0000h|
|1104h|(DMA_CH0_Tx_Control)|32|RW|0000_0000h|
|1108h|(DMA_CH0_Rx_Control)|32|RW|0000_0000h|
|1114h|(DMA_CH0_TxDesc_List_Address)|32|RW|0000_0000h|
|111Ch|(DMA_CH0_RxDesc_List_Address)|32|RW|0000_0000h|
|1120h|(DMA_CH0_TxDesc_Tail_Pointer)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3557 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|1128h|(DMA_CH0_RxDesc_Tail_Pointer)|32|RW|0000_0000h|
|112Ch|(DMA_CH0_TxDesc_Ring_Length)|32|RW|0000_0000h|
|1130h|(DMA_CH0_Rx_Control2)|32|RW|0000_0000h|
|1134h|(DMA_CH0_Interrupt_Enable)|32|RW|0000_0000h|
|1138h|(DMA_CH0_Rx_Interrupt_Watchdog_Timer)|32|RW|0000_0000h|
|113Ch|(DMA_CH0_Slot_Function_Control_Status)|32|RW|0000_07C0h|
|1144h|(DMA_CH0_Current_App_TxDesc)|32|RO|0000_0000h|
|114Ch|(DMA_CH0_Current_App_RxDesc)|32|RO|0000_0000h|
|1154h|(DMA_CH0_Current_App_TxBuffer)|32|RO|0000_0000h|
|115Ch|(DMA_CH0_Current_App_RxBuffer)|32|RO|0000_0000h|
|1160h|(DMA_CH0_Status)|32|RW|0000_0000h|
|1164h|(DMA_CH0_Miss_Frame_Cnt)|32|RO|0000_0000h|
|1168h|(DMA_CH0_RXP_Accept_Cnt)|32|RO|0000_0000h|
|116Ch|(DMA_CH0_RX_ERI_Cnt)|32|RO|0000_0000h|
|1180h|(DMA_CH1_Control)|32|RW|0000_0000h|
|1184h|(DMA_CH1_Tx_Control)|32|RW|0000_0000h|
|1188h|(DMA_CH1_Rx_Control)|32|RW|0000_0000h|
|1194h|(DMA_CH1_TxDesc_List_Address)|32|RW|0000_0000h|
|119Ch|(DMA_CH1_RxDesc_List_Address)|32|RW|0000_0000h|
|11A0h|(DMA_CH1_TxDesc_Tail_Pointer)|32|RW|0000_0000h|
|11A8h|(DMA_CH1_RxDesc_Tail_Pointer)|32|RW|0000_0000h|
|11ACh|(DMA_CH1_TxDesc_Ring_Length)|32|RW|0000_0000h|
|11B0h|(DMA_CH1_Rx_Control2)|32|RW|0000_0000h|
|11B4h|(DMA_CH1_Interrupt_Enable)|32|RW|0000_0000h|
|11B8h|(DMA_CH1_Rx_Interrupt_Watchdog_Timer)|32|RW|0000_0000h|
|11BCh|(DMA_CH1_Slot_Function_Control_Status)|32|RW|0000_07C0h|
|11C4h|(DMA_CH1_Current_App_TxDesc)|32|RO|0000_0000h|
|11CCh|(DMA_CH1_Current_App_RxDesc)|32|RO|0000_0000h|
|11D4h|(DMA_CH1_Current_App_TxBuffer)|32|RO|0000_0000h|
|11DCh|(DMA_CH1_Current_App_RxBuffer)|32|RO|0000_0000h|
|11E0h|(DMA_CH1_Status)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3558 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|11E4h|(DMA_CH1_Miss_Frame_Cnt)|32|RO|0000_0000h|
|11E8h|(DMA_CH1_RXP_Accept_Cnt)|32|RO|0000_0000h|
|11ECh|(DMA_CH1_RX_ERI_Cnt)|32|RO|0000_0000h|
|1200h|(DMA_CH2_Control)|32|RW|0000_0000h|
|1204h|(DMA_CH2_Tx_Control)|32|RW|0000_0000h|
|1208h|(DMA_CH2_Rx_Control)|32|RW|0000_0000h|
|1214h|(DMA_CH2_TxDesc_List_Address)|32|RW|0000_0000h|
|121Ch|(DMA_CH2_RxDesc_List_Address)|32|RW|0000_0000h|
|1220h|(DMA_CH2_TxDesc_Tail_Pointer)|32|RW|0000_0000h|
|1228h|(DMA_CH2_RxDesc_Tail_Pointer)|32|RW|0000_0000h|
|122Ch|(DMA_CH2_TxDesc_Ring_Length)|32|RW|0000_0000h|
|1230h|(DMA_CH2_Rx_Control2)|32|RW|0000_0000h|
|1234h|(DMA_CH2_Interrupt_Enable)|32|RW|0000_0000h|
|1238h|(DMA_CH2_Rx_Interrupt_Watchdog_Timer)|32|RW|0000_0000h|
|123Ch|(DMA_CH2_Slot_Function_Control_Status)|32|RW|0000_07C0h|
|1244h|(DMA_CH2_Current_App_TxDesc)|32|RO|0000_0000h|
|124Ch|(DMA_CH2_Current_App_RxDesc)|32|RO|0000_0000h|
|1254h|(DMA_CH2_Current_App_TxBuffer)|32|RO|0000_0000h|
|125Ch|(DMA_CH2_Current_App_RxBuffer)|32|RO|0000_0000h|
|1260h|(DMA_CH2_Status)|32|RW|0000_0000h|
|1264h|(DMA_CH2_Miss_Frame_Cnt)|32|RO|0000_0000h|
|1268h|(DMA_CH2_RXP_Accept_Cnt)|32|RO|0000_0000h|
|126Ch|(DMA_CH2_RX_ERI_Cnt)|32|RO|0000_0000h|



### 75.7.2 (MAC_Configuration) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Configuration|0h|



Function 

The MAC Configuration Register establishes the operating mode of the MAC. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3559 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3560-02.png)


<!-- Start of picture text -->
Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R ARPE GPSL<br>SARC  IPC  IPG  S2KP  CST  ACS  WD  BE  JD  JE<br>W N  CE<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv<br>R PS  FES  DM  LM  ECRS DO  DCRS  DR  e... BL  DC  PRELEN  TE  RE<br>FD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31<br>ARPEN|ARP Offload Enable When this bit is set, the MAC can recognize an incoming ARP request packet<br>and schedules the ARP packet for transmission. It forwards the ARP packet to the application and also<br>indicate the events in the RxStatus. When this bit is reset, the MAC receiver does not recognize any<br>ARP packet and indicates them as Type frame in the RxStatus. This bit is available only when the<br>Enable IPv4 ARP Offload is selected.<br>0b - ARP Offload is disabled<br>1b - ARP Offload is enabled|
|30-28<br>SARC|Source Address Insertion or Replacement Control This field controls the source address insertion or<br>replacement for all transmitted packets. Bit 30 specifies which MAC Address register (0 or 1) is used for<br>source address insertion or replacement based on the values of Bits[29:28]: 2'b0x: - The mti_sa_ctrl_i<br>and ati_sa_ctrl_i input signals control the SA field generation. 2'b10: - If Bit 30 is set to 0, the MAC inserts<br>the content of the MAC Address 0 registers in the SA field of all transmitted packets. - If Bit 30 is set to<br>1 and the Enable MAC Address Register 1 option is selected while configuring the IP, the MAC inserts<br>the content of the MAC Address 1 registers in the SA field of all transmitted packets. 2'b11: - If Bit 30 is<br>set to 0, the MAC replaces the content of the MAC Address 0 registers in the SA field of all transmitted<br>packets. - If Bit 30 is set to 1 and the MAC Address Register 1 is enabled, the MAC replaces the content<br>of the MAC Address 1 registers in the SA field of all transmitted packets. Note: Changes to this field take<br>effect only on the start of a packet. If you write to this register field when a packet is being transmitted,<br>only the subsequent packet can use the updated value, that is, the current packet does not use the<br>updated value.<br>000b - mti_sa_ctrl_i and ati_sa_ctrl_i input signals control the SA field generation<br>010b - Contents of MAC Addr-0 inserted in SA field<br>011b - Contents of MAC Addr-0 replaces SA field<br>110b - Contents of MAC Addr-1 inserted in SA field<br>111b - Contents of MAC Addr-1 replaces SA field|
|27<br>IPC|Checksum Offload When set, this bit enables the IPv4 header checksum checking and IPv4 or IPv6<br>TCP, UDP, or ICMP payload checksum checking. When this bit is reset, the COE function in the receiver<br>is disabled. The Layer 3 and Layer 4 Packet Filter and Enable Split Header features automatically|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3560 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function<br>selects the IPC Full Checksum Offload Engine on the Receive side. When any of these features are<br>enabled, you must set the IPC bit.<br>0b - IP header/payload checksum checking is disabled<br>1b - IP header/payload checksum checking is enabled|
|---|---|
|26-24<br>IPG|Inter-Packet Gap These bits control the minimum IPG between packets during transmission. This<br>range of minimum IPG is valid in full-duplex mode. In the half-duplex mode, the minimum IPG can<br>be configured only for 64-bit times (IPG = 100). Lower values are not considered. When a JAM pattern<br>is being transmitted because of backpressure activation, the MAC does not consider the minimum IPG.<br>This function (IPG less than 96 bit times) is valid only when EIPGEN bit in MAC_Ext_Configuration<br>register is reset. When EIPGEN is set, then the minimum IPG (greater than 96 bit times) is controlled as<br>per the description given in EIPG field in MAC_Ext_Configuration register.<br>000b - 96 bit times IPG<br>001b - 88 bit times IPG<br>010b - 80 bit times IPG<br>011b - 72 bit times IPG<br>100b - 64 bit times IPG<br>101b - 56 bit times IPG<br>110b - 48 bit times IPG<br>111b - 40 bit times IPG|
|23<br>GPSLCE|Giant Packet Size Limit Control Enable When this bit is set, the MAC considers the value in GPSL<br>field in MAC_Ext_Configuration register to declare a received packet as Giant packet. This field must be<br>programmed to more than 1,518 bytes. Otherwise, the MAC considers 1,518 bytes as giant packet limit.<br>When this bit is reset, the MAC considers a received packet as Giant packet when its size is greater<br>than 1,518 bytes (1522 bytes for tagged packet). The watchdog timeout limit, Jumbo Packet Enable<br>and 2K Packet Enable have higher precedence over this bit, that is the MAC considers a received<br>packet as Giant packet when its size is greater than 9,018 bytes (9,022 bytes for tagged packet) with<br>Jumbo Packet Enabled and greater than 2,000 bytes with 2K Packet Enabled. The watchdog timeout,<br>if enabled, terminates the received packet when watchdog limit is reached. Therefore, the programmed<br>giant packet limit should be less than the watchdog limit to get the giant packet status.<br>0b - Giant Packet Size Limit Control is disabled<br>1b - Giant Packet Size Limit Control is enabled|
|22<br>S2KP|IEEE 802.3as Support for 2K Packets When this bit is set, the MAC considers all packets with up to<br>2,000 bytes length as normal packets. When the JE bit is not set, the MAC considers all received<br>packets of size more than 2K bytes as Giant packets. When this bit is reset and the JE bit is not set,<br>the MAC considers all received packets of size more than 1,518 bytes (1,522 bytes for tagged) as giant<br>packets. For more information about how the setting of this bit and the JE bit impact the Giant packet<br>status, see the Table, Giant Packet Status based on S2KP and JE Bits. Note: When the JE bit is set,<br>setting this bit has no effect on the giant packet status.<br>0b - Support upto 2K packet is disabled<br>1b - Support upto 2K packet is Enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3561 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|21<br>CST|CRC stripping for Type packets When this bit is set, the last four bytes (FCS) of all packets of Ether type<br>(type field greater than 1,536) are stripped and dropped before forwarding the packet to the application.<br>Note: For information about how the settings of the ACS bit and this bit impact the packet length, see the<br>Table, Packet Length based on the CST and ACS Bits.<br>0b - CRC stripping for Type packets is disabled<br>1b - CRC stripping for Type packets is enabled|
|20<br>ACS|Automatic Pad or CRC Stripping When this bit is set, the MAC strips the Pad or FCS field on the<br>incoming packets only if the value of the length field is less than 1,536 bytes. All received packets with<br>length field greater than or equal to 1,536 bytes are passed to the application without stripping the Pad<br>or FCS field. When this bit is reset, the MAC passes all incoming packets to the application, without<br>any modification. Note: For information about how the settings of CST bit and this bit impact the packet<br>length, see the Table, Packet Length based on the CST and ACS Bit .<br>0b - Automatic Pad or CRC Stripping is disabled<br>1b - Automatic Pad or CRC Stripping is enabled|
|19<br>WD|Watchdog Disable When this bit is set, the MAC disables the watchdog timer on the receiver. The MAC<br>can receive packets of up to 16,383 bytes. When this bit is reset, the MAC does not allow more than<br>2,048 bytes (10,240 if JE is set high) of the packet being received. The MAC cuts off any bytes received<br>after 2,048 bytes.<br>0b - Watchdog is enabled<br>1b - Watchdog is disabled|
|18<br>BE|Packet Burst Enable When this bit is set, the MAC allows packet bursting during transmission in the GMII<br>half-duplex mode.<br>0b - Packet Burst is disabled<br>1b - Packet Burst is enabled|
|17<br>JD|Jabber Disable When this bit is set, the MAC disables the jabber timer on the transmitter. The MAC can<br>transfer packets of up to 16,383 bytes. When this bit is reset, if the application sends more than 2,048<br>bytes of data (10,240 if JE is set high) during transmission, the MAC does not send rest of the bytes in<br>that packet.<br>0b - Jabber is enabled<br>1b - Jabber is disabled|
|16<br>JE|Jumbo Packet Enable When this bit is set, the MAC allows jumbo packets of 9,018 bytes (9,022 bytes for<br>VLAN tagged packets) without reporting a giant packet error in the Rx packet status.<br>0b - Jumbo packet is disabled<br>1b - Jumbo packet is enabled|
|15<br>PS|Port Select This bit selects the Ethernet line speed. This bit, along with Bit 14, selects the exact line<br>speed. In the 10/100 Mbps-only (always 1) or 1000 Mbps-only (always 0) configurations, this bit is<br>read-only (RO) with appropriate value. In default 10/100/1000 Mbps configurations, this bit is read-write<br>(R/W). The mac_speed_o[1] signal reflects the value of this bit.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3562 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - For 1000 or 2500 Mbps operations<br>1b - For 10 or 100 Mbps operations|
|14<br>FES|Speed This bit selects the speed mode. The mac_speed_o[0] signal reflects the value of this bit.<br>0b - 10 Mbps when PS bit is 1 and 1 Gbps when PS bit is 0<br>1b - 100 Mbps when PS bit is 1 and 2.5 Gbps when PS bit is 0|
|13<br>DM|Duplex Mode When this bit is set, the MAC operates in the full-duplex mode in which it can transmit and<br>receive simultaneously. This bit is RO with default value of 1'b1 in the full-duplex-only configurations.<br>0b - Half-duplex mode<br>1b - Full-duplex mode|
|12<br>LM|Loopback Mode When this bit is set, the MAC operates in the loopback mode at GMII or MII. The (G)MII<br>Rx clock input (clk_rx_i) is required for the loopback to work properly. This is because the Tx clock is not<br>internally looped back.<br>0b - Loopback is disabled<br>1b - Loopback is enabled|
|11<br>ECRSFD|Enable Carrier Sense Before Transmission in Full-Duplex Mode When this bit is set, the MAC transmitter<br>checks the CRS signal before packet transmission in the full-duplex mode. The MAC starts the<br>transmission only when the CRS signal is low. When this bit is reset, the MAC transmitter ignores the<br>status of the CRS signal.<br>0b - ECRSFD is disabled<br>1b - ECRSFD is enabled|
|10<br>DO|Disable Receive Own When this bit is set, the MAC disables the reception of packets when the<br>gmii_txen_o is asserted in the half-duplex mode. When this bit is reset, the MAC receives all packets<br>given by the PHY. This bit is not applicable in the full-duplex mode.<br>0b - Enable Receive Own<br>1b - Disable Receive Own|
|9<br>DCRS|Disable Carrier Sense During Transmission When this bit is set, the MAC transmitter ignores the (G)MII<br>CRS signal during packet transmission in the half-duplex mode. As a result, no errors are generated<br>because of Loss of Carrier or No Carrier during transmission. When this bit is reset, the MAC transmitter<br>generates errors because of Carrier Sense. The MAC can even abort the transmission.<br>0b - Enable Carrier Sense During Transmission<br>1b - Disable Carrier Sense During Transmission|
|8<br>DR|Disable Retry When this bit is set, the MAC attempts only one transmission. When a collision occurs on<br>the GMII or MII interface, the MAC ignores the current packet transmission and reports a Packet Abort<br>with excessive collision error in the Tx packet status. When this bit is reset, the MAC retries based on the<br>settings of the BL field. This bit is applicable only in the half-duplex mode.<br>0b - Enable Retry<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3563 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function<br>1b - Disable Retry|
|---|---|
|7<br>Reserved_7|Reserved.|
|6-5<br>BL|Back-Off Limit The back-off limit determines the random integer number (r) of slot time delays (4,096 bit<br>times for 1000/2500 Mbps; 512 bit times for 10/100 Mbps) for which the MAC waits before rescheduling<br>a transmission attempt during retries after a collision. n = retransmission attempt. The random integer r<br>takes the value in the range 0 <= r < 2^k This bit is applicable only in the half-duplex mode.<br>00b - k = min(n,10)<br>01b - k = min(n,8)<br>10b - k = min(n,4)<br>11b - k = min(n,1)|
|4<br>DC|Deferral Check When this bit is set, the deferral check function is enabled in the MAC. The MAC issues<br>a Packet Abort status, along with the excessive deferral error bit set in the Tx packet status, when<br>the Tx state machine is deferred for more than 24,288 bit times in 10 or 100 Mbps mode. If the MAC<br>is configured for 1000/2500 Mbps operation, the threshold for deferral is 155,680 bits times. Deferral<br>begins when the transmitter is ready to transmit, but it is prevented because of an active carrier sense<br>signal (CRS) on GMII or MII. The defer time is not cumulative. For example, if the transmitter defers for<br>10,000 bit times because the CRS signal is active and the CRS signal becomes inactive, the transmitter<br>transmits and collision happens. Because of collision, the transmitter needs to back off and then defer<br>again after back off completion. In such a scenario, the deferral timer is reset to 0, and it is restarted.<br>When this bit is reset, the deferral check function is disabled and the MAC defers until the CRS signal<br>goes inactive. This bit is applicable only in the half-duplex mode.<br>0b - Deferral check function is disabled<br>1b - Deferral check function is enabled|
|3-2<br>PRELEN|Preamble Length for Transmit packets These bits control the number of preamble bytes that are added<br>to the beginning of every Tx packet. The preamble reduction occurs only when the MAC is operating in<br>the full-duplex mode.<br>00b - 7 bytes of preamble<br>01b - 5 bytes of preamble<br>10b - 3 bytes of preamble<br>11b - Reserved|
|1<br>TE|Transmitter Enable When this bit is set, the Tx state machine of the MAC is enabled for transmission on<br>the GMII or MII interface. When this bit is reset, the MAC Tx state machine is disabled after it completes<br>the transmission of the current packet. The Tx state machine does not transmit any more packets.<br>0b - Transmitter is disabled<br>1b - Transmitter is enabled|
|0|Receiver Enable When this bit is set, the Rx state machine of the MAC is enabled for receiving packets<br>from the GMII or MII interface. When this bit is reset, the MAC Rx state machine is disabled after it|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3564 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|RE|completes the reception of the current packet. The Rx state machine does not receive any more packets<br>from the GMII or MII interface.|
||0b - Receiver is disabled|
||1b - Receiver is enabled|



### 75.7.3 (MAC_Ext_Configuration) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Ext_Configuration|4h|



##### Function 

The MAC Extended Configuration Register establishes the operating mode of the MAC. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3565-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv Reserv<br>R e... APDIM  EIPG  EIPGE e... HDSMS  PDC  USP  SPEN  DCRC<br>N  C<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserved_15_1<br>R<br>4  GPSL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Reserved.|
|Reserved_FHE||
|30<br>APDIM|ARP Packet Drop if IP Address Mismatch When this bit is set, Packet for which Target Protocol Address<br>does not match IPv4 address is dropped in the MTL layer. When this bit is reset, when target Protocol<br>Address does not match, packet is forwarded to MTL maintaining backward compatibility|
||0b - mux select to drop the arp packet if target protocol address mismatches IPv4 address<br>disabled|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3565 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function<br>1b - mux select to drop the arp packet if target protocol address mismatches IPv4 address<br>enabled|
|---|---|
|29-25<br>EIPG|Extended Inter-Packet Gap The value in this field is applicable when the EIPGEN bit is set. This field (as<br>Most Significant bits), along with IPG field in MAC_Configuration register, gives the minimum IPG greater<br>than 96 bit times in steps of 8 bit times: {EIPG, IPG} 8'h00 - 104 bit times 8'h01 - 112 bit times 8'h02 -<br>120 bit times ----------------------- 8'hFF - 2144 bit times|
|24<br>EIPGEN|Extended Inter-Packet Gap Enable When this bit is set, the MAC interprets EIPG field and IPG field in<br>MAC_Configuration register together as minimum IPG greater than 96 bit times in steps of 8 bit times.<br>When this bit is reset, the MAC ignores EIPG field and interprets IPG field in MAC_Configuration register<br>as minimum IPG less than or equal to 96 bit times in steps of 8 bit times. Note: Enable the extended<br>Inter-Packet Gap feature only when operating in Full-Duplex mode. There might be undesirable effects<br>on back-pressure function and frame transmission if it is enabled in Half-Duplex mode.<br>0b - Extended Inter-Packet Gap is disabled<br>1b - Extended Inter-Packet Gap is enabled|
|23<br>Reserved_23|Reserved.|
|22-20<br>HDSMS|Maximum Size for Splitting the Header Data These bits indicate the maximum header size allowed for<br>splitting the header data in the received packet.<br>000b - Maximum Size for Splitting the Header Data is 64 bytes<br>001b - Maximum Size for Splitting the Header Data is 128 bytes<br>010b - Maximum Size for Splitting the Header Data is 256 bytes<br>011b - Maximum Size for Splitting the Header Data is 512 bytes<br>100b - Maximum Size for Splitting the Header Data is 1024 bytes<br>101b - Reserved|
|19<br>PDC|Packet Duplication Control When this bit is set, the received packet with Multicast/Broadcast Destination<br>address is routed to multiple Receive DMA Channels. The Receive DMA Channels is identified by the<br>DCS field of MAC_Address(#i)_High register corresponding to the MAC Address register that matches<br>the Multicast/Broadcast Destination address in the received packet. The DCS field is interpreted to be a<br>one-hot value, each bit corresponding to the Receive DMA Channel. When this bit is reset, the received<br>packet is routed to single Receive DMA Channel. The Receive DMA Channel is identified by the DCS<br>field of MAC_Address(#i)_High register corresponding to the MAC Address register that matches the<br>Destination address in the received packet. The DCS field is interpreted as a binary value.<br>0b - Packet Duplication Control is disabled<br>1b - Packet Duplication Control is enabled|
|18<br>USP|Unicast Slow Protocol Packet Detect When this bit is set, the MAC detects the Slow Protocol packets<br>with unicast address of the station specified in the MAC_Address0_High and MAC_Address0_Low<br>registers. The MAC also detects the Slow Protocol packets with the Slow Protocols multicast address<br>(01-80-C2-00-00-02). When this bit is reset, the MAC detects only Slow Protocol packets with the Slow<br>Protocol multicast address specified in the IEEE 802.3-2015, Section 5.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3566 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Unicast Slow Protocol Packet Detection is disabled<br>1b - Unicast Slow Protocol Packet Detection is enabled|
|17<br>SPEN|Slow Protocol Detection Enable When this bit is set, MAC processes the Slow Protocol packets (Ether<br>Type 0x8809) and provides the Slow Protocol Sub-Type and Code fields in Rx status. When this bit is<br>reset, the MAC forwards all error-free Slow Protocol packets to the application. The MAC considers such<br>packets as normal Type packets.<br>0b - Slow Protocol Detection is disabled<br>1b - Slow Protocol Detection is enabled|
|16<br>DCRCC|Disable CRC Checking for Received Packets When this bit is set, the MAC receiver does not check the<br>CRC field in the received packets. When this bit is reset, the MAC receiver always checks the CRC field<br>in the received packets.<br>0b - CRC Checking is enabled<br>1b - CRC Checking is disabled|
|15-14|Reserved.|
|Reserved_15_1<br>4||
|13-0<br>GPSL|Giant Packet Size Limit If the received packet size is greater than the value programmed in this field<br>in units of bytes, the MAC declares the received packet as Giant packet. The value programmed in<br>this field must be greater than or equal to 1,518 bytes. Any other programmed value is considered as<br>1,518 bytes. For VLAN tagged packets, the MAC adds 4 bytes to the programmed value. When the<br>Enable Double VLAN Processing option is selected, the MAC adds 8 bytes to the programmed value<br>for double VLAN tagged packets. The value in this field is applicable when the GPSLCE bit is set in<br>MAC_Configuration register.|



### 75.7.4 (MAC_Packet_Filter) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Packet_Filter|8h|



##### Function 

The MAC Packet Filter register contains the filter controls for receiving packets. Some of the controls from this register go to the address check block of the MAC which performs the first level of address filtering. The second level of filtering is performed on the incoming packet based on other controls such as Pass Bad Packets and Pass Control Packets. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3567 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|RA||||Res|erved_30|_22||||DNTU|IPFE|Res|erved_19|_17|VTFE|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||Res|erved_15|_11||HPF|SAF|SAIF|PCF||DBF|PM|DAIF|HMC|HUC|PR|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31<br>RA|Receive All When this bit is set, the MAC Receiver module passes all received packets to the<br>application, irrespective of whether they pass the address filter or not. The result of the SA or DA<br>filtering is updated (pass or fail) in the corresponding bit in the Rx Status Word. When this bit is reset, the<br>Receiver module passes only those packets to the application that pass the SA or DA address filter.<br>0b - Receive All is disabled<br>1b - Receive All is enabled|
|30-22<br>Reserved_30_2<br>2|Reserved.|
|21<br>DNTU|Drop Non-TCP/UDP over IP Packets When this bit is set, the MAC drops the non-TCP or UDP over IP<br>packets. The MAC forward only those packets that are processed by the Layer 4 filter. When this bit is<br>reset, the MAC forwards all non-TCP or UDP over IP packets.<br>0b - Forward Non-TCP/UDP over IP Packets<br>1b - Drop Non-TCP/UDP over IP Packets|
|20<br>IPFE|Layer 3 and Layer 4 Filter Enable When this bit is set, the MAC drops packets that do not match the<br>enabled Layer 3 and Layer 4 filters. If Layer 3 or Layer 4 filters are not enabled for matching, this bit<br>does not have any effect. When this bit is reset, the MAC forwards all packets irrespective of the match<br>status of the Layer 3 and Layer 4 fields.<br>0b - Layer 3 and Layer 4 Filters are disabled<br>1b - Layer 3 and Layer 4 Filters are enabled|
|19-17<br>Reserved_19_1<br>7|Reserved.|
|16<br>VTFE|VLAN Tag Filter Enable When this bit is set, the MAC drops the VLAN tagged packets that do not match<br>the VLAN Tag. When this bit is reset, the MAC forwards all packets irrespective of the match status of<br>the VLAN Tag.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3568 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function<br>0b - VLAN Tag Filter is disabled<br>1b - VLAN Tag Filter is enabled|
|---|---|
|15-11<br>Reserved_15_<br>1|1<br>Reserved.|
|10<br>HPF|Hash or Perfect Filter When this bit is set, the address filter passes a packet if it matches either the<br>perfect filtering or hash filtering as set by the HMC or HUC bit. When this bit is reset and the HUC or<br>HMC bit is set, the packet is passed only if it matches the Hash filter.<br>0b - Hash or Perfect Filter is disabled<br>1b - Hash or Perfect Filter is enabled|
|9<br>SAF|Source Address Filter Enable When this bit is set, the MAC compares the SA field of the received<br>packets with the values programmed in the enabled SA registers. If the comparison fails, the MAC<br>drops the packet. When this bit is reset, the MAC forwards the received packet to the application with<br>updated SAF bit of the Rx Status depending on the SA address comparison. Note: According to the<br>IEEE specification, Bit 47 of the SA is reserved. However, in DWC_ether_qos, the MAC compares all<br>48 bits. The software driver should take this into consideration while programming the MAC address<br>registers for SA.<br>0b - SA Filtering is disabled<br>1b - SA Filtering is enabled|
|8<br>SAIF|SA Inverse Filtering When this bit is set, the Address Check block operates in the inverse filtering mode<br>for SA address comparison. If the SA of a packet matches the values programmed in the SA registers, it<br>is marked as failing the SA Address filter. When this bit is reset, if the SA of a packet does not match the<br>values programmed in the SA registers, it is marked as failing the SA Address filter.<br>0b - SA Inverse Filtering is disabled<br>1b - SA Inverse Filtering is enabled|
|7-6<br>PCF|Pass Control Packets These bits control the forwarding of all control packets (including unicast and<br>multicast Pause packets).<br>00b - MAC filters all control packets from reaching the application<br>01b - MAC forwards all control packets except Pause packets to the application even if they fail<br>the Address filter<br>10b - MAC forwards all control packets to the application even if they fail the Address filter<br>11b - MAC forwards the control packets that pass the Address filter|
|5<br>DBF|Disable Broadcast Packets When this bit is set, the AFM module blocks all the incoming broadcast<br>packets. In addition, it overrides all other filter settings. When this bit is reset, the AFM module passes all<br>received broadcast packets.<br>0b - Enable Broadcast Packets<br>1b - Disable Broadcast Packets|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3569 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|4<br>PM|Pass All Multicast When this bit is set, it indicates that all the received packets with a multicast<br>destination address (first bit in the destination address field is '1') are passed. When this bit is reset,<br>filtering of multicast packet depends on HMC bit.<br>0b - Pass All Multicast is disabled<br>1b - Pass All Multicast is enabled|
|3<br>DAIF|DA Inverse Filtering When this bit is set, the Address Check block operates in inverse filtering mode for<br>the DA address comparison for both unicast and multicast packets. When this bit is reset, normal filtering<br>of packets is performed.<br>0b - DA Inverse Filtering is disabled<br>1b - DA Inverse Filtering is enabled|
|2<br>HMC|Hash Multicast When this bit is set, the MAC performs the destination address filtering of received<br>multicast packets according to the hash table. When this bit is reset, the MAC performs the perfect<br>destination address filtering for multicast packets, that is, it compares the DA field with the values<br>programmed in DA registers.<br>0b - Hash Multicast is disabled<br>1b - Hash Multicast is enabled|
|1<br>HUC|Hash Unicast When this bit is set, the MAC performs the destination address filtering of unicast packets<br>according to the hash table. When this bit is reset, the MAC performs a perfect destination address<br>filtering for unicast packets, that is, it compares the DA field with the values programmed in DA registers.<br>0b - Hash Unicast is disabled<br>1b - Hash Unicast is enabled|
|0<br>PR|Promiscuous Mode When this bit is set, the Address Filtering module passes all incoming packets<br>irrespective of the destination or source address. The SA or DA Filter Fails status bits of the Rx Status<br>Word are always cleared when PR is set.<br>0b - Promiscuous Mode is disabled<br>1b - Promiscuous Mode is enabled|



### 75.7.5 (MAC_Watchdog_Timeout) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Watchdog_Timeou<br>t|Ch|



##### Function 

The Watchdog Timeout register controls the watchdog timeout for received packets. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3570 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18||17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||Reserve|d_31_9|||||||||
|W||||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0||0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2||1|0|
|R<br>W|||Res|erved_3|1_9|||PWE||Reserv|ed_7_4|||W|TO|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0||0|0|



##### Fields 

|Field|Function|
|---|---|
|31-9|Reserved.|
|Reserved_31_9||
|8<br>PWE|Programmable Watchdog Enable When this bit is set and the WD bit of the MAC_Configuration register<br>is reset, the WTO field is used as watchdog timeout for a received packet. When this bit is cleared, the<br>watchdog timeout for a received packet is controlled by setting of WD and JE bits in MAC_Configuration<br>register.<br>0b - Programmable Watchdog is disabled<br>1b - Programmable Watchdog is enabled|
|7-4|Reserved.|
|Reserved_7_4||
|3-0<br>WTO|Watchdog Timeout When the PWE bit is set and the WD bit of the MAC_Configuration register is reset,<br>this field is used as watchdog timeout for a received packet. If the length of a received packet exceeds<br>the value of this field, such packet is terminated and declared as an error packet. Note: When the PWE<br>bit is set, the value in this field should be more than 1,522 (0x05F2). Otherwise, the IEEE 802.3-specified<br>valid tagged packets are declared as error packets and then dropped.<br>0000b - 2 KB|
||0001b - 3 KB|
||0010b - 4 KB|
||0011b - 5 KB|
||0100b - 6 KB|
||0101b - 7 KB|
||0110b - 8 KB|
||0111b - 9 KB|
||1000b - 10 KB|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3571 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function||
|---|---|---|
||1001b -|11 KB|
||1010b -|12 KB|
||1011b -|13 KB|
||1100b -|14 KB|
||1101b -|15 KB|
||1110b -|16383 Bytes|
||1111b -|Reserved|



### 75.7.6 (MAC_Hash_Table_Reg0) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Hash_Table_Reg0|10h|



##### Function 

The Hash Table Register 0 contains the first 32 bits of the hash table, when the width of the hash table is 128 or 256 bits. You can specify the width of the hash table by using the Hash Table Size option in coreConsultant. The Hash table is used for group address filtering. For hash filtering, the content of the destination address in the incoming packet is passed through the CRC logic and the upper six (seven in 128-bit Hash or eight in 256-bit Hash) bits of the CRC register are used to index the content of the Hash table. The most significant bits determines the register to be used (Hash Table Register X), and the least significant five bits determine the bit within the register. For example, a hash value of 6'b100000 (in 64-bit Hash) selects Bit 0 of the Hash Table Register 1, a value of 7b'1110000 (in 128-bit Hash) selects Bit 16 of the Hash Table Register 3 and a value of 8b'10111111 (in 256-bit Hash) selects Bit 31 of the Hash Table Register 5. The hash value of the destination address is calculated in the following way: - Calculate the 32-bit CRC for the DA (See IEEE 802.3, Section 3.2.8 for the steps to calculate CRC32). - Perform bitwise reversal for the value obtained in Step 1. - Take the upper 6 (or 7 or 8) bits from the value obtained in Step 2. If the corresponding bit value of the register is 1'b1, the packet is accepted. Otherwise, it is rejected. If the PM bit is set in MAC_Packet_Filter, all multicast packets are accepted regardless of the multicast hash values. If the Hash Table register is configured to be double-synchronized to the (G)MII clock domain, the synchronization is triggered only when Bits[31:24] (in little-endian mode) or Bits[7:0] (in big-endian mode) of the Hash Table Register X registers are written. If double-synchronization is enabled, consecutive writes to this register should be performed after at least four clock cycles in the destination clock domain. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3572 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3573-01.png)


<!-- Start of picture text -->
Gigabit Ethernet Media Access Controller (GMAC)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>HT31T0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>HT31T0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|MAC Hash Table First 32 Bits This field contains the first 32 Bits [31:0] of the Hash table.|
|HT31T0||



### 75.7.7 (MAC_Hash_Table_Reg1) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Hash_Table_Reg1|14h|



##### Function 

The Hash Table Register 1 contains the second 32 bits of the hash table. You can specify the width of the hash table by using the Hash Table Size option in coreConsultant. The Hash table is used for group address filtering. For hash filtering, the content of the destination address in the incoming packet is passed through the CRC logic and the upper six (seven in 128-bit Hash or eight in 256-bit Hash) bits of the CRC register are used to index the content of the Hash table. The most significant bits determines the register to be used (Hash Table Register X), and the least significant five bits determine the bit within the register. For example, a hash value of 6'b100000 (in 64-bit Hash) selects Bit 0 of the Hash Table Register 1, a value of 7b'1110000 (in 128-bit Hash) selects Bit 16 of the Hash Table Register 3 and a value of 8b'10111111 (in 256-bit Hash) selects Bit 31 of the Hash Table Register 5. The hash value of the destination address is calculated in the following way: - Calculate the 32-bit CRC for the DA (See IEEE 802.3, Section 3.2.8 for the steps to calculate CRC32). - Perform bitwise reversal for the value obtained in Step 1. - Take the upper 6 (or 7 or 8) bits from the value obtained in Step 2. If the corresponding bit value of the register is 1'b1, the packet is accepted. Otherwise, it is rejected. If the PM bit is set in MAC_Packet_Filter, all multicast packets are accepted regardless of the multicast hash values. If the Hash Table register is configured to be double-synchronized to the (G)MII clock domain, the synchronization is triggered only when Bits[31:24] (in little-endian mode) or Bits[7:0] (in big-endian mode) of the Hash Table Register X registers are written. If double-synchronization is enabled, consecutive writes to this register should be performed after at least four clock cycles in the destination clock domain. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3573 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3574-01.png)


<!-- Start of picture text -->
Gigabit Ethernet Media Access Controller (GMAC)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>HT63T32<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>HT63T32<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|MAC Hash Table Second 32 Bits This field contains the second 32 Bits [63:32] of the Hash table.|
|HT63T32||



### 75.7.8 (MAC_Hash_Table_Reg2) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Hash_Table_Reg2|18h|



##### Function 

The Hash Table Register 2 contains the third 32 bits of the hash table. You can specify the width of the hash table by using the Hash Table Size option in coreConsultant. The Hash table is used for group address filtering. For hash filtering, the content of the destination address in the incoming packet is passed through the CRC logic and the upper six (seven in 128-bit Hash or eight in 256-bit Hash) bits of the CRC register are used to index the content of the Hash table. The most significant bits determines the register to be used (Hash Table Register X), and the least significant five bits determine the bit within the register. For example, a hash value of 6'b100000 (in 64-bit Hash) selects Bit 0 of the Hash Table Register 1, a value of 7b'1110000 (in 128-bit Hash) selects Bit 16 of the Hash Table Register 3 and a value of 8b'10111111 (in 256-bit Hash) selects Bit 31 of the Hash Table Register 5. The hash value of the destination address is calculated in the following way: - Calculate the 32-bit CRC for the DA (See IEEE 802.3, Section 3.2.8 for the steps to calculate CRC32). - Perform bitwise reversal for the value obtained in Step 1. - Take the upper 6 (or 7 or 8) bits from the value obtained in Step 2. If the corresponding bit value of the register is 1'b1, the packet is accepted. Otherwise, it is rejected. If the PM bit is set in MAC_Packet_Filter, all multicast packets are accepted regardless of the multicast hash values. If the Hash Table register is configured to be double-synchronized to the (G)MII clock domain, the synchronization is triggered only when Bits[31:24] (in little-endian mode) or Bits[7:0] (in big-endian mode) of the Hash Table Register X registers are written. If double-synchronization is enabled, consecutive writes to this register should be performed after at least four clock cycles in the destination clock domain. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3574 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3575-01.png)


<!-- Start of picture text -->
Gigabit Ethernet Media Access Controller (GMAC)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>HT95T64<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>HT95T64<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3575-03.png)


<!-- Start of picture text -->
Field Function<br>31-0 MAC Hash Table Third 32 Bits This field contains the third 32 Bits [95:64] of the Hash table.<br>HT95T64<br><!-- End of picture text -->

### 75.7.9 (MAC_Hash_Table_Reg3) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Hash_Table_Reg3|1Ch|



##### Function 

The Hash Table Register 3 contains the fourth 32 bits of the hash table. You can specify the width of the hash table by using the Hash Table Size option in coreConsultant. The Hash table is used for group address filtering. For hash filtering, the content of the destination address in the incoming packet is passed through the CRC logic and the upper six (seven in 128-bit Hash or eight in 256-bit Hash) bits of the CRC register are used to index the content of the Hash table. The most significant bits determines the register to be used (Hash Table Register X), and the least significant five bits determine the bit within the register. For example, a hash value of 6'b100000 (in 64-bit Hash) selects Bit 0 of the Hash Table Register 1, a value of 7b'1110000 (in 128-bit Hash) selects Bit 16 of the Hash Table Register 3 and a value of 8b'10111111 (in 256-bit Hash) selects Bit 31 of the Hash Table Register 5. The hash value of the destination address is calculated in the following way: - Calculate the 32-bit CRC for the DA (See IEEE 802.3, Section 3.2.8 for the steps to calculate CRC32). - Perform bitwise reversal for the value obtained in Step 1. - Take the upper 6 (or 7 or 8) bits from the value obtained in Step 2. If the corresponding bit value of the register is 1'b1, the packet is accepted. Otherwise, it is rejected. If the PM bit is set in MAC_Packet_Filter, all multicast packets are accepted regardless of the multicast hash values. If the Hash Table register is configured to be double-synchronized to the (G)MII clock domain, the synchronization is triggered only when Bits[31:24] (in little-endian mode) or Bits[7:0] (in big-endian mode) of the Hash Table Register X registers are written. If double-synchronization is enabled, consecutive writes to this register should be performed after at least four clock cycles in the destination clock domain. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3575 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3576-01.png)


<!-- Start of picture text -->
Gigabit Ethernet Media Access Controller (GMAC)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>HT127T96<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>HT127T96<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|MAC Hash Table Fourth 32 Bits This field contains the fourth 32 Bits [127:96] of the Hash table.|
|HT127T96||



### 75.7.10 (MAC_Hash_Table_Reg4) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Hash_Table_Reg4|20h|



##### Function 

The Hash Table Register 4 contains the fifth 32 bits of the hash table. You can specify the width of the hash table by using the Hash Table Size option in coreConsultant. The Hash table is used for group address filtering. For hash filtering, the content of the destination address in the incoming packet is passed through the CRC logic and the upper six (seven in 128-bit Hash or eight in 256-bit Hash) bits of the CRC register are used to index the content of the Hash table. The most significant bits determines the register to be used (Hash Table Register X), and the least significant five bits determine the bit within the register. For example, a hash value of 6'b100000 (in 64-bit Hash) selects Bit 0 of the Hash Table Register 1, a value of 7b'1110000 (in 128-bit Hash) selects Bit 16 of the Hash Table Register 3 and a value of 8b'10111111 (in 256-bit Hash) selects Bit 31 of the Hash Table Register 5. The hash value of the destination address is calculated in the following way: - Calculate the 32-bit CRC for the DA (See IEEE 802.3, Section 3.2.8 for the steps to calculate CRC32). - Perform bitwise reversal for the value obtained in Step 1. - Take the upper 6 (or 7 or 8) bits from the value obtained in Step 2. If the corresponding bit value of the register is 1'b1, the packet is accepted. Otherwise, it is rejected. If the PM bit is set in MAC_Packet_Filter, all multicast packets are accepted regardless of the multicast hash values. If the Hash Table register is configured to be double-synchronized to the (G)MII clock domain, the synchronization is triggered only when Bits[31:24] (in little-endian mode) or Bits[7:0] (in big-endian mode) of the Hash Table Register X registers are written. If double-synchronization is enabled, consecutive writes to this register should be performed after at least four clock cycles in the destination clock domain. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3576 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3577-01.png)


<!-- Start of picture text -->
Gigabit Ethernet Media Access Controller (GMAC)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>HT159T128<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>HT159T128<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|MAC Hash Table Fifth 32 Bits This field contains the fifth 32 Bits [159:128] of the Hash table.|
|HT159T128||



### 75.7.11 (MAC_Hash_Table_Reg5) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Hash_Table_Reg5|24h|



##### Function 

The Hash Table Register 5 contains the sixth 32 bits of the hash table. You can specify the width of the hash table by using the Hash Table Size option in coreConsultant. The Hash table is used for group address filtering. For hash filtering, the content of the destination address in the incoming packet is passed through the CRC logic and the upper six (seven in 128-bit Hash or eight in 256-bit Hash) bits of the CRC register are used to index the content of the Hash table. The most significant bits determines the register to be used (Hash Table Register X), and the least significant five bits determine the bit within the register. For example, a hash value of 6'b100000 (in 64-bit Hash) selects Bit 0 of the Hash Table Register 1, a value of 7b'1110000 (in 128-bit Hash) selects Bit 16 of the Hash Table Register 3 and a value of 8b'10111111 (in 256-bit Hash) selects Bit 31 of the Hash Table Register 5. The hash value of the destination address is calculated in the following way: - Calculate the 32-bit CRC for the DA (See IEEE 802.3, Section 3.2.8 for the steps to calculate CRC32). - Perform bitwise reversal for the value obtained in Step 1. - Take the upper 6 (or 7 or 8) bits from the value obtained in Step 2. If the corresponding bit value of the register is 1'b1, the packet is accepted. Otherwise, it is rejected. If the PM bit is set in MAC_Packet_Filter, all multicast packets are accepted regardless of the multicast hash values. If the Hash Table register is configured to be double-synchronized to the (G)MII clock domain, the synchronization is triggered only when Bits[31:24] (in little-endian mode) or Bits[7:0] (in big-endian mode) of the Hash Table Register X registers are written. If double-synchronization is enabled, consecutive writes to this register should be performed after at least four clock cycles in the destination clock domain. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3577 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3578-01.png)


<!-- Start of picture text -->
Gigabit Ethernet Media Access Controller (GMAC)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>HT191T160<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>HT191T160<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3578-03.png)


<!-- Start of picture text -->
Field Function<br>31-0 MAC Hash Table Sixth 32 Bits This field contains the sixth 32 Bits [191:160] of the Hash table.<br>HT191T160<br><!-- End of picture text -->

### 75.7.12 (MAC_Hash_Table_Reg6) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Hash_Table_Reg6|28h|



##### Function 

The Hash Table Register 6 contains the seventh 32 bits of the hash table. You can specify the width of the hash table by using the Hash Table Size option in coreConsultant. The Hash table is used for group address filtering. For hash filtering, the content of the destination address in the incoming packet is passed through the CRC logic and the upper six (seven in 128-bit Hash or eight in 256-bit Hash) bits of the CRC register are used to index the content of the Hash table. The most significant bits determines the register to be used (Hash Table Register X), and the least significant five bits determine the bit within the register. For example, a hash value of 6'b100000 (in 64-bit Hash) selects Bit 0 of the Hash Table Register 1, a value of 7b'1110000 (in 128-bit Hash) selects Bit 16 of the Hash Table Register 3 and a value of 8b'10111111 (in 256-bit Hash) selects Bit 31 of the Hash Table Register 5. The hash value of the destination address is calculated in the following way: - Calculate the 32-bit CRC for the DA (See IEEE 802.3, Section 3.2.8 for the steps to calculate CRC32). - Perform bitwise reversal for the value obtained in Step 1. - Take the upper 6 (or 7 or 8) bits from the value obtained in Step 2. If the corresponding bit value of the register is 1'b1, the packet is accepted. Otherwise, it is rejected. If the PM bit is set in MAC_Packet_Filter, all multicast packets are accepted regardless of the multicast hash values. If the Hash Table register is configured to be double-synchronized to the (G)MII clock domain, the synchronization is triggered only when Bits[31:24] (in little-endian mode) or Bits[7:0] (in big-endian mode) of the Hash Table Register X registers are written. If double-synchronization is enabled, consecutive writes to this register should be performed after at least four clock cycles in the destination clock domain. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3578 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3579-01.png)


<!-- Start of picture text -->
Gigabit Ethernet Media Access Controller (GMAC)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>HT223T192<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>HT223T192<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3579-03.png)


<!-- Start of picture text -->
Field Function<br>31-0 MAC Hash Table Seventh 32 Bits This field contains the seventh 32 Bits [223:192] of the Hash table.<br>HT223T192<br><!-- End of picture text -->

### 75.7.13 (MAC_Hash_Table_Reg7) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Hash_Table_Reg7|2Ch|



##### Function 

The Hash Table Register 7 contains the eighth 32 bits of the hash table. You can specify the width of the hash table by using the Hash Table Size option in coreConsultant. The Hash table is used for group address filtering. For hash filtering, the content of the destination address in the incoming packet is passed through the CRC logic and the upper six (seven in 128-bit Hash or eight in 256-bit Hash) bits of the CRC register are used to index the content of the Hash table. The most significant bits determines the register to be used (Hash Table Register X), and the least significant five bits determine the bit within the register. For example, a hash value of 6'b100000 (in 64-bit Hash) selects Bit 0 of the Hash Table Register 1, a value of 7b'1110000 (in 128-bit Hash) selects Bit 16 of the Hash Table Register 3 and a value of 8b'10111111 (in 256-bit Hash) selects Bit 31 of the Hash Table Register 5. The hash value of the destination address is calculated in the following way: - Calculate the 32-bit CRC for the DA (See IEEE 802.3, Section 3.2.8 for the steps to calculate CRC32). - Perform bitwise reversal for the value obtained in Step 1. - Take the upper 6 (or 7 or 8) bits from the value obtained in Step 2. If the corresponding bit value of the register is 1'b1, the packet is accepted. Otherwise, it is rejected. If the PM bit is set in MAC_Packet_Filter, all multicast packets are accepted regardless of the multicast hash values. If the Hash Table register is configured to be double-synchronized to the (G)MII clock domain, the synchronization is triggered only when Bits[31:24] (in little-endian mode) or Bits[7:0] (in big-endian mode) of the Hash Table Register X registers are written. If double-synchronization is enabled, consecutive writes to this register should be performed after at least four clock cycles in the destination clock domain. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3579 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3580-01.png)


<!-- Start of picture text -->
Gigabit Ethernet Media Access Controller (GMAC)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>HT255T224<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>HT255T224<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3580-03.png)


<!-- Start of picture text -->
Field Function<br>31-0 MAC Hash Table Eighth 32 Bits This field contains the eighth 32 Bits [255:224] of the Hash table.<br>HT255T224<br><!-- End of picture text -->

### 75.7.14 (MAC_VLAN_Tag_Ctrl) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Ctrl|50h|



##### Function 

This register is the redefined format of the MAC VLAN Tag Register. It is used for indirect addressing. It contains the address offset, command type and Busy Bit for CSR access of the Per VLAN Tag registers. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3580-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv Reserv<br>R<br>EIVLR e... EIVLS  ERIVL EDVL VTHM  EVLR e... EVLS  DOVL ERSV ESVL  VTIM  ETV<br>XS  T  P  XS  TC  LM<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_15_y<br>OFS  CT  OB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3580 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Fields 

|Field|Function|
|---|---|
|31<br>EIVLRXS|Enable Inner VLAN Tag in Rx Status When this bit is set, the MAC provides the inner VLAN Tag in the<br>Rx status. When this bit is reset, the MAC does not provide the inner VLAN Tag in Rx status.<br>0b - Inner VLAN Tag in Rx status is disabled<br>1b - Inner VLAN Tag in Rx status is enabled|
|30<br>Reserved_30|Reserved.|
|29-28<br>EIVLS|Enable Inner VLAN Tag Stripping on Receive This field indicates the stripping operation on inner VLAN<br>Tag in received packet.<br>00b - Do not strip<br>01b - Strip if VLAN filter passes<br>10b - Strip if VLAN filter fails<br>11b - Always strip|
|27<br>ERIVLT|Enable Inner VLAN Tag Comparison When this bit, VTHM bit and the EDVLP field are set, the MAC<br>receiver enables VLAN Hash filtering operation on the inner VLAN Tag (if present). When this bit is reset<br>and VTHM bit is set, the MAC receiver enables VLAN Hash filtering operation on the outer VLAN Tag (if<br>present). The ERSVLM bit and DOVLTC bit determines which VLAN type is enabled for filtering.<br>0b - Inner VLAN tag is disabled<br>1b - Inner VLAN tag is enabled|
|26<br>EDVLP|Enable Double VLAN Processing When this bit is set, the MAC enables processing of up to two VLAN<br>Tags on Tx and Rx (if present). When this bit is reset, the MAC enables processing of up to one VLAN<br>Tag on Tx and Rx (if present).<br>0b - Double VLAN Processing is disabled<br>1b - Double VLAN Processing is enabled|
|25<br>VTHM|VLAN Tag Hash Table Match Enable When this bit is set, the most significant four bits of CRC of VLAN<br>Tag are used to index the content of the MAC_VLAN_Hash_Table register. A value of 1 in the VLAN<br>Hash Table register, corresponding to the index, indicates that the packet matched the VLAN hash table.<br>When the ETV bit is set, the CRC of the 12-bit VLAN Identifier (VID) is used for comparison. When the<br>ETV bit is reset, the CRC of the 16-bit VLAN tag is used for comparison. When this bit is reset, the VLAN<br>Hash Match operation is not performed.<br>0b - VLAN Tag Hash Table Match is disabled<br>1b - VLAN Tag Hash Table Match is enabled|
|24<br>EVLRXS<br>23|Enable VLAN Tag in Rx status When this bit is set, MAC provides the outer VLAN Tag in the Rx status.<br>When this bit is reset, the MAC does not provide the outer VLAN Tag in Rx status.<br>0b - VLAN Tag in Rx status is disabled<br>1b - VLAN Tag in Rx status is enabled<br>Reserved.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3581 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field<br>Reserved_23|Function|
|---|---|
|22-21<br>EVLS|Enable VLAN Tag Stripping on Receive This field indicates the stripping operation on the outer VLAN<br>Tag in received packet.<br>00b - Do not strip<br>01b - Strip if VLAN filter passes<br>10b - Strip if VLAN filter fails<br>11b - Always strip|
|20<br>DOVLTC|Disable VLAN Type Check for VLAN Hash Filtering When this bit is set, the MAC VLAN Hash Filter does<br>not check whether the VLAN Tag specified by the ERIVLT bit is of type S-VLAN or C-VLAN. When this<br>bit is reset, the MAC VLAN Hash Filter filters or matches the VLAN Tag specified by the ERIVLT bit only<br>when VLAN Tag type is similar to the one specified by the ERSVLM bit.<br>0b - VLAN Type Check is enabled<br>1b - VLAN Type Check is disabled|
|19<br>ERSVLM|Enable Receive S-VLAN Match for VLAN Hash Filtering When this bit is set, the MAC receiver enables<br>VLAN Hash filtering or matching for S-VLAN (Type = 0x88A8) packets. When this bit is reset, the MAC<br>receiver enables VLAN Hash filtering or matching for C-VLAN (Type = 0x8100) packets. The ERIVLT bit<br>determines the VLAN tag position considered for VLAN Hash filtering or matching.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|
|18<br>ESVL|Enable S-VLAN When this bit is set, the MAC transmitter and receiver consider the S-VLAN packets<br>(Type = 0x88A8) as valid VLAN tagged packets.<br>0b - S-VLAN is disabled<br>1b - S-VLAN is enabled|
|17<br>VTIM|VLAN Tag Inverse Match Enable When this bit is set, this bit enables the VLAN Tag inverse matching.<br>The packets without matching VLAN Tag are marked as matched. When reset, this bit enables the VLAN<br>Tag perfect matching. The packets with matched VLAN Tag are marked as matched.<br>0b - VLAN Tag Inverse Match is disabled<br>1b - VLAN Tag Inverse Match is enabled|
|16<br>ETV|Enable 12-Bit VLAN Tag Comparison for VLAN Hash Filtering When this bit is set, a 12-bit VLAN<br>identifier is used for VLAN Hash filtering instead of the complete 16-bit VLAN tag. Bits[11:0] of VLAN tag<br>in the received VLAN-tagged packet are used for hash-based VLAN filtering. When this bit is reset, all 16<br>bits of the 15th and 16th bytes of the received VLAN packet are used for VLAN hash filtering.<br>0b - 12-Bit VLAN Tag Comparison is disabled<br>1b - 12-Bit VLAN Tag Comparison is enabled|
|15-7<br>Reserved_15_y|Reserved.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3582 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|6-2<br>OFS|Offset This field holds the address offset of the MAC VLAN Tag Filter Register which the application is<br>trying to access. The width of the field depends on the number of MAC VLAN Tag Registers enabled.|
|1<br>CT|Command Type This bit indicates if the current register access is a read or a write. When set, it indicate<br>a read operation. When reset, it indicates a write operation.<br>0b - Write operation<br>1b - Read operation|
|0<br>OB|Operation Busy This bit is set along with a read or write command for initiating the indirect access to<br>per VLAN Tag Filter register. This bit is reset when the read or write command to per VLAN Tag Filter<br>indirect access register is complete. The next indirect register access can be initiated only after this bit is<br>reset. During a write operation, the bit is reset only after the data has been written into the Per VLAN Tag<br>register. During a read operation, the data should be read from the MAC_VLAN_Tag_Data register only<br>after this bit is reset.<br>0b - Operation Busy is disabled<br>1b - Operation Busy is enabled|



### 75.7.15 (MAC_VLAN_Tag_Data) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Data|54h|



##### Function 

This register holds the read/write data for Indirect Access of the Per VLAN Tag registers. During the read access, this field contains valid read data only after the OB bit is reset. During the write access, this field should be valid prior to setting the OB bit in the MAC_VLAN_Tag_Ctrl Register. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3583-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_y  DMAC Reserved_23_21  ERIVL ERSV DOVL<br>DMACHN  ETV  VEN<br>W HEN  T  LM  TC<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>VID<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3583 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Fields 

|Field<br>31-27|Function<br>Reserved.|
|---|---|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21<br>Reserved_23_2<br>1|Reserved.|
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3584 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.|
||0b - VLAN Tag is disabled|
||1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.16 (MAC_VLAN_Tag_Filter0) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter0|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3585-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_y  DMAC Reserved_23_21  ERIVL ERSV DOVL<br>DMACHN  ETV  VEN<br>W HEN  T  LM  TC<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>VID<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3585 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field<br>24<br>DMACHEN|Function<br>DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|---|---|
|23-21<br>Reserved_23_2<br>1|Reserved.|
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3586 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|15-0|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is|
|VID|valid when VLAN Tag Enable is set.|



### 75.7.17 (MAC_VLAN_Tag_Filter1) 

Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter1|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||Re|served_3|1_y||DMA|CHN|DMAC|Rese|rved_23|_21|ERIVL|ERSV|DOVL|ETV|VEN|
|W||||||||HEN||||T|LM|TC|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.|
||0b - DMA Channel Number is disabled|
||1b - DMA Channel Number is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3587 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|23-21<br>Reserved_23_2<br>1|Reserved.|
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3588 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

### 75.7.18 (MAC_VLAN_Tag_Filter10) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter1<br>0|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3589-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_y  DMAC Reserved_23_21  ERIVL ERSV DOVL<br>DMACHN  ETV  VEN<br>W HEN  T  LM  TC<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>VID<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3589 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|---|---|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.19 (MAC_VLAN_Tag_Filter11) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter1<br>1|54h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3590 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Function 

This register contains VLAN Tag filter ${i} control information. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3591 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.20 (MAC_VLAN_Tag_Filter12) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter1<br>2|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3592 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3593 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.21 (MAC_VLAN_Tag_Filter13) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter1<br>3|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3594 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3595 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.22 (MAC_VLAN_Tag_Filter14) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter1<br>4|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3596 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3597 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.23 (MAC_VLAN_Tag_Filter15) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter1<br>5|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3598 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3599 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.24 (MAC_VLAN_Tag_Filter16) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter1<br>6|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3600 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3601 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.25 (MAC_VLAN_Tag_Filter17) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter1<br>7|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3602 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3603 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.26 (MAC_VLAN_Tag_Filter18) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter1<br>8|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3604 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3605 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.27 (MAC_VLAN_Tag_Filter19) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter1<br>9|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3606 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3607 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.28 (MAC_VLAN_Tag_Filter2) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter2|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3608 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3609 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.29 (MAC_VLAN_Tag_Filter20) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter2<br>0|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3610 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3611 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.30 (MAC_VLAN_Tag_Filter21) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter2<br>1|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3612 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3613 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.31 (MAC_VLAN_Tag_Filter22) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter2<br>2|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3614 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3615 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.32 (MAC_VLAN_Tag_Filter23) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter2<br>3|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3616 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3617 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.33 (MAC_VLAN_Tag_Filter24) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter2<br>4|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3618 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3619 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.34 (MAC_VLAN_Tag_Filter25) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter2<br>5|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3620 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3621 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.35 (MAC_VLAN_Tag_Filter26) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter2<br>6|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3622 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3623 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.36 (MAC_VLAN_Tag_Filter27) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter2<br>7|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3624 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3625 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.37 (MAC_VLAN_Tag_Filter28) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter2<br>8|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3626 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3627 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.38 (MAC_VLAN_Tag_Filter29) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter2<br>9|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3628 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3629 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.39 (MAC_VLAN_Tag_Filter3) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter3|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3630 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3631 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.40 (MAC_VLAN_Tag_Filter30) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter3<br>0|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3632 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3633 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.41 (MAC_VLAN_Tag_Filter31) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter3<br>1|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3634 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3635 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.42 (MAC_VLAN_Tag_Filter4) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter4|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3636 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3637 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.43 (MAC_VLAN_Tag_Filter5) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter5|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3638 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3639 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.44 (MAC_VLAN_Tag_Filter6) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter6|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3640 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3641 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.45 (MAC_VLAN_Tag_Filter7) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter7|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3642 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3643 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.46 (MAC_VLAN_Tag_Filter8) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter8|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3644 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3645 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.47 (MAC_VLAN_Tag_Filter9) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter9|54h|



##### Function 

This register contains VLAN Tag filter ${i} control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3646 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Re|served_3|1_y||DMA|CHN|DMAC<br>HEN|Rese|rved_23|_21|ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved.|
|Reserved_31_y||
|26-25<br>DMACHN|DMA Channel Number The DMA Channel number to which the VLAN Tagged Frame is to be routed if it<br>passes this VLAN Tag Filter is programmed in this field. If the Routing based on VLAN Tag Filter is not<br>necessary, this field need not be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable This bit is the Enable for the DMA Channel Number value programmed<br>in the field DMACH. When this bit is reset, the Routing does not occur based on VLAN Filter result. The<br>frame is routed based on DA Based DMA Channel Routing.<br>0b - DMA Channel Number is disabled<br>1b - DMA Channel Number is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>ERIVLT|Enable Inner VLAN Tag Comparison This bit is valid only when Double VLAN Tag Enable of the Filter is<br>set. When this bit and the EDVLP field are set, the MAC receiver enables operation on the inner VLAN<br>Tag (if present). When this bit is reset, the MAC receiver enables operation on the outer VLAN Tag (if<br>present).<br>0b - Inner VLAN tag comparison is disabled<br>1b - Inner VLAN tag comparison is enabled|
|19<br>ERSVLM|Enable S-VLAN Match for received Frames This bit is valid only when VLAN Tag Enable of the Filter is<br>set. When this bit is set, the MAC receiver enables filtering or matching for S-VLAN (Type = 0x88A8)<br>packets. When this bit is reset, the MAC receiver enables filtering or matching for C-VLAN (Type =<br>0x8100) packets.<br>0b - Receive S-VLAN Match is disabled<br>1b - Receive S-VLAN Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3647 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>DOVLTC|Disable VLAN Type Comparison This bit is valid only when VLAN Tag Enable of the Filter is set. When<br>this bit is set, the MAC does not check whether the VLAN Tag specified by the Enable Inner VLAN Tag<br>Comparison bit is of type S-VLAN or C-VLAN. When this bit is reset, the MAC filters or matches the<br>VLAN Tag specified by the Enable Inner VLAN Tag Comparison bit only when VLAN Tag type is similar<br>to the one specified by the Enable S-VLAN Match for received Frames bit.<br>0b - VLAN type comparison is enabled<br>1b - VLAN type comparison is disabled|
|17<br>ETV|12bits or 16bits VLAN comparison This bit is valid only when VEN of the Filter is set. When this bit is set,<br>a 12-bit VLAN identifier is used for comparing and filtering instead of the complete 16-bit VLAN tag. Bits<br>[11:0] of VLAN tag are compared with the corresponding field in the received VLAN-tagged packet.<br>0b - 16 bit VLAN comparison<br>1b - 12 bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable This bit is used to enable or disable the VLAN Tag. When this bit is set, the MAC<br>compares the VLAN Tag of received packet with the VLAN Tag ID. When this bit is reset, no comparison<br>is performed irrespective of the programming of the other fields.<br>0b - VLAN Tag is disabled<br>1b - VLAN Tag is enabled|
|15-0<br>VID|VLAN Tag ID This field holds the VLAN Tag value which is used by the MAC for perfect comparison. It is<br>valid when VLAN Tag Enable is set.|



### 75.7.48 (MAC_VLAN_Hash_Table) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Hash_Table|58h|



##### Function 

When VTHM bit of the MAC_VLAN_Tag register is set, the 16-bit VLAN Hash Table register is used for group address filtering based on the VLAN tag. For hash filtering, the content of the 16-bit VLAN tag or 12-bit VLAN ID (based on the ETV bit of MAC_VLAN_Tag Register) in the incoming packet is passed through the CRC logic. The upper four bits of the calculated CRC value are used to index the contents of the VLAN Hash table. For example, hash value of 4b'1000 selects Bit 8 of the VLAN Hash table. The hash value of the destination address is calculated in the following way: - Calculate the 32-bit CRC for the VLAN tag or ID (For steps to calculate CRC32, see Section 3.2.8 of IEEE 802.3). - Perform bitwise reversal for the value obtained in step 1. - Take the upper four bits from the value obtained in step 2. If the VLAN hash Table register is configured to be double-synchronized to the (G)MII clock domain, the synchronization is triggered only when Bits[15:8] (in little-endian mode) or Bits[7:0] (in big-endian mode) of this register are written. - If double-synchronization is enabled, consecutive writes to this register should be performed after at least four clock cycles in the destination clock domain. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3648 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3649-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_16<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>VLHT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16|Reserved.|
|Reserved_31_1<br>6||
|15-0|VLAN Hash Table This field contains the 16-bit VLAN Hash Table.|
|VLHT||



### 75.7.49 (MAC_VLAN_Incl) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Incl|60h|



##### Function 

The VLAN Tag Inclusion or Replacement register contains the VLAN tag for insertion or replacement in the Transmit packets. It also contains the VLAN tag insertion controls. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3649 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3650-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserved_23_2<br>R BUSY  Reserved_29_y<br>2<br>RDWR  ADDR  CBTI  VLTI  CSVL  VLP  VLC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>VLT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31<br>BUSY|Busy This bit indicates the status of the read/write operation of indirect access to the queue/channel<br>specific VLAN inclusion register. For write operation write to a register is complete when this bit is reset.<br>For read operation the read data is valid when the bit is reset. The application must make sure that this<br>bit is reset before attempting subsequent access to this register.<br>0b - Busy status not detected<br>1b - Busy status detected|
|30<br>RDWR|Read write control This bit controls the read or write operation for indirectly accessing the queue/channel<br>specific VLAN Inclusion register. When set indicates write operation and when reset indicates read<br>operation. This does not have any effect when CBTI is reset.<br>0b - Read operation of indirect access<br>1b - Write operation of indirect access|
|29-26<br>Reserved_29_y|Reserved.|
|25-24<br>ADDR|Address This field selects one of the queue/channel specific VLAN Inclusion register for read/write<br>access. This does not have any effect when CBTI is reset.|
|23-22<br>Reserved_23_2<br>2|Reserved.|
|21<br>CBTI|Channel based tag insertion When this bit is set, outer VLAN tag is inserted for every packets<br>transmitted by the MAC. The tag value is taken from the queue/channel specific VLAN tag register.<br>The VLTI, VLP, VLC, and VLT fields of this register are ignored when this bit is set. When this bit is set,<br>a write operation to byte 3 of this register initiates the read/write access to the indirect register. When<br>reset, outer VLAN operation is based on the setting of VLTI, VLP, VLC and VLT fields of this register.<br>0b - Channel based tag insertion is disabled<br>1b - Channel based tag insertion is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3650 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|20<br>VLTI|VLAN Tag Input When this bit is set, it indicates that the VLAN tag to be inserted or replaced in Tx<br>packet should be taken from: - The Tx descriptor<br>0b - VLAN Tag Input is disabled<br>1b - VLAN Tag Input is enabled|
|19<br>CSVL|C-VLAN or S-VLAN When this bit is set, S-VLAN type (0x88A8) is inserted or replaced in the 13th and<br>14th bytes of transmitted packets. When this bit is reset, C-VLAN type (0x8100) is inserted or replaced in<br>the 13th and 14th bytes of transmitted packets.<br>0b - C-VLAN type (0x8100) is inserted or replaced<br>1b - S-VLAN type (0x88A8) is inserted or replaced|
|18<br>VLP|VLAN Priority Control When this bit is set, the control bits[17:16] are used for VLAN deletion, insertion, or<br>replacement. When this bit is reset, the mti_vlan_ctrl_i control input is used and bits[17:16] are ignored.<br>0b - VLAN Priority Control is disabled<br>1b - VLAN Priority Control is enabled|
|17-16<br>VLC|VLAN Tag Control in Transmit Packets - 2'b00: No VLAN tag deletion, insertion, or replacement - 2'b01:<br>VLAN tag deletion The MAC removes the VLAN type (bytes 13 and 14) and VLAN tag (bytes 15 and<br>16) of all transmitted packets with VLAN tags. - 2'b10: VLAN tag insertion The MAC inserts VLT in bytes<br>15 and 16 of the packet after inserting the Type value (0x8100 or 0x88a8) in bytes 13 and 14. This<br>operation is performed on all transmitted packets, irrespective of whether they already have a VLAN tag.<br>- 2'b11: VLAN tag replacement The MAC replaces VLT in bytes 15 and 16 of all VLAN-type transmitted<br>packets (Bytes 13 and 14 are 0x8100 or 0x88a8). Note: Changes to this field take effect only on the start<br>of a packet. If you write this register field when a packet is being transmitted, only the subsequent packet<br>can use the updated value, that is, the current packet does not use the updated value.<br>00b - No VLAN tag deletion, insertion, or replacement<br>01b - VLAN tag deletion<br>10b - VLAN tag insertion<br>11b - VLAN tag replacement|
|15-0<br>VLT|VLAN Tag for Transmit Packets This field contains the value of the VLAN tag to be inserted or replaced.<br>The value must only be changed when the transmit lines are inactive or during the initialization phase.<br>Bits[15:13] are the User Priority field, Bit 12 is the CFI/DEI field, and Bits[11:0] are the VID field in the<br>VLAN tag. The following list describes the bits of this field: - Bits[15:13]: User Priority - Bit 12: Canonical<br>Format Indicator (CFI) or Drop Eligible Indicator (DEI) - Bits[11:0]: VLAN Identifier (VID) field of VLAN tag|



### 75.7.50 (MAC_VLAN_Incl0) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Incl0|60h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3651 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Function 

The Tx Queue ${i} VLAN Tag Inclusion register contains the VLAN tag for insertion in the Transmit packets from Tx Queue ${i}. It also contains the VLAN tag insertion controls. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||Reserve|d_31_20||||||CSVL|Res|erved_18|_16|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||V|LT||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-20|Reserved.|
|Reserved_31_2<br>0||
|19<br>CSVL|C-VLAN or S-VLAN When this bit is set, S-VLAN type (0x88A8) is inserted in the 13th and 14th bytes of<br>transmitted packets. When this bit is reset, C-VLAN type (0x8100) is inserted in the 13th and 14th bytes<br>of transmitted packets.<br>0b - C-VLAN type (0x8100) is inserted<br>1b - S-VLAN type (0x88A8) is inserted|
|18-16|Reserved.|
|Reserved_18_1<br>6||
|15-0<br>VLT|VLAN Tag for Transmit Packets This field contains the value of the VLAN tag to be inserted. The value<br>must only be changed when the transmit lines are inactive or during the initialization phase. Bits[15:13]<br>are the User Priority field, Bit 12 is the CFI/DEI field, and Bits[11:0] are the VID field in the VLAN tag.<br>The following list describes the bits of this field: - Bits[15:13]: User Priority - Bit 12: Canonical Format<br>Indicator (CFI) or Drop Eligible Indicator (DEI) - Bits[11:0]: VLAN Identifier (VID) field of VLAN tag|



### 75.7.51 (MAC_VLAN_Incl1) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Incl1|60h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3652 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Function 

The Tx Queue ${i} VLAN Tag Inclusion register contains the VLAN tag for insertion in the Transmit packets from Tx Queue ${i}. It also contains the VLAN tag insertion controls. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||Reserve|d_31_20||||||CSVL|Res|erved_18|_16|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||V|LT||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-20|Reserved.|
|Reserved_31_2<br>0||
|19<br>CSVL|C-VLAN or S-VLAN When this bit is set, S-VLAN type (0x88A8) is inserted in the 13th and 14th bytes of<br>transmitted packets. When this bit is reset, C-VLAN type (0x8100) is inserted in the 13th and 14th bytes<br>of transmitted packets.<br>0b - C-VLAN type (0x8100) is inserted<br>1b - S-VLAN type (0x88A8) is inserted|
|18-16|Reserved.|
|Reserved_18_1<br>6||
|15-0<br>VLT|VLAN Tag for Transmit Packets This field contains the value of the VLAN tag to be inserted. The value<br>must only be changed when the transmit lines are inactive or during the initialization phase. Bits[15:13]<br>are the User Priority field, Bit 12 is the CFI/DEI field, and Bits[11:0] are the VID field in the VLAN tag.<br>The following list describes the bits of this field: - Bits[15:13]: User Priority - Bit 12: Canonical Format<br>Indicator (CFI) or Drop Eligible Indicator (DEI) - Bits[11:0]: VLAN Identifier (VID) field of VLAN tag|



### 75.7.52 (MAC_VLAN_Incl2) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Incl2|60h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3653 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Function 

The Tx Queue ${i} VLAN Tag Inclusion register contains the VLAN tag for insertion in the Transmit packets from Tx Queue ${i}. It also contains the VLAN tag insertion controls. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||Reserve|d_31_20||||||CSVL|Res|erved_18|_16|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||V|LT||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-20|Reserved.|
|Reserved_31_2<br>0||
|19<br>CSVL|C-VLAN or S-VLAN When this bit is set, S-VLAN type (0x88A8) is inserted in the 13th and 14th bytes of<br>transmitted packets. When this bit is reset, C-VLAN type (0x8100) is inserted in the 13th and 14th bytes<br>of transmitted packets.<br>0b - C-VLAN type (0x8100) is inserted<br>1b - S-VLAN type (0x88A8) is inserted|
|18-16|Reserved.|
|Reserved_18_1<br>6||
|15-0<br>VLT|VLAN Tag for Transmit Packets This field contains the value of the VLAN tag to be inserted. The value<br>must only be changed when the transmit lines are inactive or during the initialization phase. Bits[15:13]<br>are the User Priority field, Bit 12 is the CFI/DEI field, and Bits[11:0] are the VID field in the VLAN tag.<br>The following list describes the bits of this field: - Bits[15:13]: User Priority - Bit 12: Canonical Format<br>Indicator (CFI) or Drop Eligible Indicator (DEI) - Bits[11:0]: VLAN Identifier (VID) field of VLAN tag|



### 75.7.53 (MAC_VLAN_Incl3) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Incl3|60h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3654 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Function 

The Tx Queue ${i} VLAN Tag Inclusion register contains the VLAN tag for insertion in the Transmit packets from Tx Queue ${i}. It also contains the VLAN tag insertion controls. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||Reserve|d_31_20||||||CSVL|Res|erved_18|_16|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||V|LT||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-20|Reserved.|
|Reserved_31_2<br>0||
|19<br>CSVL|C-VLAN or S-VLAN When this bit is set, S-VLAN type (0x88A8) is inserted in the 13th and 14th bytes of<br>transmitted packets. When this bit is reset, C-VLAN type (0x8100) is inserted in the 13th and 14th bytes<br>of transmitted packets.<br>0b - C-VLAN type (0x8100) is inserted<br>1b - S-VLAN type (0x88A8) is inserted|
|18-16|Reserved.|
|Reserved_18_1<br>6||
|15-0<br>VLT|VLAN Tag for Transmit Packets This field contains the value of the VLAN tag to be inserted. The value<br>must only be changed when the transmit lines are inactive or during the initialization phase. Bits[15:13]<br>are the User Priority field, Bit 12 is the CFI/DEI field, and Bits[11:0] are the VID field in the VLAN tag.<br>The following list describes the bits of this field: - Bits[15:13]: User Priority - Bit 12: Canonical Format<br>Indicator (CFI) or Drop Eligible Indicator (DEI) - Bits[11:0]: VLAN Identifier (VID) field of VLAN tag|



### 75.7.54 (MAC_VLAN_Incl4) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Incl4|60h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3655 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Function 

The Tx Queue ${i} VLAN Tag Inclusion register contains the VLAN tag for insertion in the Transmit packets from Tx Queue ${i}. It also contains the VLAN tag insertion controls. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||Reserve|d_31_20||||||CSVL|Res|erved_18|_16|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||V|LT||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-20|Reserved.|
|Reserved_31_2<br>0||
|19<br>CSVL|C-VLAN or S-VLAN When this bit is set, S-VLAN type (0x88A8) is inserted in the 13th and 14th bytes of<br>transmitted packets. When this bit is reset, C-VLAN type (0x8100) is inserted in the 13th and 14th bytes<br>of transmitted packets.<br>0b - C-VLAN type (0x8100) is inserted<br>1b - S-VLAN type (0x88A8) is inserted|
|18-16|Reserved.|
|Reserved_18_1<br>6||
|15-0<br>VLT|VLAN Tag for Transmit Packets This field contains the value of the VLAN tag to be inserted. The value<br>must only be changed when the transmit lines are inactive or during the initialization phase. Bits[15:13]<br>are the User Priority field, Bit 12 is the CFI/DEI field, and Bits[11:0] are the VID field in the VLAN tag.<br>The following list describes the bits of this field: - Bits[15:13]: User Priority - Bit 12: Canonical Format<br>Indicator (CFI) or Drop Eligible Indicator (DEI) - Bits[11:0]: VLAN Identifier (VID) field of VLAN tag|



### 75.7.55 (MAC_VLAN_Incl5) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Incl5|60h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3656 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Function 

The Tx Queue ${i} VLAN Tag Inclusion register contains the VLAN tag for insertion in the Transmit packets from Tx Queue ${i}. It also contains the VLAN tag insertion controls. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||Reserve|d_31_20||||||CSVL|Res|erved_18|_16|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||V|LT||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-20|Reserved.|
|Reserved_31_2<br>0||
|19<br>CSVL|C-VLAN or S-VLAN When this bit is set, S-VLAN type (0x88A8) is inserted in the 13th and 14th bytes of<br>transmitted packets. When this bit is reset, C-VLAN type (0x8100) is inserted in the 13th and 14th bytes<br>of transmitted packets.<br>0b - C-VLAN type (0x8100) is inserted<br>1b - S-VLAN type (0x88A8) is inserted|
|18-16|Reserved.|
|Reserved_18_1<br>6||
|15-0<br>VLT|VLAN Tag for Transmit Packets This field contains the value of the VLAN tag to be inserted. The value<br>must only be changed when the transmit lines are inactive or during the initialization phase. Bits[15:13]<br>are the User Priority field, Bit 12 is the CFI/DEI field, and Bits[11:0] are the VID field in the VLAN tag.<br>The following list describes the bits of this field: - Bits[15:13]: User Priority - Bit 12: Canonical Format<br>Indicator (CFI) or Drop Eligible Indicator (DEI) - Bits[11:0]: VLAN Identifier (VID) field of VLAN tag|



### 75.7.56 (MAC_VLAN_Incl6) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Incl6|60h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3657 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Function 

The Tx Queue ${i} VLAN Tag Inclusion register contains the VLAN tag for insertion in the Transmit packets from Tx Queue ${i}. It also contains the VLAN tag insertion controls. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||Reserve|d_31_20||||||CSVL|Res|erved_18|_16|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||V|LT||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-20|Reserved.|
|Reserved_31_2<br>0||
|19<br>CSVL|C-VLAN or S-VLAN When this bit is set, S-VLAN type (0x88A8) is inserted in the 13th and 14th bytes of<br>transmitted packets. When this bit is reset, C-VLAN type (0x8100) is inserted in the 13th and 14th bytes<br>of transmitted packets.<br>0b - C-VLAN type (0x8100) is inserted<br>1b - S-VLAN type (0x88A8) is inserted|
|18-16|Reserved.|
|Reserved_18_1<br>6||
|15-0<br>VLT|VLAN Tag for Transmit Packets This field contains the value of the VLAN tag to be inserted. The value<br>must only be changed when the transmit lines are inactive or during the initialization phase. Bits[15:13]<br>are the User Priority field, Bit 12 is the CFI/DEI field, and Bits[11:0] are the VID field in the VLAN tag.<br>The following list describes the bits of this field: - Bits[15:13]: User Priority - Bit 12: Canonical Format<br>Indicator (CFI) or Drop Eligible Indicator (DEI) - Bits[11:0]: VLAN Identifier (VID) field of VLAN tag|



### 75.7.57 (MAC_VLAN_Incl7) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Incl7|60h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3658 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Function 

The Tx Queue ${i} VLAN Tag Inclusion register contains the VLAN tag for insertion in the Transmit packets from Tx Queue ${i}. It also contains the VLAN tag insertion controls. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||Reserve|d_31_20||||||CSVL|Res|erved_18|_16|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||V|LT||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-20|Reserved.|
|Reserved_31_2<br>0||
|19<br>CSVL|C-VLAN or S-VLAN When this bit is set, S-VLAN type (0x88A8) is inserted in the 13th and 14th bytes of<br>transmitted packets. When this bit is reset, C-VLAN type (0x8100) is inserted in the 13th and 14th bytes<br>of transmitted packets.<br>0b - C-VLAN type (0x8100) is inserted<br>1b - S-VLAN type (0x88A8) is inserted|
|18-16|Reserved.|
|Reserved_18_1<br>6||
|15-0<br>VLT|VLAN Tag for Transmit Packets This field contains the value of the VLAN tag to be inserted. The value<br>must only be changed when the transmit lines are inactive or during the initialization phase. Bits[15:13]<br>are the User Priority field, Bit 12 is the CFI/DEI field, and Bits[11:0] are the VID field in the VLAN tag.<br>The following list describes the bits of this field: - Bits[15:13]: User Priority - Bit 12: Canonical Format<br>Indicator (CFI) or Drop Eligible Indicator (DEI) - Bits[11:0]: VLAN Identifier (VID) field of VLAN tag|



### 75.7.58 (MAC_Inner_VLAN_Incl) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Inner_VLAN_Incl|64h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3659 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Function 

The Inner VLAN Tag Inclusion or Replacement register contains the inner VLAN tag to be inserted or replaced in the Transmit packet. It also contains the inner VLAN tag insertion controls. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||||Res|erved_31|_21|||||VLTI|CSVL|VLP|VLC|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R<br>W||||||||V|LT|||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



##### Fields 

|Field|Function|
|---|---|
|31-21|Reserved.|
|Reserved_31_2<br>1||
|20<br>VLTI|VLAN Tag Input When this bit is set, it indicates that the VLAN tag to be inserted or replaced in Tx<br>packet should be taken from: - The Tx descriptor<br>0b - VLAN Tag Input is disabled<br>1b - VLAN Tag Input is enabled|
|19<br>CSVL|C-VLAN or S-VLAN When this bit is set, S-VLAN type (0x88A8) is inserted or replaced in the 17th and<br>18th bytes of transmitted packets. When this bit is reset, C-VLAN type (0x8100) is inserted or replaced in<br>the 17th and 18th bytes of transmitted packets.<br>0b - C-VLAN type (0x8100) is inserted<br>1b - S-VLAN type (0x88A8) is inserted|
|18<br>VLP|VLAN Priority Control When this bit is set, the VLC field is used for VLAN deletion, insertion, or<br>replacement. When this bit is reset, the mti_vlan_ctrl_i control input is used and the VLC field is ignored.<br>0b - VLAN Priority Control is disabled<br>1b - VLAN Priority Control is enabled|
|17-16<br>VLC|VLAN Tag Control in Transmit Packets - 2'b00: No VLAN tag deletion, insertion, or replacement - 2'b01:<br>VLAN tag deletion The MAC removes the VLAN type (bytes 17 and 18) and VLAN tag (bytes 19 and<br>20) of all transmitted packets with VLAN tags. - 2'b10: VLAN tag insertion The MAC inserts VLT in bytes<br>19 and 20 of the packet after inserting the Type value (0x8100 or 0x88a8) in bytes 17 and 18. This<br>operation is performed on all transmitted packets, irrespective of whether they already have a VLAN tag.<br>- 2'b11: VLAN tag replacement The MAC replaces VLT in bytes 19 and 20 of all VLAN-type transmitted<br>packets (Bytes 17 and 18 are 0x8100 or 0x88a8). Note: Changes to this field take effect only on the start|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3660 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||of a packet. If you write this register field when a packet is being transmitted, only the subsequent packet<br>can use the updated value, that is, the current packet does not use the updated value.<br>00b - No VLAN tag deletion, insertion, or replacement<br>01b - VLAN tag deletion<br>10b - VLAN tag insertion|
||11b - VLAN tag replacement|
|15-0<br>VLT|VLAN Tag for Transmit Packets This field contains the value of the VLAN tag to be inserted or replaced.<br>The value must only be changed when the transmit lines are inactive or during the initialization phase.<br>Bits[15:13] are the User Priority field, Bit 12 is the CFI/DEI field, and Bits[11:0] are the VID field in the<br>VLAN tag. The following list describes the bits of this field: - Bits[15:13]: User Priority - Bit 12: Canonical<br>Format Indicator (CFI) or Drop Eligible Indicator (DEI) - Bits[11:0]: VLAN Identifier (VID) field of VLAN tag|



### 75.7.59 (MAC_Q0_Tx_Flow_Ctrl) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Q0_Tx_Flow_Ctrl|70h|



##### Function 

The Flow Control register controls the generation and reception of the Control (Pause Command) packets by the Flow control module of the MAC. A Write to a register with the Busy bit set to 1 triggers the Flow Control block to generate a Pause packet. The fields of the control packet are selected as specified in the 802.3x specification, and the Pause Time value from this register is used in the Pause Time field of the control packet. The Busy bit remains set until the control packet is transferred onto the cable. The application must make sure that the Busy bit is cleared before writing to the register. When the PFCE bit in the MAC_Rx_Flow_Ctrl register is enabled, this register controls the generation of Priority Flow Control (PFC) frames with priorities mapped according to PSRQ0 in the MAC_RxQ_Ctrl2 register. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||P|T||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||Reserve|d_15_8||||DZPQ||PLT||Reserve|d_3_2|TFE|FCB_|
|W||||||||||||||||BPA|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3661 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Fields 

|Field|Function|
|---|---|
|31-16<br>PT|Pause Time This field holds the value to be used in the Pause Time field in the Tx control packet. If<br>the Pause Time bits are configured to be double-synchronized to the (G)MII clock domain, consecutive<br>writes to this register should be performed only after at least four clock cycles in the destination clock<br>domain.|
|15-8|Reserved.|
|Reserved_15_8||
|7<br>DZPQ|Disable Zero-Quanta Pause When this bit is set, it disables the automatic generation of the zero-quanta<br>Pause packets on de-assertion of the flow-control signal from the FIFO layer (MTL or external sideband<br>flow control signal sbd_flowctrl_i or mti_flowctrl_i). When this bit is reset, normal operation with automatic<br>zero-quanta Pause packet generation is enabled.<br>0b - Zero-Quanta Pause packet generation is enabled<br>1b - Zero-Quanta Pause packet generation is disabled|
|6-4<br>PLT|Pause Low Threshold This field configures the threshold of the Pause timer at which the input flow<br>control signal mti_flowctrl_i (or sbd_flowctrl_i) is checked for automatic retransmission of the Pause<br>packet. The threshold values should be always less than the Pause Time configured in Bits[31:16].<br>For example, if PT = 100H (256 slot times), and PLT = 001, a second Pause packet is automatically<br>transmitted if the mti_flowctrl_i signal is asserted at 228 (256-28) slot times after the first Pause packet<br>is transmitted. The following list provides the threshold values for different values. The slot time is<br>defined as the time taken to transmit 512 bits (64 bytes) on the GMII or MII interface. This (approximate)<br>computation is based on the packet size (64, 1518, 2000, 9018, 16384, or 32768) + 2 Pause Packet Size<br>+ IPG in Slot Times.<br>000b - Pause Time minus 4 Slot Times (PT -4 slot times)<br>001b - Pause Time minus 28 Slot Times (PT -28 slot times)<br>010b - Pause Time minus 36 Slot Times (PT -36 slot times)<br>011b - Pause Time minus 144 Slot Times (PT -144 slot times)<br>100b - Pause Time minus 256 Slot Times (PT -256 slot times)<br>101b - Pause Time minus 512 Slot Times (PT -512 slot times)<br>110b - Reserved|
|3-2<br>Reserved_3_2|Reserved.|
|1<br>TFE|Transmit Flow Control Enable Full-Duplex Mode: In the full-duplex mode, when this bit is set, the MAC<br>enables the flow control operation to Tx Pause packets. When this bit is reset, the flow control operation<br>in the MAC is disabled, and the MAC does not transmit any Pause packets. Half-Duplex Mode: In the<br>half-duplex mode, when this bit is set, the MAC enables the backpressure operation. When this bit is<br>reset, the backpressure feature is disabled.<br>0b - Transmit Flow Control is disabled<br>1b - Transmit Flow Control is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3662 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|0<br>FCB_BPA|Flow Control Busy or Backpressure Activate This bit initiates a Pause packet in the full-duplex mode<br>and activates the backpressure function in the half-duplex mode if the TFE bit is set. Full-Duplex Mode:<br>In the full-duplex mode, this bit should be read as 1'b0 before writing to this register. To initiate a<br>Pause packet, the application must set this bit to 1'b1. During Control packet transfer, this bit continues<br>to be set to indicate that a packet transmission is in progress. When Pause packet transmission is<br>complete, the MAC resets this bit to 1'b0. You should not write to this register until this bit is cleared.<br>Half-Duplex Mode: When this bit is set (and TFE bit is set) in the half-duplex mode, the MAC asserts<br>the backpressure. During backpressure, when the MAC receives a new packet, the transmitter starts<br>sending a JAM pattern resulting in a collision. This control register bit is logically ORed with the<br>mti_flowctrl_i input signal for the backpressure function. When the MAC is configured for the full-duplex<br>mode, the BPA is automatically disabled. Access restriction applies. Setting 1 sets. Self-cleared. Setting<br>0 has no effect.<br>0b - Flow Control Busy or Backpressure Activate is disabled<br>1b - Flow Control Busy or Backpressure Activate is enabled|



### 75.7.60 (MAC_Q1_Tx_Flow_Ctrl) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Q1_Tx_Flow_Ctrl|74h|



##### Function 

This register controls the generation of PFC Control packets of priorities mapped as per the PSRQi field in the MAC_RxQ_Ctrl2/MAC_RxQ_Ctrl3 registers. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||P|T||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||Reserve|d_15_8||||DZPQ||PLT||Reserve|d_3_2|TFE|FCB_|
|W||||||||||||||||BPA|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3663 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Fields 

|Field|Function|
|---|---|
|31-16<br>PT|Pause Time This field holds the value to be used in the Pause Time field in the Tx control packet. If<br>the Pause Time bits are configured to be double-synchronized to the (G)MII clock domain, consecutive<br>writes to this register should be performed only after at least four clock cycles in the destination clock<br>domain.|
|15-8|Reserved.|
|Reserved_15_8||
|7<br>DZPQ|Disable Zero-Quanta Pause When this bit is set, it disables the automatic generation of the zero-quanta<br>Pause packets on de-assertion of the flow-control signal from the FIFO layer (MTL or external sideband<br>flow control signal sbd_flowctrl_i or mti_flowctrl_i). When this bit is reset, normal operation with automatic<br>zero-quanta Pause packet generation is enabled.<br>0b - Zero-Quanta Pause packet generation is enabled<br>1b - Zero-Quanta Pause packet generation is disabled|
|6-4<br>PLT|Pause Low Threshold This field configures the threshold of the Pause timer at which the input flow<br>control signal mti_flowctrl_i (or sbd_flowctrl_i) is checked for automatic retransmission of the Pause<br>packet. The threshold values should be always less than the Pause Time configured in Bits[31:16].<br>For example, if PT = 100H (256 slot times), and PLT = 001, a second Pause packet is automatically<br>transmitted if the mti_flowctrl_i signal is asserted at 228 (256-28) slot times after the first Pause packet<br>is transmitted. The following list provides the threshold values for different values. The slot time is<br>defined as the time taken to transmit 512 bits (64 bytes) on the GMII or MII interface. This (approximate)<br>computation is based on the packet size (64, 1518, 2000, 9018, 16384, or 32768) + 2 Pause Packet Size<br>+ IPG in Slot Times.<br>000b - Pause Time minus 4 Slot Times (PT -4 slot times)<br>001b - Pause Time minus 28 Slot Times (PT -28 slot times)<br>010b - Pause Time minus 36 Slot Times (PT -36 slot times)<br>011b - Pause Time minus 144 Slot Times (PT -144 slot times)<br>100b - Pause Time minus 256 Slot Times (PT -256 slot times)<br>101b - Pause Time minus 512 Slot Times (PT -512 slot times)<br>110b - Reserved|
|3-2<br>Reserved_3_2|Reserved.|
|1<br>TFE|Transmit Flow Control Enable When this bit is set in full-duplex mode, the MAC enables the flow control<br>operation to Tx pause packets. When this bit is reset, the flow control operation in the MAC is disabled,<br>and the MAC does not transmit any pause packets.<br>0b - Transmit Flow Control is disabled<br>1b - Transmit Flow Control is enabled|
|0<br>FCB_BPA|Flow Control Busy This bit initiates a PFC packet if the TFE bit is set. To initiate a PFC packet, the<br>application must set this bit to 1'b1. During Control packet transfer, this bit continues to be set to indicate<br>that a packet transmission is in progress. When PFC packet transmission is complete, the MAC resets|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3664 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||this bit to 1'b0. You should not write to this register until this bit is cleared. Access restriction applies.<br>Setting 1 sets. Self-cleared. Setting 0 has no effect.|
||0b - Flow Control Busy or Backpressure Activate is disabled|
||1b - Flow Control Busy or Backpressure Activate is enabled|



### 75.7.61 (MAC_Q2_Tx_Flow_Ctrl) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Q2_Tx_Flow_Ctrl|78h|



##### Function 

This register controls the generation of PFC Control packets of priorities mapped as per the PSRQi field in the MAC_RxQ_Ctrl2/MAC_RxQ_Ctrl3 registers. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||P|T||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||Reserve|d_15_8||||DZPQ||PLT||Reserve|d_3_2|TFE|FCB_|
|W||||||||||||||||BPA|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-16<br>PT|Pause Time This field holds the value to be used in the Pause Time field in the Tx control packet. If<br>the Pause Time bits are configured to be double-synchronized to the (G)MII clock domain, consecutive<br>writes to this register should be performed only after at least four clock cycles in the destination clock<br>domain.|
|15-8|Reserved.|
|Reserved_15_8||
|7|Disable Zero-Quanta Pause When this bit is set, it disables the automatic generation of the zero-quanta<br>Pause packets on de-assertion of the flow-control signal from the FIFO layer (MTL or external sideband|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3665 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|DZPQ|flow control signal sbd_flowctrl_i or mti_flowctrl_i). When this bit is reset, normal operation with automatic<br>zero-quanta Pause packet generation is enabled.<br>0b - Zero-Quanta Pause packet generation is enabled<br>1b - Zero-Quanta Pause packet generation is disabled|
|6-4<br>PLT|Pause Low Threshold This field configures the threshold of the Pause timer at which the input flow<br>control signal mti_flowctrl_i (or sbd_flowctrl_i) is checked for automatic retransmission of the Pause<br>packet. The threshold values should be always less than the Pause Time configured in Bits[31:16].<br>For example, if PT = 100H (256 slot times), and PLT = 001, a second Pause packet is automatically<br>transmitted if the mti_flowctrl_i signal is asserted at 228 (256-28) slot times after the first Pause packet<br>is transmitted. The following list provides the threshold values for different values. The slot time is<br>defined as the time taken to transmit 512 bits (64 bytes) on the GMII or MII interface. This (approximate)<br>computation is based on the packet size (64, 1518, 2000, 9018, 16384, or 32768) + 2 Pause Packet Size<br>+ IPG in Slot Times.<br>000b - Pause Time minus 4 Slot Times (PT -4 slot times)<br>001b - Pause Time minus 28 Slot Times (PT -28 slot times)<br>010b - Pause Time minus 36 Slot Times (PT -36 slot times)<br>011b - Pause Time minus 144 Slot Times (PT -144 slot times)<br>100b - Pause Time minus 256 Slot Times (PT -256 slot times)<br>101b - Pause Time minus 512 Slot Times (PT -512 slot times)<br>110b - Reserved|
|3-2|Reserved.|
|Reserved_3_2||
|1<br>TFE|Transmit Flow Control Enable When this bit is set in full-duplex mode, the MAC enables the flow control<br>operation to Tx pause packets. When this bit is reset, the flow control operation in the MAC is disabled,<br>and the MAC does not transmit any pause packets.<br>0b - Transmit Flow Control is disabled<br>1b - Transmit Flow Control is enabled|
|0<br>FCB_BPA|Flow Control Busy This bit initiates a PFC packet if the TFE bit is set. To initiate a PFC packet, the<br>application must set this bit to 1'b1. During Control packet transfer, this bit continues to be set to indicate<br>that a packet transmission is in progress. When PFC packet transmission is complete, the MAC resets<br>this bit to 1'b0. You should not write to this register until this bit is cleared. Access restriction applies.<br>Setting 1 sets. Self-cleared. Setting 0 has no effect.<br>0b - Flow Control Busy or Backpressure Activate is disabled<br>1b - Flow Control Busy or Backpressure Activate is enabled|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3666 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

### 75.7.62 (MAC_Rx_Flow_Ctrl) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Rx_Flow_Ctrl|90h|



##### Function 

The Receive Flow Control register controls the pausing of MAC Transmit based on the received Pause packet. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3667-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_9<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_31_9  Reserved_7_2<br>PFCE  UP  RFE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-9|Reserved.|
|Reserved_31_9||
|8<br>PFCE|Priority Based Flow Control Enable When this bit is set, it enables generation and reception of priority-<br>based flow control (PFC) packets. When this bit is reset, it enables generation and reception of 802.3x<br>Pause control packets.<br>0b - Priority Based Flow Control is disabled<br>1b - Priority Based Flow Control is enabled|
|7-2|Reserved.|
|Reserved_7_2||
|1<br>UP|Unicast Pause Packet Detect A pause packet is processed when it has the unique multicast address<br>specified in the IEEE 802.3. When this bit is set, the MAC can also detect Pause packets with<br>unicast address of the station. This unicast address should be as specified in MAC_Address0_High and<br>MAC_Address0_Low. When this bit is reset, the MAC only detects Pause packets with unique multicast<br>address. Note: The MAC does not process a Pause packet if the multicast address is different from<br>the unique multicast address. This is also applicable to the received PFC packet when the Priority Flow<br>Control (PFC) is enabled. The unique multicast address (0x01_80_C2_00_00_01) is as specified in IEEE<br>802.1 Qbb-2011.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3667 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Unicast Pause Packet Detect disabled<br>1b - Unicast Pause Packet Detect enabled|
|0<br>RFE|Receive Flow Control Enable When this bit is set and the MAC is operating in full-duplex mode, the<br>MAC decodes the received Pause packet and disables its transmitter for a specified (Pause) time. When<br>this bit is reset or the MAC is operating in half-duplex mode, the decode function of the Pause packet<br>is disabled. When PFC is enabled, flow control is enabled for PFC packets. The MAC decodes the<br>received PFC packet and disables the Transmit queue, with matching priorities, for a duration of received<br>Pause time.|
||0b - Receive Flow Control is disabled|
||1b - Receive Flow Control is enabled|



### 75.7.63 (MAC_RxQ_Ctrl4) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_RxQ_Ctrl4|94h|



##### Function 

The Receive Queue Control 4 register controls the routing of unicast and multicast packets that fail the Destination or Source address filter to the Rx queues. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3668-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_y  VFFQ<br>VFFQ<br>E<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_15_y  MFFQ Reserved_7_y  UFFQ<br>MFFQ  UFFQ<br>E  E<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-19|Reserved.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3668 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field<br>Reserved_31_y|Function|
|---|---|
|18-17<br>VFFQ|VLAN Tag Filter Fail Packets Queue This field holds the Rx queue number to which the tagged packets<br>failing the Destination or Source Address filter (and UFFQE/MFFQE not enabled) or failing the VLAN tag<br>filter must be routed to. This field is valid only when the VFFQE bit is set.|
|16<br>VFFQE|VLAN Tag Filter Fail Packets Queuing Enable When this bit is set, the tagged packets which fail the<br>Destination or Source address filter or fail the VLAN tag filter, are routed to the Rx Queue Number<br>programmed in the VFFQ. When this bit is reset, the tagged packets which fail the Destination or Source<br>address filter or fail the VLAN tag filter are routed based on other routing options. This bit is valid only<br>when the RA bit of the MAC_Packet_Filter register is set.<br>0b - VLAN tag Filter Fail Packets Queuing is disabled<br>1b - VLAN tag Filter Fail Packets Queuing is enabled|
|15-11|Reserved.|
|Reserved_15_y||
|10-9<br>MFFQ|Multicast Address Filter Fail Packets Queue. This field holds the Rx queue number to which the Multicast<br>packets failing the Destination or Source Address filter are routed to. This field is valid only when the<br>MFFQE bit is set.|
|8<br>MFFQE|Multicast Address Filter Fail Packets Queuing Enable. When this bit is set, the Multicast packets which<br>fail the Destination or Source address filter is routed to the Rx Queue Number programmed in the MFFQ.<br>When this bit is reset, the Multicast packets which fail the Destination or Source address filter is routed<br>based on other routing options. This bit is valid only when the RA bit of the MAC_Packet_Filter register is<br>set.<br>0b - Multicast Address Filter Fail Packets Queuing is disabled<br>1b - Multicast Address Filter Fail Packets Queuing is enabled|
|7-3<br>Reserved_7_y|Reserved.|
|2-1<br>UFFQ|Unicast Address Filter Fail Packets Queue. This field holds the Rx queue number to which the Unicast<br>packets failing the Destination or Source Address filter are routed to. This field is valid only when the<br>UFFQE bit is set.|
|0<br>UFFQE|Unicast Address Filter Fail Packets Queuing Enable. When this bit is set, the Unicast packets which fail<br>the Destination or Source address filter is routed to the Rx Queue Number programmed in the UFFQ.<br>When this bit is reset, the Unicast packets which fail the Destination or Source address filter is routed<br>based on other routing options. This bit is valid only when the RA bit of the MAC_Packet_Filter register is<br>set.<br>0b - Unicast Address Filter Fail Packets Queuing is disabled<br>1b - Unicast Address Filter Fail Packets Queuing is enabled|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3669 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

### 75.7.64 (MAC_TxQ_Prty_Map0) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_TxQ_Prty_Map0|98h|



##### Function 

The Transmit Queue Priority Mapping 0 register contains the priority values assigned to Tx Queue 0 through Tx Queue 3. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||Reserve|d_PSTQ3|||||||PST|Q2||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||PS|TQ1|||||||PST|Q0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-24|Reserved.|
|Reserved_PST<br>Q3||
|23-16<br>PSTQ2|Priorities Selected in Transmit Queue 2 This bit is similar to the PSTQ0 bit.|
|15-8<br>PSTQ1|Priorities Selected in Transmit Queue 1 This bit is similar to the PSTQ0 bit.|
|7-0<br>PSTQ0|Priorities Selected in Transmit Queue 0 This field holds the priorities assigned to Tx Queue 0 by the<br>software. This field determines if Tx Queue 0 should be blocked from transmitting specified pause time<br>when a PFC packet is received with priorities matching the priorities programmed in this field. If the<br>content of this field is not mutually exclusive to the corresponding fields of other Transmit queues, that is,<br>same priority is mapped to multiple Tx queues, the MAC blocks all queues with matching priority, for the<br>specified time.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3670 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

### 75.7.65 (MAC_RxQ_Ctrl0) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_RxQ_Ctrl0|A0h|



##### Function 

The Receive Queue Control 0 register controls the queue management in the MAC Receiver. Note: In multiple Rx queues configuration, all the queues are disabled by default. Enable the Rx queue by programming the corresponding field in this register. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3671-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_16<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserved_RXQ Reserved_RXQ Reserved_RXQ Reserved_RXQ Reserved_RXQ<br>R<br>7EN  6EN  5EN  4EN  3EN  RXQ2EN  RXQ1EN  RXQ0EN<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16|Reserved.|
|Reserved_31_1<br>6||
|15-14|Reserved.|
|Reserved_RXQ<br>7EN||
|13-12|Reserved.|
|Reserved_RXQ<br>6EN||
|11-10|Reserved.|
|Reserved_RXQ<br>5EN||
|9-8|Reserved.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3671 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|Reserved_RXQ<br>4EN||
|7-6|Reserved.|
|Reserved_RXQ<br>3EN||
|5-4<br>RXQ2EN|Receive Queue 2 Enable This field is similar to the RXQ0EN field.<br>00b - Queue not enabled<br>01b - Queue enabled for AV<br>10b - Queue enabled for DCB/Generic<br>11b - Reserved|
|3-2<br>RXQ1EN|Receive Queue 1 Enable This field is similar to the RXQ0EN field.<br>00b - Queue not enabled<br>01b - Queue enabled for AV<br>10b - Queue enabled for DCB/Generic<br>11b - Reserved|
|1-0<br>RXQ0EN|Receive Queue 0 Enable This field indicates whether Rx Queue 0 is enabled for AV or DCB.<br>00b - Queue not enabled<br>01b - Queue enabled for AV<br>10b - Queue enabled for DCB/Generic<br>11b - Reserved|



### 75.7.66 (MAC_RxQ_Ctrl1) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_RxQ_Ctrl1|A4h|



##### Function 

The Receive Queue Control 1 register controls the routing of multicast, broadcast, AV, DCB, and untagged packets to the Rx queues. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3672 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3673-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserved_31_3 Reserv Reserv<br>R 0  TBRQ OMCB e... FPRQ  TPQC  TACP MCBC e... MCBCQ<br>E  CQ  QE  QEN<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv Reserv Reserv Reserv<br>R<br>e... UPQ  e... DCBCPQ  e... PTPQ  e... AVCPQ<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-30|Reserved.|
|Reserved_31_3<br>0||
|29<br>TBRQE|Type Field Based Rx Queuing Enable When this bit is set, it enables Type Field based Rx<br>Queuing where the Type field of received packet is compared with programmed TYP field in<br>MAC_TMRQ_Regs(#i) and if a match occurs the packet is routed to the corresponding TMRQ field.|
|28<br>OMCBCQ|Over-riding MC-BC queue priority select - 1: Priority of MCBCQ is reduced and the received packet is<br>first routed to PTPQ, AVCPQ, DCBCPQ depending on packet type. - 0: Received Multicast/Broadcast<br>packet is routed to MCBCQ.<br>0b - overriding MCBCQ priority disabled<br>1b - overriding MCBCQ priority enabled|
|27<br>Reserved_27|Reserved.|
|26-24<br>FPRQ|Frame Preemption Residue Queue This field holds the Rx queue number to which the residual<br>preemption frames must be forwarded. Preemption frames that are tagged and pass the SA/DA/VLAN<br>filtering are routed based on PSRQ and all other frames are treated as residual frames and is routed to<br>the queue number mentioned in this field. The Queue-0 is used as a default queue for express frames,<br>so this field cannot be programmed to a value 0.|
|23-22<br>TPQC|Tagged PTP over Ethernet Packets Queuing Control. This field controls the routing of the VLAN<br>Tagged PTPoE packets. If DWC_EQOS_AV_ENABLE is selected in the configuration, the following<br>programmable options are allowed. - 2'b00: VLAN Tagged PTPoE packets are routed as generic VLAN<br>Tagged packet (based on PSRQ for only non-AV enabled Rx Queues). - 2'b01: VLAN Tagged PTPoE<br>packets are routed to Rx Queue specified by PTPQ field (That Rx Queue can be enabled for AV<br>or non-AV traffic). - 2'b10: VLAN Tagged PTPoE packets are routed to only AV enabled Rx Queues<br>based on PSRQ. - 2'b11: Reserved If DWC_EQOS_AV_ENABLE is not selected in the configuration, the<br>following programmable options are allowed. - 1'b0: VLAN Tagged PTPoE packets are routed as generic|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3673 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function<br>VLAN Tagged packet (based on PSRQ for DCB/Generic enabled Rx Queues). - 1'b1: VLAN Tagged<br>PTPoE packets are routed to Rx Queues specified by PTPQ field.|
|---|---|
|21<br>TACPQE|Tagged AV Control Packets Queuing Enable. When set, the MAC routes the received Tagged AV<br>Control packets to the Rx queue specified by AVCPQ field. When reset, the MAC routes the received<br>Tagged AV Control packets based on the tag priority matching the PSRQ fields in MAC_RxQ_Ctrl2 and<br>MAC_RxQ_Ctrl3 registers.<br>0b - Tagged AV Control Packets Queuing is disabled<br>1b - Tagged AV Control Packets Queuing is enabled|
|20<br>MCBCQEN|Multicast and Broadcast Queue Enable This bit specifies that Multicast or Broadcast packets routing to<br>the Rx Queue is enabled and the Multicast or Broadcast packets must be routed to Rx Queue specified<br>in MCBCQ field.<br>0b - Multicast and Broadcast Queue is disabled<br>1b - Multicast and Broadcast Queue is enabled|
|19|Reserved.|
|Reserved_19||
|18-16<br>MCBCQ|Multicast and Broadcast Queue This field specifies the Rx Queue onto which Multicast or Broadcast<br>Packets are routed. Any Rx Queue enabled for Generic/DCB/AV traffic can be used to route the<br>Multicast or Broadcast Packets.<br>000b - Receive Queue 0<br>001b - Receive Queue 1<br>010b - Receive Queue 2<br>011b - Receive Queue 3<br>100b - Receive Queue 4<br>101b - Receive Queue 5<br>110b - Receive Queue 6<br>111b - Receive Queue 7|
|15<br>Reserved_15|Reserved.|
|14-12<br>UPQ|Untagged Packet Queue This field indicates the Rx Queue to which Untagged Packets are to be routed.<br>Any Rx Queue enabled for Generic/DCB/AV traffic can be used to route the Untagged Packets.<br>000b - Receive Queue 0<br>001b - Receive Queue 1<br>010b - Receive Queue 2<br>011b - Receive Queue 3<br>100b - Receive Queue 4|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3674 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||101b - Receive Queue 5<br>110b - Receive Queue 6<br>111b - Receive Queue 7|
|11|Reserved.|
|Reserved_11||
|10-8<br>DCBCPQ|DCB Control Packets Queue This field specifies the Rx queue on which the received DCB control<br>packets are routed. The DCB data packets are routed based on the PSRQ field of the Transmit Flow<br>Control Register of corresponding queue.<br>000b - Receive Queue 0<br>001b - Receive Queue 1|
||010b - Receive Queue 2<br>011b - Receive Queue 3|
||100b - Receive Queue 4<br>101b - Receive Queue 5|
||110b - Receive Queue 6|
||111b - Receive Queue 7|
|7|Reserved.|
|Reserved_7||
|6-4<br>PTPQ|PTP Packets Queue This field specifies the Rx queue on which the PTP packets sent over the Ethernet<br>payload (not over IPv4 or IPv6) are routed. When the AV8021ASMEN bit of MAC_Timestamp_Control<br>register is set, only untagged PTP over Ethernet packets are routed on an Rx Queue. If the bit is not set,<br>then based on programming of TPQC field, both tagged and untagged PTPoE packets can be routed to<br>this Rx Queue.<br>000b - Receive Queue 0<br>001b - Receive Queue 1<br>010b - Receive Queue 2<br>011b - Receive Queue 3<br>100b - Receive Queue 4<br>101b - Receive Queue 5<br>110b - Receive Queue 6|
||111b - Receive Queue 7|
|3<br>Reserved_3|Reserved.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3675 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|2-0<br>AVCPQ|AV Untagged Control Packets Queue This field specifies the Receive queue on which the received<br>AV tagged and untagged control packets are routed. The AV tagged (when TACPQE bit is set) and<br>untagged control packets are routed to Receive queue specified by this field.<br>000b - Receive Queue 0<br>001b - Receive Queue 1<br>010b - Receive Queue 2<br>011b - Receive Queue 3<br>100b - Receive Queue 4<br>101b - Receive Queue 5|
||110b - Receive Queue 6|
||111b - Receive Queue 7|



### 75.7.67 (MAC_RxQ_Ctrl2) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_RxQ_Ctrl2|A8h|



##### Function 

This register controls the routing of tagged packets based on the USP (user Priority) field of the received packets to the RxQueues 0 to 3. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||Reserve|d_PSRQ3|||||||PSR|Q2||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||PS|RQ1|||||||PSR|Q0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3676 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Fields 

|Field|Function|
|---|---|
|31-24|Reserved.|
|Reserved_PSR<br>Q3||
|23-16<br>PSRQ2|Priorities Selected in the Receive Queue 2 This field decides the priorities assigned to Rx Queue 2. All<br>packets with priorities that match the values set in this field are routed to Rx Queue 2. For example, if<br>PSRQ2[1, 0] are set, packets with USP field equal to 1 or 0 are routed to Rx Queue 2. The software<br>must ensure that the content of this field is mutually exclusive to the PSRQ fields for other queues, that<br>is, the same priority is not mapped to multiple Rx queues. this field also determines the priorities to be<br>included in the PFC packet sent to remote station when Rx Queue 2 crosses the flow control threshold<br>settings.|
|15-8<br>PSRQ1|Priorities Selected in the Receive Queue 1 This field decides the priorities assigned to Rx Queue 1. All<br>packets with priorities that match the values set in this field are routed to Rx Queue 1. For example, if<br>PSRQ1[4] is set, packets with USP field equal to 4 are routed to Rx Queue 1. The software must ensure<br>that the content of this field is mutually exclusive to the PSRQ fields for other queues, that is, the same<br>priority is not mapped to multiple Rx queues. this field also determines the priorities to be included in the<br>PFC packet sent to remote station when Rx Queue 1 crosses the flow control threshold settings.|
|7-0<br>PSRQ0|Priorities Selected in the Receive Queue 0 This field decides the priorities assigned to Rx Queue 0. All<br>packets with priorities that match the values set in this field are routed to Rx Queue 0. For example, if<br>PSRQ0[5] is set, packets with USP field equal to 5 are routed to Rx Queue 0. The software must ensure<br>that the content of this field is mutually exclusive to the PSRQ fields for other queues, that is, the same<br>priority is not mapped to multiple Rx queues. this field also determines the priorities to be included in the<br>PFC packet sent to remote station when Rx Queue 0 crosses the flow control threshold settings.|



### 75.7.68 (MAC_Interrupt_Status) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Interrupt_Status|B0h|



##### Function 

The Interrupt Status register contains the status of interrupts. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3677 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3678-01.png)


<!-- Start of picture text -->
Gigabit Ethernet Media Access Controller (GMAC)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>MDIOI Reserv<br>R Reserved_31_21  MFRIS  MFTIS  FPEIS<br>S  e...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv RXST TXST Reserv MMCT MMCR MMCI Reserv Reserv Reserv Reserv RGSM<br>R TSIS  Reserved_7_6  PHYIS<br>e... SIS  SIS  e... XIS  XIS  S  e... e... e... e... IIIS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-21|Reserved.|
|Reserved_31_2<br>1||
|20<br>MFRIS|MMC FPE Receive Interrupt Status This bit is set high when an interrupt is generated in the MMC FPE<br>Receive Interrupt Register. This bit is cleared when all bits in this interrupt register are cleared. This<br>bit is valid only when you select the Enable MAC Management Counters (MMC) option along with FPE<br>support.<br>0b - MMC FPE Receive Interrupt status not active<br>1b - MMC FPE Receive Interrupt status active|
|19<br>MFTIS|MMC FPE Transmit Interrupt Status This bit is set high when an interrupt is generated in the MMC FPE<br>Transmit Interrupt Register. This bit is cleared when all bits in this interrupt register are cleared. This<br>bit is valid only when you select the Enable MAC Management Counters (MMC) option along with FPE<br>support.<br>0b - MMC FPE Transmit Interrupt status not active<br>1b - MMC FPE Transmit Interrupt status active|
|18<br>MDIOIS|MDIO Interrupt Status This bit indicates an interrupt event after the completion of MDIO operation.<br>To reset this bit, the application has to read this bit/Write 1 to this bit when RCWE bit of<br>MAC_CSR_SW_Ctrl register is set. Access restriction applies. Clears on read (or write of 1 when RCWE<br>bit in MAC_CSR_SW_Ctrl register is set). Self-set to 1 on internal event.<br>0b - MDIO Interrupt status not active<br>1b - MDIO Interrupt status active|
|17<br>FPEIS|Frame Preemption Interrupt Status This bit indicates an interrupt event during the operation of Frame<br>Preemption (Bits[19:16] of MAC_FPE_CTRL_STS register is set). To reset this bit, the application must<br>clear the event in MAC_FPE_CTRL_STS that has caused the Interrupt.<br>0b - Frame Preemption Interrupt status not active<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3678 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function<br>1b - Frame Preemption Interrupt status active|
|---|---|
|16<br>Reserved_16|Reserved.|
|15<br>Reserved_GPII<br>S|Reserved.|
|14<br>RXSTSIS|Receive Status Interrupt This bit indicates the status of received packets. This bit is set when the RWT<br>bit is set in the MAC_Rx_Tx_Status register. This bit is cleared when the corresponding interrupt source<br>bit is read (or corresponding interrupt source bit is written to 1 when RCWE bit of MAC_CSR_SW_Ctrl<br>register is set) in the MAC_Rx_Tx_Status register.<br>0b - Receive Interrupt status not active<br>1b - Receive Interrupt status active|
|13<br>TXSTSIS|Transmit Status Interrupt This bit indicates the status of transmitted packets. This bit is set when<br>any of the following bits is set in the MAC_Rx_Tx_Status register: - Excessive Collision (EXCOL) -<br>Late Collision (LCOL) - Excessive Deferral (EXDEF) - Loss of Carrier (LCARR) - No Carrier (NCARR)<br>- Jabber Timeout (TJT) This bit is cleared when the corresponding interrupt source bit is read (or<br>corresponding interrupt source bit is written to 1 when RCWE bit of MAC_CSR_SW_Ctrl register is set) in<br>the MAC_Rx_Tx_Status register.<br>0b - Transmit Interrupt status not active<br>1b - Transmit Interrupt status active|
|12<br>TSIS|Timestamp Interrupt Status If the Timestamp feature is enabled, this bit is set when any of the following<br>conditions is true: - The system time value is equal to or exceeds the value specified in the Target Time<br>High and Low registers. - There is an overflow in the Seconds register. - The Target Time Error occurred,<br>that is, programmed target time already elapsed. In configurations other than EQOS_CORE, when drop<br>transmit status is enabled in MTL, this bit is set when the captured transmit timestamp is updated in<br>the MAC_Tx_Timestamp_Status_Nanoseconds and Mac_TxTimestamp_Status_Seconds registers. This<br>bit is cleared when the corresponding interrupt source bit is read (or corresponding interrupt source bit<br>is written to 1 when RCWE bit of MAC_CSR_SW_Ctrl register is set) in the MAC_Timestamp_Status<br>register.<br>0b - Timestamp Interrupt status not active<br>1b - Timestamp Interrupt status active|
|11|Reserved.|
|Reserved_MMC<br>RXIPIS||
|10<br>MMCTXIS|MMC Transmit Interrupt Status This bit is set high when an interrupt is generated in the MMC Transmit<br>Interrupt Register. This bit is cleared when all bits in this interrupt register are cleared. This bit is valid<br>only when you select the Enable MAC Management Counters (MMC) option.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3679 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function<br>0b - MMC Transmit Interrupt status not active<br>1b - MMC Transmit Interrupt status active|
|---|---|
|9<br>MMCRXIS|MMC Receive Interrupt Status This bit is set high when an interrupt is generated in the MMC Receive<br>Interrupt Register. This bit is cleared when all bits in this interrupt register are cleared. This bit is valid<br>only when you select the Enable MAC Management Counters (MMC) option.<br>0b - MMC Receive Interrupt status not active<br>1b - MMC Receive Interrupt status active|
|8<br>MMCIS|MMC Interrupt Status This bit is set high when Bit 11, Bit 10, or Bit 9 is set high. This bit is cleared only<br>when all these bits are low. This bit is valid only when you select the Enable MAC Management Counters<br>(MMC) option.<br>0b - MMC Interrupt status not active<br>1b - MMC Interrupt status active|
|7-6<br>Reserved_7_6|Reserved.|
|5<br>Reserved_LPIIS|Reserved.|
|4<br>Reserved_PMTI<br>S|Reserved.|
|3<br>PHYIS|PHY Interrupt This bit is set when rising edge is detected on the phy_intr_i input. This bit is cleared when<br>this register is read (or this bit is written to 1 when RCWE bit of MAC_CSR_SW_Ctrl register is set).<br>0b - PHY Interrupt not detected<br>1b - PHY Interrupt detected|
|2<br>Reserved_PCS<br>ANCIS|Reserved.|
|1<br>Reserved_PCS<br>LCHGIS|Reserved.|
|0<br>RGSMIIIS|RGMII or SMII Interrupt Status This bit is set because of any change in value of the Link Status of<br>RGMII or SMII interface (LNKSTS bit in MAC_PHYIF_Control_Status register). This bit is cleared when<br>the MAC_PHYIF_Control_Status register is read (or LNKSTS bit of MAC_PHYIF_Control_Status register<br>is written to 1 when RCWE bit of MAC_CSR_SW_Ctrl register is set). This bit is valid only when you<br>select the optional RGMII or SMII PHY interface.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3680 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function||
|---|---|---|
||0b - RGMII or SMII|Interrupt Status is not active|
||1b - RGMII or SMII|Interrupt Status is active|



### 75.7.69 (MAC_Interrupt_Enable) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Interrupt_Enable|B4h|



##### Function 

The Interrupt Enable register contains the masks for generating the interrupts. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3681-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R Reserved_31_19  MDIOI FPEIE  e...<br>E<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv Reserv Reserv Reserv Reserv<br>R e... RXST TXSTS TSIE  Reserved_11_6  e... e... PHYIE  e... e... RGSM<br>SIE  IE  IIIE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-19|Reserved.|
|Reserved_31_1<br>9||
|18<br>MDIOIE|MDIO Interrupt Enable When this bit is set, it enables the assertion of the interrupt when MDIOIS field is<br>set in the MAC_Interrupt_Status register.<br>0b - MDIO Interrupt is disabled|
||1b - MDIO Interrupt is enabled|
|17|Frame Preemption Interrupt Enable When this bit is set, it enables the assertion of the interrupt when<br>FPEIS field is set in the MAC_Interrupt_Status register.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3681 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|FPEIE|0b - Frame Preemption Interrupt is disabled<br>1b - Frame Preemption Interrupt is enabled|
|16<br>Reserved_16|Reserved.|
|15|Reserved.|
|Reserved_15||
|14<br>RXSTSIE|Receive Status Interrupt Enable When this bit is set, it enables the assertion of the interrupt signal<br>because of the setting of RXSTSIS bit in the MAC_Interrupt_Status register.<br>0b - Receive Status Interrupt is disabled<br>1b - Receive Status Interrupt is enabled|
|13<br>TXSTSIE|Transmit Status Interrupt Enable When this bit is set, it enables the assertion of the interrupt signal<br>because of the setting of TXSTSIS bit in the MAC_Interrupt_Status register.<br>0b - Timestamp Status Interrupt is disabled<br>1b - Timestamp Status Interrupt is enabled|
|12<br>TSIE|Timestamp Interrupt Enable When this bit is set, it enables the assertion of the interrupt signal because<br>of the setting of TSIS bit in MAC_Interrupt_Status register.<br>0b - Timestamp Interrupt is disabled<br>1b - Timestamp Interrupt is enabled|
|11-6<br>Reserved_11_6|Reserved.|
|5<br>Reserved_LPIIE|Reserved.|
|4|Reserved.|
|Reserved_PMTI<br>E<br>3<br>PHYIE|PHY Interrupt Enable When this bit is set, it enables the assertion of the interrupt signal because of the<br>setting of PHYIS bit in MAC_Interrupt_Status register.<br>0b - PHY Interrupt is disabled<br>1b - PHY Interrupt is enabled|
|2|Reserved.|
|Reserved_PCS<br>ANCIE||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3682 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|1|Reserved.|
|Reserved_PCS<br>LCHGIE||
|0<br>RGSMIIIE|RGMII or SMII Interrupt Enable When this bit is set, it enables the assertion of the interrupt signal<br>because of the setting of RGSMIIIS bit in MAC_Interrupt_Status register.<br>0b - RGMII or SMII Interrupt is disabled|
||1b - RGMII or SMII Interrupt is enabled|



### 75.7.70 (MAC_Rx_Tx_Status) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Rx_Tx_Status|B8h|



##### Function 

The Receive Transmit Status register contains the Receive and Transmit Error status. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3683-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_9<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>EXCO EXDE LCAR NCAR<br>R Reserved_31_9  RWT  Reserved_7_6  LCOL  TJT<br>L  F  R  R<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-9|Reserved.|
|Reserved_31_9||
|8|Receive Watchdog Timeout This bit is set when a packet with length greater than 2,048 bytes is received<br>(10, 240 bytes when Jumbo Packet mode is enabled) and the WD bit is reset in the MAC_Configuration|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3683 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|RWT|register. This bit is set when a packet with length greater than 16,383 bytes is received and the WD bit<br>is set in the MAC_Configuration register. Access restriction applies. Clears on read (or write of 1 when<br>RCWE bit in MAC_CSR_SW_Ctrl register is set). Self-set to 1 on internal event.<br>0b - No receive watchdog timeout<br>1b - Receive watchdog timed out|
|7-6<br>Reserved_7_6|Reserved.|
|5<br>EXCOL|Excessive Collisions When the DTXSTS bit is set in the MTL_Operation_Mode register, this bit indicates<br>that the transmission aborted after 16 successive collisions while attempting to transmit the current<br>packet. If the DR bit is set in the MAC_Configuration register, this bit is set after the first collision and the<br>packet transmission is aborted. Access restriction applies. Clears on read (or write of 1 when RCWE bit<br>in MAC_CSR_SW_Ctrl register is set). Self-set to 1 on internal event.<br>0b - No collision<br>1b - Excessive collision is sensed|
|4<br>LCOL|Late Collision When the DTXSTS bit is set in the MTL_Operation_Mode register, this bit indicates<br>that the packet transmission aborted because a collision occurred after the collision window (64 bytes<br>including Preamble in MII mode; 512 bytes including Preamble and Carrier Extension in GMII mode).<br>This bit is not valid if the Underflow error occurs. Access restriction applies. Clears on read (or write of 1<br>when RCWE bit in MAC_CSR_SW_Ctrl register is set). Self-set to 1 on internal event.<br>0b - No collision<br>1b - Late collision is sensed|
|3<br>EXDEF|Excessive Deferral When the DTXSTS bit is set in the MTL_Operation_Mode register and the DC bit<br>is set in the MAC_Configuration register, this bit indicates that the transmission ended because of<br>excessive deferral of over 24,288 bit times (155,680 in 1000/2500 Mbps mode or when Jumbo packet is<br>enabled). Access restriction applies. Clears on read (or write of 1 when RCWE bit in MAC_CSR_SW_Ctrl<br>register is set). Self-set to 1 on internal event.<br>0b - No Excessive deferral<br>1b - Excessive deferral|
|2<br>LCARR|Loss of Carrier When the DTXSTS bit is set in the MTL_Operation_Mode register, this bit indicates that<br>the loss of carrier occurred during packet transmission, that is, the phy_crs_i signal was inactive for<br>one or more transmission clock periods during packet transmission. This bit is valid only for packets<br>transmitted without collision. Access restriction applies. Clears on read (or write of 1 when RCWE bit in<br>MAC_CSR_SW_Ctrl register is set). Self-set to 1 on internal event.<br>0b - Carrier is present<br>1b - Loss of carrier|
|1<br>NCARR|No Carrier When the DTXSTS bit is set in the MTL_Operation_Mode register, this bit indicates that<br>the carrier signal from the PHY is not present at the end of preamble transmission. Access restriction<br>applies. Clears on read (or write of 1 when RCWE bit in MAC_CSR_SW_Ctrl register is set). Self-set to 1<br>on internal event.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3684 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Carrier is present<br>1b - No carrier|
|0<br>TJT|Transmit Jabber Timeout This bit indicates that the Transmit Jabber Timer expired which happens when<br>the packet size exceeds 2,048 bytes (10,240 bytes when the Jumbo packet is enabled) and JD bit is<br>reset in the MAC_Configuration register. This bit is set when the packet size exceeds 16,383 bytes and<br>the JD bit is set in the MAC_Configuration register. Access restriction applies. Clears on read (or write of<br>1 when RCWE bit in MAC_CSR_SW_Ctrl register is set). Self-set to 1 on internal event.|
||0b - No Transmit Jabber Timeout|
||1b - Transmit Jabber Timeout occurred|



### 75.7.71 (MAC_PHYIF_Control_Status) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_PHYIF_Control_St|F8h|
|atus||



##### Function 

The PHY Interface Control and Status register indicates the status signals received by the SGMII, RGMII, or SMII interface (selected at reset) from the PHY. This register is optional. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3685-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv Reserv LNKST LNKM<br>R Reserved_31_22  LNKSPEED<br>e... e... S  OD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv Reserv Reserv<br>R Reserved_15_5<br>e... e... e... LUD  TC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-22|Reserved.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3685 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field<br>Reserved_31_2<br>2|Function|
|---|---|
|21|Reserved.|
|Reserved_FAL<br>SCARDET||
|20|Reserved.|
|Reserved_JABT<br>O||
|19<br>LNKSTS|Link Status This bit indicates whether the link is up (1'b1) or down (1'b0).<br>0b - Link down<br>1b - Link up|
|18-17<br>LNKSPEED|Link Speed This bit indicates the current speed of the link.<br>00b - 2.5 MHz<br>01b - 25 MHz<br>10b - 125 MHz<br>11b - Reserved|
|16<br>LNKMOD|Link Mode This bit indicates the current mode of operation of the link.<br>0b - Half-duplex mode<br>1b - Full-duplex mode|
|15-5|Reserved.|
|Reserved_15_5||
|4|Reserved.|
|Reserved_SMI<br>DRXS||
|3|Reserved.|
|Reserved_3||
|2|Reserved.|
|Reserved_SFT<br>ERR||
|1<br>LUD|Link Up or Down This bit indicates whether the link is up or down during transmission of configuration in<br>the RGMII, SGMII, or SMII interface.<br>0b - Link down<br>1b - Link up|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3686 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|0<br>TC|Transmit Configuration in RGMII, SGMII, or SMII When set, this bit enables the transmission of duplex<br>mode, link speed, and link up or down information to the PHY in the RGMII, SMII, or SGMII port. When<br>this bit is reset, no such information is driven to the PHY. The details of this feature are provided in<br>the following sections: - "Reduced Gigabit Media Independent Interface" - "Serial Media Independent<br>Interface" - "Serial Gigabit Media Independent Interface"|
||0b - Disable Transmit Configuration in RGMII, SGMII, or SMII|
||1b - Enable Transmit Configuration in RGMII, SGMII, or SMII|



### 75.7.72 (MAC_Version) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Version|110h|



##### Function 

Identifies the version of the module. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||Reserve|d_31_16||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||USER|VER|||||||IPV|ER||||
|W|||||||||||||||||
|Reset|0|0|0|1|0|0|0|0|0|1|0|1|0|0|1|0|



##### Fields 

|Field|Function|
|---|---|
|31-16|Reserved.|
|Reserved_31_1<br>6||
|15-8|User-defined Version (configured with coreConsultant)|
|USERVER||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3687 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|7-0|IP version|
|IPVER||



### 75.7.73 (MAC_Debug) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Debug|114h|



##### Function 

The Debug register provides the debug status of various MAC blocks. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3688-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>TPEST<br>R Reserved_31_19  TFCSTS<br>S<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>RPES<br>R Reserved_15_3  RFCFCSTS<br>TS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-19|Reserved.|
|Reserved_31_1<br>9||
|18-17<br>TFCSTS|MAC Transmit Packet Controller Status This field indicates the state of the MAC Transmit Packet<br>Controller module.<br>00b - Idle state|
||01b - Waiting for one of the following: Status of the previous packet OR IPG or back off period to<br>be over|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3688 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||10b - Generating and transmitting a Pause control packet (in full-duplex mode)<br>11b - Transferring input packet for transmission|
|16<br>TPESTS|MAC GMII or MII Transmit Protocol Engine Status When this bit is set, it indicates that the MAC GMII or<br>MII transmit protocol engine is actively transmitting data, and it is not in the Idle state.<br>0b - MAC GMII or MII Transmit Protocol Engine Status not detected<br>1b - MAC GMII or MII Transmit Protocol Engine Status detected|
|15-3|Reserved.|
|Reserved_15_3||
|2-1<br>RFCFCSTS|MAC Receive Packet Controller FIFO Status When this bit is set, this field indicates the active state of<br>the small FIFO Read and Write controllers of the MAC Receive Packet Controller module.|
|0<br>RPESTS|MAC GMII or MII Receive Protocol Engine Status When this bit is set, it indicates that the MAC GMII or<br>MII receive protocol engine is actively receiving data, and it is not in the Idle state.<br>0b - MAC GMII or MII Receive Protocol Engine Status not detected<br>1b - MAC GMII or MII Receive Protocol Engine Status detected|



### 75.7.74 (MAC_HW_Feature0) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_HW_Feature0|11Ch|



##### Function 

This register indicates the presence of first set of the optional features or functions of the DWC_ether_qos. The software driver can use this register to dynamically enable or disable the programs related to the optional blocks. Note: All bits are set or reset according to the features selected while configuring the IP in coreConsultant. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3689 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3690-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv SAVLA MACA MACA Reserv RXCO<br>R ACTPHYSEL  TSSTSSEL  ADDMACADRSEL<br>e... NI... DR6... DR3... e... ESEL<br>W<br>Reset 0 0 0 0 1 1 1 0 0 0 0 0 1 0 0 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv TXCO EEES Reserved_11_1 ARPO MMCS MGKS RWKS SMAS VLHA PCSS HDSE GMIIS MIISE<br>R TSSEL<br>e... ESEL  EL  0  FFS... EL  EL  EL  EL  SH  EL  L  EL  L<br>W<br>Reset 0 1 0 1 0 0 1 1 0 0 1 1 0 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Reserved.|
|Reserved_31||
|30-28<br>ACTPHYSEL|Active PHY Selected When you have multiple PHY interfaces in your configuration, this field indicates<br>the sampled value of phy_intf_sel_i during reset de-assertion.<br>000b - GMII or MII<br>001b - RGMII|
||010b - SGMII<br>011b - TBI|
||100b - RMII<br>101b - RTBI|
||110b - SMII<br>111b - RevMII|
|27<br>SAVLANINS|Source Address or VLAN Insertion Enable This bit is set to 1 when the Enable SA and VLAN Insertion on<br>Tx option is selected<br>0b - Source Address or VLAN Insertion Enable option is not selected<br>1b - Source Address or VLAN Insertion Enable option is selected|
|26-25<br>TSSTSSEL|Timestamp System Time Source This bit indicates the source of the Timestamp system time: This bit is<br>set to 1 when the Enable IEEE 1588 Timestamp Support option is selected<br>00b - Internal<br>01b - External<br>10b - Both|
||11b - Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3690 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|24<br>MACADR64SE<br>L|MAC Addresses 64-127 Selected This bit is set to 1 when the Enable Additional 64 MAC Address<br>Registers (64-127) option is selected<br>0b - MAC Addresses 64-127 Select option is not selected<br>1b - MAC Addresses 64-127 Select option is selected|
|23<br>MACADR32SE<br>L|MAC Addresses 32-63 Selected This bit is set to 1 when the Enable Additional 32 MAC Address<br>Registers (32-63) option is selected<br>0b - MAC Addresses 32-63 Select option is not selected<br>1b - MAC Addresses 32-63 Select option is selected|
|22-18<br>ADDMACADRS<br>EL|MAC Addresses 1-31 Selected This bit is set to 1 when the non-zero value is selected for Enable<br>Additional 1-31 MAC Address Registers option|
|17<br>Reserved_17|Reserved.|
|16<br>RXCOESEL|Receive Checksum Offload Enabled This bit is set to 1 when the Enable Receive TCP/IP Checksum<br>Check option is selected<br>0b - Receive Checksum Offload Enable option is not selected<br>1b - Receive Checksum Offload Enable option is selected|
|15<br>Reserved_15|Reserved.|
|14<br>TXCOESEL|Transmit Checksum Offload Enabled This bit is set to 1 when the Enable Transmit TCP/IP Checksum<br>Insertion option is selected<br>0b - Transmit Checksum Offload Enable option is not selected<br>1b - Transmit Checksum Offload Enable option is selected|
|13<br>EEESEL|Energy Efficient Ethernet Enabled This bit is set to 1 when the Enable Energy Efficient Ethernet (EEE)<br>option is selected<br>0b - Energy Efficient Ethernet Enable option is not selected<br>1b - Energy Efficient Ethernet Enable option is selected|
|12<br>TSSEL|IEEE 1588-2008 Timestamp Enabled This bit is set to 1 when the Enable IEEE 1588 Timestamp Support<br>option is selected<br>0b - IEEE 1588-2008 Timestamp Enable option is not selected<br>1b - IEEE 1588-2008 Timestamp Enable option is selected|
|11-10|Reserved.|
|Reserved_11_1<br>0||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3691 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|9<br>ARPOFFSEL|ARP Offload Enabled This bit is set to 1 when the Enable IPv4 ARP Offload option is selected<br>0b - ARP Offload Enable option is not selected<br>1b - ARP Offload Enable option is selected|
|8<br>MMCSEL|RMON Module Enable This bit is set to 1 when the Enable MAC Management Counters (MMC) option is<br>selected<br>0b - RMON Module Enable option is not selected<br>1b - RMON Module Enable option is selected|
|7<br>MGKSEL|PMT Magic Packet Enable This bit is set to 1 when the Enable Magic Packet Detection option is selected<br>0b - PMT Magic Packet Enable option is not selected<br>1b - PMT Magic Packet Enable option is selected|
|6<br>RWKSEL|PMT Remote Wake-up Packet Enable This bit is set to 1 when the Enable Remote Wake-Up Packet<br>Detection option is selected<br>0b - PMT Remote Wake-up Packet Enable option is not selected<br>1b - PMT Remote Wake-up Packet Enable option is selected|
|5<br>SMASEL|SMA (MDIO) Interface This bit is set to 1 when the Enable Station Management (MDIO Interface) option<br>is selected<br>0b - SMA (MDIO) Interface not selected<br>1b - SMA (MDIO) Interface selected|
|4<br>VLHASH|VLAN Hash Filter Selected This bit is set to 1 when the Enable VLAN Hash Table Based Filtering option<br>is selected<br>0b - VLAN Hash Filter not selected<br>1b - VLAN Hash Filter selected|
|3<br>PCSSEL|PCS Registers (TBI, SGMII, or RTBI PHY interface) This bit is set to 1 when the TBI, SGMII, or RTBI<br>PHY interface option is selected<br>0b - No PCS Registers (TBI, SGMII, or RTBI PHY interface)<br>1b - PCS Registers (TBI, SGMII, or RTBI PHY interface)|
|2<br>HDSEL|Half-duplex Support This bit is set to 1 when the half-duplex mode is selected<br>0b - No Half-duplex support<br>1b - Half-duplex support|
|1<br>GMIISEL|1000 Mbps Support This bit is set to 1 when 1000 Mbps is selected as the Mode of Operation<br>0b - No 1000 Mbps support<br>1b - 1000 Mbps support|
|0|10 or 100 Mbps Support This bit is set to 1 when 10/100 Mbps is selected as the Mode of Operation|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3692 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|MIISEL|0b - No 10 or 100 Mbps support|
||1b - 10 or 100 Mbps support|



### 75.7.75 (MAC_HW_Feature1) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_HW_Feature1|120h|



##### Function 

This register indicates the presence of second set of the optional features or functions of the DWC_ether_qos. The software driver can use this register to dynamically enable or disable the programs related to the optional blocks. Note: All bits are set or reset according to the features selected while configuring the IP in coreConsultant. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3693-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv Reserv POUO Reserv RAVS DBGM TSOE SPHE DCBE<br>R L3L4FNUM  HASHTBLSZ  AVSEL<br>e... e... ST  e... EL  EMA  N  N  N<br>W<br>Reset 0 1 0 0 0 0 1 1 0 0 0 1 1 0 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>ADVT<br>PTOE OSTE SPRA<br>R ADDR64  HWO.. TXFIFOSIZE  RXFIFOSIZE<br>N  N  M<br>.<br>W<br>Reset 0 0 1 0 1 0 0 1 1 1 1 0 0 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Reserved.|
|Reserved_31||
|30-27|Total number of L3 or L4 Filters This field indicates the total number of L3 or L4 filters:|
|L3L4FNUM|0000b - No L3 or L4 Filter|
||0001b - 1 L3 or L4 Filter|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3693 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function<br>0010b - 2 L3 or L4 Filters<br>0011b - 3 L3 or L4 Filters<br>0100b - 4 L3 or L4 Filters<br>0101b - 5 L3 or L4 Filters<br>0110b - 6 L3 or L4 Filters<br>0111b - 7 L3 or L4 Filters<br>1000b - 8 L3 or L4 Filters|
|---|---|
|26<br>Reserved_26|Reserved.|
|25-24<br>HASHTBLSZ|Hash Table Size This field indicates the size of the hash table:<br>00b - No hash table<br>01b - 64<br>10b - 128<br>11b - 256|
|23<br>POUOST|One Step for PTP over UDP/IP Feature Enable This bit is set to 1 when the Enable One step timestamp<br>for PTP over UDP/IP feature is selected.<br>0b - One Step for PTP over UDP/IP Feature is not selected<br>1b - One Step for PTP over UDP/IP Feature is selected|
|22<br>Reserved_22|Reserved.|
|21<br>RAVSEL|Rx Side Only AV Feature Enable This bit is set to 1 when the Enable Audio Video Bridging option on Rx<br>Side Only is selected.<br>0b - Rx Side Only AV Feature is not selected<br>1b - Rx Side Only AV Feature is selected|
|20<br>AVSEL|AV Feature Enable This bit is set to 1 when the Enable Audio Video Bridging option is selected.<br>0b - AV Feature is not selected<br>1b - AV Feature is selected|
|19<br>DBGMEMA|DMA Debug Registers Enable This bit is set to 1 when the Debug Mode Enable option is selected<br>0b - DMA Debug Registers option is not selected<br>1b - DMA Debug Registers option is selected|
|18<br>TSOEN|TCP Segmentation Offload Enable This bit is set to 1 when the Enable TCP Segmentation Offloading for<br>TCP/IP Packets option is selected|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3694 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function<br>0b - TCP Segmentation Offload Feature is not selected<br>1b - TCP Segmentation Offload Feature is selected|
|---|---|
|17<br>SPHEN|Split Header Feature Enable This bit is set to 1 when the Enable Split Header Structure option is<br>selected<br>0b - Split Header Feature is not selected<br>1b - Split Header Feature is selected|
|16<br>DCBEN|DCB Feature Enable This bit is set to 1 when the Enable Data Center Bridging option is selected<br>0b - DCB Feature is not selected<br>1b - DCB Feature is selected|
|15-14<br>ADDR64|Address Width. This field indicates the configured address width:<br>00b - 32<br>01b - 40<br>10b - 48<br>11b - Reserved|
|13<br>ADVTHWORD|IEEE 1588 High Word Register Enable This bit is set to 1 when the Add IEEE 1588 Higher Word<br>Register option is selected<br>0b - IEEE 1588 High Word Register option is not selected<br>1b - IEEE 1588 High Word Register option is selected|
|12<br>PTOEN|PTP Offload Enable This bit is set to 1 when the Enable PTP Timestamp Offload Feature is selected.<br>0b - PTP Offload feature is not selected<br>1b - PTP Offload feature is selected|
|11<br>OSTEN|One-Step Timestamping Enable This bit is set to 1 when the Enable One-Step Timestamp Feature is<br>selected.<br>0b - One-Step Timestamping feature is not selected<br>1b - One-Step Timestamping feature is selected|
|10-6<br>TXFIFOSIZE|MTL Transmit FIFO Size This field contains the configured value of MTL Tx FIFO in bytes expressed as<br>Log to base 2 minus 7, that is, Log2(TXFIFO_SIZE) -7:<br>0_0000b - 128 bytes<br>0_0001b - 256 bytes<br>0_0010b - 512 bytes<br>0_0011b - 1024 bytes<br>0_0100b - 2048 bytes<br>0_0101b - 4096 bytes|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3695 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0_0110b - 8192 bytes<br>0_0111b - 16384 bytes<br>0_1000b - 32 KB<br>0_1001b - 64 KB<br>0_1010b - 128 KB<br>0_1011b - Reserved|
|5<br>SPRAM|Single Port RAM Enable This bit is set to 1 when the Use single port RAM Feature is selected.<br>0b - Single Port RAM feature is not selected<br>1b - Single Port RAM feature is selected|
|4-0<br>RXFIFOSIZE|MTL Receive FIFO Size This field contains the configured value of MTL Rx FIFO in bytes expressed as<br>Log to base 2 minus 7, that is, Log2(RXFIFO_SIZE) -7:<br>0_0000b - 128 bytes|
||0_0001b - 256 bytes|
||0_0010b - 512 bytes|
||0_0011b - 1024 bytes|
||0_0100b - 2048 bytes<br>0_0101b - 4096 bytes|
||0_0110b - 8192 bytes<br>0_0111b - 16384 bytes<br>0_1000b - 32 KB|
||0_1001b - 64 KB|
||0_1010b - 128 KB|
||0_1011b - 256 KB|
||0_1100b - Reserved|



### 75.7.76 (MAC_HW_Feature2) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_HW_Feature2|124h|



##### Function 

This register indicates the presence of third set of the optional features or functions of the DWC_ether_qos. The software driver can use this register to dynamically enable or disable the programs related to the optional blocks. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3696 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3697-02.png)


<!-- Start of picture text -->
Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv Reserv<br>R AUXSNAPNUM  PPSOUTNUM  TDCSZ  TXCHCNT  RDCSZ<br>e... e...<br>W<br>Reset 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserved_11_1<br>R RXCHCNT  TXQCNT  Reserved_5_4  RXQCNT<br>0<br>W<br>Reset 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0<br>Fields<br>Field Function<br>31 Reserved.<br>Reserved_31<br>30-28 Number of Auxiliary Snapshot Inputs This field indicates the number of auxiliary snapshot inputs:<br>AUXSNAPNUM 000b - No auxiliary input<br>001b - 1 auxiliary input<br>010b - 2 auxiliary input<br>011b - 3 auxiliary input<br>100b - 4 auxiliary input<br>101b - Reserved<br>27 Reserved.<br>Reserved_27<br>26-24 Number of PPS Outputs This field indicates the number of PPS outputs:<br>PPSOUTNUM 000b - No PPS output<br>001b - 1 PPS output<br>010b - 2 PPS output<br>011b - 3 PPS output<br>100b - 4 PPS output<br>101b - Reserved<br>23-22 Tx DMA Descriptor Cache Size in terms of 16 bytes descriptors: 00 - Cache Not configured 01 - 4 16<br>bytes descriptor 10 - 8 16 bytes descriptor 11 - 16 16 bytes descriptor<br>TDCSZ<br>21-18 Number of DMA Transmit Channels This field indicates the number of DMA Transmit channels:<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3697 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|TXCHCNT|0000b - 1 MTL Tx Channel<br>0001b - 4<br>0010b - 8<br>0011b - 16<br>0100b - 5 MTL Tx Channels<br>0101b - 6 MTL Tx Channels<br>0110b - 7 MTL Tx Channels<br>0111b - 8 MTL Tx Channels|
|17-16<br>RDCSZ|Rx DMA Descriptor Cache Size in terms of 16 bytes descriptors: 00 - Cache Not configured 01 - 4 16<br>bytes descriptor 10 - 8 16 bytes descriptor 11 - 16 16 bytes descriptor|
|15-12<br>RXCHCNT|Number of DMA Receive Channels This field indicates the number of DMA Receive channels:<br>0000b - 1 MTL Rx Channel<br>0001b - 4<br>0010b - 8<br>0011b - 16<br>0100b - 5 MTL Rx Channels<br>0101b - 6 MTL Rx Channels<br>0110b - 7 MTL Rx Channels<br>0111b - 8 MTL Rx Channels|
|11-10<br>Reserved_11_1<br>0|Reserved.|
|9-6<br>TXQCNT|Number of MTL Transmit Queues This field indicates the number of MTL Transmit queues:<br>0000b - 1 MTL Tx Queue<br>0001b - 2 MTL Tx Queues<br>0010b - 3 MTL Tx Queues<br>0011b - 4 MTL Tx Queues<br>0100b - 5 MTL Tx Queues<br>0101b - 6 MTL Tx Queues<br>0110b - 7 MTL Tx Queues<br>0111b - 8 MTL Tx Queues|
|5-4|Reserved.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3698 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|Reserved_5_4||
|3-0|Number of MTL Receive Queues This field indicates the number of MTL Receive queues:|
|RXQCNT|0000b - 1 MTL Rx Queue|
||0001b - 2 MTL Rx Queues|
||0010b - 3 MTL Rx Queues|
||0011b - 4 MTL Rx Queues|
||0100b - 5 MTL Rx Queues|
||0101b - 6 MTL Rx Queues|
||0110b - 7 MTL Rx Queues|
||0111b - 8 MTL Rx Queues|



### 75.7.77 (MAC_HW_Feature3) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_HW_Feature3|128h|



##### Function 

This register indicates the presence of fourth set the optional features or functions of the DWC_ether_qos. The software driver can use this register to dynamically enable or disable the programs related to the optional blocks. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part1/S32K3XXRM_数据表.pdf-3699-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserved_31_3 TBSS FPES ESTS<br>R ASP  Reserved_25_22  ESTWID  ESTDEP<br>0  EL  EL  EL<br>W<br>Reset 0 0 1 0 1 1 0 0 0 0 1 1 0 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv FRPS PDUP DVLA CBTIS Reserv<br>R FRPES  FRPBS  Reserved_7_6  NRVF<br>e... EL  SEL  N  EL  e...<br>W<br>Reset 0 0 0 1 0 1 1 0 0 0 1 1 0 1 0 1<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3699 / 4640 

