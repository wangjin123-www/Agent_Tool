NXP Semiconductors 

# Chapter 38 Device Configuration Module (DCM) 

## 38.1 Introduction 

### 38.1.1 Overview 

DCM controls: 

- LC 

- DCF client population 

- Debug authorization (Export Control mode) 

The module also establishes a RoT for the chip by parsing the master root key and other security records. This figure is a pictorical representation of DCM: 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/038_Device_Configuration_Module_-DCM-/S32K3XXRM_数据表.pdf-1197-09.png)


<!-- Start of picture text -->
PFC<br>uTest sector<br>PFC flash memory Block 0<br>interface<br>DCM<br>Block 1<br>Lifecycle   Lifecycle Flash memoryscanner<br>DCF client<br>bus controller<br>Block 2<br>Block 3<br>SWD/JTAG<br>DCM debug DCM registers<br>interface<br>Block 4<br>Block 5<br><!-- End of picture text -->

Figure 141. DCM block diagram 

### 38.1.2 Features 

- Scans flash memory and configures the system for: 

   - LC detection 

   - DCF records configuration using flash memory 

- Allows debug features for flash memory content and the chip 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1197 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

- Provides debug enable control 

- Provides a valid boot address detection 

- Enables the DCF client to be writable via the IPS bus 

- Parameterizes control to mask a set of DCF client chip select 

- Supports temporary advancement of the LC 

- Controls chip debug enablement 

### 38.1.3 Modes of operation 

DCM operates identically in all system modes of operation. 

## 38.2 Functional description 

DCM provides information about the current state and configuration of the system that you could use to: 

- Configure the application software. 

- Debug the system. 

### 38.2.1 DCF mechanism 

The DCF mechanism handles chip parameter settings via the OTP flash memory. 

You can store a series of DCF records in flash memory, and each record is 64 bits in length. The chip processes these records during the system reset sequence before the CPU leaves reset. 

A DCF record contains: 

- A start record. Placed at UTEST_OFFSET, it indicates to the chip that the specified data records must be processed. See Table 199 that shows a general format of the start record. 

- Application-specific number of data records. These follow the start record, as required. 

- A stop record. Its presence indicates that the processing must stop. See Table 201 for a general format of the stop record. Only the STOP field needs to be 1 to form a stop record—all other fields are ignored. Also, an unprogrammed location in Utest flash memory is interpreted as a stop record. 

#### Table 199. DCF start record 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/038_Device_Configuration_Module_-DCM-/S32K3XXRM_数据表.pdf-1198-22.png)


<!-- Start of picture text -->
05AA 55AFh<br>0000 0000h<br><!-- End of picture text -->

Table 200. DCF stop record 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/038_Device_Configuration_Module_-DCM-/S32K3XXRM_数据表.pdf-1198-24.png)


<!-- Start of picture text -->
Reserved 1<br>Reserved<br><!-- End of picture text -->

A data record is structured in a way similar to a CPU-write instruction—comprising a 15-bit client select field, a 15-bit address field, and a 32-bit payload data field plus a STOP field. See Table 201 for details. 

In a data record, the value of the STOP field must always be 0. Some clients support a parity (PRTY) field too. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1198 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Table 201. Format of a DCF data record 

||WDATA[31:0]||
|---|---|---|
|CS[14:0]|ADDR[16:2]<br>PRTY|STOP|



If n data records are to be stored in Utest, the data structure must be as shown in the next table. 

Table 202. Series of DCF records in Utest 

|Address<br>offset||Data|||
|---|---|---|---|---|
|00h||05AA 55AFh|||
|04h||0000 0000h||STOP = 0|
|08h||WDATA[31:0]|||
|0Ch|CS[14:0]|ADDR[16:2]|PRTY|STOP = 0|
|10h||WDATA[31:0]|||
|14h|CS[14:0]|ADDR[16:2]|PRTY|STOP = 0|
|8n - 1 + 0h||Reserved|||
|8n - 1 + 4h||Reserved||1|
|8n + 0h<br>8n + 4h|||||



An unprogrammed record must not exist in the data structure because that is interpreted as a stop record. This leads to the subsequent records being ignored. In this case: 

- You need to program the records in several sessions, each time appending new records at the end of the list, as shown in the next figure. 

- A record may overwrite a client's value defined by a previous record. However, not all clients allow overwrites— that depends on their individiual implementation. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1199 / 4640 

NXP Semiconductors 

##### Device Configuration Module (DCM) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/038_Device_Configuration_Module_-DCM-/S32K3XXRM_数据表.pdf-1200-02.png)


<!-- Start of picture text -->
No start record Start record Start record<br>No start record Data record - CS1, Ad = 0 Data record - CS0, Ad = 0<br>No start record Data record - CS2, Ad = 0 Data record - CS1, Ad = 0<br>Ov erw rite<br>No start record Data record - CS0, Ad = 0 Data record - CS2, Ad = 0<br>No start record Stop record Data record - CS0, Ad = 0<br>Stop record<br>Empty flash memory Initial programming<br>- no action Extension<br><!-- End of picture text -->

Figure 142. Appending DCF records 

Some of the DCF records require parity bits, and the parity scheme used is even parity. So, the number of 1s in the WDATA and PRTY fields needs to be even. For example, if the WDATA field has the value 0000_0001h, the value of the PRTY field needs to be 1 so that the total number of 1s is even. 

~~<mark>NOTE</mark>~~ 

You must ensure that DCF records are programmed uninterruptedly and the process completes without an error. 

### 38.2.2 DCF error recording 

DCF errors are recorded in DCM for both types of clients—spread spectrum safe and normal. See DCF client error mechanism for details on spread spectrum safe clients. 

### 38.2.3 DCF client error mechanism 

The DCM consists of DCMMISC[DCMCERS] for detecting faulty DCF records. The DCMSRRn registers capture the details up to 16 faulty records. The CERS bit can be cleared by writing 1 to it. 

While scanning the flash, in case if a faulty record is encountered, the DCMMISC[DCMCERS] gets set indicating that there is atleast one faulty record. In such a case, the user can identify the details about the faulty record in the DCMSRRn registers and should update the flash memory with a new record, provided the record is not write-once. 

For example, in the image below, if the faulty DCF record is DCF2, then the correct DCF record must also be DCF2. Even in case if the faulty record is updated, the DCM stores the faulty record via the DCMMISC[CERS] and DCMSRRn registers. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1200 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/038_Device_Configuration_Module_-DCM-/S32K3XXRM_数据表.pdf-1201-02.png)


