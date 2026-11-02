NXP Semiconductors 

# Chapter 21 Flash Memory Controller (PFLASH) 

## 21.1 Chip-specific PFLASH information 

### 21.1.1 Flash memory architecture 

The flash memory on the chip consists of a flash memory controller and a flash memory array module. The flash memory controller provides flash–memory configuration and control functions and manages the interface between the flash memory array and the chip's crossbar switch. 

This chip implements three 64-bit AHB buses. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/021_Flash_Memory_Controller_-PFLASH-/S32K3XXRM_数据表.pdf-0707-06.png)


<!-- Start of picture text -->
Port 0 Port 1 Port 2*<br>All other<br>Core 0 Core 1<br>masters<br>256 + 32 bit 256 + 32 bit 256 + 32 bit<br>buffer buffer buffer<br>256 + 32 bit 256 + 32 bit 256 + 32 bit<br>buffer buffer buffer<br>256 + 32 bit 256 + 32 bit 256 + 32 bit<br>buffer buffer buffer<br>256 + 32 bit 256 + 32 bit 256 + 32 bit<br>buffer buffer buffer<br>Flash memory array<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/021_Flash_Memory_Controller_-PFLASH-/S32K3XXRM_数据表.pdf-0707-07.png)


<!-- Start of picture text -->
* This port does not exist on S32K311 and S32K312.<br><!-- End of picture text -->

Figure 46. Flash memory architecture 

### 21.1.2 Flash memory controller 

The flash memory controller: 

- Acts as an interface between the system bus and flash memory array. 

- Is a triple-ported controller with a dedicated line buffering per port and per master ID. This enables you to use the line buffers more efficiently because various masters have dedicated buffers that are not compromised when other masters perform read operations. 

Also, by having separate ports, you can have separate connections for each CPU instruction bus and a single port for all data accesses as shown in Figure 46. 

In general, the flash memory controller registers affect the global flash memory behavior (for example, read buffering and access control). 

~~<mark>NOTE</mark>~~ 

In S32K312: 

- PFLASH block 3 and block 4 are not present, so both the sector and super sector registers are not available. 

- For PFLASH block 2, the super sector registers are not available. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

707 / 4640 

NXP Semiconductors 

Flash Memory Controller (PFLASH) 

### 21.1.3 Platform flash configuration registers (PFCRn) 

The table below defines the PFCRn fields that the chip uses. 

Table 96. Platform flash configuration registers (PFCRn) 

|Master|Buffer enable field|Prefetch enable field|
|---|---|---|
|Cortex–M7_0|P0_CBFEN, P0_DBFEN|P0_CPFEN, P0_DPFEN|
|eDMA + HSE_B + EMAC<sup>1</sup>|P1_CBFEN, P1_DBFEN|P1_CPFEN, P1_DPFEN|
|Cortex–M7_1|P2_CBFEN, P2_DBFEN|P2_CPFEN, P2_DPFEN|
|Cortex–M7_2|P3_CBFEN, P3_DBFEN|P3_CPFEN, P3_DPFEN|



1. S32K311 and S32K312 do not support EMAC. 

### 21.1.4 Platform flash access protection register (PFAPR) 

This table defines the PFAPR[MnAP] fields that the chip uses. This chip does not use the other master access protection fields, but those fields are readable and writable. 

Table 97. Platform flash access protection register (PFAPR) 

|Master number|Master name|Access protection field|
|---|---|---|
|0|Cortex–M7_0 AHBM|M0AP|
|1|eDMA/ STAM|M1AP|
|2|HSE_B|M2AP|
|3|EMAC|M3AP|
|4|Cortex–M7_1 AHBM|M4AP|
|5|Cortex–M7_2 AHBM|M5AP|
|6|uSDHC|M6AP|



## 21.2 Introduction 

PFLASH acts as an interface between the system bus (AHB-Lite 2.v6) and flash memory array. 

PFLASH supports three 64-bit AHB buses and a 256-bit read data interface from each flash memory array. The slave port assignments and buffer organization are organized to offer maximum performance of code execution in a multicore architecture. The buffer mechanism serves to deliver flash memory read data with zero-wait state response on lines that reside in cache. AHB requests that miss the prefetch cache generate the needed flash memory array access and are forwarded to the AHB upon completion. Each cache entry is 256 bits, matching the flash memory array page size and providing 512 bytes of high-speed local storage. 

## 21.3 Features 

- Four 64-bit AHB interface ports (p0, p1, p2, p3) allowing simultaneous access to dedicated prefetch mini-cache per slave port 

- 256-bit read data bus and 64-bit write data bus 

- Configurable read buffering and line prefetching support via a mini-cache, plus a prefetch controller for each AHB port to provide single-cycle buffer hit read response 

- Configurable access control based on read/write and AHB master ID attributes 

- Support for reporting single-bit and multi-bit flash memory ECC events on a 64-bit doubleword boundary 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

708 / 4640 

NXP Semiconductors 

Flash Memory Controller (PFLASH) 

## 21.4 Block diagrams 

The following figure provides a block diagram showing PFLASH and the attached flash memory array. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/021_Flash_Memory_Controller_-PFLASH-/S32K3XXRM_数据表.pdf-0709-04.png)


<!-- Start of picture text -->
Arm Cortex-M<br>processor<br>Flash<br>PFLASH<br>memory<br>AMBA-AHB AXBS<br>System<br>RAM Memory<br><!-- End of picture text -->

Figure 47. Platform-centric simple block diagram with PFLASH 

## 21.5 Functional description 

As shown in Figure 47, PFLASH interfaces between: 

- The AHB system bus port 

- The flash memory array 

For accesses targeting flash memory, the PFLASH generates as inputs to the flash memory array: 

- Read and write enables 

- Block selects 

- Array address 

- Write size 

- Write data 

