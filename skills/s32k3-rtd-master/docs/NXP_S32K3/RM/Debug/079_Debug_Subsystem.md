NXP Semiconductors 

# Chapter 79 Debug Subsystem 

## 79.1 Introduction 

This chapter discusses the debug and trace architecture of the chip that is based on the specifications provided in the Arm<sup>®</sup> CoreSight<sup>™</sup> SoC-400 Technical Reference Manual. See References for a link to this document and to other related documentation available on the Arm website. 

The chip architecture includes debug and trace modules. See Features for details on the debug and trace features that Cortex-M7 core clusters support. 

The debug components that the Cortex-M7 core supports are accessible via the Arm DAP controller-based architecture. The DAP controller works in parallel with the system JTAGC. Both these controllers share the JTAG port and JTAG instruction set. 

The system components are similar for different chips in the same family and include the primary core debug interfaces, the chip-level debug interfaces, and chip-level trace interfaces. The accelerator components include debug and trace circuits. These circuits are necessary for any application-specific accelerators required for the different application spaces that a chip supports. They vary from one chip to another and could include only trace components. 

## 79.2 Interfaces supported in S32K3 family 

Table 691. Interfaces supported in S32K3 family 

|S32K344|S32K324|S32K322|S32K342|S32K312 /<br>S32K311 /<br>S32K310|S32K314|S32K338|S32K358|S32K348|S32K328|
|---|---|---|---|---|---|---|---|---|---|
|Cortex-<br>M7_0<br>(CTI,<br>DWT,<br>BPU,<br>ETM, ITM)|Cortex-<br>M7_0<br>(CTI,<br>DWT,<br>BPU,<br>ETM, ITM)|Cortex-<br>M7_0<br>(CTI,<br>DWT,<br>BPU, ITM)|Cortex-<br>M7_0<br>(CTI,<br>DWT,<br>BPU, ITM)|Cortex-<br>M7_0<br>(CTI,<br>DWT,<br>BPU, ITM)|Cortex-<br>M7_0<br>(CTI,<br>DWT,<br>BPU,<br>ETM, ITM)|Cortex-<br>M7_0<br>(CTI,<br>DWT,<br>BPU,<br>ETM, ITM)|Cortex-<br>M7_0<br>(CTI,<br>DWT,<br>BPU,<br>ETM, ITM)|Cortex-<br>M7_0<br>(CTI,<br>DWT,<br>BPU,<br>ETM, ITM)|Cortex-<br>M7_0<br>(CTI,<br>DWT,<br>BPU,<br>ETM, ITM)|
|-|Cortex-<br>M7_1<br>(CTI,<br>DWT,<br>BPU,<br>ETM, ITM)|Cortex-<br>M7_1<br>(CTI,<br>DWT,<br>BPU, ITM)|-|-|-|Cortex-<br>M7_1<br>(CTI,<br>DWT,<br>BPU,<br>ETM, ITM)|-|-|-|
|-|-|-|-|-|-|Cortex-<br>M7_2<br>(CTI,<br>DWT,<br>BPU,<br>ETM, ITM)|Cortex-<br>M7_2<br>(CTI,<br>DWT,<br>BPU,<br>ETM, ITM)|Cortex-<br>M7_2<br>(CTI,<br>DWT,<br>BPU,<br>ETM, ITM)|Cortex-<br>M7_2<br>(CTI,<br>DWT,<br>BPU,<br>ETM, ITM)|
|Cortex-<br>M0+|Cortex-<br>M0+|Cortex-<br>M0+|Cortex-<br>M0+|Cortex-<br>M0+|Cortex-<br>M0+|Cortex-<br>M0+|Cortex-<br>M0+|Cortex-<br>M0+|Cortex-<br>M0+|
|HTM<br>(CTI+DMA|HTM<br>(CTI+DMA|-|-|-|HTM<br>(CTI+DMA|HTM<br>(CTI+DMA|HTM<br>(CTI+DMA|HTM<br>(CTI+DMA|HTM<br>(CTI+DMA|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4548 / 4640 

NXP Semiconductors 

Debug Subsystem 

Table 691. Interfaces supported in S32K3 family (continued) 

|S32K344|S32K324|S32K322|S32K342|S32K312 /<br>S32K311 /<br>S32K310|S32K314|S32K338|S32K358|S32K348|S32K328|
|---|---|---|---|---|---|---|---|---|---|
|/EMAC<br>TRACE)|/EMAC<br>TRACE)||||/EMAC<br>TRACE)|/EMAC<br>TRACE)|/EMAC<br>TRACE)|/EMAC<br>TRACE)|/EMAC<br>TRACE)|
|SWO|SWO|SWO|SWO|SWO|SWO|SWO|SWO|SWO|SWO|
|TPIU|TPIU|-|-|-|TPIU|TPIU|TPIU|TPIU|TPIU|
|ETF (4)|ETF (4)|-|-|-|ETF (4)|ETF (4)|ETF (4)|ETF (4)|ETF (4)|
|FUNNELs<br>(3)|FUNNELs<br>(3)|-|-|-|FUNNELs<br>(3)|FUNNELs<br>(3)|FUNNELs<br>(3)|FUNNELs<br>(3)|FUNNELs<br>(3)|
|CTI (3)|CTI (4)|CTI (3)|CTI (2)|CTI (2)|CTI (3)|CTI (5)|CTI (4)|CTI (3)|CTI (4)|
|CTM (1)|CTM (1)|CTM (1)|CTM (1)|CTM (1)|CTM (1)|CTM (2)|CTM (2)|CTM (2)|CTM (2)|
|Timestam<br>p|Timestam<br>p|Timestam<br>p|Timestam<br>p|Timestam<br>p|Timestam<br>p|Timestam<br>p|Timestam<br>p|Timestam<br>p|Timestam<br>p|
|MDM_AP|MDM_AP|MDM_AP|MDM_AP|MDM_AP|MDM_AP|MDM_AP|MDM_AP|MDM_AP|MDM_AP|
|SDA_AP|SDA_AP|SDA_AP|SDA_AP|SDA_AP|SDA_AP|SDA_AP|SDA_AP|SDA_AP|SDA_AP|



## 79.3 Block diagram 

This figure illustrates the DAP architecture of the S32K3xx family. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4549 / 4640 

NXP Semiconductors 

Debug Subsystem 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Debug/079_Debug_Subsystem/S32K3XXRM_数据表.pdf-4550-02.png)


<!-- Start of picture text -->
DAP/TAP JTAG pins<br>SWJ-DP<br>DAPMUX<br>AHB_AP AHB_AP AHB_AP<br>JTAGC APB-AP MDM_AP<br>AHB_AP<br>Cortex-M0+<br>Boundary<br>scan Time<br>HTM64<br>stamp SDA_AP<br>Security Available only on the<br>SystemJDC  S32K3x4 Cortex-M7_0 Cortex-M7_2<br>JDC<br>Only available<br>ETF_x Cortex-M7_1 on the S32K358<br>CSTF_x<br>System interconnect (AHB)<br>Available only on the<br>TPIU<br> S32K3x4<br>IPS2APB<br>CTl_x<br>SWO<br>HSE_B System debug APB interconnect (APBIC)<br><!-- End of picture text -->


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Debug/079_Debug_Subsystem/S32K3XXRM_数据表.pdf-4550-03.png)


<!-- Start of picture text -->
Figure 504. DAP architecture<br><!-- End of picture text -->

~~<mark>NOTE</mark>~~ 

Debug components other than the Cortex-M0+ core are accessible through software path (CORE > AXBS > AIPS > DAPMUX > APs), that is, by directly specifying the memory mapped addresses without doing challenge response. 

## 79.4 Features 

This chip includes these features that support the functions listed under each feature type: 

- Debug control 

   - Is implemented via IEEE 1149.1-compliant JTAG 

- Test control 

   - Is implemented via IEEE 1149.1-compliant JTAG 

   - Uses IEEE 1149.6 extension to IEEE 1149.1 

- Trace interface 

   - Includes four high-speed data pads and one clock pad @120 MHz (120 MB/s throughput per pad) 

   - Includes 16 low-speed data pads and one clock pad @25 MHz (100 MB/s throughput per pad) 

- Debug security 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4550 / 4640 

NXP Semiconductors 

Debug Subsystem 

   - Includes a DAP/TAP interface that controls all debug features and is gated by Cortex M0+ JDC module 

   - Includes security modes as described in the "Security" chapter 

- Debugging and run control 

Is implemeted through stopping points, starting points, breakpoints, and watchpoints 

   - Each Cortex-M7 core supports eight instruction comparators and a watchpoint unit having four watchpoints 

- Trace source 

   - Includes Cortex-M7: 

      - ◦ETM that provides instruction and data trace 

      - ◦ITM that provides DWT, time-stamping, and diagnostic information 

- Cross-triggering support 

   - Controls run-control options of cores based on other cores 

   - Provides a matrix having connections to: 

      - ◦HTM via system CTI 

◦All Cortex-M7 CPUs 

- Ability to view and modify all memory-mapped areas that are not otherwise blocked—includes a system bus debug access port 

- Performance monitoring of cores—implements a performance monitoring unit (PMU) on each Cortex core 

- Safety 

   - Supports monitoring of debug signals to avoid common mode faults 

   - Allows checking of erroneous activation of debugging, especially if intrusive (for example, a CPU entering Debug state) 

- Timestamps 

   - Generates a timestamp bus for distribution to the trace sources 

   - Includes a 48-bit binary timestamp bus 

   - Clocks timestamp generator by a frequency of 160 MHz 

## 79.5 Debug 

### 79.5.1 TAP connectivity 

This figure shows a detailed view of TAP connectivity. JTAG select, SWJ-DP, and JTAG-DP are parts of DAP. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4551 / 4640 

NXP Semiconductors 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Debug/079_Debug_Subsystem/S32K3XXRM_数据表.pdf-4552-01.png)


