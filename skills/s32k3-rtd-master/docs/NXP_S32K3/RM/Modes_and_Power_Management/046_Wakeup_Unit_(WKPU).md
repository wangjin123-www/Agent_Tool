NXP Semiconductors 

# Chapter 46 Wakeup Unit (WKPU) 

## 46.1 Chip-specific WKPU information 

### 46.1.1 WKPU configuration on the chip 

WKPU provides the following features: 

- A configurable, low-power wake-up capability to the chip from multiple configurable asynchronous wake-up events. 

- Support for four internal and minimum 59 external source depending on the chip, that can generate interrupts or wakeup events. 

- Support for an NMI input. 

Table 228. WKPU configuration on the chip 

|Number of sources, interrupts, and<br>vectors|S32K3x4/<br>S32K3x2|S32K358|Description|
|---|---|---|---|
|NMI sources|1|1|Single NMI pin routed to all application cores|
|Internal wake-up sources|4|4|• SWT_0 wake-up, RTC-API wake-up<br>• RTC timeout<br>• Analog comparator round robin wake-up<br>(from LPCMP_0, 1, and 2 round robin wake-<br>up)<sup>1</sup><br>• RTI wake-up|
|External wake-up sources|60|67|Minimum 59 GPIO pins (WKPU[0]-WKPU[59])<sup>2</sup><br>support the wake-up functionality. See the<br>IOMUX file attached to this document for details.|
|Glitch filters for external interrupts|60|67|Glitch filter on each external wake-up source|
|External interrupt vectors|8|8|—|



1. Both wake-up sources 0 (RTC-API) and 2 (CMP_x trigger mode wake-up) use RTC-API wake-up, with Trigger mode having a higher priority. This means, if you configure LPCMP_x.RRCR0[ERR_EN] for either of the comparators, the RTC_API wake-up is used only for the CMP_x trigger mode operation. The RTC-API wake-up does not cause wake-up from Standby mode in this scenario. 

2. For S32K312, WKPU[34] is reserved. 

All of the aforementioned wake-up sources can be enabled or disabled. Also, you can configure these wake-up sources, by using WKPU configuration registers, to provide wake-up on rising or falling events. See the WKPU register memory map for details. 

~~<mark>NOTE</mark>~~ 

You must use SIUL2 to perform WKPU pin configurations (PUE, PUS, and IBE). For this, you must first configure SIUL2.MSCR[IBE] for the corresponding pin. This chip does not support WKPU-provided pin configurations; it supports only bypass control. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1571 / 4640 

NXP Semiconductors 

Wakeup Unit (WKPU) 

### 46.1.2 WKPU register fields and their applicability 

Table 229. WKPU register fields and applicability 

|Register|Field|Chips where applicable|
|---|---|---|
|NSR|NIF1|S32K324, S32K322|
|NSR|NOVF1|S32K324, S32K322|
|NCR|NLOCK1|S32K324, S32K322|
|NCR|NDSS1|S32K324, S32K322|
|NCR|NWRE1|S32K324, S32K322|
|NCR|NREE1|S32K324, S32K322|
|NCR|NFEE1|S32K324, S32K322|
|NCR|NFE1|S32K324, S32K322|



### 46.1.3 WKPU NMI configuration 

WKPU supports one external source that can cause non-maskable interrupts to on-chip cores and wake-up events to the system. 

The following figure shows applicable cores, some family chips may not have cores Cortex-M7_1 or Cortex-M7_2. In case of a wake-up event (internal or external), WKPU initiates the recovery of the chip and feeds an interrupt to the core(s) depending on the configuration. The sections that follow provide details related to the associated configurations. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/046_Wakeup_Unit_-WKPU-/S32K3XXRM_数据表.pdf-1572-08.png)


<!-- Start of picture text -->
Cortex-M7_0 Cortex-M7_1 Cortex-M7_2<br>Destination Destination Destination<br>System wake-up<br>Flag Overrun Flag Overrun Flag Overrun<br>Edge detect Edge detect Edge detect<br>Glitch filter<br>NMI<br>NMI Configuration Register (NCR)<br>Nonmaskable interrutp Nonmaskable interrutp Nonmaskable interrutp<br>NDSS[0] NWRE[0] NREE[0] NFEE[0] NFE[0] NDSS[1] NWRE[1] NREE[1] NFEE[1] NDSS[2] NWRE[2] NREE[2] NFEE[2] RDSS RWRE RREE RFEE<br><!-- End of picture text -->

Figure 174. WKPU NMI configuration 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1572 / 4640 

NXP Semiconductors 

Wakeup Unit (WKPU) 

### 46.1.4 WKPU wake-up source connectivity 

WKPU allows the external NMI pin to assert the core NMIs on the chip. NMI supports NSR's status and overrun flags. This is what you could do using NCR: 

- Control the NMI destination interrupt by configuring NCR[NDSS]. 

