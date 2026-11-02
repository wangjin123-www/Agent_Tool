NXP Semiconductors 

# Chapter 31 Boot Overview 

## 31.1 Overview 

### 31.1.1 Introduction 

This chapter describes the system boot sequence and provides details of boot options. The only CPU available when the hardware reset sequence completes is in the HSE subsystem hereafter referred to as HSE CPU. 

The HSE CPU starts executing firmware code in HSE code flash from fixed location that contains the Secure BAF code . Secure BAF provides the boot sequence until control is passed as determined by the type of boot: 

- Non-Secure boot - To customer software that executes on one or all the application cores. 

- Secure boot - To the HSE FW running on HSE CPU. 

## 31.2 Secure BAF features 

The features of Secure BAF are as follows: 

- Secure and Non-secure boot modes 

- Application boot core selection 

- Chip LC advancement 

- Debug authorization 

- XRDC configuration 

## 31.3 Chip Configuration 

This section describes the chip configuration details for S32K3xx variants when Secure BAF is programmed and HSE Firmware feature flag is disabled. 

If HSE firmware feature flag is enabled see the HSE Firmware Reference manual. 

### 31.3.1 Memory map 

This section explains the memory sections used by the Secure BAF in various configurations. 

#### 31.3.1.1 Memory map when HSE firmware usage feature flag is disabled 

Table 165. Memory map when HSE firmware usage feature flag is disabled 

|Memory Section|S32K311|S32K341|S32K312,<br>S32K322,<br>S32K342,|S32K314,<br>S32K324,<br>S32K344|S32K328, S32K338,<br>S32K348, S32K358|
|---|---|---|---|---|---|
|Flash memory|1 MB|1 MB|2 MB|4 MB|8 MB|
|IVT<br>Locations in<br>Priority order|0040_0000h,<br>0048_0000h,<br>1000_0000h|0040_0000h,<br>1000_0000h|0040_0000h,<br>0050_0000h,<br>1000_0000h|0040_0000h,<br>0050_0000h,<br>0060_0000h,<br>0070_0000h|0x0040_0000h,<br>0x0060_0000h,<br>0x0080_0000h,<br>0x00A0_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

979 / 4640 

NXP Semiconductors 

Boot Overview 

Table 165. Memory map when HSE firmware usage feature flag is disabled (continued) 

|Memory Section|S32K311|S32K341|S32K312,<br>S32K322,<br>S32K342,|S32K314,<br>S32K324,<br>S32K344|S32K328, S32K338,<br>S32K348, S32K358|
|---|---|---|---|---|---|
|Flash memory|1 MB|1 MB|2 MB|4 MB|8 MB|
|||||1000_0000h|0x1000_0000h|
|Secure BAF Boot<br>Location|004F_FC00h|005F_FC00h||007F_FC00h|00BF_FC00h|
|Secure BAF<br>code region|004F_4000h<br>to 004F_FFFFh<br>(48 KB)|005F_4000h to 00|5F_FFFFh (48 KB)|007F_4000h<br>to 007F_FFFFh<br>(48 KB)|00BF_4000h to<br>00BF_FFFFh (48 KB)|
|Application Flash area|00400_000h<br>to 004F_3FFFh<br>(976 KB)|0040_0000h<br>to 004F_FFFFh<br>(1024 KB)|00400_000h<br>to 005F_3FFFh<br>(2000 KB)|0040_0000h<br>to 007F_3FFFh<br>(4048 KB)|00400_000h<br>to 00BF_3FFFh<br>(8144 KB)|
|Application Data Flash|1000_0000h to<br>1000_FFFFh (64<br>KB)|1000_0000h to 1|001_FFFFh (128 KB|)||
|Secure BAF UTEST<br>flash||1B00_0|200h to 1B00_06FF|h (1280 Bytes)||



#### 31.3.1.2 Memory map when HSE firmware usage feature flag is enabled 

Following table explains the memory sections used by the Secure BAF in case HSE firmware feature flag is enabled in UTEST. Below tables are applicable for standard firmware in which HSE Firmware size is 128 KB. For custom firmware, the secure size depends on size of custom HSE Firmware. This table is provided for the information to the user that how much memory will be used by security firmware in case security feature is enabled. 

Table 166. Memory map when full memory HSE firmware is installed 

|Memory Section|S32K311|S32K341|S32K312,<br>S32K322,<br>S32K342|S32K314,<br>S32K324,<br>S32K344|S32K328, S32K338,<br>S32K348, S32K358|
|---|---|---|---|---|---|
|Flash<br>memory|1 MB|1 MB|2 MB|4 MB|8 MB|
|IVT<br>Locations in<br>Priority order|0040_0000h,<br>0048_0000h,<br>1000_0000h|0040_0000h,<br>1000_0000h<br>Table continue|0040_0000h,<br>0050_0000h,<br>1000_0000h<br>s on the next page...|0040_0000h,<br>0050_0000h,<br>0060_0000h,<br>0070_0000h<br>1000_0000h|0040_0000h,<br>0060_0000h,<br>0080_0000h,<br>00A0_0000h<br>1000_0000h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

980 / 4640 

NXP Semiconductors 

Boot Overview 

Table 166. Memory map when full memory HSE firmware is installed (continued) 

|Memory Section|S32K311|S32K341|S32K312,<br>S32K322,<br>S32K342|S32K314,<br>S32K324,<br>S32K344|S32K328, S32K338,<br>S32K348, S32K358|
|---|---|---|---|---|---|
|Flash<br>memory|1 MB|1 MB|2 MB|4 MB|8 MB|
|Secure BAF Boot<br>Location|004F_FC00h|005F_FC00h||007F_FC00h|00BF_FC00h|
|Secure BAF<br>code region|004F_4000h<br>to 004F_FFFFh<br>(48 KB)|005F4_000h to 00|5F_FFFFh (48 KB)|007F_4000h<br>to 007F_FFFFh<br>(48 KB)|00BF_4000h to<br>00BF_FFFFh (48 KB)|
|Full memory HSE<br>Firmware<br>code area in last block|004D_4000h<br>to 004F_3FFFh<br>(128 KB)|005D_4000h to 0<br>(128 KB)|05F_3FFFh|007D_4000h<br>to 007F_3FFFh<br>(128 KB)|00BD_4000h to<br>00BF_3FFFh (128 KB)|
|Application Flash area<br>when Full memory HSE<br>Firmware present|0040_0000h<br>To 004D_3FFFh<br>(848 KB)|0040_0000h<br>to 004F_FFFFh<br>(1024 KB)|0040_0000h<br>to 005D_3FFFh<br>(1824 KB)|0040_0000h<br>to 007D_3FFFh<br>(3920 KB)|0040_0000h<br>to 00BD_3FFFh<br>(8016 KB)|
|Application Data Flash|1000_0000h to<br>1000_FFFFh (64<br>KB)|1000_0000h to 10|01_5FFFh (88 KB)|||
|Secure BAF<br>UTEST Flash||1B00_0|200h to 1B00_06FF|h (1280 Bytes)||