<!-- Start of picture text -->
Flash memory<br>Original DCF1<br>DCF<br>DCF2<br>DCM<br>DCM error flags IPS interface<br>Faulty DCF2<br>DCF<br>Final Pulse<br>DCF2 DCF1 DCF2<br>DCF wrapper<br><!-- End of picture text -->

Figure 143. DCF error and CERS handling 

### 38.2.4 DCF error detection mechanism 

This figure shows that a faulty DCF record is loaded between the original and final DCF record sets. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1201 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/038_Device_Configuration_Module_-DCM-/S32K3XXRM_数据表.pdf-1202-02.png)


<!-- Start of picture text -->
Flash memory<br>DCF bus<br>Flash memory<br>DCF scanner<br>DCF bus Mux<br>DCF bus<br>Lifecycle & Start record<br>ExportControl DCF client<br>control<br>Utest<br>DCM regs<br>TimeOut/ECC/<br>FlashIntfViol<br>Software control<br>End record<br>Xfr_err/<br>Mem_err/ Error logging<br>31:0 Err bus<br><!-- End of picture text -->

Figure 144. DCF error detection mechanism 

### 38.2.5 LC 

DCM determines the LC of the chip by reading the LC slots from the Utest flash memory. This read operation is performed during the reset phase, with normal timings. The operating monitors and an ECC check protect the operation. Additionally, a set of sanity checks executed over the LC read data guarantee the integrity of the final LC value. 

At the end of the reset phase, the LC contains one of the following values: 

- OEM production (OEM_PROD) 

- In field (IN_FIELD) 

- Pre-FA 

- FA 

The DCM LC progresses in the direction shown in this figure: 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/038_Device_Configuration_Module_-DCM-/S32K3XXRM_数据表.pdf-1202-12.png)


<!-- Start of picture text -->
MCU Customer OEM In field Pre-failure Failure<br>production delivery production analysis analysis<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/038_Device_Configuration_Module_-DCM-/S32K3XXRM_数据表.pdf-1202-13.png)


<!-- Start of picture text -->
Figure 145. LC sequence<br><!-- End of picture text -->

The LC is written into six slots, 128 bits each, and at fixed locations in the Utest flash memory blockblock. Each LC slot is read in a single atomic operation and is organized in two types of fields: 

- Valid 

- Invalid 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1202 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

Depending on the possible combinations of data programmed into these fields, each LC slot indicates one of the four possible statuses as shown in Table 203. To know more about LC slots, see Table 204. 

Table 203. LC slot status 

||LC slots||LC slot value|
|---|---|---|---|
|Valid field (64 bits)||Invalid field (64 bits)||
|Erased||Erased|Erased|
|Marked||Erased|Active|
|Marked||Marked|Inactive|
||Other values||Illegal|



In this case, "Marked" refers to a value that is configured based on the bit pattern 55AA_50AF_55AA_50AFh, and "Erased" is detected using the bit pattern FFFF_FFFF_FFFF_FFFFh. 

Table 204. LC slots 

|LC slot 0<br>MCU_PROD|LC slot 1<br>CUST_DEL|LC slot 2<br>OEM_PROD|LC slot 3<br>IN_FIELD|LC slot 4<br>Pre-FA|LC slot 5<br>FA|Resulting LC|
|---|---|---|---|---|---|---|
|Active|Erased|Erased|Erased|Erased|Erased|MCU_PROD|
|Inactive|Active|Erased|Erased|Erased|Erased|CUST_DEL|
|Inactive|Inactive|Active|Erased|Erased|Erased|OEM_PROD|
|Inactive|Inactive|Inactive|Active|Erased|Erased|IN_FIELD|
|Inactive|Inactive|Inactive|Inactive|Active|Erased|PFA|
|Inactive or<br>Erased|Inactive|Inactive|Inactive|Inactive|Active|FA|
|Erased|Erased|Erased|Erased|Erased|Erased|System reset|
|Illegal<sup>1</sup>|Illegal|Illegal|Illegal|Erased|Erased|IN_FIELD|



1. Values other than the ones specified in this table for Erased, Active, and Inactive are treated as illegal. 

~~<mark>NOTE</mark>~~ 

When triggering DCM for rescanning the software, you must ensure that the flash memory program and erase fields are not set. Otherwise, DCM does not configure the chip and ignores all data returned from the flash memory. This results in LC becoming IN_FIELD. All DCF clients indicate their default values in this case. 

## 38.3 DCM register descriptions 

### 38.3.1 DCM memory map 

DCM base address: 402A_C000h 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1203 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|0h|DCM Status (DCMSTAT)|32|RO|See<br>description|
|4h|LC and LC Control (DCMLCC)|32|RW|See<br>description|
|8h|LC Scan Status (DCMLCS)|32|W1C|0000_0000h|
|1Ch|DCM Miscellaneous (DCMMISC)|32|W1C|0000_0001h|
|20h|Debug Status and Configuration (DCMDEB)|32|RW|0000_0000h|
|2Ch|DCF Error Count (DCMEC)|32|RO|0000_0000h|
|30h|DCF Scan Report (DCMSRR1)|32|W1C|0000_0000h|
|34h|DCF Scan Report (DCMSRR2)|32|W1C|0000_0000h|
|38h|DCF Scan Report (DCMSRR3)|32|W1C|0000_0000h|
|3Ch|DCF Scan Report (DCMSRR4)|32|W1C|0000_0000h|
|40h|DCF Scan Report (DCMSRR5)|32|W1C|0000_0000h|
|44h|DCF Scan Report (DCMSRR6)|32|W1C|0000_0000h|
|48h|DCF Scan Report (DCMSRR7)|32|W1C|0000_0000h|
|4Ch|DCF Scan Report (DCMSRR8)|32|W1C|0000_0000h|
|50h|DCF Scan Report (DCMSRR9)|32|W1C|0000_0000h|
|54h|DCF Scan Report (DCMSRR10)|32|W1C|0000_0000h|
|58h|DCF Scan Report (DCMSRR11)|32|W1C|0000_0000h|
|5Ch|DCF Scan Report (DCMSRR12)|32|W1C|0000_0000h|
|60h|DCF Scan Report (DCMSRR13)|32|W1C|0000_0000h|
|64h|DCF Scan Report (DCMSRR14)|32|W1C|0000_0000h|
|68h|DCF Scan Report (DCMSRR15)|32|W1C|0000_0000h|
|6Ch|DCF Scan Report (DCMSRR16)|32|W1C|0000_0000h|
|80h|LC Scan Status 2 (DCMLCS_2)|32|W1C|0000_0000h|