- Control the rising edge, falling edge, or either of the edge reactions to the NMI pin by using bits 2:0 of NCR[NFEE] and NCR[NREE]. The enabling of these edge reactions to the NMI pin is independent of each core. 

WKPU supports the capturing of a second event per NMI input before the interrupt is cleared, thus reducing the chance of losing an NMI event. 

The following figure shows routing of external wake-up events or interrupts with WKPU and the system interrupt controller. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/046_Wakeup_Unit_-WKPU-/S32K3XXRM_数据表.pdf-1573-08.png)


<!-- Start of picture text -->
Interrupt vectors Mode and<br>power control<br>Interrupt<br>controller Wake-up enable<br>WRER_64[31:0]<br>OR OR OR OR OR OR OR OR<br>WRER[31:0]<br>IRER_64[31:0] Interrupt enable IRER[31:0] Interrupt enable<br>Flag[31:24] Flag[23:16] Flag[15:8] Flag[7:0] WISR_64[31:0] Flag[31:24] Flag[23:16] Flag[15:8] Flag[7:0] WISR[31:0]<br>Rising Rising<br>Edge detection WIREER_64[31:0] Edge detection WIREER[31:0]<br>Glitch filter enable Falling Glitch filter enable Falling<br>WIFER_64[31:0] Analog glitch filter WIFEER_64[31:0] WIFER[31:0] Analog glitch filter WIFEER[31:0]<br>Interrupt edge enable Interrupt edge enable<br>External wake-up pins External wake-up pins<br>RTI wake-up RTC timeout<br>CMP_0 round-robin wake-upCMP_1 round-robin wake-upCMP_2 round-robin wake-up SWT_0 timeoutRTC API wake-up<br><!-- End of picture text -->

Figure 175. WKPU wake-up source connectivity 

This is the wake-up source mapping to WKPU: 

- Wake-up source 0 : SWT_0 timeout, RTC-API API wake-up 

- Wake-up source 1 : RTC-API RTC timeout 

- Wake-up source 2 : Round robin wake-up interrupt (Trigger mode interrupt) from LPCMP_0, LPCMP_1, or LPCMP_2 

- Wake-up source 3 : RTI wake-up 

- Wake-up source 4 : Wake-up source minimum 59-external pin wake-up sources, WKPU[0]-WKPU[59] 

If you configure any or all of the LPCMP_x.RRCR0[RR_EN] fields to be active, the corresponding CMP_x pins must be dedicated for the CMP_x operation. In case you are not using any of the CMPs, you can use SIUL2.MSCRx[SSS] to configure the pins for digital functionalities. 

~~<mark>NOTE</mark>~~ 

You must enable WKPU (by using MC_ME.PRTNx_COFBy_CLKEN) before entering any of the chip's lowpower modes. 

## 46.2 Introduction 

The WKPU supports 64 external sources that can generate interrupts or wakeup events and 3 external source(s) that can cause non-maskable interrupt request(s) or wakeup event(s). In addition, it combines its wakeup events with those generated from other wakeup sources to supply a single wakeup to the system. The block diagram of WKPU and its interfaces to other system components is shown below. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1573 / 4640 

NXP Semiconductors 

Wakeup Unit (WKPU) 

~~<mark>NOTE</mark>~~ 

The signal widths in the following diagram might not depict this device's particular configuration. See chip-specific WKPU for more information. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/046_Wakeup_Unit_-WKPU-/S32K3XXRM_数据表.pdf-1574-04.png)


<!-- Start of picture text -->
Wakeup unit<br>0-4<br>NMI / Wakeup 0-4 Platform<br>- Configuration 0-4<br>NMI enable<br>Filter bypass<br>Wakeup<br>0-4<br>Filter Pads<br>Peripheral bus IOMUX<br>0-64<br>IRQ / Wakeup Filter<br>- Configuration<br>Filter bypass<br>Mode/<br>Sys wakeup<br>Power CTL<br>0-4 Interrupt<br>IRQs<br>controller<br>0-64<br>RTC, etc.<br><!-- End of picture text -->

Figure 176. WKPU and connected system components 

## 46.3 Features 

The WKPU supports these features: 

- Non-maskable interrupt support with: 

   - 3 NMI sources 

   - 3 analog glitch filters 

   - Independent interrupt destination for each core: 

      - ◦Non-maskable interrupt 

      - ◦Critical interrupt 

   - Active (rise/fall) edge selection control for events 

   - Configurable system wakeup triggering from NMI sources 

- External wakeup/interrupt support with: 

   - One System interrupt vector for interrupt sources 

   - 64 analog glitch filters 

   - Independent interrupt mask 

   - Edge detection 

   - Configurable system wakeup triggering from all interrupt sources 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1574 / 4640 

NXP Semiconductors 

Wakeup Unit (WKPU) 

## 46.4 Functional description 

This section provides functional description of WKPU. 

