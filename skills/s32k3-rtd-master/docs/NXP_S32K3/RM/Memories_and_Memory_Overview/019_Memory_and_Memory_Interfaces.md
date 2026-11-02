NXP Semiconductors 

# Chapter 19 Memory and Memory Interfaces 

## 19.1 Introduction 

This chapter discusses the configuration of memories and memory interfaces, such as flash memory, flash memory controller, and SRAM. 

## 19.2 Flash memory controller and flash memory modules 

For information on this, see the following chapters: 

- Flash Memory Controller (PFLASH) 

- Embedded Flash Memory 

## 19.3 Related information 

Table 87. Related information 

|Topic|Related chapters|For additional information|
|---|---|---|
|System memory map|Memory Map|See the memory map file attached to this document.|
|Clocking|• Clocking Overview|—|
||• Clock Generation Module (MC_CGM)||
|Arm Cortex-M7 core|Cortex-M7 Overview||
|XRDC|Extended Resource Domain Controller||
|Direct-memory access|• Direct Memory Access Multiplexer<br>(DMAMUX)|See the DMAMUX map file attached to<br>this document.|
||• Enhanced Direct Memory Access<br>(eDMA)||
|EIM|Error Injection Module|—|
|ERM|Error Reporting Module|—|



## 19.4 SRAM access 

In case a master accesses an SRAM with multi-bit ECC errors, the chip may respond as follows: 

- Map all such faults to FCCU. The recommended reaction for the fault is to generate the functional reset. 

- Map such faults to ERM. If the ERM interrupt is enabled, ERM generates an interrupt. 

## 19.5 Memories 

The following table provides information on the types of memories, with their associated configurations, available in S32K3xx family. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

625 / 4640 

NXP Semiconductors 

Memory and Memory Interfaces 

Table 88. Memory configuration 

|Memory|Size|Configuration<br>(words × bits)|ECC or parity|ECC or<br>parity<br>width|Diagnostic<br>information or<br>error report|Applicability|
|---|---|---|---|---|---|---|
|SRAM0|160 KB|32 KB with<br>STANDBY mode retention<br>(4096 × (64 + 8))|ECC (SECDED)|8|ERM|S32K314<br>S32K324|
|||128 KB (16384 × (64 + 8))||||S32K344|
||64 KB|32 KB with<br>STANDBY mode retention<br>(4096 × (64 + 8))|ECC (SECDED)|8|ERM|S32K342<br>S32K322|
|||32 KB (4096 × (64 + 8))|||||
||96 KB|32 KB with<br>STANDBY mode retention<br>(4096 × (64 + 8))|ECC (SECDED)|8|ERM|S32K312|
|||64 KB (8192 × (64 + 8))|||||
||32 KB|32 KB with<br>STANDBY mode retention<br>(4096 × (64 + 8))|ECC (SECDED)|8|ERM|S32K311|
||256 KB|64 KB with standby mode<br>retension (8192 x (64 +8))|ECC (SECDED)|8|ERM|S32K358|
|||128 KB (16384 x (64+8))|||||
|||64 KB (8192 x (64 +8))|||||
|SRAM1|160 KB|32 KB (4096 × (64 + 8))|ECC (SECDED)|8|ERM|S32K314|
|||128 KB (16384 × (64 + 8))||||S32K324<br>S32K344|
||256 KB|128 KB (16384 x (64+8))|ECC (SECDED)|8|ERM|S32K358|
|||128 KB (16384 x (64+8))|||||
|SRAM_2|256 KB|64 KB (8192 x (64 +8))|ECC (SECDED)|8|ERM|S32K358|
|||128 KB (16384 x (64+8))|||||
|||64KB (8192 x (64 +8))|||||
|CM7_1 I-cache|8 KB|4 KB (512 × (64 + 8))|ECC (SECDED)|8|ERM|S32K324|
|data||4 KB (512 × (64 + 8))||||S32K322|
|CM7_1 I-cache|672 bytes|336 bytes (128 × (21 + 7))|ECC (SECDED)|7|ERM||
|tag||336 bytes (128 × (21 + 7))|||||
|CM7_1 D-cache|8 KB|1 KB (256 × (32 + 7))|ECC (SECDED)|7|ERM||
|data||1 KB (256 × (32 + 7))<br>1 KB (256 × (32 + 7))|||||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