PFLASH captures read data from the flash memory array and drives it onto the AHB system bus. Up to four pages of data (256-bit page size) may be buffered in each prefetch buffer for AHB Port0, Port1, and Port2. and Port 3. Lines may be prefetched in advance of being requested, allowing single-cycle (zero AHB wait-states) read data responses on buffer hits. 

Access protections may be applied on a per-master basis for both reads and writes to support security and privilege mechanisms. 

### 21.5.1 Read transactions 

On an incoming AHB read request, a mini-cache lookup and access privilege evaluation are performed during the AHB address phase. If a buffer hit occurs, the requested data is retrieved from the previously loaded prefetch buffer entry and returned on the system bus with a zero wait-state response. If a buffer miss occurs, a flash memory access is initiated. 

Read accesses are terminated under control of the appropriate wait state settings. Access timing can be varied to account for the operating conditions of the chip (for example, frequency, voltage, temperature, and so on) by appropriately setting the read wait state field in flash memory. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

709 / 4640 

NXP Semiconductors 

Flash Memory Controller (PFLASH) 

### 21.5.2 Write transactions 

An interlock write on a program or erase sequence is initiated by first writing to Platform Flash Memory Program Erase Address Logical (PFCPGM_PEADR_L), Platform Flash Memory Express Program Erase Address Logical (PFCPGM_XPEADR_L)(see the Flash Memory chapter for write sequence details). 

### 21.5.3 Access protections 

#### 21.5.3.1 PFAPR 

PFLASH provides programmable, configurable access protections for read cycles on a per-master basis in PFAPR[MnAP]. This field restricts read access on a per-master basis. This functionality is described in Platform Flash Memory Access Protection (PFAPR). Detection of a protection violation based on PFAPR settings results in an error response from PFLASH on the AHB transfer. 

### 21.5.4 Error termination 

PFLASH can invoke a system bus error termination in the following scenarios: 

- Access privilege violation (see Access protections for details) 

- Attempted access by an AHB master to a reserved region in the flash memory map 

- Multi-bit ECC error detection on AHB read, and PFCR4[DMEEE] = 0 (for data flash memory, it is further qualified by PFCR4[DERR_SUP] = 0) 

### 21.5.5 Line read buffers and prefetch operation 

The PFLASH AHB ports of the a mini-cache. PFLASH uses the buffers for both prefetch and normal demand fetches. Also, the buffers are shared for code and data fetches, and can be controlled independently for code and data from control registers. 

Prefetch triggering is controllable on a per-port basis. A PFLASH read access may trigger a prefetch to the next sequential line of array data on the cycle following the request. The access address is incremented by 32 bytes, and a subsequent flash memory access is initiated. A flash memory array prefetch is initiated if the data is not already resident in a line read buffer. Prefetched data is always loaded into the least-recently-used buffer. 

For Port0, Port1, and Port2 there are four line buffer entries in their respective prefetch mini-caches that follow a fully associative, least-recently-used replacement policy. Port 3 configuration is the same as other ports. 

For prefetching to occur, you must set the following configuration fields, where n corresponds to the port number and m corresponds to C (code) or D (data): 

PFCRn[Pn_mBFEN] = 1 and PFCRn[Pn_mPFEN] = 1 

### 21.5.6 Array integrity considerations 

During an array integrity sequence, the flash memory array ignores any incoming read requests. When a flash memory array integrity check is in progress, PFLASH terminates all flash memory access requests with an error. More specifically, it aborts the incoming flash memory access requests and terminates the system bus transfer with an error. 

### 21.5.7 Safety considerations 

#### 21.5.7.1 Flash memory address generation check 

Functional safety coverage of the address path and control within PFLASH rely on a feedback path between PFLASH and flash memory. Remember that on a requested access to flash memory, PFLASH must decode the system AHB bus signals to generate the corresponding flash memory interface signals to invoke a flash memory lookup. In addition to providing the requested read data, the flash memory also provides output sidebands reflecting the encoded address and block selects used to perform the actual row lookup. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

710 / 4640 

NXP Semiconductors 

Flash Memory Controller (PFLASH) 

PFLASH uses this sideband information to verify the expected transaction. If a mismatch is detected, indicating a failure in the address generation or control logic within PFLASH or the transmission path between PFLASH and the flash memory array, then the event is forwarded to the chip fault collection module and the corresponding buffer is invalidated. 

### 21.5.8 ECC error handling on data flash block 

When PFCR4[DERR_SUP] is enabled, ECC errors on data flash blocks are handled specially. 

If there is a noncorrectable error detection, a fixed, illegal opcode value is returned to the requesting master along with the associated ECC checkbits as determined by the requesting address. 

For noncorrectable error detection, PFLASH returns a value of 1555_1555h to the requesting master. 

This is mainly used for EEPROM emulation applications. 

### 21.5.9 Read cycles—buffer miss 

On an incoming AHB read request, a mini-cache lookup and access privilege evaluation are performed during the AHB address phase. If a buffer miss occurs, a flash memory access is initiated. 

If the flash memory access was the direct result of an AHB transaction, the corresponding page buffer is loaded and marked as the most-recently-used. If the flash memory access was the result of a speculative prefetch to the next sequential line, it is loaded into the least-recently-used buffer. The status of this buffer is not changed to most-recently-used until a subsequent buffer hit occurs as a result of an AHB read request. 

### 21.5.10 Read cycles—buffer hit 

PFLASH allows single-cycle read responses to the AHB when the requested read access was previously loaded into one of the page buffers. In these cases of a buffer hit, read data is returned on the system bus with a zero wait-state response. 

### 21.5.11 Flash memory error response operation 

