# S32K3XX 

### <u>S32K3xx Data Sheet</u> 

Supports S32K312, S32K344, S32K324, and S32K314. Data is preliminary for S32K311, S32K322, S32K341, S32K342, S32K328, S32K338, S32K348, S32K358. 

Rev. 4 — 04/2022 

Data Sheet: Technical Data 

- Operating characteristics 

   - Voltage range: 2.97 V to 5.5 V 

   - Ambient temperature range: -40 °C to 125 °C for all power modes 

- Arm<sup>™</sup> Cortex-M7 core, 32-bit CPU 

   - M7 supports up to 160 MHz frequency with 2.14 DMIPS / MHz 

   - Arm Core based on the Armv7 and Thumb<sup>®</sup> -2 ISA 

   - Integrated Digital Signal Processor (DSP) 

   - Configurable Nested Vectored Interrupt Controller (NVIC) 

   - Single Precision Floating Point Unit (FPU) 

- Clock interfaces 

   - 8 - 40 MHz Fast External Oscillator (FXOSC) 

   - 48 MHz Fast Internal RC oscillator (FIRC) 

   - 32 kHz Low Power Oscillator (SIRC) 

   - 32 kHz Slow External Oscillator (SXOSC) 

   - System Phased Lock Loop (SPLL) 

- I/O and package 

   - LQFP48, MAXQFP100, MAXQFP172, MAPBGA257, MAPBGA289, MaxQFP172 with Exposed pad (EP) package options 

- Memory and memory interfaces 

   - Up to 8 MB program flash memory with ECC 

   - Up to 128 K of flexible program or data flash memory 

   - Up to 512 KB SRAM with ECC, includes 192 KB of TCM RAM ensuring maximum CPU performance of fast control loops with minimal latency 

   - Data and instruction cache for each core to minimize performance impact of memory access latencies 

   - QuadSPI support 

- Mixed-signal analog 

— Up to three 12-bit Analog-to-Digital Converters (ADC) with up to 24 channel analog inputs per module 

      - One Temperature Sensor (TempSense) 

      - Up to three Analog Comparators (CMP), with each comparator having an internal 8-bit DAC 

   - Human-Machine Interface (HMI) 

      - Up to 235 GPIO pins 

      - Non-Maskable Interrupt (NMI) 

      - Up to 60 pins with wakeup capability 

      - Up to 32 pins with interrupt support 

- Up to 32-channel DMA with up to 128 request sources using DMAMUX 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0001-38.png)


NXP reserves the right to change the detail specifications as may be required to permit improvements in the design of its products. 

NXP Semiconductors 

- Power management 

   - Low-power Arm Cortex-M7 core with excellent energy efficiency, balanced with performance 

   - Power Management Controller (PMC) with simplified mode management (RUN and STANDBY) 

   - Supports peripheral specific clock gating. Only specific peripherals remain working in low power modes. 

- Communications interfaces 

   - Up to 16 serial communication interface (LPUART) modules, with LIN, UART and DMA support 

   - Up to six Low Power Serial Peripheral Interface (LPSPI) modules with DMA support 

   - Up to two Low Power Inter-Integrated Circuit (LPI2C) modules with DMA support 

   - One Improved Inter-Integrated Circuit (I3C) module with DMA support 

   - Up to six FlexCAN modules (with optional CAN-FD support) 

   - FlexIO module for flexible and high performance serial interfaces 

   - One Ethernet module 

   - Up to two Synchronous Audio Interface (SAI) modules 

- Reliability, safety and security 

   - Hardware Security Engine (HSE_B) 

   - Up to two Internal Software Watchdog Timers (SWT) 

   - Error-Correcting Code (ECC) on all memories 

   - Debug functionality 

      - Serial Wire JTAG debug Port (SWJ-DP), with 2 pin Serial Wire Debug (SWD) for external debugger 

      - Debug Watchpoint and Trace (DWT), with four configurable comparators as hardware watchpoints 

      - Serial Wire Output (SWO)-synchronous trace data support 

      - Instrumentation Trace Macrocell (ITM) with software and hardware trace, plus time stamping 

      - CoreSight AHB Trace Macrocell (HTM) 

      - Flash Patch and Breakpoints (FPB) with ability to patch code and data from code space to system space 

      - Serial Wire Viewer (SWV): A trace capability providing displays of reads, writes, exceptions, PC Samples and print 

      - Full data trace for up to 16 output wide 

      - Embedded Cross Trigger (ECT) is used for multicore run-control and trace cross triggering, using CoreSight Cross Trigger Interface (CTI) 

   - Timing and control 

      - Up to three enhanced modular I/O system (eMIOS), offering up to 72 timer channels (IC/OC/PWM) 

      - Up to two System Timer Modules (STM) 

      - Up to two Logic Control Units (LCU) 

      - Full cross triggering support for ADC / timer (BCTU) 

      - One Trigger MUX Control (TRGMUX) module 

      - Up to three Periodic Interrupt Timer (PIT) modules 

      - 32-bit Real Time Counter (RTC) with autonomous periodic interrupt (API) function 

- Error Detection Code (EDC) on data path 

- Cyclic Redundancy Check (CRC) module 

- 120-bit Unique Identification (ID) number 

- Extended Cross domain Domain Controller (XRDC), providing protection for master core access rights 

- Virtualization Wrapper (VIRT_WRAPPER), providing I/O protection 

S32K3xx Data Sheet, Rev. 4, 04/2022 Preliminary Information 

Data Sheet: Technical Data 

2 / 130 

## Contents 

|1|Overview............................................................ 4|9.5|Flash memory read timing parameters......... 74|
|---|---|---|---|
|2|Block diagram.....................................................4|10|Analog modules................................................75|
|3|Feature comparison......................................... 10|10.1|SAR ADC...................................................... 75|
|4|Ordering information.........................................14|10.2|Supply Diagnosis.......................................... 78|
|4.1|Determining valid orderable parts ................ 14|10.3|Low Power Comparator (LPCMP)................ 78|
|5|General.............................................................14|10.4|Temperature Sensor..................................... 82|
|5.1|Absolute maximum ratings............................15|11|Clocking modules............................................. 83|
|5.2|Voltage and current operating requirements.16|11.1|FIRC..............................................................83|
|5.3|Thermal operating characteristics.................18|11.2|SIRC............................................................. 83|
|5.4|ESD and Latch-up Protection Characteristics|11.3|PLL................................................................83|
||...................................................................... 18|11.4|Fast External Oscillator (FXOSC)................. 85|
|6|Power management......................................... 19|11.5|Slow Crystal Oscillator (SXOSC).................. 86|
|6.1|Power management system - S32K344,|12|Communication interfaces................................87|
||S32K324, S32K341, S32K314, S32K342, and|12.1|LPSPI............................................................87|
||S32K322....................................................... 20|12.1.1|LPSPI............................................................87|
|6.2|Power management system - S32K312,|12.1.2|LPSPI0 20 MHz and 15 MHz Combinations. 91<br>|
||S32K311....................................................... 21|12.2|I<sup>2</sup>C.................................................................92|
|6.3|Power management system - S32K358....... 22|12.3|I3C Push-Pull Timing Parameters for SDR|
|6.4|Power mode transition operating behaviors..22||Mode............................................................. 92|
|6.4.1|Power mode transition operating behaviour. 22|12.4|FlexCAN characteristics................................94|
|6.4.2|Boot time, HSE firmware not installed.......... 23|12.5|SAI electrical specifications.......................... 94|
|6.4.3|Boot time, HSE firmware installed................ 23|12.5.1|SAI Electrical Characteristics, Slave Mode...94|
|6.4.4|HSE firmware memory verification time|12.5.2|SAI Electrical Characteristics, Master Mode.96|
||examples.......................................................24|12.6|Ethernet characteristics................................ 97|
|6.5|Supply Monitoring......................................... 29|12.6.1|Ethernet MII (100 Mbps)............................... 97|
|6.6|SMPS regulator electrical specifications.......30|12.6.2|Ethernet MII (200 Mbps)............................... 99|
|6.7|Recommended Decoupling Capacitors........ 31|12.6.3|Ethernet RMII..............................................101|
|6.8|NPN Ballast Transistor Control Specification|12.6.4|Ethernet RGMII........................................... 103|
||...................................................................... 42|12.6.5|MDIO timing specifications......................... 104|
|6.9|Supply currents............................................. 42|12.7|QuadSPI..................................................... 105|
|6.10|Operating mode............................................ 58|12.7.1|QuadSPI Quad 3.3V SDR 120MHz............ 105|
|6.11|Cyclic wake-up current .................................60|12.7.2|QuadSPI Octal 3.3V DDR 100MHz............ 107|
|7|I/O parameters................................................. 60|12.7.3|QuadSPI Octal 3.3V DDR 120MHz............ 108|
|7.1|GPIO DC electrical specifications, 3.3V Range|12.8|uSDHC........................................................109|
||(2.97V - 3.63V)..............................................60|12.8.1|uSDHC SDR electrical specifications......... 109|
|7.2|GPIO DC electrical specifications, 5.0V (4.5V -|12.8.2|uSDHC DDR electrical specifications......... 110|
||5.5V)............................................................. 64|12.9|LPUART specifications............................... 112|
|7.3|5.0V (4.5V - 5.5V) GPIO Output AC|13|Debug modules.............................................. 112|
||Specification..................................................68|13.1|Debug trace timing specifications............... 112|
|7.4|3.3V (2.97V - 3.63V) GPIO Output AC|13.2|SWD electrical specifications......................113|
||Specification..................................................69|13.3|JTAG electrical specifications..................... 114|
|8|Glitch Filter....................................................... 70|14|Thermal Attributes.......................................... 116|
|9|Flash memory specification..............................71|14.1|Description.................................................. 116|
|9.1|Flash memory program and erase|14.2|Thermal characteristics...............................117|
||specifications................................................ 71|15|Dimensions.....................................................117|
|9.2|Flash memory Array Integrity and Margin Read|15.1|Obtaining package dimensions...................118|
||specifications................................................ 72|16|Revision history.............................................. 118|
|9.3|Flash memory module life specifications...... 73|Legal inf|ormation.............................................................127|
|9.3.1|Data retention vs program/erase cycles....... 73|||
|9.4|Flash memory AC timing specifications........ 74|||



NXP Semiconductors 

Overview 

#### 1 Overview 

The S32K3xx product series further extends the highly-scalable portfolio of Arm<sup>®</sup> Cortex<sup>®</sup> - M0+/M4F S32K1xx chips in the automotive industry with the Arm Cortex-M7 core at higher frequency, more memory, ASIL-B and D rating and advanced security module. With a focus on automotive environment robustness, the S32K3xx product series devices are well suited to a wide range of applications in electrical harsh environments, and are optimized for cost-sensitive applications offering new, space saving package options. The S32K3xx series offers a broad range of memory, peripherals and performance options. Devices in this series share common peripherals and pin-out, allowing developers to migrate easily within a chip series or among other chip series to take advantage of more memory or feature integration. 

~~<mark>CAUTION</mark>~~ 

S32K3x1, S32K322, S32K342 and S32K3x8 specific information is preliminary until these devices are qualified and may change without notice. 

#### 2 Block diagram 

The following figures show the S32K3xx product series block diagrams<sup>[1]</sup> 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0004-08.png)


<!-- Start of picture text -->
Memory CPU Platform Security: HSE-B<br>1 MB Pflash with ECC Cortex-M7 Cortex-M0+ RAM Security<br>64 kB Dflash with ECC 120 MHz Asymmetric Hardware Accelerators<br>128 kB RAM with ECCIncl 96 kB TCM Single Core FPU, DSPD-cacheI-cache Symmetric Hardware Accelerators ••• Side-channel physicalFirmware included,upgradableHW accl for AES 256,RSA 4096, ECC 521<br>System protection<br>XRDC Lifecycle • Meet Evita Full<br>Access control Management function goal<br>FXOSC (8-40 MHz) Fabric<br>Xbar (64 bit) TRNG/PRNG<br>FIRC (48 MHz)<br>Network Communication Analog/Timers Functional Safety<br>SIRC (32 KHz) 16 ch FlexIOEmulating 2 x 24 ch 12 bit ADC Safety<br>PLL I2S, SENT, PWMUART, I2C, SPI BCTU (Body Control Trigger Unit) CMU FCCU •• MBIST/LBIST/Self TestHW redundancy<br>12ch DMA all ch support CAN FD3 x FlexCAN 4 x LPSPI LCU MPU SWT •• Clock/Voltage monitorCentralized errordetection<br>32ch ext. INT/WUP 2 x LPI2C 2 x 24 ch 16 bit eMIOS Timer EIM/ERM CRC STCU2 • ASIL B compliant<br>Debug/Trace (SWD/JTAG/ETB) 4 x LPUART (LIN) 1 x I3C 1 x LPCMP 32 bit RTC<br>Memory CPU Platform Network/ Motor Control<br>Communication<br>• OTA ready - • Single Arm M7 • CAN/CAN FD, LIN • On-chip motor • Future Proof Security/OTA<br>RWW, A/B swap core • Flexible IO emulation control subsystem • ISO26262 Compliant Safety System<br>• Optimized for Real- • Offloading CPU • Scalable Arm platform<br>time with zero wait • Optimized for LOW power<br>I/D-TCM • Rich Network/Communication Interface<br><!-- End of picture text -->

Figure 1. S32K311: ASIL B Single Core 1MB General Purpose MCU 

[1] See Table 1 for device specific values. 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

4 / 130 

NXP Semiconductors 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0005-01.png)


<!-- Start of picture text -->
Block diagram<br><!-- End of picture text -->


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0005-02.png)


<!-- Start of picture text -->
Memory CPU Platform Security: HSE-B<br>2 MB Pflash with ECC Cortex-M7 Cortex-M0+ RAM Security<br>128 kB Dflash with ECC 120 MHz Asymmetric Hardware Accelerators<br>192 kB RAM with ECCIncl 96 kB TCM Single Core FPU, DSPD-cacheI-cache Symmetric Hardware Accelerators ••• Side-channel physicalFirmware included,HW accl for AES 256,upgradableRSA 4096, ECC 521<br>System protection<br>XRDC Lifecycle • Meet Evita Full<br>Access control Management function goal<br>FXOSC (8-40 MHz) Fabric<br>Xbar (64 bit) TRNG/PRNG<br>FIRC (48 MHz)<br>SIRC (32 kHz) Network Communication Analog/Timers Functional Safety<br>SXOSC (32 kHz) 32 ch FlexIOEmulating 2 x 24 ch 12 bit ADC Safety<br>PLL I2S, SENT, PWMUART, I2C, SPI BCTU (Body Control Trigger Unit) CMU FCCU •• MBIST/LBIST/Self TestHW redundancy<br>32ch DMA all ch support CAN FD6 x FlexCAN 4 x LPSPI LCU MPU SWT •• Centralized errordetectionClock/Voltage monitor<br>32ch ext. INT/WUP 2 x LPI2C 2 x 24 ch 16 bit eMIOS Timer EIM/ERM CRC STCU2 • ASIL B compliant<br>Debug/Trace (SWD/JTAG/ETB) 8 x LPUART (LIN) 1 x I3C 2 x LPCMP<br>Memory CPU Platform Network/ Motor Control<br>Communication<br>• OTA ready - • Single Arm M7 • CAN/CAN FD, LIN • On-chip motor • Future Proof Security/OTA<br>RWW, A/B swap core • Flexible IO emulation control subsystem • ISO26262 Compliant Safety System<br>• Optimized for Real- • Offloading CPU • Scalable Arm platform<br>time with zero wait • Optimized for LOW power<br>I/D-TCM • Rich Network/Communication Interface<br>Figure 2. S32K312: ASIL B Single Core 2MB General Purpose MCU<br>Memory External Memory IF CPU Platform Security: HSE-B<br>2 MB Pflash with ECC 1 x QuadSPI Cortex-M7 Cortex-M7 Cortex-M0+ RAM Security<br>128 kB Dflash with ECC256 kB RAM with ECCIncl 192 kB TCM Up to 480 Mbps4 bit data width Dual Core FPU, DSP160 MHzD-cacheI-cache FPU, DSP160 MHzD-cacheI-cache Asymmetric Hardware AcceleratorsSymmetric Hardware Accelerators ••• Side-channel physicalFirmware included,upgradableHW accl for AES 256,RSA 4096, ECC 521<br>System protection<br>XRDC Lifecycle • Meet Evita Full<br>Access control Management function goal<br>FXOSC (8-40 MHz) Fabric<br>Xbar (64 bit) TRNG/PRNG<br>FIRC (48 MHz)<br>SIRC (32 kHz) Network Communication Analog/Timers Functional Safety<br>SXOSC (32 kHz)PLL 1 x Ethernet, 100 MbpsAVB/TSN I2S, SENT, PWMUART, I2C, SPI32 ch FlexIOEmulating BCTU (Body Control Trigger Unit)2 x 24 ch 12 bit ADC CMU FCCU •• MBIST/LBIST/Self TestHW redundancy Safety<br>32ch ext. INT/WUP32ch DMA all ch support CAN FD4 x FlexCAN 4 x LPSPI2 x LPI2C1 x I3C 2 x 24 ch 16 bit eMIOS TimerLCU EIM/ERMMPU CRC SWTSTCU2 ••• ASIL B compliantClock/Voltage monitorCentralized errordetection<br>Debug/Trace (SWD/JTAG/ETB) 4 x LPUART (LIN) 2 x SAI (TDM, I2S) 2 x LPCMP 32 bit RTC<br>Memory CPU Platform Network/ Motor Control<br>Communication<br>• OTA ready - • Two independent • Ethernet (TSN), CAN/ • On-chip motor • Future Proof Security/OTA<br>RWW, A/B swap Arm M7 cores CAN FD, LIN control subsystem • ISO26262 Compliant Safety System<br>• External • Optimized for Real- • SAI for Audio • Offloading CPU • Scalable Arm platform<br>Flash/Ram time with zero wait • Flexible IO emulation • Optimized for LOW power<br>expansion by I/D-TCM • Rich Network/Communication Interface<br>QuadSPI<br>Figure 3. S32K322: ASIL B Dual Core 2MB General Purpose MCU<br><!-- End of picture text -->

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

5 / 130 

NXP Semiconductors 

Block diagram 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0006-02.png)


<!-- Start of picture text -->
Memory External Memory IF CPU Platform Security: HSE-B<br>1 MB Pflash with ECC 1 x QuadSPI Cortex-M7 Cortex-M7 Cortex-M0+ RAM Security<br>128 kB Dflash with ECC256 kB RAM with ECCIncl 192 kB TCM Up to 480 Mbps4 bit data width Lockstep Core FPU, DSP160 MHzD-cacheI-cache FPU, DSP160 MHzD-cacheI-cache Asymmetric Hardware AcceleratorsSymmetric Hardware Accelerators ••• HW accl for AES 256,RSA 4096, ECC 521Firmware included,upgradableSide-channel physical<br>System protection<br>XRDC Lifecycle • Meet Evita Full<br>Access control Management function goal<br>FXOSC (8-40 MHz) Fabric<br>Xbar (64 bit) TRNG/PRNG<br>FIRC (48 MHz)<br>SIRC (32 kHz) Network Communication Analog/Timers Functional Safety<br>SXOSC (32 kHz)PLL 1 x Ethernet, 100 MbpsAVB/TSN I2S, SENT, PWMUART, I2C, SPI32 ch FlexIOEmulating BCTU (Body Control Trigger Unit)2 x 24 ch 12 bit ADC CMU FCCU •• HW redundancyMBIST/LBIST/Self Test Safety<br>32ch ext. INT/WUP32ch DMA all ch support CAN FD4 x FlexCAN 4 x LPSPI1 x I3C2 x LPI2C 2 x 24 ch 16 bit eMIOS TimerLCU EIM/ERMMPU CRC SWTSTCU2 ••• Clock/Voltage monitorCentralized errordetectionASIL D compliant<br>Debug/Trace (SWD/JTAG/ETB) 4 x LPUART (LIN) 2 x SAI (TDM, I2S) 2 x LPCMP 32 bit RTC<br>Memory CPU Platform Network/ Motor Control<br>Communication<br>• OTA ready - • Scalable Arm M7 • Ethernet (TSN), CAN/ • On-chip motor • Future Proof Security/OTA<br>RWW, A/B swap core in Lockstep CAN FD, LIN control subsystem • ISO26262 Compliant Safety System<br>• External • Optimized for Real- • SAI for Audio • Offloading CPU • Scalable Arm platform<br>Flash/Ram time with zero wait • Flexible IO emulation • Optimized for LOW power<br>expansion by I/D-TCM • Rich Network/Communication Interface<br>QuadSPI<br>Figure 4. S32K341: ASIL D Lockstep Core 1MB General Purpose MCU<br>Memory External Memory IF CPU Platform Security: HSE-B<br>2 MB Pflash with ECC 1 x QuadSPI Cortex-M7 Cortex-M7 Cortex-M0+ RAM Security<br>128 kB Dflash with ECC256 kB RAM with ECCIncl 192 kB TCM Up to 480 Mbps4 bit data width Lockstep Core FPU, DSP160 MHzD-cacheI-cache FPU, DSP160 MHzD-cacheI-cache Asymmetric Hardware AcceleratorsSymmetric Hardware Accelerators ••• upgradableRSA 4096, ECC 521Firmware included,Side-channel physicalHW accl for AES 256,<br>System protection<br>XRDC Lifecycle • Meet Evita Full<br>Access control Management function goal<br>FXOSC (8-40 MHz) Fabric<br>Xbar (64 bit) TRNG/PRNG<br>FIRC (48 MHz)<br>SIRC (32 kHz) Network Communication Analog/Timers Functional Safety<br>SXOSC (32 kHz)PLL 1 x Ethernet, 100 MbpsAVB/TSN I2S, SENT, PWMUART, I2C, SPI32 ch FlexIOEmulating BCTU (Body Control Trigger Unit)2 x 24 ch 12 bit ADC CMU FCCU •• MBIST/LBIST/Self TestHW redundancy Safety<br>32ch ext. INT/WUP32ch DMA all ch support CAN FD4 x FlexCAN 4 x LPSPI2 x LPI2C1 x I3C 2 x 24 ch 16 bit eMIOS TimerLCU EIM/ERMMPU CRC SWTSTCU2 ••• detectionClock/Voltage monitorASIL D compliantCentralized error<br>Debug/Trace (SWD/JTAG/ETB) 4 x LPUART (LIN) 2 x SAI (TDM, I2S) 2 x LPCMP 32 bit RTC<br>Memory CPU Platform Network/ Motor Control<br>Communication<br>• OTA ready - • Scalable Arm M7 • Ethernet (TSN), CAN/ • On-chip motor • Future Proof Security/OTA<br>RWW, A/B swap core in Lockstep CAN FD, LIN control subsystem • ISO26262 Compliant Safety System<br>• External • Optimized for Real- • SAI for Audio • Offloading CPU • Scalable Arm platform<br>Flash/Ram time with zero wait • Flexible IO emulation • Optimized for LOW power<br>expansion by I/D-TCM • Rich Network/Communication Interface<br>QuadSPI<br>Figure 5. S32K342: ASIL D Lockstep Core 2MB General Purpose MCU<br><!-- End of picture text -->

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

6 / 130 

NXP Semiconductors 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0007-01.png)


<!-- Start of picture text -->
Block diagram<br><!-- End of picture text -->


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0007-02.png)


<!-- Start of picture text -->
Memory External Memory IF CPU Platform Security: HSE-B<br>4 MB Pflash with ECC 1 x QuadSPI Cortex-M7 Cortex-M0+ RAM Security<br>128 kB Dflash with ECC512 kB RAM with ECCIncl 96 kB TCM Up to 480 Mbps4 bit data width Single Core FPU, DSP160 MHzD-cacheI-cache Asymmetric Hardware AcceleratorsSymmetric Hardware Accelerators ••• upgradableRSA 4096, ECC 521Firmware included,Side-channel physicalHW accl for AES 256,<br>System protection<br>XRDC Lifecycle • Meet Evita Full<br>Access control Management function goal<br>FXOSC (8-40 MHz) Fabric<br>Xbar (64 bit) TRNG/PRNG<br>FIRC (48 MHz)<br>SIRC (32 kHz) Network Communication Analog/Timers Functional Safety<br>SXOSC (32 kHz) 1 x Ethernet, 100 MbpsAVB/TSN 32 ch FlexIOEmulating 3 x 24 ch 12 bit ADC Safety<br>PLL I2S, SENT, PWMUART, I2C, SPI BCTU (Body Control Trigger Unit) CMU FCCU •• MBIST/LBIST/Self TestHW redundancy<br>32ch DMA all ch support CAN FD6 x FlexCAN 6 x LPSPI LCU MPU SWT •• detectionClock/Voltage monitorCentralized error<br>32ch ext. INT/WUP 2 x LPI2C 3 x 24 ch 16 bit eMIOS Timer EIM/ERM CRC STCU2 • ASIL B compliant<br>Debug/Trace (SWD/JTAG/ETB) 16 x LPUART (LIN) 2 x SAI (TDM, I2S) 3 x LPCMP 32 bit RTC<br>Memory CPU Platform Network/ Motor Control<br>Communication<br>• OTA ready - • Single Arm M7 • Ethernet (TSN), CAN/ • On-chip motor • Future Proof Security/OTA<br>RWW, A/B swap core CAN FD, LIN control subsystem • ISO26262 Compliant Safety System<br>• External • Optimized for Real- • SAI for Audio • Offloading CPU • Scalable Arm platform<br>Flash/Ram time with zero wait • Flexible IO emulation • Optimized for LOW power<br>expansion by I/D-TCM • Rich Network/Communication Interface<br>QuadSPI<br>Figure 6. S32K314: ASIL B Single Core 4MB General Purpose MCU<br>Memory External Memory IF CPU Platform Security: HSE-B<br>4 MB Pflash with ECC 1 x QuadSPI Cortex-M7 Cortex-M7 Cortex-M0+ RAM Security<br>128 kB Dflash with ECC512 kB RAM with ECCIncl 192 kB TCM Up to 480 Mbps4 bit data width Dual Core FPU, DSP160 MHzD-cacheI-cache FPU, DSP160 MHzD-cacheI-cache Asymmetric Hardware AcceleratorsSymmetric Hardware Accelerators ••• HW accl for AES 256,upgradableRSA 4096, ECC 521Firmware included,Side-channel physical<br>System protection<br>XRDC Lifecycle • Meet Evita Full<br>Access control Management function goal<br>FXOSC (8-40 MHz) Fabric<br>Xbar (64 bit) TRNG/PRNG<br>FIRC (48 MHz)<br>SIRC (32 kHz) Network Communication Analog/Timers Functional Safety<br>SXOSC (32 kHz) 1 x Ethernet, 100 MbpsAVB/TSN 32 ch FlexIOEmulating 3 x 24 ch 12 bit ADC Safety<br>PLL I2S, SENT, PWMUART, I2C, SPI BCTU (Body Control Trigger Unit) CMU FCCU •• MBIST/LBIST/Self TestHW redundancy<br>32ch DMAMUX all ch support CAN FD6 x FlexCAN 6 x LPSPI LCU MPU SWT •• detectionClock/Voltage monitorCentralized error<br>32ch ext. INT/WUP 2 x LPI2C 3 x 24 ch 16 bit eMIOS Timer EIM/ERM CRC STCU2 • ASIL B compliant<br>Debug/Trace (SWD/JTAG/ETB) 16 x LPUART (LIN) 2 x SAI (TDM, I2S) 3 x LPCMP 32 bit RTC<br>Memory CPU Platform Network/ Motor Control<br>Communication<br>• OTA ready - • Two independent • Ethernet (TSN), CAN/ • On-chip motor • Future Proof Security/OTA<br>RWW, A/B swap Arm M7 cores CAN FD, LIN control subsystem • ISO26262 Compliant Safety System<br>• External • Optimized for Real- • SAI for Audio • Offloading CPU • Scalable Arm platform<br>Flash/Ram time with zero wait • Flexible IO emulation • Optimized for LOW power<br>expansion by I/D-TCM • Rich Network/Communication Interface<br>QuadSPI<br>Figure 7. S32K324: ASIL B Dual Core 4MB General Purpose MCU<br><!-- End of picture text -->

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

7 / 130 

NXP Semiconductors 

Block diagram 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0008-02.png)


<!-- Start of picture text -->
Memory External Memory IF CPU Platform Security: HSE-B<br>4 MB Pflash with ECC 1 x QuadSPI Cortex-M7 Cortex-M7 Cortex-M0+ RAM Security<br>128 kB Dflash with ECC512 kB RAM with ECCIncl 192 kB TCM Up to 480 Mbps4 bit data width Lockstep Core FPU, DSP160 MHzD-cacheI-cache FPU, DSP160 MHzD-cacheI-cache Asymmetric Hardware AcceleratorsSymmetric Hardware Accelerators ••• Side-channel physicalFirmware included,HW accl for AES 256,upgradableRSA 4096, ECC 521<br>System protection<br>XRDC Lifecycle • Meet Evita Full<br>Access control Management function goal<br>FXOSC (8-40 MHz) Fabric<br>Xbar (64 bit) TRNG/PRNG<br>FIRC (48 MHz)<br>SIRC (32 kHz) Network Communication Analog/Timers Functional Safety<br>SXOSC (32 kHz) 1 x Ethernet, 100 MbpsAVB/TSN 32 ch FlexIOEmulating 3 x 24 ch 12 bit ADC Safety<br>PLL I2S, SENT, PWMUART, I2C, SPI BCTU (Body Control Trigger Unit) CMU FCCU •• MBIST/LBIST/Self TestHW redundancy<br>32ch DMA and DMAMUX all ch support CAN FD6 x FlexCAN 6 x LPSPI LCU MPU SWT •• Centralized errordetectionClock/Voltage monitor<br>32ch ext. INT/WUP 2 x LPI2C 3 x 24 ch 16 bit eMIOS Timer EIM/ERM CRC STCU2 • ASIL D compliant<br>Debug/Trace (SWD/JTAG/ETB) 16 x LPUART (LIN) 2 x SAI (TDM, I2S) 3 x LPCMP 32 bit RTC<br>Memory CPU Platform Network/ Motor Control<br>Communication<br>• OTA ready - • Scalable Arm M7 • Ethernet (TSN), CAN/ On-chip motor • Future Proof Security/OTA<br>RWW, A/B swap core in Lockstep CAN FD, LIN control subsystem • ISO26262 Compliant Safety System<br>• External • Optimized for Real- • SAI for Audio Offloading CPU • Scalable Arm platform<br>Flash/Ram time with zero wait • Flexible IO emulation • Optimized for LOW power<br>expansion by I/D-TCM • Rich Network/Communication Interface<br>QuadSPI<br>Figure 8. S32K344: ASIL D Lockstep Core 4MB General Purpose MCU<br>Memory External Memory IF CPU Platform Security: HSE-B<br>8 MB Pflash with ECC 1 x QuadSPI Cortex-M7 Cortex-M7 Cortex-M0+ RAM Security<br>128 kB Dflash with ECC Up to 2 Gbps  240 MHz 240 MHz Asymmetric Hardware Accelerators<br>1152 kB RAM with ECCIncl 192 kB TCM 8 bit data width FPU, DSPD-cacheI-cache FPU, DSPD-cacheI-cache Symmetric Hardware Accelerators ••• Side-channel physicalFirmware included,HW accl for AES 256,upgradableRSA 4096, ECC 521<br>System protection<br>XRDC Lifecycle • Meet Evita Full<br>Access control Management function goal<br>FXOSC (8-40 MHz) Fabric<br>Xbar (64 bit) TRNG/PRNG<br>FIRC (48 MHz)<br>SIRC (32 kHz) Network Communication Analog/Timers Functional Safety<br>32ch ext. INT/WUPSXOSC (32 kHz)32ch DMAMUX2 x PLL 1 x Ethernet, 1 Gbpsall ch support CAN FD6 x FlexCANAVB/TSN1 x uSDHC I2S, SENT, PWMUART, I2C, SPI32 ch FlexIOEmulating6 x LPSPI2 x LPI2C1 x I3C BCTU (Body Control Trigger Unit)3 x 24 ch 16 bit eMIOS Timer3 x 24 ch 12 bit ADCLCU EIM/ERMCMUMPU CRC FCCUSWTSTCU2 ••••• Centralized errorMBIST/LBIST/Self TestdetectionClock/Voltage monitorHW redundancyASIL B compliant Safety<br>Debug/Trace (SWD/JTAG/ETB) 16 x LPUART (LIN) 2 x SAI (TDM, I2S) 3 x LPCMP 32 bit RTC<br>Memory CPU Platform Network/ Motor Control<br>Communication<br>• OTA ready - • Two independent • Ethernet (TSN), CAN/ • On-chip motor • Future Proof Security/OTA<br>RWW, A/B swap Arm M7 cores CAN FD, LIN control subsystem • ISO26262 Compliant Safety System<br>• External • Optimized for Real- • SAI for Audio • Offloading CPU • Scalable Arm platform<br>Flash/Ram time with zero wait • Flexible IO emulation • Optimized for LOW power<br>expansion by I/D-TCM • Rich Network/Communication Interface<br>QuadSPI<br>Figure 9. S32K328: ASIL B Dual Core 8MB General Purpose MCU<br><!-- End of picture text -->

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

8 / 130 

NXP Semiconductors 

###### Block diagram 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0009-02.png)


