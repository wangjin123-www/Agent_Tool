NXP Semiconductors 

# Chapter 24 Clock Generation Module (MC_CGM) 

## 24.1 Chip-specific MC_CGM information 

### 24.1.1 Associated content references 

See the Clocking chapter for details pertaining to these: 

- Chip clocking 

- MC_CGM clock source mapping (see the "MC_CGM clock sources mapping" section for this) 

- MC_CGM clock multiplexers (see the "MC_CGM clock multiplexers" section for this) 

~~<mark>CAUTION</mark>~~ 

MC_CGM clock multiplexer configurations to non-supported and reserved clock sources are prohibited and can result in chip malfunctioning. 

## 24.2 Introduction 

The clock generation module (MC_CGM) is used to set up the configurable clock domains used by various chip blocks as per the application needs. It includes the clock multiplexers that allow software to select the desired clock sources for these domains. This is managed by the MC_CGM to ensure that the changing of the clock selection from one source to another occurs in a glitch-less fashion. In addition, the MC_CGM includes the clock dividers that can be configured by software. 

See following figure for the MC_CGM block diagram: 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0816-13.png)


<!-- Start of picture text -->
Clock sources<br>(input)<br>MC_CGM<br>Clock Mux 0<br>DIV<br>PCFS DIV<br>DIV<br>Clock Mux 1<br>DIV<br>PCFS DIV<br>DIV<br>Clock Mux 14<br>%<br>PCFS %<br>%<br>Configuration<br>bus<br>(output)<br>Generated Clocks<br>PCFS configuration registers<br><!-- End of picture text -->

Figure 104. MC_CGM block diagram 

~~<mark>NOTE</mark>~~ 

The block diagram is generic and does not necessarily reflect any specific MC_CGM implementation. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

816 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

## 24.3 Features 

MC_CGM includes the following features: 

- Implements software configurable clock multiplexers for selecting from various clock sources 

- Provides hardware-controlled multiplexers that guarantee glitchless transition, while the software-controlled multiplexers need a software sequence to ensure such a transition 

- Provides software configurable automatic PCFS on certain clocks to minimize the impact of a sudden power consumption change through a gentle ramp-down and -up of the clock frequency when switching clock sources 

- Implements software configurable clock dividers 

## 24.4 Functional description 

### 24.4.1 Clock selection multiplexer 

Each of the clock multiplexers inside the MC_CGM either implements a fully hardware-controlled clock multiplexer or a software-controlled clock multiplexer. The following sections describe the two variants of the clock multiplexer. 

#### 24.4.1.1 Hardware-controlled clock multiplexer 

In hardware-based clock multiplexing, the underlying assumption is that under some conditions, error or reset states, software may not be active. Therefore, the clock switching is fully hardware based and is glitchless. To facilitate clock switching requests with software, the MUX_n_CSC and MUX_n_CSS registers implement request and status for the clock multiplexer, the rest is managed in hardware. Using these registers, the software can monitor the state of the hardware-based clock multiplexer and also make clock switching requests. It is recommended that a new clock switch request is given only when there are no pending/ongoing clock switching requests. However, a switch to the safe clock, that is, FIRC, can be performed at any instance of time. A switch to the safe clock is always completed. Software should ensure that while making a software-based switch to safe clock, the register configuration clock should be available, at least for completing the write to the MUX_n_CSC register. This means that the clock should be running for the register write to complete. Hardware clock multiplexer also supports hardware-based switch to safe clock, which is requested externally to MC_CGM (for example, by MC_RGM). For a hardware-based switch to safe clock, it is not required to have a register configuration clock for MC_CGM. 

~~<mark>NOTE</mark>~~ 

- "Switch to safe clock" from software is requested by programming the MUX_n_CSC[SAFE_SW] bit field only and not by combining the MUX_n_CSC[CLK_SW] and MUX_n_CSC[SELCTL] bit fields of the MUX_n_CSC register. Writes to other fields are ignored when requesting switch for safe clock. 

- After the switch to the safe clock requested by the MC_RGM has completed, the MC_RGM also requests the clock dividers to switch to their default values. This hardware-triggered divider update can be monitored in the same manner as for software-configured updates, and software should use it to ensure that the configuration update has completed before reconfiguring the clocks. 

- Write accesses to the MUX_n_CSC register with clock select pointing to the "reserved" input clock source are aborted with bus transfer errors. 

See Figure 105 that shows the flowchart representation for the sequence of steps to be followed when making a clock switch request to hardware-controlled clock multiplexer. Switch to safe clock can be requested at any instance of time, and for clarity reasons, it is not shown in Figure 105. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

817 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0818-02.png)


<!-- Start of picture text -->
Wait for CLK_SW or<br>Start SAFE_SW or<br>RAMPDOWN or<br>RAMPUP fields to auto-clear<br>Read<br>MUX_n_CSS<br>Read<br>MUX_n_CSS<br>MUX_n_CSS<br>[SWIP] in progress?<br>Y N<br>MUX_n_CSS<br>[SWIP] completed?<br>N<br>Y<br>Configure<br>MUX_n_CSC Check the<br>for clock switch MUX_n_CSS[SWTRG]<br>field status<br>End<br><!-- End of picture text -->

Figure 105. Flow for clock switch request on hardware-controlled clock multiplexer 

      - ~~<mark>NOTE</mark>~~ 

- A switch to the safe clock command always leads to a ramp-down from the currently selected clock and then a switch to "safe clock", except when there is an ongoing clock switch requested by the software without ramp-up and ramp-down. A safe clock switch request when there is an ongoing clock switch without ramp-up or ramp-down results in a switch to the safe clock without performing a ramp-down (either by MC_RGM or provided using the MUX_n_CSC register) does not perform a ramp-down before switching to "safe clock". 

- The above flowchart steps can be preceded by points 1 and 3 below: 

   1. Disable the divider. 

   2. Switch clocks through hardware multiplexer. 

   3. Enable and configure the dividers (atomic write instruction). 

#### 24.4.1.2 Software-controlled clock multiplexer 

In software-based clock multiplexing, the underlying assumption is that the software is always available and there are no error or reset conditions in the chip. This implies that a glitchless switch between input clock sources of MC_CGM MUX can be achieved by following a sequence of steps in software. The software-based clock multiplexer implements a clock gate at the output of the clock mux. The software can gate the selected clock of MC_CGM MUX using a synchronous/graceful clock gate bit (that is, MUX_n_CSC[CG]) or a forced clock gate bit (that is, MUX_n_CSC[FCG]). The hardware does not guarantee that any glitches will escape when using forced clock gating. When a forced clock gate bit is written to 1, the internal clock gate forcefully gates the selected clock to logic-0, therefore, to avoid clock glitches, it should be ensured that the selected clock source is not running. See Figure 106 that shows the flowchart representation for the sequence of steps to be followed when making a clock switch request to software-controlled clock multiplexer. No switch to safe clock is supported in software-controlled clock multiplexer. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

818 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0819-02.png)


<!-- Start of picture text -->
Start<br>Write logic-1 to<br>MUX_n_CSC[CG]<br>Is current clock Write logic-1 to<br>source active? N MUX_n_CSC[FCG]<br>Y<br>Read<br>MUX_n_CSS<br>Is<br>Select the desired<br>N MUX_n_CSS[CS] Y clock source<br>logic-0?<br>Write logic-0 to<br>Write logic-0 to<br>MUX_n_CSC[FCG],<br>MUX_n_CSC[CG]<br>if it is logic-1<br>Read<br>MUX_n_CSS<br>Write logic-1 to<br>MUX_n_CSC[CG]<br>Y<br>Is<br>MUX_n_CSS[CS]logic-1? N Is current clocksource active?  N<br>Y<br>End<br><!-- End of picture text -->

Figure 106. Flow for clock switch request on software controlled clock multiplexer 

###### ~~<mark>NOTE</mark>~~ 

- Ensure that before using the force gate bit, any IP or other logic using the clock of MC_CGM MUX is in the inactive state or a clock glitch resulting from usage of forced gating does not effect the IP (that is, it is clock gated after the MC_CGM). 

- In Figure 106, the clock source to be selected should be active at the time of clock switch, else the MUX_n_CSS[CS] field will remain set to logic-0. In case the clock source to be selected becomes inactive (that is, loss of clock, and so on) during the switching operation, the switch to another clock source can be initiated by writing both the MUX_n_CSC[CG] and MUX_n_CSC[FCG] fields to logic-1. 

- Writing a 'reserved' value for the MUX_n_CSC[SELCTL] field may result in an unpredictable clock at the output of the clock multiplexer. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

819 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

~~<mark>NOTE</mark>~~ 

The above flowchart steps can be preceded by points 1 and 3 below: 

1. Disable the divider. 

2. Switch clocks through software multiplexer. 

3. Enable and configure the dividers (atomic write instruction). 

### 24.4.2 PCFS 

MC_CGM implements PCFS when changing clock source at an MC_CGM clock mux. The PCFS is only implemented in a hardware-controlled clock multiplexer and not in a software-controlled clock multiplexer. It allows a gradual load change for a power/voltage supply unit by employing a gradual frequency changeover from one to another. The frequency changeover is achieved by clock division of input clock source with a sequence of division values, where frequency ramp down and ramp up is achieved when the sequence of division values are ascending and descending in nature, respectively. As the clock division (fractional) is implemented in digital logic, therefore, it is a coarse-level clock division rather than being an accurate-level division, implying that the duty cycle of the progressively divided clock can vary with time. 

The PCFS feature is utilized when a drain current to frequency relationship is known, that is, for a given drain current what is the maximum allowed change in frequency (fchg). The fchg is the first input parameter for PCFS and other parameters for PCFS are specified or calculated in relation to FIRC. 

The PCFS hardware generates the clock division factors based on certain values that are programmed into the PCFS configuration register. The following pseudo codes represent the generation of clock division value sequence (di). 

```
/* ramp down division values (dn) with k steps*/
      delta1 = RATE/1000;
      delta2 = RATE/1000;
      d0       = 1.0;
      for i=1 to k-1 do
        di = di-1 + delta1;
        delta1 = delta1 + delta2;
      endfor
```

```
/* ramp up division values (dn) with k steps*/
      delta1 = RATE*k/1000;
      delta2 = RATE/1000;
      d0       = 1.0 + RATE*k*(k+1)/2;
      for i=1 to k-1 do
        di = di-1 - delta1;
        delta1 = delta1 - delta2;
    endfor
```

As the generation of clock division values is not a closed-bounded function, calculating RATE for a given fchg is an iterative process. Find a value of RATE that produces a clock division sequence, which when used does not lead to a frequency change greater than fchg. See Table 147 that tabulates some of the RATE values against amax, where 

```
amax=fchg/Fi
```

where, Fi is the frequency of i<sup>th</sup> input clock source of the clock mux. 

Table 147. PCFS RATE values 

|amax|PCFS rate|
|---|---|
|0.005|12|
|0.01|48|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

820 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

Table 147. PCFS RATE values (continued) 

|amax|PCFS rate|
|---|---|
|0.15|112|
|0.20|184|



The last clock division factor in case of ramp-down or the first clock in case of ramp-up (following a ramp-down procedure), should be such that clock switch from any input clock source to another should be termed as safe, indicating that load changes have sustainable power effects. This frequency level is referred to as "safe frequency", equivalent to frequency of FIRC referred to as "safe clock" with frequency "safe clock frequency" (fsafe). The last clock division factor in the sequence of clock division factors happens after "k" steps. The factor k (=steps) is calculated by using the following formula: 

```
 k = ceil(0.5 + sqrt(0.25 - (2000 * (1 -(Fi/fsafe)) / RATE)))
```

Using the above formula, all the PCFS register configuration values can be calculated for a given frequency of a clock source: 

```
PCFS_DIVEi.DIV = (Fi/fsafe)*1000-1;
        PCFS_DIVCi.INIT = RATE * k;
        PCFS_DIVCi.RATE = RATE;
        PCFS_DIVSi.DIV  = 999 + (RATE * k * (k+1)/2);
```

See Figure 107 that shows a graphical representation of the change in frequency, which happens during PCFS ramp-down and ramp-up. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0821-09.png)


<!-- Start of picture text -->
Frequency change rate for ramp-down and ramp-up<br>Max<br>Frequency change --><br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0821-10.png)


<!-- Start of picture text -->
N<br><!-- End of picture text -->

Figure 107. PCFS steps vs frequency changes 

For any given clock source, if its frequency is less than that of FIRC, then its corresponding registers should be programmed to default values, where the default values are such that PCFS divider start and PCFS divider end values are same and equal to divide-by-1. The default values ensure that no progressive clock division is done when a clock switch request is given to switch from or to that source. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

821 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

~~<mark>NOTE</mark>~~ 

Calculate the minimum frequency during the PCFS RAMPDOWN and RAMPUP operations by using the formula: 

```
(FIRC/((PCFS_DIVE+1)/1000)) MHz
```

#### 24.4.2.1 PCFS control 

The PCFS operation is configured by a set of configuration registers. One set pertains to the calculation of the clock division factors, which are PCFS_DIVC, PCFS_DIVE, PCFS_DIVS, and PCFS_SDUR, while the registers MUX_n_CSC and MUX_n_CSS implement trigger and status of the PCFS operation. The clock division factors are expected to be programmed before any other MC_CGM operation is initiated and remain unchanged. All the registers corresponding to the clock division factors should be programmed with FIRC as the configuration clock and before doing any clock switch or PCFS operation on any of the MC_CGM mux. It should be noted that the default values of the register corresponding to clock division factors are such that only the clock division factor is calculated by hardware that is divide-by-1. The PCFS operation is always triggered when the safe clock request is generated except when there is an on-going clock switch without ramp-up or ramp-down. Therefore, the software needs to ensure that the PCFS configuration is complete and correct. 

While configuring MUX_n_CSC, only valid PCFS and clock switch requests should be provided. PCFS or clock switch requests should only be provided if the PCFS operation is in the idle state. If there is an ongoing PCFS operation, it is recommended not to provide any new PCFS triggers (except switch to safe clock) until the ongoing operation is completed. Switch to safe clock via hardware or by register configuration can be provided at any instance of time and is always completed. Valid combinations of PCFS and clock switches triggers are listed in Table 148. All the PCFS commands should be atomic in nature, which means a single register write should provide complete PCFS sequence to be executed that is ramp-down, clock switch, and ramp-up. 

Table 148. Valid PCFS and clock switch requests 

|PCFS operation state|Command|
|---|---|
|Idle|Ramp-down, clock switch, and ramp-up|
|Idle|Clock switch only (without ramp-up or ramp-down)|



When a switch to safe clock is provided by writing to MUX_n_CSC, then writes to other register fields are ignored. 

#### 24.4.2.2 Clock source powerup and selection 

This section provides guidelines for powering up a given clock source and selecting it at the MC_CGM clock multiplexer. 

Following is the powerup procedure for a clock source: 

1. Configure the parameter, if any. 

2. Configure the powerup (or powerdown) control field. 

3. Wait for the powerup status indication. 

After a powerup indication, the clock source can be selected to provide output clock at an MC_CGM clock multiplexer. A clock-monitoring setup can also be activated on the powered-up clock source. 

