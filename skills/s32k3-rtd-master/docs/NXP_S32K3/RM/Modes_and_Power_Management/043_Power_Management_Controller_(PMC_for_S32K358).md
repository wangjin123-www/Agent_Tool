NXP Semiconductors 

# Chapter 43 Power Management Controller (PMC for S32K358) 

## 43.1 Introduction 

PMC is the power management controller for the S32K3 family of microcontrollers. It provides multiple power options to allow you to optimize power consumption for the level of functionality needed. It includes internal voltage regulators, POR, and the integrated low/high voltage detect system with reset (brown-out) capability. The voltage regulator requires a 3.3 V or 5 V input to generate all the required secondary supplies. 

## 43.2 Features 

PMC includes the following features: 

- Combination of internal and external voltage regulator options, offering RUN and Standby modes 

- Active POR providing brown-out detect 

- LVR for all system-relevant power domains 

- LVD and HVD as indication for software 

## 43.3 Modes of operation 

PMC provides two basic modes of operation for the voltage regualtors and monitors: 

- FPM, which is used on chip-level in RUN modes: For high-current consumption 

- LPM, which is used on chip-level for Standby modes: For low-current consumption 

## 43.4 Block diagram 

The following figure shows the block diagram for this module. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1426 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K358) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/043_Power_Management_Controller_-PMC_for_S32K358-/S32K3XXRM_数据表.pdf-1427-02.png)


<!-- Start of picture text -->
optional<br>VIN<br>VC_BJT<br>optional<br>VDD_HV_A<br>LPM (V15)<br>Last Mile SOG<br>SMPS (DCDC) distributed LPCMP_ n (Standby) ADC_ n Pads<br>regulator GPIO<br>PMC LPM FPM<br>SOG<br>V11_STANDBY V11_STANDBY (Run) VSS<br>SW*<br>V25 64 kB<br>VDD_HV_B<br>SRAM<br>SIRC FIRC SXOSC Pads<br>GPIO<br>V11_RUN<br>Registers V11_STANDBY<br>VSS<br>FXOSC<br>PIT_0<br>Flash PLLDIG0 MC_RGM (RTI)<br>memory<br>WKPU RTC<br>TempSense<br>MC_PCU DCM<br>PLLDIG1<br>(Triple bond) (Triple bond)<br>- Standby domain<br>- Standby domain (optional)<br>SW* - On during FPM (Run mode) only<br>VDD_HV_B VDD_DCDC PMOS_CTRL VSS_DCDC VDD_HV_A VRC_CTRL V15 VREFH VREFL<br>VSS V25 V11<br><!-- End of picture text -->

Figure 164. PMC block diagram 

## 43.5 Signals 

This table describes the PMC module signals. 

Table 222. Signal Description 

|Signal|I/O|Description|
|---|---|---|
|VDD_HV_A|Supply input|This is the primary high-voltage supply input to PMC. VDD_HV_A is<br>used for the PMC internal precision references. After the VDD_HV_A<br>domain is powered up, it must be kept powered at all times of<br>operation (FPM and LPM).|
|VDD_HV_B|Supply input|This is the secondary high-voltage supply input supervised by the<br>PMC. After the VDD_HV_B domain is powered up, it must be kept<br>powered at all times of operation (FPM and LPM).|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1427 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K358) 

Table 222. Signal Description (continued) 

|Signal|I/O|Description|
|---|---|---|
|V25|Supply output|V25 power supply domain is driven by a fully integrated low-dropout<br>linear voltage regulator. It supplies the Flash memory and (via a<br>double bond) the clock modules.|
|V15|Supply input|This is the high-current input for core/logic supply that can be fed by<br>an external BJT or the SMPS or an external source.|
|VRC_CTRL|Output|VRC_CTRL connects to the base of external BJT, if this option is used<br>to generate V15.|
|V11|Supply output|V11 is the core/logic supply. It is driven by a fully integrated low-<br>dropout linear voltage regulator.|
|VSS|Ground|VSS must be grounded. All VSS Pins need to be externally connected<br>to the same ground node.|
|VDD_DCDC|SMPS supply<br>input|This is the power supply domain for the SMPS gate driver and must<br>be shorted with the source voltage of the external power FET. Off-<br>chip decoupling capacitor (10uF or larger) between VDD_DCDC and<br>ground is required.|
|VSS_DCDC|SMPS ground|This is the power ground for the SMPS gate driver and must be<br>shorted with the main ground node and the ground node of the<br>external Schottky diode.|
|PMOS_CTRL|PMOS Control,<br>SMPS Gate<br>Drive output|This is the gate driver output for the external power FET. In case<br>Switched-mode power supply feature is not used (software can clear<br>CONFIG register: LMSPMSEN=0) this pin can be used as general<br>purpose output. If used as general purpose output the following must<br>be considered:<br>• As SMPS is enabled by default (LMSMPSEN=1) the pin can<br>behave randomly during startup phase.<br>• If LMSMPSEN=0 then during low power mode the PMOS_CTRL<br>is forced to VDD_DCDC voltage level, regardless of the output<br>data value that the software has programmed.|



