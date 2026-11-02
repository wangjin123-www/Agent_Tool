NXP Semiconductors 

# Chapter 41 Power Management Controller (PMC for S32K34x, S32K32x and S32K314) 

## 41.1 Introduction 

PMC is the power management controller for the S32K3 family of microcontrollers. It provides multiple power options to allow you to optimize power consumption for the level of functionality needed. It includes internal voltage regulators, POR, and the integrated low/high voltage detect system with reset (brown-out) capability. The voltage regulator requires a 3.3 V or 5 V input to generate all the required secondary supplies. 

## 41.2 Features 

PMC includes the following features: 

- Combination of internal and external voltage regulator options, offering RUN and Standby modes 

- Active POR providing brown-out detect 

- LVR for all system-relevant power domains 

- LVD and HVD as indication for software 

## 41.3 Modes of operation 

PMC provides two basic modes of operation for the voltage regualtors and monitors: 

- FPM, which is used on chip-level in RUN modes: For high-current consumption 

- LPM, which is used on chip-level for Standby modes: For low-current consumption 

## 41.4 Block diagram 

The following figure shows the block diagram for this module. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1401 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K34x, S32K32x and S32K314) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/041_Power_Management_Controller_-PMC_for_S32K34x,_S32K32x_and_S32K314-/S32K3XXRM_数据表.pdf-1402-02.png)


<!-- Start of picture text -->
VC_BJT<br>optional<br>Last Mile<br>distributed CMP ADC<br>regulator<br>LPM Boot FPM<br>PMC VDD_HV_A<br>V11  VSS VSS<br>[V11 (STANDBY)] (STANDBY)<br>Pads<br>V25 sw<br>GPIO<br>SOG (STANDBY)<br>SIRC, FIRC,<br>SXOSC<br>V11 (RUN) VSS<br>VDD_HV_B<br>FXOSC<br>V11  SOG (RUN)<br>(STANDBY)<br>Pads<br>Flash<br>PLL GPIO<br>& CTS<br>VSS VSS<br>VSS<br>(double bond)<br>(double bond)<br>Figure 162. PMC block diagram<br>41.5 Signals<br>This table describes the PMC module signals.<br>Table 220. Signal Description<br>Signal I/O Description<br>VDD_HV_A Supply input This is the primary high-voltage supply input to PMC. VDD_HV_A is<br>used for the PMC internal precision references. After the VDD_HV_A<br>domain is powered up, it must be kept powered at all times of<br>operation (FPM and LPM).<br>VDD_HV_B 1 Supply input This is the secondary high-voltage supply input supervised by the<br>PMC. After the VDD_HV_B domain is powered up, it must be kept<br>powered at all times of operation (FPM and LPM).<br>VREFH VREFL<br>VDD_HV_B VDD_HV_A VRC_CTRL V15<br>VSS V25 V11<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1402 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K34x, S32K32x and S32K314) 

Table 220. Signal Description (continued) 

|Signal|I/O|Description|
|---|---|---|
|V25|Supply output|V25 power supply domain is driven by a fully integrated low-dropout<br>linear voltage regulator. It supplies the Flash memory and (via a<br>double bond) the clock modules.|
|V15<sup>1</sup>|Supply input|This is the high-current input for core/logic supply that can be fed by<br>an external BJT or another source.|
|VRC_CTRL|Output|VRC_CTRL connects to the base of external BJT, if this option is used<br>to generate V15.|
|V11|Supply output|V11 is the core/logic supply. It is driven by a fully integrated low-<br>dropout linear voltage regulator.|
|VSS|Ground|VSS must be grounded. All VSS Pins need to be externally connected<br>to the same ground node.|



1. VDD_HV_B and V15 not present in S32K312 and S32K311. 

## 41.6 Functional description 

The following sections describe functional details of the PMC. 

### 41.6.1 Reset 

The POR and all LVRs are combined into one single MCU POR. 

After an MCU POR event, it can be determined which power domain caused it, by reading in the PMC_LVSC register, the POR flag, and LVR flags. 

After an initial power ramp up of the MCU in the PMC_LVSC register, the POR flag and the LVR flags are all set to 1. The Go/Nogo flags have an arbitrary value. 

~~<mark>NOTE</mark>~~ After an initial power ramp up, all flags in the LVSC register must be cleared (by writing 0xFFFFFFFF to the LVSC register). 

Because the flags are sticky bits, it is required to clear them before usage. So, in case of an unxepected MCU POR, the source of the problem can be tracked and debugged by reading the flags in the LVSC register. 

