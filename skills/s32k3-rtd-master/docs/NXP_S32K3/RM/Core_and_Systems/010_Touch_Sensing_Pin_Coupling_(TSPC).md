NXP Semiconductors 

# Chapter 10 Touch Sensing Pin Coupling (TSPC) 

## 10.1 Chip-specific TSPC information 

### 10.1.1 TSPC instances and configuration 

This chip has one instance of TSPC module. The GPIO pads being used for TSPC should be configured with Source Signal Select (SSS) = 0. TSPC module works in conjunction with SIUL2. 

Table 36. TSPC instances 

|Instance|S32K311/S32K312/S32K322/S32K342/S32K314/S32K324/|
|---|---|
||S32K344/S32K358|
|TSPC|Yes|



For the GPIOs and ADC pads supporting TSPC, see the IOMUX file attached to this document. There are two groups of pads which can be configured via TSPC: 

1. Group 1 consists of 32 ADC channels and 14 GPIOs 

2. Group 2 consists of 32 ADC channels and 6 GPIOs 

- ~~<mark>NOTE</mark>~~ 

Use preferably the same type of I/O pins for driving each electrode. Such I/O pins matching will improve resolution of the capacitance sensing. For more information about types of I/O pins, see the IOMUX file attached to this document. 

## 10.2 Introduction 

TSPC provides simultaneous transitioning of a group of pads into high impedance to support a more robust recognition of touch sense. 

### 10.2.1 Block diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/010_Touch_Sensing_Pin_Coupling_-TSPC-/S32K3XXRM_数据表.pdf-0368-15.png)


<!-- Start of picture text -->
lPS bus<br>TSPC registers lPS bus<br>TSPC logic block<br>Output buffer enable from SIUL2<br>Gated output buffer<br>enable from TSPC<br><!-- End of picture text -->

Figure 21. TSPC block diagram 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

368 / 4640 

NXP Semiconductors 

Touch Sensing Pin Coupling (TSPC) 

### 10.2.2 Features 

TSPC provides a set of control registers for pairing up GPIO pads for the touch sensing pairing operation. These control registers select the set of GPIO pads to pair with the set of ADC channels of an ADC instance. TSPC supports the following features: 

- Up to 512 GPIO pads allow grouping 

- OBE of all the grouped pads transitions from high to low simultaneously if SIUL2 transitions a pad's OBE from high to low 

- Programming of group registers defines grouping 

## 10.3 Logic block 

This block takes the information from register fields to produce gated OBEs. 

The simultaneous transition of grouped OBEs occurs when the GRPn_EN field in Group Enable (GRP_EN) for the respective group becomes 1. 

The logic diagram below shows that if the GRP_EN is high for a particular group, and one of the output buffer enable (ipp_obe_in_b) from SIUL2 belonging to that group transitions from high to low, then all the other output buffer enables belonging to that group also transitions from high to low. If the GRP_EN is set low, the transitions in OBE do not affect the other OBE's belonging to that group. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/010_Touch_Sensing_Pin_Coupling_-TSPC-/S32K3XXRM_数据表.pdf-0369-11.png)


<!-- Start of picture text -->
GRP1_EN ipp_obe_in_b 0 Y ipp_obe_out<br>(GRP_EN from Group Enable register) 1<br>OBE1<br>ipp_obe_in_b SEL0<br>OBE1<br>(OBE from register bits)<br>GRP1_EN<br>(GRP_EN from Group Enable register) ipp_obe_in_b 0 Y ipp_obe_out<br>1<br>ipp_obe_in_b OBE2<br>SEL0<br>OBE2<br>(OBE from register bits)<br>Gated OBEs from TSPC<br>GRP2_EN ipp_obe_in_b 0 Y ipp_obe_out<br>(GRP_EN from Group Enable register) 1<br>OBE1<br>ipp_obe_in_b SEL0<br>OBE1<br>(OBE from register bits)<br>GRP2_EN<br>(GRP_EN from Group Enable register) ipp_obe_in_b 0 Y ipp_obe_out<br>1<br>ipp_obe_in_b OBE2<br>SEL0<br>OBE2<br>(OBE from register bits)<br>Figure 22. Logic block diagram<br><!-- End of picture text -->

