NXP Semiconductors 

# Chapter 9 System Integration Unit Lite2 (SIUL2) 

## 9.1 Chip-specific SIUL2 information 

### 9.1.1 Feature availability 

This chip: 

- Supports input filter enable (MSCR5[IFE]) only for the reset pad (PTA5). For details, see the "Pad signal description" table in the "Signal Multiplexing" chapter. 

- Does not implement the open-drain feature. LPI2C directly configures only the pads related to the I2C and LPUART functions in pseudo open-drain when these functions are muxed to the pads. See the LPI2C and LPUART chapters for more information. 

- Reserves GPDO[25:24] and PGPDO1[7:6] because PTA24 and PTA25 are input-only pins. 

~~<mark>NOTE</mark>~~ 

EIRQ[0-15] can be used either for interrupt or DMA request. EIRQ[16-31] can only be used for interrupt request. 

### 9.1.2 Mapping of MSCR and IMCR instances 

- CR numbers 0-511 correspond to the MSCR instances. 

- CR numbers 512-1023 correspond to the IMCR instances. IMCRs defined in the attached IOMUX file have an offset of 512 with respect to the IMCR number defined in SIUL2 memory map section. 

~~<mark>NOTE</mark>~~ 

IMCR register only supports 32 bit access, any other access might result in unexpected data. See IOMUX file attached to this document for the reset value and exact number of IMCR and MSCR register instances. 

## 9.2 Introduction 

### 9.2.1 Overview 

SIUL2 provides control over all electrical pin controls and ports with 16 bits of bidirectional, general-purpose input and output signals. SIUL2 enables you to select the functions and electrical characteristics that appear on external chip pins. It also controls the multiplexing of internal signals from one module to another and controls chip I/O. It supports as many as 32 external interrupts with trigger event configuration. 

The block diagram shows the functional blocks of the module and its interfaces to other system components. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

215 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/009_System_Integration_Unit_Lite2_-SIUL2-/S32K3XXRM_数据表.pdf-0216-02.png)


<!-- Start of picture text -->
SIUL2 Module<br>IP Modules<br>Pad Control and Pin Muxing<br>MSCR<br>Registers<br>GPIO<br>IO PADS<br>MUX<br>Data Registers<br>Peripheral<br>Master<br>Interrupt/DMA Request<br>Interrupt<br>Controller<br>Interrupt<br>- Configuration<br>- Glitch Filter<br>DMA<br>MCU Specific (UDR) Registers<br>Misc.<br>Registers<br>Logic<br>Figure 16. SIUL2 block diagram<br>Peripheral Bus<br><!-- End of picture text -->

SIUL2 provides dedicated pad control to general-purpose pads that can be configured as either inputs or outputs. It provides registers for you to read values from GPIO pads configured as inputs and to write values to GPIO pads configured as outputs: 

- When configured as output, you can write to an internal register to control the state driven on the associated output pad. 

- When configured as input, you can detect the state of the associated pad by reading the value from an internal register. 

- When configured as input and output, the pad value can be read back to check if the written value appeared on the pad. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

216 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

You can access GPIO data registers in various ways to allow port access and bit manipulation without read-modifywrite operations: 

- Access to two 16-bit ports in one access 

- Read/write access to a single bit 

- A 16-bit port write with a bit mask using single 32-bit access 

You can configure external interrupt sources at the chip level to be used with any chip pad. You can configure interrupt sources to have a digital filter to reject short glitches on the inputs. The external interrupt/DMA requests map to the REQ pins in the chip packages. The User Defined Registers (UDRs) contain miscellaneous control and status bits. 

### 9.2.2 Features 

SIUL2 supports: 

- One to 32 GPIO ports with data control 

   - Drives data to as many as 16 independent I/O channels 

   - Samples data from as many as 16 independent I/O channels 

- Read or write of two 16-bit registers with one access for a 32-bit port 

- External interrupt/DMA requests: 

   - One to 32 programmable digital glitch filters, one for each interrupt REQ pin 

   - Edge detection 

- Multiplexed Signal Configuration Registers (MSCR) to configure the electrical parameters and settings for as many as 512 functional pads. 

See the interrupt map file and the DMAMUX map file attached to this document for mapping of interrupt and DMA sources to interrupt vectors and DMA channels. 

## 9.3 Functional description 

### 9.3.1 Pad Control 

SIUL2 can control the electrical characteristics of as many as 512 pads. It provides a consistent interface for all pads, both on a by-port and a by-bit basis. 

The setting of each pad out of reset is fixed per chip but can be configured individually. This way you can select special pull settings or peripheral pad ownership. 

You can configure each pad independently of all other pads on the chip or other pads grouped within a single port. Thus you can group different pad types together in ports and operate the pads individually. Grouping the various functions for each pad into a single register allows you to configure each pad with a single write to a register, which further allows you to duplicate software for similar pads with index changes. 

### 9.3.2 General Purpose Input and Output pads (GPIO) 

SIUL2 allows each pad to be configured as either of the following: 

- General Purpose Input or Output pad (GPIO) 

- A pad for one or more alternate functions (input or output) determined by the peripheral that uses the pad 

GPIO pads can also be implemented without any alternate function. 

SIUL2 can manage as many as 512 GPIO pads organized as ports that can be accessed for data reads and writes as 8-bit, 16-bit, or 32-bit. 

All port accesses are identical, with each read or write performed only at a different location to access a different port width: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

217 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/009_System_Integration_Unit_Lite2_-SIUL2-/S32K3XXRM_数据表.pdf-0218-01.png)


<!-- Start of picture text -->
System Integration Unit Lite2 (SIUL2)<br>31 23 15 7 0<br>Base+ 0x0000 32-bit Port<br>15 7 0 15 7 0<br>Base+ 16-bit Port Base+ 16-bit Port<br>0x0002 0x0000<br>7 0 7 0 7 0 7 0<br>Base+ Base+ Base+ Base+<br>8-bit Port 8-bit Port 8-bit Port 8-bit Port<br>0x0003 0x0002 0x0001 0x0000<br>Figure 17. Data Port example arrangement showing configuration for different port width accesses<br><!-- End of picture text -->

SIUL2 has separate data input and data output registers for all pads. You can thus directly read back an input or output value of a pad to validate what is actually present on the pad instead of confirming the value that was written to the data input registers. 

- The data output registers support both read and write operations. 

- The data input registers support read access only. 

When a pad is configured to use one of its alternate functions, the data input values reflect the respective value of the pad. If a write operation is performed to the data output register for a pad configured as an alternate function (non-GPIO), this write will not be reflected by the pad value until re-configured to GPIO. All general purpose pads are implemented as bidirectional. 

If bidirectional operation impacts performance or is not required for a pad function, you can limit the functionality of the pad to input only. 

### 9.3.3 External interrupts/DMA requests (REQ Pins) 

SIUL2 supports one to 32 external interrupts allocated to pads by the chip. 

See the interrupt map file and the DMAMUX map file attached to this document for mapping of interrupt and DMA sources to interrupt vectors and DMA channels. 

SIUL2 supports one to four interrupt vectors to the interrupt controller of the chip. Each interrupt vector can support as many as eight external interrupt sources from the chip pads. 

All the external interrupt pads within a single group have equal priority. You are responsible for searching through the group of sources in the appropriate way for the application. 

~~<mark>NOTE</mark>~~ 

Glitch filters applied to external interrupts require a running internal oscillator clock. If such a clock is not available, enabling the glitch filter on an external interrupt will disable the interrupt. 

The external interrupt signals from a pad have internal synchronizers. Therefore, the width of the interrupt signals should be at least 2.5/3 times the IRC clock cycles to correctly capture the interrupts. 

#### 9.3.3.1 External interrupt initialization 

Follow these steps to enable external interrupts: 

~~<mark>NOTE</mark>~~ 

If you do not follow these steps you may get a false interrupt flag during interrupt initialization. 

1. Set the appropriate IFER[IFEn] fields to enable the glitch filter. 

2. Clear the DIRER0[EIREn] bits to mask interrupts. 

3. Set the appropriate IREER0[IREEn] bits and IFEER0[IFEEn] bits as needed to select the pin polarity. 

4. Configure the appropriate bits in the MSCR register instances for the external interrupt pin(s): 

   - a. Clear the OBE and ODE bits to disable output. 

   - b. Set the IBE bit to enable the input buffer of the pin. 

   - c. If you are using the internal pullup or pulldown, configure the appropriate PUE and PUS fields. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

218 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

~~<mark>NOTE</mark>~~ 

When you chose external interrupt inputs for for external interrupt pins, do not configure them as outputs (that is, MSCR[OBE] bits must not be to 0) because it can cause false interrupts detection (such as from a GPIO configuration). 

5. Write the appropriate DIRSR0[DIRSn] bits to select a request between DMA or interrupt. 

6. Select the desired glitch filter setup for the pins: 

   - a. Write the appropriate value to IFMCRn[MAXCNT] register for the respective external interrupt to the filter counter. 

   - b. Write the appropriate value to IFCPR[IFCP] to set the filter clock prescaler. 

   - c. Set the appropriate IFER0[IFEn] bits to enable the glitch filter for the external interrupt pins. 

7. Write to the appropriate DISR0[EIFn] bits to clear any flags. 

8. Set the appropriate DIRER0[EIREn] bits to enable the interrupt pins. 

#### 9.3.3.2 External interrupt management 

You can enable or disable each interrupt independently using a single rolled up register, DIRER0. 

You can configure a pad defined as an external interrupt to recognize interrupts with an active rising edge, an active falling edge, or both, using the IREER and IFEER registers. 

~~<mark>NOTE</mark>~~ 

You must not disable both edge events of a given interrupt. 

Each external interrupt has an individual flag, held in the DISR0 register. DISR0 is a clear-by-write-1 register, which prevents inadvertent overwriting of other flags in the same register. 

This figure provides an overview of the external interrupt implementation: 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/009_System_Integration_Unit_Lite2_-SIUL2-/S32K3XXRM_数据表.pdf-0219-18.png)


<!-- Start of picture text -->
Int<br>Vectors<br>IRQ_31_24 IRQ_23_16 IRQ_15_08 IRQ_07_00<br>OR OR OR OR<br>Interrupt enable EIRE[31:0]<br>Glitch filter Prescaler EIF[31:24] EIF[23:16] EIF[15:8] EIF[7:0]<br>Interrupt Edge Enable<br>IFCP[3:0]<br>Rising<br>Glitch filter Counter_n Edge Detection IREE[31:0]<br>MAXCOUNT[x]<br>Falling<br>IRQ Glitch Filter enable Glitch Filter IFEE[31:0]<br>IFE[31:0]<br>Pads<br>Interrupt Controller<br><!-- End of picture text -->

Figure 18. External interrupt pad diagram 

#### 9.3.3.3 External interrupt request 

The REQ input pins on the chip are sources for interrupt or DMA requests. The chip provides four possible interrupt vectors for the SIUL2. The 32 interrupt request sources map to vectors and channels as follows: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

219 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table 35. Interrupt source mapping to SIUL2 interrupt request output for 32 interrupt sources 

|Vector/Channel #<br>I|nterrupt vector source|
|---|---|
|0<br>REQ[07] | REQ[06] | REQ[05]|| REQ[04] | REQ[03] | REQ[02] | REQ[01] | REQ[00]|
|1<br>REQ[15] | REQ[14] | REQ[13]|| REQ[12] | REQ[11] | REQ[10] | REQ[09] | REQ[08]|
|2<br>REQ[23] | REQ[22] | REQ[21]|| REQ[20] | REQ[19] | REQ[18] | REQ[17] | REQ[16]|
|3<br>REQ[31] | REQ[30] | REQ[29]|| REQ[28] | REQ[27] | REQ[26] | REQ[25] | REQ[24]|



#### 9.3.3.4 DMA requests 

The REQ pins on the chip map to independent DMA request channels in the DMA controller. 

## 9.4 SIUL2 register descriptions 

This section describes the SIUL2 registers. 

###### ~~<mark>NOTE</mark>~~ 

- Undocumented register spaces in the SIUL2 memory map, including addresses shown as blanks, are Reserved. 

   - Reserved registers or spaces are read as 0. 

   - Writes to Reserved registers or spaces generate a transfer error. 

- Writes to read-only registers generate a transfer error. 

###### ~~<mark>NOTE</mark>~~ 

- For the array of 8-bit registers GPDOn and GPDIn: 

   - An 8-bit access to an unimplemented address (a "hole") within the array region will generate a transfer error. 

   - However, if you do a 16-bit or a 32-bit access and if any register instance is implemented within the accessed range, a transfer error will not be generated even if the range includes a hole. 

- For the array of 16-bit registers PGPDOn and PGPDIn: 

   - A 16-bit access to an unimplemented address (a "hole") within the array region will generate a transfer error. 

   - However, a 32-bit access does not generate a transfer error for a hole irrespective of whether or not the other 16-bit range includes a register instance. 

### 9.4.1 SIUL2 memory map 

SIUL2 base address: 4029_0000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|4h|SIUL2 MCU ID Register #1 (MIDR1)|32|RO|See<br>description|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

220 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|8h|SIUL2 MCU ID Register #2 (MIDR2)|32|RO|See<br>description|
|10h|SIUL2 DMA/Interrupt Status Flag Register0 (DISR0)|32|W1C|0000_0000h|
|18h|SIUL2 DMA/Interrupt Request Enable Register0 (DIRER0)|32|RW|0000_0000h|
|20h|SIUL2 DMA/Interrupt Request Select Register0 (DIRSR0)|32|RW|0000_0000h|
|28h|SIUL2 Interrupt Rising-Edge Event Enable Register 0 (IREER0)|32|RW|0000_0000h|
|30h|SIUL2 Interrupt Falling-Edge Event Enable Register 0 (IFEER0)|32|RW|0000_0000h|
|38h|SIUL2 Interrupt Filter Enable Register 0 (IFER0)|32|RW|0000_0000h|
|40h - BCh|SIUL2 Interrupt Filter Maximum Counter Register (IFMCR0 -<br>IFMCR31)|32|RW|0000_0000h|
|C0h|SIUL2 Interrupt Filter Clock Prescaler Register (IFCPR)|32|RW|0000_0000h|
|100h|MUX0 EMIOS ENABLE 1 (MUX0_EMIOS_EN1)|32|RW|See<br>description|
|104h|MUX0 MISC ENABLE (MUX0_MISC_EN)|32|RW|See<br>description|
|108h|MUX1 EMIOS ENABLE (MUX1_EMIOS_EN )|32|RW|See<br>description|
|10Ch|MUX1 MISC ENABLE (MUX1_MISC_EN)|32|RW|See<br>description|
|110h|MUX2 EMIOS ENABLE (MUX2_EMIOS_EN)|32|RW|See<br>description|
|114h|MUX2 MISC ENABLE (MUX2_MISC_EN)|32|RW|See<br>description|
|200h|SIUL2 MCU ID Register #3 (MIDR3)|32|RO|See<br>description|
|204h|SIUL2 MCU ID Register #4 (MIDR4)|32|RO|See<br>description|
|240h|SIUL2 Multiplexed Signal Configuration Register (MSCR0)|32|RW|0000_0000h|
|244h|SIUL2 Multiplexed Signal Configuration Register (MSCR1)|32|RW|0000_0000h|
|248h|SIUL2 Multiplexed Signal Configuration Register (MSCR2)|32|RW|0000_0000h|
|24Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR3)|32|RW|0000_0000h|
|250h|SIUL2 Multiplexed Signal Configuration Register (MSCR4)|32|RW|0008_2827h|
|254h|SIUL2 Multiplexed Signal Configuration Register (MSCR5)|32|RW|0000_0000h|
|258h|SIUL2 Multiplexed Signal Configuration Register (MSCR6)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

221 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|25Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR7)|32|RW|0000_0000h|
|260h|SIUL2 Multiplexed Signal Configuration Register (MSCR8)|32|RW|0000_0000h|
|264h|SIUL2 Multiplexed Signal Configuration Register (MSCR9)|32|RW|0000_0000h|
|268h|SIUL2 Multiplexed Signal Configuration Register (MSCR10)|32|RW|0000_0127h|
|26Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR11)|32|RW|0000_0000h|
|270h|SIUL2 Multiplexed Signal Configuration Register (MSCR12)|32|RW|0000_0003h|
|274h|SIUL2 Multiplexed Signal Configuration Register (MSCR13)|32|RW|0000_0000h|
|278h|SIUL2 Multiplexed Signal Configuration Register (MSCR14)|32|RW|0000_0000h|
|27Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR15)|32|RW|0000_0000h|
|280h|SIUL2 Multiplexed Signal Configuration Register (MSCR16)|32|RW|0000_0000h|
|284h|SIUL2 Multiplexed Signal Configuration Register (MSCR17)|32|RW|0000_0000h|
|288h|SIUL2 Multiplexed Signal Configuration Register (MSCR18)|32|RW|0000_0000h|
|28Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR19)|32|RW|0000_0000h|
|290h|SIUL2 Multiplexed Signal Configuration Register (MSCR20)|32|RW|0000_0000h|
|294h|SIUL2 Multiplexed Signal Configuration Register (MSCR21)|32|RW|0000_0000h|
|298h|SIUL2 Multiplexed Signal Configuration Register (MSCR22)|32|RW|0000_0000h|
|29Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR23)|32|RW|0000_0000h|
|2A0h|SIUL2 Multiplexed Signal Configuration Register (MSCR24)|32|RW|0000_0000h|
|2A4h|SIUL2 Multiplexed Signal Configuration Register (MSCR25)|32|RW|0000_0000h|
|2A8h|SIUL2 Multiplexed Signal Configuration Register (MSCR26)|32|RW|0000_0000h|
|2ACh|SIUL2 Multiplexed Signal Configuration Register (MSCR27)|32|RW|0000_0000h|
|2B0h|SIUL2 Multiplexed Signal Configuration Register (MSCR28)|32|RW|0000_0000h|
|2B4h|SIUL2 Multiplexed Signal Configuration Register (MSCR29)|32|RW|0000_0000h|
|2B8h|SIUL2 Multiplexed Signal Configuration Register (MSCR30)|32|RW|0000_0000h|
|2BCh|SIUL2 Multiplexed Signal Configuration Register (MSCR31)|32|RW|0000_0000h|
|2C0h|SIUL2 Multiplexed Signal Configuration Register (MSCR32)|32|RW|0000_0000h|
|2C4h|SIUL2 Multiplexed Signal Configuration Register (MSCR33)|32|RW|0000_0000h|
|2C8h|SIUL2 Multiplexed Signal Configuration Register (MSCR34)|32|RW|0000_0000h|
|2CCh|SIUL2 Multiplexed Signal Configuration Register (MSCR35)|32|RW|0000_0000h|
|2D0h|SIUL2 Multiplexed Signal Configuration Register (MSCR36)|32|RW|0000_0000h|
|2D4h|SIUL2 Multiplexed Signal Configuration Register (MSCR37)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

222 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|2E0h|SIUL2 Multiplexed Signal Configuration Register (MSCR40)|32|RW|0000_0000h|
|2E4h|SIUL2 Multiplexed Signal Configuration Register (MSCR41)|32|RW|0000_0000h|
|2E8h|SIUL2 Multiplexed Signal Configuration Register (MSCR42)|32|RW|0000_0000h|
|2ECh|SIUL2 Multiplexed Signal Configuration Register (MSCR43)|32|RW|0000_0000h|
|2F0h|SIUL2 Multiplexed Signal Configuration Register (MSCR44)|32|RW|0000_0000h|
|2F4h|SIUL2 Multiplexed Signal Configuration Register (MSCR45)|32|RW|0000_0000h|
|2F8h|SIUL2 Multiplexed Signal Configuration Register (MSCR46)|32|RW|0000_0000h|
|2FCh|SIUL2 Multiplexed Signal Configuration Register (MSCR47)|32|RW|0000_0000h|
|300h|SIUL2 Multiplexed Signal Configuration Register (MSCR48)|32|RW|0000_0000h|
|304h|SIUL2 Multiplexed Signal Configuration Register (MSCR49)|32|RW|0000_0000h|
|308h|SIUL2 Multiplexed Signal Configuration Register (MSCR50)|32|RW|0000_0000h|
|30Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR51)|32|RW|0000_0000h|
|310h|SIUL2 Multiplexed Signal Configuration Register (MSCR52)|32|RW|0000_0000h|
|314h|SIUL2 Multiplexed Signal Configuration Register (MSCR53)|32|RW|0000_0000h|
|318h|SIUL2 Multiplexed Signal Configuration Register (MSCR54)|32|RW|0000_0000h|
|31Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR55)|32|RW|0000_0000h|
|320h|SIUL2 Multiplexed Signal Configuration Register (MSCR56)|32|RW|0000_0000h|
|324h|SIUL2 Multiplexed Signal Configuration Register (MSCR57)|32|RW|0000_0000h|
|328h|SIUL2 Multiplexed Signal Configuration Register (MSCR58)|32|RW|0000_0000h|
|32Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR59)|32|RW|0000_0000h|
|330h|SIUL2 Multiplexed Signal Configuration Register (MSCR60)|32|RW|0000_0000h|
|334h|SIUL2 Multiplexed Signal Configuration Register (MSCR61)|32|RW|0000_0000h|
|338h|SIUL2 Multiplexed Signal Configuration Register (MSCR62)|32|RW|0000_0000h|
|33Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR63)|32|RW|0000_0000h|
|340h|SIUL2 Multiplexed Signal Configuration Register (MSCR64)|32|RW|0000_0000h|
|344h|SIUL2 Multiplexed Signal Configuration Register (MSCR65)|32|RW|0000_0000h|
|348h|SIUL2 Multiplexed Signal Configuration Register (MSCR66)|32|RW|0000_4000h|
|34Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR67)|32|RW|0000_4000h|
|350h|SIUL2 Multiplexed Signal Configuration Register (MSCR68)|32|RW|0008_2000h|
|354h|SIUL2 Multiplexed Signal Configuration Register (MSCR69)|32|RW|0008_2800h|
|358h|SIUL2 Multiplexed Signal Configuration Register (MSCR70)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

223 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|35Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR71)|32|RW|0000_0000h|
|360h|SIUL2 Multiplexed Signal Configuration Register (MSCR72)|32|RW|0000_0000h|
|364h|SIUL2 Multiplexed Signal Configuration Register (MSCR73)|32|RW|0000_0000h|
|368h|SIUL2 Multiplexed Signal Configuration Register (MSCR74)|32|RW|0000_0000h|
|36Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR75)|32|RW|0000_0000h|
|370h|SIUL2 Multiplexed Signal Configuration Register (MSCR76)|32|RW|0000_4000h|
|374h|SIUL2 Multiplexed Signal Configuration Register (MSCR77)|32|RW|0000_0000h|
|378h|SIUL2 Multiplexed Signal Configuration Register (MSCR78)|32|RW|0000_0000h|
|37Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR79)|32|RW|0000_0000h|
|380h|SIUL2 Multiplexed Signal Configuration Register (MSCR80)|32|RW|0000_4000h|
|384h|SIUL2 Multiplexed Signal Configuration Register (MSCR81)|32|RW|0000_0000h|
|388h|SIUL2 Multiplexed Signal Configuration Register (MSCR82)|32|RW|0000_0000h|
|38Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR83)|32|RW|0000_0000h|
|390h|SIUL2 Multiplexed Signal Configuration Register (MSCR84)|32|RW|0000_0000h|
|394h|SIUL2 Multiplexed Signal Configuration Register (MSCR85)|32|RW|0000_0000h|
|398h|SIUL2 Multiplexed Signal Configuration Register (MSCR86)|32|RW|0000_0000h|
|39Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR87)|32|RW|0000_0000h|
|3A0h|SIUL2 Multiplexed Signal Configuration Register (MSCR88)|32|RW|0000_0000h|
|3A4h|SIUL2 Multiplexed Signal Configuration Register (MSCR89)|32|RW|0000_0000h|
|3A8h|SIUL2 Multiplexed Signal Configuration Register (MSCR90)|32|RW|0000_0000h|
|3ACh|SIUL2 Multiplexed Signal Configuration Register (MSCR91)|32|RW|0000_0000h|
|3B0h|SIUL2 Multiplexed Signal Configuration Register (MSCR92)|32|RW|0000_0000h|
|3B4h|SIUL2 Multiplexed Signal Configuration Register (MSCR93)|32|RW|0000_0000h|
|3B8h|SIUL2 Multiplexed Signal Configuration Register (MSCR94)|32|RW|0000_0000h|
|3BCh|SIUL2 Multiplexed Signal Configuration Register (MSCR95)|32|RW|0000_0000h|
|3C0h|SIUL2 Multiplexed Signal Configuration Register (MSCR96)|32|RW|0000_0000h|
|3C4h|SIUL2 Multiplexed Signal Configuration Register (MSCR97)|32|RW|0000_0000h|
|3C8h|SIUL2 Multiplexed Signal Configuration Register (MSCR98)|32|RW|0000_0000h|
|3CCh|SIUL2 Multiplexed Signal Configuration Register (MSCR99)|32|RW|0000_0000h|
|3D0h|SIUL2 Multiplexed Signal Configuration Register (MSCR100)|32|RW|0000_0000h|
|3D4h|SIUL2 Multiplexed Signal Configuration Register (MSCR101)|32|RW|0000_4000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

224 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|3D8h|SIUL2 Multiplexed Signal Configuration Register (MSCR102)|32|RW|0000_4000h|
|3DCh|SIUL2 Multiplexed Signal Configuration Register (MSCR103)|32|RW|0000_4000h|
|3E0h|SIUL2 Multiplexed Signal Configuration Register (MSCR104)|32|RW|0000_0000h|
|3E4h|SIUL2 Multiplexed Signal Configuration Register (MSCR105)|32|RW|0000_0000h|
|3E8h|SIUL2 Multiplexed Signal Configuration Register (MSCR106)|32|RW|0000_4000h|
|3ECh|SIUL2 Multiplexed Signal Configuration Register (MSCR107)|32|RW|0000_4000h|
|3F0h|SIUL2 Multiplexed Signal Configuration Register (MSCR108)|32|RW|0000_4000h|
|3F4h|SIUL2 Multiplexed Signal Configuration Register (MSCR109)|32|RW|0000_0000h|
|3F8h|SIUL2 Multiplexed Signal Configuration Register (MSCR110)|32|RW|0000_0000h|
|3FCh|SIUL2 Multiplexed Signal Configuration Register (MSCR111)|32|RW|0000_0000h|
|400h|SIUL2 Multiplexed Signal Configuration Register (MSCR112)|32|RW|0000_0000h|
|404h|SIUL2 Multiplexed Signal Configuration Register (MSCR113)|32|RW|0000_0000h|
|408h|SIUL2 Multiplexed Signal Configuration Register (MSCR114)|32|RW|0000_0000h|
|40Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR115)|32|RW|0000_0000h|
|410h|SIUL2 Multiplexed Signal Configuration Register (MSCR116)|32|RW|0000_0000h|
|414h|SIUL2 Multiplexed Signal Configuration Register (MSCR117)|32|RW|0000_0000h|
|418h|SIUL2 Multiplexed Signal Configuration Register (MSCR118)|32|RW|0000_0000h|
|41Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR119)|32|RW|0000_0000h|
|420h|SIUL2 Multiplexed Signal Configuration Register (MSCR120)|32|RW|0000_0000h|
|424h|SIUL2 Multiplexed Signal Configuration Register (MSCR121)|32|RW|0000_0000h|
|428h|SIUL2 Multiplexed Signal Configuration Register (MSCR122)|32|RW|0000_0000h|
|42Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR123)|32|RW|0000_0000h|
|430h|SIUL2 Multiplexed Signal Configuration Register (MSCR124)|32|RW|0000_0000h|
|434h|SIUL2 Multiplexed Signal Configuration Register (MSCR125)|32|RW|0000_0000h|
|438h|SIUL2 Multiplexed Signal Configuration Register (MSCR126)|32|RW|0000_0000h|
|43Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR127)|32|RW|0000_0000h|
|440h|SIUL2 Multiplexed Signal Configuration Register (MSCR128)|32|RW|0000_0000h|
|444h|SIUL2 Multiplexed Signal Configuration Register (MSCR129)|32|RW|0000_0000h|
|448h|SIUL2 Multiplexed Signal Configuration Register (MSCR130)|32|RW|0000_0000h|
|44Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR131)|32|RW|0000_0000h|
|450h|SIUL2 Multiplexed Signal Configuration Register (MSCR132)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

225 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|454h|SIUL2 Multiplexed Signal Configuration Register (MSCR133)|32|RW|0000_0000h|
|458h|SIUL2 Multiplexed Signal Configuration Register (MSCR134)|32|RW|0000_0000h|
|45Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR135)|32|RW|0000_0000h|
|460h|SIUL2 Multiplexed Signal Configuration Register (MSCR136)|32|RW|0000_4000h|
|464h|SIUL2 Multiplexed Signal Configuration Register (MSCR137)|32|RW|0000_0000h|
|468h|SIUL2 Multiplexed Signal Configuration Register (MSCR138)|32|RW|0000_0000h|
|46Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR139)|32|RW|0000_0000h|
|470h|SIUL2 Multiplexed Signal Configuration Register (MSCR140)|32|RW|0000_0000h|
|474h|SIUL2 Multiplexed Signal Configuration Register (MSCR141)|32|RW|0000_0000h|
|478h|SIUL2 Multiplexed Signal Configuration Register (MSCR142)|32|RW|0000_0000h|
|47Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR143)|32|RW|0000_0000h|
|480h|SIUL2 Multiplexed Signal Configuration Register (MSCR144)|32|RW|0000_0000h|
|484h|SIUL2 Multiplexed Signal Configuration Register (MSCR145)|32|RW|0000_0000h|
|488h|SIUL2 Multiplexed Signal Configuration Register (MSCR146)|32|RW|0000_0000h|
|48Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR147)|32|RW|0000_0000h|
|490h|SIUL2 Multiplexed Signal Configuration Register (MSCR148)|32|RW|0000_0000h|
|494h|SIUL2 Multiplexed Signal Configuration Register (MSCR149)|32|RW|0000_0000h|
|498h|SIUL2 Multiplexed Signal Configuration Register (MSCR150)|32|RW|0000_0000h|
|49Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR151)|32|RW|0000_0000h|
|4A0h|SIUL2 Multiplexed Signal Configuration Register (MSCR152)|32|RW|0000_0000h|
|4A4h|SIUL2 Multiplexed Signal Configuration Register (MSCR153)|32|RW|0000_0000h|
|4A8h|SIUL2 Multiplexed Signal Configuration Register (MSCR154)|32|RW|0000_0000h|
|4ACh|SIUL2 Multiplexed Signal Configuration Register (MSCR155)|32|RW|0000_0000h|
|4B0h|SIUL2 Multiplexed Signal Configuration Register (MSCR156)|32|RW|0000_0000h|
|4B4h|SIUL2 Multiplexed Signal Configuration Register (MSCR157)|32|RW|0000_0000h|
|4B8h|SIUL2 Multiplexed Signal Configuration Register (MSCR158)|32|RW|0000_0000h|
|4BCh|SIUL2 Multiplexed Signal Configuration Register (MSCR159)|32|RW|0000_0000h|
|4C0h|SIUL2 Multiplexed Signal Configuration Register (MSCR160)|32|RW|0000_0000h|
|4C4h|SIUL2 Multiplexed Signal Configuration Register (MSCR161)|32|RW|0000_0000h|
|4C8h|SIUL2 Multiplexed Signal Configuration Register (MSCR162)|32|RW|0000_0000h|
|4CCh|SIUL2 Multiplexed Signal Configuration Register (MSCR163)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