The flash memory array may signal an error response to terminate a requested access because of improper sequencing during program/erase operations and improper sequencing during array integrity testing. When an error response is received, PFLASH does not update or validate a page read buffer. An error response may be signaled on a read or interlock write operation. For more information on the specifics related to signaling of flash memory errors, including flash memory ECC events, array integrity testing, and read-while-write events, see the flash memory chapter. 

## 21.6 PFLASH register descriptions 

PFLASH provides an IPS programming model mapped to a standard 16 KB on-platform peripheral slot. The programming model consists of flash memory access configuration. 

You can reference the programming model only by using a 32-bit (word) access. References that are attempted using different access sizes, or to undefined (reserved) addresses, or in User mode generate an IPS error termination. PFLASH allows access to the programming model by all system bus masters. 

Write to read only registers don't generate error termination. 

You can only access the programming model in Supervisor mode, except *PEADR* registers which can be accessed in Supervisor or User mode. 

Attempted updates to the programming model when PFLASH is in the middle of an operation results in non-deterministic behavior. You must architect software to avoid this scenario. The recommended flow for multicore devices is: 

1. Start only one core. 

2. Execute initialization code until it is complete. 

3. Start the remaining cores. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

711 / 4640 

NXP Semiconductors 

Flash Memory Controller (PFLASH) 

If you need to reconfigure the flash memory, code execution must be temporarily moved to system RAM. 

### 21.6.1 PFLASH memory map 

PFLASH base address: 4026_8000h 

PFLASH_ALT base address: 4026_C000h 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|0h|Platform Flash Memory Configuration 0 (PFCR0)|32|RW|0000_0003h|
|4h|Platform Flash Memory Configuration 1 (PFCR1)|32|RW|0000_0003h|
|8h|Platform Flash Memory Configuration 2 (PFCR2)|32|RW|0000_0003h|
|Ch|Platform Flash Memory Configuration 3 (PFCR3)|32|RW|0000_0003h|
|10h|Platform Flash Memory Configuration 4 (PFCR4)|32|RW|0000_0000h|
|14h|Platform Flash Memory Access Protection (PFAPR)|32|RW|FFFF_FFFFh|
|300h|Platform Flash Memory Program Erase Address Logical<br>(PFCPGM_PEADR_L)|32|RW|0000_0000h|
|304h|Platform Flash Memory Program Erase Address Physical<br>(PFCPGM_PEADR_P)|32|RO|0000_0000h|
|308h|Platform Flash Memory Express Program Erase Address Logical<br>(PFCPGM_XPEADR_L)|32|RW|0000_0000h|
|30Ch|Platform Flash Memory Express Program Erase Address Physical<br>(PFCPGM_XPEADR_P)|32|RO|0000_0000h|
|340h - 350h|Block n Sector Program Erase Lock (PFCBLK0_SPELOCK -<br>PFCBLK4_SPELOCK)|32|RW|FFFF_FFFFh|
|358h|Block UTEST Sector Program Erase Lock (PFCBLKU_SPELOCK)|32|RW|0000_0001h|
|35Ch - 368h|Block n Super Sector Program Erase Lock (PFCBLK0_SSPELOCK -<br>PFCBLK3_SSPELOCK)|32|RW|0FFF_FFFFh|
|380h - 390h|Block n Set Sector Lock (PFCBLK0_SETSLOCK -<br>PFCBLK4_SETSLOCK)|32|RW|0000_0000h|
|398h|Block UTEST Set Sector Lock (PFCBLKU_SETSLOCK)|32|RW|0000_0000h|
|39Ch - 3A8h|Block n Set Super Sector Lock (PFCBLK0_SSETSLOCK -<br>PFCBLK3_SSETSLOCK)|32|RW|0000_0000h|
|3C0h - 45Ch|Block a Lock Master Sector b (PFCBLK0_LOCKMASTER_S0 -<br>PFCBLK4_LOCKMASTER_S7)|32|RO|FFFF_FFFFh|
|480h|Block UTEST Lock Master Sector (PFCBLKU_LOCKMASTER_S)|32|RO|0000_00FFh|
|484h - 4F0h|Block m Lock Master Super Sector n<br>(PFCBLK0_LOCKMASTER_SS0 - PFCBLK3_LOCKMASTER_SS6)|32|RO|FFFF_FFFFh|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

712 / 4640 

NXP Semiconductors 

Flash Memory Controller (PFLASH) 

### 21.6.2 Platform Flash Memory Configuration 0 (PFCR0) 

##### Offset 

|Register|Offset|
|---|---|
|PFCR0|0h|



##### Function 

##### Specifies the operation of PFLASH Port0. 

See the chip-specific PFLASH information for details about the actual masters available on the chip. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/021_Flash_Memory_Controller_-PFLASH-/S32K3XXRM_数据表.pdf-0713-09.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>P0_DP P0_CP P0_DB P0_CB<br>FEN  FEN  FEN  FEN<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-6|Reserved|
|—||
|5|Port0 Data Prefetch Enable|
|P0_DPFEN|Enables or disables data prefetching initiated by a read access on Port0. Prefetching can only be<br>enabled if the buffers are enabled by writing 1 toDBFEN. Hardware reset returns this field to 0.<br>0b - Disable<br>1b - Enable|
|4|Port0 Code Prefetch Enable|
|P0_CPFEN|Enables or disables code prefetching initiated by a read access on Port0. Prefetching can only be<br>enabled if the buffers are enabled by writing 1 toCBFEN. Hardware reset returns this field to 0.<br>0b - Disable|
||1b - Enable|
|3-2|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

713 / 4640 

NXP Semiconductors 

