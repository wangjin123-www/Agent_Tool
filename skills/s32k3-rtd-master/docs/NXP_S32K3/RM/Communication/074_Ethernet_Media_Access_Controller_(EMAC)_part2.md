NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0|Receive Alignment Error Packets|
|RXALGNERR|Indicates the number of packets received with alignment (dribble) error. It is valid only in 10/100 mode.|



# 74.7.95 Receive Runt Error Packets (Rx_Runt_Error_Packets) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Runt_Error_Packets|79Ch|



## Function 

Provides the number of runt packets, which have a length less than 64 bytes and a CRC error, that the module received. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3137-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RXRUNTERR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXRUNTERR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Receive Runt Error Packets|
|RXRUNTERR|Indicates the number of runt packets received.|



# 74.7.96 Receive Jabber Error Packets (Rx_Jabber_Error_Packets) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Jabber_Error_Packet|7A0h|
|s||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3137 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Function 

Provides the number of giant packets that the module received, having a length (including CRC) greater than 1,518 bytes (1,522 bytes for VLAN-tagged packets), and with a CRC error. If Jumbo Packet mode is enabled, packets of length greater than 9,018 bytes (9,022 bytes for VLAN-tagged packets) are considered as giant packets. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3138-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RXJABERR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXJABERR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Receive Jabber Error Packets|
|RXJABERR|Indicates the number of giant packets received, having a length (including CRC) greater than 1,518 bytes|
||(1,522 bytes for VLAN-tagged packets), and with a CRC error. If Jumbo Packet mode is enabled, packets|
||of length greater than 9,018 bytes (9,022 bytes for VLAN-tagged packets) are considered as giant packets.|



# 74.7.97 Receive Undersize Packets Good (Rx_Undersize_Packets_Good) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Undersize_Packets_|7A4h|
|Good||



## Function 

Provides the number of packets that the module received, having a length less than 64 bytes, but without any errors. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3138 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3139-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RXUNDERSZG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXUNDERSZG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Receive Undersize Packets Good|
|RXUNDERSZG|Indicates the number of packets received, having a length less than 64 bytes, but without any errors.|



# 74.7.98 Receive Oversize Packets Good (Rx_Oversize_Packets_Good) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Oversize_Packets_G|7A8h|
|ood||



## Function 

Provides the number of packets that the module received without any errors, having a length greater than the maximum size (1,518 bytes or 1,522 bytes for VLAN-tagged packets; 2000 bytes if MAC_Configuration[S2KP] = 1). 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||RXOVE|RSZG||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||RXOVE|RSZG||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3139 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0|Receive Oversize Packets Good|
|RXOVERSZG|Indicates the number of packets received without errors, with a length greater than the maximum size (1,518|
||bytes or 1,522 bytes for VLAN-tagged packets; 2000 bytes ifMAC_Configuration[S2KP]= 1).|



# 74.7.99 Receive 64 Octets Packets Good Bad (Rx_64Octets_Packets_Good_Bad) 

## Offset 

|Register|Offset|
|---|---|
|Rx_64Octets_Packets_G|7ACh|
|ood_Bad||



## Function 

Provides the number of 64-byte good and bad packets that the module received, exclusive of the preamble. 

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
|31-0|Receive 64 Octets Packets Good Bad|
|RX64OCTGB|Provides the number of 64-byte good and bad packets that the module received, exclusive of the preamble.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3140 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

# 74.7.100 Receive 65-127 Octets Packets Good Bad (Rx_65To127Octets_Packets_Good_Bad) 

## Offset 

|Register|Offset|
|---|---|
|Rx_65To127Octets_Pac|7B0h|
|kets_Good_Bad||



## Function 

Provides the number of good and bad packets that the module received, ranging between 65 and 127 (inclusive) bytes, exclusive of the preamble. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3141-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RX65_127OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RX65_127OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Receive 65-127 Octets Packets Good Bad|
|RX65_127OCT|Indicates the number of good and bad packets received, ranging between 65 and 127 (inclusive) bytes,|
|GB|exclusive of the preamble.|



# 74.7.101 Receive 128-255 Octets Packets Good Bad (Rx_128To255Octets_Packets_Good_Bad) 

## Offset 

|Register|Offset|
|---|---|
|Rx_128To255Octets_Pa|7B4h|
|ckets_Good_Bad||



## Function 

Provides the number of good and bad packets that the module received, with packet length between 128 and 255 (inclusive) bytes, exclusive of the preamble. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3141 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3142-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RX128_255OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RX128_255OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Receive 128-255 Octets Packets Good Bad|
|RX128_255OC|Indicates the number of good and bad packets received, with packet length between 128 and 255 (inclusive)|
|TGB|bytes, exclusive of the preamble.|



# 74.7.102 Receive 256-511 Octets Packets Good Bad (Rx_256To511Octets_Packets_Good_Bad) 

## Offset 

|Register|Offset|
|---|---|
|Rx_256To511Octets_Pa|7B8h|
|ckets_Good_Bad||



## Function 

Provides the number of good and bad packets that the module received, having a packet length between 256 and 511 (inclusive) bytes, exclusive of the preamble. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3142-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RX256_511OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RX256_511OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3142 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0|Receive 256-511 Octets Packets Good Bad|
|RX256_511OC<br>TGB|Indicates the number of good and bad packets received, having a packet length between 256 and 511<br>(inclusive) bytes, exclusive of the preamble.|



# 74.7.103 Receive 512-1023 Octets Packets Good Bad (Rx_512To1023Octets_Packets_Good_Bad) 

## Offset 

|Register|Offset|
|---|---|
|Rx_512To1023Octets_P|7BCh|
|ackets_Good_Bad||



## Function 

Provides the number of good and bad packets that the module received, having a packet length between 512 and 1023 (inclusive) bytes, exclusive of the preamble. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3143-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RX512_1023OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RX512_1023OCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-0|Receive 512-1023 Octets Packets Good Bad|
|RX512_1023O|Indicates the number of good and bad packets received, having a packet length between 512 and 1023|
|CTGB|(inclusive) bytes, exclusive of the preamble.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3143 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

# 74.7.104 Receive 1024 To Max Octets Good Bad (Rx_1024ToMaxOctets_Packets_Good_Bad) 

## Offset 

|Register|Offset|
|---|---|
|Rx_1024ToMaxOctets_P|7C0h|
|ackets_Good_Bad||



## Function 

Provides the number of good and bad packets that the module received, having an inclusive packet length between 1024 bytes and the maximum byte size, exclusive of the preamble. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3144-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RX1024_MAXOCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RX1024_MAXOCTGB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Receive 1024-Max Octets Good Bad|
|RX1024_MAXO<br>CTGB|Indicates the number of good and bad packets received with length between 1024 and the maximum size<br>(inclusive) bytes, exclusive of the preamble.|



# 74.7.105 Receive Unicast Packets Good (Rx_Unicast_Packets_Good) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Unicast_Packets_Go|7C4h|
|od||



## Function 

Provides the number of good unicast packets that the module received. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3144 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3145-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RXUCASTG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXUCASTG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Receive Unicast Packets Good|
|RXUCASTG|Indicates the number of good unicast packets received.|



# 74.7.106 Receive Length Error Packets (Rx_Length_Error_Packets) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Length_Error_Packet|7C8h|
|s||



## Function 

Provides the number of packets that the module received with a length error (the Length/Type (LT) field of the RDES3 normal descriptor not equal to the packet size) for all the packets with a valid length field. For more information on the LT field, see the "RDES3 normal descriptor (write-back format)" section. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3145-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RXLENERR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXLENERR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3145 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0|Receive Length Error Packets|
|RXLENERR|Indicates the number of packets received with a length error (the Length/Type (LT) field of the RDES3<br>normal descriptor not equal to the packet size) for all the packets with a valid length field. For more<br>information on the LT field, see the "RDES3 normal descriptor (write-back format)" section.|



# 74.7.107 Receive Out of Range Type Packet (Rx_Out_Of_Range_Type_Packets) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Out_Of_Range_Type<br>_Packets|7CCh|



## Function 

Provides the number of packets that the module received, with the length field not equal to the valid packet size (greater than 1,500 but less than 1,536). 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3146-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RXOUTOFRNG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXOUTOFRNG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Receive Out of Range Type Packet|
|RXOUTOFRNG|Indicates the number of packets received with length field not equal to the valid packet size (greater than<br>1,500 but less than 1,536).|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3146 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

# 74.7.108 Receive Pause Packets (Rx_Pause_Packets) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Pause_Packets|7D0h|



## Function 

Provides the number of good and valid pause packets that the module received. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3147-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RXPAUSEPKT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXPAUSEPKT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Receive Pause Packets|
|RXPAUSEPKT|Indicates the number of good and valid pause packets received.|



# 74.7.109 Receive FIFO Overflow Packets (Rx_FIFO_Overflow_Packets) 

## Offset 

|Register|Offset|
|---|---|
|Rx_FIFO_Overflow_Pack|7D4h|
|ets||



## Function 

Provides the number of missed received packets because of FIFO overflow in the module. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3147 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3148-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RXFIFOOVFL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXFIFOOVFL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Receive FIFO Overflow Packets|
|RXFIFOOVFL|Indicates the number of missed received packets because of FIFO overflow.|



# 74.7.110 Receive VLAN Packets Good Bad (Rx_VLAN_Packets_Good_Bad) 

## Offset 

|Register|Offset|
|---|---|
|Rx_VLAN_Packets_Goo|7D8h|
|d_Bad||



## Function 

Provides the number of good and bad VLAN packets that the module received. 

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



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3148 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0|Receive VLAN Packets Good Bad|
|RXVLANPKTG<br>B|Indicates the number of good and bad VLAN packets received.|



# 74.7.111 Receive Watchdog Error Packets (Rx_Watchdog_Error_Packets) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Watchdog_Error_Pac|7DCh|
|kets||



## Function 

Provides the number of packets that the module received with a watchdog timeout error. Packets with a data load larger than the following are received: 

- 2,048 bytes when MAC_Configuration[JE] = 0 and MAC_Configuration[WD] = 0 

- 10,240 bytes when MAC_Configuration[JE] = 1 and MAC_Configuration[WD] = 0 

- 16,384 bytes when MAC_Configuration[WD] = 1 or the value programmed in MAC Watchdog Timeout (MAC_Watchdog_Timeout) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3149-13.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RXWDGERR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXWDGERR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Receive Watchdog Error Packets|
|RXWDGERR|Indicates the number of packets received with a watchdog timeout error. Packets with a data load larger than<br>the following are received:|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3149 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

- Field Function • 2,048 bytes when MAC_Configuration[JE] = 0 and MAC_Configuration[WD] = 0 • 10,240 bytes when MAC_Configuration[JE] = 1 and MAC_Configuration[WD] = 0 • 16,384 bytes when MAC_Configuration[WD] = 1 or the value programmed in MAC Watchdog Timeout (MAC_Watchdog_Timeout) 

# 74.7.112 Receive Receive Error Packets (Rx_Receive_Error_Packets) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Receive_Error_Pack|7E0h|
|ets||



## Function 

Provides the number of packets that the module received with a receive or packet extension error on GMII or MII. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||RXRC|VERR||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||RXRC|VERR||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Receive Receive Error Packets|
|RXRCVERR|Indicates the number of packets received with a receive or packet extension error on GMII or MII.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3150 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

# 74.7.113 Receive Control Packets Good (Rx_Control_Packets_Good) 

## Offset 

|Register|Offset|
|---|---|
|Rx_Control_Packets_Go|7E4h|
|od||



## Function 

Provides the number of good control packets that the module received. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3151-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RXCTRLG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXCTRLG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Receive Control Packets Good|
|RXCTRLG|Indicates the number of good control packets received.|



# 74.7.114 MMC Transmit FPE Fragment Counter Interrupt Status (MMC_FPE_Tx_Interrupt) 

## Offset 

|Register|Offset|
|---|---|
|MMC_FPE_Tx_Interrupt|8A0h|



## Function 

Maintains the interrupts generated from all the FPE-related transmit statistic counters when they reach half of their maximum values (8000_0000h for a 32-bit counter and 8000h for a 16-bit counter), and when they cross their maximum values (FFFF_FFFFh for a 32-bit counter and FFFFh for a 16-bit counter). When MMC_Control[CNTSTOPRO] = 1, the interrupts are set but the counter remains at all-ones. 

An interrupt bit of this register becomes 0 when the respective MMC counter that caused the interrupt is read. The least significant byte lane (bits [7:0]) of the respective counter must be read to clear the interrupt bit. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3151 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3152-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R HRCIS  FCIS<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-2|Reserved|
|—||
|1|MMC Transmit Hold Request Counter Interrupt Status|
|HRCIS|Indicates whether the MMC Transmit hold request counter interrupt status is detected.<br>This field:<br>• Becomes 1 when the Tx_Hold_Req_Cntr counter reaches half of the maximum value or the<br>maximum value.<br>• Exists when any one of the receive or transmit MMC counters is enabled during FPE with AV_EST-<br>enabled configuration.<br>Access restrictions apply to this field that clears on read and automatically becomes 1 on an internal<br>event occurrence.|
||0b - Not detected<br>1b - Detected|
|0|MMC Transmit FPE Fragment Counter Interrupt Status|
|FCIS|Indicates whether the MMC Transmit FPE fragment counter interrupt status is detected.<br>This field:<br>• Becomes 1 when the Tx_FPE_Fragment_Cntr counter reaches half of the maximum value or the<br>maximum value.<br>• Exists when any one of the receive or transmit MMC counters is enabled during FPE-enabled<br>configuration.<br>Access restrictions apply to this field that clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3152 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

# 74.7.115 MMC FPE Transmit Interrupt Mask (MMC_FPE_Tx_Interrupt_Mask) 

## Offset 

|Register|Offset|
|---|---|
|MMC_FPE_Tx_Interrupt_|8A4h|
|Mask||



## Function 

Maintains the masks for interrupts generated from all FPE-related transmit statistics counters. MMC Receive Interrupt Mask (MMC_Rx_Interrupt_Mask) maintains the masks for the interrupts generated when FPE-related receive statistic counters reach half of their maximum value or the maximum value. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3153-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>Reserved  HRCIM  FCIM<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-2|Reserved|
|—||
|1|MMC Transmit Hold Request Counter Interrupt Mask|
|HRCIM|Indicates the status of the MMC transmit hold request counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the Tx_Hold_Req_Cntr counter reaches half of its maximum<br>value or the maximum value.<br>The field exists when any one of the receive, transmit, or MMC counters is enabled during FPE with<br>AV_EST-enabled configuration.|
||0b - Disabled|
||1b - Enabled|
|0|MMC Transmit Fragment Counter Interrupt Mask|
|FCIM|Indicates the status of the MMC transmit fragment counter interrupt mask.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3153 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||Writing 1 to this field masks the interrupt when the Tx_FPE_Fragment_Cntr counter reaches half of its<br>maximum value or the maximum value. The field exists when any one of the receive, transmit, or MMC<br>counters is enabled during FPE-enabled configuration.|
||0b - Disabled|
||1b - Enabled|



# 74.7.116 Transmit FPE Fragment Counter (MMC_Tx_FPE_Fragment_Cntr) 

## Offset 

|Register|Offset|
|---|---|
|MMC_Tx_FPE_Fragment<br>_Cntr|8A8h|



## Function 

Provides the number of additional mPackets transmitted because of preemption. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||TXF|FC||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||TXF|FC||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Transmit FPE Fragment Counter|
|TXFFC|Indicates the number of additional mPackets transmitted because of preemption.|
||Exists when any one of the receive, transmit, or MMC counters is enabled during FPE-<br>enabled configuration.|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3154 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

# 74.7.117 Transmit Hold Request Counter (MMC_Tx_Hold_Req_Cntr) 

## Offset 

|Register|Offset|
|---|---|
|MMC_Tx_Hold_Req_Cnt|8ACh|
|r||



## Function 

Provides the count of times that a hold request is given to MAC. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3155-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXHRC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXHRC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Transmit Hold Request Counter|
|TXHRC|Indicates the count of times that a hold request is given to MAC.|
||Exists when any one of the receive, transmit, or MMC counters is enabled during FPE with AV_EST-<br>enabled configuration.|



# 74.7.118 MMC Receive Packet Assembly Error Counter Interrupt Status (MMC_FPE_Rx_Interrupt) 

## Offset 

|Register|Offset|
|---|---|
|MMC_FPE_Rx_Interrupt|8C0h|



## Function 

Maintains the interrupts generated from all the FPE-related receive statistic counters, when these transmit statistic counters reach half of their maximum values (8000_0000h for a 32-bit counter and 8000h for a 16-bit counter), and when they cross their maximum values (FFFF_FFFFh for a 32-bit counter and FFFFh for 16-bit counter). When MMC_Control[CNTSTOPRO] = 1, the interrupts are set but the counter remains at all-ones. An interrupt bit of this register becomes 0 when the respective 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3155 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

MMC counter that caused the interrupt is read. The least significant byte lane (bits [7:0]) of the respective counter must be read to clear the interrupt bit. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3156-04.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>PAOCI PSECI PAECI<br>R FCIS<br>S  S  S<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-4|Reserved|
|—||
|3|MMC Receive FPE Fragment Counter Interrupt Status|
|FCIS|Indicates whether the MMC receive FPE fragment counter interrupt status is detected.<br>This field becomes 1 when the Rx_FPE_Fragment_Cntr counter reaches half of its maximum value or the<br>maximum value.<br>Exists when any one of the receive, transmit, or MMC counters is enabled during FPE-<br>enabled configuration.<br>Access restrictions apply to this field that clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected|
||1b - Detected|
|2|MMC Receive Packet Assembly OK Counter Interrupt Status|
|PAOCIS|Indicates whether the MMC receive packet assembly OK counter interrupt status is detected.<br>This field becomes 1 when the Rx_Packet_Assemble_Ok_Cntr counter reaches half of its maximum value<br>or the maximum value.<br>Exists when any one of the receive, transmit, or MMC counters is enabled during FPE-<br>enabled configuration.<br>Access restrictions apply to this field that clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3156 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|1|MMC Receive, Transmit, Packet SMD Error Counter Interrupt Status|
|PSECIS|Indicates whether the status of the MMC receive packet SMD error counter interrupt is detected.<br>This field becomes 1 when the Rx_Packet_SMD_Err_Cntr counter reaches half of its maximum value or the<br>maximum value.<br>Exists when any one of the receive, transmit, or MMC counters is enabled during FPE-<br>enabled configuration.<br>Access restrictions apply to this field that clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|0<br>PAECIS|MMC Receive, transmit, Packet Assembly Error Counter Interrupt Status<br>Indicates whether the status of the MMC receive packet assembly error counter interrupt is detected.<br>This field becomes 1 when the Rx_Packet_Assemble_Err_Cntr counter reaches half of its maximum value<br>or the maximum value.<br>Exists when any one of the receive, transmit, or MMC counters is enabled during the FPE-<br>enabled configuration.<br>Access restrictions apply to this field that clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|



# 74.7.119 MMC FPE Receive Interrupt Mask (MMC_FPE_Rx_Interrupt_Mask) 

## Offset 

|Register|Offset|
|---|---|
|MMC_FPE_Rx_Interrupt|8C4h|
|_Mask||



## Function 

Maintains the masks for interrupts generated from all FPE-related receive statistic counters. 

This register maintains the masks for the interrupts generated when FPE-related receive statistic counters reach half of their maximum value or the maximum value. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3157 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||Rese|rved||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||Rese|rved||||||FCIM|PAOCI<br>M|PSECI<br>M|PAECI<br>M|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-4|Reserved|
|—||
|3|MMC Receive FPE Fragment Counter Interrupt Mask|
|FCIM|Indicates the status of the MMC receive FPE fragment counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the Tx_FPE_Fragment_Cntr counter reaches half of its<br>maximum value or the maximum value.<br>Exists when any one of the receive, transmit, or MMC counters is enabled during FPE-<br>enabled configuration.<br>0b - Disabled<br>1b - Enabled|
|2|MMC Receive Packet Assembly OK Counter Interrupt Mask|
|PAOCIM|Indicates the status of the MMC receive packet assembly OK counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the Rx_Packet_Assemble_Ok_Cntr counter reaches half of<br>its maximum value or the maximum value.<br>Exists when any one of the receive, transmit, or MMC counters is enabled during FPE-<br>enabled configuration.<br>0b - Disabled<br>1b - Enabled|
|1<br>PSECIM|MMC Receive Packet SMD Error Counter Interrupt Mask<br>Indicates the status of the MMC receive packet SMD error counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the Rx_Packet_SMD_Err_Cntr counter reaches half of its<br>maximum value or the maximum value.<br>Exists when any one of the receive, transmit, or MMC counters is enabled during FPE-<br>enabled configuration.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3158 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Disabled<br>1b - Enabled|
|0|MMC receive Packet Assembly Error Counter Interrupt Mask|
|PAECIM|Indicates the status of the MMC receive packet assembly error counter interrupt mask.<br>Writing 1 to this field masks the interrupt when the Rx_Packet_Assemble_Err_Cntr counter reaches half of<br>its maximum value or the maximum value.<br>Exists when any one of the receive, transmit, or MMC counters is enabled during FPE-<br>enabled configuration.|
||0b - Disabled<br>1b - Enabled|



# 74.7.120 MMC Receive Packet Assembly Error Counter (MMC_Rx_Packet_Assembly_Err_Cntr) 

## Offset 

|Register|Offset|
|---|---|
|MMC_Rx_Packet_Assem|8C8h|
|bly_Err_Cntr||



## Function 

Provides the number of MAC frames having reassembly errors on the receiver arising out of mismatch in the fragment count value. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||PA|EC||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||PA|EC||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3159 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0|Packet Assembly Error Counter|
|PAEC|Indicates the number of MAC frames having reassembly errors on the receiver arising out of mismatch in<br>the fragment count value.|
||Exists when any one of the receive, transmit, or MMC counters is enabled during FPE-<br>enabled configuration.|



# 74.7.121 MMC Receive Packet SMD Error Counter (MMC_Rx_Packet_SMD_Err_Cntr) 

## Offset 

|Register|Offset|
|---|---|
|MMC_Rx_Packet_SMD_|8CCh|
|Err_Cntr||



## Function 

Provides the number of received MAC frames rejected because of an unknown SMD value and MAC frame fragments rejected because of arriving with SMD-C when there was no preceding preempted frame. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||PS|EC||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||PS|EC||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function|
|---|---|
|31-0|Packet SMD Error Counter|
|PSEC|Indicates the number of MAC frames rejected because of an unknown SMD value and MAC frame<br>fragments rejected because of arriving with SMD-C when there was no preceding preempted frame.|
||Exists when at least one of the receive, transmit, or MMC counters is enabled during FPE-<br>enabled configuration.|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3160 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

# 74.7.122 MMC Receive Packet Assembly OK Counter (MMC_Rx_Packet_Assembly_OK_Cntr) 

## Offset 

|Register|Offset|
|---|---|
|MMC_Rx_Packet_Assem|8D0h|
|bly_OK_Cntr||



## Function 

Provides the number of MAC frames that were successfully reassembled and delivered to MAC. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3161-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R PAOC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R PAOC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Packet Assembly OK Counter|
|PAOC|Indicates the number of MAC frames that were successfully reassembled and delivered to MAC.|
||Exists when at least one of the receive, transmit, or MMC counters is enabled during FPE-<br>enabled configuration.|



# 74.7.123 MMC Receive FPE Fragment Counter (MMC_Rx_FPE_Fragment_Cntr) 

## Offset 

|Register|Offset|
|---|---|
|MMC_Rx_FPE_Fragmen|8D4h|
|t_Cntr||



## Function 

Provides the number of additional mPackets received because of preemption. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3161 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3162-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R FFC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R FFC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|FPE Fragment Counter|
|FFC|Indicates the number of additional mPackets received because of preemption.|
||Exists when at least one of the receive, transmit, or MMC counters is enabled during FPE-<br>enabled configuration.|



# 74.7.124 MAC Layer 3 Layer 4 Control 0 (MAC_L3_L4_Control0) 

## Offset 

|Register|Offset|
|---|---|
|MAC_L3_L4_Control0|900h|



## Function 

Controls the filter 0 operations of the layer 3 and layer 4 protocols. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Reserved||DMCH<br>EN0||Reserved||DMCH<br>N0|Rese|rved|L4DPI<br>M0|L4DP<br>M0|L4SPI<br>M0|L4SP<br>M0|Reserv<br>ed|L4PEN<br>0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||L|3HDBM0|||||L3HSBM0|||L3DAI<br>M0|L3DA<br>M0|L3SAI<br>M0|L3SA<br>M0|Reserv<br>ed|L3PEN<br>0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3162 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Fields 

|Field<br>31-29<br>—|Function<br>Reserved|
|---|---|
|28<br>DMCHEN0|DMA Channel Select Enable<br>Indicates the status of the DMA channel number.<br>• If this field is 1, it enables the selection of the DMA channel number for the packet that the L3_L4<br>filter passes. The DMCHN fields indicate the DMA channel number.<br>• If this field is 0, the filter does not decide the DMA channel number.<br>0b - Disabled<br>1b - Enabled|
|27-25<br>—|Reserved|
|24<br>DMCHN0|DMA Channel Number<br>Indicates the DMA channel number.<br>If the value of the DMCHEN fields is 1, this field selects the DMA channel number to which the packet that<br>this filter passes is routed. The width of this field depends on the number of the DMA channels present in<br>your configuration.|
|23-22<br>—<br>21|Reserved<br>Layer 4 Destination Port Inverse Match Enable|
|L4DPIM0|Indicates the status of layer 4 destination port inverse matching.<br>• If this field is 1,MAC_Layer4_Address0[L4DP0]is enabled for inverse matching.<br>• If this field is 0,MAC_Layer4_Address0[L4DP0]is enabled for perfect matching.<br>This field is valid and applicable only when the L4DPM0 field is 1.<br>0b - Disabled<br>1b - Enabled|
|20<br>L4DPM0|Layer 4 Destination Port Match Enable<br>Indicates the status of layer 4 destination port matching.<br>• If this field is 1,MAC_Layer4_Address0[L4DP0]is enabled for matching.<br>• If this field is 0, MAC ignoresMAC_Layer4_Address0[L4DP0]for matching.<br>0b - Disabled<br>1b - Enabled|
|19|Layer 4 Source Port Inverse Match Enable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3163 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|L4SPIM0|Indicates the status of layer 4 source port inverse matching.<br>• If this field is 1,MAC_Layer4_Address0[L4SP0]is enabled for inverse matching.<br>• If this field is 0,MAC_Layer4_Address0[L4SP0]is enabled for perfect matching.<br>This field is valid and applicable only whenMAC_Layer4_Address0[L4SP0]= 1.<br>0b - Disabled<br>1b - Enabled|
|18<br>L4SPM0|Layer 4 Source Port Match Enable<br>Indicates the status of layer 4 source port matching.<br>• If this field is 1,MAC_Layer4_Address0[L4SP0]is enabled for matching.<br>• If this field is 0, MAC ignoresMAC_Layer4_Address0[L4SP0]for matching.<br>0b - Disabled<br>1b - Enabled|
|17<br>—|Reserved|
|16|Layer 4 Protocol Enable|
|L4PEN0|Indicates the status of layer 4 protocol.<br>• If this field is 1,MAC_Layer4_Address0[L4SP0]andMAC_Layer4_Address0[L4DP0]are used for<br>matching UDP packets.<br>• If this field is 0,MAC_Layer4_Address0[L4SP0]andMAC_Layer4_Address0[L4DP0]are used for<br>matching TCP packets.<br>Layer 4 matching is performed only when the L4SPM0 field or the L4DPM0 field is 1.<br>0b - Disabled<br>1b - Enabled|
|15-11<br>L3HDBM0|Layer 3 IP DA Higher Bits Match<br>IPv4 packets:<br>This field contains the number of higher bits of IP DA that are matched in the IPv4 packets. The following<br>list describes the values of this field:<br>• 0: No bits are masked.<br>• 1: LSb[0] is masked.<br>• 2: Two LSbs [1:0] are masked.<br>• - ..<br>• 31: All bits except MSb are masked.<br>IPv6 packets:|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3164 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function<br>Bits [12:11] of this field correspond to bits [6:5] of the L3HSBM0 field, which indicates the number of lower<br>bits of IP SA or DA that are masked in the IPv6 packets. The following list describes the concatenated values<br>of the L3HDBM0[1:0] and L3HSBM0 fields:<br>• 0: No bits are masked.<br>• 1: LSb[0] is masked.<br>• 2: Two LSbs [1:0] are masked.<br>• ..<br>• 127: All bits except MSb are masked.<br>This field is valid and applicable only when the L3DAM0 field or the L3SAM0 field is 1.|
|---|---|
|10-6<br>L3HSBM0|Layer 3 IP SA Higher Bits Match<br>IPv4 packets:<br>This field contains the number of lower bits of IP SA that are masked for matching in the IPv4 packets. The<br>following list describes the values of this field:<br>• 0: No bits are masked.<br>• 1: LSb[0] is masked.<br>• 2: Two LSbs [1:0] are masked.<br>• ..<br>• 31: All bits except MSb are masked.<br>IPv6 packets:<br>This field contains bits [4:0] of L3HSBM0. These bits indicate the number of higher bits of IP SA or DA<br>matched in the IPv6 packets. The field is valid and applicable only when the L3DAM0 field or the L3SAM0<br>field is 1.|
|5<br>L3DAIM0|Layer 3 IP DA Inverse Match Enable<br>Indicates the status of layer 3 IP DA inverse matching.<br>• If this field is 1, layer 3 IP DA is enabled for inverse matching.<br>• If this field is 0, layer 3 IP DA is enabled for perfect matching.<br>This field is valid and applicable only if L3DAM0 = 1.<br>0b - Disabled<br>1b - Enabled|
|4<br>L3DAM0|Layer 3 IP DA Match Enable<br>Indicates the status of layer 3 IP DA matching.<br>• If this field is 1, layer 3 IP DA is enabled for matching.<br>• If this field is 0, MAC ignores layer 3 IP DA for matching.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3165 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function<br>If L3PEN0 = 1, you must write 1 to either this field or the L3SAM0 field because either the<br>IPv6 DA or SA can be checked for filtering.<br>~~NOTE~~|
|---|---|
||0b - Disabled<br>1b - Enabled|
|3<br>L3SAIM0|Layer 3 IP SA Inverse Match Enable<br>Indicates the status of layer 3 IP SA inverse matching.<br>• If this field is 1, layer 3 IP SA is enabled for inverse matching.<br>• If this field is 0, layer 3 IP SA is enabled for perfect matching.<br>This field is valid and applicable only if the L3SAM0 field is 1.<br>0b - Disabled<br>1b - Enabled|
|2<br>L3SAM0|Layer 3 IP SA Match Enable<br>Indicates the status of layer 3 IP SA matching.<br>• If this field is 1, layer 3 IP SA matching is enabled.<br>• If this field is 0, MAC ignores layer 3 IP SA matching.<br>If L3PEN0 = 1, you must write 1 to either this field or the L3DAM0 field because either IPv6<br>SA or DA can be checked for filtering.<br>~~NOTE~~|
||0b - Disabled<br>1b - Enabled|
|1<br>—|Reserved|
|0<br>L3PEN0|Layer 3 Protocol Enable<br>Indicates the status of layer 3 protocol.<br>• If this field is 1, the layer 3 IP SA or DA matching is enabled for IPv6 packets.<br>• If this field is 0, the layer 3 IP SA or DA matching is enabled for IPv4 packets.<br>The layer 3 matching is performed only when either the L3SAM0 field or the L3DAM0 field is 1.<br>0b - Disabled<br>1b - Enabled|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3166 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

# 74.7.125 MAC Layer 4 Address 0 (MAC_Layer4_Address0) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer4_Address0|904h|



## Function 

## Provides the layer 4 source and destination port numbers. 

MAC Layer 4 Address 1 (MAC_Layer4_Address1), MAC L3 L4 Control 1 (MAC_L3_L4_Control1), MAC Layer 3 Address 0 Reg 1 (MAC_Layer3_Addr0_Reg1), MAC Layer 3 Address 1 Reg 1 (MAC_Layer3_Addr1_Reg1), MAC Layer 3 Address 2 Reg 1 (MAC_Layer3_Addr2_Reg1), and MAC Layer 3 Address 3 Reg 1 (MAC_Layer3_Addr3_Reg1) are reserved registers (RO with a default value) if MAC_Packet_Filter[IPFE] is 0 when configuring the core. 

You can configure the layer 3 and layer 4 address registers to be double-synchronized by selecting the synchronize layer 3 and layer 4 address registers to the receive clock domain option while configuring the core. When you select this option, the synchronization is triggered only when bits [31:24] (in Little-Endian mode) or bits [7:0] (in Big-Endian mode) of the layer 3 and layer 4 address registers are written to. For proper synchronization updates, you must perform consecutive writes to the same layer 3 and layer 4 address registers after a delay of at least four destination clock cycles. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L4|DP0||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L4|SP0||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-16|Layer 4 Destination Port Number|
|L4DP0|Indicates layer 4 destination port number.<br>IfMAC_L3_L4_Control0[L4PEN0]= 0 andMAC_L3_L4_Control0[L4DPM0]= 1, this field contains the value<br>to be matched with the TCP destination port number field in the IPv4 or IPv6 packets.<br>IfMAC_L3_L4_Control0[L4PEN0]andMAC_L3_L4_Control0[L4DPM0]are 1, this field contains the value<br>to be matched with the UDP destination port number field in the IPv4 or IPv6 packets.|
|15-0|Layer 4 Source Port Number|
|L4SP0|Indicates layer 4 source port number.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3167 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||IfMAC_L3_L4_Control0[L4PEN0]= 0 andMAC_L3_L4_Control0[L4SPM0]= 1, this field contains the value<br>to be matched with the TCP source port number field in the IPv4 or IPv6 packets.|
||IfMAC_L3_L4_Control0[L4PEN0]andMAC_L3_L4_Control0[L4SPM0]are 1, this field contains the value|
||to be matched with the UDP source port number field in the IPv4 or IPv6 packets.|