Table 167. Memory map in AB swap configuration 

|Memory<br>Section|S32K311|S32K341|S32K312,<br>S32K322,<br>S32K342|S32K314,<br>S32K324, S32K344|S32K328,<br>S32K338,<br>S32K348,<br>S32K358|
|---|---|---|---|---|---|
|Flash<br>memory|1 MB|1 MB|2 MB|4 MB|8 MB|
|IVT locations in<br>priority order|0040_0000h,<br>1000_0000h|0040_0000h,<br>1000_0000h|0040_0000h,<br>1000_0000h|0040_0000h,<br>0050_0000h,<br>1000_0000h|0040_0000h,<br>0060_0000h,<br>1000_0000h|
|HSE FW boot<br>location|0047_FC00h|004F_FC00h|004F_FC00h|005F_FC00h|007F_FC00h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

981 / 4640 

NXP Semiconductors 

Boot Overview 

Table 167. Memory map in AB swap configuration (continued) 

|Memory<br>Section|S32K311|S32K341|S32K312,<br>S32K322,<br>S32K342|S32K314,<br>S32K324, S32K344|S32K328,<br>S32K338,<br>S32K348,<br>S32K358|
|---|---|---|---|---|---|
|Flash<br>memory|1 MB|1 MB|2 MB|4 MB|8 MB|
|AB Swap HSE<br>firmware code<br>area in active<br>block<sup>1</sup>|0045_4000h<br>to 0047_FFFFh<br>(176 KB)|004D_4000h<br>to 004F_FFFFh<br>(176 KB)|004D_4000h<br>to 004F_FFFFh<br>(176 KB)|005D_4000h to<br>005F_FFFFh (176 KB)|007D_4000h to<br>007F_FFFFh (176<br>KB)|
|AB Swap HSE<br>firmware code<br>area in passive<br>block<sup>1</sup>|004D_4000h<br>to 004F_FFFFh<br>(176 KB)|005D_4000h<br>to 005F_FFFFh<br>(176 KB)|005D_4000h<br>to 005F_FFFFh<br>(176 KB)|007D_4000h to<br>007F_FFFFh (176 KB)|00BD_4000h to<br>00BF_FFFFh<br>(176 KB)|
|Application<br>Flash area in<br>active block|0040_0000h to<br>0045_3FFFh (336<br>KB)|0040_0000h<br>to 0047_FFFFh<br>(512 KB)|0040_0000h<br>to 004D_3FFFh<br>(848 KB)|0040_0000h to<br>005D_3FFFh (1872 KB)|0040_0000h<br>to 007D_3FFFh<br>(3920 KB)|
|Application<br>Flash area in<br>passive block|00480_000h to<br>004_D3FFFh (336<br>KB)|0050_0000h<br>to 0057_FFFFh<br>(512 KB)|0050_0000h<br>to 005D_3FFFh<br>(848 KB)|0060_0000h to<br>007D_3FFFh (1872 KB)|0080_0000h<br>to 00BD_3FFFh<br>(3920 KB)|
|Application<br>Data Flash|1000_0000h<br>to<br>1000_FFFFh<br>(64 KB)|1000_0000h to 10|01_FFFFh (128 KB)|||
|Secure BAF<br>UTEST<br>Flash||1B00|_0200h to 1B00_06FF|h (1280 Bytes)||



1. HSE firmware includes the Secure BAF in AB swap configuration 

### 31.3.2 Hardware protection 

Platform flash of S32K3xx has facilitated hardware protection exclusive to HSE core. BAF releases hardware protection of that area which is being used by Application as mentioned in previous section. If the hardware protection fails, for security purpose, Secure BAF issues a reset. 

Below table explains default values of Hardware protection. 

Table 168. Hardware protection by Secure BAF 

|Register name|Register address<br>Secure memory|Configured value|
|---|---|---|
|CONFIG_RAMPR|4039_C038h<br>SRAM memory|4000_0000h|
||Table continues on the next page...||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

982 / 4640 

NXP Semiconductors 

Boot Overview 

Table 168. Hardware protection by Secure BAF (continued) 

|Register name|Register address|Secure memory|Configured value|
|---|---|---|---|
|CONFIG_CFPRL|4039_C03Ch|Code flash memory active block|4000_0000h|
|CONFIG_CFPRH|4039_C040h|Code flash memory passive block|4000_C000h|
|CONFIG_DFPR|4039_C044h|Data flash memory|4002_0000h|



## 31.4 Device common configuration 

### 31.4.1 Feature configuration in virgin device 

Following table lists down the status of various features when device "LC = CUST_DEL". Many features are configurable directly or indirectly by application software. 

|Feature|Configuration information|Status|Configurability|
|---|---|---|---|
|OTA functionality|Samples are always shipped in the OTA<br>disabled configuration|Disabled|Yes<br>Can be enabled by<br>application by requesting<br>to HSE firmware or<br>Secure BAF|
|HSE firmware usage<br>feature flag|This flag indicates whether firmware installation<br>allowed in the device or not. By default, this flag<br>is unprogrammed and Secure BAF assumes that<br>firmware installation is not allowed.|Disabled|Yes<br>Can be enabled by<br>programming in the<br>UTEST location. More<br>details on “UTEST Flag<br>description” section.|
|Secure BAF firmware|Samples are always shipped with Secure<br>BAF programmed|Programmed|No|
|HSE Firmware|HSE firmware is always programmed by user/<br>Encrypted and signed firmware image is always<br>delivered to user.|Not programmed|Yes<br>Can be installed by the<br>application software.|
|Image Vector Table|No IVT is programmed at any of the IVT locations.|Not programmed|Yes<br>Can be programmed by<br>application software.|
|SWT0|Application core watchdog SWT0 is disabled.|Disabled|Yes<br>It can be optionally<br>enabled by BAF if SWT<br>bit is configured in boot<br>configuration word.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

983 / 4640 

NXP Semiconductors 

Boot Overview 

##### Table continued from the previous page... 

