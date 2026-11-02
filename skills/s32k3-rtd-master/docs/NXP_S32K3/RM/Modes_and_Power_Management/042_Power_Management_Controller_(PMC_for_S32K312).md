NXP Semiconductors 

# Chapter 42 Power Management Controller (PMC for S32K312) 

## 42.1 Introduction 

PMC provides multiple power options to allow you to optimize power consumption for the appropriate level of functionality. It includes: 

- Internal voltage regulators 

- POR 

- Integrated low and high voltage detection system with reset (brownout) capability 

The voltage regulator requires a 3.3 V or 5 V input to generate all the required secondary supplies. 

## 42.2 Features 

- A combination of internal and external voltage regulator options, offering Run and Standby modes 

- Active POR, providing brownout detect 

- LVR for all system-relevant power domains 

- Software-readable Low Voltage Status and Control register that contains flags that indicate low- or high-voltage conditions 

## 42.3 Modes of operation 

PMC provides two basic modes of operation for voltage regulators and monitors: 

- FPM supports chip run modes that have high current consumption. 

- LPM supports chip standby modes that have low current consumption. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1413 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K312) 

## 42.4 Block diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/042_Power_Management_Controller_-PMC_for_S32K312-/S32K3XXRM_数据表.pdf-1414-03.png)


<!-- Start of picture text -->
CMP ADC<br>FPM LPM<br>PMC<br>VDD_HV_A<br>V11  VSS VSS<br>(Standby)<br>Pins<br>SW<br>V25<br>GPIO<br>SOG (Standby)<br>SIRC, FIRC,<br>SXOSC<br>V11 (Run) VSS<br>FXOSC V11<br>(Standby) SOG (Run)<br>Flash<br>memory PLL<br>&<br>TempSense<br>VSS VSS<br>(Double bond) (Double bond)<br>V25 V11<br>VDD_HV_A VREFH VREFL<br>VSS<br><!-- End of picture text -->

Figure 163. Block diagram 

## 42.5 Signals 

Table 221. Signals 

|Signal|Type|Description|
|---|---|---|
|VDD_HV_A|Supply input|The primary high-voltage supply input to PMC. VDD_HV_A is used<br>for the PMC internal precision references. After the VDD_HV_A power<br>domain is powered up, it must always be kept powered for both FPM<br>and LPM.|
|V25|Supply output|A fully integrated low-dropout linear voltage regulator drives the V25<br>power supply domain. V25 supplies the flash memory and (via a<br>double bond) the clock modules.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1414 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K312) 

Table 221. Signals (continued) 

|Signal|Type|Description|
|---|---|---|
|V11|Supply output|V11 is the core and logic supply. A fully integrated low-dropout linear<br>voltage regulator drives V11.|
|VSS|Ground|VSS must be grounded. You must connect all VSS pins externally to<br>the same ground node.|



## 42.6 Functional description 

### 42.6.1 Reset 

The POR and all LVRs combine into one single chip POR. 

After a chip POR event, you can determine which power domain caused it by reading the PORF and LVRx flags in Low Voltage Status And Control (LVSC). 

After an initial power ramp-up of the chip in LVSC, PMC sets the POR and LVRx flags. The go/no go flags have an arbitrary value. 

~~<mark>NOTE</mark>~~ 

After an initial power ramp-up, you must clear all flags in LVSC by writing FFFF_FFFFh to that register. 

Because the flags are sticky bits, you must clear them before using them. That way, if an unexpected chip POR occurs you can track and debug the source of the problem by reading the flags in LVSC. 

### 42.6.2 Interrupts 

PMC includes two interrupt sources: 

- HVD interrupt: Combines all HVD monitors into one interrupt source. CONFIG[HVDIE] enables this interrupt. See PMC Configuration (CONFIG) and Low Voltage Status And Control (LVSC) for details. 

- LVD interrupt: The LVD5A monitor is the only interrupt source. CONFIG[LVDIE] enables this interrupt. See PMC Configuration (CONFIG) and Low Voltage Status And Control (LVSC) for details. 

## 42.7 PMC register descriptions 

### 42.7.1 PMC memory map 

PMC base address: 402E_8000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|Low Voltage Status And Control (LVSC)|32|W1C|See<br>description|
|4h|PMC Configuration (CONFIG)|32|RW|0000_0000h|
|Ch|Version ID (VERID)|32|RO|0300_0000h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1415 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K312) 

