NXP Semiconductors 

# Chapter 40 Power Management 

## 40.1 Introduction 

The power management system generates, monitors, and controls power supplies and related resets. This chapter describes the system's interaction with other peripherals. 

The power management system includes the following modules: 

Table 215. Power management system modules and their functions 

|Part|Function|
|---|---|
|MC_ME|Initiates entry into Low-Power mode|
|MC_PCU|Controls entry into and exit from Low-Power mode|
|PMC|Regulates and monitors power supplies of the Run and the<br>Standby domains|
|MC_RGM|Ensures a clean state and Run domain sanity by controlling the<br>reset sequence|
|FIRC, WKPU, and other chip peripherals|Controls Standby mode wake-up and operations in Run and<br>Standby modes|



Power management system for S32K344, S32K324, S32K314, S32K341, S32K342, and S32K322 and Power management system for S32K312 and S32K311 represent block diagrams of the power management system for the S32K3xx family. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1380 / 4640 

NXP Semiconductors 

Power Management 

### 40.1.1 Power management system for S32K344, S32K324, S32K314, S32K341, S32K342, and S32K322 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/040_Power_Management/S32K3XXRM_数据表.pdf-1381-03.png)


<!-- Start of picture text -->
VC_BJT<br>Optional<br>COUT_V15<br>VDD_HV_A<br>Last Mile SOG Pads<br>distributed LPCMP_ n ADC_ n<br>(Standby)<br>LPM Boot FPM regulator GPIO<br>PMC<br>SOG<br>V11_STANDBY (Run)<br>V11_STANDBY<br>VSS<br>SW*<br>V25 32 K B<br>SRAM VDD_HV_B<br>SIRC FIRC SXOSC<br>Pads<br>V11_RUN<br>GPIO<br>Registers V11_STANDBY<br>FXOSC<br>PIT_0<br>MC_RGM<br>(RTI) VSS<br>Flash<br>memory WKPU RTC<br>PLLDIG<br>MC_PCU DCM<br>TempSense<br>(Double bond) (Double bond)<br>- Standby domain<br>- Standby domain (optional)<br>SW* - On during FPM (Run mode) only<br>VDD_HV_B VDD_HV_A VRC_CTRL V15 VREFH VREFL<br>VSS V25 V11<br><!-- End of picture text -->

Figure 150. Power management system for S32K344, S32K324, S32K314, S32K341, S32K342, and S32K322 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1381 / 4640 

NXP Semiconductors 

Power Management 

### 40.1.2 Power management system for S32K312 and S32K311 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/040_Power_Management/S32K3XXRM_数据表.pdf-1382-03.png)


<!-- Start of picture text -->
VDD_HV_A<br>SOG Pads<br>LPCMP_ n ADC_ n<br>(Standby)<br>FPM LPM GPIO<br>PMC<br>SOG<br>(Run)<br>V11_STANDBY<br>VSS<br>SW*<br>V25 32 K B<br>SRAM<br>SIRC FIRC SXOSC<br>Not available<br>V11_RUN in the S32K311<br>Registers V11_STANDBY<br>FXOSC<br>PIT_0<br>MC_RGM<br>(RTI)<br>Flash<br>memory WKPU RTC<br>PLLDIG<br>MC_PCU DCM<br>TempSense<br>(Double bond) (Double bond)<br>- Standby domain<br>- Standby domain (optional)<br>SW* - On during FPM (Run mode) only<br>VDD_HV_A VREFH VREFL<br>VSS V25 V11<br><!-- End of picture text -->

Figure 151. Power management system for S32K312 and S32K311 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1382 / 4640 

NXP Semiconductors 

Power Management 

### 40.1.3 Power management system for S32K358 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/040_Power_Management/S32K3XXRM_数据表.pdf-1383-03.png)


<!-- Start of picture text -->
optional [See footnotes]<br>VIN<br>VC_BJT<br>COUT_V15<br>optional<br>[See footnotes]<br>VDD_HV_A<br>LPM (V15)<br>Last Mile SOG<br>SMPS distributed LPCMP_ n ADC_ n Pads<br>(Standby)<br>regulator GPIO<br>PMC LPM FPM<br>SOG<br>V11_STANDBY V11_STANDBY (Run) VSS<br>SW*<br>V25 64 kB<br>VDD_HV_B<br>SRAM<br>SIRC FIRC SXOSC Pads<br>GPIO<br>V11_RUN<br>Registers V11_STANDBY<br>VSS<br>FXOSC<br>PIT_0<br>MC_RGM<br>Flash PLLDIG0 (RTI)<br>memory<br>WKPU RTC<br>TempSense<br>MC_PCU DCM<br>PLLDIG1<br>(Triple bond) (Triple bond)<br>- Standby domain<br>- Standby domain (optional)<br>SW* - On during FPM (Run mode) only<br>The V15 input voltage can be supplied directly by an SBC or Voltage regulator. The S32K3x8 devices provide two options to derive the V15 regulator from the 5V or 3.3V supply.<br>Option 1: A DC/DC converter (SMPS) regulator can be implemented by connecting the external components (PMOS, inductor, diode) shown in the figure above, at pins VDD_DCDC,<br>PMOS_CTRL, and VSS_DCDC. In this case, VRC_CTRL must not be connected. VDD_DCDC must be connected to the VDD_HV_A or VDD_HV_B, supply voltage. In this<br>VDD_HV_B VDD_DCDC PGATE_CTRL VSS_DCDC VDD_HV_A VRC_CTRL V15 VREFH VREFL<br>VSS V25 V11<br><!-- End of picture text -->


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/040_Power_Management/S32K3XXRM_数据表.pdf-1383-04.png)


