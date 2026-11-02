NXP Semiconductors 

# Chapter 74 Ethernet Media Access Controller (EMAC) 

## 74.1 Chip-specific EMAC information 

### 74.1.1 EMAC instance and configuration 

This chip supports up to 1 instance of EMAC IP. 

Table 486. EMAC instance 

|Instance|S32K322/S32K342/S32K314/S32K324/S32K344|S32K311/S32K312/S32K358|
|---|---|---|
|EMAC|Yes|No|



~~<mark>NOTE</mark>~~ 

DWC_EQOS refer to the Synopsys Ethernet MAC IP. 

~~<mark>NOTE</mark>~~ 

The description for some EMAC registers include references to configurations of the Synopsis Ethernet MAC IP. Refer to MAC_HW_Feature registers for the specific features available in this chip. 

~~<mark>NOTE</mark>~~ 

EMAC operates only in Clock options A and B, since the module clock becomes lower than the protocol clock (RMII/MII clocks) in other modes. 

Following key features are supported: 

- This chip supports only MII/RMII interfaces 

- 4 bit MII interface operating at 2.5/25/50Mhz, MII can run at 10/100/200 Mbps. 

- 2 bit RMII interface operating at 50Mhz, RMII can run at 10/100Mbps 

- 4 bit MII-Lite interface operating at 2.5/25Mhz 

- 4 PPS are supported using DMA trigger 

- 200Mbps data rate is supported on Ethernet MII interface 

- MTL Receive FIFO size 8192bytes 

- MTL Transmit FIFO size 8192bytes 

~~<mark>NOTE</mark>~~ 

The DMA referred within EMAC chapter refers to the internal EMAC DMA engine and not the device AXBS master DMA. 

~~<mark>NOTE</mark>~~ 

Register access beyond 8k address space is not supported and will generate a transfer error. 

~~<mark>NOTE</mark>~~ 

Always use store and forward mode if possible. In cut through mode, if multiple masters are active then there is chance (even in round robin arbitration mode) that EMAC DMA may starve for data resulting in insufficient data in TX FIFO leading to Tx underflow. To avoid this, increase MTL_TxQ0_Operation_Mode[TTC] value as needed. 

The table below provides the information on the specific configuration utilized for the S32K3x4 and K342 devices. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2940 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table 487. Specific configuration information 

|Application Interface|||
|---|---|---|
||Application interface configuration|EQOS-AHB|
||Data width|32|
||Endian mode|Little Endian|
||Address width|32|
||CSR interfcae|APB3 interface|
|General feature|||
||Mode of operation|10/100|
||Enable double VLAN processing|Yes|
||Enable Que/channel based VLAN tag<br>inertion on Tx|Yes|
||Enable SA and VLAN insertion on Tx|Enabled by default|
|Buffer managemnet|||
||MTL Receive FIFO size in bytes|8192|
||MTL Receive FIFO size in bytes|8192|
||Enable debug memory access|Yes|
||Use single port memory|Yes|
|PHY interface|||
||Enable RGMII, RMII only|Enable RMII, GMII/MII default|
||Enabled signel phy interface|No|
||Enable MDIO interface|Yes|
|Filtering|||
||Enable Additional 1-31 MAC<br>address registers|2|
||Enable Address Filter Hash Table|Yes|
||Hash Table Size|64|
||Enable VLAN Hash table based filtering|Yes|
||Extended Rx VLAN Filter Enable|Yes|
||Number of VLAN tag Filters|4|
||Enable Layer3 and Layer4 Packet Filter|Yes|
||Number of layer3 and Layer 4<br>packet filters|4|
||Enable Flexible Programmable<br>Receive Parser|Yes|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2941 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table 487. Specific configuration information (continued) 

||Maximum Packet Header Size|128|
|---|---|---|
||for Parsing||
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
||Enable One Step timestamp for PTP over<br>UDP/IP feature|No|
||Enable One Step timestamp feature|Yes|
|Multiple queue support|||
||Number of transmit Queue|2|
||Number of recieve Queue|2|
||Enable data center Bridging|No|
||Enable Audo Vedio Bridging|Yes|
||Enable support for AV in Tx queue 1|No|
||Number of DMA Channel on the<br>receive side|2|
|Time sensitive networking|||
||Enable Enhancement to<br>Schedule traffic(EST)|Yes|
||Width of Time Interval Field in the Gate<br>Control List|24|
||Depth of Gate Control List|256|
||Enable Frame Pre-emption support|Yes|
|Time based scheduling|||
||Enable time based Scheduling|Yes|
|TCP/IP offloading features|||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2942 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table 487. Specific configuration information (continued) 

||Enable receive TCP/IP Checksum Check|Enabled by default|
|---|---|---|
||Enable transmit TCP/IP<br>Checksum offload|Enabled by default|
||Enable support for Tx COE in Tx queue 0|Yes|
||Enable support for Tx COE in Tx queue 1|No|
||Enable TCP Segmentation offloading for<br>TCP/IP|No|
||Enable Split Header Feature|No|
||Enable IPv4 ARP offload|No|
|RMON counters|||
||Enable MAC<br>Management Counters(MMC)|Yes|
||Enable the MAC Management Counters<br>for Reciever TCP/IP Checksum offload|No|
|Automotive safety feature|||
||Enable all automotive safety feature|Yes|



### 74.1.2 Impact of MAC flush commands on MAC_PPSx_Target_Time_Seconds register 

If the software discards the media clock generation request by configuring the PPSCTRL_PPSCMD (or PPSCMD#i) field of MAC_PPS_Control register to 0, the MAC does not flush the captured presentation time, i.e., the MAC_PPSx_Target_Time_Seconds register contents don't get changed. 

## 74.4 Introduction 

This section and all its sub-sections are Synopsys Proprietary. Used with permission. 

##### EMAC: 

- Supports the 10/100 Mbps application in compliance with IEEE802.3-2015 specifications 

- Can support advanced applications such as time-sensitive networking and AVB 

- Supports a MAC core that has prominent features such as a flexible receive parser, media clock recovery and generation, and safety 

### 74.4.1 Features 

EMAC supports these features in addition to the default feature defined in the IEEE802.3 specification: 

- MII (10/100 Mbps), RMII (10/100 Mbps) 

- Time-aware shaper (IEEE802.1bv), time synchronization (IEEE802.1AS-rev), and frame preemption (IEEE802.1Qbu) for time-sensitive networking 

- Media clock recovery and generation for AVB 

- AMBA 2.0 for AHB master and APB3 interface 

- RMII specification version 1.2 from RMII consortium 

- Separate interface for transmit, receive, and control paths 

- Two-buffer ring 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2943 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

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

~~<mark>NOTE</mark>~~ 

The DCB feature discussed in the following section(s) is not supported. 

### 74.4.2 Functional block diagram 

This figure shows the EMAC block diagram. EMAC has four main blocks to perform all the functions. 

- The AHB interface is connected to all DMA channels. 

- The DMA arbiter helps in the arbitration of all paths (transmit and receive) in DMA channels. 

- Each channel has a separate set of control and status registers (CSRs) for managing the transmit and receive functions, descriptor handling, and interrupt handling. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2944 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-2945-02.png)


<!-- Start of picture text -->
Transmit<br>memory<br>Transmit MTL transmit RGMII, RMII,<br>MAC<br>DMA FIFO or SGMII<br>transmit<br>channel control interface<br>Receive MTL receive<br>AHB MAC<br>interface DMA FIFO receive GMII<br>channel control<br>CSR<br>DMA MTL  MAC Core<br>channel CSR CSR<br>APB<br>interace DMA MTL<br>AHB<br>Receive<br>memory<br>DMA arbiter Select<br><!-- End of picture text -->

Figure 394. System-level block diagram 

## 74.5 Architecture 

This section and all its sub-sections are Synopsys Proprietary. Used with permission. 

The section describes EMAC interfaces, protocols, and functionality. These are its main blocks: 

- AHB master and APB3 slave interface 

- DMA controller 

- MTL 

- MAC 

- Interrupts 

### 74.5.1 AHB master and CSR slave (APB3) interface 

The 32-bit APB3 slave interface: 

- Provides access to DMA, MTL, and MAC control and status registers (CSRs) 

- Supports the 32-bit write and read transfers to these CSRs 

- Supports single- and all-burst transfers, and an OKAY response 

The DMA block uses the AHB master interface to interact with the external world. The AHB master interface: 

- Controls data transfer 

- Is AMBA 2.0-compliant with no restrictions 

- Supports 32-bit data transfer 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2945 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

- Supports single and INCR transfers 

- Supports burst-length modes such as Fixed, Unspecified, and Mixed 

### 74.5.2 DMA inclusions 

DMA controller: 

- Includes independent transmit (Tx) and receive (Rx) engines, and a CSR space. The transmit engine transfers data from the system memory to the MTL interface, whereas the receive engine transfers data from the MTL interface to the system memory. 

- Is designed for packet-oriented data transfers such as packets in Ethernet. 

- Communicates with the host through CSR, descriptor lists, and data buffers. 

##### DMA descriptors 

DMA supports up to two transmit and two receive descriptor lists (or DMA channels). The base address of each list is written to the respective transmit and receive descriptor list address registers. A descriptor list is forward linked and the next descriptor is always considered at a fixed offset to the current one, and DMA_CH0_Control[DSL] contols the offset. The number of descriptors in the list is programmed using the respective DMA Channel 0 Tx Descriptor Ring Length (DMA_CH0_TxDesc_Ring_Length) and DMA Channel 0 Rx Descriptor Ring Length (DMA_CH0_RxDesc_Ring_Length) registers. After the DMA processes the last descriptor in the list, it automatically jumps to the descriptor in the list address register to create a descriptor ring. 

EMAC supports the ring structure for DMA descriptors. For more information, see Descriptors . 

The DMA engine uses descriptors to efficiently move data from source to destination with minimal host intervention, and the DMA controller can be programmed to interrupt the host in certain situations. These situations may include packet transmit and receive transfer completion and other normal or error conditions. 

The descriptor lists reside in the physical memory address space of the application. Each descriptor can point to a maximum of two buffers in the system memory, enabling two buffers to be used and physically addressed rather than contiguous buffers in the memory. 

##### Data buffers 

A data buffer resides in the application physical memory space and consists of an entire packet or part of a packet but cannot exceed a single packet. Buffers contain only data. The buffer status is maintained in the descriptor. Data chaining refers to packets that span multiple data buffers. However, a single descriptor cannot span multiple packets. The DMA skips to the data buffer of the next packet when an EOP is detected. 

The next few sections discuss DMA controller. 

#### 74.5.2.1 DMA controller bus burst access 

DMA engines attempt to transfer data in a burst of the maximum size programmed using DMA_CH0_Tx_Control[TxPBL] and DMA_CH0_Rx_Control[RxPBL] of the respective DMAs, which always access the receive and transmit descriptors in the maximum possible (limited by PBL or 16 * 8/bus width) burst length for 16 bytes to be read. The burst transfers that the DMA initates can be split into multiple burst transfers according to the AHB requirements and settings specified in DMA System Bus Mode (DMA_SysBus_Mode). 

The transmit DMA initiates a data transfer only when sufficient space is available in the MTL transmit queue to accommodate either of these: 

- Bytes corresponding to the configured burst (PBL * bus_width/8) 

- Remaining bytes in the transmit buffer without EOP 

- Number of bytes till EOP 

The receive DMA initiates a data transfer in these conditions: 

- Sufficient data is available in the MTL receive queue to accommodate the configured burst 

- EOP (when it is less than the configured burst length) is detected in the receive queue 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2946 / 4640 

NXP Semiconductors 

###### Ethernet Media Access Controller (EMAC) 

DMA indicates the start address and the number of transfers required to the AHB master interface. When the interface is configured for fixed-length burst, it transfers data by using the best combination of the INCR4, INCR8, or INCR16 and SINGLE transactions. If EOP is reached before the fixed burst ends on the AHB interface, DMA performs dummy transfers to complete the fixed burst. Otherwise, DMA_SysBus_Mode[FB] becomes 0. The DMA transfers the data using undefined length (INCR) and SINGLE transactions. 

When the AHB interface is configured for address-aligned beats, both DMA engines ensure that the first-burst transfer that AHB initates is less than or equal to the size of the configured PBL value, and the subsequent beats start at an address aligned to this value. The DMA can only align the address for beats up to size 16 (for PBL > 16) for the AHB interface because it does not support more than INCR16. 

#### 74.5.2.2 DMA application data buffer alignment 

The transmit and receive data buffers do not have any restrictions on start address alignment. For example, in systems with 32-bit memory, the start address for buffers can be aligned to any of the four bytes. However, the DMA always initiates write transfers with an address aligned to the bus width and dummy data (old data) in the invalid byte lanes. The process of write transfer typically happens during the beginning or end of an Ethernet packet transfer. The software driver must discard the dummy bytes based on the start address of the buffer and size of the packet. 

Table 488. Data buffer alignment examples 

|Examples||
|---|---|
|Buffer read|If the transmit buffer address is FF2h (for a 32-bit data bus) and 15 bytes need to be transferred, the DMA reads<br>five full words from address FF0h. However, when DMA transfers data to the MTL transmit queue, the extra<br>bytes (the first two bytes) are dropped or ignored. Similarly, the last 3 bytes of the last transfer are also ignored.<br>The DMA always ensures that it transfers a full 32-bit data to the MTL transmit queue, unless it is the end of<br>the packet.|
|Buffer write|If the receive buffer address is FF2h (for a 64-bit data bus) and 16 bytes of a received packet need to be<br>transferred, the DMA writes 3 full words from address FF0h. However, the first 2 bytes of the first transfer and<br>the last 6 bytes of the third transfer have dummy data. The DMA considers the offset address only if it is the first<br>receive buffer of the packet. It ignores the offset address and performs full-word writes for the middle and last<br>receive buffers of the packet.|



#### 74.5.2.3 DMA buffer size calculations 

DMA does not update the size fields in the transmit and receive descriptors. It updates only the status fields (RDES and TDES) of the descriptors. The driver performs the size calculations. 

The transmit DMA transfers the exact number of bytes (as the buffer size field of TDES2 indicates) to MAC. If a descriptor is marked as first (TDES3[FD] = 1), the DMA marks the first transfer from the buffer as SOP, and if the descriptor is marked as last (TDES3[LD]), the DMA marks the last transfer from that data buffer as EOP to the MTL. 

The receive DMA transfers data to a buffer until the buffer is full or MTL sends the end of packet. When TDES3[FD] = 1, the amount of valid data in a buffer is accurately indicated by the buffer size fields in DMA Channel Rx Control (DMA_CH0_Rx_Control) minus the data buffer pointer offset. The offset is 0 when the data buffer pointer is aligned to the data bus width. If a descriptor is marked as last, the buffer may not be full (as indicated by DMA_CH0_Rx_Control[RBSZ_13_y] and DMA_CH0_Rx_Control[RBSZ_x_0]). To compute the amount of valid data in this final buffer, the driver must read the packet length (PL fields of RDES3[14:0]) and subtract the sum of the buffer sizes of the preceding buffers in this packet. The receive DMA always transfers the start of the next packet with a new descriptor. 

#### 74.5.2.4 DMA arbiter 

The arbiter inside the DMA module performs the arbitration between the transmit and receive channel accesses to the AHB master interface. These two types of arbitrations are supported: 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2947 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

- Round-robin: If DMA_Mode[DA] = 0 and both transmit and receive DMAs simultaneously request access, the arbiter allocates the data bus in ratio sets defined in DMA_Mode[PR]. 

- Fixed-priority: If DMA_Mode[DA] = 1, receive DMA is always prioritized over transmit DMA for data access by default. If DMA_Mode[TXPR] = 1, transmit DMA is prioritized over receive DMA as explained in Table 506. 

### 74.5.3 MTL 

MTL provides the FIFO memory interface to buffer and regulate the packets between system memory and MAC. It also enables data to be transferred between the system clock and MAC clock domains. The MTL layer has two data paths: transmit path and receive path. MTL communicates with the host through ATI on the transmit path and through ARI on the receive path. 

#### 74.5.3.1 Transmit path 

The internal DMA: 

- Handles all transactions for the transmit path through ATI. 

- Pushes the Ethernet packet reads from system memory to the corresponding queue. 

The Ethernet packet, then, pops out and is transfered to MAC when the queue reaches its threshold (Threshold mode) or if the complete packet is in the queue (Store-and-Forward mode). When EOP is transferred, the status of the transmission is taken from MAC and transferred back to the internal DMA. 

#### 74.5.3.1.1 Transmit control word 

This control information related to packet transmission is provided as part of the control word through the ATI interface: 

- Packet length (if DCB is enabled with WFQ scheduling algorithm) 

- CRC pad control 

- Source address insertion control 

- VLAN insertion and replacement control and VLAN tag for outer and inner VLAN tags 

- TCP/IP checksum insertion control 

- One-step timestamping control correction 

- Transmit timestamp enable 

#### 74.5.3.1.2 Transmit operation 

These two modes of operation trigger data read towards MAC: 

- Threshold (or cut-through) mode: This is the default mode. In this mode, as soon as the number of bytes in the queue crosses the configured threshold level (or when the end of packet is written before the threshold is crossed), the data is ready to be popped out and forwarded to MAC. The threshold level is configured by using MTL_TxQ0_Operation_Mode[TTC]. 

- Store-and-Forward mode: In this mode, MTL pops the packet out to MAC only when one or more of the following conditions are true: 

   - A complete packet is stored in the queue. 

   - The transmit FIFO becomes almost full. 

   - The ATI watermark becomes low. 

The watermark becomes low when the requested queue is not spacious enough to accommodate the requested burst length on ATI. Therefore, MTL, when operating in Store-and-Forward mode, allows packet transmission even if the packet length is bigger than the transmit queue size. 

You can flush the complete content of the transmit queue by writing 1 to MTL_TxQ0_Operation_Mode[FTQ] or MTL_TxQ1_Operation_Mode[FTQ], depending on the queue. Doing so initializes the queue pointers to the default state. The FTQ 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2948 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

field returns to 0 by itself. If you write 1 to the FTQ field during a packet transfer from MTL to MAC, MTL stops further transfers because MTL considers the queue to be empty. Therefore, an underflow event occurs at the MAC transmitter. 

#### 74.5.3.1.3 Initialization flow 

After reset, MTL is ready to manage the data flow between DMA and MAC. 

- With single-transmit queue configurations, there are no initialization requirements for enabling MTL. 

- With multiple-transmit queue configurations, initialize the queue size for each of the queues by programming MTL_TxQ0_Operation_Mode[TQS] corresponding to a transmit queue. Also, initialize the MAC block. Internal DMA controllers must be individually enabled through their respective CSRs. 

#### 74.5.3.2 Receive path 

MAC sends packets to the MTL receive module and pushes them into the receive queue. MTL indicates the status (fill level) of the queue to the application or DMA when it crosses the configured receive threshold (MTL_RxQ0_Operation_Mode[RTC]), or when the MTL receive module receives the complete packet in Store-and-Forward mode. MTL also indicates the fill level of the queue so that DMA can initiate preconfigured burst transfers to the AHB interface. 

#### 74.5.3.2.1 Receive operation 

During a receive operation, MTL is MAC's slave. This is the general sequence of events: 

1. When MAC receives a packet, it indicates the availability of receive data. 

2. MAC indicates the SOP and EOP delimiters. 

3. MTL accepts the data and pushes it into the corresponding receive queue. 

4. When MAC transfers EOP to the MTL receive module, MAC also drives the status word that MTL pushes into the corresponding receive queue. 

5. MTL takes the data out of the queue and sends it to DMA depending on these modes: 

   - Threshold mode 

   - Store-and-Forward mode 

The sections that follow discuss these modes. 

#### 74.5.3.2.1.1 Threshold mode 

In Threshold (default) mode, MTL reads the data and indicates its availability to the application or DMA when one of these occurs: 

- Data bytes equal to the threshold amount are written to the receive queue (to MTL_RxQ0_Operation_Mode[RTC] and MTL_RxQ1_Operation_Mode[RTC]). 

- A full packet of data is received into the queue. 

#### 74.5.3.2.1.2 Store-and-Forward mode 

In this mode (when MTL_RxQ0_Operation_Mode[RSF] = 1), the initial receive queue locations are reserved for the status words before writing the SOP. A packet is read out only after it is completely written into the receive queue. In this mode, all error packets are dropped (if configured through MTL_RxQ0_Operation_Mode[FEP]) in such a way that only valid packets are read and forwarded to the application. 

#### 74.5.3.2.2 Multi-packet receive operation 

In Threshold mode, the packet status is available immediately after the packet data. In Store-and-Forward mode, the packet data is available after the packet status. MTL is capable of storing any number of packets in the queue as long as it is not full. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2949 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

If MAC receives a packet when the corresponding receive queue is full, MTL ignores that packet and overflow pulse generates on the corresponding receive queue. In addition, MTL increments the overflow counter in MTL Rx Queue Missed Packet Overflow Count (MTL_RxQ0_Missed_Packet_Overflow_Cnt) for the corresponding queue. 

#### 74.5.3.2.3 Error handling in receive operation 

MTL performs these actions if the MTL receive queue is full before it receives the EOP data from MAC: 

1. Declares an overflow 

2. Drops the whole packet (including the status word) 

3. Increments the overflow counter in DMA (MTL Rx Queue Missed Packet Overflow Count (MTL_RxQ0_Missed_Packet_Overflow_Cnt)) 

This is true even if MTL_RxQ0_Operation_Mode[FEP] is 1. 

If the start address of such a packet is already transferred to the read controller, the rest of the packet is dropped and a dummy EOP is written to the queue along with the status word with overflow status. The status indicates a partial packet because of overflow. In such packets, the Packet Length field is invalid. If the MTL receive queue is configured to operate in the Store-and-Forward mode and the length of the received packet is more than the queue size, overflow occurs and all such packets are dropped. 

The MTL receive control logic can filter errors and undersized packets, if enabled by using MTL_RxQ0_Operation_Mode[FEP] and MTL_RxQ0_Operation_Mode[FUP]. If the start address of one such packet is already transferred to the receive queue read controller, the packet is not filtered. The start address of the packet is transferred to the read controller after the packet crosses the receive threshold defined using MTL_RxQ0_Operation_Mode[RTC]. 

If the MTL receive queue is configured to operate in Store-and-Forward mode, all error packets can be filtered and dropped. For the application or DMA to flush the error packet being read from the queue, it must assert the flush signal. MTL then stops transferring data to the application (DMA). It internally reads the rest of the packet and drops it. MTL then starts transferring the next packet, if it's available. 

### 74.5.4 MAC 

MAC can support the MII and RMII PHY interface and it consists of: 

- MTI 

- MRI 

- MCI 

#### 74.5.4.1 MAC transmission 

The MAC transmission process is as follows: 

1. The transmission initiates when MTL pushes in data with the SOP signal asserted. 

2. After the SOP signal is detected, MAC accepts the data and begins transmitting to RMII or MII. 

3. After the EOP signal is transferred to MAC, it performs one of these steps: 

   - Completes normal packet transmission and sends the transmission status to MTL 

   - Sends retry requests if a normal collision (in Half-Duplex mode) occurs during transmission, and until one of the following is true: 

      - Packet is successfully transmitted. 

      - Maximum retry requests have expired. When this happens, MAC aborts the packet transmission with "excessive collision transmit" status. MAC accepts and drops all further data until it receives the next SOP. The MTL block must retransmit the same packet from SOP on observing a retry request (in the status) from MAC. 

   - If any one of the following happens, MAC aborts the packet transmission: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2950 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

   - No carrier (Half-Duplex mode) 

   - Loss of carrier (Half-Duplex mode) 

   - Excessive deferral (Half-Duplex mode) 

   - Late collisions (Half-Duplex mode) 

   - Jabber 

   - MAC accepts and drops all further data until it receives the next SOP 

4. MAC issues an underflow status if MTL is not able to provide data continuously during transmission. Until the next SOP is received, MAC accepts and drops all further data. 

5. During the normal transfer of a packet from MTL, if MAC receives an SOP without getting an EOP for the previous packet, it ignores the SOP and considers the new packet as a continuation of the previous packet. 

#### 74.5.4.2 MAC reception 

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

### 74.5.5 Interrupts 

EMAC supports interrupt coalescing, which reduces the number of interrupts generated by the module and reduces the CPU load. MAC Interrupt Status (MAC_Interrupt_Status) captures various interrupt events. If the interrupt enable field of an interrupt is 1, the corresponding interrupt generates based on the event status in the Status registers. The Interrupt mode (INTM) field decides whether the interrupt signal is a level signal or pulse signal. See the following table and interrupt map file attached to this document for details. 

Table 489. Interrupt request 

|Interrupt request|Interrupt Enable / Mask Register|Interrupt Flag Register|
|---|---|---|
|Common interrupt|MAC Interrupt Enable (MAC_Interrupt_Enable)|MAC Interrupt<br>Status (MAC_Interrupt_Status)|
||MMC Receive Interrupt<br>Mask (MMC_Rx_Interrupt_Mask)|MMC Receive<br>Interrupt (MMC_Rx_Interrupt)|
||MMC Transmit Interrupt<br>Mask (MMC_Tx_Interrupt_Mask)|MMC Transmit<br>Interrupt (MMC_Tx_Interrupt)|
||MMC FPE Transmit Interrupt<br>Mask (MMC_FPE_Tx_Interrupt_Mask)|MMC Transmit FPE<br>Fragment Counter Interrupt<br>Status (MMC_FPE_Tx_Interrupt)|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2951 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table 489. Interrupt request (continued) 

|Interrupt request|Interrupt Enable / Mask Register|Interrupt Flag Register|
|---|---|---|
||MMC FPE Receive Interrupt<br>Mask (MMC_FPE_Rx_Interrupt_Mask)|MMC Receive Packet Assembly<br>Error Counter Interrupt<br>Status (MMC_FPE_Rx_Interrupt)|
||MTL Debug Control (MTL_DBG_CTL)|MTL Debug Status (MTL_DBG_STS)|
||MTL EST Interrupt Enable (MTL_EST_Intr_Enable)|MTL EST Status (MTL_EST_Status)|
||MTL Rx Parser Interrupt Control<br>Status (MTL_RXP_Interrupt_Control_Status)|MTL Rx Parser Interrupt Control Status<br>(MTL_RXP_Interrupt_Control_Status)|
||MTL Queue 0 Interrupt Control<br>Status (MTL_Q0_Interrupt_Control_Status)|MTL Queue 0 Interrupt Control Status<br>(MTL_Q0_Interrupt_Control_Status)|
||MTL Queue 1 Interrupt Control<br>Status (MTL_Q1_Interrupt_Control_Status)|MTL Queue 1 Interrupt Control Status<br>(MTL_Q1_Interrupt_Control_Status)|
||DMA Channel 0 Interrupt Enable<br>(DMA_CH0_Interrupt_Enable)(transfer complete<br>interrupts only)|DMA_CH0_Interrupt_Status|
||DMA Channel 1 Interrupt Enable<br>(DMA_CH1_Interrupt_Enable)(transfer complete<br>interrupts only)|DMA_CH1_Interrupt_Status|
|||DMA Interrupt<br>Status (DMA_Interrupt_Status)<br>(First level status. Indicates major<br>block event source: DMA channel, MTL<br>or MAC)|
|||MTL Interrupt<br>Status (MTL_Interrupt_Status)<br>(Status summary for MTL block<br>interrupts: Rx Parser, EST, FIFO Debug,<br>Queue 1/Queue 0)|
|Tx interrupt 0/1|DMA Channel Tx Control (DMA_CH0_Tx_Control)<br>DMA Channel 0 Interrupt<br>Enable (DMA_CH0_Interrupt_Enable)|DMA Channel 0<br>Status (DMA_CH0_Status)|
||DMA Channel 1 Tx Control (DMA_CH1_Tx_Control)|DMA Channel 1<br>|
||DMA Channel 1 Interrupt<br>Enable (DMA_CH1_Interrupt_Enable)|Status (DMA_CH1_Status)|
|Rx interrupt 0/1|DMA Channel Rx Control (DMA_CH0_Rx_Control)<br>DMA Channel 0 Interrupt<br>Enable (DMA_CH0_Interrupt_Enable)|DMA Channel 0<br>Status (DMA_CH0_Status)|
||DMA Channel 1 Rx Control (DMA_CH1_Rx_Control)|DMA Channel 1<br>|
||DMA Channel 1 Interrupt<br>Enable (DMA_CH1_Interrupt_Enable)|Status (DMA_CH1_Status)|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2952 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table 489. Interrupt request (continued) 

|Interrupt request|Interrupt Enable / Mask Register|Interrupt Flag Register|
|---|---|---|
|Safety interrupt|MTL ECC Interrupt<br>Enable (MTL_ECC_Interrupt_Enable)|MTL ECC Interrupt<br>Status (MTL_ECC_Interrupt_Status)|
|||MTL Safety Interript<br>Status (MTL_Safety_Interrupt_Status)|
||MTL DPP Control (MTL_DPP_Control)<br>MAC FSM Control (MAC_FSM_Control)|MAC DPP FSM Interrupt Status<br>(MAC_DPP_FSM_Interrupt_Status)|



These are the interrupt output signals that are synchronous to the CSR clock. 

- Sbd_intr_o – common interrupt 

- Sbd_perch_tx_intr_o[max_dma_ch] – interrupt per transmit channel 

- Sbd_perch_rx_intr_o [max_dma_ch] – interrupt per receive channel 

~~<mark>NOTE</mark>~~ 

max_dma_ch = number of transmit/receive queues, which is 2 

The sbd_intr_o common interrupt is a level signal. When it is asserted, a corresponding interrupt event source can be found in DMA Interrupt Status (DMA_Interrupt_Status), which is a read-only register that contains the event source fields corresponding to each DMA channel (transmit and receive queue pair), MAC transaction layer, and MAC blocks. You must then read the following registers and look for the fields that are 1: 

- MAC Interrupt Status (MAC_Interrupt_Status) 

- MTL Interrupt Status (MTL_Interrupt_Status) 

- DMA Channel 0 Status (DMA_CH0_Status) 

The sbd_intr_o interrupt deasserts only when all the enabled interrupt events are clear in their respective status registers, and correspondingly, all the fields in DMA Interrupt Status (DMA_Interrupt_Status) are 0. DMA Channel 0 Status (DMA_CH0_Status) captures all the interrupt events of that transmit DMA and receive DMA channel pair. 

DMA Channel 0 Interrupt Enable (DMA_CH0_Interrupt_Enable) contains the corresponding enable fields for each of the interrupt events. These are the two groups of interrupts in the DMA channel: 

- Normal—DMA_CH0_Status[NIS] indicates this interrupt, which is used for events that occur during the normal transfer of packets (TI, RI, TBU). 

- Abnormal—DMA_CH0_Status[AIS] indicates this interrupt, which is used for error events. 

Interrupts are not queued. If the same interrupt event occurs again before the driver responds to the previous one, no additional interrupts generate. 

The common sbd_intr_o output signal asserts for the transfer complete interrupts only when the corresponding interrupts are enabled in DMA Channel 0 Interrupt Enable (DMA_CH0_Interrupt_Enable). 

EMAC also supports these per-channel transfer-complete interrupt signals: 

- sbd_perch_tx_intr_o[max_dma_ch] (transmit per channel interrupts) 

- sbd_perch_rx_intr_o[max_dma_ch] (receive per channel interrupts) 

The behavior of the RI/TI/sbd_perch_tx_intr_o[]/sbd_perch_rx_intr_o[] changes depends on the configuration specified in DMA_Mode[INTM]. This table explains the transfer complete interrupt behavior. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2953 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table 490. Transfer complete interrupt behavior 

|Interrupt<br>mode|Behavior of sbd_perch_tx_intr_o[] and sbd_perch_rx_intr_o[]|Behavior of the TI/RI<br>interrupts and sbd_intr_o|
|---|---|---|
|INTM = 1|In this mode, these signals indicate the values of the<br>correspondingDMA_CH0_Status[RI]andDMA_CH0_Status[TI]fields when<br>DMA_CH0_Status[RI]andDMA_CH0_Status[TI]are 1, respectively.<br>Therefore, they are level signals that you clear by writing 1 to these fields.<br>The signals do not assert whenDMA_CH0_Status[RI]orDMA_CH0_Status[TI]<br>is 0.|DMA_CH0_Status[RI]and<br>DMA_CH0_Status[TI]are<br>configured as explained.<br>For any RI/TI events:<br>• The sbd_intr_o signal<br>does not assert.<br>• DMA_CH0_Status[NIS]<br>remains 0.|
|INTM = 2|In this mode, RI/TI are queued and indicate the values of the corresponding<br>DMA_CH0_Status[RI]andDMA_CH0_Status[TI]fields when any of these<br>fields is 1. RI and TI are level signals that you clear by writing 1 to these<br>fields. However, the fields become 1 again if another TI/RI event is detected<br>beforeDMA_CH0_Status[RI]andDMA_CH0_Status[TI]become 1 for the<br>previous event.|DMA_CH0_Status[RI]<br>andDMA_CH0_Status[TI]<br>become 1 whenever the<br>transfer complete event is<br>detected and are reset<br>whenever the software driver<br>changes them to 0 by<br>writing 1. However, if another<br>transfer complete event is<br>detected before the software<br>changes it to 0 (services it),<br>EMAC automatically writes 1<br>to these fields again. The<br>generation of the sbd_intr_o<br>signal; however, is not based<br>onDMA_CH0_Status[RI]<br>orDMA_CH0_Status[TI].|



## 74.6 Signal descriptions 

This section and all its sub-sections are Synopsys Proprietary. Used with permission. 

### 74.6.1 Module signals 

This table provides port/signal names and their descriptions. See the IOMUX file attached to this document for details. 

Table 491. Module signals 

|Port name (clock/signal)|I/O|Description|
|---|---|---|
|MII_RMII_TXCLK (Clock)|I|MII: The external PHY provides this<br>transmission clock, which operates at a<br>frequency of 25 MHz in 100 Mbps mode<br>and at 2.5 MHz in 10 Mbps mode. All<br>transmission signals that MAC generates<br>are synchronous to this clock, which is<br>required for all PHY interfaces.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2954 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table 491. Module signals (continued) 

|Port name (clock/signal)|I/O|Description|
|---|---|---|
|||RMII: The RMII interface uses this 50<br>MHz clock. If you select RMII mode,<br>MII_RX_CLK (25 MHz or 2.5 MHz) must<br>be derived from the RMII reference clock.|
|MII_RX_CLK (Clock)|I|The external PHY provides this receive<br>clock for the MII and RMII interfaces.<br>The clock operates at a frequency of<br>25 MHz in 100 Mbps mode and at<br>2.5 MHz in 10 Mbps mode. All MII<br>receive signals that MAC receives are<br>synchronous to MII_RX_CLK. The clock's<br>input is required for all PHY interfaces.|
|EMAC_PPS[3:0] (Signals)|I/O|This group of signals is used as pulse<br>per second in Output mode and as<br>media clock generation trigger in Input<br>mode. The signals trigger input toDUTto<br>capture presentation time. Based on the<br>presentation control value ofMAC PPS<br>Control (MAC_PPS_Control), the signals<br>can be defined as pulse or level signals.|
|MII_RMII_TX_EN (Signal)|O|MAC drives this signal, which performs<br>multiple functions depending on the<br>selected PHY interface as described in<br>this list:<br>• MII: When high, indicates that valid<br>data is being transmitted to the<br>phy_txd_o bus. MII_RMII_TX_EN is<br>synchronous to MII_RMII_TX_CLK.<br>• RMII: When high, indicates that valid<br>data is being transmitted to the<br>phy_txd_o bus. MII_RMII_TX_EN is<br>synchronous to MII_RMII_RX_CLK.|
|MII_RMII_TXD[3:0] (Signals)|O|This is a group of transmit data signals<br>driven by MAC. These signals perform<br>multiple functions depending on the<br>selected PHY interface as described in<br>this list:<br>• MII: Bits[3:0] provide the MII transmit<br>data nibble. The data is valid<br>only when the MII_RMII_TX_EN<br>signal is high. MII_RMII_TXD[3:0] is<br>synchronous to MII_MII_TX_CLK.<br>• RMII: Bits[1:0] provide the RMII<br>transmit data. The data is valid|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2955 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table 491. Module signals (continued) 

|Port name (clock/signal)|I/O|Description|
|---|---|---|
|||only when the MII_RMII_TX_EN<br>signal is high. MII_RMII_TXD[3:0] is<br>synchronous to MII_RMII_TX_CLK.|
|MII_CRS (Signal)|I|This signal is valid only in MII mode.<br>The PHY drives this signal high when<br>the transmit or receive medium is not<br>idle, and drives the signal low when both<br>these mediums are idle. The signal is not<br>synchronous to any clock.|
|MII_COL (Signal)|I|This signal is valid only in MII mode.<br>The PHY drives this signal high when a<br>collision is detected on the medium. The<br>signal is not synchronous to any clock.|
|MII_RMII_RX_DV (Signal)|I|The PHY drives this signal. It performs<br>multiple functions depending on the<br>selected PHY interface as described in<br>this list:<br>• MII: Indicates that the data on the<br>MII_RXD bus is valid. It remains high<br>continuously from the first recovered<br>byte or nibble of the packet through<br>the final recovered byte or nibble<br>of the packet. MII_RMII_RX_DV is<br>synchronous to MII_RX_CLK.<br>• RMII: Contains the CRS and data<br>valid information of the receive<br>interface. MII_RMII_RX_DV is<br>synchronous to MII_RMII_TX_CLK.|
|MII_RMII_RX_ER (Signal)|I|The PHY drives this signal. It performs<br>multiple functions depending on the<br>selected PHY interface as described in<br>this list:<br>• MII: Indicates an error or<br>carrier extension in the received<br>packet of the MII_RXD[3:0] bus.<br>MII_RMII_RX_ER is synchronous<br>to MII_RX_CLK.<br>• RMII: Is not used.|
|MII_RMII_RXD[3:0] (Signals)|I|This is a group of data signals received<br>from the PHY. These signals perform<br>multiple functions depending on the<br>selected PHY interface as described in<br>this list:|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2956 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table 491. Module signals (continued) 