### 42.7.2 Low Voltage Status And Control (LVSC) 

#### Offset 

|Register|Offset|
|---|---|
|LVSC|0h|



#### Function 

Contains status and control fields that support the low-voltage reset and low- or high-voltage detect functions. When PMC is in LPM, the low- or high-voltage detect systems are disabled. 

~~<mark>NOTE</mark>~~ 

For all flags that are not affected by reset (POR flag, all LVR flags, all GNG flags), if a reset occurs while trying to clear the flags (by writing 1), the flag value is not defined appropriately. In this case, you must clear the flag again after exiting from reset. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/042_Power_Management_Controller_-PMC_for_S32K312-/S32K3XXRM_数据表.pdf-1416-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>GNG1 GNG2 LVR11 LVR11 LVR25 LVR25 LVRAL<br>R PORF  0 0 LVRAF<br>1OS... 5OS... LPF  F  LPF  F  PF<br>W W1C W1C W1C W1C W1C W1C W1C W1C W1C<br>Reset u 0 0 0 0 0 u u u u u u 0 0 u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>LVD5A HVD11 HVD25 HVDA LVD5A HVD11 HVD25 HVDA<br>R 0 0 0 0<br>S  S  S  S  F  F  F  F<br>W W1C W1C W1C W1C<br>Reset 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31|POR Flag|
|PORF|Indicates that a power-on reset event has occurred. Other reset sources have no effect.|
||This field behaves differently for read and write operations.<br>~~NOTE~~|
||When reading|
||0b - Event did not occur|
||1b - Event occurred|
||When writing|
||0b - No effect|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1416 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K312) 

#### Table continued from the previous page... 

|Field|Function<br>1b - Clear the flag|
|---|---|
|30-26<br>—|Reserved|
|25<br>GNG11OSCF|Go/No Go Detect Flag On OSC Part Of V11 Power Domain<br>Indicates that the go/no go sensor has detected a low voltage in the V11 power domain in FPM. This<br>applies only to the part of the power domain that supplies the 1.1 V clocking modules (for example, PLL).<br>Other reset sources have no effect.<br>This field behaves differently for read and write operations.<br>~~NOTE~~|
||When reading<br>0b - Event did not occur<br>1b - Event occurred<br>When writing<br>0b - No effect<br>1b - Clear the flag|
|24|Go/No Go Detect Flag On OSC Part of V25 Power Domain|
|GNG25OSCF|Indicates that the go/no go sensor has detected a low voltage in the V25 power domain in FPM. This<br>applies only to the part of the power domain that supplies the 2.5 V clocking modules (for example,<br>XOSC and IRC). Other reset sources have no effect.|
||This field behaves differently for read and write operations.<br>~~NOTE~~|
||When reading<br>0b - Event did not occur<br>1b - Event occurred<br>When writing<br>0b - No effect<br>1b - Clear the flag|
|23<br>LVR11LPF|LVR11LP Flag On V11 Power Domain<br>Indicates that a low-voltage reset event has occurred in the 1.1 V V11 power domain (FPM or<br>LPM).Other reset sources have no effect.<br>This field behaves differently for read and write operations.<br>~~NOTE~~<br>When reading<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1417 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K312) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/042_Power_Management_Controller_-PMC_for_S32K312-/S32K3XXRM_数据表.pdf-1418-03.png)


<!-- Start of picture text -->
Field Function<br>0b - Event did not occur<br>1b - Event occurred<br>When writing<br>0b - No effect<br>1b - Clear the flag<br>22 LVR11 Flag On V11 Power Domain In FPM<br>LVR11F Indicates that a low-voltage reset event has occurred in the 1.1 V V11 power domain in FPM. Other reset<br>sources have no effect.<br>  NOTE<br>This field behaves differently for read and write operations.<br>When reading<br>0b - Event did not occur<br>1b - Event occurred<br>When writing<br>0b - No effect<br>1b - Clear the flag<br>21 LVR25LP Flag On V25 Power Domain<br>LVR25LPF Indicates that a low-voltage reset event has occurred in the V25 power domain (FPM or LPM). Other<br>reset sources have no effect.<br>  NOTE<br>This field behaves differently for read and write operations.<br>When reading<br>0b - Event did not occur<br>1b - Event occurred<br>When writing<br>0b - No effect<br>1b - Clear the flag<br>20 LVR25 Flag On V25 Power Domain In FPM<br>LVR25F Indicates that a low-voltage reset event has occurred in the V25 power domain in FPM. Other reset<br>sources have no effect.<br>  NOTE<br>This field behaves differently for read and write operations.<br>When reading<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1418 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K312) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/042_Power_Management_Controller_-PMC_for_S32K312-/S32K3XXRM_数据表.pdf-1419-03.png)