<!-- Start of picture text -->
Option 2: A linear regulator can be implemented by connecting a bipolar NPN transistor from the VDD_HV_A or VDD_HV_B, supply voltage shown as VC_BJT in the figure above. The<br>VRC_CTRL pin must be connected to the base of the transistor. In this case, VDD_DCDC, PMOS_CTRL must not be connected. VSS_DCDC must be connected to MCU GND.<br>In this option, COUT_V15 is specified in Recommended decoupling capacitors.<br><!-- End of picture text -->


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/040_Power_Management/S32K3XXRM_数据表.pdf-1383-05.png)


<!-- Start of picture text -->
Figure 152. Power management system for S32K358<br><!-- End of picture text -->

### 40.1.4 Features 

- Includes a linear regulator to use an optional external ballast (BJT) and VRC_CTRL output for 1.5 V generation. PMC uses 1.5 V supply and an internal regulator to generate 1.1 V (nominal) supply (V11_RUN) for the core logic 

- Supports a low-power regulator (LPM) supplying core logic during Standby mode (V11_STANDBY) 

- Includes two regulators for driving the logic in Run mode (both can be software-controlled): 

   - Boot (Applicable for S32K3x4 and S32K3x2) 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1383 / 4640 

NXP Semiconductors 

Power Management 

   - Last-mile (FPM) 

   - SMPS regulator to generate 1.5V (Applicable for S32K3x8 only) 

- Supports power switches to isolate voltage islands and configure the chip in Standby mode 

- S32K358 supports a DC-DC buck converter stage, with a dedicated pin to control an external Power MOSFET in the range from 1.4V to 1.5V. 

- In S32K358, a high voltage detection (HVD) monitor monitors the 1.5V supply, including a status bit, a flag and an interrupt option. 

- Includes a linear regulator that generates a 2.5 V supply (V25) from VDD_HV_A 

- Supports voltage monitors ensuring transitions to a safe state (POR) when a supply is out of a valid range 

- Controls power-mode transitions through an interaction with the digital interface 

- Offers a padkeeping feature that retains I/O configuration after exiting Standby mode 

- Separates ADC reference supplies (VREFH and VREFL) 

### 40.1.5 Operational power modes 

This chip uses two modes: 

- Run mode (FPM): Main operation mode having full-chip performance and a higher current consumption as compared to Standby mode. 

- Standby mode (LPM): Low-performance mode of the chip in which the Run domain is turned off. Most of the cores and peripherals turn off in this mode. 

The boot regulator manages the chip during the booting process. 

The last-mile regulator is the full-performance regulator, which you enable for running applications. The upcoming sections discuss the sequence to enable or disable the regulator. 

The LPM regulator manages the chip in Standby mode. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1384 / 4640 

NXP Semiconductors 

Power Management 

### 40.1.6 External 1.5 V source 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/040_Power_Management/S32K3XXRM_数据表.pdf-1385-03.png)


<!-- Start of picture text -->
Power supply S32K3xx<br>VDD_HV_A<br>5 V VDD_HV_B<br>1.5 V V15<br>Power supply S32K3xx<br>VDD_HV_A<br>3.3 V VDD_HV_B<br>1.5 V V15<br>Power supply S32K3xx<br>5 V VDD_HV_A<br>3.3 V VDD_HV_B<br>1.5 V V15<br><!-- End of picture text -->

Figure 153. External 1.5 V source 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1385 / 4640 

NXP Semiconductors 

Power Management 

### 40.1.7 Using a BJT for 1.5 V generation 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/040_Power_Management/S32K3XXRM_数据表.pdf-1386-03.png)


<!-- Start of picture text -->
Power supply S32K3xx<br>VDD_HV_A<br>5 V VDD_HV_B<br>VRC_CTRL<br>V15<br>Power supply S32K3xx<br>VDD_HV_A<br>3.3 V VDD_HV_B<br>VRC_CTRL<br>V15<br>Power supply S32K3xx<br>5 V VDD_HV_A<br>3.3 V VDD_HV_B<br>VRC_CTRL<br>V15<br><!-- End of picture text -->

Figure 154. Using a BJT for 1.5 V generation 

## 40.2 Power-up sequence 

Figure 155 shows the reset sequence for a power-up or Standby mode event. This sequence starts from the POR phase. For the Run domain logic, Standby mode exit operation is same as power-up. 

See the Reset Overview chapter for more information about the chip reset sequence. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1386 / 4640 

NXP Semiconductors 

Power Management 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/040_Power_Management/S32K3XXRM_数据表.pdf-1387-02.png)


