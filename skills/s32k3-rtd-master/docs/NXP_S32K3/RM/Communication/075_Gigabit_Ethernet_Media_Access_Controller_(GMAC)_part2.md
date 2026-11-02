NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field<br>31-30<br>Reserved_31_3<br>0|Function<br>Reserved.|
|---|---|
|29-28<br>ASP|Automotive Safety Package Following are the encoding for the different Safety features<br>00b - No Safety features selected<br>01b - Only "ECC protection for external memory" feature is selected<br>10b - All the Automotive Safety features are selected without the "Parity Port Enable for external<br>interface" feature<br>11b - All the Automotive Safety features are selected with the "Parity Port Enable for external<br>interface" feature|
|27<br>TBSSEL|Time Based Scheduling Enable This bit is set to 1 when the Time Based Scheduling feature is selected.<br>0b - Time Based Scheduling Enable feature is not selected<br>1b - Time Based Scheduling Enable feature is selected|
|26<br>FPESEL|Frame Preemption Enable This bit is set to 1 when the Enable Frame preemption feature is selected.<br>0b - Frame Preemption Enable feature is not selected<br>1b - Frame Preemption Enable feature is selected|
|25-22<br>Reserved_25_2<br>2|Reserved.|
|21-20<br>ESTWID|Width of the Time Interval field in the Gate Control List This field indicates the width of the Configured<br>Time Interval Field<br>00b - Width not configured<br>01b - 16<br>10b - 20<br>11b - 24|
|19-17<br>ESTDEP|Depth of the Gate Control List This field indicates the depth of Gate Control list expressed as<br>Log2(DWC_EQOS_EST_DEP)-5<br>000b - No Depth configured<br>001b - 64<br>010b - 128<br>011b - 256<br>100b - 512<br>101b - 1024<br>110b - Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3700 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field<br>16<br>ESTSEL|Function<br>Enhancements to Scheduled Traffic Enable This bit is set to 1 when the Enable Enhancements to<br>Scheduling Traffic feature is selected.<br>0b - Enable Enhancements to Scheduling Traffic feature is not selected<br>1b - Enable Enhancements to Scheduling Traffic feature is selected|
|---|---|
|15<br>Reserved_15|Reserved.|
|14-13<br>FRPES|Flexible Receive Parser Table Entries size This field indicates the Max Number of Parser Entries<br>supported by Flexible Receive Parser.<br>00b - 64 Entries<br>01b - 128 Entries<br>10b - 256 Entries<br>11b - Reserved|
|12-11<br>FRPBS|Flexible Receive Parser Buffer size This field indicates the supported Max Number of bytes of the packet<br>data to be Parsed by Flexible Receive Parser.<br>00b - 64 Bytes<br>01b - 128 Bytes<br>10b - 256 Bytes<br>11b - Reserved|
|10<br>FRPSEL|Flexible Receive Parser Selected This bit is set to 1 when the Enable Flexible Programmable Receive<br>Parser option is selected.<br>0b - Flexible Receive Parser feature is not selected<br>1b - Flexible Receive Parser feature is selected|
|9<br>PDUPSEL|Broadcast/Multicast Packet Duplication This bit is set to 1 when the Broadcast/Multicast Packet<br>Duplication feature is selected.<br>0b - Broadcast/Multicast Packet Duplication feature is not selected<br>1b - Broadcast/Multicast Packet Duplication feature is selected|
|8-6|Reserved.|
|Reserved_7_6||
|5<br>DVLAN|Double VLAN Tag Processing Selected This bit is set to 1 when the Enable Double VLAN Processing<br>Feature is selected.<br>0b - Double VLAN option is not selected<br>1b - Double VLAN option is selected|
|4|Queue/Channel based VLAN tag insertion on Tx Enable This bit is set to 1 when the Enable Queue/<br>Channel based VLAN tag insertion on Tx Feature is selected.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3701 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|CBTISEL|0b - Enable Queue/Channel based VLAN tag insertion on Tx feature is not selected<br>1b - Enable Queue/Channel based VLAN tag insertion on Tx feature is selected|
|3|Reserved.|
|Reserved_3||
|2-0<br>NRVF|Number of Extended VLAN Tag Filters Enabled This field indicates the Number of Extended VLAN Tag<br>Filters selected:<br>000b - No Extended Rx VLAN Filters<br>001b - 4 Extended Rx VLAN Filters<br>010b - 8 Extended Rx VLAN Filters<br>011b - 16 Extended Rx VLAN Filters<br>100b - 24 Extended Rx VLAN Filters<br>101b - 32 Extended Rx VLAN Filters<br>110b - Reserved|



# 75.7.78 (MAC_DPP_FSM_Interrupt_Status) 

## Offset 

|Register|Offset|
|---|---|
|MAC_DPP_FSM_Interru|140h|
|pt_Status||



## Function 

This register contains the status of Automotive Safety related Data Path Parity Errors, Interface Timeout Errors, FSM State Parity Errors and FSM State Timeout Errors. All the non-Reserved bits are cleared on read. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3702-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv Reserv<br>R Reserved_31_29  e... MRWC MTFC MTBU FSMP Reserved_23_18  e... MSTT<br>PES  PES  PES  ES  ES<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv Reserv Reserv Reserv Reserv Reserv Reserv Reserv<br>R<br>e... e... e... PTES  ATES  e... RTES  TTES  e... e... ARPE MTSP MPES  RDPE e... e...<br>S  ES  S<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3702 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-29|Reserved.|
|Reserved_31_2<br>9||
|28<br>Reserved_DCP<br>ES|Reserved.|
|27<br>MRWCPES|MTL RWC data path Parity checker Error Status This filed when set indicates that, parity error is<br>detected on the MTL RWC data interface (or at PC12 as shown in Recieve data path parity protection<br>diagram).<br>0b - MTL RWC data path Parity checker Error Status not detected<br>1b - MTL RWC data path Parity checker Error Status detected|
|26<br>MTFCPES|MAC TFC data path Parity checker Error Status This filed when set indicates that, parity error is detected<br>on the MAC TFC data interface (or at PC11 as shown in Transmit data path parity protection diagram).<br>0b - MAC TFC data path Parity checker Error Status not detected<br>1b - MAC TFC data path Parity checker Error Status detected|
|25<br>MTBUPES|MAC TBU data path Parity checker Error Status This filed when set indicates that, parity error is detected<br>on the MAC TBU data interface (or at PC10 as shown in Transmit data path parity protection diagram).<br>0b - MAC TBU data path Parity checker Error Status not detected<br>1b - MAC TBU data path Parity checker Error Status detected|
|24<br>FSMPES|FSM State Parity Error Status This field when set indicates one of the FSMs State registers has a parity<br>error detected.<br>0b - FSM State Parity Error Status not detected<br>1b - FSM State Parity Error Status detected|
|23-18|Reserved.|
|Reserved_23_1<br>8||
|17|Reserved.|
|Reserved_SLV<br>TES||
|16<br>MSTTES|Master Read/Write Timeout Error Status This field when set indicates that an Application/CSR Timeout<br>has occurred on the master (AXI/AHB/ARI/ATI) interface.<br>0b - Master Read/Write Timeout Error Status not detected<br>1b - Master Read/Write Timeout Error Status detected|
|15|Reserved.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3703 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|Reserved_RVC<br>TES||
|14|Reserved.|
|Reserved_R125<br>ES||
|13|Reserved.|
|Reserved_T125<br>ES||
|12<br>PTES|PTP FSM Timeout Error Status This field when set indicates that one of the PTP FSM Timeout has<br>occurred.<br>0b - PTP FSM Timeout Error Status not detected<br>1b - PTP FSM Timeout Error Status detected|
|11<br>ATES|APP FSM Timeout Error Status This field when set indicates that one of the APP FSM Timeout has<br>occurred.<br>0b - APP FSM Timeout Error Status not detected<br>1b - APP FSM Timeout Error Status detected|
|10<br>Reserved_CTE<br>S|Reserved.|
|9<br>RTES|Rx FSM Timeout Error Status This field when set indicates that one of the Rx FSM Timeout has<br>occurred.<br>0b - Rx FSM Timeout Error Status not detected<br>1b - Rx FSM Timeout Error Status detected|
|8<br>TTES|Tx FSM Timeout Error Status This field when set indicates that one of the Tx FSM Timeout has<br>occurred.<br>0b - Tx FSM Timeout Error Status not detected|
||1b - Tx FSM Timeout Error Status detected|
|7|Reserved.|
|Reserved_ASR<br>PES||
|6|Reserved.|
|Reserved_CWP<br>ES||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3704 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|5<br>ARPES|Application Receive interface data path Parity Error Status This bit when set indicates that a parity<br>error is detected at the following checkers based on the system configuration: - In MTL configuration<br>(DWC_EQOS_SYS=1), parity checker (PC6 as shown in Receive Data path Parity protection diagram)<br>at ARI interface. - In DMA configuration (DWC_EQOS_SYS=2), parity checker (PC6 as shown in<br>Receive Data path Parity protection diagram) at DMA application interface. - In AHB configuration<br>(DWC_EQOS_SYS=3), parity checker (PC6 as shown in Receive Data path Parity protection diagram)<br>at AHB master interface. - In AXI configuration (DWC_EQOS_SYS=4), parity checker (PC6 as shown in<br>Receive Data path Parity protection diagram) at AXI master interface.<br>0b - Application Receive interface data path Parity Error Status not detected<br>1b - Application Receive interface data path Parity Error Status detected|
|4<br>MTSPES|MTL TX Status data path Parity checker Error Status This filed when set indicates that, parity error is<br>detected on the MTL TX Status data on ati interface (or at PC5 as shown in Transmit data path parity<br>protection diagram).<br>0b - MTL TX Status data path Parity checker Error Status not detected<br>1b - MTL TX Status data path Parity checker Error Status detected|
|3<br>MPES|MTL data path Parity checker Error Status This bit when set indicates that a parity error is detected<br>at the MTL transmit write controller parity checker (or at PC4 as shown in Transmit data path parity<br>protection diagram).<br>0b - MTL data path Parity checker Error Status not detected<br>1b - MTL data path Parity checker Error Status detected|
|2<br>RDPES|Read Descriptor Parity checker Error Status This bit when set indicates that a parity error is detected<br>at the DMA Read descriptor parity checker (or at PC3 as shown in Transmit data path parity protection<br>diagram).<br>0b - Read Descriptor Parity checker Error Status not detected<br>1b - Read Descriptor Parity checker Error Status detected|
|1<br>Reserved_TPE<br>S|Reserved.|
|0|Reserved.|
|Reserved_ATP<br>ES||



# 75.7.79 (MAC_FSM_Control) 

## Offset 

|Register|Offset|
|---|---|
|MAC_FSM_Control|148h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3705 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Function 

This register is used to control the FSM State parity and timeout error injection in Debug mode. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3706-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv Reserv Reserv Reserv Reserv Reserv Reserv Reserv<br>R e... e... e... PLGR ALGR e... RLGR TLGR e... e... e... PPEIN  APEIN  e... RPEIN  TPEIN<br>NML  NML  NML  NML<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv Reserv Reserv Reserv<br>R e... e... e... PTEIN  ATEIN  e... RTEIN  TTEIN  Reserved_7_2  PRTY TMOU<br>EN  TEN<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31|Reserved.|
|Reserved_RVC<br>LGRNML||
|30|Reserved.|
|Reserved_R125<br>LGRNML||
|29|Reserved.|
|Reserved_T125<br>LGRNML||
|28<br>PLGRNML|PTP Large/Normal Mode Select This field when set indicates that large mode tic generation is used for<br>PTP domain, else normal mode tic generation is used.<br>0b - normal mode tic generation is used for PTP domain<br>1b - large mode tic generation is used for PTP domain|
|27<br>ALGRNML|APP Large/Normal Mode Select This field when set indicates that large mode tic generation is used for<br>APP domain, else normal mode tic generation is used.<br>0b - normal mode tic generation is used for APP domain<br>1b - large mode tic generation is used for APP domain|
|26|Reserved.|
|Reserved_CLG<br>RNML||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3706 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|25<br>RLGRNML|Rx Large/Normal Mode Select This field when set indicates that large mode tic generation is used for Rx<br>domain, else normal mode tic generation is used.<br>0b - normal mode tic generation is used for Rx domain<br>1b - large mode tic generation is used for Rx domain|
|24<br>TLGRNML|Tx Large/Normal Mode Select This field when set indicates that large mode tic generation is used for Tx<br>domain, else normal mode tic generation is used.<br>0b - normal mode tic generation is used for Tx domain<br>1b - large mode tic generation is used for Tx domain|
|23|Reserved.|
|Reserved_RVC<br>PEIN||
|22|Reserved.|
|Reserved_R125<br>PEIN||
|21|Reserved.|
|Reserved_T125<br>PEIN||
|20<br>PPEIN|PTP FSM Parity Error Injection This field when set indicates that Error Injection for PTP FSM Parity is<br>enabled.<br>0b - PTP FSM Parity Error Injection is disabled<br>1b - PTP FSM Parity Error Injection is enabled|
|19<br>APEIN|APP FSM Parity Error Injection This field when set indicates that Error Injection for APP FSM Parity is<br>enabled.<br>0b - APP FSM Parity Error Injection is disabled<br>1b - APP FSM Parity Error Injection is enabled|
|18|Reserved.|
|Reserved_CPEI<br>N||
|17<br>RPEIN|Rx FSM Parity Error Injection This field when set indicates that Error Injection for RX FSM Parity is<br>enabled.<br>0b - Rx FSM Parity Error Injection is disabled<br>1b - Rx FSM Parity Error Injection is enabled|
|16<br>TPEIN|Tx FSM Parity Error Injection This field when set indicates that Error Injection for TX FSM Parity is<br>enabled.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3707 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Tx FSM Parity Error Injection is disabled<br>1b - Tx FSM Parity Error Injection is enabled|
|15|Reserved.|
|Reserved_RVC<br>TEIN||
|14|Reserved.|
|Reserved_R125<br>TEIN||
|13|Reserved.|
|Reserved_T125<br>TEIN||
|12<br>PTEIN|PTP FSM Timeout Error Injection This field when set indicates that Error Injection for PTP FSM timeout<br>is enabled.<br>0b - PTP FSM Timeout Error Injection is disabled<br>1b - PTP FSM Timeout Error Injection is enabled|
|11<br>ATEIN|APP FSM Timeout Error Injection This field when set indicates that Error Injection for APP FSM timeout<br>is enabled.<br>0b - APP FSM Timeout Error Injection is disabled<br>1b - APP FSM Timeout Error Injection is enabled|
|10|Reserved.|
|Reserved_CTEI<br>N||
|9<br>RTEIN|Rx FSM Timeout Error Injection This field when set indicates that Error Injection for RX FSM timeout is<br>enabled.<br>0b - Rx FSM Timeout Error Injection is disabled<br>1b - Rx FSM Timeout Error Injection is enabled|
|8<br>TTEIN|Tx FSM Timeout Error Injection This field when set indicates that Error Injection for TX FSM timeout is<br>enabled.<br>0b - Tx FSM Timeout Error Injection is disabled<br>1b - Tx FSM Timeout Error Injection is enabled|
|7-2|Reserved.|
|Reserved_7_2||
|1|This bit when set indicates that the FSM parity feature is enabled.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3708 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|PRTYEN|0b - FSM Parity feature is disabled|
||1b - FSM Parity feature is enabled|
|0|This bit when set indicates that the FSM timeout feature is enabled.|
|TMOUTEN|0b - FSM timeout feature is disabled|
||1b - FSM timeout feature is enabled|



# 75.7.80 (MAC_FSM_ACT_Timer) 

## Offset 

|Register|Offset|
|---|---|
|MAC_FSM_ACT_Timer|14Ch|



## Function 

This register is used to select the FSM and Interface Timeout values. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||Reserved|_31_24|||||LTM|RMD|||NTM|RMD||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||Reserve|d_15_10|||||||TM|R|||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-24|Reserved.|
|Reserved_31_2<br>4||
|23-20<br>LTMRMD|Large Mode Timeout Value This field provides the mode value to be used for large mode FSM and other<br>interface time outs. The timeout duration is based on the mode value.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3709 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||0000b - Timer disabled<br>0001b - 1us<br>0010b - 1.024ms (~4ms)<br>0011b - 16.384ms (~16ms)<br>0100b - 65.536ms (~64ms)<br>0101b - 262.144ms (~256ms)<br>0110b - 1.048sec (~1sec)<br>0111b - 4.194sec (~4sec)<br>1000b - 16.777sec (~16sec)<br>1001b - 33.554sec (~32sec)<br>1010b - 67.108sec (~64sec)<br>1011b - Reserved|
|19-16<br>NTMRMD|Normal Mode Timeout Value This field provides the value to be used for normal mode FSM and other<br>interface time outs. The timeout duration is based on the mode value.<br>0000b - Timer disabled<br>0001b - 1us<br>0010b - 1.024ms (~4ms)<br>0011b - 16.384ms (~16ms)<br>0100b - 65.536ms (~64ms)<br>0101b - 262.144ms (~256ms)<br>0110b - 1.048sec (~1sec)<br>0111b - 4.194sec (~4sec)<br>1000b - 16.777sec (~16sec)<br>1001b - 33.554sec (~32sec)<br>1010b - 67.108sec (~64sec)<br>1011b - Reserved|
|15-10|Reserved.|
|Reserved_15_1<br>0||
|9-0<br>TMR|CSR Clocks for 1us Tic This field indicates the number of CSR clocks required to generate 1us tic.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3710 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.81 (SCS_REG1) 

## Offset 

|Register|Offset|
|---|---|
|SCS_REG1|150h|



Function 

NXP Reserved Register 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||MAC_|SCS1||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||MAC_|SCS1||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|NXP Reserved, All the bits must be set to "0". This field is reserved for NXP Internal use, and must|
|MAC_SCS1|always be set to "0" unless instructed by NXP. Setting any bit to "1" might cause unexpected behavior in<br>the IP.|



# 75.7.82 (MAC_MDIO_Address) 

## Offset 

|Register|Offset|
|---|---|
|MAC_MDIO_Address|200h|



## Function 

The MDIO Address register controls the management cycles to external PHY through a management interface. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3711 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3712-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_28<br>PSE  BTB  PA  RDA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv<br>R e... NTC  CR  Reserved_7_5  SKAP  GOC_ GOC_ C45E  GB<br>1  0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-28|Reserved.|
|Reserved_31_2<br>8||
|27<br>PSE|Preamble Suppression Enable When this bit is set, the SMA suppresses the 32-bit preamble and<br>transmits MDIO frames with only 1 preamble bit. When this bit is 0, the MDIO frame always has 32 bits<br>of preamble as defined in the IEEE specifications.<br>0b - Preamble Suppression disabled<br>1b - Preamble Suppression enabled|
|26<br>BTB|Back to Back transactions When this bit is set and the NTC has value greater than 0, then the MAC<br>informs the completion of a read or write command at the end of frame transfer (before the trailing<br>clocks are transmitted). The software can thus initiate the next command which is executed immediately<br>irrespective of the number trailing clocks generated for the previous frame. When this bit is reset, then<br>the read/write command completion (GB is cleared) only after the trailing clocks are generated. In this<br>mode, it is ensured that the NTC is always generated after each frame. This bit must not be set when<br>NTC=0.<br>0b - Back to Back transactions disabled<br>1b - Back to Back transactions enabled|
|25-21<br>PA|Physical Layer Address This field indicates which Clause 22 PHY devices (out of 32 devices) the MAC is<br>accessing. This field indicates which Clause 45 capable PHYs (out of 32 PHYs) the MAC is accessing.|
|20-16<br>RDA|Register/Device Address These bits select the PHY register in selected Clause 22 PHY device. These<br>bits select the Device (MMD) in selected Clause 45 capable PHY.|
|15|Reserved.|
|Reserved_15||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3712 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field<br>14-12<br>NTC|Function<br>Number of Trailing Clocks This field controls the number of trailing clock cycles generated on<br>gmii_mdc_o (MDC) after the end of transmission of MDIO frame. The valid values can be from 0 to<br>7. Programming the value to 3'h3 indicates that there are additional three clock cycles on the MDC line<br>after the end of MDIO frame transfer.|
|---|---|
|11-8<br>CR|CSR Clock Range The CSR Clock Range selection determines the frequency of the MDC clock<br>according to the CSR clock frequency used in your design: - 0000: CSR clock = 60-100 MHz; MDC<br>clock = CSR clock/42 - 0001: CSR clock = 100-150 MHz; MDC clock = CSR clock/62 - 0010: CSR clock<br>= 20-35 MHz; MDC clock = CSR clock/16 - 0011: CSR clock = 35-60 MHz; MDC clock = CSR clock/26<br>- 0100: CSR clock = 150-250 MHz; MDC clock = CSR clock/102 - 0101: CSR clock = 250-300 MHz;<br>MDC clock = CSR clock/124 - 0110: CSR clock = 300-500 MHz; MDC clock = CSR clock/204 - 0111:<br>CSR clock = 500-800 MHz; MDC clock = CSR clock/324 The suggested range of CSR clock frequency<br>applicable for each value (when Bit 11 = 0) ensures that the MDC clock is approximately between 1.0<br>MHz to 2.5 MHz frequency range. When Bit 11 is set, you can achieve a higher frequency of the MDC<br>clock than the frequency limit of 2.5 MHz (specified in the IEEE 802.3) and program a clock divider<br>of lower value. For example, when CSR clock is of 100 MHz frequency and you program these bits<br>as 1010, the resultant MDC clock is of 12.5 MHz which is beyond the range specified in IEEE 802.3.<br>Program the following values only if the interfacing chips support faster MDC clocks: - 1000: CSR clock/4<br>- 1001: CSR clock/6 - 1010: CSR clock/8 - 1011: CSR clock/10 - 1100: CSR clock/12 - 1101: CSR<br>clock/14 - 1110: CSR clock/16 - 1111: CSR clock/18 These bits are not used for accessing RevMII.<br>These bits are read-only if the RevMII interface is selected as single PHY interface.|
|7-5<br>Reserved_7_5|Reserved.|
|4<br>SKAP|Skip Address Packet When this bit is set, the SMA does not send the address packets before read, write,<br>or post-read increment address packets. This bit is valid only when C45E is set.<br>0b - Skip Address Packet is disabled<br>1b - Skip Address Packet is enabled|
|3<br>GOC_1|GMII Operation Command 1 This bit is higher bit of the operation command to the PHY or RevMII,<br>GOC_1 and GOC_O is encoded as follows: - 00: Reserved - 01: Write - 10: Post Read Increment<br>Address for Clause 45 PHY - 11: Read When Clause 22 PHY or RevMII is enabled, only Write and Read<br>commands are valid.<br>0b - GMII Operation Command 1 is disabled<br>1b - GMII Operation Command 1 is enabled|
|2<br>GOC_0|GMII Operation Command 0 This is the lower bit of the operation command to the PHY or RevMII. When<br>in SMA mode (MDIO master) this bit along with GOC_1 determines the operation to be performed to the<br>PHY. When only RevMII is selected in configuration this bit is read-only and tied to 1.<br>0b - GMII Operation Command 0 is disabled<br>1b - GMII Operation Command 0 is enabled|
|1<br>C45E|Clause 45 PHY Enable When this bit is set, Clause 45 capable PHY is connected to MDIO. When this bit<br>is reset, Clause 22 capable PHY is connected to MDIO.<br>0b - Clause 45 PHY is disabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3713 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - Clause 45 PHY is enabled|
|0<br>GB|GMII Busy The application sets this bit to instruct the SMA to initiate a Read or Write access to the MDIO<br>slave. The MAC clears this bit after the MDIO frame transfer is completed. Hence the software must not<br>write or change any of the fields in MAC_MDIO_Address and MAC_MDIO_Data registers as long as this<br>bit is set. For write transfers, the application must first write 16-bit data in the GDl field (and also RA field<br>when C45E is set) in MAC_MDIO_Data register before setting this bit. When C45E is set, it should also<br>write into the RA field of MAC_MDIO_Data register before initiating a read transfer. When a read transfer<br>is completed (GB=0), the data read from the PHY register is valid in the GD field of the MAC_MDIO_Data<br>register. Note: Even if the addressed PHY is not present, there is no change in the functionality of this<br>bit. Access restriction applies. Setting 1 sets. Self-cleared. Setting 0 has no effect.<br>0b - GMII Busy is disabled|
||1b - GMII Busy is enabled|



# 75.7.83 (MAC_MDIO_Data) 

## Offset 

|Register|Offset|
|---|---|
|MAC_MDIO_Data|204h|



## Function 

The MDIO Data register stores the Write data to be written to the PHY register located at the address specified in MAC_MDIO_Address. This register also stores the Read data from the PHY register located at the address specified by MDIO Address register. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3714-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>RA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>GD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3714 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-16<br>RA|Register Address This field is valid only when C45E is set. It contains the Register Address in the PHY to<br>which the MDIO frame is intended for.|
|15-0<br>GD|GMII Data This field contains the 16-bit data value read from the PHY or RevMII after a Management<br>Read operation or the 16-bit data value to be written to the PHY or RevMII before a Management Write<br>operation.|



# 75.7.84 (MAC_ARP_Address) 

## Offset 

|Register|Offset|
|---|---|
|MAC_ARP_Address|210h|



## Function 

The ARP Address register contains the IPv4 Destination Address of the MAC. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||AR|PPA||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||AR|PPA||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|ARP Protocol Address This field contains the IPv4 Destination Address of the MAC. This address is|
|ARPPA|used for perfect match with the Protocol Address of Target field in the received ARP packet. This field is<br>available only when the Enable IPv4 ARP Offload option is selected.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3715 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.85 (MAC_CSR_SW_Ctrl) 

## Offset 

|Register|Offset|
|---|---|
|MAC_CSR_SW_Ctrl|230h|



## Function 

This register contains software programmable controls for changing the CSR access response and status bits clearing. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3716-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_9<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_31_9  Reserved_7_1<br>SEEN  RCWE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-9|Reserved.|
|Reserved_31_9||
|8<br>SEEN|Slave Error Response Enable When this bit is set, the MAC responds with Slave Error for accesses to<br>reserved registers in CSR space. When this bit is reset, the MAC responds with Okay response to any<br>register accessed from CSR space.<br>0b - Slave Error Response is disabled<br>1b - Slave Error Response is enabled|
|7-1|Reserved.|
|Reserved_7_1||
|0<br>RCWE|Register Clear on Write 1 Enable When this bit is set, the access mode of some register fields changes<br>to Clear on Write 1, the application needs to set that respective bit to 1 to clear it. When this bit is reset,<br>the access mode of these register fields remain as Clear on Read.<br>0b - Register Clear on Write 1 is disabled<br>1b - Register Clear on Write 1 is enabled|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3716 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.86 (MAC_FPE_CTRL_STS) 

## Offset 

|Register|Offset|
|---|---|
|MAC_FPE_CTRL_STS|234h|



## Function 

This register controls the operation of Frame Preemption. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||Reserve|d_31_20||||||TRSP|TVER|RRSP|RVER|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||Reserve|d_15_4||||||S1_SE<br>T_0|SRSP|SVER|EFPE|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-20|Reserved.|
|Reserved_31_2<br>0||
|19<br>TRSP|Transmitted Respond Frame Set when a Respond mPacket is transmitted (triggered by setting SRSP<br>field). An interrupt can be generated for this event if FPEIE bit of MAC_Interrupt_Enable is set. Access<br>restriction applies. Clears on read (or write of 1 when RCWE bit in MAC_CSR_SW_Ctrl register is set).<br>Self-set to 1 on internal event.<br>0b - Not transmitted Respond Frame<br>1b - transmitted Respond Frame|
|18<br>TVER|Transmitted Verify Frame Set when a Verify mPacket is transmitted (triggered by setting SVER field). An<br>interrupt can be generated for this event if FPEIE bit of MAC_Interrupt_Enable is set. Access restriction<br>applies. Clears on read (or write of 1 when RCWE bit in MAC_CSR_SW_Ctrl register is set). Self-set to 1<br>on internal event.<br>0b - Not transmitted Verify Frame<br>1b - transmitted Verify Frame|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3717 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|17<br>RRSP|Received Respond Frame Set when a Respond mPacket is received. An interrupt can be generated for<br>this event if FPEIE bit of MAC_Interrupt_Enable is set. Access restriction applies. Clears on read (or<br>write of 1 when RCWE bit in MAC_CSR_SW_Ctrl register is set). Self-set to 1 on internal event.<br>0b - Not received Respond Frame<br>1b - Received Respond Frame|
|16<br>RVER|Received Verify Frame Set when a Verify mPacket is received. An interrupt can be generated for this<br>event if FPEIE bit of MAC_Interrupt_Enable is set. Access restriction applies. Clears on read (or write of<br>1 when RCWE bit in MAC_CSR_SW_Ctrl register is set). Self-set to 1 on internal event.<br>0b - Not received Verify Frame<br>1b - Received Verify Frame|
|15-4|Reserved.|
|Reserved_15_4||
|3<br>S1_SET_0|NXP Reserved, Must be set to "0". This field is reserved for NXP Internal use, and must always be set to<br>"0" unless instructed by NXP. Setting to "1" might cause unexpected behavior in the IP.|
|2<br>SRSP|Send Respond mPacket When set indicates hardware to send a Respond mPacket. Reset by hardware<br>after sending the Respond mPacket. Access restriction applies. Setting 1 sets. Self-cleared. Setting 0<br>has no effect.<br>0b - Send Respond mPacket is disabled<br>1b - Send Respond mPacket is enabled|
|1<br>SVER|Send Verify mPacket When set indicates hardware to send a verify mPacket. Reset by hardware after<br>sending the Verify mPacket. Access restriction applies. Setting 1 sets. Self-cleared. Setting 0 has no<br>effect.<br>0b - Send Verify mPacket is disabled<br>1b - Send Verify mPacket is enabled|
|0<br>EFPE|Enable Tx Frame Preemption When set Frame Preemption Tx functionality is enabled.<br>0b - Tx Frame Preemption is disabled<br>1b - Tx Frame Preemption is enabled|



# 75.7.87 (MAC_Ext_Cfg1) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Ext_Cfg1|238h|



## Function 

This register contains Split mode control field and offset field for Split Header feature. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3718 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3719-02.png)


<!-- Start of picture text -->
Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R Reserved_31_25<br>SAVE  e... SAVO<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv<br>R Reserved_15_10<br>SPLM  e... SPLOFST<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-25|Reserved.|
|Reserved_31_2<br>5||
|24<br>SAVE|Split AV Enable - When this bit is set to 1, and the received packet is an AV Type packet, the header is<br>split at SAVO bytes from the beginning of Length/Type field of the packet, for L2 Split. - When this bit is<br>set to 0, header is split at SPLOFST bytes from the beginning of Length/Type field of the frame, for L2<br>Split.|
|23|Reserved.|
|Reserved_23||
|22-16<br>SAVO|Split AV Offset When SAVE bit is set to 1, and the received packet is an AV Type packet, these bits<br>indicate the value of the offset from the beginning of Length/Type field at which header should be split,<br>when appropriate SPLM is selected. The reset value of this field is 2 bytes, indicating a split at L2<br>header. Value is in terms of bytes.|
|15-10|Reserved.|
|Reserved_15_1<br>0||
|9-8<br>SPLM|Split Mode These bits indicate the mode of splitting the incoming Rx packets. They are<br>00b - Split at L3/L4 header<br>01b - Split at L2 header with an offset. Always Split at SPLOFST bytes from the beginning of<br>Length/Type field of the Frame<br>10b - Combination mode: Split similar to SPLM=00 for IP packets that are untagged or tagged<br>and VLAN stripped<br>11b - Reserved|
|7|Reserved.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3719 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|Reserved_7||
|6-0|Split Offset These bits indicate the value of offset from the beginning of Length/Type field at which|
|SPLOFST|header split should take place when the appropriate SPLM is selected. The reset value of this field is 2<br>bytes indicating a split at L2 header. Value is in terms of bytes.|



# 75.7.88 (MAC_Presn_Time_ns) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Presn_Time_ns|240h|



## Function 

This register contains the 32-bit binary rollover equivalent time of the PTP System Time in ns Exists when DWC_EQOS_FLEXI_PPS_OUT_EN is configured 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||MP|TN||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||MP|TN||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|MAC 1722 Presentation Time in ns These bits indicate the value of the 32-bit binary rollover equivalent|
|MPTN|time of the PTP System Time in ns|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3720 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.89 (MAC_Presn_Time_Updt) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Presn_Time_Updt|244h|



## Function 

