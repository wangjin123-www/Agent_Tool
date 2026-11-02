NXP Semiconductors 

# Chapter 57 Power Conversion and Motor Control (PCMC) 

## 57.1 Introduction 

The PCMC subsystem is a group of modules that can be interconnected to perform a variety of real-time tasks, such as: 

- Motor control 

- Power conversion 

- Advanced PWM generation 

- Lighting control 

The modules that make up PCMC are: 

- ADC 

- BCTU 

- eMIOS 

- LCU 

- LPCMP 

- TRGMUX 

See Feature comparison for the number of instances of each module in your chip. 

## 57.2 Block diagram 

The figure and table below show a typical configuration. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1879 / 4640 

NXP Semiconductors 

Power Conversion and Motor Control (PCMC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/057_Power_Conversion_and_Motor_Control_-PCMC-/S32K3XXRM_数据表.pdf-1880-02.png)


<!-- Start of picture text -->
Digital<br>outputs<br>S32K3xx<br>Control action<br>eMIOS LCU<br>LPCMP<br>TRGMUX<br>Control Analog<br>processing feedback<br>Analog<br>BCTU inputs<br>ADC<br>eMIOS<br>Digital<br>inputs<br>TRGMUX<br>Digital feedback<br>and faults<br>LCU LPCMP<br><!-- End of picture text -->

Figure 208. Block diagram 

##### Table 273. Block diagram components 

|Component|Description|
|---|---|
|ADC|Measures external analog signals|
|BCTU|Performs advanced ADC triggering|
|Control processing|Arm Cortex-M7 core:<br>• Processes digital and analog inputs to generate control outputs<br>• Writes control outputs to peripherals|
|eMIOS|• Generates high-resolution PWM outputs<br>• Measures time-based digital inputs|
|LCU|Performs programmable logic functions and fault control|
|LPCMP|Compares analog values to detect faults|
|TRGMUX|• Routes signals between internal peripherals<br>• Routes external signals to internal peripherals|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1880 / 4640 

NXP Semiconductors 

Power Conversion and Motor Control (PCMC) 

## 57.3 Functional overview 

### 57.3.1 Analog signal measurement 

ADC measures the voltage of external analog signals and converts that voltage to a digital value. Each ADC instance operates independently of other instances. Software or hardware can trigger conversions. Together with BCTU and eMIOS, ADC can preempt normal measurements by injecting high-priority measurements when needed. 

See Analog-to-Digital Converter. 

### 57.3.2 Advanced ADC triggering 

BCTU works with ADC to initiate conversions triggered by outputs from other modules in the PCMC subsystem, such as PWM signals from eMIOS or LCU sequential logic outputs. 

With BCTU, you can group measurements into configuration lists containing up to 32 items. Each item contains information such as: 

- ADC instance to use for the conversion 

- The ADC channel 

- The trigger event for initiating the next conversion 

- The conversion list address 

BCTU can store conversion results by routing them through DMA or putting them in FIFO queues. The FIFO queues enable conversions to occur seamlessly by storing conversion results without software intervention. 

BCTU has 72 trigger inputs, 69 of which come from the eMIOS channel outputs. The three remaining trigger inputs come from other on-chip modules via TRGMUX. You can also trigger conversions by software through the BCTU register interface. 

BCTU can issue a single conversion or a list of conversions based on a single trigger occurrence. BCTU signals the eMIOS timers when ADC receives a single command or a list of commands. ADC sends conversion data back to BCTU, which loads it in the ADCn Result Data (ADCnDR) register for the CPU to read. 

BCTU-to-ADC interface illustrates the connections between BCTU and an ADC. 

See also: 

- Body cross-triggering unit (BCTU) 

- PCDRn, ICDRn, and ECDRn register descriptions in ADC register descriptions 

### 57.3.3 BCTU-to-ADC interface 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/057_Power_Conversion_and_Motor_Control_-PCMC-/S32K3XXRM_数据表.pdf-1881-21.png)


