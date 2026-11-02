NXP Semiconductors 

# Chapter 35 Hardware Security Engine (HSE_B) 

## 35.1 HSE subsystem 

HSE is a security subsystem. It runs security functions for applications having stringent confidentiality and authenticity requirements. HSE has the following objectives: 

- Isolating security-sensitive information (for example, secret keys) from the application (the host) 

- Transferring the cryptographic operations from application cores and processing them 

- Accelerating cryptographic operations with dedicated coprocessors 

- Enforcing security measures on the application, during runtime and system startup 

The HSE subsystem is the only master that is unconditionally released from reset after POR. It then releases the CPU subsystems in the host from reset, with the opportunity to apply certain checks beforehand (secure system startup). Based on certain conditions, HSE can also trigger interrupts and reset signals to the host during runtime. 

### 35.1.1 CPU subsystem 

The HSE CPU subsystems process the security functions and control system resources to provide security services to the application domain (the host). 

### 35.1.2 Cryptographic accelerators 

The HSE subsystem supports the following cryptographic accelerators: 

- An AES engine supporting all standard key sizes (128, 192, 256 bits) and various complex ciphering modes (ECB, CBC, CTR, OFB, CFB, CCM, CMAC) 

- A hash engine that supports standard several primitives: MD5, SHA-1, SHA-224, SHA-256 

- PKC which accelerates RSA and ECC operations (key generation, signature generation, signature verification, ciphering) 

   - RSA (1024, 2048, 3072, 4096-bit) 

   - ECC over prime numbers 

      - ◦BN P256, P638 

      - ◦ANSI X9P192 to X9P512 

      - ◦Brainpool P160 to P512 

      - ◦Sec P128 to P521 

      - ◦TU Darmstadt prime Curve 1 to 35 

      - ◦Ed25519 

The HSE subsystem supports several other cryptographic primitives through the software. See HSE firmware for more information. 

### 35.1.3 Random number generator (RNG) 

The RNG in this chip consists of a TRNG and a DRBG. Both are designed to be compliant to the highest strength in security as specified in 

- BSI AIS20/31 

- NIST SP800-90a,b,c 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1039 / 4640 

NXP Semiconductors 

Hardware Security Engine (HSE_B) 

The TRNG function provides a seed for the DRBG, while the DRBG is available to the host via dedicated random number generation services. 

### 35.1.4 Timers 

The HSE subsystem features: 

- An independent dedicated system timer 

- HSE_STM (apart from chip timer resources), that allows recurring autonomous functions such as runtime memory verification checks 

- A watchdog timer to reset the HSE subsystem in case of unexpected runtime failure 

### 35.1.5 Memory resources 

See Configuration_GPR memory map for more information on configuration controls related to HSE functions. 

#### 35.1.5.1 Secure RAM 

Secure RAM refers to RAM area that the HSE subsystem access exclusively. The HSE firmware use it to operate as well as to store a copy of the cryptographic keys in service. 

#### 35.1.5.2 Secure NVM 

Secure NVM refers to nonvolatile memory that the HSE subsystem accesses exclusively. It stores the HSE firmware and the security assets (for example, keys and private data). 

The size of the secure NVM is configurable by the HSE firmware. 

## 35.2 HSE interface 

### 35.2.1 Messaging unit (MU) 

The HSE subsystem has two messaging units: 

- HSE_MU0 

- HSE_MU1 

See the "Messaging Unit (MU)" chapter for more information. 

#### 35.2.1.1 Overview 

MU is the communication interface between the host and the HSE subsystem. The host uses MU to trigger service requests and to receive service responses. The HSE firmware uses MU to receive service requests, return service responses, and provide a general status of the HSE subsystem. 

Each of the two MU instances available in the HSE subsystem has: 

- Two sides: 

   - MUA: Only the HSE subsystem accesses it. 

   - MUB: The host accesses it. 

The registers on one side have corresponding registers on the other side. 

- A set of 32-bit readable and writable transmit registers (MUB_TRn), which the host uses to transfer the address of the service descriptor to the HSE firmware. The HSE firmware retrieves the address of the service descriptor in the corresponding registers MUA_RRn. 

- A set of 32-bit read-only receive registers (MUB_RRn), which the host uses to retrieve the response to the service requests. The HSE firmware provides the response to service requests in the corresponding registers MUA_TRn. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1040 / 4640 