This field holds the 32-bit value of MAC 1722 Presentation Time in ns, that should be added to the Current Presentation Time Counter value. Init happens when TSINIT is set, and update happens when the TSUPDT bit is set (TSINIT and TSINIT defined in MAC_Timestamp_ Control register). Exists when DWC_EQOS_FLEXI_PPS_OUT_EN is configured 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||MP|TU||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||MP|TU||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0<br>MPTU|MAC 1722 Presentation Time Update This field holds the init value or the update value for the<br>presentation time. When used for update, this field holds the 32-bit value in ns, that should be<br>added to the Current Presentation Time Counter value. Init happens when TSINIT is set, and update|
||happens when the TSUPDT bit is set (TSINIT and TSINIT defined in MAC_Timestamp_ Control register).<br>When ADDSUB field of MAC_System_Time_Nanoseconds_Update is set, this value is directly used for<br>subtraction|



# 75.7.90 (MAC_Address0_High) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Address0_High|300h|



## Function 

The MAC Address0 High register holds the upper 16 bits of the first 6-byte MAC address of the station. The first DA byte that is received on the (G)MII interface corresponds to the LS byte (Bits [7:0]) of the MAC Address Low register. For example, if 0x112233445566 is received (0x11 in lane 0 of the first column) on the (G)MII as the destination address, then the MacAddress0 Register [47:0] is compared with 0x665544332211. If the MAC address registers are configured to be 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3721 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

double-synchronized to the (G)MII clock domains, then the synchronization is triggered only when Bits[31:24] (in little-endian mode) or Bits[7:0] (in big-endian mode) of the MAC Address0 Low Register are written. For proper synchronization updates, the consecutive writes to this Address Low Register should be performed after at least four clock cycles in the destination clock domain. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|AE||||||Reserve|d_30_y|||||||DCS||
|Reset|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||ADD|RHI||||||||
|Reset|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|



## Fields 

|Field|Function|
|---|---|
|31|Address Enable This bit is always set to 1.|
|AE|0b - INVALID : This bit must be always set to 1<br>1b - This bit is always set to 1|
|30-19|Reserved.|
|Reserved_30_y||
|18-16<br>DCS|DMA Channel Select If the PDC bit of MAC_Ext_Configuration register is not set: This field contains the<br>binary representation of the DMA Channel number to which an Rx packet whose DA matches the MAC<br>Address0 content is routed. If the PDC bit of MAC_Ext_Configuration register is set: This field contains<br>the one-hot representation of one or more DMA Channel numbers to which an Rx packet whose DA<br>matches the MAC Address0 content is routed.|
|15-0<br>ADDRHI|MAC Address0[47:32] This field contains the upper 16 bits [47:32] of the first 6-byte MAC address. The<br>MAC uses this field for filtering the received packets and inserting the MAC address in the Transmit Flow<br>Control (Pause) Packets.|



# 75.7.91 (MAC_Address0_Low) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Address0_Low|304h|



## Function 

The MAC Address0 Low register holds the lower 32 bits of the 6-byte first MAC address of the station. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3722 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3723-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>ADDRLO<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>ADDRLO<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|MAC Address0[31:0] This field contains the lower 32 bits of the first 6-byte MAC address. The MAC uses|
|ADDRLO|this field for filtering the received packets and inserting the MAC address in the Transmit Flow Control<br>(Pause) Packets.|



# 75.7.92 (MAC_Address1_High) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Address1_High|308h|



## Function 

The MAC Address1 High register holds the upper 16 bits of the second 6-byte MAC address of the station. If the MAC address registers are configured to be double-synchronized to the (G)MII clock domains, the synchronization is triggered only when Bits[31:24] (in little-endian mode) or Bits[7:0] (in big-endian mode) of the MAC Address1 Low Register are written. For proper synchronization updates, the consecutive writes to this Address Low Register should be performed after at least four clock cycles in the destination clock domain. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|AE|SA|||MB|C||||Res|erved_2|3_y|||DCS||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||ADD|RHI||||||||
|Reset|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3723 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31<br>AE|Address Enable When this bit is set, the address filter module uses the second MAC address for perfect<br>filtering. When this bit is reset, the address filter module ignores the address for filtering.<br>0b - Address is ignored<br>1b - Address is enabled|
|30<br>SA|Source Address When this bit is set, the MAC Address1[47:0] is used to compare with the SA fields of<br>the received packet. When this bit is reset, the MAC Address1[47:0] is used to compare with the DA<br>fields of the received packet.<br>0b - Compare with Destination Address<br>1b - Compare with Source Address|
|29-24<br>MBC|Mask Byte Control These bits are mask control bits for comparing each of the MAC Address bytes.<br>When set high, the MAC does not compare the corresponding byte of received DA or SA with<br>the contents of MAC Address1 registers. Each bit controls the masking of the bytes as follows:<br>- Bit 29: MAC_Address${i}_High[15:8] - Bit 28: MAC_Address${i}_High[7:0] - Bit 27: MAC_Address$ {i}_Low[31:24] - .. - Bit 24: MAC_Address${i}_Low[7:0] You can filter a group of addresses (known as<br>group address filtering) by masking one or more bytes of the address.|
|23-19|Reserved.|
|Reserved_23_y||
|18-16<br>DCS|DMA Channel Select If the PDC bit of MAC_Ext_Configuration register is not set: This field contains the<br>binary representation of the DMA Channel number to which an Rx packet whose DA matches the MAC<br>Address(#i) content is routed. If the PDC bit of MAC_Ext_Configuration register is set: This field contains<br>the one-hot representation of one or more DMA Channel numbers to which an Rx packet whose DA<br>matches the MAC Address(#i) content is routed.|
|15-0<br>ADDRHI|MAC Address1 [47:32] This field contains the upper 16 bits[47:32] of the second 6-byte MAC address.|



# 75.7.93 (MAC_Address1_Low) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Address1_Low|30Ch|



## Function 

The MAC Address1 Low register holds the lower 32 bits of the second 6-byte MAC address of the station. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3724 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3725-01.png)


<!-- Start of picture text -->
Gigabit Ethernet Media Access Controller (GMAC)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>ADDRLO<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>ADDRLO<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|MAC Address1 [31:0] This field contains the lower 32 bits of second 6-byte MAC address. The content of|
|ADDRLO|this field is undefined until loaded by the application after the initialization process.|



# 75.7.94 (MAC_Address2_High) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Address2_High|310h|



## Function 