<!-- Start of picture text -->
triggers<br>channel number<br>next command<br>end of conversion<br>BCTU conversion data ADC0-2 IO MUX<br>eMIOS<br>eDMA<br>eMIOS<br>TRGMUX TRGMUX TRGMUX<br>eDMA<br>CORE_CLK<br><!-- End of picture text -->

Figure 209. BCTU-to-ADC interface 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1881 / 4640 

NXP Semiconductors 

Power Conversion and Motor Control (PCMC) 

### 57.3.4 Generate PWM outputs and measure digital inputs 

eMIOS generates high-resolution PWM outputs. Each eMIOS instance has 23 dedicated channel outputs. You can configure each channel to operate in a different mode. Depending on the mode, eMIOS channels can: 

- Measure the period of an input signal 

- Measure the width of an input pulse 

- Function as general-purpose I/O 

- Count pulses or edges 

- Capture input values 

- Compare outputs 

For example, eMIOS can generate periodic ADC triggers. Using TRGMUX, you can route eMIOS triggers to other on-chip peripherals such as LCU, another eMIOS instance, external chip I/O, and so on. 

eMIOS connections illustrates the input and output connections for eMIOS. 

See also: 

- Enhanced Modular IO Subsystem (eMIOS) 

- Body cross-triggering unit (BCTU) 

- Trigger Mux (TRGMUX) 

### 57.3.5 eMIOS connections 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/057_Power_Conversion_and_Motor_Control_-PCMC-/S32K3XXRM_数据表.pdf-1882-17.png)


<!-- Start of picture text -->
From TRGMUX To BCTU<br>eMIOS0-2 To TRGMUX<br>CORE_CLK IO MUX<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/057_Power_Conversion_and_Motor_Control_-PCMC-/S32K3XXRM_数据表.pdf-1882-18.png)


<!-- Start of picture text -->
Figure 210. eMIOS connections<br><!-- End of picture text -->

### 57.3.6 Create combinatorial and sequential logic functions 

LCU enables you to implement hardware-based combinatorial and sequential logic on the chip. This capability reduces cost and decreases application size. 

Each LCU instance has 12 dedicated inputs and 12 outputs. You can use LCU to implement a variety of combinatorial and sequential logic functions with no CPU intervention, including a simple OR gate, flip flops, and motor control logic. As detailed in Fault detection, LCU also plays a significant role in fault management. 

LCU connections shows the input and output connections for LCU. 

See also: 

- Logic Control Unit (LCU) 

- LCU use case examples 

- Trigger MUX (TRGMUX) 

- TRGMUX connectivity file attached to this document 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1882 / 4640 

NXP Semiconductors 

Power Conversion and Motor Control (PCMC) 

### 57.3.7 LCU connections 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/057_Power_Conversion_and_Motor_Control_-PCMC-/S32K3XXRM_数据表.pdf-1883-03.png)


<!-- Start of picture text -->
From TRGMUX To TRGMUX<br>LCU0-1<br>CORE_CLK IO MUX<br><!-- End of picture text -->

Figure 211. LCU connections 

### 57.3.8 Fault detection 

The PCMC subsystem uses LPCMP and LCU to implement fault detection. 

LPCMP can detect fault conditions (such as short circuits, over-voltages, and excessive temperature) by comparing an external input voltage to a programmable reference voltage. It produces a digital output that indicates whether the input voltage is higher or lower than the reference voltage. 

The chip can detect faults via external digital or analog signals. TRGMUX routes digital signals from SIUL to a peripheral to trigger the appropriate behavior. 

LCU has four force inputs that you can use to manage fault assertion via its own internal logic mechanism. 

The typical reaction to the presence of fault is to put the system in a safe state by: 

- Deasserting output signals such as PWM outputs controlling a power stage. 

- Disconnecting an entire circuit by switching off a relay. 

See also Low Power Comparator (LPCMP). 