|Port name (clock/signal)|I/O|Description|
|---|---|---|
|||• MII: Bits [3:0] provide the MII receive<br>data nibble. The data is valid<br>only when the MII_RMII_RX_DV<br>signals are high. MII_RMII_RXD[3:0]<br>is synchronous to MII_RX_CLK.<br>• RMII: Bits [1:0] provide the RMII<br>receive data. The data is valid<br>only when the MII_RMII_RX_DV<br>signal is high. MII_RMII_RXD[3:0] is<br>synchronous to MII_RMII_TX_CLK.|
|MII_RMII_MDC|O|MAC provides timing reference<br>for MII_RMII_MDIO or MII<br>through this periodic clock. The<br>application clock generates this<br>clock through a clock divider that<br>MAC_MDIO_Address[CR]controls.|
|MII_RMII_MDIO (Signal)|I/O|MDIO uses this signal to transfer control<br>and data information to PHY.|



## 74.7 EMAC register descriptions 

This section and all its sub-sections are Synopsys Proprietary. Used with permission. 

~~<mark>NOTE</mark>~~ 

This chip has 16 KB allocated per Ethernet controller for configuration space. EMAC uses only 8 KB of this memory and the remaining 8 KB is reserved for future use. Writing to the reserved memory may lead to unintended behavior. 

### 74.7.1 EMAC memory map 

EMAC base address: 4048_0000h 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|0h|MAC Configuration (MAC_Configuration)|32|RW|0000_8000h|
|4h|MAC Extended Configuration (MAC_Ext_Configuration)|32|RW|0000_0000h|
|8h|MAC Packet Filter (MAC_Packet_Filter)|32|RW|0000_0000h|
|Ch|MAC Watchdog Timeout (MAC_Watchdog_Timeout)|32|RW|0000_0000h|
|10h|MAC Hash Table First 32 Bits (MAC_Hash_Table_Reg0)|32|RW|0000_0000h|
|14h|MAC Hash Table Second 32 Bits (MAC_Hash_Table_Reg1)|32|RW|0000_0000h|
|50h|MAC VLAN Tag (MAC_VLAN_Tag)|32|RW|0000_0000h|
|50h|MAC VLAN Tag Control (MAC_VLAN_Tag_Ctrl)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2957 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|54h|MAC VLAN Tag Data (MAC_VLAN_Tag_Data)|32|RW|0000_0000h|
|54h|MAC VLAN Tag Filter 0 (MAC_VLAN_Tag_Filter0)|32|RW|0000_0000h|
|54h|MAC VLAN Tag Filter 1 (MAC_VLAN_Tag_Filter1)|32|RW|0000_0000h|
|54h|MAC VLAN Tag Filter 2 (MAC_VLAN_Tag_Filter2)|32|RW|0000_0000h|
|54h|MAC VLAN Tag Filter 3 (MAC_VLAN_Tag_Filter3)|32|RW|0000_0000h|
|58h|MAC VLAN Hash Table (MAC_VLAN_Hash_Table)|32|RW|0000_0000h|
|60h|MAC VLAN Inclusion Or Replacement (MAC_VLAN_Incl)|32|RW|0000_0000h|
|60h|MAC VLAN Inclusion 0 (MAC_VLAN_Incl0)|32|RW|0000_0000h|
|60h|MAC VLAN Inclusion 1 (MAC_VLAN_Incl1)|32|RW|0000_0000h|
|60h|MAC VLAN Inclusion 2 (MAC_VLAN_Incl2)|32|RW|0000_0000h|
|60h|MAC VLAN Inclusion 3 (MAC_VLAN_Incl3)|32|RW|0000_0000h|
|60h|MAC VLAN Inclusion 4 (MAC_VLAN_Incl4)|32|RW|0000_0000h|
|60h|MAC VLAN Inclusion 5 (MAC_VLAN_Incl5)|32|RW|0000_0000h|
|60h|MAC VLAN Inclusion 6 (MAC_VLAN_Incl6)|32|RW|0000_0000h|
|60h|MAC VLAN Inclusion 7 (MAC_VLAN_Incl7)|32|RW|0000_0000h|
|64h|Inner VLAN Tag Inclusion Or Replacement (MAC_Inner_VLAN_Incl)|32|RW|0000_0000h|
|70h|MAC Q0 Tx Flow Control (MAC_Q0_Tx_Flow_Ctrl)|32|RW|0000_0000h|
|90h|MAC Receive Flow Control (MAC_Rx_Flow_Ctrl)|32|RW|0000_0000h|
|94h|MAC RxQ Control 4 (MAC_RxQ_Ctrl4)|32|RW|0000_0000h|
|A0h|MAC RxQ Control 0 (MAC_RxQ_Ctrl0)|32|RW|0000_0000h|
|A4h|Receive Queue Control 1 (MAC_RxQ_Ctrl1)|32|RW|0000_0000h|
|A8h|MAC RxQ Control 2 (MAC_RxQ_Ctrl2)|32|RW|0000_0000h|
|B0h|MAC Interrupt Status (MAC_Interrupt_Status)|32|RO|0000_0000h|
|B4h|MAC Interrupt Enable (MAC_Interrupt_Enable)|32|RW|0000_0000h|
|B8h|MAC Rx Transmit Status (MAC_Rx_Tx_Status)|32|RO|0000_0000h|
|110h|MAC Version (MAC_Version)|32|RO|0000_1051h|
|114h|MAC Debug (MAC_Debug)|32|RO|0000_0000h|
|11Ch|MAC Hardware Feature 0 (MAC_HW_Feature0)|32|RO|0E09_5135h|
|120h|MAC Hardware Feature 1 (MAC_HW_Feature1)|32|RO|2118_29A6h|
|124h|MAC Hardware Feature 2 (MAC_HW_Feature2)|32|RO|0404_1041h|
|128h|MAC Hardware Feature 3 (MAC_HW_Feature3)|32|RO|2C37_0E31h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2958 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|140h|MAC DPP FSM Interrupt Status (MAC_DPP_FSM_Interrupt_Status)|32|R2C|0000_0000h|
|148h|MAC FSM Control (MAC_FSM_Control)|32|RW|0000_0000h|
|14Ch|MAC FSM ACT Timer (MAC_FSM_ACT_Timer)|32|RW|0000_0000h|
|150h|SCS_REG 1 (SCS_REG1)|32|RW|0000_0000h|
|200h|MAC MDIO Address (MAC_MDIO_Address)|32|RW|0000_0000h|
|204h|MAC MDIO Data (MAC_MDIO_Data)|32|RW|0000_0000h|
|230h|MAC CSR Software Control (MAC_CSR_SW_Ctrl)|32|RW|0000_0000h|
|234h|MAC FPE Control STS (MAC_FPE_CTRL_STS)|32|RW|0000_0000h|
|240h|MAC Presentation Time (MAC_Presn_Time_ns)|32|RO|0000_0000h|
|244h|MAC Presentation Time Update (MAC_Presn_Time_Updt)|32|RW|0000_0000h|
|300h|MAC Address 0 High (MAC_Address0_High)|32|RW|8000_FFFFh|
|304h|MAC Address 0 Low (MAC_Address0_Low)|32|RW|FFFF_FFFFh|
|308h|MAC Address 1 High (MAC_Address1_High)|32|RW|0000_FFFFh|
|30Ch|MAC Address 1 Low (MAC_Address1_Low)|32|RW|FFFF_FFFFh|
|310h|MAC Address 2 High (MAC_Address2_High)|32|RW|0000_FFFFh|
|314h|MAC Address 2 Low (MAC_Address2_Low)|32|RW|FFFF_FFFFh|
|700h|MMC Control (MMC_Control)|32|RW|0000_0000h|
|704h|MMC Receive Interrupt (MMC_Rx_Interrupt)|32|RO|0000_0000h|
|708h|MMC Transmit Interrupt (MMC_Tx_Interrupt)|32|RO|0000_0000h|
|70Ch|MMC Receive Interrupt Mask (MMC_Rx_Interrupt_Mask)|32|RW|0000_0000h|
|710h|MMC Transmit Interrupt Mask (MMC_Tx_Interrupt_Mask)|32|RW|0000_0000h|
|714h|Transmit Octet Count Good Bad (Tx_Octet_Count_Good_Bad)|32|RO|0000_0000h|
|718h|Transmit Packet Count Good Bad (Tx_Packet_Count_Good_Bad)|32|RO|0000_0000h|
|71Ch|Transmit Broadcast Packets Good (Tx_Broadcast_Packets_Good)|32|RO|0000_0000h|
|720h|Transmit Multicast Packets Good (Tx_Multicast_Packets_Good)|32|RO|0000_0000h|
|724h|Transmit 64-Octet Packets Good Bad<br>(Tx_64Octets_Packets_Good_Bad)|32|RO|0000_0000h|
|728h|Transmit 65 To 127 Octet Packets Good Bad<br>(Tx_65To127Octets_Packets_Good_Bad)|32|RO|0000_0000h|
|72Ch|Transmit 128 To 255 Octet Packets Good Bad<br>(Tx_128To255Octets_Packets_Good_Bad)|32|RO|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2959 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|730h|Transmit 256 To 511 Octet Packets Good Bad<br>(Tx_256To511Octets_Packets_Good_Bad)|32|RO|0000_0000h|
|734h|Transmit 512 To 1023 Octet Packets Good Bad<br>(Tx_512To1023Octets_Packets_Good_Bad)|32|RO|0000_0000h|
|738h|Transmit 1024 To Max Octet Packets Good Bad<br>(Tx_1024ToMaxOctets_Packets_Good_Bad)|32|RO|0000_0000h|
|73Ch|Transmit Unicast Packets Good Bad<br>(Tx_Unicast_Packets_Good_Bad)|32|RO|0000_0000h|
|740h|Transmit Multicast Packets Good Bad<br>(Tx_Multicast_Packets_Good_Bad)|32|RO|0000_0000h|
|744h|Transmit Broadcast Packets Good Bad<br>(Tx_Broadcast_Packets_Good_Bad)|32|RO|0000_0000h|
|748h|Transmit Underflow Error Packets (Tx_Underflow_Error_Packets)|32|RO|0000_0000h|
|74Ch|Transmit Single Collision Good Packets<br>(Tx_Single_Collision_Good_Packets)|32|RO|0000_0000h|
|750h|Transmit Multiple Collision Good Packets<br>(Tx_Multiple_Collision_Good_Packets)|32|RO|0000_0000h|
|754h|Transmit Deferred Packets (Tx_Deferred_Packets)|32|RO|0000_0000h|
|758h|Transmit Late Collision Packets (Tx_Late_Collision_Packets)|32|RO|0000_0000h|
|75Ch|Transmit Excessive Collision Packets<br>(Tx_Excessive_Collision_Packets)|32|RO|0000_0000h|
|760h|Transmit Carrier Error Packets (Tx_Carrier_Error_Packets)|32|RO|0000_0000h|
|764h|Transmit Octet Count Good (Tx_Octet_Count_Good)|32|RO|0000_0000h|
|768h|Transmit Packet Count Good (Tx_Packet_Count_Good)|32|RO|0000_0000h|
|76Ch|Transmit Excessive Deferral Error (Tx_Excessive_Deferral_Error)|32|RO|0000_0000h|
|770h|Transmit Pause Packets (Tx_Pause_Packets)|32|RO|0000_0000h|
|774h|Transmit VLAN Packets Good (Tx_VLAN_Packets_Good)|32|RO|0000_0000h|
|778h|Transmit O Size Packets Good (Tx_OSize_Packets_Good)|32|RO|0000_0000h|
|780h|Receive Packets Count Good Bad (Rx_Packets_Count_Good_Bad)|32|RO|0000_0000h|
|784h|Receive Octet Count Good Bad (Rx_Octet_Count_Good_Bad)|32|RO|0000_0000h|
|788h|Receive Octet Count Good (Rx_Octet_Count_Good)|32|RO|0000_0000h|
|78Ch|Receive Broadcast Packets Good (Rx_Broadcast_Packets_Good)|32|RO|0000_0000h|
|790h|Receive Multicast Packets Good (Rx_Multicast_Packets_Good)|32|RO|0000_0000h|
|794h|Receive CRC Error Packets (Rx_CRC_Error_Packets)|32|RO|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2960 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|798h|Receive Alignment Error Packets (Rx_Alignment_Error_Packets)|32|RO|0000_0000h|
|79Ch|Receive Runt Error Packets (Rx_Runt_Error_Packets)|32|RO|0000_0000h|
|7A0h|Receive Jabber Error Packets (Rx_Jabber_Error_Packets)|32|RO|0000_0000h|
|7A4h|Receive Undersize Packets Good (Rx_Undersize_Packets_Good)|32|RO|0000_0000h|
|7A8h|Receive Oversize Packets Good (Rx_Oversize_Packets_Good)|32|RO|0000_0000h|
|7ACh|Receive 64 Octets Packets Good Bad<br>(Rx_64Octets_Packets_Good_Bad)|32|RO|0000_0000h|
|7B0h|Receive 65-127 Octets Packets Good Bad<br>(Rx_65To127Octets_Packets_Good_Bad)|32|RO|0000_0000h|
|7B4h|Receive 128-255 Octets Packets Good Bad<br>(Rx_128To255Octets_Packets_Good_Bad)|32|RO|0000_0000h|
|7B8h|Receive 256-511 Octets Packets Good Bad<br>(Rx_256To511Octets_Packets_Good_Bad)|32|RO|0000_0000h|
|7BCh|Receive 512-1023 Octets Packets Good Bad<br>(Rx_512To1023Octets_Packets_Good_Bad)|32|RO|0000_0000h|
|7C0h|Receive 1024 To Max Octets Good Bad<br>(Rx_1024ToMaxOctets_Packets_Good_Bad)|32|RO|0000_0000h|
|7C4h|Receive Unicast Packets Good (Rx_Unicast_Packets_Good)|32|RO|0000_0000h|
|7C8h|Receive Length Error Packets (Rx_Length_Error_Packets)|32|RO|0000_0000h|
|7CCh|Receive Out of Range Type Packet<br>(Rx_Out_Of_Range_Type_Packets)|32|RO|0000_0000h|
|7D0h|Receive Pause Packets (Rx_Pause_Packets)|32|RO|0000_0000h|
|7D4h|Receive FIFO Overflow Packets (Rx_FIFO_Overflow_Packets)|32|RO|0000_0000h|
|7D8h|Receive VLAN Packets Good Bad (Rx_VLAN_Packets_Good_Bad)|32|RO|0000_0000h|
|7DCh|Receive Watchdog Error Packets (Rx_Watchdog_Error_Packets)|32|RO|0000_0000h|
|7E0h|Receive Receive Error Packets (Rx_Receive_Error_Packets)|32|RO|0000_0000h|
|7E4h|Receive Control Packets Good (Rx_Control_Packets_Good)|32|RO|0000_0000h|
|8A0h|MMC Transmit FPE Fragment Counter Interrupt Status<br>(MMC_FPE_Tx_Interrupt)|32|RO|0000_0000h|
|8A4h|MMC FPE Transmit Interrupt Mask (MMC_FPE_Tx_Interrupt_Mask)|32|RW|0000_0000h|
|8A8h|Transmit FPE Fragment Counter (MMC_Tx_FPE_Fragment_Cntr)|32|RO|0000_0000h|
|8ACh|Transmit Hold Request Counter (MMC_Tx_Hold_Req_Cntr)|32|RO|0000_0000h|
|8C0h|MMC Receive Packet Assembly Error Counter Interrupt Status<br>(MMC_FPE_Rx_Interrupt)|32|RO|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2961 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|8C4h|MMC FPE Receive Interrupt Mask (MMC_FPE_Rx_Interrupt_Mask)|32|RW|0000_0000h|
|8C8h|MMC Receive Packet Assembly Error Counter<br>(MMC_Rx_Packet_Assembly_Err_Cntr)|32|RO|0000_0000h|
|8CCh|MMC Receive Packet SMD Error Counter<br>(MMC_Rx_Packet_SMD_Err_Cntr)|32|RO|0000_0000h|
|8D0h|MMC Receive Packet Assembly OK Counter<br>(MMC_Rx_Packet_Assembly_OK_Cntr)|32|RO|0000_0000h|
|8D4h|MMC Receive FPE Fragment Counter<br>(MMC_Rx_FPE_Fragment_Cntr)|32|RO|0000_0000h|
|900h|MAC Layer 3 Layer 4 Control 0 (MAC_L3_L4_Control0)|32|RW|0000_0000h|
|904h|MAC Layer 4 Address 0 (MAC_Layer4_Address0)|32|RW|0000_0000h|
|910h|MAC Layer 3 Address 0 Reg 0 (MAC_Layer3_Addr0_Reg0)|32|RW|0000_0000h|
|914h|MAC Layer 3 Address 1 Reg 0 (MAC_Layer3_Addr1_Reg0)|32|RW|0000_0000h|
|918h|MAC Layer 3 Address 2 Reg 0 (MAC_Layer3_Addr2_Reg0)|32|RW|0000_0000h|
|91Ch|MAC Layer 3 Address 3 Reg 0 (MAC_Layer3_Addr3_Reg0)|32|RW|0000_0000h|
|930h|MAC L3 L4 Control 1 (MAC_L3_L4_Control1)|32|RW|0000_0000h|
|934h|MAC Layer 4 Address 1 (MAC_Layer4_Address1)|32|RW|0000_0000h|
|940h|MAC Layer 3 Address 0 Reg 1 (MAC_Layer3_Addr0_Reg1)|32|RW|0000_0000h|
|944h|MAC Layer 3 Address 1 Reg 1 (MAC_Layer3_Addr1_Reg1)|32|RW|0000_0000h|
|948h|MAC Layer 3 Address 2 Reg 1 (MAC_Layer3_Addr2_Reg1)|32|RW|0000_0000h|
|94Ch|MAC Layer 3 Address 3 Reg 1 (MAC_Layer3_Addr3_Reg1)|32|RW|0000_0000h|
|960h|MAC L3 L4 Control 2 (MAC_L3_L4_Control2)|32|RW|0000_0000h|
|964h|MAC Layer 4 Address 2 (MAC_Layer4_Address2)|32|RW|0000_0000h|
|970h|MAC Layer 3 Address 0 Reg 2 (MAC_Layer3_Addr0_Reg2)|32|RW|0000_0000h|
|974h|MAC Layer 3 Address 1 Reg 2 (MAC_Layer3_Addr1_Reg2)|32|RW|0000_0000h|
|978h|MAC Layer 3 Address 2 Reg 2 (MAC_Layer3_Addr2_Reg2)|32|RW|0000_0000h|
|97Ch|MAC Layer 3 Address 3 Reg 2 (MAC_Layer3_Addr3_Reg2)|32|RW|0000_0000h|
|990h|MAC L3 L4 Control 3 (MAC_L3_L4_Control3)|32|RW|0000_0000h|
|994h|MAC Layer 4 Address 3 (MAC_Layer4_Address3)|32|RW|0000_0000h|
|9A0h|MAC Layer 3 Address 0 Reg 3 (MAC_Layer3_Addr0_Reg3)|32|RW|0000_0000h|
|9A4h|MAC Layer 3 Address 1 Reg 3 (MAC_Layer3_Addr1_Reg3)|32|RW|0000_0000h|
|9A8h|MAC Layer 3 Address 2 Reg 3 (MAC_Layer3_Addr2_Reg3)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2962 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|9ACh|MAC Layer 3 Address 3 Reg 3 (MAC_Layer3_Addr3_Reg3)|32|RW|0000_0000h|
|B00h|MAC Timestamp Control (MAC_Timestamp_Control)|32|RW|0000_2000h|
|B04h|MAC Sub Second Increment (MAC_Sub_Second_Increment)|32|RW|0000_0000h|
|B08h|MAC System Time In Seconds (MAC_System_Time_Seconds)|32|RO|0000_0000h|
|B0Ch|MAC System Time In Nanoseconds<br>(MAC_System_Time_Nanoseconds)|32|RO|0000_0000h|
|B10h|MAC System Time Seconds Update<br>(MAC_System_Time_Seconds_Update)|32|RW|0000_0000h|
|B14h|MAC System Time Nanoseconds Update<br>(MAC_System_Time_Nanoseconds_Update)|32|RW|0000_0000h|
|B18h|MAC Timestamp Addend (MAC_Timestamp_Addend)|32|RW|0000_0000h|
|B1Ch|MAC System Time Higher Word In Seconds<br>(MAC_System_Time_Higher_Word_Seconds)|32|RW|0000_0000h|
|B20h|MAC Timestamp Status (MAC_Timestamp_Status)|32|RO|0000_0000h|
|B30h|MAC Transmit Timestamp Status In Nanoseconds<br>(MAC_Tx_Timestamp_Status_Nanoseconds)|32|RO|0000_0000h|
|B34h|MAC Transmit Timestamp Status In Seconds<br>(MAC_Tx_Timestamp_Status_Seconds)|32|RO|0000_0000h|
|B50h|MAC Timestamp Ingress Asymmetry Correction<br>(MAC_Timestamp_Ingress_Asym_Corr)|32|RW|0000_0000h|
|B54h|MAC Timestamp Egress Asymmetry Correction<br>(MAC_Timestamp_Egress_Asym_Corr)|32|RW|0000_0000h|
|B58h|MAC Timestamp Ingress Correction In Nanoseconds<br>(MAC_Timestamp_Ingress_Corr_Nanosecond)|32|RW|0000_0000h|
|B5Ch|MAC Timestamp Egress Correction In Nanoseconds<br>(MAC_Timestamp_Egress_Corr_Nanosecond)|32|RW|0000_0000h|
|B60h|MAC Timestamp Ingress Correction In Subnanoseconds<br>(MAC_Timestamp_Ingress_Corr_Subnanosec)|32|RW|0000_0000h|
|B64h|MAC Timestamp Engress Correction In Subnanoseconds<br>(MAC_Timestamp_Egress_Corr_Subnanosec)|32|RW|0000_0000h|
|B68h|MAC Timestamp Ingress Latency<br>(MAC_Timestamp_Ingress_Latency)|32|RO|0000_0000h|
|B6Ch|MAC Timestamp Egress Latecy (MAC_Timestamp_Egress_Latency)|32|RO|0000_0000h|
|B70h|MAC PPS Control (MAC_PPS_Control)|32|RW|0000_0000h|
|B80h|MAC PPS0 Target Time In Seconds<br>(MAC_PPS0_Target_Time_Seconds)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2963 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|B84h|MAC PPS0 Target Time In Nanoseconds<br>(MAC_PPS0_Target_Time_Nanoseconds)|32|RW|0000_0000h|
|B88h|MAC PPS0 Interval (MAC_PPS0_Interval)|32|RW|0000_0000h|
|B8Ch|MAC PPS0 Width (MAC_PPS0_Width)|32|RW|0000_0000h|
|B90h|MAC PPS1 Target Time In Seconds<br>(MAC_PPS1_Target_Time_Seconds)|32|RW|0000_0000h|
|B94h|MAC PPS1 Target Time In Nanoseconds<br>(MAC_PPS1_Target_Time_Nanoseconds)|32|RW|0000_0000h|
|B98h|MAC PPS1 Interval (MAC_PPS1_Interval)|32|RW|0000_0000h|
|B9Ch|MAC PPS1 Width (MAC_PPS1_Width)|32|RW|0000_0000h|
|BA0h|MAC PPS2 Taget Time In Seconds<br>(MAC_PPS2_Target_Time_Seconds)|32|RW|0000_0000h|
|BA4h|MAC PPS2 Target Time In Nanoseconds<br>(MAC_PPS2_Target_Time_Nanoseconds)|32|RW|0000_0000h|
|BA8h|MAC PPS2 Interval (MAC_PPS2_Interval)|32|RW|0000_0000h|
|BACh|MAC PPS2 Width (MAC_PPS2_Width)|32|RW|0000_0000h|
|BB0h|MAC PPS3 Target Time In Seconds<br>(MAC_PPS3_Target_Time_Seconds)|32|RW|0000_0000h|
|BB4h|MAC PPS3 Target Time In Nanoseconds<br>(MAC_PPS3_Target_Time_Nanoseconds)|32|RW|0000_0000h|
|BB8h|MAC PPS3 Interval (MAC_PPS3_Interval)|32|RW|0000_0000h|
|BBCh|MAC PPS3 Width (MAC_PPS3_Width)|32|RW|0000_0000h|
|C00h|MTL Operation Mode (MTL_Operation_Mode)|32|RW|0000_0000h|
|C08h|MTL Debug Control (MTL_DBG_CTL)|32|RW|0000_0000h|
|C0Ch|MTL Debug Status (MTL_DBG_STS)|32|RW|0000_0018h|
|C10h|MTL FIFO Debug Data (MTL_FIFO_Debug_Data)|32|RW|0000_0000h|
|C20h|MTL Interrupt Status (MTL_Interrupt_Status)|32|RO|0000_0000h|
|C30h|MTL Receive Queue DMA Map 0 (MTL_RxQ_DMA_Map0)|32|RW|0000_0000h|
|C40h|MTL TBS Control (MTL_TBS_CTRL)|32|RW|0000_0000h|
|C50h|MTL EST Control (MTL_EST_Control)|32|RW|0000_0000h|
|C58h|MTL EST Status (MTL_EST_Status)|32|RW|0000_0000h|
|C60h|MTL EST Scheduling Error (MTL_EST_Sch_Error)|32|RW|0000_0000h|
|C64h|MTL EST Frame Size Error (MTL_EST_Frm_Size_Error)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2964 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|C68h|MTL EST Frame Size Capture (MTL_EST_Frm_Size_Capture)|32|RO|0000_0000h|
|C70h|MTL EST Interrupt Enable (MTL_EST_Intr_Enable)|32|RW|0000_0000h|
|C80h|MTL EST GCL Control (MTL_EST_GCL_Control)|32|RW|0000_0000h|
|C84h|MTL EST GCL Data (MTL_EST_GCL_Data)|32|RW|0000_0000h|
|C90h|MTL FPE Control Status (MTL_FPE_CTRL_STS)|32|RW|0000_0000h|
|C94h|MTL FPE Advance (MTL_FPE_Advance)|32|RW|0000_0000h|
|CA0h|MTL Rx Parser Control Status (MTL_RXP_Control_Status)|32|RW|803F_003Fh|
|CA4h|MTL Rx Parser Interrupt Control Status<br>(MTL_RXP_Interrupt_Control_Status)|32|RW|0000_0000h|
|CA8h|MTL Rx Parser Drop Count (MTL_RXP_Drop_Cnt)|32|RO|0000_0000h|
|CACh|MTL Rx Parser Error Count (MTL_RXP_Error_Cnt)|32|RO|0000_0000h|
|CB0h|MTL Rx Parser Indirect Access Control Status<br>(MTL_RXP_Indirect_Acc_Control_Status)|32|RW|0000_0000h|
|CB4h|MTL Rx Parser Indirect Access Data (MTL_RXP_Indirect_Acc_Data)|32|RO|0000_0000h|
|CC0h|MTL ECC Control (MTL_ECC_Control)|32|RW|0000_000Fh|
|CC4h|MTL Safety Interript Status (MTL_Safety_Interrupt_Status)|32|RO|0000_0000h|
|CC8h|MTL ECC Interrupt Enable (MTL_ECC_Interrupt_Enable)|32|RW|0000_1111h|
|CCCh|MTL ECC Interrupt Status (MTL_ECC_Interrupt_Status)|32|RW|0000_0000h|
|CD0h|MTL ECC Error Status (MTL_ECC_Err_Sts_Rctl)|32|RW|0000_0000h|
|CD4h|MTL ECC Error Adress Status (MTL_ECC_Err_Addr_Status)|32|RO|0000_0000h|
|CD8h|MTL ECC Error Control Status (MTL_ECC_Err_Cntr_Status)|32|RO|0000_0000h|
|CE0h|MTL DPP Control (MTL_DPP_Control)|32|RW|0000_0003h|
|D00h|MTL Tx Queue 0 Operation Mode (MTL_TxQ0_Operation_Mode)|32|RW|0000_0000h|
|D04h|MTL Tx Queue 0 Underflow (MTL_TxQ0_Underflow)|32|RO|0000_0000h|
|D08h|MTL Tx Queue 0 Debug (MTL_TxQ0_Debug)|32|RO|0000_0000h|
|D14h|MTL Tx Queue 0 ETS Status (MTL_TxQ0_ETS_Status)|32|RO|0000_0000h|
|D18h|MTL Tx Queue Quantum Weight (MTL_TxQ0_Quantum_Weight)|32|RW|0000_0000h|
|D2Ch|MTL Queue 0 Interrupt Control Status<br>(MTL_Q0_Interrupt_Control_Status)|32|RW|0000_0000h|
|D30h|MTL Rx Queue 0 Operation Mode (MTL_RxQ0_Operation_Mode)|32|RW|0000_0000h|
|D34h|MTL Rx Queue Missed Packet Overflow Count<br>(MTL_RxQ0_Missed_Packet_Overflow_Cnt)|32|RO|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2965 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|D38h|MTL Rx Queue 0 Debug (MTL_RxQ0_Debug)|32|RO|0000_0000h|
|D3Ch|MTL Rx Queue 0 Control 0 (MTL_RxQ0_Control)|32|RW|0000_0000h|
|D40h|MTL Tx Queue 1 Operation Mode (MTL_TxQ1_Operation_Mode)|32|RW|0000_0000h|
|D44h|MTL Tx Queue 1 Underflow (MTL_TxQ1_Underflow)|32|RO|0000_0000h|
|D48h|MTL Tx Queue 1 Debug (MTL_TxQ1_Debug)|32|RO|0000_0000h|
|D50h|MTL Tx Queue 1 ETS Control (MTL_TxQ1_ETS_Control)|32|RW|0000_0000h|
|D54h|MTL Tx Queue 1 ETS Status (MTL_TxQ1_ETS_Status)|32|RO|0000_0000h|
|D58h|MTL Tx Queue 1 Quantum Weight (MTL_TxQ1_Quantum_Weight)|32|RW|0000_0000h|
|D5Ch|MTL Tx Queue 1 Sendslope Credit (MTL_TxQ1_SendSlopeCredit)|32|RW|0000_0000h|
|D60h|MTL Tx Queue 1 HiCredit (MTL_TxQ1_HiCredit)|32|RW|0000_0000h|
|D64h|MTL Tx Queue 1 LoCredit (MTL_TxQ1_LoCredit)|32|RW|0000_0000h|
|D6Ch|MTL Queue 1 Interrupt Control Status<br>(MTL_Q1_Interrupt_Control_Status)|32|RW|0000_0000h|
|D70h|MTL Rx Queue 1 Operation Mode (MTL_RxQ1_Operation_Mode)|32|RW|0000_0000h|
|D74h|MTL Rx Queue 1 Missed Packet Overflow Counter<br>(MTL_RxQ1_Missed_Packet_Overflow_Cnt)|32|RO|0000_0000h|
|D78h|MTL Rx Queue 1 Debug (MTL_RxQ1_Debug)|32|RO|0000_0000h|
|D7Ch|MTL Rx Queue 1 Control (MTL_RxQ1_Control)|32|RW|0000_0000h|
|1000h|DMA Mode (DMA_Mode)|32|RW|0000_0000h|
|1004h|DMA System Bus Mode (DMA_SysBus_Mode)|32|RW|0000_0000h|
|1008h|DMA Interrupt Status (DMA_Interrupt_Status)|32|RO|0000_0000h|
|100Ch|DMA Debug Status 0 (DMA_Debug_Status0)|32|RO|0000_0000h|
|1050h|DMA TBS Control (DMA_TBS_CTRL)|32|RW|0000_0000h|
|1080h|DMA Safety Interrupt Status (DMA_Safety_Interrupt_Status)|32|RO|0000_0000h|
|1100h|DMA Channel 0 Control (DMA_CH0_Control)|32|RW|0000_0000h|
|1104h|DMA Channel Tx Control (DMA_CH0_Tx_Control)|32|RW|0000_0000h|
|1108h|DMA Channel Rx Control (DMA_CH0_Rx_Control)|32|RW|0000_0000h|
|1114h|DMA Channel 0 Tx Descriptor List Address<br>(DMA_CH0_TxDesc_List_Address)|32|RW|0000_0000h|
|111Ch|DMA Channel 0 Rx Descriptor List Address<br>(DMA_CH0_RxDesc_List_Address)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2966 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|1120h|DMA Channel 0 Tx Descriptor Tail Pointer<br>(DMA_CH0_TxDesc_Tail_Pointer)|32|RW|0000_0000h|
|1128h|DMA Channeli 0 Rx Descriptor List Pointer<br>(DMA_CH0_RxDesc_Tail_Pointer)|32|RW|0000_0000h|
|112Ch|DMA Channel 0 Tx Descriptor Ring Length<br>(DMA_CH0_TxDesc_Ring_Length)|32|RW|0000_0000h|
|1130h|DMA Channel 0 Rx Descriptor Ring Length<br>(DMA_CH0_RxDesc_Ring_Length)|32|RW|0000_0000h|
|1134h|DMA Channel 0 Interrupt Enable (DMA_CH0_Interrupt_Enable)|32|RW|0000_0000h|
|1138h|DMA Channel 0 Rx Interrupt Watchdog Timer<br>(DMA_CH0_Rx_Interrupt_Watchdog_Timer)|32|RW|0000_0000h|
|113Ch|DMA Channel 0 Slot Function Control Status<br>(DMA_CH0_Slot_Function_Control_Status)|32|RW|0000_07C0h|
|1144h|DMA Channel 0 Current Application Transmit Descriptor<br>(DMA_CH0_Current_App_TxDesc)|32|RO|0000_0000h|
|114Ch|DMA Channel 0 Current Application Receive Descriptor<br>(DMA_CH0_Current_App_RxDesc)|32|RO|0000_0000h|
|1154h|DMA Channel 0 Current Application Transmit Descriptor<br>(DMA_CH0_Current_App_TxBuffer)|32|RO|0000_0000h|
|115Ch|DMA Channel 0 Current Application Receive Buffer<br>(DMA_CH0_Current_App_RxBuffer)|32|RO|0000_0000h|
|1160h|DMA Channel 0 Status (DMA_CH0_Status)|32|RW|0000_0000h|
|1164h|DMA Channel 0 Miss Frame Counter (DMA_CH0_Miss_Frame_Cnt)|32|RO|0000_0000h|
|1168h|DMA Channel 0 Rx Parser Accept Count<br>(DMA_CH0_RXP_Accept_Cnt)|32|RO|0000_0000h|
|116Ch|DMA Channel 0 Rx ERI Count (DMA_CH0_RX_ERI_Cnt)|32|RO|0000_0000h|
|1180h|DMA Channel 1 Control (DMA_CH1_Control)|32|RW|0000_0000h|
|1184h|DMA Channel 1 Tx Control (DMA_CH1_Tx_Control)|32|RW|0000_0000h|
|1188h|DMA Channel 1 Rx Control (DMA_CH1_Rx_Control)|32|RW|0000_0000h|
|1194h|DMA Channel 1 Tx Descriptor List Address<br>(DMA_CH1_TxDesc_List_Address)|32|RW|0000_0000h|
|119Ch|DMA Channel 1 Rx Descriptor List Address<br>(DMA_CH1_RxDesc_List_Address)|32|RW|0000_0000h|
|11A0h|DMA Channel 1 Tx Descriptor Tail Pointer<br>(DMA_CH1_TxDesc_Tail_Pointer)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2967 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|11A8h|DMA Channel 1 Rx Descriptor Tail Pointer<br>(DMA_CH1_RxDesc_Tail_Pointer)|32|RW|0000_0000h|
|11ACh|DMA Channel 1 Tx Descriptor Ring Length<br>(DMA_CH1_TxDesc_Ring_Length)|32|RW|0000_0000h|
|11B0h|DMA Channel 1 Rx Descriptor Ring Length<br>(DMA_CH1_RxDesc_Ring_Length)|32|RW|0000_0000h|
|11B4h|DMA Channel 1 Interrupt Enable (DMA_CH1_Interrupt_Enable)|32|RW|0000_0000h|
|11B8h|DMA Channel 1 Rx Interrupt Watchdog Timer<br>(DMA_CH1_Rx_Interrupt_Watchdog_Timer)|32|RW|0000_0000h|
|11BCh|DMA Channel 1 Slot Function Control Status<br>(DMA_CH1_Slot_Function_Control_Status)|32|RW|0000_07C0h|
|11C4h|DMA Channel 1 Current Application Transmit Descriptor<br>(DMA_CH1_Current_App_TxDesc)|32|RO|0000_0000h|
|11CCh|DMA Channel 1 Current Application Receive Descriptor<br>(DMA_CH1_Current_App_RxDesc)|32|RO|0000_0000h|
|11D4h|DMA Channel 1 Current Application Transmit Buffer<br>(DMA_CH1_Current_App_TxBuffer)|32|RO|0000_0000h|
|11DCh|DMA Channel 1 Current Application Receive Buffer<br>(DMA_CH1_Current_App_RxBuffer)|32|RO|0000_0000h|
|11E0h|DMA Channel 1 Status (DMA_CH1_Status)|32|RW|0000_0000h|
|11E4h|DMA Channel 1 Miss Frame Counter (DMA_CH1_Miss_Frame_Cnt)|32|RO|0000_0000h|
|11E8h|DMA Channel 1 Rx Parser Accept Count<br>(DMA_CH1_RXP_Accept_Cnt)|32|RO|0000_0000h|
|11ECh|DMA Channel 1 Rx ERI Count (DMA_CH1_RX_ERI_Cnt)|32|RO|0000_0000h|