See Figure 108 that shows a flow chart representation of this sequence. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

822 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0823-02.png)


<!-- Start of picture text -->
Start<br>Program the corresponding<br>PCFS configuration<br>register inside MC_CGM<br>Program clock source  Powerup the clock  Read the clock source<br>configuration register(s) source stabilization status (for<br>example, PLL LOCK<br>Setup clock Is clock<br>monitor for powerup Yes source  No<br>clock source stable?<br>Program clock mux<br>control for corresponding<br>clock selection inside<br>MC_CGM with PCFS<br>PCFS to  Read the PCFS<br>destination clock  completion status<br>is triggered<br>Is PCFS  No<br>complete?<br>Yes<br>End<br><!-- End of picture text -->

Figure 108. Clock source powerup and selection procedure 

#### 24.4.2.3 Clock source powerdown and deselection 

This section provides guidelines for powering down a given clock source and deselecting it at MC_CGM clock multiplexer. 

Following is the powerdown procedure for a clock source: 

1. Deselect the clock source at all MC_CGM clock multiplexers. 

2. Configure the powerup (or powerdown) control field. 

3. Wait for the powerdown status indication. 

See Figure 109 that shows a flow chart representation of this sequence. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

823 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0824-02.png)


<!-- Start of picture text -->
Start<br>Deselect clock source at<br>all clock muxs of<br>MC_CGM with PCFS<br>No<br>destination clock PCFS to  completion statusRead the PCFS  complete? Is PCFS<br>is triggered<br>Yes<br>Program the clock source<br>to powerdown<br>Read the clock source  Is clock<br>power status source<br>powerdown? No<br>Yes<br>End<br><!-- End of picture text -->

Figure 109. Clock source powerdown and clock source deselection procedure 

#### 24.4.2.4 Clock switch with load change 

This section provides guidelines to switch between two high-frequency clock sources along with load changes in the system. Load change is referred to switching ON or OFF of logic/peripherals in the system, which has an effect of significant capacitance changes on the chip. This triggers the voltage regulation for the chip. 

When a large number of peripherals or digital logic is enabled or disabled, it is recommended that this step should be performed at a low frequency. Independent of whether a clock switch is required, this criteria needs to be met. When a clock switch is required at two high frequencies, the recommended sequence is as follows: 

1. Intermediately switch to FIRC. 

2. Change load (that is, enable/disable peripherals). 

3. Switch to the target clock. 

See the following figure that shows a flow chart representation of this sequence. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

824 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0825-02.png)


<!-- Start of picture text -->
Start<br>Select FIRC at clock<br>muxs of MC_CGM where load<br>change is required with PCFS<br>No<br>destination clock PCFS to  completion statusRead the PCFS  complete? Is PCFS<br>is triggered<br>Yes<br>Perform load<br>change<br>Program clock mux<br>control inside MC_CGM<br>to select target clock with<br>PCFS<br>PCFS to  Read the PCFS<br>destination clock  completion status<br>is triggered<br>Is PCFS  No<br>complete?<br>Yes<br>End<br><!-- End of picture text -->

Figure 110. Clock switch with load change procedure 

### 24.4.3 Clock dividers 

Clock dividers are used for the generation of a divided clock that is used for running IPs or peripherals. The MC_CGM provides the following built-in dividers at each clock mux: 

##### • 50% clock dividers 

Each divider can be controlled by the Divider Enable (DE) bit and the Division Value (DIV) field. If a divider has its DE bit set to logic-0 in the respective configuration register, then that divider is disabled and the output divided clock is held to logic-0. If the DE bit is logic-1, the divider is enabled and provides a divided clock according to the value set in the DIV field. 

#### 24.4.3.1 50% clock divider 

50% duty cycle dividers generate a real divided clock. The division factor is always an integer but is not restricted to even numbers. The rising edge of the divided clock is always synchronous to the rising edge of the divider source clock, but the falling edge is synchronous to the rising edge or the falling edge depending on whether the division factor is even or odd, respectively. If the input clock has a duty cycle of 50%, the divided output clock maintains the same 50% duty cycle. See Figure 111 that shows the 50% clock divider operation and its associated signals. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

825 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0826-01.png)


<!-- Start of picture text -->
Clock Generation Module (MC_CGM)<br>Clock input<br>Divider counter 3 2 1 0 3 2 1 0 3 2 1 0 3 2 1 0<br>Divided clock output (%4)<br>Figure 111. 50% clock divider programmed for divide by 4 (DIV=3)<br><!-- End of picture text -->

A 50% divided clock can be considered asynchronous (not edge aligned) to other divided clocks from dividers at the same clock mux. 50% clock dividers are implemented without an active closed loop, and are expected not to get stuck if the input clock glitches for a single cycle. 

#### 24.4.3.2 Clock dividers update 

To update the division value or the divider enable, the software should follow the procedure as shown in Figure 112. These updates happen only after the current division cycle has elapsed. However, if the phase of the clock divider is updated, the update happens independently from the state of the division cycle. Any update to the clock divider fields does not result in clock glitch either at the divided clock output or the phase-divided clock output. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0826-05.png)


<!-- Start of picture text -->
Start<br>Configure the<br>MUX_n_DIV_x register<br>Read the<br>MUX_n_DIV_UPD_STAT<br>register<br>Is divider<br>N update complete? Y End<br><!-- End of picture text -->

Figure 112. Flow for clock divider programming update 

Following is the procedure for updating the dividers using the common trigger update: 

1. Configure the MUX_n_DIV_TRIG_CTRL register. 

2. Wait for the update to finish (until MUX_n_DIV_UPD_STAT is 0). 

3. Update the clock dividers (only 50%) per the divider update procedure. 

4. After the divider update is finished, perform a write operation on the MUX_n_DIV_TRIG register. 

5. Wait for the update to finish, that is, until MUX_n_DIV_UPD_STAT is 0. During this period, the following process takes place: 

   - Halt handshake is initiated if configured in step 1. 

   - Clock dividers is updated only when AXBS is halted (that is, halt acknowledgment is received by MC_CGM). It is initiated, else the dividers are updated at alignment. 

   - After the clock dividers are updated, MUX_n_DIV_UPD_STAT is asserted to 0. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

826 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

- When the bit fields MUX_x_DIV_TRIG_CTRL[TCTL] and MUX_x_DIV_TRIG_CTRL[HHEN] are set to 1, then any write operation on trigger register will assert (MUX_n_DIV_UPD_STAT). Once the dividers are updated and aligned (MUX_n_DIV_UPD_STAT) will be deasserted. 

~~<mark>NOTE</mark>~~ 

   - The MUX_x_DIV_TRIG_CTRL[HHEN] bit should only be set when MUX_x_DIV_TRIG_CTRL[TCTL] is set, otherwise it may lead to misalignment of the dividers. 

   - In case of divider initialization by MC_RGM, a halt handshake protocol is initiated if the corresponding register bit is set and the clock dividers are initialized after the halt handshake protocol completion. 

6. This completes the divider update. 

7. When multiple writes to the dividers of same clock MUX is made without waiting for the previous update status signal to finish may lead to misalignment of the dividers. 

For aligned dividers, the LCM of the division values programmed in the dividers of respective clock mux should be less than 100. 

~~<mark>NOTE</mark>~~ 

Performing multiple writes to the divider without waiting for the earlier update to complete can lead to misalignment of the dividers. 

Recommended software sequence for ensuring no undivided output at MC_CGM: 

1. Reset is de-asserted 

2. MC_RGM goes to IDLE 

3. Enable the clock dividers of MC_CGM to provide FIRC clock so that reset of fixed dividers can be lifted. 

4. Program the MC_CGM as per use case division values. 

5. Switch the clock of MC_CGM Mux to desired one, and run the system. 

## 24.5 MC_CGM register descriptions 

MC_CGM implements a set of clock multiplexers that share PCFS configuration registers. MC_CGM registers have the following properties: 

- All registers are 32-bit wide. 

- Only 32-bit read and write accesses are supported. 

- Read/write accesses of less than 32 bits terminate with an error. 

- Writes to read-only register fields in writable registers are ignored and do not provide an error response. 

- Writes to read-only registers are aborted with an error response. 

### 24.5.1 MC_CGM memory map 

MC_CGM base address: 402D_8000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|PCFS Step Duration (PCFS_SDUR)|32|RW|0000_0000h|
|58h|PCFS Divider Change 8 Register (PCFS_DIVC8)|32|RW|0000_0000h|
|5Ch|PCFS Divider End 8 Register (PCFS_DIVE8)|32|RW|0000_03E7h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

827 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|60h|PCFS Divider Start 8 Register (PCFS_DIVS8)|32|RW|0000_03E7h|
|300h|Clock Mux 0 Select Control Register (MUX_0_CSC)|32|RW|0000_0000h|
|304h|Clock Mux 0 Select Status Register (MUX_0_CSS)|32|RO|0008_0000h|
|308h|Clock Mux 0 Divider 0 Control Register (MUX_0_DC_0)|32|RW|8000_0000h|
|30Ch|Clock Mux 0 Divider 1 Control Register (MUX_0_DC_1)|32|RW|8000_0000h|
|310h|Clock Mux 0 Divider 2 Control Register (MUX_0_DC_2)|32|RW|8001_0000h|
|314h|Clock Mux 0 Divider 3 Control Register (MUX_0_DC_3)|32|RW|8000_0000h|
|318h|Clock Mux 0 Divider 4 Control Register (MUX_0_DC_4)|32|RW|8000_0000h|
|31Ch|Clock Mux 0 Divider 5 Control Register (MUX_0_DC_5)|32|RW|8003_0000h|
|320h|Clock Mux 0 Divider 6 Control Register (MUX_0_DC_6)|32|RW|8000_0000h|
|334h|Clock Mux 0 Divider Trigger Control Register<br>(MUX_0_DIV_TRIG_CTRL)|32|RW|0000_0000h|
|338h|Clock Mux 0 Divider Trigger Register (MUX_0_DIV_TRIG)|32|WORZ|0000_0000h|
|33Ch|Clock Mux 0 Divider Update Status Register<br>(MUX_0_DIV_UPD_STAT)|32|RO|0000_0000h|
|340h|Clock Mux 1 Select Control Register (MUX_1_CSC)|32|RW|0000_0000h|
|344h|Clock Mux 1 Select Status Register (MUX_1_CSS)|32|RO|0008_0000h|
|348h|Clock Mux 1 Divider 0 Control Register (MUX_1_DC_0)|32|RW|0000_0000h|
|37Ch|Clock Mux 1 Divider Update Status Register<br>(MUX_1_DIV_UPD_STAT)|32|RO|0000_0000h|
|380h|Clock Mux 2 Select Control Register (MUX_2_CSC)|32|RW|0000_0000h|
|384h|Clock Mux 2 Select Status Register (MUX_2_CSS)|32|RO|0008_0000h|
|388h|Clock Mux 2 Divider 0 Control Register (MUX_2_DC_0)|32|RW|0000_0000h|
|3BCh|Clock Mux 2 Divider Update Status Register<br>(MUX_2_DIV_UPD_STAT)|32|RO|0000_0000h|
|3C0h|Clock Mux 3 Select Control Register (MUX_3_CSC)|32|RW|0000_0000h|
|3C4h|Clock Mux 3 Select Status Register (MUX_3_CSS)|32|RO|0008_0000h|
|3C8h|Clock Mux 3 Divider 0 Control Register (MUX_3_DC_0)|32|RW|0000_0000h|
|3FCh|Clock Mux 3 Divider Update Status Register<br>(MUX_3_DIV_UPD_STAT)|32|RO|0000_0000h|
|400h|Clock Mux 4 Select Control Register (MUX_4_CSC)|32|RW|0000_0000h|
|404h|Clock Mux 4 Select Status Register (MUX_4_CSS)|32|RO|0008_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

828 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|408h|Clock Mux 4 Divider 0 Control Register (MUX_4_DC_0)|32|RW|0000_0000h|
|43Ch|Clock Mux 4 Divider Update Status Register<br>(MUX_4_DIV_UPD_STAT)|32|RO|0000_0000h|
|440h|Clock Mux 5 Select Control Register (MUX_5_CSC)|32|RW|0000_0000h|
|444h|Clock Mux 5 Select Status Register (MUX_5_CSS)|32|RO|0002_0000h|
|448h|Clock Mux 5 Divider 0 Control Register (MUX_5_DC_0)|32|RW|8001_0000h|
|47Ch|Clock Mux 5 Divider Update Status Register<br>(MUX_5_DIV_UPD_STAT)|32|RO|0000_0000h|
|480h|Clock Mux 6 Select Control Register (MUX_6_CSC)|32|RW|0000_0000h|
|484h|Clock Mux 6 Select Status Register (MUX_6_CSS)|32|RO|0002_0000h|
|488h|Clock Mux 6 Divider 0 Control Register (MUX_6_DC_0)|32|RW|8001_0000h|
|4BCh|Clock Mux 6 Divider Update Status Register<br>(MUX_6_DIV_UPD_STAT)|32|RO|0000_0000h|
|4C0h|Clock Mux 7 Select Control Register (MUX_7_CSC)|32|RW|0000_0000h|
|4C4h|Clock Mux 7 Select Status Register (MUX_7_CSS)|32|RO|0008_0000h|
|4C8h|Clock Mux 7 Divider 0 Control Register (MUX_7_DC_0)|32|RW|0000_0000h|
|4FCh|Clock Mux 7 Divider Update Status Register<br>(MUX_7_DIV_UPD_STAT)|32|RO|0000_0000h|
|500h|Clock Mux 8 Select Control Register (MUX_8_CSC)|32|RW|0000_0000h|
|504h|Clock Mux 8 Select Status Register (MUX_8_CSS)|32|RO|0008_0000h|
|508h|Clock Mux 8 Divider 0 Control Register (MUX_8_DC_0)|32|RW|0000_0000h|
|53Ch|Clock Mux 8 Divider Update Status Register<br>(MUX_8_DIV_UPD_STAT)|32|RO|0000_0000h|
|540h|Clock Mux 9 Select Control Register (MUX_9_CSC)|32|RW|0000_0000h|
|544h|Clock Mux 9 Select Status Register (MUX_9_CSS)|32|RO|0008_0000h|
|548h|Clock Mux 9 Divider 0 Control Register (MUX_9_DC_0)|32|RW|0000_0000h|
|57Ch|Clock Mux 9 Divider Update Status Register<br>(MUX_9_DIV_UPD_STAT)|32|RO|0000_0000h|
|580h|Clock Mux 10 Select Control Register (MUX_10_CSC)|32|RW|0000_0000h|
|584h|Clock Mux 10 Select Status Register (MUX_10_CSS)|32|RO|0008_0000h|
|588h|Clock Mux 10 Divider 0 Control Register (MUX_10_DC_0)|32|RW|0000_0000h|
|5BCh|Clock Mux 10 Divider Update Status Register<br>(MUX_10_DIV_UPD_STAT)|32|RO|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