|Feature|Configuration information|Status|Configurability|
|---|---|---|---|
|Boot Sequence|Boot sequence is non-secure boot<br>i.e. application are booted by Secure BAF without<br>any authentication.|Non secure boot|Yes<br>It can be changed<br>to secure boot<br>by programming the<br>BOOT_SEQ bit in IVT.|
|Life Cycle|Samples are always delivered in LC=CUST_DEL|Customer Delivery|Yes<br>It can be changed<br>to OEM_PROD and<br>IN_FIELD by application<br>through Secure BAF and<br>HSE firmware.|
|Application Core<br>enablement status|All applications cores are in disable state.|Disabled.|Yes<br>Single or all application<br>cores can be enabled<br>at required address by<br>programming the required<br>fields in the IVT.|
|Clock Source|Fast Internal Reference clock|FIRC|Yes|
|FIRC Frequency Value|48 MHz|48 MHz|Yes, application can<br>configures after Secure<br>BAF goes in WFI.|
|Application debug<br>authorization mode|Debug Authorization mode of application cores is<br>password based. It can be changed to challenge<br>response mode by programming the configuration<br>in UTEST.|Password<br>based approach|When HSE Firmware<br>Feature flag is disabled,<br>debug authorization mode<br>cannot be changed.<br>When HSE Firmware<br>Feature flag is enabled,<br>debug authorization mode<br>can be changed to<br>challenge response mode<br>by requesting to HSE<br>firmware.|
|Application core<br>debug status|Debug of application cores is enabled in customer<br>delivery lifecycle.|Enabled|No|



### 31.4.2 Secure BAF memory map description 

Following table explains the memory sections used by the Secure BAF. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

984 / 4640 

NXP Semiconductors 

Boot Overview 

Table 169. Secure BAF memory 

|Memory Section|Remarks|
|---|---|
|IVT location|This is the base address of IVT. The size of IVT is always 256 byte starting from base address.<br>IVT at one location must be programmed by the application.|
|Secure BAF boot location|Location where interrupt vector table of HSE core is present. Secure BAF on HSE CPU boots<br>from this location. From this address 1024 bytes of interrupt vector table is present.<br>This location is protected by XRDC and it can be accessed only by HSE core.|
|Secure BAF code region|Secure BAF code area in flash. This area is protected by XRDC and it can be accessed only by<br>HSE core.|
|UTEST flash location|1280 Kbytes of UTEST area of flash.|



### 31.4.3 UTEST memory usage by Secure BAF 

Table 170. UTEST memory location usage by Secure BAF 

|Start address|End address|Size (bytes)|Description|Programmed by|Write protected|
|---|---|---|---|---|---|
|1B00_0000h|1B00_0007h|8|HSE Firmware<br>Feature Usage<br>flag. For more<br>detail, seeUTEST<br>flag description|Application|No|
|1B00_0040h|1B00_0047h|8|Unique Chip<br>Identifier (UID) 0|NXP|No|
|1B00_0050h|1B00_0057h|8|FXOSC<br>enablement flag<br>For more<br>detail,UTEST<br>flag description|Application|No|
|1B00_0080h|1B00_009Fh|32|Debug<br>password(CUST_D<br>B_PSWD_A).<br>When HSE FW<br>feature Flag is<br>disabled, this<br>location is used<br>by Secure BAF<br>to run the debug<br>authorization<br>feature. Secure<br>BAF copies this<br>value in application<br>expected response|Application|No|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

985 / 4640 

NXP Semiconductors 

Boot Overview 

Table 170. UTEST memory location usage by Secure BAF (continued) 

|Start address|End address|Size (bytes)|Description|Programmed by|Write protected|
|---|---|---|---|---|---|
||||register and this<br>value is used to<br>derive the HSE<br>expected response<br>register. Size of<br>this register is 16B<br>and 1B00_0090h<br>– 1B00_009h<br>is reserved.<br>When HSE<br>Firmware feature<br>flag is enabled,<br>password is<br>programmed by<br>HSE firmware at<br>different location.<br>Password is<br>scanned by DCM<br>during Reset only.<br>Password to be<br>retained in standby.|||
|1B00_0220h|1B00_022Fh|16|Lifecycle slot<br>1: CUST_DEL|NXP|Yes|
|1B00_0230h|1B00_023Fh|16|Lifecycle slot<br>2: OEM_PROD|Secure BAF|Yes|
|1B00_0240h|1B00_024Fh|16|Lifecycle slot<br>3: IN_FEILD|Secure BAF|Yes|
|1B00_0250h|1B00_025Fh|16|Lifecycle slot<br>4: Pre-FA|Secure BAF|Yes|
|1B00_0260h|1B00_026Fh|16|Lifecycle slot 5: FA|Secure BAF|Yes|



Detail description of each field is out of scope of this document. For details, see S32K3xx_DCF_clients file attached with this document. 

### 31.4.4 UTEST flag description 

#### 31.4.4.1 HSE firmware usage feature flag 

This flag is an indication to Secure BAF that application intend to use HSE firmware on the device. By default, this flag is unprogrammed and Secure BAF assumes that HSE firmware installation is not allowed in the secure samples. But, if application decides to allow installation of HSE firmware, it can program the HSE Firmware Usage Feature flag in the UTEST at location 0x1B000000. 

Description of the flag as follows: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

986 / 4640 

NXP Semiconductors 

Boot Overview 

Table 171. HSE firmware usage feature flag description 

|Field type|Description|Remarks|
|---|---|---|
|Size|64 bits||
|Default value|0xFFFFFFFFFFFFFFFF||
|Default status|Disabled|Secure BAF does not allows installation<br>of HSE firmware.|
|UTEST location|0x1B000000||
|Programmed by|Application software||
|LC in which programming is allowed|All LC||
|Value to program to to enable HSE<br>FW installation|Any value other than default value|Secure BAF allows installation of<br>HSE firmware.|



Implication when this flag is not programmed by application 

- Secure BAF never try to install the HSE firmware. 

- Secure BAF does not protect the HSE firmware code flash area. 

- The logic of debug authorization protocol is different. See Debug authorization for more details. 

- Secure BAF does not protect the data flash area reserved for HSE firmware. 

- Debug authorization always be password based for application cores. 

- Secure BAF always boot the application without any authentication. BOOT_SEQ bit in the boot configuration word is ignored. 

- Secure BAF does not authenticate the IVT and XRDC configuration table in all LC. 

- Application password area in UTEST area is not read and write protected by XRDC in LC = CUST_DEL. In other LC, it is accessible only to HSE core. 

- Number of region descriptors in MRC0 and MRC1 increased which can be configured by the application. 

- Default configuration of XRDC and valid address range changed. For more details see XRDC configuration. 

#### 31.4.4.2 Crystal oscillator configuration flag 

Description of the flag as follows: 

|Field type|Description|
|---|---|
|Size|64 bits|
|Default Value|FFFF_FFFF_FFFF_FFFFh|
|Default Status|Boot via FIRC|
|UTEST Location|1B00_0050h|
|Programmed by|Application|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

987 / 4640 

NXP Semiconductors 

Boot Overview 

##### Table continued from the previous page... 