# 74.7.126 MAC Layer 3 Address 0 Reg 0 (MAC_Layer3_Addr0_Reg0) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr0_Re<br>g0|910h|



## Function 

Contains the 32-bit IP source address field for IPv4 packets. For IPv6 packets, the field contains bits [31:0] of the 128-bit IP source address or destination address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3|A00||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3|A00||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 0|
|L3A00|Indicates layer 3 address 0.|
||• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3SAM0]are 1, this field contains the<br>value to be matched with bits [31:0] of the IP source address field in the IPv6 packets.<br>• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3DAM0]are 1, this field contains the<br>value to be matched with bits [31:0] of the IP destination address field in the IPv6 packets.|
||• IfMAC_L3_L4_Control0[L3PEN0]= 0, andMAC_L3_L4_Control0[L3SAM0]= 1, this field contains<br>the value to be matched with the IP source address field in the IPv4 packets.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3168 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

# 74.7.127 MAC Layer 3 Address 1 Reg 0 (MAC_Layer3_Addr1_Reg0) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr1_Re<br>g0|914h|



## Function 

Contains the 32-bit IP destination address field for IPv4 packets. For IPv6 packets, the field contains bits [63:32] of the 128-bit IP source address or destination address field. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3169-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>L3A10<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>L3A10<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 1|
|L3A10|Indicates layer 3 address 1.|
||• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3SAM0]are 1, this field contains the<br>value to be matched with bits [63:32] of the IP source address field in the IPv6 packets.<br>• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3DAM0]are 1, this field contains the<br>value to be matched with bits [63:32] of the IP destination address field in the IPv6 packets.|
||• IfMAC_L3_L4_Control0[L3PEN0]= 0, andMAC_L3_L4_Control0[L3SAM0]= 1, this field contains<br>the value to be matched with the IP source address field in the IPv4 packets.|



# 74.7.128 MAC Layer 3 Address 2 Reg 0 (MAC_Layer3_Addr2_Reg0) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr2_Re<br>g0|918h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3169 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Function 

Contains the 32-bit IP destination address field for IPv4 packets. For IPv6 packets, the field contains bits [95:64] of the 128-bit IP source address or destination address field. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3170-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>L3A20<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>L3A20<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 2|
|L3A20|Indicates layer 3 address 2.|
||• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3SAM0]are 1, this field contains the<br>value to be matched with bits [95:64] of the IP source address field in the IPv6 packets.|
||• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3DAM0]are 1, this field contains the<br>value to be matched with bits [95:64] of the IP destination address field in the IPv6 packets.|
||• IfMAC_L3_L4_Control0[L3PEN0]= 0, this field is not used.|



# 74.7.129 MAC Layer 3 Address 3 Reg 0 (MAC_Layer3_Addr3_Reg0) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr3_Re<br>g0|91Ch|



## Function 

Contains the 32-bit IP destination address field for IPv4 packets. For IPv6 packets, the field contains bits [127:96] of the 128-bit IP source address or destination address field. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3170 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3171-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>L3A30<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>L3A30<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 3|
|L3A30|Indicates layer 3 address 3.|
||• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3SAM0]are 1, this field contains the<br>value to be matched with bits [127:96] of the IP source address field in the IPv6 packets.|
||• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3DAM0]are 1, this field contains the<br>value to be matched with bits [127:96] of the IP destination address field in the IPv6 packets.|
||• IfMAC_L3_L4_Control0[L3PEN0]= 0, this field is not used.|



# 74.7.130 MAC L3 L4 Control 1 (MAC_L3_L4_Control1) 

## Offset 

|Register|Offset|
|---|---|
|MAC_L3_L4_Control1|930h|



## Function 

Controls the filter 0 operations of the layer 3 and layer 4 protocols. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3171 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Reserved||DMCH<br>EN1||Reserved||DMCH<br>N1|Rese|rved|L4DPI<br>M1|L4DP<br>M1|L4SPI<br>M1|L4SP<br>M1|Reserv<br>ed|L4PEN<br>1|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||L|3HDBM1|||||L3HSBM1|||L3DAI<br>M1|L3DA<br>M1|L3SAI<br>M1|L3SA<br>M1|Reserv<br>ed|L3PEN<br>1|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-29<br>—|Reserved|
|28|DMA Channel Select Enable 1|
|DMCHEN1|Indicates the status of the DMA channel number.<br>• If this field is 1, it enables the selection of the DMA channel number for the packet that the L3_L4<br>filter passes. The DMCHN fields indicate the DMA channel number.<br>• If this field is 0, the filter does not decide the DMA channel number.<br>0b - Disabled<br>1b - Enabled|
|27-25|Reserved|
|—<br>24|DMA Channel Number 1|
|DMCHN1|Indicates the DMA channel number.<br>If the value of the DMCHEN fields is 1, this field selects the DMA channel number to which the packet that<br>this filter passes is routed. The width of this field depends on the number of the DMA channels present in<br>your configuration.|
|23-22<br>—<br>21<br>L4DPIM1|Reserved<br>Layer 4 Destination Port Inverse Match Enable 1<br>Indicates the status of layer 4 destination port inverse matching.<br>• If this field is 1,MAC_Layer4_Address0[L4DP0]is enabled for inverse matching.<br>• If this field is 0,MAC_Layer4_Address0[L4DP0]is enabled for perfect matching.<br>This field is valid and applicable only when the L4DPM0 field is 1.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3172 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function<br>0b - Disabled<br>1b - Enabled|
|---|---|
|20<br>L4DPM1|Layer 4 Destination Port Match Enable 1<br>Indicates the status of layer 4 destination port matching.<br>• If this field is 1,MAC_Layer4_Address0[L4DP0]is enabled for matching.<br>• If this field is 0, MAC ignoresMAC_Layer4_Address0[L4DP0]for matching.<br>0b - Disabled<br>1b - Enabled|
|19<br>L4SPIM1|Layer 4 Source Port Inverse Match Enable 1<br>Indicates the status of layer 4 source port inverse matching.<br>• If this field is 1,MAC_Layer4_Address0[L4SP0]is enabled for inverse matching.<br>• If this field is 0,MAC_Layer4_Address0[L4SP0]is enabled for perfect matching.<br>This field is valid and applicable only whenMAC_Layer4_Address0[L4SP0]= 1.<br>0b - Disabled<br>1b - Enabled|
|18|Layer 4 Source Port Match Enable 1|
|L4SPM1|Indicates the status of layer 4 source port matching.<br>• If this field is 1,MAC_Layer4_Address0[L4SP0]is enabled for matching.<br>• If this field is 0, MAC ignoresMAC_Layer4_Address0[L4SP0]for matching.<br>0b - Disabled<br>1b - Enabled|
|17|Reserved|
|—||
|16<br>L4PEN1|Layer 4 Protocol Enable 1<br>Indicates the status of layer 4 protocol.<br>• If this field is 1,MAC_Layer4_Address0[L4SP0]andMAC_Layer4_Address0[L4DP0]of UDP packets<br>are used for matching.<br>• If this field is 0,MAC_Layer4_Address0[L4SP0]andMAC_Layer4_Address0[L4DP0]of TCP packets<br>are used for matching.<br>Layer 4 matching is performed only when the L4SPM0 field or the L4DPM0 field is 1.<br>0b - Disabled<br>1b - Enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3173 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|15-11|Layer 3 IP DA Higher Bits Match 1|
|L3HDBM1|IPv4 Packets:<br>This field contains the number of higher bits of IP DA that are matched in the IPv4 packets. The following<br>list describes the values of this field:<br>• 0: No bits are masked.<br>• 1: LSb[0] is masked.<br>• 2: Two LSbs [1:0] are masked.<br>• ..<br>• 31: All bits except MSb are masked.<br>IPv6 Packets:<br>Bits [12:11] of this field correspond to bits [6:5] ofMAC_L3_L4_Control0[L3HSBM0], which indicates the<br>number of lower bits of IP SA or DA that are masked in the IPv6 packets. The following list describes the<br>concatenated values ofMAC_L3_L4_Control0[L3HDBM0][1:0] andMAC_L3_L4_Control0[L3HSBM0]:<br>• 0: No bits are masked.<br>• 1: LSb[0] is masked.<br>• 2: Two LSbs [1:0] are masked<br>• ..<br>• 127: All bits except MSb are masked.<br>This field is valid and applicable only whenMAC_L3_L4_Control0[L3DAM0]or<br>MAC_L3_L4_Control0[L3SAM0]is 1.|
|10-6<br>L3HSBM1|Layer 3 IP SA Higher Bits Match 1<br>IPv4 packets:<br>This field contains the number of lower bits of IP SA that are masked for matching in the IPv4 packets. The<br>following list describes the values of this field:<br>• 0: No bits are masked.<br>• 1: LSb[0] is masked.<br>• 2: Two LSbs [1:0] are masked.<br>• ..<br>• 31: All bits except MSb are masked.<br>IPv6 packets:<br>This field contains bits [4:0] ofMAC_L3_L4_Control0[L3HSBM0]. These bits indicate the number of<br>higher bits of IP SA or DA matched in the IPv6 packets. The field is valid and applicable only when<br>MAC_L3_L4_Control0[L3DAM0]orMAC_L3_L4_Control0[L3SAM0]is 1.|
|5|Layer 3 IP DA Inverse Match Enable 1|
|L3DAIM1|Indicates the status of layer 3 IP DA inverse matching.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3174 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function<br>• If this field is 1, layer 3 IP DA is enabled for inverse matching.<br>• If this field is 0, layer 3 IP DA is enabled for perfect matching.<br>This field is valid and applicable only ifMAC_L3_L4_Control0[L3DAM0]= 1.<br>0b - Disabled<br>1b - Enabled|
|---|---|
|4<br>L3DAM1|Layer 3 IP DA Match Enable 1<br>Indicates the status of layer 3 IP DA matching.<br>• If this field is 1, layer 3 IP DA is enabled for matching.<br>• If this field is 0, MAC ignores layer 3 IP DA for matching.<br>IfMAC_L3_L4_Control0[L3PEN0]= 1, you must write 1 to either this field or to<br>MAC_L3_L4_Control0[L3SAM0]because either the IPv6 DA or SA can be checked<br>for filtering.<br>~~NOTE~~|
||0b - Disabled<br>1b - Enabled|
|3<br>L3SAIM1|Layer 3 IP SA Inverse Match Enable 1<br>Indicates the status of layer 3 IP SA inverse matching.<br>• If this field is 1, layer 3 IP SA is enabled for inverse matching.<br>• If this field is 0, layer 3 IP SA is enabled for perfect matching.<br>This field is valid and applicable only ifMAC_L3_L4_Control0[L3SAM0]is 1.<br>0b - Disabled<br>1b - Enabled|
|2<br>L3SAM1|Layer 3 IP SA Match Enable 1<br>Indicates the status of layer 3 IP SA matching.<br>• If this field is 1, layer 3 IP SA matching is enabled.<br>• If this field is 0, MAC ignores layer 3 IP SA matching.<br>IfMAC_L3_L4_Control0[L3PEN0]= 1, you must write 1 to either this field or to<br>MAC_L3_L4_Control0[L3DAM0]because either IPv6 SA or DA can be checked for filtering.<br>~~NOTE~~<br>0b - Disabled<br>1b - Enabled|
|1<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3175 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|0|Layer 3 Protocol Enable 1|
|L3PEN1|Indicates the status of layer 3 protocol.|
||• If this field is 1, the layer 3 IP SA or DA matching is enabled for IPv6 packets.|
||• If this field is 0, the layer 3 IP SA or DA matching is enabled for IPv4 packets.<br>The layer 3 matching is performed only when eitherMAC_L3_L4_Control0[L3SAM0]or<br>MAC_L3_L4_Control0[L3DAM0]is 1.<br>0b - Disabled|
||1b - Enabled|



# 74.7.131 MAC Layer 4 Address 1 (MAC_Layer4_Address1) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer4_Address1|934h|



## Function 

## Provides the layer 4 source and destination port numbers. 

MAC Layer 4 Address 1 (MAC_Layer4_Address1), MAC L3 L4 Control 1 (MAC_L3_L4_Control1), MAC Layer 3 Address 0 Reg 1 (MAC_Layer3_Addr0_Reg1), MAC Layer 3 Address 1 Reg 1 (MAC_Layer3_Addr1_Reg1), MAC Layer 3 Address 2 Reg 1 (MAC_Layer3_Addr2_Reg1), and MAC Layer 3 Address 3 Reg 1 (MAC_Layer3_Addr3_Reg1) are reserved registers (RO with a default value) if the enable layer 3 and layer 4 packet filter option is not selected when configuring the core. 

You can configure the layer 3 and layer 4 address registers to be double-synchronized by selecting the synchronize layer 3 and layer 4 address registers to the receive clock domain option while configuring the core. When you select this option, the synchronization is triggered only when bits [31:24] (in Little-Endian mode) or bits [7:0] (in Big-Endian mode) of the layer 3 and layer 4 address registers are written to. For proper synchronization updates, you must perform consecutive writes to the same layer 3 and layer 4 address registers after a delay of at least four destination clock cycles. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L4|DP1||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L4|SP1||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3176 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Fields 

|Field|Function|
|---|---|
|31-16|Layer 4 Destination Port Number 1|
|L4DP1|Indicates layer 4 destination port number.<br>IfMAC_L3_L4_Control0[L4PEN0]= 0 andMAC_L3_L4_Control0[L4DPM0]= 1, this field contains the value<br>to be matched with the TCP destination port number field in the IPv4 or IPv6 packets.<br>IfMAC_L3_L4_Control0[L4PEN0]andMAC_L3_L4_Control0[L4DPM0]are 1, this field contains the value<br>to be matched with the UDP destination port number field in the IPv4 or IPv6 packets.|
|15-0|Layer 4 Source Port Number 1|
|L4SP1|Indicates layer 4 source port number.|
||IfMAC_L3_L4_Control0[L4PEN0]= 0 andMAC_L3_L4_Control0[L4SPM0]= 1, this field contains the value<br>to be matched with the TCP source port number field in the IPv4 or IPv6 packets.<br>IfMAC_L3_L4_Control0[L4PEN0]andMAC_L3_L4_Control0[L4SPM0]are 1, this field contains the value<br>to be matched with the UDP source port number field in the IPv4 or IPv6 packets.|



# 74.7.132 MAC Layer 3 Address 0 Reg 1 (MAC_Layer3_Addr0_Reg1) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr0_Re<br>g1|940h|



## Function 

Contains the 32-bit IP source address field for IPv4 packets. For IPv6 packets, the field contains bits [31:0] of the 128-bit IP source address or destination address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3A|01||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3A|01||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3177 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 0|
|L3A01|Indicates layer 3 address 0.|
||• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3SAM0]are 1, this field contains the<br>value to be matched with bits [31:0] of the IP source address field in the IPv6 packets.<br>• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3DAM0]are 1, this field contains the<br>value to be matched with bits [31:0] of the IP destination address field in the IPv6 packets.<br>• IfMAC_L3_L4_Control0[L3PEN0]= 0, andMAC_L3_L4_Control0[L3SAM0]= 1, this field contains<br>the value to be matched with the IP source address field in the IPv4 packets.|



# 74.7.133 MAC Layer 3 Address 1 Reg 1 (MAC_Layer3_Addr1_Reg1) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr1_Re<br>g1|944h|



## Function 

Contains the 32-bit IP destination address field for IPv4 packets. For IPv6 packets, the field contains bits[63:32] of the 128-bit IP source address or destination address field. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3178-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>L3A11<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>L3A11<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 1|
|L3A11|Indicates layer 3 address 1.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3178 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

|Field|Function|
|---|---|
||• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3SAM0]are 1, this field contains the<br>value to be matched with bits [63:32] of the IP source address field in the IPv6 packets.|
||• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3DAM0]are 1, this field contains the<br>value to be matched with bits [63:32] of the IP destination address field in the IPv6 packets.|
||• IfMAC_L3_L4_Control0[L3PEN0]= 0, andMAC_L3_L4_Control0[L3SAM0]= 1, this field contains<br>the value to be matched with the IP source address field in the IPv4 packets.|



# 74.7.134 MAC Layer 3 Address 2 Reg 1 (MAC_Layer3_Addr2_Reg1) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr2_Re<br>g1|948h|



## Function 

Contains the 32-bit IP destination address field for IPv4 packets. For IPv6 packets, the field contains bits [95:64] of the 128-bit IP source address or destination address field. 

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
|31-0|Layer 3 Address 2|
|L3A21|Indicates layer 3 address 2.|
||• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3SAM0]are 1, this field contains the<br>value to be matched with bits [95:64] of the IP source address field in the IPv6 packets.|
||• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3DAM0]are 1, this field contains the<br>value to be matched with bits [95:64] of the IP destination address field in the IPv6 packets.|
||• IfMAC_L3_L4_Control0[L3PEN0]= 0, this field is not used.|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3179 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

# 74.7.135 MAC Layer 3 Address 3 Reg 1 (MAC_Layer3_Addr3_Reg1) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr3_Re<br>g1|94Ch|



## Function 

Contains the 32-bit IP destination address field for IPv4 packets. For IPv6 packets, the field contains bits [127:96] of the 128-bit IP source address or destination address field. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3180-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>L3A31<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>L3A31<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 3|
|L3A31|Indicates layer 3 address 3.|
||• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3SAM0]are 1, this field contains the<br>value to be matched with bits [127:96] of the IP source address field in the IPv6 packets.<br>• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3DAM0]are 1, this field contains the<br>value to be matched with bits [127:96] of the IP destination address field in the IPv6 packets.<br>• IfMAC_L3_L4_Control0[L3PEN0]= 0, this field is not used.|



# 74.7.136 MAC L3 L4 Control 2 (MAC_L3_L4_Control2) 

## Offset 

|Register|Offset|
|---|---|
|MAC_L3_L4_Control2|960h|



## Function 

Controls the filter 0 operations of the layer 3 and layer 4 protocols. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3180 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Reserved||DMCH<br>EN2||Reserved||DMCH<br>N2|Rese|rved|L4DPI<br>M2|L4DP<br>M2|L4SPI<br>M2|L4SP<br>M2|Reserv<br>ed|L4PEN<br>2|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||L|3HDBM2|||||L3HSBM2|||L3DAI<br>M2|L3DA<br>M2|L3SAI<br>M2|L3SA<br>M2|Reserv<br>ed|L3PEN<br>2|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-29<br>—|Reserved|
|28|DMA Channel Select Enable 2|
|DMCHEN2|Indicates the status of the DMA channel number.<br>• If this field is 1, it enables the selection of the DMA channel number for the packet that the L3_L4<br>filter passes. The DMCHN fields indicate the DMA channel number.<br>• If this field is 0, the filter does not decide the DMA channel number.<br>0b - Disabled<br>1b - Enabled|
|27-25|Reserved|
|—<br>24|DMA Channel Number 2|
|DMCHN2|Indicates the DMA channel number.<br>If the value of the DMCHEN fields is 1, this field selects the DMA channel number to which the packet that<br>this filter passes is routed. The width of this field depends on the number of the DMA channels present in<br>your configuration.|
|23-22<br>—<br>21<br>L4DPIM2|Reserved<br>Layer 4 Destination Port Inverse Match Enable 2<br>Indicates the status of layer 4 destination port inverse matching.<br>• If this field is 1,MAC_Layer4_Address0[L4DP0]is enabled for inverse matching.<br>• If this field is 0,MAC_Layer4_Address0[L4DP0]is enabled for perfect matching.<br>This field is valid and applicable only when the L4DPM0 field is 1.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3181 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Disabled<br>1b - Enabled|
|20<br>L4DPM2|Layer 4 Destination Port Match Enable 2<br>Indicates the status of layer 4 destination port matching.<br>• If this field is 1,MAC_Layer4_Address0[L4DP0]is enabled for matching.<br>• If this field is 0, MAC ignoresMAC_Layer4_Address0[L4DP0]for matching.<br>0b - Disabled<br>1b - Enabled|
|19<br>L4SPIM2|Layer 4 Source Port Inverse Match Enable 2<br>Indicates the status of layer 4 source port inverse matching.<br>• If this field is 1,MAC_Layer4_Address0[L4SP0]is enabled for inverse matching.<br>• If this field is 0,MAC_Layer4_Address0[L4SP0]is enabled for perfect matching.<br>This field is valid and applicable only whenMAC_Layer4_Address0[L4SP0]= 1.<br>0b - Disabled<br>1b - Enabled|
|18|Layer 4 Source Port Match Enable 2|
|L4SPM2|Indicates the status of layer 4 source port matching.<br>• If this field is 1,MAC_Layer4_Address0[L4SP0]is enabled for matching.<br>• If this field is 0, MAC ignoresMAC_Layer4_Address0[L4SP0]for matching.<br>0b - Disabled<br>1b - Enabled|
|17|Reserved|
|—||
|16<br>L4PEN2|Layer 4 Protocol Enable 2<br>Indicates the status of layer 4 protocol.<br>• If this field is 1,MAC_Layer4_Address0[L4SP0]andMAC_Layer4_Address0[L4DP0]of UDP packets<br>are used for matching.<br>• If this field is 0,MAC_Layer4_Address0[L4SP0]andMAC_Layer4_Address0[L4DP0]of TCP packets<br>are used for matching.<br>Layer 4 matching is performed only when the L4SPM0 field or the L4DPM0 field is 1.<br>0b - Disabled<br>1b - Enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3182 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|15-11<br>L3HDBM2|Layer 3 IP DA Higher Bits Match 2<br>IPv4 Packets:<br>This field contains the number of higher bits of IP DA that are matched in the IPv4 packets. The following<br>list describes the values of this field:<br>• 0: No bits are masked.<br>• 1: LSb[0] is masked.<br>• 2: Two LSbs [1:0] are masked.<br>• ..<br>• 31: All bits except MSb are masked.<br>IPv6 Packets:<br>Bits [12:11] of this field correspond to bits [6:5] ofMAC_L3_L4_Control0[L3HSBM0], which indicates the<br>number of lower bits of IP SA or DA that are masked in the IPv6 packets. The following list describes the<br>concatenated values ofMAC_L3_L4_Control0[L3HDBM0][1:0] andMAC_L3_L4_Control0[L3HSBM0]:<br>• 0: No bits are masked.<br>• 1: LSb[0] is masked.<br>• 2: Two LSbs [1:0] are masked<br>• ..<br>• 127: All bits except MSb are masked.<br>This field is valid and applicable only whenMAC_L3_L4_Control0[L3DAM0]or<br>MAC_L3_L4_Control0[L3SAM0]is 1.|
|10-6<br>L3HSBM2|Layer 3 IP SA Higher Bits Match 2<br>IPv4 packets:<br>This field contains the number of lower bits of IP SA that are masked for matching in the IPv4 packets. The<br>following list describes the values of this field:<br>• 0: No bits are masked.<br>• 1: LSb[0] is masked.<br>• 2: Two LSbs [1:0] are masked.<br>• ..<br>• 31: All bits except MSb are masked.<br>IPv6 packets:<br>This field contains bits [4:0] ofMAC_L3_L4_Control0[L3HSBM0]. These bits indicate the number of<br>higher bits of IP SA or DA matched in the IPv6 packets. The field is valid and applicable only when<br>MAC_L3_L4_Control0[L3DAM0]orMAC_L3_L4_Control0[L3SAM0]is 1.|
|5|Layer 3 IP DA Inverse Match Enable 2|
|L3DAIM2|Indicates the status of layer 3 IP DA inverse matching.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3183 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function<br>• If this field is 1, layer 3 IP DA is enabled for inverse matching.<br>• If this field is 0, layer 3 IP DA is enabled for perfect matching.<br>This field is valid and applicable only ifMAC_L3_L4_Control0[L3DAM0]= 1.<br>0b - Disabled<br>1b - Enabled|
|---|---|
|4<br>L3DAM2|Layer 3 IP DA Match Enable 2<br>Indicates the status of layer 3 IP DA matching.<br>• If this field is 1, layer 3 IP DA is enabled for matching.<br>• If this field is 0, MAC ignores layer 3 IP DA for matching.<br>IfMAC_L3_L4_Control0[L3PEN0]= 1, you must write 1 to either this field or to<br>MAC_L3_L4_Control0[L3SAM0]because either the IPv6 DA or SA can be checked<br>for filtering.<br>~~NOTE~~|
||0b - Disabled<br>1b - Enabled|
|3<br>L3SAIM2|Layer 3 IP SA Inverse Match Enable 2<br>Indicates the status of layer 3 IP SA inverse matching.<br>• If this field is 1, layer 3 IP SA is enabled for inverse matching.<br>• If this field is 0, layer 3 IP SA is enabled for perfect matching.<br>This field is valid and applicable only ifMAC_L3_L4_Control0[L3SAM0]is 1.<br>0b - Disabled<br>1b - Enabled|
|2<br>L3SAM2|Layer 3 IP SA Match Enable 2<br>Indicates the status of layer 3 IP SA matching.<br>• If this field is 1, layer 3 IP SA matching is enabled.<br>• If this field is 0, MAC ignores layer 3 IP SA matching.<br>IfMAC_L3_L4_Control0[L3PEN0]= 1, you must write 1 to either this field or to<br>MAC_L3_L4_Control0[L3DAM0]because either IPv6 SA or DA can be checked for filtering.<br>~~NOTE~~<br>0b - Disabled<br>1b - Enabled|
|1<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3184 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|0|Layer 3 Protocol Enable 2|
|L3PEN2|Indicates the status of layer 3 protocol.|
||• If this field is 1, the layer 3 IP SA or DA matching is enabled for IPv6 packets.|
||• If this field is 0, the layer 3 IP SA or DA matching is enabled for IPv4 packets.<br>The layer 3 matching is performed only when eitherMAC_L3_L4_Control0[L3SAM0]or<br>MAC_L3_L4_Control0[L3DAM0]is 1.<br>0b - Disabled|
||1b - Enabled|



# 74.7.137 MAC Layer 4 Address 2 (MAC_Layer4_Address2) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer4_Address2|964h|



## Function 

## Provides the layer 4 source and destination port numbers. 

MAC Layer 4 Address 1 (MAC_Layer4_Address1), MAC L3 L4 Control 1 (MAC_L3_L4_Control1), MAC Layer 3 Address 0 Reg 1 (MAC_Layer3_Addr0_Reg1), MAC Layer 3 Address 1 Reg 1 (MAC_Layer3_Addr1_Reg1), MAC Layer 3 Address 2 Reg 1 (MAC_Layer3_Addr2_Reg1), and MAC Layer 3 Address 3 Reg 1 (MAC_Layer3_Addr3_Reg1) are reserved registers (RO with a default value) if the enable layer 3 and layer 4 packet filter option is not selected when configuring the core. 

You can configure the layer 3 and layer 4 address registers to be double-synchronized by selecting the synchronize layer 3 and layer 4 address registers to the receive clock domain option while configuring the core. When you select this option, the synchronization is triggered only when bits [31:24] (in Little-Endian mode) or bits [7:0] (in Big-Endian mode) of the layer 3 and layer 4 address registers are written to. For proper synchronization updates, you must perform consecutive writes to the same layer 3 and layer 4 address registers after a delay of at least four destination clock cycles. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L4|DP2||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L4|SP2||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3185 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Fields 

|Field|Function|
|---|---|
|31-16|Layer 4 Destination Port Number 2|
|L4DP2|Indicates layer 4 destination port number.<br>IfMAC_L3_L4_Control0[L4PEN0]= 0 andMAC_L3_L4_Control0[L4DPM0]= 1, this field contains the value<br>to be matched with the TCP destination port number field in the IPv4 or IPv6 packets.<br>IfMAC_L3_L4_Control0[L4PEN0]andMAC_L3_L4_Control0[L4DPM0]are 1, this field contains the value<br>to be matched with the UDP destination port number field in the IPv4 or IPv6 packets.|
|15-0|Layer 4 Source Port Number 2|
|L4SP2|Indicates layer 4 source port number.|
||IfMAC_L3_L4_Control0[L4PEN0]= 0 andMAC_L3_L4_Control0[L4SPM0]= 1, this field contains the value<br>to be matched with the TCP source port number field in the IPv4 or IPv6 packets.<br>IfMAC_L3_L4_Control0[L4PEN0]andMAC_L3_L4_Control0[L4SPM0]are 1, this field contains the value<br>to be matched with the UDP source port number field in the IPv4 or IPv6 packets.|



# 74.7.138 MAC Layer 3 Address 0 Reg 2 (MAC_Layer3_Addr0_Reg2) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr0_Re<br>g2|970h|



## Function 

Contains the 32-bit IP source address field for IPv4 packets. For IPv6 packets, the field contains bits [31:0] of the 128-bit IP source address or destination address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3A|02||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3A|02||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3186 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 0|
|L3A02|Indicates layer 3 address 0.|
||• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3SAM0]are 1, this field contains the<br>value to be matched with bits [31:0] of the IP source address field in the IPv6 packets.<br>• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3DAM0]are 1, this field contains the<br>value to be matched with bits [31:0] of the IP destination address field in the IPv6 packets.<br>• IfMAC_L3_L4_Control0[L3PEN0]= 0, andMAC_L3_L4_Control0[L3SAM0]= 1, this field contains<br>the value to be matched with the IP source address field in the IPv4 packets.|



# 74.7.139 MAC Layer 3 Address 1 Reg 2 (MAC_Layer3_Addr1_Reg2) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr1_Re<br>g2|974h|



## Function 

Contains the 32-bit IP destination address field for IPv4 packets. For IPv6 packets, the field contains bits[63:32] of the 128-bit IP source address or destination address field. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3187-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>L3A12<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>L3A12<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 1|
|L3A12|Indicates layer 3 address 1.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3187 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

|Field|Function|
|---|---|
||• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3SAM0]are 1, this field contains the<br>value to be matched with bits [63:32] of the IP source address field in the IPv6 packets.|
||• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3DAM0]are 1, this field contains the<br>value to be matched with bits [63:32] of the IP destination address field in the IPv6 packets.|
||• IfMAC_L3_L4_Control0[L3PEN0]= 0, andMAC_L3_L4_Control0[L3SAM0]= 1, this field contains<br>the value to be matched with the IP source address field in the IPv4 packets.|



# 74.7.140 MAC Layer 3 Address 2 Reg 2 (MAC_Layer3_Addr2_Reg2) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr2_Re<br>g2|978h|



## Function 

Contains the 32-bit IP destination address field for IPv4 packets. For IPv6 packets, the field contains bits [95:64] of the 128-bit IP source address or destination address field. 

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
|31-0|Layer 3 Address 2|
|L3A22|Indicates layer 3 address 2.|
||• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3SAM0]are 1, this field contains the<br>value to be matched with bits [95:64] of the IP source address field in the IPv6 packets.|
||• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3DAM0]are 1, this field contains the<br>value to be matched with bits [95:64] of the IP destination address field in the IPv6 packets.|
||• IfMAC_L3_L4_Control0[L3PEN0]= 0, this field is not used.|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3188 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

# 74.7.141 MAC Layer 3 Address 3 Reg 2 (MAC_Layer3_Addr3_Reg2) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr3_Re<br>g2|97Ch|



## Function 

Contains the 32-bit IP destination address field for IPv4 packets. For IPv6 packets, the field contains bits [127:96] of the 128-bit IP source address or destination address field. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3189-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>L3A32<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>L3A32<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 3|
|L3A32|Indicates layer 3 address 3.|
||• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3SAM0]are 1, this field contains the<br>value to be matched with bits [127:96] of the IP source address field in the IPv6 packets.<br>• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3DAM0]are 1, this field contains the<br>value to be matched with bits [127:96] of the IP destination address field in the IPv6 packets.<br>• IfMAC_L3_L4_Control0[L3PEN0]= 0, this field is not used.|



# 74.7.142 MAC L3 L4 Control 3 (MAC_L3_L4_Control3) 

## Offset 

|Register|Offset|
|---|---|
|MAC_L3_L4_Control3|990h|



## Function 