NXP Semiconductors 

Hardware Security Engine (HSE_B) 

- Control and status registers to manage MU and the access to transmit and receive registers. 

The advantages of using the MU to manage the HSE service requests and responses are: 

- Hardware mechanisms are in place on the transmit registers to avoid service request overrun. 

- Interrupt signals are available to allow asynchronous management of the requests (avoiding active waiting loops). 

- Freedom from interference between different application cores. You can configure each MU instance with specific access restrictions that can be used, for example, to isolate the requests that different masters make (in different MU instances). You configure such access controls using XRDC. 

### 35.2.2 HSE interface RAM 

The HSE interface RAM (also known as host interface RAM) is a secure RAM area. The host accesses it with the restrictions that HSE set via XRDC. This RAM area is a part of chip RAM and the size is configurable by secure core using CONFIG_RAMPR[SECURE_SIZE]. 

## 35.3 Debug 

### 35.3.1 HSE subsystem debug 

The debugging of the HSE subsystem and associated firmware is restricted to NXP engineering teams. 

### 35.3.2 Host debug 

The host debug is either open or protected, depending on the device Lifecycle state. See the ‘Life cycle’ section in ‘Device Configuration Module’ chapter for details on device lifecycle advancement and decoding. The details of the device security features is published in a separate document, the Security Reference Manual. Please contact your NXP sales representative for details. See the Debug chapter for details on host/application core debug. 

The debug protection consists of locking the debugger access through the JTAG interface until the HSE firmware authenticates the debugger. This authentication is based on ADK/P, a 16-byte region within UTEST used for application core debug. See UTEST memory map in the DCF clients file attached to this document. 

The authentication method can be: 

- Static: In this case, ADK/P is a password which the debugger provides in plain form. 

- Dynamic: In this case, ADK/P is a cryptographic key which the debugger uses to calculate a cryptographic response to a random challenge. 

## 35.4 HSE firmware 

Factory supplied firmware that runs in the HSE subsystem controls HSE functionality. It essentially serves the host with a set of security services as described in Table 190. 

Table 190. Summary of firmware security services 

|Service|Summary|
|---|---|
|Administration|Install, configure, update, and test the HSE firmware|
|Key management|Available for the application to manage different sets of keys that the HSE firmware manages, for<br>example, cryptographic services|
|Cryptographic|Provide the application with cryptographic primitives that high level security stacks use in<br>the application|
|Random number|Generate random streams that can be used in various security protocols|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1041 / 4640 

NXP Semiconductors 

Hardware Security Engine (HSE_B) 

Table 190. Summary of firmware security services (continued) 

|Service|Summary|
|---|---|
|Memory verification|Allow the application to verify different memory areas at startup (after reset) and during runtime|
|Monotonic counter|Provide the application with a set of monotonic counters that can be read and only incremented|
|Secure time|Allow the configuration of a secure tick to be signaled to the application|



Table 191 provides an overview of services and features that the HSE firmware supports. 

Table 191. HSE firmware features 

|Service|Category|Feature|
|---|---|---|
|Cryptography|Ciphers|AES: ECB, CBC, CFB, OFB, CTR,XTS<sup>1</sup><br>RSAES:PKCS1-v1_5,OAEP|
||Message<br>Authentication<br>Code (MAC)|AES:CMAC,XCBC-MAC<sup>1</sup>,HMAC<sup>1</sup>, andGMAC<sup>1</sup>|
||Hashing|SHA1<br>SHA224, SHA256, SHA384, SHA512<br>SHA3_224<sup>1</sup>, SHA3_256<sup>1</sup>, SHA3_384<sup>1</sup>, SHA3_512<sup>1</sup><br>MD5<br>Miyaguchi-Preneel Compression|
||Authenticated ciphers|AES: CCM,GCM<sup>1</sup>|
||Digital signature<br>generation<br>and verification|RSASSA_PSS<br>RSASSA_PKCS1-v1_5<br>ECDSA– ECC over GF(P) with all prime standard curve supported<br>EdDSA- Ed25519 pre-hashed curve|
|Key management|Max key sizes|AES: 256 bits<br>RSA: 4096 bits<br>ECC: 521 bits<br>DH: 4096 bits|
||Key generation|Permanent and ephemeral RSA and ECC key pair generation|
||Key import or export|Plain or encrypted form, with optional authentication tag.<br>SHEkey update protocol|
||Key derivation|NIST800-108, PBKDF2, and so on|
||Key exchange|ECDHandClassic DH|
||Certificate handling|Key Installation from X.509 andCVCcertificates<br>Certificate installation for Root of Trust establishment.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1042 / 4640 

