NXP Semiconductors 

# Chapter 56 Cyclic Redundancy Check (CRC) 

## 56.1 Chip-specific CRC information 

This chip supports one instance of CRC module. 

## 56.2 Overview 

The Cyclic Redundancy Check (CRC) module generates 16/32-bit CRC code for error detection. 

The CRC module provides a programmable polynomial and other parameters required to implement a 16-bit or 32-bit CRC standard. 

The 16/32-bit code is calculated for 32 bits of data at a time. 

### 56.2.1 Block diagram 

The following is a block diagram of the CRC. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/056_Cyclic_Redundancy_Check_-CRC-/S32K3XXRM_数据表.pdf-1868-10.png)


<!-- Start of picture text -->
TOT WAS FXOR TOTR<br>CRC Data Register<br>[31:24][ CRC Data Register<br>[23:16] Reverse Seed [31:24]<br>[15:8][7:0] Logic CRC Data LogicNOT LogicReverse [23:16][15:8]<br>[7:0]<br>Checksum<br>CRC Polynomial                       CRC Engine<br>Register               Data<br>[31:24]<br>[23:16] Combine<br>Polynomial<br>[15:8] Logic<br>[7:0]<br>16-/32-bit Select<br>TCRC<br>MUX<br><!-- End of picture text -->

Figure 204. Programmable cyclic redundancy check (CRC) block diagram 

### 56.2.2 Features 

Following are the features of the CRC module. 

- Hardware CRC generator circuit using a 16-bit or 32-bit programmable shift register 

- Programmable initial seed value and polynomial 

- Option to transpose input data or output data (the CRC result) bitwise or bytewise. This option is required for certain CRC standards. A bytewise transpose operation is not possible when accessing the CRC data register via 8-bit accesses. In this case, the user's software must perform the bytewise transpose function. 

- Option for inversion of final CRC result 

- 32-bit CPU register programming interface 

## 56.3 Functional description 

### 56.3.1 Modes of operation 

Following sections provide a brief description of various modes which affect the functionality of the CRC module. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1868 / 4640 

NXP Semiconductors 

Cyclic Redundancy Check (CRC) 

#### 56.3.1.1 Run mode 

This is the basic mode of operation. 

#### 56.3.1.2 Low-power modes 

Any CRC calculation in progress stops when the device enters a low-power mode that disables the module clock. It resumes after the clock is enabled or via the system reset for exiting the low-power mode. Clock gating for this module is dependent on the device. 

### 56.3.2 CRC calculations 

In 16-bit and 32-bit CRC modes, data values can be programmed 8 bits, 16 bits, or 32 bits at a time, provided all bytes are contiguous. Noncontiguous bytes can lead to an incorrect CRC computation. 

#### 56.3.2.1 16-bit CRC 

The steps to compute a 16-bit CRC are listed as follows. 

1. Clear CRC_CTRL[TCRC] to enable 16-bit CRC mode. 

2. Program the transpose and complement options in the CTRL register as required for the CRC calculation. See Transpose feature and CRC result complement for details. 

3. Write a 16-bit polynomial to the CRC_GPOLY[LOW] field. The CRC_GPOLY[HIGH] field is not usable in 16-bit CRC mode. 

4. Set CRC_CTRL[WAS] to program the seed value. 

5. Write a 16-bit seed to CRC_DATA[LU:LL]. CRC_DATA[HU:HL] are not used. 

6. Clear CRC_CTRL[WAS] to start writing data values. 

7. Write data values into CRC_DATA[HU:HL:LU:LL]. A CRC is computed on every data value write, and the intermediate CRC result is stored back into CRC_DATA[LU:LL]. 

8. When all values have been written, read the final CRC result from CRC_DATA[LU:LL]. 

Transpose and complement operations are performed on-the-fly while reading or writing values. See Transpose feature and CRC result complement for details. 

#### 56.3.2.2 32-bit CRC 

The steps to compute a 32-bit CRC are listed as follows. 

1. Set CRC_CTRL[TCRC] to enable 32-bit CRC mode. 

2. Program the transpose and complement options in the CTRL register as required for the CRC calculation. See Transpose feature and CRC result complement for details. 

3. Write a 32-bit polynomial to CRC_GPOLY[HIGH:LOW]. 

4. Set CRC_CTRL[WAS] to program the seed value. 

5. Write a 32-bit seed to CRC_DATA[HU:HL:LU:LL]. 

6. Clear CRC_CTRL[WAS] to start writing data values. 

7. Write data values into CRC_DATA[HU:HL:LU:LL]. A CRC is computed on every data value write, and the intermediate CRC result is stored back into CRC_DATA[HU:HL:LU:LL]. 

8. When all values have been written, read the final CRC result from CRC_DATA[HU:HL:LU:LL]. The CRC is calculated bytewise, and two clocks are required to complete one CRC calculation. 

Transpose and complement operations are performed on-the-fly while reading or writing values. See Transpose feature and CRC result complement for details. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1869 / 4640 

NXP Semiconductors 

Cyclic Redundancy Check (CRC) 

### 56.3.3 Transpose feature 

By default, the transpose feature is not enabled. However, some CRC standards require the input data and/or the final checksum to be transposed. The user software has the option to configure each transpose operation separately, as desired by the CRC standard. The data is transposed on-the-fly while being read or written. 

Some protocols use little-endian format for the data stream to calculate a CRC. In this case, the transpose feature usefully flips the bits. This transpose option is one of the types supported by the CRC module. 

#### 56.3.3.1 Types of transpose 

The CRC module provides several types of transpose functions to flip the bits and/or bytes, for both writing input data and reading the CRC result, separately using the CTRL[TOT] or CTRL[TOTR] fields, according to the CRC calculation being used. 

The following types of transpose functions are available for writing to and reading from the CRC Data register. 

1. CTRL[TOT] or CTRL[TOTR] is 0b00. 

No transposition occurs. 

2. CTRL[TOT] or CTRL[TOTR] is 0b01 

Bits in a byte are transposed, while bytes are not transposed. 

reg[31:0] becomes {reg[24:31], reg[16:23], reg[8:15], reg[0:7]}. See the following figure. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/056_Cyclic_Redundancy_Check_-CRC-/S32K3XXRM_数据表.pdf-1870-13.png)


