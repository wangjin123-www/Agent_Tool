NXP Semiconductors 

# Chapter 7 Miscellaneous System Control Module (MSCM) 

## 7.1 Chip-specific MSCM information 

### 7.1.1 MSCM instance 

This chip has one instance of MSCM. See the following table for details. 

Table 31. MSCM instance 

|Instance|S32K311/S32K312/S32K322/S32K342/S32K314/S32K324/S32K344/S32K358|
|---|---|
|MSCM|Yes|



~~<mark>NOTE</mark>~~ 

The XN_CTRL register is used to restrict execution from SRAM, including TCMs and their backdoors, which will be permanent until next device reset, while still allowing data R/W. 

XN_CTRL register is reserved for S32K3x4. 

## 7.2 Introduction 

MSCM contains registers for: 

- CPU configuration 

- On-chip memory control 

- Interrupt router control 

- Message-based interrupt configuration 

- Virtual management 

### 7.2.1 Features 

- Software-accessible processor core configuration information 

- Support for interrupt router control 

- Support for message-based interrupt configuration 

## 7.3 Functional description 

MSCM provides information of the system cores and can identify the core that is running currently. 

### 7.3.1 MSI routing 

MSIs are interrupts that are indirectly broadcast to a target core by writing configuration bits in MSCM. These MSIs can be initiated by one core targeting another core in the system (known as core-to-core interrupts). These MSIs are initiated via writes to Interrupt Router CPn Interrupt Generation (IRCP0IGR0 - IRCP2IGR3) and managed through Interrupt Router CPn Interrupt Status (IRCP0ISR0 - IRCP2ISR3), where n indicates the logical core number (0-1) and m represents the interrupt number (0-3). Cortex-M7_0 and Cortex-M7_1 cores can support up to four outstanding core-to-core interrupts. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

66 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/007_Miscellaneous_System_Control_Module_-MSCM-/S32K3XXRM_数据表.pdf-0067-01.png)


<!-- Start of picture text -->
Miscellaneous System Control Module (MSCM)<br>CPn Core-to-Core Int0 CPn Core-to-Core Int1<br>IRCP nlGR0 IRCP nlGR1<br>IRCP nlSR0 IRCP nlSR1<br>CPn Core-to-Core Int2 CPn Core-to-Core Int3<br>IRCP nlGR2 IRCP nlGR3<br>IRCP nlSR2 IRCP nlSR3<br>Figure 11. IRCPnIGRm/IRCPnISRm pairs for one core<br>CPn Core-to-Core Int0 CPn Core-to-Core Int1<br>IRCP nlGR0 IRCP nlGR1<br>IRCP nlSR0 IRCP nlSR1<br>CPn Core-to-Core Int2 CPn Core-to-Core Int3<br>IRCP nlGR2 IRCP nlGR3<br>IRCP nlSR2 IRCP nlSR3<br>CP0<br>CP1<br>Figure 12. IRCPnIGRm/IRCPnISRm pairs per core<br>int_en int_en<br>cp1_int cp0_int cp1_int cp0_int<br>int_en int0_en<br>cp1_int cp0_int cp1_int cp0_int<br>int_en int_en<br>cp1_int cp0_int cp1_int cp0_int<br>int_en int0_en<br>cp1_int cp0_int cp1_int cp0_int<br><!-- End of picture text -->

#### 7.3.1.1 Core-to-core MSIs 

The next figure depicts the sequence for initiating a core-to-core MSI, in which m represents the initiating core, n represents the target core, and x indicates the MSI number. CPm writes to IRCPnIGRx to initiate an MSI. The outstanding MSI that CPm initiates, targeting CPn, is reflected in the corresponding bit-mapped field in IRCPnISRx. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/007_Miscellaneous_System_Control_Module_-MSCM-/S32K3XXRM_数据表.pdf-0067-04.png)


<!-- Start of picture text -->
CPm writes to<br>wr 1<br>IRCP n IGR x IRCPnlGRx to generate<br>core-to-core<br>interrupt to CPn<br>CP m  masterID<br>IRCP n ISR x<br>int_en<br>1intcp_ cp0_int<br><!-- End of picture text -->

Figure 13. Initiating a core-to-core MSI via IRCPnIGRx/IRCPnISRx 

### 7.3.2 Interrupt steering and semaphores 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

67 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

#### 7.3.2.1 Interrupt handling overview 

The interrupt handling mechanisms of the Cortex-M7 cores are very similar. These cores have a NVIC tightly coupled to the processor core. The real-time performance of the cores means the NVIC directly provides an appropriate interrupt vector, in the form of the starting instruction address for the interrupt service routine, to the core. These core architectural features directly translate into a faster ISR entry and exit capabilities, coupled with an improved runtime performance. See the Arm modules and Arm core technical reference manuals for details. 

In this architecture, a total of 240 IRQs are supported, where this parameter is defined by the realistic limits of the NVIC implementation, both in terms of silicon size and supported frequency of operation. These 240 IRQs are split into a total of four directed requests and 236 shared peripheral requests. Unless noted otherwise, let the directed requests be defined as IRQ[3:0] and the shared peripheral requests as IRQ[239:4]. See the interrupt map file attached to this document for details. 

#### 7.3.2.2 MSCM interrupt router functional description 

As described in MSCM register descriptions, the interrupt routing registers enable the steering of requests to the processor cores. 

## 7.4 Memory map and register definition 

~~<mark>NOTE</mark>~~ 

The CP1 registers shown in the MSCM memory map section (from offset value 220h to 23Ch) are unavailable for the S32K312 and S32K311 variants. 

### 7.4.1 Core configuration registers 

These read-only registers contain data that defines the core setup for this chip. You can access the registers using 32-bit read references; other access sizes terminate with an error. Attempted write accesses to the read-only core configuration registers also terminate with an error. 

The core configuration portion of the MSCM programming model map is organized based on the logical core number, and not on any type of physical port number. The following table shows how the configuration is partitioned. 

Table 32. MSCM core configuration partitioning 

|Offset address|Purpose|
|---|---|
|range||
|0h–018h|Defines the generic core x configuration information. Only the Cortex-M7 cores on the chip can access this<br>region in either User or Privileged mode; reads by non-core bus masters (including the debugger) are treated<br>as read as zero (RAZ) accesses. Write attempts are not permitted and terminate with a system bus error.|
|020h–038h|Defines the configuration information for core 0 (CP0). Any bus master can access this region in either User<br>or Privileged mode. Write attempts are not permitted and terminate with a system bus error.|
|040h–058h|Defines the configuration information for core 1 (CP1). A bus master can access this region in either User or<br>Privileged mode. Write attempts are not permitted and terminate with a system bus error.|



~~<mark>NOTE</mark>~~ Attempted accesses to reserved locations are not permitted and terminate with a system bus error. 

### 7.4.2 Shared peripheral interrupt (SPI) routing 

The SPI router portion of MSCM provides a set of memory-mapped registers defining the interrupt routing for all the SPIs on this chip. 

### 7.4.3 MSCM register descriptions 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

68 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

#### 7.4.3.1 MSCM memory map 

MSCM base address: 4026_0000h 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|0h|Processor X Type (CPXTYPE)|32|RO|See<br>description|
|4h|Processor X Number (CPXNUM)|32|RO|See<br>description|
|8h|Processor X Revision (CPXREV)|32|RO|See<br>description|
|Ch|Processor X Configuration 0 (CPXCFG0)|32|RO|0602_0604h|
|10h|Processor X Configuration 1 (CPXCFG1)|32|RO|See<br>description|
|14h|Processor X Configuration 2 (CPXCFG2)|32|RO|See<br>description|
|18h|Processor x Configuration 3 (CPXCFG3)|32|RO|0000_000Bh|
|20h|Processor 0 Type (CP0TYPE)|32|RO|434D_3730h|
|24h|Processor 0 Number (CP0NUM)|32|RO|See<br>description|
|28h|Processor 0 Count (CP0REV)|32|RO|See<br>description|
|2Ch|Processor 0 Configuration 0 (CP0CFG0)|32|RO|0602_0604h|
|30h|Processor 0 Configuration 1 (CP0CFG1)|32|RO|0000_0000h|
|34h|Processor 0 Configuration 2 (CP0CFG2)|32|RO|See<br>description|
|38h|Processor 0 Configuration 3 (CP0CFG3)|32|RO|0000_000Bh|
|40h|Processor 1 Type (CP1TYPE)|32|RO|434D_3731h|
|44h|Processor 1 Number (CP1NUM)|32|RO|0000_0001h|
|48h|Processor 1 Count (CP1REV)|32|RO|See<br>description|
|4Ch|Processor 1 Configuration 0 (CP1CFG0)|32|RO|0602_0604h|
|50h|Processor 1 Configuration 1 (CP1CFG1)|32|RO|See<br>description|
|54h|Processor 1 Configuration 2 (CP1CFG2)|32|RO|See<br>description|
|58h|Processor 1 Configuration 3 (CP1CFG3)|32|RO|0000_000Bh|
|60h|Processor 2 Type (CP2TYPE)|32|RO|434D_3732h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

