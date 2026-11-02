NXP Semiconductors 

# Chapter 52 Self-Test Control Unit (STCU2) 

## 52.1 Chip-specific STCU2 information 

### 52.1.1 Supported BIST sequences 

This chip supports only STCU2 BIST sequences that NXP has validated for in-field testing usage. The detailed programming sequences for supported configurations are available in a separate application note (contact your NXP sales representative for this information). 

### 52.1.2 Self-test overview 

STCU2 provides the overall control of both LBIST and MBIST, in serial or parallel, depending on the power, timing, or coverage constraints. 

~~<mark>NOTE</mark>~~ 

LBIST is not available for S32K312 and S32K311. 

The application software initiates the self-test sequence or procedure (please use whichever term is correct), and has provisions to bypass the self-test configuration to directly move to normal Run mode. 

There is a programmable BIST-sequence-execution watchdog timer that specifies the maximum time allowed for the execution of a BIST sequence. In case the selected LBISTs or MBISTs are not complete during the assigned time, the current LBISTs or MBISTs execution is interrupted and a failure is flagged into ERR_STAT[WDTOSW] and MBESWx or LBESW. 

The STCU2 execution includes three phases: 

- Software configuration. Load or program the test configuration parameters to be executed, depending on ASIL target and performance requirements. The self-test configuration parameters allow the self-test sequence to run with different times depending on pattern numbers and types, achieving different levels of coverage. 

- Start of BIST execution. This involves software register configuration in STCU2. The BIST completion is followed by a functional reset. 

- End of BIST execution. After BIST execution and functional reset are complete, the BIST results are made available and you decide how to continue (trigger a new reset or start a safety application). The BIST execution completion is signalized in an internal STCU2 register (LBESWn) bit which is not affected by the functional reset. The BIST test results are also not affected by the functional reset. 

The following figure shows a pictorial representation of two LBIST partitions having two and one MBIST groups, respectively. STCU2 interacts with LBIST_CTRL for the respective partitions to configure and control the LBIST sequence and compare results. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1782 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

It also interacts with MTR controller (MCT) for MBIST. Each LBIST partition has its corresponding controller whereas a single MCT can cater to multiple MBIST groups. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/052_Self-Test_Control_Unit_-STCU2-/S32K3XXRM_数据表.pdf-1783-03.png)


<!-- Start of picture text -->
Figure 191. Logical partitions Other functional<br>blocks<br>MCT<br>MBIST C<br>MBIST A MBIST B<br>LBIST_CTRL LBIST_CTRL<br>STCU2<br>Self-test overview<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/052_Self-Test_Control_Unit_-STCU2-/S32K3XXRM_数据表.pdf-1783-04.png)


<!-- Start of picture text -->
  NOTE<br><!-- End of picture text -->

LBIST_CTRL is not available for S32K312 and S32K311. 

Each LBIST partition also includes a block called Self-test GPR involving a set of registers that provide miscellaneous configuration and parameter details for an LBIST operation. 

When you trigger a self-test sequence, the chip becomes unavailable for software application during the self-test run. 

### 52.1.3 STCU2 LBIST/MBIST mapping 

This topic covers STCU2 LBIST/MBIST mapping. 

##### LBIST mapping 

The below table lists the LBIST mapping of the chip. The NLBIST value is 1. 

Table 249. LBIST mapping 

|BIST ID<br>(NLBIST)|BIST instance<br>name|Modules|
|---|---|---|
|0|LBIST|DMA:|
|||• DMA controller|
|||EIM|
|||ERM|
|||XRDC|
|||• MDAC0|
|||• MDAC1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1783 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

##### Table 249. LBIST mapping (continued) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/052_Self-Test_Control_Unit_-STCU2-/S32K3XXRM_数据表.pdf-1784-03.png)


<!-- Start of picture text -->
BIST ID  BIST instance  Modules<br>(NLBIST) name<br>• MDAC2<br>• MDAC3<br>• MDAC4<br>• MDAC5<br>• MRC0<br>• MRC1<br>• MRC2<br>• PDAC0<br>• PDAC1<br>• PDAC2<br>CRC<br>FCCU<br>FOSU<br>PFLASH_CTL<br>PRAMC_0<br>PRAMC_1<br>  NOTE<br>PRAMC_1 is not present in S32K342, S32K312, and S32K311.<br>SWT_1<br>  NOTE<br>SWT_1 is not present in S32K312 and S32K311.<br>CMU:<br>• CMU1<br>• CMU2<br>• CMU4<br>• CMU5<br>iAHB Gaskets:<br>• DMA_GSKT<br>• HSE_GSKT<br>• AIPS1_GSKT<br>• AIPS2_GSKT<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1784 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

Table 249. LBIST mapping (continued) 

|BIST ID<br>(NLBIST)|BIST instance<br>name|Modules|
|---|---|---|
|||• QSPI_GSKT|
|||AIPS2_GSKT and QSPI_GSKT are not present in S32K312<br>and S32K311.<br>~~NOTE~~|
|||• TCM_GSKT|
|||• EMAC_GSKT<br>• EDC master checker gaskets (See block diagram in Introduction chapter for details)<br>• EDC slave checker gasket (See block diagram in Introduction chapter for details)|
|||Crossbars|
|||• AXBS|
|||• DMA_AXBS<br>• HSE_AXBS|
|||• PERIPHERAL_AXBS|
|||• TCM_AXBS|



##### MBIST mapping 

The below tables lists the MBIST mapping of different variants of this chip. The NMCUT value is 12. 

Table 250. S32K314/S32K324/S32K344 MBIST mapping 

|BIST<br>index (NMCUT)|BIST name|Memory<br>index|Memory instance name|
|---|---|---|---|
|0|SYS0_RAMS|0|PRAM0 block 1|
|0|SYS0_RAMS|1|PRAM0 block 2|
|1|SYS1_RAMS|0|PRAM1 block 1|
|1|SYS1_RAMS|1|PRAM1 block 2|
|2|DMA_TCD_RAM|0|DMA TCD RAM|
|3|CM7_0_TOP|0|CM7_0 instruction cache data block 1|
|3|CM7_0_TOP|1|CM7_0 instruction cache data block 2|
|3|CM7_0_TOP|2|CM7_0 instruction cache tag block 1|
|3|CM7_0_TOP|3|CM7_0 instruction cache tag block 2|
|3|CM7_0_TOP|4|CM7_0 data cache data block 1|
|3|CM7_0_TOP|4|CM7_0 data cache data block 2|
|3|CM7_0_TOP|5|CM7_0 data cache data block 3|
|3|CM7_0_TOP|5|CM7_0 data cache data block 4|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1785 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

Table 250. S32K314/S32K324/S32K344 MBIST mapping (continued) 

|BIST<br>index (NMCUT)|BIST name|Memory<br>index|Memory instance name|
|---|---|---|---|
|3|CM7_0_TOP|6|CM7_0 data cache data block 5|
|3|CM7_0_TOP|6|CM7_0 data cache data block 6|
|3|CM7_0_TOP|7|CM7_0 data cache data block 7|
|3|CM7_0_TOP|7|CM7_0 data cache data block 8|
|3|CM7_0_TOP|8|CM7_0 data cache tag block 1|
|3|CM7_0_TOP|9|CM7_0 data cache tag block 2|
|3|CM7_0_TOP|10|CM7_0 data cache tag block 3|
|3|CM7_0_TOP|11|CM7_0 data cache tag block 4|
|3|CM7_0_TOP|12|CM7_0 instruction TCM (Tightly Coupled Memory)|
|3|CM7_0_TOP|13|CM7_0 data TCM block 1|
|3|CM7_0_TOP|13|CM7_0 data TCM block 2|
|4|CM7_1_TOP|0|CM7_1 instruction cache data block 1|
|4|CM7_1_TOP|1|CM7_1 instruction cache data block 2|
|4|CM7_1_TOP|2|CM7_1 instruction cache tag block 1|
|4|CM7_1_TOP|3|CM7_1 instruction cache tag block 2|
|4|CM7_1_TOP|4|CM7_1 data cache data block 1|
|4|CM7_1_TOP|4|CM7_1 data cache data block 2|
|4|CM7_1_TOP|5|CM7_1 data cache data block 3|
|4|CM7_1_TOP|5|CM7_1 data cache data block 4|
|4|CM7_1_TOP|6|CM7_1 data cache data block 5|
|4|CM7_1_TOP|6|CM7_1 data cache data block 6|
|4|CM7_1_TOP|7|CM7_1 data cache data block 7|
|4|CM7_1_TOP|7|CM7_1 data cache data block 8|
|4|CM7_1_TOP|8|CM7_0 data cache tag block 1|
|4|CM7_1_TOP|9|CM7_0 data cache tag block 2|
|4|CM7_1_TOP|10|CM7_0 data cache tag block 3|
|4|CM7_1_TOP|11|CM7_0 data cache tag block 4|
|4|CM7_1_TOP|12|CM7_0 instruction TCM|
|4|CM7_1_TOP|13|CM7_0 data TCM block 1|
|4|CM7_1_TOP|13|CM7_0 data TCM block 2|
|5|FLEX_CAN_RAMS|0|FLEXCAN0 MB memory|
|5|FLEX_CAN_RAMS|1|FLEXCAN1 MB memory|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1786 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

Table 250. S32K314/S32K324/S32K344 MBIST mapping (continued) 

|BIST<br>index (NMCUT)|BIST name|Memory<br>index|Memory instance name|
|---|---|---|---|
|5|FLEX_CAN_RAMS|2|FLEXCAN2 MB memory|
|5|FLEX_CAN_RAMS|3|FLEXCAN3 MB memory|
|5|FLEX_CAN_RAMS|4|FLEXCAN4 MB memory|
|5|FLEX_CAN_RAMS|5|FLEXCAN5 MB memory|
|6|QSPI_PERI_RAMS|0|QSPI RAM|
|6|QSPI_PERI_RAMS|1|QSPI TX memory|
|7|EMAC_TSN_RAM|0|EMAC Timestamp Memory|
|8|EMAC_RAMS|0|EMAC RXParser|
|8|EMAC_RAMS|1|EMAC TX block 1|
|8|EMAC_RAMS|2|EMAC TX block 1|
|8|EMAC_RAMS|3|EMAC TX block 2|
|8|EMAC_RAMS|4|EMAC RX block 2|
|9|b03_ETF_RAMS|0|HTM ETF|
|9|b03_ETF_RAMS|1|Shared ETF|
|9|b03_ETF_RAMS|2|CM7 cluster Instruction ETF|
|9|b03_ETF_RAMS|3|CM7 cluster Data ETF|
|10|HSE_RAMS|0|HSE secure RAM|
|10|HSE_RAMS|1|HSE PKC memory block 1|
|10|HSE_RAMS|2|HSE PKC memory block 2|
|10|HSE_RAMS|3|HSE MTB memory|
|11|HSE_ROMS|0|BOOTROM block 1|
|11|HSE_ROMS|0|BOOTROM block 2|
|11|HSE_ROMS|0|BOOTROM block 3|
|11|HSE_ROMS|0|BOOTROM block 4|
|11|HSE_ROMS|0|BOOTROM block 5|



Table 251. K342 MBIST mapping 