### 38.3.2 DCM Status (DCMSTAT) 

#### Offset 

|Register|Offset|
|---|---|
|DCMSTAT|0h|



#### Function 

Indicates the status of DCM at different stages. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1204 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

~~<mark>NOTE</mark>~~ 

This register resets on functional reset. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||||||0||||||||0||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||0|||0|DCMD<br>BGPS|DCMO<br>TAS|DCMU<br>TS||0||DCML<br>CST|0||DCME<br>RR|DCMD<br>ONE|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|u<sup>1</sup>|1|0|1|1|1|0|0|0|1|



1. The value of this field is loaded from flash memory based on chip configuration. 

#### Fields 

|Field|Function|
|---|---|
|31-19<br>—|Reserved|
|18-16<br>—|Reserved|
|15-12<br>—|Reserved|
|11<br>—<br>10|Reserved<br>Debug Password Scanning Status|
|DCMDBGPS|Indicates the DCM debug password scanning status.<br>0b - Completed with errors<br>1b - Completed successfully|
|9<br>DCMOTAS|DCM OTA Scanning Status (valid only when the value of the DCMDONE field is 1)<br>0b - Completed with errors<br>1b - Completed successfully|
|8<br>DCMUTS|DCM Utest DCF Scanning Status (valid only if DCMDONE bit is set)|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1205 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||This bit always returns 0 in In Field LC.<br>~~NOTE~~<br>0b - DCM Utest DCF completed with errors.<br>1b - DCM Utest DCF completed successfully.|
|7-5<br>—<br>4<br>DCMLCST|Reserved<br>LC Scanning Status<br>Indicates the DCM LC scanning status.<br>This field is valid only if the value of the DCMDONE field is 1. Also, it always returns 0 in the IN_FIELD phase<br>of the LC. For details, seeLC.<br>0b - Completed with errors<br>1b - Completed successfully|
|3-2<br>—<br>1<br>DCMERR|Reserved<br>DCM completion with error status (valid only if DCMDONE bit is set)<br>0b - DCM completed with success.<br>1b - DCM completed with error.|
|0|DCM Scanning Status|
|DCMDONE|Indicates whether the DCM scanning is in progress or complete.<br>0b - Running<br>1b - Completed|



### 38.3.3 LC and LC Control (DCMLCC) 

#### Offset 

|Register|Offset|
|---|---|
|DCMLCC|4h|



Function 

Resets on the functional reset. 

~~<mark>NOTE</mark>~~ 

The DCMLCFN and DCMFLC fields of this register reset on destructive reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1206 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/038_Device_Configuration_Module_-DCM-/S32K3XXRM_数据表.pdf-1207-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset<br>0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 DCMRLC  DCMCLC<br>DCML<br>DCMFLC<br>W CFN<br>Reset 0 0 0 0 0 0 0 0 0 u u u 0 u u u<br><!-- End of picture text -->

1. Post reset, the reset value of this register is 0000_0077h, and after scanning, it changes according to the programmed value. 

#### Fields 

|Field|Function|
|---|---|
|31-10<br>—|Reserved|
|9-8|Force Next LC|
|DCMFLC|Provides provisions for a temporary LC update.<br>LC can be temporarily forced as follows:<br>• MCU_PROD => Force one => CUST_DEL (CD)<br>• CUST_DEL => Force one => OEM_PROD<br>• CUST_DEL => Force two => IN_FIELD<br>• OEM_PROD => Force one => IN_FIELD<br>• IN_FIELD => Force not allowed to move LC<br>• Pre-FA => Force not allowed to move LC<br>• FA => Force not allowed to move LC<br>00b - No force<br>01b - Force LC to one next<br>10b - Force LC to two next (only possible in CD)<br>11b - Reserved (no effect)|
|7<br>—|Reserved|
|6-4|Real LC|
|DCMRLC|Projects the real LC of the chip.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1207 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||The LC can move in this sequence: (110 : MCU_PROD) > (011 : CUST_DEL) > (010 : OEM_PROD) > (111 :<br>IN_FIELD) > (001 : Pre-FA) > (000 : FA)<br>000b - FA<br>001b - Pre-FA<br>010b - OEM_PROD<br>011b - CUST_DEL<br>100b - Reserved<br>101b - Reserved<br>110b - MCU_PROD<br>111b - IN_FIELD|
|3<br>DCMLCFN|Force LC<br>Indicates if the LC is normal or forced on the current LC.<br>If the value of this field is 1, the value configured according to the DCMLCF register is forced on the current<br>LC whereas the real LC remains the same.<br>0b - Normal<br>1b - Forced on current LC|
|2-0<br>DCMCLC|Current LC<br>Projects the current LC of the chip.<br>The LC can move in this sequence: (110 : MCU_PROD) > (011 : CUST_DEL) > (010 : OEM_PROD) > (111 :<br>IN_FIELD) > (001 : Pre-FA) > (000 : FA)<br>000b - FA<br>001b - Pre-FA<br>010b - OEM_PROD<br>011b - CUST_DEL<br>100b - Reserved<br>101b - Reserved<br>110b - MCU_PROD<br>111b - IN_FIELD|



### 38.3.4 LC Scan Status (DCMLCS) 

#### Offset 

|Register|Offset|
|---|---|
|DCMLCS|8h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1208 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Function 

Stores the status of LC scanning. By default, the status of each LC is "not yet scanned." 

This register: 

- Resets on destructive reset. 

- Always returns 0 in a valid IN_FIELD LC (in LC without an error). 

This register captures the errors related to LC scanning on each of these resets: POR, destructive, and functional. If an error is captured, its status in this register is cleared by writing 1 to the corresponding field or to any of the destructive or POR events. 

