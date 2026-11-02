NXP Semiconductors 

# Chapter 48 Error Injection Module (EIM) 

## 48.1 Chip-specific EIM information 

### 48.1.1 EIM instances 

This chip supports up to three instances of EIM: 

- EIM_0 

- EIM_1 

- EIM_2 

Table 232. EIM instances 

|Instances|S32K358|S32K322/S32K324/S32K344/S32K342/S32K312/S32K311/S32K314|
|---|---|---|
|EIM_0|Yes|Yes|
|EIM_1|Yes|No|
|EIM_2|Yes|No|



### 48.1.2 EIM channel mapping 

EIM integrates with the memory controller and memory array to enable error injection in a controlled way. Each memory controller has its own EIM channel. 

Cortex-M7_1, EMAC, AIPS2 gasket, Cortex-M7 lockstep, and QuadSPI gasket are not available in the S32K312 and S32K311 product variants of the S32K3 family. 

EIM channel mapping - S32K3x1, S32K3x2, S32K3x4 

Table 233. EIM channel mapping - S32K3x1, S32K3x2, S32K3x4 

|Channel #|Target|Data bits<sup>1</sup>|Check bits<sup>1</sup>|# of data bits|# of check bits|
|---|---|---|---|---|---|
|0|SRAM0|Word1[31:0] – SRAM0<br>read data[63:32]|Word0[31:24] – SRAM0<br>read data ECC[7:0]|64|8|
|||Word2[31:0] – SRAM0<br>read data[31:0]||||
|1|SRAM1<sup>2</sup>|Word1[31:0] – SRAM1<br>read data[63:32]|Word0[31:24] SRAM1 read<br>data ECC[7:0]|64|8|
|||Word2[31:0] – SRAM1<br>read data[31:0]||||
|2|DMA TCD|Word1[31:0] – DMA TCD<br>RAM read data[63:32]|Word0[31:24] DMA<br>TCD RAM read<br>|64|8|
|||Word2[31:0] – DMA TCD<br>RAM read data[31:0]|data checkbits[7:0]|||
|3|Cortex-M7_0 IC tag|Word1[12:0] – Cortex-M7_0<br>IC tag read data1[28:16]|Word0[31:25] – Cortex-<br>M7_0 IC tag read data1[6:0]|44|14|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1607 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

Table 233. EIM channel mapping - S32K3x1, S32K3x2, S32K3x4 (continued) 

|Channel #|Target|Data bits<sup>1</sup>|Check bits<sup>1</sup>|# of data bits|# of check bits|
|---|---|---|---|---|---|
|||Word2[31:22] – Cortex-<br>M7_0 IC tag<br>read data1[15:7]||||
|||Word2[21:0] – Cortex-M7_0<br>IC tag read data0[28:7]|Word0[24:18] – Cortex-<br>M7_0 IC tag read data1[6:0]|||
|4|Cortex-M7_0 IC data|Word1[31:0] – Cortex-M7_0<br>IC data read data1[71:40]|Word0[31:24] – Cortex-<br>M7_0 IC data data1[7:0]|128|16|
|||Word2[31:0] – Cortex-M7_0<br>IC data read data1[39:8]||||
|||Word3[31:0] – Cortex-M7_0<br>IC data read data0[71:40]|Word0[23:16] – Cortex-<br>M7_0 IC data<br>|||
|||Word4[31:0] – Cortex-M7_0<br>IC data read data0[39:8]|read data0[7:0]|||
|5|Cortex-M7_0 DC tag|Word1[7:0] – Cortex-M7_0<br>DC tag read data3[32:25]|Word0[31:25] – Cortex-<br>M7_0 DC tag<br>|104|28|
|||Word2[31:14] – Cortex-<br>M7_0 DC tag<br>read data3[24:7]|read data3[6:0]|||
|||Word2[13:0] – Cortex-M7_0<br>DC tag read data2[32:19]|Word0[24:18] – Cortex-<br>M7_0 DC tag<br>|||
|||Word3[31:20] – Cortex-<br>M7_0 DC tag<br>read data2[18:7]|read data2[6:0]|||
|||Word3[19:0] – Cortex-M7_0<br>DC tag read data1[32:13]|Word0[17:11] – Cortex-<br>M7_0 DC tag<br>|||
|||Word4[31:26] – Cortex-<br>M7_0 DC tag<br>read data1[12:7]|read data1[6:0]|||
|||Word4[25:0] – Cortex-M7_0<br>DC tag read data0[32:7]|Word0[10:4] – Cortex-M7_0<br>DC tag read data0[6:0]|||
|6|Cortex-M7_0<br>DC data0|Word1[31:0] – Cortex-M7_0<br>DC data0 read data3[38:7]|Word0[31:25] – Cortex-<br>M7_0 DC data0<br>read data3[6:0]|128|28|
|||Word2[31:0] – Cortex-M7_0<br>DC data0 read data2[38:7]|Word0[24:18] – Cortex-<br>M7_0 DC data0<br>read data2[6:0]|||
|||Word3[31:0] – Cortex-M7_0<br>DC data0 read data1[38:7]|Word0[17:11] – Cortex-<br>M7_0 DC data0<br>read data1[6:0]|||
|||Word4[31:0] – Cortex-M7_0<br>DC data0 read data0[38:7]|Word0[10:4] – Cortex-M7_0<br>DC data0 read data0[6:0]|||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1608 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

Table 233. EIM channel mapping - S32K3x1, S32K3x2, S32K3x4 (continued) 

|Channel #|Target|Data bits<sup>1</sup>|Check bits<sup>1</sup>|# of data bits|# of check bits|
|---|---|---|---|---|---|
|7|Cortex-M7_0<br>DC data1|Word1[31:0] – Cortex-M7_0<br>DC data1 read data3[38:7]|Word0[31:25] – Cortex-<br>M7_0 DC data1<br>read data3[6:0]|128|28|
|||Word2[31:0] – Cortex-M7_0<br>DC data1 read data2[38:7]|Word0[24:18] – Cortex-<br>M7_0 DC data1<br>read data2[6:0]|||
|||Word3[31:0] – Cortex-M7_0<br>DC data1 read data1[38:7]|Word0[17:11] – Cortex-<br>M7_0 DC data1<br>read data1[6:0]|||
|||Word4[31:0] – Cortex-M7_0<br>DC data1 read data0[38:7]|Word0[10:4] – Cortex-M7_0<br>DC data1 read data0[6:0]|||
|8|Cortex-M7_1 IC tag|Word1[12:0] – Cortex-M7_1<br>IC tag read data1[28:16]<br>Word2[31:22] – Cortex-<br>M7_1 IC tag<br>read data1[15:7]|Word0[31:25] – Cortex-<br>M7_1 IC tag read data1[6:0]|44|14|
|||Word2[21:0] – Cortex-M7_1<br>IC tag read data0[28:7]|Word0[24:18] – Cortex-<br>M7_1 IC tag read data0[6:0]|||
|9|Cortex-M7_1 IC tag|Word1[31:0] – Cortex-M7_1<br>IC data read data0[71:40]<br>Word2[31:0] – Cortex-M7_1<br>IC data read data0[39:8]|Word0[31:24] – Cortex-<br>M7_1 IC data<br>read data1[7:0]|128|16|
|||Word3[31:0] – Cortex-M7_1<br>IC data read data0[71:40]<br>Word4[31:0] – Cortex-M7_1<br>IC data read data0[39:8]|Word0[23:16] – Cortex-<br>M7_1 IC data<br>read data0[7:0]|||
|10|Cortex-M7_1 DC tag|Word1[7:0] – Cortex-M7_1<br>DC tag read data3[32:25]<br>Word2[31:14] – Cortex-<br>M7_1 DC tag<br>read data3[24:7]|Word0[31:25] – Cortex-<br>M7_1 DC tag<br>read data3[6:0]|104|28|
|||Word2[31:0] – Cortex-M7_1<br>DC tag read data2[32:19]|Word0[24:18] – Cortex-<br>M7_1 DC tag<br>|||
|||Word3[31:20] – Cortex-<br>M7_1 DC tag<br>read data1[18:7]|read data2[6:0]|||
|||Word3[19:0] – Cortex-M7_1<br>DC tag read data1[32:13]<br>Word4[31:26] – Cortex-<br>M7_1 DC tag<br>read data1[12:7]|Word0[17:11] – Cortex-<br>M7_1 DC tag<br>read data1[6:0]|||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1609 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

Table 233. EIM channel mapping - S32K3x1, S32K3x2, S32K3x4 (continued) 

|Channel #|Target|Data bits<sup>1</sup>|Check bits<sup>1</sup>|# of data bits|# of check bits|
|---|---|---|---|---|---|
|||Word4[25:0] – Cortex-M7_1<br>DC tag read data0[32:7]|Word0[10:4] – Cortex-M7_1<br>DC tag read data0[6:0]|||
|11|Cortex-M7_1<br>DC data0|Word1[31:0] – Cortex-M7_1<br>DC data0 read data3[38:7]|Word0[31:25] – Cortex-<br>M7_1 DC data0<br>read data3[6:0]|128|28|
|||Word2[31:0] – Cortex-M7_1<br>DC data0 read data2[38:7]|Word0[24:18] – Cortex-<br>M7_1 DC data0<br>read data2[6:0]|||
|||Word3[31:0] – Cortex-M7_1<br>DC data0 read data1[38:7]|Word0[17:11] – Cortex-<br>M7_1 DC data0<br>read data1[6:0]|||
|||Word4[31:0] – Cortex-M7_1<br>DC data0 read data0[38:7]|Word0[10:4] – Cortex-M7_1<br>DC data0 read data0[6:0]|||
|12|Cortex-M7_1<br>DC data1|Word1[31:0] – Cortex-M7_1<br>DC data1 read data0[38:7]|Word0[31:25] – Cortex-<br>M7_1 DC data1<br>read data3[6:0]|128|28|
|||Word2[31:0] – Cortex-M7_1<br>DC data1 read data0[38:7]|Word0[24:18] – Cortex-<br>M7_1 DC data1<br>read data2[6:0]|||
|||Word3[31:0] – Cortex-M7_1<br>DC data1 read data0[38:7]|Word0[17:11] – Cortex-<br>M7_1 DC data1<br>read data1[6:0]|||
|||Word4[31:0] – Cortex-M7_1<br>DC data1 read data0[38:7]|Word0[10:4] – Cortex-M7_1<br>DC data1 read data0[6:0]|||
|13|Cortex-M7_0 ITCM|Word1[31:0] – Cortex-M7_0<br>ITCM read data[63:32]<br>Word2[31:0] – Cortex-M7_0<br>ITCM read data[31:0]|Word0[31:24] – Cortex-<br>M7_0 ITCM read<br>data ECC[7:0]|64|8|
|14|Cortex-M7_0 D0TCM|Word1[31:0] – Cortex-M7_0<br>D0TCM read data[31:0]|Word0[31:24] – Cortex-<br>M7_0 D0TCM read<br>data ECC[7:0]|32|8|
|15|Cortex-M7_0 D1TCM|Word1[31:0] – Cortex-M7_0<br>D1TCM read data[31:0]|Word0[31:24] – Cortex-<br>M7_0 D1TCM read<br>data ECC[7:0]|32|8|
|16|Cortex-M7_1 ITCM|Word1[31:0] – Cortex-M7_1<br>ITCM read data[63:32]<br>Word2[31:0] – Cortex-M7_1<br>ITCM read data[31:0]|Word0[31:24] – Cortex-<br>M7_1 ITCM read<br>data ECC[7:0]|64|8|
|17|Cortex-M7_1 D0TCM|Word1[31:0] – Cortex-M7_1<br>D0TCM read data[31:0]|Word0[31:24] – Cortex-<br>M7_1 D0TCM read<br>data ECC[7:0]|32|8|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1610 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

Table 233. EIM channel mapping - S32K3x1, S32K3x2, S32K3x4 (continued) 

|Channel #|Target|Data bits<sup>1</sup>|Check bits<sup>1</sup>|# of data bits|# of check bits|
|---|---|---|---|---|---|
|18|Cortex-M7_1 D1TCM|Word1[31:0] – Cortex-M7_1<br>D1TCM read data[31:0]|Word0[31:24] – Cortex-<br>M7_1 D1TCM read<br>data ECC[7:0]|32|8|
|19|EMAC gasket|Word1[27:0] – EMAC AHB<br>write data[63:36]|—|188|0|
|||Word2[31:28] – EMAC AHB<br>write data[35:32]||||
|||Word2[27:0] – EMAC AHB<br>write data[31:4]||||
|||Word3[31:28] – EMAC AHB<br>write data[3:0]||||
|||Word3[27:0] – EMAC AHB<br>read data[63:36]||||
|||Word4[31:28] – EMAC AHB<br>read data[35:32]||||
|||Word4[27:0] – EMAC AHB<br>read data[31:4]||||
|||Word5[31:28] – EMAC AHB<br>read data[3:0]||||
|||Word5[27:0] – EMAC<br>gasket monitor<br>error injection[59:32]||||
|||Word6[31:0] – EMAC<br>gasket monitor<br>error injection[31:0]||||
|20|Cortex-M7<br>TCM gasket|Word1[27:0] – TCM AHB<br>write data[63:36]|—|188|0|
|||Word2[31:28] – TCM AHB<br>write data[35:32]||||
|||Word2[27:0] – TCM AHB<br>write data[31:4]||||
|||Word3[31:28] – TCM AHB<br>write data[3:0]||||
|||Word3[27:0] – TCM AHB<br>read data[63:36]||||
|||Word4[31:28] – TCM AHB<br>read data[35:32]||||
|||Word4[27:0] – TCM AHB<br>read data[31:4]||||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1611 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

Table 233. EIM channel mapping - S32K3x1, S32K3x2, S32K3x4 (continued) 