226 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|4D0h|SIUL2 Multiplexed Signal Configuration Register (MSCR164)|32|RW|0000_0000h|
|4D4h|SIUL2 Multiplexed Signal Configuration Register (MSCR165)|32|RW|0000_0000h|
|4D8h|SIUL2 Multiplexed Signal Configuration Register (MSCR166)|32|RW|0000_0000h|
|4DCh|SIUL2 Multiplexed Signal Configuration Register (MSCR167)|32|RW|0000_0000h|
|4E0h|SIUL2 Multiplexed Signal Configuration Register (MSCR168)|32|RW|0000_0000h|
|4E4h|SIUL2 Multiplexed Signal Configuration Register (MSCR169)|32|RW|0000_0000h|
|4E8h|SIUL2 Multiplexed Signal Configuration Register (MSCR170)|32|RW|0000_0000h|
|4ECh|SIUL2 Multiplexed Signal Configuration Register (MSCR171)|32|RW|0000_0000h|
|4F0h|SIUL2 Multiplexed Signal Configuration Register (MSCR172)|32|RW|0000_0000h|
|4F4h|SIUL2 Multiplexed Signal Configuration Register (MSCR173)|32|RW|0000_0000h|
|4F8h|SIUL2 Multiplexed Signal Configuration Register (MSCR174)|32|RW|0000_0000h|
|4FCh|SIUL2 Multiplexed Signal Configuration Register (MSCR175)|32|RW|0000_0000h|
|500h|SIUL2 Multiplexed Signal Configuration Register (MSCR176)|32|RW|0000_0000h|
|504h|SIUL2 Multiplexed Signal Configuration Register (MSCR177)|32|RW|0000_0000h|
|508h|SIUL2 Multiplexed Signal Configuration Register (MSCR178)|32|RW|0000_0000h|
|50Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR179)|32|RW|0000_0000h|
|510h|SIUL2 Multiplexed Signal Configuration Register (MSCR180)|32|RW|0000_0000h|
|514h|SIUL2 Multiplexed Signal Configuration Register (MSCR181)|32|RW|0000_0000h|
|518h|SIUL2 Multiplexed Signal Configuration Register (MSCR182)|32|RW|0000_0000h|
|51Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR183)|32|RW|0000_0000h|
|520h|SIUL2 Multiplexed Signal Configuration Register (MSCR184)|32|RW|0000_0000h|
|524h|SIUL2 Multiplexed Signal Configuration Register (MSCR185)|32|RW|0000_0000h|
|528h|SIUL2 Multiplexed Signal Configuration Register (MSCR186)|32|RW|0000_0000h|
|52Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR187)|32|RW|0000_0000h|
|530h|SIUL2 Multiplexed Signal Configuration Register (MSCR188)|32|RW|0000_0000h|
|534h|SIUL2 Multiplexed Signal Configuration Register (MSCR189)|32|RW|0000_0000h|
|538h|SIUL2 Multiplexed Signal Configuration Register (MSCR190)|32|RW|0000_0000h|
|53Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR191)|32|RW|0000_0000h|
|540h|SIUL2 Multiplexed Signal Configuration Register (MSCR192)|32|RW|0000_0000h|
|544h|SIUL2 Multiplexed Signal Configuration Register (MSCR193)|32|RW|0000_0000h|
|548h|SIUL2 Multiplexed Signal Configuration Register (MSCR194)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

227 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|54Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR195)|32|RW|0000_0000h|
|550h|SIUL2 Multiplexed Signal Configuration Register (MSCR196)|32|RW|0000_0000h|
|554h|SIUL2 Multiplexed Signal Configuration Register (MSCR197)|32|RW|0000_0000h|
|558h|SIUL2 Multiplexed Signal Configuration Register (MSCR198)|32|RW|0000_0000h|
|55Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR199)|32|RW|0000_0000h|
|560h|SIUL2 Multiplexed Signal Configuration Register (MSCR200)|32|RW|0000_0000h|
|564h|SIUL2 Multiplexed Signal Configuration Register (MSCR201)|32|RW|0000_0000h|
|568h|SIUL2 Multiplexed Signal Configuration Register (MSCR202)|32|RW|0000_0000h|
|56Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR203)|32|RW|0000_0000h|
|570h|SIUL2 Multiplexed Signal Configuration Register (MSCR204)|32|RW|0000_0000h|
|574h|SIUL2 Multiplexed Signal Configuration Register (MSCR205)|32|RW|0000_0000h|
|578h|SIUL2 Multiplexed Signal Configuration Register (MSCR206)|32|RW|0000_0000h|
|57Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR207)|32|RW|0000_0000h|
|580h|SIUL2 Multiplexed Signal Configuration Register (MSCR208)|32|RW|0000_0000h|
|584h|SIUL2 Multiplexed Signal Configuration Register (MSCR209)|32|RW|0000_0000h|
|588h|SIUL2 Multiplexed Signal Configuration Register (MSCR210)|32|RW|0000_0000h|
|58Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR211)|32|RW|0000_0000h|
|590h|SIUL2 Multiplexed Signal Configuration Register (MSCR212)|32|RW|0000_0000h|
|594h|SIUL2 Multiplexed Signal Configuration Register (MSCR213)|32|RW|0000_0000h|
|598h|SIUL2 Multiplexed Signal Configuration Register (MSCR214)|32|RW|0000_0000h|
|59Ch|SIUL2 Multiplexed Signal Configuration Register (MSCR215)|32|RW|0000_0000h|
|5A0h|SIUL2 Multiplexed Signal Configuration Register (MSCR216)|32|RW|0000_0000h|
|5A4h|SIUL2 Multiplexed Signal Configuration Register (MSCR217)|32|RW|0000_0000h|
|5A8h|SIUL2 Multiplexed Signal Configuration Register (MSCR218)|32|RW|0000_0000h|
|5ACh|SIUL2 Multiplexed Signal Configuration Register (MSCR219)|32|RW|0000_0000h|
|5B0h|SIUL2 Multiplexed Signal Configuration Register (MSCR220)|32|RW|0001_0000h|
|5B4h|SIUL2 Multiplexed Signal Configuration Register (MSCR221)|32|RW|0001_0000h|
|5B8h|SIUL2 Multiplexed Signal Configuration Register (MSCR222)|32|RW|0001_0000h|
|5BCh|SIUL2 Multiplexed Signal Configuration Register (MSCR223)|32|RW|0001_0000h|
|5C0h|SIUL2 Multiplexed Signal Configuration Register (MSCR224)|32|RW|0001_0000h|
|5C4h|SIUL2 Multiplexed Signal Configuration Register (MSCR225)|32|RW|0001_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

228 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|5C8h|SIUL2 Multiplexed Signal Configuration Register (MSCR226)|32|RW|0001_0000h|
|5CCh|SIUL2 Multiplexed Signal Configuration Register (MSCR227)|32|RW|0001_0000h|
|5D0h|SIUL2 Multiplexed Signal Configuration Register (MSCR228)|32|RW|0001_0000h|
|5D4h|SIUL2 Multiplexed Signal Configuration Register (MSCR229)|32|RW|0001_0000h|
|5D8h|SIUL2 Multiplexed Signal Configuration Register (MSCR230)|32|RW|0001_0000h|
|5DCh|SIUL2 Multiplexed Signal Configuration Register (MSCR231)|32|RW|0001_0000h|
|5E0h|SIUL2 Multiplexed Signal Configuration Register (MSCR232)|32|RW|0001_0000h|
|5E4h|SIUL2 Multiplexed Signal Configuration Register (MSCR233)|32|RW|0001_0000h|
|5E8h|SIUL2 Multiplexed Signal Configuration Register (MSCR234)|32|RW|0001_0000h|
|5ECh|SIUL2 Multiplexed Signal Configuration Register (MSCR235)|32|RW|0001_0000h|
|5F0h|SIUL2 Multiplexed Signal Configuration Register (MSCR236)|32|RW|0001_0000h|
|A40h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR0)|32|RW|0000_0000h|
|A44h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR1)|32|RW|0000_0000h|
|A48h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR2)|32|RW|0000_0000h|
|A4Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR3)|32|RW|0000_0000h|
|A50h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR4)|32|RW|0000_0000h|
|A54h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR5)|32|RW|0000_0000h|
|A80h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR16)|32|RW|0000_0000h|
|A84h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR17)|32|RW|0000_0000h|
|A88h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR18)|32|RW|0000_0000h|
|A8Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR19)|32|RW|0000_0000h|
|A90h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR20)|32|RW|0000_0000h|
|A94h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR21)|32|RW|0000_0000h|
|A98h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR22)|32|RW|0000_0000h|
|A9Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR23)|32|RW|0000_0000h|
|AA0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR24)|32|RW|0000_0000h|
|AA4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR25)|32|RW|0000_0000h|
|AA8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR26)|32|RW|0000_0000h|
|AACh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR27)|32|RW|0000_0000h|
|AB0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR28)|32|RW|0000_0000h|
|AB4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR29)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

229 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|AB8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR30)|32|RW|0000_0000h|
|ABCh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR31)|32|RW|0000_0000h|
|AC0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR32)|32|RW|0000_0000h|
|AC4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR33)|32|RW|0000_0000h|
|AC8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR34)|32|RW|0000_0000h|
|ACCh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR35)|32|RW|0000_0000h|
|AD0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR36)|32|RW|0000_0000h|
|AD4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR37)|32|RW|0000_0000h|
|AD8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR38)|32|RW|0000_0000h|
|ADCh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR39)|32|RW|0000_0000h|
|AE0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR40)|32|RW|0000_0000h|
|AE4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR41)|32|RW|0000_0000h|
|AE8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR42)|32|RW|0000_0000h|
|AECh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR43)|32|RW|0000_0000h|
|AF0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR44)|32|RW|0000_0000h|
|AF4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR45)|32|RW|0000_0000h|
|AF8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR46)|32|RW|0000_0000h|
|AFCh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR47)|32|RW|0000_0000h|
|B00h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR48)|32|RW|0000_0000h|
|B04h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR49)|32|RW|0000_0000h|
|B08h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR50)|32|RW|0000_0000h|
|B0Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR51)|32|RW|0000_0000h|
|B10h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR52)|32|RW|0000_0000h|
|B14h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR53)|32|RW|0000_0000h|
|B18h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR54)|32|RW|0000_0000h|
|B1Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR55)|32|RW|0000_0000h|
|B20h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR56)|32|RW|0000_0000h|
|B24h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR57)|32|RW|0000_0000h|
|B28h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR58)|32|RW|0000_0000h|
|B2Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR59)|32|RW|0000_0000h|
|B30h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR60)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

230 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|B34h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR61)|32|RW|0000_0000h|
|B38h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR62)|32|RW|0000_0000h|
|B3Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR63)|32|RW|0000_0000h|
|B40h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR64)|32|RW|0000_0000h|
|B44h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR65)|32|RW|0000_0000h|
|B48h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR66)|32|RW|0000_0000h|
|B4Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR67)|32|RW|0000_0000h|
|B50h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR68)|32|RW|0000_0000h|
|B54h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR69)|32|RW|0000_0000h|
|B58h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR70)|32|RW|0000_0000h|
|B5Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR71)|32|RW|0000_0000h|
|B80h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR80)|32|RW|0000_0000h|
|B84h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR81)|32|RW|0000_0000h|
|B88h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR82)|32|RW|0000_0000h|
|B8Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR83)|32|RW|0000_0000h|
|B90h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR84)|32|RW|0000_0000h|
|B94h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR85)|32|RW|0000_0000h|
|B98h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR86)|32|RW|0000_0000h|
|B9Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR87)|32|RW|0000_0000h|
|BA0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR88)|32|RW|0000_0000h|
|BA4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR89)|32|RW|0000_0000h|
|BA8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR90)|32|RW|0000_0000h|
|BACh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR91)|32|RW|0000_0000h|
|BB0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR92)|32|RW|0000_0000h|
|BB4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR93)|32|RW|0000_0000h|
|BB8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR94)|32|RW|0000_0000h|
|BBCh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR95)|32|RW|0000_0000h|
|BC0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR96)|32|RW|0000_0000h|
|BC4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR97)|32|RW|0000_0000h|
|BC8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR98)|32|RW|0000_0000h|
|BCCh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR99)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

231 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|BD0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR100)|32|RW|0000_0000h|
|BD4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR101)|32|RW|0000_0000h|
|BD8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR102)|32|RW|0000_0000h|
|BDCh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR103)|32|RW|0000_0000h|
|C00h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR112)|32|RW|0000_0000h|
|C04h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR113)|32|RW|0000_0000h|
|C08h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR114)|32|RW|0000_0000h|
|C0Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR115)|32|RW|0000_0000h|
|C10h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR116)|32|RW|0000_0000h|
|C14h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR117)|32|RW|0000_0000h|
|C18h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR118)|32|RW|0000_0000h|
|C1Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR119)|32|RW|0000_0000h|
|C20h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR120)|32|RW|0000_0000h|
|C24h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR121)|32|RW|0000_0000h|
|C28h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR122)|32|RW|0000_0000h|
|C2Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR123)|32|RW|0000_0000h|
|C30h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR124)|32|RW|0000_0000h|
|C34h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR125)|32|RW|0000_0000h|
|C38h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR126)|32|RW|0000_0000h|
|C3Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR127)|32|RW|0000_0000h|
|C40h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR128)|32|RW|0000_0000h|
|C44h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR129)|32|RW|0000_0000h|
|C48h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR130)|32|RW|0000_0000h|
|C4Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR131)|32|RW|0000_0000h|
|C50h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR132)|32|RW|0000_0000h|
|C54h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR133)|32|RW|0000_0000h|
|C58h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR134)|32|RW|0000_0000h|
|C5Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR135)|32|RW|0000_0000h|
|C80h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR144)|32|RW|0000_0000h|
|C84h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR145)|32|RW|0000_0000h|
|C88h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR146)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

232 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|C8Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR147)|32|RW|0000_0000h|
|C90h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR148)|32|RW|0000_0000h|
|C94h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR149)|32|RW|0000_0000h|
|CA0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR152)|32|RW|0000_0000h|
|CA4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR153)|32|RW|0000_0000h|
|CA8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR154)|32|RW|0000_0000h|
|CACh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR155)|32|RW|0000_0000h|
|CB0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR156)|32|RW|0000_0000h|
|CB4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR157)|32|RW|0000_0000h|
|CB8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR158)|32|RW|0000_0000h|
|CBCh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR159)|32|RW|0000_0000h|
|CC0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR160)|32|RW|0000_0000h|
|CC4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR161)|32|RW|0000_0000h|
|CC8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR162)|32|RW|0000_0000h|
|CCCh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR163)|32|RW|0000_0000h|
|CD0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR164)|32|RW|0000_0000h|
|CD4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR165)|32|RW|0000_0000h|
|CD8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR166)|32|RW|0000_0000h|
|CDCh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR167)|32|RW|0000_0000h|
|CE0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR168)|32|RW|0000_0000h|
|CE4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR169)|32|RW|0000_0000h|
|CE8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR170)|32|RW|0000_0000h|
|CECh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR171)|32|RW|0000_0000h|
|CF0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR172)|32|RW|0000_0000h|
|CF4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR173)|32|RW|0000_0000h|
|CF8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR174)|32|RW|0000_0000h|
|CFCh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR175)|32|RW|0000_0000h|
|D00h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR176)|32|RW|0000_0000h|
|D04h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR177)|32|RW|0000_0000h|
|D08h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR178)|32|RW|0000_0000h|
|D0Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR179)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

233 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|D10h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR180)|32|RW|0000_0000h|
|D14h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR181)|32|RW|0000_0000h|
|D18h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR182)|32|RW|0000_0000h|
|D1Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR183)|32|RW|0000_0000h|
|D20h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR184)|32|RW|0000_0000h|
|D24h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR185)|32|RW|0000_0000h|
|D28h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR186)|32|RW|0000_0000h|
|D2Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR187)|32|RW|0000_0000h|
|D30h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR188)|32|RW|0000_0000h|
|D34h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR189)|32|RW|0000_0000h|
|D38h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR190)|32|RW|0000_0000h|
|D3Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR191)|32|RW|0000_0000h|
|D40h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR192)|32|RW|0000_0000h|
|D44h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR193)|32|RW|0000_0000h|
|D48h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR194)|32|RW|0000_0000h|
|D4Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR195)|32|RW|0000_0000h|
|D50h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR196)|32|RW|0000_0000h|
|D54h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR197)|32|RW|0000_0000h|
|D58h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR198)|32|RW|0000_0000h|
|D5Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR199)|32|RW|0000_0000h|
|D60h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR200)|32|RW|0000_0000h|
|D64h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR201)|32|RW|0000_0000h|
|D68h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR202)|32|RW|0000_0000h|
|D8Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR211)|32|RW|0000_0000h|
|D90h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR212)|32|RW|0000_0000h|
|D94h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR213)|32|RW|0000_0000h|
|D98h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR214)|32|RW|0000_0000h|
|D9Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR215)|32|RW|0000_0000h|
|DA0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR216)|32|RW|0000_0000h|
|DA4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR217)|32|RW|0000_0000h|
|DA8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR218)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

234 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|DACh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR219)|32|RW|0000_0000h|
|DB0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR220)|32|RW|0000_0000h|
|DB4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR221)|32|RW|0000_0000h|
|DB8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR222)|32|RW|0000_0000h|
|DBCh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR223)|32|RW|0000_0000h|
|DC0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR224)|32|RW|0000_0000h|
|DC4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR225)|32|RW|0000_0000h|
|DC8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR226)|32|RW|0000_0000h|
|DCCh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR227)|32|RW|0000_0000h|
|DD0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR228)|32|RW|0000_0000h|
|DD4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR229)|32|RW|0000_0000h|
|DD8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR230)|32|RW|0000_0000h|
|DDCh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR231)|32|RW|0000_0000h|
|DE0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR232)|32|RW|0000_0000h|
|DE4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR233)|32|RW|0000_0000h|
|DE8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR234)|32|RW|0000_0000h|
|DECh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR235)|32|RW|0000_0000h|
|DF0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR236)|32|RW|0000_0000h|
|DF4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR237)|32|RW|0000_0000h|
|DF8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR238)|32|RW|0000_0000h|
|DFCh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR239)|32|RW|0000_0000h|
|E00h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR240)|32|RW|0000_0000h|
|E04h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR241)|32|RW|0000_0000h|
|E08h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR242)|32|RW|0000_0000h|
|E0Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR243)|32|RW|0000_0000h|
|E10h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR244)|32|RW|0000_0000h|
|E14h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR245)|32|RW|0000_0000h|
|E18h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR246)|32|RW|0000_0000h|
|E1Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR247)|32|RW|0000_0000h|
|E20h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR248)|32|RW|0000_0000h|
|E24h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR249)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

235 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|E28h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR250)|32|RW|0000_0000h|
|E2Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR251)|32|RW|0000_0000h|
|E30h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR252)|32|RW|0000_0000h|
|E34h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR253)|32|RW|0000_0000h|
|E38h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR254)|32|RW|0000_0000h|
|E3Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR255)|32|RW|0000_0000h|
|E40h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR256)|32|RW|0000_0000h|
|E44h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR257)|32|RW|0000_0000h|
|E48h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR258)|32|RW|0000_0000h|
|E4Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR259)|32|RW|0000_0000h|
|E50h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR260)|32|RW|0000_0000h|
|E54h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR261)|32|RW|0000_0000h|
|E58h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR262)|32|RW|0000_0000h|
|E5Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR263)|32|RW|0000_0000h|
|E60h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR264)|32|RW|0000_0000h|
|E64h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR265)|32|RW|0000_0000h|
|E68h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR266)|32|RW|0000_0000h|
|E6Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR267)|32|RW|0000_0000h|
|E70h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR268)|32|RW|0000_0000h|
|EC4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR289)|32|RW|0000_0000h|
|EC8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR290)|32|RW|0000_0000h|
|ECCh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR291)|32|RW|0000_0000h|
|ED0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR292)|32|RW|0000_0000h|
|ED4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR293)|32|RW|0000_0000h|
|ED8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR294)|32|RW|0000_0000h|
|EDCh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR295)|32|RW|0000_0000h|
|EE0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR296)|32|RW|0000_0000h|
|EE4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR297)|32|RW|0000_0000h|
|EE8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR298)|32|RW|0000_0000h|
|EECh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR299)|32|RW|0000_0000h|
|EF0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR300)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

236 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|EF4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR301)|32|RW|0000_0000h|
|EF8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR302)|32|RW|0000_0000h|
|EFCh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR303)|32|RW|0000_0000h|
|F00h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR304)|32|RW|0000_0000h|
|F04h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR305)|32|RW|0000_0000h|
|F08h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR306)|32|RW|0000_0000h|
|F0Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR307)|32|RW|0000_0000h|
|F10h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR308)|32|RW|0000_0000h|
|F14h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR309)|32|RW|0000_0000h|
|F2Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR315)|32|RW|0000_0000h|
|F30h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR316)|32|RW|0000_0000h|
|F34h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR317)|32|RW|0000_0000h|
|F38h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR318)|32|RW|0000_0000h|
|F3Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR319)|32|RW|0000_0000h|
|F40h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR320)|32|RW|0000_0000h|
|F44h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR321)|32|RW|0000_0000h|
|F48h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR322)|32|RW|0000_0000h|
|F4Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR323)|32|RW|0000_0000h|
|F50h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR324)|32|RW|0000_0000h|
|F54h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR325)|32|RW|0000_0000h|
|F9Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR343)|32|RW|0000_0000h|
|FA0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR344)|32|RW|0000_0000h|
|FA4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR345)|32|RW|0000_0000h|
|FA8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR346)|32|RW|0000_0000h|
|FACh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR347)|32|RW|0000_0000h|
|FB0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR348)|32|RW|0000_0000h|
|FB4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR349)|32|RW|0000_0000h|
|FB8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR350)|32|RW|0000_0000h|
|FBCh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR351)|32|RW|0000_0000h|
|FC0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR352)|32|RW|0000_0000h|
|FC4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR353)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

237 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|FC8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR354)|32|RW|0000_0000h|
|FCCh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR355)|32|RW|0000_0000h|
|FD0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR356)|32|RW|0000_0000h|
|FD4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR357)|32|RW|0000_0000h|
|FD8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR358)|32|RW|0000_0000h|
|FDCh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR359)|32|RW|0000_0000h|
|FE0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR360)|32|RW|0000_0000h|
|FE4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR361)|32|RW|0000_0000h|
|FE8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR362)|32|RW|0000_0000h|
|FECh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR363)|32|RW|0000_0000h|
|FF0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR364)|32|RW|0000_0000h|
|FF4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR365)|32|RW|0000_0000h|
|FF8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR366)|32|RW|0000_0000h|
|FFCh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR367)|32|RW|0000_0000h|
|1000h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR368)|32|RW|0000_0000h|
|1004h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR369)|32|RW|0000_0000h|
|1008h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR370)|32|RW|0000_0000h|
|100Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR371)|32|RW|0000_0000h|
|1010h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR372)|32|RW|0000_0000h|
|1014h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR373)|32|RW|0000_0000h|
|1018h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR374)|32|RW|0000_0000h|
|101Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR375)|32|RW|0000_0000h|
|1020h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR376)|32|RW|0000_0000h|
|1024h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR377)|32|RW|0000_0000h|
|1028h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR378)|32|RW|0000_0000h|
|1054h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR389)|32|RW|0000_0000h|
|1078h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR398)|32|RW|0000_0000h|
|107Ch|SIUL2 Input Multiplexed Signal Configuration Register (IMCR399)|32|RW|0000_0000h|
|10A4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR409)|32|RW|0000_0000h|
|10A8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR410)|32|RW|0000_0000h|
|10ACh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR411)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

238 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|10B0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR412)|32|RW|0000_0000h|
|10B4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR413)|32|RW|0000_0000h|
|10B8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR414)|32|RW|0000_0000h|
|10BCh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR415)|32|RW|0000_0000h|
|10C0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR416)|32|RW|0000_0000h|
|10C4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR417)|32|RW|0000_0000h|
|10C8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR418)|32|RW|0000_0000h|
|10CCh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR419)|32|RW|0000_0000h|
|10D0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR420)|32|RW|0000_0000h|
|10D4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR421)|32|RW|0000_0000h|
|10D8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR422)|32|RW|0000_0000h|
|10DCh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR423)|32|RW|0000_0000h|
|10E0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR424)|32|RW|0000_0000h|
|10E4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR425)|32|RW|0000_0000h|
|10E8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR426)|32|RW|0000_0000h|
|10ECh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR427)|32|RW|0000_0000h|
|10F0h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR428)|32|RW|0000_0000h|
|10F4h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR429)|32|RW|0000_0000h|
|10F8h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR430)|32|RW|0000_0000h|
|10FCh|SIUL2 Input Multiplexed Signal Configuration Register (IMCR431)|32|RW|0000_0000h|
|1100h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR432)|32|RW|0000_0000h|
|1104h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR433)|32|RW|0000_0000h|
|1108h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR434)|32|RW|0000_0000h|
|1114h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR437)|32|RW|0000_0000h|
|1120h|SIUL2 Input Multiplexed Signal Configuration Register (IMCR440)|32|RW|0000_0000h|
|1300h|SIUL2 GPIO Pad Data Output Register (GPDO3)|8|RW|00h|
|1301h|SIUL2 GPIO Pad Data Output Register (GPDO2)|8|RW|00h|
|1302h|SIUL2 GPIO Pad Data Output Register (GPDO1)|8|RW|00h|
|1303h|SIUL2 GPIO Pad Data Output Register (GPDO0)|8|RW|00h|
|1304h|SIUL2 GPIO Pad Data Output Register (GPDO7)|8|RW|00h|
|1305h|SIUL2 GPIO Pad Data Output Register (GPDO6)|8|RW|00h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

239 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|1306h|SIUL2 GPIO Pad Data Output Register (GPDO5)|8|RW|00h|
|1307h|SIUL2 GPIO Pad Data Output Register (GPDO4)|8|RW|00h|
|1308h|SIUL2 GPIO Pad Data Output Register (GPDO11)|8|RW|00h|
|1309h|SIUL2 GPIO Pad Data Output Register (GPDO10)|8|RW|00h|
|130Ah|SIUL2 GPIO Pad Data Output Register (GPDO9)|8|RW|00h|
|130Bh|SIUL2 GPIO Pad Data Output Register (GPDO8)|8|RW|00h|
|130Ch|SIUL2 GPIO Pad Data Output Register (GPDO15)|8|RW|00h|
|130Dh|SIUL2 GPIO Pad Data Output Register (GPDO14)|8|RW|00h|
|130Eh|SIUL2 GPIO Pad Data Output Register (GPDO13)|8|RW|00h|
|130Fh|SIUL2 GPIO Pad Data Output Register (GPDO12)|8|RW|00h|
|1310h|SIUL2 GPIO Pad Data Output Register (GPDO19)|8|RW|00h|
|1311h|SIUL2 GPIO Pad Data Output Register (GPDO18)|8|RW|00h|
|1312h|SIUL2 GPIO Pad Data Output Register (GPDO17)|8|RW|00h|
|1313h|SIUL2 GPIO Pad Data Output Register (GPDO16)|8|RW|00h|
|1314h|SIUL2 GPIO Pad Data Output Register (GPDO23)|8|RW|00h|
|1315h|SIUL2 GPIO Pad Data Output Register (GPDO22)|8|RW|00h|
|1316h|SIUL2 GPIO Pad Data Output Register (GPDO21)|8|RW|00h|
|1317h|SIUL2 GPIO Pad Data Output Register (GPDO20)|8|RW|00h|
|1318h|SIUL2 GPIO Pad Data Output Register (GPDO27)|8|RW|00h|
|1319h|SIUL2 GPIO Pad Data Output Register (GPDO26)|8|RW|00h|
|131Ah|SIUL2 GPIO Pad Data Output Register (GPDO25)|8|RW|00h|
|131Bh|SIUL2 GPIO Pad Data Output Register (GPDO24)|8|RW|00h|
|131Ch|SIUL2 GPIO Pad Data Output Register (GPDO31)|8|RW|00h|
|131Dh|SIUL2 GPIO Pad Data Output Register (GPDO30)|8|RW|00h|
|131Eh|SIUL2 GPIO Pad Data Output Register (GPDO29)|8|RW|00h|
|131Fh|SIUL2 GPIO Pad Data Output Register (GPDO28)|8|RW|00h|
|1320h|SIUL2 GPIO Pad Data Output Register (GPDO35)|8|RW|00h|
|1321h|SIUL2 GPIO Pad Data Output Register (GPDO34)|8|RW|00h|
|1322h|SIUL2 GPIO Pad Data Output Register (GPDO33)|8|RW|00h|
|1323h|SIUL2 GPIO Pad Data Output Register (GPDO32)|8|RW|00h|
|1326h|SIUL2 GPIO Pad Data Output Register (GPDO37)|8|RW|00h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

