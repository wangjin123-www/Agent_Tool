NXP Semiconductors 

# Chapter 20 Embedded Flash Memory (c40asf) 

## 20.1 Chip-specific c40asf flash memory information 

### 20.1.1 Flash memory configuration and register settings 

Table 90 shows flash memory blocks and their associated configuration. 

Table 90. Flash block configuration 

|Block or<br>address<br>number|Block name|Start<br>address (hex)|End address<br>(hex)|Size|Applicability|
|---|---|---|---|---|---|
|0|Code flash memory 0|0040_0000|004F_FFFF|1 MB|S32K3x4, S32K342,<br>S32K312, S32K322|
|||||512 KB|S32K311|
||||005F_FFFF|2 MB|S32K358|
|1|Code flash memory 1|0050_0000|005F_FFFF|1 MB|S32K3x4, S32K342,<br>S32K312, S32K322|
|||||512 KB|S32K311|
|||0060_0000|007F_FFFF|2 MB|S32K358|
|2|Code flash memory 2|0060_0000|006F_FFFF|1 MB|S32K3x4|
|||0080_0000|009F_FFFF|2 MB|S32K358|
|3|Code flash memory 3|0070_0000|007F_FFFF|1 MB|S32K3x4|
|||00A0_0000|00BF_FFFF|2 MB|S32K358|
|4<sup>1</sup>|Data flash memory|1000_0000|1001_FFFF|128 KB|S32K3x4|
|2<sup>1</sup>||||128 KB|S32K342, S32K312, S32K322|
|||1000_0000|1000_FFFF|64 KB|S32K311|
|||1000_0000|1003_FFFF|128 KB|S32K358|
|0<sup>2</sup>|UTest NVM|1B00_0000|1B00_1FFF|8 KB|S32K358, S32K3x4, S32K342,<br>S32K312, S32K311|



1. Sector operation should be used for data flash during high voltage operation. 

2. The address region number is the same as block number for all the blocks except this one. Address region is called UTest NVM address region in this case. 

No application cores except HSE_B can access the address regions shown in Table 91. 

Table 91. Secure flash memory configuration 

|Descriptio|S32K311||S32K312||S32K342||S32K3x4|/ S32K358|Size|
|---|---|---|---|---|---|---|---|---|---|
|n|Start|End|Start|End|Start|End|Start|End||
||address|address|address|address|address|address|address|address||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

633 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

Table 91. Secure flash memory configuration (continued) 

|Secure|004F_400|004F_FFF|005F_400|005F_FFF|005F_400|005F_FFF|007F_400|007F_FFF|48 KB|
|---|---|---|---|---|---|---|---|---|---|
|BAF code|0h|Fh|0h|Fh|0h|Fh|0h|Fh||
|(SBAF_C||||||||||
|ODE)||||||||||



~~<mark>NOTE</mark>~~ 

For HSE memory configuration, see 'Memory map when HSE firmware usage feature flag is enabled' section in 'Boot Overview' chapter. 

The flash memory can perform multiple reads in parallel (between different blocks), using the single-, dual-, or quad-read feature. It also includes an internal UTest mode that can generate single- and double-bit ECC errors. 

The code flash memory lets you access three data paths simultaneously. 

You can configure the flash memory sectors as erase- or write-protected by using the flash memory's sector and super-sector locking features. 

Data flash and/or Code flash memory blocks can be altered by a code executing from different flash block or SRAM. 

Data flash memory is the same as code flash memory—supporting program, erase, and read operations. 

After the completion of the program or erase operations, the MCR and MCRS registers notify you as soon as the code flash memory code can be executed. At the end of reset recovery, MCRS[DONE] transitions from 0 to 1. 

~~<mark>NOTE</mark>~~ 

MCRS[RWE] might become 1 during the program or erase operation because of speculative accesses by CortexM7 core(s). If there are memory regions where no speculative accesses must be initiated, Arm recommends to configure the on-core MPU to set those regions with these attributes: 

- Device or strongly-ordered 

- Execute never 

~~<mark>NOTE</mark>~~ 

- ADR[A3] and ADR[A4] field are reserved for S32K312, as code flash memory size in 2 MB for S32K312. 

- For S32K312, reset value of FLASH_SSPELOCK and FLASH_XSSPELOCK register is 0x0FFF_FFFF. 

### 20.1.2 MCRE register reset value 

The reset value of the MCRE register depends on the chip-specific flash memory configuration. This table provides the flash memory configuration of the chip and the associated register reset values. 

Table 92. MCRE register reset value 

|MCRE fields|Reset value|
|---|---|
|n1M (bit position 23:21)|100b – Four 1 MB blocks|
||010b – Two 1 MB blocks|
|n512K (bit position 15:14)|00b – Zero 512 KB blocks|
|n256K (bit position 7:6)|01b – One 256 KB blocks|
|MCRE register reset value|S32K3x4 - 0080_0040h|
||S32K3x2 - 0040_0040h|
||S32K3x8 - 8000_0040h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

634 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

### 20.1.3 Debugger considerations while Flash Program/Erase 

While flash programming is done via debugger, special considerations should be taken care off. See "Debug Subsystem" chapter for details. 

## 20.2 Introduction 

The primary function of the embedded flash memory serves as an electrically programmable and erasable non-volatile memory (NVM) that may be used for instruction or data storage. 

### 20.2.1 Overview 

The embedded flash memory is designed for use in embedded MCU and SoC applications. It supports a total memory size up to 8.5 MB of NVM in main space and 8 KB of UTest NVM space per module. Multiple flash modules may be instantiated within an SoC to achieve higher density. The embedded flash memory is addressable by page (256 bits) for read operation and double-word(s) and page and quad page for program operations. Flash memory reads always return 256 bits, although read page buffering may be performed by the PFC. The flash memory is able to do multiple reads in parallel (between different blocks), utilizing the quad read feature. 

For details on the embedded flash memory architecture and features, see Functional description. 

The following figure shows the top-level diagram and functional organization of the flash memory unit. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/020_Embedded_Flash_Memory_-c40asf-/S32K3XXRM_数据表.pdf-0635-10.png)


<!-- Start of picture text -->
Vss Vddf Vflash<br>FMU<br>Slave Bus<br>Signals<br>Configuration Analog<br>AIPS<br>Registers<br>Osc/Timer<br>Flash Read<br>Interface<br>Flash Interface<br>Ref. Generator<br>Program/Erase<br>Flash Write Controller<br>Platform Interface<br>Flash<br>BIU<br>ECC<br>Signal<br>Flash Bias<br>UTest<br>P/E<br>Controller<br>LOCK<br>sidebands<br>Misc. OPP Flash Block(s)<br>SoC sidebands HW<br>Blocks Control Factory Test<br>(DCM, Interface Logic<br>security) Security<br>sidebands<br>Test Configuration<br>Registers<br>SoC Sstem Busy<br><!-- End of picture text -->

Figure 45. Block diagram 

### 20.2.2 Features 

The embedded flash memory includes these distinct features: 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

635 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

- Test information stored in a dedicated non-volatile sector (referred to as the UTest sector) 

- OTP space made available in the UTest sector 

- Read page size of 256 bits (8 words) 

- ECC with single bit correction, double bit detection (all 1s valid) with 64-bit granularity 

- Quad page programming (256-bit granularity) 

- Hardware programmable sector and super sector program or erase restriction control 

- Erasing of selected sector or block erase 

- Independent programming of the UTest NVM sector 

- Embedded hardware program and erase algorithms 

- Support for reading while writing when the accesses are to different blocks 

- UTest mode (user-accessible test modes) including array integrity and margin read 

- Triple-voted flops for safety-critical flash memory functions (for example, internal trimming, redundancy, mode control, and others) 

### 20.2.3 Modes of operation 

Following is a brief description of the embedded flash memory operating modes. 

- User mode is the default operating mode of the embedded flash memory. In this mode, it is possible to read and write registers (including register-based interlock writes), read the memory array, program the memory array, and erase the memory array. In this mode program and erase operations are initiated by doing register writes. Program and erase operations are controlled by an internal state machine. 

- Low-Power mode turns off all DC current sources within the embedded flash memory and enables VFLASH and VDDF to be power gated. The embedded flash memory is not accessible for read, write, program, or erase when in Low-Power mode. This mode results in the lowest current draw that embedded flash memory can achieve. 

- UTest mode is a tiered test mode strategy in which a portion of the factory test modes are made available. This mode is protected but accessible. 

## 20.3 UTest NVM sector 

The UTest NVM sector may be enabled by PEADR[PEASAD] during interlock writes. When the UTest NVM space is enabled, all program and erase operations are mapped to the UTest NVM sector. User-mode programming of the UTest NVM sector is enabled only when PEADR[PEASAD] is high. 

The UTest NVM sector is an OTP sector (assuming Test mode disable seal is written) . Therefore, performing an erase operation is not permitted. 

The UTest NVM sector supports RWW, and is grouped with the sectors in partition 0. 

The UTest NVM sector may be locked against program by using hardware program and erase protection input to the flash module (MCRS[TSPELOCK]). 

The UTest NVM sector contains specified data that is needed for embedded flash memory or SoC features. 

Programming of the UTest NVM space has restrictions that are similar to those of the main space in terms of how ECC is calculated. Only one program operation is allowed per 64-bit ECC segment. 

## 20.4 Test mode disable seal 

The UTest NVM sector includes a mechanism to disable factory entry into Test mode selectable by block. Extreme care must be taken when using this feature, because blocks that are selected to be protected in this method will not have possible failures analyzed by factory failure analysts. Once sealed, the UTest sector becomes OTP (erase locked, and OPP enabled). The UTest sector is not accessible in Test Mode. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

636 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

Protection of this sort prevents all high voltage operations to the flash memory executed by the internal state-machine, as well as reads through this state machine, and reads through the array integrity state machine when using Test mode interfaces. 

UTest operations, margin read and array integrity, are also protected by preventing MISR updates on blocks selected for protection, although reads are still performed, and single bit corrections and double bit detections will be logged. Protection through other interfaces is provided by normal User mode protection mechanisms and is device-specific. 

The method to disable factory entry into Test mode is to first program the Test mode disable seal location to be 5A4B_3C2Dh. After the next reset is asserted, Test mode is disabled. 

It is possible to create a password to enable factory entry into Test mode. This can be programmed into the Test mode disable override passcode. The passcode may not be 0000_0000h, FFFF_FFFFh, or 5555_5555h. These are all invalid passcodes and will not be accepted to override. If it is desired, by the customer, that override never be possible, one of the three invalid passcodes must be put into the Test mode disable override passcode location. Passcode may be entered to authenticate entry, if enabled, by performing a 32-bit register write to register address 90h. 

Even if the Test mode disable seal password is written, the UTest NVM sector is always protected and the UTest operations, margin read and array integrity, are always protected. 

Only blocks selected in the Test mode disable block select field are controlled by the Test mode disable feature. Therefore, it is possible for customers to selectively pick blocks that have this type of protection and will not be eligible for factory failure analysis. Bits programmed to 0 in the Test mode disable block select field(s) designate blocks that are controlled by the Test mode disable feature. 

In order to let two opportunities to select blocks for the Test mode disable, two regions are available, Test mode disable bock select - 1 and Test mode disable block select - 2. If either Test mode disable block select - 1 or Test mode disable block select - 2 has a 0 programmed, that block will be protected. The bits of these two regions are logically ANDed to define the blocks that are effectively selected for the Test mode disable feature. The bock select field is organized as shown in the next table: 

Table 93. Test mode disable block select 

|Block|Bits used to select blocks|
|---|---|
|Block 0 disable|Data[0]|
|Block 1 disable|Data[8]|
|Block 2 disable|Data[16]|
|Block 3 disable|Data[24]|
|Block 4 disable|Data[32]|
|Block 5 disable|Data[40]|



## 20.5 Functional description 

The embedded flash memory module consists of blocks with the following options: 

- 2 MB blocks (0, 1, 2, 3 or 4 blocks allowed per module) 

- 1 MB blocks (0, 1, 2, 3 or 4 blocks allowed per module) 

- 512 KB blocks (0, 1, 2 or 4 blocks allowed per module) 

- 256 KB blocks (0, 1, 2 or 4 blocks allowed per module) 

- A total of six blocks are allowed per module 

Read while Write is allowed within a module, and is determined based on block boundaries. Read while Write partitions are used to determine locations for valid read-while-write (RWW) operations. While the embedded flash memory performs a write (program or erase) to a given partition, it can simultaneously perform a read from any other partition. For program and erase operations, only 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

637 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

the address specified by an interlock write determines the partition being written (sector or super sector locking does not determine the RWW partitions being written). 

The main address space is also divided into sectors and super sectors to implement independent erase and program protection. The UTest NVM space also exists as a sector and has independent program protection. The UTest NVM sector is included to support systems that require non-volatile memory (NVM) for security or to store system initialization information. 

A number of MCR bits are protected against write when another field, or set of fields, is in a specific state. These write locks are covered on a bit-by-bit basis in Module Configuration Register. The write locks do not consider the effects of trying to write two or more bits simultaneously. This module does not allow fields to be written simultaneously that put the device into an illegal state. This is implemented through a priority mechanism among the fields, and the next table shows this mechanism. 

Table 94. MCR field set and clear priority levels 

|Priority level|MCR field(s)|
|---|---|
|1|ERS|
|2|PGM|
|3|EHV|



If two or more MCR fields are written simultaneously, only the field with the lowest priority number is accepted for modification. For example, writing 1 to ERS and PGM simultaneously results in 1 being written only to ERS. 

Each read of the embedded flash memory retrieves a page, or eight consecutive words (256 bits), of information. The address for each word retrieved within a page differs from the other addresses in the page only by address bits [4:2]. The flash memory page read architecture easily supports both cache and burst mode at the PFC BIU level for high-speed read applications. 

The embedded flash memory supports fault tolerance through error correction code (ECC) and error detection. ECC implemented within the embedded flash memory corrects single bit failures and detects double bit failures. 

Program and erase of the embedded flash memory requires multiple system clock cycles to complete. Program and erase may be aborted. 

The embedded flash memory may operate in various modes as described in the following sections. 

### 20.5.1 User mode 

In User mode, the embedded flash memory may be read and written (register writes and interlock writes), programmed or erased. The following sub-sections define all actions that may be performed in User mode. 

#### 20.5.1.1 Read and write 

The default state of the embedded flash memory is read. The main and UTest NVM address spaces can be read only in the read state. The flash registers are always available for read, except when the embedded flash memory is in Low-Power mode. The module enters the read state on reset, and remains in the read state under two sets of conditions: 

- The read state is active when the embedded flash memory is enabled (User mode read). 

- The read state is active when MCR[PGM] or MCR[ERS] are 1 and a high voltage operation is ongoing (RWW). 

~~<mark>NOTE</mark>~~ 

Reads done to the partition(s) being operated on (either erased or programmed) result in MCRS[RWE] becoming 1. 

In embedded flash memory, flash core reads return 256 bits (1 page). Register reads return 32 bits of data. 

~~<mark>NOTE</mark>~~ 

Flash core reads are performed through the PFC BIU. In many cases, the BIU does read page buffering to allow sequential reads to be done with higher performance. This could provide a data coherency issue that must be handled with software. Data coherency may be an issue after a program or erase operation, as well as UTest NVM sector operations. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

638 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

In user mode, registers may be written (including interlock writes using registers). 

Register reads to unmapped register address space return all 0s. 

Register writes to unmapped register address space have no effect. 

Interlock writes that are attempted during a high voltage operation (MCR[EHV] = 1 or MCRS[DONE] =0) result in the interlock write being ignored, and address and data will not be updated. 

#### 20.5.1.2 Program 

A flash memory program sequence operates on any page within the flash core. Within a page, up to eight words may be altered in a single program operation. Also, up to four pages can be altered in a single program operation. Whenever the array is programmed, the ECC bits also get programmed. 

ECC is handled on a 64-bit boundary. Thus, if only one word in any given 64-bit ECC segment is programmed, the adjoining word in that segment should not be programmed, because ECC calculation is already complete for that 64-bit segment. Attempts to program the adjoining word may likely result in an operation failure. It is recommended that all programming operations ranger from 64 bits to 1024 bits, and be 64-bit aligned. The programming operation should completely fill selected ECC segments within the page. Only one program is allowed per 64-bit ECC segment between erases. 

~~<mark>Caution</mark>~~ 

In rare cases, over-programming of a 64-bit ECC segment may be done (EEPROM emulation in data flash region). In this case, approved EEPROM emulation drivers must be used, and they must limit the number of over-program operations to three times (four total programs between erases). 

Programming changes the value stored in an array bit from logic 1 to logic 0 only. Programming cannot change a stored logic 0 to a logic 1. 

~~<mark>NOTE</mark>~~ 

If a logic 0 is attempted to be over-programmed by a logic 1, the resulting operation fails (MCRS[PEG] = 0), and the 0s that are interlocked are merged (ORed) with the 0s that are already present in the 64-bit ECC segment, unless the block is designated as an over-orogram protected block. 

Addresses in locked sectors cannot be programmed. Values may be programmed in any or all of eight words, within a page, with a single program sequence. Up to four pages can be programmed at once on a quad-page boundary. The program operation consists of the following sequence of events: 

1. Write the address to be programmed using logical address registers located in the PFC. The result of this write will also be reflected physically in the PEADR register. 

~~<mark>NOTE</mark>~~ 

PEADR writes are initiated by writes that first occur in the PFC. Please see the platform flash memory controller chapter for more information. PEADR reads are allowed, and represent the flash memory physical address. 

~~<mark>NOTE</mark>~~ 

Ensure the sector that contains the address to be programmed is unlocked. Sector and super sector lock status is latched at this step and does not change until the next program or erase sequence is started. 

2. Data to be programmed must be written in the appropriate DATAX register (where X is 0 to 31). All unwritten data words default to FFFF_FFFFh. 

3. Change the value in MCR[PGM] from a 0 to a 1. 

4. Write a 1 to MCR[EHV] to start the internal program sequence or skip to step 8 to terminate. 

5. Wait until MCRS[DONE] becomes 1. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

639 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

~~<mark>NOTE</mark>~~ 

Since MCRS[DONE] clears with MCR[EHV] being set, it may not be possible for software to read MCRS[DONE] as 0 between step 4 and step 5, depending on the operation selected. 

6. Confirm MCRS[PEG] = 1. 

7. Write 0 to MCR[EHV]. 

8. Write 0 to MCR[PGM] to terminate the program sequence. 

