NXP Semiconductors 

# Chapter 5 Cortex-M7 Overview 

## 5.1 Introduction 

Cortex-M7 is a high-performance embedded processor intended for deeply embedded applications that require fast interrupt response features. The configuration of the processor is based on little-endian format, and you must compile the execution testbench tests in this format too. 

Table 26. Cortex-M7 instances 

|Instances|S32K338|S32K358|S32K328/<br>S32K324/S32K322|S32K348/S32K344/S32K342/S32K341/<br>S32K314/S32K312/S32K311|
|---|---|---|---|---|
|CM7_0|Yes|Yes|Yes|Yes|
|CM7_1|Yes|No|Yes|No|
|CM7_2|Yes|Yes|No|No|



### 5.1.1 Features 

Cortex-M7 provides: 

- Low interrupt latency 

- Low-cost debug 

- Backwards compatibility with existing Cortex-M profile processors 

- In-order superscalar pipeline 

- Dual-issue support for load/load and load/store instruction pairs to multiple memory interfaces 

- An MPU that you could configure to protect regions of memory 

- A NVIC 

- A debug and trace unit (CoreSight components) 

- Floating-point arithmetic functionality, with support for single-precision arithmetic 

- The ability to perform speculative load from any Normal type memory space through its AXIM bus, if D-cache is enabled 

- Several memory interfaces that include: 

   - Harvard architecture-based instruction and data caches, and an AXIM interface 

   - A dedicated low-latency AHBP interface 

   - A 64-bit AXI AMBA4 memory interface with a 16 KB instruction cache and a 16 KB data cache for efficient access to external resources. The instruction and data caches are ECC protected. 

   - A 32-bit AHBS for interfacing with slaves such as DMA 

   - 64-bit and 32-bit memory interfaces for the connection to local Tightly Coupled Memories called ITCM and DTCM. Each Cortex-M7 core interfaces with low-latency 32 KB ITCM, 32 KB DTCM0 and 32KB DTCM1 for CM7_0/1 and 64 KB ITCM, 64 KB DTCM0 and 64 KB DTCM1 for CM7_2 

### 5.1.2 Related information 

For detailed information on: 

- Cortex-M7 processor, see Arm Cortex-M7 Processor Technical Reference Manual. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

42 / 4640 

NXP Semiconductors 

Cortex-M7 Overview 

- Cortex-M7 peripherals and control, see Arm Cortex-M7 Devices Generic User Guide. 

- System memory map, see the memory map file attached to this document. 

### 5.1.3 Buses, interconnects, and interfaces 

This table discusses Cortex-M7 buses and their associated interconnects and interfaces. 

Table 27. Buses and associated information 

|Bus name|Description|
|---|---|
|AXIM|Using the XHB400 module, this bus is first translated to the AHB-Lite bus that interfaces<br>with the AXBS crossbar switch providing high-bandwidth access to on-chip memories and<br>peripherals.|
|AHBP|This bus connects to the AXBS crossbar switch providing high-bandwidth access to on-chip<br>peripherals.|
|PPB|This bus provides access to these modules:|
||• Arm modules such as NVIC,ETM,ITM,DWT, and ROM tables<br>• Miscellaneous Control Module (MCM)|



~~<mark>NOTE</mark>~~ 

S32K3xx AHBP bus is enabled after reset. Therefore, accesses of all cores to on-chip peripherals are performed exclusively through this bus. 

### 5.1.4 Core configuration 

This table describes Cortex-M7 parameter settings. 

Table 28. Core configuration 

|Parameter|Configuration<sup>1</sup>|
|---|---|
|FPU|Single precision|
|DSP extension instructions|• Single cycle 16/32-bitMAC<br>• Single cycle dual 16-bit MAC<br>• 8/16-bitSIMDarithmetic<br>• Hardware divide (2-12 cycles)|
|Armv8-M security extensions|Not implemented|
|I-cache|Implemented|
|D-cache|Implemented|
|Caches ECC|Implemented|
|On core MPU region|16|
|Number of IRQs|240|
|IRQ priority width configuration|4 (16 interrupt priority levels)|
|Debug (breakpoint/watchpoint)|Full comparator set: 4 DWT and 8FPBcomparators|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

43 / 4640 

NXP Semiconductors 

Cortex-M7 Overview 

Table 28. Core configuration (continued) 

|Parameter|Configuration<sup>1</sup>|
|---|---|
|Internal trace support|ITM and DWT trace functionality implemented|
|ETM support|Instruction and data ETM interface implemented|
|CTI|Implemented|
|WIC support|Not implemented|
|Dual-redundant core (lock-step) CPU functionality|Not implemented<sup>2</sup>|
|RAR|All asynchronously reset|
|I-cache size|16 KB|
|D-cache size|16 KB|
|ITCM|32 KB for CM7_0/1, 64 KB for CM7_2|
|DTCM0|32 KB for CM7_0/1, 64 KB for CM7_2|
|DTCM1|32 KB for CM7_0/1, 64 KB for CM7_2|