<!-- Start of picture text -->
Chip<br>power-up<br>Keep chip in POR<br>Power-on reset V > VtPOR No Run-domain POR<br>sequence proceeds<br>Yes<br>FIRC powers on Run-domain destructive<br>Wait for FIRC stabilization reset sequence proceeds STANDBY_ENTRY_SW1<br>Peripheral shutdown<br>Destructive reset Run-domain functional<br>sequence proceedsDestructive reset reset sequence proceeds STANDBY_ENTRY_SW2<br>Application core shutdown<br>Functional reset Functional reset Flash memory initialization<br>sequence proceeds Flash memory scanning STANDBY_ENTRY_SW3<br>Trim loading Flash memory or PMC<br>Chip out of reset in normal Run mode low-power handshake<br>Standbyexit? Yes Security functions disabled STANDBY_ENTRY_SW4Main core shutdown Run<br>No Security functions enabled<br>sBAF initialization code Change FIRC_DIV to DIV1Enable FXOSC, PLL (Configurable) lsolations in between Run andstandby logic enabled<br>Boot header parsing<br>XRDC configurations<br>HSE_FW verification CAAM_RNG initialization<br>Debug authorization MC_RGM asserts all<br>resets to Run domain<br>CAAM_RNG initialization<br>NoSecureboot? Yes HSE_FW boot Application bootOS initializationHSE_FW initialization code PMC moves to LPM regulatorand device enters standby<br>Standby recovery initialization<br>Run sBAF enabling application core Application core VTOR change event detectedWake-up Yes Wake-up sequence proceeds withPMC moving to run regulation<br>Standby<br>HSE_FW enabling application core no<br>Remain in<br>Standby mode<br>self-test?Trigger Yes Execute self-test Legend:<br>No Hardware<br>HSE_B sBAF<br>Enter Yes Continue to standby<br>Standby mode software entry HSE_B firmware<br>No Application core<br>software<br>Continue to application Note: HSE_FW and application sizes are 128 KB each<br><!-- End of picture text -->


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/040_Power_Management/S32K3XXRM_数据表.pdf-1387-03.png)


<!-- Start of picture text -->
Figure 155. Power-up sequence<br><!-- End of picture text -->

## 40.3 PMC last-mile regulator auto-enable feature 

PMC includes an automatic last-mile auto-enable feature. After starting on boot regulator, this feature allows automatic switch over to last-mile regulator if 1.5 V is present during: 

- Chip startup 

- Standby mode recovery 

You can control the PMC last-mile regulator by appropriately configuring: 

- PMC's CONFIG[LMAUTOEN] field 

- PMC's CONFIG[LM_EN] field 

For more information, see the descriptions of these fields in PMC's CONFIG register. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1387 / 4640 

NXP Semiconductors 

Power Management 

~~<mark>NOTE</mark>~~ 

You must write 1 to PMC's CONFIG[LM_EN] field before transtioning to faster clock frequencies irrespective of the setting of PMC's CONFIG[LMAUTOEN] field. This is because of the reduced clock speed when using the boot regulator. 

### 40.3.1 Last-mile regulator with 1.5 V from an external source 

Table 216. Last-mile regulator with 1.5 V from an external source 

|Operating condition|Last-mile regulator operation|
|---|---|
|After POR|Boots on boot regulator and then automatically switches to the last-mile regulator|
|After destructive reset|Remains on last-mile regulator|
||If the destructive reset source is low voltage reset on 1.1 V then<br>switchback happens from last-mile to boot regulator for boot.<br>~~NOTE~~|
|After functional reset|Remains on last-mile regulator|
|After PMC's LVSC[LVD15S] field<br>becomes 1|Switches, automatically, to the boot regulator to configure clocks for slow speed|



### 40.3.2 Last-mile regulator using a BJT 

Table 217. Last-mile regulator using a BJT 

|Operating condition|Last-mile regulator operation|
|---|---|
|After POR|Boots on boot regulator; switches to the last-mile regulator post reset when the Cortex-M7<br>core configures the software (post-secure boot) on FIRC (100 ms)|
|After destructive reset|Switches to boot regulator to check reset propagation delay|
|After functional reset|Remains on last-mile regulator|
|After PMC's LVSC[LVD15S]<br>field becomes 1|Switches, automatically, to boot regulator to configure clocks for slow speed|



## 40.4 Standby mode entry sequence 

The Standby mode entry sequence includes three phases of operation: 

- Standby mode entry configuration phase or software Standby mode entry sequence 

- Standby mode entry handshake phase or hardware Standby mode entry sequence 

- Standby mode entry or PMC Standby mode entry 

~~<mark>NOTE</mark>~~ 

The Standby mode entry sequence described in this section is the only supported sequence. Contact NXP support if you require an alternate Standby mode entry sequence. 

### 40.4.1 Software Standby mode entry sequence 

The Standby mode entry sequence discusses chip configuration described in the sections that follow. 

Before entering the software Standby mode sequence, the system clock source must be changed to FIRC because PLLDIG is not available in Standby mode. In this mode, all clock sources can be optionally disabled (including FIRC, which results in a no-clock, 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1388 / 4640 

NXP Semiconductors 

Power Management 

low-power consumption mode). You could use FXOSC, if enabled, when the 2.5 V supply is available by appropriate configuration of PMC's CONFIG[LPM25EN]. 

The software Standby mode entry sequence consists of four steps: 

1. SW1: Module shutdown process 