69 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|64h|Processor 2 Number (CP2NUM)|32|RO|0000_0002h|
|68h|Processor 2 Count (CP2REV)|32|RO|See<br>description|
|6Ch|Processor 2 Configuration 0 (CP2CFG0)|32|RO|0602_0604h|
|70h|Processor 2 Configuration 1 (CP2CFG1)|32|RO|See<br>description|
|74h|Processor 2 Configuration 2 (CP2CFG2)|32|RO|See<br>description|
|78h|Processor 2 Configuration 3 (CP2CFG3)|32|RO|0000_000Bh|
|200h|Interrupt Router CP0 Interrupt Status (IRCP0ISR0)|32|W1C|0000_0000h|
|204h|Interrupt Router CP0 Interrupt Generation (IRCP0IGR0)|32|WORZ|0000_0000h|
|208h|Interrupt Router CP0 Interrupt Status (IRCP0ISR1)|32|W1C|0000_0000h|
|20Ch|Interrupt Router CP0 Interrupt Generation (IRCP0IGR1)|32|WORZ|0000_0000h|
|210h|Interrupt Router CP0 Interrupt Status (IRCP0ISR2)|32|W1C|0000_0000h|
|214h|Interrupt Router CP0 Interrupt Generation (IRCP0IGR2)|32|WORZ|0000_0000h|
|218h|Interrupt Router CP0 Interrupt Status (IRCP0ISR3)|32|W1C|0000_0000h|
|21Ch|Interrupt Router CP0 Interrupt Generation (IRCP0IGR3)|32|WORZ|0000_0000h|
|220h|Interrupt Router CP1 Interrupt Status (IRCP1ISR0)|32|W1C|0000_0000h|
|224h|Interrupt Router CP1 Interrupt Generation (IRCP1IGR0)|32|WORZ|0000_0000h|
|228h|Interrupt Router CP1 Interrupt Status (IRCP1ISR1)|32|W1C|0000_0000h|
|22Ch|Interrupt Router CP1 Interrupt Generation (IRCP1IGR1)|32|WORZ|0000_0000h|
|230h|Interrupt Router CP1 Interrupt Status (IRCP1ISR2)|32|W1C|0000_0000h|
|234h|Interrupt Router CP1 Interrupt Generation (IRCP1IGR2)|32|WORZ|0000_0000h|
|238h|Interrupt Router CP1 Interrupt Status (IRCP1ISR3)|32|W1C|0000_0000h|
|23Ch|Interrupt Router CP1 Interrupt Generation (IRCP1IGR3)|32|WORZ|0000_0000h|
|240h|Interrupt Router CP2 Interrupt Status (IRCP2ISR0)|32|W1C|0000_0000h|
|244h|Interrupt Router CP2 Interrupt Generation (IRCP2IGR0)|32|WORZ|0000_0000h|
|248h|Interrupt Router CP2 Interrupt Status (IRCP2ISR1)|32|W1C|0000_0000h|
|24Ch|Interrupt Router CP2 Interrupt Generation (IRCP2IGR1)|32|WORZ|0000_0000h|
|250h|Interrupt Router CP2 Interrupt Status (IRCP2ISR2)|32|W1C|0000_0000h|
|254h|Interrupt Router CP2 Interrupt Generation (IRCP2IGR2)|32|WORZ|0000_0000h|
|258h|Interrupt Router CP2 Interrupt Status (IRCP2ISR3)|32|W1C|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

70 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|25Ch|Interrupt Router CP2 Interrupt Generation (IRCP2IGR3)|32|WORZ|0000_0000h|
|400h|Interrupt Router Configuration (IRCPCFG)|32|RW|0000_0000h|
|500h|Memory Execution Control (XN_CTRL)|32|RW|4000_0000h|
|600h|Enable Interconnect Error Detection (ENEDC)|32|RW|0000_0000h|
|604h|Enable Interconnect Error Detection (ENEDC1)|32|RW|0000_0000h|
|700h|AHB Gasket Configuration (IAHBCFGREG)|32|RW|0000_0000h|
|880h - A5Eh|Interrupt Router Shared Peripheral Routing Control (IRSPRC0 -<br>IRSPRC239)|16|RW|0007h|



#### 7.4.3.2 Processor X Type (CPXTYPE) 

##### Offset 

|Register|Offset|
|---|---|
|CPXTYPE|0h|



##### Function 

Provides a CPU-specific response indicating the personality of the core making the access. The 32-bit response includes four ASCII characters defining the CPU type (Cortex-M7 cores) along with a byte defining the logical revision number and a byte defining the instance number of the core. 

A read from Cortex-M7 returns the appropriate processor information. Reads from any other bus master return all 0s and attempted write accesses terminate with an error. 

Access: User or privileged read-only 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/007_Miscellaneous_System_Control_Module_-MSCM-/S32K3XXRM_数据表.pdf-0071-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R PERSONALITY<br>W<br>Reset u u u u u u u u u u u u u u u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R PERSONALITY<br>W<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

71 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Fields 

|Field|Function||
|---|---|---|
|31-0|Personality of CPx||
|PERSONALITY|Defines the processor personality for CPx.||
||Processor|Personality|
||CPx = Cortex-M7_0|43_4D_37_30h|
||CPx = Cortex-M7_1|43_4D_37_31h|
||CPx = Cortex-M7_2|43_4D_37_32h|



#### 7.4.3.3 Processor X Number (CPXNUM) 

##### Offset 

|Register|Offset|
|---|---|
|CPXNUM|4h|



##### Function 

Provides a CPU-specific response indicating the logical processor number of the core making the access. 

A read from the Cortex-M7 cores returns the appropriate processor information. Reads from any other bus master return all 0s and attempted write accesses terminate with an error. 

Access: User or privileged read-only 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||||0||||||||CPN||
|W|||||||||||||||||
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

72 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Fields 

|Field|Function|
|---|---|
|31-3|Reserved|
|—||
|2-0|Processor Number|
|CPN|This zero-filled word defines the logical processor number for CPx.|
||CPN in MSCM indicates only the on-platform cores and not the HSE_B core. CPN = 0<br>represents Cortex-M7_0 if it is a lockstep or dual core. In Lockstep mode, CPN = 1 does not<br>read fromProcessor X Number (CPXNUM).<br>~~NOTE~~|
||000b - Cortex-M7 core 0|
||001b - Cortex-M7 core 1<br>010b - Cortex-M7 core 2|



#### 7.4.3.4 Processor X Revision (CPXREV) 

##### Offset 

|Register|Offset|
|---|---|
|CPXREV|8h|



##### Function 

Provides a CPU-specific response indicating the logical revision number of the core. 

A read from the Cortex-M7 cores returns the appropriate processor information. Reads from any other bus master return all 0s and attempted write accesses terminate with an error. 

Access: User or privileged read-only 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/007_Miscellaneous_System_Control_Module_-MSCM-/S32K3XXRM_数据表.pdf-0073-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 RYPZ<br>W<br>Reset 0 0 0 0 0 0 0 0 u u u u u u u u<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

73 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Fields 

|Field|Function|
|---|---|
|31-8|Reserved|
|—||
|7-0|Processor Revision|
|RYPZ|Defines the processor revision for CPx.|
||For the Cortex-M7 cores in this chip, RYPZ = 12h corresponding to the r1p2 core release.|



#### 7.4.3.5 Processor X Configuration 0 (CPXCFG0) 

##### Offset 

|Register|Offset|
|---|---|
|CPXCFG0|Ch|



##### Function 

Provides a CPU-specific response detailing configuration information. In this case, it is information on Level 1 (L1) cache, if present. 

A read from Cortex-M7 returns the appropriate processor information. Reads from any other bus master return all 0s and attempted write accesses terminate with an error. 

Access: User or privileged read-only 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/007_Miscellaneous_System_Control_Module_-MSCM-/S32K3XXRM_数据表.pdf-0074-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R ICSZ  ICWY<br>W<br>Reset 0 0 0 0 0 1 1 0 0 0 0 0 0 0 1 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DCSZ  DCWY<br>W<br>Reset 0 0 0 0 0 1 1 0 0 0 0 0 0 1 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-24|Level 1 Instruction Cache Size|
|ICSZ||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

74 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||Provides an encoded value of the instruction cache size. The capacity of the memory is derived using the<br>formula 2<sup>(8+SZ)</sup>and expressed as bytes. Here, ICSZ is a non-zero value and ICSZ = 0 indicates that the<br>memory is not present.<br>For Cortex-M7 cores in this chip, DCSZ = 6h (16 KB).|
|23-16<br>ICWY|L1 Instruction Cache Ways<br>Provides the number of cache ways for the instruction cache.<br>For Cortex-M7 cores in this chip, ICWY = 2h (2-way set-associative).|
|15-8<br>DCSZ|L1 Data Cache Size<br>Provides an encoded value of the data cache size.<br>The capacity of the memory is derived using the formula 2<sup>(8+SZ)</sup>and expressed as bytes. Here, DCSZ is a<br>non-zero value and DCSZ = 0 indicates that the memory is not present.<br>For Cortex-M7 cores in this chip, DCSZ = 6h (16 KB).|
|7-0|L1 Data Cache Ways|
|DCWY|Provides the number of cache ways for the data cache.<br>For the Cortex-M7 cores in this chip, DCWY = 4h (4-way set-associative).|



#### 7.4.3.6 Processor X Configuration 1 (CPXCFG1) 

##### Offset 

|Register|Offset|
|---|---|
|CPXCFG1|10h|



##### Function 

Provides a CPU-specific response detailing configuration information. In this case, it is information on Level 2 (L2) cache, if present. 

A read from the Cortex-M7 cores returns the appropriate processor information. Reads from any other bus master return all 0s and attempted write accesses terminate with an error. 

Access: User or privileged read-only 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

75 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||L2|SZ|||||||L2|WY||||
|W|||||||||||||||||
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-24|L2 Cache Size|
|L2SZ|Provides an encoded value of the L2 cache size. The capacity of the memory is derived using the formula<br>2<sup>(8+SZ)</sup>and expressed as bytes. Here, L2SZ is a non-zero value, and L2SZ = 0 indicates that the memory<br>is not present.<br>For the Cortex-M7 cores in this chip, L2SZ = 0h (not present).|
|23-16|L2 Cache Ways|
|L2WY|Provides the number of cache ways for the L2 cache.<br>For the Cortex-M7 cores in this chip, L2WY = 0h (not present).|
|15-0<br>—|Reserved|



#### 7.4.3.7 Processor X Configuration 2 (CPXCFG2) 

##### Offset 

|Register|Offset|
|---|---|
|CPXCFG2|14h|



##### Function 

Provides a CPU-specific response detailing configuration information. In this case, it is information on tightly coupled local memories, if present. 

A read from the Cortex-M7 cores returns the appropriate processor information. Reads from any other bus master return all 0s and attempted write accesses terminate with an error. 

Access: User or privileged read-only 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