|BIST<br>index (NMCUT)|BIST name|Memory<br>index|Memory instance name|
|---|---|---|---|
|0|HSE_ROMS|0|BOOTROM block 1|
|0|HSE_ROMS|0|BOOTROM block 2|
|0|HSE_ROMS|0|BOOTROM block 3|
|0|HSE_ROMS|0|BOOTROM block 4|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1787 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

Table 251. K342 MBIST mapping (continued) 

|BIST<br>index (NMCUT)|BIST name|Memory<br>index|Memory instance name|
|---|---|---|---|
|0|HSE_ROMS|0|BOOTROM block 5|
|1|HSE_RAMS|0|HSE secure RAM|
|1|HSE_RAMS|1|HSE PKC memory block 1|
|1|HSE_RAMS|2|HSE PKC memory block 2|
|1|HSE_RAMS|3|HSE MTB memory|
|2|SYS0_DMA_RAMS|0|PRAM0 block 1|
|2|SYS0_DMA_RAMS|1|PRAM0 block 2|
|2|SYS0_DMA_RAMS|2|DMA TCD RAM|
|3|CM7_0_TOP|0|CM7_0 instruction cache data block 1|
|3|CM7_0_TOP|1|CM7_0 instruction cache data block 2|
|3|CM7_0_TOP|2|CM7_0 instruction cache tag block 1|
|3|CM7_0_TOP|3|CM7_0 instruction cache tag block 2|
|3|CM7_0_TOP|4|CM7_0 data cache data block 1|
|3|CM7_0_TOP|4|CM7_0 data cache data block 2|
|3|CM7_0_TOP|5|CM7_0 data cache data block 3|
|3|CM7_0_TOP|5|CM7_0 data cache data block 4|
|3|CM7_0_TOP|6|CM7_0 data cache data block 5|
|3|CM7_0_TOP|6|CM7_0 data cache data block 6|
|3|CM7_0_TOP|7|CM7_0 data cache data block 7|
|3|CM7_0_TOP|7|CM7_0 data cache data block 8|
|3|CM7_0_TOP|8|CM7_0 data cache tag block 1|
|3|CM7_0_TOP|9|CM7_0 data cache tag block 2|
|3|CM7_0_TOP|10|CM7_0 data cache tag block 3|
|3|CM7_0_TOP|11|CM7_0 data cache tag block 4|
|3|CM7_0_TOP|12|CM7_0 instruction TCM (Tightly Coupled Memory)|
|3|CM7_0_TOP|13|CM7_0 data TCM block 1|
|3|CM7_0_TOP|13|CM7_0 data TCM block 2|
|4|FLEX_CAN_RAMS|0|FLEXCAN0 MB memory|
|4|FLEX_CAN_RAMS|1|FLEXCAN1 MB memory|
|4|FLEX_CAN_RAMS|2|FLEXCAN2 MB memory|
|4|FLEX_CAN_RAMS|3|FLEXCAN3 MB memory|
|5|CM7_1_TOP|0|CM7_1 instruction cache data block 1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1788 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

Table 251. K342 MBIST mapping (continued) 

|BIST<br>index (NMCUT)|BIST name|Memory<br>index|Memory instance name|
|---|---|---|---|
|5|CM7_1_TOP|1|CM7_1 instruction cache data block 2|
|5|CM7_1_TOP|2|CM7_1 instruction cache tag block 1|
|5|CM7_1_TOP|3|CM7_1 instruction cache tag block 2|
|5|CM7_1_TOP|4|CM7_1 data cache data block 1|
|5|CM7_1_TOP|4|CM7_1 data cache data block 2|
|5|CM7_1_TOP|5|CM7_1 data cache data block 3|
|5|CM7_1_TOP|5|CM7_1 data cache data block 4|
|5|CM7_1_TOP|6|CM7_1 data cache data block 5|
|5|CM7_1_TOP|6|CM7_1 data cache data block 6|
|5|CM7_1_TOP|7|CM7_1 data cache data block 7|
|5|CM7_1_TOP|7|CM7_1 data cache data block 8|
|5|CM7_1_TOP|8|CM7_0 data cache tag block 1|
|5|CM7_1_TOP|9|CM7_0 data cache tag block 2|
|5|CM7_1_TOP|10|CM7_0 data cache tag block 3|
|5|CM7_1_TOP|11|CM7_0 data cache tag block 4|
|5|CM7_1_TOP|12|CM7_0 instruction TCM|
|5|CM7_1_TOP|13|CM7_0 data TCM block 1|
|5|CM7_1_TOP|13|CM7_0 data TCM block 2|
|6|QSPI_PERI_RAMS|0|QSPI RAM|
|6|QSPI_PERI_RAMS|1|QSPI TX memory|
|7|EMAC_TSN_RAM|0|EMAC Timestamp Memory|
|8|EMAC_RAMS|0|EMAC RXParser|
|8|EMAC_RAMS|1|EMAC TX block 1|
|8|EMAC_RAMS|2|EMAC TX block 1|
|8|EMAC_RAMS|3|EMAC TX block 2|
|8|EMAC_RAMS|4|EMAC RX block 2|



Table 252. K312 MBIST mapping 

|BIST|BIST name|Memory|Memory instance name|
|---|---|---|---|
|index (NMCUT)||index||
|0|HSE_ROMS|0|BOOTROM block 1|
|0|HSE_ROMS|0|BOOTROM block 2|
|0|HSE_ROMS|0|BOOTROM block 3|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1789 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

Table 252. K312 MBIST mapping (continued) 

|BIST<br>index (NMCUT)|BIST name|Memory<br>index|Memory instance name|
|---|---|---|---|
|0|HSE_ROMS|0|BOOTROM block 4|
|0|HSE_ROMS|0|BOOTROM block 5|
|1|HSE_RAMS|0|HSE secure RAM|
|1|HSE_RAMS|1|HSE PKC memory block 1|
|1|HSE_RAMS|2|HSE PKC memory block 2|
|1|HSE_RAMS|3|HSE MTB memory|
|2|SYS0_DMA_RAMS|0|PRAM0 block 1|
|2|SYS0_DMA_RAMS|1|PRAM0 block 2|
|2|SYS0_DMA_RAMS|2|DMA TCD RAM|
|3|CM7_0_TOP|0|CM7_0 instruction cache data block 1|
|3|CM7_0_TOP|1|CM7_0 instruction cache data block 2|
|3|CM7_0_TOP|2|CM7_0 instruction cache tag block 1|
|3|CM7_0_TOP|3|CM7_0 instruction cache tag block 2|
|3|CM7_0_TOP|4|CM7_0 data cache data block 1|
|3|CM7_0_TOP|4|CM7_0 data cache data block 2|
|3|CM7_0_TOP|5|CM7_0 data cache data block 3|
|3|CM7_0_TOP|5|CM7_0 data cache data block 4|
|3|CM7_0_TOP|6|CM7_0 data cache data block 5|
|3|CM7_0_TOP|6|CM7_0 data cache data block 6|
|3|CM7_0_TOP|7|CM7_0 data cache data block 7|
|3|CM7_0_TOP|7|CM7_0 data cache data block 8|
|3|CM7_0_TOP|8|CM7_0 data cache tag block 1|
|3|CM7_0_TOP|9|CM7_0 data cache tag block 2|
|3|CM7_0_TOP|10|CM7_0 data cache tag block 3|
|3|CM7_0_TOP|11|CM7_0 data cache tag block 4|
|3|CM7_0_TOP|12|CM7_0 instruction TCM (Tightly Coupled Memory)|
|3|CM7_0_TOP|13|CM7_0 data TCM block 1|
|3|CM7_0_TOP|13|CM7_0 data TCM block 2|
|4|FLEX_CAN_RAMS|0|FLEXCAN0 MB memory|
|4|FLEX_CAN_RAMS|1|FLEXCAN1 MB memory|
|4|FLEX_CAN_RAMS|2|FLEXCAN2 MB memory|
|4|FLEX_CAN_RAMS|3|FLEXCAN3 MB memory|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1790 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

Table 252. K312 MBIST mapping (continued) 

|BIST|BIST name|Memory|Memory instance name|
|---|---|---|---|
|index (NMCUT)||index||
|4|FLEX_CAN_RAMS|4|FLEXCAN4 MB memory|
|4|FLEX_CAN_RAMS|5|FLEXCAN5 MB memory|



Table 253. K358 MBIST mapping 

|BIST<br>index (NMCUT)|BIST name|Memory index|Memory instance name|
|---|---|---|---|
|0|HSE_ROMS|0|BOOTROM block 1 bootrom_160KB_cut1|
|0|HSE_ROMS|0|BOOTROM block 2 bootrom_160KB_cut1|
|0|HSE_ROMS|0|BOOTROM block 3 bootrom_160KB_cut1|
|0|HSE_ROMS|0|BOOTROM block 4 bootrom_160KB_cut1|
|0|HSE_ROMS|0|BOOTROM block 5 bootrom_160KB_cut1|
|1|HSE_RAMS|0|HSE secure RAM hse_secure_ram_64KB|
|1|HSE_RAMS|1|HSE PKC memory block 1 hse_pkc_8KB_cut1|
|1|HSE_RAMS|2|HSE PKC memory block 2 hse_pkc_8KB_cut2|
|1|HSE_RAMS|3|HSE MTB memory hse_MTB_1KB|
|2|SYS0_DMA_R<br>AMS|0|PRAM0 block 1 sys_ram0_64KB_cut1_pd0|
|2|SYS0_DMA_R<br>AMS|1|PRAM0 block 2 sys_ram0_64KB_cut2_pd1|
|2|SYS0_DMA_R<br>AMS|2|PRAM0 block 3 sys_ram0_128KB_cut3_pd1|
|2|SYS0_DMA_R<br>AMS|3|PRAM0 block 4 dma_tcd_ram|
|3|SYS1_RAMS|0|PRAM1 block 1 sys_ram1_128KB_cut1_pd1|
|3|SYS1_RAMS|1|PRAM1 block 2 sys_ram1_128KB_cut2_pd1|
|4|SYS2_RAMS|0|PRAM2 block 1 sys_ram2_64KB_cut1_pd1|
|4|SYS2_RAMS|1|PRAM2 block 2 sys_ram2_64KB_cut2_pd1|
|4|SYS2_RAMS|2|PRAM2 block 3 sys_ram2_128KB_cut3_pd1|
|5|CM7_0_TOP|0|CM7_0 instruction cache data block<br>1 cm7_0_cache_instruction_data_16KB_cut1|
|5|CM7_0_TOP|1|CM7_0 instruction cache data block<br>2 cm7_0_cache_instruction_data_16KB_cut2|
|5|CM7_0_TOP|2|CM7_0 instruction cache tag block<br>1 cm7_0_cache_instruction_tag_cut1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1791 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

Table 253. K358 MBIST mapping (continued) 