<!-- Start of picture text -->
31 24 23 16 15 8 7 0<br>24 31 16 23 8 15 0 7<br><!-- End of picture text -->

Figure 205. Transpose type 0b01 

3. CTRL[TOT] or CTRL[TOTR] is 0b10. 

Both bits in bytes and bytes are transposed. 

reg[31:0] becomes = {reg[0:7], reg[8:15],reg[16:23], reg[24:31]}. See the following figure. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/056_Cyclic_Redundancy_Check_-CRC-/S32K3XXRM_数据表.pdf-1870-18.png)


<!-- Start of picture text -->
31 0<br>0 31<br><!-- End of picture text -->

Figure 206. Transpose type 0b10 

4. CTRL[TOT] or CTRL[TOTR] is 0b11. 

Bytes are transposed, but bits are not transposed. 

reg[31:0] becomes {reg[7:0], reg[15:8], reg[23:16], reg[31:24]}. See the following figure. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1870 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/056_Cyclic_Redundancy_Check_-CRC-/S32K3XXRM_数据表.pdf-1871-01.png)


<!-- Start of picture text -->
Cyclic Redundancy Check (CRC)<br>31 24 23 16 15 8 7 0<br>7 0 15 8 23 16 31 24<br>Figure 207. Transpose type 0b11<br><!-- End of picture text -->

~~<mark>NOTE</mark>~~ 

For 8-bit and 16-bit write accesses to the CRC data register, the data is transposed with zeros on the unused byte or bytes (taking 32 bits as a whole), but the CRC is calculated on the valid byte(s) only. When reading the CRC data register for a 16-bit CRC result and using transpose options 10 and 11, the resulting value after transposition resides in the CRC[HU:HL] fields. The user software must account for this situation when reading the 16-bit CRC result, so reading 32 bits is preferred. 

### 56.3.4 CRC result complement 

When CTRL[FXOR] is set, the checksum is complemented. The CRC result complement function outputs the complement of the checksum value stored in the CRC Data (DATA) Register every time the CRC Data (DATA) register is read. When CTRL[FXOR] is cleared, reading the CRC Data (DATA) Register accesses the raw checksum value. 

## 56.4 Use cases 

~~<mark>NOTE</mark>~~ 

The following tables apply to little-endian format. 

### 56.4.1 CRC Control Register programming 

The following table shows the CRC Control Register programming for 16-bit CRC. 