<!-- Start of picture text -->
Debug Subsystem<br>JTAGC Arm JTAG-DP<br>JTAG-mode instruction loaded<br>SWD-JTAG TCK<br>switcher TMS TDO<br>TDI<br>0<br>TCK TDO<br>JTAG-DP 1<br>TMS TCK<br>TMS TDO<br>TDI TDI<br>SWJ-DP<br>DBGCLK<br>DBGDI<br>DBGDOEN<br>DBGDO<br>Figure 505. TAP connectivity<br><!-- End of picture text -->

The debug port comes out of reset in a standard JTAG mode. It switches to another mode by using the change sequences. After the mode changes, unused debug pins can be reassigned to any of their alternative muxed functions. 

JTAG-DP and JTAGC are connected in an overlay scheme and both have an Instruction Register (IR) length of 8 bits. 

### 79.5.2 DAP TAP 

DAP is an Arm component that provides multiple-master driving ports. A single external interface port accesses and controls these ports to provide system-wide debug. 

The DAP Instruction Register (DAP IR) overlays with the system JTAG Instruction Register (JTAGC IR). Table 692 presents DAP instructions. In addition to the four codes listed in the table, DAP uses BYPASS, which is identical to JTAGC BYPASS and is therefore not shown in the table. 

Table 692. DAP IR codes 

|Code|DAP IR|
|---|---|
|1111_1000b|ABORT|
|1111_1010b|DPACC|
|1111_1011b|APACC|
|1111_1110b|IDCODE|



DAP offers an AHB master interface to access system buses. It also exports the internal DAP bus to extend the access ports. For more information on DAP TAP, see the Arm Debug Interface Architecture Specification document available in References. 

In this chip: 

- The AHB slave ports of all Cortex-Mx cores provide debugger access to all memory units and registers in the system. 

- The new pass-through approach allows the debugger to see a cache coherent view of the memory map for that core. 

- The debugger must access the corresponding AHB_AP port to access the AHB-S port of that subsystem. 

- XRDC controls system access. 

- A core can access the debug components of another core through a DAPMUX to the bus interconnect. 

- The exported DAP bus hosts AHB_AP and MDM_AP. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4552 / 4640 

NXP Semiconductors 

Debug Subsystem 

- MDM_AP hosts system-level JTAG status and control registers. These registers can be used for cross triggering, synchronized debug, and other miscellaneous control and status functions. 

- APB_AP uses an APSEL value of 1h to access any APB-mapped debug modules. 

Table 696 describes the access addresses of APB-mapped debug modules. The value of the DAP select signal in the APSEL field of SWJ-DP's Select register selects the access ports in the DAP. Table 693 shows APSEL decoding. 

Table 693. DAP master address mapping 

|DAP master #|DAP<br>component|DAPBUS base<br>address<br>(access from|System memor<br>(access fr|y map address<br>om cores)|Selected port or<br>master|Applicability|
|---|---|---|---|---|---|---|
|||debugger)<sup>1</sup>|Page number|Base address|||
|0h|Reserved|0000_0000h|0|4025_0000h|Reserved|-|
|1h|APB_AP to all<br>APB-mapped<br>debug modules<br>(for example,<br>ETFs, HTM,<br>and trace<br>funnels)|0100_0000h|0|4025_0100h|APB_AP to all<br>APB-mapped<br>debug modules<br>(for example,<br>ETFs, HTM,<br>CSTF, and so<br>on)|S32K3x4 (for<br>ETF, HTM, and<br>CSTF see<br>Table 691)|
|2h|Reserved|0200_0000h|0|4025_0200h|Reserved|-|
|3h|AHB_AP to<br>Cortex-M7_2<br>debug modules<br>and chip system<br>memory map|0300_0000h|0|4025_0300h|AHB_AP to<br>Cortex-M7_2<br>debug modules<br>and chip system<br>memory map|<br>S32K358,<br>S32K338|
|4h|AHB_AP to<br>Cortex-M7_0<br>debug modules<br>and chip system<br>memory map|0400_0000h|0|4025_0400h|AHB_AP to<br>Cortex-M7_0<br>debug modules<br>and chip system<br>memory map|<br>All|
|5h|AHB_AP to<br>Cortex-M7_1<br>debug modules<br>and chip system<br>memory map|0500_0000h|0|4025_0500h|AHB_AP to<br>Cortex-M7_1<br>debug modules<br>and chip system<br>memory map|<br>S32K344,<br>S32K324,<br>S32K3x2,<br>S32K358|
|6h|MDM_AP|0600_0000h|0|4025_0600h|MDM_AP|All|
|7h|SDA_AP|0700_0000h|0|4025_4700h|SDA_AP used<br>for challenge-<br>response (CR)<br>in SWJ-DP<br>mode|All|
|8h—FFh|Reserved<br>(default AP<br>response)|—|—|—|—|-|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4553 / 4640 

NXP Semiconductors 

Debug Subsystem 

1. For example, 4000_XXYYh address is provided when accessing access ports (APs) via the debugger. Here, XX shows the AP select number and YY shows the address to be accessed. If you access SDA_AP via the debugger on 80h, you must provide the address 4000_0780h. 

~~<mark>NOTE</mark>~~ 

Accessing SDA_AP simultaneously from the core and the debugger is prohibited. If you try to do so, you may receive unpredictable responses to core-initiated transactions (for example, incorrect data read, a failed attempt to write to the register, or a transfer error). Debugger-initiated transactions proceed correctly. 

### 79.5.3 System JTAGC 

JTAGC connects in parallel with the TAP controller (JTAG-DP of DAP), which has an IR length of 8 bits. The JTAGC IR codes overlay the ones of the DAP controller. DAP uses four instructions and JTAGC uses the remaining ones. The TAP outputs (TPOs) are multiplexed based on the selected IR code. This chip is fully JTAG-compliant and appears as a single TAP to the JTAG chain. 

This table shows the JTAGC IR codes. The instructions that are used by Arm DAP TAP are shown in Table 692. 

Table 694. JTAG instructions for JTAGC 

|Code|JTAGC IR|
|---|---|
|0000_0000b|IDCODE|
|0000_0001b|Reserved|
|0000_0010b|SAMPLE/PRELOAD|
|0000_0011b|SAMPLE|
|0000_0100b|EXTEST|
|0000_0101b|HI-Z|
|0000_0110b|Reserved|
|0000_0111b|Reserved|
|0000_1000b—0000_1001b|Reserved|
|0000_1010b—0000_1011b|Reserved|
|0000_1100b|CLAMP|
|0000_1101b|ENABLE_SOC_DATA1|
|0000_1110b|Reserved|
|0000_1111b|Reserved|
|1000_0000b|Reserved|
|1000_0001b|Reserved|
|1000_0010b|Reserved|
|1000_0011b|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4554 / 4640 

NXP Semiconductors 

Debug Subsystem 

Table 694. JTAG instructions for JTAGC (continued) 

|Code|JTAGC IR|
|---|---|
|1000_0100b|Reserved|
|1000_0101b|Reserved|
|1000_0110b—1000_0111b|Reserved|
|1000_1000b|Reserved|
|1000_1001b|Reserved|
|1000_1010b—1000_1111b|Reserved|
|1001_0000b|Security JDC|
|1001_0001b|System JDC|
|1001_0010b—1001_0111b|Reserved for other system auxiliary clients|
|1001_1000b—1001_1011b|Reserved|
|1001_1100b—1011_1111b|Reserved for other system auxiliary clients|
|1100_0000b|Reserved|
|1100_0001b|Reserved|
|1100_0010b—1110_1111b|Reserved|
|1111_1000b|ABORT (Arm)|
|1111_1001b|Reserved|
|1111_1010b|DPACC (Arm)|
|1111_1011b|APACC (Arm)|
|1111_1100b|Reserved|
|1111_1101b|Reserved|
|1111_1110b|IDCODE (Arm)|
|1111_1111b|BYPASS|



#### 79.5.3.1 Chip JTAG/Target ID 

Each chip in the S32K3xx family includes a unique JTAG ID, which must be changed when instantiated with a different die in an SiP. The next table shows the JTAGC ID for this chip. 

Table 695. JTAG/Target ID 

|Chip|PRN|DC|PIN|MIC|IDCODE ID|JTAG ID|Target ID|
|---|---|---|---|---|---|---|---|
|S32K344|0|26h (38d)|160h (352d)<br>Table cont|Eh (14d)<br>inues on the nex|1<br>t page...|0996_001Dh|0995_C01Dh|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4555 / 4640 

NXP Semiconductors 

Debug Subsystem 

Table 695. JTAG/Target ID (continued) 

|Chip|PRN|DC|PIN|MIC|IDCODE ID|JTAG ID|Target ID|
|---|---|---|---|---|---|---|---|
|S32K324|0|26h (38d)|160h (352d)|Eh (14d)|1|0996_001Dh|0996_001Dh|
|S32K314|0|26h (38d)|160h (352d)|Eh (14d)|1|0996_001Dh|0996_001Dh|
|S32K311|0|26h (38d)|16Ch (364d)|Eh (14d)|1|0996_C01Dh|0996_C01Dh|
|S32K312|0|26h (38d)|168h (360d)|Eh (14d)|1|0996_801Dh|0996_801Dh|
|S32K342 /<br>S32K341 /<br>S32K322|0|26h (38d)|164h (356d)|Eh (14d)|1|0996_401Dh|0996_401Dh|
|S32K358 /<br>S32K348 /<br>S32K338 /<br>S32K328|0|26h (38d)|15Eh (350d)|Eh (14d)|1|0995_E01Dh|0995_E01Dh|



#### 79.5.3.2 JDC 

JDC allows you to access two 32-bit data registers by using the JTAG interface and by software running on one of the CPUs in the chip. These registers exchange data between an internal CPU and an external debug tool. 

### 79.5.4 Peripheral IPG debug implementation 

S32K344 is a multi-core chip. Any core can control a peripheral instance individually. You define the core's control over a peripheral during application development. 

For peripheral halt, all individual cores have the same capability and are gated by a dedicated MDM_AP core halt register field. For more information, see the configurations defined in MDM_AP register descriptions. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Debug/079_Debug_Subsystem/S32K3XXRM_数据表.pdf-4556-09.png)