All LC slot errors are captured and cleared independently. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||0|DCML<br>CFE5|DCML<br>CE5||DCMLCC5||DCML<br>CSS5|DCML<br>CFE4|DCML<br>CE4||DCMLCC4||DCML<br>CSS4|DCML<br>CFE3|DCML<br>CE3|
|W|||W1C|W1C||W1C||W1C|W1C|W1C||W1C||W1C|W1C|W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||DCMLCC|3|DCML<br>CSS3|DCML<br>CFE2|DCML<br>CE2||DCMLCC|2|DCML<br>CSS2|DCML<br>CFE1|DCML<br>CE1||DCMLCC|1|DCML<br>CSS1|
|W||W1C||W1C|W1C|W1C||W1C||W1C|W1C|W1C||W1C||W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-30|Reserved|
|—<br>29|Pre-FA Flash Memory Error Check|
|DCMLCFE5|Indicates the status of the Pre-FA flash memory error check.<br>0b - Successful<br>1b - Failed|
|28|Pre-FA ECC Errors|
|DCMLCE5|Indicates if Pre-FA is successful or has ECC errors.<br>0b - No errors<br>1b - Marking error|
|27-25|Pre-FA Marking Status|
|DCMLCC5|Indicates the Pre-FA marking status.<br>These errors may cause this field to indicate the "not scanned yet" status:|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1209 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

Table continued from the previous page... 

|Field|Function<br>• If the reading completes too early and DCM has not yet scanned the LC.<br>• If there is an error in the flash memory after completion of the reading.<br>000b - Not scanned yet<br>001b - Marked as active<br>010b - Marked as inactive<br>011b - Region is erased/virgin<br>101b - Marked as inactive by an unknown pattern<br>110b - Scanning timed out|
|---|---|
|24<br>DCMLCSS5|Pre-FA Scan Status<br>Indicates the status of the Pre-FA scan.<br>0b - Successful<br>1b - Errors exist|
|23<br>DCMLCFE4|IN_FIELD Flash Memory Error Check<br>Indicates the status of IN_FIELD flash memory error check.<br>0b - Successful<br>1b - Failed|
|22<br>DCMLCE4|IN_FIELD ECC Errors<br>Indicates if IN_FIELD has ECC errors.<br>0b - No errors<br>1b - Errors exist|
|21-19<br>DCMLCC4|IN_FIELD Marking Status<br>Indicates the IN_FIELD marking status.<br>These errors may cause this field to indicate the "not scanned yet" status:<br>• If the reading completes too early and DCM has not yet scanned the LC.<br>• If there is an error in the flash memory after completion of the reading.<br>000b - Not scanned yet<br>001b - Marked as active<br>010b - Marked as inactive<br>011b - Region is erased/virgin<br>101b - Marked as inactive by an unknown pattern<br>110b - Scanning timed out|
|18|IN_FIELD Scan Status|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1210 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|DCMLCSS4|Indicates the status of the IN_FIELD scan.<br>0b - No errors<br>1b - Errors exist|
|17<br>DCMLCFE3|OEM_PROD Flash Memory Error Check<br>Indicates the status of the OEM_PROD flash memory error check.<br>0b - Successful<br>1b - Failed|
|16<br>DCMLCE3|OEM_PROD ECC Errors<br>Indicates if OEM_PROD has ECC errors.<br>0b - No errors<br>1b - Errors exist|
|15-13<br>DCMLCC3|OEM_PROD Marking<br>Indicates the OEM_PROD marking status.<br>These errors may cause this field to indicate the "not scanned yet" status:<br>• If the reading completes too early and DCM has not yet scanned the LC.<br>• If there is an error in the flash memory after completion of the reading.<br>000b - Not scanned yet<br>001b - Marked as active<br>010b - Marked as inactive<br>011b - Region is erased/virgin<br>101b - Marked as inactive by an unknown pattern<br>110b - Scanning timed out|
|12<br>DCMLCSS3|OEM_PROD Scan Status<br>Indicates the status of OEM_PROD scan.<br>0b - No errors<br>1b - Errors exist|
|11<br>DCMLCFE2|CUST_DEL Flash Memory Error Check<br>Indicates the status of CUST_DEL flash memory error check.<br>0b - Successful<br>1b - Failed|
|10|ECC Errors In CUST_DEL|
|DCMLCE2|Indicates if CUST_DEL has ECC errors.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1211 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - No errors<br>1b - Errors exist|
|9-7<br>DCMLCC2|CUST_DEL Marking<br>Indicates the CUST_DEL marking status.<br>These errors may cause this field to indicate the "not scanned yet" status:<br>• If the reading completes too early and DCM has not yet scanned the LC.<br>• If there is an error in the flash memory after completion of the reading.<br>000b - Not scanned yet<br>001b - Marked as active<br>010b - Marked as inactive<br>011b - Region is erased/virgin<br>101b - Marked as inactive by an unknown pattern<br>110b - Scanning timed out|
|6<br>DCMLCSS2|CUST_DEL Scan Status<br>Indicates the status of the CUST_DEL scan.<br>0b - No errors<br>1b - Errors exist|
|5|MCU_PROD Flash Memory Error Check|
|DCMLCFE1|Indicates the status of flash memory error check.<br>0b - Successful<br>1b - Failed|
|4<br>DCMLCE1|MCU_PROD ECC Errors<br>Indicates if MCU_PROD has ECC errors.<br>0b - No errors<br>1b - Errors exist|
|3-1<br>DCMLCC1|MCU_PROD Marking<br>Indicates the MCU_PROD marking status.<br>These errors may cause this field to indicate the "not scanned yet" status:<br>• If the reading completes too early and DCM has not yet scanned the LC.<br>• If there is an error in the flash memory after completion of the reading.<br>000b - Not scanned yet|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1212 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||001b - Marked as active|
||010b - Marked as inactive<br>011b - Region is erased/virgin<br>101b - Marked as inactive by an unknown pattern|
||110b - Scanning timed out|
|0|MCU_PROD Scan Status|
|DCMLCSS1|Indicates the MCU_PROD scan status.|
||0b - No errors|
||1b - Errors exist|



### 38.3.5 DCM Miscellaneous (DCMMISC) 

#### Offset 

|Register|Offset|
|---|---|
|DCMMISC|1Ch|



#### Function 

#### Resets on destructive reset. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/038_Device_Configuration_Module_-DCM-/S32K3XXRM_数据表.pdf-1213-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>DCMC<br>R 0 0 0 0 0<br>ERS<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>DCMD DCMD<br>R 0 0 0<br>BGE  BGT<br>W W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1<br><!-- End of picture text -->

Fields 

|Field<br>Function|
|---|
|31<br>Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1213 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