NXP Semiconductors 

Hardware Security Engine (HSE_B) 

Table 191. HSE firmware features (continued) 

|Service|Category|Feature|
|---|---|---|
|Boot and<br>memory verification|Authentication schema|AES CMAC, XCBC-MAC<br>RSA & ECC signatures|
||Verification flow|Before application startup (strict secure boot)<br>In parallel to the application startup<br>On the application demand|
||Sanctions|No startup (strict secure boot)<br>Chip reset<br>Key usage restrictions|
|Monotonic counter|Counter management|Incrementing and reading volatile and non-volatile counters|
|Random number|Deterministic random<br>bit generation|Based on a True Random Number<br>AIS31 Class P2 high and FIPS 140-2 compliant|
|Secure time|Secure tick|Application interrupts at configurable frequency|
|Administration services|HSE administration|Firmware installation and update<br>Subsystem configuration and testing|



1. Software implementation of cryptographic primitives. 

See documents in Table 192 for more information about how to install, configure, and use the HSE firmware that NXP provides. 

Table 192. References 

|Document number|Document title|Description|
|---|---|---|
|HSEFWRM|HSE Firmware<br>Reference Manual|Contains details about how to install, configure, and use the<br>HSE subsystem.|
|HSESIRM|HSE Service Interface<br>Reference Manual|Security firmware API reference for non-AUTOSAR users.|



## 35.5 General purpose registers with write access by HSE core 

This is a general purpose register bank that only the HSE core can write. Secure master ID gating allows only the secure core to write in these registers, whereas any application core can read. 

## 35.6 Configuration_GPR register descriptions 

### 35.6.1 Configuration_GPR memory map 

This section describes the chip configurations that only the HSE core manages. These constitute control of peripherals, secure size configurations for SRAM and flash memory, flash memory program or erase control, and so on. 

~~<mark>NOTE</mark>~~ 

Write accesses to configuration registers apart from 32-bit accesses might result in unpredictable chip behavior, therefore must not be done. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1043 / 4640 

NXP Semiconductors 

Hardware Security Engine (HSE_B) 

##### Configuration_GPR base address: 4039_C000h 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|1Ch|General Purpose Configuration 0 (CONFIG_REG0)|32|RO|0000_0000h|
|34h|General Purpose Configuration 6 (CONFIG_REG6)|32|RO|0000_0035h|
|38h|Configuration RAM Protected Region (CONFIG_RAMPR)|32|RO|See<br>description|
|3Ch|Configuration Code Flash Memory Active Block (CONFIG_CFPRL)|32|RO|See<br>description|
|40h|Configuration Code Flash Memory Passive Block (CONFIG_CFPRH)|32|RO|See<br>description|
|44h|Configuration Data Flash Memory Protected Region<br>(CONFIG_DFPR)|32|RO|See<br>description|
|50h|Configuration Program and Erase Lock (CONFIG_PE_LOCK)|32|RO|0000_0000h|
|54h|Configuration RAM Protected Region Alternate<br>(CONFIG_RAMPR_ALT)|32|RO|See<br>description|
|58h|Configuration Code Flash Memory Active Block Alternate<br>(CONFIG_CFPRL_ALT)|32|RO|See<br>description|
|5Ch|Configuration Code Flash Memory Passive Block Alternate<br>(CONFIG_CFPRH_ALT)|32|RO|See<br>description|
|60h|Configuration Data Flash Memory Protected Region Alternate<br>(CONFIG_DFPR_ALT)|32|RO|See<br>description|
|64h|Configuration REG_GPR (CONFIG_REG_GPR)|32|RW|A000_0003h|
|C0h|QuadSPI SFP Control (QSPI_SFP_CTRL)|32|RO|See<br>description|
|C4h|QuadSPI SFP Control Alternate (QSPI_SFP_CTRL_ALT)|32|RO|See<br>description|



### 35.6.2 General Purpose Configuration 0 (CONFIG_REG0) 

##### Offset 