626 / 4640 

NXP Semiconductors 

Memory and Memory Interfaces 

Table 88. Memory configuration (continued) 

|Memory|Size|Configuration<br>(words × bits)|ECC or parity|ECC or<br>parity<br>width|Diagnostic<br>information or<br>error report|Applicability|
|---|---|---|---|---|---|---|
|||1 KB (256 × (32 + 7))|||||
|||1 KB (256 × (32 + 7))|||||
|||1 KB (256 × (32 + 7))|||||
|||1 KB (256 × (32 + 7))|||||
|||1 KB (256 × (32 + 7))|||||
|CM7_1 D-cache<br>|800 bytes|200 bytes (64 × (25 + 7))|ECC (SECDED)|7|ERM||
|tag||200 bytes (64 × (25 + 7))|||||
|||200 bytes (64 × (25 + 7))|||||
|||200 bytes (64 × (25 + 7))|||||
|CM7_0 I-cache<br>|8 KB|4 KB (512 × (64 + 8))|ECC (SECDED)|8|ERM|S32K314|
|data||4 KB (512 × (64 + 8))||||S32K324|
|CM7_0 I-cache<br>|672 bytes|336 bytes (128 × (21 + 7))|ECC (SECDED)|7|ERM|S32K344|
|tag||336 bytes (128 × (21 + 7))||||S32K312|
|CM7_0 D-cache<br>|8 KB|1 KB (256 × (32 + 7))|ECC (SECDED)|7|ERM|S32K342|
|data||1 KB (256 × (32 + 7))||||S32K311|
|||1 KB (256 × (32 + 7))||||S32K322|
|||1 KB (256 × (32 + 7))|||||
|||1 KB (256 × (32 + 7))|||||
|||1 KB (256 × (32 + 7))|||||
|||1 KB (256 × (32 + 7))|||||
|||1 KB (256 × (32 + 7))|||||
|CM7_0 D-cache<br>|800 bytes|200 bytes (64 × (25 + 7))|ECC (SECDED)|7|ERM||
|tag||200 bytes (64 × (25 + 7))|||||
|||200 bytes (64 × (25 + 7))|||||
|||200 bytes (64 × (25 + 7))|||||
|CM7_0 I-|8 KB|4 KB (1024 x (64 + 8))|ECC (SECDED)|8|ERM|S32K358|
|cache data||4 KB (1024 x (64 + 8))|||||
|CM7_1 I-<br>cache data|||||||
|CM7_2 I-<br>cache data|||||||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

627 / 4640 

NXP Semiconductors 

Memory and Memory Interfaces 

Table 88. Memory configuration (continued) 