### 74.7.2 MAC Configuration (MAC_Configuration) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Configuration|0h|



Function Establishes MAC's operating mode. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2968 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table 492. Packet length based on CST and ACS bits 

|Received packet length|CST|ACS|FCS stripping done|
|---|---|---|---|
|<1536|—|0|No|
||—|1|Yes (for Ethernet packets)|
|>=1536|0|—|No|
||1|—|Yes (for Type packets)|
|<1536|—|0|No|
||—|1|Yes (for Ethernet packets)|



##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-2969-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserv GPSL Reserv<br>SARC  IPC  IPG  S2KP  CST  ACS  WD  JD  JE<br>W ed  CE  ed<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R PS<br>ECRS Reserv<br>FES  DM  LM  DO  DCRS  DR  BL  DC  PRELEN  TE  RE<br>W FD  ed<br>Reset 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31<br>—|Reserved|
|30-28|Source Address Insertion Or Replacement Control|
|SARC|Controls the source address insertion or replacement for all the transmitted packets.<br>Bit 30 of this field specifies which MAC Address register (0 or 1) is used for source address insertion or<br>replacement based on the values of bits [29:28]:<br>• 2'b0x: The mti_sa_ctrl_i and ati_sa_ctrl_i input signals control the SA field generation.<br>• 2'b10: If bit 30 = 0, MAC inserts the content of the MAC Address 0 registers in the SA field of all the<br>transmitted packets. If bit 30 = 1 and the Enable MAC Address Register 1 option is selected while<br>configuring the core, MAC inserts the content of the MAC Address 1 registers in the SA field of all<br>the transmitted packets.<br>• 2'b11: If bit 30 = 0, MAC replaces the content of the MAC Address 0 registers in the SA field of all<br>the transmitted packets. If bit 30 = 1 and the MAC Address Register 1 is enabled, MAC replaces the<br>content of the MAC Address 1 registers in the SA field of all the transmitted packets.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2969 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function<br>Changes to this field take effect only on the start of a packet. If you write to the field when<br>a packet is being transmitted, only the subsequent packet can use the updated value. This<br>means that the current packet does not use the updated value.<br>~~NOTE~~<br>000b - mti_sa_ctrl_i and ati_sa_ctrl_i input signals control the SA field generation<br>010b - Contents of are inserted in the SA field<br>011b - Contents of replace the SA field<br>110b - Contents of are inserted in the SA field<br>111b - Contents of replace the SA field|
|---|---|
|27<br>IPC|Checksum Offload<br>Indicates the status of IP header or payload checksum checking.<br>If this field is 1, the field enables IPv4 header checksum checking and IPv4 or IPv6 TCP, UDP, or ICMP<br>payload checksum checking. When the field becomes 0, the COE function in the receiver is disabled.<br>The Layer 3 and Layer 4 packet filter and enable split header features automatically select the IPC full<br>checksum offload engine on the receive side. When any of these features are enabled, you must write 1 to<br>this field.<br>0b - Disabled<br>1b - Enabled|
|26-24<br>IPG|Inter-Packet Gap<br>Controls the minimum IPG between packets during transmission.<br>The range of minimum IPG is valid in Full-Duplex mode, and in this mode, the minimum IPG can be<br>configured only for 64-bit times (IPG = 100). Lower values are not considered.<br>When a JAM pattern is being transmitted because of backpressure activation, MAC does not consider the<br>minimum IPG.<br>This function (IPG less than 96-bit times) is valid only whenMAC_Ext_Configuration[EIPGEN]is 0. If this<br>field is 1, the minimum IPG (greater than 96-bit times) is controlled according to the field's description.<br>000b - 96-bit times IPG<br>001b - 88-bit times IPG<br>010b - 80-bit times IPG<br>011b - 72-bit times IPG<br>100b - 64-bit times IPG<br>101b - 56-bit times IPG<br>110b - 48-bit times IPG<br>111b - 40-bit times IPG|
|23|Giant Packet Size Limit Control Enable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2970 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field<br>GPSLCE|Function<br>Enables and disables giant packet size limit control.<br>If this field = 1, MAC considers the value ofMAC_Ext_Configuration[GPSL]to declare a received packet as<br>a giant packet. This field must be programmed to have a size of more than 1,518 bytes. Otherwise, MAC<br>considers 1,518 bytes as the giant packet limit.<br>When this field becomes 0, MAC considers the received packet as a giant packet if its size is greater than<br>1,518 bytes (1522 bytes for a tagged packet).<br>The WD, JE, and S2KP fields have a higher precedence over this field, which means MAC considers a<br>received packet as a giant packet when its size is greater than 9,018 bytes (9,022 bytes for a tagged packet)<br>with JE = 1 and the size of the jumbo packet greater than 2,000 bytes and S2KP = 1. If the WD field is 1,<br>the field terminates the received packet if it reaches the watchdog limit. Therefore, the programmed giant<br>packet limit must be less than the watchdog limit to get the giant packet status.<br>0b - Disabled<br>1b - Enabled|
|---|---|
|22<br>S2KP|IEEE 802.3 Support For 2K Packets<br>Indicates the status of IEEE 802.3 support for 2K packets.<br>If this field is 1, MAC considers all the packets with up to 2,000-byte length as normal. When the JE field is<br>not 1, MAC considers all the received packets of size more than 2K bytes as giant packets.<br>When this field becomes 0 and the JE field is not 1, MAC considers all the received packets of size more<br>than 1,518 bytes (1,522 bytes for tagged) as giant packets. For more information about how the setting of<br>this field and the JE field impacts the giant packet status, see this status based on the S2KP and JE fields.<br>If the JE field is 1, writing 1 to the S2KP field has no effect on the giant packet status.<br>0b - Disabled<br>1b - Enabled|
|21<br>CST|CRC Stripping For Type Packets<br>Indicates the status of CRC stripping for Type packets.<br>If this field is 1, the last four bytes (FCS) of all the Ether-type packets are stripped and dropped before<br>forwarding the packet to the application.<br>This field is valid only when the receive packet size is more than or equal to 1536 bytes.<br>For information about how the settings of this field and the ACS field impact the packet length, seeMAC<br>Configuration (MAC_Configuration).<br>0b - Disabled<br>1b - Enabled|
|20<br>ACS|Automatic Pad Or CRC Stripping<br>Indicates the status of automatic pad or CRC stripping.<br>If this field is 1, MAC strips the pad or the FCS field on the incoming packets only if the size of the packets is<br>less than 1,536 bytes. All the received packets with a size greater than or equal to 1,536 bytes are passed<br>to the application without stripping the pad or the FCS field.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2971 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||When this field becomes 0, MAC passes all the incoming packets to the application, without<br>any modification.<br>For information about how the settings of this field and the CST field impact the packet length, seeMAC<br>Configuration (MAC_Configuration).<br>0b - Disabled<br>1b - Enabled|
|19<br>WD|Watchdog Disable<br>Indicates the status of watchdog.<br>If this field is 1, MAC disables the watchdog timer on the receiver. MAC can receive packets of up to<br>16,383 bytes.<br>When this field becomes 0, MAC does not allow more than 2,048 bytes (10,240 if the JE field = 1) of the<br>packet being received. MAC cuts off bytes received after 2,048.<br>0b - Enabled<br>1b - Disabled|
|18<br>—|Reserved|
|17<br>JD|Jabber Disable<br>Indicates the status of jabber.<br>If this field is 1, MAC disables the jabber timer on the transmitter. It can transfer packets of up to<br>16,383 bytes.<br>If this field is 0 and the application sends more than 2,048 bytes of data (10,240 if the JE field = 1) during<br>transmission, MAC does not send the rest of the bytes in that packet.<br>0b - Enabled<br>1b - Disabled|
|16<br>JE|Jumbo Packet Enable<br>Indicates the status of jumbo packets.<br>If this field is 1, MAC allows jumbo packets of 9,018 bytes (9,022 bytes for VLAN-tagged packets) without<br>reporting a giant packet error in the receive packet status.<br>0b - Disabled<br>1b - Enabled|
|15<br>PS|Port Select<br>Selects the Ethernet line speed.<br>This field, along with the FES field, selects the exact line speed. In the 10/100 Mbit/s-only (always 1) or 1000<br>Mbit/s-only (always 0) configurations, this field is read-only (RO) with an appropriate value. By default, with<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2972 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||10/100/1000 Mbit/s configurations, this field is read-write (R/W). The mac_speed_o[1] signal reflects the<br>value of this field.<br>0b - For 1000 or 2500 Mbit/s operations<br>1b - For 10 or 100 Mbit/s operations|
|14<br>FES|Speed<br>Indicates the speed.<br>This field selects the speed mode.<br>The mac_speed_o[0] signal indicates the value of this field.<br>0b - 10 Mbit/s if PS = 1 and 1 Gbps if PS = 0<br>1b - 100 Mbit/s if PS = 1 and 2.5 Gbps if PS = 0|
|13<br>DM|Duplex Mode<br>Indicates the mode in which MAC operates.<br>If this field is 1, MAC operates in Full-Duplex mode in which it can transmit and receive simultaneously. The<br>field can only be read, with 1 as its default value, in full-duplex-only configurations.<br>0b - Half-duplex mode<br>1b - Full-duplex mode|
|12|Loopback Mode|
|LM|Indicates the status of Loopback mode<br>If this field is 1, MAC operates in Loopback mode at GMII or MII. This mode requires the (G)MII Rx clock<br>input (clk_rx_i) signal to function properly because the transmit clock is not internally looped back.<br>0b - Disabled<br>1b - Enabled|
|11|Enable Carrier Sense In Full-Duplex Mode|
|ECRSFD|Indicates whether ECRSFD is enabled or disabled.<br>If this field is 1, the MAC transmitter checks the CRS signal before packet transmission in Full-Duplex mode.<br>MAC starts transmitting only when the CRS signal is low.<br>If this field becomes 0, the MAC transmitter ignores the status of the CRS signal.<br>0b - Disabled<br>1b - Enabled|
|10|Disable Receive Own|
|DO|Enables or disables receive own.<br>If this field is 1, MAC disables the reception of packets when the gmii_txen_o signal asserts in Half-Duplex<br>mode. When the field is 0, MAC receives all the packets that PHY sent.<br>This field is not applicable in Full-Duplex mode.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2973 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Enabled<br>1b - Disabled|
|9<br>DCRS|Disable Carrier Sense During Transmission<br>Enables or disables carrier sense during transmission.<br>If this field is 1, the MAC transmitter ignores the (G)MII CRS signal during packet transmission in Half-Duplex<br>mode. As a result, no errors generate because of loss of carrier or no carrier during transmission.<br>When this field becomes 0, the MAC transmitter generates errors because of carrier sense. MAC can even<br>abort the transmission.<br>0b - Enabled<br>1b - Disabled|
|8<br>DR|Disable Retry<br>Enables or disables retry attempts.<br>If this field is 1, MAC attempts only one transmission. When a collision occurs on GMII or MII, MAC ignores<br>the current packet transmission and reports a packet abort with excessive collision errors in the transmit<br>packet status.<br>If this field becomes 0, MAC retries based on the settings of the BL field of this register.<br>The settings of this field apply only in Half-Duplex mode.<br>0b - Enabled<br>1b - Disabled|
|7<br>—|Reserved|
|6-5<br>BL|Back-Off Limit<br>Determines the random integer number (r) of slot time delays (4,096 bit times for 1000/2500 Mbit/s; 512<br>bit times for 10/100 Mbit/s) for which MAC waits before rescheduling a transmission attempt during retry<br>attempts after a collision.<br>• n = retransmission attempt<br>• r = random integer that takes the value in the range 0 <= r < 2^k<br>This field is applicable only in Half-Duplex mode.<br>00b - k = min(n,10)<br>01b - k = min(n,8)<br>10b - k = min(n,4)<br>11b - k = min(n,1)|
|4|Deferral Check|
|DC|Indicates the status of the deferral check function.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2974 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function<br>If this field is 1, the deferral check function is enabled in MAC, which issues a packet abort status,<br>withTx_Excessive_Deferral_Error[TXEXSDEF]= 1 in the transmit packet status, when the transmit state<br>machine is deferred for more than 24,288 bit times in 10 Mbit/s or 100 Mbit/s mode.<br>If MAC is configured for a 1000/2500 Mbit/s operation, the threshold for deferral is 155,680 bit times. Deferral<br>begins when the transmitter is ready to transmit, but it is prevented because of an active carrier sense signal<br>(CRS) on GMII or MII.<br>The defer time is not cumulative. For example, if the transmitter defers for 10,000 bit times because the CRS<br>signal is active, and then the CRS signal becomes inactive, the transmitter transmits and collision happens.<br>Because of this collision, the transmitter needs to back off and then defer again after back off completion.<br>In such a scenario, the deferral timer resets to 0 and restarts.<br>When this field becomes 0, the deferral check function disables and MAC defers until the CRS signal<br>becomes inactive.<br>This field is applicable only in Half-Duplex mode.<br>0b - Disabled<br>1b - Enabled|
|---|---|
|3-2<br>PRELEN|Preamble Length for Transmit Packets<br>Controls the number of preamble bytes that are added to the beginning of every transmit packet.<br>Preamble reduction occurs only when MAC operates in Full-Duplex mode.<br>00b - 7 bytes<br>01b - 5 bytes<br>10b - 3 bytes<br>11b - Reserved|
|1<br>TE|Transmitter Enable<br>Indicates the status of the transmitter.<br>• If this field is 1, the MAC transmit state machine is enabled for transmission on GMII or MII.<br>• When the field becomes 0, the MAC transmit state machine is disabled after it completes the<br>transmission of the current packet. The transmit state machine does not transmit any more packets.<br>0b - Disabled<br>1b - Enabled|
|0<br>RE|Receiver Enable<br>Indicates the status of the receiver.<br>If this field is 1, MAC's receive state machine is enabled for receiving packets fromGMIIor MII. When this<br>field becomes 0, the MAC receive state machine is disabled after it completes the reception of the current<br>packet. The receive state machine does not receive any more packets from GMII or MII.<br>0b - Disabled<br>1b - Enabled|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2975 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

### 74.7.3 MAC Extended Configuration (MAC_Ext_Configuration) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Ext_Configuration|4h|



##### Function 

Establishes MAC's operating mode. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|Reserv<br>ed|Reserv<br>ed|||EIPG|||EIPGE<br>N|Reserv<br>ed||Reserved||PDC|USP|SPEN|DCRC<br>C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|Rese|rved|||||||GP|SL|||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|Reserved|
|—||
|30|Reserved|
|—||
|29-25|Extended Inter-Packet Gap|
|EIPG|Indicates the value of the extended inter-packet gap.<br>The value of this field is applicable when EIPGEN = 1. The most-significant bits of this field, along with those<br>ofMAC_Configuration[IPG], render the minimum IPG greater than 96-bit times in steps of 8-bit times.|
||8'h00: 104-bit times|
||8'h01: 112-bit times<br>8'h02: 120-bit times<br>-----------------------<br>8'hFF: 2144-bit times|
|24|Extended Inter-Packet Gap Enable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2976 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field<br>EIPGEN|Function<br>Indicates the status of the extended inter-packet gap.<br>• If this field is 1, MAC interprets the EIPG field of this register and the IPG field ofMAC Configuration<br>(MAC_Configuration)together as minimum IPG greater than 96-bit times in steps of 8-bit times.<br>• If this field is 0, MAC ignores the EIPG field of this regsiter and interprets the IPG field ofMAC<br>Configuration (MAC_Configuration)as minimum IPG less than or equal to 96-bit times in steps of<br>8-bit times.<br>You must enable the extended inter-packet gap feature when operating in Full-Duplex<br>mode only. There could be undesirable effects on the back-pressure function and frame<br>transmission if the feature is enabled in Half-Duplex mode.<br>~~NOTE~~<br>0b - Disabled<br>1b - Enabled|
|---|---|
|23<br>—|Reserved|
|22-20<br>—|Reserved|
|19<br>PDC|Packet Duplication Control<br>Indicates the packet duplication control status.<br>• If this field is 1, the received packet with multicast or broadcast destination address is routed to<br>multiple receive DMA channels.MAC_Address0_High[DCS]identifies the receive DMA channels<br>(corresponding to the MAC Address register) that match the multicast or broadcast destination<br>addresses in the received packet. The DCS field is interpreted to be a one-hot value, each bit<br>corresponding to the receive DMA channel.<br>• If this field is 0, the received packet routes to a single receive DMA channel.<br>MAC_Address0_High[DCS]identifies the receive DMA channel corresponding to the MAC Address<br>register that matches the destination address in the received packet. The DCS field is interpreted as<br>a binary value.<br>0b - Disabled<br>1b - Enabled|
|18<br>USP|Unicast Slow Protocol Packet Detect<br>Indicates the status of unicast slow-protocol packet detection.<br>• If this field is 1, MAC detects the slow-protocol packets with unicast address of the station specified<br>inMAC Address 0 High (MAC_Address0_High)andMAC Address 0 Low (MAC_Address0_Low).<br>MAC also detects the slow-protocol packets with the slow-protocol multicast address (01-80-<br>C2-00-00-02).<br>• If this field is 0, MAC detects only slow-protocol packets with the slow protocol multicast address<br>specified in IEEE 802.3-2015, section 5.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2977 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Disabled<br>1b - Enabled|
|17<br>SPEN|Slow Protocol Detection Enable<br>Enables or disables slow protocol detection.<br>• If this field is 0, EMAC forwards all error-free, slow-protocol packets to the application. EMAC<br>considers such packets as normal-type packets.<br>• If this field is 1, EMAC processes the slow-protocol packets (Ether type 8809h) and provides the<br>slow protocol sub-type and code fields in receive status.<br>0b - Disabled<br>1b - Enabled|
|16<br>DCRCC|Disable CRC Checking For Received Packets<br>Indicates the status of CRC checking.<br>If this field is 1, MAC receiver does not check the CRC field in the received packets. When this field becomes<br>0, the MAC receiver always checks the CRC field in the received packets.<br>0b - Enabled<br>1b - Disabled|
|15-14<br>—|Reserved|
|13-0<br>GPSL|Giant Packet Size Limit<br>Declares the status of a packet based on its size.<br>If the received packet size (in bytes) is greater than the value programmed in this field, MAC declares the<br>received packet as a giant packet. The value programmed in this field must be greater than or equal to 1,518<br>bytes. Also, any other programmed value is considered as 1,518 bytes.<br>For VLAN-tagged packets, MAC adds 4 bytes to the programmed value. IfMAC_VLAN_Tag_Ctrl[EDVLP]<br>= 1, MAC adds 8 bytes to the programmed value for double VLAN-tagged packets.<br>The value of GPSL is valid ifMAC_Configuration[GPSLCE]= 1.|



### 74.7.4 MAC Packet Filter (MAC_Packet_Filter) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Packet_Filter|8h|



##### Function 

Contains the filter controls for receiving packets. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2978 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Some of the controls from this register go to MAC's address check block that performs the first level of address filtering. The second level of filtering is performed on the incoming packet based on other controls such as pass bad packets and pass control packets. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-2979-04.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>RA  Reserved  DNTU  IPFE  Reserved  VTFE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>Reserved  HPF  SAF  SAIF  PCF  DBF  PM  DAIF  HMC  HUC  PR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Receive All|
|RA|Indicates whether the received packets are enabled or disabled.<br>• If this field is 1, the MAC Receiver module passes all the received packets to the application,<br>irrespective of their passing the address filter. The result (pass or fail) of the SA or DA filtering is<br>updated in the corresponding field of the receive status word.<br>• If this field is 0, the module passes only those packets to the application that pass the SA or DA<br>address filter.<br>0b - Receive All is disabled<br>1b - Receive All is enabled|
|30-22<br>—|Reserved|
|21<br>DNTU|Drop Non-TCP/UDP Over IP Packets<br>Indicates whether MAC drops or forwards non-TCP/UDP protocols over IP packets.<br>• If this field is 1, MAC drops these protocols over IP packets. MAC forwards only those packets that<br>the layer 4 filter processes.<br>• If this field is 0, MAC forwards all these protocols over IP packets.<br>0b - Forwards<br>1b - Drops|
|20<br>IPFE|Layer 3 and Layer 4 Filter Enable<br>Indicates the status of layer 3 and layer 4 filters.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2979 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function<br>• If this field is 1, MAC drops packets that do not match the enabled layer 3 and layer 4 filters. If these<br>two filters are not enabled for matching, this field does not have any effect.<br>• If this field is 0, MAC forwards all the packets irrespective of the match status of the layer 3 and layer<br>4 fields.<br>0b - Disabled<br>1b - Enabled|
|---|---|
|19-17<br>—|Reserved|
|16<br>VTFE|VLAN Tag Filter Enable<br>Indicates the status of VLAN tag filter.<br>• If this field is 1, MAC drops the VLAN-tagged packets that do not match the VLAN tag.<br>• If this field is 0, MAC forwards all the packets irrespective of the match status of the VLAN tag.<br>0b - Disabled<br>1b - Enabled|
|15-11<br>—|Reserved|
|10<br>HPF|Hash Or Perfect Filter<br>Indicates the status of hash or perfect filter.<br>• If this field is 1, the address filter passes a packet if it matches either perfect filtering or hash filtering<br>as defined by the HMC or HUC fields of this register.<br>• If this field is 0 and HUC = 1 or HMC = 1, the packet passes only if it matches the hash filter.<br>0b - Disabled<br>1b - Enabled|
|9<br>SAF|Source Address Filter Enable<br>Indicates the status of SA filtering.<br>• If this field is 1, MAC compares the SA field of the received packets with the values programmed in<br>the enabled SA registers. If the comparison fails, MAC drops the packet.<br>• When this field becomes 0, MAC forwards the received packet to the application with an updated<br>field value, depending on the SA address comparison.<br>According to the IEEE specification, bit 47 of the SA field is reserved. However, MAC<br>compares all the 48 bits. You must consider this when programming the MAC address<br>registers for SA.<br>~~NOTE~~|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2980 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Disabled<br>1b - Enabled|
|8|SA Inverse Filtering|
|SAIF|Indicates the status of SA inverse filtering.<br>• If this field is 1, the address check block operates in the inverse filtering mode for SA address<br>comparison. If the SA of a packet matches the values programmed in the SA registers, it is marked<br>as failing the SA address filter.<br>• If this field becomes 0 and the SA of a packet does not match the values programmed in the SA<br>registers, the SA is marked as failing the SA address filter.<br>0b - Disabled<br>1b - Enabled|
|7-6|Pass Control Packets|
|PCF|Controls the forwarding of all the control packets (including unicast and multicast pause packets).<br>00b - MAC filters all the control packets from reaching the application<br>01b - MAC forwards all the control packets, except pause packets, to the application even if they<br>fail the address filter<br>10b - MAC forwards all the control packets to the application even if they fail the address filter<br>11b - MAC forwards all the control packets that pass the address filter|
|5|Disable Broadcast Packets|
|DBF|Enables or disables broadcast packets.<br>• If this field is 1, AFM blocks all the incoming broadcast packets. In addition, it overrides all the other<br>filter settings.<br>• If this field is 0, AFM passes all the received broadcast packets.<br>0b - Enabled<br>1b - Disabled|
|4<br>PM|Pass All Multicast<br>Enables or disables the passing of received packets.<br>• If this field is 1, it indicates that all the received packets with a multicast destination address (first bit<br>in the destination address field is 1) are passed.<br>• If this field is 0, filtering of multicast packets depends on the settings of the HMC field.<br>0b - Disabled|
||1b - Enabled|
|3|DA Inverse Filtering|
|DAIF|Indicates the status of DA inverse filtering.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2981 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||• If this field is 1, the Address Check block operates in Inverse Filtering mode for the DA address<br>comparison of both unicast and multicast packets.<br>• If this field is 0, normal filtering of packets is performed.<br>0b - Disabled<br>1b - Enabled|
|2<br>HMC|Hash Multicast<br>Indicates the status of hast multicast.<br>• If this field is 1, MAC performs the destination address filtering of received multicast packets<br>according to the hash table.<br>• If this field is 0, MAC performs the perfect destination address filtering for multicast packets, that is, it<br>compares the DA field with the values programmed in DA registers.<br>0b - Disabled<br>1b - Enabled|
|1<br>HUC|Hash Unicast<br>Indicates the status of hash unicast.<br>• If this field is 1, MAC performs the destination address filtering of unicast packets according to the<br>hash table.<br>• When this field becomes 0, MAC performs a perfect destination address filtering for unicast packets,<br>that is, it compares the DA field with the values you program in the MAC Address registers.<br>0b - Disabled<br>1b - Enabled|
|0|Promiscuous Mode|
|PR|Indicates the status of Promiscuous mode.<br>If this field is 1, the address filtering module passes all the incoming packets irrespective of the destination<br>or source address. MAC clears the SA or DA filter fail status fields of the receive status word when PR = 1.<br>0b - Disabled<br>1b - Enabled|



### 74.7.5 MAC Watchdog Timeout (MAC_Watchdog_Timeout) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Watchdog_Timeou|Ch|
|t||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2982 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Function 

Controls the watchdog timeout for received packets. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18||17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||Rese|rved|||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0||0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2||1|0|
|R<br>W||||Reserved||||PWE||Rese|rved|||W|TO|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0||0|0|



##### Fields 

|Field|Function|
|---|---|
|31-9|Reserved|
|—||
|8|Programmable Watchdog Enable|
|PWE|Indicates the status of programmable watchdog.<br>• If this field is 1 andMAC_Configuration[WD]is 0, the WTO field of this register is used as watchdog<br>timeout for a received packet.<br>• If this field is 0,MAC_Configuration[WD]andMAC_Configuration[JE]control the watchdog timeout<br>for a received packet.<br>0b - Disabled<br>1b - Enabled|
|7-4<br>—|Reserved|
|3-0|Watchdog Timeout|
|WTO|Indicates the size of watchdog timer.<br>If PWE = 1 andMAC_Configuration[WD]= 0, this field is used as watchdog timeout for a received packet.<br>If the length of a received packet exceeds the value of this field, the packet terminates as an error packet.<br>If PWE = 1, the value in this field must exceed 1,522 (05F2h). Otherwise, the IEEE<br>802.3-specified valid tagged packets are declared as error packets and dropped.<br>~~NOTE~~|
||0000b - 2 KB|
||0001b - 3 KB|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2983 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Field|Function||
|---|---|---|
||0010b -|4 KB|
||0011b -|5 KB|
||0100b -|6 KB|
||0101b -|7 KB|
||0110b -|8 KB|
||0111b -|9 KB|
||1000b -|10 KB|
||1001b -|11 KB|
||1010b -|12 KB|
||1011b -|13 KB|
||1100b -|14 KB|
||1101b -|15 KB|
||1110b -|16383 bytes|
||1111b -|Reserved|



### 74.7.6 MAC Hash Table First 32 Bits (MAC_Hash_Table_Reg0) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Hash_Table_Reg0|10h|



##### Function 

Contains the first 32 bits of the hash table, when the total width of the hash table is 128 bits or 256 bits. 

The hash table is used for group address filtering, for which the content of the destination address in the incoming packet is passed through the CRC logic and the bits of Receive CRC Error Packets (Rx_CRC_Error_Packets) are used to index the contents of the hash table as follows: 

- 6 bits when you have a 64-bit hash 

- 7 bits when you have a 128-bit hash 

- 8 bits when you have a 256-bit hash 

The most-significant bits determine the Hash Table register to be used, and the least-significant 5 bits determine the bit within the register. For example, a hash value of 10_0000b (in 64-bit hash) selects bit 0 of MAC Hash Table Second 32 Bits (MAC_Hash_Table_Reg1). 

Perform these steps to calculate the hash value of the destination address: 

1. Calculate the 32-bit CRC for DA (see section 3.2.8 in IEEE 802.3 for the steps to calculate CRC32). 

2. Perform bit-wise reversal for the value obtained in step 1. 

3. Use the upper 6, 7, or 8 bits from the value obtained in step 2. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2984 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

If this field is 1, the packet is accepted. Otherwise, it is rejected. If MAC_Packet_Filter[PM] = 1, all multicast packets are accepted regardless of the multicast hash values. 

If this register is configured to be double-synchronized with the (G)MII clock domain, the synchronization is triggered only when bits [31:24] (in Little-Endian mode) or bits [7:0] (in Big-Endian mode) of the Hash Table registers are written to. 

If double-synchronization is enabled, consecutive writes to this register must be performed after at least four clock cycles in the destination clock domain. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-2985-06.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>HT31T0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>HT31T0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|MAC Hash Table First 32 Bits|
|HT31T0|Contains the first 32 bits [31:0] of the hash table.|



### 74.7.7 MAC Hash Table Second 32 Bits (MAC_Hash_Table_Reg1) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Hash_Table_Reg1|14h|



##### Function 

Contains the second 32 bits of the hash table, when the width of the hash table is 128 or 256 bits. 

The hash table is used for group address filtering, for which the content of the destination address in the incoming packet is passed through the CRC logic and the bits of Receive CRC Error Packets (Rx_CRC_Error_Packets) are used to index the contents of the hash table as follows: 

- 6 bits when you have a 64-bit hash 

- 7 bits when you have a 128-bit hash 

- 8 bits when you have a 256-bit hash 

The most-significant bits determine the Hash Table register to be used, and the least-significant 5 bits determine the bit within the register. For example, a hash value of 10_0000b (in 64-bit hash) selects bit 0 of MAC Hash Table Second 32 Bits (MAC_Hash_Table_Reg1). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2985 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Perform these steps to calculate the hash value of the destination address: 

1. Calculate the 32-bit CRC for DA (see section 3.2.8 in IEEE 802.3 for the steps to calculate CRC32). 

2. Perform bit-wise reversal for the value obtained in step 1. 

3. Take the upper 6, 7, or 8 bits from the value obtained in step 2. 

If the corresponding bit value of this register is 1'b1, the packet is accepted. Otherwise, it is rejected. If MAC_Packet_Filter[PM] = 1, all multicast packets are accepted regardless of the multicast hash values. 

If this register is configured to be double-synchronized with the (G)MII clock domain, the synchronization is triggered only when bits [31:24] (in Little-Endian mode) or bits [7:0] (in Big-Endian mode) of the Hash Table registers are written to. 

If double-synchronization is enabled, consecutive writes to this register must be performed after at least four clock cycles in the destination clock domain. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-2986-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>HT63T32<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>HT63T32<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|MAC Hash Table Second 32 Bits|
|HT63T32|Contains the second 32 bits [63:32] of the hash table.|



### 74.7.8 MAC VLAN Tag (MAC_VLAN_Tag) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag|50h|



##### Function 

Identifies the IEEE 802.1Q VLAN type packets. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2986 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|EIVLR<br>XS|Reserv<br>ed|EIVL|S|ERIVL<br>T|EDVL<br>P|VTHM|EVLR<br>XS|Reserv<br>ed|EV|LS|DOVL<br>TC|ERSV<br>LM|ESVL|VTIM|ETV|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||V|L||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|Enable Inner VLAN Tag In Receive Status|
|EIVLRXS|Indicates whether the inner VLAN tag in receive status is enabled or disabled.<br>• If this field is 1, MAC provides the inner VLAN tag in the receive status.<br>• If this field is 0, MAC does not provide the inner VLAN tag in the receive status.<br>0b - Disabled<br>1b - Enabled|
|30<br>—|Reserved|
|29-28<br>EIVLS|Enable Inner VLAN Tag Stripping<br>Indicates the stripping operation on the inner VLAN tag in a received packet. The field enables or disables<br>inner VLAN tag stripping on receive.<br>00b - Do not strip<br>01b - Strip if VLAN filter passes<br>10b - Strip if VLAN filter fails<br>11b - Always strip|
|27<br>ERIVLT|Enable Inner VLAN Tag Comparison<br>Enables or disables the inner VLAN tag.<br>• If ERIVLT =VTHM=EDVLP= 1, the EMAC receiver enables the VLAN hash filtering operation on<br>the inner VLAN tag (if present).<br>• If ERIVLT = 0 andVTHM= 1, the EMAC receiver enables the VLAN hash filtering operation on<br>the outer VLAN tag (if present).ERSVLMandDOVLTCdetermine which VLAN type is enabled for<br>filtering.<br>0b - Disabled<br>1b - Enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2987 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|26<br>EDVLP|Enable Double VLAN Processing<br>Enables or disables double VLAN processing.<br>• If this field is 1, MAC enables processing of up to two VLAN tags on transmit and receive (if present).<br>• If this field is 0, MAC enables processing of up to one VLAN tag on transmit and receive (if present).<br>0b - Disabled<br>1b - Enabled|
|25<br>VTHM|VLAN Tag Hash Table Match<br>Indicates the status of VLAN tag hash table match.<br>• If this field is 1, the most-significant four bits of CRC-32 of VLAN tag are used to index the content of<br>MAC VLAN Hash Table (MAC_VLAN_Hash_Table). SeeVLAN filteringfor details.<br>• IfMAC_VLAN_Hash_Table[VLHT]= 1, corresponding to the index, it indicates that the Ethernet<br>packet matches the VLAN hash table. SeeVLAN filteringfor details.<br>• If ETV = 1, the CRC of the 12-bit VLAN identifier (VID) is used for comparison. When the ETV field<br>becomes 0, the CRC of the 16-bit VLAN tag is used for comparison.<br>• If VTHM = 1, the VLAN hash match operation is not performed.<br>0b - Disabled<br>1b - Enabled|
|24<br>EVLRXS|Enable VLAN Tag In Receive Status<br>Indicates whether the VLAN tag in receive status is enabled.<br>• If this field is 1, MAC provides the outer VLAN tag in the receive status.<br>• If this field is 0, MAC does not provide the outer VLAN tag in receive status.<br>0b - Disabled<br>1b - Enabled|
|23<br>—|Reserved|
|22-21<br>EVLS|Enable VLAN Tag Stripping<br>Indicates the stripping operation on the outer VLAN tag in received packets. The field enables or disables<br>VLAN tag stripping on receive.<br>00b - Do not strip<br>01b - Strip if VLAN filter passes<br>10b - Strip if VLAN filter fails<br>11b - Always strip|
|20|Disable VLAN Type Check|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2988 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|DOVLTC|Enables or disables VLAN type check for VLAN hash filtering.<br>• If this field is 1, the MAC VLAN hash filter matches or filters the VLAN tag that the ERIVLT field<br>specifies only when the VLAN tag type is similar to the one that the ERSVLM field specifies.<br>• If this field is 0, the MAC VLAN hash filter does not check whether the VLAN tag that the ERIVLT<br>field specifies is of type S-VLAN or C-VLAN.<br>• The VLAN filter is bypassed when VLAN type of received packet do not match the programmed<br>VLAN type in the VLAN filter.<br>0b - Enabled<br>1b - Disabled|
|19<br>ERSVLM|Enable Receive S-VLAN Match<br>Enables or disables receive S-VLAN match for VLAN hash filtering.<br>• If this field is 1, the MAC receiver enables VLAN hash filtering or S-VLAN matching (type = 88A8h)<br>packets.<br>• If this field is 0, the MAC receiver enables VLAN hash filtering or matching for C-VLAN (type =<br>8100h) packets.<br>The ERIVLT field determines the VLAN tag position considered for VLAN hash filtering or matching.<br>0b - Disabled<br>1b - Enabled|
|18<br>ESVL|Enable S-VLAN<br>Enables or disables S-VLAN.<br>If this field is 1, the MAC transmitter and receiver consider the S-VLAN packets (type = 88A8h) as valid<br>VLAN-tagged packets.<br>0b - Disabled<br>1b - Enabled|
|17<br>VTIM|VLAN Tag Inverse Match Enable<br>Enables or disables VLAN tag inverse matching.<br>• If this field is 1, it enables the VLAN tag inverse matching. The packets without matching VLAN tag<br>are marked as matched.<br>• If this field is 0, it enables the VLAN tag perfect matching. The packets with matched VLAN tag are<br>marked as matched.<br>0b - Disabled<br>1b - Enabled|
|16<br>ETV|Enable Tag For VLAN<br>Enables or disables 12-bit VLAN tag comparison for VLAN hash filtering.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2989 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||• If this field is 1, a 12-bit VLAN identifier is used for VLAN hash filtering instead of the complete 16-bit<br>VLAN tag. Bits [11:0] of the VLAN tag in the received VLAN-tagged packet are used for hash-based<br>VLAN filtering.<br>• When this field becomes 0, all 16 bits of the 15th and 16th bytes of the received VLAN packet are<br>used for VLAN hash filtering.<br>0b - Disabled<br>1b - Enabled|
|15-0<br>VL|VLAN Tag Identifier for Receive Packets<br>Contains the 802.1Q VLAN tag to identify the VLAN packets.<br>This VLAN tag identifier is compared to the 15th and 16th bytes of the packets being received for<br>VLAN packets.<br>The following list describes the bits of this field:<br>• 15:13 — User priority<br>• 12 — Canonical Format Indicator (CFI) or Drop Eligible Indicator (DEI)<br>• 11:0 — VID field of VLAN tag<br>When ETV = 1, only the VID is used for comparison.<br>When VL = 0, and ETV = 1, MAC does not check the 15th and 16th bytes for VLAN tag comparison and<br>declares all packets with Type field value of 8100h or 88a8h as VLAN packets.|