829 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|5C0h|Clock Mux 11 Select Control Register (MUX_11_CSC)|32|RW|0000_0000h|
|5C4h|Clock Mux 11 Select Status Register (MUX_11_CSS)|32|RO|0002_0000h|
|5C8h|Clock Mux 11 Divider 0 Control Register (MUX_11_DC_0)|32|RW|8000_0000h|
|5FCh|Clock Mux 11 Divider Update Status Register<br>(MUX_11_DIV_UPD_STAT)|32|RO|0000_0000h|
|640h|Clock Mux 13 Select Control Register (MUX_13_CSC)|32|RW|0000_0000h|
|644h|Clock Mux 13 Select Status Register (MUX_13_CSS)|32|RO|0008_0000h|
|648h|Clock Mux 13 Divider 0 Control Register (MUX_13_DC_0)|32|RW|0000_0000h|
|67Ch|Clock Mux 13 Divider Update Status Register<br>(MUX_13_DIV_UPD_STAT)|32|RO|0000_0000h|
|680h|Clock Mux 14 Select Control Register (MUX_14_CSC)|32|RW|0000_0000h|
|684h|Clock Mux 14 Select Status Register (MUX_14_CSS)|32|RO|0008_0000h|
|688h|Clock Mux 14 Divider 0 Control Register (MUX_14_DC_0)|32|RW|0000_0000h|
|6BCh|Clock Mux 14 Divider Update Status Register<br>(MUX_14_DIV_UPD_STAT)|32|RO|0000_0000h|



### 24.5.2 PCFS Step Duration (PCFS_SDUR) 

##### Offset 

|Register|Offset|
|---|---|
|PCFS_SDUR|0h|



##### Function 

This register specifies the step duration of each PCFS step. The value provided in this register specifies the PCFS step duration in terms of the number of cycles of FIRC. 

This register is reset only by a destructive reset. For details, see PCFS. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

830 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0831-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>SDUR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16<br>—|This field is reserved and reads return zeros.|
|15-0|Step duration|
|SDUR|Count value of the step duration|



### 24.5.3 PCFS Divider Change 8 Register (PCFS_DIVC8) 

##### Offset 

|Register|Offset|
|---|---|
|PCFS_DIVC8|58h|



##### Function 

This register defines the rate of frequency change and initial change value on frequency ramp-up for the Progressive Clock Frequency switching of PLL_PHI0_CLK. 

This register is reset only on destructive reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

831 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0832-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>INIT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>RATE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16|Divider change initial value|
|INIT|This field provides the initial change value of the clock divider for the clock ramp-up phase<br>of PLL_PHI0_CLK.|
|15-8|This field is reserved and reads return zeros.|
|—||
|7-0|Divider change rate|
|RATE|This value controls the change value of the clock divider for the clock ramp-up and ramp-down phase of<br>PLL_PHI0_CLK.|



### 24.5.4 PCFS Divider End 8 Register (PCFS_DIVE8) 

##### Offset 

|Register|Offset|
|---|---|
|PCFS_DIVE8|5Ch|



##### Function 

This register defines the final division value on frequency ramp-down for the progressive system clock switching of PLL_PHI0_CLK. 

This registers is reset only on destructive reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

832 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0833-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>DIVE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>DIVE<br>W<br>Reset 0 0 0 0 0 0 1 1 1 1 1 0 0 1 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-20|This field is reserved and reads return zeros.|
|—||
|19-0|Divider end value|
|DIVE|This field provides the end value of the clock divider for the PLL_PHI0_CLK ramp-down phase.|



### 24.5.5 PCFS Divider Start 8 Register (PCFS_DIVS8) 

##### Offset 

|Register|Offset|
|---|---|
|PCFS_DIVS8|60h|



##### Function 

This register defines the initial division value on frequency ramp-up for the progressive system clock switching of PLL_PHI0_CLK. This register is reset only on destructive reset. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0833-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>DIVS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>DIVS<br>W<br>Reset 0 0 0 0 0 0 1 1 1 1 1 0 0 1 1 1<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

833 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Fields 

|Field|Function|
|---|---|
|31-20|This field is reserved and reads return zeros.|
|—||
|19-0|Divider start value|
|DIVS|This field provides the start value of the clock divider for the PLL_PHI0_CLK ramp-up phase|



### 24.5.6 Clock Mux 0 Select Control Register (MUX_0_CSC) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_0_CSC|300h|



##### Function 

This register provides the clock source selection control for clock mux 0. Clock mux 0 implements hardware control clock switching ensuring that the clock switch happens in a graceful manner (without glitches). See the "Hardware-controlled clock multiplexer" section for details. 

This register is reset on destructive reset only. 

An update to all the PCFS-related fields of this register must be an atomic write, which means a single write must update the CLK_SW, RAMPDOWN, and RAMPUP fields. It is necessary to set both RAMPUP and RAMPDOWN bits together even if you want to trigger either RAMPUP or RAMPDOWN process otherwise the desired PCFS sequence will not be executed. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0834-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0<br>SELCTL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 SAFE_ CLK_ RAMP RAMP<br>W SW  SW  DOWN  UP<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-28|This field is reserved and reads return zeros.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

834 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|27-24|Clock source selection control|
|SELCTL|Selects the source clock for clock mux 0. The reserved values are not displayed.<br>0000b - FIRC<br>1000b - PLL_PHI0_CLK|
|23-4<br>—|This field is reserved and reads return zeros.|
|3|Safe clock request|
|SAFE_SW|Writing 1 to this bit makes a safe clock switch request to FIRC. After a safe clock switch operation is<br>requested, this bit is auto cleared and a corresponding bit in the status register is set.|
|2<br>CLK_SW|Clock switch<br>Writing 1 to this bit makes a clock switch request to clock mux 0. After a clock switch operation is requested,<br>this bit is auto cleared and a corresponding bit in the status register is set.|
|1|PCFS ramp-down|
|RAMPDOWN|Writing 1 to this bit makes a PCFS ramp-down request to clock mux 0. After a PCFS ramp-down operation<br>is requested, this bit is auto cleared and a corresponding bit in the status register is set.|
|0|PCFS ramp-up|
|RAMPUP|Writing 1 to this bit makes a PCFS ramp-up request to clock mux 0. After a PCFS ramp-up operation is<br>requested, this bit is auto cleared and a corresponding bit in the status register is set.|



### 24.5.7 Clock Mux 0 Select Status Register (MUX_0_CSS) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_0_CSS|304h|



##### Function 

This register provides the current clock source selection status for clock mux 0. 

This register is reset on destructive reset only. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

835 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Diagram 

|Bits|31|30||29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||0||||SELS|TAT|||0||||SWTRG||SWIP|
|W||||||||||||||||||
|Reset|0|0||0|0|0|0|0|0|0|0|0|0|1|0|0|0|
|Bits|15|14||13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||||0|||||||SAFE_<br>SW|CLK_<br>SW|RAMP<br>DOWN|RAMP<br>UP|
|W||||||||||||||||||
|Reset|0|0||0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-28|This field is reserved and reads return zeros.|
|—||
|27-24|Clock source selection status|
|SELSTAT|This value indicates the current source selected for clock mux 0. The reserved values are not displayed.<br>0000b - FIRC<br>1000b - PLL_PHI0_CLK|
|23-20<br>—<br>19-17|This field is reserved and reads return zeros.<br>Switch trigger cause|
|SWTRG|This value indicates the cause for the latest clock source switch.|
||If the clock fails, followed by multiple safe clock switch requests for MC_CGM hardware<br>clock mux, the value of the SWTRG field can be either 4 or 5.<br>~~NOTE~~|
||000b - Reserved|
||001b - Switch after request succeeded.<br>010b - Switch after the request failed because of an inactive target clock and the current clock is<br>FIRC.<br>011b - Switch after the request failed because of an inactive current clock and the current clock is<br>FIRC.<br>100b - Switch to FIRC because of a safe clock request or reset succeeded.<br>101b - Switch to FIRC because of a safe clock request or reset succeeded, but the previous<br>current clock source was inactive.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

836 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

||Table continued from the previous page...|
|---|---|
|Field|Function|
||110b - Reserved<br>111b - Reserved|
|16<br>SWIP|Switch in progress<br>New clock switch request can only be given three clock cycles after the completion of the<br>previous request.<br>~~NOTE~~|
||0b - Clock source switching is complete.<br>1b - Clock source switching is in progress.|
|15-4<br>—|This field is reserved and reads return zeros.|
|3<br>SAFE_SW|Safe clock request<br>This field provides an indication of whether a switch to safe clock operation was requested during the<br>previous/ongoing request on clock mux 0.<br>0b - No safe clock switch operation was requested.<br>1b - Safe clock switch operation was requested.|
|2<br>CLK_SW|Clock switch<br>This field provides an indication of whether a clock switch operation was requested during the previous/<br>ongoing request on clock mux 0.<br>0b - No clock switch operation was requested.<br>1b - Clock switch operation was requested.|
|1<br>RAMPDOWN|PCFS ramp-down<br>This field provides an indication of whether a PCFS ramp-down operation was requested during the<br>previous/ongoing request on clock mux 0.<br>In case of safe clock switching, the ramp-down operation runs internally, but the value of the<br>corresponding status field is not set to 1.<br>~~NOTE~~|
||0b - No ramp-down operation was requested.<br>1b - Ramp-down operation was requested.|
|0<br>RAMPUP|PCFS ramp-up<br>This field provides an indication of whether a PCFS ramp-up operation was requested during the previous/<br>ongoing request on clock mux 0.<br>0b - No ramp-up operation was requested.<br>1b - Ramp-up operation was requested.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

837 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

### 24.5.8 Clock Mux 0 Divider 0 Control Register (MUX_0_DC_0) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_0_DC_0|308h|



##### Function 

This register controls the clock divider 0 for clock mux 0. 

This divider is a 50% duty cycle divider. 

~~<mark>NOTE</mark>~~ 

The update to the fields of this register should be an atomic write, that is, one single write should update the complete register. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|DE|||||||0|||||||DIV||
|Reset|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|Divider enable|
|DE|0b - Reserved<br>1b - Divider is enabled.|
|30-19|This field is reserved and reads return zeros.|
|—||
|18-16|Division value|
|DIV|This field provides the division value for the clock divider. The clock period of the clock after division is<br>'DIV+1' times the time period of the current input clock to the divider.|
|15-0<br>—|This field is reserved and reads return zeros.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

838 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

### 24.5.9 Clock Mux 0 Divider 1 Control Register (MUX_0_DC_1) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_0_DC_1|30Ch|



##### Function 

This register controls the clock divider 1 for clock mux 0. 

This divider is a 50% duty cycle divider. 

~~<mark>NOTE</mark>~~ 

The update to the fields of this register should be an atomic write, that is, one single write should update the complete register. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|DE|||||||0|||||||DIV||
|Reset|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|Divider enable|
|DE|0b - Reserved<br>1b - Divider is enabled.|
|30-19|This field is reserved and reads return zeros.|
|—||
|18-16|Division value|
|DIV|This field provides the division value for the clock divider. The clock period of the clock after division is<br>'DIV+1' times the time period of the current input clock to the divider.|
|15-0<br>—|This field is reserved and reads return zeros.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

839 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

### 24.5.10 Clock Mux 0 Divider 2 Control Register (MUX_0_DC_2) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_0_DC_2|310h|



##### Function 

This register controls the clock divider 2 for clock mux 0. 

This divider is a 50% duty cycle divider. 

~~<mark>NOTE</mark>~~ 

The update to the fields of this register should be an atomic write, that is, one single write should update the complete register. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18||17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|DE||||||0|||||||DI|V|||
|Reset|1|0|0|0|0|0|0|0|0|0|0|0|0|0||0|1|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2||1|0|
|R||||||||0||||||||||
|W||||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0||0|0|



##### Fields 

|Field|Function|
|---|---|
|31|Divider enable|
|DE|0b - Reserved<br>1b - Divider is enabled.|
|30-20|This field is reserved and reads return zeros.|
|—||
|19-16|Division value|
|DIV|This field provides the division value for the clock divider. The clock period of the clock after division is<br>'DIV+1' times the time period of the current input clock to the divider.|
|15-0<br>—|This field is reserved and reads return zeros.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

840 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

### 24.5.11 Clock Mux 0 Divider 3 Control Register (MUX_0_DC_3) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_0_DC_3|314h|



##### Function 

This register controls the clock divider 3 for clock mux 0. 

This divider is a 50% duty cycle divider. 

~~<mark>NOTE</mark>~~ 

The update to the fields of this register should be an atomic write, that is, one single write should update the complete register. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|DE|||||||0|||||||DIV||
|Reset|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|Divider enable|
|DE|0b - Reserved<br>1b - Divider is enabled.|
|30-19|This field is reserved and reads return zeros.|
|—||
|18-16|Division value|
|DIV|This field provides the division value for the clock divider. The clock period of the clock after division is<br>'DIV+1' times the time period of the current input clock to the divider.|
|15-0<br>—|This field is reserved and reads return zeros.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

841 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

### 24.5.12 Clock Mux 0 Divider 4 Control Register (MUX_0_DC_4) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_0_DC_4|318h|



##### Function 

This register controls the clock divider 4 for clock mux 0. 

This divider is a 50% duty cycle divider. 

~~<mark>NOTE</mark>~~ 

The update to the fields of this register should be an atomic write, that is, one single write should update the complete register. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|DE|||||||0|||||||DIV||
|Reset|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|Divider enable|
|DE|0b - Reserved<br>1b - Divider is enabled.|
|30-19|This field is reserved and reads return zeros.|
|—||
|18-16|Division value|
|DIV|This field provides the division value for the clock divider. The clock period of the clock after division is<br>'DIV+1' times the time period of the current input clock to the divider.|
|15-0<br>—|This field is reserved and reads return zeros.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

842 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

### 24.5.13 Clock Mux 0 Divider 5 Control Register (MUX_0_DC_5) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_0_DC_5|31Ch|



##### Function 

This register controls the clock divider 5 for clock mux 0. 

This divider is a 50% duty cycle divider. 

~~<mark>NOTE</mark>~~ 

The update to the fields of this register should be an atomic write, that is, one single write should update the complete register. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18<br>17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|DE|||||||0||||||DIV||
|Reset|1|0|0|0|0|0|0|0|0|0|0|0|0|0<br>1|1|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2<br>1|0|
|R<br>W|||||||0|||||||Reserved||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|0|



##### Fields 

|Field|Function|
|---|---|
|31|Divider enable|
|DE|0b - Reserved<br>1b - Divider is enabled.|
|30-19|This field is reserved and reads return zeros.|
|—||
|18-16|Division value|
|DIV|This field provides the division value for the clock divider. The clock period of the clock after division is<br>'DIV+1' times the time period of the current input clock to the divider.|
|15-3<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

843 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|2-0<br>—|Reserved|



### 24.5.14 Clock Mux 0 Divider 6 Control Register (MUX_0_DC_6) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_0_DC_6|320h|



##### Function 

This register controls the clock divider 6 for clock mux 0. 

This divider is a 50% duty cycle divider. 

~~<mark>NOTE</mark>~~ 