240 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|1327h|SIUL2 GPIO Pad Data Output Register (GPDO36)|8|RW|00h|
|1328h|SIUL2 GPIO Pad Data Output Register (GPDO43)|8|RW|00h|
|1329h|SIUL2 GPIO Pad Data Output Register (GPDO42)|8|RW|00h|
|132Ah|SIUL2 GPIO Pad Data Output Register (GPDO41)|8|RW|00h|
|132Bh|SIUL2 GPIO Pad Data Output Register (GPDO40)|8|RW|00h|
|132Ch|SIUL2 GPIO Pad Data Output Register (GPDO47)|8|RW|00h|
|132Dh|SIUL2 GPIO Pad Data Output Register (GPDO46)|8|RW|00h|
|132Eh|SIUL2 GPIO Pad Data Output Register (GPDO45)|8|RW|00h|
|132Fh|SIUL2 GPIO Pad Data Output Register (GPDO44)|8|RW|00h|
|1330h|SIUL2 GPIO Pad Data Output Register (GPDO51)|8|RW|00h|
|1331h|SIUL2 GPIO Pad Data Output Register (GPDO50)|8|RW|00h|
|1332h|SIUL2 GPIO Pad Data Output Register (GPDO49)|8|RW|00h|
|1333h|SIUL2 GPIO Pad Data Output Register (GPDO48)|8|RW|00h|
|1334h|SIUL2 GPIO Pad Data Output Register (GPDO55)|8|RW|00h|
|1335h|SIUL2 GPIO Pad Data Output Register (GPDO54)|8|RW|00h|
|1336h|SIUL2 GPIO Pad Data Output Register (GPDO53)|8|RW|00h|
|1337h|SIUL2 GPIO Pad Data Output Register (GPDO52)|8|RW|00h|
|1338h|SIUL2 GPIO Pad Data Output Register (GPDO59)|8|RW|00h|
|1339h|SIUL2 GPIO Pad Data Output Register (GPDO58)|8|RW|00h|
|133Ah|SIUL2 GPIO Pad Data Output Register (GPDO57)|8|RW|00h|
|133Bh|SIUL2 GPIO Pad Data Output Register (GPDO56)|8|RW|00h|
|133Ch|SIUL2 GPIO Pad Data Output Register (GPDO63)|8|RW|00h|
|133Dh|SIUL2 GPIO Pad Data Output Register (GPDO62)|8|RW|00h|
|133Eh|SIUL2 GPIO Pad Data Output Register (GPDO61)|8|RW|00h|
|133Fh|SIUL2 GPIO Pad Data Output Register (GPDO60)|8|RW|00h|
|1340h|SIUL2 GPIO Pad Data Output Register (GPDO67)|8|RW|00h|
|1341h|SIUL2 GPIO Pad Data Output Register (GPDO66)|8|RW|00h|
|1342h|SIUL2 GPIO Pad Data Output Register (GPDO65)|8|RW|00h|
|1343h|SIUL2 GPIO Pad Data Output Register (GPDO64)|8|RW|00h|
|1344h|SIUL2 GPIO Pad Data Output Register (GPDO71)|8|RW|00h|
|1345h|SIUL2 GPIO Pad Data Output Register (GPDO70)|8|RW|00h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

241 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|1346h|SIUL2 GPIO Pad Data Output Register (GPDO69)|8|RW|00h|
|1347h|SIUL2 GPIO Pad Data Output Register (GPDO68)|8|RW|00h|
|1348h|SIUL2 GPIO Pad Data Output Register (GPDO75)|8|RW|00h|
|1349h|SIUL2 GPIO Pad Data Output Register (GPDO74)|8|RW|00h|
|134Ah|SIUL2 GPIO Pad Data Output Register (GPDO73)|8|RW|00h|
|134Bh|SIUL2 GPIO Pad Data Output Register (GPDO72)|8|RW|00h|
|134Ch|SIUL2 GPIO Pad Data Output Register (GPDO79)|8|RW|00h|
|134Dh|SIUL2 GPIO Pad Data Output Register (GPDO78)|8|RW|00h|
|134Eh|SIUL2 GPIO Pad Data Output Register (GPDO77)|8|RW|00h|
|134Fh|SIUL2 GPIO Pad Data Output Register (GPDO76)|8|RW|00h|
|1350h|SIUL2 GPIO Pad Data Output Register (GPDO83)|8|RW|00h|
|1351h|SIUL2 GPIO Pad Data Output Register (GPDO82)|8|RW|00h|
|1352h|SIUL2 GPIO Pad Data Output Register (GPDO81)|8|RW|00h|
|1353h|SIUL2 GPIO Pad Data Output Register (GPDO80)|8|RW|00h|
|1354h|SIUL2 GPIO Pad Data Output Register (GPDO87)|8|RW|00h|
|1355h|SIUL2 GPIO Pad Data Output Register (GPDO86)|8|RW|00h|
|1356h|SIUL2 GPIO Pad Data Output Register (GPDO85)|8|RW|00h|
|1357h|SIUL2 GPIO Pad Data Output Register (GPDO84)|8|RW|00h|
|1358h|SIUL2 GPIO Pad Data Output Register (GPDO91)|8|RW|00h|
|1359h|SIUL2 GPIO Pad Data Output Register (GPDO90)|8|RW|00h|
|135Ah|SIUL2 GPIO Pad Data Output Register (GPDO89)|8|RW|00h|
|135Bh|SIUL2 GPIO Pad Data Output Register (GPDO88)|8|RW|00h|
|135Ch|SIUL2 GPIO Pad Data Output Register (GPDO95)|8|RW|00h|
|135Dh|SIUL2 GPIO Pad Data Output Register (GPDO94)|8|RW|00h|
|135Eh|SIUL2 GPIO Pad Data Output Register (GPDO93)|8|RW|00h|
|135Fh|SIUL2 GPIO Pad Data Output Register (GPDO92)|8|RW|00h|
|1360h|SIUL2 GPIO Pad Data Output Register (GPDO99)|8|RW|00h|
|1361h|SIUL2 GPIO Pad Data Output Register (GPDO98)|8|RW|00h|
|1362h|SIUL2 GPIO Pad Data Output Register (GPDO97)|8|RW|00h|
|1363h|SIUL2 GPIO Pad Data Output Register (GPDO96)|8|RW|00h|
|1364h|SIUL2 GPIO Pad Data Output Register (GPDO103)|8|RW|00h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

242 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|1365h|SIUL2 GPIO Pad Data Output Register (GPDO102)|8|RW|00h|
|1366h|SIUL2 GPIO Pad Data Output Register (GPDO101)|8|RW|00h|
|1367h|SIUL2 GPIO Pad Data Output Register (GPDO100)|8|RW|00h|
|1368h|SIUL2 GPIO Pad Data Output Register (GPDO107)|8|RW|00h|
|1369h|SIUL2 GPIO Pad Data Output Register (GPDO106)|8|RW|00h|
|136Ah|SIUL2 GPIO Pad Data Output Register (GPDO105)|8|RW|00h|
|136Bh|SIUL2 GPIO Pad Data Output Register (GPDO104)|8|RW|00h|
|136Ch|SIUL2 GPIO Pad Data Output Register (GPDO111)|8|RW|00h|
|136Dh|SIUL2 GPIO Pad Data Output Register (GPDO110)|8|RW|00h|
|136Eh|SIUL2 GPIO Pad Data Output Register (GPDO109)|8|RW|00h|
|136Fh|SIUL2 GPIO Pad Data Output Register (GPDO108)|8|RW|00h|
|1370h|SIUL2 GPIO Pad Data Output Register (GPDO115)|8|RW|00h|
|1371h|SIUL2 GPIO Pad Data Output Register (GPDO114)|8|RW|00h|
|1372h|SIUL2 GPIO Pad Data Output Register (GPDO113)|8|RW|00h|
|1373h|SIUL2 GPIO Pad Data Output Register (GPDO112)|8|RW|00h|
|1374h|SIUL2 GPIO Pad Data Output Register (GPDO119)|8|RW|00h|
|1375h|SIUL2 GPIO Pad Data Output Register (GPDO118)|8|RW|00h|
|1376h|SIUL2 GPIO Pad Data Output Register (GPDO117)|8|RW|00h|
|1377h|SIUL2 GPIO Pad Data Output Register (GPDO116)|8|RW|00h|
|1378h|SIUL2 GPIO Pad Data Output Register (GPDO123)|8|RW|00h|
|1379h|SIUL2 GPIO Pad Data Output Register (GPDO122)|8|RW|00h|
|137Ah|SIUL2 GPIO Pad Data Output Register (GPDO121)|8|RW|00h|
|137Bh|SIUL2 GPIO Pad Data Output Register (GPDO120)|8|RW|00h|
|137Ch|SIUL2 GPIO Pad Data Output Register (GPDO127)|8|RW|00h|
|137Dh|SIUL2 GPIO Pad Data Output Register (GPDO126)|8|RW|00h|
|137Eh|SIUL2 GPIO Pad Data Output Register (GPDO125)|8|RW|00h|
|137Fh|SIUL2 GPIO Pad Data Output Register (GPDO124)|8|RW|00h|
|1380h|SIUL2 GPIO Pad Data Output Register (GPDO131)|8|RW|00h|
|1381h|SIUL2 GPIO Pad Data Output Register (GPDO130)|8|RW|00h|
|1382h|SIUL2 GPIO Pad Data Output Register (GPDO129)|8|RW|00h|
|1383h|SIUL2 GPIO Pad Data Output Register (GPDO128)|8|RW|00h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

243 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|1384h|SIUL2 GPIO Pad Data Output Register (GPDO135)|8|RW|00h|
|1385h|SIUL2 GPIO Pad Data Output Register (GPDO134)|8|RW|00h|
|1386h|SIUL2 GPIO Pad Data Output Register (GPDO133)|8|RW|00h|
|1387h|SIUL2 GPIO Pad Data Output Register (GPDO132)|8|RW|00h|
|1388h|SIUL2 GPIO Pad Data Output Register (GPDO139)|8|RW|00h|
|1389h|SIUL2 GPIO Pad Data Output Register (GPDO138)|8|RW|00h|
|138Ah|SIUL2 GPIO Pad Data Output Register (GPDO137)|8|RW|00h|
|138Bh|SIUL2 GPIO Pad Data Output Register (GPDO136)|8|RW|00h|
|138Ch|SIUL2 GPIO Pad Data Output Register (GPDO143)|8|RW|00h|
|138Dh|SIUL2 GPIO Pad Data Output Register (GPDO142)|8|RW|00h|
|138Eh|SIUL2 GPIO Pad Data Output Register (GPDO141)|8|RW|00h|
|138Fh|SIUL2 GPIO Pad Data Output Register (GPDO140)|8|RW|00h|
|1390h|SIUL2 GPIO Pad Data Output Register (GPDO147)|8|RW|00h|
|1391h|SIUL2 GPIO Pad Data Output Register (GPDO146)|8|RW|00h|
|1392h|SIUL2 GPIO Pad Data Output Register (GPDO145)|8|RW|00h|
|1393h|SIUL2 GPIO Pad Data Output Register (GPDO144)|8|RW|00h|
|1394h|SIUL2 GPIO Pad Data Output Register (GPDO151)|8|RW|00h|
|1395h|SIUL2 GPIO Pad Data Output Register (GPDO150)|8|RW|00h|
|1396h|SIUL2 GPIO Pad Data Output Register (GPDO149)|8|RW|00h|
|1397h|SIUL2 GPIO Pad Data Output Register (GPDO148)|8|RW|00h|
|1398h|SIUL2 GPIO Pad Data Output Register (GPDO155)|8|RW|00h|
|1399h|SIUL2 GPIO Pad Data Output Register (GPDO154)|8|RW|00h|
|139Ah|SIUL2 GPIO Pad Data Output Register (GPDO153)|8|RW|00h|
|139Bh|SIUL2 GPIO Pad Data Output Register (GPDO152)|8|RW|00h|
|139Ch|SIUL2 GPIO Pad Data Output Register (GPDO159)|8|RW|00h|
|139Dh|SIUL2 GPIO Pad Data Output Register (GPDO158)|8|RW|00h|
|139Eh|SIUL2 GPIO Pad Data Output Register (GPDO157)|8|RW|00h|
|139Fh|SIUL2 GPIO Pad Data Output Register (GPDO156)|8|RW|00h|
|13A0h|SIUL2 GPIO Pad Data Output Register (GPDO163)|8|RW|00h|
|13A1h|SIUL2 GPIO Pad Data Output Register (GPDO162)|8|RW|00h|
|13A2h|SIUL2 GPIO Pad Data Output Register (GPDO161)|8|RW|00h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

244 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|13A3h|SIUL2 GPIO Pad Data Output Register (GPDO160)|8|RW|00h|
|13A4h|SIUL2 GPIO Pad Data Output Register (GPDO167)|8|RW|00h|
|13A5h|SIUL2 GPIO Pad Data Output Register (GPDO166)|8|RW|00h|
|13A6h|SIUL2 GPIO Pad Data Output Register (GPDO165)|8|RW|00h|
|13A7h|SIUL2 GPIO Pad Data Output Register (GPDO164)|8|RW|00h|
|13A8h|SIUL2 GPIO Pad Data Output Register (GPDO171)|8|RW|00h|
|13A9h|SIUL2 GPIO Pad Data Output Register (GPDO170)|8|RW|00h|
|13AAh|SIUL2 GPIO Pad Data Output Register (GPDO169)|8|RW|00h|
|13ABh|SIUL2 GPIO Pad Data Output Register (GPDO168)|8|RW|00h|
|13ACh|SIUL2 GPIO Pad Data Output Register (GPDO175)|8|RW|00h|
|13ADh|SIUL2 GPIO Pad Data Output Register (GPDO174)|8|RW|00h|
|13AEh|SIUL2 GPIO Pad Data Output Register (GPDO173)|8|RW|00h|
|13AFh|SIUL2 GPIO Pad Data Output Register (GPDO172)|8|RW|00h|
|13B0h|SIUL2 GPIO Pad Data Output Register (GPDO179)|8|RW|00h|
|13B1h|SIUL2 GPIO Pad Data Output Register (GPDO178)|8|RW|00h|
|13B2h|SIUL2 GPIO Pad Data Output Register (GPDO177)|8|RW|00h|
|13B3h|SIUL2 GPIO Pad Data Output Register (GPDO176)|8|RW|00h|
|13B4h|SIUL2 GPIO Pad Data Output Register (GPDO183)|8|RW|00h|
|13B5h|SIUL2 GPIO Pad Data Output Register (GPDO182)|8|RW|00h|
|13B6h|SIUL2 GPIO Pad Data Output Register (GPDO181)|8|RW|00h|
|13B7h|SIUL2 GPIO Pad Data Output Register (GPDO180)|8|RW|00h|
|13B8h|SIUL2 GPIO Pad Data Output Register (GPDO187)|8|RW|00h|
|13B9h|SIUL2 GPIO Pad Data Output Register (GPDO186)|8|RW|00h|
|13BAh|SIUL2 GPIO Pad Data Output Register (GPDO185)|8|RW|00h|
|13BBh|SIUL2 GPIO Pad Data Output Register (GPDO184)|8|RW|00h|
|13BCh|SIUL2 GPIO Pad Data Output Register (GPDO191)|8|RW|00h|
|13BDh|SIUL2 GPIO Pad Data Output Register (GPDO190)|8|RW|00h|
|13BEh|SIUL2 GPIO Pad Data Output Register (GPDO189)|8|RW|00h|
|13BFh|SIUL2 GPIO Pad Data Output Register (GPDO188)|8|RW|00h|
|13C0h|SIUL2 GPIO Pad Data Output Register (GPDO195)|8|RW|00h|
|13C1h|SIUL2 GPIO Pad Data Output Register (GPDO194)|8|RW|00h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

245 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|13C2h|SIUL2 GPIO Pad Data Output Register (GPDO193)|8|RW|00h|
|13C3h|SIUL2 GPIO Pad Data Output Register (GPDO192)|8|RW|00h|
|13C4h|SIUL2 GPIO Pad Data Output Register (GPDO199)|8|RW|00h|
|13C5h|SIUL2 GPIO Pad Data Output Register (GPDO198)|8|RW|00h|
|13C6h|SIUL2 GPIO Pad Data Output Register (GPDO197)|8|RW|00h|
|13C7h|SIUL2 GPIO Pad Data Output Register (GPDO196)|8|RW|00h|
|13C8h|SIUL2 GPIO Pad Data Output Register (GPDO203)|8|RW|00h|
|13C9h|SIUL2 GPIO Pad Data Output Register (GPDO202)|8|RW|00h|
|13CAh|SIUL2 GPIO Pad Data Output Register (GPDO201)|8|RW|00h|
|13CBh|SIUL2 GPIO Pad Data Output Register (GPDO200)|8|RW|00h|
|13CCh|SIUL2 GPIO Pad Data Output Register (GPDO207)|8|RW|00h|
|13CDh|SIUL2 GPIO Pad Data Output Register (GPDO206)|8|RW|00h|
|13CEh|SIUL2 GPIO Pad Data Output Register (GPDO205)|8|RW|00h|
|13CFh|SIUL2 GPIO Pad Data Output Register (GPDO204)|8|RW|00h|
|13D0h|SIUL2 GPIO Pad Data Output Register (GPDO211)|8|RW|00h|
|13D1h|SIUL2 GPIO Pad Data Output Register (GPDO210)|8|RW|00h|
|13D2h|SIUL2 GPIO Pad Data Output Register (GPDO209)|8|RW|00h|
|13D3h|SIUL2 GPIO Pad Data Output Register (GPDO208)|8|RW|00h|
|13D4h|SIUL2 GPIO Pad Data Output Register (GPDO215)|8|RW|00h|
|13D5h|SIUL2 GPIO Pad Data Output Register (GPDO214)|8|RW|00h|
|13D6h|SIUL2 GPIO Pad Data Output Register (GPDO213)|8|RW|00h|
|13D7h|SIUL2 GPIO Pad Data Output Register (GPDO212)|8|RW|00h|
|13D8h|SIUL2 GPIO Pad Data Output Register (GPDO219)|8|RW|00h|
|13D9h|SIUL2 GPIO Pad Data Output Register (GPDO218)|8|RW|00h|
|13DAh|SIUL2 GPIO Pad Data Output Register (GPDO217)|8|RW|00h|
|13DBh|SIUL2 GPIO Pad Data Output Register (GPDO216)|8|RW|00h|
|13DCh|SIUL2 GPIO Pad Data Output Register (GPDO223)|8|RW|00h|
|13DDh|SIUL2 GPIO Pad Data Output Register (GPDO222)|8|RW|00h|
|13DEh|SIUL2 GPIO Pad Data Output Register (GPDO221)|8|RW|00h|
|13DFh|SIUL2 GPIO Pad Data Output Register (GPDO220)|8|RW|00h|
|13E0h|SIUL2 GPIO Pad Data Output Register (GPDO227)|8|RW|00h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

246 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|13E1h|SIUL2 GPIO Pad Data Output Register (GPDO226)|8|RW|00h|
|13E2h|SIUL2 GPIO Pad Data Output Register (GPDO225)|8|RW|00h|
|13E3h|SIUL2 GPIO Pad Data Output Register (GPDO224)|8|RW|00h|
|13E4h|SIUL2 GPIO Pad Data Output Register (GPDO231)|8|RW|00h|
|13E5h|SIUL2 GPIO Pad Data Output Register (GPDO230)|8|RW|00h|
|13E6h|SIUL2 GPIO Pad Data Output Register (GPDO229)|8|RW|00h|
|13E7h|SIUL2 GPIO Pad Data Output Register (GPDO228)|8|RW|00h|
|13E8h|SIUL2 GPIO Pad Data Output Register (GPDO235)|8|RW|00h|
|13E9h|SIUL2 GPIO Pad Data Output Register (GPDO234)|8|RW|00h|
|13EAh|SIUL2 GPIO Pad Data Output Register (GPDO233)|8|RW|00h|
|13EBh|SIUL2 GPIO Pad Data Output Register (GPDO232)|8|RW|00h|
|13EFh|SIUL2 GPIO Pad Data Output Register (GPDO236)|8|RW|00h|
|1500h|SIUL2 GPIO Pad Data Input Register (GPDI3)|8|RO|00h|
|1501h|SIUL2 GPIO Pad Data Input Register (GPDI2)|8|RO|00h|
|1502h|SIUL2 GPIO Pad Data Input Register (GPDI1)|8|RO|00h|
|1503h|SIUL2 GPIO Pad Data Input Register (GPDI0)|8|RO|00h|
|1504h|SIUL2 GPIO Pad Data Input Register (GPDI7)|8|RO|00h|
|1505h|SIUL2 GPIO Pad Data Input Register (GPDI6)|8|RO|00h|
|1506h|SIUL2 GPIO Pad Data Input Register (GPDI5)|8|RO|00h|
|1507h|SIUL2 GPIO Pad Data Input Register (GPDI4)|8|RO|00h|
|1508h|SIUL2 GPIO Pad Data Input Register (GPDI11)|8|RO|00h|
|1509h|SIUL2 GPIO Pad Data Input Register (GPDI10)|8|RO|00h|
|150Ah|SIUL2 GPIO Pad Data Input Register (GPDI9)|8|RO|00h|
|150Bh|SIUL2 GPIO Pad Data Input Register (GPDI8)|8|RO|00h|
|150Ch|SIUL2 GPIO Pad Data Input Register (GPDI15)|8|RO|00h|
|150Dh|SIUL2 GPIO Pad Data Input Register (GPDI14)|8|RO|00h|
|150Eh|SIUL2 GPIO Pad Data Input Register (GPDI13)|8|RO|00h|
|150Fh|SIUL2 GPIO Pad Data Input Register (GPDI12)|8|RO|00h|
|1510h|SIUL2 GPIO Pad Data Input Register (GPDI19)|8|RO|00h|
|1511h|SIUL2 GPIO Pad Data Input Register (GPDI18)|8|RO|00h|
|1512h|SIUL2 GPIO Pad Data Input Register (GPDI17)|8|RO|00h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

247 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|1513h|SIUL2 GPIO Pad Data Input Register (GPDI16)|8|RO|00h|
|1514h|SIUL2 GPIO Pad Data Input Register (GPDI23)|8|RO|00h|
|1515h|SIUL2 GPIO Pad Data Input Register (GPDI22)|8|RO|00h|
|1516h|SIUL2 GPIO Pad Data Input Register (GPDI21)|8|RO|00h|
|1517h|SIUL2 GPIO Pad Data Input Register (GPDI20)|8|RO|00h|
|1518h|SIUL2 GPIO Pad Data Input Register (GPDI27)|8|RO|00h|
|1519h|SIUL2 GPIO Pad Data Input Register (GPDI26)|8|RO|00h|
|151Ah|SIUL2 GPIO Pad Data Input Register (GPDI25)|8|RO|00h|
|151Bh|SIUL2 GPIO Pad Data Input Register (GPDI24)|8|RO|00h|
|151Ch|SIUL2 GPIO Pad Data Input Register (GPDI31)|8|RO|00h|
|151Dh|SIUL2 GPIO Pad Data Input Register (GPDI30)|8|RO|00h|
|151Eh|SIUL2 GPIO Pad Data Input Register (GPDI29)|8|RO|00h|
|151Fh|SIUL2 GPIO Pad Data Input Register (GPDI28)|8|RO|00h|
|1520h|SIUL2 GPIO Pad Data Input Register (GPDI35)|8|RO|00h|
|1521h|SIUL2 GPIO Pad Data Input Register (GPDI34)|8|RO|00h|
|1522h|SIUL2 GPIO Pad Data Input Register (GPDI33)|8|RO|00h|
|1523h|SIUL2 GPIO Pad Data Input Register (GPDI32)|8|RO|00h|
|1526h|SIUL2 GPIO Pad Data Input Register (GPDI37)|8|RO|00h|
|1527h|SIUL2 GPIO Pad Data Input Register (GPDI36)|8|RO|00h|
|1528h|SIUL2 GPIO Pad Data Input Register (GPDI43)|8|RO|00h|
|1529h|SIUL2 GPIO Pad Data Input Register (GPDI42)|8|RO|00h|
|152Ah|SIUL2 GPIO Pad Data Input Register (GPDI41)|8|RO|00h|
|152Bh|SIUL2 GPIO Pad Data Input Register (GPDI40)|8|RO|00h|
|152Ch|SIUL2 GPIO Pad Data Input Register (GPDI47)|8|RO|00h|
|152Dh|SIUL2 GPIO Pad Data Input Register (GPDI46)|8|RO|00h|
|152Eh|SIUL2 GPIO Pad Data Input Register (GPDI45)|8|RO|00h|
|152Fh|SIUL2 GPIO Pad Data Input Register (GPDI44)|8|RO|00h|
|1530h|SIUL2 GPIO Pad Data Input Register (GPDI51)|8|RO|00h|
|1531h|SIUL2 GPIO Pad Data Input Register (GPDI50)|8|RO|00h|
|1532h|SIUL2 GPIO Pad Data Input Register (GPDI49)|8|RO|00h|
|1533h|SIUL2 GPIO Pad Data Input Register (GPDI48)|8|RO|00h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

248 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|1534h|SIUL2 GPIO Pad Data Input Register (GPDI55)|8|RO|00h|
|1535h|SIUL2 GPIO Pad Data Input Register (GPDI54)|8|RO|00h|
|1536h|SIUL2 GPIO Pad Data Input Register (GPDI53)|8|RO|00h|
|1537h|SIUL2 GPIO Pad Data Input Register (GPDI52)|8|RO|00h|
|1538h|SIUL2 GPIO Pad Data Input Register (GPDI59)|8|RO|00h|
|1539h|SIUL2 GPIO Pad Data Input Register (GPDI58)|8|RO|00h|
|153Ah|SIUL2 GPIO Pad Data Input Register (GPDI57)|8|RO|00h|
|153Bh|SIUL2 GPIO Pad Data Input Register (GPDI56)|8|RO|00h|
|153Ch|SIUL2 GPIO Pad Data Input Register (GPDI63)|8|RO|00h|
|153Dh|SIUL2 GPIO Pad Data Input Register (GPDI62)|8|RO|00h|
|153Eh|SIUL2 GPIO Pad Data Input Register (GPDI61)|8|RO|00h|
|153Fh|SIUL2 GPIO Pad Data Input Register (GPDI60)|8|RO|00h|
|1540h|SIUL2 GPIO Pad Data Input Register (GPDI67)|8|RO|00h|
|1541h|SIUL2 GPIO Pad Data Input Register (GPDI66)|8|RO|00h|
|1542h|SIUL2 GPIO Pad Data Input Register (GPDI65)|8|RO|00h|
|1543h|SIUL2 GPIO Pad Data Input Register (GPDI64)|8|RO|00h|
|1544h|SIUL2 GPIO Pad Data Input Register (GPDI71)|8|RO|00h|
|1545h|SIUL2 GPIO Pad Data Input Register (GPDI70)|8|RO|00h|
|1546h|SIUL2 GPIO Pad Data Input Register (GPDI69)|8|RO|00h|
|1547h|SIUL2 GPIO Pad Data Input Register (GPDI68)|8|RO|00h|
|1548h|SIUL2 GPIO Pad Data Input Register (GPDI75)|8|RO|00h|
|1549h|SIUL2 GPIO Pad Data Input Register (GPDI74)|8|RO|00h|
|154Ah|SIUL2 GPIO Pad Data Input Register (GPDI73)|8|RO|00h|
|154Bh|SIUL2 GPIO Pad Data Input Register (GPDI72)|8|RO|00h|
|154Ch|SIUL2 GPIO Pad Data Input Register (GPDI79)|8|RO|00h|
|154Dh|SIUL2 GPIO Pad Data Input Register (GPDI78)|8|RO|00h|
|154Eh|SIUL2 GPIO Pad Data Input Register (GPDI77)|8|RO|00h|
|154Fh|SIUL2 GPIO Pad Data Input Register (GPDI76)|8|RO|00h|
|1550h|SIUL2 GPIO Pad Data Input Register (GPDI83)|8|RO|00h|
|1551h|SIUL2 GPIO Pad Data Input Register (GPDI82)|8|RO|00h|
|1552h|SIUL2 GPIO Pad Data Input Register (GPDI81)|8|RO|00h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

249 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|1553h|SIUL2 GPIO Pad Data Input Register (GPDI80)|8|RO|00h|
|1554h|SIUL2 GPIO Pad Data Input Register (GPDI87)|8|RO|00h|
|1555h|SIUL2 GPIO Pad Data Input Register (GPDI86)|8|RO|00h|
|1556h|SIUL2 GPIO Pad Data Input Register (GPDI85)|8|RO|00h|
|1557h|SIUL2 GPIO Pad Data Input Register (GPDI84)|8|RO|00h|
|1558h|SIUL2 GPIO Pad Data Input Register (GPDI91)|8|RO|00h|
|1559h|SIUL2 GPIO Pad Data Input Register (GPDI90)|8|RO|00h|
|155Ah|SIUL2 GPIO Pad Data Input Register (GPDI89)|8|RO|00h|
|155Bh|SIUL2 GPIO Pad Data Input Register (GPDI88)|8|RO|00h|
|155Ch|SIUL2 GPIO Pad Data Input Register (GPDI95)|8|RO|00h|
|155Dh|SIUL2 GPIO Pad Data Input Register (GPDI94)|8|RO|00h|
|155Eh|SIUL2 GPIO Pad Data Input Register (GPDI93)|8|RO|00h|
|155Fh|SIUL2 GPIO Pad Data Input Register (GPDI92)|8|RO|00h|
|1560h|SIUL2 GPIO Pad Data Input Register (GPDI99)|8|RO|00h|
|1561h|SIUL2 GPIO Pad Data Input Register (GPDI98)|8|RO|00h|
|1562h|SIUL2 GPIO Pad Data Input Register (GPDI97)|8|RO|00h|
|1563h|SIUL2 GPIO Pad Data Input Register (GPDI96)|8|RO|00h|
|1564h|SIUL2 GPIO Pad Data Input Register (GPDI103)|8|RO|00h|
|1565h|SIUL2 GPIO Pad Data Input Register (GPDI102)|8|RO|00h|
|1566h|SIUL2 GPIO Pad Data Input Register (GPDI101)|8|RO|00h|
|1567h|SIUL2 GPIO Pad Data Input Register (GPDI100)|8|RO|00h|
|1568h|SIUL2 GPIO Pad Data Input Register (GPDI107)|8|RO|00h|
|1569h|SIUL2 GPIO Pad Data Input Register (GPDI106)|8|RO|00h|
|156Ah|SIUL2 GPIO Pad Data Input Register (GPDI105)|8|RO|00h|
|156Bh|SIUL2 GPIO Pad Data Input Register (GPDI104)|8|RO|00h|
|156Ch|SIUL2 GPIO Pad Data Input Register (GPDI111)|8|RO|00h|
|156Dh|SIUL2 GPIO Pad Data Input Register (GPDI110)|8|RO|00h|
|156Eh|SIUL2 GPIO Pad Data Input Register (GPDI109)|8|RO|00h|
|156Fh|SIUL2 GPIO Pad Data Input Register (GPDI108)|8|RO|00h|
|1570h|SIUL2 GPIO Pad Data Input Register (GPDI115)|8|RO|00h|
|1571h|SIUL2 GPIO Pad Data Input Register (GPDI114)|8|RO|00h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