|Channel #|Target|Data bits<sup>1</sup>|Check bits<sup>1</sup>|# of data bits|# of check bits|
|---|---|---|---|---|---|
|||Word5[31:28] – TCM AHB<br>read data[3:0]||||
|||Word5[27:0] – TCM<br>gasket monitor<br>error injection[59:32]<br>Word6[31:0] – TCM gasket<br>monitor error injection[31:0]||||
|21|DMA AXBS<br>S0 gasket|Word1[27:0] – DMA<br>AXBS S0 gasket monitor<br>error injection[59:32]<br>Word2[31:0] – DMA<br>AXBS S0 gasket monitor<br>error injection[0:31]|—|60|0|
|22|DMA AXBS<br>S1 gasket|Word1[27:0] – DMA<br>AXBS S1 gasket monitor<br>error injection[59:32]<br>Word2[31:0] – DMA<br>AXBS S1 gasket monitor<br>error injection[31:0]|—|60|0|
|23|HSE gasket|Word1[27:0] – HSE<br>gasket monitor<br>error injection[59:32]<br>Word2[31:0] – HSE gasket<br>monitor error injection[31:0]|—|60|0|
|24|QuadSPI gasket|Word1[27:0] – QuadSPI<br>gasket monitor<br>error injection[59:32]|—|60|0|
|||Word2[31:0] – QuadSPI<br>gasket monitor<br>error injection[31:0]||||
|25|AIPS1 gasket|Word1[27:0] – AIPS1<br>gasket monitor<br>error injection[59:32]|—|60|0|
|||Word2[31:0] – AIPS1<br>gasket monitor<br>error injection[31:0]||||
|26|AIPS2 gasket|Word1[27:0] – AIPS2<br>gasket monitor<br>error injection[59:32]|—|60|0|
|||Word2[31:0] – AIPS2<br>gasket monitor<br>error injection[31:0]||||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1612 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

Table 233. EIM channel mapping - S32K3x1, S32K3x2, S32K3x4 (continued) 

|Channel #|Target|Data bits<sup>1</sup>|Check bits<sup>1</sup>|# of data bits|# of check bits|
|---|---|---|---|---|---|
|27|Cortex-M7 lockstep|Word1[29:0] – Cortex-M7<br>error injection[29:0]|—|30|0|
|28|ECC<br>checking address|Word1[1:0] – Inject error on<br>flash memory controller port<br>0 address checker|—|24|0|
|||Word1[3:2] – Inject error on<br>flash memory controller port<br>1 address checker||||
|||Word1[4:4] – Inject error on<br>flash memory controller port<br>2 address checker||||
|||Word1[7:6] – Inject error<br>on PRAM0 controller<br>address checker||||
|||Word1[9:8] – Inject error<br>on PRAM1 controller<br>address checker||||
|||Word1[11:10] – Inject<br>error on 64-bit TCM bus<br>address checker||||
|||Word1[13:12] – Inject<br>error on QuadSPI path<br>address checker||||
|||Word1[15:14] – Inject error<br>on AIPS0 address checker||||
|||Word1[17:16] – Inject error<br>on AIPS1 address checker||||
|||Word1[19:18] – Inject error<br>on AIPS2 address checker||||
|||Word1[21:20] – Inject error<br>on 32-bit TCM Cortex-M7_0<br>path address checker||||
|||Word1[23:22] – Inject error<br>on 32-bit TCM Cortex-M7_1<br>path address checker||||
|||Word1[25:24] – Inject error<br>on DMA AXBS S0 address<br>parity checker<sup>3</sup>||||
|||Word1[27:26] – Inject error<br>on DMA AXBS S1 address<br>parity checker<sup>3</sup>||||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1613 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

Table 233. EIM channel mapping - S32K3x1, S32K3x2, S32K3x4 (continued) 

|Channel #|Target|Data bits<sup>1</sup>|Check bits<sup>1</sup>|# of data bits|# of check bits|
|---|---|---|---|---|---|
|29|EDC checking wdata|Word1[1:0] – Inject error<br>on PRAM0 controller write<br>data checker|—|18|0|
|||Word1[3:2] – Inject error<br>on PRAM1 controller write<br>data checker||||
|||Word1[5:4] – Inject error<br>on 64-bit TCM bus write<br>data checker||||
|||Word1[7:6] – Reserved||||
|||Word1[9:8] – Inject error on<br>AIPS0 write data checker||||
|||Word1[11:10] – Inject<br>error on AIPS1 write<br>data checker||||
|||Word1[13:12] – Inject<br>error on AIPS2 write<br>data checker||||
|||Word1[15:14] – Inject error<br>on 32-bit TCM Cortex-M7_0<br>path write data checker||||
|||Word1[17:16] – Inject error<br>on 32-bit TCM Cortex-M7_1<br>path write data checker||||
|30|EDC checking rdata|Word1[1:0] – Inject error on<br>Cortex-M7_0 AHBM read<br>data checker|—|18|0|
|||Word1[3:2] – Inject error<br>on Cortex-M7_0 AHBP read<br>data checker||||
|||Word1[5:4] – Inject error on<br>DMA read data checker||||
|||Word1[7:6] – Inject error on<br>STAM read data checker||||
|||Word1[9:8] – Inject error on<br>HSE read data checker||||
|||Word1[11:10] – Inject<br>error on EMAC read<br>data checker||||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1614 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

Table 233. EIM channel mapping - S32K3x1, S32K3x2, S32K3x4 (continued) 

|Channel #|Target|Data bits<sup>1</sup>|Check bits<sup>1</sup>|# of data bits|# of check bits|
|---|---|---|---|---|---|
|||Word1[13:12] – Inject error<br>on Cortex-M7_1 AHBM<br>read data checker||||
|||Word1[15:14] – Inject error<br>on Cortex-M7_1 AHBP read<br>data checker||||
|||Word1[17:16] – Inject error<br>on 32-bit TCM bus path<br>read data checker||||



1. You must write to EICHDi_WORDj registers to inject errors in the desired data and check bits. For details, see tables "Error injection channel descriptor: DATA_MASK details" and "DATA_MASK bit: Channel-word mapping" in this chapter. 

2. SRAM1 is not available for the S32K342, S32K312, and S32K311 variants. 

3. Applicable for S32K342 and S32K322 only. 

The two enables, GEIEN and EICHENn, enable the error injection functionality. The former enables it globally and the latter does it for a particular channel. This double-layer enable provides protection against accidental enabling and reconfiguration of the error injection function for each channel. 

EIM provides support for inducing single-bit and multi-bit inversions on read data when accessing peripheral RAMs through its data mask registers. 

~~<mark>NOTE</mark>~~ 

For enabling error injection on EDC gaskets (corresponding to channel 28, channel 29, and channel 30), you must also enable the fields corresponding to the required EDC gasket in the MSCM_ENEDC register before enabling the EIM channel. 

EIM_EICHD1_CH01, EIM_EICHD1_CH08, EIM_EICHD1_CH09, EIM_EICHD1_CH10, EIM_EICHD1_CH11, EIM_EICHD1_CH12, EIM_EICHD1_CH16, EIM_EICHD1_CH17, EIM_EICHD1_CH18, EIM_EICHD1_CH19, EIM_EICHD1_CH21, EIM_EICHD1_CH22, EIM_EICHD1_CH24, EIM_EICHD1_CH26, EIM_EICHD1_CH27 are not present in K312, hence the registers corresponding to these channels are also not present in K312. 

EIM channel mapping - S32K3x8 

Table 234. EIM_0 channel mapping - S32K3x8 

|Channel<br>Number|Target|Data bits|Check bits|Num of<br>data bits|Num of<br>check bits|
|---|---|---|---|---|---|
|0|cm7_0 ic tag|[43:22] - cm7_0 ic tag<br>read data1[28:7]|[13:7] - cm7_0 ic tag<br>read data1[6:0]|44|14|
|||[21:0] - cm7_0 ic tag<br>read data0[28:7]|[6:0] - cm7_0 ic tag<br>read data0[6:0]|||
|1|cm7_0 ic data|[127:64] - cm7_0 ic data<br>read data1[71:8]|[15:8] - cm7_0 ic data<br>read data1[7:0]|128|16|
|||[63:0] - cm7_0 ic data<br>read data0[71:8]|[7:0] - cm7_0 ic data<br>read data0[7:0]|||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1615 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

Table 234. EIM_0 channel mapping - S32K3x8 (continued) 

|Channel<br>Number|Target|Data bits|Check bits|Num of<br>data bits|Num of<br>check bits|
|---|---|---|---|---|---|
|2|cm7_0 dc tag|[103:76] - cm7_0 dc tag<br>read data3[32:7]<br>[75:52] - cm7_0 dc tag<br>read data2[32:7]<br>[51:26] - cm7_0 dc tag<br>read data1[32:7]<br>[25:0] - cm7_0 dc tag<br>read data0[32:7]|[27:21] - cm7_0 dc tag<br>read data3[6:0]<br>[20:14] - cm7_0 dc tag<br>read data2[6:0]<br>[13:7] - cm7_0 dc tag<br>read data1[6:0]<br>[6:0] - cm7_0 dc tag<br>read data0[6:0]|104|28|
|3|cm7_0 dc data0|[127:96] - cm7_0 dc data0<br>read data3[38:7]<br>[95:64] - cm7_0 dc data0<br>read data2[38:7]<br>[63:32] - cm7_0 dc data0<br>read data1[38:7]<br>[31:0] - cm7_0 dc data0<br>read data0[38:7]|[27:21] - cm7_0 dc data0<br>read data3[6:0]<br>[20:14] - cm7_0 dc data0<br>read data2[6:0]<br>[13:7] - cm7_0 dc data0<br>read data1[6:0]<br>[6:0] - cm7_0 dc data0<br>read data0[6:0]|128|28|
|4|cm7_0 dc data1|[127:96] - cm7_0 dc data1<br>read data3[38:7]<br>[95:64] - cm7_0 dc data1<br>read data2[38:7]<br>[63:32] - cm7_0 dc data1<br>read data1[38:7]<br>[31:0] - cm7_0 dc data1<br>read data0[38:7]|[27:21] - cm7_0 dc data1<br>read data3[6:0]<br>[20:14] - cm7_0 dc data1<br>read data2[6:0]<br>[13:7] - cm7_0 dc data1<br>read data1[6:0]<br>[6:0] - cm7_0 dc data1<br>read data0[6:0]|128|28|
|5|cm7_1 ic tag|[43:22] - cm7_1 ic tag<br>read data1[28:7]<br>[21:0] - cm7_1 ic tag<br>read data0[28:7]|[13:7] - cm7_1 ic tag<br>read data1[6:0]<br>[6:0] - cm7_1 ic tag<br>read data0[6:0]|44|14|
|6|cm7_1 ic data|[127:64] - cm7_1 ic data<br>read data1[71:8]<br>[63:0] - cm7_1 ic data<br>read data0[71:8]|[15:8] - cm7_1 ic data<br>read data1[7:0]<br>[7:0] - cm7_1 ic data<br>read data0[7:0]|128|16|
|7|cm7_1 dc tag|[103:76] - cm7_1 dc tag<br>read data3[32:7]<br>[75:52] - cm7_1 dc tag<br>read data2[32:7]<br>[51:26] - cm7_1 dc tag<br>read data1[32:7]|[27:21] - cm7_1 dc tag<br>read data3[6:0]<br>[20:14] - cm7_1 dc tag<br>read data2[6:0]<br>[13:7] - cm7_1 dc tag<br>read data1[6:0]|104|28|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1616 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

Table 234. EIM_0 channel mapping - S32K3x8 (continued) 

|Channel<br>Number|Target|Data bits|Check bits|Num of<br>data bits|Num of<br>check bits|
|---|---|---|---|---|---|
|||[25:0] - cm7_1 dc tag<br>read data0[32:7]|[6:0] - cm7_1 dc tag<br>read data0[6:0]|||
|8|cm7_1 dc data0|[127:96] - cm7_1 dc data0<br>read data3[38:7]<br>[95:64] - cm7_1 dc data0<br>read data2[38:7]<br>[63:32] - cm7_1 dc data0<br>read data1[38:7]<br>[31:0] - cm7_1 dc data0<br>read data0[38:7]|[27:21] - cm7_1 dc data0<br>read data3[6:0]<br>[20:14] - cm7_1 dc data0<br>read data2[6:0]<br>[13:7] - cm7_1 dc data0<br>read data1[6:0]<br>[6:0] - cm7_1 dc data0<br>read data0[6:0]|128|28|
|9|cm7_1 dc data1|[127:96] - cm7_1 dc data1<br>read data3[38:7]<br>[95:64] - cm7_1 dc data1<br>read data2[38:7]<br>[63:32] - cm7_1 dc data1<br>read data1[38:7]<br>[31:0] - cm7_1 dc data1<br>read data0[38:7]|[27:21] - cm7_1 dc data1<br>read data3[6:0]<br>[20:14] - cm7_1 dc data1<br>read data2[6:0]<br>[13:7] - cm7_1 dc data1<br>read data1[6:0]<br>[6:0] - cm7_1 dc data1<br>read data0[6:0]|128|28|
|10|cm7_0 itcm|[63:0] - cm7_0 itcm read data<br>[63:0]|[7:0] - cm7_0 itcm read data<br>ecc[7:0]|64|8|
|11|cm7_0 d0tcm|[31:0] - cm7_0 d0tcm read data<br>[31:0]|[7:0] - cm7_0 d0tcm read data<br>ecc[7:0]|32|8|
|12|cm7_0 d1tcm|[31:0] - cm7_0 d1tcm read data<br>[31:0]|[7:0] - cm7_0 d1tcm read data<br>ecc[7:0]|32|8|
|13|cm7_1 itcm|[63:0] - cm7_1 itcm read data<br>[63:0]|[7:0] - cm7_1 itcm read data<br>ecc[7:0]|64|8|
|14|cm7_1 d0tcm|[31:0] - cm7_1 d0tcm read data<br>[31:0]|[7:0] - cm7_1 d0tcm read data<br>ecc[7:0]|32|8|
|15|cm7_1 d1tcm|[31:0] - cm7_1 d1tcm read data<br>[31:0]|[7:0] - cm7_1 d1tcm read data<br>ecc[7:0]|32|8|
|16|cm7 lockstep|[29:0] - cm7 error injection[29:0]|-|30|0|
|17|-|-|-|0|0|
|18|-|-|-|0|0|
|19|-|-|-|0|0|
|20|-|-|-|0|0|
|21|-|-|-|0|0|
|22|-|-|-|0|0|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1617 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