### 41.6.2 Interrupts 

PMC includes two interrupt sources: 

- HVD interrupt: It combines all HVD monitors into one interrupt source. Interrupt enable is the HVDIE field in the CONFIG register. See the PMC Configuration Register (CONFIG) and Low Voltage Status and Control Register (LVSC) registers for details. 

- LVD interrupt: It combines the LVD15 and LVD5A monitors into one interrupt source. Interrupt enable is the LVDIE field in the CONFIG register. See the CONFIG and LVSC registers for details. 

## 41.7 PMC register descriptions 

### 41.7.1 PMC memory map 

This section includes the PMC module memory map and detailed descriptions for all the registers. 

PMC base address: 402E_8000h 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1403 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K34x, S32K32x and S32K314) 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|Low Voltage Status and Control Register (LVSC)|32|W1C|See<br>description|
|4h|PMC Configuration Register (CONFIG)|32|RW|See<br>description|
|Ch|Version ID register (VERID)|32|RO|0200_0001h|



### 41.7.2 Low Voltage Status and Control Register (LVSC) 

#### Offset 

|Register|Offset|
|---|---|
|LVSC|0h|



#### Function 

This register contains status and control bits to support the low-voltage reset and low- or high-voltage detect function. When the PMC is in LPM, the low- or high-voltage detect systems are disabled. 

~~<mark>NOTE</mark>~~ 

For all flags that are not affected by reset (POR flag, all LVR flags, all GNG flags), in case a reset occurs at the same time while trying to clear the flags (by writing 1), the flag value is not defined appropriately. In this case, you need to clear the flag again after exit from reset. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/041_Power_Management_Controller_-PMC_for_S32K34x,_S32K32x_and_S32K314-/S32K3XXRM_数据表.pdf-1404-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>GNG1 GNG2 LVR11 LVR11 LVR25 LVR25 LVRBL LVRAL<br>R PORF  0 LVRBF  LVRAF<br>1OS... 5OS... LPF  F  LPF  F  PF  PF<br>W W1C W1C W1C W1C W1C W1C W1C W1C W1C W1C W1C<br>Reset u 0 0 0 0 0 u u u u u u u u u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>LVD15 LVD5A HVD1 HVD2 HVDB HVDA LVD15 LVD5A HVD1 HVD2 HVDB HVDA<br>R 0 0<br>S  S  1S  5S  S  S  F  F  1F  5F  F  F<br>W W1C W1C W1C W1C W1C W1C<br>Reset 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field<br>Function|
|---|
|31<br>POR flag|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1404 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K34x, S32K32x and S32K314) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|PORF|Indicates that a power-on reset event has occurred. Writing 1 to this field clears it, and other reset<br>sources have no effect.<br>0b - No power-on reset event has occurred<br>1b - Power-on reset event has occurred|
|30-26<br>—|Reserved|
|25<br>GNG11OSCF|Go/NoGo detect flag on Osc part of V11 domain<br>Indicates that the Go/NoGo sensor has detected a low voltage on the V11 domain in FPM. This applies<br>to only that part of the domain which supplies the 1.1V clocking modules (for example, PLL). Writing 1 to<br>the field clears it, and other reset sources have no effect.<br>0b - No event has occurred<br>1b - NoGo event has occurred|
|24<br>GNG25OSCF|GO/NoGo detect flag on Osc part of V25 domain<br>Indicates that the Go/NoGo sensor has detected a low voltage on the V25 domain in FPM. This applies<br>to only that part of the domain which supplies the 2.5V clocking modules (for example,XOSCandIRC).<br>Writing 1 to the field clears it, and other reset sources have no effect.<br>0b - No event has occurred<br>1b - NoGo event has occurred|
|23<br>LVR11LPF|LVR11LP flag on V11 domain<br>Indicates that a low-voltage reset event has occurred on the 1.1V V11 power domain (FPM or LPM).<br>Writing 1 to the field clears it, and other reset sources have no effect.<br>0b - No low-voltage reset event has occurred<br>1b - Low-voltage reset event has occurred|
|22<br>LVR11F|LVR11 flag on V11 domain in FPM<br>Indicates that a low-voltage reset event has occurred on the 1.1V V11 power domain in the FPM. Writing<br>1 to this field clears it, and other reset sources have no effect.<br>0b - No low-voltage reset event has occurred<br>1b - Low-voltage reset event has occurred|
|21<br>LVR25LPF|LVR25LP flag on V25 domain<br>Indicates that a low-voltage reset event has occurred on the V25 power domain (FPM or LPM). Writing 1<br>to this field clears it, and other reset sources have no effect.<br>0b - No low-voltage reset event has occurred<br>1b - Low-voltage reset event has occurred|
|20|LVR25 flag on V25 domain in FPM|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1405 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K34x, S32K32x and S32K314) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|LVR25F|Indicates that a low-voltage reset event has occurred on the V25 power domain in FPM. Writing 1 to this<br>field clears it, and other reset sources have no effect.<br>0b - No low-voltage reset event has occurred<br>1b - Low-voltage reset event has occurred|
|19<br>LVRBLPF|LVRBLP flag on VDD_HV_B domain<br>Indicates that a low-voltage reset event has occurred on the VDD_HV_B power domain (FPM or LPM).<br>Writing 1 to this field clears it, and other reset sources have no effect.<br>0b - No low-voltage reset event has occurred<br>1b - Low-voltage reset event has occurred|
|18<br>LVRBF|LVRB flag on VDD_HV_B domain in FPM<br>Indicates that a low-voltage reset event has occurred on the VDD_HV_B power domain in FPM. Writing 1<br>to this field clears it, and other reset sources have no effect.<br>0b - No low-voltage reset event has occurred<br>1b - Low-voltage reset event has occurred|
|17<br>LVRALPF|LVRALP flag on VDD_HV_A domain<br>Indicates that a low-voltage reset event has occurred on the VDD_HV_A power domain (FPM or LPM).<br>Writing 1 to this field clears it, and other reset sources have no effect.<br>0b - No low-voltage reset event has occurred<br>1b - Low-voltage reset event has occurred|
|16<br>LVRAF|LVRA flag on VDD_HV_A domain in FPM<br>Indicates that a low-voltage reset event has occurred on the VDD_HV_A power domain in FPM. Writing 1<br>to this field clears it, and other reset sources have no effect.<br>0b - No low-voltage reset event has occurred<br>1b - Low-voltage reset event has occurred|
|15-14<br>—|Reserved|
|13<br>LVD15S|LVD15 status on V15 domain in FPM<br>Shows the status of the 1.5V low-voltage detect, LVD15, on the V15 power domain. This monitor<br>indicates when the V15 voltage level generated from external is on target. This feature is available only<br>in FPM and disabled in LPM. After a reset or wakeup from LPM, the software should clear the LVD15F<br>flag and check the status bit LVD15S to determine voltage level on V15 supply.<br>0b - Voltage on V15 is above low-voltage detect threshold or LPM.<br>1b - Voltage on V15 is below low-voltage detect threshold and FPM.|
|12|LVD5A status on VDD_HV_A domain in FPM|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1406 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K34x, S32K32x and S32K314) 