250 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|1572h|SIUL2 GPIO Pad Data Input Register (GPDI113)|8|RO|00h|
|1573h|SIUL2 GPIO Pad Data Input Register (GPDI112)|8|RO|00h|
|1574h|SIUL2 GPIO Pad Data Input Register (GPDI119)|8|RO|00h|
|1575h|SIUL2 GPIO Pad Data Input Register (GPDI118)|8|RO|00h|
|1576h|SIUL2 GPIO Pad Data Input Register (GPDI117)|8|RO|00h|
|1577h|SIUL2 GPIO Pad Data Input Register (GPDI116)|8|RO|00h|
|1578h|SIUL2 GPIO Pad Data Input Register (GPDI123)|8|RO|00h|
|1579h|SIUL2 GPIO Pad Data Input Register (GPDI122)|8|RO|00h|
|157Ah|SIUL2 GPIO Pad Data Input Register (GPDI121)|8|RO|00h|
|157Bh|SIUL2 GPIO Pad Data Input Register (GPDI120)|8|RO|00h|
|157Ch|SIUL2 GPIO Pad Data Input Register (GPDI127)|8|RO|00h|
|157Dh|SIUL2 GPIO Pad Data Input Register (GPDI126)|8|RO|00h|
|157Eh|SIUL2 GPIO Pad Data Input Register (GPDI125)|8|RO|00h|
|157Fh|SIUL2 GPIO Pad Data Input Register (GPDI124)|8|RO|00h|
|1580h|SIUL2 GPIO Pad Data Input Register (GPDI131)|8|RO|00h|
|1581h|SIUL2 GPIO Pad Data Input Register (GPDI130)|8|RO|00h|
|1582h|SIUL2 GPIO Pad Data Input Register (GPDI129)|8|RO|00h|
|1583h|SIUL2 GPIO Pad Data Input Register (GPDI128)|8|RO|00h|
|1584h|SIUL2 GPIO Pad Data Input Register (GPDI135)|8|RO|00h|
|1585h|SIUL2 GPIO Pad Data Input Register (GPDI134)|8|RO|00h|
|1586h|SIUL2 GPIO Pad Data Input Register (GPDI133)|8|RO|00h|
|1587h|SIUL2 GPIO Pad Data Input Register (GPDI132)|8|RO|00h|
|1588h|SIUL2 GPIO Pad Data Input Register (GPDI139)|8|RO|00h|
|1589h|SIUL2 GPIO Pad Data Input Register (GPDI138)|8|RO|00h|
|158Ah|SIUL2 GPIO Pad Data Input Register (GPDI137)|8|RO|00h|
|158Bh|SIUL2 GPIO Pad Data Input Register (GPDI136)|8|RO|00h|
|158Ch|SIUL2 GPIO Pad Data Input Register (GPDI143)|8|RO|00h|
|158Dh|SIUL2 GPIO Pad Data Input Register (GPDI142)|8|RO|00h|
|158Eh|SIUL2 GPIO Pad Data Input Register (GPDI141)|8|RO|00h|
|158Fh|SIUL2 GPIO Pad Data Input Register (GPDI140)|8|RO|00h|
|1590h|SIUL2 GPIO Pad Data Input Register (GPDI147)|8|RO|00h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

251 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|1591h|SIUL2 GPIO Pad Data Input Register (GPDI146)|8|RO|00h|
|1592h|SIUL2 GPIO Pad Data Input Register (GPDI145)|8|RO|00h|
|1593h|SIUL2 GPIO Pad Data Input Register (GPDI144)|8|RO|00h|
|1594h|SIUL2 GPIO Pad Data Input Register (GPDI151)|8|RO|00h|
|1595h|SIUL2 GPIO Pad Data Input Register (GPDI150)|8|RO|00h|
|1596h|SIUL2 GPIO Pad Data Input Register (GPDI149)|8|RO|00h|
|1597h|SIUL2 GPIO Pad Data Input Register (GPDI148)|8|RO|00h|
|1598h|SIUL2 GPIO Pad Data Input Register (GPDI155)|8|RO|00h|
|1599h|SIUL2 GPIO Pad Data Input Register (GPDI154)|8|RO|00h|
|159Ah|SIUL2 GPIO Pad Data Input Register (GPDI153)|8|RO|00h|
|159Bh|SIUL2 GPIO Pad Data Input Register (GPDI152)|8|RO|00h|
|159Ch|SIUL2 GPIO Pad Data Input Register (GPDI159)|8|RO|00h|
|159Dh|SIUL2 GPIO Pad Data Input Register (GPDI158)|8|RO|00h|
|159Eh|SIUL2 GPIO Pad Data Input Register (GPDI157)|8|RO|00h|
|159Fh|SIUL2 GPIO Pad Data Input Register (GPDI156)|8|RO|00h|
|15A0h|SIUL2 GPIO Pad Data Input Register (GPDI163)|8|RO|00h|
|15A1h|SIUL2 GPIO Pad Data Input Register (GPDI162)|8|RO|00h|
|15A2h|SIUL2 GPIO Pad Data Input Register (GPDI161)|8|RO|00h|
|15A3h|SIUL2 GPIO Pad Data Input Register (GPDI160)|8|RO|00h|
|15A4h|SIUL2 GPIO Pad Data Input Register (GPDI167)|8|RO|00h|
|15A5h|SIUL2 GPIO Pad Data Input Register (GPDI166)|8|RO|00h|
|15A6h|SIUL2 GPIO Pad Data Input Register (GPDI165)|8|RO|00h|
|15A7h|SIUL2 GPIO Pad Data Input Register (GPDI164)|8|RO|00h|
|15A8h|SIUL2 GPIO Pad Data Input Register (GPDI171)|8|RO|00h|
|15A9h|SIUL2 GPIO Pad Data Input Register (GPDI170)|8|RO|00h|
|15AAh|SIUL2 GPIO Pad Data Input Register (GPDI169)|8|RO|00h|
|15ABh|SIUL2 GPIO Pad Data Input Register (GPDI168)|8|RO|00h|
|15ACh|SIUL2 GPIO Pad Data Input Register (GPDI175)|8|RO|00h|
|15ADh|SIUL2 GPIO Pad Data Input Register (GPDI174)|8|RO|00h|
|15AEh|SIUL2 GPIO Pad Data Input Register (GPDI173)|8|RO|00h|
|15AFh|SIUL2 GPIO Pad Data Input Register (GPDI172)|8|RO|00h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

252 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|15B0h|SIUL2 GPIO Pad Data Input Register (GPDI179)|8|RO|00h|
|15B1h|SIUL2 GPIO Pad Data Input Register (GPDI178)|8|RO|00h|
|15B2h|SIUL2 GPIO Pad Data Input Register (GPDI177)|8|RO|00h|
|15B3h|SIUL2 GPIO Pad Data Input Register (GPDI176)|8|RO|00h|
|15B4h|SIUL2 GPIO Pad Data Input Register (GPDI183)|8|RO|00h|
|15B5h|SIUL2 GPIO Pad Data Input Register (GPDI182)|8|RO|00h|
|15B6h|SIUL2 GPIO Pad Data Input Register (GPDI181)|8|RO|00h|
|15B7h|SIUL2 GPIO Pad Data Input Register (GPDI180)|8|RO|00h|
|15B8h|SIUL2 GPIO Pad Data Input Register (GPDI187)|8|RO|00h|
|15B9h|SIUL2 GPIO Pad Data Input Register (GPDI186)|8|RO|00h|
|15BAh|SIUL2 GPIO Pad Data Input Register (GPDI185)|8|RO|00h|
|15BBh|SIUL2 GPIO Pad Data Input Register (GPDI184)|8|RO|00h|
|15BCh|SIUL2 GPIO Pad Data Input Register (GPDI191)|8|RO|00h|
|15BDh|SIUL2 GPIO Pad Data Input Register (GPDI190)|8|RO|00h|
|15BEh|SIUL2 GPIO Pad Data Input Register (GPDI189)|8|RO|00h|
|15BFh|SIUL2 GPIO Pad Data Input Register (GPDI188)|8|RO|00h|
|15C0h|SIUL2 GPIO Pad Data Input Register (GPDI195)|8|RO|00h|
|15C1h|SIUL2 GPIO Pad Data Input Register (GPDI194)|8|RO|00h|
|15C2h|SIUL2 GPIO Pad Data Input Register (GPDI193)|8|RO|00h|
|15C3h|SIUL2 GPIO Pad Data Input Register (GPDI192)|8|RO|00h|
|15C4h|SIUL2 GPIO Pad Data Input Register (GPDI199)|8|RO|00h|
|15C5h|SIUL2 GPIO Pad Data Input Register (GPDI198)|8|RO|00h|
|15C6h|SIUL2 GPIO Pad Data Input Register (GPDI197)|8|RO|00h|
|15C7h|SIUL2 GPIO Pad Data Input Register (GPDI196)|8|RO|00h|
|15C8h|SIUL2 GPIO Pad Data Input Register (GPDI203)|8|RO|00h|
|15C9h|SIUL2 GPIO Pad Data Input Register (GPDI202)|8|RO|00h|
|15CAh|SIUL2 GPIO Pad Data Input Register (GPDI201)|8|RO|00h|
|15CBh|SIUL2 GPIO Pad Data Input Register (GPDI200)|8|RO|00h|
|15CCh|SIUL2 GPIO Pad Data Input Register (GPDI207)|8|RO|00h|
|15CDh|SIUL2 GPIO Pad Data Input Register (GPDI206)|8|RO|00h|
|15CEh|SIUL2 GPIO Pad Data Input Register (GPDI205)|8|RO|00h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

253 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|15CFh|SIUL2 GPIO Pad Data Input Register (GPDI204)|8|RO|00h|
|15D0h|SIUL2 GPIO Pad Data Input Register (GPDI211)|8|RO|00h|
|15D1h|SIUL2 GPIO Pad Data Input Register (GPDI210)|8|RO|00h|
|15D2h|SIUL2 GPIO Pad Data Input Register (GPDI209)|8|RO|00h|
|15D3h|SIUL2 GPIO Pad Data Input Register (GPDI208)|8|RO|00h|
|15D4h|SIUL2 GPIO Pad Data Input Register (GPDI215)|8|RO|00h|
|15D5h|SIUL2 GPIO Pad Data Input Register (GPDI214)|8|RO|00h|
|15D6h|SIUL2 GPIO Pad Data Input Register (GPDI213)|8|RO|00h|
|15D7h|SIUL2 GPIO Pad Data Input Register (GPDI212)|8|RO|00h|
|15D8h|SIUL2 GPIO Pad Data Input Register (GPDI219)|8|RO|00h|
|15D9h|SIUL2 GPIO Pad Data Input Register (GPDI218)|8|RO|00h|
|15DAh|SIUL2 GPIO Pad Data Input Register (GPDI217)|8|RO|00h|
|15DBh|SIUL2 GPIO Pad Data Input Register (GPDI216)|8|RO|00h|
|15DCh|SIUL2 GPIO Pad Data Input Register (GPDI223)|8|RO|00h|
|15DDh|SIUL2 GPIO Pad Data Input Register (GPDI222)|8|RO|00h|
|15DEh|SIUL2 GPIO Pad Data Input Register (GPDI221)|8|RO|00h|
|15DFh|SIUL2 GPIO Pad Data Input Register (GPDI220)|8|RO|00h|
|15E0h|SIUL2 GPIO Pad Data Input Register (GPDI227)|8|RO|00h|
|15E1h|SIUL2 GPIO Pad Data Input Register (GPDI226)|8|RO|00h|
|15E2h|SIUL2 GPIO Pad Data Input Register (GPDI225)|8|RO|00h|
|15E3h|SIUL2 GPIO Pad Data Input Register (GPDI224)|8|RO|00h|
|15E4h|SIUL2 GPIO Pad Data Input Register (GPDI231)|8|RO|00h|
|15E5h|SIUL2 GPIO Pad Data Input Register (GPDI230)|8|RO|00h|
|15E6h|SIUL2 GPIO Pad Data Input Register (GPDI229)|8|RO|00h|
|15E7h|SIUL2 GPIO Pad Data Input Register (GPDI228)|8|RO|00h|
|15E8h|SIUL2 GPIO Pad Data Input Register (GPDI235)|8|RO|00h|
|15E9h|SIUL2 GPIO Pad Data Input Register (GPDI234)|8|RO|00h|
|15EAh|SIUL2 GPIO Pad Data Input Register (GPDI233)|8|RO|00h|
|15EBh|SIUL2 GPIO Pad Data Input Register (GPDI232)|8|RO|00h|
|15EFh|SIUL2 GPIO Pad Data Input Register (GPDI236)|8|RO|00h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

254 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|1700h -<br>1704h|SIUL2 Parallel GPIO Pad Data Out Register (PGPDO0 - PGPDO3) <sup>1</sup>|16|RW|0000h|
|1706h|SIUL2 Parallel GPIO Pad Data Out Register (PGPDO2)|16|RW|0000h|
|1708h -<br>171Ah|SIUL2 Parallel GPIO Pad Data Out Register (PGPDO4 -<br>PGPDO13) <sup>1</sup>|16|RW|0000h|
|171Eh|SIUL2 Parallel GPIO Pad Data Out Register (PGPDO14)|16|RW|0000h|
|1740h -<br>1744h|SIUL2 Parallel GPIO Pad Data In Register (PGPDI0 - PGPDI3) <sup>1</sup>|16|RO|0000h|
|1746h|SIUL2 Parallel GPIO Pad Data In Register (PGPDI2)|16|RO|0000h|
|1748h -<br>175Ah|SIUL2 Parallel GPIO Pad Data In Register (PGPDI4 - PGPDI13) <sup>1</sup>|16|RO|0000h|
|175Eh|SIUL2 Parallel GPIO Pad Data In Register (PGPDI14)|16|RO|0000h|
|1780h -<br>1784h|SIUL2 Masked Parallel GPIO Pad Data Out Register (MPGPDO0 -<br>MPGPDO1)|32|WORZ|0000_0000h|
|1788h|SIUL2 Masked Parallel GPIO Pad Data Out Register (MPGPDO2)|32|WORZ|0000_0000h|
|178Ch -<br>17B4h|SIUL2 Masked Parallel GPIO Pad Data Out Register (MPGPDO3 -<br>MPGPDO13)|32|WORZ|0000_0000h|
|17B8h|SIUL2 Masked Parallel GPIO Pad Data Out Register (MPGPDO14)|32|WORZ|0000_0000h|



1. In this array, the index and offset values of the registers do not increment in direct alignment. For details, see the register description. 

### 9.4.2 SIUL2 MCU ID Register #1 (MIDR1) 

##### Offset 

|Register|Offset|
|---|---|
|MIDR1|4h|



##### Function 

This register holds identification information about the device. 

~~<mark>NOTE</mark>~~ 

This register supports only 32-bit accesses. Byte and half-word accesses are not supported. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

255 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||PRO|DUCT_L|INE_LETT|ER||||||PART|_NO|||||
|W|||||||||||||||||
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||Rese|rved|||||MAJOR|_MASK|||MINOR|_MASK||
|W|||||||||||||||||
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|



##### Fields 

|Field|Function|
|---|---|
|31-26|Product Line Letter|
|PRODUCT_LIN<br>E_LETTER|Identified the ASCII character in MCU Part Number. This field specifies the part number suffix, and needs<br>to be combined with MIDR1[PART_NO] to provide the full chip number.<br>0x0B K<br>This value is set at the factory and cannot be changed. All other values are reserved.|
|25-16<br>PART_NO|MCU Part Number<br>S32K311 - 0x137<br>S32K312 - 0x138<br>S32K314 - 0x13A|
||S32K322 - 0x142|
||S32K324 - 0x144|
||S32K328 - 0x148<br>S32K338 - 0x152<br>S32K342 - 0x156<br>S32K344 - 0x158<br>S32K348 - 0x15C<br>S32K358 - 0x166|
|15-8<br>—<br>7-4|Reserved<br>Major Mask Revision|
|MAJOR_MASK||
|3-0|Minor Mask Revision|
|MINOR_MASK||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

256 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

### 9.4.3 SIUL2 MCU ID Register #2 (MIDR2) 

##### Offset 

|Register|Offset|
|---|---|
|MIDR2|8h|



##### Function 

~~<mark>NOTE</mark>~~ 

This register supports only 32-bit accesses. Byte and half-word accesses are not supported. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/009_System_Integration_Unit_Lite2_-SIUL2-/S32K3XXRM_数据表.pdf-0257-09.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R TECHNOLOGY  TEMPERATURE  PACKAGE  FREQUENCY<br>W<br>Reset u u u u u u u u u u u u u u u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R FLASH_CODE  FLASH_DATA  FLASH_SIZE_DATA  FLASH_SIZE_CODE<br>W<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-29|Technology|
|TECHNOLOGY|Identifies the silicon technology.<br>001b - C40EFS3|
|28-26|Temperature|
|TEMPERATUR<br>E|Identifies the ambient temperature range.<br>100b - M = 125C|
|25-20|Package|
|PACKAGE|This field can by read by software to determine the package type that is used for the particular device.<br>00_0011b - 257-MAPBGA|
||10_0010b - 100-MAXQFP|
||10_0101b - 172-MAXQFP|
|19-16|Frequency|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

257 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|FREQUENCY|Identifies maximum core frequency. Qualified by Product Line Letter to provide wider range of<br>frequencies.<br>0011b - 120 MHz<br>0100b - 160 MHz<br>0101b - 240 MHz|
|15-14<br>FLASH_CODE|Flash Code<br>Identifies the location of Code Flash, if any, within the package.<br>10b - Monolithic|
|13-12<br>FLASH_DATA|Flash Data<br>Identifies the location of Data Flash, if any, within the package.<br>10b - Monolithic|
|11-8|Flash Size Data|
|FLASH_SIZE_D<br>ATA|Identifies the Flash (EE) memory size.<br>0000b - 64KB<br>0001b - 128KB<br>0010b - 256KB|
|7-0|Flash Size Code|
|FLASH_SIZE_C<br>ODE|Identifies the Flash (code) memory size.<br>0000_0010b - 512kB<br>0000_0100b - 1MB<br>0000_1000b - 2.00MB<br>0000_1100b - 3.00MB<br>0001_0000b - 4.00MB<br>0001_1000b - 6.00MB<br>0010_0000b - 8.00MB|



### 9.4.4 SIUL2 DMA/Interrupt Status Flag Register0 (DISR0) 

##### Offset 

|Register|Offset|
|---|---|
|DISR0|10h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

258 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Function 

DISR0 contains flag bits that record an event on the external IRQ pins. When an event as defined in IREER0 and IFEER0 occurs, the corresponding flag bit is set. The IRQ flag bit is set regardless of the state of the corresponding DIRER0[EIREn] bit. The IRQ flag bit remains set until you clear it or is cleared by servicing of a DMA request. The IRQ flag bits are cleared by writing a 1 to the bits. A write of 0 has no effect. 

This register supports 8-, 16-, and 32-bit accesses. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|EIF31|EIF30|EIF29|EIF28|EIF27|EIF26|EIF25|EIF24|EIF23|EIF22|EIF21|EIF20|EIF19|EIF18|EIF17|EIF16|
|W|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|EIF15|EIF14|EIF13|EIF12|EIF11|EIF10|EIF9|EIF8|EIF7|EIF6|EIF5|EIF4|EIF3|EIF2|EIF1|EIF0|
|W|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|External Interrupt Status Flag 31|
|EIF31|If enabled (DIRERR31 = 1) causes an interrupt.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER31 and IFEER31 has occurred.|
|30|External Interrupt Status Flag 30|
|EIF30|If enabled (DIRERR30 = 1) causes an interrupt.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER30 and IFEER30 has occurred.|
|29<br>EIF29|External Interrupt Status Flag 29<br>If enabled (DIRERR29 = 1) causes an interrupt.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER29 and IFEER29 has occurred.|
|28|External Interrupt Status Flag 28|
|EIF28|If enabled (DIRERR28 = 1) causes an interrupt.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

259 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER28 and IFEER28 has occurred.|
|---|---|
|27|External Interrupt Status Flag 27|
|EIF27|If enabled (DIRERR27 = 1) causes an interrupt.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER27 and IFEER27 has occurred.|
|26|External Interrupt Status Flag 26|
|EIF26|If enabled (DIRERR26 = 1) causes an interrupt.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER26 and IFEER26 has occurred.|
|25|External Interrupt Status Flag 25|
|EIF25|If enabled (DIRERR25 = 1) causes an interrupt.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER25 and IFEER25 has occurred.|
|24|External Interrupt Status Flag 24|
|EIF24|If enabled (DIRERR24 = 1) causes an interrupt.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER24 and IFEER24 has occurred.|
|23|External Interrupt Status Flag 23|
|EIF23|If enabled (DIRERR23 = 1) causes an interrupt.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER23 and IFEER23 has occurred.|
|22|External Interrupt Status Flag 22|
|EIF22|If enabled (DIRERR22 = 1) causes an interrupt.|
||This flag can be cleared only by writing 1. Writing 0 has no effect.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

260 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER22 and IFEER22 has occurred.|
|21|External Interrupt Status Flag 21|
|EIF21|If enabled (DIRERR21 = 1) causes an interrupt.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER21 and IFEER21 has occurred.|
|20|External Interrupt Status Flag 20|
|EIF20|If enabled (DIRERR20 = 1) causes an interrupt.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER20 and IFEER20 has occurred.|
|19|External Interrupt Status Flag 19|
|EIF19|If enabled (DIRERR19 = 1) causes an interrupt.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER19 and IFEER19 has occurred.|
|18|External Interrupt Status Flag 18|
|EIF18|If enabled (DIRERR18 = 1) causes an interrupt.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER18 and IFEER18 has occurred.|
|17|External Interrupt Status Flag 17|
|EIF17|If enabled (DIRERR17 = 1) causes an interrupt.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER17 and IFEER17 has occurred.|
|16|External Interrupt Status Flag 16|
|EIF16|If enabled (DIRERR16 = 1) causes an interrupt.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

261 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function<br>1b - An interrupt event as defined by IREER16 and IFEER16 has occurred.|
|---|---|
|15|External Interrupt Status Flag 15|
|EIF15|If enabled (DIRERR15 = 1) causes an interrupt or DMA request.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER15 and IFEER15 has occurred.|
|14|External Interrupt Status Flag 14|
|EIF14|If enabled (DIRERR14 = 1) causes an interrupt or DMA request.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER14 and IFEER14 has occurred.|
|13|External Interrupt Status Flag 13|
|EIF13|If enabled (DIRERR13 = 1) causes an interrupt or DMA request.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER13 and IFEER13 has occurred.|
|12|External Interrupt Status Flag 12|
|EIF12|If enabled (DIRERR12 = 1) causes an interrupt or DMA request.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER12 and IFEER12 has occurred.|
|11|External Interrupt Status Flag 11|
|EIF11|If enabled (DIRERR11 = 1) causes an interrupt or DMA request.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER11 and IFEER11 has occurred.|
|10|External Interrupt Status Flag 10|
|EIF10|If enabled (DIRERR10 = 1) causes an interrupt or DMA request.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER10 and IFEER10 has occurred.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

262 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field<br>9|Function<br>External Interrupt Status Flag 9|
|---|---|
|EIF9|If enabled (DIRERR9 = 1) causes an interrupt or DMA request.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER9 and IFEER9 has occurred.|
|8<br>EIF8|External Interrupt Status Flag 8<br>If enabled (DIRERR8 = 1) causes an interrupt or DMA request.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER8 and IFEER8 has occurred.|
|7|External Interrupt Status Flag 7|
|EIF7|If enabled (DIRERR7 = 1) causes an interrupt or DMA request.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER7 and IFEER7 has occurred.|
|6|External Interrupt Status Flag 6|
|EIF6|If enabled (DIRERR6 = 1) causes an interrupt or DMA request.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER6 and IFEER6 has occurred.|
|5|External Interrupt Status Flag 5|
|EIF5|If enabled (DIRERR5 = 1) causes an interrupt or DMA request.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER5 and IFEER5 has occurred.|
|4|External Interrupt Status Flag 4|
|EIF4|If enabled (DIRERR4 = 1) causes an interrupt or DMA request.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER4 and IFEER4 has occurred.|
|3|External Interrupt Status Flag 3<br>If enabled (DIRERR3 = 1) causes an interrupt or DMA request.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

263 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|EIF3|This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER3 and IFEER3 has occurred.|
|2<br>EIF2|External Interrupt Status Flag 2<br>If enabled (DIRERR2 = 1) causes an interrupt or DMA request.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER2 and IFEER2 has occurred.|
|1<br>EIF1|External Interrupt Status Flag 1<br>If enabled (DIRERR1 = 1) causes an interrupt or DMA request.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER1 and IFEER1 has occurred.|
|0<br>EIF0|External Interrupt Status Flag 0<br>If enabled (DIRERR0 = 1) causes an interrupt or DMA request.<br>This flag can be cleared only by writing 1. Writing 0 has no effect.<br>0b - No interrupt event has occurred on the pad.<br>1b - An interrupt event as defined by IREER0 and IFEER0 has occurred.|



### 9.4.5 SIUL2 DMA/Interrupt Request Enable Register0 (DIRER0) 

##### Offset 

|Register|Offset|
|---|---|
|DIRER0|18h|



##### Function 

DIRER0 enables the assertion of DMA or interrupt request to the interrupt controller if the corresponding DISR0[EIFn] bit is set. The type of request is determined by the corresponding DIRSR0[DIRSRn] bit. 

This register supports 8-, 16-, and 32-bit accesses. 

~~<mark>NOTE</mark>~~ 

Once DIRSR0 selects a DMA request, you cannot enable or disable it. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

264 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

|Diagra<br>Bits|m<br>31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|EIRE3<br>1|EIRE3<br>0|EIRE2<br>9|EIRE2<br>8|EIRE2<br>7|EIRE2<br>6|EIRE2<br>5|EIRE2<br>4|EIRE2<br>3|EIRE2<br>2|EIRE2<br>1|EIRE2<br>0|EIRE1<br>9|EIRE1<br>8|EIRE1<br>7|EIRE1<br>6|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|EIRE1<br>5|EIRE1<br>4|EIRE1<br>3|EIRE1<br>2|EIRE1<br>1|EIRE1<br>0|EIRE9|EIRE8|EIRE7|EIRE6|EIRE5|EIRE4|EIRE3|EIRE2|EIRE1|EIRE0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|External Interrupt Request Enable|
|EIRE31|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled<br>1b - Enabled|
|30|External Interrupt Request Enable|
|EIRE30|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled<br>1b - Enabled|
|29|External Interrupt Request Enable|
|EIRE29|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled<br>1b - Enabled|
|28|External Interrupt Request Enable|
|EIRE28|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled<br>1b - Enabled|
|27|External Interrupt Request Enable|
|EIRE27|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled<br>1b - Enabled|
|26|External Interrupt Request Enable|
|EIRE26|Enables or disables interrupt requests from the corresponding pin.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

265 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Disabled<br>1b - Enabled|
|25|External Interrupt Request Enable|
|EIRE25|Enables or disables interrupt requests from the corresponding pin.|
||0b - Disabled<br>1b - Enabled|
|24|External Interrupt Request Enable|
|EIRE24|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled<br>1b - Enabled|
|23|External Interrupt Request Enable|
|EIRE23|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled<br>1b - Enabled|
|22|External Interrupt Request Enable|
|EIRE22|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled<br>1b - Enabled|
|21|External Interrupt Request Enable|
|EIRE21|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled<br>1b - Enabled|
|20|External Interrupt Request Enable|
|EIRE20|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled<br>1b - Enabled|
|19|External Interrupt Request Enable|
|EIRE19|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled<br>1b - Enabled|
|18|External Interrupt Request Enable<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

266 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|EIRE18|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled<br>1b - Enabled|
|17|External Interrupt Request Enable|
|EIRE17|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled<br>1b - Enabled|
|16|External Interrupt Request Enable|
|EIRE16|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled<br>1b - Enabled|
|15|External Interrupt Request Enable|
|EIRE15|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled<br>1b - Enabled|
|14|External Interrupt Request Enable|
|EIRE14|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled<br>1b - Enabled|
|13|External Interrupt Request Enable|
|EIRE13|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled<br>1b - Enabled|
|12|External Interrupt Request Enable|
|EIRE12|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled<br>1b - Enabled|
|11|External Interrupt Request Enable|
|EIRE11|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled<br>1b - Enabled|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

267 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|10|External Interrupt Request Enable|
|EIRE10|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled<br>1b - Enabled|
|9<br>EIRE9|External Interrupt Request Enable<br>Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled<br>1b - Enabled|
|8|External Interrupt Request Enable|
|EIRE8|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled<br>1b - Enabled|
|7|External Interrupt Request Enable|
|EIRE7|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled<br>1b - Enabled|
|6|External Interrupt Request Enable|
|EIRE6|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled<br>1b - Enabled|
|5|External Interrupt Request Enable|
|EIRE5|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled<br>1b - Enabled|
|4|External Interrupt Request Enable|
|EIRE4|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled|
||1b - Enabled|
|3|External Interrupt Request Enable|
|EIRE3|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

268 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - Enabled|
|2|External Interrupt Request Enable|
|EIRE2|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled<br>1b - Enabled|
|1|External Interrupt Request Enable|
|EIRE1|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled|
||1b - Enabled|
|0|External Interrupt Request Enable|
|EIRE0|Enables or disables interrupt requests from the corresponding pin.<br>0b - Disabled|
||1b - Enabled|



### 9.4.6 SIUL2 DMA/Interrupt Request Select Register0 (DIRSR0) 

##### Offset 

|Register|Offset|
|---|---|
|DIRSR0|20h|



##### Function 

DIRSR0 selects between the DMA or interrupt request. The DIRSR0[DIRSRn] bit determines whether DMA or an interrupt request asserts the corresponding DISR0[EIFn] bit. 

This register supports 8-, 16-, and 32-bit accesses. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|DIRSR<br>31|DIRSR<br>30|DIRSR<br>29|DIRSR<br>28|DIRSR<br>27|DIRSR<br>26|DIRSR<br>25|DIRSR<br>24|DIRSR<br>23|DIRSR<br>22|DIRSR<br>21|DIRSR<br>20|DIRSR<br>19|DIRSR<br>18|DIRSR<br>17|DIRSR<br>16|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|DIRSR<br>15|DIRSR<br>14|DIRSR<br>13|DIRSR<br>12|DIRSR<br>11|DIRSR<br>10|DIRSR<br>9|DIRSR<br>8|DIRSR<br>7|DIRSR<br>6|DIRSR<br>5|DIRSR<br>4|DIRSR<br>3|DIRSR<br>2|DIRSR<br>1|DIRSR<br>0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

269 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Fields 

|Field|Function|
|---|---|
|31<br>DIRSR31|DMA/Interrupt Request Select Register<br>Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - Reserved|
|30<br>DIRSR30|DMA/Interrupt Request Select Register<br>Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - Reserved|
|29<br>DIRSR29|DMA/Interrupt Request Select Register<br>Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - Reserved|
|28<br>DIRSR28|DMA/Interrupt Request Select Register<br>Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - Reserved|
|27<br>DIRSR27|DMA/Interrupt Request Select Register<br>Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - Reserved|
|26<br>DIRSR26|DMA/Interrupt Request Select Register<br>Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - Reserved|
|25|DMA/Interrupt Request Select Register|
|DIRSR25|Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