|Memory|Size|Configuration<br>(words × bits)|ECC or parity|ECC or<br>parity<br>width|Diagnostic<br>information or<br>error report|Applicability|
|---|---|---|---|---|---|---|
|CM7_0 I-cache tag|1280<br>bt|640 bytes (256 x (20 + 7))|ECC (SECDED)|7|ERM|S32K358|
|CM7_1 I-cache tag<br>CM7_2 I-cache tag|yes|640 bytes (256 x (20 + 7))|||||
|CM7_0 D-<br>cache data|16 KB|2048 bytes (512 x (32 x 7))<br>2048 bytes (512 x (32 x 7))|ECC (SECDED)|7|ERM|S32K358|
|CM7_1 D-<br>cache data||2048 bytes (512 x (32 x 7))|||||
|CM7_2 D-||2048 bytes (512 x (32 x 7))|||||
|cache data||2048 bytes (512 x (32 x 7))<br>2048 bytes (512 x (32 x 7))<br>2048 bytes (512 x (32 x 7))<br>2048 bytes (512 x (32 x 7))|||||
|CM7_1 D-<br>cache tag|1536<br>bytes|384 bytes (128 x (24 x 7))<br>384 bytes (128 x (24 x 7))<br>384 bytes (128 x (24 x 7))<br>384 bytes (128 x (24 x 7))|ECC (SECDED)|7|ERM|S32K358|
|DMA TCD|1 KB|1 KB (128 × (64 + 8))|ECC (SECDED)|8|ERM|S32K314<br>S32K324<br>S32K344<br>S32K342<br>S32K322|
||640 bytes|640 bytes (80 × (64 + 8))|ECC (SECDED)|8|ERM|S32K312<br>S32K311|
|FlexCAN_0|5 KB|5 KB (640 × (64 + 40))|ECC (SECDED)|40|FlexCAN_0|S32K314|
|FlexCAN_1|1920<br>bytes|1920 bytes<br>(240 × (64 + 40))|ECC (SECDED)|40|FlexCAN_1|S32K324<br>S32K344|
|FlexCAN_2|1920<br>bytes|1920 bytes<br>(240 × (64 + 40))|ECC (SECDED)|40|FlexCAN_2|S32K312<br>S32K342<br>S32K311<br>S32K322|
|FlexCAN_3|1152<br>bytes|1152 bytes<br>(144 × (64 + 40))|ECC (SECDED)|40|FlexCAN_3|S32K314<br>S32K324|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

628 / 4640 

NXP Semiconductors 

Memory and Memory Interfaces 

Table 88. Memory configuration (continued) 