Table continued from the previous page... 

|Field<br>LVD5AS|Function<br>Shows the status of the 5V low-voltage detect, LVD5A, on the VDD_HV_A power domain. This monitor<br>indicates if the voltage is below a certain threshold, which is set slightly below 4.5V (see Datasheet for<br>exact value). The feature is only available in FPM and disabled in LPM. After a reset or wakeup from<br>LPM, the software should clear the LVD5AF flag and check the status bit LVD5AS to determine voltage<br>level on VDD_HV_A supply.<br>0b - Voltage on VDD_HV_A is above low-voltage detect threshold<br>1b - Voltage on VDD_HV_A is below low-voltage detect threshold|
|---|---|
|11<br>HVD11S|HVD11 status on V11 domain in FPM<br>Shows the status of the high-voltage detect, HVD11, on the V11 power domain. This feature is only<br>available in FPM and disabled in LPM.<br>0b - Voltage on V11 is below high-voltage detect threshold or LPM.<br>1b - Voltage on V11 is above high-voltage detect threshold and FPM.|
|10<br>HVD25S|HVD25 status on V25 domain in FPM<br>Shows the status of the high-voltage detect, HVD25, on the V25 power domain. The feature is only<br>available in FPM and disabled in LPM.<br>0b - Voltage on V25 is below high-voltage detect threshold or LPM.<br>1b - Voltage on V25 is above high-voltage detect threshold and FPM.|
|9<br>HVDBS|HVDB status on VDD_HV_B domain in FPM<br>Shows the status of the high-voltage detect, HVDB, on the VDD_HV_B power domain. The feature is<br>only available in FPM and disabled in LPM.<br>0b - Voltage on VDD_HV_B is below high-voltage detect threshold or LPM.<br>1b - Voltage on VDD_HV_B is above high-voltage detect threshold and FPM.|
|8<br>HVDAS|HVDA status on VDD_HV_A domain in FPM<br>Shows the status of the high-voltage detect HVDA on the VDD_HV_A power domain. The feature is only<br>available in FPM and disabled in LPM.<br>0b - Voltage on VDD_HV_A is below high-voltage detect threshold or LPM.<br>1b - Voltage on VDD_HV_A is above high-voltage detect threshold and FPM.|
|7-6<br>—|Reserved|
|5<br>LVD15F|LVD15 flag on V15 domain in FPM<br>PMC writes 1 to the LVD15F field when the LVD15S status field changes. To clear LVD15F, write 1 to it.<br>If enabled, LVD15F causes an interrupt request.<br>0b - LVD15S has not changed.<br>1b - LVD15S has changed.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1407 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K34x, S32K32x and S32K314) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|4<br>LVD5AF|LVD5A flag on VDD_HV_A domain in FPM<br>PMC writes 1 to this field when LVD5AS status field changes. To clear LVD5AF, write 1 to it. If enabled,<br>LVD5AF causes an interrupt request.<br>0b - LVD5AS has not changed.<br>1b - LVD5AS has changed.|
|3<br>HVD11F|HVD11 flag on V11 domain in FPM<br>PMC writes 1 to this field when the HVD11S status field changes. To clear HVD11F, write 1 to it. If<br>enabled, HVD11F causes an interrupt request.<br>0b - HVD11S has not changed.<br>1b - HVD11S has changed.|
|2<br>HVD25F|HVD25 flag on V25 domain in FPM<br>PMC writes 1 to the HVD25F field when HVD25S status field changes. To clear HVD25F, write 1 to it. If<br>enabled, HVD25F causes an interrupt request.<br>0b - HVD25S has not changed.<br>1b - HVD25S has changed.|
|1<br>HVDBF|HVDB flag on VDD_HV_B domain in FPM<br>PMC writes 1 to the HVDBF field when HVDBS status field changes. To clear HVDBF, write 1 to it. If<br>enabled, HVDBF causes an interrupt request.<br>0b - HVDBS has not changed.<br>1b - HVDBS has changed.|
|0<br>HVDAF|HVDA flag on VDD_HV_A domain in FPM<br>PMC writes 1 to the HVDAF field when HVDAS status field changes. To clear HVDAF, write 1 to it. If<br>enabled, HVDAF causes an interrupt request.<br>0b - HVDAS has not changed.<br>1b - HVDAS has changed.|