76 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||DTC|MSZ|||||||ITC|MSZ||||
|W|||||||||||||||||
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-24|Tightly Coupled Data Memory Size|
|DTCMSZ|Provides an encoded value of the tightly coupled local data memory size. The capacity of the memory is<br>derived using the formula 2<sup>(8+SZ)</sup>and expressed as bytes. Here, DTCMSZ is a non-zero value and DTCMSZ<br>= 0 indicates that the memory is not present.<br>For the Cortex-M7 cores in this chip:<br>• DTCMSZ = 08 in Decoupled mode (64 KB)<br>• DTCMSZ = 09 for Cortex-M7_0 in Lockstep mode (128 KB)|
|23-16|Instruction Tightly Coupled Memory Size|
|ITCMSZ|Provides an encoded value of the tightly coupled local instruction memory size. The capacity of the memory<br>is derived using the formula 2<sup>(8+SZ)</sup>and expressed as bytes. Here, ITCMSZ is a non-zero value, and<br>ITCMSZ = 0 indicates that the memory is not present.<br>For the Cortex-M7 cores in this chip:<br>• ITCMSZ = 07 in Decoupled mode (32 KB)<br>• ITCMSZ = 08 for Cortex-M7_0 in Lockstep mode (64 KB)|
|15-0<br>—|Reserved|



#### 7.4.3.8 Processor x Configuration 3 (CPXCFG3) 

##### Offset 

|Register|Offset|
|---|---|
|CPXCFG3|18h|



##### Function 

Provides a CPU-specific response detailing configuration information. In this case, it is information on processor options. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

77 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

A privileged read from Cortex-M7 returns the appropriate processor information. Reads from any other bus master return all 0s and attempted write accesses terminate with an error. 

Access: User or privileged read-only 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||||||||0||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||0||||||CPY|CMP|MMU|SIMD|FPU|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|1|0|1|1|



##### Fields 

|Field|Function|
|---|---|
|31-5<br>—|Reserved|
|4<br>CPY|Cryptography<br>Indicates if the cryptography extensions are supported in the core.<br>For the Cortex-M7 cores in this chip, CPY = 0h.<br>0b - Not supported<br>1b - Supported|
|3<br>CMP|Core Memory Protection Unit<br>Indicates if the core memory protection hardware is included in this core.<br>For the Cortex-M7 cores in this chip, CMP = 1h.<br>0b - Not included<br>1b - Included|
|2<br>MMU|Memory Management Unit<br>Indicates if virtual management capabilities are supported in this core.<br>For the Cortex-M7 cores in this chip, MMU = 0h.<br>0b - Not supported<br>1b - Supported|
|1<br>SIMD|SIMD/NEON Instruction Support|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

78 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||Indicates if the instruction set extensions supporting SIMD and/or NEON capabilities are included in<br>the processor.<br>For the Cortex-M7 cores in this chip, SIMD = 1h.<br>0b - Not included<br>1b - Included|
|0|Floating Point Unit|
|FPU|Indicates if hardware support for floating point capabilities is provided in the processor.<br>For the Cortex-M7 cores in this chip, FPU = 1h.<br>0b - Not provided<br>1b - Provided|



#### 7.4.3.9 Processor 0 Type (CP0TYPE) 

##### Offset 

|Register|Offset|
|---|---|
|CP0TYPE|20h|



##### Function 

Defines the configuration information for processor 0 (CP0). It has the same field definitions and functionality as provided in Processor X Type (CPXTYPE). 

A read from any bus master returns the appropriate processor information and attempted write accesses terminate with an error. 

Access: User or privileged read-only 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||PERSO|NALITY||||||||
|W|||||||||||||||||
|Reset|0|1|0|0|0|0|1|1|0|1|0|0|1|1|0|1|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||PERSO|NALITY||||||||
|W|||||||||||||||||
|Reset|0|0|1|1|0|1|1|1|0|0|1|1|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

79 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Fields 

|Field|Function|
|---|---|
|31-0|Processor Personality|
|PERSONALITY|This field defines the processor personality for CP0.|
||For Cortex-M7 core 0, personality = 43_4D_37_30h.|



#### 7.4.3.10 Processor 0 Number (CP0NUM) 

##### Offset 

|Register|Offset|
|---|---|
|CP0NUM|24h|



##### Function 

Defines the configuration information for processor 0 (CP0). It has the same field definitions and functionality as provided in Processor X Number (CPXNUM). 

A privileged read from any bus master returns the appropriate processor information and attempted write accesses terminate with an error. 

Access: User or privileged read-only 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/007_Miscellaneous_System_Control_Module_-MSCM-/S32K3XXRM_数据表.pdf-0080-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 CPN<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 u u<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-2<br>—|Reserved|
|1-0|Processor Number|
|CPN|This zero-filled word defines the logical processor number for CP0.|
||For processor Cortex-M7 core 0, processor number = 0.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

80 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

#### 7.4.3.11 Processor 0 Count (CP0REV) 

##### Offset 

|Register|Offset|
|---|---|
|CP0REV|28h|



##### Function 

Defines the configuration information for processor 0 (CP0). It has the same field definitions and functionality as provided in Processor X Revision (CPXREV). 

A read from any bus master returns the appropriate processor information and attempted write accesses terminate with an error. Access: User or privileged read-only 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/007_Miscellaneous_System_Control_Module_-MSCM-/S32K3XXRM_数据表.pdf-0081-09.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 RYPZ<br>W<br>Reset 0 0 0 0 0 0 0 0 u u u u u u u u<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-8|Reserved|
|—||
|7-0|Processor Revision|
|RYPZ|Defines the processor revision for CP0.|
||For the Cortex-M7 processor, RYPZ = 12h corresponding to the r1p2 core release.|



#### 7.4.3.12 Processor 0 Configuration 0 (CP0CFG0) 

##### Offset 

|Register|Offset|
|---|---|
|CP0CFG0|2Ch|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

81 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Function 

Defines the configuration information for processor 0 (CP0). It has the same field definitions and functionality as provided in Processor X Configuration 0 (CPXCFG0). 

A read from any bus master returns the appropriate processor information and attempted write accesses terminate with an error. Access: User or privileged read-only 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||IC|SZ|||||||ICW|Y||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|1|1|0|0|0|0|0|0|0|1|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||DC|SZ|||||||DCW|Y||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|1|1|0|0|0|0|0|0|1|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-24<br>ICSZ|Level 1 Instruction Cache Size<br>Provides an encoded value of the instruction cache size. The capacity of the memory is derived using the<br>formula 2<sup>(8+SZ)</sup>and expressed as bytes. Here, ICSZ is a non-zero value, and ICSZ = 0 indicates that the<br>memory is not present.<br>For Cortex-M7 cores in this chip, DCSZ = 6h (16 KB).|
|23-16<br>ICWY|L1 Instruction Cache Ways<br>Provides the number of cache ways for the instruction cache.<br>For the Cortex-M7 cores in this chip, ICWY = 2h (2-way set-associative).|
|15-8|L1 Data Cache Size|
|DCSZ|Provides an encoded value of the data cache size.<br>The capacity of the memory is derived using the formula 2<sup>(8+SZ)</sup>and expressed as bytes. Here, DCSZ is a<br>non-zero value, and DCSZ = 0 indicates that the memory is not present.<br>For Cortex-M7 cores in this chip, DCSZ = 6h (16 KB).|
|7-0|L1 Data Cache Ways|
|DCWY|Provides the number of cache ways for the data cache.<br>For the Cortex-M7 cores in this chip, DCWY = 4h (4-way set-associative).|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

82 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

#### 7.4.3.13 Processor 0 Configuration 1 (CP0CFG1) 

##### Offset 

|Register|Offset|
|---|---|
|CP0CFG1|30h|



##### Function 

Defines the configuration information for processor 0 (CP0). It has the same field definitions and functionality as provided in Processor X Configuration 1 (CPXCFG1). 

A privileged read from any bus master returns the appropriate processor information and attempted write accesses terminate with an error. 

Access: User or privileged read-only 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/007_Miscellaneous_System_Control_Module_-MSCM-/S32K3XXRM_数据表.pdf-0083-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R L2SZ  L2WY<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-24|L2 Cache Size|
|L2SZ|Provides an encoded value of the L2 cache size.<br>The capacity of the memory is derived using the formula 2<sup>(8+SZ)</sup>and expressed as bytes. Here, L2SZ is a<br>non-zero value, and L2SZ = 0 indicates that the memory is not present.<br>For the Cortex-M7 cores in this chip, L2SZ = 0h (not present).|
|23-16|L2 Cache Ways|
|L2WY|Provides the number of cache ways for the L2 cache.<br>For the Cortex-M7 cores in this chip, L2WY = 0h (not present).|
|15-0<br>—|Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

83 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

#### 7.4.3.14 Processor 0 Configuration 2 (CP0CFG2) 

##### Offset 

|Register|Offset|
|---|---|
|CP0CFG2|34h|



##### Function 

Defines the configuration information for processor 0 (CP0). It has the same field definitions and functionality as provided in Processor X Configuration 2 (CPXCFG2). 

A privileged read from any bus master returns the appropriate processor information and attempted write accesses terminate with an error. 

Access: User or privileged read-only 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/007_Miscellaneous_System_Control_Module_-MSCM-/S32K3XXRM_数据表.pdf-0084-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R DTCMSZ  ITCMSZ<br>W<br>Reset u u u u u u u u u u u u u u u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-24|Tightly Coupled Data Memory Size|
|DTCMSZ|Provides an encoded value of the tightly coupled local data memory size.<br>The capacity of the memory is derived using the formula 2<sup>(8+SZ)</sup>and expressed as bytes. Here, TMLSZ is<br>a non-zero value, and TMLSZ = 0 indicates that the memory is not present.<br>For the Cortex-M7 cores in this chip:<br>• DTCMSZ = 8h in Decoupled mode (64 KB)<br>• DTCMSZ = 9h in Lockstep mode (128 KB)|
|23-16|Instruction Tightly Coupled Memory Size|
|ITCMSZ|Provides an encoded value of the tightly coupled local instruction memory size.<br>The capacity of the memory is derived using the formula 2<sup>(8+SZ)</sup>and expressed as bytes. Here, TMUSZ is<br>a non-zero value, and TMUSZ = 0 indicates that the memory is not present.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

84 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||For the Cortex-M7 cores in this chip:|
||• ITCMSZ = 7h in Decoupled mode (32 KB)|
||• ITCMSZ = 8h in Lockstep mode (64 KB)|
|15-0<br>—|Reserved|



#### 7.4.3.15 Processor 0 Configuration 3 (CP0CFG3) 

##### Offset 

|Register|Offset|
|---|---|
|CP0CFG3|38h|