<!-- Start of picture text -->
Memory External Memory IF CPU Platform Security: HSE-B<br>8 MB Pflash with ECC 1 x QuadSPI Cortex-M7 Cortex-M7 Cortex-M7 Cortex-M0+ RAM Security<br>128 kB Dflash with ECC Up to 2 Gbps  240 MHz 240 MHz 240 MHz Asymmetric Hardware Accelerators<br>1152 kB RAM with ECCIncl 384 kB TCM 8 bit data width FPU, DSPD-cacheI-cache FPU, DSPD-cacheI-cache FPU, DSPD-cacheI-cache Symmetric Hardware Accelerators ••• Firmware included,HW accl for AES 256,Side-channel physicalRSA 4096, ECC 521upgradable<br>System protection<br>XRDC Lifecycle • Meet Evita Full<br>Access control Management function goal<br>FXOSC (8-40 MHz) Fabric<br>Xbar (64 bit) TRNG/PRNG<br>FIRC (48 MHz)<br>SIRC (32 kHz) Network Communication Analog/Timers Functional Safety<br>32ch DMA and DMAMUX32ch ext. INT/WUPSXOSC (32 kHz)2 x PLL 1 x Ethernet, 1 Gbpsall ch support CAN FD8 x FlexCAN1 x uSDHCAVB/TSN I2S, SENT, PWMUART, I2C, SPI32 ch FlexIOEmulating6 x LPSPI2 x LPI2C1 x I3C BCTU (Body Control Trigger Unit)3 x 24 ch 16 bit eMIOS Timer3 x 24 ch 12 bit ADCLCU EIM/ERMCMUMPU CRC FCCUSWTSTCU2 ••••• Centralized errorMBIST/LBIST/Self TestdetectionClock/Voltage monitorHW redundancyASIL D compliant Safety<br>Debug/Trace (SWD/JTAG/ETB) 16 x LPUART (LIN) 2 x SAI (TDM, I2S) 3 x LPCMP 32 bit RTC<br>Memory CPU Platform Network/ Motor Control<br>Communication<br>• OTA ready - • Three independent • Ethernet (TSN), CAN/ • On-chip motor • Future Proof Security/OTA<br>RWW, A/B swap Arm M7 cores CAN FD, LIN control subsystem • ISO26262 Compliant Safety System<br>• External • Optimized for Real- • SAI for Audio • Offloading CPU • Scalable Arm platform<br>Flash/Ram time with zero wait • Flexible IO emulation • Optimized for LOW power<br>expansion by I/D-TCM • Rich Network/Communication Interface<br>QuadSPI<br>Figure 10. S32K338: ASIL B Three Core 8MB General Purpose MCU<br>Memory External Memory IF CPU Platform Security: HSE-B<br>8 MB Pflash with ECC 1 x QuadSPI Cortex-M7 Cortex-M7 Cortex-M0+ RAM Security<br>128 kB Dflash with ECC Up to 2 Gbps  240 MHz 240 MHz Asymmetric Hardware Accelerators<br>1152 kB RAM with ECCIncl 192 kB TCM 8 bit data width FPU, DSPD-cacheI-cache FPU, DSPD-cacheI-cache Symmetric Hardware Accelerators ••• Firmware included,HW accl for AES 256,Side-channel physicalRSA 4096, ECC 521upgradable<br>System protection<br>Lockstep Core XRDC Lifecycle • Meet Evita Full<br>Access control Management function goal<br>FXOSC (8-40 MHz) Fabric<br>Xbar (64 bit) TRNG/PRNG<br>FIRC (48 MHz)<br>SIRC (32 kHz) Network Communication Analog/Timers Functional Safety<br>32ch DMA and DMAMUX32ch ext. INT/WUPSXOSC (32 kHz)2 x PLL 1 x Ethernet, 1 Gbpsall ch support CAN FD6 x FlexCAN1 x uSDHCAVB/TSN I2S, SENT, PWMUART, I2C, SPI32 ch FlexIOEmulating6 x LPSPI2 x LPI2C1 x I3C BCTU (Body Control Trigger Unit)3 x 24 ch 16 bit eMIOS Timer3 x 24 ch 12 bit ADCLCU EIM/ERMCMUMPU CRC FCCUSWTSTCU2 ••••• MBIST/LBIST/Self TestCentralized errordetectionClock/Voltage monitorHW redundancyASIL D compliant Safety<br>Debug/Trace (SWD/JTAG/ETB) 16 x LPUART (LIN) 2 x SAI (TDM, I2S) 3 x LPCMP 32 bit RTC<br>Memory CPU Platform Network/ Motor Control<br>Communication<br>• OTA ready - • Arm M7 cores in • Ethernet (TSN), CAN/ • On-chip motor • Future Proof Security/OTA<br>RWW, A/B swap lockstep CAN FD, LIN control subsystem • ISO26262 Compliant Safety System<br>• External • Optimized for Real- • SAI for Audio • Offloading CPU • Scalable Arm platform<br>Flash/Ram time with zero wait • Flexible IO emulation • Optimized for LOW power<br>expansion by I/D-TCM • Rich Network/Communication Interface<br>QuadSPI<br>Figure 11. S32K348: ASIL D Lockstep Core 8MB General Purpose MCU<br><!-- End of picture text -->

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

9 / 130 

NXP Semiconductors 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0010-01.png)


<!-- Start of picture text -->
Feature comparison<br><!-- End of picture text -->


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0010-02.png)


<!-- Start of picture text -->
Memory External Memory IF CPU Platform Security: HSE-B<br>8 MB Pflash with ECC 1 x QuadSPI Cortex-M7 Cortex-M7 Cortex-M7 Cortex-M0+ RAM Security<br>128 kB Dflash with ECC Up to 2 Gbps  240 MHz 240 MHz 240 MHz Asymmetric Hardware Accelerators<br>1152 kB RAM with ECCIncl 384 kB TCM 4 bit data width FPU, DSPD-cacheI-cache FPU, DSPD-cacheI-cache FPU, DSPD-cacheI-cache Symmetric Hardware Accelerators ••• Side-channel physicalFirmware included,HW accl for AES 256,upgradableRSA 4096, ECC 521<br>System protection<br>Lockstep Core XRDC Lifecycle • Meet Evita Full<br>Access control Management function goal<br>FXOSC (8-40 MHz) Fabric<br>Xbar (64 bit) TRNG/PRNG<br>FIRC (48 MHz)<br>SIRC (32 kHz) Network Communication Analog/Timers Functional Safety<br>32ch ext. INT/WUPSXOSC (32 kHz)32ch DMA2 x PLL 1 x Ethernet, 1 Gbpsall ch support CAN FD8 x FlexCAN1 x uSDHCAVB/TSN I2S, SENT, PWMUART, I2C, SPI32 ch FlexIOEmulating6 x LPSPI2 x LPI2C1 x I3C BCTU (Body Control Trigger Unit)3 x 24 ch 16 bit eMIOS Timer3 x 24 ch 12 bit ADCLCU EIM/ERMCMUMPU CRC FCCUSWTSTCU2 ••••• Centralized errorMBIST/LBIST/Self TestdetectionClock/Voltage monitorHW redundancyASIL D compliant Safety<br>Debug/Trace (SWD/JTAG/ETB) 16 x LPUART (LIN) 2 x SAI (TDM, I2S) 3 x LPCMP 32 bit RTC<br>Memory CPU Platform Network/ Motor Control<br>Communication<br>• OTA ready - • Arm M7 cores in • Ethernet (TSN), CAN/ • On-chip motor • Future Proof Security/OTA<br>RWW, A/B swap lockstep CAN FD, LIN control subsystem • ISO26262 Compliant Safety System<br>• External • One independent • SAI for Audio • Offloading CPU • Scalable Arm platform<br>Flash/Ram Arm M7 for real • Flexible IO emulation • Optimized for LOW power<br>expansion by time processing • Rich Network/Communication Interface<br>QuadSPI • Optimized for Real-<br>time with zero wait<br>I/D-TCM<br><!-- End of picture text -->

Figure 12. S32K358: ASIL D Lockstep Core + One, 8MB General Purpose MCU 

#### 3 Feature comparison 

The following table compares some of the prominent features related to memory and package options of the chips from the S32K3xx family/product series. 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

10 / 130 

Table 1. S32K3xx chip's feature comparison 

|Feature||||||Ch|ip||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||S32K311|S32K312|S32K322|S32K341|S32K342|S32K314|S32K324|S32K344|S32K328<sup>1</sup>|S32K338<br>2|S32K348<sup>3</sup>|S32K358<sup>4</sup>|
|Safety/ASIL||B||D||B||D|B|B|D|D|
|Program flash<br>memory (MB)|1||2|1|2||4||||8||
|Data flash<br>memory (KB)|64||||128|||||1|28||
|Total RAM<br>(KB)|128 KB<br>(including<br>96 KB<br>TCM)|192 KB<br>(including<br>96 KB<br>TCM)|256 KB (in|cluding 192|KB TCM)|512 KB<br>(including<br>96 KB<br>TCM)|512 KB (<br>192 KB|including<br>TCM)|1152 KB<br>(including<br>192 KB<br>TCM)|1152 KB<br>(including<br>384 KB<br>TCM)|<br>1152 KB<br>(including<br>192 KB<br>TCM)|1152 KB<br>(including<br>384 KB<br>TCM)|
|Standby RAM||||32|KB|||||64|KB||
|Security||||HSE|_B|||||HS|E_B||
|Core quantity|1 x Cor|tex-M7|2 x Cortex-<br>M7|1 x Cortex|-M7 LS|1 x Cortex-<br>M7|2 x<br>Cortex-M7|1 x Cortex-<br>M7 LS|2 x<br>Cortex-<br>M7|3 x<br>Cortex-<br>M7|1 x<br>Cortex-<br>M7 LS|1 x Cortex-<br>M7 LS + 1 x<br>Cortex-M7|
|Frequency<br>(MHz)|1|20|||1|60|||160|240|160|240|
|DMA channels|1|2||||32|||||32||
|ASIL–B<br>DMIPS<sup>5</sup>|256|–387|684–1033|—||342–516|684–1033|—|684–1033|1539–<br>2325|—|513–775<sup>6</sup>|
|ASIL–D<br>DMIPS<sup>5</sup>||—||342–|516|—||342–516|—||342–516|513–775<sup>6</sup>|
|ASIL–B<br>CoreMark<br>score<sup>7</sup>|5|84|1558|—||779|1558|—|1558|3506|—|1168<sup>6</sup>|
|ASIL–D<br>CoreMark<br>score<sup>7</sup>||—||77|9|—||779|—||779|1168<sup>6</sup>|



Table continues on the next page... 

###### Table 1. S32K3xx chip's feature comparison (continued) 

|Feature||||||Ch|ip||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||S32K311|S32K312|S32K322|S32K341|S32K342|S32K314|S32K324|S32K344|S32K328<sup>1</sup>|S32K338<br>2<br>|S32K348<sup>3</sup>|S32K358<sup>4</sup>|
|FlexCAN<br>instances|3|6||4|||6|||8|||
|EMAC<br>instances||0||||1||||0|||
|GMAC<br>instances|||||0|||||1|||
|SAI instances||0||||2||||2|||
|LPUART<br>instances|4|8||4|||16|||1|6||
|LPSPI<br>instances|||4||||6|||6|||
|I<sup>2</sup>C instances|||||2|||||2|||
|I<sup>3</sup>C instances|||1||||—|||1|||
|FlexIO (incl.<br>SENT support)<br>channels|16||||32|||||3|2||
|QuadSPI<br>instances||0||||1<sup>8</sup>||||1|<sup>9</sup>||
|uSDHC<br>instances|||||0|||||1|||
|ADC instances|||2||||3|||3|||
|LPCMP<br>instances|1||2||||3|||3|||
|PIT instances||2||||3||||3|||
|SWT instances<br>STM instances||1<br>1|2||1|2|2|1|2|3<br>3|1<br>|2|



Table continues on the next page... 

Table 1. S32K3xx chip's feature comparison (continued) 

|Feature||||||Ch|ip|||||
|---|---|---|---|---|---|---|---|---|---|---|---|
||S32K311|S32K312|S32K322|S32K341|S32K342|S32K314|S32K324|S32K344|S32K328<sup>1</sup>|S32K338<br>2<br>S32K348<sup>3</sup>|S32K358<sup>4</sup>|
|LCU instances|||||2|||||2||
|BCTU<br>instances|||||1|||||1||
|TRGMUX<br>instances|||||1|||||1||
|eMIOS<br>instances|||2||||3|||3||
|RTC instances|||||Yes|||||Yes||
|289-ball<br>MAPBGA<br>package|||||No|||||Yes||
|257-ball<br>MAPBGA<br>package|||No||||Yes|||No||
|172-MAX QFP<br>package|No||||Yes|||||Yes<sup>10</sup>||
|100-MAX QFP<br>package|||Yes||||No|||No||
|48-pin LQFP<br>package|Yes||||No|||||No||



1. The S32K328 feature set is under evaluation and subject to change. 

2. The S32K338 feature set is under evaluation and subject to change. 

3. The S32K348 feature set is under evaluation and subject to change. 

4. The S32K358 feature set is under evaluation and subject to change. 5. Final DMIPS is in range base on complier setting. Low number is using "ground rules" laid out in the Dhrystone documentation. High number is using inlining of functions a simultaneous ("multi-file") compilation. 

6. ASIL-B and ASIL-D performance is available simultaneously. 

7. Result depends on specific compiler version, contact NXP sales representative for more details. 8. 4-bit data width 9. 8-bit data width 10. 172 MAXQFP-EP (exposed pad) 

NXP Semiconductors 

Ordering information 

#### 4 Ordering information 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0014-03.png)


<!-- Start of picture text -->
Figure 13. Ordering information<br>P/S 32 K 3 4 4 X X T0 M PA S R<br>Product status<br>Product Type/Brand<br>Product Line<br>Series/Family<br>Core platform<br>Memory size<br>Features<br>Security<br>Fab and Mask rev letter<br>Temperature Suffix<br>Package Suffix<br>Software<br>configuration<br>Tape and Reel<br>Indicator<br>Product status Features Package Suffix<br>P: Prototype Ethernet Feature pins BGA MaxQFP MaxQFP-EP LQFP<br>S: Qualified ordering P/N No Ethernet 100 Mbps Ethernet 48 - - - LF<br>Product Type/Brand MAC MAC 100 - PA - -<br>32: Automotive 32-bit MCU/MPU N E 172 - PB PC -<br>257 MM - - -<br>Product Line 289 JB - - -<br>Security<br>K: General purpose MCU<br>Flex HSE B Customised Software Configuration<br>Series/Family SHE Security S: Standard Family SW Package, including:<br>3: K3 product family/ARM CortexM7 based N H TBD •  Real time driver including combined SDK &<br>Autosar MCAL (ISO26262, crypto driver<br>Core platform Fab and Mask rev letter included)<br>1: 1 x M7 Core •  Standard Security Firmware<br>2: 2 x M7 Cores Tx: Global Foundry<br>3: 3 x M7 Cores x0: 1 st  fab revision I: ISELED SW licensed + Standard Family SW<br>4: 1 x M7 lockstep core x1: 2 nd  fab revision Package<br>5: 1 x M7 lockstep core plus 1 x M7 core<br>Additional solution specific SW TBD<br>Temperature Suffix<br>Memory Size<br>V: -40 °C to 105 °C Tape and Reel Indicator<br>1 2 4 8 M: -40 °C to 125 °C<br>T: Trays/Tubes<br>P-Flash 1 MB 2 MB 4 MB 8 MB<br>R: Tape & Reel<br><!-- End of picture text -->

##### 4.1 Determining valid orderable parts 

To determine the orderable part numbers for this device, please contact NXP sales representative. 

#### 5 General 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

14 / 130 

NXP Semiconductors 

General 

##### 5.1 Absolute maximum ratings 

~~<mark>CAUTION</mark>~~ 

When the MCU is in an unpowered state, current injected through the chip pins may bias internal chip structures (for example, ESD diodes) and incorrectly power up these internal structures through inadvertent paths. The presence of such residual voltage may influence different chip-internal blocks in an unpredictable manner and may ultimately result in unpredictable chip behavior (for example, POR flag not set). Once in the illegal state, powering up the chip further and then applying reset will clear the illegal state. Injection current specified for the chip under the aspect of absolute maximum ratings represent the capability of the internal circuitry to withstand such condition without causing physical damage. Functional operation of the chip under conditions - specified as absolute maximum ratings - is not implied. 

~~<mark>NOTE</mark>~~ 

Functional operating conditions appear in the DC electrical characteristics. Absolute maximum ratings are stress ratings only, and functional operation at the maximum values is not guaranteed. See footnotes in the following table for specific conditions. Stress beyond the listed maximum values may affect device reliability or cause permanent damage to the device. All the limits defined in the datasheet specification must be honored together and any violation to any one or more will not guarantee desired operation. Unless otherwise specified, all maximum and minimum values in the datasheet are across process, voltage, and temperature. 

The VDD_HV_B and V15 voltage supply domains are only present in certain devices and packages (S32K358, S32K348, S32K338, S32K328, S32K344, S32K324, S32K314, S32K342, S32K341, S32K322). 

The VDD_DCDC supply voltage is only present in certain devices and packages (S32K358, S32K348, S32K338, S32K328). 

Table 2. Absolute maximum ratings 

|Symbol|Description|Min|Typ|Max|Unit||Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|---|
|VDD_HV_A|Main I/O and<br>analog supply<br>voltage<sup>1, 2</sup>|-0.3|—|6.0|V|—||—|
|VDD_HV_B|Secondary I/O<br>supply voltage<sup>1, 2</sup>|-0.3|—|6.0|V|—||—|
|VDD_DCDC|Supply voltage for<br>the SMPS gate<br>driver<sup>1, 2</sup>|-0.3|—|6.0|V|—||—|
|V15|High-current<br>logic supply<br>voltage<sup>1, 2</sup>|-0.3|—|6.0|V|—||—|
|V25|Flash memory<br>supply (2.5 V),<br>internally regulated<sup>1</sup>|-0.3|—|2.9|V|—||—|
|V11|Core logic<br>voltage supply<br>(1.1 V), internally<br>regulated<sup>1</sup>|-0.3|—|1.26|V|—||—|
|VREFH|ADC high reference<br>voltage<sup>1, 2</sup>|-0.3|—|6.0|V|—||—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

15 / 130 

NXP Semiconductors 

General 

Table 2. Absolute maximum ratings (continued) 

|Symbol|Description|Min|Typ|Max|Unit||Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|---|
|VREFL|ADC low reference<br>voltage<sup>1</sup>|-0.3|—|0.3|V|—||—|
|VGPIO_trans|Transient<br>overshoot voltage<br>allowed on I/<br>O pin<sup>1, 2, 3</sup>|-|—|6.0|V|—||—|
|I_INJPAD_DC_<br>ABS|Continuous DC<br>input current<br>(positive/negative)<br>that can be injected<br>into an I/O pin<sup>4</sup>|-3|—|3|mA|—||—|
|I_INJSUM_DC_<br>ABS|Sum of absolute<br>value of injected<br>currents on all the<br>I/O pins (continuous<br>DC limit)<sup>4</sup>|—|—|30|mA|—||—|
|TSTG|Storage ambient<br>temperature<sup>5</sup>|-55|—|150|°C|—||—|



1. All voltages are referred to VSS unless otherwise specified. 

2. 6.0 V maximum for 10 hours over lifetime; 7.0 V maximum for 60 seconds over lifetime. 

3. Absolute max rating must be honored under all conditions, including current injection. 

4. When input pad voltage levels are close to VDD_HV_A (respectively to VDD_HV_B) or VSS, practically no current injection is possible. See application note AN4731 for a description of injection current on NXP automotive microcontrollers. 

5. TSTG specifies the storage temperature range. It is not the operating temperature range. Please refer to the Thermal operating characteristics table. 

##### 5.2 Voltage and current operating requirements 

~~<mark>NOTE</mark>~~ 

Device functionality is guaranteed down to the LVR assert level, however electrical performance of 12-bit ADC, CMP with 8-bit DAC, IO electrical characteristics, and communication modules electrical characteristics will be degraded when voltage drops below 2.97 V. 

The VDD_HV_B and V15 voltage supply domains are only present in certain devices and packages (S32K358, S32K348, S32K338, S32K328, S32K344, S32K324, S32K314, S32K342, S32K341, S32K322). 

The VDD_DCDC supply voltage is only present in certain devices and packages (S32K358, S32K348, S32K338, S32K328). 

Table 3. Voltage and current operating requirements 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|VDD_HV_A|Main I/O and analog<br>supply voltage<sup>1</sup>|2.97|3.3 or 5.0|5.5|V|—|—|
|VDD_HV_B|Secondary I/O<br>supply voltage<sup>1</sup>|2.97|3.3 or 5.0|5.5|V|—|—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 Preliminary Information 

Data Sheet: Technical Data 

16 / 130 

NXP Semiconductors 

General 