The MAC Address1 High register holds the upper 16 bits of the second 6-byte MAC address of the station. If the MAC address registers are configured to be double-synchronized to the (G)MII clock domains, the synchronization is triggered only when Bits[31:24] (in little-endian mode) or Bits[7:0] (in big-endian mode) of the MAC Address1 Low Register are written. For proper synchronization updates, the consecutive writes to this Address Low Register should be performed after at least four clock cycles in the destination clock domain. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|AE|SA|||MB|C||||Res|erved_2|3_y|||DCS||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||ADD|RHI||||||||
|Reset|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3725 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31<br>AE|Address Enable When this bit is set, the address filter module uses the second MAC address for perfect<br>filtering. When this bit is reset, the address filter module ignores the address for filtering.<br>0b - Address is ignored<br>1b - Address is enabled|
|30<br>SA|Source Address When this bit is set, the MAC Address1[47:0] is used to compare with the SA fields of<br>the received packet. When this bit is reset, the MAC Address1[47:0] is used to compare with the DA<br>fields of the received packet.<br>0b - Compare with Destination Address<br>1b - Compare with Source Address|
|29-24<br>MBC|Mask Byte Control These bits are mask control bits for comparing each of the MAC Address bytes.<br>When set high, the MAC does not compare the corresponding byte of received DA or SA with<br>the contents of MAC Address1 registers. Each bit controls the masking of the bytes as follows:<br>- Bit 29: MAC_Address${i}_High[15:8] - Bit 28: MAC_Address${i}_High[7:0] - Bit 27: MAC_Address$ {i}_Low[31:24] - .. - Bit 24: MAC_Address${i}_Low[7:0] You can filter a group of addresses (known as<br>group address filtering) by masking one or more bytes of the address.|
|23-19|Reserved.|
|Reserved_23_y||
|18-16<br>DCS|DMA Channel Select If the PDC bit of MAC_Ext_Configuration register is not set: This field contains the<br>binary representation of the DMA Channel number to which an Rx packet whose DA matches the MAC<br>Address(#i) content is routed. If the PDC bit of MAC_Ext_Configuration register is set: This field contains<br>the one-hot representation of one or more DMA Channel numbers to which an Rx packet whose DA<br>matches the MAC Address(#i) content is routed.|
|15-0<br>ADDRHI|MAC Address1 [47:32] This field contains the upper 16 bits[47:32] of the second 6-byte MAC address.|



# 75.7.95 (MAC_Address2_Low) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Address2_Low|314h|



## Function 

The MAC Address1 Low register holds the lower 32 bits of the second 6-byte MAC address of the station. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3726 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3727-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>ADDRLO<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>ADDRLO<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|MAC Address1 [31:0] This field contains the lower 32 bits of second 6-byte MAC address. The content of|
|ADDRLO|this field is undefined until loaded by the application after the initialization process.|



# 75.7.96 (MMC_Control) 

## Offset 

|Register|Offset|
|---|---|
|MMC_Control|700h|



## Function 

This register establishes the operating mode of MMC. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3727-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_9<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_31_9  UCDB Reserved_7_6  CNTP CNTP CNTF RSTO CNTS CNTR<br>W C  RST... RST  REEZ  NRD  TOP... ST<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3727 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field<br>31-9<br>Reserved_31_9|Function<br>Reserved.|
|---|---|
|8<br>UCDBC|Update MMC Counters for Dropped Broadcast Packets Note: The CNTRST bit has a higher priority than<br>the CNTPRST bit. Therefore, when the software tries to set both bits in the same write cycle, all counters<br>are cleared and the CNTPRST bit is not set. When set, the MAC updates all related MMC Counters for<br>Broadcast packets that are dropped because of the setting of the DBF bit of MAC_Packet_Filter register.<br>When reset, the MMC Counters are not updated for dropped Broadcast packets.<br>0b - Update MMC Counters for Dropped Broadcast Packets is disabled<br>1b - Update MMC Counters for Dropped Broadcast Packets is enabled|
|7-6<br>Reserved_7_6|Reserved.|
|5<br>CNTPRSTLVL|Full-Half Preset When this bit is low and the CNTPRST bit is set, all MMC counters get preset to<br>almost-half value. All octet counters get preset to 0x7FFF_F800 (Half 2KBytes) and all packet-counters<br>gets preset to 0x7FFF_FFF0 (Half 16). When this bit is high and the CNTPRST bit is set, all MMC<br>counters get preset to almost-full value. All octet counters get preset to 0xFFFF_F800 (Full 2KBytes)<br>and all packet-counters gets preset to 0xFFFF_FFF0 (Full 16). For 16-bit counters, the almost-half preset<br>values are 0x7800 and 0x7FF0 for the respective octet and packet counters. Similarly, the almost-full<br>preset values for the 16-bit counters are 0xF800 and 0xFFF0.<br>0b - Full-Half Preset is disabled<br>1b - Full-Half Preset is enabled|
|4<br>CNTPRST|Counters Preset When this bit is set, all counters are initialized or preset to almost full or almost half<br>according to the CNTPRSTLVL bit. This bit is cleared automatically after 1 clock cycle. This bit, along<br>with the CNTPRSTLVL bit, is useful for debugging and testing the assertion of interrupts because of<br>MMC counter becoming half-full or full. Access restriction applies. Self-cleared. Setting 0 clears. Setting<br>1 sets.<br>0b - Counters Preset is disabled<br>1b - Counters Preset is enabled|
|3<br>CNTFREEZ|MMC Counter Freeze When this bit is set, it freezes all MMC counters to their current value. Until this<br>bit is reset to 0, no MMC counter is updated because of any transmitted or received packet. If any MMC<br>counter is read with the Reset on Read bit set, then that counter is also cleared in this mode.<br>0b - MMC Counter Freeze is disabled<br>1b - MMC Counter Freeze is enabled|
|2<br>RSTONRD|Reset on Read When this bit is set, the MMC counters are reset to zero after Read (self-clearing after<br>reset). The counters are cleared when the least significant byte lane (Bits[7:0]) is read.<br>0b - Reset on Read is disabled<br>1b - Reset on Read is enabled|
|1|Counter Stop Rollover When this bit is set, the counter does not roll over to zero after reaching the<br>maximum value.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3728 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|CNTSTOPRO|0b - Counter Stop Rollover is disabled|
||1b - Counter Stop Rollover is enabled|
|0<br>CNTRST|Counters Reset When this bit is set, all counters are reset. This bit is cleared automatically after 1 clock<br>cycle. Access restriction applies. Self-cleared. Setting 0 clears. Setting 1 sets.<br>0b - Counters are not reset|
||1b - All counters are reset|



# 75.7.97 (MMC_Rx_Interrupt) 

## Offset 

|Register|Offset|
|---|---|
|MMC_Rx_Interrupt|704h|



## Function 

This register maintains the interrupts generated from all Receive statistics counters. The MMC Receive Interrupt register maintains the interrupts that are generated when the following occur: - Receive statistic counters reach half of their maximum values (0x8000_0000 for 32 bit counter and 0x8000 for 16 bit counter). - Receive statistic counters cross their maximum values (0xFFFF_FFFF for 32 bit counter and 0xFFFF for 16 bit counter). When the Counter Stop Rollover is set, interrupts are set but the counter remains at all-ones. The MMC Receive Interrupt register is a 32 bit register. An interrupt bit is cleared when the respective MMC counter that caused the interrupt is read. The least significant byte lane (Bits[7:0]) of the respective counter must be read to clear the interrupt bit. Note: R_SS_RC means that this register bit is set internally, and it is cleared when the Counter register is read. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3729-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv Reserv RXCT RXRC RXWD RXVL RXFO RXPA RXOR RXLE RXUC RX102<br>R Reserved_31_28<br>e... e... RLP... VER... OGP... ANG... VPIS  USP... ANG... NER... GPIS  4T...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>RX512 RX256 RX128 RX65T RX64 RXOSI RXUSI RXJA RXRU RXAL RXCR RXMC RXBC RXGO RXGB RXGB<br>R<br>T1... T5... T2... 12... OCT... ZE... ZE... BER... NTP... GNE... CER... GPIS  GPIS  CTIS  OCT... PKT...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3729 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-28|Reserved.|
|Reserved_31_2<br>8||
|27|Reserved.|
|Reserved_RXL<br>PITRCIS||
|26|Reserved.|
|Reserved_RXL<br>PIUSCIS||
|25<br>RXCTRLPIS|MMC Receive Control Packet Counter Interrupt Status This bit is set when the rxctrlpackets_g counter<br>reaches half of the maximum value or the maximum value. Access restriction applies. Clears on read.<br>Self-set to 1 on internal event.<br>0b - MMC Receive Control Packet Counter Interrupt Status not detected<br>1b - MMC Receive Control Packet Counter Interrupt Status detected|
|24<br>RXRCVERRPIS|MMC Receive Error Packet Counter Interrupt Status This bit is set when the rxrcverror counter reaches<br>half of the maximum value or the maximum value. Access restriction applies. Clears on read. Self-set to<br>1 on internal event.<br>0b - MMC Receive Error Packet Counter Interrupt Status not detected<br>1b - MMC Receive Error Packet Counter Interrupt Status detected|
|23<br>RXWDOGPIS|MMC Receive Watchdog Error Packet Counter Interrupt Status This bit is set when the rxwatchdog error<br>counter reaches half of the maximum value or the maximum value. Access restriction applies. Clears on<br>read. Self-set to 1 on internal event.<br>0b - MMC Receive Watchdog Error Packet Counter Interrupt Status not detected<br>1b - MMC Receive Watchdog Error Packet Counter Interrupt Status detected|
|22<br>RXVLANGBPIS|MMC Receive VLAN Good Bad Packet Counter Interrupt Status This bit is set when the<br>rxvlanpackets_gb counter reaches half of the maximum value or the maximum value. Access restriction<br>applies. Clears on read. Self-set to 1 on internal event.<br>0b - MMC Receive VLAN Good Bad Packet Counter Interrupt Status not detected<br>1b - MMC Receive VLAN Good Bad Packet Counter Interrupt Status detected|
|21<br>RXFOVPIS|MMC Receive FIFO Overflow Packet Counter Interrupt Status This bit is set when the rxfifooverflow<br>counter reaches half of the maximum value or the maximum value. Access restriction applies. Clears on<br>read. Self-set to 1 on internal event.<br>0b - MMC Receive FIFO Overflow Packet Counter Interrupt Status not detected<br>1b - MMC Receive FIFO Overflow Packet Counter Interrupt Status detected<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3730 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field<br>20<br>RXPAUSPIS|Function<br>MMC Receive Pause Packet Counter Interrupt Status This bit is set when the rxpausepackets counter<br>reaches half of the maximum value or the maximum value. Access restriction applies. Clears on read.<br>Self-set to 1 on internal event.<br>0b - MMC Receive Pause Packet Counter Interrupt Status not detected<br>1b - MMC Receive Pause Packet Counter Interrupt Status detected|
|---|---|
|19<br>RXORANGEPI<br>S|MMC Receive Out Of Range Error Packet Counter Interrupt Status. This bit is set when the<br>rxoutofrangetype counter reaches half of the maximum value or the maximum value. Access restriction<br>applies. Clears on read. Self-set to 1 on internal event.<br>0b - MMC Receive Out Of Range Error Packet Counter Interrupt Status not detected<br>1b - MMC Receive Out Of Range Error Packet Counter Interrupt Status detected|
|18<br>RXLENERPIS|MMC Receive Length Error Packet Counter Interrupt Status This bit is set when the rxlengtherror counter<br>reaches half of the maximum value or the maximum value. Access restriction applies. Clears on read.<br>Self-set to 1 on internal event.<br>0b - MMC Receive Length Error Packet Counter Interrupt Status not detected<br>1b - MMC Receive Length Error Packet Counter Interrupt Status detected|
|17<br>RXUCGPIS|MMC Receive Unicast Good Packet Counter Interrupt Status This bit is set when the rxunicastpackets_g<br>counter reaches half of the maximum value or the maximum value. Access restriction applies. Clears on<br>read. Self-set to 1 on internal event.<br>0b - MMC Receive Unicast Good Packet Counter Interrupt Status not detected<br>1b - MMC Receive Unicast Good Packet Counter Interrupt Status detected|
|16<br>RX1024TMAXO<br>CTGBPIS|MMC Receive 1024 to Maximum Octet Good Bad Packet Counter Interrupt Status This bit is set when<br>the rx1024tomaxoctets_gb counter reaches half of the maximum value or the maximum value. Access<br>restriction applies. Clears on read. Self-set to 1 on internal event.<br>0b - MMC Receive 1024 to Maximum Octet Good Bad Packet Counter Interrupt Status not<br>detected<br>1b - MMC Receive 1024 to Maximum Octet Good Bad Packet Counter Interrupt Status detected|
|15<br>RX512T1023O<br>CTGBPIS|MMC Receive 512 to 1023 Octet Good Bad Packet Counter Interrupt Status This bit is set when<br>the rx512to1023octets_gb counter reaches half of the maximum value or the maximum value. Access<br>restriction applies. Clears on read. Self-set to 1 on internal event.<br>0b - MMC Receive 512 to 1023 Octet Good Bad Packet Counter Interrupt Status not detected<br>1b - MMC Receive 512 to 1023 Octet Good Bad Packet Counter Interrupt Status detected|
|14<br>RX256T511OC<br>TGBPIS|MMC Receive 256 to 511 Octet Good Bad Packet Counter Interrupt Status This bit is set when<br>the rx256to511octets_gb counter reaches half of the maximum value or the maximum value. Access<br>restriction applies. Clears on read. Self-set to 1 on internal event.<br>0b - MMC Receive 256 to 511 Octet Good Bad Packet Counter Interrupt Status not detected<br>1b - MMC Receive 256 to 511 Octet Good Bad Packet Counter Interrupt Status detected|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3731 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field<br>13<br>RX128T255OC<br>TGBPIS|Function<br>MMC Receive 128 to 255 Octet Good Bad Packet Counter Interrupt Status This bit is set when<br>the rx128to255octets_gb counter reaches half of the maximum value or the maximum value. Access<br>restriction applies. Clears on read. Self-set to 1 on internal event.<br>0b - MMC Receive 128 to 255 Octet Good Bad Packet Counter Interrupt Status not detected<br>1b - MMC Receive 128 to 255 Octet Good Bad Packet Counter Interrupt Status detected|
|---|---|
|12<br>RX65T127OCT<br>GBPIS|MMC Receive 65 to 127 Octet Good Bad Packet Counter Interrupt Status This bit is set when<br>the rx65to127octets_gb counter reaches half of the maximum value or the maximum value. Access<br>restriction applies. Clears on read. Self-set to 1 on internal event.<br>0b - MMC Receive 65 to 127 Octet Good Bad Packet Counter Interrupt Status not detected<br>1b - MMC Receive 65 to 127 Octet Good Bad Packet Counter Interrupt Status detected|
|11<br>RX64OCTGBPI<br>S|MMC Receive 64 Octet Good Bad Packet Counter Interrupt Status This bit is set when the rx64octets_gb<br>counter reaches half of the maximum value or the maximum value. Access restriction applies. Clears on<br>read. Self-set to 1 on internal event.<br>0b - MMC Receive 64 Octet Good Bad Packet Counter Interrupt Status not detected<br>1b - MMC Receive 64 Octet Good Bad Packet Counter Interrupt Status detected|
|10<br>RXOSIZEGPIS|MMC Receive Oversize Good Packet Counter Interrupt Status This bit is set when the rxoversize_g<br>counter reaches half of the maximum value or the maximum value. Access restriction applies. Clears on<br>read. Self-set to 1 on internal event.<br>0b - MMC Receive Oversize Good Packet Counter Interrupt Status not detected<br>1b - MMC Receive Oversize Good Packet Counter Interrupt Status detected|
|9<br>RXUSIZEGPIS|MMC Receive Undersize Good Packet Counter Interrupt Status This bit is set when the rxundersize_g<br>counter reaches half of the maximum value or the maximum value. Access restriction applies. Clears on<br>read. Self-set to 1 on internal event.<br>0b - MMC Receive Undersize Good Packet Counter Interrupt Status not detected<br>1b - MMC Receive Undersize Good Packet Counter Interrupt Status detected|
|8<br>RXJABERPIS|MMC Receive Jabber Error Packet Counter Interrupt Status This bit is set when the rxjabbererror<br>counter reaches half of the maximum value or the maximum value. Access restriction applies. Clears on<br>read. Self-set to 1 on internal event.<br>0b - MMC Receive Jabber Error Packet Counter Interrupt Status not detected<br>1b - MMC Receive Jabber Error Packet Counter Interrupt Status detected|
|7<br>RXRUNTPIS|MMC Receive Runt Packet Counter Interrupt Status This bit is set when the rxrunterror counter reaches<br>half of the maximum value or the maximum value. Access restriction applies. Clears on read. Self-set to<br>1 on internal event.<br>0b - MMC Receive Runt Packet Counter Interrupt Status not detected<br>1b - MMC Receive Runt Packet Counter Interrupt Status detected|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3732 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field<br>6<br>RXALGNERPIS|Function<br>MMC Receive Alignment Error Packet Counter Interrupt Status This bit is set when the rxalignmenterror<br>counter reaches half of the maximum value or the maximum value. Access restriction applies. Clears on<br>read. Self-set to 1 on internal event.<br>0b - MMC Receive Alignment Error Packet Counter Interrupt Status not detected<br>1b - MMC Receive Alignment Error Packet Counter Interrupt Status detected|
|---|---|
|5<br>RXCRCERPIS|MMC Receive CRC Error Packet Counter Interrupt Status This bit is set when the rxcrcerror counter<br>reaches half of the maximum value or the maximum value. Access restriction applies. Clears on read.<br>Self-set to 1 on internal event.<br>0b - MMC Receive CRC Error Packet Counter Interrupt Status not detected<br>1b - MMC Receive CRC Error Packet Counter Interrupt Status detected|
|4<br>RXMCGPIS|MMC Receive Multicast Good Packet Counter Interrupt Status This bit is set when the<br>rxmulticastpackets_g counter reaches half of the maximum value or the maximum value. Access<br>restriction applies. Clears on read. Self-set to 1 on internal event.<br>0b - MMC Receive Multicast Good Packet Counter Interrupt Status not detected<br>1b - MMC Receive Multicast Good Packet Counter Interrupt Status detected|
|3<br>RXBCGPIS|MMC Receive Broadcast Good Packet Counter Interrupt Status This bit is set when the<br>rxbroadcastpackets_g counter reaches half of the maximum value or the maximum value. Access<br>restriction applies. Clears on read. Self-set to 1 on internal event.<br>0b - MMC Receive Broadcast Good Packet Counter Interrupt Status not detected<br>1b - MMC Receive Broadcast Good Packet Counter Interrupt Status detected|
|2<br>RXGOCTIS|MMC Receive Good Octet Counter Interrupt Status This bit is set when the rxoctetcount_g counter<br>reaches half of the maximum value or the maximum value. Access restriction applies. Clears on read.<br>Self-set to 1 on internal event.<br>0b - MMC Receive Good Octet Counter Interrupt Status not detected<br>1b - MMC Receive Good Octet Counter Interrupt Status detected|
|1<br>RXGBOCTIS|MMC Receive Good Bad Octet Counter Interrupt Status This bit is set when the rxoctetcount_gb counter<br>reaches half of the maximum value or the maximum value. Access restriction applies. Clears on read.<br>Self-set to 1 on internal event.<br>0b - MMC Receive Good Bad Octet Counter Interrupt Status not detected<br>1b - MMC Receive Good Bad Octet Counter Interrupt Status detected|
|0<br>RXGBPKTIS|MMC Receive Good Bad Packet Counter Interrupt Status This bit is set when the rxpacketcount_gb<br>counter reaches half of the maximum value or the maximum value. Access restriction applies. Clears on<br>read. Self-set to 1 on internal event.<br>0b - MMC Receive Good Bad Packet Counter Interrupt Status not detected<br>1b - MMC Receive Good Bad Packet Counter Interrupt Status detected|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3733 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.98 (MMC_Tx_Interrupt) 

## Offset 

|Register|Offset|
|---|---|
|MMC_Tx_Interrupt|708h|



## Function 

This register maintains the interrupts generated from all Transmit statistics counters. The MMC Transmit Interrupt register maintains the interrupts generated when transmit statistic counters reach half their maximum values (0x8000_0000 for 32 bit counter and 0x8000 for 16 bit counter), and when they cross their maximum values (0xFFFF_FFFF for 32-bit counter and 0xFFFF for 16-bit counter). When Counter Stop Rollover is set, the interrupts are set but the counter remains at all-ones. The MMC Transmit Interrupt register is a 32 bit register. An interrupt bit is cleared when the respective MMC counter that caused the interrupt is read. The least significant byte lane (Bits[7:0]) of the respective counter must be read to clear the interrupt bit. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3734-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv Reserv TXOSI TXVLA TXPA TXEX TXGP TXGO TXCA TXEX TXLAT TXDE<br>R Reserved_31_28<br>e... e... ZE... NG... USP... DEF... KTIS  CTIS  RER... COL... CO... FPIS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>TXMC TXSC TXUFL TXBC TXMC TXUC TX102 TX512 TX256 TX128 TX65T TX64O TXMC TXBC TXGB TXGB<br>R<br>OLG... OLG... OW... GBP... GBP... GBP... 4T... T1... T5... T2... 12... CT... GPIS  GPIS  PKT... OCT...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-28|Reserved.|
|Reserved_31_2<br>8||
|27|Reserved.|
|Reserved_TXL<br>PITRCIS||
|26|Reserved.|
|Reserved_TXL<br>PIUSCIS||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3734 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field<br>25<br>TXOSIZEGPIS|Function<br>MMC Transmit Oversize Good Packet Counter Interrupt Status This bit is set when the txoversize_g<br>counter reaches half of the maximum value or the maximum value. Access restriction applies. Clears on<br>read. Self-set to 1 on internal event.<br>0b - MMC Transmit Oversize Good Packet Counter Interrupt Status not detected<br>1b - MMC Transmit Oversize Good Packet Counter Interrupt Status detected|
|---|---|
|24<br>TXVLANGPIS|MMC Transmit VLAN Good Packet Counter Interrupt Status This bit is set when the txvlanpackets_g<br>counter reaches half of the maximum value or the maximum value. Access restriction applies. Clears on<br>read. Self-set to 1 on internal event.<br>0b - MMC Transmit VLAN Good Packet Counter Interrupt Status not detected<br>1b - MMC Transmit VLAN Good Packet Counter Interrupt Status detected|
|23<br>TXPAUSPIS|MMC Transmit Pause Packet Counter Interrupt Status This bit is set when the txpausepacketserror<br>counter reaches half of the maximum value or the maximum value. Access restriction applies. Clears on<br>read. Self-set to 1 on internal event.<br>0b - MMC Transmit Pause Packet Counter Interrupt Status not detected<br>1b - MMC Transmit Pause Packet Counter Interrupt Status detected|
|22<br>TXEXDEFPIS|MMC Transmit Excessive Deferral Packet Counter Interrupt Status This bit is set when the txexcessdef<br>counter reaches half of the maximum value or the maximum value. Access restriction applies. Clears on<br>read. Self-set to 1 on internal event.<br>0b - MMC Transmit Excessive Deferral Packet Counter Interrupt Status not detected<br>1b - MMC Transmit Excessive Deferral Packet Counter Interrupt Status detected|
|21<br>TXGPKTIS|MMC Transmit Good Packet Counter Interrupt Status This bit is set when the txpacketcount_g counter<br>reaches half of the maximum value or the maximum value. Access restriction applies. Clears on read.<br>Self-set to 1 on internal event.<br>0b - MMC Transmit Good Packet Counter Interrupt Status not detected<br>1b - MMC Transmit Good Packet Counter Interrupt Status detected|
|20<br>TXGOCTIS|MMC Transmit Good Octet Counter Interrupt Status This bit is set when the txoctetcount_g counter<br>reaches half of the maximum value or the maximum value. Access restriction applies. Clears on read.<br>Self-set to 1 on internal event.<br>0b - MMC Transmit Good Octet Counter Interrupt Status not detected<br>1b - MMC Transmit Good Octet Counter Interrupt Status detected|
|19<br>TXCARERPIS|MMC Transmit Carrier Error Packet Counter Interrupt Status This bit is set when the txcarriererror<br>counter reaches half of the maximum value or the maximum value. Access restriction applies. Clears on<br>read. Self-set to 1 on internal event.<br>0b - MMC Transmit Carrier Error Packet Counter Interrupt Status not detected<br>1b - MMC Transmit Carrier Error Packet Counter Interrupt Status detected<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3735 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field<br>18<br>TXEXCOLPIS|Function<br>MMC Transmit Excessive Collision Packet Counter Interrupt Status This bit is set when the txexesscol<br>counter reaches half of the maximum value or the maximum value. Access restriction applies. Clears on<br>read. Self-set to 1 on internal event.<br>0b - MMC Transmit Excessive Collision Packet Counter Interrupt Status not detected<br>1b - MMC Transmit Excessive Collision Packet Counter Interrupt Status detected|
|---|---|
|17<br>TXLATCOLPIS|MMC Transmit Late Collision Packet Counter Interrupt Status This bit is set when the txlatecol counter<br>reaches half of the maximum value or the maximum value. Access restriction applies. Clears on read.<br>Self-set to 1 on internal event.<br>0b - MMC Transmit Late Collision Packet Counter Interrupt Status not detected<br>1b - MMC Transmit Late Collision Packet Counter Interrupt Status detected|
|16<br>TXDEFPIS|MMC Transmit Deferred Packet Counter Interrupt Status This bit is set when the txdeferred counter<br>reaches half of the maximum value or the maximum value. Access restriction applies. Clears on read.<br>Self-set to 1 on internal event.<br>0b - MMC Transmit Deferred Packet Counter Interrupt Status not detected<br>1b - MMC Transmit Deferred Packet Counter Interrupt Status detected|
|15<br>TXMCOLGPIS|MMC Transmit Multiple Collision Good Packet Counter Interrupt Status This bit is set when the<br>txmulticol_g counter reaches half of the maximum value or the maximum value. Access restriction<br>applies. Clears on read. Self-set to 1 on internal event.<br>0b - MMC Transmit Multiple Collision Good Packet Counter Interrupt Status not detected<br>1b - MMC Transmit Multiple Collision Good Packet Counter Interrupt Status detected|
|14<br>TXSCOLGPIS|MMC Transmit Single Collision Good Packet Counter Interrupt Status This bit is set when the<br>txsinglecol_g counter reaches half of the maximum value or the maximum value. Access restriction<br>applies. Clears on read. Self-set to 1 on internal event.<br>0b - MMC Transmit Single Collision Good Packet Counter Interrupt Status not detected<br>1b - MMC Transmit Single Collision Good Packet Counter Interrupt Status detected|
|13<br>TXUFLOWERPI<br>S|MMC Transmit Underflow Error Packet Counter Interrupt Status This bit is set when the txunderflowerror<br>counter reaches half of the maximum value or the maximum value. Access restriction applies. Clears on<br>read. Self-set to 1 on internal event.<br>0b - MMC Transmit Underflow Error Packet Counter Interrupt Status not detected<br>1b - MMC Transmit Underflow Error Packet Counter Interrupt Status detected|
|12<br>TXBCGBPIS|MMC Transmit Broadcast Good Bad Packet Counter Interrupt Status This bit is set when the<br>txbroadcastpackets_gb counter reaches half of the maximum value or the maximum value. Access<br>restriction applies. Clears on read. Self-set to 1 on internal event.<br>0b - MMC Transmit Broadcast Good Bad Packet Counter Interrupt Status not detected<br>1b - MMC Transmit Broadcast Good Bad Packet Counter Interrupt Status detected<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3736 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field<br>11<br>TXMCGBPIS|Function<br>MMC Transmit Multicast Good Bad Packet Counter Interrupt Status The bit is set when the<br>txmulticastpackets_gb counter reaches half of the maximum value or the maximum value. Access<br>restriction applies. Clears on read. Self-set to 1 on internal event.<br>0b - MMC Transmit Multicast Good Bad Packet Counter Interrupt Status not detected<br>1b - MMC Transmit Multicast Good Bad Packet Counter Interrupt Status detected|
|---|---|
|10<br>TXUCGBPIS|MMC Transmit Unicast Good Bad Packet Counter Interrupt Status This bit is set when the<br>txunicastpackets_gb counter reaches half of the maximum value or the maximum value. Access<br>restriction applies. Clears on read. Self-set to 1 on internal event.<br>0b - MMC Transmit Unicast Good Bad Packet Counter Interrupt Status not detected<br>1b - MMC Transmit Unicast Good Bad Packet Counter Interrupt Status detected|
|9<br>TX1024TMAXO<br>CTGBPIS|MMC Transmit 1024 to Maximum Octet Good Bad Packet Counter Interrupt Status This bit is set when<br>the tx1024tomaxoctets_gb counter reaches half of the maximum value or the maximum value. Access<br>restriction applies. Clears on read. Self-set to 1 on internal event.<br>0b - MMC Transmit 1024 to Maximum Octet Good Bad Packet Counter Interrupt Status not<br>detected<br>1b - MMC Transmit 1024 to Maximum Octet Good Bad Packet Counter Interrupt Status detected|
|8<br>TX512T1023O<br>CTGBPIS|MMC Transmit 512 to 1023 Octet Good Bad Packet Counter Interrupt Status This bit is set when<br>the tx512to1023octets_gb counter reaches half of the maximum value or the maximum value. Access<br>restriction applies. Clears on read. Self-set to 1 on internal event.<br>0b - MMC Transmit 512 to 1023 Octet Good Bad Packet Counter Interrupt Status not detected<br>1b - MMC Transmit 512 to 1023 Octet Good Bad Packet Counter Interrupt Status detected|
|7<br>TX256T511OC<br>TGBPIS|MMC Transmit 256 to 511 Octet Good Bad Packet Counter Interrupt Status This bit is set when<br>the tx256to511octets_gb counter reaches half of the maximum value or the maximum value. Access<br>restriction applies. Clears on read. Self-set to 1 on internal event.<br>0b - MMC Transmit 256 to 511 Octet Good Bad Packet Counter Interrupt Status not detected<br>1b - MMC Transmit 256 to 511 Octet Good Bad Packet Counter Interrupt Status detected|
|6<br>TX128T255OC<br>TGBPIS|MMC Transmit 128 to 255 Octet Good Bad Packet Counter Interrupt Status This bit is set when<br>the tx128to255octets_gb counter reaches half of the maximum value or the maximum value. Access<br>restriction applies. Clears on read. Self-set to 1 on internal event.<br>0b - MMC Transmit 128 to 255 Octet Good Bad Packet Counter Interrupt Status not detected<br>1b - MMC Transmit 128 to 255 Octet Good Bad Packet Counter Interrupt Status detected|
|5<br>TX65T127OCT<br>GBPIS|MMC Transmit 65 to 127 Octet Good Bad Packet Counter Interrupt Status This bit is set when the<br>tx65to127octets_gb counter reaches half the maximum value, and also when it reaches the maximum<br>value. Access restriction applies. Clears on read. Self-set to 1 on internal event.<br>0b - MMC Transmit 65 to 127 Octet Good Bad Packet Counter Interrupt Status not detected<br>1b - MMC Transmit 65 to 127 Octet Good Bad Packet Counter Interrupt Status detected|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3737 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|4<br>TX64OCTGBPI<br>S|MMC Transmit 64 Octet Good Bad Packet Counter Interrupt Status This bit is set when the<br>tx64octets_gb counter reaches half of the maximum value or the maximum value. Access restriction<br>applies. Clears on read. Self-set to 1 on internal event.<br>0b - MMC Transmit 64 Octet Good Bad Packet Counter Interrupt Status not detected<br>1b - MMC Transmit 64 Octet Good Bad Packet Counter Interrupt Status detected|
|3<br>TXMCGPIS|MMC Transmit Multicast Good Packet Counter Interrupt Status This bit is set when the<br>txmulticastpackets_g counter reaches half of the maximum value or the maximum value. Access<br>restriction applies. Clears on read. Self-set to 1 on internal event.<br>0b - MMC Transmit Multicast Good Packet Counter Interrupt Status not detected<br>1b - MMC Transmit Multicast Good Packet Counter Interrupt Status detected|
|2<br>TXBCGPIS|MMC Transmit Broadcast Good Packet Counter Interrupt Status This bit is set when the<br>txbroadcastpackets_g counter reaches half of the maximum value or the maximum value. Access<br>restriction applies. Clears on read. Self-set to 1 on internal event.<br>0b - MMC Transmit Broadcast Good Packet Counter Interrupt Status not detected<br>1b - MMC Transmit Broadcast Good Packet Counter Interrupt Status detected|
|1<br>TXGBPKTIS|MMC Transmit Good Bad Packet Counter Interrupt Status This bit is set when the txpacketcount_gb<br>counter reaches half of the maximum value or the maximum value. Access restriction applies. Clears on<br>read. Self-set to 1 on internal event.<br>0b - MMC Transmit Good Bad Packet Counter Interrupt Status not detected<br>1b - MMC Transmit Good Bad Packet Counter Interrupt Status detected|
|0<br>TXGBOCTIS|MMC Transmit Good Bad Octet Counter Interrupt Status This bit is set when the txoctetcount_gb counter<br>reaches half of the maximum value or the maximum value. Access restriction applies. Clears on read.<br>Self-set to 1 on internal event.<br>0b - MMC Transmit Good Bad Octet Counter Interrupt Status not detected<br>1b - MMC Transmit Good Bad Octet Counter Interrupt Status detected|



# 75.7.99 (MMC_Rx_Interrupt_Mask) 

## Offset 

|Register|Offset|
|---|---|
|MMC_Rx_Interrupt_Mask|70Ch|



## Function 

This register maintains the masks for interrupts generated from all Receive statistics counters. The MMC Receive Interrupt Mask register maintains the masks for the interrupts generated when receive statistic counters reach half of their maximum value or the maximum values. This register is 32 bit wide. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3738 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3739-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv Reserv<br>R Reserved_31_28  e... e... RXCT RXRC RXWD RXVL RXFO RXPA RXOR RXLE RXUC RX102<br>RLP... VER... OGP... ANG... VPIM  USP... ANG... NER... GPIM  4T...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RX512 RX256 RX128 RX65T RX64 RXOSI RXUSI RXJA RXRU RXAL RXCR RXMC RXBC RXGO RXGB RXGB<br>W T1... T5... T2... 12... OCT... ZE... ZE... BER... NTP... GNE... CER... GPIM  GPIM  CTIM  OCT... PKT...<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-28|Reserved.|
|Reserved_31_2<br>8||
|27|Reserved.|
|Reserved_RXL<br>PITRCIM||
|26|Reserved.|
|Reserved_RXL<br>PIUSCIM||
|25<br>RXCTRLPIM|MMC Receive Control Packet Counter Interrupt Mask Setting this bit masks the interrupt when the<br>rxctrlpackets_g counter reaches half of the maximum value or the maximum value.<br>0b - MMC Receive Control Packet Counter Interrupt Mask is disabled<br>1b - MMC Receive Control Packet Counter Interrupt Mask is enabled|
|24<br>RXRCVERRPI<br>M|MMC Receive Error Packet Counter Interrupt Mask Setting this bit masks the interrupt when the<br>rxrcverror counter reaches half of the maximum value or the maximum value.<br>0b - MMC Receive Error Packet Counter Interrupt Mask is disabled<br>1b - MMC Receive Error Packet Counter Interrupt Mask is enabled|
|23<br>RXWDOGPIM|MMC Receive Watchdog Error Packet Counter Interrupt Mask Setting this bit masks the interrupt when<br>the rxwatchdog counter reaches half of the maximum value or the maximum value.<br>0b - MMC Receive Watchdog Error Packet Counter Interrupt Mask is disabled<br>1b - MMC Receive Watchdog Error Packet Counter Interrupt Mask is enabled|
|22<br>RXVLANGBPIM|MMC Receive VLAN Good Bad Packet Counter Interrupt Mask Setting this bit masks the interrupt when<br>the rxvlanpackets_gb counter reaches half of the maximum value or the maximum value.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3739 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function<br>0b - MMC Receive VLAN Good Bad Packet Counter Interrupt Mask is disabled<br>1b - MMC Receive VLAN Good Bad Packet Counter Interrupt Mask is enabled|
|---|---|
|21<br>RXFOVPIM|MMC Receive FIFO Overflow Packet Counter Interrupt Mask Setting this bit masks the interrupt when<br>the rxfifooverflow counter reaches half of the maximum value or the maximum value.<br>0b - MMC Receive FIFO Overflow Packet Counter Interrupt Mask is disabled<br>1b - MMC Receive FIFO Overflow Packet Counter Interrupt Mask is enabled|
|20<br>RXPAUSPIM|MMC Receive Pause Packet Counter Interrupt Mask Setting this bit masks the interrupt when the<br>rxpausepackets counter reaches half of the maximum value or the maximum value.<br>0b - MMC Receive Pause Packet Counter Interrupt Mask is disabled<br>1b - MMC Receive Pause Packet Counter Interrupt Mask is enabled|
|19<br>RXORANGEPI<br>M|MMC Receive Out Of Range Error Packet Counter Interrupt Mask Setting this bit masks the interrupt<br>when the rxoutofrangetype counter reaches half of the maximum value or the maximum value.<br>0b - MMC Receive Out Of Range Error Packet Counter Interrupt Mask is disabled<br>1b - MMC Receive Out Of Range Error Packet Counter Interrupt Mask is enabled|
|18<br>RXLENERPIM|MMC Receive Length Error Packet Counter Interrupt Mask Setting this bit masks the interrupt when the<br>rxlengtherror counter reaches half of the maximum value or the maximum value.<br>0b - MMC Receive Length Error Packet Counter Interrupt Mask is disabled<br>1b - MMC Receive Length Error Packet Counter Interrupt Mask is enabled|
|17<br>RXUCGPIM|MMC Receive Unicast Good Packet Counter Interrupt Mask Setting this bit masks the interrupt when the<br>rxunicastpackets_g counter reaches half of the maximum value or the maximum value.<br>0b - MMC Receive Unicast Good Packet Counter Interrupt Mask is disabled<br>1b - MMC Receive Unicast Good Packet Counter Interrupt Mask is enabled|
|16<br>RX1024TMAXO<br>CTGBPIM|MMC Receive 1024 to Maximum Octet Good Bad Packet Counter Interrupt Mask. Setting this bit<br>masks the interrupt when the rx1024tomaxoctets_gb counter reaches half of the maximum value or<br>the maximum value.<br>0b - MMC Receive 1024 to Maximum Octet Good Bad Packet Counter Interrupt Mask is disabled<br>1b - MMC Receive 1024 to Maximum Octet Good Bad Packet Counter Interrupt Mask is enabled|
|15<br>RX512T1023O<br>CTGBPIM|MMC Receive 512 to 1023 Octet Good Bad Packet Counter Interrupt Mask Setting this bit masks the<br>interrupt when the rx512to1023octets_gb counter reaches half of the maximum value or the maximum<br>value.<br>0b - MMC Receive 512 to 1023 Octet Good Bad Packet Counter Interrupt Mask is disabled<br>1b - MMC Receive 512 to 1023 Octet Good Bad Packet Counter Interrupt Mask is enabled|
|14<br>RX256T511OC<br>TGBPIM|MMC Receive 256 to 511 Octet Good Bad Packet Counter Interrupt Mask Setting this bit masks the<br>interrupt when the rx256to511octets_gb counter reaches half of the maximum value or the maximum<br>value.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3740 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function<br>0b - MMC Receive 256 to 511 Octet Good Bad Packet Counter Interrupt Mask is disabled<br>1b - MMC Receive 256 to 511 Octet Good Bad Packet Counter Interrupt Mask is enabled|
|---|---|
|13<br>RX128T255OC<br>TGBPIM|MMC Receive 128 to 255 Octet Good Bad Packet Counter Interrupt Mask Setting this bit masks the<br>interrupt when the rx128to255octets_gb counter reaches half of the maximum value or the maximum<br>value.<br>0b - MMC Receive 128 to 255 Octet Good Bad Packet Counter Interrupt Mask is disabled<br>1b - MMC Receive 128 to 255 Octet Good Bad Packet Counter Interrupt Mask is enabled|
|12<br>RX65T127OCT<br>GBPIM|MMC Receive 65 to 127 Octet Good Bad Packet Counter Interrupt Mask Setting this bit masks the<br>interrupt when the rx65to127octets_gb counter reaches half of the maximum value or the maximum<br>value.<br>0b - MMC Receive 65 to 127 Octet Good Bad Packet Counter Interrupt Mask is disabled<br>1b - MMC Receive 65 to 127 Octet Good Bad Packet Counter Interrupt Mask is enabled|
|11<br>RX64OCTGBPI<br>M|MMC Receive 64 Octet Good Bad Packet Counter Interrupt Mask Setting this bit masks the interrupt<br>when the rx64octets_gb counter reaches half of the maximum value or the maximum value.<br>0b - MMC Receive 64 Octet Good Bad Packet Counter Interrupt Mask is disabled<br>1b - MMC Receive 64 Octet Good Bad Packet Counter Interrupt Mask is enabled|
|10<br>RXOSIZEGPIM|MMC Receive Oversize Good Packet Counter Interrupt Mask Setting this bit masks the interrupt when<br>the rxoversize_g counter reaches half of the maximum value or the maximum value.<br>0b - MMC Receive Oversize Good Packet Counter Interrupt Mask is disabled<br>1b - MMC Receive Oversize Good Packet Counter Interrupt Mask is enabled|
|9<br>RXUSIZEGPIM|MMC Receive Undersize Good Packet Counter Interrupt Mask Setting this bit masks the interrupt when<br>the rxundersize_g counter reaches half of the maximum value or the maximum value.<br>0b - MMC Receive Undersize Good Packet Counter Interrupt Mask is disabled<br>1b - MMC Receive Undersize Good Packet Counter Interrupt Mask is enabled|
|8<br>RXJABERPIM|MMC Receive Jabber Error Packet Counter Interrupt Mask Setting this bit masks the interrupt when the<br>rxjabbererror counter reaches half of the maximum value or the maximum value.<br>0b - MMC Receive Jabber Error Packet Counter Interrupt Mask is disabled<br>1b - MMC Receive Jabber Error Packet Counter Interrupt Mask is enabled|
|7<br>RXRUNTPIM|MMC Receive Runt Packet Counter Interrupt Mask Setting this bit masks the interrupt when the<br>rxrunterror counter reaches half of the maximum value or the maximum value.<br>0b - MMC Receive Runt Packet Counter Interrupt Mask is disabled<br>1b - MMC Receive Runt Packet Counter Interrupt Mask is enabled|
|6<br>RXALGNERPI<br>M|MMC Receive Alignment Error Packet Counter Interrupt Mask Setting this bit masks the interrupt when<br>the rxalignmenterror counter reaches half of the maximum value or the maximum value.<br>0b - MMC Receive Alignment Error Packet Counter Interrupt Mask is disabled<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3741 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - MMC Receive Alignment Error Packet Counter Interrupt Mask is enabled|
|5<br>RXCRCERPIM|MMC Receive CRC Error Packet Counter Interrupt Mask Setting this bit masks the interrupt when the<br>rxcrcerror counter reaches half of the maximum value or the maximum value.<br>0b - MMC Receive CRC Error Packet Counter Interrupt Mask is disabled<br>1b - MMC Receive CRC Error Packet Counter Interrupt Mask is enabled|
|4<br>RXMCGPIM|MMC Receive Multicast Good Packet Counter Interrupt Mask Setting this bit masks the interrupt when<br>the rxmulticastpackets_g counter reaches half of the maximum value or the maximum value.<br>0b - MMC Receive Multicast Good Packet Counter Interrupt Mask is disabled<br>1b - MMC Receive Multicast Good Packet Counter Interrupt Mask is enabled|
|3<br>RXBCGPIM|MMC Receive Broadcast Good Packet Counter Interrupt Mask Setting this bit masks the interrupt when<br>the rxbroadcastpackets_g counter reaches half of the maximum value or the maximum value.<br>0b - MMC Receive Broadcast Good Packet Counter Interrupt Mask is disabled<br>1b - MMC Receive Broadcast Good Packet Counter Interrupt Mask is enabled|
|2<br>RXGOCTIM|MMC Receive Good Octet Counter Interrupt Mask Setting this bit masks the interrupt when the<br>rxoctetcount_g counter reaches half of the maximum value or the maximum value.<br>0b - MMC Receive Good Octet Counter Interrupt Mask is disabled<br>1b - MMC Receive Good Octet Counter Interrupt Mask is enabled|
|1<br>RXGBOCTIM|MMC Receive Good Bad Octet Counter Interrupt Mask Setting this bit masks the interrupt when the<br>rxoctetcount_gb counter reaches half of the maximum value or the maximum value.<br>0b - MMC Receive Good Bad Octet Counter Interrupt Mask is disabled<br>1b - MMC Receive Good Bad Octet Counter Interrupt Mask is enabled|
|0<br>RXGBPKTIM|MMC Receive Good Bad Packet Counter Interrupt Mask Setting this bit masks the interrupt when the<br>rxpacketcount_gb counter reaches half of the maximum value or the maximum value.<br>0b - MMC Receive Good Bad Packet Counter Interrupt Mask is disabled<br>1b - MMC Receive Good Bad Packet Counter Interrupt Mask is enabled|



# 75.7.100 (MMC_Tx_Interrupt_Mask) 

## Offset 

|Register|Offset|
|---|---|
|MMC_Tx_Interrupt_Mask|710h|



## Function 

This register maintains the masks for interrupts generated from all Transmit statistics counters. The MMC Transmit Interrupt Mask register maintains the masks for the interrupts generated when the transmit statistic counters reach half of their maximum value or the maximum values. This register is 32 bit wide. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3742 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3743-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv Reserv<br>R Reserved_31_28  e... e... TXOSI TXVLA TXPA TXEX TXGP TXGO TXCA TXEX TXLAT TXDE<br>ZE... NG... USP... DEF... KTIM  CTIM  RER... COL... CO... FPIM<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXMC TXSC TXUFL TXBC TXMC TXUC TX102 TX512 TX256 TX128 TX65T TX64O TXMC TXBC TXGB TXGB<br>W OLG... OLG... OW... GBP... GBP... GBP... 4T... T1... T5... T2... 12... CT... GPIM  GPIM  PKT... OCT...<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-28|Reserved.|
|Reserved_31_2<br>8||
|27|Reserved.|
|Reserved_TXL<br>PITRCIM||
|26|Reserved.|
|Reserved_TXL<br>PIUSCIM||
|25<br>TXOSIZEGPIM|MMC Transmit Oversize Good Packet Counter Interrupt Mask Setting this bit masks the interrupt when<br>the txoversize_g counter reaches half of the maximum value or the maximum value.<br>0b - MMC Transmit Oversize Good Packet Counter Interrupt Mask is disabled<br>1b - MMC Transmit Oversize Good Packet Counter Interrupt Mask is enabled|
|24<br>TXVLANGPIM|MMC Transmit VLAN Good Packet Counter Interrupt Mask Setting this bit masks the interrupt when the<br>txvlanpackets_g counter reaches half of the maximum value or the maximum value.<br>0b - MMC Transmit VLAN Good Packet Counter Interrupt Mask is disabled<br>1b - MMC Transmit VLAN Good Packet Counter Interrupt Mask is enabled|
|23<br>TXPAUSPIM|MMC Transmit Pause Packet Counter Interrupt Mask Setting this bit masks the interrupt when the<br>txpausepackets counter reaches half of the maximum value or the maximum value.<br>0b - MMC Transmit Pause Packet Counter Interrupt Mask is disabled<br>1b - MMC Transmit Pause Packet Counter Interrupt Mask is enabled|
|22<br>TXEXDEFPIM|MMC Transmit Excessive Deferral Packet Counter Interrupt Mask Setting this bit masks the interrupt<br>when the txexcessdef counter reaches half of the maximum value or the maximum value.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3743 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function<br>0b - MMC Transmit Excessive Deferral Packet Counter Interrupt Mask is disabled<br>1b - MMC Transmit Excessive Deferral Packet Counter Interrupt Mask is enabled|
|---|---|
|21<br>TXGPKTIM|MMC Transmit Good Packet Counter Interrupt Mask Setting this bit masks the interrupt when the<br>txpacketcount_g counter reaches half of the maximum value or the maximum value.<br>0b - MMC Transmit Good Packet Counter Interrupt Mask is disabled<br>1b - MMC Transmit Good Packet Counter Interrupt Mask is enabled|
|20<br>TXGOCTIM|MMC Transmit Good Octet Counter Interrupt Mask Setting this bit masks the interrupt when the<br>txoctetcount_g counter reaches half of the maximum value or the maximum value.<br>0b - MMC Transmit Good Octet Counter Interrupt Mask is disabled<br>1b - MMC Transmit Good Octet Counter Interrupt Mask is enabled|
|19<br>TXCARERPIM|MMC Transmit Carrier Error Packet Counter Interrupt Mask Setting this bit masks the interrupt when the<br>txcarriererror counter reaches half of the maximum value or the maximum value.<br>0b - MMC Transmit Carrier Error Packet Counter Interrupt Mask is disabled<br>1b - MMC Transmit Carrier Error Packet Counter Interrupt Mask is enabled|
|18<br>TXEXCOLPIM|MMC Transmit Excessive Collision Packet Counter Interrupt Mask Setting this bit masks the interrupt<br>when the txexcesscol counter reaches half of the maximum value or the maximum value.<br>0b - MMC Transmit Excessive Collision Packet Counter Interrupt Mask is disabled<br>1b - MMC Transmit Excessive Collision Packet Counter Interrupt Mask is enabled|
|17<br>TXLATCOLPIM|MMC Transmit Late Collision Packet Counter Interrupt Mask Setting this bit masks the interrupt when the<br>txlatecol counter reaches half of the maximum value or the maximum value.<br>0b - MMC Transmit Late Collision Packet Counter Interrupt Mask is disabled<br>1b - MMC Transmit Late Collision Packet Counter Interrupt Mask is enabled|
|16<br>TXDEFPIM|MMC Transmit Deferred Packet Counter Interrupt Mask Setting this bit masks the interrupt when the<br>txdeferred counter reaches half of the maximum value or the maximum value.<br>0b - MMC Transmit Deferred Packet Counter Interrupt Mask is disabled<br>1b - MMC Transmit Deferred Packet Counter Interrupt Mask is enabled|
|15<br>TXMCOLGPIM|MMC Transmit Multiple Collision Good Packet Counter Interrupt Mask Setting this bit masks the interrupt<br>when the txmulticol_g counter reaches half of the maximum value or the maximum value.<br>0b - MMC Transmit Multiple Collision Good Packet Counter Interrupt Mask is disabled<br>1b - MMC Transmit Multiple Collision Good Packet Counter Interrupt Mask is enabled|
|14<br>TXSCOLGPIM|MMC Transmit Single Collision Good Packet Counter Interrupt Mask Setting this bit masks the interrupt<br>when the txsinglecol_g counter reaches half of the maximum value or the maximum value.<br>0b - MMC Transmit Single Collision Good Packet Counter Interrupt Mask is disabled<br>1b - MMC Transmit Single Collision Good Packet Counter Interrupt Mask is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3744 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|13<br>TXUFLOWERPI<br>M|MMC Transmit Underflow Error Packet Counter Interrupt Mask Setting this bit masks the interrupt when<br>the txunderflowerror counter reaches half of the maximum value or the maximum value.<br>0b - MMC Transmit Underflow Error Packet Counter Interrupt Mask is disabled<br>1b - MMC Transmit Underflow Error Packet Counter Interrupt Mask is enabled|
|12<br>TXBCGBPIM|MMC Transmit Broadcast Good Bad Packet Counter Interrupt Mask Setting this bit masks the interrupt<br>when the txbroadcastpackets_gb counter reaches half of the maximum value or the maximum value.<br>0b - MMC Transmit Broadcast Good Bad Packet Counter Interrupt Mask is disabled<br>1b - MMC Transmit Broadcast Good Bad Packet Counter Interrupt Mask is enabled|
|11<br>TXMCGBPIM|MMC Transmit Multicast Good Bad Packet Counter Interrupt Mask Setting this bit masks the interrupt<br>when the txmulticastpackets_gb counter reaches half of the maximum value or the maximum value.<br>0b - MMC Transmit Multicast Good Bad Packet Counter Interrupt Mask is disabled<br>1b - MMC Transmit Multicast Good Bad Packet Counter Interrupt Mask is enabled|
|10<br>TXUCGBPIM|MMC Transmit Unicast Good Bad Packet Counter Interrupt Mask Setting this bit masks the interrupt<br>when the txunicastpackets_gb counter reaches half of the maximum value or the maximum value.<br>0b - MMC Transmit Unicast Good Bad Packet Counter Interrupt Mask is disabled<br>1b - MMC Transmit Unicast Good Bad Packet Counter Interrupt Mask is enabled|
|9<br>TX1024TMAXO<br>CTGBPIM|MMC Transmit 1024 to Maximum Octet Good Bad Packet Counter Interrupt Mask Setting this bit<br>masks the interrupt when the tx1024tomaxoctets_gb counter reaches half of the maximum value or<br>the maximum value.<br>0b - MMC Transmit 1024 to Maximum Octet Good Bad Packet Counter Interrupt Mask is disabled<br>1b - MMC Transmit 1024 to Maximum Octet Good Bad Packet Counter Interrupt Mask is enabled|
|8<br>TX512T1023O<br>CTGBPIM|MMC Transmit 512 to 1023 Octet Good Bad Packet Counter Interrupt Mask Setting this bit masks the<br>interrupt when the tx512to1023octets_gb counter reaches half of the maximum value or the maximum<br>value.<br>0b - MMC Transmit 512 to 1023 Octet Good Bad Packet Counter Interrupt Mask is disabled<br>1b - MMC Transmit 512 to 1023 Octet Good Bad Packet Counter Interrupt Mask is enabled|
|7<br>TX256T511OC<br>TGBPIM|MMC Transmit 256 to 511 Octet Good Bad Packet Counter Interrupt Mask Setting this bit masks the<br>interrupt when the tx256to511octets_gb counter reaches half of the maximum value or the maximum<br>value.<br>0b - MMC Transmit 256 to 511 Octet Good Bad Packet Counter Interrupt Mask is disabled<br>1b - MMC Transmit 256 to 511 Octet Good Bad Packet Counter Interrupt Mask is enabled|
|6<br>TX128T255OC<br>TGBPIM|MMC Transmit 128 to 255 Octet Good Bad Packet Counter Interrupt Mask Setting this bit masks the<br>interrupt when the tx128to255octets_gb counter reaches half of the maximum value or the maximum<br>value.<br>0b - MMC Transmit 128 to 255 Octet Good Bad Packet Counter Interrupt Mask is disabled<br>1b - MMC Transmit 128 to 255 Octet Good Bad Packet Counter Interrupt Mask is enabled<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3745 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|5<br>TX65T127OCT<br>GBPIM|MMC Transmit 65 to 127 Octet Good Bad Packet Counter Interrupt Mask Setting this bit masks the<br>interrupt when the tx65to127octets_gb counter reaches half of the maximum value or the maximum<br>value.<br>0b - MMC Transmit 65 to 127 Octet Good Bad Packet Counter Interrupt Mask is disabled<br>1b - MMC Transmit 65 to 127 Octet Good Bad Packet Counter Interrupt Mask is enabled|
|4<br>TX64OCTGBPI<br>M|MMC Transmit 64 Octet Good Bad Packet Counter Interrupt Mask Setting this bit masks the interrupt<br>when the tx64octets_gb counter reaches half of the maximum value or the maximum value.<br>0b - MMC Transmit 64 Octet Good Bad Packet Counter Interrupt Mask is disabled<br>1b - MMC Transmit 64 Octet Good Bad Packet Counter Interrupt Mask is enabled|
|3<br>TXMCGPIM|MMC Transmit Multicast Good Packet Counter Interrupt Mask Setting this bit masks the interrupt when<br>the txmulticastpackets_g counter reaches half of the maximum value or the maximum value.<br>0b - MMC Transmit Multicast Good Packet Counter Interrupt Mask is disabled<br>1b - MMC Transmit Multicast Good Packet Counter Interrupt Mask is enabled|
|2<br>TXBCGPIM|MMC Transmit Broadcast Good Packet Counter Interrupt Mask Setting this bit masks the interrupt when<br>the txbroadcastpackets_g counter reaches half of the maximum value or the maximum value.<br>0b - MMC Transmit Broadcast Good Packet Counter Interrupt Mask is disabled<br>1b - MMC Transmit Broadcast Good Packet Counter Interrupt Mask is enabled|
|1<br>TXGBPKTIM|MMC Transmit Good Bad Packet Counter Interrupt Mask Setting this bit masks the interrupt when the<br>txpacketcount_gb counter reaches half of the maximum value or the maximum value.<br>0b - MMC Transmit Good Bad Packet Counter Interrupt Mask is disabled<br>1b - MMC Transmit Good Bad Packet Counter Interrupt Mask is enabled|
|0<br>TXGBOCTIM|MMC Transmit Good Bad Octet Counter Interrupt Mask Setting this bit masks the interrupt when the<br>txoctetcount_gb counter reaches half of the maximum value or the maximum value.<br>0b - MMC Transmit Good Bad Octet Counter Interrupt Mask is disabled<br>1b - MMC Transmit Good Bad Octet Counter Interrupt Mask is enabled|



# 75.7.101 (Tx_Octet_Count_Good_Bad) 

## Offset 

|Register|Offset|
|---|---|
|Tx_Octet_Count_Good_|714h|
|Bad||



## Function 

This register provides the number of bytes transmitted by the DWC_ether_qos, exclusive of preamble and retried bytes, in good and bad packets. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3746 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3747-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXOCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXOCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Tx Octet Count Good Bad This field indicates the number of bytes transmitted, exclusive of preamble|
|TXOCTGB|and retried bytes, in good and bad packets.|



# 75.7.102 (Tx_Packet_Count_Good_Bad) 

## Offset 

|Register|Offset|
|---|---|
|Tx_Packet_Count_Good|718h|
|_Bad||



## Function 

This register provides the number of good and bad packets transmitted by DWC_ether_qos, exclusive of retried packets. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3747-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXPKTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXPKTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3747 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0<br>TXPKTGB|Tx Packet Count Good Bad This field indicates the number of good and bad packets transmitted,<br>exclusive of retried packets.|



# 75.7.103 (Tx_Broadcast_Packets_Good) 

## Offset 

|Register|Offset|
|---|---|
|Tx_Broadcast_Packets_|71Ch|
|Good||



## Function 

This register provides the number of good broadcast packets transmitted by DWC_ether_qos. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||TXBC|ASTG||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||TXBC|ASTG||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Tx Broadcast Packets Good This field indicates the number of good broadcast packets transmitted.|
|TXBCASTG||



# 75.7.104 (Tx_Multicast_Packets_Good) 

## Offset 

|Register|Offset|
|---|---|
|Tx_Multicast_Packets_G|720h|
|ood||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3748 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Function 

This register provides the number of good multicast packets transmitted by DWC_ether_qos. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3749-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXMCASTG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXMCASTG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3749-07.png)


<!-- Start of picture text -->
Field Function<br>31-0 Tx Multicast Packets Good This field indicates the number of good multicast packets transmitted.<br>TXMCASTG<br><!-- End of picture text -->

# 75.7.105 (Tx_64Octets_Packets_Good_Bad) 

## Offset 

|Register|Offset|
|---|---|
|Tx_64Octets_Packets_G|724h|
|ood_Bad||



## Function 