2. SW2: Application core shutdown process 

3. SW3: Flash memory low-power handshake and PMC last-mile regulator control 

4. SW4: Main core shutdown process 

These processes are described in detail in the sections that follow. See Figure 155 that shows the relationship between these four steps in a flow diagram. 

#### 40.4.1.1 SW1: Module shutdown process 

I/O and module configuration for Standby mode discusses the procedure to configure I/O and the chip modules for Standby mode. 

The entry sequence for this mode includes module clock disabling steps (see the "Clocking" chapter for module clock turn on and turn off processes). You must use MC_ME's PRTNn_COFBm_CLKEN[REQp] fields to enable or disable module clocks. 

#### 40.4.1.1.1 Disabling modules 

Disable modules by configuring the appropriate fields in their registers for Standby mode operation. See specific module chapters for more information. 

The Standby mode entry sequence includes the module clock disabling step, with which you can disable the modules that you do not need for Standby mode operation. 

The sequence of disabling modules is shown in I/O and module configuration for Standby mode. 

~~<mark>NOTE</mark>~~ 

While enabling or disabling the modules, you must verify that the module is disabled when you read MC_ME's PRTNn_COFBm_STAT register and the module disable field, if applicable. In case of a discrepancy, you must perform proper diagnostic steps. 

You must clear the I/O controls for the pads that you do not require in Standby mode (OBE, IBE, and so on). This avoids any unwanted pad keeping settings. See Pad keeping for more information on the chip pad keeping process. 

For any standby wake source, if an interrupt occurs it must be disabled before entering into standby and only the wake up event of that source must be enabled. This is to avoid any SW conflict in the interrupt handling for multi application core cases. 

The MC_ME's PRTNn_COFBm_STAT register indicates the status of peripheral clock enable or disable. It may take up to three clock cycles for MC_ME's PRTNn_COFBm_STAT register to update after MC_ME's PRTNn_COFBm_CLKEN register is updated. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1389 / 4640 

NXP Semiconductors 

Power Management 

#### 40.4.1.1.2 I/O and module configuration for Standby mode 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/040_Power_Management/S32K3XXRM_数据表.pdf-1390-03.png)


<!-- Start of picture text -->
Initiate Standby sequence<br>Clear all pending interrupts<br>Disable all communications<br>(QuadSPI, EMAC, and so on)<br>Have all<br>No<br>communications<br>stopped?<br>Yes<br>As needed, configure the associated<br>MC_ME.PRTN n _COFB m _CLKEN<br>fields for Standby mode<br>Are all necessary No<br>MC_ME.PRTN n _COFB m _STAT<br>fields 0?<br>Yes<br>Before switching to<br>FIRC_CLK, you must<br>Configure entire chip to<br>take the necessary<br>only use FIRC_CLK<br>precautions to avoid<br>clock glitches.<br>Need fast startup No<br>of FXOSC_CLK after<br>Standby exit?<br>Yes<br>Not recommended if<br>minimum power Verify PMC.CONFIG[LPM25EN]<br>Configure FXOSC_CLK for<br>consumption is needed. equals 0 disabling 2.5 V<br>Use if faster FXOSC operation after Standby mode during Standby mode<br>start is required.<br>Write 1 to<br>PMC.CONFIG[LPM25EN]<br>Write 0 to<br>See the ‘’Padkeeping’’<br>section for details. DCM.DCMRWF1[STANDBY_IO_CONFIG]<br>to enable padkeeping<br>Write 1 to SIUL2.MSCR n [PKE]<br>of the I/O that you want active in<br>Standby mode<br>Configure SIUL2.MSCR<br>for the function of the I/O<br>during Standby mode<br>Configure module registers<br>used in Standby mode<br>Application core shutdown<br><!-- End of picture text -->


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/040_Power_Management/S32K3XXRM_数据表.pdf-1390-04.png)


<!-- Start of picture text -->
Figure 156. I/O and module configuration for Standby mode<br>S32K3xx Reference Manual, Rev. 4, 04/2022<br><!-- End of picture text -->


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/040_Power_Management/S32K3XXRM_数据表.pdf-1390-05.png)


<!-- Start of picture text -->
Preliminary Information<br><!-- End of picture text -->

Reference Manual 

1390 / 4640 

NXP Semiconductors 

Power Management 

#### 40.4.1.2 SW2: Application core shutdown process 

The application cores(s) execute a WFI (as opposed to the main core running the Standby mode entry sequence). See the section "Application core shutdown" in the MC_ME chapter for more information. 

The main core configuration (programming valid core ID and enabling standby entry process) and wake-up source configuration must also be set in SW2, so that SW4 contains only the main core WFI execution. 

#### 40.4.1.3 SW3: Flash memory low-power handshake and PMC last-mile regulator 

In this process, you execute a flash memory low-power handshake and disable the PMC last-mile regulator by executing the procedures indicated in Figure 157 and Figure 158 . 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/040_Power_Management/S32K3XXRM_数据表.pdf-1391-07.png)