270 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Interrupt request<br>1b - Reserved|
|24<br>DIRSR24|DMA/Interrupt Request Select Register<br>Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - Reserved|
|23<br>DIRSR23|DMA/Interrupt Request Select Register<br>Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - Reserved|
|22<br>DIRSR22|DMA/Interrupt Request Select Register<br>Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - Reserved|
|21|DMA/Interrupt Request Select Register|
|DIRSR21|Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - Reserved|
|20<br>DIRSR20|DMA/Interrupt Request Select Register<br>Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - Reserved|
|19|DMA/Interrupt Request Select Register|
|DIRSR19|Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - Reserved|
|18|DMA/Interrupt Request Select Register|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

271 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|DIRSR18|Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - Reserved|
|17<br>DIRSR17|DMA/Interrupt Request Select Register<br>Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - Reserved|
|16<br>DIRSR16|DMA/Interrupt Request Select Register<br>Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - Reserved|
|15<br>DIRSR15|DMA/Interrupt Request Select Register<br>Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - DMA request|
|14<br>DIRSR14|DMA/Interrupt Request Select Register<br>Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - DMA request|
|13<br>DIRSR13|DMA/Interrupt Request Select Register<br>Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - DMA request|
|12<br>DIRSR12|DMA/Interrupt Request Select Register<br>Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - DMA request|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

272 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Table continued from the previous page... 

|Field<br>11<br>DIRSR11|Function<br>DMA/Interrupt Request Select Register<br>Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - DMA request|
|---|---|
|10<br>DIRSR10|DMA/Interrupt Request Select Register<br>Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - DMA request|
|9<br>DIRSR9|DMA/Interrupt Request Select Register<br>Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - DMA request|
|8<br>DIRSR8|DMA/Interrupt Request Select Register<br>Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - DMA request|
|7<br>DIRSR7|DMA/Interrupt Request Select Register<br>Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - DMA request|
|6<br>DIRSR6|DMA/Interrupt Request Select Register<br>Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - DMA request|
|5|DMA/Interrupt Request Select Register|
|DIRSR5|Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

273 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Interrupt request<br>1b - DMA request|
|4<br>DIRSR4|DMA/Interrupt Request Select Register<br>Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - DMA request|
|3|DMA/Interrupt Request Select Register|
|DIRSR3|Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - DMA request|
|2<br>DIRSR2|DMA/Interrupt Request Select Register<br>Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - DMA request|
|1|DMA/Interrupt Request Select Register|
|DIRSR1|Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - DMA request|
|0<br>DIRSR0|DMA/Interrupt Request Select Register<br>Selects between DMA request or external interrupt request when an edge-triggered event occurs on the<br>corresponding pin.<br>0b - Interrupt request<br>1b - DMA request|



### 9.4.7 SIUL2 Interrupt Rising-Edge Event Enable Register 0 (IREER0) 

##### Offset 

|Register|Offset|
|---|---|
|IREER0|28h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

274 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Function 

IREER0 enables the rising-edge triggered events on the corresponding interrupt pads. 

This register supports 8-, 16-, and 32-bit accesses. 

~~<mark>NOTE</mark>~~ 

If both the IREE and IFEE bits are cleared for the same interrupt source, the interrupt status flag for the corresponding external interrupt will never be set. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|IREE3<br>1|IREE3<br>0|IREE2<br>9|IREE2<br>8|IREE2<br>7|IREE2<br>6|IREE2<br>5|IREE2<br>4|IREE2<br>3|IREE2<br>2|IREE2<br>1|IREE2<br>0|IREE1<br>9|IREE1<br>8|IREE1<br>7|IREE1<br>6|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|IREE1<br>5|IREE1<br>4|IREE1<br>3|IREE1<br>2|IREE1<br>1|IREE1<br>0|IREE9|IREE8|IREE7|IREE6|IREE5|IREE4|IREE3|IREE2|IREE1|IREE0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31<br>IREE31|Enables rising-edge events to set DISR0[EIF31].<br>0b - Disabled<br>1b - Enabled|
|30<br>IREE30|Enables rising-edge events to set DISR0[EIF30].<br>0b - Disabled<br>1b - Enabled|
|29<br>IREE29|Enables rising-edge events to set DISR0[EIF29].<br>0b - Disabled<br>1b - Enabled|
|28<br>IREE28|Enables rising-edge events to set DISR0[EIF28].<br>0b - Disabled<br>1b - Enabled|
|27<br>IREE27|Enables rising-edge events to set DISR0[EIF27].<br>0b - Disabled<br>1b - Enabled|
|26|Enables rising-edge events to set DISR0[EIF26].|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

275 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|IREE26|0b - Disabled<br>1b - Enabled|
|25|Enables rising-edge events to set DISR0[EIF25].|
|IREE25|0b - Disabled<br>1b - Enabled|
|24<br>IREE24|Enables rising-edge events to set DISR0[EIF24].<br>0b - Disabled<br>1b - Enabled|
|23|Enables rising-edge events to set DISR0[EIF23].|
|IREE23|0b - Disabled<br>1b - Enabled|
|22|Enables rising-edge events to set DISR0[EIF22].|
|IREE22|0b - Disabled<br>1b - Enabled|
|21|Enables rising-edge events to set DISR0[EIF21].|
|IREE21|0b - Disabled<br>1b - Enabled|
|20|Enables rising-edge events to set DISR0[EIF20].|
|IREE20|0b - Disabled<br>1b - Enabled|
|19<br>IREE19|Enables rising-edge events to set DISR0[EIF19].<br>0b - Disabled<br>1b - Enabled|
|18|Enables rising-edge events to set DISR0[EIF18].|
|IREE18|0b - Disabled<br>1b - Enabled|
|17|Enables rising-edge events to set DISR0[EIF17].|
|IREE17|0b - Disabled<br>1b - Enabled|
|16|Enables rising-edge events to set DISR0[EIF16].|
|IREE16|0b - Disabled<br>1b - Enabled<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

276 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|15|Enables rising-edge events to set DISR0[EIF15].|
|IREE15|0b - Disabled<br>1b - Enabled|
|14|Enables rising-edge events to set DISR0[EIF14].|
|IREE14|0b - Disabled<br>1b - Enabled|
|13|Enables rising-edge events to set DISR0[EIF13].|
|IREE13|0b - Disabled<br>1b - Enabled|
|12|Enables rising-edge events to set DISR0[EIF12].|
|IREE12|0b - Disabled<br>1b - Enabled|
|11|Enables rising-edge events to set DISR0[EIF11].|
|IREE11|0b - Disabled<br>1b - Enabled|
|10|Enables rising-edge events to set DISR0[EIF10].|
|IREE10|0b - Disabled<br>1b - Enabled|
|9<br>IREE9|Enables rising-edge events to set DISR0[EIF9].<br>0b - Disabled<br>1b - Enabled|
|8<br>IREE8|Enables rising-edge events to set DISR0[EIF8].<br>0b - Disabled<br>1b - Enabled|
|7|Enables rising-edge events to set DISR0[EIF7].|
|IREE7|0b - Disabled<br>1b - Enabled|
|6|Enables rising-edge events to set DISR0[EIF6].|
|IREE6|0b - Disabled<br>1b - Enabled|
|5<br>IREE5|Enables rising-edge events to set DISR0[EIF5].|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

277 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Disabled<br>1b - Enabled|
|4<br>IREE4|Enables rising-edge events to set DISR0[EIF4].<br>0b - Disabled<br>1b - Enabled|
|3<br>IREE3|Enables rising-edge events to set DISR0[EIF3].<br>0b - Disabled<br>1b - Enabled|
|2<br>IREE2|Enables rising-edge events to set DISR0[EIF2].<br>0b - Disabled<br>1b - Enabled|
|1<br>IREE1|Enables rising-edge events to set DISR0[EIF1].<br>0b - Disabled<br>1b - Enabled|
|0<br>IREE0|Enables rising-edge events to set DISR0[EIF0].<br>0b - Disabled|
||1b - Enabled|



### 9.4.8 SIUL2 Interrupt Falling-Edge Event Enable Register 0 (IFEER0) 

##### Offset 

|Register|Offset|
|---|---|
|IFEER0|30h|



##### Function 

IFEER0 enables falling-edge triggered events on the corresponding interrupt pads. 

This register supports 8-, 16-, and 32-bit accesses. 

~~<mark>NOTE</mark>~~ 

If both the IREE and IFEE bits are cleared for the same interrupt source, the interrupt status flag for the corresponding external interrupt will never be set. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

278 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

|Diagra<br>Bits|m<br>31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|IFEE3<br>1|IFEE3<br>0|IFEE2<br>9|IFEE2<br>8|IFEE2<br>7|IFEE2<br>6|IFEE2<br>5|IFEE2<br>4|IFEE2<br>3|IFEE2<br>2|IFEE2<br>1|IFEE2<br>0|IFEE1<br>9|IFEE1<br>8|IFEE1<br>7|IFEE1<br>6|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|IFEE1<br>5|IFEE1<br>4|IFEE1<br>3|IFEE1<br>2|IFEE1<br>1|IFEE1<br>0|IFEE9|IFEE8|IFEE7|IFEE6|IFEE5|IFEE4|IFEE3|IFEE2|IFEE1|IFEE0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31<br>IFEE31|Enables falling-edge events to set DISR0[EIF31].<br>0b - Disabled<br>1b - Enabled|
|30<br>IFEE30|Enables falling-edge events to set DISR0[EIF30].<br>0b - Disabled<br>1b - Enabled|
|29<br>IFEE29|Enables falling-edge events to set DISR0[EIF29].<br>0b - Disabled<br>1b - Enabled|
|28<br>IFEE28|Enables falling-edge events to set DISR0[EIF28].<br>0b - Disabled<br>1b - Enabled|
|27<br>IFEE27|Enables falling-edge events to set DISR0[EIF27].<br>0b - Disabled<br>1b - Enabled|
|26<br>IFEE26|Enables falling-edge events to set DISR0[EIF26].<br>0b - Disabled<br>1b - Enabled|
|25<br>IFEE25|Enables falling-edge events to set DISR0[EIF25].<br>0b - Disabled<br>1b - Enabled|
|24|Enables falling-edge events to set DISR0[EIF24].|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

279 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|IFEE24|0b - Disabled<br>1b - Enabled|
|23|Enables falling-edge events to set DISR0[EIF23].|
|IFEE23|0b - Disabled<br>1b - Enabled|
|22<br>IFEE22|Enables falling-edge events to set DISR0[EIF22].<br>0b - Disabled<br>1b - Enabled|
|21|Enables falling-edge events to set DISR0[EIF21].|
|IFEE21|0b - Disabled<br>1b - Enabled|
|20|Enables falling-edge events to set DISR0[EIF20].|
|IFEE20|0b - Disabled<br>1b - Enabled|
|19|Enables falling-edge events to set DISR0[EIF19].|
|IFEE19|0b - Disabled<br>1b - Enabled|
|18|Enables falling-edge events to set DISR0[EIF18].|
|IFEE18|0b - Disabled<br>1b - Enabled|
|17<br>IFEE17|Enables falling-edge events to set DISR0[EIF17].<br>0b - Disabled<br>1b - Enabled|
|16|Enables falling-edge events to set DISR0[EIF16].|
|IFEE16|0b - Disabled<br>1b - Enabled|
|15|Enables falling-edge events to set DISR0[EIF15].|
|IFEE15|0b - Disabled<br>1b - Enabled|
|14|Enables falling-edge events to set DISR0[EIF14].|
|IFEE14|0b - Disabled<br>1b - Enabled<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

280 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|13|Enables falling-edge events to set DISR0[EIF13].|
|IFEE13|0b - Disabled<br>1b - Enabled|
|12|Enables falling-edge events to set DISR0[EIF12].|
|IFEE12|0b - Disabled<br>1b - Enabled|
|11|Enables falling-edge events to set DISR0[EIF11].|
|IFEE11|0b - Disabled<br>1b - Enabled|
|10|Enables falling-edge events to set DISR0[EIF10].|
|IFEE10|0b - Disabled<br>1b - Enabled|
|9<br>IFEE9|Enables falling-edge events to set DISR0[EIF9].<br>0b - Disabled<br>1b - Enabled|
|8|Enables falling-edge events to set DISR0[EIF8].|
|IFEE8|0b - Disabled<br>1b - Enabled|
|7<br>IFEE7|Enables falling-edge events to set DISR0[EIF7].<br>0b - Disabled<br>1b - Enabled|
|6<br>IFEE6|Enables falling-edge events to set DISR0[EIF6].<br>0b - Disabled<br>1b - Enabled|
|5|Enables falling-edge events to set DISR0[EIF5].|
|IFEE5|0b - Disabled<br>1b - Enabled|
|4|Enables falling-edge events to set DISR0[EIF4].|
|IFEE4|0b - Disabled<br>1b - Enabled|
|3<br>IFEE3|Enables falling-edge events to set DISR0[EIF3].|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

281 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Disabled<br>1b - Enabled|
|2|Enables falling-edge events to set DISR0[EIF2].|
|IFEE2|0b - Disabled<br>1b - Enabled|
|1|Enables falling-edge events to set DISR0[EIF1].|
|IFEE1|0b - Disabled|
||1b - Enabled|
|0|Enables falling-edge events to set DISR0[EIF0].|
|IFEE0|0b - Disabled<br>1b - Enabled|



### 9.4.9 SIUL2 Interrupt Filter Enable Register 0 (IFER0) 

##### Offset 

|Register|Offset|
|---|---|
|IFER0|38h|



##### Function 

IFER0 enables a digital filter counter on the corresponding interrupt pads to filter out glitches on the inputs. This register supports 8-, 16-, and 32-bit accesses. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|IFE31|IFE30|IFE29|IFE28|IFE27|IFE26|IFE25|IFE24|IFE23|IFE22|IFE21|IFE20|IFE19|IFE18|IFE17|IFE16|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|IFE15|IFE14|IFE13|IFE12|IFE11|IFE10|IFE9|IFE8|IFE7|IFE6|IFE5|IFE4|IFE3|IFE2|IFE1|IFE0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

282 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Fields 

|Field|Function|
|---|---|
|31|Enables digital glitch filter on the interrupt pad input.|
|IFE31|0b - Disabled<br>1b - Enabled|
|30|Enables digital glitch filter on the interrupt pad input.|
|IFE30|0b - Disabled<br>1b - Enabled|
|29|Enables digital glitch filter on the interrupt pad input.|
|IFE29|0b - Disabled<br>1b - Enabled|
|28|Enables digital glitch filter on the interrupt pad input.|
|IFE28|0b - Disabled<br>1b - Enabled|
|27|Enables digital glitch filter on the interrupt pad input.|
|IFE27|0b - Disabled<br>1b - Enabled|
|26|Enables digital glitch filter on the interrupt pad input.|
|IFE26|0b - Disabled<br>1b - Enabled|
|25|Enables digital glitch filter on the interrupt pad input.|
|IFE25|0b - Disabled<br>1b - Enabled|
|24|Enables digital glitch filter on the interrupt pad input.|
|IFE24|0b - Disabled<br>1b - Enabled|
|23|Enables digital glitch filter on the interrupt pad input.|
|IFE23|0b - Disabled<br>1b - Enabled|
|22|Enables digital glitch filter on the interrupt pad input.|
|IFE22|0b - Disabled<br>1b - Enabled|
|21<br>IFE21|Enables digital glitch filter on the interrupt pad input.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

283 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Disabled<br>1b - Enabled|
|20|Enables digital glitch filter on the interrupt pad input.|
|IFE20|0b - Disabled<br>1b - Enabled|
|19<br>IFE19|Enables digital glitch filter on the interrupt pad input.<br>0b - Disabled<br>1b - Enabled|
|18|Enables digital glitch filter on the interrupt pad input.|
|IFE18|0b - Disabled<br>1b - Enabled|
|17|Enables digital glitch filter on the interrupt pad input.|
|IFE17|0b - Disabled<br>1b - Enabled|
|16|Enables digital glitch filter on the interrupt pad input.|
|IFE16|0b - Disabled<br>1b - Enabled|
|15|Enables digital glitch filter on the interrupt pad input.|
|IFE15|0b - Disabled<br>1b - Enabled|
|14<br>IFE14|Enables digital glitch filter on the interrupt pad input.<br>0b - Disabled<br>1b - Enabled|
|13|Enables digital glitch filter on the interrupt pad input.|
|IFE13|0b - Disabled<br>1b - Enabled|
|12|Enables digital glitch filter on the interrupt pad input.|
|IFE12|0b - Disabled<br>1b - Enabled|
|11|Enables digital glitch filter on the interrupt pad input.|
|IFE11|0b - Disabled<br>1b - Enabled<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

284 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|10|Enables digital glitch filter on the interrupt pad input.|
|IFE10|0b - Disabled<br>1b - Enabled|
|9|Enables digital glitch filter on the interrupt pad input.|
|IFE9|0b - Disabled<br>1b - Enabled|
|8<br>IFE8|Enables digital glitch filter on the interrupt pad input.<br>0b - Disabled<br>1b - Enabled|
|7<br>IFE7|Enables digital glitch filter on the interrupt pad input.<br>0b - Disabled<br>1b - Enabled|
|6<br>IFE6|Enables digital glitch filter on the interrupt pad input.<br>0b - Disabled<br>1b - Enabled|
|5<br>IFE5|Enables digital glitch filter on the interrupt pad input.<br>0b - Disabled<br>1b - Enabled|
|4|Enables digital glitch filter on the interrupt pad input.|
|IFE4|0b - Disabled<br>1b - Enabled|
|3|Enables digital glitch filter on the interrupt pad input.|
|IFE3|0b - Disabled<br>1b - Enabled|
|2|Enables digital glitch filter on the interrupt pad input.|
|IFE2|0b - Disabled<br>1b - Enabled|
|1|Enables digital glitch filter on the interrupt pad input.|
|IFE1|0b - Disabled|
||1b - Enabled|
|0|Enables digital glitch filter on the interrupt pad input.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

285 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|IFE0|0b - Disabled|
||1b - Enabled|



### 9.4.10 SIUL2 Interrupt Filter Maximum Counter Register (IFMCR0 - IFMCR31) 

##### Offset 

For a = 0 to 31: 

|Register|Offset|
|---|---|
|IFMCRa|40h + (a × 4h)|



##### Function 

IFMCRn registers configure the filter counter associated with each digital glitch filter. 

~~<mark>NOTE</mark>~~ These registers support only 32-bit accesses. Byte and half-word accesses are not supported. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||0|||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||0||||||||MAX|CNT||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-4<br>—|Reserved|
|3-0|Maximum Interrupt Filter Counter setting|
|MAXCNT|MAXCNT can be 0d to 15d.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

286 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||• A value of 0d, 1d, or 2d sets the filter as an all pass filter.|
||• A value of 3d to 15d sets the filter period to TCK Á MAXCNT + n Á TCK, where:<br>— n is 0, 1, 2, 3, or 4.|
||— TCK is the prescaled filter clock period, which is the IRC clock prescaled to the IFCP value<br>specified in IFCPR.|
||n accounts for the uncertainty factor in filter period calculation.|



### 9.4.11 SIUL2 Interrupt Filter Clock Prescaler Register (IFCPR) 

##### Offset 

|Register|Offset|
|---|---|
|IFCPR|C0h|



##### Function 

IFCPR configures the clock prescaler which selects the clock for all digital filters. A prescaler is applied to the input clock to SIUL2, which is the peripheral clock counter in the SIUL2. 

~~<mark>NOTE</mark>~~ This register supports only 32-bit accesses. Byte and half-word accesses are not supported. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/009_System_Integration_Unit_Lite2_-SIUL2-/S32K3XXRM_数据表.pdf-0287-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>IFCP<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function||
|---|---|---|
|31-4<br>—|Reserved|Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

287 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|3-0|Interrupt Filter Clock Prescaler setting|
|IFCP|Prescaled Filter Clock period is TIRCÁ (IFCP + 1), where:|
||• TIRCis the internal oscillator period.|
||• IFCP is 0 to 15.|



### 9.4.12 MUX0 EMIOS ENABLE 1 (MUX0_EMIOS_EN1) 

##### Offset 

|Register|Offset|
|---|---|
|MUX0_EMIOS_EN1|100h|



Function 

~~<mark>NOTE</mark>~~ 

This register is reserved for S32K3x4. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/009_System_Integration_Unit_Lite2_-SIUL2-/S32K3XXRM_数据表.pdf-0288-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R EMIO EMIO EMIO EMIO EMIO EMIO EMIO EMIO EMIO EMIO EMIO EMIO EMIO EMIO EMIO EMIO<br>W SFL... SFL... SFL... SFL... SFL... SFL... SFL... SFL... SFL... SFL... SFL... SFL... SFL... SFL... SFL... SFL...<br>Reset u u u u u u u u u u u u u u u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R EMIOS EMIOS EMIOS EMIOS EMIOS EMIOS EMIOS EMIOS<br>Reserved<br>W FL... FL... FL... FL... FL... FL... FL... FL...<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31|EMIOS0 Output Flag 15 Monitor Enable|
|EMIOSFLG15_<br>EN||
|30|EMIOS0 Output Flag 14 Monitor Enable|
|EMIOSFLG14_<br>EN||
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

288 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|29|EMIOS0 Output Flag 13 Monitor Enable|
|EMIOSFLG13_<br>EN||
|28|EMIOS0 Output Flag 12 Monitor Enable|
|EMIOSFLG12_<br>EN||
|27|EMIOS0 Output Flag 11 Monitor Enable|
|EMIOSFLG11_<br>EN||
|26|EMIOS0 Output Flag 10 Monitor Enable|
|EMIOSFLG10_<br>EN||
|25<br>EMIOSFLG9_E<br>N|EMIOS0 Output Flag 9 Monitor Enable|
|24|EMIOS0 Output Flag 8 Monitor Enable|
|EMIOSFLG8_E<br>N||
|23|EMIOS0 Output Flag 7 Monitor Enable|
|EMIOSFLG7_E<br>N||
|22|EMIOS0 Output Flag 6 Monitor Enable|
|EMIOSFLG6_E<br>N||
|21|EMIOS0 Output Flag 5 Monitor Enable|
|EMIOSFLG5_E<br>N||
|20|EMIOS0 Output Flag 4 Monitor Enable|
|EMIOSFLG4_E<br>N||
|19|EMIOS0 Output Flag 3 Monitor Enable|
|EMIOSFLG3_E<br>N||
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

289 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|18|EMIOS0 Output Flag 2 Monitor Enable|
|EMIOSFLG2_E<br>N||
|17|EMIOS0 Output Flag 1 Monitor Enable|
|EMIOSFLG1_E<br>N||
|16|EMIOS0 Output Flag 0 Monitor Enable|
|EMIOSFLG0_E<br>N||
|15-8<br>—|Reserved|
|7|EMIOS0 Output Flag 23 Monitor Enable|
|EMIOSFLG23_<br>EN||
|6|EMIOS0 Output Flag 22 Monitor Enable|
|EMIOSFLG22_<br>EN||
|5|EMIOS0 Output Flag 21 Monitor Enable|
|EMIOSFLG21_<br>EN||
|4|EMIOS0 Output Flag 20 Monitor Enable|
|EMIOSFLG20_<br>EN||
|3|EMIOS0 Output Flag 19 Monitor Enable|
|EMIOSFLG19_<br>EN||
|2|EMIOS0 Output Flag 18 Monitor Enable|
|EMIOSFLG18_<br>EN||
|1|EMIOS0 Output Flag 17 Monitor Enable|
|EMIOSFLG17_<br>EN||
|0|EMIOS0 Output Flag 16 Monitor Enable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

290 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Table continued from the previous page... 

|Field<br>Function|
|---|
|EMIOSFLG16_<br>EN|



### 9.4.13 MUX0 MISC ENABLE (MUX0_MISC_EN) 

##### Offset 

|Register|Offset|
|---|---|
|MUX0_MISC_EN|104h|



Function 

~~<mark>NOTE</mark>~~ 

This register is reserved for S32K3x4. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||Reserved|||BCTU<br>ADC...|BCTU<br>ADC...|BCTU<br>ADC...|BCTU<br>LIS...|BCTU<br>FIF...|BCTU<br>FIF...|BCTU<br>ADC...|BCTU<br>ADC...|BCTU<br>ADC...|BCTU<br>FIF...|BCTU<br>FIF...|
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||Res|erved||LPUA<br>RT3...|LPUA<br>RT2...|LPUA<br>RT1...|LPUA<br>RT0...|||Reserved|||ADC2<br>EOC...|ADC1<br>EOC...|ADC0<br>EOC...|
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|



##### Fields 

|Field|Function|
|---|---|
|31-27<br>—|Reserved|
|26|BCTU ADC2DR Interrupt Request Monitor Enable|
|BCTUADC2INT<br>_EN||
|25|BCTU ADC1DR Interrupt Request Monitor Enable|
|BCTUADC1INT<br>_EN||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

291 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|24|BCTU ADC0DR Interrupt Request Monitor Enable|
|BCTUADC0INT<br>_EN||
|23|BCTU Conversion List Interrupt Request Enable|
|BCTULISTINT_<br>EN||
|22|BCTU FIFO0 Interrupt Request Monitor Enable|
|BCTUFIFO1INT<br>_EN||
|21|BCTU FIFO0 Interrupt Request Monitor Enable|
|BCTUFIFO0INT<br>_EN||
|20|BCTU ADC2DR DMA Request Monitor Enable|
|BCTUADC2DM<br>A_EN||
|19|BCTU ADC1DR DMA Request Monitor Enable|
|BCTUADC1DM<br>A_EN||
|18|BCTU ADC0DR DMA Request Monitor Enable|
|BCTUADC0DM<br>A_EN||
|17|BCTU FIFO1 DMA Request Monitor Enable|
|BCTUFIFO1DM<br>A_EN||
|16<br>BCTUFIFO0DM<br>A_EN|BCTU FIFO0 DMA Request Monitor Enable|
|15-12<br>—|Reserved|
|11|LPUART3 Output Trigger Monitor Enable|
|LPUART3TRG_<br>EN||
|10|LPUART2 Output Trigger Monitor Enable<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

292 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|LPUART2TRG_<br>EN||
|9|LPUART1 Output Trigger Monitor Enable|
|LPUART1TRG_<br>EN||
|8|LPUART0 Output Trigger Monitor Enable|
|LPUART0TRG_<br>EN||
|7-3<br>—|Reserved|
|2|ADC2 End of Conversion Trigger Monitor|
|ADC2EOC_EN||
|1|ADC1 End of Conversion Trigger Monitor|
|ADC1EOC_EN||
|0|ADC0 End of Conversion Trigger Monitor|
|ADC0EOC_EN||



### 9.4.14 MUX1 EMIOS ENABLE (MUX1_EMIOS_EN ) 

##### Offset 

|Register|Offset|
|---|---|
|MUX1_EMIOS_EN|108h|



Function 

~~<mark>NOTE</mark>~~ 

This register is reserved for S32K3x4. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

293 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

|Diagra|m||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|R<br>W|EMIO<br>SFL...|EMIO<br>SFL...|EMIO<br>SFL...|EMIO<br>SFL...|EMIO<br>SFL...|EMIO<br>SFL...|EMIO<br>SFL...|EMIO<br>SFL...|EMIO<br>SFL...|EMIO<br>SFL...|EMIO<br>SFL...|EMIO<br>SFL...|EMIO<br>SFL...|EMIO<br>SFL...|EMIO<br>SFL...|EMIO<br>SFL...|
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||Rese|rved||||EMIOS<br>FL...|EMIOS<br>FL...|EMIOS<br>FL...|EMIOS<br>FL...|EMIOS<br>FL...|EMIOS<br>FL...|EMIOS<br>FL...|EMIOS<br>FL...|
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|



##### Fields 

|Field|Function|
|---|---|
|31|EMIOS0 Output Flag 15 Monitor Enable|
|EMIOSFLG15_<br>EN||
|30<br>EMIOSFLG14_<br>EN|EMIOS0 Output Flag 14 Monitor Enable|
|29<br>EMIOSFLG13_<br>EN|EMIOS0 Output Flag 13 Monitor Enable|
|28<br>EMIOSFLG12_<br>EN|EMIOS0 Output Flag 12 Monitor Enable|
|27<br>EMIOSFLG11_<br>EN|EMIOS0 Output Flag 11 Monitor Enable|
|26<br>EMIOSFLG10_<br>EN|EMIOS0 Output Flag 10 Monitor Enable|
|25<br>EMIOSFLG9_E<br>N|EMIOS0 Output Flag 9 Monitor Enable|
|24<br>EMIOSFLG8_E<br>N|EMIOS0 Output Flag 8 Monitor Enable<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

294 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|23|EMIOS0 Output Flag 7 Monitor Enable|
|EMIOSFLG7_E<br>N||
|22<br>EMIOSFLG6_E<br>N|EMIOS0 Output Flag 6 Monitor Enable|
|21|EMIOS0 Output Flag 5 Monitor Enable|
|EMIOSFLG5_E<br>N||
|20<br>EMIOSFLG4_E<br>N|EMIOS0 Output Flag 4 Monitor Enable|
|19|EMIOS0 Output Flag 3 Monitor Enable|
|EMIOSFLG3_E<br>N||
|18|EMIOS0 Output Flag 2 Monitor Enable|
|EMIOSFLG2_E<br>N||
|17<br>EMIOSFLG1_E<br>N|EMIOS0 Output Flag 1 Monitor Enable|
|16|EMIOS0 Output Flag 0 Monitor Enable|
|EMIOSFLG0_E<br>N||
|15-8<br>—|Reserved|
|7<br>EMIOSFLG23_<br>EN|EMIOS0 Output Flag 23 Monitor Enable|
|6|EMIOS0 Output Flag 22 Monitor Enable|
|EMIOSFLG22_<br>EN||
|5|EMIOS0 Output Flag 21 Monitor Enable<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

295 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|EMIOSFLG21_<br>EN||
|4|EMIOS0 Output Flag 20 Monitor Enable|
|EMIOSFLG20_<br>EN||
|3<br>EMIOSFLG19_<br>EN|EMIOS0 Output Flag 19 Monitor Enable|
|2|EMIOS0 Output Flag 18 Monitor Enable|
|EMIOSFLG18_<br>EN||
|1|EMIOS0 Output Flag 17 Monitor Enable|
|EMIOSFLG17_<br>EN||
|0|EMIOS0 Output Flag 16 Monitor Enable|
|EMIOSFLG16_<br>EN||



### 9.4.15 MUX1 MISC ENABLE (MUX1_MISC_EN) 