Flash Memory Controller (PFLASH) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|1|Port0 PFLASH Line Read Data Buffers Enable|
|P0_DBFEN|Enables or disables line read data buffer hits. It is also used to invalidate the buffers.<br>If this field is 0, the line read buffers are disabled from satisfying read requests, and all buffer valid bits are<br>set to 0. If this field is enabled, the line read buffers are enabled to satisfy read requests on hits. Buffer valid<br>bits may be set when the buffers are successfully filled.<br>0b - Disable<br>1b - Enable|
|0|Port0 PFLASH Line Read Code Buffers Enable|
|P0_CBFEN|Enables or disables line read code buffer hits. It is also used to invalidate the buffers.<br>If disabled, the line read buffers are disabled from satisfying read requests, and all buffer valid bits are set<br>to 0. If enabled, the line read buffers are enabled to satisfy read requests on hits. Buffer valid bits may be<br>set when the buffers are successfully filled.<br>0b - Disable<br>1b - Enable|



### 21.6.3 Platform Flash Memory Configuration 1 (PFCR1) 

##### Offset 

|Register|Offset|
|---|---|
|PFCR1|4h|



##### Function 

##### Specifies the operation of PFLASH Port1. 

See the chip-specific PFLASH information for details about the actual masters available on the chip. 

~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

||Instance|Register supported|Register not supported|
|---|---|---|---|
|PFLASH||PFCR1|—|
|PFLASH_ALT||—|PFCR1|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

714 / 4640 

NXP Semiconductors 

Flash Memory Controller (PFLASH) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||0||||||P1_DP|P1_CP|0||P1_DB|P1_CB|
|W|||||||||||FEN|FEN|||FEN|FEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|1|



##### Fields 

|Field|Function|
|---|---|
|31-6|Reserved|
|—<br>5|Port1 Data Prefetch Enable|
|P1_DPFEN|Enables or disables data prefetching initiated by a read access on Port1. Prefetching can only be<br>enabled if the buffers are enabled by writing 1 toDBFEN. Hardware reset returns this field to 0.<br>0b - Disable<br>1b - Enable|
|4|Port1 Code Prefetch Enable|
|P1_CPFEN|Enables or disables code prefetching initiated by a read access on Port1. Prefetching can only be<br>enabled if the buffers are enabled by writing 1 toCBFEN. Hardware reset returns this field to 0.<br>0b - Disable<br>1b - Enable|
|3-2<br>—<br>1<br>P1_DBFEN|Reserved<br>Port1 PFLASH Line Read Data Buffers Enable<br>Enables or disables line read data buffer hits. It is also used to invalidate the buffers.<br>If this field is 0, the line read buffers are disabled from satisfying read requests, and all buffer valid bits are<br>set to 0. If this field is enabled, the line read buffers are enabled to satisfy read requests on hits. Buffer valid<br>bits may be set when the buffers are successfully filled.<br>0b - Disable<br>1b - Enable|
|0|Port1 PFLASH Line Read Code Buffers Enable|
|P1_CBFEN|Enables or disables line read code buffer hits. It is also used to invalidate the buffers.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

715 / 4640 

NXP Semiconductors 

Flash Memory Controller (PFLASH) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||If disabled, the line read buffers are disabled from satisfying read requests, and all buffer valid bits are set<br>to 0. If enabled, the line read buffers are enabled to satisfy read requests on hits. Buffer valid bits may be<br>set when the buffers are successfully filled.|
||0b - Disable|
||1b - Enable|



### 21.6.4 Platform Flash Memory Configuration 2 (PFCR2) 

##### Offset 

|Register|Offset|
|---|---|
|PFCR2|8h|



##### Function 

##### Specifies the operation of PFLASH Port2. 

See the chip-specific PFLASH information for details about the actual masters available on the chip. 

~~<mark>NOTE</mark>~~ Each module instance supports a different number of registers. 

||Instance|Register supported|Register not supported|
|---|---|---|---|
|PFLASH||PFCR2|—|
|PFLASH_ALT||—|PFCR2|



##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/021_Flash_Memory_Controller_-PFLASH-/S32K3XXRM_数据表.pdf-0716-13.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>P2_DP P2_CP P2_DB P2_CB<br>FEN  FEN  FEN  FEN<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

716 / 4640 

NXP Semiconductors 

Flash Memory Controller (PFLASH) 

##### Fields 

|Field|Function|
|---|---|
|31-6<br>—|Reserved|
|5|Port2 Data Prefetch Enable|
|P2_DPFEN|Enables or disables data prefetching initiated by a read access on Port2. Prefetching can only be<br>enabled if the buffers are enabled by writing 1 toDBFEN. Hardware reset returns this field to 0.<br>0b - Disable<br>1b - Enable|
|4|Port2 Code Prefetch Enable|
|P2_CPFEN|Enables or disables code prefetching initiated by a read access on Port2. Prefetching can only be<br>enabled if the buffers are enabled by writing 1 toCBFEN. Hardware reset returns this field to 0.<br>0b - Disable<br>1b - Enable|
|3-2|Reserved|
|—||
|1|Port2 PFLASH Line Read Data Buffers Enable|
|P2_DBFEN|Enables or disables line read data buffer hits. It is also used to invalidate the buffers.<br>If this field is 0, the line read buffers are disabled from satisfying read requests, and all buffer valid bits are<br>set to 0. If this field is enabled, the line read buffers are enabled to satisfy read requests on hits. Buffer valid<br>bits may be set when the buffers are successfully filled.<br>0b - Disable<br>1b - Enable|
|0<br>P2_CBFEN|Port2 PFLASH Line Read Code Buffers Enable<br>Enables or disables line read code buffer hits. It is also used to invalidate the buffers.<br>If disabled, the line read buffers are disabled from satisfying read requests, and all buffer valid bits are set<br>to 0. If enabled, the line read buffers are enabled to satisfy read requests on hits. Buffer valid bits may be<br>set when the buffers are successfully filled.<br>0b - Disable<br>1b - Enable|



### 21.6.5 Platform Flash Memory Configuration 3 (PFCR3) 

##### Offset 

