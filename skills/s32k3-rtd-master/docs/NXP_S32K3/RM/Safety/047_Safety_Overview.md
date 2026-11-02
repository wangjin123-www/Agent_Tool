NXP Semiconductors 

# Chapter 47 Safety Overview 

## 47.1 Introduction 

This chip family is developed following the ISO 26262 standards, with derivatives targeting the chips that are operable in a system that fulfills the requirements of the ASIL D or ASIL B safety integrity levels. 

Table 230. ASIL levels 

|Chip<br>ASIL level|
|---|
|S32K344<br>D|
|S32K342|
|S32K358|
|S32K312<br>B|
|S32K311|



The ASIL level targets the safety processing, which means the software functions are executed as intended: 

1. Read instructions from memory. 

2. Execute instructions. 

3. Read data from memory. 

4. Process data. 

5. Write back the result data into memory. 

Some elements of the safety concept are based on the assumption that the chip is connected to an external SBC or PMIC. The SBC or PMIC performs observations and control functionalities that are essential to fulfill some related functional safety requirements. If you do not use an SBC or PMIC, you must ensure that your S32K-family chip provides an equivalent functionality that properly manages the corresponding interface(s). 

The following figure illustrates the safety interface between the chip and the SBC or PMIC. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1597 / 4640 

NXP Semiconductors 

Safety Overview 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/047_Safety_Overview/S32K3XXRM_数据表.pdf-1598-02.png)


<!-- Start of picture text -->
Safety<br>Chip<br>interface<br>Power supply<br>(VDD_HV_A, VDD_HV_B, Internal PMC:<br>Voltage regulator V1.5V) Internal voltage<br>VDD output generation: 1.1 V, 2.5 V,<br>redundant LVDs,<br>and single HVDs<br>SPI communication<br>External watchdog Software-driven SPI communication<br>RESET_b (bidirectional)<br>MC_RGM<br>1) External reset source<br>2) Output to external subsystem<br>FCCU monitoring FCCU drives the EOUT pads<br>FCCU_0 FCCU_0 actively during functional reset if<br>Internal chip safe state 1) dcf_client_utest_misc<br>FCCU_1 FCCU_1 [FCCU_EOUT_DEDICATED]<br>2) SW CONFIG (FCCU-CFG)<br>aaa-038719<br><!-- End of picture text -->

Figure 179. Safety interface between the chip and the SBC or PMIC 

In the safety context, the chip interfaces can be classified into the groups shown in the table. 

Table 231. Chip interface groups 

|Interface|Description|
|---|---|
|Power supply|This interface is between the SBC and the chip. It ensures<br>that the supply to the chip is in the correct range. In case<br>of any low-voltage event, the chip has POR, LVR, and LVD<br>circuits in place and in case of any HVD event, the chip<br>raises an interrupt. The SBC must ensure that the voltage<br>regulator outputs never exceed the allowed range (more<br>specifically for HVD range).|
|Communication|Responsible for communication between the SBC and the<br>chip. Though the chip supports multiple communication<br>protocols (UART, LIN, SPI, I2C, FlexCAN, and so on), SPI<br>is the preferred communication with SBC. This is relevant to<br>initialize an external watchdog when the chip is inoperative<br>for a considerably long time (this is indicated by the pin states<br>of the communication interface).|
|Reset|The chip consists of a reset bidirectional pin interfaced with<br>SBC. The SBC can initiate a chip reset via this pin as a<br>safety reaction in case of:<br>• Extreme critical faults<br>• An inoperative chip<br>• Stuck cases based on the criticality and the application<br>requirements|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1598 / 4640 

NXP Semiconductors 

Safety Overview 

Table 231. Chip interface groups (continued) 

||Interface|Description|
|---|---|---|
|||The SBC also samples the reset pin state to identify the chip<br>condition (whether in running state or in reset).|
|FCCU||The chip indicates the chip faults to the SBC via FCCU<br>EOUT pins through this interface.|



The interfaces in Table 231 ensure the chip's operational safety and integrity. 

## 47.2 Safety architecture elements 

The chip safety architecture consists of following elements that operate in an interconnected way to meet the ASIL requirements: 

- Cortex-M7 core complex (including the cache controllers) operating in delayed lockstep (ASIL D only) 