|Register|Offset|
|---|---|
|CONFIG_REG0|1Ch|



##### Function 

The EDB field resets on destructive or POR reset events and functional reset has no impact on it. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1044 / 4640 

NXP Semiconductors 

Hardware Security Engine (HSE_B) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||Rese|rved||||||||
|W|||||||||||||||||
|Reset|||||||||||||||||
|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||Reserved|||||EDB|||Rese|rved|||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



1. If export_control=1, the reset value of EDB is 1. If export_control=0, the reset value is 0. 

##### Fields 

|Field|Function|
|---|---|
|31-7<br>—|Reserved|
|6|Hardware Debugger Attached|
|EDB|This is a sticky field that clears on destructive reset.<br>0b - Debugger not connected|
||1b - Debugger connected|
|5-0<br>—|Reserved|



### 35.6.3 General Purpose Configuration 6 (CONFIG_REG6) 

##### Offset 

|Register|Offset|
|---|---|
|CONFIG_REG6|34h|



Function 

Resets on functional reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1045 / 4640 

NXP Semiconductors 

Hardware Security Engine (HSE_B) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|HL||||||||Reserve|d|||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||Reserved|||||Reserv<br>ed|SAI_S<br>DI...|FLEXI<br>O_...|Reserv<br>ed|EMAC<br>_CL...|Reserv<br>ed|QUAD<br>SPI...|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|1|1|0|1|0|1|



##### Fields 

|Field|Function|
|---|---|
|31<br>HL|Hard Lock<br>Only functional reset clears this field.<br>0b - You can write to this register<br>1b - Register is locked for any write|
|30-7<br>—|Reserved|
|6<br>—|Reserved|
|5<br>SAI_SDID_PCT<br>L|SAI0 and SAI1 clock gating<br>Clock to SAI peripheral is on or off.<br>0b - Clock is off (gated)<br>1b - Clock is on|
|4<br>FLEXIO_CLOC<br>K_GATE|FlexIO Clock Gating<br>Clock to FlexIO peripheral is on or off.<br>0b - Clock is off (gated)<br>1b - Clock is on|
|3<br>—|Reserved|
|2|Ethernet Clock Gating|
|EMAC_CLOCK<br>_GATE|Clock to Ethernet peripheral is on or off.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1046 / 4640 

NXP Semiconductors 

Hardware Security Engine (HSE_B) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Clock is off (gated)|
||1b - Clock is on|
|1<br>—|Reserved|
|0|QuadSPI Clock Gating|
|QUADSPI_SDI<br>D_PCTL|Clock to QuadSPI peripheral is on or off.<br>0b - Clock is off (gated)|
||1b - Clock is on|



### 35.6.4 Configuration RAM Protected Region (CONFIG_RAMPR) 

##### Offset 

|Register|Offset|
|---|---|
|CONFIG_RAMPR|38h|



##### Function 

##### Resets on functional reset. 

~~<mark>NOTE</mark>~~ 

The secure size will go to default or reset value on assertion of any DCF violation from HSE. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/035_Hardware_Security_Engine_-HSE_B-/S32K3XXRM_数据表.pdf-1047-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>HARD SOFT_<br>R Reserved  SECURE_SIZE<br>_LO... LO...<br>W<br>Reset<br>u u u u u u u u u u u u u u u u<br>1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R SECURE_SIZE  Reserved<br>W<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

1. The default reset value of this register varies on the part basis, depending on NXP factory configurations. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1047 / 4640 

NXP Semiconductors 

Hardware Security Engine (HSE_B) 

##### Fields 

|Field|Function|
|---|---|
|31|Hard Lock|
|HARD_LOCK|This is a sticky field. If you write 1 to it, it remains 1 until next reset.<br>0b - Write access is allowed<br>1b - Write access is not allowed until next functional reset|
|30<br>SOFT_LOCK|Soft Lock<br>0b - Write access is allowed<br>1b - Write access is not allowed|
|29-21<br>—|Reserved|
|20-5|Secure Size|
|SECURE_SIZE|Secure size region (in bytes) for PRAM1. This is 32-byte-aligned to ensure alignment with cache lines.|
|4-0<br>—|Reserved|



### 35.6.5 Configuration Code Flash Memory Active Block (CONFIG_CFPRL) 

##### Offset 

|Register|Offset|
|---|---|
|CONFIG_CFPRL|3Ch|