<!-- Start of picture text -->
Cortex-M7_0  Cortex-M7_0  is halted<br>Cortex-M7_1  is halted<br>Cortex-M7_1<br>Peripheral 0<br>Not available on the S32K311, S32K312, and S32K314<br>GPR_CORE1_DBGFRZ0[P0]<br>Cortex-M7_2 Cortex-M7_2  is halted GPR_CORE0_DBGFRZ0[P0]<br>Only available on S32K358 GPR_CORE2_DBGFRZ0[P0]<br><!-- End of picture text -->

Figure 506. Peripheral IPG debug implementation 

### 79.5.5 Application debugging 

This section covers the following two cases: 

- Case 1: Debugger connected—application debugging from the first instruction 

- Case 2: Debugger not connected 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4556 / 4640 

NXP Semiconductors 

Debug Subsystem 

#### 79.5.5.1 Application debugging from first instruction 

This chip supports debugging from the first instruction on system power-up, destructive reset, functional reset, and standby exit. However, by default, debugging from the first instruction is disabled. 

The next figure shows the timing diagram of application debug implementation from first instruction on system power-up or destructive reset. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Debug/079_Debug_Subsystem/S32K3XXRM_数据表.pdf-4557-05.png)


<!-- Start of picture text -->
Debugger keeps the chip in reset by pressing reset pin<br>Debugger configures to hold app core’s reset<br>Debugger releases the chip’s reset pin; app core still in reset<br>BAF writes expected response; status in SDA_AP<br>BAF enables app coreCCTL<br>Debugger provides the expected response and CR passes status to SDA_AP<br>Debugger configures the core’s debug and releases the core’s resets<br>SDA_AP [Reset_Release]<br>Reset_b pad<br>Valid challenge<br>CCTL<br>app dbg en<br>Debugger decision must be configured before Before app dbg en becomes 1, the debugger has<br>reset deassertion because the debugger doesn’t no access to the chip except for some SDA_AP<br>know when BAF enables CCTL. response, status, and reset-release registers.<br><!-- End of picture text -->

Figure 507. Application debug implementation from first instruction 

These are the steps involved in enabling application debug from the first instruction on system power-up or destructive reset: 

1. After the reset is applied, the debugger provides an option to debug from the first instruction. To do this: 

   - a. Write 1 to SDAAPRSTCTRL[RSTRELTLCM70] and SDAAPRSTCTRL[RSTRELTLCM71]. 

   - b. Set the reset value of Reset Control (SDAAPRSTCTRL). 

2. Cortex M0+ starts after the reset pin is released. 

3. Debugger challenge-response (CR) starts. 

4. Cortex-M7_0 and Cortex-M7_1 remain in reset until MC_ME's PRTN0_CORE0_PCONF[CCE] field becomes 1 for Cortex-M7_0 and PRTN0_CORE1_PCONF[CCE] field becomes 1 for Cortex-M7_1. 

5. When BAF or FW writes 1 to MC_ME's PRTN0_CORE0_PCONF[CCE] field for Cortex-M7_0 and to PRTN0_CORE1_PCONF[CCE] field for Cortex-M7_1, and the debugger CR has passed: 

   - If the value of SDAAPRSTCTRL[RSTRELTLCM71] and SDAAPRSTCTRL[RSTRELTLCM70] is 0 for their respective cores, the debugger configures the core debug registers and then enables these fields that start the code execution. 

   - If the value of SDAAPRSTCTRL[RSTRELTLCM71] and SDAAPRSTCTRL[RSTRELTLCM70] is 1 for their respective cores, the debugger configures the core debug registers and then enables these fields that start the code execution. 

To debug from the first instruction during the low-power debug protocol, the debugger: 

1. Writes 0 to SDAAPRSTCTRL[RSTRELTLCM71] and SDAAPRSTCTRL[RSTRELTLCM70] for their respective cores. 

2. Writes 1 to MDMAPWIRREL[WTRSTRGM]. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4557 / 4640 

NXP Semiconductors 

Debug Subsystem 

#### 79.5.5.2 Debugger not connected 

If the debugger is not connected, the value of the DBGPWRUP_ACK signal is 0 as there is no DBGPWRUP_REQ. This results in the following scenario: 

1. The booting core writes 1 to MC_ME's PRTN0_CORE0_PCONF[CCE] field for Cortex-M7_0 and to PRTN0_CORE1_PCONF[CCE] field for Cortex-M7_1. 

2. The application core starts running. In case of Lock-step mode, the checker core executes the same code after a delay of two cycles. 

### 79.5.6 Debugger considerations while flash program/erase 

The flash programming can be done by application cores as well as debugger. The debugger can program/erase flash using either of the following two options: 

1. Loading the program/erase code to SRAM from the debugger and then executing the program/erase sequence by application code from SRAM. 

   - Debugger is connected and authenticated. 

   - The debugger loads the code in the form of application binary image into the on-chip SRAM. 

   - The debugger then initiates the application core to execute the binary from SRAM. 

2. Debugger executing the program/erase sequence. 

   - Debugger is connected and authenticated. 

   - The debugger then initiates the flash programming by reading/writing the registers involved and following the program/ erase sequence. 

First option is the recommended because of less execution time. In second option, the debugger is the master and since the debug interface is serial, the execution takes more time. 

In some cases, you might experience flash program/erase failure due to flash watchdog timeout when debugger executes the flash program/erase sequence due to the serial interface. Therefore, it is recommended to use the first option. In case second option is required, it should be performed in reduced clocking options (Option E and E2 only. For details, refer to the Clocking details section in the Clocking chapter). 

### 79.5.7 SWJ-DP sequence for debug authentication 

To perform the SWJ-DP sequence for debug authentication, the debugger: 

1. Polls the AUTHSTTS[CHALRDY] field until it indicates the challenge status. 

2. Reads Key Challenge (KEYCHAL0 - KEYCHAL7) if the challenge is valid and creates an authenticated 256-bit response key. 

3. Writes a 256-bit response key to Key Response (KEYRESP0 - KEYRESP7). 

4. Indicates that the response is ready by configuring AUTHCTL[HSEAUTHREQ]. 

5. Checks the status of Authentication Status (AUTHSTTS) to evaluate if the operation is successful. 

If the authentication process is successful and the debugger has write access to Debug Enable Control (DBGENCTRL), the challenge or response is considered successful too. 

~~<mark>NOTE</mark>~~ 

SDA_AP supports challenge and response based on both JTAG and SWJ-DP modes. See SDAAPGENCTRL0[JTAG_CR_EN] for details. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4558 / 4640 

NXP Semiconductors 

Debug Subsystem 

## 79.6 APB memory map 

You can access the debug registers via the APB_AP bus. The next table shows all the addresses for the CoreSight APB components and the addressing used for accessing the DAP components via the memory interface. You can also access all APB registers from the processing cores. 

Table 696. APB components mapping 

|Debug APB<br>component|APBIC base<br>address<br>(access from|System memory<br>(access from co|map address<br>res)|Memory<br>allocation (KB)|APB-AP0 slot<br>number|Applicability|
|---|---|---|---|---|---|---|
||debugger)|Page number|Base address||||
|APB_AP ROM<br>table|F8h|0|4024_00F8h|4|APBIC base|All|
|Funnel 0|1000h|0|4024_1000h|4|0|ETM/<br>ITM:S32K344,<br>S32K324,<br>S32K314<br>S32K358,<br>S32K348,<br>S32K338,<br>S32K328<br>ITM: S32K312,<br>S32K311,<br>S32K310,<br>S32K342,<br>S32K341,<br>S32K322|
|Funnel 1|2000h|0|4024_2000h|4|1|S32K344,<br>S32K324,<br>S32K314<br>S32K358,<br>S32K348,<br>S32K338,<br>S32K328|
|Funnel 2|3000h|0|4024_3000h|4|2|S32K344,<br>S32K324,<br>S32K314<br>S32K358,<br>S32K348,<br>S32K338,<br>S32K328|
|CM7_cluster_E<br>TF_ETMI|4000h|1|4024_4000h|4|3|S32K344,<br>S32K324,<br>S32K314<br>S32K358,<br>S32K348,<br>S32K338,<br>S32K328|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4559 / 4640 

NXP Semiconductors 

Debug Subsystem 

Table 696. APB components mapping (continued) 

|Debug APB<br>component|APBIC base<br>address<br>(access from|System memor<br>(access from co|y map address<br>res)|Memory<br>allocation (KB)|APB-AP0 slot<br>number|Applicability|
|---|---|---|---|---|---|---|
||debugger)|Page number|Base address||||
|CM7_cluster_E<br>TF_ETMD|5000h|1|4024_5000h|4|4|S32K344,<br>S32K324,<br>S32K314<br>S32K358,<br>S32K348,<br>S32K338,<br>S32K328|
|HTM ETF|6000h|1|4024_6000h|4|5|S32K344,<br>S32K324,<br>S32K314<br>S32K358,<br>S32K348,<br>S32K338,<br>S32K328|
|Shared_system<br>_ETF|7000h|1|4024_7000h|4|6|S32K344,<br>S32K324,<br>S32K314<br>S32K358,<br>S32K348,<br>S32K338,<br>S32K328|
|HTM 0|8000h|2|4024_8000h|4|7|S32K344,<br>S32K324,<br>S32K314<br>S32K358,<br>S32K348,<br>S32K338,<br>S32K328|
|HTM 0 CTI|9000h|2|4024_9000h|4|8|All|
|TPIU|A000h|2|4024_A000h|4|9|S32K344,<br>S32K324,<br>S32K314<br>S32K358,<br>S32K348,<br>S32K338,<br>S32K328|
|System SWO|B000h|2|4024_B000h|4|10|All|
|Timestamp CTL|C000h|3|4024_C000h|4|11|All|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4560 / 4640 

NXP Semiconductors 

Debug Subsystem 

## 79.7 Trace 

### 79.7.1 Trace modules and connectivity 

The Trace subsystem: 

- Combines trace data from all internal clients that generate trace information 

- Includes a 32-bit TPIU 

- Includes these components: 

   - ATB 

   - ATBR 

   - CSTF 

   - Debug APB 

   - ETF 

   - TPIU 

Multiple options for trace output allow parallel tracing. Trace information can be read from the trace interface or the DAP interface, and traces can be alternatively read out from ETF at a slow speed via APB_AP. Table 697 shows EFT sizes. 