- eDMA controller 

- Structural core self-test 

- Internal windowed watchdogs with independent clock sources 

- Power supply monitoring with redundant low-voltage detectors, single high-voltage detectors, and internal ADC connection to check the internal voltages during application 

- Robust clock monitoring, including PLL loss of lock detection 

- Embedded flash memory with ECC (single-bit data correction, double-bit data detection) and address encoding (parallel address path check) 

- System RAM with ECC 

   - Single-bit data correction 

   - Double-bit data detection 

   - Address detection 

- Cortex-M7 cache memories with ECC (single-bit data correction, double-bit data detection) 

- Peripherals memories (EMAC, FlexCAN) with ECC (single-bit data correction, double-bit data detection) 

- End-to-End EDC (E2E EDC), with address encoding and monitoring of the control signals done by a dedicated module (XBIC). This ensures the safety of storage and of the data path to the internal storage (RAM, flash memory, core cache) and peripherals across the crossbar switch. See the XBIC chapter for details. 

- Hardware CRC module that supports end-to-end data check integrity for any data transfer in the system (SRAM to peripherals via DMA transfer, external interfaces to SRAM/peripherals, and so on) 

- Cortex-M7 MPUs 

- XRDC for memory and peripheral protection 

- AIPS_Lite peripheral protection with trusted master-slave connection 

- Register protection mechanism for safety-critical registers 

- On-chip temperature sensor for temperature monitoring 

- Self-test: 

   - LBIST to detect latent faults in functional logic as well as in safety integrity mechanisms 

~~<mark>NOTE</mark>~~ 

LBIST is not supported in S32K312 and S32K311. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1599 / 4640 

NXP Semiconductors 

Safety Overview 

   - MBIST to ensure integrity of the memories in the chip (SRAM, ITCM, DTCM, peripheral memories, and so on) 

   - Check-the-checker software library 

   - ADC self-test 

- FCCU for error collection and reaction, including reporting error status to system; FCCU supports these programmable reaction types: 

   - Interrupt 

   - Functional reset 

- Error pads indicate the chip's internal state to the external chip interface or SBC. 

- EIM to inject errors into the memories and interface gaskets to verify the error-detection features of the memory controllers and the interface gaskets 

- ERM to collect diagnostic information from memory controllers in case of an error event 

## 47.3 I/O peripherals 

The arrangement of I/O peripherals across peripheral bridges allows redundant use of peripherals while limiting possible causes of CCF. Redundant use includes using equivalent peripherals in a replicated way as well as using functionally different peripherals in, for example, feedback measurement loops. Comparison of redundant operation is the responsibility of the application software, not the safety hardware mechanism. 

The peripherals are distributed evenly across the peripheral bridges (AIPSn), except for singular modules like EMAC, QuadSPI, and so on. 

~~<mark>NOTE</mark>~~ 

EMAC and QuadSPI are not present in S32K312 and S32K311. 

## 47.4 Self-test 

The chip supports a self-test operation. Your safety software must initiate self-test by configuring STCU2; the chip does not initiate it. STCU2 then controls the self-test operation. Self-test supports both MBIST and LBIST. After the self-test operation completes, the chip enters a reset sequence. Self-test results are stored in STCU2 and your safety software can read the results after the reset sequence. 

Figure 180 depicts the processing steps related to the self-test operation, and its linkage to the chip reset and an application start. You decide whether to run a self-test or to skip it before starting an application. You must also specify the self-test configuration before relinquishing control to STCU2 for performing the self-test operation. This processing finishes by reentering the chip reset sequence, depending on whether the chip encountered an unrecoverable fault during the self-test operation. When an unrecoverable fault is encountered during the self-test operation, the chip enters a reset sequence by performing a destructive reset. When no such fault is encountered, the self-test operation completes by entering the chip sequence with a functional reset sequence. You can prevent reset cycling by limiting the amount of resets permitted; the chip shuts down when this limit has been reached. See the "Functional reset escalation" and "Destructive reset escalation" sections in the MC_RGM chapter. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1600 / 4640 

NXP Semiconductors 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/047_Safety_Overview/S32K3XXRM_数据表.pdf-1601-01.png)


