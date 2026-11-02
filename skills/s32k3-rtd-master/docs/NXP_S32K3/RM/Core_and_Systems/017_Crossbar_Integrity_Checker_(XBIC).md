NXP Semiconductors 

# Chapter 17 Crossbar Integrity Checker (XBIC) 

## 17.1 Chip-specific XBIC information 

### 17.1.1 XBIC instances and configuration 

This chip has up to five instances of XBIC. The following tables describes the instances and their configuration. 

Table 57. XBIC instances 

|Instance|S32K358|S32K322/S32K342/S32K314/S32K324/S32K344|S32K312|
|---|---|---|---|
|XBIC_0|Yes|Yes|Yes|
|XBIC_1|Yes|Yes|No|
|XBIC_2|Yes|Yes|No|
|XBIC_3|No|Yes|No|
|XBIC_4|Yes|No|No|



Table 58. XBIC configuration for S32K358 

|Instance|Available on crossbar|Master a|nd slave assignments|||
|---|---|---|---|---|---|
|XBIC_0|AXBS_0 (main)|||||
|||Master<br>port|Master module|Slave<br>port|Slave module|
|||M0|Cortex-M7_0 AHBM|S0|Flash memory port 0|
|||M1|DMA/ STAM|S1|Flash memory port 1|
|||M2|HSE_B|S2|PRAM_0|
|||M3|EMAC|S3|Cortex-M7 TCM/ PRAM_2|
|||M4|Cortex-M7_1 AHBM|S4|Flash memory Port 2|
|||M5|Cortex-M7_2 AHBM|S5|QuadSPI|
|||M6|uSDHC|S6|PRAM_1|
|||||S7|Flash memory port 3|
|XBIC_1|AXBS_1 (peripheral)|||||
|||Master<br>port|Master module|Slave<br>port|Slave module|
|||M0|Cortex-M7_0 AHBP|S0|AIPS_0|
|||M1|DMA/ STAM|S1|AIPS_1|
|||M2|HSE_B|S2|AIPS_2|
|||M3|Cortex-M7_1 AHBP|||
|||M4|Cortex-M7_2 AHBP|||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

525 / 4640 

NXP Semiconductors 

Crossbar Integrity Checker (XBIC) 

Table 58. XBIC configuration for S32K358 (continued) 

|Instance|Available on crossbar|Master a|nd slave assignments|||
|---|---|---|---|---|---|
|XBIC_2|AXBS_2 (eDMA)|||||
|||Master<br>port|Master module|Slave<br>port|Slave module|
|||M0|eDMA|S0|System AXBS|
|||||S1|Peripheral AXBS|
|XBIC_3|AXBS_3 (Cortex-<br>M7 TCM)|Not appli|cable|||
|XBIC_4|AXBS_4 (Cortex-M7|||||
||TCM PRAM)|Master<br>port|Master module|Slave<br>port|Slave module|
|||M0|System AXBS|S0|PRAM_2|
|||||S1|Cortex-M7_0 TCM|
|||||S2|Cortex-M7_1 TCM|
|||||S3|Cortex-M7_2 TCM|



Table 59. XBIC configuration for S32K322/S32K342/S32K314/S32K324/S32K344 

|Instance|Available on crossbar|Master a|nd slave assignments|||
|---|---|---|---|---|---|
|XBIC_0|AXBS_0 (main)|||||
|||Master<br>port|Master module|Slave<br>port|Slave module|
|||M0|Cortex-M7_0 AHBM|S0|Flash memory port 0|
|||M1|AXBS_2 S0|S1|Flash memory port 1|
|||M2|HSE_B|S2|PRAM_0|
|||M3|EMAC|S3|Cortex-M7 TCM|
|||M4<sup>1</sup>|Cortex-M7_1 AHBM|S4|Flash memory Port 2|
|||||S5|QuadSPI|
|||||S6|PRAM_1|
|XBIC_1|AXBS_1 (peripheral)|||||
|||Master<br>port|Master module|Slave<br>port|Slave module|
|||M0|Cortex-M7_0 AHBP|S0|AIPS_0|
|||M1|AXBS_2 S1|S1|AIPS_1|
|||M2|HSE_B|S2|AIPS_2|
|||M3<sup>1</sup>|Cortex-M7_1 AHBP|||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