## 10.4 Functional description 

TSPC contains these types of registers: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

369 / 4640 

NXP Semiconductors 

Touch Sensing Pin Coupling (TSPC) 

- Group enable: Each field of this register enables the respective group's OBE register—that is, if any OBE within a group transitions from high to low, it enables that group of OBEs for simultaneous transition from high to low. For example, GRP1_EN is the enable field for group 1 OBE registers. The number of fields in this register is equal to the number of groups. 

- Group n OBE register n: The number of registers for a particular group n depends on the number of grouped OBEs in the respective group. For example, if the number of OBEs in group 1 is 36, then two registers of 32 fields each exist. Each field of this register represents an OBE pad. If you write 1 to the field, it indicates the OBE's participation in the grouping. If one of the pad's OBEs transitions from high to low, all the participating OBEs transition from high to low. The remaining OBEs that are not participating in the grouping are not affected. 

The register programming sequence is as follows: 

1. Reset all the registers. 

2. Write 1 to the GRPn_OBEx[OBEn] of the OBEs that participate in grouping. 

3. Program the corresponding group enable field participating in grouping in Group Enable (GRP_EN). 

You must write 0 to the corresponding GRP_EN field when you configure the group n OBE fields. You must write 1 to the OBEn field in Group OBE (GRP1_OBE1 - GRP2_OBE1) and then write 1 to the corresponding GRP_EN field in Group Enable (GRP_EN). 

## 10.5 TSPC register descriptions 

### 10.5.1 TSPC memory map 

TSPC base address: 402C_4000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|Group Enable (GRP_EN)|32|RW|0000_0000h|
|50h|Group OBE (GRP1_OBE1)|32|RW|0000_0000h|
|54h|Group OBE (GRP1_OBE2)|32|RW|0000_0000h|
|A0h|Group OBE (GRP2_OBE1)|32|RW|0000_0000h|
|A4h|Group OBE (GRP2_OBE2)|32|RW|0000_0000h|



### 10.5.2 Group Enable (GRP_EN) 

#### Offset 

|Register|Offset|
|---|---|
|GRP_EN|0h|



#### Function 

Allows enabling of the group, the pads of which participate in simultaneous transition. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

370 / 4640 

NXP Semiconductors 

Touch Sensing Pin Coupling (TSPC) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||||0||||||||GRP2_|GRP1_|
|W|||||||||||||||EN|EN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-2|Reserved|
|—||
|1|Enable for GRP2_OBEn Register|
|GRP2_EN|Enables or disables the GRP2_OBEn register that participates in grouping.<br>0b - Disable|
||1b - Enable|
|0|Enable for GRP1_OBEn Register|
|GRP1_EN|Enables or disables the GRP1_OBEn register that participates in grouping.<br>0b - Disable<br>1b - Enable|



### 10.5.3 Group OBE (GRP1_OBE1 - GRP2_OBE1) 

#### Offset 

|Register|Offset|
|---|---|
|GRP1_OBE1|50h|
|GRP2_OBE1|A0h|



#### Function 

Allows grouping of OBEs in the respective group. Each field corresponds to an OBE pad. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

371 / 4640 

NXP Semiconductors 

Touch Sensing Pin Coupling (TSPC) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/010_Touch_Sensing_Pin_Coupling_-TSPC-/S32K3XXRM_数据表.pdf-0372-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R OBE3 OBE3 OBE2 OBE2 OBE2 OBE2 OBE2 OBE2 OBE2 OBE2 OBE2 OBE2 OBE1 OBE1 OBE1 OBE1<br>W 1  0  9  8  7  6  5  4  3  2  1  0  9  8  7  6<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R OBE1 OBE1 OBE1 OBE1 OBE1 OBE1<br>OBE9  OBE8  OBE7  OBE6  OBE5  OBE4  OBE3  OBE2  OBE1  OBE0<br>W 5  4  3  2  1  0<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-0|Output Buffer Enable|
|OBEn|Indicates if a particular OBE participates in grouping.|
||0b - OBE pad does not transition if any OBE in group transitions from high to low. The OBE pad<br>value is unaltered at the output.|
||1b - OBE pad transitions from high to low if any OBE in group transitions from high to low.|