### 74.7.9 MAC VLAN Tag Control (MAC_VLAN_Tag_Ctrl) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Ctrl|50h|



##### Function 

Is the redefined version of the MAC_VLAN_Tag register. 

This register provides the control and addressing fields required for indirect access to the MAC_VLAN_Tag_Filter registers. It also contains the address offset, command type, and busy bit for CSR access of the MAC VLAN Hash Filter registers. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2990 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Diagram 

|Bits|31|30<br>29<br>28<br>27|26<br>25<br>24|23|22<br>21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|EIVLR<br>XS<br>|Reserv<br>ed<br>EIVLS<br>ERIVL<br>T|EDVL<br>P<br>VTHM<br>EVLR<br>XS|Reserv<br>ed|EVLS|DOVL<br>TC|ERSV<br>LM|ESVL|VTIM|ETV|
|Reset|0|0<br>0<br>0<br>0|0<br>0<br>0|0|0<br>0|0|0|0|0|0|
|Bits|15|14<br>13<br>12<br>11|10<br>9<br>8|7|6<br>5|4|3|2|1|0|
|R<br>W|||Reserved||||OF|S|CT|OB|
|Reset|0|0<br>0<br>0<br>0|0<br>0<br>0|0|0<br>0|0|0|0|0|0|
|Fields<br>|Field|Function|||||||||
|EI|31<br>VLRXS|Enable Inner VLAN Tag I<br>Indicates whether the inn<br>• If this field is 1, MAC<br>• If this field is 0, MAC<br>0b - Disabled<br>1b - Enabled|n Receive Status<br>er VLAN tag in receive<br>provides the inner VLA<br>does not provide the in|status i<br>N tag in<br>ner VLA|s enabled or<br>the receive<br>N tag in the|disabled.<br>status.<br>receive s|tatus.||||
||30<br>—|Reserved|||||||||
|E|29-28<br>IVLS|Enable Inner VLAN Tag S<br>Indicates the stripping op<br>inner VLAN tag stripping<br>00b - Do not strip<br>01b - Strip if VLAN<br>10b - Strip if VLAN<br>11b - Always strip|tripping<br>eration on the inner VL<br>on receive.<br>filter passes<br>filter fails|AN tag i|n a received|packet. T|he field|enable|s or disa|bles|
|E|27<br>RIVLT|Enable Inner VLAN Tag C<br>Enables or disables the in<br>• If ERIVLT =VTHM=<br>the inner VLAN tag (i<br>• If ERIVLT = 0 andVT<br>the outer VLAN tag (i<br>filtering.<br>0b - Disabled<br>1b - Enabled|omparison<br>ner VLAN tag.<br> EDVLP= 1, the EMAC<br>f present).<br>HM= 1, the EMAC rec<br>f present).ERSVLMan|receive<br>eiver e<br>dDOV|r enables th<br>nables the V<br>LTCdetermi|e VLAN h<br>LAN hash<br>ne which|ash filte<br>filtering<br>VLAN ty|ring op<br>opera<br>pe is e|eration o<br>tion on<br>nabled f|n<br>or|



##### Fields 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2991 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|26<br>EDVLP|Enable Double VLAN Processing<br>Enables or disables double VLAN processing.<br>• If this field is 1, MAC enables processing of up to two VLAN tags on transmit and receive (if present).<br>• If this field is 0, MAC enables processing of up to one VLAN tag on transmit and receive (if present).<br>0b - Disabled<br>1b - Enabled|
|25<br>VTHM|VLAN Tag Hash Table Match<br>Indicates the status of VLAN tag hash table match.<br>• If this field is 1, the most-significant four bits of CRC-32 of VLAN tag are used to index the content of<br>MAC VLAN Hash Table (MAC_VLAN_Hash_Table). SeeVLAN filteringfor details.<br>• IfMAC_VLAN_Hash_Table[VLHT]= 1, corresponding to the index, it indicates that the Ethernet<br>packet matches the VLAN hash table. SeeVLAN filteringfor details.<br>• If ETV = 1, the CRC of the 12-bit VLAN identifier (VID) is used for comparison. When the ETV field<br>becomes 0, the CRC of the 16-bit VLAN tag is used for comparison.<br>• If VTHM = 1, the VLAN hash match operation is not performed.<br>0b - Disabled<br>1b - Enabled|
|24<br>EVLRXS|Enable VLAN Tag In Receive Status<br>Indicates whether the VLAN tag in receive status is enabled.<br>• If this field is 1, MAC provides the outer VLAN tag in the receive status.<br>• If this field is 0, MAC does not provide the outer VLAN tag in receive status.<br>0b - Disabled<br>1b - Enabled|
|23<br>—|Reserved|
|22-21<br>EVLS|Enable VLAN Tag Stripping<br>Indicates the stripping operation on the outer VLAN tag in received packets. The field enables or disables<br>VLAN tag stripping on receive.<br>00b - Do not strip<br>01b - Strip if VLAN filter passes<br>10b - Strip if VLAN filter fails<br>11b - Always strip|
|20|Disable VLAN Type Check|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2992 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|DOVLTC|Enables or disables VLAN type check for VLAN hash filtering.<br>• If this field is 1, the MAC VLAN hash filter matches or filters the VLAN tag that the ERIVLT field specifies<br>only when the VLAN tag type is similar to the one that the ERSVLM field specifies.<br>• If this field is 0, the MAC VLAN hash filter does not check whether the VLAN tag that the ERIVLT field<br>specifies is of type S-VLAN or C-VLAN.<br>0b - Enabled<br>1b - Disabled|
|19<br>ERSVLM|Enable Receive S-VLAN Match<br>Enables or disables receive S-VLAN match for VLAN hash filtering.<br>• If this field is 1, the MAC receiver enables VLAN hash filtering or S-VLAN matching (type = 88A8h)<br>packets.<br>• If this field is 0, the MAC receiver enables VLAN hash filtering or matching for C-VLAN (type =<br>8100h) packets.<br>The ERIVLT field determines the VLAN tag position considered for VLAN hash filtering or matching.<br>0b - Disabled<br>1b - Enabled|
|18<br>ESVL|Enable S-VLAN<br>Enables or disables S-VLAN.<br>If this field is 1, the MAC transmitter and receiver consider the S-VLAN packets (type = 88A8h) as valid<br>VLAN-tagged packets.<br>0b - Disabled<br>1b - Enabled|
|17|VLAN Tag Inverse Match Enable|
|VTIM|Enables or disables VLAN tag inverse matching.<br>• If this field is 1, it enables the VLAN tag inverse matching. The packets without matching VLAN tag<br>are marked as matched.<br>• If this field is 0, it enables the VLAN tag perfect matching. The packets with matched VLAN tag are<br>marked as matched.<br>0b - Disabled<br>1b - Enabled|
|16<br>ETV|Enable Tag For VLAN<br>Enables or disables 12-bit VLAN tag comparison for VLAN hash filtering.<br>• If this field is 1, a 12-bit VLAN identifier is used for VLAN hash filtering instead of the complete 16-bit<br>VLAN tag. Bits [11:0] of the VLAN tag in the received VLAN-tagged packet are used for hash-based<br>VLAN filtering.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2993 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-2994-03.png)


<!-- Start of picture text -->
Field Function<br>• When this field becomes 0, all 16 bits of the 15th and 16th bytes of the received VLAN packet are<br>used for VLAN hash filtering.<br>0b - Disabled<br>1b - Enabled<br>15-4 Reserved<br>—<br>3-2 Offset<br>OFS Holds the address offset of the MAC VLAN Tag Filter register that the application tries to access.<br>The width of this field depends on the number of enabled MAC VLAN Tag registers.<br>1 Command Type<br>CT Specifies whether the current register access indicates a read or a write operation. It indicates a read<br>operation if this field is 1 and a write operation when the field is 0.<br>0b - Write operation<br>1b - Read operation<br>0 Operation Busy<br>OB Indicates the operation busy status.<br>• This field becomes 1 to initiate a read or write command for an indirect access to the Per VLAN Tag<br>Filter register.<br>• The field becomes 0 when the read or write command to Per VLAN Tag Filter indirect access<br>register completes. The next indirect register access can be initiated only after the field resets.<br>During a write operation, the field becomes 0 only after the data is written into a<br>MAC_VLAN_Tag_Filter register.<br>During a read operation, the data must be read from MAC VLAN Tag Data (MAC_VLAN_Tag_Data) only<br>after this field becomes 0.<br>0b - Disabled<br>1b - Enabled<br><!-- End of picture text -->

### 74.7.10 MAC VLAN Tag Data (MAC_VLAN_Tag_Data) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Data|54h|



##### Function 

Holds the read and write data for indirect access to the Per VLAN Tag registers. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2994 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

- During read access, this register contains valid read data only after MAC_VLAN_Tag_Ctrl[OB] becomes 0. 

- During write access, this register must become valid before you write 1 to MAC_VLAN_Tag_Ctrl[OB]. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-2995-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R DMAC DMAC ERIVL ERSV DOVL<br>Reserved  Reserved  ETV  VEN<br>W HN  HEN  T  LM  TC<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>VID<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-26|Reserved|
|—||
|25<br>DMACHN|DMA Channel Number<br>Indicates the DMA channel number to which the VLAN-tagged frame is to be routed if it passes the VLAN<br>tag filter programmed using this field.<br>If the routing based on VLAN tag filter is not necessary, this field does not need to be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable<br>Enables or disables the DMA channel number value programmed using the DMACHN field.<br>If this field is 0, the routing does not occur based on the VLAN filter result. The frame is routed on the basis<br>of DA-based DMA channel routing.<br>0b - Disabled<br>1b - Enabled|
|23-21<br>—<br>20<br>ERIVLT|Reserved<br>Enable Inner VLAN Tag<br>Enables or disables inner VLAN tag comparison.<br>• This field is valid only when the double VLAN tag enable of the filter is set.<br>• If this field and the EDVLP field is 1, the MAC receiver enables operation on the inner VLAN tag (if<br>present).<br>• If this field is 0, the MAC receiver enables operation on the outer VLAN tag (if present).|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2995 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Disabled<br>1b - Enabled|
|19<br>ERSVLM|Enable S-VLAN Match<br>Enables or disables S-VLAN match for received frames.<br>This field is valid only when the VLAN tag enable of the filter is set.<br>• If this field is 1, the MAC receiver enables filtering or matching for S-VLAN (type = 88A8h) packets.<br>• If this field is 0, the MAC receiver enables filtering or matching for C-VLAN (type = 8100h) packets.<br>0b - Disabled<br>1b - Enabled|
|18|Disable VLAN Type Comparison|
|DOVLTC|Enables or disables VLAN type comparison.<br>This field is valid only when the VEN field is 1.<br>• If this field is 1, MAC does not check whether the VLAN tag that ERIVLT specifies is of type S-VLAN<br>or C-VLAN.<br>• If this field is 0, MAC filters or matches the VLAN tag that the ERIVLT field specifies only when the<br>VLAN tag type is similar to the one that the ERSVLM field specifies.<br>0b - Enabled<br>1b - Disabled|
|17|VLAN Comparison|
|ETV|Indicates 12-bit or 16-bit VLAN comparison.<br>• This field is valid only when the VEN field is 1.<br>• When the value of this field is 1, a 12-bit VLAN identifier is used for filter and comparison instead of<br>the complete 16-bit VLAN tag. Bits [11:0] of the VLAN tag are compared with the corresponding field<br>in the received VLAN-tagged packet.<br>0b - 16-bit VLAN comparison<br>1b - 12-bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable<br>Enables or disables the VLAN tag.<br>• If this field is 1, MAC compares the VLAN tag of the received packet with the VLAN tag ID.<br>• If this field is 0, no comparison is performed irrespective of the programming of the other fields.<br>0b - Disabled|
||1b - Enabled|
|15-0|VLAN Tag ID|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2996 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|VID|Holds the VLAN tag value that MAC uses for perfect comparison. The field is valid when VEN = 1.|



### 74.7.11 MAC VLAN Tag Filter 0 (MAC_VLAN_Tag_Filter0) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter0|54h|



Function 

Contains VLAN tag filter 0 control information. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||Rese|rved|||DMAC<br>HN|DMAC<br>HEN||Reserved||ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-26|Reserved|
|—||
|25|DMA Channel Number|
|DMACHN|Indicates the DMA channel number to which the VLAN-tagged frame is to be routed if it passes the VLAN<br>tag filter programmed using this field.<br>If the routing based on VLAN tag filter is not necessary, this field does not need to be programmed.|
|24|DMA Channel Number Enable|
|DMACHEN|Enables or disables the DMA channel number value programmed using the DMACHN field.<br>If this field is 0, the routing does not occur based on the VLAN filter result. The frame is routed on the basis<br>of DA-based DMA channel routing.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2997 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Disabled<br>1b - Enabled|
|23-21<br>—|Reserved|
|20<br>ERIVLT|Enable Inner VLAN Tag<br>Enables or disables inner VLAN tag comparison.<br>• This field is valid only when the double VLAN tag enable of the filter is set.<br>• If this field and the EDVLP field is 1, the MAC receiver enables operation on the inner VLAN tag (if<br>present).<br>• If this field is 0, the MAC receiver enables operation on the outer VLAN tag (if present).<br>0b - Disabled<br>1b - Enabled|
|19|Enable S-VLAN Match|
|ERSVLM|Enables or disables S-VLAN match for received frames.<br>This field is valid only when the VLAN tag enable of the filter is set.<br>• If this field is 1, the MAC receiver enables filtering or matching for S-VLAN (type = 88A8h) packets.<br>• If this field is 0, the MAC receiver enables filtering or matching for C-VLAN (type = 8100h) packets.<br>0b - Disabled<br>1b - Enabled|
|18|Disable VLAN Type Comparison|
|DOVLTC|Enables or disables VLAN type comparison.<br>This field is valid only when the VEN field is 1.<br>• If this field is 1, MAC does not check whether the VLAN tag that ERIVLT specifies is of type S-VLAN<br>or C-VLAN.<br>• If this field is 0, MAC filters or matches the VLAN tag that the ERIVLT field specifies only when the<br>VLAN tag type is similar to the one that the ERSVLM field specifies.<br>0b - Enabled<br>1b - Disabled|
|17<br>ETV|VLAN Comparison<br>Indicates 12-bit or 16-bit VLAN comparison.<br>• This field is valid only when the VEN field is 1.<br>• When the value of this field is 1, a 12-bit VLAN identifier is used for filter and comparison instead of<br>the complete 16-bit VLAN tag. Bits [11:0] of the VLAN tag are compared with the corresponding field<br>in the received VLAN-tagged packet.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2998 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - 16-bit VLAN comparison|
||1b - 12-bit VLAN comparison|
|16|VLAN Tag Enable|
|VEN|Enables or disables the VLAN tag.|
||• If this field is 1, MAC compares the VLAN tag of the received packet with the VLAN tag ID.<br>• If this field is 0, no comparison is performed irrespective of the programming of the other fields.<br>0b - Disabled|
||1b - Enabled|
|15-0|VLAN Tag ID|
|VID|Holds the VLAN tag value that MAC uses for perfect comparison. The field is valid when VEN = 1.|



### 74.7.12 MAC VLAN Tag Filter 1 (MAC_VLAN_Tag_Filter1) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter1|54h|



##### Function 

Contains VLAN tag filter 1 control information. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||Rese|rved|||DMAC<br>HN|DMAC<br>HEN||Reserved||ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2999 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Fields 

|Field<br>31-26<br>—|Function<br>Reserved|
|---|---|
|25<br>DMACHN|DMA Channel Number<br>Indicates the DMA channel number to which the VLAN-tagged frame is to be routed if it passes the VLAN<br>tag filter programmed using this field.<br>If the routing based on VLAN tag filter is not necessary, this field does not need to be programmed.|
|24<br>DMACHEN|DMA Channel Number Enable<br>Enables or disables the DMA channel number value programmed using the DMACHN field.<br>If this field is 0, the routing does not occur based on the VLAN filter result. The frame is routed on the basis<br>of DA-based DMA channel routing.<br>0b - Disabled<br>1b - Enabled|
|23-21<br>—|Reserved|
|20<br>ERIVLT|Enable Inner VLAN Tag<br>Enables or disables inner VLAN tag comparison.<br>• This field is valid only when the double VLAN tag enable of the filter is set.<br>• If this field and the EDVLP field is 1, the MAC receiver enables operation on the inner VLAN tag (if<br>present).<br>• If this field is 0, the MAC receiver enables operation on the outer VLAN tag (if present).<br>0b - Disabled<br>1b - Enabled|
|19<br>ERSVLM|Enable S-VLAN Match<br>Enables or disables S-VLAN match for received frames.<br>This field is valid only when the VLAN tag enable of the filter is set.<br>• If this field is 1, the MAC receiver enables filtering or matching for S-VLAN (type = 88A8h) packets.<br>• If this field is 0, the MAC receiver enables filtering or matching for C-VLAN (type = 8100h) packets.<br>0b - Disabled<br>1b - Enabled|
|18|Disable VLAN Type Comparison|
|DOVLTC|Enables or disables VLAN type comparison.<br>This field is valid only when the VEN field is 1.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3000 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||• If this field is 1, MAC does not check whether the VLAN tag that ERIVLT specifies is of type S-VLAN<br>or C-VLAN.<br>• If this field is 0, MAC filters or matches the VLAN tag that the ERIVLT field specifies only when the<br>VLAN tag type is similar to the one that the ERSVLM field specifies.<br>0b - Enabled<br>1b - Disabled|
|17<br>ETV|VLAN Comparison<br>Indicates 12-bit or 16-bit VLAN comparison.<br>• This field is valid only when the VEN field is 1.<br>• When the value of this field is 1, a 12-bit VLAN identifier is used for filter and comparison instead of<br>the complete 16-bit VLAN tag. Bits [11:0] of the VLAN tag are compared with the corresponding field<br>in the received VLAN-tagged packet.<br>0b - 16-bit VLAN comparison<br>1b - 12-bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable<br>Enables or disables the VLAN tag.<br>• If this field is 1, MAC compares the VLAN tag of the received packet with the VLAN tag ID.<br>• If this field is 0, no comparison is performed irrespective of the programming of the other fields.<br>0b - Disabled<br>1b - Enabled|
|15-0<br>VID|VLAN Tag ID<br>Holds the VLAN tag value that MAC uses for perfect comparison. The field is valid when VEN = 1.|



### 74.7.13 MAC VLAN Tag Filter 2 (MAC_VLAN_Tag_Filter2) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter2|54h|



##### Function 

Contains VLAN tag filter 2 control information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3001 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3002-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R DMAC DMAC ERIVL ERSV DOVL<br>Reserved  Reserved  ETV  VEN<br>W HN  HEN  T  LM  TC<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>VID<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-26|Reserved|
|—||
|25|DMA Channel Number|
|DMACHN|Indicates the DMA channel number to which the VLAN-tagged frame is to be routed if it passes the VLAN<br>tag filter programmed using this field.<br>If the routing based on VLAN tag filter is not necessary, this field does not need to be programmed.|
|24|DMA Channel Number Enable|
|DMACHEN|Enables or disables the DMA channel number value programmed using the DMACHN field.<br>If this field is 0, the routing does not occur based on the VLAN filter result. The frame is routed on the basis<br>of DA-based DMA channel routing.<br>0b - Disabled|
||1b - Enabled|
|23-21|Reserved|
|—||
|20<br>ERIVLT|Enable Inner VLAN Tag<br>Enables or disables inner VLAN tag comparison.<br>• This field is valid only when the double VLAN tag enable of the filter is set.<br>• If this field and the EDVLP field is 1, the MAC receiver enables operation on the inner VLAN tag (if<br>present).<br>• If this field is 0, the MAC receiver enables operation on the outer VLAN tag (if present).<br>0b - Disabled<br>1b - Enabled|
|19|Enable S-VLAN Match|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3002 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|ERSVLM|Enables or disables S-VLAN match for received frames.<br>This field is valid only when the VLAN tag enable of the filter is set.<br>• If this field is 1, the MAC receiver enables filtering or matching for S-VLAN (type = 88A8h) packets.<br>• If this field is 0, the MAC receiver enables filtering or matching for C-VLAN (type = 8100h) packets.<br>0b - Disabled<br>1b - Enabled|
|18<br>DOVLTC|Disable VLAN Type Comparison<br>Enables or disables VLAN type comparison.<br>This field is valid only when the VEN field is 1.<br>• If this field is 1, MAC does not check whether the VLAN tag that ERIVLT specifies is of type S-VLAN<br>or C-VLAN.<br>• If this field is 0, MAC filters or matches the VLAN tag that the ERIVLT field specifies only when the<br>VLAN tag type is similar to the one that the ERSVLM field specifies.<br>0b - Enabled<br>1b - Disabled|
|17|VLAN Comparison|
|ETV|Indicates 12-bit or 16-bit VLAN comparison.<br>• This field is valid only when the VEN field is 1.<br>• When the value of this field is 1, a 12-bit VLAN identifier is used for filter and comparison instead of<br>the complete 16-bit VLAN tag. Bits [11:0] of the VLAN tag are compared with the corresponding field<br>in the received VLAN-tagged packet.<br>0b - 16-bit VLAN comparison<br>1b - 12-bit VLAN comparison|
|16<br>VEN|VLAN Tag Enable<br>Enables or disables the VLAN tag.<br>• If this field is 1, MAC compares the VLAN tag of the received packet with the VLAN tag ID.<br>• If this field is 0, no comparison is performed irrespective of the programming of the other fields.<br>0b - Disabled<br>1b - Enabled|
|15-0<br>VID|VLAN Tag ID<br>Holds the VLAN tag value that MAC uses for perfect comparison. The field is valid when VEN = 1.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3003 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

### 74.7.14 MAC VLAN Tag Filter 3 (MAC_VLAN_Tag_Filter3) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Tag_Filter3|54h|



##### Function 

Contains VLAN tag filter 3 control information. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||Rese|rved|||DMAC<br>HN|DMAC<br>HEN||Reserved||ERIVL<br>T|ERSV<br>LM|DOVL<br>TC|ETV|VEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VI|D||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-26<br>—|Reserved|
|25|DMA Channel Number|
|DMACHN|Indicates the DMA channel number to which the VLAN-tagged frame is to be routed if it passes the VLAN<br>tag filter programmed using this field.<br>If the routing based on VLAN tag filter is not necessary, this field does not need to be programmed.|
|24|DMA Channel Number Enable|
|DMACHEN|Enables or disables the DMA channel number value programmed using the DMACHN field.<br>If this field is 0, the routing does not occur based on the VLAN filter result. The frame is routed on the basis<br>of DA-based DMA channel routing.<br>0b - Disabled<br>1b - Enabled|
|23-21<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3004 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|20|Enable Inner VLAN Tag|
|ERIVLT|Enables or disables inner VLAN tag comparison.<br>• This field is valid only when the double VLAN tag enable of the filter is set.<br>• If this field and the EDVLP field is 1, the MAC receiver enables operation on the inner VLAN tag (if<br>present).<br>• If this field is 0, the MAC receiver enables operation on the outer VLAN tag (if present).<br>0b - Disabled<br>1b - Enabled|
|19<br>ERSVLM|Enable S-VLAN Match<br>Enables or disables S-VLAN match for received frames.<br>This field is valid only when the VLAN tag enable of the filter is set.<br>• If this field is 1, the MAC receiver enables filtering or matching for S-VLAN (type = 88A8h) packets.<br>• If this field is 0, the MAC receiver enables filtering or matching for C-VLAN (type = 8100h) packets.<br>0b - Disabled<br>1b - Enabled|
|18|Disable VLAN Type Comparison|
|DOVLTC|Enables or disables VLAN type comparison.<br>This field is valid only when the VEN field is 1.<br>• If this field is 1, MAC does not check whether the VLAN tag that ERIVLT specifies is of type S-VLAN<br>or C-VLAN.<br>• If this field is 0, MAC filters or matches the VLAN tag that the ERIVLT field specifies only when the<br>VLAN tag type is similar to the one that the ERSVLM field specifies.<br>0b - Enabled|
||1b - Disabled|
|17<br>ETV|VLAN Comparison<br>Indicates 12-bit or 16-bit VLAN comparison.<br>• This field is valid only when the VEN field is 1.<br>• When the value of this field is 1, a 12-bit VLAN identifier is used for filter and comparison instead of<br>the complete 16-bit VLAN tag. Bits [11:0] of the VLAN tag are compared with the corresponding field<br>in the received VLAN-tagged packet.<br>0b - 16-bit VLAN comparison<br>1b - 12-bit VLAN comparison|
|16|VLAN Tag Enable|
|VEN|Enables or disables the VLAN tag.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3005 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||• If this field is 1, MAC compares the VLAN tag of the received packet with the VLAN tag ID.|
||• If this field is 0, no comparison is performed irrespective of the programming of the other fields.|
||0b - Disabled|
||1b - Enabled|
|15-0|VLAN Tag ID|
|VID|Holds the VLAN tag value that MAC uses for perfect comparison. The field is valid when VEN = 1.|



### 74.7.15 MAC VLAN Hash Table (MAC_VLAN_Hash_Table) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Hash_Table|58h|



##### Function 

If MAC_VLAN_Tag_Ctrl[VTHM] = 1, the 16-bit VLAN hash table register is used for group address filtering based on the VLAN tag. For hash filtering, the content of the 16-bit VLAN tag or 12-bit VLAN ID (based on MAC_VLAN_Tag_Ctrl[ETV]) in the incoming packet is passed through the CRC logic. The upper four bits of the calculated CRC value are used to index the contents of the VLAN hash table. For example, hash value of 1000b selects bit 8 of the VLAN hash table. 

Perform these steps to calculate the hash value of the destination address: 

1. Calculate the 32-bit CRC for DA (see section 3.2.8 of IEEE 802.3 for steps to calculate CRC32). 

2. Perform bit-wise reversal for the value obtained in step 1. 

3. Take the upper 4 bits from the value obtained in step 2. 

If this register is configured to be double-synchronized with the (G)MII clock domain, the synchronization is triggered only when bits [15:8] (in Little-Endian mode) or bits [7:0] (in Big-Endian mode) of the register are written to. 

If double-synchronization is enabled, consecutive writes to this register must be performed after at least four clock cycles in the destination clock domain. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||Rese|rved||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||VL|HT||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3006 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Fields 

|Field|Function|
|---|---|
|31-16<br>—|Reserved|
|15-0|VLAN Hash Table|
|VLHT|Contains the 16-bit VLAN hash table.|



### 74.7.16 MAC VLAN Inclusion Or Replacement (MAC_VLAN_Incl) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Incl|60h|



##### Function 

Contains the VLAN tag for insertion or replacement in the transmit packets and the VLAN tag insertion controls. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3007-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R BUSY<br>RDWR  Reserved  ADDR  Reserved  CBTI  VLTI  CSVL  VLP  VLC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>VLT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Busy|
|BUSY|Indicates the status of the read or write operation of indirect access to the queue- or channel-specific VLAN<br>inclusion register.|
||The write operation to a register completes when this field becomes 0. For a read operation, the read data<br>is valid when the field becomes 0.<br>The application must make sure that this field becomes 0 before attempting subsequent accesses to<br>this register.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3007 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function<br>0b - Busy status not detected<br>1b - Busy status detected|
|---|---|
|30<br>RDWR|Read Write Control<br>Controls the read or write operation for indirectly accessing the queue- or channel-specific VLAN<br>inclusion register.<br>• If this field is 1, it indicates the write operation.<br>• If this field is 0, it indicates the read operation.<br>The value of this field is not impacted when the CBTI field becomes 0.<br>0b - Read operation of indirect access<br>1b - Write operation of indirect access|
|29-25<br>—|Reserved|
|24<br>ADDR|Address<br>Selects one of the queue- or channel-specific VLAN inclusion registers for read or write access.<br>The value of this field is not impacted when the CBTI field is 0.|
|23-22<br>—|Reserved|
|21<br>CBTI|Channel-Based Tag Insertion<br>Indicates the status of channel-based tag insertion.<br>If this field is 1:<br>• The outer VLAN tag is inserted for all the packets that MAC transmits.<br>• The tag value is taken from the queue- or channel-specific VLAN tag register. Also, the VLTI, VLP,<br>VLC, and VLT fields of the register are ignored.<br>• A write operation to byte 3 of this register initiates the read or write access to the indirect register.<br>If this field is 0, the outer VLAN operation is based on the settings of the VLTI, VLP, VLC, and VLT fields of<br>this register.<br>0b - Disabled<br>1b - Enabled|
|20<br>VLTI|VLAN Tag Input<br>Indicates the status of the VLAN tag input.<br>The value of this field being 1 indicates that the VLAN tag to be inserted or replaced in the transmit packet<br>must be taken from the transmit descriptor.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3008 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Disabled<br>1b - Enabled|
|19<br>CSVL|C-VLAN Or S-VLAN<br>Indicates whether C-VLAN or S-VLAN is inserted or replaced in the transmitted packets.<br>• If this field is 1, S-VLAN type (88A8h) is inserted or replaced in the 13th and 14th bytes of the<br>transmitted packets.<br>• If this field is 0, C-VLAN type (8100h) is inserted or replaced in the 13th and 14th bytes of the<br>transmitted packets.<br>0b - C-VLAN|
||1b - S-VLAN|
|18|VLAN Priority Control|
|VLP|Indicates the status of VLAN priority control.<br>• If this field is 1, the control bits [17:16] are used for VLAN deletion, insertion, or replacement.<br>• If this field is 0, the mti_vlan_ctrl_i control input is used and bits [17:16] are ignored.<br>0b - Disabled|
||1b - Enabled|
|17-16|VLAN Tag Control|
|VLC|Contains values for VLAN tag control in transmit packets.<br>MAC:<br>• Removes the VLAN type (bytes 13 and 14) and VLAN tag (bytes 15 and 16) of all the transmitted<br>packets with VLAN tags.<br>• Replaces VLT in bytes 15 and 16 of all the VLAN-type transmitted packets (bytes 13 and 14 are<br>8100h or 88a8h).<br>MAC inserts the following into the packet in the order shown:<br>1. Type value (8100h or 88A8h) into bytes 13 and 14<br>2. MAC_VLAN_Tag_Data[VLT]into bytes 15 and 16<br>This operation is performed on all the transmitted packets, irrespective of whether they already have a<br>VLAN tag.<br>Changes to this field take effect only on the start of a packet. If you write to this field when a<br>packet is being transmitted, only the subsequent packets can use the updated value. That<br>is, the current packet does not use the updated value.<br>~~NOTE~~|
||00b - No VLAN tag deletion, insertion, or replacement<br>01b - VLAN tag deletion|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3009 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||10b - VLAN tag insertion|
||11b - VLAN tag replacement|
|15-0|VLAN Tag For Transmit Packets|
|VLT|Contains the value of the VLAN tag to be inserted or replaced. This value must only be changed during the<br>initialization phase or when the transmit lines are inactive.|
||The following list describes the bits of this field:|
||• Bits [15:13]: User priority|
||• Bit 12: Canonical format indicator (CFI) or drop eligible indicator (DEI)<br>• Bits [11:0]:MAC_VLAN_Tag_Data[VID]|



### 74.7.17 MAC VLAN Inclusion 0 (MAC_VLAN_Incl0) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Incl0|60h|



##### Function 

Contains the VLAN tag for insertion in the transmit packets from transmit queue 0. The register also contains the VLAN tag insertion controls. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||Rese|rved||||||CSVL||Reserved||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||V|LT||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function||
|---|---|---|
|31-20|Reserved||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3010 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|19|C-VLAN or S-VLAN|
|CSVL|When this field is 1, S-VLAN type (0x88A8) is inserted in the 13th and 14th bytes of transmitted packets.<br>When this field is reset, C-VLAN type (0x8100) is inserted in the 13th and 14th bytes of transmitted packets.<br>0b - C-VLAN type (0x8100) is inserted<br>1b - S-VLAN type (0x88A8) is inserted|
|18-16<br>—|Reserved|
|15-0<br>VLT|VLAN Tag for Transmit Packets<br>Contains the value of the VLAN tag to be inserted.<br>The value of this field must only be changed when the transmit lines are inactive or during the<br>initialization phase.<br>The following list describes the bits of this field:<br>• Bits[15:13]: User Priority<br>• Bit 12: Canonical Format Indicator (CFI) or Drop Eligible Indicator (DEI)<br>• Bits[11:0]: VLAN Identifier (VID) field of VLAN tag|



### 74.7.18 MAC VLAN Inclusion 1 (MAC_VLAN_Incl1) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Incl1|60h|



##### Function 

Contains the VLAN tag for insertion in the transmit packets from transmit queue 1. The register also contains the VLAN tag insertion controls. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3011 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||Rese|rved||||||CSVL||Reserved||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||V|LT||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-20|Reserved|
|—||
|19|C-VLAN or S-VLAN|
|CSVL|When this field is 1, S-VLAN type (0x88A8) is inserted in the 13th and 14th bytes of transmitted packets.<br>When this field is reset, C-VLAN type (0x8100) is inserted in the 13th and 14th bytes of transmitted packets.<br>0b - C-VLAN type (0x8100) is inserted<br>1b - S-VLAN type (0x88A8) is inserted|
|18-16<br>—|Reserved|
|15-0<br>VLT|VLAN Tag for Transmit Packets<br>Contains the value of the VLAN tag to be inserted.<br>The value of this field must only be changed when the transmit lines are inactive or during the<br>initialization phase.<br>The following list describes the bits of this field:<br>• Bits[15:13]: User Priority<br>• Bit 12: Canonical Format Indicator (CFI) or Drop Eligible Indicator (DEI)<br>• Bits[11:0]: VLAN Identifier (VID) field of VLAN tag|



### 74.7.19 MAC VLAN Inclusion 2 (MAC_VLAN_Incl2) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Incl2|60h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3012 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Function 

Contains the VLAN tag for insertion in the transmit packets from transmit queue 2. The register also contains the VLAN tag insertion controls. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3013-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved  CSVL  Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>VLT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-20|Reserved|
|—||
|19|C-VLAN or S-VLAN|
|CSVL|When this field is 1, S-VLAN type (0x88A8) is inserted in the 13th and 14th bytes of transmitted packets.<br>When this field is reset, C-VLAN type (0x8100) is inserted in the 13th and 14th bytes of transmitted packets.<br>0b - C-VLAN type (0x8100) is inserted<br>1b - S-VLAN type (0x88A8) is inserted|
|18-16<br>—|Reserved|
|15-0<br>VLT|VLAN Tag for Transmit Packets<br>Contains the value of the VLAN tag to be inserted.<br>The value of this field must only be changed when the transmit lines are inactive or during the<br>initialization phase.<br>The following list describes the bits of this field:<br>• Bits[15:13]: User Priority<br>• Bit 12: Canonical Format Indicator (CFI) or Drop Eligible Indicator (DEI)<br>• Bits[11:0]: VLAN Identifier (VID) field of VLAN tag|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3013 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

### 74.7.20 MAC VLAN Inclusion 3 (MAC_VLAN_Incl3) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Incl3|60h|



##### Function 

Contains the VLAN tag for insertion in the transmit packets from transmit queue 3. The register also contains the VLAN tag insertion controls. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||Rese|rved||||||CSVL||Reserved||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||V|LT||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-20|Reserved|
|—||
|19|C-VLAN or S-VLAN|
|CSVL|When this field is 1, S-VLAN type (0x88A8) is inserted in the 13th and 14th bytes of transmitted packets.<br>When this field is reset, C-VLAN type (0x8100) is inserted in the 13th and 14th bytes of transmitted packets.<br>0b - C-VLAN type (0x8100) is inserted<br>1b - S-VLAN type (0x88A8) is inserted|
|18-16<br>—|Reserved|
|15-0<br>VLT|VLAN Tag for Transmit Packets<br>Contains the value of the VLAN tag to be inserted.<br>The value of this field must only be changed when the transmit lines are inactive or during the<br>initialization phase.<br>The following list describes the bits of this field:|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3014 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||• Bits[15:13]: User Priority|
||• Bit 12: Canonical Format Indicator (CFI) or Drop Eligible Indicator (DEI)|
||• Bits[11:0]: VLAN Identifier (VID) field of VLAN tag|