Table 234. EIM_0 channel mapping - S32K3x8 (continued) 

|Channel<br>Number|Target|Data bits|Check bits|Num of<br>data bits|Num of<br>check bits|
|---|---|---|---|---|---|
|23|-|-|-|0|0|
|24|-|-|-|0|0|
|25|-|-|-|0|0|
|26|-|-|-|0|0|
|27|-|-|-|0|0|
|28|-|-|-|0|0|
|29|-|-|-|0|0|
|30|-|-|-|0|0|
|31|-|-|-|0|0|



Table 235. EIM_1 channel mapping - S32K3x8 

|Channel<br>Number|Target|Data bits|Check bits|Num of<br>data bits|Num of<br>check bits|
|---|---|---|---|---|---|
|0|cm7_2 ic tag|[43:22] - cm7_2 ic tag<br>read data1[28:7]<br>[21:0] - cm7_2 ic tag<br>read data0[28:7]|[13:7] - cm7_2 ic tag<br>read data1[6:0]<br>[6:0] - cm7_2 ic tag<br>read data0[6:0]|44|14|
|1|cm7_2 ic data|[127:64] - cm7_2 ic data<br>read data1[71:8]<br>[63:0] - cm7_2 ic data<br>read data0[71:8]|[15:8] - cm7_2 ic data<br>read data1[7:0]<br>[7:0] - cm7_2 ic data<br>read data0[7:0]|128|16|
|2|cm7_2 dc tag|[103:76] - cm7_2 dc tag<br>read data3[32:7]<br>[75:52] - cm7_2 dc tag<br>read data2[32:7]<br>[51:26] - cm7_2 dc tag<br>read data1[32:7]<br>[25:0] - cm7_2 dc tag<br>read data0[32:7]|[27:21] - cm7_2 dc tag<br>read data3[6:0]<br>[20:14] - cm7_2 dc tag<br>read data2[6:0]<br>[13:7] - cm7_2 dc tag<br>read data1[6:0]<br>[6:0] - cm7_2 dc tag<br>read data0[6:0]|104|28|
|3|cm7_2 dc data0|[127:96] - cm7_2 dc data0<br>read data3[38:7]<br>[95:64] - cm7_2 dc data0<br>read data2[38:7]<br>[63:32] - cm7_2 dc data0<br>read data1[38:7]|[27:21] - cm7_2 dc data0<br>read data3[6:0]<br>[20:14] - cm7_2 dc data0<br>read data2[6:0]<br>[13:7] - cm7_2 dc data0<br>read data1[6:0]|128|28|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1618 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

Table 235. EIM_1 channel mapping - S32K3x8 (continued) 

|Channel<br>Number|Target|Data bits|Check bits|Num of<br>data bits|Num of<br>check bits|
|---|---|---|---|---|---|
|||[31:0] - cm7_2 dc data0<br>read data0[38:7]|[6:0] - cm7_2 dc data0<br>read data0[6:0]|||
|4|cm7_2 dc data1|[127:96] - cm7_2 dc data1<br>read data3[38:7]<br>[95:64] - cm7_2 dc data1<br>read data2[38:7]<br>[63:32] - cm7_2 dc data1<br>read data1[38:7]<br>[31:0] - cm7_2 dc data1<br>read data0[38:7]|[27:21] - cm7_2 dc data1<br>read data3[6:0]<br>[20:14] - cm7_2 dc data1<br>read data2[6:0]<br>[13:7] - cm7_2 dc data1<br>read data1[6:0]<br>[6:0] - cm7_2 dc data1<br>read data0[6:0]|128|28|
|5|-|-|-|0|0|
|6|-|-|-|0|0|
|7|-|-|-|0|0|
|8|-|-|-|0|0|
|9|-|-|-|0|0|
|10|cm7_2 itcm|[63:0] - cm7_2 itcm read data<br>[63:0]|[7:0] - cm7_2 itcm read data<br>ecc[7:0]|64|8|
|11|cm7_2 d0tcm|[31:0] - cm7_2 d0tcm read data<br>[31:0]|[7:0] - cm7_2 d0tcm read data<br>ecc[7:0]|32|8|
|12|cm7_2 d1tcm|[31:0] - cm7_2 d1tcm read data<br>[31:0]|[7:0] - cm7_2 d1tcm read data<br>ecc[7:0]|32|8|
|13|-|-|-|0|0|
|14|-|-|-|0|0|
|15|-|-|-|0|0|
|16|-|-|-|0|0|
|17|-|-|-|0|0|
|18|-|-|-|0|0|
|19|-|-|-|0|0|
|20|-|-|-|0|0|
|21|-|-|-|0|0|
|22|-|-|-|0|0|
|23|-|-|-|0|0|
|24|-|-|-|0|0|
|25|-|-|-|0|0|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1619 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

Table 235. EIM_1 channel mapping - S32K3x8 (continued) 

|Channel<br>Number|Target|Data bits|Check bits|Num of<br>data bits|Num of<br>check bits|
|---|---|---|---|---|---|
|26|-|-|-|0|0|
|27|-|-|-|0|0|
|28|-|-|-|0|0|
|29|-|-|-|0|0|
|30|-|-|-|0|0|
|31|-|-|-|0|0|



Table 236. EIM_2 channel mapping - S32K3x8 

|Channel<br>Number|Target|Data bits|Check bits|Num of<br>data bits|Num of<br>check bits|
|---|---|---|---|---|---|
|0|sram0|[63:0] - sram0 read data[63:0]|[7:0] sram0 read data<br>ecc[7:0]|64|8|
|1|sram1|[63:0] - sram1 read data[63:0]|[7:0] sram1 read data<br>ecc[7:0]|64|8|
|2|sram2|[63:0] - sram2 read data[63:0]|[7:0] sram2 read data<br>ecc[7:0]|64|8|
|3|dma tcd|[63:0] - dma tcd ram read data[63:0]|[7:0] dma tcd ram read<br>data checkbits[7:0]|64|8|
|4|-|-|-|0|0|
|5|enet gasket|[59:0] GMAC AHB Gasket Mon Error<br>Injection data[59:0]|-|60|0|
|6|CM7 TCM<br>gasket|[187:124] TCM AHB WRITE DATA[63:0]<br>[123:60] TCM AHB READ DATA[63:0]<br>[59:0] TCM AHB Gasket Mon Error<br>Injection data[59:0]|-|188|0|
|7|dma axbs s0<br>gasket|[59:0] DMA Axbs s0 Gasket Mon Error<br>Injection data[59:0]|-|60|0|
|8|dma axbs s1<br>gasket|[59:0] DMA Axbs s1 Gasket Mon Error<br>Injection data[59:0]|-|60|0|
|9|pram0_gasket|[59:0] PRAM0 Gasket Mon Error Injection<br>data[59:0]|-|60|0|
|10|pram1_gasket|[59:0] PRAM1 Gasket Mon Error Injection<br>data[59:0]|-|60|0|
|11|tcm_pram_gaske<br>t|[59:0] TCM PRAM Gasket Mon Error<br>Injection data[59:0]|-|60|0|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1620 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

Table 236. EIM_2 channel mapping - S32K3x8 (continued) 

|Channel<br>Number|Target|Data bits|Check bits|Num of<br>data bits|Num of<br>check bits|
|---|---|---|---|---|---|
|12|cm7_0_ahbs<br>gasket|[187:124]<br>- cm7_0_ahbs_gskt_err_inj_rdata[63:0]<br>[123:60]<br>- cm7_0_ahbs_gskt_err_inj_wdata[63:0]<br>[59:0]<br>– cm7_0_ahbs_gskt_mon_err_inj[59:0]|-|0|0|
|13|cm7_1_ahbs<br>gasket|[187:124]<br>- cm7_0_ahbs_gskt_err_inj_rdata[63:0]<br>[123:60]<br>- cm7_0_ahbs_gskt_err_inj_wdata[63:0]<br>[59:0]<br>– cm7_0_ahbs_gskt_mon_err_inj[59:0]|-|0|0|
|14|cm7_2_ahbs<br>gasket|[187:124]<br>- cm7_2_ahbs_gskt_err_inj_rdata[63:0]<br>[123:60]<br>- cm7_2_ahbs_gskt_err_inj_wdata[63:0]<br>[59:0]<br>– cm7_2_ahbs_gskt_mon_err_inj[59:0]|-|0|0|
|15|-|-|-|0|0|
|16|-|-|-|0|0|
|17|hse gasket|[59:0] HSE Gasket Mon Error Injection<br>data[59:0]|-|60|0|
|18|qspi gasket|[59:0] QSPI Gasket Mon Error Injection<br>data[59:0]|-|60|0|
|19|aips1|[59:0] AIPS1 Gasket Mon Error Injection<br>data[59:0]|-|60|0|
|20|aips2|[59:0] AIPS2 Gasket Mon Error Injection<br>data[59:0]|-|60|0|
|21|aips0|[59:0] AIPS0 Gasket Mon Error Injection<br>data[59:0]|-|60|0|
|22|-|-|-|0|0|
|23<br>24|uDSHC gasket<br>-|[187:124]<br>- uSDHC_gskt_wdata_err_inj[63:0]<br>[123:60] - uSDHC_gskt_rdata_err_inj[63:0]<br>[59:0] – USDHC_gskt_mon_err_inj[59:0]<br>-|-<br>-|188<br>0|0<br>0|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1621 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

Table 236. EIM_2 channel mapping - S32K3x8 (continued) 

|Channel<br>Number|Target|Data bits|Check bits|Num of<br>data bits|Num of<br>check bits|
|---|---|---|---|---|---|
|25|-|-|-|0|0|
|26|edc1 gaskets<br>addr|[1:0] Inject error on flash controller 3 port<br>address checker<br>[3:2] Inject error on 32 bit CM7_2 TCM path<br>address checker<br>[5:4] Inject error on PRAM2<br>address checker|-|6|0|
|27|edc1 gaskets<br>wdata|[1:0] Inject error on CM7_2 TCM path write<br>data checker<br>[3:2] Inject error on PRAM2 write<br>data checker|-|4|0|
|28|edc1 gaskets<br>rdata|[1:0] Inject error on CM7_2 AHBM read<br>data checker<br>[3:2] Inject error on CM7_2 AHBP read<br>data checker<br>[5:4] Inject error on uSDHC read<br>data checker|-|6|0|
|29|edc gaskets addr|[1:0] Inject error on flash controller 0 port<br>address checker<br>[3:2] Inject error on flash controller 1 port<br>address checker<br>[5:4] Inject error on flash controller 2 port<br>address checker<br>[7:6] Inject error on PRAM0<br>address checker<br>[9:8] Inject error on PRAM1<br>address checker<br>[11:10] Inject error on 64 bit TCM PRAM<br>address checker<br>[13:12] Inject error on QSPI<br>address checker<br>[15:14] Inject error on AIPS0<br>address checker<br>[17:16] Inject error on AIPS1<br>address checker<br>[19:18] Inject error on AIPS2<br>address checker|-|28|0|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1622 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

Table 236. EIM_2 channel mapping - S32K3x8 (continued) 

|Channel<br>Number|Target|Data bits|Check bits|Num of<br>data bits|Num of<br>check bits|
|---|---|---|---|---|---|
|||[21:20] Inject error on 32 bit CM2_0 TCM<br>address checker<br>[23:22] Inject error on 32 bit CM7_1 TCM<br>path address checker<br>[25:24] Inject error on DMA S0<br>address checker<br>[27:26] Inject error on DMA S1<br>address checker||||
|30|edc gaskets<br>wdata|[1:0] Inject error on PRAM0 write<br>data checker<br>[3:2] Inject error on PRAM1 write<br>data checker<br>[7:6] Inject error on QSPI write data checker<br>[9:8] Inject error on AIPS0 write<br>data checker<br>[11:10] Inject error on AIPS1 write<br>data checker<br>[13:12] Inject error on AIPS2 write<br>data checker<br>[15:14] Inject error on CM7_0 TCM path<br>write data checker<br>[17:16] Inject error on CM7_1 TCM path<br>write data checker|-|18|0|
|31|edc gaskets<br>rdata|[1:0] Inject error on CM7_0 AHBM read<br>data checker<br>[3:2] Inject error on CM7_0 AHBP read<br>data checker<br>[5:4] Inject error on DMA read data checker<br>[7:6] Inject error on STAM read<br>data checker<br>[9:8] Inject error on HSE read data checker<br>[11:10] Inject error on ENET read<br>data checker<br>[13:12] Inject error on CM7_1 AHBM read<br>data checker<br>[15:14] Inject error on CM7_1 AHBP read<br>data checker|-|18|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1623 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

### 48.1.3 Behavior of EIM error injection on gaskets 

The error injection on gaskets don't impact the actual data flow. The gasket read data, write data and the monitor error don't get changed when EIM error injection is done. The gasket compares the actual data with the modified data (with error injection) and flags the gasket alarm. In case of single-bit error also, the alarm is flagged. 

The channels which depict such behavior are the gasket channels listed below: 

- Channel 19: EMAC gasket 

- Channel 20: Cortex-M7 TCM gasket 

- Channel 21: DMA AXBS S0 gasket 

- Channel 22: DMA AXBS S1 gasket 

- Channel 23: HSE gasket 

- Channel 24: QuadSPI gasket 

- Channel 25: AIPS1 gasket 

- Channel 26: AIPS2 gasket 

## 48.2 Overview 

The Error Injection Module (EIM) is mainly used for diagnostic purposes. It provides a method for diagnostic coverage of internal memories (for example, system RAM, cache RAMs, and peripheral memories). See the chip-specific EIM information to determine which functional safety features are supported by this method. 

EIM enables you to induce artificial errors on error-checking mechanisms of a system, such as ECC for RAM read data and parity bits. For each such mechanism that EIM supports on the chip, EIM can inject single-bit and multi-bit inversions on data in the applicable target bus. Injecting faults on memory accesses can be used to exercise the SEC-DED ECC function of the related system. 