This register provides the number of good and bad packets transmitted by DWC_ether_qos with length 64 bytes, exclusive of preamble and retried packets. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3749-14.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TX64OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TX64OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3749 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0|Tx 64Octets Packets Good_Bad This field indicates the number of good and bad packets transmitted|
|TX64OCTGB|with length 64 bytes, exclusive of preamble and retried packets.|



# 75.7.106 (Tx_65To127Octets_Packets_Good_Bad) 

## Offset 

|Register|Offset|
|---|---|
|Tx_65To127Octets_Pack|728h|
|ets_Good_Bad||



## Function 

This register provides the number of good and bad packets transmitted by DWC_ether_qos with length between 65 and 127 (inclusive) bytes, exclusive of preamble and retried packets. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||TX65_12|7OCTGB||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||TX65_12|7OCTGB||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Tx 65To127Octets Packets Good Bad This field indicates the number of good and bad packets|
|TX65_127OCT<br>GB|transmitted with length between 65 and 127 (inclusive) bytes, exclusive of preamble and retried packets.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3750 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.107 (Tx_128To255Octets_Packets_Good_Bad) 

## Offset 

|Register|Offset|
|---|---|
|Tx_128To255Octets_Pac|72Ch|
|kets_Good_Bad||



## Function 

This register provides the number of good and bad packets transmitted by DWC_ether_qos with length between 128 to 255 (inclusive) bytes, exclusive of preamble and retried packets. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3751-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TX128_255OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TX128_255OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Tx 128To255Octets Packets Good Bad This field indicates the number of good and bad packets|
|TX128_255OCT<br>GB|transmitted with length between 128 and 255 (inclusive) bytes, exclusive of preamble and retried<br>packets.|



# 75.7.108 (Tx_256To511Octets_Packets_Good_Bad) 

## Offset 

|Register|Offset|
|---|---|
|Tx_256To511Octets_Pac|730h|
|kets_Good_Bad||



## Function 

This register provides the number of good and bad packets transmitted by DWC_ether_qos with length between 256 to 511 (inclusive) bytes, exclusive of preamble and retried packets. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3751 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3752-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TX256_511OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TX256_511OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Tx 256To511Octets Packets Good Bad This field indicates the number of good and bad packets|
|TX256_511OCT<br>GB|transmitted with length between 256 and 511 (inclusive) bytes, exclusive of preamble and retried<br>packets.|



# 75.7.109 (Tx_512To1023Octets_Packets_Good_Bad) 

## Offset 

|Register|Offset|
|---|---|
|Tx_512To1023Octets_P|734h|
|ackets_Good_Bad||



## Function 

This register provides the number of good and bad packets transmitted by DWC_ether_qos with length 512 to 1023 (inclusive) bytes, exclusive of preamble and retried packets. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3752-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TX512_1023OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TX512_1023OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3752 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0|Tx 512To1023Octets Packets Good Bad This field indicates the number of good and bad packets|
|TX512_1023OC<br>TGB|transmitted with length between 512 and 1023 (inclusive) bytes, exclusive of preamble and retried<br>packets.|



# 75.7.110 (Tx_1024ToMaxOctets_Packets_Good_Bad) 

## Offset 

|Register|Offset|
|---|---|
|Tx_1024ToMaxOctets_P|738h|
|ackets_Good_Bad||



## Function 

This register provides the number of good and bad packets transmitted by DWC_ether_qos with length 1024 to maxsize (inclusive) bytes, exclusive of preamble and retried packets. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||T|X1024_M|AXOCTGB||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||||T|X1024_M|AXOCTGB||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function|
|---|---|
|31-0|Tx 1024ToMaxOctets Packets Good Bad This field indicates the number of good and bad packets|
|TX1024_MAXO<br>CTGB|transmitted with length between 1024 and maxsize (inclusive) bytes, exclusive of preamble and retried<br>packets.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3753 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.111 (Tx_Unicast_Packets_Good_Bad) 

## Offset 

|Register|Offset|
|---|---|
|Tx_Unicast_Packets_Go|73Ch|
|od_Bad||



## Function 

This register provides the number of good and bad unicast packets transmitted by DWC_ether_qos. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||TXUCA|STGB||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||TXUCA|STGB||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0<br>TXUCASTGB|Tx Unicast Packets Good Bad This field indicates the number of good and bad unicast packets<br>transmitted.|



# 75.7.112 (Tx_Multicast_Packets_Good_Bad) 

## Offset 

|Register|Offset|
|---|---|
|Tx_Multicast_Packets_G|740h|
|ood_Bad||



## Function 

This register provides the number of good and bad multicast packets transmitted by DWC_ether_qos. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3754 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3755-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXMCASTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXMCASTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0<br>TXMCASTGB|Tx Multicast Packets Good Bad This field indicates the number of good and bad multicast packets<br>transmitted.|



# 75.7.113 (Tx_Broadcast_Packets_Good_Bad) 

## Offset 

|Register|Offset|
|---|---|
|Tx_Broadcast_Packets_|744h|
|Good_Bad||



## Function 

This register provides the number of good and bad broadcast packets transmitted by DWC_ether_qos. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3755-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXBCASTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXBCASTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3755 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0<br>TXBCASTGB|Tx Broadcast Packets Good Bad This field indicates the number of good and bad broadcast packets<br>transmitted.|



# 75.7.114 (Tx_Underflow_Error_Packets) 

## Offset 

|Register|Offset|
|---|---|
|Tx_Underflow_Error_Pac|748h|
|kets||



## Function 

This register provides the number of packets aborted by DWC_ether_qos because of packets underflow error. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||TXUND|RFLW||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||TXUND|RFLW||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0<br>TXUNDRFLW|Tx Underflow Error Packets This field indicates the number of packets aborted because of packets<br>underflow error.|



# 75.7.115 (Tx_Single_Collision_Good_Packets) 

## Offset 

|Register|Offset|
|---|---|
|Tx_Single_Collision_Goo|74Ch|
|d_Packets||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3756 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Function 

This register provides the number of successfully transmitted packets by DWC_ether_qos after a single collision in the half-duplex mode. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3757-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXSNGLCOLG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXSNGLCOLG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Tx Single Collision Good Packets This field indicates the number of successfully transmitted packets|
|TXSNGLCOLG|after a single collision in the half-duplex mode.|



# 75.7.116 (Tx_Multiple_Collision_Good_Packets) 

## Offset 

|Register|Offset|
|---|---|
|Tx_Multiple_Collision_Go|750h|
|od_Packets||



## Function 

This register provides the number of successfully transmitted packets by DWC_ether_qos after multiple collisions in the half-duplex mode. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3757 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3758-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXMULTCOLG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXMULTCOLG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Tx Multiple Collision Good Packets This field indicates the number of successfully transmitted packets|
|TXMULTCOLG|after multiple collisions in the half-duplex mode.|



# 75.7.117 (Tx_Deferred_Packets) 

## Offset 

|Register|Offset|
|---|---|
|Tx_Deferred_Packets|754h|



## Function 

This register provides the number of successfully transmitted by DWC_ether_qos after a deferral in the half-duplex mode. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||TXDE|FRD||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||TXDE|FRD||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3758 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0<br>TXDEFRD|Tx Deferred Packets This field indicates the number of successfully transmitted after a deferral in the<br>half-duplex mode.|



# 75.7.118 (Tx_Late_Collision_Packets) 

## Offset 

|Register|Offset|
|---|---|
|Tx_Late_Collision_Packe|758h|
|ts||



## Function 

This register provides the number of packets aborted by DWC_ether_qos because of late collision error. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||TXLAT|ECOL||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||TXLAT|ECOL||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Tx Late Collision Packets This field indicates the number of packets aborted because of late collision|
|TXLATECOL|error.|



# 75.7.119 (Tx_Excessive_Collision_Packets) 

## Offset 

|Register|Offset|
|---|---|
|Tx_Excessive_Collision_|75Ch|
|Packets||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3759 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Function 

This register provides the number of packets aborted by DWC_ether_qos because of excessive (16) collision errors. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3760-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXEXSCOL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXEXSCOL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Tx Excessive Collision Packets This field indicates the number of packets aborted because of excessive|
|TXEXSCOL|(16) collision errors.|



# 75.7.120 (Tx_Carrier_Error_Packets) 

## Offset 

|Register|Offset|
|---|---|
|Tx_Carrier_Error_Packet|760h|
|s||



## Function 

This register provides the number of packets aborted by DWC_ether_qos because of carrier sense error (no carrier or loss of carrier). 

## Diagram 

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

3760 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0|Tx Carrier Error Packets This field indicates the number of packets aborted because of carrier sense|
|TXCARR|error (no carrier or loss of carrier).|



# 75.7.121 (Tx_Octet_Count_Good) 

## Offset 

|Register|Offset|
|---|---|
|Tx_Octet_Count_Good|764h|



## Function 

This register provides the number of bytes transmitted by DWC_ether_qos, exclusive of preamble, only in good packets. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||TXO|CTG||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||TXO|CTG||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Tx Octet Count Good This field indicates the number of bytes transmitted, exclusive of preamble, only in|
|TXOCTG|good packets.|



# 75.7.122 (Tx_Packet_Count_Good) 

## Offset 

|Register|Offset|
|---|---|
|Tx_Packet_Count_Good|768h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3761 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Function 

This register provides the number of good packets transmitted by DWC_ether_qos. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3762-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXPKTG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXPKTG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Tx Packet Count Good This field indicates the number of good packets transmitted.|
|TXPKTG||



# 75.7.123 (Tx_Excessive_Deferral_Error) 

## Offset 

|Register|Offset|
|---|---|
|Tx_Excessive_Deferral_<br>Error|76Ch|



## Function 

This register provides the number of packets aborted by DWC_ether_qos because of excessive deferral error (deferred for more than two max-sized packet times). 

## Diagram 

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

3762 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0|Tx Excessive Deferral Error This field indicates the number of packets aborted because of excessive|
|TXEXSDEF|deferral error (deferred for more than two max-sized packet times).|



# 75.7.124 (Tx_Pause_Packets) 

## Offset 

|Register|Offset|
|---|---|
|Tx_Pause_Packets|770h|



## Function 

This register provides the number of good Pause packets transmitted by DWC_ether_qos. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3763-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXPAUSE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXPAUSE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Tx Pause Packets This field indicates the number of good Pause packets transmitted.|
|TXPAUSE||



# 75.7.125 (Tx_VLAN_Packets_Good) 

## Offset 

|Register|Offset|
|---|---|
|Tx_VLAN_Packets_Good|774h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3763 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Function 

This register provides the number of good VLAN packets transmitted by DWC_ether_qos. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3764-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXVLANG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXVLANG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Tx VLAN Packets Good This field provides the number of good VLAN packets transmitted.|
|TXVLANG||



# 75.7.126 (Tx_OSize_Packets_Good) 

## Offset 

|Register|Offset|
|---|---|
|Tx_OSize_Packets_Goo<br>d|778h|



## Function 

This register provides the number of packets transmitted by DWC_ether_qos without errors and with length greater than the maxsize (1,518 or 1,522 bytes for VLAN tagged packets; 2000 bytes if enabled in S2KP bit of the MAC_Configuration register). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3764 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3765-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXOSIZG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXOSIZG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Tx OSize Packets Good This field indicates the number of packets transmitted without errors and with|
|TXOSIZG|length greater than the maxsize (1,518 or 1,522 bytes for VLAN tagged packets; 2000 bytes if enabled in<br>S2KP bit of the MAC_Configuration register).|



# 75.7.127 (Rx_Packets_Count_Good_Bad) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Packets_Count_Goo|780h|
|d_Bad||



## Function 

This register provides the number of good and bad packets received by DWC_ether_qos. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||RXPK|TGB||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||RXPK|TGB||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3765 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0|Rx Packets Count Good Bad This field indicates the number of good and bad packets received.|
|RXPKTGB||



# 75.7.128 (Rx_Octet_Count_Good_Bad) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Octet_Count_Good_|784h|
|Bad||



## Function 

This register provides the number of bytes received by DWC_ther_qos, exclusive of preamble, in good and bad packets. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||RXO|CTGB||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||RXO|CTGB||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Rx Octet Count Good Bad This field indicates the number of bytes received, exclusive of preamble, in|
|RXOCTGB|good and bad packets.|



# 75.7.129 (Rx_Octet_Count_Good) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Octet_Count_Good|788h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3766 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Function 

This register provides the number of bytes received by DWC_ether_qos, exclusive of preamble, only in good packets. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3767-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RXOCTG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXOCTG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Rx Octet Count Good This field indicates the number of bytes received, exclusive of preamble, only in|
|RXOCTG|good packets.|



# 75.7.130 (Rx_Broadcast_Packets_Good) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Broadcast_Packets_|78Ch|
|Good||



## Function 

This register provides the number of good broadcast packets received by DWC_ether_qos. 

## Diagram 

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

3767 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0|Rx Broadcast Packets Good This field indicates the number of good broadcast packets received.|
|RXBCASTG||



# 75.7.131 (Rx_Multicast_Packets_Good) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Multicast_Packets_G|790h|
|ood||



## Function 

This register provides the number of good multicast packets received by DWC_ether_qos. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3768-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RXMCASTG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXMCASTG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Rx Multicast Packets Good This field indicates the number of good multicast packets received.|
|RXMCASTG||



# 75.7.132 (Rx_CRC_Error_Packets) 

## Offset 

|Register|Offset|
|---|---|
|Rx_CRC_Error_Packets|794h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3768 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Function 

This register provides the number of packets received by DWC_ether_qos with CRC error. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3769-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RXCRCERR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXCRCERR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Rx CRC Error Packets This field indicates the number of packets received with CRC error.|
|RXCRCERR||



# 75.7.133 (Rx_Alignment_Error_Packets) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Alignment_Error_Pac|798h|
|kets||



## Function 

This register provides the number of packets received by DWC_ether_qos with alignment (dribble) error. It is valid only in 10/100 mode. 

## Diagram 

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

3769 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0|Rx Alignment Error Packets This field indicates the number of packets received with alignment (dribble)|
|RXALGNERR|error. It is valid only in 10/100 mode.|



# 75.7.134 (Rx_Runt_Error_Packets) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Runt_Error_Packets|79Ch|



## Function 

This register provides the number of packets received by DWC_ether_qos with runt (length less than 64 bytes and CRC error) error. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||RXRUN|TERR||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||RXRUN|TERR||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Rx Runt Error Packets This field indicates the number of packets received with runt (length less than 64|
|RXRUNTERR|bytes and CRC error) error.|



# 75.7.135 (Rx_Jabber_Error_Packets) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Jabber_Error_Packet|7A0h|
|s||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3770 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Function 

This register provides the number of giant packets received by DWC_ether_qos with length (including CRC) greater than 1,518 bytes (1,522 bytes for VLAN tagged) and with CRC error. If Jumbo Packet mode is enabled, packets of length greater than 9,018 bytes (9,022 bytes for VLAN tagged) are considered as giant packets. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||RXJA|BERR||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||RXJA|BERR||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Rx Jabber Error Packets This field indicates the number of giant packets received with length (including|
|RXJABERR|CRC) greater than 1,518 bytes (1,522 bytes for VLAN tagged) and with CRC error. If Jumbo Packet<br>mode is enabled, packets of length greater than 9,018 bytes (9,022 bytes for VLAN tagged) are<br>considered as giant packets.|



# 75.7.136 (Rx_Undersize_Packets_Good) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Undersize_Packets_|7A4h|
|Good||



## Function 

This register provides the number of packets received by DWC_ether_qos with length less than 64 bytes, without any errors. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3771 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3772-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RXUNDERSZG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXUNDERSZG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Rx Undersize Packets Good This field indicates the number of packets received with length less than 64|
|RXUNDERSZG|bytes, without any errors.|



# 75.7.137 (Rx_Oversize_Packets_Good) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Oversize_Packets_G|7A8h|
|ood||



## Function 

This register provides the number of packets received by DWC_ether_qos without errors, with length greater than the maxsize (1,518 bytes or 1,522 bytes for VLAN tagged packets; 2000 bytes if enabled in the S2KP bit of the MAC_Configuration register). 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3772-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RXOVERSZG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXOVERSZG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3772 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0|Rx Oversize Packets Good This field indicates the number of packets received without errors, with length|
|RXOVERSZG|greater than the maxsize (1,518 bytes or 1,522 bytes for VLAN tagged packets; 2000 bytes if enabled in<br>the S2KP bit of the MAC_Configuration register).|



# 75.7.138 (Rx_64Octets_Packets_Good_Bad) 

## Offset 

|Register|Offset|
|---|---|
|Rx_64Octets_Packets_G|7ACh|
|ood_Bad||



## Function 

This register provides the number of good and bad packets received by DWC_ether_qos with length 64 bytes, exclusive of the preamble. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||RX64O|CTGB||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||RX64O|CTGB||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0<br>RX64OCTGB|Rx 64 Octets Packets Good Bad This field indicates the number of good and bad packets received with<br>length 64 bytes, exclusive of the preamble.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3773 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.139 (Rx_65To127Octets_Packets_Good_Bad) 

## Offset 

|Register|Offset|
|---|---|
|Rx_65To127Octets_Pac|7B0h|
|kets_Good_Bad||



## Function 

This register provides the number of good and bad packets received by DWC_ether_qos with length between 65 and 127 (inclusive) bytes, exclusive of the preamble. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3774-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RX65_127OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RX65_127OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Rx 65-127 Octets Packets Good Bad This field indicates the number of good and bad packets received|
|RX65_127OCT<br>GB|with length between 65 and 127 (inclusive) bytes, exclusive of the preamble.|



# 75.7.140 (Rx_128To255Octets_Packets_Good_Bad) 

## Offset 

|Register|Offset|
|---|---|
|Rx_128To255Octets_Pa|7B4h|
|ckets_Good_Bad||



## Function 

This register provides the number of good and bad packets received by DWC_ether_qos with length between 128 and 255 (inclusive) bytes, exclusive of the preamble. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3774 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3775-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RX128_255OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RX128_255OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Rx 128-255 Octets Packets Good Bad This field indicates the number of good and bad packets received|
|RX128_255OC<br>TGB|with length between 128 and 255 (inclusive) bytes, exclusive of the preamble.|



# 75.7.141 (Rx_256To511Octets_Packets_Good_Bad) 

## Offset 

|Register|Offset|
|---|---|
|Rx_256To511Octets_Pa|7B8h|
|ckets_Good_Bad||



## Function 

This register provides the number of good and bad packets received by DWC_ether_qos with length between 256 and 511 (inclusive) bytes, exclusive of the preamble. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3775-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RX256_511OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RX256_511OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3775 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0|Rx 256-511 Octets Packets Good Bad This field indicates the number of good and bad packets received|
|RX256_511OC<br>TGB|with length between 256 and 511 (inclusive) bytes, exclusive of the preamble.|



# 75.7.142 (Rx_512To1023Octets_Packets_Good_Bad) 

## Offset 

|Register|Offset|
|---|---|
|Rx_512To1023Octets_P|7BCh|
|ackets_Good_Bad||



## Function 

This register provides the number of good and bad packets received by DWC_ether_qos with length between 512 and 1023 (inclusive) bytes, exclusive of the preamble. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||R|X512_10|23OCTGB||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||||R|X512_10|23OCTGB||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function|
|---|---|
|31-0|RX 512-1023 Octets Packets Good Bad This field indicates the number of good and bad packets|
|RX512_1023O<br>CTGB|received with length between 512 and 1023 (inclusive) bytes, exclusive of the preamble.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3776 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.143 (Rx_1024ToMaxOctets_Packets_Good_Bad) 

## Offset 

|Register|Offset|
|---|---|
|Rx_1024ToMaxOctets_P|7C0h|
|ackets_Good_Bad||



## Function 

This register provides the number of good and bad packets received by DWC_ether_qos with length between 1024 and maxsize (inclusive) bytes, exclusive of the preamble. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3777-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RX1024_MAXOCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RX1024_MAXOCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0<br>RX1024_MAXO<br>CTGB|Rx 1024-Max Octets Good Bad This field indicates the number of good and bad packets received with<br>length between 1024 and maxsize (inclusive) bytes, exclusive of the preamble.|



# 75.7.144 (Rx_Unicast_Packets_Good) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Unicast_Packets_Go|7C4h|
|od||



## Function 

This register provides the number of good unicast packets received by DWC_ether_qos. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3777 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3778-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RXUCASTG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXUCASTG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Rx Unicast Packets Good This field indicates the number of good unicast packets received.|
|RXUCASTG||



# 75.7.145 (Rx_Length_Error_Packets) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Length_Error_Packet|7C8h|
|s||



## Function 

This register provides the number of packets received by DWC_ether_qos with length error (Length Type field not equal to packet size), for all packets with valid length field. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3778-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RXLENERR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXLENERR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3778 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0|Rx Length Error Packets This field indicates the number of packets received with length error (Length|
|RXLENERR|Type field not equal to packet size), for all packets with valid length field.|



# 75.7.146 (Rx_Out_Of_Range_Type_Packets) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Out_Of_Range_Type<br>_Packets|7CCh|



## Function 

This register provides the number of packets received by DWC_ether_qos with length field not equal to the valid packet size (greater than 1,500 but less than 1,536). 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3779-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RXOUTOFRNG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXOUTOFRNG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Rx Out of Range Type Packet This field indicates the number of packets received with length field not|
|RXOUTOFRNG|equal to the valid packet size (greater than 1,500 but less than 1,536).|



# 75.7.147 (Rx_Pause_Packets) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Pause_Packets|7D0h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3779 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Function 

This register provides the number of good and valid Pause packets received by DWC_ether_qos. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3780-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RXPAUSEPKT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXPAUSEPKT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Rx Pause Packets This field indicates the number of good and valid Pause packets received.|
|RXPAUSEPKT||



# 75.7.148 (Rx_FIFO_Overflow_Packets) 

## Offset 

|Register|Offset|
|---|---|
|Rx_FIFO_Overflow_Pack|7D4h|
|ets||



## Function 

This register provides the number of missed received packets because of FIFO overflow in DWC_ether_qos. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||RXFIF|OOVFL||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||RXFIF|OOVFL||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3780 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0<br>RXFIFOOVFL|Rx FIFO Overflow Packets This field indicates the number of missed received packets because of FIFO<br>overflow.|



# 75.7.149 (Rx_VLAN_Packets_Good_Bad) 

## Offset 

|Register|Offset|
|---|---|
|Rx_VLAN_Packets_Goo|7D8h|
|d_Bad||



## Function 

This register provides the number of good and bad VLAN packets received by DWC_ether_qos. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||RXVLAN|PKTGB||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||RXVLAN|PKTGB||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Rx VLAN Packets Good Bad This field indicates the number of good and bad VLAN packets received.|
|RXVLANPKTG<br>B||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3781 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.150 (Rx_Watchdog_Error_Packets) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Watchdog_Error_Pac|7DCh|
|kets||



## Function 

This register provides the number of packets received by DWC_ether_qos with error because of watchdog timeout error (packets with a data load larger than 2,048 bytes (when JE and WD bits are reset in MAC_Configuration register), 10,240 bytes (when JE bit is set and WD bit is reset in MAC_Configuration register), 16,384 bytes (when WD bit is set in MAC_Configuration register) or the value programmed in the MAC_Watchdog_Timeout register). 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3782-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RXWDGERR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXWDGERR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0<br>RXWDGERR|Rx Watchdog Error Packets This field indicates the number of packets received with error because<br>of watchdog timeout error (packets with a data load larger than 2,048 bytes (when JE and WD bits<br>are reset in MAC_Configuration register), 10,240 bytes (when JE bit is set and WD bit is reset in|
||MAC_Configuration register), 16,384 bytes (when WD bit is set in MAC_Configuration register) or the<br>value programmed in the MAC_Watchdog_Timeout register).|



# 75.7.151 (Rx_Receive_Error_Packets) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Receive_Error_Pack|7E0h|
|ets||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3782 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Function 

This register provides the number of packets received by DWC_ether_qos with Receive error or Packet Extension error on the GMII or MII interface. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3783-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RXRCVERR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXRCVERR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Rx Receive Error Packets This field indicates the number of packets received with Receive error or|
|RXRCVERR|Packet Extension error on the GMII or MII interface.|



# 75.7.152 (Rx_Control_Packets_Good) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Control_Packets_Go|7E4h|
|od||



## Function 

This register provides the number of good control packets received by DWC_ether_qos. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||RXCT|RLG||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||RXCT|RLG||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3783 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0|Rx Control Packets Good This field indicates the number of good control packets received.|
|RXCTRLG||



# 75.7.153 (MMC_FPE_Tx_Interrupt) 

## Offset 

|Register|Offset|
|---|---|
|MMC_FPE_Tx_Interrupt|8A0h|



## Function 

This register maintains the interrupts generated from all FPE related Transmit statistics counters. The MMC FPE Transmit Interrupt register maintains the interrupts generated when transmit statistic counters reach half their maximum values (0x8000_0000 for 32 bit counter and 0x8000 for 16 bit counter), and when they cross their maximum values (0xFFFF_FFFF for 32-bit counter and 0xFFFF for 16-bit counter). When Counter Stop Rollover is set, the interrupts are set but the counter remains at all-ones. The MMC FPE Transmit Interrupt register is a 32 bit register. An interrupt bit is cleared when the respective MMC counter that caused the interrupt is read. The least significant byte lane (Bits[7:0]) of the respective counter must be read to clear the interrupt bit. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3784-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_31_2  HRCIS  FCIS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-2|Reserved.|
|Reserved_31_2||
|1<br>HRCIS|MMC Tx Hold Request Counter Interrupt Status This bit is set when the Tx_Hold_Req_Cntr counter<br>reaches half of the maximum value or the maximum value. Access restriction applies. Clears on read.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3784 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||Self-set to 1 on internal event. Exists when any one of the RX/TX MMC counters are enabled during FPE<br>with AV_EST Enabled configuration.<br>0b - MMC Tx Hold Request Counter Interrupt Status not detected<br>1b - MMC Tx Hold Request Counter Interrupt Status detected|
|0<br>FCIS|MMC Tx FPE Fragment Counter Interrupt status This bit is set when the Tx_FPE_Fragment_Cntr counter<br>reaches half of the maximum value or the maximum value. Access restriction applies. Clears on read.<br>Self-set to 1 on internal event. Exists when any one of the RX/TX MMC counters are enabled during FPE<br>Enabled configuration.|
||0b - MMC Tx FPE Fragment Counter Interrupt status not detected|
||1b - MMC Tx FPE Fragment Counter Interrupt status detected|



# 75.7.154 (MMC_FPE_Tx_Interrupt_Mask) 

## Offset 

|Register|Offset|
|---|---|
|MMC_FPE_Tx_Interrupt_|8A4h|
|Mask||



## Function 

This register maintains the masks for interrupts generated from all FPE related Transmit statistics counters. The MMC Receive Interrupt Mask register maintains the masks for the interrupts generated when FPE related receive statistic counters reach half of their maximum value or the maximum values. This register is 32 bit wide. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3785-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_31_2<br>HRCIM  FCIM<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3785 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-2|Reserved.|
|Reserved_31_2||
|1<br>HRCIM|MMC Transmit Hold Request Counter Interrupt Mask Setting this bit masks the interrupt when the<br>Tx_Hold_Req_Cntr counter reaches half of the maximum value or the maximum value. Exists when any<br>one of the RX/TX MMC counters are enabled during FPE with AV_EST Enabled configuration.<br>0b - MMC Transmit Hold Request Counter Interrupt Mask is disabled<br>1b - MMC Transmit Hold Request Counter Interrupt Mask is enabled|
|0<br>FCIM|MMC Transmit Fragment Counter Interrupt Mask Setting this bit masks the interrupt when the<br>Tx_FPE_Fragment_Cntr counter reaches half of the maximum value or the maximum value. Exists when<br>any one of the RX/TX MMC counters are enabled during FPE Enabled configuration.<br>0b - MMC Transmit Fragment Counter Interrupt Mask is disabled<br>1b - MMC Transmit Fragment Counter Interrupt Mask is enabled|



# 75.7.155 (MMC_Tx_FPE_Fragment_Cntr) 

## Offset 

|Register|Offset|
|---|---|
|MMC_Tx_FPE_Fragment<br>_Cntr|8A8h|



## Function 

This register provides the number of additional mPackets transmitted due to preemption. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||TXF|FC||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||TXF|FC||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3786 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0|Tx FPE Fragment counter This field indicates the number of additional mPackets that has been|
|TXFFC|transmitted due to preemption Exists when any one of the RX/TX MMC counters are enabled during<br>FPE Enabled configuration.|



# 75.7.156 (MMC_Tx_Hold_Req_Cntr) 

## Offset 

|Register|Offset|
|---|---|
|MMC_Tx_Hold_Req_Cnt|8ACh|
|r||



## Function 

This register provides the count of number of times a hold request is given to MAC 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||TXH|RC||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||TXH|RC||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Tx Hold Request Counter This field indicates count of number of a hold request is given to MAC. Exists|
|TXHRC|when any one of the RX/TX MMC counters are enabled during FPE with AV_EST Enabled configuration.|



# 75.7.157 (MMC_FPE_Rx_Interrupt) 

## Offset 

|Register|Offset|
|---|---|
|MMC_FPE_Rx_Interrupt|8C0h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3787 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Function 

This register maintains the interrupts generated from all FPE related Receive statistics counters. The MMC FPE Receive Interrupt register maintains the interrupts generated when transmit statistic counters reach half their maximum values (0x8000_0000 for 32 bit counter and 0x8000 for 16 bit counter), and when they cross their maximum values (0xFFFF_FFFF for 32-bit counter and 0xFFFF for 16-bit counter). When Counter Stop Rollover is set, the interrupts are set but the counter remains at all-ones. The MMC FPE Receive Interrupt register is a 32 bit register. An interrupt bit is cleared when the respective MMC counter that caused the interrupt is read. The least significant byte lane (Bits[7:0]) of the respective counter must be read to clear the interrupt bit. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3788-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_4<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>PAOCI PSECI PAECI<br>R Reserved_31_4  FCIS<br>S  S  S<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-4|Reserved.|
|Reserved_31_4||
|3<br>FCIS|MMC Rx FPE Fragment Counter Interrupt Status This bit is set when the Rx_FPE_Fragment_Cntr<br>counter reaches half of the maximum value or the maximum value. Access restriction applies. Clears<br>on read. Self-set to 1 on internal event. Exists when any one of the RX/TX MMC counters are enabled<br>during FPE Enabled configuration.<br>0b - MMC Rx FPE Fragment Counter Interrupt Status not detected<br>1b - MMC Rx FPE Fragment Counter Interrupt Status detected|
|2<br>PAOCIS|MMC Rx Packet Assembly OK Counter Interrupt Status This bit is set when the<br>Rx_Packet_Assemble_Ok_Cntr counter reaches half of the maximum value or the maximum value.<br>Access restriction applies. Clears on read. Self-set to 1 on internal event. Exists when any one of the<br>RX/TX MMC counters are enabled during FPE Enabled configuration.<br>0b - MMC Rx Packet Assembly OK Counter Interrupt Status not detected<br>1b - MMC Rx Packet Assembly OK Counter Interrupt Status detected|
|1<br>PSECIS|MMC Rx Packet SMD Error Counter Interrupt Status This bit is set when the Rx_Packet_SMD_Err_Cntr<br>counter reaches half of the maximum value or the maximum value. Access restriction applies. Clears<br>on read. Self-set to 1 on internal event. Exists when any one of the RX/TX MMC counters are enabled<br>during FPE Enabled configuration.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3788 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - MMC Rx Packet SMD Error Counter Interrupt Status not detected|
||1b - MMC Rx Packet SMD Error Counter Interrupt Status detected|
|0<br>PAECIS|MMC Rx Packet Assembly Error Counter Interrupt Status This bit is set when the<br>Rx_Packet_Assemble_Err_Cntr counter reaches half of the maximum value or the maximum value.<br>Access restriction applies. Clears on read. Self-set to 1 on internal event. Exists when any one of the<br>RX/TX MMC counters are enabled during FPE Enabled configuration.|
||0b - MMC Rx Packet Assembly Error Counter Interrupt Status not detected|
||1b - MMC Rx Packet Assembly Error Counter Interrupt Status detected|



# 75.7.158 (MMC_FPE_Rx_Interrupt_Mask) 

## Offset 

|Register|Offset|
|---|---|
|MMC_FPE_Rx_Interrupt|8C4h|
|_Mask||



## Function 