|BIST<br>index (NMCUT)|BIST name|Memory index|Memory instance name|
|---|---|---|---|
|5|CM7_0_TOP|3|CM7_0 instruction cache tag block<br>2 cm7_0_cache_instruction_tag_cut2|
|5|CM7_0_TOP|4|CM7_0 data cache data block<br>1 cm7_0_cache_data_data_16KB_cut1|
|5|CM7_0_TOP|4|CM7_0 data cache data block<br>5 cm7_0_cache_data_data_16KB_cut5|
|5|CM7_0_TOP|5|CM7_0 data cache data block<br>2 cm7_0_cache_data_data_16KB_cut2|
|5|CM7_0_TOP|5|CM7_0 data cache data block<br>6 cm7_0_cache_data_data_16KB_cut6|
|5|CM7_0_TOP|6|CM7_0 data cache data block<br>3 cm7_0_cache_data_data_16KB_cut3|
|5|CM7_0_TOP|6|CM7_0 data cache data block<br>7 cm7_0_cache_data_data_16KB_cut7|
|5|CM7_0_TOP|7|CM7_0 data cache data block<br>4 cm7_0_cache_data_data_16KB_cut4|
|5|CM7_0_TOP|7|CM7_0 data cache data block<br>8 cm7_0_cache_data_data_16KB_cut8|
|5|CM7_0_TOP|8|CM7_0 data cache tag block 1 cm7_0_cache_data_tag_cut1|
|5|CM7_0_TOP|9|CM7_0 data cache tag block 2 cm7_0_cache_data_tag_cut2|
|5|CM7_0_TOP|10|CM7_0 data cache tag block 3 cm7_0_cache_data_tag_cut3|
|5|CM7_0_TOP|11|CM7_0 data cache tag block 4 cm7_0_cache_data_tag_cut4|
|5|CM7_0_TOP|12|CM7_0 instruction TCM cm7_0_itcm_32KB|
|5|CM7_0_TOP|13|CM7_0 data TCM block 1 cm7_0_d0tcm_32KB|
|5|CM7_0_TOP|13|CM7_0 data TCM block 2 cm7_0_d1tcm_32KB|
|6|CM7_1_TOP|0|CM7_1 instruction cache data block<br>1 cm7_1_cache_instruction_data_16KB_cut1|
|6|CM7_1_TOP|1|CM7_1 instruction cache data block<br>2 cm7_1_cache_instruction_data_16KB_cut2|
|6|CM7_1_TOP|2|CM7_1 instruction cache tag block<br>1 cm7_1_cache_instruction_tag_cut1|
|6|CM7_1_TOP|3|CM7_1 instruction cache tag block<br>2 cm7_1_cache_instruction_tag_cut2|
|6|CM7_1_TOP|4|CM7_1 data cache data block<br>1 cm7_1_cache_data_data_16KB_cut1|
|6|CM7_1_TOP|4|CM7_1 data cache data block<br>5 cm7_1_cache_data_data_16KB_cut5|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1792 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

Table 253. K358 MBIST mapping (continued) 

|BIST<br>index (NMCUT)|BIST name|Memory index|Memory instance name|
|---|---|---|---|
|6|CM7_1_TOP|5|CM7_1 data cache data block<br>2 cm7_1_cache_data_data_16KB_cut2|
|6|CM7_1_TOP|5|CM7_1 data cache data block<br>6 cm7_1_cache_data_data_16KB_cut6|
|6|CM7_1_TOP|6|CM7_1 data cache data block<br>3 cm7_1_cache_data_data_16KB_cut3|
|6|CM7_1_TOP|6|CM7_1 data cache data block<br>7 cm7_1_cache_data_data_16KB_cut7|
|6|CM7_1_TOP|7|CM7_1 data cache data block<br>4 cm7_1_cache_data_data_16KB_cut4|
|6|CM7_1_TOP|7|CM7_1 data cache data block<br>8 cm7_1_cache_data_data_16KB_cut8|
|6|CM7_1_TOP|8|CM7_1 data cache tag block 1 cm7_1_cache_data_tag_cut1|
|6|CM7_1_TOP|9|CM7_1 data cache tag block 2 cm7_1_cache_data_tag_cut2|
|6|CM7_1_TOP|10|CM7_1 data cache tag block 3 cm7_1_cache_data_tag_cut3|
|6|CM7_1_TOP|11|CM7_1 data cache tag block 4 cm7_1_cache_data_tag_cut4|
|6|CM7_1_TOP|12|CM7_1 instruction TCM cm7_1_itcm_32KB|
|6|CM7_1_TOP|13|CM7_1 data block 1 cm7_1_d0tcm_32KB|
|6|CM7_1_TOP|13|CM7_1 data block 2 cm7_1_d1tcm_32KB|
|7|CM7_2_TOP|0|CM7_2 instruction cache data block<br>1 cm7_2_cache_instruction_data_16KB_cut1|
|7|CM7_2_TOP|1|CM7_2 instruction cache data block<br>2 cm7_2_cache_instruction_data_16KB_cut2|
|7|CM7_2_TOP|2|CM7_2 instruction cache tag block<br>1 cm7_2_cache_instruction_tag_cut1|
|7|CM7_2_TOP|3|CM7_2 instruction cache tag block<br>2 cm7_2_cache_instruction_tag_cut2|
|7|CM7_2_TOP|4|CM7_2 data cache data block<br>1 cm7_2_cache_data_data_16KB_cut1|
|7|CM7_2_TOP|4|CM7_2 data cache data block<br>5 cm7_2_cache_data_data_16KB_cut5|
|7|CM7_2_TOP|5|CM7_2 data cache data block<br>2 cm7_2_cache_data_data_16KB_cut2|
|7|CM7_2_TOP|5|CM7_2 data cache data block<br>6 cm7_2_cache_data_data_16KB_cut6|
|7|CM7_2_TOP|6|CM7_2 data cache data block<br>3 cm7_2_cache_data_data_16KB_cut3|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1793 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

Table 253. K358 MBIST mapping (continued) 

|BIST<br>index (NMCUT)|BIST name|Memory index|Memory instance name|
|---|---|---|---|
|7|CM7_2_TOP|6|CM7_2 data cache data block<br>7 cm7_2_cache_data_data_16KB_cut7|
|7|CM7_2_TOP|7|CM7_2 data cache data block<br>4 cm7_2_cache_data_data_16KB_cut4|
|7|CM7_2_TOP|7|CM7_2 data cache data block<br>8 cm7_2_cache_data_data_16KB_cut8|
|7|CM7_2_TOP|8|CM7_2 data cache tag block 1 cm7_2_cache_data_tag_cut1|
|7|CM7_2_TOP|9|CM7_2 data cache tag block 2 cm7_2_cache_data_tag_cut2|
|7|CM7_2_TOP|10|CM7_2 data cache tag block 3 cm7_2_cache_data_tag_cut3|
|7|CM7_2_TOP|11|CM7_2 data cache tag block 4 cm7_2_cache_data_tag_cut4|
|7|CM7_2_TOP|12|CM7_2 instruction TCM cm7_2_itcm_64KB|
|7|CM7_2_TOP|13|CM7_2 data TCM block 1 cm7_2_d0tcm_64KB|
|7|CM7_2_TOP|13|CM7_2 data TCM block 2 cm7_2_d1tcm_64KB|
|8|FLEX_CAN_RA<br>MS|0|FLEXCAN0 MB memoryd_ip_flexcan3_syn_0_mb_memory|
|8|FLEX_CAN_RA<br>MS|1|FLEXCAN1 MB memoryd_ip_flexcan3_syn_1_mb_memory|
|8|FLEX_CAN_RA<br>MS|2|FLEXCAN2 MB memoryd_ip_flexcan3_syn_2_mb_memory|
|8|FLEX_CAN_RA<br>MS|3|FLEXCAN3 MB memoryd_ip_flexcan3_syn_3_mb_memory|
|8|FLEX_CAN_RA<br>MS|4|FLEXCAN4 MB memoryd_ip_flexcan3_syn_4_mb_memory|
|8|FLEX_CAN_RA<br>MS|5|FLEXCAN5 MB memoryd_ip_flexcan3_syn_5_mb_memory|
|8|FLEX_CAN_RA<br>MS|6|FLEXCAN6 MB memoryd_ip_flexcan3_syn_6_mb_memory|
|8|FLEX_CAN_RA<br>MS|7|FLEXCAN7 MB memoryd_ip_flexcan3_syn_7_mb_memory|
|9|QSPI_PERI_RA<br>MS|0|QSPI RAM qspi_ram|
|9|QSPI_PERI_RA<br>MS|1|QSPI TX memory qspi_tx|
|10|ENET_TSN_RA<br>M|0|ENET Timestamp Memory enet_tsn|
|11|ENET_RAMS|0|ENET RXParser enet_rxparser|
|11|ENET_RAMS|1|ENET TX block 1 enet_tx_0|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1794 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

Table 253. K358 MBIST mapping (continued) 

|BIST<br>index (NMCUT)|BIST name|Memory index|Memory instance name|
|---|---|---|---|
|11|ENET_RAMS|2|ENET RX block 1 enet_rx_0|
|11|ENET_RAMS|3|ENET TX block 2 enet_tx_1|
|11|ENET_RAMS|4|ENET RX block 2 enet_rx_1|
|12|ETF_RAMS|0|HTM ETF HTM_ETF|
|12|ETF_RAMS|1|Shared ETF Shared_system_ETF|
|12|ETF_RAMS|2|CM7 cluster Instruction ETF CM7_cluster_ETF_ETMI|
|12|ETF_RAMS|3|CM7 cluster Data ETF CM7_cluster_ETF_ETMD|



### 52.1.4 Clock connectivity 

STCU2 works on the system clock domain. The scan operations while LBIST are done on TCK clock. 

Table 254. Clock connectivity 

|STCU2 clock|Clock connected to the chip|Remarks|
|---|---|---|
|CORE_CLK|AIPS_SLOW_CLK|System clock divider output clock node<br>|
|REG_INTF_CLK||for STCU2 operations and register<br>interface accesses|
|SHIFT_CLK|JTAG_TCK|JTAG_TCK used for shift operations<br>when self-test is in progress|



### 52.1.5 Memory map for self-test GPRs 

See the memory map file attached to this document and 'SELFTEST_GPR' chapter for details. 

### 52.1.6 Handling unrecoverable faults 

Only recoverable and non-critical faults from STCU2 are mapped to FCCU. The unrecoverable and critical faults are mapped to MC_RGM. Therefore, ignore any references to mapping of unrecoverable and critical faults with FCCU in this chapter. 

### 52.1.7 Indicating fault state during the main reset domain Self-Test 

FCCU EOUT indicates the fault state during the Self-Test as soon as the UTEST_MISC[FCCU_EOUT_ DEDICATED] is enabled and DCMRWD2[EOUT_STAT_DUR_STEST] is enabled at the time of Self-Test setup steps. 

The fault state remains asserted until the bit DCMRWD2[EOUT_STAT_DUR_STEST] is cleared post Self-Test reset sequence. 

In case it is not required to indicate the fault state during the Self-Test, then the bit DCMRWD2[EOUT_STAT_DUR_STEST] should not be programmed. 

### 52.1.8 Error events management in main reset domain Self-Test 

Error events should be mapped to unrecoverable faults in STCU2_ERR_FM register for main reset domain Self-Test. 

### 52.1.9 AUTOLOCK_VALUE for register write access via STCU2_SKC 

Register write-access watchdog timer explains that access to STCU2 registers via the STCU2_SKC security-key mechanism times out after a number of STCU2 clock cycles equal to AUTOLOCK_VALUE. On this chip, AUTOLOCK_VALUE is 32'hFFFF_FFFF. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1795 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

### 52.1.10 PLL loss of lock during Self-Test 

Detection of PLL loss of lock during LBIST or MBIST causes a destructive reset in the system. 

CMU0 programming is required before the Self-Test programming begins. 

