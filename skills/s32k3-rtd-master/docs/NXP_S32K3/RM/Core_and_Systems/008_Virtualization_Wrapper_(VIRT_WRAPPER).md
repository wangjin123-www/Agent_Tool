NXP Semiconductors 

# Chapter 8 Virtualization Wrapper (VIRT_WRAPPER) 

## 8.1 Chip-specific VIRT_WRAPPER information 

### 8.1.1 System overview of PDAC scheme 

This figure shows the interaction of XRDC (containing PDACs), related to different cores (domain IDs), with VIRT_WRAPPER. 

~~<mark>NOTE</mark>~~ Cortex-M7_1 is present only in S32K32x devices. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/008_Virtualization_Wrapper_-VIRT_WRAPPER-/S32K3XXRM_数据表.pdf-0123-06.png)


<!-- Start of picture text -->
Typical cores assignment<br>using XRDC in software<br>Cortex-M7_2 Cortex-M7_2 domain ID = IDD PDAC4 ConfigD<br>32 KB<br>Cortex-M7_1 domain ID = IDC ConfigC<br>Cortex-M7_1 PDAC2<br>32 KB<br>SIUL2<br>Cortex-M7_0 domain ID = IDB ConfigB<br>Cortex-M7_0 PDAC1<br>32 KB<br>HSE_B domain ID = IDA ConfigA<br>HSE_B PDAC0<br>32 KB<br>HSE_B and/or other domain ID<br>PDAC3<br>Config A, B, C and D (write only)<br>16 KB<br>XRDC<br>Write access to SIUL2 registers allowed through PDAC0-2,4<br> (ConfigA..C,D) after VIRT_WRAPPER is configured<br>Write access to all SIUL2 registers allowed prior<br>VIRT_WRAPPER is configured<br>Write access to VIRT_WRAPPER configuration registers only<br>S32K358<br>S32K342(4)<br>REG_PROT<br>VIRT_WRAPPER<br>S32K311(2)<br><!-- End of picture text -->

Figure 14. System overview of PDAC scheme 

### 8.1.2 Initial VIRT_WRAPPER operation 

Initially, VIRT_WRAPPER: 

- Protects the "ConfigB-C" paths to SIUL2. You must configure VIRT_WRAPPER to define the SIUL2 R/W control registers that you can access through the "ConfigB-C" VIRT_WRAPPER access paths. 

- Does not protect the direct path to SIUL2. It allows write accesses to all the SIUL2 R/W control registers. If PDAC0 is set to allow write access only to master core, for example HSE-B core (variant supported by the chip), then other masters cannot program the SIUL2 register. However, if these non-HSE_B masters program SIUL2 registers using other PDAC slots, a transfer error occurs. Any core can act as master core. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

123 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

- Protects the "ConfigB-D" paths to SIUL2. You must configure VIRT_WRAPPER to define the SIUL2 R/W control registers that you can access through the "ConfigB-D" VIRT_WRAPPER access paths. 

### 8.1.3 Additional VIRT_WRAPPER details 

See the "SIUL2 memory map overview and protection" table, later in this chapter, for an overview of the SIUL2 registers and their protection attributes. 

By default, any core can access SIUL2 registers through PDAC0. This process is called ANY_MASTER. However, after XRDC configuration, HSE_B: 

- Assigns PDACs to the respective cores or domain IDs 

- Locks the XRDC configuration 

- Programs VIRT_WRAPPER registers for pad assignments 

HSE_B accesses PDAC0 solely for the pads having 11b as the value in their corresponding registers. Also, HSE_B retains the same value for the pads that it stores. In case HSE_B needs to take control of some pins, it can still configure PDACn to be accessible not only from a specific core master, but also from HSE_B, before it allows other cores to execute. 

PDAC3 protects the IPS register portal of VIRT_WRAPPER configuration registers that any master can access but only via the memory slot assigned to PDAC3. The configuration via IPS register portal can be locked to prevent any further changes until the next functional reset. PDAC3 implements this locking. 

The protection information of the parallel port output registers is inherited from the protection information of the included pads, according to these rules: 

- When all the pads assigned to a GPIO port share the same protection information, the corresponding parallel port output register for this port inherits the same protection information. 

- When at least one of the pads assigned to a GPIO port has different protection information than the other pads assigned to this GPIO port, access to the corresponding parallel port output register for this port is disabled for all the masters. Because of the aforementioned protection group mapping, the data bits of a register encode the protection control information related to one full GPIO port, or a chunk of 16 pads. 

- You can assign the following SIUL2 registers to individual PDAC control: 

   - DISR0 

   - DIRER0 

   - DIRSR0 

   - IREER0 

   - IFEER0 

   - IFER0 

   - IFMCR0–31 

   - IFCPR 

Then, you can access all these registers only through the assigned PDAC because the VIRT_WRAPPER_REG_C1039_1024 register controls the SIUL2 interrupt registers. 

- You cannot access the SIUL2 R/W control registers configured through PDAC3 to be accessible through the ConfigA VIRT_WRAPPER access path, using the ConfigB VIRT_WRAPPER access path. 

- You cannot access any of the SIUL2 R/W control registers through ConfigB-C VIRT_WRAPPER access paths prior to VIRT_WRAPPER configuration. By default, any core can access SIUL2 registers through PDAC0 after reset. 

- The same PDAC that accesses the main SIUL2 registers is used to access the SIUL2-mirrored registers and soft-lock-bit registers. This is because these registers are a part of the same 16 KB space. 

- Access to mirrored SIUL2 registers sets the bit in Soft lock bit as an inherent property of register protection. See the "Register Protection" chapter for details on the soft lock bit behavior, when accessing the mirrored region. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

124 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

- You cannot access any of the SIUL2 R/W control registers through ConfigB-D VIRT_WRAPPER access paths prior to VIRT_WRAPPER configuration. By default, any core can access SIUL2 registers through PDAC0 after reset. 

## 8.2 Introduction 

Virtualization refers to the various techniques, methods, or approaches of creating a virtual (rather than actual) version of something, such as a virtual hardware platform, operating system (OS), storage device, or network resources. The term "hardware virtualization" refers to the creation of a virtual machine that acts like a real computer with an operating system. The underlying hardware resources separate the software executed on these virtual machines (named "guest program"). In many cases, the specifically modified guest programs are required to run in such a virtual environment. 

There are different types of hardware virtualization. One of them is para-virtualization. The para-virtualization is a non-simulated hardware environment. However, a guest program is executed in its own isolated domain, as if it is running on a separate system. Such a behavior is especially beneficial for the software targeted toward functional safety, because it allows freedom of interference for certain aspects of this software. 

The hardware-assisted virtualization is a way of improving the efficiency of hardware virtualization. It involves employing specially designed CPUs and hardware components that help improve the performance of a guest environment. VIRT_WRAPPER, described in this chapter, is such a hardware component. 

### 8.2.1 Overview 

Virtualization is implemented by protecting (for example, granting or inhibiting) the access to a register within the virtualized module, dependent on the specific criteria. Virtualized module is the module instance associated with VIRT_WRAPPER. In this chip, SIUL2 is the virtualized module. Registers within virtualized module are virtualized by granting or inhibiting the access to different PDAC slots as encoded within virtualization pad assignments in VIRT_WRAPPER configuration registers. For this purpose, the virtualization information is programmed into VIRT_WRAPPER configuration registers that specify the grouping of registers within the virtualized module. Upon an access to virtualized module through the peripheral interface, the grouping information is exercised to identify whether the corresponding transaction should be granted or inhibited. The following figure depicts the usage of VIRT_WRAPPER in combination with the virtualized module. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/008_Virtualization_Wrapper_-VIRT_WRAPPER-/S32K3XXRM_数据表.pdf-0125-09.png)


<!-- Start of picture text -->
Peripheral bus (for VIRT_WRAPPER)<br>Protection setup<br>information<br>Address Access Peripheral<br>Peripheralbus space allowed? enable<br>Register<br>grouping<br>Grant/inhibit<br>Virtualized<br>module (VM)<br><!-- End of picture text -->

Figure 15. VIRT_WRAPPER block diagram 

### 8.2.2 Features 

VIRT_WRAPPER includes these features: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

125 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

- A programmable chip-specific virtualization setup, capable to select a subset of the available masters in combination with up to four available address spaces 

- Virtualizing accesses to the registers within a VM by inhibiting accesses to a subset of these registers under control of the specified virtualization information. Only write accesses can be inhibited for a specific master or set of masters. 

### 8.2.3 Modes of operation 

VIRT_WRAPPER is operable when the VM is operable. For details about the availability of the VM, see the chapter of the corresponding module. When there is no virtualization information specified for the VIRT_WRAPPER module, if XRDC is not configured, PDAC slot 0 is open as the default value of configuration register is 11b that is assigned with PDAC slot 0 and any master can access through it. 

## 8.3 Functional description 

This section describes the following topics: 

- PDAC-based protection scheme 

- Register group mapping considering SIUL2 

- Access errors 

### 8.3.1 PDAC-based protection scheme 

VIRT_WRAPPER uses a protection scheme of the PDACs sub-blocks of XRDC. Each PDAC slot is assigned to one or more cores (by domain ID assignment in XRDC) as shown in Chip-specific VIRT_WRAPPER information section. Only the write accesses are protected by the virtualization feature. Read accesses are not impacted. 