Table 697. ETF sizes 

|FIFO|Memory interface data width (in bits)|Size (KB)|
|---|---|---|
|Cortex-M7 ETM/ITM cluster ETF|64|1|
|Cortex-M7 ETMD cluster ETF|128|2|
|HTM ETF|64|1|
|Shared system ETF|64|2|



~~<mark>NOTE</mark>~~ 

- The DMA-HTM trace supports four words at 80 MHz. For HTM trace, both DBGENCTRL[GSPNIDEN] and DBGENCTRL[GSPIDEN] must be 1. 

- Enabling any one of data trace causes overflow inside ETM and trace packets get dropped. Enabling instruction trace of both the core simultaneously does not cause any overflow. 

Control (MDMAPCTL) provides fields to override the speed control (see Table 698 for details) from some of the trace sinks (and TPIU). The complete trace pipeline bandwidth is limited by the slowest sink component. The default settings of these fields allow maximum bandwidth for the TPIU to trace. When tracing to memory (if supported), the fields may need to be changed. 

Table 698. Trace output overrides 

|Trace destination|SWO_override|TPIU_override|
|---|---|---|
|TPIU|1|0|



The trace sources of the chip are the cores and their related modules. Trace funnels exist for all possible trace clients. For more information on the various components in the trace bus connectivity, see the CoreSight Components Technical Reference Manual (available in References). See Table 699 for details on funnel assignments. 

The ATBR is integrated to send a shared funnel output across TPIU. This figure illustrates the chip's detailed trace architecture. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4561 / 4640 

NXP Semiconductors 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Debug/079_Debug_Subsystem/S32K3XXRM_数据表.pdf-4562-01.png)


<!-- Start of picture text -->
Debug Subsystem<br><!-- End of picture text -->


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Debug/079_Debug_Subsystem/S32K3XXRM_数据表.pdf-4562-02.png)


<!-- Start of picture text -->
Trace @ 50 MHz DDR: 50 MHz clock logic Trace CLKOUT: 25 MHz<br>Cortex-M7_0 ETMI 8 UP 32 240 MHz Trace @ 120 MHz DDR: 240 MHz clock logic (room temperature only)Trace @ 120 MHz DDR: 120 MHz clock logic Trace CLKOUT: 60 MHzTrace CLKOUT: 120 MHz<br>Cortex-M7_0 ITM 8 UP 32<br>Cortex-M7_1 ETMI 8 UP 32<br>Not available on Funnel 0 32 ETF 16 Async 32<br>the S32K314 Cortex-M7_1 ITM 8 UP 32 1 KB bridge<br>Only available on Cortex-M7_2 ETMI 8 UP 32<br> the S32K358<br>Cortex-M7_2 ITM 8 UP 32<br>32 CLKOUT<br>TPIU<br>Cortex-M7_0 ETMD 64 Funnel 232-bit 32 ETF32 KB 160 M32 A B 120/25 M<br>32 8<br>DN SWO<br>Not available on Funnel 1 64 ETF 64 DN 32 Async<br>64 2 KB bridge<br> the S32K314 Cortex-M7_1 ETMD<br>Only available on 64<br>Cortex-M7_2 ETMD<br> the S32K358<br>AXBS masters<br>EMACDMA HTM 32 1 KBETF bridgeAsync 32<br>Figure 508. S32K358 and S32K3x4 detailed trace architecture<br>160 MHz 25 MHz<br>8<br>Cortex-M7_0 ITM<br>8 8<br>Funnel 0 A B SWO<br>Async<br>bridge<br>8<br>Cortex-M7_1 ITM<br>Figure 509. S32K342/S32K322 detailed trace architecture<br>120 MHz 25 MHz<br>8 8<br>Cortex-M7_0 ITM A B SWO<br>Async<br>bridge<br>Figure 510. S32K312/S32K311 detailed trace architecture<br>Repilcator<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4562 / 4640 

NXP Semiconductors 

Debug Subsystem 

Table 699. Funnel assignments 

|Funnel|Port|Input|S32K344<br>Frquency (MHz)|S32K358<br>Frequency (MHz)|Applicability|
|---|---|---|---|---|---|
|0|0|Cortex-M7_0 ETMI|160|240|S32K3x4|
|0|1|Cortex-M7_0 ITM|160|240|S32K358, S32K338|
|0|2|Cortex-M7_1 ETMI|160|240|S32K324 S32K338,<br>S32K328|
|0|3|Cortex-M7_1 ITM|160|240|All|
|0|4|Cortex-M7_2 ETMI|-|240|S32K344, S32K358|
|0|5|Cortex-M7_2 ITM|-|240|S32K358, S32K338|
|0|6-7|Reserved|-|240|-|
|1|0|Cortex-M7_0 ETMD|160|240|S32K344, S32K324,<br>S32K314 S32K358,<br>S32K348, S32K338,<br>S32K328|
|1|1|Cortex-M7_1 ETMD|160|240|S32K324 S32K338,<br>S32K328|
|1|2|Cortex-M7_2 ETMD|-|240|S32K358, S32K338|
|1|3-7|Reserved|-|240|-|
|2|0|Cortex-M7 instruction ETF<br>through an asynchronous<br>bridge|160|240|S32K344, S32K324,<br>S32K314 S32K358,<br>S32K348, S32K338,<br>S32K328|
|2|1|Cortex-M7 data ETF through<br>an asynchronous bridge|160|240|S32K344, S32K324,<br>S32K314 S32K358,<br>S32K348, S32K338,<br>S32K328|
|2|2|HTM ETF through an<br>asynchronous bridge|160|160|S32K344, S32K324,<br>S32K314 S32K358,<br>S32K348, S32K338,<br>S32K328|
|2|3-7|Reserved|-|-|-|



#### 79.7.1.1 Chip's bus trace client 

Chips in the S32K3xx family include a bus trace client. 

HTM provides the address and data trace information about AXBS buses. The information from an HTM can be used with the debugger to enable easy, accurate debugging on AXBS-based embedded systems. The chip implements an HTM64 configuration to trace 64-bit AXBS masters in the system. To simplify the implementation, instead of tracing the individual ports of various AXBS masters and slaves, which may be running at different frequencies, HTM64 snoops the AXBS crossbar master ports that are all synchronous with a 160 MHz system clock. This table provides details related to the HTM input connectivity. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4563 / 4640 

NXP Semiconductors 

Debug Subsystem 

Table 700. HTM connections 

|HTM64 port|AHB crossbar port|
|---|---|
|HTMBUSSELECT0|M0 AXBS_Lite XBIC (DMA)|
|HTMBUSSELECT1|M3 AXBS (Ethernet)|



#### 79.7.1.2 TPIU interface 

A standard 16-bit parallel TPIU is integrated into the debug subsystem. Chips in the S32K3xx family generate the trace via the trace port. 

To prevent instruction trace from being dropped in a multi-core environment, a TPIU throughput of 55.2 MB/s or higher must be maintained. You could use these pin and frequency combinations: 

- Four high-speed data + one clock pads @120 MHz (240 Mbit/s throughput per pad) totaling 120 MB/s 

- 16 low-speed data + one clock pads @25 MHz (50 Mbit/s throughput per pad) totaling 100 MB/s 

High-end chips from the S32K3xx family support at least 56 MB/s of trace throughput on the TPIU interface. 

Table 701. Throughput 

|Core|Throughput value|Applicability|
|---|---|---|
|Cortex-M7_0|27.6 MB/s|All|
|Cortex-M7_1|27.6 MB/s|S32K338, S32K328 S32K324,<br>S32K314 S32K322|
|Cortex-M7_2|27.6 MB/s|S32K358, S32K338|
|Total|82.8 MB/s||



#### 79.7.1.3 TPIU flush 

To allow the chip to enter Standby mode, software executes an WFI instruction indicating Standby entry. When the chip enters this mode, MC_RGM asserts a trace flush request to the TPIU and waits for a trace flush done signal from the TPIU  before requesting MC_PCU to proceed. The TPIU and debug infrastructure clocks can be gated after this. Because the TPIU is sourced from system clock, the clock must not be gated until this point. 

### 79.7.2 Trace assignments 

ETF combines trace information from multiple clients into a single stream of trace data. This table shows the CoreSight funnel input assignments. 

Table 702. CoreSight funnel assignments 

|Instance name<br>Port assignment|Applicability|
|---|---|
|Funnel 0 (CSTF0)<br>Cortex-M7_0 ETMI|S32K3x4|
|Cortex-M7_0 ITM|All|
|Cortex-M7_1 ETMI|S32K3x4|
|Cortex-M7_1 ITM|S32K324, S32K322, S32K312|
|Cortex-M7_2 ITM|S32K358, S32K338|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4564 / 4640 

NXP Semiconductors 

Debug Subsystem 

Table 702. CoreSight funnel assignments (continued) 

|Instance name<br>Port assignment|Applicability|
|---|---|
|Funnel 1 (CSTF1)<br>Cortex-M7_0 ETMD|S32K3x4|
|Cortex-M7_1 ETMD|S32K324|
|Cortex-M7_2 ETMD|S32K358,S32K338|
|Funnel 2 (CSTF2)<br>Funnel 0|S32K3x4|
|Funnel 1|S32K3x4|
|HTM|S32K3x4|



## 79.8 Embedded cross trigger (ECT) 

ECT allows multi-core run control and trace cross-triggering, such as synchronous stop-start for all cores or trigger trace on a trigger event from another core or module. See the CoreSight Components Technical Reference Manual (available in References) for detailed information on ECT. 

ECT architecture involves CTMs and CTIs. The CTIs provide a cross-triggering interface between the cores and other debug and trace modules. The channels of these CTIs are interconnected using CTMs, as shown in this figure. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Debug/079_Debug_Subsystem/S32K3XXRM_数据表.pdf-4565-07.png)


<!-- Start of picture text -->
CTM 0<br>CH 0 CH 1 CH 2 CH 3<br>Reserved<br>CH 0<br>CTM 1 HTM<br>CH 1 CH 2 CH 3<br>CTI<br>5<br>off_pl_ETF<br>_Trigger<br>Figure 511. ECT<br>CTI CTI CTI<br>Cortex-M0+   CTI<br>Cortex-M7_0 Cortex-M7_1 Cortex-M7_2<br><!-- End of picture text -->