This register maintains the masks for interrupts generated from all FPE related Receive statistics counters. The MMC Receive Interrupt Mask register maintains the masks for the interrupts generated when FPE related receive statistic counters reach half of their maximum value or the maximum values. This register is 32 bit wide. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||Reserve|d_31_4||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||Reserve|d_31_4||||||FCIM|PAOCI<br>M|PSECI<br>M|PAECI<br>M|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field<br>Function|
|---|
|31-4<br>Reserved.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3789 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|Reserved_31_4||
|3<br>FCIM|MMC Rx FPE Fragment Counter Interrupt Mask Setting this bit masks the interrupt when the<br>Tx_FPE_Fragment_Cntr counter reaches half of the maximum value or the maximum value. Exists when<br>any one of the RX/TX MMC counters are enabled during FPE Enabled configuration.<br>0b - MMC Rx FPE Fragment Counter Interrupt Mask is disabled<br>1b - MMC Rx FPE Fragment Counter Interrupt Mask is enabled|
|2<br>PAOCIM|MMC Rx Packet Assembly OK Counter Interrupt Mask Setting this bit masks the interrupt when the<br>Rx_Packet_Assemble_Ok_Cntr counter reaches half of the maximum value or the maximum value.<br>Exists when any one of the RX/TX MMC counters are enabled during FPE Enabled configuration.<br>0b - MMC Rx Packet Assembly OK Counter Interrupt Mask is disabled<br>1b - MMC Rx Packet Assembly OK Counter Interrupt Mask is enabled|
|1<br>PSECIM|MMC Rx Packet SMD Error Counter Interrupt Mask Setting this bit masks the interrupt when the R<br>Rx_Packet_SMD_Err_Cntr counter reaches half of the maximum value or the maximum value. Exists<br>when any one of the RX/TX MMC counters are enabled during FPE Enabled configuration.<br>0b - MMC Rx Packet SMD Error Counter Interrupt Mask is disabled<br>1b - MMC Rx Packet SMD Error Counter Interrupt Mask is enabled|
|0<br>PAECIM|MMC Rx Packet Assembly Error Counter Interrupt Mask Setting this bit masks the interrupt when the<br>R Rx_Packet_Assemble_Err_Cntr counter reaches half of the maximum value or the maximum value.<br>Exists when any one of the RX/TX MMC counters are enabled during FPE Enabled configuration.<br>0b - MMC Rx Packet Assembly Error Counter Interrupt Mask is disabled<br>1b - MMC Rx Packet Assembly Error Counter Interrupt Mask is enabled|



# 75.7.159 (MMC_Rx_Packet_Assembly_Err_Cntr) 

## Offset 

|Register|Offset|
|---|---|
|MMC_Rx_Packet_Assem|8C8h|
|bly_Err_Cntr||



## Function 

This register provides the number of MAC frames with reassembly errors on the Receiver, due to mismatch in the Fragment Count value. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3790 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3791-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R PAEC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R PAEC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Rx Packet Assembly Error Counter This field indicates the number of MAC frames with reassembly|
|PAEC|errors on the Receiver, due to mismatch in the Fragment Count value. Exists when any one of the RX/TX<br>MMC counters are enabled during FPE Enabled configuration.|



# 75.7.160 (MMC_Rx_Packet_SMD_Err_Cntr) 

## Offset 

|Register|Offset|
|---|---|
|MMC_Rx_Packet_SMD_|8CCh|
|Err_Cntr||



## Function 

This register provides the number of received MAC frames rejected due to unknown SMD value and MAC frame fragments rejected due to arriving with an SMD-C when there was no preceding preempted frame. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||PS|EC||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||PS|EC||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3791 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0|Rx Packet SMD Error Counter This field indicates the number of MAC frames rejected due to unknown|
|PSEC|SMD value and MAC frame fragments rejected due to arriving with an SMD-C when there was no<br>preceding preempted frame. Exists when at least one of the RX/TX MMC counters are enabled during<br>FPE Enabled configuration.|



# 75.7.161 (MMC_Rx_Packet_Assembly_OK_Cntr) 

## Offset 

|Register|Offset|
|---|---|
|MMC_Rx_Packet_Assem|8D0h|
|bly_OK_Cntr||



## Function 

This register provides the number of MAC frames that were successfully reassembled and delivered to MAC. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||PA|OC||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||PA|OC||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Rx Packet Assembly OK Counter This field indicates the number of MAC frames that were successfully|
|PAOC|reassembled and delivered to MAC. Exists when at least one of the RX/TX MMC counters are enabled<br>during FPE Enabled configuration.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3792 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.162 (MMC_Rx_FPE_Fragment_Cntr) 

## Offset 

|Register|Offset|
|---|---|
|MMC_Rx_FPE_Fragmen|8D4h|
|t_Cntr||



## Function 

This register provides the number of additional mPackets received due to preemption. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3793-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R FFC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R FFC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Rx FPE Fragment Counter This field indicates the number of additional mPackets received due to|
|FFC|preemption Exists when at least one of the RX/TX MMC counters are enabled during FPE Enabled<br>configuration.|



# 75.7.163 (MAC_L3_L4_Control0) 

## Offset 

|Register|Offset|
|---|---|
|MAC_L3_L4_Control0|900h|



## Function 

The Layer 3 and Layer 4 Control register controls the operations of filter 0 of Layer 3 and Layer 4. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3793 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3794-02.png)


<!-- Start of picture text -->
Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserved_23_2 Reserv<br>R Reserved_31_29  DMCH Reserved_27_y  DMCHN0  2  L4DPI L4DP L4SPI L4SP e... L4PEN<br>EN0  M0  M0  M0  M0  0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv<br>R L3HDBM0  L3HSBM0  L3DAI L3DA L3SAI L3SA e... L3PEN<br>M0  M0  M0  M0  0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-29|Reserved.|
|Reserved_31_2<br>9||
|28<br>DMCHEN0|DMA Channel Select Enable When set, this bit enables the selection of the DMA channel number for the<br>packet that is passed by this L3_L4 filter. The DMA channel is indicated by the DMCHN bits. When this<br>bit is reset, the DMA channel is not decided by this filter.<br>0b - DMA Channel Select is disabled<br>1b - DMA Channel Select is enabled|
|27-26|Reserved.|
|Reserved_27_y||
|25-24<br>DMCHN0|DMA Channel Number When DMCHEN is set high, this field selects the DMA Channel number to which<br>the packet passed by this filter is routed. The width of this field depends on the number of the DMA<br>channels present in your configuration.|
|23-22|Reserved.|
|Reserved_23_2<br>2||
|21<br>L4DPIM0|Layer 4 Destination Port Inverse Match Enable When this bit is set, the Layer 4 Destination Port number<br>field is enabled for inverse matching. When this bit is reset, the Layer 4 Destination Port number field is<br>enabled for perfect matching. This bit is valid and applicable only when the L4DPM0 bit is set high.<br>0b - Layer 4 Destination Port Inverse Match is disabled<br>1b - Layer 4 Destination Port Inverse Match is enabled|
|20<br>L4DPM0|Layer 4 Destination Port Match Enable When this bit is set, the Layer 4 Destination Port number field is<br>enabled for matching. When this bit is reset, the MAC ignores the Layer 4 Destination Port number field<br>for matching.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3794 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function<br>0b - Layer 4 Destination Port Match is disabled<br>1b - Layer 4 Destination Port Match is enabled|
|---|---|
|19<br>L4SPIM0|Layer 4 Source Port Inverse Match Enable When this bit is set, the Layer 4 Source Port number field is<br>enabled for inverse matching. When this bit is reset, the Layer 4 Source Port number field is enabled for<br>perfect matching. This bit is valid and applicable only when the L4SPM0 bit is set high.<br>0b - Layer 4 Source Port Inverse Match is disabled<br>1b - Layer 4 Source Port Inverse Match is enabled|
|18<br>L4SPM0|Layer 4 Source Port Match Enable When this bit is set, the Layer 4 Source Port number field is enabled<br>for matching. When this bit is reset, the MAC ignores the Layer 4 Source Port number field for matching.<br>0b - Layer 4 Source Port Match is disabled<br>1b - Layer 4 Source Port Match is enabled|
|17<br>Reserved_17|Reserved.|
|16<br>L4PEN0|Layer 4 Protocol Enable When this bit is set, the Source and Destination Port number fields of UDP<br>packets are used for matching. When this bit is reset, the Source and Destination Port number fields of<br>TCP packets are used for matching. The Layer 4 matching is done only when the L4SPM0 or L4DPM0<br>bit is set.<br>0b - Layer 4 Protocol is disabled<br>1b - Layer 4 Protocol is enabled|
|15-11<br>L3HDBM0|Layer 3 IP DA Higher Bits Match IPv4 Packets: This field contains the number of higher bits of IP<br>Destination Address that are matched in the IPv4 packets. The following list describes the values of<br>this field: - 0: No bits are masked. - 1: LSb[0] is masked - 2: Two LSbs [1:0] are masked - .. - 31: All<br>bits except MSb are masked. IPv6 Packets: Bits[12:11] of this field correspond to Bits[6:5] of L3HSBM0<br>which indicate the number of lower bits of IP Source or Destination Address that are masked in the IPv6<br>packets. The following list describes the concatenated values of the L3HDBM0[1:0] and L3HSBM0 bits:<br>- 0: No bits are masked. - 1: LSb[0] is masked. - 2: Two LSbs [1:0] are masked - .. - 127: All bits except<br>MSb are masked. This field is valid and applicable only when the L3DAM0 or L3SAM0 bit is set.|
|10-6<br>L3HSBM0|Layer 3 IP SA Higher Bits Match IPv4 Packets: This field contains the number of lower bits of IP Source<br>Address that are masked for matching in the IPv4 packets. The following list describes the values of this<br>field: - 0: No bits are masked. - 1: LSb[0] is masked - 2: Two LSbs [1:0] are masked - .. - 31: All bits<br>except MSb are masked. IPv6 Packets: This field contains Bits[4:0] of L3HSBM0. These bits indicate the<br>number of higher bits of IP Source or Destination Address matched in the IPv6 packets. This field is valid<br>and applicable only when the L3DAM0 or L3SAM0 bit is set high.|
|5<br>L3DAIM0|Layer 3 IP DA Inverse Match Enable When this bit is set, the Layer 3 IP Destination Address field is<br>enabled for inverse matching. When this bit is reset, the Layer 3 IP Destination Address field is enabled<br>for perfect matching. This bit is valid and applicable only when the L3DAM0 bit is set high.<br>0b - Layer 3 IP DA Inverse Match is disabled<br>1b - Layer 3 IP DA Inverse Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3795 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|4<br>L3DAM0|Layer 3 IP DA Match Enable When this bit is set, the Layer 3 IP Destination Address field is enabled for<br>matching. When this bit is reset, the MAC ignores the Layer 3 IP Destination Address field for matching.<br>Note: When the L3PEN0 bit is set, you should set either this bit or the L3SAM0 bit because either IPv6<br>DA or SA can be checked for filtering.<br>0b - Layer 3 IP DA Match is disabled<br>1b - Layer 3 IP DA Match is enabled|
|3<br>L3SAIM0|Layer 3 IP SA Inverse Match Enable When this bit is set, the Layer 3 IP Source Address field is enabled<br>for inverse matching. When this bit reset, the Layer 3 IP Source Address field is enabled for perfect<br>matching. This bit is valid and applicable only when the L3SAM0 bit is set.<br>0b - Layer 3 IP SA Inverse Match is disabled<br>1b - Layer 3 IP SA Inverse Match is enabled|
|2<br>L3SAM0|Layer 3 IP SA Match Enable When this bit is set, the Layer 3 IP Source Address field is enabled for<br>matching. When this bit is reset, the MAC ignores the Layer 3 IP Source Address field for matching.<br>Note: When the L3PEN0 bit is set, you should set either this bit or the L3DAM0 bit because either IPv6<br>SA or DA can be checked for filtering.<br>0b - Layer 3 IP SA Match is disabled<br>1b - Layer 3 IP SA Match is enabled|
|1<br>Reserved_1|Reserved.|
|0<br>L3PEN0|Layer 3 Protocol Enable When this bit is set, the Layer 3 IP Source or Destination Address matching is<br>enabled for IPv6 packets. When this bit is reset, the Layer 3 IP Source or Destination Address matching<br>is enabled for IPv4 packets. The Layer 3 matching is done only when the L3SAM0 or L3DAM0 bit is set.<br>0b - Layer 3 Protocol is disabled<br>1b - Layer 3 Protocol is enabled|



# 75.7.164 (MAC_Layer4_Address0) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer4_Address0|904h|



## Function 

The MAC_Layer4_Address(#i), MAC_L3_L4_Control(#i), MAC_Layer3_Addr0_Reg(#i), MAC_Layer3_Addr1_Reg(#i), MAC_Layer3_Addr2_Reg(#i) and MAC_Layer3_Addr3_Reg(#i) registers are reserved (RO with default value) if Enable Layer 3 and Layer 4 Packet Filter option is not selected while configuring the IP. You can configure the Layer 3 and Layer 4 Address Registers to be double-synchronized by selecting the Synchronize Layer 3 and Layer 4 Address Registers to Rx Clock Domain option while configuring the IP. When you select this option, the synchronization is triggered only when Bits[31:24] (in little-endian mode) or Bits[7:0] (in big-endian mode) of the Layer 3 and Layer 4 Address Registers are written. For proper 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3796 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

synchronization updates, you should perform consecutive writes to same Layer 3 and Layer 4 Address Registers after at least four clock cycles delay of the destination clock. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3797-04.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>L4DP0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>L4SP0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-16<br>L4DP0|Layer 4 Destination Port Number Field When the L4PEN0 bit is reset and the L4DPM0 bit is set in the<br>MAC_L3_L4_Control0 register, this field contains the value to be matched with the TCP Destination<br>Port Number field in the IPv4 or IPv6 packets. When the L4PEN0 and L4DPM0 bits are set in<br>MAC_L3_L4_Control0 register, this field contains the value to be matched with the UDP Destination<br>Port Number field in the IPv4 or IPv6 packets.|
|15-0<br>L4SP0|Layer 4 Source Port Number Field When the L4PEN0 bit is reset and the L4SPM0 bit is set in<br>the MAC_L3_L4_Control0 register, this field contains the value to be matched with the TCP Source<br>Port Number field in the IPv4 or IPv6 packets. When the L4PEN0 and L4SPM0 bits are set in<br>MAC_L3_L4_Control0 register, this field contains the value to be matched with the UDP Source Port<br>Number field in the IPv4 or IPv6 packets.|



# 75.7.165 (MAC_Layer3_Addr0_Reg0) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr0_Re<br>g0|910h|



## Function 

For IPv4 packets, the Layer 3 Address 0 Register 0 register contains the 32-bit IP Source Address field. For IPv6 packets, it contains Bits[31:0] of the 128-bit IP Source Address or Destination Address field. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3797 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3798-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>L3A00<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>L3A00<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0<br>L3A00|Layer 3 Address 0 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0<br>register, this field contains the value to be matched with Bits[31:0] of the IP Source Address field in the<br>IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with Bits[31:0] of the IP Destination Address field in the IPv6 packets.|
||When the L3PEN0 bit is reset and the L3SAM0 bit is set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with the IP Source Address field in the IPv4 packets.|



# 75.7.166 (MAC_Layer3_Addr1_Reg0) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr1_Re<br>g0|914h|



## Function 

For IPv4 packets, the Layer 3 Address 1 Register 0 register contains the 32-bit IP Destination Address field. For IPv6 packets, it contains Bits[63:32] of the 128-bit IP Source Address or Destination Address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3|A10||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3|A10||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3798 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0<br>L3A10|Layer 3 Address 1 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0<br>register, this field contains the value to be matched with Bits[63:32] of the IP Source Address field in the<br>IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with Bits[63:32] of the IP Destination Address field in the IPv6 packets.|
||When the L3PEN0 bit is reset and the L3SAM0 bit is set in the MAC_L3_L4_Control0 register, this field<br>contains the value to be matched with the IP Destination Address field in the IPv4 packets.|



# 75.7.167 (MAC_Layer3_Addr2_Reg0) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr2_Re<br>g0|918h|



## Function 

The Layer 3 Address 2 Register 0 register is reserved for IPv4 packets. For IPv6 packets, it contains Bits[95:64] of 128-bit IP Source Address or Destination Address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3|A20||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3|A20||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 2 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0|
|L3A20|register, this field contains the value to be matched with Bits[95:64] of the IP Source Address field in the<br>IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with Bits[95:64] of the IP Destination Address field in the IPv6 packets.|
||When the L3PEN0 bit is reset in the MAC_L3_L4_Control0 register, this field is not used.|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3799 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.168 (MAC_Layer3_Addr3_Reg0) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr3_Re<br>g0|91Ch|



## Function 

The Layer 3 Address 3 Register 0 register is reserved for IPv4 packets. For IPv6 packets, it contains Bits[127:96] of 128-bit IP Source Address or Destination Address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3|A30||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3|A30||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 3 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0|
|L3A30|register, this field contains the value to be matched with Bits[127:96] of the IP Source Address field in|
||the IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this|
||field contains the value to be matched with Bits[127:96] of the IP Destination Address field in the IPv6|
||packets. When the L3PEN0 bit is reset in the MAC_L3_L4_Control0 register, this field is not used.|



# 75.7.169 (MAC_L3_L4_Control1) 

## Offset 

|Register|Offset|
|---|---|
|MAC_L3_L4_Control1|930h|



## Function 

The Layer 3 and Layer 4 Control register controls the operations of filter 0 of Layer 3 and Layer 4. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3800 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3801-02.png)


<!-- Start of picture text -->
Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserved_23_2 Reserv<br>R Reserved_31_29  DMCH Reserved_27_y  DMCHN1  2  L4DPI L4DP L4SPI L4SP e... L4PEN<br>EN1  M1  M1  M1  M1  1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv<br>R L3HDBM1  L3HSBM1  L3DAI L3DA L3SAI L3SA e... L3PEN<br>M1  M1  M1  M1  1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-29|Reserved.|
|Reserved_31_2<br>9||
|28<br>DMCHEN1|DMA Channel Select Enable When set, this bit enables the selection of the DMA channel number for the<br>packet that is passed by this L3_L4 filter. The DMA channel is indicated by the DMCHN bits. When this<br>bit is reset, the DMA channel is not decided by this filter.<br>0b - DMA Channel Select is disabled<br>1b - DMA Channel Select is enabled|
|27-26|Reserved.|
|Reserved_27_y||
|25-24<br>DMCHN1|DMA Channel Number When DMCHEN is set high, this field selects the DMA Channel number to which<br>the packet passed by this filter is routed. The width of this field depends on the number of the DMA<br>channels present in your configuration.|
|23-22|Reserved.|
|Reserved_23_2<br>2||
|21<br>L4DPIM1|Layer 4 Destination Port Inverse Match Enable When this bit is set, the Layer 4 Destination Port number<br>field is enabled for inverse matching. When this bit is reset, the Layer 4 Destination Port number field is<br>enabled for perfect matching. This bit is valid and applicable only when the L4DPM0 bit is set high.<br>0b - Layer 4 Destination Port Inverse Match is disabled<br>1b - Layer 4 Destination Port Inverse Match is enabled|
|20<br>L4DPM1|Layer 4 Destination Port Match Enable When this bit is set, the Layer 4 Destination Port number field is<br>enabled for matching. When this bit is reset, the MAC ignores the Layer 4 Destination Port number field<br>for matching.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3801 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function<br>0b - Layer 4 Destination Port Match is disabled<br>1b - Layer 4 Destination Port Match is enabled|
|---|---|
|19<br>L4SPIM1|Layer 4 Source Port Inverse Match Enable When this bit is set, the Layer 4 Source Port number field is<br>enabled for inverse matching. When this bit is reset, the Layer 4 Source Port number field is enabled for<br>perfect matching. This bit is valid and applicable only when the L4SPM0 bit is set high.<br>0b - Layer 4 Source Port Inverse Match is disabled<br>1b - Layer 4 Source Port Inverse Match is enabled|
|18<br>L4SPM1|Layer 4 Source Port Match Enable When this bit is set, the Layer 4 Source Port number field is enabled<br>for matching. When this bit is reset, the MAC ignores the Layer 4 Source Port number field for matching.<br>0b - Layer 4 Source Port Match is disabled<br>1b - Layer 4 Source Port Match is enabled|
|17<br>Reserved_17|Reserved.|
|16<br>L4PEN1|Layer 4 Protocol Enable When this bit is set, the Source and Destination Port number fields of UDP<br>packets are used for matching. When this bit is reset, the Source and Destination Port number fields of<br>TCP packets are used for matching. The Layer 4 matching is done only when the L4SPM0 or L4DPM0<br>bit is set.<br>0b - Layer 4 Protocol is disabled<br>1b - Layer 4 Protocol is enabled|
|15-11<br>L3HDBM1|Layer 3 IP DA Higher Bits Match IPv4 Packets: This field contains the number of higher bits of IP<br>Destination Address that are matched in the IPv4 packets. The following list describes the values of<br>this field: - 0: No bits are masked. - 1: LSb[0] is masked - 2: Two LSbs [1:0] are masked - .. - 31: All<br>bits except MSb are masked. IPv6 Packets: Bits[12:11] of this field correspond to Bits[6:5] of L3HSBM0<br>which indicate the number of lower bits of IP Source or Destination Address that are masked in the IPv6<br>packets. The following list describes the concatenated values of the L3HDBM0[1:0] and L3HSBM0 bits:<br>- 0: No bits are masked. - 1: LSb[0] is masked. - 2: Two LSbs [1:0] are masked - .. - 127: All bits except<br>MSb are masked. This field is valid and applicable only when the L3DAM0 or L3SAM0 bit is set.|
|10-6<br>L3HSBM1|Layer 3 IP SA Higher Bits Match IPv4 Packets: This field contains the number of lower bits of IP Source<br>Address that are masked for matching in the IPv4 packets. The following list describes the values of this<br>field: - 0: No bits are masked. - 1: LSb[0] is masked - 2: Two LSbs [1:0] are masked - .. - 31: All bits<br>except MSb are masked. IPv6 Packets: This field contains Bits[4:0] of L3HSBM0. These bits indicate the<br>number of higher bits of IP Source or Destination Address matched in the IPv6 packets. This field is valid<br>and applicable only when the L3DAM0 or L3SAM0 bit is set high.|
|5<br>L3DAIM1|Layer 3 IP DA Inverse Match Enable When this bit is set, the Layer 3 IP Destination Address field is<br>enabled for inverse matching. When this bit is reset, the Layer 3 IP Destination Address field is enabled<br>for perfect matching. This bit is valid and applicable only when the L3DAM0 bit is set high.<br>0b - Layer 3 IP DA Inverse Match is disabled<br>1b - Layer 3 IP DA Inverse Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3802 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|4<br>L3DAM1|Layer 3 IP DA Match Enable When this bit is set, the Layer 3 IP Destination Address field is enabled for<br>matching. When this bit is reset, the MAC ignores the Layer 3 IP Destination Address field for matching.<br>Note: When the L3PEN0 bit is set, you should set either this bit or the L3SAM0 bit because either IPv6<br>DA or SA can be checked for filtering.<br>0b - Layer 3 IP DA Match is disabled<br>1b - Layer 3 IP DA Match is enabled|
|3<br>L3SAIM1|Layer 3 IP SA Inverse Match Enable When this bit is set, the Layer 3 IP Source Address field is enabled<br>for inverse matching. When this bit reset, the Layer 3 IP Source Address field is enabled for perfect<br>matching. This bit is valid and applicable only when the L3SAM0 bit is set.<br>0b - Layer 3 IP SA Inverse Match is disabled<br>1b - Layer 3 IP SA Inverse Match is enabled|
|2<br>L3SAM1|Layer 3 IP SA Match Enable When this bit is set, the Layer 3 IP Source Address field is enabled for<br>matching. When this bit is reset, the MAC ignores the Layer 3 IP Source Address field for matching.<br>Note: When the L3PEN0 bit is set, you should set either this bit or the L3DAM0 bit because either IPv6<br>SA or DA can be checked for filtering.<br>0b - Layer 3 IP SA Match is disabled<br>1b - Layer 3 IP SA Match is enabled|
|1<br>Reserved_1|Reserved.|
|0<br>L3PEN1|Layer 3 Protocol Enable When this bit is set, the Layer 3 IP Source or Destination Address matching is<br>enabled for IPv6 packets. When this bit is reset, the Layer 3 IP Source or Destination Address matching<br>is enabled for IPv4 packets. The Layer 3 matching is done only when the L3SAM0 or L3DAM0 bit is set.<br>0b - Layer 3 Protocol is disabled<br>1b - Layer 3 Protocol is enabled|



# 75.7.170 (MAC_Layer4_Address1) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer4_Address1|934h|



## Function 

The MAC_Layer4_Address(#i), MAC_L3_L4_Control(#i), MAC_Layer3_Addr0_Reg(#i), MAC_Layer3_Addr1_Reg(#i), MAC_Layer3_Addr2_Reg(#i) and MAC_Layer3_Addr3_Reg(#i) registers are reserved (RO with default value) if Enable Layer 3 and Layer 4 Packet Filter option is not selected while configuring the IP. You can configure the Layer 3 and Layer 4 Address Registers to be double-synchronized by selecting the Synchronize Layer 3 and Layer 4 Address Registers to Rx Clock Domain option while configuring the IP. When you select this option, the synchronization is triggered only when Bits[31:24] (in little-endian mode) or Bits[7:0] (in big-endian mode) of the Layer 3 and Layer 4 Address Registers are written. For proper 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3803 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

synchronization updates, you should perform consecutive writes to same Layer 3 and Layer 4 Address Registers after at least four clock cycles delay of the destination clock. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3804-04.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>L4DP1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>L4SP1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-16<br>L4DP1|Layer 4 Destination Port Number Field When the L4PEN0 bit is reset and the L4DPM0 bit is set in the<br>MAC_L3_L4_Control0 register, this field contains the value to be matched with the TCP Destination<br>Port Number field in the IPv4 or IPv6 packets. When the L4PEN0 and L4DPM0 bits are set in<br>MAC_L3_L4_Control0 register, this field contains the value to be matched with the UDP Destination<br>Port Number field in the IPv4 or IPv6 packets.|
|15-0<br>L4SP1|Layer 4 Source Port Number Field When the L4PEN0 bit is reset and the L4SPM0 bit is set in<br>the MAC_L3_L4_Control0 register, this field contains the value to be matched with the TCP Source<br>Port Number field in the IPv4 or IPv6 packets. When the L4PEN0 and L4SPM0 bits are set in<br>MAC_L3_L4_Control0 register, this field contains the value to be matched with the UDP Source Port<br>Number field in the IPv4 or IPv6 packets.|



# 75.7.171 (MAC_Layer3_Addr0_Reg1) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr0_Re<br>g1|940h|



## Function 

For IPv4 packets, the Layer 3 Address 0 Register 0 register contains the 32-bit IP Source Address field. For IPv6 packets, it contains Bits[31:0] of the 128-bit IP Source Address or Destination Address field. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3804 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3805-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>L3A01<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>L3A01<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0<br>L3A01|Layer 3 Address 0 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0<br>register, this field contains the value to be matched with Bits[31:0] of the IP Source Address field in the<br>IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with Bits[31:0] of the IP Destination Address field in the IPv6 packets.|
||When the L3PEN0 bit is reset and the L3SAM0 bit is set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with the IP Source Address field in the IPv4 packets.|



# 75.7.172 (MAC_Layer3_Addr1_Reg1) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr1_Re<br>g1|944h|



## Function 

For IPv4 packets, the Layer 3 Address 1 Register 0 register contains the 32-bit IP Destination Address field. For IPv6 packets, it contains Bits[63:32] of the 128-bit IP Source Address or Destination Address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3|A11||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3|A11||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3805 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0<br>L3A11|Layer 3 Address 1 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0<br>register, this field contains the value to be matched with Bits[63:32] of the IP Source Address field in the<br>IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with Bits[63:32] of the IP Destination Address field in the IPv6 packets.|
||When the L3PEN0 bit is reset and the L3SAM0 bit is set in the MAC_L3_L4_Control0 register, this field<br>contains the value to be matched with the IP Destination Address field in the IPv4 packets.|



# 75.7.173 (MAC_Layer3_Addr2_Reg1) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr2_Re<br>g1|948h|



## Function 

The Layer 3 Address 2 Register 0 register is reserved for IPv4 packets. For IPv6 packets, it contains Bits[95:64] of 128-bit IP Source Address or Destination Address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3|A21||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3|A21||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 2 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0|
|L3A21|register, this field contains the value to be matched with Bits[95:64] of the IP Source Address field in the<br>IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with Bits[95:64] of the IP Destination Address field in the IPv6 packets.|
||When the L3PEN0 bit is reset in the MAC_L3_L4_Control0 register, this field is not used.|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3806 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.174 (MAC_Layer3_Addr3_Reg1) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr3_Re<br>g1|94Ch|



## Function 

The Layer 3 Address 3 Register 0 register is reserved for IPv4 packets. For IPv6 packets, it contains Bits[127:96] of 128-bit IP Source Address or Destination Address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3|A31||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3|A31||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 3 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0|
|L3A31|register, this field contains the value to be matched with Bits[127:96] of the IP Source Address field in|
||the IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this|
||field contains the value to be matched with Bits[127:96] of the IP Destination Address field in the IPv6|
||packets. When the L3PEN0 bit is reset in the MAC_L3_L4_Control0 register, this field is not used.|



# 75.7.175 (MAC_L3_L4_Control2) 

## Offset 

|Register|Offset|
|---|---|
|MAC_L3_L4_Control2|960h|



## Function 

The Layer 3 and Layer 4 Control register controls the operations of filter 0 of Layer 3 and Layer 4. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3807 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3808-02.png)


<!-- Start of picture text -->
Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserved_23_2 Reserv<br>R Reserved_31_29  DMCH Reserved_27_y  DMCHN2  2  L4DPI L4DP L4SPI L4SP e... L4PEN<br>EN2  M2  M2  M2  M2  2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv<br>R L3HDBM2  L3HSBM2  L3DAI L3DA L3SAI L3SA e... L3PEN<br>M2  M2  M2  M2  2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-29|Reserved.|
|Reserved_31_2<br>9||
|28<br>DMCHEN2|DMA Channel Select Enable When set, this bit enables the selection of the DMA channel number for the<br>packet that is passed by this L3_L4 filter. The DMA channel is indicated by the DMCHN bits. When this<br>bit is reset, the DMA channel is not decided by this filter.<br>0b - DMA Channel Select is disabled<br>1b - DMA Channel Select is enabled|
|27-26|Reserved.|
|Reserved_27_y||
|25-24<br>DMCHN2|DMA Channel Number When DMCHEN is set high, this field selects the DMA Channel number to which<br>the packet passed by this filter is routed. The width of this field depends on the number of the DMA<br>channels present in your configuration.|
|23-22|Reserved.|
|Reserved_23_2<br>2||
|21<br>L4DPIM2|Layer 4 Destination Port Inverse Match Enable When this bit is set, the Layer 4 Destination Port number<br>field is enabled for inverse matching. When this bit is reset, the Layer 4 Destination Port number field is<br>enabled for perfect matching. This bit is valid and applicable only when the L4DPM0 bit is set high.<br>0b - Layer 4 Destination Port Inverse Match is disabled<br>1b - Layer 4 Destination Port Inverse Match is enabled|
|20<br>L4DPM2|Layer 4 Destination Port Match Enable When this bit is set, the Layer 4 Destination Port number field is<br>enabled for matching. When this bit is reset, the MAC ignores the Layer 4 Destination Port number field<br>for matching.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3808 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function<br>0b - Layer 4 Destination Port Match is disabled<br>1b - Layer 4 Destination Port Match is enabled|
|---|---|
|19<br>L4SPIM2|Layer 4 Source Port Inverse Match Enable When this bit is set, the Layer 4 Source Port number field is<br>enabled for inverse matching. When this bit is reset, the Layer 4 Source Port number field is enabled for<br>perfect matching. This bit is valid and applicable only when the L4SPM0 bit is set high.<br>0b - Layer 4 Source Port Inverse Match is disabled<br>1b - Layer 4 Source Port Inverse Match is enabled|
|18<br>L4SPM2|Layer 4 Source Port Match Enable When this bit is set, the Layer 4 Source Port number field is enabled<br>for matching. When this bit is reset, the MAC ignores the Layer 4 Source Port number field for matching.<br>0b - Layer 4 Source Port Match is disabled<br>1b - Layer 4 Source Port Match is enabled|
|17<br>Reserved_17|Reserved.|
|16<br>L4PEN2|Layer 4 Protocol Enable When this bit is set, the Source and Destination Port number fields of UDP<br>packets are used for matching. When this bit is reset, the Source and Destination Port number fields of<br>TCP packets are used for matching. The Layer 4 matching is done only when the L4SPM0 or L4DPM0<br>bit is set.<br>0b - Layer 4 Protocol is disabled<br>1b - Layer 4 Protocol is enabled|
|15-11<br>L3HDBM2|Layer 3 IP DA Higher Bits Match IPv4 Packets: This field contains the number of higher bits of IP<br>Destination Address that are matched in the IPv4 packets. The following list describes the values of<br>this field: - 0: No bits are masked. - 1: LSb[0] is masked - 2: Two LSbs [1:0] are masked - .. - 31: All<br>bits except MSb are masked. IPv6 Packets: Bits[12:11] of this field correspond to Bits[6:5] of L3HSBM0<br>which indicate the number of lower bits of IP Source or Destination Address that are masked in the IPv6<br>packets. The following list describes the concatenated values of the L3HDBM0[1:0] and L3HSBM0 bits:<br>- 0: No bits are masked. - 1: LSb[0] is masked. - 2: Two LSbs [1:0] are masked - .. - 127: All bits except<br>MSb are masked. This field is valid and applicable only when the L3DAM0 or L3SAM0 bit is set.|
|10-6<br>L3HSBM2|Layer 3 IP SA Higher Bits Match IPv4 Packets: This field contains the number of lower bits of IP Source<br>Address that are masked for matching in the IPv4 packets. The following list describes the values of this<br>field: - 0: No bits are masked. - 1: LSb[0] is masked - 2: Two LSbs [1:0] are masked - .. - 31: All bits<br>except MSb are masked. IPv6 Packets: This field contains Bits[4:0] of L3HSBM0. These bits indicate the<br>number of higher bits of IP Source or Destination Address matched in the IPv6 packets. This field is valid<br>and applicable only when the L3DAM0 or L3SAM0 bit is set high.|
|5<br>L3DAIM2|Layer 3 IP DA Inverse Match Enable When this bit is set, the Layer 3 IP Destination Address field is<br>enabled for inverse matching. When this bit is reset, the Layer 3 IP Destination Address field is enabled<br>for perfect matching. This bit is valid and applicable only when the L3DAM0 bit is set high.<br>0b - Layer 3 IP DA Inverse Match is disabled<br>1b - Layer 3 IP DA Inverse Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3809 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|4<br>L3DAM2|Layer 3 IP DA Match Enable When this bit is set, the Layer 3 IP Destination Address field is enabled for<br>matching. When this bit is reset, the MAC ignores the Layer 3 IP Destination Address field for matching.<br>Note: When the L3PEN0 bit is set, you should set either this bit or the L3SAM0 bit because either IPv6<br>DA or SA can be checked for filtering.<br>0b - Layer 3 IP DA Match is disabled<br>1b - Layer 3 IP DA Match is enabled|
|3<br>L3SAIM2|Layer 3 IP SA Inverse Match Enable When this bit is set, the Layer 3 IP Source Address field is enabled<br>for inverse matching. When this bit reset, the Layer 3 IP Source Address field is enabled for perfect<br>matching. This bit is valid and applicable only when the L3SAM0 bit is set.<br>0b - Layer 3 IP SA Inverse Match is disabled<br>1b - Layer 3 IP SA Inverse Match is enabled|
|2<br>L3SAM2|Layer 3 IP SA Match Enable When this bit is set, the Layer 3 IP Source Address field is enabled for<br>matching. When this bit is reset, the MAC ignores the Layer 3 IP Source Address field for matching.<br>Note: When the L3PEN0 bit is set, you should set either this bit or the L3DAM0 bit because either IPv6<br>SA or DA can be checked for filtering.<br>0b - Layer 3 IP SA Match is disabled<br>1b - Layer 3 IP SA Match is enabled|
|1<br>Reserved_1|Reserved.|
|0<br>L3PEN2|Layer 3 Protocol Enable When this bit is set, the Layer 3 IP Source or Destination Address matching is<br>enabled for IPv6 packets. When this bit is reset, the Layer 3 IP Source or Destination Address matching<br>is enabled for IPv4 packets. The Layer 3 matching is done only when the L3SAM0 or L3DAM0 bit is set.<br>0b - Layer 3 Protocol is disabled<br>1b - Layer 3 Protocol is enabled|