The update to the fields of this register should be an atomic write, that is, one single write should update the complete register. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0844-13.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R DE  0<br>DIV<br>W<br>Reset 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31|Divider enable|
|DE|0b - Reserved|
||1b - Divider is enabled.|
|30-19|This field is reserved and reads return zeros.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

844 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|18-16|Division value|
|DIV|This field provides the division value for the clock divider. The clock period of the clock after division is<br>'DIV+1' times the time period of the current input clock to the divider.|
|15-0<br>—|This field is reserved and reads return zeros.|



### 24.5.15 Clock Mux 0 Divider Trigger Control Register (MUX_0_DIV_TRIG_CTRL) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_0_DIV_TRIG_CTR|334h|
|L||



##### Function 

This register selects whether the dividers associated with clock mux 0 are updated immediately on writing to the corresponding divider configuration register (referred to as immediate divider update) or only on writing to the MC_CGM_MUX_0_DIV_TRIG register (referred to as common trigger update). When common trigger update is configured, this register also controls initiation of the halt handshake protocol with the on-chip AXBS. Software is required to configure HHEN field for handshaking with on-chip AXBS when the ratio of division value among the clock dividers need to be changed. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|HHEN||||||||0||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||0||||||||TCTL|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function|
|---|---|
|31|Halt handshake enable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

845 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|HHEN|This field controls the initiation of the halt handshake protocol with AXBS when a common trigger divider<br>update is initiated.<br>0b - No halt handshake protocol is initiated.<br>1b - Halt handshake protocol is initiated.|
|30-1|This field is reserved and reads return zeros.|
|—||
|0|Trigger control|
|TCTL|This field controls the divider update configuration between immediate and common update.<br>0b - Immediate divider update|
||1b - Common trigger divider update|



### 24.5.16 Clock Mux 0 Divider Trigger Register (MUX_0_DIV_TRIG) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_0_DIV_TRIG|338h|



##### Function 

This register provides a common trigger for the clock dividers (only 50% duty cycle dividers) of clock mux 0. Writing any value to this register provides a trigger to the dividers. This register should only be written after appropriately configuring the MC_CGM_MUX_0_DIV_TRIG_CTRL register. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W||||||||TRIG|GER||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0|||||||||
|W||||||||TRIG|GER||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

846 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Fields 

|Field|Function|
|---|---|
|31-0|Trigger for divider update|
|TRIGGER||



### 24.5.17 Clock Mux 0 Divider Update Status Register (MUX_0_DIV_UPD_STAT) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_0_DIV_UPD_STAT|33Ch|



##### Function 

This register provides the update status of the clock dividers corresponding to clock mux 0. When a write operation on any divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 when the corresponding divider update is pending. 

~~<mark>NOTE</mark>~~ 

Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of whether any divider(s) are implemented inside MC_CGM clock mux. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||0|||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0||||||||DIV_<br>STAT|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function|
|---|---|
|31-1<br>—|This field is reserved and reads return zeros.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

847 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|0|Divider status for clock mux 0|
|DIV_STAT|On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is<br>fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux<br>to a new clock source:|
||1. Switch the mux to a working clock source without polling this field.<br>2. Update MUX_n_DC_m and poll this field.<br>0b - No divider configuration update is pending.<br>1b - Divider configuration update on at least one divider associated with this multiplexer is<br>pending.|



### 24.5.18 Clock Mux 1 Select Control Register (MUX_1_CSC) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_1_CSC|340h|



##### Function 

This register provides the clock source selection control for clock mux 1. Clock mux 1 implements hardware control clock switching ensuring that the clock switch happens in a graceful manner (without glitches). See the "Hardware-controlled clock multiplexer" section for details. 

This register is reset on destructive reset only. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||0||||SELCTL|||||||0|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R||||||0|||||||SAFE_|CLK_|0|
|W|||||||||||||SW|SW||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

848 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Fields 

|Field|Function|
|---|---|
|31-29<br>—<br>28-24<br>SELCTL|This field is reserved and reads return zeros.<br>Clock source selection control<br>Selects the source clock for clock mux 1. The reserved values are not displayed.<br>0_0000b - FIRC<br>0_0010b - FXOSC<br>1_0110b - AIPS_PLAT_CLK|
|23-4<br>—|This field is reserved and reads return zeros.|
|3|Safe clock request|
|SAFE_SW|Writing 1 to this bit makes a safe clock switch request to FIRC. After a safe clock switch operation is<br>requested, this bit is auto cleared and a corresponding bit in the status register is set.|
|2|Clock switch|
|CLK_SW|Writing 1 to this bit makes a clock switch request to clock mux 1. After a clock switch operation is requested,<br>this bit is auto cleared and a corresponding bit in the status register is set.|
|1-0<br>—|This field is reserved and reads return zeros.|



### 24.5.19 Clock Mux 1 Select Status Register (MUX_1_CSS) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_1_CSS|344h|



##### Function 

This register provides the current clock source selection status for clock mux 1. 

This register is reset on destructive reset only. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

849 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0850-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 SELSTAT  0 SWTRG  SWIP<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>SAFE_ CLK_<br>R 0 0<br>SW  SW<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-29|This field is reserved and reads return zeros.|
|—||
|28-24|Clock source selection status|
|SELSTAT|This value indicates the current source selected for clock mux 1. The reserved values are not displayed.<br>0_0000b - FIRC<br>0_0010b - FXOSC<br>1_0110b - AIPS_PLAT_CLK|
|23-20<br>—|This field is reserved and reads return zeros.|
|19-17<br>SWTRG|Switch trigger cause<br>This value indicates the cause for the latest clock source switch.<br>If the clock fails, followed by multiple safe clock switch requests for MC_CGM hardware<br>clock mux, the value of the SWTRG field can be either 4 or 5.<br>~~NOTE~~|
||000b - Reserved<br>001b - Switch after request succeeded.<br>010b - Switch after the request failed because of an inactive target clock and the current clock is<br>FIRC.<br>011b - Switch after the request failed because of an inactive current clock and the current clock is<br>FIRC.<br>100b - Switch to FIRC because of a safe clock request or reset succeeded.<br>101b - Switch to FIRC because of a safe clock request or reset succeeded, but the previous<br>current clock source was inactive.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

850 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||110b - Reserved<br>111b - Reserved|
|16<br>SWIP|Switch in progress<br>New clock switch request can only be given three clock cycles after the completion of the<br>previous request.<br>~~NOTE~~|
||0b - Clock source switching is complete.<br>1b - Clock source switching is in progress.|
|15-4<br>—<br>3<br>SAFE_SW|This field is reserved and reads return zeros.<br>Safe clock request<br>This field provides an indication of whether a switch to safe clock operation was requested during the<br>previous/ongoing request on clock mux 1.<br>0b - No safe clock switch operation was requested.<br>1b - Safe clock switch operation was requested.|
|2<br>CLK_SW|Clock switch<br>This field provides an indication of whether a clock switch operation was requested during the previous/<br>ongoing request on clock mux 1.<br>0b - No clock switch operation was requested.<br>1b - Clock switch operation was requested.|
|1-0<br>—|This field is reserved and reads return zeros.|



### 24.5.20 Clock Mux 1 Divider 0 Control Register (MUX_1_DC_0) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_1_DC_0|348h|



##### Function 

This register controls the clock divider 0 for clock mux 1. 

This divider is a 50% duty cycle divider. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

851 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

~~<mark>NOTE</mark>~~ 

The update to the fields of this register should be an atomic write, that is, one single write should update the complete register. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0852-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>DE  DIV<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Divider enable|
|DE|0b - Divider is disabled.<br>1b - Divider is enabled.|
|30-17|This field is reserved and reads return zeros.|
|—||
|16|Division value|
|DIV|This field provides the division value for the clock divider. The clock period of the clock after division is<br>'DIV+1' times the time period of the current input clock to the divider.|
|15-0<br>—|This field is reserved and reads return zeros.|



### 24.5.21 Clock Mux 1 Divider Update Status Register (MUX_1_DIV_UPD_STAT) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_1_DIV_UPD_STAT|37Ch|



##### Function 

This register provides the update status of the clock dividers corresponding to clock mux 1. When a write operation on any divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

852 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 when the corresponding divider update is pending. 

~~<mark>NOTE</mark>~~ 

Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of whether any divider(s) are implemented inside MC_CGM clock mux. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||||||||0||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0||||||||DIV_<br>STAT|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-1|This field is reserved and reads return zeros.|
|—||
|0|Divider status for clock mux 1|
|DIV_STAT|On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is<br>fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux<br>to a new clock source:<br>1. Switch the mux to a working clock source without polling this field.<br>2. Update MUX_n_DC_m and poll this field.<br>0b - No divider configuration update is pending.<br>1b - Divider configuration update on at least one divider associated with this multiplexer is<br>pending.|



### 24.5.22 Clock Mux 2 Select Control Register (MUX_2_CSC) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_2_CSC|380h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

853 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Function 

This register provides the clock source selection control for clock mux 2. Clock mux 2 implements hardware control clock switching ensuring that the clock switch happens in a graceful manner (without glitches). See the "Hardware-controlled clock multiplexer" section for details. 

This register is reset on destructive reset only. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||0||||SELCTL|||||||0|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R||||||0|||||||SAFE_|CLK_|0|
|W|||||||||||||SW|SW||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



##### Fields 

|Field|Function|
|---|---|
|31-29<br>—<br>28-24<br>SELCTL|This field is reserved and reads return zeros.<br>Clock source selection control<br>Selects the source clock for clock mux 2. The reserved values are not displayed.<br>0_0000b - FIRC<br>0_0010b - FXOSC<br>1_0110b - AIPS_PLAT_CLK|
|23-4<br>—<br>3|This field is reserved and reads return zeros.<br>Safe clock request|
|SAFE_SW|Writing 1 to this bit makes a safe clock switch request to FIRC. After a safe clock switch operation is<br>requested, this bit is auto cleared and a corresponding bit in the status register is set.|
|2|Clock switch|
|CLK_SW|Writing 1 to this bit makes a clock switch request to clock mux 2. After a clock switch operation is requested,<br>this bit is auto cleared and a corresponding bit in the status register is set.|
|1-0<br>—|This field is reserved and reads return zeros.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

854 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

### 24.5.23 Clock Mux 2 Select Status Register (MUX_2_CSS) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_2_CSS|384h|



##### Function 

This register provides the current clock source selection status for clock mux 2. 

This register is reset on destructive reset only. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0855-09.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 SELSTAT  0 SWTRG  SWIP<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>SAFE_ CLK_<br>R 0 0<br>SW  SW<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-29|This field is reserved and reads return zeros.|
|—||
|28-24|Clock source selection status|
|SELSTAT|This value indicates the current source selected for clock mux 2. The reserved values are not displayed.|
||0_0000b - FIRC|
||0_0010b - FXOSC|
||1_0110b - AIPS_PLAT_CLK|
|23-20<br>—|This field is reserved and reads return zeros.|
|19-17|Switch trigger cause|
|SWTRG|This value indicates the cause for the latest clock source switch.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

855 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||If the clock fails, followed by multiple safe clock switch requests for MC_CGM hardware<br>clock mux, the value of the SWTRG field can be either 4 or 5.<br>~~NOTE~~<br>000b - Reserved<br>001b - Switch after request succeeded.<br>010b - Switch after the request failed because of an inactive target clock and the current clock is<br>FIRC.<br>011b - Switch after the request failed because of an inactive current clock and the current clock is<br>FIRC.<br>100b - Switch to FIRC because of a safe clock request or reset succeeded.|
||101b - Switch to FIRC because of a safe clock request or reset succeeded, but the previous<br>current clock source was inactive.<br>110b - Reserved<br>111b - Reserved|
|16<br>SWIP|Switch in progress<br>New clock switch request can only be given three clock cycles after the completion of the<br>previous request.<br>~~NOTE~~<br>0b - Clock source switching is complete.<br>1b - Clock source switching is in progress.|
|15-4<br>—|This field is reserved and reads return zeros.|
|3<br>SAFE_SW|Safe clock request<br>This field provides an indication of whether a switch to safe clock operation was requested during the<br>previous/ongoing request on clock mux 2.<br>0b - No safe clock switch operation was requested.<br>1b - Safe clock switch operation was requested.|
|2<br>CLK_SW|Clock switch<br>This field provides an indication of whether a clock switch operation was requested during the previous/<br>ongoing request on clock mux 2.<br>0b - No clock switch operation was requested.<br>1b - Clock switch operation was requested.|
|1-0<br>—|This field is reserved and reads return zeros.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

856 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

### 24.5.24 Clock Mux 2 Divider 0 Control Register (MUX_2_DC_0) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_2_DC_0|388h|



##### Function 

This register controls the clock divider 0 for clock mux 2. 

This divider is a 50% duty cycle divider. 

~~<mark>NOTE</mark>~~ 

The update to the fields of this register should be an atomic write, that is, one single write should update the complete register. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|DE|||||||0||||||||DIV|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|Divider enable|
|DE|0b - Divider is disabled.<br>1b - Divider is enabled.|
|30-17|This field is reserved and reads return zeros.|
|—||
|16|Division value|
|DIV|This field provides the division value for the clock divider. The clock period of the clock after division is<br>'DIV+1' times the time period of the current input clock to the divider.|
|15-0<br>—|This field is reserved and reads return zeros.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

857 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

### 24.5.25 Clock Mux 2 Divider Update Status Register (MUX_2_DIV_UPD_STAT) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_2_DIV_UPD_STAT|3BCh|



##### Function 

This register provides the update status of the clock dividers corresponding to clock mux 2. When a write operation on any divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 when the corresponding divider update is pending. 

~~<mark>NOTE</mark>~~ 

Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of whether any divider(s) are implemented inside MC_CGM clock mux. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0858-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>DIV_<br>R 0<br>STAT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-1|This field is reserved and reads return zeros.|
|—||
|0|Divider status for clock mux 2|
|DIV_STAT|On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is<br>fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux<br>to a new clock source:|
||1. Switch the mux to a working clock source without polling this field.<br>2. Update MUX_n_DC_m and poll this field.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

858 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - No divider configuration update is pending.|
||1b - Divider configuration update on at least one divider associated with this multiplexer is<br>pending.|



### 24.5.26 Clock Mux 3 Select Control Register (MUX_3_CSC) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_3_CSC|3C0h|



##### Function 

This register provides the clock source selection control for clock mux 3. Clock mux 3 implements hardware control clock switching ensuring that the clock switch happens in a graceful manner (without glitches). See the "Hardware-controlled clock multiplexer" section for details. 

This register is reset on destructive reset only. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0859-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0<br>SELCTL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 SAFE_ CLK_ 0<br>W SW  SW<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-29<br>—|This field is reserved and reads return zeros.|
|28-24|Clock source selection control|
|SELCTL|Selects the source clock for clock mux 3. The reserved values are not displayed.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

859 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0_0000b - FIRC<br>0_0010b - FXOSC<br>1_0000b - CORE_CLK<br>1_0110b - AIPS_PLAT_CLK|
|23-4<br>—|This field is reserved and reads return zeros.|
|3|Safe clock request|
|SAFE_SW|Writing 1 to this bit makes a safe clock switch request to FIRC. After a safe clock switch operation is<br>requested, this bit is auto cleared and a corresponding bit in the status register is set.|
|2|Clock switch|
|CLK_SW|Writing 1 to this bit makes a clock switch request to clock mux 3. After a clock switch operation is requested,<br>this bit is auto cleared and a corresponding bit in the status register is set.|
|1-0<br>—|This field is reserved and reads return zeros.|