### 79.8.1 CTI assignments 

Table 703. CTI assignments 

|CTI instance|Trigger number|Trigger in|Trigger out|
|---|---|---|---|
|CTI_Cortex-M7_0|7|ETM event output 3|Processor restart|
||6|ETM event output 2|ETM event input 3|
||5|ETM event output 1|ETM event input 2|
||4|ETM event output 0|ETM event input 1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4565 / 4640 

NXP Semiconductors 

Debug Subsystem 

Table 703. CTI assignments (continued) 

|CTI instance|Trigger number|Trigger in|Trigger out|
|---|---|---|---|
||3|DWT comparator output 2|ETM event input 0|
||2|DWT comparator output 1|Interrupt request 1|
||1|DWT comparator output 0|Interrupt request 0|
||0|Processor halted|Processor debug request|
|CTI_Cortex-M7_1|7|ETM event output 3|Processor restart|
||6|ETM event output 2|ETM event input 3|
||5|ETM event output 1|ETM event input 2|
||4|ETM event output 0|ETM event input 1|
||3|DWT comparator output 2|ETM event input 0|
||2|DWT comparator output 1|Interrupt request 1|
||1|DWT comparator output 0|Interrupt request 0|
||0|Processor halted|Processor debug request|
|CTI_Cortex-M7_2|7|ETM event output 3|Processor restart|
||6|ETM event output 2|ETM event input 3|
||5|ETM event output 1|ETM event input 2|
||4|ETM event output 0|ETM event input 1|
||3|DWT comparator output 2|ETM event input 0|
||2|DWT comparator output 1|Interrupt request 1|
||1|DWT comparator output 0|Interrupt request 0|
||0|Processor halted|Processor debug request|
|CTI_0|7|Reserved (grounded)|Reserved (no connection)|
||6|ETF_3 full|ETF_3 trigger input|
||5|ETF_2 full|ETF_2 trigger input|
||4|ETF_1 full|ETF_1 trigger input|
||3|ETF_0 full|ETF_0 trigger input|
||2|HTM trigger out 2|HTM trigger in 2|
||1|HTM trigger out 1|HTM trigger in 1|
||0|Reserved|HTM trigger in 0|



## 79.9 Low-power debug handshake protocol 

The debugger must perform this sequence to enter or exit Standby mode, if the debugger handshake is enabled: 

1. Power on DAP. 

The debugger connection is established. 

2. Configure the Debug subsystem for the relevant operations. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4566 / 4640 

NXP Semiconductors 

Debug Subsystem 

3. Write 1 to to gate entry into Standby mode with the debugger handshake. 

4. Disable POR_WDG for monitoring the entry to or exit from Standby mode by writing 1 to DCM's DCMRWP1[8] field. This is required for low-power debug handshake because debugger configurations can be more time consuming than the POR_WDG threshold levels and can raise a false POR_WDG event. 

5. Write 1 to DCMRWF1[STANDBY_IO_CONFIG] in the Device Configuration Module (DCM). This causes padkeeping to be disabled on standby entry itself without any software dependency. This is needed in case of low-power debug since otherwise the padkeeping on TDO would result in no debugger communication. In other cases, DCMRWF1[STANDBY_IO_CONFIG] should be configured as 0 before standby entry. 

6. Initiate entry into Standby mode. See the "Power Management" chapter for the Standby mode entry sequence and configurations. 

7. Identify whether the low-power debug is enabled on the low-power entry by reading MC_RGM's LPDEBUG[LP_DBG_EN] field. 

   - If low-power debug is enabled and TPIU is enabled too, trace flush starts, and the debugger acknowledges the following: 

      - Low-power debug traces 

      - DAP-related configuration reception and context saving 

After this, the chip enters Standby mode. 

- If TPIU is disabled: 

   - The debugger acknowledges DAP-related configuration reception and context saving by writing 1 to MDMAPWIRREL[PRVNTRSTRGM]. 

After this, the chip enters Standby mode. 

- If low-power debug is disabled, the chip enters Standby mode without waiting for debugger acknowledgment. 

On any wakeup event, the chip starts the Standby mode exit sequence described in the "Power Management" chapter. After the chip exits Standby mode, the debugger connection is restored. By this time, the debugger is already aware that it has enabled the low-power debug handshake. In this case, the debugger must poll MDMAPSTTS[DESTRST] to check whether: 

- The debug infrastructure is out of reset. 

- The DAP connection can be established. 

After DAP is powered on (the debugger connection is established), the debugger: 

- a. Reconfigures the debug and trace attributes using the fields in DBGENCTRL 

- b. Writes 1 to MDMAPWIRREL[WTRSTRGM] after the debugger trace context is restored 

The chip exits Standby mode. 

If low-power debug is not configured, the chip exits Standby mode without waiting for the debugger to write to MDMAPWIRREL[WTRSTRGM]. 

8. Reconfigure the debug and trace configuration in SDA_AP register descriptions after the chip exits Standby mode. 

~~<mark>NOTE</mark>~~ 

If the chip wakes up from Standby mode through pad reset, the debugger must perform a CR again. 

## 79.10 Debug resets 

The debug subsystem follows this sequence on the source of reset: 

1. POR resets the complete debug logic. 

2. The destructive reset resets all types of debug logic except JTAGC. 

Conversely, the debug subsystem can generate a system reset using these mechanisms: 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4567 / 4640 

NXP Semiconductors 

Debug Subsystem 

- System destructive reset defined in Control (MDMAPCTL) that allows the debugger to provide the destructive reset to the system. The debugger loses connection to the system with this reset. 

- System functional reset defined in Control (MDMAPCTL) that allows the debugger to hold the system in functional reset. 

To program various debug registers, the functional clocks must be enabled. All debug and trace components must be on destructive reset. 

## 79.11 Debug across device LifeCycles 

The debug access to the system is available in early lifecycles and subsequently based on NVM configuration settings. 

After the debug is set to 'Trusted', the system access is allowed after a successful authorization step between the debugger and the system. 

The authorization provides provisions to allow debug for Cortex M0+ core and Cortex M7 cores. 

Following table shows the debug access based on various configuration bits. 

Table 704. Debug access based on LifeCycle and bit configurations 

|LifeCycle|Configurati|on bits|||Debug access|
|---|---|---|---|---|---|
||DBG_EN_OEM|APP_DIS_OEM|DBG_EN_FLD|APP_DIS_FLD|Appl Core Debug|
|MCU_PROD|-|-|-|-|Open|
||-|-|-|-|Open|
|CUST_DEL|-|-|-|-|Open|
||-|-|-|-|Open|
|OEM_PROD|0|-|-|-|Closed|
||1|0|-|-|Trusted|
||1|0|-|-|Trusted|
||1|1|-|-|Disabled|
|IN_FIELD|-|-|0|-|Closed|
||-|-|1|0|Trusted|
||-|-|1|0|Trusted|
||-|-|1|1|Disabled|
|PRE_FA|-|-|-|-|Trusted|
||-|-|-|-|Trusted|
|FA|-|-|-|-|Open|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4568 / 4640 

NXP Semiconductors 

Debug Subsystem 

~~<mark>NOTE</mark>~~ 

1. Closed: Debug is not possible in this state (not even if keys are known - no authentication is possible) 

2. Open: Debug is always possible 

3. Trusted: Debug is possible after successful authentication (Challenge/Response handshake with correct credentials) 

4. Disabled: Debug has been explicitly disabled via burning of a fuse in that LC, otherwise behaves as Closed 

5. During functional reset, the debug-enable will retain its last status, while DCM scans NVM for lifecycle and DCF values. Debug status will be re-evaluated once dcm_done gets 1. 

6. During temporary advancement of lifecycle, debug-en will immediately reflect the status based on updated lifecycle/DCF bits. 

## 79.12 Pin interface 

This table presents a summary of functional and power pins that are used for debugging purposes. 

Table 705. Pin interface 

|Pin type|Pins|Number of pins (balls)<sup>1</sup>|Nominal voltage|
|---|---|---|---|
|Functional JTAG|JCOMP, TCK, TMS, TDI, TDO|Five (only TDI and TDO can be<br>multiplexed with GPIO or other<br>functions)|3.3 V, 5 V|
|Functional trace pins<br>|TRACE_CLK|One|3.3 V, 5 V|
|(parallel trace)|TRACE_D[15:0]|16|3.3 V, 5 V|
|Ground|VSS|See the IOMUX file attached to<br>this document for information on<br>the number of VSS pins in various<br>packages.|0 V|



1. The terms pins and balls are used interchangeably. Some chip packages include pins and others include balls. 

~~<mark>NOTE</mark>~~ 

Fast Trace pad TRACE_D[15:0] is available only in S32K344. 

### 79.12.1 Debug port and pin descriptions 

The pads to which the debug signals are mapped operate using the JTAG functionality out of reset but can later be reassigned to their alternate functionalities. TDI and TDO can operate as alternate GPIO functions. See this table for pin assignments in different modes. 

Table 706. Debug port pins 

|Pin name|JTAG deb<br>Type|ug port<br>Description|Internal pullup or<br>pulldown logic|
|---|---|---|---|
|TMS|I/O|JTAG test mode selection (TMS)|Pullup|
|TCK/SWCLK|I|JTAG test clock (TCK)|Pulldown|
|TDI|I|JTAG test data input (TDI)|Pullup|
|TDO/TRACESWO|O|JTAG test data output (TDO)|Not connected|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4569 / 4640 

NXP Semiconductors 

Debug Subsystem 

### 79.12.2 Trace port pin descriptions 

This chip generates trace via TPIU that transmits the trace data out of the chip over a parallel trace port. The trace port consists of an ETM trace clock and 16 parallel trace data outputs. The Arm optional trace port control (TRACECTRL), debug request (DBGRQ), and debug acknowledge (DBGACK) signals are not implemented. 

Table 707. Trace output port pins 