### 48.2.1 Features 

The EIM includes these features: 

- Supports 27 error injection channels. See the chip-specific EIM information for channel assignment details. 

- Protection against accidental enable and reconfiguration error injection function via two-stage enable mechanism 

### 48.2.2 Block diagram 

The following diagram shows an example of EIM implementation with a 64-bit read data bus and an 8-bit checkbit bus. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1624 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/048_Error_Injection_Module_-EIM-/S32K3XXRM_数据表.pdf-1625-02.png)


<!-- Start of picture text -->
rdata[63](MSB)<br>rdata[62]<br>rdata[61]<br>   RAM  Module<br>   array<br>rdata[0](LSB)<br>chkbit[7]<br>chkbit[0]<br>EIM<br>EIMCR[GEIEN]<br>EICHEN[EICHnEN]<br>EICHDn_WORD0<br>EICHDn_WORD1<br>EICHDn_WORD2<br><!-- End of picture text -->

Figure 182. EIM functional block diagram (64-bit read data bus and 8-bit check bit bus) 

Several memory elements are implemented within a device, which may not only be the large memory blocks (Flash and SRAM) but also smaller memories like caches, the TCD blocks, and the embedded peripheral memories. Some larger memories may actually be built from multiple memory elements, dependent on their size or function. Each of these memory elements implements its own control logic, the memory controller, that performs the accesses to the actual memory, the memory array. An EIM channel is associated with a memory controller and provides the capability to alter one or multiple signals in the read access path from the corresponding memory array(s). Only memory controllers controlling a safety related memory may be associated with an EIM channel. 

## 48.3 Functional description 

The EIM provides protection against accidental enabling and reconfiguration of the error injection function by enforcing a two-stage enablement mechanism. To properly enable the error injection mechanism for a channel: 

- Write 1 to the EICHEN[EICHnEN] field, where n denotes the channel number. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1625 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

- Write 1 to EIMCR[GEIEN]. 

~~<mark>NOTE</mark>~~ 

When the use case for a channel requires writing any EICHDn_WORD register, write the EICHDn_WORD register before executing the two-stage enablement mechanism. A successful write to any EICHDn_WORD register clears the corresponding EICHEN[EICHnEN] field. 

The EIM supports 27 error injection channels. See the chip-specific EIM information for channel assignment details. Each channel: 

- Can be assigned to a single memory array interface by intercepting the assigned memory read data bus and checkbit bus, and injects errors by inverting the value transmitted for selected bits on each bus line. 

- Can be assigned to a redundant comparison unit by intercepting the signals being compared, and injecting errors by inverting the value transmitted for selected bits on each bus line. 

On a memory read access, the applicable EICHDn_WORD registers define which bits of the read data and/or checkbit bus to invert. 

Figure 182 depicts the interception and override of a 64-bit read data bus and an 8-bit checkbit data bus for an example memory array. 

Error injection scenarios 

The EIM supports these cases of error injection: 

- To generate a single-bit error, invert only 1 bit of the CHKBIT_MASK or DATA_MASK in the EICHDn_WORD registers. 

- To generate a multi-bit error, invert only 2 bits of the CHKBIT_MASK or DATA_MASK in the EICHDn_WORD registers. 

~~<mark>NOTE</mark>~~ 

An attempt to invert more than 2 bits in one operation might result in undefined behavior. 

To enable error injection: 

1. Set the EICHDn_WORDm[CHKBIT_MASK] and EICHDn_WORDm[Ba_bDATA_MASK] fields for each channel that will be driving an injection. 

2. Program the EICHEN register to enable the channels that will be injecting errors. 

3. Set the EIMCR[GEIEN] field to globally allow all enabled channels to actively inject errors. 

To disable error injection, either disable the EIMCR[GEIEN] field or disable the individual channel enable fields of the EICHEN register. 

## 48.4 EIM register descriptions 

The EIM provides a programming model mapped to an on-platform peripheral slot. 

#### Programming model access 

All system bus masters can access the programming model: 

- Only in supervisor mode 

- Using only 32-bit (word) accesses 

Any of the following attempted references to the programming model generates an error termination: 

- In user mode 

- Using non-32-bit access sizes 

- To undefined (reserved) addresses 

Attempted updates to the programming model while the EIM is in the midst of an operation result in non-deterministic behavior. 

Error injection channel descriptor: function and structure 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1626 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

Each error injection channel descriptor: 

- Specifies a mask that defines which bits of the read data and/or checkbit bus from target RAM are inverted on a read access. 

- Consists of a 288-bit (36-byte) structure, composed of nine 32-bit words, in the EIM programming model. Unused words are not documented. 

   - Word0 (EICHDn_WORD0), if present, defines the checkbit mask. 

   - Word1 (EICHDn_WORD1) and additional words, if present, define the data mask. Word registers subsequent to Word1 are present only when required by the total width of the channel's data mask. Error injection channel descriptor: DATA_MASK details. 

The multiple channel descriptors are organized sequentially. 

Error injection channel descriptor: DATA_MASK details 

For each channel: The following tables show the distribution of DATA_MASK's bits across the WORD registers. The first table shows the total width of DATA_MASK and the distribution of its bits across WORD1, WORD2, and WORD3. The second table shows the distribution of DATA_MASK's bits across WORD4 and subsequent registers. 

Table 237. Error injection channel descriptor: DATA_MASK details 

|Channel|DATA_MASK total<br>idth bit|Sp<br>|ecific bits of DATA_MASK<br>|in<br>|
|---|---|---|---|---|
||w (s)|WORD1|WORD2|WORD3|
|0|64|63-32|31-0|—|
|1|64|63-32|31-0|—|
|2|64|63-32|31-0|—|
|3|64|63-32|31-0|—|
|5|60|59-32|31-0|—|
|6|188|187-160|159-128|127-96|
|7|60|59-32|31-0|—|
|8|60|59-32|31-0|—|
|9|60|59-32|31-0|—|
|10|60|59-32|31-0|—|
|11|60|59-32|31-0|—|
|12|188|187-160|159-128|127-96|
|13|188|187-160|159-128|127-96|
|14|188|187-160|159-128|127-96|
|15|60|59-32|31-0|—|
|17|60|59-32|31-0|—|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1627 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

Table 237. Error injection channel descriptor: DATA_MASK details (continued) 

|Channel|DATA_MASK total<br>ih i|Sp|ecific bits of DATA_MASK|in|
|---|---|---|---|---|
||wdt (bts)|WORD1|WORD2|WORD3|
|18|60|59-32|31-0|—|
|19|60|59-32|31-0|—|
|20|60|59-32|31-0|—|
|21|60|59-32|31-0|—|
|23|188|187-160|159-128|127-96|
|26|6|5-0|—|—|
|27|4|3-0|—|—|
|28|6|5-0|—|—|
|29|28|27-0|—|—|
|30|18|17-0|—|—|
|31|18|17-0|—|—|



#### Table 238. DATA_MASK bit: Channel-word mapping 

|Channel||Spec<br>|ific bits of DATA_MA<br>|SK in<br>||
|---|---|---|---|---|---|
||WORD4|WORD5|WORD6|WORD7|WORD8|
|6|95-64|63-32|31-0|—|—|
|12|95-64|63-32|31-0|—|—|
|13|95-64|63-32|31-0|—|—|
|14|95-64|63-32|31-0|—|—|
|23|95-64|63-32|31-0|—|—|



### 48.4.1 EIM memory map 

EIM_0 base address: 4025_8000h 

EIM_1 base address: 4000_8000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|Error Injection Module Configuration Register (EIMCR)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1628 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|4h|Error Injection Channel Enable register (EICHEN)|32|RW|0000_0000h|
|100h|Error Injection Channel Descriptor 0, Word0 (EICHD0_WORD0)|32|RW|0000_0000h|
|104h|Error Injection Channel Descriptor 0, Word1 (EICHD0_WORD1)|32|RW|0000_0000h|
|108h|Error Injection Channel Descriptor 0, Word2 (EICHD0_WORD2)|32|RW|0000_0000h|
|200h|Error Injection Channel Descriptor 1, Word0 (EICHD1_WORD0)|32|RW|0000_0000h|
|204h|Error Injection Channel Descriptor 1, Word1 (EICHD1_WORD1)|32|RW|0000_0000h|
|208h|Error Injection Channel Descriptor 1, Word2 (EICHD1_WORD2)|32|RW|0000_0000h|
|20Ch|Error Injection Channel Descriptor 1, Word3 (EICHD1_WORD3)|32|RW|0000_0000h|
|210h|Error Injection Channel Descriptor 1, Word4 (EICHD1_WORD4)|32|RW|0000_0000h|
|300h|Error Injection Channel Descriptor 2, Word0 (EICHD2_WORD0)|32|RW|0000_0000h|
|304h|Error Injection Channel Descriptor 2, Word1 (EICHD2_WORD1)|32|RW|0000_0000h|
|308h|Error Injection Channel Descriptor 2, Word2 (EICHD2_WORD2)|32|RW|0000_0000h|
|30Ch|Error Injection Channel Descriptor 2, Word3 (EICHD2_WORD3)|32|RW|0000_0000h|
|310h|Error Injection Channel Descriptor 2, Word4 (EICHD2_WORD4)|32|RW|0000_0000h|
|400h|Error Injection Channel Descriptor 3, Word0 (EICHD3_WORD0)|32|RW|0000_0000h|
|404h|Error Injection Channel Descriptor 3, Word1 (EICHD3_WORD1)|32|RW|0000_0000h|
|408h|Error Injection Channel Descriptor 3, Word2 (EICHD3_WORD2)|32|RW|0000_0000h|
|40Ch|Error Injection Channel Descriptor 3, Word3 (EICHD3_WORD3)|32|RW|0000_0000h|
|410h|Error Injection Channel Descriptor 3, Word4 (EICHD3_WORD4)|32|RW|0000_0000h|
|500h|Error Injection Channel Descriptor 4, Word0 (EICHD4_WORD0)|32|RW|0000_0000h|
|504h|Error Injection Channel Descriptor 4, Word1 (EICHD4_WORD1)|32|RW|0000_0000h|
|508h|Error Injection Channel Descriptor 4, Word2 (EICHD4_WORD2)|32|RW|0000_0000h|
|50Ch|Error Injection Channel Descriptor 4, Word3 (EICHD4_WORD3)|32|RW|0000_0000h|
|510h|Error Injection Channel Descriptor 4, Word4 (EICHD4_WORD4)|32|RW|0000_0000h|
|604h|Error Injection Channel Descriptor 5, Word1 (EICHD5_WORD1)|32|RW|0000_0000h|
|608h|Error Injection Channel Descriptor 5, Word2 (EICHD5_WORD2)|32|RW|0000_0000h|
|704h|Error Injection Channel Descriptor 6, Word1 (EICHD6_WORD1)|32|RW|0000_0000h|
|708h|Error Injection Channel Descriptor 6, Word2 (EICHD6_WORD2)|32|RW|0000_0000h|
|70Ch|Error Injection Channel Descriptor 6, Word3 (EICHD6_WORD3)|32|RW|0000_0000h|
|710h|Error Injection Channel Descriptor 6, Word4 (EICHD6_WORD4)|32|RW|0000_0000h|
|714h|Error Injection Channel Descriptor 6, Word5 (EICHD6_WORD5)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1629 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|718h|Error Injection Channel Descriptor 6, Word6 (EICHD6_WORD6)|32|RW|0000_0000h|
|804h|Error Injection Channel Descriptor 7, Word1 (EICHD7_WORD1)|32|RW|0000_0000h|
|808h|Error Injection Channel Descriptor 7, Word2 (EICHD7_WORD2)|32|RW|0000_0000h|
|904h|Error Injection Channel Descriptor 8, Word1 (EICHD8_WORD1)|32|RW|0000_0000h|
|908h|Error Injection Channel Descriptor 8, Word2 (EICHD8_WORD2)|32|RW|0000_0000h|
|A04h|Error Injection Channel Descriptor 9, Word1 (EICHD9_WORD1)|32|RW|0000_0000h|
|A08h|Error Injection Channel Descriptor 9, Word2 (EICHD9_WORD2)|32|RW|0000_0000h|
|B00h|Error Injection Channel Descriptor 10, Word0 (EICHD10_WORD0)|32|RW|0000_0000h|
|B04h|Error Injection Channel Descriptor 10, Word1 (EICHD10_WORD1)|32|RW|0000_0000h|
|B08h|Error Injection Channel Descriptor 10, Word2 (EICHD10_WORD2)|32|RW|0000_0000h|
|C00h|Error Injection Channel Descriptor 11, Word0 (EICHD11_WORD0)|32|RW|0000_0000h|
|C04h|Error Injection Channel Descriptor 11, Word1 (EICHD11_WORD1)|32|RW|0000_0000h|
|C08h|Error Injection Channel Descriptor 11, Word2 (EICHD11_WORD2)|32|RW|0000_0000h|
|D00h|Error Injection Channel Descriptor 12, Word0 (EICHD12_WORD0)|32|RW|0000_0000h|
|D04h|Error Injection Channel Descriptor 12, Word1 (EICHD12_WORD1)|32|RW|0000_0000h|
|D08h|Error Injection Channel Descriptor 12, Word2 (EICHD12_WORD2)|32|RW|0000_0000h|
|D0Ch|Error Injection Channel Descriptor 12, Word3 (EICHD12_WORD3)|32|RW|0000_0000h|
|D10h|Error Injection Channel Descriptor 12, Word4 (EICHD12_WORD4)|32|RW|0000_0000h|
|D14h|Error Injection Channel Descriptor 12, Word5 (EICHD12_WORD5)|32|RW|0000_0000h|
|D18h|Error Injection Channel Descriptor 12, Word6 (EICHD12_WORD6)|32|RW|0000_0000h|
|E04h|Error Injection Channel Descriptor 13, Word1 (EICHD13_WORD1)|32|RW|0000_0000h|
|E08h|Error Injection Channel Descriptor 13, Word2 (EICHD13_WORD2)|32|RW|0000_0000h|
|E0Ch|Error Injection Channel Descriptor 13, Word3 (EICHD13_WORD3)|32|RW|0000_0000h|
|E10h|Error Injection Channel Descriptor 13, Word4 (EICHD13_WORD4)|32|RW|0000_0000h|
|E14h|Error Injection Channel Descriptor 13, Word5 (EICHD13_WORD5)|32|RW|0000_0000h|
|E18h|Error Injection Channel Descriptor 13, Word6 (EICHD13_WORD6)|32|RW|0000_0000h|
|F04h|Error Injection Channel Descriptor 14, Word1 (EICHD14_WORD1)|32|RW|0000_0000h|
|F08h|Error Injection Channel Descriptor 14, Word2 (EICHD14_WORD2)|32|RW|0000_0000h|
|F0Ch|Error Injection Channel Descriptor 14, Word3 (EICHD14_WORD3)|32|RW|0000_0000h|
|F10h|Error Injection Channel Descriptor 14, Word4 (EICHD14_WORD4)|32|RW|0000_0000h|
|F14h|Error Injection Channel Descriptor 14, Word5 (EICHD14_WORD5)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1630 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|F18h|Error Injection Channel Descriptor 14, Word6 (EICHD14_WORD6)|32|RW|0000_0000h|
|1004h|Error Injection Channel Descriptor 15, Word1 (EICHD15_WORD1)|32|RW|0000_0000h|
|1008h|Error Injection Channel Descriptor 15, Word2 (EICHD15_WORD2)|32|RW|0000_0000h|
|1204h|Error Injection Channel Descriptor 17, Word1 (EICHD17_WORD1)|32|RW|0000_0000h|
|1208h|Error Injection Channel Descriptor 17, Word2 (EICHD17_WORD2)|32|RW|0000_0000h|
|1304h|Error Injection Channel Descriptor 18, Word1 (EICHD18_WORD1)|32|RW|0000_0000h|
|1308h|Error Injection Channel Descriptor 18, Word2 (EICHD18_WORD2)|32|RW|0000_0000h|
|1404h|Error Injection Channel Descriptor 19, Word1 (EICHD19_WORD1)|32|RW|0000_0000h|
|1408h|Error Injection Channel Descriptor 19, Word2 (EICHD19_WORD2)|32|RW|0000_0000h|
|1504h|Error Injection Channel Descriptor 20, Word1 (EICHD20_WORD1)|32|RW|0000_0000h|
|1508h|Error Injection Channel Descriptor 20, Word2 (EICHD20_WORD2)|32|RW|0000_0000h|
|1604h|Error Injection Channel Descriptor 21, Word1 (EICHD21_WORD1)|32|RW|0000_0000h|
|1608h|Error Injection Channel Descriptor 21, Word2 (EICHD21_WORD2)|32|RW|0000_0000h|
|1804h|Error Injection Channel Descriptor 23, Word1 (EICHD23_WORD1)|32|RW|0000_0000h|
|1808h|Error Injection Channel Descriptor 23, Word2 (EICHD23_WORD2)|32|RW|0000_0000h|
|180Ch|Error Injection Channel Descriptor 23, Word3 (EICHD23_WORD3)|32|RW|0000_0000h|
|1810h|Error Injection Channel Descriptor 23, Word4 (EICHD23_WORD4)|32|RW|0000_0000h|
|1814h|Error Injection Channel Descriptor 23, Word5 (EICHD23_WORD5)|32|RW|0000_0000h|
|1818h|Error Injection Channel Descriptor 23, Word6 (EICHD23_WORD6)|32|RW|0000_0000h|
|1B04h|Error Injection Channel Descriptor 26, Word1 (EICHD26_WORD1)|32|RW|0000_0000h|
|1C04h|Error Injection Channel Descriptor 27, Word1 (EICHD27_WORD1)|32|RW|0000_0000h|
|1D04h|Error Injection Channel Descriptor 28, Word1 (EICHD28_WORD1)|32|RW|0000_0000h|
|1E04h|Error Injection Channel Descriptor 29, Word1 (EICHD29_WORD1)|32|RW|0000_0000h|
|1F04h|Error Injection Channel Descriptor 30, Word1 (EICHD30_WORD1)|32|RW|0000_0000h|
|2004h|Error Injection Channel Descriptor 31, Word1 (EICHD31_WORD1)|32|RW|0000_0000h|