### 74.7.21 MAC VLAN Inclusion 4 (MAC_VLAN_Incl4) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Incl4|60h|



##### Function 

Contains the VLAN tag for insertion in the transmit packets from transmit queue 4. The register also contains the VLAN tag insertion controls. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3015-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved  CSVL  Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>VLT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-20|Reserved|
|—||
|19|C-VLAN or S-VLAN|
|CSVL|When this field is 1, S-VLAN type (0x88A8) is inserted in the 13th and 14th bytes of transmitted packets.<br>When this field is reset, C-VLAN type (0x8100) is inserted in the 13th and 14th bytes of transmitted packets.|
||0b - C-VLAN type (0x8100) is inserted|
||1b - S-VLAN type (0x88A8) is inserted|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3015 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18-16|Reserved|
|—||
|15-0|VLAN Tag for Transmit Packets|
|VLT|Contains the value of the VLAN tag to be inserted.<br>The value of this field must only be changed when the transmit lines are inactive or during the<br>initialization phase.<br>The following list describes the bits of this field:<br>• Bits[15:13]: User Priority<br>• Bit 12: Canonical Format Indicator (CFI) or Drop Eligible Indicator (DEI)<br>• Bits[11:0]: VLAN Identifier (VID) field of VLAN tag|



### 74.7.22 MAC VLAN Inclusion 5 (MAC_VLAN_Incl5) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Incl5|60h|



##### Function 

Contains the VLAN tag for insertion in the transmit packets from transmit queue 5. The register also contains the VLAN tag insertion controls. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3016-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved  CSVL  Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>VLT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3016 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Fields 

|Field|Function|
|---|---|
|31-20|Reserved|
|—||
|19|C-VLAN or S-VLAN|
|CSVL|When this field is 1, S-VLAN type (0x88A8) is inserted in the 13th and 14th bytes of transmitted packets.<br>When this field is reset, C-VLAN type (0x8100) is inserted in the 13th and 14th bytes of transmitted packets.<br>0b - C-VLAN type (0x8100) is inserted<br>1b - S-VLAN type (0x88A8) is inserted|
|18-16<br>—|Reserved|
|15-0<br>VLT|VLAN Tag for Transmit Packets<br>Contains the value of the VLAN tag to be inserted.<br>The value of this field must only be changed when the transmit lines are inactive or during the<br>initialization phase.<br>The following list describes the bits of this field:<br>• Bits[15:13]: User Priority<br>• Bit 12: Canonical Format Indicator (CFI) or Drop Eligible Indicator (DEI)<br>• Bits[11:0]: VLAN Identifier (VID) field of VLAN tag|



### 74.7.23 MAC VLAN Inclusion 6 (MAC_VLAN_Incl6) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Incl6|60h|



##### Function 

Contains the VLAN tag for insertion in the transmit packets from transmit queue 6. The register also contains the VLAN tag insertion controls. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3017 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||Rese|rved||||||CSVL||Reserved||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||V|LT||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-20|Reserved|
|—||
|19|C-VLAN or S-VLAN|
|CSVL|When this field is 1, S-VLAN type (0x88A8) is inserted in the 13th and 14th bytes of transmitted packets.<br>When this field is reset, C-VLAN type (0x8100) is inserted in the 13th and 14th bytes of transmitted packets.<br>0b - C-VLAN type (0x8100) is inserted<br>1b - S-VLAN type (0x88A8) is inserted|
|18-16<br>—|Reserved|
|15-0<br>VLT|VLAN Tag for Transmit Packets<br>Contains the value of the VLAN tag to be inserted.<br>The value of this field must only be changed when the transmit lines are inactive or during the<br>initialization phase.<br>The following list describes the bits of this field:<br>• Bits[15:13]: User Priority<br>• Bit 12: Canonical Format Indicator (CFI) or Drop Eligible Indicator (DEI)<br>• Bits[11:0]: VLAN Identifier (VID) field of VLAN tag|



### 74.7.24 MAC VLAN Inclusion 7 (MAC_VLAN_Incl7) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_VLAN_Incl7|60h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3018 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Function 

Contains the VLAN tag for insertion in the transmit packets from transmit queue 7. The register also contains the VLAN tag insertion controls. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3019-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved  CSVL  Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>VLT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-20|Reserved|
|—||
|19|C-VLAN or S-VLAN|
|CSVL|When this field is 1, S-VLAN type (0x88A8) is inserted in the 13th and 14th bytes of transmitted packets.<br>When this field is reset, C-VLAN type (0x8100) is inserted in the 13th and 14th bytes of transmitted packets.<br>0b - C-VLAN type (0x8100) is inserted<br>1b - S-VLAN type (0x88A8) is inserted|
|18-16<br>—|Reserved|
|15-0<br>VLT|VLAN Tag for Transmit Packets<br>Contains the value of the VLAN tag to be inserted.<br>The value of this field must only be changed when the transmit lines are inactive or during the<br>initialization phase.<br>The following list describes the bits of this field:<br>• Bits[15:13]: User Priority<br>• Bit 12: Canonical Format Indicator (CFI) or Drop Eligible Indicator (DEI)<br>• Bits[11:0]: VLAN Identifier (VID) field of VLAN tag|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3019 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

### 74.7.25 Inner VLAN Tag Inclusion Or Replacement (MAC_Inner_VLAN_Incl) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Inner_VLAN_Incl|64h|



##### Function 

Contains: 

- The inner VLAN tag to be inserted or replaced in the transmit packet 

- The inner VLAN tag insertion controls 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||Reserved||||||VLTI|CSVL|VLP|VLC|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R<br>W||||||||V|LT|||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



##### Fields 

|Field|Function|
|---|---|
|31-21|Reserved|
|—||
|20|VLAN Tag Input|
|VLTI|Indicates the status of VLAN tag input.<br>If this field is 1, it indicates that the VLAN tag to be inserted or replaced in the transmit packet must be taken<br>from the transmit descriptor.<br>0b - Disabled|
||1b - Enabled|
|19|C-VLAN Or S-VLAN|
|CSVL|Controls the insertion or replacement type in the 17th and 18th bytes of the transmitted packets.<br>0b - C-VLAN type (8100h)<br>1b - S-VLAN type (88A8h)|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3020 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|18|VLAN Priority Control|
|VLP|Indicates the status of VLAN priority control.<br>• If this field is 1, it's used for VLAN deletion, insertion, or replacement.<br>• If this field is 0, the mti_vlan_ctrl_i control input is used andMAC_VLAN_Incl[VLC]is ignored.<br>0b - Disabled<br>1b - Enabled|
|17-16<br>VLC|VLAN Tag Control in Transmit Packets<br>Indicates the value of VLAN tag control in transmit packets.<br>The following list specifies these values:<br>• 2'b00: No VLAN tag deletion, insertion, or replacement<br>• 2'b01: VLAN tag deletion<br>• 2'b10: VLAN tag insertion<br>• 2'b11: VLAN tag replacement<br>MAC:<br>• Removes the VLAN type (bytes 17 and 18) and VLAN tag (bytes 19 and 20) of all the transmitted<br>packets with VLAN tags<br>• Inserts VLT in bytes 19 and 20 of the packet after inserting the Type value (8100h or 88a8h) in bytes<br>17 and 18. This operation is performed on all the transmitted packets, irrespective of whether they<br>already have a VLAN tag.<br>• Replaces VLT in bytes 19 and 20 for all the VLAN-type transmitted packets (bytes 17 and 18 are<br>8100h or 88a8h).|
||Changes to this field take effect only on the start of a packet. If you write to the field when a<br>packet is being transmitted, only the subsequent packets can use the updated value. That<br>is, the current packet does not use the updated value.<br>~~NOTE~~|
||00b - No VLAN tag deletion, insertion, or replacement<br>01b - VLAN tag deletion<br>10b - VLAN tag insertion|
||11b - VLAN tag replacement|
|15-0<br>VLT|VLAN Tag For Transmit Packets<br>Contains the value of the VLAN tag to be inserted or replaced. The value must only be changed when the<br>transmit lines are inactive or during the initialization phase.<br>The following list describes the bits of this field:<br>• Bits [15:13]: User priority|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3021 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||• Bit 12: CFI or DEI|
||• Bits [11:0]:MAC_VLAN_Tag_Data[VID]|



### 74.7.26 MAC Q0 Tx Flow Control (MAC_Q0_Tx_Flow_Ctrl) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Q0_Tx_Flow_Ctrl|70h|



##### Function 

Controls the generation and reception of the control (pause command) packets by MAC's flow control module. A write to the register with the Busy field = 1 triggers the flow control block to generate a pause packet. The 802.3x specification indicates the way the fields of the control packet are selected, and the pause time value from this register is used in the PT field of the control packet. The Busy field remains 1 until the control packet is transferred onto the cable. You must make sure that the Busy field is 0 before writing to this register. 

If the value of the PFCE field in the MAC_Rx_Flow_Ctrl register is 1, this register controls the generation of priority flow control (PFC) frames with priorities mapped according to MAC_RxQ_Ctrl2[PSRQ0]. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3022-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>PT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R FCB_<br>Reserved  DZPQ  PLT  Reserved  TFE<br>W BPA<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-16|Pause Time|
|PT|Holds the value to be used in this field in the transmit control packet. If the bits of this field are configured to<br>be double-synchronized with the (G)MII clock domain, consecutive writes to this register must be performed<br>only after at least four clock cycles in the destination clock domain.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3022 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|15-8<br>—|Reserved|
|7<br>DZPQ|Disable Zero-Quanta Pause<br>Enables or disables zero-quanta pause packet generation.<br>• If this field is 1, it disables the automatic generation of the zero-quanta pause packets that the<br>flow-control signal from the FIFO layer (MTL or external sideband flow control signal sbd_flowctrl_i or<br>mti_flowctrl_i) deasserts.<br>• If this field is 0, normal operations with automatic zero-quanta pause packet generation are enabled.<br>0b - Enabled<br>1b - Disabled|
|6-4<br>PLT|Pause Low Threshold<br>Configures the threshold of the pause timer at which the input flow control signal mti_flowctrl_i (or<br>sbd_flowctrl_i) is checked for automatic retransmission of the pause packet.<br>The threshold values must always be less than the pause time configured in bits [31:16]. For example, if the<br>PT field = 100H (256 slot times), and the PLT field = 001, a second pause packet automatically transmits if<br>the mti_flowctrl_i signal is asserted at 228 (256-28) slot times after the first pause packet transmits.<br>This list provides the threshold values for different values:<br>• The slot time is defined as the time taken to transmit 512 bits (64 bytes) on GMII or MII.<br>• This (approximate) computation is based on the packet size (64, 1518, 2000, 9018, 16384, or<br>32768) + two pause packet sizes + IPG in slot times.<br>000b - Pause time minus 4 slot times (PT is 4 slot times)<br>001b - Pause time minus 28 slot times (PT is 28 slot times)<br>010b - Pause time minus 36 slot times (PT is 36 slot times)<br>011b - Pause time minus 144 slot times (PT is 144 slot times)<br>100b - Pause time minus 256 slot times (PT is 256 slot times)<br>101b - Pause time minus 512 slot times (PT is 512 slot times)<br>110b - Reserved|
|3-2<br>—|Reserved|
|1<br>TFE|Transmit Flow Control Enable<br>Indicates whether transmit flow control is enabled or disabled.<br>• Full-Duplex mode: If this field is 1, MAC enables the flow control operation to the transmit pause<br>packets. When the field becomes 0, MAC's flow control operation disables and MAC does not<br>transmit any pause packets.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3023 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||• Half-Duplex mode: If this field is 1, MAC enables the backpressure operation. When the field<br>becomes 0, the backpressure operation disables.<br>0b - Disabled<br>1b - Enabled|
|0|Flow Control Busy Or Backpressure Activate|
|FCB_BPA|Initiates if a pause packet is in Full-Duplex mode and activates the backpressure function in Half-Duplex<br>mode if the TFE field is 1.<br>• Full-Duplex mode: In this mode, FCB_BPA must be read as 1'b0 before writing to this register. To<br>initiate a pause packet, the application must set this field to 1'b1. During control packet transfer, the<br>field's value continues to be 1 to indicate that a packet transmission is in progress. When pause<br>packet transmission is complete, MAC resets this field to 1'b0. You must not write to this register<br>until this field becomes 0.<br>• Half-Duplex mode: If FCB_BPA = 1 and TFE = 1 too, MAC asserts backpressure in this mode.<br>During the backpressure function, when MAC receives a new packet, the transmitter starts<br>sending a JAM pattern resulting in a collision. This control register field is logically ORed with the<br>mti_flowctrl_i input signal for the backpressure function. When you configure MAC using Full-Duplex<br>mode, this field automatically becomes 0.<br>Access restrictions apply to this field: writing 1 sets it, writing 0 has no effect, and the field is self-clearing.<br>0b - Flow control busy or backpressure activate is disabled<br>1b - Flow control busy or backpressure activate is enabled|



### 74.7.27 MAC Receive Flow Control (MAC_Rx_Flow_Ctrl) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Rx_Flow_Ctrl|90h|



##### Function 

Controls the pausing of MAC transmit based on the received pause packet. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3024 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3025-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserv<br>Reserved  Reserved  UP  RFE<br>W ed<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-9<br>—|Reserved|
|8<br>—|Reserved|
|7-2<br>—|Reserved|
|1<br>UP|Unicast Pause Packet Detect<br>Indicates whether the unicast pause packet is enabled or disabled.<br>A pause packet is processed when it has the unique multicast address specified in IEEE 802.3.<br>• If this field is 1, MAC can detect pause packets with a unicast address of the station. This address<br>must comply with the specifications inMAC Address 0 High (MAC_Address0_High)andMAC<br>Address 0 Low (MAC_Address0_Low).<br>• If this field is 0, MAC only detects pause packets with a unique multicast address.<br>MAC does not process a pause packet if the multicast address is different from the<br>unique multicast address. This applies to the received PFC packet if PFC is enabled.<br>The unique multicast address (01_80_C2_00_00_01h) complies with the IEEE 802.1<br>Qbb-2011 specifications.<br>~~NOTE~~|
||0b - Disabled<br>1b - Enabled|
|0|Receive Flow Control Enable|
|RFE|Indicates whether the receive flow control is enabled or disabled.<br>• If this field is 1 and MAC is operating in Full-Duplex mode, MAC decodes the received pause packet<br>and disables its transmitter for a specified (pause) time.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3025 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||• If this field is 0 or if MAC is operating in Half-Duplex mode, the decode function of the pause packet<br>disables.|
||When PFC is enabled, the flow control for PFC packets is enabled too. MAC decodes the received PFC<br>packet and disables the transmit queue, with matching priorities, for a duration of the received pause time.|
||0b - Disabled|
||1b - Enabled|



### 74.7.28 MAC RxQ Control 4 (MAC_RxQ_Ctrl4) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_RxQ_Ctrl4|94h|



##### Function 

Controls the routing of unicast and multicast packets that fail the destination or source address filter to the receive queues. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3026-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R VFFQ<br>Reserved  VFFQ<br>W E<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R MFFQ UFFQ<br>Reserved  MFFQ  Reserved  UFFQ<br>W E  E<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-18|Reserved|
|—||
|17|VLAN Tag Filter Fail Packets Queue|
|VFFQ|Holds the receive queue number to which the tagged packets failing the destination or source address filter<br>(and UFFQE and MFFQE not being 1) or failing the VLAN tag filter must be routed to. This field is valid only<br>when the VFFQE field = 1.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3026 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field<br>16<br>VFFQE|Function<br>VLAN Tag Filter Fail Packets Queuing Enable<br>Indicates whether VLAN tag filter fail packet queuing is enabled or disabled.<br>• If this field is 1, the tagged packets that fail the destination or source address filter or fail the VLAN<br>tag filter are routed to the receive queue number programmed using the VFFQ field.<br>• If this field is 0, the tagged packets that fail the destination or source address filter or fail the<br>VLAN tag filter are routed based on the other routing options. This field is valid only when<br>MAC_Packet_Filter[RA]= 1.<br>0b - Disabled<br>1b - Enabled|
|---|---|
|15-10<br>—|Reserved|
|9<br>MFFQ|Multicast Address Filter Fail Packets Queue<br>Holds the receive queue number to which the multicast packets failing the destination or source address<br>filter are routed to. This field is valid only when the MFFQE field = 1.|
|8<br>MFFQE|Multicast Address Filter Fail Packets Queuing Enable<br>Indicates whether multicast address filter fail packet queuing is enabled or disabled.<br>• If this field is 1, the multicast packets that fail the destination or source address filter are routed to<br>the receive queue number programmed using the MFFQ field.<br>• If this field is 0, the multicast packets that fail the destination or source address filter are routed<br>based on the other routing options.<br>This field is valid only whenMAC_Packet_Filter[RA]= 1.<br>0b - Disabled<br>1b - Enabled|
|7-2<br>—|Reserved|
|1<br>UFFQ|Unicast Address Filter Fail Packets Queue<br>Holds the receive queue number to which the unicast packets failing the destination or source address filter<br>are routed to. This field is valid only when the UFFQE field = 1.|
|0<br>UFFQE|Unicast Address Filter Fail Packets Queuing Enable<br>Indicates whether unicast address filter fail packet queuing is enabled or disabled.<br>• When the value of this field is 1, the unicast packets that fail the destination or source address filter<br>are routed to the receive queue number programmed using the UFFQ field.<br>• If this field is 0, the unicast packets that fail the destination or source address filter are routed based<br>on the other routing options.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3027 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||This field is valid only whenMAC_Packet_Filter[RA]= 1.|
||0b - Disabled|
||1b - Enabled|



### 74.7.29 MAC RxQ Control 0 (MAC_RxQ_Ctrl0) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_RxQ_Ctrl0|A0h|



##### Function 

Controls queue management in the MAC receiver. 

~~<mark>NOTE</mark>~~ 

In multiple receive queues configuration, all the queues are disabled by default. Enable the receive queue by programming the corresponding field in this register. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3028-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>Reserved  Reserved  Reserved  Reserved  Reserved  Reserved  RXQ1EN  RXQ0EN<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16<br>—|Reserved|
|15-14<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3028 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|13-12<br>—|Reserved|
|11-10|Reserved|
|—<br>9-8|Reserved|
|—<br>7-6<br>—|Reserved|
|5-4|Reserved|
|—||
|3-2<br>RXQ1EN|Receive Queue 1 Enable<br>Performs in a manner similar to the RXQ0EN field and indicates if receive queue 1 is enabled for AV or DCB.<br>00b - Queue not enabled<br>01b - Queue enabled for AV<br>10b - Queue enabled for DCB/generic<br>11b - Reserved|
|1-0|Receive Queue 0 Enable|
|RXQ0EN|Indicates whether receive queue 0 is enabled for AV or DCB.<br>00b - Queue not enabled<br>01b - Queue enabled for AV<br>10b - Queue enabled for DCB/generic<br>11b - Reserved|



### 74.7.30 Receive Queue Control 1 (MAC_RxQ_Ctrl1) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_RxQ_Ctrl1|A4h|



##### Function 

Controls the routing of multicast, broadcast, AV, DCB, and untagged packets to the receive queues. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3029 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18<br>17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||Reserved||||FPRQ||TPQ|C|TACP<br>QE|MCBC<br>QEN|Reserv<br>ed|MCBCQ||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2<br>1|0|
|R<br>W|Reserv<br>ed||UPQ||Reserv<br>ed||Reserved||Reserv<br>ed||PTPQ||Reserv<br>ed|AVCPQ||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27<br>—|Reserved|
|26-24<br>FPRQ|Frame Preemption Residue Queue<br>Holds the receive queue number to which the residual preemption frames must be forwarded.<br>Preemption frames that are tagged and pass the SA, DA, or VLAN filtering are routed based on the settings<br>of the PSRQ fields inMAC RxQ Control 2 (MAC_RxQ_Ctrl2). All other frames are treated as residual frames<br>and are routed to the queue number mentioned in this field. Queue 0 is used as the default queue for express<br>frames, so you cannot write 0 to this field.|
|23-22<br>TPQC|Tagged PTP Over Ethernet Packets Queuing Control<br>Controls the routing of the VLAN-tagged PTPoE packets.<br>These are the allowed programmable options:<br>• 2'b00: VLAN-tagged PTPoE packets are routed as generic VLAN-tagged packets (based on the<br>PSRQ fields inMAC RxQ Control 2 (MAC_RxQ_Ctrl2)for only non-AV enabled receive queues).<br>• 2'b01: VLAN-tagged PTPoE packets are routed to the receive queue that the PTPQ field of this<br>register specifies (this Rx queue can be enabled for AV or non-AV traffic).<br>• 2'b10: VLAN-tagged PTPoE packets are routed to only AV-enabled receive queues based on the<br>settings of the PSRQ fields.|
|21<br>TACPQE|Tagged AV Control Packets Queuing Enable<br>Indicates the status of tagged AV control packet queuing.<br>• If this field is 1, MAC routes the received tagged AV control packets to the receive queue that the<br>AVCPQ field specifies.<br>• If this field is 0, MAC routes the received tagged AV control packets based on the tag priority<br>matching the PSRQ fields inMAC RxQ Control 2 (MAC_RxQ_Ctrl2).<br>0b - Disabled<br>1b - Enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3030 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field<br>20<br>MCBCQEN|Function<br>Multicast And Broadcast Queue Enable<br>Specifies whether multicast or broadcast packet routing to the receive queue is enabled or disabled. The<br>multicast or broadcast packets must be routed to the receive queue specified in the MCBCQ field.<br>0b - Disabled<br>1b - Enabled|
|---|---|
|19<br>—|Reserved|
|18-16<br>MCBCQ|Multicast And Broadcast Queue<br>Specifies the receive queue onto which multicast or broadcast packets are routed. Any receive queue<br>enabled for Generic, DCB, or AV traffic can be used to route the multicast or broadcast packets.<br>000b - Receive queue 0<br>001b - Receive queue 1<br>010b - Receive queue 2<br>011b - Receive queue 3<br>100b - Receive queue 4<br>101b - Receive queue 5<br>110b - Receive queue 6<br>111b - Receive queue 7|
|15<br>—|Reserved|
|14-12<br>UPQ|Untagged Packet Queue<br>Indicates the receive queue to which the untagged packets need to be routed. Any receive queue enabled<br>for generic, DCB, or AV traffic can be used to route the untagged packets.<br>000b - Receive queue 0<br>001b - Receive queue 1<br>010b - Receive queue 2<br>011b - Receive queue 3<br>100b - Receive queue 4<br>101b - Receive queue 5<br>110b - Receive queue 6<br>111b - Receive queue 7|
|11<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3031 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|10-8<br>—|Reserved|
|7<br>—|Reserved|
|6-4<br>PTPQ|PTP Packets Queue<br>Specifies the receive queue on which the PTP packets sent over the Ethernet payload (not over IPv4 or<br>IPv6) are routed.<br>WhenMAC_Timestamp_Control[AV8021ASMEN]= 1, only untagged PTP over Ethernet packets are<br>routed to a receive queue. If this field is not 1, then based on the settings of the TPQC field, both tagged and<br>untagged PTPoE packets can be routed to this receive queue.<br>000b - Receive queue 0|
||001b - Receive queue 1|
||010b - Receive queue 2|
||011b - Receive queue 3|
||100b - Receive queue 4|
||101b - Receive queue 5|
||110b - Receive queue 6|
||111b - Receive queue 7|
|3|Reserved|
|—||
|2-0<br>AVCPQ|AV Untagged Control Packets Queue<br>Specifies the receive queue on which the received AV tagged and untagged control packets are routed.<br>The AV tagged (when the TACPQE field = 1) and untagged control packets are routed to the receive queue<br>that this field specifies.<br>000b - Receive queue 0<br>001b - Receive queue 1<br>010b - Receive queue 2<br>011b - Receive queue 3<br>100b - Receive queue 4<br>101b - Receive queue 5|
||110b - Receive queue 6<br>111b - Receive queue 7|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3032 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

### 74.7.31 MAC RxQ Control 2 (MAC_RxQ_Ctrl2) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_RxQ_Ctrl2|A8h|



##### Function 

Controls the routing of tagged packets based on the settings of MAC_Ext_Configuration[USP] for packets received in receive queues 0-3. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||Rese|rved|||||||Rese|rved||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||PS|RQ1|||||||PSR|Q0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-24<br>—|Reserved|
|23-16<br>—|Reserved|
|15-8|Priorities Selected In Receive Queue 1|
|PSRQ1|Determines the priorities assigned to receive queue 1. All the packets with priorities that match the values<br>defined in this field are routed to receive queue 1.<br>For example, if PSRQ1[4] = 1, packets withMAC_Ext_Configuration[USP]equal to 4 are routed to receive<br>queue 1. You must ensure that the content of this field is mutually exclusive to the PSRQ fields for other<br>queues. This means that the same priority is not mapped to multiple receive queues.|
|7-0|Priorities Selected In Receive Queue 0|
|PSRQ0|Determines the priorities assigned to receive queue 0. All the packets with priorities that match the values<br>defined in this field are routed to receive queue 0.<br>For example, if PSRQ0[5] = 1, packets withMAC_Ext_Configuration[USP]equal to 5 are routed to receive<br>queue 0. You must ensure that the content of this field is mutually exclusive to the PSRQ fields for other<br>queues. This means that the same priority is not mapped to multiple receive queues.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3033 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

### 74.7.32 MAC Interrupt Status (MAC_Interrupt_Status) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Interrupt_Status|B0h|



##### Function 

Contains the status of interrupts. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3034-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>MDIOI<br>R MFRIS  MFTIS  FPEIS<br>S  Reserv<br>Reserved<br>ed<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>RXST TXST MMCT MMCR MMCI<br>R TSIS<br>Reserv SIS  SIS  Reserv XIS  XIS  S  Reserv Reserv PHYIS Reserv Reserv Reserv<br>Reserved<br>ed  ed  ed  ed  ed  ed  ed<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-21|Reserved|
|—||
|20|MMC FPE Receive Interrupt Status|
|MFRIS|Indicates the status of MMC FPE receive interrupt.<br>This field becomes 1 when any of the fields inMMC Receive Packet Assembly Error Counter Interrupt<br>Status (MMC_FPE_Rx_Interrupt)is 1. The field becomes 0 when all the other fields inMMC Receive Packet<br>Assembly Error Counter Interrupt Status (MMC_FPE_Rx_Interrupt)become 0 too.<br>0b - Inactive<br>1b - Active|
|19<br>MFTIS|MMC FPE Transmit Interrupt Status<br>Indicates the status of MMC FPE transmit interrupt.<br>This field becomes 1 when an interrupt generates inMMC Transmit FPE Fragment Counter Interrupt Status<br>(MMC_FPE_Tx_Interrupt). The field becomes 0 when all the other fields in this register become 0 too.<br>This field is valid only when you select the Enable MAC Management Counters (MMC) option along with<br>FPE support.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3034 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function<br>0b - Inactive<br>1b - Active|
|---|---|
|18<br>MDIOIS|MDIO Interrupt Status<br>Indicates the status of an interrupt event after the completion of an MDIO operation.<br>To reset this field, you must read this field or write 1 to it whenMAC_CSR_SW_Ctrl[RCWE]= 1.<br>Access restrictions apply to this field. It clears on a read or write of 1 whenMAC_CSR_SW_Ctrl[RCWE]=<br>1. The field automatically becomes 1 on an internal event.<br>0b - Inactive<br>1b - Active|
|17<br>FPEIS|Frame Preemption Interrupt Status<br>Indicates the status of an interrupt event during the frame preemption operation (the value of RVER, RRSP,<br>TVER, and TRSP fields ofMAC FPE Control STS (MAC_FPE_CTRL_STS)= 1).<br>To reset this field, you must clear the event inMAC FPE Control STS (MAC_FPE_CTRL_STS)that caused<br>the interrupt.<br>0b - Inactive<br>1b - Ative|
|16<br>—|Reserved|
|15<br>—|Reserved|
|14|Receive Status Interrupt|
|RXSTSIS|Indicates the status of received packets.<br>This field becomes 1 whenMAC_Rx_Tx_Status[RWT]= 1. The field becomes 0 when you read the<br>corresponding interrupt source field inMAC Rx Transmit Status (MAC_Rx_Tx_Status), or if you write to this<br>interrupt source field whenMAC_CSR_SW_Ctrl[RCWE]= 1.<br>The field becomes 0 in either of these circumstances:<br>• You read the corresponding interrupt-source field inMAC Rx Transmit Status (MAC_Rx_Tx_Status).<br>• You write 1 to the corresponding interrupt-source field inMAC Rx Transmit Status<br>(MAC_Rx_Tx_Status)whenMAC_CSR_SW_Ctrl[RCWE]= 1.<br>0b - Inactive<br>1b - Active|
|13|Transmit Status Interrupt|
|TXSTSIS|Indicates the status of transmitted packets.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3035 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3036-03.png)


<!-- Start of picture text -->
Field Function<br>This field becomes 1 when any of the following fields is 1 in MAC Rx Transmit Status (MAC_Rx_Tx_Status):<br>• Excessive collision (EXCOL)<br>• Late collision (LCOL)<br>• Excessive deferral (EXDEF)<br>• Loss of carrier (LCARR)<br>• No carrier (NCARR)<br>• Jabber timeout (TJT)<br>This field becomes 0 in either of these circumstances:<br>• You read the corresponding interrupt-source field in MAC Rx Transmit Status (MAC_Rx_Tx_Status).<br>• You write 1 to the corresponding interrupt-source field in MAC Rx Transmit Status<br>(MAC_Rx_Tx_Status) when MAC_CSR_SW_Ctrl[RCWE] = 1.<br>0b - Inactive<br>1b - Active<br>12 Timestamp Interrupt Status<br>TSIS Indicates the status of timestamp interrupt.<br>If the timestamp feature is enabled, this field becomes 1 when any of the following conditions is true:<br>• The system time value is equal to or exceeds the value specified in MAC PPS1 Target Time<br>In Seconds (MAC_PPS1_Target_Time_Seconds) and MAC PPS1 Target Time In Nanoseconds<br>(MAC_PPS1_Target_Time_Nanoseconds).<br>• There is an overflow in MAC System Time In Seconds (MAC_System_Time_Seconds).<br>• The target time error occurred, which means, the programmed target time already elapsed.<br>In configurations other than EQOS_CORE, when the drop transmit status is enabled in MTL, this field<br>becomes 1 when the captured transmit timestamp is updated in MAC Transmit Timestamp Status<br>In Nanoseconds (MAC_Tx_Timestamp_Status_Nanoseconds) and MAC Transmit Timestamp Status In<br>Seconds (MAC_Tx_Timestamp_Status_Seconds).<br>The field becomes 0 in either of these circumstances:<br>• You read the corresponding interrupt-source field in MAC Rx Transmit Status (MAC_Rx_Tx_Status).<br>• You write 1 to the corresponding interrupt-source field in MAC Rx Transmit Status<br>(MAC_Rx_Tx_Status) when MAC_CSR_SW_Ctrl[RCWE] = 1.<br>0b - Inactive<br>1b - Active<br>11 Reserved<br>—<br>10 MMC Transmit Interrupt Status<br>MMCTXIS Indicates the status of MMC transmit interrupt.<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3036 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function<br>This field:<br>• Becomes 1 when any field inMMC Transmit Interrupt (MMC_Tx_Interrupt)becomes 1.<br>• Becomes 0 when all the fields inMMC Transmit Interrupt (MMC_Tx_Interrupt)return to 0.<br>This field is valid only when you select the Enable MAC Management Counters (MMC) option.<br>0b - Inactive<br>1b - Active|
|---|---|
|9<br>MMCRXIS|MMC Receive Interrupt Status<br>Indicates the status of MMC receive interrupt.<br>This field:<br>• Becomes 1 when any field inMMC Receive Interrupt (MMC_Rx_Interrupt)becomes 1.<br>• Becomes 0 when all the fields inMMC Receive Interrupt (MMC_Rx_Interrupt)return to 0.<br>This field is valid only when you select the Enable MAC Management Counters (MMC) option.<br>0b - Inactive<br>1b - Active|
|8<br>MMCIS|MMC Interrupt Status<br>Indicates the status of MMC interrupt.<br>This field becomes 1 when MMCRXIS = MMCTXIS = 1, and the field becomes 0 only when MMCRXIS =<br>MMCTXIS = 0.<br>MMCIS is valid only when you select the Enable MAC Management Counters (MMC) option.<br>0b - Inactive<br>1b - Active|
|7-6<br>—|Reserved|
|5<br>—|Reserved|
|4<br>—|Reserved|
|3<br>PHYIS|PHY Interrupt<br>Indicates whether the PHY interrupt is detected.<br>This field becomes 1 when rising edge is detected on the phy_intr_i input signal. The field becomes 0 when<br>you read this register (or if you write 1 to this field whenMAC_CSR_SW_Ctrl[RCWE]= 1).<br>0b - Not detected<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3037 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - Detected|
|2<br>—|Reserved|
|1<br>—|Reserved|
|0<br>—|Reserved|



### 74.7.33 MAC Interrupt Enable (MAC_Interrupt_Enable) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Interrupt_Enable|B4h|



##### Function 

Contains masks for generating MAC interrupts. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||||||Reserved|||||||MDIOI<br>E|FPEIE|Reserv<br>ed|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|Reserv<br>ed|RXST<br>SIE|TXSTS<br>IE|TSIE|||Rese|rved|||Reserv<br>ed|Reserv<br>ed|PHYIE|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-19<br>—|Reserved|
|18|MDIO Interrupt Enable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3038 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field<br>MDIOIE|Function<br>Indicates whether the MDIO interrupt is enabled or disabled.<br>If this field is 1, it enables the assertion of the interrupt whenMAC_Interrupt_Status[MDIOIS]= 1.<br>0b - Disabled<br>1b - Enabled|
|---|---|
|17<br>FPEIE|Frame Preemption Interrupt Enable<br>Indicates whether the frame preemption interrupt is enabled or disabled.<br>If this field is 1, it enables the assertion of the interrupt whenMAC_Interrupt_Status[FPEIS]= 1.<br>0b - Disabled<br>1b - Enabled|
|16<br>—|Reserved|
|15<br>—|Reserved|
|14<br>RXSTSIE|Receive Status Interrupt Enable<br>Indicates whether the receive status interrupt is enabled or disabled.<br>If this field is 1, it enables the assertion of the interrupt signal because of the setting<br>ofMAC_Interrupt_Status[RXSTSIS].<br>0b - Disabled<br>1b - Enabled|
|13<br>TXSTSIE|Transmit Status Interrupt Enable<br>Indicates whether the timestamp status interrupt is enabled or disabled.<br>If this field is 1, it enables the assertion of the interrupt signal because of the setting<br>ofMAC_Interrupt_Status[TXSTSIS].<br>0b - Disabled<br>1b - Enabled|
|12<br>TSIE<br>11-6|Timestamp Interrupt Enable<br>Indicates whether the timestamp interrupt is enabled or disabled.<br>If this field is 1, it enables the assertion of the interrupt signal because of the<br>settingMAC_Interrupt_Status[TSIS].<br>0b - Disabled<br>1b - Enabled<br>Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3039 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—<br>5<br>—<br>4<br>—<br>3<br>PHYIE|Reserved<br>Reserved<br>PHY Interrupt Enable<br>Indicates whether the assertion of the interrupt signal is enabled or disabled.<br>If this field is 1, it enables the assertion of the interrupt signal because of the setting<br>ofMAC_Interrupt_Status[PHYIS].<br>0b - Disabled<br>1b - Enabled|
|2<br>—<br>1<br>—<br>0<br>—|Reserved<br>Reserved<br>Reserved|



### 74.7.34 MAC Rx Transmit Status (MAC_Rx_Tx_Status) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Rx_Tx_Status|B8h|



##### Function 