<!-- Start of picture text -->
Safety Overview<br>Power-on reset<br>Chip reset sequence<br>Destructive reset<br>STCU2 encounters an unrecoverable fault and sequence<br>generates a destructive reset.<br>Functional reset<br>sequence Self-test completion results in a functional reset.<br>Out of reset<br>Yes<br>Too many resets? Chip shutdown<br>No<br>Software reads STCU2<br>and MC_RGM registers.<br>Is previous reset Yes Software checks the<br>due to self-test? LBIST or MBIST results<br>No<br>STCU2 is under destructive reset.<br>The self-test configurations and the results Software decides: No Software starts application<br>(assuming self-test execution was successful) run the self-test? execution<br>remains preserved across self-test within STCU2.<br>Yes<br>Software configures STCU2<br>for self-test execution.<br>STCU2 exectutes<br>LBIST or MBIST<br>Does STCU2<br>Yes encounter any No<br>unrecoverable<br>fault?<br>Figure 180. LBIST/MBIST execution<br><!-- End of picture text -->

Figure 181 visualizes the top-level partitioning of the chip. The chip consists of two partitions, Run and Standby. 

- Run: This partition consists of logic which is present in switchable domain and is shut off (has no supply) while the chip operates in low-power (Standby) mode. 

- Standby: This partition consists of always-on logic which is functional even while the chip operates In low-power (Standby) mode. 

The Run partition also contains the control logic that is essential for the chip self-test operation, as well as blocks that undergo self-test. The chip consists of a single LBIST partition, which is a subpartition within the Run partition. The LBIST subpartition 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1601 / 4640 

NXP Semiconductors 

Safety Overview 

contains the logic over which self-test is executed. The logic outside the LBIST subpartition and within the Run partition consists of the LBIST control logic as well as logic which does not undergo LBIST. 

The components within these different partitions are listed below the figure (they are not indicated in the figure for clarity). 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/047_Safety_Overview/S32K3XXRM_数据表.pdf-1602-04.png)


<!-- Start of picture text -->
Run<br>LBIST<br>Standby<br><!-- End of picture text -->

Figure 181. S32K314/S32K324/S32K344 chip top-level partition view 

The following list specifies the content of the LBIST partition and both power domains related to their participation in the self-test operation: 

- Modules participating in the LBIST operation: 

~~<mark>NOTE</mark>~~ 

LBIST is not supported in S32K312 and S32K311. The modules participating in the LBIST operation are out of LBIST in S32K312 and S32K311. 

— eDMA 

- EIM 

- — ERM 

- XRDC 

   - ◦MDAC0 (Cortex-M7_0) ◦MDAC1 (eDMA) ◦MDAC2 (reserved) ◦MDAC3 (HSE_B) ◦MDAC4 (Cortex-M7_1) ◦MDAC5 (EMAC) ◦MRC0 (flash memory) ◦MRC1 (PRAM) ◦MRC2 (QuadSPI) 

~~<mark>NOTE</mark>~~ Cortex-M7, EMAC, and QuadSPI are not present in S32K312 and S32K311. 

◦PDAC1 

◦PDAC2 

- CRC 

- FCCU 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1602 / 4640 

NXP Semiconductors 

Safety Overview 

- FOSU 

- PFLASH_CTL 

- PRAM_C0 

- PRAM_C1 

- SWT_1 

- CMU 

   - ◦CMU_FC_0 

   - ◦CMU_FM_1 

   - ◦CMU_FM_2 

   - ◦CMU_FC_3 

   - ◦CMU_FC_4 

   - ◦CMU_FC_5 

- IAHB gaskets 

~~<mark>NOTE</mark>~~ 

An IAHB gasket is a frequency translation gasket in the system. These gaskets are used to add register walls and synchronize the timing domain across different operating frequencies. See the configurable gaskets in the 'Block diagram' in 'Introduction' chapter for the locations of the IAHB_GASKETs in the chip. 

- ◦DMA_GSKT 

- ◦HSE_GSKT 

- ◦AIPS1_GSKT 

- ◦AIPS2_GSKT 

- ◦QSPI_GSKT 

~~<mark>NOTE</mark>~~ 

AIPS2_GSKT and QSPI_GSKT are not present in S32K312 and S32K311. 

   - ◦TCM_GSKT 

   - ◦EMAC_GSKT 

   - ◦EDC master checker gaskets (See block diagram in Introduction chapter for details) 

   - ◦EDC slave checker gasket (See block diagram in Introduction chapter for details) 