526 / 4640 

NXP Semiconductors 

Crossbar Integrity Checker (XBIC) 

Table 59. XBIC configuration for S32K322/S32K342/S32K314/S32K324/S32K344 (continued) 

|Instance|Available on crossbar|Master a|nd slave assignments|||
|---|---|---|---|---|---|
|||1. Thes|e ports are reserved for S3|2K314.||
|XBIC_2|AXBS_2 (eDMA)|||||
|||Master<br>port|Master module|Slave<br>port|Slave module|
|||M0|eDMA|S0|AXBS_0 M1|
|||||S1|AXBS_1 M1|
|XBIC_3|AXBS_3 (Cortex-|||||
||M7 TCM)|Master<br>port|Master module|Slave<br>port|Slave module|
|||M0|AXBS_0 S3|S0|Cortex-M7_0 TCM|
|||||S1<sup>1</sup>|Cortex-M7_1 TCM|



Table 60. XBIC configuration for S32K312 

|Instance|Available on crossbar|Master a|nd slave assignments|||
|---|---|---|---|---|---|
|XBIC_0|AXBS_0 (main)|||||
|||Master<br>port|Master module|Slave<br>port|Slave module|
|||M0|Cortex-M7_0 AHBM|S0|Flash memory port 0|
|||M1|eDMA|S1|Flash memory port 1|
|||M2|HSE_B|S2|PRAM_0|
|||M3|Cortex-M7_0 AHBP|S3|Cortex-M7 TCM|
|||M4|Reserved|S4|AIPS_0|
|||||S5|AIPS_1|



The errors detected are connected to FCCU. See the memory map file attached to this document for details. 

~~<mark>NOTE</mark>~~ 

- Reset value of MCR register for S32K311, S32K3x2 and S32K3x4 is "FFFF_0000h". 

- For S32K358 specific reset value, see MCR register description. 

### 17.1.2 Target master IDs 

See "Chip-specific XRDC information" for master IDs. 

## 17.2 Overview 

XBIC verifies the integrity of crossbar transfers. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

527 / 4640 

NXP Semiconductors 

Crossbar Integrity Checker (XBIC) 

## 17.3 Features 

XBIC includes the following features: 

- Verification of attribute information for crossbar transfers<sup>[1],[2]</sup> 

   - EDC detects single- and double-bit errors 

- Verification of feedback information for each data phase during crossbar transfers 

- Error injection for testing 

   - Programmable master and slave port specifiers 

   - Programmable 8-bit toggle vector to insert error in master EDC value 

   - Address, EDC syndrome, master, and slave port information are captured when error is detected 

- Crossbar transfer attribute integrity check programmable on a per-slave-port basis 

- Feedback integrity check programmable on a per-master-port basis 

## 17.4 Block diagram 

The chip routes crossbar transfer attribute information for all mapped master and slave ports to XBIC, which calculates and checks the EDC value of the attribute information, as shown in the following diagram. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/017_Crossbar_Integrity_Checker_-XBIC-/S32K3XXRM_数据表.pdf-0528-15.png)


<!-- Start of picture text -->
master 0 master 1 master 7<br>Master data phase output<br>Master attribute input<br>Attribute EDC output<br>m0 m1 ... m7 m0 m1 ... m7<br>XBIC Crossbar<br>s0 s1 ... s7 s0 s1 ... s7<br>Attribute EDC input<br>Slave attribute input<br>Slave data phase output<br>Error out<br>to FCCU<br>slave 0 slave 1 slave 7<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/017_Crossbar_Integrity_Checker_-XBIC-/S32K3XXRM_数据表.pdf-0528-16.png)


<!-- Start of picture text -->
Figure 37. XBIC system block diagram<br><!-- End of picture text -->

The above figure illustrates one of many possible XBIC and crossbar configurations. See the Chip-specific XBIC information section for actual port mappings. 

- [1] See Table 61 for a list of crossbar attribute signals verified. 

- [2] The chip verifies read and write data separately, via the end-to-end ECC architecture. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

528 / 4640 

NXP Semiconductors 

Crossbar Integrity Checker (XBIC) 

## 17.5 Signal description 

XBIC has no external interface signals. 

## 17.6 Functional description 