### 46.4.1 Non-maskable interrupts 

The WKPU supports the capturing of a second event per NMI input before the interrupt is cleared, thus reducing the chance of losing an NMI event, although it creates an overrun condition. 

Each NMI passes through a bypassable analog glitch filter. 

~~<mark>NOTE</mark>~~ 

Glitch filter control and pad configuration should be performed when NMI is disabled, to avoid erroneous triggering by glitches caused by the configuration process itself. 

- ~~<mark>NOTE</mark>~~ 

The figure below represents a generic configuration and might not represent this particular device's configuration. See the chip-specific information for details on this chip's WKPU. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/046_Wakeup_Unit_-WKPU-/S32K3XXRM_数据表.pdf-1575-11.png)


<!-- Start of picture text -->
CPU CPU CPU CPU<br>Mode/<br>Pwr Ctl<br>Destination Destination Destination Destination<br>Wakeup Enable Wakeup Enable Wakeup Enable Wakeup Enable<br>Flag Overrun Flag Overrun Flag Overrun Flag Overrun<br>Edge Detect Edge Detect Edge Detect Edge Detect<br>Glitch Filter Glitch Filter Glitch Filter Glitch Filter<br>NMI Configuration Register (NCR)<br>MMI critical IRQ machine check MMI critical IRQ machine check MMI critical IRQ machine check MMI critical IRQ machine check<br>NDSS[0] NWRE[0] NREE[0] NFEE[0] NFE[0] NDSS[1] NWRE[1] NREE[1] NFEE[1] NFE[1] NDSS[2] NWRE[2] NREE[2] NFEE[2] NFE[2] NDSS[3] NWRE[3] NREE[3] NFEE[3] NFE[3]<br><!-- End of picture text -->

Figure 177. NMI pad diagram 

#### 46.4.1.1 NMI management 

Each NMI can be enabled or disabled independently. This can be performed using the single NCR register laid out to contain all configuration bits for a given NMI in a single byte (see NMI Configuration Register (NCR)). A pad defined as an NMI can be configured by the user to recognize interrupts with an active rising edge, an active falling edge, or both edges being active. A setting of having both edge events disabled results in no interrupt being detected and should not be configured. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1575 / 4640 

NXP Semiconductors 

Wakeup Unit (WKPU) 

The active NMI edge is controlled by the user through the configuration of the NCR[NREEn] and NCR[NFEEn] bits. 

~~<mark>NOTE</mark>~~ After reset, NREE and NFEE are set to '0'; therefore, the NMI functionality is disabled after reset and must be enabled explicitly by software. 

After a pad's NMI functionality is enabled, the pad cannot be reconfigured to override or disable the NMI. See the chip-specific WKPU information for details of NMI implementation. 

The NMI destination interrupt is controlled by the user through the configuration of the NCR[NDSSn] bits. See NMI Configuration Register (NCR) for details. 

Each NMI supports a status flag and an overrun flag, which are located in the NSR register (see NMI Status Flag Register (NSR)). This register is a clear-by-write-1 register type, preventing inadvertent overwriting of other flags in the same register. The status flag is set whenever an NMI event is detected. The overrun flag is set whenever an NMI event is detected and the status flag is set (that is, status flag has not been cleared). 

~~<mark>NOTE</mark>~~ 

The overrun flag is cleared by writing a '1' to the appropriate overrun bit in the NSR register. If the status bit is cleared and the overrun bit is still set, the pending interrupt is not cleared. 

During an NMI ISR, on wakeup of the chip from an NMI, any writes to the ECC-protected memory must have the correct ECC. 

## 46.5 External wakeups/interrupts 

The WKPU supports 3 interrupt vectors to the interrupt controller of the chip. Each interrupt vector can support up to the number of external interrupt sources from the device pads, with the total across all vectors being equal to the number of external interrupt sources. Each external interrupt source is assigned to exactly one interrupt vector. The interrupt vector assignment is sequential so that one interrupt vector is for external interrupt sources 0 through N-1, the next is for N through N+M-1, and so forth. 

See the following figure for an overview of the external interrupt implementation, showing an example of four interrupt vectors with eight external interrupt sources each. 

~~<mark>NOTE</mark>~~ 

The figure below shows a generic representation of WKPU. See the chip-specific WKPU information for details on how this device's configuration might differ from this figure. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1576 / 4640 

NXP Semiconductors 

###### Wakeup Unit (WKPU) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/046_Wakeup_Unit_-WKPU-/S32K3XXRM_数据表.pdf-1577-02.png)