### 41.7.3 PMC Configuration Register (CONFIG) 

#### Offset 

|Register|Offset|
|---|---|
|CONFIG|4h|



#### Function 

If the Last Mile Regulator option is not available on your device ( Version ID register (VERID) register: LMFEAT=0), then the bits LMEN, LMBCTLEN, LMAUTOEN and LMSTAT fields can not be written and read always 0. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1408 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K34x, S32K32x and S32K314) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/041_Power_Management_Controller_-PMC_for_S32K34x,_S32K32x_and_S32K314-/S32K3XXRM_数据表.pdf-1409-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>LMST<br>R 0<br>AT  LMAU<br>TOEN<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 u 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 LVRBL LPM25 FAST LMBC<br>LVDIE  HVDIE  LMEN<br>W PEN  EN  REC  TLEN<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-18<br>—|Reserved|
|17<br>LMSTAT|Last Mile regulator status bit<br>This bits reflects the current status of the Last Mile regulator. This information is required as when auto<br>turn over feature is enabled (LMAUTOEN=1) the PMC will switch automatically between Boot regulator<br>and Last Mile regulator debending on the V15 status (LVD15S).<br>0b - Last Mile Regulator is off<br>1b - Last Mile Regulator is on|
|16<br>LMAUTOEN|Last Mile regulator auto turn over bit<br>Enables to turn over automatically from Boot Regulator Mode to Last Mile regulator mode and vice versa<br>depending on the V15 voltage status (LVD15S). As long as LMEN=0 software must make sure that the<br>system clock is on FIRC clock or slower. To use higher clock speed software must set LMEN=1.<br>0b - Auto turnover disabled<br>1b - Auto turnover enabled|
|15-10<br>—<br>9<br>LVDIE|Reserved<br>Low voltage detect interrupt enable<br>Enables hardware interrupt requests if any of the following flags is set: LVD5AF, LVD15F. LVD interrupt<br>must be disabled before going into LPM.<br>0b - LVD hardware interrupt is disabled (use polling).<br>1b - Request an LVD hardware interrupt when LVDA5F=1 or LVD15F=1.|
|8<br>HVDIE|High voltage detect interrupt enable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1409 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K34x, S32K32x and S32K314) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||Enables hardware interrupt requests if any of the following flags is set: HVDAF, HVDBF, HVD25F,<br>HVD11F.<br>0b - HVD hardware interrupt is disabled (use polling).<br>1b - Request an HVD hardware interrupt when HVDAF=1, HVDBF=1, HVD25F=1, or HVD11F=1.|
|7-5<br>—|Reserved|
|4<br>LVRBLPEN|LVRBLP enable bit during LPM<br>Controls whether the low-voltage reset detection (LVRBLP) on the VDD_HV_B power domain is active or<br>inactive in LPM<br>0b - Low-voltage reset detection is disabled in LPM.<br>1b - Low-voltage reset detection is enabled in LPM.|
|3<br>LPM25EN|V25 domain enable bit during LPM<br>Controls whether the V25 regulator and low-voltage reset detection (LVR25LP) are active or inactive in<br>LPM<br>0b - V25 regulator and LVR25LP are disabled in LPM.<br>1b - V25 regulator and LVR25LP are enabled in LPM.|
|2<br>FASTREC|Fast recovery from LPM enable bit<br>Controls the recovery time from LPM to FPM. At recovery from LPM, all the tank capacitors from the<br>secondary supplies have to be recharged. This causes a high-current demand, which might not be<br>met by the supply driving the VDD_HV_A primary domain. When selecting the fast recovery time, the<br>current for recharging is approximately three times higher than that for FASTREC=0. The application<br>must determine from the drive capability of the external VDD_HV_A regulator, the size of tank caps on<br>the secondary supply pins and the selected recovery time if this is sufficient to start up from LPM in time.<br>0b - Normal recovery time from LPM<br>1b - Fast recovery time from LPM|
|1<br>LMBCTLEN|Last Mile regulator base control enable bit<br>This field must be set to 1 if external BJT between VDD_HV_A and V15 is used on the PCB. The<br>base of this BJT must be connected to the VRC_CTRL pin and is controlled by the PMC to regulate a<br>voltage of 1.5V on V15 pin. After setting LMBCTLEN=1 the software has to wait for 15us (FASTREC=1)<br>respectively 50us (FASTREC=0) before polling LVD15S=0 and then setting LMEN=1. This respects the<br>softstart time of the V15 regulator. If LMAUTOEN=1 then LMBCTLEN can be left enabled when going<br>into LPM, the hardware will turn the regulator off and back on automatically after recovery from LPM.<br>0b - External BCTL regulator for V15 disabled<br>1b - External BCTL regulator for V15 enabled|
|0<br>LMEN|Last Mile regulator enable bit|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1410 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K34x, S32K32x and S32K314) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||Enables the Last Mile regulator, which regulates an external 1.5V voltage on V15 down to the core and<br>logic supply (V11 power domain), which is typically 1.1V. Setting LMEN=1 hands over the V11 voltage<br>generation from the Boot regulator to the Last Mile regulator. The software must ensure that before<br>enabling the Last Mile regulator, the voltage on V15 is sufficiently high as indicated by the LVD15S<br>status field (LVD15S=0). To use external BJT between VDD_HV_A and V15, the LMBCTLEN field must<br>be set before the LMEN field, and the software must wait until 1.5V is up (LVD15S=0). If LMAUTOEN=0<br>then to disable the Last Mile regulator, LMEN and LMBCTLEN must be cleared simultaneously (single<br>register write). The software must disable (LMEN=0) the Last Mile regulator before going into LPM. After<br>setting LMEN=1, software must wait a minimum time of 1.5us before changing clock rate.<br>0b - Last Mile regulator is disabled.|
||1b - Last Mile regulator is enabled.|



### 41.7.4 Version ID register (VERID) 

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
|Reset|0|0|0|0|0|0|1|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0||||||||LMFE<br>AT|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|



Fields 

|Field|Function|
|---|---|
|31-24|Major version number|
|MAJOR|Returns the version number for the specification|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1411 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K34x, S32K32x and S32K314) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|23-16|Minor version number|
|MINOR|Returns the version number for the hardware implementation|
|15-1|Reserved|
|—<br>0|Last Mile Regulator Feature|
|LMFEAT|This read-only field shows if the Last Mile regulator feature is available.|
||0b - No Last Mile regulator|
||1b - Last Mile regulator (1.5V to 1.1V) is available|



|41.8 Glossary||
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



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1412 / 4640 