## 43.6 Functional description 

The following sections describe functional details of the PMC. 

### 43.6.1 Reset 

The POR and all LVRs are combined into one single MCU POR. 

After an MCU POR event, it can be determined which power domain caused it, by reading in the PMC_LVSC register, the POR flag, and LVR flags. 

After an initial power ramp up of the MCU in the PMC_LVSC register, the POR flag and the LVR flags are all set to 1. The Go/Nogo flags have an arbitrary value. 

~~<mark>NOTE</mark>~~ 

After an initial power ramp up, all flags in the LVSC register must be cleared (by writing 0xFFFFFFFF to the LVSC register). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1428 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K358) 

Because the flags are sticky bits, it is required to clear them before usage. So, in case of an unxepected MCU POR, the source of the problem can be tracked and debugged by reading the flags in the LVSC register. 

### 43.6.2 Interrupts 

PMC includes two interrupt sources: 

- HVD interrupt: It combines all HVD monitors into one interrupt source. Interrupt enable is the HVDIE field in the CONFIG register. 

- LVD interrupt: This is the interrupt for the LVD5A monitor. Interrupt enable is the LVDIE field in the CONFIG register. 

See the PMC Configuration Register (CONFIG) and Low Voltage Status and Control Register (LVSC) registers for details. 

## 43.7 PMC register descriptions 

### 43.7.1 PMC memory map 

This section includes the PMC module memory map and detailed descriptions for all the registers. 

PMC base address: 402E_8000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|Low Voltage Status and Control Register (LVSC)|32|W1C|See<br>description|
|4h|PMC Configuration Register (CONFIG)|32|RW|0000_0083h|
|8h|SMPS Configuration Register (SMPSCONFIG)|32|RW|See<br>description|
|Ch|Version ID register (VERID)|32|RO|0400_0001h|



### 43.7.2 Low Voltage Status and Control Register (LVSC) 

#### Offset 

|Register|Offset|
|---|---|
|LVSC|0h|



#### Function 

This register contains status and control bits to support the low-voltage reset and low- or high-voltage detect function. When the PMC is in LPM, the low- or high-voltage detect systems are disabled. 

~~<mark>NOTE</mark>~~ 

For all flags that are not affected by reset (POR flag, all LVR flags, all GNG flags), in case a reset occurs at the same time while trying to clear the flags (by writing 1), the flag value is not defined appropriately. In this case, you need to clear the flag again after exit from reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1429 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K358) 

~~<mark>NOTE</mark>~~ 

