NXP Semiconductors 

# Chapter 26 Slow Internal RC Oscillator (SIRC) 

## 26.1 Introduction 

The SIRC digital interface controls the slow internal on-chip 32 KHz RC oscillator system. 

## 26.2 Features 

The SIRC module: 

- Status register provides the current operating state: 

   - On and stable 

   - Off or on but not stable 

- Operates at a frequency of 32 kHz in Functional mode 

## 26.3 Operating mode 

Only a POR reset will initialize the SIRC. Destructive or Functional resets do not impact the SIRC functionality. 

SIRC stabilization occurs after 96 SIRC_CLK cycles. 

The SIRC output clock remains invalid until the analog SIRC stabilizes. The output clock does not glitch or overshoot its frequency during enabling or disabling. Also, the clock does not get stuck or produce glitches on a very short hardware disable pulse. 

## 26.4 SIRC register descriptions 

### 26.4.1 SIRC memory map 

Access to registers use 8-bit, 16-bit, or 32-bit addressing. 

SIRC base address: 402C_8000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|4h|Status Register (SR)|32|RO|0000_0001h|
|Ch|Miscellaneous input (MISCELLANEOUS_IN)|32|RW|0000_0000h|



### 26.4.2 Status Register (SR) 

Offset 

|Register|Offset|
|---|---|
|SR|4h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

924 / 4640 

NXP Semiconductors 

Slow Internal RC Oscillator (SIRC) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/026_Slow_Internal_RC_Oscillator_-SIRC-/S32K3XXRM_数据表.pdf-0925-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>STATU<br>R<br>S<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-1<br>—|Reserved|
|0|Status bit for SIRC|
|STATUS|0b - SIRC is off or unstable|
||1b - SIRC is on and stable|



### 26.4.3 Miscellaneous input (MISCELLANEOUS_IN) 

#### Offset 

|Register|Offset|
|---|---|
|MISCELLANEOUS_IN|Ch|



#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/026_Slow_Internal_RC_Oscillator_-SIRC-/S32K3XXRM_数据表.pdf-0925-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R STAN<br>Reserved  Reserved  Reserved<br>W DBY...<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

925 / 4640 

NXP Semiconductors 

Slow Internal RC Oscillator (SIRC) 

#### Fields 

|Field|Function|
|---|---|
|31-9<br>—|Reserved|
|8|Standby Enable for SIRC|
|STANDBY_EN|0b - SIRC disables in Standby mode|
|ABLE|1b - SIRC enables in Standby mode|
|7-4<br>—|Reserved|
|3-0<br>—|Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

926 / 4640 

