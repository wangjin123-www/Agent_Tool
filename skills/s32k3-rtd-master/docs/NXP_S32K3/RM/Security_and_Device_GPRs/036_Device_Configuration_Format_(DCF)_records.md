NXP Semiconductors 

# Chapter 36 Device Configuration Format (DCF) records 

## 36.1 Introduction 

DCF configures certain registers of this chip during system boot while the reset signal asserts. An individual DCF record points to an internal register in the chip and the data to be written to that register. 

UTEST DCF—The UTEST DCF clients are present within the UTEST region of the flash and programmed during production testing. You may write the other records and program them at the same time the application code is programmed in the flash memory. See the DCF client file attached to this document for the description on the UTEST DCF records. 

System boot is a complex process that requires you to initialize the chip properly before releasing reset. Before using the chip, you must write the user application code and the DCF records into their respective flash memory. 

After power is supplied to an appropriately configured chip, PMC controls the chip, and after the system power supplies reach predefined levels, PMC signals MC_RCM to start the boot sequence. During this sequence, MC_RGM enables DCM to read the chip configuration records and then write the configuration information to the specified registers. 

## 36.2 DCF clients 

These are 32-bit wide hardware registers inside a module that receive and store data from a DCF record. This stored data is used to initialize registers and configure features. 

DCF clients: 

- Are assigned a default value before any DCF records are written. 

- May have special writing constraints, such as: 

   - Write once. 

   - Change from 1 to 0 only. 

   - Change from 0 to 1 only. 

- May not implement all 32 bits. 

### 36.2.1 Safety features of DCF clients 

Depending on the DCF client's role in the chip, the client may be equipped with a safety feature or a combination of these features. 

#### 36.2.1.1 Parity 

If a DCF client implements parity checking, the client receives a parity bit in addition to its data in the DCF record. During chip operation, the client continuously monitors whether the data it stores matches the parity. It also reports errors to DCM in case of discrepancies. 

#### 36.2.1.2 Triple voting 

DCF clients that use triple voting have three copies of the register. DCM writes to all the three registers in a single write cycle. During chip operation, the DCF client continuously monitors whether all these three copies match. In case of discrepancies, the client reports errors to DCM. The chip uses the majority result, so single errors do not affect the chip's operation. 

### 36.2.2 DCF client modification rules 

Depending on its role in the chip, a DCF client may implement one or a combination of modification rules. If a modification rule is in effect, the order in which DCF records are placed in the record list may be important. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1062 / 4640 

NXP Semiconductors 

Device Configuration Format (DCF) records 

#### 36.2.2.1 Write once 

A DCF client using the write once rule can only be written with a single DCF record. The records that are appended later in the list are ignored and do not change the value of the client. 

#### 36.2.2.2 Write 0 only 

A field in a DCF client can only be changed from 1 to 0. Therefore, if the value of a field in the previous DCF record is 0, an attempt by a later record to write 1 to it is ignored. 

#### 36.2.2.3 Write 1 only 

A field in a DCF client can only be changed from 0 to 1. Therefore, if the value of a field in the previous DCF record is 1, an attempt by a later record to write 0 to the field is ignored. 

## 36.3 DCF record structure 

A DCF record is a double-word (64-bit) entry that consists of the following: 

- Control word—This provides information to locate the corresponding DCF client internal to the chip (pointer to the location of a register internal to the chip). 

- Data word—This contains the data to be written to the DCF client. 

DCF records select the target DCF client using a 30-bit field in the DCF record that consists of a 15-bit chip select field and a 15-bit address field. All modules that include DCF clients are assigned a chip select during chip definition. The address field is only relevant for address decoding within that module and may not necessarily relate to the address of a register that is visible to you. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/036_Device_Configuration_Format_-DCF-_records/S32K3XXRM_数据表.pdf-1063-13.png)


<!-- Start of picture text -->
Offset 0h 1h 2h 3h<br>Bit number 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31<br>Data[0:31]<br>Offset 4h 5h 6h 7h<br>Bit number 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63<br>C C C C C C C C C C C C C C C<br>S S S S S S S S S S S S S S S Address[16:2] Parity Stop<br>14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br><!-- End of picture text -->

Figure 139. DCF record structure 

##### Table 193. DCF record field descriptions 

|Field|Name|Description|
|---|---|---|
|0-31|Data[0:31]|Provides the data that is to be written to the DCF client.|
|32-46|CSn|Indicates chip select n.|
|||The value 1 is written to a chip select per DCF record to select the target module for the<br>DCF client. The value 0 must be written to all other chip selects.|
|47-61|Address[16:2]|Contains the address of the DCF client within the selected module.<br>Address decoding for DCF clients may not match the standard software address map<br>decoding. For details, see the DCF client addresses provided with each module.|
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1063 / 4640 