All the registers present in LBIST domains do not retain their content after Self-Test reset. 

### 52.1.11 STCU2 BIST start (BSTART) register description 

Attempted accesses with the undefined reserved values in the BSTART register can result in undefined behavior. The following table defines the BSTART field on this chip. 

Table 255. BSTART description 

|Field value|Description|
|---|---|
|000b|NOP (reset value)|
|001b|RUN_ONLY: Run BISTs.<br>MTR controller (MCT) runs the selected BISTs without<br>programming them first.|
|010b|Reserved|
|011b|Reserved|
|100b|PROG_ONLY: Program BISTs only.<br>MCT only programs BISTs and does not start them. This<br>enables different BISTs to be programmed with different<br>algorithms before all the selected BISTs are started using the<br>RUN_ONLY command.|
|101b|PROG_RUN: Program BISTs and start them.|
|110b|Reserved|
|111b|Reserved|



### 52.1.12 STCU2 algorithm select (ALGOSEL) register description 

This register selects any one of the predefined algorithms. The value used in this register is mapped to a predefined algorithm register in BIST. After MCT has programmed information on this register and starts some BIST operation, this value is transferred to the predefined algorithm register in every BIST that is selected. 

If multiple predefined algorithms are selected, the order of execution is from LSB to MSB. 

Any field that does not have a predefined algorithm associated with it is a reserved bit. No data is written to reserved bits and when you read these bits, they always return 0. These predefined algorithms include: 

- Backgrounds 

- Address modes and other register programming that may be necessary 

- The number of BIST runs needed to perform the exact coverage requested. 

MCT decodes this information through a series of look-up tables. The following table describes the high-level BIST algorithms that can be invoked through the MCT. The columns in that table have the following meaning: 

- Index: The position in this MCT register enables this algorithm. 

- Name: The symbolic name for this algorithm. 

- Description: The intent and use model for this algorithm. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1796 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

- BIST runs: The sequence of BIST invocations comprising this algorithm. 

- Sequences: The ordered list of march elements to run. Each march element consists of a direction indicator (for increasing addresses and for decreasing addresses) and a set of march phases. A march phase consists of reading (R) or writing (W), the non-inverted (0) or inverted (1) background pattern. 

- Used by default: Whether this algorithm is selected in the post-reset state of this register. 

Table 256. ALGOSEL description 

|Index|Name|Description|BIST runs|Sequences|Used by default|
|---|---|---|---|---|---|
|3|March C+ single|March C+ with<br>column fast and<br>solid background|MarchC+ column<br>fast 1x (#4)|W0, R0W1,<br>R1W0R0W1,<br>R1W0,<br>R0W1R1W0, R0|Yes|
|13|BasicChk|Basic selfcontained<br>checkerboard,<br>using column fast|BasicChk (#18)|R0W1R1|-|



### 52.1.13 Self-Test programming sequence 

This section describes a high level programming sequence for executing Self-Test. The detailed programming sequences for supported configurations are available in a separate application note (contact your NXP sales representative). 

- Program clock sources and MC_CGMs as per the clock configuration. 

~~<mark>NOTE</mark>~~ 

While running MBIST on EMAC timestamp memory, MC_CGM.MUX_9_DC_0[DIV] should be appropriately configured to ensure EMAC_CLK_TS should be atleast 1.5 times the AIPS_SLOW_CLK frequency. 

- Program SELFTEST_GPR[CONFIG_REG] and SELFTEST_GPR[LBIST_PROG_REG] as per the LBIST configurations. 

~~<mark>NOTE</mark>~~ 

This is not applicable for S32K312 and S32K311 wherein LBIST is not supported. 

- Program STCU2 as per NXP recommended. 

- Program dcf_client_utest_misc[FCCU_EOUT_DEDICATED] and DCMRWD2[EOUT_STAT_DUR_STEST] to configure EOUT pins as dedicated and to indicate FCCU error states on EOUT pins during Self-Test respectively. 

- Configure ERCTRL[ERASSERT] register bit in MC_RGM to achieve desired behaviour of Reset Pin as documented in Reset Section and Pad States Section. 

- Disable functional reset sources to avoid false Self-Test abort scenarios. For example, software watchdog timers cannot be serviced while Self-Test because the software is not accessible and can cause invalid timeout reset. See Reset events and configurations while Self-Test. 

- Program the PCS_ENABLE[8:7] fields of the CONFIG_REG register (SELFTEST_GPR) to 0 to disable PCS. 

- Trigger Self-Test execution by programming RUNSW register in STCU2. 

- At the end of the Self-Test run, a functional reset is generated. Out of reset, the software can check the status registers inside STCU2 and take actions accordingly. 

### 52.1.14 Modules operation during/post Self-Test 

The clock, reset, power generation modules, such as RGM, PMC, CGM, FIRC, PLL, and SIRC will be available during and post Self-Test. However, because the chip undergoes the reset sequence, PLL and CGM will be reset. 

CMU0 and CMU3 will be available during Self-Test if enabled prior to Self-Test, but will be Reset post Self-Test. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1797 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

STCU2 will also be available during Self-Test and the results can be read post Self-Test. 

### 52.1.15 Reset events and configurations while Self-Test 

As Self-Test is a software initiated Self-Test, it is expected by software to ensure all the peripherals are disabled as documented in Software considerations before Self-Test. 

The functional reset sources should be appropriately configured to avoid any functional reset while Self-Test is running (disable SWT_RST and HSE_SWT_RST. JTAGC should not be in EXTEST, HIGHZ or CLAMP instructions). This ensures no selftest abort while running selftest due to functional reset source. The below table specifies the state of functional reset sources for Self-Test. 

Table 257. Reset events and configurations while self-test 

|Reset source|Reset description|Configurations/remarks for selftest|
|---|---|---|
|FCCU_RST|FCCU reset reaction|The FCCU is a part of logic which is under Self-Test and thus it would be<br>disabled during the Self-Test|
|ST_DONE|Self-Test done reset|The selftest done indication resets the device post selftest. While Self-Test is<br>running, the Self-Test done indication will be in disabled state|
|SWT_RST|SWT reset request|SWT should be disabled in Self-Test configuration sequence.|
|JTAG_RST|JTAG Reset|JTAG communication should be inactive while Self-Test and JTAGC state<br>machine should not be in EXTEST, HIGHZ or CLAMP instructions|
|HSE_SWT_R<br>ST|HSE SWT timeout|HSE_SWT should be disabled in Self-Test configuration sequence.|
|SW_FUNC|software 'functional' reset|The software is inactive during Self-Test and hence software functional reset<br>will not arrive while the chip is under Self-Test.|
|DEBUG_FUN<br>C|debug 'functional' reset|MDM DAP should not be configured for debug functional reset generation while<br>Self-Test is running.|



The destructive reset sources are available while in Self-Test. In case of any destructive reset event, the device undergoes a destructive reset sequence, thereby resetting the STCU2 and Self-Test logic itself. 

After completion of Self-Test (LBIST or MBIST), a functional reset sequence is executed by MC_RGM. 

### 52.1.16 Software considerations before Self-Test 

1. As all the communication peripherals are not in LBIST partitions; hence, it is required by SW to stop all communications and disable all the PCTLs of the communication peripherals before initiating Self-Test as the device will be unusable in Self-Test. This is needed so that there is graceful safe stating of inputs of non-lbisted peripheral modules. 

2. Configure RGM functional reset sources as interrupts before Self-Test as per the considerations mentioned in Reset events and configurations while Self-Test, i.e., the SWTs should be disabled, the JTAGC should not be in states which can cause a JTAG reset event (EXTEST, HIGHZ, CLAMP instructions) and the software should not trigger a functional reset event via MC_ME or MDM_AP while the selftest is ongoing. This is to avoid any abort scenario due to any functional reset source as Self-Test is initiated by SW. 

There is no issue with Reset pin as Reset pin is a source of destructive reset and will reset STCU2 and Self-Test related logic etc. 

### 52.1.17 End of Self-Test 

The Self-Test completion is a source of functional reset to the device, by which the device executes a functional reset sequence. The logic which is LBISTed additionally undergoes a complete POR sequence to ensure that the random content shifted during BIST sequence get cleared. 

At the end of MBIST , the software should execute below steps: 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1798 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

1. Software reads the MBIST end flag to identify that the MBIST sequence had ended properly without any interruption or abort, by reading STCU2.MBESWn. 

2. Software reads the MBIST status to identify whether the MBIST was successful or not, by reading STCU2.MBSSWn. 

   - ~~<mark>NOTE</mark>~~ 

The MBIST status should always be read in accordance with MBIST end flag. The STCU2.MBSSWn status is irrelevant if STCU2.MBESWn indicates that MBIST execution is incomplete. 

At the end of LBIST , the software should execute below steps: 

1. Software reads the LBIST end flag to identify that the LBIST sequence had ended properly without any interruption or abort, by reading STCU2.LBESWn. 

2. Software reads the LBIST status to identify whether the LBIST was successful or not, by reading STCU2.LBSSWn. 

   - ~~<mark>NOTE</mark>~~ 

The LBIST status should always be read in accordance with LBIST end flag. The STCU2.LBSSWn status is irrelevant if STCU2.LBESWn indicates that LBIST execution is incomplete. 

## 52.2 Introduction 

STCU2 is a comprehensive programmable hardware module that: 

- Manages the execution of BISTs 

- Indicates whether each BIST passed 

- Manages the chip's LBIST and the MBIST blocks 

## 52.3 Main features 

STCU2 includes: 

- System interface for reading from and writing to the STCU2 registers during runtime (online) via the CPU 

- Programmable scheduler for BIST execution 

- Control over LBIST concurrent or sequential execution 

- Control over MBIST concurrent or sequential execution 

- Programmable LBIST delayed concurrent start 

- Programmable internal clock prescaler to reduce internal and BIST clocks 

- PLL lock signal monitoring during BIST sequences 

- Programmable BIST-sequence-execution watchdog timer that specifies the maximum time allowed for the execution of a BIST sequence 

- Fixed register-write-access watchdog timer that specifies the maximum amount of time that STCU2 allows you to write to its registers after you unlock them 

- Fields that indicate the execution status of each BIST, see Types of BIST sequences and Types of BIST partitions 

- Fields that indicate the status of each type of online STCU2 internal error condition 

- Programmable fault mapping of each BIST for controlling the type of fault that STCU2 reports (recoverable or unrecoverable) when the BIST fails to execute 

- Programmable fault mapping of each STCU2 internal error condition for controlling the type of fault that STCU2 reports (recoverable or unrecoverable) when the condition occurs 

- Signals to report recoverable and unrecoverable faults to the FCCU module 

- Redundant recoverable and unrecoverable fault-generation logic to improve reliability 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1799 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

- FCCU recoverable and unrecoverable fault-injection mechanism 

- Global register write-protection mechanism that requires two security key codes 

- Global automatic power saving after a BIST sequence is completed when watchdog timer time-out is detected 

- Watchdog automatic clock wake-up mechanism when software unlocks the STCU2 registers for write access 

- Watchdog automatic power saving when the fixed register-write-access watchdog timer times out 

## 52.4 Block diagram 

This diagram shows the parts of STCU2: 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/052_Self-Test_Control_Unit_-STCU2-/S32K3XXRM_数据表.pdf-1800-09.png)


<!-- Start of picture text -->
LBIST<br>LBIST<br>interface<br>WDG FSM<br>Loader<br>Reg Master Shifter<br>interface FSM Interrupt<br>FSM<br>IPS<br>Fault interfaces  PLL Lock<br>MBIST MBIST<br>interface<br>Clock<br>interface FCCU<br><!-- End of picture text -->

Figure 192. STCU2 block diagram 

This table describes the parts of STCU2: 

Table 258. STCU2 parts 

|Part|Function|
|---|---|
|Reg interface|Provides access to:|
||• Registers|
||• The security key logic<br>• TheIPSinterface|
|Fault interface|Performs the following tasks:|
||• Collects the fault conditions caused by STCU2 internal error conditions and each<br>BIST executed in a sequence|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1800 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

Table 258. STCU2 parts (continued) 

|Part|Function|
|---|---|
||• Sets the global recoverable or unrecoverable status flag, depending on the fault<br>mapping for a given BIST<br>• Manages the recoverable and unrecoverable fault lines to and from the<br>FCCU module<br>• Manages the set/clear injection mechanism provided by the FCCU module<br>To improve the intrinsic reliability of this critical logic, the generation logic<br>is duplicated.|
|Clock interface|Manages the internal and the BIST clock prescaler, the internal clock-gating power<br>saving, and the wake-up clock feature|
|WDG FSM|Provides the following:<br>• A programmable BIST-sequence-execution watchdog timer that specifies the<br>maximum time allowed for the execution of a BIST sequence<br>• A fixed register-write-access watchdog timer that specifies the maximum<br>amount of time that STCU2 allows you to write to its registers after you<br>unlock them|
|MasterFSM|Coordinates and schedules all of the operations performed during a BIST sequence|
|Loader Shifter FSM|Programs the BIST registers and reads back the data to be checked at the end of<br>each test operation|
|LBIST interface|Provides the interface between the chip's LBIST engines and the STCU2 controllers|
|MBIST interface|Provides the interface between the MBIST controller and the STCU2 controllers|



## 52.5 Peripheral bus interface 

The peripheral bus interface is a slave bus used for configuration purposes via CPU. The module supports the following bus read operations: 

- Word (32 bits) data read operations to any registers 

- Any other operation is not supported. 

Word, low and high half-words, byte operations are supported in write mode only: 

- Write access is allowed by software only when CFG[WRP] is cleared. The default value of CFG[WRP] is cleared. 

- Exceptions are the following read/write fields: CFG[WRP], ERR_STAT[UFSF] and ERR_STAT[RFSF]. 

- In all the other conditions, the write operations are not supported and all the STCU2 registers can be only read. 

- STCU2 Configuration (CFG) should only be accessed in 32 bit (partial access not allowed). 

The STCU2 module generates a transfer error in the following cases: 

- Any read access to the registers after writing Key1 and before writing Key2 (in online ) and before register write-access watchdog timer expires. 

- Any write/read access to the register addresses not mapped on the peripheral but included in the address space of the peripheral 

- Any write/read operation different from byte/halfword/word (free byte enables or other operations) on each register 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1801 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

- Any write operation on Double Security Key register applying a wrong sequence of keys (the two write operations cannot be interleaved with other access to STCU2 registers) 

- Any write operation performed on a register when the Double Security keys have not been applied 

- Any write operation performed on registers when CFG[WRP] is set and the access is performed through software (internal peripheral interface). The exceptions are SKC register (for valid keys value and sequence) and INT_FLG register(interrupt flag) in which STCU2 does not assert transfer error. 

- Any write operation performed on Read Only registers 

The registers of the STCU2 module are accessible (read/write) in each access mode: user, supervisor, or test. 

In case there are write operations on bits marked as reserved, the transfer error is not generated. 

~~<mark>NOTE</mark>~~ 

See the chip-specific STCU2 information for the wait time necessary to write to the online registers. 

## 52.6 BISTs and BIST partitions 

### 52.6.1 Definition: BIST 

A BIST is a test that the chip can execute to verify the functional integrity of a part of itself. The chip uses STCU2 and other on-chip hardware to execute a BIST. 

### 52.6.2 Definition: BIST partition 

A BIST partition is a part of a chip for which a BIST has been defined. The hardware that is included in a given BIST partition is chip-specific. For a list of the hardware included in each of the BIST partitions on this chip, see the chip-specific STCU2 information. 

### 52.6.3 Example: BIST partitions on a chip 

This is an example of a chip with six BIST partitions: 

Chip BIST partition 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/052_Self-Test_Control_Unit_-STCU2-/S32K3XXRM_数据表.pdf-1802-18.png)