|Pin name|Description|
|---|---|
|TRACE_DATA00|ETM parallel trace data output 01|
|TRACE_DATA01|ETM parallel trace data output 01|
|TRACE_DATA02|ETM parallel trace data output 02|
|TRACE_DATA03|ETM parallel trace data output 03|
|TRACE_DATA04|ETM parallel trace data output 04|
|TRACE_DATA05|ETM parallel trace data output 05|
|TRACE_DATA06|ETM parallel trace data output 06|
|TRACE_DATA07|ETM parallel trace data output 07|
|TRACE_DATA08|ETM parallel trace data output 08|
|TRACE_DATA09|ETM parallel trace data output 09|
|TRACE_DATA10|ETM parallel trace data output 10|
|TRACE_DATA11|ETM parallel trace data output 11|
|TRACE_DATA12|ETM parallel trace data output 12|
|TRACE_DATA13|ETM parallel trace data output 13|
|TRACE_DATA14|ETM parallel trace data output 14|
|TRACE_DATA15|ETM parallel trace data output 15|
|TRACE_CLK|ETM parallel trace clock output|



~~<mark>NOTE</mark>~~ 

ETM is supported in S32K344 only 

~~<mark>NOTE</mark>~~ 

By default, Rx pins float and are not pulled inside. An internal active pulldown logic exists only when you enable Rx via software (IBE). 

## 79.13 Timestamp distribution network 

The timestamp distribution network uses CoreSight timestamp components to generate a 48-bit timestamp value for the trace sources, as shown in the next figure. The CoreSight timestamp generator generates a 64-bit counter value, but only the least significant 48 bits are distributed to the trace sources. A 7-bit narrow timestamp is derived from the 48-bit timestamp and distributed to the trace client, where a decoder regenerates the 48-bit timestamp. The generator must be programmed, and you could find the related programming information in the CoreSight Components Technical Reference Manual (available in References). 

This chip supports 48-bit timestamping. The generator operates at a frequency of 160 MHz and gives a 64-bit timestamp value. The Cortex-M7_0 and Cortex-M7_1 cores operate at a frequency of 160 MHz. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4570 / 4640 

NXP Semiconductors 

Debug Subsystem 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Debug/079_Debug_Subsystem/S32K3XXRM_数据表.pdf-4571-02.png)


<!-- Start of picture text -->
Cortex-M7_0 (ts_valueb)<br>[63:48] - GND<br>[47:0] - Tied to generator<br>Generator at Cortex-M7_1 (ts_valueb) Not available on the<br>160 MHz<br>[63:48] - GND S32K311 and S32K312<br>64-bit output [47:0] - Tied to generator<br>Cortex-M7_2 (ts_valueb) Only available<br>[63:48] - GND on the S32K358<br>[47:0] - Tied to generator<br><!-- End of picture text -->

Figure 512. Timestamp distribution network 

## 79.14 Peripheral debug freeze register descriptions 

Implement the logic provided in this section for each peripheral instance supporting the debug operation. 

~~<mark>NOTE</mark>~~ 

Debug freeze is enabled for all the peripherals so that as soon as the core halts, peripherals can be frozen to support debugging from the first instruction. 

For register details, refer to the following registers in the Device Configuration Module (DCM): 

- Read Write GPR On Destructive Reset Register (DCMRWD6) 

- Read Write GPR On Destructive Reset Register (DCMRWD7) 

- Read Write GPR On Destructive Reset Register (DCMRWD8) 

- Read Write GPR On Destructive Reset Register (DCMRWD9) 

## 79.15 MDM_AP register descriptions 

The debugger has access to the status and control elements implemented as registers in MDM_AP, which is selected by APSEL (6h) on the DAP bus. These registers provide additional control and status information for typical debug, cross-triggering, and run-control scenarios. Also, the register fields provide a way for the debugger to get the updated status of the core without initiating a bus transaction across the crossbar switch, thus remaining less intrusive during a debug session. 

MDM_AP is accessible as DAP (see DAP TAP for details). 

### 79.15.1 MDM_AP memory map 

MDM_AP base address: 4025_0600h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|Status (MDMAPSTTS)|32|RO|F000_0000h|
|4h|Control (MDMAPCTL)|32|RW|0640_0000h|
|30h|WIR Enable (MDMAPWIREN)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4571 / 4640 

NXP Semiconductors 

Debug Subsystem 

##### Table continued from the previous page... 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|38h|MDM AP WIR Release (MDMAPWIRREL)|32|RW|0000_0000h|



### 79.15.2 Status (MDMAPSTTS) 

##### Offset 

|Register|Offset|
|---|---|
|MDMAPSTTS|0h|



##### Diagram 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Debug/079_Debug_Subsystem/S32K3XXRM_数据表.pdf-4572-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>CM72 Reserv CM71 CM70 CM0P CM72 CM71 CM70 CM0P CM72 CM71 CM70<br>R Reserved<br>DBG... ed  DBG... DBG... SLP... SLP... SLP... SLP... DPS... DPS... DPS... DPS...<br>W<br>Reset 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>HSEH CM72 CM71 CM70 FUNC DEST Reserv<br>R Reserved<br>LT  HLT  HLT  HLT  RST  RST  ed<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Cortex-M7_2 Debug Restarted|
|CM72DBGRST<br>RD|Indicates if Cortex-M7_2 has returned to Normal mode from Debug mode.<br>0b - In Debug mode|
||1b - In Normal mode|
|30|Reserved|
|—<br>29|Cortex-M7_1 Debug Restarted|
|CM71DBGRST<br>RD|Indicates if Cortex-M7_1 has returned to Normal mode from Debug mode.<br>0b - In Debug mode|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4572 / 4640 

NXP Semiconductors 

Debug Subsystem 

Table continued from the previous page... 

|Field|Function<br>1b - In Normal mode|
|---|---|
|28<br>CM70DBGRST<br>RD|Cortex-M7_0 Debug Restarted<br>Indicates if Cortex-M7_0 has returned to Normal mode from Debug mode.<br>0b - In Debug mode<br>1b - In Normal mode|
|27-24<br>—|Reserved|
|23<br>CM0PSLPNG|Cortex-M0+ Sleeping<br>Indicates if Cortex-M0+ is in Sleep mode.<br>0b - Not in Sleep mode<br>1b - In Sleep mode|
|22<br>CM72SLPNG|CM7_2 Sleeping<br>Indicates if Cortex-M7_2 is in Sleep mode.<br>0b - Not in Sleep mode<br>1b - In Sleep mode|
|21<br>CM71SLPNG|CM7_1 Sleeping<br>Indicates if Cortex-M7_1 is in Sleep mode.<br>0b - Not in Sleep mode<br>1b - In Sleep mode|
|20<br>CM70SLPNG|Cortex-M7_0 Sleeping<br>Indicates if Cortex-M7_0 is in Sleep mode.<br>0b - Not in Sleep mode<br>1b - In Sleep mode|
|19<br>CM0PDPSLP|Cortex-M0+ Deep Sleep<br>Indicates if Cortex-M0+ is in Deep Sleep mode.<br>0b - Not in Deep Sleep mode<br>1b - In Deep Sleep mode|
|18<br>CM72DPSLP|Cortex-M7_2 Deep Sleep<br>Indicates if Cortex-M7_2 is in Deep Sleep mode.<br>0b - Not in Deep Sleep mode<br>1b - In Deep Sleep mode|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4573 / 4640 

NXP Semiconductors 

Debug Subsystem 

Table continued from the previous page... 

|Field|Function|
|---|---|
|17<br>CM71DPSLP|Cortex-M7_1 Deep Sleep<br>Indicates if Cortex-M7_1 is in Deep Sleep mode.<br>0b - Not in Deep Sleep mode<br>1b - In Deep Sleep mode|
|16<br>CM70DPSLP|Cortex-M7_0 Deep Sleep<br>Indicates if Cortex-M7_0 is in Deep Sleep mode.<br>0b - Not in Deep Sleep mode<br>1b - In Deep Sleep mode|
|15<br>HSEHLT|Cortex-M0+ Halted<br>Indicates if Cortex-M0+ is halted because of entry into Debug mode.<br>0b - Core is not halted<br>1b - Core is halted|
|14<br>CM72HLT|CM7_2 Debug Halted<br>Indicates if Cortex-M7_1 is halted because of entry into Debug mode.<br>0b - Core is not halted<br>1b - Core is halted|
|13<br>CM71HLT|CM7_1 Debug Halted<br>Indicates if Cortex-M7_2 is halted because of entry into Debug mode.<br>0b - Core is not halted<br>1b - Core is halted|
|12<br>CM70HLT|Cortex-M7_0 Halted<br>Indicates if Cortex-M7_0 is halted because of entry into Debug mode.<br>0b - Core is not halted<br>1b - Core is halted|
|11-3<br>—|Reserved|
|2<br>FUNCRST|Functional Reset<br>Indicates the system reset state.<br>0b - Not in functional reset<br>1b - In functional reset|
|1|Destructive Reset<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4574 / 4640 

NXP Semiconductors 

Debug Subsystem 

Table continued from the previous page... 

|Field|Function|
|---|---|
|DESTRST|Indicates the system reset state.|
||0b - Not in destructive reset|
||1b - In destructive reset|
|0<br>—|Reserved|



### 79.15.3 Control (MDMAPCTL) 

##### Offset 

|Register|Offset|
|---|---|
|MDMAPCTL|4h|



##### Function 

##### Allows the debugger: 

- To give the destructive reset to the system. A system destructive reset enables this. The debugger also loses connection to the system with this reset. 

- To hold the system in functional reset. A system functional reset enables this. 

~~<mark>NOTE</mark>~~ 

The trace functionality on trace pins is selected with this register and is retained across the functional reset. 

##### Diagram 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Debug/079_Debug_Subsystem/S32K3XXRM_数据表.pdf-4575-14.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R CM72 Reserv CM71 CM70 RSTR RSTR RSTR SWOO Reserv TRIUO<br>Reserved  Reserved<br>W DBG... ed  DBG... DBG... ELC... ELC... ELC... VRD  ed  VRD<br>Reset 0 0 0 0 0 1 1 0 0 1 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R POR_<br>DBGR Reserv CM72 CM71 CM70 SYSF SYSR<br>WDG.. Reserved  Reserved  Reserved<br>W STS... ed  DBG... DBG... DBG... UNC... ESE...<br>.<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Cortex-M7_2 Debug Restart|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4575 / 4640 