Program may be initiated with the writing of the PEADR register (enabled with a write done in the PFC block). The PEADR write to initiate the program sequence determines the quad-page address to be programmed. Data must also be written to the DATA register(s). This first write is referred to as an interlock write. Unwritten locations default to a data value of FFFF_FFFFh. 

An interlock write must be performed before writing 1 to MCR[PGM], and MCR[PGM] must be set before writing 1 to MCR[EHV] during a program sequence. A program sequence may be terminated by writing 0 to MCR[PGM] prior to writing 1 to MCR[EHV]. 

While MCR[EHV] is 1 and MCRS[DONE] is 0, MCR[EHV] may be cleared, resulting in a program abort. A program abort forces the embedded flash memory to step 8 of the program sequence. An aborted program results in PEG becoming 0, indicating a failed operation. The data space being operated on before the abort contains indeterminate data. 

~~<mark>Caution</mark>~~ Aborting a program operation leaves the FC addresses being programmed in an indeterminate data state. This may be recovered by executing an erase on the affected block. 

#### 20.5.1.2.1 Program hardware locking 

Hardware locking which affects the program and erase operations is available for UTest sector and all array blocks. 

#### 20.5.1.2.2 Over-program protection enable 

One-time programming can be enabled. If over-program protection is enabled, any double word that has already been programmed cannot be programmed again. The over-program protection enable does not affect the erase operation. Attempts to over-program result in MCRS[PEG] becoming 0. If any double word within a quad-page has an over-program protection violation, MCRS[PEG] becomes 0, and no double words are programmed. 

One-time programming can be enabled for the UTest NVM sector. 

#### 20.5.1.3 Erase 

An erase changes the value stored in all bits of the selected sector or block to logic 1, and operates on a sector or a block in the main address space. The erase sequence is fully automated within the flash memory. Locked sectors cannot be erased. The erase sequence consists of the following events: 

1. Write to the sector or block address to be erased using logical address registers located in the PFC. The result of this write is reflected physically in the PEADR register. One, and only one, DATA register must also be written. This is referred to as an erase interlock write. 

~~<mark>NOTE</mark>~~ 

PEADR writes are initiated by writes that first occur in the PFC. Please see the platform memory flash controller chapter for more information. PEADR reads are allowed, and represent the flash memory physical address. 

~~<mark>NOTE</mark>~~ 

The selected block or sector must be unlocked prior to initiating an erase with the appropriate sector or super sector lock registers. Sector and super sector lock status is latched at this step and does not change until the next program or erase sequence starts. If a block is selected for erase, all the sectors and super sectors must be unlocked within that block. 

2. Change the value in MCR[ERS] from a 0 to a 1, and at the same time select the size of erase using MCR[ESS]. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

640 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

3. Write a 1 to MCR[EHV] to start the internal erase sequence or skip to step 6 to terminate. 

4. Wait until MCRS[DONE] becomes 1. 

~~<mark>NOTE</mark>~~ 

Since MCRS[DONE] clears with MCR[EHV] being set, it may not be possible for software to read MCRS[DONE] as 0 between step 3 and step 4, depending on the operation selected. 

5. Confirm MCRS[PEG] = 1. 

6. Write 0 to MCR[EHV]. 

7. Write 0 to MCR[ERS] to terminate the erase, and if set MCR[ESS] should also be cleared (else the field auto clears). 

Erase may be initiated with the writing of the PEADR register (enabled with a write done in the Platform Flash Controller block). The PEADR write to initiate the erase sequence determines the sector or block to be erased. One write must also occur to a DATA register. Data word written during an erase sequence interlock write is ignored. This write is referred to as an erase interlock write. 

An erase interlock write must occur before writing 1 to MCR[ERS] (and optionally MCR[ESS]), and MCR[ERS] must be set before writing 1 to MCR[EHV] during an erase sequence. The erase sequence may be terminated by writing 0 to MCR[ERS] prior to writing 1 to MCR[EHV]. 

While MCR[EHV] is 1 and MCRS[DONE] is 0, MCR[EHV] may be cleared, resulting in an erase abort. An erase abort forces the embedded flash memory to step 7 of the erase sequence. An aborted erase results in PEG becoming 0, indicating a failed operation. The sector or block being operated on before the abort contain indeterminate data. 

#### 20.5.1.3.1 Erase hardware locking 

Hardware locking which affects the erase and program operations is available for UTest sector and all array blocks. For details, see Program hardware locking. 

#### 20.5.1.4 Express program 

A mechanism is made available to provide an express method to program up to 1024 bits of flash memory. When activated, all ongoing program and erase operations through the register interface are automatically aborted (MCR[EHV] becomes 0 automatically) and the express interface is given priority. When using the express interface, sequence requirements are ignored, although a XPEADR write is required to start the express program sequence. 

The flash express program mechanism provides a quicker way to get information programmed into a block of flash memory when an application needs an immediate diary access, or a crash log access. 

Addresses in locked sectors cannot be express programmed. 

The express program operation consists of the following sequence of events: 

1. Write the address to be programmed using the logical address register located in the PFC. The result of this write will also be reflected physically in the XPEADR register. 

~~<mark>NOTE</mark>~~ 

XPEADR writes are initiated by writes that first occur to the PFC. Please see the platform flash controller chapter for more information. XPEADR reads are allowed, and represent the flash memory physical address. 

~~<mark>NOTE</mark>~~ 

Ensure the sector that contains the address to be programmed is unlocked. Sector and super sector lock status is latched at this step and does not change until the next program, erase or express program is started. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

641 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

~~<mark>NOTE</mark>~~ 

If XMCR[XPGM] interrupts a program or erase setup after MCR[EHV] is written to 1, the MCR and MCRS registers indicate if the operation was automatically aborted (MCR[EHV] = 0, MCRS[PEG] = 0, MCR[PGM] =1 or MCR[ERS] = 1), or if the operation was successful (MCR[EHV] = 1, MCRS[PEG] = 1, MCR[PGM] =1 or MCR[ERS] = 1). If express program interrupts a program or erase setup prior to MCR[EHV] being written to a 1, the MCR and PEADR registers will be preserved to show the state of the setup upon interruption. If fields MCR[PGM] = 1 or MCR[ERS] = 1 at interruption, the user must terminate the event by writing 0 to these fields. However, if MCR[PGM] or MCR[ERS] were not 1 at interruption, PEADR is preserved and does not need to be rewritten, but the PDATA registers are required to be rewritten for the interrupted operation. After the PDATA write(s) are repeated to finish the interlock write, the remainder of the program and erase sequence can be done to restart the interrupted operation (including doing a terminate after PGM or ERS are written to 1, if desired). 

~~<mark>NOTE</mark>~~ 

Before starting the express program, ensure that UTest operations (array integrity or user margin read) are not ongoing (or about to be started). UT0[UTE] must be low before requesting the express program, and remain low during express program operations. Hardware locks are in place to ensure this occurs. 

2. Wait until XMCR[XDOK] goes high. 

3. Write the DATA registers with the data desired to be programmed. Up to 1024b (128B) may be programmed with express program. Only DATA registers that are written will receive program pulses. 

4. Change the value in XMCR[XPGM] from a 0 to a 1. 

5. Write a 1 to XMCR[XEHV] to start the internal express program sequence. 

6. Wait until XMCR[XDONE] becomes 1. 

7. Confirm XMCR[XPEG] = 1. 

8. Write 0 to XMCR[XEHV]. 

9. Write 0 to XMCR[XPGM] to terminate the express program sequence. 

### 20.5.2 Low-Power mode 

In Low-Power mode, the embedded flash memory is put into a state where VDDF power gating and VFLASH power gating is allowed. It is the lowest current mode for the flash memory. No reads from or writes to the embedded flash memory are possible when in this mode. Most power dissipation is due to leakage in this mode. 

Prior to entering Low-Power mode, it is required that all program, erase, and UTest operations be stopped. 

When in Low-Power mode, register access is prevented. Flash core accesses are also prevented until power mode is exited. Flash core reads and writes may occur after power mode is exited. 

The embedded flash memory returns to a post-reset state in all cases. 

### 20.5.3 Program and erase watchdog timer 

The embedded flash memory contains an internal watchdog timer that is used to prevent denial of service issues and events. 

The watchdog timer is active during two periods of a program and erase event: program/erase setup and program/erase cleanup. If it is desired that program and erase operations also be checked with a watchdog timer, a system resource may be used for this purpose. 

Program/erase setup always starts at the time of the PEADR write. An express program setup starts with a write to XPEADR and XMCR[XDOK] = 1. In the event of an Express program interrupt of main or alternate interface setup, the timer starts at the time when the express program operation completes (write of XMCR[XPGM] = 0). The watchdog stops when either MCR[EHV] is set to start the operation, or when the operation is terminated. Termination can occur when MCR[PGM] or MCR[ERS] are written to 0 (prior to MCR[EHV] being written to 1), or MCRS[PES] written to 0. If the express program interrupts the program/erase setup, this also stops the timer on that interface, and express program maintains priority. The above statements also apply to the alternate interface. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

642 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

~~<mark>NOTE</mark>~~ 

If PEADR writes occur while UT0[UTE] is 1, the watchdog feature does not activate for setup. Watchdog timer is not active during UTest operations. 

Program/erase cleanup always starts at the time of MCRS[DONE] = 1 on completion or an abort. In the event of an express program auto-abort of main or alternate interface, the cleanup starts at the time of MCRS[DONE] becoming 1 and the express program operation completed (XMCR[XPGM] written to 0). The watchdog stops when MCR[PGM] or MCR[ERS] are written to 0 at the end of the operation. If express program interrupts the program/erase cleanup, the timer on that interface also stops. The above statements also apply to the alternate interface. 

Watchdog timers exist for each interface (main, alternate and express). 

If a watchdog timeout occurs, the watchdog interrupt will be reflected in MCRS[WDI], AMCRS[AWDI] or XMCR[XWDI]. Interrupts can be enabled on the main and alternate interfaces using MCR[WDIE] or AMCR[AWDIE]. When a watchdog timeout occurs and an interrupt register asserts, the PEID restrictions on that interface are released. At that point, any master can complete the operation, and PEID locking is no longer enforced. If the watchdog timeout occurs, the EHV bit on that interface (MCR[EHV], AMCR[AEHV], and XMCR[XEHV]) are locked for writing to a 1. In this instance, any master can take the interface to a program and erase terminate. This enables accepted MCRS[WDI], AMCRS[AWDI] or XMCR[XWDI] to become 0, and the operation may restart with a new interlock write. 

~~<mark>NOTE</mark>~~ 

If the watchdog timeout occurs before PGM becomes 1 (on any interface), or ERS becomes 1 (on any interface), the sequence must be taken to the point that the PGM or ERS bit for that interface is written and then the field for that interface can be cleared to create the terminate event and to clear the watchdog interrupt. 

By default, the watchdog is enabled. Through the alternate MCR, the watchdog may be disabled (AMCR[WDD]), and the watchdog timeouts maybe adjusted (AMCR[WDT]) for all timeouts and all interfaces. 

### 20.5.4 UTest mode 

UTest mode enables customers to do specific tests that check the integrity of the embedded flash memory. 

~~<mark>NOTE</mark>~~ 

When entering UTest mode, a best practice is to ensure all error flags and address error reporting in ADR are cleared to their reset value to ensure robust software and procedure execution. 

~~<mark>NOTE</mark>~~ 

UTest mode diagnostic features ECC Logic Check, EDC after ECC Logic Check, Address Encode Logic Check, and Read Reference and Voltage Check, require serialization of flash reads starting with mode setup and ending with mode exit. This may be accomplished by executing diagnostic code from system RAM (with single reads to flash tagged address) as well as ensuring any flash reads outside of this diagnostic code are idle (single core). 

#### 20.5.4.1 Array integrity self check 

Array integrity is checked using a predefined address sequence (based on UT0[AIS]), and this operation is executed on selected blocks. 

The data to be read is customer-specific user code programmed into the flash memory and the correct MISR signature is calculated based on that code. 

Any random or nonrandom code is valid. After the operation completes, the results of the reads can be checked by reading the MISR value, to determine if an incorrect read or ECC detection was noted. Array integrity MISR value is calculated after ECC detection and correction. Array integrity requires that the read wait states control registers in the CTL register be set to match the system frequency being used. 

The array integrity self check consists of the following steps: 

1. Enable UTest mode. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

643 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

2. Select the block to receive the array integrity check by performing an interlock write to that block. Write logical address register in the PFC (which will be reflected in the PEADR register) and 1 DATA register (PDATA is ignored). The block selected for array integrity check does not need to be unlocked. 

   - ~~<mark>NOTE</mark>~~ 

Blocks protected with the Test mode disable seal are still read as part of the array integrity sequence. The resulting read on sealed blocks is not captured in the MISR, but single bit correction, double bit detection and breakpoints are still honored. 

~~<mark>NOTE</mark>~~ 

It is not possible to perform array integrity operations on the UTest NVM sector. 

3. If desired, write 1 to UT0[AIS] for sequential addressing only. 

~~<mark>NOTE</mark>~~ 

For normal integrity checks of the flash memory, sequential addressing is recommended. If it is required to more thoroughly check the read path (in a diagnostic mode), AIS shall remain 0 to examine more read transitions. This sequence takes more time. 

4. Seed the MISR registers (UM0 - UM9) with desired values. 

5. If breakpoints are desired, write 1 to UT0[AIBPE], and ensure that MCRS[EER] and MCRS[SBC] are 0. If it is desired to break on a single bit correction, ensure that UT0[SBCE] = 1. 

6. Write 1 to UT0[AIE]. 

   - a. If desired, the array integrity operation may be aborted before UT0[AID] goes high. This may be done by writing 0 to UT0[AIE] and then continuing to the next step. Note that in the event of an aborted array integrity check, MISRs contain a signature for the portion of the operation that was completed prior to the abort and are not deterministic. Before performing another array integrity operation, the UM0, UM1, UM2, UM3, UM4, UM5, UM6, UM7, UM8, and UM9 registers may need to be initialized to the desired seed value by doing register writes. 

   - b. If desired, the array integrity operation may be suspended before UT0[AID] goes high. This may be done by writing 1 to UT0[AISUS] to request an array integrity suspend. After UT0[AISUS] becomes 1, the user should wait for UT0[AID] to become 1, which indicates that the flash memory has entered the suspend state, and normal reads to the flash memory may be done. After UT0[AID] becomes 1, UT0[AISUS] may be written to 0 to resume the array integrity sequence. 

      - ~~<mark>NOTE</mark>~~ 

User mode array reads requested during the array integrity test are ignored to ensure that the array integrity operation is not corrupted. The memory array does not respond to array read requests during this time. User mode array reads may be executed if suspended or at a breakpoint. 

7. Wait until UT0[AID] becomes 1. 

8. If breakpoints are enabled, check if UT0[NAIBP] = 1. If the value of this field is 1, MCRS[EER], MCRS[SBC], and ADDR may be checked to determine the cause of the break and the address of the break. Prior to resuming the operation, write 1 to clear MCRS[SBC] or MCRS[EER]. Then, the operation may be resumed by writing 0 to UT0[NAIBP]. Continue to wait until UT0[AID] becomes 1. If breakpoints are not enabled, or if UT0[NAIBP] = 0 when UT0[AID] becomes 1, the operation is complete. Continue to the next step. 

9. Read values in MISRs (UM0 - UM9) to ensure correct signature. 

~~<mark>NOTE</mark>~~ 

Array integrity reads may be done to unselected (or non-present) locations. Reads done to these locations do not update the MISRs, MCRS[EER] and MCRS[SBC]. 

10. Write 0 to UT0[AIE]. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

644 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

#### 20.5.4.2 User margin read 

User margin read may be done using the array integrity interface, and has all the associated features of the array integrity interface (MISR and breakpoints). 

User margin reads are done at a read margin level, checking for erased bits or programmed bits encroaching on the nominal read level. 

User margin read requires that the Read Wait States control registers in the CTL register be written to match the system frequency being used. Margin ECC corrections and detections are noted during the user margin read test. Margin read MISR value is calculated after ECC detection and correction. 

The data to be read is customer-specific user code programmed into the flash memory. 

Any random or non-random code is valid. After the operation completes, the margin read results can be checked by reading MCRS[EER] and the MCRS[SBC] to determine if zero, one, or two bits are being detected by the margin read, as well as checking the MISR signature. 

The use model for margin read is in the event of a user-detected single bit correction (through user reads), a margin read may be done to check for a possible second bit falling within the selected margin levels. 

The user margin read consists of the following steps: 

1. Enable UTest mode. 

2. Select the block to receive the array integrity check by performing an interlock write to that block. Write logical address register in the PFC (which will be reflected in the PEADR register) and 1 DATA register (PDATA is ignored). The block selected for user margin read check does not need to be unlocked. 

~~<mark>NOTE</mark>~~ 

Blocks protected with the Test mode disable seal are still read as part of the margin read sequence. The resulting read on sealed blocks is not captured in the MISR, but single bit correction, double bit detection and breakpoints are still honored. 

~~<mark>NOTE</mark>~~ 

It is not possible to perform margin read operations on the UTest NVM sector. 

3. Write 1 to UT0[AIS] for sequential addressing only. 

~~<mark>NOTE</mark>~~ 

For margin read checks of the flash memory, sequential addressing is recommended. Writing 0 to UT0[AIS] is possible for margin reads, but using the sequence takes more time, and is not recommended. 

4. Seed the MISR registers (UM0 - UM9) with desired values. 

5. Ensure that MCRS[EER] and MCRS[SBC] are 0. 

6. To enable single bit correction reporting during margin read, write UT0[SBCE] = 1. 

7. Write 1 to UT0[MRE]. 

8. Write UT0[MRV] to the desired value depending on if it is desired to do one's margin or zero's margin. 

9. Write 1 to UT0[AIE]. 

~~<mark>NOTE</mark>~~ 

User mode array reads requested during the margin read test are ignored to ensure that the margin read operation is not corrupted. The memory array does not respond to array read requests during this time. User mode array reads may be executed if suspended or at a breakpoint. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

645 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

~~<mark>NOTE</mark>~~ 

During margin read operations, with UT0[AID] = 0, it is not recommended to attempt write operations to MCRS[SBC] and MCRS[EER]. It is recommended that these fields only be written during suspend, breakpoints or at the completion of the margin read operation. 

10. Wait until UT0[AID] becomes 1. 

11. If breakpoints are enabled or a suspend was requested during margin read, the operation may be at a breakpoint or a suspend state. See Array integrity self check for more information. 