|Register|Offset|
|---|---|
|PFCR3|Ch|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

717 / 4640 

NXP Semiconductors 

Flash Memory Controller (PFLASH) 

##### Function 

##### Specifies the operation of PFLASH Port3. 

See the chip-specific PFLASH information for details about the actual masters available on the chip. 

~~<mark>NOTE</mark>~~ Each module instance supports a different number of registers. 

|||Insta|nce||||Regis|ter sup|ported|||Re|gister n|ot su|pported||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|PFLASH||||||PFCR3|||||—||||||
|PFLASH_|ALT|||||—|||||PFC|R3|||||
|Diagram|||||||||||||||||
|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|R|||||||||0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||0|||||P3_DP|P3_CP|0||P3_DB|P3_CB|
|W|||||||||||FEN|FEN|||FEN|FEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|1|



##### Fields 

|Field|Function|
|---|---|
|31-6|Reserved|
|—||
|5|Port3 Data Prefetch Enable|
|P3_DPFEN|Enables or disables data prefetching initiated by a read access on Port3. Prefetching can only be<br>enabled if the buffers are enabled by writing 1 toDBFEN. Hardware reset returns this field to 0.<br>0b - Disable<br>1b - Enable|
|4|Port3 Code Prefetch Enable|
|P3_CPFEN|Enables or disables code prefetching initiated by a read access on Port3. Prefetching can only be<br>enabled if the buffers are enabled by writing 1 toCBFEN. Hardware reset returns this field to 0.<br>0b - Disable<br>1b - Enable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

718 / 4640 

NXP Semiconductors 

Flash Memory Controller (PFLASH) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|3-2|Reserved|
|—||
|1|Port3 PFLASH Line Read Data Buffers Enable|
|P3_DBFEN|Enables or disables line read data buffer hits. It is also used to invalidate the buffers.<br>If this field is 0, the line read buffers are disabled from satisfying read requests, and all buffer valid bits are<br>set to 0. If this field is enabled, the line read buffers are enabled to satisfy read requests on hits. Buffer valid<br>bits may be set when the buffers are successfully filled.<br>0b - Disable<br>1b - Enable|
|0|Port3 PFLASH Line Read Code Buffers Enable|
|P3_CBFEN|Enables or disables line read code buffer hits. It is also used to invalidate the buffers.<br>If disabled, the line read buffers are disabled from satisfying read requests, and all buffer valid bits are set<br>to 0. If enabled, the line read buffers are enabled to satisfy read requests on hits. Buffer valid bits may be<br>set when the buffers are successfully filled.<br>0b - Disable<br>1b - Enable|



### 21.6.6 Platform Flash Memory Configuration 4 (PFCR4) 

##### Offset 

|Register|Offset|
|---|---|
|PFCR4|10h|



##### Function 

Specifies operation of the flash memory controller buffer. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/021_Flash_Memory_Controller_-PFLASH-/S32K3XXRM_数据表.pdf-0719-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 DMEE 0 DERR<br>BLK4_PS<br>W E  _SUP<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

719 / 4640 

NXP Semiconductors 

Flash Memory Controller (PFLASH) 

##### Fields 

|Field|Function|
|---|---|
|31-8|Reserved|
|—<br>7<br>DMEEE|Disable Multi-Bit ECC Error Exception<br>Enables or disables system bus error response on multi-bit ECC error. Hardware reset returns this field to 0.<br>0b - Error response sent on system bus for multi-bit ECC error<br>1b - Error response not sent on system bus for multi-bit ECC error|
|6-4<br>—<br>3-1<br>BLK4_PS|Reserved<br>Block 4 Pipe Select<br>Selects the active pipe for flash memory block 4 access.<br>PFLASH has four independent command pipes to issue four parallel read commands to different flash<br>memory blocks. Reads from flash memory block 0–3 are always done through command pipe 0–3,<br>respectively. However, the access to block 4 is not fixed and can be through any of the command pipes. You<br>must only change this field when there is no ongoing block 4 access.<br>A special round-robin arbitration scheme snoops the availability of a command pipe during block 4 access.<br>If any of the command pipes are idle during the first read request to block 4, the ownership of that command<br>pipe gets shared between block 4 and the respective block. If none of the command pipes are idle during a<br>block 4 read request, block 4 gets associated with each of the command pipes in round-robin fashion. When<br>a command pipe acquires ownership of block 4, it keeps that ownership until all the commands to block 4<br>from all the masters are served.<br>000b - Block 4 access is always through pipe0<br>001b - Block 4 access is always through pipe1<br>010b - Block 4 access is always through pipe2<br>011b - Block 4 access is always through pipe3<br>1xxb - Block 4 access can be through any of the command pipes, based on which command pipe<br>is available for block 4 access|
|0<br>DERR_SUP|Data Error Suppression<br>See the Embedded Flash Memory configuration information or system memory map for which flash<br>memory blocks are affected by this field.<br>0b - Reports ECC events on data flash memory accesses<br>1b - Single-bit and multi-bit ECC events on data flash memory accesses are suppressed|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

720 / 4640 

NXP Semiconductors 

Flash Memory Controller (PFLASH) 

### 21.6.7 Platform Flash Memory Access Protection (PFAPR) 

##### Offset 

|Register|Offset|
|---|---|
|PFAPR|14h|



##### Function 

Controls read accesses to the flash memory array. 