### 24.5.27 Clock Mux 3 Select Status Register (MUX_3_CSS) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_3_CSS|3C4h|



##### Function 

This register provides the current clock source selection status for clock mux 3. 

This register is reset on destructive reset only. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

860 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||0||||SELSTAT||||0||||SWTRG||SWIP|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|1|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||0|||||||SAFE_<br>SW|CLK_<br>SW||0|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-29|This field is reserved and reads return zeros.|
|—||
|28-24|Clock source selection status|
|SELSTAT|This value indicates the current source selected for clock mux 3. The reserved values are not displayed.<br>0_0000b - FIRC<br>0_0010b - FXOSC<br>1_0000b - CORE_CLK<br>1_0110b - AIPS_PLAT_CLK|
|23-20<br>—|This field is reserved and reads return zeros.|
|19-17|Switch trigger cause|
|SWTRG|This value indicates the cause for the latest clock source switch.|
||If the clock fails, followed by multiple safe clock switch requests for MC_CGM hardware<br>clock mux, the value of the SWTRG field can be either 4 or 5.<br>~~NOTE~~|
||000b - Reserved<br>001b - Switch after request succeeded.<br>010b - Switch after the request failed because of an inactive target clock and the current clock is<br>FIRC.<br>011b - Switch after the request failed because of an inactive current clock and the current clock is<br>FIRC.<br>100b - Switch to FIRC because of a safe clock request or reset succeeded.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

861 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||101b - Switch to FIRC because of a safe clock request or reset succeeded, but the previous<br>current clock source was inactive.<br>110b - Reserved<br>111b - Reserved|
|16<br>SWIP|Switch in progress<br>New clock switch request can only be given three clock cycles after the completion of the<br>previous request.<br>~~NOTE~~|
||0b - Clock source switching is complete.<br>1b - Clock source switching is in progress.|
|15-4<br>—|This field is reserved and reads return zeros.|
|3<br>SAFE_SW|Safe clock request<br>This field provides an indication of whether a switch to safe clock operation was requested during the<br>previous/ongoing request on clock mux 3.<br>0b - No safe clock switch operation was requested.<br>1b - Safe clock switch operation was requested.|
|2<br>CLK_SW|Clock switch<br>This field provides an indication of whether a clock switch operation was requested during the previous/<br>ongoing request on clock mux 3.<br>0b - No clock switch operation was requested.<br>1b - Clock switch operation was requested.|
|1-0<br>—|This field is reserved and reads return zeros.|



### 24.5.28 Clock Mux 3 Divider 0 Control Register (MUX_3_DC_0) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_3_DC_0|3C8h|



##### Function 

This register controls the clock divider 0 for clock mux 3. 

This divider is a 50% duty cycle divider. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

862 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

~~<mark>NOTE</mark>~~ 

The update to the fields of this register should be an atomic write, that is, one single write should update the complete register. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0863-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>DE  DIV<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Divider enable|
|DE|0b - Divider is disabled.<br>1b - Divider is enabled.|
|30-18<br>—|This field is reserved and reads return zeros.|
|17-16|Division value|
|DIV|This field provides the division value for the clock divider. The clock period of the clock after division is<br>'DIV+1' times the time period of the current input clock to the divider.|
|15-0<br>—|This field is reserved and reads return zeros.|



### 24.5.29 Clock Mux 3 Divider Update Status Register (MUX_3_DIV_UPD_STAT) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_3_DIV_UPD_STAT|3FCh|



##### Function 

This register provides the update status of the clock dividers corresponding to clock mux 3. When a write operation on any divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

863 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 when the corresponding divider update is pending. 

~~<mark>NOTE</mark>~~ 

Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of whether any divider(s) are implemented inside MC_CGM clock mux. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||||||||0||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0||||||||DIV_<br>STAT|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-1|This field is reserved and reads return zeros.|
|—||
|0|Divider status for clock mux 3|
|DIV_STAT|On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is<br>fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux<br>to a new clock source:<br>1. Switch the mux to a working clock source without polling this field.<br>2. Update MUX_n_DC_m and poll this field.<br>0b - No divider configuration update is pending.<br>1b - Divider configuration update on at least one divider associated with this multiplexer is<br>pending.|



### 24.5.30 Clock Mux 4 Select Control Register (MUX_4_CSC) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_4_CSC|400h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

864 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Function 

This register provides the clock source selection control for clock mux 4. Clock mux 4 implements hardware control clock switching ensuring that the clock switch happens in a graceful manner (without glitches). See the "Hardware-controlled clock multiplexer" section for details. 

This register is reset on destructive reset only. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||0||||SELCTL|||||||0|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R||||||0|||||||SAFE_|CLK_|0|
|W|||||||||||||SW|SW||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



##### Fields 

|Field|Function|
|---|---|
|31-29<br>—<br>28-24<br>SELCTL|This field is reserved and reads return zeros.<br>Clock source selection control<br>Selects the source clock for clock mux 4. The reserved values are not displayed.<br>0_0000b - FIRC<br>0_0010b - FXOSC<br>1_0000b - CORE_CLK<br>1_0110b - AIPS_PLAT_CLK|
|23-4<br>—|This field is reserved and reads return zeros.|
|3|Safe clock request|
|SAFE_SW|Writing 1 to this bit makes a safe clock switch request to FIRC. After a safe clock switch operation is<br>requested, this bit is auto cleared and a corresponding bit in the status register is set.|
|2|Clock switch|
|CLK_SW|Writing 1 to this bit makes a clock switch request to clock mux 4. After a clock switch operation is requested,<br>this bit is auto cleared and a corresponding bit in the status register is set.|
|1-0<br>—|This field is reserved and reads return zeros.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

865 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

### 24.5.31 Clock Mux 4 Select Status Register (MUX_4_CSS) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_4_CSS|404h|



##### Function 

This register provides the current clock source selection status for clock mux 4. 

This register is reset on destructive reset only. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0866-09.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 SELSTAT  0 SWTRG  SWIP<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>SAFE_ CLK_<br>R 0 0<br>SW  SW<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-29|This field is reserved and reads return zeros.|
|—||
|28-24|Clock source selection status|
|SELSTAT|This value indicates the current source selected for clock mux 4. The reserved values are not displayed.<br>0_0000b - FIRC|
||0_0010b - FXOSC|
||1_0000b - CORE_CLK|
||1_0110b - AIPS_PLAT_CLK|
|23-20<br>—|This field is reserved and reads return zeros.|
|19-17|Switch trigger cause|
|SWTRG|This value indicates the cause for the latest clock source switch.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

866 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||If the clock fails, followed by multiple safe clock switch requests for MC_CGM hardware<br>clock mux, the value of the SWTRG field can be either 4 or 5.<br>~~NOTE~~<br>000b - Reserved<br>001b - Switch after request succeeded.<br>010b - Switch after the request failed because of an inactive target clock and the current clock is<br>FIRC.<br>011b - Switch after the request failed because of an inactive current clock and the current clock is<br>FIRC.<br>100b - Switch to FIRC because of a safe clock request or reset succeeded.|
||101b - Switch to FIRC because of a safe clock request or reset succeeded, but the previous<br>current clock source was inactive.<br>110b - Reserved<br>111b - Reserved|
|16<br>SWIP|Switch in progress<br>New clock switch request can only be given three clock cycles after the completion of the<br>previous request.<br>~~NOTE~~<br>0b - Clock source switching is complete.<br>1b - Clock source switching is in progress.|
|15-4<br>—|This field is reserved and reads return zeros.|
|3<br>SAFE_SW|Safe clock request<br>This field provides an indication of whether a switch to safe clock operation was requested during the<br>previous/ongoing request on clock mux 4.<br>0b - No safe clock switch operation was requested.<br>1b - Safe clock switch operation was requested.|
|2<br>CLK_SW|Clock switch<br>This field provides an indication of whether a clock switch operation was requested during the previous/<br>ongoing request on clock mux 4.<br>0b - No clock switch operation was requested.<br>1b - Clock switch operation was requested.|
|1-0<br>—|This field is reserved and reads return zeros.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

867 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

### 24.5.32 Clock Mux 4 Divider 0 Control Register (MUX_4_DC_0) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_4_DC_0|408h|



##### Function 

This register controls the clock divider 0 for clock mux 4. 

This divider is a 50% duty cycle divider. 

~~<mark>NOTE</mark>~~ 

The update to the fields of this register should be an atomic write, that is, one single write should update the complete register. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|DE|||||||0|||||||DIV|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R||||||||0||||||||
|W||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



##### Fields 

|Field|Function|
|---|---|
|31|Divider enable|
|DE|0b - Divider is disabled.<br>1b - Divider is enabled.|
|30-18|This field is reserved and reads return zeros.|
|—||
|17-16|Division value|
|DIV|This field provides the division value for the clock divider. The clock period of the clock after division is<br>'DIV+1' times the time period of the current input clock to the divider.|
|15-0<br>—|This field is reserved and reads return zeros.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

868 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

### 24.5.33 Clock Mux 4 Divider Update Status Register (MUX_4_DIV_UPD_STAT) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_4_DIV_UPD_STAT|43Ch|



##### Function 

This register provides the update status of the clock dividers corresponding to clock mux 4. When a write operation on any divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 when the corresponding divider update is pending. 

~~<mark>NOTE</mark>~~ 

Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of whether any divider(s) are implemented inside MC_CGM clock mux. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0869-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>DIV_<br>R 0<br>STAT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-1|This field is reserved and reads return zeros.|
|—||
|0|Divider status for clock mux 4|
|DIV_STAT|On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is<br>fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux<br>to a new clock source:|
||1. Switch the mux to a working clock source without polling this field.<br>2. Update MUX_n_DC_m and poll this field.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

869 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - No divider configuration update is pending.|
||1b - Divider configuration update on at least one divider associated with this multiplexer is<br>pending.|



### 24.5.34 Clock Mux 5 Select Control Register (MUX_5_CSC) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_5_CSC|440h|



##### Function 

This register provides the clock source selection control of clock mux 5. Clock mux 5 implements software control clock switching, and a graceful clock switch can be performed by executing a sequence of steps in software. See "Software-controlled clock multiplexer" section for details. 

This register is reset on destructive reset only. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0870-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0<br>SELCTL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>FCG  CG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-30<br>—|This field is reserved and reads return zeros.|
|29-24|Clock source selection control|
|SELCTL|Selects the source clock for clock mux 5. The reserved values are not displayed.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

870 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||00_0000b - FIRC<br>00_0001b - SIRC<br>00_0010b - FXOSC<br>00_0100b - SXOSC<br>01_0111b - AIPS_SLOW_CLK<br>11_0010b - Reserved|
|23-4<br>—|This field is reserved and reads return zeros.|
|3|Force clock gate|
|FCG|Writing 1 to this bit gates the clock at the output of clock mux 5 to logic-0 irrespective of the logic level of the<br>currently selected clock. Clock gating using this bit should only be performed when it is insured that current<br>clock source is inactive.|
|2<br>CG|Clock gate<br>Writing 1 to this bit gates the clock at the output of clock mux 5 to logic-0. Using this bit it is insured that no<br>glitches are resulted when gating the clock.|
|1-0<br>—|This field is reserved and reads return zeros.|



### 24.5.35 Clock Mux 5 Select Status Register (MUX_5_CSS) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_5_CSS|444h|



##### Function 

This register provides the current clock source selection status for clock mux 5. 

This register is reset on destructive reset only. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

871 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Diagram 

|Bits|31||30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||0||||SELS|TAT||||0|||0||CS|GRIP|
|W||||||||||||||||||
|Reset|0||0|0|0|0|0|0|0|0|0|0|0|0|0|1|0|
|Bits|15||14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||||0||||||||
|W||||||||||||||||||
|Reset|0||0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-30|This field is reserved and reads return zeros.|
|—||
|29-24|Clock source selection status|
|SELSTAT|This value indicates the current source selected for clock mux 5. The reserved values are not displayed.<br>00_0000b - FIRC<br>00_0001b - SIRC<br>00_0010b - FXOSC<br>00_0100b - SXOSC<br>01_0111b - AIPS_SLOW_CLK<br>11_0010b - Reserved|
|23-20<br>—|This field is reserved and reads return zeros.|
|19-18<br>—|This field is reserved and reads return zeros.|
|17<br>CS|Clock status<br>This field indicates state of the clock at the output of the clock mux.<br>0b - Clock is gated to logic-0 at output of clock mux<br>1b - Clock mux is transparent. Active clock pulses at input of clock mux results in same number of<br>pulses at its output|
|16<br>GRIP|Gating request is in progress.<br>When a clock gate request is given this bit indicates if the clock gating at the output of mux has completed<br>or not.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

872 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Clock source gating or ungating has completed.|
||1b - Clock source gating or ungating is in progress.|
|15-0<br>—|This field is reserved and reads return zeros.|



### 24.5.36 Clock Mux 5 Divider 0 Control Register (MUX_5_DC_0) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_5_DC_0|448h|



##### Function 

This register controls the clock divider 0 for clock mux 5. 

This divider is a 50% duty cycle divider. 

~~<mark>NOTE</mark>~~ 

The update to the fields of this register should be an atomic write, that is, one single write should update the complete register. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0873-13.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>DE  DIV<br>W<br>Reset 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31|Divider enable|
|DE|0b - Divider is disabled.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

873 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - Divider is enabled.|
|30-19|This field is reserved and reads return zeros.|
|—||
|18-16|Division value|
|DIV|This field provides the division value for the clock divider. The clock period of the clock after division is<br>'DIV+1' times the time period of the current input clock to the divider.|
|15-0<br>—|This field is reserved and reads return zeros.|



### 24.5.37 Clock Mux 5 Divider Update Status Register (MUX_5_DIV_UPD_STAT) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_5_DIV_UPD_STAT|47Ch|



##### Function 

This register provides the update status of the clock dividers corresponding to clock mux 5. When a write operation on any divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 when the corresponding divider update is pending. 

~~<mark>NOTE</mark>~~ 

Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of whether any divider(s) are implemented inside MC_CGM clock mux. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0874-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>DIV_<br>R 0<br>STAT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

874 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Fields 

|Field|Function|
|---|---|
|31-1|This field is reserved and reads return zeros.|
|—||
|0|Divider status for clock mux 5|
|DIV_STAT|On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is<br>fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux<br>to a new clock source:<br>1. Switch the mux to a working clock source without polling this field.<br>2. Update MUX_n_DC_m and poll this field.<br>0b - No divider configuration update is pending.<br>1b - Divider configuration update on at least one divider associated with this multiplexer is<br>pending.|



### 24.5.38 Clock Mux 6 Select Control Register (MUX_6_CSC) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_6_CSC|480h|



##### Function 