12. Read values in the MISRs (UM0 - UM9) to ensure correct signature. 

~~<mark>NOTE</mark>~~ 

Margin reads may be done to unselected (or non-present) locations. Reads done to these locations do not update the MISRs, MCRS[EER] and MCRS[SBC]. 

13. Write 0 to UT0[AIE]. 

#### 20.5.4.3 ECC logic check 

ECC logic can be checked by providing data to be read in UD0[EDATA], UD1[EDATA] and/or UD2[EDATAC]. Array reads can then be performed, ensuring expected results. 

The ECC logic check consists of the following steps: 

1. Enable UTest mode. 

2. Write 1 to UT0[EIE]. 

3. Write to UD0[EDATA], UD1[EDATA] and/or UD2[EDATAC] to provide data and check bit values to be read. Single bit corrections or double bit detections can be simulated by properly selecting data and check bit combinations. 

4. Write the page address to receive data provided in step 3 into ADR. 

5. Write to UD2[ED3], UD2[ED2], UD2[ED1] and/or UD2[ED0] to select the double words on the page to receive the check. 

6. Reads can now be done through the BIU using an array read request. In the event of a BIU read requested from an address that matches the address in ADR, expected data and corrections or detections are observed based on data written into UD0[EDATA], UD1[EDATA] and/or UD2[EDATAC]. MCRS[EER] and MCRS[SBC] can be checked to evaluate the status of reads done. 

~~<mark>NOTE</mark>~~ 

In the event of an ECC error or single bit correction, during the ECC logic check (UT0[EIE] = 1), ADR is not loaded, and the address tagged to receive the ECC logic check values is preserved. 

7. Once completed, write UT0[EIE] to 0. 

#### 20.5.4.4 EDC after ECC logic check 

EDC after ECC logic can be checked by providing data to be read in UD3[EDDATA], UD4[EDDATA] and/or UD5[EDDATAC]. Array reads can then be performed, ensuring expected results. 

The EDC after ECC logic check consists of the following steps: 

1. Enable UTest mode. 

2. Write 1 to UT0[EDIE]. 

3. Write to UD3[EDDATA], UD4[EDDATA] and/or UD5[EDDATAC] to provide data and check bit values to be read. 

4. Write the page address to receive data provided in step 3 into ADR. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

646 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

5. Write to UD5[EDD3], UD5[EDD2], UD5[EDD1] and/or UD5[EDD0] to select the double words on the page to receive the check. 

6. Reads can now be done through the BIU using an array read request. In the event of a BIU read requested from an address that matches the address in ADR, expected EDC after ECC errors are observed based on data written into UD3[EDDATA], UD4[EDDATA] and/or UD5[EDDATAC]. MCRS[EEE] can be checked to evaluate the status of reads done. 

7. Once completed, write UT0[EDIE] to 0. 

#### 20.5.4.5 Address encode logic check 

Address encode logic can be checked by inverting the address encode information from the memory array in UA0[AEI] and UA1[AEI]. Array reads can then be performed, ensuring expected results. 

The Address encode check consists of the following steps: 

1. Enable UTest mode. 

2. Write 1 to UT0[AEIE]. 

3. Write to UA0[AEI] and/or UA1[AEI] to provide address bit(s) to be inverted. 

4. Write the page address to receive inverted addresses provided in step 3 into ADR. 

5. Reads can now be done through the BIU using an array read request. In the event of a BIU read requested from an address that matches the address in ADR, expected address encode errors are observed based on address invert values written into UA0[AEI] and/or UA1[AEI]. MCRS[AEE] can be checked to evaluate the status of reads done. 

6. Once completed, write UT0[AEIE] to 0. 

#### 20.5.4.6 Read reference and voltage check 

Read reference and voltage detection logic can be checked by writing 1 to UT0[RRIE]. Array reads can be then be performed, ensuring expected results. 

The read reference and voltage check consists of the following steps: 

1. Enable UTest mode. 

2. Write 1 to UT0[RRIE]. 

3. Write the page address to receive a read reference error MCRS[RRE] and a read voltage error MCRS[RVE] into ADR. 

4. Reads can now be done through the BIU using an array read request. In the event of a BIU read requested from an address that matches the address in ADR, expected read reference and read voltage errors are observed based on ADR registers. MCRS[RRE] and MCRS[RVE] can be checked to evaluate the status of reads done. 

5. Once completed, write UT0[RRIE] to 0. 

### 20.5.5 Data flash memory requirements for EEPROM emulation 

The embedded flash memory may be used to emulate an EEPROM utilizing software drivers, strategic over-programming of double words in the flash memory and following the below requirement and best practices in EEPROM software drivers. 

It is required that the EEPROM emulation driver must build in fault tolerance allowing for the ability to “skip” records. In the case of an unsuccessful program, the ability to retry programming in the next available record location is required (record retirement). In the case of an unsuccessful sector erase, the ability to retire a sector is required (sector retirement). 

In addition, following are best practices for the EEPROM emulation software driver to be considered: 

- Choose a record scheme which allows for grouping of EEPROM data contents that are updated at one time such that unchanged data is not needlessly copied while minimizing record qualifier and status overhead. A variable length record scheme may be used to allow for grouping of data that is written together and limiting total record overhead. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

647 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

- Copy only the valid records during a sector change and re-constitution of EEPROM data set to avoid needless copying of data within flash memory. This avoids rebuilding the entire data set. 

- Only redundantly storing critical data which cannot be recovered in two sectors if attempting to protect against record or sector failures. 

- Load level total program/erase cycles applied to flash memory locations allocated for EEPROM emulation by using a round-robin sector scheme. 

When combining round-robin with sector retirement requirement, three or more sectors must be allocated for EEPROM emulation inclusive of extra spare sector(s). 

For details, see NXP application notes published on this topic. 

## 20.6 Initialization information 

A reset is the highest priority operation for the embedded flash memory and terminates all other operations. 

The embedded flash memory uses reset to initialize register and status fields to their default reset values. If the embedded flash memory is executing a program or erase operation (MCR[PGM] = 1 or MCR[ERS] = 1) and a reset is issued, the operation aborts and the embedded flash memory disables the high voltage logic without causing any damage to the high voltage circuits. Reset aborts all operations and forces the embedded flash memory into User mode, ready to receive accesses. 

After reset is requested, MCRS[DONE] becomes 0, and remains low during reset and reset recovery. 

At the end of reset recovery, MCRS[DONE] transitions from 0 to 1. 

After a reset completes, register reads may be performed. 

~~<mark>NOTE</mark>~~ 

Registers that require updating from UTest NVM information, or other inputs, may not read updated values until MCRS[DONE] becomes 1. 

During reset recovery, register writes are not allowed until MCRS[DONE] becomes 1 to indicate reset recovery is complete. 

~~<mark>Caution</mark>~~ 

Resetting during a program or erase operation leaves the FC blocks being programmed or erased in an indeterminate data state. This may be recovered by executing an erase on the affected blocks. 

## 20.7 Memory map and register description 

### 20.7.1 c40asf flash memory register descriptions 

The embedded flash memory map consists of a flash memory array (which includes main array space and UTest NVM space) and a region of registers associated with the programming model that enable flash memory array operation and modification. 

The address space consists of up to 6 blocks (with restrictions), and blocks can be 2 MB, 1 MB, 512 KB or 256KB in size. 

#### 20.7.1.1 c40asf_flash memory map 

FLASH base address: 402E_C000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|Module Configuration (MCR)|32|RW|00FF_0000h|
|4h|Module Configuration Status (MCRS)|32|W1C|0000_C100h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

648 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|8h|Extended Module Configuration (MCRE)|32|RO|0000_0000h|
|Ch|Module Control (CTL)|32|RW|0000_0600h|
|10h|Address (ADR)|32|RW|0000_0000h|
|14h|Program and Erase Address (PEADR)|32|RO|0000_0000h|
|20h|Alternate Module Configuration (AMCR)|32|RW|00FF_0000h|
|24h|Alternate Module Configuration Status (AMCRS)|32|W1C|0000_C100h|
|28h|Alternate Program and Erase Address (APEADR)|32|RO|0000_0000h|
|30h - 4Ch|Alternate Program Data (ADATA0 - ADATA7)|32|RW|FFFF_FFFFh|
|50h|Sector Program and Erase Hardware Lock (SPELOCK)|32|RO|FFFF_FFFFh|
|54h|Super Sector Program and Erase Hardware Lock (SSPELOCK)|32|RO|0FFF_FFFFh|
|60h|Alternate Sector Program and Erase Hardware Lock (ASPELOCK)|32|RO|FFFF_FFFFh|
|64h|Alternate Super Sector Program and Erase Hardware Lock<br>(ASSPELOCK)|32|RO|0FFF_FFFFh|
|70h|Express Sector Program and Erase Hardware Lock (XSPELOCK)|32|RO|FFFF_FFFFh|
|74h|Express Super Sector Program and Erase Hardware Lock<br>(XSSPELOCK)|32|RO|0FFF_FFFFh|
|90h|Test Mode Disable Password Check (TMD)|32|RW|0000_0000h|
|94h|UTest 0 (UT0)|32|RW|0000_0001h|
|98h - B8h|UMISRn (UM0 - UM8)|32|RW|0000_0000h|
|BCh|UMISR9 (UM9)|32|RW|0000_0000h|
|D0h|UTest Data 0 (UD0)|32|RW|0000_0000h|
|D4h|UTest Data 1 (UD1)|32|RW|0000_0000h|
|D8h|UTest Data 2 (UD2)|32|RW|0000_0000h|
|DCh|UTest Data 3 (UD3)|32|RW|0000_0000h|
|E0h|UTest Data 4 (UD4)|32|RW|0000_0000h|
|E4h|UTest Data 5 (UD5)|32|RW|0000_0000h|
|E8h|UTest Address 0 (UA0)|32|RW|0000_0000h|
|ECh|UTest Address 1 (UA1)|32|RW|0000_0000h|
|F0h|Express Module Configuration (XMCR)|32|RW|00FF_C000h|
|F4h|Express Program Address (XPEADR)|32|RO|0000_0000h|
|100h - 17Ch|Program Data (DATA0 - DATA31)|32|RW|FFFF_FFFFh|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

649 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

#### 20.7.1.2 Module Configuration (MCR) 

##### Offset 

|Register|Offset|
|---|---|
|MCR|0h|



##### Function 

~~<mark>NOTE</mark>~~ 

- A number of Module Configuration Register (MCR) bits are locked against write by other bits. These locks are discussed in relationship to each bit in this section. Simultaneously writing bits which lock each other out is also discussed in Functional description. 

- See Functional description for information about simultaneous MCR writes, and priority levels. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/020_Embedded_Flash_Memory_-c40asf-/S32K3XXRM_数据表.pdf-0650-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 PEID<br>W<br>Reset 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 0 0<br>PECIE  WDIE  PGM  ESS  ERS  EHV<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-24|Reserved|
|—||
|23-16|Program and Erase Master/Domain ID|
|PEID|This field shows the ID of the master that has started the Program or Erase sequence (as well as Array<br>Integrity and User Margin Reads). The ID is latched when the sequence has started (writing of the PEADR<br>register). Upon completion of an operation (Program (MCR[PGM] written to 0 and MCRS[PES] equals 0),<br>Erase (MCR[ERS] written to 0 and MCRS[PES] equals 0), Array Integrity (UT0[AIE] written to 0), User<br>Margin Read(UT0[AIE] written to 0)), or Program and Erase Sequence clear (MCRS[PES] cleared to 0) the<br>PEID field will return to an all ones state. See the chip-specific information for a list of Master IDs.|
|15|Program/Erase Complete Interrupt Enable|
|PECIE|PECIE provides a mechanism to trigger an interrupt request upon the assertion of the DONE status due to a<br>high voltage event (program or erase) finishing (normal, abort). If PECIE is written while not in a high voltage|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

650 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function<br>event, the interrupt will not immediately trigger, but will trigger after the next high voltage event is completed.<br>Writing (and reading) of this bit will be restricted to the master that updated the PEADR register as captured<br>in the PEID register at the start of the Program or Erase sequence.<br>See the chip-specific information for interrupt details<br>~~NOTE~~<br>0b - Interrupt request not generated when MCRS[DONE] is 1<br>1b - Interrupt request generated when MCRS[DONE] is 1|
|---|---|
|14-13<br>—|Reserved|
|12<br>WDIE|Watch Dog Interrupt Enable<br>WDIE provides a mechanism to trigger an interrupt request upon the assertion of the WDI bit on the main<br>interface. If WDIE is asserted, when WDI asserts, an interrupt from the flash will trigger to the system. The<br>interrupt from the flash will mirror exactly the WDI bit. WDIE does not affect the register bit WDI. Writing (and<br>reading) of this bit will be restricted to the master that updated the PEADR register as captured in the PEID<br>register at the start of the Program or Erase sequence.<br>See the chip-specific information for interrupt details<br>~~NOTE~~<br>0b - Watchdog interrupt not enabled<br>1b - Watchdog interrupt enabled|
|11-9<br>—|Reserved|
|8<br>PGM|Program<br>PGM is used as part of the setup for a program operation. A 0 to 1 transition of PGM after program interlock<br>write(s) is part of the program sequence. A 1 to 0 transition of PGM ends the program sequence. PGM can<br>be set while in user mode read (ERS is low and UTE is low), and after the interlock write is completed. PES<br>must also be low to enable PGM to be set.<br>PGM can be cleared only when EHV is low and DONE is high. PGM is cleared on reset. Writing (and<br>reading) of this bit will be restricted to the master that updated the PEADR register as captured in the PEID<br>register at the start of the Program or Erase sequence.<br>0b - Flash memory not executing a program sequence<br>1b - Flash memory executing a program sequence|
|7-6<br>—|Reserved|
|5<br>ESS|Erase Size Select|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

651 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function<br>ESS is used to qualify the embedded flash memory erase operation for either sector erase or block erase.<br>If ESS is selected for block erase, only the main array of that block will be erased.|
|---|---|
||Block erase is for Factory use only, under controlled conditions. See Appendix A<br>(Electrical Specifications) for more information on environmental condition requirements,<br>and cycle limit.<br>~~NOTE~~|
||If interlock write occurs to UTest sector, ESS will be locked from setting to a 1. Block Erase<br>of UTest sector is not supported, only sector erase is allowed. Erase of UTest space is not<br>allowed if sealed, although ERS can be set and a PEG error will occur in response to the<br>HV request.<br>~~NOTE~~<br>ESS can only be written to a 1 at the same time that ERS is written to a 1. If ESS is set, ESS will auto clear<br>with ERS clearing (independent of the value written to ESS). ESS can not be cleared by writing a zero. ESS<br>is cleared on reset. Writing (and reading) of this bit will be restricted to the master that updated the PEADR<br>register as captured in the PEID register at the start of the Program or Erase sequence.<br>0b - Flash memory erase is on a sector<br>1b - Flash memory erase is on a block|
|4<br>ERS|Erase<br>ERS is used as part of the setup for an erase operation. A 0 to 1 transition of ERS after an erase interlock<br>write is part of the erase sequence. A 1 to 0 transition of ERS ends the erase sequence. ERS can only be<br>set in user mode read (PGM is low and UTE is low), and after the interlock write is completed. PES must<br>also be low to enable ERS to be set.<br>ERS can be cleared only when EHV is low and DONE is high. ERS is cleared on reset. Writing (and reading)<br>of this bit will be restricted to the master that updated the PEADR register as captured in the PEID register<br>at the start of the Program or Erase sequence.<br>0b - Flash memory not executing an erase sequence<br>1b - Flash memory executing an erase sequence|
|3-1<br>|Reserved|
|—<br>0<br>EHV|Enable High Voltage<br>The EHV bit enables the embedded flash memory for a high voltage program/erase operation. EHV is<br>cleared on reset. EHV must be set after the PGM or ERS bit is set in a program or erase sequence. Writing<br>(and reading) of this bit will be restricted to the master that updated the PEADR register as captured in the<br>PEID register at the start of the Program or Erase sequence. EHV may be set, initiating a program/erase<br>under one of the following conditions:<br>• Erase (ERS = 1, PEP = 0, PES = 0, WDI = 0)<br>• Program (PGM = 1, PEP = 0, PES = 0, WDI = 0)|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

652 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||Clearing EHV while DONE is low will abort the current program/erase high voltage operation. An abort<br>causes the value of PEG to be cleared, indicating a failed program/erase; address locations being operated<br>on by the aborted operation contain indeterminate data after an abort. EHV may not be written to a 1 after<br>an abort is requested (EHV being cleared) and before DONE transitions high. EHV may not be written to a<br>1 after it is cleared as part of a program or erase cleanup, until after the next PEADR write.<br>Aborting a high voltage operation leaves addresses in an indeterminate data state. This may<br>be recovered by executing an erase on the affected sectors.<br>~~NOTE~~|
||0b - Flash memory is not enabled to perform a high voltage operation.<br>1b - Flash memory is enabled to perform a high voltage operation.|



#### 20.7.1.3 Module Configuration Status (MCRS) 

##### Offset 

|Register|Offset|
|---|---|
|MCRS|4h|



##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|EER|SBC|AEE|EEE|0||RVE|RRE||0||RWE|0||PEP|PES|
|W|W1C|W1C|W1C|W1C|||W1C|W1C||||W1C|||W1C|W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|DONE|PEG|0|WDI|0||EPEG|TSPEL<br>OCK||||0||||RE|
|W|||||||||||||||||
|Reset|1|1|0|0|0|0|0|1|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|ECC Event Error|
|EER|This bit provides information on previous reads (either user initiated reads or internally initiated reset|
||reads).If a double bit detection occurred, the EER bit is set to a '1'. This bit must then be cleared, or a reset|
||must occur before it returns to a 0 state. This bit may not be set by software. In the event of a single bit|
||detection and correction, this bit is not set. If EER is not set, or remains 0, this indicates that all previous|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