# 75.7.176 (MAC_Layer4_Address2) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer4_Address2|964h|



## Function 

The MAC_Layer4_Address(#i), MAC_L3_L4_Control(#i), MAC_Layer3_Addr0_Reg(#i), MAC_Layer3_Addr1_Reg(#i), MAC_Layer3_Addr2_Reg(#i) and MAC_Layer3_Addr3_Reg(#i) registers are reserved (RO with default value) if Enable Layer 3 and Layer 4 Packet Filter option is not selected while configuring the IP. You can configure the Layer 3 and Layer 4 Address Registers to be double-synchronized by selecting the Synchronize Layer 3 and Layer 4 Address Registers to Rx Clock Domain option while configuring the IP. When you select this option, the synchronization is triggered only when Bits[31:24] (in little-endian mode) or Bits[7:0] (in big-endian mode) of the Layer 3 and Layer 4 Address Registers are written. For proper 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3810 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

synchronization updates, you should perform consecutive writes to same Layer 3 and Layer 4 Address Registers after at least four clock cycles delay of the destination clock. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3811-04.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>L4DP2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>L4SP2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-16<br>L4DP2|Layer 4 Destination Port Number Field When the L4PEN0 bit is reset and the L4DPM0 bit is set in the<br>MAC_L3_L4_Control0 register, this field contains the value to be matched with the TCP Destination<br>Port Number field in the IPv4 or IPv6 packets. When the L4PEN0 and L4DPM0 bits are set in<br>MAC_L3_L4_Control0 register, this field contains the value to be matched with the UDP Destination<br>Port Number field in the IPv4 or IPv6 packets.|
|15-0<br>L4SP2|Layer 4 Source Port Number Field When the L4PEN0 bit is reset and the L4SPM0 bit is set in<br>the MAC_L3_L4_Control0 register, this field contains the value to be matched with the TCP Source<br>Port Number field in the IPv4 or IPv6 packets. When the L4PEN0 and L4SPM0 bits are set in<br>MAC_L3_L4_Control0 register, this field contains the value to be matched with the UDP Source Port<br>Number field in the IPv4 or IPv6 packets.|



# 75.7.177 (MAC_Layer3_Addr0_Reg2) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr0_Re<br>g2|970h|



## Function 

For IPv4 packets, the Layer 3 Address 0 Register 0 register contains the 32-bit IP Source Address field. For IPv6 packets, it contains Bits[31:0] of the 128-bit IP Source Address or Destination Address field. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3811 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3812-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>L3A02<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>L3A02<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0<br>L3A02|Layer 3 Address 0 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0<br>register, this field contains the value to be matched with Bits[31:0] of the IP Source Address field in the<br>IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with Bits[31:0] of the IP Destination Address field in the IPv6 packets.|
||When the L3PEN0 bit is reset and the L3SAM0 bit is set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with the IP Source Address field in the IPv4 packets.|



# 75.7.178 (MAC_Layer3_Addr1_Reg2) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr1_Re<br>g2|974h|



## Function 

For IPv4 packets, the Layer 3 Address 1 Register 0 register contains the 32-bit IP Destination Address field. For IPv6 packets, it contains Bits[63:32] of the 128-bit IP Source Address or Destination Address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3|A12||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3|A12||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3812 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0<br>L3A12|Layer 3 Address 1 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0<br>register, this field contains the value to be matched with Bits[63:32] of the IP Source Address field in the<br>IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with Bits[63:32] of the IP Destination Address field in the IPv6 packets.|
||When the L3PEN0 bit is reset and the L3SAM0 bit is set in the MAC_L3_L4_Control0 register, this field<br>contains the value to be matched with the IP Destination Address field in the IPv4 packets.|



# 75.7.179 (MAC_Layer3_Addr2_Reg2) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr2_Re<br>g2|978h|



## Function 

The Layer 3 Address 2 Register 0 register is reserved for IPv4 packets. For IPv6 packets, it contains Bits[95:64] of 128-bit IP Source Address or Destination Address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3|A22||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3|A22||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 2 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0|
|L3A22|register, this field contains the value to be matched with Bits[95:64] of the IP Source Address field in the<br>IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with Bits[95:64] of the IP Destination Address field in the IPv6 packets.|
||When the L3PEN0 bit is reset in the MAC_L3_L4_Control0 register, this field is not used.|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3813 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.180 (MAC_Layer3_Addr3_Reg2) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr3_Re<br>g2|97Ch|



## Function 

The Layer 3 Address 3 Register 0 register is reserved for IPv4 packets. For IPv6 packets, it contains Bits[127:96] of 128-bit IP Source Address or Destination Address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3|A32||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3|A32||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 3 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0|
|L3A32|register, this field contains the value to be matched with Bits[127:96] of the IP Source Address field in|
||the IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this|
||field contains the value to be matched with Bits[127:96] of the IP Destination Address field in the IPv6|
||packets. When the L3PEN0 bit is reset in the MAC_L3_L4_Control0 register, this field is not used.|



# 75.7.181 (MAC_L3_L4_Control3) 

## Offset 

|Register|Offset|
|---|---|
|MAC_L3_L4_Control3|990h|



## Function 

The Layer 3 and Layer 4 Control register controls the operations of filter 0 of Layer 3 and Layer 4. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3814 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3815-02.png)


<!-- Start of picture text -->
Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserved_23_2 Reserv<br>R Reserved_31_29  DMCH Reserved_27_y  DMCHN3  2  L4DPI L4DP L4SPI L4SP e... L4PEN<br>EN3  M3  M3  M3  M3  3<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv<br>R L3HDBM3  L3HSBM3  L3DAI L3DA L3SAI L3SA e... L3PEN<br>M3  M3  M3  M3  3<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-29|Reserved.|
|Reserved_31_2<br>9||
|28<br>DMCHEN3|DMA Channel Select Enable When set, this bit enables the selection of the DMA channel number for the<br>packet that is passed by this L3_L4 filter. The DMA channel is indicated by the DMCHN bits. When this<br>bit is reset, the DMA channel is not decided by this filter.<br>0b - DMA Channel Select is disabled<br>1b - DMA Channel Select is enabled|
|27-26|Reserved.|
|Reserved_27_y||
|25-24<br>DMCHN3|DMA Channel Number When DMCHEN is set high, this field selects the DMA Channel number to which<br>the packet passed by this filter is routed. The width of this field depends on the number of the DMA<br>channels present in your configuration.|
|23-22|Reserved.|
|Reserved_23_2<br>2||
|21<br>L4DPIM3|Layer 4 Destination Port Inverse Match Enable When this bit is set, the Layer 4 Destination Port number<br>field is enabled for inverse matching. When this bit is reset, the Layer 4 Destination Port number field is<br>enabled for perfect matching. This bit is valid and applicable only when the L4DPM0 bit is set high.<br>0b - Layer 4 Destination Port Inverse Match is disabled<br>1b - Layer 4 Destination Port Inverse Match is enabled|
|20<br>L4DPM3|Layer 4 Destination Port Match Enable When this bit is set, the Layer 4 Destination Port number field is<br>enabled for matching. When this bit is reset, the MAC ignores the Layer 4 Destination Port number field<br>for matching.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3815 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function<br>0b - Layer 4 Destination Port Match is disabled<br>1b - Layer 4 Destination Port Match is enabled|
|---|---|
|19<br>L4SPIM3|Layer 4 Source Port Inverse Match Enable When this bit is set, the Layer 4 Source Port number field is<br>enabled for inverse matching. When this bit is reset, the Layer 4 Source Port number field is enabled for<br>perfect matching. This bit is valid and applicable only when the L4SPM0 bit is set high.<br>0b - Layer 4 Source Port Inverse Match is disabled<br>1b - Layer 4 Source Port Inverse Match is enabled|
|18<br>L4SPM3|Layer 4 Source Port Match Enable When this bit is set, the Layer 4 Source Port number field is enabled<br>for matching. When this bit is reset, the MAC ignores the Layer 4 Source Port number field for matching.<br>0b - Layer 4 Source Port Match is disabled<br>1b - Layer 4 Source Port Match is enabled|
|17<br>Reserved_17|Reserved.|
|16<br>L4PEN3|Layer 4 Protocol Enable When this bit is set, the Source and Destination Port number fields of UDP<br>packets are used for matching. When this bit is reset, the Source and Destination Port number fields of<br>TCP packets are used for matching. The Layer 4 matching is done only when the L4SPM0 or L4DPM0<br>bit is set.<br>0b - Layer 4 Protocol is disabled<br>1b - Layer 4 Protocol is enabled|
|15-11<br>L3HDBM3|Layer 3 IP DA Higher Bits Match IPv4 Packets: This field contains the number of higher bits of IP<br>Destination Address that are matched in the IPv4 packets. The following list describes the values of<br>this field: - 0: No bits are masked. - 1: LSb[0] is masked - 2: Two LSbs [1:0] are masked - .. - 31: All<br>bits except MSb are masked. IPv6 Packets: Bits[12:11] of this field correspond to Bits[6:5] of L3HSBM0<br>which indicate the number of lower bits of IP Source or Destination Address that are masked in the IPv6<br>packets. The following list describes the concatenated values of the L3HDBM0[1:0] and L3HSBM0 bits:<br>- 0: No bits are masked. - 1: LSb[0] is masked. - 2: Two LSbs [1:0] are masked - .. - 127: All bits except<br>MSb are masked. This field is valid and applicable only when the L3DAM0 or L3SAM0 bit is set.|
|10-6<br>L3HSBM3|Layer 3 IP SA Higher Bits Match IPv4 Packets: This field contains the number of lower bits of IP Source<br>Address that are masked for matching in the IPv4 packets. The following list describes the values of this<br>field: - 0: No bits are masked. - 1: LSb[0] is masked - 2: Two LSbs [1:0] are masked - .. - 31: All bits<br>except MSb are masked. IPv6 Packets: This field contains Bits[4:0] of L3HSBM0. These bits indicate the<br>number of higher bits of IP Source or Destination Address matched in the IPv6 packets. This field is valid<br>and applicable only when the L3DAM0 or L3SAM0 bit is set high.|
|5<br>L3DAIM3|Layer 3 IP DA Inverse Match Enable When this bit is set, the Layer 3 IP Destination Address field is<br>enabled for inverse matching. When this bit is reset, the Layer 3 IP Destination Address field is enabled<br>for perfect matching. This bit is valid and applicable only when the L3DAM0 bit is set high.<br>0b - Layer 3 IP DA Inverse Match is disabled<br>1b - Layer 3 IP DA Inverse Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3816 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|4<br>L3DAM3|Layer 3 IP DA Match Enable When this bit is set, the Layer 3 IP Destination Address field is enabled for<br>matching. When this bit is reset, the MAC ignores the Layer 3 IP Destination Address field for matching.<br>Note: When the L3PEN0 bit is set, you should set either this bit or the L3SAM0 bit because either IPv6<br>DA or SA can be checked for filtering.<br>0b - Layer 3 IP DA Match is disabled<br>1b - Layer 3 IP DA Match is enabled|
|3<br>L3SAIM3|Layer 3 IP SA Inverse Match Enable When this bit is set, the Layer 3 IP Source Address field is enabled<br>for inverse matching. When this bit reset, the Layer 3 IP Source Address field is enabled for perfect<br>matching. This bit is valid and applicable only when the L3SAM0 bit is set.<br>0b - Layer 3 IP SA Inverse Match is disabled<br>1b - Layer 3 IP SA Inverse Match is enabled|
|2<br>L3SAM3|Layer 3 IP SA Match Enable When this bit is set, the Layer 3 IP Source Address field is enabled for<br>matching. When this bit is reset, the MAC ignores the Layer 3 IP Source Address field for matching.<br>Note: When the L3PEN0 bit is set, you should set either this bit or the L3DAM0 bit because either IPv6<br>SA or DA can be checked for filtering.<br>0b - Layer 3 IP SA Match is disabled<br>1b - Layer 3 IP SA Match is enabled|
|1<br>Reserved_1|Reserved.|
|0<br>L3PEN3|Layer 3 Protocol Enable When this bit is set, the Layer 3 IP Source or Destination Address matching is<br>enabled for IPv6 packets. When this bit is reset, the Layer 3 IP Source or Destination Address matching<br>is enabled for IPv4 packets. The Layer 3 matching is done only when the L3SAM0 or L3DAM0 bit is set.<br>0b - Layer 3 Protocol is disabled<br>1b - Layer 3 Protocol is enabled|



# 75.7.182 (MAC_Layer4_Address3) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer4_Address3|994h|



## Function 

The MAC_Layer4_Address(#i), MAC_L3_L4_Control(#i), MAC_Layer3_Addr0_Reg(#i), MAC_Layer3_Addr1_Reg(#i), MAC_Layer3_Addr2_Reg(#i) and MAC_Layer3_Addr3_Reg(#i) registers are reserved (RO with default value) if Enable Layer 3 and Layer 4 Packet Filter option is not selected while configuring the IP. You can configure the Layer 3 and Layer 4 Address Registers to be double-synchronized by selecting the Synchronize Layer 3 and Layer 4 Address Registers to Rx Clock Domain option while configuring the IP. When you select this option, the synchronization is triggered only when Bits[31:24] (in little-endian mode) or Bits[7:0] (in big-endian mode) of the Layer 3 and Layer 4 Address Registers are written. For proper 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3817 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

synchronization updates, you should perform consecutive writes to same Layer 3 and Layer 4 Address Registers after at least four clock cycles delay of the destination clock. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3818-04.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>L4DP3<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>L4SP3<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-16<br>L4DP3|Layer 4 Destination Port Number Field When the L4PEN0 bit is reset and the L4DPM0 bit is set in the<br>MAC_L3_L4_Control0 register, this field contains the value to be matched with the TCP Destination<br>Port Number field in the IPv4 or IPv6 packets. When the L4PEN0 and L4DPM0 bits are set in<br>MAC_L3_L4_Control0 register, this field contains the value to be matched with the UDP Destination<br>Port Number field in the IPv4 or IPv6 packets.|
|15-0<br>L4SP3|Layer 4 Source Port Number Field When the L4PEN0 bit is reset and the L4SPM0 bit is set in<br>the MAC_L3_L4_Control0 register, this field contains the value to be matched with the TCP Source<br>Port Number field in the IPv4 or IPv6 packets. When the L4PEN0 and L4SPM0 bits are set in<br>MAC_L3_L4_Control0 register, this field contains the value to be matched with the UDP Source Port<br>Number field in the IPv4 or IPv6 packets.|



# 75.7.183 (MAC_Layer3_Addr0_Reg3) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr0_Re<br>g3|9A0h|



## Function 

For IPv4 packets, the Layer 3 Address 0 Register 0 register contains the 32-bit IP Source Address field. For IPv6 packets, it contains Bits[31:0] of the 128-bit IP Source Address or Destination Address field. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3818 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3819-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>L3A03<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>L3A03<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0<br>L3A03|Layer 3 Address 0 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0<br>register, this field contains the value to be matched with Bits[31:0] of the IP Source Address field in the<br>IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with Bits[31:0] of the IP Destination Address field in the IPv6 packets.|
||When the L3PEN0 bit is reset and the L3SAM0 bit is set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with the IP Source Address field in the IPv4 packets.|



# 75.7.184 (MAC_Layer3_Addr1_Reg3) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr1_Re<br>g3|9A4h|



## Function 

For IPv4 packets, the Layer 3 Address 1 Register 0 register contains the 32-bit IP Destination Address field. For IPv6 packets, it contains Bits[63:32] of the 128-bit IP Source Address or Destination Address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3|A13||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3|A13||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3819 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0<br>L3A13|Layer 3 Address 1 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0<br>register, this field contains the value to be matched with Bits[63:32] of the IP Source Address field in the<br>IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with Bits[63:32] of the IP Destination Address field in the IPv6 packets.|
||When the L3PEN0 bit is reset and the L3SAM0 bit is set in the MAC_L3_L4_Control0 register, this field<br>contains the value to be matched with the IP Destination Address field in the IPv4 packets.|



# 75.7.185 (MAC_Layer3_Addr2_Reg3) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr2_Re<br>g3|9A8h|



## Function 

The Layer 3 Address 2 Register 0 register is reserved for IPv4 packets. For IPv6 packets, it contains Bits[95:64] of 128-bit IP Source Address or Destination Address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3|A23||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3|A23||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 2 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0|
|L3A23|register, this field contains the value to be matched with Bits[95:64] of the IP Source Address field in the<br>IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with Bits[95:64] of the IP Destination Address field in the IPv6 packets.|
||When the L3PEN0 bit is reset in the MAC_L3_L4_Control0 register, this field is not used.|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3820 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.186 (MAC_Layer3_Addr3_Reg3) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr3_Re<br>g3|9ACh|



## Function 

The Layer 3 Address 3 Register 0 register is reserved for IPv4 packets. For IPv6 packets, it contains Bits[127:96] of 128-bit IP Source Address or Destination Address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3|A33||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3|A33||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 3 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0|
|L3A33|register, this field contains the value to be matched with Bits[127:96] of the IP Source Address field in|
||the IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this|
||field contains the value to be matched with Bits[127:96] of the IP Destination Address field in the IPv6|
||packets. When the L3PEN0 bit is reset in the MAC_L3_L4_Control0 register, this field is not used.|



# 75.7.187 (MAC_L3_L4_Control4) 

## Offset 

|Register|Offset|
|---|---|
|MAC_L3_L4_Control4|9C0h|



## Function 

The Layer 3 and Layer 4 Control register controls the operations of filter 0 of Layer 3 and Layer 4. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3821 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3822-02.png)


<!-- Start of picture text -->
Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserved_23_2 Reserv<br>R Reserved_31_29  DMCH Reserved_27_y  DMCHN4  2  L4DPI L4DP L4SPI L4SP e... L4PEN<br>EN4  M4  M4  M4  M4  4<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv<br>R L3HDBM4  L3HSBM4  L3DAI L3DA L3SAI L3SA e... L3PEN<br>M4  M4  M4  M4  4<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-29|Reserved.|
|Reserved_31_2<br>9||
|28<br>DMCHEN4|DMA Channel Select Enable When set, this bit enables the selection of the DMA channel number for the<br>packet that is passed by this L3_L4 filter. The DMA channel is indicated by the DMCHN bits. When this<br>bit is reset, the DMA channel is not decided by this filter.<br>0b - DMA Channel Select is disabled<br>1b - DMA Channel Select is enabled|
|27-26|Reserved.|
|Reserved_27_y||
|25-24<br>DMCHN4|DMA Channel Number When DMCHEN is set high, this field selects the DMA Channel number to which<br>the packet passed by this filter is routed. The width of this field depends on the number of the DMA<br>channels present in your configuration.|
|23-22|Reserved.|
|Reserved_23_2<br>2||
|21<br>L4DPIM4|Layer 4 Destination Port Inverse Match Enable When this bit is set, the Layer 4 Destination Port number<br>field is enabled for inverse matching. When this bit is reset, the Layer 4 Destination Port number field is<br>enabled for perfect matching. This bit is valid and applicable only when the L4DPM0 bit is set high.<br>0b - Layer 4 Destination Port Inverse Match is disabled<br>1b - Layer 4 Destination Port Inverse Match is enabled|
|20<br>L4DPM4|Layer 4 Destination Port Match Enable When this bit is set, the Layer 4 Destination Port number field is<br>enabled for matching. When this bit is reset, the MAC ignores the Layer 4 Destination Port number field<br>for matching.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3822 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function<br>0b - Layer 4 Destination Port Match is disabled<br>1b - Layer 4 Destination Port Match is enabled|
|---|---|
|19<br>L4SPIM4|Layer 4 Source Port Inverse Match Enable When this bit is set, the Layer 4 Source Port number field is<br>enabled for inverse matching. When this bit is reset, the Layer 4 Source Port number field is enabled for<br>perfect matching. This bit is valid and applicable only when the L4SPM0 bit is set high.<br>0b - Layer 4 Source Port Inverse Match is disabled<br>1b - Layer 4 Source Port Inverse Match is enabled|
|18<br>L4SPM4|Layer 4 Source Port Match Enable When this bit is set, the Layer 4 Source Port number field is enabled<br>for matching. When this bit is reset, the MAC ignores the Layer 4 Source Port number field for matching.<br>0b - Layer 4 Source Port Match is disabled<br>1b - Layer 4 Source Port Match is enabled|
|17<br>Reserved_17|Reserved.|
|16<br>L4PEN4|Layer 4 Protocol Enable When this bit is set, the Source and Destination Port number fields of UDP<br>packets are used for matching. When this bit is reset, the Source and Destination Port number fields of<br>TCP packets are used for matching. The Layer 4 matching is done only when the L4SPM0 or L4DPM0<br>bit is set.<br>0b - Layer 4 Protocol is disabled<br>1b - Layer 4 Protocol is enabled|
|15-11<br>L3HDBM4|Layer 3 IP DA Higher Bits Match IPv4 Packets: This field contains the number of higher bits of IP<br>Destination Address that are matched in the IPv4 packets. The following list describes the values of<br>this field: - 0: No bits are masked. - 1: LSb[0] is masked - 2: Two LSbs [1:0] are masked - .. - 31: All<br>bits except MSb are masked. IPv6 Packets: Bits[12:11] of this field correspond to Bits[6:5] of L3HSBM0<br>which indicate the number of lower bits of IP Source or Destination Address that are masked in the IPv6<br>packets. The following list describes the concatenated values of the L3HDBM0[1:0] and L3HSBM0 bits:<br>- 0: No bits are masked. - 1: LSb[0] is masked. - 2: Two LSbs [1:0] are masked - .. - 127: All bits except<br>MSb are masked. This field is valid and applicable only when the L3DAM0 or L3SAM0 bit is set.|
|10-6<br>L3HSBM4|Layer 3 IP SA Higher Bits Match IPv4 Packets: This field contains the number of lower bits of IP Source<br>Address that are masked for matching in the IPv4 packets. The following list describes the values of this<br>field: - 0: No bits are masked. - 1: LSb[0] is masked - 2: Two LSbs [1:0] are masked - .. - 31: All bits<br>except MSb are masked. IPv6 Packets: This field contains Bits[4:0] of L3HSBM0. These bits indicate the<br>number of higher bits of IP Source or Destination Address matched in the IPv6 packets. This field is valid<br>and applicable only when the L3DAM0 or L3SAM0 bit is set high.|
|5<br>L3DAIM4|Layer 3 IP DA Inverse Match Enable When this bit is set, the Layer 3 IP Destination Address field is<br>enabled for inverse matching. When this bit is reset, the Layer 3 IP Destination Address field is enabled<br>for perfect matching. This bit is valid and applicable only when the L3DAM0 bit is set high.<br>0b - Layer 3 IP DA Inverse Match is disabled<br>1b - Layer 3 IP DA Inverse Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3823 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|4<br>L3DAM4|Layer 3 IP DA Match Enable When this bit is set, the Layer 3 IP Destination Address field is enabled for<br>matching. When this bit is reset, the MAC ignores the Layer 3 IP Destination Address field for matching.<br>Note: When the L3PEN0 bit is set, you should set either this bit or the L3SAM0 bit because either IPv6<br>DA or SA can be checked for filtering.<br>0b - Layer 3 IP DA Match is disabled<br>1b - Layer 3 IP DA Match is enabled|
|3<br>L3SAIM4|Layer 3 IP SA Inverse Match Enable When this bit is set, the Layer 3 IP Source Address field is enabled<br>for inverse matching. When this bit reset, the Layer 3 IP Source Address field is enabled for perfect<br>matching. This bit is valid and applicable only when the L3SAM0 bit is set.<br>0b - Layer 3 IP SA Inverse Match is disabled<br>1b - Layer 3 IP SA Inverse Match is enabled|
|2<br>L3SAM4|Layer 3 IP SA Match Enable When this bit is set, the Layer 3 IP Source Address field is enabled for<br>matching. When this bit is reset, the MAC ignores the Layer 3 IP Source Address field for matching.<br>Note: When the L3PEN0 bit is set, you should set either this bit or the L3DAM0 bit because either IPv6<br>SA or DA can be checked for filtering.<br>0b - Layer 3 IP SA Match is disabled<br>1b - Layer 3 IP SA Match is enabled|
|1<br>Reserved_1|Reserved.|
|0<br>L3PEN4|Layer 3 Protocol Enable When this bit is set, the Layer 3 IP Source or Destination Address matching is<br>enabled for IPv6 packets. When this bit is reset, the Layer 3 IP Source or Destination Address matching<br>is enabled for IPv4 packets. The Layer 3 matching is done only when the L3SAM0 or L3DAM0 bit is set.<br>0b - Layer 3 Protocol is disabled<br>1b - Layer 3 Protocol is enabled|



# 75.7.188 (MAC_Layer4_Address4) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer4_Address4|9C4h|



## Function 

The MAC_Layer4_Address(#i), MAC_L3_L4_Control(#i), MAC_Layer3_Addr0_Reg(#i), MAC_Layer3_Addr1_Reg(#i), MAC_Layer3_Addr2_Reg(#i) and MAC_Layer3_Addr3_Reg(#i) registers are reserved (RO with default value) if Enable Layer 3 and Layer 4 Packet Filter option is not selected while configuring the IP. You can configure the Layer 3 and Layer 4 Address Registers to be double-synchronized by selecting the Synchronize Layer 3 and Layer 4 Address Registers to Rx Clock Domain option while configuring the IP. When you select this option, the synchronization is triggered only when Bits[31:24] (in little-endian mode) or Bits[7:0] (in big-endian mode) of the Layer 3 and Layer 4 Address Registers are written. For proper 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3824 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

synchronization updates, you should perform consecutive writes to same Layer 3 and Layer 4 Address Registers after at least four clock cycles delay of the destination clock. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L4|DP4||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L4|SP4||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-16<br>L4DP4|Layer 4 Destination Port Number Field When the L4PEN0 bit is reset and the L4DPM0 bit is set in the<br>MAC_L3_L4_Control0 register, this field contains the value to be matched with the TCP Destination<br>Port Number field in the IPv4 or IPv6 packets. When the L4PEN0 and L4DPM0 bits are set in<br>MAC_L3_L4_Control0 register, this field contains the value to be matched with the UDP Destination<br>Port Number field in the IPv4 or IPv6 packets.|
|15-0<br>L4SP4|Layer 4 Source Port Number Field When the L4PEN0 bit is reset and the L4SPM0 bit is set in<br>the MAC_L3_L4_Control0 register, this field contains the value to be matched with the TCP Source<br>Port Number field in the IPv4 or IPv6 packets. When the L4PEN0 and L4SPM0 bits are set in<br>MAC_L3_L4_Control0 register, this field contains the value to be matched with the UDP Source Port<br>Number field in the IPv4 or IPv6 packets.|



# 75.7.189 (MAC_Layer3_Addr0_Reg4) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr0_Re<br>g4|9D0h|



## Function 

For IPv4 packets, the Layer 3 Address 0 Register 0 register contains the 32-bit IP Source Address field. For IPv6 packets, it contains Bits[31:0] of the 128-bit IP Source Address or Destination Address field. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3825 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3826-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>L3A04<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>L3A04<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0<br>L3A04|Layer 3 Address 0 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0<br>register, this field contains the value to be matched with Bits[31:0] of the IP Source Address field in the<br>IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with Bits[31:0] of the IP Destination Address field in the IPv6 packets.|
||When the L3PEN0 bit is reset and the L3SAM0 bit is set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with the IP Source Address field in the IPv4 packets.|



# 75.7.190 (MAC_Layer3_Addr1_Reg4) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr1_Re<br>g4|9D4h|



## Function 

For IPv4 packets, the Layer 3 Address 1 Register 0 register contains the 32-bit IP Destination Address field. For IPv6 packets, it contains Bits[63:32] of the 128-bit IP Source Address or Destination Address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3|A14||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3|A14||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3826 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0<br>L3A14|Layer 3 Address 1 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0<br>register, this field contains the value to be matched with Bits[63:32] of the IP Source Address field in the<br>IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with Bits[63:32] of the IP Destination Address field in the IPv6 packets.|
||When the L3PEN0 bit is reset and the L3SAM0 bit is set in the MAC_L3_L4_Control0 register, this field<br>contains the value to be matched with the IP Destination Address field in the IPv4 packets.|



# 75.7.191 (MAC_Layer3_Addr2_Reg4) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr2_Re<br>g4|9D8h|



## Function 

The Layer 3 Address 2 Register 0 register is reserved for IPv4 packets. For IPv6 packets, it contains Bits[95:64] of 128-bit IP Source Address or Destination Address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3|A24||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3|A24||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 2 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0|
|L3A24|register, this field contains the value to be matched with Bits[95:64] of the IP Source Address field in the<br>IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with Bits[95:64] of the IP Destination Address field in the IPv6 packets.|
||When the L3PEN0 bit is reset in the MAC_L3_L4_Control0 register, this field is not used.|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3827 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.192 (MAC_Layer3_Addr3_Reg4) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr3_Re<br>g4|9DCh|



## Function 

The Layer 3 Address 3 Register 0 register is reserved for IPv4 packets. For IPv6 packets, it contains Bits[127:96] of 128-bit IP Source Address or Destination Address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3|A34||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3|A34||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 3 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0|
|L3A34|register, this field contains the value to be matched with Bits[127:96] of the IP Source Address field in|
||the IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this|
||field contains the value to be matched with Bits[127:96] of the IP Destination Address field in the IPv6|
||packets. When the L3PEN0 bit is reset in the MAC_L3_L4_Control0 register, this field is not used.|



# 75.7.193 (MAC_L3_L4_Control5) 

## Offset 

|Register|Offset|
|---|---|
|MAC_L3_L4_Control5|9F0h|



## Function 

The Layer 3 and Layer 4 Control register controls the operations of filter 0 of Layer 3 and Layer 4. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3828 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3829-02.png)