|Field type|Description|
|---|---|
|LC in which programming is allowed|All LC|



Table 172. Crystal oscillator configuration flag in UTEST 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/031_Boot_Overview/S32K3XXRM_数据表.pdf-0988-05.png)


<!-- Start of picture text -->
63 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48<br>R FXOSC_ENABLE_MAGIC_NUMBER<br>W<br>47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32<br>R<br>W<br><!-- End of picture text -->


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/031_Boot_Overview/S32K3XXRM_数据表.pdf-0988-06.png)


<!-- Start of picture text -->
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R GMSEL EOCV<br>W<br>15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R CRYSTAL_OSCILLATOR_FREQUENCY<br>W<br><!-- End of picture text -->

Table 173. Crystal oscillator configuration bit definition 

|Field|Description|
|---|---|
|63-33|FXOSC_ENABLE_MAGIC_NUMBER|
||AAAA_5555h – Enable|
||FFFF_FFFFh – Disable|
|31 - 28|GMSEL (Crystal overdrive protection):|
||For invalid values = 0x0 or 0xF, default value 0xC is used.|
|27 - 20|EOCV (End of count value):|
||For invalid value = 0x0, default value 9Dh is used.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

988 / 4640 

NXP Semiconductors 

Boot Overview 

|19 - 16|Reserved|
|---|---|
|15 - 0|CRYSTAL_OSCILLATOR_FREQUENCY:|
||Crystal frequency in KHz. Valid Crystal frequency range is 8000 – 40000 KHz. BAF does not checks for invalid|
||frequencies. This field is only necessary if HSE Firmware installation is required.|



## 31.5 Image Vector Table 

The following section describes the various fields in Image Vector Table that is to be programmed by the application. IVT is scanned by Secure BAF after the device is out of reset. The structure is 256 bytes in size. This structure contains application core start address, XRDC configuration etc. It must be programmed at least at one of the locations as mentioned in Chip Configuration 

After reset, Secure BAF searches for the first valid IVT starting from the lowest address. If there are multiple valid IVT at IVT locations at the same time, the lowest address wins the priority. 

Table 174. Image Vector Table 

|Address<br>offset|Size in<br>bytes|Content|Comments|
|---|---|---|---|
|00h|4|Image Vector<br>Table Marker|It is a magic number which marks the starting of Image Vector Table location.<br>Its value must be 5AA5_5AA5h|
|04h|4|Boot<br>Configuration Word|Configuration word that allows the user to select the various configuration in<br>which device can be booted. Details are mentioned in the next section.|
|08h|4|Reserved||
|0Ch|4|CM7_0<br>application<br>Start Address|Boot address of CM7_0 application in code flash area. It must honor<br>core VTOR register alignment restrictions. This field is used by BAF when<br>BOOT_SEQ bit is 0.|
|10h|4|Reserved||
|14h|4|CM7_1<br>application<br>Start Address|Boot address of CM7_1 application in code flash area. It must honor core<br>VTOR register alignment restrictions. This field is used by BAF only when<br>BOOT_SEQ bit is 0.<br>This filed is ignored if Lockstep configuration is enabled.<br>Reserved for S32K31x|
|18h|4|Reserved||
|1Ch|4|CM7_2<br>application<br>Start Address|Boot address of CM7_2 application in code flash area. It must honor core<br>VTOR register alignment restrictions. This field is used by BAF only when<br>BOOT_SEQ bit is 0<br>Reserved for S32K31x, S32K32x, and S32K34x|
|20h|4|Reserved||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

989 / 4640 

NXP Semiconductors 

Boot Overview 

Table 174. Image Vector Table (continued) 

|Address|Size in|Content|Comments|
|---|---|---|---|
|offset|bytes|||
|24h|4|Address of|Address of Configuration word that allows User to Advance LC. Details are|
|||LC Configuration|mentioned below.|
|28h|216|Reserved||



### 31.5.1 Boot configuration word 

This register informs Secure BAF to allow booting of selected applications. 

Table 175. Boot configuration register 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/031_Boot_Overview/S32K3XXRM_数据表.pdf-0990-07.png)


<!-- Start of picture text -->
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>W<br>15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>W<br>APP_SWT_INIT RESERVED BOOT_SEQ CM7_2_ENABLE CM7_1_ENABLE CM7_0_ENABLE<br><!-- End of picture text -->

Table 176. Boot configuration register bit definition 

|Field|Description|
|---|---|
|31 – 6|Reserved|
|5|APP_SWT_INIT: Control SWT0 enablement before control is passed to application core(s).<br>0 Disable<br>1 Enable<br>BAF initializes the SWT0 before enabling the application cores. BAF scans this bit only when BOOT_SEQ bit is 0.|
|4|RESERVED|
|3|BOOT_SEQ|
||Control the boot flow of the application.|
||0 Non-Secure Boot- Application image without any authentication is started by Secure BAF in parallel to HSE<br>firmware.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

990 / 4640 

NXP Semiconductors 

Boot Overview 

Table 176. Boot configuration register bit definition (continued) 

||1 Secure Boot- Application image is executed by HSE firmware after the authentication. Secure BAF only starts the<br>HSE firmware after successful authentication.<br>(Only valid for HSE Firmware feature flag enabled)|
|---|---|
|2|CM7_2_ENABLE<br>0 Cortex-M7_2 application core clock gated after boot<br>1 Cortex-M7_2 application core clock un-gated after boot<br>Reserved for S32K31x, S32K32x, S32K34x.|
|1|CM7_1_ENABLE<br>0 Cortex-M7_1 application core clock gated after boot<br>1 Cortex-M7_1 application core clock un-gated after boot<br>This field is ignored if Lockstep configuration is enabled.<br>Reserved for S32K31x|
|0|CM7_0_ENABLE<br>0 Cortex-M7_0 application core clock gated after boot<br>1 Cortex-M7_0 application core clock un-gated after boot|



### 31.5.2 Address LC configuration word 

This field allows User to Advance LC. To advance lifecycle User must program a valid 32 bits wide value at an address which must be given in IVT at address offset 24h. This address must be 4 bytes aligned and should not lie in Secure BAF/HSE FW protected areas. 

Valid values for advancement in next lifecycles are mentioned in below table. For all other values at given address lifecycle advancement is not allowed. 

Table 177. Valid values for lifecycle advancement 

|Lifecyle|Valid values for lifecycle advancement|
|---|---|
|OEM_PROD|DADA_DADAh|
|IN_FIELD|BABA_BABAh|



Application password on the location depending on HSE FW Feature flag must be program before lifecycle advancement otherwise lifecycle advancement doesn’t attempted by Secure BAF. 

The SoC provides a LC mechanism for an irreversible progression of restrictions to accessing security related content on the device. The device LC cannot be reversed, so it is only possible to mature the device. Secure BAF takes on the responsibility of advancing the device through the LC: 