Table 3. Voltage and current operating requirements (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|VDD_DCDC|Supply voltage for<br>the SMPS gate<br>driver<sup>1</sup>|2.97|3.3 or 5.0|5.5|V|—|—|
|V15|High-current logic<br>supply input<br>voltage<sup>1</sup>|1.425|1.5|1.65|V|—|—|
|V15_extended|High-current logic<br>supply input voltage,<br>extended range<sup>1, 2</sup>|1.425|3.3 or 5.0|5.5|V|—|—|
|VREFH|ADC high reference<br>voltage<sup>1, 3</sup>|2.97|3.3 or 5.0|5.5|V|—|—|
|VREFL|ADC low reference<br>voltage<sup>1</sup>|-0.1|0|0.1|V|—|—|
|VSS_DCDC|Power ground for the<br>SMPS gate driver<sup>1</sup>|-0.1|0|0.1|V|—|—|
|V25|Flash memory<br>and clock<br>supply (2.5 V),<br>internally regulated<sup>1</sup>|—|2.5|—|V|—|—|
|V11|Core logic supply<br>(1.1 V), internally<br>regulated<sup>1</sup>|—|1.14|—|V|—|—|
|VGPIO|Input voltage range<br>at any I/O or analog<br>pin<sup>1</sup>|-0.3|—|VDD_HV<br>_A/B +<br>0.3|V|—|—|
|VODPU|Open-drain pull-up<br>voltage<sup>1, 4</sup>|—|—|VDD_HV<br>_A/B|V|—|—|
|IINJPAD_DC_OP|Continuous DC input<br>current (positive/<br>negative) that can be<br>injected into an I/O<br>pin<sup>5</sup>|-3|—|3|mA|VDD_HV_A >= 3.6V|—|
|IINJPAD_DC_OP|Continuous DC input<br>current (positive/<br>negative) that can be<br>injected into an I/O<br>pin<sup>5</sup>|-2|—|3|mA|VDD_HV_A >= 2.97V|—|
|IINJSUM_DC_OP|Sum of<br>absolute value of<br>injected currents<br>on all the I/O|-30|—|30|mA|VDD_HV_A >= 3.6V|—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

17 / 130 

NXP Semiconductors 

General 

Table 3. Voltage and current operating requirements (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
||pins (continuous<br>DC limit)<sup>5</sup>|||||||
|IINJSUM_DC_OP|Sum of<br>absolute value of<br>injected currents<br>on all the I/O<br>pins (continuous<br>DC limit)<sup>5</sup>|-20|—|30|mA|VDD_HV_A >= 2.97V|—|
|Vramp_slow|Supply ramp rate<br>(slow)<sup>1, 6</sup>|0.5|—|—|V/min|—|—|
|Vramp_fast|Supply ramp rate<br>(fast)<sup>1, 6</sup>|—|—|100|V/ms|—|—|



1. All voltages are referred to VSS unless otherwise specified. 

2. If total power dissipation and maximum junction temperature allows. Please refer to Thermal operating characteristics table for the maximum junction temperature, and Thermal characteristics table for the thermal  characteristics, to determine the maximum power dissipation allowed for a given package. 

3. VREFH should always be equal to or less than VDD_HV_A +0.1. Any positive differential voltage between VREFH and VDD_HV_A i.e., VDD_HV_A < VREFH <= VDD_HV_A + 0.1V) is for RF-AC only. Appropriate decoupling capacitors should be used to filter noise on the supplies. See application note AN5032 for reference supply design for SAR ADC. 

4. Open-drain outputs must be pulled respectively to their supply rail (VDD_HV_A or VDD_HV_B). 

5. When input pad voltage levels are close to VDD_HV_A (respectively to VDD_HV_B) or VSS, practically no current injection is possible. 

6. The MCU supply ramp rate parameter must be applicable to the MCU input/external supplies. The ramp rate assumes that the S32K3xx HW design guidelines in ANxxxx (TBD) are followed. 

##### 5.3 Thermal operating characteristics 

Table 4. Thermal operating characteristics 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|Tamb|Ambient temperature|-40|—|125|°C|—|—|
|TJ|Junction<br>temperature|-40|—|150|°C|—|—|



##### 5.4 ESD and Latch-up Protection Characteristics 

Table 5. ESD and Latch-up Protection Characteristics 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|Vhbm|Electrostatic<br>discharge voltage,<br>human body model<br>(HBM)<sup>1, 2, 3</sup>|-2000|—|2000|V|—|—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 Preliminary Information 

Data Sheet: Technical Data 

18 / 130 

NXP Semiconductors 

Power management 

Table 5. ESD and Latch-up Protection Characteristics (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|Vcdm|Electrostatic<br>discharge voltage,<br>charged-device<br>model (CDM),<br>all pins except<br>corner<sup>1, 3, 4</sup>|-500|—|500|V|—|—|
|Vcdm|Electrostatic<br>discharge voltage,<br>charged-device<br>model (CDM), corner<br>pins<sup>1, 3, 4</sup>|-750|—|750|V|—|—|
|Ilat|Latch-up current at<br>ambient temperature<br>of 125°C<sup>5</sup>|-100|—|100|mA|—|—|



1. Device failure is defined as: "If after exposure to ESD pulses, the device does not meet specification requirements." 

2. This parameter is tested in conformity with AEC-Q100-002. 

3. All ESD testing conforms with AEC-Q100 Stress Test Qualification for Automotive Grade Integrated Circuits. 

4. This parameter is tested in conformity with AEC-Q100-011. 

5. This parameter is tested in conformity with AEC-Q100-004. 

#### 6 Power management 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

19 / 130 

NXP Semiconductors 

Power management 

##### 6.1 Power management system - S32K344, S32K324, S32K341, S32K314, S32K342, and S32K322. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0020-03.png)


<!-- Start of picture text -->
VC_BJT<br>Optional<br>COUT_V15<br>VDD_HV_A<br>Last Mile SOG Pads<br>distributed LPCMP_ n ADC_ n<br>(Standby)<br>LPM Boot FPM regulator GPIO<br>PMC<br>SOG<br>V11_STANDBY (Run)<br>V11_STANDBY<br>VSS<br>SW*<br>V25 32 K B<br>SRAM VDD_HV_B<br>SIRC FIRC SXOSC<br>Pads<br>V11_RUN<br>GPIO<br>Registers V11_STANDBY<br>FXOSC<br>PIT_0<br>MC_RGM<br>(RTI) VSS<br>Flash<br>memory WKPU RTC<br>PLLDIG<br>MC_PCU DCM<br>TempSense<br>(Double bond) (Double bond)<br>- Standby domain<br>- Standby domain (optional)<br>SW* - On during FPM (Run mode) only<br>VDD_HV_B VDD_HV_A VRC_CTRL V15 VREFH VREFL<br>VSS V25 V11<br><!-- End of picture text -->

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

20 / 130 

NXP Semiconductors 

Power management 

##### 6.2 Power management system - S32K312, S32K311 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0021-03.png)


<!-- Start of picture text -->
VDD_HV_A<br>SOG Pads<br>LPCMP_ n ADC_ n<br>(Standby)<br>FPM LPM GPIO<br>PMC<br>SOG<br>(Run)<br>V11_STANDBY<br>VSS<br>SW*<br>V25 32 K B<br>SRAM<br>SIRC FIRC SXOSC<br>Not available<br>V11_RUN in the S32K311<br>Registers V11_STANDBY<br>FXOSC<br>PIT_0<br>MC_RGM<br>(RTI)<br>Flash<br>memory WKPU RTC<br>PLLDIG<br>MC_PCU DCM<br>TempSense<br>(Double bond) (Double bond)<br>- Standby domain<br>- Standby domain (optional)<br>SW* - On during FPM (Run mode) only<br>VDD_HV_A VREFH VREFL<br>VSS V25 V11<br><!-- End of picture text -->

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

21 / 130 

NXP Semiconductors 

Power management 

##### 6.3 Power management system - S32K358 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0022-03.png)


<!-- Start of picture text -->
optional [See footnotes]<br>VIN<br>VC_BJT<br>COUT_V15<br>optional<br>[See footnotes]<br>VDD_HV_A<br>LPM (V15)<br>Last Mile SOG<br>SMPS distributed LPCMP_ n ADC_ n Pads<br>(Standby)<br>regulator GPIO<br>PMC LPM FPM<br>SOG<br>V11_STANDBY V11_STANDBY (Run) VSS<br>SW*<br>V25 64 kB<br>VDD_HV_B<br>SRAM<br>SIRC FIRC SXOSC Pads<br>GPIO<br>V11_RUN<br>Registers V11_STANDBY<br>VSS<br>FXOSC<br>PIT_0<br>MC_RGM<br>Flash PLLDIG0 (RTI)<br>memory<br>WKPU RTC<br>TempSense<br>MC_PCU DCM<br>PLLDIG1<br>(Triple bond) (Triple bond)<br>- Standby domain<br>- Standby domain (optional)<br>SW* - On during FPM (Run mode) only<br>The V15 input voltage can be supplied directly by an SBC or Voltage regulator. The S32K3x8 devices provide two options to derive the V15 regulator from the 5V or 3.3V supply.<br>Option 1: A DC/DC converter (SMPS) regulator can be implemented by connecting the external components (PMOS, inductor, diode) shown in the figure above, at pins VDD_DCDC,<br>PMOS_CTRL, and VSS_DCDC. In this case, VRC_CTRL must not be connected. VDD_DCDC must be connected to the VDD_HV_A or VDD_HV_B, supply voltage. In this<br>option, COUT_V15 is specified in SMPS regulator electrical specifications.<br>Option 2: A linear regulator can be implemented by connecting a bipolar NPN transistor from the VDD_HV_A or VDD_HV_B, supply voltage shown as VC_BJT in the figure above. The<br>VRC_CTRL pin must be connected to the base of the transistor. In this case, VDD_DCDC, PMOS_CTRL must not be connected. VSS_DCDC must be connected to MCU GND.<br>In this option, COUT_V15 is specified in Recommended decoupling capacitors.<br>VDD_HV_B VDD_DCDC PGATE_CTRL VSS_DCDC VDD_HV_A VRC_CTRL V15 VREFH VREFL<br>VSS V25 V11<br><!-- End of picture text -->

##### 6.4 Power mode transition operating behaviors 

###### 6.4.1 Power mode transition operating behaviour 

The values in the table below are provided for reference only. 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

22 / 130 

NXP Semiconductors 

Power management 

Table 6. Power mode transition operating behaviour 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|tMODE_<br>STDBYENTRY|RUN --> STANDBY<br>transition time|—|955|—|ns|—|—|
|tMODE_<br>STDBYEXIT_FAST|STANDBY --> RUN<br>transition time, fast<br>standby exit|—|53|—|us|—|—|
|tMODE_<br>STDBYEXIT|STANDBY --> RUN<br>transition time,<br>normal standby exit|—|TBD|—|us|—|—|



###### 6.4.2 Boot time, HSE firmware not installed 

Table 7. Boot time, HSE firmware not installed 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|tBOOT_noHSE|After a POR event,<br>amount of time to<br>execution of the<br>first instruction of<br>the application core,<br>when HSE firmware<br>is not installed. (HSE<br>FW feature flag is<br>disabled)|—|2|—|ms|FIRC 48MHz|—|



###### 6.4.3 Boot time, HSE firmware installed 

The following table provides the boot time of the S32K3 SBAF and Firmware initialization. To obtain the total boot time, the corresponding user code verification time must be added. 

Table 8. Boot time, HSE firmware installed 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|tBOOT_HSE_<br>NONSECURE|After a POR event,<br>amount of time to<br>execution of the<br>first instruction of<br>the application core,<br>when HSE firmware<br>is installed BOOT<br>SEQ = 0 Default<br>configuration:<br>CORE_CLK @ 48<br>MHz (source = FIRC|—|—|3|ms|—|—|
|tBOOT_HSE|After a POR event,<br>amount of time to|—|12.36|—|ms|—|—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

23 / 130 

NXP Semiconductors 

Power management 

Table 8. Boot time, HSE firmware installed (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
||execution of the<br>first instruction of<br>the application core,<br>when HSE firmware<br>is installed. Default<br>configuration:<br>CORE_CLK @ 48<br>MHz (source =<br>FIRC)|||||||
|tBOOT_HSE|After a POR event,<br>amount of time to<br>execution of the<br>first instruction of<br>the application core,<br>when HSE firmware<br>is installed. Optional<br>configuration:<br>CORE_CLK @ 120<br>MHz (source = PLL)|—|9.51|—|ms|—|—|
|tBOOT_HSE|After a POR event,<br>amount of time to<br>execution of the<br>first instruction of<br>the application core,<br>when HSE firmware<br>is installed. Optional<br>configuration:<br>CORE_CLK @<br>80 MHz (source =<br>PLL)|—|10.91|—|ms|—|—|



###### 6.4.4 HSE firmware memory verification time examples 

Table 9. HSE firmware memory verification time examples 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|tCMAC_64KB|Memory verification<br>of 64 KB of<br>application firmware,<br>using AES-128<br>CMAC cipher.|—|11.3|—|ms|FIRC 48MHz|—|
|tCMAC_1024KB|Memory verification<br>of 1024 KB of<br>application firmware,<br>using AES-128<br>CMAC cipher.|—<br>Table co|176<br>ntinues on|—<br>the next pa|ms<br>ge...|FIRC 48MHz|—|



S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

24 / 130 

NXP Semiconductors 

Power management 

Table 9. HSE firmware memory verification time examples (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|tGMAC_64KB|Memory verification<br>of 64 KB of<br>application firmware,<br>using AES-128<br>GMAC cipher.|—|3.2|—|ms|FIRC 48MHz|—|
|tGMAC_1024KB|Memory verification<br>of 1024 KB of<br>application firmware,<br>using AES-128<br>GMAC cipher.|—|46.8|—|ms|FIRC 48MHz|—|
|tHMAC_64KB|Memory verification<br>of 64 KB of<br>application firmware,<br>using AES-128<br>HMAC cipher.|—|1.74|—|ms|FIRC 48MHz|—|
|tHMAC_1024KB|Memory verification<br>of 1024 KB of<br>application firmware,<br>using AES-128<br>HMAC cipher.|—|22.87|—|ms|FIRC 48MHz|—|
|tRSA_64KB|Memory verification<br>of 64 KB of<br>application firmware,<br>using RSA 2048<br>cipher.|—|30.47|—|ms|FIRC 48MHz|—|
|tRSA_1024KB|Memory verification<br>of 1024 KB of<br>application firmware,<br>using RSA 2048<br>cipher.|—|51.6|—|ms|FIRC 48MHz|—|
|tECDSA_64KB|Memory verification<br>of 64 KB of<br>application firmware,<br>using ECDSA 521<br>bits cipher.|—|38.45|—|ms|FIRC 48MHz|—|
|tECDSA_1024KB|Memory verification<br>of 1024 KB of<br>application firmware,<br>using ECDSA 521<br>bits cipher.|—|59.56|—|ms|FIRC 48MHz|—|
|tSHA2_256_64KB|Memory verification<br>of 64 KB of<br>application firmware,|—|1.62|—|ms|FIRC 48MHz|—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

25 / 130 

NXP Semiconductors 

Power management 

Table 9. HSE firmware memory verification time examples (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
||using SHA2 256 bits<br>bits cipher.|||||||
|tSHA2_256_<br>1024KB|Memory verification<br>of 1024 KB of<br>application firmware,<br>using SHA2 256 bits<br>bits cipher.|—|22.73|—|ms|FIRC 48MHz|—|
|tCMAC_64KB|Memory verification<br>of 64 KB of<br>application firmware,<br>using AES-128<br>CMAC cipher.|—|6.7|—|ms|PLL 80MHz|—|
|tCMAC_1024KB|Memory verification<br>of 1024 KB of<br>application firmware,<br>using AES-128<br>CMAC cipher.|—|104.8|—|ms|PLL 80MHz|—|
|tGMAC_64KB|Memory verification<br>of 64 KB of<br>application firmware,<br>using AES-128<br>GMAC cipher.|—|1.9|—|ms|PLL 80MHz|—|
|tGMAC_1024KB|Memory verification<br>of 1024 KB of<br>application firmware,<br>using AES-128<br>GMAC cipher.|—|28|—|ms|PLL 80MHz|—|
|tHMAC_64KB|Memory verification<br>of 64 KB of<br>application firmware,<br>using AES-128<br>HMAC cipher.|—|1.01|—|ms|PLL 80MHz|—|
|tHMAC_1024KB|Memory verification<br>of 1024 KB of<br>application firmware,<br>using AES-128<br>HMAC cipher.|—|13.65|—|ms|PLL 80MHz|—|
|tRSA_64KB|Memory verification<br>of 64 KB of<br>application firmware,<br>using RSA 2048<br>cipher.|—|16.72|—|ms|PLL 80MHz|—|
|tRSA_1024KB|Memory verification<br>of 1024 KB of|—|34.19|—|ms|PLL 80MHz|—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

26 / 130 

NXP Semiconductors 

Power management 

Table 9. HSE firmware memory verification time examples (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
||application firmware,<br>using RSA 2048<br>cipher.|||||||
|tECDSA_64KB|Memory verification<br>of 64 KB of<br>application firmware,<br>using ECDSA 521<br>bits cipher.|—|21.58|—|ms|PLL 80MHz|—|
|tECDSA_1024KB|Memory verification<br>of 1024 KB of<br>application firmware,<br>using ECDSA 521<br>bits cipher.|—|27.19|—|ms|PLL 80MHz|—|
|tSHA2_256_64KB|Memory verification<br>of 64 KB of<br>application firmware,<br>using SHA2 256 bits<br>bits cipher.|—|0.94|—|ms|PLL 80MHz|—|
|tSHA2_256_<br>1024KB|Memory verification<br>of 1024 KB of<br>application firmware,<br>using SHA2 256 bits<br>bits cipher.|—|13.59|—|ms|PLL 80MHz|—|
|tCMAC_64KB|Memory verification<br>of 64 KB of<br>application firmware,<br>using AES-128<br>CMAC cipher.|—|4.5|—|ms|PLL 120MHz|—|
|tCMAC_1024KB|Memory verification<br>of 1024 KB of<br>application firmware,<br>using AES-128<br>CMAC cipher.|—|69.9|—|ms|PLL 120MHz|—|
|tGMAC_64KB|Memory verification<br>of 64 KB of<br>application firmware,<br>using AES-128<br>GMAC cipher.|—|1.3|—|ms|PLL 120MHz|—|
|tGMAC_1024KB|Memory verification<br>of 1024 KB of<br>application firmware,<br>using AES-128<br>GMAC cipher.|—|18.7|—|ms|PLL 120MHz|—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

27 / 130 

NXP Semiconductors 

Power management 

Table 9. HSE firmware memory verification time examples (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|tHMAC_64KB|Memory verification<br>of 64 KB of<br>application firmware,<br>using AES-128<br>HMAC cipher.|—|0.7|—|ms|PLL 120MHz|—|
|tHMAC_1024KB|Memory verification<br>of 1024 KB of<br>application firmware,<br>using AES-128<br>HMAC cipher.|—|9.12|—|ms|PLL 120MHz|—|
|tRSA_64KB|Memory verification<br>of 64 KB of<br>application firmware,<br>using RSA 2048<br>cipher.|—|15.4|—|ms|PLL 120MHz|—|
|tRSA_1024KB|Memory verification<br>of 1024 KB of<br>application firmware,<br>using RSA 2048<br>cipher.|—|23.8|—|ms|PLL 120MHz|—|
|tECDSA_64KB|Memory verification<br>of 64 KB of<br>application firmware,<br>using ECDSA 521<br>bits cipher.|—|19.42|—|ms|PLL 120MHz|—|
|tECDSA_1024KB|Memory verification<br>of 1024 KB of<br>application firmware,<br>using ECDSA 521<br>bits cipher.|—|27.81|—|ms|PLL 120MHz|—|
|tSHA2_256_64KB|Memory verification<br>of 64 KB of<br>application firmware,<br>using SHA2 256 bits<br>bits cipher.|—|0.64|—|ms|PLL 120MHz|—|
|tSHA2_256_<br>1024KB|Memory verification<br>of 1024 KB of<br>application firmware,<br>using SHA2 256 bits<br>bits cipher.|—|9.07|—|ms|PLL 120MHz|—|



S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

28 / 130 

NXP Semiconductors 

Power management 

##### 6.5 Supply Monitoring 

Table 10. Supply Monitoring 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|LVD_V15|Low Voltage Detect<br>(LVD) on V15,<br>deassert threshold<br>(in FPM)|1.34|1.38|1.42|V|—|—|
|HVD_V15|High Voltage Detect<br>(HVD) on V15,<br>assert threshold (in<br>FPM)|—|2.5|—|V|—|—|
|LVR_VDD_HV_A|LVR on VDD_HV_A,<br>assert threshold (in<br>FPM)|2.77|2.85|2.93|V|—|—|
|LVR_VDD_HV_A|LVR on VDD_HV_A,<br>assert threshold (in<br>RPM)|2.77|2.85|2.93|V|—|—|
|—|VDD_HV_A LVR<br>monitor hysteresis|—|18.75|—|mV|—|—|
|HVD_VDD_HV_A|HVD on VDD_HV_A,<br>assert threshold (in<br>FPM)|5.787|5.887|5.987|V|—|—|
|—|VDD_HV_A HVD<br>monitor hysteresis|—|37.5|—|mV|—|—|
|LVR_VDD_HV_B|LVR on VDD_HV_B,<br>assert threshold (in<br>FPM)|2.77|2.85|2.93|V|—|—|
|LVR_VDD_HV_B|LVR on VDD_HV_B,<br>assert threshold (in<br>RPM)|2.77|2.85|2.93|V|—|—|
|—|VDD_HV_B LVR<br>monitor hysteresis|—|18.75|—|mV|—|—|
|HVD_VDD_HV_B|HVD on VDD_HV_B,<br>assert threshold (in<br>FPM)|5.787|5.887|5.987|V|—|—|
|—|VDD_HV_B HVD<br>monitor hysteresis|—|37.5|—|mV|—|—|
|LVD_VDD_HV_A|Low Voltage<br>Detect (LVD5A) on<br>VDD_HV_A, assert<br>threshold (in FPM)|4.33|4.41|4.49|V|—|—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

29 / 130 

NXP Semiconductors 

Power management 

Table 10. Supply Monitoring (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|—|VDD_HV_A<br>LVD monitor<br>hysteresis|—|37.5|—|mV|—|—|
|VPOR_VDD_HV_A|Power-On-Reset<br>(VPOR) on<br>VDD_HV_A,<br>deassert threshold|0.9|1.5|2.2|V|—|—|
|VREF12|Bandgap reference,<br>trimmed|1.18|1.2|1.22|V|—|—|



##### 6.6 SMPS regulator electrical specifications 

The chip hardware design guidelines document lists the recommended part numbers for PMOS & Schottky diode. 

Table 11. SMPS regulator electrical specifications 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|V15|V15 output|—|1.51|—|V|—|—|
|—|External coil<br>inductance|—|4.7|—|uH|—|—|
|COUT_V15_SMPS|External bypass<br>capacitor|—|20-22|—|uF|—|—|
|—|External Schottky<br>diode|—|TBD|—|—|—|—|
|VR|Schottky diode<br>reverse voltage|5.0|—|—|V|—|—|
|IF|Schottky diode<br>forward current|1.0|—|—|A|—|—|
|—|External P-channel<br>MOSFET total gate<br>charge|—|—|10|nC|VDD_DCDC = 5V|—|
|—|External P-channel<br>MOSFET threshold<br>voltage|—|—|TBD|mV|—|—|



S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

30 / 130 

NXP Semiconductors 

Power management 

##### 6.7 Recommended Decoupling Capacitors 

Table 12. Recommended Decoupling Capacitors 

|Symbol|Description|Min|Typ|Max|Unit||Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|---|
|CDEC|Decoupling capacitor<br>(one per supply<br>pin)<sup>1, 2, 3</sup>|70|100|-|nF|—||—|
|CBULK|Input supply bulk<br>capacitor<sup>2, 4, 5, 6</sup>|-|4.7|-|µF|—||—|
|COUT_V15_NPN|V15 (1.5V<br>Regulator) output<br>capacitor<sup>2, 7</sup>|-|2.2|-|µF|—||—|
|COUT_V11|V11 (1.1V<br>Regulator)<br>output capacitor<br>(all chips, except<br>S32K312 &<br>S32K311)<sup>2</sup>|-|2.2|-|µF|—||—|
|COUT_V11|V11 (1.1V<br>Regulator)<br>output capacitor<br>(S32K312 &<br>S32K311)<sup>2</sup>|-|1|-|µF|—||—|
|COUT_V25|V25 (2.5V<br>Regulator) output<br>capacitor<sup>2, 3</sup>|140|220|-|nF|—||—|



1. Optionally, 1 nF capacitors can be added in parallel to the decoupling capacitors. 

2. All capacitors must be low ESR ceramic capacitors (for example, X7R).  The minimum recommendation is after considering component aging and tolerance. 

3. These capacitors must be placed as close as possible to the corresponding supply and ground pins. For BGA packages, the capacitors must be placed on the other side of the PCB to minimize the trace lengths. 

4. For devices where the VDD_HV_B domain is present, if the VDD_HV_B supply is different supply from VDD_HV_A, a dedicated bulk capacitor is needed. 

5. It is also possible to use higher capacitance values (for example, 10 μF) in place of the 4.7 μF capacitor. 

6. These capacitors must be placed close to the source. 

7. For devices where V15 is present, the V15 regulator output capacitor and the filter capacitors are required when using an NPN bipolar ballast transistor for the regulation stage. When V15 is supplied from an external regulator, these capacitance recommendations can be followed in addition to the capacitance requirements of the external voltage regulator. 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

31 / 130 

NXP Semiconductors 

Power management 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0032-02.png)


<!-- Start of picture text -->
S32K311<br>48LQFP<br>V25<br>6 V25<br>COUT_V25<br>V11<br>7 V11<br>VREFL 4<br>COUT11<br>VSS 8<br>VSS 30<br>VDD_HV_A<br>5 VDD_HV_A<br>31 VDD_HV_A<br>CBULK CDEC<br>VREFH<br>3 VREFH<br>CDEC<br><!-- End of picture text -->

Figure 14. 48-pin LQFP decoupling capacitor pinout diagram (S32K311) 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

32 / 130 

NXP Semiconductors 

Power management 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0033-02.png)


<!-- Start of picture text -->
S32K312<br>S32K311<br>100MAXQFP<br>V25<br>11 V25<br>COUT_V25<br>V11<br>13 V11<br>60 V11<br>COUT_V11 CDEC<br>VREFL 9<br>VSS<br>VDD_HV_A 12<br>VSS<br>14<br>10 VDD_HV_A VSS<br>16<br>37 VDD_HV_A VSS<br>CBULK CDEC CDEC CDEC 6 2 VDD_HV_A VSS 38<br>87 VDD_HV_A VSS 61<br>VSS 86<br>VREFH<br>8 VREFH<br>CDEC<br><!-- End of picture text -->

Figure 15. 100-pin MaxQFP decoupling capacitor pinout diagram (S32K312) 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

33 / 130 

NXP Semiconductors 

Power management 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0034-02.png)


<!-- Start of picture text -->
S32K342<br>100MAXQFP<br>V25<br>11 V25<br>COUT_V25<br>V11<br>13 V11<br>60 V11<br>COUT_V11 CDEC<br>VREFL 9<br>VSS<br>14<br>VSS<br>V15 16<br>VSS<br>24<br>12 V15 VSS<br>59 V15 VSS 38<br>COUT_V15_NPN CDEC CDEC VSS 61<br>VSS 8 6<br>V15<br>BJT option<br>NPN 7 VRC_CTRL<br>VDD_HV_NPN<br>VDD_HV_B<br>25 VDD_HV_B<br>CBULK CDEC 37 VDD_HV_B<br>VDD_HV_A<br>10 VDD_HV_A<br>CBULK CDEC CDEC 6 2 VDD_HV_A<br>87 VDD_HV_A<br>VREFH<br>8 VREFH<br>CDEC<br><!-- End of picture text -->

Figure 16. 100-pin MaxQFP decoupling capacitor pinout diagram (S32K342) S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

34 / 130 

NXP Semiconductors 

Power management 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0035-02.png)


<!-- Start of picture text -->
S32K312<br>172MAXQFP<br>V25<br>19 V25<br>COUT_V25<br>V11<br>21 V11<br>5 9 V11<br>COUT_V11 CDEC CDEC CDEC<br>1 06 V11 VREFL 17<br>149 V11<br>VSS 22<br>VSS 24<br>VDD_HV_A VSS 37<br>18 VDD_HV_A VSS 58<br>CBULK CDEC CDEC CDEC CDEC CDEC 3 8 VDD_HV_A VSS 78<br>5 7 VDD_HV_A VSS 107<br>77 VDD_HV_A VSS 127<br>VDD_HV_A VSS 150<br>108<br>VDD_HV_A VSS 168<br>128<br>VDD_HV_A<br>151<br>VDD_HV_A<br>1 69 VDD_HV_A<br>VREFH<br>16 VREFH<br>CDEC<br>Figure 17. 172-pin MaxQFP decoupling capacitor pinout diagram (S32K312)<br><!-- End of picture text -->

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

35 / 130 

NXP Semiconductors 

Power management 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0036-02.png)


<!-- Start of picture text -->
S32K344<br>S32K342<br>172MAXQFP<br>V25<br>19 V25<br>COUT_V25<br>V11<br>21 V11<br>5 9 V11<br>COUT_V11 CDEC CDEC CDEC<br>1 06 V11 VREFL 17<br>149 V11<br>VSS 22<br>VSS 24<br>V15<br>VSS 37<br>2 0 V15 VSS 58<br>6 0 V15 VSS 78<br>COUT_V15_NPN CDEC CDEC CDEC<br>1 05 V15 VSS 107<br>148 V15 VSS 127<br>VSS 150<br>VSS 168<br>V15<br>RBCT15<br>BJT option<br>QNPN15 11 VRC_CTRL<br>VDD_HV_NPN<br>VDD_HV_B<br>38 VDD_HV_B<br>CBULK CDEC CDEC 5 7 VDD_HV_B<br>77 VDD_HV_B<br>VDD_HV_A<br>18 VDD_HV_A<br>CBULK CDEC CDEC 1 08 VDD_HV_A<br>1 28 VDD_HV_A<br>1 51 VDD_HV_A<br>169 VDD_HV_A<br>VREFH<br>16 VREFH<br>CDEC<br>Figure 18. 172-pin MaxQFP decoupling capacitor pinout diagram (S32K342, S32K344)<br><!-- End of picture text -->

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

36 / 130 

NXP Semiconductors 

Power management 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0037-02.png)


<!-- Start of picture text -->
S32K358<br>172MAXQFP<br>V25<br>19 V25<br>COUT_V25<br>V11<br>21 V11<br>5 9 V11<br>COUT_V11 CDEC CDEC CDEC 1 06 V11 VREFL 17<br>149 V11<br>VSS_DCDC 26<br>VSS 22<br>VSS 24<br>V15<br>VSS 37<br>20 V15 VSS 58<br>COUT_V15_NPN CDEC CDEC CDEC CDEC CDEC 3 6 V15 VSS 78<br>6 0 V15 VSS<br>10<br>7 9 V15 VSS<br>1 05 V15 VSS 71<br>148 V15 VSS 27<br>VSS 150<br>VSS 168<br>V15<br>BJT option<br>NPN 11 VRC_CTRL<br>VDD_HV_NPN<br>27 PMOS_CTRL<br>28 VDD_DCDC<br>VDD_HV_B<br>38 VDD_HV_B<br>CBULK CDEC CDEC CDEC 5 7 VDD_HV_B<br>77 VDD_HV_B<br>VDD_HV_A<br>18 VDD_HV_A<br>CBULK CDEC CDEC CDEC 1 08 VDD_HV_A<br>1 28 VDD_HV_A<br>1 51 VDD_HV_A<br>169 VDD_HV_A<br>VREFH<br>16 VREFH<br>CDEC<br>Figure 19. 172-pin MaxQFP decoupling capacitor pinout diagram (S32K358)<br><!-- End of picture text -->

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

37 / 130 

NXP Semiconductors 

Power management 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0038-02.png)


<!-- Start of picture text -->
S32K358<br>172MAXQFP<br>V25<br>19 V25<br>COUT_V25<br>V11<br>21 V11<br>5 9 V11<br>COUT_V11 CDEC CDEC CDEC 1 06 V11 VREFL 17<br>149 V11<br>VSS_DCDC 26<br>VSS 22<br>VSS 24<br>V15<br>VSS 37<br>20 V15 VSS 58<br>3 6 V15 VSS<br>CDEC CDEC CDEC CDEC CDEC CDEC 78<br>6 0 V15 VSS<br>10<br>7 9 V15 VSS<br>1 05 V15 VSS 71<br>148 V15 VSS 27<br>VSS 150<br>VDD_HV_SMPS SMPS option VSS 168<br>Q_SMPS L_SMPS V15<br>D_SMPS COUT_V15_SMPS<br>11 VRC_CTRL<br>27 PMOS_CTRL<br>28 VDD_DCDC<br>VDD_HV_B<br>38 VDD_HV_B<br>CBULK CDEC CDEC CDEC 5 7 VDD_HV_B<br>77 VDD_HV_B<br>VDD_HV_A<br>1 8 VDD_HV_A<br>CBULK CDEC CDEC CDEC 1 08 VDD_HV_A<br>1 28 VDD_HV_A<br>1 51 VDD_HV_A<br>169 VDD_HV_A<br>VREFH<br>16 VREFH<br>CDEC<br>Figure 20. 172-pin MaxQFP decoupling capacitor pinout diagram (S32K358_SMPS)<br><!-- End of picture text -->

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

38 / 130 

NXP Semiconductors 

Power management 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0039-02.png)


<!-- Start of picture text -->
S32K358<br>289MBGA<br>V25<br>J7 V25<br>COUT_V25<br>V11<br>H9 V11<br>J8 V11<br>COUT_V11 CDEC CDEC CDEC J10 V11 VREFL J6<br>K9 V11<br>VSS_DCDC J5<br>VSS B2<br>VSS B16<br>V15<br>VSS D4<br>E9 V15 VSS D9<br>COUT_V15_NPN CDEC CDEC CDEC CDEC CDEC H8 V15 VSS E13<br>H10 V15 VSS G7<br>J13 V15 VSS G11<br>K8 V15 VSS J1<br>K10 V15 VSS J4<br>N6 V15 VSS J9<br>N8 V15 VSS J14<br>VSS L7<br>V15 VSS L11<br>VSS M5<br>VSS N7<br>BJT option VSS N10<br>NPN F1 VRC_CTRL VSS P4<br>VDD_HV_NPN VSS P14<br>VSS T2<br>K5 PMOS_CTRL VSS T7<br>L5 VDD_DCDC VSS T10<br>VSS T16<br>VDD_HV_B<br>N4 VDD_HV_B<br>CBULK CDEC CDEC R7 VDD_HV_B<br>R10 VDD_HV_B<br>VDD_HV_A<br>D14 VDD_HV_A<br>CBULK CDEC CDEC CDEC CDEC CDEC CDEC E5 VDD_HV_A<br>G10 VDD_HV_A<br>H7 VDD_HV_A<br>H13 VDD_HV_A<br>K11 VDD_HV_A<br>L8 VDD_HV_A<br>N5 VDD_HV_A<br>N9 VDD_HV_A<br>VREFH<br>H6 VREFH<br>CDEC<br>Figure 21. 289BGA package decoupling capacitor pinout diagram (S32K358)<br><!-- End of picture text -->

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

39 / 130 

NXP Semiconductors 

Power management 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0040-02.png)


<!-- Start of picture text -->
S32K358<br>289MBGA<br>V25<br>J7 V25<br>COUT_V25<br>V11<br>H9 V11<br>J8 V11<br>COUT_V11 CDEC CDEC CDEC J10 V11 VREFL J6<br>K9 V11<br>VSS_DCDC J5<br>VSS B2<br>VSS B16<br>V15<br>VSS D4<br>E9 V15 VSS D9<br>CDEC CDEC CDEC CDEC CDEC H8 V15 VSS E13<br>H10 V15 VSS G7<br>J13 V15 VSS G11<br>K8 V15 VSS J1<br>K10 V15 VSS J4<br>N6 V15 VSS J9<br>N8 V15 VSS J14<br>VSS L7<br>VDD_HV_SMPS Q_SMPS L_SMPS V15 SMPS option VSS L11<br>VSS M5<br>VSS N7<br>VSS N10<br>D_SMPS COUT_V15_SMPS F1 VRC_CTRL VSS P4<br>VSS P14<br>VSS T2<br>VSS T7<br>VSS T10<br>K5 PMOS_CTRL VSS T16<br>L5 VDD_DCDC<br>VDD_HV_B<br>N4 VDD_HV_B<br>CBULK CDEC CDEC R7 VDD_HV_B<br>R10 VDD_HV_B<br>VDD_HV_A<br>D14 VDD_HV_A<br>CBULK CDEC CDEC CDEC CDEC CDEC CDEC E5 VDD_HV_A<br>G10 VDD_HV_A<br>H7 VDD_HV_A<br>H13 VDD_HV_A<br>K11 VDD_HV_A<br>L8 VDD_HV_A<br>N5 VDD_HV_A<br>N9 VDD_HV_A<br>VREFH<br>H6 VREFH<br>CDEC<br>Figure 22. 289BGA package decoupling capacitor pinout diagram (S32K358_SMPS)<br><!-- End of picture text -->

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

40 / 130 

NXP Semiconductors 

Power management 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0041-02.png)


<!-- Start of picture text -->
S32K344<br>257MBGA<br>V25<br>J7 V25<br>COUT_V25<br>H9 V11<br>J8 V11<br>COUT_V11 CDEC CDEC CDEC J10 V11 VREFL J6<br>K9 V11<br>VSS B2<br>VSS B16<br>V15<br>VSS D4<br>H8 V15 VSS D9<br>COUT_V15_NPN CDEC CDEC H10 V15 VSS G7<br>K8 V15 VSS G11<br>K10 V15 VSS J1<br>VSS J4<br>VSS J9<br>VSS J14<br>VSS L7<br>VSS L11<br>V15 VSS P4<br>VSS P14<br>VSS T2<br>BJT option<br>VSS T7<br>NPN F1 VRC_CTRL VSS T10<br>VDD_HV_NPN<br>VSS T16<br>VDD_HV_B<br>N4 VDD_HV_B<br>CBULK CDEC CDEC R7 VDD_HV_B<br>R10 VDD_HV_B<br>VDD_HV_A<br>D14 VDD_HV_A<br>CBULK CDEC CDEC CDEC G10 VDD_HV_A<br>H7 VDD_HV_A<br>K11 VDD_HV_A<br>L8 VDD_HV_A<br>VDD_HV_A<br>VREFH<br>H6 VREFH<br>CDEC<br>V11<br><!-- End of picture text -->

Figure 23. 257BGA package decoupling capacitor pinout diagram (S32K344) S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

41 / 130 

NXP Semiconductors 

Power management 

##### 6.8 NPN Ballast Transistor Control Specification 

Table 13. NPN Ballast Transistor Control Specification 

|Symbol|Description|Min|Typ|Max|Unit<br>Condition|Spec<br>Number|
|---|---|---|---|---|---|---|
|V15|V15 output|—|1.51|—|V<br>—|—|
|IBCTL|IBCTL (V15 reg)<br>source|10|—|—|mA<br>—|—|
|IBCTL|IBCTL (V15 reg) sink|—|—|-50|uA<br>—|—|
|tsettle_lm|Required setting<br>time from activating<br>last mile regulator to<br>load change|2|—|—|us<br>—|—|
|VDD_HV_NPN|Input voltage supply<br>for NPN external<br>ballast transistor|2.5|3.3 or 5|—|V<br>—|—|
|VD|D_HV_NPN|Q_V1<br>_Externa_<br>_Ballast_|5_NPN<br>_l NPN_<br>_Transistor_||V15<br>_High-current_<br>_Logic supply_||
||_BJT option_|||R_V15_<br>2.2k|COUT_V15_NPN<br>NPN<br>2.2uF||
|||PTE13 ||VRC_CTRL||||
|Figure 24. Ballast|circuit||||||



##### 6.9 Supply currents 

~~<mark>NOTE</mark>~~ All data in this table is preliminary and based on first samples. 

Typical current numbers are indicative for typical silicon process and may vary based on the silicon distribution and user configuration. Typical conditions assumes VDD_HV_A = VREFH = 5 V, VDD_HV_B = 5V (if the VDD_HV_B domain present in the device), temperature = 25 °C, and typical silicon process unless otherwise stated. In STANDBY configuration, no current flows through the V15 supply. 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

42 / 130 

###### Table 14. STANDBY mode supply currents 

||||ST|ANDBY<sup>1</sup>||
|---|---|---|---|---|---|
||||VDD_HV_A<sup>2</sup>||VDD_HV_B<sup>2</sup>|
|Chip|Ambient Temperature (°C)|All clocks & peripherals OFF<br>(µA)|SIRC ON<br>(µA)|FIRC ON (24 MHz)<br>(mA)|All Config.<br>(µA)|
|S32K358, S32K348,<br>|25, typ<sup>3</sup>|75|78|0.98|TBD|
|S32K338, S32K328|25, max<sup>4</sup>|TBD|TBD|TBD|TBD|
||85, typ<sup>3</sup>|TBD|TBD|TBD|TBD|
||85, max<sup>4</sup>|TBD|TBD|TBD|TBD|
||105, typ<sup>3</sup>|TBD|TBD|TBD|TBD|
||105, max<sup>4</sup>|TBD|TBD|TBD|TBD|
||125, typ<sup>3</sup>|TBD|TBD|TBD|TBD|
||125, max<sup>4</sup>|TBD|TBD|TBD|TBD|
|S32K344,<br>|25, typ<sup>3</sup>|50|52|0.91|1.8|
|S32K324, S32K314|25, max<sup>4</sup>|153|153|1.05|3.8|
||85, typ<sup>3</sup>|315|316|1.18|6.1|
||85, max<sup>4</sup>|900|910|1.78|15.4|



Table continues on the next page... 

Table 14. STANDBY mode supply currents (continued) 

|105, typ<sup>3</sup>|498|530|1.40|8.5|
|---|---|---|---|---|
|105, max<sup>4</sup>|1672|1682|2.55|26.2|
|125, typ<sup>3</sup>|932|998|1.88|18.5|
|125, max<sup>4</sup>|2638|2650|3.5|47.3|
|S32K342,<br> <br>25, typ<sup>3</sup>|50|52|0.91|1.8|
|S32K322, S32K341<br>25, max<sup>4</sup>|TBD|TBD|TBD|TBD|
|85, typ<sup>3</sup>|TBD|TBD|TBD|TBD|
|85, max<sup>4</sup>|TBD|TBD|TBD|TBD|
|105, typ<sup>3</sup>|TBD|TBD|TBD|TBD|
|105, max<sup>4</sup>|TBD|TBD|TBD|-|
|125, typ<sup>3</sup>|TBD|TBD|TBD|TBD|
|125, max<sup>4</sup>|TBD|TBD|5.5|-|
|S32K312<br>25, typ<sup>3</sup>|40|41|0.887|NA|
|25, max<sup>4</sup>|79|80|1.031||
|85, typ<sup>3</sup>|178|178|1.027||
|85, max<sup>4</sup>|496|497|1.422||
|105, typ<sup>3</sup>|350|346|1.197||
|105, max<sup>4</sup>|994|997|1.924||
|125, typ<sup>3</sup>|620|611|1.457||
|125, max<sup>4</sup>|1788|1792|2.761||



Table continues on the next page... 

###### Table 14. STANDBY mode supply currents (continued) 

|S32K311|25, typ<sup>3</sup>|46|48|0.91|NA|
|---|---|---|---|---|---|
||25, max<sup>4</sup>|TBD|TBD|TBD||
||85, typ<sup>3</sup>|TBD|TBD|TBD||
||85, max<sup>4</sup>|TBD|TBD|TBD||
||105, typ<sup>3</sup>|TBD|TBD|TBD||
||105, max<sup>4</sup>|TBD|TBD|TBD||
||125, typ<sup>3</sup>|TBD|TBD|TBD||
||125, max<sup>4</sup>|TBD|TBD|TBD||



1. See the configurations in Table 18. 

2. IO load current is not included. The actual current requirements for IOs will depend on the I/O configuration in the application. 

3. “typ” is indicative of the average current numbers at the nominal internally regulated V11 supply voltage, VDD_HV_A = 5.0V, VDD_HV_B = 5.0V, for the typical silicon process.. 

4. “max” is indicative of the maximum current numbers at the maximum internally regulated V11 supply voltage (1.16 V), VDD_HV_A = 5.5V, VDD_HV_B = 5.5V, for the fast silicon process. 

NXP Semiconductors 

Power management 

~~<mark>NOTE</mark>~~ 

All data in this table is preliminary and based on first samples. 

Typical current numbers are indicative for typical silicon process and may vary based on the silicon distribution and user configuration. Typical conditions assumes VDD_HV_A = VREFH = 5 V, VDD_HV_B = 5V (if the VDD_HV_B domain present in the device), temperature = 25 °C, and typical silicon process unless otherwise stated. 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

46 / 130 

Table 15. Low speed RUN mode supply currents 

||||||||Low Spee|d RUN M|ode (mA)|<sup>1</sup>|||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||BOOT<br>[Clock<br>FIRC @<br>[Las<br>Disa|Mode<sup>2</sup><br>Option C]<br>24 MHz<br>t Mile<br>bled]|BOOT<br>[Clock O<br>FIRC @<br>[Last<br>Ena|Mode<sup>2</sup><br>ption C]<br>24 MHz<br>Mile<br>bled]|Low<br>RU<br>[Clock<br>FIRC<br>[Las<br>Disa|Speed<br>N<sup>2</sup><br>Option E]<br>@3 MHz<br>t Mile<br>bled]|Low<br>RU<br>[Clock<br>FIRC<br>[Las<br>Ena|Speed<br>N<sup>2</sup><br>Option E]<br>@3 MHz<br>t Mile<br>bled]|Low<br>R<br>[Clock<br>FIRC<br>[La<br>Dis|Speed<br>UN<sup>2</sup><br>Option D]<br>@48 MHz<br>st Mile<br>abled]|Low<br>RU<br>[Clock<br>FIRC @<br>[Las<br>Ena|Speed<br>N<sup>2</sup><br>Option D]<br>48 MHz<br>t Mile<br>bled]|All<br>Config<sup>2</sup><br>.|
|Chip|Ambient Temperature (°C)|VDD_HV_A3,4|V155|VDD_HV_A3,4|V155|VDD_HV_A3,4|V155|VDD_HV_A3,4|V155|VDD_HV_A3,4|V155|VDD_HV_A3,4|V155|VDD_H<br>V_B<sup>3</sup>|
|S32K358,<br>S32K348|25, typ<sup>6</sup>|N|A|5|25|N|A|5|6||NA|5|55|TBD|
|,<br>S32K338,<br>|25, max<sup>7</sup>|||TBD|TBD|||TBD|TBD|||TBD|TBD|TBD|
|S32K328|85, typ<sup>6</sup>|||TBD|TBD|||TBD|TBD|||TBD|TBD|TBD|
||85, max<sup>7</sup>|||TBD|TBD|||TBD|TBD|||TBD|TBD|TBD|
||105, typ<sup>6</sup>|||TBD|TBD|||TBD|TBD|||TBD|TBD|TBD|
||105, max<sup>7</sup>|||TBD|TBD|||TBD|TBD|||TBD|TBD|TBD|
||125, typ<sup>6</sup>|||TBD|TBD|||TBD|TBD|||TBD|TBD|TBD|
||125, max<sup>7,</sup> <sup>8</sup>|||TBD|TBD|||TBD|TBD|||TBD|TBD|TBD|
|S32K344,<br>|25, typ<sup>6</sup>|20.5|-|2.8|17.9|6.4|-|2.8|4.5|37.2|-|2.9|34|0.6|
|S32K324,<br>S32K314|25, max<sup>7</sup>|29.4|-|3.2|27.2|14.8|-|3.1|12.6|46.8|-|3.2|46.6|0.8|
||85, typ<sup>6</sup>|34.2|-|2.9|31.2|19.7|-|2.9|17.5|50.4|-|2.9|47.3|0.5|



Table continues on the next page... 

Table 15. Low speed RUN mode supply currents (continued) 

||85, max<sup>7</sup>|71.6|-|3.5|68.7|56.2|-|3.4|54|89.1|-|3.5|86.2|0.7|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||105, typ<sup>6</sup>|46.1|-|2.9|43.1|31.7|-|2.9|29.3|62.2|-|2.9|59.2|0.5|
||105, max<sup>7</sup>|114|-|3.7|111|99.1|-|3.6|96.1|131|-|3.9|128|0.7|
||125, typ<sup>6</sup>|69.9|-|3.0|66.8|55.8|-|3.0|53.1|86|-|3.1|83|0.5|
||125, max<sup>7, 8</sup>|161|-|4.2|159|148|-|4.1|145|178|-|4.3|176|0.7|
|S32K342,<br>|25, typ<sup>6</sup>|20|-|2.8|17.9|6.4|-|2.8|4.5|37.2|-|2.9|34|0.6|
|S32K322,<br>S32K341|25, max<sup>7</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|0.7|
||85, typ<sup>6</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|
||85, max<sup>7</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|
||105, typ<sup>6</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|0.5|
||105, max<sup>7</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|0.6|
||125, typ<sup>6</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|0.5|
||125, max<sup>7, 8</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|0.6|
|S32K312|25, typ<sup>6</sup>|15|NA|N|A|5|NA|N|A|26|NA|N|A|NA|
||25, max<sup>7</sup>|20||||10||||32|||||
||85, typ<sup>6</sup>|20||||10||||31|||||
||85, max<sup>7</sup>|35.2||||24.6||||46.4|||||
||105, typ<sup>6</sup>|26.1||||16.2||||37|||||
||105, max<sup>7</sup>|52.9||||42.6||||64.2|||||
||125, typ<sup>6</sup>|35.3||||25.3||||46.4|||||



Table continues on the next page... 

Table 15. Low speed RUN mode supply currents (continued) 

||125, max<sup>7,</sup> <sup>8,</sup> <sup>9</sup>|79.8|||66.9|||90.1||||
|---|---|---|---|---|---|---|---|---|---|---|---|
|S32K311|25, typ<sup>6</sup>|15|NA|NA|6|NA|NA|30|NA|NA|NA|
||25, max<sup>7</sup>|TBD|||TBD|||TBD||||
||85, typ<sup>6</sup>|TBD|||TBD|||TBD||||
||85, max<sup>7</sup>|TBD|||TBD|||TBD||||
||105, typ<sup>6</sup>|TBD|||TBD|||TBD||||
||105, max<sup>7</sup>|TBD|||TBD|||TBD||||
||125, typ<sup>6</sup>|TBD|||TBD|||TBD||||
||125, max<sup>7,</sup> <sup>8,</sup> <sup>9</sup>|TBD|||TBD|||TBD||||



