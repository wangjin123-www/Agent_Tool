NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field<br>14-10<br>Reserved_14_1<br>0|Function<br>Reserved.|
|---|---|
|9<br>TSTRGTERR3|Timestamp Target Time Error This bit is set when the latest target time programmed in the<br>MAC_PPS3_Target_Time_Seconds and MAC_PPS3_Target_Time_Nanoseconds registers elapses. This<br>bit is cleared when the application reads this bit. Access restriction applies. Clears on read (or this bit is<br>written to 1 when RCWE bit in MAC_CSR_SW_Ctrl register is set). Self-set to 1 on internal event.<br>0b - Timestamp Target Time Error status not detected<br>1b - Timestamp Target Time Error status detected|
|8<br>TSTARGT3|Timestamp Target Time Reached for Target Time PPS3 When this bit is set and<br>MCGREN3 of MAC_PPS_Control register is reset, it indicates that the value of system<br>time is greater than or equal to the value specified in the MAC_PPS3_Target_Time_Seconds<br>and MAC_PPS3_Target_Time_Nanoseconds registers. When this bit is set and MCGREN3 of<br>MAC_PPS_Control register is set, it indicates that mcgr_dma_req_o[3] is asserted. Access restriction<br>applies. Clears on read (or this bit is written to 1 when RCWE bit in MAC_CSR_SW_Ctrl register is set).<br>Self-set to 1 on internal event.<br>0b - Timestamp Target Time Reached for Target Time PPS3 status not detected<br>1b - Timestamp Target Time Reached for Target Time PPS3 status detected|
|7<br>TSTRGTERR2|Timestamp Target Time Error This bit is set when the latest target time programmed in the<br>MAC_PPS2_Target_Time_Seconds and MAC_PPS2_Target_Time_Nanoseconds registers elapses. This<br>bit is cleared when the application reads this bit. Access restriction applies. Clears on read (or this bit is<br>written to 1 when RCWE bit in MAC_CSR_SW_Ctrl register is set). Self-set to 1 on internal event.<br>0b - Timestamp Target Time Error status not detected<br>1b - Timestamp Target Time Error status detected|
|6<br>TSTARGT2|Timestamp Target Time Reached for Target Time PPS2 When this bit is set and<br>MCGREN2 of MAC_PPS_Control register is reset, it indicates that the value of system<br>time is greater than or equal to the value specified in the MAC_PPS2_Target_Time_Seconds<br>and MAC_PPS2_Target_Time_Nanoseconds registers. When this bit is set and MCGREN2 of<br>MAC_PPS_Control register is set, it indicates that mcgr_dma_req_o[2] is asserted. Access restriction<br>applies. Clears on read (or this bit is written to 1 when RCWE bit in MAC_CSR_SW_Ctrl register is set).<br>Self-set to 1 on internal event.<br>0b - Timestamp Target Time Reached for Target Time PPS2 status not detected<br>1b - Timestamp Target Time Reached for Target Time PPS2 status detected|
|5<br>TSTRGTERR1|Timestamp Target Time Error This bit is set when the latest target time programmed in the<br>MAC_PPS1_Target_Time_Seconds and MAC_PPS1_Target_Time_Nanoseconds registers elapses. This<br>bit is cleared when the application reads this bit. Access restriction applies. Clears on read (or this bit is<br>written to 1 when RCWE bit in MAC_CSR_SW_Ctrl register is set). Self-set to 1 on internal event.<br>0b - Timestamp Target Time Error status not detected<br>1b - Timestamp Target Time Error status detected|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3871 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|4<br>TSTARGT1|Timestamp Target Time Reached for Target Time PPS1 When this bit is set and<br>MCGREN1 of MAC_PPS_Control register is reset, it indicates that the value of system<br>time is greater than or equal to the value specified in the MAC_PPS1_Target_Time_Seconds<br>and MAC_PPS1_Target_Time_Nanoseconds registers. When this bit is set and MCGREN1 of<br>MAC_PPS_Control register is set, it indicates that mcgr_dma_req_o[1] is asserted. Access restriction<br>applies. Clears on read (or this bit is written to 1 when RCWE bit in MAC_CSR_SW_Ctrl register is set).<br>Self-set to 1 on internal event.<br>0b - Timestamp Target Time Reached for Target Time PPS1 status not detected<br>1b - Timestamp Target Time Reached for Target Time PPS1 status detected|
|3<br>TSTRGTERR0|Timestamp Target Time Error This bit is set when the latest target time programmed in the<br>MAC_PPS0_Target_Time_Seconds and MAC_PPS0_Target_Time_Nanoseconds registers elapses. This<br>bit is cleared when the application reads this bit. Access restriction applies. Clears on read (or this bit is<br>written to 1 when RCWE bit in MAC_CSR_SW_Ctrl register is set). Self-set to 1 on internal event.<br>0b - Timestamp Target Time Error status not detected<br>1b - Timestamp Target Time Error status detected|
|2<br>Reserved_AUX<br>TSTRIG|Reserved.|
|1<br>TSTARGT0|Timestamp Target Time Reached When this bit is set and MCGREN0 of MAC_PPS_Control register<br>is reset, it indicates that the value of system time is greater than or equal to the value specified<br>in the MAC_PPS0_Target_Time_Seconds and MAC_PPS0_Target_Time_Nanoseconds registers. When<br>this bit is set and MCGREN0 of MAC_PPS_Control register is set, it indicates that mcgr_dma_req_o[0]<br>is asserted. Access restriction applies. Clears on read (or this bit is written to 1 when RCWE bit in<br>MAC_CSR_SW_Ctrl register is set). Self-set to 1 on internal event.<br>0b - Timestamp Target Time Reached status not detected<br>1b - Timestamp Target Time Reached status detected|
|0<br>TSSOVF|Timestamp Seconds Overflow When this bit is set, it indicates that the seconds value of the timestamp<br>(when supporting version 2 format) has overflowed beyond 32'hFFFF_FFFF. Access restriction applies.<br>Clears on read (or this bit is written to 1 when RCWE bit in MAC_CSR_SW_Ctrl register is set). Self-set<br>to 1 on internal event.<br>0b - Timestamp Seconds Overflow status not detected<br>1b - Timestamp Seconds Overflow status detected|



# 75.7.230 (MAC_Tx_Timestamp_Status_Nanoseconds) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Tx_Timestamp_St|B30h|
|atus_Nanoseconds||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3872 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Function 

This register contains the nanosecond part of timestamp captured for Transmit packets when Tx status is disabled. The MAC_Tx_Timestamp_Status_Nanoseconds register, along with MAC_Tx_Timestamp_Status_Seconds, gives the 64-bit timestamp captured for the PTP packet successfully transmitted by the MAC. This value is considered to be read by the application when the last byte of MAC_Tx_Timestamp_Status_Nanoseconds is read. In the little-endian mode, this means when bits[31:24] are read; in big-endian mode, bits[7:0] are read. If the application does not read these registers and timestamp of another packet is captured, then either the current timestamp is lost (overwritten) or the new timestamp is lost (dropped), depending on the setting of the TXTSSTSM bit of the MAC_Timestamp_Control register. The status bit TXTSSIS bit [15] in MAC_Timestamp_Status register is set when the MAC transmitter captures the timestamp. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3873-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>TXTSS<br>R TXTSSLO<br>MIS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXTSSLO<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31<br>TXTSSMIS|Transmit Timestamp Status Missed When this bit is set, it indicates one of the following: - The timestamp<br>of the current packet is ignored if TXTSSTSM bit of the MAC_Timestamp_Control register is reset - The<br>timestamp of the previous packet is overwritten with timestamp of the current packet if TXTSSTSM bit of<br>the MAC_Timestamp_Control register is set. Access restriction applies. Clears on read. Self-set to 1 on<br>internal event.<br>0b - Transmit Timestamp Status Missed status not detected<br>1b - Transmit Timestamp Status Missed status detected|
|30-0<br>TXTSSLO|Transmit Timestamp Status Low This field contains the 31 bits of the Nanoseconds field of the Transmit<br>packet's captured timestamp.|



# 75.7.231 (MAC_Tx_Timestamp_Status_Seconds) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Tx_Timestamp_St|B34h|
|atus_Seconds||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3873 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Function 

The register contains the higher 32 bits of the timestamp (in seconds) captured when a PTP packet is transmitted. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3874-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXTSSHI<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXTSSHI<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Transmit Timestamp Status High This field contains the lower 32 bits of the Seconds field of Transmit|
|TXTSSHI|packet's captured timestamp.|



# 75.7.232 (MAC_Timestamp_Ingress_Asym_Corr) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Timestamp_Ingres|B50h|
|s_Asym_Corr||



## Function 

The MAC Timestamp Ingress Asymmetry Correction register contains the Ingress Asymmetry Correction value to be used while updating correction field in PDelay_Resp PTP messages. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3874-14.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>OSTIAC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>OSTIAC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3874 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0<br>OSTIAC|One-Step Timestamp Ingress Asymmetry Correction This field contains the ingress path asymmetry<br>value to be added to correctionField of Pdelay_Resp PTP packet. The programmed value should be in<br>units of nanoseconds and multiplied by 2^16. For example, 2.5 ns is represented as 0x00028000. The<br>value can also be negative, which is represented in 2's complement form with bit 31 representing the<br>sign bit.|



# 75.7.233 (MAC_Timestamp_Egress_Asym_Corr) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Timestamp_Egres|B54h|
|s_Asym_Corr||



## Function 

The MAC Timestamp Egress Asymmetry Correction register contains the Egress Asymmetry Correction value to be used while updating the correction field in PDelay_Req PTP messages. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||OST|EAC||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||OST|EAC||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0<br>OSTEAC|One-Step Timestamp Egress Asymmetry Correction This field contains the egress path asymmetry value<br>to be subtracted from correctionField of Pdelay_Resp PTP packet. The programmed value must be the<br>negated value in units of nanoseconds multiplied by 2^16. For example, if the required correction is +2.5|
||ns, the programmed value must be 0xFFFD_8000, which is the 2's complement of 0x0002_8000(2.5 *|
||216). Similarly, if the required correction is -3.3 ns, the programmed value is 0x0003_4CCC (3.3 * 216).|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3875 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.234 (MAC_Timestamp_Ingress_Corr_Nanosecond) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Timestamp_Ingres|B58h|
|s_Corr_Nanosecond||



## Function 

This register contains the correction value in nanoseconds to be used with the captured timestamp value in the ingress path. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3876-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>TSIC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>TSIC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-0<br>TSIC|Timestamp Ingress Correction This field contains the ingress path correction value as defined by the<br>Ingress Correction expression.|



# 75.7.235 (MAC_Timestamp_Egress_Corr_Nanosecond) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Timestamp_Egres|B5Ch|
|s_Corr_Nanosecond||



## Function 

This register contains the correction value in nanoseconds to be used with the captured timestamp value in the egress path. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3876 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3877-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>TSEC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>TSEC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0<br>TSEC|Timestamp Egress Correction This field contains the nanoseconds part of the egress path correction<br>value as defined by the Egress Correction expression.|



# 75.7.236 (MAC_Timestamp_Ingress_Corr_Subnanosec) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Timestamp_Ingres|B60h|
|s_Corr_Subnanosec||



## Function 

This register contains the sub-nanosecond part of the correction value to be used with the captured timestamp value, for ingress direction. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3877-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_16<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_7_0<br>TSICSNS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3877 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-16|Reserved.|
|Reserved_31_1<br>6||
|15-8<br>TSICSNS|Timestamp Ingress Correction, sub-nanoseconds This field contains the sub-nanoseconds part of the<br>ingress path correction value as defined by the "Ingress Correction" expression.|
|7-0|Reserved.|
|Reserved_7_0||



# 75.7.237 (MAC_Timestamp_Egress_Corr_Subnanosec) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Timestamp_Egres|B64h|
|s_Corr_Subnanosec||



## Function 

This register contains the sub-nanosecond part of the correction value to be used with the captured timestamp value, for egress direction. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3878-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_16<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_7_0<br>TSECSNS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-16|Reserved.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3878 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|Reserved_31_1<br>6||
|15-8<br>TSECSNS|Timestamp Egress Correction, sub-nanoseconds This field contains the sub-nanoseconds part of the<br>egress path correction value as defined by the "Egress Correction" expression.|
|7-0|Reserved.|
|Reserved_7_0||



# 75.7.238 (MAC_Timestamp_Ingress_Latency) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Timestamp_Ingres<br>s_Latency|B68h|



## Function 

This register holds the Ingress MAC latency. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||Reserve|d_31_28|||||||ITL|NS||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||ITL|SNS|||||||Reserv|ed_7_0||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function||
|---|---|---|
|31-28|Reserved.||
|Reserved_31_2|||
|8|||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3879 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|27-16<br>ITLNS|Ingress Timestamp Latency, in sub-nanoseconds This register holds the average latency in sub-<br>nanoseconds between the input ports (phy_rxd_i) of MAC and the actual point (GMII/MII) where the<br>ingress timestamp is taken. Ingress correction value is computed as described in the section, "Ingress<br>Correction".|
|15-8<br>ITLSNS|Ingress Timestamp Latency, in nanoseconds This register holds the average latency in nanoseconds<br>between the input ports (phy_rxd_i) of MAC and the actual point (GMII/MII) where the ingress timestamp<br>is taken. Ingress correction value is computed as described in the section, "Ingress Correction".|
|7-0|Reserved.|
|Reserved_7_0||



# 75.7.239 (MAC_Timestamp_Egress_Latency) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Timestamp_Egres|B6Ch|
|s_Latency||



## Function 

This register holds the Egress MAC latency. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||Reserve|d_31_28|||||||ETL|NS||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||ETL|SNS|||||||Reserv|ed_7_0||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-28|Reserved.|
|Reserved_31_2<br>8||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3880 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|27-16<br>ETLNS|Egress Timestamp Latency, in nanoseconds This register holds the average latency in nanoseconds<br>between the actual point (GMII/MII) where the egress timestamp is taken and the output ports<br>(phy_txd_o) of the MAC. Ingress correction value is computed as described in the section, "Ingress<br>Correction".|
|15-8<br>ETLSNS|Egress Timestamp Latency, in sub-nanoseconds This register holds the average latency in sub-<br>nanoseconds between the actual point (GMII/MII) where the egress timestamp is taken and the output<br>ports (phy_txd_o) of the MAC. Ingress correction value is computed as described in the section "Ingress<br>Correction".|
|7-0|Reserved.|
|Reserved_7_0||



# 75.7.240 (MAC_PPS_Control) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS_Control|B70h|



## Function 

PPS Control register. Bits[30:24] of this register are valid only when four Flexible PPS outputs are selected. Bits[22:16] are valid only when three or more Flexible PPS outputs are selected. Bits[14:8] are valid only when two or more Flexible PPS outputs are selected. Bits[6:4] are valid only when Flexible PPS feature is selected. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3881-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R MCGR TRGTMODSEL TIMES PPSCMD3  MCGR TRGTMODSEL e... PPSCMD2<br>EN3  3  EL  EN2  2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv<br>R MCGR TRGTMODSEL e... PPSCMD1  MCGR TRGTMODSEL PPSE PPSCTRL_PPSCMD<br>EN1  1  EN0  0  N0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3881 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field<br>31<br>MCGREN3|Function<br>MCGR Mode Enable for PPS3 Output This field enables the 3rd PPS instance to operate in PPS or<br>MCGR mode. - 1: Operates in MCGR mode - 0: Operates in PPS mode|
|---|---|
|30-29<br>TRGTMODSEL<br>3|Target Time Register Mode for PPS3 Output This field indicates the Target Time registers<br>(MAC_PPS3_Target_Time_Seconds and MAC_PPS3_Target_Time_Nanoseconds) mode for PPS3<br>output signal.<br>00b - Target Time registers are programmed only for generating the interrupt event. The Flexible<br>PPS function must not be enabled in this mode, otherwise spurious transitions may be observed<br>on the corresponding ptp_pps_o output port<br>01b - Enables MCGR Interrupt whose status bit is indicated by TSTARGT3<br>(MAC_Timestamp_Status[8])<br>10b - Target Time registers are programmed for generating the interrupt event and starting or<br>stopping the PPS0 output signal generation<br>11b - Target Time registers are programmed only for starting or stopping the PPS0 output signal<br>generation. No interrupt is asserted|
|28<br>TIMESEL|Time Select When this bit is set, 64 bit PTP time is used to capture time at MCGR trigger[0] input<br>When this bit is reset, presentation time is used to capture time at trigger input, maintaining backward<br>compatibility|
|27-24<br>PPSCMD3|Flexible PPS3 Output Control This field controls the flexible PPS3 output (ptp_pps_o[3]) signal. This field<br>is similar to the PPSCMD0[2:0] field. - When MCGREN3 is 1, PPSCMD3 indicated by the 4 bits [27:24]<br>are taken as Presentation Time Control bits for media clock generation and recovery for comparator<br>instance 3. This field is similar to the PPSCMD0 Presentation Time Control bits. - When MCGREN3 is<br>0, only 3 bits from [26:24] are used as PPSCMD3 and the 4th bit must be set as 0. Access restriction<br>applies. Setting 1 sets. Self-cleared. Setting 0 has no effect.|
|23<br>MCGREN2|MCGR Mode Enable for PPS2 Output This field enables the 2nd PPS instance to operate in PPS or<br>MCGR mode. - 1: Operates in MCGR mode - 0: Operates in PPS mode<br>0b - 2nd PPS instance is disabled to operate in PPS or MCGR mode<br>1b - 2nd PPS instance is enabled to operate in PPS or MCGR mode|
|22-21<br>TRGTMODSEL<br>2|Target Time Register Mode for PPS2 Output This field indicates the Target Time registers<br>(MAC_PPS2_Target_Time_Seconds and MAC_PPS2_Target_Time_Nanoseconds) mode for PPS2<br>output signal.<br>00b - Target Time registers are programmed only for generating the interrupt event. The Flexible<br>PPS function must not be enabled in this mode, otherwise spurious transitions may be observed<br>on the corresponding ptp_pps_o output port<br>01b - Enables MCGR Interrupt whose status bit is indicated by TSTARGT2<br>(MAC_Timestamp_Status[6])<br>10b - Target Time registers are programmed for generating the interrupt event and starting or<br>stopping the PPS0 output signal generation<br>11b - Target Time registers are programmed only for starting or stopping the PPS0 output signal<br>generation. No interrupt is asserted|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3882 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field<br>20<br>Reserved_20|Function<br>Reserved.|
|---|---|
|19-16<br>PPSCMD2|Flexible PPS2 Output Control This field controls the flexible PPS2 output (ptp_pps_o[2]) signal. This field<br>is similar to the PPSCMD0 field. - When MCGREN2 is 1, PPSCMD2 indicated by the 4 bits, [19:16] are<br>taken as Presentation Time Control bits for media clock generation and recovery for comparator instance<br>2. This field is similar to the PPSCMD0 Presentation Time Control bits. - When MCGREN2 is 0, only 3<br>bits, [18:16] are used as PPSCMD2 and the 4th bit must be set as 0. Access restriction applies. Setting 1<br>sets. Self-cleared. Setting 0 has no effect.|
|15<br>MCGREN1|MCGR Mode Enable for PPS1 Output This field enables the 1st PPS instance to operate in PPS or<br>MCGR mode. - 1: Operates in MCGR mode - 0: Operates in PPS mode<br>0b - 1st PPS instance is disabled to operate in PPS or MCGR mode<br>1b - 1st PPS instance is enabled to operate in PPS or MCGR mode|
|14-13<br>TRGTMODSEL<br>1|Target Time Register Mode for PPS1 Output This field indicates the Target Time registers<br>(MAC_PPS1_Target_Time_Seconds and MAC_PPS1_Target_Time_Nanoseconds) mode for PPS1<br>output signal.<br>00b - Target Time registers are programmed only for generating the interrupt event. The Flexible<br>PPS function must not be enabled in this mode, otherwise spurious transitions may be observed<br>on the corresponding ptp_pps_o output port<br>01b - Enables MCGR Interrupt whose status bit is indicated by TSTARGT1<br>(MAC_Timestamp_Status[4])<br>10b - Target Time registers are programmed for generating the interrupt event and starting or<br>stopping the PPS0 output signal generation<br>11b - Target Time registers are programmed only for starting or stopping the PPS0 output signal<br>generation. No interrupt is asserted|
|12<br>Reserved_12|Reserved.|
|11-8<br>PPSCMD1|Flexible PPS1 Output Control This field controls the flexible PPS1 output (ptp_pps_o[1]) signal. This field<br>is similar to the PPSCMD0 field. - When MCGREN1 is 1, PPSCMD1 indicated by the 4 bits [11:8] are<br>taken as Presentation Time Control bits for media clock generation and recovery for comparator instance<br>1. This field is similar to the PPSCMD0 Presentation Time Control bits. - When MCGREN1 is 0, only 3<br>bits, [10:8] are used as PPSCMD1 and the 4th bit must be set as 0. Access restriction applies. Setting 1<br>sets. Self-cleared. Setting 0 has no effect.|
|7<br>MCGREN0|MCGR Mode Enable for PPS0 Output This field enables the 0th PPS instance to operate in PPS or<br>MCGR mode. When set it operates in MCGR mode and on reset it operates in PPS mode.<br>0b - 0th PPS instance is enabled to operate in PPS mode<br>1b - 0th PPS instance is enabled to operate in MCGR mode|
|6-5|Target Time Register Mode for PPS0 Output This field indicates the Target Time registers<br>(MAC_PPS0_Target_Time_Seconds and MAC_PPS0_Target_Time_Nanoseconds) mode for PPS0<br>output signal:<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3883 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|TRGTMODSEL<br>0|00b - Target Time registers are programmed only for generating the interrupt event. The Flexible<br>PPS function must not be enabled in this mode, otherwise spurious transitions may be observed<br>on the corresponding ptp_pps_o output port<br>01b - Enables MCGR Interrupt whose status bit is indicated by TSTARGT0<br>(MAC_Timestamp_Status[1])<br>10b - Target Time registers are programmed for generating the interrupt event and starting or<br>stopping the PPS0 output signal generation<br>11b - Target Time registers are programmed only for starting or stopping the PPS0 output signal<br>generation. No interrupt is asserted|
|4<br>PPSEN0|Flexible PPS Output Mode Enable When this bit is - 1: Bits[3:0] function as PPSCMD. - 0: Bits[3:0]<br>function as PPSCTRL (Fixed PPS mode).<br>0b - Flexible PPS Output Mode is disabled<br>1b - Flexible PPS Output Mode is enabled|
|3-0<br>PPSCTRL_PPS<br>CMD|PPS Output Frequency Control This field controls the frequency of the PPS0 output (ptp_pps_o[0])<br>signal. The default value of PPSCTRL is 0000, and the PPS output is 1 pulse (of width clk_ptp_i)<br>every second. For other values of PPSCTRL, the PPS output becomes a generated clock of following<br>frequencies: - 0001: The binary rollover is 2 Hz, and the digital rollover is 1 Hz. - 0010: The binary<br>rollover is 4 Hz, and the digital rollover is 2 Hz. - 0011: The binary rollover is 8 Hz, and the digital<br>rollover is 4 Hz. - 0100: The binary rollover is 16 Hz, and the digital rollover is 8 Hz. - .. - 1111:<br>The binary rollover is 32.768 KHz and the digital rollover is 16.384 KHz. Note: In the binary rollover<br>mode, the PPS output (ptp_pps_o) has a duty cycle of 50 percent with these frequencies. In the<br>digital rollover mode, the PPS output frequency is an average number. The actual clock is of different<br>frequency that gets synchronized every second. For example: - When PPSCTRL = 0001, the PPS<br>(1 Hz) has a low period of 537 ms and a high period of 463 ms - When PPSCTRL = 0010, the<br>PPS (2 Hz) is a sequence of One clock of 50 percent duty cycle and 537 ms period Second clock<br>of 463 ms period (268 ms low and 195 ms high) - When PPSCTRL = 0011, the PPS (4 Hz) is<br>a sequence of Three clocks of 50 percent duty cycle and 268 ms period Fourth clock of 195 ms<br>period (134 ms low and 61 ms high) This behavior is because of the non-linear toggling of bits in<br>the digital rollover mode in the MAC_System_Time_Nanoseconds register. or Flexible PPS Output<br>(ptp_pps_o[0]) Control Programming these bits with a non-zero value instructs the MAC to initiate<br>an event. When the command is transferred or synchronized to the PTP clock domain, these bits<br>get cleared automatically. The software should ensure that these bits are programmed only when<br>they are 'all-zero'. The following list describes the values of PPSCMD0: - 0000: No Command -<br>0001: START Single Pulse This command generates single pulse rising at the start point defined<br>in MAC_PPS0_Target_Time_Seconds and MAC_PPS0_Target_Time_Nanoseconds register and of a<br>duration defined in the PPS0 Width Register. - 0010: START Pulse Train This command generates the<br>train of pulses rising at the start point defined in the Target Time Registers and of a duration defined<br>in the PPS0 Width Register and repeated at interval defined in the PPS Interval Register. By default,<br>the PPS pulse train is free-running unless stopped by the 'Stop Pulse train at time' or 'Stop Pulse<br>Train immediately' commands. - 0011: Cancel START This command cancels the START Single Pulse<br>and START Pulse Train commands if the system time has not crossed the programmed start time. -<br>0100: STOP Pulse train at time This command stops the train of pulses initiated by the START Pulse<br>Train command (PPSCMD = 0010) after the time programmed in the Target Time registers elapses. -<br>0101: STOP Pulse Train immediately This command immediately stops the train of pulses initiated by<br>the START Pulse Train command (PPSCMD = 0010). - 110: Cancel STOP Pulse train This command|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3884 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||cancels the STOP pulse train at time command if the programmed stop time has not elapsed. The<br>PPS pulse train becomes free-running on the successful execution of this command. - 0111-1111:<br>Reserved or Presentation Time Control When MCGREN0 is 1, these bits are treated as Presentation<br>time control bits. The following list describes the values of PPSCMD0: - 0000: MCGR operation is<br>not carried out. If set to this value in the mid of clock recovery or generation, all the processing<br>inputs are flushed - 0001: Capture the Presentation time at the rising edge of mcg_pst_trig_i[0] into the<br>MAC_PPS0_Target_Time_Seconds register - 0010: Capture the Presentation time at the falling edge of<br>mcg_pst_trig_i[0] into the MAC_PPS0_Target_Time_Seconds register - 0011: Capture the Presentation<br>time at both edges of mcg_pst_trig_i[0] into the MAC_PPS0_Target_Time_Seconds register - 0100-1000:<br>Reserved - 1001: Toggle output on compare - 1010: Pulse output low on compare for one PTP-clock<br>cycle - 1011: Pulse output high on compare for one PTP-clock cycle - 1100-1111: Reserved|



# 75.7.241 (MAC_PPS0_Target_Time_Seconds) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS0_Target_Tim|B80h|
|e_Seconds||



## Function 

The PPS Target Time Seconds register, along with PPS Target Time Nanoseconds register, is used to schedule an interrupt event [Bit 1 of MAC_Timestamp_Status] when the system time exceeds the value programmed in these registers. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||TST|RH0||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||TST|RH0||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function|
|---|---|
|31-0|PPS Target Time Seconds Register This field stores the time in seconds. When the timestamp value|
|TSTRH0|matches or exceeds both Target Timestamp registers, the MAC starts or stops the PPS signal output<br>and generates an interrupt (if enabled) based on Target Time mode selected for the corresponding|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3885 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

|Field|Function|
|---|---|
||PPS output in the MAC_PPS_Control register. If DWC_EQOS_FLEXI_PPS_OUT_EN is enabled in the<br>configuration and PTGE field of MAC_Timestamp_Control Register is set with Presentation time control|
||set in recovery mode, then these bits indicate the TPT being programmed by the application and in|
||generation mode it indicates the CPT generated at the sampled trigger.|



# 75.7.242 (MAC_PPS0_Target_Time_Nanoseconds) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS0_Target_Tim|B84h|
|e_Nanoseconds||



## Function 

PPS0 Target Time Nanoseconds register. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3886-09.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TRGT<br>TTSL0<br>W BUS...<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>TTSL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31<br>TRGTBUSY0|PPS Target Time Register Busy The MAC sets this bit when the PPSCMD0 field in the<br>MAC_PPS_Control register is programmed to 010 or 011. Programming the PPSCMD0 field to 010<br>or 011 instructs the MAC to synchronize the Target Time Registers to the PTP clock domain. The MAC<br>clears this bit after synchronizing the Target Time Registers to the PTP clock domain The application<br>must not update the Target Time Registers when this bit is read as 1. Otherwise, the synchronization of<br>the previous programmed time gets corrupted.<br>0b - PPS Target Time Register Busy status is not detected<br>1b - PPS Target Time Register Busy is detected|
|30-0<br>TTSL0|Target Time Low for PPS Register This register stores the time in (signed) nanoseconds. When the<br>value of the timestamp matches the value in both Target Timestamp registers, the MAC starts or stops<br>the PPS signal output and generates an interrupt (if enabled) based on the TRGTMODSEL0 field (Bits|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3886 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||[6:5]) in MAC_PPS_Control. When the TSCTRLSSR bit is reset in the MAC_Timestamp_Control register,<br>this value should be (time in ns / 0.465). The actual start or stop time of the PPS signal output might<br>have an error margin up to one unit of sub-second increment value. When the TSCTRLSSR bit is set in|
||the MAC_Timestamp_Control register, this value should not exceed 0x3B9A_C9FF. The actual start or<br>stop time of the PPS signal output might have an error margin up to one unit of sub-second increment|
||value. Access restriction applies. Setting 1 sets. Self-cleared. Setting 0 has no effect.|



# 75.7.243 (MAC_PPS0_Interval) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS0_Interval|B88h|



## Function 

The PPS0 Interval register contains the number of units of sub-second increment value between the rising edges of PPS0 signal output (ptp_pps_o[0]). 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||PPS|INT0||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||PPS|INT0||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function|
|---|---|
|31-0<br>PPSINT0|PPS Output Signal Interval These bits store the interval between the rising edges of PPS0 signal output.<br>The interval is stored in terms of number of units of sub-second increment value. You need to program<br>one value less than the required interval. For example, if the PTP reference clock is 50 MHz (period of|
||20 ns), and desired interval between the rising edges of PPS0 signal output is 100 ns (that is, 5 units of<br>sub-second increment value), you should program value 4 (5-1) in this register.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3887 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.244 (MAC_PPS0_Width) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS0_Width|B8Ch|



## Function 

The PPS0 Width register contains the number of units of sub-second increment value between the rising and corresponding falling edges of PPS0 signal output (ptp_pps_o[0]). 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||PPSW|IDTH0||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||PPSW|IDTH0||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0<br>PPSWIDTH0|PPS Output Signal Width These bits store the width between the rising edge and corresponding falling<br>edge of PPS0 signal output. The width is stored in terms of number of units of sub-second increment<br>value. You need to program one value less than the required interval. For example, if PTP reference<br>clock is 50 MHz (period of 20 ns), and width between the rising and corresponding falling edges of<br>PPS0 signal output is 80 ns (that is, four units of sub-second increment value), you should program<br>value 3 (4-1) in this register. Note: The value programmed in this register must be lesser than the value<br>programmed in MAC_PPS0_Interval.|



# 75.7.245 (MAC_PPS1_Target_Time_Seconds) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS1_Target_Tim|B90h|
|e_Seconds||



## Function 