Contains the receive and transmit error status. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3040 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3041-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>EXCO EXDE LCAR NCAR<br>R RWT  LCOL  TJT<br>L  F  R  R<br>Reserved  Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-9<br>|Reserved|
|—<br>8|Receive Watchdog Timeout|
|RWT|Indicates the status of receive watchdog.<br>This field becomes 1 when a packet with a length greater than 2,048 bytes is received (10,240 bytes when<br>Jumbo Packet mode is enabled) andMAC_Configuration[WD]= 0. RWT becomes 1 when a packet with<br>length greater than 16,383 bytes is received andMAC_Configuration[WD]= 1.<br>Access restrictions apply to RWT. It becomes 0 on read or write of 1 whenMAC_CSR_SW_Ctrl[RCWE]=<br>1. RWT automatically becomes 1 on an internal event occurrence.<br>0b - No receive watchdog timed out<br>1b - Receive watchdog timed out|
|7-6<br>—<br>5|Reserved<br>Excessive Collisions|
|EXCOL|Indicates the status of excessive collision.<br>IfMTL_Operation_Mode[DTXSTS]= 1, this field, EXCOL, indicates that the transmission aborted after 16<br>successive collisions while attempting to transmit the current packet.<br>IfMAC_Configuration[DR]= 1, EXCOL becomes 1 after the first collision and the packet transmission<br>is aborted.<br>Access restrictions apply to EXCOL. It becomes 0 on read or write of 1 whenMAC_CSR_SW_Ctrl[RCWE]<br>= 1. EXCOL automatically becomes 1 on an internal event occurrence.<br>0b - No collision|
||1b - Excessive collision is sensed|
|4|Late Collision|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3041 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field<br>LCOL|Function<br>Indicates the status of late collision.<br>IfMTL_Operation_Mode[DTXSTS]= 1, this field, LCOL, indicates that the packet transmission aborted<br>because a collision occurred after the collision window (64 bytes including preamble in MII mode; 512 bytes<br>including preamble and carrier extension in GMII mode).<br>This field is invalid if an underflow error occurs.<br>Access restrictions apply to LCOL. It becomes 0 on read or write of 1 whenMAC_CSR_SW_Ctrl[RCWE]=<br>1. LCOL automatically becomes 1 on an internal event occurrence.<br>0b - No collision<br>1b - Late collision is sensed|
|---|---|
|3<br>EXDEF|Excessive Deferral<br>Indicates whether the transmission ended because of excessive deferral.<br>IfMTL_Operation_Mode[DTXSTS]= 1 andMAC_Configuration[DC]= 1 too, this field, EXDEF, indicates that<br>the transmission ended because of excessive deferral of over 24,288 bit times (155,680 in 1000/2500 Mbit/s<br>mode or when the jumbo packet is enabled).<br>Access restrictions apply to EXDEF. It becomes 0 on read or write of 1 whenMAC_CSR_SW_Ctrl[RCWE]<br>= 1. EXDEF automatically becomes 1 on an internal event occurrence.<br>0b - No excessive deferral<br>1b - Excessive deferral|
|2|Loss of Carrier|
|LCARR|Indicates the status of carrier signal.<br>IfMTL_Operation_Mode[DTXSTS]= 1, this field, LCARR, indicates that the loss of carrier occurred during<br>packet transmission, which means, the phy_crs_i signal was inactive for one or more transmission clock<br>periods during packet transmission. The field is valid only for packets transmitted without collision.<br>Access restrictions apply to LCARR. It becomes 0 on read or write of 1 whenMAC_CSR_SW_Ctrl[RCWE]<br>= 1. LCARR automatically becomes 1 on an internal event occurrence.<br>0b - Carrier is present<br>1b - Loss of carrier|
|1<br>NCARR|No Carrier<br>Indicates whether the carrier signal is present from the PHY at the end of preamble transmission.<br>IfMTL_Operation_Mode[DTXSTS]= 1, NCARR indicates that the carrier signal from the PHY is absent at<br>the end of preamble transmission.<br>Access restrictions apply to NCARR. It becomes 0 after either of these actions:<br>• You read NCARR.<br>• You write 1 to NCARR whenMAC_CSR_SW_Ctrl[RCWE]= 1.<br>NCARR automatically becomes 1 after an internal event occurs.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3042 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Present<br>1b - Absent|
|0|Transmit Jabber Timeout|
|TJT|Indicates whether a transmit-jabber timer timeout occurred. The timeout occurs after any of these events:<br>• MAC_Configuration[JD]= 0 and the normal packet size exceeds 2,048 bytes.<br>• MAC_Configuration[JD]= 0 and the jumbo packet size exceeds 10240 bytes.<br>• MAC_Configuration[JD]= 1 and the normal packet size exceeds 16383 bytes.<br>Access restrictions apply to TJT. It becomes 0 after either of these actions:<br>• You read TJT.<br>• You write 1 to TJT whenMAC_CSR_SW_Ctrl[RCWE]= 1.<br>TJT automatically becomes 1 after an internal event occurs.<br>0b - No transmit jabber timeout occurred|
||1b - Transmit jabber timeout occurred|



### 74.7.35 MAC Version (MAC_Version) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Version|110h|



##### Function 

Identifies the version of the module. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||Rese|rved||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||CFG|VER|||||||IPV|ER||||
|W|||||||||||||||||
|Reset|0|0|0|1|0|0|0|0|0|1|0|1|0|0|0|1|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3043 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Fields 

|Field|Function|
|---|---|
|31-16<br>—|Reserved|
|15-8|IP Configuration Version|
|CFGVER||
|7-0|IP Version|
|IPVER||



### 74.7.36 MAC Debug (MAC_Debug) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Debug|114h|



##### Function 

Provides the debug status of the various MAC blocks. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3044-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>TPEST<br>R TFCSTS<br>S<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>RPES<br>R RFCFCSTS<br>TS<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-19<br>—|Reserved|
|18-17|MAC Transmit Packet Controller Status|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3044 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|TFCSTS|Indicates the state of the MAC transmit packet controller module.<br>00b - Idle state<br>01b - Waiting for one of these: status of the previous packet or IPG, or for the back-off period to<br>be over<br>10b - Generating and transmitting a pause control packet (in Full-Duplex mode)<br>11b - Transferring input packet for transmission|
|16<br>TPESTS|MAC GMII Or MII Transmit Protocol Engine Status<br>Indicates whether MAC GMII or MII transmit protocol engine is detected.<br>If this field is 1, it indicates that the MAC GMII or MII transmit protocol engine is actively transmitting data<br>and is not in an idle state.<br>0b - Not detected<br>1b - Detected|
|15-3<br>—|Reserved|
|2-1<br>RFCFCSTS|MAC Receive Packet Controller FIFO Status<br>Indicates the status of the small FIFO read and write controllers of the MAC receive packet<br>controller module.<br>If this field is 1, it indicates that the small FIFO read and write controllers of the MAC receive packet controller<br>module are in an active state.<br>00b - Inactive<br>01b - Active|
|0<br>RPESTS|Receive Protocol Engine Status<br>Indicates whether MAC GMII or MII receive protocol engine is detected.<br>If this field is 1, it indicates that the MAC GMII or MII receive protocol engine is actively receiving data and<br>is not in an idle state.<br>0b - Not detected<br>1b - Detected|



### 74.7.37 MAC Hardware Feature 0 (MAC_HW_Feature0) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_HW_Feature0|11Ch|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3045 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Function 

Indicates the presence of the first set of EMAC optional features or functions. You can use this register to dynamically enable or disable the programs related to these features. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3046-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>SAVLA MACA MACA RXCO<br>R ACTPHYSEL  TSSTSSEL  ADDMACADRSEL<br>Reserv NI... DR6... DR3... Reserv ESEL<br>ed  ed<br>W<br>Reset 0 0 0 0 1 1 1 0 0 0 0 0 1 0 0 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>TXCO EEES ARPO MMCS MGKS RWKS SMAS VLHA PCSS HDSE GMIIS MIISE<br>R TSSEL<br>Reserv ESEL  EL  FFS... EL  EL  EL  EL  SH  EL  L  EL  L<br>Reserved<br>ed<br>W<br>Reset 0 1 0 1 0 0 0 1 0 0 1 1 0 1 0 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Reserved|
|—||
|30-28|Active PHY Feature|
|ACTPHYSEL|Indicates the selected active PHY interface.<br>If you have multiple PHY interfaces (GMII, MII, RevMII,RGMII, RMII, RTBI, SGMII,SGMII, or TBI) in your<br>configuration, this field indicates the sampled value of the phy_intf_sel_i signal during reset deassertion.<br>000b - GMII or MII<br>001b - RGMII|
||010b - SGMII<br>011b - TBI|
||100b - RMII|
||101b - RTBI|
||110b - SMII|
||111b - RevMII|
|27|SA or VLAN Insertion Feature|
|SAVLANINS|Indicates whether the feature that enables SA or VLAN insertion on transmit is selected.<br>This field becomes 1 if you select the "enable SA and VLAN insertion on Tx" option.<br>0b - Not selected|
||1b - Selected|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3046 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|26-25<br>TSSTSSEL|Timestamp System Time Source Feature<br>Indicates the source of the timestamp system time.<br>This field becomes 1 if you select the "enable IEEE 1588 timestamp support" option.<br>00b - Internal<br>01b - External<br>10b - Both internal and external<br>11b - Reserved|
|24<br>MACADR64SE<br>L|MAC Addresses 64-127<br>Indicates whether the feature that enables additional 64 MAC address regsiters (64-127) is selected.<br>This field becomes 1 if you enable the "MAC addresses (64-127) select" option.<br>0b - Not selected<br>1b - Selected|
|23<br>MACADR32SE<br>L|MAC Addresses 32-63<br>Indicates whether the feature that enables additional 32 MAC address registers (32-63) is selected.<br>This field becomes 1 if you select the "MAC addresses 32-63 select" option.<br>0b - Not selected<br>1b - Selected|
|22-18<br>ADDMACADRS<br>EL|MAC Addresses 1-31<br>Indicates whether the feature that enables additional 1-31 MAC address registers is selected.<br>This field becomes 1 if you select a non-zero value for enabling the "MAC addresses 1-31 select" option.<br>0_0000b - Not selected<br>0_0001b - Selected|
|17<br>—|Reserved|
|16<br>RXCOESEL|Receive Checksum Offload Feature<br>Indicates whether the feature that enables receive TCP/IP checksum offload is selected.<br>This field becomes 1 if you select the "enable receive TCP/IP checksum check" option.<br>0b - Not selected<br>1b - Selected|
|15<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3047 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field<br>14<br>TXCOESEL|Function<br>Transmit Checksum Offload Feature<br>Indicates whether the feature that enables transmit TCP/IP checksum insertion is selected.<br>This field becomes 1 if you select the "enable transmit TCP/IP checksum insertion" option.<br>0b - Not selected<br>1b - Selected|
|---|---|
|13<br>EEESEL|Energy Efficient Ethernet (EEE) Feature<br>Indicates whether the feature that enables EEE is selected.<br>This field becomes 1 if you select the "enable EEE" option.<br>0b - Not selected<br>1b - Selected|
|12<br>TSSEL|IEEE 1588-2008 Timestamp Feature<br>Indicates whether the option that enables IEEE 1588-2008 timestamp is selected.<br>This field becomes 1 if you select the "enable IEEE 1588 timestamp support" option.<br>0b - Not selected<br>1b - Selected|
|11-10<br>—|Reserved|
|9<br>ARPOFFSEL|ARP Offload Feature<br>Indicates whether the feature that enables ARP offload is selected.<br>This field becomes 1 if you select the "enable IPv4 ARP offload" option.<br>0b - Not selected<br>1b - Selected|
|8<br>MMCSEL|MAC Management Counters (MMC) Feature<br>Indicates whether the feature that enables MMC is selected.<br>This field becomes 1 if you select the "enable MMC" option.<br>0b - Not selected<br>1b - Selected|
|7<br>MGKSEL|PMT Magic Packet Feature<br>Indicates whether the feature that enables PMT magic detection is selected.<br>This field becomes 1 if you select the "enable magic packet detection" option.<br>0b - Not selected<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3048 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function<br>1b - Selected|
|---|---|
|6<br>RWKSEL|PMT Remote Wake-Up Packet Feature<br>Indicates whether the feature that enables PMT remote wake-up packet detection is selected.<br>This field becomes 1 if you select the "enable remote wake-up packet detection" option.<br>0b - Not selected<br>1b - Selected|
|5<br>SMASEL|SMA (MDIO) Interface Feature<br>Indicates whether the feature that enables station management (MDIO interface) is selected.<br>This field becomes 1 if you select the "enable station management (MDIO interface)" option.<br>0b - Not selected<br>1b - Selected|
|4<br>VLHASH|VLAN Hash Filter Feature<br>Indicates whether the filtering option based on VLAN hash table is selected.<br>This field becomes 1 if you select the "enable VLAN hash table based filtering" option.<br>0b - Not selected<br>1b - Selected|
|3<br>PCSSEL|PCS Select<br>Indicates if either of the TBI, SGMII, or RTBI PHY interface options is selected.<br>This field becomes 1 if you select any one of the TBI, SGMII, or RTBI PHY interface options.<br>0b - No<br>1b - Yes|
|2<br>HDSEL|Half-Duplex Support Feature<br>Indicates whether half-duplex support is available as the mode of operation.<br>This field becomes 1 if you select Half-Duplex as the mode of operation.<br>0b - Unavailable<br>1b - Available|
|1<br>GMIISEL|1000 Mbit/s Support Feature<br>Indicates whether 1000 Mbit/s support is available as the mode of operation.<br>This field becomes 1 if you select 1000 Mbit/s as the mode of operation.<br>0b - Unavailable<br>1b - Available<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3049 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|0|10 or 100 Mbit/s Support Feature|
|MIISEL|Indicates whether 10 or 100 Mbit/s support is available as the mode of operation.|
||This field becomes 1 if you select 10/100 Mbit/s as the mode of operation.|
||0b - Unavailable|
||1b - Available|



### 74.7.38 MAC Hardware Feature 1 (MAC_HW_Feature1) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_HW_Feature1|120h|



##### Function 

Indicates the presence of the second set of optional features or functions of the module. You can use this register to dynamically enable or disable the programs related to these features. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3050-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>POUO RAVS DBGM TSOE SPHE DCBE<br>R L3L4FNUM  HASHTBLSZ  AVSEL<br>Reserv Reserv ST  Reserv EL  EMA  N  N  N<br>ed  ed  ed<br>W<br>Reset 0 0 1 0 0 0 0 1 0 0 0 1 1 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>ADVT<br>PTOE OSTE SPRA<br>R ADDR64  HWO.. TXFIFOSIZE  RXFIFOSIZE<br>N  N  M<br>.<br>W<br>Reset 0 0 1 0 1 0 0 1 1 0 1 0 0 1 1 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31<br>—|Reserved|
|30-27|L3 Or L4 Filter Number|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3050 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|L3L4FNUM|Indicates the total number of L3 or L4 filters.<br>0000b - No filters (0)<br>0001b - 1<br>0010b - 2<br>0011b - 3<br>0100b - 4<br>0101b - 5<br>0110b - 6<br>0111b - 7<br>1000b - 8|
|26|Reserved|
|—||
|25-24|Hash Table Size|
|HASHTBLSZ|Indicates the size of the hash table.<br>00b - No hash table<br>01b - 64<br>10b - 128<br>11b - 256|
|23<br>POUOST|One Step For PTP Over UDP/IP Feature<br>Indicates whether the feature that enables one step for PTP over UDP/IP is selected.<br>This field becomes 1 if you select the "enable one-step timestamp for PTP over UDP/IP" option.<br>0b - Not selected<br>1b - Selected|
|22<br>—|Reserved|
|21<br>RAVSEL|Receive Side-Only AV Feature<br>Indicates whether the feature that enables audio-video bridging only on the receive side is selected.<br>This field becomes 1 if you select the "enable audio-video bridging on receive side only" option.<br>0b - Not selected<br>1b - Selected|
|20|AV Feature<br>Indicates whether the feature that enables audio-video bridging is selected.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3051 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|AVSEL|This field becomes 1 if you select the "enable audio video bridging" option.<br>0b - Not selected<br>1b - Selected|
|19<br>DBGMEMA|DMA Debug Registers Enable Feature<br>Indicates whether the feature that enables DMA debug regsiters is selected.<br>This field becomes 1 if you select the "enable DMA debug mode" option.<br>0b - Not selected<br>1b - Selected|
|18<br>TSOEN|TCP Segmentation Offload Enable Feature<br>Indicates whether the feature that enables TCP segmentation offload for TCP/IP packets is selected.<br>This field becomes 1 if you select the "enable TCP segmentation offloading for TCP/IP packets" option.<br>0b - Not selected<br>1b - Selected|
|17<br>SPHEN|Split Header Enable Feature<br>Indicates whether the feature that enables a split header structure is selected.<br>This field becomes 1 if you select the "enable split header structure" option.<br>0b - Not selected<br>1b - Selected|
|16<br>DCBEN|DCB Enable Feature<br>Indicates whether the feature that enables data center bridging is selected.<br>This field becomes 1 if you select the "enable data center bridging" option.<br>0b - Not selected<br>1b - Selected|
|15-14<br>ADDR64|Address Width Feature<br>Indicates the configured address width.<br>00b - 32<br>01b - 40<br>10b - 48<br>11b - Reserved|
|13|IEEE 1588 High-Word Feature|
|ADVTHWORD|Indicates whether the feature that enables the IEEE 1588 high-word register is selected.<br>This field becomes 1 if you select the "enable/add IEEE 1588 higher-word register" option.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3052 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Not selected<br>1b - Selected|
|12<br>PTOEN|PTP Offload Enable Feature<br>Indicates whether the feature that enables PTP offload is selected.<br>This field becomes 1 if you select the "enable PTP timestamp offload" option.<br>0b - Not selected<br>1b - Selected|
|11<br>OSTEN|One-Step Timestamping Enable Feature<br>Indicates whether the feature that enables one-step timestamping is selected.<br>This field becomes 1 if you select the "enable one-step timestamp" option.<br>0b - Not selected<br>1b - Selected|
|10-6|MTL Transmit FIFO Size Feature|
|TXFIFOSIZE|Contains the configured value of MTL transmit FIFO (in bytes) expressed as log to base 2 minus 7, which<br>means, Log 2 (TXFIFO_SIZE) - 7.<br>0_0000b - 128 bytes<br>0_0001b - 256 bytes<br>0_0010b - 512 bytes<br>0_0011b - 1024 bytes<br>0_0100b - 2048 bytes<br>0_0101b - 4096 bytes<br>0_0110b - 8192 bytes<br>0_0111b - 16384 bytes<br>0_1000b - 32 KB<br>0_1001b - 64 KB<br>0_1010b - 128 KB|
||0_1011b - Reserved|
|5<br>SPRAM|Single Port RAM Feature<br>Indicates whether the single-port RAM feature is selected.<br>This field becomes 1 if you select the option that enables the "use single port RAM" feature.<br>0b - Not selected|
||1b - Selected|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3053 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|4-0|MTL Receive FIFO Size Feature|
|RXFIFOSIZE|Contains the configured value of MTL receive FIFO (in bytes) expressed as log to base 2 minus 7, which<br>means, Log 2 (RXFIFO_SIZE) - 7.<br>0_0000b - 128 bytes|
||0_0001b - 256 bytes|
||0_0010b - 512 bytes|
||0_0011b - 1024 bytes|
||0_0100b - 2048 bytes|
||0_0101b - 4096 bytes|
||0_0110b - 8192 bytes|
||0_0111b - 16384 bytes<br>0_1000b - 32 KB|
||0_1001b - 64 KB|
||0_1010b - 128 KB|
||0_1011b - 256 KB|
||0_1100b - Reserved|



### 74.7.39 MAC Hardware Feature 2 (MAC_HW_Feature2) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_HW_Feature2|124h|



##### Function 

Indicates the presence of the third set of optional features or functions of the module. You can use this register to dynamically enable or disable the programs related to these features. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3054 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|Reserv|AU|XSNAPN|UM|Reserv|PP|SOUTN|UM|Rese|rved||TXCH|CNT||Res|erved|
|W|ed||||ed||||||||||||
|Reset|0|0|0|0|0|1|0|0|0|0|0|0|0|1|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||RXCH|CNT||Reser|ved||TXQ|CNT||Rese|rved||RXQ|CNT||
|W|||||||||||||||||
|Reset|0|0|0|1|0|0|0|0|0|1|0|0|0|0|0|1|



##### Fields 

|Field|Function|
|---|---|
|31<br>—|Reserved|
|30-28<br>AUXSNAPNUM|Number Of Auxiliary Snapshot Inputs<br>Indicates the number of auxiliary snapshot inputs.<br>000b - No auxiliary input (0)<br>001b - 1<br>010b - 2<br>011b - 3<br>100b - 4<br>101b - Reserved|
|27<br>—|Reserved|
|26-24<br>PPSOUTNUM|Number Of PPS Outputs<br>Indicates the number of PPS outputs.<br>000b - No PPS output (0)<br>001b - 1<br>010b - 2<br>011b - 3<br>100b - 4|
||101b - Reserved|
|23-22<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3055 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|21-18|Number Of DMA Transmit Channels|
|TXCHCNT|Indicates the number of DMA transmit channels.|
||0000b - 1<br>0001b - 2<br>0010b - 3<br>0011b - 4<br>0100b - 5<br>0101b - 6<br>0110b - 7|
||0111b - 8|
|17-16<br>—|Reserved|
|15-12|Number Of DMA Receive Channels|
|RXCHCNT|Indicates the number of DMA receive channels.<br>0000b - 1<br>0001b - 2<br>0010b - 3|
||0011b - 4|
||0100b - 5|
||0101b - 6<br>0110b - 7|
||0111b - 8|
|11-10<br>—|Reserved|
|9-6<br>TXQCNT|Number Of MTL Transmit Queues<br>Indicates the number of MTL transmit queues.<br>0000b - 1<br>0001b - 2<br>0010b - 3|
||0011b - 4<br>0100b - 5|
||0101b - 6|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3056 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0110b - 7<br>0111b - 8|
|5-4<br>—|Reserved|
|3-0|Number Of MTL Receive Queues|
|RXQCNT|Indicates the number of MTL receive queues.<br>0000b - 1|
||0001b - 2|
||0010b - 3|
||0011b - 4|
||0100b - 5|
||0101b - 6|
||0110b - 7|
||0111b - 8|



### 74.7.40 MAC Hardware Feature 3 (MAC_HW_Feature3) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_HW_Feature3|128h|



##### Function 

Indicates the presence of the fourth set of optional features or functions of the module. You can use this register to dynamically enable or disable the programs related to these features. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3057 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3058-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>TBSS FPES ESTS<br>R ASP  ESTWID  ESTDEP<br>EL  EL  EL<br>Reserved  Reserved<br>W<br>Reset 0 0 1 0 1 1 0 0 0 0 1 1 0 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>FRPS PDUP DVLA CBTIS<br>R FRPES  FRPBS  NRVF<br>Reserv EL  SEL  N  EL  Reserv<br>Reserved<br>ed  ed<br>W<br>Reset 0 0 0 0 1 1 1 0 0 0 1 1 0 0 0 1<br>Fields<br>Field Function<br>31-30 Reserved<br>—<br>29-28 Automotive Safety Package<br>ASP Indicates the encoding for the different automotive safety features.<br>00b - No safety features selected<br>01b - Only "ECC protection for external memory" feature is selected<br>10b - All the safety features are selected without the "parity port enable for external interface"<br>feature<br>11b - All the safety features are selected with the "parity port enable for external interface" feature<br>27 Time-Based Scheduling Feature<br>TBSSEL Indicates whether the time-based scheduling feature is selected.<br>This field becomes 1 if you select the option that enables the time-based scheduling feature.<br>0b - Selected<br>1b - Selected<br>26 Frame Preemption Feature<br>FPESEL Indicates whether the feature that enables frame preemption is selected.<br>This field becomes 1 if you select the "enable frame preemption" option.<br>0b - Not selected<br>1b - Selected<br>25-22 Reserved<br>—<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3058 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|21-20|Estimated Time Interval Width|
|ESTWID|Indicates the width configured for the time interval field in the gate control list.<br>00b - Width not configured<br>01b - 16 bits<br>10b - 20 bits<br>11b - 24 bits|
|19-17<br>ESTDEP|Depth Of Gate Control List<br>Indicates the depth of gate control list expressed as Log 2 (DWC_EQOS_EST_DEP) - 5.<br>000b - No depth configured<br>001b - 64 bytes<br>010b - 128 bytes<br>011b - 256 bytes<br>100b - 512 bytes<br>101b - 1024 bytes<br>110b - Reserved|
|16|Enhancements To Scheduling Traffic Feature|
|ESTSEL|Indicates whether the "enhancements to scheduling traffic" feature is selected.<br>This field becomes 1 if you select the "enable enhancements to scheduling traffic" option.<br>0b - Not selected<br>1b - Selected|
|15<br>—|Reserved|
|14-13<br>FRPES|Flexible Receive Parser Table Entry Size<br>Indicates the maximum number of parser entries that the flexible receive parser supports.<br>00b - 64<br>01b - 128<br>10b - 256<br>11b - Reserved|
|12-11<br>FRPBS|Flexible Receive Parser Buffer Size<br>Indicates the maximum number of packet data bytes that the flexible receive parser supports.<br>00b - 64<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3059 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function<br>01b - 128<br>10b - 256<br>11b - Reserved|
|---|---|
|10<br>FRPSEL|Flexible Receive Parser Feature<br>Indicates whether the flexible receive parser feature is selected.<br>This field becomes 1 if you select the "enable flexible programmable receive parser" option.<br>0b - Not selected<br>1b - Selected|
|9<br>PDUPSEL|Broadcast/Multicast Packet Duplication Feature<br>Indicates whether the broadcast or multicast duplication feature is selected.<br>This field becomes 1 if you select the "broadcast or multicast packet duplication" option.<br>0b - Not selected<br>1b - Selected|
|8-6<br>—|Reserved|
|5<br>DVLAN|Double VLAN Tag Processing Feature<br>Indicates whether the double VLAN processing feature is selected.<br>0b - Not selected<br>1b - Selected|
|4<br>CBTISEL|Queue/Channel Based VLAN Tag Insertion On Transmit Feature<br>Indicates whether the "queue- or channel-based VLAN tag insertion on Tx" feature is selected.<br>This field becomes 1 if you select the "enable queue- or channel-based VLAN tag insertion on Tx" option.<br>0b - Not selected<br>1b - Selected|
|3|Reserved|
|—<br>2-0<br>NRVF|Number Of Extended VLAN Tag Filters<br>Indicates the number of selected extended VLAN tag filters.<br>000b - No filters (0)<br>001b - 4<br>010b - 8|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3060 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||011b - 16|
||100b - 24|
||101b - 32|
||110b - Reserved|



### 74.7.41 MAC DPP FSM Interrupt Status (MAC_DPP_FSM_Interrupt_Status) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_DPP_FSM_Interru|140h|
|pt_Status||



##### Function 

Contains the status of automative-safety related data path parity errors, interface timeout errors, FSM state parity errors, and FSM state timeout errors. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3061-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>FSMP MSTT<br>R<br>ES  Reserv ES<br>Reserved  Reserved<br>ed<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>ARPE MTSP RDPE<br>R PTES  ATES  RTES  TTES  MPES<br>Reserv Reserv Reserv Reserv Reserv Reserv S  ES  S  Reserv Reserv<br>ed  ed  ed  ed  ed  ed  ed  ed<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-25|Reserved|
|—||
|24|FSM State Parity Error Status|
|FSMPES|Indicates whether a parity error is detected on one of the FSM state registers.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3061 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Field|Function<br>After a read operation, the field's value clears to 0.<br>0b - Not detected<br>1b - Detected|
|---|---|
|23-18<br>—|Reserved|
|17<br>—|Reserved|
|16<br>MSTTES|Master Read Or Write Timeout Error Status<br>Indicates whether an application or CSR timeout error is detected on the master (AXI, AHB, ARI, or<br>ATI) interface.<br>After a read operation, the field's value clears to 0.<br>0b - Not detected<br>1b - Detected|
|15<br>—|Reserved|
|14<br>—|Reserved|
|13<br>—|Reserved|
|12<br>PTES|PTP FSM Timeout Error Status<br>Indicates whether one of the PTP FSM timeout errors is detected.<br>After a read operation, the field's value clears to 0.<br>0b - Not detected<br>1b - Detected|
|11<br>ATES|APP FSM Timeout Error Status<br>Indicates whether one of the APP FSM timeout errors is detected.<br>After a read operation, the field's value clears to 0.<br>0b - Not detected<br>1b - Detected|
|10<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3062 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|9<br>RTES|Receive FSM Timeout Error Status<br>Indicates whether one of the receive FSM timeout errors is detected.<br>After a read operation, the field's value clears to 0.<br>0b - Not detected<br>1b - Detected|
|8<br>TTES|Transmit FSM Timeout Error Status<br>Indicates whether one of the transmit FSM timeout errors is detected.<br>After a read operation, the field's value clears to 0.<br>0b - Not detected<br>1b - Detected|
|7<br>—|Reserved|
|6<br>—|Reserved|
|5<br>ARPES|Application Receive Interface Data Path Parity Error Status<br>Indicates whether the parity checker detected a parity error on the application receive interface (or on PC6<br>as shown in the transmit data path parity protection diagram).<br>After a read operation, the field's value clears to 0.<br>0b - Not detected<br>1b - Detected|
|4<br>MTSPES|MTL Transmit Status Data Path Parity Checker Error Status<br>Indicates whether the parity checker detected a parity error for the MTL transmit status data on ATI (or on<br>PC5 as shown in the transmit data path parity protection diagram).<br>After a read operation, the field's value clears to 0.<br>0b - Not detected<br>1b - Detected|
|3<br>MPES|MTL Data Path Parity Checker Error Status<br>Indicates whether the parity checker detected a parity error on the MTL transmit write controller interface (or<br>on PC4 as shown in the transmit data path parity protection diagram).<br>After a read operation, the field's value clears to 0.<br>0b - Not detected<br>1b - Detected|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3063 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|2|Read Descriptor Parity Checker Error Status|
|RDPES|Indicates whether the parity checker detected a parity error on the DMA read descriptor interface (or on PC3<br>as shown in the transmit data path parity protection diagram).<br>After a read operation, the field's value clears to 0.<br>0b - Not detected<br>1b - Detected|
|1|Reserved|
|—||
|0<br>—|Reserved|



### 74.7.42 MAC FSM Control (MAC_FSM_Control) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_FSM_Control|148h|



##### Function 

Is used to control the FSM state parity and timeout error injection in Debug mode. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3064-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserv Reserv Reserv PLGR ALGR Reserv RLGR TLGR Reserv Reserv Reserv Reserv<br>PPEIN  APEIN  RPEIN  TPEIN<br>W ed  ed  ed  NML  NML  ed  NML  NML  ed  ed  ed  ed<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserv Reserv Reserv Reserv PRTY TMOU<br>PTEIN  ATEIN  RTEIN  TTEIN  Reserved<br>W ed  ed  ed  ed  EN  TEN<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field<br>Function|
|---|
|31<br>Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3064 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|—<br>30<br>—|Reserved|
|29<br>—|Reserved|
|28<br>PLGRNML|PTP Large Or Normal Mode Select<br>Indicates which mode of tic generation is used for the PTP domain.<br>0b - Normal mode<br>1b - Large mode|
|27<br>ALGRNML|APP Large Or Normal Mode Select<br>Indicates which mode of tic generation is used for the APP domain.<br>0b - Normal mode<br>1b - Large mode|
|26<br>—|Reserved|
|25<br>RLGRNML|Receive Large Or Normal Mode Select<br>Indicates which mode of tic generation is used for the receive domain.<br>0b - Normal mode<br>1b - Large mode|
|24<br>TLGRNML|Transmit Large Or Normal Mode Select<br>Indicates which mode of tic generation is used for the transmit domain.<br>0b - Normal mode<br>1b - Large mode|
|23<br>—|Reserved|
|22<br>—|Reserved|
|21<br>—|Reserved|
|20|PTP FSM Parity Error Injection|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3065 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|PPEIN|Indicates the status of error injection for PTP FSM parity.<br>0b - Disabled<br>1b - Enabled|
|19<br>APEIN|APP FSM Parity Error Injection<br>Indicates the status of error injection for APP FSM parity.<br>0b - Disabled<br>1b - Enabled|
|18<br>—|Reserved|
|17<br>RPEIN|Receive FSM Parity Error Injection<br>Indicates the status of error injection for receive FSM parity.<br>0b - Disabled<br>1b - Enabled|
|16<br>TPEIN|Transmit FSM Parity Error Injection<br>Indicates the status of error injection for transmit FSM parity.<br>0b - Disabled<br>1b - Enabled|
|15<br>—|Reserved|
|14<br>—|Reserved|
|13<br>—|Reserved|
|12<br>PTEIN|PTP FSM Timeout Error Injection<br>Indicates the status of error injection for PTP FSM timeout.<br>0b - Disabled<br>1b - Enabled|
|11<br>ATEIN|APP FSM Timeout Error Injection<br>Indicates the status of APP FSM timeout error injection.<br>0b - Disabled<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3066 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - Enabled|
|10<br>—|Reserved|
|9<br>RTEIN|Receive FSM Timeout Error Injection<br>Indicates the status of receive FSM timeout error injection.<br>0b - Disabled<br>1b - Enabled|
|8<br>TTEIN|Transmit FSM Timeout Error Injection<br>Indicates the status of transmit FSM timeout eror injection.<br>0b - Disabled<br>1b - Enabled|
|7-2<br>—|Reserved|
|1<br>PRTYEN|Parity Enable<br>Indicates whether the FSM parity feature is enabled.<br>0b - Disabled<br>1b - Enabled|
|0<br>TMOUTEN|Time Out Enable<br>Indicates the status of the FSM timeout feature.<br>0b - Disabled<br>1b - Enabled|



### 74.7.43 MAC FSM ACT Timer (MAC_FSM_ACT_Timer) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_FSM_ACT_Timer|14Ch|



##### Function 

Is used to select the FSM and interface timeout values. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3067 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3068-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved  LTMRMD  NTMRMD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>Reserved  TMR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-24|Reserved|
|—||
|23-20|Large Mode Timeout Value|
|LTMRMD|Provides the timeout duration value to be used for large mode FSM and other interface timeouts.<br>0000b - Timer disabled<br>0001b - 1 us<br>0010b - 1.024 ms (~4 ms)<br>0011b - 16.384 ms (~16 ms)|
||0100b - 65.536 ms (~64 ms)<br>0101b - 262.144 ms (~256 ms)<br>0110b - 1.048 sec (~1 sec)<br>0111b - 4.194 sec (~4sec)<br>1000b - 16.777 sec (~16 sec)<br>1001b - 33.554 sec (~32 sec)<br>1010b - 67.108 sec (~64 sec)<br>1011b - Reserved|
|19-16|Normal Mode Timeout Value|
|NTMRMD|Provides the timeout duration value to be used for normal mode FSM and other interface timeouts.<br>0000b - Timer disabled<br>0001b - 1 us<br>0010b - 1.024 ms (~4 ms)|
||0011b - 16.384 ms (~16 ms)|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3068 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0100b - 65.536 ms (~64 ms)<br>0101b - 262.144 ms (~256 ms)<br>0110b - 1.048 sec (~1 sec)<br>0111b - 4.194 sec (~4 sec)<br>1000b - 16.777 sec (~16 sec)<br>1001b - 33.554 sec (~32 sec)<br>1010b - 67.108 sec (~64 sec)<br>1011b - Reserved|
|15-10<br>—|Reserved|
|9-0|CSR Clocks For 1 µs Tic|
|TMR|Indicates the number of CSR clocks required to generate 1 µs tic.|



### 74.7.44 SCS_REG 1 (SCS_REG1) 

##### Offset 

|Register|Offset|
|---|---|
|SCS_REG1|150h|



##### Function 

Is an NXP-reserved register for internal use. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||MAC_|SCS1||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||MAC_|SCS1||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3069 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Fields 

|Field|Function|
|---|---|
|31-0|MAC SCS 1|
|MAC_SCS1|Is reserved for NXP internal use.|
||The value of this field must always be 0 unless NXP instructs you otherwise. Writing 1 to any of the bits of<br>this field might cause expected chip behavior.|



### 74.7.45 MAC MDIO Address (MAC_MDIO_Address) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_MDIO_Address|200h|



##### Function 