<!-- Start of picture text -->
Flash memory<br>disable<br>Initiate a flash memory<br>handshake to cofirm no high<br>voltage operations are in process<br>High voltage<br>Yes<br>flash memory operation<br>in progress?<br>No<br>PLLDIG not on during Disable PLLDIG by writing zero<br>Standby mode. to PLLDIG.PLLCR[PLLPD]<br>FIRC.STDBY_ENABLE[STDBY_ENABLE] Configure SIRC, FXOSC, and<br>SIRC.MISCELLANEOUS_IN[STANDBY_ENABLE]<br>SXOSC as needed for Standby<br>FXOSC.CTRL[OSCON] mode<br>SXOSC.SXOSC_CTRL[OSCON]<br>Configure the V25 regulator for<br>operation in Standby mode<br>Configure the following DCM register fields as needed:<br>DCMRWF2[PMC_TRIM_RGM_DCF__BYP_STDBY_EXT]<br>DCMRWF2[FIRC_TRIM_BYP_STDBY_EXT]<br>DCMRWF2[DCM_SCAN_BYP_STDBY_EXT]<br>DCMRWF2[SIRC_TRIM_BYP_STDBY_EXT]<br>Continue Standby<br>mode entry process<br>Figure 157. Flash memory Standby mode configuration<br>  NOTE<br><!-- End of picture text -->

Disable the last-mile regulator according to the Last-mile regulator disable sequence. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1391 / 4640 

NXP Semiconductors 

Power Management 

#### 40.4.1.3.1 Last-mile regulator disable sequence 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/040_Power_Management/S32K3XXRM_数据表.pdf-1392-03.png)


<!-- Start of picture text -->
Disable PMC<br>last-mile regulator<br>Simultaneously write 0 to both<br>PMC.CONFIG[LMEN] and<br>PMC.CONFIG[LMBCTLEN]<br>Software writes GPIO indicating<br>last-mile regulator is disabled<br>External source disables<br>BJT collector voltage<br>Continue Standby mode<br>disable process<br><!-- End of picture text -->

Figure 158. Last-mile regulator disable sequence 

When exiting Standby mode, the 1.1 V capacitor is charging. You can charge the 1.5 V capacitor during or after the 1.1 V capacitor is charged. If you charge the 1.5 V capacitor sequentially after the 1.1 V capacitor, you will need additional time to complete the overall charging process. 

Leaving PMCs CTRL[LMBCTLEN] = 1 saves time when exiting Standby mode and does not draw any additional current during this mode. 

#### 40.4.1.4 SW4: Main core shutdown process 

For information on this process, see these in the "Mode Entry Module (MC_ME)" chapter: 

- Figure "Standby entry sequence along with main core shutdown" 

- Section "Main core shutdown and Standby mode entry" 

You must configure WKPU before disabling interrupts to avoid missing any events as shown in the Standby entry sequence along with main core shutdown flowchart in the MC_ME chapter. You must program WKPU, disable interrupts, and configure MC_ME's Standby mode entry in SW1 (see SW1: Module shutdown process for more information). In SW4, you must perform only the main-core WFI execution. 

### 40.4.2 Hardware Standby mode entry sequence 

The hardware Standby mode entry sequence consists of handshaking between MC_PCU and MC_ME occuring after Software Standby mode entry sequence completes. The FSM in MC_PCU performs these steps automatically and does not require your intervention (see Power sequence FSM in the Power Control Unit (MC_PCU) chapter for more information). 

#### 40.4.2.1 PMC Standby mode entry 

The PMC Standby mode entry sequence starts after Hardware Standby mode entry sequence completes, and consists of these phases: 

1. Standby mode entry acknowledgment and initiation of an internal low-power process on receiving Standby mode entry request 

2. Disabling of the boot regulator within the PMC low-power process. This point is only applicable for S32K3x4 and S32K3x2. 

3. Disabling of the V25 regulator and the FPM LVR monitors 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1392 / 4640 

NXP Semiconductors 

Power Management 