Table 269. Control Register (CTRL) programming for 16-bit CRC 

|Algorithm|Poly|Seed|Ref In|Ref Out|XOR Out|CTRL[TOT]|CTRL[TOTR]|CTRL[FXOR]|
|---|---|---|---|---|---|---|---|---|
|CRC-16/<br>CCITT_FALSE|0x1021|0xFFFF|0|0|0x0000|0x0|0x0|0x0|
|CRC-16 / ARC|0x8005|0x0000|1|1|0x0000|0x1|0x2|0x0|
|CRC16_AUG_CCI<br>TT|0x1021|0x1D0F|0|0|0x0000|0x0|0x0|0x0|
|CRC16_BUYPAS<br>S|0x8005|0x0000|0|0|0x0000|0x0|0x0|0x0|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1871 / 4640 

NXP Semiconductors 

Cyclic Redundancy Check (CRC) 

Table 269. Control Register (CTRL) programming for 16-bit CRC (continued) 

|Algorithm<br>CRC16_CCITT_Z<br>ERO|Poly<br>0x1021|Seed<br>0x0000|Ref In<br>0|Ref Out<br>0|XOR Out<br>0x0000|CTRL[TOT]<br>0x0|CTRL[TOTR]<br>0x0|CTRL[FXOR]<br>0x0|
|---|---|---|---|---|---|---|---|---|
|CRC16_CDMA20<br>00|0xC867|0xFFFF|0|0|0x0000|0x0|0x0|0x0|
|CRC16_DDS_110|0x8005|0x800D|0|0|0x0000|0x0|0x0|0x0|
|CRC16_DECT_R|0x589|0x0000|0|0|0xFFFF|0x1|0x2|0x1|
|CRC16_DECT_X|0x589|0x0000|0|0|0x0000|0x0|0x0|0x0|
|CRC16_DNP|0x3D65|0x0000|1|1|0xFFFF|0x1|0x2|0x1|
|CRC16_EN_1375<br>7|0x3D65|0x0000|0|0|0xFFFF|0x1|0x2|0x1|
|CRC16_GENIBUS|0x1021|0xFFFF|0|0|0xFFFF|0x1|0x2|0x1|
|CRC16_MAXIM|0x8005|0x0000|1|1|0xFFFF|0x1|0x2|0x1|
|CRC16_MCRF4X<br>X|0x1021|0xFFFF|1|1|0x0000|0x1|0x2|0x0|
|CRC16_RIELLO|0x1021|0xB2AA|1|1|0x0000|0x1|0x2|0x0|
|CRC16_T10_DIF|0x8BB7|0x0000|0|0|0x0000|0x0|0x0|0x0|
|CRC16_TELEDIS<br>K|0xA097|0x0000|0|0|0x0000|0x0|0x0|0x0|
|CRC16_TMS3715<br>7|0x1021|0x89EC|1|1|0x0000|0x1|0x2|0x0|
|CRC16_USB|0x8005|0xFFFF|1|1|0xFFFF|0x1|0x2|0x1|
|CRC16_A|0x1021|0xC6C6|1|1|0x0000|0x1|0x2|0x0|
|CRC16_KERMIT|0x1021|0x0000|1|1|0x0000|0x1|0x2|0x0|
|CRC16_MODBUS|0x8005|0xFFFF|1|1|0x0000|0x1|0x2|0x0|
|CRC16_X_25|0x1021|0xFFFF|1|1|0xFFFF|0x1|0x2|0x1|
|CRC16_XMODEM|0x1021|0x0000|0|0|0x0000|0x0|0x0|0x0|



The following table shows the CRC Control Register programming for 32-bit CRC. 

Table 270. Control Register (CTRL) programming for 32-bit CRC 

|Algorithm|Poly|Seed|Ref In|Ref Out|Xor Out|CTRL[TOT]|CTRL[TOTR]|CTRL[FXOR]|
|---|---|---|---|---|---|---|---|---|
|CRC - 32|0x04C11DB<br>7|0xFFFFFFFF|1|1|0xFFFF_FFFF|0x1|0x2|0x1|
|CRC-32/<br>BZIP2|0x04C11DB<br>7|0xFFFFFFFF|0|0|0xFFFF_FFFF|0x0|0x0|0x1|
|CRC-32C|0x1EDC6F4<br>1|0xFFFFFFFF|1|1|0xFFFF_FFFF|0x1|0x2|0x1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1872 / 4640 