For any protection group defined within the register, two bits specify the protection control information according to the following table. 

Table 33. Protection control information for a single group 

|Value|Mnemonic|Protection|Description|
|---|---|---|---|
|00|PDAC1|Restricted access of registers,<br>MSCR, IMCR, to PDAC slot 1|Protection setup information for PDAC slot 1 is used.|
|01|PDAC2|Restricted access of registers,<br>MSCR, IMCR, to PDAC slot2|Protection setup information for PDAC slot 2 is used.|
|10|PDAC3|Restricted access of registers,<br>MSCR, IMCR, to PDAC slot 3|Protection setup information for PDAC slot 3 is used.|
|11|PDAC0|By default, any core can access<br>SIUL2 registers through PDAC<br>slot 0. This process is called<br>ANY_MASTER.|Protection setup information for PDAC slot 0 is used.|



### 8.3.2 Register group mapping for SIUL2 

For the SIUL2 instance, the corresponding virtualization information within the VIRT_WRAPPER module is defined on a per-pad basis. Additionally, the virtualization information protects the control registers (controlling the input multiplexing scheme). 

#### 8.3.2.1 Virtualization of pad output registers 

Any functional pad (controlled by the SIUL2 instance) is assigned to a separate protection group. This scheme excludes the pads that a MSCR register does not control within an SIUL2 instance (for example, power supply pads). As a result, the protection granularity defined by the virtualization information is a single pad. The control information associated with this protection group affects all the registers related to this pad. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

126 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

The protection control information for pad i is specified within the protection group i; thus, it enables a very simple assignment scheme for the related protection control data that is hard-coded. The protection control information for pad i affects all the registers related to this pad, in the MSCRi and the GPDOi registers (in case such registers exist). 

SIUL2 can control up to 512 pads that the MSCR, GPDO, and GPDI registers can access individually. The actual number of pads associated with a SIUL2 instance is specific to implementation. GPIO pads are also organized in GPIO ports consisting of a maximum of 16 pads that the parallel port registers (PGPDO, PGPDI, MPGPDO) can access. 

Only the pad control and pad output registers are protected. Accesses to the read-only registers GPDI and PGPDI are not affected by virtualization. 

As the protection granularity is a single pad, any virtualization information associated with this pad affects the corresponding MCSR and GPDO registers directly. 

The parallel port output registers (PGPDO, MPGPDO) inherit the protection information from the protection information of the included pads according to the following rules: 

- When all pads assigned to a GPIO port share the same protection information, the corresponding parallel port output register for this port inherits the same protection information. 

- When at least one of the pads assigned to a GPIO port has a different protection information than the other pads assigned to this GPIO port, the write access to the corresponding parallel port output register (PGPDO and MPGPDO) for this port is disabled for all the masters through all the PDAC slots and a transfer error is generated. 

Due to the aforementioned protection group mapping, the data bits of a register encode the protection control information related to one full GPIO port, or a chunk of 16 pads. 

#### 8.3.2.2 Virtualization of input multiplexing control registers 

Additionally, the SIUL2 instance supports the control of an input multiplexer (INMUX) scheme. This scheme provides the capability to select one of a set of the input pads to be the source of an input function for some of the peripheral modules. Any INMUX controlled by the SIUL2 instance is assigned to a separate protection group. It therefore provides an equivalent protection granularity within the virtualization information. 

The protection group 512+i specifies the protection control information for the input multiplexer INMUX i. This enables a very simple assignment scheme for the related protection control data that is hard-coded. The protection control information for INMUX i affects the input multiplexing control register related to this input—namely, IMCRi. 

SIUL2 can control up to 512 MSCRs and 512 IMCRs input multiplexers that the IMCRs can access individually. GPIO inputs are not affected by the input multiplexer scheme. Therefore, the associated virtualization information does not affect the corresponding pad input registers. 

As the protection granularity is a single INMUX, any virtualization information associated with this INMUX affects the corresponding IMCR directly. 

#### 8.3.2.3 Virtualization of interrupt control registers 