653 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function<br>reads (from the last reset, or clearing of EER) are correct. Since this bit is an error flag, it must be cleared<br>to a 0 by writing a 1 to the register location. A write of 0 has no effect.<br>0b - Reads occurring normally<br>1b - ECC error occurred during a previous read|
|---|---|
|30<br>SBC|Single Bit Correction<br>SBC provides information on previous reads, if the SBCE is set. If a single bit correction occurred, the SBC<br>bit is set to a 1. This bit must then be cleared, or a reset must occur before this bit returns to a 0 state. If<br>SBC is not set, or remains 0, this indicates that all previous reads (from the last reset, or clearing of SBC) did<br>not require a correction. Since this bit is a status flag, it must be cleared to a 0 by writing a 1 to the register<br>location. A write of 0 has no effect.<br>0b - Reads occurring without corrections<br>1b - Single bit correction occurred during a previous read|
|29<br>AEE|Address Encode Error<br>AEE provides information on previous reads monitoring the address encode feature. On every read request<br>to the flash, the incoming address is compared to an encoded address (row, column, and block) coming<br>back from the memory array using the read data sense amplifier timing. If these two values do not match<br>(zero selected, multiple selected, wrong selected), or the timing is incorrect, an address encode error will be<br>recorded. If an address encode mismatch is detected, this bit is set to indicate that previous reads requested<br>may have been corrupted. Since this bit is a status flag, it must be cleared to a 0 by writing a 1 to the register<br>location. A write of 0 has no effect.<br>0b - Reads are occurring without address encode mismatches<br>1b - Previous read may be corrupted based on address encode mismatch|
|28<br>EEE|EDC after ECC Error<br>EEE provides information on previous reads monitoring the EDC after ECC feature. On every read request<br>to the flash, ECC is recalculated serially, and if there is a mismatch between the ECC calculations (taking<br>into account corrections or detections) a late error will be reported. If an EDC after ECC mismatch is<br>detected, this bit is set to indicate that previous reads requested may have been corrupted. Since this bit is<br>a status flag, it must be cleared to a 0 by writing a 1 to the register location. A write of 0 has no effect.<br>0b - Reads are occurring without EDC after ECC mismatches<br>1b - Previous read may be corrupted based on ECC calculation errors|
|27-26<br>—|Reserved|
|25<br>RVE|Read Voltage Error<br>RVE provides information on previous reads monitoring the read voltage. If the read voltage is detected to<br>be out of range, this bit is set to indicate that previous reads requested may have been corrupted. Since this<br>bit is a status flag, it must be cleared to a 0 by writing a 1 to the register location. A write of 0 has no effect.<br>0b - Reads are occurring without voltage issues<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

654 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function<br>1b - A previous read may have been corrupted due to read voltage being out of range|
|---|---|
|24|Read Reference Error|
|RRE|RRE provides information on previous reads monitoring the read reference. If the read reference is detected<br>to be out of range, this bit is set to indicate that previous reads requested may have been corrupted. Since<br>this bit is a status flag, it must be cleared to a 0 by writing a 1 to the register location. A write of 0 has no effect.<br>0b - Reads occur without reference issues<br>1b - Previous read may be corrupted because of read reference being out of range|
|23-21<br>—|Reserved|
|20<br>RWE|Read-While-Write Event Error<br>This bit provides information on previous read-while-write (RWW) reads. If an RWW error occurs, this bit is<br>set to 1. The bit must then be cleared, or a reset must occur before it returns to a 0 state. If RWE is not set, or<br>remains 0, this indicates that all previous RWW reads (from the last reset, or clearing of RWE) are correct.<br>Since this bit is an error flag, it must be cleared to a 0 by writing a 1 to the register location. A write of 0 has<br>no effect.<br>0b - Reads occur normally<br>1b - RWW error occurred during a previous read|
|19-18<br>—|Reserved|
|17<br>PEP|Program and Erase Protection Error<br>PEP provides information about program and erase operations with respect to protection errors. A<br>protection error occurs if a program is attempted to a locked sector or super sector, or if an erase is selected<br>to a locked sector or super sector. This is evaluated prior to the operation beginning, and if an error is<br>detected, high voltage operations (either a Program or Erase) will not be attempted for this request.<br>If a location has both OTP and Lock protection, the response from the NVM will be<br>PEP=1 only.<br>~~NOTE~~<br>If PEP is asserted, it must be cleared prior to attempting another high voltage operation. Since this bit is a<br>status flag, it must be cleared to a 0 by writing a 1 to the register location. A write of 0 has no effect.<br>0b - Program and erase protection errors do not exist<br>1b - Previous program or erase protection error encountered|
|16|Program and Erase Sequence Error|
|PES|PES provides information about program and erase operations with respect to sequence errors. A sequence<br>error occurs when the program or erase sequence is not followed exactly. If an “out-of-order” event is<br>detected, PES will assert, and the remainder of the sequence will not be accepted. PES monitoring begins<br>when the PEADR register is written and ends when EHV is set to start the operation. PES monitoring<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

655 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function<br>only applies to Program and Erase (Sector and Block). It does not apply to Express Program, or UTest<br>operations. Following is a complete list of sequence error conditions:<br>• Any specific DATA register written twice.<br>• More than one DATA register write for ERS operations.<br>• Attempts to write PGM or ERS register out of sequence.<br>• Attempts to write PGM after ERS, or ERS after PGM.<br>• Attempts to write DATA registers after PGM or ERS are written.<br>• Attempts to write EHV out of sequence.<br>Writes to the MCR that are protected by the MCR Priority Levels (i.e. simultaneous PGM, ERS and EHV<br>writes) will not result in a PES condition.<br>Attempts to write MCR or DATA registers by a master that does not match the PEID, will not result in a PES<br>condition. Those reads and writes will be blocked, and the master in control of the interface may continue<br>with its' sequence.<br>Clearing of PES (due to a sequence error) has the same effect as the clearing of PGM or ERS after a<br>program or erase operation. PEADR and DATA registers are cleared, PEID is cleared, and the operation<br>must be re-started from the beginning. If PGM or ERS are already set, they must be cleared before PES is<br>cleared. PES can only be cleared once the PGM or ERS bit for the sequence in progress is cleared. Since<br>this bit is a status flag, it must be cleared to a 0 by writing a 1 to the register location. A write of 0 has no effect.<br>0b - Program and erase sequence errors do not exist<br>1b - Previous program or erase sequence encountered an error|
|---|---|
|15<br>DONE|State Machine Status<br>DONE indicates whether the embedded flash memory is performing a high voltage operation. DONE is set<br>to a 1 on termination of the embedded flash memory reset. DONE is read only. DONE is set to a 1 at the<br>end of program and erase high voltage sequences.<br>This field transitions from a 0 to 1 during reset and remains at 1 after reset.<br>~~NOTE~~<br>0b - Performing a high voltage operation<br>1b - Not executing a high voltage operation|
|14<br>PEG|Program/Erase Good<br>The value of PEG is updated automatically during the program and erase high voltage operations. Aborting<br>a program/erase high voltage operation causes PEG to be cleared, indicating the sequence failed. PEG is<br>set to a 1 when the embedded flash memory is reset. PEG is read only.<br>The value of PEG is valid only when PGM = 1 or ERS = 1 and after DONE transitions from 0 to 1 due to an<br>abort or the completion of a program/erase operation. PEG is valid until PGM/ERS makes a 1 to 0 transition<br>or EHV makes a 0 to 1 transition.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

656 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function<br>1. If program or erase operations are attempted on sector(s) that are locked, the<br>response from embedded flash memory is PEG = 1, indicating that the operation<br>was successful, and the contents of the sector(s) are properly protected from the<br>program or erase operation. PEG = 1 is also true if an abort occurs during an HV<br>request to a locked sector.<br>2. If a program or erase operation is attempted to a location marked as OTP,<br>the response from the embedded flash memory is PEG = 0, indicating that the<br>operation was not allowed. The value interlocked is not programmed, since desired<br>double word was already programmed with a previous program operation. Erase is<br>prevented on OTP locations.<br>~~NOTE~~<br>0b - Program or erase operation failed<br>1b - Program or erase operation successful|
|---|---|
|13<br>—<br>12<br>WDI|Reserved<br>Watch Dog Interrupt<br>WDI is a status register to indicate that the Watchdog Timer for Program or Erase had expired. WDI is status<br>only, and will be automatically cleared once the operation that caused the watchdog timeout is terminated or<br>clean up from the operation is completed (clearing of PGM (with PES low), ERS (with PES low) or PES bit).<br>0b - Normal Operation, Watchdog Timer has not expired.<br>1b - Program Watchdog Timer has expired.|
|11-10<br>—|Reserved|
|9<br>EPEG|ECC Enabled Program/Erase Good<br>EPEG is a qualifier to PEG to indicate if a passing program or erase required ECC Enabled verifies to pass.<br>In the event of a failed operation (PEG=0), EPEG will always remain 0. The value of EPEG is updated<br>automatically during the program and erase high voltage operations. EPEG is set to a 0 when the embedded<br>flash memory is reset. EPEG is read only.<br>The value of EPEG is valid only when PGM = 1 or ERS = 1 and after DONE transitions from 0 to 1 due to an<br>abort or the completion of a program/erase operation. EPEG is valid until PGM/ERS makes a 1 to 0 transition<br>or EHV makes a 0 to 1 transition.<br>0b - Program or erase operation did not require ECC Enabled verifies.<br>1b - Program or erase operation required ECC Enabled verifies to pass.|
|8<br>TSPELOCK|UTest NVM Program and Erase Lock<br>TSPELOCK reflects the status of the hardware program and erase protection input to the flash module.<br>The TSPELOCK register is latched on the PEADR[PEASAD] write (UTest Sector Interlock), is not writable,<br>and is status only. During high voltage events, the status is locked. When not interlocked this bit will read 1.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

657 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||The default value of the TSPELOCK bits is program and erase protected.<br>0b - Corresponding sector not locked, and may be programmed or erased<br>1b - Corresponding sector protected from the program and erase sequences|
|7-1|Reserved|
|—||
|0|Reset Error|
|RE|This bit provides information on previous resets. Checks are done within the flash and if a coherency issue<br>or ECC error is detected during the reset reads used for trimming on the flash, this status flag will assert.<br>This bit is status only, and is not writable.|
||0b - Reset occurred without errors<br>1b - Reset error encountered|



#### 20.7.1.4 Extended Module Configuration (MCRE) 

##### Offset 

|Registe|r||O|ffset|||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|MCRE|||8|h|||||||||||||
|Diagram<br>Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|R||n2M||||0||||n1M||||0|||
|W|||||||||||||||||
|Reset<br>1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|n5|12K||||0|||n2|56K|||0||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Diagram 

1. The reset value of this register is set at the factory and varies among chips. See the chip-specific c40asf information for details. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

658 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Fields 

|Field|Function|
|---|---|
|31-29|Number of 2 MB Blocks|
|n2M|000b - Zero 2 MB blocks<br>001b - One 2 MB block<br>010b - Two 2 MB blocks<br>011b - Three 2 MB blocks<br>100b - Four 2 MB blocks<br>101b - Reserved<br>110b - Reserved<br>111b - Reserved|
|28-24<br>—|Reserved|
|23-21<br>n1M|Number of 1 MB Blocks<br>000b - Zero 1 MB blocks<br>001b - One 1 MB block<br>010b - Two 1 MB blocks<br>011b - Three 1 MB blocks<br>100b - Four 1 MB blocks<br>101b - Reserved<br>110b - Reserved<br>111b - Reserved|
|20-16<br>—|Reserved|
|15-14|Number of 512 KB Blocks|
|n512K|00b - Zero 512 KB blocks|
||01b - One 512 KB block<br>10b - Two 512 KB blocks|
||11b - Four 512 KB blocks|
|13-8<br>—|Reserved|
|7-6|Number of 256 KB Blocks|
|n256K|00b - Zero 256 KB blocks<br>01b - One 256 KB block|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

659 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||10b - Two 256 KB blocks|
||11b - Four 256 KB blocks|
|5-0<br>—|Reserved|



#### 20.7.1.5 Module Control (CTL) 

##### Offset 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/020_Embedded_Flash_Memory_-c40asf-/S32K3XXRM_数据表.pdf-0660-06.png)


<!-- Start of picture text -->
Register Offset<br>CTL Ch<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>RWSL  RWSC<br>W<br>Reset 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16|Reserved|
|—||
|15|Read Wait State Lock|
|RWSL|Read Wait State Lock. The RWSL bit locks the read wait state control register (RWSC). If RWSL is set, then<br>the RWSC field can not be written. RWSL is not clearable by a register write, it is only cleared upon reset.<br>Once RWSL is written to a 1, it will remain a 1 until the next reset and RWSC will be locked from writing.<br>RWSC and RWSL are allowed to be written simultaneously. RWSL does not affect readability of RWSC.<br>0b - RWSC not locked and available for writing|
||1b - RWSC locked and unavailable for writing|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

660 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|14-13<br>—|Reserved|
|12-8<br>RWSC|Wait State Control<br>This field controls the number of wait states to be added to the best-case flash array access time for reads.<br>RWSC is only writable when RWSL is a 0. The best case flash array access time for reads is one cycle.<br>This field must be set to a value corresponding to the operation frequency of the Flash and the actual read<br>access time of the Flash to the flash boundary. Total read latency will be SoC dependant based on the<br>how the cores are coupled within the platform. The frequency information, and total latency details are<br>documented in the SoC specification.<br>Higher operating frequencies require non-zero settings for this field for proper flash operation.<br>• Updates to this configuration field that control reads must take place only when the<br>flash memory is idle. Changing configuration settings while flash memory access is in<br>progress can lead to non-deterministic behavior.<br>• Values of RWSC[4:0] not listed here are reserved.<br>~~NOTE~~|
||~~NOTE~~<br>0_0000b - Reserved<br>0_0001b - One additional wait state is added.<br>0_0010b - Two additional wait states are added.<br>0_0011b - Three additional wait states are added.<br>0_0100b - Four additional wait states are added.<br>0_0101b - Five additional wait states are added.<br>0_0110b - Six additional wait states are added.<br>0_0111b - Seven additional wait states are added.<br>0_1000b - Eight additional wait states are added.<br>0_1001b - Reserved<br>1_1111b - Reserved|
|7-0<br>—|Reserved|



#### 20.7.1.6 Address (ADR) 

##### Offset 

|Register|Offset|
|---|---|
|ADR|10h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

661 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Function 

The Address register (ADR) provides the first failing address in the event of a failure (ECC or PGM/Erase state machine), as well as single bit correction information. The address register is also writable for UTest Mode operations. The address is identified using a combination of bits that identify the memory region and offset address. 

~~<mark>NOTE</mark>~~ 

- The address given is an offset from the base address of the address space. 

- The block numbering scheme that corresponds to the offset address is based on the flash memory's internal addressing scheme, which may be different than the chip's system addressing scheme. 

Understanding the mapping between the flash address, which is specified relative to the flash module's internal addressing scheme, and the location within the chip's system memory map requires a clear understanding of the flash memory layout. See the chip-specific information for a detailed explanation of the chip's flash memory layout and how to map system addresses to the flash module's internal addressing. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/020_Embedded_Flash_Memory_-c40asf-/S32K3XXRM_数据表.pdf-0662-09.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>SAD  A5  A4  A3  A2  A1  A0  ADDR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>ADDR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|UTest NVM Address|
|SAD|Qualifies the address captured during an ECC event error, single bit correction, or state machine operation.<br>See the description of the ADDR field for more information. This field is not writeable if UTE = 1, and is<br>ignored if it's in UTest mode.<br>0b - Address captured or to be accessed is from the main array space<br>1b - Address captured or to be accessed is from the UTest NVM array space|
|30-25|Reserved|
|—|Reserved; reset to 0|
|24|Address Region 5|
|A5|Qualifies the address field (ADDR) to region 5<br>If the value of this field is 1, the ADDR field maps to region 5. See the description of the ADDR field for more<br>information. If the region is not present, this field is locked to 0.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

662 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Address captured or to be accessed is not from region 5<br>1b - Address captured or to be accessed is from region 5|
|23<br>A4|Address Region 4<br>Qualifies the address field (ADDR) to region 4<br>If the value of this field is 1, the ADDR field maps to region 4. See the description of the ADDR field for more<br>information. If the region is not present, this field is locked to 0.<br>0b - Address captured or to be accessed is not from region 4<br>1b - Address captured or to be accessed is from region 4|
|22<br>A3|Address Region 3<br>Qualifies the address field (ADDR) to region 3<br>If the value of this field is 1, the ADDR field maps to region 3. See the description for the ADDR field for more<br>information. If the region is not present, this field is locked to 0.<br>0b - Address captured or to be accessed is not from region 3<br>1b - Address captured or to be accessed is from region 3|
|21<br>A2|Address Region 2<br>Qualifies the address field (ADDR) to region 2<br>If the value of this field is 1, the ADDR field maps to region 2. See the description of the ADDR field for more<br>information. If the region is not present, this field is locked to 0.<br>0b - Address captured or to be accessed is not from region 2<br>1b - Address captured or to be accessed is from region 2|
|20<br>A1|Address Region 1<br>Qualifies the address field (ADDR) to the region<br>If the value of this field is 1, the ADDR field maps to region 1. See the description for the ADDR field for more<br>information. If the region is not present, this field is locked to 0.<br>0b - Address captured or to be accessed is not from region 1<br>1b - Address captured or to be accessed is from region 1|
|19<br>A0|Address Region 0<br>Qualifies the ADDR field to region 0. If A0 = 1, then the ADDR field maps to that region. If the region is not<br>present, this field is locked to 0. For details, see the field description for ADDR.<br>0b - Address captured or to be accessed is not from region 0<br>1b - Address captured or to be accessed is from region 0|
|18-1|Address|
|ADDR||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

663 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||The ADR register provides the first failing address in the event of ECC event error (EER set), single bit<br>correction (SBC set), as well as providing the address of a failure that may have occurred in a state machine<br>operation (PEG cleared). ECC event errors take priority over single bit corrections, which take priority over<br>state machine errors. This is especially valuable in the event of an RWW operation, where the read senses<br>an ECC error or single bit correction, and the state machine fails simultaneously. The failing address for ECC<br>event error is held until EER is cleared. The failing address for single bit correction is held until an ECC event<br>error, or until SBC is cleared. State machine address is held until an ECC event error or single bit correction<br>event occurs, or until the next state machine event (PEG cleared) occurs. This address is always a double<br>word address that selects 64 bits.<br>The ADR register is writable, and can be used in the UTest ECC Logic Test, UTest EDC after ECC Logic<br>Test, and UTest Address Encode Logic Test. If any of these tests are enabled (UT0[EIE] = 1, UT0[EDIE] =<br>1, or UT0[AEIE] = 1) then the ADR register will not update for ECC event error, single bit correction or state<br>machine errors.<br>If MCRS[EER] or MCRS[SBC] are set, the ADR register is locked from writing. MCRS[PEG] does not affect<br>the writeability of the ADR register.<br>ADDR[18:1] is an offset from a base address of 0h for each block region. The A0, A1, A2, A3, A4, and A5<br>bits qualify the block size region the ADDR field.|
|0|Reserved|
|—|Reserved; reset to 0|