Table continued from the previous page... 

|Field<br>—|Function|
|---|---|
|30<br>—|Reserved|
|29<br>—|Reserved|
|28<br>DCMCERS|DCF Client Errors<br>Records the status of errors from DCF clients.<br>0b - No errors on any of the DCF clients<br>1b - Atleast one safety DCF client has an error|
|27-24<br>—<br>23-14<br>—<br>13-12<br>—<br>11<br>DCMDBGE|Reserved<br>Reserved<br>Reserved<br>DCM ECC error on DBG sections<br>This bit is set if there is any ECC error during scanning of NXP_PWD, CUST_PWD, or UID.<br>0b - No error on DBG section<br>1b - DBG section error|
|10<br>DCMDBGT|DBG Section Error<br>Indicates if there is a DCM flash memory timeout error in DBG sections. The value of this field is 1 in<br>case a timeout error occurs when scanning NXP_PWD, CUST_PWD, or UID.<br>0b - No error<br>1b - Error exists|
|9-0<br>—|Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1214 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

### 38.3.6 Debug Status and Configuration (DCMDEB) 

#### Offset 

|Register|Offset|
|---|---|
|DCMDEB|20h|



#### Function 

#### Resets on destructive reset. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/038_Device_Configuration_Module_-DCM-/S32K3XXRM_数据表.pdf-1215-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>APPD<br>R 0<br>BG_...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>DCM_<br>R 0 0 0 0 0 0 0 0 0<br>APP...<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-17<br>—|Reserved|
|16|Application Debug Status|
|APPDBG_STAT<br>_SOC|Indicates the application debug status of the chip.<br>0b - Disabled<br>1b - Enabled|
|15<br>—|Reserved|
|14<br>—|Reserved|
|13<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1215 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|12<br>—|Reserved|
|11-10<br>—|Reserved|
|9<br>—<br>8<br>—|Reserved<br>Reserved|
|7-6<br>—<br>5-2<br>—<br>1<br>DCM_APPDBG<br>_STAT|Reserved<br>Reserved<br>DCM Authentication Engine Status<br>Indicates the DCM authentication engine status for the application core.<br>This value of this field is 0 in Non-Export Control mode.<br>~~NOTE~~|
||0b - Disabled<br>1b - Enabled|
|0<br>—|Reserved|



### 38.3.7 DCF Error Count (DCMEC) 

#### Offset 

|Register|Offset|
|---|---|
|DCMEC|2Ch|



#### Function 

Indicates the display count for the number of errors encountered when scanning the flash memory during DCF scanning. This register resets on destructive reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1216 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||DCM|ECT||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-16|Reserved|
|—||
|15-0|Error Count|
|DCMECT|Indicates the display count for the number of errors encountered when scanning the flash memory during<br>DCF scanning.|



### 38.3.8 DCF Scan Report (DCMSRR1) 

#### Offset 

|Register|Offset|
|---|---|
|DCMSRR1|30h|



#### Function 

#### Resets on destructive reset. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|0||DCMD<br>CFT1|DCME<br>SD1|DCME<br>SF1|D|CMDCFF|1||0|||D|CMDCFE1|||
|W|||W1C|W1C|W1C||W1C|||||||W1C|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||DCMD|CFE1||||||||
|W||||||||W1|C||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1217 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Fields 

|Field|Function|
|---|---|
|31-30|Reserved|
|—||
|29<br>DCMDCFT1|Scanning Timeout On Flash Memory<br>Indicates if scanning timeout exists on flash memory address.<br>0b - Does not exist<br>1b - Exists|
|28<br>DCMESD1|Chip Side Error<br>Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the<br>DCF client, such as write-once error.<br>0b - No errors<br>1b - Errors exist|
|27<br>DCMESF1|Flash Memory Error<br>Indicates if a flash memory error exists.<br>0b - No errors<br>1b - Errors exist|
|26-24|DCF Record Location|
|DCMDCFF1|Indicates the DCF record location in flash memory.<br>010b - Utest region<br>101b - Others: Reserved|
|23-21<br>—|Reserved|
|20-0|Flash Memory Address|
|DCMDCFE1|Indicates the flash memory address of the DCF client having an error.|



### 38.3.9 DCF Scan Report (DCMSRR2) 

#### Offset 

|Register|Offset|
|---|---|
|DCMSRR2|34h|



Function Resets on destructive reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1218 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|0||DCMD<br>CFT2|DCME<br>SD2|DCME<br>SF2|D|CMDCFF|2||0|||D|CMDCFE2|||
|W|||W1C|W1C|W1C||W1C|||||||W1C|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||DCMD|CFE2||||||||
|W||||||||W1|C||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29<br>DCMDCFT2|Scanning Timeout On Flash Memory<br>Indicates if scanning timeout exists on flash memory address.<br>0b - Does not exist<br>1b - Exists|
|28<br>DCMESD2|Chip Side Error<br>Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the<br>DCF client, such as write-once error.<br>0b - No errors<br>1b - Errors exist|
|27<br>DCMESF2|Flash Memory Error<br>Indicates if a flash memory error exists.<br>0b - No errors<br>1b - Errors exist|
|26-24<br>DCMDCFF2|DCF Record Location<br>Indicates the DCF record location in flash memory.<br>010b - Utest region<br>101b - Others: Reserved|
|23-21<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1219 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|20-0|Flash Memory Address|
|DCMDCFE2|Indicates the flash memory address of the DCF client having an error.|



### 38.3.10 DCF Scan Report (DCMSRR3) 

#### Offset 

|Register|Offset|
|---|---|
|DCMSRR3|38h|



#### Function 

Resets on destructive reset. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/038_Device_Configuration_Module_-DCM-/S32K3XXRM_数据表.pdf-1220-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>DCMD DCME DCME<br>R 0 DCMDCFF3  0 DCMDCFE3<br>CFT3  SD3  SF3<br>W W1C W1C W1C W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DCMDCFE3<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29|Scanning Timeout On Flash Memory|
|DCMDCFT3|Indicates if scanning timeout exists on flash memory address.|
||0b - Does not exist|
||1b - Exists|
|28|Chip Side Error|
|DCMESD3||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1220 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the<br>DCF client, such as write-once error.<br>0b - No errors<br>1b - Errors exist|
|27<br>DCMESF3|Flash Memory Error<br>Indicates if a flash memory error exists.<br>0b - No errors<br>1b - Errors exist|
|26-24|DCF Record Location|
|DCMDCFF3|Indicates the DCF record location in flash memory.<br>010b - Utest region<br>101b - Others: Reserved|
|23-21<br>—|Reserved|
|20-0|Flash Memory Address|
|DCMDCFE3|Indicates the flash memory address of the DCF client having an error.|