Controls the filter 0 operations of the layer 3 and layer 4 protocols. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3189 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Reserved||DMCH<br>EN3||Reserved||DMCH<br>N3|Rese|rved|L4DPI<br>M3|L4DP<br>M3|L4SPI<br>M3|L4SP<br>M3|Reserv<br>ed|L4PEN<br>3|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||L|3HDBM3|||||L3HSBM3|||L3DAI<br>M3|L3DA<br>M3|L3SAI<br>M3|L3SA<br>M3|Reserv<br>ed|L3PEN<br>3|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-29<br>—|Reserved|
|28|DMA Channel Select Enable 3|
|DMCHEN3|Indicates the status of the DMA channel number.<br>• If this field is 1, it enables the selection of the DMA channel number for the packet that the L3_L4<br>filter passes. The DMCHN fields indicate the DMA channel number.<br>• If this field is 0, the filter does not decide the DMA channel number.<br>0b - Disabled<br>1b - Enabled|
|27-25|Reserved|
|—<br>24|DMA Channel Number 2|
|DMCHN3|Indicates the DMA channel number.<br>If the value of the DMCHEN fields is 1, this field selects the DMA channel number to which the packet that<br>this filter passes is routed. The width of this field depends on the number of the DMA channels present in<br>your configuration.|
|23-22<br>—<br>21<br>L4DPIM3|Reserved<br>Layer 4 Destination Port Inverse Match Enable 3<br>Indicates the status of layer 4 destination port inverse matching.<br>• If this field is 1,MAC_Layer4_Address0[L4DP0]is enabled for inverse matching.<br>• If this field is 0,MAC_Layer4_Address0[L4DP0]is enabled for perfect matching.<br>This field is valid and applicable only when the L4DPM0 field is 1.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3190 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function<br>0b - Disabled<br>1b - Enabled|
|---|---|
|20<br>L4DPM3|Layer 4 Destination Port Match Enable 3<br>Indicates the status of layer 4 destination port matching.<br>• If this field is 1,MAC_Layer4_Address0[L4DP0]is enabled for matching.<br>• If this field is 0, MAC ignoresMAC_Layer4_Address0[L4DP0]for matching.<br>0b - Disabled<br>1b - Enabled|
|19<br>L4SPIM3|Layer 4 Source Port Inverse Match Enable 3<br>Indicates the status of layer 4 source port inverse matching.<br>• If this field is 1,MAC_Layer4_Address0[L4SP0]is enabled for inverse matching.<br>• If this field is 0,MAC_Layer4_Address0[L4SP0]is enabled for perfect matching.<br>This field is valid and applicable only whenMAC_Layer4_Address0[L4SP0]= 1.<br>0b - Disabled<br>1b - Enabled|
|18|Layer 4 Source Port Match Enable 3|
|L4SPM3|Indicates the status of layer 4 source port matching.<br>• If this field is 1,MAC_Layer4_Address0[L4SP0]is enabled for matching.<br>• If this field is 0, MAC ignoresMAC_Layer4_Address0[L4SP0]for matching.<br>0b - Disabled<br>1b - Enabled|
|17|Reserved|
|—||
|16<br>L4PEN3|Layer 4 Protocol Enable 3<br>Indicates the status of layer 4 protocol.<br>• If this field is 1,MAC_Layer4_Address0[L4SP0]andMAC_Layer4_Address0[L4DP0]of UDP packets<br>are used for matching.<br>• If this field is 0,MAC_Layer4_Address0[L4SP0]andMAC_Layer4_Address0[L4DP0]of TCP packets<br>are used for matching.<br>Layer 4 matching is performed only when the L4SPM0 field or the L4DPM0 field is 1.<br>0b - Disabled<br>1b - Enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3191 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|15-11<br>L3HDBM3|Layer 3 IP DA Higher Bits Match 3<br>IPv4 Packets:<br>This field contains the number of higher bits of IP DA that are matched in the IPv4 packets. The following<br>list describes the values of this field:<br>• 0: No bits are masked.<br>• 1: LSb[0] is masked.<br>• 2: Two LSbs [1:0] are masked.<br>• ..<br>• 31: All bits except MSb are masked.<br>IPv6 Packets:<br>Bits [12:11] of this field correspond to bits [6:5] ofMAC_L3_L4_Control0[L3HSBM0], which indicates the<br>number of lower bits of IP SA or DA that are masked in the IPv6 packets. The following list describes the<br>concatenated values ofMAC_L3_L4_Control0[L3HDBM0][1:0] andMAC_L3_L4_Control0[L3HSBM0]:<br>• 0: No bits are masked.<br>• 1: LSb[0] is masked.<br>• 2: Two LSbs [1:0] are masked<br>• ..<br>• 127: All bits except MSb are masked.<br>This field is valid and applicable only whenMAC_L3_L4_Control0[L3DAM0]or<br>MAC_L3_L4_Control0[L3SAM0]is 1.|
|10-6<br>L3HSBM3|.<br>Layer 3 IP SA Higher Bits Match 3<br>IPv4 packets:<br>This field contains the number of lower bits of IP SA that are masked for matching in the IPv4 packets. The<br>following list describes the values of this field:<br>• 0: No bits are masked.<br>• 1: LSb[0] is masked.<br>• 2: Two LSbs [1:0] are masked.<br>• ..<br>• 31: All bits except MSb are masked.<br>IPv6 packets:<br>This field contains bits [4:0] ofMAC_L3_L4_Control0[L3HSBM0]. These bits indicate the number of<br>higher bits of IP SA or DA matched in the IPv6 packets. The field is valid and applicable only when<br>MAC_L3_L4_Control0[L3DAM0]orMAC_L3_L4_Control0[L3SAM0]is 1.|
|5|Layer 3 IP DA Inverse Match Enable 3|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3192 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|L3DAIM3|Indicates the status of layer 3 IP DA inverse matching.<br>• If this field is 1, layer 3 IP DA is enabled for inverse matching.<br>• If this field is 0, layer 3 IP DA is enabled for perfect matching.<br>This field is valid and applicable only ifMAC_L3_L4_Control0[L3DAM0]= 1.<br>0b - Disabled<br>1b - Enabled|
|4<br>L3DAM3|Layer 3 IP DA Match Enable 3<br>Indicates the status of layer 3 IP DA matching.<br>• If this field is 1, layer 3 IP DA is enabled for matching.<br>• If this field is 0, MAC ignores layer 3 IP DA for matching.<br>IfMAC_L3_L4_Control0[L3PEN0]= 1, you must write 1 to either this field or to<br>MAC_L3_L4_Control0[L3SAM0]because either the IPv6 DA or SA can be checked<br>for filtering.<br>~~NOTE~~|
||0b - Disabled<br>1b - Enabled|
|3<br>L3SAIM3|Layer 3 IP SA Inverse Match Enable 3<br>Indicates the status of layer 3 IP SA inverse matching.<br>• If this field is 1, layer 3 IP SA is enabled for inverse matching.<br>• If this field is 0, layer 3 IP SA is enabled for perfect matching.<br>This field is valid and applicable only ifMAC_L3_L4_Control0[L3SAM0]is 1.<br>0b - Disabled<br>1b - Enabled|
|2<br>L3SAM3|Layer 3 IP SA Match Enable 3<br>Indicates the status of layer 3 IP SA matching.<br>• If this field is 1, layer 3 IP SA matching is enabled.<br>• If this field is 0, MAC ignores layer 3 IP SA matching.<br>IfMAC_L3_L4_Control0[L3PEN0]= 1, you must write 1 to either this field or to<br>MAC_L3_L4_Control0[L3DAM0]because either IPv6 SA or DA can be checked for filtering.<br>~~NOTE~~<br>0b - Disabled<br>1b - Enabled|
|1|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3193 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|0|Layer 3 Protocol Enable 3|
|L3PEN3|Indicates the status of layer 3 protocol.|
||• If this field is 1, the layer 3 IP SA or DA matching is enabled for IPv6 packets.<br>• If this field is 0, the layer 3 IP SA or DA matching is enabled for IPv4 packets.<br>The layer 3 matching is performed only when eitherMAC_L3_L4_Control0[L3SAM0]or<br>MAC_L3_L4_Control0[L3DAM0]is 1.|
||0b - Disabled<br>1b - Enabled|



# 74.7.143 MAC Layer 4 Address 3 (MAC_Layer4_Address3) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer4_Address3|994h|



## Function 

## Provides the layer 4 source and destination port numbers. 

MAC Layer 4 Address 1 (MAC_Layer4_Address1), MAC L3 L4 Control 1 (MAC_L3_L4_Control1), MAC Layer 3 Address 0 Reg 1 (MAC_Layer3_Addr0_Reg1), MAC Layer 3 Address 1 Reg 1 (MAC_Layer3_Addr1_Reg1), MAC Layer 3 Address 2 Reg 1 (MAC_Layer3_Addr2_Reg1), and MAC Layer 3 Address 3 Reg 1 (MAC_Layer3_Addr3_Reg1) are reserved registers (RO with a default value) if the enable layer 3 and layer 4 packet filter option is not selected when configuring the core. 

You can configure the layer 3 and layer 4 address registers to be double-synchronized by selecting the synchronize layer 3 and layer 4 address registers to the receive clock domain option while configuring the core. When you select this option, the synchronization is triggered only when bits [31:24] (in Little-Endian mode) or bits [7:0] (in Big-Endian mode) of the layer 3 and layer 4 address registers are written to. For proper synchronization updates, you must perform consecutive writes to the same layer 3 and layer 4 address registers after a delay of at least four destination clock cycles. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L4|DP3||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L4|SP3||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3194 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Fields 

|Field|Function|
|---|---|
|31-16|Layer 4 Destination Port Number 3|
|L4DP3|Indicates layer 4 destination port number.<br>IfMAC_L3_L4_Control0[L4PEN0]= 0 andMAC_L3_L4_Control0[L4DPM0]= 1, this field contains the value<br>to be matched with the TCP destination port number field in the IPv4 or IPv6 packets.<br>IfMAC_L3_L4_Control0[L4PEN0]andMAC_L3_L4_Control0[L4DPM0]are 1, this field contains the value<br>to be matched with the UDP destination port number field in the IPv4 or IPv6 packets.|
|15-0|Layer 4 Source Port Number 3|
|L4SP3|Indicates layer 4 source port number.|
||IfMAC_L3_L4_Control0[L4PEN0]= 0 andMAC_L3_L4_Control0[L4SPM0]= 1, this field contains the value<br>to be matched with the TCP source port number field in the IPv4 or IPv6 packets.<br>IfMAC_L3_L4_Control0[L4PEN0]andMAC_L3_L4_Control0[L4SPM0]are 1, this field contains the value<br>to be matched with the UDP source port number field in the IPv4 or IPv6 packets.|



# 74.7.144 MAC Layer 3 Address 0 Reg 3 (MAC_Layer3_Addr0_Reg3) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr0_Re<br>g3|9A0h|



## Function 

Contains the 32-bit IP source address field for IPv4 packets. For IPv6 packets, the field contains bits [31:0] of the 128-bit IP source address or destination address field. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||L3A|03||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||L3A|03||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3195 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 0|
|L3A03|Indicates layer 3 address 0.|
||• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3SAM0]are 1, this field contains the<br>value to be matched with bits [31:0] of the IP source address field in the IPv6 packets.<br>• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3DAM0]are 1, this field contains the<br>value to be matched with bits [31:0] of the IP destination address field in the IPv6 packets.<br>• IfMAC_L3_L4_Control0[L3PEN0]= 0, andMAC_L3_L4_Control0[L3SAM0]= 1, this field contains<br>the value to be matched with the IP source address field in the IPv4 packets.|



# 74.7.145 MAC Layer 3 Address 1 Reg 3 (MAC_Layer3_Addr1_Reg3) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr1_Re<br>g3|9A4h|



## Function 

Contains the 32-bit IP destination address field for IPv4 packets. For IPv6 packets, the field contains bits [63:32] of the 128-bit IP source address or destination address field. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3196-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>L3A13<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>L3A13<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 1|
|L3A13|Indicates layer 3 address 1.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3196 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

|Field|Function|
|---|---|
||• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3SAM0]are 1, this field contains the<br>value to be matched with bits [63:32] of the IP source address field in the IPv6 packets.|
||• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3DAM0]are 1, this field contains the<br>value to be matched with bits [63:32] of the IP destination address field in the IPv6 packets.|
||• IfMAC_L3_L4_Control0[L3PEN0]= 0, andMAC_L3_L4_Control0[L3SAM0]= 1, this field contains<br>the value to be matched with the IP source address field in the IPv4 packets.|



# 74.7.146 MAC Layer 3 Address 2 Reg 3 (MAC_Layer3_Addr2_Reg3) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr2_Re<br>g3|9A8h|



## Function 

Contains the 32-bit IP destination address field for IPv4 packets. For IPv6 packets, the field contains bits [95:64] of the 128-bit IP source address or destination address field. 

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
|31-0|Layer 3 Address 2|
|L3A23|Indicates layer 3 address 2.|
||• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3SAM0]are 1, this field contains the<br>value to be matched with bits [95:64] of the IP source address field in the IPv6 packets.|
||• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3DAM0]are 1, this field contains the<br>value to be matched with bits [95:64] of the IP destination address field in the IPv6 packets.|
||• IfMAC_L3_L4_Control0[L3PEN0]= 0, this field is not used.|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3197 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

# 74.7.147 MAC Layer 3 Address 3 Reg 3 (MAC_Layer3_Addr3_Reg3) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Layer3_Addr3_Re<br>g3|9ACh|



## Function 

Contains the 32-bit IP destination address field for IPv4 packets. For IPv6 packets, the field contains bits [127:96] of the 128-bit IP source address or destination address field. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3198-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>L3A33<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>L3A33<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Layer 3 Address 3|
|L3A33|Indicates layer 3 address 3.|
||• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3SAM0]are 1, this field contains the<br>value to be matched with bits [127:96] of the IP source address field in the IPv6 packets.<br>• IfMAC_L3_L4_Control0[L3PEN0]andMAC_L3_L4_Control0[L3DAM0]are 1, this field contains the<br>value to be matched with bits [127:96] of the IP destination address field in the IPv6 packets.<br>• IfMAC_L3_L4_Control0[L3PEN0]= 0, this field is not used.|



# 74.7.148 MAC Timestamp Control (MAC_Timestamp_Control) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Timestamp_Contro|B00h|
|l||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3198 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Function 

Controls the operation of the system time generator and processing of PTP packets for timestamping in the receiver. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3199-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R AV802 TXTSS Reserv TSEN<br>Reserved  Reserved  Reserved  ESTI  SNAPTYPSEL<br>W 1A... TSM  ed  MAC...<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TSMS TSEV TSIPV TSIPV TSIPE TSVE TSCT TSEN Reserv TSAD Reserv TSUP TSCF TSEN<br>PTGE  TSINIT<br>W TRE... NTE... 4E... 6E... NA  R2E... RLS... ALL  ed  DREG  ed  DT  UPDT  A<br>Reset 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-29<br>—|Reserved|
|28|AV 802.1AS Mode Enable|
|AV8021ASMEN|Indicates the status of AV 802.1AS mode.<br>If this field is 1, MAC processes only untagged PTP over Ethernet packets for providing PTP status and<br>capturing timestamp snapshots, which means using the IEEE 802.1AS mode of operation.<br>IfMAC_HW_Feature1[PTOEN]= 1, for the purpose of PTP offload, the transport-specific field in the PTP<br>header is generated and checked based on the value of the AV8021ASMEN field.<br>0b - Disabled<br>1b - Enabled|
|27-25<br>—|Reserved|
|24<br>TXTSSTSM|Transmit Timestamp Status Mode<br>Indicates the status of transmit timestamp status mode.<br>• If this field is 1, MAC overwrites the previous transmit timestamp status even if the software does not<br>read it. MAC indicates this by writing 1 toMAC_Tx_Timestamp_Status_Nanoseconds[TXTSSMIS].<br>• If this field is 0, MAC ignores the timestamp status of the current packet if the software does<br>not read the timestamp status of the previous packet. MAC indicates this by writing 1 to<br>MAC_Tx_Timestamp_Status_Nanoseconds[TXTSSMIS].<br>0b - Disabled<br>1b - Enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3199 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field<br>23-21<br>—|Function<br>Reserved|
|---|---|
|20<br>ESTI|External System Time Input<br>Indicates the status of external system time input.<br>If this field is 1, MAC uses the external 64-bit reference system time input for these functions:<br>• To consider the timestamp provided as status<br>• To insert the timestamp in transmit PTP packets if the one-step timestamp or the timestamp offload<br>feature is enabled<br>If this field is 1, MAC uses the internal reference system time.<br>0b - Disabled<br>1b - Enabled|
|19<br>—|Reserved|
|18<br>TSENMACADD<br>R|Enable MAC Address For PTP Packet Filtering<br>Indicates whether the MAC address for PTP packet filtering is enabled.<br>If this field is 1, the DA MAC address, which matches any MAC Address register, is used to filter the PTP<br>packets when PTP is directly sent over Ethernet.<br>If this field is 1, received PTP packets with DA containing a special multicast or unicast address that matches<br>the one programmed in the MAC address registers are considered for processing when PTP is directly sent<br>over Ethernet.<br>• For a normal time stamping operation, MAC address registers 0 to 31 are considered for unicast<br>destination address matching.<br>• For PTP offload, only MAC address register 0 is considered for unicast destination address<br>matching.<br>0b - Disabled<br>1b - Enabled|
|17-16<br>SNAPTYPSEL|Select PTP Packets For Taking Snapshots<br>Determines the set of PTP packet types for which a snapshot needs to be taken.<br>This field, along with the TSEVNTENA and TSMSTRENA fields, determines the set of PTP packet types for<br>which a snapshot needs to be taken. SeeReceive path functionsfor encoding.|
|15<br>TSMSTRENA|Enable Snapshot For Messages Relevant To Master<br>Indicates whether the snapshot for messages relevant to master is enabled.<br>If this field is 1, the snapshot is taken only for the messages that are relevant to the master node. Otherwise,<br>the snapshot is taken for the messages relevant to the slave node.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3200 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function<br>0b - Disabled<br>1b - Enabled|
|---|---|
|14<br>TSEVNTENA|Enable Timestamp Snapshot For Event Messages<br>Enables or disables timestamp snapshot for event messages.<br>If this field is 1, the timestamp snapshot is taken only for event messages (SYNC, Delay_Req, Pdelay_Req,<br>or Pdelay_Resp). When the field becomes 0, the snapshot is taken for all the messages except Announce,<br>Management, and Signaling. For more information on timestamp snapshot dependency on register bits, see<br>Receive path functions.<br>0b - Disabled<br>1b - Enabled|
|13<br>TSIPV4ENA|Enable Processing Of PTP Packets Sent Over IPv4-UDP<br>Indicates whether the processing of PTP packets sent over IPv4-UDP is enabled.<br>If this field is 1, the MAC receiver processes the PTP packets encapsulated in the IPv4-UDP packets. When<br>this field becomes 0, MAC ignores the PTP transported over the IPv4-UDP packets. The default value of this<br>field is 1.<br>0b - Disabled<br>1b - Enabled|
|12<br>TSIPV6ENA|Enable Processing Of PTP Packets Sent Over IPv6-UDP<br>Indicates whether the processing of PTP packets sent over IPv6-UDP is enabled.<br>If this field is 1, the MAC receiver processes the PTP packets encapsulated in the IPv6-UDP packets. If the<br>value is 0, MAC ignores the PTP transported over IPv6-UDP packets.<br>0b - Disabled<br>1b - Enabled|
|11<br>TSIPENA|Enable Processing Of PTP Over Ethernet Packets<br>Indicates the status of PTP processing over Ethernet packets.<br>If this field is 1, the MAC receiver processes the PTP packets encapsulated directly in the Ethernet packets.<br>When the field becomes 0, MAC ignores the PTP over Ethernet packets.<br>0b - Disabled<br>1b - Enabled|
|10<br>TSVER2ENA|Enable PTP Packet Processing For Version 2 Format<br>Indicates the status of PTP packet processing for version 2 format.<br>If this field is 1, the IEEE 1588 version 2 format is used to process the PTP packets. When this field becomes<br>0, the IEEE 1588 version 1 format is used to process the PTP packets. SeePTP processing and controlfor<br>more information on the IEEE 1588 formats.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3201 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function<br>0b - Disabled<br>1b - Enabled|
|---|---|
|9<br>TSCTRLSSR|Timestamp Digital Or Binary Rollover Control<br>Indicates the status of timestamp digital or binary rollover control.<br>• If this field is 1, the Timestamp Low register rolls over after the 3B9A_C9FFh value (that is, 1<br>nanosecond accuracy) and increments the timestamp (high) seconds.<br>• If this field is 0, the rollover value of the Subsecond register is 7FFF_FFFFh. The sub-second<br>increment must be programmed correctly depending on the PTP reference clock frequency and the<br>value of this field.<br>0b - Disabled<br>1b - Enabled|
|8<br>TSENALL|Enable Timestamp For All Packets<br>Indicates the status of timestamp snapshot for all packets.<br>If this field is 1, the timestamp snapshot is enabled for all packets that MAC receives.<br>0b - Disabled<br>1b - Enabled|
|7<br>—|Reserved|
|6<br>PTGE|Presentation Time Generation Enable<br>Indicates the status of presentation time generation.<br>If this field is 1, the presentation time generation is enabled.<br>0b - Disabled<br>1b - Enabled|
|5<br>TSADDREG|Update Addend Register<br>Indicates whetherMAC Timestamp Addend (MAC_Timestamp_Addend)is updated.<br>If this field is 1, the contents ofMAC Timestamp Addend (MAC_Timestamp_Addend)are updated in the PTP<br>block for fine correction. The field becomes 0 after the update completes. The value of the field must also<br>be 0 before you write 1 to it.<br>Access restrictions apply to this field that clears automatically. Writing 0 has no effect.<br>0b - Not updated<br>1b - Updated|
|4<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3202 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|3|Update Timestamp|
|TSUPDT|Indicates whether the timestamp is updated.<br>If this field is 1, the system time is updated (added or subtracted) with the value specified inMAC System<br>Time Seconds Update (MAC_System_Time_Seconds_Update)andMAC System Time Nanoseconds<br>Update (MAC_System_Time_Nanoseconds_Update).<br>The value of this field must be 0 before you update it. It resets after the update is complete in hardware.<br>MAC_System_Time_Higher_Word_Seconds[TSHWR], if enabled during core configuration, is not updated.<br>When media clock generation and recovery is configured (DWC_EQOS_FLEXI_PPS_OUT_EN) and<br>enabled,MAC Presentation Time Update (MAC_Presn_Time_Updt)must also be updated before you write<br>1 to this field.<br>Access restrictions apply to this field that clears automatically. Writing 0 has no effect.<br>0b - Not updated<br>1b - Updated|
|2<br>TSINIT|Initialize Timestamp<br>Indicates whether the timestamp is initialized.<br>If this field is 1, the system time is initialized (overwritten) with the value specified inMAC System<br>Time Seconds Update (MAC_System_Time_Seconds_Update)andMAC System Time Nanoseconds<br>Update (MAC_System_Time_Nanoseconds_Update).<br>The value of this field must be 0 before you update it, and the field is reset after the initialization is<br>complete.MAC_System_Time_Higher_Word_Seconds[TSHWR], if enabled during core configuration, can<br>only be initialized.<br>When media clock generation and recovery is configured (DWC_EQOS_FLEXI_PPS_OUT_EN) and<br>enabled,MAC Presentation Time Update (MAC_Presn_Time_Updt)must also be updated before you write<br>1 to this field.<br>Access restrictions apply to this field that clears automatically. Writing 0 has no effect.<br>0b - Not initialized<br>1b - Initialized|
|1|Fine Or Coarse Timestamp Update|
|TSCFUPDT|Indicates the method used to update system timestamp.<br>• If this field is 1, the fine method is used to update system timestamp.<br>• If this field is 0, the coarse method is used to update the system timestamp.<br>0b - Coarse method<br>1b - Fine method|
|0<br>TSENA|Timestamp Enable<br>Enables or disables timestamp for transmit and receive packets.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3203 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||• If this field is 1, the timestamp is added for transmit and receive packets.|
||• If this field is 0, timestamp is not added for transmit and receive packets and the timestamp<br>generator is also suspended. You need to initialize the timestamp (system time) after enabling this<br>mode.|
||On the receive side, MAC processes the 1588 packets only if this field is 1.|
||0b - Disabled|
||1b - Enabled|



# 74.7.149 MAC Sub Second Increment (MAC_Sub_Second_Increment) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Sub_Second_Incre|B04h|
|ment||



## Function 

Specifies the value to be added to the internal system time register at every cycle of the clk_ptp_ref_i clock. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||Rese|rved|||||||SSI|NC||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||SNS|INC|||||||Rese|rved||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-24<br>—|Reserved|
|23-16|Sub-Second Increment Value|
|SSINC||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3204 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||Contains the sub-second incement value, which accumulates every clock cycle (of clk_ptp_i) with the<br>contents of the Subsecond register. For example, if the PTP clock is 50 MHz (period is 20 ns), you must<br>program 20 (14h) whenMAC System Time In Nanoseconds (MAC_System_Time_Nanoseconds)has an<br>accuracy of 1 ns (MAC_Timestamp_Control[TSCTRLSSR]= 1). When TSCTRLSSR = 0, the Nanoseconds<br>register has a resolution of ~0.465 ns. In this case, you must program a value of 43 (2Bh), which is derived<br>by 20 ns/0.465.|
|15-8|Sub-Nanosecond Increment Value|
|SNSINC|Contains the sub-nanosecond increment value, represented in nanoseconds multiplied by 2^8. This<br>value is accumulated in the sub-nanoseconds field of the Subsecond register. For example, if<br>MAC_Timestamp_Control[TSCTRLSSR]= 1, and if the required increment is 5.3 ns, then this field must be<br>4Ch and the SSINC field must be 05h.|
|7-0<br>—|Reserved|



# 74.7.150 MAC System Time In Seconds (MAC_System_Time_Seconds) 

## Offset 

|Register|Offset|
|---|---|
|MAC_System_Time_Sec<br>onds|B08h|



## Function 

Indicates, along with MAC System Time In Nanoseconds (MAC_System_Time_Nanoseconds), the current value of the system time that MAC maintains. Although it is updated on a continuous basis, there is some delay from the actual time because of clock domain transfer latencies (from clk_ptp_ref_i to the CSR clock). 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||TS|S||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||TS|S||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3205 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0|Timestamp Second|
|TSS|Indicates the current value, in seconds, of the system time that MAC maintains.|



# 74.7.151 MAC System Time In Nanoseconds (MAC_System_Time_Nanoseconds) 

## Offset 

|Register|Offset|
|---|---|
|MAC_System_Time_Nan<br>oseconds|B0Ch|



## Function 

Indicates, along with MAC System Time In Seconds (MAC_System_Time_Seconds), the current value of the system time that MAC maintains. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|Reserv||||||||TSSS||||||||
|W|ed||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||TS|SS||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31|Reserved|
|—||
|30-0|Timestamp Sub Seconds|
|TSSS|Indicates the sub-second representation of time, with an accuracy of 0.46 ns. When<br>MAC_Timestamp_Control[TSCTRLSSR]= 1, each bit represents 1 ns. The maximum value is<br>3B9A_C9FFh after which it rolls over to 0.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3206 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

# 74.7.152 MAC System Time Seconds Update (MAC_System_Time_Seconds_Update) 

## Offset 

|Register|Offset|
|---|---|
|MAC_System_Time_Sec|B10h|
|onds_Update||



## Function 

Initializes or updates, along with MAC System Time Nanoseconds Update (MAC_System_Time_Nanoseconds_Update), the system time that MAC maintains. You must write both to this register and the MAC System Time Nanoseconds Update register before writing 1 to MAC_Timestamp_Control[TSINIT] and MAC_Timestamp_Control[TSUPDT]. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3207-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>TSS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>TSS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Timestamp Seconds|
|TSS|Indicates the timestamp seconds value.|
||The value in this field is the seconds part of the update.<br>• IfMAC_System_Time_Nanoseconds_Update[ADDSUB]= 0, this field must be programmed with the<br>seconds part of the update value.|
||• IfMAC_System_Time_Nanoseconds_Update[ADDSUB]= 1, this field must be programmed with the<br>complement of the seconds part of the update value.|
||For example, if 2.000000001 seconds need to be subtracted from the system time,<br>MAC_System_Time_Seconds[TSS]must be FFFF_FFFEh (that is, 2^32 - 2).|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3207 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

# 74.7.153 MAC System Time Nanoseconds Update (MAC_System_Time_Nanoseconds_Update) 

## Offset 

|Register|Offset|
|---|---|
|MAC_System_Time_Nan|B14h|
|oseconds_Update||



## Function 

Indicates system time nanoseconds update. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3208-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R ADDS<br>TSSS<br>W UB<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>TSSS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31|Add Or Subtract Time|
|ADDSUB|Indicates whether the time value is added or subtracted from the contents of the update register.<br>• If this field is 1, the time value is subtracted from the contents of the update register.<br>• If this field is 0, the time value is added to the contents of the update register.<br>0b - Add time<br>1b - Subtract time|
|30-0<br>TSSS|Timestamp Subseconds<br>Indicates the sub-second part of the update.<br>• If ADDSUB = 0, this field must be programmed with the sub-second part of the update value, with an<br>accuracy based onMAC_Timestamp_Control[TSCTRLSSR].<br>• If ADDSUB = 0, this field must be programmed with the complement of the sub-second part of the<br>update value as described below.<br>• IfMAC_Timestamp_Control[TSCTRLSSR]= 1, the programmed value must be 10^9 - <sub-second<br>value>, and ifMAC_Timestamp_Control[TSCTRLSSR]= 0, the programmed value must be 2^31 -<br><sub-second_value>.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3208 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||• IfMAC_Timestamp_Control[TSCTRLSSR]= 0, each bit of it represents an accuracy of 0.46 ns, and<br>ifMAC_Timestamp_Control[TSCTRLSSR]= 1, each bit represents 1 ns and the programmed value<br>must not exceed 3B9A_C9FFh.|
||For example, if 2.000000001 seconds need to be subtracted from the system time, this field must<br>be 7FFF_FFFFh (that is, 2^31 - 1) ifMAC_Timestamp_Control[TSCTRLSSR]= 0. This field must be|
||3B9A_C9FFh (that is, 10^9 - 1) ifMAC_Timestamp_Control[TSCTRLSSR]= 1.|



# 74.7.154 MAC Timestamp Addend (MAC_Timestamp_Addend) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Timestamp_Adden<br>d|B18h|



## Function 

Is used only when the system time is configured for Fine Update mode (MAC_Timestamp_Control[TSINIT] = 1). The contents of this register are added to a 32-bit accumulator in every clock cycle (of clk_ptp_ref_i), and the system time is updated whenever the accumulator overflows. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3209-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>TSAR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>TSAR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-0|Timestamp Addend Register|
|TSAR|Indicates the 32-bit time value to be added to the Accumulator register to achieve time synchronization.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3209 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

# 74.7.155 MAC System Time Higher Word In Seconds (MAC_System_Time_Higher_Word_Seconds) 

## Offset 

|Register|Offset|
|---|---|
|MAC_System_Time_Hig|B1Ch|
|her_Word_Seconds||



## Function 

Indicates system time - higher word in seconds. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3210-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>TSHWR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-16|Reserved|
|—||
|15-0|Timestamp Higher Word Register|
|TSHWR|Contains the most-significant 16 bits of the timestamp seconds value. This register is optional, and you<br>can add it if you select the IEEE 1588 higher-word register option. You write to this register directly to<br>initialize the value, which increments when there is an overflow from the 32 bits ofMAC System Time In<br>Seconds (MAC_System_Time_Seconds).|
||Access restrictions apply to this field, which updates based on an event occurrence.|



# 74.7.156 MAC Timestamp Status (MAC_Timestamp_Status) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Timestamp_Status|B20h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3210 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Function 