##### Function 

Defines the configuration information for processor 0 (CP0). It has the same field definitions and functionality as provided in Processor x Configuration 3 (CPXCFG3). 

A privileged read from any bus master returns the appropriate processor information and attempted write accesses terminate with an error. 

Access: User or privileged read-only 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/007_Miscellaneous_System_Control_Module_-MSCM-/S32K3XXRM_数据表.pdf-0085-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 CPY  CMP  MMU  SIMD  FPU<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 1<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-5<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

85 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|4<br>CPY|Cryptography<br>Indicates if the cryptography extensions are supported in the core.<br>For the Cortex-M7 cores in this chip, CPY = 0h.<br>0b - Not supported<br>1b - Supported|
|3<br>CMP|Core Memory Protection Unit<br>Indicates if the core memory protection hardware is included in this core.<br>For the Cortex-M7 cores in this chip, CMP = 1h.<br>0b - Not included<br>1b - Included|
|2<br>MMU|Memory Management Unit<br>Indicates if virtual management capabilities are supported in this core.<br>For the Cortex-M7 cores in this chip, MMU = 0h.<br>0b - Not supported<br>1b - Supported|
|1<br>SIMD|SIMD/NEON Instruction Support<br>Indicates if the instruction set extensions supporting SIMD and/or NEON capabilities are included in<br>the processor.<br>For the Cortex-M7 cores in this chip, SIMD = 1h.<br>0b - Not included<br>1b - Included|
|0<br>FPU|Floating Point Unit<br>Indicates if hardware support for floating point capabilities is provided in the processor.<br>For the Cortex-M7 cores in this chip, FPU = 1h.<br>0b - Not provided<br>1b - Provided|



#### 7.4.3.16 Processor 1 Type (CP1TYPE) 

##### Offset 

|Register|Offset|
|---|---|
|CP1TYPE|40h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

86 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Function 

Defines the configuration information for processor 1 (CP1). It has the same field definitions and functionality as provided in Processor X Type (CPXTYPE). 

A read from any bus master returns the appropriate processor information and attempted write accesses terminate with an error. Access: User or privileged read-only 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/007_Miscellaneous_System_Control_Module_-MSCM-/S32K3XXRM_数据表.pdf-0087-06.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R PERSONALITY<br>W<br>Reset 0 1 0 0 0 0 1 1 0 1 0 0 1 1 0 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R PERSONALITY<br>W<br>Reset 0 0 1 1 0 1 1 1 0 0 1 1 0 0 0 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Personality Processor|
|PERSONALITY|Defines the processor personality for CP1.|
||CP1 = Cortex-M7 core 1 and processor personality = 43_4D_37_31h.|



#### 7.4.3.17 Processor 1 Number (CP1NUM) 

##### Offset 

|Register|Offset|
|---|---|
|CP1NUM|44h|



##### Function 

Defines the configuration information for processor 1 (CP1). It has the same field definitions and functionality as provided in Processor X Number (CPXNUM). 

A read from any bus master returns the appropriate processor information and attempted write accesses terminate with an error. 

Access: User or privileged read-only 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

87 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/007_Miscellaneous_System_Control_Module_-MSCM-/S32K3XXRM_数据表.pdf-0088-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 CPN<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-2<br>—|Reserved|
|1-0|Processor Number|
|CPN|This zero-filled word defines the logical processor number for CP1.|
||For the Cortex-M7 core 1 processor, the processor number = 1.|



#### 7.4.3.18 Processor 1 Count (CP1REV) 

##### Offset 

|Register|Offset|
|---|---|
|CP1REV|48h|



##### Function 

Defines the configuration information for processor 1 (CP1). It has the same field definitions and functionality as provided in Processor X Revision (CPXREV). 

A read from any bus master returns the appropriate processor information and attempted write accesses terminate with an error. 

Access: User or privileged read-only 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

88 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||0|||||||RY|PZ||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|u|u|u|u|u|u|u|u|



##### Fields 

|Field|Function|
|---|---|
|31-8|Reserved|
|—||
|7-0|Processor Revision|
|RYPZ|Defines the processor revision for CP1.|
||For the Cortex-M7 processor, RYPZ = 12h corresponding to the r1p2 core release.|



#### 7.4.3.19 Processor 1 Configuration 0 (CP1CFG0) 

##### Offset 

|Register|Offset|
|---|---|
|CP1CFG0|4Ch|



##### Function 

Defines the configuration information for processor 1 (CP1). It has the same field definitions and functionality as provided in Processor X Configuration 0 (CPXCFG0). 

A privileged read from any bus master returns the appropriate processor information and attempted write accesses terminate with an error. 

Access: User or privileged read-only 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

89 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||IC|SZ|||||||IC|WY||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|1|1|0|0|0|0|0|0|0|1|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||DC|SZ|||||||DC|WY||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|1|1|0|0|0|0|0|0|1|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-24<br>ICSZ|Level 1 Instruction Cache Size<br>Provides an encoded value of the instruction cache size.<br>The capacity of the memory is derived using the formula 2<sup>(8+SZ)</sup>and expressed as bytes. Here, ICSZ is a<br>non-zero value, and ICSZ = 0 indicates that the memory is not present.<br>For Cortex-M7 cores in this chip, DCSZ = 6h (16 KB).|
|23-16<br>ICWY|Level 1 Instruction Cache Ways<br>Provides the number of cache ways for the instruction cache.<br>For the Cortex-M7 cores in this chip, ICWY = 2h (2-way set-associative).|
|15-8<br>DCSZ|L1 Data Cache Size<br>Provides an encoded value of the data cache size.<br>The capacity of the memory is derived using the formula 2<sup>(8+SZ)</sup>and expressed as bytes. Here, DCSZ is a<br>non-zero value, and DCSZ = 0 indicates that the memory is not present.<br>For Cortex-M7 cores in this chip, DCSZ = 6h (16 KB).|
|7-0|L1 Data Cache Ways|
|DCWY|Provides the number of cache ways for the data cache.<br>For the Cortex-M7 cores in this chip, DCWY = 4h (4-way set-associative).|



#### 7.4.3.20 Processor 1 Configuration 1 (CP1CFG1) 

##### Offset 

|Register|Offset|
|---|---|
|CP1CFG1|50h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

90 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Function 

Defines the configuration information for processor 1 (CP1). It has the same field definitions and functionality as provided in Processor X Configuration 1 (CPXCFG1). 

A privileged read from any bus master returns the appropriate processor information and attempted write accesses terminate with an error. 

Access: User or privileged read-only 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/007_Miscellaneous_System_Control_Module_-MSCM-/S32K3XXRM_数据表.pdf-0091-07.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R L2SZ  L2WY<br>W<br>Reset u u u u u u u u u u u u u u u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-24|L2 Cache Size|
|L2SZ|Provides an encoded value of the L2 cache size.<br>The capacity of the memory is derived using the formula 2<sup>(8+SZ)</sup>and expressed as bytes. Here, L2SZ is a<br>non-zero value, and L2SZ = 0 indicates that the memory is not present.<br>For the Cortex-M7 cores in this chip, L2SZ = 0h (not present).|
|23-16|L2 Cache Ways|
|L2WY|Provides the number of cache ways for the L2 cache.<br>For the Cortex-M7 cores in this chip, L2WY = 0h (not present).|
|15-0<br>—|Reserved|



#### 7.4.3.21 Processor 1 Configuration 2 (CP1CFG2) 

##### Offset 

|Register|Offset|
|---|---|
|CP1CFG2|54h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

91 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Function 

Defines the configuration information for processor 1 (CP1). It has the same field definitions and functionality as provided in Processor X Configuration 2 (CPXCFG2). 

A privileged read from any bus master returns the appropriate processor information and attempted write accesses terminate with an error. 

Access: User or privileged read-only 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||DTC|MSZ|||||||ITC|MSZ||||
|W|||||||||||||||||
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||0|||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-24|Tightly Coupled Data Memory Size|
|DTCMSZ|Provides an encoded value of the tightly coupled local data memory size.<br>The capacity of the memory is derived using the formula 2<sup>(8+SZ)</sup>and expressed as bytes. Here, TMLSZ is<br>a non-zero value, and TMLSZ = 0 indicates that the memory is not present.<br>For the Cortex-M7 cores in this chip, DTCMSZ = 8h in Decoupled mode (64 KB), and this value is not<br>applicable in Lockstep mode.|
|23-16|Instruction Tightly Coupled Memory Size|
|ITCMSZ|Provides an encoded value of the tightly coupled local instruction memory size. The capacity of the memory<br>is derived using the formula 2<sup>(8+SZ)</sup>and expressed as bytes. Here, TMUSZ is a non-zero value, and TMUSZ<br>= 0 indicates that the memory is not present.<br>For the Cortex-M7 cores in this chip, ITCMSZ = 7h in Decoupled mode (32 KB); this value is not applicable<br>in Lockstep mode.|
|15-0<br>—|Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

92 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

#### 7.4.3.22 Processor 1 Configuration 3 (CP1CFG3) 

##### Offset 

|Register|Offset|
|---|---|
|CP1CFG3|58h|



##### Function 

Defines the configuration information for processor 1 (CP1). It has the same field definitions and functionality as provided in Processor x Configuration 3 (CPXCFG3). 

A privileged read from any bus master returns the appropriate processor information and attempted write accesses terminate with an error. 

Access: User or privileged read-only 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/007_Miscellaneous_System_Control_Module_-MSCM-/S32K3XXRM_数据表.pdf-0093-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 CPY  CMP  MMU  SIMD  FPU<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-5|Reserved|
|—||
|4|Cryptography|
|CPY|Indicates if cryptography extensions are supported in the core.<br>For the Cortex-M7 cores in this chip, CPY = 0h.<br>0b - Not supported|
||1b - Supported|
|3|Core Memory Protection Unit|
|CMP|Indicates if the core memory protection hardware is included in this core.|
||For the Cortex-M7 cores in this chip, CMP = 1h.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