XBIC verifies the integrity of the crossbar interface on an individual port basis according to the configuration specified via the MCR register. When XBIC detects an error, it reports relevant information and sends an error signal to the FCCU module, but does not generate a bus error. XBIC integrity checking is independent of end-to-end ECC, which monitors the integrity of the transfer address and data. 

During the address phase of a transfer, XBIC verifies the crossbar attribute information using an 8-bit EDC, which detects any single-bit or double-bit errors. When XBIC detects an error (an attribute integrity error), due to either hardware fault or error injection, it reports information related to the error in ESR and EAR. 

During the data phase of a data transfer, XBIC verifies the integrity of response signals from slave to master as they pass through the crossbar. When XBIC detects an error in the response signals (a feedback integrity error), it reports the XBIC slave and master ports in ESR[DPSE0] - ESR[DPSE7] and ESR[DPME0] - ESR[DPME7], respectively. 

During the data phase, XBIC sends an alarm to the FCCU module if a master port attempts back-to-back accesses in which: 

1. The first access terminates normally. 

2. The second attempts access to an address space not mapped to any slave on the crossbar. 

The resultant 'absent slave error' causes the crossbar to generate a bus error response to the requesting master. XBIC detects the bus error response as a difference because the bus error did not originate from the slave port. 

You can program XBIC to inject EDC errors for testing purposes. Error injection targets a single slave port and a single master port, as specified by the configuration settings in the EIR register. When XBIC inserts an error, it changes the EDC syndrome, causing the XBIC to assert an error indication to the FCCU module. Otherwise, transfers are unaffected by error injection. This enables verification of the check logic without compromising the integrity of the data transfer. After you enable error injection function by writing 1 to EIR[EIE], XBIC induces errors on all subsequent targeted transactions until you write a 0 to the field. After the FCCU error indication asserts, it remains asserted even after you write 0 to EIR[EIE]. The error indication deasserts after FCCU specifically clears the existing error. After FCCU clears the XBIC error, additional error injection testing can continue. 

To trace a fault reported by the XBIC to the FCCU: 

1. Note the error reported by the FCCU. For example, "NCF[46]". 

2. Locate the source module and error description in the attached fault mapping spreadsheet. For example: 

   - Channel number: NCF[46] 

   - Source module: AXBS_1 integrity checker 

   - Description: Instruction crossbar error indication to FCCU if syndrome calculated using EDC on the data is not zero 

3. Refer to the Chip-specific XBIC information section for the source XBIC module to determine the specific XBIC module instance—"XBIC_1", for example. 

4. Determine the type of error (attribute integrity error or feedback integrity error) and the XBIC port(s) involved by reading the information reported in the ESR register of the reported XBIC instance. 

5. For attribute integrity check errors, read the XBIC EAR register for the target address of the requested transfer. 

6. Refer to the Chip-specific XBIC information section and possibly the Chip-specific AXBS information section for port mapping of XBIC ports to AXBS ports. 

Decode a single-bit error syndrome value reported in ESR[SYN] by finding the value in the following table. Any syndrome value not included in the table indicates a multi-bit error. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

529 / 4640 

NXP Semiconductors 

Crossbar Integrity Checker (XBIC) 

Table 61. Hexadecimal attribute single-bit error syndromes 

|Signal|SYN|Signal|SYN|Signal|SYN|Signal|SYN|
|---|---|---|---|---|---|---|---|
|hwrite|07|hbstrb[7]|70|hdecor[31]|25|hdecor[15]|23|
|htrans[0]|0b|hbstrb[6]|32|hdecor[30]|68|hdecor[14]|51|
|hsize[2]|0d|hbstrb[5]|52|hdecor[29]|c7|hdecor[13]|54|
|hsize[1]|0e|hbstrb[4]|a8|hdecor[28]|83|hdecor[12]|61|
|hsize[0]|13|hbstrb[3]|43|hdecor[27]|85|hdecor[11]|e3|
|hprot[5]|15|hbstrb[2]|45|hdecor[26]|86|hdecor[10]|e6|
|hprot[4]|16|hbstrb[1]|4c|hdecor[25]|89|hdecor[9]|f8|
|hprot[3]|19|hbstrb[0]|a4|hdecor[24]|8a|hdecor[8]|38|
|hprot[2]|1a|hmaster[3]|a2|hdecor[23]|8c|hdecor[7]|58|
|hprot[1]|1c|hmaster[2]|b0|hdecor[22]|49|hdecor[6]|37|
|hprot[0]|91|hmaster[1]|c1|hdecor[21]|92|hdecor[5]|f1|
|hburst[2]|a1|hmaster[0]|c2|hdecor[20]|94|hdecor[4]|3b|
|hburst[1]|64|hslave[2]|c4|hdecor[19]|98|hdecor[3]|3d|
|hburst[0]|29|hslave[1]|c8|hdecor[18]|46|hdecor[2]|3e|
|hmastlock|2a|hslave[0]|d0|hdecor[17]|34|hdecor[1]|4f|
|hunalign|2c|hdecorated|e0|hdecor[16]|4a|hdecor[0]|6e|
|edc[7]|80|edc[6]|40|edc[5]|20|edc[4]|10|
|edc[3]|08|edc[2]|04|edc[1]|02|edc[0]|01|