<!-- Start of picture text -->
Field Function<br>0b - Event did not occur<br>1b - Event occurred<br>When writing<br>0b - No effect<br>1b - Clear the flag<br>19-18 Reserved<br>—<br>17 LVRALP Flag On VDD_HV_A Power Domain<br>LVRALPF Indicates that a low-voltage reset event has occurred in the VDD_HV_A power domain (FPM or LPM).<br>Other reset sources have no effect.<br>  NOTE<br>This field behaves differently for read and write operations.<br>When reading<br>0b - Event did not occur<br>1b - Event occurred<br>When writing<br>0b - No effect<br>1b - Clear the flag<br>16 LVRA Flag On VDD_HV_A Power Domain In FPM<br>LVRAF Indicates that a low-voltage reset event has occurred in the VDD_HV_A power domain in FPM. Other<br>reset sources have no effect.<br>  NOTE<br>This field behaves differently for read and write operations.<br>When reading<br>0b - Event did not occur<br>1b - Event occurred<br>When writing<br>0b - No effect<br>1b - Clear the flag<br>15-13 Reserved<br>—<br>12 LVD5A Status On VDD_HV_A Power Domain In FPM<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1419 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K312) 

#### Table continued from the previous page... 

|Field<br>LVD5AS|Function<br>Indicates whether the voltage on VDD_HV_A is above or below the low-voltage detect threshold. This<br>monitor reflects the status of the 5 V low-voltage detect, LVD5A, and indicates if the voltage is below<br>a certain threshold, which is set slightly below 4.5 V (see the chip data sheet for the exact value). The<br>feature is only available in FPM and is disabled in LPM. After a reset or wake-up from LPM, you must<br>clear the LVD5AF flag and check LVD5AS to determine the voltage level on the VDD_HV_A supply.<br>0b - Above<br>1b - Below|
|---|---|
|11<br>HVD11S|HVD11 Status On V11 Power Domain In FPM<br>Indicates whether the voltage on V11 is above or below the high-voltage detect threshold. This field<br>reflects the status of the high-voltage detect, HVD11, on the V11 power domain. This feature is only<br>available in FPM and is disabled in LPM.<br>0b - Voltage is below threshold or chip is in LPM<br>1b - Voltage is above threshold and chip is in FPM|
|10<br>HVD25S|HVD25 Status On V25 Power Domain In FPM<br>Indicates whether the voltage on V25 is above or below the high-voltage detect threshold. This field<br>reflects the status of the high-voltage detect, HVD25, on the V25 power domain. The feature is only<br>available in FPM and is disabled in LPM.<br>0b - Voltage is below threshold or chip is in LPM<br>1b - Voltage is above threshold and chip is in FPM|
|9<br>—|Reserved|
|8<br>HVDAS|HVDA Status On VDD_HV_A Power Domain In FPM<br>Indicates whether the voltage on VDD_HV_A is above or below the high-voltage detect threshold. This<br>field reflects the status of the high-voltage detect, HVDA, on the V25 power domain. The feature is only<br>available in FPM and is disabled in LPM.<br>0b - Voltage is below threshold or chip is in LPM<br>1b - Voltage is above threshold and chip is in FPM|
|7-5<br>—|Reserved|
|4<br>LVD5AF|LVD5A Flag On VDD_HV_A Power Domain In FPM<br>Indicates whether LVD5AS has changed. When LVD5AS changes, PMC changes LVD5AF to 1.<br>This field behaves differently for read and write operations.<br>~~NOTE~~<br>When reading|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1420 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K312) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Modes_and_Power_Management/042_Power_Management_Controller_-PMC_for_S32K312-/S32K3XXRM_数据表.pdf-1421-03.png)