### 48.4.2 Error Injection Module Configuration Register (EIMCR) 

#### Offset 

|Register|Offset|
|---|---|
|EIMCR|0h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1631 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Function 

The EIM Configuration Register is used to globally enable/disable the error injection function. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/048_Error_Injection_Module_-EIM-/S32K3XXRM_数据表.pdf-1632-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>GEIEN<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-1|Reserved|
|—||
|0|Global Error Injection Enable|
|GEIEN|This bit globally enables or disables the error injection function of the EIM. This field is initialized by<br>hardware reset.|
||0b - Disabled|
||1b - Enabled|



### 48.4.3 Error Injection Channel Enable register (EICHEN) 

#### Offset 

|Register|Offset|
|---|---|
|EICHEN|4h|



#### Function 

Each field of the Error Injection Channel Enable register (EICHEN) is used to enable or disable the corresponding error injection channel. 

~~<mark>NOTE</mark>~~ 

To enable an error injection channel, the Global Error Injection Enable (EIMCR[GEIEN]) field must also be asserted. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1632 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|EICH0<br>EN|EICH1<br>EN|EICH2<br>EN|EICH3<br>EN|EICH4<br>EN|EICH5<br>EN|EICH6<br>EN|EICH7<br>EN|EICH8<br>EN|EICH9<br>EN|EICH1<br>0EN|EICH1<br>1EN|EICH1<br>2EN|EICH1<br>3EN|EICH1<br>4EN|EICH1<br>5EN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|0|EICH1|EICH1|EICH1|EICH2|EICH2|0|EICH2|0|0|EICH2|EICH2|EICH2|EICH2|EICH3|EICH3|
|W||7EN|8EN|9EN|0EN|1EN||3EN|||6EN|7EN|8EN|9EN|0EN|1EN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31|Error Injection Channel 0 Enable|
|EICH0EN|This field enables the corresponding error injection channel. The Global Error Injection Enable<br>(EIMCR[GEIEN]) field must also be asserted to enable error injection.<br>After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined<br>in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection<br>channel is manually disabled via software.<br>Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN]<br>field, disabling the error injection channel.<br>0b - Error injection is disabled on Error Injection Channel 0<br>1b - Error injection is enabled on Error Injection Channel 0|
|30|Error Injection Channel 1 Enable|
|EICH1EN|This field enables the corresponding error injection channel. The Global Error Injection Enable<br>(EIMCR[GEIEN]) field must also be asserted to enable error injection.<br>After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined<br>in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection<br>channel is manually disabled via software.<br>Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN]<br>field, disabling the error injection channel.<br>0b - Error injection is disabled on Error Injection Channel 1<br>1b - Error injection is enabled on Error Injection Channel 1|
|29|Error Injection Channel 2 Enable|
|EICH2EN|This field enables the corresponding error injection channel. The Global Error Injection Enable<br>(EIMCR[GEIEN]) field must also be asserted to enable error injection.<br>After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined<br>in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection<br>channel is manually disabled via software.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1633 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Table continued from the previous page... 

|Field|Function<br>Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN]<br>field, disabling the error injection channel.<br>0b - Error injection is disabled on Error Injection Channel 2<br>1b - Error injection is enabled on Error Injection Channel 2|
|---|---|
|28<br>EICH3EN|Error Injection Channel 3 Enable<br>This field enables the corresponding error injection channel. The Global Error Injection Enable<br>(EIMCR[GEIEN]) field must also be asserted to enable error injection.<br>After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined<br>in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection<br>channel is manually disabled via software.<br>Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN]<br>field, disabling the error injection channel.<br>0b - Error injection is disabled on Error Injection Channel 3<br>1b - Error injection is enabled on Error Injection Channel 3|
|27<br>EICH4EN|Error Injection Channel 4 Enable<br>This field enables the corresponding error injection channel. The Global Error Injection Enable<br>(EIMCR[GEIEN]) field must also be asserted to enable error injection.<br>After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined<br>in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection<br>channel is manually disabled via software.<br>Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN]<br>field, disabling the error injection channel.<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>~~NOTE~~|
||Instance<br>Field supported in<br>Field not supported in|
||EIM_0<br>EICHEN<br>—|
||EIM_1<br>—<br>EICHEN|
||0b - Error injection is disabled on Error Injection Channel 4<br>1b - Error injection is enabled on Error Injection Channel 4|
|26|Error Injection Channel 5 Enable|
|EICH5EN|This field enables the corresponding error injection channel. The Global Error Injection Enable<br>(EIMCR[GEIEN]) field must also be asserted to enable error injection.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1634 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/048_Error_Injection_Module_-EIM-/S32K3XXRM_数据表.pdf-1635-03.png)


<!-- Start of picture text -->
Field Function<br>After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined<br>in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection<br>channel is manually disabled via software.<br>Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN]<br>field, disabling the error injection channel.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>EIM_0 — EICHEN<br>EIM_1 EICHEN —<br>0b - Error injection is disabled on Error Injection Channel 5<br>1b - Error injection is enabled on Error Injection Channel 5<br>25 Error Injection Channel 6 Enable<br>EICH6EN This field enables the corresponding error injection channel. The Global Error Injection Enable<br>(EIMCR[GEIEN]) field must also be asserted to enable error injection.<br>After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined<br>in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection<br>channel is manually disabled via software.<br>Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN]<br>field, disabling the error injection channel.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>EIM_0 — EICHEN<br>EIM_1 EICHEN —<br>0b - Error injection is disabled on Error Injection Channel 6<br>1b - Error injection is enabled on Error Injection Channel 6<br>24 Error Injection Channel 7 Enable<br>EICH7EN<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1635 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Table continued from the previous page... 

Field Function This field enables the corresponding error injection channel. The Global Error Injection Enable (EIMCR[GEIEN]) field must also be asserted to enable error injection. After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection channel is manually disabled via software. Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] field, disabling the error injection channel. ~~<mark>NOTE</mark>~~ This field is not supported in every instance. The following table includes only supported registers. Instance Field supported in Field not supported in EIM_0 — EICHEN EIM_1 EICHEN — 

- 0b - Error injection is disabled on Error Injection Channel 7 

1b - Error injection is enabled on Error Injection Channel 7 

23 Error Injection Channel 8 Enable EICH8EN This field enables the corresponding error injection channel. The Global Error Injection Enable (EIMCR[GEIEN]) field must also be asserted to enable error injection. After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection channel is manually disabled via software. 

Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] field, disabling the error injection channel. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

||Instance|Field supported in|Field not supported in|
|---|---|---|---|
|EIM_0||—|EICHEN|
|EIM_1||EICHEN|—|



- 0b - Error injection is disabled on Error Injection Channel 8 

- 1b - Error injection is enabled on Error Injection Channel 8 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1636 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Table continued from the previous page... 

|Field<br>22<br>EICH9EN|Function<br>Error Injection Channel 9 Enable<br>This field enables the corresponding error injection channel. The Global Error Injection Enable<br>(EIMCR[GEIEN]) field must also be asserted to enable error injection.<br>After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined<br>in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection<br>channel is manually disabled via software.<br>Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN]<br>field, disabling the error injection channel.<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>~~NOTE~~|
|---|---|
||Instance<br>Field supported in<br>Field not supported in|
||EIM_0<br>—<br>EICHEN|
||EIM_1<br>EICHEN<br>—<br>0b - Error injection is disabled on Error Injection Channel 9<br>1b - Error injection is enabled on Error Injection Channel 9|
|21<br>EICH10EN|Error Injection Channel 10 Enable<br>This field enables the corresponding error injection channel. The Global Error Injection Enable<br>(EIMCR[GEIEN]) field must also be asserted to enable error injection.<br>After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined<br>in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection<br>channel is manually disabled via software.<br>Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN]<br>field, disabling the error injection channel.<br>0b - Error injection is disabled on Error Injection Channel 10<br>1b - Error injection is enabled on Error Injection Channel 10|
|20<br>EICH11EN|Error Injection Channel 11 Enable<br>This field enables the corresponding error injection channel. The Global Error Injection Enable<br>(EIMCR[GEIEN]) field must also be asserted to enable error injection.<br>After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined<br>in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection<br>channel is manually disabled via software.<br>Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN]<br>field, disabling the error injection channel.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1637 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Error injection is disabled on Error Injection Channel 11<br>1b - Error injection is enabled on Error Injection Channel 11|
|19<br>EICH12EN|Error Injection Channel 12 Enable<br>This field enables the corresponding error injection channel. The Global Error Injection Enable<br>(EIMCR[GEIEN]) field must also be asserted to enable error injection.<br>After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined<br>in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection<br>channel is manually disabled via software.<br>Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN]<br>field, disabling the error injection channel.<br>0b - Error injection is disabled on Error Injection Channel 12<br>1b - Error injection is enabled on Error Injection Channel 12|
|18|Error Injection Channel 13 Enable|
|EICH13EN|This field enables the corresponding error injection channel. The Global Error Injection Enable<br>(EIMCR[GEIEN]) field must also be asserted to enable error injection.<br>After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined<br>in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection<br>channel is manually disabled via software.<br>Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN]<br>field, disabling the error injection channel.<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>~~NOTE~~|
||Instance<br>Field supported in<br>Field not supported in|
||EIM_0<br>—<br>EICHEN|
||EIM_1<br>EICHEN<br>—|
||0b - Error injection is disabled on Error Injection Channel 13<br>1b - Error injection is enabled on Error Injection Channel 13|
|17<br>EICH14EN|Error Injection Channel 14 Enable<br>This field enables the corresponding error injection channel. The Global Error Injection Enable<br>(EIMCR[GEIEN]) field must also be asserted to enable error injection.<br>After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined<br>in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection<br>channel is manually disabled via software.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1638 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/048_Error_Injection_Module_-EIM-/S32K3XXRM_数据表.pdf-1639-03.png)