### 10.5.4 Group OBE (GRP1_OBE2) 

#### Offset 

|Register|Offset|
|---|---|
|GRP1_OBE2|54h|



#### Function 

Allows grouping of OBEs in the respective group. Each field corresponds to an OBE pad. 

#### Diagram 

|Bits|31||30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||||0||||||||
|W||||||||||||||||||
|Reset|0||0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15||14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||0||OBE4|OBE4|OBE4|OBE4|OBE4|OBE4|OBE3|OBE3|OBE3|OBE3|OBE3|OBE3|OBE3|OBE3|
|W||||5|4|3|2|1|0|9|8|7|6|5|4|3|2|
|Reset|0||0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

372 / 4640 

NXP Semiconductors 

Touch Sensing Pin Coupling (TSPC) 

#### Fields 

|Field|Function|
|---|---|
|31-14<br>—|Reserved|
|13|Output Buffer Enable|
|OBE45|Indicates if a particular OBE participates in grouping.<br>0b - OBE pad does not transition if any OBE in group transitions from high to low. The OBE pad<br>value is unaltered at the output.<br>1b - OBE pad transitions from high to low if any OBE in group transitions from high to low.|
|12|Output Buffer Enable|
|OBE44|Indicates if a particular OBE participates in grouping.<br>0b - OBE pad does not transition if any OBE in group transitions from high to low. The OBE pad<br>value is unaltered at the output.<br>1b - OBE pad transitions from high to low if any OBE in group transitions from high to low.|
|11|Output Buffer Enable|
|OBE43|Indicates if a particular OBE participates in grouping.<br>0b - OBE pad does not transition if any OBE in group transitions from high to low. The OBE pad<br>value is unaltered at the output.<br>1b - OBE pad transitions from high to low if any OBE in group transitions from high to low.|
|10|Output Buffer Enable|
|OBE42|Indicates if a particular OBE participates in grouping.<br>0b - OBE pad does not transition if any OBE in group transitions from high to low. The OBE pad<br>value is unaltered at the output.<br>1b - OBE pad transitions from high to low if any OBE in group transitions from high to low.|
|9|Output Buffer Enable|
|OBE41|Indicates if a particular OBE participates in grouping.<br>0b - OBE pad does not transition if any OBE in group transitions from high to low. The OBE pad<br>value is unaltered at the output.<br>1b - OBE pad transitions from high to low if any OBE in group transitions from high to low.|
|8|Output Buffer Enable|
|OBE40<br>7|Indicates if a particular OBE participates in grouping.<br>0b - OBE pad does not transition if any OBE in group transitions from high to low. The OBE pad<br>value is unaltered at the output.<br>1b - OBE pad transitions from high to low if any OBE in group transitions from high to low.<br>Output Buffer Enable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

373 / 4640 

NXP Semiconductors 