- CUST_DEL --> OEM_PROD 

- CUST_DEL and OEM_PROD --> IN_FIELD 

Advancing the LC through Secure BAF involves configuring the LC configuration word in the IVT. Upon successful advancement, Secure BAF issues a Destructive reset. LC advancement is ignored if the device is found in same LC as indicated by the IVT. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

991 / 4640 

NXP Semiconductors 

Boot Overview 

### 31.5.3 Structure definition of Image Vector Table 

Following structure can be used by application to configure the IVT configuration. 

~~<mark>NOTE</mark>~~ 

The fields which are not valid for the specific configuration must be kept reserved. For Secure-Boot, see HSE Firmware Reference Manual. 

```
typedef const struct image_vector_table
{
uint32_t Header; /*Header of IVT Structure */
uint32_t BootConfig; /*Boot Configuration Word */
const uint32_t Reserved1; /* Reserved */
const uint32_t * CM7_0_StartAddress; /*Start Address of Application on CM7_0 Core */
const uint32_t Reserved2; /* Reserved */
const uint32_t * CM7_1_StartAddress; /*Start Address of Application on CM7_1 Core */
const uint32_t Reserved3; /* Reserved */
const uint32_t * CM7_2_StartAddress; /*Start Address of Application on CM7_1 Core */
const uint32_t * Reserved4; /* Reserved */
const uint32_t * LCConfig; /*Address of LC configuration Word */
uint8_t Reserved5[216];
}ivt_t;
```

### 31.5.4 Invalid IVT scenarios 

This section lists down the scenarios in which IVT is considered as invalid by Secure BAF. 

1. IVT marker is not present. 

2. ECC error is present in any of the 256 bytes of IVT memory. 

## 31.6 Boot flow 

Below diagram explains boot sequence flow of Secure BAF. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/031_Boot_Overview/S32K3XXRM_数据表.pdf-0992-13.png)


<!-- Start of picture text -->
START Reset Exit System Initialization<br>Standby Exit<br>Normal Boot Load and verify the<br>IVT<br>Standby Boot<br>Valid IVT Valid? Invalid<br>Boot the Application Failure Execute Recovery<br>Mode Sequence<br>Execute Debug  Shutdown<br>Success Authorization<br>Secure BAF<br>Sequence<br>Figure 129. Boot flow<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

992 / 4640 

NXP Semiconductors 

Boot Overview 

## 31.7 Standby boot 

Secure BAF supports boot from Standby exit. SOC register DCMRWF5 (address 0x402AC610) provided to support boot on standby exit. This register gets clear on POR. For more details, see chapter Device Configuration Module (DCM) in S32K3xx Reference Manual. 

Application is supposed to program this register before entering the standby mode. 

There are two types of boot mode on exit from standby. 

- Fast standby mode 

- Normal boot on exit from standby 

In Fast standby mode Secure BAF boots CM7_0 and halts the HSE core. The flow of standby boot is explained below: 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/031_Boot_Overview/S32K3XXRM_数据表.pdf-0993-09.png)


<!-- Start of picture text -->
Standby Boot Flow Normal Boot Flow<br>START<br>MC_ME_MODE_<br>Status[PreviousMode] RESET EXIT<br>STANDBY EXIT<br>DCMRWF5[0] for StandBy Boot  NORMAL STANDBY EXIT<br>Configuration<br>FAST STANDBY EXIT<br>Release FIRC Divider for  Continue with Secure BAF<br>Application Core boot Flow<br>Read App Core reset register<br>DCMRWF5[31:1]<br>MC_ME_CADDR_CM7_0 = Core<br>Reset Address for standby Exit<br>Enable CM7_0<br>Shutdown<br>Secure BAF<br>Figure 130. Standby boot flow<br><!-- End of picture text -->

## 31.8 Reduced clock mode configuration 

In case user wants to use clocking option B, application can enable this mode by setting “dcf_client_utest_misc” DCF record. For more details on DCF record, see the DCF sheet available with the S32K3xx Reference Manual. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

993 / 4640 

NXP Semiconductors 

Boot Overview 

After reset, Secure BAF checks for the HSE_CLK_MODE_OPTION field in DCMROF21 register in DCM. If this field is configured for clocking option B, Secure BAF configures the following dividers in MC CGM 

- MUX_0_DC_1 

- MUX_0_DC_2 

Below figure explains steps for reduced clock mode configuration steps by Secure BAF. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/031_Boot_Overview/S32K3XXRM_数据表.pdf-0994-06.png)


<!-- Start of picture text -->
Start<br>YES NO<br>HSE_CLK_MODE_OPTION =<br>2b10<br>Configure<br>MC_CGM_MUX_0_DC_1[DIV]<br>for AIPS_PLAT_CLK as 2<br>Configure STATUS =<br>MC_CGM_MUX_0_DC_2[DIV]<br>CONFIGURATION_NOT_REQUIRED<br>for AIPS_SLOW_CLK as 4<br>STATUS =<br>CONFIGURATION_SUCCESS<br>return STATUS<br>End<br>Figure 131. Reduced clock mode configuration<br><!-- End of picture text -->

## 31.9 Debug authorization 

If HSE firmware feature flag is disabled then application core debug is always password based. CUST_DB_PSWD_A must be programmed at location 1B00_0080h. See UTEST memory usage by Secure BAF more details. 

## 31.10 FIRC divider register control 

FIRC divider is controlled by Configuration HSE GPR Register (CONFIG_REG_GPR) address 0x4039C064. This HSE GPR register for FIRC divider is write protected by default and application can’t modify it. 

After Secure BAF executes WFI, it provides write access to FIRC divider field of this HSE GPR register and application can configure this register. Before access to this register, application should wait for Secure BAF to go in WFI by reading register PRTN0_CORE2_STAT. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

994 / 4640 

NXP Semiconductors 

Boot Overview 

## 31.11 Application boot 

Secure-BAF is not responsible for booting application image in a secure way. The responsibility of booting application image in a secure way lies with HSE firmware. In case secure boot is not requested (by setting BOOT_SEQ bit in Boot configuration word in IVT structure to 0), the application image is always loaded by Secure-BAF without authentication in all LC of the device. By default, Secure-BAF releases the reset of every core which is configured to be enabled. 

Following flow chart explains the steps of application boot performed by Secure-BAF when boot sequence field in boot configuration word is configured to 0. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/031_Boot_Overview/S32K3XXRM_数据表.pdf-0995-05.png)