<!-- Start of picture text -->
Field Function<br>Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN]<br>field, disabling the error injection channel.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>EIM_0 — EICHEN<br>EIM_1 EICHEN —<br>0b - Error injection is disabled on Error Injection Channel 14<br>1b - Error injection is enabled on Error Injection Channel 14<br>16 Error Injection Channel 15 Enable<br>EICH15EN This field enables the corresponding error injection channel. The Global Error Injection Enable<br>(EIMCR[GEIEN]) field must also be asserted to enable error injection.<br>After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined<br>in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection<br>channel is manually disabled via software.<br>Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN]<br>field, disabling the error injection channel.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>EIM_0 — EICHEN<br>EIM_1 EICHEN —<br>0b - Error injection is disabled on Error Injection Channel 15<br>1b - Error injection is enabled on Error Injection Channel 15<br>15 Reserved<br>—<br>14 Error Injection Channel 17 Enable<br>EICH17EN<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1639 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Table continued from the previous page... 

Field Function This field enables the corresponding error injection channel. The Global Error Injection Enable (EIMCR[GEIEN]) field must also be asserted to enable error injection. After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection channel is manually disabled via software. Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] field, disabling the error injection channel. ~~<mark>NOTE</mark>~~ This field is not supported in every instance. The following table includes only supported registers. Instance Field supported in Field not supported in EIM_0 — EICHEN EIM_1 EICHEN — 

- 0b - Error injection is disabled on Error Injection Channel 17 

1b - Error injection is enabled on Error Injection Channel 17 

13 Error Injection Channel 18 Enable EICH18EN This field enables the corresponding error injection channel. The Global Error Injection Enable (EIMCR[GEIEN]) field must also be asserted to enable error injection. After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection channel is manually disabled via software. 

Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] field, disabling the error injection channel. 

~~<mark>NOTE</mark>~~ 

This field is not supported in every instance. The following table includes only supported registers. 

||Instance|Field supported in|Field not supported in|
|---|---|---|---|
|EIM_0||—|EICHEN|
|EIM_1||EICHEN|—|




![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/048_Error_Injection_Module_-EIM-/S32K3XXRM_数据表.pdf-1640-11.png)


<!-- Start of picture text -->
0b - Error injection is disabled on Error Injection Channel 18<br><!-- End of picture text -->

- 1b - Error injection is enabled on Error Injection Channel 18 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1640 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|12|Error Injection Channel 19 Enable|
|EICH19EN|This field enables the corresponding error injection channel. The Global Error Injection Enable<br>(EIMCR[GEIEN]) field must also be asserted to enable error injection.<br>After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined<br>in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection<br>channel is manually disabled via software.<br>Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN]<br>field, disabling the error injection channel.|
||This field is not supported in every instance. The following table includes only<br>supported registers.<br>~~NOTE~~|
||Instance<br>Field supported in<br>Field not supported in|
||EIM_0<br>—<br>EICHEN|
||EIM_1<br>EICHEN<br>—|



0b - Error injection is disabled on Error Injection Channel 19 1b - Error injection is enabled on Error Injection Channel 19 11 Error Injection Channel 20 Enable EICH20EN This field enables the corresponding error injection channel. The Global Error Injection Enable (EIMCR[GEIEN]) field must also be asserted to enable error injection. After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection channel is manually disabled via software. Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] field, disabling the error injection channel. ~~<mark>NOTE</mark>~~ This field is not supported in every instance. The following table includes only supported registers. 

||Instance|Field supported in|Field not supported in|
|---|---|---|---|
|EIM_0||—|EICHEN|
|EIM_1||EICHEN|—|



0b - Error injection is disabled on Error Injection Channel 20 1b - Error injection is enabled on Error Injection Channel 20 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1641 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|10|Error Injection Channel 21 Enable|
|EICH21EN|This field enables the corresponding error injection channel. The Global Error Injection Enable<br>(EIMCR[GEIEN]) field must also be asserted to enable error injection.<br>After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined<br>in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection<br>channel is manually disabled via software.<br>Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN]<br>field, disabling the error injection channel.|
||This field is not supported in every instance. The following table includes only<br>supported registers.<br>~~NOTE~~|
||Instance<br>Field supported in<br>Field not supported in|
||EIM_0<br>—<br>EICHEN|
||EIM_1<br>EICHEN<br>—|



0b - Error injection is disabled on Error Injection Channel 21 1b - Error injection is enabled on Error Injection Channel 21 9 Reserved — 8 Error Injection Channel 23 Enable EICH23EN This field enables the corresponding error injection channel. The Global Error Injection Enable (EIMCR[GEIEN]) field must also be asserted to enable error injection. After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection channel is manually disabled via software. Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] field, disabling the error injection channel. ~~<mark>NOTE</mark>~~ This field is not supported in every instance. The following table includes only supported registers. Instance Field supported in Field not supported in EIM_0 — EICHEN EIM_1 EICHEN — 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1642 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/048_Error_Injection_Module_-EIM-/S32K3XXRM_数据表.pdf-1643-03.png)


<!-- Start of picture text -->
Field Function<br>Instance Field supported in Field not supported in<br>0b - Error injection is disabled on Error Injection Channel 23<br>1b - Error injection is enabled on Error Injection Channel 23<br>7 Reserved<br>—<br>6 Reserved<br>—<br>5 Error Injection Channel 26 Enable<br>EICH26EN This field enables the corresponding error injection channel. The Global Error Injection Enable<br>(EIMCR[GEIEN]) field must also be asserted to enable error injection.<br>After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined<br>in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection<br>channel is manually disabled via software.<br>Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN]<br>field, disabling the error injection channel.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>EIM_0 — EICHEN<br>EIM_1 EICHEN —<br>0b - Error injection is disabled on Error Injection Channel 26<br>1b - Error injection is enabled on Error Injection Channel 26<br>4 Error Injection Channel 27 Enable<br>EICH27EN This field enables the corresponding error injection channel. The Global Error Injection Enable<br>(EIMCR[GEIEN]) field must also be asserted to enable error injection.<br>After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined<br>in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection<br>channel is manually disabled via software.<br>Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN]<br>field, disabling the error injection channel.<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1643 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/048_Error_Injection_Module_-EIM-/S32K3XXRM_数据表.pdf-1644-03.png)


<!-- Start of picture text -->
Field Function<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>EIM_0 — EICHEN<br>EIM_1 EICHEN —<br>0b - Error injection is disabled on Error Injection Channel 27<br>1b - Error injection is enabled on Error Injection Channel 27<br>3 Error Injection Channel 28 Enable<br>EICH28EN This field enables the corresponding error injection channel. The Global Error Injection Enable<br>(EIMCR[GEIEN]) field must also be asserted to enable error injection.<br>After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined<br>in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection<br>channel is manually disabled via software.<br>Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN]<br>field, disabling the error injection channel.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>EIM_0 — EICHEN<br>EIM_1 EICHEN —<br>0b - Error injection is disabled on Error Injection Channel 28<br>1b - Error injection is enabled on Error Injection Channel 28<br>2 Error Injection Channel 29 Enable<br>EICH29EN This field enables the corresponding error injection channel. The Global Error Injection Enable<br>(EIMCR[GEIEN]) field must also be asserted to enable error injection.<br>After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined<br>in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection<br>channel is manually disabled via software.<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1644 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Table continued from the previous page... 

|Field|Function<br>Optionally, a hardware error event from the logic being injected by this c<br>if that feature is utilized at the instantiation of the EIM.<br>Any write to the corresponding EICHDn_WORD registers clears the c<br>field, disabling the error injection channel.<br>This field is not supported in every instance. The following table<br>supported registers.<br>~~NOTE~~|hannel can also disable the injection<br>orresponding EICHEN[EICHnEN]<br>includes only|
|---|---|---|
||Instance<br>Field supported in|Field not supported in|
||EIM_0<br>—|EICHEN|
||EIM_1<br>EICHEN|—|
||0b - Error injection is disabled on Error Injection Channel 29<br>1b - Error injection is enabled on Error Injection Channel 29||
|1|Error Injection Channel 30 Enable||
|EICH30EN|This field enables the corresponding error injection channel. The Glo<br>(EIMCR[GEIEN]) field must also be asserted to enable error injection<br>After error injection is enabled, all subsequent read accesses incur o<br>in the corresponding EICHDn_WORD registers. Error injection remai<br>channel is manually disabled via software.<br>Optionally, a hardware error event from the logic being injected by this c<br>if that feature is utilized at the instantiation of the EIM.<br>Any write to the corresponding EICHDn_WORD registers clears the c<br>field, disabling the error injection channel.<br>This field is not supported in every instance. The following table<br>supported registers.<br>~~NOTE~~|bal Error Injection Enable<br>.<br>ne or more bit inversions as defined<br>ns in effect until the error injection<br>hannel can also disable the injection<br>orresponding EICHEN[EICHnEN]<br>includes only|
||Instance<br>Field supported in|Field not supported in|
||EIM_0<br>—|EICHEN|
||EIM_1<br>EICHEN<br>0b - Error injection is disabled on Error Injection Channel 30<br>1b - Error injection is enabled on Error Injection Channel 30|—|
|0|Error Injection Channel 31 Enable||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1645 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Table continued from the previous page... 

Field Function EICH31EN This field enables the corresponding error injection channel. The Global Error Injection Enable (EIMCR[GEIEN]) field must also be asserted to enable error injection. After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection channel is manually disabled via software. Optionally, a hardware error event from the logic being injected by this channel can also disable the injection if that feature is utilized at the instantiation of the EIM. Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] field, disabling the error injection channel. ~~<mark>NOTE</mark>~~ This field is not supported in every instance. The following table includes only supported registers. 

||Instance|Field supported in|Field not supported in|
|---|---|---|---|
|EIM_0||—|EICHEN|
|EIM_1||EICHEN|—|



0b - Error injection is disabled on Error Injection Channel 31 

1b - Error injection is enabled on Error Injection Channel 31 

### 48.4.4 Error Injection Channel Descriptor 0, Word0 (EICHD0_WORD0) 

#### Offset 

|Register|Offset|
|---|---|
|EICHD0_WORD0|100h|



#### Function 

The first word of the Error Injection Channel Descriptor defines a left-justified mask field: CHKBIT_MASK. Each bit of CHKBIT_MASK specifies whether the corresponding bit of the checkbit bus from the target RAM should be inverted or remain unmodified on read accesses. Successful write to this field clears the corresponding error injection channel valid bit, EICHEN[EICHnEN]. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1646 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||||||CHKBIT|_MASK|||||||0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R||||||||0||||||||
|W||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



#### Fields 

|Field|Function|
|---|---|
|31-18|Checkbit Mask|
|CHKBIT_MASK|This field defines a bit-mapped mask that specifies whether the corresponding bit of the checkbit bus from<br>the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.<br>For any unique details about the mapping of CHKBIT_MASK's bits to a channel's target RAM, see the<br>chip-specific EIM information.|
||Because CHKBIT_MASK is left-justified, the highest bit in the bit range is always in the<br>position of the most significant bit. For CHKBIT_MASK[7:0] (8 bits wide), CHKBIT_MASK[7]<br>is in the position of the most significant bit.<br>~~NOTE~~|
||0b - The corresponding bit of the checkbit bus remains unmodified.<br>1b - The corresponding bit of the checkbit bus is inverted.<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>~~NOTE~~|



||Instance|Field supported in|Field not supported in|
|---|---|---|---|
||EIM_0|EICHD0_WORD0|—|
||EIM_1|EICHD0_WORD0[31–24]|EICHD0_WORD0[23–18]|
|17-0<br>—|Reserved|||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1647 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

### 48.4.5 Error Injection Channel Descriptor n, Word1 (EICHD0_WORD1 - EICHD4_WORD1) 

#### Offset 

|Register|Offset|
|---|---|
|EICHD0_WORD1|104h|
|EICHD1_WORD1|204h|
|EICHD2_WORD1|304h|
|EICHD3_WORD1|404h|
|EICHD4_WORD1|504h|



#### Function 

The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid field, EICHEN[EICHnEN]. 

~~<mark>NOTE</mark>~~ Each module instance supports a different number of registers. 

||Instance|Register supported|Register not supported|
|---|---|---|---|
|EIM_0||EICHD0_WORD1–EICHD4_WORD1|—|
|EIM_1||EICHD0_WORD1–EICHD3_WORD1|EICHD4_WORD1|



#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/048_Error_Injection_Module_-EIM-/S32K3XXRM_数据表.pdf-1648-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>B0_3DATA_MASK<br>W<br>Reset See Register reset values.<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>B0_3DATA_MASK<br>W<br>Reset See Register reset values.<br><!-- End of picture text -->

#### Register reset values 

|Register|Reset value|
|---|---|
|EICHD0_WORD1–EICHD3_WORD1|EIM_0,EIM_1: 0000_0000h|
|EICHD4_WORD1|0000_0000h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1648 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Fields 

|Field|Function||
|---|---|---|
|31-0|Data Mask Bytes 0-3||
|B0_3DATA_MA<br>SK|This field defines a bit-mapped mask that specifies whether the corre<br>the target RAM should be inverted or remain unmodified. Writes to u<br>For the specific DATA_MASK bits to which B0_3DATA_MASK<br>injection channel descriptor: DATA_MASK details.<br>~~NOTE~~|sponding bit of the read data bus from<br>nimplemented bits are ignored.<br>corresponds, See Error|
||0b - The corresponding bit of bytes 0-3 on the read data bus<br>1b - The corresponding bit of bytes 0-3 on the read data bus<br>This field is not supported in every instance. The following tabl<br>supported registers.<br>~~NOTE~~|remains unmodified.<br>is inverted.<br>e includes only|
||Instance<br>Field supported in|Field not supported in|
||EIM_0<br>EICHD0_WORD1[11–0]<br>EICHD1_WORD1<br>EICHD2_WORD1[7–0]<br>EICHD3_WORD1–EICHD4_WORD1|EICHD0_WORD1[31–12]<br>EICHD2_WORD1[31–8]|
||EIM_1<br>EICHD0_WORD1–EICHD3_WORD1|—|