## 17.7 XBIC register descriptions 

The XBIC programming model consists of four 32-bit registers. Software can access this model only in supervisor mode using 32-bit (word) accesses. Each of the following generates a transaction error back to the requesting master. Such errors could cause core exceptions apart from other problems. 

- Access size other than 32-bit 

- Access to an undefined (reserved) address 

- Unsupported access type—an attempted write to a read-only register, for example 

- Access in user mode 

### 17.7.1 XBIC memory map 

XBIC_AXBS base address: 4020_4000h 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

530 / 4640 

NXP Semiconductors 

Crossbar Integrity Checker (XBIC) 

#### XBIC_AXBS_PERI base address: 4020_8000h 

XBIC_AXBS_PRAM_TCM base address: 4040_8000h 

XBIC_AXBS_eDMA base address: 4040_4000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|XBIC Module Control (MCR)|32|RW|See<br>description|
|4h|XBIC Error Injection (EIR)|32|RW|0000_0000h|
|8h|XBIC Error Status (ESR)|32|W1C|0000_0000h|
|Ch|XBIC Error Address (EAR)|32|RO|0000_0000h|



### 17.7.2 XBIC Module Control (MCR) 

#### Offset 

|Register|Offset|
|---|---|
|MCR|0h|



#### Function 

Use this register to turn attribute integrity checking and feedback integrity checking on or off on a per-port basis. 

- Turn on attribute integrity checking on one or more XBIC slave ports by ensuring that the associated SEn field(s) have a value of 1. For example, setting field SE0 enables attribute integrity checking for slave port 0. The default (reset) behavior is for attribute integrity checking to be performed for all slave ports. XBIC performs EDC-based checks on all transfer requests targeting the selected slave port(s). The signals verified are transfer attribute signals going from master to slave. When XBIC detects an attribute integrity error, it reports relevant information in the ESR and EAR registers. 

- Turn on feedback integrity checking on one or more XBIC master ports by ensuring that the associated MEn field(s) have a value of 1. For example, setting field ME0 to 1 enables feedback integrity checking for master port 0. The default (reset) behavior is for feedback integrity checking to be performed for all master ports. XBIC checks slave-to-master feedback signals for transfer requests originating from the selected XBIC master port(s). If any feedback signal value is different at the master and slave ports during the data phase, XBIC reports the relevant master and slave ports in the ESR register. 

Each field in this register references a specific master or slave port using XBIC port numbering. Referring to Figure 37, "slave port 0" refers to XBIC port "s0" in the figure, "slave port 1" refers to port "s1", and so on. Similarly, "master port 0" refers to XBIC port "m0", "master port 1" refers to port "m1", and so on. See the "Chip-specific XBIC information" section in this document for the mapping of XBIC instances to AXBS instances and XBIC ports to AXBS ports. See the "Chip-specific AXBS information" section in this document for the device component(s) mapped to each port of an AXBS instance. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

531 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/017_Crossbar_Integrity_Checker_-XBIC-/S32K3XXRM_数据表.pdf-0532-01.png)


<!-- Start of picture text -->
Crossbar Integrity Checker (XBIC)<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/017_Crossbar_Integrity_Checker_-XBIC-/S32K3XXRM_数据表.pdf-0532-02.png)