### 57.3.9 Programmable module interconnections 

TRGMUX enables you to interconnect on-chip peripherals to create application-specific configurations. TRGMUX has 128 inputs and 111 outputs, which you can interconnect in hundreds of combinations through software during runtime. 

You can also route on-chip peripheral outputs to chip I/O pins to enable signal debugging. Similarly, you can route external signals to on-chip peripheral inputs. 

~~<mark>NOTE</mark>~~ There is a two-cycle AIPS_SLOW_CLK delay through TRGMUX. 

For details of PCMC interconnections, see PCMC connections diagram. 

The attached TRGMUX connectivity file, a portion of which appears below, shows the interconnections possible between module instances. Column B in the spreadsheet lists TRGMUX inputs. Row 3 lists TRGMUX outputs. A connection between an input and an output is possible if the intersecting cell of the input row and the output column is blank. "NA" indicates that a connection is not possible. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1883 / 4640 

NXP Semiconductors 

Power Conversion and Motor Control (PCMC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/057_Power_Conversion_and_Motor_Control_-PCMC-/S32K3XXRM_数据表.pdf-1884-02.png)


Figure 212. Portion of TRGMUX connectivity 

See also: 

- Trigger Mux (TRGMUX) 

- TRGMUX connectivity file attached to this document 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1884 / 4640 

NXP Semiconductors 

Power Conversion and Motor Control (PCMC) 

#### 57.3.9.1 PCMC connections diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/057_Power_Conversion_and_Motor_Control_-PCMC-/S32K3XXRM_数据表.pdf-1885-03.png)


<!-- Start of picture text -->
triggers<br>channel number<br>next command<br>ADC mux outputs<br>eMIOSeMIOS n n  channel [0:22]clear [0:22] BCTU conversion dataend of conversion ADC0-2 ADC std/prec/ext inputs } IO MUX<br>eDMA<br>BCTU_Trg23,47,71 CORE_CLK<br>ADC12_ n _EOC<br>CORE_CLK<br>ADC12_ n _EXTRG for normal conversion eDMA<br>ADC12_ n _EXTRG for injected conversion<br>ADC12_ n _EXTRG for sync conversion<br>eMIOS_ n _CH[0:23]_[GHXY]<br>IO MUX<br>eMIOS_CORE_CLK n _ipp_ind_emios_ch[ ] eMIOS0-2 eMIOS_eMIOS_ nn _ipp_do_emios_ch[ ]_reload_out_ch[ ] RT LPCMP, FlexIO, LPI2C, LPUART<br>eMIOS_0_1_2_emios_odis[0:3] G SIUL2_TRGMUX_OUT0-15 (IO MUX)<br>eDMA, FlexIO, LPI2C, M<br>LPSPI, LPUART, PIT, LPCMP U<br>X<br>SIUL_TRGMUX_IN0-15 (IO MUX)<br>AIPS_SLOW_CLK<br>CORE_CLK LCU_ n _lcm_out_i[1:4]<br>LCU_ n _Icm_inp_i[1:4] LCU0-1<br>LCU_ n _force[1:3]<br>LCU_ n _sync[1:2] LCU n _OUT[0:11] IO MUX<br><!-- End of picture text -->

Figure 213. PCMC connections diagram 

## 57.4 Reset, clocking, and other considerations 

### 57.4.1 Reset 

ADC, BCTU, eMIOS, LCU, and TRGMUX fully reset during a POR, destructive reset, or functional reset. 

See also: 

- Module reset status 

- Software reset 

### 57.4.2 Clocking 

Detailed clocking information is given in the links below. In summary: 

- CORE_CLK clocks ADC, BCTU, eMIOS, and LCU. 

- AIPS_SLOW_CLK clocks TRGMUX. 

- In general, you must set AIPS_SLOW_CLK to one-fourth or one-half the frequency of CORE_CLK. 

See also: 

- ADC and motor control modules 