Additionally, the complete set of interrupt control registers within SIUL2 (address offset range 0010h–00C3h) can be protected as a separate group (protection group #1024). 

The following table shows an overview of the SIUL2 registers and their protection attributes. 

Table 34. SIUL2 memory map overview and protection 

|Offset range|Register|Size<br>(bits)|Protected|Description|
|---|---|---|---|---|
|0000–000Fh|MIDR1, MIDR2|32|N|Read-only registers, not protected|
|0010–00C3h|Interrupt registers|32|Y|Protected as a single group—no individual protection<br>of related registers|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

127 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table 34. SIUL2 memory map overview and protection (continued) 

|Offset range|Register|Size<br>(bits)|Protected|Description|
|---|---|---|---|---|
|0240–A3Fh<sup>1</sup>|MSCR|32|Y|Amount of registers defines maximum number of<br>PADs to be controlled and protected|
|0A40–0123Fh|IMCR|32|Y|Amount of registers defines maximum number of<br>INMUXes to be controlled and protected|
|1300–14FFh|GPDO GPDO[0] (8-<br>bit) register controls<br>single PAD[0] pad<br>means that if PAD[0]<br>is assigned to PDAC<br>slot 1 then PDAC<br>slot 1 can write to<br>GPDO[0] (8-bit).|8|Y|There are fewer GPDO registers than MSCR registers,<br>as some PADs are not made available as GPIO<br>PADs, but their electrical characteristics can still be<br>programmed|
|1500–16FFh|GPDI|8|N|PAD input register, not protected|
|1700–173Fh|PGPDO PGPDO[0]<br>(16-bit) register<br>controls PAD[0-15]<br>pads meaning if only<br>all the PADs[0-15]<br>are assigned to<br>PDAC slot 1, then<br>PDAC slot 1 can<br>write to PGPDO[0]<br>(16-bit).|16|Y|Writable with 8-, 16-, and as a pair with 32-bit<br>accesses|
|1740–177Fh|PGPDI|16|N|PAD input register, not protected|
|1780–17FFh|MPGPDO<br>MPGPDO[0] (32-bit)<br>register controls<br>PAD[0-15] pads<br>meaning if only all<br>the PADs[0-15] are<br>assigned to PDAC<br>slot 1, then PDAC<br>slot 1 can write<br>to MPGPDO[0] (32-<br>bit).|32|Y|Only writable with 32-bit accesses|
|2010–20C3h|Reserved|—|—|—|
|2240–2A3Fh|Reserved|—|—|—|
|2A40–323Fh|Reserved|—|—|—|
|3300–34FFh|Reserved|—|—|—|
|4000–47FFh|Reserved|—|—|—|
|4800–48FFh|Reserved|—|—|—|



1. The SIUL2 block guide specifies the support of a maximum of 512 MSCRs. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

128 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

## 8.4 VIRT_WRAPPER memory map register descriptions 

~~<mark>NOTE</mark>~~ 

Access to reserved spaces outside the register bank and holes (unimplemented registers) within register bank generates the transfer error. Access to offset 104h does not generate any transfer error. 

### 8.4.1 VIRT_WRAPPER memory map 

VIRT_WRAPPER base address: 402A_8000h 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|0h - 4h|Parameter_n Register (REG_A0 - REG_A1)|32|RW|FFFF_FFFFh|
|8h|Parameter_n Register (REG_A2)|32|RW|FFFF_FFFFh|
|Ch - 34h|Parameter_n Register (REG_A3 - REG_A13)|32|RW|FFFF_FFFFh|
|38h|Parameter_n Register (REG_A14)|32|RW|FFFF_FFFFh|
|80h|Parameter_n Register (REG_B0)|32|RW|FFFF_FFFFh|
|84h - 8Ch|Parameter_n Register (REG_B1 - REG_B3)|32|RW|FFFF_FFFFh|
|90h|Parameter_n Register (REG_B4)|32|RW|FFFF_FFFFh|
|94h|Parameter_n Register (REG_B5)|32|RW|FFFF_FFFFh|
|98h|Parameter_n Register (REG_B6)|32|RW|FFFF_FFFFh|
|9Ch|Parameter_n Register (REG_B7)|32|RW|FFFF_FFFFh|
|A0h|Parameter_n Register (REG_B8)|32|RW|FFFF_FFFFh|
|A4h|Parameter_n Register (REG_B9)|32|RW|FFFF_FFFFh|
|A8h - ACh|Parameter_n Register (REG_B10 - REG_B11)|32|RW|FFFF_FFFFh|
|B0h|Parameter_n Register (REG_B12)|32|RW|FFFF_FFFFh|
|B4h|Parameter_n Register (REG_B13)|32|RW|FFFF_FFFFh|
|B8h - BCh|Parameter_n Register (REG_B14 - REG_B15)|32|RW|FFFF_FFFFh|
|C0h|Parameter_n Register (REG_B16)|32|RW|FFFF_FFFFh|
|C8h|Parameter_n Register (REG_B18)|32|RW|FFFF_FFFFh|
|CCh|Parameter_n Register (REG_B19)|32|RW|FFFF_FFFFh|
|D0h|Parameter_n Register (REG_B20)|32|RW|FFFF_FFFFh|
|D4h|Parameter_n Register (REG_B21)|32|RW|FFFF_FFFFh|
|D8h|Parameter_n Register (REG_B22)|32|RW|FFFF_FFFFh|
|DCh|Parameter_n Register (REG_B23)|32|RW|FFFF_FFFFh|
|E0h|Parameter_n Register (REG_B24)|32|RW|FFFF_FFFFh|
|E4h|Parameter_n Register (REG_B25)|32|RW|FFFF_FFFFh|
|E8h|Parameter_n Register (REG_B26)|32|RW|FFFF_FFFFh|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

129 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|ECh|Parameter_n Register (REG_B27)|32|RW|FFFF_FFFFh|
|100h|Parameter_n Register (REG_C1039_1024)|32|RW|FFFF_FFFFh|



### 8.4.2 Parameter_n Register (REG_A0 - REG_A1) 

##### Offset 

|Register|Offset|
|---|---|
|REG_A0|0h|
|REG_A1|4h|



##### Function 

This register set is for PAD0-511. They control MSCR, GPDO, PGPDO, and MPGPDO. Two bits assigned per PDAC slot have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

~~<mark>NOTE</mark>~~ 

- Any master can access holes (unimplemented registers) of SIUL2 through PDAC0. 

- After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/008_Virtualization_Wrapper_-VIRT_WRAPPER-/S32K3XXRM_数据表.pdf-0130-17.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>PAD_15  PAD_14  PAD_13  PAD_12  PAD_11  PAD_10  PAD_9  PAD_8<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>PAD_7  PAD_6  PAD_5  PAD_4  PAD_3  PAD_2  PAD_1  PAD_0<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

130 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

##### Fields 

|Field|Funct|ion|
|---|---|---|
|31-30|PAD_|15|
|PAD_15||00 - SIUL2_VIRTWRAPPER_PDAC1|
|||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|29-28|PAD_|14|
|PAD_14||00 - SIUL2_VIRTWRAPPER_PDAC1|
|||01 - SIUL2_VIRTWRAPPER_PDAC2|
|||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|27-26|PAD_|13|
|PAD_13||00 - SIUL2_VIRTWRAPPER_PDAC1|
|||01 - SIUL2_VIRTWRAPPER_PDAC2|
|||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|25-24|PAD_|12|
|PAD_12||00 - SIUL2_VIRTWRAPPER_PDAC1|
|||01 - SIUL2_VIRTWRAPPER_PDAC2|
|||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|23-22|PAD_|11|
|PAD_11||00 - SIUL2_VIRTWRAPPER_PDAC1|
|||01 - SIUL2_VIRTWRAPPER_PDAC2|
|||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|21-20|PAD_|10|
|PAD_10||00 - SIUL2_VIRTWRAPPER_PDAC1|
|||01 - SIUL2_VIRTWRAPPER_PDAC2|
|||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|19-18|PAD_|9|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

131 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|PAD_9|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|17-16|PAD_8|
|PAD_8|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|15-14|PAD_7|
|PAD_7|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|13-12|PAD_6|
|PAD_6|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|11-10|PAD_5|
|PAD_5|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|9-8|PAD_4|
|PAD_4|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|7-6|PAD_3|
|PAD_3|00 - SIUL2_VIRTWRAPPER_PDAC1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

132 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|5-4|PAD_2|
|PAD_2|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|3-2|PAD_1|
|PAD_1|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|1-0|PAD_0|
|PAD_0|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|



### 8.4.3 Parameter_n Register (REG_A2) 

##### Offset 

|Register|Offset|
|---|---|
|REG_A2|8h|



##### Function 

This register set is for PAD0-511. They control MSCR, GPDO, PGPDO, and MPGPDO. Two bits assigned per PDAC slot have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

133 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

~~<mark>NOTE</mark>~~ 

- Any master can access holes (unimplemented registers) of SIUL2 through PDAC0. 

- After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/008_Virtualization_Wrapper_-VIRT_WRAPPER-/S32K3XXRM_数据表.pdf-0134-06.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>PAD_15  PAD_14  PAD_13  PAD_12  PAD_11  PAD_10  PAD_9  PAD_8<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>Reserved  Reserved  PAD_5  PAD_4  PAD_3  PAD_2  PAD_1  PAD_0<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-30|PAD_15|
|PAD_15|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|29-28|PAD_14|
|PAD_14|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|27-26|PAD_13|
|PAD_13|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|25-24|PAD_12|
|PAD_12|00 - SIUL2_VIRTWRAPPER_PDAC1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

134 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Funct|ion|
|---|---|---|
|||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|23-22|PAD_|11|
|PAD_11||00 - SIUL2_VIRTWRAPPER_PDAC1|
|||01 - SIUL2_VIRTWRAPPER_PDAC2|
|||10 - SIUL2_VIRTWRAPPER_PDAC4|
|||11-SIUL2_VIRTWRAPPER_PDAC0|
|21-20|PAD_|10|
|PAD_10||00 - SIUL2_VIRTWRAPPER_PDAC1|
|||01 - SIUL2_VIRTWRAPPER_PDAC2|
|||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|19-18|PAD_|9|
|PAD_9||00 - SIUL2_VIRTWRAPPER_PDAC1|
|||01 - SIUL2_VIRTWRAPPER_PDAC2|
|||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|17-16|PAD_|8|
|PAD_8||00 - SIUL2_VIRTWRAPPER_PDAC1|
|||01 - SIUL2_VIRTWRAPPER_PDAC2|
|||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|15-14<br>—|Rese|rved|
|13-12<br>—|Rese|rved|
|11-10|PAD_|5|
|PAD_5||00 - SIUL2_VIRTWRAPPER_PDAC1|
|||01 - SIUL2_VIRTWRAPPER_PDAC2|
|||10 - SIUL2_VIRTWRAPPER_PDAC4|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

135 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Funct|ion<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|---|---|---|
|9-8|PAD_|4|
|PAD_4||00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|7-6|PAD_|3|
|PAD_3||00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|5-4|PAD_|2|
|PAD_2||00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|3-2|PAD_|1|
|PAD_1||00 - SIUL2_VIRTWRAPPER_PDAC1|
|||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|1-0|PAD_|0|
|PAD_0||00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2|
|||10 - SIUL2_VIRTWRAPPER_PDAC4|
|||11-SIUL2_VIRTWRAPPER_PDAC0|



### 8.4.4 Parameter_n Register (REG_A3 - REG_A13) 

Offset 

For a = 3 to 13: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

136 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

|Register|Offset|
|---|---|
|REG_Aa|0h + (a × 4h)|



##### Function 

This register set is for PAD0-511. They control MSCR, GPDO, PGPDO, and MPGPDO. Two bits assigned per PDAC slot have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

~~<mark>NOTE</mark>~~ 

- Any master can access holes (unimplemented registers) of SIUL2 through PDAC0. 

- After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/008_Virtualization_Wrapper_-VIRT_WRAPPER-/S32K3XXRM_数据表.pdf-0137-13.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>PAD_15  PAD_14  PAD_13  PAD_12  PAD_11  PAD_10  PAD_9  PAD_8<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>PAD_7  PAD_6  PAD_5  PAD_4  PAD_3  PAD_2  PAD_1  PAD_0<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-30|PAD_15|
|PAD_15|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|29-28|PAD_14|
|PAD_14|00 - SIUL2_VIRTWRAPPER_PDAC1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

137 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Funct|ion|
|---|---|---|
|||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|27-26|PAD_|13|
|PAD_13||00 - SIUL2_VIRTWRAPPER_PDAC1|
|||01 - SIUL2_VIRTWRAPPER_PDAC2|
|||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|25-24|PAD_|12|
|PAD_12||00 - SIUL2_VIRTWRAPPER_PDAC1|
|||01 - SIUL2_VIRTWRAPPER_PDAC2|
|||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|23-22|PAD_|11|
|PAD_11||00 - SIUL2_VIRTWRAPPER_PDAC1|
|||01 - SIUL2_VIRTWRAPPER_PDAC2|
|||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|21-20|PAD_|10|
|PAD_10||00 - SIUL2_VIRTWRAPPER_PDAC1|
|||01 - SIUL2_VIRTWRAPPER_PDAC2|
|||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|19-18|PAD_|9|
|PAD_9||00 - SIUL2_VIRTWRAPPER_PDAC1|
|||01 - SIUL2_VIRTWRAPPER_PDAC2|
|||10 - SIUL2_VIRTWRAPPER_PDAC4|
|||11-SIUL2_VIRTWRAPPER_PDAC0|
|17-16|PAD_|8|
|PAD_8||00 - SIUL2_VIRTWRAPPER_PDAC1|
|||01 - SIUL2_VIRTWRAPPER_PDAC2|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

138 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Funct|ion|
|---|---|---|
|||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|15-14|PAD_|7|
|PAD_7||00 - SIUL2_VIRTWRAPPER_PDAC1|
|||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|13-12|PAD_|6|
|PAD_6||00 - SIUL2_VIRTWRAPPER_PDAC1|
|||01 - SIUL2_VIRTWRAPPER_PDAC2|
|||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|11-10|PAD_|5|
|PAD_5||00 - SIUL2_VIRTWRAPPER_PDAC1|
|||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|9-8|PAD_|4|
|PAD_4||00 - SIUL2_VIRTWRAPPER_PDAC1|
|||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|7-6|PAD_|3|
|PAD_3||00 - SIUL2_VIRTWRAPPER_PDAC1|
|||01 - SIUL2_VIRTWRAPPER_PDAC2|
|||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|5-4|PAD_|2|
|PAD_2||00 - SIUL2_VIRTWRAPPER_PDAC1|
|||01 - SIUL2_VIRTWRAPPER_PDAC2|
|||10 - SIUL2_VIRTWRAPPER_PDAC4|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

139 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|3-2|PAD_1|
|PAD_1|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|1-0|PAD_0|
|PAD_0|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|



### 8.4.5 Parameter_n Register (REG_A14) 

##### Offset 

|Register|Offset|
|---|---|
|REG_A14|38h|



##### Function 

This register set is for PAD0-511. They control MSCR, GPDO, PGPDO, and MPGPDO. Two bits assigned per PDAC slot have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

~~<mark>NOTE</mark>~~ 

- Any master can access holes (unimplemented registers) of SIUL2 through PDAC0. 

- After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

140 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

##### Diagram 

|Bits|31<br>30|29|28|27<br>26|25|24|23|22|21|20|19<br>18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|Reserved|Rese|rved|Reserved|PAD|_12|PAD_|11|PAD|_10|PAD_9|PAD_8|
|Reset|1<br>1|1|1|1<br>1|1|1|1|1|1|1|1<br>1|1<br>1|
|Bits|15<br>14|13|12|11<br>10|9|8|7|6|5|4|3<br>2|1<br>0|
|R<br>W|PAD_7|PAD|_6|PAD_5|PAD|_4|PAD|_3|PAD|_2|PAD_1|PAD_0|
|Reset|1<br>1|1|1|1<br>1|1|1|1|1|1|1|1<br>1|1<br>1|



##### Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29-28<br>—|Reserved|
|27-26<br>—|Reserved|
|25-24|PAD_12|
|PAD_12|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|23-22|PAD_11|
|PAD_11|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|21-20|PAD_10|
|PAD_10|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|19-18|PAD_9|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

141 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|PAD_9|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|17-16|PAD_8|
|PAD_8|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|15-14|PAD_7|
|PAD_7|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|13-12|PAD_6|
|PAD_6|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|11-10|PAD_5|
|PAD_5|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|9-8|PAD_4|
|PAD_4|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|7-6|PAD_3|
|PAD_3|00 - SIUL2_VIRTWRAPPER_PDAC1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

142 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|5-4|PAD_2|
|PAD_2|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|3-2|PAD_1|
|PAD_1|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|1-0|PAD_0|
|PAD_0|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|



### 8.4.6 Parameter_n Register (REG_B0) 

##### Offset 

|Register|Offset|
|---|---|
|REG_B0|80h|



##### Function 

Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

143 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

~~<mark>NOTE</mark>~~ 

- Any master can access holes (unimplemented registers) of SIUL2 through PDAC0. 

- After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/008_Virtualization_Wrapper_-VIRT_WRAPPER-/S32K3XXRM_数据表.pdf-0144-06.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved  Reserved  Reserved  Reserved  Reserved  Reserved  Reserved  Reserved<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>Reserved  Reserved  INMUX_5  INMUX_4  INMUX_3  INMUX_2  INMUX_1  INMUX_0<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29-28<br>—|Reserved|
|27-26<br>—|Reserved|
|25-24<br>—|Reserved|
|23-22<br>—|Reserved|
|21-20<br>—|Reserved|
|19-18<br>—|Reserved|
|17-16<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

144 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|15-14<br>—|Reserved|
|13-12<br>—|Reserved|
|11-10|INMUX_5|
|INMUX_5|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|9-8|INMUX_4|
|INMUX_4|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|7-6|INMUX_3|
|INMUX_3|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|5-4|INMUX_2|
|INMUX_2|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|3-2|INMUX_1|
|INMUX_1|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|1-0|INMUX_0|
|INMUX_0|00 - SIUL2_VIRTWRAPPER_PDAC1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

145 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|



### 8.4.7 Parameter_n Register (REG_B1 - REG_B3) 

##### Offset 

|Register|Offset|
|---|---|
|REG_B1|84h|
|REG_B2|88h|
|REG_B3|8Ch|



##### Function 

Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

~~<mark>NOTE</mark>~~ 

- Any master can access holes (unimplemented registers) of SIUL2 through PDAC0. 

- After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/008_Virtualization_Wrapper_-VIRT_WRAPPER-/S32K3XXRM_数据表.pdf-0146-17.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>INMUX_15  INMUX_14  INMUX_13  INMUX_12  INMUX_11  INMUX_10  INMUX_9  INMUX_8<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>INMUX_7  INMUX_6  INMUX_5  INMUX_4  INMUX_3  INMUX_2  INMUX_1  INMUX_0<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

146 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

##### Fields 

|Field|Function|
|---|---|
|31-30|INMUX_15|
|INMUX_15|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|29-28|INMUX_14|
|INMUX_14|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|27-26|INMUX_13|
|INMUX_13|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|25-24|INMUX_12|
|INMUX_12|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|23-22|INMUX_11|
|INMUX_11|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|21-20|INMUX_10|
|INMUX_10|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|19-18|INMUX_9|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

147 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|INMUX_9|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|17-16|INMUX_8|
|INMUX_8|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|15-14|INMUX_7|
|INMUX_7|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|13-12|INMUX_6|
|INMUX_6|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|11-10|INMUX_5|
|INMUX_5|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|9-8|INMUX_4|
|INMUX_4|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|7-6|INMUX_3|
|INMUX_3|00 - SIUL2_VIRTWRAPPER_PDAC1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

148 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|5-4|INMUX_2|
|INMUX_2|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|3-2|INMUX_1|
|INMUX_1|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|1-0|INMUX_0|
|INMUX_0|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|



### 8.4.8 Parameter_n Register (REG_B4) 

##### Offset 

|Register|Offset|
|---|---|
|REG_B4|90h|



##### Function 

Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

149 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

~~<mark>NOTE</mark>~~ 

- Any master can access holes (unimplemented registers) of SIUL2 through PDAC0. 

- After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

##### Diagram 

|Bits|31<br>30|29|28|27|26|25<br>24|23|22|21<br>20|19<br>18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|Reserved|Rese|rved|Rese|rved|Reserved|Reser|ved|Reserved|Reserved|Reserved|
|Reset|1<br>1|1|1|1|1|1<br>1|1|1|1<br>1|1<br>1|1<br>1|
|Bits|15<br>14|13|12|11|10|9<br>8|7|6|5<br>4|3<br>2|1<br>0|
|R<br>W|INMUX_7|INMU|X_6|INMU|X_5|INMUX_4|INMU|X_3|INMUX_2|INMUX_1|INMUX_0|
|Reset|1<br>1|1|1|1|1|1<br>1|1|1|1<br>1|1<br>1|1<br>1|



##### Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29-28<br>—|Reserved|
|27-26<br>—|Reserved|
|25-24<br>—|Reserved|
|23-22<br>—|Reserved|
|21-20<br>—|Reserved|
|19-18<br>—|Reserved|
|17-16<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

150 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|15-14|INMUX_7|
|INMUX_7|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|13-12|INMUX_6|
|INMUX_6|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|11-10|INMUX_5|
|INMUX_5|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|9-8|INMUX_4|
|INMUX_4|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|7-6|INMUX_3|
|INMUX_3|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|5-4|INMUX_2|
|INMUX_2|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|3-2|INMUX_1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

151 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|INMUX_1|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|1-0|INMUX_0|
|INMUX_0|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|



### 8.4.9 Parameter_n Register (REG_B5) 

##### Offset 

|Register|Offset|
|---|---|
|REG_B5|94h|



##### Function 

Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

~~<mark>NOTE</mark>~~ 

- Any master can access holes (unimplemented registers) of SIUL2 through PDAC0. 

- After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

152 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19<br>18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|INMU|X_15|INMU|X_14|INMU|X_13|INMU|X_12|INMU|X_11|INMU|X_10|INMUX_9|INMUX_8|
|Reset|1|1|1|1|1|1|1|1|1|1|1|1|1<br>1|1<br>1|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3<br>2|1<br>0|
|R<br>W|INMU|X_7|INMU|X_6|INMU|X_5|INMU|X_4|INMU|X_3|INMU|X_2|INMUX_1|INMUX_0|
|Reset|1|1|1|1|1|1|1|1|1|1|1|1|1<br>1|1<br>1|



##### Fields 

|Field|Function|
|---|---|
|31-30|INMUX_15|
|INMUX_15|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|29-28|INMUX_14|
|INMUX_14|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|27-26|INMUX_13|
|INMUX_13|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|25-24|INMUX_12|
|INMUX_12|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|23-22|INMUX_11|
|INMUX_11|00 - SIUL2_VIRTWRAPPER_PDAC1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

153 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function||
|---|---|---|
||01<br>10<br>11-|- SIUL2_VIRTWRAPPER_PDAC2<br>- SIUL2_VIRTWRAPPER_PDAC4<br>SIUL2_VIRTWRAPPER_PDAC0|
|21-20|INMUX_10||
|INMUX_10|00|- SIUL2_VIRTWRAPPER_PDAC1|
||01|- SIUL2_VIRTWRAPPER_PDAC2|
||10<br>11-|- SIUL2_VIRTWRAPPER_PDAC4<br>SIUL2_VIRTWRAPPER_PDAC0|
|19-18|INMUX_9||
|INMUX_9|00|- SIUL2_VIRTWRAPPER_PDAC1|
||01|- SIUL2_VIRTWRAPPER_PDAC2|
||10<br>11-|- SIUL2_VIRTWRAPPER_PDAC4<br>SIUL2_VIRTWRAPPER_PDAC0|
|17-16|INMUX_8||
|INMUX_8|00|- SIUL2_VIRTWRAPPER_PDAC1|
||01|- SIUL2_VIRTWRAPPER_PDAC2|
||10<br>11-|- SIUL2_VIRTWRAPPER_PDAC4<br>SIUL2_VIRTWRAPPER_PDAC0|
|15-14|INMUX_7||
|INMUX_7|00|- SIUL2_VIRTWRAPPER_PDAC1|
||01|- SIUL2_VIRTWRAPPER_PDAC2|
||10<br>11-|- SIUL2_VIRTWRAPPER_PDAC4<br>SIUL2_VIRTWRAPPER_PDAC0|
|13-12|INMUX_6||
|INMUX_6|00|- SIUL2_VIRTWRAPPER_PDAC1|
||01|- SIUL2_VIRTWRAPPER_PDAC2|
||10|- SIUL2_VIRTWRAPPER_PDAC4|
||11-|SIUL2_VIRTWRAPPER_PDAC0|
|11-10|INMUX_5||
|INMUX_5|00|- SIUL2_VIRTWRAPPER_PDAC1|
||01|- SIUL2_VIRTWRAPPER_PDAC2|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

154 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|9-8|INMUX_4|
|INMUX_4|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|7-6|INMUX_3|
|INMUX_3|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|5-4|INMUX_2|
|INMUX_2|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|3-2|INMUX_1|
|INMUX_1|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|1-0|INMUX_0|
|INMUX_0|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

155 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

### 8.4.10 Parameter_n Register (REG_B6) 

##### Offset 

|Register|Offset|
|---|---|
|REG_B6|98h|



##### Function 

Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

~~<mark>NOTE</mark>~~ 

- Any master can access holes (unimplemented registers) of SIUL2 through PDAC0. 

- After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/008_Virtualization_Wrapper_-VIRT_WRAPPER-/S32K3XXRM_数据表.pdf-0156-15.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved  Reserved  Reserved  Reserved  Reserved  Reserved  Reserved  Reserved<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>INMUX_7  INMUX_6  INMUX_5  INMUX_4  INMUX_3  INMUX_2  INMUX_1  INMUX_0<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29-28<br>—|Reserved|
|27-26|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

156 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|—<br>25-24<br>—|Reserved|
|23-22<br>—|Reserved|
|21-20<br>—|Reserved|
|19-18<br>—|Reserved|
|17-16<br>—|Reserved|
|15-14|INMUX_7|
|INMUX_7|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|13-12|INMUX_6|
|INMUX_6|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|11-10|INMUX_5|
|INMUX_5|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|9-8|INMUX_4|
|INMUX_4|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

157 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|7-6|INMUX_3|
|INMUX_3|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|5-4|INMUX_2|
|INMUX_2|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|3-2|INMUX_1|
|INMUX_1|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|1-0|INMUX_0|
|INMUX_0|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|



### 8.4.11 Parameter_n Register (REG_B7) 

##### Offset 

|Register|Offset|
|---|---|
|REG_B7|9Ch|



##### Function 

Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

158 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

~~<mark>NOTE</mark>~~ 

- Any master can access holes (unimplemented registers) of SIUL2 through PDAC0. 

- After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/008_Virtualization_Wrapper_-VIRT_WRAPPER-/S32K3XXRM_数据表.pdf-0159-07.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>INMUX_15  INMUX_14  INMUX_13  INMUX_12  INMUX_11  INMUX_10  INMUX_9  INMUX_8<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>INMUX_7  INMUX_6  INMUX_5  INMUX_4  INMUX_3  INMUX_2  INMUX_1  INMUX_0<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-30|INMUX_15|
|INMUX_15|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|29-28|INMUX_14|
|INMUX_14|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|27-26|INMUX_13|
|INMUX_13|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|25-24|INMUX_12|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

159 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|INMUX_12|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|23-22|INMUX_11|
|INMUX_11|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|21-20|INMUX_10|
|INMUX_10|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|19-18|INMUX_9|
|INMUX_9|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|17-16|INMUX_8|
|INMUX_8|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|15-14|INMUX_7|
|INMUX_7|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|13-12|INMUX_6|
|INMUX_6|00 - SIUL2_VIRTWRAPPER_PDAC1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

160 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|11-10|INMUX_5|
|INMUX_5|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|9-8|INMUX_4|
|INMUX_4|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|7-6|INMUX_3|
|INMUX_3|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|5-4|INMUX_2|
|INMUX_2|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|3-2|INMUX_1|
|INMUX_1|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|1-0|INMUX_0|
|INMUX_0|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

161 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|



### 8.4.12 Parameter_n Register (REG_B8) 

##### Offset 

|Register|Offset|
|---|---|
|REG_B8|A0h|



##### Function 

Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

~~<mark>NOTE</mark>~~ 

- Any master can access holes (unimplemented registers) of SIUL2 through PDAC0. 

- After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/008_Virtualization_Wrapper_-VIRT_WRAPPER-/S32K3XXRM_数据表.pdf-0162-17.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved  Reserved  Reserved  Reserved  Reserved  Reserved  Reserved  Reserved<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>INMUX_7  INMUX_6  INMUX_5  INMUX_4  INMUX_3  INMUX_2  INMUX_1  INMUX_0<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

162 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

##### Fields 

|Field<br>31-30<br>—|Function<br>Reserved|
|---|---|
|29-28<br>—|Reserved|
|27-26<br>—|Reserved|
|25-24<br>—|Reserved|
|23-22<br>—|Reserved|
|21-20<br>—|Reserved|
|19-18<br>—|Reserved|
|17-16<br>—|Reserved|
|15-14|INMUX_7|
|INMUX_7|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|13-12|INMUX_6|
|INMUX_6|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|11-10|INMUX_5|
|INMUX_5|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

163 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|---|---|
|9-8|INMUX_4|
|INMUX_4|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|7-6|INMUX_3|
|INMUX_3|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|5-4|INMUX_2|
|INMUX_2|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|3-2|INMUX_1|
|INMUX_1|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|1-0|INMUX_0|
|INMUX_0|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|



### 8.4.13 Parameter_n Register (REG_B9) 

Offset 

|Register|Offset|
|---|---|
|REG_B9|A4h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

164 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

##### Function 

Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

~~<mark>NOTE</mark>~~ 

- Any master can access holes (unimplemented registers) of SIUL2 through PDAC0. 

- After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/008_Virtualization_Wrapper_-VIRT_WRAPPER-/S32K3XXRM_数据表.pdf-0165-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>INMUX_15  INMUX_14  INMUX_13  INMUX_12  INMUX_11  INMUX_10  INMUX_9  INMUX_8<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>Reserved  Reserved  INMUX_5  INMUX_4  INMUX_3  INMUX_2  INMUX_1  INMUX_0<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-30|INMUX_15|
|INMUX_15|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|29-28|INMUX_14|
|INMUX_14|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|27-26|INMUX_13|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

165 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|INMUX_13|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|25-24|INMUX_12|
|INMUX_12|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|23-22|INMUX_11|
|INMUX_11|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|21-20|INMUX_10|
|INMUX_10|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|19-18|INMUX_9|
|INMUX_9|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|17-16|INMUX_8|
|INMUX_8|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|15-14<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

166 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|13-12<br>—|Reserved|
|11-10|INMUX_5|
|INMUX_5|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|9-8|INMUX_4|
|INMUX_4|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|7-6|INMUX_3|
|INMUX_3|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|5-4|INMUX_2|
|INMUX_2|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|3-2|INMUX_1|
|INMUX_1|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|1-0|INMUX_0|
|INMUX_0|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

167 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||11-SIUL2_VIRTWRAPPER_PDAC0|



### 8.4.14 Parameter_n Register (REG_B10 - REG_B11) 

##### Offset 

|Register|Offset|
|---|---|
|REG_B10|A8h|
|REG_B11|ACh|



##### Function 

Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

~~<mark>NOTE</mark>~~ 

- Any master can access holes (unimplemented registers) of SIUL2 through PDAC0. 

- After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/008_Virtualization_Wrapper_-VIRT_WRAPPER-/S32K3XXRM_数据表.pdf-0168-17.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>INMUX_15  INMUX_14  INMUX_13  INMUX_12  INMUX_11  INMUX_10  INMUX_9  INMUX_8<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>INMUX_7  INMUX_6  INMUX_5  INMUX_4  INMUX_3  INMUX_2  INMUX_1  INMUX_0<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

168 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

##### Fields 

|Field|Function|
|---|---|
|31-30|INMUX_15|
|INMUX_15|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|29-28|INMUX_14|
|INMUX_14|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|27-26|INMUX_13|
|INMUX_13|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|25-24|INMUX_12|
|INMUX_12|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|23-22|INMUX_11|
|INMUX_11|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|21-20|INMUX_10|
|INMUX_10|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|19-18|INMUX_9|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

169 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|INMUX_9|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|17-16|INMUX_8|
|INMUX_8|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|15-14|INMUX_7|
|INMUX_7|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|13-12|INMUX_6|
|INMUX_6|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|11-10|INMUX_5|
|INMUX_5|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|9-8|INMUX_4|
|INMUX_4|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|7-6|INMUX_3|
|INMUX_3|00 - SIUL2_VIRTWRAPPER_PDAC1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

170 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|5-4|INMUX_2|
|INMUX_2|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|3-2|INMUX_1|
|INMUX_1|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|1-0|INMUX_0|
|INMUX_0|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|



### 8.4.15 Parameter_n Register (REG_B12) 

##### Offset 

|Register|Offset|
|---|---|
|REG_B12|B0h|



##### Function 

Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

171 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

~~<mark>NOTE</mark>~~ 

- Any master can access holes (unimplemented registers) of SIUL2 through PDAC0. 

- After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

##### Diagram 

|Bits|31<br>30|29|28|27|26|25<br>24|23|22|21|20|19<br>18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|Reserved|Rese|rved|Rese|rved|Reserved|Reser|ved|INMU|X_10|INMUX_9|INMUX_8|
|Reset|1<br>1|1|1|1|1|1<br>1|1|1|1|1|1<br>1|1<br>1|
|Bits|15<br>14|13|12|11|10|9<br>8|7|6|5|4|3<br>2|1<br>0|
|R<br>W|INMUX_7|INMU|X_6|INMU|X_5|INMUX_4|INMU|X_3|INMU|X_2|INMUX_1|INMUX_0|
|Reset|1<br>1|1|1|1|1|1<br>1|1|1|1|1|1<br>1|1<br>1|



##### Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29-28<br>—|Reserved|
|27-26<br>—|Reserved|
|25-24<br>—|Reserved|
|23-22<br>—|Reserved|
|21-20|INMUX_10|
|INMUX_10|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|19-18<br>INMUX_9|INMUX_9|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

172 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|17-16|INMUX_8|
|INMUX_8|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|15-14|INMUX_7|
|INMUX_7|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|13-12|INMUX_6|
|INMUX_6|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|11-10|INMUX_5|
|INMUX_5|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|9-8|INMUX_4|
|INMUX_4|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|7-6|INMUX_3|
|INMUX_3|00 - SIUL2_VIRTWRAPPER_PDAC1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

173 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|5-4|INMUX_2|
|INMUX_2|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|3-2|INMUX_1|
|INMUX_1|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|1-0|INMUX_0|
|INMUX_0|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|



### 8.4.16 Parameter_n Register (REG_B13) 

##### Offset 

|Register|Offset|
|---|---|
|REG_B13|B4h|



##### Function 

Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

174 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

~~<mark>NOTE</mark>~~ 

- Any master can access holes (unimplemented registers) of SIUL2 through PDAC0. 

- After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/008_Virtualization_Wrapper_-VIRT_WRAPPER-/S32K3XXRM_数据表.pdf-0175-06.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>INMUX_15  INMUX_14  INMUX_13  INMUX_12  INMUX_11  INMUX_10  INMUX_9  INMUX_8<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>INMUX_7  INMUX_6  INMUX_5  INMUX_4  INMUX_3  Reserved  Reserved  Reserved<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-30|INMUX_15|
|INMUX_15|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|29-28|INMUX_14|
|INMUX_14|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|27-26|INMUX_13|
|INMUX_13|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|25-24|INMUX_12|
|INMUX_12|00 - SIUL2_VIRTWRAPPER_PDAC1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

175 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|23-22|INMUX_11|
|INMUX_11|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|21-20|INMUX_10|
|INMUX_10|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|19-18|INMUX_9|
|INMUX_9|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|17-16|INMUX_8|
|INMUX_8|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|15-14|INMUX_7|
|INMUX_7|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|13-12|INMUX_6|
|INMUX_6|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

176 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|11-10|INMUX_5|
|INMUX_5|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|9-8|INMUX_4|
|INMUX_4|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|7-6|INMUX_3|
|INMUX_3|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|5-4<br>—|Reserved|
|3-2<br>—|Reserved|
|1-0<br>—|Reserved|



### 8.4.17 Parameter_n Register (REG_B14 - REG_B15) 

##### Offset 

|Register|Offset|
|---|---|
|REG_B14|B8h|
|REG_B15|BCh|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

177 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

##### Function 

Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

~~<mark>NOTE</mark>~~ 

- Any master can access holes (unimplemented registers) of SIUL2 through PDAC0. 

- After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/008_Virtualization_Wrapper_-VIRT_WRAPPER-/S32K3XXRM_数据表.pdf-0178-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>INMUX_15  INMUX_14  INMUX_13  INMUX_12  INMUX_11  INMUX_10  INMUX_9  INMUX_8<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>INMUX_7  INMUX_6  INMUX_5  INMUX_4  INMUX_3  INMUX_2  INMUX_1  INMUX_0<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-30|INMUX_15|
|INMUX_15|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|29-28|INMUX_14|
|INMUX_14|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|27-26|INMUX_13|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

178 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|INMUX_13|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|25-24|INMUX_12|
|INMUX_12|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|23-22|INMUX_11|
|INMUX_11|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|21-20|INMUX_10|
|INMUX_10|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|19-18|INMUX_9|
|INMUX_9|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|17-16|INMUX_8|
|INMUX_8|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|15-14|INMUX_7|
|INMUX_7|00 - SIUL2_VIRTWRAPPER_PDAC1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

179 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|13-12|INMUX_6|
|INMUX_6|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|11-10|INMUX_5|
|INMUX_5|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|9-8|INMUX_4|
|INMUX_4|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|7-6|INMUX_3|
|INMUX_3|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|5-4|INMUX_2|
|INMUX_2|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|3-2|INMUX_1|
|INMUX_1|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

180 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|1-0|INMUX_0|
|INMUX_0|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|



### 8.4.18 Parameter_n Register (REG_B16) 

##### Offset 

|Register|Offset|
|---|---|
|REG_B16|C0h|



##### Function 

Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

~~<mark>NOTE</mark>~~ 

- Any master can access holes (unimplemented registers) of SIUL2 through PDAC0. 

- After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

181 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19<br>18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|Rese|rved|Rese|rved|Rese|rved|INMU|X_12|INMU|X_11|INMU|X_10|INMUX_9|INMUX_8|
|Reset|1|1|1|1|1|1|1|1|1|1|1|1|1<br>1|1<br>1|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3<br>2|1<br>0|
|R<br>W|INMU|X_7|INMU|X_6|INMU|X_5|INMU|X_4|INMU|X_3|INMU|X_2|INMUX_1|INMUX_0|
|Reset|1|1|1|1|1|1|1|1|1|1|1|1|1<br>1|1<br>1|



##### Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29-28<br>—|Reserved|
|27-26<br>—|Reserved|
|25-24|INMUX_12|
|INMUX_12|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|23-22|INMUX_11|
|INMUX_11|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|21-20|INMUX_10|
|INMUX_10|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|19-18|INMUX_9|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

182 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|INMUX_9|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|17-16|INMUX_8|
|INMUX_8|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|15-14|INMUX_7|
|INMUX_7|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|13-12|INMUX_6|
|INMUX_6|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|11-10|INMUX_5|
|INMUX_5|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|9-8|INMUX_4|
|INMUX_4|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|7-6|INMUX_3|
|INMUX_3|00 - SIUL2_VIRTWRAPPER_PDAC1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

183 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|5-4|INMUX_2|
|INMUX_2|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|3-2|INMUX_1|
|INMUX_1|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|1-0|INMUX_0|
|INMUX_0|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|



### 8.4.19 Parameter_n Register (REG_B18) 

##### Offset 

|Register|Offset|
|---|---|
|REG_B18|C8h|



##### Function 

Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

184 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

~~<mark>NOTE</mark>~~ 

- Any master can access holes (unimplemented registers) of SIUL2 through PDAC0. 

- After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/008_Virtualization_Wrapper_-VIRT_WRAPPER-/S32K3XXRM_数据表.pdf-0185-06.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>INMUX_15  INMUX_14  INMUX_13  INMUX_12  INMUX_11  INMUX_10  INMUX_9  INMUX_8<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>INMUX_7  INMUX_6  INMUX_5  INMUX_4  INMUX_3  INMUX_2  INMUX_1  Reserved<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-30|INMUX_15|
|INMUX_15|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|29-28|INMUX_14|
|INMUX_14|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|27-26|INMUX_13|
|INMUX_13|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|25-24|INMUX_12|
|INMUX_12|00 - SIUL2_VIRTWRAPPER_PDAC1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

185 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|23-22|INMUX_11|
|INMUX_11|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|21-20|INMUX_10|
|INMUX_10|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|19-18|INMUX_9|
|INMUX_9|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|17-16|INMUX_8|
|INMUX_8|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|15-14|INMUX_7|
|INMUX_7|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|13-12|INMUX_6|
|INMUX_6|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

186 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|---|---|
|11-10|INMUX_5|
|INMUX_5|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|9-8|INMUX_4|
|INMUX_4|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|7-6|INMUX_3|
|INMUX_3|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|5-4|INMUX_2|
|INMUX_2|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|3-2|INMUX_1|
|INMUX_1|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|1-0<br>—|Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

187 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

### 8.4.20 Parameter_n Register (REG_B19) 

##### Offset 

|Register|Offset|
|---|---|
|REG_B19|CCh|



##### Function 

Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

~~<mark>NOTE</mark>~~ 

- Any master can access holes (unimplemented registers) of SIUL2 through PDAC0. 

- After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/008_Virtualization_Wrapper_-VIRT_WRAPPER-/S32K3XXRM_数据表.pdf-0188-15.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>INMUX_15  INMUX_14  INMUX_13  INMUX_12  INMUX_11  Reserved  Reserved  Reserved<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>Reserved  Reserved  INMUX_5  INMUX_4  INMUX_3  INMUX_2  INMUX_1  INMUX_0<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-30|INMUX_15|
|INMUX_15|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

188 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field<br>29-28|Function<br>INMUX_14|
|---|---|
|INMUX_14|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|27-26|INMUX_13|
|INMUX_13|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|25-24|INMUX_12|
|INMUX_12|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|23-22|INMUX_11|
|INMUX_11|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|21-20<br>—|Reserved|
|19-18<br>—|Reserved|
|17-16<br>—|Reserved|
|15-14<br>|Reserved|
|—<br>13-12<br>—|Reserved|
|11-10|INMUX_5|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

189 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|INMUX_5|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|9-8|INMUX_4|
|INMUX_4|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|7-6|INMUX_3|
|INMUX_3|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|5-4|INMUX_2|
|INMUX_2|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|3-2|INMUX_1|
|INMUX_1|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|1-0|INMUX_0|
|INMUX_0|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

190 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

### 8.4.21 Parameter_n Register (REG_B20) 

##### Offset 

|Register|Offset|
|---|---|
|REG_B20|D0h|



##### Function 

Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

~~<mark>NOTE</mark>~~ 

- Any master can access holes (unimplemented registers) of SIUL2 through PDAC0. 

- After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/008_Virtualization_Wrapper_-VIRT_WRAPPER-/S32K3XXRM_数据表.pdf-0191-15.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved  Reserved  Reserved  Reserved  Reserved  Reserved  Reserved  Reserved<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>Reserved  Reserved  INMUX_5  INMUX_4  INMUX_3  INMUX_2  INMUX_1  INMUX_0<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29-28<br>—|Reserved|
|27-26|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

191 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field<br>—<br>25-24<br>—|Function<br>Reserved|
|---|---|
|23-22<br>—|Reserved|
|21-20<br>—|Reserved|
|19-18<br>—|Reserved|
|17-16<br>—|Reserved|
|15-14<br>—|Reserved|
|13-12<br>—|Reserved|
|11-10|INMUX_5|
|INMUX_5|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|9-8|INMUX_4|
|INMUX_4|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|7-6|INMUX_3|
|INMUX_3|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

192 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|5-4|INMUX_2|
|INMUX_2|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|3-2|INMUX_1|
|INMUX_1|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|1-0|INMUX_0|
|INMUX_0|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|



### 8.4.22 Parameter_n Register (REG_B21) 

##### Offset 

|Register|Offset|
|---|---|
|REG_B21|D4h|



##### Function 

Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

~~<mark>NOTE</mark>~~ 

- Any master can access holes (unimplemented registers) of SIUL2 through PDAC0. 

- After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

193 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19<br>18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|INMU|X_15|INMU|X_14|INMU|X_13|INMU|X_12|INMU|X_11|INMU|X_10|INMUX_9|INMUX_8|
|Reset|1|1|1|1|1|1|1|1|1|1|1|1|1<br>1|1<br>1|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3<br>2|1<br>0|
|R<br>W|INMU|X_7|Rese|rved|Rese|rved|Rese|rved|Reser|ved|Rese|rved|Reserved|Reserved|
|Reset|1|1|1|1|1|1|1|1|1|1|1|1|1<br>1|1<br>1|



##### Fields 

|Field|Function|
|---|---|
|31-30|INMUX_15|
|INMUX_15|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|29-28|INMUX_14|
|INMUX_14|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|27-26|INMUX_13|
|INMUX_13|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|25-24|INMUX_12|
|INMUX_12|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|23-22|INMUX_11|
|INMUX_11|00 - SIUL2_VIRTWRAPPER_PDAC1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

194 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|21-20|INMUX_10|
|INMUX_10|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|19-18|INMUX_9|
|INMUX_9|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|17-16|INMUX_8|
|INMUX_8|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|15-14|INMUX_7|
|INMUX_7|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|13-12<br>—|Reserved|
|11-10<br>—|Reserved|
|9-8<br>—|Reserved|
|7-6<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

195 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|5-4<br>—|Reserved|
|3-2<br>—|Reserved|
|1-0<br>—|Reserved|



### 8.4.23 Parameter_n Register (REG_B22) 

##### Offset 

|Register|Offset|
|---|---|
|REG_B22|D8h|



##### Function 

Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

###### ~~<mark>NOTE</mark>~~ 

- Any master can access holes (unimplemented registers) of SIUL2 through PDAC0. 

- After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

##### Diagram 

|Bits|31<br>30|29|28|27<br>26|25<br>24|23|22|21|20|19<br>18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|INMUX_15|INMU|X_14|INMUX_13|INMUX_12|INMU|X_11|INMU|X_10|INMUX_9|INMUX_8|
|Reset|1<br>1|1|1|1<br>1|1<br>1|1|1|1|1|1<br>1|1<br>1|
|Bits|15<br>14|13|12|11<br>10|9<br>8|7|6|5|4|3<br>2|1<br>0|
|R<br>W|INMUX_7|INMU|X_6|INMUX_5|INMUX_4|INMU|X_3|INMU|X_2|INMUX_1|INMUX_0|
|Reset|1<br>1|1|1|1<br>1|1<br>1|1|1|1|1|1<br>1|1<br>1|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

196 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

##### Fields 

|Field|Function|
|---|---|
|31-30|INMUX_15|
|INMUX_15|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|29-28|INMUX_14|
|INMUX_14|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|27-26|INMUX_13|
|INMUX_13|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|25-24|INMUX_12|
|INMUX_12|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|23-22|INMUX_11|
|INMUX_11|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|21-20|INMUX_10|
|INMUX_10|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|19-18|INMUX_9|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

197 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|INMUX_9|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|17-16|INMUX_8|
|INMUX_8|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|15-14|INMUX_7|
|INMUX_7|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|13-12|INMUX_6|
|INMUX_6|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|11-10|INMUX_5|
|INMUX_5|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|9-8|INMUX_4|
|INMUX_4|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|7-6|INMUX_3|
|INMUX_3|00 - SIUL2_VIRTWRAPPER_PDAC1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

198 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|5-4|INMUX_2|
|INMUX_2|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|3-2|INMUX_1|
|INMUX_1|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|1-0|INMUX_0|
|INMUX_0|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|



### 8.4.24 Parameter_n Register (REG_B23) 

##### Offset 

|Register|Offset|
|---|---|
|REG_B23|DCh|



##### Function 

Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

199 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

~~<mark>NOTE</mark>~~ 

- Any master can access holes (unimplemented registers) of SIUL2 through PDAC0. 

- After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

##### Diagram 

|Bits|31<br>30|29|28|27|26|25<br>24|23|22|21|20|19<br>18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|Reserved|Rese|rved|Rese|rved|Reserved|Reser|ved|INMU|X_10|INMUX_9|INMUX_8|
|Reset|1<br>1|1|1|1|1|1<br>1|1|1|1|1|1<br>1|1<br>1|
|Bits|15<br>14|13|12|11|10|9<br>8|7|6|5|4|3<br>2|1<br>0|
|R<br>W|INMUX_7|INMU|X_6|INMU|X_5|INMUX_4|INMU|X_3|INMU|X_2|INMUX_1|INMUX_0|
|Reset|1<br>1|1|1|1|1|1<br>1|1|1|1|1|1<br>1|1<br>1|



##### Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29-28<br>—|Reserved|
|27-26<br>—|Reserved|
|25-24<br>—|Reserved|
|23-22<br>—|Reserved|
|21-20|INMUX_10|
|INMUX_10|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|19-18<br>INMUX_9|INMUX_9|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

200 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|17-16|INMUX_8|
|INMUX_8|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|15-14|INMUX_7|
|INMUX_7|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|13-12|INMUX_6|
|INMUX_6|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|11-10|INMUX_5|
|INMUX_5|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|9-8|INMUX_4|
|INMUX_4|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|7-6|INMUX_3|
|INMUX_3|00 - SIUL2_VIRTWRAPPER_PDAC1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

201 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|5-4|INMUX_2|
|INMUX_2|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|3-2|INMUX_1|
|INMUX_1|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|1-0|INMUX_0|
|INMUX_0|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|



### 8.4.25 Parameter_n Register (REG_B24) 

##### Offset 

|Register|Offset|
|---|---|
|REG_B24|E0h|



##### Function 

Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

202 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

~~<mark>NOTE</mark>~~ 

- Any master can access holes (unimplemented registers) of SIUL2 through PDAC0. 

- After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/008_Virtualization_Wrapper_-VIRT_WRAPPER-/S32K3XXRM_数据表.pdf-0203-06.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>INMUX_15  INMUX_14  Reserved  Reserved  Reserved  Reserved  Reserved  Reserved<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>Reserved  Reserved  INMUX_5  Reserved  Reserved  Reserved  Reserved  Reserved<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-30|INMUX_15|
|INMUX_15|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|29-28|INMUX_14|
|INMUX_14|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|27-26<br>—|Reserved|
|25-24<br>—|Reserved|
|23-22<br>—|Reserved|
|21-20|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

203 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—<br>19-18<br>—|Reserved|
|17-16<br>—|Reserved|
|15-14<br>—|Reserved|
|13-12<br>—|Reserved|
|11-10<br>INMUX_5|INMUX_5<br>00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|9-8<br>—|Reserved|
|7-6<br>—|Reserved|
|5-4<br>—|Reserved|
|3-2<br>—|Reserved|
|1-0<br>—|Reserved|



### 8.4.26 Parameter_n Register (REG_B25) 

##### Offset 

|Register|Offset|
|---|---|
|REG_B25|E4h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

204 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

##### Function 

Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

~~<mark>NOTE</mark>~~ 

- Any master can access holes (unimplemented registers) of SIUL2 through PDAC0. 

- After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/008_Virtualization_Wrapper_-VIRT_WRAPPER-/S32K3XXRM_数据表.pdf-0205-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>INMUX_15  INMUX_14  INMUX_13  INMUX_12  INMUX_11  INMUX_10  INMUX_9  Reserved<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>Reserved  Reserved  Reserved  Reserved  Reserved  Reserved  Reserved  Reserved<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-30|INMUX_15|
|INMUX_15|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|29-28|INMUX_14|
|INMUX_14|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|27-26|INMUX_13|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

205 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|INMUX_13|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|25-24|INMUX_12|
|INMUX_12|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|23-22|INMUX_11|
|INMUX_11|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|21-20|INMUX_10|
|INMUX_10|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|19-18|INMUX_9|
|INMUX_9|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|17-16<br>—|Reserved|
|15-14<br>—|Reserved|
|13-12<br>—|Reserved|
|11-10|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

206 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

##### Table continued from the previous page... 

|Field<br>—|Function|
|---|---|
|9-8<br>—|Reserved|
|7-6<br>—|Reserved|
|5-4<br>—|Reserved|
|3-2<br>—|Reserved|
|1-0<br>—|Reserved|



### 8.4.27 Parameter_n Register (REG_B26) 

##### Offset 

|Register|Offset|
|---|---|
|REG_B26|E8h|



##### Function 

Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

~~<mark>NOTE</mark>~~ 

- Any master can access holes (unimplemented registers) of SIUL2 through PDAC0. 

- After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

207 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19<br>18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|INMU|X_15|INMU|X_14|INMU|X_13|INMU|X_12|INMU|X_11|INMU|X_10|INMUX_9|INMUX_8|
|Reset|1|1|1|1|1|1|1|1|1|1|1|1|1<br>1|1<br>1|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3<br>2|1<br>0|
|R<br>W|INMU|X_7|INMU|X_6|INMU|X_5|INMU|X_4|INMU|X_3|INMU|X_2|INMUX_1|INMUX_0|
|Reset|1|1|1|1|1|1|1|1|1|1|1|1|1<br>1|1<br>1|



##### Fields 

|Field|Function|
|---|---|
|31-30|INMUX_15|
|INMUX_15|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|29-28|INMUX_14|
|INMUX_14|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|27-26|INMUX_13|
|INMUX_13|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|25-24|INMUX_12|
|INMUX_12|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|23-22|INMUX_11|
|INMUX_11|00 - SIUL2_VIRTWRAPPER_PDAC1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

208 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function||
|---|---|---|
||01<br>10<br>11-|- SIUL2_VIRTWRAPPER_PDAC2<br>- SIUL2_VIRTWRAPPER_PDAC4<br>SIUL2_VIRTWRAPPER_PDAC0|
|21-20|INMUX_10||
|INMUX_10|00|- SIUL2_VIRTWRAPPER_PDAC1|
||01|- SIUL2_VIRTWRAPPER_PDAC2|
||10<br>11-|- SIUL2_VIRTWRAPPER_PDAC4<br>SIUL2_VIRTWRAPPER_PDAC0|
|19-18|INMUX_9||
|INMUX_9|00|- SIUL2_VIRTWRAPPER_PDAC1|
||01|- SIUL2_VIRTWRAPPER_PDAC2|
||10<br>11-|- SIUL2_VIRTWRAPPER_PDAC4<br>SIUL2_VIRTWRAPPER_PDAC0|
|17-16|INMUX_8||
|INMUX_8|00|- SIUL2_VIRTWRAPPER_PDAC1|
||01|- SIUL2_VIRTWRAPPER_PDAC2|
||10<br>11-|- SIUL2_VIRTWRAPPER_PDAC4<br>SIUL2_VIRTWRAPPER_PDAC0|
|15-14|INMUX_7||
|INMUX_7|00|- SIUL2_VIRTWRAPPER_PDAC1|
||01|- SIUL2_VIRTWRAPPER_PDAC2|
||10<br>11-|- SIUL2_VIRTWRAPPER_PDAC4<br>SIUL2_VIRTWRAPPER_PDAC0|
|13-12|INMUX_6||
|INMUX_6|00|- SIUL2_VIRTWRAPPER_PDAC1|
||01|- SIUL2_VIRTWRAPPER_PDAC2|
||10|- SIUL2_VIRTWRAPPER_PDAC4|
||11-|SIUL2_VIRTWRAPPER_PDAC0|
|11-10|INMUX_5||
|INMUX_5|00|- SIUL2_VIRTWRAPPER_PDAC1|
||01|- SIUL2_VIRTWRAPPER_PDAC2|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

209 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|9-8|INMUX_4|
|INMUX_4|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|7-6|INMUX_3|
|INMUX_3|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|5-4|INMUX_2|
|INMUX_2|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|3-2|INMUX_1|
|INMUX_1|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|1-0|INMUX_0|
|INMUX_0|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

210 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

### 8.4.28 Parameter_n Register (REG_B27) 

##### Offset 

|Register|Offset|
|---|---|
|REG_B27|ECh|



##### Function 

Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

~~<mark>NOTE</mark>~~ 

- Any master can access holes (unimplemented registers) of SIUL2 through PDAC0. 

- After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/008_Virtualization_Wrapper_-VIRT_WRAPPER-/S32K3XXRM_数据表.pdf-0211-15.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved  Reserved  Reserved  Reserved  Reserved  Reserved  Reserved  INMUX_8<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>Reserved  Reserved  INMUX_5  Reserved  Reserved  INMUX_2  INMUX_1  INMUX_0<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29-28<br>—|Reserved|
|27-26|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

211 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|—<br>25-24<br>—|Reserved|
|23-22<br>—|Reserved|
|21-20<br>—|Reserved|
|19-18<br>—|Reserved|
|17-16|INMUX_8|
|INMUX_8|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|15-14<br>—|Reserved|
|13-12<br>—|Reserved|
|11-10|INMUX_5|
|INMUX_5|00 - SIUL2_VIRTWRAPPER_PDAC1<br>01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|9-8<br>—|Reserved|
|7-6<br>—|Reserved|
|5-4|INMUX_2|
|INMUX_2|00 - SIUL2_VIRTWRAPPER_PDAC1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

212 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||01 - SIUL2_VIRTWRAPPER_PDAC2<br>10 - SIUL2_VIRTWRAPPER_PDAC4<br>11-SIUL2_VIRTWRAPPER_PDAC0|
|3-2|INMUX_1|
|INMUX_1|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|
|1-0|INMUX_0|
|INMUX_0|00 - SIUL2_VIRTWRAPPER_PDAC1|
||01 - SIUL2_VIRTWRAPPER_PDAC2|
||10 - SIUL2_VIRTWRAPPER_PDAC4|
||11-SIUL2_VIRTWRAPPER_PDAC0|



### 8.4.29 Parameter_n Register (REG_C1039_1024) 

##### Offset 

|Register|Offset|
|---|---|
|REG_C1039_1024|100h|



##### Function 

Controls access to DISR0, DIRER0, DIRSR0, IREER0, IFEER0, IFER0, IFMCR, and IFCPR0 interrupt registers. Two bits assigned per PDAC slot have attributes of one of the implemented PDAC slots: 

- 00 - SIUL2_VIRTWRAPPER_PDAC1 

- 01 - SIUL2_VIRTWRAPPER_PDAC2 

- 10 - SIUL2_VIRTWRAPPER_PDAC4 

- 11-SIUL2_VIRTWRAPPER_PDAC0 

~~<mark>NOTE</mark>~~ 

After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will be generated. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

213 / 4640 

NXP Semiconductors 

Virtualization Wrapper (VIRT_WRAPPER) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/008_Virtualization_Wrapper_-VIRT_WRAPPER-/S32K3XXRM_数据表.pdf-0214-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>Reserved  INTC_CTRL<br>W<br>Reset 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-2<br>—|Reserved|
|1-0|Interrupt register control|
|INTC_CTRL|This bit controls the interrupt register.|



## 8.5 Glossary 

VM Virtualized module, such as SIUL2. 

PDAC Peripheral domain access control. PDAC and PDAC slot are interchangeable terms. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

214 / 4640 