### 52.6.4 Types of BIST partitions 

The STCU2 module on this chip supports the following type or types of BIST partitions: 

Table 259. Types of BIST partitions 

|BIST partition type|Description|
|---|---|
|MBIST partition|An SRAM or ROM block|
|LBIST partition|One or more digital modules|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1802 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

## 52.7 BIST sequences 

### 52.7.1 Definition: BIST sequence 

A BIST sequence is a programmable series of one or more phases, each of which executes one or more individual BISTs. 

### 52.7.2 STCU2 executes MBISTs before LBISTs 

If a BIST sequence includes both MBISTs and LBISTs; STCU2 executes the MBISTs first. 

### 52.7.3 Example: Single-phase BIST sequence 

This is an example of a single-phase BIST sequence in which STCU2 executes only one BIST: 

Table 260. Example: Single-phase BIST sequence 

|Phase|BIST executed|
|---|---|
|0|MBIST 16|



### 52.7.4 Example: Multi-phase BIST sequence 

This is an example of a multiphase BIST sequence in which STCU2 executes more than one BIST in parallel in some phases: 

Table 261. Example: Multi-phase BIST sequence 

|Phase|BISTs executed|
|---|---|
|0|MBISTs 7, 30|
|1|MBIST 23|
|2|MBISTs 6, 16, 29, 23|
|3|LBIST 12|
|4|LBISTs 13, 8, 11|
|5|LBISTs 19, 6|



### 52.7.5 Types of BIST sequences 

The STCU2 module on this chip supports these types of BIST sequences: 

Table 262. Example: Types of BIST sequences 

|BIST sequence type|Description|
|---|---|
|Online BIST sequence|A BIST sequence that STCU2 executes during runtime at<br>the request of software. Application software configures and<br>initiates execution of the BIST sequence by loading values into<br>STCU2 registers.|



### 52.7.6 Supported BIST sequences 

NXP supports only a specific set of BIST sequences for this chip. For the list of supported BIST sequences, see the chip-specific STCU2 information. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1803 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

## 52.8 Functional description 

### 52.8.1 FSM description 

The module has three state machines that work together: Master State Machine, Loader/Shifter State Machine, and the Watchdog State Machine. Basically the Master State Machine is the core unit of the STCU2 module. It coordinates all the self-test operations and the other state machines. The Loader/Shifter State Machine is used to program the MBIST and the LBIST parameters and to retrieve the related results depending on the parameters stored into the STCU2 registers and under the control of the Master State Machine. The Watchdog State Machine evaluates all the schedule time for MBIST and LBIST and the time-out in case of wrong STCU2 programming. 

### 52.8.2 BIST scheduling 

STCU2 is designed to program the parallel/serial execution of the MBIST or LBIST depending on the power, timing, and coverage constraints. 

The mechanism used to provide this flexibility is a linked list of BIST descriptors where the starting pointer is defined in CFG[PTR]. The first LBIST is mapped on 0, the second on 1, and so on. A BIST descriptor identifies a LBIST or MBIST via an index that is associated with its control register (STCU2 LBIST Control (LB_CTRL0) or STCU2 MBIST Control (MB_CTRL0 - MB_CTRL12)). The first MBIST is mapped on (00000080h + 0), the second on (00000080h + 1), and so on. The additional pointers of the linked list are in LB_CTRLn[PTR] for LBIST n (where n is the selected LBIST) and MB_CTRLm[PTR] for MBIST m (where m is the selected MBIST) and must be populated depending on the selected run sequence. The additional fields LB_CTRL[CSM] and MB_CTRL[CSM] provide the flexibility to run concurrently or sequentially the chosen set of the LBIST or MBIST or to close the linked list by setting the NIL pointer. 

### 52.8.3 FCCU interface 

The FCCU interface is the hardware flag mechanism towards the system, to indicate the occurrence of an Unrecoverable fault and/or a Recoverable fault failure during the Self Test sequence. Two independent signals have been used to mitigate the common cause faults. 

To diagnose physical defects on the two fault signals, a fault injection mechanism is also provided. In this case, the FCCU interface allows the user application to check the integrity of the UF and RF connection lines between the STCU2 and the FCCU. Refer to the description of FCCU fault injection mechanism to understand how the UF/RF set/clear mechanism works. 

### 52.8.4 Watchdogs 

The STCU2 implements different watchdogs to ensure that operations are finished in time. 

#### 52.8.4.1 BIST watchdog timer 

The LBIST and MBIST execution time has to be configured as described in STCU2 Watchdog Granularity (WDG), to account for the overall execution time of the self test sequence. In case the selected LBISTs or MBISTs are not yet completed during assigned time, the current LBISTs or MBISTs execution is interrupted and a failure is flagged into ERR_STAT[WDTOSW] and MBESWx or LBESW. 

In case of multiple sequential run in the same online session and the time-out happens in the middle of a sequential run, the next sequential run will be skipped and the execution ends with the current updated status of the registers reported above. 

#### 52.8.4.2 Register write-access watchdog timer 

As explained in the STCU2 SK Code (SKC): 

- A key mechanism protects STCU2 registers during the self-test configuration phase by preventing any unwanted access. 

- A hardware watchdog timer locks register-write access after a number of STCU2 clock cycles. To refresh the hardware watchdog timer before it times out, write Key1 and Key2 sequences. 

AUTOLOCK_VALUE is the number of STCU2 clock cycles after which the hardware watchdog timer locks register-write access. See the chip-specific STCU2 information for the value of AUTOLOCK_VALUE. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1804 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

The hardware watchdog timer is particularly useful in case CFG[WRP] is 0 during the software self-test configuration. In this case, the software application might enable write access to the STCU2 registers. 

## 52.9 Use cases and limitations 

For details on use cases and limitations, contact NXP sales representative. 

## 52.10 STCU2 register descriptions 

The STCU2 registers are listed in this section. 

~~<mark>NOTE</mark>~~ 

Always write the reset value for the Reserved fields. 

During online self-test, after the STCU2 registers are configured, they must not be overridden via internal peripheral system until the self-test is complete. 

### 52.10.1 STCU2 memory map 