Indicates timestamp status. All the bits except [27:25] are cleared when the application reads this register. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3211-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserv<br>Reserved  Reserved  Reserved  Reserved<br>W ed<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>TXTSS TSTR TSTA TSTR TSTA TSTR TSTA TSTR TSTA TSSO<br>R<br>IS  GTE... RGT3  GTE... RGT2  GTE... RGT1  GTE... Reserv RGT0  VF<br>Reserved<br>ed<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29-25<br>—|Reserved|
|24|Reserved|
|—||
|23-20<br>—|Reserved|
|19-16<br>—|Reserved|
|15|Transmit Timestamp Status Interrupt Status|
|TXTSSIS|Indicates whether the transmit timestamp interrupt status is detected.<br>In non-EQOS_CORE configurations, if the drop transmit status is enabled in MTL, this field<br>becomes 1 when the captured transmit timestamp is updated inMAC Transmit Timestamp<br>Status In Seconds (MAC_Tx_Timestamp_Status_Seconds)andMAC Transmit Timestamp Status In<br>Nanoseconds (MAC_Tx_Timestamp_Status_Nanoseconds).<br>IfMAC_HW_Feature1[PTOEN]= 1, TXTSSIS becomes 1 when the captured transmit timestamp is<br>updated inMAC Transmit Timestamp Status In Seconds (MAC_Tx_Timestamp_Status_Seconds)and<br>MAC Transmit Timestamp Status In Nanoseconds (MAC_Tx_Timestamp_Status_Nanoseconds)for PTO-<br>generated delay request and Pdelay request packets.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3211 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function<br>This field becomes 0 if you read or write toMAC Transmit Timestamp Status In Seconds<br>(MAC_Tx_Timestamp_Status_Seconds)whenMAC_CSR_SW_Ctrl[RCWE]= 1.<br>0b - Not detected<br>1b - Detected|
|---|---|
|14-10<br>—|Reserved|
|9<br>TSTRGTERR3|Timestamp Target Time Error<br>Indicates whether the timestamp target time error status is detected.<br>This field becomes 1 if the latest target time programmed inMAC PPS3 Target Time<br>In Seconds (MAC_PPS3_Target_Time_Seconds)andMAC PPS3 Target Time In Nanoseconds<br>(MAC_PPS3_Target_Time_Nanoseconds)elapses. The field becomes 0 when the application reads it.<br>Access restrictions apply to this field that clears when read (or when this field is written to 1 if<br>MAC_CSR_SW_Ctrl[RCWE]= 1). Also, the field automatically becomes 1 on an internal event occurrence.<br>0b - Not detected<br>1b - Detected|
|8<br>TSTARGT3|Timestamp Target Time Reached For Target Time PPS3<br>Indicates whether the timestamp target time reached for target time PPS3 status is detected.<br>If this field is 1, it indicates that the value of the system time is greater than or equal to the value specified<br>inMAC PPS3 Target Time In Seconds (MAC_PPS3_Target_Time_Seconds)andMAC PPS3 Target Time<br>In Nanoseconds (MAC_PPS3_Target_Time_Nanoseconds).<br>Access restrictions apply to this field that clears when read (or when this field is written to 1 if<br>MAC_CSR_SW_Ctrl[RCWE]= 1). Also, the field automatically becomes 1 on an internal event occurrence.<br>0b - Not detected<br>1b - Detected|
|7<br>TSTRGTERR2|Timestamp Target Time Error<br>Indicates whether the timestamp target time error status is detected.<br>This field becomes 1 when the latest target time programmed inMAC PPS2 Taget Time<br>In Seconds (MAC_PPS2_Target_Time_Seconds)andMAC PPS2 Target Time In Nanoseconds<br>(MAC_PPS2_Target_Time_Nanoseconds)elapses. The field becomes 0 when the application reads it.<br>Access restrictions apply to this field that clears when read (or when this field is written to 1 if<br>MAC_CSR_SW_Ctrl[RCWE]= 1). Also, the field automatically becomes 1 on an internal event occurrence.<br>0b - Not detected<br>1b - Detected|
|6<br>TSTARGT2|Timestamp Target Time Reached For Target Time PPS2<br>Indicates whether the timestamp target time reached for the target time PPS2 status is detected.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3212 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||If this field is 1, it indicates that the value of system time is greater than or equal to the value specified in<br>MAC PPS2 Taget Time In Seconds (MAC_PPS2_Target_Time_Seconds)andMAC PPS2 Target Time In<br>Nanoseconds (MAC_PPS2_Target_Time_Nanoseconds).<br>Access restrictions apply to this field that clears when read (or when this field is written to 1 if<br>MAC_CSR_SW_Ctrl[RCWE]= 1). Also, the field automatically becomes 1 on an internal event occurrence.<br>0b - Not detected<br>1b - Detected|
|5<br>TSTRGTERR1|Timestamp Target Time Error<br>Indicates whether the timestamp target time error status is detected.<br>This field becomes 1 when the latest target time programmed inMAC PPS1 Target Time<br>In Seconds (MAC_PPS1_Target_Time_Seconds)andMAC PPS1 Target Time In Nanoseconds<br>(MAC_PPS1_Target_Time_Nanoseconds)elapses. The field becomes 0 when the application reads it.<br>Access restrictions apply to this field that clears when read (or when this field is written to 1 if<br>MAC_CSR_SW_Ctrl[RCWE]= 1). Also, the field automatically becomes 1 on an internal event occurrence.<br>0b - Not detected<br>1b - Detected|
|4<br>TSTARGT1|Timestamp Target Time Reached For Target Time PPS1<br>Indicates whether the timestamp target time reached for target time PPS1 status is detected.<br>If this field is 1, it indicates that the value of system time is greater than or equal to the value specified in<br>MAC PPS1 Target Time In Seconds (MAC_PPS1_Target_Time_Seconds)andMAC PPS1 Target Time In<br>Nanoseconds (MAC_PPS1_Target_Time_Nanoseconds)<br>Access restrictions apply to this field that clears when read (or when this field is written to 1 if<br>MAC_CSR_SW_Ctrl[RCWE]= 1). Also, the field automatically becomes 1 on an internal event occurrence.<br>0b - Not detected<br>1b - Detected|
|3<br>TSTRGTERR0|Timestamp Target Time Error<br>Indicates whether the timestamp target time error status is detected.<br>This field becomes 1 when the latest target time programmed inMAC PPS0 Target Time<br>In Seconds (MAC_PPS0_Target_Time_Seconds)andMAC PPS0 Target Time In Nanoseconds<br>(MAC_PPS0_Target_Time_Nanoseconds)elapses. The field becomes 0 when the application reads it.<br>Access restrictions apply to this field that clears when read (or when this field is written to 1 if<br>MAC_CSR_SW_Ctrl[RCWE]= 1). Also, the field automatically becomes 1 on an internal event occurrence.<br>0b - Not detected<br>1b - Detected|
|2<br>—|Reserved<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3213 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|1|Timestamp Target Time Reached|
|TSTARGT0|Indicates whether the timestamp target time reached status is detected.<br>If this field is 1, it indicates that the value of the system time is greater than or equal to the value specified<br>inMAC PPS0 Target Time In Seconds (MAC_PPS0_Target_Time_Seconds)andMAC PPS0 Target Time<br>In Nanoseconds (MAC_PPS0_Target_Time_Nanoseconds)<br>Access restrictions apply to this field that clears when read (or when this field is written to 1 if<br>MAC_CSR_SW_Ctrl[RCWE]= 1). Also, the field automatically becomes 1 on an internal event occurrence.<br>0b - Not detected<br>1b - Detected|
|0<br>TSSOVF|Timestamp Seconds Overflow<br>Indicates whether the timestamp seconds overflow status is detected.<br>If this field is 1, it indicates that the seconds value of the timestamp (when supporting version 2 format) has<br>overflowed beyond 32'hFFFF_FFFF.<br>Access restrictions apply to this field that clears when read (or when this field is written to 1 if<br>MAC_CSR_SW_Ctrl[RCWE]= 1). Also, the field automatically becomes 1 on an internal event occurrence.<br>0b - Not detected<br>1b - Detected|



# 74.7.157 MAC Transmit Timestamp Status In Nanoseconds (MAC_Tx_Timestamp_Status_Nanoseconds) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Tx_Timestamp_St|B30h|
|atus_Nanoseconds||



## Function 

Contains the nanosecond part of the timestamp captured for tansmit packets when the transmit status is disabled. 

This register, along with MAC Transmit Timestamp Status In Seconds (MAC_Tx_Timestamp_Status_Seconds), gives the 64-bit timestamp captured for the PTP packet that MAC successfully transmits. The application considers reading this value after the last byte of this register is read. In Little-Endian mode, this means when bits [31:24] are read, and in Big-Endian mode, this means when bits [7:0] are read. 

If the application does not read these registers and the timestamp of another packet is captured, then either the current timestamp is lost (overwritten) or the new timestamp is lost (dropped), depending on the settings specified in MAC_Timestamp_Control[TXTSSTSM]. The status bit TXTSC bit [15] in the MAC_Timestamp_Status register is set whenever the MAC transmitter captures the timestamp. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3214 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|TXTSS<br>MIS||||||||TXTSSLO||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||TXTS|SLO||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31|Transmit Timestamp Status Missed|
|TXTSSMIS|Indicates whether the transmit timestamp missed status is detected.<br>If this field is 1, it indicates one of these conditions:<br>• The timestamp of the current packet is ignored ifMAC_Timestamp_Control[TXTSSTSM]= 0.<br>• The timestamp of the previous packet is overwritten with the timestamp of the current packet if<br>MAC_Timestamp_Control[TXTSSTSM]= 1.<br>Access restrictions apply to this field that cleas on read and automatically becomes 1 on an internal<br>event occurrence.|
||0b - Not detected<br>1b - Detected|
|30-0|Transmit Timestamp Status Low|
|TXTSSLO|Contains 31 bits of the Nanoseconds field of the transmit packet's captured timestamp.|



# 74.7.158 MAC Transmit Timestamp Status In Seconds (MAC_Tx_Timestamp_Status_Seconds) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Tx_Timestamp_St|B34h|
|atus_Seconds||



## Function 

Contains the higher 32 bits of the timestamp (in seconds) captured when a PTP packet is transmitted. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3215 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3216-01.png)


<!-- Start of picture text -->
Ethernet Media Access Controller (EMAC)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TXTSSHI<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TXTSSHI<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Diagram 

## Fields 

|Field|Function|
|---|---|
|31-0|Transmit Timestamp Status High|
|TXTSSHI|Contains the lower 32 bits of the Seconds field of the transmitted packet's captured timestamp.|



# 74.7.159 MAC Timestamp Ingress Asymmetry Correction (MAC_Timestamp_Ingress_Asym_Corr) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Timestamp_Ingres|B50h|
|s_Asym_Corr||



## Function 

Contains the ingress asymmetry correction value to be used when updating the correction field in the PDelay_Resp PTP messages. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||OST|IAC||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||OST|IAC||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3216 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0|One-Step Timestamp Ingress Asymmetry Correction|
|OSTIAC|Contains the ingress path asymmetry value to be added to the correctionField of the Pdelay_Resp<br>PTP packet.|
||The programmed value must be expressed in units of nanoseconds and multiplied by 2^16. For example,<br>2.5 ns is represented as 00028000h. This value can also be negative, which is represented in the<br>two's-complement form with bit 31 representing the sign bit.|



# 74.7.160 MAC Timestamp Egress Asymmetry Correction (MAC_Timestamp_Egress_Asym_Corr) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Timestamp_Egres|B54h|
|s_Asym_Corr||



## Function 

Contains the egress asymmetry correction value to be used when updating the correction field in the PDelay_Req PTP messages. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||OST|EAC||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||OST|EAC||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function|
|---|---|
|31-0|One-Step Timestamp Egress Asymmetry Correction|
|OSTEAC|Contains the egress path asymmetry value to be subtracted from the correctionField of the Pdelay_Resp<br>PTP packet. The programmed value must be the negated value in units of nanoseconds multiplied by 2^16.|
||For example, if the required correction is +2.5 ns, the programmed value must be FFFD_8000h, which is the<br>two's-complement of 0002_8000h (2.5 * 216). Similarly, if the required correction is -3.3 ns, the programmed<br>value is 0003_4CCCh (3.3 * 216).|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3217 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

# 74.7.161 MAC Timestamp Ingress Correction In Nanoseconds (MAC_Timestamp_Ingress_Corr_Nanosecond) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Timestamp_Ingres|B58h|
|s_Corr_Nanosecond||



## Function 

Contains the correction value, in nanoseconds, to be used with the captured timestamp value in the ingress path. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3218-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>TSIC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>TSIC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Timestamp Ingress Correction|
|TSIC|Contains the ingress path correction value as defined by the ingress correction expression.|



# 74.7.162 MAC Timestamp Egress Correction In Nanoseconds (MAC_Timestamp_Egress_Corr_Nanosecond) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Timestamp_Egres|B5Ch|
|s_Corr_Nanosecond||



## Function 

Contains the correction value, in nanoseconds, to be used with the captured timestamp value in the egress path. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3218 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3219-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>TSEC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>TSEC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Timestamp Egress Correction|
|TSEC|Contains the nanoseconds part of the egress path correction value as defined by the egress<br>correction expression.|



# 74.7.163 MAC Timestamp Ingress Correction In Subnanoseconds (MAC_Timestamp_Ingress_Corr_Subnanosec) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Timestamp_Ingres|B60h|
|s_Corr_Subnanosec||



## Function 

Contains the sub-nanosecond part of the correction value to be used with the captured timestamp value for ingress direction. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||Rese|rved||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||TSIC|SNS|||||||Rese|rved||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3219 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Fields 

|Field|Function|
|---|---|
|31-16|Reserved|
|—||
|15-8|Timestamp Ingress Correction In Sub-Nanoseconds|
|TSICSNS|Contains the sub-nanoseconds part of the ingress path correction value as defined by the Ingress<br>Correction expression.|
|7-0<br>—|Reserved|



# 74.7.164 MAC Timestamp Engress Correction In Subnanoseconds (MAC_Timestamp_Egress_Corr_Subnanosec) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Timestamp_Egres|B64h|
|s_Corr_Subnanosec||



## Function 

Contains the sub-nanosecond part of the correction value to be used with the captured timestamp value for the egress direction. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3220-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>TSECSNS  Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field<br>Function|
|---|
|31-16<br>Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3220 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|15-8|Timestamp Egress Correction In Sub-Nanoseconds|
|TSECSNS|Contains the sub-nanoseconds part of the egress path correction value, as defined by the Egress<br>Correction expression.|
|7-0<br>—|Reserved|



# 74.7.165 MAC Timestamp Ingress Latency (MAC_Timestamp_Ingress_Latency) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Timestamp_Ingres<br>s_Latency|B68h|



## Function 

Holds the ingress MAC latency. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3221-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R ITLNS<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R ITLSNS<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-28<br>—|Reserved|
|27-16|Ingress Timestamp Latency In Sub-Nanoseconds|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3221 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|ITLNS|Holds the average latency, in sub-nanoseconds, between the MAC input ports (phy_rxd_i) and the actual<br>point (GMII/MII), where the ingress timestamp is taken. The ingress correction value is computed as<br>described in section 7.1.2.4.1 of QoS Databook.|
|15-8|Ingress Timestamp Latency In Nanoseconds|
|ITLSNS|Holds the average latency, in nanoseconds, between the MAC input ports (phy_rxd_i) and the actual point<br>(GMII/MII), where the ingress timestamp is taken. The ingress correction value is computed as described<br>in section 7.1.2.4.1 of QoS Databook.|
|7-0<br>—|Reserved|



# 74.7.166 MAC Timestamp Egress Latecy (MAC_Timestamp_Egress_Latency) 

## Offset 

|Register|Offset|
|---|---|
|MAC_Timestamp_Egres<br>s_Latency|B6Ch|



## Function 

## Holds the egress MAC latency. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Rese|rved|||||||ETL|NS||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||ETL|SNS|||||||Rese|rved||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-28<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3222 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|27-16|Egress Timestamp Latency In Nanoseconds|
|ETLNS|Holds the average latency, in nanoseconds, between the actual point (GMII/MII) where the egress<br>timestamp is taken and the MAC output ports (phy_txd_o). The ingress correction value is computed as<br>described in section 7.1.2.4.2 of QoS Databook.|
|15-8|Egress Timestamp Latency In Sub-Nanoseconds|
|ETLSNS|Holds the average latency, in sub-nanoseconds, between the actual point (GMII/MII) where the egress<br>timestamp is taken and the MAC output ports (phy_txd_o). The ingress correction value is computed as<br>described in section 7.1.2.4.2 of QoS Databook.|
|7-0<br>—|Reserved|



# 74.7.167 MAC PPS Control (MAC_PPS_Control) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS_Control|B70h|



## Function 

Indicates PPS control. 

In this register: 

- Bits [30:24] are valid only when four flexible PPS outputs are selected. 

- Bits [22:16] are valid only when three or more flexible PPS outputs are selected. 

- Bits [14:8] are valid only when two or more flexible PPS outputs are selected. 

- Bits [6:4] are valid only when the flexible PPS feature is selected. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3223-15.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R MCGR TRGTMODSEL Reserv MCGR TRGTMODSEL Reserv<br>PPSCMD3  PPSCMD2<br>W EN3  3  ed  EN2  2  ed<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R MCGR TRGTMODSEL Reserv MCGR TRGTMODSEL PPSE<br>PPSCMD1  PPSCTRL_PPSCMD<br>W EN1  1  ed  EN0  0  N0<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3223 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Fields 

|Field|Function|
|---|---|
|31|MCGR Mode Enable For PPS3 Output|
|MCGREN3|Enables the third PPS instance to operate in PPS or MCGR mode. If this field is 1, it operates in MCGR<br>mode, and if the value is 0, it operates in PPS mode.|
|30-29|Target Time Register Mode For PPS3 Output|
|TRGTMODSEL<br>3|IndicatesMAC PPS3 Target Time In Seconds (MAC_PPS3_Target_Time_Seconds)andMAC PPS3 Target<br>Time In Nanoseconds (MAC_PPS3_Target_Time_Nanoseconds)mode for the PPS3 output signal.<br>00b - Target Time registers are programmed only for generating the interrupt event. The flexible<br>PPS function must not be enabled in this mode, otherwise spurious transitions may be observed<br>on the corresponding ptp_pps_o output port.<br>01b - Reserved<br>10b - Target Time registers are programmed for generating the interrupt event and starting or<br>stopping the PPS0 output signal generation.<br>11b - Target Time registers are programmed only for starting or stopping the PPS0 output signal<br>generation. No interrupt is asserted.|
|28<br>—|Reserved|
|27-24<br>PPSCMD3|Flexible PPS3 Output Control<br>Controls the flexible PPS3 output (ptp_pps_o[3]) signal. The functioning of this field is similar to that of<br>PPSCMD0[2:0] (presentation time control bits).<br>If MCGREN3 = 1, PPSCMD3 that includes bits [27:24] are considered as presentation time control bits for<br>media clock generation and recovery for comparator instance 3. If MCGREN3 is not 1, only three bits [26:24]<br>are considered as PPSCMD3 and the fourth bit becomes 0.<br>Access restrictions apply to this field that clears automatically. Writing 0 to it has no effect.|
|23<br>MCGREN2|MCGR Mode Enable For PPS2 Output<br>Enables or disables the second PPS instance to operate in PPS or MCGR mode. If this field is 1, it operates<br>in MCGR mode, and if the value is 0, it operates in PPS mode.<br>0b - Disabled<br>1b - Enabled|
|22-21|Target Time Register Mode For PPS2 Output|
|TRGTMODSEL<br>2|IndicatesMAC PPS2 Taget Time In Seconds (MAC_PPS2_Target_Time_Seconds)andMAC PPS2 Target<br>Time In Nanoseconds (MAC_PPS2_Target_Time_Nanoseconds)mode for the PPS2 output signal.<br>00b - Target Time registers are programmed only for generating the interrupt event. The flexible<br>PPS function must not be enabled in this mode, otherwise spurious transitions may be observed<br>on the corresponding ptp_pps_o output port.<br>01b - Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3224 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||10b - Target Time registers are programmed for generating the interrupt event and starting or<br>stopping the PPS0 output signal generation.<br>11b - Target Time registers are programmed only for starting or stopping the PPS0 output signal<br>generation. No interrupt is asserted.|
|20<br>—|Reserved|
|19-16<br>PPSCMD2|Flexible PPS2 Output Control<br>Controls the flexible PPS2 output (ptp_pps_o[2]) signal. The functioning of this field is similar to that of the<br>PPSCMD0 (presentation time control bits).<br>If MCGREN2 = 1, the bits included in PPSCMD2 [19:16] are considered as presentation time control bits for<br>media clock generation and recovery for comparator instance 2. If MCGREN2 is not 1, only three bits [18:16]<br>are used as PPSCMD2 and the fourth bit becomes 0.<br>Access restrictions apply to this field that clears automatically. Writing 0 to it has no effect.|
|15<br>MCGREN1|MCGR Mode Enable For PPS1 Output<br>Enables or disables the first PPS instance to operate in PPS or MCGR mode. If this field is 1, it operates in<br>MCGR mode, and if the value is 0, it operates in PPS mode.<br>0b - Disabled<br>1b - Enabled|
|14-13|Target Time Register Mode For PPS1 Output|
|TRGTMODSEL<br>1|IndicatesMAC PPS1 Target Time In Seconds (MAC_PPS1_Target_Time_Seconds)andMAC PPS1 Target<br>Time In Nanoseconds (MAC_PPS1_Target_Time_Nanoseconds)mode for the PPS1 output signal.<br>00b - Target Time registers are programmed only for generating the interrupt event. The flexible<br>PPS function must not be 1 in this mode, otherwise spurious transitions may be observed on the<br>corresponding ptp_pps_o output port.<br>01b - Reserved<br>10b - Target Time registers are programmed for generating the interrupt event and starting or<br>stopping the PPS0 output signal generation.<br>11b - Target Time registers are programmed only for starting or stopping the PPS0 output signal<br>generation. No interrupt is asserted.|
|12<br>—|Reserved|
|11-8<br>PPSCMD1|Flexible PPS1 Output Control<br>Controls the flexible PPS1 output (ptp_pps_o[1]) signal. The functioning of this field is similar to that of the<br>PPSCMD0 field.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3225 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function<br>If MCGREN1 = 1, the bits included in PPSCMD1 [11:8] are considered as presentation time control bits for<br>media clock generation and recovery for comparator instance 1. The functioning of PPSCMD1 is similar to<br>that of the PPSCMD0 presentation time control bits. If MCGREN1 is not 1, only three bits [10:8] are used<br>as PPSCMD1 and the fourth bit becomes 0.<br>Access restrictions apply to this field that clears automatically. Writing 0 to it has no effect.|
|---|---|
|7<br>MCGREN0|MCGR Mode Enable For PPS0 Output<br>Indictaes whether the 0th PPS instance is enabled to operate in PPS or MCGR mode. If this field is 1, it<br>operates in MCGR mode, and if the value is 0, it operates in PPS mode.<br>0b - PPS mode<br>1b - MCGR mode|
|6-5|Target Time Register Mode For PPS0 Output|
|TRGTMODSEL<br>0|IndicatesMAC PPS0 Target Time In Seconds (MAC_PPS0_Target_Time_Seconds)andMAC PPS0 Target<br>Time In Nanoseconds (MAC_PPS0_Target_Time_Nanoseconds)mode for the PPS0 output signal.<br>00b - Target Time registers are programmed only for generating the interrupt event. The flexible<br>PPS function must not be 1 in this mode, otherwise spurious transitions may be observed on the<br>corresponding ptp_pps_o output port.<br>01b - Reserved<br>10b - Target Time registers are programmed for generating the interrupt event and starting or<br>stopping the PPS0 output signal generation.<br>11b - Target Time registers are programmed only for starting or stopping the PPS0 output signal<br>generation. No interrupt is asserted.|
|4<br>PPSEN0|Flexible PPS Output Mode Enable 0<br>Indicates the status of Flexible PPS Output mode.<br>• If this field is 1, the PPSCTRL_PPSCMD field functions as PPSCMD.<br>• If this field is 0, the PPSCTRL_PPSCMD field functions as PPSCTRL (fixed PPS mode).<br>0b - Disabled<br>1b - Enabled|
|3-0|PPS Output Frequency Control|
|PPSCTRL_PPS<br>CMD|Controls the frequency of the PPS0 output (ptp_pps_o[0] signal). The default value of this field is 0, and the<br>PPS output is 1 pulse (of width clk_ptp_i) every second. For the other values of PPSCTRL, the PPS output<br>becomes a generated clock having these frequencies:<br>• 0001: The binary rollover is 2 Hz, and the digital rollover is 1 Hz.<br>• 0010: The binary rollover is 4 Hz, and the digital rollover is 2 Hz.<br>• 0011: The binary rollover is 8 Hz, and the digital rollover is 4 Hz.<br>• 0100: The binary rollover is 16 Hz, and the digital rollover is 8 Hz.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3226 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

- Field Function • .. • 1111: The binary rollover is 32.768 kHz and the digital rollover is 16.384 kHz. ~~<mark>NOTE</mark>~~ 

- In Binary Rollover mode, the PPS output (ptp_pps_o) has a duty cycle of 50 percent with these frequencies. In Digital Rollover mode, the PPS output frequency is an average number. The actual clock has a different frequency that is synchronized every second. 

- For example, • If PPSCTRL = 0001, PPS (1 Hz) has a low period of 537 ms and a high period of 463 ms. • If PPSCTRL = 0010, PPS (2 Hz) is a sequence of one clock of 50 percent duty cycle and a 537 ms period. The second clock has a period of 463 ms (268 ms low and 195 ms high). 

- • If PPSCTRL = 0011, PPS (4 Hz) is a sequence of three clocks of 50 percent duty cycle and a 268 ms period, and the fourth clock of 195 ms period (134 ms low and 61 ms high). 

- This behavior is a result of the non-linear toggling of bits in Digital Rollover mode in MAC System Time In Nanoseconds (MAC_System_Time_Nanoseconds) or flexible PPS output (ptp_pps_o[0]) control. Programming these bits with a non-zero value instructs MAC to initiate an event. When the command is transferred or synchronized with the PTP clock domain, these bits automatically become 0. You must ensure that these bits are programmed only when they are "all-zero." The following list describes the values of PPSCMD0. • 0000: No command • 0001: Start a single pulse. This command generates a single pulse rising at the start point defined in MAC PPS0 Target Time In Seconds (MAC_PPS0_Target_Time_Seconds) and MAC PPS0 Target Time In Nanoseconds (MAC_PPS0_Target_Time_Nanoseconds), for a duration defined in MAC PPS0 Width (MAC_PPS0_Width). 

- • 0010: Start pulse train. This command generates the train of pulses rising at the start point defined in the Target Time registers and for a duration defined in MAC PPS0 Width (MAC_PPS0_Width), repeated at an interval defined in the PPS Interval registers. By default, the PPS pulse train runs freely unless the "stop pulse train at time" or "stop pulse train immediately" command stops it. 

- • 0011: Cancel start. This command cancels the start single pulse and start pulse train commands if the system time has not crossed the programmed start time. 

- • 0100: Stop pulse train at time. This command stops the train of pulses that the start pulse train command (PPSCMD = 0010) initiates after the time programmed in the Target Time registers elapses. 

- • 0101: Stop pulse train immediately. This command immediately stops the train of pulses that the start pulse train command (PPSCMD = 0010) initiates. 

- • 110: Cancel stop pulse train. This command cancels the stop pulse train at the time command if the programmed stop time has not elapsed. The PPS pulse train runs freely if the command executes successfully. 

- • 0111-1111: Reserved or presentation time control. If MAC_PPS_Control[MCGREN0] = 0, then these are treated as presentation time control bits. 

- This list describes the values of PPSCMD0: 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3227 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||• 0000: The MCGR operation is not carried out. If set to this value in the mid of clock recovery or<br>generation, all the processing inputs are flushed.<br>• 0001: Captures the presentation time at the rising edge of mcg_pst_trig_i[0] inMAC PPS0 Target<br>Time In Seconds (MAC_PPS0_Target_Time_Seconds)<br>• 0010: Captures the presentation time at the falling edge of mcg_pst_trig_i[0] inMAC PPS0 Target<br>Time In Seconds (MAC_PPS0_Target_Time_Seconds)<br>• 0011: Captures the presentation time at both the edges of mcg_pst_trig_i[0] inMAC PPS0 Target<br>Time In Seconds (MAC_PPS0_Target_Time_Seconds)<br>• 0100-1000: Reserved<br>• 1001: Toggle output on compare|
||• 1010: Pulse output low on compare for one PTP-clock cycle<br>• 1011: Pulse output high on compare for one PTP-clock cycle<br>• 1100-1111: Reserved|



# 74.7.168 MAC PPS0 Target Time In Seconds (MAC_PPS0_Target_Time_Seconds) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS0_Target_Tim|B80h|
|e_Seconds||



## Function 

Is used, along with the PPS Target Time Nanoseconds register, to schedule an interrupt event (MAC_Timestamp_Status[TSTARGT0]) when the system time exceeds the value programmed in these registers. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||TST|RH0||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||TST|RH0||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3228 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0|PPS Target Time In Seconds Register|
|TSTRH0|Stores the target time in seconds. When the timestamp value matches or exceeds both the Target<br>Timestamp registers, MAC starts or stops the PPS signal output and generates an interrupt (if<br>enabled), based on Target Time mode selected for the corresponding PPS output inMAC PPS<br>Control (MAC_PPS_Control).<br>If DWC_EQOS_FLEXI_PPS_OUT_EN is enabled in the configuration and<br>MAC_Timestamp_Control[PTGE]= 1, with the presentation time control set in Recovery mode, these<br>fields indicate that the application programs the TPT. In Generation mode, it indicates thatCPTis generated<br>at the sampled trigger.|



# 74.7.169 MAC PPS0 Target Time In Nanoseconds (MAC_PPS0_Target_Time_Nanoseconds) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS0_Target_Tim|B84h|
|e_Nanoseconds||



## Function 

Indicates the target time in nanoseconds for PPS0. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|TRGT<br>BUS...||||||||TTSL0||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||TT|SL0||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31|PPS Target Time Busy Status 0|
|TRGTBUSY0|Indicates whether the PPS target time busy status 0 is detected.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3229 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||• MAC writes 1 to this field whenMAC_PPS_Control[PPSCTRL_PPSCMD]is programmed to 010 or<br>011. This instructs MAC to synchronize the Target Time registers with the PTP clock domain.<br>• MAC writes 0 to this field after synchronizing the Target Time registers with the PTP clock domain.<br>The application must not update the Target Time registers when this field is read as 1. Otherwise,<br>the synchronization of the previously programmed time is corrupted.<br>0b - Not detected<br>1b - Detected|
|30-0<br>TTSL0|Target Time Low For PPS0<br>Stores the time in (signed) nanoseconds.<br>If the value of the timestamp matches the value in both the Target Timestamp registers,<br>MAC starts or stops the PPS signal output and generates an interrupt, if enabled, based<br>onMAC_PPS_Control[TRGTMODSEL0].<br>• IfMAC_Timestamp_Control[TSCTRLSSR]= 0, this value must be calculated as (time in ns / 0.465).<br>The actual start or stop time of the PPS signal output might have an error margin up to one unit of<br>the sub-second increment value.<br>• IfMAC_Timestamp_Control[TSCTRLSSR]= 1, this value must not exceed 3B9A_C9FFh. The actual<br>start or stop time of the PPS signal output might have an error margin up to one unit of the<br>sub-second increment value.<br>Access restriction apply to this field that clears automatically. Writing 0 to it has no effect.|



# 74.7.170 MAC PPS0 Interval (MAC_PPS0_Interval) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS0_Interval|B88h|



## Function 

Contains the number of units of the sub-second increment value between the rising edges of the PPS0 signal output (ptp_pps_o[0]). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3230 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3231-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>PPSINT0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>PPSINT0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|PPS Output Signal Interval 0|
|PPSINT0|Stores the interval between the rising edges of the PPS0 signal output. The interval is stored in terms of the<br>number of units of the sub-second increment value.|
||You must program one value less than the required interval. For example, if the PTP reference clock is 50<br>MHz (period of 20 ns), and the desired interval between the rising edges of the PPS0 signal output is 100<br>ns (that is, five units of the sub-second increment value), you must program value 4 (5-1) in this register.|



# 74.7.171 MAC PPS0 Width (MAC_PPS0_Width) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS0_Width|B8Ch|



## Function 

Contains the number of units of the sub-second increment value between the rising and corresponding falling edges of the PPS0 signal output (ptp_pps_o[0]). 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3231-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>PPSWIDTH0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>PPSWIDTH0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3231 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0|PPS Output Signal Width 0|
|PPSWIDTH0|Stores the width between the rising and corresponding falling edges of the PPS0 signal output. The width<br>is stored in terms of the number of units of the sub-second increment value.|
||You must program one value less than the required interval. For example, if the PTP reference clock has a<br>frequency of 50 MHz (period of 20 ns), and a width between the rising and corresponding falling edges of<br>the PPS0 signal output is 80 ns (that is, four units of the sub-second increment value), you should program<br>value 3 (4-1) in this register.|
||The value programmed in this register must be lesser than the value programmed inMAC<br>PPS0 Interval (MAC_PPS0_Interval).<br>~~NOTE~~|



# 74.7.172 MAC PPS1 Target Time In Seconds (MAC_PPS1_Target_Time_Seconds) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS1_Target_Tim|B90h|
|e_Seconds||



## Function 

Is used to schedule an interrupt event (MAC_Timestamp_Status[TSTARGT0]), along with the PPS Target Time Nanoseconds register, when the system time exceeds the value programmed in these registers. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||TST|RH1||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||TST|RH1||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function|
|---|---|
|31-0|PPS Target Time In Seconds 1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3232 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

|Field|Function|
|---|---|
|TSTRH1|Stores the target time in seconds.|
||When the timestamp value matches or exceeds both the Target Timestamp registers, MAC starts or stops<br>the PPS signal output and generates an interrupt, if enabled, based on Target Time mode selected for the<br>corresponding PPS output inMAC PPS Control (MAC_PPS_Control).<br>If DWC_EQOS_FLEXI_PPS_OUT_EN is enabled in the configuration and<br>MAC_Timestamp_Control[PTGE]= 1, with the presentation time control set in Recovery mode, these<br>fields indicate that the application programs the TPT. In Generation mode, it indicates that CPT is generated<br>at the sampled trigger.|



# 74.7.173 MAC PPS1 Target Time In Nanoseconds (MAC_PPS1_Target_Time_Nanoseconds) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS1_Target_Tim|B94h|
|e_Nanoseconds||



## Function 

Indicates the target time in nanoseconds for PPS1. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|TRGT<br>BUS...||||||||TTSL1||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||TT|SL1||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31|PPS Target Time Busy Status 1|
|TRGTBUSY1|Indicates whether the PPS target time busy status 1 is detected.|
||• MAC writes 1 to this field whenMAC_PPS_Control[PPSCTRL_PPSCMD]is programmed to 010 or<br>011. Programming the PPSCMD0 field as 010 or 011 instructs MAC to synchronize the Target Time<br>registers with the PTP clock domain.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3233 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||• MAC writes 0 to this field after synchronizing the Target Time registers with the PTP clock domain.<br>The application must not update the Target Time registers when this field is read as 1. Otherwise,<br>the synchronization of the previously programmed time is corrupted.<br>0b - Not detected<br>1b - Detected|
|30-0<br>TTSL1|Target Time Low For PPS1<br>Stores the time in (signed) nanoseconds.<br>If the value of the timestamp matches the value in both the Target Timestamp registers,<br>MAC starts or stops the PPS signal output and generates an interrupt, if enabled, based<br>onMAC_PPS_Control[TRGTMODSEL0].<br>• IfMAC_Timestamp_Control[TSCTRLSSR]= 0, this value must be defined as (time in ns / 0.465).<br>The actual start or stop time of the PPS signal output might have an error margin up to one unit of<br>the sub-second increment value.<br>• IfMAC_Timestamp_Control[TSCTRLSSR]= 1, this value must not exceed 3B9A_C9FFh. The actual<br>start or stop time of the PPS signal output might have an error margin up to one unit of the<br>sub-second increment value.<br>Access restriction apply to this field that clears automatically. Writing 0 to it has no effect.|