See the chip-specific PFLASH information for details about the actual masters available on the chip. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/021_Flash_Memory_Controller_-PFLASH-/S32K3XXRM_数据表.pdf-0721-09.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>M0AP  M1AP  M2AP  Reserved  M4AP  M5AP  M6AP  M7AP<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>M8AP  M9AP  M10AP  M11AP  M12AP  M13AP  M14AP  M15AP<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-30: M0AP|Master n Access Protection|
|29-28: M1AP<br>27-26: M2AP|Controls whether read accesses to the flash memory are allowed based on the master ID of a requesting<br>master. These fields are initialized by hardware reset. The location that would be M3AP is a reserved<br>field.|
|25-24: —|x0b - This master cannot perform any read accesses|
|23-22: M4AP|x1b - This master can perform read accesses|
|21-20: M5AP||
|19-18: M6AP||
|17-16: M7AP||
|15-14: M8AP||
|13-12: M9AP||
|11-10: M10AP||
|9-8: M11AP||
|7-6: M12AP||
|5-4: M13AP||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

721 / 4640 

NXP Semiconductors 

Flash Memory Controller (PFLASH) 

|Field|Function|
|---|---|
|3-2: M14AP||
|1-0: M15AP||



### 21.6.8 Platform Flash Memory Program Erase Address Logical (PFCPGM_PEADR_L) 

##### Offset 

|Register|Offset|
|---|---|
|PFCPGM_PEADR_L|300h|



##### Function 

Provides the flash memory address to be programmed, or the location of the sector or block to be erased through main flash memory (pgm/erase) queue. Write access to this register is domain-ID aware. 

The respective bus master must have program/erase permission to the flash memory address written to this register. Otherwise a transfer error results. For further information on flash memory address restrictions see the XRDC chapter. 

A write to this register is managed via three-cycle access. Before updating the register, you must ensure that no ongoing high-voltage operation is executing through the flash memory main queue. 

Unauthorized flash memory address writes result in a transfer error. 

Writes to this register during an ongoing high-voltage operation (initiated through the flash memory main queue) or during express program operation are ignored. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/021_Flash_Memory_Controller_-PFLASH-/S32K3XXRM_数据表.pdf-0722-13.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>PEADR_L<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>PEADR_L<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-0|Program Erase Address Logical|
|PEADR_L|Contains the system logical address for flash memory program/erase.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

722 / 4640 

NXP Semiconductors 

Flash Memory Controller (PFLASH) 

### 21.6.9 Platform Flash Memory Program Erase Address Physical (PFCPGM_PEADR_P) 

##### Offset 

|Register|Offset|
|---|---|
|PFCPGM_PEADR_P|304h|



##### Function 

Reflects the flash memory block number and offset address corresponding to Platform Flash Memory Program Erase Address Logical (PFCPGM_PEADR_L). This register has the same format as the PEADR register in the Flash Memory chapter—see it for details. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/021_Flash_Memory_Controller_-PFLASH-/S32K3XXRM_数据表.pdf-0723-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R PEADR_P<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R PEADR_P<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Program Erase Address Physical|
|PEADR_P|Contains the flash block select and offset address for flash memory program/erase.|



### 21.6.10 Platform Flash Memory Express Program Erase Address Logical (PFCPGM_XPEADR_L) 

##### Offset 

|Register|Offset|
|---|---|
|PFCPGM_XPEADR_L|308h|



##### Function 

Provides the flash memory address to be programmed using the flash memory express program feature. Write access to this register is domain-ID aware. 

The respective bus master must have program/erase permission to the flash memory address written to this register. Otherwise a transfer error results. See the XRDC chapter for further information on flash memory address restrictions. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

723 / 4640 

NXP Semiconductors 

Flash Memory Controller (PFLASH) 

A write to this register is managed via three-cycle access. Before updating the register, you must ensure that no ongoing high-voltage operation is executing through the flash memory main queue. 

Unauthorized flash memory address writes result in a transfer error. 

Writes to this register during an ongoing express program operation are ignored. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/021_Flash_Memory_Controller_-PFLASH-/S32K3XXRM_数据表.pdf-0724-06.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>XPEADR_L<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>XPEADR_L<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-0|Express Program Erase Address Logical|
|XPEADR_L|Contains the system logical address for express flash program/erase.|



### 21.6.11 Platform Flash Memory Express Program Erase Address Physical (PFCPGM_XPEADR_P) 

##### Offset 

|Register|Offset|
|---|---|
|PFCPGM_XPEADR_P|30Ch|



##### Function 

Reflects the flash memory block number and offset address corresponding to PFCPGM_XPEADR_L. This register has the same format as the XPEADR register in the Flash Memory chapter—see it for details. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

724 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/021_Flash_Memory_Controller_-PFLASH-/S32K3XXRM_数据表.pdf-0725-01.png)


<!-- Start of picture text -->
Flash Memory Controller (PFLASH)<br><!-- End of picture text -->

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/021_Flash_Memory_Controller_-PFLASH-/S32K3XXRM_数据表.pdf-0725-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R XPEADR_P<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R XPEADR_P<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Express Program Erase Address Physical|
|XPEADR_P|Contains the flash memory block select and offset address for flash memory express program/erase.|



### 21.6.12 Block n Sector Program Erase Lock (PFCBLK0_SPELOCK - PFCBLK4_SPELOCK) 

##### Offset 

|Register|Offset|
|---|---|
|PFCBLK0_SPELOCK|340h|
|PFCBLK1_SPELOCK|344h|
|PFCBLK2_SPELOCK|348h|
|PFCBLK3_SPELOCK|34Ch|
|PFCBLK4_SPELOCK|350h|



##### Function 

Provides a way to protect sectors from being modified. Sector protection is available on the last 256 KB of every block (for 256 KB blocks, all sectors are available for protection). Each lock bit can be associated with a particular domain ID by writing 1 to the appropriate bit in PFCBLKn_SETSLOCK[SETSLCK]. After the lock is acquired, only a master having the same domain ID can modify the corresponding lock bit. If the corresponding PFCBLKn_SETSLOCK[SETSLCK] bit is not equal to 1, any master can modify the appropriate SLCK bit. If a lock bit is already acquired by a particular domain ID, any effort to modify (1 to 0, or 0 to 1) the lock bit by a master with a different domain ID results in a transfer error. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