### 38.3.11 DCF Scan Report (DCMSRR4) 

#### Offset 

|Register|Offset|
|---|---|
|DCMSRR4|3Ch|



Function Resets on destructive reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1221 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|0||DCMD<br>CFT4|DCME<br>SD4|DCME<br>SF4|D|CMDCFF|4||0|||D|CMDCFE4|||
|W|||W1C|W1C|W1C||W1C|||||||W1C|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||DCMD|CFE4||||||||
|W||||||||W1|C||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29<br>DCMDCFT4|Scanning Timeout On Flash Memory<br>Indicates if scanning timeout exists on flash memory address.<br>0b - Does not exist<br>1b - Exists|
|28<br>DCMESD4|Chip Side Error<br>Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the<br>DCF client, such as write-once error.<br>0b - No errors<br>1b - Errors exist|
|27<br>DCMESF4|Flash Memory Error<br>Indicates if a flash memory error exists.<br>0b - No errors<br>1b - Errors exist|
|26-24<br>DCMDCFF4|DCF Record Location<br>Indicates the DCF record location in flash memory.<br>010b - Utest region<br>101b - Others: Reserved|
|23-21<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1222 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|20-0|Flash Memory Address|
|DCMDCFE4|Indicates the flash memory address of the DCF client having an error.|



### 38.3.12 DCF Scan Report (DCMSRR5) 

#### Offset 

|Register|Offset|
|---|---|
|DCMSRR5|40h|



#### Function 

Resets on destructive reset. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/038_Device_Configuration_Module_-DCM-/S32K3XXRM_数据表.pdf-1223-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>DCMD DCME DCME<br>R 0 DCMDCFF5  0 DCMDCFE5<br>CFT5  SD5  SF5<br>W W1C W1C W1C W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DCMDCFE5<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29|Scanning Timeout On Flash Memory|
|DCMDCFT5|Indicates if scanning timeout exists on flash memory address.|
||0b - Does not exist|
||1b - Exists|
|28|Chip Side Error|
|DCMESD5||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1223 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the<br>DCF client, such as write-once error.<br>0b - No errors<br>1b - Errors exist|
|27<br>DCMESF5|Flash Memory Error<br>Indicates if a flash memory error exists.<br>0b - No errors<br>1b - Errors exist|
|26-24|DCF Record Location|
|DCMDCFF5|Indicates the DCF record location in flash memory.<br>010b - Utest region<br>101b - Others: Reserved|
|23-21<br>—|Reserved|
|20-0|Flash Memory Address|
|DCMDCFE5|Indicates the flash memory address of the DCF client having an error.|



### 38.3.13 DCF Scan Report (DCMSRR6) 

#### Offset 

|Register|Offset|
|---|---|
|DCMSRR6|44h|



Function 

Resets on destructive reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1224 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|0||DCMD<br>CFT6|DCME<br>SD6|DCME<br>SF6|D|CMDCFF|6||0|||D|CMDCFE6|||
|W|||W1C|W1C|W1C||W1C|||||||W1C|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||DCMD|CFE6||||||||
|W||||||||W1|C||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29<br>DCMDCFT6|Scanning Timeout On Flash Memory<br>Indicates if scanning timeout exists on flash memory address.<br>0b - Does not exist<br>1b - Exists|
|28<br>DCMESD6|Chip Side Error<br>Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the<br>DCF client, such as write-once error.<br>0b - No errors<br>1b - Errors exist|
|27<br>DCMESF6|Flash Memory Error<br>Indicates if a flash memory error exists.<br>0b - No errors<br>1b - Errors exist|
|26-24<br>DCMDCFF6|DCF Record Location<br>Indicates the DCF record location in flash memory.<br>010b - Utest region<br>101b - Others: Reserved|
|23-21<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1225 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|20-0|Flash Memory Address|
|DCMDCFE6|Indicates the flash memory address of the DCF client having an error.|



### 38.3.14 DCF Scan Report (DCMSRR7) 

#### Offset 

|Register|Offset|
|---|---|
|DCMSRR7|48h|



#### Function 

Resets on destructive reset. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/038_Device_Configuration_Module_-DCM-/S32K3XXRM_数据表.pdf-1226-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>DCMD DCME DCME<br>R 0 DCMDCFF7  0 DCMDCFE7<br>CFT7  SD7  SF7<br>W W1C W1C W1C W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DCMDCFE7<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29|Scanning Timeout On Flash Memory|
|DCMDCFT7|Indicates if scanning timeout exists on flash memory address.|
||0b - Does not exist|
||1b - Exists|
|28|Chip Side Error|
|DCMESD7||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1226 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the<br>DCF client, such as write-once error.<br>0b - No errors<br>1b - Errors exist|
|27<br>DCMESF7|Flash Memory Error<br>Indicates if a flash memory error exists.<br>0b - No errors<br>1b - Errors exist|
|26-24|DCF Record Location|
|DCMDCFF7|Indicates the DCF record location in flash memory.<br>010b - Utest region<br>101b - Others: Reserved|
|23-21<br>—|Reserved|
|20-0|Flash Memory Address|
|DCMDCFE7|Indicates the flash memory address of the DCF client having an error.|



### 38.3.15 DCF Scan Report (DCMSRR8) 

#### Offset 

|Register|Offset|
|---|---|
|DCMSRR8|4Ch|



Function 

Resets on destructive reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1227 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|0||DCMD<br>CFT8|DCME<br>SD8|DCME<br>SF8|D|CMDCFF|8||0|||D|CMDCFE8|||
|W|||W1C|W1C|W1C||W1C|||||||W1C|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||DCMD|CFE8||||||||
|W||||||||W1|C||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29<br>DCMDCFT8|Scanning Timeout On Flash Memory<br>Indicates if scanning timeout exists on flash memory address.<br>0b - Does not exist<br>1b - Exists|
|28<br>DCMESD8|Chip Side Error<br>Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the<br>DCF client, such as write-once error.<br>0b - No errors<br>1b - Errors exist|
|27<br>DCMESF8|Flash Memory Error<br>Indicates if a flash memory error exists.<br>0b - No errors<br>1b - Errors exist|
|26-24<br>DCMDCFF8|DCF Record Location<br>Indicates the DCF record location in flash memory.<br>010b - Utest region<br>101b - Others: Reserved|
|23-21<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1228 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|20-0|Flash Memory Address|
|DCMDCFE8|Indicates the flash memory address of the DCF client having an error.|