### 48.4.6 Error Injection Channel Descriptor n, Word2 (EICHD0_WORD2 - EICHD23_WORD2) 

#### Offset 

|Register|Offset|
|---|---|
|EICHD0_WORD2|108h|
|EICHD1_WORD2|208h|
|EICHD2_WORD2|308h|
|EICHD3_WORD2|408h|
|EICHD4_WORD2|508h|
|EICHD5_WORD2|608h|
|EICHD6_WORD2|708h|
|EICHD7_WORD2|808h|
|EICHD8_WORD2|908h|
|EICHD9_WORD2|A08h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1649 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Table continued from the previous page... 

|Register|Offset|
|---|---|
|EICHD10_WORD2|B08h|
|EICHD11_WORD2|C08h|
|EICHD12_WORD2|D08h|
|EICHD13_WORD2|E08h|
|EICHD14_WORD2|F08h|
|EICHD15_WORD2|1008h|
|EICHD17_WORD2|1208h|
|EICHD18_WORD2|1308h|
|EICHD19_WORD2|1408h|
|EICHD20_WORD2|1508h|
|EICHD21_WORD2|1608h|
|EICHD23_WORD2|1808h|



#### Function 

The third word of the Error Injection Channel Descriptor, when present, defines a right-justified mask field. The bits in B4_7DATA_MASK correspond to bytes 4–7 of the read data bus. Each bit specifies whether the corresponding bit of the read data bus from the target RAM should be inverted or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid field, EICHEN[EICHnEN]. 

~~<mark>NOTE</mark>~~ Each module instance supports a different number of registers. 

|||Instan|ce|||Register sup|ported||Re|gister n|ot supp|orted||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|EIM_0||||||EICHD0_WORD2–EICHD4_<br>EICHD10_WORD2|WORD2||EICHD5_WO<br>EICHD11_WO|RD2–EICH<br>RD2–EIC|D9_WO<br>HD23_W|RD2<br>ORD2||
|EIM_1||||||EICHD0_WORD2–EICHD23_|WORD2||EICHD4_WO|RD2||||
|Diagram<br>Bits|31|30|29|28|27|26<br>25<br>24|23|22|21<br>20|19|18|17|16|
|R<br>W||||||B4_7DA|TA_MASK|||||||
|Reset||||||SeeRegister|reset valu|es.||||||
|Bits|15|14|13|12|11|10<br>9<br>8|7|6|5<br>4|3|2|1|0|
|R<br>W||||||B4_7DA|TA_MASK|||||||
|Reset||||||SeeRegister|reset valu|es.||||||



#### Diagram 

See Register reset values. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1650 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Register reset values 

|Register|Reset value|
|---|---|
|EICHD0_WORD2–EICHD3_WORD2|EIM_0,EIM_1: 0000_0000h|
|EICHD4_WORD2|0000_0000h|
|EICHD5_WORD2–EICHD9_WORD2|0000_0000h|
|EICHD6_WORD2–EICHD23_WORD2|Register not supported|
|EICHD10_WORD2|EIM_0,EIM_1: 0000_0000h|
|EICHD11_WORD2–EICHD23_WORD2|0000_0000h|



#### Fields 

|Field|Function|
|---|---|
|31-0|Data Mask Bytes 4-7|
|B4_7DATA_MA<br>SK|This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from<br>the target RAM should be inverted or remain unmodified.|
||For each channel: For the specific DATA_MASK bits to which B4_7DATA_MASK<br>corresponds, See Error injection channel descriptor: DATA_MASK details.<br>~~NOTE~~|
||0b - The corresponding bit of bytes 4-7 on the read data bus remains unmodified.|
||1b - The corresponding bit of bytes 4-7 on the read data bus is inverted.|



### 48.4.7 Error Injection Channel Descriptor 1, Word0 (EICHD1_WORD0) 

#### Offset 

|Register|Offset|
|---|---|
|EICHD1_WORD0|200h|



#### Function 

The first word of the Error Injection Channel Descriptor defines a left-justified mask field: CHKBIT_MASK. Each bit of CHKBIT_MASK specifies whether the corresponding bit of the checkbit bus from the target RAM should be inverted or remain unmodified on read accesses. Successful write to this field clears the corresponding error injection channel valid bit, EICHEN[EICHnEN]. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1651 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/048_Error_Injection_Module_-EIM-/S32K3XXRM_数据表.pdf-1652-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>CHKBIT_MASK<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function||
|---|---|---|
|31-16|Checkbit Mask||
|CHKBIT_MASK|This field defines a bit-mapped mask that specifies whether the corre<br>the target RAM should be inverted or remain unmodified. Writes to u<br>For any unique details about the mapping of CHKBIT_MASK's bits t<br>chip-specific EIM information.<br>Because CHKBIT_MASK is left-justified, the highest bit in the<br>position of the most significant bit. For CHKBIT_MASK[7:0] (8 b<br>is in the position of the most significant bit.<br>~~NOTE~~<br>0b - The corresponding bit of the checkbit bus remains unmo<br>1b - The corresponding bit of the checkbit bus is inverted.<br>This field is not supported in every instance. The following tab<br>supported registers.<br>~~NOTE~~|sponding bit of the checkbit bus from<br>nimplemented bits are ignored.<br>o a channel's target RAM, see the<br>bit range is always in the<br>its wide), CHKBIT_MASK[7]<br>dified.<br>le includes only|
||Instance<br>Field supported in|Field not supported in|
||EIM_0<br>EICHD1_WORD0|—|
||EIM_1<br>EICHD1_WORD0[31–24]|EICHD1_WORD0[23–16]|
|15-0<br>—|Reserved||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1652 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

### 48.4.8 Error Injection Channel Descriptor n, Word3 (EICHD1_WORD3 - EICHD23_WORD3) 

#### Offset 

|Register|Offset|
|---|---|
|EICHD1_WORD3|20Ch|
|EICHD2_WORD3|30Ch|
|EICHD3_WORD3|40Ch|
|EICHD4_WORD3|50Ch|
|EICHD6_WORD3|70Ch|
|EICHD12_WORD3|D0Ch|
|EICHD13_WORD3|E0Ch|
|EICHD14_WORD3|F0Ch|
|EICHD23_WORD3|180Ch|



#### Function 

The fourth word of the Error Injection Channel Descriptor, when present, defines a right-justified mask field. The bits in B8_11DATA_MASK correspond to bytes 8–11 of the read data bus. Each bit specifies whether the corresponding bit of the read data bus from the target RAM should be inverted or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid field, EICHEN[EICHnEN]. 

~~<mark>NOTE</mark>~~ Each module instance supports a different number of registers. 

|||Instan|ce||||Register sup|ported||Re|gister n|ot supp|orted||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|EIM_0||||||EICHD1_W|ORD3–EICHD4_|WORD3||EICHD6_WOR|D3–EICH|D23_W|ORD3||
|EIM_1||||||EICHD6_W|ORD3–EICHD23_|WORD3||EICHD1_WOR|D3–EICH|D4_WO|RD3||
|Diagram<br>Bits|31|30|29|28|27|26|25<br>24|23|22|21<br>20|19|18|17|16|
|R<br>W|||||||B8_11DA|TA_MASK|||||||
|Reset|||||||SeeRegister|reset valu|es.||||||
|Bits|15|14|13|12|11|10|9<br>8|7|6|5<br>4|3|2|1|0|
|R<br>W|||||||B8_11DA|TA_MASK|||||||
|Reset|||||||SeeRegiste|reset valu|es.||||||



#### Diagram 

See Register reset values. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1653 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Register reset values 

|Register|Reset value|
|---|---|
|EICHD1_WORD3–EICHD4_WORD3|0000_0000h|
|EICHD6_WORD3–EICHD23_WORD3|0000_0000h|
|EICHD23_WORD3|Register not supported|



#### Fields 

|Field|Function|
|---|---|
|31-0|Data Mask Bytes 8-11|
|B8_11DATA_M<br>ASK|This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from<br>the target RAM should be inverted or remain unmodified.|
||For each channel: For the specific DATA_MASK bits to which B8_11DATA_MASK<br>corresponds, See Error injection channel descriptor: DATA_MASK details.<br>~~NOTE~~|
||0b - The corresponding bit of bytes 8-11 on the read data bus remains unmodified.|
||1b - The corresponding bit of bytes 8-11 on the read data bus is inverted.|



### 48.4.9 Error Injection Channel Descriptor n, Word4 (EICHD1_WORD4 - EICHD23_WORD4) 

#### Offset 

|Register|Offset|
|---|---|
|EICHD1_WORD4|210h|
|EICHD2_WORD4|310h|
|EICHD3_WORD4|410h|
|EICHD4_WORD4|510h|
|EICHD6_WORD4|710h|
|EICHD12_WORD4|D10h|
|EICHD13_WORD4|E10h|
|EICHD14_WORD4|F10h|
|EICHD23_WORD4|1810h|



#### Function 

The fifth word of the Error Injection Channel Descriptor, when present, defines a right-justified mask field. The bits in B12_15DATA_MASK correspond to bytes 12–15 of the read data bus. Each bit specifies whether the corresponding bit of the read data bus from the target RAM should be inverted or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid field, EICHEN[EICHnEN]. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1654 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/048_Error_Injection_Module_-EIM-/S32K3XXRM_数据表.pdf-1655-04.png)


<!-- Start of picture text -->
Instance Register supported Register not supported<br>EIM_0 EICHD1_WORD4–EICHD4_WORD4 EICHD6_WORD4–EICHD23_WORD4<br>EIM_1 EICHD6_WORD4–EICHD23_WORD4 EICHD1_WORD4–EICHD4_WORD4<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>B12_15DATA_MASK<br>W<br>Reset See Register reset values.<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>B12_15DATA_MASK<br>W<br>Reset See Register reset values.<br><!-- End of picture text -->

#### Register reset values 

|Register|Reset value|
|---|---|
|EICHD1_WORD4–EICHD4_WORD4|0000_0000h|
|EICHD6_WORD4–EICHD23_WORD4|0000_0000h|
|EICHD23_WORD4|Register not supported|



#### Fields 

|Field|Function|
|---|---|
|31-0|Data Mask Bytes 12-15|
|B12_15DATA_<br>MASK|This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from<br>the target RAM should be inverted or remain unmodified.|
||For each channel: For the specific DATA_MASK bits to which B12_15DATA_MASK<br>corresponds, See Error injection channel descriptor: DATA_MASK details.<br>~~NOTE~~|
||0b - The corresponding bit of bytes 12-15 on the read data bus remains unmodified.|
||1b - The corresponding bit of bytes 12-15 on the read data bus is inverted.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1655 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

### 48.4.10 Error Injection Channel Descriptor n, Word0 (EICHD2_WORD0 - EICHD4_WORD0) 

#### Offset 

|Register|Offset|
|---|---|
|EICHD2_WORD0|300h|
|EICHD3_WORD0|400h|
|EICHD4_WORD0|500h|



#### Function 

The first word of the Error Injection Channel Descriptor defines a left-justified mask field: CHKBIT_MASK. Each bit of CHKBIT_MASK specifies whether the corresponding bit of the checkbit bus from the target RAM should be inverted or remain unmodified on read accesses. Successful write to this field clears the corresponding error injection channel valid bit, EICHEN[EICHnEN]. 

~~<mark>NOTE</mark>~~ Each module instance supports a different number of registers. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/048_Error_Injection_Module_-EIM-/S32K3XXRM_数据表.pdf-1656-08.png)


<!-- Start of picture text -->
Instance Register supported Register not supported<br>EIM_0 EICHD2_WORD0–EICHD4_WORD0 —<br>EIM_1 EICHD2_WORD0–EICHD3_WORD0 EICHD4_WORD0<br><!-- End of picture text -->

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/048_Error_Injection_Module_-EIM-/S32K3XXRM_数据表.pdf-1656-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>CHKBIT_MASK<br>W<br>Reset See Register reset values.<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>CHKBIT_MASK<br>W<br>Reset See Register reset values.<br><!-- End of picture text -->

#### Register reset values 

|Register|Reset value|
|---|---|
|EICHD2_WORD0–EICHD3_WORD0|EIM_0,EIM_1: 0000_0000h|
|EICHD4_WORD0|0000_0000h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1656 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Fields 

Field Function 31-4 Checkbit Mask CHKBIT_MASK This field defines a bit-mapped mask that specifies whether the corresponding bit of the checkbit bus from the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored. For any unique details about the mapping of CHKBIT_MASK's bits to a channel's target RAM, see the chip-specific EIM information. ~~<mark>NOTE</mark>~~ Because CHKBIT_MASK is left-justified, the highest bit in the bit range is always in the position of the most significant bit. For CHKBIT_MASK[7:0] (8 bits wide), CHKBIT_MASK[7] is in the position of the most significant bit. 0b - The corresponding bit of the checkbit bus remains unmodified. 1b - The corresponding bit of the checkbit bus is inverted. ~~<mark>NOTE</mark>~~ This field is not supported in every instance. The following table includes only supported registers. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/048_Error_Injection_Module_-EIM-/S32K3XXRM_数据表.pdf-1657-04.png)


<!-- Start of picture text -->
31-4 Checkbit Mask<br>CHKBIT_MASK This field defines a bit-mapped mask that specifies whether the corresponding bit of the checkbit bus from<br>the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.<br>For any unique details about the mapping of CHKBIT_MASK's bits to a channel's target RAM, see the<br>chip-specific EIM information.<br>  NOTE<br>Because CHKBIT_MASK is left-justified, the highest bit in the bit range is always in the<br>position of the most significant bit. For CHKBIT_MASK[7:0] (8 bits wide), CHKBIT_MASK[7]<br>is in the position of the most significant bit.<br>0b - The corresponding bit of the checkbit bus remains unmodified.<br>1b - The corresponding bit of the checkbit bus is inverted.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>EIM_0 EICHD2_WORD0–EICHD4_WORD0 —<br>EIM_1 EICHD2_WORD0– EICHD2_WORD0–<br>EICHD3_WORD0[31–24] EICHD3_WORD0[23–4]<br>3-0 Reserved<br>—<br><!-- End of picture text -->