NXP Semiconductors 

Debug Subsystem 

Table continued from the previous page... 

|Field|Function|
|---|---|
|CM72DBGRSR<br>T|Indicates if a request to Cortex-M7_2 to leave the debug halt state is asserted.<br>0b - Normal operation<br>1b - Request asserted|
|30<br>—|Reserved|
|29<br>CM71DBGRSR<br>T|Cortex-M7_1 Debug Restart<br>Indicates if a request to Cortex-M7_1 to leave the debug halt state is asserted.<br>0b - Normal operation<br>1b - Request asserted|
|28<br>CM70DBGRSR<br>T|Cortex-M7_0 Debug Restart<br>Indicates if a request to Cortex-M7_0 to leave the debug halt state is asserted.<br>0b - Normal operation<br>1b - Request asserted|
|27<br>RSTRELCM72|Reset Release for CM7_2<br>Control signal to release the reset for CM7_2. This was done to debug the core from first instruction. The<br>default value is 1.|
|26<br>RSTRELCM71|Reset Release for CM7_1<br>Control signal to release the reset for CM7_1. This was done to debug the core from first instruction. The<br>default value is 1.|
|25<br>RSTRELCM70|Reset Release for CM7_0<br>Control signal to release the reset for CM7_0. This was done to debug the core from first instruction. The<br>default value is 1.|
|24-23<br>—|Reserved|
|22<br>SWOOVRD|SWO Override<br>Indicates if the SWO trace response is overriden. When TPIU is not the selected trace sink target, you<br>must override the trace response.<br>0b - Not overridden, and SWO generates the trace response<br>1b - Is overridden|
|21<br>—<br>20|Reserved<br>TPIU Override|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4576 / 4640 

NXP Semiconductors 

Debug Subsystem 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|TRIUOVRD|Indicates if TPIU trace response is overridden. When TPIU is not the selected trace sink target, you must<br>override the trace response.<br>0b - Not overridden, and TPIU generates the trace response<br>1b - Is overridden and asserted|
|19-16|Reserved|
|—<br>15|Power Watchdog Status|
|POR_WDG_DI<br>S_FUNC_RST|0b - Power watchdog is disabled<br>1b - Power watchdog is enabled|
|14-13<br>—<br>12|Reserved<br>Debug Over Reset Via Slow Pads|
|DBGRSTSLOW<br>PAD|Enables or diasables trace via slow pads. If enabled, the trace pads have trace over functional reset<br>feature enabled. This field does not take care of the clock configuration.<br>0b - Disabled<br>1b - Enabled|
|11<br>—|Reserved|
|10<br>CM72DBGREQ|Cortex-M7_2 Debug Request<br>Drives the EDBGREQ input for Cortex-M7_2 and indicates if the debug request is generated.<br>When the core goes into debug state, the field acknowledges that with a halted output signal (see<br>MDMAPSTTS[CM72HLT]). If the core is in Stop mode, this field is used to wake up the core and<br>transition it to the debug halt state.<br>0b - Debug request is not generated<br>1b - Debug request is generated|
|9<br>CM71DBGREQ|Cortex-M7_1 Debug Request<br>Drives the EDBGREQ input for Cortex-M7_1 and indicates if the debug request is generated.<br>When the core goes into debug state, the field acknowledges that with a halted output signal (see<br>MDMAPSTTS[CM71HLT]). If the core is in Stop mode, this field is used to wake up the core and<br>transition it to the debug halt state.<br>0b - Debug request is not generated<br>1b - Debug request is generated|
|8<br>CM70DBGREQ|Cortex-M7_0 Debug Request|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4577 / 4640 

NXP Semiconductors 

Debug Subsystem 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||Drives the EDBGREQ input for Cortex-M7_0 and indicates if the debug request is generated.<br>When the core goes into debug state, the field acknowledges that with a halted output signal (see<br>MDMAPSTTS[CM70HLT]). If the core is in Stop mode, this field is used to wake up the core and<br>transition it to the debug halt state.<br>0b - Debug request is not generated<br>1b - Debug request is generated|
|7-6<br>—|Reserved|
|5<br>SYSFUNCRST|System Functional Reset<br>Asserts or deasserts functional reset to the chip. The debugger maintains connection with the chip.<br>0b - Deasserted<br>1b - Asserted|
|4<br>SYSRESETRE<br>Q|System Destructive Reset<br>Asserts or deasserts destructive reset to the chip. The debugger also loses connection with this reset.<br>When this field is reset, the entire system comes out of reset.<br>0b - Deasserted<br>1b - Asserted|
|3-0<br>—|Reserved|



### 79.15.4 WIR Enable (MDMAPWIREN) 

##### Offset 

|Register|Offset|
|---|---|
|MDMAPWIREN|30h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4578 / 4640 

NXP Semiconductors 

Debug Subsystem 

##### Diagram 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Debug/079_Debug_Subsystem/S32K3XXRM_数据表.pdf-4579-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R LWPW<br>Reserved<br>W REN<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-1|Reserved|
|—||
|0|Low Power Debug Enable|
|LWPWREN|Enables or disables low-power debug.|
||When the debugger writes 1 to this field, MC_RGM's LPDEBUG[LP_DBG_EN] field becomes 1 too.|
||0b - Disabled|
||1b - Enabled|



### 79.15.5 MDM AP WIR Release (MDMAPWIRREL) 

##### Offset 

|Registe|r||O|ffset|||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|MDMA|PWIRR|EL|3|8h|||||||||||||
|Diagram<br>Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|R<br>W||||||||Rese|rved||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||||||Rese|rved|||||||PRVN<br>TRS...|WTRS<br>TRGM|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Diagram 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4579 / 4640 

NXP Semiconductors 

Debug Subsystem 

##### Fields 

|Field|Function|
|---|---|
|31-2|Reserved|
|—||
|1|Prevent Reset|
|PRVNTRSTRG<br>M|Indicates if MC_RGM is prevented from generating reset.<br>After TPIU flush, this field prevents MC_RGM from generating reset even if MC_RGM receives an<br>acknowledge response from TPIU. This is valid for low-power entry.<br>0b - Normal operation<br>1b - MC_RGM prevented|
|0<br>WTRSTRGM|Wait In Reset B<br>Indicates if waiting of MC_RGM from generating reset is supported.<br>On exiting Standby mode, MC_RGM waits until the debugger writes to another field in the MDM_AP register<br>to allow it to exit reset.<br>0b - Normal operation<br>1b - Wait supported|



## 79.16 SDA_AP register descriptions 

The debugger and system have access to secure authentication control and status, implemented as registers in SDA_AP on the DAP bus. These registers provide authentication control, authentication status, key exchange information, and debug enable controls. 

### 79.16.1 SDA_AP memory map 

SDA_AP base address: 4025_4700h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|Authentication Status (AUTHSTTS)|32|RO|6000_0004h|
|4h|Authentication Control (AUTHCTL)|32|RW|0000_0000h|
|10h - 2Ch|Key Challenge (KEYCHAL0 - KEYCHAL7)|32|RO|0000_0000h|
|40h - 5Ch|Key Response (KEYRESP0 - KEYRESP7)|32|RW|0000_0000h|
|70h|User Identification 0 (UID0)|32|RO|0000_0000h|
|74h|User Identification 1 (UID1)|32|RO|0000_0000h|
|80h|Debug Enable Control (DBGENCTRL)|32|RW|See<br>description|
|90h|Reset Control (SDAAPRSTCTRL)|32|RW|0E00_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4580 / 4640 

NXP Semiconductors 

Debug Subsystem 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|A0h|SDA_AP Generic Status (SDAAPGENSTATUS0)|32|RO|0000_0000h|
|A4h|Generic Control 0 (SDAAPGENCTRL0)|32|RW|0000_0000h|
|B0h|SDA_AP Generic Status (SDAAPGENSTATUS1)|32|RO|0000_0000h|
|C0h|SDA_AP Generic Status (SDAAPGENSTATUS2)|32|RO|0000_0000h|
|D0h|SDA_AP Generic Status (SDAAPGENSTATUS3)|32|RO|0000_0000h|
|E0h|SDA_AP Generic Status (SDAAPGENSTATUS4)|32|RO|0000_0000h|
|FCh|Identity (ID)|32|RO|001C_0040h|



### 79.16.2 Authentication Status (AUTHSTTS) 

##### Offset 

|Register|Offset|
|---|---|
|AUTHSTTS|0h|



##### Function 

Indicates the status of the authentication process. 

##### Diagram 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Debug/079_Debug_Subsystem/S32K3XXRM_数据表.pdf-4581-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv APPD<br>R Reserved<br>ed  BGEN<br>W<br>Reset 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>SWAP UIDST Reserv CHAL<br>R Reserved<br>PDBG  AT... ed  RDY<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4581 / 4640 

NXP Semiconductors 

Debug Subsystem 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|30<br>APPDBGEN|Application Debug Enabled or Disabled<br>Indicates:<br>• The status of application debug<br>• Whether CR is satisfied<br>• Whether access to other APs is allowed<br>0b - Application debug disabled<br>1b - Application debug enabled|
|29-4<br>—|Reserved|
|3<br>SWAPPDBG|Software Application Debug<br>Indicates:<br>• The status of software application debug<br>• Whether access to debug controls is allowed<br>0b - Software application debug disabled<br>1b - Software application debug enabled|
|2<br>UIDSTATUS|User Identification Status<br>Indicates:<br>• The status of UID<br>• Whether DCM has finished reading the flash memory user section<br>0b - UID is not ready and is invalid<br>1b - UID is ready and is valid|
|1<br>—|Reserved|
|0<br>CHALRDY|Challenge Ready<br>Indicates:<br>• The status of challenge ready when the value of export control is 0<br>• The status of the DCM_DONE signal if the value of export control is 1<br>0b - Challenge is not ready<br>1b - Challenge is ready|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4582 / 4640 

NXP Semiconductors 

Debug Subsystem 