# 74.7.174 MAC PPS1 Interval (MAC_PPS1_Interval) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS1_Interval|B98h|



## Function 

Contains the number of units of the sub-second increment value between the rising edges of the PPS0 signal output (ptp_pps_o[0]). 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3234-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>PPSINT1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>PPSINT1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3234 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Fields 

|Field|Function|
|---|---|
|31-0|PPS Output Signal Interval 1|
|PPSINT1|Stores the interval between the rising edges of the PPS0 signal output. The interval is stored in terms of the<br>number of units of the sub-second increment value.|
||You must program one value less than the required interval. For example, if the PTP reference clock is 50<br>MHz (period of 20 ns), and the desired interval between the rising edges of the PPS0 signal output is 100<br>ns (that is, five units of the sub-second increment value), you must program value 4 (5-1) in this register.|



# 74.7.175 MAC PPS1 Width (MAC_PPS1_Width) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS1_Width|B9Ch|



## Function 

Contains the number of units of the sub-second increment value between the rising and corresponding falling edges of the PPS0 signal output (ptp_pps_o[0]). 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||PPSWI|DTH1||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||PPSWI|DTH1||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|PPS Output Signal Width 1|
|PPSWIDTH1|Stores the width between the rising and corresponding falling edges of the PPS0 signal output. The width<br>is stored in terms of the number of units of the sub-second increment value.|
||You must program one value less than the required interval. For example, if the PTP reference clock has a<br>frequency of 50 MHz (period of 20 ns), and a width between the rising and corresponding falling edges of<br>the PPS0 signal output is 80 ns (that is, four units of the sub-second increment value), you should program<br>value 3 (4-1) in this register.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3235 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

|Field|Function||
|---|---|---|
|||~~NOTE~~|
|||The value programmed in this register must be lesser than the value programmed inMAC|
|||PPS0 Interval (MAC_PPS0_Interval).|



# 74.7.176 MAC PPS2 Taget Time In Seconds (MAC_PPS2_Target_Time_Seconds) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS2_Target_Tim<br>e_Seconds|BA0h|



## Function 

Is used to schedule an interrupt event (MAC_Timestamp_Status[TSTARGT0]), along with the PPS Target Time Nanoseconds register, when the system time exceeds the value programmed in these registers. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3236-09.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>TSTRH2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>TSTRH2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|PPS Target Time In Seconds 2|
|TSTRH2|Stores the target time in seconds.|
||When the timestamp value matches or exceeds both the Target Timestamp registers, MAC starts or stops<br>the PPS signal output and generates an interrupt, if enabled, based on Target Time mode selected for the<br>corresponding PPS output inMAC PPS Control (MAC_PPS_Control).<br>If DWC_EQOS_FLEXI_PPS_OUT_EN is enabled in the configuration and<br>MAC_Timestamp_Control[PTGE]= 1, with the presentation time control set in Recovery mode, these<br>fields indicate that the application programs the TPT. In Generation mode, it indicates that CPT is generated<br>at the sampled trigger.|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3236 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

# 74.7.177 MAC PPS2 Target Time In Nanoseconds (MAC_PPS2_Target_Time_Nanoseconds) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS2_Target_Tim|BA4h|
|e_Nanoseconds||



## Function 

Indicates the target time in nanoseconds for PPS2. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|TRGT<br>BUS...||||||||TTSL2||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||TT|SL2||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31|PPS Target Time Busy Status 2|
|TRGTBUSY2|Indicates whether the PPS target time busy status 2 is detected.<br>• MAC writes 1 to this field whenMAC_PPS_Control[PPSCTRL_PPSCMD]is programmed to 010 or<br>011. This instructs MAC to synchronize the Target Time registers with the PTP clock domain.<br>• MAC writes 0 to this field after synchronizing the Target Time registers with the PTP clock domain.<br>The application must not update the Target Time registers when this field is read as 1. Otherwise,<br>the synchronization of the previously programmed time is corrupted.<br>0b - Not detected<br>1b - Detected|
|30-0<br>TTSL2|Target Time Low For PPS2<br>Stores the time in (signed) nanoseconds.<br>If the value of the timestamp matches the value in both the Target Timestamp registers,<br>MAC starts or stops the PPS signal output and generates an interrupt, if enabled, based<br>onMAC_PPS_Control[TRGTMODSEL0].|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3237 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

- Field Function • If MAC_Timestamp_Control[TSCTRLSSR] = 0, this value must be defined as (time in ns / 0.465). The actual start or stop time of the PPS signal output might have an error margin up to one unit of the sub-second increment value. 

- • If MAC_Timestamp_Control[TSCTRLSSR] = 1, this value must not exceed 3B9A_C9FFh. The actual start or stop time of the PPS signal output might have an error margin up to one unit of the sub-second increment value. 

- Access restriction apply to this field that clears automatically. Writing 0 to it has no effect. 

# 74.7.178 MAC PPS2 Interval (MAC_PPS2_Interval) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS2_Interval|BA8h|



## Function 

Contains the number of units of the sub-second increment value between the rising edges of the PPS0 signal output (ptp_pps_o[0]). 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||PPS|INT2||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||PPS|INT2||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-0|PPS Output Signal Interval 2|
|PPSINT2|Stores the interval between the rising edges of the PPS0 signal output. The interval is stored in terms of the<br>number of units of the sub-second increment value.|
||You must program one value less than the required interval. For example, if the PTP reference clock is 50<br>MHz (period of 20 ns), and the desired interval between the rising edges of the PPS0 signal output is 100<br>ns (that is, five units of the sub-second increment value), you must program value 4 (5-1) in this register.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3238 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

# 74.7.179 MAC PPS2 Width (MAC_PPS2_Width) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS2_Width|BACh|



## Function 

Contains the number of units of the sub-second increment value between the rising and corresponding falling edges of the PPS0 signal output (ptp_pps_o[0]). 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3239-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>PPSWIDTH2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>PPSWIDTH2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|PPS Output Signal Width 2|
|PPSWIDTH2|Stores the width between the rising and corresponding falling edges of the PPS0 signal output. The width<br>is stored in terms of the number of units of the sub-second increment value.|
||You must program one value less than the required interval. For example, if the PTP reference clock has a<br>frequency of 50 MHz (period of 20 ns), and a width between the rising and corresponding falling edges of<br>the PPS0 signal output is 80 ns (that is, four units of the sub-second increment value), you should program<br>value 3 (4-1) in this register.|
||The value programmed in this register must be lesser than the value programmed inMAC<br>PPS0 Interval (MAC_PPS0_Interval).<br>~~NOTE~~|



# 74.7.180 MAC PPS3 Target Time In Seconds (MAC_PPS3_Target_Time_Seconds) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS3_Target_Tim|BB0h|
|e_Seconds||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3239 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Function 

Is used to schedule an interrupt event (MAC_Timestamp_Status[TSTARGT0]), along with the PPS Target Time Nanoseconds register, when the system time exceeds the value programmed in these registers. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3240-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>TSTRH3<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>TSTRH3<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|PPS Target Time In Seconds 3|
|TSTRH3|Stores the target time in seconds.|
||When the timestamp value matches or exceeds both the Target Timestamp registers, MAC starts or stops<br>the PPS signal output and generates an interrupt, if enabled, based on Target Time mode selected for the<br>corresponding PPS output inMAC PPS Control (MAC_PPS_Control).<br>If DWC_EQOS_FLEXI_PPS_OUT_EN is enabled in the configuration and<br>MAC_Timestamp_Control[PTGE]= 1, with the presentation time control set in Recovery mode, these<br>fields indicate that the application programs the TPT. In Generation mode, it indicates that CPT is generated<br>at the sampled trigger.|



# 74.7.181 MAC PPS3 Target Time In Nanoseconds (MAC_PPS3_Target_Time_Nanoseconds) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS3_Target_Tim|BB4h|
|e_Nanoseconds||



## Function 

Indicates the target time in nanoseconds for PPS3. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3240 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|TRGT<br>BUS...||||||||TTSL3||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||TT|SL3||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31<br>TRGTBUSY3|PPS Target Time Register Busy 3<br>Indicates whether the PPS target time register busy status is detected.<br>MAC writes 1 to this field whenMAC_PPS_Control[PPSCTRL_PPSCMD]is programmed to 010 or 011.<br>This instructs MAC to synchronize the Target Time registers with the PTP clock domain.<br>MAC writes 0 to this field after synchronizing the Target Time registers with the PTP clock domain.<br>The application must not update the Target Time registers when this field is read as 1. Otherwise, the<br>synchronization of the previously programmed time is corrupted.<br>0b - Not detected<br>1b - Detected|
|30-0<br>TTSL3|Target Time Low For PPS3<br>Stores the time in (signed) nanoseconds.<br>If the value of the timestamp matches the value in both the Target Timestamp registers,<br>MAC starts or stops the PPS signal output and generates an interrupt, if enabled, based<br>onMAC_PPS_Control[TRGTMODSEL0].<br>• IfMAC_Timestamp_Control[TSCTRLSSR]= 0, this value must be defined as (time in ns / 0.465).<br>The actual start or stop time of the PPS signal output might have an error margin up to one unit of<br>the sub-second increment value.<br>• IfMAC_Timestamp_Control[TSCTRLSSR]= 1, this value must not exceed 3B9A_C9FFh. The actual<br>start or stop time of the PPS signal output might have an error margin up to one unit of the<br>sub-second increment value.<br>Access restriction apply to this field that clears automatically. Writing 0 to it has no effect.|



# 74.7.182 MAC PPS3 Interval (MAC_PPS3_Interval) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS3_Interval|BB8h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3241 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Function 

Contains the number of units of the sub-second increment value between the rising edges of the PPS0 signal output (ptp_pps_o[0]). 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3242-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>PPSINT3<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>PPSINT3<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|PPS Output Signal Interval|
|PPSINT3|Stores the interval between the rising edges of the PPS0 signal output. The interval is stored in terms of the<br>number of units of the sub-second increment value.|
||You must program one value less than the required interval. For example, if the PTP reference clock is 50<br>MHz (period of 20 ns), and the desired interval between the rising edges of the PPS0 signal output is 100<br>ns (that is, five units of the sub-second increment value), you must program value 4 (5-1) in this register.|



# 74.7.183 MAC PPS3 Width (MAC_PPS3_Width) 

## Offset 

|Register|Offset|
|---|---|
|MAC_PPS3_Width|BBCh|



## Function 

Contains the number of units of the sub-second increment value between the rising and corresponding falling edges of the PPS0 signal output (ptp_pps_o[0]). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3242 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3243-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>PPSWIDTH3<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>PPSWIDTH3<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|PPS Output Signal Width 3|
|PPSWIDTH3|Stores the width between the rising and corresponding falling edges of the PPS0 signal output. The width<br>is stored in terms of the number of units of the sub-second increment value.|
||You must program one value less than the required interval. For example, if the PTP reference clock has a<br>frequency of 50 MHz (period of 20 ns), and a width between the rising and corresponding falling edges of<br>the PPS0 signal output is 80 ns (that is, four units of the sub-second increment value), you should program<br>value 3 (4-1) in this register.|
||The value programmed in this register must be lesser than the value programmed inMAC<br>PPS0 Interval (MAC_PPS0_Interval).<br>~~NOTE~~|



# 74.7.184 MTL Operation Mode (MTL_Operation_Mode) 

## Offset 

|Register|Offset|
|---|---|
|MTL_Operation_Mode|C00h|



## Function 

Establishes the transmit and receive operating modes and commands. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3243 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3244-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R CNTC CNTP Reserv DTXS Reserv<br>FRPE  Reserved  SCHALG  Reserved  RAA<br>W LR  RST  ed  TS  ed<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-16|Reserved|
|—||
|15<br>FRPE|Flexible Receive Parser Enable<br>Indicates the status of the flexible receive parser.<br>• If this field is 1, the programmable receive parser functionality is enabled.<br>• If the receive parser is disabled and is in the middle of parsing, the receive parser functionality is<br>disabled only after completing the current packet parsing.<br>When the receive parser is enabled from the disabled state, the receive parser is activated for the next<br>immediate packet.<br>0b - Disabled|
||1b - Enabled|
|14-10<br>—|Reserved|
|9<br>CNTCLR|Counters Reset<br>Indicates whether the counters are reset.<br>• If this field is 1, all the counters are reset. The field cleares automatically after one clock cycle.<br>• If you write 1 to this field along with the CNTPRST field, the CNT_PRESET field takes precedence.<br>Access restrictions apply to this field that clears automatically. Writing 0 to it has no effect.<br>0b - Not reset<br>1b - Reset|
|8|Counters Preset|
|CNTPRST|Indicates the status of preset counters.<br>If this field is 1,|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3244 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function<br>• MTL Tx Queue 0 Underflow (MTL_TxQ0_Underflow)[bits 0-7] is initialized or preset to 12'h7F0.<br>• Missed packet and overflow packet counters inMTL Rx Queue Missed Packet Overflow Count<br>(MTL_RxQ0_Missed_Packet_Overflow_Cnt)[bits 0-7] are initialized or preset to 12'h7F0.<br>Access restrictions apply to this field that clears automatically. Writing 0 to it has no effect.<br>0b - Disabled<br>1b - Enabled|
|---|---|
|7<br>—|Reserved|
|6-5<br>SCHALG|Transmit Scheduling Algorithm<br>Indicates the algorithm for transmit scheduling.<br>00b - WRR algorithm<br>01b - WFQ algorithm when DCB feature selected; otherwise, reserved<br>10b - DWRR algorithm when DCB feature selected; otherwise, reserved<br>11b - Strict priority algorithm|
|4-3<br>—<br>2<br>RAA|Reserved<br>Receive Arbitration Algorithm<br>Is used to select the arbitration algorithm for the receive side. Queue 0 has the lowest priority and the last<br>queue has the highest priority.<br>0b - Strict priority (SP)<br>1b - Weighted strict priority (WSP)|
|1<br>DTXSTS|Drop Transmit Status<br>Indicates whether the drop transmit status is enabled.<br>• If this field is 1, the transmit packet status received from MAC is dropped in MTL.<br>• If this field is 0, the transmit packet status received from MAC is forwarded to the application.<br>0b - Disabled<br>1b - Enabled|
|0<br>—|Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3245 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

# 74.7.185 MTL Debug Control (MTL_DBG_CTL) 

## Offset 

|Register|Offset|
|---|---|
|MTL_DBG_CTL|C08h|



## Function 

Controls, along with MTL Debug Status (MTL_DBG_STS), the operation mode of FIFO debug access. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||||||Reserved|||||||EI|EC|EIEE|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|STSIE|PKTIE|FIFO|SEL|FIFOW<br>REN|FIFOR<br>DEN|RSTS<br>EL|RSTAL<br>L|Reserv<br>ed|PKTS|TATE|Reserv<br>ed|BYT|EEN|DBGM<br>OD|FDBG<br>EN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-19|Reserved|
|—||
|18-17|ECC Inject Error Control|
|EIEC|Indicates the status of the ECC inject error control feature for transmit, receive, and TSO memories.<br>If EIEE = 1, following are the errors inserted based on the value encoded in this field.<br>00b - 1-bit error|
||01b - 2-bit errors<br>10b - 3-bit errors|
||11b - 1-bit error in the address field|
|16|ECC Inject Error Enable|
|EIEE|Indicates the status of the ECC error injection feature for transmit, receive, and TSO memories.<br>• If the value if this field is 1, it enables the ECC error injection feature.<br>• If the value if this field is 0, it disables the ECC error injection feature.<br>0b - Disabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3246 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Field|Function<br>1b - Enabled|
|---|---|
|15<br>STSIE|Transmit Status Available Interrupt Status Enable<br>Indicates whether the transmit packet available interrupt status is enabled.<br>If this field is 1, an interrupt is generated when transmit status is available in Slave mode.<br>0b - Disabled<br>1b - Enabled|
|14<br>PKTIE|Receive Packet Available Interrupt Status Enable<br>Indicates whether the receive packet available interrupt status is enabled.<br>If this field is 1, an interrupt is generated when EOP of the received packet is written to the receive FIFO.<br>0b - Disabled<br>1b - Enabled|
|13-12|FIFO Selected for Access|
|FIFOSEL|Indicates the FIFO selected for debug access.<br>00b - Transmit FIFO<br>01b - Transmit status FIFO (only read access when SLVMOD is set)<br>10b - TSO FIFO (cannot be accessed when SLVMOD is set)<br>11b - Receive FIFO|
|11<br>FIFOWREN|FIFO Write Enable<br>Indicates the status of FIFO write.<br>If this field is 1, it enables the write operation on the selected FIFO when FIFO debug access is enabled.<br>This field must not be written to 1 when FIFO debug access is disabled, that is, when FDBGEN = 0.<br>Access restrictions apply to this field that clears automatically. Also, writing 0 to the field clears it and writing<br>1 sets it.<br>0b - Disabled<br>1b - Enabled|
|10<br>FIFORDEN|FIFO Read Enable<br>Indicates the status of FIFO read.<br>If this field is 1, it enables the read operation on the selected FIFO when FIFO debug access is enabled.<br>This field must not be written to 1 when FIFO debug access is disabled, that is, when FDBGEN = 0.<br>Access restrictions apply to this field that clears automatically. Also, writing 0 to the field clears it and writing<br>1 sets it.<br>0b - Disabled<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3247 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function<br>1b - Enabled|
|---|---|
|9<br>RSTSEL|Reset Pointers Of Selected FIFO<br>Indicates whether the resetting of pointers for the selected FIFO is enabled.<br>If this field is 1, the pointers of the currently selected FIFO are reset when FIFO debug access is enabled.<br>This field must not be written to 1 when FIFO debug access is disabled, that is, when FDBGEN = 0.<br>Access restrictions apply to this field that clears automatically. Also, writing 0 to the field clears it and writing<br>1 sets it.<br>0b - Disabled<br>1b - Enabled|
|8<br>RSTALL|Reset All Pointers<br>Indicates whether the resetting of all the pointers is enabled.<br>If this field is 1, the pointers of all the FIFOs are reset when the FIFO debug access is enabled.<br>This field must not be written to 1 when FIFO debug access is disabled, that is, when FDBGEN = 0.<br>Access restrictions apply to this field that clears automatically. Also, writing 0 to the field clears it and writing<br>1 sets it.<br>0b - Disabled<br>1b - Enabled|
|7<br>—|Reserved|
|6-5<br>PKTSTATE|Encoded Packet State<br>Is used to write the control information to the transmit FIFO or receive FIFO.<br>These are the values related to the transmit FIFO:<br>• 00: Packet data<br>• 01: Control word<br>• 10: SOP data<br>• 11: EOP data<br>These are the values related to the receive FIFO:<br>• 00: Packet data<br>• 01: Normal status<br>• 10: Last status<br>• 11: EOP<br>00b - Packet data|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3248 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||01b - Control word/normal status<br>10b - SOP data/last status<br>11b - EOP data/EOP|
|4<br>—|Reserved|
|3-2<br>BYTEEN|Byte Enables<br>Indicates the number of data bytes valid in the data register during a write operation. This is valid only when<br>MTL_DBG_STS[PKTSTATE]is 2'b10 (EOP), and the transmit FIFO or receive FIFO is selected.<br>00b - Byte 0 valid<br>01b - Byte 0 and byte 1 valid<br>10b - Byte 0, byte 1, and byte 2 valid<br>11b - All four bytes valid|
|1|Debug Mode Access to FIFO|
|DBGMOD|Indicates the status of Debug mode access to FIFO.<br>If this field is 1, it indicates that the current access to FIFO is read, write, and debug. In this mode, the<br>following access types are allowed:<br>• Read and write access to transmit FIFO, TSO FIFO, and receive FIFO<br>• Read access to transmit status FIFO<br>If this field is 0, it indicates that the current access to FIFO is slave access bypassing DMA. In this mode,<br>the following access types are allowed:<br>• Write access to transmit FIFO<br>• Read access to receive FIFO and transmit status FIFO<br>0b - Disabled<br>1b - Enabled|
|0<br>FDBGEN|FIFO Debug Access Enable<br>Indicates the status of FIFO debug access.<br>• If this field is 1, it indicates that the FIFO debug mode access is enabled.<br>• If the value of the field is 0, it indicates that FIFO can be accessed only through a master interface.<br>0b - Disabled<br>1b - Enabled|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3249 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

# 74.7.186 MTL Debug Status (MTL_DBG_STS) 

## Offset 

|Register|Offset|
|---|---|
|MTL_DBG_STS|C0Ch|



## Function 

Contains the status of FIFO debug access. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3250-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R LOCR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>FIFOB<br>R LOCR  BYTEEN  PKTSTATE<br>Reserved  STSI  PKTI  Reserved  USY<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-15|Remaining Locations In FIFO|
|LOCR|Indicates the remaining locations in FIFO. For Slave Access mode, the field indicates the space available<br>in the selected FIFO, and for Debug Access mode, this field contains the write or read pointer value of the<br>selected FIFO during the write or read operation, respectively.<br>Reset: In single transmit queue configurations, (DWC_EQOS_TXFIFO_SIZE/(DWC_EQOS_DATAWIDTH/<br>8)), otherwise 0000h.|
|14-10|Reserved|
|—||
|9|Transmit Status Available Interrupt Status|
|STSI|Indicates whether the transmit status available interrupt status is detected.<br>If this field is 1, it indicates that Slave mode transmit packet is transmitted, and the status is available in<br>transmit status FIFO. The field resets when you write 1 to it.<br>0b - Not detected|
||1b - Detected|
|8|Receive Packet Available Interrupt Status|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3250 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|PKTI|Indicates whether the receive packet available interrupt status is detected.<br>If this field is 1, it indicates that the MAC layer has written the EOP of the received packet to the receive FIFO.<br>The field resets when you write 1 to it.<br>0b - Not detected<br>1b - Detected|
|7-5<br>—|Reserved|
|4-3<br>BYTEEN|Byte Enables<br>Indicates the number of data bytes valid in the data register during a read operation. This is valid only when<br>MTL_DBG_STS[PKTSTATE]is 2'b10 (EOP), and the transmit FIFO or receive FIFO is selected.<br>00b - Byte 0 valid<br>01b - Byte 0 and byte 1 valid<br>10b - Byte 0, byte 1, and byte 2 valid<br>11b - All four bytes valid|
|2-1<br>PKTSTATE|Encoded Packet State<br>Is used to get the control or status information of the selected FIFO.<br>These are the values related to the transmit FIFO.<br>• 00: Packet data<br>• 01: Control word<br>• 10: SOP data<br>• 11: EOP data<br>These are the values related to the receive FIFO.<br>• 00: Packet data<br>• 01: Normal status<br>• 10: Last status<br>• 11: EOP<br>This field is applicable only for transmit and receive FIFOs during a read operation.<br>00b - Packet data<br>01b - Control word/normal status<br>10b - SOP data/last status<br>11b - EOP data/EOP|
|0|FIFO Busy|
|FIFOBUSY|Indicates whether the FIFO busy status is detected.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3251 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||If this field is 1, it indicates that a FIFO operation is in progress in MAC and the content of the following<br>is invalid:|
||• All other fields of this register|
||• All the fields ofMTL FIFO Debug Data (MTL_FIFO_Debug_Data)|
||0b - Not detected|
||1b - Detected|



# 74.7.187 MTL FIFO Debug Data (MTL_FIFO_Debug_Data) 

## Offset 

|Register|Offset|
|---|---|
|MTL_FIFO_Debug_Data|C10h|



## Function 

Contains the data to be written to or read from the FIFOs. 

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
|31-0|FIFO Debug Data|
|FDBGDATA|Contains the data to be written to the transmit FIFO, receive FIFO, or TSO FIFO during a debug or slave<br>access write operations. The field contains the data read from the transmit FIFO, receive FIFO, TSO FIFO,<br>or transmit status FIFO during debug or slave access read operations.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3252 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

# 74.7.188 MTL Interrupt Status (MTL_Interrupt_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_Interrupt_Status|C20h|



## Function 

Determines the interrupt status of MAC and MTL queues. The software driver (application) reads this register during an interrupt service routine or polling to perform this function. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3253-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>MTLPI<br>R S  ESTIS  DBGIS Reserv<br>Reserved  Reserved<br>ed<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserv Reserv Reserv Reserv Reserv Reserv Q1IS  Q0IS<br>Reserved<br>W ed  ed  ed  ed  ed  ed<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-24|Reserved|
|—||
|23|MTL Receive Parser Interrupt Status|
|MTLPIS|Indicates whether the MTL receive parser interrupt status is detected.<br>This field indicates an interrupt from the receive parser block. To reset this field, the application must read<br>MTL Rx Parser Interrupt Control Status (MTL_RXP_Interrupt_Control_Status)to get the exact cause of the<br>interrupt and clear its source.<br>0b - Not detected|
||1b - Detected|
|22-19<br>—|Reserved|
|18|EST (TAS- 802.1Qbv) Interrupt Status|
|ESTIS|Indicates whether the EST (TAS- 802.1Qbv) interrupt status is detected.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3253 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function<br>This field indicates an interrupt event during the operation of 802.1Qbv. To reset the field, the application<br>must clear the error or event that caused the interrupt.<br>0b - Not detected<br>1b - Detected|
|---|---|
|17<br>DBGIS|Debug Interrupt Status<br>Indicates whether the debug interrupt status is detected.<br>This field indicates an interrupt event during the slave access. To reset the field, the application must read<br>MTL Debug Status (MTL_DBG_STS)to get the exact cause of the interrupt and clear its source.<br>0b - Not detected<br>1b - Detected|
|16<br>—|Reserved|
|15-8<br>—|Reserved|
|7<br>—|Reserved|
|6<br>—|Reserved|
|5<br>—|Reserved|
|4<br>—|Reserved|
|3<br>—|Reserved|
|2<br>—|Reserved|
|1<br>Q1IS|Queue 1 Interrupt Status<br>Indicates whether the queue 1 interrupt status is detected.<br>To reset this field, the application must readMTL Queue 1 Interrupt Control Status<br>(MTL_Q1_Interrupt_Control_Status)to get the exact cause of the interrupt and clear its source.<br>0b - Not detected<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3254 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - Detected|
|0|Queue 0 Interrupt Status|
|Q0IS|Indicates whether the queue 0 interrupt status is detected.|
||To reset this field, the application must readMTL Queue 0 Interrupt Control Status<br>(MTL_Q0_Interrupt_Control_Status)to get the exact cause of the interrupt and clear its source.|
||0b - Not detected|
||1b - Detected|



# 74.7.189 MTL Receive Queue DMA Map 0 (MTL_RxQ_DMA_Map0) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RxQ_DMA_Map0|C30h|



## Function 

## Reserves in EQOS-CORE and EQOS-MTL configurations. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3255-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserv Reserv Reserv Reserv<br>Reserved  Reserved  Reserved  Reserved<br>W ed  ed  ed  ed<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Q1DD Q1MD Q0DD Q0MD<br>Reserved  Reserved  Reserved  Reserved<br>W MACH  MACH  MACH  MACH<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-29<br>—|Reserved.|
|28<br>—|Reserved.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3255 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field<br>27-25<br>—|Function<br>Reserved.|
|---|---|
|24<br>—|Reserved.|
|23-21<br>—|Reserved.|
|20<br>—|Reserved.|
|19-17|Reserved.|
|—<br>16<br>—|Reserved.|
|15-13<br>—|Reserved.|
|12<br>Q1DDMACH|Queue 1 Enabled for DA-based DMA Channel Selection<br>Enables or disables queue 1 for DA-based DMA channel selection.<br>If this field is 1, it indicates that the packets received in queue 1 are routed to a particular DMA channel as<br>decided in the MAC receiver based on the DMA channel number programmed in the L3-L4 filter registers,<br>or the Ethernet DA address.<br>When this field becomes 0, it indicates that the packets received in queue 1 are routed to the DMA Channel<br>programmed in theMTL_RxQ_DMA_Map0[Q1MDMACH](bits [10:8]).<br>0b - Disabled<br>1b - Enabled|
|11-9<br>—|Reserved.|
|8<br>Q1MDMACH|Queue 1 Mapped to DMA Channel<br>Controls the routing of the received packet in Queue 1 to the DMA channel:<br>000b - DMA Channel 0<br>001b - DMA Channel 1<br>010b - DMA Channel 2<br>011b - DMA Channel 3<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3256 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function<br>100b - DMA Channel 4<br>101b - DMA Channel 5<br>110b - DMA Channel 6<br>111b - DMA Channel 7<br>This field is valid when theMTL_RxQ_DMA_Map0[Q1DDMACH]resets.<br>The field's width depends on the number of RX DMA channels and in some configurations all the values may<br>not be valid . For example, if two RX DMA channels are selected, then only 000b and 001b are valid, the<br>other bits are reserved.|
|---|---|
|7-5<br>—|Reserved.|
|4<br>Q0DDMACH|Queue 0 Enabled for DA-based DMA Channel Selection<br>Enables or disables queue 0 for DA-based DMA channel selection.<br>If this field is 1, it indicates that the packets received in queue 0 are routed to a particular DMA channel as<br>decided in the MAC Receiver based on the DMA channel number programmed in the L3-L4 filter registers,<br>or the Ethernet DA address.<br>When this field becomes 0, it indicate that the packets received in queue 0 are routed to the DMA Channel<br>programmed in theMTL_RxQ_DMA_Map0[Q0MDMACH].<br>0b - Disable<br>1b - Enable|
|3-1<br>—|Reserved.|
|0<br>Q0MDMACH|Queue 0 Mapped to DMA Channel<br>Controls the routing of the packet received in queue 0 to the DMA channel:<br>000b - DMA channel 0<br>001b - DMA channel 1<br>010b - DMA channel 2<br>011b - DMA channel 3<br>100b - DMA channel 4<br>101b - DMA channel 5<br>110b - DMA channel 6<br>111b - DMA channel 7<br>This field is valid when theMTL_RxQ_DMA_Map0[Q0DDMACH]resets.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3257 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||The field's width depends on the number of RX DMA channels in some configurations all the values may not|
||be valid. For example, if the number of RX DMA channels selected is 2, only 000 and 001 bits are valid, the<br>other bits are reserved.|



# 74.7.190 MTL TBS Control (MTL_TBS_CTRL) 

Offset 

|Register|Offset|
|---|---|
|MTL_TBS_CTRL|C40h|



## Function 

Controls the operation of time based scheduling. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3258-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>LEOS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserv<br>LEOS  LEGOS  Reserved  LEOV  ESTM<br>W ed<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-8|Launch Expiry Offset|
|LEOS|Computes the launch expiry time.|
||To compute the launch expiry time the value in units of 256 nanoseconds is added to the launch time. The<br>field value is valid only ifMTL_TBS_CTRL[LEOV]is 1.|
||Max value: 999,999,999 nanosecond should be smaller than CTR-1 value when ESTM mode = 1, because<br>this value is a modulo CTR value.|
|7|Reserved.|
|—||
|6-4|Launch Expiry GSN Offset|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3258 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|LEGOS|Computes the Launch expiry time.<br>To compute the launch expiry time the number of GSN slots is to be added to the launch GSN. The field<br>value is valid only ifMTL_TBS_CTRL[LEOV]is 1.|
|3-2<br>—<br>1<br>LEOV|Reserved.<br>Launch Expiry Offset Valid<br>Indicates ifMTL_TBS_CTRL[LEOS]is valid or invalid.<br>When this field is 1, it indicates thatMTL_TBS_CTRL[LEOS]is valid.<br>When not 1, it indicates that the launch expiry Offset is not valid and the MTL must not check for launch<br>expiry time.<br>0b - Invalid<br>1b - Valid|
|0<br>ESTM|EST offset Mode<br>Enables or disables EST Offset mode.<br>If this field is 1, the launch time value used in Time Based Scheduling is interpreted as an EST offset value<br>and is added to theBTRof the current list.<br>When this field becomes 0, the launch time value is used as an absolute value that must be compared with<br>the system time [39:8].<br>0b - Disabled<br>1b - Enabled|



# 74.7.191 MTL EST Control (MTL_EST_Control) 

## Offset 

|Register|Offset|
|---|---|
|MTL_EST_Control|C50h|



## Function 