### 48.4.11 Error Injection Channel Descriptor n, Word1 (EICHD5_WORD1 - EICHD9_WORD1) 

#### Offset 

|Register|Offset|
|---|---|
|EICHD5_WORD1|604h|
|EICHD6_WORD1|704h|
|EICHD7_WORD1|804h|
|EICHD8_WORD1|904h|
|EICHD9_WORD1|A04h|



#### Function 

The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1657 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid field, EICHEN[EICHnEN]. 

~~<mark>NOTE</mark>~~ Each module instance supports a different number of registers. 

|||Instan|ce||||Regis|ter sup|ported|||Re|gister n|ot sup|ported||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|EIM_0||||||—|||||EICHD|5_WOR|D1–EICH|D9_WO|RD1||
|EIM_1||||||EICHD5_W|ORD1–E|ICHD9_W|ORD1||—||||||
|Diagram<br>Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|R<br>W||0|||||||B0|_3DAT|A_MASK||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||B0_3DAT|A_MASK||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Diagram 

#### Fields 

|Field|Function|
|---|---|
|31-28|Reserved|
|—||
|27-0|Data Mask Bytes 0-3|
|B0_3DATA_MA<br>SK|This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from<br>the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.<br>For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error<br>injection channel descriptor: DATA_MASK details.<br>~~NOTE~~|
||0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.|
||1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1658 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

### 48.4.12 Error Injection Channel Descriptor n, Word5 (EICHD6_WORD5 - EICHD23_WORD5) 

#### Offset 

|Register|Offset|
|---|---|
|EICHD6_WORD5|714h|
|EICHD12_WORD5|D14h|
|EICHD13_WORD5|E14h|
|EICHD14_WORD5|F14h|
|EICHD23_WORD5|1814h|



#### Function 

The sixth word of the Error Injection Channel Descriptor, when present, defines a right-justified mask field. The bits in B16_19DATA_MASK correspond to bytes 16–19 of the read data bus. Each bit specifies whether the corresponding bit of the read data bus from the target RAM should be inverted or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid field, EICHEN[EICHnEN]. 

~~<mark>NOTE</mark>~~ Each module instance supports a different number of registers. 

||Instance|Register supported|Register not supported|
|---|---|---|---|
|EIM_0||—|EICHD6_WORD5–EICHD23_WORD5|
|EIM_1||EICHD6_WORD5–EICHD23_WORD5|—|



#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/048_Error_Injection_Module_-EIM-/S32K3XXRM_数据表.pdf-1659-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>B16_19DATA_MASK<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>B16_19DATA_MASK<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-0|Data Mask Bytes 16-19|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1659 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

|Field|Function|
|---|---|
|B16_19DATA_<br>MASK|This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from<br>the target RAM should be inverted or remain unmodified.|
||For each channel: For the specific DATA_MASK bits to which B16_19DATA_MASK<br>corresponds, See Error injection channel descriptor: DATA_MASK details.<br>~~NOTE~~|
||0b - The corresponding bit of bytes 16-19 on the read data bus remains unmodified.|
||1b - The corresponding bit of bytes 16-19 on the read data bus is inverted.|



### 48.4.13 Error Injection Channel Descriptor n, Word6 (EICHD6_WORD6 - EICHD23_WORD6) 

#### Offset 

|Register|Offset|
|---|---|
|EICHD6_WORD6|718h|
|EICHD12_WORD6|D18h|
|EICHD13_WORD6|E18h|
|EICHD14_WORD6|F18h|
|EICHD23_WORD6|1818h|



#### Function 

The seventh word of the Error Injection Channel Descriptor, when present, defines a right-justified mask field. The bits in B20_23DATA_MASK correspond to bytes 20–23 of the read data bus. Each bit specifies whether the corresponding bit of the read data bus from the target RAM should be inverted or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid field, EICHEN[EICHnEN]. 

~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

||Instance|Register supported|Register not supported|
|---|---|---|---|
|EIM_0||—|EICHD6_WORD6–EICHD23_WORD6|
|EIM_1||EICHD6_WORD6–EICHD23_WORD6|—|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1660 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/048_Error_Injection_Module_-EIM-/S32K3XXRM_数据表.pdf-1661-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>B20_23DATA_MASK<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>B20_23DATA_MASK<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-0|Data Mask Bytes 20-23|
|B20_23DATA_<br>MASK|This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from<br>the target RAM should be inverted or remain unmodified.|
||For each channel: For the specific DATA_MASK bits to which B20_23DATA_MASK<br>corresponds, See Error injection channel descriptor: DATA_MASK details.<br>~~NOTE~~|
||0b - The corresponding bit of bytes 20-23 on the read data bus remains unmodified.|
||1b - The corresponding bit of bytes 20-23 on the read data bus is inverted.|



### 48.4.14 Error Injection Channel Descriptor n, Word0 (EICHD10_WORD0 - EICHD12_WORD0) 

#### Offset 

|Register|Offset|
|---|---|
|EICHD10_WORD0|B00h|
|EICHD11_WORD0|C00h|
|EICHD12_WORD0|D00h|



#### Function 

The first word of the Error Injection Channel Descriptor defines a left-justified mask field: CHKBIT_MASK. Each bit of CHKBIT_MASK specifies whether the corresponding bit of the checkbit bus from the target RAM should be inverted or remain unmodified on read accesses. Successful write to this field clears the corresponding error injection channel valid bit, EICHEN[EICHnEN]. 

~~<mark>NOTE</mark>~~ Each module instance supports a different number of registers. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1661 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

||Instance|Register supported|Register not supported|
|---|---|---|---|
|EIM_0||EICHD10_WORD0–EICHD12_WORD0|—|
|EIM_1||—|EICHD10_WORD0–EICHD12_WORD0|



#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||CHKBIT|_MASK|||||||0|||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-24|Checkbit Mask|
|CHKBIT_MASK|This field defines a bit-mapped mask that specifies whether the corresponding bit of the checkbit bus from<br>the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.<br>For any unique details about the mapping of CHKBIT_MASK's bits to a channel's target RAM, see the<br>chip-specific EIM information.<br>Because CHKBIT_MASK is left-justified, the highest bit in the bit range is always in the<br>position of the most significant bit. For CHKBIT_MASK[7:0] (8 bits wide), CHKBIT_MASK[7]<br>is in the position of the most significant bit.<br>~~NOTE~~|
||0b - The corresponding bit of the checkbit bus remains unmodified.<br>1b - The corresponding bit of the checkbit bus is inverted.|
|23-0<br>—|Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1662 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

### 48.4.15 Error Injection Channel Descriptor n, Word1 (EICHD10_WORD1 - EICHD12_WORD1) 

#### Offset 

|Register|Offset|
|---|---|
|EICHD10_WORD1|B04h|
|EICHD11_WORD1|C04h|
|EICHD12_WORD1|D04h|



#### Function 

The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid field, EICHEN[EICHnEN]. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||B0_3DAT|A_MASK||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||B0_3DAT|A_MASK||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-0|Data Mask Bytes 0-3|
|B0_3DATA_MA<br>SK|This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from<br>the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.|
||For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error<br>injection channel descriptor: DATA_MASK details.<br>~~NOTE~~|
||0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.<br>1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.|
||This field is not supported in every instance. The following table includes only<br>supported registers.<br>~~NOTE~~|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1663 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

|Field|Function|||
|---|---|---|---|
||Instance|Field supported in|Field not supported in|
||EIM_0|EICHD10_WORD1–EICHD12_WORD1|—|
||EIM_1|EICHD10_WORD1–|EICHD10_WORD1–|
|||EICHD12_WORD1[27–0]|EICHD12_WORD1[31–28]|



### 48.4.16 Error Injection Channel Descriptor n, Word1 (EICHD13_WORD1 - EICHD23_WORD1) 

#### Offset 

|Register|Offset|
|---|---|
|EICHD13_WORD1|E04h|
|EICHD14_WORD1|F04h|
|EICHD15_WORD1|1004h|
|EICHD17_WORD1|1204h|
|EICHD18_WORD1|1304h|
|EICHD19_WORD1|1404h|
|EICHD20_WORD1|1504h|
|EICHD21_WORD1|1604h|
|EICHD23_WORD1|1804h|



#### Function 

The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid field, EICHEN[EICHnEN]. 

~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

||Instance|Register supported|Register not supported|
|---|---|---|---|
|EIM_0||—|EICHD13_WORD1–EICHD23_WORD1|
|EIM_1||EICHD13_WORD1–EICHD23_WORD1|—|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1664 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/048_Error_Injection_Module_-EIM-/S32K3XXRM_数据表.pdf-1665-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>B0_3DATA_MASK<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>B0_3DATA_MASK<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-28|Reserved|
|—||
|27-0|Data Mask Bytes 0-3|
|B0_3DATA_MA<br>SK|This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from<br>the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.|
||For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error<br>injection channel descriptor: DATA_MASK details.<br>~~NOTE~~|
||0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.|
||1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.|



### 48.4.17 Error Injection Channel Descriptor 26, Word1 (EICHD26_WORD1) 

#### Offset 

|Register|Offset|
|---|---|
|EICHD26_WORD1|1B04h|



#### Function 

The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid field, EICHEN[EICHnEN]. 

~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1665 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

||Instance|Register supported|Register not supported|
|---|---|---|---|
|EIM_0||—|EICHD26_WORD1|
|EIM_1||EICHD26_WORD1|—|



#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||0|||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||||0||||||||B0_3DAT|A_MASK|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-6|Reserved|
|—||
|5-0|Data Mask Bytes 0-3|
|B0_3DATA_MA<br>SK|This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from<br>the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.|
||For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error<br>injection channel descriptor: DATA_MASK details.<br>~~NOTE~~|
||0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.|
||1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.|



### 48.4.18 Error Injection Channel Descriptor 27, Word1 (EICHD27_WORD1) 

#### Offset 

|Register|Offset|
|---|---|
|EICHD27_WORD1|1C04h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1666 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Function 

The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid field, EICHEN[EICHnEN]. 

~~<mark>NOTE</mark>~~ Each module instance supports a different number of registers. 

|||Insta|nce||||Regist|er sup|ported|||Re|gister n|ot supp|orted||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|EIM_0||||||—|||||EICH|D27_WO|RD1||||
|EIM_1<br>Diagram||||||EICHD27_|WORD1||||—||||||
|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||||0|||||||B03DA|AMASK||
|W||||||||||||||_|_||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Diagram 

#### Fields 

|Field|Function|
|---|---|
|31-4|Reserved|
|—||
|3-0|Data Mask Bytes 0-3|
|B0_3DATA_MA<br>SK|This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from<br>the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.|
||For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error<br>injection channel descriptor: DATA_MASK details.<br>~~NOTE~~|
||0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.|
||1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1667 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

### 48.4.19 Error Injection Channel Descriptor 28, Word1 (EICHD28_WORD1) 

#### Offset 

|Register|Offset|
|---|---|
|EICHD28_WORD1|1D04h|



#### Function 

The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid field, EICHEN[EICHnEN]. 

~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

||Instance|Register supported|Register not supported|
|---|---|---|---|
|EIM_0||—|EICHD28_WORD1|
|EIM_1||EICHD28_WORD1|—|



#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/048_Error_Injection_Module_-EIM-/S32K3XXRM_数据表.pdf-1668-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>B0_3DATA_MASK<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-6|Reserved|
|—||
|5-0|Data Mask Bytes 0-3|
|B0_3DATA_MA<br>SK|This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from<br>the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1668 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||~~NOTE~~|
||For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error<br>injection channel descriptor: DATA_MASK details.|
||0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.|
||1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.|



### 48.4.20 Error Injection Channel Descriptor 29, Word1 (EICHD29_WORD1) 

#### Offset 

|Register|Offset|
|---|---|
|EICHD29_WORD1|1E04h|



#### Function 

The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid field, EICHEN[EICHnEN]. 

~~<mark>NOTE</mark>~~ Each module instance supports a different number of registers. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/048_Error_Injection_Module_-EIM-/S32K3XXRM_数据表.pdf-1669-10.png)


<!-- Start of picture text -->
Instance Register supported Register not supported<br>EIM_0 — EICHD29_WORD1<br>EIM_1 EICHD29_WORD1 —<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>B0_3DATA_MASK<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>B0_3DATA_MASK<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1669 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Fields 

|Field|Function|
|---|---|
|31-28|Reserved|
|—||
|27-0|Data Mask Bytes 0-3|
|B0_3DATA_MA<br>SK|This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from<br>the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.|
||For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error<br>injection channel descriptor: DATA_MASK details.<br>~~NOTE~~|
||0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.|
||1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.|



### 48.4.21 Error Injection Channel Descriptor n, Word1 (EICHD30_WORD1 - EICHD31_WORD1) 

#### Offset 

|Register|Offset|
|---|---|
|EICHD30_WORD1|1F04h|
|EICHD31_WORD1|2004h|



#### Function 

The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid field, EICHEN[EICHnEN]. 

|~~NOTE~~|
|---|



Each module instance supports a different number of registers. 

||Instance|Register supported|Register not supported|
|---|---|---|---|
|EIM_0||—|EICHD30_WORD1–EICHD31_WORD1|
|EIM_1||EICHD30_WORD1–EICHD31_WORD1|—|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1670 / 4640 

NXP Semiconductors 

Error Injection Module (EIM) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17||16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||B0_3D|AT|A_MA|
|W||||||||||||||||SK||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0||0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1||0|
|R<br>W||||||||B0_3DAT|A_MASK|||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0||0|



#### Fields 

|Field|Function|
|---|---|
|31-18|Reserved|
|—||
|17-0|Data Mask Bytes 0-3|
|B0_3DATA_MA<br>SK|This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from<br>the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.|
||For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error<br>injection channel descriptor: DATA_MASK details.<br>~~NOTE~~|
||0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.|
||1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.|



## 48.5 Glossary 

SEC-DED Single error correct – dual error detect ECC Error correction code 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1671 / 4640 