1. Current numbers are for reduced configuration and may vary based on user configuration and silicon process variation. 

2. See the example configurations in Table 18. 

3. IO load current is not included. The actual current requirements for IOs will depend on the I/O configuration in the application. 

4. RUN IDD @ VDD_HV_A includes Flash memory read current from the V25 voltage rail. 

5. RUN IDD @ V15 includes Flash memory read current from the V11 voltage rail 

6. “typ” is indicative of the average current numbers at the nominal internally regulated V11 supply voltage, VDD_HV_A = 5.0V, VDD_HV_B = 5.0V, V15 = 1.5V, for the typical silicon process. 

7. “max” is indicative of the maximum current numbers at the maximum internally regulated V11 supply voltage (1.16 V), VDD_HV_A = 5.5V, VDD_HV_B = 5.5V, V15 = 1.65V, for the fast silicon process. 

8. For the maximum allowable RUN current in an application, the junction temperature must be kept below the maximum specification, TJ < 150°C, to avoid self-heating. 

9. If the total power dissipation would cause the junction temperature to be exceeded when VDD_HV_A is at 5V, then VDD_HV_A should be limited to operate at 3.3V. 

NXP Semiconductors 

Power management 

~~<mark>NOTE</mark>~~ 

All data in this table is preliminary and based on first samples. 

Typical current numbers are indicative for typical silicon process and may vary based on the silicon distribution and user configuration. Typical conditions assumes VDD_HV_A = VREFH = 5 V, VDD_HV_B = 5V (if the VDD_HV_B domain present in the device), temperature = 25 °C and typical silicon process unless otherwise stated. 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

50 / 130 

Table 16. RUN mode supply currents (peripherals disabled) 

||||||||RU|N Mode (|mA)<sup>1</sup>||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||Min. C<br>Singl<br>@80<br>[Clock|onfig.<sup>2</sup><br>e Core<br>MHz<br>Option F]|Min. C<br>Singl<br>@12<br>[Clock|onfig.<sup>2</sup><br>e Core<br>0 MHz<br>Option B]|Min. C<br>Singl<br>@16<br>[Clock|onfig.<sup>2</sup><br>e Core<br>0 MHz<br>Option A]|Min. C<br>Dual<br>@80<br>[Clock|onfig.<sup>2</sup><br>Core<br>MHz<br>Option F]|Min. C<br>Dua<br>@12<br>[Clock|onfig.<sup>2</sup><br>l Core<br>0 MHz<br>Option B]|Min.<br>Dua<br>@16<br>[Clock|Config.<sup>2</sup><br>l Core<br>0 MHz<br>Option A]|All.<br>Config.<br>2|
|Chip|Ambient Temperature (°C)|VDD_HV_A3,4|V155|VDD_HV_A3,4|V155|VDD_HV_A3,4|V155|VDD_HV_A3,4|V155|VDD_HV_A3,4|V155|VDD_HV_A3,4|V155|VDD_H<br>V_B<sup>3</sup>|
|S32K358,<br>S32K348|25, typ<sup>6</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|
|,<br>S32K338,<br>S32K328|25, max<sup>7</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|
||85, typ<sup>6</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|
||85, max<sup>7</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|
||105, typ<sup>6</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|
||105, max<sup>7</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|
||125, typ<sup>6</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|
||125, max<sup>7, 8</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|
|S32K344,<br>S32K324|25, typ<sup>6</sup>|2.9|51.3|2.9|54.8|2.9|69.6|3.1|62.7|3.1|75.1|3.1|97.5|0.6|
|,<br>S32K314|25, max<sup>7</sup>|3.3|60.2|3.3|64.5|3.3|80.4|3.4|73.3|3.5|86.8|3.5|110|0.7|
||85, typ<sup>6</sup>|3.0|64.5|3.0|68.1|3.0|83.1|3.1|76.2|3.2|89|3.2|111|0.4|
||85, max<sup>7</sup>|3.6|104|3.6|108|3.7|124|3.8|117|3.9|131|3.8|155|0.6|



Table continues on the next page... 

Table 16. RUN mode supply currents (peripherals disabled) (continued) 

||105, typ<sup>6</sup>|3.0|75.4|3.0|79|3.0|93.9|3.2|87.3|3.2|100|3.2|122.6|0.5|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||105, max<sup>7</sup>|3.8|145|3.8|149|3.8|166|3.9|159|4.0|173|4.0|197|0.6|
||125, typ<sup>6</sup>|3.1|97.4|3.1|101.2|3.1|116.4|3.3|110|3.3|122.9|3.3|145.7|0.5|
||125, max<sup>7, 8</sup>|4.2|191|4.1|196|4.2|212|4.3|206|4.3|220|4.3|245|0.6|
|S32K342,<br>|25, typ<sup>6</sup>|2.9|51|2.9|54|2.9|69|3.1|62|3.1|74|3.1|97|0.6|
|S32K322,<br>S32K341|25, max<sup>7</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|0.7|
||85, typ<sup>6</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|
||85, max<sup>7</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|
||105, typ<sup>6</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|
||105, max<sup>7</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|
||125, typ<sup>6</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|0.5|
||125, max<sup>7, 8</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|0.6|
|S32K312|25, typ<sup>6</sup>|37|NA|37|NA|N|A|||N|A|||NA|
||25, max<sup>7</sup>|44||46|||||||||||
||85, typ<sup>6</sup>|42||43|||||||||||
||85, max<sup>7</sup>|58.5||59.7|||||||||||
||105, typ<sup>6</sup>|48.1||48.7|||||||||||
||105, max<sup>7</sup>|76.4||77.8|||||||||||
||125, typ<sup>6</sup>|56.5||57|||||||||||
||125, max<sup>7, 8, 9</sup>|98.7||99.9|||||||||||



Table continues on the next page... 

###### Table 16. RUN mode supply currents (peripherals disabled) (continued) 

|S32K311|25, typ<sup>6</sup>|60|NA|65|NA|NA|NA|NA|
|---|---|---|---|---|---|---|---|---|
||25, max<sup>7</sup>|TBD||TBD|||||
||85, typ<sup>6</sup>|TBD||TBD|||||
||85, max<sup>7</sup>|TBD||TBD|||||
||105, typ<sup>6</sup>|TBD||TBD|||||
||105, max<sup>7</sup>|TBD||TBD|||||
||125, typ<sup>6</sup>|TBD||TBD|||||
||125, max<sup>7, 8, 9</sup>|120||125|||||



1. Current numbers are for reduced configuration and may vary based on user configuration and silicon process variation. 

2. See the configurations in Table 19. 

3. IO load current is not included. The actual current requirements for IOs will depend on the I/O configuration in the application. 

4. RUN IDD @ VDD_HV_A includes Flash memory read current from the V25 voltage rail. 

5. RUN IDD @ V15 includes Flash memory read current from the V11 voltage rail. 

6. “typ” is indicative of the average current numbers at the nominal internally regulated V11 supply voltage, VDD_HV_A = 5.0V, VDD_HV_B = 5.0V, V15 = 1.5V, for the typical silicon process. 

7. “max” is indicative of the maximum current numbers at the maximum internally regulated V11 supply voltage (1.16 V), VDD_HV_A = 5.5V, VDD_HV_B = 5.5V, V15 = 1.65V, for the fast silicon process. 

8. For the maximum allowable RUN current in an application, the junction temperature must be kept below the maximum specification, TJ < 150°C, to avoid self-heating. 

9. If the total power dissipation would cause the junction temperature to be exceeded when VDD_HV_A is at 5V, then VDD_HV_A should be limited to operate at 3.3V. 

NXP Semiconductors 

Power management 

~~<mark>NOTE</mark>~~ 

The data in this table is preliminary and based on first samples. 

Typical current numbers are indicative for typical silicon process and may vary based on the silicon distribution and user configuration. Typical conditions assumes VDD_HV_A = VREFH = 5 V, VDD_HV_B = 5V (if the VDD_HV_B domain present in the device), temperature = 25 °C and typical silicon process unless otherwise stated. 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

54 / 130 

Table 17. Example RUN mode configuration supply currents 

||||||||RU|N Mode (|mA)<sup>1</sup>||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||Conf<br>Dual<br>@16|ig. 1<sup>2</sup><br>Core<br>0 MHz|Conf<br>Singl<br>@16|ig. 2<sup>2</sup><br>e Core<br>0 MHz|Con<br>Dua<br>@12|fig. 3<sup>2</sup><br>l Core<br>0 MHz|Conf<br>Singl<br>@12|ig. 4<sup>2</sup><br>e Core<br>0 MHz|Conf<br>Singl<br>@80|ig. 5<sup>2</sup><br>e Core<br>MHz|Config.<br>Triple C<br>@240 M|6<sup>2</sup><br>ore<br>Hz|Config.<br>1-6<sup>2</sup>|
|Chip|Ambient Temperature (°C)|VDD_HV_A3,4|V155|VDD_HV_A3,4|V155|VDD_HV_A3,4|V155|VDD_HV_A3,4|V155|VDD_HV_A3,4|V155|VDD_H<br>V_A<sup>3, 4 </sup>|<sup>V155</sup>|VDD_H<br>V_B<sup>3</sup>|
|S32K358,<br>S32K348|25, typ<sup>6</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|
|,<br>S32K338,<br>|25, max<sup>7</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|
|S32K328|85, typ<sup>6</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|
||85, max<sup>7</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|
||105, typ<sup>6</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|
||105, max<sup>7</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|
||125, typ<sup>6</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|
||125, max<sup>7,</sup> <sup>8</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|
|S32K344,<br>|25, typ<sup>6</sup>|2.9|119|3.0|102|3.1|106|3.0|80|2.9|68|NA||0.6|
|S32K324,<br>S32K314|25, max<sup>7</sup>|3.3|133|3.3|115|3.5|119|3.4|92|3.4|79|||0.7|
||85, typ<sup>6</sup>|3.0|134|3.0|116|3.2|120|3.1|94|3.0|81.8|||0.4|
||85, max<sup>7</sup>|3.6|180|3.7|160|3.9|165|3.8|137|3.6|123|||0.6|
||105, typ<sup>6</sup>|3.0|145|3.1|128|3.2|132|3.1|105|3.0|93|||0.5|



Table continues on the next page... 

Table 17. Example RUN mode configuration supply currents (continued) 

||105, max<sup>7</sup>|3.8|222|3.9|203|4.0|208|3.9|179|3.6|165||0.6|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||125, typ<sup>6</sup>|3.1|169|3.2|151|3.3|155|3.2|128|3.2|116||0.5|
||125, max<sup>7, 8</sup>|4.3|271|4.3|250|4.5|256|4.4|226|4.2|213||0.6|
|S32K342,<br>S32K322|25, typ<sup>6</sup>|2.9|115|3.0|99|3.1|99|2.9|78|2.9|66|NA|0.6|
|,<br>S32K341|25, max<sup>7</sup>|3.3|128|3.3|110|3.5|112|3.3|90|3.3|77||0.7|
||85, typ<sup>6</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD||TBD|
||85, max<sup>7</sup>|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD|TBD||TBD|
||105, typ<sup>6</sup>|3.0|140|3.1|121|3.2|126|3.0|103|3.0|90||0.5|
||105, max<sup>7</sup>|3.8|240|3.9|220|4.0|225|3.8|198|3.8|184||0.6|
||125, typ<sup>6</sup>|3.1|164|3.2|145|3.3|150|3.1|125|3.1|110||0.5|
||125, max<sup>7, 8</sup>|4.3|330|4.5|304|4.7|304|4.3|280|4.3|265||0.6|
|S32K312|25, typ<sup>6</sup>|N|A|N|A|N|A|54|NA|44|NA|NA|NA|
||25, max<sup>7</sup>|||||||62||53||||
||85, typ<sup>6</sup>|||||||60||49||||
||85, max<sup>7</sup>|||||||76.4||66.3||||
||105, typ<sup>6</sup>|||||||65.8||55||||
||105, max<sup>7</sup>|||||||94.4||84.4||||
||125, typ<sup>6</sup>|||||||78.6||64.7||||
||125, max<sup>7, 8, 9</sup>|||||||120.7||110.5||||
|S32K311|25, typ<sup>6</sup>|N|A|N|A|N|A|80|NA|70|NA|NA|NA|



Table continues on the next page... 

###### Table 17. Example RUN mode configuration supply currents (continued) 

|25, max<sup>7</sup>|92|80|
|---|---|---|
|85, typ<sup>6</sup>|TBD|TBD|
|85, max<sup>7</sup>|TBD|TBD|
|105, typ<sup>6</sup>|TBD|TBD|
|105, max<sup>7</sup>|TBD|TBD|
|125, typ<sup>6</sup>|TBD|TBD|
|125, max<sup>7, 8, 9</sup>|140|130|



1. Current numbers are for reduced configuration and may vary based on user configuration and silicon process variation. 

2. See the configurations in Table 19. 

3. IO current is not included. The actual current requirements for IOs will depend on the I/O configuration in the application. 

4. RUN IDD @ VDD_HV_A includes Flash memory read current from the V25 voltage rail. 

5. RUN IDD @ V15 includes Flash memory read current from the V11 voltage rail. 

6. “typ” is indicative of the average current numbers at the nominal internally regulated V11 supply voltage, VDD_HV_A = 5.0V, VDD_HV_B = 5.0V, V15 = 1.5V, for the typical silicon process. 

7. “max” is indicative of the maximum current numbers at the maximum internally regulated V11 supply voltage (1.16 V), VDD_HV_A = 5.5V, VDD_HV_B = 5.5V, V15 = 1.65V, for the fast silicon process. 

8. For the maximum allowable RUN current in an application, the junction temperature must be kept below the maximum specification, TJ < 150°C, to avoid self-heating. 

9. If the total power dissipation would cause the junction temperature to be exceeded when VDD_HV_A is at 5V, then VDD_HV_A should be limited to operate at 3.3V. 

NXP Semiconductors 

Power management 

##### 6.10 Operating mode 

Table 18. STANDBY and low speed RUN configuration options 

|MODULE|STANDBY<br>All OFF|STANDBY<br>SIRC ON|STANDBY<br>FIRC ON|BOOT Mode<br>(OptionC<sup>1</sup>, FIRC<br>@24 MHz)|Low Speed RUN<br>(OptionE<sup>1</sup>, FIRC<br>@ 3MHz)|FIRC Mode<br>(OptionD<sup>1</sup>, FIRC<br>@48 MHz)|
|---|---|---|---|---|---|---|
|Core M7_0|OFF|OFF|OFF|24 MHz|3 MHz|48 MHz|
|Core M7_1|OFF|OFF|OFF|24 MHz|3 MHz|48 MHz|
|HSE_B|OFF|OFF|OFF|24 MHz|3 MHz|48 MHz|
|FIRC|OFF|OFF|24 MHz|24 MHz|3 MHz|48 MHz|
|FXOSC|OFF|OFF|OFF|OFF|OFF|OFF|
|SIRC|OFF|ON|OFF|ON|ON|ON|
|PLL|OFF|OFF|OFF|OFF|OFF|OFF|
|Flash|OFF|OFF|OFF|ON|ON|ON|
|eDMA|OFF|OFF|OFF|ON|ON|ON|
|FlexCAN|All OFF|All OFF|All OFF|All OFF|All OFF|All OFF|
|LPUART|All OFF|All OFF|All OFF|All OFF|All OFF|All OFF|
|LPSPI|All OFF|All OFF|All OFF|All OFF|All OFF|All OFF|
|LPI2C|All OFF|All OFF|All OFF|All OFF|All OFF|All OFF|
|EMAC|OFF|OFF|OFF|OFF|OFF|OFF|
|eMIOS|All OFF|All OFF|All OFF|All OFF|All OFF|All OFF|
|SAR_ADC|All OFF|All OFF|All OFF|All OFF|All OFF|All OFF|
|LPCMP|All OFF|All OFF|All OFF|All OFF|All OFF|All OFF|



1. See clocking use case examples in the Clocking chapter of the S32K3xx Reference Manual. 

Table 19. RUN mode configuration options 

||Min.<br>Config.<br>(OptionF<sup>1</sup>)<br>, PLL@80<br>MHz|Min.<br>Config.<br>(OptionB<sup>1</sup>)<br>,<br>PLL@120|Min.<br>Config.<br>(OptionA<sup>1</sup>)<br>,<br>PLL@160|Config. 1<br>Dual Core<br>@160MHz|Config. 2<br>Single<br>Core<br>@160MHz|Config. 3<br>Dual Core<br>@120MHz|Config. 4<br>Single<br>Core<br>@120MHz|Config. 5<br>Single<br>Core<br>@80MHz|Config. 6<br>Triple Core<br>@240MHz|
|---|---|---|---|---|---|---|---|---|---|
|MODULE||MHz|MHz|||||||
|Core M7_0|80 MHz|120 MHz|160 MHz|160 MHz|160 MHz|120 MHz|120 MHz|80 MHz|240 MHz|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

58 / 130 

NXP Semiconductors 

Power management 

Table 19. RUN mode configuration options (continued) 

|Core M7_1|80 MHz|120 MHz|160 MHz|160 MHz|-|120 MHz|-|-|240 MHz|
|---|---|---|---|---|---|---|---|---|---|
|Core M7_2|-|-|-|-|-|-|-|-|240 MHz|
|HSE_B<sup>2</sup>|80 MHz|120 MHz|80 MHz|80 MHz|80 MHz|120 MHz|120 MHz|80 MHz|120 MHz|
|FIRC|ON|ON|ON|ON|ON|ON|ON|ON|ON|
|FXOSC|ON|ON|ON|ON|ON|ON|ON|ON|ON|
|SIRC|ON|ON|ON|ON|ON|ON|ON|ON|ON|
|PLL|ON|ON|ON|ON|ON|ON|ON|ON|ON|
|Flash|ON|ON|ON|ON|ON|ON|ON|ON|ON|
|eDMA|ON|ON|ON|ON|ON|ON|ON|ON|ON|
|FlexCAN<sup>3</sup>|All OFF|All OFF|All OFF|6x|2x|4x|6x|1x|8x|
|LPUART<sup>4</sup>|All OFF|All OFF|All OFF|16x|4x|10x|8x|7x|16x|
|LPSPI<sup>5</sup>|All OFF|All OFF|All OFF|6x|4x|4x|4x|3x|5x|
|LPI2C<sup>6</sup>|All OFF|All OFF|All OFF|All OFF|2x|2x|2x|All OFF|1x|
|EMAC<sup>7</sup>|OFF|OFF|OFF|ON|OFF|ON|OFF|OFF|ON|
|SAI|OFF|OFF|OFF|OFF|OFF|OFF|OFF|OFF|OFF|
|QSPI|OFF|OFF|OFF|OFF|OFF|OFF|OFF|OFF|ON|
|eMIOS<sup>8</sup>|All OFF|All OFF|All OFF|All OFF|3x|3x|2x|2x|2x|
|SAR_ADC<br>9|All OFF|All OFF|All OFF|All OFF|3x|3x|2x|2x|3x|
|LPCMP<sup>10</sup>|All OFF|All OFF|All OFF|All OFF|2x|3x|All OFF|All OFF|OFF|



1. See clocking use case examples in the Clocking chapter of the S32K3xx Reference Manual. 

2. HSE_B: After start-up, the HSE core is in WFI. 

3. • FlexCAN0: Transmitting an 8-byte CAN-FD data frame at 5 Mbps, every 10 ms. 

   - FlexCAN1: Transmitting a 64-byte CAN-FD data frame at 2 Mbps, every 20 ms. 

   - FlexCAN2-5: Transmitting an 8-byte CAN data frame at 500 Kbps, every 20 ms. 

4. LPUART0-15: Transmitting at 19200 bps, every 100ms. 

5. • LPSPI0: Transmitting 32 bits at 20 Mbps (GPIO Fast pads), every 5 ms. 

   - LPSPI1-5: Transmitting 32 bits at 1 Mbps, every 5 ms. 

6. LPI2C0-1: Transmitting 3 bytes at 400 Kbps, every 100ms. 

7. EMAC: ON for MII interface. 

8. • eMIOS0: 6 channels in PWM mode @ 20 KHz. 

   - eMIOS1-2: 8 channels in PWM mode @ 400 Hz. 

9. • SAR_ADC0: 16 channels at 400 Hz rate, BCTU triggered. 

   - SAR_ADC1-2: 4 channels at 20 KHz rate, BCTU triggered. 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

59 / 130 

NXP Semiconductors 

I/O parameters 

###### 10. LPCMP0: 8 channels enabled; LPCMP1-2: 4 channels enabled. 

##### 6.11 Cyclic wake-up current 

The cyclic wake-up current is the calculated average current consumption during the periodic switching between RUN mode and STANDBY mode. This average current can be calculated with the following formula: 

ICYCL = RUN Current According to Ratio + STANDBY Current According to Ratio 

Where the Current According to Ratio value is calculated as follows: 

Current According to Ratio = Supply Current × Ratio of Duration 

As an example, the following data was obtained with an application that periodically (every 40ms) alternates between RUN mode, for approximately 200μs to scan several GPIO inputs (51 GPIOS), and spends the rest of the time in STANDBY mode. 

|Chip|Device<br>Operating Mode|Supply Current<sup>1</sup><br>[μA]|Duration<sup>2</sup>[ms]|Ratio of<br>Duration<sup>3</sup>|Current<br>According to|ICYCL -<br>Average current|
|---|---|---|---|---|---|---|
||||||Ratio<sup>4</sup>[μA]|5[μA]|
|S32K314|RUN|20000|0.2|0.005|100|159.7|
||STANDBY|60|39.8|0.995|59.7||



1. The supply current is obtained through the measurements of the current during the corresponding operating mode. 

2. The duration is defined by the application (how much time will the device spend in the according operating mode). 

3. The ratio of duration is obtained by dividing the duration of the corresponding operating mode by the total duration of the application. 

4. The current according to ratio is obtained by multiplying the supply current and the ratio of duration related to the proper operating mode. 

5. The average current is calculated by the addition of each device operating mode’s current according to ratio. 

#### 7 I/O parameters 

##### 7.1 GPIO DC electrical specifications, 3.3V Range (2.97V - 3.63V) 

Table 20. GPIO DC electrical specifications, 3.3V Range (2.97V - 3.63V) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|VIH|Input high level DC<br>voltage threshold|0.70 x<br>VDD_HV<br>_A/B|—|VDD_HV<br>_A/B +<br>0.3|V|VDD_HV_A/B = 3.3V|—|
|VIL|Input low level DC<br>voltage threshold|VSS - 0.3|—|0.30 x<br>VDD_HV<br>_A/B|V|VDD_HV_A/B = 3.3V|—|
|WFRST|RESET Input<br>Filtered pulse width<sup>1</sup>|—|—|33|ns|—|—|
|WNFRST|RESET Input not<br>filtered pulse width<sup>2</sup>|100|—|—|ns|—|—|
|ILKG_33_S|3.3V input leakage<br>current for Standard<br>GPIO<sup>3</sup>|-160|—|600|nA|Analog Function<br>Count=0|—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

60 / 130 

NXP Semiconductors 

I/O parameters 