This register provides the clock source selection control of clock mux 6. Clock mux 6 implements software control clock switching, and a graceful clock switch can be performed by executing a sequence of steps in software. See "Software-controlled clock multiplexer" section for details. 

This register is reset on destructive reset only. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0875-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0<br>SELCTL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>FCG  CG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

875 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Fields 

|Field<br>31-30<br>—|Function<br>This field is reserved and reads return zeros.|
|---|---|
|29-24<br>SELCTL|Clock source selection control<br>Selects the source clock for clock mux 6. The reserved values are not displayed.<br>00_0000b - FIRC<br>00_0001b - SIRC<br>00_0010b - FXOSC<br>00_0100b - SXOSC<br>00_1000b - PLL_PHI0_CLK<br>00_1001b - PLL_PHI1_CLK<br>00_1100b - PLL1_PHI0_CLK<br>00_1101b - PLL1_PHI1_CLK<br>00_1110b - PLL1_PHI2_CLK<br>01_0000b - CORE_CLK<br>01_0011b - HSE_CLK<br>01_0110b - AIPS_PLAT_CLK<br>01_0111b - AIPS_SLOW_CLK<br>01_1000b - EMAC_RMII_TX_CLK<br>01_1001b - EMAC_RX_CLK<br>11_0011b - Reserved<br>11_0100b - Reserved<br>11_0101b - Reserved<br>11_0110b - Reserved<br>11_0111b - Reserved<br>11_1000b - Reserved<br>11_1001b - Reserved<br>11_1010b - Reserved|
||11_1011b - Reserved<br>11_1100b - Reserved<br>11_1101b - Reserved|
||11_1110b - Reserved|
|23-4<br>—|This field is reserved and reads return zeros.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

876 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|3|Force clock gate|
|FCG|Writing 1 to this bit gates the clock at the output of clock mux 6 to logic-0 irrespective of the logic level of the<br>currently selected clock. Clock gating using this bit should only be performed when it is insured that current<br>clock source is inactive.|
|2|Clock gate|
|CG|Writing 1 to this bit gates the clock at the output of clock mux 6 to logic-0. Using this bit it is insured that no<br>glitches are resulted when gating the clock.|
|1-0<br>—|This field is reserved and reads return zeros.|



### 24.5.39 Clock Mux 6 Select Status Register (MUX_6_CSS) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_6_CSS|484h|



##### Function 

This register provides the current clock source selection status for clock mux 6. 

This register is reset on destructive reset only. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|0||||SELS|TAT||||0|||0||CS|GRIP|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||||||0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-30|This field is reserved and reads return zeros.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

877 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|29-24|Clock source selection status|
|SELSTAT|This value indicates the current source selected for clock mux 6. The reserved values are not displayed.<br>00_0000b - FIRC<br>00_0001b - SIRC|
||00_0010b - FXOSC<br>00_0100b - SXOSC<br>00_1000b - PLL_PHI0_CLK<br>00_1001b - PLL_PHI1_CLK<br>00_1100b - PLL1_PHI0_CLK|
||00_1101b - PLL1_PHI1_CLK|
||00_1110b - PLL1_PHI2_CLK<br>01_0000b - CORE_CLK<br>01_0011b - HSE_CLK<br>01_0110b - AIPS_PLAT_CLK<br>01_0111b - AIPS_SLOW_CLK|
||01_1000b - EMAC_RMII_TX_CLK|
||01_1001b - EMAC_RX_CLK|
||11_0011b - Reserved|
||11_0100b - Reserved|
||11_0101b - Reserved|
||11_0110b - Reserved|
||11_0111b - Reserved|
||11_1000b - Reserved|
||11_1001b - Reserved|
||11_1010b - Reserved|
||11_1011b - Reserved|
||11_1100b - Reserved|
||11_1101b - Reserved|
||11_1110b - Reserved|
|23-20<br>—|This field is reserved and reads return zeros.|
|19-18|This field is reserved and reads return zeros.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

878 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|17|Clock status|
|CS|This field indicates state of the clock at the output of the clock mux.<br>0b - Clock is gated to logic-0 at output of clock mux<br>1b - Clock mux is transparent. Active clock pulses at input of clock mux results in same number of<br>pulses at its output|
|16<br>GRIP|Gating request is in progress.<br>When a clock gate request is given this bit indicates if the clock gating at the output of mux has completed<br>or not.<br>0b - Clock source gating or ungating has completed.<br>1b - Clock source gating or ungating is in progress.|
|15-0<br>—|This field is reserved and reads return zeros.|



### 24.5.40 Clock Mux 6 Divider 0 Control Register (MUX_6_DC_0) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_6_DC_0|488h|



##### Function 

This register controls the clock divider 0 for clock mux 6. 

This divider is a 50% duty cycle divider. 

~~<mark>NOTE</mark>~~ 

The update to the fields of this register should be an atomic write, that is, one single write should update the complete register. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

879 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|DE|||||0|||||||DIV||||
|Reset|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|Divider enable|
|DE|0b - Divider is disabled.<br>1b - Divider is enabled.|
|30-22<br>—|This field is reserved and reads return zeros.|
|21-16|Division value|
|DIV|This field provides the division value for the clock divider. The clock period of the clock after division is<br>'DIV+1' times the time period of the current input clock to the divider.|
|15-0<br>—|This field is reserved and reads return zeros.|



### 24.5.41 Clock Mux 6 Divider Update Status Register (MUX_6_DIV_UPD_STAT) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_6_DIV_UPD_STAT|4BCh|



##### Function 

This register provides the update status of the clock dividers corresponding to clock mux 6. When a write operation on any divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 when the corresponding divider update is pending. 

~~<mark>NOTE</mark>~~ 

Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of whether any divider(s) are implemented inside MC_CGM clock mux. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

880 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0||||||||DIV_<br>STAT|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-1|This field is reserved and reads return zeros.|
|—||
|0|Divider status for clock mux 6|
|DIV_STAT|On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is<br>fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux<br>to a new clock source:<br>1. Switch the mux to a working clock source without polling this field.<br>2. Update MUX_n_DC_m and poll this field.<br>0b - No divider configuration update is pending.<br>1b - Divider configuration update on at least one divider associated with this multiplexer is<br>pending.|



### 24.5.42 Clock Mux 7 Select Control Register (MUX_7_CSC) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_7_CSC|4C0h|



##### Function 

This register provides the clock source selection control for clock mux 7. Clock mux 7 implements hardware control clock switching ensuring that the clock switch happens in a graceful manner (without glitches). See the "Hardware-controlled clock multiplexer" section for details. 

This register is reset on destructive reset only. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

881 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||0||||SELCTL|||||||0|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R||||||0|||||||SAFE_|CLK_|0|
|W|||||||||||||SW|SW||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



##### Fields 

|Field|Function|
|---|---|
|31-29<br>—|This field is reserved and reads return zeros.|
|28-24<br>SELCTL|Clock source selection control<br>Selects the source clock for clock mux 7. The reserved values are not displayed.<br>0_0000b - FIRC<br>0_1000b - PLL_PHI0_CLK<br>0_1100b - PLL1_PHI0_CLK<br>1_1000b - EMAC_RMII_TX_CLK|
|23-4<br>—<br>3|This field is reserved and reads return zeros.<br>Safe clock request|
|SAFE_SW|Writing 1 to this bit makes a safe clock switch request to FIRC. After a safe clock switch operation is<br>requested, this bit is auto cleared and a corresponding bit in the status register is set.|
|2|Clock switch|
|CLK_SW|Writing 1 to this bit makes a clock switch request to clock mux 7. After a clock switch operation is requested,<br>this bit is auto cleared and a corresponding bit in the status register is set.|
|1-0<br>—|This field is reserved and reads return zeros.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

882 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

### 24.5.43 Clock Mux 7 Select Status Register (MUX_7_CSS) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_7_CSS|4C4h|



##### Function 

This register provides the current clock source selection status for clock mux 7. 

This register is reset on destructive reset only. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0883-09.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 SELSTAT  0 SWTRG  SWIP<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>SAFE_ CLK_<br>R 0 0<br>SW  SW<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-29|This field is reserved and reads return zeros.|
|—||
|28-24|Clock source selection status|
|SELSTAT|This value indicates the current source selected for clock mux 7. The reserved values are not displayed.<br>0_0000b - FIRC|
||0_1000b - PLL_PHI0_CLK<br>0_1100b - PLL1_PHI0_CLK|
||1_1000b - EMAC_RMII_TX_CLK|
|23-20<br>—|This field is reserved and reads return zeros.|
|19-17|Switch trigger cause|
|SWTRG|This value indicates the cause for the latest clock source switch.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

883 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||If the clock fails, followed by multiple safe clock switch requests for MC_CGM hardware<br>clock mux, the value of the SWTRG field can be either 4 or 5.<br>~~NOTE~~<br>000b - Reserved<br>001b - Switch after request succeeded.<br>010b - Switch after the request failed because of an inactive target clock and the current clock is<br>FIRC.<br>011b - Switch after the request failed because of an inactive current clock and the current clock is<br>FIRC.<br>100b - Switch to FIRC because of a safe clock request or reset succeeded.|
||101b - Switch to FIRC because of a safe clock request or reset succeeded, but the previous<br>current clock source was inactive.<br>110b - Reserved<br>111b - Reserved|
|16<br>SWIP|Switch in progress<br>New clock switch request can only be given three clock cycles after the completion of the<br>previous request.<br>~~NOTE~~<br>0b - Clock source switching is complete.<br>1b - Clock source switching is in progress.|
|15-4<br>—|This field is reserved and reads return zeros.|
|3<br>SAFE_SW|Safe clock request<br>This field provides an indication of whether a switch to safe clock operation was requested during the<br>previous/ongoing request on clock mux 7.<br>0b - No safe clock switch operation was requested.<br>1b - Safe clock switch operation was requested.|
|2<br>CLK_SW|Clock switch<br>This field provides an indication of whether a clock switch operation was requested during the previous/<br>ongoing request on clock mux 7.<br>0b - No clock switch operation was requested.<br>1b - Clock switch operation was requested.|
|1-0<br>—|This field is reserved and reads return zeros.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

884 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

### 24.5.44 Clock Mux 7 Divider 0 Control Register (MUX_7_DC_0) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_7_DC_0|4C8h|



##### Function 

This register controls the clock divider 0 for clock mux 7. 

This divider is a 50% duty cycle divider. 

~~<mark>NOTE</mark>~~ 

The update to the fields of this register should be an atomic write, that is, one single write should update the complete register. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|DE|||||0|||||||DIV||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|Divider enable|
|DE|0b - Divider is disabled.<br>1b - Divider is enabled.|
|30-22|This field is reserved and reads return zeros.|
|—||
|21-16|Division value|
|DIV|This field provides the division value for the clock divider. The clock period of the clock after division is<br>'DIV+1' times the time period of the current input clock to the divider.|
|15-0<br>—|This field is reserved and reads return zeros.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

885 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

### 24.5.45 Clock Mux 7 Divider Update Status Register (MUX_7_DIV_UPD_STAT) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_7_DIV_UPD_STAT|4FCh|



##### Function 

This register provides the update status of the clock dividers corresponding to clock mux 7. When a write operation on any divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 when the corresponding divider update is pending. 

~~<mark>NOTE</mark>~~ 

Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of whether any divider(s) are implemented inside MC_CGM clock mux. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0886-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>DIV_<br>R 0<br>STAT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-1|This field is reserved and reads return zeros.|
|—||
|0|Divider status for clock mux 7|
|DIV_STAT|On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is<br>fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux<br>to a new clock source:|
||1. Switch the mux to a working clock source without polling this field.|
||2. Update MUX_n_DC_m and poll this field.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

886 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - No divider configuration update is pending.|
||1b - Divider configuration update on at least one divider associated with this multiplexer is<br>pending.|



### 24.5.46 Clock Mux 8 Select Control Register (MUX_8_CSC) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_8_CSC|500h|



##### Function 

This register provides the clock source selection control for clock mux 8. Clock mux 8 implements hardware control clock switching ensuring that the clock switch happens in a graceful manner (without glitches). See the "Hardware-controlled clock multiplexer" section for details. 

This register is reset on destructive reset only. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0887-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0<br>SELCTL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 SAFE_ CLK_ 0<br>W SW  SW<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-29<br>—|This field is reserved and reads return zeros.|
|28-24|Clock source selection control|
|SELCTL|Selects the source clock for clock mux 8. The reserved values are not displayed.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

887 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0_0000b - FIRC<br>0_1000b - PLL_PHI0_CLK<br>0_1100b - PLL1_PHI0_CLK<br>1_1000b - EMAC_RMII_TX_CLK<br>1_1010b - Reserved|
|23-4<br>—|This field is reserved and reads return zeros.|
|3|Safe clock request|
|SAFE_SW|Writing 1 to this bit makes a safe clock switch request to FIRC. After a safe clock switch operation is<br>requested, this bit is auto cleared and a corresponding bit in the status register is set.|
|2|Clock switch|
|CLK_SW|Writing 1 to this bit makes a clock switch request to clock mux 8. After a clock switch operation is requested,<br>this bit is auto cleared and a corresponding bit in the status register is set.|
|1-0<br>—|This field is reserved and reads return zeros.|



### 24.5.47 Clock Mux 8 Select Status Register (MUX_8_CSS) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_8_CSS|504h|



##### Function 

This register provides the current clock source selection status for clock mux 8. 

This register is reset on destructive reset only. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

888 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||0||||SELSTAT||||0||||SWTRG||SWIP|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|1|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||0|||||||SAFE_<br>SW|CLK_<br>SW||0|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-29|This field is reserved and reads return zeros.|
|—||
|28-24|Clock source selection status|
|SELSTAT|This value indicates the current source selected for clock mux 8. The reserved values are not displayed.<br>0_0000b - FIRC<br>0_1000b - PLL_PHI0_CLK<br>0_1100b - PLL1_PHI0_CLK<br>1_1000b - EMAC_RMII_TX_CLK<br>1_1010b - Reserved|
|23-20<br>—<br>19-17<br>SWTRG|This field is reserved and reads return zeros.<br>Switch trigger cause<br>This value indicates the cause for the latest clock source switch.<br>If the clock fails, followed by multiple safe clock switch requests for MC_CGM hardware<br>clock mux, the value of the SWTRG field can be either 4 or 5.<br>~~NOTE~~|
||000b - Reserved<br>001b - Switch after request succeeded.<br>010b - Switch after the request failed because of an inactive target clock and the current clock is<br>FIRC.<br>011b - Switch after the request failed because of an inactive current clock and the current clock is<br>FIRC.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

889 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||100b - Switch to FIRC because of a safe clock request or reset succeeded.<br>101b - Switch to FIRC because of a safe clock request or reset succeeded, but the previous<br>current clock source was inactive.<br>110b - Reserved<br>111b - Reserved|
|16<br>SWIP|Switch in progress<br>New clock switch request can only be given three clock cycles after the completion of the<br>previous request.<br>~~NOTE~~|
||0b - Clock source switching is complete.<br>1b - Clock source switching is in progress.|
|15-4<br>—|This field is reserved and reads return zeros.|
|3<br>SAFE_SW|Safe clock request<br>This field provides an indication of whether a switch to safe clock operation was requested during the<br>previous/ongoing request on clock mux 8.<br>0b - No safe clock switch operation was requested.<br>1b - Safe clock switch operation was requested.|
|2<br>CLK_SW|Clock switch<br>This field provides an indication of whether a clock switch operation was requested during the previous/<br>ongoing request on clock mux 8.<br>0b - No clock switch operation was requested.<br>1b - Clock switch operation was requested.|
|1-0<br>—|This field is reserved and reads return zeros.|