4. Disabling of the V25 regulator (oscillator and flash memory supply) and the LPM monitor, unless it is enabled during Standby mode (see PMC's CONFIG[LPM25EN] field in the PMC chapter for more information) 

5. Disabling of the VDD_HV_B LPM monitors 

## 40.5 Chip status at the end of Standby mode entry sequence 

After PMC Standby mode entry completes, the chip completes Standby mode entry as follows: 

1. Configures Standby domain peripherals according to SW1 (see SW1: Module shutdown process). 

2. Enables pad keeping on pins as described in SW1 (see SW1: Module shutdown process). See Pad keeping for other details. 

3. Powers down all memory types except Standby RAM (in SRAM0). 

   - The V25 regulator can remain on during Standby mode. However, for maximum power savings, it must remain off in this mode. 

4. Isolates Standby and Run domains from each other: 

   - Standby domain is functional. 

   - Run domain is held in reset. 

5. Configures the system clock (FIRC_CLK or PLL_PHIn_CLK, depending on their configuration) and other clock sources according to SW3 (see Figure 157 for the procedure details). 

The cores are off and in the Standby domain. 

6. Turns off the boot and FPM regulators. 

7. Waits for a wake-up event to initiate recovery from Standby mode. 

## 40.6 Chip operation in Standby mode 

This chip supports the following functionalities in Standby mode: 

- STANDBY_RAM content retention during Standby mode. 

- Wake-up from up to 60 digital inputs (for details, see the signals WKUP[n] functions of WKPU module in the IOMUX file attached to this document). The section WKPU configuration on the chip in the "Wakeup Unit (WKPU)" chapter shows mapping of the wake-up sources. 

- Wake-up from up to 16 analog inputs through the Trigger mode functionality (see the signals CMPn_INm functions of CMPn modules in the IOMUX file attached to this document). 

- Wake-up from on-chip timers: 

   - RTI (function of PIT[0]) 

   - SWT0 

   - RTC 

- Ability to configure the chip clocking modules to optionally enable or disable in Standby mode (FIRC, SXOSC, FXOSC, and SIRC). 

## 40.7 Standby mode exit 

This chip supports Standby mode exit from a wake-up, functional reset, or destructive reset event. The sources that cause chip Standby mode exit are: 

- MC_RGM functional reset event 

- MC_RGM destructive reset event 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1393 / 4640 

NXP Semiconductors 

Power Management 

- WKPU wake-up events, WKPU[0]–WKPU[63]. See the WKPU chapter for more information. 

After Standby mode exit, the following events occur (for more information, see "Power sequence FSM" in the MC_PCU chapter for MC_PCU FSM transitions during entry into and exit from Standby mode): 

1. A wake-up event arrives. 

2. FIRC starts powering up (if disabled in Standby mode). 

3. PMC starts the transition process to FPM (for example, enables the last-mile regulator and provides V11_RUN supply to the chip). 

4. MC_PCU removes the isolation between Run and Standby domains. 

5. Run domain reset deasserts (asserts on Standby mode entry) and the chip undergoes a functional reset exit sequence for this domain. 

6. The chip enters Run mode of operation. 

### 40.7.1 Faster Standby mode exit 

The chip supports an optional configuration for faster recovery from Standby mode on the expense of a higher capacitor recharging current. See the CONFIG[FASTREC] field description in the PMC chapter for more information on faster PMC recovery from Standby mode. 

This chip supports an optional feature that bypasses SIRC trimming, FIRC trimming, PMC trimming and DCM scanning phases in case of Standby mode exit sequence by writing 1 to DCM's DCMRWF2[6], DCMRWF2[5], DCMRWF2[4], and DCMRWF2[3] fields respectively before Standby mode entry for bypass operation. This results in a considerable reduction in Standby mode exit duration. The trim values are retained across Standby mode and bypassing these values does not cause any impact. 

### 40.7.2 Last-mile regulator enable sequence 

After Standby mode exit, you must re-enable the PMC last-mile regulator before transitioning to faster clock frequencies. Figure 159 shows the last-mile regulator enable sequence part of the Standby mode exit process. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1394 / 4640 

NXP Semiconductors 

##### Power Management 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/040_Power_Management/S32K3XXRM_数据表.pdf-1395-02.png)


<!-- Start of picture text -->
Enable PMC<br>last-mile regulator<br>Using BJT No<br>for 1.5 V<br>generation?<br>Yes<br>If applicable,<br>Request turn on of 1.5 V<br>turn on BJT collector voltage<br>Write 1 to<br>PMC.CONFIG[LMBCTLEN]<br>PMC<br>No<br>CONFIG[FASTREC]<br>equal 0?<br>Yes<br>Wait 50 µs Wait 15 µs<br>PMC<br>No<br>LVSC[LVD15S]<br>equal 0?<br>Yes<br>Write 1 to PMC.LVSC[LVD15F]<br>to clear flag<br>Write 1 to<br>PMC.CONFIG[LMEN]<br>Yes<br>Do not turn on anything Wait tsettle_lm time before<br>else until after setting proceeding (see data sheet<br>time. for settling time)<br>Continue Standby<br>mode exit process<br><!-- End of picture text -->


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/040_Power_Management/S32K3XXRM_数据表.pdf-1395-03.png)


<!-- Start of picture text -->
Figure 159. Last-mile regulator enable sequence<br><!-- End of picture text -->

## 40.8 Chip power domain partitioning 

These are the modules in the Standby domain. For more information, see "Peripheral reset status" in the "Reset Overview" chapter. 

- FIRC 

- FXOSC 

- MC_RGM 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1395 / 4640 

NXP Semiconductors 

Power Management 

- DCM 

- WKPU 

- PIT_0 (RTI) 

- LPCMP_[0:2] 

- PMC 

- SIRC 

- SXOSC 

- RTC 

- SWT_0 

- DCF clients 

### 40.8.1 Module power status 

Table 218. Module power status 