Function Resets on functional reset. 

~~<mark>NOTE</mark>~~ 

The secure size will go to default or reset value on assertion of any DCF violation from HSE. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/035_Hardware_Security_Engine_-HSE_B-/S32K3XXRM_数据表.pdf-1048-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>HARD SOFT_<br>R Reserved  SECURE_SIZE<br>_LO... LO...<br>W<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1048 / 4640 

NXP Semiconductors 

Hardware Security Engine (HSE_B) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/035_Hardware_Security_Engine_-HSE_B-/S32K3XXRM_数据表.pdf-1049-02.png)


<!-- Start of picture text -->
1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R SECURE_SIZE  Reserved<br>W<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

1. The default reset value of this register varies on the part basis, depending on NXP factory configurations. 

##### Fields 

|Field|Function|
|---|---|
|31<br>HARD_LOCK|Hard Lock<br>After this field is configured it cannot be modified until a reset event.<br>0b - Write access is allowed<br>1b - Write access is not allowed until next functional reset|
|30<br>SOFT_LOCK|Soft Lock<br>0b - Write access is allowed<br>1b - Write access is not allowed|
|29-21<br>—|Reserved|
|20-13|Secure Size|
|SECURE_SIZE|Flash memory active block secure size in bytes to align to 8 KB (sector) aligned write.|
|12-0<br>—|Reserved|



### 35.6.6 Configuration Code Flash Memory Passive Block (CONFIG_CFPRH) 

##### Offset 

|Register|Offset|
|---|---|
|CONFIG_CFPRH|40h|



Function 

Resets on functional reset. 

~~<mark>NOTE</mark>~~ 

The secure size will go to default or reset value on assertion of any DCF violation from HSE. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1049 / 4640 

NXP Semiconductors 

Hardware Security Engine (HSE_B) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/035_Hardware_Security_Engine_-HSE_B-/S32K3XXRM_数据表.pdf-1050-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>HARD SOFT_<br>R Reserved  SECURE_SIZE<br>_LO... LO...<br>W<br>Reset<br>u u u u u u u u u u u u u u u u<br>1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R SECURE_SIZE  Reserved<br>W<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

1. The default reset value of this register varies on the part basis, depending on NXP factory configurations. 

##### Fields 

|Field|Function|
|---|---|
|31<br>HARD_LOCK|Hard Lock<br>After this field is configured, it cannot be modified until a reset event.<br>0b - Write access is allowed<br>1b - Write access is not allowed until next functional reset|
|30<br>SOFT_LOCK|Soft Lock<br>0b - Write access is allowed<br>1b - Write access is not allowed|
|29-21<br>—|Reserved|
|20-13|Secure Size|
|SECURE_SIZE|Secure size region (in bytes) for flash memory passive block for alignment with 8 KB (sector) aligned<br>writes.|
|12-0<br>—|Reserved|



### 35.6.7 Configuration Data Flash Memory Protected Region (CONFIG_DFPR) 

##### Offset 

|Register|Offset|
|---|---|
|CONFIG_DFPR|44h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1050 / 4640 

NXP Semiconductors 

Hardware Security Engine (HSE_B) 

##### Function 

##### Resets on functional reset. 

###### ~~<mark>NOTE</mark>~~ 

The secure size will go to default or reset value on assertion of any DCF violation from HSE. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/035_Hardware_Security_Engine_-HSE_B-/S32K3XXRM_数据表.pdf-1051-07.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>HARD SOFT_<br>R Reserved  SECURE_SIZE<br>_LO... LO...<br>W<br>Reset<br>u u u u u u u u u u u u u u u u<br>1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R SECURE_SIZE  Reserved<br>W<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

1. The default reset value of this register varies on the part basis, depending on NXP factory configurations. 

##### Fields 

|Field|Function|
|---|---|
|31<br>HARD_LOCK|Hard Lock<br>After this field is configured, it cannot be modified until a reset event.<br>0b - Write access is allowed<br>1b - Write access is not allowed until next functional reset|
|30<br>SOFT_LOCK|Soft Lock<br>0b - Write access is allowed<br>1b - Write access is not allowed|
|29-21<br>—|Reserved|
|20-13|Secure Size|
|SECURE_SIZE|Secure size region (in bytes) for data flash memory aligned to 8KB (sector) aligned writes.|
|12-0<br>—|Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1051 / 4640 