<!-- Start of picture text -->
Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserved_23_2 Reserv<br>R Reserved_31_29  DMCH Reserved_27_y  DMCHN5  2  L4DPI L4DP L4SPI L4SP e... L4PEN<br>EN5  M5  M5  M5  M5  5<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv<br>R L3HDBM5  L3HSBM5  L3DAI L3DA L3SAI L3SA e... L3PEN<br>M5  M5  M5  M5  5<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-29|Reserved.|
|Reserved_31_2<br>9||
|28<br>DMCHEN5|DMA Channel Select Enable When set, this bit enables the selection of the DMA channel number for the<br>packet that is passed by this L3_L4 filter. The DMA channel is indicated by the DMCHN bits. When this<br>bit is reset, the DMA channel is not decided by this filter.<br>0b - DMA Channel Select is disabled<br>1b - DMA Channel Select is enabled|
|27-26|Reserved.|
|Reserved_27_y||
|25-24<br>DMCHN5|DMA Channel Number When DMCHEN is set high, this field selects the DMA Channel number to which<br>the packet passed by this filter is routed. The width of this field depends on the number of the DMA<br>channels present in your configuration.|
|23-22|Reserved.|
|Reserved_23_2<br>2||
|21<br>L4DPIM5|Layer 4 Destination Port Inverse Match Enable When this bit is set, the Layer 4 Destination Port number<br>field is enabled for inverse matching. When this bit is reset, the Layer 4 Destination Port number field is<br>enabled for perfect matching. This bit is valid and applicable only when the L4DPM0 bit is set high.<br>0b - Layer 4 Destination Port Inverse Match is disabled<br>1b - Layer 4 Destination Port Inverse Match is enabled|
|20<br>L4DPM5|Layer 4 Destination Port Match Enable When this bit is set, the Layer 4 Destination Port number field is<br>enabled for matching. When this bit is reset, the MAC ignores the Layer 4 Destination Port number field<br>for matching.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3829 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function<br>0b - Layer 4 Destination Port Match is disabled<br>1b - Layer 4 Destination Port Match is enabled|
|---|---|
|19<br>L4SPIM5|Layer 4 Source Port Inverse Match Enable When this bit is set, the Layer 4 Source Port number field is<br>enabled for inverse matching. When this bit is reset, the Layer 4 Source Port number field is enabled for<br>perfect matching. This bit is valid and applicable only when the L4SPM0 bit is set high.<br>0b - Layer 4 Source Port Inverse Match is disabled<br>1b - Layer 4 Source Port Inverse Match is enabled|
|18<br>L4SPM5|Layer 4 Source Port Match Enable When this bit is set, the Layer 4 Source Port number field is enabled<br>for matching. When this bit is reset, the MAC ignores the Layer 4 Source Port number field for matching.<br>0b - Layer 4 Source Port Match is disabled<br>1b - Layer 4 Source Port Match is enabled|
|17<br>Reserved_17|Reserved.|
|16<br>L4PEN5|Layer 4 Protocol Enable When this bit is set, the Source and Destination Port number fields of UDP<br>packets are used for matching. When this bit is reset, the Source and Destination Port number fields of<br>TCP packets are used for matching. The Layer 4 matching is done only when the L4SPM0 or L4DPM0<br>bit is set.<br>0b - Layer 4 Protocol is disabled<br>1b - Layer 4 Protocol is enabled|
|15-11<br>L3HDBM5|Layer 3 IP DA Higher Bits Match IPv4 Packets: This field contains the number of higher bits of IP<br>Destination Address that are matched in the IPv4 packets. The following list describes the values of<br>this field: - 0: No bits are masked. - 1: LSb[0] is masked - 2: Two LSbs [1:0] are masked - .. - 31: All<br>bits except MSb are masked. IPv6 Packets: Bits[12:11] of this field correspond to Bits[6:5] of L3HSBM0<br>which indicate the number of lower bits of IP Source or Destination Address that are masked in the IPv6<br>packets. The following list describes the concatenated values of the L3HDBM0[1:0] and L3HSBM0 bits:<br>- 0: No bits are masked. - 1: LSb[0] is masked. - 2: Two LSbs [1:0] are masked - .. - 127: All bits except<br>MSb are masked. This field is valid and applicable only when the L3DAM0 or L3SAM0 bit is set.|
|10-6<br>L3HSBM5|Layer 3 IP SA Higher Bits Match IPv4 Packets: This field contains the number of lower bits of IP Source<br>Address that are masked for matching in the IPv4 packets. The following list describes the values of this<br>field: - 0: No bits are masked. - 1: LSb[0] is masked - 2: Two LSbs [1:0] are masked - .. - 31: All bits<br>except MSb are masked. IPv6 Packets: This field contains Bits[4:0] of L3HSBM0. These bits indicate the<br>number of higher bits of IP Source or Destination Address matched in the IPv6 packets. This field is valid<br>and applicable only when the L3DAM0 or L3SAM0 bit is set high.|
|5<br>L3DAIM5|Layer 3 IP DA Inverse Match Enable When this bit is set, the Layer 3 IP Destination Address field is<br>enabled for inverse matching. When this bit is reset, the Layer 3 IP Destination Address field is enabled<br>for perfect matching. This bit is valid and applicable only when the L3DAM0 bit is set high.<br>0b - Layer 3 IP DA Inverse Match is disabled<br>1b - Layer 3 IP DA Inverse Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3830 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|4<br>L3DAM5|Layer 3 IP DA Match Enable When this bit is set, the Layer 3 IP Destination Address field is enabled for<br>matching. When this bit is reset, the MAC ignores the Layer 3 IP Destination Address field for matching.<br>Note: When the L3PEN0 bit is set, you should set either this bit or the L3SAM0 bit because either IPv6<br>DA or SA can be checked for filtering.<br>0b - Layer 3 IP DA Match is disabled<br>1b - Layer 3 IP DA Match is enabled|
|3<br>L3SAIM5|Layer 3 IP SA Inverse Match Enable When this bit is set, the Layer 3 IP Source Address field is enabled<br>for inverse matching. When this bit reset, the Layer 3 IP Source Address field is enabled for perfect<br>matching. This bit is valid and applicable only when the L3SAM0 bit is set.<br>0b - Layer 3 IP SA Inverse Match is disabled<br>1b - Layer 3 IP SA Inverse Match is enabled|
|2<br>L3SAM5|Layer 3 IP SA Match Enable When this bit is set, the Layer 3 IP Source Address field is enabled for<br>matching. When this bit is reset, the MAC ignores the Layer 3 IP Source Address field for matching.<br>Note: When the L3PEN0 bit is set, you should set either this bit or the L3DAM0 bit because either IPv6<br>SA or DA can be checked for filtering.<br>0b - Layer 3 IP SA Match is disabled<br>1b - Layer 3 IP SA Match is enabled|
|1<br>Reserved_1|Reserved.|
|0<br>L3PEN5|Layer 3 Protocol Enable When this bit is set, the Layer 3 IP Source or Destination Address matching is<br>enabled for IPv6 packets. When this bit is reset, the Layer 3 IP Source or Destination Address matching<br>is enabled for IPv4 packets. The Layer 3 matching is done only when the L3SAM0 or L3DAM0 bit is set.<br>0b - Layer 3 Protocol is disabled<br>1b - Layer 3 Protocol is enabled|



# 75.7.194 (MAC_Layer4_Address5) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer4_Address5|9F4h|



## Function 

The MAC_Layer4_Address(#i), MAC_L3_L4_Control(#i), MAC_Layer3_Addr0_Reg(#i), MAC_Layer3_Addr1_Reg(#i), MAC_Layer3_Addr2_Reg(#i) and MAC_Layer3_Addr3_Reg(#i) registers are reserved (RO with default value) if Enable Layer 3 and Layer 4 Packet Filter option is not selected while configuring the IP. You can configure the Layer 3 and Layer 4 Address Registers to be double-synchronized by selecting the Synchronize Layer 3 and Layer 4 Address Registers to Rx Clock Domain option while configuring the IP. When you select this option, the synchronization is triggered only when Bits[31:24] (in little-endian mode) or Bits[7:0] (in big-endian mode) of the Layer 3 and Layer 4 Address Registers are written. For proper 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3831 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

synchronization updates, you should perform consecutive writes to same Layer 3 and Layer 4 Address Registers after at least four clock cycles delay of the destination clock. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3832-04.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>L4DP5<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>L4SP5<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-16<br>L4DP5|Layer 4 Destination Port Number Field When the L4PEN0 bit is reset and the L4DPM0 bit is set in the<br>MAC_L3_L4_Control0 register, this field contains the value to be matched with the TCP Destination<br>Port Number field in the IPv4 or IPv6 packets. When the L4PEN0 and L4DPM0 bits are set in<br>MAC_L3_L4_Control0 register, this field contains the value to be matched with the UDP Destination<br>Port Number field in the IPv4 or IPv6 packets.|
|15-0<br>L4SP5|Layer 4 Source Port Number Field When the L4PEN0 bit is reset and the L4SPM0 bit is set in<br>the MAC_L3_L4_Control0 register, this field contains the value to be matched with the TCP Source<br>Port Number field in the IPv4 or IPv6 packets. When the L4PEN0 and L4SPM0 bits are set in<br>MAC_L3_L4_Control0 register, this field contains the value to be matched with the UDP Source Port<br>Number field in the IPv4 or IPv6 packets.|



# 75.7.195 (MAC_Layer3_Addr0_Reg5) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr0_Re<br>g5|A00h|



## Function 

For IPv4 packets, the Layer 3 Address 0 Register 0 register contains the 32-bit IP Source Address field. For IPv6 packets, it contains Bits[31:0] of the 128-bit IP Source Address or Destination Address field. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3832 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3833-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>L3A05<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>L3A05<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0<br>L3A05|Layer 3 Address 0 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0<br>register, this field contains the value to be matched with Bits[31:0] of the IP Source Address field in the<br>IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with Bits[31:0] of the IP Destination Address field in the IPv6 packets.|
||When the L3PEN0 bit is reset and the L3SAM0 bit is set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with the IP Source Address field in the IPv4 packets.|



# 75.7.196 (MAC_Layer3_Addr1_Reg5) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr1_Re<br>g5|A04h|



## Function 

For IPv4 packets, the Layer 3 Address 1 Register 0 register contains the 32-bit IP Destination Address field. For IPv6 packets, it contains Bits[63:32] of the 128-bit IP Source Address or Destination Address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3|A15||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3|A15||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3833 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0<br>L3A15|Layer 3 Address 1 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0<br>register, this field contains the value to be matched with Bits[63:32] of the IP Source Address field in the<br>IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with Bits[63:32] of the IP Destination Address field in the IPv6 packets.|
||When the L3PEN0 bit is reset and the L3SAM0 bit is set in the MAC_L3_L4_Control0 register, this field<br>contains the value to be matched with the IP Destination Address field in the IPv4 packets.|



# 75.7.197 (MAC_Layer3_Addr2_Reg5) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr2_Re<br>g5|A08h|



## Function 

The Layer 3 Address 2 Register 0 register is reserved for IPv4 packets. For IPv6 packets, it contains Bits[95:64] of 128-bit IP Source Address or Destination Address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3|A25||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3|A25||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 2 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0|
|L3A25|register, this field contains the value to be matched with Bits[95:64] of the IP Source Address field in the<br>IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with Bits[95:64] of the IP Destination Address field in the IPv6 packets.|
||When the L3PEN0 bit is reset in the MAC_L3_L4_Control0 register, this field is not used.|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3834 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.198 (MAC_Layer3_Addr3_Reg5) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr3_Re<br>g5|A0Ch|



## Function 

The Layer 3 Address 3 Register 0 register is reserved for IPv4 packets. For IPv6 packets, it contains Bits[127:96] of 128-bit IP Source Address or Destination Address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3|A35||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3|A35||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 3 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0|
|L3A3|register, this field contains the value to be matched with Bits[127:96] of the IP Source Address field in|
|5|the IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this|
||field contains the value to be matched with Bits[127:96] of the IP Destination Address field in the IPv6|
||packets. When the L3PEN0 bit is reset in the MAC_L3_L4_Control0 register, this field is not used.|



# 75.7.199 (MAC_L3_L4_Control6) 

## Offset 

|Register|Offset|
|---|---|
|MAC_L3_L4_Control6|A20h|



## Function 

The Layer 3 and Layer 4 Control register controls the operations of filter 0 of Layer 3 and Layer 4. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3835 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3836-02.png)


<!-- Start of picture text -->
Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserved_23_2 Reserv<br>R Reserved_31_29  DMCH Reserved_27_y  DMCHN6  2  L4DPI L4DP L4SPI L4SP e... L4PEN<br>EN6  M6  M6  M6  M6  6<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv<br>R L3HDBM6  L3HSBM6  L3DAI L3DA L3SAI L3SA e... L3PEN<br>M6  M6  M6  M6  6<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-29|Reserved.|
|Reserved_31_2<br>9||
|28<br>DMCHEN6|DMA Channel Select Enable When set, this bit enables the selection of the DMA channel number for the<br>packet that is passed by this L3_L4 filter. The DMA channel is indicated by the DMCHN bits. When this<br>bit is reset, the DMA channel is not decided by this filter.<br>0b - DMA Channel Select is disabled<br>1b - DMA Channel Select is enabled|
|27-26|Reserved.|
|Reserved_27_y||
|25-24<br>DMCHN6|DMA Channel Number When DMCHEN is set high, this field selects the DMA Channel number to which<br>the packet passed by this filter is routed. The width of this field depends on the number of the DMA<br>channels present in your configuration.|
|23-22|Reserved.|
|Reserved_23_2<br>2||
|21<br>L4DPIM6|Layer 4 Destination Port Inverse Match Enable When this bit is set, the Layer 4 Destination Port number<br>field is enabled for inverse matching. When this bit is reset, the Layer 4 Destination Port number field is<br>enabled for perfect matching. This bit is valid and applicable only when the L4DPM0 bit is set high.<br>0b - Layer 4 Destination Port Inverse Match is disabled<br>1b - Layer 4 Destination Port Inverse Match is enabled|
|20<br>L4DPM6|Layer 4 Destination Port Match Enable When this bit is set, the Layer 4 Destination Port number field is<br>enabled for matching. When this bit is reset, the MAC ignores the Layer 4 Destination Port number field<br>for matching.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3836 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function<br>0b - Layer 4 Destination Port Match is disabled<br>1b - Layer 4 Destination Port Match is enabled|
|---|---|
|19<br>L4SPIM6|Layer 4 Source Port Inverse Match Enable When this bit is set, the Layer 4 Source Port number field is<br>enabled for inverse matching. When this bit is reset, the Layer 4 Source Port number field is enabled for<br>perfect matching. This bit is valid and applicable only when the L4SPM0 bit is set high.<br>0b - Layer 4 Source Port Inverse Match is disabled<br>1b - Layer 4 Source Port Inverse Match is enabled|
|18<br>L4SPM6|Layer 4 Source Port Match Enable When this bit is set, the Layer 4 Source Port number field is enabled<br>for matching. When this bit is reset, the MAC ignores the Layer 4 Source Port number field for matching.<br>0b - Layer 4 Source Port Match is disabled<br>1b - Layer 4 Source Port Match is enabled|
|17<br>Reserved_17|Reserved.|
|16<br>L4PEN6|Layer 4 Protocol Enable When this bit is set, the Source and Destination Port number fields of UDP<br>packets are used for matching. When this bit is reset, the Source and Destination Port number fields of<br>TCP packets are used for matching. The Layer 4 matching is done only when the L4SPM0 or L4DPM0<br>bit is set.<br>0b - Layer 4 Protocol is disabled<br>1b - Layer 4 Protocol is enabled|
|15-11<br>L3HDBM6|Layer 3 IP DA Higher Bits Match IPv4 Packets: This field contains the number of higher bits of IP<br>Destination Address that are matched in the IPv4 packets. The following list describes the values of<br>this field: - 0: No bits are masked. - 1: LSb[0] is masked - 2: Two LSbs [1:0] are masked - .. - 31: All<br>bits except MSb are masked. IPv6 Packets: Bits[12:11] of this field correspond to Bits[6:5] of L3HSBM0<br>which indicate the number of lower bits of IP Source or Destination Address that are masked in the IPv6<br>packets. The following list describes the concatenated values of the L3HDBM0[1:0] and L3HSBM0 bits:<br>- 0: No bits are masked. - 1: LSb[0] is masked. - 2: Two LSbs [1:0] are masked - .. - 127: All bits except<br>MSb are masked. This field is valid and applicable only when the L3DAM0 or L3SAM0 bit is set.|
|10-6<br>L3HSBM6|Layer 3 IP SA Higher Bits Match IPv4 Packets: This field contains the number of lower bits of IP Source<br>Address that are masked for matching in the IPv4 packets. The following list describes the values of this<br>field: - 0: No bits are masked. - 1: LSb[0] is masked - 2: Two LSbs [1:0] are masked - .. - 31: All bits<br>except MSb are masked. IPv6 Packets: This field contains Bits[4:0] of L3HSBM0. These bits indicate the<br>number of higher bits of IP Source or Destination Address matched in the IPv6 packets. This field is valid<br>and applicable only when the L3DAM0 or L3SAM0 bit is set high.|
|5<br>L3DAIM6|Layer 3 IP DA Inverse Match Enable When this bit is set, the Layer 3 IP Destination Address field is<br>enabled for inverse matching. When this bit is reset, the Layer 3 IP Destination Address field is enabled<br>for perfect matching. This bit is valid and applicable only when the L3DAM0 bit is set high.<br>0b - Layer 3 IP DA Inverse Match is disabled<br>1b - Layer 3 IP DA Inverse Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3837 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|4<br>L3DAM6|Layer 3 IP DA Match Enable When this bit is set, the Layer 3 IP Destination Address field is enabled for<br>matching. When this bit is reset, the MAC ignores the Layer 3 IP Destination Address field for matching.<br>Note: When the L3PEN0 bit is set, you should set either this bit or the L3SAM0 bit because either IPv6<br>DA or SA can be checked for filtering.<br>0b - Layer 3 IP DA Match is disabled<br>1b - Layer 3 IP DA Match is enabled|
|3<br>L3SAIM6|Layer 3 IP SA Inverse Match Enable When this bit is set, the Layer 3 IP Source Address field is enabled<br>for inverse matching. When this bit reset, the Layer 3 IP Source Address field is enabled for perfect<br>matching. This bit is valid and applicable only when the L3SAM0 bit is set.<br>0b - Layer 3 IP SA Inverse Match is disabled<br>1b - Layer 3 IP SA Inverse Match is enabled|
|2<br>L3SAM6|Layer 3 IP SA Match Enable When this bit is set, the Layer 3 IP Source Address field is enabled for<br>matching. When this bit is reset, the MAC ignores the Layer 3 IP Source Address field for matching.<br>Note: When the L3PEN0 bit is set, you should set either this bit or the L3DAM0 bit because either IPv6<br>SA or DA can be checked for filtering.<br>0b - Layer 3 IP SA Match is disabled<br>1b - Layer 3 IP SA Match is enabled|
|1<br>Reserved_1|Reserved.|
|0<br>L3PEN6|Layer 3 Protocol Enable When this bit is set, the Layer 3 IP Source or Destination Address matching is<br>enabled for IPv6 packets. When this bit is reset, the Layer 3 IP Source or Destination Address matching<br>is enabled for IPv4 packets. The Layer 3 matching is done only when the L3SAM0 or L3DAM0 bit is set.<br>0b - Layer 3 Protocol is disabled<br>1b - Layer 3 Protocol is enabled|



# 75.7.200 (MAC_Layer4_Address6) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer4_Address6|A24h|



## Function 

The MAC_Layer4_Address(#i), MAC_L3_L4_Control(#i), MAC_Layer3_Addr0_Reg(#i), MAC_Layer3_Addr1_Reg(#i), MAC_Layer3_Addr2_Reg(#i) and MAC_Layer3_Addr3_Reg(#i) registers are reserved (RO with default value) if Enable Layer 3 and Layer 4 Packet Filter option is not selected while configuring the IP. You can configure the Layer 3 and Layer 4 Address Registers to be double-synchronized by selecting the Synchronize Layer 3 and Layer 4 Address Registers to Rx Clock Domain option while configuring the IP. When you select this option, the synchronization is triggered only when Bits[31:24] (in little-endian mode) or Bits[7:0] (in big-endian mode) of the Layer 3 and Layer 4 Address Registers are written. For proper 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3838 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

synchronization updates, you should perform consecutive writes to same Layer 3 and Layer 4 Address Registers after at least four clock cycles delay of the destination clock. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3839-04.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>L4DP6<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>L4SP6<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-16<br>L4DP6|Layer 4 Destination Port Number Field When the L4PEN0 bit is reset and the L4DPM0 bit is set in the<br>MAC_L3_L4_Control0 register, this field contains the value to be matched with the TCP Destination<br>Port Number field in the IPv4 or IPv6 packets. When the L4PEN0 and L4DPM0 bits are set in<br>MAC_L3_L4_Control0 register, this field contains the value to be matched with the UDP Destination<br>Port Number field in the IPv4 or IPv6 packets.|
|15-0<br>L4SP6|Layer 4 Source Port Number Field When the L4PEN0 bit is reset and the L4SPM0 bit is set in<br>the MAC_L3_L4_Control0 register, this field contains the value to be matched with the TCP Source<br>Port Number field in the IPv4 or IPv6 packets. When the L4PEN0 and L4SPM0 bits are set in<br>MAC_L3_L4_Control0 register, this field contains the value to be matched with the UDP Source Port<br>Number field in the IPv4 or IPv6 packets.|



# 75.7.201 (MAC_Layer3_Addr0_Reg6) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr0_Re<br>g6|A30h|



## Function 

For IPv4 packets, the Layer 3 Address 0 Register 0 register contains the 32-bit IP Source Address field. For IPv6 packets, it contains Bits[31:0] of the 128-bit IP Source Address or Destination Address field. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3839 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3840-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>L3A06<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>L3A06<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0<br>L3A06|Layer 3 Address 0 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0<br>register, this field contains the value to be matched with Bits[31:0] of the IP Source Address field in the<br>IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with Bits[31:0] of the IP Destination Address field in the IPv6 packets.|
||When the L3PEN0 bit is reset and the L3SAM0 bit is set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with the IP Source Address field in the IPv4 packets.|



# 75.7.202 (MAC_Layer3_Addr1_Reg6) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr1_Re<br>g6|A34h|



## Function 

For IPv4 packets, the Layer 3 Address 1 Register 0 register contains the 32-bit IP Destination Address field. For IPv6 packets, it contains Bits[63:32] of the 128-bit IP Source Address or Destination Address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3|A16||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3|A16||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3840 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0<br>L3A16|Layer 3 Address 1 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0<br>register, this field contains the value to be matched with Bits[63:32] of the IP Source Address field in the<br>IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with Bits[63:32] of the IP Destination Address field in the IPv6 packets.|
||When the L3PEN0 bit is reset and the L3SAM0 bit is set in the MAC_L3_L4_Control0 register, this field<br>contains the value to be matched with the IP Destination Address field in the IPv4 packets.|



# 75.7.203 (MAC_Layer3_Addr2_Reg6) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr2_Re<br>g6|A38h|



## Function 

The Layer 3 Address 2 Register 0 register is reserved for IPv4 packets. For IPv6 packets, it contains Bits[95:64] of 128-bit IP Source Address or Destination Address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3|A26||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3|A26||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 2 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0|
|L3A26|register, this field contains the value to be matched with Bits[95:64] of the IP Source Address field in the<br>IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with Bits[95:64] of the IP Destination Address field in the IPv6 packets.|
||When the L3PEN0 bit is reset in the MAC_L3_L4_Control0 register, this field is not used.|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3841 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.204 (MAC_Layer3_Addr3_Reg6) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr3_Re<br>g6|A3Ch|



## Function 

The Layer 3 Address 3 Register 0 register is reserved for IPv4 packets. For IPv6 packets, it contains Bits[127:96] of 128-bit IP Source Address or Destination Address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3|A36||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3|A36||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 3 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0|
|L3A36|register, this field contains the value to be matched with Bits[127:96] of the IP Source Address field in|
||the IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this|
||field contains the value to be matched with Bits[127:96] of the IP Destination Address field in the IPv6|
||packets. When the L3PEN0 bit is reset in the MAC_L3_L4_Control0 register, this field is not used.|



# 75.7.205 (MAC_L3_L4_Control7) 

## Offset 

|Register|Offset|
|---|---|
|MAC_L3_L4_Control7|A50h|



## Function 

The Layer 3 and Layer 4 Control register controls the operations of filter 0 of Layer 3 and Layer 4. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3842 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3843-02.png)


<!-- Start of picture text -->
Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserved_23_2 Reserv<br>R Reserved_31_29  DMCH Reserved_27_y  DMCHN7  2  L4DPI L4DP L4SPI L4SP e... L4PEN<br>EN7  M7  M7  M7  M7  7<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv<br>R L3HDBM7  L3HSBM7  L3DAI L3DA L3SAI L3SA e... L3PEN<br>M7  M7  M7  M7  7<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-29|Reserved.|
|Reserved_31_2<br>9||
|28<br>DMCHEN7|DMA Channel Select Enable When set, this bit enables the selection of the DMA channel number for the<br>packet that is passed by this L3_L4 filter. The DMA channel is indicated by the DMCHN bits. When this<br>bit is reset, the DMA channel is not decided by this filter.<br>0b - DMA Channel Select is disabled<br>1b - DMA Channel Select is enabled|
|27-26|Reserved.|
|Reserved_27_y||
|25-24<br>DMCHN7|DMA Channel Number When DMCHEN is set high, this field selects the DMA Channel number to which<br>the packet passed by this filter is routed. The width of this field depends on the number of the DMA<br>channels present in your configuration.|
|23-22|Reserved.|
|Reserved_23_2<br>2||
|21<br>L4DPIM7|Layer 4 Destination Port Inverse Match Enable When this bit is set, the Layer 4 Destination Port number<br>field is enabled for inverse matching. When this bit is reset, the Layer 4 Destination Port number field is<br>enabled for perfect matching. This bit is valid and applicable only when the L4DPM0 bit is set high.<br>0b - Layer 4 Destination Port Inverse Match is disabled<br>1b - Layer 4 Destination Port Inverse Match is enabled|
|20<br>L4DPM7|Layer 4 Destination Port Match Enable When this bit is set, the Layer 4 Destination Port number field is<br>enabled for matching. When this bit is reset, the MAC ignores the Layer 4 Destination Port number field<br>for matching.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3843 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function<br>0b - Layer 4 Destination Port Match is disabled<br>1b - Layer 4 Destination Port Match is enabled|
|---|---|
|19<br>L4SPIM7|Layer 4 Source Port Inverse Match Enable When this bit is set, the Layer 4 Source Port number field is<br>enabled for inverse matching. When this bit is reset, the Layer 4 Source Port number field is enabled for<br>perfect matching. This bit is valid and applicable only when the L4SPM0 bit is set high.<br>0b - Layer 4 Source Port Inverse Match is disabled<br>1b - Layer 4 Source Port Inverse Match is enabled|
|18<br>L4SPM7|Layer 4 Source Port Match Enable When this bit is set, the Layer 4 Source Port number field is enabled<br>for matching. When this bit is reset, the MAC ignores the Layer 4 Source Port number field for matching.<br>0b - Layer 4 Source Port Match is disabled<br>1b - Layer 4 Source Port Match is enabled|
|17<br>Reserved_17|Reserved.|
|16<br>L4PEN7|Layer 4 Protocol Enable When this bit is set, the Source and Destination Port number fields of UDP<br>packets are used for matching. When this bit is reset, the Source and Destination Port number fields of<br>TCP packets are used for matching. The Layer 4 matching is done only when the L4SPM0 or L4DPM0<br>bit is set.<br>0b - Layer 4 Protocol is disabled<br>1b - Layer 4 Protocol is enabled|
|15-11<br>L3HDBM7|Layer 3 IP DA Higher Bits Match IPv4 Packets: This field contains the number of higher bits of IP<br>Destination Address that are matched in the IPv4 packets. The following list describes the values of<br>this field: - 0: No bits are masked. - 1: LSb[0] is masked - 2: Two LSbs [1:0] are masked - .. - 31: All<br>bits except MSb are masked. IPv6 Packets: Bits[12:11] of this field correspond to Bits[6:5] of L3HSBM0<br>which indicate the number of lower bits of IP Source or Destination Address that are masked in the IPv6<br>packets. The following list describes the concatenated values of the L3HDBM0[1:0] and L3HSBM0 bits:<br>- 0: No bits are masked. - 1: LSb[0] is masked. - 2: Two LSbs [1:0] are masked - .. - 127: All bits except<br>MSb are masked. This field is valid and applicable only when the L3DAM0 or L3SAM0 bit is set.|
|10-6<br>L3HSBM7|Layer 3 IP SA Higher Bits Match IPv4 Packets: This field contains the number of lower bits of IP Source<br>Address that are masked for matching in the IPv4 packets. The following list describes the values of this<br>field: - 0: No bits are masked. - 1: LSb[0] is masked - 2: Two LSbs [1:0] are masked - .. - 31: All bits<br>except MSb are masked. IPv6 Packets: This field contains Bits[4:0] of L3HSBM0. These bits indicate the<br>number of higher bits of IP Source or Destination Address matched in the IPv6 packets. This field is valid<br>and applicable only when the L3DAM0 or L3SAM0 bit is set high.|
|5<br>L3DAIM7|Layer 3 IP DA Inverse Match Enable When this bit is set, the Layer 3 IP Destination Address field is<br>enabled for inverse matching. When this bit is reset, the Layer 3 IP Destination Address field is enabled<br>for perfect matching. This bit is valid and applicable only when the L3DAM0 bit is set high.<br>0b - Layer 3 IP DA Inverse Match is disabled<br>1b - Layer 3 IP DA Inverse Match is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3844 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|4<br>L3DAM7|Layer 3 IP DA Match Enable When this bit is set, the Layer 3 IP Destination Address field is enabled for<br>matching. When this bit is reset, the MAC ignores the Layer 3 IP Destination Address field for matching.<br>Note: When the L3PEN0 bit is set, you should set either this bit or the L3SAM0 bit because either IPv6<br>DA or SA can be checked for filtering.<br>0b - Layer 3 IP DA Match is disabled<br>1b - Layer 3 IP DA Match is enabled|
|3<br>L3SAIM7|Layer 3 IP SA Inverse Match Enable When this bit is set, the Layer 3 IP Source Address field is enabled<br>for inverse matching. When this bit reset, the Layer 3 IP Source Address field is enabled for perfect<br>matching. This bit is valid and applicable only when the L3SAM0 bit is set.<br>0b - Layer 3 IP SA Inverse Match is disabled<br>1b - Layer 3 IP SA Inverse Match is enabled|
|2<br>L3SAM7|Layer 3 IP SA Match Enable When this bit is set, the Layer 3 IP Source Address field is enabled for<br>matching. When this bit is reset, the MAC ignores the Layer 3 IP Source Address field for matching.<br>Note: When the L3PEN0 bit is set, you should set either this bit or the L3DAM0 bit because either IPv6<br>SA or DA can be checked for filtering.<br>0b - Layer 3 IP SA Match is disabled<br>1b - Layer 3 IP SA Match is enabled|
|1<br>Reserved_1|Reserved.|
|0<br>L3PEN7|Layer 3 Protocol Enable When this bit is set, the Layer 3 IP Source or Destination Address matching is<br>enabled for IPv6 packets. When this bit is reset, the Layer 3 IP Source or Destination Address matching<br>is enabled for IPv4 packets. The Layer 3 matching is done only when the L3SAM0 or L3DAM0 bit is set.<br>0b - Layer 3 Protocol is disabled<br>1b - Layer 3 Protocol is enabled|



# 75.7.206 (MAC_Layer4_Address7) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer4_Address7|A54h|



## Function 