#### 20.7.1.7 Program and Erase Address (PEADR) 

##### Offset 

|Register|Offset|
|---|---|
|PEADR|14h|



##### Function 

The Program and Erase Address register (PEADR) is used to provide the address to be programmed or the location of the sector or block to be erased. The program and erase address register is read only in user mode (user mode writes occur with writes done to the Platform Flash Controller). The address is identified using a combination of bits that identify the memory region and offset address. 

~~<mark>NOTE</mark>~~ 

- The address provided is an offset from the base address of the address space. 

- The block numbering scheme that corresponds to the offset address is based on the flash memory's internal addressing scheme, which may be different from the chip's system addressing scheme. 

Understanding the mapping between the flash address, which is specified relative to the flash module's internal addressing scheme, and the location within the chip's system memory map requires a clear understanding of the flash memory layout. See the chip-specific information for a detailed explanation of the chip's flash memory layout and how to map system addresses to the flash module's internal addressing. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

664 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/020_Embedded_Flash_Memory_-c40asf-/S32K3XXRM_数据表.pdf-0665-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>PEAS<br>R 0 PEA5  PEA4  PEA3  PEA2  PEA1  PEA0  PEADDR<br>AD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R PEADDR  0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|UTest NVM Program and Erase Address|
|PEASAD|Qualifies the address field (PEADDR) to the region.<br>If PESAD = 1, the PEADDR field maps to that region. See the description of the PEADDR field for<br>more information.<br>This field is not writeable if UTE = 1 and is ignored if it becomes 1 while in UTest mode.<br>0b - Address accessed is from the main array space<br>1b - Address accessed is from the UTest NVM array space|
|30-25<br>—|Reserved<br>Reserved; reset to 0|
|24<br>PEA5|Program and Erase Address Region 5<br>Qualifies the address field (PEADDR) to region 5.<br>If PEA5 = 1, the PEADDR field maps to region 5. See the description of the PEADDR field for more<br>information. If region 5 is not present, this field is locked to 0.<br>0b - Address accessed is not from region 5<br>1b - Address accessed is from region 5|
|23<br>PEA4|Program and Erase Address Region 4<br>Qualifies the address field (PEADDR) to region 4.<br>If PEA4 = 1, the PEADDR field maps to region 4. See the description of the PEADDR field for more<br>information. If region 4 is not present, this field is locked to 0.<br>0b - Address accessed is not from region 4<br>1b - Adrress accessed is from region 4|
|22|Program and Erase Address Region 3<br>Qualifies the address field (PEADDR) to region 3.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

665 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|PEA3|If PEA3 = 1, the PEADDR field maps to region 3. See the description for PEADDR for more information. If<br>region 3 is not present, this field is locked to 0.<br>0b - Address accessed is not from region 3<br>1b - Address accessed is from region 3|
|21<br>PEA2|Program and Erase Address Region 2<br>Qualifies the address field (PEADDR) to the region.<br>If PEA2 = 1, the PEADDR field maps to region 2. See the description of the PEADDR field for more<br>information. If region 2 is not present, this field is locked to 0.<br>0b - Address accessed is not from region 2<br>1b - Address accessed is from region 2|
|20<br>PEA1|Program and Erase Address Region 1<br>Qualifies the address field (PEADDR) to the region.<br>If PEA1 = 1, the PEADDR field maps to region 1. See the description of the PEADDR field for more<br>information. If region 1 is not present, this field is locked to 0.<br>0b - Address accessed is not from region 1<br>1b - Address accessed is from region 1|
|19<br>PEA0|Program and Erase Address Region 0<br>Qualifies the address field (PEADDR) to the region.<br>If PEA0 = 1, the PEADDR field maps to region 0. See the description of the PEADDR field for more<br>information. If region 0 is not present, this field is locked to 0.<br>0b - Address accessed is not from region 0<br>1b - Address accessed is from region 0|
|18-5<br>PEADDR|Program and Erase Address<br>The PEADDR register provides offset address location to be programmed or the sector to be erased in the<br>case of sector erase. This address is always a quad page address that selects 1024 bits.<br>The PEADDR register is read only in user mode and represents the flash physical address status. PEADDR<br>may be updated once (and only once) per Program or Erase event. PEADDR writes initiate a Program,<br>Erase, Array Integrity or User Margin Read request.<br>Once PEADDR is updated, it will be locked for the full program and erase operation, until MCR[PGM] or<br>MCR[ERS] is cleared at the end of the operation (as long as MCRS[PES] is zero). If MCRS[PES] is set,<br>PEADR is locked until this bit is also cleared.<br>If Express Program has been initiated (XPEADR written), the PEADR is locked from writing<br>until Express Program is completed (XPGM written to 0).<br>~~NOTE~~|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

666 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||Upon completion of an operation (Program (MCR[PGM] written to 0 and MCRS[PES] equals 0), Erase<br>(MCR[ERS] written to 0 and MCRS[PES] equals 0), Array Integrity (UT0[AIE] written to 0), User Margin<br>Read(UT0[AIE] written to 0)), or Program and Erase Sequence clear (MCRS[PES] written to 0) the PEADR<br>registers will return to an all zeros state.<br>When MCR[EHV] or UT0[AIE] are set, PEADDR bits will not be writeable.<br>Once PEADDR is updated, it will have read restrictions based on the PEID master that did the original write<br>in the Platform Flash Controller.<br>PEADDR[18:5] is an offset from a base address of 0h for each block region. The PEA0, PEA1, PEA2, PEA3,<br>PEA4 and PEA5 qualify the block size region the PEADDR field.|
|4-0|Reserved|
|—|Reserved; reset to 0|



#### 20.7.1.8 Alternate Module Configuration (AMCR) 

##### Offset 

|Register|Offset|
|---|---|
|AMCR|20h|



##### Function 

This register is accessible only from the alternate base address. Attempted access to this register is reserved from any address other than the alternate base address. See the chip-specific c40asf flash memory information for the alternate base address. 

~~<mark>NOTE</mark>~~ 

- A number of Alternate Module Configuration Register (MCR) bits are locked against write by other bits. These locks are discussed in relationship to each bit in this section. Simultaneously writing bits which lock each other out is also discussed in Functional description. 

- See Functional description for information about simultaneous MCR writes (also applies to AMCR writes), and priority levels. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/020_Embedded_Flash_Memory_-c40asf-/S32K3XXRM_数据表.pdf-0667-13.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 APEID<br>WDT  WDD<br>W<br>Reset 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 AWDI 0 0 0<br>APGM  AESS  AERS  AEHV<br>E<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

667 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Fields 