The PPS Target Time Seconds register, along with PPS Target Time Nanoseconds register, is used to schedule an interrupt event [Bit 1 of MAC_Timestamp_Status] when the system time exceeds the value programmed in these registers. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3888 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3889-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>TSTRH1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>TSTRH1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0<br>TSTRH1|PPS Target Time Seconds Register This field stores the time in seconds. When the timestamp value<br>matches or exceeds both Target Timestamp registers, the MAC starts or stops the PPS signal output<br>and generates an interrupt (if enabled) based on Target Time mode selected for the corresponding<br>PPS output in the MAC_PPS_Control register. If DWC_EQOS_FLEXI_PPS_OUT_EN is enabled in the<br>configuration and PTGE field of MAC_Timestamp_Control Register is set with Presentation time control<br>set in recovery mode, then these bits indicate the TPT being programmed by the application and in<br>generation mode it indicates the CPT generated at the sampled trigger.|



# 75.7.246 (MAC_PPS1_Target_Time_Nanoseconds) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS1_Target_Tim|B94h|
|e_Nanoseconds||



## Function 

## PPS0 Target Time Nanoseconds register. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|TRGT<br>BUS...||||||||TTSL1||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||TT|SL1||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3889 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31<br>TRGTBUSY1|PPS Target Time Register Busy The MAC sets this bit when the PPSCMD0 field in the<br>MAC_PPS_Control register is programmed to 010 or 011. Programming the PPSCMD0 field to 010<br>or 011 instructs the MAC to synchronize the Target Time Registers to the PTP clock domain. The MAC<br>clears this bit after synchronizing the Target Time Registers to the PTP clock domain The application<br>must not update the Target Time Registers when this bit is read as 1. Otherwise, the synchronization of<br>the previous programmed time gets corrupted.<br>0b - PPS Target Time Register Busy status is not detected<br>1b - PPS Target Time Register Busy is detected|
|30-0<br>TTSL1|Target Time Low for PPS Register This register stores the time in (signed) nanoseconds. When the<br>value of the timestamp matches the value in both Target Timestamp registers, the MAC starts or stops<br>the PPS signal output and generates an interrupt (if enabled) based on the TRGTMODSEL0 field (Bits<br>[6:5]) in MAC_PPS_Control. When the TSCTRLSSR bit is reset in the MAC_Timestamp_Control register,<br>this value should be (time in ns / 0.465). The actual start or stop time of the PPS signal output might<br>have an error margin up to one unit of sub-second increment value. When the TSCTRLSSR bit is set in<br>the MAC_Timestamp_Control register, this value should not exceed 0x3B9A_C9FF. The actual start or<br>stop time of the PPS signal output might have an error margin up to one unit of sub-second increment<br>value. Access restriction applies. Setting 1 sets. Self-cleared. Setting 0 has no effect.|



# 75.7.247 (MAC_PPS1_Interval) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS1_Interval|B98h|



## Function 

The PPS0 Interval register contains the number of units of sub-second increment value between the rising edges of PPS0 signal output (ptp_pps_o[0]). 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||PPS|INT1||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||PPS|INT1||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3890 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0<br>PPSINT1|PPS Output Signal Interval These bits store the interval between the rising edges of PPS0 signal output.<br>The interval is stored in terms of number of units of sub-second increment value. You need to program<br>one value less than the required interval. For example, if the PTP reference clock is 50 MHz (period of|
||20 ns), and desired interval between the rising edges of PPS0 signal output is 100 ns (that is, 5 units of<br>sub-second increment value), you should program value 4 (5-1) in this register.|



# 75.7.248 (MAC_PPS1_Width) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS1_Width|B9Ch|



## Function 

The PPS0 Width register contains the number of units of sub-second increment value between the rising and corresponding falling edges of PPS0 signal output (ptp_pps_o[0]). 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3891-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>PPSWIDTH1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>PPSWIDTH1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0<br>PPSWIDTH1|PPS Output Signal Width These bits store the width between the rising edge and corresponding falling<br>edge of PPS0 signal output. The width is stored in terms of number of units of sub-second increment<br>value. You need to program one value less than the required interval. For example, if PTP reference<br>clock is 50 MHz (period of 20 ns), and width between the rising and corresponding falling edges of<br>PPS0 signal output is 80 ns (that is, four units of sub-second increment value), you should program<br>value 3 (4-1) in this register. Note: The value programmed in this register must be lesser than the value<br>programmed in MAC_PPS0_Interval.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3891 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.249 (MAC_PPS2_Target_Time_Seconds) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS2_Target_Tim|BA0h|
|e_Seconds||



## Function 

The PPS Target Time Seconds register, along with PPS Target Time Nanoseconds register, is used to schedule an interrupt event [Bit 1 of MAC_Timestamp_Status] when the system time exceeds the value programmed in these registers. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||TST|RH2||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||TST|RH2||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0<br>TSTRH2|PPS Target Time Seconds Register This field stores the time in seconds. When the timestamp value<br>matches or exceeds both Target Timestamp registers, the MAC starts or stops the PPS signal output<br>and generates an interrupt (if enabled) based on Target Time mode selected for the corresponding<br>PPS output in the MAC_PPS_Control register. If DWC_EQOS_FLEXI_PPS_OUT_EN is enabled in the<br>configuration and PTGE field of MAC_Timestamp_Control Register is set with Presentation time control<br>set in recovery mode, then these bits indicate the TPT being programmed by the application and in<br>generation mode it indicates the CPT generated at the sampled trigger.|



# 75.7.250 (MAC_PPS2_Target_Time_Nanoseconds) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS2_Target_Tim|BA4h|
|e_Nanoseconds||



## Function 

PPS0 Target Time Nanoseconds register. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3892 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3893-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TRGT<br>TTSL2<br>W BUS...<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>TTSL2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31<br>TRGTBUSY2|PPS Target Time Register Busy The MAC sets this bit when the PPSCMD0 field in the<br>MAC_PPS_Control register is programmed to 010 or 011. Programming the PPSCMD0 field to 010<br>or 011 instructs the MAC to synchronize the Target Time Registers to the PTP clock domain. The MAC<br>clears this bit after synchronizing the Target Time Registers to the PTP clock domain The application<br>must not update the Target Time Registers when this bit is read as 1. Otherwise, the synchronization of<br>the previous programmed time gets corrupted.<br>0b - PPS Target Time Register Busy status is not detected<br>1b - PPS Target Time Register Busy is detected|
|30-0<br>TTSL2|Target Time Low for PPS Register This register stores the time in (signed) nanoseconds. When the<br>value of the timestamp matches the value in both Target Timestamp registers, the MAC starts or stops<br>the PPS signal output and generates an interrupt (if enabled) based on the TRGTMODSEL0 field (Bits<br>[6:5]) in MAC_PPS_Control. When the TSCTRLSSR bit is reset in the MAC_Timestamp_Control register,<br>this value should be (time in ns / 0.465). The actual start or stop time of the PPS signal output might<br>have an error margin up to one unit of sub-second increment value. When the TSCTRLSSR bit is set in<br>the MAC_Timestamp_Control register, this value should not exceed 0x3B9A_C9FF. The actual start or<br>stop time of the PPS signal output might have an error margin up to one unit of sub-second increment<br>value. Access restriction applies. Setting 1 sets. Self-cleared. Setting 0 has no effect.|



# 75.7.251 (MAC_PPS2_Interval) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS2_Interval|BA8h|



## Function 

The PPS0 Interval register contains the number of units of sub-second increment value between the rising edges of PPS0 signal output (ptp_pps_o[0]). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3893 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3894-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>PPSINT2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>PPSINT2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0<br>PPSINT2|PPS Output Signal Interval These bits store the interval between the rising edges of PPS0 signal output.<br>The interval is stored in terms of number of units of sub-second increment value. You need to program<br>one value less than the required interval. For example, if the PTP reference clock is 50 MHz (period of|
||20 ns), and desired interval between the rising edges of PPS0 signal output is 100 ns (that is, 5 units of|
||sub-second increment value), you should program value 4 (5-1) in this register.|



# 75.7.252 (MAC_PPS2_Width) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS2_Width|BACh|



## Function 

The PPS0 Width register contains the number of units of sub-second increment value between the rising and corresponding falling edges of PPS0 signal output (ptp_pps_o[0]). 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||PPSW|IDTH2||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||PPSW|IDTH2||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3894 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0<br>PPSWIDTH2|PPS Output Signal Width These bits store the width between the rising edge and corresponding falling<br>edge of PPS0 signal output. The width is stored in terms of number of units of sub-second increment<br>value. You need to program one value less than the required interval. For example, if PTP reference<br>clock is 50 MHz (period of 20 ns), and width between the rising and corresponding falling edges of<br>PPS0 signal output is 80 ns (that is, four units of sub-second increment value), you should program<br>value 3 (4-1) in this register. Note: The value programmed in this register must be lesser than the value<br>programmed in MAC_PPS0_Interval.|



# 75.7.253 (MAC_PPS3_Target_Time_Seconds) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS3_Target_Tim|BB0h|
|e_Seconds||



## Function 

The PPS Target Time Seconds register, along with PPS Target Time Nanoseconds register, is used to schedule an interrupt event [Bit 1 of MAC_Timestamp_Status] when the system time exceeds the value programmed in these registers. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||TST|RH3||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||TST|RH3||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function|
|---|---|
|31-0<br>TSTRH3|PPS Target Time Seconds Register This field stores the time in seconds. When the timestamp value<br>matches or exceeds both Target Timestamp registers, the MAC starts or stops the PPS signal output<br>and generates an interrupt (if enabled) based on Target Time mode selected for the corresponding<br>PPS output in the MAC_PPS_Control register. If DWC_EQOS_FLEXI_PPS_OUT_EN is enabled in the<br>configuration and PTGE field of MAC_Timestamp_Control Register is set with Presentation time control<br>set in recovery mode, then these bits indicate the TPT being programmed by the application and in<br>generation mode it indicates the CPT generated at the sampled trigger.|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3895 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.254 (MAC_PPS3_Target_Time_Nanoseconds) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS3_Target_Tim|BB4h|
|e_Nanoseconds||



## Function 

## PPS0 Target Time Nanoseconds register. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3896-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TRGT<br>TTSL3<br>W BUS...<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>TTSL3<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31<br>TRGTBUSY3|PPS Target Time Register Busy The MAC sets this bit when the PPSCMD0 field in the<br>MAC_PPS_Control register is programmed to 010 or 011. Programming the PPSCMD0 field to 010<br>or 011 instructs the MAC to synchronize the Target Time Registers to the PTP clock domain. The MAC<br>clears this bit after synchronizing the Target Time Registers to the PTP clock domain The application<br>must not update the Target Time Registers when this bit is read as 1. Otherwise, the synchronization of<br>the previous programmed time gets corrupted.<br>0b - PPS Target Time Register Busy status is not detected<br>1b - PPS Target Time Register Busy is detected|
|30-0<br>TTSL3|Target Time Low for PPS Register This register stores the time in (signed) nanoseconds. When the<br>value of the timestamp matches the value in both Target Timestamp registers, the MAC starts or stops<br>the PPS signal output and generates an interrupt (if enabled) based on the TRGTMODSEL0 field (Bits<br>[6:5]) in MAC_PPS_Control. When the TSCTRLSSR bit is reset in the MAC_Timestamp_Control register,<br>this value should be (time in ns / 0.465). The actual start or stop time of the PPS signal output might<br>have an error margin up to one unit of sub-second increment value. When the TSCTRLSSR bit is set in<br>the MAC_Timestamp_Control register, this value should not exceed 0x3B9A_C9FF. The actual start or<br>stop time of the PPS signal output might have an error margin up to one unit of sub-second increment<br>value. Access restriction applies. Setting 1 sets. Self-cleared. Setting 0 has no effect.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3896 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.255 (MAC_PPS3_Interval) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS3_Interval|BB8h|



## Function 

The PPS0 Interval register contains the number of units of sub-second increment value between the rising edges of PPS0 signal output (ptp_pps_o[0]). 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3897-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>PPSINT3<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>PPSINT3<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0<br>PPSINT3|PPS Output Signal Interval These bits store the interval between the rising edges of PPS0 signal output.<br>The interval is stored in terms of number of units of sub-second increment value. You need to program<br>one value less than the required interval. For example, if the PTP reference clock is 50 MHz (period of|
||20 ns), and desired interval between the rising edges of PPS0 signal output is 100 ns (that is, 5 units of|
||sub-second increment value), you should program value 4 (5-1) in this register.|



# 75.7.256 (MAC_PPS3_Width) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS3_Width|BBCh|



## Function 

The PPS0 Width register contains the number of units of sub-second increment value between the rising and corresponding falling edges of PPS0 signal output (ptp_pps_o[0]). 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3897 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3898-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>PPSWIDTH3<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>PPSWIDTH3<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0<br>PPSWIDTH3|PPS Output Signal Width These bits store the width between the rising edge and corresponding falling<br>edge of PPS0 signal output. The width is stored in terms of number of units of sub-second increment<br>value. You need to program one value less than the required interval. For example, if PTP reference<br>clock is 50 MHz (period of 20 ns), and width between the rising and corresponding falling edges of<br>PPS0 signal output is 80 ns (that is, four units of sub-second increment value), you should program<br>value 3 (4-1) in this register. Note: The value programmed in this register must be lesser than the value<br>programmed in MAC_PPS0_Interval.|



# 75.7.257 (MTL_Operation_Mode) 

## Offset 

|Register|Offset|
|---|---|
|MTL_Operation_Mode|C00h|



## Function 

The Operation Mode register establishes the Transmit and Receive operating modes and commands. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3898-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_16<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv Reserv<br>R FRPE  RXPE Reserved_13_10  CNTC CNTP e... SCHALG  Reserved_4_3  RAA  DTXS e...<br>D  LR  RST  TS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3898 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field<br>31-16<br>Reserved_31_1<br>6|Function<br>Reserved.|
|---|---|
|15<br>FRPE|Flexible Rx parser Enable - 1: Enables Programmable Rx Parser - 0: Disables Programmable Rx Parser<br>When the Rx parser is disabled when parsing is in progress, the Rx parser is disabled only after the<br>current packet parsing complete. When the Rx parser is enabled, the parser gets activated for the next<br>packet.<br>0b - Flexible Rx parser is disabled<br>1b - Flexible Rx parser is enabled|
|14<br>RXPED|RxParser Software Error/Incomplete Parsing Packet Drop Enable when this bit is set to 0, packets<br>encountering software programming errors (NPE/NVE/frame offset overflow errors) or incomplete<br>parsing are forwarded to application with the corresponding RxParser status. When this bit is set to<br>1, backward compatibility is maintained where all the specified packets are dropped (when RA is not set)<br>0b - Flexible Rx parser, packet drop in case software error is disabled<br>1b - Flexible Rx parser, packet drop in case software error is enabled|
|13-10<br>Reserved_13_1<br>0|Reserved.|
|9<br>CNTCLR|Counters Reset When this bit is set, all counters are reset. This bit is cleared automatically after 1 clock<br>cycle. If this bit is set along with CNT_PRESET bit, CNT_PRESET has precedence. Access restriction<br>applies. Setting 1 sets. Self-cleared. Setting 0 has no effect.<br>0b - Counters are not reset<br>1b - All counters are reset|
|8<br>CNTPRST|Counters Preset When this bit is set, - MTL_TxQ[0-7]_Underflow register is initialized/preset to 12'h7F0.<br>- Missed Packet and Overflow Packet counters in MTL_RxQ[0-7]_Missed_Packet_Overflow_Cnt register<br>is initialized/preset to 12'h7F0. Access restriction applies. Setting 1 sets. Self-cleared. Setting 0 has no<br>effect.<br>0b - Counters Preset is disabled<br>1b - Counters Preset is enabled|
|7<br>Reserved_7|Reserved.|
|6-5<br>SCHALG|Tx Scheduling Algorithm This field indicates the algorithm for Tx scheduling:<br>00b - WRR algorithm<br>01b - WFQ algorithm when DCB feature is selected.Otherwise, Reserved<br>10b - DWRR algorithm when DCB feature is selected.Otherwise, Reserved<br>11b - Strict priority algorithm|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3899 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|4-3|Reserved.|
|Reserved_4_3||
|2<br>RAA|Receive Arbitration Algorithm This field is used to select the arbitration algorithm for the Rx side. - 0:<br>Strict priority (SP). Queue 0 has the lowest priority and the last queue has the highest priority. - 1:<br>Weighted Strict Priority (WSP)<br>0b - Strict priority (SP)<br>1b - Weighted Strict Priority (WSP)|
|1<br>DTXSTS|Drop Transmit Status - 1: Tx packet status received from the MAC is dropped in the MTL - 0: Tx packet<br>status received from the MAC is forwarded to the application<br>0b - Drop Transmit Status is disabled<br>1b - Drop Transmit Status is enabled|
|0|Reserved.|
|Reserved_0||



# 75.7.258 (MTL_DBG_CTL) 

## Offset 

|Register|Offset|
|---|---|
|MTL_DBG_CTL|C08h|



## Function 

The FIFO Debug Access Control and Status register controls the operation mode of FIFO debug access. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3900-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_19<br>EIEC  EIAEE  EIEE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv Reserv<br>R STSIE  PKTIE  FIFOSEL  FIFOW FIFOR RSTS RSTAL e... PKTSTATE  e... BYTEEN  DBGM FDBG<br>REN  DEN  EL  L  OD  EN<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3900 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field<br>31-19<br>Reserved_31_1<br>9|Function<br>Reserved.|
|---|---|
|18<br>EIEC|ECC Inject Error Control for Tx, Rx, TSO and DCACHE memories When EIEE or EIAEE bit of this<br>register is set, following are the errors inserted based on the value encoded in this field.<br>0b - Insert 1 bit error<br>1b - insert 2 bit errors|
|17<br>EIAEE|ECC Inject Address Error for Tx, Rx, TSO and DCACHE memories - 1: Enables the ECC address error<br>injection feature - 0: Disables the ECC address error injection feature<br>0b - Disables the ECC address error injection<br>1b - Enables the ECC address error injection|
|16<br>EIEE|ECC Inject Error Enable for Tx, Rx, TSO and DCACHE memories - 1: Enables the ECC error injection<br>feature - 0: Disables the ECC error injection feature<br>0b - ECC Inject Error for Tx, Rx, TSO and DCACHE memories is disabled<br>1b - ECC Inject Error for Tx, Rx, TSO and DCACHE memories is enabled|
|15<br>STSIE|Transmit Status Available Interrupt Status Enable When this bit is set, an interrupt is generated when<br>Transmit status is available in slave mode.<br>0b - Transmit Packet Available Interrupt Status is disabled<br>1b - Transmit Packet Available Interrupt Status is enabled|
|14<br>PKTIE|Receive Packet Available Interrupt Status Enable When this bit is set, an interrupt is generated when<br>EOP of received packet is written to the Rx FIFO.<br>0b - Receive Packet Available Interrupt Status is disabled<br>1b - Receive Packet Available Interrupt Status is enabled|
|13-12<br>FIFOSEL|FIFO Selected for Access This field indicates the FIFO selected for debug access.<br>00b - Tx FIFO<br>01b - Tx Status FIFO (only read access when SLVMOD is set)/ DC Memory FIFO read-write<br>access when DBGMOD is set<br>10b - TSO FIFO (cannot be accessed when SLVMOD is set)<br>11b - Rx FIFO|
|11<br>FIFOWREN|FIFO Write Enable When this bit is set, it enables the Write operation on selected FIFO when FIFO<br>Debug Access is enabled. This bit must not be written to 1 when FIFO Debug Access is not enabled, that<br>is FDBGEN bit is 0. Access restriction applies. Self-cleared. Setting 0 clears. Setting 1 sets.<br>0b - FIFO Write is disabled<br>1b - FIFO Write is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3901 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field<br>10<br>FIFORDEN|Function<br>FIFO Read Enable When this bit is set, it enables the Read operation on selected FIFO when FIFO<br>Debug Access is enabled. This bit must not be written to 1 when FIFO Debug Access is not enabled, that<br>is FDBGEN bit is 0. Access restriction applies. Self-cleared. Setting 0 clears. Setting 1 sets.<br>0b - FIFO Read is disabled<br>1b - FIFO Read is enabled|
|---|---|
|9<br>RSTSEL|Reset Pointers of Selected FIFO When this bit is set, the pointers of the currently-selected FIFO are<br>reset when FIFO Debug Access is enabled. This bit must not be written to 1 when FIFO Debug Access is<br>not enabled, that is FDBGEN bit is 0. Access restriction applies. Self-cleared. Setting 0 clears. Setting 1<br>sets.<br>0b - Reset Pointers of Selected FIFO is disabled<br>1b - Reset Pointers of Selected FIFO is enabled|
|8<br>RSTALL|Reset All Pointers When this bit is set, the pointers of all FIFOs are reset when FIFO Debug Access is<br>enabled. This bit must not be written to 1 when FIFO Debug Access is not enabled, that is FDBGEN bit<br>is 0. Access restriction applies. Self-cleared. Setting 0 clears. Setting 1 sets.<br>0b - Reset All Pointers is disabled<br>1b - Reset All Pointers is enabled|
|7<br>Reserved_7|Reserved.|
|6-5<br>PKTSTATE|Encoded Packet State This field is used to write the control information to the Tx FIFO or Rx FIFO. - Tx<br>FIFO: -- 00: Packet Data -- 01: Control Word -- 10: SOP Data -- 11: EOP Data - Rx FIFO: -- 00: Packet<br>Data -- 01: Normal Status -- 10: Last Status -- 11: EOP<br>00b - Packet Data<br>01b - Control Word/Normal Status<br>10b - SOP Data/Last Status<br>11b - EOP Data/EOP|
|4<br>Reserved_4|Reserved.|
|3-2<br>BYTEEN|Byte Enables This field indicates the number of data bytes valid in the data register during Write<br>operation. This is valid only when PKTSTATE is 2'b10 (EOP) and Tx FIFO or Rx FIFO is selected.<br>00b - Byte 0 valid<br>01b - Byte 0 and Byte 1 are valid<br>10b - Byte 0, Byte 1, and Byte 2 are valid<br>11b - All four bytes are valid|
|1<br>DBGMOD|Debug Mode Access to FIFO - 1: Indicates that the current access to the FIFO is read, write, and debug<br>access. In this mode, the following access types are allowed: -- Read and Write access to Tx FIFO, TSO<br>FIFO, DCACHE FIFO and Rx FIFO -- Read access is allowed to Tx Status FIFO. - 0: Indicates that the|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3902 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||current access to the FIFO is slave access bypassing the DMA. In this mode, the following access are<br>allowed: -- Write access to the Tx FIFO -- Read access to the Rx FIFO and Tx Status FIFO<br>0b - Debug Mode Access to FIFO is disabled|
||1b - Debug Mode Access to FIFO is enabled|
|0<br>FDBGEN|FIFO Debug Access Enable - 1: Indicates that the debug mode access to the FIFO is enabled. - 0:<br>Indicates that the FIFO can be accessed only through a master interface.<br>0b - FIFO Debug Access is disabled<br>1b - FIFO Debug Access is enabled|



# 75.7.259 (MTL_DBG_STS) 

## Offset 

|Register|Offset|
|---|---|
|MTL_DBG_STS|C0Ch|



## Function 

The FIFO Debug Status register contains the status of FIFO debug access. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3903-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R LOCR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>FIFOB<br>R LOCR  Reserved_14_10  Reserved_7_5  BYTEEN  PKTSTATE<br>STSI  PKTI  USY<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-15<br>LOCR|Remaining Locations in the FIFO - Slave Access Mode: This field indicates the space available in<br>the selected FIFO. - Debug Access Mode: This field contains the Write or Read pointer value of the<br>selected FIFO during Write or Read operation, respectively. - Reset: In single Tx Queue configurations,<br>(DWC_EQOS_TXFIFO_SIZE/(DWC_EQOS_DATAWIDTH/8)), Otherwise 0000H|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3903 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|14-10|Reserved.|
|Reserved_14_1<br>0||
|9<br>STSI|Transmit Status Available Interrupt Status When set, this bit indicates that the Slave mode Tx packet is<br>transmitted, and the status is available in Tx Status FIFO. This bit is reset when 1 is written to this bit.<br>0b - Transmit Status Available Interrupt Status not detected<br>1b - Transmit Status Available Interrupt Status detected|
|8<br>PKTI|Receive Packet Available Interrupt Status When set, this bit indicates that MAC layer has written the<br>EOP of received packet to the Rx FIFO. This bit is reset when 1 is written to this bit.<br>0b - Receive Packet Available Interrupt Status not detected<br>1b - Receive Packet Available Interrupt Status detected|
|7-5|Reserved.|
|Reserved_7_5||
|4-3<br>BYTEEN|Byte Enables This field indicates the number of data bytes valid in the data register during Read<br>operation. This is valid only when PKTSTATE is 2'b10 (EOP) and Tx FIFO or Rx FIFO is selected.<br>00b - Byte 0 valid<br>01b - Byte 0 and Byte 1 are valid<br>10b - Byte 0, Byte 1, and Byte 2 are valid<br>11b - All four bytes are valid|
|2-1<br>PKTSTATE|Encoded Packet State This field is used to get the control or status information of the selected FIFO. - Tx<br>FIFO: -- 00: Packet Data -- 01: Control Word -- 10: SOP Data -- 11: EOP Data - Rx FIFO: -- 00: Packet<br>Data -- 01: Normal Status -- 10: Last Status -- 11: EOP This field is applicable only for Tx FIFO and Rx<br>FIFO during Read operation.<br>00b - Packet Data<br>01b - Control Word/Normal Status<br>10b - SOP Data/Last Status<br>11b - EOP Data/EOP|
|0<br>FIFOBUSY|FIFO Busy When set, this bit indicates that a FIFO operation is in progress in the MAC and content of<br>the following fields is not valid: - All other fields of this register - All fields of the MTL_FIFO_Debug_Data<br>register<br>0b - FIFO Busy not detected<br>1b - FIFO Busy detected|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3904 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.260 (MTL_FIFO_Debug_Data) 

## Offset 

|Register|Offset|
|---|---|
|MTL_FIFO_Debug_Data|C10h|



## Function 

The FIFO Debug Data register contains the data to be written to or read from the FIFOs. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||FDBG|DATA||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||FDBG|DATA||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|FIFO Debug Data During debug or slave access write operation, this field contains the data to be written|
||to the Tx FIFO, Rx FIFO, or TSO FIFO. During debug or slave access read operation, this field contains|
|FDBGDATA|the data read from the Tx FIFO, Rx FIFO, TSO FIFO, or Tx Status FIFO.|



# 75.7.261 (MTL_Interrupt_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_Interrupt_Status|C20h|



## Function 

The software driver (application) reads this register during interrupt service routine or polling to determine the interrupt status of MTL queues and the MAC. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3905 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3906-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>MTLPI Reserv<br>R Reserved_31_24  Reserved_22_19  ESTIS  DBGIS<br>S  e...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv Reserv Reserv Reserv Reserv<br>R Reserved_15_8  Q2IS  Q1IS  Q0IS<br>e... e... e... e... e...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-24|Reserved.|
|Reserved_31_2<br>4||
|23<br>MTLPIS|MTL Rx Parser Interrupt Status This bit indicates that there is an interrupt from Rx Parser Block. To reset<br>this bit, the application must read the MTL_ Rxp_Interrupt_Status register to get the exact cause of the<br>interrupt and clear its source.<br>0b - MTL Rx Parser Interrupt status not detected<br>1b - MTL Rx Parser Interrupt status detected|
|22-19|Reserved.|
|Reserved_22_1<br>9||
|18<br>ESTIS|EST (TAS- 802.1Qbv) Interrupt Status This bit indicates an interrupt event during the operation of<br>802.1Qbv. To reset this bit, the application must clear the error/event that has caused the Interrupt.<br>0b - EST (TAS- 802.1Qbv) Interrupt status not detected<br>1b - EST (TAS- 802.1Qbv) Interrupt status detected|
|17<br>DBGIS|Debug Interrupt status This bit indicates an interrupt event during the slave access. To reset this bit, the<br>application must read the FIFO Debug Access Status register to get the exact cause of the interrupt and<br>clear its source.<br>0b - Debug Interrupt status not detected<br>1b - Debug Interrupt status detected|
|16|Reserved.|
|Reserved_MAC<br>IS||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3906 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|15-8<br>Reserved_15_8|Reserved.|
|7|Reserved.|
|Reserved_Q7IS||
|6|Reserved.|
|Reserved_Q6IS||
|5|Reserved.|
|Reserved_Q5IS||
|4|Reserved.|
|Reserved_Q4IS||
|3|Reserved.|
|Reserved_Q3IS||
|2<br>Q2IS|Queue 2 Interrupt status This bit indicates that there is an interrupt from Queue 2. To reset this bit,<br>the application must read the MTL_Q2_Interrupt_Control_Status register to get the exact cause of the<br>interrupt and clear its source.<br>0b - Queue 2 Interrupt status not detected<br>1b - Queue 2 Interrupt status detected|
|1<br>Q1IS|Queue 1 Interrupt status This bit indicates that there is an interrupt from Queue 1. To reset this bit,<br>the application must read the MTL_Q1_Interrupt_Control_Status register to get the exact cause of the<br>interrupt and clear its source.<br>0b - Queue 1 Interrupt status not detected<br>1b - Queue 1 Interrupt status detected|
|0<br>Q0IS|Queue 0 Interrupt status This bit indicates that there is an interrupt from Queue 0. To reset this bit,<br>the application must read Queue 0 Interrupt Control and Status register to get the exact cause of the<br>interrupt and clear its source.<br>0b - Queue 0 Interrupt status not detected|
||1b - Queue 0 Interrupt status detected|



# 75.7.262 (MTL_RxQ_DMA_Map0) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RxQ_DMA_Map0|C30h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3907 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Function 