- System clocking configurations 

- System clock frequency limitations 

- Clock frequency 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1885 / 4640 

NXP Semiconductors 

Power Conversion and Motor Control (PCMC) 

### 57.4.3 Power modes 

All ADC, BCTU, eMIOS, LCU, and TRGMUX instances operate only in Run mode. None of the instances operate in Standby mode. 

See also: 

- Module reset status 

- ADC modes of operation 

- LCU modes of operation 

## 57.5 Use case examples 

### 57.5.1 Motor control use case 

The following sections show: 

- A PMSM control system 

- A BLDC control system 

Both PMSM and BLDC use a rotating magnetic stator field to turn the stator consisting of permanent magnets. The stator is driven by 3-phase AC voltage. The difference between PMSM and BLDC is in how stator position is calculated. 

- PMSM calculates stator position by measuring back EMF from the motor. 

- BLDC calculates stator position based on feedback from motor sensors. 

#### 57.5.1.1 PMSM motor control use case 

#### 57.5.1.1.1 Generic PMSM motor control 

The following figure and table illustrate a generic PMSM motor control system. The feedback loops in the system create a motor control loop. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/057_Power_Conversion_and_Motor_Control_-PCMC-/S32K3XXRM_数据表.pdf-1886-19.png)


<!-- Start of picture text -->
Commutation<br>logic<br>Reference<br>signal<br>Control<br>a<br>Motor control signal PWM signal DC-to-3-phase b Brushless Speed and back<br>logic generator inverter DC motor EMF measurement<br>c<br><!-- End of picture text -->

Figure 214. Generic PMSM motor control 

Table 274. Block diagram components 

|Block|Description|
|---|---|
|Angular position sensor|Generates data that enables commutation logic to calculate rotor position.|
|Brushless DC motor|Electronically commutated electric motor.|
|Commutation logic|Compares values from the rotor angular position sensors to entries in a lookup<br>table, and applies voltage to stator winding corresponding to same set of values in<br>lookup table.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1886 / 4640 

NXP Semiconductors 

Power Conversion and Motor Control (PCMC) 

Table 274. Block diagram components (continued) 

|Block|Description|
|---|---|
|DC-to-3-phase inverter|Switching network that transmits power to the motor stator windings according to a<br>control signal.|
|Motor control logic|• Compares speed measurement to required speed and adjusts the PWM<br>signal generator.|
||• Generates the assertions for the PWM signal generator according to<br>commutation logic input.|
|PWM signal generator|Generates PWM signal voltage source.|
|Reference signal|Signal that indicates required motor speed.|
|Speed and back EMF measurement|An ADC is linked to a shunt resistor to perform measurements and detect over-<br>current conditions. If one is found, then hardware generates a fault interrupt.|



#### 57.5.1.1.2 PMSM motor control 

The PCMC subsystem consists of a group of modules that enable you to implement PMSM motor control loops in a variety of ways. The following figure and table illustrate one possible implementation. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/057_Power_Conversion_and_Motor_Control_-PCMC-/S32K3XXRM_数据表.pdf-1887-06.png)


<!-- Start of picture text -->
S32K3xx PWM<br>signals a<br>LCU eMIOS DC-to-3-phase b Brushless<br>inverter chip DC motor<br>c<br>Control process<br>TRGMUX<br>implemented in<br>software or firmware<br>eMIOS BCTU<br>ADC Back EMF<br>Feedback<br>measurement<br>Digital feedback<br>Analog feedback<br><!-- End of picture text -->

Figure 215. PMSM motor control 

Table 275. Block diagram components 

|Block|Description|
|---|---|
|ADC|Measures analog inputs (currents and/or voltages) and converts to digital values.<br>Typically, it measures currents and can be configured to generate a fault interrupt<br>when a measured input is outside a pre‑defined acceptable range.|
|BCTU|Triggers conversions by ADC.|
|Control process|Provides top-level system control functions forFOCor another feasible<br>control algorithm:|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1887 / 4640 