- Crossbar switches and bridges 

   - ◦AXBS_0 (main) 

   - ◦AXBS_1 (peripheral) 

   - ◦AXBS_2 (eDMA) 

   - ◦AXBS_3 (Cortex-M7 TCM) 

   - ◦AXBS_4 (HSE) 

   - ◦AIPS_Lite_1 

   - ◦AIPS_Lite_2 

AIPS2_Lite_ is not present in S32K312 and S32K311. 

~~<mark>NOTE</mark>~~ 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1603 / 4640 

NXP Semiconductors 

Safety Overview 

- Modules within the Standby domain (not participating in the LBIST operation): 

   - 32 KB standby SRAM 

— LPCMP_0–LPCMP_2 — Reset generation ◦MC_RGM ◦POR_WDG — Power management ◦PMC ◦MC_PCU ◦WKPU ◦Chip standby pins — Clock sources ◦FIRC ◦SIRC ◦FXOSC ◦SXOSC 

~~<mark>NOTE</mark>~~ SXOSC is not present in S32K311. 

— Timers ◦PIT_0 ◦RTC ◦SWT_0 

- Modules not participating in the LBIST operation (in the Run domain): 

   - HSE subsystem 

◦Engine ◦Memories — Cortex-M7_0 ◦Core ◦I-cache ◦D-cache ◦ ITCM 

◦ DTCM 

- Cortex-M7_1 

~~<mark>NOTE</mark>~~ 

Cortex-M7_1 is not present in S32K312 and S32K311. 

◦Core 

◦I-cache 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1604 / 4640 

NXP Semiconductors 

Safety Overview 

   - ◦D-cache ◦ITCM 

   - ◦DTCM 

- CMUs 

   - ◦CMU0 

   - ◦CMU3 

- Analog blocks 

   - ◦ADC_0–ADC_2 

   - ◦TempSense 

~~<mark>NOTE</mark>~~ 

ADC_2 is not present in S32K342, S32K312, and S32K311. 

- Communication modules 

   - ◦LPSPI_0–LPSPI_5 

   - ◦LPI2C_0 

   - ◦LPI2C_1 

   - ◦LPUART_0–LPUART_15 

   - ◦FlexCAN_0–FlexCAN_5 

   - ◦SAI_0 

   - ◦SAI_1 

~~<mark>NOTE</mark>~~ 

SAI_0 and SAI_1 are not present in S32K312 and S32K311. 

- Timers 

   - ◦PIT_1 

   - ◦PIT_2 ◦eMIOS 

   - ◦BCTU 

   - ◦STM_0 

   - ◦STM_1 

~~<mark>NOTE</mark>~~ 

PIT_2 and STM_1 are not present in S32K312 and S32K311. 

- TRGMUX 

- PLLDIG 

- SIUL2 

- LCU_0 

- LCU_1 

- STCU2 

- DMAMUX 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1605 / 4640 

NXP Semiconductors 

Safety Overview 

- MCM 

- MCSM 

- INTM 

- SEMA42 

- MU 

~~<mark>NOTE</mark>~~ 

SEMA42 and chip MU are not present in S32K312 and S32K311. 

- TSPC 

~~<mark>NOTE</mark>~~ 

REG_PROT of an IP undergoes (or does not undergo) LBIST in conjunction with the protected module that undergoes (or does not undergo) LBIST. 

The modules that are vital to the self-test operation are excluded from LBIST regions to allow LBIST to execute successfully. 

You must run self-test with PLLDIG configured as the system clock. The LBIST clock controller controls the clock during serial shift, but returns clock control to the functional nodes during the self-test. 

## 47.5 Glossary 

ASIL Automotive safety integrity level. This is a risk classification scheme as defined by ISO 26262 for automotive standard. 

CCF Common cause failure 

DTCM Data tightly coupled memory 

ECC Error correction code 

ITCM Instruction tightly coupled memory 

LBIST Logic built-in self-test 

MBIST Memory built-in self-test 

PLL Phase-locked loop oscillator PMIC Power management integrated chip 

SBC System basis chip 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1606 / 4640 