|PD0 contents|K344|K342|K312|K311|K358|
|---|---|---|---|---|---|
|External<br>Pin wakeups|Minimum 60|Minimum 60|Minimum 60|33 on 100MQFP &<br>12 on 48LQFP|Minimum 60|
|RTC_API|Yes|Yes|Yes|Yes|Yes|
|LPCMP0|Yes|Yes|Yes|Yes|Yes|
|LPCMP1|Yes|Yes|Yes|No|Yes|
|LPCMP2|Yes|No|No|No|Yes|
|SWT0|Yes|Yes|Yes|Yes|Yes|
|WKPU|Yes|Yes|Yes|Yes|Yes|
|PMC|Yes|Yes|Yes|Yes|Yes|
|RGM|Yes|Yes|Yes|Yes|Yes|
|SXOSC(only used<br>for RTC)|Yes|Yes|Yes|No|Yes|
|FXOSC|Yes|Yes|Yes|Yes|Yes|
|FIRC|Yes|Yes|Yes|Yes|Yes|
|SIRC|Yes|Yes|Yes|Yes|Yes|
|CLK OUT|Yes|Yes|Yes|Yes|Yes|
|SRAM|32K|32K|32K|32K|64K|
|PIT_RTI_0|Yes|Yes|Yes|Yes|Yes|
|ATX|Yes|Yes|Yes|Yes|Yes|
|DCM and<br>DCF records|Yes|Yes|Yes|Yes|Yes|
|DCM<br>Flash Interface|Yes|Yes|Yes|Yes|Yes|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1396 / 4640 

NXP Semiconductors 

Power Management 

SWT0 (Cortex-M7_0) resides in the Standby domain and supports a configurable hardware-based timer operation during Standby mode depending on the configuration of SWTs. 

All clock sources (excpet PLLDIG) are available in Standby mode. SIRC is present in the Standby domain for low-power wake-up, but can be enabled. 

~~<mark>NOTE</mark>~~ This chip does not support Stop and Wait modes. The only low-power mode it supports is Standby. 

## 40.9 Pad keeping 

Pad keeping allows you to return to I/O Run mode configuration settings after using I/O during Standby mode. It eliminates I/O reconfiguration in Run mode. 

### 40.9.1 Pad keeping on Run domain pins 

The process of entering Standby mode ensures that the chip maintains the Run domain configuration settings. Software Standby mode entry sequence specifies that you must write 0 to DCM's DCMRWF1[STANDBY_IO_CONFIG] before configuring I/O pad keeping. You could consider DCM's DCMRWF1[STANDBY_IO_CONFIG] field as a global enable for all pad keeping purposes during Standby mode. If you are unable to write to this field as described, pad keeping works as explained in this chapter, during Standby mode. 

After the chip exits Standby mode, you must write 1 to DCM's DCMRWF1[STANDBY_IO_CONFIG] field (see "Chip specific register descriptions" in the DCM chapter). Writing 1 to this field disables pad keeping and places chip I/O according to its Run mode configuration. 

### 40.9.2 Pad keeping on Standby domain pins 

The Standby domain pads can have pad keeping enabled or disabled based on pad availability in Standby mode. Writing to SIUL2's MSCRn[PKE] field configures Standby mode pad keeping on a selected I/O. 

Ensure that DCM's DCMRWF1[STANDBY_IO_CONFIG] = 0 before Standby mode entry for pad keeping on Standby domain pads. Write 0 to the field in case its value is not 0 already. 

If a pad is not required during Standby mode, the corresponding MSCRn[PKE] field in SIUL2 must be 0. 

### 40.9.3 Pad keeping configuration procedure 

This procedure specifies how to enable an I/O for pad keeping: 

1. Configure SIUL2's MSCRn register to control the pad state prior to Standby mode entry (for example, writing 0 to SIUL2's MSCRn[OBE], MSCRn[IBE], and MSCR[PUE] fields tristates the corresponding I/O). 

2. Configure SIUL2's MSCRn[PKE] field as needed for an I/O pad keeping state during Standby mode. 

3. Write 0 to DCM's DCMRWF1[STANDBY_IO_CONFIG]. 

The application core executes WFI, and Standby mode sequence starts. 

4. Write 1 to DCM's DCMRWF1[STANDBY_IO_CONFIG] field on Standby mode exit to disable pad keeping. This configures SIUL2 according to its previous settings. 

If you write 1 to DCM's DCMRWF1[STANDBY_IO_CONFIG] field before entering Standby mode, the isolation removal hardware removes pad keeping on Standby mode exit. This (writing 1 to DCM's DCMRWF1[STANDBY_IO_CONFIG] field before Standby mode entry) is useful in case of low-power debug because enabling pad keeping does not allow low-power debug protocol to work properly (because the TDO pad is padkept). For low-power debug, you must write 1 to DCM's DCMRWF1[STANDBY_IO_CONFIG] field prior to Standby mode entry. 

In case of Standby mode exit by reset, the pad keeping of the reset pin is removed when the chip is reset on Standby mode wake up. See the "GPIO padkeeping enable" signal in Figure 161. The signal corresponds to wake-up via reset event case. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1397 / 4640 

NXP Semiconductors 

Power Management 

### 40.9.4 Pad keeping waveforms 

#### 40.9.4.1 Pad keeping when the chip wakes up from Standby mode via an interrupt event 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/040_Power_Management/S32K3XXRM_数据表.pdf-1398-04.png)


<!-- Start of picture text -->
FIRC_CLK<br>Run domain reset (active low) a f<br>Standby domain reset (active low)<br>Chip isolation enabled after Run Run domain comes out of reset<br>domain is reset on standby entry<br>Run domain isolation b e<br>Isolation is removed on wake-up event and PMC<br>switches from Standby to Run mode gracefully<br>Wake-up event d<br>GPIO padkeeping enabled on isolation enable<br>Padkeeping enable, DCM.DCMRWF1[16] You must write 0 to this GPR GPR must be 1 to remove GPIO padkeeping g<br>before Standby entry.<br>GPIO padkeeping disabled after padkeeping enable GPR is 1<br>GPIO padkeeping enable c h<br><!-- End of picture text -->