93 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Not included<br>1b - Included|
|2<br>MMU|Memory Management Unit<br>Indicates if virtual management capabilities are supported in this core.<br>For the Cortex-M7 cores in this chip, MMU = 0h.<br>0b - Not supported<br>1b - Supported|
|1<br>SIMD|SIMD/NEON Instruction Support<br>Indicates if the instruction set extensions supporting SIMD and/or NEON capabilities are included in<br>the processor.<br>For the Cortex-M7 cores in this chip, SIMD = 1h.<br>0b - Not included<br>1b - Included|
|0<br>FPU|Floating Point Unit<br>Indicates if the processor includes hardware support for floating point capabilities.<br>For the Cortex-M7 cores in this chip, FPU = 1h.<br>0b - Not included<br>1b - Included|



#### 7.4.3.23 Processor 2 Type (CP2TYPE) 

##### Offset 

|Register|Offset|
|---|---|
|CP2TYPE|60h|



##### Function 

Defines the configuration information for processor 2 (CP2). It has the same field definitions and functionality as provided in Processor X Type (CPXTYPE). 

A read from any bus master returns the appropriate processor information and attempted write accesses terminate with an error. 

Access: User or privileged read-only 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

94 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/007_Miscellaneous_System_Control_Module_-MSCM-/S32K3XXRM_数据表.pdf-0095-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R PERSONALITY<br>W<br>Reset 0 1 0 0 0 0 1 1 0 1 0 0 1 1 0 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R PERSONALITY<br>W<br>Reset 0 0 1 1 0 1 1 1 0 0 1 1 0 0 1 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Processor Personality|
|PERSONALITY|Defines the processor personality for CP2.|
||CP2 = Cortex-M7 core 2 and processor personality = 43_4D_37_32h.|



#### 7.4.3.24 Processor 2 Number (CP2NUM) 

##### Offset 

|Register|Offset|
|---|---|
|CP2NUM|64h|



##### Function 

Defines the configuration information for processor 2 (CP2). It has the same field definitions and functionality as provided in Processor X Number (CPXNUM). 

A read from any bus master returns the appropriate processor information and attempted write accesses terminate with an error. 

Access: User or privileged read-only 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

95 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/007_Miscellaneous_System_Control_Module_-MSCM-/S32K3XXRM_数据表.pdf-0096-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 CPN<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-2<br>—|Reserved|
|1-0|Processor Number|
|CPN|This zero-filled word defines the logical processor number for CP2.|
||For Cortex-M7 core 2, processor number = 2.|



#### 7.4.3.25 Processor 2 Count (CP2REV) 

##### Offset 

|Register|Offset|
|---|---|
|CP2REV|68h|



##### Function 

Defines the configuration information for processor 2 (CP2). It has the same field definitions and functionality as provided in Processor X Revision (CPXREV). 

A read from any bus master returns the appropriate processor information and attempted write accesses terminate with an error. 

Access: User or privileged read-only 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

96 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||0|||||||RY|PZ||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|u|u|u|u|u|u|u|u|



##### Fields 

|Field|Function|
|---|---|
|31-8|Reserved|
|—||
|7-0|Processor Revision|
|RYPZ|Defines the processor revision for CP2.|
||For the Cortex-M7 processor, RYPZ = 12h corresponding to the r1p2 core release.|



#### 7.4.3.26 Processor 2 Configuration 0 (CP2CFG0) 

##### Offset 

|Register|Offset|
|---|---|
|CP2CFG0|6Ch|



##### Function 

Defines the configuration information for processor 2 (CP2). It has the same field definitions and functionality as provided in Processor X Configuration 0 (CPXCFG0). 

A privileged read from any bus master returns the appropriate processor information and attempted write accesses terminate with an error. 

Access: User or privileged read-only 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

97 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||IC|SZ|||||||IC|WY||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|1|1|0|0|0|0|0|0|0|1|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||DC|SZ|||||||DC|WY||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|1|1|0|0|0|0|0|0|1|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-24<br>ICSZ|Level 1 Instruction Cache Size<br>Provides an encoded value of the instruction cache size.<br>The capacity of the memory is derived using the formula 2<sup>(8+SZ)</sup>and expressed as bytes. Here, ICSZ is a<br>non-zero value, and ICSZ = 0 indicates that the memory is not present.<br>For the Cortex-M7 cores in this chip, ICSZ = 6h (16 KB).|
|23-16<br>ICWY|Level 1 Instruction Cache Ways<br>Provides the number of cache ways for the instruction cache.<br>For the Cortex-M7 cores in this chip, ICWY = 2h (2-way set-associative).|
|15-8<br>DCSZ|L1 Data Cache Size<br>Provides an encoded value of the data cache size.<br>The capacity of the memory is derived using the formula 2<sup>(8+SZ)</sup>and expressed as bytes. Here, DCSZ is a<br>non-zero value, and DCSZ = 0 indicates that the memory is not present.<br>For the Cortex-M7 cores in this chip, DCSZ = 6h (16 KB).|
|7-0|L1 Data Cache Ways|
|DCWY|Provides the number of cache ways for the data cache.<br>For the Cortex-M7 cores in this chip, DCWY = 4h (4-way set-associative).|



#### 7.4.3.27 Processor 2 Configuration 1 (CP2CFG1) 

##### Offset 

|Register|Offset|
|---|---|
|CP2CFG1|70h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

98 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Function 

Defines the configuration information for processor 2 (CP2). It has the same field definitions and functionality as provided in Processor X Configuration 1 (CPXCFG1). 

A privileged read from any bus master returns the appropriate processor information and attempted write accesses terminate with an error. 

Access: User or privileged read-only 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/007_Miscellaneous_System_Control_Module_-MSCM-/S32K3XXRM_数据表.pdf-0099-07.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R L2SZ  L2WY<br>W<br>Reset u u u u u u u u u u u u u u u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-24|L2 Cache Size|
|L2SZ|Provides an encoded value of the L2 cache size. The capacity of the memory is derived using the formula<br>2<sup>(8+SZ)</sup>and expressed as bytes. Here, L2SZ is a non-zero value, and L2SZ = 0 indicates that the memory<br>is not present.<br>For the Cortex-M7 cores in this chip, L2SZ = 0h (not present).|
|23-16|L2 Cache Ways|
|L2WY|Provides the number of cache ways for the L2 cache.<br>For the Cortex-M7 cores in this chip, L2WY = 0h (not present).|
|15-0<br>—|Reserved|



#### 7.4.3.28 Processor 2 Configuration 2 (CP2CFG2) 

##### Offset 

|Register|Offset|
|---|---|
|CP2CFG2|74h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

99 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Function 

Defines the configuration information for processor 2 (CP2). It has the same field definitions and functionality as provided in Processor X Configuration 2 (CPXCFG2). 

A privileged read from any bus master returns the appropriate processor information and attempted write accesses terminate with an error. 

Access: User or privileged read-only 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||DTC|MSZ|||||||ITC|MSZ||||
|W|||||||||||||||||
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||0|||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-24|Tightly Coupled Data Memory Size|
|DTCMSZ|Provides an encoded value of the tightly coupled local data memory size.<br>The capacity of the memory is derived using the formula 2<sup>(8+SZ)</sup>and expressed as bytes. Here, TMLSZ is<br>a non-zero value, and TMLSZ = 0 indicates that the memory is not present.<br>For the Cortex-M7 cores in this chip, DTCMSZ = 8h in Decoupled mode (64 KB), and this value is not<br>applicable in Lockstep mode.|
|23-16|Instruction Tightly Coupled Memory Size|
|ITCMSZ|Provides an encoded value of the tightly coupled local instruction memory size. The capacity of the memory<br>is derived using the formula 2<sup>(8+SZ)</sup>and expressed as bytes. Here, TMUSZ is a non-zero value, and TMUSZ<br>= 0 indicates that the memory is not present.<br>For the Cortex-M7 cores in this chip, ITCMSZ = 7h in Decoupled mode (32 KB); this value is not applicable<br>in Lockstep mode.|
|15-0<br>—|Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

100 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

#### 7.4.3.29 Processor 2 Configuration 3 (CP2CFG3) 

##### Offset 

|Register|Offset|
|---|---|
|CP2CFG3|78h|



##### Function 

Defines the configuration information for processor 2 (CP2). It has the same field definitions and functionality as provided in Processor x Configuration 3 (CPXCFG3). 

A privileged read from any bus master returns the appropriate processor information and attempted write accesses terminate with an error. 

Access: User or privileged read-only 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/007_Miscellaneous_System_Control_Module_-MSCM-/S32K3XXRM_数据表.pdf-0101-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 CPY  CMP  MMU  SIMD  FPU<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-5|Reserved|
|—||
|4|Cryptography|
|CPY|Indicates whether cryptography extensions are supported in the core.<br>For the Cortex-M7 cores in this chip, CPY = 0h.<br>0b - Not supported|
||1b - Supported|
|3|Core Memory Protection Unit|
|CMP|Indicates whether the core memory protection hardware is included in this core.|
||For the Cortex-M7 cores in this chip, CMP = 1h.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

101 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Not included<br>1b - Included|
|2<br>MMU|Memory Management Unit<br>Indicates whether virtual management capabilities are supported in this core.<br>For the Cortex-M7 cores in this chip, MMU = 0h.<br>0b - Not supported<br>1b - Supported|
|1|SIMD/NEON Instruction Support|
|SIMD|Indicates whether the instruction set extensions supporting SIMD and/or NEON capabilities are included in<br>the processor.<br>For the Cortex-M7 cores in this chip, SIMD = 1h.<br>0b - Not included<br>1b - Included|
|0|Floating Point Unit|
|FPU|Indicates whether the processor includes hardware support for floating point capabilities.<br>For the Cortex-M7 cores in this chip, FPU = 1h.<br>0b - Not included<br>1b - Included|



#### 7.4.3.30 Interrupt Router CPn Interrupt Status (IRCP0ISR0 - IRCP2ISR3) 

##### Offset 

For n = 0 to 2; m = 0 to 3: 

|Register|Offset|
|---|---|
|IRCPnISRm|200h + (n × 20h) + (m × 8h)|



##### Function 

Provides an interrupt bit map, where each bit defines the state of a unique MSI based on the initiating core. An MSI interrupt clears in an interrupt service routine by writing 1 to the appropriate field in IRCPnISRm. 

In this discussion, CPm represents the initiating core and CPn represents the target core for a core-to-core interrupt. For more information on interrupt source mapping, see the interrupt map file attached to this document. 