NXP Semiconductors 

Cyclic Redundancy Check (CRC) 

Table 270. Control Register (CTRL) programming for 32-bit CRC (continued) 

|Algorithm|Poly|Seed|Ref In|Ref Out|Xor Out|CTRL[TOT]|CTRL[TOTR]|CTRL[FXOR]|
|---|---|---|---|---|---|---|---|---|
|CRC-32D|0xA833982<br>B|0xFFFFFFFF|1|1|0xFFFF_FFFF|0x1|0x2|0x1|
|CRC-32/<br>MPEG-2|0x04C11DB<br>7|0xFFFFFFFF|0|0|0x0000_0000|0x0|0x0|0x0|
|CRC-32/<br>POSIX|0x04C11DB<br>7|0x00000000|0|0|0xFFFF_FFFF|0x0|0x0|0x1|
|CRC-32Q|0x814141A<br>B|0x00000000|0|0|0x0000_0000|0x0|0x0|0x0|
|CRC-32/<br>JAMCRC|0x04C11DB<br>7|0xFFFFFFFF|1|1|0x0000_0000|0x1|0x2|0x0|
|CRC-32/<br>XFER|0x000000A<br>F|0x00000000|0|0|0x0000_0000|0x0|0x0|0x0|



### 56.4.2 Expected read data fields 

The following table shows the expected read data fields for 16-bit CRC. 

Table 271. Expected read data fields for 16-bit CRC 

|Algorithm|CRC DATA Register (DATA)|
|---|---|
|CRC-16/CCITT_FALSE|[ 31 : 16 ] = Unknown [ 15 : 0 ] = Valid Data|
|CRC-16 / ARC|[ 31 : 16 ] = Valid Data [ 15 : 0 ] = Unknown|
|CRC16_AUG_CCITT|[ 31 : 16 ] = Unknown [ 15 : 0 ] = Valid Data|
|CRC16_BUYPASS|[ 31 : 16 ] = Unknown [ 15 : 0 ] = Valid Data|
|CRC16_CCITT_ZERO|[ 31 : 16 ] = Unknown [ 15 : 0 ] = Valid Data|
|CRC16_CDMA2000|[ 31 : 16 ] = Unknown [ 15 : 0 ] = Valid Data|
|CRC16_DDS_110|[ 31 : 16 ] = Unknown [ 15 : 0 ] = Valid Data|
|CRC16_DECT_R|[ 31 : 16 ] = Valid Data [ 15 : 0 ] = Unknown|
|CRC16_DECT_X|[ 31 : 16 ] = Unknown [ 15 : 0 ] = Valid Data|
|CRC16_DNP|[ 31 : 16 ] = Valid Data [ 15 : 0 ] = Unknown|
|CRC16_EN_13757|[ 31 : 16 ] = Valid Data [ 15 : 0 ] = Unknown|
|CRC16_GENIBUS|[ 31 : 16 ] = Valid Data [ 15 : 0 ] = Unknown|
|CRC16_MAXIM|[ 31 : 16 ] = Valid Data [ 15 : 0 ] = Unknown|
|CRC16_MCRF4XX|[ 31 : 16 ] = Valid Data [ 15 : 0 ] = Unknown|
|CRC16_RIELLO|[ 31 : 16 ] = Valid Data [ 15 : 0 ] = Unknown|
|CRC16_T10_DIF|[ 31 : 16 ] = Unknown [ 15 : 0 ] = Valid Data|
|CRC16_TELEDISK|[ 31 : 16 ] = Unknown [ 15 : 0 ] = Valid Data|
|CRC16_TMS37157|[ 31 : 16 ] = Valid Data [ 15 : 0 ] = Unknown|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1873 / 4640 

NXP Semiconductors 

Cyclic Redundancy Check (CRC) 

Table 271. Expected read data fields for 16-bit CRC (continued) 

|Algorithm|CRC DATA Register (DATA)|
|---|---|
|CRC16_USB|[ 31 : 16 ] = Valid Data [ 15 : 0 ] = Unknown|
|CRC16_A|[ 31 : 16 ] = Valid Data [ 15 : 0 ] = Unknown|
|CRC16_KERMIT|[ 31 : 16 ] = Valid Data [ 15 : 0 ] = Unknown|
|CRC16_MODBUS|[ 31 : 16 ] = Valid Data [ 15 : 0 ] = Unknown|
|CRC16_X_25|[ 31 : 16 ] = Valid Data [ 15 : 0 ] = Unknown|
|CRC16_XMODEM|[ 31 : 16 ] = Unknown [ 15 : 0 ] = Valid Data|