For the GNG flags, in case a GNG event occurs at the same time as the GNG flag is read, the flag value might not be defined appropriately. In such case, you need to read the flag twice and consider the value only if it both read values match. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/043_Power_Management_Controller_-PMC_for_S32K358-/S32K3XXRM_数据表.pdf-1430-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>GNG1 GNG2 GNG1 GNG2 LVR11 LVR11 LVR25 LVR25 LVRBL LVRB LVRAL LVRA<br>R PORF  0<br>1OS... 5OS... 1OS... 5OS... LPF  F  LPF  F  PF  F  PF  F<br>W W1C W1C W1C W1C W1C W1C W1C W1C W1C W1C W1C W1C W1C<br>Reset u 0 0 0 u u u u u u u u u u u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>HVD1 LVD5A HVD1 HVD2 HVDB HVDA HVD1 LVD5A HVD1 HVD2 HVDB HVDA<br>R 0 0 0<br>5S  Reserv S  1S  5S  S  S  5F  F  1F  5F  F  F<br>ed<br>W W1C W1C W1C W1C W1C W1C<br>Reset 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31<br>PORF|POR flag<br>Indicates that a power-on reset event has occurred. Writing 1 to this field clears it, and other reset<br>sources have no effect.<br>0b - No power-on reset event has occurred<br>1b - Power-on reset event has occurred|
|30-28<br>—|Reserved|
|27<br>GNG11OSC2F|Go/NoGo detect flag on 2nd PLL part of V11 domain<br>Indicates that the Go/NoGo sensor has detected a low voltage on the V11 domain in FPM. This applies<br>to only that part of the domain which supplies the 2nd PLL. Writing 1 to the field clears it, and other reset<br>sources have no effect.<br>0b - No event has occurred<br>1b - NoGo event has occurred|
|26<br>GNG25OSC2F|GO/NoGo detect flag on 2nd PLL part of V25 domain<br>Indicates that the Go/NoGo sensor has detected a low voltage on the V25 domain in FPM. This applies<br>to only that part of the domain which supplies the 2nd PLL. Writing 1 to the field clears it, and other reset<br>sources have no effect.<br>0b - No event has occurred<br>1b - NoGo event has occurred|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1430 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K358) 

#### Table continued from the previous page... 

|Field<br>25<br>GNG11OSCF|Function<br>Go/NoGo detect flag on Osc part of V11 domain<br>Indicates that the Go/NoGo sensor has detected a low voltage on the V11 domain in FPM. This applies<br>to only that part of the domain which supplies the 1.1V clocking modules (e.g. PLL, IRC). Writing 1 to the<br>field clears it, and other reset sources have no effect.<br>0b - No event has occurred<br>1b - NoGo event has occurred|
|---|---|
|24<br>GNG25OSCF|GO/NoGo detect flag on Osc part of V25 domain<br>Indicates that the Go/NoGo sensor has detected a low voltage on the V25 domain in FPM. This applies<br>to only that part of the domain which supplies the 2.5V clocking modules (e.g. PLL,XOSCandIRC).<br>Writing 1 to the field clears it, and other reset sources have no effect.<br>0b - No event has occurred<br>1b - NoGo event has occurred|
|23<br>LVR11LPF|LVR11LP flag on V11 domain<br>Indicates that a low-voltage reset event has occurred on the 1.1V V11 power domain (FPM or LPM).<br>Writing 1 to the field clears it, and other reset sources have no effect.<br>0b - No low-voltage reset event has occurred<br>1b - Low-voltage reset event has occurred|
|22<br>LVR11F|LVR11 flag on V11 domain in FPM<br>Indicates that a low-voltage reset event has occurred on the 1.1V V11 power domain in the FPM. Writing<br>1 to this field clears it, and other reset sources have no effect.<br>0b - No low-voltage reset event has occurred<br>1b - Low-voltage reset event has occurred|
|21<br>LVR25LPF|LVR25LP flag on V25 domain<br>Indicates that a low-voltage reset event has occurred on the V25 power domain (FPM or LPM). Writing 1<br>to this field clears it, and other reset sources have no effect.<br>0b - No low-voltage reset event has occurred<br>1b - Low-voltage reset event has occurred|
|20<br>LVR25F|LVR25 flag on V25 domain in FPM<br>Indicates that a low-voltage reset event has occurred on the V25 power domain in FPM. Writing 1 to this<br>field clears it, and other reset sources have no effect.<br>0b - No low-voltage reset event has occurred<br>1b - Low-voltage reset event has occurred|
|19<br>LVRBLPF|LVRBLP flag on VDD_HV_B domain|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1431 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K358) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||Indicates that a low-voltage reset event has occurred on the VDD_HV_B power domain (FPM or LPM).<br>Writing 1 to this field clears it, and other reset sources have no effect.<br>0b - No low-voltage reset event has occurred<br>1b - Low-voltage reset event has occurred|
|18<br>LVRBF|LVRB flag on VDD_HV_B domain in FPM<br>Indicates that a low-voltage reset event has occurred on the VDD_HV_B power domain in FPM. Writing 1<br>to this field clears it, and other reset sources have no effect.<br>0b - No low-voltage reset event has occurred<br>1b - Low-voltage reset event has occurred|
|17<br>LVRALPF|LVRALP flag on VDD_HV_A domain<br>Indicates that a low-voltage reset event has occurred on the VDD_HV_A power domain (FPM or LPM).<br>Writing 1 to this field clears it, and other reset sources have no effect.<br>0b - No low-voltage reset event has occurred<br>1b - Low-voltage reset event has occurred|
|16<br>LVRAF|LVRA flag on VDD_HV_A domain in FPM<br>Indicates that a low-voltage reset event has occurred on the VDD_HV_A power domain in FPM. Writing 1<br>to this field clears it, and other reset sources have no effect.<br>0b - No low-voltage reset event has occurred<br>1b - Low-voltage reset event has occurred|
|15<br>|Reserved|
|—<br>14<br>HVD15S|HVD15 status on V15 domain in FPM<br>Shows the status of the high-voltage detect, HVD15, on the V15 power domain. This feature is only<br>available in FPM and disabled in LPM.<br>0b - Voltage on V15 is below high-voltage detect threshold or LPM.<br>1b - Voltage on V15 is above high-voltage detect threshold and FPM.|
|13<br>—|Reserved, ignore value<br>Reserved, ignore value|
|12|LVD5A status on VDD_HV_A domain in FPM|
|LVD5AS|Shows the status of the 5V low-voltage detect, LVD5A, on the VDD_HV_A power domain. This monitor<br>indicates if the voltage is below a certain threshold, which is set slightly below 4.5V (see Datasheet for<br>exact value). The feature is only available in FPM and disabled in LPM. After a reset or wakeup from<br>LPM, the software should clear the LVD5AF flag and check the status bit LVD5AS to determine voltage<br>level on VDD_HV_A supply.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1432 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K358) 