Controls the operation of enhancements to scheduled transmission (IEEE802.1Qbv). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3259 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3260-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>PTOV  CTOV<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserv<br>CTOV  TILS  LCSE  DFBS  DDBF  Reserved  SSWL  EEST<br>W ed<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-24|PTP Time Offset Value|
|PTOV|Indicates the PTP time offset value.<br>You must multiply 6 to the value of PTP clock period in nanoseconds. At the beginning of the installation of<br>a new GCL this value avoid transmission overruns.|
|23-12|Current Time Offset Value|
|CTOV|Provides a 12 bit time offset value in nano second which is added to the current time to compensate for all<br>the implementation pipeline delays such as the CDC sync delay, buffering delays, data path delays and so<br>on. This offset ensures that the impact of gate controls is visible on the line exactly at the pre-determined<br>schedule (or as close to the schedule as possible).|
|11<br>—|Reserved.|
|10-8<br>TILS|Time Interval Left Shift Amount<br>Provides the left shift amount for the programmed time interval values used in the gate control lists.<br>000b - No left shift needed (equal to x1ns)<br>001b - Left shift TI by 1 bit (equal to x2ns)<br>010b - Left shift TI by 2 bits (equal to x4ns)<br>-<br>-<br>100b - Left shift TI by 7 bits (equal to x128ns)<br>On the basis of configuration you must consider one or more bits of this field as reserved or read-only.|
|7-6|Loop Count to Report Scheduling Error|
|LCSE|Provides programmable number of GCL list iterations before reporting an HLBS error which is defined<br>inMTL_EST_Status.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3260 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function<br>00b - 4 iterations<br>01b - 8 iterations<br>10b - 16 iterations<br>11b - 32 iterations|
|---|---|
|5<br>DFBS|Drop Frames Causing Scheduling Error<br>Provides the status of the frames causing scheduling error.<br>If this field is 1 then the frames report to cause an HOL blocking because theMTL_EST_Status[HLBS]is<br>not scheduled after 4,8,16,and 32 (on the basis ofMTL_EST_Control[LCSE]) GCL iterations are dropped.<br>0b - Do not drop frames<br>1b - Drop frames|
|4<br>DDBF|Do not Drop Frames during Frame Size Error<br>Provides status of frames during Frame Size Error.<br>If this field is 1, it indicates that the frames are not dropped during head-of-line blocking because of the frame<br>size error (MTL_EST_Status[HLBF]).<br>0b - Drop frames during frame size error<br>1b - Do not Drop frames during frame size error|
|3-2<br>—|Reserved.|
|1<br>SSWL|Switch to Software Owned List<br>If this field is 1, it indicates that the software has programmed that list that it currently owns (SWOL) and the<br>hardware should switch to the new list based on the new BTR. Hardware clears this bit when the switch to<br>the SWOL happens to indicate the completion of the switch or when an BTR error (BTRE in Status register)<br>is set. When BTRE is set this bit is cleared but SWOL is not updated as the switch was not successful.<br>Access restriction apply to this field that clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>Enables or disables the switch to the software owned list.<br>0b - Disabled<br>1b - Enabled|
|0<br>EEST|Enable EST<br>Enables or disables EST.<br>If the field becomes 0, it indicate that the gate control list processing is halted and all gates are assumed to<br>be in open state. The field must be 1 for the hardware to start processing the gate control lists. During the<br>toggle from 0 to 1, when theMTL_EST_Control[SSWL]is 1, the gate control list processing starts.<br>During the configuration when DWC_EQOS_ASP_ECC is selected, the hardware resets this field and<br>disables the EST function if any uncorrectable error is detected in the EST memory .|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3261 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Disabled|
||1b - Enabled|



# 74.7.192 MTL EST Status (MTL_EST_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_EST_Status|C58h|



## Function 

Provides status of enhancements to scheduled transmission (IEEE802.1Qbv). 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||Rese|rved|||||||CG|SN||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||Rese|rved|||BTR|L||SWOL|Rese|rved|CGCE|HLBS|HLBF|BTRE|SWLC|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-20|Reserved.|
|—||
|19-16|Current GCL Slot Number|
|CGSN|Indicates the slot number of the GCL list. Slot number is a modulo 16 count of the GCL List loops executed<br>so far.|
||Even if a new GCL list is installed, the count is incremental.|
|15-12<br>—|Reserved.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3262 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field<br>11-8|Function<br>BTR Error Loop Count|
|---|---|
|BTRL|Provides the minimum count (N) for which the equation Current Time =< New BTR + (N * New Cycle Time)<br>becomes true. N = "1111" indicates the iterations exceeded the value of 8 and the hardware was not able<br>to update New BTR to be equal to or greater than Current Time. Software intervention is needed to update<br>the New BTR. Value cleared when BTRE field of this register is cleared.|
|7<br>SWOL|S/W owned list<br>When '0' indicates Gate control list number "0" is owned by software and when "1" indicates the Gate Control<br>list "1" is owned by the software. Any reads/writes by the software (using indirect access via GCL_Control)<br>is directed to the list indicated by this value by default. The inverse of this value is treated as HWOL.<br>R/W operations performed by hardware are directed to the list pointed by HWOL by default.<br>0b - Gate control list number "0" is owned by software<br>1b - Gate control list number "1" is owned by software|
|6-5<br>—|Reserved.|
|4<br>CGCE|Constant Gate Control Error<br>This error occurs when the list length (LLR) is 1 and the Cycle Time (CTR) is less than or equal to the<br>programmed Time Interval (TI) value after the optional Left Shifting. The above programming implies<br>Gates are either always Closed or always Open based on the Gate Control values; the same effect can<br>be achieved by other simpler (non TSN) programming mechanisms. Since the implementation does not<br>support such a programming an error is reported.<br>Access restriction applies. Self-set to 1 on internal event. Setting 1 clears. Setting 0 has no effect.<br>0b - Constant Gate Control Error not detected<br>1b - Constant Gate Control Error detected|
|3<br>HLBS|Head-Of-Line Blocking due to Scheduling<br>Set when the frame is not able to win arbitration and get scheduled even after 4 iterations of the GCL.<br>Indicates to software a potential programming error. The one hot encoded values of the Queue Numbers<br>that are not able to make progress are indicated in the MTL_EST_Sch_Error register. Bit cleared when<br>MTL_EST_Sch_Error register is all zeros.<br>0b - Head-Of-Line Blocking due to Scheduling not detected<br>1b - Head-Of-Line Blocking due to Scheduling detected|
|2<br>HLBF|Head-Of-Line Blocking due to Frame Size<br>Set when HOL Blocking is noticed on one or more Queues as a result of none of the Time Intervals of gate<br>open in the GCL being greater than or equal to the duration needed for frame size (or frame fragment size<br>when preemption is enabled) transmission. The one hot encoded Queue numbers that are experiencing<br>HLBF are indicated in the MTL_EST_Frm_Size_Error register. Additionally, the first Queue number that<br>experienced HLBF along with the frame size is captured in MTL_EST_Frm_Size_Capture register. Bit<br>cleared when MTL_EST_Frame_Size_ Error register is all zeros.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3263 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Head-Of-Line Blocking due to Frame Size not detected<br>1b - Head-Of-Line Blocking due to Frame Size detected|
|1<br>BTRE|BTR Error<br>Indicates whether the BTR error is detected.<br>When this field is 1, it indicates a programming error in the BTR of SWOL where the programmed value is<br>less than the current time. If the BTRL = "1111", SWOL is not updated and software must reprogram the BTR<br>to a value greater than current time and then set SSWL to reinitiate the switch to SWOL. Else if the value of<br>BTRL < "1111", SWOL is updated and this field indicates the number of iterations (of + CycleTime) taken<br>by hardware to update the BTR to a value greater than Current Time.<br>Access restrictions apply to this field. It sets automatically to 1 on an internal event occurence. Writing 1<br>clears this field and writing 0 has no effect.<br>0b - BTR Error not detected<br>1b - BTR Error detected|
|0<br>SWLC|Switch to Software Owned List Complete<br>Indicates whether the switch to software owned list complete is detected.<br>When the field is 1, it indicates that the hardware has successfully switched to the SWOL, and updated the<br>MTL_EST_Status[SWOL]to that effect.<br>This field is 0 whenMTL_EST_Control[SSWL]transitions from 0 to 1, or on a software write.<br>Access restrictions apply to this field. It clears automatically and writing 0 to it has no effect.<br>0b - Not detected<br>1b - Detected|



# 74.7.193 MTL EST Scheduling Error (MTL_EST_Sch_Error) 

## Offset 

|Register|Offset|
|---|---|
|MTL_EST_Sch_Error|C60h|



## Function 

Provides the one hot encoded queue numbers that have the scheduling related error (timeout). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3264 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3265-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>Reserved  SEQN<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-2|Reserved.|
|—||
|1-0|Schedule Error Queue Number|
|SEQN|Provides the one hot encoded queue numbers that have experienced error or timeout described<br>inMTL_EST_Status[HLBS].|
||Access restriction apply to this field. It automatically becomes 1 on an internal event occurrence. Writing 1<br>clears this field and writing 0 to it has no effect.|



# 74.7.194 MTL EST Frame Size Error (MTL_EST_Frm_Size_Error) 

## Offset 

|Register|Offset|
|---|---|
|MTL_EST_Frm_Size_Err|C64h|
|or||



## Function 

Provides the one hot encoded queue numbers that have the frame Size related error. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3265 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3266-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>Reserved  FEQN<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-2|Reserved.|
|—||
|1-0|Frame Size Error Queue Number|
|FEQN|Provides the one hot encoded queue Nnumbers that have experienced error described<br>inMTL_EST_Status[HLBF].|
||Access restriction apply to this field. It automatically becomes 1 on an internal event occurrence. Writing 1<br>clears this field and writing 0 to it has no effect.|



# 74.7.195 MTL EST Frame Size Capture (MTL_EST_Frm_Size_Capture) 

## Offset 

|Register|Offset|
|---|---|
|MTL_EST_Frm_Size_Ca|C68h|
|pture||



## Function 

Captures the frame Size and queue number of the first occurrence of the frame Size related error. When you write 0, it captures the data of immediate next occurrence of a similar error. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3266 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||Reserve|d|||||||HBFQ|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|Reserv||||||||HBFS||||||||
|W|ed||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-17|Reserved.|
|—||
|16|Queue Number of HLBF|
|HBFQ|Captures the binary value of the first queue (number) which experiences the HLBF error (see<br>MTL_EST_Status[HLBF]). Any subsequent queue errors similar to HLBF errors does not alter the value<br>after it is written. After this field is 0, it captures the queue number of the next occurring HLBF error.<br>Field's width is based on the number of transit queues configured; remaining fields are read-only. This field<br>clears whenMTL_EST_Frm_Size_Erroris all zeros.|
|15<br>—|Reserved.|
|14-0|Frame Size of HLBF|
|HBFS|Captures the frame Size of the dropped frame related to queue number indicated<br>inMTL_EST_Frm_Size_Capture[HBFQ].<br>If this field is zero, then this register must be considered invalid.<br>This field clears whenMTL_EST_Frm_Size_Erroris all zeros.|



# 74.7.196 MTL EST Interrupt Enable (MTL_EST_Intr_Enable) 

## Offset 

|Register|Offset|
|---|---|
|MTL_EST_Intr_Enable|C70h|



## Function 

Implements the interrupt enable fields for the various events that generate an interrupt. Bit positions have a 1 to 1 correlation with the status bit positions in MTL_ETS_Status register. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3267 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||Rese|rved||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||Reserved||||||CGCE|IEHS|IEHF|IEBE|IECC|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-5|Reserved.|
|—||
|4|Interrupt Enable for CGCE|
|CGCE|Indicates whether an interrupt forMTL_EST_Intr_Enable[CGCE]is enabled.<br>When this field is 1, it generates an interrupt when the constant gate control error occurs and is indicated<br>in the status. When this field becomes 0, this event does not generate an interrupt<br>0b - Disabled<br>1b - Enabled|
|3<br>IEHS|Interrupt Enable for HLBS<br>Indicates whether an interrupt forMTL_EST_Status[HLBS]is enabled.<br>When this field is 1, it generates an interrupt when the head-of-line blocking due to scheduling issue occurs<br>and is indicated in the status. When this field becomes 0, this event does not generate an interrupt.<br>0b - Disabled<br>1b - Enabled|
|2<br>IEHF|Interrupt Enable for HLBF<br>Indicates whether an interrupt forMTL_EST_Status[HLBF]is enabled.<br>When this field is 1, it generates an interrupt when the head-of-line blocking due to frame size error occurs<br>and is indicated in the status. When this field becomes 0, this event does not generate an interrupt.<br>0b - Disabled<br>1b - Enabled|
|1|Interrupt Enable for BTR Error|
|IEBE|Indicates whether an interrupt for BTR error is enabled.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3268 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||When this field is 1, it generates an interrupt when the BTR error occurs and is indicated in the status. When<br>this field becomes 0, this event does not generate an interrupt.<br>0b - Disabled<br>1b - Enabled|
|0|Interrupt Enable for Switch List|
|IECC|Indicates whether the interrupt for switch list is enabled.<br>When this field is 1, it generates an interrupt when the configuration change is successful and the hardware<br>switches to the new list. When this field becomes 0, this event does not generate an interrupt.<br>0b - Disabled<br>1b - Enabled|



# 74.7.197 MTL EST GCL Control (MTL_EST_GCL_Control) 

## Offset 

|Register|Offset|
|---|---|
|MTL_EST_GCL_Control|C80h|



## Function 

Provides the control information for reading and writing to the gate control lists. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||Rese|rved||||EST|EIEC|ESTEI<br>EE|ERR0||Res|erved||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||AD|DR||||Rese|rved|DBGB|DBGM|Reserv<br>ed|GCRR|R1W0|SRWO|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function||
|---|---|---|
|31-24|Reserved.||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3269 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|23-22<br>ESTEIEC|ECC Inject Error Control for EST Memory<br>Provides the status of inject error control for EST memory.<br>WhenMTL_EST_GCL_Control[ESTEIEE]= 1, it indicates that on the basis of the value encoded in this field<br>following errors are inserted.<br>This field is valid only if you select DWC_EQOS_ASP_ECC feature during the configuration, otherwise it<br>is reserved.<br>00b - Insert 1 bit error<br>01b - Insert 2 bit errors<br>10b - Insert 3 bit errors<br>11b - Insert 1 bit error in address field|
|21<br>ESTEIEE|EST ECC Inject Error Enable<br>Indicates whether the EST ECC inject error is enabled.<br>If this field along withMTL_EST_Control[EEST]= 1, it enables the ECC error injection feature.<br>When this field becomes 0, it disables the ECC error injection feature.<br>0b - Disabled<br>1b - Enabled|
|20<br>ERR0|If this field is 1, it indicates that when the software writes to GCL the last write operation was aborted and<br>whenMTL_EST_Control[SSWL]is 1, GCL registers are prohibited.<br>Access restriction apply to this field and automatically becomes 1 on an internal event occurrence. Writing<br>1 to this field clears it and writing 0 to this field has no effect.<br>0b - ERR0 is disabled<br>1b - ERR1 is enabled|
|19-16<br>—|Reserved.|
|15-8<br>ADDR|Gate Control List Address: (GCLA when GCRR is "0").<br>Provides the address (row number) of the gate control list at which the R/W operation has to be performed.<br>By default the gate control list to whichMTL_EST_Status[SWOL]points is selected for read and write. If<br>MTL_EST_GCL_Control[DBGM]is 1, it indicates thatMTL_EST_GCL_Control[DBGB]gives Debug mode<br>access to read and write. The field's width depends on DWC_EQOS_EST_DEP and the unused bits must<br>be treated as read only.<br>Gate Control list Related Registers Address: (GCRA when GCRR is "1").<br>By default the GCL related register set pointed byMTL_EST_Status[SWOL]is selected for read or write.<br>IfMTL_EST_GCL_Control[DBGM], it indicates thatMTL_EST_GCL_Control[DBGB]gives Debug mode<br>access to read write. Lower 3 bits are only used in this mode, higher order bits are treated as dont cares.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3270 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function<br>000b - BTR Low (31:0)<br>001b - BTR High (63:31)<br>010b - CTR Low (31:0)<br>011b - CTR High (39:32)<br>100b - TER (31:0)<br>101b - LLR (n:0) (where n is (log{DWC_EQOS_EST_DEP} / log2))<br>Others - Reserved|
|---|---|
|7-6<br>—|Reserved.|
|5|Debug Mode Bank Select|
|DBGB|Indicates whether the read and write in Debug mode is directed to bank 0 or bank 1.<br>When this field is 0, it indicates that read or write in Debug mode must be directed to bank<br>0 (GCL0 and corresponding Time related registers). When this field is 1, it indicates that read<br>or write in Debug mode should be directed to bank 1 (GCL1 and corresponding Time related<br>registers). WhenMTL_EST_GCL_Control[DBGM]is 1 you can use this value and overrides with the<br>MTL_EST_Status[SWOL]value.<br>0b - Directed to bank 0<br>1b - Directed to bank 1|
|4<br>DBGM|Debug Mode<br>Enables or disables Debug mode.<br>When this field is 1, it indicates that the read and write is in Debug mode where the<br>MTL_EST_GCL_Control[DBGB]value explicitly provides the memory bank (for GCL and time related<br>registers). When this field is 0, it indicates thatMTL_EST_Status[SWOL]determines which bank to use.<br>0b - Disabled<br>1b - Enabled|
|3<br>—|Reserved.|
|2<br>GCRR|Gate Control Related Registers<br>Enables or disables gate control related registers.<br>When this field is 1, it indicates that the read or write access is for the GCL related registers (BTR, CTR,<br>TER, LLR) for which GCRA provides the address. When this field is 0, it indicates that read and write must<br>be directed to GCL from the address which GCLA provides.<br>0b - Disabled<br>1b - Enabled<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3271 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|1|Read '1', Write '0'|
|R1W0|Indicates whether this field performs read operation or write operation.<br>When this field is 1 it indicates that it performs a read operation.<br>When this field is 0 it indicates that it performs a write operation.<br>0b - Write operation<br>1b - Read operation|
|0|Start Read/Write Operation|
|SRWO|Indicates whether the read/write operation is enabled.<br>When this field is 1, it indicates that a read/write operation has started and is in progress.<br>When hardware resets this field andMTL_EST_GCL_Control[ERR0]= 1 , it indicates that the read/write<br>operation has completed or an error has occurred.<br>Reads: When this field becomes 0, it indicates thatMTL_EST_GCL_Datareads data.<br>Writes: Before writing 1 to this field, you must programMTL_EST_GCL_Datawith write data.<br>Access restrictions apply to this field. It clears automatically. Writing 1 sets this field and writing 0 to it has<br>no effect.<br>0b - Disabled<br>1b - Enabled|



# 74.7.198 MTL EST GCL Data (MTL_EST_GCL_Data) 

## Offset 

|Register|Offset|
|---|---|
|MTL_EST_GCL_Data|C84h|



## Function 

Holds the read data or write data in case of reads and writes respectively. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3272 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3273-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>GCD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>GCD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|Gate Control Data|
|GCD|Provides the data corresponding to the address selected in theMTL_EST_GCL_Control. This field is used<br>for both read and write operations.|



# 74.7.199 MTL FPE Control Status (MTL_FPE_CTRL_STS) 

## Offset 

|Register|Offset|
|---|---|
|MTL_FPE_CTRL_STS|C90h|



## Function 

Controls the operation of, and provides status for frame preemption (IEEE802.1Qbu/802.3br). 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3273-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R HRS<br>Reserved  Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>Reserved  PEC  Reserved  AFSZ<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3273 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Fields 

|Field|Function|
|---|---|
|31-29<br>—|Reserved.|
|28<br>HRS|Hold/Release Status<br>Indicates whether a set-and-release-MAC operation which was last executed and the pMAC is in release<br>state or in hold state.<br>0b - Release state<br>1b - Hold state|
|27-16<br>—|Reserved.|
|15-10<br>—<br>9-8<br>PEC|Reserved.<br>Preemption Classification<br>When this field is 1, it indicates that you must classify the corresponding queue as preemptable.<br>When this field is 0, it indicates that you must classify the queue as express.<br>When set indicates the corresponding Queue must be classified as preemptable, when '0' Queue is<br>classified as express. When both EST (Qbv) and Preemption are enabled, Queue-0 is always assumed to<br>be preemptable. When you enables EST (Qbv), the preemptable queues are always assumed to be in open<br>state in gate control list.|
|7-2<br>—<br>1-0|Reserved.<br>Additional Fragment Size|
|AFSZ|Indicates that, in units of 64 bytes, the minimum number of bytes over 64 bytes required in non-final<br>fragments of preempted frames. The minimum non-final fragment size is (AFSZ +1) * 64 bytes.|



# 74.7.200 MTL FPE Advance (MTL_FPE_Advance) 

## Offset 

|Register|Offset|
|---|---|
|MTL_FPE_Advance|C94h|



Function 

Holds the hold and release advance time. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3274 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3275-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>RADV<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>HADV<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-16|Release Advance|
|RADV|Provides the maximum time in nanoseconds that can elapse between issuing a release to the MAC and the<br>MAC being ready to resume transmission of preemptable frames, in the absence of there being any express<br>frames available for transmission.|
|15-0|Hold Advance|
|HADV|Provides the maximum time in nanoseconds that can elapse between issuing a hold to the MAC and the<br>MAC ceasing to transmit any preemptable frame that is in the process of transmission or any preemptable<br>frames that are queued for transmission.|



# 74.7.201 MTL Rx Parser Control Status (MTL_RXP_Control_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RXP_Control_Statu|CA0h|
|s||



## Function 

Establishes the operating mode of receive parser and provides some status. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3275 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3276-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RXPI<br>Reserved  NPE<br>W<br>Reset 1 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R MTL_<br>Reserved  NVE<br>W SCS1<br>Reset 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31<br>RXPI|RX Parser in Idle State<br>Indicates whether the receive parser is in idle state.<br>When this field is 1, it indicates that the receive parser is in idle state and waiting for the processing of a new<br>packet. When parser disables, you can use this field as a handshake with software and also the software<br>can update the receive parser instruction table when you write 1 to this field.<br>0b - Not in Idle state<br>1b - Idle state|
|30-22<br>—<br>21-16<br>NPE|Reserved.<br>Number of parsable entries in the Instruction table<br>Indicates the number of parsable entries in the instruction memory. This is used in receive parser logic to<br>detect programming error.<br>MTL_RXP_Interrupt_Control_Status[NPEOVIS]= 1, if the number of parsed entries for a packet is more<br>than this entry.|
|15|MTL_SCS1|
|MTL_SCS1|Is reserved for NXP internal use.<br>The value of this field must always be 0 unless NXP instructs you otherwise. Writing 1 to any of the bits of<br>this field might cause unexpected behavior in th IP.|
|14-6<br>—<br>5-0|Reserved.<br>Number Of Valid Entry Address Or Index In The Instruction Table|
|NVE|Indicates the number of valid entry address or index in the instruction memory.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3276 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||The maximum valid entry address is = NVE + 1 and the addresses or indices range from 0 to 32. Therefore,<br>if the value of this field is 32, the number of valid entry address is 33. This value is used in receive parser<br>logic to detect if any programming errors exist. When parsing, the module writes 1 toNVEOVISif the number<br>of the memory address is found to be more than the defined maximum valid entry address number.|
||The minimum value of this field must be two.<br>~~NOTE~~|



# 74.7.202 MTL Rx Parser Interrupt Control Status (MTL_RXP_Interrupt_Control_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RXP_Interrupt_Con|CA4h|
|trol_Status||



## Function 

Provides enable control for the interrupts and also provides interrupt status. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||Rese|rved||||||PDRFI<br>E|FOOVI<br>E|NPEO<br>VIE|NVEO<br>VIE|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||Rese|rved||||||PDRFI<br>S|FOOVI<br>S|NPEO<br>VIS|NVEO<br>VIS|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function|
|---|---|
|31-20|Reserved.|
|—||
|19|Packet Drop due to RF Interrupt Enable|
|PDRFIE|Indicates whether the packet drop due to RF interrupt is enabled.|
||If this field is 1, it enables the PDRFIS interrupt. When this field becomes 0, it disables the PDRFIS interrupt.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3277 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Disabled<br>1b - Enabled|
|18<br>FOOVIE|Frame Offset Overflow Interrupt Enable<br>Indicates whether the frame offset overflow interrupt is enabled.<br>If this field is 1, it enables the FOOVIS interrupt.<br>When this field becomes 0, it disables the FOOVIS interrupt.<br>0b - Disabled<br>1b - Enabled|
|17|Number of Parsable Entries Overflow Interrupt Enable|
|NPEOVIE|Enables or disables the number of parsable entries overflow interrupt.<br>If this field is 1, it enables the NPEOVIS interrupt.<br>When this field becomes 0, it disables the NPEOVIS interrupt.<br>0b - Disable<br>1b - Enable|
|16|Number of Valid Entries Overflow Interrupt Enable|
|NVEOVIE|Enables or disables the number of valid entries overflow interrupt.<br>If this field is 1, it enables the NVEOVIS interrupt.<br>When this field becomes 0, it disables the NVEOVIS interrupt.<br>0b - Disable<br>1b - Enable|
|15-4<br>—|Reserved.|
|3<br>PDRFIS|Packet Dropped due to RF Interrupt Status<br>Indicates whether the packet dropped due to RF interrupt status is detected.<br>If the Rx Parser result says to drop the packet by setting RF=1 in the instruction memory, then this bit is set<br>to 1.<br>This field clears when the application writes 1 to this field.<br>Access apply to this field. It automatically sets to 1 on an internal event occurrence. Writing 1 clears this field<br>and writing 0 to it has no effect.<br>0b - Not detected<br>1b - Detected|
|2|Frame Offset Overflow Interrupt Status|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3278 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|FOOVIS|Indicates whether the frame offset overflow interrupt status is detected.<br>If this field is 1, it indicates that when parsing, the instruction table entry's frame offset is more than the<br>EOF offset.<br>This field clears when the application writes 1 to this field.<br>Access apply to this field. It automatically sets to 1 on an internal event occurrence. Writing 1 clears this field<br>and writing 0 to it has no effect.<br>0b - Not detected<br>1b - Detected|
|1<br>NPEOVIS|Number of Parsable Entries Overflow Interrupt Status<br>Indicates whether the number of parsable entries overflow interrupt status is detected.<br>If this field is 1, it indicates that when parsing a packet the number of parsed entries are more than<br>NPE[] (MTL_RXP_Control_Status[NPE]).<br>This field clears when the application writes 1 to this field.<br>Access apply to this field. It automatically sets to 1 on an internal event occurrence. Writing 1 clears this field<br>and writing 0 to it has no effect.<br>0b - Not detected<br>1b - Detected|
|0<br>NVEOVIS|Number of Valid Entry Address/Index Overflow Interrupt Status<br>Indicates whether the number of valid entry address or index overflow interrupt status is detected.<br>If this field is 1, it indicates that when parsing, the instruction address is more<br>thanMTL_RXP_Control_Status[NVE].<br>For example, whenMTL_RXP_Control_Status[NVE]= 31, the maximum valid entry address/index is NVE+1<br>that is 32 (addresses/indices = 0 to 32, or 33 entries).MTL_RXP_Interrupt_Control_Status[NVEOVIS]= 1<br>when currently processed entry indicates that the next address is 33 or more, that is 34th or later entries.<br>This field clears when the application writes 1 to this field.<br>Access apply to this field. It automatically sets to 1 on an internal event occurrence. Writing 1 clears this field<br>and writing 0 to it has no effect.<br>0b - Not detected<br>1b - Detected|



# 74.7.203 MTL Rx Parser Drop Count (MTL_RXP_Drop_Cnt) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RXP_Drop_Cnt|CA8h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3279 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Function 

Provides the drop count of receive parser initiated drops. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3280-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>RXPD<br>R RXPDC<br>COVF<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXPDC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31|Rx Parser Drop Counter Overflow Bit|
|RXPDCOVF|Indicates whether the receive parser drop count overflow has occurred.<br>When this field is 1, it indicates that theMTL_RXP_Drop_Cnt[RXPDC]counter field has crossed the<br>maximum limit.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not occurred|
||1b - Occurred|
|30-0|Rx Parser Drop Count|
|RXPDC|Provides the receive parser drop count.|
||This 31-bit counter is implemented whenever a receive parser drops a packet due to RF = 1. The counter<br>clears when you read the register.|



# 74.7.204 MTL Rx Parser Error Count (MTL_RXP_Error_Cnt) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RXP_Error_Cnt|CACh|



## Function 

Provides the receive parser related error occurrence count. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3280 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3281-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>RXPE<br>R RXPEC<br>COVF<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXPEC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31|Rx Parser Error Counter Overflow Bit|
|RXPECOVF|Indicates whether the receive parser error counter overflow has occurred.<br>When this field is 1, it indicates thatMTL_RXP_Error_Cnt[RXPEC]counter field has crossed the<br>maximum limit.<br>Access restrictions apply to this field, which clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not occurred<br>1b - Occurred|
|30-0<br>RXPEC|Rx Parser Error Count<br>Provides the receive parser error count.<br>This 31-bit counter is implemented whenever a receive parser encounters following error scenarios:<br>Entry address >= NVE[]<br>Number parsed entries >= NPE[]<br>Entry address > EOF data entry address<br>The counter clears when you read the register.|



# 74.7.205 MTL Rx Parser Indirect Access Control Status (MTL_RXP_Indirect_Acc_Control_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RXP_Indirect_Acc_|CB0h|
|Control_Status||



## Function 

Provides the indirect access control and status for receive parser memory. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3281 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3282-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R STAR RXPEI WRRD<br>Reserved  RXPEIEC  Reserved<br>W TBU... EE  N<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>Reserved  ADDR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31|FRP Instruction Table Access Busy|
|STARTBUSY|When this bit is set to 1 by the software then it indicates to start the Read/Write operation from/to the Rx<br>Parser Memory.<br>Software should read this bit as 0 before issuing read or write request to access the Parser<br>Memory Instructions.<br>This bit when set to 1 indicates that hardware is busy until its gets cleared by hardware and software should<br>not issue any read or write operation.<br>0b - hardware not busy<br>1b - hardware is busy (Read/Write operation from/to the Rx Parser Memory)|
|30-23<br>—|Reserved.|
|22-21<br>RXPEIEC|ECC Inject Error Control for Rx Parser Memory<br>Controls the ECC inject error for receive parser memory.<br>WhenMTL_RXP_Indirect_Acc_Control_Status[RXPEIEE]= 1, it indicates that on the basis of the value<br>encoded in this field following errors are inserted:<br>00b - Insert 1 bit error<br>01b - Insert 2 bit errors<br>10b - Insert 3 bit errors<br>11b - Insert 1 bit error in address field|
|20<br>RXPEIEE|ECC Inject Error Enable for Rx Parser Memory<br>Indicates whether the ECC inject error for receive parser memory is enabled.<br>If this field is 1, it enables the ECC error injection feature.|
||When this field becomes 0, it disables the ECC error injection feature.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3282 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Disabled<br>1b - Enabled|
|19-17<br>—|Reserved.|
|16<br>WRRDN|Read Write Control<br>Controls the read and write operation to the receive parser memory.<br>If this field is 1, it indicates the write operation to the receive parser memory.<br>When this field is 0, it indicates the read operation to the receive parser memory.<br>0b - Read operation to the receive parser memory<br>1b - Write operation to the receive parser memory|
|15-8<br>—|Reserved.|
|7-0<br>ADDR|FRP Instruction Table Offset Address<br>Indicates the ADDR of the 32-bit entry in receive parser instruction table. Each entry has 128-bit (4x32-<br>bit words).<br>The X depends on the configurable DWC_EQOS_FRP_ENTRIES.<br>If DWC_EQOS_FRP_ENTRIES = 256 , then X = 9<br>If DWC_EQOS_FRP_ENTRIES = 128 , then X = 8<br>If DWC_EQOS_FRP_ENTRIES = 64, then X = 7|



# 74.7.206 MTL Rx Parser Indirect Access Data (MTL_RXP_Indirect_Acc_Data) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RXP_Indirect_Acc_|CB4h|
|Data||



## Function 

Provides the data associated to indirect access to receive parser memory. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3283 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3284-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R DATA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DATA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-0|FRP Instruction Table Write/Read Data|
|DATA|You must write this register before issuing any write command.|
||After read command, whenMTL_RXP_Indirect_Acc_Control_Status[STARTBUSY]= 0, the hardware<br>provides the read data from the receive parser memory for read operation.|



# 74.7.207 MTL ECC Control (MTL_ECC_Control) 

## Offset 

|Register|Offset|
|---|---|
|MTL_ECC_Control|CC0h|



## Function 

Establishes the operating mode of ECC related to MTL memories. 

## Diagram 

|Bits<br>R<br>W|31|30|29|28|27|26|25|24<br>Rese|23<br>rved|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||Reserved||||MEEA<br>O||Reserved||Reserv<br>ed|MRXP<br>EE|MEST<br>EE|MRXE<br>E|MTXE<br>E|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

3284 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Fields 

|Field<br>31-9<br>—|Function<br>Reserved.|
|---|---|
|8<br>MEEAO|MTL ECC Error Address Status Over-ride<br>Enables or disables the MTL ECC error address status over-ride.<br>When this field is 1, it indicates thatMTL_ECC_Err_Addr_Status[EUEAS]and<br>MTL_ECC_Err_Addr_Status[ECEAS]hold the last valid address where the error is detected.<br>When this field becomes 0, it indicates thatMTL_ECC_Err_Addr_Status[EUEAS]and<br>MTL_ECC_Err_Addr_Status[ECEAS]hold the first address where the error is detected.<br>0b - Disable<br>1b - Enable|
|7-5<br>—|Reserved.|
|4<br>—|Reserved.|
|3<br>MRXPEE|MTL Rx Parser ECC Enable<br>Indicates whether the MTL receive parser ECC is enabled.<br>If this field is 1, it enables the ECC feature for receive parser memory. When this field is 0, it disables the<br>ECC feature for receive parser memory.<br>0b - Disabled<br>1b - Enabled|
|2<br>MESTEE|MTL EST ECC Enable<br>Indicates whether the MTL EST ECC is enabled.<br>If this field is 1, it enables the ECC feature for EST memory. When this field is 0, it disables the ECC feature<br>for EST memory.<br>0b - Disabled<br>1b - Enabled|
|1<br>MRXEE|MTL Rx FIFO ECC Enable<br>Indicates whether the MTL Rx FIFO ECC is enabled.<br>If this field is 1, it enables the ECC feature for MTL receive FIFO memory. When this field is 0, it disables<br>the ECC feature for MTL receive FIFO memory.<br>0b - Disabled<br>1b - Enabled|
|0|MTL Tx FIFO ECC Enable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3285 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|MTXEE|Indicates whether the MTL Tx FIFO ECC is enabled.|
||If this field is 1, it enables the ECC feature for MTL Tx FIFO memory. When field is 0, it disables the ECC<br>feature for MTL Tx FIFO memory.|
||0b - Disabled|
||1b - Enabled|