<!-- Start of picture text -->
Int<br>Vectors<br>Interrupt Mode/<br>Controller Pwr Ctl<br>IRQ_31_24 IRQ_23_16 IRQ_15_08 IRQ_07_00<br>Wakeup enable<br>OR OR OR OR WRER[31:0]<br>IRER[31:0] Interrupt enable<br>Flag[31:24] Flag[23:16] Flag[15:8] Flag[7:0] WISR[31:0]<br>Rising<br>Edge Detection WIREER[31:0]<br>Glitch Filter enable Falling<br>WIFER[31:0] Analog Glitch Filter WIFEER[31:0]<br>Interrupt Edge Enable<br>Pads<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/046_Wakeup_Unit_-WKPU-/S32K3XXRM_数据表.pdf-1577-03.png)


<!-- Start of picture text -->
Figure 178. External interrupt pad diagram<br><!-- End of picture text -->

All of the external interrupt pads within a single group have equal priority. It is the responsibility of the user software to search through the group of sources in the most appropriate way for their application. 

The priority of the vectors used by the external interrupt pads is set based on the platform and the interrupt controller's priority levels, but the allocation of pads to each group of interrupts can be independently configured by the chip. 

External interrupt lines have a digital glitch filter applied to them. 

### 46.5.1 External interrupt management 

Each interrupt can be enabled or disabled independently. This can be performed using a single rolled-up register (Interrupt Request Enable Register (IRER)). A pad defined as an external interrupt can be configured by the user to recognize interrupts with an active rising edge, an active falling edge, or both edges being active. 

~~<mark>NOTE</mark>~~ 

Writing a '0' to both IREE[x] and IFEE[x] disables the external interrupt functionality for that pad completely (that is, no system wakeup or interrupt is generated on any activity of that pad). 

The active IRQ edge is controlled by users through the configuration of the registers WIREER and WIFEER. 

Each external interrupt supports an individual flag, which is held in the flag register, WISR. This register is a clear-by-write-1 register type, preventing inadvertent overwriting of other flags in the same register. 

## 46.6 Initialization information 

This section discusses initialization for the following features: 

- Glitch filter and pad configuration 

- Non-maskable interrupts 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1577 / 4640 

NXP Semiconductors 

Wakeup Unit (WKPU) 

### 46.6.1 Glitch filter and pad configuration 

Glitch filter control and pad configuration should be performed when the NMI is disabled. This is to avoid erroneous triggering by glitches caused by the configuration process. 

When enabling the glitch filter, do not enable the rising-/falling-edge events bits, i.e., the NCR[NREE], NCR[NFEE], NCR[RREE], and NCR[RFEE] bits in the same register write. 

### 46.6.2 Non-maskable interrupts 

If the IBE of NMI is tied off to 1, no false interrupt is expected. 

## 46.7 WKPU memory map and registers 

### 46.7.1 WKPU register descriptions 

This section provides a detailed description of all the registers accessible in the WKPU module. 

~~<mark>NOTE</mark>~~ 

Reserved registers read as zero and writes have no effect. A transfer error is generated when trying to access a completely reserved register space. The field length of external pad control registers depends on the number of WKPU channels implemented in a chip. 

#### 46.7.1.1 WKPU memory map 

WKPU base address: 402B_4000h 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|0h|NMI Status Flag Register (NSR)|32|W1C|0000_0000h|
|8h|NMI Configuration Register (NCR)|32|RW|6060_6000h|
|14h|Wakeup/Interrupt Status Flag Register (WISR)|32|W1C|0000_0000h|
|18h|Interrupt Request Enable Register (IRER)|32|RW|0000_0000h|
|1Ch|Wakeup Request Enable Register (WRER)|32|RW|0000_0000h|
|28h|Wakeup/Interrupt Rising-Edge Event Enable Register (WIREER)|32|RW|0000_0000h|
|2Ch|Wakeup/Interrupt Falling-Edge Event Enable Register (WIFEER)|32|RW|0000_0000h|
|30h|Wakeup/Interrupt Filter Enable Register (WIFER)|32|RW|0000_0000h|
|54h|Wakeup/Interrupt Status Flag Register (WISR_64)|32|W1C|0000_0000h|
|58h|Interrupt Request Enable Register (IRER_64)|32|RW|0000_0000h|
|5Ch|Wakeup Request Enable Register (WRER_64)|32|RW|0000_0000h|
|68h|Wakeup/Interrupt Rising-Edge Event Enable Register (WIREER_64)|32|RW|0000_0000h|
|6Ch|Wakeup/Interrupt Falling-Edge Event Enable Register (WIFEER_64)|32|RW|0000_0000h|
|70h|Wakeup/Interrupt Filter Enable Register (WIFER_64)|32|RW|0000_0000h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1578 / 4640 

NXP Semiconductors 

Wakeup Unit (WKPU) 

#### 46.7.1.2 NMI Status Flag Register (NSR) 

##### Offset 

|Register|Offset|
|---|---|
|NSR|0h|



##### Function 

This register holds the non-maskable interrupt status flags. 

~~<mark>NOTE</mark>~~ 

This register is accessible by 8-, 16-, and 32-bit read/write operations. 