<!-- Start of picture text -->
Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>SE0  SE1  SE2  SE3  SE4  SE5  SE6  SE7  ME0  ME1  ME2  ME3  ME4  ME5  ME6<br>W<br>Reset See Register reset values.<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W<br>Reset See Register reset values.<br><!-- End of picture text -->

#### Register reset values 

|Register|Reset value|
|---|---|
|MCR|XBIC_AXBS: FFFE_0000h|
||XBIC_AXBS_PERI: E0F8_0000h|
||XBIC_AXBS_PRAM_TCM: F080_0000h|
||XBIC_AXBS_eDMA: C0C0_0000h|



#### Fields 

|Field|Function||
|---|---|---|
|31<br>SE0|Slave port EDC Error Detection Enable<br>0b - Attribute integrity checking disabled for slave port 0<br>1b - Attribute integrity checking enabled for slave port 0||
|30<br>SE1|Slave port EDC Error Detection Enable<br>0b - Attribute integrity checking disabled for slave port 1<br>1b - Attribute integrity checking enabled for slave port 1||
|29|Slave port EDC Error Detection Enable||
|SE2|This field is not supported in every instance. The following ta<br>supported registers.<br>~~NOTE~~|ble includes only|
||Instance<br>Field supported in|Field not supported in|
||XBIC_AXBS<br>MCR|—|
||XBIC_AXBS_PERI<br>MCR|—|
||XBIC_AXBS_PRAM_TCM<br>MCR|—|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

532 / 4640 

NXP Semiconductors 

Crossbar Integrity Checker (XBIC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/017_Crossbar_Integrity_Checker_-XBIC-/S32K3XXRM_数据表.pdf-0533-02.png)


<!-- Start of picture text -->
Field Function<br>Instance Field supported in Field not supported in<br>XBIC_AXBS_eDMA — MCR<br>0b - Attribute integrity checking disabled for slave port 2<br>1b - Attribute integrity checking enabled for slave port 2<br>28 Slave port EDC Error Detection Enable<br>SE3   NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>XBIC_AXBS MCR —<br>XBIC_AXBS_PERI — MCR<br>XBIC_AXBS_PRAM_TCM MCR —<br>XBIC_AXBS_eDMA — MCR<br>0b - Attribute integrity checking disabled for slave port 3<br>1b - Attribute integrity checking enabled for slave port 3<br>27 Slave port EDC Error Detection Enable<br>SE4   NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>XBIC_AXBS MCR —<br>XBIC_AXBS_PERI — MCR<br>XBIC_AXBS_PRAM_TCM — MCR<br>XBIC_AXBS_eDMA — MCR<br>0b - Attribute integrity checking disabled for slave port 4<br>1b - Attribute integrity checking enabled for slave port 4<br>26 Slave port EDC Error Detection Enable<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

533 / 4640 

NXP Semiconductors 

Crossbar Integrity Checker (XBIC) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/017_Crossbar_Integrity_Checker_-XBIC-/S32K3XXRM_数据表.pdf-0534-03.png)


<!-- Start of picture text -->
Field Function<br>SE5<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>XBIC_AXBS MCR —<br>XBIC_AXBS_PERI — MCR<br>XBIC_AXBS_PRAM_TCM — MCR<br>XBIC_AXBS_eDMA — MCR<br>0b - Attribute integrity checking disabled for slave port 5<br>1b - Attribute integrity checking enabled for slave port 5<br>25 Slave port EDC Error Detection Enable<br>SE6   NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>XBIC_AXBS MCR —<br>XBIC_AXBS_PERI — MCR<br>XBIC_AXBS_PRAM_TCM — MCR<br>XBIC_AXBS_eDMA — MCR<br>0b - Attribute integrity checking disabled for slave port 6<br>1b - Attribute integrity checking enabled for slave port 6<br>24 Slave Port EDC Error Detection Enable<br>SE7   NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

534 / 4640 

NXP Semiconductors 

Crossbar Integrity Checker (XBIC) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/017_Crossbar_Integrity_Checker_-XBIC-/S32K3XXRM_数据表.pdf-0535-03.png)