NXP Semiconductors 

Power Conversion and Motor Control (PCMC) 

Table 275. Block diagram components (continued) 

|Block|Description|
|---|---|
||• Compares speed measurement to required speed and adjusts the PWM<br>signal generator.<br>• Generates the assertions for the PWM signal generator according to<br>commutation logic input.|
|DC-to-3-phase inverter|Switching network that transmits power to the motor stator windings according to a<br>control signal.|
|eMIOS|• Generates PWM input for DC to 3-phase inverter.<br>• Measures digital feedback inputs—BLDC position sensors, for example.|
|LCU|Implements commutation lookup table. Control Process compares values from the<br>angular position sensors to entries in the lookup table. It then applies voltage to stator<br>winding corresponding to same set of values in lookup table.|
|TRGMUX|• Enables interconnect to the required set of on-chip peripherals.<br>• Indirectly triggers ADC sampling via BCTU.<br>• Triggers eMIOS to measure digital feedback signals.|



#### 57.5.1.2 Sensored BLDC motor control use case 

#### 57.5.1.2.1 Generic sensored BLDC motor control 

The following figure and table illustrate a generic sensored BLDC motor control system. The feedback loops in the system create a motor control loop. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/057_Power_Conversion_and_Motor_Control_-PCMC-/S32K3XXRM_数据表.pdf-1888-07.png)


<!-- Start of picture text -->
Commutation<br>logic<br>Reference Angular<br>position<br>signal<br>Control sensor<br>a<br>Motor control signal PWM signal DC-to-3-phase b Brushless<br>logic generator inverter DC motor<br>c<br>Speed<br>measurement<br><!-- End of picture text -->

Figure 216. Generic sensored BLDC motor control 

Table 276. Block diagram components 

|Block|Description|
|---|---|
|Angular position sensor|Hall effect sensors or optical decoders detect rotor position|
|Commutation logic|Compares values from the angular position sensors to entries in a lookup table and<br>applies voltage to stator winding corresponding to same set of values in lookup table|
|Reference signal|Signal that indicates required motor speed|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1888 / 4640 

NXP Semiconductors 

Power Conversion and Motor Control (PCMC) 

Table 276. Block diagram components (continued) 

|Block|Description|
|---|---|
|DC-to-3-phase inverter|Switching network that transmits power to the stator windings according to a<br>control signal|
|Motor control logic|• Compares speed measurement to required speed and adjusts the PWM<br>signal generator|
||• Generates the assertions for the PWM signal generator according to<br>commutation logic input|
|Speed measurement|Uses an ADC linked to a shunt resistor to perform measurements and detect<br>over-current conditions, in which case hardware generates an interrupt.|



#### 57.5.1.2.2 PCMC sensored field-oriented control (FOC) of 3-phase BLDC motor 

FOC is a VFD control method in which the stator currents of a 3-phase AC electric motor (such as BLDC, PMCM, reluctance motor, or other spinning electrical machine) is identified as a vector. 

The PCMC subsystem consists of a group of modules that enable you to implement sensored FOC BLDC motor control loops in a variety of ways. The following figure and table show one possible implementation. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/057_Power_Conversion_and_Motor_Control_-PCMC-/S32K3XXRM_数据表.pdf-1889-07.png)


<!-- Start of picture text -->
S32K3xx PWM<br>signals a<br>LCU eMIOS DC-to-3-phase b Brushless<br>inverter chip DC motor<br>c<br>Control process<br>TRGMUX<br>implemented in<br>software or firmware<br>eMIOS BCTU<br>ADC<br>Feedback<br>measurement<br>Digital feedback<br>Analog feedback<br><!-- End of picture text -->

Figure 217. PCMC sensored BLDC motor control 

Table 277. Block diagram components 