For read access: 

- Reads to IRCPnISRm are only accessible in Privileged mode using 32-bit (word) accesses. 

- Privileged 32-bit read accesses from non-core (and non-debugger) bus masters are treated as RAZ. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

102 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

- Attempted accesses in User mode or the ones using a size other than 32 bits are not permitted. They terminate with an error. 

- When CPn requests to read IRCPnISRm, MSCM returns the entire content of IRCPnISRm. 

- When a trusted core, as the IRCPCFG register indicates, requests to read IRCPnISRm, MSCM returns the entire content of IRCPnISRm. 

- When the debugger requests to read IRCPnISRm, MSCM returns the entire content of IRCPnISRm. 

- When CPm requests to read IRCPnISRm, MSCM returns the value of the corresponding status, CPm_INT, while not exposing all the other pending interrupts that the cores initiated. 

- When CPm requests to read IRCPnISRm, MSCM returns the value of the corresponding status, CPm_INT, in bit position 0, reflecting how CPm set the MSI when it wrote to IRCPnIGRm. All the other fields on the returned read value are zero-filled. 

For write access: 

- Writes to IRCPnISRm are only accessible in Privileged mode using 32-bit (word) accesses. 

- Attempted accesses in User mode or the ones using a size other than 32 bits are not permitted. They terminate with an error. 

- Writes to IRCPnISRm follow the Write 1 to Clear (W1C) protocol, whereby writing 1 causes the corresponding field to become 0, and writing 0 is ignored. 

- The target core, CPn, has full access to write to all the fields of IRCPnISRm. 

- A trusted core, as the IRCPCFG register indicates, has full access to write to all the fields of IRCPnISRm. 

- When CPm is different from CPn, the W1C action by CPm only clears IRCPnISRm[CPm_INT]. 

- The CPm field must present W1C in bit position 0 to clear its corresponding interrupt. Write data bits 1-31 that CPm presents are ignored. 

- Privileged write accesses from the non-core (and non-debugger) bus masters are treated as Writes Ignored (WI). 

- Privileged write accesses from the debugger are treated as WI. 

Access: Privileged mode only 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/007_Miscellaneous_System_Control_Module_-MSCM-/S32K3XXRM_数据表.pdf-0103-20.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>CP2_ CP1_ CP0_<br>R 0<br>INT  INT  INT<br>W W1C W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function||
|---|---|---|
|31-3|Reserved||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

103 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|2|CP2-to-CPn Interrupt|
|CP2_INT|Generates a directed interrupt initiated by core 2 targeting core n, if the appropriate interrupt routing bit<br>is enabled. The interrupt is negated when the target core, a trusted core, or core 2 writes 1 to clear the<br>field.<br>0b - No interrupt is asserted to CPn<br>1b - Interrupt to CPn is asserted|
|1|CP1-to-CPn Interrupt|
|CP1_INT|Generates a directed interrupt initiated by core 1 targeting core n, if the appropriate interrupt routing bit<br>is enabled. The interrupt is negated when the target core, a trusted core, or core 1 writes 1 to clear the<br>field.<br>0b - No interrupt is asserted to CPn<br>1b - Interrupt to CPn is asserted|
|0|CP0-to-CPn Interrupt|
|CP0_INT|Generates a directed interrupt initiated by core 0 targeting core n, if the appropriate interrupt routing bit<br>is enabled. The interrupt is negated when the target core, a trusted core, or core 0 writes 1 to clear the<br>field.<br>0b - No interrupt asserted to CPn<br>1b - Interrupt to CPn asserted|



#### 7.4.3.31 Interrupt Router CPn Interrupt Generation (IRCP0IGR0 - IRCP2IGR3) 

##### Offset 

For n = 0 to 2; m = 0 to 3: 

|Register|Offset|
|---|---|
|IRCPnIGRm|204h + (n × 20h) + (m × 8h)|



##### Function 

Provides a mechanism for cores to initiate an MSI to another core in the system. 

Privileged, 32-bit accesses from the: 

- Cortex-M7 cores are treated as RAZ/W. 

- Debugger are treated as RAZ/WI. 

- Non-core (and non-debugger) bus masters are treated as RAZ/WI. 

Access: Privileged mode only. Attempted accesses in User mode or the ones using a size other than 32 bits are not permitted and terminate with an error. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

104 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/007_Miscellaneous_System_Control_Module_-MSCM-/S32K3XXRM_数据表.pdf-0105-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>INT_<br>W<br>EN<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-1|Reserved|
|—||
|0|Interrupt Enable|
|INT_EN|Initiates a core-to-core interrupt targeting CPn, if CPm writes to this field. SeeMSI routing.|



#### 7.4.3.32 Interrupt Router Configuration (IRCPCFG) 

##### Offset 

|Register|Offset|
|---|---|
|IRCPCFG|400h|



##### Function 

Provides a mechanism to designate specific cores in the system as trusted. These trusted cores are allowed to access and manage outstanding MSIs. 

Privileged, 32-bit accesses from the: 

- Cortex-M7 cores are treated as R/W. 

- Debugger are treated as R/WI. 

- Non-core (and non-debugger) bus masters are treated as RAZ/WI. 

Attempted accesses in User mode or the ones using a size other than 32 bits are not permitted. They terminate with an error. 

Access: Privileged mode only 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

105 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|LOCK||||||||0||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||||0|||||||CP2_|CP1_|CP0_|
|W||||||||||||||TR|TR|TR|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|Lock|
|LOCK|Provides a locking mechanism that can be used to limit the ability to write to the register. After you write<br>1 to this field, it remains 1 until the next reset.<br>0b - Register can be written by any privileged write<br>1b - Register is locked (read-only) until the next reset|
|30-3<br>—<br>2<br>CP2_TR|Reserved<br>CP2 as Trusted Core<br>Indicates if CP2 is a trusted core with access to read the full contents of IRCPnISRm.<br>0b - Not trusted<br>1b - Trusted|
|1<br>CP1_TR|CP1 as Trusted Core<br>Indicates if CP1 is a trusted core with access to read the full contents of IRCPnISRm.<br>0b - Not trusted<br>1b - Trusted|
|0<br>CP0_TR|CP0 as Trusted Core<br>Indicates if CP0 is a trusted core with access to read the full contents of IRCPnISRm.<br>0b - Not trusted<br>1b - Trusted|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

106 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

#### 7.4.3.33 Memory Execution Control (XN_CTRL) 

##### Offset 

|Register|Offset|
|---|---|
|XN_CTRL|500h|



##### Function 

Controls whether an instruction fetch, also known as a code fetch or executable fetch, is allowed for SRAM and TCM. 

~~<mark>NOTE</mark>~~ 

This register does not inhibit HSE_B instruction accesses. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/007_Miscellaneous_System_Control_Module_-MSCM-/S32K3XXRM_数据表.pdf-0107-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 CM7_2 CM7_1 CM7_0 0 CM7_2 CM7_1 CM7_0<br>HLK  SLK<br>W _D... _D... _D... _D... _D... _D...<br>Reset 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 CM7_2 CM7_1 CM7_0 0 CM7_2 CM7_1 CM7_0 0 PRAM PRAM PRAM<br>W _I... _I... _I... _D... _D... _D... _2  _1  0<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Hard Lock|
|HLK|Enables and disables hard lock.<br>Locks the register to disable writes until the next hardware reset.<br>0b - Disabled|
||1b - Enabled|
|30|Soft Lock|
|SLK|Enables and disables soft lock.|
||Locks the register to disable writes until this field becomes 0.<br>0b - Disabled|
||1b - Enabled|
|29-23|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

107 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—<br>22<br>CM7_2_DTCM|Transaction Control For Cortex-M7_2 DTCM<br>Does not select Cortex-M7_2 as Slave. All transactions to Cortex-M7_2 DTCM are not generated<br>because Cortex-M7_2 DTCM is not selected (backdoor access).<br>0b - Transaction enabled<br>1b - Transaction disabled|
|21<br>CM7_1_DTCM|Transaction Control For Cortex-M7_1 DTCM<br>Does not select Cortex-M7_1 as Slave. All transactions to Cortex-M7_1 DTCM are not generated<br>because Cortex-M7_1 DTCM is not selected (backdoor access).<br>0b - Transaction enabled<br>1b - Transaction disabled|
|20<br>CM7_0_DTCM|Transaction Control For Cortex-M7_0 DTCM<br>Does not select Cortex-M7_0 as Slave. All transactions to Cortex-M7_0 DTCM are not generated<br>because Cortex-M7_0 DTCM is not selected (backdoor access).<br>0b - Transaction enabled<br>1b - Transaction disabled|
|19<br>—|Reserved|
|18<br>CM7_2_DIS_D0<br>_D1TCM_EXEC|Disable D0 and D1 TCM Execution For Cortex-M7_2<br>Disables D0 and D1 TCM execution for Cortex-M7_2. It is provided to the core. If execution is disabled, it<br>is taken as illegal access by the core.<br>0b - Execution enabled<br>1b - Execution disabled|
|17<br>CM7_1_DIS_D0<br>_D1TCM_EXEC|D0 and D1 TCM Execution For Cortex-M7_1<br>Disables D0 and D1 TCM execution for Cortex-M7_1. It is provided to the core. If execution is disabled, it<br>is taken as illegal access by the core.<br>0b - Execution enabled<br>1b - Execution disabled|
|16|D0 And D1 TCM Execution For Cortex-M7_0|
|CM7_0_DIS_D0<br>_D1TCM_EXEC|Disables D0 and D1 TCM execution for Cortex-M7_0. It is provided to the core. If execution is disabled, it<br>is taken as illegal access by the core.<br>0b - Execution enabled<br>1b - Execution disabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