NXP Semiconductors 

Hardware Security Engine (HSE_B) 

### 35.6.8 Configuration Program and Erase Lock (CONFIG_PE_LOCK) 

##### Offset 

|Register|Offset|
|---|---|
|CONFIG_PE_LOCK|50h|



##### Function 

Resets on functional reset. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/035_Hardware_Security_Engine_-HSE_B-/S32K3XXRM_数据表.pdf-1052-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>PE_LO Reserv PE_LO<br>R Reserved<br>CK... ed  CK...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>PE_LO PE_LO PE_LO PE_LO<br>R Reserved<br>CK... CK... CK... CK...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-19<br>—|Reserved|
|18|Program/Erase Lock for UTEST|
|PE_LOCK_UTE<br>ST|0b - UTEST lock request is clear<br>1b - UTEST lock requested|
|17<br>—|Reserved|
|16|Program/Erase Lock for Block 4|
|PE_LOCK_BLO<br>CK_4|0b - Block 4 lock request is clear<br>1b - Block 4 lock requested|
|15|Program/Erase Lock for Block 3|
|PE_LOCK_BLO<br>CK_3|0b - Block 3 lock request is clear<br>1b - Block 3 lock requested|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1052 / 4640 

NXP Semiconductors 

Hardware Security Engine (HSE_B) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|14|Program/Erase Lock for Block 2|
|PE_LOCK_BLO<br>CK_2|0b - Block 2 lock request is clear<br>1b - Block 2 lock requested|
|13|Program/Erase Lock for Block 1|
|PE_LOCK_BLO<br>CK_1|0b - Block 1 lock request is clear<br>1b - Block 1 lock requested|
|12|Program/Erase Lock for Block 0|
|PE_LOCK_BLO<br>CK_0|0b - Block 0 lock request is clear<br>1b - Block 0 lock requested|
|11-0<br>—|Reserved|



### 35.6.9 Configuration RAM Protected Region Alternate (CONFIG_RAMPR_ALT) 

##### Offset 

|Register|Offset|
|---|---|
|CONFIG_RAMPR_ALT|54h|



##### Function 

Resets on functional reset. 

~~<mark>NOTE</mark>~~ The secure size will go to default or reset value on assertion of any DCF violation from HSE. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||INVE|RT_VAL|UE_RAM|PR|||||||
|W|||||||||||||||||
|Reset|||||||||||||||||
|1|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||||INVE|RT_VAL|UE_RAM|PR|||||||
|W|||||||||||||||||
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|



1. The default reset value of this register varies on the part basis, depending on NXP factory configurations. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1053 / 4640 

NXP Semiconductors 

Hardware Security Engine (HSE_B) 

##### Fields 

|Field|Function|
|---|---|
|31-0|Invert Value RAMPR|
|INVERT_VALU<br>E_RAMPR|Write inverted value of register CONFIG_RAMPR to CONFIG_RAMPR_ALT.|



### 35.6.10 Configuration Code Flash Memory Active Block Alternate (CONFIG_CFPRL_ALT) 

##### Offset 

|Register|Offset|
|---|---|
|CONFIG_CFPRL_ALT|58h|



Function Resets on functional reset. 

~~<mark>NOTE</mark>~~ 

The secure size will go to default or reset value on assertion of any DCF violation from HSE. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||INVE|RT_VAL|UE_CFP|RAB|||||||
|W|||||||||||||||||
|Reset|||||||||||||||||
|1|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||||INVE|RT_VAL|UE_CFP|RAB|||||||
|W|||||||||||||||||
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|



1. The default reset value of this register varies on the part basis, depending on NXP factory configurations. 

##### Fields 

|Field|Function|
|---|---|
|31-0|Invert Value CFPRAB|
|INVERT_VALU<br>E_CFPRAB|Write inverted value of register CONFIG_CFPRL to CONFIG_CFPRL_ALT.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1054 / 4640 

NXP Semiconductors 

Hardware Security Engine (HSE_B) 

### 35.6.11 Configuration Code Flash Memory Passive Block Alternate (CONFIG_CFPRH_ALT) 

##### Offset 

|Register|Offset|
|---|---|
|CONFIG_CFPRH_ALT|5Ch|



Function 

Resets on functional reset. 