# 74.7.208 MTL Safety Interript Status (MTL_Safety_Interrupt_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_Safety_Interrupt_St<br>atus|CC4h|



## Function 

Provides safety interrupt status. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3286-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserv<br>Reserved<br>W ed<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R MEUIS MECIS<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31|Reserved|
|—|Indicates whether the MAC safety uncorrectable interrupt status is detected.|
||0b - Not detected|
||1b - Detected|
|30-2|Reserved.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3286 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|1|MTL ECC Uncorrectable Error Interrupt Status|
|MEUIS|Indicates whether the MTL ECC uncorrectable error interrupt status is detected.<br>Indicates that an uncorrectable error interrupt event in the MTL ECC safety feature. The application must<br>readMTL_ECC_Interrupt_Statusto get the exact cause of the interrupt.<br>0b - Not detected<br>1b - Detected|
|0|MTL ECC Correctable Error Interrupt Status|
|MECIS|Indicates whether the MTL ECC correctable error interrupt status is detected.<br>Indicates that a correctable error interrupt event in the MTL ECC safety feature. The application must read<br>MTL_ECC_Interrupt_Statusto get the exact cause of the interrupt .<br>0b - MTL ECC Correctable error Interrupt Status not detected<br>1b - MTL ECC Correctable error Interrupt Status detected|



# 74.7.209 MTL ECC Interrupt Enable (MTL_ECC_Interrupt_Enable) 

## Offset 

|Register|Offset|
|---|---|
|MTL_ECC_Interrupt_Ena|CC8h|
|ble||



## Function 

Provides enable bits for the ECC interrupts. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3287-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RPCEI RXCEI TXCEI<br>Reserved  Reserved  ECEIE  Reserved  Reserved<br>W E  E  E<br>Reset 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 1<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3287 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Fields 

|Field|Function|
|---|---|
|31-13<br>—|Reserved.|
|12<br>RPCEIE|Rx Parser Memory Correctable Error Interrupt Enable<br>Indicates whether the Rx parser memory correctable error interrupt is enabled.<br>When this field is 1, it generates an interrupt when an uncorrectable error is detected at the Rx parser<br>memory interface. It is indicated inMTL_ECC_Interrupt_Status[RPCES].<br>When this field becomes 0, it indicates that this event does not generates an interrupt.<br>0b - Disabled<br>1b - Enabled|
|11-9<br>—|Reserved.|
|8<br>ECEIE|EST Memory Correctable Error Interrupt Enable<br>Indicates whether the EST memory correctable error interrupt is enabled.<br>When this field is 1, it generates an interrupt when a correctable error is detected at the MTL EST memory<br>interface. It is indicated inMTL_ECC_Interrupt_Status[ECES].<br>When this field becomes 0, it indicates that this event does not generates an interrupt.<br>0b - Disabled<br>1b - Enabled|
|7-5<br>—|Reserved.|
|4<br>RXCEIE|Rx Memory Correctable Error Interrupt Enable<br>Indicates whether the Rx memory correctable error interrupt is enabled.<br>When this field is 1, it generates an interrupt when a correctable error is detected at the MTL Rx memory<br>interface. It is indicated inMTL_ECC_Interrupt_Status[RXCES].<br>When this field becomes 0, it indicates that this event does not generates an interrupt.<br>0b - Disabled<br>1b - Enabled|
|3-1<br>—|Reserved.|
|0|Tx Memory Correctable Error Interrupt Enable|
|TXCEIE|Indicates whether the Tx memory correctable error interrupt is enabled.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3288 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||When this field is 1, it generates an interrupt when a correctable error is detected at the MTL Tx memory<br>interface. It is indicated inMTL_ECC_Interrupt_Status[TXCES].|
||When this field becomes 0, it indicates that this event does not generates an interrupt.<br>0b - Disabled|
||1b - Enabled|



# 74.7.210 MTL ECC Interrupt Status (MTL_ECC_Interrupt_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_ECC_Interrupt_Stat|CCCh|
|us||



## Function 

Provides MTL ECC Interrupt Status. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3289-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserv RPUE RPAM RPCE Reserv Reserv RXUE RXAM RXCE Reserv TXUE TXAM TXCE<br>EUES  EAMS  ECES<br>W ed  S  S  S  ed  ed  S  S  S  ed  S  S  S<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-15|Reserved.|
|—||
|14|Rx Parser Memory Uncorrectable Error Status|
|RPUES|Indicates whether the Rx parser memory uncorrectable error status is detected.|
||When this field is 1, it indicates that an uncorrectable error is detected at Rx parser memory interface.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3289 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function<br>0b - Not detected<br>1b - Detected|
|---|---|
|13<br>RPAMS|MTL Rx Parser Memory Address Mismatch Status<br>Indicates whether the MTL Rx parser memory address mismatch status is detected.<br>When this field is 1, it indicates that an address mismatch is found for Rx parser memory's address bus.<br>0b - Not detected<br>1b - Detected|
|12<br>RPCES|MTL Rx Parser Memory Correctable Error Status<br>Indicates whther the MTL Rx parser memory correctable error status is detected.<br>When this field is 1, it indicates that a correctable error is detected at RX parser memory interface.<br>0b - Not detected<br>1b - Detected|
|11<br>—|Reserved.|
|10<br>EUES|MTL EST Memory Uncorrectable Error Status<br>Indicates whether the MTL EST memory uncorrectable error status is detected.<br>When this field is 1, it indicates that an uncorrectable error is detected at MTL EST memory interface.<br>0b - Not detected<br>1b - Detected|
|9<br>EAMS|MTL EST Memory Address Mismatch Status<br>Indicates whether the MTL EST memory address mismatch status is detected.<br>When this field is 1, it indicates that an address mismatch is found for MTL EST memory's address bus.<br>0b - Not detected<br>1b - Detected|
|8<br>ECES|MTL EST Memory Correctable Error Status<br>Indicates whether the MTL EST memory correctable error status is detected.<br>When this field is 1, it indicates that a correctable error is detected at the MTL EST memory.<br>0b - Not detected<br>1b - Detected|
|7<br>—|Reserved.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3290 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Field<br>6<br>RXUES|Function<br>MTL Rx Memory Uncorrectable Error Status<br>Indicates whether the MTL Rx memory uncorrectable error status is detected.<br>When this field is 1, it indicates that an uncorrectable error is detected at the MTL Rx memory interface.<br>0b - Not detected<br>1b - Detected|
|---|---|
|5<br>RXAMS|MTL Rx Memory Address Mismatch Status<br>Indicates whether the MTL Rx memory address mismatch status is detected.<br>When this field is 1, it indicates that an address mismatch is found for MTL Rx memory's address bus.<br>0b - Not detected<br>1b - Detected|
|4<br>RXCES|MTL Rx memory Correctable Error Status<br>Indicates whether the MTL Rx memory correctable error status is detected.<br>When this field is 1, it indicates that a correctable error is detected at the MTL Rx memory.<br>0b - Not detected<br>1b - Detected|
|3<br>—|Reserved.|
|2<br>TXUES|MTL Tx Memory Uncorrectable Error Status<br>Indicates whether the MTL Tx memory uncorrectable error status is detected.<br>When this field is 1, it indicates that an uncorrectable error is detected at the MTL TX memory interface.<br>0b - Not detected<br>1b - Detected|
|1<br>TXAMS|MTL Tx Memory Address Mismatch Status<br>Indicates whether the MTL Tx memory address mismatch status is detected.<br>When this field is 1, it indicates that an address mismatch is found for MTL Tx memory's address bus.<br>0b - Not detected<br>1b - Detected|
|0<br>TXCES|MTL Tx Memory Correctable Error Status<br>Indicates whether the MTL Tx memory correctable error status is detected.<br>When this field is 1, it indicates that a correctable error is detected at the MTL Tx memory.<br>0b - Not detected|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3291 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - Detected|



# 74.7.211 MTL ECC Error Status (MTL_ECC_Err_Sts_Rctl) 

## Offset 

|Register|Offset|
|---|---|
|MTL_ECC_Err_Sts_Rctl|CD0h|



Function 

Establishes the control for ECC error status capture. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3292-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R EESR<br>Reserved  CUES  CCES  EMS<br>W E<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-6|Reserved.|
|—||
|5|Clear Uncorrectable Error Status|
|CUES|Indicates whether the clear uncorrectable error status is detected.<br>When this field andMTL_ECC_Err_Sts_Rctl[EESRE]is 1, it indicates that based on the<br>MTL_ECC_Err_Sts_Rctl[EMS], the respective memory's uncorrectable error address and uncorrectable<br>error count values are cleared upon reading.|
||When all the error status values are cleared hardware resets this field.<br>0b - Not detected<br>1b - Detected|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3292 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|4|Clear Correctable Error Status|
|CCES|Indicates whether the clear correctable error status is detected.<br>When this field andMTL_ECC_Err_Sts_Rctl[EESRE]is 1, it indicates that based on the<br>MTL_ECC_Err_Sts_Rctl[EMS],, the respective memory's correctable error address and correctable error<br>count values are cleared upon reading.<br>When all the error status values are cleared, hardware resets this field.<br>0b - Not detected<br>1b - Detected|
|3-1<br>EMS|MTL ECC Memory Selection<br>Provides the memory selection encoding.<br>WhenMTL_ECC_Err_Sts_Rctl[EESRE]is 1, this field indicates which memory's error status value to<br>be read.|
||The memory selection encoding is as described below.<br>000b - MTL Tx memory|
||001b - MTL Rx memory<br>010b - MTL EST memory<br>011b - MTL Rx Parser memory|
||100b - DMA TSO memory|
|0<br>EESRE|MTL ECC Error Status Read Enable<br>Indicates whether the MTL ECC error status read is enabled.<br>When this field is 1, it indicates that based onMTL_ECC_Err_Sts_Rctl[EMS], the respective memory's error<br>status values are captured as described below:<br>• The correctable and uncorrectable error count values are captured into MTL_ECC_Err_Cnt_Status.<br>• The address location of correctable and uncorrectable errors are captured into<br>MTL_ECC_Err_Addr_Status.<br>When all the status values are captured into MTL_ECC_Err_Cnt_Status andMTL_ECC_Err_Addr_Status,<br>hardware resets this field.<br>0b - Disabled<br>1b - Enabled|



# 74.7.212 MTL ECC Error Adress Status (MTL_ECC_Err_Addr_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_ECC_Err_Addr_Sta|CD4h|
|tus||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3293 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Function 

Provides the memory addresses for the correctable and uncorrectable errors. 

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
|31-16|MTL ECC Uncorrectable Error Address Status|
|EUEAS|Based on theMTL_ECC_Err_Sts_Rctl[EMS], this field holds the respective memory's address locations for<br>which an uncorrectable error or address mismatch is detected.<br>WhenMTL_ECC_Control[MEEAO]= 1, this field holds the last valid address of memory for which either an<br>uncorrectable error or an address mismatch is detected.<br>WhenMTL_ECC_Control[MEEAO]= 0, this field holds the first address of the memory for which either an<br>uncorrectable error or address mismatch is detected.|
|15-0|MTL ECC Correctable Error Address Status|
|ECEAS|Based on theMTL_ECC_Err_Sts_Rctl[EMS], this field holds the respective memory's address locations for<br>which a correctable error is detected.<br>WhenMTL_ECC_Control[MEEAO]= 1, this field holds the last valid address of memory for which the<br>correctable error or address mismatch is detected.<br>WhenMTL_ECC_Control[MEEAO]= 0, this field holds the first address of the memory for which correctable<br>error is detected.|



# 74.7.213 MTL ECC Error Control Status (MTL_ECC_Err_Cntr_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_ECC_Err_Cntr_Stat|CD8h|
|us||



## Function 

Provides ECC Error count for correctable and uncorrectable errors. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3294 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||Rese|rved|||||||EU|ECS||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||Rese|rved|||||||ECE|CS||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-20|Reserved.|
|—||
|19-16|MTL ECC Uncorrectable Error Counter Status|
|EUECS|Based on the EMS field of MTL_ECC_Err_Cntr_Rctl register, this field holds the respective memory's<br>uncorrectable error count value.|
|15-8|Reserved.|
|—||
|7-0|MTL ECC Correctable Error Counter Status|
|ECECS|Based on the EMS field of MTL_ECC_Err_Cntr_Rctl register, this field holds the respective memory's<br>correctable error count value.|



# 74.7.214 MTL DPP Control (MTL_DPP_Control) 

## Offset 

|Register|Offset|
|---|---|
|MTL_DPP_Control|CE0h|



## Function 

Establishes the operating mode of data parity protection and error injection. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3295 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 

|Bits<br>R<br>W|31|30|29|28|27|26|25|24<br>Res|23<br>erved|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|Rese|rved|Reserv<br>ed|Reserv<br>ed|IPERD|IPETD|Reserv<br>ed|IPEDD<br>C|IPEMR<br>F|IPEMT<br>S|IPEMC|IPEID|Reserv<br>ed|Reserv<br>ed|OPE|EDPP|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|1|



## Fields 

|Field|Function|
|---|---|
|31-14<br>—|Reserved.|
|13<br>—<br>12<br>—|Reserved.<br>Reserved.|
|11<br>IPERD|Insert Parity error in Rx write-back Descriptor parity generator<br>Indicates whether the insert parity error in receive write-back descriptor parity generator is enabled.<br>When this field is 1, it flips the parity bit of first valid data to which the DMA Rx write-back descriptor parity<br>generator(or at PG8 as shown in Receive data path parity protection diagram) generates.<br>0b - Disabled<br>1b - Enabled|
|10<br>IPETD|Insert Parity error in Tx write-back Descriptor parity generator<br>Indicates whether the insert parity error in transit write-back descriptor parity generator is enabled.<br>When this field is 1, it flips the parity bit of first valid data to which the DMA Tx write-back descriptor parity<br>generator(or at PG4 as shown in Transmit data path parity protection diagram) generates.<br>Hardware clears this field, when the respective parity bit flips.<br>0b - Disabled<br>1b - Enabled|
|9<br>—|Reserved.|
|8|Insert Parity Error in DMA DTX Control Word Parity Generator|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3296 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field<br>IPEDDC|Function<br>Indicates whether the insert parity error in DMA DTX control word parity generator is enabled.<br>When this field is 1, it flips the parity bit of first valid data to which the DMA DTX Control word parity generator<br>(or at PG2 as shown in Transmit data path parity protection diagram) generates.<br>Hardware clears this field, when the respective parity bit flips.<br>0b - Disabled<br>1b - Enabled|
|---|---|
|7<br>IPEMRF|Insert Parity Error in MTL Rx FIFO Read Control Parity Generator<br>Inserts parity Eerror in MTL receive FIFO read control parity generator.<br>When this field is 1, it flips the parity bit of first valid data to which the MTL Rx FIFO read control parity<br>generator (or at PG7 as shown in Receive data path parity protection diagram) generates.<br>Hardware clears this field, when the respective parity bit flips.<br>0b - Disabled<br>1b - Enabled|
|6<br>IPEMTS|Insert Parity Error in MTL Tx Status Parity Generator<br>Indicates whether the insert parity error in MTL transit status parity generator is enabled.<br>When this field is 1, it flips the parity bit of first valid data to which the MTL Tx Status parity generator (or at<br>PG6 as shown in Transmit data path parity protection diagram) generates.<br>Hardware clears this field, when the respective parity bit flips.<br>0b - Disabled<br>1b - Enabled|
|5<br>IPEMC|Insert Parity Error in MTL Checksum Parity Generator<br>Indicates whether the insert parity error in MTL checksum parity generator is enabled.<br>When this field is 1, it flips the parity bit of first valid data to which the MTL checksum parity generator (or<br>at PG5 as shown in Transmit data path parity protection diagram) generates.<br>Hardware clears this field, when the respective parity bit flips.<br>0b - Disabled<br>1b - Enabled|
|4<br>IPEID|Insert Parity Error in Interface Data Parity Generator<br>Indicates whether the insert parity error in interface data parity generator is enabled.<br>When this field is 1, it flips the parity bit of first valid input data to which the interface data parity generator<br>(or at PG1 as shown in Transmit data path parity protection diagram) generates.<br>Following are the input data bus on which parity bits are generated on the basis of configuration selected.<br>In AHB Config, hrdata_i<br>In AXI config, rdata_m_i|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3297 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||In DMA Config, mdc_rdata_i<br>In MTL Config, ati_data_i<br>Hardware clears this field, when the respective parity bit flips.<br>0b - Disabled<br>1b - Enabled|
|3<br>—|Reserved.|
|2<br>—|Reserved.|
|1|Odd Parity Enable|
|OPE|Indicates whether an odd parity protection is enabled.<br>When this field is 1, it enables an odd parity protection on all the external interfaces and when this field is<br>0, it enables an even parity protection on all the external interfaces.<br>0b - Disabled<br>1b - Enabled|
|0|Enable Data path Parity Protection|
|EDPP|Enables or disables the data path parity protection.<br>When this field is 1, it indicates that by generating and checking the parity on EQOS datapath it enables<br>the parity protection for EQOS datapath . When this field is 0, it disables the parity protection for<br>EQOS datapath.<br>0b - Disable<br>1b - Enable|



# 74.7.215 MTL Tx Queue 0 Operation Mode (MTL_TxQ0_Operation_Mode) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ0_Operation_M|D00h|
|ode||



Function 

Establishes the transmit queue operating modes and commands. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3298 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||Reserved||||||||TQS|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||||Reserved||||||TTC||TXQ|EN|TSF|FTQ|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-21|Reserved.|
|—||
|20-16<br>TQS|Transmit Queue Size<br>Indicates the size of the allocated transmit queues in blocks of 256 bytes. This field is read-write only if the<br>number of transit queues are more than one, the reset value is 0x0 and indicates 256 bytes size. This means<br>that value of 0x0 = 256 bytes, 0x1 = 512 bytes and so on. You must program TQS [5:0] = 6'b001111 to<br>allocate queue size of 4096 (4K) bytes . In general, the size of the Queue = (TQS+1)*256 bytes.<br>When the number of transit queue is one, the field is read-only and the reset value reflects the configured<br>TX FIFO size in blocks of 256 bytes.<br>The field's width depends on the transit memory size selected in your configuration. For example, if the<br>memory size is 2048, the field's width is 3 bits:<br>LOG2(2048/256) = LOG2(8) = 3 bits|
|15-7<br>—|Reserved.|
|6-4<br>TTC|Transmit Threshold Control<br>Controls the threshold level of the MTL transit queue. The transmission starts when the packet size within<br>the MTL transit queue is larger than the threshold, also transmits full packets with length less than the<br>threshold. These fields are used only whenMTL_TxQ0_Operation_Mode[TSF]resets.<br>000b - 32<br>001b - 64<br>010b - 96|
||011b - 128|
||100b - 192<br>101b - 256|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3299 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||110b - 384<br>111b - 512|
|3-2|Transmit Queue Enable|
|TXQEN|Enables or disables the transmit queue 0.<br>2'b00 - Not enabled<br>2'b01 - Reserved<br>2'b10 - Enabled<br>2'b11 - Reserved<br>This field is read only in single queue configurations and read write in multiple queue configurations.<br>In multiple transit queue configuration, all the queues disables by default and programming<br>this field enables the transit queue.<br>~~NOTE~~|
||00b - Not enabled<br>01b - Enable in AV mode (Reserved in non-AV)<br>10b - Enabled<br>11b - Reserved|
|1<br>TSF|Transmit Store and Forward<br>Indicates whether the transmit store and forward is enabled.<br>When this field is 1, it indicates that the transmission starts when a full packet resides in the MTL transit<br>queue and the TTC values specified in Bits[6:4] of this register are ignored. This field must be changed only<br>when you stop the transmission.<br>0b - Disabled<br>1b - Enabled|
|0<br>FTQ|Flush Transmit Queue<br>Indicates whether the flush transmit queue is enabled.<br>When this field is 1, it indicates that the transit queue controller logic resets to its default values. Therefore,<br>all the data in the transit queue is lost or flushed. After the flushing operation completes this field resets<br>internally. You must not write to theMTL_TxQ1_Operation_Modeuntil this field resets. The data to which<br>the MAC transmitter has already accepted is not flushed. It is scheduled for transmission and results in<br>underflow and runt packet transmission.<br>The flush operation completes only when the transit queue is empty and the application<br>accepts the pending transit status of all the transmitted packets. To complete the flush<br>operation, the PHY Tx clock (clk_tx_i) must be active.<br>~~NOTE~~|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3300 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||Access restriction apply to this field. It clears automatically. Writing 1 sets this field and writing 0 has<br>no effect.|
||0b - Disabled|
||1b - Enabled|



# 74.7.216 MTL Tx Queue 0 Underflow (MTL_TxQ0_Underflow) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ0_Underflow|D04h|



## Function 

Contains the counter for packets aborted because of transmit queue underflow and packets missed because of receive queue packet flush. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3301-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>UFCN<br>R UFFRMCNT<br>TOVF<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-12|Reserved.|
|—||
|11|Overflow Bit for Underflow Packet Counter|
|UFCNTOVF|Indicates whether the overflow is detected for underflow packet counter.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3301 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||This field is 1, when the transit queue underflow packet counter field overflows, that is, it has crossed the<br>maximum count. In such a scenario, the overflow packet counter resets to all-zeros and this field indicates<br>that the rollover occured.<br>Access restriction apply to this field. It clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|10-0|Underflow Packet Counter|
|UFFRMCNT|Indicates the number of packets aborted by the controller because of transit queue underflow. This counter<br>increments each time the MAC aborts outgoing packet because of underflow. The counter clears when this<br>register is read with mci_be_i[0] at 1'b1.<br>Access restriction apply to this field. It clears on read and automatically becomes 1 on an internal<br>event occurrence.|



# 74.7.217 MTL Tx Queue 0 Debug (MTL_TxQ0_Debug) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ0_Debug|D08h|



## Function 

Provides the debug status of various blocks related to the transmit queue. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||||Reserved||||||STXSTSF||Reserv<br>ed||PTXQ||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||Reserv|ed|||||TXSTS<br>FS...|TXQS<br>TS|TWCS<br>TS|TRC|STS|TXQP<br>AUS...|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3302 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Fields 

|Field<br>31-23<br>—|Function<br>Reserved.|
|---|---|
|22-20<br>STXSTSF|Number of Status Words in Tx Status FIFO of Queue<br>Indicates the current number of status in the transit status FIFO of this queue.<br>This field does not reflect the number of status words in transit status FIFO, when<br>MTL_Operation_Mode[DTXSTS]= 1.|
|19|Reserved.|
|—<br>18-16<br>PTXQ|Number of Packets in the Transmit Queue<br>Indicates the current number of packets in the transit queue.<br>This field does not reflect the number of packets in the transmit queue, when<br>MTL_Operation_Mode[DTXSTS]= 1.|
|15-6<br>—|Reserved.|
|5<br>TXSTSFSTS|MTL Tx Status FIFO Full Status<br>Indicates whether the MTL transit status and FIFO full status is detected.<br>When this field is 1, it indicates that the MTL transit status FIFO is full. Therefore, MTL cannot accept any<br>more packets for transmission.<br>0b - Not detected<br>1b - Detected|
|4<br>TXQSTS|MTL Tx Queue Not Empty Status<br>Indicates whether the MTL transit queue not empty status is detected.<br>When this field is high, it indicates that the MTL transit queue is not empty and some data is left<br>for transmission.<br>0b - Not detected<br>1b - Detected|
|3<br>TWCSTS|MTL Tx Queue Write Controller Status<br>Indicates whether the MTL transit queue write controller status is detected.<br>When high, this field indicates that the MTL transit queue write controller is active, and transfers the data to<br>the transit queue.<br>0b - Not detected<br>1b - Detected<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3303 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|2-1|MTL Tx Queue Read Controller Status|
|TRCSTS|Indicates the state of the transit queue read controller.<br>00b - Idle state<br>01b - Read state (transferring data to the MAC transmitter)<br>10b - Waiting for pending transit status from the MAC transmitter<br>11b - Flushing the transit queue because of the packet abort request from the MAC|
|0|Transmit Queue in Pause|
|TXQPAUSED|Indicates whether the transmit queue in pause is detected.<br>When this field is 1 and the receive flow control is enabled, it indicates that the transit queue is in the pause<br>condition (in the full-duplex only mode) because of the following scenario:<br>• Receives PFC packet with the priorities assigned to the transit queue when PFC is enabled.<br>• Receives 802.3x pause packet when PFC is disabled.<br>0b - Not detected<br>1b - Detected|



# 74.7.218 MTL Tx Queue 0 ETS Status (MTL_TxQ0_ETS_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ0_ETS_Status|D14h|



## Function 

Provides the average traffic transmitted in queue 0. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||Rese|rved|||||||AB|S||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||A|BS||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3304 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Fields 

|Field|Function|
|---|---|
|31-24|Reserved.|
|—||
|23-0|Average Bits per Slot|
|ABS|Contains the average transmitted bits per slot.|
||Computes over every 10 million bit times slot (4 ms in 2500 Mbit/s; 10 ms in 1000 Mbit/s; 100 ms in 100<br>Mbit/s), when the DCB operation enables for queue 0. The maximum value is 0x989680.|



# 74.7.219 MTL Tx Queue Quantum Weight (MTL_TxQ0_Quantum_Weight) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ0_Quantum_W|D18h|
|eight||



## Function 

Contains the quantum value for Deficit Weighted Round Robin (DWRR), weights for the Weighted Round Robin (WRR), and Weighted Fair Queuing (WFQ) for queue 0. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||Reserved||||||||ISCQW|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||ISC|QW||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-21<br>—|Reserved.|
|20-0|Quantum or Weights|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3305 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|ISCQW|Contains the quantum value in bytes which is added to credit during every queue scanning cycle, when DCB<br>operation enables with DWRR algorithm for queue 0 traffic. The maximum value is 0x1312D0 bytes.<br>Contains the weight for this queue, when DCB operation enables with WFQ algorithm for queue 0 traffic. The<br>maximum value is 0x3FFF where weight of 0 indicates 100% bandwidth. Write 0 to bits[20:14]. The higher<br>the programmed weights, the lesser is the bandwidth that is allocated for the particular transmit queue. This<br>is because the weights compute the packet finish time (weights*packet_size). The lesser the finish time, the<br>higher is the probability of the packet getting scheduled first and consuming more bandwidth.<br>Contains the weight for this queue, when DCB operation or generic queuing operation enables with WRR<br>algorithm for queue 0 traffic. The maximum value is 0x64.<br>Write 0 to bits [20:7].|



# 74.7.220 MTL Queue 0 Interrupt Control Status (MTL_Q0_Interrupt_Control_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_Q0_Interrupt_Contr|D2Ch|
|ol_Status||



## Function 

Contains the interrupt enable and status bits for the queue 0 interrupts. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||Reserved||||RXOIE||||Reserved||||RXOV<br>FIS|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||Res|erved|||ABPSI<br>E|TXUIE|||Res|erved|||ABPSI<br>S|TXUN<br>FIS|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function|
|---|---|
|31-25<br>—|Reserved.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3306 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|24<br>RXOIE|Receive Queue Overflow Interrupt Enable<br>Enables or disables the receive queue overflow interrupt.<br>When this field is 1, it enables the receive queue overflow interrupt.<br>When this field becomes 0, it disables the receive queue overflow interrupt.<br>0b - Disabled<br>1b - Enabled|
|23-17<br>—|Reserved.|
|16|Receive Queue Overflow Interrupt Status|
|RXOVFIS|Indicates whether the status of receive queue overflow interrupt is detected.<br>This bit indicates that the receive queue had an overflow when you receive the packet. If you transfer a<br>partial packet to the application, the overflow status sets in RDES3[21]. This fiels is 0 when the application<br>writes 1 to it.<br>Access restriction apply to this field. It becomes 0 automatically on an internal event occurrence. Writing 1<br>clears this field and writing 0 has no effect.<br>0b - Not detected<br>1b - Detected|
|15-10<br>—|Reserved.|
|9<br>ABPSIE|Average Bits Per Slot Interrupt Enable<br>Enables or disables the average bits per slot interrupt.<br>When this field is 1, it indicates that when you update the average bits per slot status, the MAC asserts the<br>sbd_intr_o or mci_intr_o interrupt.<br>When this field is 0, it indicates that the interrupt do not assert for such an event.<br>0b - Disabled<br>1b - Enabled|
|8<br>TXUIE|Transmit Queue Underflow Interrupt Enable<br>Enables or disables transmit queue underflow interrupt.<br>When this field is 1, it enables the transmit queue underflow interrupt.<br>When this field becomes 0, it disables the transmit queue underflow interrupt.<br>0b - Disabled<br>1b - Enabled|
|7-2|Reserved.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3307 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|1<br>ABPSIS|Average Bits Per Slot Interrupt Status<br>Indicates whether the status of average bits per slot interrupt is detected.<br>When this field is 1, it indicates that the MAC has updated the ABS value. This field is 0 when the application<br>writes 1 it.<br>Access restriction apply to this field. It becomes 0 automatically on an internal event occurrence. Writing 1<br>sets this field and writing 0 has no effect.<br>0b - Not detected<br>1b - Detected|
|0|Transmit Queue Underflow Interrupt Status|
|TXUNFIS|Indicates whether the status of transmit queue underflow interrupt is detected.<br>This field indicates that, when you transmit the packet,the transmit queue had an underflow. Suspend the<br>transmission and write 1 to an underflow error TDES3[2].<br>This field is 0, when the application writes 1 to it.<br>Access restriction apply to this field. It becomes 0 automatically on an internal event occurrence. Writing 1<br>sets this field and writing 0 has no effect.<br>0b - Not detected<br>1b - Detected|



# 74.7.221 MTL Rx Queue 0 Operation Mode (MTL_RxQ0_Operation_Mode) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RxQ0_Operation_|D30h|
|Mode||



## Function 

Establishes the receive queue operating modes and command. 

The RFA and RFD fields are not backward compatible with the RFA and RFD fields of 4.00a release 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3308 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3309-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved  RQS  Reserved  RFD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DIS_T Reserv<br>RFD  Reserved  RFA  EHFC  RSF  FEP  FUP  RTC<br>W CP... ed<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-25|Reserved.|
|—||
|24-20|Receive Queue Size|
|RQS|Indicates the size of the allocated receive queues in blocks of 256 bytes. The<br>MTL_RxQ0_Operation_Mode[RQS]is read-write only if the number of receive queues are more than<br>one, the reset value is 0x0 and indicates size of 256 bytes. This means that value of 0x0 = 256 bytes, 0x1 =<br>512 bytes and so on. You must program RQS [5:0] = 6'b001111 to allocate queue size of 4096 (4K) bytes.<br>In general, the size of the Queue = (RQS+1)*256 bytes.<br>When the number of receive queues is one, the field is read-only and the configured receive FIFO size in<br>blocks of 256 bytes is reflected in the reset value.<br>The field width depends on the receive memory size selected in your configuration. For example, if the<br>memory size is 2048, the field width is 3 bits:<br>LOG2(2048/256) = LOG2(8) = 3 bits|
|19-18<br>—<br>17-14<br>RFD|Reserved.<br>Threshold for Deactivating Flow Control (in half-duplex and full-duplex modes)<br>Controls the threshold (fill-level of Rx queue) at which the flow control is de-asserts after activation.<br>0 - Full minus 1 KB, that is, FULL 1 KB<br>1 - Full minus 1.5 KB, that is, FULL 1.5 KB<br>2 - Full minus 2 KB, that is, FULL 2 KB<br>3 - Full minus 2.5 KB, that is, FULL 2.5 KB<br>...<br>14 - Full minus 8 KB, that is, FULL 8 KB<br>15 - Full minus 8.5 KB, that is, FULL 8.5 KB|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3309 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function<br>De-assertion is effective only after flow control is asserted.<br>You must program the value in such a way that the threshold is a positive number.<br>~~NOTE~~<br>WhenMTL_RxQ0_Operation_Mode[EHFC]= 1, these values are applicable only when the receive queue<br>size which theMTL_RxQ0_Operation_Mode[RQS]determines is equal to or greater than 4 KB.<br>For a given queue size, the values ranges between 0 and the encoding for FULL minus (QSIZE - 0.5<br>KB) and all other values are illegal. Here the term FULL and QSIZE refers to the queue size which the<br>MTL_RxQ0_Operation_Mode[RQS]determines.<br>The field width depends on RX FIFO size selected during the configuration. Remaining bits are reserved and<br>read only.|
|---|---|
|13-12<br>—|Reserved.|
|11-8<br>RFA|Threshold for Activating Flow Control (in half-duplex and full-duplex)<br>Controls the threshold (fill-level of receive queue) at which the flow control is activated.<br>SeeMTL_RxQ0_Operation_Mode[RFD]for more information on encoding for this field.|
|7<br>EHFC|Enable Hardware Flow Control<br>Enables or disables hardware flow control.<br>If this field is 1, it enables the flow control signal operation, on the basis of the fill-level of receive queue.<br>When this field becomes 0, it disables the flow control operation.<br>0b - Disable<br>1b - Enable|
|6<br>DIS_TCP_EF|Disable Dropping of TCP/IP Checksum Error Packets<br>Enables or disable dropping of TCP or IP checksum error packets.<br>When this field is 1, it indicates that the MAC does not drop the packets which only have the errors which<br>the receive checksum offload engine detects. Such packets have errors only in the encapsulated payload.<br>There are no errors (including FCS error) in the Ethernet packet received by the MAC.<br>When this field becomes 0, it indicates that all error packets are dropped if<br>MTL_RxQ0_Operation_Mode[FEP]resets.<br>0b - Enable<br>1b - Disable|
|5<br>RSF|Receive Queue Store and Forward<br>Indicates whether the receive queue store and forward is enabled.<br>When this field is 1, it indicates that the module reads a packet from the receive queue only after the<br>complete packet has been written to it, ignores theMTL_RxQ0_Operation_Mode[RTC].|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3310 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function<br>When this field becomes 0, it indicates that the receive queue operates in the Threshold (cut-through) mode,<br>subject to the threshold which theMTL_RxQ0_Operation_Mode[RTC]specifies.<br>0b - Disabled<br>1b - Enabled|
|---|---|
|4<br>FEP|Forward Error Packets<br>Indicates whether the forward error packets are enabled.<br>When this field becomes 0, it indicates that the receive queue drop packets with an error status (CRC error,<br>GMII_ER, watchdog timeout, or overflow). However, the packet does not drop if the start byte (write) pointer<br>of a packet is already transferred to the read controller side (in Threshold mode).<br>When this field is 1, it indicates that all packets except the runt error packets are forwarded<br>to the application or DMA. The packet is dropped irrespective of the setting of this field, if<br>MTL_RxQ0_Operation_Mode[RSF]is 1 and the receive queue overflows when a partial packet is written.<br>However, ifMTL_RxQ0_Operation_Mode[RSF]becomes 0 and the receive queue overflows when a partial<br>packet is written, a partial packet might be forwarded to the application or DMA.<br>0b - Disabled<br>1b - Enabled|
|3<br>FUP|Forward Undersized Good Packets<br>Indicates whether the forward undersized good packets are enabled.<br>When this field is 1, it indicates that the receive queue forwards the undersized good packets (packets with<br>no error and length less than 64 bytes), including pad-bytes and CRC.<br>When this field becomes 0, it indicates that the receive queue drops all packets of less than 64 bytes,<br>unless a packet is already transferred because of the lower value of receive threshold, for example,<br>MTL_RxQ0_Operation_Mode[RTC]= 01.<br>0b - Disabled<br>1b - Enabled|
|2<br>—|Reserved.|
|1-0<br>RTC|Receive Queue Threshold Control<br>Controls the threshold level of the MTL receive queue (in bytes).<br>The received packet is transferred to the application or DMA when the packet size within the MTL receive<br>queue is larger than the threshold. In addition, automatically tranfer full packets with length less than<br>the threshold.<br>This field is valid only whenMTL_RxQ0_Operation_Mode[RSF]= 0.<br>This field is ignored whenMTL_RxQ0_Operation_Mode[RSF]= 1.<br>00b - 64|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3311 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||01b - 32|
||10b - 96|
||11b - 128|