Controls the management cycles to external PHY through a management interface. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3070-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved  PSE  BTB  PA  RDA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserv GOC_ GOC_<br>NTC  CR  Reserved  SKAP  C45E  GB<br>W ed  1  0<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-28|Reserved|
|—||
|27|Preamble Suppression Enable|
|PSE|Indicates the status of preamble suppression.|
||• If this field is 1,SMAsuppresses the 32-bit preamble and transmits MDIO frames with only 1<br>preamble bit.|
||• If this field is 0, the MDIO frame always includes 32 bits of preamble as defined in the IEEE<br>specification.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3070 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function<br>0b - Disabled<br>1b - Enabled|
|---|---|
|26<br>BTB|Back-To-Back Transactions<br>Indicates the status of back-to-back transactions.<br>When BTB = 1 and NTC > 0, MAC indicates the completion of a read or write command at the end of a<br>frame transfer (before the trailing clocks are transmitted). Therefore, you can initiate the next command,<br>and that command executes immediately irrespective of the number of trailing clocks generated for the<br>previous frame.<br>When BTB = 0, the read or write command completes (GB = 0) only after the trailing clocks generate. In this<br>mode, you must ensure that:<br>• NTC is always generated after each frame.<br>• BTB must not be equal to 1 when NTC = 0.<br>0b - Disabled<br>1b - Enabled|
|25-21<br>PA|Physical Layer Address<br>Indicates whether MAC accesses clause 22 PHY devices (out of 32) or clause 45 capable PHYs (out of 32).|
|20-16<br>RDA|Register Or Device Address<br>Indicates whether MAC accesses clause 22 PHY devices (out of 32) or clause 45 capable PHYs (out of 32).|
|15<br>—|Reserved|
|14-12<br>NTC|Number Of Trailing Clocks<br>Controls the number of trailing clock cycles generated on the gmii_mdc_o (MDC) signal after the end of<br>MDIO frame transmission. The valid values can range from 0 to 7.<br>Writing 3h to this field indicates that there are additional three clock cycles on the MDC line after the end of<br>MDIO frame transfer.|
|11-8<br>CR|CSR Clock Range<br>Determines the frequency of the MDC clock according to the CSR clock frequencies used in your design:<br>• 0000: CSR clock = 60-100 MHz; MDC clock = CSR clock/42<br>• 0001: CSR clock = 100-150 MHz; MDC clock = CSR clock/62<br>• 0010: CSR clock = 20-35 MHz; MDC clock = CSR clock/16<br>• 0011: CSR clock = 35-60 MHz; MDC clock = CSR clock/26<br>• 0100: CSR clock = 150-250 MHz; MDC clock = CSR clock/102|
||• 0101: CSR clock = 250-300 MHz; MDC clock = CSR clock/124|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3071 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||• 0110: CSR clock = 300-500 MHz; MDC clock = CSR clock/204<br>• 0111: CSR clock = 500-800 MHz; MDC clock = CSR clock/324<br>When bit 3 of this field is 0, the suggested CSR clock-frequency range applicable to each value ensures that<br>the MDC clock frequency is approximately between 1.0  MHz and 2.5 MHz.<br>When bit 3 of this field is 1, you can achieve a higher MDC clock frequency than the IEEE 802.3 frequency<br>limit of 2.5 MHz, and program a clock divider of a lower value. For example, if the CSR clock frequency is<br>100 MHz and you write 1010 to this field, the resultant MDC clock frequency equals 12.5 MHz, which is<br>above the range specified in IEEE 802.3. Program these values only if the interfacing chips support faster<br>MDC clocks:<br>• 1000: CSR clock/4<br>• 1001: CSR clock/6<br>• 1010: CSR clock/8<br>• 1011: CSR clock/10<br>• 1100: CSR clock/12<br>• 1101: CSR clock/14<br>• 1110: CSR clock/16<br>• 1111: CSR clock/18<br>These bits are not used for accessing RevMII. They are read-only if the RevMII interface is selected as a<br>single PHY interface.|
|7-5<br>—|Reserved|
|4<br>SKAP|Skip Address Packet<br>Indicates the status of the skip address packet.<br>If this field is 1, SMA does not send the address packets before read, write, or post-read increment address<br>packets. This field is valid only when C45E = 1.<br>0b - Disabled<br>1b - Enabled|
|3<br>GOC_1|GMII Operation Command 1<br>Indicates the status of GMII operation command 1.<br>GMII operation command 1 represents the higher bit of the operation command to PHY or RevMII. The fields<br>GOC_1 and GOC_O indicate these values:<br>• 00: Reserved<br>• 01: Write<br>• 10: Post-read increment address for clause 45 PHY<br>• 11: Read|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3072 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function<br>When clause 22 PHY or RevMII is enabled, only write and read commands are valid.<br>0b - Disabled<br>1b - Enabled|
|---|---|
|2|GMII Operation Command 0|
|GOC_0|Indicates the status of GMII operation command 0.<br>GMII operation command 0 represents the lower bit of the operation command to PHY or RevMII. When in<br>SMA mode (MDIO master), this field, along with the GOC_1 field, determines the operation to be performed<br>to PHY.<br>This field is read-only and tied to 1 when only RevMII is selected in configuration.<br>0b - Disabled<br>1b - Enabled|
|1<br>C45E|Clause 45 PHY Enable<br>Indicates the status of clause 45 PHY.<br>• If this field is 1, clause 45 capable PHY is connected to MDIO.<br>• If this field is 0, clause 22 capable PHY is connected to MDIO.<br>0b - Disabled<br>1b - Enabled|
|0<br>GB|GMII Busy<br>Indicates the status of GMII busy.<br>Writing 1 to this field instructs SMA to initiate a read or write access to the MDIO slave. MAC writes 0 to the<br>field after the MDIO frame transfer is complete. Therefore, you must not write or change any of the fields in<br>the MAC_MDIO_Address and MAC_MDIO_Data registers as long as the value of this field is 1.<br>For write transfers, before writing 1 to this field, you must write a 16-bit data toMAC_MDIO_Data[GD]and<br>MAC_MDIO_Data[RA]if C45E = 1.<br>If C45E = 1, you must also write toMAC_MDIO_Data[RA]before initiating a read transfer.<br>After a read transfer completes (GB = 0), a data read from the PHY register is valid<br>inMAC_MDIO_Data[GD].<br>Even if the addressed PHY is not present, there is no change in the functionality of this field.<br>~~NOTE~~<br>Access restrictions apply to this field. It clears automatically and writing 0 to it has no effect.<br>0b - Disabled<br>1b - Enabled|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3073 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

### 74.7.46 MAC MDIO Data (MAC_MDIO_Data) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_MDIO_Data|204h|



##### Function 

Is used to store the write data to be written to the PHY register located at the address specified in MAC MDIO Address (MAC_MDIO_Address). This register also stores the read data from the PHY register located at the address that MAC MDIO Address (MAC_MDIO_Address) specifies. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3074-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>RA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>GD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16|Register Address|
|RA|Contains the PHY register address intended for the MDIO frame.|
||This field is valid only whenMAC_MDIO_Address[C45E]= 1.|
|15-0|GMII Data|
|GD|Contains the 16-bit data value read from PHY or RevMII after a management read operation or the 16-bit<br>data value to be written to PHY or RevMII before a management write operation.|



### 74.7.47 MAC CSR Software Control (MAC_CSR_SW_Ctrl) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_CSR_SW_Ctrl|230h|



##### Function 

Contains software programmable controls for changing the CSR access response and clearing the status bits on read. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3074 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3075-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>Reserved  SEEN  Reserved  RCWE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-9|Reserved|
|—<br>8|Slave Error Response Enable|
|SEEN|Indicates the status of the slave error response.<br>• If this field is 1, MAC responds with a slave error for accesses to reserved registers in the CSR<br>space.<br>• If this field is 0, MAC sends an "okay" response to registers accessed from the CSR space.<br>0b - Disabled<br>1b - Enabled|
|7-1<br>—|Reserved|
|0|Enable Register Write 1 To Clear (W1C)|
|RCWE|Enables and disables the W1C feature for some registers.<br>When this field is 1, the access mode of some of the other fields changes from R2C to W1C.<br>When this field is 0, the access mode of those fields remains R2C.<br>0b - Disabled<br>1b - Enabled|



### 74.7.48 MAC FPE Control STS (MAC_FPE_CTRL_STS) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_FPE_CTRL_STS|234h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3075 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Function 

Controls the operation of frame preemption. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||Rese|rved||||||TRSP|TVER|RRSP|RVER|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||Rese|rved||||||S1_SE<br>T_0|SRSP|SVER|EFPE|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-20|Reserved|
|—<br>19|Transmitted Respond Frame|
|TRSP|Indicates whether the respond frame is transmitted.<br>This field becomes 1 when a respond frame is transmitted (triggered by writing 1 to the SRSP field). An<br>interrupt can be generated for this event if you write 1 toMAC_Interrupt_Enable[FPEIE].<br>Access restrictions apply to this field. TRSP becomes a W1C field whenMAC_CSR_SW_Ctrl[RCWE]=<br>1, and becomes an R2C field whenMAC_CSR_SW_Ctrl[RCWE]= 0. Thus, TRSP becomes 0 sometimes<br>when you read it and sometimes when you write 1 to it. It automatically becomes 1 on an internal event.<br>0b - Not transmitted<br>1b - Transmitted|
|18|Transmitted Verify Frame|
|TVER|Indicates whether the verify frame is transmitted.<br>This field becomes 1 when a verify frame is transmitted (triggered by writing 1 to the SVER field). An interrupt<br>can be generated for this event if you write 1 toMAC_Interrupt_Enable[FPEIE].<br>Access restrictions apply to this field. The field clears on read or write of 1 when<br>MAC_CSR_SW_Ctrl[RCWE]= 1. It automatically becomes 1 on an internal event.<br>0b - Not transmitted<br>1b - Transmitted|
|17|Received Respond Frame|
|RRSP|Indicates whether the respond frame is received.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3076 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function<br>This field becomes 1 when a respond frame is received. An interrupt can be generated for this event if you<br>write 1 toMAC_Interrupt_Enable[FPEIE].<br>Access restrictions apply to this field. The field clears on read or write of 1 when<br>MAC_CSR_SW_Ctrl[RCWE]= 1. It automatically becomes 1 on an internal event.<br>0b - Not received<br>1b - Received|
|---|---|
|16<br>RVER|Received Verify Frame<br>Indicates whether the verify frame is received.<br>This field becomes 1 when a verify frame is received. An interrupt can be generated on the transmission of<br>a packet if you write 1 toMAC_Interrupt_Enable[FPEIE].<br>Access restrictions apply to this field. The field clears on read or write of 1 when<br>MAC_CSR_SW_Ctrl[RCWE]= 1. It automatically becomes 1 on an internal event.<br>0b - Not received<br>1b - Received|
|15-4<br>—|Reserved|
|3<br>S1_SET_0|S1 SET 0<br>Is reserved for NXP internal use and must always be 0 unless instructed by NXP. Writing 1 to this field may<br>cause unexpected behavior.|
|2<br>SRSP|Send Respond mPacket<br>Indicates the status of the send respond mPacket.<br>If this field is 1, it indicates the hardware to send a respond mPacket. The hardware resets the field after<br>sending the respond mPacket.<br>Access restrictions apply to this field. It clears automatically and writing 0 to it has no effect.<br>0b - Disabled<br>1b - Enabled|
|1<br>SVER|Send Verify mPacket<br>Enables and disables the sending of a verify mPacket.<br>Write 1 to this field to command EMAC to send a verify mPacket. EMAC writes 0 to this field after sending<br>the verify mPacket.<br>Access restrictions apply to this field. It clears automatically and writing 0 to it has no effect.<br>0b - Disabled<br>1b - Enabled|
|0|Enable Transmit Frame Preemption|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3077 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|EFPE|Enables or disables the frame preemption transmit functionality.|
||0b - Disabled|
||1b - Enabled|



### 74.7.49 MAC Presentation Time (MAC_Presn_Time_ns) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Presn_Time_ns|240h|



##### Function 

Contains the 32-bit binary rollover equivalent time of the PTP system time (in nanoseconds) and exists when DWC_EQOS_FLEXI_PPS_OUT_EN is configured. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3078-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R MPTN<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R MPTN<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|MAC 1722 Presentation Time (In Nanoseconds)|
|MPTN|Indicates the value of the 32-bit binary rollover equivalent time of the PTP System Time (in ns).|



### 74.7.50 MAC Presentation Time Update (MAC_Presn_Time_Updt) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Presn_Time_Updt|244h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3078 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Function 

Holds the 32-bit value of MAC 1722 presentation time (in ns), which must be added to the current presentation time counter value. Initialization happens when MAC_Timestamp_Control[TSINIT] = 1, and an update happens when MAC_Timestamp_Control[TSUPDT] = 1. 

Exists when DWC_EQOS_FLEXI_PPS_OUT_EN is configured. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||MP|TU||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||MP|TU||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-0|MAC 1722 Presentation Time Update|
|MPTU|Holds the initial value or the update value for the presentation time. When used for an update, this<br>field holds the 32-bit value (in ns), which must be added to the current presentation time counter<br>value. Initialization happens whenMAC_Timestamp_Control[TSINIT]= 1, and an update happens when<br>MAC_Timestamp_Control[TSUPDT]= 1.|
||WhenMAC_System_Time_Nanoseconds_Update[ADDSUB]= 1, this value is directly used for subtraction.|



### 74.7.51 MAC Address 0 High (MAC_Address0_High) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Address0_High|300h|



##### Function 

Holds the upper 16 bits of the first 6-byte MAC address of the station. 

The first DA byte that is received on the (G)MII interface corresponds to the LS byte (bits [7:0]) of MAC Address 0 Low (MAC_Address0_Low). For example, if 112233445566h is received (11h in lane 0 of the first column) on (G)MII as the destination address, MAC Address 0 Low (MAC_Address0_Low)[47:0] is compared to 665544332211h. 

If MAC address registers are configured to be double-synchronized with the (G)MII clock domains, the synchronization is triggered only when bits [31:24] (in Little-Endian mode) or bits [7:0] (in Big-Endian mode) of MAC Address 0 Low (MAC_Address0_Low) are written to. For proper synchronization updates, the consecutive writes to MAC Address 0 Low (MAC_Address0_Low) must be performed after at least four clock cycles in the destination clock domain. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3079 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|AE|||||||Reserved|||||||DCS|
|Reset|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R<br>W||||||||ADD|RHI|||||||
|Reset|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1<br>1|



##### Fields 