##### Offset 

|Register|Offset|
|---|---|
|MUX1_MISC_EN|10Ch|



Function 

~~<mark>NOTE</mark>~~ 

This register is reserved for S32K3x4. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

296 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

|Diagram<br>Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||Reserved|||BCTU<br>ADC...|BCTU<br>ADC...|BCTU<br>ADC...|BCTU<br>LIS...|BCTU<br>FIF...|BCTU<br>FIF...|BCTU<br>ADC...|BCTU<br>ADC...|BCTU<br>ADC...|BCTU<br>FIF...|BCTU<br>FIF...|
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||Res|erved||LPUA<br>RT3...|LPUA<br>RT2...|LPUA<br>RT1...|LPUA<br>RT0...|||Reserved|||ADC2<br>EOC...|ADC1<br>EOC...|ADC0<br>EOC...|
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|



##### Fields 

|Field|Function|
|---|---|
|31-27<br>—|Reserved|
|26<br>BCTUADC2INT<br>_EN|BCTU ADC2DR Interrupt Request Monitor Enable|
|25<br>BCTUADC1INT<br>_EN|BCTU ADC1DR Interrupt Request Monitor Enable|
|24<br>BCTUADC0INT<br>_EN|BCTU ADC0DR Interrupt Request Monitor Enable|
|23<br>BCTULISTINT_<br>EN|BCTU Conversion List Interrupt Request Enable|
|22<br>BCTUFIFO1INT<br>_EN|BCTU FIFO0 Interrupt Request Monitor Enable|
|21<br>BCTUFIFO0INT<br>_EN|BCTU FIFO0 Interrupt Request Monitor Enable|
|20<br>BCTUADC2DM<br>A_EN|BCTU ADC2DR DMA Request Monitor Enable<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

297 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|19|BCTU ADC1DR DMA Request Monitor Enable|
|BCTUADC1DM<br>A_EN||
|18|BCTU ADC0DR DMA Request Monitor Enable|
|BCTUADC0DM<br>A_EN||
|17|BCTU FIFO1 DMA Request Monitor Enable|
|BCTUFIFO1DM<br>A_EN||
|16|BCTU FIFO0 DMA Request Monitor Enable|
|BCTUFIFO0DM<br>A_EN||
|15-12<br>—|Reserved|
|11<br>LPUART3TRG_<br>EN|LPUART3 Output Trigger Monitor Enable|
|10|LPUART2 Output Trigger Monitor Enable|
|LPUART2TRG_<br>EN||
|9|LPUART1 Output Trigger Monitor Enable|
|LPUART1TRG_<br>EN||
|8|LPUART0 Output Trigger Monitor Enable|
|LPUART0TRG_<br>EN||
|7-3<br>—|Reserved|
|2|ADC2 End of Conversion Trigger Monitor|
|ADC2EOC_EN||
|1<br>ADC1EOC_EN|ADC1 End of Conversion Trigger Monitor|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

298 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|0|ADC0 End of Conversion Trigger Monitor|
|ADC0EOC_EN||



### 9.4.16 MUX2 EMIOS ENABLE (MUX2_EMIOS_EN) 

##### Offset 

|Register|Offset|
|---|---|
|MUX2_EMIOS_EN|110h|



##### Function 

~~<mark>NOTE</mark>~~ 

This register is reserved for S32K3x4, S32K310, S32K311, S32K312, S32K322, S32K341 and S32K342. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/009_System_Integration_Unit_Lite2_-SIUL2-/S32K3XXRM_数据表.pdf-0299-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R EMIO EMIO EMIO EMIO EMIO EMIO EMIO EMIO EMIO EMIO EMIO EMIO EMIO EMIO EMIO EMIO<br>W SFL... SFL... SFL... SFL... SFL... SFL... SFL... SFL... SFL... SFL... SFL... SFL... SFL... SFL... SFL... SFL...<br>Reset u u u u u u u u u u u u u u u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R EMIOS EMIOS EMIOS EMIOS EMIOS EMIOS EMIOS EMIOS<br>Reserved<br>W FL... FL... FL... FL... FL... FL... FL... FL...<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|EMIOS0 Output Flag 15 Monitor Enable|
|EMIOSFLG15_<br>EN||
|30|EMIOS0 Output Flag 14 Monitor Enable|
|EMIOSFLG14_<br>EN||
|29|EMIOS0 Output Flag 13 Monitor Enable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

299 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|EMIOSFLG13_<br>EN||
|28|EMIOS0 Output Flag 12 Monitor Enable|
|EMIOSFLG12_<br>EN||
|27|EMIOS0 Output Flag 11 Monitor Enable|
|EMIOSFLG11_<br>EN||
|26|EMIOS0 Output Flag 10 Monitor Enable|
|EMIOSFLG10_<br>EN||
|25|EMIOS0 Output Flag 9 Monitor Enable|
|EMIOSFLG9_E<br>N||
|24<br>EMIOSFLG8_E<br>N|EMIOS0 Output Flag 8 Monitor Enable|
|23|EMIOS0 Output Flag 7 Monitor Enable|
|EMIOSFLG7_E<br>N||
|22|EMIOS0 Output Flag 6 Monitor Enable|
|EMIOSFLG6_E<br>N||
|21|EMIOS0 Output Flag 5 Monitor Enable|
|EMIOSFLG5_E<br>N||
|20|EMIOS0 Output Flag 4 Monitor Enable|
|EMIOSFLG4_E<br>N||
|19|EMIOS0 Output Flag 3 Monitor Enable|
|EMIOSFLG3_E<br>N||
|18|EMIOS0 Output Flag 2 Monitor Enable<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

300 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|EMIOSFLG2_E<br>N||
|17|EMIOS0 Output Flag 1 Monitor Enable|
|EMIOSFLG1_E<br>N||
|16|EMIOS0 Output Flag 0 Monitor Enable|
|EMIOSFLG0_E<br>N||
|15-8<br>—|Reserved|
|7<br>EMIOSFLG23_<br>EN|EMIOS0 Output Flag 23 Monitor Enable|
|6|EMIOS0 Output Flag 22 Monitor Enable|
|EMIOSFLG22_<br>EN||
|5|EMIOS0 Output Flag 21 Monitor Enable|
|EMIOSFLG21_<br>EN||
|4|EMIOS0 Output Flag 20 Monitor Enable|
|EMIOSFLG20_<br>EN||
|3|EMIOS0 Output Flag 19 Monitor Enable|
|EMIOSFLG19_<br>EN||
|2|EMIOS0 Output Flag 18 Monitor Enable|
|EMIOSFLG18_<br>EN||
|1|EMIOS0 Output Flag 17 Monitor Enable|
|EMIOSFLG17_<br>EN||
|0|EMIOS0 Output Flag 16 Monitor Enable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

301 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Table continued from the previous page... 

|Field<br>Function|
|---|
|EMIOSFLG16_<br>EN|



### 9.4.17 MUX2 MISC ENABLE (MUX2_MISC_EN) 

##### Offset 

|Register|Offset|
|---|---|
|MUX2_MISC_EN|114h|



##### Function 

~~<mark>NOTE</mark>~~ 

This register is reserved for S32K3x4, S32K310, S32K311, S32K312, S32K322, S32K341 and S32K342. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||Reserved|||BCTU<br>ADC...|BCTU<br>ADC...|BCTU<br>ADC...|BCTU<br>LIS...|BCTU<br>FIF...|BCTU<br>FIF...|BCTU<br>ADC...|BCTU<br>ADC...|BCTU<br>ADC...|BCTU<br>FIF...|BCTU<br>FIF...|
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||Res|erved||LPUA<br>RT3...|LPUA<br>RT2...|LPUA<br>RT1...|LPUA<br>RT0...|||Reserved|||ADC2<br>EOC...|ADC1<br>EOC...|ADC0<br>EOC...|
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|



##### Fields 

|Field|Function|
|---|---|
|31-27<br>—|Reserved|
|26|BCTU ADC2DR Interrupt Request Monitor Enable|
|BCTUADC2INT<br>_EN||
|25|BCTU ADC1DR Interrupt Request Monitor Enable|
|BCTUADC1INT<br>_EN||
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

302 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|24|BCTU ADC0DR Interrupt Request Monitor Enable|
|BCTUADC0INT<br>_EN||
|23|BCTU Conversion List Interrupt Request Enable|
|BCTULISTINT_<br>EN||
|22|BCTU FIFO0 Interrupt Request Monitor Enable|
|BCTUFIFO1INT<br>_EN||
|21|BCTU FIFO0 Interrupt Request Monitor Enable|
|BCTUFIFO0INT<br>_EN||
|20|BCTU ADC2DR DMA Request Monitor Enable|
|BCTUADC2DM<br>A_EN||
|19|BCTU ADC1DR DMA Request Monitor Enable|
|BCTUADC1DM<br>A_EN||
|18|BCTU ADC0DR DMA Request Monitor Enable|
|BCTUADC0DM<br>A_EN||
|17|BCTU FIFO1 DMA Request Monitor Enable|
|BCTUFIFO1DM<br>A_EN||
|16<br>BCTUFIFO0DM<br>A_EN|BCTU FIFO0 DMA Request Monitor Enable|
|15-12<br>—|Reserved|
|11|LPUART3 Output Trigger Monitor Enable|
|LPUART3TRG_<br>EN||
|10|LPUART2 Output Trigger Monitor Enable<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

303 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|LPUART2TRG_<br>EN||
|9|LPUART1 Output Trigger Monitor Enable|
|LPUART1TRG_<br>EN||
|8|LPUART0 Output Trigger Monitor Enable|
|LPUART0TRG_<br>EN||
|7-3<br>—|Reserved|
|2|ADC2 End of Conversion Trigger Monitor|
|ADC2EOC_EN||
|1|ADC1 End of Conversion Trigger Monitor|
|ADC1EOC_EN||
|0|ADC0 End of Conversion Trigger Monitor|
|ADC0EOC_EN||



### 9.4.18 SIUL2 MCU ID Register #3 (MIDR3) 

##### Offset 

|Register|Offset||
|---|---|---|
|MIDR3|200h||
|unction|This register supports only 3|2-bit accesses. Byte and half-word accesses are not supported.<br>~~NOTE~~|



##### Function 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

304 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||PROD_F|AM_LET|||||||PROD_F|AM_NO|||||
|W|||||||||||||||||
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||PART_N|O_SUF||||0|||||SYS_RA|M_SIZE|||
|W|||||||||||||||||
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|



##### Fields 

|Field|Function|
|---|---|
|31-26<br>PROD_FAM_LE<br>T|Product Family Letter<br>Identifies the product family letter.<br>01_0011b - S|
|25-16<br>PROD_FAM_N<br>O|Product Family Number<br>Identifies the product family number.<br>00_0010_0000b - 32|
|15-10<br>PART_NO_SUF|Part Number Suffix<br>Describes the part number suffix.<br>00_0000b - None|
|9-6<br>—|Reserved|
|5-0<br>SYS_RAM_SIZ<br>E|System RAM Size<br>Total RAM size in SoC, including TCMs.<br>00_0010b - 128kB<br>00_0011b - 192kB<br>00_0100b - 256kB<br>00_0110b - 512kB|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

305 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

### 9.4.19 SIUL2 MCU ID Register #4 (MIDR4) 

##### Offset 

|Register|Offset|
|---|---|
|MIDR4|204h|



##### Function 

~~<mark>NOTE</mark>~~ This register supports only 32-bit accesses. Byte and half-word accesses are not supported. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/009_System_Integration_Unit_Lite2_-SIUL2-/S32K3XXRM_数据表.pdf-0306-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset u u u u u u u u u u u u u u u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 SEC_FET  EMAC_FET  CORE_PLAT_FET<br>W<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16<br>—|Reserved|
|15-14<br>—|Reserved|
|13-7<br>—|Reserved|
|6-5|Security Feature|
|SEC_FET|Security feature.|
||01b - HSE-B|
|4-3|Ethernet Feature|
|EMAC_FET|Ethernet feature.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

306 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||00b - No Ethernet|
||01b - Ethernet present|
|2-0|Core Platform Options Feature|
|CORE_PLAT_F<br>ET|Core platform options feature.<br>000b - Single core|
||001b - Dual core|
||010b - 1x lock-step core|
||011b - 1x lock-step core + 1 perf. core|
||100b - Triple core|



### 9.4.20 SIUL2 Multiplexed Signal Configuration Register (MSCR0 - MSCR236) 

##### Offset 

|Register|Offset|
|---|---|
|MSCR0|240h|
|MSCR1|244h|
|MSCR2|248h|
|MSCR3|24Ch|
|MSCR4|250h|
|MSCR5|254h|
|MSCR6|258h|
|MSCR7|25Ch|
|MSCR8|260h|
|MSCR9|264h|
|MSCR10|268h|
|MSCR11|26Ch|
|MSCR12|270h|
|MSCR13|274h|
|MSCR14|278h|
|MSCR15|27Ch|
|MSCR16|280h|
|MSCR17|284h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

307 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Register|Offset|
|---|---|
|MSCR18|288h|
|MSCR19|28Ch|
|MSCR20|290h|
|MSCR21|294h|
|MSCR22|298h|
|MSCR23|29Ch|
|MSCR24|2A0h|
|MSCR25|2A4h|
|MSCR26|2A8h|
|MSCR27|2ACh|
|MSCR28|2B0h|
|MSCR29|2B4h|
|MSCR30|2B8h|
|MSCR31|2BCh|
|MSCR32|2C0h|
|MSCR33|2C4h|
|MSCR34|2C8h|
|MSCR35|2CCh|
|MSCR36|2D0h|
|MSCR37|2D4h|
|MSCR40|2E0h|
|MSCR41|2E4h|
|MSCR42|2E8h|
|MSCR43|2ECh|
|MSCR44|2F0h|
|MSCR45|2F4h|
|MSCR46|2F8h|
|MSCR47|2FCh|
|MSCR48|300h|
|MSCR49|304h|
|MSCR50|308h|
|MSCR51|30Ch|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

308 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Register|Offset|
|---|---|
|MSCR52|310h|
|MSCR53|314h|
|MSCR54|318h|
|MSCR55|31Ch|
|MSCR56|320h|
|MSCR57|324h|
|MSCR58|328h|
|MSCR59|32Ch|
|MSCR60|330h|
|MSCR61|334h|
|MSCR62|338h|
|MSCR63|33Ch|
|MSCR64|340h|
|MSCR65|344h|
|MSCR66|348h|
|MSCR67|34Ch|
|MSCR68|350h|
|MSCR69|354h|
|MSCR70|358h|
|MSCR71|35Ch|
|MSCR72|360h|
|MSCR73|364h|
|MSCR74|368h|
|MSCR75|36Ch|
|MSCR76|370h|
|MSCR77|374h|
|MSCR78|378h|
|MSCR79|37Ch|
|MSCR80|380h|
|MSCR81|384h|
|MSCR82|388h|
|MSCR83|38Ch|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

309 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Register|Offset|
|---|---|
|MSCR84|390h|
|MSCR85|394h|
|MSCR86|398h|
|MSCR87|39Ch|
|MSCR88|3A0h|
|MSCR89|3A4h|
|MSCR90|3A8h|
|MSCR91|3ACh|
|MSCR92|3B0h|
|MSCR93|3B4h|
|MSCR94|3B8h|
|MSCR95|3BCh|
|MSCR96|3C0h|
|MSCR97|3C4h|
|MSCR98|3C8h|
|MSCR99|3CCh|
|MSCR100|3D0h|
|MSCR101|3D4h|
|MSCR102|3D8h|
|MSCR103|3DCh|
|MSCR104|3E0h|
|MSCR105|3E4h|
|MSCR106|3E8h|
|MSCR107|3ECh|
|MSCR108|3F0h|
|MSCR109|3F4h|
|MSCR110|3F8h|
|MSCR111|3FCh|
|MSCR112|400h|
|MSCR113|404h|
|MSCR114|408h|
|MSCR115|40Ch|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

310 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Register|Offset|
|---|---|
|MSCR116|410h|
|MSCR117|414h|
|MSCR118|418h|
|MSCR119|41Ch|
|MSCR120|420h|
|MSCR121|424h|
|MSCR122|428h|
|MSCR123|42Ch|
|MSCR124|430h|
|MSCR125|434h|
|MSCR126|438h|
|MSCR127|43Ch|
|MSCR128|440h|
|MSCR129|444h|
|MSCR130|448h|
|MSCR131|44Ch|
|MSCR132|450h|
|MSCR133|454h|
|MSCR134|458h|
|MSCR135|45Ch|
|MSCR136|460h|
|MSCR137|464h|
|MSCR138|468h|
|MSCR139|46Ch|
|MSCR140|470h|
|MSCR141|474h|
|MSCR142|478h|
|MSCR143|47Ch|
|MSCR144|480h|
|MSCR145|484h|
|MSCR146|488h|
|MSCR147|48Ch|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

311 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Register|Offset|
|---|---|
|MSCR148|490h|
|MSCR149|494h|
|MSCR150|498h|
|MSCR151|49Ch|
|MSCR152|4A0h|
|MSCR153|4A4h|
|MSCR154|4A8h|
|MSCR155|4ACh|
|MSCR156|4B0h|
|MSCR157|4B4h|
|MSCR158|4B8h|
|MSCR159|4BCh|
|MSCR160|4C0h|
|MSCR161|4C4h|
|MSCR162|4C8h|
|MSCR163|4CCh|
|MSCR164|4D0h|
|MSCR165|4D4h|
|MSCR166|4D8h|
|MSCR167|4DCh|
|MSCR168|4E0h|
|MSCR169|4E4h|
|MSCR170|4E8h|
|MSCR171|4ECh|
|MSCR172|4F0h|
|MSCR173|4F4h|
|MSCR174|4F8h|
|MSCR175|4FCh|
|MSCR176|500h|
|MSCR177|504h|
|MSCR178|508h|
|MSCR179|50Ch|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

312 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Register|Offset|
|---|---|
|MSCR180|510h|
|MSCR181|514h|
|MSCR182|518h|
|MSCR183|51Ch|
|MSCR184|520h|
|MSCR185|524h|
|MSCR186|528h|
|MSCR187|52Ch|
|MSCR188|530h|
|MSCR189|534h|
|MSCR190|538h|
|MSCR191|53Ch|
|MSCR192|540h|
|MSCR193|544h|
|MSCR194|548h|
|MSCR195|54Ch|
|MSCR196|550h|
|MSCR197|554h|
|MSCR198|558h|
|MSCR199|55Ch|
|MSCR200|560h|
|MSCR201|564h|
|MSCR202|568h|
|MSCR203|56Ch|
|MSCR204|570h|
|MSCR205|574h|
|MSCR206|578h|
|MSCR207|57Ch|
|MSCR208|580h|
|MSCR209|584h|
|MSCR210|588h|
|MSCR211|58Ch|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

313 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Table continued from the previous page... 

|Register|Offset|
|---|---|
|MSCR212|590h|
|MSCR213|594h|
|MSCR214|598h|
|MSCR215|59Ch|
|MSCR216|5A0h|
|MSCR217|5A4h|
|MSCR218|5A8h|
|MSCR219|5ACh|
|MSCR220|5B0h|
|MSCR221|5B4h|
|MSCR222|5B8h|
|MSCR223|5BCh|
|MSCR224|5C0h|
|MSCR225|5C4h|
|MSCR226|5C8h|
|MSCR227|5CCh|
|MSCR228|5D0h|
|MSCR229|5D4h|
|MSCR230|5D8h|
|MSCR231|5DCh|
|MSCR232|5E0h|
|MSCR233|5E4h|
|MSCR234|5E8h|
|MSCR235|5ECh|
|MSCR236|5F0h|



##### Function 

MSCRn registers select the source signal connected to the register's associated destination, which is a chip output pin or a chip pin that can be configured as an output. 

MSCRn also specifies the electrical properties of the associated pin. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

314 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/009_System_Integration_Unit_Lite2_-SIUL2-/S32K3XXRM_数据表.pdf-0315-02.png)


<!-- Start of picture text -->
Destination (module port) Internal connections<br>Port (input)<br>Input<br>Module 0<br>buffer<br>Pin a<br>Port (output)<br>Module-port IMCR Input<br>buffer<br>Pin b<br>Chip-pin MSCR<br>Port (output) Output<br>buffer<br>Module x<br>Port (output)<br>Destination (chip pin)<br><!-- End of picture text -->

Figure 19. MSCR and IMCR port and pin connection 

For chip-pin MSCR assignments and pin types, see the IOMUX file attached to this document. 

~~<mark>NOTE</mark>~~ 

- MSCRn registers support only 32-bit accesses. Byte and half-word write accesses are not supported. 

- MSCRn registers must be configured only during application initialization and must not be modified during application runtime. 

- Accessing a reserved MSCRn register generates a transfer error. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/009_System_Integration_Unit_Lite2_-SIUL2-/S32K3XXRM_数据表.pdf-0315-09.png)


<!-- Start of picture text -->
Diagram<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/009_System_Integration_Unit_Lite2_-SIUL2-/S32K3XXRM_数据表.pdf-0315-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0 0<br>OBE  IBE  INV  PKE<br>W<br>Reset See Register reset values.<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 0 0 0<br>SRC  PUE  PUS  DSE  IFE  SMC  SSS_2  SSS_1  SSS_0<br>W<br>Reset See Register reset values.<br><!-- End of picture text -->

##### Register reset values 

|Register|Reset value|
|---|---|
|MSCR0–MSCR3|0000_0000h|
|MSCR4|0008_2827h|
|MSCR5–MSCR9|0000_0000h|
|MSCR10|0000_0127h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

315 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Table continued from the previous page... 

|Register|Reset value|
|---|---|
|MSCR11|0000_0000h|
|MSCR12|0000_0003h|
|MSCR13–MSCR65|0000_0000h|
|MSCR38–MSCR39|Register not supported|
|MSCR66–MSCR67|0000_4000h|
|MSCR68|0008_2000h|
|MSCR69|0008_2800h|
|MSCR70–MSCR75|0000_0000h|
|MSCR76|0000_4000h|
|MSCR77–MSCR79|0000_0000h|
|MSCR80|0000_4000h|
|MSCR81–MSCR100|0000_0000h|
|MSCR101–MSCR103|0000_4000h|
|MSCR104–MSCR105|0000_0000h|
|MSCR106–MSCR108|0000_4000h|
|MSCR109–MSCR135|0000_0000h|
|MSCR136|0000_4000h|
|MSCR137–MSCR219|0000_0000h|
|MSCR220–MSCR236|0001_0000h|



##### Fields 

|Field|Function|
|---|---|
|31-22<br>—|Reserved|
|21|GPIO Output Buffer Enable|
|OBE|Applies only to digital pins. Otherwise this bit is reserved.|
||0b - Output driver disabled|
||1b - Output driver enabled|
|20<br>—|Reserved|
|19|Input Buffer Enable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

316 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|IBE|Used only when the associated destination is a chip pin. Enables the associated pin's input buffer.<br>0b - Disabled<br>1b - Enabled|
|18<br>—|Reserved|
|17<br>INV|Invert<br>Inverts the signal selected by SSS before transmitting it to the associated destination (chip pin or module<br>port).<br>0b - Don't invert<br>1b - Invert|
|16|Pad keeping enable|
|PKE|Pad keeping enable<br>0b - Disabled<br>1b - Enabled|
|15<br>—|Reserved|
|14<br>SRC|Slew Rate Control<br>0b - Fastest setting<br>1b - Slowest setting|
|13|Pull Enable|
|PUE|Enables the pull function. Used only when the associated destination is a chip pin.<br>0b - Disabled<br>1b - Enabled|
|12<br>—|Reserved|
|11|Pull Select|
|PUS|Determines whether the pull function is a pullup or pulldown when the pull function is enabled by the<br>PUE field. Used only when the associated destination is a chip pin.<br>0b - Pull down<br>1b - Pull up|
|10-9|Reserved<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

317 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/009_System_Integration_Unit_Lite2_-SIUL2-/S32K3XXRM_数据表.pdf-0318-02.png)


<!-- Start of picture text -->
Table continued from the previous page...<br>Field Function<br>—<br>8 DSE<br>DSE Drive strength enable<br>0b - Disabled<br>1b - Enabled<br>7 Reserved<br>—<br>6 IFE<br>IFE Input filter enable<br>  NOTE<br>This field is supported for RESET pad only (PTA5).<br>0b - Disabled<br>1b - Enabled<br>5 Safe Mode Control<br>SMC Used only when the associated destination is a chip pin. Specifies whether the chip disables the pin's<br>output buffer when the chip enters Safe mode.<br>0b - Disable (The output buffer returns to its previous state when the chip leaves Safe mode.)<br>1b - Don't disable<br>4-3 Reserved<br>—<br>2 Source Signal Select_2<br>SSS_2 Selects a function for the pad. Refer to “SSS” column of the ‘IO Signal Table' tab of the IOMUX<br>spreadsheet attachment.<br>1 Source Signal Select_1<br>SSS_1 Selects a function for the pad. Refer to “SSS” column of the ‘IO Signal Table' tab of the IOMUX<br>spreadsheet attachment.<br>0 Source Signal Select_0<br>SSS_0 Selects a function for the pad. Refer to “SSS” column of the ‘IO Signal Table' tab of the IOMUX<br>spreadsheet attachment.<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

318 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

### 9.4.21 SIUL2 Input Multiplexed Signal Configuration Register (IMCR0 - IMCR440) 

##### Offset 

|Register|Offset|
|---|---|
|IMCR0|A40h|
|IMCR1|A44h|
|IMCR2|A48h|
|IMCR3|A4Ch|
|IMCR4|A50h|
|IMCR5|A54h|
|IMCR16|A80h|
|IMCR17|A84h|
|IMCR18|A88h|
|IMCR19|A8Ch|
|IMCR20|A90h|
|IMCR21|A94h|
|IMCR22|A98h|
|IMCR23|A9Ch|
|IMCR24|AA0h|
|IMCR25|AA4h|
|IMCR26|AA8h|
|IMCR27|AACh|
|IMCR28|AB0h|
|IMCR29|AB4h|
|IMCR30|AB8h|
|IMCR31|ABCh|
|IMCR32|AC0h|
|IMCR33|AC4h|
|IMCR34|AC8h|
|IMCR35|ACCh|
|IMCR36|AD0h|
|IMCR37|AD4h|
|IMCR38|AD8h|
|IMCR39|ADCh|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

319 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Register|Offset|
|---|---|
|IMCR40|AE0h|
|IMCR41|AE4h|
|IMCR42|AE8h|
|IMCR43|AECh|
|IMCR44|AF0h|
|IMCR45|AF4h|
|IMCR46|AF8h|
|IMCR47|AFCh|
|IMCR48|B00h|
|IMCR49|B04h|
|IMCR50|B08h|
|IMCR51|B0Ch|
|IMCR52|B10h|
|IMCR53|B14h|
|IMCR54|B18h|
|IMCR55|B1Ch|
|IMCR56|B20h|
|IMCR57|B24h|
|IMCR58|B28h|
|IMCR59|B2Ch|
|IMCR60|B30h|
|IMCR61|B34h|
|IMCR62|B38h|
|IMCR63|B3Ch|
|IMCR64|B40h|
|IMCR65|B44h|
|IMCR66|B48h|
|IMCR67|B4Ch|
|IMCR68|B50h|
|IMCR69|B54h|
|IMCR70|B58h|
|IMCR71|B5Ch|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

320 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Register|Offset|
|---|---|
|IMCR80|B80h|
|IMCR81|B84h|
|IMCR82|B88h|
|IMCR83|B8Ch|
|IMCR84|B90h|
|IMCR85|B94h|
|IMCR86|B98h|
|IMCR87|B9Ch|
|IMCR88|BA0h|
|IMCR89|BA4h|
|IMCR90|BA8h|
|IMCR91|BACh|
|IMCR92|BB0h|
|IMCR93|BB4h|
|IMCR94|BB8h|
|IMCR95|BBCh|
|IMCR96|BC0h|
|IMCR97|BC4h|
|IMCR98|BC8h|
|IMCR99|BCCh|
|IMCR100|BD0h|
|IMCR101|BD4h|
|IMCR102|BD8h|
|IMCR103|BDCh|
|IMCR112|C00h|
|IMCR113|C04h|
|IMCR114|C08h|
|IMCR115|C0Ch|
|IMCR116|C10h|
|IMCR117|C14h|
|IMCR118|C18h|
|IMCR119|C1Ch|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

321 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Register|Offset|
|---|---|
|IMCR120|C20h|
|IMCR121|C24h|
|IMCR122|C28h|
|IMCR123|C2Ch|
|IMCR124|C30h|
|IMCR125|C34h|
|IMCR126|C38h|
|IMCR127|C3Ch|
|IMCR128|C40h|
|IMCR129|C44h|
|IMCR130|C48h|
|IMCR131|C4Ch|
|IMCR132|C50h|
|IMCR133|C54h|
|IMCR134|C58h|
|IMCR135|C5Ch|
|IMCR144|C80h|
|IMCR145|C84h|
|IMCR146|C88h|
|IMCR147|C8Ch|
|IMCR148|C90h|
|IMCR149|C94h|
|IMCR152|CA0h|
|IMCR153|CA4h|
|IMCR154|CA8h|
|IMCR155|CACh|
|IMCR156|CB0h|
|IMCR157|CB4h|
|IMCR158|CB8h|
|IMCR159|CBCh|
|IMCR160|CC0h|
|IMCR161|CC4h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

322 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Register|Offset|
|---|---|
|IMCR162|CC8h|
|IMCR163|CCCh|
|IMCR164|CD0h|
|IMCR165|CD4h|
|IMCR166|CD8h|
|IMCR167|CDCh|
|IMCR168|CE0h|
|IMCR169|CE4h|
|IMCR170|CE8h|
|IMCR171|CECh|
|IMCR172|CF0h|
|IMCR173|CF4h|
|IMCR174|CF8h|
|IMCR175|CFCh|
|IMCR176|D00h|
|IMCR177|D04h|
|IMCR178|D08h|
|IMCR179|D0Ch|
|IMCR180|D10h|
|IMCR181|D14h|
|IMCR182|D18h|
|IMCR183|D1Ch|
|IMCR184|D20h|
|IMCR185|D24h|
|IMCR186|D28h|
|IMCR187|D2Ch|
|IMCR188|D30h|
|IMCR189|D34h|
|IMCR190|D38h|
|IMCR191|D3Ch|
|IMCR192|D40h|
|IMCR193|D44h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