725 / 4640 

NXP Semiconductors 

###### Flash Memory Controller (PFLASH) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/021_Flash_Memory_Controller_-PFLASH-/S32K3XXRM_数据表.pdf-0726-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>SLCK<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>SLCK<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Sector Lock|
|SLCK|Locks selected sector. If vector bit value = 0, the sector is available for program and erase operations. If|
||vector bit value = 1, the sector is locked and not available for program and erase operations.|



### 21.6.13 Block UTEST Sector Program Erase Lock (PFCBLKU_SPELOCK) 

##### Offset 

|Register|Offset|
|---|---|
|PFCBLKU_SPELOCK|358h|



##### Function 

Provides a way to protect sectors from being modified. Sector protection is available on the last 256 KB of every block (for 256 KB blocks, all sectors are available for protection). Each lock bit can be associated with a particular domain ID by writing 1 to PFCBLKU_SETSLOCK[SETSLCK]. After the lock is acquired, only a master having the same domain ID can modify the corresponding lock bit. If the corresponding PFCBLKU_SETSLOCK[SETSLCK] bit is not equal to 1, any master can modify the SLCK bit. If a lock bit is already acquired by a particular domain ID, any effort to modify (1 to 0, or 0 to 1) the lock bit by a master with a different domain ID results in a transfer error. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

726 / 4640 

NXP Semiconductors 

Flash Memory Controller (PFLASH) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/021_Flash_Memory_Controller_-PFLASH-/S32K3XXRM_数据表.pdf-0727-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>SLCK<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-1|Reserved|
|—||
|0|Sector Lock|
|SLCK|Locks selected sector. If vector bit value = 0, the sector is available for program and erase operations. If<br>vector bit value = 1, the sector is locked and not available for program and erase operations.|



### 21.6.14 Block n Super Sector Program Erase Lock (PFCBLK0_SSPELOCK - PFCBLK3_SSPELOCK) 

##### Offset 

|Register|Offset|
|---|---|
|PFCBLK0_SSPELOCK|35Ch|
|PFCBLK1_SSPELOCK|360h|
|PFCBLK2_SSPELOCK|364h|
|PFCBLK3_SSPELOCK|368h|



##### Function 

Provides a way to protect super sectors from being modified. Super sector protection is available on block space larger than 256 KB. For 256 KB blocks, this register is not applicable. For 512 KB blocks, the first half of the block is protected with super sector granularity. For 1 MB blocks, the first 768 KB is protected with super sector granularity. Each lock bit can be associated with a particular domain ID by writing 1 to the appropriate bit in PFCBLKn_SSETSLOCK[SSETSLCK]. After the lock is acquired, only a master having the same domain ID can modify the corresponding lock bit. If the corresponding PFCBLKn_SSETSLOCK[SSETSLCK] bit is not equal to 1, any master can modify the SSLCK bit. If a lock bit is already acquired by a particular domain ID, any effort to modify (1 to 0, or 0 to 1) the lock bit by a master with a different domain ID results in a transfer error. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

727 / 4640 

NXP Semiconductors 

Flash Memory Controller (PFLASH) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/021_Flash_Memory_Controller_-PFLASH-/S32K3XXRM_数据表.pdf-0728-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>SSLCK<br>W<br>Reset 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>SSLCK<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-28|Reserved|
|—||
|27-0|Super Sector Lock|
|SSLCK|Locks selected super sector. If vector bit value = 0, the super sector is available for program and<br>erase operations. If vector bit value = 1, the super sector is locked and not available for program and<br>erase operations.|



### 21.6.15 Block n Set Sector Lock (PFCBLK0_SETSLOCK - PFCBLK4_SETSLOCK) 

##### Offset 

|Register|Offset|
|---|---|
|PFCBLK0_SETSLOCK|380h|
|PFCBLK1_SETSLOCK|384h|
|PFCBLK2_SETSLOCK|388h|
|PFCBLK3_SETSLOCK|38Ch|
|PFCBLK4_SETSLOCK|390h|



##### Function 

Provides a mechanism for the masters to gain the ownership of the corresponding PFCBLKn_SPELOCK lock bit based on domain id . After it is equal to 1, the bit is returned to 0 at next reset. If any SETSLOCK bit is not equal to 1, the corresponding LOCK bit can be modified by any master. If a bit is already acquired by a particular domain ID, any effort to modify the lock bit by a master with a different domain ID is ignored without transfer error. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

728 / 4640 

NXP Semiconductors 

###### Flash Memory Controller (PFLASH) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/021_Flash_Memory_Controller_-PFLASH-/S32K3XXRM_数据表.pdf-0729-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>SETSLCK<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>SETSLCK<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|If the vector bit value = 0, the corresponding lock bit is not owned by any master. If the vector bit value = 1,|
|SETSLCK|the lock bit is owned by the masters having the domain ID stored inPFCBLKn_LOCKMASTER_Sm.|



### 21.6.16 Block UTEST Set Sector Lock (PFCBLKU_SETSLOCK) 

##### Offset 

|Register|Offset|
|---|---|
|PFCBLKU_SETSLOCK|398h|



##### Function 

Provides a mechanism for the masters to gain ownership of the corresponding PFCBLKU_SPELOCK lock bit based on domain id. After it is equal to 1, the bit is returned to 0 at next reset. If any SETSLOCK bit is not equal to 1, the corresponding LOCK bit can be modified by any master. If a bit is already acquired by a particular domain ID, any effort to modify the lock bit by a master with a different domain ID is ignored without transfer error. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/021_Flash_Memory_Controller_-PFLASH-/S32K3XXRM_数据表.pdf-0729-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 SETSL<br>W CK<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

729 / 4640 