Table continued from the previous page... 

|Field|Function<br>0b - Voltage on VDD_HV_A is above low-voltage detect threshold<br>1b - Voltage on VDD_HV_A is below low-voltage detect threshold|
|---|---|
|11<br>HVD11S|HVD11 status on V11 domain in FPM<br>Shows the status of the high-voltage detect, HVD11, on the V11 power domain. This feature is only<br>available in FPM and disabled in LPM.<br>0b - Voltage on V11 is below high-voltage detect threshold or LPM.<br>1b - Voltage on V11 is above high-voltage detect threshold and FPM.|
|10<br>HVD25S|HVD25 status on V25 domain in FPM<br>Shows the status of the high-voltage detect, HVD25, on the V25 power domain. The feature is only<br>available in FPM and disabled in LPM.<br>0b - Voltage on V25 is below high-voltage detect threshold or LPM.<br>1b - Voltage on V25 is above high-voltage detect threshold and FPM.|
|9<br>HVDBS|HVDB status on VDD_HV_B domain in FPM<br>Shows the status of the high-voltage detect, HVDB, on the VDD_HV_B power domain. The feature is<br>only available in FPM and disabled in LPM.<br>0b - Voltage on VDD_HV_B is below high-voltage detect threshold or LPM.<br>1b - Voltage on VDD_HV_B is above high-voltage detect threshold and FPM.|
|8<br>HVDAS|HVDA status on VDD_HV_A domain in FPM<br>Shows the status of the high-voltage detect HVDA on the VDD_HV_A power domain. The feature is only<br>available in FPM and disabled in LPM.<br>0b - Voltage on VDD_HV_A is below high-voltage detect threshold or LPM.<br>1b - Voltage on VDD_HV_A is above high-voltage detect threshold and FPM.|
|7<br>—|Reserved|
|6<br>HVD15F|HVD15 flag on V15 domain in FPM<br>PMC writes 1 to this field when the HVD15S status field changes. To clear HVD15F, write 1 to it. If<br>enabled, HVD15F causes an interrupt request.<br>0b - HVD15S has not changed.<br>1b - HVD15S has changed.|
|5<br>—|Reserved|
|4|LVD5A flag on VDD_HV_A domain in FPM|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1433 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K358) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|LVD5AF|PMC writes 1 to this field when LVD5AS status field changes. To clear LVD5AF, write 1 to it. If enabled,<br>LVD5AF causes an interrupt request.<br>0b - LVD5AS has not changed.<br>1b - LVD5AS has changed.|
|3<br>HVD11F|HVD11 flag on V11 domain in FPM<br>PMC writes 1 to this field when the HVD11S status field changes. To clear HVD11F, write 1 to it. If<br>enabled, HVD11F causes an interrupt request.<br>0b - HVD11S has not changed.<br>1b - HVD11S has changed.|
|2<br>HVD25F|HVD25 flag on V25 domain in FPM<br>PMC writes 1 to the HVD25F field when HVD25S status field changes. To clear HVD25F, write 1 to it. If<br>enabled, HVD25F causes an interrupt request.<br>0b - HVD25S has not changed.<br>1b - HVD25S has changed.|
|1<br>HVDBF|HVDB flag on VDD_HV_B domain in FPM<br>PMC writes 1 to the HVDBF field when HVDBS status field changes. To clear HVDBF, write 1 to it. If<br>enabled, HVDBF causes an interrupt request.<br>0b - HVDBS has not changed.<br>1b - HVDBS has changed.|
|0<br>HVDAF|HVDA flag on VDD_HV_A domain in FPM<br>PMC writes 1 to the HVDAF field when HVDAS status field changes. To clear HVDAF, write 1 to it. If<br>enabled, HVDAF causes an interrupt request.<br>0b - HVDAS has not changed.<br>1b - HVDAS has changed.|