# 74.7.222 MTL Rx Queue Missed Packet Overflow Count (MTL_RxQ0_Missed_Packet_Overflow_Cnt) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RxQ0_Missed_Pac|D34h|
|ket_Overflow_Cnt||



## Function 

Contains the counter for packets missed because of receive queue packet flush and packets discarded because of receive queue overflow. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Reser|ved||MISCN<br>TO...|||||MI|SPKTCNT||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||Reser|ved||OVFC<br>NTO...|||||OV|FPKTCNT||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-28|Reserved.|
|—||
|27|Missed Packet Counter Overflow Bit|
|MISCNTOVF|Indicates whether the missed packet counter overflow is detected.|
||When this field is 1, it indicates that the receive queue missed packet counter has crossed the<br>maximum limit.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3312 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||Access restriction apply to this field. It clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|26-16<br>MISPKTCNT|Missed Packet Counter<br>Indicates the number of packets this module has missed because the application asserts ari_pkt_flush_i[]<br>for this queue. This counter resets when this register reads with mci_be_i[0] at 1b1.<br>This counter increments by 1 when the DMA discards the packet because of buffer unavailability.<br>Access restriction apply to this field. It clears on read and automatically becomes 1 on an internal<br>event occurrence.|
|15-12<br>—|Reserved.|
|11<br>OVFCNTOVF|Overflow Counter Overflow Bit<br>Indicates whether the counter overflow is detected.<br>When this field is 1, it indicates that the receive queue overflow packet counter field has crossed the<br>maximum limit.<br>Access restriction apply to this field. It clears on read and automatically becomes 1 on an internal<br>event occurrence.<br>0b - Not detected<br>1b - Detected|
|10-0<br>OVFPKTCNT|Overflow Packet Counter<br>Indicates the number of packets which this module discards because of receive queue overflow. This<br>counter increments each time the module discards an incoming packet because of overflow. This counter<br>resets when this register reads with mci_be_i[0] at 1'b1.<br>Access restriction apply to this field. It clears on read and automatically becomes 1 on an internal<br>event occurrence.|



# 74.7.223 MTL Rx Queue 0 Debug (MTL_RxQ0_Debug) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RxQ0_Debug|D38h|



## Function 

Provides the debug status of various blocks related to the receive queue. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3313 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|Rese|rved|||||||PR|XQ|||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||Rese|rved|||||RXQ|STS|Reserv<br>d|RRC|STS|RWCS<br>TS|
|W|||||||||||||e||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-30|Reserved.|
|—||
|29-16<br>PRXQ|Number of Packets in Receive Queue<br>Indicates the current number of packets in the receive queue. The theoretical maximum value for this field<br>is 256KB/16B = 16K packets, that is, Max_Queue_Size/Min_Packet_Size.|
|15-6|Reserved.|
|—<br>5-4|MTL Rx Queue Fill-Level Status|
|RXQSTS|Provides the status of the receive queue fill-level.<br>00b - Rx Queue empty<br>01b - Rx Queue fill-level below flow-control deactivate threshold<br>10b - Rx Queue fill-level above flow-control activate threshold<br>11b - Rx Queue full|
|3<br>—<br>2-1<br>RRCSTS|Reserved.<br>MTL Rx Queue Read Controller State<br>Provides the state of the receive queue read controller.<br>00b - Idle state<br>01b - Reading packet data<br>10b - Reading packet status (or timestamp)<br>11b - Flushing the packet data and status<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3314 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|0|MTL Rx Queue Write Controller Active Status|
|RWCSTS|Indicates whether the MTL receive queue write controller active status is detected.|
||When high, this bit indicates that the MTL receive queue write controller is active, and it is transferring a<br>received packet to the receive queue.|
||0b - Not detected|
||1b - Detected|



# 74.7.224 MTL Rx Queue 0 Control 0 (MTL_RxQ0_Control) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RxQ0_Control|D3Ch|



## Function 

Controls the receive arbitration and passing of received packets to the application. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||Rese|rved|||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R<br>W||||||Rese|rved||||||RXQ_F<br>RM...|R|XQ_WEGT|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



## Fields 

|Field|Function|
|---|---|
|31-4<br>—|Reserved.|
|3|Receive Queue Packet Arbitration|
|RXQ_FRM_AR<br>BIT|Indicates whether the receive queue packet arbitration is enabled.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3315 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||When this field is 1, it indicates that the module drives the packet data to the ARI interface such that the entire<br>packet data of currently-selected queue transmits before switching to other queue.<br>When this field becomes 0, it indicates that the module drives the packet data to the ARI interface such that<br>the following amount of data of currently-selected queue transmits before switching to other queue:<br>• PBL amount of data (indicated by ari_qN_pbl_i[]), or<br>• Complete data of a packet<br>The status and the timestamp are not a part of the PBL data. Therefore, the module drives the complete<br>status (including timestamp status) during first PBL request for the packet (in store-and-forward mode) or<br>the last PBL request for the packet (in Threshold mode).<br>0b - Disabled<br>1b - Enabled|
|2-0<br>RXQ_WEGT|Receive Queue Weight<br>Indicates the weight assigned to receive queue 0.<br>You must write a value to this field that is 1 less than the required queue weight. Therefore, if this field is 0,<br>it indicates that the queue weight is 1, if this field is 1, it indicates that the queue weight is 2, and so on. You<br>must use this weight to calculate the number of continuous PBL or packet requests, depending on the value<br>ofRXQ_FRM_ARBIT, allocated to the queue in an arbitration cycle.<br>The field's value changes when the current service round completes or when there is a change from<br>RAA=SP to RAA=WSP algorithm. This approach is required for a smooth transition. You must configure<br>MTL Rx Queue 0 Control 0 (MTL_RxQ0_Control)beforeMTL Operation Mode (MTL_Operation_Mode)if<br>you want to change the field's value before either of these two processes completes.|



# 74.7.225 MTL Tx Queue 1 Operation Mode (MTL_TxQ1_Operation_Mode) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ1_Operation_M|D40h|
|ode||



## Function 

Establishes the transmit queue operating modes and commands. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3316 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||Reserved||||||||TQS|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||||Reserved||||||TTC||TXQ|EN|TSF|FTQ|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-21|Reserved.|
|—||
|20-16<br>TQS|Transmit Queue Size<br>Indicates the size of the allocated transmit queues in blocks of 256 bytes. This field is read-write only if the<br>number of transit queues is more than one, the reset value is 0x0 and indicates size of 256 bytes. This<br>means that value of 0x0 = 256 bytes, 0x1 = 512 bytes and so on. You must program TQS [5:0] = 6'b001111<br>to allocate queue size of 4096 (4K) bytes. In general, the size of the queue = (TQS+1)*256 bytes.<br>When the number of transit queues is one, the field is read-only and the reset value reflects the configured<br>TX FIFO size in blocks of 256 bytes.<br>The field width depends on the transit memory size selected in your configuration. For example, if the<br>memory size is 2048, the field width is 3 bits:<br>LOG2(2048/256) = LOG2(8) = 3 bits|
|15-7<br>—|Reserved.|
|6-4<br>TTC|Transmit Threshold Control<br>Controls the threshold level of the MTL Tx Queue. The transmission starts when the packet size within the<br>MTL Tx Queue is larger than the threshold. In addition, it also transmit full packets with length less than the<br>threshold. These fields are used only when theMTL_TxQ1_Operation_Mode[TSF]resets.<br>000b - 32<br>001b - 64<br>010b - 96|
||011b - 128|
||100b - 192<br>101b - 256|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3317 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3318-03.png)


<!-- Start of picture text -->
Field Function<br>110b - 384<br>111b - 512<br>3-2 Transmit Queue Enable<br>TXQEN Enables or disables the transmit queue 0.<br>2'b00 - Not enabled<br>2'b01 - Enable in AV mode<br>2'b10 - Enabled<br>2'b11 - Reserved<br>  NOTE<br>All the queues disables by default, in multiple transit queues configuration. You must<br>program this field to enable the transit queue.<br>00b - Not enabled<br>01b - Enable in AV mode (Reserved in non-AV)<br>10b - Enabled<br>11b - Reserved<br>1 Transmit Store and Forward<br>TSF Indicates whether the transmit store and forward is enabled.<br>When this field is 1, it indicates that the transmission starts when full packet resides in the MTL transit queue<br>and the TTC values specified in MTL_TxQ1_Operation_Mode[TTC] are ignored. This field must change only<br>when the transmission stops.<br>0b - Transmit Store and Forward is disabled<br>1b - Transmit Store and Forward is enabled<br>0 Flush Transmit Queue<br>FTQ Indicates whether the flush transmit queue is enabled.<br>When this field is 1, it indicates that the transmit queue controller logic resets to its default values. Therefore,<br>all the data in the transit queue is lost or flushed. This field resets internally when the flushing operation<br>completes. Until this field becomes 0, you must not write to MTL_TxQ1_Operation_Mode. The data which<br>the MAC transmitter has already accepted is not flushed. It is scheduled for transmission and results in an<br>underflow and runt packet transmission.<br>  NOTE<br>The flush operation completes only when the transit queue is empty and the application<br>has accepted the pending transit status of all transmitted packets. To complete this flush<br>operation, the PHY Tx clock (clk_tx_i) must be active.<br>Access restriction apply to this field. Writing 1 sets this field and it clears automatically. Writing 0 has<br>no effect.<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3318 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Disabled|
||1b - Enabled|



# 74.7.226 MTL Tx Queue 1 Underflow (MTL_TxQ1_Underflow) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ1_Underflow|D44h|



## Function 

Contains the counter for packets aborted because of transmit queue underflow and packets missed because of receive queue packet flush. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3319-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>UFCN<br>R UFFRMCNT<br>TOVF<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-12|Reserved.|
|—||
|11|Overflow Bit for Underflow Packet Counter|
|UFCNTOVF|Indicates whether the overflow is detected for underflow packet counter.|
||When this field is 1, it indicates that every time the transit queue underflow packet counter field overflows,<br>that is, it has crossed the maximum count. In such case, the overflow packet counter resets to all-zeros and<br>this field indicates that the rollover have occurred.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3319 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||Access restriction apply to this field. It clears on read and automatically becomes 1 on an internal<br>event occurrence.|
||0b - Not detected|
||1b - Detected|
|10-0|Underflow Packet Counter|
|UFFRMCNT|Indicates the number of packets which the controller abort because of transit queue underflow. This counter<br>increments each time the MAC aborts outgoing packet because of underflow. The counter clears when this<br>register is read with mci_be_i[0] at 1'b1.<br>Access restriction apply to this field. It clears on read and automatically becomes 1 on an internal<br>event occurrence.|



# 74.7.227 MTL Tx Queue 1 Debug (MTL_TxQ1_Debug) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ1_Debug|D48h|



## Function 

Provides the debug status of various blocks related to the transmit queue. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||||Reserved||||||STXSTSF||Reserv<br>ed||PTXQ||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||Reserv|ed|||||TXSTS<br>FS...|TXQS<br>TS|TWCS<br>TS|TRC|STS|TXQP<br>AUS...|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function||
|---|---|---|
|31-23|Reserved.||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3320 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|—<br>22-20<br>STXSTSF|Number of Status Words in Tx Status FIFO of Queue<br>Indicates the current number of status in the transit status FIFO of this queue.<br>WhenMTL_Operation_Mode[DTXSTS]= 1, this field does not reflect the number of status words in transit<br>status FIFO.|
|19<br>—|Reserved.|
|18-16<br>PTXQ|Number of Packets in the Transmit Queue<br>Indicates the current number of packets in the transit queue.<br>WhenMTL_Operation_Mode[DTXSTS]= 1, this field does not reflect the number of packets in the<br>transmit queue.|
|15-6<br>—|Reserved.|
|5<br>TXSTSFSTS|MTL Tx Status FIFO Full Status<br>Indicates whether the MTL transit status FIFO full status is detected.<br>When this field is 1, it indicates that the MTL transit status FIFO is full. Therefore, the MTL cannot accept<br>any more packets for transmission.<br>0b - Not detected<br>1b - Detected|
|4<br>TXQSTS|MTL Tx Queue Not Empty Status<br>Indicates whether the MTL transit queue not empty status is detected.<br>When this field is 1, it indicates that the MTL transit queue is not empty and some data is left for transmission.<br>0b - Not detected<br>1b - Detected|
|3<br>TWCSTS|MTL Tx Queue Write Controller Status<br>Indicates whether the MTL transit queue write controller status is detected.<br>When this field is 1, it indicates that the MTL transit queue write controller is active, and it is transferring the<br>data to the transit queue.<br>0b - Not detected<br>1b - Detected|
|2-1|MTL Tx Queue Read Controller Status|
|TRCSTS|Indicates the state of the transit queue read controller.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3321 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||00b - Idle state<br>01b - Read state (transferring data to the MAC transmitter)<br>10b - Waiting for pending transit status from the MAC transmitter<br>11b - Flushing the transit queue because of the packet abort request from the MAC|
|0|Transmit Queue in Pause|
|TXQPAUSED|Indicates whether the transmit queue in pause status is detected.<br>When this field is 1 and the receive flow control is enabled, it indicates that the transit queue is in the pause<br>condition (in the full-duplex only mode) because of these scenarios:<br>• Reception of the PFC packet for the priorities assigned to the transit queue when PFC is enabled.<br>• Reception of 802.3x pause packet when PFC is disabled.<br>0b - Not detected<br>1b - Detected|



# 74.7.228 MTL Tx Queue 1 ETS Control (MTL_TxQ1_ETS_Control) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ1_ETS_Control|D50h|



## Function 

Controls the enhanced transmission selection operation. 

## Diagram 

|Bits<br>R<br>W|31|30|29|28|27|26|25|24<br>Rese|23<br>rved|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||||Reserved||||||SLC||CC|AVAL<br>G|Res|erved|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3322 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Fields 

|Field|Function|
|---|---|
|31-7<br>—|Reserved.|
|6-4<br>SLC|Slot Count<br>If the credit-based shaper algorithm is enabled, then you can program the number of slots (of duration<br>programmed in DMA_CH(#i)_Slot_Interval register) over which the average transmitted bits per slot,<br>provided in the MTL_TxQ(#i)_ETS_Status register, is computed for queue. The encoding is as follows:<br>000b - 1 slot<br>001b - 2 slots<br>010b - 4 slots<br>011b - 8 slots<br>100b - 16 slots<br>101b - Reserved|
|3<br>CC|Credit Control<br>Indicates whether the credit control is enabled.<br>When this field is 1, it indicates that the accumulated credit parameter in the credit-based shaper algorithm<br>logic is not reset to zero, when there is positive credit and no packet to transmit in channel 1. The credit<br>accumulates even when no packet is waiting in channel 1 and another channel is transmitting.<br>When this field becomes 0, it indicates that the accumulated credit parameter in the credit-based shaper<br>algorithm logic sets to zero, when there is positive credit and no packet to transmit in channel 1. No credit<br>accumulates when no packet is waiting in channel 1 and other channel is transmitting.<br>0b - Disabled<br>1b - Enabled|
|2<br>AVALG|AV Algorithm<br>Indicates whether the CBS algorithm is enabled.<br>If you program queue 1 for AV, this field configures the scheduling algorithm for this queue.<br>When this field is 1, it indicates that the credit based shaper algorithm (CBS) is selected for queue 1 traffic.<br>If this field becomes 0, strict priority is selected.<br>0b - Disabled<br>1b - Enabled|
|1-0<br>—|Reserved.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3323 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

# 74.7.229 MTL Tx Queue 1 ETS Status (MTL_TxQ1_ETS_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ1_ETS_Status|D54h|



## Function 

Provides the average traffic transmitted in queue 1. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||Rese|rved|||||||AB|S||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||AB|S||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-24|Reserved.|
|—||
|23-0|Average Bits per Slot|
|ABS|Contains the average transmitted bits per slot.|
||Computes this field over number of slots programmed in the MTL_TxQ(#i)_ETS_CONTROL register's SLC<br>field of, if you enables AV operation. This field's maximum value is 0x6_4000 in 100 Mbit/s, 0x3E_8000 in<br>1000 Mbit/s and 9C_4000 in 2500 Mbit/s mode respectively.|
||Computes this field over every 10 million bit times slot (4 ms in 2500 Mbit/s; 10 ms in 1000 Mbit/s; 100 ms<br>in 100 Mbit/s) when you enables DCB operation for queue. The maximum value is 0x989680.|



# 74.7.230 MTL Tx Queue 1 Quantum Weight (MTL_TxQ1_Quantum_Weight) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ1_Quantum_W|D58h|
|eight||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3324 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Function 

Provides the average traffic transmitted in queue 1. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3325-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved  ISCQW<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>ISCQW<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

## Fields 

|Field|Function|
|---|---|
|31-21|Reserved.|
|—||
|20-0|idleSlopeCredit, Quantum or Weights|
|ISCQW|idleSlopeCredit<br>Contains the idleSlopeCredit value required for the credit-based shaper algorithm for queue 1, when you<br>enables the AV feature. This is the rate of change of credit in bits per cycle (40 ns for 100 Mbit/s; 8 ns for 1000<br>Mbit/s; 3.2 ns for 2500 Mbit/s) when the credit is increasing. You must program this field with computed credit<br>in bits per cycle scaled by 1,024. The maximum value is portTransmitRate, that is, 0x2000 in 1000/2500<br>Mbit/s mode and 0x1000 in 100 Mbit/s mode. Bits[20:14] must be written to zero.<br>Quantum<br>Contains the quantum value in bytes to be added to credit during every queue scanning cycle, when<br>you enables the DCB operation with DWRR algorithm for queue 1 traffic. The maximum value is<br>0x1312D0 bytes.<br>Weights<br>Contains the weight for this queue, when you enables the DCB operation with WFQ algorithm for queue 1<br>traffic. The maximum value is 0x3FFF where weight of 0 indicates 100% bandwidth. Bits[20:14] must be<br>written to zero.<br>Contains the weight for this queue, when you enables the DCB operation or generic queuing operation with<br>WRR algorithm for queue 1 traffic. The maximum value is 0x64.<br>Bits [20:7] must be written to zero.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3325 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function||
|---|---|---|
|||In multiple Queue configuration you must program this field in respective per queue register<br>to some non-zero value when multiple queues are enabled or single queue other than Q0<br>is enabled. You must not program this field when only Q0 is enabled. In general, you must<br>program a non-zero value on both receive and transmit when WRR algorithm is selected.<br>In receive, the register is MTL_Operation_Mode register.<br>~~NOTE~~|
|||For WFQ algorithm, higher the programmed weights lesser the bandwidth allocated for that<br>transmit queue. The finish time is not a function of particular packet alone but it is according<br>to the formula: (previous_finish_time of particular Transmit Queue + (weights*packet_size))<br>~~NOTE~~|
|||The programmed weights do not correspond to the number of packets but the fraction of<br>bandwidth or time allocated for particular queue w.r.t. total BW or time.<br>~~NOTE~~|



# 74.7.231 MTL Tx Queue 1 Sendslope Credit (MTL_TxQ1_SendSlopeCredit) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ1_SendSlopeC<br>redit|D5Ch|



## Function 

Contains the sendSlope credit value required for the credit-based shaper algorithm for the queue. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||Rese|rved||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|Rese|rved|||||||SS|C|||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3326 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Fields 

|Field|Function|
|---|---|
|31-14|Reserved.|
|—||
|13-0|sendSlopeCredit Value|
|SSC|Contains the sendSlopeCredit value required for credit-based shaper algorithm for Queue 1, when you<br>enables the AV operation. This is the rate of change of credit in bits per cycle (40 ns, 8 ns and 3.2 ns for<br>100 Mbit/s, 1000 Mbit/s and 2500 Mbit/s respectively) when the credit is decreasing. You must program<br>this field with computed credit in bits per cycle scaled by 1,024. The maximum value is portTransmitRate,<br>that is, 0x2000 in 1000/2500 Mbit/s mode and 0x1000 in 100 Mbit/s mode. You must program this fiels with<br>absolute sendSlopeCredit value. The credit-based shaper logic subtracts it from the accumulated credit<br>when channel 1 is selected for transmission.|



# 74.7.232 MTL Tx Queue 1 HiCredit (MTL_TxQ1_HiCredit) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ1_HiCredit|D60h|



## Function 

Contains the hiCredit value required for the credit-based shaper algorithm for the queue. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Reserved||||||||HC|||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||H|C||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function||
|---|---|---|
|31-29<br>—|Reserved.||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3327 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|28-0|hiCredit Value|
|HC|Contains the hiCredit value required for the credit-based shaper algorithm, when you enables the AV<br>feature. This is the maximum value that you can accumulate in the credit parameter. This is specified in bits<br>scaled by 1,024.|
||The maximum value is maxInterferenceSize, that is, best-effort maximum packet size (16,384 bytes or<br>131,072 bits). The specified value is 131,072 * 1,024 = 134,217,728 or 0x0800_0000.|



# 74.7.233 MTL Tx Queue 1 LoCredit (MTL_TxQ1_LoCredit) 

## Offset 

|Register|Offset|
|---|---|
|MTL_TxQ1_LoCredit|D64h|



## Function 

Contains the loCredit value required for the credit-based shaper algorithm for the queue. 

## Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/074_Ethernet_Media_Access_Controller_-EMAC-_part2/S32K3XXRM_数据表.pdf-3328-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved  LC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>LC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-29|Reserved.|
|—||
|28-0|loCredit Value|
|LC|Contains the loCredit value required for the credit-based shaper algorithm, when you enables the AV<br>operation. This is the minimum value that you can accumulate in the credit parameter. This is specified in bits<br>scaled by 1,024. The maximum value you can program corresponds to twice the maxFrameSize this queue<br>transmits. If the maxFrameSize is 8192 bytes, then (8192*2) * 8 * 1024 = 134,217,728 or 0x0800_0000. The<br>programmed value is 2's complement of the value, that is, 0x1800_0000 because it is a negative value.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3328 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

# 74.7.234 MTL Queue 1 Interrupt Control Status (MTL_Q1_Interrupt_Control_Status) 

## Offset 

|Register|Offset|
|---|---|
|MTL_Q1_Interrupt_Contr|D6Ch|
|ol_Status||



## Function 

Contains the interrupt enable and status bits for the queue 1 interrupts. 

## Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||Reserved||||RXOIE||||Reserved||||RXOV<br>FIS|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||Res|erved|||ABPSI<br>E|TXUIE|||Res|erved|||ABPSI<br>S|TXUN<br>FIS|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



## Fields 

|Field|Function|
|---|---|
|31-25<br>—|Reserved.|
|24<br>RXOIE|Receive Queue Overflow Interrupt Enable<br>Enables or disables the receive queue overflow interrupt.<br>When this field is 1, it enables the receive queue overflow interrupt.<br>When this field becomes 0, it disables the receive queue overflow interrupt.<br>0b - Disable<br>1b - Enable|
|23-17<br>—|Reserved.|
|16|Receive Queue Overflow Interrupt Status|
|RXOVFIS|Indicates whether the status of receive queue overflow interrupt is detected.<br>Indicates that the receive queue had an overflow when it receives the packet. If you transfers a partial packet<br>to the application, the overflow status sets in RDES3[21]. This field is 0 when the application writes 1 to it.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3329 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function<br>Access restriction apply to this field. It automatically becomes 1 on an internal event occurrence. Writing 1<br>clears this field and writing 0 has no effect.<br>0b - Not detected<br>1b - Detected|
|---|---|
|15-10<br>—|Reserved.|
|9<br>ABPSIE|Average Bits Per Slot Interrupt Enable<br>Indicates whether an average bits per slot interrupt is enabled.<br>When this field is 1, it indicates that the MAC asserts the sbd_intr_o or mci_intr_o interrupt when you update<br>the average bits per slot status.<br>When this field is 0, it indicates that the interrupt is not asserted for such an event.<br>0b - Disabled<br>1b - Enabled|
|8<br>TXUIE|Transmit Queue Underflow Interrupt Enable<br>Enables or disables the transmit queue underflow interrupt.<br>When this field is 1, it enables the transmit queue underflow interrupt.<br>When this field becomes 0, it disables the transmit queue underflow interrupt.<br>0b - Disabled<br>1b - Enabled|
|7-2<br>—|Reserved.|
|1<br>ABPSIS|Average Bits Per Slot Interrupt Status<br>Indicates whether the average bits per slot interrupt status is detected.<br>When this field is 1, it indicates that the MAC has updated the ABS value. This field is 0 when the application<br>writes 1 to it.<br>Access restriction apply to this field. It automatically becomes 1 on an internal event occurrence. Writing 1<br>clears this field and writing 0 has no effect.<br>0b - Not detected<br>1b - Detected|
|0<br>TXUNFIS|Transmit Queue Underflow Interrupt Status<br>Indicates whether the transmit queue underflow interrupt status is detected.<br>Indicates that the transmit queue had an underflow when you transmits the packet. Suspends the<br>transmission and sets an underflow error TDES3[2]. This field is 0 when the application writes 1 to this field.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3330 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
||Access restriction apply to this field. It automatically becomes 1 on an internal event occurrence. Writting 1<br>clears this field and writing 0 has no effect.|
||0b - Not detected|
||1b - Detected|



# 74.7.235 MTL Rx Queue 1 Operation Mode (MTL_RxQ1_Operation_Mode) 

## Offset 

|Register|Offset|
|---|---|
|MTL_RxQ1_Operation_|D70h|
|Mode||



## Function 

Establishes the receive queue operating modes and command. 

The MTL_RxQ1_Operation_Mode[RFA] and MTL_RxQ1_Operation_Mode[RFD] are not backward compatible with the RFA and RFD fields of 4.00a release. 

## Diagram 

|Bits|31<br>30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||Reserved||||||RQS|||Res|erved|RFD|
|Reset|0<br>0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15<br>14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R<br>W|RFD|Res|erved||RFA|||EHFC|DIS_T<br>CP...|RSF|FEP|FUP|Reserv<br>ed|RTC|
|Reset|0<br>0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



Fields 

|Field|Function|
|---|---|
|31-25|Reserved.|
|—||
|24-20|Receive Queue Size|
|RQS|Indicates the size of the allocated receive queues in blocks of 256 bytes.<br>MTL_RxQ1_Operation_Mode[RQS]is read-write only if the number of receive queues is more than one, the|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3331 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function<br>reset value is 0x0 and indicates 256 bytes size. This means that value of 0x0 = 256 bytes, 0x1 = 512 bytes<br>and so on. You must program RQS [5:0] = 6'b001111 to allocate queue size of 4096 (4K) bytes. In general,<br>the size of the Queue = (RQS+1)*256 bytes.<br>When the number of receive queues is one, the field is read-only and the reset value reflects the configured<br>RX FIFO size in blocks of 256 bytes.<br>The field width depends on the receive memory size selected in your configuration. For example, if the<br>memory size is 2048, the field width is 3 bits:<br>LOG2(2048/256) = LOG2(8) = 3 bits|
|---|---|
|19-18<br>—|Reserved.|
|17-14<br>RFD|Threshold for Deactivating Flow Control (in half-duplex and full-duplex modes)<br>Controls the threshold (fill-level of Rx queue) at which the flow control de-asserts after activation<br>0 - Full minus 1 KB, that is, FULL 1 KB<br>1 - Full minus 1.5 KB, that is, FULL 1.5 KB<br>2 - Full minus 2 KB, that is, FULL 2 KB<br>3 -Full minus 2.5 KB, that is, FULL 2.5 KB<br>...<br>14 - Full minus 8 KB, that is, FULL 8 KB<br>15 - Full minus 8.5 KB, that is, FULL 8.5 KB<br>The de-assertion is effective only when flow control asserts.<br>Program the value in such a way that the threshold is a positive number.<br>~~NOTE~~<br>WhenMTL_RxQ1_Operation_Mode[EHFC]= 1, these values are applicable only when the receive queue<br>size whichMTL_RxQ1_Operation_Mode[RQS]determines, is equal to or greater than 4 KB.<br>For a given queue size, the values ranges between 0 and the encoding for FULL minus (QSIZE - 0.5<br>KB) and all other values are illegal. Here the term FULL and QSIZE refers to the queue size which<br>MTL_RxQ1_Operation_Mode[RQS]determines.<br>The field width depends on RX FIFO size selected during the configuration. Remaining bits are reserved and<br>read only.|
|13-12<br>—|Reserved.|
|11-8|Threshold for Activating Flow Control (in half-duplex and full-duplex|
|RFA|Controls the threshold (fill-level of Rx queue) at which the flow control activates.|
||SeeMTL_RxQ1_Operation_Mode[RFD], for more information on encoding for this field.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3332 / 4640 

NXP Semiconductors 

Ethernet Media Access Controller (EMAC) 

## Table continued from the previous page... 

|Field|Function|
|---|---|
|7<br>EHFC|Enable Hardware Flow Control<br>Enables or disables hardware flow control.<br>If this field is 1, it enables the flow control signal operation, based on the receive queue's fill-level.<br>When this field becomes 0, it disables the flow control operation.<br>0b - Disable<br>1b - Enable|
|6<br>DIS_TCP_EF|Disable Dropping of TCP or IP Checksum Error Packets<br>Indicates whether the dropping of TCP or IP checksum error packets is enabled.<br>When this field is 1, it indicates that the MAC does not drop the packets which only have the errors that the<br>receive checksum offload engine detects. Such packets have errors only in the encapsulated payload. MAC<br>receives an Ethernet packet in which there are no errors (including FCS error).<br>When this field becomes 0, it indicates that all the error packets drop if<br>MTL_RxQ1_Operation_Mode[FEP]resets.<br>0b - Enabled<br>1b - Disabled|
|5<br>RSF|Receive Queue Store and Forward<br>Indicates whether the receive queue store and forward is enabled.<br>When this field is 1, it indicates that the module reads a packet from the receive queue only after the<br>complete packet is written to it and ignoresMTL_RxQ1_Operation_Mode[RTC].<br>When this field becomes 0, it indicates that the receive queue operates in the Threshold (cut-through) mode,<br>subject to the threshold whichMTL_RxQ1_Operation_Mode[RTC]specifies.<br>0b - Disabled<br>1b - Enabled|
|4<br>FEP|Forward Error Packets<br>Indicates whether the forward error packets are enabled.<br>If this field becomes 0, it indicates that the receive queue drops the packets with an error status (CRC<br>error, GMII_ER, watchdog timeout, or overflow). However, the packet does not drops, if the start byte (write)<br>pointer of a packet is already transferred to the read controller side in Threshold mode.<br>When this field is 1, it indicates that all the packets except the runt error packets forward to the<br>application or DMA. IfMTL_RxQ1_Operation_Mode[RSF]is 1 and the receive queue overflows when<br>a partial packet is written, the packet drops irrespective of the setting of this field. However, if<br>MTL_RxQ1_Operation_Mode[RSF]resets and the receive queue overflows when a partial packet is written,<br>you may forward a partial packet to the application or DMA.<br>0b - Disabled<br>1b - Enabled|
|3|Forward Undersized Good Packets|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

3333 / 4640 