<!-- Start of picture text -->
Field Function<br>0b - Did not change<br>1b - Changed<br>When writing<br>0b - No effect<br>1b - Clear the flag<br>3 HVD11 Flag On V11 Power Domain In FPM<br>HVD11F Indicates whether HVD11S has changed. When HVD11S changes, PMC changes HVD11F to 1.<br>  NOTE<br>This field behaves differently for read and write operations.<br>When reading<br>0b - Did not change<br>1b - Changed<br>When writing<br>0b - No effect<br>1b - Clear the flag<br>2 HVD25 Flag On V25 Power Domain In FPM<br>HVD25F Indicates whether HVD25S has changed. When HVD25S changes, PMC changes HVD25F to 1.<br>  NOTE<br>This field behaves differently for read and write operations.<br>When reading<br>0b - Did not change<br>1b - Changed<br>When writing<br>0b - No effect<br>1b - Clear the flag<br>1 Reserved<br>—<br>0 HVDA Flag On VDD_HV_A Power Domain In FPM<br>HVDAF Indicates whether HVDAS has changed. When HVDAS changes, PMC changes HVDAF to 1.<br>  NOTE<br>This field behaves differently for read and write operations.<br>When reading<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1421 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K312) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Did not change|
||1b - Changed|
||When writing|
||0b - No effect|
||1b - Clear the flag|



### 42.7.3 PMC Configuration (CONFIG) 

#### Offset 

|Register|Offset|
|---|---|
|CONFIG|4h|



Function Configures PMC. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0||||||||
|W||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R|||0||||LVDIE|HVDIE||0|||LPM25|FAST|0|
|W|||||||||||||EN|REC||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



#### Fields 

|Field|Function|
|---|---|
|31-10|Reserved|
|—||
|9|Low Voltage Detect Interrupt Enable|
|LVDIE|Enables hardware interrupt requests ifLVSC[LVD5AF]= 1. You must disable the LVD interrupt before<br>entering LPM.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1422 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K312) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - LVD hardware interrupt is disabled (use polling)<br>1b - Request an LVD hardware interrupt when LVDA5F = 1|
|8<br>HVDIE|High Voltage Detect Interrupt Enable<br>Enables hardware interrupt requests if any of the following flags inLow Voltage Status And Control<br>(LVSC)are set:<br>• HVDAF<br>• HVDBF<br>• HVD25F<br>• HVD11F<br>0b - HVD hardware interrupt is disabled (use polling)<br>1b - Request an HVD hardware interrupt when HVDAF=1, HVDBF=1, HVD25F=1, or HVD11F=1|
|7-4<br>—<br>3<br>LPM25EN|Reserved<br>V25 Power Domain Enable During LPM<br>Controls whether the V25 regulator and low-voltage reset detection (LVR25LP) are enabled or disabled<br>in LPM<br>0b - Disabled<br>1b - Enabled|
|2<br>FASTREC|Fast Recovery From LPM Enable<br>Controls the recovery time from LPM to FPM.<br>At recovery from LPM, all the tank capacitors from the secondary supplies must be recharged. This causes a<br>high-current demand, which the supply driving the VDD_HV_A primary power domain might not meet. When<br>you select the fast recovery time, the current for recharging is approximately three times higher than that<br>for normal recovery time. You must determine whether this current is sufficient to start up from LPM in time,<br>using these criteria:<br>• Drive capability of the external VDD_HV_A regulator<br>• Size of the tank caps on the secondary supply pin<br>• Selected recovery time<br>0b - Normal<br>1b - Fast|
|1-0<br>—|Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1423 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K312) 

### 42.7.4 Version ID (VERID) 

#### Offset 

|Register|Offset|
|---|---|
|VERID|Ch|



#### Function 

Records the specific PMC version in the chip. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||MAJ|OR|||||||MIN|OR||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|1|1|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0||||||||LMFE<br>AT|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-24|Major Version Number|
|MAJOR|Indicates the major version number of the PMC design.|
|23-16|Minor Version Number|
|MINOR|Indicates the minor version number of the PMC design.|
|15-1|Reserved|
|—<br>0|Last-Mile Regulator Feature|
|LMFEAT|Indicates whether the last-mile regulator (1.5 V to 1.1 V) is available.<br>0b - Not available<br>1b - Available|



## 42.8 Glossary 

FPM Full Performance mode 

HVD High voltage detect 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1424 / 4640 

NXP Semiconductors 

Power Management Controller (PMC for S32K312) 

LPM Low Power mode LVD Low voltage detect LVR Low voltage reset POR Power-on reset 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1425 / 4640 