### 43.7.3 PMC Configuration Register (CONFIG) 

#### Offset 

|Register|Offset|
|---|---|
|CONFIG|4h|



#### Function 

This register configures the various PMC options. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1434 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K358) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||||0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||0||||LVDIE|HVDIE|LMSM<br>PSEN|0||LVRBL<br>|LPM25<br>|FAST<br>|LMBC<br>TLEN|LMEN|
|W|||||||||0|||PEN|EN|REC|0||
|Reset|0|0|0|0|0|0|0|0|1|0|0|0|0|0|1|1|



#### Fields 

|Field|Function|
|---|---|
|31-10<br>—|Reserved|
|9<br>LVDIE|Low voltage detect interrupt enable<br>Enables hardware interrupt requests if any of the following flags is set: LVD5AF, LVD15F. LVD interrupt<br>must be disabled before going into LPM.<br>0b - LVD hardware interrupt is disabled (use polling).<br>1b - Request an LVD hardware interrupt when LVDA5F=1 or LVD15F=1.|
|8<br>HVDIE|High voltage detect interrupt enable<br>Enables hardware interrupt requests if any of the following flags is set: HVDAF, HVDBF, HVD25F,<br>HVD11F.<br>0b - HVD hardware interrupt is disabled (use polling).<br>1b - Request an HVD hardware interrupt when HVDAF=1, HVDBF=1, HVD25F=1, or HVD11F=1.|
|7|V15 Switched-mode power supply enable bit|
|LMSMPSEN|Enables the SMPS regulator (Switched-mode power supply), which regulates from VDD_DCDC down<br>to 1.5V on V15 pin to supply the Last Mile regulator. As LMSMPSEN=1 after startup or reset, in case<br>SMPS is not used, software must write LMBSMPSEN=0 after each reset to turn the feature off. Once<br>LMSMPSEN=0 it can no longer be written 1 until next reset.<br>0b - Switched-mode power supply (SMPS) for V15 disabled<br>1b - Switched-mode power supply (SMPS) for V15 enabled|
|6-5<br>—|Reserved|
|4<br>LVRBLPEN|LVRBLP enable bit during LPM|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1435 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K358) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||Controls whether the low-voltage reset detection (LVRBLP) on the VDD_HV_B power domain is active or<br>inactive in LPM<br>0b - Low-voltage reset detection is disabled in LPM.<br>1b - Low-voltage reset detection is enabled in LPM.|
|3<br>LPM25EN|V25 domain enable bit during LPM<br>Enables a low power V25 regulator and the low-voltage reset detection (LVR25LP) in LPM. In FPM this<br>low power regulator is always off.<br>0b - V25 regulator and LVR25LP are disabled in LPM.<br>1b - V25 regulator and LVR25LP are enabled in LPM.|
|2<br>FASTREC|Fast recovery from LPM enable bit<br>Controls the recovery time from LPM to FPM. This causes a higher current demand on V15, and this<br>translates to a higher current demand on the primary side of the V15 supply.<br>0b - Normal recovery time from LPM<br>1b - Fast recovery time from LPM|
|1<br>LMBCTLEN|V15 external BJT enable bit<br>This field must be set to 1 if external BJT between VDD_HV_A and V15 is used on the PCB. The<br>base of this BJT must be connected to the VRC_CTRL pin and is controlled by the PMC to regulate a<br>voltage of 1.5V on V15 pin to supply the Last Mile Regulator. As LMBCTLEN=1 after startup or reset, in<br>case BJT is not used, software must write LMBCTLEN=0 after each reset to turn the feature off. Once<br>LMBCTLEN=0 it can no longer be written 1 until next reset.<br>0b - External BCTL regulator for V15 disabled<br>1b - External BCTL regulator for V15 enabled|
|0<br>LMEN|Last Mile regulator enable bit<br>Enables the Last Mile regulator, which regulates an external 1.5V voltage on V15 down to the core and<br>logic supply (V11 power domain), which is typically 1.1V. As the Last Mile regulator is always enabled on<br>this device, LMEN bit is read-only and always reads 1.|



