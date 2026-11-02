NXP Semiconductors 

# Chapter 25 Fast Internal RC Oscillator (FIRC) 

## 25.1 Introduction 

The FIRC digital interface controls the internal 48 MHz RC oscillator system. 

## 25.2 Features 

FIRC can be disabled in Standby mode via software. 

- Status register provides the current operating state: 

   - On and stable 

   - Off or on but not stable 

## 25.3 FIRC register descriptions 

### 25.3.1 FIRC memory map 

FIRC base address: 402D_0000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|4h|Status Register (Status_Register)|32|RO|0000_0001h|
|8h|Standby Enable Register (STDBY_ENABLE)|32|RW|0000_0000h|



### 25.3.2 Status Register (Status_Register) 

#### Offset 

|Register|Offset|
|---|---|
|Status_Register|4h|



#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/025_Fast_Internal_RC_Oscillator_-FIRC-/S32K3XXRM_数据表.pdf-0921-17.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>STATU<br>R<br>S<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

921 / 4640 

NXP Semiconductors 

Fast Internal RC Oscillator (FIRC) 

#### Fields 

|Field|Function|
|---|---|
|31-1<br>—|Reserved|
|0|Status bit for FIRC|
|STATUS|0b - FIRC is off or unstable.|
||1b - FIRC is on and stable.|



### 25.3.3 Standby Enable Register (STDBY_ENABLE) 

#### Offset 

|Register|Offset|
|---|---|
|STDBY_ENABLE|8h|



#### Function 

This register enables or disables FIRC in chip’s Standby mode. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/025_Fast_Internal_RC_Oscillator_-FIRC-/S32K3XXRM_数据表.pdf-0922-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R STDB<br>Reserved<br>W Y_EN<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-1<br>—|RESERVED|
|0|Enables or disables FIRC in chip’s Standby mode.|
|STDBY_EN|0b - Disabled|
||1b - Enabled|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

922 / 4640 

NXP Semiconductors 

Fast Internal RC Oscillator (FIRC) 

## 25.4 Glossary 

Standby mode 

Power saving mode of the chip 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

923 / 4640 