Figure 160. Pad keeping when the chip wakes up from Standby mode via an interrupt event 

#### 40.9.4.2 Pad keeping when the chip wakes up from Standby mode via reset 

If the chip exits Standby mode via reset, the reset pad keeping is removed when the chip resets after Standby-mode wake-up. See the figure's "GPIO padkeeping enable" waveform corresponding to wake-up via a reset event. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/040_Power_Management/S32K3XXRM_数据表.pdf-1398-08.png)


<!-- Start of picture text -->
FIRC_CLK<br>Run domain reset (active low) a f g<br>Run domain comes out of reset<br>Standby domain reset (active low)<br>Chip isolation enabled after Run<br>domain is reset on standby entry After graceful Standby exit, the chip undergoes reset<br>(functional/destructive as per the reset event)<br>Run domain isolation b e<br>Isolation is removed on wake-up event and PMC<br>gracefully switches from Standby to Run mode<br>Wake-up event d<br>(functional or destructive reset event)<br>GPIO padkeeping enabled on isolation enable GPIO padkeeping disabled due to reset.<br>GPR configuration is not required.<br>Padkeeping enable, DCM.DCMRWF1[16] You must write 0 to this GPR<br>before Standby entry.<br>GPIO padkeeping enable c h<br><!-- End of picture text -->

Figure 161. Pad keeping when the chip wakes up from Standby mode via reset 

### 40.9.5 SIUL2's fields for actively-driven pins in Standby mode 

If you use a WKPU pin as a wake-up input, perform these operations on SIUL2's fields: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1398 / 4640 

NXP Semiconductors 

Power Management 

1. Write 1 to MSCRx[IBE]. 

2. Program MSCRx[PUE] and MSCRx[PUS] according to the use case. 

3. Write 0 to MSCRx[PKE]. 

For the GPIO pins that are driven to high impedance during Standby mode: 

1. Write 0 to DCM's DCMRWF1[STANDBY_IO_CONFIG] field. 

2. Write 0 to SIUL2's MSCRx[SSS] field (GPIO mode). 

3. Write 0 to SIUL2's MSCRx[IBE] and MSCRx[OBE] fields. 

Some of the pins are, by default, actively driven in Standby mode. If these pins retain a static value throughout the mode, program the corresponding MSCRx[PKE] bits individually. 

This table shows the list of pins available in Standby mode along with the functions they perform. 

Table 219. Active pins in Standby mode 

|Pin<sup>1</sup>|Function|
|---|---|
|GPIO_4|CMP0_OUT|
|GPIO_5|RESET_b|
|GPIO_9|CMP2_OUT|
|GPIO_11|CMP0_RRT|
|GPIO_12|CLKOUT_STANDBY; CMP1_OUT|
|GPIO_69|CMP2_RRT|
|GPIO_110|CMP0_RRT|
|GPIO_131|CMP0_OUT|
|GPIO_138|CLKOUT_STANDBY|
|GPIO_143|CMP1_RRT|
|GPIO_158|CMP1_OUT|
|GPIO_159|CMP1_RRT|
|GPIO_174|CMP0_OUT|
|GPIO_175|CMP0_RRT|
|GPIO_196|CMP2_OUT|
|GPIO_197|CMP2_RRT|



1. See the IOMUX sheet attached to this document for details on pins configuration in different chips. 

## 40.10 Glossary 

Application core Core apart from the main core 

Boot regulator The on chip 1.1 V regulator that is active during startup and entry and exit from Standby mode FSM Finite state machine FPM Full-power mode (Run mode)—uses the last-mile regulator and 1.5 V source to generate the 1.1 V core logic supply during a full-power operation (V11_RUN) 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1399 / 4640 

NXP Semiconductors 

Power Management 

|LPM|Low-power mode (Standby mode)—uses the low-power regulator to generate the 1.1 V core logic supply<br>during low-power operation (V11_STANDBY)|
|---|---|
|LVR|Low voltage reset|
|Main core|Core initiating the chip Standby mode request (for example, the core corresponding to the "core index" in<br>MC_ME's MAIN_COREID register)|
|Pad keeping|Maintains I/O pad configuration during Standby mode, if enabled|
|V11_STANDBY|Core logic and clock sources, low-voltage supply to Standby domain|
|V11_RUN|Low-voltage supply to Run domain|
|V15|High-current input for core or logic supply from either an external BJT or from direct 1.5 V external supply|
|V25|Flash memory, FXOSC, and PLLDIG high-voltage supply|
|VDDA_ADC|ADC supply voltage|
|VREFH|ADC high-voltage reference supply|
|VREFL|ADC low-voltage reference supply|
|VSS|Core logic ground supply|
|VDD_HV_A|Main I/O voltage supply (5 V or 3.3 V)|
|VDD_HV_B|Other I/O domain voltage supply (5 V or 3.3 V)|
|VRC_CTRL|PMC voltage regulator control output using the BJT option to generate a 1.5 V supply|
|WFI|Wait for interrupt software instruction|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1400 / 4640 