STCU base address: 403A_0000h 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|4h|STCU2 Run Software (RUNSW)|32|RW|0000_0000h|
|8h|STCU2 SK Code (SKC)|32|WO|0000_0000h|
|Ch|STCU2 Configuration (CFG)|32|RW|0000_0000h|
|14h|STCU2 Watchdog Granularity (WDG)|32|RW|0000_FFFFh|
|24h|STCU2 Error (ERR_STAT)|32|RW|0000_0000h|
|28h|STCU2 Error FM (ERR_FM)|32|RW|0000_0000h|
|4Ch|STCU2 Online LBIST Status (LBSSW0)|32|RO|0000_0000h|
|5Ch|STCU2 Online LBIST End Flag (LBESW0)|32|RO|0000_0000h|
|7Ch|STCU2 Online LBIST Unrecoverable FM (LBUFM0)|32|RW|0000_0000h|
|10Ch|STCU2 Online MBIST Status (MBSSW0)|32|RO|0000_0000h|
|14Ch|STCU2 Online MBIST End Flag (MBESW0)|32|RO|0000_0000h|
|18Ch|STCU2 MBIST Unrecoverable FM (MBUFM0)|32|RW|0000_0000h|
|200h|STCU2 LBIST Control (LB_CTRL0)|32|RW|0000_0000h|
|204h|STCU2 LBIST PC Stop (LB_PCS0)|32|RW|0000_0000h|
|220h|STCU2 Online LBIST MISR Expected Low (LB_MISRELSW0)|32|RW|FFFF_FFFFh|
|224h|STCU2 Online LBIST MISR Expected High (LB_MISREHSW0)|32|RW|FFFF_FFFFh|
|228h|STCU2 Online LBIST MISR Read Low (LB_MISRRLSW0)|32|RO|0000_0000h|
|22Ch|STCU2 Online LBIST MISR Read High (LB_MISRRHSW0)|32|RO|0000_0000h|
|2200h|STCU2 Algorithm Select (ALGOSEL)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1805 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

Table continued from the previous page... 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|220Ch|STCU2 MBIST Stagger (STGGR)|32|RW|0000_0000h|
|2210h|STCU2 BIST Start (BSTART)|32|RW|0000_0000h|
|2214h -<br>2244h|STCU2 MBIST Control (MB_CTRL0 - MB_CTRL12)|32|RW|0000_0000h|



### 52.10.2 STCU2 Run Software (RUNSW) 

##### Offset 

|Register|Offset|
|---|---|
|RUNSW|4h|



##### Function 

The RUNSW register defines the RUN bit to start the online self-testing procedure. 

The R/W fields in this register are readable at any time. However, you can write to these fields only when CFG[WRP] = 0. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/052_Self-Test_Control_Unit_-STCU2-/S32K3XXRM_数据表.pdf-1806-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 0 MBSW LBSW 0 0 RUNS<br>PLL... PLL... W<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-12<br>—|Reserved|
|11<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1806 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|10<br>—|Reserved|
|9|Online MBIST with PLL Enabled|
|MBSWPLLEN|0b - Online MBIST is executed without using the on-chip PLL.<br>1b - Online MBIST is executed using the PLL configuration provided by software. STCU2 does<br>not take the PLL control but monitors the PLL lock signal to check if PLL is working correctly.|
|8<br>LBSWPLLEN|Online LBIST with PLL Enabled<br>0b - Online LBIST is executed without using the on-chip PLL.<br>1b - Online LBIST is executed using the PLL configuration provided by the software. STCU2 does<br>not take the PLL control but monitors the PLL lock signal to check if PLL is working correctly.|
|7-2<br>—|Reserved|
|1<br>—|Reserved|
|0<br>RUNSW|The RUNSW bit is automatically cleared by STCU2 when the online self-testing procedure is complete.<br>0b - Idle|
||1b - Online self-testing procedure is running|



### 52.10.3 STCU2 SK Code (SKC) 

##### Offset 

|Register|Offset|
|---|---|
|SKC|8h|



##### Function 

The SKC register implements the security key code mechanism needed to access in write mode to the other STCU2 registers. 

To unlock STCU2 access after the STCU2 asynchronous reset and at the end of the STCU2 run, the software (IPS bus) need to apply the following sequence: 

- write the key1 into the SKC register 

- write the key2 into the SKC register 

Depending on the online test step, the two keys are different. Byte write operation is not allowed because the full key has to be recognized as one unit. 

In case of invalid access or sequence (Key1/2 have to be applied consecutively), a transfer error on the IPS is asserted. The STCU2 write access is locked and to unlock the access, the sequence has to be applied again. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1807 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

In case the STCU2 register access lasts more cycles than the one defined in the hard-coded WDG timeout, the STCU2 write access is locked and the WDG and register interface clocks are switched off. Also, in this case, to enable the write access to the STCU2 again and the WDG and register interface clocks, it is required to apply the sequence again. This hard-coded WDG counter starts decrementing its value right after POR is deasserted. 

In case it is required to extend the STCU2 register access cycles before the hard-coded WDG timeout expires, Key1 and Key2 sequences need to be applied. The effect of this write operation is to re-initialize the WDG timeout counter. The STCU2 write access is locked and to unlock the access, the sequence has to be applied again. 

The SKC register is not readable. The value 00000000h is always returned in case of read operation. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/052_Self-Test_Control_Unit_-STCU2-/S32K3XXRM_数据表.pdf-1808-06.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>W SKC<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>W SKC<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|STCU2 SK Code|
|SKC|STCU2 security key code for online test|
||= 753F924Eh: Key1 to unlock the write access the STCU2|
||= 8AC06DB1h: Key2 to unlock the write access the STCU2|



### 52.10.4 STCU2 Configuration (CFG) 

##### Offset 

|Register|Offset|
|---|---|
|CFG|Ch|



##### Function 

The CFG register includes the global configuration of the STCU2 and can be updated in the online test steps. 

The access to this register is described in the following figure. It further depends on the state of the WRP bit as follows: 

- When WRP = 0: The register can be written during the online self-test case without restrictions. 

- When WRP = 1: 

   - The only bit that can be written without any restriction is WRP. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1808 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

- In case there are software operations that write all the register's bits, a transfer error is raised only if the value of the selected byte written differs from the current status of the register. This functionality has been implemented to prevent potential compilation behavior that might invalidate this single bit clean capability. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/052_Self-Test_Control_Unit_-STCU2-/S32K3XXRM_数据表.pdf-1809-04.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>PTR  LB_DELAY<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 0 0<br>Reserv<br>LB_DELAY  WRP  CLK_CFG<br>W ed<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Reserved|
|—<br>30-21<br>PTR|First LBIST or MBIST pointer<br>PTR defines the logical pointer to the first LBIST or MBIST to be scheduled when the self-testing procedure<br>is enabled. PTR is the entry pointer to a linked list of BIST descriptors. If PTR = 0 then the LBIST0 is initially<br>scheduled. SeeBIST schedulingfor details.<br>You can write to this field only when WRP = 0.<br>~~NOTE~~<br>0h to (01h - 1): pointer to LBIST<br>00000080h to (00000080h + 00Dh - 1): pointer to MBIST<br>3FFh: pointer to NIL. No BIST execution.<br>others: invalid pointer => an error is set into theSTCU2 Error (ERR_STAT).|
|20-13<br>LB_DELAY|Delay LBIST run<br>LB_DELAY defines the delay between the LBIST starts when more than a single LBIST is selected to be<br>executed concurrently with the purpose of smoothing the power consumption transient. The allowed delay<br>time are these:<br>00h: No delay<br>01h: 1 x 16 STCU2 CORE_CLK cycles<br>02h: 2 x 16 STCU2 CORE_CLK cycles<br>03h: 3 x 16 STCU2 CORE_CLK cycles<br>...|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1809 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

Table continued from the previous page... 

|Field|Function<br>FDh: 253 x 16 STCU2 CORE_CLK cycles<br>FEh: 254 x 16 STCU2 CORE_CLK cycles<br>FFh: 255 x 16 STCU2 CORE_CLK cycles<br>You can write to this field only when WRP = 0.<br>~~NOTE~~|
|---|---|
|12-9<br>—<br>8<br>WRP|Reserved<br>Write Protection<br>0: Specific STCU2 registers can be written through IPS bus interface<br>1: STCU2 registers cannot be written through IPS, preventing any user application write operation|
|7-6<br>—|Reserved|
|5<br>—|Reserved|
|4<br>—<br>3<br>—|Reserved<br>Reserved|
|2-0|Logic, Memory BIST, and STCU2CORE_CLKconfiguration|
|CLK_CFG|CLK_CFG defines the ratio between the sys_clk and the internal clock used to program both the LBIST and<br>the MBIST and the STCU2 CORE_CLK. The punch-out mechanism is used to generate the derived clocks.<br>The following configurations are allowed:<br>You can write to this field only when WRP = 0.<br>~~NOTE~~<br>000b - sys_clk/1<br>001b - sys_clk/2<br>010b - sys_clk/3<br>011b - sys_clk/4<br>100b - sys_clk/5<br>101b - sys_clk/6<br>110b - sys_clk/7|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1810 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||111b - sys_clk/8|



### 52.10.5 STCU2 Watchdog Granularity (WDG) 

##### Offset 

|Register|Offset|
|---|---|
|WDG|14h|



##### Function 

The WDG register defines the time budget of LBIST and MBIST execution providing a protection mechanism in case of dead-lock or endless conditions during the self-test procedure. 

In case online self-test sequence is run, it defines the timeout of the execution run. 

The R/W fields in this register are readable at any time. You can write to these fields when online self-test phase is active and CFG[WRP] = 0. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/052_Self-Test_Control_Unit_-STCU2-/S32K3XXRM_数据表.pdf-1811-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>WDGEOC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>WDGEOC<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Watchdog End of Count Timer|
|WDGEOC|This value has to be set to define the time budget related to the online self-test execution and check that<br>everything is correctly working within this slot of time. The delay time slots that are allowed are as follows:<br>0000 0000h: 1 x 16 STCU2 CORE_CLK cycles<br>0000 0001h: 2 x 16 STCU2 CORE_CLK cycles<br>0000 0002h: 3 x 16 STCU2 CORE_CLK cycles<br>...|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1811 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

|Field|Function|
|---|---|
||FFFF FFFDh: 4294967294 x 16 STCU2 CORE_CLK cycles|
||FFFF FFFEh: 4294967295 x 16 STCU2 CORE_CLK cycles|
||FFFF FFFFh: 4294967296 x 16 STCU2 CORE_CLK cycles|



### 52.10.6 STCU2 Error (ERR_STAT) 

##### Offset 

|Register|Offset|
|---|---|
|ERR_STAT|24h|



##### Function 

The ERR_STAT register includes the status flags related to the STCU2 internal error conditions occurred during the configuration or the online self-testing execution. 

The UFSF and RFSF can be set/cleared using the FCCU dedicated channels. 

The access to this register is described in the following figure and as follows: 

- If you select the byte write capability to write only UFSF and RFSF, then there is no restriction in writing these bits. 