### 24.5.48 Clock Mux 8 Divider 0 Control Register (MUX_8_DC_0) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_8_DC_0|508h|



##### Function 

This register controls the clock divider 0 for clock mux 8. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

890 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

This divider is a 50% duty cycle divider. 

~~<mark>NOTE</mark>~~ 

The update to the fields of this register should be an atomic write, that is, one single write should update the complete register. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|DE|||||0|||||||DIV||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|Divider enable|
|DE|0b - Divider is disabled.<br>1b - Divider is enabled.|
|30-22<br>—|This field is reserved and reads return zeros.|
|21-16|Division value|
|DIV|This field provides the division value for the clock divider. The clock period of the clock after division is<br>'DIV+1' times the time period of the current input clock to the divider.|
|15-0<br>—|This field is reserved and reads return zeros.|



### 24.5.49 Clock Mux 8 Divider Update Status Register (MUX_8_DIV_UPD_STAT) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_8_DIV_UPD_STAT|53Ch|



##### Function 

This register provides the update status of the clock dividers corresponding to clock mux 8. When a write operation on any divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

891 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 when the corresponding divider update is pending. 

~~<mark>NOTE</mark>~~ Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of whether any divider(s) are implemented inside MC_CGM clock mux. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||||||||0||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0||||||||DIV_<br>STAT|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-1|This field is reserved and reads return zeros.|
|—||
|0|Divider status for clock mux 8|
|DIV_STAT|On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is<br>fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux<br>to a new clock source:<br>1. Switch the mux to a working clock source without polling this field.<br>2. Update MUX_n_DC_m and poll this field.<br>0b - No divider configuration update is pending.<br>1b - Divider configuration update on at least one divider associated with this multiplexer is<br>pending.|



### 24.5.50 Clock Mux 9 Select Control Register (MUX_9_CSC) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_9_CSC|540h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

892 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Function 

This register provides the clock source selection control for clock mux 9. Clock mux 9 implements hardware control clock switching ensuring that the clock switch happens in a graceful manner (without glitches). See the "Hardware-controlled clock multiplexer" section for details. 

This register is reset on destructive reset only. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||0||||SELCTL|||||||0|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R||||||0|||||||SAFE_|CLK_|0|
|W|||||||||||||SW|SW||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



##### Fields 

|Field|Function|
|---|---|
|31-29<br>—|This field is reserved and reads return zeros.|
|28-24|Clock source selection control|
|SELCTL|Selects the source clock for clock mux 9. The reserved values are not displayed.<br>0_0000b - FIRC<br>0_0010b - FXOSC<br>0_1000b - PLL_PHI0_CLK<br>0_1100b - PLL1_PHI0_CLK<br>1_1000b - EMAC_RMII_TX_CLK<br>1_1001b - EMAC_RX_CLK|
|23-4<br>—|This field is reserved and reads return zeros.|
|3|Safe clock request|
|SAFE_SW|Writing 1 to this bit makes a safe clock switch request to FIRC. After a safe clock switch operation is<br>requested, this bit is auto cleared and a corresponding bit in the status register is set.|
|2<br>CLK_SW|Clock switch|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

893 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||Writing 1 to this bit makes a clock switch request to clock mux 9. After a clock switch operation is requested,<br>this bit is auto cleared and a corresponding bit in the status register is set.|
|1-0<br>—|This field is reserved and reads return zeros.|



### 24.5.51 Clock Mux 9 Select Status Register (MUX_9_CSS) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_9_CSS|544h|



##### Function 

This register provides the current clock source selection status for clock mux 9. 

This register is reset on destructive reset only. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||0||||SELSTAT||||0||||SWTRG||SWIP|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|1|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||0|||||||SAFE_<br>SW|CLK_<br>SW||0|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function|
|---|---|
|31-29|This field is reserved and reads return zeros.|
|—||
|28-24|Clock source selection status|
|SELSTAT|This value indicates the current source selected for clock mux 9. The reserved values are not displayed.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

894 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0895-03.png)


<!-- Start of picture text -->
Field Function<br>0_0000b - FIRC<br>0_0010b - FXOSC<br>0_1000b - PLL_PHI0_CLK<br>0_1100b - PLL1_PHI0_CLK<br>1_1000b - EMAC_RMII_TX_CLK<br>1_1001b - EMAC_RX_CLK<br>23-20 This field is reserved and reads return zeros.<br>—<br>19-17 Switch trigger cause<br>SWTRG This value indicates the cause for the latest clock source switch.<br>  NOTE<br>If the clock fails, followed by multiple safe clock switch requests for MC_CGM hardware<br>clock mux, the value of the SWTRG field can be either 4 or 5.<br>000b - Reserved<br>001b - Switch after request succeeded.<br>010b - Switch after the request failed because of an inactive target clock and the current clock is<br>FIRC.<br>011b - Switch after the request failed because of an inactive current clock and the current clock is<br>FIRC.<br>100b - Switch to FIRC because of a safe clock request or reset succeeded.<br>101b - Switch to FIRC because of a safe clock request or reset succeeded, but the previous<br>current clock source was inactive.<br>110b - Reserved<br>111b - Reserved<br>16 Switch in progress<br>SWIP<br>  NOTE<br>New clock switch request can only be given three clock cycles after the completion of the<br>previous request.<br>0b - Clock source switching is complete.<br>1b - Clock source switching is in progress.<br>15-4 This field is reserved and reads return zeros.<br>—<br>3 Safe clock request<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

895 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|SAFE_SW|This field provides an indication of whether a switch to safe clock operation was requested during the<br>previous/ongoing request on clock mux 9.<br>0b - No safe clock switch operation was requested.<br>1b - Safe clock switch operation was requested.|
|2|Clock switch|
|CLK_SW|This field provides an indication of whether a clock switch operation was requested during the previous/<br>ongoing request on clock mux 9.|
||0b - No clock switch operation was requested.<br>1b - Clock switch operation was requested.|
|1-0<br>—|This field is reserved and reads return zeros.|



### 24.5.52 Clock Mux 9 Divider 0 Control Register (MUX_9_DC_0) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_9_DC_0|548h|



##### Function 

This register controls the clock divider 0 for clock mux 9. 

This divider is a 50% duty cycle divider. 

~~<mark>NOTE</mark>~~ 

The update to the fields of this register should be an atomic write, that is, one single write should update the complete register. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|DE|||||0|||||||DIV||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||0|||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

896 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Fields 

|Field|Function|
|---|---|
|31|Divider enable|
|DE|0b - Divider is disabled.<br>1b - Divider is enabled.|
|30-22<br>—|This field is reserved and reads return zeros.|
|21-16|Division value|
|DIV|This field provides the division value for the clock divider. The clock period of the clock after division is<br>'DIV+1' times the time period of the current input clock to the divider.|
|15-0<br>—|This field is reserved and reads return zeros.|



### 24.5.53 Clock Mux 9 Divider Update Status Register (MUX_9_DIV_UPD_STAT) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_9_DIV_UPD_STAT|57Ch|



##### Function 

This register provides the update status of the clock dividers corresponding to clock mux 9. When a write operation on any divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 when the corresponding divider update is pending. 

~~<mark>NOTE</mark>~~ 

Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of whether any divider(s) are implemented inside MC_CGM clock mux. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

897 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0||||||||DIV_<br>STAT|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-1|This field is reserved and reads return zeros.|
|—||
|0|Divider status for clock mux 9|
|DIV_STAT|On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is<br>fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux<br>to a new clock source:<br>1. Switch the mux to a working clock source without polling this field.<br>2. Update MUX_n_DC_m and poll this field.<br>0b - No divider configuration update is pending.<br>1b - Divider configuration update on at least one divider associated with this multiplexer is<br>pending.|



### 24.5.54 Clock Mux 10 Select Control Register (MUX_10_CSC) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_10_CSC|580h|



##### Function 

This register provides the clock source selection control for clock mux 10. Clock mux 10 implements hardware control clock switching ensuring that the clock switch happens in a graceful manner (without glitches). See the "Hardware-controlled clock multiplexer" section for details. 

This register is reset on destructive reset only. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

898 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||0||||SELC|TL||||||0|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R||||||0|||||||SAFE_|CLK_|0|
|W|||||||||||||SW|SW||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



##### Fields 

|Field|Function|
|---|---|
|31-28<br>—|This field is reserved and reads return zeros.|
|27-24<br>SELCTL|Clock source selection control<br>Selects the source clock for clock mux 10. The reserved values are not displayed.<br>0000b - FIRC<br>0010b - FXOSC<br>1001b - PLL_PHI1_CLK<br>1100b - PLL1_PHI0_CLK|
|23-4<br>—<br>3|This field is reserved and reads return zeros.<br>Safe clock request|
|SAFE_SW|Writing 1 to this bit makes a safe clock switch request to FIRC. After a safe clock switch operation is<br>requested, this bit is auto cleared and a corresponding bit in the status register is set.|
|2|Clock switch|
|CLK_SW|Writing 1 to this bit makes a clock switch request to clock mux 10. After a clock switch operation is requested,<br>this bit is auto cleared and a corresponding bit in the status register is set.|
|1-0<br>—|This field is reserved and reads return zeros.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

899 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

### 24.5.55 Clock Mux 10 Select Status Register (MUX_10_CSS) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_10_CSS|584h|



##### Function 

This register provides the current clock source selection status for clock mux 10. 

This register is reset on destructive reset only. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0900-09.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 SELSTAT  0 SWTRG  SWIP<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>SAFE_ CLK_<br>R 0 0<br>SW  SW<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-28|This field is reserved and reads return zeros.|
|—||
|27-24|Clock source selection status|
|SELSTAT|This value indicates the current source selected for clock mux 10. The reserved values are not<br>displayed.|
||0000b - FIRC|
||0010b - FXOSC|
||1001b - PLL_PHI1_CLK|
||1100b - PLL1_PHI0_CLK|
|23-20<br>—|This field is reserved and reads return zeros.|
|19-17|Switch trigger cause|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

900 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|SWTRG|This value indicates the cause for the latest clock source switch.|
||If the clock fails, followed by multiple safe clock switch requests for MC_CGM hardware<br>clock mux, the value of the SWTRG field can be either 4 or 5.<br>~~NOTE~~|
||000b - Reserved<br>001b - Switch after request succeeded.<br>010b - Switch after the request failed because of an inactive target clock and the current clock is<br>FIRC.<br>011b - Switch after the request failed because of an inactive current clock and the current clock is<br>FIRC.<br>100b - Switch to FIRC because of a safe clock request or reset succeeded.|
||101b - Switch to FIRC because of a safe clock request or reset succeeded, but the previous<br>current clock source was inactive.<br>110b - Reserved|
||111b - Reserved|
|16<br>SWIP|Switch in progress<br>New clock switch request can only be given three clock cycles after the completion of the<br>previous request.<br>~~NOTE~~|
||0b - Clock source switching is complete.<br>1b - Clock source switching is in progress.|
|15-4<br>—|This field is reserved and reads return zeros.|
|3<br>SAFE_SW|Safe clock request<br>This field provides an indication of whether a switch to safe clock operation was requested during the<br>previous/ongoing request on clock mux 10.<br>0b - No safe clock switch operation was requested.<br>1b - Safe clock switch operation was requested.|
|2|Clock switch|
|CLK_SW|This field provides an indication of whether a clock switch operation was requested during the previous/<br>ongoing request on clock mux 10.<br>0b - No clock switch operation was requested.<br>1b - Clock switch operation was requested.|
|1-0|This field is reserved and reads return zeros.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

901 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

Table continued from the previous page... 

|Field<br>Function<br>—|
|---|



### 24.5.56 Clock Mux 10 Divider 0 Control Register (MUX_10_DC_0) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_10_DC_0|588h|



##### Function 

This register controls the clock divider 0 for clock mux 10. 

This divider is a 50% duty cycle divider. 

~~<mark>NOTE</mark>~~ 

The update to the fields of this register should be an atomic write, that is, one single write should update the complete register. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|DE|||||||0|||||||DIV||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|Divider enable|
|DE|0b - Divider is disabled.|
||1b - Divider is enabled.|
|30-19<br>—|This field is reserved and reads return zeros.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

902 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|18-16|Division value|
|DIV|This field provides the division value for the clock divider. The clock period of the clock after division is<br>'DIV+1' times the time period of the current input clock to the divider.|
|15-0<br>—|This field is reserved and reads return zeros.|



### 24.5.57 Clock Mux 10 Divider Update Status Register (MUX_10_DIV_UPD_STAT) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_10_DIV_UPD_STA<br>T|5BCh|



##### Function 

This register provides the update status of the clock dividers corresponding to clock mux 10. When a write operation on any divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 when the corresponding divider update is pending. 

~~<mark>NOTE</mark>~~ 

Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of whether any divider(s) are implemented inside MC_CGM clock mux. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0903-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>DIV_<br>R 0<br>STAT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

903 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Fields 

|Field|Function|
|---|---|
|31-1|This field is reserved and reads return zeros.|
|—||
|0|Divider status for clock mux 10|
|DIV_STAT|On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is<br>fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux<br>to a new clock source:<br>1. Switch the mux to a working clock source without polling this field.<br>2. Update MUX_n_DC_m and poll this field.<br>0b - No divider configuration update is pending.<br>1b - Divider configuration update on at least one divider associated with this multiplexer is<br>pending.|



### 24.5.58 Clock Mux 11 Select Control Register (MUX_11_CSC) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_11_CSC|5C0h|



##### Function 

This register provides the clock source selection control of clock mux 11. Clock mux 11 implements software control clock switching, and a graceful clock switch can be performed by executing a sequence of steps in software. See "Software-controlled clock multiplexer" section for details. 

This register is reset on destructive reset only. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0904-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0<br>SELCTL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>FCG  CG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

904 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Fields 

|Field|Function|
|---|---|
|31-28<br>—|This field is reserved and reads return zeros.|
|27-24<br>SELCTL|Clock source selection control<br>Selects the source clock for clock mux 11. The reserved values are not displayed.<br>0000b - FIRC<br>0010b - FXOSC<br>1000b - PLL_PHI0_CLK<br>1001b - PLL_PHI1_CLK<br>1100b - PLL1_PHI0_CLK<br>1101b - PLL1_PHI1_CLK|
|23-4<br>—|This field is reserved and reads return zeros.|
|3<br>FCG|Force clock gate<br>Writing 1 to this bit gates the clock at the output of clock mux 11 to logic-0 irrespective of the logic level of the<br>currently selected clock. Clock gating using this bit should only be performed when it is insured that current<br>clock source is inactive.|
|2<br>CG|Clock gate<br>Writing 1 to this bit gates the clock at the output of clock mux 11 to logic-0. Using this bit it is insured that no<br>glitches are resulted when gating the clock.|
|1-0<br>—|This field is reserved and reads return zeros.|