~~<mark>NOTE</mark>~~ 

The secure size will go to default or reset value on assertion of any DCF violation from HSE. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/035_Hardware_Security_Engine_-HSE_B-/S32K3XXRM_数据表.pdf-1055-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R INVERT_VALUE_CFPRP<br>W<br>Reset<br>u u u u u u u u u u u u u u u u<br>1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R INVERT_VALUE_CFPRP<br>W<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

1. The default reset value of this register varies on the part basis, depending on NXP factory configurations. 

##### Fields 

|Field|Function|
|---|---|
|31-0|Invert Value CFPRP|
|INVERT_VALU<br>E_CFPRP|Write inverted value of register CONFIG_CFPRH to CONFIG_CFPRH_ALT.|



### 35.6.12 Configuration Data Flash Memory Protected Region Alternate (CONFIG_DFPR_ALT) 

##### Offset 

|Register|Offset|
|---|---|
|CONFIG_DFPR_ALT|60h|



Function 

Resets on functional reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1055 / 4640 

NXP Semiconductors 

Hardware Security Engine (HSE_B) 

~~<mark>NOTE</mark>~~ 

The secure size will go to default or reset value on assertion of any DCF violation from HSE. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||INV|ERT_VA|LUE_DFP|R|||||||
|W|||||||||||||||||
|Reset|||||||||||||||||
|1|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||||INV|ERT_VA|LUE_DFP|R|||||||
|W|||||||||||||||||
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|



1. The default reset value of this register varies on the part basis, depending on NXP factory configurations. 

##### Fields 

|Field|Function|
|---|---|
|31-0|Invert Value CFPRP|
|INVERT_VALU<br>E_DFPR|Write inverted value of register CONFIG_DFPR to CONFIG_DFPR_ALT.|



### 35.6.13 Configuration REG_GPR (CONFIG_REG_GPR) 

##### Offset 

|Register|Offset|
|---|---|
|CONFIG_REG_GPR|64h|



Function 

Resets on functional reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1056 / 4640 

NXP Semiconductors 

Hardware Security Engine (HSE_B) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/035_Hardware_Security_Engine_-HSE_B-/S32K3XXRM_数据表.pdf-1057-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R APP_CORE_ACC  Reserved<br>W<br>Reset 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved<br>FIRC_DIV_SEL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-29|FIRC Divider|
|APP_CORE_A<br>CC|While writing to this register, APP_CORE_ACC is RO and should not be changed<br>from 0b101.<br>~~NOTE~~|
||101b - Application core can write this field [FIRC_DIV_SEL]<br>All other values - No access to application core|
|28-2<br>—|Reserved|
|1-0|FIRC Divider|
|FIRC_DIV_SEL|Indicates this chip's FIRC clock division factor.<br>00b - Divided by 2|
||01b - Divided by 2|
||10b - Divided by 16|
||11b - Undivided|



### 35.6.14 QuadSPI SFP Control (QSPI_SFP_CTRL) 

##### Offset 

|Register|Offset|
|---|---|
|QSPI_SFP_CTRL|C0h|



Function 

Resets on functional reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1057 / 4640 

NXP Semiconductors 

Hardware Security Engine (HSE_B) 

~~<mark>NOTE</mark>~~ 

This register is applicable for S32K358 only. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/035_Hardware_Security_Engine_-HSE_B-/S32K3XXRM_数据表.pdf-1058-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>HARD SOFT_ GMID_ DXAC<br>R 0 VLD<br>_LO... LO... VLD  P<br>W<br>Reset<br>u u u u u u u u u u u u u u u u<br>1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DXACP  ADDRESS_SIZE  GMID<br>W<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

1. The default reset value of this register varies on the part basis, depending on NXP factory configurations. 

##### Fields 

|Field|Function|
|---|---|
|31|Hard Lock|
|HARD_LOCK|This is a sticky field. If you write 1 to it, it remains 1 until next reset.<br>0b - Write access is allowed<br>1b - Write access is not allowed until next functional reset|
|30<br>SOFT_LOCK|Soft Lock<br>0b - Write access is allowed<br>1b - Write access is not allowed|
|29-19<br>—<br>18<br>VLD|Reserved<br>Valid<br>This bit indicates if the fields (apart from GMID) are valid or invalid.<br>0b - Fields are invalid<br>1b - Fields are valid|
|17|GMID Valid|
|GMID_VLD|This bit indicates if the GMID field is valid or invalid.<br>0b - GMID field is invalid|
||1b - GMID field is valid|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1058 / 4640 