|Field<br>31-30<br>WDT|Function<br>Watch Dog Tune<br>Provides a mechanism to tune all program and erase watchdog timers (main, alternate, and express<br>program interfaces).<br>This field may not be written to if MCRS[WDI], AMCR[AWDI], or XMCR[XWDI] are 1, or if any program or<br>erase event is in progress (setup, active, or cleanup). Any master that has access toAMCRmay write or<br>read this field.<br>00b - Timeout set to 10x (400 clocks default)<br>01b - Timeout set to 5x<br>10b - Timeout set to 100x<br>11b - Timeout set to 1000x|
|---|---|
|29<br>WDD|Watch Dog Disable<br>Provides a mechanism to enable or disable all program and erase watchdog timers (main, alternate, and<br>express program interfaces).<br>This field may not become 1 if MCRS[WDI], AMCR[AWDI], or XMCR[XWDI] are 1. Any master that has<br>access toAMCRmay read or write to this field.<br>0b - Watchdog timers enabled<br>1b - Watchdog timers disabled|
|28-24<br>—|Reserved|
|23-16<br>APEID|Alternate Program and Erase Master/Domain ID<br>This field shows the ID of the master that has started the Program or Erase sequence on the alternate<br>interface. The ID is latched when the sequence has started (writing of the APEADR register). Upon<br>completion of an operation (Program (AMCR[APGM] written to 0 and AMCRS[APES] equals 0), Erase<br>(AMCR[AERS] written to 0 and AMCRS[APES] equals 0), or Program and Erase Sequence clear<br>(AMCRS[APES] cleared to 0) the APEID field will return to an all ones state. See the chip-specific<br>information for a list of Master IDs.|
|15-13<br>—|Reserved|
|12<br>AWDIE|Alternate Watch Dog Interrupt Enable<br>AWDIE provides a mechanism to trigger an interrupt request upon the assertion of the AWDI bit on the<br>alternate interface. If AWDIE is asserted, when AWDI asserts an interrupt from the flash will trigger to the<br>system. The interrupt from the flash will mirror exactly the AWDI bit. AWDIE does not affect the register bit<br>AWDI. Writing (and reading) of this bit will be restricted to the master that updated the APEADR register as<br>captured in the APEID register at the start of the Alternate Program or Alternate Erase sequence.<br>0b - Alternate Watchdog interrupt is not enabled.<br>1b - Alternate Watchdog interrupt is enabled.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

668 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|11-9<br>—|Reserved|
|8<br>APGM|Alternate Program<br>APGM is used as part of the setup for a program operation on the alternate interface. A 0 to 1 transition of<br>APGM after program interlock write(s) is part of the program sequence. A 1 to 0 transition of APGM ends<br>the program sequence. APGM can be set while in user mode read (AERS is low and UTE is low), and after<br>the interlock write is completed. APES must also be low to enable APGM to be set.<br>APGM can be cleared only when AEHV is low and ADONE is high. APGM is cleared on reset. Writing (and<br>reading) of this bit will be restricted to the master that updated the APEADR register as captured in the<br>APEID register at the start of the Program or Erase sequence.<br>0b - Flash memory not executing a program sequence<br>1b - Flash memory executing a program sequence|
|7-6<br>—|Reserved|
|5<br>AESS|Alternate Erase Size Select<br>AESS is used to qualify the embedded flash memory erase operation for either sector erase or block erase<br>on the alternate interface. If AESS is selected for block erase, only the main array of that block will be erased.<br>If interlock write occurs to UTest sector, AESS will be locked from setting to a 1. Block Erase<br>of UTest sector is not supported, only sector erase is allowed. Erase of UTest space is not<br>allowed if sealed, although AERS can be set and a APEG error will occur in response to the<br>HV request.<br>~~NOTE~~<br>AESS can only be written to a 1 at the same time that AERS is written to a 1. If AESS is set, AESS will auto<br>clear with AERS clearing (independent of the value written to AESS). AESS can not be cleared by writing a<br>zero. AESS is cleared on reset. Writing (and reading) of this bit will be restricted to the master that updated<br>the APEADR register as captured in the APEID register at the start of the Program or Erase sequence.<br>0b - Flash memory erase is on a sector<br>1b - Flash memory erase is on a block|
|4<br>AERS|Alternate Erase<br>AERS is used as part of the setup for an erase operation on the alternate interface. A 0 to 1 transition of<br>AERS after an erase interlock write is part of the erase sequence. A 1 to 0 transition of AERS ends the erase<br>sequence. AERS can only be set in user mode read (APGM is low and UTE is low), and after the interlock<br>write is completed. APES must also be low to enable AERS to be set.<br>AERS can be cleared only when AEHV is low and ADONE is high. AERS is cleared on reset. Writing (and<br>reading) of this bit will be restricted to the master that updated the APEADR register as captured in the<br>APEID register at the start of the Program or Erase sequence.<br>0b - Flash memory not executing an erase sequence<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

669 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - Flash memory executing an erase sequence|
|3-1<br>—|Reserved|
|0|Alternate Enable High Voltage|
|AEHV|The AEHV bit enables the embedded flash memory for a high voltage program/erase operation on the<br>alternate interface. AEHV is cleared on reset. AEHV must be set after the APGM or AERS bit is set in a<br>program or erase sequence. Writing (and reading) of this bit will be restricted to the master that updated the<br>APEADR register as captured in the APEID register at the start of the Program or Erase sequence. AEHV<br>may be set, initiating a program/erase under one of the following conditions:<br>• Erase (AERS = 1, APEP = 0, APES = 0, AWDI = 0)<br>• Program (APGM = 1, APEP = 0, APES = 0, AWDI = 0)<br>Clearing AEHV while ADONE is low will abort the current program/erase high voltage operation. An abort<br>causes the value of APEG to be cleared, indicating a failed program/erase; address locations being<br>operated on by the aborted operation contain indeterminate data after an abort. AEHV may not be written<br>to a 1 after an abort is requested (AEHV being cleared) and before ADONE transitions high. AEHV may not<br>be written to a 1 after it is cleared as part of a program or erase cleanup, until after the next APEADR write.<br>Aborting a high voltage operation leaves addresses in an indeterminate data state. This may<br>be recovered by executing an erase on the affected sectors.<br>~~NOTE~~|
||0b - Flash memory is not enabled to perform a high voltage operation.<br>1b - Flash memory is enabled to perform a high voltage operation.|



#### 20.7.1.9 Alternate Module Configuration Status (AMCRS) 

##### Offset 

|Register|Offset|
|---|---|
|AMCRS|24h|



##### Function 

Is accessible only from the alternate base address. 

Attempted accesses to this register are reserved from any address other than the alternate base address. See the chip-specific c40asf information for the alternate base address, 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

670 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/020_Embedded_Flash_Memory_-c40asf-/S32K3XXRM_数据表.pdf-0671-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 APEP  APES<br>W W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>ADON AEPE ATSP<br>R APEG  0 AWDI  0 0<br>E  G  ELO...<br>W<br>Reset 1 1 0 0 0 0 0 1 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-18|Reserved|
|—||
|17<br>APEP|Alternate Program and Erase Protection Error<br>APEP provides information about program and erase operations with respect to protection errors on the<br>alternate interface. A protection error occurs if a program is attempted to a locked sector or super sector, or<br>if an erase is selected to a locked sector or super sector. This is evaluated prior to the operation beginning,<br>and if an error is detected, high voltage operations (either a Program or Erase) will not be attempted for<br>this request.|
||If a location has both OTP and Lock protection, the response from the NVM will be<br>APEP=1 only.<br>~~NOTE~~<br>If APEP is asserted, it must be cleared prior to attempting another high voltage operation. Since this bit is<br>a status flag, it must be cleared to a 0 by writing a 1 to the register location. A write of 0 has no effect.<br>0b - Program and erase protection errors do not exist<br>1b - Previous program or erase protection error encountered|
|16<br>APES|Alternate Program and Erase Sequence Error<br>APES provides information about program and erase operations with respect to sequence errors on the<br>alternate interface. A sequence error occurs when the program or erase sequence is not followed exactly.<br>If an “out-of-order” event is detected, APES will assert, and the remainder of the sequence will not be<br>accepted. APES monitoring begins when the APEADR register is written and ends when AEHV is set to<br>start the operation. APES monitoring only applies to Program and Erase (Sector and Block). Following is a<br>complete list of sequence error conditions:<br>• Any specific ADATA register written twice.<br>• More than one ADATA register write for AERS operations.<br>• Attempts to write APGM or AERS register out of sequence.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

671 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function<br>• Attempts to write APGM after AERS, or AERS after APGM.<br>• Attempts to write ADATA registers after APGM or AERS are written.<br>• Attempts to write AEHV out of sequence.<br>Writes to the AMCR that are protected by the MCR Priority Levels (i.e. simultaneous APGM, AERS and<br>AEHV writes) will not result in a APES condition.<br>Attempts to write AMCR or ADATA registers by a master that does not match the APEID, will not result in<br>a APES condition. Those reads and writes will be blocked, and the master in control of the interface may<br>continue with its' sequence.<br>Clearing of APES (due to a sequence error) has the same effect as the clearing of APGM or AERS after<br>a program or erase operation. APEADR will be cleared, ADATA registers are returned to their all 1's state,<br>APEID is cleared, and the operation must be re-started from the beginning. If APGM or AERS are already<br>set, they must be cleared before APES is cleared. APES can only be cleared once the APGM or AERS bit<br>for the sequence in progress is cleared. Since this bit is a status flag, it must be cleared to a 0 by writing a<br>1 to the register location. A write of 0 has no effect.<br>0b - Program and Erase sequence errors do not exist.<br>1b - Previous program or erase sequence encountered an error.|
|---|---|
|15|Alternate State Machine Status|
|ADONE|Indicates whether the embedded flash memory is performing a high voltage operation.<br>This field becomes 1 on termination of the embedded flash memory reset. ADONE becomes 1 at the end<br>of program and erase high voltage sequences.<br>This field transitions from 0 to 1 during reset and remains 1 after reset.<br>~~NOTE~~<br>0b - Executing a high voltage operation<br>1b - Not executing a high voltage operation|
|14<br>APEG|Alternate Program/Erase Good<br>The value of APEG is updated automatically during the program and erase high voltage operations on the<br>alternate interface. Aborting a program/erase high voltage operation causes APEG to be cleared, indicating<br>the sequence failed. APEG is set to a 1 when the embedded flash memory is reset. APEG is read only.<br>The value of APEG is valid only when APGM = 1 or AERS = 1 and after ADONE transitions from 0 to 1 due<br>to an abort or the completion of a program/erase operation. APEG is valid until APGM/AERS makes a 1 to<br>0 transition or AEHV makes a 0 to 1 transition.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

672 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function<br>• If program or erase operations are attempted on sector(s) that are locked, the<br>response from embedded flash memory is APEG = 1, indicating that the operation was<br>successful, and the contents of the sector(s) are properly protected from the program<br>or erase operation. APEG = 1 is also true if an abort occurs during an HV request to a<br>locked sector.<br>• If a program or erase operation is attempted to a location marked as OTP, the response<br>from the embedded flash memory is APEG = 0, indicating that the operation was not<br>allowed. The value interlocked is not programmed because the desired double word<br>was already programmed with a previous program operation. Erase is prevented on<br>OTP locations.<br>~~NOTE~~<br>0b - Program or erase operation failed<br>1b - Program or erase operation successful|
|---|---|
|13<br>—|Reserved|
|12<br>AWDI|Alternate Watch Dog Interrupt<br>AWDI is a status register to indicate that the Watchdog Timer for Program or Erase had expired on the<br>alternate interface. AWDI is status only, and will be automatically cleared once the operation that caused the<br>watchdog timeout is terminated or clean up from the operation is completed (clearing of APGM (with APES<br>low), AERS (with APES low) or APES bit).<br>0b - Normal operation, watchdog timer not expired<br>1b - Alternate program watchdog timer expired|
|11-10<br>—|Reserved|
|9<br>AEPEG|Alternate ECC Enabled Program/Erase Good<br>AEPEG is a qualifier to APEG to indicate if a passing program or erase required ECC Enabled verifies to<br>pass. In the event of a failed operation (APEG=0), AEPEG will always remain 0. The value of AEPEG is<br>updated automatically during the program and erase high voltage operations on the alternate interface.<br>AEPEG is set to a 0 when the embedded flash memory is reset. AEPEG is read only.<br>The value of AEPEG is valid only when APGM = 1 or AERS = 1 and after ADONE transitions from 0 to 1<br>due to an abort or the completion of a program/erase operation. AEPEG is valid until APGM/AERS makes<br>a 1 to 0 transition or AEHV makes a 0 to 1 transition.<br>0b - Program or erase operation did not require ECC-enabled verifies<br>1b - Program or erase operation required ECC-enabled verifies to pass|
|8<br>ATSPELOCK|Alternate UTest NVM Program and Erase Lock<br>ATSPELOCK reflects the status of the hardware program and erase protection input to the flash module.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

673 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||The ATSPELOCK register is latched on the APEADR[APEASAD] write (UTest Sector Interlock), is not<br>writable, and is status only. During high voltage events, the status is locked. When not interlocked this bit<br>will read 1.|
||The default value of the ATSPELOCK bits is program and erase protected.|
||0b - Corresponding sector not locked and may be programmed or erased|
||1b - Corresponding sector protected from program or erase|
|7-0<br>—|Reserved|



#### 20.7.1.10 Alternate Program and Erase Address (APEADR) 

##### Offset 

|Register|Offset|
|---|---|
|APEADR|28h|



##### Function 

This register is accessible only from the alternate base address. Attempted access to this register is reserved from any address other than the alternate base address. See the chip-specific c40asf flash memory information for the alternate base address. 

~~<mark>NOTE</mark>~~ 

- The block numbering scheme that corresponds to the offset address is based on the flash memory's internal addressing scheme, which may be different than the chip's system addressing scheme. 

Understanding the mapping between the flash address, which is specified relative to the flash module's internal addressing scheme, and the location within the chip's system memory map requires a clear understanding of the flash memory layout. See the chip-specific information for a detailed explanation of the chip's flash memory layout and how to map system addresses to the flash module's internal addressing. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/020_Embedded_Flash_Memory_-c40asf-/S32K3XXRM_数据表.pdf-0674-13.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>APEA<br>R 0 APEA5 APEA4 APEA3 APEA2 APEA1 APEA0  APEADDR<br>SAD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R APEADDR  0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

674 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Fields 

|Field|Function|
|---|---|
|31<br>APEASAD|Alternate UTest NVM Alternate Program and Erase Address<br>Qualifies the address field (APEADDR) to the region.<br>If APESAD = 1, the APEADDR field maps to that region. This field is not writeable if UTE = 1, and is ignored<br>if it becomes 1 while in UTest mode. See the description of the APEADDR field for more information.<br>0b - Address accessed is from main array space<br>1b - Address accessed is from UTest NVM array space|
|30-25<br>—|Reserved<br>Reserved; reset to 0|
|24<br>APEA5|Alternate Program and Erase Address Region 5<br>Qualifies the address field (APEADDR) to the region.<br>If APEA5 = 1, the APEADDR field maps to that region. See the description of the APEADDR field for more<br>information. If this region is not present, the field is locked to 0.<br>0b - Address accessed is not from region 5<br>1b - Address accessed is from region 5|
|23<br>APEA4|Alternate Program and Erase Address Region 4<br>Qualifies the address field (APEADDR) to the region.<br>If APEA4 = 1, the APEADDR field maps to that region. See the description of the APEADDR field for more<br>information. If this region is not present, the field is locked to 0.<br>0b - Address accessed is not from region 4<br>1b - Address accessed is from region 4|
|22<br>APEA3|Alternate Program and Erase Address Region 3<br>Qualifies the address field (APEADDR) to the region.<br>If APEA3 = 1, the APEADDR field maps to that region. See the description of the APEADDR field for more<br>information. If this region is not present, the field is locked to 0.<br>0b - Address accessed is not from region 3<br>1b - Address accessed is from region 3|
|21<br>APEA2|Alternate Program and Erase Address Region 2<br>Qualifies the address field (APEADDR) to the region.<br>If APEA2 = 1, the APEADDR field maps to that region. See the description of the APEADDR field for more<br>information. If this region is not present, the field is locked to 0.<br>0b - Address accessed is not from region 2.<br>1b - Address accessed is from region 2.|
|20|Alternate Program and Erase Address Region 1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

675 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|APEA1|Qualifies the address field (APEADDR) to the region.<br>If APEA1 = 1, the APEADDR field maps to that region. See the description of the APEADDR field for more<br>information. If this region is not present, the field is locked to 0.<br>0b - Address accessed is not from region 1<br>1b - Address accessed is from region 1|
|19<br>APEA0|Alternate Program and Erase Address Region 0<br>Qualifies the address field (APEADDR) to the region.<br>If APEA0 = 1, the APEADDR field maps to that region. See the description of the APEADDR field for more<br>information. If this region is not present, the field is locked to 0.<br>0b - Address accessed is not from region 0|
||1b - Address accessed is from region 0|
|18-3|Alternate Program and Erase Address|
|APEADDR|The APEADDR register provides offset address location to be programmed or the sector to be erased in the<br>case of sector erase. This address is always a page address that selects 256 bits.<br>The APEADDR register is read only in user mode and represents the flash physical address status.<br>APEADDR may be updated once (and only once) per Program or Erase event. APEADDR writes initiate a<br>Program, Erase request on the alternate interface.<br>Once APEADDR is updated, it will be locked for the full program and erase operation, until AMCR[APGM] or<br>AMCR[AERS] is cleared at the end of the operation (as long as AMCRS[APES] is zero). If AMCRS[APES]<br>is set, APEADDR is locked until this bit is also cleared.|
||If Express Program has been initiated (XPEADR written), the APEADR is locked from<br>writing until Express Program is completed (XPGM written to 0).<br>~~NOTE~~<br>Upon completion of an operation (Program (AMCR[APGM] written to 0 and AMCRS[APES] equals 0),<br>Erase (AMCR[AERS] written to 0 and AMCRS[APES] equals 0), or Program and Erase Sequence clear<br>(AMCRS[APES] written to 0) the APEADR registers will return to an all zeros state.<br>When UT0[UTE] is set or AMCR[AEHV] is set, APEADDR bits will not be writeable.<br>Once APEADDR is updated, it will have read restrictions based on the APEID master that did the original<br>write in the Platform Flash Controller.<br>APEADDR[18:3] is an offset from a base address of 0h for each block region. The APEA0, APEA1, APEA2,<br>APEA3, APEA4 and APEA5 qualify the block size region the PEADDR field.|
|2-0<br>—|Reserved<br>Reserved; reset to 0|



20.7.1.11 Alternate Program Data (ADATA0 - ADATA7) 

Offset 

For a = 0 to 7: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

676 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

|Register<br>ADATAa|Offset<br>30h + (a × 4h)|
|---|---|



##### Function 

The ADATA registers enable data to be provided for Program. There are 8 ADATA registers to enable 256 bits of data to be programmed. 

This register is accessible only from the alternate base address. Attempted access to this register is reserved from any address other than the alternate base address. See the chip-specific c40asf flash memory information for the alternate base address. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/020_Embedded_Flash_Memory_-c40asf-/S32K3XXRM_数据表.pdf-0677-07.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>APDATA<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>APDATA<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Alternate Program Data|
|APDATA|Alternate Program Data|
||APDATA registers will reset to all ones.|
||APDATA is not writable before APEADR is written or updated to start a program operation, and will read a<br>value of all ones.|
||Once APEADR is written, all APDATA registers will be made available for writing. Writing (and reading) of<br>the APDATA registers will be restricted to the master that updated the APEADR register as captured in the<br>APEID register.|
||Upon completion of an operation (Program (AMCR[APGM] written to 0 and AMCRS[APES] equals 0),<br>Erase (AMCR[AERS] written to 0 and AMCRS[APES] equals 0) or Program and Erase Sequence clear<br>(AMCRS[APES] written to 0) the APDATA registers will return to an all ones state.<br>When AMCR[APGM], AMCR[AERS], AMCRS[APES] are set, APDATA bits will not be writeable.<br>Only APDATA Bits that are written will receive program pulses.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

677 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

#### 20.7.1.12 Sector Program and Erase Hardware Lock (SPELOCK) 

##### Offset 

|Register|Offset|
|---|---|
|SPELOCK|50h|



##### Function 

The Sector Program and Erase Lock register provides a means to protect sectors from being programed and erased on the main interface. The last 256 KB of all blocks have sector lock protection capability. The rest of the block (if applicable) is protected with super sector protection capability. This register shows the status of the pelock hardware input for the block that is interlocked. For more information on hardware program and erase protection see Program hardware locking and Erase hardware locking . 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||SPEL|OCK||||||||
|Reset|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||SPEL|OCK||||||||
|W|||||||||||||||||
|Reset|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|



##### Fields 

|Field|Function|
|---|---|
|31-0|Sector Program and Erase Lock [31:0]|
|SPELOCK|SPELOCK reflects the status of the hardware program and erase protection input to the flash module for the<br>block interlocked on the main interface.|
||The SPELOCK register is latched on the PEADR write, is not writable, and is status only. SPELOCK will<br>return back to all ones at the same time that PEADR is cleared. When not interlocked this register will read<br>all ones. During high voltage events, the status is locked.|
||The default value of the SPELOCK bits is program and erase protected. In the event that sectors are not<br>present (due to configuration or total memory size), the SPELOCK bits default to locked, and will remain 1.<br>0 - The corresponding sector is not locked, and may be programed or erased.|
||1 - The corresponding sector is protected from program or erase.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

678 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

#### 20.7.1.13 Super Sector Program and Erase Hardware Lock (SSPELOCK) 

##### Offset 

|Register|Offset|
|---|---|
|SSPELOCK|54h|



##### Function 

The Program and Erase Lock register provides a means to protect super sectors from being programed and erased on the main interface. Super Sector protection is available on block space greater than 256 KB. For 256 KB blocks, this register is not applicable. For 512 KB blocks, the first half of the block is protected with super sector granularity. For 1 MB blocks, the first 768 KB is protected with super sector granularity. For 2 MB blocks, the first 1792 KB is protected with super sector granularity. This register shows the status of the pelock hardware input for the block interlocked. For more information on hardware program and erase protection see Program hardware locking and Erase hardware locking . 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||0||||||||SSPEL|OCK||||||
|W|||||||||||||||||
|Reset|0|0|0|0|1|1|1|1|1|1|1|1|1|1|1|1|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||SSPE|LOCK||||||||
|Reset|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|



##### Fields 

|Field|Function|
|---|---|
|31-28<br>—|Reserved<br>Reserved; reset to 0|
|27-0|Super Sector Program and Erase Lock [27:0]|
|SSPELOCK|SSPELOCK reflects the status of the hardware program and erase protection input to the flash module for<br>the block interlocked on the main interface.<br>The SSPELOCK register is latched on the PEADR write, is not writable, and is status only. SSPELOCK will<br>return back to all ones at the same time that PEADR is cleared. When not interlocked this register will read<br>all ones. During high voltage events, the status is locked.<br>The default value of the SSPELOCK bits is program and erase protected. In the event that super sectors<br>are not present (due to configuration or total memory size), or super sectors not present due to block size,<br>the SSPELOCK bits default locked, and will remain 1.<br>0 - The corresponding super sector is not locked, and may be programmed or erased.<br>1 - The corresponding super sector is protected from program or erase.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

679 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

#### 20.7.1.14 Alternate Sector Program and Erase Hardware Lock (ASPELOCK) 

##### Offset 

|Register|Offset|
|---|---|
|ASPELOCK|60h|



##### Function 

The Alternate Program and Erase Lock register provides a means to protect sectors from being programed and erased on the alternate interface. The last 256 KB of all block have sector lock protection capability. The rest of the block (if applicable) is protected with super sector protection capability. This register shows the status of the pelock hardware input for the block that is interlocked. For more information on hardware program and erase protection see Program hardware locking and Erase hardware locking . 

This register is accessible only from the alternate base address. Attempted access to this register is reserved from any address other than the alternate base address. See the chip-specific c40asf flash memory information for the alternate base address. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/020_Embedded_Flash_Memory_-c40asf-/S32K3XXRM_数据表.pdf-0680-09.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R ASPELOCK<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R ASPELOCK<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Alternate Sector Program and Erase Lock [31:0]|
|ASPELOCK|ASPELOCK reflects the status of the hardware program and erase protection input to the flash module for<br>the block interlocked on the alternate interface.|
||The ASPELOCK register is latched on the APEADR write, is not writable, and is status only. ASPELOCK<br>will return back to all ones at the same time that APEADR is cleared. When not interlocked this register will<br>read all ones. During high voltage events, the status is locked.|
||The default value of the ASPELOCK bits is program and erase protected. In the event that sectors are not<br>present (due to configuration or total memory size), the ASPELOCK bits default to locked, and will remain 1.|
||0 - The corresponding sector is not locked, and may be programmed or erased.|
||1 - The corresponding sector is protected from program or erase.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

680 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

#### 20.7.1.15 Alternate Super Sector Program and Erase Hardware Lock (ASSPELOCK) 

##### Offset 

|Register|Offset|
|---|---|
|ASSPELOCK|64h|



##### Function 

The Alternate Program and Erase Lock register provides a means to protect super sectors from being programed and erased on the alternate interface. Super Sector protection is available on block space greater than 256 KB. For 256 KB blocks, this register is not applicable. For 512 KB blocks, the first half of the block is protected with super sector granularity. For 1 MB blocks, the first 768 KB is protected with super sector granularity. For 2 MB blocks, the first 1792 KB is protected with super sector granularity. This register shows the status of the pelock hardware input for the block interlocked. For more information on hardware program and erase protection see Program hardware locking and Erase hardware locking . 

This register is accessible only from the alternate base address. Attempted access to this register is reserved from any address other than the alternate base address. See the chip-specific c40asf flash memory information for the alternate base address. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/020_Embedded_Flash_Memory_-c40asf-/S32K3XXRM_数据表.pdf-0681-09.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 ASSPELOCK<br>W<br>Reset 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R ASSPELOCK<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-28|Reserved|
|—|Reserved; reset to 0|
|27-0|Alternate Super Sector Program and Erase Lock [27:0]|
|ASSPELOCK|ASSPELOCK reflects the status of the hardware program and erase protection input to the flash module for<br>the block interlocked on the alternate interface.|
||The ASSPELOCK register is latched on the APEADR write, is not writable, and is status only. ASSPELOCK<br>will return back to all ones at the same time that APEADR is cleared. When not interlocked this register will<br>read all ones. During high voltage events, the status is locked.<br>The default value of the ASSPELOCK bits is program and erase protected. In the event that super sectors<br>are not present (due to configuration or total memory size), or super sectors not present due to block size,<br>the ASSPELOCK bits default to locked, and will remain 1.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

681 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0 - The corresponding super sector is not locked, and may be programmed or erased.|
||1 - The corresponding super sector is protected from program or erase.|



#### 20.7.1.16 Express Sector Program and Erase Hardware Lock (XSPELOCK) 

##### Offset 

|Register|Offset|
|---|---|
|XSPELOCK|70h|



##### Function 

The Express Program and Erase Lock register provides a means to protect sectors from being programed and erased on the express program interface. The last 256 KB of all blocks have sector lock protection capability. The rest of the block (if applicable) is protected with super sector protection capability. This register shows the status of the pelock hardware input for the block that is interlocked. For more information on hardware program and erase protection see Program hardware locking and Erase hardware locking . 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/020_Embedded_Flash_Memory_-c40asf-/S32K3XXRM_数据表.pdf-0682-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R XSPELOCK<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R XSPELOCK<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Express Sector Program and Erase Lock [31:0]|
|XSPELOCK|XSPELOCK reflects the status of the hardware program and erase protection input to the flash module for<br>the block interlocked on the express program interface.|
||The XSPELOCK register is latched on the XPEADR write, is not writable, and is status only. XSPELOCK<br>will return back to all ones at the same time that XPEADR is cleared. When not interlocked this register will<br>read all ones. During high voltage events, the status is locked.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

682 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

|Field|Function|
|---|---|
||The default value of the XSPELOCK bits is program and erase protected. In the event that sectors are not<br>present (due to configuration or total memory size), the XSPELOCK bits default to locked, and will remain 1.|
||0 - The corresponding sector is not locked, and may be programmed or erased.|
||1 - The corresponding sector is protected from program or erase.|



#### 20.7.1.17 Express Super Sector Program and Erase Hardware Lock (XSSPELOCK) 

##### Offset 

|Register|Offset|
|---|---|
|XSSPELOCK|74h|



##### Function 

The Express Program and Erase Lock register provides a means to protect super sectors from being programed and erased on the express program interface. Super Sector protection is available on block space greater than 256 KB. For 256 KB blocks, this register is not applicable. For 512 KB blocks, the first half of the block is protected with super sector granularity. For 1 MB blocks, the first 768 KB is protected with super sector granularity. For 2 MB blocks, the first 1792 KB is protected with super sector granularity. This register shows the status of the pelock hardware input for the block interlocked. For more information on hardware program and erase protection see Program hardware locking and Erase hardware locking . 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/020_Embedded_Flash_Memory_-c40asf-/S32K3XXRM_数据表.pdf-0683-09.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 XSSPELOCK<br>W<br>Reset 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R XSSPELOCK<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-28|Reserved|
|—|Reserved; reset to 0|
|27-0|Express Super Sector Program and Erase Lock [27:0]|
|XSSPELOCK||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

683 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||XSSPELOCK reflects the status of the hardware program and erase protection input to the flash module for<br>the block interlocked on the express program interface.|
||The XSSPELOCK register is latched on the XPEADR write, is not writable, and is status only. XSSPELOCK<br>will return back to all ones at the same time that XPEADR is cleared. When not interlocked this register will<br>read all ones. During high voltage events, the status is locked.<br>The default value of the XSSPELOCK bits is program and erase protected. In the event that super sectors<br>are not present (due to configuration or total memory size), or super sectors not present due to block size,<br>the XSSPELOCK bits default to locked, and will remain 1.|
||0 - The corresponding super sector is not locked, and may be programmed or erased.|
||1 - The corresponding super sector is protected from program or erase.|



#### 20.7.1.18 Test Mode Disable Password Check (TMD) 

##### Offset 

|Register|Offset|
|---|---|
|TMD|90h|



##### Function 

Provides a means to supply a challenge password to disable the Test mode disable seal block select. 

Writes to the register have no effect except for a password challenge. Reads to this register always return 0. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/020_Embedded_Flash_Memory_-c40asf-/S32K3XXRM_数据表.pdf-0684-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>PWD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>PWD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-0|Password Challenge|
|PWD||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

684 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

#### 20.7.1.19 UTest 0 (UT0) 

##### Offset 

|Register|Offset|
|---|---|
|UT0|94h|



##### Function 

##### Provides a means to control UTest. 

UTest mode provides the ability to perform test features on the flash memory. This register is only writeable when the flash memory is put into UTest mode by writing a passcode. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/020_Embedded_Flash_Memory_-c40asf-/S32K3XXRM_数据表.pdf-0685-09.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>UTE  SBCE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 0 AID<br>RRIE  AEIE  EDIE  EIE  NAIBP  AIBPE  AISUS  MRE  MRV  AIS  AIE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|UTest Enable|
|UTE|This status bit indicates when U-Test is enabled. All bits in UT0, UM0, UM1, UM2, UM3, UM4, UM5, UM6,<br>UM7, UM8, UM9, UD0, UD1, UD2, UD3, UD4, UD5, UA0 and UA1 registers are locked when this bit is 0.<br>This bit is not writeable to a 1, but may be cleared. The reset value is 0. The method to set this bit is to<br>provide a password, and if the password matches, the UTE bit is set to reflect a status of enabled, and is<br>enabled until it is cleared by a register write. The UTE password (set UTE=1) and UTE clearing to 0 will only<br>be accepted if Program or Erase are not in progress (PEADR write through clearing of PGM/ERS/PES),<br>Alternate Program or Erase are not in progress (APEADR write through clearing of APGM/AERS/APES),<br>AI/MR Operation are not in progress (PEADR write through clearing of AIE), and an Express Program<br>operation is not in progress (XPEADR write through the clearing of XPGM). UTE can only be cleared if AID<br>= 1, MRE, AIE, EIE, EDIE, AEIE, and RRIE are all equal to 0. While successfully clearing UTE, writes to set<br>AIE, MRE, EIE, EDIE, AEIE or RRIE will be ignored. For UTE, the password F9F9_9999h must be written<br>to the UT0 register, and this must be a 32bit write.<br>0b - U-Test mode is not enabled.<br>1b - U-Test mode is enabled.|
|30|Single Bit Correction Enable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

685 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field<br>SBCE|Function<br>SBCE enables single bit correction results to be observed in SBC. ECC corrections that occur when SBCE<br>is cleared will not be logged.<br>0b - Disabled<br>1b - Enabled|
|---|---|
|29-16<br>—|Reserved<br>Reserved; reset to 0|
|15<br>RRIE|Read Reference Input Enable<br>RRIE enables the force of an error on the read reference detection circuit. This is useful in the Read<br>Reference Error check. If this bit is set, the read reference error register MCRS[RRE] will set when an<br>address match is achieved to the ADR register. RRIE is not simultaneously writable to a 1 as UTE is being<br>successfully cleared to a 0.<br>0b - Read reference input disabled<br>1b - Read reference input enabled|
|14<br>AEIE|Address Encode Invert Enable<br>AEIE enables the input register AEI to invert the address encode value received from the array, and force a<br>mismatch in the address encode comparison. This is useful in the Address Encode logic check. If this bit is<br>set, address encode information from the memory array will be inverted based on values in the AEI register<br>when an address match is achieved to the ADR register. AEIE is not simultaneously writable to a 1 as UTE<br>is being successfully cleared to a 0.<br>0b - Address encode invert is disabled<br>1b - Address encode values are inverted based on UA0[AEI]|
|13<br>EDIE|EDC after ECC Data Input Enable<br>EDIE enables the input registers EDDATA and EDDATAC to be the source of data to the EDC after ECC<br>comparator or EDC after ECC encoder. This is useful in the EDC after ECC logic check. If this bit is set,<br>data read via a BIU read request will be from the EDDATA and EDDATAC registers when an address match<br>is achieved to the ADR register. EDIE is not simultaneously writable to a 1 as UTE is being successfully<br>cleared to a 0.<br>0b - EDC after ECC data input is disabled<br>1b - Data read is from UD3[EDDATA] and UD5[EDDATAC]|
|12<br>EIE|ECC Data Input Enable<br>EIE enables the input registers EDATA and EDATAC to be the source of data to the ECC logic (instead<br>of from the memory array). This is useful in the ECC logic check. If this bit is set, data read via a BIU read<br>request will be from the EDATA and EDATAC registers when an address match is achieved to the ADR<br>register. EIE is not simultaneously writable to a 1 as UTE is being successfully cleared to a 0.<br>0b - ECC data input is disabled<br>1b - Data read is from UD0[EDATA] and UD2[EDATAC]|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

686 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|11-10<br>—|Reserved|
|9<br>NAIBP|Next Array Integrity Break Point<br>If AIBPE is set, NAIBP will be set once a single bit correction (if enabled) or double bit detection is noted<br>during the Array Integrity test. NAIBP is not writable to 1, but may be cleared to 0. Clearing NAIBP to 0, will<br>enable the Array Integrity operation to be re-started after a breakpoint is encountered. NAIPB may only be<br>cleared to 0 if both EER = 0 and SBC = 0. If the Array Integrity operation completes without encountering<br>another correction or detection, AID will be set with NAIBP remaining 0.<br>0b - Array integrity state machine is not currently at a breakpoint<br>1b - Array integrity state machine is at a breakpoint|
|8<br>AIBPE|Array Integrity Break Point Enable<br>To enable breakpoints during an array integrity test, AIBPE may be set. See NAIBP description for more<br>information about array integrity breakpoints.<br>0b - Array integrity breakpoints disabled<br>1b - Array integrity breakpoints enabled during array integrity checks|
|7<br>—|Reserved<br>Reserved; reset to 0|
|6<br>AISUS|Array Integrity Suspend<br>AISUS enables a suspend of an Array Integrity Operation. Array Integrity may be suspend by setting AISUS,<br>and resumed by clearing AISUS. AISUS is writeable to a 1 only when AID is low. AISUS is clearable to a<br>0 only when AID is high. Attempting to write AISUS and AIE on the same clock cycle will result in only AIE<br>getting written.<br>0b - Array integrity sequence not suspended.<br>1b - Array integrity sequence is suspended.|
|5<br>MRE|Margin Read Enable<br>MRE combined with MRV enables user margin reads to be done. Normal user reads are not affected by<br>MRE, although user reads while the margin read operation is ongoing are not supported. MRE is not writable<br>if AID is low, or if AISUS is high, or if NAIBP is high. MRE is not simultaneously writable to a 1 as UTE is<br>being successfully cleared to a 0.<br>0b - Margin reads are not enabled.<br>1b - Margin reads are enabled.|
|4|Margin Read Value|
|MRV|MRV selects the margin level that is being checked. Margin can be checked to an erased level (MRV=1) or to<br>a programmed level (MRV=0). In order for this value to be valid, MRE must also be set. MRV is not writable<br>if AID is low, or if AISUS is high, or if NAIBP is high.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

687 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Zero's margin reads are requested.<br>1b - One's margin reads are requested.|
|3|Reserved|
|—||
|2<br>AIS|Array Integrity Sequence<br>AIS determines the address sequence to be used during array integrity checks. The default sequence<br>(AIS = 0) is meant to replicate sequences that normal user code follows, and thoroughly checks the read<br>propagation paths. This sequence is proprietary. The alternative sequence (AIS = 1) is logically sequential.<br>It should be noted that the time to run a sequential sequence is shorter than the time to run the proprietary<br>sequence. AIS is not writeable if AIE is high.<br>0b - Array integrity sequence is proprietary sequence<br>1b - Array integrity sequence is sequential|
|1|Array Integrity Enable|
|AIE|AIE set to one starts the array integrity check done on all selected blocks. The address sequence is<br>determined by AIS, and the MISR (UM0 through UM9) can be checked after the operation is complete, to<br>determine if a correct signature has been obtained. Once an array integrity operation is requested (AIE=1),<br>it may be terminated by clearing AIE if the operation has finished (AID = 1) or aborted by clearing AIE if the<br>operation is ongoing (AID = 0). AIE is locked from writing unless an interlock write occurred (PEADR write<br>and DATA write). AIE is not simultaneously writable to a 1 as UTE is being successfully cleared to a 0.<br>0b - Array integrity checks not enabled<br>1b - Array integrity checks enabled|
|0<br>AID|Array Integrity Done<br>AID is cleared upon an array integrity check being enabled (to signify the operation is ongoing). Once<br>completed, AID is set to indicate that the array integrity check is complete. At this time the MISR (UMR<br>registers) can be checked. AID may also assert if breakpoints are enabled (AIBPE is set), an abort is<br>requested or a suspend is requested. AID cannot be written, and is status only.<br>0b - Array integrity check ongoing<br>1b - Array integrity check complete|



#### 20.7.1.20 UMISRn (UM0 - UM8) 

##### Offset 

For a = 0 to 8: 

|Register<br>UMa|Offset<br>98h + (a × 4h)|
|---|---|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

688 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Function 

Provides a means to evaluate array integrity. UM9 to UM0 are a set of multiple-input signature registers (MISRs) that hold the 289-bit MISR value as shown in the next table. 

Table 95. MISR mapping 

|UM register|MISR bits|
|---|---|
|UM0|MISR[31:0]|
|UM1|MISR[63:32]|
|UM2|MISR[95:64]|
|UM3|MISR[127:96]|
|UM4|MISR[159:128]|
|UM5|MISR[191:160]|
|UM6|MISR[223:192]|
|UM7|MISR[255:224]|
|UM8|MISR[287:256]|
|UM9|MISR[288]|



##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/020_Embedded_Flash_Memory_-c40asf-/S32K3XXRM_数据表.pdf-0689-07.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>MISR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>MISR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-0|MISR[31:0]|
|MISR|The MISR registers accumulate a signature from an array integrity event. The MISR captures all data fields,<br>as well as ECC fields, and the ECC error signal. Data (read and ECC) captured in the MISR is after the ECC<br>logic, and represents corrected data (if required).|
||The MISR can be seeded to any value by writing the MISR registers.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

689 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

|Field|Function|
|---|---|
||Writing the MISR register during an array integrity operation (including suspend or<br>breakpoint) although possible, is not recommended. A write of the MISR registers at<br>this point may alter the final signature in an unpredictable way. Writing the MISR registers<br>prior to an Array Integrity operation (to seed the MISR) is allowed.<br>~~NOTE~~|
||The MISR register provides a means to calculate a MISR during array integrity operations.<br>The MISR can be represented by the following polynomial:<br>x<sup>289</sup>+ x<sup>7</sup>+ x<sup>6</sup>+ x<sup>5</sup>+ x<sup>4</sup>+ x<sup>2</sup>+ 1<br>The MISR is calculated by taking the previous MISR value and then "exclusive ORing" the new data.<br>In addition the most significant bit (in this case it is MISR[288]), is then "exclusive ORed" into input of<br>MISR[7], MISR[6], MISR[5], MISR[4], MISR[2] and MISR[0]. The result of the "exclusive OR" is shifted left<br>on each read.<br>The MISR register is used in array integrity operations.<br>If during address sequencing, reads extend into an invalid address location (in other words, greater than the<br>maximum address for a given array size) then reads are still executed to the array, but the results from the<br>array read are not deterministic. In this instance, the MISR registers are not recalculated, and the previous<br>value is retained. Once the AIE register is cleared, the MISR register will return to an all 0's state.|



#### 20.7.1.21 UMISR9 (UM9) 

##### Offset 

|Register|Offset|
|---|---|
|UM9|BCh|



##### Function 

Provides a means to evaluate array integrity. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||||0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||0||||||||MISR|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

690 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Fields 

|Field|Function|
|---|---|
|31-1<br>—|Reserved<br>Reserved; reset to 0|
|0|MISR[288]|
|MISR|The MISR registers accumulate a signature from an array integrity event. The MISR captures all data fields,<br>as well as ECC fields, and the ECC error signal. Data (read and ECC) captured in the MISR is after the ECC<br>logic, and represents corrected data (if required).<br>The MISR can be seeded to any value by writing the MISR registers.<br>Writing the MISR register during an array integrity operation (including suspend or<br>breakpoint) although possible, is not recommended. A write of the MISR registers at<br>this point may alter the final signature in an unpredictable way. Writing the MISR registers<br>prior to an Array Integrity operation (to seed the MISR) is allowed.<br>~~NOTE~~<br>The MISR register provides a means to calculate a MISR during array integrity operations.<br>The MISR can be represented by the following polynomial:<br>x<sup>289</sup>+ x<sup>7</sup>+ x<sup>6</sup>+ x<sup>5</sup>+ x<sup>4</sup>+ x<sup>2</sup>+ 1<br>The MISR is calculated by taking the previous MISR value and then "exclusive ORing" the new data.<br>In addition the most significant bit (in this case it is MISR[288]), is then "exclusive ORed" into input of<br>MISR[7], MISR[6], MISR[5], MISR[4], MISR[2] and MISR[0]. The result of the "exclusive OR" is shifted left<br>on each read.<br>The MISR register is used in array integrity operations.<br>If during address sequencing, reads extend into an invalid address location (in other words, greater than the<br>maximum address for a given array size) then reads are still executed to the array, but the results from the<br>array read are not deterministic. In this instance, the MISR registers are not recalculated, and the previous<br>value is retained. Once the AIE register is cleared, the MISR register will return to an all 0's state.|



#### 20.7.1.22 UTest Data 0 (UD0) 

##### Offset 

|Register|Offset|
|---|---|
|UD0|D0h|



##### Function 

Provides a means to enable data to be substituted during UTest procedures. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

691 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/020_Embedded_Flash_Memory_-c40asf-/S32K3XXRM_数据表.pdf-0692-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>EDATA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>EDATA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|ECC Data [31:0]|
|EDATA|Enables checks of ECC logic by allowing data bits to be input into the ECC logic and then read out by doing<br>array reads or array integrity checks. EDATA corresponds to the 32 array bits representing word 0 of all<br>double words in the page selected inADR.|



#### 20.7.1.23 UTest Data 1 (UD1) 

##### Offset 

|Register|Offset|
|---|---|
|UD1|D4h|



##### Function 

Provides a means to enable data to be substituted during UTest procedures. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||ED|ATA||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||ED|ATA||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

692 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Fields 

|Field|Function|
|---|---|
|31-0|ECC Data [63:32]|
|EDATA|Enables checks of ECC logic by allowing data bits to be input into the ECC logic and then read out by doing<br>array reads or array integrity checks. UD0[EDATA] corresponds to the 32 array bits representing word 1 of<br>all double words in the page selected inADR.|



#### 20.7.1.24 UTest Data 2 (UD2) 

##### Offset 

|Register|Offset|
|---|---|
|UD2|D8h|



##### Function 

##### Provides a means to enable data to be substituted during UTest procedures. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||0|||ED3|ED2|ED1|ED0||||0|||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||||0|||||||EDAT|AC||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-28|Reserved|
|—||
|27|ECC Logic Check Double Word 3|
|ED3|Enables checks of ECC logic by allowing data bits to be input into the ECC logic and then read out by doing<br>array reads or array integrity checks.|
||If this field's value becomes 1, the data replacement occurs on DW3 on the page selected inADR.|
|26|ECC Logic Check Double Word 2|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

693 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|ED2|Enables checks of ECC logic by allowing data bits to be input into the ECC logic and then read out by doing<br>array reads or array integrity checks.<br>If this field's value becomes 1, the data replacement occurs on DW2 on the page selected inADR.|
|25<br>ED1|ECC Logic Check Double Word 1<br>Enables checks of ECC logic by allowing data bits to be input into the ECC logic and then read out by doing<br>array reads or array integrity checks.<br>If this field's value becomes 1, the data replacement occurs on DW1 on the page selected inADR.|
|24<br>ED0|ECC Logic Check Double Word 0<br>Enables checks of ECC logic by allowing data bits to be input into the ECC logic and then read out by doing<br>array reads or array integrity checks.<br>If this field's value becomes 1, the data replacement occurs on DW0 on the page selected inADR.|
|23-8<br>—|Reserved|
|7-0<br>EDATAC|ECC Data Check Bits [7:0]<br>Enables checks of ECC logic by allowing data bits to be input into the ECC logic and then read out by doing<br>array reads or array integrity checks.<br>This field corresponds to the eight array bits representing the check bits of all double words in the page<br>selected inADR.|



#### 20.7.1.25 UTest Data 3 (UD3) 

##### Offset 

|Register|Offset|
|---|---|
|UD3|DCh|



##### Function 

Provides a means to enable data to be substituted during UTest procedures. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

694 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/020_Embedded_Flash_Memory_-c40asf-/S32K3XXRM_数据表.pdf-0695-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>EDDATA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>EDDATA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|EDC After ECC Data [31:0]|
|EDDATA|Enables checks of EDC after ECC logic by allowing data bits to be input into the EDC after ECC logic and<br>then read out by doing array reads or array integrity checks.|
||This field corresponds to the 32 array bits representing word 0 of all double words in the page selected<br>inADR.|



#### 20.7.1.26 UTest Data 4 (UD4) 

##### Offset 

|Register|Offset|
|---|---|
|UD4|E0h|



##### Function 

Provides a means to enable data to be substituted during UTest procedures. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||EDD|ATA||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||EDD|ATA||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

695 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Fields 

|Field|Function|
|---|---|
|31-0|EDC After ECC Data [63:31]|
|EDDATA|Enables checks of EDC after ECC logic by allowing data bits to be input into the EDC after ECC logic and<br>then read out by doing array reads or array integrity checks.|
||This field corresponds to the 32 array bits representing word 1 of all double words in the page selected<br>inADR.|



#### 20.7.1.27 UTest Data 5 (UD5) 

##### Offset 

|Register|Offset|
|---|---|
|UD5|E4h|



##### Function 

Provides a means to enable data to be substituted during UTest procedures. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/020_Embedded_Flash_Memory_-c40asf-/S32K3XXRM_数据表.pdf-0696-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0<br>EDD3  EDD2  EDD1  EDD0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>EDDATAC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-28|Reserved|
|—||
|27|EDC After ECC Logic Check Double Word 3|
|EDD3|Enables checks of EDC after ECC logic by allowing data bits to be input into the EDC after ECC logic and<br>then read out by doing array reads or array integrity checks.|
||If this field's value becomes 1, the data replacement occurs on DW3 on the page selected inADR.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

696 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|26<br>EDD2|EDC after ECC Logic Check Double Word 2<br>Enables checks of EDC after ECC logic by allowing data bits to be input into the EDC after ECC logic and<br>then read out by doing array reads or array integrity checks.<br>If this field's value becomes 1, the data replacement occurs on DW2 on the page selected inADR.|
|25<br>EDD1|EDC After ECC Logic Check Double Word 1<br>Enables checks of EDC after ECC logic by allowing data bits to be input into the EDC after ECC logic and<br>then read out by doing array reads or array integrity checks.<br>If this field's value becomes 1, the data replacement occurs on DW1 on the page selected inADR.|
|24<br>EDD0|EDC After ECC Logic Check Double Word 0<br>Enables checks of EDC after ECC logic by allowing data bits to be input into the EDC after ECC logic and<br>then read out by doing array reads or array integrity checks.<br>If this field's value becomes 1, the data replacement occurs on DW0 on the page selected inADR.|
|23-8<br>—<br>7-0<br>EDDATAC|Reserved<br>EDC After ECC Data Check Bits [7:0]<br>Enables checks of EDC after ECC logic by allowing data bits to be input into the EDC after ECC logic and<br>then read out by doing array reads or array integrity checks.<br>This field corresponds to the eight array bits representing the check bits of all double words in the page<br>selected inADR.|



#### 20.7.1.28 UTest Address 0 (UA0) 

##### Offset 

|Register|Offset|
|---|---|
|UA0|E8h|



##### Function 

Provides a means to enable address to be inverted during UTest procedures. 

~~<mark>NOTE</mark>~~ 

- UTest Address 0 (UA0) and UTest Address 1 (UA1) combine to represent a 52-bit wide field, which matches the width of the address internally to the flash memory that is used for the address encode comparison. 

- Writing 1 to any one of the fields in UA0 or UA1 leads to flagging an AEE error when causing the error injection. 

- When the value of a field within the range of bits 18:3 is 1, the corresponding address signal to the flash memory controller or BIU is inverted. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

697 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||AE|I||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||AE|I||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-0|Address Encode Invert [31:0]|
|AEI|Enables checks of address encode logic by allowing address bits to be inverted into the address encode<br>compare logic, forcing a miscompare. Performing array reads on the page selected inADRallows the<br>address encode invert(s) to be active.<br>Additionally, in the event of an address encode error during normal user mode operation, the page address<br>provided to the PFC is inverted when an address encode error is encountered. AEI[18:3], which reflects the<br>page address, can be used with the Address Encode Logic Check to control this inversion feature (aligning<br>withADR). Any bit in AEI[18:3] written to a 1 also enables the inversion of the corresponding signal of that<br>address, allowing checks to be performed on the comparison logic that exists in the PFC.<br>Multiple bits in AEI[18:3] may be written to a 1, which causes these bits to miscompare on<br>the address encode comparison logic, as well as causing multiple bits to have their inversion<br>enabled as part of the address provided to the BIU.<br>~~NOTE~~|



#### 20.7.1.29 UTest Address 1 (UA1) 

##### Offset 

|Register|Offset|
|---|---|
|UA1|ECh|



##### Function 

Provides a means to enable address to be inverted during UTest procedures. 

|~~NOTE~~|
|---|



- UTest Address 0 (UA0) and UTest Address 1 (UA1) combine to represent a 52-bit wide field, which matches 

- the width of the address internally to the flash that is used for the address encode comparison. 

- Writing 1 to any one of the fields in UA0 or UA1 leads to flagging an AEE error when causing the error injection. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

698 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/020_Embedded_Flash_Memory_-c40asf-/S32K3XXRM_数据表.pdf-0699-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>AEI<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>AEI<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-20|Reserved|
|—||
|19-0|Address Encode Invert [51:32]|
|AEI|Enables checks of address encode logic by allowing address bits to be inverted into the address encode<br>compare logic, forcing a miscompare. Performing array reads on the page selected inADRallows the<br>address encode invert(s) to be active.|



#### 20.7.1.30 Express Module Configuration (XMCR) 

##### Offset 

|Register|Offset|
|---|---|
|XMCR|F0h|



##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||0||||||||XPE|ID||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|XDON<br>E|XPEG|XDOK|XWDI|XWDI<br>|0|XEPE<br>G|XPGM||||0||||XEHV|
|W|||||E||||||||||||
|Reset|1|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

699 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Fields 

|Field|Function|
|---|---|
|31-24<br>—|Reserved|
|23-16<br>XPEID|Express Program Master/Domain ID<br>This field shows the ID of the master that has started the express program sequence. The ID is latched when<br>the sequence has started (writing of the XPEADR register). It is set back to the reset value (set to all '1') when<br>the operation is completed. See the chip-specific information for a list of Master IDs.|
|15|Express State Machine Status|
|XDONE|XDONE indicates whether the embedded flash memory is performing an express program operation.<br>XDONE is set to a 1 on completion of the express program operation.<br>0b - Executing an express program operation<br>1b - Not executing an express program operation|
|14|Express Program Good|
|XPEG|The XPEG field indicates the completion status of the last flash memory express program operation. The<br>value of XPEG is updated automatically after the program operations. XPEG will be 0 if the program<br>operation failed. See MCRS[PEG] for more information, as the features of that bit apply to XPEG as well.<br>0b - Program operation failed<br>1b - Program operation successful|
|13|Express Data OK|
|XDOK|This field is a status signal from the flash to indicate that it is OK to load Data into the DATA registers. It will<br>assert in response to a XPEADR load (once ongoing operations are aborted, if required). XDOK will clear<br>once the Express Program operation is complete (XPGM written to 0).<br>0b - Flash memory not ready to accept writes to the DATA registers<br>1b - Writes to DATA registers allowed|
|12|Express Watch Dog Interrupt|
|XWDI|XWDI is a status register to indicate that the Watchdog Timer for Express Program had expired. XWDI<br>is status only, and will be automatically cleared once the operation that caused the watchdog timeout is<br>terminated or clean up from the operation is completed (clearing of XPGM bit).<br>0b - Normal Operation, Watchdog Timer has not expired.<br>1b - Express Program Watchdog Timer has expired.|
|11|Express Watch Dog Interrupt Enable|
|XWDIE|XWDIE provides a mechanism to trigger an interrupt request upon the assertion of the XWDI bit on the<br>express interface. If XWDIE is asserted, when XWDI asserts an interrupt from the flash will trigger to the<br>system. The interrupt from the flash will mirror exactly the XWDI bit. XWDIE does not affect the register bit<br>XWDI. Writing (and reading) of this bit will be restricted to the master that updated the XPEADR register as<br>captured in the XPEID register at the start of the Express Program sequence.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

700 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Express watchdog interrupt disabled<br>1b - Express watchdog interrupt enabled|
|10<br>—|Reserved|
|9<br>XEPEG|Express ECC Enabled Program Good<br>XEPEG is a qualifier to XPEG to indicate if a passing program required ECC Enabled verifies to pass. In<br>the event of a failed operation (XPEG=0), XEPEG will always remain 0. The value of XEPEG is updated<br>automatically after the program operations. See MCRS[EPEG] for more information, as the features of that<br>bit apply to XEPEG as well.<br>0b - Program operation did not require ECC-enabled verifies<br>1b - Program operation required ECC-enabled verifies to pass|
|8<br>XPGM|Express Program<br>XPGM is used as part of the setup for an express program operation.<br>A 0 to 1 transition of XPGM after program interlock write(s) is part of the setup for an express program<br>sequence. A 1 to 0 transition of XPGM ends the express program sequence.<br>XPGM can be set at any time if UT0[UTE] is low, and after the interlock write is completed (XPEADR written,<br>XDOK asserted, and DATAn register(s) written).<br>XPGM may be cleared when XEHV is low. Writing (and reading) of this bit will be restricted to the master<br>that updated the XPEADR register as captured in the XPEID register at the start of the Program sequence.<br>0b - Flash memory not executing an express program sequence<br>1b - Flash memory executing an express program sequence|
|7-1<br>—<br>0<br>XEHV|Reserved<br>Express Enable High Voltage<br>The XEHV field enables the embedded flash memory for a high voltage program/erase operation. XEHV is<br>cleared on reset. XEHV must be set after DATA writes to start an express program operation and XPGM is<br>set. This field may be set when XPGM = 1, XDOK = 1, and XWDI = 0. XEHV may not be written to a 1 after<br>it is cleared as part of an express program cleanup, until after the next XPEADR write.<br>Express Program operations may not be aborted. XEHV may only be cleared once XDONE is set to 1.<br>Writing (and reading) of this bit will be restricted to the master that updated the XPEADR register as captured<br>in the XPEID register at the start of the Program sequence.<br>0b - Flash memory is not enabled to perform an express high voltage operation.<br>1b - Flash memory is enabled to perform an express high voltage operation.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

701 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

#### 20.7.1.31 Express Program Address (XPEADR) 

##### Offset 

|Register|Offset|
|---|---|
|XPEADR|F4h|



##### Function 

The Express Program Address register (XPEADR) is used to provide the address to be programmed. The express program address register is read only in user mode (user mode writes occur with writes done to the Platform Flash Controller). The address is identified using a combination of bits that identify the memory region and offset address. 

   - ~~<mark>NOTE</mark>~~ 

- The address given is an offset from the base address of the address space. 

- The block numbering scheme that corresponds to the offset address is based on the flash memory's internal addressing scheme, which may be different than the chip's system addressing scheme. 

Understanding the mapping between the flash address, which is specified relative to the flash module's internal addressing scheme, and the location within the chip's system memory map requires a clear understanding of the flash memory layout. See the chip-specific information for a detailed explanation of the chip's flash memory layout and how to map system addresses to the flash module's internal addressing. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/020_Embedded_Flash_Memory_-c40asf-/S32K3XXRM_数据表.pdf-0702-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 XPEA5 XPEA4 XPEA3 XPEA2 XPEA1 XPEA0  XPEADDR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R XPEADDR  0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-25|Reserved|
|—|Reserved; reset to 0|
|24|Express Program Address Region 5|
|XPEA5|Qualifies the address field (XPEADDR) to the region.|
||If XPEA5 = 1, the XPEADDR field maps to that region. See the description of the XPEADDR field for more<br>information. If this region is not present, the field is locked to 0.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

702 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Address accessed is not from region 5<br>1b - Address accessed is from region 5|
|23<br>XPEA4|Express Program Address Region 4<br>Qualifies the address field (XPEADDR) to the region.<br>If XPEA4 = 1, the XPEADDR field maps to that region. See the description of the XPEADDR field for more<br>information. If this region is not present, the field is locked to 0.<br>0b - Address accessed is not from region 4<br>1b - Address accessed is from region 4|
|22<br>XPEA3|Express Program Address Region 3<br>Qualifies the address field (XPEADDR) to the region.<br>If XPEA3 = 1, the XPEADDR field maps to that region. See the description of the XPEADDR field for more<br>information. If this region is not present, the field is locked to 0.<br>0b - Address accessed is not from region 3<br>1b - Address accessed is from region 3|
|21<br>XPEA2|Express Program Address Region 2<br>Qualifies the address field (XPEADDR) to the region.<br>If XPEA2 = 1, the XPEADDR field maps to that region. See the description of the XPEADDR field for more<br>information. If this region is not present, the field is locked to 0.<br>0b - Address accessed is not from region 2<br>1b - Address accessed is from region 2|
|20<br>XPEA1|Express Program Address Region 1<br>Qualifies the address field (XPEADDR) to the region.<br>If XPEA1 = 1, the XPEADDR field maps to that region. See the description of the XPEADDR field for more<br>information. If this region is not present, the field is locked to 0.<br>0b - Address accessed is not from region 1<br>1b - Address accessed is from region 1|
|19<br>XPEA0|Express Program Address Region 0<br>Qualifies the address field (XPEADDR) to the region.<br>If XPEA0 = 1, the PEADDR field maps to that region. See the description of the XPEADDR field for more<br>information. If this region is not present, the field is locked to 0.<br>0b - Address accessed is not from region 0<br>1b - Address accessed is from region 0|
|18-5|Express Program Address|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

703 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|XPEADDR|The XPEADDR register provides offset address location to be programmed. This address is always a quad<br>page address that selects 1024 bits.<br>The XPEADDR register is read only in user mode and represents the flash physical address status.<br>XPEADDR may be updated once (and only once) per Express Program event. XPEADDR writes initiate an<br>Express Program request.<br>XPEADDR may be updated four times between reset events. Upon completing the fourth Express Program<br>request (clearing of XPGM register), the XPEADDR register will return to all zeros, and remain locked from<br>future XPEADDR updates and thus future Express Program requests will be ignored until the next reset.<br>Once XPEADDR is updated, it will be locked for the full express program operation, until XMCR[XPGM] is<br>cleared at the end of the operation.<br>Writing of XPEADDR has the effect of blocking other registers used for program and erase to be written<br>(PEADR/MCR registers as well as APEADR/APDATA/AMCR registers) until the express program operation<br>is completed.<br>Upon completion of an Express Program operation (XMCR[XPGM] written to 0) the XPEADR registers will<br>return to an all zeros state.<br>When UT0[UTE] is set or XMCR[XEHV] is set, XPEADDR bits will not be writeable.<br>Once XPEADDR is updated, it will have read restrictions based on the PEID master that did the original write<br>in the Platform Flash Controller.<br>XPEADDR[18:5] is an offset from a base address of 0h for each block region. The XPEA0, XPEA1, XPEA2,<br>XPEA3, XPEA4 and XPEA5 qualify the block size region the XPEADDR field.|
|4-0<br>—|Reserved<br>Reserved; reset to 0|



#### 20.7.1.32 Program Data (DATA0 - DATA31) 

##### Offset 

For a = 0 to 31: 

|Register<br>DATAa|Offset<br>100h + (a × 4h)|
|---|---|



##### Function 

Enables data to be provided for program (or express program). This set of 32 data registers enables 1024 bits of data to be programmed. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

704 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/020_Embedded_Flash_Memory_-c40asf-/S32K3XXRM_数据表.pdf-0705-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>PDATA<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>PDATA<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Program Data|
|PDATA|PDATA registers will reset to all ones.<br>PDATA is not writable before PEADR is written or updated to start a program, express program, erase or<br>UTest operation, and will read a value of all ones.<br>Once PEADR is written, all PDATA registers will be made available for writing. Writing (and reading) of<br>the PDATA registers will be restricted to the master that updated the PEADR register as captured in the<br>PEID register.<br>PDATA restrictions related to PEID will be disabled if UT0[UTE] is set.<br>~~NOTE~~|
||For Express Program a similar behavior exists on the PDATA registers. Once XPEADR is<br>written, and XDOK comes back as a 1, all PDATA registers will switch to all 1's (program<br>safe state) and be made available for writing (and reading) to the master's ID that matches<br>XPEID captured during the XPEADR update. In the event of an interrupted operation,<br>XPEID permissions will override PEID permissions until the express program operation is<br>completed (XPGM written to a 0).<br>~~NOTE~~<br>Upon completion of an operation (Program (MCR[PGM] written to 0 and MCRS[PES] equals 0), Erase<br>(MCR[ERS] written to 0 and MCRS[PES] equals 0), Express Program (XMCR[XPGM] written to 0), Array<br>Integrity (UT0[AIE] written to 0), User Margin Read(UT0[AIE] written to 0)) or Program and Erase Sequence<br>clear (MCRS[PES] written to 0) the PDATA registers will return to an all ones state.<br>When UT0[AIE] is set, PDATA bits will not be writeable.<br>When MCRS[PES] is set, PDATA bits will not be writeable except when an express program request occurs<br>and XMCR[XDOK] is set.<br>Also, when MCR[PGM] or MCR[ERS] are set, PDATA bits will not be writeable except when an express<br>program request occurs and XMCR[XDOK] is set. When an express program operation is in process,<br>PDATA bits will not be writeable once XMCR[XEHV] is set until XMCR[XPGM] is cleared.<br>Only PDATA Bits that are written will receive program or express program pulses.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

705 / 4640 

NXP Semiconductors 

Embedded Flash Memory (c40asf) 

## 20.8 Glossary 

|Abort|Premature end of a mode, sequence, state or operation. An abort may leave the embedded flash<br>memory in a state in which it contains indeterminate or corrupted data.|
|---|---|
|BIU|Bus interface unit(Contains all system-level customization required to make the embedded flash memory<br>part of an SoC)|
|Block|Subdivision of the Flash Module containing NVM memory bits. Block sizes range from 256KB to 2MB.<br>Each block is made up of 8KB sectors.|
|Double word|Two words, or 64 bits.|
|ECC|Error correction code(Internally used to correct single bit errors, or detect double errors within a 64-bit<br>double word.)|
|ECC segment|64 bit double word, representing the size of data used to calculate ECC information.|
|EDC|Error detection code|
|FC|Flash memory core|
|FMU|Flash Management Unit - Logic that enables program, erase, read, and other flash functions.|
|Interlock Write|A write to the PEADR register followed by a write to any DATA register performed while initiating a<br>program, erase, array integrity, or user margin read sequence. Interlock in cleared once the operation is<br>finished by clearing the appropriate control bit, causing PEADR register to clear.|
|MCU|Microcontroller unit|
|Module|Flash memory instance that contains flash block(s), FMU, and required analog support structures.|
|NVM|Nonvolatile memory|
|OTP|One time programmable|
|PFC|Platform flash memory controller(Contains all system-level customization required to make the<br>embedded flash memory part of an SoC)|
|Page|8 words of data (256 bits). When doing reads to the embedded flash memory, this is the width of data<br>read. Up to 4 pages can be programmed at a time.|
|Partition|Subdivision of the Flash Module. Used for read-while-write operation, where addresses in the partition<br>being written may not be read. Partitions is always equal to 1 block, and contains multiple sectors.|
|RWW|Read-while-write (operation)|
|Sector|Subdivision of the Flash Block that is independently erasable. Sector Size is always 8 KB.|
|Super sector|Subdivision of the flash block that includes a group of sectors. Super Sector Size is always 64 KB, and<br>consists of 8 sectors.|
|SoC|System-on-chip|
|UTest NVM sector <br>Word|8 KB sector outside the main address space<br>32 bits|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

706 / 4640 