The Receive Queue and DMA Channel Mapping 0 register is reserved in EQOS-CORE and EQOS-MTL configurations. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3908-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv Reserved_Q3M<br>R Reserved_31_29  e... Reserved_27_y  DMA... Reserved_23_21  Q2DD Reserved_19_y  Q2MDMACH<br>MACH<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_15_13  Q1DD Reserved_11_y  Reserved_7_5  Q0DD Reserved_3_y<br>Q1MDMACH  Q0MDMACH<br>W MACH  MACH<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-29|Reserved.|
|Reserved_31_2<br>9||
|28|Reserved.|
|Reserved_Q3D<br>DMACH||
|27-26|Reserved.|
|Reserved_27_y||
|25-24|Reserved.|
|Reserved_Q3M<br>DMACH||
|23-21|Reserved.|
|Reserved_23_2<br>1||
|20<br>Q2DDMACH|Queue 2 Enabled for DA-based DMA Channel Selection When set, this bit indicates that the packets<br>received in Queue 2 are routed to a particular DMA channel as decided in the MAC Receiver based<br>on the DMA channel number programmed in the L3-L4 filter registers, or the Ethernet DA address.<br>When reset, this bit indicates that the packets received in Queue 2 are routed to the DMA Channel<br>programmed in the Q2MDMACH field (Bits[18:16]).<br>0b - Queue 2 disabled for DA-based DMA Channel Selection|
||1b - Queue 2 enabled for DA-based DMA Channel Selection|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3908 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field<br>19-18<br>Reserved_19_y|Function<br>Reserved.|
|---|---|
|17-16<br>Q2MDMACH|Queue 2 Mapped to DMA Channel This field controls the routing of the received packet in Queue 2 to the<br>DMA channel: - 000: DMA Channel 0 - 001: DMA Channel 1 - 010: DMA Channel 2 - 011: DMA Channel<br>3 - 100: DMA Channel 4 - 101: DMA Channel 5 - 110: DMA Channel 6 - 111: DMA Channel 7 This field<br>is valid when the Q2DDMACH field is reset.|
|15-13|Reserved.|
|Reserved_15_1<br>3||
|12<br>Q1DDMACH|Queue 1 Enabled for DA-based DMA Channel Selection When set, this bit indicates that the packets<br>received in Queue 1 are routed to a particular DMA channel as decided in the MAC Receiver based<br>on the DMA channel number programmed in the L3-L4 filter registers, or the Ethernet DA address.<br>When reset, this bit indicates that the packets received in Queue 1 are routed to the DMA Channel<br>programmed in the Q1MDMACH field (Bits[10:8]).<br>0b - Queue 1 disabled for DA-based DMA Channel Selection<br>1b - Queue 1 enabled for DA-based DMA Channel Selection|
|11-10<br>Reserved_11_y|Reserved.|
|9-8<br>Q1MDMACH|Queue 1 Mapped to DMA Channel This field controls the routing of the received packet in Queue 1 to the<br>DMA channel: - 000: DMA Channel 0 - 001: DMA Channel 1 - 010: DMA Channel 2 - 011: DMA Channel<br>3 - 100: DMA Channel 4 - 101: DMA Channel 5 - 110: DMA Channel 6 - 111: DMA Channel 7 This field<br>is valid when the Q1DDMACH field is reset. The width of this field depends on the number of RX DMA<br>channels and not all the values might be valid in some configurations. For example, if the number of RX<br>DMA channels selected is 2, only 000 and 001 are valid, the other bits are reserved.|
|7-5<br>Reserved_7_5|Reserved.|
|4<br>Q0DDMACH|Queue 0 Enabled for DA-based DMA Channel Selection When set, this bit indicates that the packets<br>received in Queue 0 are routed to a particular DMA channel as decided in the MAC Receiver based<br>on the DMA channel number programmed in the L3-L4 filter registers, or the Ethernet DA address.<br>When reset, this bit indicates that the packets received in Queue 0 are routed to the DMA Channel<br>programmed in the Q0MDMACH field.<br>0b - Queue 0 disabled for DA-based DMA Channel Selection<br>1b - Queue 0 enabled for DA-based DMA Channel Selection|
|3-2|Reserved.|
|Reserved_3_y||
|1-0<br>Q0MDMACH|Queue 0 Mapped to DMA Channel This field controls the routing of the packet received in Queue 0 to the<br>DMA channel: - 000: DMA Channel 0 - 001: DMA Channel 1 - 010: DMA Channel 2 - 011: DMA Channel|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3909 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||3 - 100: DMA Channel 4 - 101: DMA Channel 5 - 110: DMA Channel 6 - 111: DMA Channel 7 This field|
||is valid when the Q0DDMACH field is reset. The width of this field depends on the number of RX DMA|
||channels and not all the values might be valid in some configurations. For example, if the number of RX|
||DMA channels selected is 2, only 000 and 001 are valid, the other bits are reserved.|



# 75.7.263 (MTL_TBS_CTRL) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TBS_CTRL|C40h|



## Function 

This register controls the operation of Time Based Scheduling. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3910-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>LEOS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv<br>R Reserved_3_2<br>LEOS  e... LEGOS  LEOV  ESTM<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-8<br>LEOS|Launch Expiry Offset The value in units of 256 nanoseconds that has to be added to the Launch time<br>to compute the Launch Expiry time. Value valid only when LEOV is set. Max value: 999,999,999 ns,<br>additionally should be smaller than CTR-1 value when ESTM mode is set since this value is a modulo<br>CTR value.|
|7|Reserved.|
|Reserved_7||
|6-4<br>LEGOS|Launch Expiry GSN Offset The number GSN slots that has to be added to the Launch GSN to compute<br>the Launch Expiry time. Value valid only when LEOV is set.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3910 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|3-2|Reserved.|
|Reserved_3_2||
|1<br>LEOV|Launch Expiry Offset Valid When set indicates the LEOS field is valid. When not set, indicates the<br>Launch Expiry Offset is not valid and the MTL must not check for Launch expiry time.<br>0b - LEOS field is invalid<br>1b - LEOS field is valid|
|0<br>ESTM|EST offset Mode When this bit is set, the Launch Time value used in Time Based Scheduling is<br>interpreted as an EST offset value and is added to the Base Time Register (BTR) of the current list.<br>When reset, the Launch Time value is used as an absolute value that should be compared with the<br>System time [39:8].|
||0b - EST offset Mode is disabled<br>1b - EST offset Mode is enabled|



# 75.7.264 (MTL_EST_Control) 

## Offset 

|Register|Offset|
|---|---|
|MTL_EST_Control|C50h|



## Function 

This register controls the operation of Enhancements to Scheduled Transmission (IEEE802.1Qbv). 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||P|TOV|||||||CT|OV||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||CTO|V||Reserv<br>e...||TILS||LCS|E|DFBS|DDBF|QHLB<br>F|Reserv<br>e...|SSWL|EEST|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3911 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-24<br>PTOV|PTP Time Offset Value The value of PTP Clock period multiplied by 6 in nanoseconds. This value is<br>needed to avoid transmission overruns at the beginning of the installation of a new GCL.|
|23-12<br>CTOV|Current Time Offset Value Provides a 12 bit time offset value in nano second that is added to the current<br>time to compensate for all the implementation pipeline delays such as the CDC sync delay, buffering<br>delays, data path delays and so on. This offset helps to ensure that the impact of gate controls is visible<br>on the line exactly at the pre-determined schedule (or as close to the schedule as possible).|
|11|Reserved.|
|Reserved_11||
|10-8<br>TILS|Time Interval Left Shift Amount This field provides the left shift amount for the programmed Time Interval<br>values used in the Gate Control Lists. - 000: No left shift needed (equal to x1ns) - 001: Left shift TI<br>by 1 bit (equal to x2ns) - 010: Left shift TI by 2 bits (equal to x4ns) - . - . - 100: Left shift TI by 7<br>bits (equal to x128ns) Based on the configuration one or more bits of this field should be treated as<br>Reserved/Read-Only.|
|7-6<br>LCSE|Loop Count to report Scheduling Error Programmable number of GCL list iterations before reporting an<br>HLBS error defined in EST_Status register.<br>00b - 4 iterations<br>01b - 8 iterations<br>10b - 16 iterations<br>11b - 32 iterations|
|5<br>DFBS|Drop Frames causing Scheduling Error When set frames reported to cause HOL Blocking due to not<br>getting scheduled (HLBS field of EST_Status register) after 4,8,16,32 (based on LCSE field of this<br>register) GCL iterations are dropped.<br>0b - Do not Drop Frames causing Scheduling Error<br>1b - Drop Frames causing Scheduling Error|
|4<br>DDBF|Do not Drop frames during Frame Size Error When set, frames are not be dropped during Head-of-Line<br>blocking due to Frame Size Error (HLBF field of EST_Status register).<br>0b - Drop frames during Frame Size Error<br>1b - Do not Drop frames during Frame Size Error|
|3<br>QHLBF|Quick Assertion of HLBF Error When set, Time Window for Head-of-Line blocking due to Frame Size<br>Error is 1 to 2 loop count of GCL list.On reset,Time Window for Head-of-Line blocking due to Frame Size<br>Error is 2 to 3 loop counts of GCL list.<br>0b - Disable Quick assertion of HLBF error<br>1b - Quick Assertion of HLBF Error|
|2<br>Reserved_2|Reserved.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3912 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|1<br>SSWL|Switch to S/W owned list When set indicates that the software has programmed that list that it currently<br>owns (SWOL) and the hardware should switch to the new list based on the new BTR. Hardware clears<br>this bit when the switch to the SWOL happens to indicate the completion of the switch or when an BTR<br>error (BTRE in Status register) is set. When BTRE is set this bit is cleared but SWOL is not updated as<br>the switch was not successful. Access restriction applies. Setting 1 sets. Self-cleared. Setting 0 has no<br>effect.<br>0b - Switch to S/W owned list is disabled<br>1b - Switch to S/W owned list is enabled|
|0<br>EEST|Enable EST When reset, the gate control list processing is halted and all gates are assumed to<br>be in Open state. Should be set for the hardware to start processing the gate control lists. During<br>the toggle from 0 to 1, the gate control list processing starts only after the SSWL bit it set. When<br>DWC_EQOS_ASP_ECC is selected during the configuration, if any uncorrectable error is detected in the<br>EST memory the hardware resets this bit and disables the EST function.<br>0b - EST is disabled<br>1b - EST is enabled|



# 75.7.265 (MTL_EST_Ext_Control) 

## Offset 

|Register|Offset|
|---|---|
|MTL_EST_Ext_Control|C54h|



## Function 

This register indicates the number of Overhead bytes for EST related scheduling. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||Reserve|d_31_6||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||||Reserve|d_31_6|||||||OVH|D|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3913 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-6|Reserved.|
|Reserved_31_6||
|5-0<br>OVHD|Overhead Bytes Value This field indicates the fixed overhead for every packet to account for EST<br>Scheduler Delay, IPG or EIPG, and Preamble bytes.|



# 75.7.266 (MTL_EST_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_EST_Status|C58h|



## Function 

This register provides Status related to Enhancements to Scheduled Transmission (IEEE802.1Qbv). 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3914-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_20  CGSN<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R BTRL  SWOL  Reserved_6_5  HLBS  HLBF<br>CGCE  BTRE  SWLC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-20|Reserved.|
|Reserved_31_2<br>0||
|19-16<br>CGSN|Current GCL Slot Number Indicates the slot number of the GCL list. Slot number is a modulo 16 count of<br>the GCL List loops executed so far. Even if a new GCL list is installed, the count is incremental.|
|15-8|BTR Error Loop Count Provides the minimum count (N) for which the equation Current Time =< New<br>BTR + (N * New Cycle Time) becomes true. N = "11111111" indicates the iterations exceeded the value|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3914 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field<br>BTRL|Function<br>of 128 and the hardware was not able to update New BTR to be equal to or greater than Current Time.<br>Software intervention is needed to update the New BTR. Value cleared when BTRE field of this register<br>is cleared.|
|---|---|
|7<br>SWOL|S/W owned list When '0' indicates Gate control list number "0" is owned by software and when "1"<br>indicates the Gate Control list "1" is owned by the software. Any reads/writes by the software (using<br>indirect access through GCL_Control) is directed to the list indicated by this value by default. The inverse<br>of this value is treated as HWOL. R/W operations performed by hardware are directed to the list pointed<br>by HWOL by default.<br>0b - Gate control list number "0" is owned by software<br>1b - Gate control list number "1" is owned by software|
|6-5|Reserved.|
|Reserved_6_5||
|4<br>CGCE|Constant Gate Control Error This error occurs when the list length (LLR) is 1 and the Cycle Time (CTR)<br>is less than or equal to the programmed Time Interval (TI) value after the optional Left Shifting. This<br>implies, Gates are either always Closed or always Open based on the Gate Control values; the same<br>effect can be achieved by other simpler (non TSN) programming mechanisms. Since the implementation<br>does not support such a programming an error is reported. Access restriction applies. Self-set to 1 on<br>internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - Constant Gate Control Error not detected<br>1b - Constant Gate Control Error detected|
|3<br>HLBS|Head-Of-Line Blocking due to Scheduling Set when the frame is not able to win arbitration and get<br>scheduled even after 4 iterations of the GCL. Indicates to software a potential programming error. The<br>one hot encoded values of the Queue Numbers that are not able to make progress are indicated in the<br>MTL_EST_Sch_Error register. Bit cleared when MTL_EST_Sch_Error register is all zeros.<br>0b - Head-Of-Line Blocking due to Scheduling not detected<br>1b - Head-Of-Line Blocking due to Scheduling detected|
|2<br>HLBF|Head-Of-Line Blocking due to Frame Size Set when HOL Blocking is noticed on one or more Queues as<br>a result of none of the Time Intervals of gate open in the GCL being greater than or equal to the duration<br>needed for frame size (or frame fragment size when preemption is enabled) transmission. The one hot<br>encoded Queue numbers that are experiencing HLBF are indicated in the MTL_EST_Frm_Size_Error<br>register. Additionally, the first Queue number that experienced HLBF along with the frame size is<br>captured in MTL_EST_Frm_Size_Capture register. Bit cleared when MTL_EST_Frame_Size_ Error<br>register is all zeros.<br>0b - Head-Of-Line Blocking due to Frame Size not detected<br>1b - Head-Of-Line Blocking due to Frame Size detected|
|1<br>BTRE|BTR Error When "1" indicates a programming error in the BTR of SWOL where the programmed value is<br>less than current time. If the BTRL = "11111111", SWOL is not updated and software should reprogram<br>the BTR to a value greater than current time and then set SSWL to reinitiate the switch to SWOL. Else<br>if the value of BTRL < "11111111", SWOL is updated and this field indicates the number of iterations|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3915 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||(of + CycleTime) taken by hardware to update the BTR to a value greater than Current Time. Access<br>restriction applies. Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - BTR Error not detected<br>1b - BTR Error detected|
|0<br>SWLC|Switch to S/W owned list Complete When "1" indicates the hardware has successfully switched to the<br>SWOL, and the SWOL bit has been updated to that effect. Cleared when the SSWL of EST_Control<br>register transitions from 0 to 1, or on a software write. Access restriction applies. Self-set to 1 on internal<br>event. Setting 1 clears. Setting 0 has no effect.<br>0b - Switch to S/W owned list Complete not detected<br>1b - Switch to S/W owned list Complete detected|



# 75.7.267 (MTL_EST_Sch_Error) 

## Offset 

|Register|Offset|
|---|---|
|MTL_EST_Sch_Error|C60h|



## Function 

This register provides the One Hot encoded Queue Numbers that are having the Scheduling related error (timeout). 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||Reserve|d_31_x||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||Res|erved_3|1_x|||||||SEQN||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function||
|---|---|---|
|31-3|Reserved.||
|Reserved_31_x|||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3916 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|2-0|Schedule Error Queue Number The One Hot Encoded Queue Numbers that have experienced error/|
|SEQN|timeout described in HLBS field of status register. Access restriction applies. Self-set to 1 on internal<br>event. Setting 1 clears. Setting 0 has no effect.|



# 75.7.268 (MTL_EST_Frm_Size_Error) 

Offset 

|Register|Offset|
|---|---|
|MTL_EST_Frm_Size_Err|C64h|
|or||



## Function 

This register provides the One Hot encoded Queue Numbers that are having the Frame Size related error. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||Reserve|d_31_x||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||Res|erved_3|1_x|||||||FEQN||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-3|Reserved.|
|Reserved_31_x||
|2-0<br>FEQN|Frame Size Error Queue Number The One Hot Encoded Queue Numbers that have experienced error<br>described in HLBF field of status register. Access restriction applies. Self-set to 1 on internal event.<br>Setting 1 clears. Setting 0 has no effect.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3917 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.269 (MTL_EST_Frm_Size_Capture) 

## Offset 

|Register|Offset|
|---|---|
|MTL_EST_Frm_Size_Ca|C68h|
|pture||



## Function 

This register captures the Frame Size and Queue Number of the first occurrence of the Frame Size related error. Up on clearing it captures the data of immediate next occurrence of a similar error. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3918-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_x  HBFQ<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv<br>R HBFS<br>e...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-18|Reserved.|
|Reserved_31_x||
|17-16<br>HBFQ|Queue Number of HLBF Captures the binary value of the of the first Queue (number) experiencing HLBF<br>error (see HLBF field of status register). Value once written is not altered by any subsequent queue<br>errors of similar nature. Once cleared the queue number of the next occurring HLBF error is captured.<br>Width is based on the number of Tx Queues configured; remaining bits are Read-Only. Cleared when<br>MTL_EST_Frm_Size_Error register is all zeros.|
|15|Reserved.|
|Reserved_15||
|14-0<br>HBFS|Frame Size of HLBF Captures the Frame Size of the dropped frame related to queue number indicated<br>in HBFQ field of this register. Contents of this register should be considered invalid, if this field is zero.<br>Cleared when MTL_EST_Frm_Size_Error register is all zeros.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3918 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.270 (MTL_EST_Intr_Enable) 

## Offset 

|Register|Offset|
|---|---|
|MTL_EST_Intr_Enable|C70h|



## Function 

This register implements the Interrupt Enable bits for the various events that generate an interrupt. Bit positions have a 1 to 1 correlation with the status bit positions in MTL_ETS_Status register. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||Reserve|d_31_5||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||||Res|erved_31|_5|||||CGCE|IEHS|IEHF|IEBE|IECC|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-5|Reserved.|
|Reserved_31_5||
|4<br>CGCE|Interrupt Enable for CGCE When set, generates interrupt when the Constant Gate Control Error occurs<br>and is indicated in the status. When reset this event does not generate an interrupt<br>0b - Interrupt for CGCE is disabled<br>1b - Interrupt for CGCE is enabled|
|3<br>IEHS|Interrupt Enable for HLBS When set, generates interrupt when the Head-of-Line Blocking due to<br>Scheduling issue and is indicated in the status. When reset this event does not generate an interrupt.<br>0b - Interrupt for HLBS is disabled<br>1b - Interrupt for HLBS is enabled|
|2<br>IEHF|Interrupt Enable for HLBF When set, generates interrupt when the Head-of-Line Blocking due to Frame<br>Size error occurs and is indicated in the status. When reset this event does not generate an interrupt.<br>0b - Interrupt for HLBF is disabled<br>1b - Interrupt for HLBF is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3919 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|1<br>IEBE|Interrupt Enable for BTR Error When set, generates interrupt when the BTR Error occurs and is indicated<br>in the status. When reset this event does not generate an interrupt.<br>0b - Interrupt for BTR Error is disabled<br>1b - Interrupt for BTR Error is enabled|
|0<br>IECC|Interrupt Enable for Switch List When set, generates interrupt when the configuration change is<br>successful and the hardware has switched to the new list. When reset this event does not generate<br>an interrupt.<br>0b - Interrupt for Switch List is disabled<br>1b - Interrupt for Switch List is enabled|



# 75.7.271 (MTL_EST_GCL_Control) 

## Offset 

|Register|Offset|
|---|---|
|MTL_EST_GCL_Control|C80h|



## Function 

This register provides the control information for reading/writing to the Gate Control lists. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3920-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_24  ESTEI ESTEI ESTEI Reserved_20_y<br>W EC  AEE  EE<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserv<br>ADDR  Reserved_7_6  DBGB  DBGM  GCRR  R1W0  SRWO<br>W e...<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-24|Reserved.|
|Reserved_31_2<br>4||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3920 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|23<br>ESTEIEC|ECC Inject Error Control for EST Memory When ESTEIEE or ESTEIAEE bit of this register is set,<br>following are the errors inserted based on the value encoded in this field. This field is valid only if<br>DWC_EQOS_ASP_ECC feature is selected during the configuration, else it is reserved.<br>0b - Insert 1 bit error<br>1b - Insert 2 bit errors|
|22<br>ESTEIAEE|EST ECC Inject Address Error Enable When set along with EEST bit of MTL_EST_Control register,<br>enables the ECC address error injection feature. When reset, disables the ECC address error injection<br>feature.<br>0b - EST ECC Inject Address Error is disabled<br>1b - EST ECC Inject Address Error is enabled|
|21<br>ESTEIEE|EST ECC Inject Error Enable When set along with EEST bit of MTL_EST_Control register, enables the<br>ECC error injection feature. When reset, disables the ECC error injection feature.<br>0b - EST ECC Inject Error is disabled<br>1b - EST ECC Inject Error is enabled|
|20-16<br>Reserved_20_y|Reserved.|
|15-8<br>ADDR|Gate Control List Address: (GCLA when GCRR is "0"). Provides the address (row number) of the<br>Gate Control List at which the R/W operation has to be performed. By default the Gate Control List<br>pointed by SWOL of MTL_EST_Status is selected for R/W, however if the DBGM bit of this register<br>is set, a debug mode access is given to R/W from DBGB. The width of this field is dependent<br>on DWC_EQOS_EST_DEP; unused bits should be treated as read only. Gate Control List Related<br>Registers Address: (GCRA when GCRR is "1"). By default the GCL related register set pointed by SWOL<br>of MTL_EST_Status is selected for R/W, however if the DBGM bit of this register is set, a debug mode<br>access is given to R/W from DBGB. Lower 3 bits are only used in this mode, higher order bits are treated<br>as dont cares. - 000: BTR Low (31:0) - 001: BTR High (63:31) - 010: CTR Low (31:0) - 011: CTR High<br>(39:32) - 100: TER (31:0) - 101: LLR (n:0) (where n is (log{DWC_EQOS_EST_DEP} / log2)) - Others:<br>Reserved|
|7-6<br>Reserved_7_6|Reserved.|
|5<br>DBGB|Debug Mode Bank Select When set to "0" indicates R/W in debug mode should be directed to Bank 0<br>(GCL0 and corresponding Time related registers). When set to "1" indicates R/W in debug mode should<br>be directed to Bank 1 (GCL1 and corresponding Time related registers). This value is used when DBGM<br>is set and overrides by value of SWOL which is normally used.<br>0b - R/W in debug mode should be directed to Bank 0<br>1b - R/W in debug mode should be directed to Bank 1|
|4<br>DBGM|Debug Mode When set to "1" indicates R/W in debug mode where the memory bank (for GCL and Time<br>related registers) is explicitly provided by DBGB value, when set to "0" SWOL bit is used to determine<br>which bank to use.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3921 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Debug Mode is disabled<br>1b - Debug Mode is enabled|
|3<br>Reserved_3|Reserved.|
|2<br>GCRR|Gate Control Related Registers When set to "1" indicates the R/W access is for the GCL related registers<br>(BTR, CTR, TER, LLR) whose address is provided by GCRA. When "0" indicates R/W should be directed<br>to GCL from the address provided by GCLA.<br>0b - Gate Control Related Registers are disabled<br>1b - Gate Control Related Registers are enabled|
|1<br>R1W0|Read '1', Write '0': - 1: Read operation - 0: Write operation.<br>0b - Write Operation<br>1b - Read Operation|
|0<br>SRWO|Start Read/Write Op - 1: Indicates the start/progress of a Read/Write operation. - Reset by hardware:<br>Indicates the R/W operation has completed or an error has occurred (when bit 20 is set) - Reads: Data<br>can be read from MTL_EST_GCL_Data register after this bit is reset - Writes: MTL_EST_GCL_Data<br>should be programmed with write data before setting SRWO. Access restriction applies. Setting 1 sets.<br>Self-cleared. Setting 0 has no effect.<br>0b - Start Read/Write Op disabled<br>1b - Start Read/Write Op enabled|



# 75.7.272 (MTL_EST_GCL_Data) 

## Offset 

|Register|Offset|
|---|---|
|MTL_EST_GCL_Data|C84h|



## Function 

This register holds the read data or write data in case of reads and writes respectively. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3922 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3923-01.png)


<!-- Start of picture text -->
Gigabit Ethernet Media Access Controller (GMAC)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>GCD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>GCD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Diagram 

## Fields 

|Field|Function|
|---|---|
|31-0|Gate Control Data The data corresponding to the address selected in the GCL_Control register. Used for|
|GCD|both Read and Write operations.|



# 75.7.273 (MTL_FPE_CTRL_STS) 

## Offset 

|Register|Offset|
|---|---|
|MTL_FPE_CTRL_STS|C90h|



## Function 

This register controls the operation of, and provides status for Frame Preemption (IEEE802.1Qbu/802.3br). 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3923-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_29  HRS  Reserved_27_16<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_15_y  Reserved_7_2<br>PEC  AFSZ<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3923 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-29|Reserved.|
|Reserved_31_2<br>9||
|28<br>HRS|Hold/Release Status - 1: Indicates a Set-and-Hold-MAC operation was last executed and the pMAC is<br>in Hold State. - 0: Indicates a Set-and-Release-MAC operation was last executed and the pMAC is in<br>Release State.<br>0b - Indicates a Set-and-Release-MAC operation was last executed and the pMAC is in Release<br>State<br>1b - Indicates a Set-and-Hold-MAC operation was last executed and the pMAC is in Hold State|
|27-16|Reserved.|
|Reserved_27_1<br>6||
|15-11|Reserved.|
|Reserved_15_y||
|10-8<br>PEC|Preemption Classification When set indicates the corresponding Queue must be classified as<br>preemptable, when '0' Queue is classified as express. When both EST (Qbv) and Preemption are<br>enabled, Queue-0 is always assumed to be preemptable. When EST (Qbv) is enabled Queues<br>categorized as preemptable here are always assumed to be in "Open" state in the Gate Control List.|
|7-2|Reserved.|
|Reserved_7_2||
|1-0<br>AFSZ|Additional Fragment Size used to indicate, in units of 64 bytes, the minimum number of bytes over<br>64 bytes required in non-final fragments of preempted frames. The minimum non-final fragment size is<br>(AFSZ +1) * 64 bytes|



# 75.7.274 (MTL_FPE_Advance) 

## Offset 

|Register|Offset|
|---|---|
|MTL_FPE_Advance|C94h|



## Function 

This register holds the Hold and Release Advance time. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3924 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3925-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>RADV<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>HADV<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-16<br>RADV|Release Advance The maximum time in nanoseconds that can elapse between issuing a RELEASE to<br>the MAC and the MAC being ready to resume transmission of preemptable frames, in the absence of<br>there being any express frames available for transmission.|
|15-0<br>HADV|Hold Advance The maximum time in nanoseconds that can elapse between issuing a HOLD to the MAC<br>and the MAC ceasing to transmit any preemptable frame that is in the process of transmission or any<br>preemptable frames that are queued for transmission.|



# 75.7.275 (MTL_RXP_Control_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RXP_Control_Statu|CA0h|
|s||



## Function 

The MTL_RXP_Control_Status register establishes the operating mode of Rx Parser and provides some status. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19<br>18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|RXPI|ELIRS||||Reserve|d_29_x||||||NPE|||
|Reset|1|0|0|0|0|0|0|0|0|0|1|1|1<br>1|1|1|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3<br>2|1|0|
|R<br>W|||||Reserve|d_15_x|||||||NVE|||
|Reset|0|0|0|0|0|0|0|0|0|0|1|1|1<br>1|1|1|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3925 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31<br>RXPI|RX Parser in Idle state This status bit is set to 1 when the Rx parser is in Idle State and waiting for a new<br>packet for processing. This bit is used as a handshake with software when parser gets disables. After<br>disabling, when bit is set then software can update the Rx parser instruction table.<br>0b - RX Parser not in Idle state<br>1b - RX Parser in Idle state|
|30<br>ELIRS|Enable Last Instruction in RX Status When this bit is set, RDES2[31:16] indicates the index of the last<br>instruction excecuted in Rx Parse, when set to 0 indicates MAC filter status.|
|29-22<br>Reserved_29_x|Reserved.|
|21-16<br>NPE|Number of parsable entries in the Instruction table This control indicates the number of parsable<br>entries in the Instruction Memory. This is used in Rx parser logic to detect programming Error.<br>In case number of parsed entries for a packet is more than this entry then NPEOVIS bit in the<br>MTL_RXP_Interrupt_Control_Status register is set.|
|15-6|Reserved.|
|Reserved_15_x||
|5-0<br>NVE|Number of valid entry address/index in the Instruction table This control indicates the number of valid<br>entries address/index in the Instruction Memory (i.e. when NVE field in register=31, the maximum valid<br>entry address is NVE+1 i.e. addresses/indices=0 to 32, or 33 entries). This is used in Rx parser logic to<br>detect any programming Error. In case while parsing Table address (memory address) found to be more<br>than this maximum valid entry address then NVEOVIS bit in the MTL_RXP_Interrupt_Control_Status<br>register is set. Note: The minimum value of this should be 2.|



# 75.7.276 (MTL_RXP_Interrupt_Control_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RXP_Interrupt_Con|CA4h|
|trol_Status||



## Function 

The MTL_RXP_Interrupt_Control_Status registers provides enable control for the interrupts and provides interrupt status. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3926 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||Reserve|d_31_20||||||PDRFI|FOOVI|NPEO|NVEO|
|W|||||||||||||E|E|VIE|VIE|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||Reserve|d_15_4||||||PDRFI|FOOVI|NPEO|NVEO|
|W|||||||||||||S|S|VIS|VIS|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-20|Reserved.|
|Reserved_31_2<br>0||
|19<br>PDRFIE|Packet Drop due to RF Interrupt Enable When this bit is set, the PDRFIS interrupt is enabled. When this<br>bit is reset, the PDRFIS interrupt is disabled.<br>0b - Packet Drop due to RF Interrupt is disabled<br>1b - Packet Drop due to RF Interrupt is enabled|
|18<br>FOOVIE|Frame Offset Overflow Interrupt Enable When this bit is set, the FOOVIS interrupt is enabled. When this<br>bit is reset, the FOOVIS interrupt is disabled.<br>0b - Frame Offset Overflow Interrupt is disabled<br>1b - Frame Offset Overflow Interrupt is enabled|
|17<br>NPEOVIE|Number of Parsable Entries Overflow Interrupt Enable When this bit is set, the NPEOVIS interrupt is<br>enabled. When this bit is reset, the NPEOVIS interrupt is disabled.<br>0b - Number of Parsable Entries Overflow Interrupt is disabled<br>1b - Number of Parsable Entries Overflow Interrupt is enabled|
|16<br>NVEOVIE|Number of Valid Entries Overflow Interrupt Enable When this bit is set, the NVEOVIS interrupt is<br>enabled. When this bit is reset, the NVEOVIS interrupt is disabled.<br>0b - Number of Valid Entries Overflow Interrupt is disabled<br>1b - Number of Valid Entries Overflow Interrupt is enabled|
|15-4<br>Reserved_15_4|Reserved.|
|3<br>PDRFIS|Packet Dropped due to RF Interrupt Status If the Rx Parser result says to drop the packet by setting<br>RF=1 in the instruction memory, then this bit is set to 1. This bit is cleared when the application writes<br>1 to this bit. Access restriction applies. Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no<br>effect.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3927 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Packet Dropped due to RF Interrupt Status not detected<br>1b - Packet Dropped due to RF Interrupt Status detected|
|2<br>FOOVIS|Frame Offset Overflow Interrupt Status While parsing if the Instruction table entry's 'Frame Offset' found<br>to be more than EOF offset, then then this bit is set. This bit is cleared when the application writes 1<br>to this bit. Access restriction applies. Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no<br>effect.<br>0b - Frame Offset Overflow Interrupt Status not detected<br>1b - Frame Offset Overflow Interrupt Status detected|
|1<br>NPEOVIS|Number of Parsable Entries Overflow Interrupt Status While parsing a packet if the number of parsed<br>entries found to be more than NPE[] (Number of Parseable Entries in MTL_RXP_Control register),then<br>this bit is set to 1. This bit is cleared when the application writes 1 to this bit. Access restriction applies.<br>Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - Number of Parsable Entries Overflow Interrupt Status not detected<br>1b - Number of Parsable Entries Overflow Interrupt Status detected|
|0<br>NVEOVIS|Number of Valid Entry Address/Index Overflow Interrupt Status While parsing if the Instruction address<br>found to be more than NVE (Number of Valid Entry Address/index in MTL_RXP_Control register), then<br>this bit is set to 1. For example, when NVE field in register=31, the maximum valid entry address/index is<br>NVE+1 i.e. 32 (addresses/indices=0 to 32, or 33 entries), so NVEOVIS is set when currently processed<br>entry indicates next address is 33 or more i.e. 34th or later entries. This bit is cleared when the<br>application writes 1 to this bit. Access restriction applies. Self-set to 1 on internal event. Setting 1 clears.<br>Setting 0 has no effect.<br>0b - Number of Valid Entries Overflow Interrupt Status not detected<br>1b - Number of Valid Entries Overflow Interrupt Status detected|