NXP Semiconductors 

Hardware Security Engine (HSE_B) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|16-14|Domain Access Control Policy|
|DXACP|0xxb - SecPriv: RD; SecUser: RD; NonSecPriv: RD; NonSecUser: RD<br>100b - SecPriv: RW; SecUser: RW; NonSecPriv: RD; NonSecUser: RD<br>101b - SecPriv: RW; SecUser: RD; NonSecPriv: RD; NonSecUser: RD<br>110b - SecPriv: RW; SecUser: RW; NonSecPriv: RW; NonSecUser: RW<br>111b - SecPriv: RW; SecUser: RW; NonSecPriv: RW; NonSecUser: RD|
|13-6|Address Size|
|ADDRESS_SIZ<br>E|The Flash protection address aize (in multiples of 256Bytes)<br>00000000b - 256 bytes<br>00000001b - 512 bytes<br>00000010b - 1024 bytes<br>...<br>11111111b - 64 Kbytes|
|5-0|GMID value|
|GMID|Global Master ID Value|



### 35.6.15 QuadSPI SFP Control Alternate (QSPI_SFP_CTRL_ALT) 

##### Offset 

|Register|Offset|
|---|---|
|QSPI_SFP_CTRL_ALT|C4h|



##### Function 

Resets on functional reset. 

~~<mark>NOTE</mark>~~ 

The values of QSPI_SFT_CTRL_ALT must be bitwise invert of QuadSPI SFP Control (QSPI_SFP_CTRL). If not, the default value of QSPI_SFP_CTRL would be used and the configured values would have no impact. 

~~<mark>NOTE</mark>~~ 

This register is applicable for S32K358 only. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1059 / 4640 

NXP Semiconductors 

Hardware Security Engine (HSE_B) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/035_Hardware_Security_Engine_-HSE_B-/S32K3XXRM_数据表.pdf-1060-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R INVERT_QSPI_SFP_TRL<br>W<br>Reset<br>u u u u u u u u u u u u u u u u<br>1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R INVERT_QSPI_SFP_TRL<br>W<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

1. The default reset value of this register varies on the part basis, depending on NXP factory configurations. 

##### Fields 

|Field|Function|
|---|---|
|31-0|Inverted value of QSPI_SFP_CTRL|
|INVERT_QSPI_|Write inverted value ofQuadSPI SFP Control (QSPI_SFP_CTRL).|
|SFP_TRL||



## 35.7 Glossary 

ADK/P Application debug key/password AES Advanced encryption standard CBC Cipher block chaining CCM Counter with CBC MAC (Cipher block chaining message authentication code) CFB Cipher feedback mode CMAC Cipher-based message authentication code CTR Counter-based block cipher mode CVC Card verifiable certificates Classic DH Classical Diffie–Hellman, a key exchange method DRBG Deterministic random bit generator ECB Electronic code book ECC Elliptic curve cryptography ECDSA Elliptic curve digital signature algorithm ECDH Elliptic-curve Diffie–Hellman, a key exchange method EdDSA Edwards-curve digital signature algorithm FIPS Federal information processing standards MUA Messaging unit A interface 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1060 / 4640 

NXP Semiconductors 

Hardware Security Engine (HSE_B) 

|MUB|Messaging unit B interface|
|---|---|
|NIST|National institute of standards and technology|
|OAEP|Optimal asymmetric encryption padding|
|OFB|Output feedback based block cipher mode|
|GCM|Galois/counter mode|
|GMAC|Galois message authentication code|
|HMAC|Keyed-hash message authentication code|
|PKC|Public key cryptographic engine|
|PKCS1|Public-key cryptography standards. PKCS provides the basic definitions of, and recommendations for<br>implementing the RSA algorithm.|
|POR|Power-on reset|
|RNG|Random number generator|
|RSA|Rivest–Shamir–Adleman (a public key cryptosystem)|
|SHE|Secure hardware extension|
|TRNG|True random number generator|
|XCBC-MAC|Extended ciphertext block chaining MAC|
|XTS|XEX (XOR encrypt XOR) based tweaked-codebook mode with ciphertext stealing|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1061 / 4640 

