NXP Semiconductors 

# Chapter 82 Temperature Sensor (TempSense) 

## 82.1 Introduction 

The TEMPSENSE module contains control registers for use with the Temperature Sensor hard block. These registers use a peripheral bus interface to communicate with the chip. 

### 82.1.1 Overview 

TEMPSENSE is used to measure the temperature on the chip through an ADC. 

### 82.1.2 Block diagram 

The functional structure of the TEMPSENSE can be seen in the block diagram in Figure 522. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4611 / 4640 

NXP Semiconductors 

Temperature Sensor (TempSense) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Analog/082_Temperature_Sensor_-TempSense-/S32K3XXRM_数据表.pdf-4612-02.png)


<!-- Start of picture text -->
ETSCTL<br>& &<br>Vdd<br>To ADC<br>GNDSEL ETS_EN<br><!-- End of picture text -->

Figure 522. TEMPSENSE block diagram 

### 82.1.3 Features 

The TEMPSENSE includes the following features: 

- Provide a voltage proportional to the temperature which will be read out by ADC 

- Ground selection for improved precision in the ETS. The ETS ground could be different from the ADC ground. By exposing it to the ADC, the temperature calculation could be improved as the voltage value will be more precise. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4612 / 4640 

NXP Semiconductors 

Temperature Sensor (TempSense) 

## 82.2 Functional description 

### 82.2.1 General 

The TEMPSENSE module is designed to measure the temperature on the chip. The TEMPSENSE output can be read by an ADC on demand so that the software can determine the current die temperature. The software should enable the TEMPSENSE by setting ETSCTL[ETS_EN]. 

Coefficients are used to allow a simple and accurate calculation of linearized temperature directly from the ADC. The increase of the sampling time of the ADC from the minimum sampling value is increasing the temperature accuracy. 

### 82.2.2 Conversion voltage Temperature 

Solve the equation for the conversion from voltage to temperature. where VETS is the difference of Vbe and VGND. VGND is expose on the ADC output when ETSCTL[GNDSEL] is set. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Analog/082_Temperature_Sensor_-TempSense-/S32K3XXRM_数据表.pdf-4613-08.png)


The coefficients TCA0, TCA1 and TCA2 are read from the corresponding registers. They are stored in a signed fixed-point format as the folowing TCAx(11,4) (1 bit for the sign, 11 bits for the integer part and 4 bits for the decimal part). 

The calculation of the temperature should be done with the actual coefficient values provided in the TCAx fields. See the example below for an ambient temperature of 25C, and an ADC reference voltage of 5V. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Analog/082_Temperature_Sensor_-TempSense-/S32K3XXRM_数据表.pdf-4613-11.png)


By using the formula the junction temperature calculated is 26.5838 C. 

The maximal calculation error is 0.0313 Degrees 

If the supply of the ETS module is 3.3V, a conversion is necessary to calculate the accurate temperature. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Analog/082_Temperature_Sensor_-TempSense-/S32K3XXRM_数据表.pdf-4613-15.png)


## 82.3 Memory map and register definition 

### 82.3.1 Transfer error description 

The following actions will cause a transfer error and will not change the register content: 

- Any access to an unused register address 

- Write access to a read-only register (TCAx) 

### 82.3.2 TempSense register descriptions 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4613 / 4640 

NXP Semiconductors 

Temperature Sensor (TempSense) 

#### 82.3.2.1 TempSense memory map 

TEMPSENSE base address: 4037_C000h 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|0h|ETS Control (ETSCTL)|32|RW|0000_0000h|
|8h|Temperature Coefficient (TCA0)|32|RO|See<br>description|
|Ch|Temperature Coefficient (TCA1)|32|RO|See<br>description|
|10h|Temperature Coefficient (TCA2)|32|RO|See<br>description|



#### 82.3.2.2 ETS Control (ETSCTL) 

##### Offset 

|Register|Offset|
|---|---|
|ETSCTL|0h|



##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||0|||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||||0||||||||GNDS|ETS_|
|W|||||||||||||||EL|EN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function|
|---|---|
|31-2<br>—|Reserved|
|1|Ground selection|
|GNDSEL|0b - No exposure of the ground|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4614 / 4640 

NXP Semiconductors 

Temperature Sensor (TempSense) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - Expose ground on the ADC output if ETS_EN=1|
|0|Temperature Sensor enable|
|ETS_EN|Power up the ETS.|
||0b - Power down|
||1b - Functional mode|



#### 82.3.2.3 Temperature Coefficient (TCA0) 

##### Offset 

|Register|Offset|
|---|---|
|TCA0|8h|



##### Function 

This register contains the coefficient TCA0 needed to calculate the temperature.the reset value is specific for each chip. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Analog/082_Temperature_Sensor_-TempSense-/S32K3XXRM_数据表.pdf-4615-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset u u u u u u u u u u u u u u u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TCA0<br>W<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-16<br>—|Reserved|
|15-0|Temperature coefficient A0|
|TCA0|seeConversion voltage Temperaturefor the usage of this coefficient|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4615 / 4640 

NXP Semiconductors 

Temperature Sensor (TempSense) 

#### 82.3.2.4 Temperature Coefficient (TCA1) 

##### Offset 

|Register|Offset|
|---|---|
|TCA1|Ch|



##### Function 

This register contains the coefficient TCA1 needed to calculate the temperature.the reset value is specific for each chip. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Analog/082_Temperature_Sensor_-TempSense-/S32K3XXRM_数据表.pdf-4616-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset u u u u u u u u u u u u u u u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TCA1<br>W<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16<br>—|Reserved|
|15-0|Temperature coefficient A1|
|TCA1|seeConversion voltage Temperaturefor the usage of this coefficient|



#### 82.3.2.5 Temperature Coefficient (TCA2) 

##### Offset 

|Register|Offset|
|---|---|
|TCA2|10h|



##### Function 

This register contains the coefficient TCA2 needed to calculate the temperature.the reset value is specific for each chip. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4616 / 4640 

NXP Semiconductors 

Temperature Sensor (TempSense) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Analog/082_Temperature_Sensor_-TempSense-/S32K3XXRM_数据表.pdf-4617-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset u u u u u u u u u u u u u u u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R TCA2<br>W<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16<br>—|Reserved|
|15-0|Temperature coefficient A2|
|TCA2|seeConversion voltage Temperaturefor the usage of this coefficient|



## 82.4 Glossary 

ADC Analog to digital converter ETS Engineering temperature sensor Vbe Base emitter voltage VETS Engineering temperature sensor voltage VGND Ground voltage 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4617 / 4640 