|Block|Description|
|---|---|
|ADC|Measures analog inputs (currents and/or voltages) and converts to digital values.<br>Typically, it measures currents, and can be configured to generate a fault interrupt<br>when a measured input is outside a pre-defined acceptable range.|
|BCTU|Triggers conversions by ADC.|
|Control process|Provides top-level system control functions for FOC control:|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1889 / 4640 

NXP Semiconductors 

Power Conversion and Motor Control (PCMC) 

Table 277. Block diagram components (continued) 

|Block|Description|
|---|---|
||• Compares speed measurement to required speed and adjusts the PWM<br>signal generator.<br>• Generates the assertions for the PWM signal generator according to<br>commutation logic input.|
|DC-to-3-phase inverter|Switching network that transmits power to the motor stator windings according to a<br>control signal.|
|eMIOS|• Generates PWM input for DC to 3-phase inverter.<br>• Measures digital feedback inputs—BLDC position sensors, for example.|
|LCU|Implements commutation lookup table. Control process compares values from the<br>angular position sensors to entries in the lookup table. It then applies voltage to stator<br>winding corresponding to same set of values in lookup table.|
|TRGMUX|• Enables interconnect of the required set on on-chip peripherals.<br>• Indirectly triggers ADC sampling via BCTU.<br>• Triggers eMIOS to measure digital feedback signals.|



## 57.6 Design considerations 

### 57.6.1 ADC design considerations 

The following topics discuss factors that affect ADC function in applications. 

#### 57.6.1.1 ADC measurement accuracy 

The FOC motor control algorithm requires a high degree of confidence in the reliability of conversion data. Here are some best practices that contribute to ADC precision. 

- Use precision channels (see ADC precision channels). 

- Minimize input noise (see ADC input noise). 

- Use BCTU triggering (see ADC triggering). 

#### 57.6.1.1.1 ADC precision channels 

See the chip-specific ADC configuration information for the number of precision channels for each ADC instance. 

See the channel mapping table for the channel numbers for the precision channels. 

#### 57.6.1.1.2 ADC input noise 

Regardless of the application, ADCs are inherently sensitive to input noise. The following best practices help minimize input noise. 

- Avoid simultaneous conversions. 

- Consider using a low-pass filter on input pins. 

All variants of this chip include multiple, independent ADC instances, so it is easily possible to have simultaneous sampling by different ADC instances. This should be avoided, though, because ADC sampling can cause noise on adjacent device ADC inputs. Avoidance of simultaneous sampling should be ensured by software design. This is important for implementations of the FOC algorithm. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1890 / 4640 

NXP Semiconductors 

Power Conversion and Motor Control (PCMC) 

Additionally, an RC low-pass filter on ADC input pins can help reduce noise and enhance accuracy. 

#### 57.6.1.1.3 ADC triggering 

Some applications, including FOC motor control, must use BCTU for precise triggering of ADC measurement. This is because the FOC algorithm requires sampling at specific times to implement the “observer/predictor”. BCTU makes it possible to perform precisely-timed ADC measurement. 

For less exigent algorithms or non-closed-loop controlled motors, BCTU triggering and precision ADC channels are not necessarily required. 

#### 57.6.1.2 Example ADC configurations 

Following are some ADC configurations that might be used for FOC motor control. 

Table 278. Example ADC configurations 