<!-- Start of picture text -->
Field Function<br>Instance Field supported in Field not supported in<br>XBIC_AXBS MCR —<br>XBIC_AXBS_PERI — MCR<br>XBIC_AXBS_PRAM_TCM — MCR<br>XBIC_AXBS_eDMA — MCR<br>0b - Attribute integrity checking disabled for slave port 7<br>1b - Attribute integrity checking enabled for slave port 7<br>23 Master Port Enable For Feedback Integrity Check<br>ME0 0b - Feedback integrity checking disabled for master port 0<br>1b - Feedback integrity checking enabled for master port 0<br>22 Master Port Enable For Feedback Integrity Check<br>ME1   NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>XBIC_AXBS MCR —<br>XBIC_AXBS_PERI MCR —<br>XBIC_AXBS_PRAM_TCM — MCR<br>XBIC_AXBS_eDMA MCR —<br>0b - Feedback integrity checking disabled for master port 1<br>1b - Feedback integrity checking enabled for master port 1<br>21 Master Port Enable For Feedback Integrity Check<br>ME2   NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

535 / 4640 

NXP Semiconductors 

Crossbar Integrity Checker (XBIC) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/017_Crossbar_Integrity_Checker_-XBIC-/S32K3XXRM_数据表.pdf-0536-03.png)


<!-- Start of picture text -->
Field Function<br>Instance Field supported in Field not supported in<br>XBIC_AXBS MCR —<br>XBIC_AXBS_PERI MCR —<br>XBIC_AXBS_PRAM_TCM — MCR<br>XBIC_AXBS_eDMA — MCR<br>0b - Feedback integrity checking disabled for master port 2<br>1b - Feedback integrity checking enabled for master port 2<br>20 Master Port Enable For Feedback Integrity Check<br>ME3   NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>XBIC_AXBS MCR —<br>XBIC_AXBS_PERI MCR —<br>XBIC_AXBS_PRAM_TCM — MCR<br>XBIC_AXBS_eDMA — MCR<br>0b - Feedback integrity checking disabled for master port 3<br>1b - Feedback integrity checking enabled for master port 3<br>19 Master Port Enable For Feedback Integrity Check<br>ME4   NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>XBIC_AXBS MCR —<br>XBIC_AXBS_PERI MCR —<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/017_Crossbar_Integrity_Checker_-XBIC-/S32K3XXRM_数据表.pdf-0536-04.png)


<!-- Start of picture text -->
Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

536 / 4640 

NXP Semiconductors 

Crossbar Integrity Checker (XBIC) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/017_Crossbar_Integrity_Checker_-XBIC-/S32K3XXRM_数据表.pdf-0537-03.png)


<!-- Start of picture text -->
Field Function<br>Instance Field supported in Field not supported in<br>XBIC_AXBS_PRAM_TCM — MCR<br>XBIC_AXBS_eDMA — MCR<br>0b - Feedback integrity checking disabled for master port 4<br>1b - Feedback integrity checking enabled for master port 4<br>18 Master Port Enable For Feedback Integrity Check<br>ME5   NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>XBIC_AXBS MCR —<br>XBIC_AXBS_PERI — MCR<br>XBIC_AXBS_PRAM_TCM — MCR<br>XBIC_AXBS_eDMA — MCR<br>0b - Feedback integrity checking disabled for master port 5<br>1b - Feedback integrity checking enabled for master port 5<br>17 Master Port Enable For Feedback Integrity Check<br>ME6   NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>XBIC_AXBS MCR —<br>XBIC_AXBS_PERI — MCR<br>XBIC_AXBS_PRAM_TCM — MCR<br>XBIC_AXBS_eDMA — MCR<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

537 / 4640 

NXP Semiconductors 

Crossbar Integrity Checker (XBIC) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Feedback integrity checking disabled for master port 6|
||1b - Feedback integrity checking enabled for master port 6|
|16<br>—|Reserved|
|15-0<br>—|Reserved|



### 17.7.3 XBIC Error Injection (EIR) 

#### Offset 

|Register|Offset|
|---|---|
|EIR|4h|



#### Function 

Use this register to configure the XBIC error injection function and turn it on or off. When enabled, the XBIC error injection function inserts an attribute integrity error when the targeted master requests a transaction of the targeted slave port. The inserted error changes the calculated EDC syndrome value, causing XBIC to: 

- Capture transfer information in the ESR and EAR registers 

- Assert an error signal to the FCCU module 