##### Access: User read/write 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/046_Wakeup_Unit_-WKPU-/S32K3XXRM_数据表.pdf-1579-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>NOVF NOVF<br>R NIF0  NIF1<br>0  1<br>Reserved  Reserved<br>W W1C W1C W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>NOVF<br>R NIF2<br>2<br>Reserved  Reserved  Reserved<br>W W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|NMI Status Flag 0|
|NIF0|This flag can be cleared only by writing 1. Writing 0 has no effect. If enabled (NREE0 or NFEE0 set), NIF0<br>causes an interrupt request.|
||0b - No event has occurred on the pad<br>1b - An event as defined by NREE0 and NFEE0 has occurred|
|30|NMI Overrun Status Flag 0|
|NOVF0|This flag can be cleared only by writing 1. Writing 0 has no effect. It will be a copy of the current NIF0 value<br>whenever an NMI event occurs, thereby indicating to the software that the NMI occurred when the last one<br>was not yet serviced. If enabled (NREE0 or NFEE0 set), NOVF0 causes an interrupt request.<br>0b - No overrun has occurred on NMI input 0<br>1b - An overrun has occurred on NMI input 0|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1579 / 4640 

NXP Semiconductors 

Wakeup Unit (WKPU) 

Table continued from the previous page... 

|Field<br>29-24<br>—|Function<br>Reserved|
|---|---|
|23<br>NIF1|NMI Status Flag 1<br>This flag can be cleared only by writing 1. Writing 0 has no effect. If enabled (NREE1 or NFEE1 set), NIF1<br>causes an interrupt request.<br>0b - No event has occurred on the pad<br>1b - An event as defined by NREE1 and NFEE1 has occurred|
|22<br>NOVF1|NMI Overrun Status Flag 1<br>This flag can be cleared only by writing 1. Writing 0 has no effect. It will be a copy of the current NIF1 value<br>whenever an NMI event occurs, thereby indicating to the software that the NMI occurred when the last one<br>was not yet serviced. If enabled (NREE1 or NFEE1 set), NOVF1 causes an interrupt request.<br>0b - No overrun has occurred on NMI input 1<br>1b - An overrun has occurred on NMI input 1|
|21-16<br>—|Reserved|
|15<br>NIF2|NMI Status Flag 2<br>This flag can be cleared only by writing 1. Writing 0 has no effect. If enabled (NREE2 or NFEE2 set), NIF2<br>causes an interrupt request.<br>0b - No event has occurred on the pad<br>1b - An event as defined by NREE2 and NFEE2 has occurred|
|14<br>NOVF2|NMI Overrun Status Flag 2<br>This flag can be cleared only by writing 1. Writing 0 has no effect. It will be a copy of the current NIF2 value<br>whenever an NMI event occurs, thereby indicating to the software that an NMI occurred while the last one<br>was not yet serviced. If enabled (NREE2 or NFEE2 set), NOVF2 causes an interrupt request.<br>0b - No overrun has occurred on NMI input 2<br>1b - An overrun has occurred on NMI input 2|
|13-8|Reserved|
|—<br>7-6<br>—|Reserved|
|5-0<br>—|Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1580 / 4640 

NXP Semiconductors 

Wakeup Unit (WKPU) 

#### 46.7.1.3 NMI Configuration Register (NCR) 

##### Offset 

|Register|Offset|
|---|---|
|NCR|8h|



##### Function 

This register holds the configuration bits for the non-maskable interrupt settings. 

~~<mark>NOTE</mark>~~ 

- This register is accessible by 8-, 16-, and 32-bit read/write operations. 

- Writing 0 to both NREE[n] and NFEE[n] disables the NMI functionality completely (that is, no non-maskable interrupt is generated on any pad activity). 

Access: User read/write 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/046_Wakeup_Unit_-WKPU-/S32K3XXRM_数据表.pdf-1581-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R NLOC NWRE 0 NREE NLOC NWRE 0 NREE<br>NDSS0  NFEE0  NFE0  NDSS1  NFEE1  NFE1<br>W K0  0  0  K1  1  1<br>Reset 0 1 1 0 0 0 0 0 0 1 1 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R NLOC NWRE 0 NREE<br>NDSS2  NFEE2  NFE2  Reserved<br>K2  2  2<br>W<br>Reset 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|NMI Configuration Lock Register 0|
|NLOCK0|Writing 1 to this bit locks the configuration for the NMI until it is unlocked by a system reset or STANDBY0<br>mode exit. Writing 0 has no effect.|
|30-29|NMI Destination Source Select 0|
|NDSS0|As wakeup does not support another interrupt than NMI, the destination source select signal<br>bits are reserved and always retain their reset value. This means no other request other than<br>NMI can be generated.<br>~~NOTE~~|
||00b - Non-maskable interrupt|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1581 / 4640 

NXP Semiconductors 

Wakeup Unit (WKPU) 

Table continued from the previous page... 