|Memory|Size|Configuration<br>(words × bits)|ECC or parity|ECC or<br>parity<br>width|Diagnostic<br>information or<br>error report|Applicability|
|---|---|---|---|---|---|---|
|||||||S32K344<br>S32K312<br>S32K342<br>S32K322|
|FlexCAN_4|1152<br>bytes|1152 bytes<br>(144 × (64 + 40))|ECC(SECDED)|40|FlexCAN_4|S32K314<br>S32K324|
|FlexCAN_5|1152<br>bytes|1152 bytes<br>(144 × (64 + 40))|ECC (SECDED)|40|FlexCAN_5|S32K344<br>S32K312|
|FlexCAN_1|5120<br>bytes|1920 bytes (640 x (64 +<br>40))|ECC (SECDED)|40|ERM|S32K358|
|FlexCAN_2|5120<br>bytes|1920 bytes (640 x (64 +<br>40))|ECC (SECDED)|40|ERM|S32K358|
|FlexCAN_3|5120<br>bytes|1920 bytes (640 x (64 +<br>40))|ECC (SECDED)|40|ERM|S32K358|
|FlexCAN_4|5120<br>bytes|1920 bytes (640 x (64 +<br>40))|ECC (SECDED)|40|ERM|S32K358|
|FlexCAN_5|5120<br>bytes|1920 bytes (640 x (64 +<br>40))|ECC (SECDED)|40|ERM|S32K358|
|FlexCAN_6|5120<br>bytes|1920 bytes (640 x (64 +<br>40))|ECC (SECDED)|40|ERM|S32K358|
|FlexCAN_7|5120<br>bytes|1920 bytes (640 x (64 +<br>40))|ECC (SECDED)|40|ERM|S32K358|
|QuadSPI RAM|1 KB|1KB (128x64)|No|0|Not applicable|S32K358|
|GMAC_TX|17408<br>bytes|8704 bytes (1024 x (68 +<br>8))|ECC (SECDED)|8|GMAC|S32K358|
|||8704 bytes (1024 x (68 +<br>8))|||||
|GMAC_RX|17408<br>bytes|8704 bytes (1024 x (68 +<br>8))|ECC (SECDED)|8|GMAC|S32K358|
|||8704 bytes (1024 x (68 +<br>8))|||||
|GMAC TSN|1728<br>bytes|1728 bytes (512 x (27 x7))|ECC (SECDED)|7|GMAC|S32K358|
|GMAC<br>RXPARSER|960 bytes|960 Bytes (80 x (96 x 80)|ECC (SECDED)|8|GMAC|S32K358|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

629 / 4640 

NXP Semiconductors 

Memory and Memory Interfaces 

Table 88. Memory configuration (continued) 

|Memory|Size|Configuration<br>(words × bits)|ECC or parity|ECC or<br>parity<br>width|Diagnostic<br>information or<br>error report|Applicability|
|---|---|---|---|---|---|---|
|QuadSPI RAM|1 KB|1 KB (128×64)|No|0|Not applicable|S32K314|
|EMAC TX|8960<br>bytes|4480 bytes<br>(1024 × (35 + 7))|ECC (SECDED)|7|EMAC|S32K324<br>S32K344|
|||4480 bytes<br>(1024 × (35 + 7))||||S32K342<br>|
|EMAC RX|8960<br>bytes|4480 bytes<br>(1024 × (35 + 7))|ECC (SECDED)|7|EMAC|S32K322|
|||4480 bytes<br>(1024 × (35 + 7))|||||
|EMACTSN|1664<br>bytes|1664 bytes (512 × (26 + 7))|ECC (SECDED)|7|EMAC||
|EMAC<br>RXPARSER|960 bytes|960 bytes (80 × (96 + 8))|ECC (SECDED)|8|EMAC||
|QuadSPI TX|320 bytes|320 bytes (80×32)|No|0|Not applicable||
|QuadSPI TX|1152<br>bytes|1152 bytes (256 x (36 + 0))|No|0|Not applicable|S32K358|
|Cortex-M7 cluster<br>ETF ETMI|1 KB|1 KB (128×64)|No|0|Not applicable|S32K314<br>S32K324|
|Cortex-M7 cluster<br>ETFETMD|2 KB|2 KB (128×128)|No|0|Not applicable|S32K344<br>|
|HTM ETF|1 KB|1 KB (128×64)|No|0|Not applicable|S32K312<br>|
|Shared system<br>ETF|2 KB|2 KB (256×64)|No|0|Not applicable|S32K342<br>S32K311|
|HSE secure RAM|64 KB|64 KB (8192 × (64 + 8))|ECC (SECDED)|8|HSE|S32K322|
|HSEPKC|8 KB|4 KB (512 × (64 + 8))|ECC (SECDED)|8|HSE||
|||4 KB (512 × (64 + 8))|||||
|HSEMTB|1 KB|1 KB (256×32)|No|0|HSE||
|Cortex-M7 cluster<br>ETF ETMI|2 KB|2 KB (256 x 64)|No|0|Not applicable|S32K358|
|Cortex-M7 cluster<br>ETF ETMD|1 KB|1 KB (128 x 128)|No|0|Not applicable|S32K358|
|HTM ETF|512 bytes|512 bytes (128 x 64)|No|0|Not applicable|S32K358|
|Shared System<br>ETF|4 KB|4 KB (512 x 64)|No|0|Not applicable|S32K358|
|HSE secure RAM|64 KB|64 KB (8192 x (64 + 8))|ECC (SECDED)|8|HSE|S32K358|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

630 / 4640 

NXP Semiconductors 

Memory and Memory Interfaces 

Table 88. Memory configuration (continued) 

|Memory|Size|Configuration<br>(words × bits)|ECC or parity|ECC or<br>parity<br>width|Diagnostic<br>information or<br>error report|Applicability|
|---|---|---|---|---|---|---|
|HSE PKC|64 KB|32 KB (512 x (64 + 8))|ECC (SECDED)|8|HSE|S32K358|
|||32 KB (512 x (64 + 8))|||||
|HSE MTB|1 KB|1KB (256 x 32)|No|0|Not applicable|S32K358|
|CM7_0ITCM|32 KB|32 KB (4096 × (64 + 8))|ECC (SECDED)|8|ERM|S32K314|
|CM7_0_DTCM|64 KB|32 KB (8192 × (32 + 8))|ECC (SECDED)|8|ERM|S32K324|
|||32 KB (8192 × (32 + 8))||||S32K322<br>S32K312<br>S32K311|
|CM7_1 ITCM|32 KB|32 KB (4096 × (64 + 8))|ECC (SECDED)|8|ERM|S32K324|
|CM7_1_DTCM|64 KB|32 KB (8192 × (32 + 8))|ECC (SECDED)|8|ERM|S32K322|
|||32 KB (8192 × (32 + 8))|||||
|CM7_0_ITCM|64 KB|32 KB (4096 × (64 + 8))|ECC (SECDED)|8|ERM|S32K344|
|||32 KB (4096 × (64 + 8))||||S32K342|
|CM7_0_DTCM|128 KB|32 KB (8192 × (32 + 8))|ECC (SECDED)|8|ERM||
|||32 KB (8192 × (32 + 8))|||||
|||32 KB (8192 × (32 + 8))|||||
|||32 KB (8192 × (32 + 8))|||||
|CM7_2 ITCM|64 KB|64 KB (8192 x (64 + 8))|ECC (SECDED)|8|ERM|S32K358|
|CM7_2 DTCM|128 KB|64 KB (16384 x (32 + 8))|ECC (SECDED)|8|ERM||
|||64 KB (16384 x (32 + 8))|||||



## 19.6 Recommendations for ARM memories 

As per ARM M-7 Safety manual, following considerations must be ensured for proper operation of ARM memories: 

- ITCM and DTCM must be properly initialized with correct ECC before any read operation to avoid any code runaway or software malfucntion or core lockup. 

~~<mark>NOTE</mark>~~ 

ITCM must be initialized with 64-bit writes whereas DTCM can be initialized with 32-bit writes also. 

- To safely disable TCM: 

   1. Clear ITCMCR[EN] or DTCMCR[EN] as required. See ARM Cortex-M7 Devices Generic User Guide for details on ITCMCR and DTCMCR register. 

   2. Execute DSB instruction 

   3. Execute ISB instruction 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

631 / 4640 

NXP Semiconductors 

Memory and Memory Interfaces 

~~<mark>NOTE</mark>~~ 

Care must be taken if disabling the ITCM while executing from it. In this case, software must ensure that the switch-off code is stored in the L2 code memory region from where execution continues when the ITCM is disabled. 

- To safely disable the I-cache: 

   1. Clear CCR[IC]. See ARM Cortex-M7 Devices Generic User Guide for details on CCR register. 

   2. Execute DSB instruction 

   3. Execute ISB instruction 

- To safely disable the D-cache: 

   1. Clean and invalidate non-WT locations in D-cache 

   2. Clear CCR[DC] 

   3. Execute DSB instruction 

See Table 89 for details on memory ECC initialization. 

## 19.7 Memory ECC initialization summary 

The table below summarizes memory ECC initialization. 

Table 89. Memory ECC initialization summary 

|Memory|Write access size|Masters|||
|---|---|---|---|---|
|||CM7_ n|CM7_ m|eDMA|
|SRAM|64-bits only|System|System|System|
|CM7_n ITCM|64-bits only|Direct or Backdoor|Backdoor|Not possible|
|CM7_n DTCM|32-bits or 64-bits|Direct or Backdoor|Backdoor|Backdoor|
|CM7_m ITCM|64-bits only|Backdoor|Direct or Backdoor|Not possible|
|CM7_m DTCM|32-bits or 64-bits|Backdoor|Direct or Backdoor|Backdoor|



## 19.8 Glossary 

DTCM Data tightly coupled memory ECC Error code correction ETF Embedded trace FIFO ETMD Embedded trace macrocell-data ETMI Embedded trace macrocell-instruction ITCM Instruction tightly coupled memory MTB Macrocell trace buffer PKC Public key cryptography RXPARSER Receive parser memory SECDED Single error correction double error detection SRAM Static random access memory TSN Time sensitive network 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

632 / 4640 