108 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|15<br>—|Reserved|
|14<br>CM7_2_ITCM|Transaction Control For Cortex-M7_2 ITCM<br>Does not select Cortex-M7_2 ITCM as Slave. All transactions to Cortex-M7_2 ITCM are not generated<br>because Cortex-M7_2 ITCM is not selected (backdoor access).<br>0b - Execution enabled<br>1b - Execution disabled|
|13<br>CM7_1_ITCM|Transaction Control For Cortex-M7_1 ITCM<br>Does not select Cortex-M7_1 ITCM as Slave. All transactions to Cortex-M7_1 ITCM are not generated<br>because Cortex-M7_1 ITCM is not selected (backdoor access).<br>0b - Execution enabled<br>1b - Execution disabled|
|12<br>CM7_0_ITCM|Transaction Control For Cortex-M7_0 ITCM<br>Does not select Cortex-M7_0 ITCM as Slave. All transactions to Cortex-M7_0 ITCM are not generated<br>because Cortex-M7_0 ITCM is not selected (backdoor access).<br>0b - Execution enabled<br>1b - Execution disabled|
|11<br>—|Reserved|
|10|ITCM Execution for Cortex-M7_2|
|CM7_2_DIS_IT<br>CM_EXEC|Disables ITCM execution for Cortex-M7_2. It is provided to the core. If execution is disabled, it is<br>considered an illegal access by the core.<br>0b - Execution enabled<br>1b - Execution disabled|
|9<br>CM7_1_DIS_IT<br>CM_EXEC|ITCM Execution For Cortex-M7_1<br>Disables ITCM execution for Cortex-M7_1. It is provided to the core. If execution is disabled, it is<br>considered an illegal access by the core.<br>0b - Execution enabled<br>1b - Execution disabled|
|8|ITCM Execution For Cortex-M7_0|
|CM7_0_DIS_IT<br>CM_EXEC|Disables ITCM execution for Cortex-M7_0. It is provided to the core. If execution is disabled, it is<br>considered an illegal access by the core.<br>0b - Execution enabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

109 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - Execution disabled|
|7-3|Reserved|
|—||
|2|Transaction Control For PRAM 2|
|PRAM_2|Does not select PRAM2 as Slave. All transactions to PRAM2 are not generated because PRAM2 is not<br>selected.|
||0b - Transaction enabled<br>1b - Transaction disabled|
|1|Transaction Control For PRAM 1|
|PRAM_1|Does not select PRAM1 as Slave. All transactions to PRAM1 are not generated because PRAM1 is not<br>selected.|
||0b - Transaction enabled|
||1b - Transaction disabled|
|0|Transaction Control For PRAM 0|
|PRAM0|Does not select PRAM0 as Slave. All transactions to PRAM0 are not generated because PRAM0 is not<br>selected.|
||0b - Transaction enabled|
||1b - Transaction disabled|



#### 7.4.3.34 Enable Interconnect Error Detection (ENEDC) 

##### Offset 

|Register|Offset|
|---|---|
|ENEDC|600h|



##### Function 

Enables interconnect error detection. 

For more information, see the FCCU file attached to this document. 

Access: Privileged mode only 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

110 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/007_Miscellaneous_System_Control_Module_-MSCM-/S32K3XXRM_数据表.pdf-0111-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R Reserved<br>ADD_ CM7_1 ADD_ CM7_0 ADD_ AIPS2  ADD_ AIPS1  ADD_ AIPS0  ADD_ QSPI  ADD_ ed<br>CM7... _T... CM7... _T... AIP... AIP... AIP... QSPI  TCM...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv<br>R<br>ADD_ PRAM ADD_ PRAM ADD_ ADD_ ADD_ ed  CM7_1 CM7_1 ENET  HSE  STAM  EDMA  CM7_0 CM7_0<br>PRA... 1  PRA... 0  PF2  PF1  PF0  _A... _A... _A... _A...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29|Address Check For Cortex-M7_1_TCM|
|ADD_CM7_1_T<br>CM|Enables or disables address check for the Cortex-M7_1_TCM backdoor path.<br>0b - Disabled<br>1b - Enabled|
|28<br>CM7_1_TCM|Write Data Check For Cortex-M7_1_TCM<br>Enables or disables write data check for the Cortex-M7_1_TCM backdoor path.<br>0b - Disabled<br>1b - Enabled|
|27<br>ADD_CM7_0_T<br>CM|Address Check For Cortex-M7_0_TCM<br>Enables or disables address check for the Cortex-M7_0_TCM backdoor path.<br>0b - Disabled<br>1b - Enabled|
|26<br>CM7_0_TCM|Write Data Check For Cortex-M7_0_TCM<br>Enables or disables write data check for the Cortex-M7_0_TCM backdoor path.<br>0b - Disabled<br>1b - Enabled|
|25|Address Check For AIPS2|
|ADD_AIPS2|Enables or disables address check for the AIPS2 path.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

111 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Disabled<br>1b - Enabled|
|24<br>AIPS2|Write Data Check For AIPS2<br>Enables or disables write data check for the AIPS2 path.<br>0b - Disabled<br>1b - Enabled|
|23<br>ADD_AIPS1|Address Check For AIPS1<br>Enables or disables address check for the AIPS1 path.<br>0b - Disabled<br>1b - Enabled|
|22<br>AIPS1|Write Data Check For AIPS1<br>Enables or disables write data check for the AIPS1 path.<br>0b - Disabled<br>1b - Enabled|
|21<br>ADD_AIPS0|Address Check For AIPS0<br>Enables or disables address check for the AIPS0 path.<br>0b - Disabled<br>1b - Enabled|
|20<br>AIPS0|Write Data Check For AIPS0<br>Enables or disables write data check for the AIPS0 path.<br>0b - Disabled<br>1b - Enabled|
|19<br>ADD_QSPI|Address Check For QuadSPI<br>Enables or disables address check for the QuadSPI path.<br>0b - Disabled<br>1b - Enabled|
|18<br>QSPI|Write Data Check For QuadSPI<br>Enables or disables write data check for the QuadSPI path.<br>0b - Disabled<br>1b - Enabled|
|17|Write Data Check For TCM Backdoor<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

112 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|ADD_TCM_BA<br>CKDOOR|Enables or disables the address check for the TCM backdoor path.<br>0b - Disabled<br>1b - Enabled|
|16<br>—|Reserved|
|15<br>ADD_PRAM1|Address Check For PRAM1<br>Enables or disables address check for the PRAM1 path.<br>0b - Disabled<br>1b - Enabled|
|14<br>PRAM1|Write Data Check For PRAM1<br>Enables or disables write data check for the PRAM1 path.<br>0b - Disabled<br>1b - Enabled|
|13<br>ADD_PRAM0|Address Check For PRAM0<br>Enables or disables address check for the PRAM0 path.<br>0b - Disabled<br>1b - Enabled|
|12<br>PRAM0|Write Data Check For PRAM0<br>Enables or disables write data check for the PRAM0 path.<br>0b - Disabled<br>1b - Enabled|
|11<br>ADD_PF2|Enable Address Check For PF2<br>Enables or disables address check for the PF2 path.<br>0b - Disabled<br>1b - Enabled|
|10<br>ADD_PF1|Address Check For PF1<br>Enables or disables address check for the PF1 path.<br>0b - Disabled<br>1b - Enabled|
|9|Address Check For PF0|
|ADD_PF0|Enables or disables address check for the PF0 path.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

113 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Disabled<br>1b - Enabled|
|8<br>—|Reserved|
|7<br>CM7_1_AHBP|Read Data Check For Cortex-M7_1_AHBP<br>Enables or disables read data check for the Cortex-M7_1_AHBP path.<br>0b - Disabled<br>1b - Enabled|
|6<br>CM7_1_AHBM|Read Data Check For Cortex-M7_1_AHBM<br>Enables or disables read data check for the Cortex-M7_1_AHBM path.<br>0b - Disabled<br>1b - Enabled|
|5<br>ENET|Read Data Check For ENET<br>Enables or disables read data check for the ENET path.<br>0b - Disabled<br>1b - Enabled|
|4<br>HSE|Read Data Check For HSE_B<br>Enables or disables read data check for the HSE_B path.<br>0b - Disabled<br>1b - Enabled|
|3<br>STAM|Read Data Check For STAM<br>Enables or disables read data check for the STAM path.<br>0b - Disabled<br>1b - Enabled|
|2<br>EDMA|Read Data Check For eDMA<br>Enables or disables read data check for the eDMA path.<br>0b - Disabled<br>1b - Enabled|
|1|Read Data Check For Cortex-M7_0_AHBP|
|CM7_0_AHBP|Enables or disables read data check for the Cortex-M7_0_AHBP path.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

114 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Disabled|
||1b - Enabled|
|0|Read Data Check For Cortex-M7_0_AHBM|
|CM7_0_AHBM|Enables or disables read data check for the Cortex-M7_0_AHBM path.|
||0b - Disabled|
||1b - Enabled|



#### 7.4.3.35 Enable Interconnect Error Detection (ENEDC1) 

##### Offset 

|Register|Offset|
|---|---|
|ENEDC1|604h|



##### Function 

Enables interconnect error detection. 

For more information, see the FCCU file attached to this document. 

Access: Privileged mode only 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/007_Miscellaneous_System_Control_Module_-MSCM-/S32K3XXRM_数据表.pdf-0115-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R USDH<br>Reserved<br>W C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R ADD_ CM7_2 ADD_ EN_P EDMA EDMA PFLAS CM7_2 CM7_2<br>Reserved  Reserved  Reserved<br>W CM7... _T... EN_... RAM2  _S1  _S0  H_3  _A... _A...<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function||
|---|---|---|
|31-17<br>—|Reserved|Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

115 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|16<br>USDHC|Enable Read Data Check uSDHC<br>Enables or disables the read data check for the uSDHC path.<br>0b - Disabled<br>1b - Enabled|
|15<br>ADD_CM7_2_T<br>CM|Enable Address Check Cortex-M7_2_TCM<br>Enables or disables the address data check for the Cortex-M7_2_TCM backdoor path.<br>0b - Disabled<br>1b - Enabled|
|14<br>CM7_2_TCM|Enable Write Data Check Cortex-M7_2_TCM<br>Enables or disables write data check for the Cortex-M7_2_TCM backdoor path.<br>0b - Disabled<br>1b - Enabled|
|13-12<br>—|Reserved|
|11<br>ADD_EN_PRA<br>M2|Enable Address Check PRAM 2<br>Enables or disables the address check for the PRAM 2 path.<br>0b - Disabled<br>1b - Enabled|
|10<br>EN_PRAM2|Enable Write Data Check PRAM 2<br>Enables or disables the write data check for PRAM2.<br>0b - Disabled<br>1b - Enabled|
|9-7<br>—|Reserved|
|6<br>EDMA_S1|Enable Address Check eDMA S1<br>Enables or disables the address check for the eDMA S1 path.<br>0b - Disabled<br>1b - Enabled|
|5|Enable Address Check eDMA S0|
|EDMA_S0|Enables or disables address check for the eDMA S0 path.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