|Description|Settings|
|---|---|
|Single-shot mode|• Enable Overwrite (OWREN=1)<br>• Disable Write Left-Aligned (WLSIDE=0)<br>• Select single shot (MODE=0)<br>• Disable External Trigger (TRGEN=0)<br>• Disable Injection Trigger (JTRGEN=0)<br>• Disable BCTU triggering (BCTUEN=0)<br>• Disable averaging (AVGEN=0)<br>• Select conversion clock = 1/2 module clock (ADCCLKSEL=01)|
|Normal conversion scan mode|• Enable Overwrite (OWREN=1)<br>• Disable Write Left-Aligned (WLSIDE=0)<br>• Select looped conversions (MODE=1)<br>• Disable External Trigger (TRGEN=0)<br>• Disable Injection Trigger (JTRGEN=0)<br>• Disable BCTU triggering (BCTUEN=0)<br>• Disable averaging (AVGEN=0)<br>• Select conversion clock = 1/2 module clock (ADCCLKSEL=01)|
|BCTU control mode|• Enable Overwrite (OWREN=1)<br>• Disable Write Left-Aligned (WLSIDE=0)<br>• Select single shot (MODE=0)<br>• Disable External Trigger (TRGEN=0)<br>• Disable Injection Trigger (JTRGEN=0)<br>• Enable BCTU triggering (BCTUEN=1)<br>• Disable averaging (AVGEN=0)<br>• Select conversion clock = 1/2 module clock (ADCCLKSEL=01)|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

1891 / 4640 

NXP Semiconductors 

Power Conversion and Motor Control (PCMC) 

Table 278. Example ADC configurations (continued) 

|Description|Settings|
|---|---|
|BCTU trigger mode|• Enable Overwrite (OWREN=1)<br>• Disable Write Left-Aligned (WLSIDE=0)<br>• Select single shot (MODE=0)<br>• Disable External Trigger (TRGEN=0)<br>• Disable Injection Trigger (JTRGEN=0)<br>• Enable BCTU triggering (BCTUEN=1)<br>• Enable all trigger sources (BCTU_MODE=1)<br>• Disable averaging (AVGEN=0)<br>• Select conversion clock = 1/2 module clock (ADCCLKSEL=01)|



### 57.6.2 BCTU design considerations 

For reasons discussed in ADC triggering, some applications require precise ADC triggering and BCTU provides that capability. The following topics discuss some design considerations when using BCTU. 

#### 57.6.2.1 BCTU or ADC data retrieval 

Although the primary function of BCTU is to provide precisely timed triggers for ADC conversions, there is some overlap in BCTU and ADC function in that conversion data can be retrieved from either module. For applications in which frequent conversions are performed, such as real-time motor control, BCTU offers a distinct advantage over ADC, because BCTU trigger sources can be configured to route conversion results to a BCTU internal FIFO. Doing so prevents subsequent conversion data from overwriting previous data, making it available for either direct access or DMA transfer to system RAM. 

#### 57.6.2.2 Disabling BCTU triggers 

There are fault scenarios in which an application must disable BCTU triggers as part of putting the system into a safe state. Examples include: 

- Over-voltage condition 

- Under-voltage condition 

- Calibration parameter mismatch between the embedded motor control system and the motor 

Application fault reaction design must include the disabling of BCTU triggers in scenarios in which either system conditions indicate an impending failure, or ADC conversion data is outside control boundaries. 

### 57.6.3 eMIOS design considerations 

In a BLDC motor control application, eMIOS plays a central role, providing the driving PWM signal as well as performing feedback signal measurements. The following topics discuss eMIOS considerations in the application design. 

#### 57.6.3.1 PWM considerations 

In a BLDC motor control application, PWM/power signal requirements are affected by a number of parameters, including: 

- Displacement Power Factor 

- DF 

- THD 

- DVA 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1892 / 4640 

NXP Semiconductors 

Power Conversion and Motor Control (PCMC) 

- CF 

- FF 

Ensure that the above parameters are included when choosing the timebase and prescaler combination for eMIOS channels producing PWM signals. 

#### 57.6.3.2 Input measurement 

In a BLDC motor control application, eMIOS measures feedback signals for the motor and provides critical information to the control system. Selecting a timebase and prescaler for eMIOS channels performing input measurement tasks is usually a tradeoff between application requirements for precision and the computational cost in relation to the selected clock speed. 

For example, some applications like electric steering demand an extremely precise control for position and torque. This is different from a compressor e-motor, where speed and torque do not demand rigid precision requirements. 

Other considerations are related to control of: 

- THD 

- FF 

- GM 

- pf correction 