|Field|Function|
|---|---|
|31|Address Enable|
|AE|Enables MAC address<br>0b - Disabled and invalid (the field's value must always be 1)<br>1b - Enabled|
|30-18<br>—|Reserved|
|17-16<br>DCS|DMA Channel Select<br>IfMAC_Ext_Configuration[PDC]= 0, this field contains the binary representation of the DMA channel<br>number to which a receive packet whose DA matchesMAC Address 0 Low (MAC_Address0_Low)content<br>is routed.<br>IfMAC_Ext_Configuration[PDC]= 1, this field contains the one-hot representation of one or more DMA<br>channel numbers to which a receive packet whose DA matchesMAC Address 0 Low (MAC_Address0_Low)<br>content is routed.|
|15-0<br>ADDRHI|MAC Address 0 [47:32]<br>Contains the upper 16 bits [47:32] of the first 6-byte MAC address.<br>MAC uses this field for filtering the received packets and inserting the MAC address in the transmit flow<br>control (pause) packets.|



### 74.7.52 MAC Address 0 Low (MAC_Address0_Low) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Address0_Low|304h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3080 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Function 

Holds the lower 32 bits of the 6-byte first MAC address of the station. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3081-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>ADDRLO<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>ADDRLO<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|MAC Address 0 [31:0]|
|ADDRLO|Contains the lower 32 bits of the first 6-byte MAC address. MAC uses this field to filter the received packets<br>and insert the MAC address in the transmit flow control (pause) packets.|



### 74.7.53 MAC Address 1 High (MAC_Address1_High) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Address1_High|308h|



##### Function 

Holds the upper 16 bits of the second 6-byte MAC address of the station. 

If the MAC address registers are configured to be double-synchronized with the (G)MII clock domains, the synchronization is triggered only when bits [31:24] (in Little-Endian mode) or bits [7:0] (in Big-Endian mode) of MAC Address 1 Low (MAC_Address1_Low) are written to. For proper synchronization updates, the consecutive writes to MAC Address 1 Low (MAC_Address1_Low) must be performed after at least four clock cycles in the destination clock domain. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3081 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3082-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>AE  SA  MBC  Reserved  DCS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>ADDRHI<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Address Enable|
|AE|Indicates whether the MAC address is enabled or ignored.<br>If this field is 1, the address filter module uses the second MAC address for perfect filtering. If this field is 0,<br>the address filter module ignores the address used for filtering.<br>0b - Ignored<br>1b - Enabled|
|30|Source Address|
|SA|Indicates whether the MAC address is compared to the source or destination address.<br>If this field is 1, MAC Address 1[47:0] is compared to the SA fields of the received packet. If this field is 0,<br>MAC Address 1[47:0] is compared to the DA fields of the received packet.<br>0b - Destination address<br>1b - Source address|
|29-24<br>MBC|Mask Byte Control<br>Contains mask control bits for comparing each of the MAC address bytes. If this field is 1, MAC does not<br>compare the corresponding byte of the received DA or SA with the contents of the MAC address 1 registers.<br>Each bit controls the masking of the bytes as follows:<br>• Bit 29: MAC Address 1 High[15:8]<br>• Bit 28: MAC Address 1 High[7:0]<br>• Bit 27: MAC Address 1 Low[31:24]<br>• - ..<br>• Bit 24: MAC Address 1 Low[7:0]<br>You can filter a group of addresses (known as group address filtering) by masking one or more bytes of<br>the address.|
|23-18|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3082 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|17-16|DMA Channel Select|
|DCS|IfMAC_Ext_Configuration[PDC]= 0, this field contains the binary representation of the DMA channel<br>number to which a receive packet whose DA matchesMAC Address 1 Low (MAC_Address1_Low)content<br>is routed.|
||IfMAC_Ext_Configuration[PDC]= 1, this field contains the one-hot representation of one or more<br>DMA Channel numbers to which a receive packet whose DA matchesMAC Address 1 Low<br>(MAC_Address1_Low)content is routed.|
|15-0|MAC Address 1 [47:32]|
|ADDRHI|Contains the upper 16 bits [47:32] of the second 6-byte MAC address.|



### 74.7.54 MAC Address 1 Low (MAC_Address1_Low) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Address1_Low|30Ch|



##### Function 

Holds the lower 32 bits of the second 6-byte MAC address of the station. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||ADD|RLO||||||||
|Reset|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||ADD|RLO||||||||
|Reset|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|



##### Fields 

|Field|Function|
|---|---|
|31-0|MAC Address 1 [31:0]|
||Contains the lower 32 bits of the second 6-byte MAC address.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3083 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

|Field|Function|
|---|---|
|ADDRLO|The contents of this field are undefined until you load them after the initialization process.|



### 74.7.55 MAC Address 2 High (MAC_Address2_High) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Address2_High|310h|



##### Function 

Holds the upper 16 bits of the second 6-byte MAC address of the station. 

If the MAC address registers are configured to be double-synchronized with the (G)MII clock domains, the synchronization is triggered only when bits [31:24] (in Little-Endian mode) or bits [7:0] (in Big-Endian mode) of MAC Address 1 Low (MAC_Address1_Low) are written to. For proper synchronization updates, the consecutive writes to MAC Address 1 Low (MAC_Address1_Low) must be performed after at least four clock cycles in the destination clock domain. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|AE|SA|||MB|C|||||Rese|rved|||DCS|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R<br>W||||||||ADD|RHI|||||||
|Reset|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1<br>1|



##### Fields 

|Field|Function|
|---|---|
|31|Address Enable|
|AE|Indicates whether the MAC address is enabled or ignored.|
||If this field is 1, the address filter module uses the second MAC address for perfect filtering. If this field is 0,<br>the address filter module ignores the address for filtering.|
||0b - Ignored|
||1b - Enabled|
|30|Source Address|
|SA|Indicates whether the MAC address is compared to the source or destination address.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3084 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||If this field is 1, MAC Address 1[47:0] is compared to the SA fields of the received packet. If this field is 0,<br>MAC Address 1[47:0] is compared to the DA fields of the received packet.<br>0b - Destination address<br>1b - Source address|
|29-24<br>MBC|Mask Byte Control<br>Contains mask control bits for comparing each of the MAC address bytes. If this field is 1, MAC does not<br>compare the corresponding byte of the received DA or SA with the contents of MAC address 1 registers.<br>Each bit controls the masking of the bytes as follows:<br>• Bit 29: MAC Address 1 High[15:8]<br>• Bit 28: MAC Address 1 High[7:0]<br>• Bit 27: MAC Address 1 Low[31:24]<br>• - ..<br>• Bit 24: MAC Address 1 Low[7:0]<br>You can filter a group of addresses (known as group address filtering) by masking one or more bytes of<br>the address.|
|23-18<br>—|Reserved|
|17-16<br>DCS|DMA Channel Select<br>IfMAC_Ext_Configuration[PDC]= 0, this field contains the binary representation of the DMA channel<br>number to which a receive packet whose DA matchesMAC Address 2 Low (MAC_Address2_Low)content<br>is routed.<br>IfMAC_Ext_Configuration[PDC]= 1, this field contains the one-hot representation of one or more<br>DMA Channel numbers to which a receive packet whose DA matchesMAC Address 2 Low<br>(MAC_Address2_Low)content is routed.|
|15-0<br>ADDRHI|MAC Address 1 [47:32]<br>Contains the upper 16 bits [47:32] of the second 6-byte MAC address.|



### 74.7.56 MAC Address 2 Low (MAC_Address2_Low) 

##### Offset 

|Register|Offset|
|---|---|
|MAC_Address2_Low|314h|



Function 

Holds the lower 32 bits of the second 6-byte MAC address of the station. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3085 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3086-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>ADDRLO<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>ADDRLO<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|MAC Address 1 [31:0]|
|ADDRLO|Contains the lower 32 bits of the second 6-byte MAC address. The content of this field remains undefined<br>until you load it after the initialization process.|



### 74.7.57 MMC Control (MMC_Control) 

##### Offset 

|Register|Offset|
|---|---|
|MMC_Control|700h|



##### Function 

##### Establishes the operating mode for MMC. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||Rese|rved||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||Reserved||||UCDB<br>C|Reser|ved|CNTP<br>RST...|CNTP<br>RST|CNTF<br>REEZ|RSTO<br>NRD|CNTS<br>TOP...|CNTR<br>ST|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3086 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Fields 

|Field|Function|
|---|---|
|31-9<br>—|Reserved|
|8<br>UCDBC|Update MMC Counters For Dropped Broadcast Packets<br>Indicates the status of MMC counters for dropped broadcast packets.<br>• If this field is 1, MAC updates all the related MMC counters for broadcast packets that are dropped<br>becauseMAC_Packet_Filter[DBF]= 1.<br>• If this field is 0, the MMC counters are not updated for dropped broadcast packets.<br>The CNTRST field has a higher priority than the CNTPRST field. Therefore, if you write 1<br>to both these fields in the same write cycle, all the counters are cleared and the CNTPRST<br>field becomes 0.<br>~~NOTE~~|
||0b - Disabled<br>1b - Enabled|
|7-6<br>—|Reserved|
|5|Full-Half Preset|
|CNTPRSTLVL|Indicates whether full-half preset is enabled or disabled.<br>• If this field is 0 and the CNTPRST field is 1, all the MMC counters are preset to the almost-half<br>value. All octet counters are preset to 7FFF_F800h (half 2 Kbytes) and all packet counters are<br>preset to 7FFF_FFF0h (half 16).<br>• If this field is 1 and the CNTPRST field is 1 too, all MMC counters are preset to the almost-full value.<br>All octet counters are preset to FFFF_F800h (full 2 Kbytes) and all packet counters are preset to<br>FFFF_FFF0h (full 16).<br>For 16-bit counters, the almost-half preset values are 7800h and 7FF0h for the respective octet and packet<br>counters. Similarly, the almost-full preset values for the 16-bit counters are 0xF800 and 0xFFF0.<br>0b - Disabled<br>1b - Enabled|
|4<br>CNTPRST|Counters Preset<br>Indicates whether MMC counter preset is enabled or disabled.<br>If this field is 1, all the counters are initialized or preset to almost full or almost half according to the settings<br>of the CNTPRSTLVL field.<br>This field clears automatically after 1 clock cycle, and along with the CNTPRSTLVL field, is useful for<br>debugging and testing the assertion of interrupts because of the MMC counter becoming half-full or full.<br>Access restrictions apply to this field, which clears automatically.<br>0b - Disabled<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3087 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - Enabled|
|3<br>CNTFREEZ|MMC Counter Freeze<br>Indicates the status of MMC counter freeze.<br>If this field is 1, the field freezes all the MMC counters to their current values.<br>Until this field becomes 0, no MMC counter is updated because of any transmitted or received packets. If<br>an MMC counter is read when RSTONRD = 1, that counter is also cleared in this mode.<br>0b - Disabled|
||1b - Enabled|
|2<br>RSTONRD|Reset On Read<br>Indicates whether the reset on read for MMC counters is enabled or disabled.<br>If this field is 1, MMC counters are reset to 0 after read (they clear automatically after reset). The counters<br>are cleared when the least significant byte lane (bits [7:0]) is read.<br>0b - Disabled|
||1b - Enabled|
|1|Counter Stop Rollover|
|CNTSTOPRO|Indicates the status of counter stop rollover.<br>If this field is 1, the counter does not roll over to 0 after reaching the maximum value.<br>0b - Disabled|
||1b - Enabled|
|0<br>CNTRST|Counters Reset<br>Indicates whether MMC counters are reset.<br>If this field is 1, all the counters are reset. This field clears automatically after 1 clock cycle.<br>Access restrictions apply to this field that clears automatically.<br>0b - Counters are not reset<br>1b - All counters are reset|



### 74.7.58 MMC Receive Interrupt (MMC_Rx_Interrupt) 

##### Offset 

|Register|Offset|
|---|---|
|MMC_Rx_Interrupt|704h|



##### Function 

Maintains the interrupts generated from all receive statistics counters when the following conditions occur: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3088 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

- Receive statistic counters reach half of their maximum values (8000_0000h for a 32-bit counter and 8000h for a 16-bit counter). 

- Receive statistic counters cross their maximum values (FFFF_FFFFh for a 32-bit counter and FFFFh for a 16-bit counter). 

If MMC_Control[CNTSTOPRO] = 1, interrupts are set but the counter remains at all-ones. This is a 32-bit register. An interrupt bit is cleared when the respective MMC counter that caused the interrupt is read. The least significant byte lane (bits [7:0]) of the respective counter must be read to clear the interrupt bit. 

~~<mark>NOTE</mark>~~ 

R_SS_RC means that this register bit is set internally, and is cleared when the counter register is read. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3089-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>RXCT RXRC RXWD RXVL RXFO RXPA RXOR RXLE RXUC RX102<br>R<br>Reserv Reserv RLP... VER... OGP... ANG... VPIS  USP... ANG... NER... GPIS  4T...<br>Reserved<br>ed  ed<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>RX512 RX256 RX128 RX65T RX64 RXOSI RXUSI RXJA RXRU RXAL RXCR RXMC RXBC RXGO RXGB RXGB<br>R<br>T1... T5... T2... 12... OCT... ZE... ZE... BER... NTP... GNE... CER... GPIS  GPIS  CTIS  OCT... PKT...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-28|Reserved|
|—||
|27|Reserved|
|—||
|26<br>—|Reserved|
|25|MMC Receive Control Packet Counter Interrupt Status|
|RXCTRLPIS|Indicates whether the status of the MMC receive control packet counter interrupt is detected.<br>This field becomes 1 when the rxctrlpackets_g counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3089 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|24<br>RXRCVERRPIS|MMC Receive Error Packet Counter Interrupt Status<br>Indicates whether the status of the MMC receive error packet counter interrupt is detected.<br>This field becomes 1 when the rxrcverror counter reaches half of its maximum value or the maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|23<br>RXWDOGPIS|MMC Receive Watchdog Error Packet Counter Interrupt Status<br>Indicates whether the status of the MMC receive watchdog error packet counter interrupt is detected.<br>This field becomes 1 when the rxwatchdog error counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|22<br>RXVLANGBPIS|MMC Receive VLAN Good Bad Packet Counter Interrupt Status<br>Indicates whether the status of the MMC receive VLAN good bad packet counter interrupt is detected.<br>This field becomes 1 when the rxvlanpackets_gb counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|21<br>RXFOVPIS|MMC Receive FIFO Overflow Packet Counter Interrupt Status<br>Indicates whether the status of the MMC receive FIFO overflow packet counter interrupt is detected.<br>This field becomes 1 when the rxfifooverflow counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|20<br>RXPAUSPIS|MMC Receive Pause Packet Counter Interrupt Status<br>Indicates whether the status of the MMC receive pause packet counter interrupt is detected.<br>This field becomes 1 when the rxpausepackets counter reaches half of its maximum value or the<br>maximum value.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3090 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|19|MMC Receive Out-Of-Range Error Packet Counter Interrupt Status|
|RXORANGEPI<br>S|Indicates whether the status of the MMC receive out-of-range error packet counter interrupt is detected.<br>This field becomes 1 when the rxoutofrangetype counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|18<br>RXLENERPIS|MMC Receive Length Error Packet Counter Interrupt Status<br>Indicates whether the status of the MMC receive length error packet counter interrupt is detected.<br>This field becomes 1 when the rxlengtherror counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|17<br>RXUCGPIS|MMC Receive Unicast Good Packet Counter Interrupt Status<br>Indicates whether the status of the MMC receive unicast good packet counter interrupt is detected.<br>This field becomes 1 when the rxunicastpackets_g counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|16|MMC Receive 1024 To Maximum Octet Good Bad Packet Counter Interrupt Status|
|RX1024TMAXO<br>CTGBPIS|Indicates whether the status of the MMC receive 1024 to maximum octet good bad packet counter interrupt<br>is detected.<br>This field becomes 1 when the rx1024tomaxoctets_gb counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3091 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Not detected<br>1b - Detected|
|15|MMC Receive 512 To 1023 Octet Good Bad Packet Counter Interrupt Status|
|RX512T1023O<br>CTGBPIS|Indicates whether the status of the MMC receive 512 to 1023 octet good bad packet counter interrupt<br>is detected.<br>This field becomes 1 when the rx512to1023octets_gb counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|14|MMC Receive 256 To 511 Octet Good Bad Packet Counter Interrupt Status|
|RX256T511OC<br>TGBPIS|Indicates whether the status of the MMC receive 256 to 511 octet good bad packet counter interrupt<br>is detected.<br>This field becomes 1 when the rx256to511octets_gb counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|13|MMC Receive 128 To 255 Octet Good Bad Packet Counter Interrupt Status|
|RX128T255OC<br>TGBPIS|Indicates whether the status of the MMC receive 128 to 255 octet good bad packet counter interrupt<br>is detected.<br>This field becomes 1 when the rx128to255octets_gb counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|12|MMC Receive 65 To 127 Octet Good Bad Packet Counter Interrupt Status|
|RX65T127OCT<br>GBPIS|Indicates whether the status of the MMC receive 65 to 127 octet good bad packet counter interrupt<br>is detected.<br>The field becomes 1 when the rx65to127octets_gb counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3092 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Not detected<br>1b - Detected|
|11<br>RX64OCTGBPI<br>S|MMC Receive 64 Octet Good Bad Packet Counter Interrupt Status<br>Indicates whether the status of the MMC receive 64-octet good bad packet counter interrupt is detected.<br>The field becomes 1 when the rx64octets_gb counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|10|MMC Receive Oversize Good Packet Counter Interrupt Status|
|RXOSIZEGPIS|Indicates whether the status of the MMC receive oversize good packet counter interrupt is detected.<br>This field becomes 1 when the rxoversize_g counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|9<br>RXUSIZEGPIS|MMC Receive Undersize Good Packet Counter Interrupt Status<br>Indicates whether the status of MMC receive undersize good packet counter interrupt is detected.<br>This field becomes 1 when the rxundersize_g counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|8<br>RXJABERPIS|MMC Receive Jabber Error Packet Counter Interrupt Status<br>Indicates whether the status of MMC receive jabber error packet counter interrupt is detected.<br>This field becomes 1 when the rxjabbererror counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3093 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|7<br>RXRUNTPIS|MMC Receive Runt Packet Counter Interrupt Status<br>Indicates whether the status of the MMC receive runt packet counter interrupt is detected.<br>This field becomes 1 when the rxrunterror counter reaches half of its maximum value or the maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|6<br>RXALGNERPIS|MMC Receive Alignment Error Packet Counter Interrupt Status<br>Indicates whether the status of the MMC receive alignment error packet counter interrupt is detected.<br>This field becomes 1 when the rxalignmenterror counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|5<br>RXCRCERPIS|MMC Receive CRC Error Packet Counter Interrupt Status<br>Indicates whether the status of the MMC receive CRC error packet counter interrupt is detected.<br>This field becomes 1 when the rxcrcerror counter reaches half of its maximum value or the maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|4<br>RXMCGPIS|MMC Receive Multicast Good Packet Counter Interrupt Status<br>Indicates whether the status of the MMC receive multicast good packet counter interrupt is detected.<br>This field becomes 1 when the rxmulticastpackets_g counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|3<br>RXBCGPIS|MMC Receive Broadcast Good Packet Counter Interrupt Status<br>Indicates whether the status of the MMC receive broadcast good packet counter interrupt is detected.<br>This field becomes 1 when the rxbroadcastpackets_g counter reaches half of its maximum value or the<br>maximum value.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3094 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|2<br>RXGOCTIS|MMC Receive Good Octet Counter Interrupt Status<br>Indicates whether the status of the MMC receive good octet counter interrupt is detected.<br>This field becomes 1 when the rxoctetcount_g counter reaches half of its maximum value or its<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|1<br>RXGBOCTIS|MMC Receive Good Bad Octet Counter Interrupt Status<br>Indicates whether the status of the MMC receive good bad octet counter interrupt is detected.<br>This field becomes 1 when the rxoctetcount_gb counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|0<br>RXGBPKTIS|MMC Receive Good Bad Packet Counter Interrupt Status<br>Indicates whether the status of the MMC receive good bad packet counter interrupt is detected.<br>This field becomes 1 when the rxpacketcount_gb counter reaches half of its maximum value or its<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|



### 74.7.59 MMC Transmit Interrupt (MMC_Tx_Interrupt) 

##### Offset 

|Register|Offset|
|---|---|
|MMC_Tx_Interrupt|708h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3095 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Function 

Maintains the interrupts generated from all the transmit statistics counters. 

This register maintains those interrupts that are generated when transmit statistic counters: 

- Reach half of their maximum values (8000_0000h for a 32-bit counter and 0x8000 for a 16-bit counter) 

- Cross their maximum values (FFFF_FFFFh for a 32-bit counter and FFFFh for a 16-bit counter) 

If MMC_Control[CNTSTOPRO] = 1, the interrupts are set but the counter remains at all-ones. 

This is a 32 bit register. An interrupt bit is cleared when the respective MMC counter that caused the interrupt is read. 

The least significant byte lane (bits [7:0]) of the respective counter must be read to clear the interrupt bit. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3096-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>TXOSI TXVLA TXPA TXEX TXGP TXGO TXCA TXEX TXLAT TXDE<br>R<br>Reserv Reserv ZE... NG... USP... DEF... KTIS  CTIS  RER... COL... CO... FPIS<br>Reserved<br>ed  ed<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>TXMC TXSC TXUFL TXBC TXMC TXUC TX102 TX512 TX256 TX128 TX65T TX64O TXMC TXBC TXGB TXGB<br>R<br>OLG... OLG... OW... GBP... GBP... GBP... 4T... T1... T5... T2... 12... CT... GPIS  GPIS  PKT... OCT...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-28|Reserved|
|—||
|27|Reserved|
|—||
|26<br>—|Reserved|
|25|MMC Transmit Oversize Good Packet Counter Interrupt Status|
|TXOSIZEGPIS|Indicates whether the status of the MMC transmit oversize good packet counter interrupt is detected.<br>This field becomes 1 when the txoversize_g counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3096 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function<br>1b - Detected|
|---|---|
|24<br>TXVLANGPIS|MMC Transmit VLAN Good Packet Counter Interrupt Status<br>Indicates whether the status of the MMC transmit VLAN good packet counter interrupt is detected.<br>This field becomes 1 when the txvlanpackets_g counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|23<br>TXPAUSPIS|MMC Transmit Pause Packet Counter Interrupt Status<br>Indicates whether the status of the MMC transmit pause packet counter interrupt is detected.<br>This field becomes 1 when the txpausepacketserror counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|22<br>TXEXDEFPIS|MMC Transmit Excessive Deferral Packet Counter Interrupt Status<br>Indicates whether the status of the MMC transmit excessive deferral packet counter interrupt is detected.<br>This field becomes 1 when the txexcessdef counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|21<br>TXGPKTIS|MMC Transmit Good Packet Counter Interrupt Status<br>Indicates whether the status of the MMC transmit good packet counter interrupt is detected.<br>This field becomes 1 when the txpacketcount_g counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|20|MMC Transmit Good Octet Counter Interrupt Status|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3097 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|TXGOCTIS|Indicates whether the status of the MMC transmit good octet counter interrupt is detected.<br>This field becomes 1 when the txoctetcount_g counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|19<br>TXCARERPIS|MMC Transmit Carrier Error Packet Counter Interrupt Status<br>Indicates whether the status of the MMC transmit carrier error packet counter interrupt is detected.<br>This field becomes 1 when the txcarriererror counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|18<br>TXEXCOLPIS|MMC Transmit Excessive Collision Packet Counter Interrupt Status<br>Indicates whether the status of the MMC transmit excessive collision packet counter interrupt is detected.<br>This field becomes 1 when the txexesscol counter reaches half of its maximum value or the maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|17<br>TXLATCOLPIS|MMC Transmit Late Collision Packet Counter Interrupt Status<br>Indicates whether the status of the MMC transmit late collision packet counter interrupt is detected.<br>This field becomes 1 when the txlatecol counter reaches half of its maximum value or the maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|16<br>TXDEFPIS|MMC Transmit Deferred Packet Counter Interrupt Status<br>Indicates whether the status of the MMC transmit deferred packet counter interrupt is detected.<br>This field becomes 1 when the txdeferred counter reaches half of its maximum value or the maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3098 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function<br>0b - Not detected<br>1b - Detected|
|---|---|
|15<br>TXMCOLGPIS|MMC Transmit Multiple Collision Good Packet Counter Interrupt Status<br>Indicates whether the status of the MMC transmit multiple collision good packet counter interrupt<br>is detected.<br>This field becomes 1 when the txmulticol_g counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|14<br>TXSCOLGPIS|MMC Transmit Single Collision Good Packet Counter Interrupt Status<br>Indicates whether the status of the MMC transmit single collision good packet counter interrupt is detected.<br>This field becomes 1 when the txsinglecol_g counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|13|MMC Transmit Underflow Error Packet Counter Interrupt Status|
|TXUFLOWERPI<br>S|Indicates whether the status of the MMC transmit underflow error packet counter interrupt is detected.<br>This field becomes 1 when the txunderflowerror counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|12<br>TXBCGBPIS|MMC Transmit Broadcast Good Bad Packet Counter Interrupt Status<br>Indicates whether the status of the MMC transmit broadcast good bad packet counter interrupt is detected.<br>This field becomes 1 when the txbroadcastpackets_gb counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3099 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|11<br>TXMCGBPIS|MMC Transmit Multicast Good Bad Packet Counter Interrupt Status<br>Indicates whether the status of the MMC transmit multicast good bad packet counter interrupt is detected.<br>This field becomes 1 when the txmulticastpackets_gb counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|10<br>TXUCGBPIS|MMC Transmit Unicast Good Bad Packet Counter Interrupt Status<br>Indicates whether the status of the MMC transmit unicast good bad packet counter interrupt is detected.<br>This field becomes 1 when the txunicastpackets_gb counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|9|MMC Transmit 1024 To Maximum Octet Good Bad Packet Counter Interrupt Status|
|TX1024TMAXO<br>CTGBPIS|Indicates whether the status of the MMC transmit 1024 to maximum octet good bad packet counter interrupt<br>is detected.<br>This field becomes 1 when the tx1024tomaxoctets_gb counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|8<br>TX512T1023O<br>CTGBPIS|MMC Transmit 512 To 1023 Octet Good Bad Packet Counter Interrupt Status<br>Indicates whether the status of the MMC transmit 512 to 1023 octet good bad packet counter interrupt<br>is detected.<br>This field becomes 1 when the tx512to1023octets_gb counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|7|MMC Transmit 256 To 511 Octet Good Bad Packet Counter Interrupt Status<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3100 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|TX256T511OC<br>TGBPIS|Indicates whether the status of the MMC transmit 256 to 511 octet good bad packet counter interrupt<br>is detected.<br>This field becomes 1 when the tx256to511octets_gb counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|6|MMC Transmit 128 To 255 Octet Good Bad Packet Counter Interrupt Status|
|TX128T255OC<br>TGBPIS|Indicates whether the status of the MMC transmit 128 to 255 octet good bad packet counter interrupt<br>is detected.<br>This field becomes 1 when the tx128to255octets_gb counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|5|MMC Transmit 65 To 127 Octet Good Bad Packet Counter Interrupt Status|
|TX65T127OCT<br>GBPIS|Indicates whether the status of the MMC transmit 65 to 127 octet good bad packet counter interrupt<br>is detected.<br>This field becomes 1 when the tx65to127octets_gb counter reaches half of its maximum value, and also<br>when it reaches the maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|4|MMC Transmit 64-Octet Good Bad Packet Counter Interrupt Status|
|TX64OCTGBPI<br>S|Indicates whether the status of the MMC transmit 64-octet good bad packet counter interrupt is detected.<br>This field becomes 1 when the tx64octets_gb counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|3|MMC Transmit Multicast Good Packet Counter Interrupt Status|
|TXMCGPIS|Indicates whether the status of the MMC transmit multicast good packet counter interrupt is detected.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3101 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function<br>This field becomes 1 when the txmulticastpackets_g counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|---|---|
|2<br>TXBCGPIS|MMC Transmit Broadcast Good Packet Counter Interrupt Status<br>Indicates whether the status of the MMC transmit broadcast good packet counter interrupt is detected.<br>This field becomes 1 when the txbroadcastpackets_g counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|1<br>TXGBPKTIS|MMC Transmit Good Bad Packet Counter Interrupt Status<br>Indicates whether the status of the MMC transmit good bad packet counter interrupt is detected.<br>This field becomes 1 when the txpacketcount_gb counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|0<br>TXGBOCTIS|MMC Transmit Good Bad Octet Counter Interrupt Status<br>Indicates whether the status of the MMC transmit good bad octet counter interrupt is detected.<br>This field becomes 1 when the txoctetcount_gb counter reaches half of its maximum value or the<br>maximum value.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|



### 74.7.60 MMC Receive Interrupt Mask (MMC_Rx_Interrupt_Mask) 

##### Offset 

|Register|Offset|
|---|---|
|MMC_Rx_Interrupt_Mask|70Ch|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3102 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Function 

Maintains the masks for interrupts generated from all the receive statistic counters. These interrupts are generated when the receive statistic counters reach half of their maximum values or the maximum values. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Rese|rved||Reserv<br>ed|Reserv<br>ed|RXCT<br>RLP...|RXRC<br>VER...|RXWD<br>OGP...|RXVL<br>ANG...|RXFO<br>VPIM|RXPA<br>USP...|RXOR<br>ANG...|RXLE<br>NER...|RXUC<br>GPIM|RX102<br>4T...|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|RX512<br>T1...|RX256<br>T5...|RX128<br>T2...|RX65T<br>12...|RX64<br>OCT...|RXOSI<br>ZE...|RXUSI<br>ZE...|RXJA<br>BER...|RXRU<br>NTP...|RXAL<br>GNE...|RXCR<br>CER...|RXMC<br>GPIM|RXBC<br>GPIM|RXGO<br>CTIM|RXGB<br>OCT...|RXGB<br>PKT...|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-28<br>—|Reserved|
|27<br>—|Reserved|
|26<br>—|Reserved|
|25<br>RXCTRLPIM|MMC Receive Control Packet Counter Interrupt Mask<br>Indicates the status of the MMC receive control packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the rxctrlpackets_g counter reaches half of its maximum value<br>or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|24<br>RXRCVERRPI<br>M|MMC Receive Error Packet Counter Interrupt Mask<br>Indicates the status of the MMC receive error packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the rxrcverror counter reaches half of its maximum value or<br>the maximum value.<br>0b - Disabled<br>1b - Enabled|
|23|MMC Receive Watchdog Error Packet Counter Interrupt Mask|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3103 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field<br>RXWDOGPIM|Function<br>Indicates the status of the MMC receive watchdog error packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the rxwatchdog counter reaches half of its maximum value<br>or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|---|---|
|22<br>RXVLANGBPIM|MMC Receive VLAN Good Bad Packet Counter Interrupt Mask<br>Indicates the status of the MMC receive VLAN good bad packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the rxvlanpackets_gb counter reaches half of its maximum<br>value or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|21<br>RXFOVPIM|MMC Receive FIFO Overflow Packet Counter Interrupt Mask<br>Indicates the status of the MMC receive FIFO overflow packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the rxfifooverflow counter reaches half of its maximum value<br>or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|20<br>RXPAUSPIM|MMC Receive Pause Packet Counter Interrupt Mask<br>Indicates the status of the MMC receive pause packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the rxpausepackets counter reaches half of its maximum<br>value or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|19<br>RXORANGEPI<br>M|MMC Receive Out-Of-Range Error Packet Counter Interrupt Mask<br>Indicates the status of the MMC receive out-of-range error packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the rxoutofrangetype counter reaches half of its maximum<br>value or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|18<br>RXLENERPIM|MMC Receive Length Error Packet Counter Interrupt Mask<br>Indicates the status of the MMC receive length error packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the rxlengtherror counter reaches half of its maximum value<br>or the maximum value.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3104 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Field|Function<br>0b - Disabled<br>1b - Enabled|
|---|---|
|17<br>RXUCGPIM|MMC Receive Unicast Good Packet Counter Interrupt Mask<br>Indicates the status of the MMC receive unicast good packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the rxunicastpackets_g counter reaches half of its maximum<br>value or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|16|MMC Receive 1024 To Maximum Octet Good Bad Packet Counter Interrupt Mask|
|RX1024TMAXO<br>CTGBPIM|Indicates the status of the MMC receive 1024 to maximum octet good bad packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the rx1024tomaxoctets_gb counter reaches half of its<br>maximum value or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|15|MMC Receive 512 To 1023 Octet Good Bad Packet Counter Interrupt Mask|
|RX512T1023O<br>CTGBPIM|Indicates the status of the MMC receive 512 to 1023 octet good bad packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the rx512to1023octets_gb counter reaches half of its<br>maximum value or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|14|MMC Receive 256 To 511 Octet Good Bad Packet Counter Interrupt Mask|
|RX256T511OC<br>TGBPIM|Indicates the status of the MMC receive 256 to 511 octet good bad packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the rx256to511octets_gb counter reaches half of its maximum<br>value or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|13|MMC Receive 128 To 255 Octet Good Bad Packet Counter Interrupt Mask|
|RX128T255OC<br>TGBPIM|Indicates the status of the MMC receive 128 to 255 octet good bad packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the rx128to255octets_gb counter reaches half of its maximum<br>value or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|12|MMC Receive 65 To 127 Octet Good Bad Packet Counter Interrupt Mask|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3105 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|RX65T127OCT<br>GBPIM|Indicates the status of the MMC receive 65 to 127 octet good bad packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the rx65to127octets_gb counter reaches half of its maximum<br>value or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|11<br>RX64OCTGBPI<br>M|MMC Receive 64-Octet Good Bad Packet Counter Interrupt Mask<br>Indicates the status of the MMC receive 64-octet good bad packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the rx64octets_gb counter reaches half of its maximum value<br>or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|10<br>RXOSIZEGPIM|MMC Receive Oversize Good Packet Counter Interrupt Mask<br>Indicates the status of the MMC receive oversize good packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the rxoversize_g counter reaches half of its maximum value<br>or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|9|MMC Receive Undersize Good Packet Counter Interrupt Mask|
|RXUSIZEGPIM|Indicates the status of the MMC receive undersize good packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the rxundersize_g counter reaches half of its maximum value<br>or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|8<br>RXJABERPIM|MMC Receive Jabber Error Packet Counter Interrupt Mask<br>Indicates the status of the MMC receive jabber error packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the rxjabbererror counter reaches half of its maximum value<br>or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|7<br>RXRUNTPIM|MMC Receive Runt Packet Counter Interrupt Mask<br>Indicates the status of the MMC receive runt packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the rxrunterror counter reaches half of its maximum value or<br>the maximum value.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3106 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function<br>0b - Disabled<br>1b - Enabled|
|---|---|
|6<br>RXALGNERPI<br>M|MMC Receive Alignment Error Packet Counter Interrupt Mask<br>Indicates the status of the MMC receive alignment error packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the rxalignmenterror counter reaches half of its maximum<br>value or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|5|MMC Receive CRC Error Packet Counter Interrupt Mask|
|RXCRCERPIM|Indicates the status of the MMC receive CRC error packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the rxcrcerror counter reaches half of its maximum value or<br>the maximum value.<br>0b - Disabled<br>1b - Enabled|
|4<br>RXMCGPIM|MMC Receive Multicast Good Packet Counter Interrupt Mask<br>Indicates the status of the MMC receive multicast good packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the rxmulticastpackets_g counter reaches half of its maximum<br>value or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|3<br>RXBCGPIM|MMC Receive Broadcast Good Packet Counter Interrupt Mask<br>Indicates the status of the MMC receive broadcast good packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the rxbroadcastpackets_g counter reaches half of its<br>maximum value or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|2<br>RXGOCTIM|MMC Receive Good Octet Counter Interrupt Mask<br>Indicates the status of the MMC receive good octet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the rxoctetcount_g counter reaches half of its maximum value<br>or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|1|MMC Receive Good Bad Octet Counter Interrupt Mask|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3107 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|RXGBOCTIM|Indicates the status of the MMC receive good bad octet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the rxoctetcount_gb counter reaches half of its maximum<br>value or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|0|MMC Receive Good Bad Packet Counter Interrupt Mask|
|RXGBPKTIM|Indicates the status of the MMC receive good bad packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the rxpacketcount_gb counter reaches half of its maximum<br>value or the maximum value.<br>0b - Disabled<br>1b - Enabled|



### 74.7.61 MMC Transmit Interrupt Mask (MMC_Tx_Interrupt_Mask) 

##### Offset 

|Register|Offset|
|---|---|
|MMC_Tx_Interrupt_Mask|710h|



##### Function 

Maintains the masks for interrupts that are generated when the transmit statistic counters reach half of their maximum values or their maximum values. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Rese|rved||Reserv<br>ed|Reserv<br>ed|TXOSI<br>ZE...|TXVLA<br>NG...|TXPA<br>USP...|TXEX<br>DEF...|TXGP<br>KTIM|TXGO<br>CTIM|TXCA<br>RER...|TXEX<br>COL...|TXLAT<br>CO...|TXDE<br>FPIM|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|TXMC<br>OLG...|TXSC<br>OLG...|TXUFL<br>OW...|TXBC<br>GBP...|TXMC<br>GBP...|TXUC<br>GBP...|TX102<br>4T...|TX512<br>T1...|TX256<br>T5...|TX128<br>T2...|TX65T<br>12...|TX64O<br>CT...|TXMC<br>GPIM|TXBC<br>GPIM|TXGB<br>PKT...|TXGB<br>OCT...|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3108 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Fields 

|Field<br>31-28<br>—|Function<br>Reserved|
|---|---|
|27<br>—|Reserved|
|26<br>—|Reserved|
|25<br>TXOSIZEGPIM|MMC Transmit Oversize Good Packet Counter Interrupt Mask<br>Indicates the status of the MMC transmit oversize good packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the txoversize_g counter reaches half of its maximum value<br>or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|24<br>TXVLANGPIM|MMC Transmit VLAN Good Packet Counter Interrupt Mask<br>Indicates the status of the MMC transmit VLAN good packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the txvlanpackets_g counter reaches half of its maximum<br>value or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|23<br>TXPAUSPIM|MMC Transmit Pause Packet Counter Interrupt Mask<br>Indicates the status of the MMC transmit pause packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the txpausepackets counter reaches half of its maximum<br>value or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|22<br>TXEXDEFPIM|MMC Transmit Excessive Deferral Packet Counter Interrupt Mask<br>Indicates the status of the MMC transmit excessive deferral packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the txexcessdef counter reaches half of its maximum value<br>or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|21<br>TXGPKTIM|MMC Transmit Good Packet Counter Interrupt Mask<br>Indicates the status of the MMC transmit good packet counter interrupt mask.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3109 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||Writing 1 to this field masks the interrupt when the txpacketcount_g counter reaches half of its maximum<br>value or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|20<br>TXGOCTIM|MMC Transmit Good Octet Counter Interrupt Mask<br>Indicates the status of the MMC transmit good octet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the txoctetcount_g counter reaches half of its maximum value<br>or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|19<br>TXCARERPIM|MMC Transmit Carrier Error Packet Counter Interrupt Mask<br>Indicates the status of the MMC transmit carrier error packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the txcarriererror counter reaches half of its maximum value<br>or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|18<br>TXEXCOLPIM|MMC Transmit Excessive Collision Packet Counter Interrupt Mask<br>Indicates the status of the MMC transmit excessive collision packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the txexcesscol counter reaches half of its maximum value<br>or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|17<br>TXLATCOLPIM|MMC Transmit Late Collision Packet Counter Interrupt Mask<br>Indicates the status of the MMC transmit late collision packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the txlatecol counter reaches half of its maximum value or<br>the maximum value.<br>0b - Disabled<br>1b - Enabled|
|16<br>TXDEFPIM|MMC Transmit Deferred Packet Counter Interrupt Mask<br>Indicates the status of the MMC transmit deferred packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the txdeferred counter reaches half of the maximum value<br>or the maximum value.<br>0b - Disabled<br>1b - Enabled<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3110 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|15<br>TXMCOLGPIM|MMC Transmit Multiple Collision Good Packet Counter Interrupt Mask<br>Indicates the status of the MMC transmit multiple collision good packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the txmulticol_g counter reaches half of its maximum value<br>or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|14<br>TXSCOLGPIM|MMC Transmit Single Collision Good Packet Counter Interrupt Mask<br>Indicates the status of the MMC transmit single collision good packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the txsinglecol_g counter reaches half of its maximum value<br>or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|13<br>TXUFLOWERPI<br>M|MMC Transmit Underflow Error Packet Counter Interrupt Mask<br>Indicates the status of the MMC transmit underflow error packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the txunderflowerror counter reaches half of its maximum<br>value or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|12<br>TXBCGBPIM|MMC Transmit Broadcast Good Bad Packet Counter Interrupt Mask<br>Indicates the status of the MMC transmit broadcast good bad packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the txbroadcastpackets_gb counter reaches half of its<br>maximum value or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|11<br>TXMCGBPIM|MMC Transmit Multicast Good Bad Packet Counter Interrupt Mask<br>Indicates the status of the MMC transmit multicast good bad packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the txmulticastpackets_gb counter reaches half of its<br>maximum value or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|10<br>TXUCGBPIM|MMC Transmit Unicast Good Bad Packet Counter Interrupt Mask<br>Indicates the status of the MMC transmit unicast good bad packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the txunicastpackets_gb counter reaches half of its maximum<br>value or the maximum value.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3111 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function<br>0b - Disabled<br>1b - Enabled|
|---|---|
|9|MMC Transmit 1024 To Maximum Octet Good Bad Packet Counter Interrupt Mask|
|TX1024TMAXO<br>CTGBPIM|Indicates the status of the MMC transmit 1024 to maximum octet good bad packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the tx1024tomaxoctets_gb counter reaches half of its<br>maximum value or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|8|MMC Transmit 512 To 1023 Octet Good Bad Packet Counter Interrupt Mask|
|TX512T1023O<br>CTGBPIM|Indicates the status of the MMC transmit 512 to 1023 octet good bad packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the tx512to1023octets_gb counter reaches half of its<br>maximum value or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|7|MMC Transmit 256 To 511 Octet Good Bad Packet Counter Interrupt Mask|
|TX256T511OC<br>TGBPIM|Indicates the status of the MMC transmit 256 to 511 octet good bad packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the tx256to511octets_gb counter reaches half of its maximum<br>value or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|6|MMC Transmit 128 To 255 Octet Good Bad Packet Counter Interrupt Mask|
|TX128T255OC<br>TGBPIM|Indicates the status of the MMC transmit 128 to 255 octet good bad packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the tx128to255octets_gb counter reaches half of its maximum<br>value or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|5|MMC Transmit 65 To 127 Octet Good Bad Packet Counter Interrupt Mask|
|TX65T127OCT<br>GBPIM|Indicates the status of the MMC transmit 65 to 127 octet good bad packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the tx65to127octets_gb counter reaches half of its maximum<br>value or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|4|MMC Transmit 64-Octet Good Bad Packet Counter Interrupt Mask|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3112 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|TX64OCTGBPI<br>M|Indicates the status of the MMC transmit 64-octet good bad packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the tx64octets_gb counter reaches half of its maximum value<br>or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|3<br>TXMCGPIM|MMC Transmit Multicast Good Packet Counter Interrupt Mask<br>Indicates the status of the MMC transmit multicast good packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the txmulticastpackets_g counter reaches half of its maximum<br>value or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|2<br>TXBCGPIM|MMC Transmit Broadcast Good Packet Counter Interrupt Mask<br>Indicates the status of the MMC transmit broadcast good packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the txbroadcastpackets_g counter reaches half of its<br>maximum value or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|1<br>TXGBPKTIM|MMC Transmit Good Bad Packet Counter Interrupt Mask<br>Indicates the status of the MMC transmit good bad packet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the txpacketcount_gb counter reaches half of its maximum<br>value or the maximum value.<br>0b - Disabled<br>1b - Enabled|
|0<br>TXGBOCTIM|MMC Transmit Good Bad Octet Counter Interrupt Mask<br>Indicates the status of the MMC transmit good bad octet counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the txoctetcount_gb counter reaches half of its maximum<br>value or the maximum value.<br>0b - Disabled<br>1b - Enabled|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3113 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

### 74.7.62 Transmit Octet Count Good Bad (Tx_Octet_Count_Good_Bad) 

##### Offset 

|Register|Offset|
|---|---|
|Tx_Octet_Count_Good_|714h|
|Bad||



##### Function 

Provides the number of bytes that the module transmitted, exclusive of preamble and retried bytes, in good and bad packets. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3114-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXOCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXOCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Transmit Octet Count Good Bad|
|TXOCTGB|Indicates the number of bytes transmitted, exclusive of preamble and retried bytes, in good and bad packets.|



### 74.7.63 Transmit Packet Count Good Bad (Tx_Packet_Count_Good_Bad) 

##### Offset 

|Register|Offset|
|---|---|
|Tx_Packet_Count_Good<br>_Bad|718h|



##### Function 

Provides the number of good and bad packets that the module transmitted, exclusive of retried packets. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3114 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3115-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXPKTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXPKTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Transmit Packet Count Good Bad|
|TXPKTGB|Indicates the number of good and bad packets transmitted, exclusive of retried packets.|



### 74.7.64 Transmit Broadcast Packets Good (Tx_Broadcast_Packets_Good) 

##### Offset 

|Register|Offset|
|---|---|
|Tx_Broadcast_Packets_|71Ch|
|Good||



##### Function 

Provides the number of good broadcast packets that the module transmitted. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||TXBC|ASTG||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||TXBC|ASTG||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3115 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Fields 

|Field|Function|
|---|---|
|31-0|Transmit Broadcast Packets Good|
|TXBCASTG|Indicates the number of good broadcast packets transmitted.|



### 74.7.65 Transmit Multicast Packets Good (Tx_Multicast_Packets_Good) 

##### Offset 

|Register|Offset|
|---|---|
|Tx_Multicast_Packets_G|720h|
|ood||



##### Function 

Provides the number of good multicast packets that the module transmitted. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3116-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXMCASTG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXMCASTG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Transmit Multicast Packets Good|
|TXMCASTG|Indicates the number of good multicast packets transmitted.|



### 74.7.66 Transmit 64-Octet Packets Good Bad (Tx_64Octets_Packets_Good_Bad) 

##### Offset 

|Register|Offset|
|---|---|
|Tx_64Octets_Packets_G|724h|
|ood_Bad||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3116 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Function 

Provides the number of 64-byte good and bad packets that the module transmitted, exclusive of preamble and retried packets. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3117-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TX64OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TX64OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Transmit 64-Octet Packets Good Bad|
|TX64OCTGB|Indicates the number of transmitted 64-byte good and bad packets, exclusive of preamble and<br>retried packets.|



### 74.7.67 Transmit 65 To 127 Octet Packets Good Bad (Tx_65To127Octets_Packets_Good_Bad) 

##### Offset 

|Register|Offset|
|---|---|
|Tx_65To127Octets_Pack|728h|
|ets_Good_Bad||



##### Function 

Provides the number of good and bad packets, having length between 65 and 127 (inclusive) bytes, that the module transmitted, exclusive of preamble and retried packets. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3117 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3118-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TX65_127OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TX65_127OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Transmit 65 To 127 Octet Packets Good Bad|
|TX65_127OCT|Indicates the number of good and bad packets transmitted, having length between 65 and 127 (inclusive)|
|GB|bytes, exclusive of preamble and retried packets.|



### 74.7.68 Transmit 128 To 255 Octet Packets Good Bad (Tx_128To255Octets_Packets_Good_Bad) 

##### Offset 

|Register|Offset|
|---|---|
|Tx_128To255Octets_Pac|72Ch|
|kets_Good_Bad||



##### Function 

Provides the number of good and bad packets that the module transmitted, having length between 128 to 255 (inclusive) bytes, exclusive of preamble and retried packets. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3118-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TX128_255OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TX128_255OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3118 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Fields 

|Field|Function|
|---|---|
|31-0|Transmit 128 To 255 Octet Packets Good Bad|
|TX128_255OCT<br>GB|Indicates the number of good and bad packets transmitted, having length between 128 and 255 (inclusive)<br>bytes, exclusive of preamble and retried packets.|



### 74.7.69 Transmit 256 To 511 Octet Packets Good Bad (Tx_256To511Octets_Packets_Good_Bad) 

##### Offset 

|Register|Offset|
|---|---|
|Tx_256To511Octets_Pac|730h|
|kets_Good_Bad||



##### Function 

Provides the number of good and bad packets that the module transmitted, having length between 256 to 511 (inclusive) bytes, exclusive of preamble and retried packets. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3119-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TX256_511OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TX256_511OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-0|Transmit 256 To 511 Octet Packets Good Bad|
|TX256_511OCT<br>GB|Indicates the number of good and bad packets transmitted, having length between 256 and 511 (inclusive)<br>bytes, exclusive of preamble and retried packets.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3119 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

### 74.7.70 Transmit 512 To 1023 Octet Packets Good Bad (Tx_512To1023Octets_Packets_Good_Bad) 

##### Offset 

|Register|Offset|
|---|---|
|Tx_512To1023Octets_P|734h|
|ackets_Good_Bad||



##### Function 

Provides the number of good and bad packets that the module transmitted, having length between 512 to 1023 (inclusive) bytes, exclusive of preamble and retried packets. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3120-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TX512_1023OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TX512_1023OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Transmit 512 To 1023 Octet Packets Good Bad|
|TX512_1023OC<br>TGB|Indicates the number of good and bad packets transmitted, having length between 512 and 1023 (inclusive)<br>bytes, exclusive of preamble and retried packets.|



### 74.7.71 Transmit 1024 To Max Octet Packets Good Bad (Tx_1024ToMaxOctets_Packets_Good_Bad) 

##### Offset 

|Register|Offset|
|---|---|
|Tx_1024ToMaxOctets_P|738h|
|ackets_Good_Bad||



##### Function 

Provides the number of good and bad packets that the module transmitted, having a length between 1024 bytes (inclusive) and the maximum size, exclusive of preamble and retried packets. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3120 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3121-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TX1024_MAXOCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TX1024_MAXOCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Transmit 1024 To Max Octet Packets Good Bad|
|TX1024_MAXO<br>CTGB|Indicates the number of good and bad packets transmitted, having a length between 1024 bytes (inclusive)<br>and the maximum size, exclusive of preamble and retried packets.|



### 74.7.72 Transmit Unicast Packets Good Bad (Tx_Unicast_Packets_Good_Bad) 

##### Offset 

|Register|Offset|
|---|---|
|Tx_Unicast_Packets_Go|73Ch|
|od_Bad||



##### Function 

Provides the number of good and bad unicast packets that the module transmitted. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||TXUCA|STGB||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||TXUCA|STGB||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3121 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Fields 

|Field|Function|
|---|---|
|31-0|Transmit Unicast Packets Good Bad|
|TXUCASTGB|Indicates the number of good and bad unicast packets transmitted.|



### 74.7.73 Transmit Multicast Packets Good Bad (Tx_Multicast_Packets_Good_Bad) 

##### Offset 

|Register|Offset|
|---|---|
|Tx_Multicast_Packets_G|740h|
|ood_Bad||



##### Function 

Provides the number of good and bad multicast packets that the module transmitted. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||TXMCA|STGB||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||TXMCA|STGB||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-0|Transmit Multicast Packets Good Bad|
|TXMCASTGB|Indicates the number of good and bad multicast packets transmitted.|



### 74.7.74 Transmit Broadcast Packets Good Bad (Tx_Broadcast_Packets_Good_Bad) 

##### Offset 

|Register|Offset|
|---|---|
|Tx_Broadcast_Packets_|744h|
|Good_Bad||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3122 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Function 

Provides the number of good and bad broadcast packets that the module transmitted. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3123-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXBCASTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXBCASTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Transmit Broadcast Packets Good Bad|
|TXBCASTGB|Indicates the number of good and bad broadcast packets transmitted.|



### 74.7.75 Transmit Underflow Error Packets (Tx_Underflow_Error_Packets) 

##### Offset 

|Register|Offset|
|---|---|
|Tx_Underflow_Error_Pac|748h|
|kets||



##### Function 

Provides the number of packets that the module aborted because of a packet underflow error. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||TXUND|RFLW||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||TXUND|RFLW||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3123 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Fields 

|Field|Function|
|---|---|
|31-0|Transmit Underflow Error Packets|
|TXUNDRFLW|Indicates the number of packets aborted because of a packet underflow error.|



### 74.7.76 Transmit Single Collision Good Packets (Tx_Single_Collision_Good_Packets) 

##### Offset 

|Register|Offset|
|---|---|
|Tx_Single_Collision_Goo|74Ch|
|d_Packets||



##### Function 

Provides the number of packets that the module successfully transmitted after a single collision in Half-Duplex mode. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||TXSNG|LCOLG||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||TXSNG|LCOLG||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-0|Transmit Single Collision Good Packets|
|TXSNGLCOLG|Indicates the number of successfully transmitted packets after a single collision in Half-Duplex mode.|



### 74.7.77 Transmit Multiple Collision Good Packets (Tx_Multiple_Collision_Good_Packets) 

##### Offset 

|Register|Offset|
|---|---|
|Tx_Multiple_Collision_Go|750h|
|od_Packets||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3124 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Function 

Provides the number of packets that the module successfully transmitted after multiple collisions in Half-Duplex mode. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3125-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXMULTCOLG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXMULTCOLG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-0|Transmit Multiple Collision Good Packets|
|TXMULTCOLG|Indicates the number of successfully transmitted packets after multiple collisions in Half-Duplex mode.|



### 74.7.78 Transmit Deferred Packets (Tx_Deferred_Packets) 

##### Offset 

|Register|Offset|
|---|---|
|Tx_Deferred_Packets|754h|



##### Function 

Provides the number of packets that the module successfully transmitted after a deferral in Half-Duplex mode. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3125-14.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXDEFRD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXDEFRD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3125 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Fields 

|Field|Function|
|---|---|
|31-0|Transmit Deferred Packets|
|TXDEFRD|Indicates the number of successfully transmitted packets after a deferral in Half-Duplex mode.|



### 74.7.79 Transmit Late Collision Packets (Tx_Late_Collision_Packets) 

##### Offset 

|Register|Offset|
|---|---|
|Tx_Late_Collision_Packe|758h|
|ts||



##### Function 

Provides the number of packets that the module aborted because of a late collision error. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3126-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXLATECOL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXLATECOL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Transmit Late Collision Packets|
|TXLATECOL|Indicates the number of packets aborted because of a late collision error.|



### 74.7.80 Transmit Excessive Collision Packets (Tx_Excessive_Collision_Packets) 

##### Offset 

|Register|Offset|
|---|---|
|Tx_Excessive_Collision_|75Ch|
|Packets||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3126 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Function 

Provides the number of packets that the module aborted because of excessive (16) collision errors. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3127-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXEXSCOL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXEXSCOL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Transmit Excessive Collision Packets|
|TXEXSCOL|Indicates the number of packets aborted because of excessive (16) collision errors.|



### 74.7.81 Transmit Carrier Error Packets (Tx_Carrier_Error_Packets) 

##### Offset 

|Register|Offset|
|---|---|
|Tx_Carrier_Error_Packet|760h|
|s||



##### Function 

Provides the number of packets that the module aborted because of a carrier sense error (such as no carrier or loss of carrier). 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||TXC|ARR||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||TXC|ARR||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3127 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Fields 

|Field|Function|
|---|---|
|31-0|Transmit Carrier Error Packets|
|TXCARR|Indicates the number of packets aborted because of a carrier sense error (such as no carrier or loss<br>of carrier).|



### 74.7.82 Transmit Octet Count Good (Tx_Octet_Count_Good) 

##### Offset 

|Register|Offset|
|---|---|
|Tx_Octet_Count_Good|764h|



##### Function 

Provides the number of bytes that the module transmitted, exclusive of preamble, only in good packets. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3128-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXOCTG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXOCTG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Transmit Octet Count Good|
|TXOCTG|Indicates the number of bytes transmitted, exclusive of preamble, only in good packets.|



### 74.7.83 Transmit Packet Count Good (Tx_Packet_Count_Good) 

##### Offset 

|Register|Offset|
|---|---|
|Tx_Packet_Count_Good|768h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3128 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Function 

Provides the number of good packets that the module transmitted. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3129-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXPKTG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXPKTG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Transmit Packet Count Good|
|TXPKTG|Indicates the number of good packets transmitted.|



### 74.7.84 Transmit Excessive Deferral Error (Tx_Excessive_Deferral_Error) 

##### Offset 

|Register|Offset|
|---|---|
|Tx_Excessive_Deferral_<br>Error|76Ch|



##### Function 

Provides the number of packets that the module aborted because of an excessive deferral error (deferred for more than two max-sized packet times). 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||TXEX|SDEF||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||TXEX|SDEF||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3129 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Fields 

|Field|Function|
|---|---|
|31-0|Transmit Excessive Deferral Error|
|TXEXSDEF|Indicates the number of packets aborted because of excessive deferral error (deferred for more than two<br>max-sized packet times).|



### 74.7.85 Transmit Pause Packets (Tx_Pause_Packets) 

##### Offset 

|Register|Offset|
|---|---|
|Tx_Pause_Packets|770h|



##### Function 

Provides the number of good pause packets that the module transmitted. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3130-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXPAUSE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXPAUSE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Transmit Pause Packets|
|TXPAUSE|Indicates the number of good pause packets transmitted.|



### 74.7.86 Transmit VLAN Packets Good (Tx_VLAN_Packets_Good) 

##### Offset 

|Register|Offset|
|---|---|
|Tx_VLAN_Packets_Good|774h|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3130 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Function 

##### Provides the number of good VLAN packets that the module transmitted. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3131-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXVLANG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXVLANG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Transmit VLAN Packets Good|
|TXVLANG|Provides the number of good VLAN packets transmitted.|



### 74.7.87 Transmit O Size Packets Good (Tx_OSize_Packets_Good) 

##### Offset 

|Register|Offset|
|---|---|
|Tx_OSize_Packets_Goo<br>d|778h|



##### Function 

Provides the number of packets that the module transmitted without errors, and having a length greater than the maximum size, which is 1,518 or 1,522 bytes for VLAN-tagged packets. This size is 2000 bytes if MAC_Configuration[S2KP] = 1. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3131-14.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXOSIZG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXOSIZG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3131 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Fields 

|Field|Function|
|---|---|
|31-0|Transmit O Size Packets Good|
|TXOSIZG|Indicates the number of packets transmitted without errors, and having a length greater than the<br>maximum size, which is 1,518 or 1,522 bytes for VLAN-tagged packets. This size is 2000 bytes if<br>MAC_Configuration[S2KP]= 1.|



### 74.7.88 Receive Packets Count Good Bad (Rx_Packets_Count_Good_Bad) 

##### Offset 

|Register|Offset|
|---|---|
|Rx_Packets_Count_Goo|780h|
|d_Bad||



##### Function 

Provides the number of good and bad packets that the module received. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||RXPK|TGB||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||RXPK|TGB||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function|
|---|---|
|31-0|Receive Packets Count Good Bad|
|RXPKTGB|Indicates the number of good and bad packets received.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3132 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

### 74.7.89 Receive Octet Count Good Bad (Rx_Octet_Count_Good_Bad) 

##### Offset 

|Register|Offset|
|---|---|
|Rx_Octet_Count_Good_|784h|
|Bad||



##### Function 

Provides the number of bytes that DWC_ther_qos received, exclusive of preamble, in good and bad packets. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3133-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RXOCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXOCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Receive Octet Count Good Bad|
|RXOCTGB|Indicates the number of bytes received, exclusive of preamble, in good and bad packets.|



### 74.7.90 Receive Octet Count Good (Rx_Octet_Count_Good) 

##### Offset 

|Register|Offset|
|---|---|
|Rx_Octet_Count_Good|788h|



##### Function 

Provides the number of bytes that the module received, exclusive of preamble, only in good packets. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3133 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3134-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RXOCTG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXOCTG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Receive Octet Count Good|
|RXOCTG|Indicates the number of bytes received, exclusive of preamble, only in good packets.|



### 74.7.91 Receive Broadcast Packets Good (Rx_Broadcast_Packets_Good) 

##### Offset 

|Register|Offset|
|---|---|
|Rx_Broadcast_Packets_|78Ch|
|Good||



##### Function 

Provides the number of good broadcast packets that the module received. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||RXBC|ASTG||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||RXBC|ASTG||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3134 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Fields 

|Field|Function|
|---|---|
|31-0|Receive Broadcast Packets Good|
|RXBCASTG|Indicates the number of good broadcast packets received.|



### 74.7.92 Receive Multicast Packets Good (Rx_Multicast_Packets_Good) 

##### Offset 

|Register|Offset|
|---|---|
|Rx_Multicast_Packets_G|790h|
|ood||



##### Function 

Provides the number of good multicast packets that the module received. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3135-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RXMCASTG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXMCASTG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Receive Multicast Packets Good|
|RXMCASTG|Indicates the number of good multicast packets received.|



### 74.7.93 Receive CRC Error Packets (Rx_CRC_Error_Packets) 

##### Offset 

|Register|Offset|
|---|---|
|Rx_CRC_Error_Packets|794h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3135 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

##### Function 

Provides the number of packets that the module received with a CRC error. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part1/S32K3XXRM_数据表.pdf-3136-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RXCRCERR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXCRCERR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Receive CRC Error Packets|
|RXCRCERR|Indicates the number of packets received with a CRC error.|



### 74.7.94 Receive Alignment Error Packets (Rx_Alignment_Error_Packets) 

##### Offset 

|Register|Offset|
|---|---|
|Rx_Alignment_Error_Pac|798h|
|kets||



##### Function 

Provides the number of packets that the module received with an alignment (dribble) error. It is valid only in 10/100 mode. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||RXALG|NERR||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||RXALG|NERR||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3136 / 4640 