Otherwise, XBIC error injection does not affect transfers. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/017_Crossbar_Integrity_Checker_-XBIC-/S32K3XXRM_数据表.pdf-0538-13.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>EIE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>SLV  MST  SYN<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

538 / 4640 

NXP Semiconductors 

Crossbar Integrity Checker (XBIC) 

#### Fields 

|Field|Function|
|---|---|
|31|Error Injection Enable|
|EIE|This field is auto-cleared, once error is generated and acknowledged by FCCU<br>~~NOTE~~|
||0b - Error injection disabled<br>1b - Error injection enabled|
|30-15<br>—|Reserved|
|14-12<br>SLV|Target Slave Port<br>Specifies the target slave port for error injection—other slave ports are unaffected.<br>Specify the target slave port by its XBIC slave port number (0–7). See the "Chip-specific XBIC information"<br>section in this document for the mapping of XBIC instances to AXBS instances and XBIC ports to AXBS<br>ports. See the "Chip-specific AXBS information" section in this document for the device component(s)<br>mapped to each port of an AXBS instance.|
|11-8|Target Master ID|
|MST|Specifies the target master port for error injection—transfers with other masters are unaffected.<br>Specify the target master port using the logical master ID number of the target bus master. See the "Chip-<br>specific XBIC information" section in this document for the master IDs and their corresponding components.|
|7-0|Syndrome|
|SYN|XBIC performs an exclusive OR operation on the value in this field and the calculated syndrome, to generate<br>an error with the specified syndrome. A value of zero does not generate an error. SeeTable 61for a list of<br>transfer attribute single-bit error syndromes, noting that the values given in the table are hexadecimal.|



### 17.7.4 XBIC Error Status (ESR) 

#### Offset 

|Register|Offset|
|---|---|
|ESR|8h|



#### Function 

In this register, XBIC reports information about the most recent transfer with an error detected. If XBIC detects an attribute integrity check error, it reports: 

- The slave port identifier (SLV) 

- The master port identifier (MST) 

- The error syndrome (SYN) 

If XBIC detects a mismatch among feedback signals during the data phase: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

539 / 4640 

NXP Semiconductors 

Crossbar Integrity Checker (XBIC) 

- The DPSE0 - DPSE7 field with a value of 1 indicates the XBIC slave port. In the DPSE0-DPSE7 field descriptions, the slave port number refers to the XBIC slave port number. Referring to Figure 37, "slave port 0" refers to XBIC port "s0" in the figure, "slave port 1" refers to port "s1", and so on. See the "Chip-specific XBIC information" section in this document for the mapping of XBIC instances to AXBS instances and XBIC ports to AXBS ports. See the "Chip-specific AXBS information" section in this document for the device component(s) mapped to each port of an AXBS instance. 

- The DPME0 - DPME7 field with a value of 1 indicates the XBIC master port. In the DPME0-DPME7 field descriptions, the master port number refers to the XBIC master port number. Referring to Figure 37, "master port 0" refers to XBIC port "m0" in the figure, "master port 1" refers to port "m1", and so on. See the "Chip-specific XBIC information" section in this document for the mapping of XBIC instances to AXBS instances and XBIC ports to AXBS ports. See the "Chip-specific AXBS information" section in this document for the device component(s) mapped to each port of an AXBS instance. 

XBIC sets this register to all 0s only on reset. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/017_Crossbar_Integrity_Checker_-XBIC-/S32K3XXRM_数据表.pdf-0540-06.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>DPSE DPSE DPSE DPSE DPSE DPSE DPSE DPSE DPME DPME DPME DPME DPME DPME DPME<br>R VLD<br>0  1  2  3  4  5  6  7  0  1  2  3  4  5  6<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>DPME<br>R SLV  MST  SYN<br>7<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31|Error Status Valid|
|VLD|0b - No error detected—other fields of the ESR and EAR registers are invalid<br>1b - Error detected—all fields of the ESR and EAR registers are valid|
|30<br>DPSE0|Data Phase Slave Port Error<br>0b - No feedback integrity error detected on slave port 0<br>1b - Feedback integrity error detected on slave port 0|
|29<br>DPSE1|Data Phase Slave Port Error<br>0b - No feedback integrity error detected on slave port 1<br>1b - Feedback integrity error detected on slave port 1|
|28|Data Phase Slave Port Error|
|DPSE2|0b - No feedback integrity error detected on slave port 2<br>1b - Feedback integrity error detected on slave port 2|
|27|Data Phase Slave Port Error|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