The following table shows the expected read data fields for 32-bit CRC. 

Table 272. Expected read data fields for 32-bit CRC 

|Algorithm|CRC DATA Register (DATA)|
|---|---|
|CRC - 32|[ 31 : 0 ] = Valid Data|
|CRC-32/BZIP2|[ 31 : 0 ] = Valid Data|
|CRC-32C|[ 31 : 0 ] = Valid Data|
|CRC-32D|[ 31 : 0 ] = Valid Data|
|CRC-32/MPEG-2|[ 31 : 0 ] = Valid Data|
|CRC-32/POSIX|[ 31 : 0 ] = Valid Data|
|CRC-32Q|[ 31 : 0 ] = Valid Data|
|CRC-32/JAMCRC|[ 31 : 0 ] = Valid Data|
|CRC-32/XFER|[ 31 : 0 ] = Valid Data|



## 56.5 External signals 

There is no CRC signal that connects off chip. 

## 56.6 CRC initialization/reinitialization 

To enable the CRC calculation, the user must program CRC_CTRL[WAS], CRC_GPOLY, necessary parameters for transposition and CRC result inversion in the applicable registers. Asserting CRC_CTRL[WAS] enables the programming of the seed value into the CRC_DATA register. 

After a completed CRC calculation, the module can be reinitialized for a new CRC computation by reasserting CRC_CTRL[WAS] and programming a new, or previously used, seed value. All other parameters must be set before programming the seed value and subsequent data values. 

## 56.7 Memory map and register descriptions 

~~<mark>NOTE</mark>~~ 

Write access to the register addresses not mapped to the peripheral but included in the address space of the peripheral may result in unpredictable functionality. The CRC module should be reconfigured if a transfer error occurs. 

### 56.7.1 CRC register descriptions 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1874 / 4640 

NXP Semiconductors 

Cyclic Redundancy Check (CRC) 

#### 56.7.1.1 CRC memory map 

CRC base address: 4038_0000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|CRC DATA register (DATA)|32|RW|FFFF_FFFFh|
|4h|CRC Polynomial register (GPOLY)|32|RW|0000_1021h|
|8h|CRC Control register (CTRL)|32|RW|0000_0000h|



#### 56.7.1.2 CRC DATA register (DATA) 

##### Offset 

|Register|Offset|
|---|---|
|DATA|0h|



##### Function 

The CRC DATA register contains the value of the seed, data, and checksum. When CTRL[WAS] is set, any write to the data register is regarded as the seed value. When CTRL[WAS] is cleared, any write to the data register is regarded as data for general CRC computation. 

In 16-bit CRC mode, the HU and HL fields are not used for programming the seed value, and reads of these fields return an indeterminate value. In 32-bit CRC mode, all fields are used for programming the seed value. 

When programming data values, the values can be written 8 bits, 16 bits, or 32 bits at a time, provided all bytes are contiguous; with MSB of data value written first. 

After all data values are written, the CRC result can be read from this data register. In 16-bit CRC mode, the CRC result is available in the LU and LL fields. In 32-bit CRC mode, all fields contain the result. Reads of this register at any time return the intermediate CRC value, provided the CRC module is configured. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||HU||||||||HL|||||
|Reset|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||LU||||||||LL|||||
|Reset|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1875 / 4640 

NXP Semiconductors 

Cyclic Redundancy Check (CRC) 

##### Fields 