Table 20. GPIO DC electrical specifications, 3.3V Range (2.97V - 3.63V) (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|ILKG_33_S|3.3V input leakage<br>current for Standard<br>GPIO<sup>3</sup>|-1020|—|870|nA|Analog Function<br>Count=1|—|
|ILKG_33_S|3.3V input leakage<br>current for Standard<br>GPIO<sup>3</sup>|-1880|—|1140|nA|Pins with Analog<br>Function Count=2, plus<br>PTD1, PTA12|—|
|ILKG_33_S|3.3V input leakage<br>current for Standard<br>GPIO<sup>3</sup>|-2740|—|1410|nA|Pins with Analog<br>Function Count=3, plus<br>PTD0|—|
|ILKG_33_S_PTE13|3.3V input leakage<br>current for Standard<br>GPIO<sup>3</sup>|-4400|—|2030|nA|PMC VRC_CTRL pin|—|
|ILKG_33_SP|3.3V input leakage<br>current for Standard<br>Plus GPIO, input<br>only, and reset IO<sup>3</sup>|-420|—|1270|nA|Analog Function<br>Count=0|—|
|ILKG_33_SP|3.3V input leakage<br>current for Standard<br>Plus GPIO, input<br>only, and reset IO<sup>3</sup>|-1270|—|1530|nA|Analog Function<br>Count=1|—|
|ILKG_33_SP|3.3V input leakage<br>current for Standard<br>Plus GPIO, input<br>only, and reset IO<sup>3</sup>|-2130|—|1800|nA|Analog Function<br>Count=2|—|
|ILKG_33_M|3.3V GPIO input<br>leakage current for<br>Medium GPIO pad<sup>3</sup>|-710|—|1630|nA|Analog Function<br>Count=0|—|
|ILKG_33_M|3.3V GPIO input<br>leakage current for<br>Medium GPIO pad<sup>3</sup>|-1560|—|1900|nA|Pins with Analog<br>Function Count=1, plus<br>PTD5, PTC16|—|
|ILKG_33_M|3.3V GPIO input<br>leakage current for<br>Medium GPIO pad<sup>3</sup>|-2410|—|2170|nA|PTE8 and PTD6|—|
|ILKG_33_F|3.3V GPIO input<br>leakage current for<br>Fast GPIO pad<sup>3</sup>|-1340|—|2720|nA|Analog Function<br>Count=0|—|
|ILKG_33_F|3.3V GPIO input<br>leakage current for<br>Fast GPIO pad<sup>3</sup>|-2200|—|2990|nA|Analog Function<br>Count=1|—|
|ILKG_33|3.3V input leakage<br>current for GPI<sup>3</sup>|-120|—|120|nA|—|—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

61 / 130 

NXP Semiconductors 

I/O parameters 

Table 20. GPIO DC electrical specifications, 3.3V Range (2.97V - 3.63V) (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|VHYS_33|input hysteresis<br>voltage|0.06 x<br>VDD_HV<br>_A/B|—|—|mV|Always enabled.|—|
|CIN|GPIO Input<br>capacitance|2|4|6|pF|add 2pF for package/<br>parasitic|—|
|IPU_33|3.3V GPIO pull up/<br>down resistance|20|—|60|kΩ|pull up @ 0.3 x VDD_<br>HV_A/B, pull down @<br>0.7 x VDD_HV_A/B|—|
|IOH_33_S|3.3V output<br>high current for<br>Standard GPIO<sup>4</sup>|1.0|—|—|mA|VOH >= VDD_HV_A/B<br>- 0.7V|—|
|IOH_33_SP|3.3V output high<br>current for Standard<br>Plus GPIO and<br>RESET IO<sup>4</sup>|1.5|—|—|mA|DSE = 0, VOH >=<br>VDD_HV_A/B - 0.7V|—|
|IOH_33_M|3.3V output high<br>current for Medium<br>GPIO<sup>4</sup>|3|—|—|mA|DSE = 0, VOH >=<br>VDD_HV_A/B - 0.7V|—|
|IOH_33_F|3.3V output high<br>current for Fast<br>GPIO<sup>4</sup>|4.5|—|—|mA|DSE = 0, VOH >=<br>VDD_HV_A/B - 0.7V|—|
|IOH_33_SP|3.3V output high<br>current for Standard<br>Plus GPIO and<br>RESET IO<sup>4</sup>|3|—|—|mA|DSE = 1, VOH >=<br>VDD_HV_A/B - 0.7V|—|
|IOH_33_M|3.3V output high<br>current for Medium<br>GPIO<sup>4</sup>|6|—|—|mA|DSE = 1, VOH >=<br>VDD_HV_A/B - 0.7V|—|
|IOH_33_F|3.3V output high<br>current for Fast<br>GPIO<sup>4</sup>|9|—|—|mA|DSE = 1, VOH >=<br>VDD_HV_A/B - 0.7V|—|
|IOL_33_S|3.3V output low<br>current for Standard<br>GPIO<sup>4</sup>|1.0|—|—|mA|VOL <= 0.7V|—|
|IOL_33_SP|3.3V output low<br>current for Standard<br>Plus GPIO and<br>RESET IO<sup>4</sup>|1.5|—|—|mA|DSE =0, VOL <= 0.7V|—|
|IOL_33_M|3.3V output low<br>current for Medium<br>GPIO<sup>4</sup>|3.0|—|—|mA|DSE =0, VOL <= 0.7V|—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

62 / 130 

NXP Semiconductors 

I/O parameters 

Table 20. GPIO DC electrical specifications, 3.3V Range (2.97V - 3.63V) (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|IOL_33_F|3.3V output low<br>current for Fast<br>GPIO<sup>4</sup>|4.5|—|—|mA|DSE =0, VOL <= 0.7V|—|
|IOL_33_SP|3.3V output low<br>current for Standard<br>Plus GPIO and<br>RESET IO<sup>4</sup>|3|—|—|mA|DSE =1, VOL <= 0.7V|—|
|IOL_33_M|3.3V output low<br>current for Medium<br>GPIO<sup>4</sup>|6|—|—|mA|DSE =1, VOL <= 0.7V|—|
|IOL_33_F|3.3V output low<br>current for Fast<br>GPIO<sup>4</sup>|9|—|—|mA|DSE =1, VOL <= 0.7V|—|
|FMAX_33_S|3.3V maximum<br>frequency for<br>Standard GPIO<sup>4, 5</sup>|—|—|10|MHz|2.9V - 3.6V, internal<br>5pF, PCB trace ~10pF<br>and external 10pF,<br>total 25pF load|—|
|FMAX_33_SP|3.3V maximum<br>frequency for<br>Standard Plus<br>GPIO<sup>4, 5</sup>|—|—|25|MHz|2.9V - 3.6V, internal<br>5pF, PCB trace ~10pF<br>and external 10pF,<br>total 25pF load|—|
|FMAX_33_M|3.3V maximum<br>frequency for<br>Medium GPIO<sup>4, 5</sup>|—|—|50|MHz|2.9V - 3.6V, internal<br>5pF, PCB trace ~10pF<br>and external 10pF,<br>total 25pF load|—|
|FMAX_33_F|3.3V maximum<br>frequency for Fast<br>GPIO<sup>4, 5</sup>|—|—|120|MHz|2.9V - 3.6V, internal<br>5pF, PCB trace ~10pF<br>and external 10pF,<br>total 25pF load|—|
|IOHT|Output high current<br>total for all ports|—|—|100|mA|—|—|



1. Maximum length of RESET pulse will be filtered by an internal filter on this pin. 

2. Minimum length of RESET pulse,  guaranteed not to be filtered by the internal filter. 

3. A positive value is leakage flowing into pin with pin at VDD_HV_A/B (the GPIO supply level); a negative value is leakage flowing out the pin with the pin at ground. 

4. GPIO output transition time information can be obtained from the device IBIS model. IBIS models are recommended for system level simulations, as discrete values for I/O transition times are not representative of the I/O pad behavior when connected to an actual transmission line load. 

5. I/O timing specifications are valid for the un-terminated transmission line reference load given in the figure below. A lumped 8pF load is assumed at the end of a 5 inch microstrip trace on standard FR4 with approximately 1.5pF/inch (25pF total with margin). For signals with frequency greater than 63MHz, a maximum 2 inch PCBÂ trace is assumed. 

I/O current specifications are valid for the given reference load figure, and the constraints given in the Operating Conditions of this document. The "Analog Function Count" is defined from the number of CMP and ADC channels multiplexed to a given pin. This information can be obtained from the "Direct Signals" column in the IOMUX file attached to the Reference Manual. 

S32K3xx Data Sheet, Rev. 4, 04/2022 Preliminary Information 

Data Sheet: Technical Data 

63 / 130 

NXP Semiconductors 

I/O parameters 

To determine total switching current on any I/O supply, current values per output pin should not be incrementally summed. I/O interfaces on the device are asynchronous to each other, so not all switching occurs at the same instant. Actual use case must be considered. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0064-03.png)


<!-- Start of picture text -->
MCU see note 1 PCB External<br>device<br>5 in.<br>(4 layer FR4)<br>CPCB = ~1.5 pF/inch  * 5 inch = ~7.5 pF<br>RDSON<br>RPCB = RDSON<br>RDSON CL = 8 pF<br>Notes:<br>1. See IBIS models for further details.<br><!-- End of picture text -->

Figure 25. Reference Load Diagram 

##### 7.2 GPIO DC electrical specifications, 5.0V (4.5V - 5.5V) 

Table 21. GPIO DC electrical specifications, 5.0V (4.5V - 5.5V) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|VIH|Input high level DC<br>voltage threshold|0.65 x<br>VDD_HV<br>_A/B|—|VDD_HV<br>_A/B +<br>0.3|V|VDD_HV_A/B = 5.0V|—|
|VIL|Input low level DC<br>voltage threshold|VSS - 0.3|—|0.35 x<br>VDD_HV<br>_A/B|V|VDD_HV_A/B = 5.0V|—|
|WFRST|RESET Input filtered<br>pulse width<sup>1</sup>|—|—|33|ns|—|—|
|WNFRST|RESET Input not<br>filtered pulse width<sup>2</sup>|100|—|—|ns|—|—|
|ILKG_50_S|5.0V input leakage<br>current for Standard<br>GPIO<sup>3</sup>|-250|—|800|nA|Analog Function<br>Count=0|—|
|ILKG_50_S|5.0V input leakage<br>current for Standard<br>GPIO<sup>3</sup>|-1300|—|1100|nA|Analog Function<br>Count=1|—|
|ILKG_50_S|5.0V input leakage<br>current for Standard<br>GPIO<sup>3</sup>|-2300|—|1450|nA|Pins with Analog<br>Function Count=2, plus<br>PTD1, PTA12|—|
|ILKG_50_S|5.0V input leakage<br>current for Standard<br>GPIO<sup>3</sup>|-3300|—|1750|nA|Pins with Analog<br>Function Count=3, plus<br>PTD0|—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

64 / 130 

NXP Semiconductors 

I/O parameters 

Table 21. GPIO DC electrical specifications, 5.0V (4.5V - 5.5V) (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|ILKG_50_S_PTE13|5.0V input leakage<br>current for Standard<br>GPIO<sup>3</sup>|-3300|—|1750|nA|PMC VRC_CTRL pin|—|
|ILKG_50_SP|5.0V input leakage<br>current for Standard<br>Plus GPIO and<br>RESET IO<sup>3</sup>|-660|—|1760|nA|Analog Function<br>Count=0|—|
|ILKG_50_SP|5.0V input leakage<br>current for Standard<br>Plus GPIO and<br>RESET IO<sup>3</sup>|-1510|—|2030|nA|Analog Function<br>Count=1|—|
|ILKG_50_SP|5.0V input leakage<br>current for Standard<br>Plus GPIO and<br>RESET IO<sup>3</sup>|-2450|—|2290|nA|Analog Function<br>Count=2|—|
|ILKG_50_M|5.0V input leakage<br>current for Medium<br>GPIO<sup>3</sup>|-1110|—|2270|nA|Analog Function<br>Count=0|—|
|ILKG_50_M|5.0V input leakage<br>current for Medium<br>GPIO<sup>3</sup>|-1970|—|2540|nA|Pins with Analog<br>Function Count=1, plus<br>PTD5, PTC16|—|
|ILKG_50_M|5.0V input leakage<br>current for Medium<br>GPIO<sup>3</sup>|-2830|—|2810|nA|PTE8 and PTD6|—|
|ILKG_50_F|5.0V input leakage<br>current for Fast<br>GPIO<sup>3</sup>|-2120|—|3790|nA|Analog Function<br>Count=0|—|
|ILKG_50_F|5.0V input leakage<br>current for Fast<br>GPIO<sup>3</sup>|-2980|—|4060|nA|Analog Function<br>Count=1|—|
|ILKG_50|5.0V input leakage<br>current for GPI<sup>3</sup>|-150|—|150|nA|—|—|
|VHYS_50|input hysteresis<br>voltage|0.06 x<br>VDD_HV<br>_A/B|—|—|mV|Always enabled.|—|
|CIN|GPIO Input<br>capacitance|2|4|6|pF|add 2pF for package/<br>parasitic|—|
|IPU_50|5.0V GPIO pull up/<br>down resistance|20|—|55|kΩ|pull up @ 0.3 * VDD_<br>HV_*, pull down @ 0.7<br>* VDD_HV_*|—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

65 / 130 

NXP Semiconductors 

I/O parameters 

Table 21. GPIO DC electrical specifications, 5.0V (4.5V - 5.5V) (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|IOH_50_S|5.0V output<br>high current<br>Standard GPIO<sup>4</sup>|1.6|—|—|mA|VOH >= VDD_HV_A/B<br>- 0.7V|—|
|IOH_50_SP|5.0V output high<br>current Standard<br>Plus GPIO and<br>RESET IO<sup>4</sup>|2.5|—|—|mA|DSE = 0, VOH >=<br>VDD_HV_A/B - 0.7V|—|
|IOH_50_M|5.0V output high<br>current for Medium<br>GPIO<sup>4</sup>|4.0|—|—|mA|DSE = 0, VOH >=<br>VDD_HV_A/B - 0.7V|—|
|IOH_50_F|5.0V output high<br>current for Fast<br>GPIO<sup>4</sup>|6.0|—|—|mA|DSE = 0, VOH >=<br>VDD_HV_A/B - 0.7V|—|
|IOH_50_SP|5.0V output high<br>current for Standard<br>Plus GPIO and<br>RESET IO<sup>4</sup>|5.0|—|—|mA|DSE = 1, VOH >=<br>VDD_HV_A/B - 0.7V|—|
|IOH_50_M|5.0V output high<br>current for Medium<br>GPIO<sup>4</sup>|8.0|—|—|mA|DSE = 1, VOH >=<br>VDD_HV_A/B - 0.7V|—|
|IOH_50_F|5.0V GPIO output<br>high current for Fast<br>GPIO<sup>4</sup>|12.0|—|—|mA|DSE = 1, VOH >=<br>VDD_HV_A/B - 0.7V|—|
|IOL_50_S|5.0V output<br>low current for<br>Standard GPIO<sup>4</sup>|1.6|—|—|mA|VOL <= 0.7V|—|
|IOL_50_SP|5.0V output low<br>current for Standard<br>Plus GPIO and<br>RESET IO<sup>4</sup>|2.5|—|—|mA|DSE =0, VOL <= 0.7V|—|
|IOL_50_M|5.0V output low<br>current for Medium<br>GPIO<sup>4</sup>|4.0|—|—|mA|DSE =0, VOL <= 0.7V|—|
|IOL_50_F|5.0V output low<br>current for Fast<br>GPIO<sup>4</sup>|6.0|—|—|mA|DSE =0, VOL <= 0.7V|—|
|IOL_50_SP|5.0V output low<br>current for Standard<br>Plus GPIO and<br>RESET IO<sup>4</sup>|5.0|—|—|mA|DSE =1, VOL <= 0.7V|—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

66 / 130 

NXP Semiconductors 

I/O parameters 

Table 21. GPIO DC electrical specifications, 5.0V (4.5V - 5.5V) (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|IOL_50_M|5.0V output low<br>current for medium<br>GPIO<sup>4</sup>|8.0|—|—|mA|DSE =1, VOL <= 0.7V|—|
|IOL_50_F|5.0V output low<br>current for Fast<br>GPIO<sup>4</sup>|12.0|—|—|mA|DSE =1, VOL <= 0.7V|—|
|FMAX_50_S|5.0V maximum<br>frequency for<br>Standard GPIO<sup>4, 5</sup>|—|—|10|MHz|3.6V - 5.5V, total 25pF<br>load includes internal<br>5pF, PCB trace ~10pF<br>and external 10pF.|—|
|FMAX_50_SP|5.0V maximum<br>frequency for<br>Standard Plus<br>GPIO<sup>4, 5</sup>|—|—|25|MHz|3.6V - 5.5V, total 25pF<br>load includes internal<br>5pF, PCB trace ~10pF<br>and external 10pF.|—|
|FMAX_50_M|5.0V maximum<br>frequency for<br>Medium GPIO<sup>4, 5</sup>|—|—|25|MHz|3.6V - 5.5V, total 25pF<br>load includes internal<br>5pF, PCB trace ~10pF<br>and external 10pF|—|
|FMAX_50_F|5.0V maximum<br>frequency for Fast<br>GPIO<sup>4, 5</sup>|—|—|25|MHz|3.6V - 5.5V, total 25pF<br>load includes internal<br>5pF, PCB trace ~10pF<br>and external 10pF.|—|
|IOHT|Output high current<br>total for all ports|—|—|100|mA|—|—|



1. Maximum length of RESET pulse will be filtered by an internal filter on this pin. 

2. Minimum length of RESET pulse,  guaranteed not to be filtered by the internal filter. 

3. A positive value is leakage flowing into pin with pin at VDD_HV_A/B (the GPIO supply level); a negative value is leakage flowing out the pin with the pin at ground. 

4. GPIO output transition time information can be obtained from the device IBIS model. IBIS models are recommended for system level simulations 

5. I/O timing specifications are valid for the un-terminated transmission line reference load given in the figure below. A lumped 8pF load is assumed at the end of a 5 inch microstrip trace on standard FR4 with approximately 1.5pF/inch (25pF total with margin). 

I/O current specifications are valid for the given reference load figure, and the constraints given in the Operating Conditions of this document. The "Analog Function Count" is defined from the number of CMP and ADC channels multiplexed to a given pin. This information can be obtained from the "Direct Signals" column in the IOMUX file attached to the Reference Manual. 

To determine total switching current on any I/O supply, current values per output pin should not be incrementally summed. I/O interfaces on the device are asynchronous to each other, so not all switching occurs at the same instant. Actual use case must be considered. 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

67 / 130 

NXP Semiconductors 

I/O parameters 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0068-02.png)


<!-- Start of picture text -->
MCU see note 1 PCB External<br>device<br>5 in.<br>(4 layer FR4)<br>CPCB = ~1.5 pF/inch  * 5 inch = ~7.5 pF<br>RDSON<br>RPCB = RDSON<br>RDSON CL = 8 pF<br>Notes:<br>1. See IBIS models for further details.<br><!-- End of picture text -->

Figure 26. Reference Load Diagram 

##### 7.3 5.0V (4.5V - 5.5V) GPIO Output AC Specification 

Table 22. 5.0V (4.5V - 5.5V) GPIO Output AC Specification 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|TR_TF_50_S|5.0V Standard GPIO<br>rise/fall time|5|—|21|ns|Capacitance=25pF|—|
|TR_TF_50_S|5.0V Standard GPIO<br>rise/fall time|10|—|31|ns|Capacitance=50pF|—|
|TR_TF_50_SP|5.0V Standard Plus<br>GPIO rise/fall time|3.5|—|13.2|ns|DSE=0,<br>Capacitance=25pF|—|
|TR_TF_50_SP|5.0V Standard<br>Plus GPIO rise/fall<br>time|1.2|—|7.1|ns|DSE=1,<br>Capacitance=25pF|—|
|TR_TF_50_SP|5.0V Standard Plus<br>GPIO rise/fall time|7.1|—|18.8|ns|DSE=0,<br>Capacitance=50pF|—|
|TR_TF_50_SP|5.0V Standard Plus<br>GPIO rise/fall time|3.4|—|11|ns|DSE=1,<br>Capacitance=50pF|—|
|TR_TF_50_M|5.0V Medium GPIO<br>rise/fall time|1.8|—|8.2|ns|DSE=0, SRE=0,<br>Capacitance=25pF|—|
|TR_TF_50_M|5.0V Medium GPIO<br>rise/fall time|2.5|—|9.8|ns|DSE=0, SRE=1,<br>Capacitance=25pF|—|
|TR_TF_50_M|5.0V Medium GPIO<br>rise/fall time|0.8|—|4.5|ns|DSE=1, SRE=0,<br>Capacitance=25pF|—|
|TR_TF_50_M|5.0V Medium GPIO<br>rise/fall time|1.8|—|7.2|ns|DSE=1, SRE=1,<br>Capacitance=25pF|—|
|TR_TF_50_M|5.0V Medium GPIO<br>rise/fall time|4.3|—|13.2|ns|DSE=0, SRE=0,<br>Capacitance=50pF|—|
|TR_TF_50_M|5.0V Medium GPIO<br>rise/fall time|4.6|—|13.8|ns|DSE=0, SRE=1,<br>Capacitance=50pF|—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

68 / 130 

NXP Semiconductors 

I/O parameters 

Table 22. 5.0V (4.5V - 5.5V) GPIO Output AC Specification (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|TR_TF_50_M|5.0V Medium GPIO<br>rise/fall time|1.6|—|7.1|ns|DSE=1, SRE=0,<br>Capacitance=50pF|—|
|TR_TF_50_M|5.0V Medium GPIO<br>rise/fall time|2.7|—|9.6|ns|DSE=1, SRE=1,<br>Capacitance=50pF|—|
|TR_TF_50_F|5.0V Fast GPIO rise/<br>fall time|0.4|—|3.1|ns|DSE=0, SRE=0,<br>Capacitance=25pF|—|
|TR_TF_50_F|5.0V Fast GPIO rise/<br>fall time|1.5|—|6.1|ns|DSE=0, SRE=1,<br>Capacitance=25pF|—|
|TR_TF_50_F|5.0V Fast GPIO rise/<br>fall time|0.3|—|0.9|ns|DSE=1, SRE=0,<br>Capacitance=25pF|—|
|TR_TF_50_F|5.0V Fast GPIO rise/<br>fall time|0.9|—|4.1|ns|DSE=1, SRE=1,<br>Capacitance=25pF|—|
|TR_TF_50_F|5.0V Fast GPIO rise/<br>fall time|1.0|—|5.3|ns|DSE=0, SRE=0,<br>Capacitance=50pF|—|
|TR_TF_50_F|5.0V Fast GPIO rise/<br>fall time|1.9|—|7.7|ns|DSE=0, SRE=1,<br>Capacitance=50pF|—|
|TR_TF_50_F|5.0V Fast GPIO rise/<br>fall time|0.9|—|3.0|ns|DSE=1, SRE=0,<br>Capacitance=50pF|—|
|TR_TF_50_F|5.0V Fast GPIO rise/<br>fall time|1.3|—|5.1|ns|DSE=1, SRE=1,<br>Capacitance=50pF|—|



##### 7.4 3.3V (2.97V - 3.63V) GPIO Output AC Specification 

Table 23. 3.3V (2.97V - 3.63V) GPIO Output AC Specification 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|TR_TF_33_S|3.3V Standard GPIO<br>rise/fall time|6.5|—|28|ns|Capacitance=25pF|—|
|TR_TF_33_S|3.3V Standard GPIO<br>rise/fall time|11|—|43|ns|Capacitance=50pF|—|
|TR_TF_33_SP|3.3V Standard Plus<br>GPIO rise/fall time|4|—|17.5|ns|DSE=0,<br>Capacitance=25pF|—|
|TR_TF_33_SP|3.3V Standard Plus<br>GPIO rise/fall time|2.0|—|10|ns|DSE=1,<br>Capacitance=25pF|—|
|TR_TF_33_SP|3.3V Standard Plus<br>GPIO rise/fall time|8.9|—|27|ns|DSE=0,<br>Capacitance=50pF|—|
|TR_TF_33_SP|3.3V Standard Plus<br>GPIO rise/fall time|4.1|—|15|ns|DSE=1,<br>Capacitance=50pF|—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

69 / 130 

NXP Semiconductors 

Glitch Filter 

Table 23. 3.3V (2.97V - 3.63V) GPIO Output AC Specification (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|TR_TF_33_M|3.3V Medium GPIO<br>rise/fall time|2.2|—|12.3|ns|DSE=0, SRE=0,<br>Capacitance=25pF|—|
|TR_TF_33_M|3.3V Medium GPIO<br>rise/fall time|3.0|—|14|ns|DSE=0, SRE=1,<br>Capacitance=25pF|—|
|TR_TF_33_M|3.3V Medium<br>GPIO rise/fall time|0.8|—|6.6|ns|DSE=1, SRE=0,<br>Capacitance=25pF|—|
|TR_TF_33_M|3.3V Medium GPIO<br>rise/fall time|2.4|—|10.5|ns|DSE=1, SRE=1,<br>Capacitance=25pF|—|
|TR_TF_33_M|3.3V Medium GPIO<br>rise/fall time|5.1|—|17.3|ns|DSE=0, SRE=0,<br>Capacitance=50pF|—|
|TR_TF_33_M|3.3V Medium GPIO<br>rise/fall time|5.8|—|19.8|ns|DSE=0, SRE=1,<br>Capacitance=50pF|—|
|TR_TF_33_M|3.3V Medium GPIO<br>rise/fall time|2.2|—|10|ns|DSE=1, SRE=0,<br>Capacitance=50pF|—|
|TR_TF_33_M|3.3V Medium GPIO<br>rise/fall time|3.7|—|13.9|ns|DSE=1, SRE=1,<br>Capacitance=50pF|—|
|TR_TF_33_F|3.3V Fast GPIO rise/<br>fall time|0.5|—|4|ns|DSE=0, SRE=0,<br>Capacitance=25pF|—|
|TR_TF_33_F|3.3V Fast GPIO rise/<br>fall time|2.1|—|9|ns|DSE=0, SRE=1,<br>Capacitance=25pF|—|
|TR_TF_33_F|3.3V Fast GPIO rise/<br>fall time|0.4|—|2|ns|DSE=1, SRE=0,<br>Capacitance=25pF|—|
|TR_TF_33_F|3.3V Fast GPIO rise/<br>fall time|1.2|—|6.4|ns|DSE=1, SRE=1,<br>Capacitance=25pF|—|
|TR_TF_33_F|3.3V Fast GPIO rise/<br>fall time|1.1|—|7|ns|DSE=0, SRE=0,<br>Capacitance=50pF|—|
|TR_TF_33_F|3.3V Fast GPIO rise/<br>fall time|2.6|—|11|ns|DSE=0, SRE=1,<br>Capacitance=50pF|—|
|TR_TF_33_F|3.3V Fast GPIO rise/<br>fall time|0.8|—|4.2|ns|DSE=1, SRE=0,<br>Capacitance=50pF|—|
|TR_TF_33_F|3.3V Fast GPIO rise/<br>fall time|1.5|—|7.8|ns|DSE=1, SRE=1,<br>Capacitance=50pF|—|



#### 8 Glitch Filter 

The glitch filter parameters in the following table apply to the filters of WKPU pins and TRGMUX inputs 60-63. 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

70 / 130 

NXP Semiconductors 

Flash memory specification 

Table 24. Glitch Filter 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|TFILT|Glitch filter max<br>filtered pulse<br>width<sup>1, 2, 3</sup>|—|—|20|ns|—|—|
|TUNFILT|Glitch filter min<br>unfiltered pulse<br>width<sup>1, 3, 4</sup>|400|—|—|ns|—|—|



1. An input signal pulse is defined by the duration between the input signal's crossing of a Vil/Vih threshold voltage level, and the next crossing of the opposite level. 

2. Pulses shorter than defined by the maximum value are guaranteed to be filtered (not passed). 

3. Pulses in between the max filtered and min unfiltered may or may not be passed through. 

4. Pulses larger than defined by the minimum value are guaranteed to not be filtered (passed). 

#### 9 Flash memory specification 

##### 9.1 Flash memory program and erase specifications 

Table 25. Flash memory program and erase specifications 

|Symbol|Characteristic<sup>1</sup>|Typ<sup>2</sup>|Factory<br>Programmi|ng<sup>3</sup>,<sup>4</sup>|Field Updat|e||Unit|
|---|---|---|---|---|---|---|---|---|
||||Initial Max|Initial Max,<br>Full Temp|<br>Typical<br>End of<br>Life<sup>5</sup>|Lifetime|Max<sup>6</sup>||
||||20°C ≤TA<br>≤30°C|-40°C ≤TJ<br>≤150°C|-40°C ≤TJ<br>≤150°C|≤ 1,000<br>cycles|≤ 100,000<br>cycles||
|tdwpgm|Doubleword (64 bits) program time|102|122|129|111|150||µs|
|tppgm|Page (256 bits) program time|142|171|180|157|200||µs|
|tqppgm|Quad-page (1024 bits)<br>program time|314|377|396|341|450||µs|
|t8kpgm|8 KB Sector program time|20|24|26|22|30||ms|
|t8kers|8 KB Sector erase time|4.8|8.5|10.6|6.5|30||ms|
|t256kbers|256KB Block erase time|22.8|27.4|28.8|24.4|40|—|ms|
|t512kbers|512KB Block erase time|25.4|30.5|32.1|27.9|45|—|ms|
|t1mbers|1MB Block erase time|30.6|36.8|38.7|33.6|50|—|ms|
|t2mbers|2MB Block erase time|41.1|49.3|51.8|45.2|60|—|ms|



1. Program times are actual hardware programming times and do not include software overhead. Sector program times assume quad-page programming. 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

71 / 130 

NXP Semiconductors 

Flash memory specification 

2. Typical program and erase times represent the median performance and assume nominal supply values and operation at 25 °C. Typical program and erase times may be used for throughput calculations. 

3. Conditions: ≤ 25 cycles, nominal voltage. 

4. Plant Programing times provide guidance for timeout limits used in the factory. 

5. Typical End of Life program and erase times represent the median performance and assume nominal supply values. Typical End of Life program and erase values may be used for throughput calculations. 

6. Conditions: -40°C ≤TJ ≤150°C, full spec voltage. 

##### 9.2 Flash memory Array Integrity and Margin Read specifications 

Table 26. Flash memory Array Integrity and Margin Read specifications 

|Symbol|Characteristic|Min|Typical|Max<sup>1</sup> <sup>2</sup>|Units<sup>3</sup>|
|---|---|---|---|---|---|
|tai256kseq|Array Integrity time and Margin<br>Read time for sequential sequence<br>on 256KB block.|—|—|8192 x Tperiod x Nread<br>(plus 40uS adder required if User<br>Margin Read)|—|
|tai512kseq|Array Integrity time and Margin<br>Read time for sequential sequence<br>on 512KB block.|—|—|16384 x Tperiod x Nread<br>(plus 40uS adder required if User<br>Margin Read)|—|
|tai1mseq|Array Integrity time and Margin<br>Read time for sequential sequence<br>on 1MB block.|—|—|32768 x Tperiod x Nread<br>(plus 40uS adder required if User<br>Margin Read)|—|
|tai2mseq|Array Integrity time and Margin<br>Read time for sequential sequence<br>on 2MB block.|—|—|65536 x Tperiod x Nread<br>(plus 40uS adder required if User<br>Margin Read)|—|
|tai256kprop|Array Integrity time for proprietary<br>sequence on 256KB block.|—|—|106496<br>x Tperiod x Nread|—|
|tai512kprop|Array Integrity time for proprietary<br>sequence on 512KB block.|—|—|229376<br>x Tperiod x Nread|—|
|tai1mprop|Array Integrity time for proprietary<br>sequence on 1MB block.|—|—|491520<br>x Tperiod x Nread|—|
|tai2mprop|Array Integrity time for proprietary<br>sequence on 2MB block.|—|—|1048576<br>x Tperiod x Nread|—|



1. Array Integrity times need to be calculated and is dependent on system frequency and number of clocks per read. The equation presented require Tperiod (which is the unit accurate period, thus for 200 MHz, Tperiod would equal 5e-9) and Nread (which is the number of clocks required for read, including single read, dual read, quad read contribution. Thus for a read setup that requires 6 clocks to read Nread would equal 6. 

2. Array Integrity times are actual hardware execution times and do not include software overhead or system code execution overhead. 

3. The units for Array Integrity are determined by the period of the system clock. If unit accurate period is used in the equation, the results of the equation are also unit accurate. 

S32K3xx Data Sheet, Rev. 4, 04/2022 Preliminary Information 

Data Sheet: Technical Data 

72 / 130 

NXP Semiconductors 

Flash memory specification 

##### 9.3 Flash memory module life specifications 

Table 27. Flash memory module life specifications 

|Symbol|Characteristic|Conditions|Min|Typical|Units|
|---|---|---|---|---|---|
|Array P/E<br>cycles|Number of program/erase cycles per block<br>for 256 KB and 512 KB blocks using<br>Sector Erase.|—|100,000|—|P/E<br>cycles|
||Number of program/erase cycles per block for<br>1 MB and 2 MB blocks using Sector Erase.|—|1,000|—|P/E<br>cycles|
||Number of program/erase cycles per block<br>using Block Erase<sup>1</sup>|—|25|—|P/E<br>cycles|
|Data<br>retention|Minimum data retention.|Blocks with 0 - 1,000<br>P/E cycles.|20|—|Years|
|||Blocks with 100,000<br>P/E cycles.|10|—|Years|



1. Program and erase supported for factory conditions. Nominal supply values and operation at 25°C. 

###### 9.3.1 Data retention vs program/erase cycles 

Graphically, Data Retention versus Program/Erase Cycles can be represented by the following figure. 

The spec window represents qualified limits. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0073-09.png)


<!-- Start of picture text -->
25<br>20<br>15<br>10<br>5<br>0<br>1 10 100 1000 10000 100000 1000000<br>P/E Cycles (Sector Erases)<br>Minimum Data Retention Life (Years)<br><!-- End of picture text -->

Figure 27. Data retention vs program/erase cycles 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

73 / 130 

NXP Semiconductors 

Flash memory specification 

##### 9.4 Flash memory AC timing specifications 

Table 28. Flash memory AC timing specifications 

|Symbol|Characteristic|Min|Typical|Max|Units|
|---|---|---|---|---|---|
|tdone|Time from 0 to 1 transition on the MCR[EHV] bit<br>initiating a program/erase until the MCR[DONE]<br>bit is cleared.|—|—|5|ns|
|tdones|Time from 1 to 0 transition on the MCR[EHV] bit<br>aborting a program/erase until the MCR[DONE]<br>bit is set to a 1.|5 plus four<br>system clock<br>periods|—|22 plus four<br>system clock<br>periods<sup>1</sup>|µs|
|tdrcv|Time to recover once exiting low power mode.|14 plus seven<br>system clock<br>periods<sup>2</sup>|17.5 plus<br>seven system<br>clock periods|21 plus seven<br>system clock<br>periods|µs|
|taistart|Time from 0 to 1 transition of UT0[AIE] initiating a<br>Margin Read or Array Integrity until the UT0[AID]<br>bit is cleared. This time also applies to the<br>resuming from a suspend or breakpoint by<br>clearing UT0[AISUS] or clearing UT0[NAIBP]|—|—|5|ns|
|taistop|Time from 1 to 0 transition of UT0[AIE] initiating<br>an Array Integrity abort until the UT0[AID] bit is<br>set. This time also applies to the UT0[AISUS] to<br>UT0[AID] setting in the event of a Array Integrity<br>suspend request.|—|—|50<br>system clock<br>periods|ns|
|tmrstop|Time from 1 to 0 transition of UT0[AIE] initiating<br>a Margin Read abort until the UT0[AID] bit is<br>set. This time also applies to the UT0[AISUS] to<br>UT0[AID] setting in the event of a Margin Read<br>suspend request.|—|—|26<br>plus fifteen<br>system clock<br>periods|µs|



> 1. For Block Erase, Tdones times may be 3x max spec. 

2. In extreme cases (1 block configurations) Tdrcv min may be faster (12uS plus seven system clocks) 

##### 9.5 Flash memory read timing parameters 

Table 29. Flash Read Wait State Settings (S32K344, S32K324, S32K314, S32K342, S32K322, S32K341, S32K312, and S32K311) 

|Flash Frequency|RWSC setting|
|---|---|
|250 KHz < Freq ≤ 66 MHz|1|
|66 MHz < Freq ≤ 100 MHz|2|
|100 MHz < Freq ≤ 133 MHz|3|
|133 MHz < Freq ≤ 167 MHz|4|
|167 MHz < Freq ≤ 200 MHz|5|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

74 / 130 

NXP Semiconductors 

Analog modules 

Table 29. Flash Read Wait State Settings (S32K344, S32K324, S32K314, S32K342, S32K322, S32K341, S32K312, and S32K311) (continued) 

|Flash Frequency|RWSC setting|
|---|---|
|200 MHz < Freq ≤ 233 MHz|6|
|233 MHz < Freq ≤ 250 MHz|7|



Table 30. Flash Read Wait State Settings (S32K358, S32K348, S32K338, and S32K328) 

|Flash Frequency|RWSC setting|
|---|---|
|250 KHz < Freq ≤ 60 MHz|1|
|60 MHz < Freq ≤ 90 MHz|2|
|90 MHz < Freq ≤ 120 MHz|3|
|120 MHz < Freq ≤ 150 MHz|4|
|150 MHz < Freq ≤ 180 MHz|5|
|180 MHz < Freq ≤ 210 MHz|6|
|210 MHz < Freq ≤ 240 MHz|7|
|240 MHz < Freq ≤ 250 MHz|8|



#### 10 Analog modules 

##### 10.1 SAR ADC 

All below specs are applicable when only one ADC instance is in operation and averaging is used. GPIO activity on pins adjacent to ADC channels, or reference, may introduce some degradation on the analog input paths. For parallel/simultaneous operation of two or three ADCs, either for sampling the same channel by each ADC, or for sampling different channels by each ADC, some amount of decrease in performance can be expected. Care must be taken to stagger each ADC conversions, in particular the sample phase, to minimize the impact of simultaneous conversions. ADC performance specifications are guaranteed when calibration uses maximum averaging i.e. when AVGEN = 1 and AVGS = 3. When using ADC averaging, see Reference Manual to determine the most appropriate settings for AVGS. 

Table 31. SAR ADC 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|VDD_HV_A|ADC Supply<br>Voltage<sup>1</sup>|2.97|—|5.5|V|—|—|
|DVREFL|VSS / VREFL<br>Voltage Difference<sup>2</sup>|-100|—|100|mV|—|—|
|VAD_INPUT|ADC Input Voltage<sup>3</sup>|VREFL|—|VREFH|V|—|—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 Preliminary Information 

Data Sheet: Technical Data 

75 / 130 

NXP Semiconductors 

Analog modules 

Table 31. SAR ADC (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|fAD_CK|ADC Clock<br>Frequency<br>(S32K344,<br>S32K324, S32K314,<br>S32K342, S32K341,<br>S32K322)|10|—|80|MHz|—|—|
|fAD_CK|ADC Clock<br>Frequency<br>(S32K312,<br>S32K311, S32K358,<br>S32K348, S32K338,<br>S32K328)|10|—|120|MHz|—|—|
|tSAMPLE|ADC Input Sampling<br>Time|275|—|—|ns|—|—|
|tCONV|ADC Total<br>Conversion Time|1|—|—|us|12-bit result|—|
|tCONV|ADC Total<br>Conversion Time|0.9|—|—|us|10-bit result|—|
|CAD_INPUT|ADC Input<br>Capacitance|—|—|13.8|pF|ADC component<br>plus pad capacitance<br>(~2pF)|—|
|RAD_INPUT|ADC Input<br>Resistance|—|—|4.6|KΩ|ADC + mux+SOC<br>routing|—|
|RS|Source Impedance,<br>precision channels|—|20|TBD|Ω|—|—|
|RS|Source Impedance,<br>standard channels|—|20|TBD|Ω|—|—|
|TUE|ADC Total<br>Unadjusted Error<sup>4</sup>|—|+/-4|+/-6|LSB|without adjacent pin<br>current injection|—|
|TUE|ADC Total<br>Unadjusted Error<sup>4</sup>|—|+/-4|+/-8|LSB|with up to +/-3mA<br>of current injection on<br>adjacent pins|—|
|IAD_REF|Current<br>Consumption on<br>ADC Reference pin,<br>VREFH.|—|—|200|uA|Per ADC for dedicated<br>or shared reference<br>pins|—|
|IDDA|Current<br>Consumption on<br>ADC Supply,<br>VDD_HV_A|—|2.1|—|mA|Current consumption<br>per ADC module, ADC<br>enabled and converting|—|
|CS|Sampling<br>Capacitance|6.4<br>(gain=0)|7.36<br>(gain=0)|8.32<br>(gain=0)|pF|all channels|—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

76 / 130 

NXP Semiconductors 

Analog modules 

Table 31. SAR ADC (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|||9.72<br>pF(gain=<br>max)|11.12<br>pF(gain=<br>max)|12.52<br>(gain=ma<br>x)||||
|RAD|Sampling Switch<br>Impedance|80|170|520|Ohm|all channels|—|
|CP1|Pin capacitance|1.42|—|5.30|pF|all channels|—|
|CP1|Pin capacitance|1.42|—|4.38|pF|Precision channels|—|
|CP1|Pin capacitance|1.61|—|5.30|pF|Standard channels|—|
|CP2|Analog Bus<br>Capacitance|0.32|—|4.18|pF|all channels|—|
|CP2|Analog Bus<br>Capacitance|0.32|—|1.42|pF|Precision channels|—|
|CP2|Analog Bus<br>Capacitance|0.497|—|4.18|pF|Standard channels|—|
|RSW1|Channel selection<br>Switch impedance|65.9|—|1410|Ohm|all channels|—|
|RSW1|Channel selection<br>Switch impedance|65.9|—|712|Ohm|Precision channels|—|
|RSW1|Channel selection<br>Switch impedance|65.9|—|1410|Ohm|Standard channels|—|



1. Appropriate decoupling capacitors to be used to filter noise on the supplies. See application note AN5032 for reference supply design for SAR ADC. 

2. VSS and VREFL should be shorted on PCB. 100mV difference between VSS and VREFL is for transient only (not for DC). 

3. This is ADC Input range for ADC accuracy guaranteed in this input range only. For SoC Pin capability, see Operation Condition Section. 

4. TUE spec for precision and standard channels is based on 12-bit level resolution. 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

77 / 130 

NXP Semiconductors 

Analog modules 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0078-02.png)


<!-- Start of picture text -->
EXTERNAL CIRCUIT INTERNAL CIRCUIT SCHEME<br>VREFH<br>Channel<br>Selection Sampling<br>Source Filter Current Limiter<br>RS RF RL RSW1 RAD<br>VA CF CP1 CP2 CS<br>RS Source Impedance<br>RF Filter Resistance<br>CF Filter Capacitance<br>RL Current Limiter Resistance<br>RSW1 Channel Selection Switch Impedance<br>RAD Sampling Switch Impedance<br>CP Pin Capacitance (two contributions: CP1, CP2)<br>CS Sampling Capacitance<br><!-- End of picture text -->

Figure 28. SAR ADC Input Circuit 

##### 10.2 Supply Diagnosis 

The table below gives the specification for the on die supply diagnosis. 

Table 32. Supply Diagnosis 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|AN_ACC|Offset to internally<br>monitored supply at<br>ADC input<sup>1, 2, 3</sup>|-5|0|5|%|—|—|
|AN_T_on|Switching time from<br>closed (OFF) to<br>conducting (ON)<sup>3</sup>|—|2.5|12|ns|—|—|
|AN_TADCSA|Required ADC<br>sampling time<sup>1</sup>|1.2|—|—|µs|—|—|



1. Required ADC sampling time specified by parameter AN_TADCSA needs to be used at the ADC conversion to guarantee the specified accuracy. A smaller sampling time leads to a less accurate result. 

2. If V15 > VDD_HV_A +100mV then the V15 measurement via anamux may be imprecise. 

3. These specs will have degraded performance when used in extended supply voltage operation range, i.e. normal supply voltage range specification is exceeded. 

##### 10.3 Low Power Comparator (LPCMP) 

Table 33. Low Power Comparator (LPCMP) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|idda(IDHSS)|vdda Supply<br>Current, High Speed<br>Mode<sup>1, 2</sup>|—|240|—|uA|—|—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 Preliminary Information 

Data Sheet: Technical Data 

78 / 130 

NXP Semiconductors 

Analog modules 

Table 33. Low Power Comparator (LPCMP) (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|idda(IDLSS)|vdda Supply<br>Current, Low Speed<br>Mode<sup>1, 2</sup>|—|17|—|uA|—|—|
|idda(IDHSS)|vdda Supply<br>Current, high speed<br>mode, DAC only<sup>1</sup>|—|10|—|uA|—|—|
|idda_lkg|vdda Supply<br>Current, module<br>disabled<sup>1</sup>|—|2|—|nA|vdda=5.5V, T=25C|—|
|TDHSB|Propagation Delay,<br>High Speed Mode<sup>3</sup>|—|—|200|ns|—|—|
|TDLSB|Propagation Delay,<br>Low Speed mode<sup>3</sup>|—|—|2|us|—|—|
|TDHSS|Propagation Delay,<br>High Speed Mode<sup>4</sup>|—|—|400|ns|—|—|
|TDLSS|Propagation Delay,<br>Low Speed mode<sup>4</sup>|—|—|5|us|—|—|
|TIDHS|Initialization Delay,<br>High Speed Mode<sup>5</sup>|—|—|3|us|—|—|
|TIDLS|Initialization Delay,<br>Low Speed mode<sup>5</sup>|—|—|30|us|—|—|
|VAIO|Analog Input Offset<br>Voltage, High Speed<br>Mode|-25|+/-1|25|mV|—|—|
|VAIO|Analog Input Offset<br>Voltage, Low Speed<br>mode|-40|+ /- 5|40|mV|—|—|
|VAHYST0|Analog Comparator<br>Hysteresis, High<br>Speed Mode|—|0|—|mV|HYSTCTR[1:0]= 2'b00|—|
|VAHYST1|Analog Comparator<br>Hysteresis, High<br>Speed Mode|—|14|41|mV|HYSTCTR[1:0]= 2'b01|—|
|VAHYST2|Analog Comparator<br>Hysteresis, High<br>Speed Mode|—|27|76|mV|HYSTCTR[1:0]= 2'b10|—|
|VAHYST3|Analog Comparator<br>Hysteresis, High<br>Speed Mode|—|40|111|mV|HYSTCTR[1:0]= 2'b11|—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

79 / 130 

NXP Semiconductors 

Analog modules 

Table 33. Low Power Comparator (LPCMP) (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|VAHYST0|Analog Comparator<br>Hysteresis, Low<br>Speed mode|—|0|—|mV|HYSTCTR[1:0]= 2'b00|—|
|VAHYST1|Analog Comparator<br>Hysteresis, Low<br>Speed mode|—|8|60|mV|HYSTCTR[1:0]= 2'b01|—|
|VAHYST2|Analog Comparator<br>Hysteresis, Low<br>Speed mode|—|15|113|mV|HYSTCTR[1:0]= 2'b10|—|
|VAHYST3|Analog Comparator<br>Hysteresis, Low<br>Speed mode|—|23|165|mV|HYSTCTR[1:0]= 2'b11|—|
|INL|DAC integral<br>linearity<sup>1, 6, 7</sup>|-1|—|1|LSB|vrefh_cmp = vdda,<br>vrefl_cmp = vss|—|
|INL|DAC integral<br>linearity<sup>1, 6, 7</sup>|-1.5|—|1.5|LSB|vrefh_cmp < vdda|—|
|DNL|DAC differential<br>linearity<sup>1, 6</sup>|-1|—|1|LSB|vrefh_cmp = vdda,<br>vrefl_cmp = vss|—|
|DNL|DAC differential<br>linearity<sup>1, 6</sup>|-1.5|—|1.5|LSB|vrefh_cmp < vdda|—|
|tDDAC|DAC Initialization<br>and switching<br>settling time|—|—|30|us|—|—|
|VAIN|Analog input voltage|0|—|VDDA|V|—|—|



1. vdda is comparator HV supply and internally shorted to VDD_HV_A pin. vss is comparator  ground 

2. Difference at input > 200mV 

3. Applied +/- (100 mV + VAHYST0/1/2/3 + max. of VAIO) around switch point 

4. Applied +/- (30 mV + 2 x VAHYST0/1/2/3 + max. of VAIO) around switch point 

5. Applied ± (100 mV + VAHYST0/1/2/3 ). 

6. 1 LSB = (vrefh_cmp - vrefl_cmp) /256. vrefh_cmp and vrefl_cmp are comparator reference high and low 

7. Calculation method used: Linear Regression Least Square Method 

For Comparator IN signals adjacent to VDD_HV_A/VDD_HV_B/VSS or XTAL/EXTAL or switching pins cross coupling may happen and hence hysteresis settings can be used to obtain the desired Comparator performance. Additionally an external capacitor to ground (1nF) should be used to filter noise on input signal. Also source drive should not be weak (Signal with <50K pull up/down is recommended). 

For devices where the VDD_HV_B domain is present, ACMP0 channels must only be selected/enabled when VDD_HV_A >= VDD_HV_B. These channels must be disabled when VDD_HV_A goes below VDD_HV_B. 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

80 / 130 

NXP Semiconductors 

Analog modules 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0081-02.png)


<!-- Start of picture text -->
90<br>Hysteresis<br>(mV)<br>60<br>30<br>0<br>0 0.3 0.6 0.9 1.2 1.5 1.8 2.1 2.4 2.7 3.0 3.3 Vin level (V)<br>25 Junction Temp (°C)<br>3.3 VDD_HV_A (V)<br>HYSTCTR setting<br>00 01 10 11<br><!-- End of picture text -->

Figure 29. Typical Hysteresis vs Vin level (VDD_HV_A = 3.3 V, High Speed Mode) 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0081-04.png)


<!-- Start of picture text -->
60<br>Hysteresis<br>(mV)<br>40<br>20<br>0<br>0 0.3 0.6 0.9 1.2 1.5 1.8 2.1 2.4 2.7 3.0 3.3 Vin level (V)<br>25 Junction Temp (°C)<br>3.3 VDD_HV_A (V)<br>HYSTCTR setting<br>00 01 10 11<br><!-- End of picture text -->

Figure 30. Typical Hysteresis vs Vin level (VDD_HV_A = 3.3 V, Low Speed Mode) 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0081-06.png)


<!-- Start of picture text -->
90<br>Hysteresis<br>(mV)<br>60<br>30<br>0<br>0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0 4.5 5.0 Vin level (V)<br>25 Junction Temp (°C)<br>5 VDD_HV_A (V)<br>HYSTCTR setting<br>00 01 10 11<br><!-- End of picture text -->

Figure 31. Typical Hysteresis vs Vin level (VDD_HV_A = 5 V, High Speed Mode).png 

S32K3xx Data Sheet, Rev. 4, 04/2022 Preliminary Information 

Data Sheet: Technical Data 

81 / 130 

NXP Semiconductors 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0082-01.png)


<!-- Start of picture text -->
Analog modules<br>60<br>Hysteresis<br>(mV)<br>40<br>20<br>0<br>0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0 4.5 5.0 Vin level (V)<br>25 Junction Temp (°C)<br>5 VDD_HV_A (V)<br>HYSTCTR setting<br>00 01 10 11<br>Figure 32. Typical Hysteresis vs Vin level (VDD_HV_A = 5 V, Low Speed Mode).png<br><!-- End of picture text -->

##### 10.4 Temperature Sensor 

The table below gives the specification for the on die temperature sensor. 

Table 34. Temperature Sensor 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|TS_TJ|Junction<br>temperature<br>monitoring range|-40|—|150|°C|—|—|
|TS_IV25|ON state current<br>consumption on V25|—|400|—|µA|ETS_EN=1|—|
|TS_ACC1|Temperature output<br>error at circuit output<br>(Voltage)<sup>1, 2, 3</sup>|-5|0|+5|°C|100 °C < Tj <= 150 °C|—|
|TS_ACC2|Temperature output<br>error at circuit output<br>(Voltage)<sup>1, 2, 3</sup>|-10|0|+10|°C|-40 °C <= Tj <=100 °C|—|
|TS_TSTART|Circuit start up time|—|4|30|µs|—|—|
|TS_TADCSA|Required ADC<br>sampling time<sup>1</sup>|1.2|—|—|µs|—|—|



1. Required ADC sampling time specified by parameter TS_TADCSA needs to be used at the ADC conversion to guarantee the specified accuracy. A smaller sampling time leads to a less accurate result. 

2. Note: The temperature sensor measures the junction temperature Tj at the location where it is placed on die. The local Tj is modulated by current and previous active state of the circuit elements on die. 

3. The error caused by ADC conversion and provided temperature calculation formula is not included. 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

82 / 130 

NXP Semiconductors 

Clocking modules 

#### 11 Clocking modules 

##### 11.1 FIRC 

Table 35. FIRC 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|fFIRC|FIRC nominal<br>Frequency|—|48|—|MHz|—|—|
|FACC|FIRC Frequency<br>deviation across<br>process, voltage,<br>and temperature<br>after trimming|-5|—|5|%|—|—|
|TSTART|Startup Time<sup>1</sup>|—|10|25|us|—|—|



> 1. Startup time is for reference only. 

##### 11.2 SIRC 

Table 36. SIRC 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|fSIRC|SIRC nominal<br>Frequency|—|32|—|KHz|—|—|
|fSIRC_ACC|SIRC Frequency<br>deviation across<br>process, voltage,<br>and temperature<br>after trimming|-10|—|10|%|—|—|
|TSIRC_start|SIRC Startup Time<sup>1</sup>|—|—|3|ms|—|—|
|TSIRC_DC|SIRC duty cycle|30|—|70|%|—|—|



> 1. Startup time is for information only. 

##### 11.3 PLL 

Table 37. PLL 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|FPLL_in|PLL input frequency|8|—|40|MHz|This is the frequency<br>after the Reference<br>Divider within the PLL|—|
|FPLL_out|PLL output<br>frequency (PLL_PHI<br>n_CLK)|48<br>Table co|—<br>ntinues on|320<br>the next pa|MHz<br>ge...|—|—|



S32K3xx Data Sheet, Rev. 4, 04/2022 Preliminary Information 

Data Sheet: Technical Data 

83 / 130 

NXP Semiconductors 

Clocking modules 

Table 37. PLL (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|FPLL_vcoRange|VCO Frequency<br>range|640|—|1280|MHz|—|—|
|FPLL_DS|Modulation Depth<br>(down spread)|-0.5|—|-3|%|—|—|
|FPLL_FM|Modulation<br>frequency|—|—|32|KHz|—|—|
|TPLL_start|PLL lock time|—|—|1|ms|—|—|
|JPLL_cyc|PLL period jitter (pk­<br>pk)<sup>1, 2, 3</sup>|—|—|237|ps|FPLL_out = 240MHz,<br>Integer Mode|—|
|JPLL_cyc|PLL period jitter (pk­<br>pk)<sup>1, 2, 3</sup>|—|—|487|ps|FPLL_out = 240MHz,<br>Fractional Mode|—|
|JPLL_acc|PLL accumulated<br>jitter (pk-pk)<sup>1, 2, 3</sup>|—|—|840|ps|FPLL_out = 240MHz,<br>Integer Mode|—|
|JPLL_acc|PLL accumulated<br>jitter (pk-pk)<sup>1, 2, 3</sup>|—|—|1680|ps|FPLL_out = 240MHz,<br>Fractional Mode|—|
|JPLL_cyc|PLL period jitter (pk­<br>pk)<sup>1, 2, 3</sup>|—|—|295|ps|FPLL_out = 160MHz,<br>Integer Mode|—|
|JPLL_cyc|PLL period jitter (pk­<br>pk)<sup>1, 2, 3</sup>|—|—|670|ps|FPLL_out = 160MHz,<br>Fractional Mode|—|
|JPLL_acc|PLL accumulated<br>jitter (pk-pk)<sup>1, 2, 3</sup>|—|—|840|ps|FPLL_out = 160MHz,<br>Integer Mode|—|
|JPLL_acc|PLL accumulated<br>jitter (pk-pk)<sup>1, 2, 3</sup>|—|—|1680|ps|FPLL_out = 160MHz,<br>Fractional Mode|—|
|JPLL_cyc|PLL period jitter (pk­<br>pk)<sup>1, 2, 3</sup>|—|—|353|ps|FPLL_out = 120MHz,<br>Integer Mode|—|
|JPLL_cyc|PLL period jitter (pk­<br>pk)<sup>1, 2, 3</sup>|—|—|853|ps|FPLL_out = 120MHz,<br>Fractional Mode|—|
|JPLL_acc|PLL accumulated<br>jitter (pk-pk)<sup>1, 2, 3</sup>|—|—|840|ps|FPLL_out = 120MHz,<br>Integer Mode|—|
|JPLL_acc|PLL accumulated<br>jitter (pk-pk)<sup>1, 2, 3</sup>|—|—|1680|ps|FPLL_out = 120MHz,<br>Fractional Mode|—|



> 1. For SSCG, jitter due to systematic modulation needs to be added as per applied modulation. 

2. Jitter numbers are valid only at IP boundary and does not include any degradation due to IO pad for clock measurement. 

3. Jitter numbers calculated by extrapolating RMS jitter numbers to +/- 7 sigma . 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

84 / 130 

NXP Semiconductors 

Clocking modules 

##### 11.4 Fast External Oscillator (FXOSC) 

Table 38. Fast External Oscillator (FXOSC) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|FREQ_BYPASS|Input clock<br>frequency in bypass<br>mode<sup>1</sup>|—|—|50|MHz|—|—|
|TRF_BYPASS|Input clock rise/fall<br>time in bypass<br>mode<sup>1</sup>|—|—|5|ns|—|—|
|CLKIN_DUTY_<br>BYPASS|Input clock duty<br>cycle in bypass<br>mode<sup>1</sup>|47.5|—|52.5|%|—|—|
|FXOSC_CLK|output clock<br>frequency in crystal<br>mode|8|—|40|MHz|—|—|
|TFXOSC|Fxosc start up<br>time (ALC enabled)<sup>2</sup>|—|—|2|ms|—|—|
|IFXOSC|Oscillator Analog<br>circuit supply<br>current, V25 supply|—|—|1|mA|using 8, 16 or 40 MHz<br>crystal|—|
|GM|Amplifier<br>Transconductance|9.7|—|18.5|mA/V|GM_SEL[3:0] =<br>4`b1111|—|



1. For bypass mode applications, the EXTAL pin should be driven low when FXOSC is in off/disabled state. 

2. The startup time specification is valid only when the recommended crystal and load capacitors are used. For higher load capacitances, the actual startup time might be higher. 

To ensure stable oscillations, FXOSC incorporates the feedback resistance internally. 

Drive level is a crystal specification and if crystal load capacitance is increased beyond the recommended value, it may violate the crystal drive level rating. In such cases, contact NXP sales representative for selecting the correct crystal. 

Crystal oscillator circuit provides stable oscillations when gmXOSC > 5 * gm_crit. The gm_crit is defined as: gm_crit = 4 * (ESR + RS) * (2πF)<sup>2</sup> * (C0 + CL)<sup>2</sup> 

where: 

- gmXOSC is the transconductance of the internal oscillator circuit 

- ESR is the equivalent series resistance of the external crystal 

- RS is the series resistance connected between XTAL pin and external crystal for current limitation 

- F is the external crystal oscillation frequency 

- C0 is the shunt capacitance of the external crystal 

- CL is the external crystal total load capacitance. CL = Cs+ [C1*C2/(C1+C2)] 

- Cs is stray or parasitic capacitance on the pin due to any PCB traces 

- C1, C2 external load capacitances on EXTAL and XTAL pins 

See manufacture datasheet for external crystal component values 

Figure 33. Oscillation build-up equation 

S32K3xx Data Sheet, Rev. 4, 04/2022 Preliminary Information 

Data Sheet: Technical Data 

85 / 130 

NXP Semiconductors 

Clocking modules 

~~<mark>NOTE</mark>~~ 

To improve the FXOSC jitter & duty cycle performance, the functionality of the pin next to the Oscillator (namely, PTE14 in MAXQFP172 and PTE3 in MAXQFP100 package) must be limited to static GPIO operation. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0086-04.png)


Figure 34. Block diagram 

##### 11.5 Slow Crystal Oscillator (SXOSC) 

Table 39. Slow Crystal Oscillator (SXOSC) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|Fsxosc|Oscillator Crystal<br>Frequency<sup>1</sup>|—|32.768|—|KHz|IP in crystal mode|—|
|Tstart|SXOSC startup time|—|—|2|s|start up time is<br>dependent upon board<br>and crystal model.|—|
|ISXOSC|Oscillator Analog<br>circuit supply current|—|2.1|—|uA|—|—|
|gm_sxocs|NMOS Amplifier<br>Transconductance|3|—|40|u A/V|—|—|



S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

86 / 130 

NXP Semiconductors 

Communication interfaces 

###### 1. Supports single frequency 

#### 12 Communication interfaces 

##### 12.1 LPSPI 

###### 12.1.1 LPSPI 

The Low Power Serial Peripheral Interface (LPSPI) provides a synchronous serial bus with master and slave operations. Many of the transfer attributes are programmable. The following table provides timing characteristics for classic LPSPI timing modes. 

1. All timing is shown with respect to 20% VDD_HV_A/B and 80% VDD_HV_A/B thresholds. 

2. All measurements are with maximum output load of 30 pF, input transition of 1 ns and pad configured with fastest slew setting (DSE = 1'b1). 

Table 40. LPSPI 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|fperiph|Peripheral Frequenc<br>y<sup>1, 2, 3</sup>|—|—|40|MHz|Master|—|
|fperiph|Peripheral Frequenc<br>y<sup>1, 2, 3</sup>|—|—|40|MHz|Slave|—|
|fperiph|Peripheral Frequenc<br>y<sup>1, 3, 4</sup>|—|—|80|MHz|Master Loopback|—|
|fop|Operating frequency|—|—|15|MHz|Slave|1|
|fop|Operating frequency|—|—|15|MHz|Master|1|
|fop|Operating<br>frequency<sup>5</sup>|—|—|10|MHz|Slave_10Mbps|1|
|fop|Operating<br>frequency<sup>5</sup>|—|—|10|MHz|Master_10Mbps|1|
|fop|Operating<br>frequency<sup>4, 6</sup>|—|—|20|MHz|Master Loopback|1|
|tSPSCK|SPSCK period|66|—|—|ns|Slave|2|
|tSPSCK|SPSCK period|66|—|—|ns|Master|2|
|tSPSCK|SPSCK period<sup>4</sup>|50|—|—|ns|Master Loopback|2|
|tSPSCK|SPSCK period|100|—|—|ns|Master_10Mbps|—|
|tSPSCK|SPSCK period|100|—|—|ns|Slave_10Mbps|—|
|tLEAD|Enable lead time<br>(PCS to SPSCK<br>delay)<sup>7</sup>|—|—|—|ns|Slave|3|
|tLEAD|Enable lead time<br>(PCS to SPSCK<br>delay)<sup>7</sup>|30|—|—|ns|Master|3|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

87 / 130 

NXP Semiconductors 

Communication interfaces 

Table 40. LPSPI (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|tLEAD|Enable lead time<br>(PCS to SPSCK<br>delay)<sup>4, 7</sup>|30|—|—|ns|Master Loopback|3|
|tLAG|Enable lag time<br>(After SPSCK<br>delay)<sup>8</sup>|—|—|—|ns|Slave|4|
|tLAG|Enable lag time<br>(After SPSCK<br>delay)<sup>8</sup>|30|—|—|ns|Master|4|
|tLAG|Enable lag time<br>(After SPSCK<br>delay)<sup>4, 8</sup>|30|—|—|ns|Master Loopback|4|
|tWSPCK|Clock (SPSCK) high<br>or low time (SPSCK<br>duty cycle)<sup>9</sup>|tSPSCK/<br>2 - 3|—|tSPSCK/<br>2 + 3|ns|Slave|5|
|tWSPCK|Clock (SPSCK) high<br>or low time (SPSCK<br>duty cycle)<sup>9</sup>|tSPSCK/<br>2 - 3|—|tSPSCK/<br>2 + 3|ns|Master|5|
|tWSPCK|Clock (SPSCK) high<br>or low time (SPSCK<br>duty cycle)<sup>4, 9</sup>|tSPSCK/<br>2 - 3|—|tSPSCK/<br>2 + 3|ns|Master Loopback|5|
|tSU|Data setup<br>time(inputs)|6|—|—|ns|Slave|6|
|tSU|Data setup<br>time(inputs)|25|—|—|ns|Master|6|
|tSU|Data setup<br>time(inputs)|5|—|—|ns|Slave_10Mbps|6|
|tSU|Data setup<br>time(inputs)|36|—|—|ns|Master_10Mbps|6|
|tSU|Data setup<br>time(inputs)<sup>4</sup>|6|—|—|ns|Master_Loopback|6|
|tHO|Data hold<br>time(inputs)|3|—|—|ns|Slave|7|
|tHO|Data hold<br>time(inputs)|0|—|—|ns|Master|7|
|tHO|Data hold<br>time(inputs)|4|—|—|ns|Slave_10Mbps|7|
|tHO|Data hold<br>time(inputs)|0|—|—|ns|Master_10Mbps|7|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

88 / 130 

NXP Semiconductors 

Communication interfaces 

Table 40. LPSPI (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|tHO|Data hold<br>time(inputs)<sup>4</sup>|3|—|—|ns|Master Loopback|7|
|tA|Slave access time|—|—|50|ns|Slave|8|
|tDIS|Slave MISO (SOUT)<br>disable time|—|—|50|ns|Slave|9|
|tV|Data valid (after<br>SPSCK edge)|—|—|26|ns|Slave|10|
|tV|Data valid (after<br>SPSCK edge)|—|—|14|ns|Master|10|
|tV|Data valid (after<br>SPSCK edge)|—|—|36|ns|Slave_10Mbps|10|
|tV|Data valid (after<br>SPSCK edge)|—|—|21|ns|Master_10Mbps|10|
|tV|Data valid (after<br>SPSCK edge)<sup>4</sup>|—|—|17.5|ns|Master Loopback|10|
|tHO|Data hold time<br>(outputs)|3|—|—|ns|Slave|11|
|tHO|Data hold time<br>(outputs)|-8|—|—|ns|Master|11|
|tHO|Data hold time<br>(outputs)|3|—|—|ns|Slave_10Mbps|11|
|tHO|Data hold time<br>(outputs)|-15|—|—|ns|Master_10Mbps|11|
|tHO|Data hold time<br>(outputs)<sup>4</sup>|-2|—|—|ns|Master Loopback|11|
|tRI/FI|Rise/Fall time input|—|—|1|ns|Slave|12|
|tFI/RI|Rise/Fall time input|—|—|1|ns|Master|12|
|tFI/RI|Rise/Fall time input<sup>4</sup>|—|—|1|ns|Master Loopback|12|
|tFO/RO|Rise/Fall time output|—|—|25|ns|Slave|13|
|tFO/RO|Rise/Fall time output|—|—|25|ns|Master|13|
|tFO/RO|Rise/Fall time<br>output<sup>4</sup>|—|—|25|ns|Master Loopback|13|



1. tperiph = 1/fperiph 

2. For LPSPI0 instance, max. peripheral frequency is equal to AIPS_PLAT_CLK. 

3. fperiph = LPSPI peripheral clock 

4. Master Loopback mode: In this mode LPSPI_SCK clock is delayed for sampling the input data which is enabled by setting LPSPI_CFGR1[SAMPLE] bit as 1. 

5. These specifications apply to the SPI operation, as master or slave, at up to 10 Mbps for the combinations not indicated in the table below. Unless otherwise noted, all other ‘master’ and ‘slave’ specifications are also applicable in the 10Mbps configurations. See table "LPSPI 20 MHz and 15 MHz Combinations. 

6. LPSPI0 support up to 20MHz on fast pin. 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

89 / 130 

NXP Semiconductors 

Communication interfaces 

7. Minimum configuration value for CR[PCSSCK] field is 3(0x00000011). 

8. Minimum configuration value for CCR[SCKPCS] field is 3(0x00000011). 

9. While selecting odd dividers, ensure Duty Cycle is meeting this parameter. 

fperiph = LPSPI peripheral clock 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0090-06.png)


<!-- Start of picture text -->
SS 1<br>(OUTPUT)<br>2 12 4<br>3 13<br>SPSCK<br>(CPOL = 0)<br>(OUTPUT)<br>5 5 12 13<br>SPSCK<br>(CPOL = 1)<br>(OUTPUT)<br>6 7<br>MISO<br>MSB IN 2 BIT 6 ... 1 LSB IN<br>(INPUT)<br>10 11<br>MOSI<br>MSB OUT 2 BIT 6 ... 1 LSB OUT<br>(OUTPUT)<br><!-- End of picture text -->

Figure 35. LPSPI Master Mode Timing (CPHA=0) 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0090-08.png)


<!-- Start of picture text -->
SS 1<br>(OUTPUT)<br>2 4<br>3 12 13<br>SPSCK<br>(CPOL = 0)<br>(OUTPUT)<br>5 5 12 13<br>SPSCK<br>(CPOL = 1)<br>(OUTPUT)<br>6 7<br>MISO<br>MSB IN 2 BIT 6 ... 1 LSB IN<br>(INPUT)<br>10 11<br>MOSI<br>PORT DATA MASTER MSB OUT BIT 6 ... 1 MASTER LSB OUT PORT DATA<br>(OUTPUT)<br><!-- End of picture text -->

Figure 36. LPSPI Master Mode Timing (CPHA=1) 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

90 / 130 

NXP Semiconductors 

Communication interfaces 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0091-02.png)


<!-- Start of picture text -->
SS<br>(INPUT)<br>2 12 4<br>3 13<br>SPSCK<br>(CPOL = 0)<br>(INPUT)<br>5 5 12 13<br>SPSCK<br>(CPOL = 1) 9<br>(INPUT)<br>8 10 11 11<br>MISO<br>SLAVE MSB BIT 6 ... 1 SLAVE LSB OUT<br>(OUTPUT)<br>6 7<br>MOSI<br>MSB IN BIT 6 ... 1 LSB IN<br>(INPUT)<br>Figure 37. LPSPI Slave Mode Timing (CPHA=0)<br>SS<br>(INPUT)<br>2 4<br>3 12 13<br>SPSCK<br>(CPOL = 0)<br>(INPUT)<br>5 5 12 13<br>SPSCK<br>(CPOL = 1)<br>(INPUT)<br>10 11 9<br>MISO<br>SLAVE MSB OUT BIT 6 ... 1 SLAVE LSB OUT<br>(OUTPUT)<br>8 6 7<br>MOSI<br>MSB IN BIT 6 ... 1 LSB IN<br>(INPUT)<br>Figure 38. LPSPI Slave Mode Timing (CPHA=1)<br><!-- End of picture text -->

###### 12.1.2 LPSPI0 20 MHz and 15 MHz Combinations 

Table 41. LPSPI0 20 MHz and 15 MHz Combinations 

|PORT|S32K344 PAD TYPE|SPI Signal|20Mbps (In loopback<br>mode only)|15 Mbps|
|---|---|---|---|---|
|PTB1|GPIO-Standard-plus|LPSPI0_SOUT||LPSPI0_SOUT|
|PTB0|GPIO-Standard-plus|LPSPI0_PCS0||LPSPI0_PCS0|
|PTC9|GPIO-Standard-plus|LPSPI0_SIN||LPSPI0_SIN|
|PTC8|GPIO-Standard-plus|LPSPI0_SCK||LPSPI0_SCK|
|PTD6|GPIO-Medium|LPSPI0_PCS0|LPSPI0_PCS0||
|PTD5|GPIO-Medium|LPSPI0_PCS1|LPSPI0_PCS1||
|PTD12|GPIO-FAST|LPSPI0_SOUT|LPSPI0_SOUT||
|PTD11|GPIO-FAST|LPSPI0_SCK|LPSPI0_SCK||
|PTD10|GPIO-FAST|LPSPI0_SIN|LPSPI0_SIN||



S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

91 / 130 

NXP Semiconductors 

Communication interfaces 

###### ~~<mark>NOTE</mark>~~ 

Trace length should not exceed 11 inches for SCK pad when used in Master loopback mode. 

##### 12.2 I<sup>2</sup> C 

See I/O parameters for I<sup>2</sup> C specification. 

"For supported baud rate see section 'Chip-specific LPI2C information' of the Reference Manual." 

##### 12.3 I3C Push-Pull Timing Parameters for SDR Mode 

I3C interface is not supported on GPIO-Standard-plus pad type for 5 V operation. Measurements are with maximum output load of 30 pf, input transition of 1 ns. GPIO-Standard-plus pad configured with DSE = 1’b1 and GPIO-Medium pad with DSE = 1’b1 and SRE = 1’b1. SCL, SDA and PUR combination should be of same pad type. For e.g. I3C medium Data Pads to be used with I3C Medium Clock and PUR Pads Only. I3C Standard plus Data Pads to be used with I3C standard plus Clock and PUR pads only. 

Table 42. I3C Push-Pull Timing Parameters for SDR Mode 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|fSCL|SCL Clock<br>Frequency|0.01|12.5|12.9|MHz|FSCL = 1 / (tDIG_L +<br>tDIG_H)|—|
|tDIG_L|SCL Clock Low<br>Period<sup>1, 2</sup>|32|—|—|ns|—|—|
|tDIG_H|SCL Clock High<br>Period<sup>1</sup>|32|—|—|ns|—|—|
|tSCO|Clock in to Data Out<br>for Slave<sup>3, 4</sup>|—|—|12|ns|—|—|
|tCR|SCL Clock Rise<br>Time<sup>5</sup>|—|—|150e06 *<br>1 / fSCL<br>(capped<br>at 60)|ns|—|—|
|tCF|SCL Clock Fall<br>Time<sup>5</sup>|—|—|150e06 *<br>1 / fSCL<br>(capped<br>at 60)|ns|—|—|
|tHD_PP|SDA Signal Data<br>Hold in Push-Pull<br>Mode, Slave<sup>6</sup>|0|—|—|—|Applicable for slave<br>and master loopback<br>modes|—|
|tSU_PP|SDA Signal Data<br>Setup in Push-Pull<br>Mode|3|—|N/A|ns|Applicable for slave<br>and master loopback<br>modes.|—|



1. tDIG_L and tDIG_H are the clock Low and High periods as seen at the receiver end of the I3C Bus using VIL and VIH (see Figure 30) 

2. As both edges are used, the hold time needs to be satisfied for the respective edges; i.e., tCF + 3 for falling edge clocks, and tCR + 3 for rising edge clocks. 

3. Pad delay based on 90 Ω / 4 mA driver and 50 pF load. Note that Master may be a Slave in a multi-Master system, and thus shall also adhere to this requirement 

4. Devices with more than 12ns of tSCO delay shall set the limitation bit in the BCR, and shall support the GETMXDS CCC to allow the Master to read this value and adjust computations accordingly. For purposes of system design and test conformance, this parameter should be considered together with pad delay, bus capacitance, propagation delay, and clock triggering points. 

S32K3xx Data Sheet, Rev. 4, 04/2022 Preliminary Information 

Data Sheet: Technical Data 

92 / 130 

NXP Semiconductors 

Communication interfaces 

5. The clock maximum rise/fall time is capped at 60 ns. For lower frequency rise and fall the maximum value is limited at 60 ns, and is not dependent upon the clock frequency. 

6. tHD_PP is a Hold time parameter for Push-Pull Mode that has a different value for Master mode vs. Slave mode. In SDR Mode the Hold time parameter is referred to as tHD_SDR. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0093-04.png)


<!-- Start of picture text -->
Sr Sr P<br>tfDA trDA tHD_DAT<br>0.7 x VDD<br>SDA<br>0.3 x VDD<br>tSU_STA<br>tHD_STA tSU_DAT tSU_STO<br>tfCL trCL<br>0.7 x VDD<br>SCL<br>0.3 x VDD<br>tHIGH tLOW tLOW tHIGH<br>= Open Drain With Weak Pullup = High Speed Active Push-Pull Drive<br><!-- End of picture text -->

Figure 39. Legacy mode timing 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0093-06.png)


<!-- Start of picture text -->
tHIGH tCF tLOW<br>0.7 x VDD<br>0.3 x VDD<br>tCR tDIG_H tDIG_L<br><!-- End of picture text -->

Figure 40. tDIG_H and tDIG_L 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0093-08.png)


<!-- Start of picture text -->
0.7 x VDD<br>SDA<br>0.3 x VDD<br>tHD_PP tSU_PP<br>0.7 x VDD<br>SCL<br>0.3 x VDD<br>tCF tCR<br><!-- End of picture text -->

Figure 41. Master out timing 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

93 / 130 

NXP Semiconductors 

Communication interfaces 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0094-02.png)


<!-- Start of picture text -->
0.7 x VDD<br>SDA<br>0.3 x VDD<br>tSCO tSU_PP<br>0.7 x VDD<br>SCL<br>0.3 x VDD<br>tCF tCR<br><!-- End of picture text -->

Figure 42. Slave out timing 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0094-04.png)


<!-- Start of picture text -->
0.7 x VDD<br>SDA<br>0.3 x VDD<br>0.7 x VDD<br>SCL<br>0.3 x VDD<br>tSU_PP tHD_SDR<br><!-- End of picture text -->

Figure 43. Master SDR timing 

##### 12.4 FlexCAN characteristics 

See I/O parameters for FlexCAN specification. 

"For supported baud rate, see section 'Protocol timing' of the Reference Manual." 

##### 12.5 SAI electrical specifications 

###### 12.5.1 SAI Electrical Characteristics, Slave Mode 

The following table describes the SAI electrical characteristics. Measurements are with maximum output load of 30pF, input transition of 1ns and pad configured with DSE = 1'b1 and SRE = 1'b0. I/O operating voltage ranges from 2.97 V to 3.63 V. 

Table 43. SAI Electrical Characteristics, Slave Mode 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|S13|SAI_BCLK cycle<br>time (input)|80|—|—|ns|—|—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 Preliminary Information 

Data Sheet: Technical Data 

94 / 130 

NXP Semiconductors 

Communication interfaces 

Table 43. SAI Electrical Characteristics, Slave Mode (continued) 

|Symbol|Description|Min|Typ|Max|Unit||Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|---|
|S14|SAI_BCLK pulse<br>width high/low<br>(input)<sup>1</sup>|45|—|55|%|—||—|
|S15|SAI_RXD input<br>setup before<br>SAI_BCLK|8|—|—|ns|—||—|
|S16|SAI_RXD input hold<br>after SAI_BCLK|2|—|—|ns|—||—|
|S17|SAI_BCLK to<br>SAI_TXD output<br>valid|—|—|28|ns|—||—|
|S18|SAI_BCLK to<br>SAI_TXD output<br>invalid|0|—|—|ns|—||—|
|S19|SAI_FS input setup<br>before SAI_BCLK|8|—|—|ns|—||—|
|S20|SAI_FS input hold<br>after SAI_BCLK|2|—|—|ns|—||—|
|S21|SAI_BCLK to<br>SAI_FS output valid|—|—|28|ns|—||—|
|S22|SAI_BCLK to<br>SAI_FS output<br>invalid|0|—|—|ns|—||—|



1. The slave mode parameters (S15 - S22) assume 50% duty cycle on SAI_BCLK input. Any change in SAI_BCLK duty cycle input must be taken care during the board design or by the master timing. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0095-05.png)


Figure 44. SAI slave mode 

S32K3xx Data Sheet, Rev. 4, 04/2022 Preliminary Information 

Data Sheet: Technical Data 

95 / 130 

NXP Semiconductors 

Communication interfaces 

###### 12.5.2 SAI Electrical Characteristics, Master Mode 

The following table describes the SAI electrical characteristics. Measurements are with maximum output load of 30pF, input transition of 1ns and pad configured with DSE = 1'b1 and SRE = 1'b 0. I/O operating voltage ranges from 2.97 V to 3.63 V. 

Table 44. SAI Electrical Characteristics, Master Mode 

|Symbol|Description|Min|Typ|Max|Unit||Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|---|
|S1|SAI_MCLK cycle<br>time|40|—|—|ns|—||—|
|S2|SAI_MCLK pulse<br>width high/low|45|—|55|%|—||—|
|S3|SAI_BCLK cycle<br>time|80|—|—|ns|—||—|
|S4|SAI_BCLK pulse<br>width high/low|45|—|55|%|—||—|
|S5|SAI_RXD input<br>setup before<br>SAI_BCLK|28|—|—|ns|—||—|
|S6|SAI_RXD input hold<br>after SAI_BCLK|0|—|—|ns|—||—|
|S7|SAI_BCLK to<br>SAI_TXD output<br>valid|—|—|8|ns|—||—|
|S8|SAI_BCLK to<br>SAI_TXD output<br>invalid|-2|—|—|ns|—||—|
|S9|SAI_FS input setup<br>before SAI_BCLK|28|—|—|ns|—||—|
|S10|SAI_FS input hold<br>after SAI_BCLK|0|—|—|ns|—||—|
|S11|SAI_BCLK to<br>SAI_FS output valid|—|—|8|ns|—||—|
|S12|SAI_BCLK to<br>SAI_FS output<br>invalid|-2|—|—|ns|—||—|



S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

96 / 130 

NXP Semiconductors 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0097-01.png)


<!-- Start of picture text -->
Communication interfaces<br><!-- End of picture text -->


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0097-02.png)


Figure 45. SAI master mode 

##### 12.6 Ethernet characteristics 

###### 12.6.1 Ethernet MII (100 Mbps) 

The following timing specs are defined at the device I/O pin and must be translated appropriately to arrive at timing specs/ constraints for the physical interface. Measurements are with maximum output load of 25pF, input transition of 1ns and pad configured with DSE = 1'b1 and SRE = 1'b0. I/O operating voltage ranges from 2.97 V to 3.63 V. 

Table 45. Ethernet MII (100 Mbps) 

|Symbol|Description|Min|Typ|Max|Unit||Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|---|
|—|RXCLK frequency|—|—|25|MHz|—||—|
|MII1|RXCLK pulse width<br>high|35|—|65|%RXCLK<br>period|—||—|
|MII2|RXCLK pulse width<br>low|35|—|65|%RXCLK<br>period|—||—|
|MII3|RXD[3:0], RXDV,<br>RXER to RXCLK<br>setup|5|—|—|ns|—||—|
|MII4|RXCLK to RXD[3:0],<br>RXDV, RXER hold|5|—|—|ns|—||—|
|tCYC_TX|TXCLK frequency|—|25|—|MHz|—||—|
|MII5|TXCLK pulse width<br>high|35|—|65|%TXCLK<br>period|—||—|
|MII6|TXCLK pulse<br>width low|35|—|65|%TXCLK<br>period|—||—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 Preliminary Information 

Data Sheet: Technical Data 

97 / 130 

NXP Semiconductors 

Communication interfaces 

Table 45. Ethernet MII (100 Mbps) (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|MII7|TXCLK to TXD[3:0],<br>TXEN, TXER invalid|2|—|—|ns|—|—|
|MII8|TXCLK to TXD[3:0],<br>TXEN, TXER valid|—|—|25|ns|—|—|




![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0098-04.png)


Figure 46. MII receive diagram 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

98 / 130 

NXP Semiconductors 

Communication interfaces 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0099-02.png)


Figure 47. MII transmit diagram 

###### 12.6.2 Ethernet MII (200 Mbps) 

The following timing specs are defined at the device I/O pin and must be translated appropriately to arrive at timing specs/ constraints for the physical interface. Measurements are with maximum output load of 25pF, input transition of 1ns and pad configured with DSE = 1'b1 and SRE = 1'b0. I/O operating voltage ranges from 2.97 V to 3.63 V. 

Table 46. Ethernet MII (200 Mbps) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|—|RXCLK frequency|—|—|50|MHz|—|—|
|MII1|RXCLK pulse width<br>high|35|—|65|%<br>RXCLK<br>period|—|—|
|MII2|RXCLK pulse width<br>low|35|—|65|%<br>RXCLK<br>period|—|—|
|MII3|RXD[3:0], RXDV,<br>RXER to RXCLK<br>setup time|4|—|—|ns|—|—|
|MII4|RXCLK to RXD[3:0],<br>RXDV, RXER hold<br>time|2|—|—|ns|—|—|
|—|TXCLK frequency|—|—|50|MHz|—|—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

99 / 130 

NXP Semiconductors 

Communication interfaces 

Table 46. Ethernet MII (200 Mbps) (continued) 

|Symbol|Description|Min|Typ|Max|Unit||Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|---|
|MII5|TXCLK pulse width<br>high|35|—|65|%<br>TXCLK<br>period|—||—|
|MII6|TXCLK pulse width<br>low|35|—|65|%<br>TXCLK<br>period|—||—|
|MII7|TXCLK to TXD[3:0],<br>TXDV, TXER invalid|2|—|—|ns|—||—|
|MII8|TXCLK to TXD[3:0],<br>TXDV, TXER valid|—|—|15|ns|—||—|




![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0100-04.png)


Figure 48. MII receive diagram 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

100 / 130 

NXP Semiconductors 

Communication interfaces 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0101-02.png)


Figure 49. MII transmit diagram 

###### 12.6.3 Ethernet RMII 

The following timing specs are defined at the device I/O pin and must be translated appropriately to arrive at timing specs/ constraints for the physical interface. Measurements are with maximum output load of 25pF, input transition of 1ns and pad configured with DSE = 1'b1 and SRE = 1'b0. I/O operating voltage ranges from 2.97 V to 3.63 V. 

Table 47. Ethernet RMII 

|Symbol|Description|Min|Typ|Max|Unit||Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|---|
|—|RMII input<br>clock frequency<br>(RMII_CLK)|—|—|50|MHz|—||—|
|RMII1,RMII5|RMII_CLK pulse<br>width high|35|—|65|%RMII_C<br>LK period|—||—|
|RMII2,RMII6|RMII_CLK pulse<br>width low|35|—|65|%RMII_C<br>LK period|—||—|
|RMII3|RXD[1:0], CRS_DV,<br>RXER to RMII_CLK<br>setup|4|—|—|ns|—||—|
|RMII4|RMII_CLK to<br>RXD[1:0], CRS_DV,<br>RXER hold|2|—|—|ns|—||—|
|RMII8|RMII_CLK to<br>TXD[1:0], TXEN<br>data valid|—|—|15|ns|—||—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

101 / 130 

NXP Semiconductors 

Communication interfaces 

Table 47. Ethernet RMII (continued) 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0102-03.png)


<!-- Start of picture text -->
Symbol Description Min Typ Max Unit Condition Spec<br>Number<br>RMII7 RMII_CLK to  2 — — ns — —<br>TXD[1:0], TXEN<br>data invalid<br><!-- End of picture text -->


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0102-04.png)


Figure 50. RMII receive diagram 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

102 / 130 

NXP Semiconductors 

###### Communication interfaces 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0103-02.png)


Figure 51. RMII transmit diagram 

###### 12.6.4 Ethernet RGMII 

Table 48. Ethernet RGMII 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|Tcyc|Clock cycle<br>duration<sup>1, 2</sup>|7.2|—|8.8|ns|SRC = 0|—|
|TskewT|Data to clock<br>output skew (at<br>transmitter)<sup>2</sup>|-500|—|500|ps|SRC=0|—|
|TskewRi|Data to clock input<br>skew (at receiver)<sup>2</sup>|1|—|2.6|ns|SRC=0|—|
|TskewRo|Data to clock output<br>skew (at receiver)<sup>2</sup>|-650|—|650|ps|SRC=0|—|
|Duty_G|Clock duty cycle for<br>Gigabit<sup>2</sup>|45|—|55|%|SRC=0|—|
|Duty_T|Clock duty cycle for<br>10/100T<sup>2</sup>|40|—|60|%|SRC=0|—|
|Tr|Output rise time<sup>3</sup>|—|—|1|ns|SRC=0|—|
|Tf|Output fall time<sup>3</sup>|—|—|1|ns|SRC=0|—|



> 1. For 10 Mbps and 100 Mbps, Tcyc will scale to 400 ns ±40 ns and 40 ns ±4 ns respectively. 

2. RGMII timing specifications is valid for 3.3V nominal I/O pad supply voltage. 

> 3. Output timing valid for maximum external load CL = 13.5pF, which is assumed to be a 5pF load at the end of a 50ohm,  un­ terminated, 2.5 inch microstrip trace on standard FR4 (1.5pF/inch). For best signal integrity, the series resistance of the  transmission line should be matched closely to the selected RDSON of the I/O pad output driver.” 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

103 / 130 

NXP Semiconductors 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0104-01.png)


<!-- Start of picture text -->
Communication interfaces<br>RXC (at transmitter)<br>TskewT<br>RXD[8:5][3:0] RXD[8:5]<br>RXD[3:0]<br>RXD[7:4][3:0] RXD[7:4]<br>RXD[4] RXD[9]<br>RX_CTL<br>RXDV RXERR<br>TskewR<br>RXC (at receiver)<br>Figure 52. RGMII Receive Timing<br>TXC (at transmitter)<br>TskewT<br>TXD[8:5][3:0] TXD[8:5]<br>TXD[3:0]<br>TXD[7:4][3:0] TXD[7:4]<br>TXD[4] TXD[9]<br>TX_CTL<br>TXEN TXERR<br>TskewR<br>TXC (at receiver)<br>Figure 53. RGMII Transmit Timing<br><!-- End of picture text -->

###### 12.6.5 MDIO timing specifications 

The following table describes the MDIO electrical characteristics. Measurements are with maximum output load of 25 pF, input transition of 1 ns and pad configured with fastest slew settings (DSE = 1'b1 and SRE = 1’b0). I/O operating voltage ranges from 2.97 V to 3.63 V. MDIO pin must have external Pull-up. 

Table 49. MDIO timing specifications 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|—|MDC clock<br>frequency|—|—|2.5|MHz|—|—|
|MDC1|MDC pulse width<br>high|40|—|60|%MDC<br>period|—|MDC1|
|MDC2|MDC pulse width low|40|—|60|%MDC<br>period|—|MDC2|
|MDC5|MDC falling edge<br>to MDIO output<br>valid(maximum<br>propagation delay)|—|—|25|ns|—|MDC5|
|MDC6|MDC falling edge<br>to MDIO output<br>invalid(minimum<br>propagation delay)|-10|—|—|ns|—|MDC6|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

104 / 130 

NXP Semiconductors 

Communication interfaces 

Table 49. MDIO timing specifications (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|MDC3|MDIO (input) to<br>MDC rising edge<br>setup time|25|—|—|ns|—|MDC3|
|MDC4|MDIO (input) to<br>MDC rising edge<br>hold time|0|—|—|ns|—|MDC4|




![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0105-04.png)


<!-- Start of picture text -->
MDC1 MDC2<br>MDC (output)<br>MDC6<br>MDIO (output)<br>MDC5<br>MDIO (input)<br>MDC3 MDC4<br><!-- End of picture text -->

Figure 54. MII/RMII serial management channel timing 

##### 12.7 QuadSPI 

###### 12.7.1 QuadSPI Quad 3.3V SDR 120MHz 

The following table describes the QuadSPI electrical characteristics. Measurements are with maximum output load of 25pF, input transition of 1ns and pads configured with DSE = 1'b1 and SRE = 1'b0. I/O operating voltage ranges from 2.97V to 3.63V. QuadSPI trace length should be less than or equal to 2 inches. For Single and Dual IO modes of operation if external device doesn’t have pull-up feature, then external pull-up must be added at board level for unused device pins. With external pull-up, performance of the interface may degrade in Quad IO mode based on load associated with external pull-up. QuadSPI support delay chain upto length 16, wherein delay length of low-frequency segment is 16 and length of high-frequency segment is 0. See the device Reference Manual for register and bit descriptions. 

Program register value QuadSPI_FLSHCR[TCSS] = 4`h3. 

Program register value QuadSPI_FLSHCR[TCSH] = 4`h3. 

Program register value QuadSPI_DLLCRA[SLV_FINE_OFFSET] to 4'b0001. 

Table 50. QuadSPI Quad 3.3V SDR 120MHz 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|fSCK|SCK clock<br>frequency<sup>1</sup>|—|—|120|MHz|Pad Loopback|—|
|fSCK|SCK clock<br>frequency<sup>1</sup>|—|—|60|MHz|Internal Loopback|—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 Preliminary Information 

Data Sheet: Technical Data 

105 / 130 

NXP Semiconductors 

Communication interfaces 

Table 50. QuadSPI Quad 3.3V SDR 120MHz (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|tSCK|SCK clock period|1/fSCK|—|—|ns|Pad Loopback|—|
|tSCK|SCK clock period|1/fSCK|—|—|ns|Internal Loopback|—|
|tSDC|SCK duty cycle<sup>2</sup>|45|—|55|%|Internal Loopback|—|
|tSDC|SCK duty cycle<sup>2</sup>|45|—|55|%|Pad Loopback|—|
|tIS|Data input setup<br>time|1.75|—|—|ns|Pad Loopback|—|
|tIS|Data input setup<br>time|9|—|—|ns|Internal Loopback|—|
|tIH|Data input hold time|1|—|—|ns|Pad Loopback|—|
|tIH|Data input hold time|1|—|—|ns|Internal Loopback|—|
|tOV|Data output valid<br>time|—|—|1.75|ns|Pad Loopback|—|
|tOV|Data output valid<br>time|—|—|1.75|ns|Internal Loopback|—|
|tIV|Data output invalid<br>time|-1.5|—|—|ns|Pad Loopback|—|
|tIV|Data output invalid<br>time|-1.5|—|—|ns|Internal Loopback|—|
|tCSSCK|CS to SCK time|5|—|—|ns|Pad Loopback|—|
|tCSSCK|CS to SCK time|5|—|—|ns|Internal Loopback|—|
|tSCKCS|SCK to CS time|3|—|—|ns|Pad Loopback|—|
|tSCKCS|SCK to CS time|3|—|—|ns|Internal Loopback|—|



> 1. This frequency specification is valid only if output valid time of external flash is ≤ 5.5ns, and if output valid time of external flash is more than 5.5ns but ≤ 6.5ns, then maximum fSCK is 104MHz. 

> 2. For S32K342 100MQFP, tSDC spec would be 44%-56% when ENET and SAI active along with QuadSPI at 120MHZ 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

106 / 130 

NXP Semiconductors 

Communication interfaces 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0107-02.png)


Figure 55. QuadSPI input timing (SDR mode) 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0107-04.png)


Figure 56. QuadSPI output timing (SDR mode) 

###### 12.7.2 QuadSPI Octal 3.3V DDR 100MHz 

The following table describes the QuadSPI electrical characteristics. Measurements are with maximum output load of 25pF, input transition of 1ns and pads configured with DSE = 1'b1 and SRE = 1'b0. I/O operating voltage ranges from 2.97V to 3.63V. QuadSPI trace length should be less than or equal to 2 inches. For Single and Dual IO modes of operation if external device doesn’t have pull-up feature, then external pull-up must be added at board level for unused device pins. With external pull-up, performance of the interface may degrade in Quad IO mode based on load associated with external pull-up. QuadSPI support delay chain upto length 16, wherein delay length of low-frequency segment is 16 and length of high-frequency segment is 0. See the device Reference Manual for register and bit descriptions. 

Set FLSHCR[TCSS]=2 and FLSHCR[TCSH]=5. 

Table 51. QuadSPI Octal 3.3V DDR 100MHz 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|fSCK_DQS|SCK / DQS<br>frequency<sup>1</sup>|—|—|100|MHz|—|—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 Preliminary Information 

Data Sheet: Technical Data 

107 / 130 

NXP Semiconductors 

Communication interfaces 

Table 51. QuadSPI Octal 3.3V DDR 100MHz (continued) 

|Symbol|Description|Min|Typ|Max|Unit||Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|---|
|tSDC|SCK duty cycle|45|—|55|%|—||—|
|tCL_SCK_DQS|SCK / DQS low<br>time<sup>1</sup>|4.500|—|—|ns|—||—|
|tCH_SCK_DQS|SCK / DQS high<br>time<sup>1</sup>|4.500|—|—|ns|—||—|
|tOD_DATA|Data output delay<br>(w.r.t. SCK)|1.016|—|3.484|ns|—||—|
|tOD_CS|CS output delay<br>(w.r.t. SCK)<sup>2</sup>|3.016 - n/<br>fSCK|—|-0.016 +<br>m/fSCK|ns|—||—|
|tDVW|Input data valid<br>window<sup>1</sup>|3.284|—|—|ns|—||—|
|tISU_DQS|Input setup time<br>(w.r.t. DQS)<sup>1</sup>|-0.816|—|—|ns|—||—|
|tIH_DQS|Input hold time (w.r.t.<br>DQS)<sup>1</sup>|<br>3.684|—|—|ns|—||—|



1. Input timing assumes maximum input signal transition of 1 ns (20%/80%).  DQS denotes external strobe provided by the Flash. 

2. Where m=TCSS and n=TCSH-1. 

###### 12.7.3 QuadSPI Octal 3.3V DDR 120MHz 

The following table describes the QuadSPI electrical characteristics. Measurements are with maximum output load of 25pF, input transition of 1ns and pads configured with DSE = 1'b1 and SRE = 1'b0. I/O operating voltage ranges from 2.97V to 3.63V. QuadSPI trace length should be less than or equal to 2 inches. For Single and Dual IO modes of operation if external device doesn’t have pull-up feature, then external pull-up must be added at board level for unused device pins. With external pull-up, performance of the interface may degrade in Quad IO mode based on load associated with external pull-up. QuadSPI support delay chain upto length 16, wherein delay length of low-frequency segment is 16 and length of high-frequency segment is 0. See the device Reference Manual for register and bit descriptions. 

Set FLSHCR[TCSS]=2 and FLSHCR[TCSH]=5. 

Table 52. QuadSPI Octal 3.3V DDR 120MHz 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|fSCK_DQS|SCK / DQS<br>frequency<sup>1</sup>|—|—|120|MHz|DLL and Auto-Learning<br>mode enabled|—|
|fSCK_DQS|SCK / DQS<br>frequency<sup>1</sup>|—|—|120|MHz|DLL mode enabled|—|
|tSCK|SCK clock period|1/<br>fSCK_D<br>QS|—|—|ns|External DQS|—|
|tSDC|SCK / DQS duty<br>cycle|45|—|55|%|External DQS|—|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

108 / 130 

NXP Semiconductors 

Communication interfaces 

Table 52. QuadSPI Octal 3.3V DDR 120MHz (continued) 

|Symbol|Description|Min|Typ|Max|Unit||Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|---|
|tCL_SCK_DQS|SCK / DQS low<br>time<sup>1</sup>|3.75|—|—|ns|—||—|
|tCH_SCK_DQS|SCK / DQS high<br>time<sup>1</sup>|3.75|—|—|ns|—||—|
|tOD_DATA|Data output delay<br>(w.r.t. SCK)|0.816|—|2.934|ns|—||—|
|tOD_CS|CS output delay<br>(w.r.t. SCK)|3.016|—|-0.766|ns|—||—|
|tDVW|Input data valid<br>window<sup>1</sup>|2.518|—|—|ns|—||—|
|tISU_DQS|Input setup time<br>(w.r.t. DQS)<sup>1</sup>|-0.616|—|—|ns|—||—|
|tIH_DQS|Input hold time (w.r.t.<br>DQS)<sup>1</sup>|<br>3.134|—|—|ns|—||—|



1. Input timing assumes an input signal transition of 1 ns (20%/80%).  DQS denotes external strobe provided by the Flash. 

##### 12.8 uSDHC 

###### 12.8.1 uSDHC SDR electrical specifications 

The following table describes the uSDHC electrical characteristics. Measurements are with maximum output load of 25pF, input transition of 1ns and pad configured with DSE = 1'b1 and SRE = 1'b0. I/O operating voltage ranges from 2.97 V to 3.63 V. 

Table 53. uSDHC SDR electrical specifications 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|fpp|Clock frequency (low<br>speed)<sup>1, 2</sup>|—|—|400|kHz|—|SD1|
|fpp|Clock frequency<sup>2, 3</sup>|—|—|50|MHz|Medium pad|SD1|
|fpp|Clock frequency<sup>2, 4</sup>|—|—|25|MHz|Standard pad|SD1|
|fOD|Clock frequency<br>(identification<br>mode)<sup>2</sup>|100|—|400|kHz|—|SD1|
|tWL|Clock low time|6|—|—|ns|Medium pad|SD2|
|tWL|Clock low time|12|—|—|ns|Standard pad|SD2|
|tWH|Clock high time|6|—|—|ns|Medium pad|SD3|
|tWH|Clock high time|12|—|—|ns|Standard pad|SD3|
|tTLH|Clock rise time<sup>2, 5</sup>|—|—|4|ns|Medium pad|SD4|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 Preliminary Information 

Data Sheet: Technical Data 

109 / 130 

NXP Semiconductors 

Communication interfaces 

Table 53. uSDHC SDR electrical specifications (continued) 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|tTLH|Clock rise time<sup>2, 5</sup>|—|—|8|ns|Standard pad|SD4|
|tTHL|Clock fall time<sup>2, 5</sup>|—|—|4|ns|Medium pad|SD5|
|tTHL|Clock fall time<sup>2, 5</sup>|—|—|8|ns|Standard pad|SD5|
|tOD|SDHC output delay<br>(output valid)<sup>2</sup>|-5.6|—|2.6|ns|SDHC_CLK to SDHC_<br>CMD / SDHC_DAT|SD6|
|tISU|SDHC Input setup<br>time<sup>6</sup>|4.8|—|—|ns|SDHC_CMD / SDHC_<br>DAT to SDHC_CLK|SD7|
|tIH|SDHC Input hold<br>time<sup>6</sup>|1.5|—|—|ns|SDHC_CLK to SDHC_<br>CMD / SDHC_DAT|SD8|



1. In low speed mode, card clock must be lower than 400 kHz, voltage ranges from 2.7V to 3.6V. 

2. Output timing valid for maximum external load CL = 25pF, which is assumed to be a 10pF load at the end of a 50Ohm, un-terminated, 3.5 inch microstrip trace on standard FR4 (1.5pF/inch), (25pF total with margin). 

3. In normal (full) speed mode for SD/SDIO card, clock frequency can be any value between 0–25 MHz. In high-speed mode, clock frequency can be any value between 0–50 MHz. 

4. In normal (full) speed mode for MMC card, clock frequency can be any value between 0–25 MHz. In high-speed mode, clock frequency can be any value between 0–50 MHz. 

5. The SDHC_CLK rise/fall time specification applies to the input clock transition required in order to meet the output delay specifications. SDHC_CLK output transition time is dependent on output load and GPIO pad drive strength. See the GPIO pad specifications for detail. 

6. Input timing assumes an input signal slew rate of 3ns (20%/80%). 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0110-10.png)


<!-- Start of picture text -->
SD4<br>SD2<br>SD5 SD1<br>SDx_CLK<br>SD3<br>SD6<br>Output from uSDHC to card<br>SDx_DATA[7:0]<br>SD7 SD8<br>Input from card to uSDHC<br>SDx_DATA[7:0]<br><!-- End of picture text -->

Figure 57. SD/eMMC4.3 High Speed Mode Interface Timing 

###### 12.8.2 uSDHC DDR electrical specifications 

The following table describes the uSDHC electrical characteristics. Measurements are with maximum output load of 25pF, input transition of 1ns and pad configured with DSE = 1'b1 and SRE = 1'b0. I/O operating voltage ranges from 2.97 V to 3.63 V. 

S32K3xx Data Sheet, Rev. 4, 04/2022 Preliminary Information 

Data Sheet: Technical Data 

110 / 130 

NXP Semiconductors 

Communication interfaces 

Table 54. uSDHC DDR electrical specifications 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|fpp|Clock frequency<br>(eMMC4.4/4.41<br>DDR)<sup>1</sup>|—|—|50|MHz|Medium pad|SD1|
|fpp|Clock frequency<br>(eMMC4.4/4.41<br>DDR)<sup>1</sup>|—|—|25|MHz|Standard pad|SD1|
|fpp|Clock frequency<br>(SD3.0 DDR)<sup>1</sup>|—|—|50|MHz|Medium pad|SD1|
|fpp|Clock frequency<br>(SD3.0 DDR)<sup>1</sup>|—|—|25|MHz|Standard pad|SD1|
|tWL|Clock low time|6|—|—|ns|Medium pad|—|
|tWL|Clock low time|12|—|—|ns|Standard pad|—|
|tWH|Clock high time|6|—|—|ns|Medium pad|—|
|tWH|Clock high time|12|—|—|ns|Standard pad|—|
|tTLH|Clock rise time<sup>1, 2</sup>|—|—|4|ns|Medium pad|—|
|tTLH|Clock rise time<sup>1, 2</sup>|—|—|8|ns|Standard pad|—|
|tTHL|Clock fall time<sup>1, 2</sup>|—|—|4|ns|Medium pad|—|
|tTHL|Clock fall time<sup>1, 2</sup>|—|—|8|ns|Standard pad|—|
|tOD|SDHC output delay<br>(output valid)<sup>1</sup>|2.7|—|5.6|ns|SDHC_CLK to SDHC_<br>DAT|SD2|
|tOD|SDHC output delay<br>(output valid)<sup>1</sup>|-5.6|—|2.6|ns|SDHC_CLK to SDHC_<br>CMD|SD6<br>(See<br>SDR<br>figure)|
|tISU|SDHC Input setup<br>time<sup>3</sup>|1.6|—|—|ns|SDHC_DAT to SDHC_<br>CLK|SD3|
|tISU|SDHC Input setup<br>time<sup>3</sup>|4.8|—|—|ns|SDHC_CMD to SDHC_<br>CLK|SD7<br>(See<br>SDR<br>figure)|
|tIH|SDHC Input hold<br>time<sup>3</sup>|1.5|—|—|ns|SDHC_CLK to SDHC_<br>DAT|SD4|
|tIH|SDHC Input hold<br>time<sup>3</sup>|1.5|—|—|ns|SDHC_CLK to SDHC_<br>CMD|SD8<br>(See<br>SDR<br>figure)|



> 1. Output timing valid for maximum external load CL = 25pF, which is assumed to be a 10pF load at the end of a 50Ohm, un-terminated, 3.5 inch microstrip trace on standard FR4 (1.5pF/inch), (25pF total with margin). 

> 2. The SDHC_CLK rise/fall time specification applies to the input clock transition required in order to meet the output delay specifications. SDHC_CLK output transition time is dependent on output load and GPIO pad drive strength. See the GPIO pad specifications for detail. 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

111 / 130 

NXP Semiconductors 

Debug modules 

3. Input timing assumes an input signal slew rate of 3ns (20%/80%). 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0112-03.png)


<!-- Start of picture text -->
SD1<br>SDx_CLK<br>SD2<br>SD2<br>Output from eSDHCv3 to card .......<br>SDx_DATA[7:0]<br>SD3<br>SD4<br>Input from card to eSDHCv3 .......<br>SDx_DATA[7:0]<br><!-- End of picture text -->

Figure 58. SD/eMMC4.4/4.41 DDR50 Mode Interface Timing 

##### 12.9 LPUART specifications 

See I/O parameters for LPUART specifications. 

#### 13 Debug modules 

##### 13.1 Debug trace timing specifications 

The following table describes the Debug trace electrical characteristics. Measurements are with maximum output load of 25pF, input transition of 1ns and pad configured with DSE = 1'b1 and SRE = 1'b0. 

Table 55. Debug trace timing specifications 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|fTRACE|Trace clock<br>frequency (trace on<br>Fast pads)|—|—|120|MHz|—|—|
|fTRACE|Trace clock<br>frequency (trace on<br>StandardPlus pads)|—|—|25|MHz|—|—|
|tDVW|Data output valid<br>window|1.2|—|—|ns|—|—|
|tDIV|Data output invalid|0.3|—|—|ns|—|—|



S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

112 / 130 

NXP Semiconductors 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0113-01.png)


<!-- Start of picture text -->
Debug modules<br><!-- End of picture text -->


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0113-02.png)


Figure 59. Trace CLKOUT specifications 

##### 13.2 SWD electrical specifications 

The following table describes the SWD electrical characteristics. Measurements are with maximum output load of 30pF, input transition of 1ns and pad configured with DSE = 1'b1 and SRE = 1'b0. 

Table 56. SWD electrical specifications 

|Symbol|Description|Min|Typ|Max|Unit|Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|
|S1|SWD_CLK<br>frequency|—|—|33|MHz|—|S1|
|S2|SWD_CLK cycle<br>period|1 / S1|—|—|ns|—|S2|
|S3|SWD_CLK pulse<br>width|40|—|60|%|—|S3|
|S4|SWD_CLK rise and<br>fall times|—|—|1|ns|—|S4|
|S9|SWD_DIO input<br>data setup time to<br>SWD_CLK rise|5|—|—|ns|—|S9|
|S10|SWD_DIO input<br>data hold time<br>after SWD_CLK<br>rising edge|5|—|—|ns|—|S10|
|S11|SWD_CLK high to<br>SWD_DIO output<br>data valid|—|—|22|ns|—|S11|
|S12|SWD_CLK high to<br>SWD_DIO output<br>data hi-Z|—|—|22|ns|—|S12|
|S13|SWD_CLK high to<br>SWD_DIO output<br>data invalid|0|—|—|ns|—|S13|



S32K3xx Data Sheet, Rev. 4, 04/2022 Preliminary Information 

Data Sheet: Technical Data 

113 / 130 

NXP Semiconductors 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0114-01.png)


<!-- Start of picture text -->
Debug modules<br>S2<br>S3 S3<br>SWD_CLK (input)<br>S4 S4<br>Figure 60. SWD Input Clock Timing<br>SWD_CLK<br>S9 S10<br>SWD_DIO Input data valid<br>S11<br>S13<br>SWD_DIO Output data valid<br>S12<br>SWD_DIO<br>Figure 61. SWD Output Data Timing<br><!-- End of picture text -->

##### 13.3 JTAG electrical specifications 

The following table describes the JTAG electrical characteristics. These specifications apply to JTAG and boundary scan. Measurements are with maximum output load of 30pF, input transition of 1ns and pad configured with DSE = 1'b1 and SRE = 1'b0. 

Table 57. JTAG electrical specifications 

|Symbol|Description|Min|Typ|Max|Unit||Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|---|
|tJCYC|TCK cycle time<sup>1, 2</sup>|30|—|—|ns|—||1|
|tJDC|TCK clock pulse<br>width|40|—|60|%|—||2|
|tTCKRISE|TCK rise/fall times<br>(40%-70%)|—|—|1|ns|—||3|
|tTMSS, tTDIS|TMS, TDI data setup<br>time|5|—|—|ns|—||4|
|tTMSH, tTDIH|TMS, TDI data hold<br>time|5|—|—|ns|—||5|
|tTDOV|TCK low to TDO<br>data valid<sup>3</sup>|—|—|22|ns|—||6|
|tTDOI|TCK low to TDO<br>data invalid|0|—|—|ns|—||7|



Table continues on the next page... 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

114 / 130 

NXP Semiconductors 

Debug modules 

Table 57. JTAG electrical specifications (continued) 

|Symbol|Description|Min|Typ|Max|Unit||Condition|Spec<br>Number|
|---|---|---|---|---|---|---|---|---|
|tTDOHZ|TCK low to TDO<br>high impedance|—|—|22|ns|—||8|
|tBSDV|TCK falling edge to<br>output valid<sup>4</sup>|—|—|600|ns|—||11|
|tBSDVZ|TCK falling edge to<br>output valid out of<br>high impedance|—|—|600|ns|—||12|
|tBSDHZ|TCK falling edge<br>to output high<br>impedance|—|—|600|ns|—||13|
|tBSDST|Boundary scan input<br>valid to TCK rising<br>edge|15|—|—|ns|—||14|
|tBSDHT|TCK rising edge to<br>boundary scan input<br>invalid|15|—|—|ns|—||15|



1. Cycle time is 30ns assuming full cycle timing. Cycle time is 60ns assuming half cycle timing. 

2. This timing applies to TDI, TDO, TMS pins, however, actual frequency is limited by pad type for EXTEST instructions. Refer to pad specification for allowed transition frequency 

3. Timing includes TCK pad delay, clock tree delay, logic delay and TDO output pad delay. 

4. Applies to all pins, limited by pad slew rate. Refer to IO delay and transition specification and add 20 ns for JTAG delay. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0115-08.png)


<!-- Start of picture text -->
TCK<br>2<br>3 2<br>1 3<br><!-- End of picture text -->

Figure 62. JTAG TCK Input Timing 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

115 / 130 

NXP Semiconductors 

Thermal Attributes 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0116-02.png)


<!-- Start of picture text -->
TCK<br>4<br>5<br>TMS, TDI<br>6<br>7 8<br>TDO<br><!-- End of picture text -->


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0116-03.png)


<!-- Start of picture text -->
Figure 63. JTAG Test Access Port Timing<br><!-- End of picture text -->


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0116-04.png)


<!-- Start of picture text -->
TCK<br>11 13<br>Output<br>signals<br>12<br>Output<br>signals<br>14<br>15<br>Input<br>signals<br>Figure 64. Boundary Scan Timing<br><!-- End of picture text -->

#### 14 Thermal Attributes 

##### 14.1 Description 

The tables in the following sections describe the thermal characteristics of the device. 

S32K3xx Data Sheet, Rev. 4, 04/2022 Preliminary Information 

Data Sheet: Technical Data 

116 / 130 

NXP Semiconductors 

Dimensions 

~~<mark>NOTE</mark>~~ 

Junction temperature is a function of die size, on-chip power dissipation, package thermal resistance, mounting side (board) temperature, ambient temperature, air flow, power dissipation or other components on the board, and board thermal resistance. 

##### 14.2 Thermal characteristics 

Thermal characteristics for the LQFP, MaxQFP & MAPBGA package in the S32K3 family. 

Table 58. Thermal characteristics 

|Rating|Conditions|Symbol|Package|Device|||||Unit|
|---|---|---|---|---|---|---|---|---|---|
|||||S32K311|S32K312|S32K342<br>S32K341<br>S32K322|S32K344<br>S32K314<br>S32K324|S32K358<br>S32K348<br>S32K328<br>S32K338||
|Thermal<br>|<br>Four-layer<br>|RϴJA|48-LQFP|TBD|NA|NA|NA|NA|°C/W|
|resistance,<br>Junction to<br>Ambient|<br> <br>board<br>(2s2p)||100-<br>MaxQFP|TBD|38|33.8|NA|NA|°C/W|
|(Natural<br>Convectio<br>|||172-<br>MaxQFP|NA|30.5|29.6|28.9|NA|°C/W|
|n)|||257-<br>MAPBGA|NA|NA|NA|26.8|NA|°C/W|
||||172<br>MAXQFP_<br>EP|NA|NA|NA|NA|15.6|°C/W|
||||289-<br>MAPBGA|NA|NA|NA|NA|19.6|°C/W|
|Thermal|Natural<br>|RϴJT|48-LQFP|TBD|NA|NA|NA|NA|°C/W|
|resistance,<br>Junction to<br>Package|<br> <br>Convectio<br>n||100-<br>MaxQFP|TBD|0.8|0.5|NA|NA|°C/W|
|<br>Top|||172-<br>MaxQFP|NA|0.5|0.5|0.4|NA|°C/W|
||||257-<br>MAPBGA|NA|NA|NA|0.3|NA|°C/W|
||||172<br>MAXQFP_<br>EP|NA|NA|NA|NA|TBD|°C/W|
||||289-<br>MAPBGA|NA|NA|NA|NA|TBD|°C/W|



#### 15 Dimensions 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

117 / 130 

NXP Semiconductors 

Revision history 

##### 15.1 Obtaining package dimensions 

Package dimensions are provided in the package drawings. To find a package drawing, go to nxp.com and perform a keyword search for the drawing’s document number: 

|Package option|Document Number|
|---|---|
|257-ball MAPBGA|98ASA01483D|
|172-pin MaxQFP|98ASA01107D|
|100-pin MaxQFP|98ASA01570D|
|172-pin MAXQFP_EP|98ASA01667D|
|289-ball MAPBGA|98ASA01216D|



#### 16 Revision history 

The following table lists the changes in this document. 

###### Rev 4, April 2022 

- Removed S32K312 from preliminary list from the title of the document and "Overview". 

- In features on first page added MAPBGA289 to the package list and updated GPIO pins upto 235. 

- Removed "NDA required" term from all block diagrams. 

- In "Ordering information", added MaxQFP-EP package suffix. 

- In section "Absolute maximum ratings", and "Voltage and current operating requirements", added S32K341 variant to the sentence "The VDD_HV_B and V15 voltage supply domains are only present....". 

- In section “Voltage and current operation requirement”, the footnote attached to supply ramp rate is updated as “ The MCU Supply ramp applicable to the MCU input/external supplies...". 

- Updated capacitor symbol to non-polarity in following figures at V25 and V11: 

   - Power management system - S32K344, S32K324, S32K341, S32K314, S32K342, and S32K322. 

   - Power management system - S32K312, S32K311 

- In "Power management system - S32K358" figure, updated connections to optional circuit with dashed lines for PGATE_CTRL and VSS_DCDC. 

- In section “SMPS regulator electrical specifications”, added a sentence “The chip hardware design guidelines documents lists the recommended part numbers of PMOS & Schottky diode." 

- In table "SMPS regulator electrical specifications" : 

   - The typ. value of "External coil inductance" changed from 5 to 4.7uH. 

   - Added “Schottky diode reverse voltage” with Min value 5.0 V. 

   - Added “Schottky diode forward current” with Min value 1.0 A. 

- In section "SMPS regulator electrical specifications" changed "COUT_V15" to "COUT_V15_SMPS" to match it with corresponding figure. 

- In section "Recommended Decoupling Capacitors" changed "COUT_V15" to "COUT_V15_NPN" to match it with corresponding figure. 

- In section "Recommended Decoupling Capacitors", following footnotes updated: 

S32K3xx Data Sheet, Rev. 4, 04/2022 Preliminary Information 

Data Sheet: Technical Data 

118 / 130 

NXP Semiconductors 

Revision history 

###### Rev 4, April 2022 

   - Footnote attached to CDEC "Optionally, 1 nF capacitors can be added...". 

   - Footnote attached to CBULK "For devices where the VDD_HV_B domain is present, if the VDD_HV_B...". 

   - Added footnote to CBULK "These capacitors must be placed close to the source." 

- In section "Recommended Decoupling Capacitors", updated and added decoupling capacitors diagrams. 

- In section "NPN Ballast Transistor Control Specification" added specification for VDD_HV_NPN. 

- Updated "Ballast circuit" figure under section " NPN Ballast Transistor Control Specification". 

- Current IDD specs are updated for S32K12 for following : 

   - Table “STANDBY mode supply currents” 

   - Table “Low speed RUN mode supply currents” 

   - Table “RUN mode supply currents (peripherals disabled)” 

   - Table “Example RUN mode configuration supply current” 

- In section “supply current”, Removed table “Recommended current limits in board design” and related sentence “The power supplies for the voltage ...." 

- In section “Power management”, added section ”Cyclic wake-up current” and removed table "Low-power, cyclic operation mode" from supply currents. 

- In section "GPIO DC electrical specifications, 3.3V Range (2.97V - 3.63V)",with symbol "ILKG_33_S", the condition has been changed from PTC0 to PTD0. 

- In section "5.0V (4.5V - 5.5V) GPIO Output AC Specification": 

   - for Symbol "TR_TF_50_F" with condition "DSE=0, SRE=1, Capacitance=50pF" Min changed from "2.8" to "1.9". 

   - — for Symbol "TR_TF_50_F" with condition "DSE=0, SRE=1, Capacitance=50pF" Max changed from "10.2" to "7.7". — for Symbol "TR_TF_50_F" with condition "DSE=1, SRE=1, Capacitance=50pF" Min changed from "1.9" to "1.3". — for Symbol "TR_TF_50_F" with condition "DSE=1, SRE=1, Capacitance=50pF" Max changed from "6.7" to "5.1". — for Symbol "TR_TF_50_F" with condition "DSE=0, SRE=0, Capacitance=50pF" Min changed from "2.0" to "1.0". — for Symbol "TR_TF_50_F" with condition "DSE=0, SRE=0, Capacitance=50pF" Max changed from "7.4" to "5.3". — for Symbol "TR_TF_50_F" with condition "DSE=1, SRE=0, Capacitance=25pF" Min changed from "0.9" to "0.3". — for Symbol "TR_TF_50_F" with condition "DSE=1, SRE=0, Capacitance=25pF" Max changed from "3.0" to "0.9". — for Symbol "TR_TF_50_F" with condition "DSE=1, SRE=1, Capacitance=25pF" Min changed from "1.3" to "0.9". — for Symbol "TR_TF_50_F" with condition "DSE=1, SRE=1, Capacitance=25pF" Max changed from "5.1" to "4.1". — for Symbol "TR_TF_50_F" with condition "DSE=1, SRE=0, Capacitance=50pF" Min changed from "1.6" to "0.9". — for Symbol "TR_TF_50_F" with condition "DSE=1, SRE=0, Capacitance=50pF" Max changed from "3.6" to "3.0". — for Symbol "TR_TF_50_F" with condition "DSE=0, SRE=0, Capacitance=25pF" Min changed from "1.0" to "0.4". — for Symbol "TR_TF_50_F" with condition "DSE=0, SRE=0, Capacitance=25pF" Max changed from "5.3" to "3.1". — for Symbol "TR_TF_50_F" with condition "DSE=0, SRE=1, Capacitance=25pF" Min changed from "1.9" to "1.5". 

   - for Symbol "TR_TF_50_F" with condition "DSE=0, SRE=1, Capacitance=25pF" Max changed from "7.7" to "6.1". 

- In section “SAR ADC“, the footnote attached to “ADC Total Unadjusted Error” is updated as “TUE spec for precision and standard channels is based on 12-bit level resolution”. 

S32K3xx Data Sheet, Rev. 4, 04/2022 Preliminary Information 

Data Sheet: Technical Data 

119 / 130 

NXP Semiconductors 

Revision history 

###### Rev 4, April 2022 

- In section "Supply Diagnosis", for Symbol "AN_ACC" and "AN_T_on" footnote added "These specs will have degraded performan..." 

- In section "Fast External Oscillator (FXOSC)", for Symbol "TFXOSC" description changed from "Fxosc start up time" to "Fxosc start up time (ALC enabled)". 

- In section "Fast External Oscillator (FXOSC)", removed the crystal part numbers and related information which includes following sentences, "In crystal mode NX5032GA crystal .....", " In crystal mode NX8045GB crystal …" and updated sentence "To ensure stable oscillations, FXOSC incorporates the feedback resistance internally.". 

- In section "LPSPI", updated the sentence updated maximum output load of 50pF to 30pF. 

- In section "LPSPI", footnote attached to "fperiph" is udated to mention clock name instead of frequency. "For LPSPI0 instance, max. peripheral...". 

- In section "I3C Push-Pull Timing Parameters for SDR Mode", Symbol "tV" and tHI are deleted. 

- Added section "Ethernet RGMII". 

- In all QuadSPI modes updated trace length from 3 inches to 2 inches. 

- Added "QuadSPI Octal 3.3V DDR 100MHz" mode. 

- Deleted "QuadSPI Quad 3.3V DDR 80MHz" mode. 

- In section "QuadSPI Octal 3.3V DDR 120MHz" : 

   - For symbol “tOD_DATA”, Max. value changed from “2.567” to “ 2.934”. 

   - For symbol “tOD_CS”, Min value has been changed from “3.015” to “3.016” and Max. value changed from “-1.33” to “-0.766”. 

   - For symbol “tDVW”, Min value has been changed from “2.314” to “2.518”. 

   - For symbol “tIH_DQS”, Min value has been changed from “2.767” to “3.134”. 

- uSDHC specifications are updated thoroughly. 

- In "Thermal characteristics": 

   - Updated table header to include all variants. 

   - For S32K312 100-MaxQFP updated RϴJA from 34.8 to 38 °C/W and RϴJT from 0.6 to 0.8 °C/W. 

   - For S32K3x4, 257MAPBGA updated RϴJA from 27 to 26.8 °C/W. 

- Updated Legal information. 

###### Rev 3, Oct 2021 

- Datasheet classification is updated to "Technical data" for S32K344. 

- In section "Supply currents" added values for 85C (typ and max) and updated 105 (max) and 125 (max) values for S32K344. 

- In front page features, added MaxQFP172 with Exposed pad (EP) option and information on I3C. 

- In section "Overview", added a note "S32K3x1, S32K3x2 and S32K3x8 specific information ....". 

- In "Feature comparision" section added footnote to add information about MaxQFP172 with Exposed pad (EP) package for S32K3x8 devices. 

- VDD_HV_SMPS is changed to VDD_DCDC throughout. 

S32K3xx Data Sheet, Rev. 4, 04/2022 Preliminary Information 

Data Sheet: Technical Data 

120 / 130 

NXP Semiconductors 

Revision history 

###### Rev 3, Oct 2021 

- In section "Absolute maximum ratings", footnote attached to "I_INJSUM_DC_ABS" is exteded to add information "See application note AN4731 for...". 

- Figure "Power management system - S32K344, S32K324, S32K341, S32K314, S32K342, and S32K322." is updated to add COUT_V15 capacitor. 

- Figure "Power management system - S32K358" is updated to add COUT_V15 capacitor and optional circuit explained in the notes. 

- In section "SMPS regulator electrical specifications", COUT_V15 is added to "External bypass capacitor". 

- Figure "Package decoupling capacitor pinout diagram" is updated to show MaxQFP172-EP package. 

- Table title "Current limit requirements for board design" is changed to "Recommended current limits in board design" and added a note as "The power supplies for the voltage rails must be...". 

- In section "GPIO DC electrical specifications, 3.3V Range (2.97V - 3.63V)": 

   - for ILKG_33_S updated condition to update pins which has Analog Function Count=2/3 

   - for ILKG_33_M updated condition to update pins which has Analog Function Count=1 

   - added ILKG_33_M with condition "PTE8 and PTD6" 

   - udpdated ILKG_33, -120 nA (min) and 120 nA (max). 

   - updated condition of IOH_*, IOL_* to add < and > symbols. 

   - added IOHT specification. 

   - Updated sentence "I/O current specifications are...". and removed "RMS current values are given....". 

- In section "GPIO DC electrical specifications, 5.0V (4.5V - 5.5V)": 

   - for ILKG_50_S updated condition to update pins which has Analog Function Count=2/3 

   - for ILKG_50_M updated condition to update pins which has Analog Function Count=1 

   - added ILKG_50_M with condition "PTE8 and PTD6" 

   - udpdated ILKG_50, -150 nA (min) and 150 nA (max). 

   - updated condition of IOH_*, IOL_* to add < and > symbols. 

   - added IOHT specification. 

   - Updated sentence "I/O current specifications are...". and removed "RMS current values are given....". 

- In section "5.0V (4.5V - 5.5V) GPIO Output AC Specification": 

   - for Symbol "TR_TF_50_S" with condition "Capacitance=25pF" Min changed from "TBD" to "5" 

   - for Symbol "TR_TF_50_S" with condition "Capacitance=25pF" Max changed from "TBD" to "21" 

   - for Symbol "TR_TF_50_S" with condition "Capacitance=50pF" Min changed from "TBD" to "10" 

   - for Symbol "TR_TF_50_S" with condition "Capacitance=50pF" Max changed from "TBD" to "31" 

   - for Symbol "TR_TF_50_SP" with condition "DSE=0, Capacitance=25pF" Min changed from "5" to "3.5" 

   - for Symbol "TR_TF_50_SP" with condition "DSE=1, Capacitance=25pF" Min changed from "2.4" to "1.2" 

   - for Symbol "TR_TF_50_SP" with condition "DSE=0, Capacitance=50pF" Min changed from "8.9" to "7.1" 

   - for Symbol "TR_TF_50_SP" with condition "DSE=1, Capacitance=50pF" Min changed from "4.1" to "3.4" 

   - for Symbol "TR_TF_50_M" with condition "DSE=0, SRE=0, Capacitance=25pF" Min changed from "2.5" to "1.8" 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

121 / 130 

NXP Semiconductors 

Revision history 

###### Rev 3, Oct 2021 

   - for Symbol "TR_TF_50_M" with condition "DSE=0, SRE=1, Capacitance=25pF" Min changed from "3" to "2.5" 

   - for Symbol "TR_TF_50_M" with condition "DSE=1, SRE=0, Capacitance=25pF" Min changed from "1" to "0.8" 

   - for Symbol "TR_TF_50_F" with condition "DSE=0, SRE=0, Capacitance=25pF" Max changed from "4.3" to "5.3" 

   - for Symbol "TR_TF_50_F" with condition "DSE=1, SRE=0, Capacitance=25pF" Max changed from "1.6" to "3.0" 

- In section "3.3V (2.97V - 3.63V) GPIO Output AC Specification": 

   - for Symbol "TR_TF_33_S" with condition "Capacitance=25pF" Min changed from "TBD" to "6.5" 

   - for Symbol "TR_TF_33_S" with condition "Capacitance=25pF" Max changed from "TBD" to "28" 

   - for Symbol "TR_TF_33_S" with condition "Capacitance=50pF" Min changed from "TBD" to "11" 

   - for Symbol "TR_TF_33_S" with condition "Capacitance=50pF" Max changed from "TBD" to "43" 

   - for Symbol "TR_TF_33_SP" with condition "DSE=0, Capacitance=25pF" Min changed from "5" to "4" 

   - for Symbol "TR_TF_33_SP" with condition "DSE=1, Capacitance=25pF" Min changed from "2.4" to "2.0" 

   - for Symbol "TR_TF_33_M" with condition "DSE=0, SRE=0, Capacitance=25pF" Min changed from "3.2" to "2.2" 

   - for Symbol "TR_TF_33_M" with condition "DSE=0, SRE=1, Capacitance=25pF" Min changed from "3.8" to "3.0" 

   - for Symbol "TR_TF_33_M" with condition "DSE=1, SRE=0, Capacitance=25pF" Min changed from "1" to "0.8" 

   - — for Symbol "TR_TF_33_F" with condition "DSE=0, SRE=0, Capacitance=25pF" Min changed from "1.1" to "0.5" — for Symbol "TR_TF_33_F" with condition "DSE=0, SRE=0, Capacitance=25pF" Max changed from "7.0" to "4" 

   - for Symbol "TR_TF_33_F" with condition "DSE=0, SRE=1, Capacitance=25pF" Min changed from "2.6" to "2.1" 

   - for Symbol "TR_TF_33_F" with condition "DSE=0, SRE=1, Capacitance=25pF" Max changed from "11.0" to "9" 

   - for Symbol "TR_TF_33_F" with condition "DSE=1, SRE=0, Capacitance=25pF" Min changed from "0.8" to "0.4" 

   - for Symbol "TR_TF_33_F" with condition "DSE=1, SRE=0, Capacitance=25pF" Max changed from "3.4" to "2" 

   - — for Symbol "TR_TF_33_F" with condition "DSE=1, SRE=1, Capacitance=25pF" Min changed from "1.5" to "1.2" 

   - for Symbol "TR_TF_33_F" with condition "DSE=1, SRE=1, Capacitance=25pF" Max changed from "7.8" to "6.4" 

   - for Symbol "TR_TF_33_F" with condition "DSE=0, SRE=0, Capacitance=50pF" Min changed from "2.5" to "1.1" 

   - — for Symbol "TR_TF_33_F" with condition "DSE=0, SRE=0, Capacitance=50pF" Max changed from "10.8" to "7" — for Symbol "TR_TF_33_F" with condition "DSE=0, SRE=1, Capacitance=50pF" Min changed from "3.6" to "2.6" — for Symbol "TR_TF_33_F" with condition "DSE=0, SRE=1, Capacitance=50pF" Max changed from "15.0" to "11" 

   - for Symbol "TR_TF_33_F" with condition "DSE=1, SRE=0, Capacitance=50pF" Min changed from "1.5" to "0.8" 

   - for Symbol "TR_TF_33_F" with condition "DSE=1, SRE=0, Capacitance=50pF" Max changed from "5.5" to "4.2" 

   - — for Symbol "TR_TF_33_F" with condition "DSE=1, SRE=1, Capacitance=50pF" Min changed from "2.2" to "1.5" — for Symbol "TR_TF_33_F" with condition "DSE=1, SRE=1, Capacitance=50pF" Max changed from "10.0" to "7.8" 

- In section "SAR ADC", added paragraph "All below specs are applicable when only one ADC instance is in operation ..... to determine the most appropriate settings for AVGS." and removed footnote from RS specification. 

- In section "SAR ADC", added specifications for CP1, CP2 and RSW1 corresponding to all channels, shared channels and precision channels. Also added the related figure. 

- In section "PLL", removed some non-applicable footnotes. 

- In section "LPSPI", added information before the table The Low Power Serial Peripheral Interface (LPSPI) provides a synchronous serial bus with master....". 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

122 / 130 

NXP Semiconductors 

Revision history 

###### Rev 3, Oct 2021 

- In section "LPSPI0 20 MHz and 15 MHz Combinations", added note as "Trace length should not exceed 11 inches for SCK pad when used in Master loopback mode." 

- Added "I3C" specifications. 

- In section "Ethernet MII (100 Mbps)", for "RXCLK frequency" typ value moved to max. 

- In section "Ethernet RMII", added paragraph "The following timing specs are defined at the device I/O pin and must be .....I/O operating voltage ranges from 2.97 V to 3.63 V." 

- In section "QuadSPI Quad 3.3V SDR 120MHz", for Symbol "tSDC" footnote added "For S32K342 100MQFP, tSDC spec would be ..." 

- In section "QuadSPI Quad 3.3V SDR 120MHz" added sentence "Program register value QuadSPI_DLLCRA[SLV_FINE_OFFSET] to 4'b0001.". 

- In section "QuadSPI Octal 3.3V DDR 120MHz", Symbol "tSCK" min is calrified, condition updated to External DQS and "tSCK" with condition Internal Loopback is deleted. 

- In section "QuadSPI Octal 3.3V DDR 120MHz", Symbol "tSDC" condition updated to External DQS and "tSDC" with condition Internal Loopback is deleted.. 

- In section "QuadSPI Octal 3.3V DDR 120MHz", specifications tISU_PCS, tIH_PCS, tCK2CKmin and tCK2CKmax are deleted. 

###### Rev 2, Aug 2021 

- Added section "Overview". 

- In block diagrams: 

   - S32K311/S32K312/S32K314 removed "Scalable ARM M7 core in Lock step" and added "Single ARM M7 core". 

   - S32K322/S32K324 removed "Scalable ARM M7 core in Lock step" and added "Two independent ARM M7 cores". 

- In "Absolute maximum ratings" and "Voltage and current operating requirements": 

   - Some general footnotes are moved to top of table 

   - VDD_HV_SMPS added footnotes 

- In "Voltage and current operating requirements" for VREFH extended footnote "VREFH should always be equal to...". 

- Updated title - Power management system - S32K344, S32K324, S32K341, S32K314, S32K342, and S32K322. 

- In figure "Power management system - S32K358" updated double bond to triple bond. 

- In section "Recommended Decoupling Capacitors" added COUT_V11 with typ as 1 uF. 

- Added section "Power mode transition operating behaviors" and its subsections: 

   - Power mode transition operating behaviour 

   - Boot time, HSE firmware not installed 

   - Boot time, HSE firmware installed 

   - HSE firmware memory verification time examples 

- Moved information from "Supply monitoring" to "Supply diagnosos" and attached it to "AN_ACC". The information is "If V15 > VDD_HV_A +100mV then..." 

- Updated figure "Package decoupling capacitor pinout diagram" to add 289 MapBGA 

S32K3xx Data Sheet, Rev. 4, 04/2022 Preliminary Information 

Data Sheet: Technical Data 

123 / 130 

NXP Semiconductors 

Revision history 

###### Rev 2, Aug 2021 

- In section "Glitch Filter", added sentence ".... WKPU pins and TRGMUX inputs 60-63.". 

- Section "Flash memory program and erase specifications" updated thoroughly. 

- In section "Flash memory module life specifications" removed footnotes 1 and 2. 

- In section "Data retention vs program/erase cycles" added sentence before related to figure "The spec window represents qualified limits.". 

- In section "Flash memory AC timing specifications": 

   - Updated register naming representation 

   - Added footnote to tdrcv min as " In extreme cases (1 block configurations)...". 

   - Max updated to "50 system clock periods" for taistop 

- Ins ection "Flash memory read timing parameters" mantioned part numbers for each table as applicable. 

- >In section "SAR ADC", for Symbol "fAD_CK" added new spec and max updated to 120. 

- In section "FIRC", Symbol "IFIRC" is deleted. 

- In section "SIRC", Symbol "Ivdda" with condition "On state" is deleted. 

- In section "PLL", clarification added in condition column for jitter specifications. 

- In section "Fast External Oscillator (FXOSC)", for Symbol "FREQ_BYPASS", "TRF_BYPASS" and "CLKIN_DUTY_BYPASS" footnote added "For bypass mode applications, the EXTAL ...". 

- In section "Fast External Oscillator (FXOSC)", for Symbol "TFXOSC" footnote added "The startup time specification is valid ...". 

- In section "Fast External Oscillator (FXOSC)", Symbol "IFXOSC" specs are merged into one and description and condition updated. 

- In section "Fast External Oscillator (FXOSC)", added paragraph "Drive level is a crystal specification and ....". 

- In section "LPSPI", Symbol "tSPSCK" with condition "Slave_10Mbps" is added. 

- In section "LPSPI", Symbol "tSPSCK" with condition "Master_10Mbps" is added. 

- Updated title to mention LPSPI0 of "LPSPI0 20 MHz and 15 MHz Combinations", and updated header "20Mbps" to "20Mbps (In loopback mode only)". 

- In "I3C" section, added two sentences. 

- Updated "QuadSPI" sections. 

- Editorial updates. 

###### Rev 2 Draft B, Mar 2021 

- Updated "block diagrams" and "Feature comparison" 

- Updated "Ordering information" to add 289 pagkage and removed one. 

- In section "Absolute maximum ratings", Symbol "VDD_HV_SMPS" is added. 

- In section "Absolute maximum ratings", for Symbol "I_INJPAD_DC_ABS" and "I_INJSUM_DC_ABS" footnote updated "When input pad voltage levels are close ...". 

- In section "Voltage and current operating requirements", Symbol "IINJSUM_DC_OP" and "IINJPAD_DC_OP" condition is updated 

S32K3xx Data Sheet, Rev. 4, 04/2022 Preliminary Information 

Data Sheet: Technical Data 

124 / 130 

NXP Semiconductors 

Revision history 

###### Rev 2 Draft B, Mar 2021 

- In section "Voltage and current operating requirements", Symbol "VDD_HV_SMPS" is added. 

- In section "Voltage and current operating requirements", for Symbol "I_INJPAD_DC_ABS" and "I_INJSUM_DC_ABS" footnote updated "When input pad voltage levels are close ...". 

- In section "Power management": 

   - "Power management system - S32K344, S32K324, S32K314" figure updated. 

   - "Power management system - S32K312, S32K311" figure updated. 

   - "Power management system - S32K358" figure added. 

- In section "Supply Monitoring", Symbol "HVD_V15" is added. 

- In section "Supply Monitoring", for "LVD_VDD_HV_A", symbol and description updated. 

- Added section "SMPS regulator electrical specifications" 

- In section "NPN Ballast Transistor Control Specification", fig with title "Ballast circuit" is changed. 

- In section "Supply currents" and "operating mode" tables are updated. 

- In section "GPIO DC electrical specifications, 3.3V Range (2.97V - 3.63V)", fig with title "Reference Load Diagram" is changed. 

- In section "GPIO DC electrical specifications, 3.3V Range (2.97V - 3.63V)", footnote updated "A positive value is leakage flowing into...". 

- In section "GPIO DC electrical specifications, 5.0V (4.5V - 5.5V)", Symbol "ILKG_50_S_PTE13" with condition "PMC VRC_CTRL pin" is added. 

- In section "GPIO DC electrical specifications, 5.0V (4.5V - 5.5V)", footnote updated "A positive value is leakage flowing into...". 

- In section "GPIO DC electrical specifications, 5.0V (4.5V - 5.5V)", fig with title "Reference Load Diagram" is changed. 

- In section "Flash memory specification", added specs for 512KB and 2MB specifications. 

- In table "Flash memory AC timing specifications", taistop max updated. 

- Updated "Flash Read Wait State Settings" 

- In section "Low Power Comparator (LPCMP)", updated IDLSS typ to 17uA. 

- In section "Low Power Comparator (LPCMP)", updated INL and DNL. 

- In section "Low Power Comparator (LPCMP)", updated paragraph "For devices where the VDD_HV_B domain is present..." 

- In "Low Power Comparator (LPCMP)" added hysterisis plots. 

- In section "PLL", symbol "FPLL_out" description updated to add (PLL_PHIn_CLK) 

- In section "PLL", "IPLL_V25" deleted. 

- In section "PLL", updated jitter specifications. 

- In section "FXOSC", updated paragraph "To improve the FXOSC jitter and duty cycle performance...". 

- In section "SXOSC", updated description of "ISXOSC" to Oscillator Analog circuit supply current. 

- In section "I2C", added paragraph "For supported baud rate ....." 

- Added section "I3C". 

- In section "FlexCAN characteristics", added paragraph "For supported baud rate ....." 

S32K3xx Data Sheet, Rev. 4, 04/2022 Preliminary Information 

Data Sheet: Technical Data 

125 / 130 

NXP Semiconductors 

Revision history 

###### Rev 2 Draft B, Mar 2021 

- Added QuadSPI DDR electrical specifications for Octal and Quad. 

- Added uSDHC specifications. 

- Updated "Thermal characteristics" and "Obtaining package dimensions" 

###### Rev 2 Draft A, Nov 2020 

- Updated features to show maximum memory support up to 8 MB. 

- Added information for S32K341. 

- Updated "Block diagrams". 

- Updated "Feature comparision" 

- Updated "Thermal characterstics" to add data for S32K312 and S32K342. 

- Added document number for 172-pin MaxQFP package in section "Obtaining package dimensions" 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

126 / 130 

NXP Semiconductors 

Legal information 

#### Legal information 

##### Data sheet status 

|Document status<sup>[1][2]</sup>|Product status<sup>[3]</sup>|Definition|
|---|---|---|
|Objective [short] data sheet|Development|This document contains data from the objective specification for product|
|||development.|
|Preliminary [short] data sheet|Qualification|This document contains data from the preliminary specification.|
|Product [short] data sheet|Production|This document contains the product specification.|



[1] Please consult the most recently issued document before initiating or completing a design. 

[2] The term 'short data sheet' is explained in section "Definitions". 

[3] The product status of device(s) described in this document may have changed since this document was published and may differ in case of multiple devices. The latest product status information is available on the Internet at URL http://www.nxp.com. 

##### Definitions 

Draft — A draft status on a document indicates that the content is still under internal review and subject to formal approval, which may result in modifications or additions. NXP Semiconductors does not give any representations or warranties as to the accuracy or completeness of information included in a draft version of a document and shall have no liability for the consequences of use of such information. 

Short data sheet — A short data sheet is an extract from a full data sheet with the same product type number(s) and title. A short data sheet is intended for quick reference only and should not be relied upon to contain detailed and full information. For detailed and full information see the relevant full data sheet, which is available on request via the local NXP Semiconductors sales office. In case of any inconsistency or conflict with the short data sheet, the full data sheet shall prevail. 

Product specification — The information and data provided in a Product data sheet shall define the specification of the product as agreed between NXP Semiconductors and its customer, unless NXP Semiconductors and customer have explicitly agreed otherwise in writing. In no event however, shall an agreement be valid in which the NXP Semiconductors product is deemed to offer functions and qualities beyond those described in the Product data sheet. 

##### Disclaimers 

Limited warranty and liability — Information in this document is believed to be accurate and reliable. However, NXP Semiconductors does not give any representations or warranties, expressed or implied, as to the accuracy or completeness of such information and shall have no liability for the consequences of use of such information. NXP Semiconductors takes no responsibility for the content in this document if provided by an information source outside of NXP Semiconductors. 

In no event shall NXP Semiconductors be liable for any indirect, incidental, punitive, special or consequential damages (including - without limitation - lost profits, lost savings, business interruption, costs related to the removal or replacement of any products or rework charges) whether or not such damages are based on tort (including negligence), warranty, breach of contract or any other legal theory. 

Notwithstanding any damages that customer might incur for any reason whatsoever, NXP Semiconductors’ aggregate and cumulative liability towards customer for the products described herein shall be limited in accordance with the Terms and conditions of commercial sale of NXP Semiconductors. 

Right to make changes — NXP Semiconductors reserves the right to make changes to information published in this document, including without limitation specifications and product descriptions, at any time and without notice. This document supersedes and replaces all information supplied prior to the publication hereof. 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

127 / 130 

NXP Semiconductors 

Legal information 

Applications — Applications that are described herein for any of these products are for illustrative purposes only. NXP Semiconductors makes no representation or warranty that such applications will be suitable for the specified use without further testing or modification. 

Customers are responsible for the design and operation of their applications and products using NXP Semiconductors products, and NXP Semiconductors accepts no liability for any assistance with applications or customer product design. It is customer’s sole responsibility to determine whether the NXP Semiconductors product is suitable and fit for the customer’s applications and products planned, as well as for the planned application and use of customer’s third party customer(s). Customers should provide appropriate design and operating safeguards to minimize the risks associated with their applications and products. 

NXP Semiconductors does not accept any liability related to any default, damage, costs or problem which is based on any weakness or default in the customer’s applications or products, or the application or use by customer’s third party customer(s). Customer is responsible for doing all necessary testing for the customer’s applications and products using NXP Semiconductors products in order to avoid a default of the applications and the products or of the application or use by customer’s third party customer(s). NXP does not accept any liability in this respect. 

Limiting values — Stress above one or more limiting values (as defined in the Absolute Maximum Ratings System of IEC 60134) will cause permanent damage to the device. Limiting values are stress ratings only and (proper) operation of the device at these or any other conditions above those given in the Recommended operating conditions section (if present) or the Characteristics sections of this document is not warranted. Constant or repeated exposure to limiting values will permanently and irreversibly affect the quality and reliability of the device. 

Terms and conditions of commercial sale — NXP Semiconductors products are sold subject to the general terms and conditions of commercial sale, as published at http://www.nxp.com/profile/terms, unless otherwise agreed in a valid written individual agreement. In case an individual agreement is concluded only the terms and conditions of the respective agreement shall apply. NXP Semiconductors hereby expressly objects to applying the customer’s general terms and conditions with regard to the purchase of NXP Semiconductors products by customer. 

No offer to sell or license — Nothing in this document may be interpreted or construed as an offer to sell products that is open for acceptance or the grant, conveyance or implication of any license under any copyrights, patents or other industrial or intellectual property rights. 

Quick reference data — The Quick reference data is an extract of the product data given in the Limiting values and Characteristics sections of this document, and as such is not complete, exhaustive or legally binding. 

Translations — A non-English (translated) version of a document, including the legal information in that document, is for reference only. The English version shall prevail in case of any discrepancy between the translated and English versions. 

Security — Customer understands that all NXP products may be subject to unidentified vulnerabilities or may support established security standards or specifications with known limitations. Customer is responsible for the design and operation of its applications and products throughout their lifecycles to reduce the effect of these vulnerabilities on customer’s applications and products. Customer’s responsibility also extends to other open and/or proprietary technologies supported by NXP products for use in customer’s applications. NXP accepts no liability for any vulnerability. Customer should regularly check security updates from NXP and follow up appropriately. 

Customer shall select products with security features that best meet rules, regulations, and standards of the intended application and make the ultimate design decisions regarding its products and is solely responsible for compliance with all legal, regulatory, and security related requirements concerning its products, regardless of any information or support that may be provided by NXP. 

NXP has a Product Security Incident Response Team (PSIRT) (reachable at PSIRT@nxp.com) that manages the investigation, reporting, and solution release to security vulnerabilities of NXP products. 

Suitability for use in automotive applications — This NXP product has been qualified for use in automotive applications. It has been developed in accordance with ISO 26262 and has been ASIL classified. If this product is used by customer in the development of, or for incorporation into, products or services (a) used in safety critical applications or (b) in which failure could lead to death, personal injury, or severe physical or environmental damage (such products and services hereinafter referred to as “Critical Applications”), then customer makes the ultimate design decisions regarding its products and is solely responsible for compliance with all legal, regulatory, safety, and security related requirements concerning its products, regardless of any information or support that may be provided by NXP. As such, customer assumes all risk related to use of any products in Critical Applications and NXP and its suppliers shall not be liable for any such use by customer. Accordingly, customer will indemnify and hold NXP harmless from any claims, liabilities, damages and associated costs and expenses (including attorneys’ fees) that NXP may incur related to customer’s incorporation of any product in a Critical Application. 

##### Trademarks 

Notice: All referenced brands, product names, service names, and trademarks are the property of their respective owners. 

NXP — wordmark and logo are trademarks of NXP B.V. 

Export control — This document as well as the item(s) described herein may be subject to export control regulations. Export might require a prior authorization from competent authorities. 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

128 / 130 

NXP Semiconductors 

Legal information 

AMBA, Arm, Arm7, Arm7TDMI, Arm9, Arm11, Artisan, big.LITTLE, Cordio, CoreLink, CoreSight, Cortex, DesignStart, DynamIQ, Jazelle, Keil, Mali, Mbed, Mbed Enabled, NEON, POP, RealView, SecurCore, Socrates, Thumb, TrustZone, ULINK, ULINK2, ULINK-ME, ULINK-PLUS, ULINKpro, μVision, Versatile — are trademarks or registered trademarks of Arm Limited (or its subsidiaries) in the US and/or elsewhere. The related technology may be protected by any or all of patents, copyrights, designs and trade secrets. All rights reserved. 

Bluetooth — the Bluetooth wordmark and logos are registered trademarks owned by Bluetooth SIG, Inc. and any use of such marks by NXP Semiconductors is under license. 

EdgeLock — is a trademark of NXP B.V. 

elQ — is a trademark of NXP B.V. 

I2C-bus — logo is a trademark of NXP B.V. 

NXP SECURE CONNECTIONS FOR A SMARTER WORLD — is a trademark of NXP B.V. 

SafeAssure — is a trademark of NXP B.V. 

SafeAssure — logo is a trademark of NXP B.V. 

SuperFlash This product uses SuperFlash<sup>®</sup> technology. SuperFlash<sup>®</sup> is a registered trademark of Silicon Storage Technology, Inc. 

Synopsys & Designware — are registered trademarks of Synopsys, Inc. 

Synopsys — Portions Copyright<sup>©</sup> 2021 Synopsys, Inc. Used with permission. All rights reserved. 

S32K3xx Data Sheet, Rev. 4, 04/2022 

Data Sheet: Technical Data 

Preliminary Information 

129 / 130 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0130-00.png)



![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0130-01.png)



![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_DS/S32K3xxDS_参考手册.pdf-0130-02.png)


Please be aware that important notices concerning this document and the product(s) described herein, have been included in section 'Legal information'. 

© NXP B.V. 2022. 

All rights reserved. 

For more information, please visit: http://www.nxp.com For sales office addresses, please send an email to: salesaddresses@nxp.com 

Date of release: 04/2022 Document identifier: S32K3XX 