### 79.16.3 Authentication Control (AUTHCTL) 

##### Offset 

|Register|Offset|
|---|---|
|AUTHCTL|4h|



##### Function 

Controls the authentication process. 

##### Diagram 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Debug/079_Debug_Subsystem/S32K3XXRM_数据表.pdf-4583-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved  HSEN HSEA<br>W EWD... UTH...<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-2|Reserved|
|—||
|1|New Data Control|
|HSENEWDATA<br>CTL|Indicates that the debugger has consumed the data registers. It is alright for the core to provide new<br>data.|
||0b - Does not indicate that the debugger has consumed the data registers<br>1b - Indicates that the debugger has consumed the data registers|
|0|Debug Enablement Authentication Request|
|HSEAUTHREQ|Indicates that all key values are written and the chip can start the authentication request.<br>0b - Does not start the authentication request|
||1b - Starts the authentication request|



### 79.16.4 Key Challenge (KEYCHAL0 - KEYCHAL7) 

##### Offset 

For a = 0 to 7: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4583 / 4640 

NXP Semiconductors 

Debug Subsystem 

|Register<br>KEYCHALa|Offset<br>10h + (a × 4h)|
|---|---|



##### Diagram 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Debug/079_Debug_Subsystem/S32K3XXRM_数据表.pdf-4584-04.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R KEYCHAL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R KEYCHAL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Debug Enablement Key Challenge|
|KEYCHAL||



### 79.16.5 Key Response (KEYRESP0 - KEYRESP7) 

##### Offset 

For a = 0 to 7: 

|Register|||Of|fset|||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|KEYRE|SPa||40|h + (a|× 4h)||||||||||||
|Diagram<br>Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|R<br>W||||||||KEY|RESP||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||KEY|RESP||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Diagram 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4584 / 4640 

NXP Semiconductors 

Debug Subsystem 

##### Fields 

|Field|Function|
|---|---|
|31-0|Debug Enablement Key Response|
|KEYRESP||



### 79.16.6 User Identification 0 (UID0) 

##### Offset 

|Registe|r|||Offset|||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|UID0||||70h|||||||||||||
|Diagram<br>Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|R||||||||UI|D0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||UI|D0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Diagram 

##### Fields 

|Field|Function|
|---|---|
|31-0|User ID 0|
|UID0|Indicates the JTAG user ID bits of the lower word.|



### 79.16.7 User Identification 1 (UID1) 

##### Offset 

|Register|Offset|
|---|---|
|UID1|74h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4585 / 4640 

NXP Semiconductors 

Debug Subsystem 

##### Diagram 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Debug/079_Debug_Subsystem/S32K3XXRM_数据表.pdf-4586-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R UID1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R UID1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|User ID 1|
|UID1|Indicates the JTAG user ID bits of the upper word.|



### 79.16.8 Debug Enable Control (DBGENCTRL) 

##### Offset 

|Register|Offset|
|---|---|
|DBGENCTRL|80h|



##### Function 

Includes a special protection that allows access from Cortex-M0+ only if bit 30 of Authentication Status (AUTHSTTS) is 1. 

##### Diagram 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Debug/079_Debug_Subsystem/S32K3XXRM_数据表.pdf-4586-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R CNIDE CDBG<br>Reserved  Reserved<br>W N  EN<br>Reset<br>u u u u u u u u u u u u u u u u<br>1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R GSPNI GSPID GNIDE GDBG<br>Reserved  Reserved<br>W DEN  EN  N  EN<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

1. The reset value is controlled by an export control enable input. If export control is enabled, the reset value of this register is FFFF_FFF0h. Otherwise, it is 0000_0000h. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4586 / 4640 

NXP Semiconductors 

Debug Subsystem 

##### Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29<br>CNIDEN|Core Non-Invasive Debug Enable<br>Controls CNIDEN of debug blocks coupled with the Cortex-M7 core.<br>0b - Disabled<br>1b - Enabled|
|28<br>CDBGEN|Core Debug Enable<br>Controls CDBGEN of debug blocks coupled with the Cortex-M7 core.<br>0b - Disabled<br>1b - Enabled|
|27-8<br>—|Reserved|
|7<br>GSPNIDEN|Global Secure Privileged Non-Invasive Debug Enable<br>Controls GSPNIDEN of debug blocks coupled with Cortex-M7's subsystems, ETM, ITM, and CTI.<br>0b - Disabled<br>1b - Enabled|
|6<br>GSPIDEN|Global Secure Privileged Debug Enable<br>Controls GSPIDEN of debug blocks coupled with Cortex-M7's subsystems, ETM, ITM, and CTI.<br>0b - Disabled<br>1b - Enabled|
|5<br>GNIDEN|Global Non-Invasive Debug Enable<br>Controls GNIDEN of debug blocks coupled with Cortex-M7's subsystems, ETM, ITM, and CTI.<br>0b - Disabled<br>1b - Enabled|
|4<br>GDBGEN|Global Debug Enable<br>Controls GDBGEN of debug blocks coupled with Cortex-M7's subsystems, ETM, ITM, and CTI.<br>0b - Disabled<br>1b - Enabled|
|3-0<br>—|Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4587 / 4640 

NXP Semiconductors 

Debug Subsystem 

### 79.16.9 Reset Control (SDAAPRSTCTRL) 

##### Offset 

|Register|Offset|
|---|---|
|SDAAPRSTCTRL|90h|



##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||Rese|rved||RSTR<br>ELT...|RSTR<br>ELT...|RSTR<br>ELT...|||||Reserved|||||
|Reset|0|0|0|0|1|1|1|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||Rese|rved||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-28<br>—|Reserved|
|27|Reset Release Cortex-M7_2|
|RSTRELTLCM7<br>2|Indicates if the control signal released the reset for Cortex-M7_2. The reset is released to debug the core<br>from first instruction.<br>The default value of this field is 1.<br>0b - Core is in reset<br>1b - Reset is released|
|26<br>RSTRELTLCM7<br>1|Reset Release Cortex-M7_1<br>Indicates if the control signal released the reset for Cortex-M7_1. The reset is released to debug the core<br>from first instruction.<br>The default value of this field is 1.<br>0b - Core is in reset<br>1b - Reset is released|
|25|Reset Release Cortex-M7_0|
|RSTRELTLCM7<br>0|Indicates if the control signal released the reset for Cortex-M7_0. The reset is released to debug the core<br>from the first instruction.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4588 / 4640 

NXP Semiconductors 

Debug Subsystem 

Table continued from the previous page... 

|Field|Function|
|---|---|
||The default value of this field is 1.|
||0b - Core is in reset|
||1b - Reset is released|
|24-0<br>—|Reserved|



### 79.16.10 SDA_AP Generic Status (SDAAPGENSTATUS0 - SDAAPGENSTATUS4) 

##### Offset 

|Register|Offset|
|---|---|
|SDAAPGENSTATUS0|A0h|
|SDAAPGENSTATUS1|B0h|
|SDAAPGENSTATUS2|C0h|
|SDAAPGENSTATUS3|D0h|
|SDAAPGENSTATUS4|E0h|



##### Diagram 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Debug/079_Debug_Subsystem/S32K3XXRM_数据表.pdf-4589-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R SDAAPGENSTATUS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R SDAAPGENSTATUS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|DAP Generic Status|
|SDAAPGENST<br>ATUS|Is a generic status field for future use.<br>0b - Does not show generic status|
||1b - Shows generic status|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4589 / 4640 

NXP Semiconductors 

Debug Subsystem 

### 79.16.11 Generic Control 0 (SDAAPGENCTRL0) 

##### Offset 

|Register|Offset|
|---|---|
|SDAAPGENCTRL0|A4h|



##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||Rese|rved||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||Reserved||||||||JTAG_<br>CR...|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-1|Reserved|
|—||
|0|JTAG CR Enable|
|JTAG_CR_EN|Performs CR or password comparison based on SWJ-DP mode or JTAG mode. If you write 1 to this<br>field, this function is performed using JTAG irrespective of SWJ-DP mode of the debugger.|
||0b - Function performed on the basis of SWJ-DP mode|
||1b - Function performed on the basis of JTAG mode|



### 79.16.12 Identity (ID) 

##### Offset 

|Register|Offset|
|---|---|
|ID|FCh|



##### Function 

~~<mark>NOTE</mark>~~ 

This register does not generate the bus error on performing the write operation. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4590 / 4640 

NXP Semiconductors 

Debug Subsystem 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||ID|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|1|1|1|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||ID|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|1|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-0|Identity|
|ID||



## 79.17 Glossary 

|AHB|Advanced high-performance bus|
|---|---|
|AHB_AP|Advanced high-performance bus access port|
|APB|Advanced peripheral bus|
|APB_AP|Advanced peripheral bus access port|
|ATB|Advanced trace bus|
|ATBR|ATB replicator|
|CSTF|CoreSight trace funnel|
|DAP|Debug access port|
|DC|Design center|
|ETF|Embedded CoreSight funnels|
|JTAG-DP|JTAG debug port|
|MDM_AP|Miscellaneous debug module access port|
|MIC|Manufacturer identity code|
|PIN|Part identification number|
|PRN|Part revision number|
|SDA_AP|Serial data access port|
|SiP|System-in-package|
|SWJ-DP|Serial wire/JTAG debug port|
|TAP|Test and debug access port|
|TPIU|Trace port interface unit|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4591 / 4640 

NXP Semiconductors 

Debug Subsystem 

## 79.18 References 

- Arm CoreSight SoC-400 Technical Reference Manual 

https://static.docs.arm.com/100536/0302/coresight_soc400_technical_reference_manual_100536_0302_01_en.pdf 

- Arm CoreSight Architecture Specification 

http://infocenter.arm.com/help/topic/com.arm.doc.ihi0029d/IHI0029D_coresight_architecture_spec_v2_0.pdf 

- CoreSight Components Technical Reference Manual 

http://infocenter.arm.com/help/topic/com.arm.doc.ddi0314h/DDI0314H_coresight_components_trm.pdf 

- Arm Debug Interface Architecture Specification 

https://static.docs.arm.com/ihi0031/c/IHI0031C_debug_interface_as.pdf 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4592 / 4640 