116 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Disabled<br>1b - Enabled|
|4<br>PFLASH_3|Enable Address Check PFlash3<br>Enables or disables address check for the PFlash3 path.<br>0b - Disabled<br>1b - Enabled|
|3<br>CM7_2_AHBP|Enable Read Data Check Cortex-M7_2_AHBP<br>Enables or disables read data check for the Cortex-M7_2_AHBP path.<br>0b - Disabled<br>1b - Enabled|
|2<br>CM7_2_AHBM|Enable Read Data Check Cortex-M7_2_AHBM<br>Enables or disables read data check for the Cortex-M7_2_AHBM path.<br>0b - Disabled<br>1b - Enabled|
|1-0<br>—|Reserved|



#### 7.4.3.36 AHB Gasket Configuration (IAHBCFGREG) 

##### Offset 

|Register|Offset|
|---|---|
|IAHBCFGREG|700h|



##### Function 

Controls the functional configuration of the AHB gaskets located on the platform. 

Access: Privileged mode only 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

117 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||Reserved||||||||PRAM<br>2_D...|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|TCM_<br>PRA...|PRAM<br>1_D...|PRAM<br>0_D...|USDH<br>C_D...|AIPS0<br>_D...|AIPS2<br>_D...|AIPS1<br>_D...|CM7_2<br>_A...|CM7_1<br>_A...|CM7_0<br>_A...|QSPI_<br>DI...|TCM_<br>DIS...|HSE_<br>DIS...|DMA_<br>AXB...|DMA_<br>AXB...|EMAC<br>_DI...|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-17<br>—|Reserved|
|16|Determines whether write burst optimizations in the PRAM2 gasket are enabled or disabled.|
|PRAM2_DIS_W<br>R_OPT|Enabling optimization allows performance improvements during burst writes. Disabling optimization is<br>required only if you expect an early write burst termination from a master.<br>0b - Enabled<br>1b - Disabled|
|15|Determines whether write burst optimizations in the TCM_PRAM gasket are enabled or disabled.|
|TCM_PRAM_DI<br>S_WR_OPT|Enabling optimization allows performance improvements during burst writes. Disabling optimization is<br>required only if you expect an early write burst termination from a master.<br>0b - Enabled<br>1b - Disabled|
|14<br>PRAM1_DIS_W<br>R_OPT|Determines whether write burst optimizations in the PRAM1 gasket are enabled or disabled.<br>Enabling optimization allows performance improvements during burst writes. Disabling optimization is<br>required only if you expect an early write burst termination from a master.<br>0b - Enabled<br>1b - Disabled|
|13<br>PRAM0_DIS_W<br>R_OPT|Determines whether write burst optimizations in the PRAM0 gasket are enabled or disabled.<br>Enabling optimization allows performance improvements during burst writes. Disabling optimization is<br>required only if you expect an early write burst termination from a master.<br>0b - Enabled<br>1b - Disabled|
|12|Determines whether write burst optimizations in the uSDHC gasket are enabled.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

118 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

Table continued from the previous page... 

|Field<br>USDHC_DIS_W<br>R_OPT|Function<br>Enabling optimization allows performance improvements during burst writes. Disabling optimization is<br>required only if you expect an early write burst termination from a master.<br>0b - Enabled<br>1b - Disabled|
|---|---|
|11|Determines whether write burst optimizations in the AIPS2 AHB gasket are enabled.|
|AIPS0_DIS_WR<br>_OPT|Enabling optimization allows performance improvements during burst writes. Disabling optimization is<br>required only if you expect an early write burst termination from a master.<br>0b - Enabled<br>1b - Disabled|
|10<br>AIPS2_DIS_WR<br>_OPT|Determines whether write burst optimizations in the AIPS2 AHB gasket are enabled.<br>Enabling optimization allows performance improvements during burst writes. Disabling optimization is<br>required only if you expect an early write burst termination from a master.<br>0b - Enabled<br>1b - Disabled|
|9|Determines whether write burst optimizations in the AIPS1 AHB gasket are enabled.|
|AIPS1_DIS_WR<br>_OPT|Enabling optimization allows performance improvements during burst writes. Disabling optimization is<br>required only if you expect an early write burst termination from a master.<br>0b - Enabled<br>1b - Disabled|
|8|Determines whether write burst optimizations in the CM7_2_AHBS gasket are enabled or disabled.|
|CM7_2_AHBS_<br>DIS_WR_OPT|Enabling optimization allows performance improvements during burst writes. Disabling optimization is<br>required only if you expect an early write burst termination from a master.<br>0b - Enabled<br>1b - Disabled|
|7|Determines whether write burst optimizations in the CM7_1_AHBS gasket are enabled or disabled.|
|CM7_1_AHBS_<br>DIS_WR_OPT|Enabling optimization allows performance improvements during burst writes. Disabling optimization is<br>required only if you expect an early write burst termination from a master.<br>0b - Enabled<br>1b - Disabled|
|6|Determines whether write burst optimizations in the CM7_0_AHBS gasket are enabled or disabled.|
|CM7_0_AHBS_<br>DIS_WR_OPT|Enabling optimization allows performance improvements during burst writes. Disabling optimization is<br>required only if you expect an early write burst termination from a master.<br>0b - Enabled<br>1b - Disabled|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

119 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|5<br>QSPI_DIS_WR_<br>OPT|Determines whether write burst optimizations in the QuadSPI AHB gasket are enabled.<br>Enabling optimization allows performance improvements during burst writes. Disabling optimization is<br>required only if you expect an early write burst termination from a master.<br>0b - Enabled<br>1b - Disabled|
|4<br>TCM_DIS_WR_<br>OPT|Determines whether write burst optimizations in the TCM AHB gasket are enabled.<br>Enabling optimization allows performance improvements during burst writes. Disabling optimization is<br>required only if you expect an early write burst termination from a master.<br>0b - Enabled<br>1b - Disabled|
|3<br>HSE_DIS_WR_<br>OPT|Determines whether write burst optimizations in the HSE_B AHB gasket are enabled.<br>Enabling optimization allows performance improvements during burst writes. Disabling optimization is<br>required only if you expect an early write burst termination from a master.<br>0b - Enabled<br>1b - Disabled|
|2|Determines whether write burst optimizations in the DMA AXBS S1 AHB gasket are enabled.|
|DMA_AXBS_S1<br>_DIS_WR_OPT|Enabling optimization allows performance improvements during burst writes. Disabling optimization is<br>required only if you expect an early write burst termination from a master.<br>0b - Enabled<br>1b - Disabled|
|1|Determines whether write burst optimizations in the DMA AXBS S0 AHB gasket are enabled.|
|DMA_AXBS_S0<br>_DIS_WR_OPT|Enabling optimization allows performance improvements during burst writes. Disabling optimization is<br>required only if you expect an early write burst termination from a master.<br>0b - Enabled<br>1b - Disabled|
|0|Determines whether write burst optimizations in the EMAC AHB gasket are enabled.|
|EMAC_DIS_WR<br>_OPT|Enabling optimization allows performance improvements during burst writes. Disabling optimization is<br>required only if you expect an early write burst termination from a master.<br>0b - Enabled<br>1b - Disabled|



7.4.3.37 Interrupt Router Shared Peripheral Routing Control (IRSPRC0 - IRSPRC239) 

Offset 

For n = 0 to 239: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

120 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

|Register<br>IRSPRCn|Offset<br>880h + (n × 2h)|
|---|---|



##### Function 

Provides an array of 16-bit registers, where each register defines the routing control for the corresponding interrupt request. Starting from IRQ = 0 (first on-platform interrupt vector). See the interrupt map file attached to this document for details. 

For this chip, each interrupt request can be either routed to a subset or to all the cores using the bit-mapped fields in IRSPRCn. If all the CPxEn fields are cleared, the interrupt request is disabled. Each routing control halfword can be locked by writing 1 to the LOCK field. 

Privileged accesses from non-core (and non-debug) bus masters are treated as RAZ/WI, and any attempted User mode reference terminates with an error. Attempted accesses using a size other than a 16-bit halfword also terminate with an error. 

If you write 1 to all the CPxEn bits, all the cores service the interrupt. It is up to software to ensure that no conflicts arise from this setup either via the interrupt handler or through programming core level interrupt routing (the NVIC/GIC). 

Reads and writes to this register beyond IRSPRC207 lead to unpredictable results. 

Access: Privileged mode only 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/007_Miscellaneous_System_Control_Module_-MSCM-/S32K3XXRM_数据表.pdf-0121-11.png)


<!-- Start of picture text -->
Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>LOCK  M7_2  M7_1  M7_0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|15|Lock|
|LOCK|Provides a mechanism to lock the routing of the corresponding interrupt request. After you write 1 to this<br>field, attempted writes to IRSPRCn are ignored until the next reset writes 0 to the field.<br>0b - Writes to IRSPRCn allowed<br>1b - Writes to IRSPRCn ignored|
|14-3<br>—|Reserved|
|2|Enable Cortex-M7_1 Interrupt Steering|
|M7_2|Enables or disables the corresponding interrupt request to route to Cortex-M7_2.<br>0b - Routing disabled<br>1b - Routing enabled|
|1|Enable Cortex-M7_1 Interrupt Steering|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

121 / 4640 

NXP Semiconductors 

Miscellaneous System Control Module (MSCM) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|M7_1|Enables or disables the corresponding interrupt request to route to Cortex-M7_1.<br>0b - Routing disabled|
||1b - Routing enabled|
|0|Enable Cortex-M7_0 Interrupt Steering|
|M7_0|Enables or disables the corresponding interrupt request to route to Cortex-M7_0.|
||0b - Routing disabled|
||1b - Routing enabled|



|7.5 Glossary||
|---|---|
|GIC|Generic interrupt controller|
|IRQs|Interrupt requests|
|ISR|Interrupt service routine|
|MSI|Message signal interface|
|NVIC|Nested vector interrupt controller|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

122 / 4640 