<!-- Start of picture text -->
Start<br>Extract the core enable bit mask<br>from Boot Configuration field<br>YES At least one  NO<br>bit mask is set?<br>Extract the Start Address of Return Application Boot<br>Application Core(s) from Status as FAIL<br>Application IVT<br>Enable Application Core(s) End<br>Is SWT bit set in Boot YES Return Application Boot<br>Enable the SWT0 Watchdog<br>Configuration Word Status as SUCCESS<br>NO<br>Trigger Mode Transition<br>Figure 132. Application boot sequence<br><!-- End of picture text -->

Before configuring HSE_CLK, application should wait for Secure BAF to go in WFI by reading register PRTN0_CORE2_STAT. 

## 31.12 Recovery mode sequence 

This feature is provided to allow the user to program the application image in LC = MCU_PROD and LC= CUST_DEL and debug the reason of corruption of IVT and re-program the IVT in other LC. 

Below are the scenarios when Secure BAF executes recovery mode sequence. 

- Valid IVT is not found. 

- Application is not booted by Secure BAF. 

- Application enablement bit is not programmed in Boot configuration word in IVT. 

- Application issued more than eight functional reset and disable recovery mode on functional reset bit is not disabled in DCMRWP1 register. 

- Application issued more than eight destructive reset and disable recovery mode on destructive reset bit is not disabled in DCMRWP1 register. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

995 / 4640 

NXP Semiconductors 

Boot Overview 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Reset_and_Boot/031_Boot_Overview/S32K3XXRM_数据表.pdf-0996-02.png)


<!-- Start of picture text -->
Start<br>YES Is Lifecycle = MCU_PROD or NO<br>Lifecycle = CUST_DEL?<br>This bit determine<br>whether debugger is<br>Is Functional Reset<br>attached to the<br>Counter ≥ 8?<br>system or not.<br>Only when debugger is<br>attached, application<br>cores will be enabled  Is EDB bit in HSE_GPR set? YES<br>at default address NO This bit determine<br>whether successful<br>Start the timer<br>YES debug authorization<br>NO sequence has<br>been completed<br>and JTAG is<br>enabled on the<br>Disable the STM timer YES Is APPDBG_STAT_SOC application core<br>bit set in DCMDEB?<br>NO<br>NO<br>Copy Infinite Loop 30 seconds Timeout?<br>Code to SRAM<br>YES<br>Enable the Application  Return Recovery Status as<br>Core(s) at SRAM address FAIL<br>Return Recovery Status as End<br>SUCCESS<br><!-- End of picture text -->

Figure 133. Recovery mode sequence 

The infinite loop with WFI code is copied to SRAM1 i.e. 2040_0100h and size of code is 16B. To prevent prefetching errors in application cores, the Infinite loop instruction is placed at 2040_012Ch. 

## 31.13 XRDC configuration 

Secure BAF needs to ensure that is has access to its own resources and application don’t have access to secure area. The following sections describe the XRDC default configuration values when HSE Firmware feature flag is disabled. In this scenario, application don’t required to provide XRDC configuration via IVT and Secure BAF never enables the XRDC at any time. 

When HSE Firmware Feature flag is enabled, Application can provide XRDC configuration via IVT. For this scenario, see HSE-B Firmware reference manual for the details of XRDC configuration. 

### 31.13.1 XRDC configuration of MDAC 

Following table list down the default configuration of MDAC by Secure BAF. 

Table 178. MDAC registers default value 

|Device variant|MDAC Register HSE CPU|Value|Domain number assigned to<br>HSE core|
|---|---|---|---|
|S32K31x|MDAC3|C000_0001h|1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

996 / 4640 

NXP Semiconductors 

Boot Overview 

Table 178. MDAC registers default value (continued) 

|Device variant|MDAC Register HSE CPU|Value|Domain number assigned to<br>HSE core|
|---|---|---|---|
|S32K32x, S32K34x|MDAC3|C000_0002h|2|
|S32K35x, S32K33x, K3E|MDAC3|C000_0003h|3|



All the other MDAC domain numbers are 0 and not locked by Secure-BAF. 

### 31.13.2 XRDC configuration of MRC 

Following table list down the default configuration of MRC by Secure BAF. 

Table 179. Default Configuration of MRC 