# 75.7.277 (MTL_RXP_Drop_Cnt) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RXP_Drop_Cnt|CA8h|



## Function 

The MTL_RXP_Drop_Cnt register provides the drop count of Rx Parser initiated drops. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3928 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3929-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>RXPD<br>R RXPDC<br>COVF<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXPDC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31<br>RXPDCOVF|Rx Parser Drop Counter Overflow Bit When set, this bit indicates that the MTL_RXP_Drop_cnt (RXPDC)<br>Counter field crossed the maximum limit. Access restriction applies. Clears on read. Self-set to 1 on<br>internal event.|
||0b - Rx Parser Drop count overflow not occurred|
||1b - Rx Parser Drop count overflow occurred|
|30-0<br>RXPDC|Rx Parser Drop count This 31-bit counter is implemented when a Rx Parser Drops a packet due to RF<br>=1. The counter is cleared when the register is read.|



# 75.7.278 (MTL_RXP_Error_Cnt) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RXP_Error_Cnt|CACh|



## Function 

The MTL_RXP_Error_Cnt register provides the Rx Parser related error occurrence count. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3929 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3930-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>RXPE<br>R RXPEC<br>COVF<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXPEC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31<br>RXPECOVF|Rx Parser Error Counter Overflow Bit When set, this bit indicates that the MTL_RXP_Error_cnt (RXPEC)<br>Counter field crossed the maximum limit. Access restriction applies. Clears on read. Self-set to 1 on<br>internal event.|
||0b - Rx Parser Error count overflow not occurred|
||1b - Rx Parser Error count overflow occurred|
|30-0<br>RXPEC|Rx Parser Error count This 31-bit counter is implemented whenr a Rx Parser encounters following Error<br>scenarios - Entry address >= NVE[] - Number Parsed Entries >= NPE[] - Entry address > EOF data entry<br>address The counter is cleared when the register is read.|



# 75.7.279 (MTL_RXP_Indirect_Acc_Control_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RXP_Indirect_Acc_|CB0h|
|Control_Status||



## Function 

The MTL_RXP_Indirect_Acc_Control_Status register provides the Indirect Access control and status for Rx Parser memory. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3930 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|STAR||||Reserved|_30_23||||RXPEI|RXPEI|RXPEI|Rese|rved_19|_17|WRRD|
|W|TBU...|||||||||EC|AEE|EE||||N|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||Reserv|ed_15_x|||||||ADD|R||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31<br>STARTBUSY|FRP Instruction Table Access Busy - Set to 1 by the software, indicates to start the Read/Write operation<br>from/to the Rx Parser Memory. Software should read this bit as 0 before issuing read or write request to<br>access the Parser Memory Instructions. - Set to 1 by the IP, indicates that the IP is busy until it is cleared<br>by the IP. Software should not issue read or write operation.<br>0b - hardware not busy<br>1b - hardware is busy (Read/Write operation from/to the Rx Parser Memory)|
|30-23<br>Reserved_30_2<br>3|Reserved.|
|22<br>RXPEIEC|ECC Inject Error Control for Rx Parser Memory When RXPEIEE or RXPEIAEE bit of this register is set,<br>following are the errors inserted based on the value encoded in this field: - 1: Insert 1 bit error. - 0: Insert<br>2 bit errors.<br>0b - Insert 1 bit error<br>1b - Insert 2 bit errors|
|21<br>RXPEIAEE|ECC Inject Address Error Enable for Rx Parser Memory - 1: Enables the ECC address error injection<br>feature. - 0: Disables the ECC address error injection feature.<br>0b - ECC Inject Address Error for Rx Parser Memory is disabled<br>1b - ECC Inject Address Error for Rx Parser Memory is enabled|
|20<br>RXPEIEE|ECC Inject Error Enable for Rx Parser Memory - 1: Enables the ECC error injection feature. - 0: Disables<br>the ECC error injection feature.<br>0b - ECC Inject Error for Rx Parser Memory is disabled<br>1b - ECC Inject Error for Rx Parser Memory is enabled|
|19-17|Reserved.|
|Reserved_19_1<br>7||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3931 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|16<br>WRRDN|Read Write Control - 1: Indicates the write operation to the Rx Parser Memory. - 0: Indicates the read<br>operation to the Rx Parser Memory.<br>0b - Read operation to the Rx Parser Memory<br>1b - Write operation to the Rx Parser Memory|
|15-8|Reserved.|
|Reserved_15_x||
|7-0<br>ADDR|FRP Instruction Table Offset Address This field indicates the ADDR of the 32-bit entry in Rx parser<br>instruction table. Each entry has 128-bit (4x32-bit words). The X is based on the configurable<br>DWC_EQOS_FRP_ENTRIES. If DWC_EQOS_FRP_ENTRIES is - 256: X = 9 - 128: X = 8 - 64: X =<br>7|



# 75.7.280 (MTL_RXP_Indirect_Acc_Data) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RXP_Indirect_Acc_|CB4h|
|Data||



## Function 

The MTL_RXP_Indirect_Acc_Data registers holds the data associated to Indirect Access to Rx Parser memory. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||DA|TA||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||DA|TA||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|FRP Instruction Table Write/Read Data Software should write this register before issuing any write|
|DATA|command. The hardware provides the read data from the Rx Parser Memory for read operation when<br>STARTBUSY =0 after read command.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3932 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.281 (MTL_RXP_Bypass_Cnt) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RXP_Bypass_Cnt|CB8h|



## Function 

The MTL_RXP_Bypass_Cnt register provides the bypass count of Rx Parser. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3933-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>RXPB<br>R RXPBC<br>COF<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXPBC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31<br>RXPBCOF|Rx Parser bypass Counter Overflow Bit When set, this bit indicates that the MTL_RXP_Bypass_cnt<br>(RXPBC) Counter field crossed the maximum limit. Access restriction applies. Clears on read. Self-set to<br>1 on internal event.|
||0b - Rx Parser Bypass count overflow not occurred|
||1b - Rx Parser Bypass count overflow occurred|
|30-0<br>RXPBC|Rx Parser Bypass count This 31-bit counter is implemented when a Rx Parser bypass a packet due to<br>AF=1 and RF =1. The counter is cleared when the register is read.|



# 75.7.282 (MTL_ECC_Control) 

## Offset 

|Register|Offset|
|---|---|
|MTL_ECC_Control|CC0h|



## Function 

The MTL_ECC_Control register establishes the operating mode of ECC related to MTL memories. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3933 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3934-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_9<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv Reserv<br>R Reserved_31_9  MEEA Reserved_7_6  e... e... MRXP MEST MRXE MTXE<br>O  EE  EE  E  E<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-9|Reserved.|
|Reserved_31_9||
|8<br>MEEAO|MTL ECC Error Address Status Over-ride - 1: The EUEAS/ECEAS field of MTL_ECC_Err_Addr_Status<br>register holds the last valid address where the error is detected. - 0: The EUEAS/ECEAS field of<br>MTL_ECC_Err_Addr_Status register holds the first address where the error is detected.<br>0b - MTL ECC Error Address Status Over-ride is disabled<br>1b - MTL ECC Error Address Status Over-ride is enabled|
|7-6|Reserved.|
|Reserved_7_6||
|5|Reserved.|
|Reserved_DSC<br>EE||
|4|Reserved.|
|Reserved_TSO<br>EE||
|3<br>MRXPEE|MTL Rx Parser ECC Enable - 1: Enables the ECC feature for Rx Parser memory - 0: Disables the ECC<br>feature for Rx Parser memory<br>0b - MTL Rx Parser ECC is disabled<br>1b - MTL Rx Parser ECC is enabled|
|2<br>MESTEE|MTL EST ECC Enable - 1: Enables the ECC feature for EST memory - 0: Disables the ECC feature for<br>EST memory<br>0b - MTL EST ECC is disabled<br>1b - MTL EST ECC is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3934 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|1<br>MRXEE|MTL Rx FIFO ECC Enable - 1: Enables the ECC feature for MTL Rx FIFO memory. - 0: Disables the<br>ECC feature for MTL Rx FIFO memory.<br>0b - MTL Rx FIFO ECC is disabled|
||1b - MTL Rx FIFO ECC is enabled|
|0<br>MTXEE|MTL Tx FIFO ECC Enable - 1: Enables the ECC feature for MTL Tx FIFO memory - 0: Disables the ECC<br>feature for MTL Tx FIFO memory<br>0b - MTL Tx FIFO ECC is disabled|
||1b - MTL Tx FIFO ECC is enabled|



# 75.7.283 (MTL_Safety_Interrupt_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_Safety_Interrupt_St<br>atus|CC4h|



## Function 

The MTL_Safety_Interrupt_Status registers provides Safety interrupt status. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3935-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R Reserved_30_2<br>e...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_30_2  MEUIS MECIS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31|Reserved.|
||0b - MAC Safety Uncorrectable Interrupt Status not detected|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3935 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|Reserved_MCS<br>IS|1b - MAC Safety Uncorrectable Interrupt Status detected|
|30-2|Reserved.|
|Reserved_30_2||
|1<br>MEUIS|MTL ECC Uncorrectable error Interrupt Status This bit indicates that an uncorrectable error interrupt<br>event in the MTL ECC safety feature. To get the exact cause of the interrupt the application should read<br>the MTL_ECC_Interrupt_Status register.<br>0b - MTL ECC Uncorrectable error Interrupt Status not detected<br>1b - MTL ECC Uncorrectable error Interrupt Status detected|
|0<br>MECIS|MTL ECC Correctable error Interrupt Status This bit indicates that a correctable error interrupt event in<br>the MTL ECC safety feature. To get the exact cause of the interrupt the application should read the<br>MTL_ECC_Interrupt_Status register.<br>0b - MTL ECC Correctable error Interrupt Status not detected<br>1b - MTL ECC Correctable error Interrupt Status detected|



# 75.7.284 (MTL_ECC_Interrupt_Enable) 

## Offset 

|Register|Offset|
|---|---|
|MTL_ECC_Interrupt_Ena|CC8h|
|ble||



## Function 