|Field|Function|
|---|---|
|31-24|CRC High Upper Byte|
|HU|In 16-bit CRC mode (CTRL[TCRC] is 0), this field is not used for programming a seed value. In 32-bit<br>CRC mode (CTRL[TCRC] is 1), values written to this field are part of the seed value when CTRL[WAS]<br>is 1. When CTRL[WAS] is 0, data written to this field is used for CRC checksum generation in both 16-bit<br>and 32-bit CRC modes.|
|23-16<br>HL|CRC High Lower Byte<br>In 16-bit CRC mode (CTRL[TCRC] is 0), this field is not used for programming a seed value. In 32-bit<br>CRC mode (CTRL[TCRC] is 1), values written to this field are part of the seed value when CTRL[WAS]<br>is 1. When CTRL[WAS] is 0, data written to this field is used for CRC checksum generation in both 16-bit<br>and 32-bit CRC modes.|
|15-8|CRC Low Upper Byte|
|LU|When CTRL[WAS] is 1, values written to this field are part of the seed value. When CTRL[WAS] is 0,<br>data written to this field is used for CRC checksum generation.|
|7-0|CRC Low Lower Byte|
|LL|When CTRL[WAS] is 1, values written to this field are part of the seed value. When CTRL[WAS] is 0,<br>data written to this field is used for CRC checksum generation.|



#### 56.7.1.3 CRC Polynomial register (GPOLY) 

##### Offset 

|Register|Offset|
|---|---|
|GPOLY|4h|



##### Function 

This register contains the value of the polynomial for the CRC calculation. The HIGH field contains the upper 16 bits of the CRC polynomial, which are used only in 32-bit CRC mode. Writes to the HIGH field are ignored in 16-bit CRC mode. The LOW field contains the lower 16 bits of the CRC polynomial, which are used in both 16- and 32-bit CRC modes. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||HIG|H||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||LO|W||||||||
|Reset|0|0|0|1|0|0|0|0|0|0|1|0|0|0|0|1|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1876 / 4640 

NXP Semiconductors 

Cyclic Redundancy Check (CRC) 

##### Fields 

|Field|Function|
|---|---|
|31-16|High Polynominal Half-word|
|HIGH|Writable and readable in 32-bit CRC mode (CTRL[TCRC] is 1). This field is not writable in 16-bit CRC<br>mode (CTRL[TCRC] is 0).|
|15-0|Low Polynominal Half-word|
|LOW|Writable and readable in both 32-bit and 16-bit CRC modes.|



#### 56.7.1.4 CRC Control register (CTRL) 

##### Offset 

|Register|Offset|
|---|---|
|CTRL|8h|



##### Function 

This register controls the configuration and working of the CRC module. Appropriate bits must be set before starting a new CRC calculation. A new CRC calculation is initialized by asserting CTRL[WAS] and then writing the seed into the CRC DATA register. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Safety/056_Cyclic_Redundancy_Check_-CRC-/S32K3XXRM_数据表.pdf-1877-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0<br>TOT  TOTR  FXOR  WAS  TCRC<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-30|Type Of Transpose For Writes|
|TOT|Defines the transpose configuration of the data written to the CRC DATA register. SeeTranspose<br>featurefor the available transpose options.|
||00b - No transposition.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1877 / 4640 

NXP Semiconductors 

Cyclic Redundancy Check (CRC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||01b - Bits in bytes are transposed; bytes are not transposed.<br>10b - Both bits in bytes and bytes are transposed.<br>11b - Only bytes are transposed; no bits in a byte are transposed.|
|29-28<br>TOTR|Type Of Transpose For Read<br>Identifies the transpose configuration of the value read from the CRC DATA register. SeeTranspose<br>featurefor the available transpose options.<br>00b - No transposition.<br>01b - Bits in bytes are transposed; bytes are not transposed.<br>10b - Both bits in bytes and bytes are transposed.<br>11b - Only bytes are transposed; no bits in a byte are transposed.|
|27<br>—<br>26<br>FXOR|Reserved<br>Complement Read Of CRC DATA register<br>Some CRC protocols require the final checksum to be XORed with 0xFFFFFFFF or 0xFFFF. Asserting<br>this bit enables on-the-fly complementing of read data.<br>0b - No XOR on reading.<br>1b - Invert or complement the read value of the CRC DATA register.|
|25<br>WAS|Write CRC DATA register As Seed<br>When asserted, a value written to the CRC DATA register is considered a seed value. When deasserted,<br>a value written to the CRC DATA register is taken as data for CRC computation.<br>0b - Writes to the CRC DATA register are data values.<br>1b - Writes to the CRC DATA register are seed values.|
|24|TCRC|
|TCRC|Width of CRC protocol.<br>0b - 16-bit CRC protocol.<br>1b - 32-bit CRC protocol.|
|23-0<br>—|Reserved|



## 56.8 Glossary 

Transpose Flipping input or output data bits (or bytes) Seed value Initial value of CRC calculation 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1878 / 4640 