### 43.7.4 SMPS Configuration Register (SMPSCONFIG) 

#### Offset 

|Register|Offset|
|---|---|
|SMPSCONFIG|8h|



#### Function 

This register configures the various options of the Switched-mode power supply (SMPS) generating the V15 (1.5V input supply to the last mile regulator). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1436 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K358) 

Table 223. SMPS configurations for driving PMOS_CTRL pin 

|CFG[3:0] bits|PMOS_CTRL Frequency|PMOS_CTRL Duty cycle 3V|PMOS_CTRL Duty cycle 5V|
|---|---|---|---|
|0000|470 kHz|58.8%|47.1%|
|0001|470 kHz|64.7%|52.9%|
|0010|470 kHz|52.9%|41.2%|
|0011|533 kHz|60%|46.7%|
|0100|533 kHz|66.7%|53.3%|
|0101|533 kHz|53.3%|40%|
|0110|421 kHz|57.9%|47.4%|
|0111|421 kHz|63.2%|52.6%|
|1000|421 kHz|52.6%|42.1%|
|1001 to 1110|Reserved|Reserved|Reserved|
|1111|8 MHz / (PERIOD[4:0]+1)|ONTIME3V[4:0] /<br>(PERIOD[4:0]+1)|ONTIME5V[4:0] /<br>(PERIOD[4:0]+1)|



Table 224. 8 MHz IRC Dither configurations 

|DITHERCFG[1:0] bits|Dither Amplitude|Dither Frequency|
|---|---|---|
|00|+/- 0.4 MHz|400 kHz|
|01|+/- 0.6 MHz|286 kHz|
|10|+/- 0.8 MHz|222 kHz|
|11|+/- 1 MHz|182 kHz|



Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/043_Power_Management_Controller_-PMC_for_S32K358-/S32K3XXRM_数据表.pdf-1437-07.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>PGAT<br>R 0 0<br>ES<br>ONTIME5V  ONTIME3V<br>W<br>Reset 0 0 0 0 1 0 0 0 u 0 0 0 1 0 1 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 DITHE LPM15<br>PERIOD  DITHERCFG  CFG<br>REN  EN<br>W<br>Reset 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field<br>Function|
|---|
|31-29<br>Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1437 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K358) 

Table continued from the previous page... 