|MRC<br>Number|Region<br>Descriptor<br>Number|Name|Remarks|Configuration done by Secure BAF|
|---|---|---|---|---|
|0|14|HSE UTEST<br>area|UTEST area that is accessible by<br>HSE core only.<br>See chip configuration chapter<br>for<br>Start<br>address<br>and<br>End address.|W0- Start address W1= End<br>Address W2={ SE=0,SNUM=0,<br>HSE domain =0x7[All permission]|
|0|15|Secure BAF<br>Code area|Code area for Secure BAF. See<br>chip configuration chapter for<br>Start address and End address.|W0- Start address<br>W1= End Address<br>W2={ SE=0, SNUM=0,<br>HSE domain =0x7[All permission]<br>Other domains = 0x00 [No permission]<br>}<br>W3={VLD=1, LK2=0x3}|



## 31.14 BAF flash programming controls 

Platform flash controller generates an exception of Read-while-Write if Read and Write are performed on the same block simultaneously. HSE core can also perform the Program and Erase for application, and the status is indicated at Configuration PE Lock Register (CONFIG_PE_LOCK) in the HSE space. 

BAF locks the high addressing code flash block during its execution and it's cleared when HSE core enters into WFI. Address of high addressing code flash area should be referred to chip configuration chapter. 

Before Programming/Erasing/Executing from this address space, application core is requested to poll for WFI bit of PRTN0_CORE2_STAT register to ensure HSE core is in WFI state. 

For Boot Sequence 1 or flash synchronization with HSE Firmware, see HSE Firmware reference manual. 

Below table explains PE lock bits setting in CONFIG_PE_LOCK register of HSE GPR during Secure BAF execution. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

997 / 4640 

NXP Semiconductors 

Boot Overview 

Table 180. PE lock bits setting in CONFIG_PE_LOCK register of HSE GPR 

|Chip<br>variants|UTEST<br>Block|Data Flash Block|Code Flash<br>Block 3|Code Flash<br>Block 2|Code Flash<br>Block 1|Code Flash<br>Block 0|
|---|---|---|---|---|---|---|
|S32K3x1|1|0|0|0|0|1|
|S32K3x2|1|0|0|0|1|0|
|S32K3x4|1|0|1|0|0|0|



## 31.15 Status registers for application usage 

This section explain various status register configuration to provide status information to application. 

### 31.15.1 Secure BAF version information 

Secure BAF version is a 64-bit field. Secure BAF version can be read by application from HSE GPR register 4039_C020h. The version information is explained below. 

Table 181. Secure BAF version information 

|Bit number|Field Name|Description|
|---|---|---|
|0 – 7|RESERVED|Reserved, must be 0|
|8 - 15|SOC_TYPE_ID|This field Identifies the SoC family<br>0 – not used<br>5 – HSE-B S32K3x4<br>11 - HSE-B S32K3x0<br>12 - HSE-B S32K3x1<br>13 - HSE-B S32K3x2<br>14 - HSE-B S32K3x8<br>15 - HSE-B S32K3x6|
|16 - 31|FW_TYPE|This field identify the FW type:<br>0 – Standard generic FW targeting all customers<br>1-7 – Reserved<br>8 >= Custom1, Custom2 (For example: Custom1 = customer X’s project A, Custom2 =<br>customer Y’s project B)|
|32 - 39|MAJOR_REV|Major version number<br>0 - EAR/BETA<br>1 - at first RTM and incremented by 1 for subsequent RTM|
|40 - 47|MINOR_REV|4 – Pre-EAR<br>8 - EAR|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

998 / 4640 

NXP Semiconductors 

Boot Overview 

Table 181. Secure BAF version information (continued) 

|||9 - BETA<br>This field is reset for every new MAJOR_REV change.|
|---|---|---|
|48 - 63|PATCH_REV|bug fix releases (After BETA) or new feature for EAR/PRE-EAR releases. (least significant<br>8 bits are reserved for hotfix / frozen branch info)|



### 31.15.2 DCM Register DCMRWP1 

Application can disable recovery mode entry by Secure BAF after programming bits 23 and 22 of DCM register DCMRWP1. This register gets clears on power on reset. 

Table 182. DCM register DCMRWP1 availalble at address 402A_C400h 

|Bits|Number<br>of bits|R/W access<br>by application|Description|
|---|---|---|---|
|24-31|8||Reserved|
|23|1|R/W|Disable recovery mode on destructive reset.<br>This bit is reset by default and Secure BAF allows recovery mode sequence if<br>Application issues >8 destructive reset. Application can set this bit to disable<br>recovery mode when Application issues > 8<br>destructive reset. [1]|
|22|1|R/W|Disable recovery mode on functional reset.<br>This bit is reset by default and Secure BAF allows recovery mode sequence<br>if Application issues >8 functional reset. Application can set this bit to disable<br>recovery mode when Application issues > 8<br>functional reset. [1]|
|21|1|R|Reserved|
|16-20|5|R|Recovery mode Reset counter. For OEM_PROD and INFIELD lifecycle, to enable<br>recovery mode functionality, Secure BAF increments this counter when Functional<br>or destructive reset is issued.|
|15|1|R|Reserved|
|11-14|4|R|Destructive reset counter. Secure BAF increments this counter when Destructive<br>reset is issued.|
|0-10|11|R|Reserved|



[1] Application core should not modify other bits of this register while updating these bits. 

### 31.15.3 Status bits on HSE GPR register 

HSE GPR register 4039_C028h is configured by Secure BAF to show various status information as explained in below table. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

999 / 4640 

NXP Semiconductors 

Boot Overview 

Table 183. Status bits on HSE GPR register available at 4039_C028h 

|Bit|Description|
|---|---|
|0|HSE FW is present and booted by Secure BAF.|
|1-4|Reserved|
|5|Application cores booted in Recovery mode by SBAF.|
|6|Debug Authentication performed by SBAF.|
|7-31|Reserved.|



## 31.16 Interrupt and exception handling 

### 31.16.1 Interrupt handling 

No special interrupt handling routines are required during the boot process. Interrupts are disabled during Secure BAF execution. 

### 31.16.2 Exception handling 

Secure BAF enters the recovery mode after Enabling Debug Authorization. 

After eight consecutive functional resets or destructive resets either from Application Firmware, the Device Enters the Recovery Mode. 

### 31.16.3 Boot target watchdog 

Secure BAF conditionally configures SWT0 watchdog with default timeout i.e. 25 ms, before enabling the application core(s). It is expected that the application services this watchdog before expiration. 

## 31.17 Hardware modules used by Secure BAF 

### 31.17.1 MC_ME 

Secure BAF uses MC_ME to enable the Application cores, mode switch, and other operations during its execution. MC_ME operations supported by Secure BAF are discussed in below section. 

### 31.17.2 FXOSC 

Secure BAF configures FXOSC if FXOSC enablement flag is programmed in UTEST. 

### 31.17.3 Clock Generation Module (MC_CGM) 

Secure BAF configures MC_CGM in Reduced Clock Mode as well. See following section for the same. 

### 31.17.4 DCM 

Secure BAF uses the DCM to identify the Life-Cycle, Standby Boot Configuration, Lockstep, Reduced Clock Mode Configuration. 

### 31.17.5 HSE_GPR 

Secure BAF configures Hardware Protection, Program Erase Lock, FIRC Divider Control, Secure BAF Version number, HSE FW Handshaking via HSE-GPR. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1000 / 4640 

NXP Semiconductors 

Boot Overview 

### 31.17.6 XRDC 

Secure BAF configures the XRDC Configuration. See XRDC Configuration for the same. 

### 31.17.7 Flash module 

Secure BAF always perform the write and erase operation on alternate interface. 

See Chip Configuration for details of Flash memory usage by Secure BAF. 

## 31.18 Hardware IP registers details modified by Secure BAF 

Below table explains the registers details which are modified by Secure BAF when HSE Firmware Feature Flag is disabled. 

Table 184. Hardware IP registers modified by Secure BAF 

|IP|Register Name|Default value (hex)|Modified value (hex)|
|---|---|---|---|
||Master Domain Assignment (MDA_W0_3_DFMT0)|0000_0000h|C000_0002h<br>C000_0001h|
||Memory Region Descriptor (MRGD_W0_14)|0000_0001h|HSE Utest Start<sup>1</sup>|
||Memory Region Descriptor (MRGD_W1_14)|0000_001Fh|HSE Utest End<sup>1</sup>|
||Memory Region Descriptor (MRGD_W2_14)|0000_0000h|0000_01C0h|
||Memory Region Descriptor (MRGD_W3_14)|0000_0000h|E000_0000h|
||Memory Region Descriptor (MRGD_W0_15)|0000_0001h|HSE Code Flash Start<sup>1</sup>|
||Memory Region Descriptor (MRGD_W1_15)|0000_001Fh|HSE code Flash End<sup>1</sup>|
||Memory Region Descriptor (MRGD_W2_15)|0000_0000h|0000_01C0h|
||Memory Region Descriptor (MRGD_W3_15)|0000_0000h|E000_0000h|
||Peripheral Domain Access Control (PDAC_W0_155)|0000_0000h|0000_01C0h|
||Peripheral Domain Access Control (PDAC_W1_155)|0000_0000h|E000_0000h|
||Peripheral Domain Access Control (PDAC_W0_188)|0000_0000h|0000_01C0h|
||Peripheral Domain Access Control (PDAC_W1_188)|0000_0000h|E000_0000h|
||Peripheral Domain Access Control (PDAC_W0_231)|0000_0000h|0000_01FFh|
||Peripheral Domain Access Control (PDAC_W1_231)|0000_0000h|E000_0000h|
|General<br>purpose<br>it ith|Configuration Program and Erase<br>Lock (CONFIG_PE_LOCK)|0000_0000h|Protect only HSE Area<sup>1</sup>|
|regsers w<br>write access by<br>HSE core|Configuration RAM Protected<br>Region (CONFIG_RAMPR)|See chapter<br>Hardware Security<br>Engine (HSE_B)|Release Full memory<sup>1</sup>|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1001 / 4640 

NXP Semiconductors 

Boot Overview 

Table 184. Hardware IP registers modified by Secure BAF (continued) 

|IP|Register Name|Default value (hex)|Modified value (hex)|
|---|---|---|---|
||Configuration RAM Protected Region<br>Alternate (CONFIG_RAMPR_ALT)|See chapter<br>Hardware Security<br>Engine (HSE_B)|Release Full memory<sup>1</sup>|
||Configuration Code Flash Memory Active<br>Block (CONFIG_CFPRL)|See chapter<br>Hardware Security<br>Engine (HSE_B)|Protect only HSE Code Flash<br>Area<sup>1</sup>|
||Configuration Code Flash Memory Active Block<br>Alternate (CONFIG_CFPRL_ALT)|See chapter<br>Hardware Security<br>Engine (HSE_B)|Protect only HSE Code Flash<br>Area<sup>1</sup>|
||Configuration Code Flash Memory Passive<br>Block (CONFIG_CFPRH)|See chapter<br>Hardware Security<br>Engine (HSE_B)|Protect only HSE Code Flash<br>Area<sup>1</sup>|
||Configuration Code Flash Memory Passive Block<br>Alternate (CONFIG_CFPRH_ALT)|See chapter<br>Hardware Security<br>Engine (HSE_B)|Protect only HSE Code Flash<br>Area<sup>1</sup>|
||Configuration Data Flash Memory Protected Region<br>(CONFIG_DFPR)|See chapter<br>Hardware Security<br>Engine (HSE_B)|Protect only HSE Data Flash<br>Area<sup>1</sup>|
||Configuration Data Flash Memory Protected Region<br>Alternate (CONFIG_DFPR_ALT)|See chapter<br>Hardware Security<br>Engine (HSE_B)|Protect only HSE Data Flash<br>Area<sup>1</sup>|
||Configuration REG_GPR (CONFIG_REG_GPR)|A000_0003h|Refer chapter ”FIRC Divider<br>Register Control“.|
|MC_ME|Partition 1 COFB Set 1 Clock Status<br>Register (PRTN1_COFB1_STAT)|1CFE_2FFCh|Clock of FXOSC and<br>MC_CGM are enabled by<br>default. But for 120 MHz clock<br>request, Secure BAF ensures<br>if MC_CGM clock is enabled.|
||Partition 0 Core 0 Address<br>Register (PRTN0_CORE0_ADDR)|0040_0000h|Secure BAF update this<br>address if App core 0 boot<br>is requested during Normal<br>boot sequence in IVT. Or in<br>recovery mode.|
||Partition 0 Core 0 Process Configuration<br>Register (PRTN0_CORE0_PCONF)|0000_0000h|0000_0001h|
||Partition 0 Core 0 Process Update<br>Register (PRTN0_CORE0_PUPD)|0000_0000h|0000_0001h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1002 / 4640 

NXP Semiconductors 

Boot Overview 

Table 184. Hardware IP registers modified by Secure BAF (continued) 

|IP|Register Name|Default value (hex)|Modified value (hex)|
|---|---|---|---|
||Partition 0 Core 1 Process Configuration<br>Register (PRTN0_CORE1_PCONF)|0000_0000h|0000_0001h|
||Partition 0 Core 1 Process Update<br>Register (PRTN0_CORE1_PUPD)|0000_0000h|00000001h|
||Partition 0 Core 1 Address<br>Register (PRTN0_CORE1_ADDR)|0041_0000h|Secure BAF update this<br>address if App core 1 boot<br>is requested during Normal<br>boot sequence in IVT. Or in<br>recovery mode.|
||Partition 0 Core 2 Process Configuration<br>Register (PRTN0_CORE2_PCONF)|0000_0000h|0000_0001h|
||Partition 0 Core 2 Process Update<br>Register (PRTN0_CORE2_PUPD)|0000_0000h|0000_0001h|
||Partition 0 Core 2 Address<br>Register (PRTN0_CORE2_ADDR)|See Mode<br>Entry Module<br>(MC_ME) chapter|Secure BAF update this<br>address if App core 2 boot<br>is requested during Normal<br>boot sequence in IVT. Or in<br>recovery mode.|
||Control Key Register (CTL_KEY)|0000_5AF0h|Secure BAF update this<br>register if anyone of<br>application core is booted<br>by Secure BAF. 0000_5AF0h<br>and then 0000_A50Fh|
|FXOSC|FXOSC Control Register (CTRL)|019D_00C0h|SeeCrystal oscillator<br>configuration flag|
|MC_RGM|Functional Reset Escalation Counter Register (FREC)|0000_0000h|0000_0000h|
||Destructive Reset Escalation Threshold<br>Register (DRET)|0000_0000h|0000_000Fh|
|SWT_0|Control (CR)|FF00_010Ah|FF00_000Bh|
||Interrupt (IR)|0000_0000h|0000_0001h|
||Service (SR)|0000_0000h|C520h and then D928h|



1. See Chip Configuration for details of HSE area addressing. 

## 31.19 Appendix 

Secure BAF takes into account for following scenarios to prevent bricking of device : 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1003 / 4640 

NXP Semiconductors 

Boot Overview 

After Maximum Functional Resets are observed in the device, BAF enters into Recovery Mode, to recover application core’s failing status. 

BAF does not allows the LC to be advanced to OEM_PROD or IN_FIELD, if CUST_DBG_PSWD/ADKP is not programmed by the Application. 

BAF boots the Application from System-RAM during recovery to avoid unpredictable behavior. 

## 31.20 Glossary 

AES Advanced Encryption Standard; a cipher primitive BAF Boot Assist Flash CUST_DEL Device Life Cycle customer delivery IN_FIELD Device Life Cycle is IN_FIELD LC Device Life Cycle; used to limit by design the configuration and debug/test possibilities of the device for in-field usage 

MCU_PROD Device Life Cycle MCU Production 

OEM_PROD Device Life Cycle OEM Production 

OTA Over The Air 

Secure BAF Secure Boot Assist Flash 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1004 / 4640 