323 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Register|Offset|
|---|---|
|IMCR194|D48h|
|IMCR195|D4Ch|
|IMCR196|D50h|
|IMCR197|D54h|
|IMCR198|D58h|
|IMCR199|D5Ch|
|IMCR200|D60h|
|IMCR201|D64h|
|IMCR202|D68h|
|IMCR211|D8Ch|
|IMCR212|D90h|
|IMCR213|D94h|
|IMCR214|D98h|
|IMCR215|D9Ch|
|IMCR216|DA0h|
|IMCR217|DA4h|
|IMCR218|DA8h|
|IMCR219|DACh|
|IMCR220|DB0h|
|IMCR221|DB4h|
|IMCR222|DB8h|
|IMCR223|DBCh|
|IMCR224|DC0h|
|IMCR225|DC4h|
|IMCR226|DC8h|
|IMCR227|DCCh|
|IMCR228|DD0h|
|IMCR229|DD4h|
|IMCR230|DD8h|
|IMCR231|DDCh|
|IMCR232|DE0h|
|IMCR233|DE4h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

324 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Register|Offset|
|---|---|
|IMCR234|DE8h|
|IMCR235|DECh|
|IMCR236|DF0h|
|IMCR237|DF4h|
|IMCR238|DF8h|
|IMCR239|DFCh|
|IMCR240|E00h|
|IMCR241|E04h|
|IMCR242|E08h|
|IMCR243|E0Ch|
|IMCR244|E10h|
|IMCR245|E14h|
|IMCR246|E18h|
|IMCR247|E1Ch|
|IMCR248|E20h|
|IMCR249|E24h|
|IMCR250|E28h|
|IMCR251|E2Ch|
|IMCR252|E30h|
|IMCR253|E34h|
|IMCR254|E38h|
|IMCR255|E3Ch|
|IMCR256|E40h|
|IMCR257|E44h|
|IMCR258|E48h|
|IMCR259|E4Ch|
|IMCR260|E50h|
|IMCR261|E54h|
|IMCR262|E58h|
|IMCR263|E5Ch|
|IMCR264|E60h|
|IMCR265|E64h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

325 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Register|Offset|
|---|---|
|IMCR266|E68h|
|IMCR267|E6Ch|
|IMCR268|E70h|
|IMCR289|EC4h|
|IMCR290|EC8h|
|IMCR291|ECCh|
|IMCR292|ED0h|
|IMCR293|ED4h|
|IMCR294|ED8h|
|IMCR295|EDCh|
|IMCR296|EE0h|
|IMCR297|EE4h|
|IMCR298|EE8h|
|IMCR299|EECh|
|IMCR300|EF0h|
|IMCR301|EF4h|
|IMCR302|EF8h|
|IMCR303|EFCh|
|IMCR304|F00h|
|IMCR305|F04h|
|IMCR306|F08h|
|IMCR307|F0Ch|
|IMCR308|F10h|
|IMCR309|F14h|
|IMCR315|F2Ch|
|IMCR316|F30h|
|IMCR317|F34h|
|IMCR318|F38h|
|IMCR319|F3Ch|
|IMCR320|F40h|
|IMCR321|F44h|
|IMCR322|F48h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

326 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Register|Offset|
|---|---|
|IMCR323|F4Ch|
|IMCR324|F50h|
|IMCR325|F54h|
|IMCR343|F9Ch|
|IMCR344|FA0h|
|IMCR345|FA4h|
|IMCR346|FA8h|
|IMCR347|FACh|
|IMCR348|FB0h|
|IMCR349|FB4h|
|IMCR350|FB8h|
|IMCR351|FBCh|
|IMCR352|FC0h|
|IMCR353|FC4h|
|IMCR354|FC8h|
|IMCR355|FCCh|
|IMCR356|FD0h|
|IMCR357|FD4h|
|IMCR358|FD8h|
|IMCR359|FDCh|
|IMCR360|FE0h|
|IMCR361|FE4h|
|IMCR362|FE8h|
|IMCR363|FECh|
|IMCR364|FF0h|
|IMCR365|FF4h|
|IMCR366|FF8h|
|IMCR367|FFCh|
|IMCR368|1000h|
|IMCR369|1004h|
|IMCR370|1008h|
|IMCR371|100Ch|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

327 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Register|Offset|
|---|---|
|IMCR372|1010h|
|IMCR373|1014h|
|IMCR374|1018h|
|IMCR375|101Ch|
|IMCR376|1020h|
|IMCR377|1024h|
|IMCR378|1028h|
|IMCR389|1054h|
|IMCR398|1078h|
|IMCR399|107Ch|
|IMCR409|10A4h|
|IMCR410|10A8h|
|IMCR411|10ACh|
|IMCR412|10B0h|
|IMCR413|10B4h|
|IMCR414|10B8h|
|IMCR415|10BCh|
|IMCR416|10C0h|
|IMCR417|10C4h|
|IMCR418|10C8h|
|IMCR419|10CCh|
|IMCR420|10D0h|
|IMCR421|10D4h|
|IMCR422|10D8h|
|IMCR423|10DCh|
|IMCR424|10E0h|
|IMCR425|10E4h|
|IMCR426|10E8h|
|IMCR427|10ECh|
|IMCR428|10F0h|
|IMCR429|10F4h|
|IMCR430|10F8h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

328 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Table continued from the previous page... 

|Register|Offset|
|---|---|
|IMCR431|10FCh|
|IMCR432|1100h|
|IMCR433|1104h|
|IMCR434|1108h|
|IMCR437|1114h|
|IMCR440|1120h|



##### Function 

IMCRn registers select the source signal connected to the register's associated destination, which is an internal module port that is an input port or can be configured as an input. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/009_System_Integration_Unit_Lite2_-SIUL2-/S32K3XXRM_数据表.pdf-0329-06.png)


<!-- Start of picture text -->
Destination (module port) Internal connections<br>Port (input)<br>Input<br>Module 0<br>buffer<br>Pin a<br>Port (output)<br>Module-port IMCR Input<br>buffer<br>Pin b<br>Chip-pin MSCR<br>Port (output) Output<br>buffer<br>Module x<br>Port (output)<br>Destination (chip pin)<br><!-- End of picture text -->

Figure 20. MSCR and IMCR port and pin connection 

For IMCR assignments and field values, see the IOMUX file attached to this document. 

~~<mark>NOTE</mark>~~ 

- IMCRn registers support only 32-bit accesses. Byte and half-word write accesses are not supported. 

- IMCRn registers must be configured only during application initialization and must not be modified during application runtime. 

- Accessing a reserved IMCRn register generates a transfer error. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

329 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/009_System_Integration_Unit_Lite2_-SIUL2-/S32K3XXRM_数据表.pdf-0330-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>SSS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-4|Reserved|
|—||
|3-0|Source Signal Select|
|SSS|Selects which source signal is connected to the associated destination (chip pin).|



### 9.4.22 SIUL2 GPIO Pad Data Output Register (GPDO0 - GPDO236) 

##### Offset 

For n = 0 to 37; n = 40 to 236: 

|Register|Offset|
|---|---|
|GPDOn|1300h + (n + 3 - 2 × (n mod 4))|



##### Function 

Each GPDOn register sets or clears a single GPIO pad with a byte access. 

These registers support 8-, 16-, and 32-bit accesses. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

330 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/009_System_Integration_Unit_Lite2_-SIUL2-/S32K3XXRM_数据表.pdf-0331-03.png)


<!-- Start of picture text -->
Bits 7 6 5 4 3 2 1 0<br>R 0<br>PDO_n<br>W<br>Reset 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/009_System_Integration_Unit_Lite2_-SIUL2-/S32K3XXRM_数据表.pdf-0331-05.png)


<!-- Start of picture text -->
Field Function<br>7-1 Reserved<br>—<br>0 Pad Data Out<br>PDO_n Stores the data to be driven out on the external GPIO pad controlled by this register when the pad is<br>configured as an output.<br>PDO_n represents PDO[n], where n is the instance of the register.<br>0b - Pad Data Out Low. Logic low value<br>1b - Pad Data Out High. Logic high value<br><!-- End of picture text -->

### 9.4.23 SIUL2 GPIO Pad Data Input Register (GPDI0 - GPDI236) 

##### Offset 

For n = 0 to 37; n = 40 to 236: 

|Register|Offset|
|---|---|
|GPDIn|1500h + (n + 3 - 2 × (n mod 4))|



##### Function 

Each GPDIn register reads the GPIO pad data with a byte access. 

These registers support 8-, 16-, and 32-bit accesses. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

331 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/009_System_Integration_Unit_Lite2_-SIUL2-/S32K3XXRM_数据表.pdf-0332-03.png)


<!-- Start of picture text -->
Bits 7 6 5 4 3 2 1 0<br>R 0 PDI_n<br>W<br>Reset 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|7-1<br>—|Reserved|
|0|Pad Data In|
|PDI_n|Stores the value of the external GPIO pad associated with this register.|
||PDI_n represents PDI[n], where n is the instance of the register.|
||0b - Pad Data In Low. Logic low|
||1b - Pad Data In High. Logic high|



### 9.4.24 SIUL2 Parallel GPIO Pad Data Out Register (PGPDO0 - PGPDO3) 

##### Offset 

|Register|Offset|
|---|---|
|PGPDO1|1700h|
|PGPDO0|1702h|
|PGPDO3|1704h|



##### Function 

Each PGPDOn register sets or clears the respective pads of the chip. 

PGPDOn registers can set the values of all output pins assigned to a chip port with a single 16-bit register write, while the GPDOn registers set the value on a specific pin with byte writes. 

Each bit writes or reads the data register that stores the value to be driven on the pad in output mode. Access to this register location is coherent with access to the bit-wise GPDOn. 

For a given PGPDOx[PPDOy] where x is the register instance index and y is the field index, the following equation shows the equivalent GPDOn[PDO_n] bit: 

PGPDOx[PPDOy] = GPDO(x Á 16) + (15 - y)[PDO_(x Á 16) + (15 - y)] 

Some examples of the mapping: 

- PGPDO0[PPDO15] = GPDO0[PDO_0] 

- PGPDO2[PPDO15] = GPDO32[PDO_32] 

- PGPDO31[PPDO0] = GPDO511[PDO_511] 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

332 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

PGPDOn registers access the same physical resource as the PDO and MPGPDO address locations. 

These registers support 8-, 16-, and 32-bit accesses. 

##### Diagram 

|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|
|W|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|15|Parallel Pad Data Out 15|
|PPDO15|0b - Logic low<br>1b - Logic high|
|14|Parallel Pad Data Out 14|
|PPDO14|0b - Logic low<br>1b - Logic high|
|13|Parallel Pad Data Out 13|
|PPDO13|0b - Logic low<br>1b - Logic high|
|12|Parallel Pad Data Out 12|
|PPDO12|0b - Logic low<br>1b - Logic high|
|11|Parallel Pad Data Out 11|
|PPDO11|0b - Logic low<br>1b - Logic high|
|10|Parallel Pad Data Out 10|
|PPDO10|0b - Logic low<br>1b - Logic high|
|9|Parallel Pad Data Out 9|
|PPDO9|0b - Logic low<br>1b - Logic high|
|8|Parallel Pad Data Out 8|
|PPDO8|0b - Logic low<br>1b - Logic high<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

333 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|7|Parallel Pad Data Out 7|
|PPDO7|0b - Logic low<br>1b - Logic high|
|6|Parallel Pad Data Out 6|
|PPDO6|0b - Logic low<br>1b - Logic high|
|5|Parallel Pad Data Out 5|
|PPDO5|0b - Logic low|
||1b - Logic high|
|4|Parallel Pad Data Out 4|
|PPDO4|0b - Logic low<br>1b - Logic high|
|3|Parallel Pad Data Out 3|
|PPDO3|0b - Logic low<br>1b - Logic high|
|2|Parallel Pad Data Out 2|
|PPDO2|0b - Logic low|
||1b - Logic high|
|1|Parallel Pad Data Out 1|
|PPDO1|0b - Logic low|
||1b - Logic high|
|0|Parallel Pad Data Out 0|
|PPDO0|0b - Logic low|
||1b - Logic high|



### 9.4.25 SIUL2 Parallel GPIO Pad Data Out Register (PGPDO2) 

##### Offset 

|Register|Offset|
|---|---|
|PGPDO2|1706h|



##### Function 

Each PGPDOn register sets or clears the respective pads of the chip. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

334 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

PGPDOn registers can set the values of all output pins assigned to a chip port with a single 16-bit register write, while the GPDOn registers set the value on a specific pin with byte writes. 

Each bit writes or reads the data register that stores the value to be driven on the pad in output mode. Access to this register location is coherent with access to the bit-wise GPDOn. 

For a given PGPDOx[PPDOy] where x is the register instance index and y is the field index, the following equation shows the equivalent GPDOn[PDO_n] bit: 

PGPDOx[PPDOy] = GPDO(x Á 16) + (15 - y)[PDO_(x Á 16) + (15 - y)] 

Some examples of the mapping: 

- PGPDO0[PPDO15] = GPDO0[PDO_0] 

- PGPDO2[PPDO15] = GPDO32[PDO_32] 

- PGPDO31[PPDO0] = GPDO511[PDO_511] 

PGPDOn registers access the same physical resource as the PDO and MPGPDO address locations. 

These registers support 8-, 16-, and 32-bit accesses. 

##### Diagram 

|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|0|0|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|
|W|15|14|13|12|11|10|||7|6|5|4|3|2|1|0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|15|Parallel Pad Data Out 15|
|PPDO15|0b - Logic low<br>1b - Logic high|
|14|Parallel Pad Data Out 14|
|PPDO14|0b - Logic low<br>1b - Logic high|
|13|Parallel Pad Data Out 13|
|PPDO13|0b - Logic low<br>1b - Logic high|
|12|Parallel Pad Data Out 12|
|PPDO12|0b - Logic low<br>1b - Logic high|
|11|Parallel Pad Data Out 11|
|PPDO11|0b - Logic low|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

335 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function<br>1b -|Logic high|
|---|---|---|
|10|Parallel Pa|d Data Out 10|
|PPDO10|0b -<br>1b -|Logic low<br>Logic high|
|9<br>—|Reserved<br>Always wri|te zero to this field.|
|8<br>—|Reserved<br>Always wri|te zero to this field.|
|7|Parallel Pa|d Data Out 7|
|PPDO7|0b -<br>1b -|Logic low<br>Logic high|
|6|Parallel Pa|d Data Out 6|
|PPDO6|0b -<br>1b -|Logic low<br>Logic high|
|5|Parallel Pa|d Data Out 5|
|PPDO5|0b -<br>1b -|Logic low<br>Logic high|
|4|Parallel Pa|d Data Out 4|
|PPDO4|0b -<br>1b -|Logic low<br>Logic high|
|3|Parallel Pa|d Data Out 3|
|PPDO3|0b -|Logic low|
||1b -|Logic high|
|2|Parallel Pa|d Data Out 2|
|PPDO2|0b -|Logic low|
||1b -|Logic high|
|1|Parallel Pa|d Data Out 1|
|PPDO1|0b -|Logic low|
||1b -|Logic high|
|0|Parallel Pa|d Data Out 0|
|PPDO0|0b -|Logic low|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

336 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - Logic high|



### 9.4.26 SIUL2 Parallel GPIO Pad Data Out Register (PGPDO4 - PGPDO13) 

Offset 

For n = 4 to 13: 

|Register|Offset|
|---|---|
|PGPDOn|1708h + 2 × (n + 1 – 2 × (n mod 2))|



##### Function 

Each PGPDOn register sets or clears the respective pads of the chip. 

PGPDOn registers can set the values of all output pins assigned to a chip port with a single 16-bit register write, while the GPDOn registers set the value on a specific pin with byte writes. 

Each bit writes or reads the data register that stores the value to be driven on the pad in output mode. Access to this register location is coherent with access to the bit-wise GPDOn. 

For a given PGPDOx[PPDOy] where x is the register instance index and y is the field index, the following equation shows the equivalent GPDOn[PDO_n] bit: 

PGPDOx[PPDOy] = GPDO(x Á 16) + (15 - y)[PDO_(x Á 16) + (15 - y)] 

Some examples of the mapping: 

- PGPDO0[PPDO15] = GPDO0[PDO_0] 

- PGPDO2[PPDO15] = GPDO32[PDO_32] 

- PGPDO31[PPDO0] = GPDO511[PDO_511] 

PGPDOn registers access the same physical resource as the PDO and MPGPDO address locations. 

These registers support 8-, 16-, and 32-bit accesses. 

##### Diagram 

|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|
|W|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|15|Parallel Pad Data Out 15|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

337 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|PPDO15|0b - Logic low|
||1b - Logic high|
|14|Parallel Pad Data Out 14|
|PPDO14|0b - Logic low<br>1b - Logic high|
|13|Parallel Pad Data Out 13|
|PPDO13|0b - Logic low<br>1b - Logic high|
|12|Parallel Pad Data Out 12|
|PPDO12|0b - Logic low<br>1b - Logic high|
|11|Parallel Pad Data Out 11|
|PPDO11|0b - Logic low<br>1b - Logic high|
|10|Parallel Pad Data Out 10|
|PPDO10|0b - Logic low<br>1b - Logic high|
|9|Parallel Pad Data Out 9|
|PPDO9|0b - Logic low<br>1b - Logic high|
|8|Parallel Pad Data Out 8|
|PPDO8|0b - Logic low<br>1b - Logic high|
|7|Parallel Pad Data Out 7|
|PPDO7|0b - Logic low<br>1b - Logic high|
|6|Parallel Pad Data Out 6|
|PPDO6|0b - Logic low<br>1b - Logic high|
|5|Parallel Pad Data Out 5|
|PPDO5|0b - Logic low<br>1b - Logic high<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

338 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|4|Parallel Pad Data Out 4|
|PPDO4|0b - Logic low<br>1b - Logic high|
|3|Parallel Pad Data Out 3|
|PPDO3|0b - Logic low<br>1b - Logic high|
|2|Parallel Pad Data Out 2|
|PPDO2|0b - Logic low<br>1b - Logic high|
|1|Parallel Pad Data Out 1|
|PPDO1|0b - Logic low<br>1b - Logic high|
|0|Parallel Pad Data Out 0|
|PPDO0|0b - Logic low|
||1b - Logic high|



### 9.4.27 SIUL2 Parallel GPIO Pad Data Out Register (PGPDO14) 

##### Offset 

|Register|Offset|
|---|---|
|PGPDO14|171Eh|



##### Function 

Each PGPDOn register sets or clears the respective pads of the chip. 

PGPDOn registers can set the values of all output pins assigned to a chip port with a single 16-bit register write, while the GPDOn registers set the value on a specific pin with byte writes. 

Each bit writes or reads the data register that stores the value to be driven on the pad in output mode. Access to this register location is coherent with access to the bit-wise GPDOn. 

For a given PGPDOx[PPDOy] where x is the register instance index and y is the field index, the following equation shows the equivalent GPDOn[PDO_n] bit: 

PGPDOx[PPDOy] = GPDO(x Á 16) + (15 - y)[PDO_(x Á 16) + (15 - y)] 

Some examples of the mapping: 

- PGPDO0[PPDO15] = GPDO0[PDO_0] 

- PGPDO2[PPDO15] = GPDO32[PDO_32] 

- PGPDO31[PPDO0] = GPDO511[PDO_511] 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

339 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

PGPDOn registers access the same physical resource as the PDO and MPGPDO address locations. 

These registers support 8-, 16-, and 32-bit accesses. 

##### Diagram 

|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|PPDO|0|0|0|
|W|15|14|13|12|11|10|9|8|7|6|5|4|3||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|15|Parallel Pad Data Out 15|
|PPDO15|0b - Logic low<br>1b - Logic high|
|14|Parallel Pad Data Out 14|
|PPDO14|0b - Logic low<br>1b - Logic high|
|13|Parallel Pad Data Out 13|
|PPDO13|0b - Logic low<br>1b - Logic high|
|12|Parallel Pad Data Out 12|
|PPDO12|0b - Logic low<br>1b - Logic high|
|11|Parallel Pad Data Out 11|
|PPDO11|0b - Logic low<br>1b - Logic high|
|10|Parallel Pad Data Out 10|
|PPDO10|0b - Logic low<br>1b - Logic high|
|9|Parallel Pad Data Out 9|
|PPDO9|0b - Logic low<br>1b - Logic high|
|8|Parallel Pad Data Out 8|
|PPDO8|0b - Logic low<br>1b - Logic high<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

340 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|7<br>PPDO7|Parallel Pad Data Out 7<br>0b - Logic low<br>1b - Logic high|
|6<br>PPDO6|Parallel Pad Data Out 6<br>0b - Logic low<br>1b - Logic high|
|5<br>PPDO5|Parallel Pad Data Out 5<br>0b - Logic low<br>1b - Logic high|
|4<br>PPDO4|Parallel Pad Data Out 4<br>0b - Logic low<br>1b - Logic high|
|3<br>PPDO3|Parallel Pad Data Out 3<br>0b - Logic low<br>1b - Logic high|
|2<br>—|Reserved<br>Always write zero to this field.|
|1<br>—|Reserved<br>Always write zero to this field.|
|0|Reserved|
|—|Always write zero to this field.|



### 9.4.28 SIUL2 Parallel GPIO Pad Data In Register (PGPDI0 - PGPDI3) 

##### Offset 

|Register|Offset|
|---|---|
|PGPDI1|1740h|
|PGPDI0|1742h|
|PGPDI3|1744h|



##### Function 

PGPDIn registers hold the synchronized input value from the pads. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

341 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

PGPDIn registers can read the values of all input pins assigned to a chip port with a single 16-bit register read, while the GPDIn registers read the value on a specific pin with a byte read. 

Each bit reads the current pad value. Access to this register location is coherent with access to the bit-wise GPDIn. 

For a given PGPDIx[PPDIy] where x is the register instance index and y is the field index, the following equation shows the equivalent GPDIn[PDI_n] bit: 

PGPDIx[PPDIy] = GPDI(x Á 16) + (15 - y)[PDI_(x Á 16) + (15 - y)] 

Some examples of the mapping: 

- PGPDI0[PPDI15] = GPDI0[PDI_0] 

- PGPDI2[PPDI15] = GPDI32[PDI_32] 

- PGPDI31[PPDI0] = GPDI511[PDI_511] 

These registers support 8-, 16-, and 32-bit accesses. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/009_System_Integration_Unit_Lite2_-SIUL2-/S32K3XXRM_数据表.pdf-0342-12.png)


<!-- Start of picture text -->
Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>PPDI1 PPDI1 PPDI1 PPDI1 PPDI1 PPDI1<br>R PPDI9  PPDI8  PPDI7  PPDI6  PPDI5  PPDI4  PPDI3  PPDI2  PPDI1  PPDI0<br>5  4  3  2  1  0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|15|Parallel Pad Data In 15|
|PPDI15|0b - Logic low<br>1b - Logic high|
|14|Parallel Pad Data In 14|
|PPDI14|0b - Logic low<br>1b - Logic high|
|13|Parallel Pad Data In 13|
|PPDI13|0b - Logic low<br>1b - Logic high|
|12|Parallel Pad Data In 12|
|PPDI12|0b - Logic low<br>1b - Logic high|
|11|Parallel Pad Data In 11|
|PPDI11|0b - Logic low|
||1b - Logic high|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

342 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|10|Parallel Pad Data In 10|
|PPDI10|0b - Logic low|
||1b - Logic high|
|9|Parallel Pad Data In 9|
|PPDI9|0b - Logic low|
||1b - Logic high|
|8|Parallel Pad Data In 8|
|PPDI8|0b - Logic low|
||1b - Logic high|
|7|Parallel Pad Data In 7|
|PPDI7|0b - Logic low|
||1b - Logic high|
|6|Parallel Pad Data In 6|
|PPDI6|0b - Logic low|
||1b - Logic high|
|5|Parallel Pad Data In 5|
|PPDI5|0b - Logic low|
||1b - Logic high|
|4|Parallel Pad Data In 4|
|PPDI4|0b - Logic low|
||1b - Logic high|
|3|Parallel Pad Data In 3|
|PPDI3|0b - Logic low|
||1b - Logic high|
|2|Parallel Pad Data In 2|
|PPDI2|0b - Logic low|
||1b - Logic high|
|1|Parallel Pad Data In 1|
|PPDI1|0b - Logic low|
||1b - Logic high|
|0|Parallel Pad Data In 0|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

343 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|PPDI0|0b - Logic low|
||1b - Logic high|



### 9.4.29 SIUL2 Parallel GPIO Pad Data In Register (PGPDI2) 

Offset 

|Register|Offset|
|---|---|
|PGPDI2|1746h|



##### Function 

PGPDIn registers hold the synchronized input value from the pads. 

PGPDIn registers can read the values of all input pins assigned to a chip port with a single 16-bit register read, while the GPDIn registers read the value on a specific pin with a byte read. 

Each bit reads the current pad value. Access to this register location is coherent with access to the bit-wise GPDIn. 

For a given PGPDIx[PPDIy] where x is the register instance index and y is the field index, the following equation shows the equivalent GPDIn[PDI_n] bit: 

PGPDIx[PPDIy] = GPDI(x Á 16) + (15 - y)[PDI_(x Á 16) + (15 - y)] 

Some examples of the mapping: 

- PGPDI0[PPDI15] = GPDI0[PDI_0] 

- PGPDI2[PPDI15] = GPDI32[PDI_32] 

- PGPDI31[PPDI0] = GPDI511[PDI_511] 

These registers support 8-, 16-, and 32-bit accesses. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/009_System_Integration_Unit_Lite2_-SIUL2-/S32K3XXRM_数据表.pdf-0344-19.png)


<!-- Start of picture text -->
Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>PPDI1 PPDI1 PPDI1 PPDI1 PPDI1 PPDI1 Reserv Reserv<br>R PPDI7  PPDI6  PPDI5  PPDI4  PPDI3  PPDI2  PPDI1  PPDI0<br>5  4  3  2  1  0  ed  ed<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|15|Parallel Pad Data In 15|
|PPDI15||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

344 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function<br>0b - Logic low<br>1b - Logic high|
|---|---|
|14|Parallel Pad Data In 14|
|PPDI14|0b - Logic low<br>1b - Logic high|
|13|Parallel Pad Data In 13|
|PPDI13|0b - Logic low<br>1b - Logic high|
|12|Parallel Pad Data In 12|
|PPDI12|0b - Logic low<br>1b - Logic high|
|11|Parallel Pad Data In 11|
|PPDI11|0b - Logic low<br>1b - Logic high|
|10|Parallel Pad Data In 10|
|PPDI10|0b - Logic low<br>1b - Logic high|
|9<br>—|Reserved|
|8<br>—|Reserved|
|7|Parallel Pad Data In 7|
|PPDI7|0b - Logic low<br>1b - Logic high|
|6|Parallel Pad Data In 6|
|PPDI6|0b - Logic low<br>1b - Logic high|
|5|Parallel Pad Data In 5|
|PPDI5|0b - Logic low<br>1b - Logic high|
|4|Parallel Pad Data In 4<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

345 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|PPDI4|0b - Logic low|
||1b - Logic high|
|3|Parallel Pad Data In 3|
|PPDI3|0b - Logic low|
||1b - Logic high|
|2|Parallel Pad Data In 2|
|PPDI2|0b - Logic low|
||1b - Logic high|
|1|Parallel Pad Data In 1|
|PPDI1|0b - Logic low|
||1b - Logic high|
|0|Parallel Pad Data In 0|
|PPDI0|0b - Logic low|
||1b - Logic high|



### 9.4.30 SIUL2 Parallel GPIO Pad Data In Register (PGPDI4 - PGPDI13) 

##### Offset 

For n = 4 to 13: 

|Register|Offset|
|---|---|
|PGPDIn|1748h + 2 × (n + 1 – 2 × (n mod 2))|



##### Function 

PGPDIn registers hold the synchronized input value from the pads. 

PGPDIn registers can read the values of all input pins assigned to a chip port with a single 16-bit register read, while the GPDIn registers read the value on a specific pin with a byte read. 

Each bit reads the current pad value. Access to this register location is coherent with access to the bit-wise GPDIn. 

For a given PGPDIx[PPDIy] where x is the register instance index and y is the field index, the following equation shows the equivalent GPDIn[PDI_n] bit: 

PGPDIx[PPDIy] = GPDI(x Á 16) + (15 - y)[PDI_(x Á 16) + (15 - y)] 

Some examples of the mapping: 

- PGPDI0[PPDI15] = GPDI0[PDI_0] 

- PGPDI2[PPDI15] = GPDI32[PDI_32] 

- PGPDI31[PPDI0] = GPDI511[PDI_511] 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

346 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

These registers support 8-, 16-, and 32-bit accesses. 

##### Diagram 

|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|PPDI1<br>5|PPDI1<br>4|PPDI1<br>3|PPDI1<br>2|PPDI1<br>1|PPDI1<br>0|PPDI9|PPDI8|PPDI7|PPDI6|PPDI5|PPDI4|PPDI3|PPDI2|PPDI1|PPDI0|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|15|Parallel Pad Data In 15|
|PPDI15|0b - Logic low<br>1b - Logic high|
|14|Parallel Pad Data In 14|
|PPDI14|0b - Logic low<br>1b - Logic high|
|13|Parallel Pad Data In 13|
|PPDI13|0b - Logic low|
||1b - Logic high|
|12|Parallel Pad Data In 12|
|PPDI12|0b - Logic low<br>1b - Logic high|
|11|Parallel Pad Data In 11|
|PPDI11|0b - Logic low<br>1b - Logic high|
|10|Parallel Pad Data In 10|
|PPDI10|0b - Logic low|
||1b - Logic high|
|9|Parallel Pad Data In 9|
|PPDI9|0b - Logic low|
||1b - Logic high|
|8|Parallel Pad Data In 8|
|PPDI8|0b - Logic low|
||1b - Logic high|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

347 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|7|Parallel Pad Data In 7|
|PPDI7|0b - Logic low|
||1b - Logic high|
|6|Parallel Pad Data In 6|
|PPDI6|0b - Logic low|
||1b - Logic high|
|5|Parallel Pad Data In 5|
|PPDI5|0b - Logic low|
||1b - Logic high|
|4|Parallel Pad Data In 4|
|PPDI4|0b - Logic low|
||1b - Logic high|
|3|Parallel Pad Data In 3|
|PPDI3|0b - Logic low|
||1b - Logic high|
|2|Parallel Pad Data In 2|
|PPDI2|0b - Logic low|
||1b - Logic high|
|1|Parallel Pad Data In 1|
|PPDI1|0b - Logic low|
||1b - Logic high|
|0|Parallel Pad Data In 0|
|PPDI0|0b - Logic low|
||1b - Logic high|



### 9.4.31 SIUL2 Parallel GPIO Pad Data In Register (PGPDI14) 

##### Offset 

|Register|Offset|
|---|---|
|PGPDI14|175Eh|



##### Function 

PGPDIn registers hold the synchronized input value from the pads. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

348 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