|Field<br>|Function|
|---|---|
|—<br>28-24<br>ONTIME5V|SMPS Duty cycle for 5V range<br>These bits determine the duty cycle of the output signal at PMOS_CTRL pin. This duty cycle is applied<br>while VDD_DCDC is greater or equal than 4V.<br>It calculates as follows: Duty_pmos_ctrl = ONTIME3V[4:0] / (PERIOD[4:0] + 1)|
|23<br>PGATES|PMOS_CTRL Status Bit<br>This read-only bit reflects the status of the PMOS_CTRL pin.<br>0b - PMOS_CTRL pin driven to VSS_DCDC (which is connect to GND)<br>1b - PMOS_CTRL pin driven to VDD_DCDC voltage|
|22-21<br>—|Reserved|
|20-16<br>ONTIME3V|SMPS Duty cycle for 3V range<br>These bits determine the duty cycle of the output signal at PMOS_CTRL pin. This duty cycle is applied<br>while VDD_DCDC is smaller than 4V.<br>It calculates as follows: Duty_pmos_ctrl = ONTIME3V[4:0] / (PERIOD[4:0] + 1)|
|15-13<br>—<br>12-8<br>PERIOD|Reserved<br>SMPS Period<br>These bits determine the period and frequency of the output signal at PMOS_CTRL pin.<br>It calculates as follows: Freq_pmos_ctrl = 8 MHz / (PERIOD[4:0] + 1)|
|7<br>DITHEREN|IRC Dither Enable<br>This bit enables dithering of the 8MHz IRC. The amplitude and period of the frequency modulation is<br>determined by the DITHERCFG[1:0] bits.<br>0b - 8MHz IRC dithering disabled<br>1b - 8MHz IRC dithering enabled|
|6-5<br>DITHERCFG|IRC Dither Configuration<br>Configuration bits to select IRC dithering amplitude and frequency.<br>This feature is to spread the spectrum of driving PMOS_CTRL pin to reduce radiated emission. To<br>change the value: Write DITHEN=0, then write desired dither configuration (DITHERCFG[1:0]), finally write<br>DITHEN=1 again. SeeTable 224for configuration options.|
|4<br>LPM15EN|V15 domain enable bit during LPM|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1438 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K358) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||Enables the V15 in LPM. This is useful for fast recovery to FPM when using the SMPS mode to generate<br>the V15. This feature is only active in LPM, in FPM it is turned off. For this purpose there is a small LDO<br>inside the PMC that regulates the V15 to target value during LPM.<br>LPM15EN bit is only allowed to use, when using the SMPS to generate the V15. For other<br>options to generate the V15 it is forbidden and software should always write 0 to LPM15EN.<br>~~NOTE~~<br>0b - V15 not kept on target in LPM<br>1b - V15 kept on target in LPM|
|3-0|SMPS configuration select|
|CFG|These bits select a configuration for period and duty cycle (ontime) of the Switched-mode power supply<br>driving via PMOS_CTRL the external power FET according toTable 223.<br>As seen in the table CFG[3:0] = 1111 allows for free customization of the PERIOD[4:0],<br>ONTIME5V[4:0] and ONTIME3V[3:0] bits. If choosing this option consider carefully the<br>value of these bits. To ensure the proper function of the SMPS, and to keep the<br>EMI in check, the switching frequency and duty cycle must be programmed within a<br>reasonable range.<br>~~NOTE~~|



### 43.7.5 Version ID register (VERID) 

#### Offset 

|Register|Offset|
|---|---|
|VERID|Ch|



#### Function 

This register returns the major and minor version numbers of hardware implementation. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||MAJ|OR|||||||MIN|OR||||
|W|||||||||||||||||
|Reset<br>Bits|0<br>15|0<br>14|0<br>13|0<br>12|0<br>11|1<br>10|0<br>9|0<br>8|0<br>7|0<br>6|0<br>5|0<br>4|0<br>3|0<br>2|0<br>1|0<br>0|
|R||||||||0||||||||LMFE<br>AT|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1439 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K358) 

#### Fields 

|Field|Function|
|---|---|
|31-24|Major version number|
|MAJOR|Returns the version number for the specification|
|23-16|Minor version number|
|MINOR|Returns the version number for the hardware implementation|
|15-1<br>—<br>0|Reserved<br>Last Mile Regulator Feature|
|LMFEAT|This read-only field shows if the Last Mile regulator feature is available.<br>0b - No Last Mile regulator|
||1b - Last Mile regulator (1.5V to 1.1V) is available|



|43.8 Glossary||
|---|---|
|FPM|Full Performance mode|
|HVD|High voltage detect|
|IRC|Internal RC oscillator|
|LM|Last mile regulator|
|LPM|Low Performance mode|
|LVD|Low voltage detect|
|LVR|Low voltage reset|
|NVM|Nonvolatile memory|
|POR|Power on reset|
|XOSC|External crystal oscillator|
|SMPS|Switched-mode power supply|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1440 / 4640 