NXP Semiconductors 

Device Configuration Format (DCF) records 

Table 193. DCF record field descriptions (continued) 

|Field|Name|Description|
|---|---|---|
|62|Parity|Indicates parity for the DCF record.|
|63|Stop|Indicates the end of the list for DCF records.<br>0 – Not the end<br>1 – End|
|||The erased state of flash memory is FFFF_FFFF_FFFF_FFFFh. Therefore, the list ends<br>with the first unprogrammed double word.<br>This location can be programmed with a new record to extend the list.|



## 36.4 DCF records sequence 

An individual DCF record contains information to locate the corresponding DCF client internal to the chip (control word) and the data to be written to that client (data word). 

DCF records appear as contiguous series of entries programmed at a specific address within flash memory, and must present the following pattern: 

- The first DCF record must be a start record. This record must be placed at the beginning of a DCF area in flash memory to indicate to the chip that the specified records must be processed. 

- DCF records containing configuration data must immediately follow the start record with no blank records in between. An unprogrammed record is interpreted as a stop record and no DCF records following that are processed. This allows you to program the records in several sessions, appending new records at the end of the list each time. 

- The presence of a stop record indicates the end of configuration records. It is not recommended to set valid UTEST DCF record programmed during production because that prevents appending additional UTEST records. The flash memory location following the last UTEST DCF record programmed at the factory is an unprogrammed location, which has FFFF_FFFFh as its content. Thus, the stop bit location in this unprogrammed flash memory location is logic 1, signifying that this is the last DCF record and it is not to be acted upon. 

Table 194 shows the record that DCM recognizes as a start record. 

Table 194. DCF start record 

|0h (0:31)|4h (32:63)|
|---|---|
|05AA_55AFh|0000_0000h|



The factory sets the start bit at the beginning of the UTEST flash memory area. 

Table 195 shows the record that DCM recognizes as a stop record. 

Table 195. DCF stop record 

|0:31|32:62|63|
|---|---|---|
|Ignored|Ignored|1|



The DCF records that you supply may be added in a contiguous manner immediately following the factory-written DCF records. You must never have an unprogrammed record in the series of DCF records because that is interpreted as a stop record. 

Table 196 shows the series of DCF records when n data records are stored in the UTEST flash memory. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1064 / 4640 

NXP Semiconductors 

Device Configuration Format (DCF) records 

Table 196. Series of DCF records in UTEST flash memory 

|Record type|Address offset||Data||
|---|---|---|---|---|
|Start|0h||05AA_55AFh||
||4h||0000_0000h|STOP = 0|
|Data|8h||WDATA[31:0]||
||Ch|CS[14:0]|ADDR[16:2]<br>Parity|STOP = 0|
||10h||WDATA[31:0]||
||14h|CS[14:0]|ADDR[16:2]<br>Parity|STOP = 0|
||...||...||
|Stop|8(n-1) + 0h||Reserved||
||8(n-1) + 4h||Reserved|1|
||8n + 0h<br>8n + 4h||||



More than one DCF records can write to the same DCF client. In this case, the later record usually overrides a DCF client value defined by a previous record. However, not all DCF clients allow overwrites; this depends on individual implementation of DCF clients. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/036_Device_Configuration_Format_-DCF-_records/S32K3XXRM_数据表.pdf-1065-05.png)


<!-- Start of picture text -->
No start record Start record Start record<br>No start record Data record - CS1, Ad = 0 Data record - CS0, Ad = 0<br>No start record Data record - CS2, Ad = 0 Data record - CS1, Ad = 0<br>Ov erw rite<br>No start record Data record - CS0, Ad = 0 Data record - CS2, Ad = 0<br>No start record Stop record Data record - CS0, Ad = 0<br>Stop record<br>Empty flash memory Initial programming<br>- no action Extension<br>Figure 140. Appending DCF records<br><!-- End of picture text -->

## 36.5 Chip configuration records 

The DCF clients table contains information on DCF clients available in the chip. See the DCF clients file attached to this document. 

The next table shows an example of how the information in this chapter is integrated with the attached DCF file. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1065 / 4640 

NXP Semiconductors 

Device Configuration Format (DCF) records 

Table 197. Integration of DCF information 

|Type|Data(n)<br>assuming<br>Quad page<br>program|Data|Comment|
|---|---|---|---|
|Reset pad dedicated control<br>|Data0|0000_0001h|Data to enable pad as dedicated reset pad|
|DCF client|Data1|00_10_0008h|Chip Select is 3 and address is 8,<br>0010_0000h+ 8h|



## 36.6 Glossary 

BIST Built-in self-test OTP One time programmable UTEST User test. Refers to UTEST region of the flash. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1066 / 4640 