### 24.5.59 Clock Mux 11 Select Status Register (MUX_11_CSS) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_11_CSS|5C4h|



##### Function 

This register provides the current clock source selection status for clock mux 11. 

This register is reset on destructive reset only. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

905 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||0||||SELS|TAT|||0|||0||CS|GRIP|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||||||0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-28<br>—|This field is reserved and reads return zeros.|
|27-24|Clock source selection status|
|SELSTAT|This value indicates the current source selected for clock mux 11. The reserved values are not<br>displayed.<br>0000b - FIRC<br>0010b - FXOSC<br>1000b - PLL_PHI0_CLK<br>1001b - PLL_PHI1_CLK<br>1100b - PLL1_PHI0_CLK|
||1101b - PLL1_PHI1_CLK|
|23-20<br>—|This field is reserved and reads return zeros.|
|19-18<br>—|This field is reserved and reads return zeros.|
|17|Clock status|
|CS|This field indicates state of the clock at the output of the clock mux.<br>0b - Clock is gated to logic-0 at output of clock mux<br>1b - Clock mux is transparent. Active clock pulses at input of clock mux results in same number of<br>pulses at its output|
|16<br>GRIP|Gating request is in progress.<br>When a clock gate request is given this bit indicates if the clock gating at the output of mux has completed<br>or not.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

906 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Clock source gating or ungating has completed.|
||1b - Clock source gating or ungating is in progress.|
|15-0<br>—|This field is reserved and reads return zeros.|



### 24.5.60 Clock Mux 11 Divider 0 Control Register (MUX_11_DC_0) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_11_DC_0|5C8h|



##### Function 

This register controls the clock divider 0 for clock mux 11. 

This divider is a 50% duty cycle divider. 

~~<mark>NOTE</mark>~~ 

The update to the fields of this register should be an atomic write, that is, one single write should update the complete register. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18||17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|DE||||||0|||||||DI|V|||
|Reset|1|0|0|0|0|0|0|0|0|0|0|0|0|0||0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2||1|0|
|R||||||||0||||||||||
|W||||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0||0|0|



Fields 

|Field|Function|
|---|---|
|31|Divider enable|
|DE|0b - Divider is disabled.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

907 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - Divider is enabled.|
|30-20|This field is reserved and reads return zeros.|
|—||
|19-16|Division value|
|DIV|This field provides the division value for the clock divider. The clock period of the clock after division is<br>'DIV+1' times the time period of the current input clock to the divider.|
|15-0<br>—|This field is reserved and reads return zeros.|



### 24.5.61 Clock Mux 11 Divider Update Status Register (MUX_11_DIV_UPD_STAT) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_11_DIV_UPD_STA<br>T|5FCh|



##### Function 

This register provides the update status of the clock dividers corresponding to clock mux 11. When a write operation on any divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 when the corresponding divider update is pending. 

~~<mark>NOTE</mark>~~ 

Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of whether any divider(s) are implemented inside MC_CGM clock mux. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0||||||||DIV_<br>STAT|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

908 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Fields 

|Field|Function|
|---|---|
|31-1|This field is reserved and reads return zeros.|
|—||
|0|Divider status for clock mux 11|
|DIV_STAT|On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is<br>fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux<br>to a new clock source:<br>1. Switch the mux to a working clock source without polling this field.<br>2. Update MUX_n_DC_m and poll this field.<br>0b - No divider configuration update is pending.<br>1b - Divider configuration update on at least one divider associated with this multiplexer is<br>pending.|



### 24.5.62 Clock Mux 13 Select Control Register (MUX_13_CSC) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_13_CSC|640h|



##### Function 

This register provides the clock source selection control for clock mux 13. Clock mux 13 implements hardware control clock switching ensuring that the clock switch happens in a graceful manner (without glitches). See the "Hardware-controlled clock multiplexer" section for details. 

This register is reset on destructive reset only. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0909-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0<br>SELCTL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 SAFE_ CLK_ 0<br>W SW  SW<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

909 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Fields 

|Field|Function|
|---|---|
|31-29<br>—<br>28-24<br>SELCTL|This field is reserved and reads return zeros.<br>Clock source selection control<br>Selects the source clock for clock mux 13. The reserved values are not displayed.<br>0_0000b - FIRC<br>0_0010b - FXOSC<br>1_0110b - AIPS_PLAT_CLK|
|23-4<br>—|This field is reserved and reads return zeros.|
|3|Safe clock request|
|SAFE_SW|Writing 1 to this bit makes a safe clock switch request to FIRC. After a safe clock switch operation is<br>requested, this bit is auto cleared and a corresponding bit in the status register is set.|
|2|Clock switch|
|CLK_SW|Writing 1 to this bit makes a clock switch request to clock mux 13. After a clock switch operation is requested,<br>this bit is auto cleared and a corresponding bit in the status register is set.|
|1-0<br>—|This field is reserved and reads return zeros.|



### 24.5.63 Clock Mux 13 Select Status Register (MUX_13_CSS) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_13_CSS|644h|



##### Function 

This register provides the current clock source selection status for clock mux 13. 

This register is reset on destructive reset only. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

910 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||0||||SELSTAT||||0||||SWTRG||SWIP|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|1|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||0|||||||SAFE_<br>SW|CLK_<br>SW||0|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-29<br>—|This field is reserved and reads return zeros.|
|28-24|Clock source selection status|
|SELSTAT|This value indicates the current source selected for clock mux 13. The reserved values are not<br>displayed.<br>0_0000b - FIRC<br>0_0010b - FXOSC<br>1_0110b - AIPS_PLAT_CLK|
|23-20<br>—|This field is reserved and reads return zeros.|
|19-17<br>SWTRG|Switch trigger cause<br>This value indicates the cause for the latest clock source switch.<br>If the clock fails, followed by multiple safe clock switch requests for MC_CGM hardware<br>clock mux, the value of the SWTRG field can be either 4 or 5.<br>~~NOTE~~<br>000b - Reserved<br>001b - Switch after request succeeded.<br>010b - Switch after the request failed because of an inactive target clock and the current clock is<br>FIRC.<br>011b - Switch after the request failed because of an inactive current clock and the current clock is<br>FIRC.<br>100b - Switch to FIRC because of a safe clock request or reset succeeded.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

911 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||101b - Switch to FIRC because of a safe clock request or reset succeeded, but the previous<br>current clock source was inactive.<br>110b - Reserved<br>111b - Reserved|
|16<br>SWIP|Switch in progress<br>New clock switch request can only be given three clock cycles after the completion of the<br>previous request.<br>~~NOTE~~|
||0b - Clock source switching is complete.<br>1b - Clock source switching is in progress.|
|15-4<br>—|This field is reserved and reads return zeros.|
|3<br>SAFE_SW|Safe clock request<br>This field provides an indication of whether a switch to safe clock operation was requested during the<br>previous/ongoing request on clock mux 13.<br>0b - No safe clock switch operation was requested.<br>1b - Safe clock switch operation was requested.|
|2<br>CLK_SW|Clock switch<br>This field provides an indication of whether a clock switch operation was requested during the previous/<br>ongoing request on clock mux 13.<br>0b - No clock switch operation was requested.<br>1b - Clock switch operation was requested.|
|1-0<br>—|This field is reserved and reads return zeros.|



### 24.5.64 Clock Mux 13 Divider 0 Control Register (MUX_13_DC_0) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_13_DC_0|648h|



##### Function 

This register controls the clock divider 0 for clock mux 13. 

This divider is a 50% duty cycle divider. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

912 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

~~<mark>NOTE</mark>~~ 

The update to the fields of this register should be an atomic write, that is, one single write should update the complete register. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0913-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>DE  DIV<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Divider enable|
|DE|0b - Divider is disabled.<br>1b - Divider is enabled.|
|30-17|This field is reserved and reads return zeros.|
|—||
|16|Division value|
|DIV|This field provides the division value for the clock divider. The clock period of the clock after division is<br>'DIV+1' times the time period of the current input clock to the divider.|
|15-0<br>—|This field is reserved and reads return zeros.|



### 24.5.65 Clock Mux 13 Divider Update Status Register (MUX_13_DIV_UPD_STAT) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_13_DIV_UPD_STA<br>T|67Ch|



##### Function 

This register provides the update status of the clock dividers corresponding to clock mux 13. When a write operation on any divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

913 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 when the corresponding divider update is pending. 

~~<mark>NOTE</mark>~~ 

Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of whether any divider(s) are implemented inside MC_CGM clock mux. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||||||||0||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0||||||||DIV_<br>STAT|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-1|This field is reserved and reads return zeros.|
|—||
|0|Divider status for clock mux 13|
|DIV_STAT|On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is<br>fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux<br>to a new clock source:<br>1. Switch the mux to a working clock source without polling this field.<br>2. Update MUX_n_DC_m and poll this field.<br>0b - No divider configuration update is pending.<br>1b - Divider configuration update on at least one divider associated with this multiplexer is<br>pending.|



### 24.5.66 Clock Mux 14 Select Control Register (MUX_14_CSC) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_14_CSC|680h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

914 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Function 

This register provides the clock source selection control for clock mux 14. Clock mux 14 implements hardware control clock switching ensuring that the clock switch happens in a graceful manner (without glitches). See the "Hardware-controlled clock multiplexer" section for details. 

This register is reset on destructive reset only. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||0||||SELCTL|||||||0|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R||||||0|||||||SAFE_|CLK_|0|
|W|||||||||||||SW|SW||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



##### Fields 

|Field|Function|
|---|---|
|31-29<br>—<br>28-24<br>SELCTL|This field is reserved and reads return zeros.<br>Clock source selection control<br>Selects the source clock for clock mux 14. The reserved values are not displayed.<br>0_0000b - FIRC<br>0_0010b - FXOSC<br>0_1001b - PLL_PHI1_CLK<br>0_1110b - PLL1_PHI2_CLK|
|23-4<br>—|This field is reserved and reads return zeros.|
|3<br>SAFE_SW|Safe clock request<br>Writing 1 to this bit makes a safe clock switch request to FIRC. After a safe clock switch operation is<br>requested, this bit is auto cleared and a corresponding bit in the status register is set.|
|2|Clock switch|
|CLK_SW|Writing 1 to this bit makes a clock switch request to clock mux 14. After a clock switch operation is requested,<br>this bit is auto cleared and a corresponding bit in the status register is set.|
|1-0<br>—|This field is reserved and reads return zeros.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

915 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

### 24.5.67 Clock Mux 14 Select Status Register (MUX_14_CSS) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_14_CSS|684h|



##### Function 

This register provides the current clock source selection status for clock mux 14. 

This register is reset on destructive reset only. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0916-09.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 SELSTAT  0 SWTRG  SWIP<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>SAFE_ CLK_<br>R 0 0<br>SW  SW<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-29|This field is reserved and reads return zeros.|
|—||
|28-24|Clock source selection status|
|SELSTAT|This value indicates the current source selected for clock mux 14. The reserved values are not<br>displayed.|
||0_0000b - FIRC|
||0_0010b - FXOSC|
||0_1001b - PLL_PHI1_CLK|
||0_1110b - PLL1_PHI2_CLK|
|23-20<br>—|This field is reserved and reads return zeros.|
|19-17|Switch trigger cause|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

916 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|SWTRG|This value indicates the cause for the latest clock source switch.|
||If the clock fails, followed by multiple safe clock switch requests for MC_CGM hardware<br>clock mux, the value of the SWTRG field can be either 4 or 5.<br>~~NOTE~~|
||000b - Reserved<br>001b - Switch after request succeeded.<br>010b - Switch after the request failed because of an inactive target clock and the current clock is<br>FIRC.<br>011b - Switch after the request failed because of an inactive current clock and the current clock is<br>FIRC.<br>100b - Switch to FIRC because of a safe clock request or reset succeeded.|
||101b - Switch to FIRC because of a safe clock request or reset succeeded, but the previous<br>current clock source was inactive.<br>110b - Reserved|
||111b - Reserved|
|16<br>SWIP|Switch in progress<br>New clock switch request can only be given three clock cycles after the completion of the<br>previous request.<br>~~NOTE~~|
||0b - Clock source switching is complete.<br>1b - Clock source switching is in progress.|
|15-4<br>—|This field is reserved and reads return zeros.|
|3<br>SAFE_SW|Safe clock request<br>This field provides an indication of whether a switch to safe clock operation was requested during the<br>previous/ongoing request on clock mux 14.<br>0b - No safe clock switch operation was requested.<br>1b - Safe clock switch operation was requested.|
|2|Clock switch|
|CLK_SW|This field provides an indication of whether a clock switch operation was requested during the previous/<br>ongoing request on clock mux 14.<br>0b - No clock switch operation was requested.<br>1b - Clock switch operation was requested.|
|1-0|This field is reserved and reads return zeros.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

917 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

Table continued from the previous page... 

|Field<br>Function<br>—|
|---|



### 24.5.68 Clock Mux 14 Divider 0 Control Register (MUX_14_DC_0) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_14_DC_0|688h|



##### Function 

This register controls the clock divider 0 for clock mux 14. 

This divider is a 50% duty cycle divider. 

~~<mark>NOTE</mark>~~ 

The update to the fields of this register should be an atomic write, that is, one single write should update the complete register. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|DE|||||||0||||||||DIV|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|Divider enable|
|DE|0b - Divider is disabled.|
||1b - Divider is enabled.|
|30-17<br>—|This field is reserved and reads return zeros.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

918 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|16|Division value|
|DIV|This field provides the division value for the clock divider. The clock period of the clock after division is<br>'DIV+1' times the time period of the current input clock to the divider.|
|15-0<br>—|This field is reserved and reads return zeros.|



### 24.5.69 Clock Mux 14 Divider Update Status Register (MUX_14_DIV_UPD_STAT) 

##### Offset 

|Register|Offset|
|---|---|
|MUX_14_DIV_UPD_STA<br>T|6BCh|



##### Function 

This register provides the update status of the clock dividers corresponding to clock mux 14. When a write operation on any divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 when the corresponding divider update is pending. 

~~<mark>NOTE</mark>~~ 

Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of whether any divider(s) are implemented inside MC_CGM clock mux. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/024_Clock_Generation_Module_-MC_CGM-/S32K3XXRM_数据表.pdf-0919-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>DIV_<br>R 0<br>STAT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

919 / 4640 

NXP Semiconductors 

Clock Generation Module (MC_CGM) 

##### Fields 

|Field|Function|
|---|---|
|31-1|This field is reserved and reads return zeros.|
|—||
|0|Divider status for clock mux 14|
|DIV_STAT|On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is<br>fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux<br>to a new clock source:<br>1. Switch the mux to a working clock source without polling this field.<br>2. Update MUX_n_DC_m and poll this field.<br>0b - No divider configuration update is pending.<br>1b - Divider configuration update on at least one divider associated with this multiplexer is<br>pending.|



## 24.6 Glossary 

PCFS Progressive clock frequency switching LCM Least common multiple 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

920 / 4640 