- If your software performs the write operations on other bits besides UFSF/RFSF, then a transfer error is generated only if the value you are writing to the other bits differs from their value currently stored in the register. This functionality has been implemented to prevent potential compilation behavior that might invalidate the UFSF/RFSF single bit set/clean capability. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/052_Self-Test_Control_Unit_-STCU2-/S32K3XXRM_数据表.pdf-1812-13.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>LOCK WDTO ENGE INVPS<br>R 0 0 0 0 0<br>ESW  SW  SW  W<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 0<br>UFSF  RFSF<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-26<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1812 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|25|Reserved|
|—<br>24|Reserved|
|—<br>23-21|Reserved|
|—<br>20<br>LOCKESW|Online LOCK error<br>You can always read this field. The content of this field is initialized to its reset value when RUNSW[RUNSW]<br>is set to 1.<br>0b - In case PLL is enabled, it is correctly locked during the self-test sequence<br>1b - When the PLL is enabled, this flag highlights that there has been an unexpected PLL<br>unlock(loss-of-lock) event during the online self-test sequence execution. The online self-test run<br>is stopped and the status of the currently running LBISTs or MBISTs is saved in the related<br>registers. The LOCK signal is monitored during the LBIST run when RUNSW[LBSWPLLEN] is set<br>and/or during the MBIST run when RUNSW[MBSWPLLEN] = 1.|
|19<br>WDTOSW|Online watchdog timeout<br>You can always read this field. The content of this field is initialized to its reset value when RUNSW[RUNSW]<br>is set to 1.<br>0b - LBIST and MBIST time slots completed within the assigned watchdog time.<br>1b - LBIST and MBIST time slots not completed within the assigned watchdog time or there are<br>internal mismatches among End of Execution signals.|
|18<br>—|Reserved|
|17<br>ENGESW|Online engine error<br>You can always read this field. The content of this field is initialized to its reset value when RUNSW[RUNSW]<br>is set to 1.<br>0b - Valid engine execution<br>1b - Invalid engine execution. The error conditions that set this bit are FSM, protocol error, and so<br>on.|
|16<br>INVPSW|Online invalid pointer<br>You can always read this field. The content of this field is initialized to its reset value when RUNSW[RUNSW]<br>is set to 1.<br>0b - Valid linked pointer list|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1813 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

##### Table continued from the previous page... 

|Field|Function<br>1b - Invalid linked pointer list. The following conditions set this bit: Initial LBIST or MBIST pointer<br>is out of range; LBIST is selected when MBIST is concurrently running or vice versa; Error in the<br>LBIST/MBIST linking (execution generates an infinite loop).|
|---|---|
|15-10<br>—|Reserved|
|9<br>UFSF|Unrecoverable Faults Status Flag<br>This flag reports the global status of the Unrecoverable Faults(UF). This field can be set or cleared using<br>the FCCU dedicated channel, and can also be set or cleared by software.<br>0b - No errors that trigger the UF condition.<br>1b - There are errors that trigger the UF condition.|
|8<br>RFSF|Recoverable Faults Status Flag<br>This flag reports the global status of the Recoverable Fault (RF). This field can be set or cleared using the<br>FCCU dedicated channel, and can also be set or cleared by software.<br>0b - No errors that trigger the Recoverable Faults condition<br>1b - There are errors that trigger the Recoverable Faults condition|
|7-5<br>—|Reserved|
|4-0<br>—|Reserved<br>Write may occur on these fields but writes have no effect.|



### 52.10.7 STCU2 Error FM (ERR_FM) 

##### Offset 

|Register|Offset|
|---|---|
|ERR_FM|28h|



##### Function 

The ERR_FM register defines the fault mapping of the STCU2 faults described in the register ERR_STAT in terms of UF or RF. All sources of internal faults can be routed to UF and RF. 

The R/W fields in this register are readable at any time. You can write to these fields when online self-test phase is active and CFG[WRP] = 0. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1814 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||0||||||LOCK|WDTO|Reserv|ENGE|INVPU|
|W||||||||||||EUFM|UFM|ed|UFM|FM|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-5<br>—|Reserved|
|4|PLL LOCK Unrecoverable Fault Mapping|
|LOCKEUFM|0b - Recoverable Fault Mapping<br>1b - Unrecoverable Fault Mapping|
|3<br>WDTOUFM|Watchdog Timeout Unrecoverable Fault Mapping<br>0b - Recoverable Fault Mapping<br>1b - Unrecoverable Fault Mapping|
|2<br>—|Reserved|
|1<br>ENGEUFM|Engine Error Unrecoverable Fault Mapping<br>0b - Recoverable Fault Mapping<br>1b - Unrecoverable Fault Mapping|
|0<br>INVPUFM|Invalid Pointer Unrecoverable Fault Mapping<br>0b - Recoverable Fault Mapping<br>1b - Unrecoverable Mapping|



### 52.10.8 STCU2 Online LBIST Status (LBSSW0) 

##### Offset 

|Register|Offset|
|---|---|
|LBSSW0|4Ch|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1815 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

##### Function 

This register includes the results corresponding to the execution of the selected online LBIST. 

The size of the register depends on the number of LBIST . 

The content of this register is initialized to its reset value when RUNSW[RUNSW] is set to 1. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||0|||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0||||||||LBSS<br>W0|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-1<br>—|Reserved|
|0-0|LBSSWn|
|LBSSWn|online status of the selected LBIST|
||0b - Failed LBIST execution|
||1b - Successful LBIST execution|



### 52.10.9 STCU2 Online LBIST End Flag (LBESW0) 

##### Offset 

|Register|Offset|
|---|---|
|LBESW0|5Ch|



##### Function 

This register includes the results corresponding to the execution of the selected online LBIST. 

The size of the register depends on the number of LBIST . 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1816 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/052_Self-Test_Control_Unit_-STCU2-/S32K3XXRM_数据表.pdf-1817-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>LBES<br>R 0<br>W0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-1<br>—|Reserved|
|0-0|LBESW|
|LBESWn|LBESWx: online LBIST end status|
||0b - LBIST execution not yet completed|
||1b - LBIST execution finished|



### 52.10.10 STCU2 Online LBIST Unrecoverable FM (LBUFM0) 

##### Offset 

|Register|Offset|
|---|---|
|LBUFM0|7Ch|



##### Function 

This register includes the results corresponding to the execution of the selected online LBIST. 

The size of the register 0 depends on the number of LBIST . 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1817 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/052_Self-Test_Control_Unit_-STCU2-/S32K3XXRM_数据表.pdf-1818-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>LBUF<br>W M0<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-1<br>—|Reserved|
|0-0|LBIST Unrecoverable Fault Mapping|
|LBUFMn|0b - Recoverable Fault mapping|
||1b - Unrecoverable Fault mapping|



### 52.10.11 STCU2 Online MBIST Status (MBSSW0) 

##### Offset 

|Register|Offset|
|---|---|
|MBSSW0|10Ch|



##### Function 

This register includes the results corresponding to the execution of the selected online MBIST in the range 0:12. The size of the register depends on the number of BISTed RAMs/ROMs. 

The content of this register is initialized to its reset value when RUNSW[RUNSW] is set to 1. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1818 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/052_Self-Test_Control_Unit_-STCU2-/S32K3XXRM_数据表.pdf-1819-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>MBSS MBSS MBSS MBSS MBSS MBSS MBSS MBSS MBSS MBSS MBSS MBSS MBSS<br>R 0<br>W12  W11  W10  W9  W8  W7  W6  W5  W4  W3  W2  W1  W0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-13<br>—|Reserved|
|12-0|MBSSW|
|MBSSWn|Online status of MBISTn (where n = 12:0).|
||0b - Failed MBIST execution|
||1b - No fault detected during the MBIST execution|



### 52.10.12 STCU2 Online MBIST End Flag (MBESW0) 

##### Offset 

|Register|Offset|
|---|---|
|MBESW0|14Ch|



##### Function 

This register includes the End Flag related to the execution of the selected online MBIST in the range 0:12. 

The size of the register depends on the number of BISTed RAMs/ROMs. 

The content of this register is initialized to its reset value when RUNSW[RUNSW] is set to 1. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1819 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/052_Self-Test_Control_Unit_-STCU2-/S32K3XXRM_数据表.pdf-1820-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>MBES MBES MBES MBES MBES MBES MBES MBES MBES MBES MBES MBES MBES<br>R 0<br>W12  W11  W10  W9  W8  W7  W6  W5  W4  W3  W2  W1  W0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-13<br>—|Reserved|
|12-0|Online end status of MBISTn (where n = 12:0).|
|MBESWn|0b - MBIST execution still ongoing|
||1b - MBIST execution finished|



### 52.10.13 STCU2 MBIST Unrecoverable FM (MBUFM0) 

##### Offset 

|Register|Offset|
|---|---|
|MBUFM0|18Ch|



##### Function 

This register defines the fault mapping, in terms of UF or RF, of the MBIST in the range 0:12 

The size of the register depends on the number of BISTed RAMs/ROMs. 

The R/W fields in this register are readable at any time. You can write to these fields when online self-test phase is active and CFG[WRP] = 0. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1820 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/052_Self-Test_Control_Unit_-STCU2-/S32K3XXRM_数据表.pdf-1821-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>MBUF MBUF MBUF MBUF MBUF MBUF MBUF MBUF MBUF MBUF MBUF MBUF MBUF<br>W M12  M11  M10  M9  M8  M7  M6  M5  M4  M3  M2  M1  M0<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-13<br>—|Reserved|
|12-0|MBESW|
|MBUFMn|Online end status of MBISTn (where n = 12:0).|
||0b - Recoverable fault mapping|
||1b - Unrecoverable fault mapping|



### 52.10.14 STCU2 LBIST Control (LB_CTRL0) 

##### Offset 

|Register|Offset|
|---|---|
|LB_CTRL0|200h|



##### Function 

This register defines the control setting of each LBIST controller. 

The R/W fields in this register are readable at any time. You can write to these fields when online self-test phase is active and CFG[WRP] = 0. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1821 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/052_Self-Test_Control_Unit_-STCU2-/S32K3XXRM_数据表.pdf-1822-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserv Reserv<br>CSM  PTR  SHS<br>W ed  ed<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>Reserv<br>SCEN_OFF  SCEN_ON  CWS<br>W ed<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Concurrent/sequential mode|
|CSM|The next LBIST is scheduled concurrently to the current one if the CSM bit is set to 1; otherwise, it is<br>scheduled sequentially to the completion of the current LBIST execution.<br>0b - Sequential mode<br>1b - Concurrent mode|
|30-21<br>PTR|Next LBIST or MBIST pointer<br>PTR defines the logical pointer to the next LBIST or MBIST to be scheduled. The next LBIST or MBIST is<br>scheduled concurrently to the current one if the CSM bit is set to 1, otherwise it is scheduled sequentially to<br>the completion of the current LBIST execution. In case of NIL pointer, the CSM bit has to be set Sequential<br>(0) to define this is the end of the list. The self-testing procedure stops after the last BIST in the configuration<br>chain is complete. SeeBIST schedulingfor details.<br>0h to (01h - 1): pointer to NLBIST-1<br>00000080h to (00000080h + 00Dh - 1): pointer to MBIST<br>3FFh: pointer to NIL. No BIST execution.<br>others: invalid pointer => an error is set into theSTCU2 Error (ERR_STAT).|
|20|Reserved|
|—|This reserved field is writable but do not write any value to it other than its reset value<br>~~NOTE~~|
|19|Reserved|
|—|This reserved field is writable but do not write any value to it other than its reset value<br>~~NOTE~~|
|18-16|Shift speed|
|SHS|SHS defines the shift speed|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1822 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

Table continued from the previous page... 