|Field|Function<br>01b - Reserved<br>10b - Reserved<br>11b - Reserved|
|---|---|
|28<br>NWRE0|NMI Wakeup Request Enable 0<br>0b - System wakeup requests from the corresponding NIF0 field are disabled<br>1b - Causes a system wakeup request when NIF0 = 1 or NOVF0 = 1|
|27<br>—|Reserved|
|26|NMI Rising-Edge Events Enable 0|
|NREE0|0b - Rising-edge event is disabled|
||1b - Rising-edge event is enabled|
|25|NMI Falling-edge Events Enable 0|
|NFEE0|0b - Falling-edge event is disabled<br>1b - Falling-edge event is enabled|
|24<br>NFE0|NMI Filter Enable 0<br>Enable analog glitch filter on the NMI pad input.<br>0b - Filter is disabled<br>1b - Filter is enabled|
|23<br>NLOCK1|NMI Configuration Lock Register 1<br>Writing 1 to this bit locks the configuration for the NMI until it is unlocked by a system reset or STANDBY0<br>mode exit . Writing 0 has no effect.|
|22-21|NMI Destination Source Select 1|
|NDSS1|~~NOTE~~|
||As wakeup does not support another interrupt than NMI, the destination source select signal<br>bits are reserved and always retain their reset value. This means no other request other than<br>NMI can be generated.|
||00b - Non-maskable interrupt<br>01b - Reserved<br>10b - Reserved<br>11b - Reserved|
|20|NMI Wakeup Request Enable 1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1582 / 4640 

NXP Semiconductors 

Wakeup Unit (WKPU) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|NWRE1|0b - System wakeup requests from the corresponding NIF1 field are disabled<br>1b - Causes a system wakeup request when NIF1 = 1 or NOVF1 = 1|
|19<br>—|Reserved|
|18|NMI Rising-Edge Events Enable 1|
|NREE1|0b - Rising-edge event is disabled<br>1b - Rising-edge event is enabled|
|17|NMI Falling-Edge Events Enable 1|
|NFEE1|0b - Falling-edge event is disabled<br>1b - Falling-edge event is enabled|
|16<br>NFE1|NMI Filter Enable 1<br>Enable analog glitch filter on the NMI pad input.<br>0b - Filter is disabled<br>1b - Filter is enabled|
|15|NMI Configuration Lock Register 2|
|NLOCK2|Writing 1 to this bit locks the configuration for the NMI until it is unlocked by a system reset. Writing 0 has<br>no effect.|
|14-13|NMI Destination Source Select 2|
|NDSS2|Since wakeup does not support any other interrupt other than NMI, the destination source<br>select signal bits are reserved and will always retain their reset value. This means no other<br>request other than NMI can be generated.<br>~~NOTE~~<br>00b - Non-maskable interrupt<br>01b - Reserved<br>10b - Reserved<br>11b - Reserved|
|12<br>NWRE2|NMI Wakeup Request Enable 2<br>0b - System wakeup requests from the corresponding NIF2 field are disabled<br>1b - Causes a system wakeup request when NIF2 = 1 or NOVF2 = 1|
|11|Reserved<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1583 / 4640 

NXP Semiconductors 

Wakeup Unit (WKPU) 

##### Table continued from the previous page... 

|Field<br>—|Function|
|---|---|
|10|NMI Rising-Edge Events Enable 2|
|NREE2|0b - Rising-edge event is disabled<br>1b - Rising-edge event is enabled|
|9<br>NFEE2|NMI Falling-Edge Events Enable 2<br>0b - Falling-edge event is disabled<br>1b - Falling-edge event is enabled|
|8<br>NFE2|NMI Filter Enable 2<br>Enable analog glitch filter on the NMI pad input.<br>0b - Filter is disabled<br>1b - Filter is enabled|
|7-0<br>—|Reserved|



#### 46.7.1.4 Wakeup/Interrupt Status Flag Register (WISR) 

##### Offset 

|Register|Offset|
|---|---|
|WISR|14h|



##### Function 

This register holds the wakeup/interrupt flags. 

~~<mark>NOTE</mark>~~ 

- This register is accessible only by 32-bit read/write operations. 

- Status bits associated with on-chip wakeup sources are located at the left of the external wakeup/interrupt status bits and are read-only. The wakeup for these sources must be configured and cleared at the on-chip wakeup source. Also, the configuration registers for the external interrupts/wakeups do not have corresponding bits. 

Access: User read/write 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1584 / 4640 

NXP Semiconductors 

Wakeup Unit (WKPU) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||EIF|||||||||
|W||||||||W1|C||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||EIF|||||||||
|W||||||||W1|C||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-0|External Wakeup/Interrupt Status Flag x|
|EIF|This flag can be cleared only by writing 1. Writing 0 has no effect. If enabled (IRER[x]), EIF[x] causes an<br>interrupt request.|
||0b - No event has occurred on the pad|
||1b - An event as defined by WIREER and WIFEER has occurred|