540 / 4640 

NXP Semiconductors 

Crossbar Integrity Checker (XBIC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|DPSE3|0b - No feedback integrity error detected on slave port 3<br>1b - Feedback integrity error detected on slave port 3|
|26|Data Phase Slave Port Error|
|DPSE4|0b - No feedback integrity error detected on slave port 4<br>1b - Feedback integrity error detected on slave port 4|
|25|Data Phase Slave Port Error|
|DPSE5|0b - No feedback integrity error detected on slave port 5<br>1b - Feedback integrity error detected on slave port 5|
|24|Data Phase Slave Port Error|
|DPSE6|0b - No feedback integrity error detected on slave port 6<br>1b - Feedback integrity error detected on slave port 6|
|23|Data Phase Slave Port Error|
|DPSE7|0b - No feedback integrity error detected on slave port 7<br>1b - Feedback integrity error detected on slave port 7|
|22|Data Phase Master Port Error|
|DPME0|0b - No feedback integrity error detected on master port 0<br>1b - Feedback integrity error detected on master port 0|
|21|Data Phase Master Port Error|
|DPME1|0b - No feedback integrity error detected on master port 1<br>1b - Feedback integrity error detected on master port 1|
|20|Data Phase Master Port Error|
|DPME2|0b - No feedback integrity error detected on master port 2<br>1b - Feedback integrity error detected on master port 2|
|19|Data Phase Master Port Error|
|DPME3|0b - No feedback integrity error detected on master port 3<br>1b - Feedback integrity error detected on master port 3|
|18|Data Phase Master Port Error|
|DPME4|0b - No feedback integrity error detected on master port 4<br>1b - Feedback integrity error detected on master port 4|
|17|Data Phase Master Port Error|
|DPME5|0b - No feedback integrity error detected on master port 5|
||1b - Feedback integrity error detected on master port 5|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

541 / 4640 

NXP Semiconductors 

Crossbar Integrity Checker (XBIC) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|16|Data Phase Master Port Error|
|DPME6|0b - No feedback integrity error detected on master port 6<br>1b - Feedback integrity error detected on master port 6|
|15|Data Phase Master Port Error|
|DPME7|0b - No feedback integrity error detected on master port 7<br>1b - Feedback integrity error detected on master port 7|
|14-12<br>SLV|Slave Port<br>Slave port targeted by the most recent transfer with an attribute integrity check error detected.<br>The value in this field is the XBIC slave port number (0–7). See the "Chip-specific XBIC information" section<br>in this document for the mapping of XBIC instances to AXBS instances and XBIC ports to AXBS ports. See<br>the "Chip-specific AXBS information" section in this document for the device component(s) mapped to each<br>port of an AXBS instance.|
|11-8<br>MST|Master ID<br>Master port that requested the most recent transfer with an attribute integrity check error detected.<br>The value in this field is the logical master ID number of the bus master. See the "Chip-specific XBIC<br>information" section in this document for the master IDs and their corresponding components.|
|7-0|Syndrome|
|SYN|Syndrome calculated for the most recent transfer with an attribute integrity check error detected.<br>For single-bit errors, identify the signal in error by matching the SYN value inTable 61, noting that the<br>syndrome (SYN) values in the table are hexadecimal.|



### 17.7.5 XBIC Error Address (EAR) 

#### Offset 

|Register|Offset|
|---|---|
|EAR|Ch|



#### Function 

In this register, XBIC reports the address of the most recent transfer with an attribute integrity check error detected—either because of a hardware fault or error injection. XBIC sets this register to all 0s only on reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

542 / 4640 

NXP Semiconductors 

Crossbar Integrity Checker (XBIC) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/017_Crossbar_Integrity_Checker_-XBIC-/S32K3XXRM_数据表.pdf-0543-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R ADDR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R ADDR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-0|Error Address|
|ADDR|Address of the most recent transfer with an attribute integrity check error detected.|



## 17.8 Glossary 

EDC Error Detection Code 

hdecor[31:0] Non-standard AHB address phase signal for transporting optional decorated storage instruction information hdecorated Non-standard AHB address phase signal for transporting optional decorated storage instruction information 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

543 / 4640 