The MTL_ECC_Interrupt_Enable register provides enable bits for the ECC interrupts. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3936-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_13<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_31_13  RPCEI Reserved_11_9  Reserved_7_5  RXCEI Reserved_3_1  TXCEI<br>ECEIE<br>E  E  E<br>W<br>Reset 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 1<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3936 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-13|Reserved.|
|Reserved_31_1<br>3||
|12<br>RPCEIE|Rx Parser memory Correctable Error Interrupt Enable When set, generates an interrupt when an<br>uncorrectable error is detected at the Rx Parser memory interface. It is indicated in RPCES status bit of<br>MTL_ECC_Interrupt_Status register. When reset this event does not generates an interrupt.<br>0b - Rx Parser memory Correctable Error Interrupt is disabled<br>1b - Rx Parser memory Correctable Error Interrupt is enabled|
|11-9|Reserved.|
|Reserved_11_9||
|8<br>ECEIE|EST memory Correctable Error Interrupt Enable When set, generates an interrupt when a<br>correctable error is detected at the MTL EST memory interface. It is indicated in the ECES bit of<br>MTL_ECC_Interrupt_Status register. When reset this event does not generates an interrupt.<br>0b - EST memory Correctable Error Interrupt is disabled<br>1b - EST memory Correctable Error Interrupt is enabled|
|7-5<br>Reserved_7_5|Reserved.|
|4<br>RXCEIE|Rx memory Correctable Error Interrupt Enable When set, generates an interrupt when a correctable<br>error is detected at the MTL Rx memory interface. It is indicated in the RXCES bit of<br>MTL_ECC_Interrupt_Status register. When reset this event does not generates an interrupt.<br>0b - Rx memory Correctable Error Interrupt is disabled<br>1b - Rx memory Correctable Error Interrupt is enabled|
|3-1|Reserved.|
|Reserved_3_1||
|0<br>TXCEIE|Tx memory Correctable Error Interrupt Enable When set, generates an interrupt when a correctable<br>error is detected at the MTL Tx memory interface. It is indicated in the TXCES bit of<br>MTL_ECC_Interrupt_Status register. When reset this event does not generates an interrupt.<br>0b - Tx memory Correctable Error Interrupt is disabled<br>1b - Tx memory Correctable Error Interrupt is enabled|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3937 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.285 (MTL_ECC_Interrupt_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_ECC_Interrupt_Stat|CCCh|
|us||



## Function 

The MTL_ECC_Interrupt_Status register provides MTL ECC Interrupt Status. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3938-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_15<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv Reserv Reserv Reserv<br>R<br>e... RPUE RPAM RPCE e... EUES  EAMS  ECES  e... RXUE RXAM RXCE e... TXUE TXAM TXCE<br>S  S  S  S  S  S  S  S  S<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-15|Reserved.|
|Reserved_31_1<br>5||
|14<br>RPUES|Rx Parser memory Uncorrectable Error Status When set, indicates that an uncorrectable error is<br>detected at Rx Parser memory interface.<br>0b - Rx Parser memory Uncorrectable Error Status not detected<br>1b - Rx Parser memory Uncorrectable Error Status detected|
|13<br>RPAMS|MTL Rx Parser memory Address Mismatch Status This bit when set indicates that address mismatch is<br>found for address bus of Rx Parser memory.<br>0b - MTL Rx Parser memory Address Mismatch Status not detected<br>1b - MTL Rx Parser memory Address Mismatch Status detected|
|12<br>RPCES|MTL Rx Parser memory Correctable Error Status This bit when set indicates that correctable error is<br>detected at RX Parser memory interface.<br>0b - MTL Rx Parser memory Correctable Error Status not detected|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3938 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function<br>1b - MTL Rx Parser memory Correctable Error Status detected|
|---|---|
|11<br>Reserved_11|Reserved.|
|10<br>EUES|MTL EST memory Uncorrectable Error Status When set, indicates that an uncorrectable error is detected<br>at MTL EST memory interface.<br>0b - MTL EST memory Uncorrectable Error Status not detected<br>1b - MTL EST memory Uncorrectable Error Status detected|
|9<br>EAMS|MTL EST memory Address Mismatch Status This bit when set indicates that address mismatch is found<br>for address bus of MTL EST memory.<br>0b - MTL EST memory Address Mismatch Status not detected<br>1b - MTL EST memory Address Mismatch Status detected|
|8<br>ECES|MTL EST memory Correctable Error Status This bit when set indicates that correctable error is detected<br>at the MTL EST memory.<br>0b - MTL EST memory Correctable Error Status not detected<br>1b - MTL EST memory Correctable Error Status detected|
|7<br>Reserved_7|Reserved.|
|6<br>RXUES|MTL Rx memory Uncorrectable Error Status When set, indicates that an uncorrectable error is detected<br>at the MTL Rx memory interface.<br>0b - MTL Rx memory Uncorrectable Error Status not detected<br>1b - MTL Rx memory Uncorrectable Error Status detected|
|5<br>RXAMS|MTL Rx memory Address Mismatch Status This bit when set indicates that address mismatch is found<br>for address bus of the MTL Rx memory.<br>0b - MTL Rx memory Address Mismatch Status not detected<br>1b - MTL Rx memory Address Mismatch Status detected|
|4<br>RXCES|MTL Rx memory Correctable Error Status This bit when set indicates that correctable error is detected at<br>the MTL Rx memory.<br>0b - MTL Rx memory correctable Error Status not detected<br>1b - MTL Rx memory correctable Error Status detected|
|3|Reserved.|
|Reserved_3||
|2<br>TXUES|MTL Tx memory Uncorrectable Error Status When set, indicates that an uncorrectable error is detected<br>at the MTL TX memory interface.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3939 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - MTL Tx memory Uncorrectable Error Status not detected<br>1b - MTL Tx memory Uncorrectable Error Status detected|
|1<br>TXAMS|MTL Tx memory Address Mismatch Status This bit when set indicates that address mismatch is found<br>for address bus of the MTL Tx memory.<br>0b - MTL Tx memory Address Mismatch Status not detected<br>1b - MTL Tx memory Address Mismatch Status detected|
|0<br>TXCES|MTL Tx memory Correctable Error Status This bit when set indicates that a correctable error is detected<br>at the MTL Tx memory.<br>0b - MTL Tx memory Correctable Error Status not detected|
||1b - MTL Tx memory Correctable Error Status detected|



# 75.7.286 (MTL_ECC_Err_Sts_Rctl) 

## Offset 

|Register|Offset|
|---|---|
|MTL_ECC_Err_Sts_Rctl|CD0h|



## Function 

The MTL_ECC_Err_Sts_Rctl register establishes the control for ECC Error status capture. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||Reserve|d_31_6||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||||Reserve|d_31_6|||||CUES|CCES||EMS||EESR<br>E|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function||
|---|---|---|
|31-6|Reserved.||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3940 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|Reserved_31_6||
|5<br>CUES|Clear Uncorrectable Error Status When this bit is set along with EESRE bit of this register, based on<br>the EMS field of this register, the respective memory's uncorrectable error address and uncorrectable<br>error count values are cleared upon reading. Hardware resets this bit when all the error status values are<br>cleared.<br>0b - Clear Uncorrectable Error Status not detected<br>1b - Clear Uncorrectable Error Status detected|
|4<br>CCES|Clear Correctable Error Status When this bit is set along with EESRE bit of this register, based on the<br>EMS field of this register, the respective memory's correctable error address and correctable error count<br>values are cleared upon reading. Hardware resets this bit when all the error status values are cleared.<br>0b - Clear Correctable Error Status not detected<br>1b - Clear Correctable Error Status detected|
|3-1<br>EMS|MTL ECC Memory Selection When EESRE bit of this register is set, this field indicates which memory's<br>error status value to be read. The memory selection encoding is as described.<br>000b - MTL Tx memory<br>001b - MTL Rx memory<br>010b - MTL EST memory<br>011b - MTL Rx Parser memory<br>100b - DMA TSO memory<br>101b - DMA DCACHE memory|
|0<br>EESRE|MTL ECC Error Status Read Enable When this bit is set, based on the EMS field of this register,<br>the respective memory's error status values are captured as described: - The correctable and<br>uncorrectable error count values are captured into MTL_ECC_Err_Cnt_Status register - The address<br>location's of correctable and uncorrectable errors are captured into MTL_ECC_Err_Addr_Status register.<br>Hardware resets this bit when all the status values are captured into the MTL_ECC_Err_Cnt_Status and<br>MTL_ECC_Err_Addr_Status registers.<br>0b - MTL ECC Error Status Read is disabled<br>1b - MTL ECC Error Status Read is enabled|



# 75.7.287 (MTL_ECC_Err_Addr_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_ECC_Err_Addr_Sta|CD4h|
|tus||



## Function 

The MTL_ECC_Err_Addr_Status register provides the memory addresses for the correctable and uncorrectable errors. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3941 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||EUE|AS||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||ECE|AS||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-16<br>EUEAS|MTL ECC Uncorrectable Error Address Status Based on the EMS field of MTL_ECC_Err_Sts_Rctl<br>register, this field holds the respective memory's address locations for which an uncorrectable error<br>or address mismatch is detected. - MEEAO field of MTL_ECC_Control register is 1: This field holds the<br>last valid address of memory for which either an uncorrectable error or an address mismatch is detected.<br>- MEEAO field of MTL_ECC_Control register is 0: This field holds the first address of the memory for<br>which either an uncorrectable error or address mismatch is detected.|
|15-0<br>ECEAS|MTL ECC Correctable Error Address Status Based on the EMS field of MTL_ECC_Err_Sts_Rctl register,<br>this field holds the respective memory's address locations for which a correctable error is detected. -<br>MEEAO field of MTL_ECC_Control register is 1: This field holds the last valid address of memory for<br>which correctable error or address mismatch is detected. - MEEAO field of MTL_ECC_Control register is<br>0: This field holds the first address of the memory for which correctable error is detected.|



# 75.7.288 (MTL_ECC_Err_Cntr_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_ECC_Err_Cntr_Stat|CD8h|
|us||



## Function 

The MTL_ECC_Err_Cntr_Status register provides ECC Error count for Correctable and uncorrectable errors. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3942 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||Reserve|d_31_20|||||||EU|ECS||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||Reserve|d_15_8|||||||ECE|CS||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-20|Reserved.|
|Reserved_31_2<br>0||
|19-16<br>EUECS|MTL ECC Uncorrectable Error Counter Status Based on the EMS field of MTL_ECC_Err_Cntr_Rctl<br>register, this field holds the respective memory's uncorrectable error count value.|
|15-8|Reserved.|
|Reserved_15_8||
|7-0<br>ECECS|MTL ECC Correctable Error Counter Status Based on the EMS field of MTL_ECC_Err_Cntr_Rctl register,<br>this field holds the respective memory's correctable error count value.|



# 75.7.289 (MTL_DPP_Control) 

## Offset 

|Register|Offset|
|---|---|
|MTL_DPP_Control|CE0h|



## Function 

The MTL_DPP_Control establishes the operating mode of Data Parity protection and error injection. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3943 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3944-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R Reserved_31_17<br>e...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv Reserv Reserv Reserv Reserv Reserv Reserv<br>R IPEMR IPEMT IPEMT IPERI IPEMT IPEMT IPETR OPE<br>e... e... e... e... e... e... e... EDPP<br>WC  FC  BU  D  S  F  D<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-17|Reserved.|
|Reserved_31_1<br>7||
|16|Reserved.|
|Reserved_IPED<br>C||
|15<br>IPEMRWC|0b - Insert Parity error in MTL RWC data parity checker is disabled<br>1b - Insert Parity error in MTL RWC data parity checker is enabled|
|14<br>IPEMTFC|Insert Parity error in MAC TFC data parity checker When set to 1, parity/data bit of first valid input parity/<br>data of the MAC TFC data parity checker (or at PC11 as shown in Transmit Data path parity protection<br>diagram) is flipped. Based on the EIM/BLEI field of MTL_DPP_ECC_EIC register, software can corrupt<br>any one bit of parity/data. Hardware clears this bit once respective parity bit is flipped.<br>0b - Insert Parity error in MAC TFC data parity checker is disabled<br>1b - Insert Parity error in MAC TFC data parity checker is enabled|
|13<br>IPEMTBU|Insert Parity error in MTL RWC data parity checker When set to 1, parity/data bit of first valid input parity/<br>data of the MTL RWC data parity checker (or at PC12 as shown in Recieve data path parity protection<br>diagram) is flipped. Based on the EIM/BLEI field of MTL_DPP_ECC_EIC register, software can corrupt<br>any one bit of parity/data. Hardware clears this bit once respective parity bit is flipped.<br>0b - Insert Parity error in MAC TBU data parity checker is disabled<br>1b - Insert Parity error in MAC TBU data parity checker is enabled|
|12|Reserved.|
|Reserved_IPEA<br>SR||
|11|Reserved.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3944 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field<br>Reserved_IPEM<br>SW|Function|
|---|---|
|10|Reserved.|
|Reserved_IPEA<br>SW||
|9<br>IPERID|Insert Parity Error in RX Interface Data parity checker When set to 1, parity/data bit of first valid input<br>parity/data of the RX Interface Data parity checker is (or at PC6 as shown in Receive data path parity<br>protection diagram) flipped. Based on the EIM/BLEI field of MTL_DPP_ECC_EIC register, software can<br>corrupt any one bit of parity/data. Following are the input data bus on which parity bits are generated<br>based on configuration selected In AHB Config, hwdata_o In AXI config, wdata_m_o In DMA Config,<br>mdc_wdata_o In MTL Config, ari_data_o Hardware clears this bit once respective parity bit is flipped.<br>0b - Insert Parity Error in Rx Interface Data parity checker is disabled<br>1b - Insert Parity Error in Rx Interface Data parity checker is enabled|
|8<br>IPEMTS|Insert Parity Error in MTL Tx Status FIFO parity checker When set to 1, parity/data bit of first valid input<br>parity/data of the MTL Tx Status FIFO parity checker (or at PC5 as shown in Transmit data path parity<br>protection diagram) is flipped. Based on the EIM/BLEI field of MTL_DPP_ECC_EIC register, software<br>can corrupt any one bit of parity/data. Hardware clears this bit once respective parity bit is flipped.<br>0b - Insert Parity Error in MTL TX Status FIFO parity checker is disabled<br>1b - Insert Parity Error in MTL TX Status FIFO parity checker is enabled|
|7<br>IPEMTF|Insert Parity Error in MTL Tx FIFO write data parity checker When set to 1, parity/data bit of first valid<br>input parity/data of the MTL Tx FIFO write data parity checker (or at PC4 as shown in Transmit data<br>path parity protection diagram) is flipped. Based on the EIM/BLEI field of MTL_DPP_ECC_EIC register,<br>software can corrupt any one bit of parity/data. Hardware clears this bit once respective parity bit is<br>flipped.<br>0b - Insert Parity Error in MTL Tx FIFO write data parity checker is disabled<br>1b - Insert Parity Error in MTL Tx FIFO write data parity checker is enabled|
|6<br>IPETRD|Insert Parity Error in DMA Tx/Rx Descriptor parity checker When set to 1, parity/data bit of first valid input<br>parity/data of the DMA Tx/Rx Descriptor parity checker (or at PC3 as shown in Transmit data path parity<br>protection diagram) is flipped. Based on the EIM/BLEI field of MTL_DPP_ECC_EIC register, software<br>can corrupt any one bit of parity/data. Hardware clears this bit once respective parity bit is flipped.<br>0b - Insert Parity Error in DMA Tx/Rx Descriptor parity checker is disabled<br>1b - Insert Parity Error in DMA Tx/Rx Descriptor parity checker is enabled|
|5<br>Reserved_IPET<br>H|Reserved.|
|4<br>Reserved_IPET<br>ID|Reserved.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3945 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|3|Reserved.|
|Reserved_3||
|2|Reserved.|
|Reserved_EPSI||
|1<br>OPE|Odd Parity Enable When set to 1, enables odd parity protection on all the external interfaces and when<br>set to 0, enables even parity protection on all the external interfaces.<br>0b - Odd Parity is disabled<br>1b - Odd Parity is enabled|
|0<br>EDPP|Enable Data path Parity Protection When set to 1, enables the parity protection for EQOS datapath by<br>generating and checking the parity on EQOS datapath. When set to 0, disables the parity protection for<br>EQOS datapath.<br>0b - Data path Parity Protection is disabled<br>1b - Data path Parity Protection is enabled|



# 75.7.290 (MTL_DPP_ECC_EIC) 

## Offset 

|Register|Offset|
|---|---|
|MTL_DPP_ECC_EIC|CE4h|



## Function 

The MTL_DPP_ECC_EIC establishes the operating mode of ECC/DPP error injection. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3946-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_17<br>EIM<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_15_8<br>BLEI<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3946 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-17|Reserved.|
|Reserved_31_1<br>7||
|16<br>EIM|Error Injection Mode When it set to 0, indicate error injection on data; When it set to 1, indicate error<br>injection on ECC/Parity bits(need to check the address error injection mode is disabled).|
|15-8|Reserved.|
|Reserved_15_8||
|7-0<br>BLEI|Bit Location of error injection This field indicates the bit location of DPP/ECC error injection,<br>determination of error in Parity/ECC bits or Data (being protected) depends on the Error Injection<br>Mode(EIM field). Depending on the interface being used for error injection not all bits of this field are<br>valid. Example, for error injection on a 64 bit data interface this field should be programmed to a value<br>between 63 and 0. In case of 2-bit error injection bit 0 is always included in error injection and this field<br>should represent the second bit selection for error injection.If the second bit is programed at bit 0 when<br>2-bit error injection is enabled, DUT only insert 1-bit error at bit 0.|



# 75.7.291 (MTL_TxQ0_Operation_Mode) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ0_Operation_M|D00h|
|ode||



## Function 

The Queue 0 Transmit Operation Mode register establishes the Transmit queue operating modes and commands. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3947-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_y<br>TQS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_15_7<br>TTC  TXQEN  TSF  FTQ<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3947 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-22<br>Reserved_31_y|Reserved.|
|21-16<br>TQS|Transmit Queue Size This field indicates the size of the allocated Transmit queues in blocks of 256<br>bytes. The TQS field is read-write only if the number of Tx Queues more than one, the reset value is<br>0x0 and indicates size of 256 bytes. This means that value of 0x0 = 256 bytes, 0x1 = 512 bytes and so<br>on. So, program TQS [5:0] = 6'b001111 to allocate queue size of 4096 (4K) bytes. In general, the size<br>of the Queue = (TQS+1)*256 bytes. When the number of Tx Queues is one, the field is read-only and<br>the configured TX FIFO size in blocks of 256 bytes is reflected in the reset value. The width of this field<br>depends on the Tx memory size selected in your configuration. For example, if the memory size is 2048,<br>the width of this field is 3 bits: LOG2(2048/256) = LOG2(8) = 3 bits|
|15-7<br>Reserved_15_7|Reserved.|
|6-4<br>TTC|Transmit Threshold Control These bits control the threshold level of the MTL Tx Queue. The<br>transmission starts when the packet size within the MTL Tx Queue is larger than the threshold. In<br>addition, full packets with length less than the threshold are also transmitted. These bits are used only<br>when the TSF bit is reset.<br>000b - 32<br>001b - 64<br>010b - 96<br>011b - 128<br>100b - 192<br>101b - 256<br>110b - 384<br>111b - 512|
|3-2<br>TXQEN|Transmit Queue Enable This field is used to enable/disable the transmit queue 0. - 2'b00: Not<br>enabled - 2'b01: Reserved - 2'b10: Enabled - 2'b11: Reserved This field is Read Only in Single<br>Queue configurations and Read Write in Multiple Queue configurations. Note: In multiple Tx queues<br>configuration, all the queues are disabled by default. Enable the Tx queue by programming this field.<br>00b - Not enabled<br>01b - Enable in AV mode (Reserved in non-AV)<br>10b - Enabled<br>11b - Reserved|
|1<br>TSF|Transmit Store and Forward When this bit is set, the transmission starts when a full packet resides in the<br>MTL Tx queue. When this bit is set, the TTC values specified in Bits[6:4] of this register are ignored. This<br>bit should be changed only when the transmission is stopped.<br>0b - Transmit Store and Forward is disabled<br>1b - Transmit Store and Forward is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3948 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|0<br>FTQ|Flush Transmit Queue When this bit is set, the Tx queue controller logic is reset to its default values.<br>Therefore, all the data in the Tx queue is lost or flushed. This bit is internally reset when the flushing<br>operation is complete. Until this bit is reset, you should not write to the MTL_TxQ1_Operation_Mode<br>register. The data which is already accepted by the MAC transmitter is not flushed. It is scheduled<br>for transmission and results in underflow and runt packet transmission. Note: The flush operation is<br>complete only when the Tx queue is empty and the application has accepted the pending Tx Status of<br>all transmitted packets. To complete this flush operation, the PHY Tx clock (clk_tx_i) should be active.<br>Access restriction applies. Setting 1 sets. Self-cleared. Setting 0 has no effect.<br>0b - Flush Transmit Queue is disabled|
||1b - Flush Transmit Queue is enabled|



# 75.7.292 (MTL_TxQ0_Underflow) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ0_Underflow|D04h|



## Function 

The Queue 0 Underflow Counter register contains the counter for packets aborted because of Transmit queue underflow and packets missed because of Receive queue packet flush 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3949-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_12<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>UFCN<br>R Reserved_31_12  UFFRMCNT<br>TOVF<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-12|Reserved.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3949 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|Reserved_31_1<br>2||
|11<br>UFCNTOVF|Overflow Bit for Underflow Packet Counter This bit is set every time the Tx queue Underflow Packet<br>Counter field overflows, that is, it has crossed the maximum count. In such a scenario, the overflow<br>packet counter is reset to all-zeros and this bit indicates that the rollover happened. Access restriction<br>applies. Clears on read. Self-set to 1 on internal event.<br>0b - Overflow not detected for Underflow Packet Counter<br>1b - Overflow detected for Underflow Packet Counter|
|10-0<br>UFFRMCNT|Underflow Packet Counter This field indicates the number of packets aborted by the controller because<br>of Tx Queue Underflow. This counter is incremented each time the MAC aborts outgoing packet because<br>of underflow. The counter is cleared when this register is read with mci_be_i[0] at 1'b1. Access restriction<br>applies. Clears on read. Self-set to 1 on internal event.|



# 75.7.293 (MTL_TxQ0_Debug) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ0_Debug|D08h|



## Function 

The Queue 0 Transmit Debug register gives the debug status of various blocks related to the Transmit queue. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3950-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R Reserved_31_23  STXSTSF  PTXQ<br>e...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>TXSTS TXQS TWCS TXQP<br>R Reserved_15_6  TRCSTS<br>FS... TS  TS  AUS...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3950 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field<br>31-23<br>Reserved_31_2<br>3|Function<br>Reserved.|
|---|---|
|22-20<br>STXSTSF|Number of Status Words in Tx Status FIFO of Queue This field indicates the current number of status in<br>the Tx Status FIFO of this queue. When the DTXSTS bit of MTL_Operation_Mode register is set to 1, this<br>field does not reflect the number of status words in Tx Status FIFO.|
|19<br>Reserved_19|Reserved.|
|18-16<br>PTXQ|Number of Packets in the Transmit Queue This field indicates the current number of packets in the Tx<br>Queue. When the DTXSTS bit of MTL_Operation_Mode register is set to 1, this field does not reflect the<br>number of packets in the Transmit queue.|
|15-6|Reserved.|
|Reserved_15_6||
|5<br>TXSTSFSTS|MTL Tx Status FIFO Full Status When high, this bit indicates that the MTL Tx Status FIFO is full.<br>Therefore, the MTL cannot accept any more packets for transmission.<br>0b - MTL Tx Status FIFO Full status is not detected<br>1b - MTL Tx Status FIFO Full status is detected|
|4<br>TXQSTS|MTL Tx Queue Not Empty Status When this bit is high, it indicates that the MTL Tx Queue is not empty<br>and some data is left for transmission.<br>0b - MTL Tx Queue Not Empty status is not detected<br>1b - MTL Tx Queue Not Empty status is detected|
|3<br>TWCSTS|MTL Tx Queue Write Controller Status When high, this bit indicates that the MTL Tx Queue Write<br>Controller is active, and it is transferring the data to the Tx Queue.<br>0b - MTL Tx Queue Write Controller status is not detected<br>1b - MTL Tx Queue Write Controller status is detected|
|2-1<br>TRCSTS|MTL Tx Queue Read Controller Status This field indicates the state of the Tx Queue Read Controller:<br>00b - Idle state<br>01b - Read state (transferring data to the MAC transmitter)<br>10b - Waiting for pending Tx Status from the MAC transmitter<br>11b - Flushing the Tx queue because of the Packet Abort request from the MAC|
|0<br>TXQPAUSED|Transmit Queue in Pause When this bit is high and the Rx flow control is enabled, it indicates that the Tx<br>Queue is in the Pause condition (in the full-duplex only mode) because of the following: - Reception of<br>the PFC packet for the priorities assigned to the Tx Queue when PFC is enabled - Reception of 802.3x<br>Pause packet when PFC is disabled<br>0b - Transmit Queue in Pause status is not detected|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3951 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - Transmit Queue in Pause status is detected|



# 75.7.294 (MTL_TxQ0_ETS_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ0_ETS_Status|D14h|



## Function 

The Queue 0 ETS Status register provides the average traffic transmitted in Queue 0. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||Reserve|d_31_24|||||||AB|S||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||AB|S||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-24|Reserved.|
|Reserved_31_2<br>4||
|23-0<br>ABS|Average Bits per Slot This field contains the average transmitted bits per slot. When the DCB operation<br>is enabled for Queue 0, this field is computed over every 10 million bit times slot (4 ms in 2500 Mbps; 10<br>ms in 1000 Mbps; 100 ms in 100 Mbps). The maximum value is 0x989680.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3952 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.295 (MTL_TxQ0_Quantum_Weight) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ0_Quantum_W|D18h|
|eight||



## Function 

The Queue 0 Quantum or Weights register contains the quantum value for Deficit Weighted Round Robin (DWRR), weights for the Weighted Round Robin (WRR), and Weighted Fair Queuing (WFQ) for Queue 0. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3953-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_21<br>ISCQW<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>ISCQW<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-21|Reserved.|
|Reserved_31_2<br>1||
|20-0<br>ISCQW|Quantum or Weights When the DCB operation is enabled with DWRR algorithm for Queue 0 traffic, this<br>field contains the quantum value in bytes to be added to credit during every queue scanning cycle. The<br>maximum value is 0x1312D0 bytes. When DCB operation is enabled with WFQ algorithm for Queue<br>0 traffic, this field contains the weight for this queue. The maximum value is 0x3FFF where weight of<br>0 indicates 100% bandwidth. Bits[20:14] must be written to zero. The higher the programmed weights<br>lesser the bandwidth allocated for the particular Transmit Queue. This is because the weights are used<br>to compute the packet finish time (weights * packet_size). Lesser the finish time, higher the probability of<br>the packet getting scheduled first and using more bandwidth. When DCB operation or generic queuing<br>operation is enabled with WRR algorithm for Queue 0 traffic, this field contains the weight for this queue.<br>The maximum value is 0x64. Bits [20:7] must be written to zero.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3953 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.296 (MTL_Q0_Interrupt_Control_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_Q0_Interrupt_Contr|D2Ch|
|ol_Status||



## Function 

This register contains the interrupt enable and status bits for the queue 0 interrupts. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||Res|erved_31|_25|||RXOIE|||Res|erved_23|_17|||RXOV|
|W||||||||||||||||FIS|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||Reserve|d_15_10|||ABPSI|TXUIE|||Reserve|d_7_2|||ABPSI|TXUN|
|W|||||||E||||||||S|FIS|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-25|Reserved.|
|Reserved_31_2<br>5||
|24<br>RXOIE|Receive Queue Overflow Interrupt Enable When this bit is set, the Receive Queue Overflow interrupt is<br>enabled. When this bit is reset, the Receive Queue Overflow interrupt is disabled.<br>0b - Receive Queue Overflow Interrupt is disabled<br>1b - Receive Queue Overflow Interrupt is enabled|
|23-17|Reserved.|
|Reserved_23_1<br>7||
|16<br>RXOVFIS|Receive Queue Overflow Interrupt Status This bit indicates that the Receive Queue had an overflow<br>while receiving the packet. If a partial packet is transferred to the application, the overflow status is set<br>in RDES3[21]. This bit is cleared when the application writes 1 to this bit. Access restriction applies.<br>Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - Receive Queue Overflow Interrupt Status not detected<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3954 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - Receive Queue Overflow Interrupt Status detected|
|15-10|Reserved.|
|Reserved_15_1<br>0||
|9<br>ABPSIE|Average Bits Per Slot Interrupt Enable When this bit is set, the MAC asserts the sbd_intr_o or mci_intr_o<br>interrupt when the average bits per slot status is updated. When this bit is cleared, the interrupt is not<br>asserted for such an event.<br>0b - Average Bits Per Slot Interrupt is disabled<br>1b - Average Bits Per Slot Interrupt is enabled|
|8<br>TXUIE|Transmit Queue Underflow Interrupt Enable When this bit is set, the Transmit Queue Underflow interrupt<br>is enabled. When this bit is reset, the Transmit Queue Underflow interrupt is disabled.<br>0b - Transmit Queue Underflow Interrupt Status is disabled<br>1b - Transmit Queue Underflow Interrupt Status is enabled|
|7-2<br>Reserved_7_2|Reserved.|
|1<br>ABPSIS|Average Bits Per Slot Interrupt Status When set, this bit indicates that the MAC has updated the ABS<br>value. This bit is cleared when the application writes 1 to this bit. Access restriction applies. Self-set to 1<br>on internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - Average Bits Per Slot Interrupt Status not detected<br>1b - Average Bits Per Slot Interrupt Status detected|
|0<br>TXUNFIS|Transmit Queue Underflow Interrupt Status This bit indicates that the Transmit Queue had an underflow<br>while transmitting the packet. Transmission is suspended and an Underflow Error TDES3[2] is set. This<br>bit is cleared when the application writes 1 to this bit. Access restriction applies. Self-set to 1 on internal<br>event. Setting 1 clears. Setting 0 has no effect.<br>0b - Transmit Queue Underflow Interrupt Status not detected<br>1b - Transmit Queue Underflow Interrupt Status detected|



# 75.7.297 (MTL_RxQ0_Operation_Mode) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RxQ0_Operation_|D30h|
|Mode||



## Function 

The Queue 0 Receive Operation Mode register establishes the Receive queue operating modes and command. The RFA and RFD fields are not backward compatible with the RFA and RFD fields of 4.00a release 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3955 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3956-02.png)


<!-- Start of picture text -->
Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R Reserved_31_y<br>RQS  e... RFD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv Reserv<br>R RFD  e... RFA  EHFC  DIS_T RSF  FEP  FUP  e... RTC<br>CP...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-26|Reserved.|
|Reserved_31_y||
|25-20<br>RQS|Receive Queue Size This field indicates the size of the allocated Receive queues in blocks of 256 bytes.<br>The RQS field is read-write only if the number of Rx Queues more than one, the reset value is 0x0 and<br>indicates size of 256 bytes. This means that value of 0x0 = 256 bytes, 0x1 = 512 bytes and so on. So,<br>program RQS [5:0] = 6'b001111 to allocate queue size of 4096 (4K) bytes. In general, the size of the<br>Queue = (RQS+1)*256 bytes. When the number of Rx Queues is one, the field is read-only and the<br>configured RX FIFO size in blocks of 256 bytes is reflected in the reset value. The width of this field<br>depends on the Rx memory size selected in your configuration. For example, if the memory size is 2048,<br>the width of this field is 3 bits: LOG2(2048/256) = LOG2(8) = 3 bits|
|19|Reserved.|
|Reserved_19_y||
|18-14<br>RFD|Threshold for Deactivating Flow Control (in half-duplex and full-duplex modes) These bits control the<br>threshold (fill-level of Rx queue) at which the flow control is de-asserted after activation: - 0: Full minus<br>1 KB, that is, FULL 1 KB - 1: Full minus 1.5 KB, that is, FULL 1.5 KB - 2: Full minus 2 KB, that is,<br>FULL 2 KB - 3: Full minus 2.5 KB, that is, FULL 2.5 KB - ... - 30: Full minus 16 KB, that is, FULL 16<br>KB - 31: Full minus 16.5 KB, that is, FULL 16.5 KB The de-assertion is effective only after flow control<br>is asserted. Note: The value must be programmed in such a way to make sure that the threshold is a<br>positive number. When the EHFC is set high, these values are applicable only when the Rx queue size<br>determined by the RQS field of this register, is equal to or greater than 4 KB. For a given queue size,<br>the values ranges between 0 and the encoding for FULL minus (QSIZE - 0.5 KB) and all other values<br>are illegal. Here the term FULL and QSIZE refers to the queue size determined by the RQS field of this<br>register. The width of this field depends on RX FIFO size selected during the configuration. Remaining<br>bits are reserved and read only.|
|13|Reserved.|
|Reserved_13_y||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3956 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field<br>12-8<br>RFA|Function<br>Threshold for Activating Flow Control (in half-duplex and full-duplex These bits control the threshold<br>(fill-level of Rx queue) at which the flow control is activated: For more information on encoding for this<br>field, see RFD.|
|---|---|
|7<br>EHFC|Enable Hardware Flow Control When this bit is set, the flow control signal operation, based on the<br>fill-level of Rx queue, is enabled. When reset, the flow control operation is disabled.<br>0b - Hardware Flow Control is disabled<br>1b - Hardware Flow Control is enabled|
|6<br>DIS_TCP_EF|Disable Dropping of TCP/IP Checksum Error Packets When this bit is set, the MAC does not drop the<br>packets which only have the errors detected by the Receive Checksum Offload engine. Such packets<br>have errors only in the encapsulated payload. There are no errors (including FCS error) in the Ethernet<br>packet received by the MAC. When this bit is reset, all error packets are dropped if the FEP bit is reset.<br>0b - Dropping of TCP/IP Checksum Error Packets is enabled<br>1b - Dropping of TCP/IP Checksum Error Packets is disabled|
|5<br>RSF|Receive Queue Store and Forward When this bit is set, the DWC_ether_qos reads a packet from the Rx<br>queue only after the complete packet has been written to it, ignoring the RTC field of this register. When<br>this bit is reset, the Rx queue operates in the Threshold (cut-through) mode, subject to the threshold<br>specified by the RTC field of this register.<br>0b - Receive Queue Store and Forward is disabled<br>1b - Receive Queue Store and Forward is enabled|
|4<br>FEP|Forward Error Packets When this bit is reset, the Rx queue drops packets with error status (CRC error,<br>GMII_ER, watchdog timeout, or overflow). However, if the start byte (write) pointer of a packet is already<br>transferred to the read controller side (in Threshold mode), the packet is not dropped. When this bit is<br>set, all packets except the runt error packets are forwarded to the application or DMA. If the RSF bit is<br>set and the Rx queue overflows when a partial packet is written, the packet is dropped irrespective of the<br>setting of this bit. However, if the RSF bit is reset and the Rx queue overflows when a partial packet is<br>written, a partial packet might be forwarded to the application or DMA.<br>0b - Forward Error Packets is disabled<br>1b - Forward Error Packets is enabled|
|3<br>FUP|Forward Undersized Good Packets When this bit is set, the Rx queue forwards the undersized good<br>packets (packets with no error and length less than 64 bytes), including pad-bytes and CRC. When this<br>bit is reset, the Rx queue drops all packets of less than 64 bytes, unless a packet is already transferred<br>because of the lower value of Rx Threshold, for example, RTC = 01.<br>0b - Forward Undersized Good Packets is disabled<br>1b - Forward Undersized Good Packets is enabled|
|2<br>Reserved_2|Reserved.|
|1-0<br>RTC|Receive Queue Threshold Control These bits control the threshold level of the MTL Rx queue (in bytes):<br>The received packet is transferred to the application or DMA when the packet size within the MTL<br>Rx queue is larger than the threshold. In addition, full packets with length less than the threshold are|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3957 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||automatically transferred. This field is valid only when the RSF bit is zero. This field is ignored when the<br>RSF bit is set to 1.|
||00b - 64|
||01b - 32|
||10b - 96|
||11b - 128|



# 75.7.298 (MTL_RxQ0_Missed_Packet_Overflow_Cnt) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RxQ0_Missed_Pac|D34h|
|ket_Overflow_Cnt||



## Function 

The Queue 0 Missed Packet and Overflow Counter register contains the counter for packets missed because of Receive queue packet flush and packets discarded because of Receive queue overflow. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3958-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>MISCN<br>R Reserved_31_28  MISPKTCNT<br>TO...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>OVFC<br>R Reserved_15_12  OVFPKTCNT<br>NTO...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function||
|---|---|---|
|31-28|Reserved.||
|Reserved_31_2|||
|8|||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3958 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|27<br>MISCNTOVF|Missed Packet Counter Overflow Bit When set, this bit indicates that the Rx Queue Missed Packet<br>Counter crossed the maximum limit. Access restriction applies. Clears on read. Self-set to 1 on internal<br>event.<br>0b - Missed Packet Counter overflow not detected<br>1b - Missed Packet Counter overflow detected|
|26-16<br>MISPKTCNT|Missed Packet Counter This field indicates the number of packets missed by the DWC_ether_qos<br>because the application asserted ari_pkt_flush_i[] for this queue. This counter is reset when this register<br>is read with mci_be_i[0] at 1b1. This counter is incremented by 1 when the DMA discards the packet<br>because of buffer unavailability. Access restriction applies. Clears on read. Self-set to 1 on internal<br>event.|
|15-12<br>Reserved_15_1<br>2|Reserved.|
|11<br>OVFCNTOVF|Overflow Counter Overflow Bit When set, this bit indicates that the Rx Queue Overflow Packet Counter<br>field crossed the maximum limit. Access restriction applies. Clears on read. Self-set to 1 on internal<br>event.<br>0b - Overflow Counter overflow not detected<br>1b - Overflow Counter overflow detected|
|10-0<br>OVFPKTCNT|Overflow Packet Counter This field indicates the number of packets discarded by the DWC_ether_qos<br>because of Receive queue overflow. This counter is incremented each time the DWC_ether_qos<br>discards an incoming packet because of overflow. This counter is reset when this register is read with<br>mci_be_i[0] at 1'b1. Access restriction applies. Clears on read. Self-set to 1 on internal event.|



# 75.7.299 (MTL_RxQ0_Debug) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RxQ0_Debug|D38h|



## Function 

The Queue 0 Receive Debug register gives the debug status of various blocks related to the Receive queue. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3959 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3960-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserved_31_3<br>R PRXQ<br>0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv RWCS<br>R Reserved_15_6  RXQSTS  RRCSTS<br>e... TS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-30|Reserved.|
|Reserved_31_3<br>0||
|29-16<br>PRXQ|Number of Packets in Receive Queue This field indicates the current number of packets in the<br>Rx Queue. The theoretical maximum value for this field is 256KB/16B = 16K Packets, that is,<br>Max_Queue_Size/Min_Packet_Size.|
|15-6<br>Reserved_15_6|Reserved.|
|5-4<br>RXQSTS|MTL Rx Queue Fill-Level Status This field gives the status of the fill-level of the Rx Queue:<br>00b - Rx Queue empty<br>01b - Rx Queue fill-level below flow-control deactivate threshold<br>10b - Rx Queue fill-level above flow-control activate threshold<br>11b - Rx Queue full|
|3<br>Reserved_3|Reserved.|
|2-1<br>RRCSTS|MTL Rx Queue Read Controller State This field gives the state of the Rx queue Read controller:<br>00b - Idle state<br>01b - Reading packet data<br>10b - Reading packet status (or timestamp)<br>11b - Flushing the packet data and status|
|0<br>RWCSTS|MTL Rx Queue Write Controller Active Status When high, this bit indicates that the MTL Rx queue Write<br>controller is active, and it is transferring a received packet to the Rx Queue.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3960 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - MTL Rx Queue Write Controller Active Status not detected|
||1b - MTL Rx Queue Write Controller Active Status detected|



# 75.7.300 (MTL_RxQ0_Control) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RxQ0_Control|D3Ch|



## Function 

The Queue Receive Control register controls the receive arbitration and passing of received packets to the application. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||Reserve|d_31_4|||||||
|W||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R<br>W||||||Reserve|d_31_4||||||RXQ_F<br>RM...|R|XQ_WEGT|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



## Fields 

|Field|Function|
|---|---|
|31-4|Reserved.|
|Reserved_31_4||
|3<br>RXQ_FRM_AR<br>BIT|Receive Queue Packet Arbitration When this bit is set, the DWC_ether_qos drives the packet data to the<br>ARI interface such that the entire packet data of currently-selected queue is transmitted before switching<br>to other queue. When this bit is reset, the DWC_ether_qos drives the packet data to the ARI interface<br>such that the following amount of data of currently-selected queue is transmitted before switching to<br>other queue: - PBL amount of data (indicated by ari_qN_pbl_i[]) or - Complete data of a packet The<br>status and the timestamp are not a part of the PBL data. Therefore, the DWC_ether_qos drives the<br>complete status (including timestamp status) during first PBL request for the packet (in store-and-forward<br>mode) or the last PBL request for the packet (in Threshold mode).|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3961 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Receive Queue Packet Arbitration is disabled<br>1b - Receive Queue Packet Arbitration is enabled|
|2-0<br>RXQ_WEGT|Receive Queue Weight This field indicates the weight assigned to the Rx Queue 0. This field needs to<br>be programmed with one value less than the required weight, that is, reset value of 0 indicates weight of<br>1, value of 1 indicates weight of 2, and so on. The weight is used as the number of continuous PBL or<br>packets requests (depending on the RXQ_FRM_ARBIT) allocated to the queue in one arbitration cycle.<br>Note: The change in value of RXQ_WEGT takes effect only after the completion of current service round<br>or when there is change from RAA=SP to RAA=WSP algorithm. This approach is taken so that there<br>is smooth transition. For the RXQ_WEGT value to take effect at the start, the MTL_RxQ(#i)_Control<br>registers must be programmed before the MTL_Operation_Mode register.|



# 75.7.301 (MTL_TxQ1_Operation_Mode) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ1_Operation_M|D40h|
|ode||



## Function 

The Queue 1 Transmit Operation Mode register establishes the Transmit queue operating modes and commands. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3962-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_y<br>TQS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_15_7<br>TTC  TXQEN  TSF  FTQ<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function||
|---|---|---|
|31-22|Reserved.||
|Reserved_31_y|||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3962 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|21-16<br>TQS|Transmit Queue Size This field indicates the size of the allocated Transmit queues in blocks of 256<br>bytes. The TQS field is read-write only if the number of Tx Queues more than one, the reset value is<br>0x0 and indicates size of 256 bytes. This means that value of 0x0 = 256 bytes, 0x1 = 512 bytes and so<br>on. So, program TQS [5:0] = 6'b001111 to allocate queue size of 4096 (4K) bytes. In general, the size<br>of the Queue = (TQS+1)*256 bytes. When the number of Tx Queues is one, the field is read-only and<br>the configured TX FIFO size in blocks of 256 bytes is reflected in the reset value. The width of this field<br>depends on the Tx memory size selected in your configuration. For example, if the memory size is 2048,<br>the width of this field is 3 bits: LOG2(2048/256) = LOG2(8) = 3 bits|
|15-7<br>Reserved_15_7|Reserved.|
|6-4<br>TTC|Transmit Threshold Control These bits control the threshold level of the MTL Tx Queue. The<br>transmission starts when the packet size within the MTL Tx Queue is larger than the threshold. In<br>addition, full packets with length less than the threshold are also transmitted. These bits are used only<br>when the TSF bit is reset.<br>000b - 32<br>001b - 64<br>010b - 96<br>011b - 128<br>100b - 192<br>101b - 256<br>110b - 384<br>111b - 512|
|3-2<br>TXQEN|Transmit Queue Enable This field is used to enable/disable the transmit queue 0. - 2'b00: Not enabled -<br>2'b01: Enable in AV mode - 2'b10: Enabled - 2'b11: Reserved Note: In multiple Tx queues configuration,<br>all the queues are disabled by default. Enable the Tx queue by programming this field.<br>00b - Not enabled<br>01b - Enable in AV mode (Reserved in non-AV)<br>10b - Enabled<br>11b - Reserved|
|1<br>TSF|Transmit Store and Forward When this bit is set, the transmission starts when a full packet resides in the<br>MTL Tx queue. When this bit is set, the TTC values specified in Bits[6:4] of this register are ignored. This<br>bit should be changed only when the transmission is stopped.<br>0b - Transmit Store and Forward is disabled<br>1b - Transmit Store and Forward is enabled|
|0<br>FTQ|Flush Transmit Queue When this bit is set, the Tx queue controller logic is reset to its default values.<br>Therefore, all the data in the Tx queue is lost or flushed. This bit is internally reset when the flushing<br>operation is complete. Until this bit is reset, you should not write to the MTL_TxQ1_Operation_Mode<br>register. The data which is already accepted by the MAC transmitter is not flushed. It is scheduled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3963 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||for transmission and results in underflow and runt packet transmission. Note: The flush operation is<br>complete only when the Tx queue is empty and the application has accepted the pending Tx Status of<br>all transmitted packets. To complete this flush operation, the PHY Tx clock (clk_tx_i) should be active.<br>Access restriction applies. Setting 1 sets. Self-cleared. Setting 0 has no effect.|
||0b - Flush Transmit Queue is disabled|
||1b - Flush Transmit Queue is enabled|



# 75.7.302 (MTL_TxQ1_Underflow) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ1_Underflow|D44h|



## Function 

The Queue 1 Underflow Counter register contains the counter for packets aborted because of Transmit queue underflow and packets missed because of Receive queue packet flush 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3964-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_12<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>UFCN<br>R Reserved_31_12  UFFRMCNT<br>TOVF<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-12|Reserved.|
|Reserved_31_1<br>2||
|11<br>UFCNTOVF|Overflow Bit for Underflow Packet Counter This bit is set every time the Tx queue Underflow Packet<br>Counter field overflows, that is, it has crossed the maximum count. In such a scenario, the overflow|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3964 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||packet counter is reset to all-zeros and this bit indicates that the rollover happened. Access restriction<br>applies. Clears on read. Self-set to 1 on internal event.<br>0b - Overflow not detected for Underflow Packet Counter|
||1b - Overflow detected for Underflow Packet Counter|
|10-0<br>UFFRMCNT|Underflow Packet Counter This field indicates the number of packets aborted by the controller because<br>of Tx Queue Underflow. This counter is incremented each time the MAC aborts outgoing packet because<br>of underflow. The counter is cleared when this register is read with mci_be_i[0] at 1'b1. Access restriction<br>applies. Clears on read. Self-set to 1 on internal event.|



# 75.7.303 (MTL_TxQ1_Debug) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ1_Debug|D48h|



## Function 

The Queue 1 Transmit Debug register gives the debug status of various blocks related to the Transmit queue. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18<br>17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||Re|served_31|_23|||||STXSTSF||Reserv<br>e...|PTXQ||
|W||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2<br>1|0|
|R|||||Reserve|d_15_6|||||TXSTS<br>FS...|TXQS<br>TS|TWCS<br>TS|TRCSTS|TXQP<br>AUS...|
|W||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|0|



## Fields 

|Field|Function||
|---|---|---|
|31-23|Reserved.||
|Reserved_31_2<br>3|||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3965 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field<br>22-20<br>STXSTSF|Function<br>Number of Status Words in Tx Status FIFO of Queue This field indicates the current number of status in<br>the Tx Status FIFO of this queue. When the DTXSTS bit of MTL_Operation_Mode register is set to 1, this<br>field does not reflect the number of status words in Tx Status FIFO.|
|---|---|
|19<br>Reserved_19|Reserved.|
|18-16<br>PTXQ|Number of Packets in the Transmit Queue This field indicates the current number of packets in the Tx<br>Queue. When the DTXSTS bit of MTL_Operation_Mode register is set to 1, this field does not reflect the<br>number of packets in the Transmit queue.|
|15-6|Reserved.|
|Reserved_15_6||
|5<br>TXSTSFSTS|MTL Tx Status FIFO Full Status When high, this bit indicates that the MTL Tx Status FIFO is full.<br>Therefore, the MTL cannot accept any more packets for transmission.<br>0b - MTL Tx Status FIFO Full status is not detected<br>1b - MTL Tx Status FIFO Full status is detected|
|4<br>TXQSTS|MTL Tx Queue Not Empty Status When this bit is high, it indicates that the MTL Tx Queue is not empty<br>and some data is left for transmission.<br>0b - MTL Tx Queue Not Empty status is not detected<br>1b - MTL Tx Queue Not Empty status is detected|
|3<br>TWCSTS|MTL Tx Queue Write Controller Status When high, this bit indicates that the MTL Tx Queue Write<br>Controller is active, and it is transferring the data to the Tx Queue.<br>0b - MTL Tx Queue Write Controller status is not detected<br>1b - MTL Tx Queue Write Controller status is detected|
|2-1<br>TRCSTS|MTL Tx Queue Read Controller Status This field indicates the state of the Tx Queue Read Controller:<br>00b - Idle state<br>01b - Read state (transferring data to the MAC transmitter)<br>10b - Waiting for pending Tx Status from the MAC transmitter<br>11b - Flushing the Tx queue because of the Packet Abort request from the MAC|
|0<br>TXQPAUSED|Transmit Queue in Pause When this bit is high and the Rx flow control is enabled, it indicates that the Tx<br>Queue is in the Pause condition (in the full-duplex only mode) because of the following: - Reception of<br>the PFC packet for the priorities assigned to the Tx Queue when PFC is enabled - Reception of 802.3x<br>Pause packet when PFC is disabled<br>0b - Transmit Queue in Pause status is not detected<br>1b - Transmit Queue in Pause status is detected|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3966 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.304 (MTL_TxQ1_ETS_Control) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ1_ETS_Control|D50h|



## Function 

The Queue ETS Control register controls the enhanced transmission selection operation. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3967-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_7<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_31_7  AVAL Reserved_1_0<br>SLC  CC<br>W G<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-7|Reserved.|
|Reserved_31_7||
|6-4<br>SLC|Slot Count If the credit-based shaper algorithm is enabled, the software can program the number of<br>slots (of duration programmed in DMA_CH(#i)_Slot_Interval register) over which the average transmitted<br>bits per slot, provided in the MTL_TxQ(#i)_ETS_Status register, need to be computed for Queue. The<br>encoding is as follows:<br>000b - 1 slot<br>001b - 2 slots<br>010b - 4 slots<br>011b - 8 slots<br>100b - 16 slots<br>101b - Reserved|
|3<br>CC|Credit Control When this bit is set, the accumulated credit parameter in the credit-based shaper<br>algorithm logic is not reset to zero when there is positive credit and no packet to transmit in Channel<br>1. The credit accumulates even when there is no packet waiting in Channel 1 and another channel<br>is transmitting. When this bit is reset, the accumulated credit parameter in the credit-based shaper|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3967 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||algorithm logic is set to zero when there is positive credit and no packet to transmit in Channel 1. When<br>there is no packet waiting in Channel 1 and other channel is transmitting, no credit is accumulated.<br>0b - Credit Control is disabled|
||1b - Credit Control is enabled|
|2<br>AVALG|AV Algorithm When Queue 1 is programmed for AV, this field configures the scheduling algorithm for this<br>queue: This bit when set, indicates credit based shaper algorithm (CBS) is selected for Queue 1 traffic.<br>When reset, strict priority is selected.<br>0b - CBS Algorithm is disabled<br>1b - CBS Algorithm is enabled|
|1-0|Reserved.|
|Reserved_1_0||



# 75.7.305 (MTL_TxQ1_ETS_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ1_ETS_Status|D54h|



## Function 

The Queue 1 ETS Status register provides the average traffic transmitted in Queue 1. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||Reserve|d_31_24|||||||AB|S||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||AB|S||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3968 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-24|Reserved.|
|Reserved_31_2<br>4||
|23-0<br>ABS|Average Bits per Slot This field contains the average transmitted bits per slot. If AV operation<br>is enabled, this field is computed over number of slots, programmed in the SLC field of<br>MTL_TxQ(#i)_ETS_CONTROL register. The maximum value of this field is 0x6_4000 in 100 Mbps,<br>0x3E_8000 in 1000 Mbps and 9C_4000 in 2500 Mbps mode respectively. When the DCB operation is<br>enabled for Queue, this field is computed over every 10 million bit times slot (4 ms in 2500 Mbps; 10 ms<br>in 1000 Mbps; 100 ms in 100 Mbps). The maximum value is 0x989680.|



# 75.7.306 (MTL_TxQ1_Quantum_Weight) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ1_Quantum_W|D58h|
|eight||



## Function 

The Queue 1 idleSlopeCredit, Quantum or Weights register provides the average traffic transmitted in Queue 1. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||||Res|erved_31|_21|||||||ISCQW|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||ISC|QW||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-21|Reserved.|
|Reserved_31_2<br>1||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3969 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|20-0<br>ISCQW|idleSlopeCredit, Quantum or Weights - idleSlopeCredit When AV feature is enabled, this field contains<br>the idleSlopeCredit value required for the credit-based shaper algorithm for Queue 1. This is the rate<br>of change of credit in bits per cycle (40 ns for 100 Mbps; 8 ns for 1000 Mbps; 3.2 ns for 2500 Mbps)<br>when the credit is increasing. The software should program this field with computed credit in bits per<br>cycle scaled by 1,024. The maximum value is portTransmitRate, that is, 0x2000 in 1000/2500 Mbps<br>mode and 0x1000 in 100 Mbps mode. Bits[20:14] must be written to zero. - Quantum When the DCB<br>operation is enabled with DWRR algorithm for Queue 1 traffic, this field contains the quantum value in<br>bytes to be added to credit during every queue scanning cycle. The maximum value is 0x1312D0 bytes.<br>- Weights When DCB operation is enabled with WFQ algorithm for Queue 1 traffic, this field contains<br>the weight for this queue. The maximum value is 0x3FFF where weight of 0 indicates 100% bandwidth.<br>Bits[20:14] must be written to zero. When DCB operation or generic queuing operation is enabled with<br>WRR algorithm for Queue 1 traffic, this field contains the weight for this queue. The maximum value is<br>0x64. Bits [20:7] must be written to zero. - Note 1: In multiple Queue configuration this field in respective<br>per queue register must be programmed to some non-zero value when multiple queues are enabled or<br>single queue other than Q0 is enabled. This field need not be programmed when only Q0 is enabled. In<br>general, when WRR algorithm is selected a non-zero value must be programmed on both Receive and<br>Transmit. In Receive, the register is MTL_Operation_Mode register. - Note 2: For WFQ algorithm, higher<br>the programmed weights lesser the bandwidth allocated for that Transmit Queue. The finish time is not a<br>function of particular packet alone but it is as per the formula: (previous_finish_time of particular Transmit<br>Queue + (weights*packet_size)) - Note 3: The weights programmed do not correspond to the number of<br>packets but the fraction of bandwidth or time allocated for particular queue w.r.t. total BW or time.|



# 75.7.307 (MTL_TxQ1_SendSlopeCredit) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ1_SendSlopeC|D5Ch|
|redit||



## Function 

The sendSlopeCredit register contains the sendSlope credit value required for the credit-based shaper algorithm for the Queue. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3970 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3971-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_14<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserved_31_1<br>R<br>4  SSC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-14|Reserved.|
|Reserved_31_1<br>4||
|13-0<br>SSC|sendSlopeCredit Value When AV operation is enabled, this field contains the sendSlopeCredit value<br>required for credit-based shaper algorithm for Queue 1. This is the rate of change of credit in bits<br>per cycle (40 ns, 8 ns and 3.2 ns for 100 Mbps, 1000 Mbps and 2500 Mbps respectively) when the<br>credit is decreasing. The software should program this field with computed credit in bits per cycle<br>scaled by 1,024. The maximum value is portTransmitRate, that is, 0x2000 in 1000/2500 Mbps mode<br>and 0x1000 in 100 Mbps mode. This field should be programmed with absolute sendSlopeCredit value.<br>The credit-based shaper logic subtracts it from the accumulated credit when Channel 1 is selected for<br>transmission.|



# 75.7.308 (MTL_TxQ1_HiCredit) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ1_HiCredit|D60h|



## Function 

The hiCredit register contains the hiCredit value required for the credit-based shaper algorithm for the Queue. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3971 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3972-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_29<br>HC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>HC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-29|Reserved.|
|Reserved_31_2<br>9||
|28-0<br>HC|hiCredit Value When the AV feature is enabled, this field contains the hiCredit value required for<br>the credit-based shaper algorithm. This is the maximum value that can be accumulated in the credit<br>parameter. This is specified in bits scaled by 1,024. The maximum value is maxInterferenceSize, that is,<br>best-effort maximum packet size (16,384 bytes or 131,072 bits). The value to be specified is 131,072 *<br>1,024 = 134,217,728 or 0x0800_0000.|



# 75.7.309 (MTL_TxQ1_LoCredit) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ1_LoCredit|D64h|



## Function 

The loCredit register contains the loCredit value required for the credit-based shaper algorithm for the Queue. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3972 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3973-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_29<br>LC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>LC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-29|Reserved.|
|Reserved_31_2<br>9||
|28-0<br>LC|loCredit Value When AV operation is enabled, this field contains the loCredit value required for the<br>credit-based shaper algorithm. This is the minimum value that can be accumulated in the credit<br>parameter. This is specified in bits scaled by 1,024. The maximum value to be programmed is<br>corresponds to twice the maxFrameSize transmitted from this queue. If the maxFrameSize is 8192<br>bytes, then (8192*2) * 8 * 1024 = 134,217,728 or 0x0800_0000. Because it is a negative value, the<br>programmed value is 2's complement of the value, that is, 0x1800_0000.|



# 75.7.310 (MTL_Q1_Interrupt_Control_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_Q1_Interrupt_Contr|D6Ch|
|ol_Status||



## Function 

This register contains the interrupt enable and status bits for the queue 1 interrupts. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3973 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||Res|erved_31|_25|||RXOIE|||Res|erved_23|_17|||RXOV|
|W||||||||||||||||FIS|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||Reserve|d_15_10|||ABPSI|TXUIE|||Reserve|d_7_2|||ABPSI|TXUN|
|W|||||||E||||||||S|FIS|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-25|Reserved.|
|Reserved_31_2<br>5||
|24<br>RXOIE|Receive Queue Overflow Interrupt Enable When this bit is set, the Receive Queue Overflow interrupt is<br>enabled. When this bit is reset, the Receive Queue Overflow interrupt is disabled.<br>0b - Receive Queue Overflow Interrupt is disabled<br>1b - Receive Queue Overflow Interrupt is enabled|
|23-17<br>Reserved_23_1<br>7|Reserved.|
|16<br>RXOVFIS|Receive Queue Overflow Interrupt Status This bit indicates that the Receive Queue had an overflow<br>while receiving the packet. If a partial packet is transferred to the application, the overflow status is set<br>in RDES3[21]. This bit is cleared when the application writes 1 to this bit. Access restriction applies.<br>Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - Receive Queue Overflow Interrupt Status not detected<br>1b - Receive Queue Overflow Interrupt Status detected|
|15-10<br>Reserved_15_1<br>0|Reserved.|
|9<br>ABPSIE|Average Bits Per Slot Interrupt Enable When this bit is set, the MAC asserts the sbd_intr_o or mci_intr_o<br>interrupt when the average bits per slot status is updated. When this bit is cleared, the interrupt is not<br>asserted for such an event.<br>0b - Average Bits Per Slot Interrupt is disabled<br>1b - Average Bits Per Slot Interrupt is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3974 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|8<br>TXUIE|Transmit Queue Underflow Interrupt Enable When this bit is set, the Transmit Queue Underflow interrupt<br>is enabled. When this bit is reset, the Transmit Queue Underflow interrupt is disabled.<br>0b - Transmit Queue Underflow Interrupt Status is disabled<br>1b - Transmit Queue Underflow Interrupt Status is enabled|
|7-2|Reserved.|
|Reserved_7_2||
|1<br>ABPSIS|Average Bits Per Slot Interrupt Status When set, this bit indicates that the MAC has updated the ABS<br>value. This bit is cleared when the application writes 1 to this bit. Access restriction applies. Self-set to 1<br>on internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - Average Bits Per Slot Interrupt Status not detected<br>1b - Average Bits Per Slot Interrupt Status detected|
|0<br>TXUNFIS|Transmit Queue Underflow Interrupt Status This bit indicates that the Transmit Queue had an underflow<br>while transmitting the packet. Transmission is suspended and an Underflow Error TDES3[2] is set. This<br>bit is cleared when the application writes 1 to this bit. Access restriction applies. Self-set to 1 on internal<br>event. Setting 1 clears. Setting 0 has no effect.<br>0b - Transmit Queue Underflow Interrupt Status not detected<br>1b - Transmit Queue Underflow Interrupt Status detected|



# 75.7.311 (MTL_RxQ1_Operation_Mode) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RxQ1_Operation_|D70h|
|Mode||



## Function 

The Queue 1 Receive Operation Mode register establishes the Receive queue operating modes and command. The RFA and RFD fields are not backward compatible with the RFA and RFD fields of 4.00a release 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3975 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3976-02.png)


<!-- Start of picture text -->
Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R Reserved_31_y<br>RQS  e... RFD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv Reserv<br>R RFD  e... RFA  EHFC  DIS_T RSF  FEP  FUP  e... RTC<br>CP...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-26|Reserved.|
|Reserved_31_y||
|25-20<br>RQS|Receive Queue Size This field indicates the size of the allocated Receive queues in blocks of 256 bytes.<br>The RQS field is read-write only if the number of Rx Queues more than one, the reset value is 0x0 and<br>indicates size of 256 bytes. This means that value of 0x0 = 256 bytes, 0x1 = 512 bytes and so on. So,<br>program RQS [5:0] = 6'b001111 to allocate queue size of 4096 (4K) bytes. In general, the size of the<br>Queue = (RQS+1)*256 bytes. When the number of Rx Queues is one, the field is read-only and the<br>configured RX FIFO size in blocks of 256 bytes is reflected in the reset value. The width of this field<br>depends on the Rx memory size selected in your configuration. For example, if the memory size is 2048,<br>the width of this field is 3 bits: LOG2(2048/256) = LOG2(8) = 3 bits|
|19|Reserved.|
|Reserved_19_y||
|18-14<br>RFD|Threshold for Deactivating Flow Control (in half-duplex and full-duplex modes) These bits control the<br>threshold (fill-level of Rx queue) at which the flow control is de-asserted after activation: - 0: Full minus<br>1 KB, that is, FULL 1 KB - 1: Full minus 1.5 KB, that is, FULL 1.5 KB - 2: Full minus 2 KB, that is,<br>FULL 2 KB - 3: Full minus 2.5 KB, that is, FULL 2.5 KB - ... - 30: Full minus 16 KB, that is, FULL 16<br>KB - 31: Full minus 16.5 KB, that is, FULL 16.5 KB The de-assertion is effective only after flow control<br>is asserted. Note: The value must be programmed in such a way to make sure that the threshold is a<br>positive number. When the EHFC is set high, these values are applicable only when the Rx queue size<br>determined by the RQS field of this register, is equal to or greater than 4 KB. For a given queue size,<br>the values ranges between 0 and the encoding for FULL minus (QSIZE - 0.5 KB) and all other values<br>are illegal. Here the term FULL and QSIZE refers to the queue size determined by the RQS field of this<br>register. The width of this field depends on RX FIFO size selected during the configuration. Remaining<br>bits are reserved and read only.|
|13|Reserved.|
|Reserved_13_y||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3976 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field<br>12-8<br>RFA|Function<br>Threshold for Activating Flow Control (in half-duplex and full-duplex These bits control the threshold<br>(fill-level of Rx queue) at which the flow control is activated: For more information on encoding for this<br>field, see RFD.|
|---|---|
|7<br>EHFC|Enable Hardware Flow Control When this bit is set, the flow control signal operation, based on the<br>fill-level of Rx queue, is enabled. When reset, the flow control operation is disabled.<br>0b - Hardware Flow Control is disabled<br>1b - Hardware Flow Control is enabled|
|6<br>DIS_TCP_EF|Disable Dropping of TCP/IP Checksum Error Packets When this bit is set, the MAC does not drop the<br>packets which only have the errors detected by the Receive Checksum Offload engine. Such packets<br>have errors only in the encapsulated payload. There are no errors (including FCS error) in the Ethernet<br>packet received by the MAC. When this bit is reset, all error packets are dropped if the FEP bit is reset.<br>0b - Dropping of TCP/IP Checksum Error Packets is enabled<br>1b - Dropping of TCP/IP Checksum Error Packets is disabled|
|5<br>RSF|Receive Queue Store and Forward When this bit is set, the DWC_ether_qos reads a packet from the Rx<br>queue only after the complete packet has been written to it, ignoring the RTC field of this register. When<br>this bit is reset, the Rx queue operates in the Threshold (cut-through) mode, subject to the threshold<br>specified by the RTC field of this register.<br>0b - Receive Queue Store and Forward is disabled<br>1b - Receive Queue Store and Forward is enabled|
|4<br>FEP|Forward Error Packets When this bit is reset, the Rx queue drops packets with error status (CRC error,<br>GMII_ER, watchdog timeout, or overflow). However, if the start byte (write) pointer of a packet is already<br>transferred to the read controller side (in Threshold mode), the packet is not dropped. When this bit is<br>set, all packets except the runt error packets are forwarded to the application or DMA. If the RSF bit is<br>set and the Rx queue overflows when a partial packet is written, the packet is dropped irrespective of the<br>setting of this bit. However, if the RSF bit is reset and the Rx queue overflows when a partial packet is<br>written, a partial packet might be forwarded to the application or DMA.<br>0b - Forward Error Packets is disabled<br>1b - Forward Error Packets is enabled|
|3<br>FUP|Forward Undersized Good Packets When this bit is set, the Rx queue forwards the undersized good<br>packets (packets with no error and length less than 64 bytes), including pad-bytes and CRC. When this<br>bit is reset, the Rx queue drops all packets of less than 64 bytes, unless a packet is already transferred<br>because of the lower value of Rx Threshold, for example, RTC = 01.<br>0b - Forward Undersized Good Packets is disabled<br>1b - Forward Undersized Good Packets is enabled|
|2<br>Reserved_2|Reserved.|
|1-0<br>RTC|Receive Queue Threshold Control These bits control the threshold level of the MTL Rx queue (in bytes):<br>The received packet is transferred to the application or DMA when the packet size within the MTL<br>Rx queue is larger than the threshold. In addition, full packets with length less than the threshold are|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3977 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||automatically transferred. This field is valid only when the RSF bit is zero. This field is ignored when the<br>RSF bit is set to 1.|
||00b - 64|
||01b - 32|
||10b - 96|
||11b - 128|



# 75.7.312 (MTL_RxQ1_Missed_Packet_Overflow_Cnt) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RxQ1_Missed_Pac|D74h|
|ket_Overflow_Cnt||



## Function 

The Queue 1 Missed Packet and Overflow Counter register contains the counter for packets missed because of Receive queue packet flush and packets discarded because of Receive queue overflow. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3978-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>MISCN<br>R Reserved_31_28  MISPKTCNT<br>TO...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>OVFC<br>R Reserved_15_12  OVFPKTCNT<br>NTO...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function||
|---|---|---|
|31-28|Reserved.||
|Reserved_31_2|||
|8|||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3978 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|27<br>MISCNTOVF|Missed Packet Counter Overflow Bit When set, this bit indicates that the Rx Queue Missed Packet<br>Counter crossed the maximum limit. Access restriction applies. Clears on read. Self-set to 1 on internal<br>event.<br>0b - Missed Packet Counter overflow not detected<br>1b - Missed Packet Counter overflow detected|
|26-16<br>MISPKTCNT|Missed Packet Counter This field indicates the number of packets missed by the DWC_ether_qos<br>because the application asserted ari_pkt_flush_i[] for this queue. This counter is reset when this register<br>is read with mci_be_i[0] at 1b1. This counter is incremented by 1 when the DMA discards the packet<br>because of buffer unavailability. Access restriction applies. Clears on read. Self-set to 1 on internal<br>event.|
|15-12<br>Reserved_15_1<br>2|Reserved.|
|11<br>OVFCNTOVF|Overflow Counter Overflow Bit When set, this bit indicates that the Rx Queue Overflow Packet Counter<br>field crossed the maximum limit. Access restriction applies. Clears on read. Self-set to 1 on internal<br>event.<br>0b - Overflow Counter overflow not detected<br>1b - Overflow Counter overflow detected|
|10-0<br>OVFPKTCNT|Overflow Packet Counter This field indicates the number of packets discarded by the DWC_ether_qos<br>because of Receive queue overflow. This counter is incremented each time the DWC_ether_qos<br>discards an incoming packet because of overflow. This counter is reset when this register is read with<br>mci_be_i[0] at 1'b1. Access restriction applies. Clears on read. Self-set to 1 on internal event.|



# 75.7.313 (MTL_RxQ1_Debug) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RxQ1_Debug|D78h|



## Function 

The Queue 1 Receive Debug register gives the debug status of various blocks related to the Receive queue. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3979 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3980-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserved_31_3<br>R PRXQ<br>0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv RWCS<br>R Reserved_15_6  RXQSTS  RRCSTS<br>e... TS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-30|Reserved.|
|Reserved_31_3<br>0||
|29-16<br>PRXQ|Number of Packets in Receive Queue This field indicates the current number of packets in the<br>Rx Queue. The theoretical maximum value for this field is 256KB/16B = 16K Packets, that is,<br>Max_Queue_Size/Min_Packet_Size.|
|15-6<br>Reserved_15_6|Reserved.|
|5-4<br>RXQSTS|MTL Rx Queue Fill-Level Status This field gives the status of the fill-level of the Rx Queue:<br>00b - Rx Queue empty<br>01b - Rx Queue fill-level below flow-control deactivate threshold<br>10b - Rx Queue fill-level above flow-control activate threshold<br>11b - Rx Queue full|
|3<br>Reserved_3|Reserved.|
|2-1<br>RRCSTS|MTL Rx Queue Read Controller State This field gives the state of the Rx queue Read controller:<br>00b - Idle state<br>01b - Reading packet data<br>10b - Reading packet status (or timestamp)<br>11b - Flushing the packet data and status|
|0<br>RWCSTS|MTL Rx Queue Write Controller Active Status When high, this bit indicates that the MTL Rx queue Write<br>controller is active, and it is transferring a received packet to the Rx Queue.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3980 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - MTL Rx Queue Write Controller Active Status not detected|
||1b - MTL Rx Queue Write Controller Active Status detected|



# 75.7.314 (MTL_RxQ1_Control) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RxQ1_Control|D7Ch|



## Function 

The Queue Receive Control register controls the receive arbitration and passing of received packets to the application. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||Reserve|d_31_4|||||||
|W||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R<br>W||||||Reserve|d_31_4||||||RXQ_F<br>RM...|R|XQ_WEGT|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



## Fields 

|Field|Function|
|---|---|
|31-4|Reserved.|
|Reserved_31_4||
|3<br>RXQ_FRM_AR<br>BIT|Receive Queue Packet Arbitration When this bit is set, the DWC_ether_qos drives the packet data to the<br>ARI interface such that the entire packet data of currently-selected queue is transmitted before switching<br>to other queue. When this bit is reset, the DWC_ether_qos drives the packet data to the ARI interface<br>such that the following amount of data of currently-selected queue is transmitted before switching to<br>other queue: - PBL amount of data (indicated by ari_qN_pbl_i[]) or - Complete data of a packet The<br>status and the timestamp are not a part of the PBL data. Therefore, the DWC_ether_qos drives the<br>complete status (including timestamp status) during first PBL request for the packet (in store-and-forward<br>mode) or the last PBL request for the packet (in Threshold mode).|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3981 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Receive Queue Packet Arbitration is disabled<br>1b - Receive Queue Packet Arbitration is enabled|
|2-0<br>RXQ_WEGT|Receive Queue Weight This field indicates the weight assigned to the Rx Queue 0. This field needs to<br>be programmed with one value less than the required weight, that is, reset value of 0 indicates weight of<br>1, value of 1 indicates weight of 2, and so on. The weight is used as the number of continuous PBL or<br>packets requests (depending on the RXQ_FRM_ARBIT) allocated to the queue in one arbitration cycle.<br>Note: The change in value of RXQ_WEGT takes effect only after the completion of current service round<br>or when there is change from RAA=SP to RAA=WSP algorithm. This approach is taken so that there<br>is smooth transition. For the RXQ_WEGT value to take effect at the start, the MTL_RxQ(#i)_Control<br>registers must be programmed before the MTL_Operation_Mode register.|



# 75.7.315 (MTL_TxQ2_Operation_Mode) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ2_Operation_M|D80h|
|ode||



## Function 

The Queue 2 Transmit Operation Mode register establishes the Transmit queue operating modes and commands. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3982-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_y<br>TQS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_15_7<br>TTC  TXQEN  TSF  FTQ<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function||
|---|---|---|
|31-22|Reserved.||
|Reserved_31_y|||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3982 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|21-16<br>TQS|Transmit Queue Size This field indicates the size of the allocated Transmit queues in blocks of 256<br>bytes. The TQS field is read-write only if the number of Tx Queues more than one, the reset value is<br>0x0 and indicates size of 256 bytes. This means that value of 0x0 = 256 bytes, 0x1 = 512 bytes and so<br>on. So, program TQS [5:0] = 6'b001111 to allocate queue size of 4096 (4K) bytes. In general, the size<br>of the Queue = (TQS+1)*256 bytes. When the number of Tx Queues is one, the field is read-only and<br>the configured TX FIFO size in blocks of 256 bytes is reflected in the reset value. The width of this field<br>depends on the Tx memory size selected in your configuration. For example, if the memory size is 2048,<br>the width of this field is 3 bits: LOG2(2048/256) = LOG2(8) = 3 bits|
|15-7<br>Reserved_15_7|Reserved.|
|6-4<br>TTC|Transmit Threshold Control These bits control the threshold level of the MTL Tx Queue. The<br>transmission starts when the packet size within the MTL Tx Queue is larger than the threshold. In<br>addition, full packets with length less than the threshold are also transmitted. These bits are used only<br>when the TSF bit is reset.<br>000b - 32<br>001b - 64<br>010b - 96<br>011b - 128<br>100b - 192<br>101b - 256<br>110b - 384<br>111b - 512|
|3-2<br>TXQEN|Transmit Queue Enable This field is used to enable/disable the transmit queue 0. - 2'b00: Not enabled -<br>2'b01: Enable in AV mode - 2'b10: Enabled - 2'b11: Reserved Note: In multiple Tx queues configuration,<br>all the queues are disabled by default. Enable the Tx queue by programming this field.<br>00b - Not enabled<br>01b - Enable in AV mode (Reserved in non-AV)<br>10b - Enabled<br>11b - Reserved|
|1<br>TSF|Transmit Store and Forward When this bit is set, the transmission starts when a full packet resides in the<br>MTL Tx queue. When this bit is set, the TTC values specified in Bits[6:4] of this register are ignored. This<br>bit should be changed only when the transmission is stopped.<br>0b - Transmit Store and Forward is disabled<br>1b - Transmit Store and Forward is enabled|
|0<br>FTQ|Flush Transmit Queue When this bit is set, the Tx queue controller logic is reset to its default values.<br>Therefore, all the data in the Tx queue is lost or flushed. This bit is internally reset when the flushing<br>operation is complete. Until this bit is reset, you should not write to the MTL_TxQ1_Operation_Mode<br>register. The data which is already accepted by the MAC transmitter is not flushed. It is scheduled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3983 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||for transmission and results in underflow and runt packet transmission. Note: The flush operation is<br>complete only when the Tx queue is empty and the application has accepted the pending Tx Status of<br>all transmitted packets. To complete this flush operation, the PHY Tx clock (clk_tx_i) should be active.<br>Access restriction applies. Setting 1 sets. Self-cleared. Setting 0 has no effect.|
||0b - Flush Transmit Queue is disabled|
||1b - Flush Transmit Queue is enabled|



# 75.7.316 (MTL_TxQ2_Underflow) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ2_Underflow|D84h|



## Function 

The Queue 2 Underflow Counter register contains the counter for packets aborted because of Transmit queue underflow and packets missed because of Receive queue packet flush 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3984-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_12<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>UFCN<br>R Reserved_31_12  UFFRMCNT<br>TOVF<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-12|Reserved.|
|Reserved_31_1<br>2||
|11<br>UFCNTOVF|Overflow Bit for Underflow Packet Counter This bit is set every time the Tx queue Underflow Packet<br>Counter field overflows, that is, it has crossed the maximum count. In such a scenario, the overflow|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3984 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||packet counter is reset to all-zeros and this bit indicates that the rollover happened. Access restriction<br>applies. Clears on read. Self-set to 1 on internal event.<br>0b - Overflow not detected for Underflow Packet Counter|
||1b - Overflow detected for Underflow Packet Counter|
|10-0<br>UFFRMCNT|Underflow Packet Counter This field indicates the number of packets aborted by the controller because<br>of Tx Queue Underflow. This counter is incremented each time the MAC aborts outgoing packet because<br>of underflow. The counter is cleared when this register is read with mci_be_i[0] at 1'b1. Access restriction<br>applies. Clears on read. Self-set to 1 on internal event.|



# 75.7.317 (MTL_TxQ2_Debug) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ2_Debug|D88h|



## Function 

The Queue 2 Transmit Debug register gives the debug status of various blocks related to the Transmit queue. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18<br>17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||Re|served_31|_23|||||STXSTSF||Reserv<br>e...|PTXQ||
|W||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2<br>1|0|
|R|||||Reserve|d_15_6|||||TXSTS<br>FS...|TXQS<br>TS|TWCS<br>TS|TRCSTS|TXQP<br>AUS...|
|W||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|0|



## Fields 

|Field|Function||
|---|---|---|
|31-23|Reserved.||
|Reserved_31_2<br>3|||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3985 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field<br>22-20<br>STXSTSF|Function<br>Number of Status Words in Tx Status FIFO of Queue This field indicates the current number of status in<br>the Tx Status FIFO of this queue. When the DTXSTS bit of MTL_Operation_Mode register is set to 1, this<br>field does not reflect the number of status words in Tx Status FIFO.|
|---|---|
|19<br>Reserved_19|Reserved.|
|18-16<br>PTXQ|Number of Packets in the Transmit Queue This field indicates the current number of packets in the Tx<br>Queue. When the DTXSTS bit of MTL_Operation_Mode register is set to 1, this field does not reflect the<br>number of packets in the Transmit queue.|
|15-6|Reserved.|
|Reserved_15_6||
|5<br>TXSTSFSTS|MTL Tx Status FIFO Full Status When high, this bit indicates that the MTL Tx Status FIFO is full.<br>Therefore, the MTL cannot accept any more packets for transmission.<br>0b - MTL Tx Status FIFO Full status is not detected<br>1b - MTL Tx Status FIFO Full status is detected|
|4<br>TXQSTS|MTL Tx Queue Not Empty Status When this bit is high, it indicates that the MTL Tx Queue is not empty<br>and some data is left for transmission.<br>0b - MTL Tx Queue Not Empty status is not detected<br>1b - MTL Tx Queue Not Empty status is detected|
|3<br>TWCSTS|MTL Tx Queue Write Controller Status When high, this bit indicates that the MTL Tx Queue Write<br>Controller is active, and it is transferring the data to the Tx Queue.<br>0b - MTL Tx Queue Write Controller status is not detected<br>1b - MTL Tx Queue Write Controller status is detected|
|2-1<br>TRCSTS|MTL Tx Queue Read Controller Status This field indicates the state of the Tx Queue Read Controller:<br>00b - Idle state<br>01b - Read state (transferring data to the MAC transmitter)<br>10b - Waiting for pending Tx Status from the MAC transmitter<br>11b - Flushing the Tx queue because of the Packet Abort request from the MAC|
|0<br>TXQPAUSED|Transmit Queue in Pause When this bit is high and the Rx flow control is enabled, it indicates that the Tx<br>Queue is in the Pause condition (in the full-duplex only mode) because of the following: - Reception of<br>the PFC packet for the priorities assigned to the Tx Queue when PFC is enabled - Reception of 802.3x<br>Pause packet when PFC is disabled<br>0b - Transmit Queue in Pause status is not detected<br>1b - Transmit Queue in Pause status is detected|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3986 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.318 (MTL_TxQ2_ETS_Control) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ2_ETS_Control|D90h|



## Function 

The Queue ETS Control register controls the enhanced transmission selection operation. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3987-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_7<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_31_7  AVAL Reserved_1_0<br>SLC  CC<br>W G<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-7|Reserved.|
|Reserved_31_7||
|6-4<br>SLC|Slot Count If the credit-based shaper algorithm is enabled, the software can program the number of<br>slots (of duration programmed in DMA_CH(#i)_Slot_Interval register) over which the average transmitted<br>bits per slot, provided in the MTL_TxQ(#i)_ETS_Status register, need to be computed for Queue. The<br>encoding is as follows:<br>000b - 1 slot<br>001b - 2 slots<br>010b - 4 slots<br>011b - 8 slots<br>100b - 16 slots<br>101b - Reserved|
|3<br>CC|Credit Control When this bit is set, the accumulated credit parameter in the credit-based shaper<br>algorithm logic is not reset to zero when there is positive credit and no packet to transmit in Channel<br>1. The credit accumulates even when there is no packet waiting in Channel 1 and another channel<br>is transmitting. When this bit is reset, the accumulated credit parameter in the credit-based shaper|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3987 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||algorithm logic is set to zero when there is positive credit and no packet to transmit in Channel 1. When<br>there is no packet waiting in Channel 1 and other channel is transmitting, no credit is accumulated.<br>0b - Credit Control is disabled|
||1b - Credit Control is enabled|
|2<br>AVALG|AV Algorithm When Queue 1 is programmed for AV, this field configures the scheduling algorithm for this<br>queue: This bit when set, indicates credit based shaper algorithm (CBS) is selected for Queue 1 traffic.<br>When reset, strict priority is selected.<br>0b - CBS Algorithm is disabled<br>1b - CBS Algorithm is enabled|
|1-0|Reserved.|
|Reserved_1_0||



# 75.7.319 (MTL_TxQ2_ETS_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ2_ETS_Status|D94h|



## Function 

The Queue 2 ETS Status register provides the average traffic transmitted in Queue 2. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||Reserve|d_31_24|||||||AB|S||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||AB|S||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3988 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-24|Reserved.|
|Reserved_31_2<br>4||
|23-0<br>ABS|Average Bits per Slot This field contains the average transmitted bits per slot. If AV operation<br>is enabled, this field is computed over number of slots, programmed in the SLC field of<br>MTL_TxQ(#i)_ETS_CONTROL register. The maximum value of this field is 0x6_4000 in 100 Mbps,<br>0x3E_8000 in 1000 Mbps and 9C_4000 in 2500 Mbps mode respectively. When the DCB operation is<br>enabled for Queue, this field is computed over every 10 million bit times slot (4 ms in 2500 Mbps; 10 ms<br>in 1000 Mbps; 100 ms in 100 Mbps). The maximum value is 0x989680.|



# 75.7.320 (MTL_TxQ2_Quantum_Weight) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ2_Quantum_W|D98h|
|eight||



## Function 

The Queue 2 idleSlopeCredit, Quantum or Weights register provides the average traffic transmitted in Queue 2. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||||Res|erved_31|_21|||||||ISCQW|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||ISC|QW||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-21|Reserved.|
|Reserved_31_2<br>1||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3989 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|20-0<br>ISCQW|idleSlopeCredit, Quantum or Weights - idleSlopeCredit When AV feature is enabled, this field contains<br>the idleSlopeCredit value required for the credit-based shaper algorithm for Queue 1. This is the rate<br>of change of credit in bits per cycle (40 ns for 100 Mbps; 8 ns for 1000 Mbps; 3.2 ns for 2500 Mbps)<br>when the credit is increasing. The software should program this field with computed credit in bits per<br>cycle scaled by 1,024. The maximum value is portTransmitRate, that is, 0x2000 in 1000/2500 Mbps<br>mode and 0x1000 in 100 Mbps mode. Bits[20:14] must be written to zero. - Quantum When the DCB<br>operation is enabled with DWRR algorithm for Queue 1 traffic, this field contains the quantum value in<br>bytes to be added to credit during every queue scanning cycle. The maximum value is 0x1312D0 bytes.<br>- Weights When DCB operation is enabled with WFQ algorithm for Queue 1 traffic, this field contains<br>the weight for this queue. The maximum value is 0x3FFF where weight of 0 indicates 100% bandwidth.<br>Bits[20:14] must be written to zero. When DCB operation or generic queuing operation is enabled with<br>WRR algorithm for Queue 1 traffic, this field contains the weight for this queue. The maximum value is<br>0x64. Bits [20:7] must be written to zero. - Note 1: In multiple Queue configuration this field in respective<br>per queue register must be programmed to some non-zero value when multiple queues are enabled or<br>single queue other than Q0 is enabled. This field need not be programmed when only Q0 is enabled. In<br>general, when WRR algorithm is selected a non-zero value must be programmed on both Receive and<br>Transmit. In Receive, the register is MTL_Operation_Mode register. - Note 2: For WFQ algorithm, higher<br>the programmed weights lesser the bandwidth allocated for that Transmit Queue. The finish time is not a<br>function of particular packet alone but it is as per the formula: (previous_finish_time of particular Transmit<br>Queue + (weights*packet_size)) - Note 3: The weights programmed do not correspond to the number of<br>packets but the fraction of bandwidth or time allocated for particular queue w.r.t. total BW or time.|



# 75.7.321 (MTL_TxQ2_SendSlopeCredit) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ2_SendSlopeC|D9Ch|
|redit||



## Function 

The sendSlopeCredit register contains the sendSlope credit value required for the credit-based shaper algorithm for the Queue. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3990 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3991-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_14<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserved_31_1<br>R<br>4  SSC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-14|Reserved.|
|Reserved_31_1<br>4||
|13-0<br>SSC|sendSlopeCredit Value When AV operation is enabled, this field contains the sendSlopeCredit value<br>required for credit-based shaper algorithm for Queue 1. This is the rate of change of credit in bits<br>per cycle (40 ns, 8 ns and 3.2 ns for 100 Mbps, 1000 Mbps and 2500 Mbps respectively) when the<br>credit is decreasing. The software should program this field with computed credit in bits per cycle<br>scaled by 1,024. The maximum value is portTransmitRate, that is, 0x2000 in 1000/2500 Mbps mode<br>and 0x1000 in 100 Mbps mode. This field should be programmed with absolute sendSlopeCredit value.<br>The credit-based shaper logic subtracts it from the accumulated credit when Channel 1 is selected for<br>transmission.|



# 75.7.322 (MTL_TxQ2_HiCredit) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ2_HiCredit|DA0h|



## Function 

The hiCredit register contains the hiCredit value required for the credit-based shaper algorithm for the Queue. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3991 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3992-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_29<br>HC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>HC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-29|Reserved.|
|Reserved_31_2<br>9||
|28-0<br>HC|hiCredit Value When the AV feature is enabled, this field contains the hiCredit value required for<br>the credit-based shaper algorithm. This is the maximum value that can be accumulated in the credit<br>parameter. This is specified in bits scaled by 1,024. The maximum value is maxInterferenceSize, that is,<br>best-effort maximum packet size (16,384 bytes or 131,072 bits). The value to be specified is 131,072 *<br>1,024 = 134,217,728 or 0x0800_0000.|



# 75.7.323 (MTL_TxQ2_LoCredit) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ2_LoCredit|DA4h|



## Function 

The loCredit register contains the loCredit value required for the credit-based shaper algorithm for the Queue. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3992 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3993-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_29<br>LC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>LC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-29|Reserved.|
|Reserved_31_2<br>9||
|28-0<br>LC|loCredit Value When AV operation is enabled, this field contains the loCredit value required for the<br>credit-based shaper algorithm. This is the minimum value that can be accumulated in the credit<br>parameter. This is specified in bits scaled by 1,024. The maximum value to be programmed is<br>corresponds to twice the maxFrameSize transmitted from this queue. If the maxFrameSize is 8192<br>bytes, then (8192*2) * 8 * 1024 = 134,217,728 or 0x0800_0000. Because it is a negative value, the<br>programmed value is 2's complement of the value, that is, 0x1800_0000.|



# 75.7.324 (MTL_Q2_Interrupt_Control_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_Q2_Interrupt_Contr|DACh|
|ol_Status||



## Function 

This register contains the interrupt enable and status bits for the queue 2 interrupts. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3993 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||Res|erved_31|_25|||RXOIE|||Res|erved_23|_17|||RXOV|
|W||||||||||||||||FIS|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||Reserve|d_15_10|||ABPSI|TXUIE|||Reserve|d_7_2|||ABPSI|TXUN|
|W|||||||E||||||||S|FIS|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-25|Reserved.|
|Reserved_31_2<br>5||
|24<br>RXOIE|Receive Queue Overflow Interrupt Enable When this bit is set, the Receive Queue Overflow interrupt is<br>enabled. When this bit is reset, the Receive Queue Overflow interrupt is disabled.<br>0b - Receive Queue Overflow Interrupt is disabled<br>1b - Receive Queue Overflow Interrupt is enabled|
|23-17<br>Reserved_23_1<br>7|Reserved.|
|16<br>RXOVFIS|Receive Queue Overflow Interrupt Status This bit indicates that the Receive Queue had an overflow<br>while receiving the packet. If a partial packet is transferred to the application, the overflow status is set<br>in RDES3[21]. This bit is cleared when the application writes 1 to this bit. Access restriction applies.<br>Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - Receive Queue Overflow Interrupt Status not detected<br>1b - Receive Queue Overflow Interrupt Status detected|
|15-10<br>Reserved_15_1<br>0|Reserved.|
|9<br>ABPSIE|Average Bits Per Slot Interrupt Enable When this bit is set, the MAC asserts the sbd_intr_o or mci_intr_o<br>interrupt when the average bits per slot status is updated. When this bit is cleared, the interrupt is not<br>asserted for such an event.<br>0b - Average Bits Per Slot Interrupt is disabled<br>1b - Average Bits Per Slot Interrupt is enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3994 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|8<br>TXUIE|Transmit Queue Underflow Interrupt Enable When this bit is set, the Transmit Queue Underflow interrupt<br>is enabled. When this bit is reset, the Transmit Queue Underflow interrupt is disabled.<br>0b - Transmit Queue Underflow Interrupt Status is disabled<br>1b - Transmit Queue Underflow Interrupt Status is enabled|
|7-2|Reserved.|
|Reserved_7_2||
|1<br>ABPSIS|Average Bits Per Slot Interrupt Status When set, this bit indicates that the MAC has updated the ABS<br>value. This bit is cleared when the application writes 1 to this bit. Access restriction applies. Self-set to 1<br>on internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - Average Bits Per Slot Interrupt Status not detected<br>1b - Average Bits Per Slot Interrupt Status detected|
|0<br>TXUNFIS|Transmit Queue Underflow Interrupt Status This bit indicates that the Transmit Queue had an underflow<br>while transmitting the packet. Transmission is suspended and an Underflow Error TDES3[2] is set. This<br>bit is cleared when the application writes 1 to this bit. Access restriction applies. Self-set to 1 on internal<br>event. Setting 1 clears. Setting 0 has no effect.<br>0b - Transmit Queue Underflow Interrupt Status not detected<br>1b - Transmit Queue Underflow Interrupt Status detected|



# 75.7.325 (MTL_RxQ2_Operation_Mode) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RxQ2_Operation_|DB0h|
|Mode||



## Function 

The Queue 2 Receive Operation Mode register establishes the Receive queue operating modes and command. The RFA and RFD fields are not backward compatible with the RFA and RFD fields of 4.00a release 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3995 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3996-02.png)


<!-- Start of picture text -->
Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R Reserved_31_y<br>RQS  e... RFD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv Reserv<br>R RFD  e... RFA  EHFC  DIS_T RSF  FEP  FUP  e... RTC<br>CP...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-26|Reserved.|
|Reserved_31_y||
|25-20<br>RQS|Receive Queue Size This field indicates the size of the allocated Receive queues in blocks of 256 bytes.<br>The RQS field is read-write only if the number of Rx Queues more than one, the reset value is 0x0 and<br>indicates size of 256 bytes. This means that value of 0x0 = 256 bytes, 0x1 = 512 bytes and so on. So,<br>program RQS [5:0] = 6'b001111 to allocate queue size of 4096 (4K) bytes. In general, the size of the<br>Queue = (RQS+1)*256 bytes. When the number of Rx Queues is one, the field is read-only and the<br>configured RX FIFO size in blocks of 256 bytes is reflected in the reset value. The width of this field<br>depends on the Rx memory size selected in your configuration. For example, if the memory size is 2048,<br>the width of this field is 3 bits: LOG2(2048/256) = LOG2(8) = 3 bits|
|19|Reserved.|
|Reserved_19_y||
|18-14<br>RFD|Threshold for Deactivating Flow Control (in half-duplex and full-duplex modes) These bits control the<br>threshold (fill-level of Rx queue) at which the flow control is de-asserted after activation: - 0: Full minus<br>1 KB, that is, FULL 1 KB - 1: Full minus 1.5 KB, that is, FULL 1.5 KB - 2: Full minus 2 KB, that is,<br>FULL 2 KB - 3: Full minus 2.5 KB, that is, FULL 2.5 KB - ... - 30: Full minus 16 KB, that is, FULL 16<br>KB - 31: Full minus 16.5 KB, that is, FULL 16.5 KB The de-assertion is effective only after flow control<br>is asserted. Note: The value must be programmed in such a way to make sure that the threshold is a<br>positive number. When the EHFC is set high, these values are applicable only when the Rx queue size<br>determined by the RQS field of this register, is equal to or greater than 4 KB. For a given queue size,<br>the values ranges between 0 and the encoding for FULL minus (QSIZE - 0.5 KB) and all other values<br>are illegal. Here the term FULL and QSIZE refers to the queue size determined by the RQS field of this<br>register. The width of this field depends on RX FIFO size selected during the configuration. Remaining<br>bits are reserved and read only.|
|13|Reserved.|
|Reserved_13_y||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3996 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field<br>12-8<br>RFA|Function<br>Threshold for Activating Flow Control (in half-duplex and full-duplex These bits control the threshold<br>(fill-level of Rx queue) at which the flow control is activated: For more information on encoding for this<br>field, see RFD.|
|---|---|
|7<br>EHFC|Enable Hardware Flow Control When this bit is set, the flow control signal operation, based on the<br>fill-level of Rx queue, is enabled. When reset, the flow control operation is disabled.<br>0b - Hardware Flow Control is disabled<br>1b - Hardware Flow Control is enabled|
|6<br>DIS_TCP_EF|Disable Dropping of TCP/IP Checksum Error Packets When this bit is set, the MAC does not drop the<br>packets which only have the errors detected by the Receive Checksum Offload engine. Such packets<br>have errors only in the encapsulated payload. There are no errors (including FCS error) in the Ethernet<br>packet received by the MAC. When this bit is reset, all error packets are dropped if the FEP bit is reset.<br>0b - Dropping of TCP/IP Checksum Error Packets is enabled<br>1b - Dropping of TCP/IP Checksum Error Packets is disabled|
|5<br>RSF|Receive Queue Store and Forward When this bit is set, the DWC_ether_qos reads a packet from the Rx<br>queue only after the complete packet has been written to it, ignoring the RTC field of this register. When<br>this bit is reset, the Rx queue operates in the Threshold (cut-through) mode, subject to the threshold<br>specified by the RTC field of this register.<br>0b - Receive Queue Store and Forward is disabled<br>1b - Receive Queue Store and Forward is enabled|
|4<br>FEP|Forward Error Packets When this bit is reset, the Rx queue drops packets with error status (CRC error,<br>GMII_ER, watchdog timeout, or overflow). However, if the start byte (write) pointer of a packet is already<br>transferred to the read controller side (in Threshold mode), the packet is not dropped. When this bit is<br>set, all packets except the runt error packets are forwarded to the application or DMA. If the RSF bit is<br>set and the Rx queue overflows when a partial packet is written, the packet is dropped irrespective of the<br>setting of this bit. However, if the RSF bit is reset and the Rx queue overflows when a partial packet is<br>written, a partial packet might be forwarded to the application or DMA.<br>0b - Forward Error Packets is disabled<br>1b - Forward Error Packets is enabled|
|3<br>FUP|Forward Undersized Good Packets When this bit is set, the Rx queue forwards the undersized good<br>packets (packets with no error and length less than 64 bytes), including pad-bytes and CRC. When this<br>bit is reset, the Rx queue drops all packets of less than 64 bytes, unless a packet is already transferred<br>because of the lower value of Rx Threshold, for example, RTC = 01.<br>0b - Forward Undersized Good Packets is disabled<br>1b - Forward Undersized Good Packets is enabled|
|2<br>Reserved_2|Reserved.|
|1-0<br>RTC|Receive Queue Threshold Control These bits control the threshold level of the MTL Rx queue (in bytes):<br>The received packet is transferred to the application or DMA when the packet size within the MTL<br>Rx queue is larger than the threshold. In addition, full packets with length less than the threshold are|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3997 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||automatically transferred. This field is valid only when the RSF bit is zero. This field is ignored when the<br>RSF bit is set to 1.|
||00b - 64|
||01b - 32|
||10b - 96|
||11b - 128|



# 75.7.326 (MTL_RxQ2_Missed_Packet_Overflow_Cnt) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RxQ2_Missed_Pac|DB4h|
|ket_Overflow_Cnt||



## Function 

The Queue 2 Missed Packet and Overflow Counter register contains the counter for packets missed because of Receive queue packet flush and packets discarded because of Receive queue overflow. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-3998-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>MISCN<br>R Reserved_31_28  MISPKTCNT<br>TO...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>OVFC<br>R Reserved_15_12  OVFPKTCNT<br>NTO...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function||
|---|---|---|
|31-28|Reserved.||
|Reserved_31_2|||
|8|||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3998 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|27<br>MISCNTOVF|Missed Packet Counter Overflow Bit When set, this bit indicates that the Rx Queue Missed Packet<br>Counter crossed the maximum limit. Access restriction applies. Clears on read. Self-set to 1 on internal<br>event.<br>0b - Missed Packet Counter overflow not detected<br>1b - Missed Packet Counter overflow detected|
|26-16<br>MISPKTCNT|Missed Packet Counter This field indicates the number of packets missed by the DWC_ether_qos<br>because the application asserted ari_pkt_flush_i[] for this queue. This counter is reset when this register<br>is read with mci_be_i[0] at 1b1. This counter is incremented by 1 when the DMA discards the packet<br>because of buffer unavailability. Access restriction applies. Clears on read. Self-set to 1 on internal<br>event.|
|15-12<br>Reserved_15_1<br>2|Reserved.|
|11<br>OVFCNTOVF|Overflow Counter Overflow Bit When set, this bit indicates that the Rx Queue Overflow Packet Counter<br>field crossed the maximum limit. Access restriction applies. Clears on read. Self-set to 1 on internal<br>event.<br>0b - Overflow Counter overflow not detected<br>1b - Overflow Counter overflow detected|
|10-0<br>OVFPKTCNT|Overflow Packet Counter This field indicates the number of packets discarded by the DWC_ether_qos<br>because of Receive queue overflow. This counter is incremented each time the DWC_ether_qos<br>discards an incoming packet because of overflow. This counter is reset when this register is read with<br>mci_be_i[0] at 1'b1. Access restriction applies. Clears on read. Self-set to 1 on internal event.|



# 75.7.327 (MTL_RxQ2_Debug) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RxQ2_Debug|DB8h|



## Function 

The Queue 2 Receive Debug register gives the debug status of various blocks related to the Receive queue. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3999 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-4000-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserved_31_3<br>R PRXQ<br>0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv RWCS<br>R Reserved_15_6  RXQSTS  RRCSTS<br>e... TS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-30|Reserved.|
|Reserved_31_3<br>0||
|29-16<br>PRXQ|Number of Packets in Receive Queue This field indicates the current number of packets in the<br>Rx Queue. The theoretical maximum value for this field is 256KB/16B = 16K Packets, that is,<br>Max_Queue_Size/Min_Packet_Size.|
|15-6<br>Reserved_15_6|Reserved.|
|5-4<br>RXQSTS|MTL Rx Queue Fill-Level Status This field gives the status of the fill-level of the Rx Queue:<br>00b - Rx Queue empty<br>01b - Rx Queue fill-level below flow-control deactivate threshold<br>10b - Rx Queue fill-level above flow-control activate threshold<br>11b - Rx Queue full|
|3<br>Reserved_3|Reserved.|
|2-1<br>RRCSTS|MTL Rx Queue Read Controller State This field gives the state of the Rx queue Read controller:<br>00b - Idle state<br>01b - Reading packet data<br>10b - Reading packet status (or timestamp)<br>11b - Flushing the packet data and status|
|0<br>RWCSTS|MTL Rx Queue Write Controller Active Status When high, this bit indicates that the MTL Rx queue Write<br>controller is active, and it is transferring a received packet to the Rx Queue.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4000 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - MTL Rx Queue Write Controller Active Status not detected|
||1b - MTL Rx Queue Write Controller Active Status detected|



# 75.7.328 (MTL_RxQ2_Control) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RxQ2_Control|DBCh|



## Function 

The Queue Receive Control register controls the receive arbitration and passing of received packets to the application. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||Reserve|d_31_4|||||||
|W||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R<br>W||||||Reserve|d_31_4||||||RXQ_F<br>RM...|R|XQ_WEGT|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



## Fields 

|Field|Function|
|---|---|
|31-4|Reserved.|
|Reserved_31_4||
|3<br>RXQ_FRM_AR<br>BIT|Receive Queue Packet Arbitration When this bit is set, the DWC_ether_qos drives the packet data to the<br>ARI interface such that the entire packet data of currently-selected queue is transmitted before switching<br>to other queue. When this bit is reset, the DWC_ether_qos drives the packet data to the ARI interface<br>such that the following amount of data of currently-selected queue is transmitted before switching to<br>other queue: - PBL amount of data (indicated by ari_qN_pbl_i[]) or - Complete data of a packet The<br>status and the timestamp are not a part of the PBL data. Therefore, the DWC_ether_qos drives the<br>complete status (including timestamp status) during first PBL request for the packet (in store-and-forward<br>mode) or the last PBL request for the packet (in Threshold mode).|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4001 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Receive Queue Packet Arbitration is disabled<br>1b - Receive Queue Packet Arbitration is enabled|
|2-0<br>RXQ_WEGT|Receive Queue Weight This field indicates the weight assigned to the Rx Queue 0. This field needs to<br>be programmed with one value less than the required weight, that is, reset value of 0 indicates weight of<br>1, value of 1 indicates weight of 2, and so on. The weight is used as the number of continuous PBL or<br>packets requests (depending on the RXQ_FRM_ARBIT) allocated to the queue in one arbitration cycle.<br>Note: The change in value of RXQ_WEGT takes effect only after the completion of current service round<br>or when there is change from RAA=SP to RAA=WSP algorithm. This approach is taken so that there<br>is smooth transition. For the RXQ_WEGT value to take effect at the start, the MTL_RxQ(#i)_Control<br>registers must be programmed before the MTL_Operation_Mode register.|



# 75.7.329 (DMA_Mode) 

## Offset 

|Register|Offset|
|---|---|
|DMA_Mode|1000h|



## Function 

The Bus Mode register establishes the bus operating modes for the DMA. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-4002-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserved_RND Reserved_TND Reserv Reserv<br>R Reserved_31_24<br>F  F  e... e... INTM<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv Reserv Reserv<br>R Reserved_7_5<br>e... PR  TXPR  e... ARBC  e... TAA  DA  SWR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-24|Reserved.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4002 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|Reserved_31_2<br>4||
|23-22<br>Reserved_RND<br>F|Reserved.|
|21-20|Reserved.|
|Reserved_TND<br>F||
|19|Reserved.|
|Reserved_DCH<br>E||
|18<br>Reserved_18|Reserved.|
|17-16<br>INTM|Interrupt Mode This field defines the interrupt mode of DWC_ether_qos. The behavior of the following<br>outputs change depending on the following settings: - sbd_perch_tx_intr_o[] (Transmit Per Channel<br>Interrupt) - sbd_perch_rx_intr_o[] (Receive Per Channel Interrupt) - sbd_intr_o (Common Interrupt) It also<br>changes the behavior of the RI/TI bits in the DMA_CH0_Status. - 00: sbd_perch_* are pulse signals<br>for each TX/RX packet transfer completion events (irrespective of whether corresponding interrupts are<br>enabled) for which IOC bits are enabled in descriptor. sbd_intr_o is also asserted when corresponding<br>interrupts are enabled and cleared only when software clears the corresponding RI/TI status bits. - 01:<br>sbd_perch_* are level signals asserted on TX/RX packet transfer completion event when corresponding<br>interrupts are enabled and de-asserted when the software clears the corresponding RI/TI status bits.<br>The sbd_intr_o is not asserted for these TX/RX packet transfer completion events. - 10: sbd_perch_*<br>are level signals asserted on TX/RX packet transfer completion event when corresponding interrupts are<br>enabled and de-asserted when the software clears the corresponding RI/TI status bits. However, the<br>signal is asserted again if the same event occurred again before it was cleared. The sbd_intr_o is not<br>asserted for these TX/RX packet transfer completion events. - 11: Reserved For more details, see Table<br>"DWC_ether_qos Transfer Complete Interrupt Behavior".<br>00b - See above description<br>01b - See above description<br>10b - See above description<br>11b - Reserved|
|15<br>Reserved_15|Reserved.|
|14-12<br>PR|Priority Ratio These bits control the priority ratio in weighted round-robin arbitration between the Rx DMA<br>and Tx DMA. These bits are valid only when the DA bit is reset. The priority ratio is Rx:Tx or Tx:Rx<br>depending on whether the TXPR bit is reset or set.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4003 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function<br>000b - The priority ratio is 1:1<br>001b - The priority ratio is 2:1<br>010b - The priority ratio is 3:1<br>011b - The priority ratio is 4:1<br>100b - The priority ratio is 5:1<br>101b - The priority ratio is 6:1<br>110b - The priority ratio is 7:1<br>111b - The priority ratio is 8:1|
|---|---|
|11<br>TXPR|Transmit Priority When set, this bit indicates that the Tx DMA has higher priority than the Rx<br>DMA during arbitration for the system-side bus or Descriptor reads from DCACHE memory when<br>DWC_EQOS_DCEXT is enabled<br>0b - Transmit Priority is disabled<br>1b - Transmit Priority is enabled|
|10<br>Reserved_SCS<br>W|Reserved.|
|9<br>ARBC|ARBC is NXP Reserved, This field must be set to "0". - This field is reserved for NXP Internal use, and<br>must always be set to "0" unless instructed by NXP. - Setting this field to "1" might cause unexpected<br>behavior in the IP.<br>0b - NXP reserved field disabled<br>1b - NXP reserved field enabled up on NXP request|
|8<br>Reserved_DSP<br>W|Reserved.|
|7-5<br>Reserved_7_5|Reserved.|
|4-2<br>TAA|Transmit Arbitration Algorithm This field is used to select the arbitration algorithm for the Transmit side<br>when multiple Tx DMAs are selected.<br>000b - Fixed priority (Channel 0 has the lowest priority and the last channel has the highest<br>priority)<br>001b - Weighted Strict Priority (WSP)<br>010b - Weighted Round-Robin (WRR)<br>011b - Reserved (for 3'b011 to 3'b111)|
|1|DMA Tx or Rx Arbitration Scheme This bit specifies the arbitration scheme between the Transmit and<br>Receive paths of all channels: - 0: Weighted Round-Robin with Rx:Tx or Tx:Rx The priority between the|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4004 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|DA|paths is according to the priority specified in Bits[14:12] and the priority weight is specified in the TXPR<br>bit. - 1: Fixed Priority The Tx path has priority over the Rx path when the TXPR bit is set. Otherwise, the<br>Rx path has priority over the Tx path.<br>0b - Weighted Round-Robin with Rx:Tx or Tx:Rx<br>1b - Fixed Priority|
|0<br>SWR|Software Reset When this bit is set, the MAC and the DMA controller reset the logic and all internal<br>registers of the DMA, MTL, and MAC. This bit is automatically cleared after the reset operation is<br>complete in all DWC_ether_qos clock domains. Before reprogramming any DWC_ether_qos register,<br>a value of zero should be read in this bit. This bit must be read at least 4 CSR clock cycles after it<br>is written to 1. Note: The reset operation is complete only when all resets in all active clock domains<br>are de-asserted. Therefore, it is essential that all PHY inputs clocks (applicable for the selected PHY<br>interface) are present for software reset completion. The time to complete the software reset operation<br>depends on the frequency of the slowest active clock. Access restriction applies. Setting 1 sets. Self-<br>cleared. Setting 0 has no effect.<br>0b - Software Reset is disabled<br>1b - Software Reset is enabled|



# 75.7.330 (DMA_SysBus_Mode) 

## Offset 

|Register|Offset|
|---|---|
|DMA_SysBus_Mode|1004h|



## Function 

The System Bus mode register controls the behavior of the AHB or AXI master. It mainly controls burst splitting and number of outstanding requests. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-4005-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv Reserv Reserved_WR_OSR_LM Reserved_RD_OSR_LM<br>R Reserved_29_y  Reserved_23_y<br>e... e... T  T<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv Reserv Reserv Reserv Reserv Reserv Reserv Reserv Reserv Reserv<br>R Reserved_9_8<br>RB  MB  e... AAL  e... e... e... e... e... e... e... e... e... FB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4005 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31|Reserved.|
|Reserved_EN_L<br>PI||
|30|Reserved.|
|Reserved_LPI_<br>XIT_PKT||
|29-27|Reserved.|
|Reserved_29_y||
|26-24|Reserved.|
|Reserved_WR_<br>OSR_LMT||
|23-19|Reserved.|
|Reserved_23_y||
|18-16|Reserved.|
|Reserved_RD_<br>OSR_LMT||
|15<br>RB|Rebuild INCRx Burst When this bit is set high and the AHB master gets SPLIT, RETRY, or Early Burst<br>Termination (EBT) response, the AHB master interface rebuilds the pending beats of any initiated burst<br>transfer with INCRx and SINGLE transfers. By default, the AHB master interface rebuilds the pending<br>beats of an EBT with an unspecified (INCR) burst.<br>0b - Rebuild INCRx Burst is disabled<br>1b - Rebuild INCRx Burst is enabled|
|14<br>MB|Mixed Burst When this bit is high and the FB bit is low, the AHB master performs undefined bursts<br>transfers (INCR) for burst length of 16 or more. For burst length of 16 or less, the AHB master performs<br>fixed burst transfers (INCRx and SINGLE).<br>0b - Mixed Burst is disabled<br>1b - Mixed Burst is enabled|
|13|Reserved.|
|Reserved_ONE<br>KBBE||
|12<br>AAL|Address-Aligned Beats When this bit is set to 1, the EQOS-AXI or EQOS-AHB master performs address-<br>aligned burst transfers on Read and Write channels. When this bit is set to 0, the EQOS-AXI or<br>EQOS-AHB master performs burst transfers on Read and Write channels without aligning to address<br>boundaries.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4006 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function<br>0b - Address-Aligned Beats is disabled<br>1b - Address-Aligned Beats is enabled|
|---|---|
|11<br>Reserved_EAM<br>E|Reserved.|
|10<br>Reserved_AAL<br>E|Reserved.|
|9-8|Reserved.|
|Reserved_9_8||
|7<br>Reserved_BLE<br>N256|Reserved.|
|6|Reserved.|
|Reserved_BLE<br>N128||
|5|Reserved.|
|Reserved_BLE<br>N64||
|4|Reserved.|
|Reserved_BLE<br>N32||
|3|Reserved.|
|Reserved_BLE<br>N16||
|2|Reserved.|
|Reserved_BLE<br>N8||
|1<br>Reserved_BLE<br>N4|Reserved.|
|0<br>FB|Fixed Burst Length - 1: AHB master initiates burst transfers of specified length (INCRx or SINGLE). - 0:<br>AHB master initiates transfers of unspecified length (INCR) or SINGLE transfers.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4007 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Fixed Burst Length is disabled|
||1b - Fixed Burst Length is enabled|



# 75.7.331 (DMA_Interrupt_Status) 

## Offset 

|Register|Offset|
|---|---|
|DMA_Interrupt_Status|1008h|



## Function 

The application reads this Interrupt Status register during interrupt service routine or polling to determine the interrupt status of DMA channels, MTL queues, and the MAC. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-4008-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_18  MACIS  MTLIS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv Reserv Reserv Reserv Reserv<br>R Reserved_15_8  DC2IS  DC1IS  DC0IS<br>e... e... e... e... e...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-18|Reserved.|
|Reserved_31_1<br>8||
|17<br>MACIS|MAC Interrupt Status This bit indicates an interrupt event in the MAC. To reset this bit to 1'b0, the<br>software must read the corresponding register in the MAC to get the exact cause of the interrupt and<br>clear its source.|
||0b - MAC Interrupt Status not detected|
||1b - MAC Interrupt Status detected|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4008 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|16<br>MTLIS|MTL Interrupt Status This bit indicates an interrupt event in the MTL. To reset this bit to 1'b0, the<br>software must read the corresponding register in the MTL to get the exact cause of the interrupt and<br>clear its source.<br>0b - MTL Interrupt Status not detected<br>1b - MTL Interrupt Status detected|
|15-8<br>Reserved_15_8|Reserved.|
|7<br>Reserved_DC7I<br>S|Reserved.|
|6<br>Reserved_DC6I<br>S|Reserved.|
|5<br>Reserved_DC5I<br>S|Reserved.|
|4<br>Reserved_DC4I<br>S|Reserved.|
|3<br>Reserved_DC3I<br>S<br>2<br>DC2IS|Reserved.<br>DMA Channel 2 Interrupt Status This bit indicates an interrupt event in DMA Channel 2. To reset this bit<br>to 1'b0, the software must read the corresponding register in DMA Channel 2 to get the exact cause of<br>the interrupt and clear its source.<br>0b - DMA Channel 2 Interrupt Status not detected<br>1b - DMA Channel 2 Interrupt Status detected|
|1<br>DC1IS|DMA Channel 1 Interrupt Status This bit indicates an interrupt event in DMA Channel 1. To reset this bit<br>to 1'b0, the software must read the corresponding register in DMA Channel 1 to get the exact cause of<br>the interrupt and clear its source.<br>0b - DMA Channel 1 Interrupt Status not detected<br>1b - DMA Channel 1 Interrupt Status detected|
|0<br>DC0IS|DMA Channel 0 Interrupt Status This bit indicates an interrupt event in DMA Channel 0. To reset this bit<br>to 1'b0, the software must read the corresponding register in DMA Channel 0 to get the exact cause of<br>the interrupt and clear its source.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4009 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - DMA Channel 0 Interrupt Status not detected|
||1b - DMA Channel 0 Interrupt Status detected|



# 75.7.332 (DMA_Debug_Status0) 

## Offset 

|Register|Offset|
|---|---|
|DMA_Debug_Status0|100Ch|



## Function 

The Debug Status 0 register gives the Receive and Transmit process status for DMA Channel 0-Channel 2 for debugging purpose. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||TPS|2|||RPS|2|||TP|S1|||R|PS1||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||TPS|0|||RPS|0||||Reserv|ed_7_2|||Reserv<br>e...|AXWH<br>STS|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-28<br>TPS2|DMA Channel 2 Transmit Process State This field indicates the Tx DMA FSM state for Channel 2. The<br>MSB of this field always returns 0. This field does not generate an interrupt.<br>0000b - Stopped (Reset or Stop Transmit Command issued)<br>0001b - Running (Fetching Tx Transfer Descriptor)<br>0010b - Running (Waiting for status)|
||0011b - Running (Reading Data from system memory buffer and queuing it to the Tx buffer (Tx<br>FIFO))|
||0100b - Timestamp write state|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4010 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

Field Function 0101b - Reserved for future use 0110b - Suspended (Tx Descriptor Unavailable or Tx Buffer Underflow) 0111b - Running (Closing Tx Descriptor) 27-24 DMA Channel 2 Receive Process State This field indicates the Rx DMA FSM state for Channel 2. The MSB of this field always returns 0. This field does not generate an interrupt. RPS2 0000b - Stopped (Reset or Stop Receive Command issued) 0001b - Running (Fetching Rx Transfer Descriptor) 0010b - Reserved for future use 0011b - Running (Waiting for Rx packet) 0100b - Suspended (Rx Descriptor Unavailable) 0101b - Running (Closing the Rx Descriptor) 0110b - Timestamp write state 0111b - Running (Transferring the received packet data from the Rx buffer to the system memory) 23-20 DMA Channel 1 Transmit Process State This field indicates the Tx DMA FSM state for Channel 1. The MSB of this field always returns 0. This field does not generate an interrupt. TPS1 0000b - Stopped (Reset or Stop Transmit Command issued) 0001b - Running (Fetching Tx Transfer Descriptor) 0010b - Running (Waiting for status) 0011b - Running (Reading Data from system memory buffer and queuing it to the Tx buffer (Tx FIFO)) 0100b - Timestamp write state 0101b - Reserved for future use 0110b - Suspended (Tx Descriptor Unavailable or Tx Buffer Underflow) 0111b - Running (Closing Tx Descriptor) 19-16 DMA Channel 1 Receive Process State This field indicates the Rx DMA FSM state for Channel 1. The MSB of this field always returns 0. This field does not generate an interrupt. RPS1 0000b - Stopped (Reset or Stop Receive Command issued) 0001b - Running (Fetching Rx Transfer Descriptor) 0010b - Reserved for future use 0011b - Running (Waiting for Rx packet) 0100b - Suspended (Rx Descriptor Unavailable) 0101b - Running (Closing the Rx Descriptor) 0110b - Timestamp write state 0111b - Running (Transferring the received packet data from the Rx buffer to the system memory) 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4011 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|15-12<br>TPS0|DMA Channel 0 Transmit Process State This field indicates the Tx DMA FSM state for Channel 0. The<br>MSB of this field always returns 0. This field does not generate an interrupt.<br>0000b - Stopped (Reset or Stop Transmit Command issued)<br>0001b - Running (Fetching Tx Transfer Descriptor)<br>0010b - Running (Waiting for status)<br>0011b - Running (Reading Data from system memory buffer and queuing it to the Tx buffer (Tx<br>FIFO))<br>0100b - Timestamp write state<br>0101b - Reserved for future use<br>0110b - Suspended (Tx Descriptor Unavailable or Tx Buffer Underflow)<br>0111b - Running (Closing Tx Descriptor)|
|11-8<br>RPS0|DMA Channel 0 Receive Process State This field indicates the Rx DMA FSM state for Channel 0. The<br>MSB of this field always returns 0. This field does not generate an interrupt.<br>0000b - Stopped (Reset or Stop Receive Command issued)<br>0001b - Running (Fetching Rx Transfer Descriptor)<br>0010b - Reserved for future use<br>0011b - Running (Waiting for Rx packet)<br>0100b - Suspended (Rx Descriptor Unavailable)<br>0101b - Running (Closing the Rx Descriptor)<br>0110b - Timestamp write state<br>0111b - Running (Transferring the received packet data from the Rx buffer to the system memory)|
|7-2<br>Reserved_7_2|Reserved.|
|1|Reserved.|
|Reserved_AXR<br>HSTS||
|0<br>AXWHSTS|AHB Master Status When high, this bit indicates that the AHB master FSMs are in the non-idle state.<br>0b - AXI Master Write Channel or AHB Master Status not detected<br>1b - AXI Master Write Channel or AHB Master Status detected|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4012 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.333 (DMA_TBS_CTRL0) 

## Offset 

|Register|Offset|
|---|---|
|DMA_TBS_CTRL0|1050h|



## Function 

This register is used to control the TBS attributes. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-4013-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>FTOS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv<br>R Reserved_3_1<br>FTOS  e... FGOS  FTOV<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-8<br>FTOS|Fetch Time Offset The value in units of 256 nanoseconds, that has to be deducted from the Launch time<br>to compute the Fetch Time. Max value: 999,999,999 ns, additionally should be smaller than CTR-1 value<br>when ESTM mode is set since this value is a modulo CTR value.|
|7|Reserved.|
|Reserved_7||
|6-4<br>FGOS|Fetch GSN Offset The number GSN slots that must be deducted from the Launch GSN to compute the<br>Fetch GSN. Value valid only when FTOV is set.|
|3-1|Reserved.|
|Reserved_3_1||
|0<br>FTOV|Fetch Time Offset Valid When set indicates the FTOS field is valid. When not set, indicates the Fetch<br>Offset is not valid and the DMA engine can fetch the frames from host memory without any time<br>restrictions.|
||0b - Fetch Time Offset is invalid<br>1b - Fetch Time Offset is valid|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4013 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.334 (DMA_TBS_CTRL1) 

## Offset 

|Register<br>DMA_TBS_CTRL1|Offset<br>1054h|
|---|---|



## Function 

This register is used to control the TBS attributes. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-4014-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>FTOS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv<br>R Reserved_3_1<br>FTOS  e... FGOS  FTOV<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-8<br>FTOS|Fetch Time Offset The value in units of 256 nanoseconds, that has to be deducted from the Launch time<br>to compute the Fetch Time. Max value: 999,999,999 ns, additionally should be smaller than CTR-1 value<br>when ESTM mode is set since this value is a modulo CTR value.|
|7|Reserved.|
|Reserved_7||
|6-4<br>FGOS|Fetch GSN Offset The number GSN slots that must be deducted from the Launch GSN to compute the<br>Fetch GSN. Value valid only when FTOV is set.|
|3-1|Reserved.|
|Reserved_3_1||
|0<br>FTOV|Fetch Time Offset Valid When set indicates the FTOS field is valid. When not set, indicates the Fetch<br>Offset is not valid and the DMA engine can fetch the frames from host memory without any time<br>restrictions.|
||0b - Fetch Time Offset is invalid<br>1b - Fetch Time Offset is valid|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4014 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.335 (DMA_TBS_CTRL2) 

## Offset 

|Register|Offset|
|---|---|
|DMA_TBS_CTRL2|1058h|



## Function 

This register is used to control the TBS attributes. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-4015-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>FTOS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv<br>R Reserved_3_1<br>FTOS  e... FGOS  FTOV<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-8<br>FTOS|Fetch Time Offset The value in units of 256 nanoseconds, that has to be deducted from the Launch time<br>to compute the Fetch Time. Max value: 999,999,999 ns, additionally should be smaller than CTR-1 value<br>when ESTM mode is set since this value is a modulo CTR value.|
|7|Reserved.|
|Reserved_7||
|6-4<br>FGOS|Fetch GSN Offset The number GSN slots that must be deducted from the Launch GSN to compute the<br>Fetch GSN. Value valid only when FTOV is set.|
|3-1|Reserved.|
|Reserved_3_1||
|0<br>FTOV|Fetch Time Offset Valid When set indicates the FTOS field is valid. When not set, indicates the Fetch<br>Offset is not valid and the DMA engine can fetch the frames from host memory without any time<br>restrictions.|
||0b - Fetch Time Offset is invalid<br>1b - Fetch Time Offset is valid|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4015 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.336 (DMA_TBS_CTRL3) 

## Offset 

|Register|Offset|
|---|---|
|DMA_TBS_CTRL3|105Ch|



## Function 

This register is used to control the TBS attributes. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-4016-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>FTOS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv<br>R Reserved_3_1<br>FTOS  e... FGOS  FTOV<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-8<br>FTOS|Fetch Time Offset The value in units of 256 nanoseconds, that has to be deducted from the Launch time<br>to compute the Fetch Time. Max value: 999,999,999 ns, additionally should be smaller than CTR-1 value<br>when ESTM mode is set since this value is a modulo CTR value.|
|7|Reserved.|
|Reserved_7||
|6-4<br>FGOS|Fetch GSN Offset The number GSN slots that must be deducted from the Launch GSN to compute the<br>Fetch GSN. Value valid only when FTOV is set.|
|3-1|Reserved.|
|Reserved_3_1||
|0<br>FTOV|Fetch Time Offset Valid When set indicates the FTOS field is valid. When not set, indicates the Fetch<br>Offset is not valid and the DMA engine can fetch the frames from host memory without any time<br>restrictions.|
||0b - Fetch Time Offset is invalid<br>1b - Fetch Time Offset is valid|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4016 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.337 (DMA_Safety_Interrupt_Status) 

## Offset 

|Register|Offset|
|---|---|
|DMA_Safety_Interrupt_St<br>atus|1080h|



## Function 

This register indicates summary (whether error occured in DMA/MTL/MAC and correctable/uncorrectable) of the Automotive Safety related error interrupts. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-4017-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R MCSIS  MSUIS MSCIS  Reserved_27_2<br>e...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_27_2  DEUIS  DECIS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31<br>MCSIS|MAC Safety Uncorrectable Interrupt Status Indicates a uncorrectable Safety related Interrupt is set in the<br>MAC module. MAC_DPP_FSM_Interrupt_Status register should be read when this bit is set, to get the<br>cause of the Safety Interrupt in MAC.|
||0b - MAC Safety Uncorrectable Interrupt Status not detected<br>1b - MAC Safety Uncorrectable Interrupt Status detected|
|30|Reserved.|
|Reserved_30||
|29<br>MSUIS|MTL Safety Uncorrectable error Interrupt Status This bit indicates an uncorrectable error interrupt event<br>in MTL. To get exact cause of the interrupt the software should read the MTL_Safety_Interrupt_Status<br>register.|
||0b - MTL Safety Uncorrectable error Interrupt Status not detected<br>1b - MTL Safety Uncorrectable error Interrupt Status detected|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4017 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|28<br>MSCIS|MTL Safety Correctable error Interrupt Status This bit indicates a correctable error interrupt event in<br>MTL. To get exact cause of the interrupt the software should read the MTL_Safety_Interrupt_Status<br>register.<br>0b - MTL Safety Correctable error Interrupt Status not detected<br>1b - MTL Safety Correctable error Interrupt Status detected|
|27-2<br>Reserved_27_2|Reserved.|
|1<br>DEUIS|DMA ECC Uncorrectable error Interrupt Status This bit indicates an interrupt event in the DMA<br>ECC safety feature. To get the exact cause of the interrupt the application should read the<br>DMA_ECC_Interrupt_Status register.<br>0b - DMA ECC Uncorrectable error Interrupt Status not detected<br>1b - DMA ECC Uncorrectable error Interrupt Status detected|
|0<br>DECIS|DMA ECC Correctable error Interrupt Status This bit indicates an interrupt event in the DMA<br>ECC safety feature. To get the exact cause of the interrupt the application should read the<br>DMA_ECC_Interrupt_Status register.<br>0b - DMA ECC Correctable error Interrupt Status not detected<br>1b - DMA ECC Correctable error Interrupt Status detected|



# 75.7.338 (DMA_CH0_Control) 

## Offset 

|Register|Offset|
|---|---|
|DMA_CH0_Control|1100h|



## Function 

The DMA Channeli Control register specifies the MSS value for segmentation, length to skip between two descriptors, and also the features such as header splitting and 8xPBL mode. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4018 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-4019-01.png)


<!-- Start of picture text -->
Gigabit Ethernet Media Access Controller (GMAC)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R Reserved_31_25  Reserved_23_21<br>SPH  DSL  e... PBLx8<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserved_15_1<br>R Reserved_MSS<br>4<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

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

4019 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-4020-03.png)


<!-- Start of picture text -->
Field Function<br>15-14 Reserved.<br>Reserved_15_1<br>4<br>13-0 Reserved.<br>Reserved_MSS<br><!-- End of picture text -->

# 75.7.339 (DMA_CH0_Tx_Control) 

## Offset 

|Register|Offset|
|---|---|
|DMA_CH0_Tx_Control|1104h|



## Function 

The DMA Channeli Transmit Control register controls the Tx features such as PBL, TCP segmentation, and Tx Channel weights. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-4020-10.png)


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

4020 / 4640 

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

4021 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Operate on Second Packet disabled<br>1b - Operate on Second Packet enabled|
|3-1<br>TCW|Transmit Channel Weight This field indicates the weight assigned to the corresponding Transmit<br>channel. When reset is complete, this field is set to 0 for all channels by default, resulting in equal<br>weights to all channels.|
|0<br>ST|Start or Stop Transmission Command When this bit is set, transmission is placed in the Running state.<br>The DMA checks the Transmit list at the current position for a packet to be transmitted. The DMA tries<br>to acquire descriptor from either of the following positions: - The current position in the list This is the<br>base address of the Transmit list set by the DMA_CH0_TxDesc_List_Address register. - The position<br>at which the transmission was previously stopped If the DMA does not own the current descriptor, the<br>transmission enters the Suspended state and the TBU bit of the DMA_CH0_Status register is set. The<br>Start Transmission command is effective only when the transmission is stopped. If the command is<br>issued before setting the DMA_CH0_TxDesc_List_Address register, the DMA behavior is unpredictable.<br>When this bit is reset, the transmission process is placed in the Stopped state after completing the<br>transmission of the current packet. The Next Descriptor position in the Transmit list is saved, and it<br>becomes the current position when the transmission is restarted. To change the list address, you need<br>to program DMA_CH0_TxDesc_List_Address register with a new value when this bit is reset. The new<br>value is considered when this bit is set again. The stop transmission command is effective only when the<br>transmission of the current packet is complete or the transmission is in the Suspended state.<br>0b - Stop Transmission Command<br>1b - Start Transmission Command|



# 75.7.340 (DMA_CH0_Rx_Control) 

## Offset 

|Register|Offset|
|---|---|
|DMA_CH0_Rx_Control|1108h|



## Function 

The DMA Channeli Receive Control register controls the Rx features such as PBL, buffer size, and extended status. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4022 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-4023-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R Reserved_30_28  Reserved_RQOS<br>RPF  e... ERIC  RxPBL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv<br>R RBSZ_x_0<br>e... RBSZ_13_y  SR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

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

4023 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|21-16<br>RxPBL|Receive Programmable Burst Length These bits indicate the maximum number of beats to be transferred<br>in one DMA block data transfer. The DMA always attempts max burst as specified in PBL each time it<br>starts a burst transfer on the application bus. You can program PBL with any of the following values:<br>1, 2, 4, 8, 16, or 32. Any other value results in undefined behavior. To transfer more than 32 beats,<br>perform the following steps: 1. Set the 8xPBL mode in the DMA_CH0_Control register. 2. Set the RxPBL.<br>Note: The maximum value of RxPBL must be less than or equal to half the Rx Queue size (RQS field<br>of MTL_RxQ(#i)_Operation_Mode register) in terms of beats. This is required so that the Rx Queue has<br>space to store at least another Rx PBL worth of data while the Rx DMA is transferring a block of data.<br>For example, in 64-bit data width configurations the total locations in Rx Queue of size 512 bytes is 64,<br>so RxPBL and 8xPBL needs to be programmed to less than or equal to 32.|
|15|Reserved.|
|Reserved_15||
|14-4<br>RBSZ_13_y|Receive Buffer size High RBSZ[13:0] is split into two fields higher RBSZ_13_y and lower RBSZ_x_0.<br>The RBSZ[13:0] field indicates the size of the Rx buffers specified in bytes. The maximum buffer size<br>is limited to 16K bytes. The buffer size is applicable to payload buffers when split headers are enabled.<br>Note: The buffer size must be a multiple of 4, 8, or 16 depending on the data bus widths (32-bit, 64-bit,<br>or 128-bit respectively). This is required even if the value of buffer address pointer is not aligned to data<br>bus width. Hence the lower RBSZ_x_0 bits are read-only and the value is considered as all-zero. Thus<br>the RBSZ_13_y indicates the buffer size in terms of locations (with the width same as bus-width).|
|3-1<br>RBSZ_x_0|Receive Buffer size Low RBSZ[13:0] is split into two fields RBSZ_13_y and RBSZ_x_0. The RBSZ_x_0 is<br>the lower field whose width is based on data bus width of the configuration. This field is of width 2, 3, or 4<br>bits for 32-bit, 64-bit, or 128-bit data bus width respectively. This field is read-only (RO).|
|0<br>SR|Start or Stop Receive When this bit is set, the DMA tries to acquire the descriptor from the<br>Receive list and processes the incoming packets. The DMA tries to acquire descriptor from either<br>of the following positions: - The current position in the list This is the address set by the<br>DMA_CH0_RxDesc_List_Address register. - The position at which the Rx process was previously<br>stopped If the DMA does not own the current descriptor, the reception is suspended and the RBU bit of<br>the DMA_CH0_Status register is set. The Start Receive command is effective only when the reception<br>is stopped. If the command is issued before setting the DMA_CH0_RxDesc_List_Address register, the<br>DMA behavior is unpredictable. When this bit is reset, the Rx DMA operation is stopped after the transfer<br>of the current packet. The next descriptor position in the Receive list is saved, and it becomes the current<br>position after the Rx process is restarted. The Stop Receive command is effective only when the Rx<br>process is in the Running (waiting for Rx packet) or Suspended state.<br>0b - Stop Receive<br>1b - Start Receive|



# 75.7.341 (DMA_CH0_TxDesc_List_Address) 

## Offset 

|Register|Offset|
|---|---|
|DMA_CH0_TxDesc_List_|1114h|
|Address||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4024 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Function 

The Channeli Tx Descriptor List Address register points the DMA to the start of Transmit descriptor list. The descriptor lists reside in the physical memory space of the application and must be Word, Dword, or Lword-aligned (for 32-bit, 64-bit, or 128-bit data bus). The DMA internally converts it to bus width aligned address by making the corresponding LSB to low. You can write to this register only when the Tx DMA has stopped, that is, the ST bit is set to zero in DMA_CH0_Tx_Control register. When stopped, this register can be written with a new descriptor list address. When you set the ST bit to 1, the DMA takes the newly-programmed descriptor base address. If this register is not changed when the ST bit is set to 0, the DMA takes the descriptor address where it was stopped earlier. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-4025-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>TDESLA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_LSb<br>TDESLA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-3<br>TDESLA|Start of Transmit List This field contains the base address of the first descriptor in the Transmit descriptor<br>list. The DMA ignores the LSB bits (1:0, 2:0, or 3:0) for 32-bit, 64-bit, or 128-bit bus width and internally<br>takes these bits as all-zero. Therefore, these LSB bits are read-only (RO). The width of this field depends<br>on the configuration: - 31:2 for 32-bit configuration - 31:3 for 64-bit configuration - 31:4 for 128-bit<br>configuration|
|2-0|Reserved.|
|Reserved_LSb||



# 75.7.342 (DMA_CH0_RxDesc_List_Address) 

## Offset 

|Register|Offset|
|---|---|
|DMA_CH0_RxDesc_List|111Ch|
|_Address||



## Function 

The Channeli Rx Descriptor List Address register points the DMA to the start of Receive descriptor list. This register points to the start of the Receive Descriptor List. The descriptor lists reside in the physical memory space of the application and must be Word, Dword, or Lword-aligned (for 32-bit, 64-bit, or 128-bit data bus). The DMA internally converts it to bus width aligned address by making the corresponding LS bits low. Writing to this register is permitted only when reception is stopped. When stopped, this register must be written to before the receive Start command is given. You can write to this register only 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4025 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

when Rx DMA has stopped, that is, SR bit is set to zero in DMA_CH0_Rx_Control register. When stopped, this register can be written with a new descriptor list address. When you set the SR bit to 1, the DMA takes the newly programmed descriptor base address. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-4026-04.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>RDESLA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_LSb<br>RDESLA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-3<br>RDESLA|Start of Receive List This field contains the base address of the first descriptor in the Rx Descriptor list.<br>The DMA ignores the LSB bits (1:0, 2:0, or 3:0) for 32-bit, 64-bit, or 128-bit bus width and internally<br>takes these bits as all-zero. Therefore, these LSB bits are read-only (RO). The width of this field depends<br>on the configuration: - 31:2 for 32-bit configuration - 31:3 for 64-bit configuration - 31:4 for 128-bit<br>configuration|
|2-0|Reserved.|
|Reserved_LSb||



# 75.7.343 (DMA_CH0_TxDesc_Tail_Pointer) 

## Offset 

|Register|Offset|
|---|---|
|DMA_CH0_TxDesc_Tail_|1120h|
|Pointer||



## Function 

The Channeli Tx Descriptor Tail Pointer register points to an offset from the base and indicates the location of the last valid descriptor. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4026 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-4027-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>TDTP<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_LSb<br>TDTP<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-3<br>TDTP|Transmit Descriptor Tail Pointer This field contains the tail pointer for the Tx descriptor ring. The software<br>writes the tail pointer to add more descriptors to the Tx channel. The hardware tries to transmit all<br>packets referenced by the descriptors between the head and the tail pointer registers. The width of this<br>field depends on the configuration: - 31:2 for 32-bit configuration - 31:3 for 64-bit configuration - 31:4 for<br>128-bit configuration|
|2-0|Reserved.|
|Reserved_LSb||



# 75.7.344 (DMA_CH0_RxDesc_Tail_Pointer) 

## Offset 

|Register|Offset|
|---|---|
|DMA_CH0_RxDesc_Tail<br>_Pointer|1128h|



## Function 

The Channeli Rx Descriptor Tail Pointer Points to an offset from the base and indicates the location of the last valid descriptor. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4027 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-4028-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>RDTP<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_LSb<br>RDTP<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-3<br>RDTP|Receive Descriptor Tail Pointer This field contains the tail pointer for the Rx descriptor ring. The software<br>writes the tail pointer to add more descriptors to the Rx channel. The hardware tries to write all received<br>packets to the descriptors referenced between the head and the tail pointer registers. The width of this<br>field depends on the configuration: - 31:2 for 32-bit configuration - 31:3 for 64-bit configuration - 31:4 for<br>128-bit configuration|
|2-0|Reserved.|
|Reserved_LSb||



# 75.7.345 (DMA_CH0_TxDesc_Ring_Length) 

## Offset 

|Register|Offset|
|---|---|
|DMA_CH0_TxDesc_Ring<br>_Length|112Ch|



## Function 

The Tx Descriptor Ring Length register contains the length of the Transmit descriptor ring. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4028 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-4029-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved_31_10<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_31_10<br>TDRL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-10|Reserved.|
|Reserved_31_1<br>0||
|9-0<br>TDRL|Transmit Descriptor Ring Length This field sets the maximum number of Tx descriptors in the circular<br>descriptor ring. The maximum number of descriptors is limited to 1K descriptors. NXP recommends a<br>minimum ring descriptor length of 4. For example, You can program any value up to 0x3FF in this field.<br>This field is 10 bits wide, if you program 0x3FF, you can have 1024 descriptors. If you want to have 10<br>descriptors, program it to a value of 0x9.|



# 75.7.346 (DMA_CH0_Rx_Control2) 

## Offset 

|Register|Offset|
|---|---|
|DMA_CH0_Rx_Control2|1130h|



## Function 

The Channeli Receive Control register controls the Rx features such as Rx Descriptor Ring Length and Alternate Rx Buffer Size. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4029 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-4030-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R Reserved_31_24<br>ARBS  e...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved_x_10<br>RDRL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-24|Reserved.|
|Reserved_31_2<br>4||
|23-17<br>ARBS|Alternate Receive Buffer Size Indicates size in bytes for Buffer 1 when ARBS is programmed to a<br>non-zero value (when split header feature is not enabled). When split header feature is enabled, ARBS<br>indicates the buffer size for header data. The maximum alternate buffer is limited to 1020, 1016 or<br>1008-bytes depending on the data bus widths (32-bit, 64-bit, or 128-bit respectively). When ARBS=0, Rx<br>Buffer1 and Rx Buffer2 sizes are based on RBSZ field of DMA_CH(#i)_Rx_Control. Width of ARBS field<br>is 8, 7 or 6-bits depending on the data bus widths (32-bit, 64-bit, or 128-bit respectively)|
|16-10|Reserved.|
|Reserved_x_10||
|9-0<br>RDRL|Receive Descriptor Ring Length This register sets the maximum number of Rx descriptors in the circular<br>descriptor ring. The maximum number of descriptors is limited to 1K descriptors. For example, You can<br>program any value up to 0x3FF in this field. This field is 10 bits wide, if you program 0x3FF, you can<br>have 1024 descriptors. If you want to have 10 descriptors, program it to a value of 0x9.|



# 75.7.347 (DMA_CH0_Interrupt_Enable) 

## Offset 

|Register|Offset|
|---|---|
|DMA_CH0_Interrupt_Ena|1134h|
|ble||



## Function 

The Channeli Interrupt Enable register enables the interrupts reported by the Status register. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4030 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||Reserve|d_31_16||||||||
|Reset<br>Bits|0<br>15|0<br>14|0<br>13|0<br>12|0<br>11|0<br>10|0<br>9|0<br>8|0<br>7|0<br>6|0<br>5|0<br>4|0<br>3|0<br>2|0<br>1|0<br>0|
|R<br>W|NIE|AIE|CDEE|FBEE|ERIE|ETIE|RWTE|RSE|RBUE|RIE|Re|served_5|_3|TBUE|TXSE|TIE|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

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

4031 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

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

4032 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|0<br>TIE|Transmit Interrupt Enable When this bit is set along with the NIE bit, the Transmit Interrupt is enabled.<br>When this bit is reset, the Transmit Interrupt is disabled.<br>0b - Transmit Interrupt is disabled|
||1b - Transmit Interrupt is enabled|



# 75.7.348 (DMA_CH0_Rx_Interrupt_Watchdog_Timer) 

## Offset 

|Register|Offset|
|---|---|
|DMA_CH0_Rx_Interrupt_|1138h|
|Watchdog_Timer||



## Function 

The Receive Interrupt Watchdog Timer register indicates the watchdog timeout for Receive Interrupt (RI) from the DMA. When this register is written with a non-zero value, it enables the watchdog timer for the RI bit of the DMA_CHi_Status register. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||||||Reserve|d_31_18|||||||RWTU|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R<br>W||||Reserve|d_15_8|||||||RW|T|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



## Fields 

|Field|Function|
|---|---|
|31-18|Reserved.|
|Reserved_31_1<br>8||
|17-16<br>RWTU|Receive Interrupt Watchdog Timer Count Units This fields indicates the number of system clock cycles<br>corresponding to one unit in RWT field. - 2'b00: 256 - 2'b01: 512 - 2'b10: 1024 - 2'b11: 2048 For<br>example, when RWT=2 and RWTU=1, the watchdog timer is set for 2*512=1024 system clock cycles.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4033 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|15-8|Reserved.|
|Reserved_15_8||
|7-0<br>RWT|Receive Interrupt Watchdog Timer Count This field indicates the number of system clock cycles,<br>multiplied by factor indicated in RWTU field, for which the watchdog timer is set. The watchdog timer<br>is triggered with the programmed value after the Rx DMA completes the transfer of a packet for which<br>the RI bit is not set in the DMA_CH(#i)_Status register, because of the setting of Interrupt Enable bit in<br>the corresponding descriptor RDES3[30]. When the watchdog timer runs out, the RI bit is set and the<br>timer is stopped. The watchdog timer is reset when the RI bit is set high because of automatic setting of<br>RI as per the Interrupt Enable bit RDES3[30] of any received packet.|



# 75.7.349 (DMA_CH0_Slot_Function_Control_Status) 

## Offset 

|Register|Offset|
|---|---|
|DMA_CH0_Slot_Functio|113Ch|
|n_Control_Status||



## Function 

The Slot Function Control and Status register contains the control bits for slot function and the status for Transmit path. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||Reserved|_31_20|||||||R|SN||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||SIV|||||||Reserv|ed_3_2|ASC|ESC|
|Reset|0|0|0|0|0|1|1|1|1|1|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-20|Reserved.|
|Reserved_31_2<br>0||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4034 / 4640 

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



# 75.7.350 (DMA_CH0_Current_App_TxDesc) 

## Offset 

|Register|Offset|
|---|---|
|DMA_CH0_Current_App<br>_TxDesc|1144h|



## Function 

The Channeli Current Application Transmit Descriptor register points to the current Transmit descriptor read by the DMA. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4035 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-4036-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R CURTDESAPTR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R CURTDESAPTR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0<br>CURTDESAPT<br>R|Application Transmit Descriptor Address Pointer The DMA updates this pointer during Tx operation. This<br>pointer is cleared on reset.|



# 75.7.351 (DMA_CH0_Current_App_RxDesc) 

## Offset 

|Register|Offset|
|---|---|
|DMA_CH0_Current_App<br>_RxDesc|114Ch|



## Function 

The Channeli Current Application Receive Descriptor register points to the current Receive descriptor read by the DMA. 

## Diagram 

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

4036 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0<br>CURRDESAPT<br>R|Application Receive Descriptor Address Pointer The DMA updates this pointer during Rx operation. This<br>pointer is cleared on reset.|



# 75.7.352 (DMA_CH0_Current_App_TxBuffer) 

## Offset 

|Register|Offset|
|---|---|
|DMA_CH0_Current_App|1154h|
|_TxBuffer||



## Function 

The Channeli Current Application Transmit Buffer Address register points to the current Tx buffer address read by the DMA. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||CURTB|UFAPTR||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||CURTB|UFAPTR||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0<br>CURTBUFAPT<br>R|Application Transmit Buffer Address Pointer The DMA updates this pointer during Tx operation. This<br>pointer is cleared on reset.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4037 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

# 75.7.353 (DMA_CH0_Current_App_RxBuffer) 

## Offset 

|Register|Offset|
|---|---|
|DMA_CH0_Current_App|115Ch|
|_RxBuffer||



## Function 

The Channel 0 Current Application Receive Buffer Address register points to the current Rx buffer address read by the DMA. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/075_Gigabit_Ethernet_Media_Access_Controller_-GMAC-_part3/S32K3XXRM_数据表.pdf-4038-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R CURRBUFAPTR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R CURRBUFAPTR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0<br>CURRBUFAPT<br>R|Application Receive Buffer Address Pointer The DMA updates this pointer during Rx operation. This<br>pointer is cleared on reset.|



# 75.7.354 (DMA_CH0_Status) 

## Offset 

|Register|Offset|
|---|---|
|DMA_CH0_Status|1160h|



## Function 

The software driver (application) reads the Status register during interrupt service routine or polling to determine the status of the DMA. Note: The number of DMA_CH(#i)_Status register in the configuration is the higher of number of Rx DMA Channels and Tx DMA Channels. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4038 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||Reserve|d_31_22||||||REB|||TEB||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|NIS|AIS|CDE|FBE|ERI|ETI|RWT|RPS|RBU|RI|Re|served_5|_3|TBU|TPS|TI|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

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

4039 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

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

4040 / 4640 

NXP Semiconductors 

Gigabit Ethernet Media Access Controller (GMAC) 

## Table continued from the previous page... 

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

4041 / 4640 