PGPDIn registers can read the values of all input pins assigned to a chip port with a single 16-bit register read, while the GPDIn registers read the value on a specific pin with a byte read. 

Each bit reads the current pad value. Access to this register location is coherent with access to the bit-wise GPDIn. 

For a given PGPDIx[PPDIy] where x is the register instance index and y is the field index, the following equation shows the equivalent GPDIn[PDI_n] bit: 

PGPDIx[PPDIy] = GPDI(x Á 16) + (15 - y)[PDI_(x Á 16) + (15 - y)] 

Some examples of the mapping: 

- PGPDI0[PPDI15] = GPDI0[PDI_0] 

- PGPDI2[PPDI15] = GPDI32[PDI_32] 

- PGPDI31[PPDI0] = GPDI511[PDI_511] 

These registers support 8-, 16-, and 32-bit accesses. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/009_System_Integration_Unit_Lite2_-SIUL2-/S32K3XXRM_数据表.pdf-0349-12.png)


<!-- Start of picture text -->
Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>PPDI1 PPDI1 PPDI1 PPDI1 PPDI1 PPDI1 Reserv Reserv Reserv<br>R PPDI9  PPDI8  PPDI7  PPDI6  PPDI5  PPDI4  PPDI3<br>5  4  3  2  1  0  ed  ed  ed<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|15|Parallel Pad Data In 15|
|PPDI15|0b - Logic low<br>1b - Logic high|
|14|Parallel Pad Data In 14|
|PPDI14|0b - Logic low<br>1b - Logic high|
|13|Parallel Pad Data In 13|
|PPDI13|0b - Logic low<br>1b - Logic high|
|12|Parallel Pad Data In 12|
|PPDI12|0b - Logic low<br>1b - Logic high|
|11|Parallel Pad Data In 11|
|PPDI11|0b - Logic low|
||1b - Logic high|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

349 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function||
|---|---|---|
|10|Parallel Pa|d Data In 10|
|PPDI10|0b -|Logic low|
||1b -|Logic high|
|9|Parallel Pa|d Data In 9|
|PPDI9|0b -|Logic low|
||1b -|Logic high|
|8|Parallel Pa|d Data In 8|
|PPDI8|0b -|Logic low|
||1b -|Logic high|
|7|Parallel Pa|d Data In 7|
|PPDI7|0b -|Logic low|
||1b -|Logic high|
|6|Parallel Pa|d Data In 6|
|PPDI6|0b -<br>1b -|Logic low<br>Logic high|
|5|Parallel Pa|d Data In 5|
|PPDI5|0b -|Logic low|
||1b -|Logic high|
|4|Parallel Pa|d Data In 4|
|PPDI4|0b -|Logic low|
||1b -|Logic high|
|3|Parallel Pa|d Data In 3|
|PPDI3|0b -|Logic low|
||1b -|Logic high|
|2<br>|Reserved||
|—<br>1<br>—|Reserved||
|0<br>—|Reserved||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

350 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

### 9.4.32 SIUL2 Masked Parallel GPIO Pad Data Out Register (MPGPDO0 - MPGPDO1) 

##### Offset 

|Register|Offset|
|---|---|
|MPGPDO0|1780h|
|MPGPDO1|1784h|



##### Function 

Each MPGPDOn register selectively modifies the pad values associated with PGPDOn. 

- ~~<mark>NOTE</mark>~~ 

MPGPDOn registers must only be accessed with 32-bit writes. 8-bit or 16-bit writes will not modify any bits in the register and cause a transfer error. Read access will return 0. 

~~<mark>NOTE</mark>~~ 

MPGPDOn registers support only 32-bit accesses. Byte and half-word accesses are not supported. 

Accesses to each MPGPDOn register location is coherent with access to the bit-wise GPDOn. 

For a given MPGPDOx[MPPDOy] where x is the register instance index and y is the field index, the following equation shows the equivalent GPDOn[PDO_n] bit: 

MPGPDOx[MPPDOy] = GPDO(x Á 16) + (15 - y)[PDO_(x Á 16) + (15 - y)] 

Some examples of the mapping: 

- MPGPDO0[MPPDO15] = GPDO0[PDO_0] 

- MPGPDO2[MPPDO15] = GPDO32[PDO_32] 

- MPGPDO31[MPPDO0] = GPDO511[PDO_511] 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|W|MASK<br>15|MASK<br>14|MASK<br>13|MASK<br>12|MASK<br>11|MASK<br>10|MASK<br>9|MASK<br>8|MASK<br>7|MASK<br>6|MASK<br>5|MASK<br>4|MASK<br>3|MASK<br>2|MASK<br>1|MASK<br>0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|W|MPPD<br>O15|MPPD<br>O14|MPPD<br>O13|MPPD<br>O12|MPPD<br>O11|MPPD<br>O10|MPPD<br>O9|MPPD<br>O8|MPPD<br>O7|MPPD<br>O6|MPPD<br>O5|MPPD<br>O4|MPPD<br>O3|MPPD<br>O2|MPPD<br>O1|MPPD<br>O0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

351 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Fields 

|Field<br>31<br>MASK15|Function<br>Mask Field 15<br>Masks MPPDO15 in the same MPGPDOn register instance.<br>0b - MPPDO15 is ignored<br>1b - MPPDO15 is written|
|---|---|
|30<br>MASK14|Mask Field 14<br>Masks MPPDO14 in the same MPGPDOn register instance.<br>0b - MPPDO14 is ignored<br>1b - MPPDO14 is written|
|29|Mask Field 13|
|MASK13|Masks MPPDO13 in the same MPGPDOn register instance.<br>0b - MPPDO13 is ignored<br>1b - MPPDO13 is written|
|28|Mask Field 12|
|MASK12|Masks MPPDO12 in the same MPGPDOn register instance.<br>0b - MPPDO12 is ignored<br>1b - MPPDO12 is written|
|27|Mask Field 11|
|MASK11|Masks MPPDO11 in the same MPGPDOn register instance.<br>0b - MPPDO11 is ignored<br>1b - MPPDO11 is written|
|26<br>MASK10|Mask Field 10<br>Masks MPPDO10 in the same MPGPDOn register instance.<br>0b - MPPDO10 is ignored<br>1b - MPPDO10 is written|
|25<br>MASK9|Mask Field 9<br>Masks MPPDO9 in the same MPGPDOn register instance.<br>0b - MPPDO9 is ignored<br>1b - MPPDO9 is written|
|24<br>MASK8|Mask Field 8<br>Masks MPPDO8 in the same MPGPDOn register instance.<br>0b - MPPDO8 is ignored<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

352 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function<br>1b - MPPDO8 is written|
|---|---|
|23|Mask Field 7|
|MASK7|Masks MPPDO7 in the same MPGPDOn register instance.<br>0b - MPPDO7 is ignored<br>1b - MPPDO7 is written|
|22|Mask Field 6|
|MASK6|Masks MPPDO6 in the same MPGPDOn register instance.<br>0b - MPPDO6 is ignored<br>1b - MPPDO6 is written|
|21|Mask Field 5|
|MASK5|Masks MPPDO5 in the same MPGPDOn register instance.<br>0b - MPPDO5 is ignored<br>1b - MPPDO5 is written|
|20|Mask Field 4|
|MASK4|Masks MPPDO4 in the same MPGPDOn register instance.<br>0b - MPPDO4 is ignored<br>1b - MPPDO4 is written|
|19|Mask Field 3|
|MASK3|Masks MPPDO3 in the same MPGPDOn register instance.<br>0b - MPPDO3 is ignored<br>1b - MPPDO3 is written|
|18|Mask Field 2|
|MASK2|Masks MPPDO2 in the same MPGPDOn register instance.<br>0b - MPPDO2 is ignored<br>1b - MPPDO2 is written|
|17|Mask Field 1|
|MASK1|Masks MPPDO1 in the same MPGPDOn register instance.<br>0b - MPPDO1 is ignored<br>1b - MPPDO1 is written|
|16|Mask Field 0|
|MASK0|Masks MPPDO0 in the same MPGPDOn register instance.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

353 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - MPPDO0 is ignored<br>1b - MPPDO0 is written|
|15|Masked Parallel Pad Data Out 15|
|MPPDO15|Writes the data register that stores the value to be driven on the pad in output mode.|
|14|Masked Parallel Pad Data Out 14|
|MPPDO14|Writes the data register that stores the value to be driven on the pad in output mode.|
|13|Masked Parallel Pad Data Out 13|
|MPPDO13|Writes the data register that stores the value to be driven on the pad in output mode.|
|12|Masked Parallel Pad Data Out 12|
|MPPDO12|Writes the data register that stores the value to be driven on the pad in output mode.|
|11|Masked Parallel Pad Data Out 11|
|MPPDO11|Writes the data register that stores the value to be driven on the pad in output mode.|
|10|Masked Parallel Pad Data Out 10|
|MPPDO10|Writes the data register that stores the value to be driven on the pad in output mode.|
|9|Masked Parallel Pad Data Out 9|
|MPPDO9|Writes the data register that stores the value to be driven on the pad in output mode.|
|8|Masked Parallel Pad Data Out 8|
|MPPDO8|Writes the data register that stores the value to be driven on the pad in output mode.|
|7|Masked Parallel Pad Data Out 7|
|MPPDO7|Writes the data register that stores the value to be driven on the pad in output mode.|
|6|Masked Parallel Pad Data Out 6|
|MPPDO6|Writes the data register that stores the value to be driven on the pad in output mode.|
|5|Masked Parallel Pad Data Out 5|
|MPPDO5|Writes the data register that stores the value to be driven on the pad in output mode.|
|4|Masked Parallel Pad Data Out 4|
|MPPDO4|Writes the data register that stores the value to be driven on the pad in output mode.|
|3|Masked Parallel Pad Data Out 3|
|MPPDO3|Writes the data register that stores the value to be driven on the pad in output mode.|
|2|Masked Parallel Pad Data Out 2|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

354 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|MPPDO2|Writes the data register that stores the value to be driven on the pad in output mode.|
|1|Masked Parallel Pad Data Out 1|
|MPPDO1|Writes the data register that stores the value to be driven on the pad in output mode.|
|0|Masked Parallel Pad Data Out 0|
|MPPDO0|Writes the data register that stores the value to be driven on the pad in output mode.|



### 9.4.33 SIUL2 Masked Parallel GPIO Pad Data Out Register (MPGPDO2) 

Offset 

|Register|Offset|
|---|---|
|MPGPDO2|1788h|



##### Function 

Each MPGPDOn register selectively modifies the pad values associated with PGPDOn. 

~~<mark>NOTE</mark>~~ 

MPGPDOn registers must only be accessed with 32-bit writes. 8-bit or 16-bit writes will not modify any bits in the 

register and cause a transfer error. Read access will return 0. 

- ~~<mark>NOTE</mark>~~ 

MPGPDOn registers support only 32-bit accesses. Byte and half-word accesses are not supported. 

Accesses to each MPGPDOn register location is coherent with access to the bit-wise GPDOn. 

For a given MPGPDOx[MPPDOy] where x is the register instance index and y is the field index, the following equation shows the equivalent GPDOn[PDO_n] bit: 

MPGPDOx[MPPDOy] = GPDO(x Á 16) + (15 - y)[PDO_(x Á 16) + (15 - y)] 

Some examples of the mapping: 

- MPGPDO0[MPPDO15] = GPDO0[PDO_0] 

- MPGPDO2[MPPDO15] = GPDO32[PDO_32] 

- MPGPDO31[MPPDO0] = GPDO511[PDO_511] 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

355 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|W|MASK<br>15|MASK<br>14|MASK<br>13|MASK<br>12|MASK<br>11|MASK<br>10|Reserv<br>ed|Reserv<br>ed|MASK<br>7|MASK<br>6|MASK<br>5|MASK<br>4|MASK<br>3|MASK<br>2|MASK<br>1|MASK<br>0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|W|MPPD<br>O15|MPPD<br>O14|MPPD<br>O13|MPPD<br>O12|MPPD<br>O11|MPPD<br>O10|Reserv<br>ed|Reserv<br>ed|MPPD<br>O7|MPPD<br>O6|MPPD<br>O5|MPPD<br>O4|MPPD<br>O3|MPPD<br>O2|MPPD<br>O1|MPPD<br>O0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|Mask Field 15|
|MASK15|Masks MPPDO15 in the same MPGPDOn register instance.<br>0b - MPPDO15 is ignored<br>1b - MPPDO15 is written|
|30<br>MASK14|Mask Field 14<br>Masks MPPDO14 in the same MPGPDOn register instance.<br>0b - MPPDO14 is ignored<br>1b - MPPDO14 is written|
|29|Mask Field 13|
|MASK13|Masks MPPDO13 in the same MPGPDOn register instance.<br>0b - MPPDO13 is ignored<br>1b - MPPDO13 is written|
|28<br>MASK12|Mask Field 12<br>Masks MPPDO12 in the same MPGPDOn register instance.<br>0b - MPPDO12 is ignored<br>1b - MPPDO12 is written|
|27|Mask Field 11|
|MASK11|Masks MPPDO11 in the same MPGPDOn register instance.<br>0b - MPPDO11 is ignored<br>1b - MPPDO11 is written|
|26|Mask Field 10|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

356 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|MASK10|Masks MPPDO10 in the same MPGPDOn register instance.<br>0b - MPPDO10 is ignored<br>1b - MPPDO10 is written|
|25<br>—|Reserved<br>Always write zero to this field.|
|24<br>—|Reserved<br>Always write zero to this field.|
|23<br>MASK7|Mask Field 7<br>Masks MPPDO7 in the same MPGPDOn register instance.<br>0b - MPPDO7 is ignored<br>1b - MPPDO7 is written|
|22<br>MASK6|Mask Field 6<br>Masks MPPDO6 in the same MPGPDOn register instance.<br>0b - MPPDO6 is ignored<br>1b - MPPDO6 is written|
|21<br>MASK5|Mask Field 5<br>Masks MPPDO5 in the same MPGPDOn register instance.<br>0b - MPPDO5 is ignored<br>1b - MPPDO5 is written|
|20<br>MASK4|Mask Field 4<br>Masks MPPDO4 in the same MPGPDOn register instance.<br>0b - MPPDO4 is ignored<br>1b - MPPDO4 is written|
|19<br>MASK3|Mask Field 3<br>Masks MPPDO3 in the same MPGPDOn register instance.<br>0b - MPPDO3 is ignored<br>1b - MPPDO3 is written|
|18|Mask Field 2|
|MASK2|Masks MPPDO2 in the same MPGPDOn register instance.<br>0b - MPPDO2 is ignored<br>1b - MPPDO2 is written|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

357 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|17|Mask Field 1|
|MASK1|Masks MPPDO1 in the same MPGPDOn register instance.<br>0b - MPPDO1 is ignored<br>1b - MPPDO1 is written|
|16<br>MASK0|Mask Field 0<br>Masks MPPDO0 in the same MPGPDOn register instance.<br>0b - MPPDO0 is ignored<br>1b - MPPDO0 is written|
|15|Masked Parallel Pad Data Out 15|
|MPPDO15|Writes the data register that stores the value to be driven on the pad in output mode.|
|14|Masked Parallel Pad Data Out 14|
|MPPDO14|Writes the data register that stores the value to be driven on the pad in output mode.|
|13|Masked Parallel Pad Data Out 13|
|MPPDO13|Writes the data register that stores the value to be driven on the pad in output mode.|
|12|Masked Parallel Pad Data Out 12|
|MPPDO12|Writes the data register that stores the value to be driven on the pad in output mode.|
|11|Masked Parallel Pad Data Out 11|
|MPPDO11|Writes the data register that stores the value to be driven on the pad in output mode.|
|10|Masked Parallel Pad Data Out 10|
|MPPDO10|Writes the data register that stores the value to be driven on the pad in output mode.|
|9<br>—|Reserved<br>Always write zero to this field.|
|8<br>—|Reserved<br>Always write zero to this field.|
|7<br>MPPDO7|Masked Parallel Pad Data Out 7<br>Writes the data register that stores the value to be driven on the pad in output mode.|
|6|Masked Parallel Pad Data Out 6|
|MPPDO6|Writes the data register that stores the value to be driven on the pad in output mode.|
|5|Masked Parallel Pad Data Out 5<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

358 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|MPPDO5|Writes the data register that stores the value to be driven on the pad in output mode.|
|4|Masked Parallel Pad Data Out 4|
|MPPDO4|Writes the data register that stores the value to be driven on the pad in output mode.|
|3|Masked Parallel Pad Data Out 3|
|MPPDO3|Writes the data register that stores the value to be driven on the pad in output mode.|
|2|Masked Parallel Pad Data Out 2|
|MPPDO2|Writes the data register that stores the value to be driven on the pad in output mode.|
|1|Masked Parallel Pad Data Out 1|
|MPPDO1|Writes the data register that stores the value to be driven on the pad in output mode.|
|0|Masked Parallel Pad Data Out 0|
|MPPDO0|Writes the data register that stores the value to be driven on the pad in output mode.|



### 9.4.34 SIUL2 Masked Parallel GPIO Pad Data Out Register (MPGPDO3 - MPGPDO13) 

##### Offset 

For a = 3 to 13: 

|Register<br>MPGPDOa|Offset<br>1780h + (a × 4h)|
|---|---|



##### Function 

Each MPGPDOn register selectively modifies the pad values associated with PGPDOn. 

~~<mark>NOTE</mark>~~ 

MPGPDOn registers must only be accessed with 32-bit writes. 8-bit or 16-bit writes will not modify any bits in the register and cause a transfer error. Read access will return 0. 

~~<mark>NOTE</mark>~~ 

MPGPDOn registers support only 32-bit accesses. Byte and half-word accesses are not supported. 

Accesses to each MPGPDOn register location is coherent with access to the bit-wise GPDOn. 

For a given MPGPDOx[MPPDOy] where x is the register instance index and y is the field index, the following equation shows the equivalent GPDOn[PDO_n] bit: 

MPGPDOx[MPPDOy] = GPDO(x Á 16) + (15 - y)[PDO_(x Á 16) + (15 - y)] 

Some examples of the mapping: 

- MPGPDO0[MPPDO15] = GPDO0[PDO_0] 

- MPGPDO2[MPPDO15] = GPDO32[PDO_32] 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

359 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### • MPGPDO31[MPPDO0] = GPDO511[PDO_511] 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|W|MASK<br>15|MASK<br>14|MASK<br>13|MASK<br>12|MASK<br>11|MASK<br>10|MASK<br>9|MASK<br>8|MASK<br>7|MASK<br>6|MASK<br>5|MASK<br>4|MASK<br>3|MASK<br>2|MASK<br>1|MASK<br>0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|W|MPPD<br>O15|MPPD<br>O14|MPPD<br>O13|MPPD<br>O12|MPPD<br>O11|MPPD<br>O10|MPPD<br>O9|MPPD<br>O8|MPPD<br>O7|MPPD<br>O6|MPPD<br>O5|MPPD<br>O4|MPPD<br>O3|MPPD<br>O2|MPPD<br>O1|MPPD<br>O0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|Mask Field 15|
|MASK15|Masks MPPDO15 in the same MPGPDOn register instance.<br>0b - MPPDO15 is ignored<br>1b - MPPDO15 is written|
|30<br>MASK14|Mask Field 14<br>Masks MPPDO14 in the same MPGPDOn register instance.<br>0b - MPPDO14 is ignored<br>1b - MPPDO14 is written|
|29<br>MASK13|Mask Field 13<br>Masks MPPDO13 in the same MPGPDOn register instance.<br>0b - MPPDO13 is ignored<br>1b - MPPDO13 is written|
|28<br>MASK12|Mask Field 12<br>Masks MPPDO12 in the same MPGPDOn register instance.<br>0b - MPPDO12 is ignored<br>1b - MPPDO12 is written|
|27|Mask Field 11|
|MASK11|Masks MPPDO11 in the same MPGPDOn register instance.<br>0b - MPPDO11 is ignored<br>1b - MPPDO11 is written|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

360 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field<br>26|Function<br>Mask Field 10|
|---|---|
|MASK10|Masks MPPDO10 in the same MPGPDOn register instance.<br>0b - MPPDO10 is ignored<br>1b - MPPDO10 is written|
|25<br>MASK9|Mask Field 9<br>Masks MPPDO9 in the same MPGPDOn register instance.<br>0b - MPPDO9 is ignored<br>1b - MPPDO9 is written|
|24<br>MASK8|Mask Field 8<br>Masks MPPDO8 in the same MPGPDOn register instance.<br>0b - MPPDO8 is ignored<br>1b - MPPDO8 is written|
|23<br>MASK7|Mask Field 7<br>Masks MPPDO7 in the same MPGPDOn register instance.<br>0b - MPPDO7 is ignored<br>1b - MPPDO7 is written|
|22<br>MASK6|Mask Field 6<br>Masks MPPDO6 in the same MPGPDOn register instance.<br>0b - MPPDO6 is ignored<br>1b - MPPDO6 is written|
|21<br>MASK5|Mask Field 5<br>Masks MPPDO5 in the same MPGPDOn register instance.<br>0b - MPPDO5 is ignored<br>1b - MPPDO5 is written|
|20<br>MASK4|Mask Field 4<br>Masks MPPDO4 in the same MPGPDOn register instance.<br>0b - MPPDO4 is ignored<br>1b - MPPDO4 is written|
|19<br>MASK3|Mask Field 3<br>Masks MPPDO3 in the same MPGPDOn register instance.<br>0b - MPPDO3 is ignored<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

361 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - MPPDO3 is written|
|18|Mask Field 2|
|MASK2|Masks MPPDO2 in the same MPGPDOn register instance.<br>0b - MPPDO2 is ignored<br>1b - MPPDO2 is written|
|17<br>MASK1|Mask Field 1<br>Masks MPPDO1 in the same MPGPDOn register instance.<br>0b - MPPDO1 is ignored<br>1b - MPPDO1 is written|
|16|Mask Field 0|
|MASK0|Masks MPPDO0 in the same MPGPDOn register instance.<br>0b - MPPDO0 is ignored<br>1b - MPPDO0 is written|
|15|Masked Parallel Pad Data Out 15|
|MPPDO15|Writes the data register that stores the value to be driven on the pad in output mode.|
|14|Masked Parallel Pad Data Out 14|
|MPPDO14|Writes the data register that stores the value to be driven on the pad in output mode.|
|13|Masked Parallel Pad Data Out 13|
|MPPDO13|Writes the data register that stores the value to be driven on the pad in output mode.|
|12<br>MPPDO12|Masked Parallel Pad Data Out 12<br>Writes the data register that stores the value to be driven on the pad in output mode.|
|11|Masked Parallel Pad Data Out 11|
|MPPDO11|Writes the data register that stores the value to be driven on the pad in output mode.|
|10|Masked Parallel Pad Data Out 10|
|MPPDO10|Writes the data register that stores the value to be driven on the pad in output mode.|
|9|Masked Parallel Pad Data Out 9|
|MPPDO9|Writes the data register that stores the value to be driven on the pad in output mode.|
|8|Masked Parallel Pad Data Out 8|
|MPPDO8|Writes the data register that stores the value to be driven on the pad in output mode.|
|7|Masked Parallel Pad Data Out 7|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

362 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|MPPDO7|Writes the data register that stores the value to be driven on the pad in output mode.|
|6|Masked Parallel Pad Data Out 6|
|MPPDO6|Writes the data register that stores the value to be driven on the pad in output mode.|
|5|Masked Parallel Pad Data Out 5|
|MPPDO5|Writes the data register that stores the value to be driven on the pad in output mode.|
|4|Masked Parallel Pad Data Out 4|
|MPPDO4|Writes the data register that stores the value to be driven on the pad in output mode.|
|3|Masked Parallel Pad Data Out 3|
|MPPDO3|Writes the data register that stores the value to be driven on the pad in output mode.|
|2|Masked Parallel Pad Data Out 2|
|MPPDO2|Writes the data register that stores the value to be driven on the pad in output mode.|
|1|Masked Parallel Pad Data Out 1|
|MPPDO1|Writes the data register that stores the value to be driven on the pad in output mode.|
|0|Masked Parallel Pad Data Out 0|
|MPPDO0|Writes the data register that stores the value to be driven on the pad in output mode.|



### 9.4.35 SIUL2 Masked Parallel GPIO Pad Data Out Register (MPGPDO14) 

##### Offset 

|Register|Offset|
|---|---|
|MPGPDO14|17B8h|



##### Function 

Each MPGPDOn register selectively modifies the pad values associated with PGPDOn. 

~~<mark>NOTE</mark>~~ 

MPGPDOn registers must only be accessed with 32-bit writes. 8-bit or 16-bit writes will not modify any bits in the register and cause a transfer error. Read access will return 0. 

~~<mark>NOTE</mark>~~ 

MPGPDOn registers support only 32-bit accesses. Byte and half-word accesses are not supported. 

Accesses to each MPGPDOn register location is coherent with access to the bit-wise GPDOn. 

For a given MPGPDOx[MPPDOy] where x is the register instance index and y is the field index, the following equation shows the equivalent GPDOn[PDO_n] bit: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

363 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

MPGPDOx[MPPDOy] = GPDO(x Á 16) + (15 - y)[PDO_(x Á 16) + (15 - y)] 

Some examples of the mapping: 

- MPGPDO0[MPPDO15] = GPDO0[PDO_0] 

- MPGPDO2[MPPDO15] = GPDO32[PDO_32] 

- MPGPDO31[MPPDO0] = GPDO511[PDO_511] 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|W|MASK<br>15|MASK<br>14|MASK<br>13|MASK<br>12|MASK<br>11|MASK<br>10|MASK<br>9|MASK<br>8|MASK<br>7|MASK<br>6|MASK<br>5|MASK<br>4|MASK<br>3|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|W|MPPD<br>O15|MPPD<br>O14|MPPD<br>O13|MPPD<br>O12|MPPD<br>O11|MPPD<br>O10|MPPD<br>O9|MPPD<br>O8|MPPD<br>O7|MPPD<br>O6|MPPD<br>O5|MPPD<br>O4|MPPD<br>O3|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|Mask Field 15|
|MASK15|Masks MPPDO15 in the same MPGPDOn register instance.<br>0b - MPPDO15 is ignored<br>1b - MPPDO15 is written|
|30<br>MASK14|Mask Field 14<br>Masks MPPDO14 in the same MPGPDOn register instance.<br>0b - MPPDO14 is ignored<br>1b - MPPDO14 is written|
|29|Mask Field 13|
|MASK13|Masks MPPDO13 in the same MPGPDOn register instance.<br>0b - MPPDO13 is ignored<br>1b - MPPDO13 is written|
|28<br>MASK12|Mask Field 12<br>Masks MPPDO12 in the same MPGPDOn register instance.<br>0b - MPPDO12 is ignored<br>1b - MPPDO12 is written|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

364 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

Table continued from the previous page... 

|Field<br>27<br>MASK11|Function<br>Mask Field 11<br>Masks MPPDO11 in the same MPGPDOn register instance.<br>0b - MPPDO11 is ignored<br>1b - MPPDO11 is written|
|---|---|
|26<br>MASK10|Mask Field 10<br>Masks MPPDO10 in the same MPGPDOn register instance.<br>0b - MPPDO10 is ignored<br>1b - MPPDO10 is written|
|25<br>MASK9|Mask Field 9<br>Masks MPPDO9 in the same MPGPDOn register instance.<br>0b - MPPDO9 is ignored<br>1b - MPPDO9 is written|
|24<br>MASK8|Mask Field 8<br>Masks MPPDO8 in the same MPGPDOn register instance.<br>0b - MPPDO8 is ignored<br>1b - MPPDO8 is written|
|23<br>MASK7|Mask Field 7<br>Masks MPPDO7 in the same MPGPDOn register instance.<br>0b - MPPDO7 is ignored<br>1b - MPPDO7 is written|
|22<br>MASK6|Mask Field 6<br>Masks MPPDO6 in the same MPGPDOn register instance.<br>0b - MPPDO6 is ignored<br>1b - MPPDO6 is written|
|21<br>MASK5|Mask Field 5<br>Masks MPPDO5 in the same MPGPDOn register instance.<br>0b - MPPDO5 is ignored<br>1b - MPPDO5 is written|
|20<br>MASK4|Mask Field 4<br>Masks MPPDO4 in the same MPGPDOn register instance.<br>0b - MPPDO4 is ignored<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

365 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - MPPDO4 is written|
|19|Mask Field 3|
|MASK3|Masks MPPDO3 in the same MPGPDOn register instance.<br>0b - MPPDO3 is ignored<br>1b - MPPDO3 is written|
|18<br>—|Reserved<br>Always write zero to this field.|
|17<br>—|Reserved<br>Always write zero to this field.|
|16<br>—|Reserved<br>Always write zero to this field.|
|15|Masked Parallel Pad Data Out 15|
|MPPDO15|Writes the data register that stores the value to be driven on the pad in output mode.|
|14|Masked Parallel Pad Data Out 14|
|MPPDO14|Writes the data register that stores the value to be driven on the pad in output mode.|
|13|Masked Parallel Pad Data Out 13|
|MPPDO13|Writes the data register that stores the value to be driven on the pad in output mode.|
|12|Masked Parallel Pad Data Out 12|
|MPPDO12|Writes the data register that stores the value to be driven on the pad in output mode.|
|11|Masked Parallel Pad Data Out 11|
|MPPDO11|Writes the data register that stores the value to be driven on the pad in output mode.|
|10|Masked Parallel Pad Data Out 10|
|MPPDO10|Writes the data register that stores the value to be driven on the pad in output mode.|
|9|Masked Parallel Pad Data Out 9|
|MPPDO9|Writes the data register that stores the value to be driven on the pad in output mode.|
|8|Masked Parallel Pad Data Out 8|
|MPPDO8|Writes the data register that stores the value to be driven on the pad in output mode.|
|7|Masked Parallel Pad Data Out 7|
|MPPDO7|Writes the data register that stores the value to be driven on the pad in output mode.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

366 / 4640 

NXP Semiconductors 

System Integration Unit Lite2 (SIUL2) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|6|Masked Parallel Pad Data Out 6|
|MPPDO6|Writes the data register that stores the value to be driven on the pad in output mode.|
|5|Masked Parallel Pad Data Out 5|
|MPPDO5|Writes the data register that stores the value to be driven on the pad in output mode.|
|4|Masked Parallel Pad Data Out 4|
|MPPDO4|Writes the data register that stores the value to be driven on the pad in output mode.|
|3|Masked Parallel Pad Data Out 3|
|MPPDO3|Writes the data register that stores the value to be driven on the pad in output mode.|
|2|Reserved|
|—|Always write zero to this field.|
|1|Reserved|
|—|Always write zero to this field.|
|0|Reserved|
|—|Always write zero to this field.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

367 / 4640 