Touch Sensing Pin Coupling (TSPC) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|OBE39|Indicates if a particular OBE participates in grouping.<br>0b - OBE pad does not transition if any OBE in group transitions from high to low. The OBE pad<br>value is unaltered at the output.<br>1b - OBE pad transitions from high to low if any OBE in group transitions from high to low.|
|6|Output Buffer Enable|
|OBE38|Indicates if a particular OBE participates in grouping.<br>0b - OBE pad does not transition if any OBE in group transitions from high to low. The OBE pad<br>value is unaltered at the output.<br>1b - OBE pad transitions from high to low if any OBE in group transitions from high to low.|
|5|Output Buffer Enable|
|OBE37|Indicates if a particular OBE participates in grouping.<br>0b - OBE pad does not transition if any OBE in group transitions from high to low. The OBE pad<br>value is unaltered at the output.<br>1b - OBE pad transitions from high to low if any OBE in group transitions from high to low.|
|4|Output Buffer Enable|
|OBE36|Indicates if a particular OBE participates in grouping.<br>0b - OBE pad does not transition if any OBE in group transitions from high to low. The OBE pad<br>value is unaltered at the output.<br>1b - OBE pad transitions from high to low if any OBE in group transitions from high to low.|
|3|Output Buffer Enable|
|OBE35|Indicates if a particular OBE participates in grouping.<br>0b - OBE pad does not transition if any OBE in group transitions from high to low. The OBE pad<br>value is unaltered at the output.<br>1b - OBE pad transitions from high to low if any OBE in group transitions from high to low.|
|2|Output Buffer Enable|
|OBE34|Indicates if a particular OBE participates in grouping.<br>0b - OBE pad does not transition if any OBE in group transitions from high to low. The OBE pad<br>value is unaltered at the output.<br>1b - OBE pad transitions from high to low if any OBE in group transitions from high to low.|
|1|Output Buffer Enable|
|OBE33|Indicates if a particular OBE participates in grouping.<br>0b - OBE pad does not transition if any OBE in group transitions from high to low. The OBE pad<br>value is unaltered at the output.<br>1b - OBE pad transitions from high to low if any OBE in group transitions from high to low.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

374 / 4640 

NXP Semiconductors 

Touch Sensing Pin Coupling (TSPC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|0|Output Buffer Enable|
|OBE32|Indicates if a particular OBE participates in grouping.|
||0b - OBE pad does not transition if any OBE in group transitions from high to low. The OBE pad<br>value is unaltered at the output.|
||1b - OBE pad transitions from high to low if any OBE in group transitions from high to low.|



### 10.5.5 Group OBE (GRP2_OBE2) 

#### Offset 

|Register|Offset|
|---|---|
|GRP2_OBE2|A4h|



#### Function 

Allows grouping of OBEs in the respective group. Each field corresponds to an OBE pad. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Core_and_Systems/010_Touch_Sensing_Pin_Coupling_-TSPC-/S32K3XXRM_数据表.pdf-0375-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>OBE37 OBE36 OBE35 OBE34 OBE33 OBE32<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-6|Reserved|
|—||
|5|Output Buffer Enable|
|OBE37|Indicates if a particular OBE participates in grouping.|
||0b - OBE pad does not transition if any OBE in group transitions from high to low. The OBE pad<br>value is unaltered at the output.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

375 / 4640 

NXP Semiconductors 

Touch Sensing Pin Coupling (TSPC) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - OBE pad transitions from high to low if any OBE in group transitions from high to low.|
|4|Output Buffer Enable|
|OBE36|Indicates if a particular OBE participates in grouping.<br>0b - OBE pad does not transition if any OBE in group transitions from high to low. The OBE pad<br>value is unaltered at the output.<br>1b - OBE pad transitions from high to low if any OBE in group transitions from high to low.|
|3<br>OBE35|Output Buffer Enable<br>Indicates if a particular OBE participates in grouping.<br>0b - OBE pad does not transition if any OBE in group transitions from high to low. The OBE pad<br>value is unaltered at the output.<br>1b - OBE pad transitions from high to low if any OBE in group transitions from high to low.|
|2|Output Buffer Enable|
|OBE34|Indicates if a particular OBE participates in grouping.<br>0b - OBE pad does not transition if any OBE in group transitions from high to low. The OBE pad<br>value is unaltered at the output.<br>1b - OBE pad transitions from high to low if any OBE in group transitions from high to low.|
|1<br>OBE33|Output Buffer Enable<br>Indicates if a particular OBE participates in grouping.<br>0b - OBE pad does not transition if any OBE in group transitions from high to low. The OBE pad<br>value is unaltered at the output.<br>1b - OBE pad transitions from high to low if any OBE in group transitions from high to low.|
|0|Output Buffer Enable|
|OBE32|Indicates if a particular OBE participates in grouping.<br>0b - OBE pad does not transition if any OBE in group transitions from high to low. The OBE pad<br>value is unaltered at the output.<br>1b - OBE pad transitions from high to low if any OBE in group transitions from high to low.|



## 10.6 Glossary 

GPIO General purpose input and output OBE Output buffer enable 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

376 / 4640 