Field Function 000b - Shift at full rate (BIST clock). 001b - Shift at 1/2 rate (BIST clock). 010b - Shift at 1/3 rate (BIST clock). 011b - Shift at 1/4 rate (BIST clock). 100b - Shift at 1/5 rate (BIST clock). 101b - Shift at 1/6 rate (BIST clock). 110b - Shift at 1/7 rate (BIST clock). 111b - Shift at 1/8 rate (BIST clock). 15-12 Scan enable OFF SCEN_OFF SCEN_OFF information is used to configure the lbist controller hardware to generate off_cycles, delay cycles during the scan enable off transition. ~~<mark>NOTE</mark>~~ SCEN_OFF must be programmed to a value >=1. 0000b - 0 delay cycles 0001b - 1 delay cycle 0010b - 2 delay cycles 0011b - 3 delay cycles 0100b - 4 delay cycles 0101b - 5 delay cycles 0110b - 6 delay cycles 0111b - 7 delay cycles 1000b - 8 delay cycles 1001b - 9 delay cycles 1010b - 10 delay cycles 1011b - 11 delay cycles 1100b - 12 delay cycles 1101b - 13 delay cycles 1110b - 14 delay cycles 1111b - 15 delay cycles 11-8 Scan enable ON SCEN_ON SCEN_ON information is used to configure the lbist controller hardware to generate on_cycles, delay cycles during the scan enable on transition, Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1823 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||SCEN_ON delay register value must be programmed to a value >=1<br>~~NOTE~~|
||0000b - 0 delay cycles<br>0001b - 1 delay cycle<br>0010b - 2 delay cycles<br>0011b - 3 delay cycles<br>0100b - 4 delay cycles<br>0101b - 5 delay cycles<br>0110b - 6 delay cycles<br>0111b - 7 delay cycles<br>1000b - 8 delay cycles<br>1001b - 9 delay cycles<br>1010b - 10 delay cycles<br>1011b - 11 delay cycles<br>1100b - 12 delay cycles<br>1101b - 13 delay cycles<br>1110b - 14 delay cycles<br>1111b - 15 delay cycles|
|7<br>—|Reserved|
|6<br>—|Reserved|
|5-0|Capture window size|
|CWS|CWS defines the capture window size.<br>00_0000b - Illegal<br>00_0001b - Controller waits 1 shift cycle for capture to finish.<br>00_0010b - Controller waits 2 shift cycles for capture to finish.|
||00_0011b - Controller waits 3 shift cycles for capture to finish.<br>00_0100b - Controller waits 4 shift cycles for capture to finish.|
||00_0101b - Controller waits 5 shift cycles for capture to finish.|
||00_0110b - Controller waits 6 shift cycles for capture to finish.|
||00_0111b - Controller waits 7 shift cycles for capture to finish.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1824 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

### 52.10.15 STCU2 LBIST PC Stop (LB_PCS0) 

##### Offset 

|Register|Offset|
|---|---|
|LB_PCS0|204h|



##### Function 

This register defines the pattern counter stop of each LBIST controller. 

The R/W fields in this register are readable at any time. You can write to these fields when online self-test phase is active and CFG[WRP] = 0. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/052_Self-Test_Control_Unit_-STCU2-/S32K3XXRM_数据表.pdf-1825-09.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>PCS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>PCS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-26<br>—|Reserved|
|25-0|PCS|
|PCS|Pattern counter stop|
||PCS defines the pattern counter stop value.|



### 52.10.16 STCU2 Online LBIST MISR Expected Low (LB_MISRELSW0) 

##### Offset 

|Register|Offset|
|---|---|
|LB_MISRELSW0|220h|



##### Function 

This register defines bits 32 of the expected MISR of the online LBIST controller. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1825 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

The size of the register depends on the number of MISR bits of the related LBIST. . 

The R/W fields in this register are readable at any time. You can write to these fields when online self-test phase is active and CFG[WRP] = 0. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/052_Self-Test_Control_Unit_-STCU2-/S32K3XXRM_数据表.pdf-1826-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>MISRESWx<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>MISRESWx<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Online MISR expected low bits|
|MISRESWx|This field defines 32 bits of the expected MISR.|



### 52.10.17 STCU2 Online LBIST MISR Expected High (LB_MISREHSW0) 

##### Offset 

|Register|Offset|
|---|---|
|LB_MISREHSW0|224h|



##### Function 

The size of the register depends on the number of MISR bits of the related LBIST. . 

The R/W fields in this register are readable at any time. You can write to these fields when online self-test phase is active and CFG[WRP] = 0. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1826 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/052_Self-Test_Control_Unit_-STCU2-/S32K3XXRM_数据表.pdf-1827-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>MISRESWx<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>MISRESWx<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Online MISR Expected High Bits|
|MISRESWx|This field defines the 32 bits of the expected MISR.|



### 52.10.18 STCU2 Online LBIST MISR Read Low (LB_MISRRLSW0) 

##### Offset 

|Register|Offset|
|---|---|
|LB_MISRRLSW0|228h|



##### Function 

This register reports 32 bits of the MISR obtained at the end of the online LBIST controller execution. 

The size of the register depends on the number of MISR bits of the related LBIST. . 

The content of this register is initialized to its reset value reset value when RUNSW[RUNSW] is set to 1. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/052_Self-Test_Control_Unit_-STCU2-/S32K3XXRM_数据表.pdf-1827-14.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R MISRRSWx<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R MISRRSWx<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1827 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

##### Fields 

|Field|Function|
|---|---|
|31-0|MISRRSWx|
|MISRRSWx|Online MISR Read Low Bin|
||This field is equivalent to 32 bits of the MISR obtained at the end of the online LBIST execution.|



### 52.10.19 STCU2 Online LBIST MISR Read High (LB_MISRRHSW0) 

##### Offset 

|Register|Offset|
|---|---|
|LB_MISRRHSW0|22Ch|



##### Function 

The size of the register depends on the number of MISR bits of the related LBIST. . 

The content of this register is initialized to its reset value reset value when RUNSW[RUNSW] is set to 1. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/052_Self-Test_Control_Unit_-STCU2-/S32K3XXRM_数据表.pdf-1828-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R MISRRSWx<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R MISRRSWx<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|MISRRSWx|
|MISRRSWx|Online MISR Read High Bits|
||This field is equivalent to 32 bits of the MISR obtained at the end of the online LBIST execution.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1828 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

### 52.10.20 STCU2 Algorithm Select (ALGOSEL) 

##### Offset 

|Register|Offset|
|---|---|
|ALGOSEL|2200h|



##### Function 

This is a 32-bit register intended to be programmed by the user to select algorithms to be run on BIST. See the chip-specific STCU2 information for details of this register. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|ALGO<br>SEL...|ALGO<br>SEL...|ALGO<br>SEL...|ALGO<br>SEL...|ALGO<br>SEL...|ALGO<br>SEL...|ALGO<br>SEL...|ALGO<br>SEL...|ALGO<br>SEL...|ALGO<br>SEL...|ALGO<br>SEL...|ALGO<br>SEL...|ALGO<br>SEL...|ALGO<br>SEL...|ALGO<br>SEL...|ALGO<br>SEL...|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|ALGO<br>SEL...|ALGO<br>SEL...|ALGO<br>SEL...|ALGO<br>SEL...|ALGO<br>SEL...|ALGO<br>SEL...|ALGO<br>SEL9|ALGO<br>SEL8|ALGO<br>SEL7|ALGO<br>SEL6|ALGO<br>SEL5|ALGO<br>SEL4|ALGO<br>SEL3|ALGO<br>SEL2|ALGO<br>SEL1|ALGO<br>SEL0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-0|Algorithm Select|
|ALGOSELn||



### 52.10.21 STCU2 MBIST Stagger (STGGR) 

##### Offset 

|Register|Offset|
|---|---|
|STGGR|220Ch|



##### Function 

This register allows one to program number of clock cycles between execution of one BIST and the next one. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1829 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/052_Self-Test_Control_Unit_-STCU2-/S32K3XXRM_数据表.pdf-1830-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>STAG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>STAG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|STAG|
|STAG|Number of STCU2 CORE_CLK cycles between execution of one BIST and the next one.|



### 52.10.22 STCU2 BIST Start (BSTART) 

##### Offset 

|Register|Offset|
|---|---|
|BSTART|2210h|



##### Function 

This is a 32-bit register intended to be programmed by the user to run BISTs with different configuration. See the chip-specific STCU2 information for details of this register. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|BSTA<br>RT31|BSTA<br>RT30|BSTA<br>RT29|BSTA<br>RT28|BSTA<br>RT27|BSTA<br>RT26|BSTA<br>RT25|BSTA<br>RT24|BSTA<br>RT23|BSTA<br>RT22|BSTA<br>RT21|BSTA<br>RT20|BSTA<br>RT19|BSTA<br>RT18|BSTA<br>RT17|BSTA<br>RT16|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|BSTA<br>RT15|BSTA<br>RT14|BSTA<br>RT13|BSTA<br>RT12|BSTA<br>RT11|BSTA<br>RT10|BSTA<br>RT9|BSTA<br>RT8|BSTA<br>RT7|BSTA<br>RT6|BSTA<br>RT5|BSTA<br>RT4|BSTA<br>RT3|BSTA<br>RT2|BSTA<br>RT1|BSTA<br>RT0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1830 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

##### Fields 

|Field|Function|
|---|---|
|31-0|BIST Start|
|BSTARTn||



### 52.10.23 STCU2 MBIST Control (MB_CTRL0 - MB_CTRL12) 

##### Offset 

For a = 0 to 12: 

|Register|Offset|
|---|---|
|MB_CTRLa|2214h + (a × 4h)|



##### Function 

The MB_CTRL register defines the control setting of MBIST controller. 

The R/W fields in this register are readable at any time. You can write to these fields when online self-test phase is active and CFG[WRP] = 0. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|CSM|||||PTR||||||BSEL||0|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|CSM|
|CSM|Concurrent/sequential mode|
||0b - Sequential mode|
||1b - Concurrent mode|
|30-21|PTR|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1831 / 4640 

NXP Semiconductors 

Self-Test Control Unit (STCU2) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|PTR|Next LBIST or MBIST pointer<br>PTR defines the logical pointer to the next LBIST or MBIST to be scheduled. The next LBIST orMBIST is<br>scheduled concurrently to the current one if the CSM bit is set to 1; otherwise it is scheduled sequentially to<br>the completion of the current MBIST execution. In case of NIL pointer the CSM bit must be set Sequential<br>(0) to define this is the end of the list. The self-testing procedure stops after the last BIST in the configuration<br>chain is complete. SeeBIST schedulingfor details.<br>If the pointer is invalid and MBIST is scheduled to run concurrently than this invalid scenario<br>is handled by watchdog timeout feature and corresponding watchdog timeout status bit will<br>be updated in ERR_STAT[WDTOSW]. In this particular case ERR_STAT[INVPSW] will not<br>be set.<br>~~NOTE~~<br>0h to (01h - 1): pointer to LBIST<br>00000080h to (00000080h + 00Dh - 1): pointer to MBIST<br>3FFh: pointer to NIL. No next BIST execution.<br>others: invalid pointer => an error is set into theSTCU2 Error (ERR_STAT).|
|20<br>BSEL|BSEL<br>BIST Select<br>0b - Selected BIST is not selected for execution.<br>1b - Selected BIST is selected for execution.|
|19-0<br>—|Reserved|



## 52.11 Glossary 

|BIST|Built-in self-test|
|---|---|
|BIST Clock|BIST controller clock corresponding to the specific BIST|
|CORE_CLK|Clock specified by the CFG register|
|FSM|Finite state machine|
|IPS|Internal peripheral system|
|LBIST|Logic BIST|
|MBIST|Memory BIST|
|NLBIST|Number of logic built-in self-test controller|
|NMCUT|Number of memory checked using memory built-in self-test controller|
|RF|Recoverable faults|
|UF|Unrecoverable faults|
|WDG FSM|Watchdog finite state machine|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1832 / 4640 