NXP Semiconductors 

Flash Memory Controller (PFLASH) 

##### Fields 

|Field|Function|
|---|---|
|31-1|Reserved|
|—||
|0|Set Sector Lock|
|SETSLCK|Locks selected sector. If vector bit value = 0, the corresponding lock bit is not owned by any<br>master. If vector bit value = 1, the lock bit is owned by the masters having the domain ID stored<br>inPFCBLKn_LOCKMASTER_SSm.|



### 21.6.17 Block n Set Super Sector Lock (PFCBLK0_SSETSLOCK - PFCBLK3_SSETSLOCK) 

##### Offset 

|Register|Offset|
|---|---|
|PFCBLK0_SSETSLOCK|39Ch|
|PFCBLK1_SSETSLOCK|3A0h|
|PFCBLK2_SSETSLOCK|3A4h|
|PFCBLK3_SSETSLOCK|3A8h|



##### Function 

Provides a mechanism for the masters to gain ownership of the corresponding PFCBLKn_SPELOCK lock bit based on domain id. After it is equal to 1, the bit is returned to 0 at next reset. If any SSETSLOCK bit is not equal to 1, the corresponding LOCK bit can be modified by any master. If a bit is already acquired by a particular domain ID, any effort to modify the lock bit by a master with a different domain ID is ignored without transfer error. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/021_Flash_Memory_Controller_-PFLASH-/S32K3XXRM_数据表.pdf-0730-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>SSETSLCK<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>SSETSLCK<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

730 / 4640 

NXP Semiconductors 

Flash Memory Controller (PFLASH) 

##### Fields 

|Field|Function|
|---|---|
|31-28|Reserved|
|—||
|27-0|Set Super Sector Lock|
|SSETSLCK|Locks selected super sector. If vector bit value = 0, the corresponding lock bit is not owned by any master. If<br>vector bit value = 1, the lock bit is owned by the masters having the domain ID stored inBlock a Lock Master<br>Sector b (PFCBLK0_LOCKMASTER_S0 - PFCBLK4_LOCKMASTER_S7).|



### 21.6.18 Block a Lock Master Sector b (PFCBLK0_LOCKMASTER_S0 - PFCBLK4_LOCKMASTER_S7) 

##### Offset 

For a = 0 to 4; b = 0 to 7: 

|Register|Offset|
|---|---|
|PFCBLKa_LOCKMASTE|3C0h + (a × 20h) + (b × 4h)|
|R_Sb||



##### Function 

Provides the domain ID information of the master currently acquiring the lock bit. The domain ID is represented by an 8-bit field. This is a read-only register. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/021_Flash_Memory_Controller_-PFLASH-/S32K3XXRM_数据表.pdf-0731-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R LOCKMASTER_S<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R LOCKMASTER_S<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-0|Block a Lock Master Sector b|
||Contains domain ID of the master currently acquiring the lock bit.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

731 / 4640 

NXP Semiconductors 

Flash Memory Controller (PFLASH) 

|Field|Function|
|---|---|
|LOCKMASTER<br>_S|PFCBLK0_LOCKMASTER_S0[LOCKMASTER_S[7:0]] holds the domain ID information<br>of PFCBLK0_SPELOCK[0].|
||PFCBLK0_LOCKMASTER_S0[LOCKMASTER_S[15:8]] holds the domain ID information of<br>PFCBLK0_SPELOCK[1], and so on in incremental order.|



### 21.6.19 Block UTEST Lock Master Sector (PFCBLKU_LOCKMASTER_S) 

##### Offset 

|Register|Offset|
|---|---|
|PFCBLKU_LOCKMAST|480h|
|ER_S||



##### Function 

Provides the domain ID information of the master currently acquiring the lock bit. The domain ID is represented by an 8-bit field. This is a read-only register. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/021_Flash_Memory_Controller_-PFLASH-/S32K3XXRM_数据表.pdf-0732-09.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 LOCKMASTER_S<br>W<br>Reset 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-8|Reserved|
|—||
|7-0|Lock Master Sector|
|LOCKMASTER<br>_S|Contains domain ID of the master currently acquiring the lock bit.<br>PFCBLKU_LOCKMASTER_S[LOCKMASTER_S[7:0]] holds the domain ID information<br>of PFCBLKU_SPELOCK[0].|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

732 / 4640 

NXP Semiconductors 

Flash Memory Controller (PFLASH) 

### 21.6.20 Block m Lock Master Super Sector n (PFCBLK0_LOCKMASTER_SS0 - PFCBLK3_LOCKMASTER_SS6) 

##### Offset 

For a = 0 to 3; b = 0 to 6: 

|Register|Offset|
|---|---|
|PFCBLKa_LOCKMASTE|484h + (a × 1Ch) + (b × 4h)|
|R_SSb||



##### Function 

Provides the domain ID information of the master currently acquiring the lock bit. The domain ID is represented by an 8-bit field. This is a read-only register. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/021_Flash_Memory_Controller_-PFLASH-/S32K3XXRM_数据表.pdf-0733-09.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R LOCKMASTER_SS<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R LOCKMASTER_SS<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Block a Lock Master Super Sector b|
|LOCKMASTER<br>_SS|Contains domain ID of the master currently acquiring the lock bit.<br>PFCBLK0_LOCKMASTER_SS0[LOCKMASTER_SS[7:0]] holds thevdomain ID information<br>of PFCBLK0_SSPELOCK[0].|
||PFCBLK0_LOCKMASTER_SS0[LOCKMASTER_SS[15:8]] holds the domain ID information of<br>PFCBLK0_SSPELOCK[1], and so on in incremental order.|



## 21.7 Glossary 

AHB Advanced high-performance bus ECC Error correcting code HSE Hardware security engine IPS Internal peripheral system ID Identification 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

733 / 4640 