### 38.3.16 DCF Scan Report (DCMSRR9) 

#### Offset 

|Register|Offset|
|---|---|
|DCMSRR9|50h|



#### Function 

Resets on destructive reset. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/038_Device_Configuration_Module_-DCM-/S32K3XXRM_数据表.pdf-1229-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>DCMD DCME DCME<br>R 0 DCMDCFF9  0 DCMDCFE9<br>CFT9  SD9  SF9<br>W W1C W1C W1C W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DCMDCFE9<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29|Scanning Timeout On Flash Memory|
|DCMDCFT9|Indicates if scanning timeout exists on flash memory address.|
||0b - Does not exist|
||1b - Exists|
|28|Chip Side Error|
|DCMESD9||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1229 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the<br>DCF client, such as write-once error.<br>0b - No errors<br>1b - Errors exist|
|27<br>DCMESF9|Flash Memory Error<br>Indicates if a flash memory error exists.<br>0b - No errors<br>1b - Errors exist|
|26-24|DCF Record Location|
|DCMDCFF9|Indicates the DCF record location in flash memory.<br>010b - Utest region<br>101b - Others: Reserved|
|23-21<br>—|Reserved|
|20-0|Flash Memory Address|
|DCMDCFE9|Indicates the flash memory address of the DCF client having an error.|



### 38.3.17 DCF Scan Report (DCMSRR10) 

#### Offset 

|Register|Offset|
|---|---|
|DCMSRR10|54h|



Function 

Resets on destructive reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1230 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|0||DCMD<br>CFT...|DCME<br>SD10|DCME<br>SF10|D|CMDCFF1|0||0|||D|CMDCFE10|||
|W|||W1C|W1C|W1C||W1C|||||||W1C|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||DCMD|CFE10||||||||
|W||||||||W1|C||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-30<br>—<br>29<br>DCMDCFT10|Reserved<br>Scanning Timeout On Flash Memory<br>Indicates if scanning timeout exists on flash memory address.<br>0b - Does not exist<br>1b - Exists|
|28<br>DCMESD10|Chip Side Error<br>Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the<br>DCF client, such as write-once error.<br>0b - No errors<br>1b - Errors exist|
|27<br>DCMESF10|Flash Memory Error<br>Indicates if a flash memory error exists.<br>0b - No errors<br>1b - Errors exist|
|26-24<br>DCMDCFF10|DCF Record Location<br>Indicates the DCF record location in flash memory.<br>010b - Utest region<br>101b - Others: Reserved|
|23-21<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1231 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|20-0|Flash Memory Address|
|DCMDCFE10|Indicates the flash memory address of the DCF client having an error.|



### 38.3.18 DCF Scan Report (DCMSRR11) 

Offset 

|Register|Offset|
|---|---|
|DCMSRR11|58h|



#### Function 

Resets on destructive reset. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/038_Device_Configuration_Module_-DCM-/S32K3XXRM_数据表.pdf-1232-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>DCMD DCME DCME<br>R 0 DCMDCFF11  0 DCMDCFE11<br>CFT... SD11  SF11<br>W W1C W1C W1C W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DCMDCFE11<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29|Scanning Timeout On Flash Memory|
|DCMDCFT11|Indicates if scanning timeout exists on flash memory address.|
||0b - Does not exist|
||1b - Exists|
|28|Chip Side Error|
|DCMESD11||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1232 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the<br>DCF client, such as write-once error.<br>0b - No errors<br>1b - Errors exist|
|27<br>DCMESF11|Flash Memory Error<br>Indicates if a flash memory error exists.<br>0b - No errors<br>1b - Errors exist|
|26-24<br>DCMDCFF11|DCF Record Location<br>Indicates the DCF record location in flash memory.<br>010b - Utest region<br>101b - Others: Reserved|
|23-21<br>—|Reserved|
|20-0|Flash Memory Address|
|DCMDCFE11|Indicates the flash memory address of the DCF client having an error.|



### 38.3.19 DCF Scan Report (DCMSRR12) 

#### Offset 

|Register|Offset|
|---|---|
|DCMSRR12|5Ch|



Function 

Resets on destructive reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1233 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|0||DCMD<br>CFT...|DCME<br>SD12|DCME<br>SF12|D|CMDCFF|12||0|||D|CMDCFE12|||
|W|||W1C|W1C|W1C||W1C|||||||W1C|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||DCMD|CFE12||||||||
|W||||||||W1|C||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-30<br>—<br>29<br>DCMDCFT12|Reserved<br>Scanning Timeout On Flash Memory<br>Indicates if scanning timeout exists on flash memory address.<br>0b - Does not exist<br>1b - Exists|
|28<br>DCMESD12|Chip Side Error<br>Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the<br>DCF client, such as write-once error.<br>0b - No errors<br>1b - Errors exist|
|27<br>DCMESF12|Flash Memory Error<br>Indicates if a flash memory error exists.<br>0b - No errors<br>1b - Errors exist|
|26-24<br>DCMDCFF12|DCF Record Location<br>Indicates the DCF record location in flash memory.<br>010b - Utest region<br>101b - Others: Reserved|
|23-21<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1234 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|20-0|Flash Memory Address|
|DCMDCFE12|Indicates the flash memory address of the DCF client having an error.|



### 38.3.20 DCF Scan Report (DCMSRR13) 

#### Offset 

|Register|Offset|
|---|---|
|DCMSRR13|60h|



#### Function 