1. Armv7-M (Harvard architecture), six-stage superscalar plus branch prediction 

2. Two different Cortex-M7 cores are used physically in the S32K342, S32K344, S32K348, and S32K358 chips (dual Cortex-M7 lock-step parts) 

## 5.2 Speculative accesses 

The Arm Cortex M7 processor can issue speculative read accesses that may access any location within the complete memory address range. This behavior can be controlled, but not disabled. Corresponding effects must be considered for a proper operation of your system. 

Speculative accesses do not cause any processor faults. The processor is aware whether an access is speculative, and ignores any error response signaled by the system due to the speculative access. However, the system that is integrating the processor cannot distinguish speculative accesses from non-speculative accesses. 

Addresses used by speculative accesses are not validated against the memory map of the device, and may attempt to also access non-existing memory regions or hardware elements having side effects. For details about corresponding behavior of the Arm Cortex M7 processor see Related information. Important processing aspects are listed in section “Memory Model” within the Generic User Guide. 

Speculative accesses can result in improved performance when the related memory regions are properly characterized. It is imperative to properly setup the attributes within the Memory Protection Unit (MPU) to avoid any unwanted impact of a speculative access. Examples for possible, corresponding issues are usually the result of side effects unknown to the processor: 

- Speculative access to an uninitialized RAM memory location that causes a double bit error {the related fault processing by the FCCU is performed independently from the processor}. 

- Speculative access to a peripheral that causes an unwanted operation; for example, a FIFO read {the corresponding data may be removed from the FIFO without being processed}. 

- Speculative access to a peripheral that is not clocked, powered down, or cannot respond {the access may not be terminated, resulting an access that is stalled, system blockage}. 

- Speculative access to an address range that causes an unexpected error being reported; for example, a read-while-write error of the embedded flash (indicated by setting MCRS[RWE]) during a flash erase or program operation {which may hide real errors}. 

Speculative accesses can be controlled by a proper assignment of memory regions within the MPU: 

- Speculative instruction fetches are never made to memory addresses in an Execute Never region. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

44 / 4640 

NXP Semiconductors 

Cortex-M7 Overview 

- Speculative data reads are never made to memory addresses marked as non-accessible in the MPU. 

- Speculative cache line-fills are never made to non-cacheable memory addresses. 

- Speculative data reads and speculative cache line-fills are never made to memory addresses in a region having a Device or Strongly-ordered attribute. 

- Speculative reads are never made on the AHBP interface. 

- Speculative writes are never made. 

Memory regions mapped to a TCM are always treated as Normal Memory (equivalent to the MPU attribute) and are therefore always subject to speculation. Related issues can be avoided by properly initializing any TCM memory before a corresponding access may occur. 

When no speculative accesses should be initiated to a memory region, it is recommended to set all of the following attributes within the MPU for this region: Device or Strongly-ordered, and Execute Never. These attributes are often also used for address ranges associated with peripherals. 

Unwanted processing of side effects caused by a speculative access can also be inhibited by disabling the related events while a speculative access may occur. As an example, the FCCU can be enabled after the ECC of the RAM memories has been initialized. As a second example, read accesses to a Flash block can be inhibited by configuring an MPU region while it is being erased. 

## 5.3 Debug facilities 

This chip has extensive debug capabilities such as run control and tracing. It includes the standard Arm debug port that supports the JTAG and SWD interfaces. 

## 5.4 Vector fetch behavior on Cortex-M7 

In Cortex-M7, the vector fetches are looked up into the I-Cache. if the vector table is located in a region of memory that is cacheable, any load or store to the vector must be treated as self-modifying code and cache maintenance instructions should be used to synchronize the updates to the data and instruction caches. The Cortex-M7 Device Generic User Guide chapter 'Cache maintenance design hints and tips' specifies a recommendation for synchronization of the D-Cache and I-Cache. 

If cache maintenance is to be avoided each time when the vector table gets updated, then the vector table must be allocated in the ITCM or DTCM, as those are non-cacheable regions. Alternatively, the I-Cache must be enabled after the vector table has been initialized. 

## 5.5 TCM retry 

TCM retry is disabled and software should disable the TCM retry bit at startup by programming the relevant core's CM7_ITCMCR[RETEN] and CM7_DTCMR[RETEN] fields to disable state. 

## 5.6 Glossary 

AHBP AHB-lite peripheral AHBS AHB-slave port AXIM Advanced extensible interface master DWT Data watchpoint and trace unit ETM Embedded trace macrocell FPU Floating point unit FPB Flash patch and breakpoint ITM Instrumentation trace macrocell MAC Multiplier accumulator (refers to a multiplier accumulator unit as well as multiplier accumulator operation) 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

45 / 4640 

NXP Semiconductors 

Cortex-M7 Overview 

NVIC Nested vectored interrupt controller RCCU Redundancy control checking unit RAR Reset-all-registers SIMD Single instruction multiple data 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

46 / 4640 