The MAC_Layer4_Address(#i), MAC_L3_L4_Control(#i), MAC_Layer3_Addr0_Reg(#i), MAC_Layer3_Addr1_Reg(#i), MAC_Layer3_Addr2_Reg(#i) and MAC_Layer3_Addr3_Reg(#i) registers are reserved (RO with default value) if Enable Layer 3 and Layer 4 Packet Filter option is not selected while configuring the IP. You can configure the Layer 3 and Layer 4 Address Registers to be double-synchronized by selecting the Synchronize Layer 3 and Layer 4 Address Registers to Rx Clock Domain option while configuring the IP. When you select this option, the synchronization is triggered only when Bits[31:24] (in little-endian mode) or Bits[7:0] (in big-endian mode) of the Layer 3 and Layer 4 Address Registers are written. For proper 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3845 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

synchronization updates, you should perform consecutive writes to same Layer 3 and Layer 4 Address Registers after at least four clock cycles delay of the destination clock. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3846-04.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>L4DP7<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>L4SP7<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-16<br>L4DP7|Layer 4 Destination Port Number Field When the L4PEN0 bit is reset and the L4DPM0 bit is set in the<br>MAC_L3_L4_Control0 register, this field contains the value to be matched with the TCP Destination<br>Port Number field in the IPv4 or IPv6 packets. When the L4PEN0 and L4DPM0 bits are set in<br>MAC_L3_L4_Control0 register, this field contains the value to be matched with the UDP Destination<br>Port Number field in the IPv4 or IPv6 packets.|
|15-0<br>L4SP7|Layer 4 Source Port Number Field When the L4PEN0 bit is reset and the L4SPM0 bit is set in<br>the MAC_L3_L4_Control0 register, this field contains the value to be matched with the TCP Source<br>Port Number field in the IPv4 or IPv6 packets. When the L4PEN0 and L4SPM0 bits are set in<br>MAC_L3_L4_Control0 register, this field contains the value to be matched with the UDP Source Port<br>Number field in the IPv4 or IPv6 packets.|



# 75.7.207 (MAC_Layer3_Addr0_Reg7) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr0_Re<br>g7|A60h|



## Function 

For IPv4 packets, the Layer 3 Address 0 Register 0 register contains the 32-bit IP Source Address field. For IPv6 packets, it contains Bits[31:0] of the 128-bit IP Source Address or Destination Address field. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3846 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3847-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>L3A07<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>L3A07<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0<br>L3A07|Layer 3 Address 0 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0<br>register, this field contains the value to be matched with Bits[31:0] of the IP Source Address field in the<br>IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with Bits[31:0] of the IP Destination Address field in the IPv6 packets.|
||When the L3PEN0 bit is reset and the L3SAM0 bit is set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with the IP Source Address field in the IPv4 packets.|



# 75.7.208 (MAC_Layer3_Addr1_Reg7) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr1_Re<br>g7|A64h|



## Function 

For IPv4 packets, the Layer 3 Address 1 Register 0 register contains the 32-bit IP Destination Address field. For IPv6 packets, it contains Bits[63:32] of the 128-bit IP Source Address or Destination Address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3|A17||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3|A17||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3847 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0<br>L3A17|Layer 3 Address 1 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0<br>register, this field contains the value to be matched with Bits[63:32] of the IP Source Address field in the<br>IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with Bits[63:32] of the IP Destination Address field in the IPv6 packets.|
||When the L3PEN0 bit is reset and the L3SAM0 bit is set in the MAC_L3_L4_Control0 register, this field<br>contains the value to be matched with the IP Destination Address field in the IPv4 packets.|



# 75.7.209 (MAC_Layer3_Addr2_Reg7) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr2_Re<br>g7|A68h|



## Function 

The Layer 3 Address 2 Register 0 register is reserved for IPv4 packets. For IPv6 packets, it contains Bits[95:64] of 128-bit IP Source Address or Destination Address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3|A27||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3|A27||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 2 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0|
|L3A27|register, this field contains the value to be matched with Bits[95:64] of the IP Source Address field in the<br>IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this field|
||contains the value to be matched with Bits[95:64] of the IP Destination Address field in the IPv6 packets.|
||When the L3PEN0 bit is reset in the MAC_L3_L4_Control0 register, this field is not used.|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3848 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.210 (MAC_Layer3_Addr3_Reg7) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr3_Re<br>g7|A6Ch|



## Function 

The Layer 3 Address 3 Register 0 register is reserved for IPv4 packets. For IPv6 packets, it contains Bits[127:96] of 128-bit IP Source Address or Destination Address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3|A37||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3|A37||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 3 Field When the L3PEN0 and L3SAM0 bits are set in the MAC_L3_L4_Control0|
|L3A37|register, this field contains the value to be matched with Bits[127:96] of the IP Source Address field in|
||the IPv6 packets. When the L3PEN0 and L3DAM0 bits are set in the MAC_L3_L4_Control0 register, this|
||field contains the value to be matched with Bits[127:96] of the IP Destination Address field in the IPv6|
||packets. When the L3PEN0 bit is reset in the MAC_L3_L4_Control0 register, this field is not used.|



# 75.7.211 (MAC_Indir_Access_Ctrl) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Indir_Access_Ctrl|A70h|



## Function 

This register provides the Indirect Access control and status for MAC_<MSEl>_<AOFF> registers. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3849 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||Reserve|d_31_20|||||||M|SEL||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||AO|FF||||Reserve|d_7_6|AUTO|Res|erved_4|_2|COM|OB|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-20|Reserved.|
|Reserved_31_2<br>0||
|19-16<br>MSEL|Mode Select This field is used in indirect access of MAC_<MSEL>_<AOFF>. This field must be set along<br>with initiation of read/write to MAC_<MSEL>_<AOFF> and should not be changed until the OB is reset.<br>Values: - 0000:Typ_RXQ_ (Type based RXQ mappping) - 0001-1111: Reserved for future use.|
|15-8<br>AOFF|Address Offset This field is used in indirect access of MAC_<MSEL>_<AOFF>. This field must be set<br>along with initiation of read/write to MAC_<MSEL>_<AOFF> and should not be changed until the OB is<br>reset. Values: - 00000000: IndReg0(Indirect register 0) - 00000001: IndReg1(Indirect register 1) - ... -<br>00000111: IndReg7(Indirect register 7) - 00001000-11111111: Reserved for future use.|
|7-6|Reserved.|
|Reserved_7_6||
|5<br>AUTO|Auto increment - 1: AOFF is incremented by 1. Software should ensure not to cause a wrap condition.<br>Byte wise read/write is not supported when auto increment is enabled. - 0: AOFF is not incremented<br>automatically. Software should program the correct Address Offset for each access.|
|4-2<br>Reserved_4_2|Reserved.|
|1<br>COM|Command type This bit indicates the register access type. - 1: Indicates a read operation. - 0: Indicates a<br>write operation.<br>0b - Write operation<br>1b - Read operation|
|0<br>OB|Operation Busy. This bit is set along with a read or write command for initiating the indirect<br>access to MAC_<MSEL>_<AOFF> register. This bit is reset when the read or write command to<br>MAC_<MSEL>_<AOFF> register is complete. The next indirect register access can be initiated only<br>after this bit is reset. During a write operation, the bit is reset only after the data has been<br>written into MAC_<MSEL>_<AOFF> register. During a read operation, the data should be read from<br>MAC_Indir_Access_Data register only after this bit is reset.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3850 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.212 (MAC_Indir_Access_Data) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Indir_Access_Data|A74h|



## Function 

This register holds the read/write data for Indirect Access of MAC_<MSEL_<AOFF> registers. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3851-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>DATA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>DATA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|This field contains data to read/write for Indirect address access associated with MAC_Indir_Access_Ctrl|
|DATA|register.|



# 75.7.213 (MAC_TMRQ_Regs0) 

## Offset 

|Register|Offset|
|---|---|
|MAC_TMRQ_Regs0|A74h|



## Function 

This register contains the type, associated queue number and paket type (Pre emption/EXpress) related to Type based RXQ mapping. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3851 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||Res|erved_31|_21|||||PFEX|Reserv<br>e...||TMRQ||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||T|YP||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-21|Reserved.|
|Reserved_31_2<br>1||
|20|Preemption or Express Packet This bit indicates if it is a preemption packet or express packet.|
|PFEX||
|19|Reserved.|
|Reserved_19||
|18-16<br>TMRQ|Type Match Rx Queue Number Indicates the receive queue number to which the packet needs to be<br>forwarded on detecting a type match.|
|15-0<br>TYP|Type field Value Indicates the type value of packet that needs to be compared with received Ethernet<br>packet. This field is valid when programmed to a value greater than or equal to 0x0600.|



# 75.7.214 (MAC_TMRQ_Regs1) 

## Offset 

|Register|Offset|
|---|---|
|MAC_TMRQ_Regs1|A74h|



## Function 

This register contains the type, associated queue number and paket type (Pre emption/EXpress) related to Type based RXQ mapping. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3852 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||Res|erved_31|_21|||||PFEX|Reserv<br>e...||TMRQ||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||T|YP||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-21|Reserved.|
|Reserved_31_2<br>1||
|20|Preemption or Express Packet This bit indicates if it is a preemption packet or express packet.|
|PFEX||
|19|Reserved.|
|Reserved_19||
|18-16<br>TMRQ|Type Match Rx Queue Number Indicates the receive queue number to which the packet needs to be<br>forwarded on detecting a type match.|
|15-0<br>TYP|Type field Value Indicates the type value of packet that needs to be compared with received Ethernet<br>packet. This field is valid when programmed to a value greater than or equal to 0x0600.|



# 75.7.215 (MAC_TMRQ_Regs2) 

## Offset 

|Register|Offset|
|---|---|
|MAC_TMRQ_Regs2|A74h|



## Function 

This register contains the type, associated queue number and paket type (Pre emption/EXpress) related to Type based RXQ mapping. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3853 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||Res|erved_31|_21|||||PFEX|Reserv<br>e...||TMRQ||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||T|YP||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-21|Reserved.|
|Reserved_31_2<br>1||
|20|Preemption or Express Packet This bit indicates if it is a preemption packet or express packet.|
|PFEX||
|19|Reserved.|
|Reserved_19||
|18-16<br>TMRQ|Type Match Rx Queue Number Indicates the receive queue number to which the packet needs to be<br>forwarded on detecting a type match.|
|15-0<br>TYP|Type field Value Indicates the type value of packet that needs to be compared with received Ethernet<br>packet. This field is valid when programmed to a value greater than or equal to 0x0600.|



# 75.7.216 (MAC_TMRQ_Regs3) 

## Offset 

|Register|Offset|
|---|---|
|MAC_TMRQ_Regs3|A74h|



## Function 

This register contains the type, associated queue number and paket type (Pre emption/EXpress) related to Type based RXQ mapping. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3854 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||Res|erved_31|_21|||||PFEX|Reserv<br>e...||TMRQ||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||T|YP||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-21|Reserved.|
|Reserved_31_2<br>1||
|20|Preemption or Express Packet This bit indicates if it is a preemption packet or express packet.|
|PFEX||
|19|Reserved.|
|Reserved_19||
|18-16<br>TMRQ|Type Match Rx Queue Number Indicates the receive queue number to which the packet needs to be<br>forwarded on detecting a type match.|
|15-0<br>TYP|Type field Value Indicates the type value of packet that needs to be compared with received Ethernet<br>packet. This field is valid when programmed to a value greater than or equal to 0x0600.|



# 75.7.217 (MAC_TMRQ_Regs4) 

## Offset 

|Register|Offset|
|---|---|
|MAC_TMRQ_Regs4|A74h|



## Function 

This register contains the type, associated queue number and paket type (Pre emption/EXpress) related to Type based RXQ mapping. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3855 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||Res|erved_31|_21|||||PFEX|Reserv<br>e...||TMRQ||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||T|YP||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-21|Reserved.|
|Reserved_31_2<br>1||
|20|Preemption or Express Packet This bit indicates if it is a preemption packet or express packet.|
|PFEX||
|19|Reserved.|
|Reserved_19||
|18-16<br>TMRQ|Type Match Rx Queue Number Indicates the receive queue number to which the packet needs to be<br>forwarded on detecting a type match.|
|15-0<br>TYP|Type field Value Indicates the type value of packet that needs to be compared with received Ethernet<br>packet. This field is valid when programmed to a value greater than or equal to 0x0600.|



# 75.7.218 (MAC_TMRQ_Regs5) 

## Offset 

|Register|Offset|
|---|---|
|MAC_TMRQ_Regs5|A74h|



## Function 

This register contains the type, associated queue number and paket type (Pre emption/EXpress) related to Type based RXQ mapping. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3856 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3857-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R Reserved_31_21<br>PFEX  e... TMRQ<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>TYP<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-21|Reserved.|
|Reserved_31_2<br>1||
|20|Preemption or Express Packet This bit indicates if it is a preemption packet or express packet.|
|PFEX||
|19|Reserved.|
|Reserved_19||
|18-16<br>TMRQ|Type Match Rx Queue Number Indicates the receive queue number to which the packet needs to be<br>forwarded on detecting a type match.|
|15-0<br>TYP|Type field Value Indicates the type value of packet that needs to be compared with received Ethernet<br>packet. This field is valid when programmed to a value greater than or equal to 0x0600.|



# 75.7.219 (MAC_TMRQ_Regs6) 

## Offset 

|Register|Offset|
|---|---|
|MAC_TMRQ_Regs6|A74h|



## Function 

This register contains the type, associated queue number and paket type (Pre emption/EXpress) related to Type based RXQ mapping. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3857 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||Res|erved_31|_21|||||PFEX|Reserv<br>e...||TMRQ||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||T|YP||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-21|Reserved.|
|Reserved_31_2<br>1||
|20|Preemption or Express Packet This bit indicates if it is a preemption packet or express packet.|
|PFEX||
|19|Reserved.|
|Reserved_19||
|18-16<br>TMRQ|Type Match Rx Queue Number Indicates the receive queue number to which the packet needs to be<br>forwarded on detecting a type match.|
|15-0<br>TYP|Type field Value Indicates the type value of packet that needs to be compared with received Ethernet<br>packet. This field is valid when programmed to a value greater than or equal to 0x0600.|



# 75.7.220 (MAC_TMRQ_Regs7) 

## Offset 

|Register|Offset|
|---|---|
|MAC_TMRQ_Regs7|A74h|



## Function 

This register contains the type, associated queue number and paket type (Pre emption/EXpress) related to Type based RXQ mapping. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3858 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||Res|erved_31|_21|||||PFEX|Reserv<br>e...||TMRQ||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||T|YP||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-21|Reserved.|
|Reserved_31_2<br>1||
|20|Preemption or Express Packet This bit indicates if it is a preemption packet or express packet.|
|PFEX||
|19|Reserved.|
|Reserved_19||
|18-16<br>TMRQ|Type Match Rx Queue Number Indicates the receive queue number to which the packet needs to be<br>forwarded on detecting a type match.|
|15-0<br>TYP|Type field Value Indicates the type value of packet that needs to be compared with received Ethernet<br>packet. This field is valid when programmed to a value greater than or equal to 0x0600.|



# 75.7.221 (MAC_Timestamp_Control) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Timestamp_Contro|B00h|
|l||



## Function 

This register controls the operation of the System Time generator and processing of PTP packets for timestamping in the Receiver. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3859 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3860-02.png)


<!-- Start of picture text -->
Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R Reserved_31_29  AV802 Reserved_27_25  TXTSS Reserved_23_21  ESTI  e... TSEN SNAPTYPSEL<br>1A... TSM  MAC...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv Reserv<br>R TSMS TSEV TSIPV TSIPV TSIPE TSVE TSCT TSEN e... PTGE  TSAD e... TSUP TSINIT  TSCF TSEN<br>TRE... NTE... 4E... 6E... NA  R2E... RLS... ALL  DREG  DT  UPDT  A<br>W<br>Reset 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-29|Reserved.|
|Reserved_31_2<br>9||
|28<br>AV8021ASMEN|AV 802.1AS Mode Enable When this bit is set, the MAC processes only untagged PTP over Ethernet<br>packets for providing PTP status and capturing timestamp snapshots, that is, IEEE 802.1AS mode of<br>operation. When PTP offload feature is enabled, for the purpose of PTP offload, the transport specific<br>field in the PTP header is generated and checked based on the value of this bit.<br>0b - AV 802.1AS Mode is disabled<br>1b - AV 802.1AS Mode is enabled|
|27-25<br>Reserved_27_2<br>5|Reserved.|
|24<br>TXTSSTSM|Transmit Timestamp Status Mode When this bit is set, the MAC overwrites the earlier transmit timestamp<br>status even if it is not read by the software. The MAC indicates this by setting the TXTSSMIS bit of<br>the MAC_Tx_Timestamp_Status_Nanoseconds register. When this bit is reset, the MAC ignores the<br>timestamp status of current packet if the timestamp status of previous packet is not read by the software.<br>The MAC indicates this by setting the TXTSSMIS bit of the MAC_Tx_Timestamp_Status_Nanoseconds<br>register.<br>0b - Transmit Timestamp Status Mode is disabled<br>1b - Transmit Timestamp Status Mode is enabled|
|23-21<br>Reserved_23_2<br>1|Reserved.|
|20|External System Time Input When this bit is set, the MAC uses the external 64-bit reference System<br>Time input for the following: - To take the timestamp provided as status - To insert the timestamp in|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3860 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|ESTI|transmit PTP packets when One-step Timestamp or Timestamp Offload feature is enabled. When this bit<br>is reset, the MAC uses the internal reference System Time.<br>0b - External System Time Input is disabled<br>1b - External System Time Input is enabled|
|19|Reserved.|
|Reserved_CSC||
|18<br>TSENMACADD<br>R|Enable MAC Address for PTP Packet Filtering When this bit is set, the DA MAC address (that matches<br>any MAC Address register) is used to filter the PTP packets when PTP is directly sent over Ethernet.<br>When this bit is set, received PTP packets with DA containing a special multicast or unicast address<br>that matches the one programmed in MAC address registers are considered for processing as indicated,<br>when PTP is directly sent over Ethernet. For normal time stamping operation, MAC address registers<br>0 to 31 is considered for unicast destination address matching. For PTP offload, only MAC address<br>register 0 is considered for unicast destination address matching.<br>0b - MAC Address for PTP Packet Filtering is disabled<br>1b - MAC Address for PTP Packet Filtering is enabled|
|17-16<br>SNAPTYPSEL|Select PTP packets for Taking Snapshots These bits, along with Bits 15 and 14, decide the set of PTP<br>packet types for which snapshot needs to be taken. The encoding is given in Timestamp Snapshot<br>Dependency on Register Bits Table.|
|15<br>TSMSTRENA|Enable Snapshot for Messages Relevant to Master When this bit is set, the snapshot is taken only for<br>the messages that are relevant to the master node. Otherwise, the snapshot is taken for the messages<br>relevant to the slave node.<br>0b - Snapshot for Messages Relevant to Master is disabled<br>1b - Snapshot for Messages Relevant to Master is enabled|
|14<br>TSEVNTENA|Enable Timestamp Snapshot for Event Messages When this bit is set, the timestamp snapshot is taken<br>only for event messages (SYNC, Delay_Req, Pdelay_Req, or Pdelay_Resp). When this bit is reset, the<br>snapshot is taken for all messages except Announce, Management, and Signaling. For more information<br>about the timestamp snapshots, see Timestamp Snapshot Dependency on Register Bits Table.<br>0b - Timestamp Snapshot for Event Messages is disabled<br>1b - Timestamp Snapshot for Event Messages is enabled|
|13<br>TSIPV4ENA|Enable Processing of PTP Packets Sent over IPv4-UDP When this bit is set, the MAC receiver<br>processes the PTP packets encapsulated in IPv4-UDP packets. When this bit is reset, the MAC ignores<br>the PTP transported over IPv4-UDP packets. This bit is set by default.<br>0b - Processing of PTP Packets Sent over IPv4-UDP is disabled<br>1b - Processing of PTP Packets Sent over IPv4-UDP is enabled|
|12<br>TSIPV6ENA|Enable Processing of PTP Packets Sent over IPv6-UDP When this bit is set, the MAC receiver<br>processes the PTP packets encapsulated in IPv6-UDP packets. When this bit is clear, the MAC ignores<br>the PTP transported over IPv6-UDP packets.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3861 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function<br>0b - Processing of PTP Packets Sent over IPv6-UDP is disabled<br>1b - Processing of PTP Packets Sent over IPv6-UDP is enabled|
|---|---|
|11<br>TSIPENA|Enable Processing of PTP over Ethernet Packets When this bit is set, the MAC receiver processes the<br>PTP packets encapsulated directly in the Ethernet packets. When this bit is reset, the MAC ignores the<br>PTP over Ethernet packets.<br>0b - Processing of PTP over Ethernet Packets is disabled<br>1b - Processing of PTP over Ethernet Packets is enabled|
|10<br>TSVER2ENA|Enable PTP Packet Processing for Version 2 Format When this bit is set, the IEEE 1588 version 2 format<br>is used to process the PTP packets. When this bit is reset, the IEEE 1588 version 1 format is used to<br>process the PTP packets. The IEEE 1588 formats are described in 'PTP Processing and Control'.<br>0b - PTP Packet Processing for Version 2 Format is disabled<br>1b - PTP Packet Processing for Version 2 Format is enabled|
|9<br>TSCTRLSSR|Timestamp Digital or Binary Rollover Control When this bit is set, the Timestamp Low register rolls<br>over after 0x3B9A_C9FF value (that is, 1 nanosecond accuracy) and increments the timestamp (High)<br>seconds. When this bit is reset, the rollover value of sub-second register is 0x7FFF_FFFF. The sub-<br>second increment must be programmed correctly depending on the PTP reference clock frequency and<br>the value of this bit.<br>0b - Timestamp Digital or Binary Rollover Control is disabled<br>1b - Timestamp Digital or Binary Rollover Control is enabled|
|8<br>TSENALL|Enable Timestamp for All Packets When this bit is set, the timestamp snapshot is enabled for all packets<br>received by the MAC.<br>0b - Timestamp for All Packets disabled<br>1b - Timestamp for All Packets enabled|
|7<br>Reserved_7|Reserved.|
|6<br>PTGE|Presentation Time Generation Enable When this bit is set the Presentation Time generation is enabled.<br>0b - Presentation Time Generation is disabled<br>1b - Presentation Time Generation is enabled|
|5<br>TSADDREG|Update Addend Register When this bit is set, the content of the Timestamp Addend register is updated in<br>the PTP block for fine correction. This bit is cleared when the update is complete. This bit should be zero<br>before it is set. Access restriction applies. Setting 1 sets. Self-cleared. Setting 0 has no effect.<br>0b - Addend Register is not updated<br>1b - Addend Register is updated|
|4|Reserved.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3862 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|Reserved_TST<br>RIG||
|3<br>TSUPDT|Update Timestamp When this bit is set, the system time is updated (added or subtracted) with the<br>value specified in MAC_System_Time_Seconds_Update and MAC_System_Time_Nanoseconds_Update<br>registers. This bit should be zero before updating it. This bit is reset when the update is complete in<br>hardware. The Timestamp Higher Word register (if enabled while configuring the IP) is not updated.<br>When Media Clock Generation and Recovery is configured (DWC_EQOS_FLEXI_PPS_OUT_EN) and<br>enabled MAC_Presn_Time_Updt should also be updated before setting this field. Access restriction<br>applies. Setting 1 sets. Self-cleared. Setting 0 has no effect.<br>0b - Timestamp is not updated<br>1b - Timestamp is updated|
|2<br>TSINIT|Initialize Timestamp When this bit is set, the system time is initialized (overwritten) with the value<br>specified in the MAC_System_Time_Seconds_Update and MAC_System_Time_Nanoseconds_Update<br>registers. This bit should be zero before it is updated. This bit is reset when the initialization is complete.<br>The Timestamp Higher Word register (if enabled while configuration the IP) can only be initialized. When<br>Media Clock Generation and Recovery is configured (DWC_EQOS_FLEXI_PPS_OUT_EN) and enabled<br>MAC_Presn_Time_Updt should also be updated before setting this field. Access restriction applies.<br>Setting 1 sets. Self-cleared. Setting 0 has no effect.<br>0b - Timestamp is not initialized<br>1b - Timestamp is initialized|
|1<br>TSCFUPDT|Fine or Coarse Timestamp Update When this bit is set, the Fine method is used to update system<br>timestamp. When this bit is reset, Coarse method is used to update the system timestamp.<br>0b - Coarse method is used to update system timestamp<br>1b - Fine method is used to update system timestamp|
|0<br>TSENA|Enable Timestamp When this bit is set, the timestamp is added for Transmit and Receive packets. When<br>disabled, timestamp is not added for transmit and receive packets and the Timestamp Generator is also<br>suspended. You need to initialize the Timestamp (system time) after enabling this mode. On the Receive<br>side, the MAC processes the 1588 packets only if this bit is set.<br>0b - Timestamp is disabled<br>1b - Timestamp is enabled|



# 75.7.222 (MAC_Sub_Second_Increment) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Sub_Second_Incre|B04h|
|ment||



## Function 

This register specifies the value to be added to the internal system time register every cycle of clk_ptp_ref_i clock. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3863 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||Reserve|d_31_24|||||||SSI|NC||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||SNS|INC|||||||Reserv|ed_7_0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-24|Reserved.|
|Reserved_31_2<br>4||
|23-16<br>SSINC|Sub-second Increment Value The value programmed in this field is accumulated every clock cycle (of<br>clk_ptp_i) with the contents of the sub-second register. For example, when the PTP clock is 50 MHz<br>(period is 20 ns), you should program 20 (0x14) when the System Time Nanoseconds register has an<br>accuracy of 1 ns [Bit 9 (TSCTRLSSR) is set in MAC_Timestamp_Control]. When TSCTRLSSR is clear,<br>the Nanoseconds register has a resolution of ~0.465 ns. In this case, you should program a value of 43<br>(0x2B) which is derived by 20 ns/0.465.|
|15-8<br>SNSINC|Sub-nanosecond Increment Value This field contains the sub-nanosecond increment value, represented<br>in nanoseconds multiplied by 2^8. This value is accumulated with the sub-nanoseconds field of the<br>subsecond register. For example, when TSCTRLSSR field in the MAC_Timestamp_Control register is<br>set. and if the required increment is 5.3ns, then SSINC should be 0x05 and SNSINC should be 0x4C.|
|7-0|Reserved.|
|Reserved_7_0||



# 75.7.223 (MAC_System_Time_Seconds) 

## Offset 

|Register|Offset|
|---|---|
|MAC_System_Time_Sec<br>onds|B08h|



## Function 

The System Time Seconds register, along with System Time Nanoseconds register, indicates the current value of the system time maintained by the MAC. Though it is updated on a continuous basis, there is some delay from the actual time because of clock domain transfer latencies (from clk_ptp_ref_i to CSR clock). 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3864 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3865-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TSS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TSS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0<br>TSS|Timestamp Second The value in this field indicates the current value in seconds of the System Time<br>maintained by the MAC.|



# 75.7.224 (MAC_System_Time_Nanoseconds) 

## Offset 

|Register|Offset|
|---|---|
|MAC_System_Time_Nan<br>oseconds|B0Ch|



## Function 

The System Time Nanoseconds register, along with System Time Seconds register, indicates the current value of the system time maintained by the MAC. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3865-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R TSSS<br>e...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TSSS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3865 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31|Reserved.|
|Reserved_31||
|30-0|Timestamp Sub Seconds The value in this field has the sub-second representation of time, with an|
|TSSS|accuracy of 0.46 ns. When Bit 9 is set in MAC_Timestamp_Control, each bit represents 1 ns. The<br>maximum value is 0x3B9A_C9FF after which it rolls-over to zero.|



# 75.7.225 (MAC_System_Time_Seconds_Update) 

## Offset 

|Register|Offset|
|---|---|
|MAC_System_Time_Sec<br>onds_Update|B10h|



## Function 

The System Time Seconds Update register, along with the System Time Nanoseconds Update register, initializes or updates the system time maintained by the MAC. You must write both registers before setting the TSINIT or TSUPDT bits in DWC_eqos_top_map/EQOS_MAC/MAC_Timestamp_Control. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||TS|S||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||TS|S||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function|
|---|---|
|31-0|Timestamp Seconds The value in this field is the seconds part of the update. When ADDSUB is|
||reset, this field must be programmed with the seconds part of the update value. When ADDSUB|
|TSS|is set, this field must be programmed with the complement of the seconds part of the update|
||value. For example, to subtract 2.000000001 seconds from the system time, the TSS field in the|
||MAC_Timestamp_Seconds_Update register must be 0xFFFF_FFFE (that is, 2^32 - 2).|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3866 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.226 (MAC_System_Time_Nanoseconds_Update) 

## Offset 

|Register|Offset|
|---|---|
|MAC_System_Time_Nan|B14h|
|oseconds_Update||



## Function 

MAC System Time Nanoseconds Update register. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3867-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R ADDS<br>TSSS<br>W UB<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>TSSS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31<br>ADDSUB|Add or Subtract Time When this bit is set, the time value is subtracted with the contents of the update<br>register. When this bit is reset, the time value is added with the contents of the update register.<br>0b - Add time<br>1b - Subtract time|
|30-0<br>TSSS|Timestamp Sub Seconds The value in this field is the sub-seconds part of the update. - ADDSUB<br>is 1: This field must be programmed with the complement of the sub-seconds part of the update<br>value as described. - ADDSUB is 0: This field must be programmed with the sub-seconds part of<br>the update value, with an accuracy based on the TSCTRLSSR bit of the MAC_Timestamp_Control<br>register. - TSCTRLSSR field in the MAC_Timestamp_Control register is 1: -- The programmed value<br>must be 10^9 - <sub-second value>. -- Each bit represents 1 ns and the programmed value should<br>not exceed 0x3B9A_C9FF. - TSCTRLSSR field in the MAC_Timestamp_Control register is 0: -- The<br>programmed value must be 2^31 - <sub-second_value>. -- Each bit represents an accuracy of 0.46<br>ns. For example, to subtract 2.000000001 seconds from the system time, then the TSSS field in<br>the MAC_Timestamp_Nanoseconds_Update register must be 0x7FFF_FFFF (that is, 2^31 - 1), when<br>TSCTRLSSR bit in MAC_Timestamp_Control is reset and 0x3B9A_C9FF (that is, 10^9 - 1), when<br>TSCTRLSSR bit in MAC_Timestamp_Control is set.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3867 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.227 (MAC_Timestamp_Addend) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Timestamp_Adden<br>d|B18h|



## Function 

Timestamp Addend register. This register value is used only when the system time is configured for Fine Update mode (TSCFUPDT bit in the MAC_Timestamp_Control register). The content of this register is added to a 32-bit accumulator in every clock cycle (of clk_ptp_ref_i) and the system time is updated when the accumulator overflows. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3868-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>TSAR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>TSAR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Timestamp Addend Register This field indicates the 32-bit time value to be added to the Accumulator|
|TSAR|register to achieve time synchronization.|



# 75.7.228 (MAC_System_Time_Higher_Word_Seconds) 

## Offset 

|Register|Offset|
|---|---|
|MAC_System_Time_Hig|B1Ch|
|her_Word_Seconds||



## Function 

System Time - Higher Word Seconds register. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3868 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3869-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_16<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>TSHWR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-16|Reserved.|
|Reserved_31_1<br>6||
|15-0<br>TSHWR|Timestamp Higher Word Register This field contains the most-significant 16-bits of timestamp seconds<br>value. This register is optional. You can add this register by selecting the Add IEEE 1588 Higher Word<br>Register option. This register is directly written to initialize the value and it is incremented when there<br>is an overflow from 32-bits of the System Time Seconds register. Access restriction applies. Updated<br>based on the event. Setting 1 sets. Setting 0 clears.|



# 75.7.229 (MAC_Timestamp_Status) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Timestamp_Status|B20h|



## Function 

Timestamp Status register. All bits except Bits[27:25] gets cleared when the application reads this register. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3869 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part2/S32K3XXRM_数据表.pdf-3870-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserved_31_3 Reserv<br>R Reserved_ATSNS  Reserved_23_20  Reserved_ATSSTN<br>0  e...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>TXTSS TSTR TSTA TSTR TSTA TSTR TSTA TSTR Reserv TSTA TSSO<br>R Reserved_14_10<br>IS  GTE... RGT3  GTE... RGT2  GTE... RGT1  GTE... e... RGT0  VF<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-30|Reserved.|
|Reserved_31_3<br>0||
|29-25|Reserved.|
|Reserved_ATS<br>NS||
|24|Reserved.|
|Reserved_ATS<br>STM||
|23-20|Reserved.|
|Reserved_23_2<br>0||
|19-16|Reserved.|
|Reserved_ATS<br>STN||
|15<br>TXTSSIS|Tx Timestamp Status Interrupt Status In non-EQOS_CORE configurations when drop transmit status<br>is enabled in MTL, this bit is set when the captured transmit timestamp is updated in the<br>MAC_Tx_Timestamp_Status_Nanoseconds and MAC_Tx_Timestamp_Status_Seconds registers. When<br>PTP offload feature is enabled, this bit is set when the captured transmit timestamp is updated<br>in the MAC_Tx_Timestamp_Status_Nanoseconds and MAC_Tx_Timestamp_Status_Seconds registers,<br>for PTO generated Delay Request and Pdelay request packets. This bit is cleared when the<br>MAC_Tx_Timestamp_Status_Seconds register is read (or write to MAC_Tx_Timestamp_Status_Seconds<br>register when RCWE bit of MAC_CSR_SW_Ctrl register is set).<br>0b - Tx Timestamp Status Interrupt status not detected<br>1b - Tx Timestamp Status Interrupt status detected|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3870 / 4640 