The above considerations are significant from the perspective of the PWM reaction speed for the output signal for BLDC applications. These parameters must be considered in the design. 

#### 57.6.3.3 eMIOS channel modes useful in motor control 

Table 279. eMIOS channel modes useful in motor control 

|Mode|Description|Use in motor control|
|---|---|---|
|MCB|Modulus Counter Buffered (Up/Down)|Time base<br>• PWM frequency<br>• Reload|
|IPWM|Input Pulse Width Measurement|Capture modes:<br>• Speed measurement<br>• Position measurement<br>• Voltage (duty cycle)|
|IPM|Input Period Measurement|Speed measurement|
|PEC|Pulse Edge Counting|Position measurement|
|OPWMCB|Center aligned Output PWM Buffered with dead time|PWM duty cycle|
|OPWMB|Output Pulse Width Modulation Buffered|Trigger placement within the period|
|OPWMT|Output Pulse Width Modulation Trigger|Trigger placement within the period|



#### 57.6.3.3.1 MCB PWM and trigger generation 

The following figure shows one option for PWM and trigger generation. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1893 / 4640 

NXP Semiconductors 

Power Conversion and Motor Control (PCMC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/057_Power_Conversion_and_Motor_Control_-PCMC-/S32K3XXRM_数据表.pdf-1894-02.png)


<!-- Start of picture text -->
Channel 0 A n Channel 0 - MCB up down<br>Channel 1 A n<br>Modulo (channel 0 A n  register) is double-buffered<br>Channel 2 A n and updated after a reload signal.<br>Channel 3 A n Duty cycle is double-buffered (A n  registers for channels<br>1, 2, and 3) and updated after a reload signal.<br>Reload<br>Channel 1- OPWMCB<br>(ADC trigger)<br>Channel 2 - OPWMCB<br>Channel 3 - OPWMCB<br>Channel 0  counter<br> output<br>Channel 1<br>  output<br>Channel 2<br>  output<br>Channel 3<br><!-- End of picture text -->

Figure 218. MCB PWM trigger generation 

#### 57.6.3.3.2 OPWMCB PWM and trigger generation 

The following figure shows another option for PWM and trigger generation. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/057_Power_Conversion_and_Motor_Control_-PCMC-/S32K3XXRM_数据表.pdf-1894-06.png)


<!-- Start of picture text -->
Channel 0 A n Channel 0 - MCB up<br>Channel 4 B n<br>Channel 3 B n<br>Channel 2 B n Modulo (channel 0 A n  register) is double-buffered<br>Channel 1 B n and updated after a reload signal.<br>Channel 4 A n<br>Channel 1 A n Duty cycle is double-buffered (A n  and B n  registers<br>Channel 2 A n  of channels 1-4) and updated after a reload signal.<br>Channel 3 A n<br>Reload<br>Channel 1- OPWMB<br>Channel 2 - OPWMB<br>Channel 3 - OPWMB<br>Figure 219. OPWMCB PWM trigger generation<br>Channel 0  counter<br> output<br>Channel 1<br> output<br>Channel 2<br> output<br>Channel 3<br><!-- End of picture text -->

## 57.7 Glossary 

BLDC Brushless DC. An electronically commutated DC motor. CF Crest Factor. A waveform parameter that is the ratio of peak values to its RMS value. DF Distortion Factor. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1894 / 4640 

NXP Semiconductors 

Power Conversion and Motor Control (PCMC) 

Displacement Power Factor In power electronics, the phase relationship between voltage and current: cos(θv – θi), where θv is the phase of the voltage and θi is the phase of the current. 

DVA Distortion Volt-Amps. FF Form Factor. FOC Field-Oriented Control. GM Gain Margin. pf Power factor. In power electronics, it is the ratio of average power to RMS power. PMSM Permanent Magnet Synchronous Motor. THD Total Harmonic Distortion. VFD Variable-Frequency Drive. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1895 / 4640 

