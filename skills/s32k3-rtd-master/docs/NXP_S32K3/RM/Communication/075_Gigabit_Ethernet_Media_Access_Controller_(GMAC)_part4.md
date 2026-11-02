NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## 75.7.355 (DMA_CH0_Miss_Frame_Cnt) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH0_Miss_Frame_|1164h|
|Cnt||



#### Function 

This register has the number of packet counter that got dropped by the DMA either due to Bus Error or due to programming RPF field in DMA_CH${i}_Rx_Control register. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4042-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_16<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R MFCO  Reserved_14_11  MFC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-16|Reserved.|
|Reserved_31_1<br>6||
|15<br>MFCO|Overflow status of the MFC Counter When this bit is set then the MFC counter does not get incremented<br>further. The bit gets cleared when this register is read. Access restriction applies. Clears on read.<br>Self-set to 1 on internal event.<br>0b - Miss Frame Counter overflow not occurred<br>1b - Miss Frame Counter overflow occurred|
|14-11|Reserved.|
|Reserved_14_1<br>1||
|10-0<br>MFC|Dropped Packet Counters This counter indicates the number of packet counters that are dropped by<br>the DMA either because of bus error or because of programing RPF field in DMA_CH${i}_Rx_Control<br>register. The counter gets cleared when this register is read. Access restriction applies. Clears on read.<br>Self-set to 1 on internal event.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4042 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## 75.7.356 (DMA_CH0_RXP_Accept_Cnt) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH0_RXP_Accept|1168h|
|_Cnt||



#### Function 

The DMA_CH(#i)_RXP_Accept_Cnt registers provides the count of the number of frames accepted by Rx Parser. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4043-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>RXPA<br>R RXPAC<br>COF<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXPAC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31<br>RXPACOF|Rx Parser Accept Counter Overflow Bit When set, this bit indicates that the RXPAC Counter field<br>crossed the maximum limit. Access restriction applies. Clears on read. Self-set to 1 on internal event.<br>0b - Rx Parser Accept Counter overflow not occurred|
||1b - Rx Parser Accept Counter overflow occurred|
|30-0<br>RXPAC|Rx Parser Accept Counter This 31-bit counter is implemented when a Rx Parser Accept a packet due to<br>AF =1. The counter is cleared when the register is read.|



## 75.7.357 (DMA_CH0_RX_ERI_Cnt) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH0_RX_ERI_Cnt|116Ch|



#### Function 

The DMA_CH(#i)_RX_ERI_Cnt registers provides the count of the number of times ERI was asserted. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4043 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4044-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_12<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_31_12  ECNT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-12|Reserved.|
|Reserved_31_1<br>2||
|11-0<br>ECNT|ERI Counter When ERIC bit of DMA_CH(#i)_RX_Control register is set, this counter increments for burst<br>transfer completed by the Rx DMA from the start of packet transfer. This counter is reset at the start of<br>new packet.|



## 75.7.358 (DMA_CH1_Control) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH1_Control|1180h|



#### Function 

The DMA Channeli Control register specifies the MSS value for segmentation, length to skip between two descriptors, and also the features such as header splitting and 8xPBL mode. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4044 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4045-01.png)


<!-- Start of picture text -->
Gigabit Ethernet Media Access Controller (GMAC)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R Reserved_31_25  Reserved_23_21<br>SPH  DSL  e... PBLx8<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserved_15_1<br>R Reserved_MSS<br>4<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-25|Reserved.|
|Reserved_31_2<br>5||
|24<br>SPH|Split Headers When this bit is set, the DMA splits the header and payload in the Receive path. The DMA<br>writes the header to the Buffer Address1 of RDES0. The DMA writes the payload to the buffer to which<br>the Buffer Address2 is pointing. The software must ensure that the header fits into the Receive buffers. If<br>the header length exceeds the receive buffer size, the DMA does not split the header and payload. This<br>bit is available only if Enable Split Header Structure option is selected.<br>0b - Split Headers feature is disabled<br>1b - Split Headers feature is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20-18<br>DSL|Descriptor Skip Length This bit specifies the Word, Dword, or Lword number (depending on the 32-bit,<br>64-bit, or 128-bit bus) to skip between two unchained descriptors. The address skipping starts from the<br>end of the current descriptor to the start of the next descriptor. When the DSL value is equal to zero, the<br>DMA takes the descriptor table as contiguous.|
|17|Reserved.|
|Reserved_17||
|16<br>PBLx8|8xPBL mode When this bit is set, the PBL value programmed in Bits[21:16] in DMA_CH(#i)_Tx_Control<br>and Bits[21:16] in DMA_CH(#i)_Rx_Control is multiplied by eight times. Therefore, the DMA transfers the<br>data in 8, 16, 32, 64, 128, and 256 beats depending on the PBL value.<br>0b - 8xPBL mode is disabled|
||1b - 8xPBL mode is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4045 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4046-03.png)


<!-- Start of picture text -->
Field Function<br>15-14 Reserved.<br>Reserved_15_1<br>4<br>13-0 Reserved.<br>Reserved_MSS<br><!-- End of picture text -->

## 75.7.359 (DMA_CH1_Tx_Control) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH1_Tx_Control|1184h|



#### Function 

The DMA Channeli Transmit Control register controls the Tx features such as PBL, TCP segmentation, and Tx Channel weights. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4046-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv Reserv<br>R Reserved_TQOS<br>e... TFSEL  EDSE  e... ETIC  TxPBL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv Reserved_TSE Reserv<br>R Reserved_11_5<br>e... _MO... e... OSF  TCW  ST<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31|Reserved.|
|Reserved_31||
|30-29<br>TFSEL|TBS Fetch Select Select bits for one of the four DMA_TBS_CTRL register fields (FTOS,FGSN,FTOV) for<br>the channel Values: - 2'b00: DMA_TBS_CTRL0 - 2'b01: DMA_TBS_CTRL1 - 2'b10: DMA_TBS_CTRL2 -<br>2'b11: DMA_TBS_CTRL3 (Reserved if DWC_EQOS_NUM_DMA_TX_CH=3)|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4046 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|28<br>EDSE|Enhanced Descriptor Enable When this bit is set, the corresponding channel uses Enhanced Descriptors<br>that are 32 Bytes for both Normal and Context Descriptors. When reset, the corresponding channel uses<br>the descriptors that are 16 Bytes.<br>0b - Enhanced Descriptor is disabled<br>1b - Enhanced Descriptor is enabled|
|27-24|Reserved.|
|Reserved_TQO<br>S||
|23<br>Reserved_23|Reserved.|
|22<br>ETIC|Early Transmit Interrupt Control When this bit is set, Early Transmit Interrupt (ETI) status is set after<br>completion of transfer of data from buffers of a transmit descriptor in which IOC bit (TDES2[31]) is set.<br>When this bit is reset, ETI is set only after a complete packet is transferred to the MTL TX FIFO memory.<br>0b - Early Transmit Interrupt is disabled<br>1b - Early Transmit Interrupt is enabled|
|21-16<br>TxPBL|Transmit Programmable Burst Length These bits indicate the maximum number of beats to be<br>transferred in one DMA block data transfer. The DMA always attempts max burst as specified in PBL<br>each time it starts a burst transfer on the application bus. You can program PBL with any of the following<br>values: 1, 2, 4, 8, 16, or 32. Any other value results in undefined behavior. To transfer more than 32<br>beats, perform the following steps: 1. Set the 8xPBL mode in DMA_CH0_Control register. 2. Set the<br>TxPBL. Note: The maximum value of TxPBL must be less than or equal to half the Tx Queue size<br>(TQS field of MTL_TxQ(#i)_Operation_Mode register) in terms of beats. This is required so that the Tx<br>Queue has space to store at least another Tx PBL worth of data while the MTL Tx Queue Controller is<br>transferring data to MAC. For example, in 64-bit data width configurations the total locations in Tx Queue<br>of size 512 bytes is 64, TxPBL and 8xPBL needs to be programmed to less than or equal to 32.|
|15<br>Reserved_IPBL|Reserved.|
|14-13|Reserved.|
|Reserved_TSE_<br>MODE||
|12<br>Reserved_TSE|Reserved.|
|11-5<br>Reserved_11_5|Reserved.|
|4<br>OSF|Operate on Second Packet When this bit is set, it instructs the DMA to process the second packet of the<br>Transmit data even before the status for the first packet is obtained.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4047 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Operate on Second Packet disabled<br>1b - Operate on Second Packet enabled|
|3-1<br>TCW|Transmit Channel Weight This field indicates the weight assigned to the corresponding Transmit<br>channel. When reset is complete, this field is set to 0 for all channels by default, resulting in equal<br>weights to all channels.|
|0<br>ST|Start or Stop Transmission Command When this bit is set, transmission is placed in the Running state.<br>The DMA checks the Transmit list at the current position for a packet to be transmitted. The DMA tries<br>to acquire descriptor from either of the following positions: - The current position in the list This is the<br>base address of the Transmit list set by the DMA_CH0_TxDesc_List_Address register. - The position<br>at which the transmission was previously stopped If the DMA does not own the current descriptor, the<br>transmission enters the Suspended state and the TBU bit of the DMA_CH0_Status register is set. The<br>Start Transmission command is effective only when the transmission is stopped. If the command is<br>issued before setting the DMA_CH0_TxDesc_List_Address register, the DMA behavior is unpredictable.<br>When this bit is reset, the transmission process is placed in the Stopped state after completing the<br>transmission of the current packet. The Next Descriptor position in the Transmit list is saved, and it<br>becomes the current position when the transmission is restarted. To change the list address, you need<br>to program DMA_CH0_TxDesc_List_Address register with a new value when this bit is reset. The new<br>value is considered when this bit is set again. The stop transmission command is effective only when the<br>transmission of the current packet is complete or the transmission is in the Suspended state.<br>0b - Stop Transmission Command<br>1b - Start Transmission Command|



## 75.7.360 (DMA_CH1_Rx_Control) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH1_Rx_Control|1188h|



#### Function 

The DMA Channeli Receive Control register controls the Rx features such as PBL, buffer size, and extended status. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4048 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4049-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R Reserved_30_28  Reserved_RQOS<br>RPF  e... ERIC  RxPBL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv<br>R RBSZ_x_0<br>e... RBSZ_13_y  SR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31<br>RPF|Rx Packet Flush. - 1: DWC_ether_qos automatically flushes the packet from the Rx Queues destined<br>to this DMA Rx Channel, when it is stopped. When this bit remains set and the DMA is re-started by<br>the software driver, the packets residing in the Rx Queues that were received when this RxDMA was<br>stopped, are flushed out. The packets that are received by the MAC after the RxDMA is re-started are<br>routed to the RxDMA. The flushing is done on the Read side of the Rx Queue. - 0: DWC_ether_qos does<br>not flush the packet in the Rx Queue destined to this RxDMA Channel when it is in STOP state. This<br>might cause head-of-line blocking in the corresponding RxQueue. Note: The stopping of packet flow from<br>a Rx DMA Channel to the application by setting RPF works only when there is one-to-one mapping of Rx<br>Queue to Rx DMA channels. In Dynamic mapping mode, setting RPF bit in any DMA_CH(#i)_Rx_Control<br>register might flush packets from unintended Rx Queues which are destined to the stopped Rx DMA<br>Channel.<br>0b - Rx Packet Flush is disabled<br>1b - Rx Packet Flush is enabled|
|30-28|Reserved.|
|Reserved_30_2<br>8||
|27-24|Reserved.|
|Reserved_RQO<br>S||
|23<br>Reserved_23|Reserved.|
|22<br>ERIC|Early Receive Interrupt Control When this bit is set, Early Receive Interrupt (ERI) status is set after the<br>completion of every burst transfer of data from the Rx DMA to the buffer. When this bit is reset, ERI is set<br>only after a complete buffer is filled up by the RxDMA.<br>0b - Early Receive Interrupt is disabled<br>1b - Early Receive Interrupt is enabled<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4049 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|21-16<br>RxPBL|Receive Programmable Burst Length These bits indicate the maximum number of beats to be transferred<br>in one DMA block data transfer. The DMA always attempts max burst as specified in PBL each time it<br>starts a burst transfer on the application bus. You can program PBL with any of the following values:<br>1, 2, 4, 8, 16, or 32. Any other value results in undefined behavior. To transfer more than 32 beats,<br>perform the following steps: 1. Set the 8xPBL mode in the DMA_CH0_Control register. 2. Set the RxPBL.<br>Note: The maximum value of RxPBL must be less than or equal to half the Rx Queue size (RQS field<br>of MTL_RxQ(#i)_Operation_Mode register) in terms of beats. This is required so that the Rx Queue has<br>space to store at least another Rx PBL worth of data while the Rx DMA is transferring a block of data.<br>For example, in 64-bit data width configurations the total locations in Rx Queue of size 512 bytes is 64,<br>so RxPBL and 8xPBL needs to be programmed to less than or equal to 32.|
|15|Reserved.|
|Reserved_15||
|14-4<br>RBSZ_13_y|Receive Buffer size High RBSZ[13:0] is split into two fields higher RBSZ_13_y and lower RBSZ_x_0.<br>The RBSZ[13:0] field indicates the size of the Rx buffers specified in bytes. The maximum buffer size<br>is limited to 16K bytes. The buffer size is applicable to payload buffers when split headers are enabled.<br>Note: The buffer size must be a multiple of 4, 8, or 16 depending on the data bus widths (32-bit, 64-bit,<br>or 128-bit respectively). This is required even if the value of buffer address pointer is not aligned to data<br>bus width. Hence the lower RBSZ_x_0 bits are read-only and the value is considered as all-zero. Thus<br>the RBSZ_13_y indicates the buffer size in terms of locations (with the width same as bus-width).|
|3-1<br>RBSZ_x_0|Receive Buffer size Low RBSZ[13:0] is split into two fields RBSZ_13_y and RBSZ_x_0. The RBSZ_x_0 is<br>the lower field whose width is based on data bus width of the configuration. This field is of width 2, 3, or 4<br>bits for 32-bit, 64-bit, or 128-bit data bus width respectively. This field is read-only (RO).|
|0<br>SR|Start or Stop Receive When this bit is set, the DMA tries to acquire the descriptor from the<br>Receive list and processes the incoming packets. The DMA tries to acquire descriptor from either<br>of the following positions: - The current position in the list This is the address set by the<br>DMA_CH0_RxDesc_List_Address register. - The position at which the Rx process was previously<br>stopped If the DMA does not own the current descriptor, the reception is suspended and the RBU bit of<br>the DMA_CH0_Status register is set. The Start Receive command is effective only when the reception<br>is stopped. If the command is issued before setting the DMA_CH0_RxDesc_List_Address register, the<br>DMA behavior is unpredictable. When this bit is reset, the Rx DMA operation is stopped after the transfer<br>of the current packet. The next descriptor position in the Receive list is saved, and it becomes the current<br>position after the Rx process is restarted. The Stop Receive command is effective only when the Rx<br>process is in the Running (waiting for Rx packet) or Suspended state.<br>0b - Stop Receive<br>1b - Start Receive|



## 75.7.361 (DMA_CH1_TxDesc_List_Address) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH1_TxDesc_List_|1194h|
|Address||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4050 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Function 

The Channeli Tx Descriptor List Address register points the DMA to the start of Transmit descriptor list. The descriptor lists reside in the physical memory space of the application and must be Word, Dword, or Lword-aligned (for 32-bit, 64-bit, or 128-bit data bus). The DMA internally converts it to bus width aligned address by making the corresponding LSB to low. You can write to this register only when the Tx DMA has stopped, that is, the ST bit is set to zero in DMA_CH0_Tx_Control register. When stopped, this register can be written with a new descriptor list address. When you set the ST bit to 1, the DMA takes the newly-programmed descriptor base address. If this register is not changed when the ST bit is set to 0, the DMA takes the descriptor address where it was stopped earlier. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4051-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>TDESLA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_LSb<br>TDESLA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-3<br>TDESLA|Start of Transmit List This field contains the base address of the first descriptor in the Transmit descriptor<br>list. The DMA ignores the LSB bits (1:0, 2:0, or 3:0) for 32-bit, 64-bit, or 128-bit bus width and internally<br>takes these bits as all-zero. Therefore, these LSB bits are read-only (RO). The width of this field depends<br>on the configuration: - 31:2 for 32-bit configuration - 31:3 for 64-bit configuration - 31:4 for 128-bit<br>configuration|
|2-0|Reserved.|
|Reserved_LSb||



## 75.7.362 (DMA_CH1_RxDesc_List_Address) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH1_RxDesc_List|119Ch|
|_Address||



#### Function 

The Channeli Rx Descriptor List Address register points the DMA to the start of Receive descriptor list. This register points to the start of the Receive Descriptor List. The descriptor lists reside in the physical memory space of the application and must be Word, Dword, or Lword-aligned (for 32-bit, 64-bit, or 128-bit data bus). The DMA internally converts it to bus width aligned address by making the corresponding LS bits low. Writing to this register is permitted only when reception is stopped. When stopped, this register must be written to before the receive Start command is given. You can write to this register only 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4051 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

when Rx DMA has stopped, that is, SR bit is set to zero in DMA_CH0_Rx_Control register. When stopped, this register can be written with a new descriptor list address. When you set the SR bit to 1, the DMA takes the newly programmed descriptor base address. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4052-04.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>RDESLA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_LSb<br>RDESLA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-3<br>RDESLA|Start of Receive List This field contains the base address of the first descriptor in the Rx Descriptor list.<br>The DMA ignores the LSB bits (1:0, 2:0, or 3:0) for 32-bit, 64-bit, or 128-bit bus width and internally<br>takes these bits as all-zero. Therefore, these LSB bits are read-only (RO). The width of this field depends<br>on the configuration: - 31:2 for 32-bit configuration - 31:3 for 64-bit configuration - 31:4 for 128-bit<br>configuration|
|2-0|Reserved.|
|Reserved_LSb||



## 75.7.363 (DMA_CH1_TxDesc_Tail_Pointer) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH1_TxDesc_Tail_|11A0h|
|Pointer||



#### Function 

The Channeli Tx Descriptor Tail Pointer register points to an offset from the base and indicates the location of the last valid descriptor. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4052 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4053-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>TDTP<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_LSb<br>TDTP<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-3<br>TDTP|Transmit Descriptor Tail Pointer This field contains the tail pointer for the Tx descriptor ring. The software<br>writes the tail pointer to add more descriptors to the Tx channel. The hardware tries to transmit all<br>packets referenced by the descriptors between the head and the tail pointer registers. The width of this<br>field depends on the configuration: - 31:2 for 32-bit configuration - 31:3 for 64-bit configuration - 31:4 for<br>128-bit configuration|
|2-0|Reserved.|
|Reserved_LSb||



## 75.7.364 (DMA_CH1_RxDesc_Tail_Pointer) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH1_RxDesc_Tail|11A8h|
|_Pointer||



#### Function 

The Channeli Rx Descriptor Tail Pointer Points to an offset from the base and indicates the location of the last valid descriptor. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4053 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4054-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>RDTP<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_LSb<br>RDTP<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-3<br>RDTP|Receive Descriptor Tail Pointer This field contains the tail pointer for the Rx descriptor ring. The software<br>writes the tail pointer to add more descriptors to the Rx channel. The hardware tries to write all received<br>packets to the descriptors referenced between the head and the tail pointer registers. The width of this<br>field depends on the configuration: - 31:2 for 32-bit configuration - 31:3 for 64-bit configuration - 31:4 for<br>128-bit configuration|
|2-0|Reserved.|
|Reserved_LSb||



## 75.7.365 (DMA_CH1_TxDesc_Ring_Length) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH1_TxDesc_Ring<br>_Length|11ACh|



#### Function 

The Tx Descriptor Ring Length register contains the length of the Transmit descriptor ring. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4054 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4055-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_10<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_31_10<br>TDRL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-10|Reserved.|
|Reserved_31_1<br>0||
|9-0<br>TDRL|Transmit Descriptor Ring Length. This field sets the maximum number of Tx descriptors in the circular<br>descriptor ring. The maximum number of descriptors is limited to 1K descriptors. NXP recommends a<br>minimum ring descriptor length of 4. For example, You can program any value up to 0x3FF in this field.<br>This field is 10 bits wide, if you program 0x3FF, you can have 1024 descriptors. If you want to have 10<br>descriptors, program it to a value of 0x9.|



## 75.7.366 (DMA_CH1_Rx_Control2) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH1_Rx_Control2|11B0h|



#### Function 

The Channeli Receive Control register controls the Rx features such as Rx Descriptor Ring Length and Alternate Rx Buffer Size. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4055 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4056-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R Reserved_31_24<br>ARBS  e...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_x_10<br>RDRL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-24|Reserved.|
|Reserved_31_2<br>4||
|23-17<br>ARBS|Alternate Receive Buffer Size Indicates size in bytes for Buffer 1 when ARBS is programmed to a<br>non-zero value (when split header feature is not enabled). When split header feature is enabled, ARBS<br>indicates the buffer size for header data. The maximum alternate buffer is limited to 1020, 1016 or<br>1008-bytes depending on the data bus widths (32-bit, 64-bit, or 128-bit respectively). When ARBS=0, Rx<br>Buffer1 and Rx Buffer2 sizes are based on RBSZ field of DMA_CH(#i)_Rx_Control. Width of ARBS field<br>is 8, 7 or 6-bits depending on the data bus widths (32-bit, 64-bit, or 128-bit respectively)|
|16-10|Reserved.|
|Reserved_x_10||
|9-0<br>RDRL|Receive Descriptor Ring Length This register sets the maximum number of Rx descriptors in the circular<br>descriptor ring. The maximum number of descriptors is limited to 1K descriptors. For example, You can<br>program any value up to 0x3FF in this field. This field is 10 bits wide, if you program 0x3FF, you can<br>have 1024 descriptors. If you want to have 10 descriptors, program it to a value of 0x9.|



## 75.7.367 (DMA_CH1_Interrupt_Enable) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH1_Interrupt_Ena|11B4h|
|ble||



#### Function 

The Channeli Interrupt Enable register enables the interrupts reported by the Status register. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4056 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||Reserve|d_31_16||||||||
|Reset<br>Bits|0<br>15|0<br>14|0<br>13|0<br>12|0<br>11|0<br>10|0<br>9|0<br>8|0<br>7|0<br>6|0<br>5|0<br>4|0<br>3|0<br>2|0<br>1|0<br>0|
|R<br>W|NIE|AIE|CDEE|FBEE|ERIE|ETIE|RWTE|RSE|RBUE|RIE|Re|served_5|_3|TBUE|TXSE|TIE|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-16|Reserved.|
|Reserved_31_1<br>6||
|15<br>NIE|Normal Interrupt Summary Enable When this bit is set, the normal interrupt summary is enabled. This<br>bit enables the following interrupts in the DMA_CH0_Status register: - Bit 0: Transmit Interrupt - Bit 2:<br>Transmit Buffer Unavailable - Bit 6: Receive Interrupt - Bit 11: Early Receive Interrupt When this bit is<br>reset, the normal interrupt summary is disabled.<br>0b - Normal Interrupt Summary is disabled<br>1b - Normal Interrupt Summary is enabled|
|14<br>AIE|Abnormal Interrupt Summary Enable When this bit is set, the abnormal interrupt summary is enabled.<br>This bit enables the following interrupts in the DMA_CH0_Status register: - Bit 1: Transmit Process<br>Stopped - Bit 7: Rx Buffer Unavailable - Bit 8: Receive Process Stopped - Bit 9: Receive Watchdog<br>Timeout - Bit 10: Early Transmit Interrupt - Bit 12: Fatal Bus Error - Bit 13: Context Descriptor Error<br>When this bit is reset, the abnormal interrupt summary is disabled.<br>0b - Abnormal Interrupt Summary is disabled<br>1b - Abnormal Interrupt Summary is enabled|
|13<br>CDEE|Context Descriptor Error Enable When this bit is set along with the AIE bit, the Descriptor error interrupt<br>is enabled. When this bit is reset, the Descriptor error interrupt is disabled.<br>0b - Context Descriptor Error is disabled<br>1b - Context Descriptor Error is enabled|
|12<br>FBEE|Fatal Bus Error Enable When this bit is set along with the AIE bit, the Fatal Bus error interrupt is enabled.<br>When this bit is reset, the Fatal Bus Error error interrupt is disabled.<br>0b - Fatal Bus Error is disabled<br>1b - Fatal Bus Error is enabled|
|11|Early Receive Interrupt Enable When this bit is set along with the NIE bit, the Early Receive interrupt is<br>enabled. When this bit is reset, the Early Receive interrupt is disabled.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4057 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|ERIE|0b - Early Receive Interrupt is disabled<br>1b - Early Receive Interrupt is enabled|
|10<br>ETIE|Early Transmit Interrupt Enable When this bit is set along with the AIE bit, the Early Transmit interrupt is<br>enabled. When this bit is reset, the Early Transmit interrupt is disabled.<br>0b - Early Transmit Interrupt is disabled<br>1b - Early Transmit Interrupt is enabled|
|9<br>RWTE|Receive Watchdog Timeout Enable When this bit is set along with the AIE bit, the Receive Watchdog<br>Timeout interrupt is enabled. When this bit is reset, the Receive Watchdog Timeout interrupt is disabled.<br>0b - Receive Watchdog Timeout is disabled<br>1b - Receive Watchdog Timeout is enabled|
|8<br>RSE|Receive Stopped Enable When this bit is set along with the AIE bit, the Receive Stopped Interrupt is<br>enabled. When this bit is reset, the Receive Stopped interrupt is disabled.<br>0b - Receive Stopped is disabled<br>1b - Receive Stopped is enabled|
|7<br>RBUE|Receive Buffer Unavailable Enable When this bit is set along with the AIE bit, the Receive Buffer<br>Unavailable interrupt is enabled. When this bit is reset, the Receive Buffer Unavailable interrupt is<br>disabled.<br>0b - Receive Buffer Unavailable is disabled<br>1b - Receive Buffer Unavailable is enabled|
|6<br>RIE|Receive Interrupt Enable When this bit is set along with the NIE bit, the Receive Interrupt is enabled.<br>When this bit is reset, the Receive Interrupt is disabled.<br>0b - Receive Interrupt is disabled<br>1b - Receive Interrupt is enabled|
|5-3<br>Reserved_5_3|Reserved.|
|2<br>TBUE|Transmit Buffer Unavailable Enable When this bit is set along with the NIE bit, the Transmit Buffer<br>Unavailable interrupt is enabled. When this bit is reset, the Transmit Buffer Unavailable interrupt is<br>disabled.<br>0b - Transmit Buffer Unavailable is disabled<br>1b - Transmit Buffer Unavailable is enabled|
|1<br>TXSE|Transmit Stopped Enable When this bit is set along with the AIE bit, the Transmission Stopped interrupt<br>is enabled. When this bit is reset, the Transmission Stopped interrupt is disabled.<br>0b - Transmit Stopped is disabled<br>1b - Transmit Stopped is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4058 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|0<br>TIE|Transmit Interrupt Enable When this bit is set along with the NIE bit, the Transmit Interrupt is enabled.<br>When this bit is reset, the Transmit Interrupt is disabled.<br>0b - Transmit Interrupt is disabled|
||1b - Transmit Interrupt is enabled|



## 75.7.368 (DMA_CH1_Rx_Interrupt_Watchdog_Timer) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH1_Rx_Interrupt_|11B8h|
|Watchdog_Timer||



#### Function 

The Receive Interrupt Watchdog Timer register indicates the watchdog timeout for Receive Interrupt (RI) from the DMA. When this register is written with a non-zero value, it enables the watchdog timer for the RI bit of the DMA_CHi_Status register. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||||||Reserve|d_31_18|||||||RWTU|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R<br>W||||Reserve|d_15_8|||||||RW|T|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



#### Fields 

|Field|Function|
|---|---|
|31-18|Reserved.|
|Reserved_31_1<br>8||
|17-16<br>RWTU|Receive Interrupt Watchdog Timer Count Units This fields indicates the number of system clock cycles<br>corresponding to one unit in RWT field. - 2'b00: 256 - 2'b01: 512 - 2'b10: 1024 - 2'b11: 2048 For<br>example, when RWT=2 and RWTU=1, the watchdog timer is set for 2*512=1024 system clock cycles.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4059 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|15-8|Reserved.|
|Reserved_15_8||
|7-0<br>RWT|Receive Interrupt Watchdog Timer Count This field indicates the number of system clock cycles,<br>multiplied by factor indicated in RWTU field, for which the watchdog timer is set. The watchdog timer<br>is triggered with the programmed value after the Rx DMA completes the transfer of a packet for which<br>the RI bit is not set in the DMA_CH(#i)_Status register, because of the setting of Interrupt Enable bit in<br>the corresponding descriptor RDES3[30]. When the watchdog timer runs out, the RI bit is set and the<br>timer is stopped. The watchdog timer is reset when the RI bit is set high because of automatic setting of<br>RI as per the Interrupt Enable bit RDES3[30] of any received packet.|



## 75.7.369 (DMA_CH1_Slot_Function_Control_Status) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH1_Slot_Functio|11BCh|
|n_Control_Status||



#### Function 

The Slot Function Control and Status register contains the control bits for slot function and the status for Transmit path. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||Reserved|_31_20|||||||R|SN||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||SIV|||||||Reserv|ed_3_2|ASC|ESC|
|Reset|0|0|0|0|0|1|1|1|1|1|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-20|Reserved.|
|Reserved_31_2<br>0||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4060 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|19-16<br>RSN|Reference Slot Number This field gives the current value of the reference slot number in the DMA. It is<br>used for slot comparison.|
|15-4<br>SIV|Slot Interval Value This field controls the period of the slot interval in which the TxDMA fetches the<br>scheduled packets. A value of 0 specifies the slot interval of 1 us while the maximum value 4095<br>specifies the slot interval of 4096us. The default/reset value is 0x07C which corresponds to slot interval<br>of 125us|
|3-2|Reserved.|
|Reserved_3_2||
|1<br>ASC|Advance Slot Check When set, this bit enables the DMA to fetch the data from the buffer when the slot<br>number (SLOTNUM) programmed in the Tx descriptor is - equal to the reference slot number given in<br>the RSN field or - ahead of the reference slot number by up to two slots This bit is applicable only when<br>the ESC bit is set.<br>0b - Advance Slot Check is disabled<br>1b - Advance Slot Check is enabled|
|0<br>ESC|Enable Slot Comparison When set, this bit enables the checking of the slot numbers programmed<br>in the Tx descriptor with the current reference given in the RSN field. The DMA fetches the data<br>from the corresponding buffer only when the slot number is - equal to the reference slot number or -<br>ahead of the reference slot number by one slot When reset, this bit disables the checking of the slot<br>numbers. The DMA fetches the data immediately after the descriptor is processed. Note: The UFO (UDP<br>Fragmentation over IPv4)/TSO/USO should not be enabled along with TBS/AVB Slot number check. The<br>UFO/TSO/USO involves multiple packets/segments/fragments transmission for single packet received<br>from application and the slot number check are applicable for fetching of only first segment/fragment. As<br>a result it might be difficult for software to specify slot number for subsequent packets.<br>0b - Slot Comparison is disabled<br>1b - Slot Comparison is enabled|



## 75.7.370 (DMA_CH1_Current_App_TxDesc) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH1_Current_App<br>_TxDesc|11C4h|



#### Function 

The Channeli Current Application Transmit Descriptor register points to the current Transmit descriptor read by the DMA. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4061 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4062-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R CURTDESAPTR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R CURTDESAPTR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-0<br>CURTDESAPT<br>R|Application Transmit Descriptor Address Pointer The DMA updates this pointer during Tx operation. This<br>pointer is cleared on reset.|



## 75.7.371 (DMA_CH1_Current_App_RxDesc) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH1_Current_App<br>_RxDesc|11CCh|



#### Function 

The Channeli Current Application Receive Descriptor register points to the current Receive descriptor read by the DMA. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||CURRD|ESAPTR||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||CURRD|ESAPTR||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4062 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Fields 

|Field|Function|
|---|---|
|31-0<br>CURRDESAPT<br>R|Application Receive Descriptor Address Pointer The DMA updates this pointer during Rx operation. This<br>pointer is cleared on reset.|



## 75.7.372 (DMA_CH1_Current_App_TxBuffer) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH1_Current_App|11D4h|
|_TxBuffer||



#### Function 

The Channeli Current Application Transmit Buffer Address register points to the current Tx buffer address read by the DMA. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||CURTB|UFAPTR||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||CURTB|UFAPTR||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-0<br>CURTBUFAPT<br>R|Application Transmit Buffer Address Pointer The DMA updates this pointer during Tx operation. This<br>pointer is cleared on reset.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4063 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## 75.7.373 (DMA_CH1_Current_App_RxBuffer) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH1_Current_App|11DCh|
|_RxBuffer||



#### Function 

The Channel 0 Current Application Receive Buffer Address register points to the current Rx buffer address read by the DMA. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4064-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R CURRBUFAPTR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R CURRBUFAPTR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-0<br>CURRBUFAPT<br>R|Application Receive Buffer Address Pointer The DMA updates this pointer during Rx operation. This<br>pointer is cleared on reset.|



## 75.7.374 (DMA_CH1_Status) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH1_Status|11E0h|



#### Function 

The software driver (application) reads the Status register during interrupt service routine or polling to determine the status of the DMA. Note: The number of DMA_CH(#i)_Status register in the configuration is the higher of number of Rx DMA Channels and Tx DMA Channels. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4064 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||Reserve|d_31_22||||||REB|||TEB||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|NIS|AIS|CDE|FBE|ERI|ETI|RWT|RPS|RBU|RI|Re|served_5|_3|TBU|TPS|TI|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-22|Reserved.|
|Reserved_31_2<br>2||
|21-19<br>REB|Rx DMA Error Bits This field indicates the type of error that caused a Bus Error. For example, error<br>response on the AHB or AXI interface. - Bit 21 -- 1'b1: Error during data transfer by Rx DMA -- 1'b0: No<br>Error during data transfer by Rx DMA - Bit 20 -- 1'b1: Error during descriptor access -- 1'b0: Error during<br>data buffer access - Bit 19 -- 1'b1: Error during read transfer -- 1'b0: Error during write transfer This field<br>is valid only when the FBE bit is set. This field does not generate an interrupt.|
|18-16<br>TEB|Tx DMA Error Bits This field indicates the type of error that caused a Bus Error. For example, error<br>response on the AHB or AXI interface. - Bit 18 -- 1'b1: Error during data transfer by Tx DMA -- 1'b0: No<br>Error during data transfer by Tx DMA - Bit 17 -- 1'b1: Error during descriptor access -- 1'b0: Error during<br>data buffer access - Bit 16 -- 1'b1: Error during read transfer -- 1'b0: Error during write transfer This field<br>is valid only when the FBE bit is set. This field does not generate an interrupt.|
|15<br>NIS|Normal Interrupt Summary Normal Interrupt Summary bit value is the logical OR of the following bits<br>when the corresponding interrupt bits are enabled in the DMA_CH0_Interrupt_Enable register: - Bit 0:<br>Transmit Interrupt - Bit 2: Transmit Buffer Unavailable - Bit 6: Receive Interrupt - Bit 11: Early Receive<br>Interrupt Only unmasked bits (interrupts for which interrupt enable is set in DMA_CH0_Interrupt_Enable<br>register) affect the Normal Interrupt Summary bit. This is a sticky bit. You must clear this bit (by writing<br>1 to this bit) each time a corresponding bit which causes NIS to be set is cleared. Access restriction<br>applies. Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - Normal Interrupt Summary status not detected<br>1b - Normal Interrupt Summary status detected|
|14<br>AIS|Abnormal Interrupt Summary Abnormal Interrupt Summary bit value is the logical OR of the following<br>when the corresponding interrupt bits are enabled in the DMA_CH0_Interrupt_Enable register: - Bit 1:<br>Transmit Process Stopped - Bit 7: Receive Buffer Unavailable - Bit 8: Receive Process Stopped - Bit 10:<br>Early Transmit Interrupt - Bit 12: Fatal Bus Error - Bit 13: Context Descriptor Error Only unmasked bits<br>affect the Abnormal Interrupt Summary bit. This is a sticky bit. You must clear this bit (by writing 1 to<br>this bit) each time a corresponding bit, which causes AIS to be set, is cleared. Access restriction applies.<br>Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no effect.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4065 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Table continued from the previous page... 

|Field|Function<br>0b - Abnormal Interrupt Summary status not detected<br>1b - Abnormal Interrupt Summary status detected|
|---|---|
|13<br>CDE|Context Descriptor Error This bit indicates that the DMA Tx/Rx engine received a descriptor error, which<br>indicates invalid context in the middle of packet flow ( intermediate descriptor) or all one's descriptor in<br>Tx case and on Rx side it indicates DMA has read a descriptor with either of the buffer address as ones<br>which is considered to be invalid. Access restriction applies. Self-set to 1 on internal event. Setting 1<br>clears. Setting 0 has no effect.<br>0b - Context Descriptor Error status not detected<br>1b - Context Descriptor Error status detected|
|12<br>FBE|Fatal Bus Error This bit indicates that a bus error occurred (as described in the EB field). When this<br>bit is set, the corresponding DMA channel engine disables all bus accesses. Access restriction applies.<br>Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - Fatal Bus Error status not detected<br>1b - Fatal Bus Error status detected|
|11<br>ERI|Early Receive Interrupt This bit when set indicates that the RxDMA has completed the transfer of packet<br>data to the memory. In configurations supporting ERIC, - ERIC = 0: This bit is set only after the Rx DMA<br>has completely filled up a receive buffer with packet data. - ERIC = 1: This bit is set after every burst<br>transfer of data from the Rx DMA to the buffer. The setting of RI bit automatically clears this bit. Access<br>restriction applies. Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - Early Receive Interrupt status not detected<br>1b - Early Receive Interrupt status detected|
|10<br>ETI|Early Transmit Interrupt This bit when set indicates that the TxDMA has completed the transfer of packet<br>data to the MTL TXFIFO memory. In configurations supporting ERIC: - ETIC = 0: This bit is set only after<br>the Tx DMA has transferred a complete packet to MTL. - ETIC = 1: This bit is set after completion of<br>(partial) packet data transfer from buffers in the Transmit descriptor in which IOC = 1. Access restriction<br>applies. Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - Early Transmit Interrupt status not detected<br>1b - Early Transmit Interrupt status detected|
|9<br>RWT|Receive Watchdog Timeout This bit is asserted when a packet with length greater than 2,048 bytes<br>(10,240 bytes when Jumbo Packet mode is enabled) is received.<br>0b - Receive Watchdog Timeout status not detected<br>1b - Receive Watchdog Timeout status detected|
|8<br>RPS|Receive Process Stopped This bit is asserted when the Rx process enters the Stopped state. Access<br>restriction applies. Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - Receive Process Stopped status not detected<br>1b - Receive Process Stopped status detected|
|7|Receive Buffer Unavailable This bit indicates that the application owns the next descriptor in the<br>Receive list, and the DMA cannot acquire it. The Rx process is suspended. To resume processing|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4066 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|RBU|Rx descriptors, the application should change the ownership of the descriptor and issue a Receive Poll<br>Demand command. If this command is not issued, the Rx process resumes when the next recognized<br>incoming packet is received. In ring mode, the application should advance the Receive Descriptor Tail<br>Pointer register of a channel. This bit is set only when the DMA owns the previous Rx descriptor. Access<br>restriction applies. Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - Receive Buffer Unavailable status not detected<br>1b - Receive Buffer Unavailable status detected|
|6<br>RI|Receive Interrupt This bit indicates that the packet reception is complete. When packet reception is<br>complete, Bit 31 of RDES3 is reset in the last descriptor, and the specific packet status information<br>is updated in the descriptor. The reception remains in the Running state. Access restriction applies.<br>Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - Receive Interrupt status not detected<br>1b - Receive Interrupt status detected|
|5-3<br>Reserved_5_3|Reserved.|
|2<br>TBU|Transmit Buffer Unavailable This bit indicates that the application owns the next descriptor in the<br>Transmit list, and the DMA cannot acquire it. Transmission is suspended. The TPS0 field of the<br>DMA_Debug_Status0 register explains the Transmit Process state transitions. To resume processing the<br>Transmit descriptors, the application should do the following: - Change the ownership of the descriptor<br>by setting Bit 31 of TDES3. - Issue a Transmit Poll Demand command. For ring mode, the application<br>should advance the Transmit Descriptor Tail Pointer register of a channel. Access restriction applies.<br>Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - Transmit Buffer Unavailable status not detected<br>1b - Transmit Buffer Unavailable status detected|
|1<br>TPS|Transmit Process Stopped This bit is set when the transmission is stopped. Access restriction applies.<br>Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - Transmit Process Stopped status not detected<br>1b - Transmit Process Stopped status detected|
|0<br>TI|Transmit Interrupt This bit indicates that the packet transmission is complete. When transmission is<br>complete, Bit 31 of TDES3 is reset in the last descriptor, and the specific packet status information is<br>updated in the descriptor. Access restriction applies. Self-set to 1 on internal event. Setting 1 clears.<br>Setting 0 has no effect.<br>0b - Transmit Interrupt status not detected<br>1b - Transmit Interrupt status detected|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4067 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## 75.7.375 (DMA_CH1_Miss_Frame_Cnt) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH1_Miss_Frame_|11E4h|
|Cnt||



#### Function 

This register has the number of packet counter that got dropped by the DMA either due to Bus Error or due to programming RPF field in DMA_CH${i}_Rx_Control register. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4068-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_16<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R MFCO  Reserved_14_11  MFC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-16|Reserved.|
|Reserved_31_1<br>6||
|15<br>MFCO|Overflow status of the MFC Counter When this bit is set then the MFC counter does not get incremented<br>further. The bit gets cleared when this register is read. Access restriction applies. Clears on read.<br>Self-set to 1 on internal event.<br>0b - Miss Frame Counter overflow not occurred<br>1b - Miss Frame Counter overflow occurred|
|14-11|Reserved.|
|Reserved_14_1<br>1||
|10-0<br>MFC|Dropped Packet Counters This counter indicates the number of packet counters that are dropped by<br>the DMA either because of bus error or because of programing RPF field in DMA_CH${i}_Rx_Control<br>register. The counter gets cleared when this register is read. Access restriction applies. Clears on read.<br>Self-set to 1 on internal event.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4068 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## 75.7.376 (DMA_CH1_RXP_Accept_Cnt) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH1_RXP_Accept|11E8h|
|_Cnt||



#### Function 

The DMA_CH(#i)_RXP_Accept_Cnt registers provides the count of the number of frames accepted by Rx Parser. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4069-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>RXPA<br>R RXPAC<br>COF<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXPAC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31<br>RXPACOF|Rx Parser Accept Counter Overflow Bit When set, this bit indicates that the RXPAC Counter field<br>crossed the maximum limit. Access restriction applies. Clears on read. Self-set to 1 on internal event.<br>0b - Rx Parser Accept Counter overflow not occurred|
||1b - Rx Parser Accept Counter overflow occurred|
|30-0<br>RXPAC|Rx Parser Accept Counter This 31-bit counter is implemented when a Rx Parser Accept a packet due to<br>AF =1. The counter is cleared when the register is read.|



## 75.7.377 (DMA_CH1_RX_ERI_Cnt) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH1_RX_ERI_Cnt|11ECh|



#### Function 

The DMA_CH(#i)_RX_ERI_Cnt registers provides the count of the number of times ERI was asserted. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4069 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4070-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_12<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_31_12  ECNT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-12|Reserved.|
|Reserved_31_1<br>2||
|11-0<br>ECNT|ERI Counter When ERIC bit of DMA_CH(#i)_RX_Control register is set, this counter increments for burst<br>transfer completed by the Rx DMA from the start of packet transfer. This counter is reset at the start of<br>new packet.|



## 75.7.378 (DMA_CH2_Control) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH2_Control|1200h|



#### Function 

The DMA Channeli Control register specifies the MSS value for segmentation, length to skip between two descriptors, and also the features such as header splitting and 8xPBL mode. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4070 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4071-01.png)


<!-- Start of picture text -->
Gigabit Ethernet Media Access Controller (GMAC)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R Reserved_31_25  Reserved_23_21<br>SPH  DSL  e... PBLx8<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserved_15_1<br>R Reserved_MSS<br>4<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-25|Reserved.|
|Reserved_31_2<br>5||
|24<br>SPH|Split Headers When this bit is set, the DMA splits the header and payload in the Receive path. The DMA<br>writes the header to the Buffer Address1 of RDES0. The DMA writes the payload to the buffer to which<br>the Buffer Address2 is pointing. The software must ensure that the header fits into the Receive buffers. If<br>the header length exceeds the receive buffer size, the DMA does not split the header and payload. This<br>bit is available only if Enable Split Header Structure option is selected.<br>0b - Split Headers feature is disabled<br>1b - Split Headers feature is enabled|
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20-18<br>DSL|Descriptor Skip Length This bit specifies the Word, Dword, or Lword number (depending on the 32-bit,<br>64-bit, or 128-bit bus) to skip between two unchained descriptors. The address skipping starts from the<br>end of the current descriptor to the start of the next descriptor. When the DSL value is equal to zero, the<br>DMA takes the descriptor table as contiguous.|
|17|Reserved.|
|Reserved_17||
|16<br>PBLx8|8xPBL mode When this bit is set, the PBL value programmed in Bits[21:16] in DMA_CH(#i)_Tx_Control<br>and Bits[21:16] in DMA_CH(#i)_Rx_Control is multiplied by eight times. Therefore, the DMA transfers the<br>data in 8, 16, 32, 64, 128, and 256 beats depending on the PBL value.<br>0b - 8xPBL mode is disabled|
||1b - 8xPBL mode is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4071 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4072-03.png)


<!-- Start of picture text -->
Field Function<br>15-14 Reserved.<br>Reserved_15_1<br>4<br>13-0 Reserved.<br>Reserved_MSS<br><!-- End of picture text -->

## 75.7.379 (DMA_CH2_Tx_Control) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH2_Tx_Control|1204h|



#### Function 

The DMA Channeli Transmit Control register controls the Tx features such as PBL, TCP segmentation, and Tx Channel weights. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4072-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv Reserv<br>R Reserved_TQOS<br>e... TFSEL  EDSE  e... ETIC  TxPBL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv Reserved_TSE Reserv<br>R Reserved_11_5<br>e... _MO... e... OSF  TCW  ST<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31|Reserved.|
|Reserved_31||
|30-29<br>TFSEL|TBS Fetch Select Select bits for one of the four DMA_TBS_CTRL register fields (FTOS,FGSN,FTOV) for<br>the channel Values: - 2'b00: DMA_TBS_CTRL0 - 2'b01: DMA_TBS_CTRL1 - 2'b10: DMA_TBS_CTRL2 -<br>2'b11: DMA_TBS_CTRL3 (Reserved if DWC_EQOS_NUM_DMA_TX_CH=3)|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4072 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|28<br>EDSE|Enhanced Descriptor Enable When this bit is set, the corresponding channel uses Enhanced Descriptors<br>that are 32 Bytes for both Normal and Context Descriptors. When reset, the corresponding channel uses<br>the descriptors that are 16 Bytes.<br>0b - Enhanced Descriptor is disabled<br>1b - Enhanced Descriptor is enabled|
|27-24|Reserved.|
|Reserved_TQO<br>S||
|23<br>Reserved_23|Reserved.|
|22<br>ETIC|Early Transmit Interrupt Control When this bit is set, Early Transmit Interrupt (ETI) status is set after<br>completion of transfer of data from buffers of a transmit descriptor in which IOC bit (TDES2[31]) is set.<br>When this bit is reset, ETI is set only after a complete packet is transferred to the MTL TX FIFO memory.<br>0b - Early Transmit Interrupt is disabled<br>1b - Early Transmit Interrupt is enabled|
|21-16<br>TxPBL|Transmit Programmable Burst Length These bits indicate the maximum number of beats to be<br>transferred in one DMA block data transfer. The DMA always attempts max burst as specified in PBL<br>each time it starts a burst transfer on the application bus. You can program PBL with any of the following<br>values: 1, 2, 4, 8, 16, or 32. Any other value results in undefined behavior. To transfer more than 32<br>beats, perform the following steps: 1. Set the 8xPBL mode in DMA_CH0_Control register. 2. Set the<br>TxPBL. Note: The maximum value of TxPBL must be less than or equal to half the Tx Queue size<br>(TQS field of MTL_TxQ(#i)_Operation_Mode register) in terms of beats. This is required so that the Tx<br>Queue has space to store at least another Tx PBL worth of data while the MTL Tx Queue Controller is<br>transferring data to MAC. For example, in 64-bit data width configurations the total locations in Tx Queue<br>of size 512 bytes is 64, TxPBL and 8xPBL needs to be programmed to less than or equal to 32.|
|15<br>Reserved_IPBL|Reserved.|
|14-13|Reserved.|
|Reserved_TSE_<br>MODE||
|12<br>Reserved_TSE|Reserved.|
|11-5<br>Reserved_11_5|Reserved.|
|4<br>OSF|Operate on Second Packet When this bit is set, it instructs the DMA to process the second packet of the<br>Transmit data even before the status for the first packet is obtained.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4073 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Operate on Second Packet disabled<br>1b - Operate on Second Packet enabled|
|3-1<br>TCW|Transmit Channel Weight This field indicates the weight assigned to the corresponding Transmit<br>channel. When reset is complete, this field is set to 0 for all channels by default, resulting in equal<br>weights to all channels.|
|0<br>ST|Start or Stop Transmission Command When this bit is set, transmission is placed in the Running state.<br>The DMA checks the Transmit list at the current position for a packet to be transmitted. The DMA tries<br>to acquire descriptor from either of the following positions: - The current position in the list This is the<br>base address of the Transmit list set by the DMA_CH0_TxDesc_List_Address register. - The position<br>at which the transmission was previously stopped If the DMA does not own the current descriptor, the<br>transmission enters the Suspended state and the TBU bit of the DMA_CH0_Status register is set. The<br>Start Transmission command is effective only when the transmission is stopped. If the command is<br>issued before setting the DMA_CH0_TxDesc_List_Address register, the DMA behavior is unpredictable.<br>When this bit is reset, the transmission process is placed in the Stopped state after completing the<br>transmission of the current packet. The Next Descriptor position in the Transmit list is saved, and it<br>becomes the current position when the transmission is restarted. To change the list address, you need<br>to program DMA_CH0_TxDesc_List_Address register with a new value when this bit is reset. The new<br>value is considered when this bit is set again. The stop transmission command is effective only when the<br>transmission of the current packet is complete or the transmission is in the Suspended state.<br>0b - Stop Transmission Command<br>1b - Start Transmission Command|



## 75.7.380 (DMA_CH2_Rx_Control) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH2_Rx_Control|1208h|



#### Function 

The DMA Channeli Receive Control register controls the Rx features such as PBL, buffer size, and extended status. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4074 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4075-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R Reserved_30_28  Reserved_RQOS<br>RPF  e... ERIC  RxPBL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv<br>R RBSZ_x_0<br>e... RBSZ_13_y  SR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31<br>RPF|Rx Packet Flush. - 1: DWC_ether_qos automatically flushes the packet from the Rx Queues destined<br>to this DMA Rx Channel, when it is stopped. When this bit remains set and the DMA is re-started by<br>the software driver, the packets residing in the Rx Queues that were received when this RxDMA was<br>stopped, are flushed out. The packets that are received by the MAC after the RxDMA is re-started are<br>routed to the RxDMA. The flushing is done on the Read side of the Rx Queue. - 0: DWC_ether_qos does<br>not flush the packet in the Rx Queue destined to this RxDMA Channel when it is in STOP state. This<br>might cause head-of-line blocking in the corresponding RxQueue. Note: The stopping of packet flow from<br>a Rx DMA Channel to the application by setting RPF works only when there is one-to-one mapping of Rx<br>Queue to Rx DMA channels. In Dynamic mapping mode, setting RPF bit in any DMA_CH(#i)_Rx_Control<br>register might flush packets from unintended Rx Queues which are destined to the stopped Rx DMA<br>Channel.<br>0b - Rx Packet Flush is disabled<br>1b - Rx Packet Flush is enabled|
|30-28|Reserved.|
|Reserved_30_2<br>8||
|27-24|Reserved.|
|Reserved_RQO<br>S||
|23<br>Reserved_23|Reserved.|
|22<br>ERIC|Early Receive Interrupt Control When this bit is set, Early Receive Interrupt (ERI) status is set after the<br>completion of every burst transfer of data from the Rx DMA to the buffer. When this bit is reset, ERI is set<br>only after a complete buffer is filled up by the RxDMA.<br>0b - Early Receive Interrupt is disabled<br>1b - Early Receive Interrupt is enabled<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4075 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|21-16<br>RxPBL|Receive Programmable Burst Length These bits indicate the maximum number of beats to be transferred<br>in one DMA block data transfer. The DMA always attempts max burst as specified in PBL each time it<br>starts a burst transfer on the application bus. You can program PBL with any of the following values:<br>1, 2, 4, 8, 16, or 32. Any other value results in undefined behavior. To transfer more than 32 beats,<br>perform the following steps: 1. Set the 8xPBL mode in the DMA_CH0_Control register. 2. Set the RxPBL.<br>Note: The maximum value of RxPBL must be less than or equal to half the Rx Queue size (RQS field<br>of MTL_RxQ(#i)_Operation_Mode register) in terms of beats. This is required so that the Rx Queue has<br>space to store at least another Rx PBL worth of data while the Rx DMA is transferring a block of data.<br>For example, in 64-bit data width configurations the total locations in Rx Queue of size 512 bytes is 64,<br>so RxPBL and 8xPBL needs to be programmed to less than or equal to 32.|
|15|Reserved.|
|Reserved_15||
|14-4<br>RBSZ_13_y|Receive Buffer size High RBSZ[13:0] is split into two fields higher RBSZ_13_y and lower RBSZ_x_0.<br>The RBSZ[13:0] field indicates the size of the Rx buffers specified in bytes. The maximum buffer size<br>is limited to 16K bytes. The buffer size is applicable to payload buffers when split headers are enabled.<br>Note: The buffer size must be a multiple of 4, 8, or 16 depending on the data bus widths (32-bit, 64-bit,<br>or 128-bit respectively). This is required even if the value of buffer address pointer is not aligned to data<br>bus width. Hence the lower RBSZ_x_0 bits are read-only and the value is considered as all-zero. Thus<br>the RBSZ_13_y indicates the buffer size in terms of locations (with the width same as bus-width).|
|3-1<br>RBSZ_x_0|Receive Buffer size Low RBSZ[13:0] is split into two fields RBSZ_13_y and RBSZ_x_0. The RBSZ_x_0 is<br>the lower field whose width is based on data bus width of the configuration. This field is of width 2, 3, or 4<br>bits for 32-bit, 64-bit, or 128-bit data bus width respectively. This field is read-only (RO).|
|0<br>SR|Start or Stop Receive When this bit is set, the DMA tries to acquire the descriptor from the<br>Receive list and processes the incoming packets. The DMA tries to acquire descriptor from either<br>of the following positions: - The current position in the list This is the address set by the<br>DMA_CH0_RxDesc_List_Address register. - The position at which the Rx process was previously<br>stopped If the DMA does not own the current descriptor, the reception is suspended and the RBU bit of<br>the DMA_CH0_Status register is set. The Start Receive command is effective only when the reception<br>is stopped. If the command is issued before setting the DMA_CH0_RxDesc_List_Address register, the<br>DMA behavior is unpredictable. When this bit is reset, the Rx DMA operation is stopped after the transfer<br>of the current packet. The next descriptor position in the Receive list is saved, and it becomes the current<br>position after the Rx process is restarted. The Stop Receive command is effective only when the Rx<br>process is in the Running (waiting for Rx packet) or Suspended state.<br>0b - Stop Receive<br>1b - Start Receive|



## 75.7.381 (DMA_CH2_TxDesc_List_Address) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH2_TxDesc_List_|1214h|
|Address||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4076 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Function 

The Channeli Tx Descriptor List Address register points the DMA to the start of Transmit descriptor list. The descriptor lists reside in the physical memory space of the application and must be Word, Dword, or Lword-aligned (for 32-bit, 64-bit, or 128-bit data bus). The DMA internally converts it to bus width aligned address by making the corresponding LSB to low. You can write to this register only when the Tx DMA has stopped, that is, the ST bit is set to zero in DMA_CH0_Tx_Control register. When stopped, this register can be written with a new descriptor list address. When you set the ST bit to 1, the DMA takes the newly-programmed descriptor base address. If this register is not changed when the ST bit is set to 0, the DMA takes the descriptor address where it was stopped earlier. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4077-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>TDESLA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_LSb<br>TDESLA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-3<br>TDESLA|Start of Transmit List This field contains the base address of the first descriptor in the Transmit descriptor<br>list. The DMA ignores the LSB bits (1:0, 2:0, or 3:0) for 32-bit, 64-bit, or 128-bit bus width and internally<br>takes these bits as all-zero. Therefore, these LSB bits are read-only (RO). The width of this field depends<br>on the configuration: - 31:2 for 32-bit configuration - 31:3 for 64-bit configuration - 31:4 for 128-bit<br>configuration|
|2-0|Reserved.|
|Reserved_LSb||



## 75.7.382 (DMA_CH2_RxDesc_List_Address) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH2_RxDesc_List|121Ch|
|_Address||



#### Function 

The Channeli Rx Descriptor List Address register points the DMA to the start of Receive descriptor list. This register points to the start of the Receive Descriptor List. The descriptor lists reside in the physical memory space of the application and must be Word, Dword, or Lword-aligned (for 32-bit, 64-bit, or 128-bit data bus). The DMA internally converts it to bus width aligned address by making the corresponding LS bits low. Writing to this register is permitted only when reception is stopped. When stopped, this register must be written to before the receive Start command is given. You can write to this register only 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4077 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

when Rx DMA has stopped, that is, SR bit is set to zero in DMA_CH0_Rx_Control register. When stopped, this register can be written with a new descriptor list address. When you set the SR bit to 1, the DMA takes the newly programmed descriptor base address. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4078-04.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>RDESLA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_LSb<br>RDESLA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-3<br>RDESLA|Start of Receive List This field contains the base address of the first descriptor in the Rx Descriptor list.<br>The DMA ignores the LSB bits (1:0, 2:0, or 3:0) for 32-bit, 64-bit, or 128-bit bus width and internally<br>takes these bits as all-zero. Therefore, these LSB bits are read-only (RO). The width of this field depends<br>on the configuration: - 31:2 for 32-bit configuration - 31:3 for 64-bit configuration - 31:4 for 128-bit<br>configuration|
|2-0|Reserved.|
|Reserved_LSb||



## 75.7.383 (DMA_CH2_TxDesc_Tail_Pointer) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH2_TxDesc_Tail_|1220h|
|Pointer||



#### Function 

The Channeli Tx Descriptor Tail Pointer register points to an offset from the base and indicates the location of the last valid descriptor. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4078 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4079-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>TDTP<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_LSb<br>TDTP<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-3<br>TDTP|Transmit Descriptor Tail Pointer This field contains the tail pointer for the Tx descriptor ring. The software<br>writes the tail pointer to add more descriptors to the Tx channel. The hardware tries to transmit all<br>packets referenced by the descriptors between the head and the tail pointer registers. The width of this<br>field depends on the configuration: - 31:2 for 32-bit configuration - 31:3 for 64-bit configuration - 31:4 for<br>128-bit configuration|
|2-0|Reserved.|
|Reserved_LSb||



## 75.7.384 (DMA_CH2_RxDesc_Tail_Pointer) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH2_RxDesc_Tail<br>_Pointer|1228h|



#### Function 

The Channeli Rx Descriptor Tail Pointer Points to an offset from the base and indicates the location of the last valid descriptor. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4079 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4080-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>RDTP<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_LSb<br>RDTP<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-3<br>RDTP|Receive Descriptor Tail Pointer This field contains the tail pointer for the Rx descriptor ring. The software<br>writes the tail pointer to add more descriptors to the Rx channel. The hardware tries to write all received<br>packets to the descriptors referenced between the head and the tail pointer registers. The width of this<br>field depends on the configuration: - 31:2 for 32-bit configuration - 31:3 for 64-bit configuration - 31:4 for<br>128-bit configuration|
|2-0|Reserved.|
|Reserved_LSb||



## 75.7.385 (DMA_CH2_TxDesc_Ring_Length) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH2_TxDesc_Ring<br>_Length|122Ch|



#### Function 

The Tx Descriptor Ring Length register contains the length of the Transmit descriptor ring. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4080 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4081-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_10<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_31_10<br>TDRL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-10|Reserved.|
|Reserved_31_1<br>0||
|9-0<br>TDRL|Transmit Descriptor Ring Length. This field sets the maximum number of Tx descriptors in the circular<br>descriptor ring. The maximum number of descriptors is limited to 1K descriptors. NXP recommends a<br>minimum ring descriptor length of 4. For example, You can program any value up to 0x3FF in this field.<br>This field is 10 bits wide, if you program 0x3FF, you can have 1024 descriptors. If you want to have 10<br>descriptors, program it to a value of 0x9.|



## 75.7.386 (DMA_CH2_Rx_Control2) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH2_Rx_Control2|1230h|



#### Function 

The Channeli Receive Control register controls the Rx features such as Rx Descriptor Ring Length and Alternate Rx Buffer Size. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4081 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4082-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R Reserved_31_24<br>ARBS  e...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_x_10<br>RDRL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-24|Reserved.|
|Reserved_31_2<br>4||
|23-17<br>ARBS|Alternate Receive Buffer Size Indicates size in bytes for Buffer 1 when ARBS is programmed to a<br>non-zero value (when split header feature is not enabled). When split header feature is enabled, ARBS<br>indicates the buffer size for header data. The maximum alternate buffer is limited to 1020, 1016 or<br>1008-bytes depending on the data bus widths (32-bit, 64-bit, or 128-bit respectively). When ARBS=0, Rx<br>Buffer1 and Rx Buffer2 sizes are based on RBSZ field of DMA_CH(#i)_Rx_Control. Width of ARBS field<br>is 8, 7 or 6-bits depending on the data bus widths (32-bit, 64-bit, or 128-bit respectively)|
|16-10|Reserved.|
|Reserved_x_10||
|9-0<br>RDRL|Receive Descriptor Ring Length This register sets the maximum number of Rx descriptors in the circular<br>descriptor ring. The maximum number of descriptors is limited to 1K descriptors. For example, You can<br>program any value up to 0x3FF in this field. This field is 10 bits wide, if you program 0x3FF, you can<br>have 1024 descriptors. If you want to have 10 descriptors, program it to a value of 0x9.|



## 75.7.387 (DMA_CH2_Interrupt_Enable) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH2_Interrupt_Ena|1234h|
|ble||



#### Function 

The Channeli Interrupt Enable register enables the interrupts reported by the Status register. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4082 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||Reserve|d_31_16||||||||
|Reset<br>Bits|0<br>15|0<br>14|0<br>13|0<br>12|0<br>11|0<br>10|0<br>9|0<br>8|0<br>7|0<br>6|0<br>5|0<br>4|0<br>3|0<br>2|0<br>1|0<br>0|
|R<br>W|NIE|AIE|CDEE|FBEE|ERIE|ETIE|RWTE|RSE|RBUE|RIE|Re|served_5|_3|TBUE|TXSE|TIE|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-16|Reserved.|
|Reserved_31_1<br>6||
|15<br>NIE|Normal Interrupt Summary Enable When this bit is set, the normal interrupt summary is enabled. This<br>bit enables the following interrupts in the DMA_CH0_Status register: - Bit 0: Transmit Interrupt - Bit 2:<br>Transmit Buffer Unavailable - Bit 6: Receive Interrupt - Bit 11: Early Receive Interrupt When this bit is<br>reset, the normal interrupt summary is disabled.<br>0b - Normal Interrupt Summary is disabled<br>1b - Normal Interrupt Summary is enabled|
|14<br>AIE|Abnormal Interrupt Summary Enable When this bit is set, the abnormal interrupt summary is enabled.<br>This bit enables the following interrupts in the DMA_CH0_Status register: - Bit 1: Transmit Process<br>Stopped - Bit 7: Rx Buffer Unavailable - Bit 8: Receive Process Stopped - Bit 9: Receive Watchdog<br>Timeout - Bit 10: Early Transmit Interrupt - Bit 12: Fatal Bus Error - Bit 13: Context Descriptor Error<br>When this bit is reset, the abnormal interrupt summary is disabled.<br>0b - Abnormal Interrupt Summary is disabled<br>1b - Abnormal Interrupt Summary is enabled|
|13<br>CDEE|Context Descriptor Error Enable When this bit is set along with the AIE bit, the Descriptor error interrupt<br>is enabled. When this bit is reset, the Descriptor error interrupt is disabled.<br>0b - Context Descriptor Error is disabled<br>1b - Context Descriptor Error is enabled|
|12<br>FBEE|Fatal Bus Error Enable When this bit is set along with the AIE bit, the Fatal Bus error interrupt is enabled.<br>When this bit is reset, the Fatal Bus Error error interrupt is disabled.<br>0b - Fatal Bus Error is disabled<br>1b - Fatal Bus Error is enabled|
|11|Early Receive Interrupt Enable When this bit is set along with the NIE bit, the Early Receive interrupt is<br>enabled. When this bit is reset, the Early Receive interrupt is disabled.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4083 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|ERIE|0b - Early Receive Interrupt is disabled<br>1b - Early Receive Interrupt is enabled|
|10<br>ETIE|Early Transmit Interrupt Enable When this bit is set along with the AIE bit, the Early Transmit interrupt is<br>enabled. When this bit is reset, the Early Transmit interrupt is disabled.<br>0b - Early Transmit Interrupt is disabled<br>1b - Early Transmit Interrupt is enabled|
|9<br>RWTE|Receive Watchdog Timeout Enable When this bit is set along with the AIE bit, the Receive Watchdog<br>Timeout interrupt is enabled. When this bit is reset, the Receive Watchdog Timeout interrupt is disabled.<br>0b - Receive Watchdog Timeout is disabled<br>1b - Receive Watchdog Timeout is enabled|
|8<br>RSE|Receive Stopped Enable When this bit is set along with the AIE bit, the Receive Stopped Interrupt is<br>enabled. When this bit is reset, the Receive Stopped interrupt is disabled.<br>0b - Receive Stopped is disabled<br>1b - Receive Stopped is enabled|
|7<br>RBUE|Receive Buffer Unavailable Enable When this bit is set along with the AIE bit, the Receive Buffer<br>Unavailable interrupt is enabled. When this bit is reset, the Receive Buffer Unavailable interrupt is<br>disabled.<br>0b - Receive Buffer Unavailable is disabled<br>1b - Receive Buffer Unavailable is enabled|
|6<br>RIE|Receive Interrupt Enable When this bit is set along with the NIE bit, the Receive Interrupt is enabled.<br>When this bit is reset, the Receive Interrupt is disabled.<br>0b - Receive Interrupt is disabled<br>1b - Receive Interrupt is enabled|
|5-3<br>Reserved_5_3|Reserved.|
|2<br>TBUE|Transmit Buffer Unavailable Enable When this bit is set along with the NIE bit, the Transmit Buffer<br>Unavailable interrupt is enabled. When this bit is reset, the Transmit Buffer Unavailable interrupt is<br>disabled.<br>0b - Transmit Buffer Unavailable is disabled<br>1b - Transmit Buffer Unavailable is enabled|
|1<br>TXSE|Transmit Stopped Enable When this bit is set along with the AIE bit, the Transmission Stopped interrupt<br>is enabled. When this bit is reset, the Transmission Stopped interrupt is disabled.<br>0b - Transmit Stopped is disabled<br>1b - Transmit Stopped is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4084 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|0<br>TIE|Transmit Interrupt Enable When this bit is set along with the NIE bit, the Transmit Interrupt is enabled.<br>When this bit is reset, the Transmit Interrupt is disabled.<br>0b - Transmit Interrupt is disabled|
||1b - Transmit Interrupt is enabled|



## 75.7.388 (DMA_CH2_Rx_Interrupt_Watchdog_Timer) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH2_Rx_Interrupt_|1238h|
|Watchdog_Timer||



#### Function 

The Receive Interrupt Watchdog Timer register indicates the watchdog timeout for Receive Interrupt (RI) from the DMA. When this register is written with a non-zero value, it enables the watchdog timer for the RI bit of the DMA_CHi_Status register. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||||||Reserve|d_31_18|||||||RWTU|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R<br>W||||Reserve|d_15_8|||||||RW|T|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



#### Fields 

|Field|Function|
|---|---|
|31-18|Reserved.|
|Reserved_31_1<br>8||
|17-16<br>RWTU|Receive Interrupt Watchdog Timer Count Units This fields indicates the number of system clock cycles<br>corresponding to one unit in RWT field. - 2'b00: 256 - 2'b01: 512 - 2'b10: 1024 - 2'b11: 2048 For<br>example, when RWT=2 and RWTU=1, the watchdog timer is set for 2*512=1024 system clock cycles.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4085 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|15-8|Reserved.|
|Reserved_15_8||
|7-0<br>RWT|Receive Interrupt Watchdog Timer Count This field indicates the number of system clock cycles,<br>multiplied by factor indicated in RWTU field, for which the watchdog timer is set. The watchdog timer<br>is triggered with the programmed value after the Rx DMA completes the transfer of a packet for which<br>the RI bit is not set in the DMA_CH(#i)_Status register, because of the setting of Interrupt Enable bit in<br>the corresponding descriptor RDES3[30]. When the watchdog timer runs out, the RI bit is set and the<br>timer is stopped. The watchdog timer is reset when the RI bit is set high because of automatic setting of<br>RI as per the Interrupt Enable bit RDES3[30] of any received packet.|



## 75.7.389 (DMA_CH2_Slot_Function_Control_Status) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH2_Slot_Functio|123Ch|
|n_Control_Status||



#### Function 

The Slot Function Control and Status register contains the control bits for slot function and the status for Transmit path. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||Reserved|_31_20|||||||R|SN||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||SIV|||||||Reserv|ed_3_2|ASC|ESC|
|Reset|0|0|0|0|0|1|1|1|1|1|0|0|0|0|0|0|



#### Fields 

|Field|Function||
|---|---|---|
|31-20|Reserved.||
|Reserved_31_2|||
|0|||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4086 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|19-16<br>RSN|Reference Slot Number This field gives the current value of the reference slot number in the DMA. It is<br>used for slot comparison.|
|15-4<br>SIV|Slot Interval Value This field controls the period of the slot interval in which the TxDMA fetches the<br>scheduled packets. A value of 0 specifies the slot interval of 1 us while the maximum value 4095<br>specifies the slot interval of 4096us. The default/reset value is 0x07C which corresponds to slot interval<br>of 125us|
|3-2|Reserved.|
|Reserved_3_2||
|1<br>ASC|Advance Slot Check When set, this bit enables the DMA to fetch the data from the buffer when the slot<br>number (SLOTNUM) programmed in the Tx descriptor is - equal to the reference slot number given in<br>the RSN field or - ahead of the reference slot number by up to two slots This bit is applicable only when<br>the ESC bit is set.<br>0b - Advance Slot Check is disabled<br>1b - Advance Slot Check is enabled|
|0<br>ESC|Enable Slot Comparison When set, this bit enables the checking of the slot numbers programmed<br>in the Tx descriptor with the current reference given in the RSN field. The DMA fetches the data<br>from the corresponding buffer only when the slot number is - equal to the reference slot number or -<br>ahead of the reference slot number by one slot When reset, this bit disables the checking of the slot<br>numbers. The DMA fetches the data immediately after the descriptor is processed. Note: The UFO (UDP<br>Fragmentation over IPv4)/TSO/USO should not be enabled along with TBS/AVB Slot number check. The<br>UFO/TSO/USO involves multiple packets/segments/fragments transmission for single packet received<br>from application and the slot number check are applicable for fetching of only first segment/fragment. As<br>a result it might be difficult for software to specify slot number for subsequent packets.<br>0b - Slot Comparison is disabled<br>1b - Slot Comparison is enabled|



## 75.7.390 (DMA_CH2_Current_App_TxDesc) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH2_Current_App<br>_TxDesc|1244h|



#### Function 

The Channeli Current Application Transmit Descriptor register points to the current Transmit descriptor read by the DMA. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4087 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4088-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R CURTDESAPTR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R CURTDESAPTR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-0<br>CURTDESAPT<br>R|Application Transmit Descriptor Address Pointer The DMA updates this pointer during Tx operation. This<br>pointer is cleared on reset.|



## 75.7.391 (DMA_CH2_Current_App_RxDesc) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH2_Current_App<br>_RxDesc|124Ch|



#### Function 

The Channeli Current Application Receive Descriptor register points to the current Receive descriptor read by the DMA. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||CURRD|ESAPTR||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||CURRD|ESAPTR||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4088 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Fields 

|Field|Function|
|---|---|
|31-0<br>CURRDESAPT<br>R|Application Receive Descriptor Address Pointer The DMA updates this pointer during Rx operation. This<br>pointer is cleared on reset.|



## 75.7.392 (DMA_CH2_Current_App_TxBuffer) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH2_Current_App|1254h|
|_TxBuffer||



#### Function 

The Channeli Current Application Transmit Buffer Address register points to the current Tx buffer address read by the DMA. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||CURTB|UFAPTR||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||CURTB|UFAPTR||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-0<br>CURTBUFAPT<br>R|Application Transmit Buffer Address Pointer The DMA updates this pointer during Tx operation. This<br>pointer is cleared on reset.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4089 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## 75.7.393 (DMA_CH2_Current_App_RxBuffer) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH2_Current_App|125Ch|
|_RxBuffer||



#### Function 

The Channel 0 Current Application Receive Buffer Address register points to the current Rx buffer address read by the DMA. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4090-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R CURRBUFAPTR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R CURRBUFAPTR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-0<br>CURRBUFAPT<br>R|Application Receive Buffer Address Pointer The DMA updates this pointer during Rx operation. This<br>pointer is cleared on reset.|



## 75.7.394 (DMA_CH2_Status) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH2_Status|1260h|



#### Function 

The software driver (application) reads the Status register during interrupt service routine or polling to determine the status of the DMA. Note: The number of DMA_CH(#i)_Status register in the configuration is the higher of number of Rx DMA Channels and Tx DMA Channels. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4090 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||Reserve|d_31_22||||||REB|||TEB||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|NIS|AIS|CDE|FBE|ERI|ETI|RWT|RPS|RBU|RI|Re|served_5|_3|TBU|TPS|TI|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-22|Reserved.|
|Reserved_31_2<br>2||
|21-19<br>REB|Rx DMA Error Bits This field indicates the type of error that caused a Bus Error. For example, error<br>response on the AHB or AXI interface. - Bit 21 -- 1'b1: Error during data transfer by Rx DMA -- 1'b0: No<br>Error during data transfer by Rx DMA - Bit 20 -- 1'b1: Error during descriptor access -- 1'b0: Error during<br>data buffer access - Bit 19 -- 1'b1: Error during read transfer -- 1'b0: Error during write transfer This field<br>is valid only when the FBE bit is set. This field does not generate an interrupt.|
|18-16<br>TEB|Tx DMA Error Bits This field indicates the type of error that caused a Bus Error. For example, error<br>response on the AHB or AXI interface. - Bit 18 -- 1'b1: Error during data transfer by Tx DMA -- 1'b0: No<br>Error during data transfer by Tx DMA - Bit 17 -- 1'b1: Error during descriptor access -- 1'b0: Error during<br>data buffer access - Bit 16 -- 1'b1: Error during read transfer -- 1'b0: Error during write transfer This field<br>is valid only when the FBE bit is set. This field does not generate an interrupt.|
|15<br>NIS|Normal Interrupt Summary Normal Interrupt Summary bit value is the logical OR of the following bits<br>when the corresponding interrupt bits are enabled in the DMA_CH0_Interrupt_Enable register: - Bit 0:<br>Transmit Interrupt - Bit 2: Transmit Buffer Unavailable - Bit 6: Receive Interrupt - Bit 11: Early Receive<br>Interrupt Only unmasked bits (interrupts for which interrupt enable is set in DMA_CH0_Interrupt_Enable<br>register) affect the Normal Interrupt Summary bit. This is a sticky bit. You must clear this bit (by writing<br>1 to this bit) each time a corresponding bit which causes NIS to be set is cleared. Access restriction<br>applies. Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - Normal Interrupt Summary status not detected<br>1b - Normal Interrupt Summary status detected|
|14<br>AIS|Abnormal Interrupt Summary Abnormal Interrupt Summary bit value is the logical OR of the following<br>when the corresponding interrupt bits are enabled in the DMA_CH0_Interrupt_Enable register: - Bit 1:<br>Transmit Process Stopped - Bit 7: Receive Buffer Unavailable - Bit 8: Receive Process Stopped - Bit 10:<br>Early Transmit Interrupt - Bit 12: Fatal Bus Error - Bit 13: Context Descriptor Error Only unmasked bits<br>affect the Abnormal Interrupt Summary bit. This is a sticky bit. You must clear this bit (by writing 1 to<br>this bit) each time a corresponding bit, which causes AIS to be set, is cleared. Access restriction applies.<br>Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no effect.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4091 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Table continued from the previous page... 

|Field|Function<br>0b - Abnormal Interrupt Summary status not detected<br>1b - Abnormal Interrupt Summary status detected|
|---|---|
|13<br>CDE|Context Descriptor Error This bit indicates that the DMA Tx/Rx engine received a descriptor error, which<br>indicates invalid context in the middle of packet flow ( intermediate descriptor) or all one's descriptor in<br>Tx case and on Rx side it indicates DMA has read a descriptor with either of the buffer address as ones<br>which is considered to be invalid. Access restriction applies. Self-set to 1 on internal event. Setting 1<br>clears. Setting 0 has no effect.<br>0b - Context Descriptor Error status not detected<br>1b - Context Descriptor Error status detected|
|12<br>FBE|Fatal Bus Error This bit indicates that a bus error occurred (as described in the EB field). When this<br>bit is set, the corresponding DMA channel engine disables all bus accesses. Access restriction applies.<br>Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - Fatal Bus Error status not detected<br>1b - Fatal Bus Error status detected|
|11<br>ERI|Early Receive Interrupt This bit when set indicates that the RxDMA has completed the transfer of packet<br>data to the memory. In configurations supporting ERIC, - ERIC = 0: This bit is set only after the Rx DMA<br>has completely filled up a receive buffer with packet data. - ERIC = 1: This bit is set after every burst<br>transfer of data from the Rx DMA to the buffer. The setting of RI bit automatically clears this bit. Access<br>restriction applies. Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - Early Receive Interrupt status not detected<br>1b - Early Receive Interrupt status detected|
|10<br>ETI|Early Transmit Interrupt This bit when set indicates that the TxDMA has completed the transfer of packet<br>data to the MTL TXFIFO memory. In configurations supporting ERIC: - ETIC = 0: This bit is set only after<br>the Tx DMA has transferred a complete packet to MTL. - ETIC = 1: This bit is set after completion of<br>(partial) packet data transfer from buffers in the Transmit descriptor in which IOC = 1. Access restriction<br>applies. Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - Early Transmit Interrupt status not detected<br>1b - Early Transmit Interrupt status detected|
|9<br>RWT|Receive Watchdog Timeout This bit is asserted when a packet with length greater than 2,048 bytes<br>(10,240 bytes when Jumbo Packet mode is enabled) is received.<br>0b - Receive Watchdog Timeout status not detected<br>1b - Receive Watchdog Timeout status detected|
|8<br>RPS|Receive Process Stopped This bit is asserted when the Rx process enters the Stopped state. Access<br>restriction applies. Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - Receive Process Stopped status not detected<br>1b - Receive Process Stopped status detected|
|7|Receive Buffer Unavailable This bit indicates that the application owns the next descriptor in the<br>Receive list, and the DMA cannot acquire it. The Rx process is suspended. To resume processing|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4092 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|RBU|Rx descriptors, the application should change the ownership of the descriptor and issue a Receive Poll<br>Demand command. If this command is not issued, the Rx process resumes when the next recognized<br>incoming packet is received. In ring mode, the application should advance the Receive Descriptor Tail<br>Pointer register of a channel. This bit is set only when the DMA owns the previous Rx descriptor. Access<br>restriction applies. Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - Receive Buffer Unavailable status not detected<br>1b - Receive Buffer Unavailable status detected|
|6<br>RI|Receive Interrupt This bit indicates that the packet reception is complete. When packet reception is<br>complete, Bit 31 of RDES3 is reset in the last descriptor, and the specific packet status information<br>is updated in the descriptor. The reception remains in the Running state. Access restriction applies.<br>Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - Receive Interrupt status not detected<br>1b - Receive Interrupt status detected|
|5-3<br>Reserved_5_3|Reserved.|
|2<br>TBU|Transmit Buffer Unavailable This bit indicates that the application owns the next descriptor in the<br>Transmit list, and the DMA cannot acquire it. Transmission is suspended. The TPS0 field of the<br>DMA_Debug_Status0 register explains the Transmit Process state transitions. To resume processing the<br>Transmit descriptors, the application should do the following: - Change the ownership of the descriptor<br>by setting Bit 31 of TDES3. - Issue a Transmit Poll Demand command. For ring mode, the application<br>should advance the Transmit Descriptor Tail Pointer register of a channel. Access restriction applies.<br>Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - Transmit Buffer Unavailable status not detected<br>1b - Transmit Buffer Unavailable status detected|
|1<br>TPS|Transmit Process Stopped This bit is set when the transmission is stopped. Access restriction applies.<br>Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - Transmit Process Stopped status not detected<br>1b - Transmit Process Stopped status detected|
|0<br>TI|Transmit Interrupt This bit indicates that the packet transmission is complete. When transmission is<br>complete, Bit 31 of TDES3 is reset in the last descriptor, and the specific packet status information is<br>updated in the descriptor. Access restriction applies. Self-set to 1 on internal event. Setting 1 clears.<br>Setting 0 has no effect.<br>0b - Transmit Interrupt status not detected<br>1b - Transmit Interrupt status detected|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4093 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## 75.7.395 (DMA_CH2_Miss_Frame_Cnt) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH2_Miss_Frame_|1264h|
|Cnt||



#### Function 

This register has the number of packet counter that got dropped by the DMA either due to Bus Error or due to programming RPF field in DMA_CH${i}_Rx_Control register. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4094-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_16<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R MFCO  Reserved_14_11  MFC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-16|Reserved.|
|Reserved_31_1<br>6||
|15<br>MFCO|Overflow status of the MFC Counter When this bit is set then the MFC counter does not get incremented<br>further. The bit gets cleared when this register is read. Access restriction applies. Clears on read.<br>Self-set to 1 on internal event.<br>0b - Miss Frame Counter overflow not occurred<br>1b - Miss Frame Counter overflow occurred|
|14-11|Reserved.|
|Reserved_14_1<br>1||
|10-0<br>MFC|Dropped Packet Counters This counter indicates the number of packet counters that are dropped by<br>the DMA either because of bus error or because of programing RPF field in DMA_CH${i}_Rx_Control<br>register. The counter gets cleared when this register is read. Access restriction applies. Clears on read.<br>Self-set to 1 on internal event.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4094 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## 75.7.396 (DMA_CH2_RXP_Accept_Cnt) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH2_RXP_Accept|1268h|
|_Cnt||



#### Function 

The DMA_CH(#i)_RXP_Accept_Cnt registers provides the count of the number of frames accepted by Rx Parser. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4095-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>RXPA<br>R RXPAC<br>COF<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXPAC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31<br>RXPACOF|Rx Parser Accept Counter Overflow Bit When set, this bit indicates that the RXPAC Counter field<br>crossed the maximum limit. Access restriction applies. Clears on read. Self-set to 1 on internal event.<br>0b - Rx Parser Accept Counter overflow not occurred|
||1b - Rx Parser Accept Counter overflow occurred|
|30-0<br>RXPAC|Rx Parser Accept Counter This 31-bit counter is implemented when a Rx Parser Accept a packet due to<br>AF =1. The counter is cleared when the register is read.|



## 75.7.397 (DMA_CH2_RX_ERI_Cnt) 

#### Offset 

|Register|Offset|
|---|---|
|DMA_CH2_RX_ERI_Cnt|126Ch|



#### Function 

The DMA_CH(#i)_RX_ERI_Cnt registers provides the count of the number of times ERI was asserted. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4095 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||Reserve|d_31_12||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||Reserve|d_31_12|||||||EC|NT||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-12|Reserved.|
|Reserved_31_1<br>2||
|11-0<br>ECNT|ERI Counter When ERIC bit of DMA_CH(#i)_RX_Control register is set, this counter increments for burst<br>transfer completed by the Rx DMA from the start of packet transfer. This counter is reset at the start of<br>new packet.|



# 75.8 Using PHY interfaces 

This section is Synopsys Proprietary. Used with permission. 

This module support the following modes: 

- RGMII 100/1000 Mbps inerface 

- RMII 10/100 Mbps interface 

- MII 10/100 Mbps interface 

Phy_intf_sel input signal decides which mode is selected. Samples the Phy_intf_sel signal at reset. See Signal descriptions for more information. MAC_Configuration[PS] and MAC_Configuration[FES] selects the mode's speed. 

The module supports the IEEE802.3-2015 specification for MII, RMII specification version 1.2 from RMII consortium, and RGMII specification version 2.6 from HP/Marvell. 

~~<mark>NOTE</mark>~~ 

RMII reference clock (50 MHz) can be fed to IP from an external source or internally from PLL on SoC. 

The module supports the access of the phy registers through SMA. It is a two wire Station management interface (MIM): 

1. MDC 

2. MDIO 

According to IEEE 802.3 specification, maximum operating frequency of MDC is 2.5 Mhz which system clock derives using a divider. MAC_MDIO_Address[CR] programs to generate different MDC clock frequency. 

SMA supports MDIO clause 45 and clause 22 frame structure per the IEEE802.3 specification. Writing 1 to MAC_MDIO_Address[C45E] enables the clause 45 frame structure. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4096 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

The MII interface reduces the accuracy of the 1588 timestamp if it is overclocked to run at 200 Mbps. This happens because the MAC logic uses the MII interface speed,to adjust or compensate for the timestamps taken at MII, as compared to the time generated in the PTP clock domain as specified in MAC_Configuration[FES]. 

# 75.9 VLAN and double VLAN insertion, deletion, replacement and tagging 

This section and all its sub-sections are Synopsys proprietary. These are used with permission. 

The following sections describe the VLAN and double VLAN features. 

## 75.9.1 Double VLAN processing 

In the double VLAN tagging processing, the module supports the processing of two VLAN tags. The two VLAN tags are: 

1. Inner VLAN tag (C-VLAN) 

2. Outer VLAN tag (S-VLAN) 

If there is only one tag in a packet then it is considered as an outer tag. 

The module uses MAC_VLAN_Incl and MAC_Inner_VLAN_Incl and MAC_VLAN_Tag registers to support the following functions in a double VLAN processing feature. 

- Insertion, replacement, or deletion of up to two VLAN tags in the transmit path. 

- Packet filtering and stripping on the basis of any one of the two VLAN tags in the receive path. Stripping and providing up to two VLAN tags in the receive path as a part of the receive status. 

### 75.9.1.1 Transmit path 

Table 561. Double VLAN processing features in transmit path 

|Feature|Description|
|---|---|
|Support for C-VLAN and<br>S-VLAN tag types|The inner or outer VLAN tag can be of C-VLAN and S-VLAN type.MAC_VLAN_Incl[CSVL]and<br>MAC_Inner_VLAN_Incl[CSVL]specifies the VLAN type.<br>The module supports the processing of any sequence of outer and inner VLAN tags.|
||The module does not support the C-VLAN and S-VLAN sequence.<br>NOTE<br>MAC does not examine whether the packet, which the application provides has a valid sequence<br>of the VLAN tag types or the insertion or replacement operation results in an invalid sequence<br>of VLAN tag type. Therefore, the application must provide a correct sequence of VLAN tag types<br>and program the MAC in such a way that it results in correct sequence of VLAN tag types in the<br>transmitted packet. The application must ensure the following:<br>• The inner tag should not be S-VLAN when outer C-VLAN Tag insertion is enabled.<br>• The outer tag should not be C-VLAN when inner S-VLAN Tag insertion is enabled.<br>• The inner tag~~should not be S-VLAN when C-VLAN replaces the outer tag~~.<br>• The outer tag should not be C-VLAN when S-VLAN replaces the inner tag.|
|VLAN tag deletion|MAC_VLAN_Incl[VLC]orMAC_Inner_VLAN_Incl[VLC]respectively enables the VLAN tag deletion<br>for an outer or inner tag. When you enable the VLAN deletion, MAC deletes the tag present at the<br>corresponding position. When a packet has only one tag, it is considered as the outer tag. If you<br>enable the inner tag deletion and if there is only one tag in the packet, then the MAC does not delete<br>the tag.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4097 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 561. Double VLAN processing features in transmit path (continued) 

|VLAN tag insertion<br>or replacement|MAC_VLAN_Incl[VLC]orMAC_Inner_VLAN_Incl[VLC]respectively enables the VLAN tag insertion<br>or replacement for an outer or inner tag. When you enable the VLAN tag insertion or replacement,<br>theMAC_VLAN_Incl[VLTI]or|
|---|---|
||MAC_Inner_VLAN_Incl[VLTI]determines whether the VLAN tag must be fetched from the register<br>or from the control word.|



### 75.9.1.2 Receive path 

Table 562. Double VLAN processing in receive path 

|Feature|Description|
|---|---|
|Outer or inner VLAN tag-<br>based filtering|Mac can filter packets through the ERIVLT bit on the basis of the outer or inner VLAN tag.|
|C-VLAN or S-VLAN tag-<br>based filtering|Mac can filter packets through the ERSVLM bit on the basis of the C-VLAN or S-VLAN<br>type.|
|Outer and inner VLAN<br>tag stripping|Mac can strip the outer and inner VLAN tags from received frame on the basis of the EVLS<br>and EIVLS bits.|
|16-bit outer and inner VLAN tag<br>and type in Rx status|Mac can provide the 16-bit outer and inner VLAN tag and type in the Rx status on the basis<br>of the EVLRXS and EIVLRXS bits, respectively.|
|Disabling or skipping checking of<br>outer VLAN tag type|Mac can disable or skip checking of an outer VLAN tag type to match C-VLAN or S-VLAN<br>on the basis of the DOVLTC bit.|



### 75.9.1.3 Source address and VLAN insertion, replacement, or deletion 

This module supports the SA, and VLAN insertion, replacement and deletion feature. The SA and VLAN fields are Tx packet-related control information that interfaces provide as part of the control word. IP supports the feature to insert or replace the source address on the basis of the information in the MAC address registers, and it also supports the feature to insert, replace, or delete the VLAN fields (VLAN type and VLAN tag) on the basis of the setting of the MAC_VLAN_Incl[VLTI]. SA insertion or replacement feature is enabled for all the transmit packets or selective packets. Similarly, VLAN insertion, replacement, or deletion feature is enabled for all the Tx packets or selective packets. 

### 75.9.1.4 Programming source address insertion or replacement 

You can use the SA insertion or replacement feature to instruct MAC to perform the following actions for Tx packets: 

- Insert the content of the MAC address registers in the SA field 

- Replace the content of the SA field with the content of the MAC address registers 

When SA insertion is enabled, the application must ensure that the packets sent to MAC do not have the SA field. The MAC does not check whether the SA field is present in the transmit packet and it inserts the content of MAC address registers in the SA field. Similarly, when the SA replacement is enabled, the application must ensure that the SA field is present in the packets sent to the MAC. 

MAC replaces the six bytes following the DA field in the transmit packet with the content of the MAC address registers. 

- Configure MAC_Configuration[SARC] to enable the SA insertion or replacement for all Tx packets. 

- Enable the SA insertion for selective packet by configuring the SA insertion control field (bits [25:23] of TDES3) in the first transmit descriptor of the packet. When you write 1 to bit 25 of TDES3, the SA insertion control field indicates insertion or 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4098 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

replacement by MAC Address1 registers. When bit 25 of TDES3 resets, it indicates insertion or replacement by MAC Address 0 registers. 

If you do not enable the MAC Address1 registers, then the MAC Address0 registers are used for insertion or replacement irrespective of the value of the most-significant bit of the SA insertion control field. 

### 75.9.1.5 Programming VLAN insertion, replacement, or deletion 

You can use the VLAN insertion, replacement, or deletion feature to instruct MAC to perform the following actions for the Tx packets: 

- Delete the VLAN type and VLAN tag fields. 

- Insert or replace the VLAN type and VLAN tag fields. 

Insertion or replacement is done on the basis of the setting of the MAC_VLAN_Incl[VLTI] as described in theTable 563: 

Table 563. VLAN insertion or replacement based on VLTI bit 

|Condition|Description|
|---|---|
|VLTI bit=1|MAC inserts or replaces the following:|
||• VLAN type field (C-VLAN or S-VLAN as indicated by theMAC_VLAN_Incl[CSVL])<br>• VLAN tag field depending on the content of the VT field of transmit context descriptor of the packet|
|VLTI bit resets|MAC inserts or replaces the following:|
||• VLAN type field (C-VLAN or S-VLAN as indicated by theMAC_VLAN_Incl[CSVL])<br>• VLAN tag field with theMAC_VLAN_Incl[VLT]|



When the VLAN replacement or deletion is enabled, MAC checks whether the VLAN type field (0x8100 or 0x88a8) is present after the DA and SA fields in the transmit packet. The replace or delete operation does not occur if the VLAN type field is not detected in two bytes following the DA and SA fields. However, when the VLAN insertion is enabled, MAC does not check the presence of VLAN type field in the transmit packet and just inserts the VLAN type and VLAN tag fields. 

Configuring MAC_VLAN_Incl[VLC] and MAC_VLAN_Incl[VLP] enables the VLAN insertion, replacement, or deletion feature for all Tx packets. 

Configuring the VTIR field of TDES2 normal descriptor enables the VLAN insertion, replacement, or deletion for selective packets. 

In addition, the VLP (VLAN Priority control) field must reset in MAC_VLAN_Incl (for outer VLAN) and MAC_Inner_VLAN_Incl register (in inner VLAN) for MAC to take the control inputs from the host, depending on the configuration. 

# 75.10 Packet Filtering 

This section and all its sub-sections are Synopsys proprietary. Used with permission. 

MAC receiver contains various packet filtering scheme. Figure 2 shows the filtering sequence in their precedence order of received packet. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4099 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4100-02.png)


<!-- Start of picture text -->
Receive packet<br>Ethernet SA<br>or DA filter<br>Layer 2<br>VLAN filter<br>IP SA or<br>Layer 3<br>DA filter<br>TCP, UDP SP,<br>or Layer 4<br>DP filter<br>Discard<br>Deliver to the host<br>packet<br>Fail Pass<br>Fail Pass<br>Fail Pass<br>Fail Pass<br><!-- End of picture text -->

Figure 430. Packet filtering sequence 

If you do not enable any of the layer filters, then that filter is bypassed and the subsequent filter is applied. Discard the packet that fails any of the filters. However, you can forward the discarded packet to the host on the basis of the register control. 

## 75.10.1 Source address or destination address filtering 

The address filtering module of MAC checks the SA and DA fields of each incoming packet. Programming of different types of address filtering is described in the sections that follows. 

### 75.10.1.1 Unicast destination address filtering 

MAC supports up to three MAC addresses for unicast perfect filtering. If perfect filtering is selected (MAC_Packet_Filter[HUC] resets), MAC compares all 48 bits of received unicast address with the programmed MAC address for any match. Default MacAddr0 is always enabled. MAC selects the MacAddr1 to MacAddr2 addresses with an individual enable field. Each byte of MacAddr1 to MacAddr2 can be masked when you compare them with corresponding received DA byte by writing 1 to the corresponding Mask byte control field in the register. This enables group address filtering for the DA. 

In hash filtering mode (when you write 1 to HUC bit), MAC performs imperfect filtering by using a 64-bit hash table for unicast addresses . For hash filtering, MAC uses the upper 6 bits CRC of the received destination address to index the content of the hash table. A value of 00000 selects bit 0 of selected register, and a value of 11111 selects bit 63 of hash table register. If the value of 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4100 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

the corresponding bit (indicated by the 6-bit CRC) is 1, the unicast packet is considered to have passed the hash filter, otherwise, the packet is considered to have failed the hash filter. 

### 75.10.1.2 Multicast destination address filtering 

Enable MAC_Packet_Filter[PM] to pass all the multicast packets or disable to do multicast addresses filtering on the basis of MAC_Packet_Filter[HMC]. Compare the multicast address with the configured MAC destination address registers (1–2), also supports the group address filtering. 

In Hash filtering mode, MAC performs imperfect filtering using a 64-bit hash table. MAC uses the upper 6-bits CRC of received multicast address to index the content of the hash table. A value of 000000 selects bit 0 of selected register and a value of 111111 selects bit 63 of the hash table register. The multicast packet is considered to have passed the hash filter if the value of the corresponding bit is equal to 1. Otherwise, the packet is considered to have failed the hash filter. 

### 75.10.1.3 Hash or perfect address filtering 

Configure MAC_Packet_Filter[HPF] to enable or disable the destination address filtering either by hash filter or perfect filter. Also configure MAC_Packet_Filter[HUC] and MAC_Packet_Filter[HMC] to select the hash filtering or perfect filtering for unicast or multicast packet. 

### 75.10.1.4 Broadcast address filtering 

MAC does not filter any broadcast packets by default. You must write 1 to MAC_Packet_Filter[DBF] to reject the broadcast packets. 

### 75.10.1.5 Unicast source address filtering 

MAC by default compares the source address field with the value configured in the source address registers. Configure bit 30 of MAC address register [1-2] to use it for source address instead of destination address comparison. MAC also supports group filtering with SA. You can filter a group of addresses by masking one or more bytes of the address. MAC drop the packets that fail the SA filter if you write 1 to MAC_Packet_Filter[SAF] field. Otherwise, the result of the SA filter is given as a status bit in the receive status word. When you write 1 to the SAF field, the SA filter and DA filter results ends to decide whether you can forward the packets. This means that the packet is dropped if either filter fails. The packet is forwarded to the application only if the packet passes both filters in-order. 

### 75.10.1.6 Inverse filtering 

For DA and SA filtering, you can invert the filter-match result at the final output by writing 1 to the DAIF and SAIF fields of MAC_Packet_Filter register. The DAIF field is applicable for both the unicast and multicast DA packets. The unicast or multicast destination address filter result is inverted in this mode. Similarly, writing 1 to the SAIF field reverses the result of unicast SA filter. 

Table 564 and Table 565 summarize the DA and SA filtering on the basis of the type of packets received. 

Table 564. Destination address filtering 

|Packet type|PR|HPF|HUC|DAIF|HMC|PM|DBF|DA filter operation|
|---|---|---|---|---|---|---|---|---|
|Broadcast|1|X|X|X|X|X|X|Pass|
||0|X|X|X|X|X|0|Pass|
||0|X|X|X|X|X|1|Fail|
|Unicast|1|X|X|X|X|X|X|All packets pass|
||0|X|0|0|X|X|X|Pass on perfect or group filter match|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4101 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 564. Destination address filtering (continued) 

|0|X|0|1|X|X|X<br>Fail on perfect or group filter match|
|---|---|---|---|---|---|---|
|0|0|1|0|X|X|X<br>Pass on hash filter match|
|0|0|1|1|X|X|X<br>Fail on hash filter match|
|0|1|1|0|X|X|X<br>Pass on hash or perfect or group filter match|
|0|1|1|1|X|X|X<br>Fail on hash or perfect or group filter match|
|Multicast<br>1|X|X|X|X|X|X<br>Pass all packets|
|X|X|X|X|X|1|X<br>Pass all packets|
|0|X|X|0|0|0|X<br>Pass on perfect or group filter match and drop pause<br>packets if PCF = 0x|
|0|0|X|0|1|0|X<br>Pass on hash filter match and drop pause packets if<br>PCF = 0x|
|0|1|X|0|1|0|X<br>Pass on hash or perfect or group filter match and drop<br>pause packets if PCF = 0x|
|0|X|X|1|0|0|X<br>Fail on perfect or group filter match and drop pause<br>packets if PCF = 0x|
|0|0|X|1|1|0|X<br>Fail on hash filter match and drop pause packets if<br>PCF = 0x|
|0|1|X|1|1|0|X<br>Fail on hash or perfect/group filter match and drop<br>pause packets if PCF = 0x|



Table 565. Source address filtering 

|Packet<br>type|PR|SAIF|SAF|SA filter operation|
|---|---|---|---|---|
|Unicast|1|X|X|Pass all packets.|
||0|0|0|Pass status on perfect or group filter match but do not drop packets that fail|
||0|1|0|Fail status on perfect or group filter match but do not drop packet|
||0|0|1|Pass status on perfect or group filter match and drop packets that fail|
||0|1|1|Fail status on perfect or group filter match and drop packets that fail|



~~<mark>NOTE</mark>~~ 

When you write 1 to the MAC_Packet_Filter[RA] field, all packets are forwarded to the system along with the correct result of the address filtering in the Rx Status. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4102 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## 75.10.2 VLAN filtering 

VLAN tag filter can be done either by perfect match or hash table. Depending upon the configuration, MAC can compare either lower 12 bits or all 16 bits of received VLAN tag for perfect match. MAC forward the VLAN tagged packet with match status when it drop all the packets which do not match. 

MAC uses 16-bit VLAN hash table for group address filtering on the basis of the VLAN tag. If MAC enables the hash filtering then the most significant 4-bit of CRC-32 of VLAN tag are used to index the content of the MAC_VLAN_Hash_Table. A value of 1 in the VLAN hash table register, corresponding to the index indicates that the VLAN tag of the packet has matched and the packet should be forwarded. A value of 0 indicates that VLAN-tagged packet should be dropped. 

MAC supports the inverse matching for VLAN packets. In the Inverse matching mode, the packet must be dropped when the VLAN tag of a packet matches the perfect or hash filter. If MAC enables the VLAN perfect and VLAN hash match, then a packet is considered as matched if either the VLAN hash or the VLAN perfect filter matches. When inverse match is set, MAC forwards a packet only when both the perfect and hash filters indicate mismatch. 

Table 566 specifies the different possibilities for VLAN matching and the final VLAN match status. When you write 1 to MAC_Packet_Filter[RA] all packets are received and it indicates the VLAN match status in the VF field of RDES2 normal descriptor (write-back format). When the RA field is not set and when you write 1 to MAC_Packet_Filter[VTFE] the packet drops if the final VLAN match status fails 

When VLAN VID programs to 0 in the VL field of MAC_VLAN_Tag register, consider that all the VLAN-tagged packets are perfectly matched but the status of the VLAN hash match depends on the VTHM and VTIM fields in MAC_VLAN_Tag register. 

Table 566. VLAN match status 

|VID|VLAN perfect filter<br>match result|VTHM bit|VLAN hash filter<br>match result|VTIM bit|Final VLAN match status|
|---|---|---|---|---|---|
|VID = 0|Pass|0|X|X|Pass|
||Pass|1|X|0|Pass|
||Pass|1|Fail|1|Pass|
||Pass|1|Pass|1|Fail|
|VID1= 0|Pass|X|X|0|Pass|
||Fail|0|X|0|Fail|
||Fail|1|Fail|0|Fail|
||Fail|1|Pass|0|Pass|
||Fail|0|X|1|Pass|
||Pass|X|X|1|Fail|
||Fail|1|Pass|1|Fail|
||Fail|1|Fail|1|Pass|



In Table 566, X represents any value. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4103 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## 75.10.3 VLAN filter fail packets queue 

When you enable VLAN filtering, route the VLAN filter fail packets to a programmable queue (VFFQ) when the value of MAC_Packet_Filter[RA] = 1 or MAC_Packet_Filter[VTFE] = 0 and write 1 to MAC_RxQ_Ctrl4[VFFQE] for the queue. 

Route the packets that passes the VLAN filtering to Rx queues on the basis of the VLAN tag priority field by configuring the PSRQ field in the corresponding MAC_RxQ_Ctrl2 and MAC_RxQ_Ctrl3 registers. Discard the packets that fail the VLAN filter if RA=0 or VTFE=1. However, when RA=1 or VTFE=0, forward the VLAN filter fail packets to the application. In such case, when you write 1 to the VLAN filter fail queue enable (VFFQE) field, the VLAN filter fail packets forward to the Rx queue number programmed in the VFFQ field. If the value of VFFQE=0, the VLAN priority mapping determines the Rx queue number per the PSRQ fields. 

Table 567 shows the Rx queue routing table for unicast tagged packets, with DA or SA filter enabled. 

Table 567. Rx queue routing table for unicast tagged packets 

|RA|VFTE|SA or DA filter result|VLAN filter result|VFFQE|Queue routing|
|---|---|---|---|---|---|
|X|X|Pass|Pass|X|PSRQ|
|0|0|Pass|Fail|0|PSRQ|
|0|0|Pass|Fail|1|VFFQ|
|0|X|Fail|X|X|Dropped|
|0|1|Pass|Fail|X|Dropped|
|1|X|Fail|X|0|UFFQ*/PSRQ|
|1|X|Fail|X|1|UFFQ*/VFFQ|
|1|X|Pass|Fail|0|PSRQ|
|1|X|Pass|Fail|1|VFFQ|



X : Don't care condition * : When UFFQE is enabled else PSRQ. 

## 75.10.4 Extended receive VLAN filtering and routing 

When the extended Rx VLAN filtering and routing is enabled then both the perfect filtering and hash filtering can be enabled. The overall VLAN filter result is based on the perfect filter result and hash filter result (if enabled). Filter result is passed to application as part of the status bit. Extended routing will take place only if VLAN filter has passed. Routing is only based on perfect filter result. Each perfect filter has a DMA channel enable and DMA channel number filed which must be programmed for routing. 

See the extended VLAN based DMA selection in Dynamic (per packet) mapping for more information about routing. 

### 75.10.4.1 Comparison mode 

Application has these comparison option for each VLAN tag filter: 

- Programs MAC to compare the inner or outer VLAN tag either with 12 bits or 16 bits programmed VID. 

- Selects whether the VID comparison is for SVLAN or CVLAN type frames, if type check is enabled for a filter. 

### 75.10.4.2 Filtering 

Perfect filtering is done on the basis of the MAC_VLAN_Tag_Filter registers. MAC compares the relevant VLAN tag ID and gives a result for each VLAN tag filter. 

The results for each VLAN tag filter are: 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4104 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

- Pass- If any one of the VLAN tag filters gives a match. 

- Fail- If the frame mismatches all the filters. 

This behavior is applicable only when the inverse filtering is not enabled in MAC_VLAN_Tag_Ctrl. 

If inverse filtering is enabled and the frame mis-matches all the relevant filters then it is considered to have passed the VLAN filter. If the frame matches any one of the relevant filters then it is considered to have failed. The frame is bypassed to the application if none of the enabled filters can perform a comparison or if none of the filters are enabled. 

The overall filter result and the programming on MAC_Packet_Filter[VTFE] and MAC_Packet_Filter[RA] determines if the frame will drop or it is forwarded to the application. If the value of RA = 1 or VTFE = 0, then the frame is always forwarded whether the filter result is a pass or fail, . If the value of RA = 0 and VTFE = 1, only then, if the VLAN tag filter result is a pass the MAC forwards the frame. If the frame is forwarded to the application, then the relevant filter result is indicated through the status bits. 

### 75.10.4.3 Filter status 

The extended receive VLAN filtering and routing feature provides two status fields to show the comparison result of the VLAN tags. 

By default, MAC indicates the VLAN filter status through one bit in the status VF field in RDES2. When you enable the extended RX VLAN filtering and routing, two status fields will show the comparison result of the VLAN tags. The outer VLAN tag filter pass and inner VLAN tag filter pass bits are defined in the following positions. The status indicated through these fields depends on the programming as described below. 

In RDES2: 

- Bit 15 – Outer VLAN tag filter status 

- Bit 14 – Inner VLAN tag filter status 

In ARI status: MAC filter status: 

- Bit 15 – Outer VLAN tag filter status 

- Bit 14 – Inner VLAN tag filter status 

In MRI status: 

- Bit 47 – Outer VLAN tag filter status 

- Bit 46 – Inner VLAN tag filter status 

Outer VLAN tag filter status (OTS) 

- In perfect filtering, without enabling inverse filtering, if you write 1 to this field, it indicates that the frame’s outer VLAN tag has matched one of the VLAN tag filters. 

- If this field resets, it indicates that the frame’s outer VLAN tag has either failed the relevant outer VLAN tag filters or bypassed them. 

- This field resets if none of the filters are enabled for outer VLAN tag comparison. 

- If inverse filtering is enabled and if you write 1 to this field, then the frame’s VLAN tag has passed all the relevant VLAN tag filters. If it is resets, then it has failed at least one filter or bypassed all the filters programmed for outer VLAN tag comparison. 

- This bit is valid for both single and double VLAN tagged frames. 

Inner VLAN tag filter status (ITS) 

- In perfect Filtering, without enabling inverse filtering, if you write 1 to this field, it indicates that the frame’s inner VLAN tag has matched one of the VLAN tag filters. 

- If this field resets, it indicates that the frame’s inner VLAN tag has either failed the relevant inner VLAN tag filters or bypassed them. 

- This field resets if none of the filters are enabled for inner VLAN tag comparison. 

- If Inverse Filtering is enabled and if you write 1 to this field, then the frame’s VLAN tag has passed all the relevant VLAN tag filters. If it resets, then it has failed at least one filter or bypassed all the filters programmed for inner VLAN tag comparison. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4105 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

- This bit is valid for only double VLAN tagged frames, when double VLAN processing is enabled. 

The application must observe the status fields and the program to determine if the frame has passed or failed the VLAN filter. 

Table 568 and Table 569 describes the possible filter combinations and the corresponding filter results and they also explain the scenarios when the double VLAN processing and the hash VLAN filter are enabled in the design. 

Legend for the table OTS and ITS Bit Values with at least 1 perfect filter enabled 

- VTIM: VLAN tag inverse match enable – bit 17 in VLAN_Tag_Ctrl register. 

- HFO: Hash filter enabled for outer VLAN tag comparison - bit 25 and bit 27 in VLAN_Tag_Ctrl register. 

- HFI: Hash filter enabled for inner VLAN tag comparison – bit 25 and bit 27 in VLAN_Tag_Ctrl register. 

- PFO – Perfect filter comparison enabled for outer VLAN tag - Any of the MAC_VLAN_Tag_Filter registers is enabled (write 1 to bit 16) and programmed for outer VLAN tag comparison (write 0 to bit 20). 

- PFI – Perfect filter comparison enabled for Inner VLAN Tag - Any of the MAC_VLAN_Tag_Filter registers is enabled (write 1 to bit 16) and programmed for inner VLAN tag comparison (write 1 to bit 20). 

- OTS – Outer VLAN tag filter status 

- ITS – Inner VLAN tag filter status 

Table 568 shows the possible values of status bits (OTS and ITS) when at least one perfect filter is enabled. 

Table 568. OTS and ITS bit values with at least 1 perfect filter enabled 

|VTIM|HFO|HFI|PFO|PFI|OTS|ITS|
|---|---|---|---|---|---|---|
|0|0|0|0|1|0|1/0|
|0|0|0|1|0|1/0|0|
|0|0|0|1|1|1/0|1/0|
|0|1|0|1|1|1/0|1/0|
|0|1|0|1|0|1/0|0|
|0|1|0|0|1|1/0|1/0|
|0|0|1|1|1|1/0|1/0|
|0|0|1|1|0|1/0|1/0|
|0|0|1|0|1|0|1/0|
|1|0|0|0|1|0|1/0|
|1|0|0|1|0|1/0|0|
|1|0|0|1|1|1/0|1/0|
|1|1|0|1|1|1/0|1/0|
|1|1|0|1|0|1/0|0|
|1|1|0|0|1|1/0|1/0|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4106 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 568. OTS and ITS bit values with at least 1 perfect filter enabled (continued) 

|VTIM|HFO|HFI|PFO|PFI|OTS|ITS|
|---|---|---|---|---|---|---|
|1|0|1|1|1|1/0|1/0|
|1|0|1|1|0|1/0|1/0|
|1|0|1|0|1|0|1/0|



Table 569 shows the possible values of status bits (OTS and ITS) when no perfect filters are enabled except the VLAN hash filter is enabled. 

Table 569. OTS and ITS bit values with only VLAN hash filter enabled 

|VTIM|HFO|HFI|OTS|ITS|
|---|---|---|---|---|
|0|0|0|0|0|
|0|1|0|1/0|0|
|0|0|1|1/0|1/0|
|1|0|0|1/0|0|
|1|1|0|1/0|0|
|1|0|1|1/0|1/0|



With no perfect filters enabled, any VLAN packet is considered to have bypassed the perfect filter. If Hash Filter is enabled for one of the Tags, then the respective Status bit depends on the Filter's result. The Status bits are set to 0 if VLAN Hash Filter is also not enabled. 

If the value of ITS/OTS is shown as 1/0; then it indicates that the final result is dependent on the enabled relevant filter's result. 

Example 1: The second row of OTS and ITS bit values with only VLAN hash filter enabled indicates that at least one Perfect Filter is enabled for Outer VLAN tag comparison and none of the filters are enabled for Inner VLAN tag comparison. Inverse VLAN Filtering is not enabled. The bit OTS is given as 1/0. If the received frame passes atleast one of the enabled Outer VLAN Tag filters then the bit is set to 1. If the frame doesn't pass any of the enabled Outer VLAN Tag filters, then the bit is set to 0. 

Example 2: The last row of table "OTS and ITS bit values with only VLAN hash filter enabled" indicates that the inverse filtering is enabled, hash filter and at least one perfect filter is enabled for Inner VLAN Tag comparison, then if the received frame's Inner VLAN tag mismatches with both the Hash Filter and all the enabled Perfect filters, then the frame will have the ITS bit set to 1 else it is set to 0. OTS will be set to 0 as no comparison is performed. 

### 75.10.4.4 Stripping 

Each VLAN tags has individual control over stripping. The programming options of always strip, never strip, strip on pass and strip on fail are available. Inner or outer VLAN tag stripping is based on the pass or fail results of the individual tag. If all the relevant filters bypasses a tag, stripping is not applicable for the tag. 

- If strip on pass is enabled for the outer VLAN tag, then the stripping occurs only if the outer VLAN tag has passed the relevant filters. The outer VLAN tag filter result field will be 1. 

- If strip on fail is enabled for the outer VLAN tag, then the stripping occurs only if the outer VLAN tag has failed relevant filters. The outer VLAN tag filter result field will reset. 

- If the outer VLAN tag of the received frame is bypassed by the entire filter (no comparison has been made), then the tag is not stripped, though the status bit is 0. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4107 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

- As multiple filters are enabled, it is possible that the received VLAN frame could have matched any one or more of thefilters. The VLAN Tag's value is not always deterministic from the filter status bits. 

If an application strips the VLAN tag on the basis of the filter result, it might lose the VID. You can use it, if stripping is enabled for any of the tags, place the tag in the status. For this the software or application will enable the respective VLAN tag in status bit - 24 or 31 in the MAC VLAN tag control register. 

See section Programming guidelines for extended VLAN filtering and routing on receive for more information. 

## 75.10.5 Layer 3 and layer 4 filtering 

IP supports the layer 3 based packet filtering which is an IP source or destination address filtering in the IPv4 or IPv6 packets, and layer 4 based packet filtering which is a source or destination port number filtering in TCP or UDP. When you enable layer 3 and layer 4 packet filtering then packets are filtered in the following manner. 

- Matched packets: MAC forward the packets that match all enabled fields to the application along with the status. It gives the matched field status only if MAC_Configuration[IPC] = 1 and if one of the following conditions is true: 

   - All enabled layer 3 and layer 4 fields match 

   - At least one enabled field matches and other fields are bypassed or disabled 

When you enable multiple layer 3 and layer 4 filters, any filter match is considered as a match. If more than one filter matches, MAC provides the status of the lowest filter where filter 0 is the lowest filter and filter 3 is the highest filter. 

- Unmatched packets: MAC drop the packets that do not match any enabled fields. You can use the inverse match feature to block or drop a packet with specific TCP or UDP over IP fields and forward all other packets. 

- Non-TCP or UDP IP packets: By default, all the non-TCP or UDP IP packets bypasses the layer 3 and layer 4 filters. You can optionally program MAC to drop all the non-TCP or UDP packets over IP packets. 

- IP has a control register MAC_L3_L4_Control to control the layer L3 and L4 packet filtering along with address registers to program the layer L3 and L4 fields to be matched. 

## 75.10.6 Flexible receive parser 

When you enable this function, all incoming packets are parsed per the programmable instruction stored in memory. It perform these functions: 

- Packet filter (Accept or reject) 

- DMA channel selection 

Flexible receive parser block operates over the first 128 bytes data of receive packet on the basis of 64 bytes of instruction on each packet. Figure 431 shows the functional block diagram of flexible receive parser. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4108 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4109-02.png)


<!-- Start of picture text -->
MAC receive MAC receive packet data<br>(first 128-byte packet data)<br>MTL receive<br>Receive parser Packet drop or accept<br>FIFO<br>(application clock domain)<br>controller<br>DMA channel number<br>Read<br>Memory indirect<br>access control<br>Slave Read/write<br>interface<br>Software parser<br>instruction table<br>(external memory)<br><!-- End of picture text -->

Figure 431. Functional block diagram of flexible recieve parser 

### 75.10.6.1 Instruction table format of the flexible receive parser 

You must build the 96-bit wide instruction before enabling the receive parser feature and program each instruction as an entry in the instruction memory. 

Table 570 shows the format of each entry in the instruction table . 

Table 570. Rx parser instruction entry format 

|Field|Field Name|Description|
|---|---|---|
|31:0|MATCH_DATA|This is a 4-byte data. You can use it to compare with incoming packet data which starts at<br>the frame offset as defined in [79:72] of the entry. The comparison is done only on those bits<br>whose corresponding mask bits are 1 (MATCH_EN bits of [63:32]). See the notes (below this<br>table) on the byte order relative to Ethernet arrival data and endianness which the QoS IP<br>supports on the slave interface. The programming of this instruction table must adhere to<br>the same.|
|62:32|MATCH_EN|When the MATCH_EN = 1, you can use the corresponding packet data bit for comparing.<br>Otherwise, corresponding data bit is don’t care.|
|64|AF|Accept frame|
|65|RF|Reject frame|
|66|IM|Inverse match|
|67|NC|Next instruction control|
|71:68|Reserved|-|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4109 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 570. Rx parser instruction entry format (continued) 

|Field|Field Name|Description|
|---|---|---|
|79:72|Frame offset|[77:72] indicates the frame offset in terms of 4 bytes. (Here [79:78] always 0) Conpare the<br>frame offset in the packet data for Match.This is in terms of 4 bytes. The value of actual frame<br>offset in bytes are 0 01 42 8… ..63 252<br>The max value programmed in this instruction table is 128 B. The 'Actual frame offset' must<br>not cross this limit.|
|87:80|OK index|If (NIC==0) the memory index you can use next when ENTRY_MATCH==1 and neither AF<br>or RF = 1. If (NIC==1) the memory index you can use next when ENTRY_MATCH==0|
|95:88|DMA Ch No|Indicates the DMA channel number (1-bit for each). You can use this when ENTRY_MATCH<br>==1 and AF = 1 (Accept frame). The following bits give the encoding: bit[0]- DMA channel<br>number o, bit[1]- DMA channel number , 1bit[2]- DMA channel number 2… bit[7]- DMA<br>channel number 7.<br>You can encode the DMA channel number using bit wise as QoS IP support<br>multicasting or broadcast across DMA channels. See section 3.3.12 for<br>more information and proper usage.<br>~~NOTE~~|
|128:96|Reserved|0 (This field is only for software view and reserved for future enhancements. The memory<br>width remains as 96-bits).|



The parser begins parsing from the 0th entry, for each received packet. The subsequent parsing entry location (next entry or OK_INDEX[]) depends on the current entry parser result. Flexible receive parser flow chart shows the detailed flow. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4110 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4111-02.png)


<!-- Start of picture text -->
Start<br>Entry address = 0<br>Number of parsed entries = 0<br>Entry address >= Yes Packet routed to Rx<br>(NVE[7:0]+1) DMA CH0 and generate<br>parser interrupt<br>Entry address = (NIC==0) ?<br>Entry address + 1:<br>OK_INDEX<br>Number of parsed Yes<br>Number of parsed entries = entries >= (NPE[7:0]+1)<br>Number of parsed entries + 1<br>Read the memory and get<br>the corresponding packet field<br>Actual frame offset ><br>EOF_OFFSET<br>No<br>No Pattern match (IM=0) or<br>Invert match (IM=1)<br>Yes<br>Route the frame into<br>AF==1 Yes DMA channel as<br>indicated in<br>DMA_CH_NO[2:0]<br>No<br>No RF==1 Yes generate an interruptReject frame and<br>No<br>Entry address = if(NIC==0) ? OK_INDEX[7:0] : Entry address + 1<br>Num of parsed entries = Num of parsed entries + 1<br>MAC drop<br>End<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4111-03.png)


<!-- Start of picture text -->
Figure 432. Flexible recieve parser flow chart<br><!-- End of picture text -->

The EOF_OFFSET shown in the figure is the least among the following: 

- Actual packet size 

- 128 Byte when frame pre-emption feature is not enabled or configured 

- 128 Byte when frame pre-emption feature is enabled and packet is pre-emptible 

- 64 Byte when frame pre-emption feature is enabled and packet is express packet 

### 75.10.6.2 Number of valid entries (NVE) 

NVE indicates the number of valid entries in the instruction table. The default value is 64. You can change this value by writing into MTL_RXP_Control_Status[NVE]. 

When parsing, an error is flagged in MTL_RXP_Interrupt_Control_Status[NVEOVIS], if the entry address is greater than MTL_RXP_Control_Status[NVE] + 1. IP generates an interrupt status (MTL_Interrupt_Status[MTLPIS]). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4111 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

### 75.10.6.3 Number of parsable entries (NPE) 

NPE indicates the number of entries that you can parse on an incoming packet. The default value is 64. Write into MTL_RXP_Control_Status[NPE] to change this value. 

When parsing, an error is flagged in MTL_RXP_Interrupt_Control_Status[NPEOVIS], if the number of parsed of parsed entries is more than MTL_RXP_Control_Status[NPE] + 1. IP generates an interrupt status (MTL_Interrupt_Status[MTLPIS]). 

NVE[] indicates the number of valid entries in the receive parser memory which you have built and NPE[] indicates the worstcase parsable entries considering the various possible paths that the parser can take. (NVE[] >= NPE[]). 

### 75.10.6.4 Frame offset 

It indicates the frame offset, in terms of 4 bytes which you use when comparing against the current table entry. 

In an entry, an error is flagged in MTL_RXP_Interrupt_Control_Status[FOOVIS] in any of the following cases: 

When frame offset is more than: 

- Packet size 

- 128B if pre-emption is disabled 

- 128B if pre-emption is enabled and packet is pre-empitble 

- 64B if pre-emption is enabled and packet is an express packet 

IP generates an interrupt status (<xref href="DWC_ether_qos.dita#MTL_Interrupt_Status/MTL_Interrupt_Status.MTLPIS" >MTL_Interrupt_Status[MTLPIS]</xref>). 

~~<mark>NOTE</mark>~~ 

If the frame ends after the (frame_offset *4) bytes but before ((frame_offset *4)+4) bytes, the receive parser declares a frame offset error if you enable comparison (via MASK bits) for the non-received bytes; from (frame_offset *4) to ((frame_offset *4)+4). 

### 75.10.6.5 Frame reject 

You can drop the frame in cases, where an entry matches (considering the inverse match, IM bit in the instruction table) and frame accept bit is not 1, and frame reject bit (RF) = 1. 

When a frame drops because RF = 1, IP generates an interrupt status (MTL_Interrupt_Status[MTLPIS]). 

### 75.10.6.6 Out of order processing 

The Rx parser flow can be out of order. The decision tree is not based on the order in which packet arrives. This implies that the next entry and next frame offset (OK_INDEX[] and FRAME_OFFSET[]) can be less than the current entry address and current frame offset. 

### 75.10.6.7 DMA channel selection 

When you enables the receive parser (MTL_Operation_Mode[FRPE] = 1) it overrides the MAC DMA selection criteria. 

When you disables the receive parser (MTL_Operation_Mode[FRPE] = 0) the MAC/MTL determines the DMA channel number. 

### 75.10.6.8 Receive queue selection 

The existing MAC functionality determines the receive queue, irrespective of whether the receive parser is enabled or disabled. This is because the receive parser is mainly designed to select the DMA channel and the MAC decides the receive queuing to enable the proper functioning of the pause or PFC feature. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4112 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

~~<mark>NOTE</mark>~~ 

When there are multiple queues and multiple DMA Channels are enabled, a particular DMA channel might receive out of order packets because queue selection is based on MAC criteria (VLAN Priority and other criteria) and Rx DMA channel selection is based on receive parser. 

### 75.10.6.9 MAC packet filtering/drop/error handling 

Packet filtering is done on the basis of the received packet fields. You must disable the packet filtering features inside the MAC when the receive parser is enabled. Follow these steps to disable the packet filtering features inside the MAC : 

1. Write 1 to the Promiscuous mode (MAC_Packet_Filter[PR]). 

2. Write 1 to all other fields in MAC_Packet_Filter to its default values. 

When MAC decides to drop the packet due to the receive MAC dependent error such as: 

- GMII error 

- Receive watchdog error 

- CRC error 

- Giant frame error 

the packet drops irrespective of the receive parser decision. 

### 75.10.6.10 Pad strip or CRC strip handling 

Software controls the pad strip and CRC strip and it is applicable to all the received packets. Also,software must build the receive parser instructions accordingly, when you enable these features. 

~~<mark>NOTE</mark>~~ 

Enable pad and CRC stripping in real use case. 

### 75.10.6.11 VLAN strip handling 

MAC supports stripping the outer VLAN as well as inner VLAN. When you program MAC to strip the VLAN, the receive parser considers those VLAN tags to be part of the incoming packet. 

### 75.10.6.12 Multicast and broadcast support 

IP supports multicast and broadcast packet and the packet route to the highest queue number. 

When you enables the receive parser, the DMA channel numbers (DMA CH NO, Bits [95:88]) in the instruction table, decide the packet routing. 

When you disables the receive parser, DCS (DMA Channel Select) field of the MAC_AddressX_High register determines the packet routing. See the Broadcast/multicast packet duplication. 

~~<mark>NOTE</mark>~~ 

You can select multiple DMA channels for the packet routing because the DCS/DMA CH NO field is per the DMA channel control. 

### 75.10.6.13 Pre-emption support 

IP supports the frame pre-emption feature when the flexible receive parser feature is enabled. It has the following limitations: 

- Number of bytes would be 64, so that the receive parser can operate on an express traffic 

- Number of bytes would be 128, so that receive parser can operate on a pre-emptible traffic. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4113 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

### 75.10.6.14 Software access to the flexible receive parser memory 

Software can read and write into the receive parser memory. It uses the following registers via indirect addressing. 

- MTL_RXP_Indirect_Acc_Control_Status 

- MTL_RXP_Indirect_Acc_Data 

For more details, see GMAC register descriptions. 

### 75.10.6.15 Statistical counters 

IP supports these statistics counters for flexible receive parser. 

1. MTL_RXP_Drop_Cnt 

2. DMA_RXP_Error_Cnt 

DMA_CH(#i)_Rxp_Accept_cnt (i=0; i<2) 

For more details, see GMAC register descriptions. 

### 75.10.6.16 Changing the instruction table by software 

Software can update the instruction table in the memory in the following ways: 

- Disables the MAC receiver and receive parser by writing 0 to MAC_Configuration[RE] and MTL_Operation_Mode[FRPE]. It waits for receive parser to become inactive (RXPIA, MTL_RXP_Control_Status register bit[31]). 

- (Optional) Programs in the entry address 0 to unconditionally (all MATCH_EN bit 0) skip to OK_INDEX[] (to certain location in the memory), where you can program it to reject or accept all the packets. 

### 75.10.6.17 Receive cut-through functionality 

In the Cut-Through mode, the receive controller transfer the received packets to DMA just after it receives the cut-through threshold amount of packet data (RTC field in the MTL_RxQx_Operation_Mode register ). 

However due to Rx parser's result worst case arrival time can be more than the programmed cut-through threshold. So, the receive controller delays the packet transfer to DMA accordingly, and the cut-through functionality is re-defined as follows: 

The receive controller transfers packet to DMA after at least RTC number of bytes have been received and receive parser results are available. 

### 75.10.6.18 Receive packet drop indication 

In most cases, the packet drops internally in the receive queue. However, back-to-back packets can arrive for the same queue and the first packet's receive parser result is not available when the second packet arrives. In such cases, the packet cannot be flushed internally and forwarded to DMA or the application interface and indicates the status accordingly. See RDES2, bit 16(RXPD) in Receive normal descriptor (write-back format) for more information. 

### 75.10.6.19 Runt packet handling 

The receive parser can performs the operation with 64B minimum size packet. If the runt packet is received (MAC must indicate it), the receive parser assumes that it is dropped in the MAC, this is because, the back-to-back runt packets (< 64B) cannot be handled in the receive parser. 

### 75.10.6.20 Uncorrectable ECC error handling 

The packet does not drops when the parser detects an uncorrectable ECC error while parsing the parser memory. The packet is sent to the application with an error indication. The RXPI (RX parser incomplete) sets in the packet status along with error summary (ES) bit. 

See the Receive normal descriptor (write-back format) for more information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4114 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.11 IEEE 1588 timestamp support 

This section and all its sub-sections are Synopsys proprietary. Used with permission. 

IP supports the IEEE 1588 precision time protocol (PTP). It is also able to do precise time stamping and captures incoming and outgoing frame because of the PTP protocol implementation in the IP. It supports all the clock types defined in IEEE 1588-2008. The typical frequency of PTP timestamp clock is 125 MHz. 

IP supports these features: 

- Provides an option to take snapshot of all packets or only PTP type packets 

- Provides an option to take snapshot of only event messages 

- Identifies the PTP message type, version, and PTP payload in packets sent directly over Ethernet and sends the status 

- Provides an option to measure sub-second time in digital or binary format 

## 75.11.1 Delay request-response mechanism 

The system or network is classified into the master and slave nodes for distributing the timing and clock information. Figure 433 shows the process that PTP uses for synchronizing a slave node to a master node by exchanging PTP messages. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4115-12.png)


<!-- Start of picture text -->
Master clock time Slave clock time<br>t 1 Sync message Data at<br>slave clock<br>t 2 m t 2 t 2<br>Follow_Up message<br>containing value of  t 1<br>t 1,  t 2<br>t 3 m t 3 t 1,  t 2,  t 3<br>Delay_Req message<br>t 4<br>Delay_Resp message<br>containing value of  t 4<br>t 1,  t 2,  t 3,  t 4<br>time<br><!-- End of picture text -->

Figure 433. Networked time synchronization 

As shown in the figure, PTP uses this process: 

1. The master broadcast the PTP sync messages to all its nodes. The sync message contains the reference time information of the master. This message leaves the system of the master at t1. You must capture this time for Ethernet ports at GMII or MII. 

2. The slave receives the sync message and it also captures the exact time, t2, using its timing reference. 

3. The master sends a Follow_Up message to the slave, which contains t1 information for later use. 

4. The slave sends a Delay_Req message to the master and note the exact time, t3, at which this packet leaves the GMII or MII interface. 

5. The master receives the message, capturing the exact time t4, at which the message enters its system. 

6. The master sends the t4 information to the slave in the Delay_Resp message. 

7. The slave use the four values of t1, t2, t3, and t4 to synchronize its local timing reference to the master's timing reference. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4115 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Most of the PTP implementation is done in the software above the Ethernet layer. However, the hardware captures the exact time when specific PTP packets enter into or leave the Ethernet port at the MII interface. This timing information must be captured and returned to the software for proper implementation of PTP with high accuracy. 

## 75.11.2 Peer-to-peer PTP transparent clock (P2P TC) message support 

The IEEE 1588-2008 supports the peer-to-peer PTP (Pdelay) message in addition to the sync, delay request, follow-up, and delay response messages. Figure 434 shows the method to calculate the propagation delay in clocks supporting the peer-to-peer path correction. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4116-05.png)


<!-- Start of picture text -->
P2P TC A P2P TC B<br>delay delay<br>requester responder<br>time time<br>Timestamps<br>that the delay<br>requester knows<br>t 1<br>Pdelay_Req t 1<br>tAB<br>t 2<br>t 3<br>Pdelay_Resp<br>tBA<br>t 4<br>t 1,  t 4<br>t 1,  t 2,  t 3,  t 4<br>Pdelay_Resp_Follow_Up:<br>t 2,  t 3<br><!-- End of picture text -->

Figure 434. Propagation delay calculation in clocks supporting peer-to-peer path correction 

As shown in the above figure, the propagation delay is calculated in the following way: 

1. Port 1 issues a Pdelay_Req message and generates a timestamp (t1) for the Pdelay_Req message. 

2. Port 2 receives a Pdelay_Req message and generates a timestamp (t2) for this message. 

3. Port 2 returns a Pdelay_Resp message and generates a timestamp (t3) for this message. Port 2 returns the Pdelay_Resp message as quickly as possible after the receipt of the Pdelay_Req message, to minimize the errors because of any frequency offset between the two ports. Port 2 returns any one of the following: 

   - Difference between the timestamps t2 and t3 in the Pdelay_Resp message 

   - Difference between the timestamps t2 and t3 in the Pdelay_Resp_Follow_Up message 

   - Timestamps t2 and t3 in the Pdelay_Resp and Pdelay_Resp_Follow_Up messages, respectively 

4. Port 1 generates a timestamp (t4) after receiving the Pdelay_Resp message. 

5. Port 1 uses all the four timestamps t1, t2, t3, and t4 to compute the mean link delay. 

## 75.11.3 Timestamp correction 

According to the IEEE 1588 specification, you must capture a timestamp when the PTP message timestamp point (leading edge of the first bit of the octet immediately following the start frame delimiter octet) crosses the boundary between the node and the network. As MAC takes the timestamp at an internal point far from the actual boundary of the node and network, you must correct or update the captured timestamp for the ingress or egress path latency (including the delay in the PHY layers). Further 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4116 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

correction is done for the inaccuracies or errors introduced because the clock (MII Tx, Rx clock) is different at the capture point as compared to the PTP clock (clk_ptp_ref_i) that generates the time. The resultant CDC (Clock domain crossing) circuits add an error depending on the clock period of the MII and PTP clocks. 

### 75.11.3.1 Ingress correction 

The timestamp captured at the internal snapshot point In the receive side is delayed (later in time) as compared to the time at which the packet's SFD bit is received at the port's boundary. Therefore, the ingress latency and the errors in CDC sampling reduces the captured timestamp. You must determine or calculate the correction value and write into the MAC_Timestamp_Ingress_Corr_* registers. 

The correction value consists of these three components: 

1. External latency in the PHY layer between boundary point and the input of the core. 

If the PHY is compliant with the IEEE 802.3 Clause 45 MMD registers, it has a register which indicates the maximum and minimum ingress latency. You can read these registers and determines the average ingress latency in the PHY. Alternatively (if the PHY does not support these registers), you must determine the ingress latency from its datasheet or timing characteristics. 

2. Internal latency from the core's input to the internal capture point. 

You can read the internal ingress latency from MAC_Timestamp_Ingress_Latency. This is a read-only register and provides the latency in scaled nanoseconds format as defined in IEEE 1588 Clause 5.3.2. The latency differs on the basis of the active PHY interface (MII, RMII, so on) and the operating speed. Therefore, you must read this register after any speed change in MAC, to determine the current internal latency. 

3. CDC synchronization 

The CDC synchronization error is almost equal to twice the clock-period of the PTP clock (clk_pt-p_ref_i). 

You must add the values that these three components determine and must write into the TSIC and TSICSNS fields of the MAC_Timestamp_Ingress_Corr_* registers. 

~~<mark>NOTE</mark>~~ The value written into the register must be negative (two's complement as explained below), because it is subtracted from the captured timestamp. The MAC receiver adds the value in this register to the captured timestamp and then gives the resultant value as the timestamp of the received packet. 

When MAC_Timestamp_Control[TSCTRLSSR] is 1, it indicates that the nanoseconds field of the captured timestamp is in decimal format with a granularity of 1ns. So the Bit31 of TSIC must be 1 (for negative value) and bits[30:0] must write with "10^9 - total ingress_correction_value[nanosecond part]" represented in binary. For example, if the required correction value is -5 ns, then the value is 0xBB9A_C9FB. 

When MAC_Timestamp_Control[TSCTRLSSR] becomes 0, it indicates that the nanoseconds field of the captured timestamp is in binary format with a granularity of ~0.466ns. Therefore, bits[30:0] must write with "2^31 - total ingress_correction_value" represented in binary with bit[31] = 1. 

### 75.11.3.2 Egress correction 

The timestamp captured at the internal snapshot point in the transmit side is earlier (advanced in time) as compared to the time at which the packet's SFD bit is output at the port's boundary. Therefore, the egress latency and the errors in CDC sampling must compensate the captured timestamp. You must determine or calculate this correction value and write into the MAC_Timestamp_Egress_Corr_* registers. 

The correction value consists of these three components: 

1. External latency in the PHY layer between the core output and the port and the network boundary 

If the PHY is compliant with the IEEE 802.3 Clause 45 MMD registers, it has a register which indicates the maximum and minimum egress latency. You can read these registers and determine the average egress latency in the PHY. Alternatively (if the PHY does not support these registers), you must dertermine the egress latency from its datasheet or timing characteristics. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4117 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

2. Internal latency from the internal capture point and the core output of the c 

You can read this internal egress latency from MAC_Timestamp_Egress_Latency. This is a read-only register and gives the latency in scaled nanoseconds format as defined in IEEE 1588 Clause 5.3.2. The latency differs on the basis of the active PHY interface (MII, RMII, so on) and the operating speed. Therefore, you must read this register after any speed change in MAC to determine the current internal latency. 

3. CDC synchronization error 

The CDC synchronization error value for one-step timestamping = (1 * period of clk_ptp_ref_i + 4 * period of clk_tx_i). Otherwise (Two-step timestamping mode), the value = -(2 * period of clk_ptp_ref_i). 

### 75.11.3.3 Frequency range of reference timing clock 

The timestamp information is transferred across asynchronous clock domains that is from the MAC clock domain to the application/system clock domain. Therefore, a minimum delay is required between the two consecutive timestamp captures. This delay is 4 clock cycles of MII and 3 clock cycles of PTP clocks. If the delay between the two captured timestamp is less than this delay, MAC does not take a timestamp snapshot for the second packet. 

### 75.11.3.4 PTP processing and control 

Table 571 shows the common message header for the PTP messages. This format is defined in the IEEE 1588-2008. 

Table 571. Message format defined in IEEE 1588-2008 

|Bits|||||||
|---|---|---|---|---|---|---|
|7<br>6<br>5|4|3<br>2|1|0|Octet|Offset|
|transportSpecific||messageType|||1|0|
|Reserved||versionPTP|||1|1|
|messageLength|||||2|2|
|domainNumber|||||1|4|
|Reserved|||||1|5|
|flagField|||||2|6|
|correctionField|||||8|8|
|Reserved|||||4|16|
|sourcePortIdentity|||||10|20|
|sequenceId|||||2|30|
|controlField (*)|||||1|32|
|logMessageInterval|||||1|33|



(*) – control Field is used in version 1. In version 2 message type field is used for detecting different message types. 

There are some fields in the Ethernet payload that detects the PTP packet type and controls the snapshot to be taken. These fields are specified in Table 572 for PTP packets over Ethernet. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4118 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Following table provides the information about the fields that match to control the snapshots for the PTP packets sent over Ethernet for IEEE 1588 version 1 and version 2. The octet positions are offset by 4 for the tagged packets. This is based on the IEEE 1588-2008, Annex D, and the message format. 

Table 572. Ethernet PTP packet fields required for control And status 

|Field matched|Octet position|Matched value|Description|
|---|---|---|---|
|MAC destination<br>multicast address<sup>1</sup>|0–5|01-1B-19-00-00-00<br>01-80-C2-00-00-0E|All PTP messages can use any of the<br>following multicast addresses<sup>2</sup>:<br>• 01-1B-19-00-00-00<br>• 01-80-C2-00-00-0E<sup>3</sup>|
|MAC packet type|12, 13|0x88F7|PTP Ethernet packet|
|PTP control field<br>(IEEE 1588 version 1)|46|0x00, 0x01, 0x02, 0x03,<br>or 0x04|• 0x00: SYNC<br>• 0x01: Delay_Req<br>• 0x02: Follow_Up<br>• 0x03: Delay_Resp<br>• 0x04: Management|
|PTP message type field<br>(IEEE 1588 version 2)|14 (nibble)|0x0, 0x1, 0x2, 0x3, 0x8, 0x9,<br>0xB, 0xC, or 0xD|• 0x0: SYNC<br>• 0x1: Delay_Req<br>• 0x2: Pdelay_Req<br>• 0x3: Pdelay_Resp<br>• 0x8: Follow_Up<br>• 0x9: Delay_Resp<br>• 0xA: Pdelay_Resp_Follow_Up<br>• 0xB: Announce<br>• 0xC: Signaling<br>• 0xD: Management|
|PTP version|15 (nibble)|0x1 or 0x2|• 0x1: Supports PTP version 1<br>• 0x2: Supports PTP version 2|



1. The unicast address match of destination addresses (DA), which is programmed in MAC address 0 to 31, is used if MAC_Timestamp_Control[TSENMACADDR] = 1. 

2. IEEE 1588-2008, Annex F 

3. MAC does not consider the PTP version 1 messages with peer delay multicast address (01-80-C2-00-00-0E) as valid PTP messages. 

## 75.11.4 Transmit path functions 

MAC captures a timestamp when the start packet delimiter (SFD) of a packet is sent on the MII interface. You can control the packets, for which the timestamps are captured on a per-packet basis and mark each transmit packet to indicate whether to capture a timestamp for it. MAC does not process the transmitted packets to identify the PTP packets. You can use the control bits in the transmit descriptor to specify the packets. MAC returns the timestamp to the software inside the corresponding transmit descriptor and therefore connects the timestamp automatically to the specific PTP packet. You must write the 64-bit timestamp information to TDES0 and TDES1 fields. The TDES0 field holds the 32 least significant bits of the timestamp. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4119 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## 75.11.5 Receive path functions 

You can program MAC to capture the timestamp of all packets received on the MII interface or to process the packets to identify the valid PTP messages. 

You can use these options of MAC_Timestamp_Control to control the snapshot of the time sent to the application: 

- Enable snapshot for all packets 

- Enable snapshot for IEEE 1588 version 1 or version 2 timestamp 

- Enable snapshot for PTP packets transmitted directly over Ethernet 

- Enable timestamp snapshot for the received packet for IPv4 or IPv6 

- Enable timestamp snapshot only for EVENT messages (SYNC, DELAY_REQ, PDELAY_REQ, or PDELAY_RESP) 

- Enable the node to be a master or slave and select the snapshot type 

Table 573. Timestamp snapshot dependency on register bits 

|SNAPTYPSEL|TSMSTRENA|TSEVNTENA|PTP messages|
|---|---|---|---|
|00|x|0|SYNC, Follow_Up, Delay_Req, Delay_Resp|
|00|0|1|SYNC|
|00|1|1|Delay_Req|
|01|x|0|SYNC, Follow_Up, Delay_Req,<br>Delay_Resp, Pdelay_Req,<br>Pdelay_Resp, Pdelay_Resp_Follow_Up|
|01|0|1|SYNC, Pdelay_Req, Pdelay_Resp|
|01|1|1|Delay_Req, Pdelay_Req, Pdelay_Resp|
|10|x|x|SYNC, Delay_Req|
|11|x|x|Pdelay_Req, Pdelay_Resp|



DMA returns the timestamp to the software inside the corresponding receive descriptor. The extended status, contains the timestamp message status and the IPC status. You must write the extended status in the normal descriptor RDES1 and the snapshot of the timestamp in RDES0 and RDES1 fields of context descriptor. The RDES0 field holds the 32 least significant bits of the timestamp. 

See the System time correction for programming guidelines for IEEE 1588 timestamping (System time correction). 

## 75.11.6 IEEE 1588 system time source 

IP supports both the external and internal time source for reference timestamping. 

- External time source uses the 64-bit external time reference and clock as an input in IP. The clock input synchronizes the external timing reference into the MAC clock domain. Upper 32-bit indicates the time in seconds and the lower 32-bit indicates the time in nanoseconds. 

- Internal time source uses the only clock input to generate timing reference internally for snapshot and capture timestamps. Internal time reference has two fields. 

   - UInteger48 seconds field: The seconds field is the integer portion of the timestamp in seconds units. It is 48-bit wide. 

For example, 2.000000001 seconds are represented as seconds field = 0x0000_0000_0002. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4120 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

- UInteger32 nanoseconds field The nanoseconds field is the fractional portion of the timestamp in nanoseconds units. 

For example, 2.000000001 seconds are represented as nanoseconds field = 0x0000_0001. The nanoseconds field supports the following two modes: 

- ◦Digital rollover mode: In this mode, the maximum value in the nanoseconds field is 0x3B9A_C9FF, that is, (10e9-1) nanoseconds. 

- ◦Binary rollover mode: In this mode, the nanoseconds field rolls over and increments the seconds field after 0x7FFF_FFFF value . Accuracy is ~0.466 ns per bit. 

There is a system time register module, it is used when you use an internal time reference. The 80-bit time is maintained in this module and updated using the input reference clock (clk_ptp_ref_i). This time is the source for taking snapshots (timestamps) of Ethernet packets which is transmitted or received at the MII interface. 

Initialize or correct the system time counter using the coarse correction method. In this method, write the initial value or the offset value to the timestamp update register. For initialization, write the system time counter with the value in the timestamp update register. For system time correction, the offset value is added to or subtracted from the system time. 

In the fine correction method, correct the frequency offset and/or frequency drift of a slave clock (clk_ptp_ref_i) with respect to the master clock (as defined in IEEE 1588-2002) over a period of time instead of in one clock, as in coarse correction. This maintains linear time and does not introduce drastic changes (or a large jitter) in the reference time between the PTP sync message intervals. 

See Initialization guidelines for system time generation for programming guidelines for IEEE 1588 timestamping (For internal timestamp source configuration). 

## 75.11.7 IEEE 1588 higher word register 

You can invoke the higher word register if system time source is internal. MAC timestamp is 64-bit wide. The values of the upper 16-bits of the seconds field are read from the CSR register. 

## 75.11.8 Flexible pulse-per-second output 

IP supports the flexibility of programming the start or stop time, generates pulse width and interval on pulse-per-second output. It also support four such output signals. By default, IP is in fixed pulse-per-second output mode with interval of 1 second. 

Initially you must program the start time in target time registers "MAC_PPSx_Target_Time_Seconds and MAC_PPSx_Target_Time_Nanoseconds" for all desired or enabled pps output. If you re-programs start or stop time then you must do it after the synchronization of earlier programmed value. Bit 31 of MAC_PPS#_Target_Time_Nanoseconds register indicates that the synchronization is complete. If the application programs a start or stop time that has already elapsed, MAC sets an error status bit which indicates the programming error. If enabled, MAC also sets the target time reached interrupt event. The application can cancel the start or stop request only if the corresponding start or stop time has not elapsed. If the time has elapsed, the cancel command has no effect. 

Program the PPS width and interval in terms of granularity of system time, that is, the number of units of sub-second increment value. 

See Programming guidelines for flexible pulse-per-second output for more information. 

## 75.11.9 Media clock generation and recovery 

Media clock recovery and generation requires a dedicated hardware and software to complete the operation. IP generates a reference clock with the help of a dedicated hardware which multiplies to get the desired media clock. Software extracts the presentation time from the incoming PTP 1722 frames and program these values into CSR registers so that IP can read them for media clock recovery. 

Figure 435 shows that the timestamp array and the DMA module are external to IP. IP supports a 32-bit presentation time counter in nanoseconds that completes at the full 32-bit value to match with 1722 presentation time format and an handshake mechanism with an external application (such as DMA) to program the presentation time into CSR register. 

Figure 435. Media clock generation and recovery block diagram 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4121 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4122-02.png)


<!-- Start of picture text -->
Timestamp<br>array<br>(in system RAM<br>external to Ethernet IP)<br>Read from or<br>write to RAM DMA external<br>Timestamp to Ethernet IP<br>Presentation<br>Request or acknowledge one pair per<br>timestamp<br>capture and compare unit<br>PTP counter Recovered<br>(32 bit nanosecond value) Compare value clock<br>Generation<br>MAC Comparator modules<br>trigger<br>(4 in current implementation)<br>Part of IP<br><!-- End of picture text -->

### 75.11.9.1 Presentation time counter 

Presentation time counter provides an another perspective of the PTP system time (1588 timer). For a given PTP system time (PTP[63:32] represents time in seconds Comparator modules and PTP[31:0] represents time in nanoseconds), there exists a corresponding presentation time (32-bit value in nanosecond). The presentation time computed is referred to as current presentation time (CPT). 

CPT derives from 64-bit PTP system time. PTPNS[63:0] = (PTP[63:32] * 32'd1,000,000,000) + PTP[31:0] where, PTPNS is the PTP system time converted into a 64-bit nanosecond value. 

Current presentation time[31:0] = PTPNS[31:0] 

Media clock recovery is possible when the system time is internally generated in IP and compute the CPT in the same way as the internal PTP system time generation. The increment cycle of CPT and system time are same because the values of both the timers are in nanoseconds and they are synchronous. The timer updates at the same instance, but the updated value could be different. You must compute a separate 32-bit update value in nanoseconds for the CPT update. CPT sampled at different edges of a triggering input generates media clock timestamps that are inserted in 1722 based AVBTP packets, to recover the clock at the destination. 

### 75.11.9.2 Comparator modules 

Figure 435 shows that the module supports four comparator modules to handle multiple media clocks that it may require. When MAC_Timestamp_Control[PTGE] is 1, it indicates that the comparator modules handshake with the application to program the timestamps into the MAC_PPS(#i)_Target_Time_Seconds register. 

Write 1 to presentation time control fields of the particular instance for recovery mode. 

The timestamps received from the application are referred as target presentation time (TPT). 

When MCGREN#i field of MAC_PPS_Control is 1, it indicates that the IP operates in MCGR mode. The comparator module sends upto two requests to the application for TPT write, when MAC_Timestamp_Control[PTGE] and the presentation time control bits of the particular instance are 1 for MCGR mode. Subsequent requests are generated each time a presentation time match occurs. CPT transitions from a value less than TPT, to a value greater than or equal to CPT. The first request asserts when a specific comparator instance sets to MCGR mode with a non-zero presentation time control and an additional request is made when the comparator receives the first data. This allows the application to write the next TPT value when IP processes the previous TPT value for a match. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4122 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

TPT read from the MAC_PPS(#i)_Target_Time_Second is considered as a future time. A toggle or pulse is generated in the next cycle when a match is detected. Also,the mcgr_dma_req_o#i request for that comparator asserts (to obtain next TPT) until the corresponding application acknowledgment is set, when a match is detected. 

The presentation control fields (PPSCMD#i field of MAC_PPS_Control) determine the shape of the generated waveform. You can program these fields to either toggle or generate a high/low pulse for one PTP clock cycle, when matched. 

Media clock recovery: A match occurs, when the free-running CPT value matches the received TPT value. An output signal, EMAC_TMR signal as shown in the IO mux sheet asserts (toggle, low pulse, or high pulse) on the basis of the programmed presentation control value. 

Media clock generation : On the basis of the presentation control value programmed in MAC_PPS_Control, the particular comparator captures the presentation time and programs it into MAC_PPS(#i)_Target_Time_Second register. The captured timestamp is read when a request is raised to the application. No new timestamps are captured, until the read operation is complete acknowledgment is received from the application. 

### 75.11.9.3 Media clock generation and recovery flow 

Figure 436 shows the media clock generation and recovery flow. Write 1 to MAC_Timestamp_Control[PTGE] for CPT generation and write 1 to MAC_PPS_Control MCGREN#i field to enable the corresponding instance in the MCGR mode, for both media clock generation and recovery. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4123-08.png)


<!-- Start of picture text -->
Read data - CPT at trigger<br>mcgr_dma_req_o[3:0] Compare and capture unit TSTRH0 CSR<br>TSTRH1<br>TSTRH2<br>PTP<br>TSTRH3<br>mcgr_dma_ack_i[3:0]<br>Sync block<br>Sync block<br>Sync block<br>Sync block<br>Presentation time<br>Comparator3<br>Comparator2<br>mcg_pst_trig_i[3:0]<br>Comparator1<br>Comparator0<br>Write path<br>Read path<br>Write data - TPT value<br>EMAC_TMR[3:0]<br><!-- End of picture text -->

Figure 436. Media clock generation and recovery flow 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4123 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

~~<mark>NOTE</mark>~~ 

1. The consecutive triggers to sample the presentation time must assert after a few PTP clock cycles so as to allow synchronization delays. (There is no such issue when the input trigger maximum frequency is 8 KHz and the PTP clock runs at least at 1MHz) 

2. In the Media Clock Recovery mode, the DMA acknowledgment is both posted as well as non-posted. 

See Programming guidelines for media clock generation and recovery for more information. 

## 75.11.10 One step timestamp 

IP supports the one step timestamp feature. Writing 1 to bit 20 (OSTC) in the control word, enables the one step timestamp feature for a packet. 

See the Programming guidelines for IEEE 1588 timestamping for more information. 

## 75.11.11 IEEE 1588 sub nanoseconds timestamp 

IP supports the ingress and egress correction accuracy in sub nanoseconds. It is programmed 

in MAC_Timestamp_Ingress_Corr_Subnanosec[TSICSNS] and MAC_Timestamp_Egress_Corr_Subnanosec[TSECSNS], respectively. In this case, the correction has an unit of nanosecond, multiplied by 2^8. You must program the least significant 8 bits of the value in the sub-nanoseconds register. 

For example, if the required egress correction is 3.6 nS and MAC_Timestamp_Control[TSCTRLSSR] is 1, then MAC_Timestamp_Egress_Corr_Nanosecond[TSEC] must be 0x3 and MAC_Timestamp_Egress_Corr_Subnanosec[TSECSNS] must be 0x99 (0.6 * 256). Similarly, if the required ingress correction is -3.6 nS and 

MAC_Timestamp_Control[TSCTRLSSR] is 1, then MAC_Timestamp_Ingress_Corr_Nanosecond[TSIC] must be 0xBB9A_C9FC and MAC_Timestamp_Ingress_Corr_Subnanosec[TSICSNS] must be 0x66 (fractional part of (10^9 - 3.6) * 256). 

# 75.12 Multiple channels and queues support 

This section and all its sub-sections are Synopsys Proprietary. Used with permission. 

IP support three queues and channel on Tx and Rx paths. Figure 437 shows the architecture of IP with three queues and channel. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4124 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4125-01.png)


<!-- Start of picture text -->
Gigabit Ethernet Media Access Controller (GMAC)<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4125-02.png)


<!-- Start of picture text -->
External transmit memory<br>TSO memory Q0, Q1, Q2, ...Q7<br>Transmit DMA CH 0<br>AHB or AXI TSO engine Transmit  MTL MAC<br>master COE transmit transmit<br>interface Receive DMA CH 0 engine(s) queue<br>scheduler<br>DMA CH0 CSR<br>MTL transmit FIFO controller<br>Transmit DMA CH 1<br>TSO engine<br>Optional<br>AHB, AXI,  PHY<br>APB, or APB3 Receive DMA CH 1 interface<br>interfaceslave DMA CH1 CSR (RGMII, RTBI,TBI, SGMII,<br>· MTL receive RMII, SMII or<br>·· queue arbiter MAC RevMll)<br>receive<br>Transmit DMA CH 7<br>TSO engine Select<br>MTL receive FIFO controller<br>Receive DMA CH 7 (G)MII<br>DMA CH7 CSR<br>MAC<br>CSR<br>DMA CSR MTL CSR<br>EQOS-CORE<br>EQOS-MTL<br>EQOS-DMA<br>EQOS-AXI or EQOS-AHB<br>Externai receive memory<br>Q0, Q1, Q2, ... Q7<br>DMA Arbiter<br><!-- End of picture text -->

Figure 437. Module with multiple channels and queues block diagram 

The above block diagram, support only three queues. 

IP DMA arbiter support two types of arbitration scheme, fixed priority and weighted round-robin. The DMA arbiter performs the arbitration between the Tx and Rx paths of DMA channels to access descriptors and data buffers. DMA_Mode[DA] specifies the arbitration scheme (fixed or weighted round-robin) between the channel Tx and Rx DMA. 

DMA_Mode[TXPR] sets the priority between the corresponding Tx DMA and Rx DMA. Writing 1 to DMA_Mode[PR] specifies the weighted priority between the Tx DMA and Rx DMA in round robin arbitration scheme. 

Table 574 provides an information about the priority scheme between Tx DMA and Rx DMA. 

Table 574. Priority scheme for Tx DMA and Rx DMA 

|Bit 14|Bit 13|Bit 12|Bit 11|Bit 10|Priority schemes|
|---|---|---|---|---|---|
|x|x|x|0|1|Rx always has priority over Tx|
|0|0|0|0|0|Tx and Rx have equal priority. Rx gets the access first on simultaneous requests|
|0|0|1|0|0|Rx has priority over Tx in ratio 2:1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4125 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 574. Priority scheme for Tx DMA and Rx DMA (continued) 

|Bit 14|Bit 13|Bit 12|Bit 11|Bit 10|Priority schemes|
|---|---|---|---|---|---|
|0|1|0|0|0|Rx has priority over Tx in ratio 3:1|
|0|1|1|0|0|Rx has priority over Tx in ratio 4:1|
|1|0|0|0|0|Rx has priority over Tx in ratio 5:1|
|1|0|1|0|0|Rx has priority over Tx in ratio 6:1|
|1|1|0|0|0|Rx has priority over Tx in ratio 7:1|
|1|1|1|0|0|Rx has priority over Tx in ratio 8:1|
|x|x|x|1|1|Tx always has priority over Rx|
|0|0|0|1|0|Tx and Rx have equal priority. Tx gets the access first on simultaneous requests|
|0|0|1|1|0|Tx has priority over Rx in ratio 2:1|
|0|1|0|1|0|Tx has priority over Rx in ratio 3:1|
|0|1|1|1|0|Tx has priority over Rx in ratio 4:1|
|1|0|0|1|0|Tx has priority over Rx in ratio 5:1|
|1|0|1|1|0|Tx has priority over Rx in ratio 6:1|
|1|1|0|1|0|Tx has priority over Rx in ratio 7:1|
|1|1|1|1|0|Tx has priority over Rx in ratio 8:1|



## 75.12.1 Multiple queues and channels support in the transmit path 

IP support three transmit queues and three channels. 

Fixed priority scheme is the default priority scheme for the DMA channels and channel with highest priority always wins the arbitration when it requests for the bus. Channel 0 is always of lowest priority and channel 1 is always of highest priority. 

In weighted strict priority (WSP), the weight corresponds to the number of burst transfers given to a channel in one arbitration cycle. Reallocate the unused burst transfers of one or more channels on the basis of the priority. The channel with highest priority receives the unused burst transfer time before it is allocated to a channel with the next highest priority. You can process the next lower priority, when a channel uses the allocated burst transfers. After processing the allocated bandwidth of all the channels that have packets to transmit, allocate any unused burst transfer time to the channel of the highest priority (if required), and then next highest priority (if required), and so on. 

In weighted round robin (WRR) priority scheme, program the weight through TCW field of DMA_CH#_Tx_Control register. IN WRR scheme, service all channels in round-robin order according to the weights settings. Table 575 shows that the TCW field of DMA_CH#_Tx_Control register provides the weight for each transmit channel. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4126 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 575. Weight for DMA channels 

|TCW Field|Transmit Channel Weight|
|---|---|
|000|1|
|001|2|
|010|3|
|011|4|
|100|5|
|101|6|
|110|7|
|111|8|



The configured weights correspond to the number of burst transfers given to a channel in one arbitration cycle. The unused or excess burst transfers are distributed equally to all channels. 

See Programming guidelines for multi-channel multi-queuing for more information. 

## 75.12.2 Multiple queues and channels support in the receive path 

IP support three receive channels and three queues. 

In the receive direction, the MTL Rx controller selects the Rx DMA for which it transfers or reads the data from the receive FIFO memory. This scheduling is based on the programming done in the respective MTL_RxQ[x]_Control register. 

Each Rx DMA indicates when it is ready to transfer data and the size of the burst-length (number of beats) that it will transfer. The scheduler checks whether sufficient data (of requested burst length) is available to transfer to these DMAs and then selects the receive DMA that is serviced using the programmed priorities. 

See Programming guidelines for multi-channel multi-queuing for more information. 

## 75.12.3 Rx queue to DMA mapping 

You can program MTL_RxQ_DMA_Map0 (for queues 0, 1, and 2) to route the packets in the MTL receive queues to any one of the multiple DMA channels. 

The following types of receive queue to DMA mapping is possible through programming. 

### 75.12.3.1 Static mapping 

In this mode, you can connect all the packets of the receive queue to a specific DMA channel. For example, all the packets from the receive queue 0 program MTL_RxQ_DMA_Map0[Q0MDMACH] (bit[3:0]) and MTL_RxQ_DMA_Map0[Q0DDMACH] (bit[7] = 0) to route to a DMA channel. 

Similarly, packets from other receive queues program register fields corresponding to each queue to route to any DMA channel. 

### 75.12.3.2 Dynamic (per packet) mapping 

In this mode, the destination DMA channel of a packet read from a Rx queue is not constant but it is decided independently for each packet. For example, if you write 1 to MTL_RxQ_DMA_Map0[Q1DDMACH], it indicates that the static mapping disables for receive queue 1 and ignores the value in MTL_RxQ_DMA_Map0[Q1MDMACH]. The MAC receiver decides the destination DMA channel for each packet, depending on the following in decreasing order of priority: 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4127 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

1. L3-L4 filter based DMA selection : The TCP/UDP and IP header fields of the received packet are matched against the corresponding values programmed and enabled for comparison in the MAC_L3_L4_Address_Control register. If the match is successful, the DMA channel number programmed in the DMCHN field of the MAC_L3_L4_Address_Control register is selected as the destination DMA channel number, if DMCHEN field of the same register is 1. If none of the L3-L4 registers give a comparison match, then the module proceeds to the next step below. 

2. Extended VLAN based DMA selection : Extended routing is applicable only if the VLAN filter has passed. Routing is done only on the basis of the perfect filter result. Each perfect filter has a DMA channel enable and a DMA channel number field which you can program. Routing is applicable for a filter, only if the DMA channel enable field is 1. The frame routes to the smallest matching filter's DMA channel, if it is enabled. If the filter's DMA channel number is not enabled, the frame route to channel 0. For example, if a frame's VLAN tag matches filters 7, 3, and 1, then the MAC checks if DMA channel number of filter 1 is enabled through programming. If yes, the frame route to the programmed value; otherwise it route to DMA. When the inverse filter is enabled; is routed to the least mismatched filter's DMA channel number provided it is enabled. If the DMA Channel enable bit is not set, then the frame routes on the basis of the DA based addressing or to channel 0. 

If hash filter is also enabled, it is determines the filter result only. Routing will still depends on the enabled perfect filters. Routing based on the VLAN filter will not occur if none of the perfect filters are enabled or if all of them are bypassed. The frame will route via DA based addressing or to channel 0. If all the perfect filters fails and the hash filter has passed, then the VLAN filter result is a pass but routing will be based on DA based addressing or to channel 0. Similar behavior is seen when you enables inverse filtering as well. 

3. Ethernet DA-based DMA selection : The DA address of the received packet is compared against the programmed DA values in MAC address registers. If the address matches any of the programmed values, the corresponding DCS field (when enabled) determines the destination DMA channel number. 

If none of the above operations make a successful match or decision, then the packet routes to the DMA channel 0 by default. 

### 75.12.3.2.1 Broadcast/multicast packet duplication 

This feature provides a mechanism to send the received broadcast or multicast packets to multiple DMA channels. 

MAC_Address0_High[DCS] and other optional MAC_Address(#i)_High (i=1 to 2) registers determines the DMA channel number to which the received packet (that matches the MAC address present in that register) must route. 

DMA channel routing mechanisms such as extended VLAN, or L3-L4 based routing does not support the packet duplication. 

The packet duplication feature is supported only on the highest MTL queue configured. Therefore, you must program MAC_RxQ_Ctrl1[MCBCQ] to the highest RxQ present in the configuration for the packet duplication for broadcast or multicast packets. 

## 75.12.4 Selection of tag priorities assigned to receive queues 

Program the PSRQ field in the corresponding MAC_RxQ_Ctrl2 to assign the VLAN tag priorities to receive queues. The bit corresponding to the VLAN tag priority can be set in the PSRQ field for assigning that priority to the receive queue. For example, if you want to assign VLAN tag priority of 3 to receive queue 0, write 1 to bit [3] in PSRQ field of MAC_RxQ_Ctrl2. The VLAN tag priority assigned to particular receive queue must be unique, that is, you cannot assign more than one receive queue to the same VLAN tag priority. However, more than one VLAN tag priorities can be assigned to same receive queue. 

The settings in the PSRQ field is used for VLAN tagged receive packet routing to receive queues as well as for PFC based transit flow control. The received VLAN tagged receive packet route to receive queue that has the VLAN tag priority match. In PFC based transit flow control, PSRQ field corresponding to a particular receive queue enables VLAN tag priorities in the PFC packet transmitted when corresponding receive queue reach the threshold level. 

## 75.12.5 Receive side routing from MAC to queues 

IP supports receive side routing from MAC to queues. MAC route the receive packets to the receive queues on the basis of the these packet types in that order 

- Unicast/Multicast destination address packets that fail the destination address filter 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4128 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

- Multicast/Broadcast destination address packets that pass the destination address filter 

- VLAN tag priority field in VLAN tagged AV data packets 

- AV control packets 

- VLAN tagged IEEE 1588 PTP over Ethernet packets 

- Untagged IEEE1588 PTP over Ethernet packets 

- VLAN tag priority field in VLAN tagged packets 

- Untagged packets 

You can route the outer C-VLAN tagged AV data receive packets on the basis of the priorities assigned to receive queues through PSRQ field in the corresponding MAC_RxQ_Ctrl2 and MAC_RxQ_Ctrl3 and the corresponding receive queue is enabled for AV through RXQ#EN field in MAC_RxQ_Ctrl0. These packets may be single VLAN tagged with C-VLAN type or double VLAN tagged with outer VLAN tag of C-VLAN type when double VLAN feature enables (MAC_VLAN_Tag_Ctrl[EDVLP] = 1) with an inner C-VLAN tagged or inner S-VLAN tagged when SVLAN processing is enabled (MAC_VLAN_Tag_Ctrl[ESVL] = 1). This type of Rx packet routing is available when you select the AV feature and multiple receive queues in the configuration. 

You can route the AV control receive packets on the basis of the receive queue number specified in MAC_RxQ_Ctrl1[AVCPQ] and the corresponding receive queue is enabled for AV through RXQ#EN field in MAC_RxQ_Ctrl0. These packets may be single VLAN tagged with C-VLAN type or double VLAN tagged with outer VLAN tag of C-VLAN type when double VLAN feature is enabled (MAC_VLAN_Tag_Ctrl[EDVLP] = 1) with inner C-VLAN tagged or inner S-VLAN tagged when SVLAN processing is enabled (MAC_VLAN_Tag_Ctrl[ESVL] = 1). This type of receive packet routing is available when you select the AV feature and multiple receive queues in the configuration. 

You can route the VLAN tagged receive packets on the basis of the priorities assigned to receive queues through PSRQ field in corresponding MAC_RxQ_Ctrl2 and MAC_RxQ_Ctrl3 and RXQ#EN field in MAC_RxQ_Ctrl0 enables the corresponding receive queue for DCB/generic. This type of receive packet routing is available when you select the multiple receive queues in the configuration. 

You can route the untagged IEEE 1588 PTP over Ethernet receive packets on the basis of the receive queue number specified in MAC_RxQ_Ctrl1[PTPQ] and the corresponding receive queue is enabled through RXQ#EN field in MAC_RxQ_Ctrl0. Also, you can route the VLAN tagged IEEE 1588 PTP over Ethernet receive packets on the basis of the priorities assigned to receive queues through PSRQ field in corresponding MAC_RxQ_Ctrl2 and MAC_RxQ_Ctrl3 or the receive queue number specified in the MAC_RxQ_Ctrl1[PTPQ] and RXQ#EN field in MAC_RxQ_Ctrl0 register enables the corresponding Rx queue. Programming MAC_RxQ_Ctrl1[TPQC] determines this. This type of receive packet routing is available when IEEE 1588 timestamp feature supports and the multiple receive queues are selected in the configuration. The VLAN tagged IEEE 1588 PTP over Ethernet receive packets are detected only when you disables 802.1AS mode (MAC_Timestamp_Control[AV8021ASMEN] = 0), otherwise this type of receive packets are routed as generic VLAN tagged Rx packets. 

You can route the multicast or broadcast destination address receive packets that passes the destination address filter on the basis of the receive queue number specified in MAC_RxQ_Ctrl1[MCBCQ]the MCBCQ field of MAC_RxQ_Ctrl1 register when enabled through MAC_RxQ_Ctrl1[MCBCQEN] and the corresponding receive queue is enabled through RXQ#EN field in MAC_RxQ_Ctrl0. This type of Rx packet routing is available when you select the multiple receive queues in the configuration. 

You can route the untagged receive packets on the basis of the receive queue number specified in MAC_RxQ_Ctrl1[UPQ] and RXQ#EN field in MAC_RxQ_Ctrl0 enables the corresponding receive queue. This type of receive packet routing is available when you select the multiple receive queues in the configuration. 

The unicast destination address receive packets that fail the destination address filter can be routed based on the receive queue number specified in MAC_RxQ_Ctrl4[UFFQ] when enabled through MAC_RxQ_Ctrl4[UFFQE]UFFQE, MAC_Packet_Filter[RA] = 1 and the corresponding receive queue is enabled through RXQ#EN field in MAC_RxQ_Ctrl0. This type of receive packet routing is available when you select the multiple receive queues in the configuration. 

You can route the multicast destination address receive packets that fails the destination address filter on the basis of the receive queue number specified in MAC_RxQ_Ctrl4[MFFQ] when MAC_RxQ_Ctrl4[MFFQE] enables it. MAC_Packet_Filter[RA] = 1 and RXQ#EN field in MAC_RxQ_Ctrl0 enables the corresponding receive queue. This type of receive packet routing is available when you select the multiple receive queues in the configuration. 

The receive packet will route through the receive queue 0, if it is not classified in any of the defined packet type for routing. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4129 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## 75.12.6 Receive side arbitration between DMA and MTL 

IP controller supports receive side arbitration between DMA and MTL. 

After the current packet processing completes, the DMA channel controller fetches the next descriptor and after the descriptor fetching completes, the DMA channel controller evaluates the amount of data to transfer to the Rx buffer on the basis of the programmed PBL and receive buffer length. Accordingly, it requests the MTL to transfer the data. 

After servicing the current request, the MTL receive queue arbitration scheme selects receive queue on the basis of the arbitration scheme (MTL_Operation_Mode[RAA]) and the weights programmed in queue <n> receive control register. The arbitration is done among queues for which DMA is ready to service. After the receive queue is selected, PBL amount of data is read out from that queue and route to the receive DMA channel on the basis of the receive channel selection criteria. 

The arbitration occur after every PBL data transfer completes and descriptors are ready for processing from at least one DMA channel. 

## 75.12.7 Transit side arbitration between DMA and MTL 

IP supports transit side arbitration between DMA and MTL. Transit DMA channels and transit queues are always mapped directly because the number of transit DMA channels are always equal to the number of transit queues in MTL. For instance, each transit DMA pushes data into its respective transit queue assigned to it. 

The data inside each transit queue is stored in packets. Therefore, if two DMAs are allowed to transfer data into the same queue, when a transit DMA starts a packet transfer, the other DMA cannot transfer data unless the previous packet is completely pushed-in. This means that the second DMA remains idle until the first packet is transferred. Hence, each DMA is always connected directly to its corresponding transit queue. 

## 75.12.8 Audio video bridging 

IP supports the audio video bridging in 100 Mbps mode only, which allows the transmission of time sensitive traffic over network. IP implements these protocol for supporting the AVB feature: 

- IEEE 802.1Qbv-2015 (Enhancements to scheduling traffic) 

- IEEE 802.3br (Interspersing traffic) 

- IEEE 802.1Qbu (Frame preemption) 

The queue 0 transmit path supports the strict priority algorithm, and it is used for best-effort traffic when transmit paths of additional queues use the credit-based shaper algorithm to support traffic management. For a queue, the credit-based shaper algorithm determines that a queue is available for transmission if these conditions are true: 

- The queue contains one or more packets. 

- The credit for the queue is positive per the algorithm 

- AV traffic is received on all queues. IP can also receive untagged PTP packets in addition to AV traffic on any queue. 

## 75.12.9 Data Centre Bridging 

The Data Center Bridging feature supports three types of algorithms: 

- Weighted Round Robin: In Weighted Round Robin (WRR) algorithm, each queue is assigned a weight based on the percentage of configured bandwidth. All queues are serviced in the round-robin order according to the weight settings. This algorithm is less complex and requires less hardware as compared to other algorithms. Large packets get more bandwidth in this algorithm. 

- Deficit Weighted Round Robin: In Deficit Weighted Round Robin (DWRR) algorithm, each queue is assigned a weight based on the percentage of configured bandwidth. A deficit counter holds the credit for transmission. The quantum value, proportional to the bandwidth, is added to the deficit counter every time a queue is scanned. The packet in the queue is selected for transmission only if the credit in the deficit counter is less than or equal to the size of the packet available at the head of the queue. A selected queue is serviced until the outstanding credit is lesser than the packet size at the head of the queue during a particular queue scan cycle. After this, the next lower priority queue is serviced. When the packets in a queue 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4130 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

are over, the credit becomes zero for that queue scan cycle. This algorithm is less complex, and it provides more fairness in scheduling as compared to other algorithms. 

- Weighted Fair Queuing: In Weighted Fair Queuing (WFQ) algorithm, each queue is assigned a weight based on the percentage of configured bandwidth. The algorithm computes the finish time of packets at the head of the queues based on the packet size and weights for the queue. The packets with earliest finish time is scheduled for transmission first. The algorithm is more complex and less scalable as compared to other algorithms. 

## 75.12.10 Queue modes 

Transit and receive queues both handles the AV traffic. 

Queueing is based on WRR (Weighted round robin) or WSP (Weighted strict priority) algorithm for generic traffic. It is based on CBS (Credit Base Shaper) and SP (Strict Priority) algorithm for AV traffic. 

The receive queue is configured for generic or AV based routing, which depends on the RXQ#EN field of corresponding queue. Queueing is done on the basis of the VLAN tag priority. The VLAN tag priority must match the PSRQ field of MAC_RxQ_Ctrl2. The receive packets can route to a particular DMA channel on the basis of the DCS field of perfectly-matched MAC address register. 

By default, the untagged packets in a generic traffic route to the receive queue specified in MAC_RxQ_Ctrl1[UPQ]. Queue 0 is the default value of MAC_RxQ_Ctrl1[UPQ]. You can override the default value with any other value, for the MAC_RxQ_Ctrl1[UPQ]. 

The AV control packets (tagged or untagged) route on the basis of MAC_RxQ_Ctrl1[AVCPQ]. The PTP over Ethernet packets route on the basis of MAC_RxQ_Ctrl1[PTPQ]. 

## 75.12.11 Queue priorities 

You can program the priority of an receive queue in the corresponding field of MAC_RxQ_Ctrl2. Also, you must program the AV queue (high priority) as an higher priority than the best-effort queue (low priority). 

## 75.12.12 Enhancements to scheduled traffic (EST) 

The IEEE 802.1Qbv-2015 defines the schedule for each queues on every egress port which makes the implementation aware of traffic arrival schedule. This information blocks the lower priority traffic from transmission in this time window or slot. This ensures that the sender forward the scheduled traffic to receiver through all the network nodes with a deterministic delay. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4131-14.png)


<!-- Start of picture text -->
Periodic priority data<br>Scheduled traffic windows<br><!-- End of picture text -->

Figure 438. Time aware shaper implementation for traffic scheduling 

An important requirement to achieve a low latency is to ensure that there are no interfering frames during the scheduled windows that are reserved for high priority traffic. The use of scheduled traffic imposes limitations when a transmission starts. 

As shown in Figure 439 , if an interfering frame begins transmission just before the reserved time period starts, it can extend transmission into the reserved window, and potentially interfere with higher priority traffic. Therefore, a guard band whose size is equal to the largest possible interfering frame is required before the window starts. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4131 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4132-02.png)


<!-- Start of picture text -->
Late<br>Interfering frame<br>Guard band<br>Interfering frame<br><!-- End of picture text -->

Figure 439. Implementing a guard band to avoid delays due to interfering frames 

A larger guard band equates to a less efficient use of network bandwidth. However, this issue is addressed with the implementation of IEEE802.1Qbu (frame preemption). Frame preemption breaks the interfering frame into smaller fragments. Therefore, the guard band must be as large as the largest possible interfering fragment instead of the largest possible interfering frame. 

During the guard band, only the frames that can complete the transmission of the entire frame before the next gate close event are permitted. This ensures that the high priority traffic can always start at the beginning of the window reserved for it. 

### 75.12.12.1 Frequently used terms in EST 

These are some of the frequently used terms in the EST support and their definitions. 

- Gate control list: The list in the hardware memory that hold the gate controls and the associated time intervals. 

- Gate controls: For a given schedule (row in gate control list) there is a gate open (O) and gate close (C) state associated with each TC. The set of O or C values, whose width is same as configured TCs is called the gate controls. Example: CCOCOOCO means TC7=C, TC6=C, TC5=O and so on. 

- Time interval: Time interval (in nanoseconds) is a 16, 20, or 24-bit configurable field in the gate control list that indicates the time for which the associated gate controls are valid. 

- Base time register: Each gate control list is associated with a 64-bit base time register that holds the start time (in PTP format) for the list. 

### 75.12.12.2 Updates to the transmit scheduling to support EST 

To support EST, these updates are required to transmit scheduling: 

- Implementation of gate control list (GCL) 

- Enforcing gate controls in the scheduler 

- Utilizing gate open (O) duty cycle in the computation of idleSlope (CBS) 

### 75.12.12.2.1 Implementation of gate control list (GCL) 

Figure 440 shows how the gate control list governs the gate close(C) and open(O) events on the basis of the schedule provided for each event. GCL has two parts: 

- Time interval: Defines the time in nanoseconds for which the gate controls are valid and must apply before reading the next gate controls from the list. The configurable width of 16, 20 or 24-bit represents a maximum of 64us, 1ms, or 16ms schedule interval respectively. It supports left shift of the time interval upto 7 bits to be able to apply a multiplication factor from 1 to 128ns (in steps of 2(power)n). The maximum value (post shifting) of this field must be 999,999,999 ns. 

- Gate control: Defines the open (O) represented by logic 1 or close (C) represented by logic 0 state for the gate of each TC. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4132 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4133-02.png)


<!-- Start of picture text -->
Queue for Queue for Queue for Queue for Queue for<br>traffic class #7 traffic class #6 traffic class #5 traffic class #4 traffic class #0<br>T00: oCooCooo<br>Transmission Transmission Transmission Transmission Transmission<br>T01: CoCooCCo<br>selection selection selection selection selection<br>T02: oCooCooo<br>algorithm algorithm algorithm algorithm algorithm T03: ooCooCCo<br>T04: oCooCooo<br>T05: CoCCoCCC<br>Transmission Transmission Transmission Transmission Transmission T06: oCooCooo<br>Gate = C Gate = o Gate = C Gate = C Gate = C T07: CoCooCCC<br>T08: oCooCooo<br>T09: CoCCoCCC<br>...<br>T78: oCooCooo<br>Transmission selection T79: CoCooCCC<br>Note: Only two queues are supported<br><!-- End of picture text -->

Figure 440. Block diagram from IEEE 802.1 Qbv specification - GCL governing gate close and open events 

The implementation of GCL consists of these two gate control lists: 

- HWOL - Hardware owned list which is a list for hardware access. 

- SWOL - Software owned list which is a list for software access. 

The access to these lists is mutually exclusive. Hardware sets the ownership to the list in MTL_EST_Status[SWOL]. Table 576 provides the implementation details of GCL. 

Table 576. External memory used for holding the two gate-control lists 

|Gate control (up to 8 bits)|Time interval (ns) 16, 20, or 24 bits||
|---|---|---|
|OOCCCCCC|T0|HWOL or SWOL|
|OOOOCCCC|T1||
|CCCCOOCC|T2||
|CCCCCCOO|T3||
|I|I||
|I|I||
|OCOCOCOO|||
|OOOOCCCC|T last||
|OOOOCCCC|T0|SWOL or HWOL|
|OOOOCCCC|T1||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4133 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 576. External memory used for holding the two gate-control lists (continued) 

|Gate control (up to 8 bits)|Time interval (ns) 16, 20, or 24 bits|
|---|---|
|OOCCCCCC|T2|
|OOOOCCCC|T3|
|I|I|
|I|I|
|OCOCCCCC||
|OOCCCCCC|T last|



### 75.12.12.2.2 Registers related to gate control list 

The following are the set of four registers (one for each GCL) related to GCL. These registers are implemented through Indirect addressing using MTL_EST_GCL_Control and MTL_EST_GCL_Data registers. 

1. 64-bit Base time register (BTR) 

2. 40-bit Cycle time register (CTR) 

3. m-bit Time extension register (TER) 

4. n-bit [Gate control] List length register (LLR) (n depends of the configured GCL depth) 

### 75.12.12.2.2.1 Base time register (BTR) 

This is a 64-bit register that specifies the start time to execute the GCL. The format of the BTR is same as the PTP format (upper 32-bits holds time in seconds and lower 32 bits hold time in nanoseconds). After the execution of a given list starts, the implementation can update the value in BTR to indicate the next list execution start time. 

### 75.12.12.2.2.2 Cycle time register (CTR) 

This is a 40-bit register that specifies the time at which the execution of the GCL must repeat. This register consists of an 8-bit value in seconds, and a 32-bit value in nanoseconds (similar to the PTP time format with truncated seconds register). For a given GCL, the start time is "Base Time" + N * "Cycle Time" where N is an integer value that represents the iteration number starting with 0 for first iteration. If the GCL execution takes longer than the cycle time, then the list is truncated at the cycle time and the subsequent loop begins at cycle time. 

### 75.12.12.2.2.3 Time extension register (TER) 

This is a m-bit (where m = Configured time interval width + 7) register that specifies the amount of time (in nano seconds) the current GCL can extend before switching to the new GCL. This helps to avoid the execution of the small fragments of the current list before switching to a new list. 

### 75.12.12.2.2.4 List length register (LLR) 

This is an n-bit register (when n is 7, 8, 9, 10, or 11 for a GCL configured depth of 64, 128, 256, 512, or 1024 respectively) that specifies the integer value of the length of the GCL (that is the number of valid rows in each GCL). The processing of the GCL stops after the number of rows read equals to the LLR value. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4134 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

### 75.12.12.2.3 Transmission gating implementation 

A bridge or an end station can enhance to allow transmission from each TC that is yet to be scheduled relative to a known timescale. To achieve this, a transmission gate is associated with each TC; the state of the transmission gate determines if you can select the queued frames for transmission. 

For a TC, the transmission gate can be in one of these two states: 

1. Open: Select queued frames for transmission, in accordance with the definition of the transmission selection algorithm associated with the TC. 

2. Closed: Does not select queued frames for transmission. 

A frame on a traffic class queue is not available for transmission if the transmission gate is in the closed state or if there is insufficient time available to transmit the entirety of that frame before the next gate-close event associated with that queue. 

The implementation has visibility to the current schedule of gate controls and the immediate next schedule of the gate controls. So the maximum Gate Open period does not exceed the sum of the two Time Intervals. This is because, a frame is selected for transmission only if the gate is currently Open and the duration of gate open interval is greater than the time taken to transfer the entire frame. 

The implementation must know the frame size before the transmission, so that you can avoid the transmission overruns and only the frames that can complete are scheduled at all times. 

The implementation adequately compensates for the implementation delays in the data transfer from the buffer to the line by offsetting the current time with all the relevant delays (provided by MTL_EST_Control[CTOV]). This ensures that the schedule provided is always accurately implemented at the line. 

You must ensure that the GCL slot interval is always greater than the expected packet size and overhead (scheduler delay, inter frame gap (IFG), and preamble, all combined). 

### 75.12.12.3 Idle slope computation updates 

When EST is enabled, credit accumulates only when the gate is open therefore, the effective data rate of the idleSlope must increase to reflect the duty cycle for the transmission gate associated with the queue. 

The idleSlope is computed on the basis of the gate open time and oper cycle time values. Program the idleSlope registers (implemented one per CBS enabled TC) based on the following equation. The existing MTL register has sufficient field width to accommodate the new values for idleSlope. 

idleSlope = (operIdleSlope(N) * OperCycle/GateOpenTime) 

### 75.12.12.3.1 Operational details of GCL 

Write 1 to MTL_EST_Control[SSWL], so that the hardware can access the programmed gate control list. The first set of gate controls are applied when the current time is equal to the value in the base time register (BTR) and is held until the programmed "time interval" value. 

One additional gate control event is always read ahead from the list, to avoid the transmission overruns. This enables the GCL to determine the next gate close events (if any) for the open TCs. 

The scheduling is done on the basis of the gate open state and time interval of only the current and subsequent schedule. An internal accumulator adds the time intervals when gate controls are applied. BTR + Accumulator specifies the time at which the next set of gate controls are applied. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4135 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4136-02.png)


<!-- Start of picture text -->
CTR = 6000 ns<br>BTR = 14200 ns<br>Gate control Time interval<br>OOCCCCCC 1000<br>OOOOCCCC 500<br>CCCCOOCC 2200<br>CCCCCCOO 300<br><!-- End of picture text -->

Figure 441. GCL and associated registers - basetime and cycletime 

GCL is read progressively from the first row adhering to the schedule. The read operations continue until the list length (from LLR register) is reached and the execution of the list restarts at BTR + CTR time. At this point the value in CTR increments BTR to mark the beginning of a new cycle. In the absence of any gate controls, all the gates are in open state, during the execution of the list. 

In cases where the execution time of the list is greater than the cycletime, the list is truncated and the next iteration starts when the current time equals BTR + CTR. 

Table 577. GCL and associated registers - BTR and CTR 

|Current time|Gate control applied|Accumulator value|BTR (with updates)|
|---|---|---|---|
|14200|OOCCCCCC|1000|14200|
|15200|OOOOCCCC|1500|14200|
|15700|CCCCOOCC|3700|14200|
|17900|CCCCCCOO|4000|14200|
|18200|OOOOOOOO|0|20200|
|20200|OOCCCCCC|1000|20200|
|21200|OOOOCCCC|1500|20200|



Table 577 describes an example in which the execution starts at 14200 and the first set of gate controls "OOCCCCCC" are applied immediately. The time interval is 1000 ns, so the next set of gate controls are applied at 14200 (BTR) + 1000 (Accumulator) = 15200 ns . The above table shows that there are no gate controls available after the execution of the last gate control and before the next iteration of the loop. The gates are deemed in open state during that time period as depicted at 18200 current time. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4136 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4137-02.png)


<!-- Start of picture text -->
CTR = 3000 ns<br>BTR = 14200 ns<br>Gate control Time interval<br>OOCCCCCC 1000<br>OOOOCCCC 500<br>CCCCOOCC 2200 1500<br>CCCCCCOO 300<br><!-- End of picture text -->

Figure 442. GCL and associated registers - BaseTime and CycleTime list execution time > CycleTime 

Table 578 indicates that the list execution takes longer than the allocated CycleTime, so the list is truncated and the list starts from the BTR+CTR. 

Table 578. GCL and associated registers - BTR and CTR, execution time > Cycle Time 

|Current Time|Gate Control Applied|Accumulator Value|BTR (with updates)|
|---|---|---|---|
|14200|OOCCCCCC|1000|14200|
|15200|OOOOCCCC|1500|14200|
|15700|CCCCOOCC|3700|14200|
|17200|OOCCCCCC|1000|17200|
|18200|OOOOCCCC|1500|17200|
|18700|CCCCOOCC|3700|17200|



When you apply the third set of gate controls, BTR + CycleTime (17200) < BTR + Accumulator (17900), so the list is truncated and execution switches to a new iteration at 17200. 

### 75.12.12.3.2 Installing a new GCL 

The switch to the new GCL can happen in one of the following ways when a new software programmed GCL is available and executed at the new BTR value: 

- New base time aligned with current schedule 

- New base time unaligned with current schedule 

### 75.12.12.3.2.1 New base time aligned with current schedule 

If the choice of cycle time for the new gating cycle is unchanged from the cycle time for the current gating cycle, and if the BTR chosen for the new gating cycle (new BTR) is an integer multiple of the current cycle time (+ current BTR), then the new gating cycle exactly lines up with the old gating cycle, that is, the cycle start times for the new gating cycle is same as they would have been for the old configuration. This could be considered to be the ideal case and allows the new gating cycle to be installed and 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4137 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

executed with no timing issues. The implementation completes the execution of an iteration of the current list and switches to the new list at the beginning of the BaseTime listed in the new list. 

If (New base time > = Current time) 

ConfigChangeTime = New BaseTime 

Else If (New base time < Current time) 

1. Set the BTRError 

2. ConfigChangeTime = (New BaseTime + N* New CycleTime) 

where N is the smallest integer for which the relation ConfigChangeTime >= CurrentTime and (N =< 8) is true. 

When N > 8 the hardware cannot auto recover and the loop count value in BTRError reporting is set to 1111 requires the software to reprogram the new base time. 

Figure 443 illustrates the installation of the new GCL along with the timelines. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4138-11.png)


<!-- Start of picture text -->
CTR = 6000 ns CTR = 6000 ns<br>BTR = 14200 ns BTR = 50200 ns<br>Gate control Time interval Gate control Incr schedule<br>OOCCCCCC 1000 CCCOCCCC 1000<br>OOOOCCCC 500 CCCCOCCC 2000<br>CCCCOOCC 2200<br>CCCCCCOO 300<br><!-- End of picture text -->

Figure 443. Switching to a new configuration that is aligned with the existing configuration 

In the above example, after the sixth iteration of the first GCL, the BTR values of the old and new GCL are equal. At that point the new GCL is processed as a natural extension to the existing GCL. 

Table 579. GCL and associated registers - BTR and CTR 

|Current time|Gate control applied|Accumulator value|BTR (with updates)|
|---|---|---|---|
|44200|OOCCCCCC|1000|44200|
|45200|OOOOCCCC|1500|44200|
|45700|CCCCOOCC|3700|44200|
|47900|CCCCCCOO|4000|44200|
|48200|OOOOOOOO|0|50200|
|50200|CCCOCCCC|1000|50200|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4138 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 579. GCL and associated registers - BTR and CTR (continued) 

|Current time|Gate control applied|Accumulator value|BTR (with updates)|
|---|---|---|---|
|51200|CCCCOCCC|3000|50200|
|53200|OOOOOOOO|0|56200|



### 75.12.12.3.2.2 New base time unaligned with current schedule 

If the new cycletime differs from the current cycletime or new basetime in the future and is not an integer multiple of current cycletime, then the old and new cycles do not line up. When new basetime is reached ( when the new configuration is installed and starts to execute), the last old cycle is normally truncated to start the first new cycle. This could be undesirable if it results in a very short last old cycle; arguably it would be better to simply extend the penultimate old cycle by that small amount, rather than starting a very short cycle. The Cycle Time Extension Register (related to the current config list) allows this extension of the last old cycle to be done in a defined way; if the last complete old cycle ends normally in less than current Cycle Time Extension (TER) ns before the new base time, then the last complete cycle before new BaseTime is reached is extended so that it ends at new BaseTime. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4139-06.png)


<!-- Start of picture text -->
TER = 1000 ns<br>CTR = 6000 ns CTR = 6000 ns<br>BTR = 14200 ns BTR = 47500 ns<br>Gate control Time interval Gate control Incr schedule<br>OOCCCCCC 1000 CCCOCCCC 1000<br>OOOOCCCC 500 CCCCOCCC 2000<br>CCCCOOCC 2200<br>CCCCCCOO 300 Sixth<br>iteration<br>truncated at<br>1800 ns<br><!-- End of picture text -->

Figure 444. Switching to new list truncating the current list 

At the end of the fifth iteration the Current time + Cycle time extension (TER) < New BTR so the sixth iteration of current configuration is started. During the sixth iteration of the current list when the new BTR value is smaller than the next schedule in the current list, it switches to the new list. 

Table 580. Extending to new list by truncating the current list 

|Current time|Gate control applied|Accumulator value|BTR (with updates)|
|---|---|---|---|
|44200|OOCCCCCC|1000|44200|
|45200|OOOOCCCC|1500|44200|
|45700|CCCCOOCC|3700|44200|
|47500|CCCOCCCC|4000|44200|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4139 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 580. Extending to new list by truncating the current list (continued) 

|Current time|Gate control applied|Accumulator value|BTR (with updates)|
|---|---|---|---|
|48500|CCCCOCCC|0|50200|
|50500|OOOOOOOO|1000|50200|



Below is an example where the current config list is extended instead of starting a new iteration as the extension time of 800 ns is less than the allowed cycle extension time (TER) of 1000 ns. 

Figure 445. Switching to new list by extending the current list 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4140-06.png)


<!-- Start of picture text -->
TER = 1000 ns<br>CTR = 6000 ns CTR = 6000 ns<br>BTR = 14200 ns BTR = 45000 ns<br>Gate control Time interval Gate control Incr schedule<br>OOCCCCCC 1000 CCCOCCCC 1000<br>OOOOCCCC 500 CCCCOCCC 2000<br>CCCCOOCC 2200<br>CCCCCCOO 300 Fifth<br>iteration<br>truncated at<br>1800 ns<br><!-- End of picture text -->

Table 581. Switching to new list by extending the current list 

|Current time|Gate control applied|Accumulator value|BTR (with updates)|
|---|---|---|---|
|38200|OOCCCCCC|1000|38200|
|39200|OOOOCCCC|1500|38200|
|39700|CCCCOOCC|3700|38200|
|41900|CCCCCCOO|4000|38200|
|42200|OOOOOOOO|0|44200|
|45000|CCCOCCCC|1000|45000|
|46000|CCCCOCCC|3000|45000|
|48000|OOOOOOOO|0|51000|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4140 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

### 75.12.12.4 Impact of Transmit Scheduling Algorithms on EST 

When EST is used in isolation, the Gate Control List manages the final open/close state of the Queues along with the checks carried out by the Transmission Selection Algorithm in MTL. As the Gate Controls operate on a predefined repetitive schedule, it is recommended to use Strict Priority or Credit Based Shaper (CBS) scheduling algorithms. 

Other algorithms such as the Weighted Round Robin (WRR), Deficit Weighted Round Robin (DWRR) and Weighted Fair Queuing (WFQ) implement masking of the queues based on the current winning queue. The algorithm is applied only among the group of queues that open simultaneously. To ensure Queues whose gates are "Open" get priority, these algorithms are modified to treat "gate open" queues and "gate closed" queues as separate groups giving priority to gate open queues. 

For example, consider 4 queues (Q3, Q2, Q1, Q0) with weights 4:3:2:1; Q3 and Q2 are in Open state in slot one slot, while Q1 and Q0 are in Open state in another slot. In this case, the scheduler works as follows: 

1. In the first slot, the Q3 and Q2 are serviced in the ratio of 4:3 for the duration the slot is open. 

2. In the second slot, the queues Q1 and Q0 are serviced in the ratio of 2:1. 

3. Fresh arbitration is started every time a slot is opened. 

In other words, the traffic does not get distributed in the intended ratio of 4:3:2:1; but as two groups with different ratios and only for the duration of the slot when the gates are open continuously 

~~<mark>NOTE</mark>~~ 

See Programming guidelines for EST 

## 75.12.13 Frame preemption (FPE) 

Frame preemption breaks the interfering frame into smaller fragments. Therefore, the guard band needs to be only as large as the largest possible interfering fragment instead of the largest possible interfering frame. During the guard band, only the frames that can complete the transmission of the entire frame before the next gate close event are permitted. This ensures that the high priority traffic can always start at the beginning of the window reserved for it. 

Preemption allows one or more higher priority (express) frames to interrupt the transmission of a lower priority (preemptable) frame; the preemptable frame transmission is resumed and completed after the express frame transmission is complete. To support frame preemption, the following two abstractions of the MAC are used: 

- A preemptable MAC, called pMAC, which carries the preemptable traffic. 

- An express MAC, called eMAC, which carries the express traffic. 

In the implementation, only parts of the MAC that holds the state during preemption is replicated and represented as pMAC and eMAC. The MAC uses the following two ways to puts on hold, the transmission of the preemtable traffic, in the presence of express traffic: 

- The MTL scheduler interrupts the preemptable traffic that is currently being transmitted. When the preemption capability is active, the MAC interrupts the transmission and reception of preemptable frames. A preempted fragment can be followed by zero or more express frames, before the continuation fragments. The preemptable frame can be fragmented any number of times, however, the minimum final and non-final fragment length criterion must be is met. However, interleaving of more than 1 preemptable packet is not permitted. This implies that if a preemptable packet is fragmented by an express packet, another preemptable packet cannot be transferred until all the remaining fragments of the first preempted packet are transferred. 

- The MTL scheduler prevents starting the transmission of preemptable traffic. When the preemption capability is inactive, the pMAC entity is disabled and only express traffic is transmitted or received. Frame preemption feature can be enabled by setting EFPE field of the MAC_FPE_CTRL_STS register. 

If you are unable to schedule fragmented packets after a certain number of attempts because of some reason, there is a possibility that the remaining fragmented packets are dropped. For this, software can program MTL_EST_Control[LCSE] to increase number of iterations or MTL_EST_Control[DFBS] to disable dropping of packet. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4141 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

### 75.12.13.1 GCL Modification to Support FPE 

In the EST-only configuration, the GCL entry has up to 24 bits of Time Interval and up to 8 high order bits representing the Gate Open/Close state requirements as shown in the following figure. 

|Gate control<br>(up to 8 bits)|Time interval (ns)<br>16, 20 or 24 bits|
|---|---|
|OOCCCCCC|T0|
|OOOOCCCC|T1|
|CCCCOOCC|T2|
|CCCCCCOO|T3|
|||||
|||||
|OCOCOCOO|T126|
|OOOOCCCC|T127|



Figure 446. Gate Control List When FPE is Disabled 

EST only supports SetGate operation, which implies that the gates are set to either open or close at a given time interval. However, when both Frame Preemption (FPE) and EST are enabled, the GCL also supports Set-and-Hold-MAC and Set-and-Release-MAC operations, in addition to the SetGate operation. To enable the support of hold and release operations, the format of the GCL is slightly changed while configuring and enabling the FPE. The first Queue (Q0) is always programmed to carry preemption traffic and therefore it is always Open. The bit corresponding to Q0 is renamed as Release/Hold MAC control. The TX Queues whose packets are preemptable are indicated by setting the PEC field of the MTL_FPE_CTRL_STS register. The GCL bit of the corresponding Queue are ignored and considered as always "Open". So, even if the software writes a "0" ("C"), it is ignored for such queues. 

|Gate control<br>(up to 7 bits)|Release or hold<br>indication|Time interval (ns)<br>16, 20 or 24 bits|
|---|---|---|
|CCCOOOO|0|T0|
|CCCCOOO|0|T1|
|OCCCOOO|1|T2|
|COCCOOO|1|T3|
|CCOCOOO|1|T4|
|CCCOOOO|0|T5|
|CCCCOOO|0|T6|



Figure 447. Gate Control List When FPE is Enabled 

When the Release/Hold bit transitions from a '0' to '1', a Set-and-Hold-MAC operation is performed. This marks the cease of the preemptable traffic. This is achieved by sending a Hold request to MTL "ha" ns in advance (where ha is the time interval mentioned in the Hold Advance (HADV) field of the MTL_FPE_Advance register). When the Release/Hold bit transitions from a '1' to '0' a Set-and-Release-MAC operation is performed. This marks the resuming of the preemptable traffic. This is achieved by sending a Release request to MTL "ra" ns in advance (where ra is the time interval mentioned in the Release Advance (RADV) field of the MTL_FPE_Advance register). The preemptable traffic is blocked for the time duration the Release/Hold bit is set to a '1' in the Gate Control List. 

### 75.12.13.2 Impact of Preemption on CBS 

In Credit Base Shaper(CBS), the definition of "Transmit" is as follows: 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4142 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

- TRUE for the duration of frame transmission from the queue. 

- FALSE when frame transmission from the queue is complete. 

- When CBS algorithm is used along with frame preemption, the value of "Transmit" is TRUE only while the frame is being transmitted by the MAC. If the frame transmission is delayed or interrupted (for instance, a preemptable frame transmission is interrupted to allow the transmission of an express frame from a different queue, or the start of express frame is delayed because a preemptable frame is being transmitted) the value of "Transmit" is FALSE until transmission of the frame commences or is resumed. 

Also, the value of "Transmit" is FALSE during the transmission of any overhead that is a consequence of frame preemption. For example, additional frame overhead (mCRC, Fragment Count) that is added to the preemptable frame. 

At any given time, if there are no frames in the queue, and the value of Transmit is FALSE, and credit is positive value, the credit value is set to zero if here is no preemptable frame from the queue for which transmission is in progress but has been interrupted. 

### 75.12.13.3 mPacket Format 

When the preemption capability is active, MAC sends mPackets to the PHY. An mPacket can be one of the following: 

1. A express packet 

2. A preemptable packet 

3. An initial fragment of a preemptable packet 

4. A continuation fragment of a preemptable packet 

#### Start mPacket Delimiter (SMD) 

The value of the SMD indicates whether the mPacket contains an express packet, the start of a preemptable packet (initial fragment or complete packet), or any of continuation fragments of a preemptable packet. Following table shows the valid SMD values. 

Table 582. Possible SMD Values of mPacket 

|mPacket Type|Notation|Frame Count|Value|
|---|---|---|---|
|verify packet|SMD-V|-|0x07|
|respond packet|SMD-R|-|0x19|
|express packet|SMD-E|-|0xD5|
|preemptable packet start|SMD-S0|0|0xE6|
||SMD-S1|1|0x4C|
||SMD-S2|2|0x7F|
||SMD-S3|3|0xB3|
|continuation fragment|SMD-C0|0|0x61|
||SMD-C1|1|0x52|
||SMD-C2|2|0x9E|
||SMD-C3|3|0x2A|



frag_count 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4143 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

A frag_count is a modulo-4 counter that increments for each continuation fragment of the preemptable packet. The frag_count protects against mPacket reassembly errors by enabling detection of the loss of up to 3 packet fragments. 

The frag_count field is present only in mPackets with SMD-C notation (continuation fragment). The frag_count is zero in the first continuation fragment of each preemptable packet. 

Table 583. Possible frag_count Values 

|frag_count|Value|
|---|---|
|0|0xE6|
|1|0x4C|
|2|0x7F|
|3|0xB3|



#### mData 

The contents of the packet from the MAC, starting with the first byte after the SFD to the last byte before the FCS are sent in the mData fields of one or more mPackets for that frame. The minimum size of the mData field is 60 bytes. 

CRC The CRC field contains a cyclic redundancy check (CRC) and has an indication of the final mPacket of a frame. In the final mPacket of a frame, the CRC field contains the last 4 octets of the MAC frame (the FCS field). 

For other mPackets, the CRC field contains an mCRC value. The mCRC is calculated on the octets of the packet from the first octet of the frame (the octet following the SFD of preemption frames) to the last octet of the packet transmitted in that mPacket by performing an XOR of the calculated 32 bit CRC value of the fragment and a value of 0x0000FFFF. 

Summary of Packet Formats 

- Express Packet: 7bytes of PREAMBLE, SMD-E, Data, and CRC 

- Complete Preemptable Packet: 7 bytes of PREAMBLE, <Current Preemptable packet SMD>, Data, CRC 

- Initial Fragment (non-final) of Preemptable Packet: 7 bytes of PREAMBLE, <Current Preemptable packet SMD>, Data, mCRC 

- Continuation fragments (non-final) of Preemptable packet: 6 bytes of PREAMBLE, <Current Preemptable continuation fragment SMD>, <Current Preemptable continuation fragment FC>, Data, mCRC 

- Final fragment of Preemptable packet: 6 bytes of PREAMBLE, <Current Preemptable continuation fragment SMD>, <Current Preemptable continuation fragment FC>, Data, CRC 

Table 584. Current and Previous SMD Values 

|Previous Preemptable packet SMD|Current Preemptable packet SMD|
|---|---|
|SMD-S0|SMD-S1|
|SMD-S1|SMD-S2|
|SMD-S2|SMD-S3|
|SMD-S3|SMD-S0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4144 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 585. Current and Previous SMD Values 

|Previous Preemptable<br>fragment SMD|<br>Previous<br>Preemptable<br>fragment FC|Current Preemptable continuation<br>fragment SMD|Current Preemptable continuation<br>fragment FC|
|---|---|---|---|
|SMD-S0|NA|SMD-C0|FC0|
|SMD-S1|NA|SMD-C1|FC0|
|SMD-S2|NA|SMD-C2|FC0|
|SMD-S3|NA|SMD-C3|FC0|
|SMD-C0|FC0|SMD-C0|FC1|
|SMD-C0|FC1|SMD-C0|FC2|
|SMD-C0|FC2|SMD-C0|FC3|
|SMD-C0|FC3|SMD-C0|FC0|
|SMD-C1|FC0|SMD-C1|FC1|
|SMD-C1|FC1|SMD-C1|FC2|
|SMD-C1|FC2|SMD-C1|FC3|
|SMD-C1|FC3|SMD-C1|FC0|
|SMD-C2|FC0|SMD-C2|FC1|
|SMD-C2|FC1|SMD-C2|FC2|
|SMD-C2|FC2|SMD-C2|FC3|
|SMD-C2|FC3|SMD-C2|FC0|
|SMD-C3|FC0|SMD-C3|FC1|
|SMD-C3|FC1|SMD-C3|FC2|
|SMD-C3|FC2|SMD-C3|FC3|
|SMD-C3|FC3|SMD-C3|FC0|



### 75.12.13.4 Transmit Preemption 

When FPE is enabled (setting EFPE=1 in MAC_FPE_CTRL_STS register), the MTL preempts a preemptable frame, when a "hold" request is asserted (EST/Qbv configured and enabled) express frames are available for transmission, that is, frame is present in MTL FIFO and is qualified for arbitration, after ensuring that the minimum mPacket mData field size is met. Therefore, preemption occurs only if at least 60 bytes of the preemptable frame have been transmitted and at least 64 bytes (including the frame CRC) remain to be transmitted. 

The earliest starting position of preemption is controlled by the AFSZ field of the MTL_ FPE_CTRL_STS Register. Preemption does not occur until at least 64 * (1+ AFSZ) - 4 bytes of the preemptable frame have been sent. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4145 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

When preemption occurs, all the preemptable queues are blocked and only the express queues are allowed to arbitrate (if more than one express queue has traffic) and transmit. 

Continuation fragment of the preempted frame is the first frame to be transmitted after "release" request is asserted (EST/Qbv configured and enabled) and all the express traffic transmission completes. 

~~<mark>NOTE</mark>~~ 

All the PTP packets should be transmitted as express packets 

MTL communicates the following frame-type information to the MAC using a 2-bit preemption control signal on the MTI interface qualified by SoF and EoF. 

- Express Frame 

- Preemption Frame (Full or Fragment) 

- Continuation Fragment (non-Final or Final) 

Table 586. Preemption Control Values on MTI Interface for Various Frame Types 

|Qualifier|Preemption Control Value|Frame Type|
|---|---|---|
|SoF|00|Start Express|
|SoF|01|Start Preemption|
|SoF|10|Continuation Fragment|
|SoF|11|Reserved|
|EoF|00|End of Frame|
|EoF|01|End of Fragment|



MTL should wait for the previous fragment status to be received before resuming the continuation fragments of a preempted frame. Fragment status is described in detail in the Tx Fragment Status section. 

### 75.12.13.4.1 MAC Tx Preemption 

MAC supports preemption by implementing the functionality needed to generate the mPackets as described in “mPacket Format”. 

Based on the Preemption Control value received on the MTI interface (qualified with SoF and EoF), MAC determines the frame type (shown in the above table 'Preemption Control Values on MTI Interface for Various Frame Types') and generates mPackets accordingly. 

When the preemption capability is active, MAC replaces the SFD of a preemption packet with an SMD-S value. A 2-bit rolling frame count is encoded in the SMD-S value. 

The SMD-E value is the same as the SFD value so the SFD of an express packet does not need to be replaced. 

### 75.12.13.4.1.1 Tx Fragment Status 

MAC sends Tx fragment status to indicate successful transmission of fragmented mPackets. 

In case of a transmission error (underflow, jabber, and so on) the frame status is sent (and not a fragment status) with an error indication along with all other relevant status fields. In case of receiving an error status for a transmitted fragment, the MTL drops the remaining fragments and does not send any more continuation fragments. 

### 75.12.13.5 Receive Preemption 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4146 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

### 75.12.13.5.1 MAC Receive Preemption 

When FPE is enabled, the MAC Receiver pases the incoming packets and differentiates between Express packets and preemptable packets. An SMD containing an SMD-E indicates express packet, and SMD containing an SMD-S indicates the first mPacket of a preemptable packet. 

If an mPacket containing an SMD-S is received when MAC has not completed receiving the previous preempted packet, MAC sets a CRC Error status for the previously received partial packet. 

When an SMD-S is detected, MAC records the frame count indicated by the SMD and then begins sending data on the MRI interface. 

The MAC checks the last four bytes of the mPacket . If the last four bytes of the mPacket do not match CRC, that indicates the end of the packet with or without a CRC error as per the CRC check result. If the last four octets of the mPacket match, that indicates that the packet was preempted. 

An SMD containing an SMD-C indicates an mPacket that continues the data for a preempted packet. Upon receiving an SMD value of SMD-C, MAC checks the following: 

1. A preempted packet is in progress 

2. The frame count indicated by the SMD matches the frame count of the packet in progress 

3. The frag_count value indicates the next fragment count. 

If any of the above check fails, the mPacket is discarded and MAC sets a CRC Error status for the partially received packet. 

If all the checks pass, the next fragment count is incremented modulo 4. 

When a packet is preempted, the MAC saves the state of the partially received packet (filter check status, timestamp, length fields etc.) and will be able to process any received Express packets before the continuation fragment is received. 

The MAC Receiver sends a "dummy status" for all the mPacket fragments successfully received and sends the Rx status with the final fragment. If an error is detected during any of the fragments the Rx status is sent and the fragment is marked as final fragment. All subsequent continuation fragments received for this packet are dropped in the MAC. 

The MAC communicates the following frame type information to the MTL using a 2-bit preemption control signal. 

1. Express Frame 

2. Preemption Frame (Full or Fragment) 

3. Continuation Fragment (non-Final or Final) 

Table 587. Preemption Control Values on MRI Interface for Various Frame Types 

|Qualifier|Preemption Control Value|Frame Type|
|---|---|---|
|SoF|00|Start Express|
|SoF|01|Start Preemption|
|SoF|10|Continuation Fragment|
|SoF|11|Reserved|
|EoF|00|End of Frame|
|EoF|01|End of Fragment|



### 75.12.13.5.1.1 Data Alignment 

When a received frame cannot be fragmented on any byte boundary, MAC retains the unaligned bytes of data in the previous fragment and resends them with the next fragment as shown in the following figure. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4147 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4148-02.png)


<!-- Start of picture text -->
MRI data width - 32-, 64-, or 128-bit wide<br>- - - - - - - X6 X5 X4 X3 X2 X1 Packet fragmented at X3<br>Unaligned fragment<br>End of fragment<br>X3 X2 X1<br>Byte En = 2<br>- - - - - - - X6 X5 X4 X3 X2 X1 Start of continuation fragment<br><!-- End of picture text -->

Figure 448. Data Alignment Feature of MAC 

### 75.12.13.5.1.2 MTL Receive Preemption 

The MTL Rx must have at least 2 Rx queues to support FPE function as the preemptable packets and the express packets must be routed to separate Rx queues. The destination Rx queue of a received packet is controlled by MAC_RxQ_Ctrl[n] registers. Program these registers such that Preemptable traffic and express traffic are not routed to the same Rx queue. As the queue mapping for tagged packets is based on VLAN user-priority field, this implies that priority of preemptable and express packets are mutually exclusive. In other words, packets of a certain priority (traffic class) are either express or preemptable but cannot be both. 

For the preemptable frames, in addition to the PSRQ (Priority Selected in Rx queue) based queue routing, a programmable "Frame Preemption Residue Queue" (FPRQ) is supported to route all other Preemption Packets received (Untagged, SA/ DA or VLAN Filter Fails forwarded due to RA being set or VTFE being reset). 

Table 588. Preemption Control Values on MRI Interface for Various Frame Types 

|Preemption Packet Type|Queue Routing|
|---|---|
|AV Tagged Packets passing the SA/DA and VLAN filters|PSRQ*|
|DCB/Generic Tagged Packets passing the SA/DA and VLAN filters|PSRQ**|
|Tagged Packets failing the SA/DA and VLAN filters without setting the Receive All (RA = 0) or setting<br>VTFE = 1|Dropped|
|All other packets OR when RA = 1|FPRQ|



### 75.12.13.5.1.3 MTL Receive Arbitration 

On the ARI Interface, data is fetched from the MTL Rx FIFO based on the arbitration selected in the MTL_Operation_Mode register. Frame based arbitration can be used only when all the MTL Preemption Queues are operating in Store and Forward mode, else there will be loss of bandwidth on the ARI interface because all the fragments of a preemptable packet is not available. Therefore, any express packets received between the fragments are blocked until all the fragments are received and transferred; this defeats the purpose of express traffic. 

When operating in either Threshold (cut through) or Store and forward modes of operation, PBL based arbitration is recommended over Frame based arbitration. In case of PBL based arbitration, the watermark check is always performed and the arbitration/ transfer of data in terms of chunks of "PBL" size of data which is almost similar to the concepts of "fragments". Therefore the express queue packets get blocked for less time as well as the ARI interface transfers the data without loss of efficiency. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4148 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

### 75.12.13.6 Verify and Respond mPackets 

When FPE function is present, the MAC can receive and detect the Verify and Respond mPackets, even when FPE is not enabled by software. When MAC detects valid Verify/Respond mPackets, it notifies the software by setting the RVER and RRSP fields of MAC_FPE_CTRL_STS register respectively. Optionally an interrupt can be generated. As such packets have empty (all-zero) data payload, they are dropped inside the MAC and not forwarded to the MRI. 

Software can set the SVER and SRSP fields of MAC_FPE_CTRL_STS register to request MAC to transmit Verify and Respond mPackets respectively. Upon successful transmission of these frames, MAC clears the SVER/SRSP bits and sets the TVER & TRSP fields of MAC_FPE_CTRL_STS register. Optionally an interrupt can be generated when these events occur. 

Software must ensure that frame preemption verify and response packet are not triggered at the same time. Trigger either of the packets and then wait for its completion before triggering another packet. 

### 75.12.13.7 Frame Preemption and MMC Counter and Interrupt Registers 

The following MMC counters and associated Interrupt registers are instantiated/present in the MAC when Frame Preemption feature is enabled. 

Table 589. MMC Counters and Associated Interrupt Registers 

|Frame Assembly<br>Error Counter|Description|Associated MMC Counter|
|---|---|---|
|Frame Assembly<br>Error Counter|A 32-bit counter that provides the number of MAC frames<br>with reassembly errors on the Receiver, due to mismatch<br>in the Fragment Count value.|MMC_Rx_Packet_Assembly_Err_Cntr|
|Frame SMD<br>Error Counter|A 32-bit counter that provides the number of received<br>MAC frames rejected due to arriving with an SMD-C when<br>there was no preceding preempted frame.|MMC_Rx_Packet_SMD_Err_Cntr|
|Frame Assembly<br>OK Counter|A 32-bit counter that provides the number of MAC frames<br>that were successfully reassembled.|MMC_Rx_Packet_Assembly_Ok_Cntr|
|MAC Rx<br>Fragment Counter|A 32-bit counter that provides the number of additional<br>mPackets received due to preemption.|MMC_Rx_FPE_Fragment_Cntr|
|MAC Tx<br>Fragment Counter|A 32-bit counter that provides the number of additional<br>mPackets transmitted due to preemption.|MMC_Tx_FPE_Fragment_Cntr|
|Hold Request Counter|A 32-bit counter that maintains the count of number of<br>times a hold request is given to MAC.|MMC_Tx_Hold_Req_Cntr|



### 75.12.13.7.1 Additional Registers Associated With MMC Interrupts 

Following are the additional registers associated with MMC interrupts for the MMC error counters: 

- MMC_FPE_Tx_Interrupt 

- MMC_FPE_Tx_Interrupt_Mask 

- MMC_Rx_Interrupt 

- MMC_FPE_Rx_Interrupt_Mask 

## 75.12.14 Time-Based Scheduling 

Time-based scheduling feature is suitable for traffic whose periodicity and rate are predictable. To improve the quality-of-service of such traffic, 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4149 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

- The transmit DMA fetches the packet from the host memory for transmission at designated time. This helps the software to setup the Transmit descriptors in advance even before packet is ready/available. It reduces the overhead on the software and avoids constant monitoring of the time and preparing descriptors just in time when the packet is targeted to be transmitted. 

- The MAC transmits the packet only at the designated/pre-determined time even if the packets are fetched in advance. This helps in maintaining a constant transmission rate that can be consumed by the receiver station; therefore avoiding congestion and excessive buffering in the network. 

The time-based scheduling feature supports fetching and launching an Ethernet packet at (or after) a pre-determined time. The time-based scheduling is supported only in the following modes/configurations: 

- Full duplex mode 

- Link speed is 100Mbps or higher 

The following figure shows the time-based scheduling flow. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4150-08.png)


<!-- Start of picture text -->
Fetch the first enhanced normal descriptor<br>If LTV = 1, compute fetch time based on<br>launch time<br>If LTV = 1, wait for system time ≥<br>fetch time<br>Read packet data from system memory<br>and push the data into the MTL FIFO<br>Close the descriptor<br>No<br>LD = 1 ? Fetch the next transmit descriptor<br>Yes<br>End of descriptor<br>ring<br>Wait for transmit poll demand<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4150-09.png)


<!-- Start of picture text -->
Figure 449. Time-Based Scheduling Flow<br><!-- End of picture text -->

Following are the definitions specific to the time-based scheduling feature: 

### 75.12.14.1 Launch time 

The time beyond which MTL can schedule the packet for transmission. The launch time resets after the transmission of one frame. These are the two formats of the launch time. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4150 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Normal or absolute format : 

In this format, the launch time is interpreted in the normal or absolute format if the ESTM bit of the MTL_TBS_CTRL register is set to 0. 

The launch time is a 32-bit value, where most-significant 8-bits represent the time in seconds and the rest 24-bits represent the time in 256 ns. The launch time is compared against the IEEE 1588 based system or PTP time (bits[39:8]) and rolls over after 256 seconds. 

The maximum value of the lower 32-bits of system time is 999,999,999 decimal (0x3B9AC9FF) and it wraps to 0 when reaching this value (representing a full second). Therefore, the maximum value of the lower 24-bits of the launch time (after multiplying by 256) must be 0x3B9AC9. 

As the maximum value of launch time is 256 seconds, 

- Launch time is greater than current system time when its value is between system time[39:8] and System time[39:8] + 128 sec. 

- Launch time is less than current system time when its value is between System Time[39:8] + 128sec and System Time[39:8] + 256 sec, because this is a modulo 256 computation. 

#### EST or offset format 

In this format, the launch time is a offset value relative to the time which the BTR of the GCL list provided in the GCL slot number (GSN) indicates. The value in the BTR is always updated to the start time of the current loop of the GCL. 

For each packet, the GSN value and the launch time value are specified in the enhanced transmit descriptor in the DMA configurations, or as control word in the MTL configurations. 

The launch time offset is a 32-bit value; the upper 8-bits represent the time in seconds and the rest 24 bits represent the time in 256 ns, which is added to the BTR value corresponding to GCL slot number. The value of the launch time offset must be smaller than the value of the cycle time (specified in the CTR register that is implemented when EST is enabled). If the CTR is greater than or equal to 1s, the maximum value of the lower-24 bits of launch time offset must be 999,999,999 decimal (0x3B9AC9FF). 

In this format, the launch time is a 64-bit value, which is interpreted as, Launch time = Launch GSN BTR[63:0] + (Launch time offset[31:0] << 8), which is compared with the system time [63:0]. 

GSN BTR is the Base Time value at which the Launch GSN loop started execution. 

GCL slot number (GSN) A modulo 16 count of the GCL loop count is implemented and it is known as GSN. The count is incremented for every new GCL loop. Installation of new GCL list does not impact the count. Read MTL_EST_Status[CGSN] to obtain the current GCL slot number. 

The maximum value of GSN is 15. Therefore the GSN values between MTL_EST_Status[CGSN] and MTL_EST_Status[CGSN]+8 represent current or future slots and all other GSN values are interpreted as elapsed slots or past slots. So, for the correct interpretation of time, GSN value must be between MTL_EST_Status[CGSN] and MTL_EST_Status[CGSN]+8. 

### 75.12.14.2 Launch expiry time 

#### Normal or Absolute Mode 

In this mode, when MTL_TBS_CTRL[LEOV] = 1, MTL_TBS_CTRL[LEOS] determines the maximum amount of time a frame is eligible for launch, starting from the time the frame becomes eligible for launch. 

The launch expiry offset is a 24-bit value defined in 256 ns units, with a maximum possible value of 999,999,999 ns (0x3B9AC9FF). 

Launch expiry time = (Launch time[39:8] + LEOS[32:8]) * 256 ns 

The packet with a specific launch time is considered as eligible for transmission when the launch time is less than the system time and (if MTL_TBS_CTRL[LEOV] = 1) the system time is less than the launch expiry time. 

When the system time is greater than the launch expiry time, the frame is categorized as expired and it drops from the MTL FIFO. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4151 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

~~<mark>NOTE</mark>~~ 

- For correct interpretation and meaningful operation, the fetch, launch, and launch expiry time must never set to a value larger than the Current system time + 128 sec; such a value is interpreted as time that has already elapsed. 

- In Full Duplex mode, the frames dropped from the MTL FIFO have error summary (Bit 15) and excessive deferral (bit 3) of TxStatus set. 

#### EST/Offset Mode 

In EST mode, when MTL_TBS_CTRL[LEOV] = 1, MTL_TBS_CTRL[LEGOS] and MTL_TBS_CTRL[LEOS] determines the maximum amount of time a frame remains eligible for launch, starting from the time the frame becomes eligible for launch. 

Launch Expiry Offset = (LEGOS: LEOS) 

LEGOS holds the GSN offset (multiples of CTR time) and LEOS holds maximum value of CTR (sub CTR values) in ns. 

Launch expiry offset is a 24-bit value defined in the units of 256 ns, with a maximum possible value of the smaller of 999,999,999 ns or CTR-1 ns. 

The Launch expiry GSN is computed as follows: 

Launch expiry GSN = (Launch GSN + LEGOS + CCMA) where, CCMA is the CTR carry due to modulo addition. This value is 1 if ((Launch time offset + LEOS) << 8) is equal to or greater than CTR. 

When CCMA = 1, Launch expiry offset = (Launch time offset+ LEOS) - CTR 

#### When CCMA = 0, 

Launch expiry offset = (Launch time offset + LEOS). 

Launch expiry time = Launch expiry GSN BTR [63:0] + Launch expiry time offset. 

When MTL_TBS_CTRL[LEOV] is not 1, the launch expiry time is not checked. 

When MTL_TBS_CTRL[LEOV] = 1, and 

- the system time is greater than the launch expiry time, the frame drops from MTL FIFO. Then the frame is considered as expired. 

- the launch time is smaller than the system time and the launch expiry time is greater than the system time, then the frame is considered eligible for launch. 

      - ~~<mark>NOTE</mark>~~ 

   - Max value of MTL_TBS_CTRL[LEGOS] is 7. This indicates that when MTL_TBS_CTRL[LEOV] = 1, the frame has a maximum life time of <8 GCL loop iterations after it becomes eligible for launch. 

   - The slot number of the first GCL list that executes each time after EST is enabled, is zero. 

### 75.12.14.3 Fetch time 

This accounts for all possible delays in the DMA fetch operation and ensures that the frame is present in the MTL FIFO before the launch time. 

If DMA_TBS_CTRL[FTOV] is 1, it indicates the fetch time for each packet. If DMA_TBS_CTRL[FTOV] is not 1, it indicates that the fetch time offset is not valid and DMA fetches packets without any time constraints. 

#### Normal/Absolute mode 

In this mode fetch time is derived or calculated by reducing the time specified in DMA_TBS_CTRL[FTOS] from the given launch time. 

In Normal mode, the fetch launch time is computed as: 

Fetch Time[39:8] = (Launch Time[39:8] - FTOS[31:8]) 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4152 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

The fetch time is 32-bits and is compared against the system time[39:8] to determine whether it is eligible for fetching the frame: 

- The fetch time is defined as greater than system time if the fetch time is in the range of system time[39:8]" and system time[39:8] + 128 sec. The frame is considered as not-eligible for fetch. 

- The fetch time is defined as smaller than the system time if the fetch time is in the range of system time[39:8] + 128 sec and system time[39:8] + 256 sec. The frame is considered as eligible for fetch. 

This is a modulo 256 computation. 

#### EST/Offset mode 

In this mode, the fetch GSN offset (DMA_TBS_CTRL[FGOS]) provides the slot number offset to deduct from the launch GSN. In this case the FTOS value must be smaller than 999,999,999 ns or CTR-1 ns. 

If (Launch time offset >= FTOS): 

Fetch time offset = ((Launch time offset - FTOS) * 256ns) 

CBFS(CTR borrow for fetch subtraction) = 0 

If (Launch time offset < FTOS) Fetch time offset = CTR + ((Launch time offset - FTOS) * 256ns) 

CBFS (CTR borrow for fetch subtraction) = 1 

The fetch GSN is computed as follows: 

Fetch GSN = Launch GSN - FGOS - CBFS 

Fetch time = Fetch GSN BTR[63:0] + Fetch time offset 

The frame is eligible for DMA fetch when the fetch time is smaller than the system time. 

#### DMA operations sequence 

This is the sequence of operation when FTOV = 1: 

1. Fetch the first enhanced normal descriptor (FD = 1). 

2. Compute the fetch time on the basis of the launch time and wait for the system time to be greater than fetch time, if LTV = 1 and fetch is enabled. 

3. Read the frame (data) from the host memory and transfer to MTL FIFO. 

4. Close the normal descriptor. 

5. Fetch the next normal descriptor (if the previous descriptor was not the last). 

6. Repeat steps 4 to 6, until the last descriptor of the frame (LD = 1). 

After the last descriptor of a frame, program the next enhanced normal descriptor with a new launch time and with LTV = 1. Otherwise, process the subsequent frames without any time restrictions. 

See Programming the launch time in time-based scheduling for more information. 

# 75.13 TCP/IP Offloading Features 

This section and all other sections, along with respective sub-sections are Synopsys Proprietary. Used with permission. 

## 75.13.1 Transmit Checksum Offload Engine 

The MAC has a Checksum Offload Engine (COE) to support checksum calculation and insertion in the Transmit path, using which, the software can offload the task of checksum insertion to the hardware. In the transmit path MAC calculates the checksum and inserts it in the Tx packet. This feature helps in reducing the load on the software and can improve the overall throughput of the system. This feature is supported for only Q0 queue. 

The checksum offload engine module supports two types of checksum calculation and insertion. The checksum engine can be controlled for each packet by setting the CIC bits (TDES3 Bits[17:16]). 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4153 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Note: The checksum for TCP, UDP, or ICMP is calculated over a complete packet, and then inserted into its corresponding header field. Because of this requirement, when this function is enabled, the Tx FIFO automatically operates in the store-and-forward mode even if IP is configured for Threshold (cut-through) mode. 

### 75.13.1.1 IP Header Checksum Engine 

In IPv4 datagrams, the integrity of the header fields is indicated by the 16-bit Header Checksum field (the eleventh and twelfth bytes of the IPv4 datagram). The COE detects an IPv4 datagram when the Type field of Ethernet packet has the value 0x0800 and the Version field of IP datagram has the value 0x4. The checksum field of the input packet is ignored during calculation and replaced with the calculated value. 

~~<mark>NOTE</mark>~~ 

IPv6 headers do not have a checksum field. Therefore, the COE does not modify the IPv6 header fields. 

The result of this IP header checksum calculation is indicated by the IP Header Error status bit in the Transmit status (Bit 0 in Table 19-12 on page 1330). This status bit is set whenever the values of the Ethernet Type field and the Version field of IP header are not consistent, or when the Ethernet packet does not have enough data, as indicated by the IP header Length field. In other words, this bit is set when an IP header error is asserted under the following circumstances: 

- For IPv4 datagrams: 

   - The received Ethernet type is 0x0800, but the Version field of IP header is not equal to 0x4. 

   - The IPv4 Header Length field indicates a value less than 0x5 (20 bytes). 

   - The total packet length is less than the value given in the IPv4 Header Length field. 

- For IPv6 datagrams: 

   - The Ethernet type is 0x86dd but the IP header Version field is not equal to 0x6. 

   - The packet ends before the IPv6 header (40 bytes) or extension header (as given in the corre-sponding Header Length field in an extension header) is completely received. 

### 75.13.1.2 TCP/UDP/ICMP Checksum Engine 

The TCP/UDP/ICMP Checksum Engine processes the IPv4 or IPv6 header (including extension headers) and determines whether the encapsulated payload is TCP, UDP, or ICMP. The checksum is calculated for the TCP, UDP, or ICMP payload and inserted into its corresponding field in the header. The Tx COE can work in the following two modes: 

- The TCP, UDP, or ICMPv6 pseudo-header is not included in the checksum calculation and is assumed to be present in the Checksum field of the input packet. This engine includes the Checksum field in the checksum calculation, and then replaces the Checksum field with the final calculated checksum. 

- The engine ignores the Checksum field, includes the TCP, UDP, or ICMPv6 pseudo-header data into the checksum calculation, and overwrites the checksum field with the final calculated value. 

~~<mark>NOTE</mark>~~ 

For ICMP-over-IPv4 packets, the Checksum field in the ICMP packet must always be 16'h0000 in both modes, because pseudo-headers are not defined for such packets. If it does not equal 16’h0000, an incorrect checksum may be inserted into the packet. 

The result of this operation is indicated by the Payload Checksum Error status bit in the Transmit Status vector (Bit 12 in Table 19-3 on page 1324). This engine sets the Payload Checksum Error status bit when it detects that the packet has been forwarded to the MAC Transmitter engine in the store-and-forward mode without the end of packet (EOP) being written to the FIFO, or when the packet ends before the number of bytes indicated by the Payload Length field in the IP Header is received. When the packet is longer than the indicated payload length, the COE ignores them as stuff bytes, and no error is reported. When this engine detects the first type of error, it does not modify the TCP, UDP, or ICMP header. For the second error type, it still inserts the calculated checksum into the corresponding header field. Following table describes the functions supported by Transmit Checksum Offload engine based on the packet type. When the MAC does not insert the checksum, it is indicated as "No" in the table. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4154 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

##### ~~<mark>NOTE</mark>~~ 

You should not enable checksum insertion for IPv4 or IPv6 packets that are greater than the frame size constraint specified in Description of Transmit Checksum Offload Engine because it may result in incorrect checksum insertion or unexpected behavior. 

Table 590. Transmit Checksum Offload Engine Functions for Different Packet Types 

|Packet Type|Hardware IP<br>headerchecksum insertion|Hardware TCP/<br>UDPchecksum insertion|
|---|---|---|
|Non-IPv4 or IPv6 packet|No|No|
|IPv4 packet is greater than 1,522 bytes (2,000 bytes when<br>IEEE 802.3ad Support for 2K Packets is enabled in MAC) but<br>less than or equal to the frame size constraint specified in<br>Transmit Checksum Offload Engine.|Yes|Yes|
|IPv6 packet is greater than 1,522 bytes (2,000 bytes when<br>IEEE 802.3ad Support for 2K Packets is enabled in MAC) but<br>less than or equal to the frame size constraint specified in<br>Transmit Checksum Offload Engine.|Not Applicable|Yes|
|IPv4 with TCP, UDP, or ICMP|Yes|Yes|
|IPv4 packet has IP options (IP header is longer than 20 bytes)|Yes|Yes|
|Packet is an IPv4 fragment|Yes|No|
|IPv6 packet with the following next header fields in main or<br>extension headers:<br>• Hop-by-hop options (in IPv6 main header)<br>• Hop-by-hop options (in IPv6 extension header)<br>• Destinations options<br>• Routing (with segment left 0)<br>• Routing (with segment left > 0)<br>• TCP, UDP, or ICMP<br>• Authentication<br>• Any other next header field in main or extension headers|• Not Applicable<br>• Not Applicable<br>• Not Applicable<br>• Not Applicable<br>• Not Applicable<br>• Not Applicable<br>• Not Applicable<br>• Not Applicable|• Yes<br>• No<br>• Yes<br>• No<br>• No<br>• Yes<br>• No<br>• No|
|IPv4 packet has TCP header with Options fields|Yes|Yes|
|IPv4 Tunnels:<br>• IPv4 packet in an IPv4 tunnel<br>• IPv6 packet in an IPv4 tunnel|• Yes (IPv4 tunnel header)<br>• Yes (IPv4 tunnel header)|• No<br>• No|
|IPv6 Tunnels:<br>• IPv4 packet in an IPv6 tunnel<br>• IPv6 packet in an IPv6 tunnel|• Not applicable<br>• Not applicable|• No<br>• No|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4155 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 590. Transmit Checksum Offload Engine Functions for Different Packet Types (continued) 

|Packet Type|Hardware IP<br>headerchecksum insertion|Hardware TCP/<br>UDPchecksum insertion|
|---|---|---|
|IPv4 packet has 802.3ac tag (with C-VLAN Tag or S-VLAN Tag<br>when enabled).|Yes|Yes|
|IPv6 packet has 802.3ac tag (with C-VLAN Tag or S-VLAN Tag<br>when enabled).|Not applicable|Yes|
|IPv4 frames with security features (such as encapsulated<br>security payload)|Yes|No|
|IPv6 frames with security features (such as encapsulated<br>security payload)|Not applicable|No|



## 75.13.2 Receive Checksum Offload Engine 

IP provides the Checksum Offload Engine that is used to detect any error in an IPv4 or IPv6 packet in the receive path. The MAC verifies the checksum field of the received packet with the internally calculated checksum and provides the status. 

The Receive Checksum Offload engine is used to detect errors in IP packets by calculating the header checksum and further matching it with the received header checksum. This engine also identifies a TCP, UDP, or ICMP payload in received IP packets and calculates the checksum of such payloads appropriately. 

Here, both IPv4 and IPv6 packet in the received Ethernet packets are detected and processed for data integrity. The MAC receiver identifies IPv4 or IPv6 packets by checking for value 0x0800 or 0x86DD, respectively, in the Type field of the received Ethernet packet. This identification is applicable to single VLAN-tagged packets. It is also applicable to double VLAN-tagged packets when the Enable Double VLAN Processing option is selected and the EDVLP bit of the MAC_VLAN_Tag register is set. 

The Rx COE calculates the IPv4 header checksums and checks that they match the received IPv4 header checksums. The result of this operation (pass or fail) is given to the RFC module for insertion into the receive status word. The IP Header Error bit is set for any mismatch between the indicated payload type (Ethernet Type field) and the IP header version, or when the received packet does not have enough bytes, as indicated by the Length field of the IPv4 header (or when fewer than 20 bytes are available in an IPv4 or IPv6 header). 

This engine also identifies a TCP, UDP, or ICMP payload in the received IP datagrams (IPv4 or IPv6) and calculates the checksum of such payloads properly, as defined in the TCP, UDP, or ICMP specifications. This engine includes the TCP, UDP, or ICMPv6 pseudo-header bytes for checksum calculation and checks whether the received checksum field matches the calculated value. The result of this operation is given as a Payload Checksum Error bit in the receive status word. This status bit is also set if the length of the TCP, UDP, or ICMP payload does not match the expected payload length given in the IP header. 

Following table describes the functions supported by the Rx COE based on the packet type. When the payload of an IP packet is not processed (indicated as "No" in the table), the information (whether the checksum engine is bypassed or not) is given in the receive status. 

~~<mark>NOTE</mark>~~ The MAC does not append any payload checksum bytes to the received Ethernet packets. 

Table 591. Receive Checksum Offload Engine Functions for Different Packet Types 

|||Hardware TCP/UDP/ICMP|
|---|---|---|
|Packet type|Hardware IP header checksum checking|checksum checking|
|Non-IPv4 or IPv6|No|No|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4156 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 591. Receive Checksum Offload Engine Functions for Different Packet Types (continued) 

|Packet type|Hardware IP header checksum checking|Hardware TCP/UDP/ICMP<br>checksum checking|
|---|---|---|
|IPv4 packet is greater than 1,522<br>bytes (2,000 bytes when IEEE<br>802.3ad Support for 2K Packets is<br>enabled in the MAC)|Yes|Yes|
|IPv6 packet is greater than 1,522<br>bytes (2,000 bytes when IEEE<br>802.3ad Support for 2K Packets is<br>enabled in the MAC)|Not Applicable|Yes|
|IPv4 with TCP, UDP, or ICMP|Yes|Yes|
|IPv4 header's protocol field contains<br>a protocol other than TCP, UDP,<br>or ICMP|Yes|No|
|IPv4 packet has IP options (IP header<br>is longer than 20 bytes)|Yes|Yes|
|Packet is an IPv4 fragment|Yes|No|
|IPv6 packet with the following<br>next header fields in main or<br>extension headers:<br>• Hop-by-hop options (in IPv6<br>main header)|• Not Applicable<br>• Not Applicable<br>• Not Applicable<br>• Not Applicable|• Yes<br>• No<br>• Yes<br>• Yes|
|• Hop-by-hop options (in IPv6<br>extension header)|• Not Applicable<br>• Not Applicable|• No<br>• Yes|
|• Destinations options<br>• Routing (with segment left 0)<br>• Routing (with segment left > 0)<br>• TCP, UDP, or ICMP<br>• Any other next header field in<br>main or extension headers|• Not Applicable|• No|
|IPv4 packet has TCP header with<br>Options fields|Yes|Yes|
|IPv4 Tunnels:<br>• IPv4 packet in an IPv4 tunnel<br>• IPv6 packet in an IPv4 tunnel|• Yes (IPv4 tunnel header)<br>• Yes (IPv4 tunnel header)|• No<br>• No|
|IPv4 Tunnels:|• Not Applicable<br>• Not Applicable|• No<br>• No|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4157 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 591. Receive Checksum Offload Engine Functions for Different Packet Types (continued) 

|Packet type|Hardware IP header checksum checking|Hardware TCP/UDP/ICMP<br>checksum checking|
|---|---|---|
|• IPv4 packet in an IPv6 tunnel<br>• IPv6 packet in an IPv6 tunnel|||
|IPv4 packet has 802.3ac tag (with<br>C-VLAN Tag or S-VLAN Tag<br>when enabled)|Yes|Yes|
|IPv6 packet has 802.3ac tag (with<br>C-VLAN Tag or S-VLAN Tag<br>when enabled)|Not Applicable|Yes|
|IPv4 frames with security<br>features (such as encapsulated<br>security payload)|Yes|No|
|IPv6 frames with security<br>features (such as encapsulated<br>security payload)|Not Applicable|No|



Set the IPC bit of the MAC_Configuration register for enabling Receive Checksum offload. 

## 75.13.3 Header payload split 

MAC is capable of identifying the boundary between header and payload of the received packet and store them into separate buffers. The MAC supports multiple methods and packet types for header-payload splitting. This is controlled by the setting the SPLM field in MAC_Ext1_cfg register. 

## 75.13.4 IPv4 ARP offload engine 

MAC supports the Address Recognition Protocol (ARP) Offload for IPv4 packets. This feature allows the processing of the IPv4 ARP request packet in the receive path and generating corresponding ARP response packet in the transmit path. MAC generates the ARP reply packets for appropriate ARP request packets. The ARP packet for IPv4 is L2 layer packet with Length/Type of 0x0806. 

~~<mark>NOTE</mark>~~ 

When the received ARP request is less than 64 bytes packet length, MAC does not send a ARP response. It is treated as normal packet and forwarded to the application based on the MAC filter settings. 

# 75.14 MAC Management Counters 

This section is Synopsys Proprietary. Used with permission. 

IP supports storing the statistics about the received and transmitted packets in registers that are accessible through the application/software. The MMC module maintains a set of registers for gathering statistics on the received and transmitted packets. The MMC counters are free running. 

For MMC register details, see registers "MMC_Control" to "MMC_Rx_FPE_Fragment_Cntr" in GMAC register descriptions. 

# 75.15 Flow Control 

This section and its sub-sections are Synopsys Proprietary. Used with permission. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4158 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## 75.15.1 Transmit Flow Control 

The Transmit Flow Control involves transmitting Pause packets in full-duplex mode and backpressure in half-duplex mode to control the flow of packets from the remote end. 

### 75.15.1.1 Flow control in Full duplex mode 

IP supports the IEEE802.3x Pause Packets. 

Pause packet structure is shown in the following table. 

Table 592. Pause Packet Fields 

|Field|Description|
|---|---|
|DA|Contains the special multicast address|
|SA|Contains the MAC address 0|
|Type|Contains 8808|
|MAC Control opcode|Contains 0001 for IEEE 802.3x Pause Control packets; 0101 for PFC packets|
|PT|Contains Pause time specified in the PT field of the MAC_Q#_Tx_Flow_Ctrl register|



### 75.15.1.2 Pause Packet Control 

When the FCB bit is set, the MAC generates and transmits a single Pause packet. If the FCB bit is set again after the Pause packet transmission is complete, the MAC sends another Pause packet irrespective of whether the pause time is complete or not. To extend the pause or terminate the pause prior to the time specified in the previously-transmitted Pause packet, the application should program the Pause Time register with appropriate value and then again set the FCB bit. 

### 75.15.1.3 Flow Control in Half-Duplex Mode 

In half-duplex mode, the MAC uses the deferral mechanism for the flow control (backpressure). When the application requests to stop receiving packets, the MAC sends a JAM pattern of 32 bytes when it senses a packet reception, provided the transmit flow control is enabled. This results in a collision and the remote station backs off. If the application requests a packet to be transmitted, it is scheduled and transmitted even when the backpressure is activated. If the backpressure is kept activated for a long time (and more than 16 consecutive collision events occur), the remote stations abort the transmission because of excessive collisions. 

Following table describes the flow control in the Tx path for Queue 0 based on the setting of the following bits: 

- EHFC bit of MTL_RxQ0_Operation_Mode register 

- TFE bit of MAC_Q0_Tx_Flow_Ctrl register 

- DM bit of MAC_Configuration register 

Flow control is similar for all queues. 

Table 593. Tx MAC Flow Control 

|EHF<br>C|TFE|DM|Description|
|---|---|---|---|
|x|0|x|The MAC transmitter does not perform the flow control or backpressure operation.|
|0|1|0|The MAC transmitter performs back-pressure when Bit 0 of MAC_Q0_Tx_Flow_Ctrl register is set or the<br>sideband signal sbd_flowctrl_i is 1.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4159 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Table 593. Tx MAC Flow Control (continued) 

|EHF<br>C|TFE|DM|Description|
|---|---|---|---|
|1|1|0|The MAC transmitter performs back-pressure when Bit 0 of MAC_Q0_Tx_Flow_Ctrl register is set or the<br>sideband signal sbd_flowctrl_i is 1. In addition, the MAC Tx performs back-pressure when Rx Queue level<br>crosses the threshold set by Bits[10:8] of MTL_RxQ0_Operation_Mode register.|
|0|1|1|The MAC transmitter sends the Pause packet when Bit 0 of MAC_Q0_Tx_Flow_Ctrl register is set or the<br>sideband signal sbd_flowctrl_i is 1.|
|1|1|1|The MAC transmitter sends the Pause packet when Bit 0 of MAC_Q0_Tx_Flow_Ctrl register is set or the<br>sideband signal sbd_flowctrl_i is 1. In addition, the MAC Tx sends a Pause packet when Rx Queue level<br>crosses the threshold set by Bits[10:8] of MTL_RxQ0_Operation_Mode register.|



### 75.15.1.4 Enabling Transmit Flow Control 

To independently enable Transmit Flow Control for each Tx queue, set the TFE bit in the MAC_Q#_Tx_Flow_Ctrl register. 

## 75.15.2 Receive Flow Control 

In the Receive path, the Flow Control is functional only in the full-duplex mode. If any Pause packet is received in the half-duplex mode, the packet is considered as a normal control packet. 

~~<mark>NOTE</mark>~~ Receive pause packets should have a frame size of 64 bytes. 

The Receive Flow Control is implemented by the MAC based on the bit value of the respective register, and the destination address and different fields of the received packet. 

Following table describes the flow control in the Rx path based on the setting of the following bits: 

- RFE bit of MAC_Rx_Flow_Ctrl register 

- DM bit of MAC_Configuration register 

Table 594. Rx MAC Flow Control 

|RFE|DM|Description|
|---|---|---|
|0|x|The MAC receiver does not detect the received Pause packets.|
|1|0|The MAC receiver does not detect the received Pause packets but recognizes such packets as<br>Control packets.|
|1|1|The MAC receiver detects or processes the Pause packets and responds to such packets by stopping the<br>MAC transmitter.|



### 75.15.2.1 Enabling Receive Flow Control 

To enable Pause Flow Control, set the RFE bit in the MAC_Rx_Flow_Ctrl register. 

# 75.16 Loopback Mode 

This section is Synopsys Proprietary. Used with permission. 

The MAC supports Loopback of transmitted packets to its receiver. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4160 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

The following are some guidelines for using the loopback mode: 

- Enable loopback only with the full-duplex mode. In half-duplex mode, the carrier sense signal (crs) or collision (col) signal inputs get sampled which may result into issues such as packet dropping. 

- If the loopback mode is enabled without connecting a PHY chip (for example, in FPGA setup), you should externally generate the Tx and Rx clocks and provide these clocks to the MAC. 

- Do not loop back big packets. Big packets (>1522 bytes) may get corrupted in the loopback FIFO. 

To enable this feature, program the LM bit of the MAC_Configuration register. 

You can enable loopback for all PHY interfaces. The data is always looped back through internal asynchronous FIFO on to the internal Receive MII or GMII interface, irrespective of which PHY interface is selected. The loopback data is also passed through the corresponding transmit PHY interface block, on to the Ethernet line. 

# 75.17 Automotive Safety Features 

This section and all its sub-sections are Synopsys Proprietary. Used with permission. 

IP supports the automotive safety feature. 

## 75.17.1 Error Correction Code (ECC) Protection for Memories 

The Error Correction Code (ECC) block can correct single-bit error and detect double-bit error. 

At the write interface, ECC checkbits are generated by computing ECC on the contents of the data bus and respective address is appended with the data that is written to the memory. 

At the read interface, ECC checkbits are recomputed on the content of the read data and the respective address is compared with the received checkbits in the memory. 

Following figure shows the block diagram of ECC protection for memories 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4161-16.png)


<!-- Start of picture text -->
Module single-port SRAMs<br>Write Read<br>interface interface<br>ECC check bits ECC error<br>generation detection/correction<br>GMAC<br><!-- End of picture text -->

Figure 450. Block Diagram of ECC Protection for Memories 

### 75.17.1.1 Handling the Address Mismatch 

The ECC is calculated over the sum of memory data and memory location address. However only data is written in the memory along with the ECC(address is excluded). 

On the read interface, the ECC is checked over the sum of memory DATA, memory ECC, and Internally generated address. When an ECC correctable error is detected over the range of the address bit position, it is treated as an uncorrectable error. This is because data might have been read from a different location. 

### 75.17.1.2 Diagnostic Support for the Error Management 

Following statistics are provided for monitoring the error behavior on each of the memory blocks. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4161 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

- Error status provided to management 

   - A separate status for correctable, uncorrectable, and address mismatch is specified in the MTL_ECC_Interrupt_Status register. 

   - Memory locations at which correctable and uncorrectable errors are detected is specified in the MTL_ECC_Err_Addr_Status register. In addition, a control bit (MEEAO field of MTL_ECC_Control register) decides, whether the first errored memory address is reported or the latest errored memory address is reported. 

   - MTL_ECC_Err_Cntr_Status register has separate counters to count the number of correctable and uncorrectable errors 

- Interrupts provided to management 

   - Separate interrupts are generated for correctable and uncorrectable errors. 

   - sbd_sfty_ue_intr_o interrupt is generated when uncorrectable errors are detected and these errors cannot be masked. 

   - sbd_sfty_ce_intr_o interrupt is generated when correctable errors are detected. The module sets the respective interrupt enable bits (in the DMA/MTL_ECC_Interrupt_enable register). 

   - To find the root cause of the error, read the DMA/MTL_Safety_Interrupt_Status and DMA/MTL_ECC_Interrupt_Status registers. 

   - To clear the interrupt, write 1 in the respective interrupt status bit in DMA/MTL_ECC_Inter-rupt_Status registers. 

         - ~~<mark>NOTE</mark>~~ 

      - The status/counters/interrupts are generated per memory. 

      - MTL Tx and Rx memory is logically divided into multiple queues. But, ECC diagnostics (status/counter/ interrupts) are common to all queues. 

### 75.17.1.3 ECC Error Injection Capabilities 

IP supports error injection capabilities for each memory as a static configuration. The position where the errors are injected in the data word is random. For each memory, 3 control bits are provided to inject errors. The 3 bits are: 

- A single bit to enable error injection 

- Two bits to indicate the type of error to be injected ❑ 00: 1 bit error 

   - 01: 2 bit error 

   - 10: 3 bit error 

   - 11: 1 bit error in address field 

The control bit descriptions for 

- MTL Tx/Rx and DMA TSO memory are specified in the MTL_DBG_CTL register, for and for R. 

- MTL EST memory are specified in the MTL_EST_GCL_Control register 

- Rx parser memory are specified in the MTL_RXP_Indirect_Acc_Control_Status register 

~~<mark>NOTE</mark>~~ 

While using debug mode for ECC error injection: 

- There should be no traffic in the module 

- When multiple CSR writes are required for writing single data word into the memory, the application should ensure that all the CSR writes corresponding to one memory write main-tains the same value for the error injection control word. 

- See Programming guidelines for ECC protection for memories 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4162 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## 75.17.2 Finite State Machine(FSM) Parity and Timeout Protection 

The FSM protection feature supports FSM parity and time out protection. 

### 75.17.2.1 FSM State Parity Protection 

Odd parity is implemented on all the FSM state register bits. Parity is monitored for every clock, after the reset is de-asserted. When a bit flips due to transient errors or permanent faults, the erroneous FSM is set to its default state and an uncorrectable error is indicated. 

When the FSM state parity protection is enabled, by setting PRTYEN field of MAC_FSM_Control Register, the FSM state error is indicated by setting the FSMPES field of the MAC_DPP_FSM_Interrupt_Status register. Also, the Safety Interrupt (sbd_sfty_ue_intr_o) is asserted when an FSM Error is detected. 

Error Injection mode is also supported for FSM parity error check. Program the Error Injection enable for the respective clock domain denoted by [23:16] bits of MAC_FSM_Control Register. 

### 75.17.2.2 FSM Timeout Protection 

The FSM Timeout feature provides a mechanism to ensure that all FSMs in the module can complete a transaction and return to a known completion state (IDLE or any other state that indicates completion of a transaction/transfer) within the programmed timeout value. 

Program the TMR field of MAC_FSM_ACT_Timer register with a value that indicates the number of CSR cycles required to generate a 1 microsecond tic. This microsecond tic is internally used to generate the programmed timeout duration. Two timeout tics (normal mode timeout and large mode timeouts) are generated to provide flexibility to choose one per clock domain, by using the bits [31:24] of MAC_FSM_Control Register. Supported values for Timeout duration are 1us, 1.024ms, 16.384ms, 65.5536ms, 262.144ms, 1048.576ms (~1sec), 4194.304ms (~4s), 8.388s, 16.777s, and 33.554s which is based on the programmable bits NTMRMD, LTMRMD fields of MAC_FSM_ACT_Timer register. Interface timeouts are based on the normal mode tic generation; only the FSM timeouts depend on either normal or large tick selection. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4163-11.png)


#### Figure 451. FSM Timeout Timing Diagram 

In the above figure, the timer ticks are generated based on the programmable timeout value. The timer ticks are synchronized and made available in all the clock domains that have the FSMs. 

At every timer tick, all the FSMs are monitored for being in active state (non-IDLE state, which indicates the FSM is actively processing transactions or hand-shakes) and an FSM active flag bit is set. The active flag bit is implemented for every FSM that is monitored for timeout. When the FSM reaches an IDLE or transaction completion state, the active flag bit of that FSM is reset. At the subsequent timer tick, all the FSMs’ active flag bits are monitored and any flag that is set indicates a timeout for that FSM. This process of setting the flag and checking at subsequent timer tick is repeated at every tick. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4163 / 4640 

NXP Semiconductors 

##### Gigabit Ethernet Media Access Controller (GMAC) 

Timeout Error Injection per clock domain is enabled by programming [15:8] fields of MAC_FSM_Control register. When Timeout error injection enable is set for a clock domain, the FSMs in that clock domain automatically timeout and generate an interrupt even without traffic. As error injection is a debug mode, TMR value need not indicate 1us, but can be programmed to a smaller value at which debug mode ticks are needed. FSM Timeout and Parity Error Injection modes can be used for testing at key-on/key-off. 

The FSM timeout status is specified in the [15:8] field of MAC_DPP_FSM_Interrupt_Status register as per the respective clock domains. One FSM timeout status bit is made available per clock domain. The safety interrupt (sbd_sfty_ue_intr_o) is asserted when the timeout error is set for any of the clock domains. IP does not attempt to recover from a FSM timeout condition and relies on the application to take the corrective action (resetting IP). 

### 75.17.2.3 Enabling FSM Parity and Timeout Protection 

FSM timeout feature is enabled by setting the TMOUTEN field of MAC_FSM_Control register. 

~~<mark>NOTE</mark>~~ 

See Programming guidelines for FSM parity and timeout 

## 75.17.3 Application/CSR Interface Timeout Protection 

This feature provides timeout protection to the application/CSR Interface. All the interfaces which has the handshake mechanism monitored for potential hangs due to the external agent (Master/Slave/Interconnect/Application client) not responding to the requests/transfers initiated by the QoS. After the request is initiated the response arrival interval is monitored. If the response does not arrive within a programmed time (TMR field of MAC_FSM_ACT_Timer) the timeout is triggered, using similar trigger generation as explained in the Section FSM protection. 

The timeout is triggered when IP initiates SEQ, NON-SEQ and BUSY transfers on HTRANS[1:0]; and HREADY is not asserted by Slave within the programmed time. 

The Timeout status for the AHB master interface is set in the MSTTES field of the MAC_DPP_FSM_Interrupt_Status register. The Safety interrupt (sbd_sfty_ue_intr_o) is asserted when application timeout status is set. 

The hardware does not attempt to recover from Application/CSR Interface hangs and relies on software to take appropriate corrective action. 

~~<mark>NOTE</mark>~~ 

- Protection is not needed for APB3 Slave interfaces because potential hangs can be only when IP does not respond to the requests. In such cases the IP internal protection logic (FSM timeout) detects such defects. 

- Based on the time at which the transfer is initiated relative to the timer ticks, the timeout period could be any value between the programmed timeout and 2x times the programmed timeout. 

- When an uncorrectable safety interrupt is issued and the read of the Interrupt status register returns all zeros, it implies that the CSR read is not functional. As soft reset of IP is not possible without the CSR access, and therefore, a hard reset of IP is recommended. 

- See Programming guidelines for FSM parity and timeout . 

# 75.18 Descriptors 

This section and all its sub-sections are Synopsys Proprietary. Used with permission. 

## 75.18.1 Overview 

The DMA in the Ethernet subsystem transfers data based on a linked list of descriptors. The application creates the descriptors in the system memory. The module supports the following two types of descriptors: 

- Normal Descriptor: Normal descriptors are used for packet data and to provide control information applicable to the packets to be transmitted. 

- Context Descriptor: Context descriptors are used to provide control information applicable to the packet to be transmitted. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4164 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Each normal descriptor contains two buffers and two address pointers. These buffers enable the adapter port to be compatible with various types of memory management schemes. 

~~<mark>NOTE</mark>~~ 

There is no limit for the number of descriptors that can be used for a single packet. 

## 75.18.2 Descriptor Structure 

The module supports the ring structure for DMA descriptor as shown in the following figure. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4165-07.png)


<!-- Start of picture text -->
Ring structure<br>Buffer 1<br>Descriptor 0<br>Buffer 2<br>Buffer 1<br>Descriptor 1<br>Buffer 2<br>Buffer 1<br>Descriptor 2<br>Buffer 2<br>Buffer 1<br>Descriptor  n<br>Buffer 2<br><!-- End of picture text -->

Figure 452. Descriptor Ring Structure 

In Ring structure, descriptors are separated by the Word, DWord, or LWord number programmed in the DSL field of the DMA_CH#_Control register. The application needs to program the total ring length, that is, the total number of descriptors in ring span in the following registers of a DMA channel: 

- Transmit Descriptor Ring Length Register (DMA_CH#_TxDesc_Ring_Length) 

- Receive Descriptor Ring Length Register (DMA_CH#_RxDesc_Ring_Length) 

The Descriptor Tail Pointer Register contains the pointer to the descriptor address (N). The base address and the current descriptor pointer decide the address of the current descriptor that the DMA can process. The descriptors up to one location less than the one indicated by the descriptor tail pointer (N – 1) are owned by the DMA. The DMA continues to process the descriptors until the following condition occurs: 

#### Current Descriptor Pointer == Descriptor Tail Pointer; 

The DMA goes into the Suspend mode when this condition occurs. The application must perform a write to the Descriptor Tail pointer register and update the tail pointer so that the following condition is true: 

Current Descriptor Pointer < Descriptor Tail Pointer; 

The DMA automatically wraps around the base address when the end of ring is reached, as shown in the following figure. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4165 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4166-02.png)


<!-- Start of picture text -->
Descriptor base address<br>Current descriptor pointer<br>Last descriptor that DMA owns<br>Descriptor tail pointer<br>Application owns DMA owns<br>to start the ring<br>Descriptor ring length<br>(number of descriptors = 10)<br>Wrap around the base address<br><!-- End of picture text -->

#### Figure 453. DMA Descriptor Ring 

For descriptors owned by the application, the OWN bit of DES3 is reset to 0. For descriptors owned by the DMA, the OWN bit is set to 1. If the application has only one descriptor in the beginning, the application sets the last descriptor address (tail pointer) to Descriptor Base Address + 1. The DMA processes the first descriptor and then waits for the application to advance the tail pointer. 

## 75.18.3 Transmit Descriptor 

The DMA in the module requires at least one descriptor for a transmit packet. In addition to two buffers, two byte-count buffers, and two address pointers, the transmit descriptor has control fields which can be used to control the MAC operation on per-transmit packet basis. The Transmit Normal descriptor has two formats: Read format and Write-Back format 

~~<mark>NOTE</mark>~~ 

TSO Split header is not supported. 

Software must not write same tail pointer addresses when DMA is in Suspended state before setting new descriptor(s) for further processing. 

### 75.18.3.1 Transmit Normal Descriptor (Read Format) 

Following figure shows the Read Format for a Transmit normal descriptor. Table: 'TDES0 Normal Descriptor (Read Format)' through Table: 'TDES3 Normal Descriptor (Read Format)' describe the read format for the Transmit Normal Descriptors: TDES0, TDES1, TDES2, and TDES3. 

Figure 454. Transmit Descriptor Read Format 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4166 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4167-02.png)


<!-- Start of picture text -->
31 0<br>TDES0 Header or buffer 1 address [31:0]<br>TDES1 Buffer 2 address [31:0] or buffer 1 address [63:32]<br>T<br>I<br>T<br>TDES2 O Buffer 2 length [29:16] VTIR Header or buffer 1 length [13:0]<br>S<br>C<br>E<br>O Control [30:16] Frame length [14:0]<br>TDES3 W<br>N Control [30:18] Payload length [17:0]<br><!-- End of picture text -->

### 75.18.3.1.1 TDES0 Normal Descriptor (Read Format) 

Table 595. TDES0 Normal Descriptor (Read Format) 

|Bit|Name|Description|
|---|---|---|
|31:0|BUF1AP|Buffer 1 Address Pointer or TSO Header Address Pointer|
|||These bits indicate the physical address of Buffer 1. These bits indicate the TSO Header Address pointer<br>when the following bits are set:|
|||• TSE bit of TDES3<br>• FD bit of TDES3|



### 75.18.3.1.2 TDES1 Normal Descriptor (Read Format) 

Table 596. TDES1 Normal Descriptor (Read Format) 

|Bit|Name|Description|
|---|---|---|
|31:0|BUF2AP|Buffer 2 or Buffer 1 Address Pointer|
|||This bit indicates the physical address of Buffer 2 when a descriptor ring structure is used. There is no<br>limitation for the buffer address alignment.|
|||In 40- or 48-bit addressing mode, these bits indicate the most-significant 8- or 16- bits of the Buffer 1<br>Address Pointer.|



### 75.18.3.1.3 TDES2 Normal Descriptor (Read Format) 

Table 597. TDES2 Normal Descriptor (Read Format) 

|31|30|29-16|15:14|13:0|
|---|---|---|---|---|
|IOC|TTSE/ TMWD|B2L|VTIR|HL or B1L|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4167 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 598. TDES2 Normal Descriptor (Read Format) 

|Bits|Name|Description|
|---|---|---|
|31|IOC|Interrupt on Completion<br>This bit controls the setting of TI and ETI status bits in the DMA_CH#_Status register. When ETIC = 1 and<br>TDES2[LD] = 0, this bit sets the ETI bit. When TDES3[LD] = 1, this bit sets the TI status bit.|
|30|TTSE/<br>TMWD|Transmit Timestamp Enable or External TSO Memory Write Enable<br>This bit enables the IEEE1588 time stamping for Transmit packet referenced by the descriptor, if TSE bit is<br>not set.<br>If TSE bit is set and external TSO memory is enabled, setting this bit disables external TSO memory writing<br>for this packet.|
|29:16|B2L|Buffer 2 Length<br>The driver sets this field. When set, this field indicates Buffer 2 length.|
|15:14|VTIR|VLAN Tag Insertion or Replacement<br>These bits request the MAC to perform VLAN tagging or untagging before transmitting the packets. The<br>application must set the CRC Pad Control bits appropriately when VLAN Tag Insertion, Replacement, or<br>Deletion is enabled for the packet. The following list describes the values of these bits:<br>• 2'b00: Do not add a VLAN tag.<br>• 2'b01: Remove the VLAN tag from the packets before transmission. This option should be used only<br>with the VLAN packets.<br>• 2'b10: Insert a VLAN tag with the tag value programmed in the MAC_VLAN_Incl register or<br>context descriptor.<br>• 2'b11: Replace the VLAN tag in packets with the tag value programmed in the MAC_VLAN_Incl register<br>or context descriptor. This option should be used only with the VLAN packets.<br>These bits are valid when the Enable SA and VLAN Insertion on Tx option is selected while configuring<br>the core.|
|13:0|HL or<br>B1L|Header Length or Buffer 1 Length<br>For Header length only bits [9:0] are taken. The size 13:0 is applicable only when interpreting buffer 1 length.<br>If the TCP Segmentation Offload feature is enabled through the TSE bit of TDES3, this field is equal to<br>the header length. When the TSE bit is set in TDES3, the header length includes the length in bytes from<br>Ethernet Source address till the end of the TCP header. The maximum header length supported for TSO<br>feature is 1023 bytes. The maximum header length supported for TSO feature is 1023 bytes.<br>If the TCP Segmentation Offload feature is not enabled, this field is equal to Buffer 1 length.|



### 75.18.3.1.4 TDES3 Normal Descriptor (Read Format) 

Table 599. TDES2 Normal Descriptor (Read Format) 

|31|30|29|28|27:26|25:23|22:19|18|17:16|15|14:0|
|---|---|---|---|---|---|---|---|---|---|---|
|OWN|CTXT|FD|LD|CPC|SAIC|SLOTNUM or THL|TSE|CIC/TPL|TPL|FL/TPL|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4168 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 600. TDES3 Normal Descriptor (Read Format) 

|Bits|Name|Description|
|---|---|---|
|31|OWN|Own Bit<br>When this bit is set, it indicates that the DMA owns the descriptor. When this bit is reset, it indicates that<br>the application owns the descriptor. The DMA clears this bit after it completes the transfer of data given<br>in the associated buffer(s).|
|30|CTXT|Context Type<br>This bit should be set to 1'b0 for normal descriptor.|
|29|FD|First Descriptor<br>When this bit is set, it indicates that the buffer contains the first segment of a packet.|
|28|LD|Last Descriptor<br>When this bit is set, it indicates that the buffer contains the last segment of the packet. When this bit is<br>set, the B1L or B2L field should have a non-zero value.|
|27:26|CPC|CRC Pad Control<br>This field controls the CRC and Pad Insertion for Tx packet. This field is valid only when the first descriptor<br>bit (TDES3[29]) is set. The following list describes the values of Bits[27:26]:<br>• 2'b00: CRC and Pad Insertion<br>The MAC appends the cyclic redundancy check (CRC) at the end of the transmitted packet of length<br>greater than or equal to 60 bytes. The MAC automatically appends padding and CRC to a packet with<br>length less than 60 bytes.<br>• 2'b01: CRC Insertion (Disable Pad Insertion)<br>The MAC appends the CRC at the end of the transmitted packet but it does not append padding. The<br>application should ensure that the padding bytes are present in the packet being transferred from the<br>Transmit Buffer, that is, the packet being transferred from the Transmit Buffer is of length greater than or<br>equal to 60 bytes.<br>• 2'b10: Disable CRC Insertion<br>The MAC does not append the CRC at the end of the transmitted packet. The application should ensure<br>that the padding and CRC bytes are present in the packet being transferred from the Transmit Buffer.<br>• 2'b11: CRC Replacement<br>The MAC replaces the last four bytes of the transmitted packet with recalculated CRC bytes. The<br>application should ensure that the padding and CRC bytes are present in the packet being transferred<br>from the Transmit Buffer.<br>This field is valid only for the first descriptor.<br>Note: When the TSE bit is set, the MAC ignores this field because the CRC and pad insertion is always<br>done for segmentation.|
|25:23|SAIC|SA Insertion Control<br>These bits request the MAC to add or replace the Source Address field in the Ethernet packet with<br>the value given in the MAC Address 0 register. The application must set the CRC Pad Control bits<br>appropriately when SA Insertion Control is enabled for the packet.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4169 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 600. TDES3 Normal Descriptor (Read Format) (continued) 

|Bits|Name|Description|
|---|---|---|
|||Bit 25 specifies the MAC Address Register (1 or 0) value that is used for Source Address insertion<br>or replacement.<br>The following list describes the values of Bits[24:23]:<br>• 2'b00: Do not include the source address<br>• 2'b01: Include or insert the source address. For reliable transmission, the application must provide<br>frames without source addresses.<br>• 2'b10: Replace the source address. For reliable transmission, the application must provide frames<br>with source addresses.<br>• 2'b11: Reserved<br>These bits are valid in the EQOS-DMA, EQOS-AXI, and EQOS-AHB configurations when the Enable<br>SA and VLAN Insertion on Tx option is selected while configuring the core and when the First Segment<br>control bit (TDES3 [29]) is set.<br>This field is valid only for the first descriptor.|
|22:19|SLOTNUM<br>or THL|SLOTNUM: Slot Number Control Bits in AV Mode<br>These bits indicate the slot interval in which the data should be fetched from the corresponding buffers<br>addressed by TDES0 or TDES1.<br>When the Transmit descriptor is fetched, the DMA compares the slot number value in this field with the<br>slot interval maintained in the RSN field DMA_CH#_Slot_Function_Control_Status. It fetches the data<br>from the buffers only if a value matches. These bits are valid only for the AV channels.<br>THL: TCP/UDP Header Length<br>If the TSE bit is set, this field contains the length of the TCP/UDP header. The minimum value of this field<br>must be 5 for TCP header. The value must be equal to 2 for UDP header.<br>This field is valid only for the first descriptor.|
|18|TSE|TSO Split header is not supported. The value of this bit is always zero.|
|17:16|CIC/TPL|Checksum Insertion Control or TCP Payload Length<br>These bits control the checksum calculation and insertion. The following list describes the bit encoding:<br>• 2'b00: Checksum Insertion Disabled.<br>• 2'b01: Only IP header checksum calculation and insertion are enabled.<br>• 2'b10: IP header checksum and payload checksum calculation and insertion are enabled, but<br>pseudo-header checksum is not calculated in hardware.<br>• 2'b11: IP Header checksum and payload checksum calculation and insertion are enabled, and<br>pseudo-header checksum is calculated in hardware.<br>This field is valid when the Enable Transmit TCP/IP Checksum Offload option is selected and the TSE<br>bit is reset.<br>When the TSE bit is set, this field contains the upper bits [17:16] of the TCP Payload (or IP Payload for<br>UDP fragmentation). This allows the TCP/UDP packet length field to be spanned across TDES3[17:0] to<br>provide 256 KB packet length support.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4170 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 600. TDES3 Normal Descriptor (Read Format) (continued) 

|Bits|Name|Description|
|---|---|---|
|||This field is valid only for the first descriptor.|
|15|TPL|Reserved or TCP Payload Length<br>When the TSE bit is reset, this bit is reserved. When the TSE bit is set, this is Bit 15 of the TCP payload<br>length [17:0].<br>This field is valid only when the Enable TCP Segmentation Offloading for TCP/IP Packets option is<br>selected while configuring the core.|
|14:0|FL/TPL|Frame Length or TCP Payload Length<br>This field is equal to the length of the packet to be transmitted in bytes. When the TSE bit is not set, this<br>field is equal to the total length of the packet to be transmitted:<br>Ethernet Header Length + TCP /IP Header Length – Preamble Length – SFD Length + Ethernet<br>Payload Length<br>When the TSE bit is set, this field is equal to the lower 15 bits of the TCP payload length in case of<br>segmentation and IP payload in case of UDP fragmentation.<br>In case of segmentation, this length does not include Ethernet header or TCP/UDP/IP header length. In<br>case of fragmentation, this length does not include Ethernet header and IP header.<br>When DWRR/WFQ algorithm is NOT enabled, value written into this field is not used when TSE = 0.|



### 75.18.3.1.5 Transmit normal descriptor (write-back format) 

The transmit descriptor write-back format includes timestamp low, timestamp high, OWN, and Status bits. 

The write-back format is applicable only for the last descriptor of the corresponding packet. Write 1 to the LD bit (TDES3[28]) in the descriptor where DMA writes back the status and timestamp information for the corresponding transmit packet. 

Figure 455 shows the transmit descriptor write-back format. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4171-08.png)


<!-- Start of picture text -->
31 0<br>TDES0 Timestamp low<br>TDES1 Timestamp high<br>TDES2 Reserved<br>O<br>TDES3 W Status [30:0]<br>N<br><!-- End of picture text -->

Figure 455. Transmit descriptor write-back format 

TDES0 normal descriptor (write-back format) 

Table 601 shows that this format is only applicable to the last descriptor of a packet. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4171 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 601. TDES0 normal descriptor (write-back format)TDES0 normal descriptor (write-back format) 

|Bit|Name|Description|
|---|---|---|
|31:0|TTSL|Transmit Packet Timestamp Low|
|||DMA updates this field with least significant 32 bits of the timestamp captured for the corresponding transmit<br>packet. DMA writes the timestamp only if TTSE bit of TDES2 is 1 in the first descriptor of the packet. This field<br>has the timestamp only if you write 1 to the Last Segment bit (LS) in the descriptor and the Timestamp status<br>(TTSS) bit.|



#### TDES1 normal descriptor (write-back format) 

Table 602 shows that this format is only applicable to the last descriptor of a packet. 

Table 602. TDES1 normal descriptor (write-back format) 

|Bit|Name|Description|
|---|---|---|
|31:0|TTSH|Transmit Packet Timestamp High|
|||DMA updates this field with the most significant 32 bits of the timestamp captured for a corresponding transmit<br>packet. DMA writes the timestamp only if the TTSE bit of TDES2 is 1 in the first descriptor of the packet. This<br>field has the timestamp only if you write 1 to the Last Segment bit (LS) in the descriptor and Timestamp status<br>(TTSS) bit.|



#### TDES2 Normal Descriptor (Write-Back Format) 

This format is applicable only to the last descriptor of a packet. 

Table 603. TDES2 normal descriptor (write-back format) 

|Bit<br>Description|
|---|
|31:0<br>Reserved|



#### TDES3 Normal Descriptor (Write-Back Format) 

This format is applicable only to the last descriptor of a packet. 

Table 604. TDES3 normal descriptor (write-back format) 

|31|30|29|28|27:18|17|16|15|14|13|12|11|10|9|8|7:4|3|2|1|0|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|OWN|CTXT|FD|LD|Rsvd|TTSS|EUE|ES|JT|FF|PCE|LoC|NC|LC|EC|CC|ED|UF|DB|IHE|



Table 605. TDES3 normal descriptor (write-back format) 

|Bit|Name|Description|
|---|---|---|
|31|OWN|Own Bit|
|||When this field is 1, it indicates that the module DMA owns the descriptor. DMA write 0 to this field when<br>it completes the packet transmission. After the write-back is complete, this field is set to 'b0.|
|30|CTXT|Context Type|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4172 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 605. TDES3 normal descriptor (write-back format) (continued) 

|Bit|Name|Description<br>This field must be set to 'b0 for normal descriptor.|
|---|---|---|
|29|FD|First Descriptor<br>This field indicates that the buffer contains the first segment of a packet.|
|28|LD|Last Descriptor<br>This field is set to 'b1 for last descriptor of a packet. DMA writes the status fields only in the last descriptor<br>of the packet.|
|27:24|Rsvd|Reserved|
|23|DE|Descriptor Error<br>When this field is 1, it indicates that the descriptor content is incorrect. DMA writes 1 to this field during<br>write-back when the descriptor is closed.<br>Descriptor errors can be:<br>• Incorrect sequence from the context descriptor. For example, a location after the first descriptor for<br>a packet.<br>• All 1s<br>• CTXT is 1 along with LD or FD bits as 1.<br>When a descriptor error occurs due to all ones or CTXT, LD, and FD bits are 1, the<br>transmit DMA closes the transmit descriptor with DE and LD bits set to 1. When you write<br>1 to IOC bit in TDES2 of corresponding first descriptor, the transmit DMA write 1 to TI bit<br>in the DMA_CH#_Status register<br>~~NOTE~~|
|||Based on CTXT, LD, and FD bits of the transmit descriptor, the subsequent descriptor<br>might consider as the first descriptor (even if FD bit is not 1) and partial packet is sent.<br>~~NOTE~~|
|22:18|Rsvd|Reserved|
|17|TTSS|Tx Timestamp Status<br>This field indicates that a timestamp has been captured for the corresponding transmit packet. When this<br>field is 1, it indicates that TDES0 and TDES1 have timestamp values that were captured for the transmit<br>packet. This field is valid only when the Last Segment control bit (TDES3 [28]) in a descriptor is 1. This<br>field is valid only when IEEE1588 timestamping feature is enabled; otherwise, it is reserved.|
|16|EUE|ECC Uncorrectable Error Status<br>Indicates the ECC uncorrectable error in the TSO memory.<br>An uncorrectable error in the transmit FIFO memory is reported with (Bit 13) FF = 1. This<br>is because the module flushes all such packets.<br>~~NOTE~~|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4173 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 605. TDES3 normal descriptor (write-back format) (continued) 

|Bit|Name|Description|
|---|---|---|
|15|ES|Error Summary<br>This field indicates the logical OR of the following bits:<br>• TDES3[0]: IP header error<br>• TDES3[14]: Jabber timeout<br>• TDES3[13]: Packet flush<br>• TDES3[12]: Payload checksum error<br>• TDES3[11]: Loss of carrier<br>• TDES3[10]: No carrier<br>• TDES3[9]: Late collision<br>• TDES3[8]: Excessive collision<br>• TDES3[3]: Excessive deferral<br>• TDES3[2]: Underflow error<br>This field is 1 when EUE (bit 16) = 1.|
|14|JT|Jabber Timeout<br>This field indicates that the MAC transmitter experiences a jabber time-out. This field is 1 only when<br>MAC_Configuration[JD]is not 1.|
|13|FF|Packet Flushed<br>This field indicates that DMA or MTL flushes the packet because the CPU gives a software<br>flush command.|
|12|PCE|Payload Checksum Error<br>This field indicates that the checksum offload engine had a failure and does not insert any checksum<br>into the encapsulated TCP, UDP, or ICMP payload. This failure can either because of insufficient bytes,<br>as the payload length field of the IP header indicates or the MTL starting to forward the packet to<br>the MAC transmitter in Store-and-forward mode without calculating the checksum. This second error<br>condition only occurs when the transmit FIFO depth is less than the length of the Ethernet packet that is<br>transmitted to avoid deadlock. The MTL starts forwarding the packet when the FIFO is full, even in the<br>Store-and-forward mode.<br>This error can also occur when you detects a bus error during packet transfer.<br>When the full checksum offload engine is not enabled, this bit is reserved.|
|11|LoC|Loss of Carrier<br>This field indicates that a loss of carrier occurred during packet transmission (that is, the gmii_crs_i signal<br>was inactive for one or more transmit clock periods during packet transmission). This field is valid only for<br>the packets transmitted without collision and when MAC operates in the Half-duplex mode.|
|10|NC|No Carrier<br>This field indicates that the carrier sense signal from the PHY was not asserted during transmission.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4174 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 605. TDES3 normal descriptor (write-back format) (continued) 

|Bit|Name|Description|
|---|---|---|
|9|LC|Late Collision<br>This bit indicates that packet transmission was aborted because a collision occurred after the collision<br>window (64 byte times including Preamble in MII mode and 512 byte times including Preamble and Carrier<br>Extension in GMII mode). This bit is not valid if Underflow Error is set.|
|8|EC|Excessive Collision<br>This field indicates that the transmission was aborted after 16 successive collisions when you transmits<br>the current packet. IfMAC_Configuration[DR]= 1, this field is 1 after first collision and abort the<br>packet transmission.|
|7:4|CC|Collision Count<br>This 4-bit counter value indicates the number of collisions occurred before transmitting the packet. The<br>count is not valid when the EC bit = 1.|
|3|ED|Excessive Deferral<br>This field indicates that the transmission ends because of an excessive deferral of over 24,288 bit times<br>(155,680 bits times in 1000 Mbit/s mode or Jumbo packet enabled mode) ifMAC_Configuration[DC]= 1.<br>When TBS is enabled in Full duplex mode and this field is 1, it indicates that the frame drops after the<br>expiry time is reached.|
|2|UF|Underflow Error<br>This field indicates that MAC aborts the packet because the data arrived late from the system memory.<br>The underflow error can occur because of either of the following conditions:<br>• DMA encounters an empty transmit buffer when it transmits the packet<br>• The application filled the MTL Tx FIFO slower than the MAC transmit rate<br>The transmission process enters the Suspended state and sets the underflow bit corresponding to a<br>queue inMTL_Interrupt_Status.|
|1|DB|Deferred Bit<br>This field indicates that MAC defers before transmitting because of presence of carrier. This field is valid<br>only in the Half-Duplex mode.|
|0|IHE|IP Header Error<br>When IP Header Error is 1, this field indicates that the checksum offload engine detects an IP header error.<br>This field is valid only when transit checksum offload is enabled. Otherwise, it is reserved. If COE detects<br>an IP header error, it inserts an IPv4 header checksum if the Ethernet type field indicates an IPv4 payload.<br>In Full-Duplex mode, when EST/Qbv is enabled and this field is 1, it indicates the frame drop status due<br>to the frame size error or schedule error.|



### 75.18.3.2 Transmit context descriptor 

The transmit context descriptor can provide any time before a packet descriptor. The context is valid for the current packet and subsequent packets. The context descriptor provide the timestamps for one-step timestamp correction and VLAN tag ID for VLAN insertion feature. Write back is done on a context descriptor only to write 0 to OWN bit. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4175 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

~~<mark>NOTE</mark>~~ 

DMA internally store the VLAN tag IDs and MSS values which the application provides in a context descriptor with their corresponding valid bits set. DMA always passes the last valid VLAN tag to the MTL, when the outer or inner VLAN tag is provided with the valid bit set. The application cannot invalidate the valid VLAN tag which DMA stores. The VLAN tag is inserted or replaced based on the control inputs provided for the packet. 

The inner VLAN tag control input is used only for the next packet that immediately follows the context descriptor. The application must provide a context descriptor before the normal descriptor of each packet for which DMA must use the inner VLAN tag control input. 

Figure 456 shows the transmit context descriptor format. 

Figure 456. Transmit context descriptor format 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4176-07.png)


<!-- Start of picture text -->
31 0<br>TDES0 Timestamp low [31:0]<br>TDES1 Timestamp high [31:0]<br>TDES2 Inner VLAN tag [31:16] Reserved Maximum segment<br>O<br>TDES3 W Control [30:16] VLAN tag [15:0]<br>N<br><!-- End of picture text -->

### 75.18.3.2.1 TDES0 context descriptor 

Table 606 describes the TDES0 context descriptor format. 

Table 606. TDES0 context descriptor 

|Bit|Name|Description|
|---|---|---|
|31:0|TTSL|Transmit Packet Timestamp Low|
|||For one-step correction, the driver can provide the lower 32 bits of timestamp in this descriptor word. DMA<br>uses this value as the low word for doing one-step timestamp correction. This field is valid only if the OSTC<br>and TCMSSV bits of TDES3 context descriptor are 1.|



### 75.18.3.2.2 TDES1 context descriptor 

Table 607 describes the TDES1 context descriptor format. 

Table 607. TDES1 context descriptor 

|Bit|Name|Description|
|---|---|---|
|31:0|TTSH|Transmit Packet Timestamp High|
|||For one-step correction, the driver can provide the upper 32 bits of timestamp in this descriptor. DMA uses this<br>value as the high word for doing one-step timestamp correction. This field is valid only if the OSTC and TCMSSV<br>bits of TDES3 context descriptor are 1.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4176 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

### 75.18.3.2.3 TDES2 context descriptor 

Table 608 shows the TDES2 context descriptor format. 

Table 608. TDES2 context descriptor 

|Bit|Name|Description|
|---|---|---|
|31:16|IVT|Inner VLAN Tag|
|||When the IVLTV bit of TDES3 context descriptor is 1 and the TCMSSV and OSTC bits of TDES3 context<br>descriptor becomes 0, it indicates that the TDES2[31:16] contains the inner VLAN tag to insert in the<br>subsequent transmit packets.|
|15:14|Rsvd|Reserved|
|13:0|MSS|TSO split header is not supported. The value of this bit is always zero.|



### 75.18.3.2.4 TDES3 context descriptor 

Table 609. TDES3 context descriptor 

|31|30|29:28|27|26|25:24|23|22:18|17|16|15:0|
|---|---|---|---|---|---|---|---|---|---|---|
|OWN|CTXT|Rsvd|OSTC|TCMSSV|Rsvd|CDE|Rsvd|IVLTV|VLTV|VT|



Table 610 shows the TDES3 context descriptor format. 

Table 610. TDES3 context descriptor 

|Bit|Name|Description|
|---|---|---|
|31|OWN|Own Bit<br>When this field is 1, it indicates that the module DMA owns the descriptor. When this field becomes 0, it indicates<br>that the application owns the descriptor. DMA writes 0 to this field immediately after the read.|
|30|CTXT|Context Type<br>This field must set to 1'b1 for context descriptor.|
|29:28|Rsvd|Reserved|
|27|OSTC|One-Step Timestamp Correction Enable<br>When this field is 1, it indicates that DMA performs a one-step timestamp correction with reference to the<br>timestamp values provided in TDES0 and TDES1.|
|26|TCMS<br>SV|One-Step Timestamp Correction Input or MSS Valid<br>When this field and the OSTC field are 1, it indicates that the timestamp correction input provided in TDES0 and<br>TDES1 is valid.<br>When the OSTC field becomes 0 and this field and the TSE bit of TDES3 are 1 in subsequent normal descriptor,<br>it indicates that the MSS input in TDES2 is valid.|
|25:24|Rsvd|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4177 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Table 610. TDES3 context descriptor (continued) 

|Bit|Name|Description|
|---|---|---|
|23|DE|Descriptor Error<br>When this field is 1, it indicates that the descriptor content is incorrect. DMA writes 1 to this field during<br>write-back when it closes the context descriptor.<br>Descriptor errors can be:<br>• Incorrect sequence from the context descriptor. For example, a location before the first descriptor for<br>a packet.<br>• All ones.<br>• CD, LD, and FD bits = 1.<br>When a descriptor error occurs due to all ones or CTXT, LD, and FD bits are 1, the transmit<br>DMA closes the transmit descriptor with DE and LD bits are 1. When you write 1 to IOC<br>bit in TDES2 of corresponding first descriptor, the transmit DMA writes 1 to TI bit in the<br>DMA_CH#_Status register<br>~~NOTE~~|
|||On the basis of CTXT, LD, and FD bits of the transmit descriptor, the subsequent descriptor<br>might considered as the first descriptor (even if FD bit is not 1) and partial packet is sent.<br>~~NOTE~~|
|22:20|Rsvd|Reserved|
|19:18|IVTIR|Inner VLAN Tag Insert or Replace<br>When this field is 1, it requests MAC to perform inner VLAN tagging or un-tagging before transmitting the<br>packets. If the packet is modified for VLAN tags, MAC automatically recalculates and replaces the CRC bytes.<br>The following list describes the values of these bits:<br>• 2'b00: Do not add the inner VLAN tag.<br>• 2'b01: Remove the inner VLAN tag from the packets before transmission. You must use this option only<br>with the VLAN frames.<br>• 2'b10: Insert an inner VLAN tag with the tag value programmed inMAC_Inner_VLAN_Inclor<br>context descriptor.<br>• 2'b11: Replace the inner VLAN tag in packets with the tag value programmed inMAC_Inner_VLAN_Inclor<br>context descriptor. You must use this option only with the VLAN frames..<br>These fields are valid when you select the enable SA and VLAN insertion on transit and enable double VLAN<br>processing options.|
|17|IVLTV|Inner VLAN Tag Valid<br>When this field is 1, it indicates that IVT field of TDES2 is valid.|
|16|VLTV|VLAN Tag Valid<br>When this field is 1, it indicates that VT field of TDES3 is valid.|
|15:0|VT|VLAN Tag|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4178 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 610. TDES3 context descriptor (continued) 

|Bit|Name|Description|
|---|---|---|
|||Contains the VLAN tag to insert or replace in the packet. This field is used as VLAN tag only when|
|||MAC_VLAN_Incl[VLTI]becomes 0.|



## 75.18.4 Receive descriptor 

DMA in the module reads a descriptor only if the tail pointer is different from the base pointer or current pointer. It is recommended to have a descriptor ring with a length that accommodates at least two complete packets which MAC receives. Otherwise, the performance of DMA is impacted because of the unavailability of the descriptors. In such situations, the RxFIFO in MTL becomes full and starts dropping packets. 

The following receive descriptors are present: 

- Normal descriptors 

- Context descriptors 

You can prepare all the receive descriptors and give to DMA as normal descriptors with the content as shown in receive normal descriptor (read format). DMA reads this descriptor and the receive DMA closes the descriptor with the corresponding packet status after transferring a received packet (or part of) to the buffers indicated by the descriptor. The receive normal descriptor (write-back format) describes the format of this status. 

For some packets, only the normal descriptor bits cannot write the complete status. For such packets, the receive DMA writes the extended status to the next descriptor (without processing or using the buffers or pointers embedded in that descriptor). Receive context descriptor describes the descriptor write back format and content. 

### 75.18.4.1 Receive normal descriptor (read format) 

The read format for a receive normal descriptor is made up of the following: 

- A header or buffer 1 address 

- Reserved field 

- Payload or buffer 2 or next descriptor address 

- A 30-bit reserved field 

- OWN bit 

- An interrupt field 

Figure 457 shows the read format for a receive normal descriptor. 

Figure 457. Receive normal descriptor read format 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4179-21.png)


<!-- Start of picture text -->
31 0<br>RDES0 Header or buffer 1 address<br>RDES1 Reserved<br>RDES2 Payload, buffer 2, or next descriptor address<br>l<br>O<br>N<br>RDES3 W Reserved [29:0]<br>T<br>N<br>E<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4179 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

~~<mark>NOTE</mark>~~ 

In the receive descriptor (read format), if the buffer address field is all zeros, the module does not transfer data to that buffer and skips to the next buffer or next descriptor. 

### 75.18.4.1.1 RDES0 normal descriptor (read format) 

Table 611 shows the RDES0 normal descriptor read format. 

Table 611. RDES0 normal descriptor (read format) 

|Bit|Name|Description|
|---|---|---|
|31:0|BUF1AP|Header or Buffer 1 Address Pointer|
|||When the SPH field of control register of a channel becomes 0, these field indicates the physical address of<br>buffer 1. When the SPH field is 1, these field indicates the physical address of header buffer where the receive<br>DMA writes the L2/L3/L4 header bytes of the received packet.<br>The application can program a byte-aligned address for this buffer which means that the LS bits of this field<br>can be non-zero. However, DMA performs a write operation with RDES0[1:0] (or RDES0[2:0]/[3:0] in case of<br>64-/128-bit configuration) as zero, when the start of packet is transfered. However, the packet data shifts per<br>the actual offset which the buffer address pointer provides.|
|||If the address pointer points to a buffer where the middle or last part of the packet is stored, DMA ignores the<br>offset address and writes to the full location which the data-width indicates .|



### 75.18.4.1.2 RDES1 normal descriptor (read format) 

Table 612 shows the RDES1 normal descriptor read format. 

Table 612. RDES1 normal descriptor (read format) 

|Bit|Name|Description|
|---|---|---|
|31:0|Reserved<br>or<br>BUF1AP|Contains the most-significant 32 bits of the buffer 1 address pointer in 64-bit Addressing mode. Otherwise,<br>this field is reserved.|



### 75.18.4.1.3 RDES2 normal descriptor (read format) 

Table 613 shows the RDES2 normal descriptor read format. 

Table 613. RDES2 normal descriptor (read format) 

|Bit|Name|Description|
|---|---|---|
|31:0|BUF2AP|Buffer 2 Address Pointer<br>Indicates the physical address of buffer 2.<br>When the SPH bit of the DMA_CH#_Control register = 1, it indicates that the buffer address pointer must be<br>bus width-aligned, that is, RDES2[3:0, 2:0, or 1:0] = 0 corresponding to 128, 64, or 32 bus width. LSBs are<br>ignored internally.<br>When the SPH bit of the DMA_CH#_Control register becomes 0, it indicates that there is no limitations on the<br>RDES2 value. However, the RxDMA uses the LS fields of the pointer address only when it transfers the start<br>bytes of a packet. If the BUF2AP provides the address of a buffer in which the middle or last part of a packet<br>is stored, DMA ignores BUF2AP[3:0 or 2:0 or 1:0] (corresponding to 128- or 64- or 32-bit data-bus) and writes<br>to the complete location.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4180 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

### 75.18.4.1.4 RDES3 normal descriptor (read format) 

#unique_3961/unique_3961_Connect_42_id_1746ef2a-ecdf-425a-a0eb-74c5a5b90e21 describes the RDES3 normal descriptor read format. 

|31|30|19-26|25|24|23:0|
|---|---|---|---|---|---|
|OWN|IOC|Rsvd|BUF2V|BUF1V|Rsvd|



Table 614. RDES3 normal descriptor (read format) 

|Bit|Name|Description|
|---|---|---|
|31|OWN|Own Bit<br>When this field is 1, it indicates that the module DMA owns the descriptor. When this field becomes 0,<br>it indicates that the application owns the descriptor. DMA write 0 this field when either of the following<br>conditions is true:<br>• DMA completes the packet reception.<br>• The buffers associated with the descriptor are full.|
|30|IOC|Interrupt Enabled on Completion<br>When this field is 1, it indicates that an interrupt is issued to the application when DMA closes this descriptor.|
|29:26|Rsvd|Reserved|
|25|BUF2V|Buffer 2 Address Valid<br>When this field is 1, it indicates to the DMA that the buffer 2 address specified in RDES2 is valid.<br>The application must write 1 to this field so that DMA can use the address, to which the buffer 2 address in<br>RDES2 points to write received packet data.|
|24|BUF1V|Buffer 1 Address Valid<br>When this field is 1, it indicates to the DMA that the buffer 1 address specified in RDES1 is valid.<br>The application must write 1 to this field, if DMA uses the address to which the buffer 1 address in RDES1<br>points to<br>write the received packet data.|
|23:0|Rsvd|Reserved|



### 75.18.4.1.5 Receive normal descriptor (write-back format) 

Figure 458 shows the write-back format for a receive normal descriptor. 

Figure 458. Receive normal descriptor (write-back format) 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4181 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4182-02.png)


<!-- Start of picture text -->
31 0<br>RDES0 Inner VLAN tag [31:16] Outer VLAN tag [15:0]<br>RDES1 OAM code or MAC control Extended status<br>ARP<br>V Reserved Header length<br>RDES2 MAC filter of flexible receive parser status<br>F [14:12] [9:0]<br>[11:10]<br>C<br>O<br>T F L E<br>RDES3 W Status [27:15] Packet length [14:0]<br>X D D S<br>N<br>T<br><!-- End of picture text -->

~~<mark>NOTE</mark>~~ 

When you enables the flexible receive parser, RDES2[31:16] indicates the parser status, and not the MAC filter status. The MAC filter status is not available when flexible receive parser is enabled. 

### 75.18.4.1.5.1 RDES0 normal descriptor (write-back format) 

Table 615 shows the write-back format for the RDES0 normal descriptor. 

Table 615. RDES0 normal descriptor (write-back format) 

|Bit|Name|Description|
|---|---|---|
|31:16|IVT|Inner VLAN Tag|
|||Contains the inner VLAN tag of the received packet if the RS0V bit of RDES3 = 1.|
|||This field is valid only when you enables the double VLAN tag processing and VLAN tag stripping.|
|15:0|OVT|Outer VLAN Tag|
|||Contains the outer VLAN tag of the received packet if the RS0V bit of RDES3 = 1.|



### 75.18.4.1.5.2 RDES1 normal descriptor (write-back format) 

The status fields in the write-back format are valid only for the last descriptor (RDES3[28] = 1). #unique_3963/ unique_3963_Connect_42_table_18e086e2-bda5-4002-b444-4d7ac47c01e8 provide the details of the write-back format for RDES1 normal descriptor. 

|31:16|15|14|13|12|11:8|7|6|5|4|3|2:0|
|---|---|---|---|---|---|---|---|---|---|---|---|
|OPC|TD|TSA|PV|PFT|PMT|IPCE|IPCB|IPV6|IPV4|IPHE|PT|



Table 616. RDES1 normal descriptor (write-back format) 

|Bit|Name|Description|
|---|---|---|
|31:16|OPC|Indicates any one of the following:|
|||• OAM sub-type code: If bits [18:16] of RDES3 as described inRDES3 normal descriptor (read format)|
|||are 111b, this field contains the OAM sub-type and code fields.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4182 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 616. RDES1 normal descriptor (write-back format) (continued) 

|Bit|Name|Description|
|---|---|---|
|||• MAC control packet opcode: Bits 15:8 of RDES3 as described inRDES3 normal descriptor (read<br>format)contain the subtype and bits 7:0 contain the code.|
|15|TD|Timestamp Dropped<br>Indicates that the timestamp was captured for this packet but it dropped in the MTL Rx FIFO because<br>of overflow.<br>This field is available only when you select the timestamp feature. Otherwise, this field is reserved.|
|14|TSA|Timestamp Available<br>Indicates that the timestamp value is available in a context descriptor word 2 (RDES2) and word 1(RDES1)<br>when timestamp is present. This is valid only when the last descriptor field (RDES3 [28]) = 1<br>You can write the context descriptor in the next descriptor just after the last normal descriptor for a packet.|
|13|PV|PTP Version<br>Indicates that the received PTP message has the IEEE 1588 version 2 format. When this field becomes 0, it<br>indicates the IEEE 1588 version 1 format.<br>This field is available only when you select the timestamp feature. Otherwise, this field is reserved.|
|12|PFT|PTP Packet Type<br>Indicates that the PTP message is sent directly over Ethernet. This field is available only when you select the<br>timestamp feature. Otherwise, this field is reserved.|
|11:8|PMT|PTP Message Type<br>Encodes to give the type of the message received:<br>• 0000: No PTP message received<br>• 0001: SYNC (all clock types)<br>• 0010: Follow_Up (all clock types)<br>• 0011: Delay_Req (all clock types)<br>• 0100: Delay_Resp (all clock types)<br>• 0101: Pdelay_Req (in peer-to-peer transparent clock)<br>• 0110: Pdelay_Resp (in peer-to-peer transparent clock)<br>• 0111: Pdelay_Resp_Follow_Up (in peer-to-peer transparent clock)<br>• 1000: Announce<br>• 1001: Management<br>• 1010: Signaling<br>• 1011–1110: Reserved<br>• 1111: PTP packet with reserved message type<br>These fields are available only when you select the timestamp feature.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4183 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 616. RDES1 normal descriptor (write-back format) (continued) 

|Bit|Name|Description|
|---|---|---|
|7|IPCE|IP Payload Error<br>When this field is 1, it indicates either of the following:<br>• The 16-bit IP payload checksum (that is, the TCP, UDP, or ICMP checksum) which MAC calculates does<br>not match the corresponding checksum field in the received segment.<br>• The TCP, UDP, or ICMP segment length does not match the payload length value in the IP header field.<br>• The TCP, UDP, or ICMP segment length is less than minimum allowed segment length for TCP, UDP,<br>or ICMP.<br>Bit 15 (ES) of RDES3 is not set when this field is 1.|
|6|IPCB|IP Checksum Bypassed<br>Indicates that the checksum offload engine is bypassed. This field is available when you select the enable<br>receive TCP/IP checksum check feature.|
|5|IPV6|IPv6 header Present<br>Indicates that an IPV6 header is detected. When you select the enable split header feature option and the<br>SPH bit of control register of a channel is 1, the IPV6 header is available in the header buffer area to which<br>RDES0 points.|
|4|IPV4|IPV4 Header Present<br>Indicates that an IPV4 header is detected. When the SPH bit of RDES3 is 1, the IPV4 header is available in the<br>header buffer area to which RDES0 points.|
|3|IPHE|IP Header Error<br>When this field is 1, it indicates either of the following:<br>• The 16-bit IPv4 header checksum which MAC calculates does not match the received checksum bytes.<br>• The IP datagram version is not consistent with the Ethernet type value.<br>• Ethernet packet does not have the expected number of IP header bytes.<br>This field is valid when either bit 5 or bit 4 is 1. This field is available when you select the enable receive TCP/IP<br>checksum check feature.|
|2:0|PT|Payload Type<br>Indicates the type of payload encapsulated in the IP datagram that the receive checksum offload engine<br>(COE) process.<br>• 3'b000: Unknown type or IP/AV payload not processed<br>• 3'b001: UDP<br>• 3'b010: TCP<br>• 3'b011: ICMP<br>• 3'b110: AV tagged data packet<br>• 3'b111: AV tagged control packet|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4184 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 616. RDES1 normal descriptor (write-back format) (continued) 

|Bit|Name|Description|
|---|---|---|
|||• 3'b101: AV untagged control packet|
|||• 3'b100: IGMP, if IPV4 header present field = 1, else DCB (LLDP) control packet|
|||If the COE does not process the payload of an IP datagram because there is an IP header error or fragmented<br>IP, it sets these fields to 3'b000.|



### 75.18.4.1.5.3 RDES2 normal descriptor (Write-back format) 

|31:29|28|27|26:19|18|17|16|15|14|13:11|10|9:0|
|---|---|---|---|---|---|---|---|---|---|---|---|
|L3L4FM|L4FM|L3FM|MADRM|HF|DAF|SAF|OTS|ITS|Rsvd|ARPNR|HL|



Table 617. RDES2 normal descriptor (Write-back format) 

|Bit|Name|Description|
|---|---|---|
|31:29|L3L4FM|Layer 3 and Layer 4 Filter Number Matched<br>Indicates the number of the layer 3 and layer 4 filter that matches the received packet:<br>• 000: Filter 0<br>• 001: Filter 1<br>• 010: Filter 2<br>• 011: Filter 3|
|||• 100: Filter 4<br>• 101: Filter 5<br>• 110: Filter 6<br>• 111: Filter 7<br>This field is valid only when bit 28 or bit 27 = 1. When more than one filter matches, these fields provide<br>the number of lowest filter.|
|||This status is not available when Flexible RX Parser is enabled.<br>~~NOTE~~|
|28|L4FM|Layer 4 Filter Match<br>When this field is 1, it indicates that the received packet matches one of the enabled layer 4 port number<br>fields. This status is given only when one of these conditions is true:<br>• Layer 3 fields are not enabled and all enabled layer 4 fields match<br>• All enabled layer 3 and layer 4 filter fields match<br>When more than one filter matches, this bit gives the layer 4 filter status of filter indicated by Bits[31:29].<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4185 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 617. RDES2 normal descriptor (Write-back format) (continued) 

|Bit|Name|Description|
|---|---|---|
|||This status is not available when the flexible receive parser is enabled.<br>~~NOTE~~|
|27|L3FM|Layer 3 Filter Match<br>When this field is 1, it indicates that the received packet matches one of the enabled layer 3 IP address<br>fields. This status is given only when one of these conditions is true:<br>• All enabled layer 3 fields match and bypasses all enabled layer 4 fields.<br>• All enabled filter fields match.<br>When more than one filter matches, this field gives the layer 3 filter status of filter which<br>bits[31:29] indicate.<br>This status is not available when the flexible receive parser is enabled.<br>~~NOTE~~|
|26:19|MADRM|MAC Address Match or Hash Value<br>When HF becomes 0, it indicates that this field contains the MAC address register number that matches<br>the received packet destination address. This field is valid only if the DAF field becomes 0.<br>When HF = 1, it indicates that this field contains the hash value that MAC computes. A packet passes the<br>hash filter when the field corresponding to the hash value is 1 in the hash filter register.<br>This status is not available when the flexible receive parser is enabled.<br>~~NOTE~~|
|18|HF|Hash Filter Status<br>When this field is 1, it indicates that the packet passes the MAC address hash filter. Bits[26:19] indicate<br>the hash value.<br>This status is not available when the flexible receive parser is enabled.<br>~~NOTE~~|
|17|DAF/RXPI|Destination Address Filter Fail<br>When flexible receive parser is disabled, and this field is 1, it indicates that the packet fails the DA<br>filter in MAC.<br>When flexible receive parser is enabled, and this field is 1, it indicates that the packet parsing is<br>incomplete (RXPI) due to ECC error.<br>When this field is 1, RDES3 ES field is also 1.<br>~~NOTE~~|
|16|SAF/RXPD|SA Address Filter Fail<br>When flexible receive parser is disabled, and this field is 1, it indicates that the packet fails the SA filter<br>in MAC.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4186 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 617. RDES2 normal descriptor (Write-back format) (continued) 

|Bit|Name|Description|
|---|---|---|
|||When flexible receive parser is enabled and this field is 1, it indicates that the parser drops the<br>RXPD packet.<br>When this field is 1, RDES3 ES field is also 1.<br>~~NOTE~~|
|15|OTS|VLAN Filter Status<br>When this field is 1, it indicates that the received packet VLAN tag passes the VLAN filter.<br>This field redefines as an outer VLAN tag filter status (OTS). This field is valid for both single and double<br>VLAN tagged frames.|
|14|ITS|Inner VLAN Tag Filter Status (ITS)<br>This field is valid only for double VLAN tagged frames, when double VLAN processing is enabled.<br>SeeFilter statusfor more information.|
|13:11|Rsvd|Reserved|
|10|ARPNR|ARP Reply Not Generated<br>When this field is 1, it indicates that MAC did not generate the ARP reply for the ARP request packet it<br>receives.. This field is 1 when MAC is busy transmitting ARP reply to earlier ARP request (only one ARP<br>request is processed at a time).<br>This field is reserved when you do not select the enable IPv4 ARP offload option.|
|9:0|HL|L3/L4 Header Length<br>Contains the length of the packet header which MAC splits at L3 or L4 header boundary which the MAC<br>receiver identifies. This field is valid only when the first descriptor bit = 1 (FD = 1).<br>You can write the header data to the buffer 1 address of corresponding descriptor. If the header length<br>is zero, this field is not valid. It implies that MAC does not identify and split the header.<br>This field is valid when you select the enable split header feature option.|



### 75.18.4.1.5.4 RDES3 normal descriptor (Write-back format) 

#unique_3965/unique_3965_Connect_42_id_9cde4392-a0c2-4731-bcb2-bf9dcd789aae describes the write-back format for the RDES3 normal descriptor. 

|31|30|29|28|27|26|25|24|23|22|21|20|19|18:16|15|14:0|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|OWN|CTXT|FD|LD|RS2V|RS1V|RS0V|CE|GP|RWT|OE|RE|DE|LT|ES|PL|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4187 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Table 618. RDES3 normal descriptor (Write-back format) 

|Bit|Name|Description|
|---|---|---|
|31|OWN|Own Bit<br>When this field is 1, it indicates that the module DMA owns the descriptor. If this field becomes 0, it indicates<br>that the application owns the descriptor. DMA writes 0 to this field when either of these conditions is true:<br>• DMA completes the packet reception.<br>• The buffers associated with the descriptor are full.|
|30|CTXT|Receive Context Descriptor<br>When this field is 1, it indicates that the current descriptor is a context type descriptor. DMA writes 1'b0 to this<br>field for a normal receive descriptor.<br>When CTXT and FD bits are used together, {CTXT, FD}<br>• 2’b00: Intermediate descriptor<br>• 2’b01: First descriptor<br>• 2’b10: Reserved<br>• 2’b11: Descriptor error (due to all 1s)<br>When descriptor error occurs, the receive DMA closes the receive descriptor indicating a<br>descriptor error. This receive descriptor is skipped and the buffer addresses are not used to<br>write the packet data. Receive DMA will write 1 to the CDE bit in DMA_CH#_Status register<br>but not to the RI bit even when IOC = 1, as this is not marked as the last receive descriptor for<br>the packet. The subsequent valid receive descriptor writes the packet data.<br>~~NOTE~~|
|29|FD|First Descriptor<br>When this field is 1, it indicates that this descriptor contains the first buffer of the packet. If the size of the first<br>buffer is 0, the second buffer contains the beginning of the packet and if the size of the second buffer is also<br>0, the next descriptor will contain the beginning of the packet.<br>See the CTXT bit description for more information on how to use the CTXT bit and FD bit together.|
|28|LD|Last Descriptor<br>When this field is 1, it indicates that this descriptor buffers points to the last buffers of the packet.|
|27|RS2V|Receive Status RDES2 Valid<br>When this field is 1, it indicates that the status in RDES2 is valid and DMA writes it. This field is valid only when<br>the LD bit of RDES3 = 1.|
|26|RS1V|Receive Status RDES1 Valid<br>When this field is 1, it indicates that the status in RDES1 is valid and DMA writes it. This field is valid only when<br>the LD bit of RDES3 = 1.|
|25|RS0V|Receive Status RDES0 Valid<br>When this field is 1, it indicates that the status in RDES0 is valid and DMA writes it. This field is valid only when<br>the LD bit of RDES3 = 1.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4188 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 618. RDES3 normal descriptor (Write-back format) (continued) 

|Bit|Name|Description|
|---|---|---|
|24|CE|CRC Error<br>When this field is 1, it indicates that a cyclic redundancy check (CRC) error occurs on the received packet. This<br>field is valid only when the LD bit of RDES3 = 1.|
|23|GP|Giant Packet<br>When this field is 1, it indicates that the packet length exceeds the specified maximum Ethernet size of 1518,<br>1522, or 2000 bytes (9018 or 9022 bytes if jumbo packet enable = 1).<br>Giant packet indicates only the packet length. It does not cause any packet truncation.<br>~~NOTE~~|
|22|RWT|Receive Watchdog Timeout<br>When this field is 1, it indicates that the receive watchdog timer expires when it receives the current packet.<br>The current packet truncates after watchdog timeout.|
|21|OE|Overflow Error<br>When this field is 1, it indicates that the received packet is damaged because of buffer overflow in<br>receive FIFO.<br>This field is 1 only when DMA transfers a partial packet to the application. This happens only<br>when the receive FIFO operates in the Threshold mode. In the Store-and-Forward mode, all<br>the partial packets drops completely in the receive FIFO.<br>~~NOTE~~|
|20|RE|Receive Error<br>When this field is 1, it indicates that the gmii_rxer_i signal asserts when the gmii_rxdv_i signal asserts during<br>the packet reception. This error also includes carrier extension error in the GMII and Half-duplex mode. Error<br>can be of less or no extension, or error (rxd!= 0f) during extension.|
|19|DE|Dribble Bit Error<br>When this field is 1, it indicates that the received packet has a non-integer multiple of bytes (odd nibbles). This<br>field is valid only in the MII mode.|
|18:16|LT|Length/Type Field<br>Indicates if the packet received is a length packet or a type packet. The encoding of the 3 bits is as follows:<br>• 3'b000: The packet is a length packet.<br>• 3'b001: The packet is a type packet.<br>• 3'b011: The packet is a ARP request packet type<br>• 3'b100: The packet is a type packet with VLAN tag<br>• 3'b101: The packet is a type packet with double VLAN tag<br>• 3'b110: The packet is a MAC control packet type<br>• 3'b111: The packet is a OAM packet type|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4189 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

#### Table 618. RDES3 normal descriptor (Write-back format) (continued) 

|Bit|Name|Description|
|---|---|---|
|||• 3'b010: Reserved|
|15|ES|Error Summary<br>When this field is 1, it indicates the logical OR of these bits, :<br>• RDES3[24]: CRC error<br>• RDES3[19]: Dribble error<br>• RDES3[20]: Receive error<br>• RDES3[22]: Watchdog timeout<br>• RDES3[21]: Overflow error<br>• RDES3[23]: Giant packet<br>• RDES2[17]: Destination address filter fail, when the flexible receive parser is enabled<br>• RDES2[16]: SA address filter fail, when flexible receive parser is enabled<br>This field is valid only when the LD bit of RDES3 = 1.|
|14:0|PL|Packet Length<br>Indicates the byte length of the received packet that was transferred to system memory (including CRC).<br>This field is valid when the LD bit of RDES3 = 1 and overflow error bits becomes 0. The packet length also<br>includes the two bytes that appends to the Ethernet packet when IP checksum calculation is enabled and the<br>received packet is not a MAC control packet.<br>This field is valid when the LD bit of RDES3 = 1. When the last descriptor and error summary bits are not 1,<br>this field indicates the accumulated number of bytes that are transferred for the current packet.|



### 75.18.4.1.6 Receive context descriptor 

This descriptor is read-only for the application. Only DMA can write to this descriptor. The context descriptor provides information about the extended status related to the last received packet. Bit 30 of RDES3 indicates the context type descriptor. 

#### Figure 459. Receive context descriptor format 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4190-07.png)


<!-- Start of picture text -->
31 0<br>RDES0 Timestamp low [31:0]<br>RDES1 Timestamp high [31:0]<br>RDES2 Reserved<br>C<br>O<br>T<br>RDES3 W Reserved [29:0]<br>X<br>N<br>T<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4190 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

### 75.18.4.1.6.1 RDES0 context descriptor 

Table 619. RDES0 context descriptor 

|Bit|Name|Description|
|---|---|---|
|31:0|RTSL|Receive Packet Timestamp Low|
|||DMA updates this field with least significant 32-bits of the timestamp captured for the corresponding receive<br>packet. When this field and the RTSH field of RDES1 show all-ones value, you must consider the timestamp<br>as corrupt.|



### 75.18.4.1.6.2 RDES1 context descriptor 

Table 620. RDES1 context descriptor 

|Bit|Field|Description|
|---|---|---|
|31:0|RTSH|Receive Packet Timestamp High|
|||DMA updates this field with the most significant 32-bits of the timestamp captured for the corresponding receive<br>packet. When this field and the RTSL field of RDES0 show all-ones value, you must consider the timestamp<br>as corrupt.|



### 75.18.4.1.6.3 RDES2 context descriptor 

Table 621. RDES2 context descriptor 

|Bit<br>Description|
|---|
|31:0<br>Reserved|



### 75.18.4.1.6.4 RDES3 context descriptor 

|31|30|29|28:0|
|---|---|---|---|
|OWN|CTXT|DE|Rsvd|



Table 622. RDES3 context descriptor 

|Bit|Name|Description|
|---|---|---|
|31|OWN|Own Bit|
|||When this field is 1, it indicates that DMA owns the descriptor. When this field becomes 0, it indicates that the<br>application owns the descriptor. DMA clears this field when either of these conditions is true:|
|||• DMA completes the packet reception.|
|||• The buffers associated with the descriptor are full.|
|30|CTXT|Receive Context Descriptor|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4191 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table 622. RDES3 context descriptor (continued) 

|Bit|Name|Description|
|---|---|---|
|||When this field is 1, it indicates that the current descriptor is a context descriptor. DMA writes 1'b1 to this field<br>for context descriptor.<br>DMA writes 2’b11 to indicate a descriptor error due to all = 1.<br>When CTXT and DE bits are used together {CTXT, DE}<br>• 2’b00: Reserved<br>• 2’b01: Reserved<br>• 2’b10: Context descriptor<br>• 2’b11: Descriptor error<br>Note: When descriptor error occurs, the receive DMA closes the receive descriptor indicating descriptor error.<br>This receive descriptor is skipped and the buffer addresses does not write the packet data. The receive DMA<br>writes 1 to the CDE bit in DMA_CH#_Status register but not to the RI bit even when IOC = 1, because this<br>is not marked as last receive descriptor for the packet. The subsequent valid receive descriptor writes the<br>packet data.|
|29|DE|Descriptor Error<br>See the CTXT bit description for more information about how to use the DE bit along with CTXT bit.|
|28:0|Rsvd|Reserved|



## 75.18.5 Enhanced descriptor for time-based scheduling 

This feature needs 32 bytes enhanced descriptors to enable on all the DMA channels that uses this feature (write 1 to EDSE bit of DMA_CH(#i)_TX_Control register). 

The structure of 32-byte descriptor for the context and the normal descriptor in read and write formats are described in the upcoming sections. 

### 75.18.5.1 Enhanced normal descriptor - Read (32-bit mode) 

These fields are present in the first 16 bytes of the enhanced descriptor format of normal descriptor: 

- LTV- Indicates that the launch time (LT) and GSN fields present in the descriptor are valid. The LTV must be = 1 only if the FD bit of the descriptor is not. 

- GSN- Indicates the GCL slot number associated with the packet. 

- LT- Indicates the launch time associated with the packet. 

Figure 460. Enhanced normal descriptor - Read (32-bit mode) 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4192 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4193-02.png)


<!-- Start of picture text -->
31 11 8 0<br>GSN<br>ETDESC4 Reserved LT [31:24]<br> [3:0]<br>ETDESC5 Launch time [23:0]<br>ETDESC6 Reserved<br>ETDESC7 Reserved<br>TDESC0 Header or buffer 1 address [31:0]<br>TDESC1 Buffer 2 address [31:0] or buffer 1 address [63:32]<br>Header or buffer 1<br>TDESC2 Buffer 2 length [29:16]<br>length [13:0]<br>Control [30:16] Frame length [14:0]<br>TDESC3<br>Control [30:18] Payload length [17:0]<br>LTV<br>IOC TTSE VTIR<br>OWN<br><!-- End of picture text -->

### 75.18.5.2 Enhanced normal descriptor (Write, 32-bit mode) 

Figure 461. Enhanced normal descriptor write (32-bit mode) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4193-05.png)


<!-- Start of picture text -->
31 11 8 0<br>GSN<br>ETDESC4 Reserved LT [31:24]<br> [3:0]<br>ETDESC5 Launch time [23:0]<br>ETDESC6 Reserved<br>ETDESC7 Reserved<br>TDESC0 Timestamp low<br>TDESC1 Timestamp high<br>TDESC2 Reserved<br>TDESC3 Status [30:0]<br>LTV<br>OWN<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4193 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

~~<mark>NOTE</mark>~~ 

- All the enhanced descriptors, example, assumes a 32-bit data width configurations. However, the same definitions are valid in 64-bit and 128-bit configurations. 

- In both the write back formats, you cannot modify the extended 16 bytes. The remaining 16 bytes (TDESC0 to TDESC3) are written back per the previous 16 bytes descriptor format. 

- When you enable the fetch time it overrides the AV slot function 

- When an unaligned new GCL list (with a different CTR) is installed it is recommended not to have traffic during the installation of the new list. Any traffic during the switching of the lists might have unpredictable behavior regarding fetch, launch, and launch expiry because the CTR and BTR values get updated when the frame is processed 

### 75.18.5.3 Enhanced context descriptor (Read, 32-bit mode) 

The first 16 bytes of the enhanced context descriptor (ETDESC4 to ETDESC7) are reserved and must be = 0. The fields present in the last bytes of the descriptor (TDESC0 to TDESC3) are same as the context descriptor (TDESC0 to TDESC3) in 16 byte format. 

Figure 462. Enhanced context descriptor - Read 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4194-10.png)


<!-- Start of picture text -->
31 0<br>ETDESC4 Reserved<br>ETDESC5 Reserved<br>ETDESC6 Reserved<br>ETDESC7 Reserved<br>TDESC0 Timestamp low [31:0]<br>TDESC1 Timestamp high [31:0]<br>TDESC2 Inner VLAN tag [31:16] Reserved Maximum segment<br>size [13:0]<br>TDESC3 OWN Control [30:16] VLAN tag [15:0]<br><!-- End of picture text -->

### 75.18.5.4 Enhanced context descriptor (Write, 32-bit mode) 

Figure 463. Enhanced context descriptor - Write 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4194 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part4/S32K3XXRM_数据表.pdf-4195-02.png)


<!-- Start of picture text -->
31 0<br>ETDESC4 Reserved<br>ETDESC5 Reserved<br>ETDESC6 Reserved<br>ETDESC7 Reserved<br>TDESC0 Reserved<br>TDESC1 Reserved<br>TDESC2 Reserved<br>TDESC3 Reserved Reserved<br>OWN CTXT CDE<br><!-- End of picture text -->

# 75.19 Programming 

This section and all its sub-sections are Synopsys Proprietary. Used with permission. 

This section provides the instructions for initializing the DMA or MAC registers in the proper sequence. 

## 75.19.1 Initializing DMA 

Perform these steps to initialize DMA: 

1. Provide a software reset. This resets all the MAC internal registers and logic (bit-0 of DMA_Mode). 

2. Wait for the reset process (poll bit 0 of DMA_Mode which is only clears after the reset operation completes) to complete. 

3. Program these fields to initialize DMA_SysBus_Mode: 

   - a. DMA_SysBus_Mode[AAL] 

   - b. Fixed burst or undefined burst 

   - c. Burst mode values in case of AHB bus interface, OSR_LMT in case of AXI bus interface. 

   - d. Select the maximum burst length possible on the AXI bus (bits [7:1]), if fixed length value is enabled. 

4. Create a descriptor list for a transmit and receive. Also, ensure that DMA (write 1 to bit 31 of descriptor TDES3/RDES3) owns the descriptors. See Descriptors for more information about descriptors. 

5. Program the transmit and receive ring length registers (DMA_CH(#i)_TxDesc_Ring_Length (for i = 0; i <= 1) and DMA_CH(#i)_RxDesc_Ring_Length (for i = 0; i <= 1)). The programmed ring length must be at least 4. 

      - ~~<mark>NOTE</mark>~~ 

The descriptor address from the start to the end of the ring must not cross the 4 GB boundary. 

6. Initialize the receive and transmit descriptor list address with the base address of the transmit and receive descriptor (DMA_CH(#i)_TxDesc_List_Address (for i = 0; i <= DWC_EQOS_NUM_DMA_TX_CH-1), DMA_CH(#i)_RxDesc_List_Address (for i = 0; i <= DWC_EQOS_NUM_DMA_RX_CH-1)). Also, program the transmit and receive tail pointer registers that indicates DMA about the available descriptors (DMA_CH(#i)_TxDesc_Tail_Pointer 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4195 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

(for i = 0; i <= DWC_EQOS_NUM_DMA_TX_CH-1) and DMA_CH(#i)_RxDesc_Tail_Pointer (for i = 0; i <= DWC_EQOS_NUM_DMA_RX_CH-1)). 

~~<mark>NOTE</mark>~~ 

For 40-bit or 48-bit addressing mode, program the higher address List registers (DMA_CH[n]_TxDesc_List_HAddress, DMA_CH[n]_RxDesc_List_HAddress). 

The tailpointer registers must advance to the location immediately after the descriptors that are set so that DMA is aware that the additional descriptors are available. 

7. Program the settings of these registers for the parameters like maximum burst-length (PBL) which DMA initiates, descriptor skip lengths, OSP in case of TxDMA, RBSZ in case of RxDMA, and so on: 

   - DMA_CH(#i)_Control (for i = 0; i <= DWC_EQOS_NUM_DMA_TX_CH-1) 

   - DMA_CH(#i)_TX_Control (for i = 0; i <= DWC_EQOS_NUM_DMA_TX_CH-1) 

   - DMA_CH(#i)_RX_Control (for i = 0; i <= DWC_EQOS_NUM_DMA_RX_CH-1) 

8. Program the DMA_CH(#i)_Interrupt_Enable (for i = 0; i <= DWC_EQOS_NUM_DMA_TX_CH-1) register to enable the interrupts. 

9. Write 1 to SR (bit 0) of the DMA_CH(#i)_RX_Control (for i = 0; i <= DWC_EQOS_NUM_DMA_RX_CH-1) and ST (bit 0) of the DMA_CH(#i)_TX_Control (for i = 0; i <= DWC_EQOS_NUM_DMA_TX_CH-1) register to start the receive and transmit DMAs. 

10. Repeat steps 4 to 9 for all the transit DMA and receive DMA channels selected in the hardware. 

## 75.19.2 Initializing MTL registers 

The transaction layer (MTL) registers must initialize to establish the transmit and receive operating modes and commands. 

Perform these steps to initialize the MTL registers: 

1. Program MTL_Operation_Mode[SCHALG] and MTL_Operation_Mode[RAA] to initialize the MTL operation in case of multiple transit and receive queues. 

2. Program the receive queue to DMA mapping in MTL_RxQ_DMA_Map0. 

3. Program these fields to initialize the mode of operation in MTL_TxQ0_Operation_Mode. 

   - a. MTL_TxQ0_Operation_Mode[TSF] or MTL_TxQ0_Operation_Mode[TTC] in case of Threshold mode. 

   - b. MTL_TxQ0_Operation_Mode[TXQEN] to value 2'b10 to enable transmit queue0. 

   - c. MTL_TxQ0_Operation_Mode[TQS] 

4. Program these fields to initialize the mode of operation in MTL_RxQ0_Operation_Mode: 

   - a. MTL_RxQ0_Operation_Mode[RSF] or MTL_RxQ0_Operation_Mode[RTC] in case of Threshold mode. 

   - b. Flow control activation and de-activation thresholds for MTL receive FIFO (MTL_RxQ0_Operation_Mode[RFA] and MTL_RxQ0_Operation_Mode[RFD]). 

   - c. Error Packet and undersized good Packet forwarding enable (MTL_RxQ0_Operation_Mode[FEP] and MTL_RxQ0_Operation_Mode[FUP]). 

   - d. MTL_RxQ0_Operation_Mode[RQS] 

5. Repeat previous two steps for all MTL transit and receive queues selected in the configuration. 

## 75.19.3 Initializing MAC 

The MAC configuration registers establish the operating mode of MAC. These registers must initialize before initializing DMA. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4196 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

You can perform these MAC initialization operations after DMA initialization. If the MAC initialization completes before DMA is configured, enable the MAC receiver (last step in the following sequence) only after the DMA is active. Otherwise, the received frames fill the receive FIFO and overflow. 

1. Provide the MAC address registers: MAC_Address0_High and MAC_Address0_Low. If more than one MAC address is enabled, , program the MAC addresses appropriately. 

2. Program these fields to set the appropriate filters for the incoming frames in MAC_Packet_Filter: 

- a. Receive all 

- b. Promiscuous mode 

- c. Hash or perfect filter 

- d. Unicast, multicast, broadcast, and control frames filter settings 

3. Program these fields for proper flow control in MAC_Q0_Tx_Flow_Ctrl: 

- a. Pause time and other Pause frame control bits 

- b. Transmit flow control bits 

- c. Flow control busy 

4. Program MAC_Interrupt_Enable as required, and if applicable, for your configuration. 

5. Program the appropriate fields in MAC_Configuration. For example Inter-packet gap when transmission and jabber disable. 

6. Write 1 to MAC_Configuration[RE] and MAC_Configuration[TE] to start the MAC transmitter and receiver. 

## 75.19.4 Performing normal receive and transmit operation 

During normal operation of the module, read the normal and transmit interrupts, poll the descriptors, suspend the DMA (if it does not own descriptors), and read the values of the current host transmitter or receiver descriptor pointers for debugging. 

For normal operation, perform these steps: 

1. Read the interrupt status for normal transmit and receive interrupts. Then poll the descriptors, read the status of the descriptor which the host owns (either transmit or receive). 

2. Set appropriate values for the descriptors, ensure that the DMA owns the transmit and receive descriptors to resume the data transmission and reception. 

3. If DMA does not own the descriptors (or no descriptor is available), DMA enters into SUSPEND state. The transmission or reception can resume by freeing the descriptors and writing the descriptor tail pointer to Tx/Rx tail pointer register (DMA_CH[n]_TxDesc_Tail_Pointer and DMA_CH[n]_RxDesc_Tail_Pointer). 

4. Read the current host transmitter or receiver descriptor address pointer values for the debug process 

(DMA_CH[n]_Current_App_TxDesc and DMA_CH[n]_Current_App_RxDesc regsiter). 

5. Read the current host transmit buffer address pointer and receive buffer address pointer values for the debug process (Register DMA_CH[n]_Current_App_TxBuffer and DMA_CH[n]_Cur-rent_App_RxBuffer). 

## 75.19.5 Stopping and starting transmission 

Perform these steps to pause the transmission for some time. The steps are provided for channel 0. 

1. Write 0 to bit 0 (ST) of DMA_CH(#i)_TX_Control (for i = 0; i <= DWC_EQOS_NUM_DMA_TX_CH-1) register to disable the transmit DMA (if applicable) . 

2. Wait for any previous frame transmissions to complete. Read the appropriate fields of MTL_TxQ0_Debug (MTL_TxQ0_Debug[TRCSTS] is not 01 and MTL_TxQ0_Debug[TXQSTS] = 0) to check this. 

3. Write 0 to MAC_Configuration[RE] and MAC_Configuration[TE] to disable the MAC transmitter and MAC receiver. 

4. Disable the receive DMA (if applicable), after you ensure that the data in the receive FIFO transfers to the system memory (read the appropriate fields MTL_RxQ0_Debug[PRXQ] = 0 and MTL_RxQ0_Debug[RXQSTS] = 00). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4197 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

5. Ensure that both the transit queue and receive queue are empty (MTL_TxQ0_Debug[TXQSTS] = 0 and MTL_RxQ0_Debug[RXQSTS] = 0). 

6. Restart the operation by first starting the DMAs, and then enable the MAC transmitter and receiver. 

      - ~~<mark>NOTE</mark>~~ 

   - Do not change the configuration (such as duplex mode, speed, port, or loop back) when the MAC is actively transmitting or receiving. You can change these parameters only when the MAC transmitter and receiver are not active. 

   - Similarly, do not change the DMA related configuration when transmit and receive DMA are active. 

## 75.19.6 Programming guidelines for switching to new descriptor list in RxDMA 

Switching to a new descriptor list is different in the receive DMA as compared to the transit DMA. It is permitted when the RxDMA is in SUSPEND state as described below: 

- RxDMA prepares the descriptors in advance. 

- If the RxDMA goes to SUSPEND state because the descriptors are not available, a major failure occurs (you are not able to free the filled-up descriptors or buffers). If this issue does not rectify immediately, frames will be lost because of an RxFIFO overflow. Therefore, you can create a new descriptor list and program the RxDMA to start using it immediately, without going into STOP state. 

## 75.19.7 Programming guidelines for multi-channel multi-queuing 

### 75.19.7.1 Transmit 

1. Program the transmit queue size in TQS field of MTL_TxQ[n]_Operation_Mode register. Based on the value programmed in TQS field, you can determine the queue size. 

In the transmit operation, the number of channels is equal to the number of the queues, because of this reason, the channel-to-queue mapping is fixed. 

2. Enable the queue in TXQEN in the corresponding MTL_TxQ[n]_Operation_Mode register to use the queue. In DMA configurations, enable the ST field of DMA_CH[n]_Tx_Con-trol register and corresponding TXQEN in MTL_TxQ[n]_Operation Mode register. 

3. Program the scheduling method in MTL_Operation_Mode[SCHALG]. 

4. Program MTL_TxQ[n]_Quantum_Weight register for DCB queue per the selected algorithm. In case of CBS algorithm in AVB queues program the MTL_TxQ[n]_ETS_Control, MTL_TxQ[n]_SendSlopeCredit, MTL_TxQ[n]_HiCredit, and MTL_TxQ[n]_LoCredit registers as required. 

5. Program the MAC_TxQ_Prty_Map0 register to assign a fixed priority to the queue, if DCB is enabled and PFC function is required. You can use this assigned priority to determine if the corresponding queue must stop transmitting packet on the basis of the received PFC packet. 

### 75.19.7.2 Receive 

1. Program the receive queue size in RQS field of MTL_RxQ[n]_Operation_Mode register. Determine the size of the queue, based on the value programmed in RQS field. 

2. Enable the receive queues 0 to 7 in the fields RXQ0EN to RXQ7EN in MAC_RxQ_Ctrl0 for AV or DCB. In DMA configurations, SR bit of statically or dynamically map DMA_CH[n]_Rx_Control register and the corresponding RXQ[n]_EN in MAC_RxQ_Ctrl0 is enabled. 

3. Based on these packet types MAC routes the receive packets to the receive queues : 

   - a. AV PTP packets: Based on the programming of MAC_RxQ_Ctrl1[PTPQ]. 

   - b. AV untagged control packets: Based on the programming of MAC_RxQ_Ctrl1[AVCPQ]. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4198 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

- c. Data center bridging (DCB) related link layer discovery protocol (LLDP) packets. Program DCBCPQ in MAC_RxQ_Ctrl1 to indicate MAC which queue should get the DCB packets. 

- d. VLAN tag priority field in VLAN tagged packets: Program PSRQ7-0 of the MAC_RxQ_Ctrl2 and MAC_RxQ_Ctrl3 register for routing the tagged packets based on the received packets USP (user priority) field to the receive queues 0 to 7. 

- e. Route the AV tagged control and data packets based on PSRQ field of MAC_RxQ_Ctrl2 and MAC_RxQ_Ctrl3 registers. 

~~<mark>NOTE</mark>~~ 

The priorities set in PSRQ7-0 must be unique. 

4. If multiple receive DMA channels are enabled, you must perform the following programming for proper arbitration and mapping: 

   - a. Program MTL_Operation_Mode[RAA] to select the arbitration algorithm to decide which RxQ is read out from the RxFIFO memory. 

   - b. Program the MTL_RxQ[n]_Control register to decide the weights and the packet arbitration for each RxQ. 

   - c. If you program the static mapping in MTL_RxQ_DMA_Map[n] register (RXQ[n]DADMACH becomes 0), fields RXQx2DMA and others are programmed to select the channel to map each queue. 

   - d. Write 1 to RXQ[n]DADMACH field in MTL_RxQ_DMA_Map0 to select the dynamic mapping of packets in each receive queue. 

   - e. In dynamic channel mapping, the value of DCS field in the lowest MAC address registerthe decides the routing of a packet to a specific RxDMA channel. 

### 75.19.7.2.1 Programming guidelines for recovering from DMA channel failure 

When the DMA channel issues a bus error, follow these steps to recover from the failure. 

Recovering from the receive DMA channel failure. 

Perform these steps if you get bus error in the receive DMA channel: 

1. Write 1 to DMA_CH0_Rx_Control[RPF]. This flushes all the packets one after the other. 

This step is optional. However, writing 1 to this field prevents head-of-line blocking in the receive queues when packets sent to the RXDMA are stopped due to the bus error. 

2. Re-program the specific registers of the DMA channel. 

3. Start the DMA channel. 

Recovering from the transmit DMA channel failure. 

1. Stop the specific DMA channel, even if it is in active state. 

2. Flush the corresponding MTL queue. 

3. Re-program the specific registers of the DMA channel. 

4. Start the DMA channel. 

~~<mark>NOTE</mark>~~ 

Due to the known limitations in the design, reprogramming the DMA channel registers might not be always successful in recovering from a bus error. If the module is not fully functional after reprogramming the DMA, you can issue a soft reset to recover from the bus error. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4199 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## 75.19.8 Programming guidelines for GMII link state transitions 

### 75.19.8.1 Transmit and receive clocks running when link down 

Perform these steps when the link is down but the transmit and receive clocks are running: 

~~<mark>NOTE</mark>~~ The steps are provided for channel 0. 

1. Write 0 to bit 0 (ST) of DMA_CH(#i)_TX_Control (for i = 0; i <= DWC_EQOS_NUM_DMA_TX_CH-1) register to disable the transmit DMA (if applicable). 

2. Write 0 to MAC_Configuration[RE] to disable the MAC receiver. 

3. Wait for any previous frame transmissions to complete. You can check this by reading the appropriate fields of MTL_TxQ0_Debug (MTL_TxQ0_Debug[TRCSTS] is not 01) or, flush the Tx FIFO for faster empty operation. 

4. Write 0 to MAC_Configuration[TE] to disable the MAC transmitter. 

5. Make sure that both the transit queue and receive queue are empty (MTL_TxQ0_Debug[TXQSTS] and MTL_RxQ0_Debug[RXQSTS] are 0). 

6. Read the PHY registers to know the latest configuration and accordingly program the MAC registers, after the link is up. 

7. Start the transit DMA to restart the operation, and then enable the MAC transmitter and receiver. 

You do not disable the receive DMA because the receiver is disabled and the FIFO does not get any data in the receive FIFO. 

### 75.19.8.2 Transmit and receive clocks stopped when link down 

Perform these steps when the link is down and the transmit and receive clocks are stopped: 

- ~~<mark>NOTE</mark>~~ 

The steps are provided for channel 0. 

1. Write 0 to MAC_Configuration[RE] and MAC_Configuration[TE] to disable the MAC transmitter and receiver. This does not take effect immediately as the clocks are absent. 

2. Wait until the link is up and the clocks are restored. 

3. Wait for the transfer of any partial frame, if any to complete at time of stopping of the transmit or receive clock. To check this, read MAC_Debug (should be all-zero). Some old packets may still remain in the TXFIFO because the MAC transmitter is stopped. 

4. Read the PHY registers to know the latest operating mode and accordingly program the MAC registers. 

5. Write 1 to MAC_Configuration[RE] and MAC_Configuration[TE] to restart the MAC transmitter and receiver. 

## 75.19.9 Programming guidelines for IEEE 1588 timestamping 

### 75.19.9.1 Initialization guidelines for system time generation 

Write 1 MAC_Timestamp_Control[TSENA] to enable the timestamp feature. However, it is essential to initialize the timestamp counter after MAC_Timestamp_Control[TSENA] = 1. Perform these steps during the module initialization: 

1. Write 0 to the bit 16 of MAC_Interrupt_Enable to mask the timestamp trigger interrupt. 

2. Write 1 to MAC_Timestamp_Control[TSENA] to enable timestamping. 

3. Program MAC_Sub_Second_Increment based on the PTP clock frequency. 

4. Program MAC_Timestamp_Addend and write 1 to MAC_Timestamp_Control[TSADDREG], if you are using the fine correction approach. 

5. Poll MAC_Timestamp_Control until MAC_Timestamp_Control[TSADDREG] = 0. 

6. Program MAC_Timestamp_Control[TSCFUPDT] to select the fine update method (if required). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4200 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

7. Program MAC_System_Time_Seconds_Update and MAC_System_Time_Nanoseconds_Update with the appropriate time value. 

8. Write 1 to MAC_Timestamp_Control[TSINIT]. 

9. Initialize the timestamp counter with the value written in the timestamp update registers so that the timestamp counter can start operation. If one-step timestamping is enabled 

   - a. Program Bit 27 of the TDES3 context descriptor, to enable one-step timestamping. 

   - b. Program MAC_Timestamp_Ingress_Asym_Corr and MAC_Timestamp_Egress_Asym_Corr to update the correction field in PDelay_Req PTP messages. 

10. Enable the MAC receiver and transmitter for proper timestamping. 

~~<mark>NOTE</mark>~~ 

If the timestamp operation is disabled by writing 0 to MAC_Timestamp_Control[TSENA], repeat all these steps to restart the timestamp operation. 

### 75.19.9.2 System time correction 

### 75.19.9.2.1 Coarse correction method 

Perform these steps to synchronize or update the system time in one process (coarse correction method): 

1. Set the offset (positive or negative) in the timestamp registers that is MAC_System_Time_Seconds_Update and MAC_System_Time_Nanoseconds_Update. 

2. Write 1 to MAC_Timestamp_Control[TSUPDT]. 

The value in the timestamp update registers is added to or subtracted from the system time when MAC_Timestamp_Control[TSUPDT] = 0. 

### 75.19.9.2.2 Fine correction method 

Perform these steps to synchronize or update the system time to reduce system-time jitter (fine correction method): 

1. Calculate the rate by which you want to increment the system time slower or faster, with the help of the algorithm. 

2. Update MAC_Timestamp_Addend with the new value and write 1 to MAC_Timestamp_Control[TSADDREG]. 

3. Wait for the time for which you want the new value of the addend register to be active. You can do this by enabling the timestamp trigger interrupt after the system time reaches the target value. 

4. Program the required target time in MAC_PPS[n]_Target_Time_Seconds register and 

MAC_PPS[n]_Target_Time_Nanoseconds register. 

5. Enable the timestamp interrupt in MAC_Interrupt_Enable[TSIE]. 

6. Write 1 to bit 4 in MAC_Timestamp_Control. 

7. Read MAC_Interrupt_Status when this trigger causes an interrupt. 

8. Reprogram MAC_Timestamp_Addend with the old value and write 1 to MAC_Timestamp_Control[TSADDREG] again. 

## 75.19.10 Programming guidelines for AV feature 

After you enable the AV feature in the module controller, follow these programming tasks: 

- Initializing the DMA for QOS-AHB configurations only 

- Enabling slot number checking 

- Enabling average bits per slot reporting 

- Disabling flow control for AV-enabled queues (transmit and receive flow control) 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4201 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

### 75.19.10.1 Initializing the DMA in audio video feature 

The first step to program the AV feature in a QOS-AHB configuration is to initialize the DMA. 

Use this initialization sequence for QOS-AHB/QOS-AXI/QOS-AXI4 configurations with AV feature. 

1. Provide a software reset to reset all the QOS internal registers and logic (DMA_Mode[SWR]). 

2. Wait for the reset process to complete. Poll DMA_Mode[SWR], which clears only after the reset operation completes. 

3. Set the values in DMA_Mode to program the fields to initialize the DMA register. 

4. Create a descriptor list for transmit and receive. In addition, ensure that the DMA owns the transmit and receive descriptors. When you use OSF mode, at least two transmit descriptors are required. 

See Descriptors for more information about descriptors. 

5. Ensure that you create three or more different transmit or receive descriptors in the list before reusing any descriptors. 

6. Program the transmit and receive ring length registers (DMA_CH(#i)_TxDesc_Ring_Length (for i = 0; i <= DWC_EQOS_NUM_DMA_TX_CH-1) and DMA_CH(#i)_RxDesc_Ring_Length (for i = 0; i <= DWC_EQOS_NUM_DMA_RX_CH-1)). The ring length programmed must be at least 4. 

7. Initialize receive and transmit descriptor list address with the base address of the transmit and receive descriptor (DMA_CH(#i)_TxDesc_List_Address (for i = 0; i <= DWC_EQOS_NUM_DMA_TX_CH-1), DMA_CH(#i)_TxDesc_List_Address (for i = 0; i <= DWC_EQOS_NUM_DMA_TX_CH-1)). In addition, you must program the transmit and receive tail pointer registers to indicate the DMA about the available descriptors (DMA_CH(#i)_TxDesc_Tail_Pointer (for i = 0; i <= DWC_EQOS_NUM_DMA_TX_CH-1) and DMA_CH(#i)_RxDesc_Tail_Pointer (for i = 0; i <= DWC_EQOS_NUM_D-MA_RX_CH-1)). 

8. Program these fields to initialize the mode of operation in MTL_TxQ0_Operation_Mode: 

a. MTL_TxQ0_Operation_Mode[TSF] 

- b. MTL_TxQ0_Operation_Mode[TTC] 

c. MTL_TxQ0_Operation_Mode[TXQEN] to value 2‘b10 to enable transmit queue0 

- d. MTL_TxQ0_Operation_Mode[TQS] 

9. Enable the interrupts by programming DMA_CH(#i)_Interrupt_Enable (for i = 0; i <= DWC_EQOS_NUM_DMA_TX_CH-1) register. 

10. Repeat steps 4 through 9 for all the additional channels of AV feature. 

11. Program the AV queues CBS control register, idleSlope, sendSlope, hiCredit, and loCredit registers. 

12. Write 1 to bit 0 of DMA_CH(#i)_TX_Control (for i = 0; i <= DWC_EQOS_NUM_DMA_TX_CH-1) and DMA_CH(#i)_RX_Control (for i = 0; i <= DWC_EQOS_NUM_DMA_RX_CH-1) register to start the receive and transmit DMA. 

### 75.19.10.2 Enabling slot number checking 

You can enable slot number checking feature if you specifies the intervals at which the DMA channels map to AV queues fetch the frames from the AHB/AXI system bus. 

You must complete these steps after step 11 and before step 12 of Initializing the DMA in audio video feature . 

You can use the slot number check feature to specify the intervals at which the DMA channels map to AV queues fetch the frames from the AHB/AXI system bus. This feature is useful for an uniform and periodic transfer of the AV traffic from the host memory and it is available only when you enable timestamping and programs MAC_Sub_Second_Increment. Perform these steps to enable the slot number checking: 

1. Follow the steps described in Initialization guidelines for system time generation to enable timestamping. 

2. Ensure that the SLOTNUM field (bits 22:19) of TDES3 normal descriptor (Read format) contains a valid slot number. You can read the current reference slot number from the DMA_CH(#i)_Slot_Func-tion_Control_Status (for i = 0; i <= DWC_EQOS_NUM_DMA_TX_CH-1) register. 

3. Write 1 to bit 0 (ESC) of the slot function control and status register of a channel to enable the slot number checking. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4202 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

### 75.19.10.3 Enabling average bits per slot reporting 

You can enable the reporting of average bits transmitted in a slot. 

The CBS status register of the additional AV channels provide information about the average bits that are transmitted in a slot. You can asynchronously read this register to retrieve information about the average bits transmitted per slot. Perform these steps to enable average bits per slot reporting: 

1. Follow the steps as described in the Initialization guidelines for system time generation to enable timestamping. 

2. Program SLC bits [6:4], of the MTL_TxQ[n]_ETS_Control register of a channel with the number of slots over which the average transmitted bits per slot are computed. 

3. Enable bit 9(ABPSSIE) of the MTL_Q[n]_Interrupt_Control_Status register of a channel to generate the average bits per 

slot interrupt. 

      - ~~<mark>NOTE</mark>~~ 

   - The frequency of this interrupt depends on the value programmed in step 2. For example, when you program value 0 in the SLC field, the interrupt generates at every 125 microsecond. 

   - You can disable this interrupt to stop the interrupt flooding, when it is not required. 

4. Read ABS bits [16:0], of the MTL_TxQ[n]_ETS_Status register of a channel on each interrupt. 

~~<mark>NOTE</mark>~~ 

You can read the ABS fields in the polling mode even if ABPSIE bit is not enabled. When bit 1 (ABPSIS) of the MTL_TxQ[n]_ETS_Status register is 1, it indicates that a new value is updated in the ABS field. 

### 75.19.10.4 Disabling flow control for AV enabled queues 

### 75.19.10.4.1 Transmit flow 

Program the EHFC (Enable Hardware Flow Control) field of the corresponding receive queue's MTL_RxQ[n]_Operation_Mode register to 0. 

### 75.19.10.4.2 Receive flow control 

Program PSTQ[n] field, corresponding to AV enabled transit queue in MAC_TxQ_Prty_Map0/1 register to 0. 

### 75.19.10.5 Programming guidelines for flexible pulse-per-second output 

After you enable the flexible pulse-per-second output feature in the module controller, you can perform these tasks: 

- Generating single pulse on PPS 

- Generating next pulse on PPS 

- Generating a pulse train on PPS 

- Generating an interrupt without affecting the PPS 

### 75.19.10.5.1 Generating single pulse on PPS 

Perform these steps to generate single pulse on PPS: 

1. Program 11 or 10 (for interrupt) in TRGTMODSEL bits [6:5], of MAC_PPS_Control. This instructs MAC to use the target time registers (MAC_PPS0_Target_Time_Seconds and MAC_PPS0_Target_Time_Nanoseconds) for a start time of the PPS signal output. 

2. Program the start time value in the target time registers (MAC_PPS0_Target_Time_Seconds and MAC_PPS0_Target_Time_Nanoseconds). 

3. Program the PPS signal output width in MAC_PPS(#i)_Width (for i = 0; i <= 3) register. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4203 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

4. Program PPSCMD bits [3:0], of MAC_PPS_Control to 0001. This instructs MAC to generate single pulse on the PPS signal output at the time programmed in the target time registers. 

### 75.19.10.5.2 Generating next pulse on PPS 

When the PPSCMD is executed (PPSCMD bits = 0), you can give the cancel start command (PPSCMD=0011) before the programmed start time elapses to cancel the pulse generation. You can also program the behavior of the next pulse in advance. 

Follow these steps to program the next pulse: 

1. Program the start time for the next pulse in the target time registers. This time must be more than the time at which the falling edge occurs for the previous pulse. 

2. Program the next PPS signal output width in MAC_PPS(#i)_Width (for i = 0; i <= DWC_EQOS_PPS_OUT_NUM-1) register. 

3. Program PPSCMD bits [3:0], of MAC_PPS_Control to generate a single pulse after the time at which the previous pulse is de-asserted. This instructs MAC to generate single pulse on the PPS signal output, at the time programmed in target time registers. 

If you give this command before the previous pulse becomes low, then the new command overwrites the previous command and the QOS may generate only 1 extended pulse. 

### 75.19.10.5.3 Generating a pulse train on PPS 

Perform these steps to generate a pulse train on PPS: 

1. Program 11 or 10 (for interrupt) in TRGTMODSEL bits [6:5] , of MAC_PPS_Control. This instructs MAC to use the target time registers for the start time of the PPS signal output. 

2. Program the start time value in the target time registers. 

3. Program the interval value between the train of pulses on the PPS signal output in MAC_PPS(#i)_Interval (for i = 0; i <= DWC_EQOS_PPS_OUT_NUM-1) register. 

4. Program the PPS signal output width in MAC_PPS(#i)_Width (for i = 0; i <= DWC_EQOS_PPS_OUT_NUM-1) register. 

5. Program PPSCMD bits [3:0], of MAC_PPS_Control to 0010. This instructs MAC to generate train of pulses on the PPS signal output with start time programmed in target time registers. 

By default, the PPS pulse train is free-running unless the STOP pulse train at time or STOP pulse train immediately commands stop it. 

6. Program the stop value in the target time registers. Ensure that bit 31 (TSTRBUSY) of 

MAC_PPS(#i)_Target_Time_Nanoseconds (for i = 0; i <= DWC_EQOS_PPS_OUT_NUM-1) register becomes 0 before programming the target time registers again. 

7. Program PPSCMD field [bit 3:0] of MAC_PPS_Control to 0100. This stops the train of pulses on the PPS signal output after the programmed stop time specified in step 6 elapses. 

You can program 0101 in PPSCMD field [bit 3:0] of MAC_PPS_Control to stop the pulse train at any time. Similarly, you can program 0110 in PPSCMD field [bit 3:0] of MAC_PPS_Control before the time (programmed in step 6) elapses to cancel the stop pulse train command (given in Step 7). Also, program 0011 in PPSCMD field [bit 3:0] of MAC_PPS_Control before the programmed start time (in Step 2) elapses to cancel the pulse train generation. 

### 75.19.10.5.4 Generating an interrupt without affecting the PPS 

MAC_PPS_Control TRGTMODSEL bits [6:5] enables you to program the target time registers to perform any one of these actions: 

- Generate only interrupts. 

- Generate interrupts and the PPS start and stop time. 

- Generate only PPS start and stop time. 

Perform these steps to program the target time registers to generate only interrupt event: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4204 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

1. Program 00 (for interrupt) in MAC_PPS_Control TRGTMODSEL bits [6:5]. This instructs the MAC to use the target time registers for target time interrupt. 

2. Program a target time value in the target time registers. This instructs the MAC to generate an interrupt when the target time elapses. 

If TRGTMODSEL bits [6:5], are changed (for example, to control the PPS) then over-write the interrupt generation with the new mode and new programmed target time register value. 

### 75.19.10.6 Programming guidelines for VLAN filtering on receive 

Perform these steps to program VLAN filtering on receive: 

1. Program MAC_VLAN_Tag register for the following fields to select the filtering method: 

a. ETV: Enables 12-Bit VLAN tag comparison or 16-bit VLAN tag comparison. 

b. VTHM: VLAN tag hash table match enable. 

c. ERIVLT: Enables inner VLAN tag or outer VLAN Tag (to enable the inner or outer VLAN tag filtering, writing 1 to MAC_VLAN_Tag_Ctrl[EDVLP] enables the double VLAN processing). 

d. ERSVLM: Enables receive S-VLAN match or C-VLAN match (write 1 to MAC_VLAN_Tag_Ctrl[ESVL] to enable S- VLAN processing). 

e. DOVLTC: Ignores VLAN type for tag match 

f. VTIM: Enables VLAN tag inverse match instead of the normal VLAN tag matching 

2. Program VL of MAC_VLAN_Tag register for the 12-bit or 16-bit VLAN tag. 

3. Program MAC_VLAN_Hash_Table, if hash filtering of VLAN tag is enabled. When MAC_VLAN_Tag_Ctrl[ETV] becomes 0, it indicates that the upper 4 bits of the calculated CRC-32 of VLAN tag are inverted and index the content of MAC_VLAN_Hash_Table. When MAC_VLAN_Tag_Ctrl[ETV] is 1, it indicates that the upper 4 bits of calculated CRC-32 of VLAN Tag index the content of MAC_VLAN_Hash_Table. For example, when MAC_VLAN_Tag_Ctrl[ETV] is 1, a hash value of 4b'1000 selects bit 8 of MAC_VLAN_Hash_Table. When MAC_VLAN_Tag_Ctrl[ETV] becomes 0 a hash value of 4'b1000 selects bit 7 of MAC_VLAN_Hash_Table. 

### 75.19.10.7 Programming guidelines for extended VLAN filtering and routing on receive 

Perform these steps, for the indirect access of the per VLAN tag registers: 

- Write 

   - Write the required data into MAC_VLAN_Tag_Data. 

   - Program MAC_VLAN_Tag_Ctrl[OFS] with the required filter register's offset and command type to MAC_VLAN_Tag_Ctrl[CT]. For a write command, set this field to 0. 

   - Write 1 to MAC_VLAN_Tag_Ctrl[OB] and wait till it becomes 0 to do the next write. This will guarantee that you have programmed the appropriate VLAN Tag Filter register. 

- Read 

   - Program MAC_VLAN_Tag_Ctrl[OFS] with the required register's offset and command type to MAC_VLAN_Tag_Ctrl[CT]. For a read command, set this field to 1. 

   - Write 1 to MAC_VLAN_Tag_Ctrl[OB] and wait till it becomes 0. The appropriate value of the VLAN Tag Filter register is available in MAC_VLAN_Tag_Data. 

### 75.19.10.8 Programming sequence for queue/channel based VLAN inclusion register 

Perform these steps to program the queue/channel-based VLAN inclusion register: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4205 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

~~<mark>NOTE</mark>~~ 

When MAC_VLAN_Incl[CBTI] = 1 you cannot access the indirect VLAN include registers. 

1. Write 1 to MAC_VLAN_Incl[CBTI], to enable queue or channel based VLAN tag insertion on all the transmitted packets. This field must be 1 before any indirect access to the queue or channel specific MAC_VLAN_Incl(#i) register. 

2. Program the VLAN tag and VLAN type to insert in packets from a particular queue or channel in MAC_VLAN_Incl[VLT] and MAC_VLAN_Incl[CSVL], corresponding offset address in ADDR field (0 for queue/channel 0, 1 for queue/channel 1, and so on) must be set. Write 0 to MAC_VLAN_Incl[RDWR] to indicate write access. The write to byte 0 (byte 3 in Big Endian mode) of MAC_VLAN_Incl initiates access to indirect access MAC_VLAN_Incl(#i) register. 

3. Write 1 to MAC_VLAN_Incl[BUSY] via the module to indicate the progress of access to indirect access MAC_VLAN_Incl(#i) register. After the access completes, MAC_VLAN_Incl[BUSY] = 0. The application must not attempt subsequent access to MAC_VLAN_Incl(#i) register when the MAC_VLAN_Incl[BUSY] is 1. 

4. Repeat step 2 and step 3 to program VLAN tag and VLAN type to insert in packets from the remaining queues or channels. The application must ensure that the required VLAN tag and VLAN type for all the queues or channels are programmed, otherwise an unintended VLAN tag and VLAN type might be inserted. 

## 75.19.11 Programming guidelines for EST 

Program the gate control values and time intervals in MTL_EST_Status[SWOL] along with the other EST related registers that are described in GMAC register descriptions to appropriate values. The upcoming sub-sections provide step by step details for programming the GCL and the other EST related registers. 

### 75.19.11.1 Programming the GCL and GCL linked registers 

Perform these steps to program the GCL and the four other registers implemented per GCL: 

1. Access the GCL and the four other GCL-linked registers via indirect addressing using MTL_EST_GCL_Control and MTL_EST_GCL_Data. MTL_EST_Status[SWOL] indicates whether the software owns GCL0 or GCL1. 

2. Write the 32-bit write data to MTL_EST_GCL_Data, to program the GCL. Then program MTL_EST_GCL_Control to write the write address and other control information. 

3. In MTL_EST_GCL_Data, write data consists of up to 8 bits (configurable) of gate controls and up to 24 bits (configurable) of time interval. Programming a 0 indicates gate close and programming a 1 indicates gate open. For a 4-TC and 20-bit time interval configuration, the data width is 24-bits and the remaining 8-bits are reserved/read-only. You must write the data in the following format. 

{8'h0, TC3, TC2, TC1, TC0, 20-bit Time Interval} where TCx = 0 or 1. 

4. Program MTL_EST_GCL_Control[SRWO] to 1 (to start a Write Op) and program the address and R/W fields appropriately. 

5. Poll and check that the hardware clears MTL_EST_GCL_Control[SRWO] to indicate that the previous operation completes before initiating a new read-write operation via the same indirect addressing mode. 

6. Repeat steps 3, 4, 5 until the programming of the GCL completes. 

7. Program the BTR, CTR, TER and LLR registers, using the same indirect addressing method as described above. Write 1 to MTL_EST_GCL_Control[GCRR] appropriately. MTL_EST_GCL_Control[GCRR] interprets the address field as belonging to these registers (instead of the GCL). 

After the GCL and the related registers are programmed, program MTL_EST_GCL_Control to allow hardware to own and process the GCL. When the list length (as indicated in LLR) is 1, the associated time interval must be smaller than the cycle time register value. Otherwise, an error is reported (as described in the Error handling section) as a single set of gate controls add no value in the TSN context. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4206 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

~~<mark>NOTE</mark>~~ 

The time unit in all the GCL related registers is seconds and nanoseconds. In cases where internally generated PTP system time is used, you must program the nanoseconds field to use the Digital Rollover mode. (The value of MAC_Timestamp_Control[TSCTRLSSR]must be 1) 

### 75.19.11.2 Programming the EST registers 

After the steps mentioned in "Programming the GCL and GCL Linked Registers" completes, program MTL_EST_Control 

1. Write 1 to MTL_EST_Control[CTOV] and MTL_EST_Control[TILS]. Also, write 1 to MTL_EST_Control[EEST] and MTL_EST_Control[SWOL]. 

~~<mark>NOTE</mark>~~ 

The CTOV recommendations for GMII for SPRAM configurations are: 

- 96 * Tx clock period, for 32 and 64 bit data width configurations. 

- 128 * Tx clock period for 128 bit data width configurations. 

The CTOV recommendations for GMII for non-SPRAM configurations are: 

   - 30 * Tx clock period, when SA/VLAN insertion is enabled. 

   - 22 * Tx clock period, when SA/VLAN insertion is not enabled. 

2. Enables the hardware to own and process the new GCL and make a switch to the new GCL at the BTR value. The hardware provides an interrupt (if enabled) when the switch to the new list happens. 

3. Performs an appropriate action to address any other interrupts (explained in the Inter-rupts section) received during the hardware execution of the GCL. 

Write 1 to MTL_EST_Control[SSWL] to handoff to hardware. Software is not allowed to write to the GCL and GCL linked registers when MTL_EST_Control[SSWL] = 1, because the hardware might be using the new GCL. 

The hardware resets or clears MTL_EST_Control[SSWL] when it successfully switches to the new list. The hardware also flips MTL_EST_Status[SWOL] to indicate the new GCL that the software owns. 

Program the GCL that software owns (MTL_EST_Status[SWOL] indicates) as described in "Programming the GCL and GCL Linked Registers" and then program MTL_EST_Control as described above, to install a new GCL. Ensure that the new BTR is set to an appropriate value to avoid BTR Error that may require software intervention in some cases. 

The packet length (frame size) information must be available at all times, to avoid transmission overruns. Therefore, in the DMA configurations, program the packet length in the first descriptor of every transmit frame. Similarly, in the MTL configuration, provide the packet length in the control word. 

~~<mark>NOTE</mark>~~ 

The packet length provided in the transmit descriptor must account for the SA and VLAN insertion, to avoid transmission overruns, if applicable, that is, packet length must represent the actual packet length on the Ethernet line. 

## 75.19.12 Programming the launch time in time-based scheduling 

Configure the launch time in the enhanced normal transmit descriptors in DMA configurations and is driven as a control word in MTL configurations as follows: 

The OSTC and launch time features are mutually exclusive and must not be used together. In case of a conflict (if OSTC = LTV = 1 in MTL configuration), give priority to OSTC and ignore the launch time. 

In DMA configuration, if a context descriptor is received with a valid OSTC values immediately before receiving a first normal descriptor with LTV = 1, then the LTV is ignored. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4207 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## 75.19.13 Programming guidelines for media clock generation and recovery 

### 75.19.13.1 Programming guidelines for media clock generation 

These are the guidelines for the media clock generation: 

1. Program the appropriate presentation time control (supported generation modes "1001-1011" ) to PPSCTRL_PPSCMD ( for 0th instance)/PPSCMD#i (for 1,2,3 instances) of MAC_PPS_Control, to define the PPS instance in Media clock generation mode. 

2. Based on the selected PPS instance, application must drive the appropriate trigger signal to the corresponding mcg_pst_trig_i[#i]. 

3. Based on the programmed mode, DUT captures the timestamp and programs it in the MAC_PPS(#i)_Target_Time_Seconds register. Then, mcgr_dma_req_o[#i] is set. 

4. For every request which DUT generates, the module reads the corresponding MAC_PPS(#i)_Target_Time_Seconds register and asserts the corresponding mcgr_d-ma_ack_i[#i] to acknowledge the read request. 

### 75.19.13.2 Programming guidelines for media clock recovery 

These are the guidelines for the media clock recovery: 

- Writing 1 to MAC_Timestamp_Control[PTGE] enables the CPT counter. In addition to configuring the initialization values for the system time, update MAC_Presn_Time_Updt with the equivalent presentation time initialization value, then MAC_Timestamp_Control[TSINIT] = 1. 

- Use the increment values for the system time and also for the CPT because the increment value is in sub-seconds and sub-nanoseconds. 

- Update MAC_Presn_Time_Updt with the equivalent presentation time update value (32 bit ns), when an update is requred, and also configure the updated values for the system time. Finally, MAC_Timestamp_Control[TSUPDT] must be 1 for the update. 

- Program the MCGREN#i field of MAC_PPS_Control to enable the PPS instance to operate in MCGR mode. 

- Program the appropriate presentation time control (supported recovery modes "0001 - 0011") to PPSCTRL_PPSCMD (for 0th instance) or PPSCMD#i (for 1,2,3 instances) of MAC_PPS_Control register, to set the PPS instance in Media clock recovery mode. 

- After the PPS instance is set in Recovery mode, DUT sets the corresponding mcgr_dma_req_o[#i]. For every request which DUT generates, program the target presentation time into the MAC_PPS(#i)_Target_Time_Seconds register and assert the corresponding mcgr_dma_ack_i[#i] to acknowledge the request. Acknowledgment can be given before/after programming the Target presentation time. 

- Observe the recovered media clock on the corresponding ptp_pps_o[#i]. 

## 75.19.14 Programming guidelines for ECC protection for memories 

These are the guidelines for the ECC protection for memories: 

- Write 1 to the appropriate field of MTL_ECC_Control to enable the ECC features for the respective memory. 

- Generate a correctable interrupt (sbd_sfty_ce_intr_o) or an uncorrectable interrupt (sbd_sfty_ue_intr_o) to indicate the application, if any correctable, uncorrectable, or address errors are detected. DMA_Interrupt_Status or MTL_ECC_Interrupt_Status indicates an appropriate status. 

- Provide debug mode for each memory to specify errors. 

~~<mark>NOTE</mark>~~ 

Enable the ECC feature before the traffic is online (or after the reset), otherwise the false interrupts may trigger. 

### 75.19.14.1 Programming guidelines for ECC hardware error injection (Debug mode) 

Follow these steps for ECC hardware error injection: 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4208 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

- Write 1 to the appropriate field in MTL_DBG_CTL to enable the ECC error injection feature for MTL TX/RX and DMA TSO. 

- Write 1 to the appropriate field in MTL_EST_GCL_Control to enable the ECC error injection feature for the EST memory. 

- Write 1 to the appropriate field in MTL_RXP_Indirect_Acc_Control_Status to enable the ECC error injection for the receive parser memory. To access the receive parser memory in Debug mode, write 0 to MTL_RXP_Indirect_Acc_Control_Status[FRPE] to disable the receive parser feature. 

- Ensure that all the CSR writes corresponding to one memory write must have the same value for the error injection control word, where multiple CSR writes are required for writing single data word into the memory. 

## 75.19.15 Programming guidelines for on-chip datapath parity protection 

Follow these steps for on-chip datapath parity protection: 

- Writing 1 to MTL_DPP_Control[EDPP] enables the parity generation and parity detection mismatch on datapath. 

- Generates an uncorrectable interrupt (sbd_sfty_ue_intr_o) to indicate the application if any parity mismatch is detected. DMA_Safety_Interrupt_Status or MTL_Safety_Interrupt_Status and MAC_DPP_FSM_Interrupt_Status indicates the appropriate status. 

- Supports Debug mode for each parity generator to insert an error. 

   - ~~<mark>NOTE</mark>~~ 

Enable the datapath parity protection before the receive or transit traffic starts, to avoid the false safety interrupts. 

## 75.19.16 Programming guidelines for FSM parity and timeout 

Follow these steps to configure the FSM parity and timeout: 

- Write 1 to MAC_FSM_Control[PRTYEN] and MAC_FSM_Control[TMOUTEN] to enable the FSM parity and timeout feature respectively. 

- Force the FSMs to enter into a state with even number of 1s and wait for the safety uncorrectable interrupt to define with MAC_DPP_FSM_Interrupt_Status[FSMPES] for a parity error detection. 

- Write 1 to the parity error injection using the [23:16] bits of MAC_FSM_Control to select the appropriate clock domain, for Error injection mode in FSM parity. Wait for the safety uncorrectable interrupt to be defined with MAC_DPP_FSM_Interrupt_Status[FSMPES]. 

- Configure the large and normal mode values which MAC_FSM_ACT_Timer[LTMRMD] and MAC_FSM_ACT_Timer[NTMRMD] indicates , for FSM timeouts. 

- Use the [31:24] bits of MAC_FSM_Control to select the large or normal mode tic generation per clock domain. 

- Write 1 to MAC_FSM_ACT_Timer[TMR] with the appropriate number of CSR clock cycles to generate 1us tic. 

- Force the FSM in a particular clock domain to remain in an active state for timeout duration (for example, T-2T). You can check the safety interrupt and the status field for the corresponding clock domain that sets in the [15:8] bits of the MAC_DPP_FSM_Interrupt_Status . 

- Select the appropriate clock domain for which timeout error injection must be set using the [15:8] bits of MAC_FSM_Control, for Error injection mode in FSM timeout. Wait for the safety uncorrectable interrupt to define with the corresponding error status in the MAC_DPP_FSM_Interrupt_Status . 

- Use only normal mode tic generation, for application or CSR interface timeout. On the basis of the time-outs of configured interface, appropriate fields (MSTTES, SLVTES) of MAC_DPP_FSM_Interrupt_Status is defined with the safety interrupt. 

# 75.20 Glossary 

AFM Address filtering module 

ARI Application receive interface 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4209 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

ATI Application transmit interface AVB Audio video bridging 

- AXI Advanced extensible interface BTR Base time register CPT Current presentation time CRC Cyclic redundancy check DA Destination address DCB Data center bridging 

- DUT Device under test 

- EOP End of packet 

- FCS A 32-bit cyclic redundancy check used to detect an in-transit corruption of data. Also marks the end of an Ethernet frame. 

- FIFO First in first out GCL Gate control list GMII Gigabit media independent interface MAC Media access controller MCI MAC control tnterface MDC Management data clock MDIO Management data input/output MII Media independent interface MRI MAC receive interface MTI MAC transmit interface MTL MAC transmit layer PBL Programmable burst length 

- PHY The physical interface transceiver that implements the OSI physical layer for an ethernet network. The IEEE 802.3 standard defines it. 

- RGMII Reduced gigabit media independent interface RMII Reduced media independent interface RMON Remote network monitoring 

SA Source address SFD Start frame delimiter SGMII Serial gigabit media independent interface SMA Station management agent TCP Transmission control protocol UDP User datagram protocol VLAN Virtual local area network 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4210 / 4640 