#### 46.7.1.5 Interrupt Request Enable Register (IRER) 

##### Offset 

|Register|Offset|
|---|---|
|IRER|18h|



##### Function 

This register is used to enable the interrupt messaging from the wakeup/interrupt pads to the interrupt controller. 

~~<mark>NOTE</mark>~~ This register is accessible only by 32-bit read/write operations. 

Access: User read/write 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1585 / 4640 

NXP Semiconductors 

Wakeup Unit (WKPU) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/046_Wakeup_Unit_-WKPU-/S32K3XXRM_数据表.pdf-1586-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>EIRE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>EIRE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|External Interrupt Request Enable x|
|EIRE|0b - Interrupt requests from the corresponding EIF[x] bit are disabled|
||1b - A set EIF[x] bit causes an interrupt request|



#### 46.7.1.6 Wakeup Request Enable Register (WRER) 

##### Offset 

|Register|Offset|
|---|---|
|WRER|1Ch|



##### Function 

This register is used to enable the system wakeup messaging from the wakeup/interrupt pads to the mode entry and power control modules. 

~~<mark>NOTE</mark>~~ 

This register is accessible only by 32-bit read/write operations. 

If a pin is disabled through this register, the corresponding bits in the WIFEER and WIREER registers must be written to 0 to ensure that the pin does not respond to any change. 

Access: User read/write 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1586 / 4640 

NXP Semiconductors 

Wakeup Unit (WKPU) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/046_Wakeup_Unit_-WKPU-/S32K3XXRM_数据表.pdf-1587-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>WRE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>WRE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|External Wakeup Request Enable x|
|WRE|0b - System wakeup requests from corresponding EIF[x] bit are disabled|
||1b - A set EIF[x] bit causes a system wakeup request|



#### 46.7.1.7 Wakeup/Interrupt Rising-Edge Event Enable Register (WIREER) 

##### Offset 

|Register|Offset|
|---|---|
|WIREER|28h|



##### Function 

This register is used to enable rising-edge triggered events on the corresponding wakeup/interrupt pads. 

|~~NOTE~~|
|---|
|This register is accessible only by 32-bit read/write operations.|



Access: User read/write 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1587 / 4640 

NXP Semiconductors 

Wakeup Unit (WKPU) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/046_Wakeup_Unit_-WKPU-/S32K3XXRM_数据表.pdf-1588-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>IREE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>IREE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|External Interrupt Rising-edge Events Enable x|
|IREE|0b - Rising-edge event is disabled|
||1b - Rising-edge event is enabled|



#### 46.7.1.8 Wakeup/Interrupt Falling-Edge Event Enable Register (WIFEER) 

##### Offset 

|Register|Offset|
|---|---|
|WIFEER|2Ch|



##### Function 

This register is used to enable falling-edge triggered events on the corresponding wakeup/interrupt pads. 

|~~NOTE~~|
|---|
|This register is accessible only by 32-bit read/write operations.|



Access: User read/write 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1588 / 4640 

NXP Semiconductors 

Wakeup Unit (WKPU) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/046_Wakeup_Unit_-WKPU-/S32K3XXRM_数据表.pdf-1589-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>IFEEx<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>IFEEx<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|External Interrupt Falling-edge Events Enable x|
|IFEEx|0b - Falling-edge event is disabled|
||1b - Falling-edge event is enabled|



#### 46.7.1.9 Wakeup/Interrupt Filter Enable Register (WIFER) 

##### Offset 

|Register|Offset|
|---|---|
|WIFER|30h|



##### Function 

This register is used to enable an analog filter on the corresponding interrupt pads to filter out glitches on the inputs. 

~~<mark>NOTE</mark>~~ This register is accessible only by 32-bit read/write operations. 

Access: User read/write 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1589 / 4640 

NXP Semiconductors 

Wakeup Unit (WKPU) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/046_Wakeup_Unit_-WKPU-/S32K3XXRM_数据表.pdf-1590-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>IFE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>IFE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|External Interrupt Filter Enable x|
|IFE|Enable analog glitch filter on the external interrupt pad input.|
||0b - Filter is disabled|
||1b - Filter is enabled|



#### 46.7.1.10 Wakeup/Interrupt Status Flag Register (WISR_64) 

##### Offset 

|Register|Offset|
|---|---|
|WISR_64|54h|



##### Function 

This register holds the wakeup/interrupt flags. 

~~<mark>NOTE</mark>~~ 

- This register is accessible only by 32-bit read/write operations. 

- Status bits associated with on-chip wakeup sources are located to the left of the external wakeup/interrupt status bits and are read-only. The wakeup for these sources must be configured and cleared at the on-chip wakeup source. Also, the configuration registers for the external interrupts/wakeups do not have corresponding bits. 

Access: User read/write 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1590 / 4640 

NXP Semiconductors 