Resets on destructive reset. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/038_Device_Configuration_Module_-DCM-/S32K3XXRM_数据表.pdf-1235-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>DCMD DCME DCME<br>R 0 DCMDCFF13  0 DCMDCFE13<br>CFT... SD13  SF13<br>W W1C W1C W1C W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DCMDCFE13<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29|Scanning Timeout On Flash Memory|
|DCMDCFT13|Indicates if scanning timeout exists on flash memory address.|
||0b - Does not exist|
||1b - Exists|
|28|Chip Side Error|
|DCMESD13||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1235 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the<br>DCF client, such as write-once error.<br>0b - No errors<br>1b - Errors exist|
|27<br>DCMESF13|Flash Memory Error<br>Indicates if a flash memory error exists.<br>0b - No errors<br>1b - Errors exist|
|26-24<br>DCMDCFF13|DCF Record Location<br>Indicates the DCF record location in flash memory.<br>010b - Utest region<br>101b - Others: Reserved|
|23-21<br>—|Reserved|
|20-0|Flash Memory Address|
|DCMDCFE13|Indicates the flash memory address of the DCF client having an error.|



### 38.3.21 DCF Scan Report (DCMSRR14) 

#### Offset 

|Register|Offset|
|---|---|
|DCMSRR14|64h|



Function 

Resets on destructive reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1236 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|0||DCMD<br>CFT...|DCME<br>SD14|DCME<br>SF14|D|CMDCFF1|4||0|||D|CMDCFE14|||
|W|||W1C|W1C|W1C||W1C|||||||W1C|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||DCMD|CFE14||||||||
|W||||||||W1|C||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-30<br>—<br>29<br>DCMDCFT14|Reserved<br>Scanning Timeout On Flash Memory<br>Indicates if scanning timeout exists on flash memory address.<br>0b - Does not exist<br>1b - Exists|
|28<br>DCMESD14|Chip Side Error<br>Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the<br>DCF client, such as write-once error.<br>0b - No errors<br>1b - Errors exist|
|27<br>DCMESF14|Flash Memory Error<br>Indicates if a flash memory error exists.<br>0b - No errors<br>1b - Errors exist|
|26-24<br>DCMDCFF14|DCF Record Location<br>Indicates the DCF record location in flash memory.<br>010b - Utest region<br>101b - Others: Reserved|
|23-21<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1237 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|20-0|Flash Memory Address|
|DCMDCFE14|Indicates the flash memory address of the DCF client having an error.|



### 38.3.22 DCF Scan Report (DCMSRR15) 

#### Offset 

|Register|Offset|
|---|---|
|DCMSRR15|68h|



#### Function 

Resets on destructive reset. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/038_Device_Configuration_Module_-DCM-/S32K3XXRM_数据表.pdf-1238-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>DCMD DCME DCME<br>R 0 DCMDCFF15  0 DCMDCFE15<br>CFT... SD15  SF15<br>W W1C W1C W1C W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DCMDCFE15<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29|Scanning Timeout On Flash Memory|
|DCMDCFT15|Indicates if scanning timeout exists on flash memory address.|
||0b - Does not exist|
||1b - Exists|
|28|Chip Side Error|
|DCMESD15||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1238 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the<br>DCF client, such as write-once error.<br>0b - No errors<br>1b - Errors exist|
|27<br>DCMESF15|Flash Memory Error<br>Indicates if a flash memory error exists.<br>0b - No errors<br>1b - Errors exist|
|26-24|DCF Record Location|
|DCMDCFF15|Indicates the DCF record location in flash memory.<br>010b - Utest region<br>101b - Others: Reserved|
|23-21<br>—|Reserved|
|20-0|Flash Memory Address|
|DCMDCFE15|Indicates the flash memory address of the DCF client having an error.|



### 38.3.23 DCF Scan Report (DCMSRR16) 

#### Offset 

|Register|Offset|
|---|---|
|DCMSRR16|6Ch|



Function 

Resets on destructive reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1239 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|0||DCMD<br>CFT...|DCME<br>SD16|DCME<br>SF16|D|CMDCFF|16||0|||D|CMDCFE16|||
|W|||W1C|W1C|W1C||W1C|||||||W1C|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||DCMD|CFE16||||||||
|W||||||||W1|C||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-30<br>—<br>29<br>DCMDCFT16|Reserved<br>Scanning Timeout On Flash Memory<br>Indicates if scanning timeout exists on flash memory address.<br>0b - Does not exist<br>1b - Exists|
|28<br>DCMESD16|Chip Side Error<br>Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the<br>DCF client, such as write-once error.<br>0b - No errors<br>1b - Errors exist|
|27<br>DCMESF16|Flash Memory Error<br>Indicates if a flash memory error exists.<br>0b - No errors<br>1b - Errors exist|
|26-24<br>DCMDCFF16|DCF Record Location<br>Indicates the DCF record location in flash memory.<br>010b - Utest region<br>101b - Others: Reserved|
|23-21<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1240 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|20-0|Flash Memory Address|
|DCMDCFE16|Indicates the flash memory address of the DCF client having an error.|



### 38.3.24 LC Scan Status 2 (DCMLCS_2) 

#### Offset 

|Register|Offset|
|---|---|
|DCMLCS_2|80h|



#### Function 

Stores the status of LC scan. The default status of each LC phase is "not yet scanned." 

This register resets on destructive reset, and always returns 0 in the IN_FIELD phase of the LC. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/038_Device_Configuration_Module_-DCM-/S32K3XXRM_数据表.pdf-1241-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>DCML DCML DCML<br>R 0 DCMLCC6<br>CFE6  CE6  CSS6<br>W W1C W1C W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-6<br>—|Reserved|
|5|Flash Memory Error Check|
|DCMLCFE6|Indicates the status of flash memory check.|
||0b - Successful|
||1b - Failed|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1241 / 4640 

NXP Semiconductors 

Device Configuration Module (DCM) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|4<br>DCMLCE6|FA ECC Errors<br>Indicates if ECC errors exist in FA.<br>0b - No errors<br>1b - Errors exist|
|3-1|FA Marking|
|DCMLCC6|Indicates the FA marking status.<br>These errors may cause this field to indicate the "not scanned yet" status:<br>• If the reading completes too early and DCM has not yet scanned the LC.<br>• If there is an error in the flash memory after completion of the reading.<br>000b - Not scanned yet<br>001b - Marked as active<br>010b - Marked as inactive<br>011b - Region is erased/virgin<br>101b - Marked as inactive by an unknown pattern<br>110b - Scanning timed out|
|0|FA Scan Status|
|DCMLCSS6|Indicates if errors exist in the FA scan.<br>0b - No errors|
||1b - Errors exist|



|38.4 Glossary||
|---|---|
|FA|Failure analysis|
|LC|Life cycle|
|Pre-FA|Pre-failure analysis|
|RoT|Root of trust|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1242 / 4640 