Wakeup Unit (WKPU) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/046_Wakeup_Unit_-WKPU-/S32K3XXRM_数据表.pdf-1591-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R EIF_1<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R EIF_1<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|External Wakeup/Interrupt Status Flag x|
|EIF_1|This flag can be cleared only by writing 1. Writing 0 has no effect. If enabled (IRER[x]), EIF[x] causes an<br>interrupt request.|
||0b - No event has occurred on the pad|
||1b - An event as defined by WIREER and WIFEER has occurred|



#### 46.7.1.11 Interrupt Request Enable Register (IRER_64) 

##### Offset 

|Register|Offset|
|---|---|
|IRER_64|58h|



##### Function 

This register is used to enable interrupt messaging from the wakeup/interrupt pads to the interrupt controller. 

~~<mark>NOTE</mark>~~ This register is accessible only by 32-bit read/write operations. 

Access: User read/write 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1591 / 4640 

NXP Semiconductors 

Wakeup Unit (WKPU) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/046_Wakeup_Unit_-WKPU-/S32K3XXRM_数据表.pdf-1592-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>EIRE_1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>EIRE_1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|External Interrupt Request Enable x|
|EIRE_1|0b - Interrupt requests from the corresponding EIF[x] bit are disabled|
||1b - A set EIF[x] bit causes an interrupt request|



#### 46.7.1.12 Wakeup Request Enable Register (WRER_64) 

##### Offset 

|Register|Offset|
|---|---|
|WRER_64|5Ch|



##### Function 

This register is used to enable system wakeup messaging from the wakeup/interrupt pads to the mode entry and power control modules. 

~~<mark>NOTE</mark>~~ 

This register is accessible only by 32-bit read/write operations. 

If a pin is disabled through this register, the corresponding bits in the WIFEER and WIREER registers must be written to 0 to ensure that the pin does not respond to any change. 

Access: User read/write 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1592 / 4640 

NXP Semiconductors 

Wakeup Unit (WKPU) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/046_Wakeup_Unit_-WKPU-/S32K3XXRM_数据表.pdf-1593-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>WRE_1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>WRE_1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|External Wakeup Request Enable x|
|WRE_1|0b - System wakeup requests from corresponding EIF[x] bit are disabled|
||1b - A set EIF[x] bit causes a system wakeup request|



#### 46.7.1.13 Wakeup/Interrupt Rising-Edge Event Enable Register (WIREER_64) 

##### Offset 

|Register|Offset|
|---|---|
|WIREER_64|68h|



##### Function 

This register is used to enable rising-edge triggered events on the corresponding wakeup/interrupt pads. 

|~~NOTE~~|
|---|
|This register is accessible only by 32-bit read/write operations.|



Access: User read/write 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1593 / 4640 

NXP Semiconductors 

Wakeup Unit (WKPU) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/046_Wakeup_Unit_-WKPU-/S32K3XXRM_数据表.pdf-1594-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>IREE_1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>IREE_1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|External Interrupt Rising-edge Events Enable x|
|IREE_1|0b - Rising-edge event is disabled|
||1b - Rising-edge event is enabled|



#### 46.7.1.14 Wakeup/Interrupt Falling-Edge Event Enable Register (WIFEER_64) 

##### Offset 

|Register|Offset|
|---|---|
|WIFEER_64|6Ch|



##### Function 

This register is used to enable falling-edge triggered events on the corresponding wakeup/interrupt pads. 

~~<mark>NOTE</mark>~~ This register is accessible only by 32-bit read/write operations. 

Access: User read/write 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1594 / 4640 

NXP Semiconductors 

Wakeup Unit (WKPU) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/046_Wakeup_Unit_-WKPU-/S32K3XXRM_数据表.pdf-1595-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>IFEEx_1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>IFEEx_1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|External Interrupt Falling-edge Events Enable x|
|IFEEx_1|0b - Falling-edge event is disabled|
||1b - Falling-edge event is enabled|



#### 46.7.1.15 Wakeup/Interrupt Filter Enable Register (WIFER_64) 

##### Offset 

|Register|Offset|
|---|---|
|WIFER_64|70h|



##### Function 

This register is used to enable an analog filter on the corresponding interrupt pads to filter out glitches on the inputs. 

~~<mark>NOTE</mark>~~ This register is accessible only by 32-bit read/write operations. 

Access: User read/write 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1595 / 4640 

NXP Semiconductors 

Wakeup Unit (WKPU) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/046_Wakeup_Unit_-WKPU-/S32K3XXRM_数据表.pdf-1596-02.png)


<!-- Start of picture text -->
Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>IFE_1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>IFE_1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|External Interrupt Filter Enable x|
|IFE_1|Enable analog glitch filter on the external interrupt pad input.|
||0b - Filter is disabled|
||1b - Filter is enabled|



## 46.8 Glossary 

NMI Non-maskable interrupts 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1596 / 4640 

