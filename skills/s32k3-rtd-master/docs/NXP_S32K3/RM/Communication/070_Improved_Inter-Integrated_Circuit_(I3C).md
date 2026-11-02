NXP Semiconductors 

# Chapter 70 Improved Inter-Integrated Circuit (I3C) 

## 70.1 Chip-specific I3C information 

### 70.1.1 I3C instances and configuration 

Table 407. I3C instances 

|Instance|K311/K312/K342/K358|K3x4|
|---|---|---|
|I3C|Yes|No|



~~<mark>NOTE</mark>~~ 

- I3C muxing on S32K312 pins PTD5 and PTC16 work upto maximum SCL clock frequency of 10MHz. 

- For configuring SDA and SCL pad type, see column 'Pad Type' in 'S32K3xx_IO Signal Table' worksheet of the IOMUX files attached to this document. 

I3C includes following features: 

- Supports Tx FIFO and Rx FIFO of size 16 bytes. 

- Allows half-word read and write. 

- Supports mipi specification of v1.0. 

- Supports static address. 

- Allows DDR mode. 

~~<mark>NOTE</mark>~~ 

I3C offers an internal delayed CLK which can be used instead of pad loopback clock, in case any issue is seen on chip. 

~~<mark>NOTE</mark>~~ 

In I3C there are Sync and Async timing controls 0/1/2/3 but the controller supports asynchronous mode 0. 

## 70.2 Overview 

[DIP_I3C_00001]The MIPI Alliance Improved Inter-Integrated Circuit (MIPI I3C) brings major improvements in use and power over I2C, and provides an alternative to SPI for mid-speed applications.[end] 

The I3C bus protocol supports: 

- In-band interrupts: interrupts can go from Slave to Master without extra wires, such that the Master knows which Slave sent the interrupt. 

- Common Command Codes (CCC) 

- Dynamic addressing 

- Multi-master/multi-drop 

- Hot-Join (HJ) 

- I2C compatibility 

The I3C peripheral supports all required and most optional features of the MIPI Alliance Specification for I3C, v1.0 and v1.1, except for the ternary data rates (HDR-TSP and HDR-TSL). 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2530 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

### 70.2.1 Block diagram 

The following figure shows the I3C block diagram. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2531-04.png)


<!-- Start of picture text -->
Components<br>CCCs<br>Optional<br>Fixed SET<br>DASA/NEWDA<br>OTHER CCCs DAA MODE<br>OTHER CCCs<br>SDR ENGINE<br>Optional EVENTS EXIT DETECTOR SCL<br>slow clock (e.g.IBI)<br>SDA<br>Optional<br>system signals REGISTERS<br>(IRQ, info, DMA, etc.) HDR-DDR<br>EXTRA REGISTERS<br>FIFO BLOCK<br>IF MASTER MASTER<br>BUS OR PSEUDO BUS<br><!-- End of picture text -->

Figure 367. [DIP_I3C_00057]I3C block diagram[end] 

### 70.2.2 Features 

##### I3C module: 

- [DIP_I3C_00003]2-wire multi-drop bus capable of 12.5 MHz clock speeds, with up to 11 devices.[end] 

   - Uses standard pads (I2C uses special pads) with 4 mA drive 

   - Slave addresses are dynamically assigned, and slaves do not require a static address.[DIP_I3C_00025] However, slaves may have an I2C static address assigned at start-up, so that the slave can operate on an I2C bus. By default, I3C supports 7-bit I2C style address.[end] 

   - [DIP_I3C_00026]It can also support extended I2C 10-bit addressing through SMAPCTRL1 register.[end] 

   - Slaves may use the inbound SCL clock as the peripheral clock, which means that devices can have slow or inaccurate clocks internally. 

   - Simple slaves can have no internal clock; for example, like a temperature sensor. 

   - [DIP_I3C_00016]I3C master supports handoff from Open Drain to Push-Pull mode for ACK to data transfer.[end] 

   - For reads from a slave, the slave normally ends the read, but the I3C master can also terminate the read. For I2C and SPI, the master must know the length of the data that is being read, but for I3C the master does not require the length of the data being read. 

- [DIP_I3C_00029]In-Band Interrupts (IBI) are allowed, which allow slaves to notify a master.[end] 

   - Can be both equivalent to a separate GPIO, but can also be directly data-bearing. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2531 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

   - IBIs are prioritized, so that if multiple Slaves want to interrupt a master at the same time, then the order is resolved. Dynamic addresses are used to establish the priority of the slaves, which means the master controls the priority of the slaves. 

   - Slaves with lower value dynamic addresses are of higher Priority Levels IBIs. 

   - Interrupts can be started even when the master is not active on the bus, and yet no free-running clock is needed (for that situation). 

   - A time-stamping option allows the resolution of an initial event, not just when an interrupt gets through 

- Built-in commands are in separate space, so that these commands do not collide with normal Master->Slave messages. 

   - Controls bus behavior, modes and states, low power state, inquiries and more 

   - Has additional room for new built-in commands to be used by other groups 

- Organized forms of multi-master modes: 

   - Secondary masters that can use clean handoffs between different Masters 

- [DIP_I3C_00032]Hot-join onto I3C bus allows devices to connect to the bus later than when the bus starts.[end] 

   - This enables a device or module to get onto the I3C bus, because it woke up after power-up, or was physically inserted onto the I3C bus. 

   - Also, provides a clean method for notification when new devices or modules get onto the I3C bus. 

- Capable of using both I2C and I3C buses: 

   - I3C supports specific legacy I2C devices on the bus 

   - I3C Slave devices can operate on I2C buses 

   - Supports bridging to I2C, SPI, UART, and other buses 

- [DIP_I3C_00006]Higher data rate modes are optionally available 

   - Only the master and the specific slave has to support the higher data rate; the other slaves are able to ignore the higher data rate. 

   - Has a High Data Rate - Double Data Rate (HDR-DDR) mode, which is 2x the data rate of SDR (so about 20 Mbps)[end] 

The I3C peripheral supports the full I3C feature set, except for the ternary data rates (HDR-TSP and HDR-TSL). 

## 70.3 Functional description 

The following sections describe functional details of the I3C module. 

### 70.3.1 Operating modes 

This section describes all functional operation modes of the I3C module. 

#### 70.3.1.1 Master vs. slave roles for I3C 

The I3C protocol defines 5 roles for devices on the I3C bus: 

- [DIP_I3C_00007]Main Master : Controls the I3C bus 

- Secondary Master : Controls the I3C with permission from the Main Master, and returns control of the bus back to the Main Master when it (Secondary Master) has finished with its tasks.[end] 

- [DIP_I3C_00008]Slave : Responds to commands from any I3C master [end] 

- I2C Slave : Responds to commands from any I2C slave 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2532 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

The I3C peripheral contains both a master and slave component and can be parameterized to be either master or slave, or both master and slave. However, if the I3C is chosen to be a master, then the I3C peripheral supports slave mode to make handoffs to multiple masters easier to do. 

In general, any I3C master should be able to be a master or a slave, because a master becomes a slave when giving over control to another master. The only exception to this rule would be when using a point-to-point master or when using a master that will never share mastership. 

##### Master requirements 

Master mode uses software that supports the various requirements of the master (including as a Secondary Master): 

- [DIP_I3C_00011]Special handling of Enter Dynamic Address Assignments (ENTDAA) assigning dynamic addresses to each slave. This process is supported by the I3C peripheral but requires the software to make choices.[end] 

- [DIP_I3C_00015]Master can drive SDA in both Open Drain and Push-Pull mode. SDA after Start is in Open Drain and after Repeated Start it is in Push-Pull.[end] 

- [DIP_I3C_00014]SDA is subject to arbitration as both Master and Slave can drive the SDA line. Arbitration is also useful for Handoff from Master to Slave. [end] 

- [DIP_I3C_00018]9th bit of SDA Master write data is an odd parity bit.[end] 

- Building up a table of slaves and their capabilities, which are used to control what kinds of actions and commands may be sent to the slaves. 

- Handling requests such as IBI and master request (handoff). 

- Adjusting clock speed or write-to-read timing to match the slave’s limitations. This can be done in hardware using dividers and uneven duty cycles, but the software must make the decisions. 

- Adjusting the maximum data length. 

- Being a slave after a master handoff to another master 

Additionally, a master needs 3 pins, unless a very precise, high-strength pullup is included in the SDA pad. The 3-pin model allows 1 pad/pin to enable a system-provided pullup, which is sized to system requirements. 

The master needs an accurate clock, capable of a frequency that is a multiple of a frequency between 11 MHz and 12.5 MHz. For example: 

- 24 MHz (multiple of 12 MHz) 

- 48 MHz (multiple of 12 MHz) 

- 25 MHz (multiple of 12.5 MHz) 

- 50 MHz (multiple of 12.5 MHz) 

- 33 MHz (multiple of 11 MHz) 

- 66 MHz (multiple of 11 MHz) 

Higher ratios can also be used. 

##### Slave requirements 

The I3C slave mode is intended to allow the use of simple module, allowing the device implementation to use fewer logic circuits on limited space. For example, when the slave minimum requirements are just I3C SDR mode and a few Common Command Code (CCC) commands. Conversely, slave functionality in the module logic can be increased, increasing the module's area on the device but saving software development costs. 

~~<mark>NOTE</mark>~~ 

The Slave can be scaled for system requirements by doing more in software or in hardware. This decision is made when the module is integrated into the device. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2533 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

[DIP_I3C_00023]I3C slave acts like I2C slave on I3C buses 

The I3C slave, if assigned an I2C static address, acts like an I2C device when the I3C slave first comes up. If the I3C slave is placed on an I2C bus with an I2C master, then the I3C slave stays in I2C mode and operates normally.[end] The software knows that the I3C slave is in I2C mode, because: 

- There has not been a DACHG indicating that a dynamic address was assigned 

[DIP_I3C_00028]If full I2C support for Fast Mode (FM) and Fast Mode Plus (FM+) is required, then the pads must support a 50 ns spike filter, which must be turned off when the I3C 0x7E broadcast address is seen (indicating an I3C master). You can turn off the spike filters by hardware using the raw net indicating that the address was seen or by software. [end][DIP_I3C_00024] A 50 ns spike filter is not needed for the I3C to operate on an I2C bus. Therefore, the spike filter is not a requirement for the I3C peripheral.[end] 

Depending on the configuration, the block supports most I2C features, except for clock stretching. These features include Extended 10-bit address, DeviceID, SW reset, and HS mode (affects pads). 

How a slave re-joins the I3C bus 

When a slave powers up or after a hard reset, when the slave tries to rejoin the I3C bus, the slave needs a new Dynamic Address (DA). The slave provides 3 ways to rejoin the I3C bus: 

- If the dynamic address is lost, then Hot-Join is used. 

- If the dynamic address is retained in the peripheral (for example, with SRFFs), then the SCONFIG[OFFLINE] bit is used (see below). 

When SCONFIG[SLVENA] = 1, the SCONFIG[OFFLINE] may be set. [DIP_I3C_00033]This causes the peripheral to safely rejoin the bus, by ensuring that the I3C bus is not in High Data Rate (HDR) mode, using the same approach as S0/S1 exit does. Waiting for the first of the HDR Exit Pattern, or waiting for 60 µs of SCL and SDA lines not changing.[end] 

After using SCONFIG[OFFLINE], the I3C peripheral cannot safely use IBI until it sees a STOP (SSTATUS register), which ensures that the next START is safe to use for IBI). 

If the application needs to do an IBI, then the application should wait for the first STOP (SSTATUS register), or should wait for 200 µs of SCL and SDA lines being High. This can be done using the SSTATUS and SINTSET controls. 

- If the SSTATUS indicates that the bus is not busy and the peripheral interrupts on START or STOP, then use a timer to measure 200 µs. If the timer goes off with no START or STOP, then it is safe to use IBI. 

- If a START causes an interrupt, then the timer should be turned off and the application should wait for a STOP. 

- If a STOP causes an interrupt, then it is safe to use IBI. 

#### 70.3.1.2 Using the I3C Master for I2C and I3C 

The I3C Master operates with a set of built-in capabilities mixed with the application flow. 

- Built-in Enter Dynamic Address Assignment (ENTDAA) mechanism to simplify the assignment of DAs to slaves (when Set Dynamic Address from Static Address (SETDASA) is not available). 

- Request for START+Address with IBI support, including both I2C and I3C modes 

- SDR Write flow via FIFO, with automatic parity in I3C and ACK/NACK detect in I2C 

- SDR Read flow via the FIFO, with an automatic NACK generator for I2C, and optional use of a terminate generator for I3C 

- Request for repeated START+Address or STOP when finished with previous, including both I2C and I3C 

- Auto-IBI mode which responds immediately to a Slave-initiated IBI can be used when in sleep or deep sleep 

- Special message mode for SDR and DDR to simplify for DMA use 

- All SCL, SDA, Pull-up, and High-Keeper controls are automated 

- I2C and I3C Frequency and duty cycle configurations from functional clock 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2534 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

~~<mark>NOTE</mark>~~ 

The MCONFIG register and the MIBIRULES register must be configured before using the Master. 

#### 70.3.1.3 Protocol modes and states 

The following modes are activated in I3C: 

- I2C mode is the default mode on startup. 

   - If no I2C static address is used, this has no effect other than to track frames looking for I3C transitional frames. 

   - If an I2C static address is used, the device can interact with the I2C bus master using the address. 

- While in I2C mode, an I3C Transitory Frame mode occurs whenever the I3C Broadcast address is seen (0x07). In particular: 

   - 0x07 is broadcast and then an ENTDASA from the Master. If there is a static address match or 0x01, the Slave is assigned a Dynamic Address and enters I3C SDR mode. 

   - 0x7E is broadcast and then an ENTDAA from the Master. [DIP_I3C_00009]If the Slave can send a 48b ID out, a Dynamic Address is assigned and the Slave enters I3C SDR mode. [end] 

   - If a Hot-Join arbitrated event generates (sending 0x02 when the Master generates some other address such as 0x7E), there is a conceptual Hot-Join mode. ENTDAA or ENTDASA sets a Dynamic Address to resolve the event and the Slave enters I3C SDR mode. 

      - ~~<mark>NOTE</mark>~~ 

An I3C Slave can operate as a normal I2C slave only when it has a static address. Otherwise, it matches nothing in I2C and waits for the above events. 

- [DIP_I3C_00005]I3C SDR mode is the standard mode once I3C activates, which is defined by a Dynamic Address being assigned. This is the resting mode of I3C and all devices are normally in SDR mode.[end] 

   - RSTDAA CCC causes an exit from SDR mode and a return to I2C mode. This is not normally used. 

   - SETNEWDA does not affect the SDR mode, only the Dynamic Address. 

   - When in SDR mode, the device ignores messages to or from its original I2C static address. 

- [DIP_I3C_00020]I3C CCC command submode of type Direct or Broadcast. 

   - Exit the Broadcast CCC submode by a repeated START or by a STOP. 

   - Exit the Direct CCC submode by a 0x7E broadcast address after a repeated START or by a STOP. 

   - I3C DAA CCC command enters the DAA mode. This is a special mode for DDA. Use STOP to exit. If a Slave has a DA, the command is ignored. 

- I3C SETDASA CCC command enters the Static Address match submode. This allows matching the device’s Static Address (if any). 

   - The command is ignored when a Slave has a Dynamic Address, or the Slave in I2C mode has no Static Address. 

~~<mark>NOTE</mark>~~ 

The special point-to-point address is also matched. 

- I3C HDR modes are activated by ENTHDRn CCC commands with the n value being the type of HDR (0 to 7). This is valid until HDR Exit Pattern, whether supported or not.[end] 

   - DDR included 

   - Exit Pattern detection must be set on at all times to prevent errors. Alternatively, it could be set to only activate on ENTHDR. 

- [DIP_I3C_00065]I3C HDR-BT modes are also activated by ENTHDRn CCC commands and exited by HDR Exit Pattern. [end] 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2535 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

- [DIP_I3C_00066]ML data transfer is available for data transfers between ML-capable I3C Devices that have ML functionality enabled.[end] 

- [DIP_I3C_00060]A special HDR-DDR syntax is used for transmitting Common Command Codes in the HDR-DDR protocol.[end] 

- [DIP_I3C_00062]As an optional feature, multiple I3C Slave Devices can share a single Group Address, allowing a Master Device to send a given I3C Message to all Slave Devices in the Group at once rather than one at a time.[end] 

- The internal states also exist, such as IBI/no-IBI, low-power mode, and so on. These are flagged internally. They are exported to the application and also affect the engine so it does not perform a prohibited operation. 

#### 70.3.1.4 Address match 

The Slave matches 2 of 3 possible addresses, depending on the internal state: 

- 0b111_1110 (written as 0x7E in spec), which is the I3C broadcast address. 

- I2C style Static Address, but only if: 

   - The device has a Static Address. 

   - Is not in I3C mode. Only matches until the ENTDAA or the SETDASA command has assigned a DA. 

~~<mark>NOTE</mark>~~ 

SETDASA matches the Static Address or special point-to-point magic address. 

- I3C DA once assigned by ENTDAA or SETDASA or modified by SETNEWDA. 

The address match is inactive (just listening) for all repeated START commands and also for START, unless an IBI/MR/HotJoin has been activated. If inactive, it simply tries to match. If not matched, it waits for a repeated START or a STOP. [DIP_I3C_00010]If an IBI/MR/HotJoin, the arbitration mechanism is used for START (but never repeated START).[end] 

If matching the 0x7E broadcast address, it listens for a CCC until the next repeated START or a STOP. The CCC_possible bit is set and cleared. 

#### 70.3.1.5 Data handling with or without FIFO 

[DIP_I3C_00034]The low-level slave engine is fed a buffer for to-bus, and provides its buffer for from-bus (so bit insertions do not build a deep mux into a FIFO).[end] 

[DIP_I3C_00048]The full wrapper and so APB interface allows for 3 methods:[end] 

- Ping-pong buffers (two entry FIFOs) for each of from-bus and to-bus only. 

   - This interfaces to the APB register model, if used, using the byte read and byte write regs, along with interrupts. 

   - If not used, these form the buffering and Clock Domain Crossing (CDC) interface for direct nets and external FIFOs. 

   - The from-bus one ends up with a three entry buffer (but two entry FIFO) since it has a holding buffer. The holding buffer in the CLK domain is to keep the path short for an external FIFO (no mux) and to give a bit more time for a processor ISR. 

- [DIP_I3C_00035]Deeper than two entry internal FIFO 

   - These replace the ping-pong buffers with deeper FIFOs which form the CDC interface as well as deeper buffering. [end] 

   - This allows for lower speed system clocks without having to slow the I3C bus rate. 

   - It is possible to engage in only one direction (for example, from-bus). 

   - [DIP_I3C_00036]The TXFIFO depth size can be in the power of 2.[end] 

   - [DIP_I3C_00037]The RXFIFO depth size can be in the power of 2.[end] 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2536 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

- External FIFO that works with the ping-pong buffers. The external FIFO is operating in the system clock domain and moves data to/from the ping-pong buffers a byte at a time. So, the CDC is still in the ping-pong buffers. 

### 70.3.2 Operations 

This section describes the I3C module’s operations. 

#### 70.3.2.1 Reading and writing I2C messages using the normal method 

The normal method: 

1. Set up interrupts. Normally: 

   - a. MCTRLDONE: Optional 

   - b. COMPLETE: To fire when the end of data 

   - c. RXPEND if read: This can be used with the MDATACTRL register to set the FIFO trigger. The alternative is for DMA to read out bytes. 

   - d. TXNOTFULL if write: tThis can be used with the MDATACTRL register to set the FIFO trigger. The alternative is for DMA to supply bytes. 

   - e. IBIWON: The software knows if an IBI has occurred 

   - f. MERRWARN: In case of an error 

2. Write the MCTRL register with: 

   - a. REQUEST set to 1 (EmitStartAddr) 

   - b. TYPE set to 1 (I2C) 

   - c. IBIRESP set depending on how you want IBIs handled 

   - d. DIR set to 1 if Read, or set to 0 if Write 

   - e. ADDR set to the static address of the I2C slave 

   - f. If read, then RDTERM may be set for the length, or may be set as the data is read out (for example, set to 1 (with REQUEST=0) when you want it to stop next). 

3. If Write: Write the MWDATAB register for each byte before the last byte, then write the MWDATABE register for the last byte. 

   - a. This can be done or started before set up interrupts. 

   - b. If there is more data than the FIFO can hold, use the TXNOTFULL interrupt based on the trigger level to allow the application to provide more or use DMA. 

4. If Read: wait for RXPEND, and then read out data via the MRDATAB register. DMA may also be used 

5. On COMPLETE, the message may be ended with a STOP, or a new message started with a repeated START. 

   - a. Write MCTRL with REQUEST of 2 (EmitStop to STOP). Then wait for MCTRLDONE status to be asserted for its completion. (While sending STOP in I2C mode MCONFIG[ODSTOP] should be 1.) 

   - b. Write MCTRL with REQUEST of 1 (EmitStartAddr to start another message). 

~~<mark>NOTE</mark>~~ 

IBI is not possible in this case. 

#### 70.3.2.2 Reading/writing I3C messages using the normal methods (SDR and HDR-DDR) 

The normal method for I3C is the same as for I2C with a few differences. Option 2 is preferred from stopped (bus free condition) when in Single Data Rate (SDR) mode and not in High Data Rate - Double Data Rate (HDR-DDR) mode, because it allows any slave to issue an IBI, and avoids collisions with IBI address. Moreover, it is faster (when MSB of dynamic address is always 0). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2537 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

~~<mark>NOTE</mark>~~ 

HDR-DDR requires writing a command value (7-bit value) for Read or Write. This must be written into the TX FIFO via MWDATAB (or can be combined with the first data byte via MWDATAH). The END bit is not used for this byte. 

1. Set up interrupts. Normally: 

   - MCTRLDONE: Optional 

   - COMPLETE: To fire when end of data 

   - RXPEND if read: This can be used with the MDATACTRL register to set the FIFO trigger. The alternative is for DMA to read out bytes. 

   - TXNOTFULL if Write: This can be used with the MDATACTRL register to set the FIFO trigger. The alternative is for DMA to supply bytes. 

   - IBIWON: So the software knows if an IBI has occurred 

   - [DIP_I3C_00021]MERRWARN: In case of an error[end] 

2. Write the MCTRL register: 

   - Option 1: Write the MCTRL register with: 

      - a. REQUEST set to 1 (EmitStartAddr) 

      - b. TYPE set to 0 (if I3C) or set to 2 (if DDR) 

      - c. IBIRESP set depending on how you want IBIs handled 

      - d. DIR set to 1 (if Read) or set to 0 (if Write) 

      - e. ADDR set to the dynamic address of the I3C slave 

      - f. If read, then optionally RDTERM is set for the maximum length to auto-terminate. 

      - g. If write, then pre-writing the data (MWDATAB or MWDATAW) is preferred to ensure that no time delays waiting on the data. If HDR-DDR, the first byte must be written through MWDATATB only for Read or Write, which is the “Command’ byte (8-bit value). 

   - Option 2: From stopped and not in HDR-DDR mode, write MCTRL register with; 

      - a. REQUEST set to 1 (EmitStartAddr). note: Cannot have pre-written TX data in the FIFO. 

      - b. TYPE set to 0 (I3C) 

      - c. IBIRESP set depending on how you want IBIs to be handled 

      - d. DIR set to 0 

      - e. ADDR set to 0x7E 

      - f. Wait for MCTRLDONE (for example, by interrupt), then proceed with previously mentioned Option 1. This Option 2 method has advantages for IBIs when 7E is emitted on START (but not on repeated STARTs). 

~~<mark>NOTE</mark>~~ 

The Option 2 method does not allow an immediate switch to read. The normal I3C process is to write index, then read data. So, if doing a blind read (no index is written), do not use the Option 2 method. 

3. If Write: then write the MWDATAB register for each byte before the last byte, then write the MWDATABE register for the last byte. For HDR-DDR, the byte with END must be even (2nd, 4th, 6th, and so on) because DDR uses byte-pairs. 

   - This can be done or started before step 1 [REQUEST set to 1 (EmitStartAddr)]) of the Option 1 and not before the Option 2 method. 

   - If there is more data than the FIFO can hold, use the TXNOTFULL interrupt based on the trigger level to allow the application to provide more or use DMA. 

4. If Read, wait for RXPEND, and then read out data using the MRDATAB register. DMA may also be used. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2538 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

5. On COMPLETE, the message may be ended with STOP (or EXIT if HDR), or a new message started with a repeated START (or HDR-Restart if HDR). 

   - For SDR: Write MCTRL with REQUEST of 2 (EmitStop to STOP). Then wait for MCTRLDONE status to be asserted for its completion. 

   - For HDR: Write MCTRL with REQUEST of 6 – ForceExit to end HDR mode. Then wait for MCTRLDONE status to be asserted for its completion. 

      - ~~<mark>NOTE</mark>~~ 

ODSTOP needs to be zero when sending HDR exit pattern. 

- Write MCTRL with REQUEST of 1 (EmitStartAddr to start another message). 

~~<mark>NOTE</mark>~~ IBI is not possible in this case. 

#### 70.3.2.3 Sending a CCC to one or all I3C slaves 

The normal Common Command Code (CCC) method is to use an I3C Write with an address of 0x7E. The first byte is the CCC. 

- If Broadcast, then any remaining bytes go with the Common Command Code (CCC). This ends with a STOP or a repeated START and 0x7E. 

- If Direct, after a write with an address of 0x7E, either only a CCC follows or a CCC and a Defining byte follows, if required by the CCC. 

This is followed by a repeated START and the address of the I3C Slave (for SETDASA, this is its I2C Static address). This may be repeated with more repeated START and addresses until done. Then, it may end in STOP or a repeated START and 0x7E. After the repeated start and target address, the values are read or write depending on the CCC. 

- [DIP_I3C_00052] I3C provided interrupts for Unhandled, Handled CCC when received by the slave and its state is reflected in the SSTATUS register.[end] 

The I3C spec requires I3C Controllers to emit a single START, 7E/W with both SCL High and SCL Low half periods being full Open-drain timing (for example, 200 ns). This allows I3C Targets which are acting as I2C legacy devices to turn off their I2C 50 ns spike filters, if they have one. 

After that, addresses following START may be sent with Open-Drain Low (for example, 200 ns) but High of Push-Pull timing (for example, 40 ns). This is just a note to the Application SW developer to have the I3C Controller emit this START,7E/W with MCONFIG[ODHPP] = 0. ODHPP is “Open Drain High period at Push-Pull speeds”; ODHPP=1 is used normally. 

~~<mark>NOTE</mark>~~ 

Note that MCONFIG[ODHPP] is ignored when sending a message to an i2c legacy device on an I3C bus. 

~~<mark>NOTE</mark>~~ 

Each repeated START is just a new EmitStart request. This can be chained by interrupt or pushed by message model using DMA. 

#### 70.3.2.4 [DIP_I3C_00029]In-Band Interrupt (IBI) handling [end] 

An IBI occurs when a slave sends its address after a START, and the slave's address is numerically lower than the address that the master sent (and any other slaves trying to send their addresses). When the master sends a 0x7E, the master will always lose, which is the intention. 

The IBI can happen unexpectedly when any new START (vs. repeated START) is emitted, but the IBI can also be in response to a slave pulling SDA low, which can happen in one of two ways: 

- The slave has set the request to AutoIBI mode, and so it happens automatically (the engine emits 0x7E to allow the slave to win). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2539 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

- The application gets the SLVSTART (slave START request) interrupt and so emits 0x7E. 

In either of these cases, the application can decide: 

- To always accept (ACK) the IBI 

- To always reject (NACK) the IBI 

- Allow the decision to be made by the application on a case-by-case. 

The IBI is configured by the MCTRL[IBIRESP] field, which can be set to ACK, NACK, or manual. 

- If the manual is selected, then the application rewrites it when stopped, pending on an IBI. The application can ACK or NACK based on the IBI address (which is in the MSTATUS register). Note that manual mode chooses if there is an IBI byte or not when doing ACK. 

- If always ACK was selected in the MCTRL[IBIRESP] field, then the MIBIRULES register must be configured so that the engine knows if bytes will follow. 

- If IBI bytes will follow (also known as IBI Mandatory byte), then the COMPLETE bit is not set when IBIWON is set, and RXPEND will be set for 1 or more bytes in RX FIFO. When the last byte is received, then the COMPLETE status is set. The Master automatically stops IBI data after 9 total bytes (including MDB) MCTRL[RDTERM] can be used with MCTRL[REQ] = 0 to end sooner. [DIP_I3C_00017] I3C will support Address ACK to Mandatory Byte transition during IBI from Open_Drain (Master ACKs the Slave Address) to Push Pull (Slave sends SDR data). [end] 

- [DIP_I3C_00030]I3C slave supports up to 7 bytes of Extended IBI Data following Mandatory Data byte. Extended Data to send would be present in register IBIEXT1 and IBIEXT2.[end] 

[DIP_I3C_00044]Accurate timestamping of I3C Slave data is supported in I3C though Async Mode 0. In I3C Asynchronous Timing Control, a Slave Device timestamp event occurring within that Slave, and then notifies the Master about it by generating an In-Band Interrupt (IBI).[end] 

#### 70.3.2.5 Assigning dynamic addresses to I3C devices 

If Dynamic Addresses (DAs) are all assigned below 0x40 (7-bit values from 0x3F down to 0x03, except where this is not allowed), then the MSB0 bit can be set in the Master In-Band Interrupt Registry and Rules register (MIBIRULES). This optimizes the START timing. When dynamic addresses are assigned, the MIBIRULES register must be programmed based on which I3C slave uses IBI bytes [DIP_I3C_00013](known from Bus Capabilities Register (BCR))[end]. 

Any Set Dynamic Address from Static Address (SETDASA) assignments can be done using the normal Common Command Code (CCC) model (except when using the static address for the directed part). 

There is a built-in mechanism to process the Dynamic Address Assignment (DAA) mode: 

1. Set up interrupts. Normally: 

   - [DIP_I3C_00050]MCTRLDONE: Need to know when a slave has sent its ID and BCR/DCR and a new DA is needed.[end] 

   - COMPLETE: To fire when DAA done (NACKed by all slaves). 

   - RXPEND to read the IDs of the slaves. The alternative is for DMA to read out bytes. 

   - [DIP_I3C_00050]IBIWON: The software knows if an IBI happened, which should not be possible normally.[end] 

   - MERRWARN: In case of an error 

2. Write the MCTRL register with: 

   - REQUEST set to 4 - ProcessDAA 

   - IBIRESP set to IBI response if that is possible (if not the 1st Slave assignment) 

3. Wait for the MCTRLDONE interrupt, while reading in ID using the RXPEND interrupt. If MSTATUS indicates in DAA mode (STATE=5) and BETWEEN (bit 4=1), then it is waiting for a dynamic address for the slave whose ID was read in. 

   - Write the dynamic address into MWDATAB using bits 6:0, such as 0x14 for dynamic address=7’h14. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2540 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

- Write MCTRL REQUEST to 4 (ProcessDAA again). This writes the dynamic address, and then moves to the next dynamic address. 

- If MSTATUS indicates all is done via the COMPLETE bit being set and STATE=0, then all slaves have been assigned. 

- If MSTATUS indicates NACK after having written a new dynamic address, then the dynamic address was not accepted by the slave. The 76next step is REQUEST set to EmitStop and start over. However, it is also OK to just set REQUEST to 4 (ProcessDAA again). 

#### 70.3.2.6 Using master message mode 

Master message mode is intended for use with DMA, although message mode can also be used by the processor. The message mode concept is that all writes are to the same location, including the control and then the data. The read back is from an associated location. 

~~<mark>NOTE</mark>~~ 

The data writes for message mode work in the same way as the half-word access registers MWDATAH and MRDATAH. 

To send a message via Single Data Rate (SDR) , do the following steps (from DMA or processor): 

1. Write to the MWMSG_SDR register with the control request, which includes the address, I2C vs. I3C, read or write, the count of bytes to process, and how to end (on STOP or ready for repeated START). 

2. Process the Data: 

   - [DIP_I3C_00051]If Write: Then write the rest of the data to MWMSG, using the DMA trigger (or interrupt) to keep the TX FIFO full, and stop asking when the count is down to 0. 

   - If Read: Then a DMA trigger (or interrupt) indicates when the RX FIFO is to be read out via the MRMSG_SDR.[end] 

3. In-band Interrupt (IBI) behavior is selected in the MCTRL register. 

4. Use END type STOP to exit MSG mode with the original message, with a 0 length message or by using the MCTRL register. 

To send a message via Double Data Rate (DDR) , do the following steps (from DMA or processor): 

1. Write to the MWMSG_DDR register with the control request, which includes the count of byte-pairs and how to end (on High Data Rate (HDR) Exit or ready for HDR Restart). 

2. Write the second control data to MWMSG_DDR, which includes the address, read or write, and the 7-bit command value. 

3. Process the Data: 

   - If Write: Then write the rest of the data to the same register, using the DMA trigger (or interrupt) to keep the TX FIFO full, and stop asking when the count is down to 0. 

   - If Read: Then a DMA trigger (or interrupt) indicates when the RX FIFO is to be read out. 

4. In-band Interrupt (IBI) behavior is selected in the MCTRL register. 

5. Use END type Exit to exit DDR MSG mode with the original message, with a 0 length message or by using the MCTRL register. 

70.3.2.7 [DIP_I3C_00031]Handing off mastership to another slave and getting it back [end] 

To hand off mastership, the master either: 

- Waits for a Master Request (MR) ([DIP_I3C_00050]an IBIWON interrupt with MSTATUS indicating that an MR is using the IBITYPE field[end]) 

- Pushes the request manually 

In either case, the master sends a GETACCMST request, which is a directed GET that tells the slave that the slave is being assigned mastership (if the slave wants it). If the slave accepts this request (and sends back its dynamic address in bits 7:1 and 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2541 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

the negative parity of the dynamic address in bit 0), then a STOP must be issued and the MCONFIG[MSTENA] field must be set to 2 (switching to the slave mode). 

To gain mastership, the slave sends an MR using the SCTRL register. 

- If the MSTENA field is 2, then the GETMSTACC CCC accepts. 

- If the MSTENA field is not 2, then the GETMSTACC CCC refuses. 

[DIP_I3C_00050]After mastership has granted, the MSTATUS[NOWMASTER] bit is set. The application must enable the MINTSET[NOWMASTER] bit, so the application is interrupted when a mastership transfer happens.[end] 

#### 70.3.2.8 Master engine flow diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2542-08.png)


<!-- Start of picture text -->
SCL=H<br>IDLE<br>SDA+OD (PUR=1)<br>Rd or Wr or App request SDA pulled Slave request<br>ENTDAA low for IBI/MR/HJ<br>7E or i2C SA<br>START +<br>or I3C DA<br>Header<br>(Open-drain)<br>Slave won?<br>No Yes<br>DA of slave<br>ACK from IBI, MR or<br>Slave(s) (Open-drain) HJ and RnW=1 or 0or 7'h02<br>SDR bytes ACK or NACK<br>(Open-drain)<br>(I3C or i2c) the request<br>Multi-bytes<br>IBI byte if any (Push-pull)<br>Repeated START (Push-pull) STOP<br>+ Header<br>to<br>IDLE<br><!-- End of picture text -->

Figure 368. Master engine flow diagram for SDR (HDR would just progress off SDR bytes) 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2542 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

#### 70.3.2.9 Slave data write from Master 

When the address match was valid for the Slave Dynamic address and the type was W (write from master), the slave will ACK the address, unless some condition prevents it, such as a full buffer. On ACK, the WRITE state is entered. Once ACKed, it waits for each complete data byte. This is handled in two steps: 

- 8 bits clocked in and stored in the next buffer location while in the WRITE state 

- [DIP_I3C_00018]I3C: On the 9th bit, the W9TH state is used and the parity is checked. The buffer is marked as complete with or without a parity error.[end] 

- I2C: On the 9th bit, the W9TH state is used and the data is ACKed and stored. 

When the address match was valid for 0x7E broadcast address, the Slave acknowledges it and sets the in_ccc Possible flag. On 1st data complete, it sets the in_ccc Broadcast or Direct flag (based on bit 7 of cmd). It then parses the command if recognized, setting that bit as well. The recognized ones are for Dynamic Address work and modes. The CCC and DAA blocks handle the work load after that. If not supported, then they are passed up to the system. 

#### 70.3.2.10 Slave data write to Master 

When the address match is valid for the Slave Dynamic address, and the type was R (read by master), the slave will ACK the address, unless no data waiting for the read. On ACK, the READ state is entered. 

Once ACKed, it emits the data byte at a time, with the 9th bit using R9TH state.[DIP_I3C_00019] 

- If I3C, the T bit is emitted to allow the device to indicate the last byte (from input signal from upper layers) or not the last byte. If not last byte, the Master may terminate the read via the T bit. 

- If I2C, the 9th bit allows the master to terminate via NACK, or else allows to continue via ACK. On completion of each byte read, the done signal is pulsed to get the next byte. [end] 

[DIP_I3C_00043]The application is notified if the read was terminated by the Master unexpectedly (abort in I3C, NACK before END marked).[end] 

### 70.3.3 DMA (for internal FIFO use only) 

The DMA model supports a few types of DMA uses: 

- [DIP_I3C_00053]Normal Request/ACK: The peripheral holds Request = 1 while RXFIFO has data or TXFIFO has space. 

   - DMA_TYPE = 0 is used if ACK is before the access to the WDATA/RDATA MMR. This ensures that the Request is dropped if last byte/half-word.[end] 

- Other DMA types are not supported such as Trigger-burst, 4-phase before the MMR access, and so on. 

~~<mark>NOTE</mark>~~ 

Do not enable DMA after a transaction starts. It must be enabled only while enabling the slave and interrupts, to avoid any kind of RX FIFO overrun. 

### 70.3.4 Clocks 

The Master block has 2 basic clocks feeding: 

- The System clock, which controls the access into the memory mapped registers. 

- [DIP_I3C_00002]A Functional clock (FCLK), which is used to generate the SCL clock rate on the I2C/I3C bus.[end] 

- [DIP_I3C_00046]I3C provides support for adjusting clock frequency and accuracy. They can be set through register STCCLOCK, The default values are configured through parameters.[end] 

[DIP_I3C_00039]CLK_SLOW is used to check conditions like Bus Availability, Bus free for IBI, or Hot Join. Slow clock helps to save power.[end] 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2543 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

- [DIP_I3C_00041]To determine Bus Available Condition for IBI, the Slave needs a clock to generate the ~1µ s timing. To support this, a Slow clock (CLK_SLOW) can be provided to save on power.[end] 

- [DIP_I3C_00038]Additionally, the block provide a slow clock gate (slow_gate) which is 1 if the CLK_SLOW can be turned off.[end] 

- [DIP_I3C_00040]I3C supports a counter register BAMATCH to calculate the Bus Available condition. BAMATCH provides the count of the slow clock to count out 1 us or more to allow an IBI to drive SDA low when the master is not doing so. The maximum width and maximum values are controlled by the I3C module.[end] 

The system has 3 basic choices: 

- Use the same clock as CLK, which may be variant. If variant, the slow match register can be used to change the match rule. 

- Provide a truly slow clock, which makes it inexpensive in power to count 1 µs or more. 

- Provide some other clock, but use the slow_gate signal to gate the clock near its source. 

- [DIP_I3C_00042]The I3C module supports a timeout if stalled too long in a frame. This happens when - The TX FIFO or RX FIFO is not handled and the bus is stuck in the middle of a message or No STOP was issued and between messages or IBI manual is used and no decision was made.[end] 

This model is used in conjunction with the parameters for width of counter and match rule. 

### 70.3.5 Resets 

These are the I3C resets: 

- Global reset fed into block. Everything is reset by this global reset. Release is assumed synchronized to the system clock (if provided). It is not synchronized to SCL/SDA since those should not be active when the block is released (or it would be in Hot-Join and so not active). 

- [DIP_I3C_00027] A Software Reset is provided by the I3C block.[end] 

- STOP is reset by START as well. 

- The DAA block is reset when not in DAA mode. 

- The CCC state detector is reset by STOP. This is because no clock accompanies STOP. 

- HDR modes are held in reset and clock gated by not_HDR which is set by Exit Pattern and cleared by EnterHDR. 

#### 70.3.5.1 Slave Reset and RSTACT CCC 

[DIP_I3C_00061] The Slave Reset mechanism is designed to allow an always-on tiny block to monitor SDA and SCL for a specific pattern based on HDR Exit – extended with repeated START and STOP at the end. This detector can be used to wake or reset the device or just a peripheral, as well as do nothing for any specific reset. The normal use is that the Master emits a RSTACT CCC message saying not to reset when this pattern is emitted just after; devices which are broken reset (since they miss the CCC) and devices in deepest sleep (for example, an unpowered core domain) wake (since they also miss the CCC).[end] 

The 1st default action is only to reset the peripheral. If that does not work, the next time will reset the chip/system. 

The Master may also request a specific action, which the slave can dial in if it supports that (for example, reset the peripheral only). 

The Slave Reset is connected into the system as shown in Figure 369. Note that it is outside of the I3C Peripheral, and may be in an always-on domain. Sleep/wake signals are not shown. The common connections are as follows: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2544 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

Table 408. Slave resets 

|Reset detector|Connect to IP|Connect to System|Notes|
|---|---|---|---|
|I3c_slave_active|raw_slvr_isslave if<br>master+slave|If I3C can be unused|Connect to enable if can be<br>unused — should probably<br>not clear for safety reasons.|
|iRstAction[3:0]|raw_slvr_reset|—|Result of RSTACT CCC|
|oRstRstAction|iraw_rst_slavr_reset|—|Clear RSACT state|
|oResetBlock|iraw_slvr_irq|—|Triggers IRQ in IP|
|oRstAll|—|System reset|Should perform similar to pin<br>RSTn|
|oRstCustom|—|Custom Reset if enabled|Must be setup via<br>RSTACT_CONFIG[2]|
|iDeepestSleep|—|Feed from system or 0|Only used if deepest sleep<br>supported|
|oWake|—|Wake controller|—|




![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2545-04.png)


<!-- Start of picture text -->
System PROCESSOR<br>reset<br>IRQ<br>Reset<br>SLAVE RESET<br>I3C PERIPHERAL<br>DETECTOR Control<br>SCL/SDA<br>APB<br><!-- End of picture text -->

Figure 369. Slave reset detector connected in the system (Slave Reset may be in Always-on domain) 

Figure 370 shows the connections of the Slave Reset detector, including support for deepest sleep and wake. If those are not used, they are just not connected. If the I3C peripheral may be powered off when the reset detector is powered, the isolation cells are used to protect it, although the nets are logically gated off when iDeepestSleep is 1. 

Note that the block wants the SCL and SDA signals to be fed as clocks. This is done outside the block, using any method needed. 3 domains are needed to support the reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2545 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2546-02.png)


<!-- Start of picture text -->
RSTn<br>(global<br>reset clk_ clk_ clk_<br>input) SDA SDA_n SCL<br>iDeepestSleep<br>iRstAction<br>oWake<br>(from CCC)<br>isolation oRstBlock<br>cell if needed SLAVE RESET<br>oRstAll<br>oRstRstAction DETECTOR<br>(clear it)<br>i3c_slave_active<br>(hard wire if<br>always i3c<br>and slave)<br><!-- End of picture text -->

Figure 370. Showing reset detector connections — not all used in many systems 

The i3c_slave_active signal must be used with caution, as it disables the reset detector when 0; it should be strapped 1 if always i3c and slave, else should be safely controlled (or may defeat the purpose of the Slave Reset block). If the i3c peripheral is optional, then it must be selected by some system control feature – that should be what controls i3c_slave_active. 

The block is connected to the I3C peripheral through the iRstAction and oRstRsttAction ports. These are clamped off if iDeepestSleep signal is 1; if that kind of sleep is not possible, the iDeepestSleep port should be strapped 0. The 2 nets can be treated as asynchronous even though from the same SCL. This is to avoid having to do setup/hold timing between the modules when the reset detector is in a separate domain. That is, the clk_SCL and clk_SDA_n are not intended to be treated the same clocks as used in the peripheral – this allows freedom in placement of the detector. 

Finally, the reset and wake signals are connected to the system; they are 0 when inactive, 1 when actively driven. There are clearing events used to clear: RstAll waits for the Reset input to assert (or i3c_active to go to 0); the RstBlock waits for the I3C peripheral to clear its cause register or to see a RSTACT or GETSTATUS. Wake clears on release of iDeepestSleep. 

### 70.3.6 Interrupts 

This section describes all the interrupts (IRQs) that the I3C module generates. All status interrupts are updated in the Master Status (MSTATUS) and Slave Status (SSTATUS) registers. 

Supported interrupts: 

- For pending IBI, MR, or Hot-Join that have been sent. 

- When a CCC is received and is handled by the block. (CHANDLED). 

- When an error or warning occurred, such as data underrun, data overrun, parity error, HDR-DDR CRC error, or other error or warning condition. 

- [DIP_I3C_00044]When a CCC is received which is unhandled by the I3C block. The register SCCCMASK allows the user to suppress any CCC which is intended to be unhandled.[end] 

## 70.4 External signals 

This table describes the I3C module signals. 

|Signal|I/O|Description|
|---|---|---|
|SCL|I/O|Serial clock|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2546 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

Table continued from the previous page... 

|Signal|I/O|Description|
|---|---|---|
|SDA|I/O|Serial data|
|PUR|O|Pull up resistance. There is internal pull up resistance on SDA, which<br>is contolled by the I3C master. PUR can be used to actively control<br>an external pull up resistance on SDA, if the internal pull up is not<br>enough.|



## 70.5 Initialization 

### 70.5.1 Configuration initialization 

[DIP_I3C_00004]The configuration is handled when initializing the I3C module. Configuration is done using the MCONFIG register, which controls the frequencies, duty cycle, optimizations for performance, and other parameters.[end] 

[DIP_I3C_00055]Parameters govern several features that are supported in the design. [end] 

[DIP_I3C_00058]High keeper controls are also included in the below configuration list. [end] 

Table 409. Configuration parameters used to initialize the I3C module 

|Confi|guration prameter|Description|
|---|---|---|
|MSTENA|Master Enable|Determines whether the I3C peripheral starts in Master mode (that is, the “Main Master” in<br>I3C terms) or starts in slave mode (and switches to Master later).|
|HKEEP|High Keeper|Determines how the high-keeper (weak pullup) is implemented, depending on the<br>device capabilities.|
|PPBAUD|Push-Pull BAUD|Sets the push-pull frequency as a divider from the FCLK (alternative clock fed to the<br>peripheral). This sets the SCL half-clock period baseline (used at least for the high time<br>of SCL).<br>Formula for SCL in Push-Pull mode using PPBAUD and PPLOW is:<br>SCL (Freq in MHz) = FCLK/((2 + 2*PPBAUD) + PPLOW).<br>If PPLOW is 0, then SCL high = SCL low (in ns) = (1 + PPBAUD)*1000/FCLK(MHz)<br>Examples:<br>• If FCLK = 24 MHz, then PPBAUD = 0 yields 12 MHz (42.67 ns per half period)<br>• If FCLK = 50 MHz, then PPBAUD = 1 yields 12.5 MHz (20 + 20 = 40 ns per half period)|
|PPLOW|Push-Pull Low|Changes the duty cycle for Push-Pull. It indicates how many more FCLKs to use for low.<br>Formula for SCL in Push-Pull mode using PPBAUD and PPLOW is:<br>SCL(Freq in MHz) = FCLK/((2 + 2 * PPBAUD) + PPLOW)<br>If PPLOW is non-zero, then<br>SCL High (in ns) = (1 + PPBAUD)*1000/FCLK(MHz)<br>SCL low (in ns) = (1 + PPBAUD + PPLOW)*1000/FCLK(MHz)|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2547 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

Table 409. Configuration parameters used to initialize the I3C module (continued) 

|Confi|guration prameter|Description|
|---|---|---|
|||For example, a 50 MHz FCLK, a PPBAUD of 1, and a PPLOW of 1, yields (1 + 1) * 1000/50<br>= 20 + 20 = 40 ns high and (1 + 1 + 1) * 1000/50 = 20 + 20 + 20 = 60 ns low. This would be<br>equivalent of 10 MHz SCL timing, but maintaining the 40 ns high needed, so that I2C devices<br>do not see the high periods.<br>The PPLOW value does not have any impact on open-drain and I2C mode<br>SCL rate calculations.<br>~~NOTE~~|
|ODBAUD|Open Drain BAUD|The number of PPBAUD periods to make up one I3C Open-Drain half-clock baseline.<br>ODBAUD half-clock time period = (ODBAUD + 1)* PPBAUD high period. (if ODHPP is 0)<br>Formula for SCL in Open-Drain mode is (if ODHPP=0)<br>SCL(in MHz) = FCLK/(2 + 2 * PPBAUD)*(ODBAUD + 1)<br>Target to get open-drain half clock period is 200ns.<br>For example:<br>• If PPBAUD yields 12.5 MHz (40 ns per PPBAUD period), then ODBAUD = 4 can be used<br>to get 200ns. See also ODHPP for details on short High and long Low.<br>• If PPBAUD = 1, FCLK = 50MHz, ODBAUD = 4 then open-drain SCL = 50/(2 + 2*1)*5 =<br>2.5 MHz.|
|ODHPP|Open-Drain<br>High Push-Pull|Optional field that allows for the I3C open-drain to be long Low and short High. The High<br>period of SCL is the PPBAUD period. This leaves enough time for the pull-up resistor<br>to pull the SDA high when SCL is low, but is quick when SCL is high and there are no<br>changes happening.<br>ODBAUD low half-clock time period = (ODBAUD + 1) * PPBAUD high period.<br>ODBAUD high half-clock time period = PPBAUD high period<br>Formula for SCL in Open-Drain mode is (if ODHPP = 1):<br>SCL(in MHz) = FCLK/(1 + PPBAUD)*(ODBAUD + 1) + (1 + PBAUD)<br>For example:<br>• If PPBAUD yields 12.5 MHz (40ns per PPBAUD period), then ODBAUD = 4 and ODHPP<br>= 1 will give high and low period as 40ns and 200ns respectively.<br>• If PPBAUD = 1, FCLK = 50MHz, ODBAUD = 4 then open-drain SCL = 50/(1 + 1)*5 + (1<br>+ 1) = 4.16 MHz.|
|I2CBAUD|I2C Baud|Indicates how many ODBAUD periods are needed to communicate with I2C devices<br>(MCTRL[TYPE] = 2 or MWMSG_SDR_CONTROL[I2C] = 1).<br>For example, if ODBAUD gives 200 ns, and the goal is Fm+ (Fast Mode, 1 MHz), then the<br>sum needs to be 1 µs.<br>If odd vs. even, then I2CBAUD acts differently. For example, if I2CBAUD = 3, it gives 3<br>ODBAUD periods low and 2 ODBAUD periods high.<br>• If I2CBAUD = 4, then it gives 3 ODBAUD periods for low and 3 ODBAUD periods for high.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2548 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

Table 409. Configuration parameters used to initialize the I3C module (continued) 

|Conf|iguration prameter|Description|
|---|---|---|
|||• Also, if I2CBAUD = 3, this yields 200 * 3 = 600 ns and 200 * 2 = 400 ns, with the sum 600<br>+ 400 = 1000 ns = 1µs.|
|SKEW|Skew|The normal SDA skew from SCL is handled by using the time for the SCL to reach its pad and<br>come back to the design. This is normally 2 ns to 5 ns (or sometimes more). If the SKEW is<br>too fast, then add more delay, the SKEW allows specifying the number of FCLKs to insert.|



Additional optimizations: 

- Use MIBIRULES[MSB0] to get much faster START header times. If the master application assigns all I3C Dynamic Addresses to be less than 0x40 (it does not have MSB set), then MIBIRULES[MSB0] can be set. This means that when the master emits 0x7E (broadcast) and the 1st bit is not driven low by a slave, the rest of the header can be at push-pull speeds. This is 2x faster (or more, depending on optimizations above). 

- Auto-emit 0x7E speeds up the frame when used in conjunction with MIBIRULES[MSB0], because it allows the processor to be sleeping when the frame starts automatically (in response to a slave). 

### 70.5.2 Interrupt service flow 

Set up interupts, normally: 

1. MCTRLDONE: optional 

2. COMPLETE: to fire when end of data 

3. RXPEND if read; this can be used with the MDATACTRL register to set the FIFO trigger. The alternative is for DMA to read out bytes. 

4. TXNOTFULL if write; this can be used with the MDATACTRL register to set the FIFO trigger. The alternative is for DMA to supply bytes. 

5. IBIWON: so the software knows if an IBI has occurred 

6. MERRWARN: in case of an error 

## 70.6 I3C register descriptions 

This section describes the registers in the I3C module. 

Table 410. Register Types 

|Type|||
|---|---|---|
|RO|Read-Only||
|RW|Read/Write||
|W1C|Write 1 to Clear|W1S and W1C registers are readable (they can be read).|
|W1S|Write 1 to Set||
|WO|Write-Only||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2549 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

###### ~~<mark>NOTE</mark>~~ 

[DIP_I3C_00047]Writing to a Read-Only (RO) register, except the MINTMASKED register, causes bus errors. This module does not check if programmed values in the registers are correct; the application software must ensure that valid programmed values are being written.[end] 

[DIP_I3C_00049]However, the I3C peripheral ignores writes to RO registers, and the I3C peripheral returns 0 for reads from WO or non-existent registers. It requires all 32-bit regs to be read and written as 32-bit and aligned to 32 bits. The peripheral uses the Advanced Peripheral Bus (APB), so the peripheral would not know if partial read or write operations (less than 32 bits) are used. [end] 

### 70.6.1 I3C memory map 

I3C base address: 400C_0000h 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|0h|Master Configuration (MCONFIG)|32|RW|0000_0000h|
|4h|Slave Configuration (SCONFIG)|32|RW|0017_0000h|
|8h|Slave Status (SSTATUS)|32|W1C|0000_1400h|
|Ch|Slave Control (SCTRL)|32|RW|0000_0000h|
|10h|Slave Interrupt Set (SINTSET)|32|RW|0000_0000h|
|14h|Slave Interrupt Clear (SINTCLR)|32|W1C|See<br>description|
|18h|Slave Interrupt Mask (SINTMASKED)|32|RO|0000_0000h|
|1Ch|Slave Errors and Warnings (SERRWARN)|32|W1C|0000_0000h|
|20h|Slave DMA Control (SDMACTRL)|32|RW|0000_0010h|
|2Ch|Slave Data Control (SDATACTRL)|32|RW|8000_0030h|
|30h|Slave Write Data Byte (SWDATAB)|32|WO|See<br>description|
|34h|Slave Write Data Byte End (SWDATABE)|32|WO|See<br>description|
|38h|Slave Write Data Half-word (SWDATAH)|32|WO|See<br>description|
|3Ch|Slave Write Data Half-word End (SWDATAHE)|32|WO|See<br>description|
|40h|Slave Read Data Byte (SRDATAB)|32|RO|0000_0000h|
|48h|Slave Read Data Half-word (SRDATAH)|32|RO|See<br>description|
|5Ch|Slave Capabilities 2 (SCAPABILITIES2)|32|RO|0000_0331h|
|60h|Slave Capabilities (SCAPABILITIES)|32|RO|FC3F_FE70h|
|68h|Slave Maximum Limits (SMAXLIMITS)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2550 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|6Ch|Slave ID Part Number (SIDPARTNO)|32|RW|7996_001Dh|
|70h|Slave ID Extension (SIDEXT)|32|RW|0066_0000h|
|74h|Slave Vendor ID (SVENDORID)|32|RW|0000_011Bh|
|78h|Slave Time Control Clock (STCCLOCK)|32|RW|0000_300Ah|
|7Ch|Slave Message Map Address (SMSGMAPADDR)|32|RO|0000_0000h|
|80h|Master Extended Configuration (MCONFIG_EXT)|32|RW|0000_0000h|
|84h|Master Control (MCTRL)|32|RW|0000_0000h|
|88h|Master Status (MSTATUS)|32|W1C|0000_1000h|
|8Ch|Master In-band Interrupt Registry and Rules (MIBIRULES)|32|RW|0000_0000h|
|90h|Master Interrupt Set (MINTSET)|32|RW|0000_0000h|
|94h|Master Interrupt Clear (MINTCLR)|32|W1C|See<br>description|
|98h|Master Interrupt Mask (MINTMASKED)|32|RO|0000_0000h|
|9Ch|Master Errors and Warnings (MERRWARN)|32|W1C|0000_0000h|
|A0h|Master DMA Control (MDMACTRL)|32|RW|0000_0010h|
|ACh|Master Data Control (MDATACTRL)|32|RW|8000_0030h|
|B0h|Master Write Data Byte (MWDATAB)|32|WO|See<br>description|
|B4h|Master Write Data Byte End (MWDATABE)|32|WO|See<br>description|
|B8h|Master Write Data Half-word (MWDATAH)|32|WO|See<br>description|
|BCh|Master Write Data Byte End (MWDATAHE)|32|WO|See<br>description|
|C0h|Master Read Data Byte (MRDATAB)|32|RO|0000_0000h|
|C8h|Master Read Data Half-word (MRDATAH)|32|RO|0000_0000h|
|CCh|Byte-only Write Byte Data (to bus) (MWDATAB1)|32|WO|0000_0000h|
|D0h|Master Write Message in SDR mode (MWMSG_SDR_CONTROL)|32|WO|See<br>description|
|D0h|Master Write Message Data in SDR mode (MWMSG_SDR_DATA)|32|WO|0000_0000h|
|D4h|Master Read Message in SDR mode (MRMSG_SDR)|32|RO|0000_0000h|
|D8h|Master Write Message in DDR mode (MWMSG_DDR_CONTROL)|32|WO|See<br>description|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2551 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|D8h|Master Write Message Data in DDR mode (MWMSG_DDR_DATA)|32|WO|0000_0000h|
|DCh|Master Read Message in DDR mode (MRMSG_DDR)|32|RO|0000_0000h|
|E4h|Master Dynamic Address (MDYNADDR)|32|RW|0000_0000h|
|10Ch|CCC Mask for Unhandled CCCs (SCCCMASK)|32|RW|0000_007Fh|
|110h|Slave Errors and Warnings Mask (SERRWARNMASK)|32|RW|0000_0F1Fh|
|11Ch|Map Feature Control 0 (SMAPCTRL0)|32|RO|0000_0000h|
|120h|Map Feature Control 1 (SMAPCTRL1)|32|RW|0000_0000h|
|140h|Extended IBI Data 1 (IBIEXT1)|32|RW|0000_0070h|
|144h|Extended IBI Data 2 (IBIEXT2)|32|RW|0000_0000h|



### 70.6.2 Master Configuration (MCONFIG) 

##### Offset 

|Register|Offset|
|---|---|
|MCONFIG|0h|



##### Function 

The MCONFIG register controls all Master states when Master operation is enabled. The MCONFIG register should not be changed when an active transaction is happening. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||I2CB|AUD|||SKEW||ODHP<br>P||||OD|BAUD|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R<br>W||PPL|OW|||PPBA|UD||Reserv<br>ed|ODST<br>OP|HKE|EP|DISTO|0|MSTENA|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2552 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Fields 

|Field<br>31-28<br>I2CBAUD|Function<br>I2C Baud Rate<br>The I2C low and high times in ODBAUD counts.<br>• I2CBAUD > 1 is the main count load, and it is count-1. Therefore, for I2CBAUD > 1: I2CBAUD==0 is<br>1 ODBAUD beat, and I2CBAUD==1 is 2 ODBAUD beats.<br>• If I2CBAUD[28] is 1, then low will be 1 extra ODBAUD beat. This means that the I2CBAUD<br>field is normally 3, where ODBAUD gives 200 ns. Therefore, this means that for I2CBAUD > 1<br>I2CBAUD==1, which means 2 ODBAUD. Therefore, (2 + 1) * 200 = 600 ns low, with 2 * 200 = 400<br>ns high for 1 µs period, to match Fast Mode Plus (FM+). For Fast Mode (FM), I2CBAUD is normally<br>11 (giving 2.6 µs) or is 6 (giving 2.4 µs).|
|---|---|
|27-25<br>SKEW|Skew<br>Number of FCLK counts for an SDA change after SCL for I3C push-pull. This is in addition to the<br>roundtrip of the SCL line from the pad back to the module (3 ns to 4 ns or more).<br>• SKEW is normally not needed, so assign SKEW=0.<br>• SKEW is only used if SDA is not naturally skewing from an SCL change.<br>• I2C automatically skews SDA (but not PUR) to match I2C rules.|
|24<br>ODHPP|Open Drain High Push-Pull<br>If ODHPP = 1, then the Open-Drain High SCL half-lock period should be 1 PPBAUD count for I3C<br>messages. If ODHPP = 0, the Open-Drain SCL High half-clock period will be the same as the Open-Drain<br>Low SCL half-period.<br>The use of ODHPP = 1 is both because it is faster (and works for I3C devices) and because any legacy I2C<br>devices on the bus will not see the SCL High at all (less than the spike filter period).<br>SeeSending a CCC to one or all I3C slavesfor open-drain timing check on first broadcast 0x7E, allowing<br>I3C peripherals acting as I2C legacy devices to turn off their I2C 50 ns Spike filters.|
|23-16<br>ODBAUD|Open Drain Baud Rate<br>ODBAUD= (number of PPBAUD counts) - 1. ODBAUD should not be 0 (not the same as push-pull). This<br>would normally go for 200 ns (see I2CBAUD for I2C counts). When used with ODHPP, this gives 250 ns<br>per clock in I3C. Therefore, if PPBAUD gives 12 MHz, then 1 PPBAUD is ½ of 12 MHz or 41.67 ns, and<br>then to get around 200 ns, use 5-1=4 for ODBAUD.|
|15-12<br>PPLOW|Push-Pull Low<br>Adder for push-pull low, to create a duty-cycle with a longer low period, with up to 15 more FCLKs low<br>than high. PPLOW=0 means a 50:50 duty cycle.|
|11-8|Push-Pull Baud Rate|
|PPBAUD|The FCLK Counter for each push-pull low and normally high period. So, PPBAUD=0 if run at ½ input<br>FCLK speed (for example, a 24 MHz FCLK yields a 12 MHz SCL, because each FCLK is SCL Low or<br>SCL High). Note the use of duty-cycle via Push-Pull Low (PPLOW). For example, 24 MHz with 50:50<br>duty cycle is 12 MHz, but with PPLOW adding 3 more low beats, the push-pull baud rate becomes 4.8<br>MHz (from 24 MHz/5 beats).|
|7|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2553 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—<br>6<br>ODSTOP|Open Drain Stop<br>If ODSTOP=1, then STOP will be emitted at open-drain speeds even for I3C messages. This can be<br>useful for legacy devices, to ensure that the legacy devices see the STOP. ODSTOP needs to be zero<br>when sending HDR exit pattern.|
|5-4<br>HKEEP|High-Keeper<br>Indicates how High-Keeper is to be supported.<br>Your specific device may not support any or all of these High-Keeper methods. See the<br>chip-specific section for this module, at the beginning of this chapter.<br>~~NOTE~~<br>00b - NONE. Use PUR (Pull-Up Resistor). Hold SCL High.<br>01b - WIRED_IN. High Keeper controls, use pin_HK (High Keeper) controls. SCL may use a HK<br>or that signal (pin_HK_SCL) may only OR into SCL_oena.<br>10b - PASSIVE_SDA. Passive on SDA, can Hi-Z (high impedance) for Bus Free (IDLE) and hold.<br>11b - PASSIVE_ON_SDA_SCL. Passive on SDA and SCL, can Hi-Z (high impedance) both for<br>Bus Free (IDLE), and can Hi-Z SDA for hold.|
|3<br>DISTO|Disable Timeout<br>This timeout detects application errors.<br>• If DISTO=1, then it disables the timeout (if the timeout is configured).<br>• If the master has been left in a state other than Stopped for more than 100 us (because 10 kHz is<br>the slowest allowed I3C speed), then the timeout will send an MERRWARN (interrupt).<br>• To prevent the MERRWARN interrupt when doing development or testing, write 1 to DISTO to<br>disable the timeout.<br>• In systems that support timeouts, timeout will be disabled automatically during debug.|
|2<br>—|Reserved|
|1-0<br>MSTENA|Master Enable<br>Indicates if the master is enabled and what states are allowed for it (the master).<br>00b - MASTER_OFF. Master is off (disabled). If MASTER_OFF is enabled, then the I3C module<br>can only use slave mode.<br>01b - MASTER_ON. Master is on (is enabled). When used from start-up, this I3C module is<br>master by default (the main master). The module controls the bus unless the master is handed<br>off. If the master is handed off, then MSTENA must move to 2 after that happens. The handoff<br>means emitting GETACCMST and if accepted, the module emits a STOP and set the MSTENA<br>bit to 2 (or 0).|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2554 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||10b - MASTER_CAPABLE. The I3C module is master-capable, however the module is operating<br>as a slave now. When used from the start, the I3C module starts as a slave, but will be prepared<br>to switch to master mode. To switch to master mode, the slave emits a Master Request (MR), or<br>gets a GETACCMST CCC command and accepts it (to switch on the STOP).|
||11b - Reserved|



### 70.6.3 Slave Configuration (SCONFIG) 

Offset 

|Register|Offset|
|---|---|
|SCONFIG|4h|



##### Function 

Contains fields that must be configured before the module is activated. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2555-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0<br>SADDR  BAMATCH<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 1 0 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 OFFLI 0 0 0 HDRO S0IGN MATC SLVE<br>NACK<br>W NE  K  ORE  HSS  NA<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-25|Static Address|
|SADDR|SADDR sets the I2C 7-bit static address, else must be 0.|
|24<br>—|Reserved|
|23-22<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2555 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Table continued from the previous page... 

|Field<br>21-16|Function<br>Bus Available Match|
|---|---|
|BAMATCH|This is the Bus Available condition match value for the current slow clock. BAMATCH provides the count<br>of the slow clock to count out 1 µs (or more) to allow an In-Band Interrupt (IBI) to drive SDA low when the<br>master is not doing so. The maximum width and maximum values are controlled by the I3C module.|
|15-12<br>—|Reserved|
|11-10<br>—|Reserved|
|9<br>OFFLINE|Offline<br>If OFFLINE = 1 when the slave enable (SCONFIG[SLVENA]) is set to 1, then the I3C module waits for<br>either 60 µs of bus quiet or a High Data Rate (HDR) Exit Pattern. This ensures that the bus is not in HDR<br>mode, and so can safely track Single Data Rate (SDR) mode.|
|8<br>—<br>7<br>—|Reserved<br>Reserved|
|6-5<br>—|Reserved|
|4<br>HDROK|HDR OK<br>Deprecated: If HDROK = 1, allowHDR-DDRand/orHDR-BTmessaging if available by setting the<br>corresponding SIDEXT[BCR] bit to say HDR is available, and the corresponding GETCAPS bit for DDR<br>and/or BT bit permitting use.<br>Use the SIDEXT[BCR] field instead.<br>~~NOTE~~|
|3<br>S0IGNORE|S0/S1 Errors Ignore<br>If S0IGNORE = 1, the Slave will not detect S0 or S1 errors and so does not lock up waiting on an Exit Pattern.<br>This should only be used when the bus will not use HDR mode.|
|2<br>MATCHSS|Match START or STOP<br>If MATCHSS = 1, then the START and STOP sticky SSTATUS bits will only be set if<br>SSTATUS[MATCHED] is set. This allows START and STOP to be used to detect the end of a message<br>to/from this slave.|
|1<br>NACK|Not Acknowledge|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2556 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||If NACK = 1, then the slave will NACK all requests to it, except a Common Command Code (CCC)<br>broadcast. NACK = 1 should be used with caution, because the master may decide that the slave is<br>missing, if NACK is overused.|
|0|Slave Enable|
|SLVENA|• If SLVENA = 1, then a slave can operate on the I2C or I3C bus.<br>• If SLVENA = 0, then a slave will ignore the I2C or I3C bus.<br>SLVENA must not be set before registers like SCONFIG (SIDPARTNO, SIDEXT, and others) are set,<br>because these registers affect the data to/from the master. Slave enable is configured just one time before<br>the I3C bus comes up. If slave enable is used at other times, see Hot-Join. In the case of Hot-Join, the<br>Hot-Join bit (SCAPABILITIES[IBI_MR_HJ]) must be set before setting the slave enable bit (SLVENA), so<br>that the device does not see a START or STOP incorrectly.<br>Default: 0 unless configured to be 1 by default.|



### 70.6.4 Slave Status (SSTATUS) 

##### Offset 

|Register|Offset|
|---|---|
|SSTATUS|8h|



##### Function 

Not all bits are used if the module only acts as a slave. The Slave Status register is used to indicate both sticky status for interrupts, as well as “states” and “modes” related to the I3C bus. The fields are divided into current activity, interrupt maskable actions, then states and modes on the bus. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2557-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>EVEN CHAN HDRM<br>R TIMECTRL  ACTSTATE  HJDIS  0 MRDIS  IBIDIS  0 EVDET  0<br>T  DLED  ATCH<br>W W1C W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>ERRW DACH TXNO RX_ MATC STAR STHD STDA STRE STRE STCC STMS STNO<br>R CCC  STOP  0<br>ARN  G  TFU... PEND  HED  T  R  A  QWR  QRD  CH  G  TST...<br>W W1C W1C W1C W1C W1C<br>Reset 0 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2557 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Fields 

|Field|Function|
|---|---|
|31-30<br>TIMECTRL|Time Control<br>Indicates if time control is currently enabled.<br>00b - NO_TIME_CONTROL. No time control is enabled<br>01b - Reserved<br>10b - ASYNC_MODE. Asynchronous standard mode (0 or 1) is enabled<br>11b - Reserved|
|29-28<br>ACTSTATE|Activity State from Common Command Codes (CCC)<br>00b - NO_LATENCY. Normal bus operations<br>01b - LATENCY_1MS. 1 ms of latency<br>10b - LATENCY_100MS. 100 ms of latency<br>11b - LATENCY_10S. 10 seconds of latency|
|27<br>HJDIS|Hot-Join Is Disabled<br>HJDIS = 1 if Hot-Join is disabled at this time. While Hot-Join is disabled, CTRL requests will be held off<br>(not responded to).|
|26<br>—|Reserved|
|25<br>MRDIS|Master Requests Are Disabled<br>MRDIS = 1 if Master Requests are disabled at this time. While Master Requests are disabled, CTRL<br>requests will be held off (not responded to).|
|24<br>IBIDIS|In-Band Interrupts Are Disabled<br>IBIDIS = 1 if In-Band Interrupts are disabled at this time. While In-Band Interrupts are disabled, CTRL<br>requests will be held off (not responded to).|
|23-22<br>—|Reserved|
|21-20<br>EVDET|Event Details<br>Current details of the last (EVENT = 1) or pending event.<br>00b - NONE. no event or no pending event<br>01b - NO_REQUEST. Request is not sent yet. Either there was no START yet, or is waiting for<br>Bus-Available or Bus-Idle (HJ).<br>10b - NACKED. Not acknowledged (Request sent and NACKED), the module will try again.<br>11b - ACKED. Acknowledged (Request sent and ACKED), so Done (unless the time control data<br>is still being sent).|
|19|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2558 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|18<br>EVENT|Event<br>For a Slave, a pending In-Band Interrupt (IBI), Master Request (MR), or Hot-Join (HJ) has been sent as<br>requested. See the upper status register fields for details.<br>For a Slave, a pending In-Band Interrupt (IBI), Master Request (MR), or Hot-Join (HJ) has<br>been sent as requested. See the upper status register fields for details.<br>~~NOTE~~|
|17<br>CHANDLED|Common Command Code Handled<br>A CCC is being handled by the module. This is a notification only, but the result may be an updated<br>SSTATUS register.|
|16|High Data Rate Command Match|
|HDRMATCH|An HDR command matched this device’s I3C Dynamic Address. The HDR command will be available as<br>the 1st byte and RXPEND will be set (whether the command is read or write, the MSb of that command<br>byte indicates if it is a read or a write command). If the HDR command is a read, and there are to-bus<br>bytes waiting, then the command will be ACKED and the data sent back; otherwise the HDR command<br>will be NACKED. Note that when HDRMATCHED is set, the ERRWARN bit should be checked, because<br>the HPAR error may have be encountered after signaling this HDR command (the parity is after the<br>destination address and command).|
|15<br>ERRWARN|Error Warning<br>An error or warning has occurred, such as data underrun, data overrun, parity error, HDR-DDR CRC<br>error, or other error or warning condition. See theSlave Errors and Warnings (SERRWARN).|
|14<br>CCC|Common Command Code<br>A CCC has been received, and is not handled by the I3C module. There are 2 types of Common<br>Command Codes:<br>• Broadcasted CCC, which will then also correspond with RXPEND and the 1st byte is the CCC<br>(command).<br>• Direct CCC, which may never be directed to this device. If Direct CCC are directed to this device,<br>then the TXSEND or RXPEND are triggered, and the RXPEND contains the command.|
|13<br>DACHG|Dynamic Address Change<br>The Slave Dynamic Address (DA) has been assigned, re-assigned, or reset (lost) and is now in that state<br>of being valid or none. Actual DA can be seen in the DYNADDR register.<br>Note that DACHG will also be used when MAP Auto feature is configured. This will be changing one or more<br>MAP items. See DYNADDR and/or MAPCTRLn. DYNAADDR for the main DA (0) indicates if last change<br>was due to Auto-MAP.|
|12|Transmit Buffer Is Not Full|
|TXNOTFULL|Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2559 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

Table continued from the previous page... 

|Field|Function<br>TXNOTFULL = 1 when the To-bus buffer/FIFO can accept more data to go out. For all but External<br>FIFO, this uses SDATACTRL[TXTRIG], which defaults to not-full. If DMA is enabled for transmitting, then<br>it will also be signaled to provide more data.|
|---|---|
|11|Received Message Pending|
|RX_PEND|Receiving a message from master, which is not being handled by the I3C module (not a Common<br>Command Code (CCC), so is internally processed by the module). For all but External FIFO, this uses<br>SDATACTRL[RXTRIG], which defaults to not-empty. If DMA is enabled for receiving, then DMA is<br>signaled as well. RX_PEND self-clears if data is read (from FIFO and non-FIFO sources).|
|10<br>STOP|Stop<br>The STOP bit is from a stopped state being detected, meaning that a STOP state was present on the bus<br>since the bus was last cleared. The STNOTSTOP state will also indicate if the I3C module is in stop mode.<br>A fast STOP/START combination may not trigger the STOP status. In that case, START is always set.|
|9|Matched|
|MATCHED|An incoming header matched this device’s I3C Dynamic or I2C Static address (if any) since the bus was<br>last cleared.|
|8<br>START|Start<br>START = 1 if a START or repeated START was seen after the START bit was last cleared. This is not<br>usually needed, but can be used for wake events.|
|7|Reserved|
|—<br>6<br>STHDR|Status High Data Rate<br>STHDR = 1 if the I3C bus is in HDR-DDR mode, regardless of whether HDR mode is supported by this<br>module or not, and regardless of whether the message is to this module or to some other module.|
|5|Status Dynamic Address Assignment|
|STDAA|STDAA = 1 if the I3C bus is in Enter Dynamic Address Assignment (ENTDAA) mode, regardless of<br>whether this bus slave has or does not have a Dynamic Address.|
|4|Status Request Write|
|STREQWR|STREQWR = 1 if the request (REQ) in process is SDR write data from the master to this bus slave (or<br>all I3C slaves), but not in ENTDAA mode. See Status High Data Rate (STHDR) for Double Data Rate<br>(DDR) handling.|
|3|Status Request Read|
|STREQRD|STREQRD = 1<br>• If the REQ in process is an SDR read from this slave<br>• If an In-Band Interrupt (IBI) is being pushed out|
||Also see Status High Data Rate (STHDR) for Double Data Rate (DDR) handling.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2560 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|2|Status Common Command Code Handler|
|STCCCH|STCCCH = 1 if a Common Command Code (CCC) message is being handled automatically.|
|1|Status message|
|STMSG|STMSG = 1 if this bus slave is listening to the bus traffic or responding. If STNOSTOP = 1, then STMSG<br>is 0 when a non-matching address is seen, until the next repeated START or STOP occurs.|
|0|Status Not Stop|
|STNOTSTOP|• When the bus is busy (has activity), STNOTSTOP = 1.<br>• When the I3C module is in a STOP condition, STNOTSTOP = 0.<br>Other SSTATUS bits may also be set when busy. Note that STNOTSTOP can also be true (= 1) after an<br>S0 or S1 error, where the I3C module is waiting for an Exit Pattern.|



### 70.6.5 Slave Control (SCTRL) 

##### Offset 

|Register|Offset|
|---|---|
|SCTRL|Ch|



##### Function 

Contains controls for the active use of the I3C bus, like event generation (for example, interrupts to the master). The Slave Control register is used to activate various special operations for the Slave, but only if the module is configured to support those operations. This includes events such as IBI and GETSTATUS fields (except the Protocol error, which is automatically set). 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2561-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>VENDINFO  ACTSTATE  PENDINT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 MAPID EXTD 0<br>IBIDATA  EVENT<br>X  ATA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2561 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Fields 

|Field|Function|
|---|---|
|31-24|Vendor Information|
|VENDINFO|Should be set to the Vendor Reserved field that the GETSTATUS CCC returns. The vendor information<br>should be maintained by the application, because the master reads this field. If VENDINFO is not<br>configured, then the GETSTATUS field always returns 0.|
|23-22<br>—|Reserved|
|21-20<br>ACTSTATE|Activity State (of slave)<br>Should be set to the slave’s activity state that the GETSTATUS CCC returns as activity mode. The<br>activity state should be maintained by the application, because the master will read this field. If the<br>activity state is not configured, then the GETSTATUS command will always return 0.|
|19-16<br>PENDINT|Pending Interrupt<br>Should be set to the pending interrupt that the GETSTATUS CCC returns. The pending interrupt should be<br>maintained by the application, because the master reads this field.<br>If PENDINT=0 and<br>• If an IBI interrupt is pending, then the GETSTATUS command returns 1.<br>• If an IBI interrupt is not pending, then the GETSTATUS field returns 0.|
|15-8<br>IBIDATA|In-Band Interrupt Data<br>Data byte to go with an In-Band Interrupt (IBI), if the module is enabled for IBI. If SCTRL[IBIDATA] is<br>enabled, then IBI is required.|
|7-5<br>—|Reserved|
|4<br>MAPIDX|Map Index<br>Index of Dynamic Address that IBI is for. This is 0 for the main or base Dynamic Address, or can be any valid<br>index. See DYNADDR register for more details. Used only if Mapping is enabled.|
|3|Extended Data|
|EXTDATA|If 1, then after IBIDATA is emitted, extended data will be taken from IBIEXT1 and IBIEXT2 if<br>configured，see the IBIEXT1[MAX] field. This may be used with time control, in which case the data<br>follows the time information.|
|2|Reserved|
|—<br>1-0|Event|
|EVENT|• If EVENT is set to non 0, it will request an event.|
||• After being requested, SSTATUS[EVENT] and SSTATUS[EVDET] show the status as it progresses.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2562 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||• After completion, the EVENT field automatically returns to 0.<br>• After EVENT is non 0, only 0 can be written to EVENT (to cancel), until the event processing is done<br>(finished).<br>00b - NORMAL_MODE. If EVENT is set to 0 after was a non 0 value, event processing will cancel<br>if the event processing has not yet started. If event processing has already been started, then<br>event processing will not be canceled.<br>01b - IBI. Start an In-Band Interrupt. This will try to push an IBI interrupt onto the I3C bus. If<br>data is associated with the IBI, then the data will be read from the SCTRL[IBIDATA] field. If<br>time control is enabled, then this data also includes any time control-related bytes. Additionally,<br>the IBIDATA byte will have bit 7 set to 1 automatically (as is required for time control). The IBI<br>interrupt will occur after the 1st (mandatory) IBIDATA, if any.<br>10b - MASTER_REQUEST. Start a Master-Request.<br>11b - HOT_JOIN_REQUEST. Start a Hot-Join request. A Hot-Join Request is used when the<br>device is powered on after the I3C bus is already powered up or when the device is connected<br>using hot insertion methods (the device is powered up when it is physically inserted in the<br>powered-up I3C bus). The HJ waits for Bus Idle, and SCTRL[EVENT] = HOT_JOIN_REQUEST<br>must be set before the slave enable (SCONFIG[SLVENA]).|



### 70.6.6 Slave Interrupt Set (SINTSET) 

##### Offset 

|Register|Offset|
|---|---|
|SINTSET|10h|



##### Function 

Sets interrupt enables for select Slave Status (SSTATUS) bits. Reading this register (SINTSET) returns the status of the interrupt enables. 

- To activate an interrupt enable, write 1 to its field in this register (SINTSET). 

- To disable an interrupt enable, write 1 to the appropriate bit in the Interrupt Clear Register (SINTCLR). Writing 0 to the interrupt enable in this register (SINTSET) does not disable the interrupt. 

The Interrupt registers allow masking interrupt sources, as well as checking which interrupts have activated. The normal method is to enable an interrupt, and then once the interrupt fires, the interrupt is either cleared by writing the SSTATUS register or cleared by action on the corresponding data register. The Interrupt is level held, meaning the interrupt stays set until the cause is cleared by some method. The module prevents races, so that if a new event comes in, that new event will not be lost. 

- SINTSET sets interrupt enables for Slave Status (SSTATUS) bits. Reading the SINTSET register returns the status of the interrupt enables. 

- SINTCLR clears interrupt enables for SSTATUS bits. 

- SINTMASKED returns the value of the SSTATUS bits ANDed with their interrupt enables. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2563 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||0|||||||0|EVEN|CHAN|DDRM|
|W||||||||||||||T|DLED|ATC...|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|ERRW|CCC|DACH|TXSE|RXPE|STOP|MATC|STAR|||||0||||
|W|ARN||G|ND|ND||HED|T|||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-20<br>—|Reserved|
|19<br>—|Reserved|
|18<br>EVENT|Event Interrupt Enable<br>Slave: Interrupt when Pending IBI, MR, or Hot-Join has been sent as requested. See<br>SSTATUS[EVDET]. Used only if configured to support events.|
|17<br>CHANDLED|Common Command Code (CCC) (that was handled by I3C module) Interrupt Enable<br>Interrupt when a CCC was received and handled by the block (is done). SSTATUS shows new results.<br>CHANDLED can be used to track when Activity states and masks on events (for example, IBIs) occur.<br>Used for CCCs that are enabled.|
|16|Double Data Rate Interrupt Enable|
|DDRMATCHED|Interrupt when DDR matched for Read or Write command. Used only if HDR enabled.|
|15|Error/Warning Interrupt Enable|
|ERRWARN|Interrupt when an error or warning has occurred, such as data underrun, data overrun, parity error,<br>HDR-DDR CRC error, or other error or warning condition. See the ERRWARN register for details of the<br>cause. Only available for errors that are configured features.|
|14<br>CCC|Common Command Code (CCC) (that was not handled by I3C module) Interrupt Enable<br>For CCCs not handled by the block, RXPEND will also interrupt and the SSTATUS REQ field will<br>indicate it is a CCC.|
|13<br>DACHG|Dynamic Address Change Interrupt Enable<br>Interrupt on Dynamic address defined (SETDASA or ENTDAA) or lost (RSTDAA). See also DADDR<br>register.|
|12|Transmit Interrupt Enable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2564 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|TXSEND|Interrupt when Request data by Master (Read). This interrupts on 1st request (header) as well as when<br>ready for more; the Application indicates if more or END. If FIFO, triggers on Tx emptiness trigger. If<br>DMA, then message end (DMA end or terminate).|
|11|Receive Interrupt Enable|
|RXPEND|Interrupt when Receiving a message from Master, which is not being handled by block (excludes CCCs<br>being handled automatically). If FIFO, then Rx fullness trigger. If DMA, then message end. See also<br>REQ in SSTATUS for context.|
|10<br>STOP|Stop Interrupt Enable<br>Interrupt on STOP state on the bus. See START as the preferred interrupt when needed. This interrupt<br>may not trigger for quick STOP/START combination, as it relates to the state of being stopped.|
|9|Match interrupt enable|
|MATCHED|Interrupt on Matching header for I3C Dynamic Address. Also for matching header for I2C Static Address,<br>if configured and if no Dynamic Address set (see DYNADDR register).|
|8|Start Interrupt Enable|
|START|Interrupt on START and repeated START when needed (such as wakeup). See also STOP.|
|7-0<br>—|Reserved|



### 70.6.7 Slave Interrupt Clear (SINTCLR) 

##### Offset 

|Register|Offset|
|---|---|
|SINTCLR|14h|



##### Function 

Clear interrupt enables for select Slave Status (SSTATUS) bits. To clear an interrupt enable, write 1 to the corresponding bit in this register (SINTCLR). However, writing 0 has no effect. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2565 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||0|||||||0|EVEN<br>T|CHAN<br>DLED|DDRM<br>ATC...|
|W||||||||||||||W1C|W1C|W1C|
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|ERRW<br>ARN|CCC|DACH<br>G|TXSE<br>ND|RXPE<br>ND|STOP|MATC<br>HED|STAR<br>T|||||0||||
|W|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|||||||||
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|



##### Fields 

|Field|Function|
|---|---|
|31-20<br>—|Reserved|
|19<br>—|Reserved|
|18<br>EVENT|EVENT Interrupt Enable Clear|
|17<br>CHANDLED|CHANDLED Interrupt Enable Clear|
|16|DDRMATCHED Interrupt Enable Clear|
|DDRMATCHED||
|15<br>ERRWARN|ERRWARN Interrupt Enable Clear|
|14<br>CCC|CCC Interrupt Enable Clear|
|13<br>DACHG|DACHG Interrupt Enable Clear|
|12<br>TXSEND|TXSEND Interrupt Enable Clear|
|11|RXPEND Interrupt Enable Clear|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2566 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|RXPEND||
|10|STOP Interrupt Enable Clear|
|STOP||
|9|MATCHED Interrupt Enable Clear|
|MATCHED||
|8|START Interrupt Enable Clear|
|START||
|7-0<br>—|Reserved|



### 70.6.8 Slave Interrupt Mask (SINTMASKED) 

##### Offset 

|Register|Offset|
|---|---|
|SINTMASKED|18h|



##### Function 

Returns the status of enabled interrupts (the value of Slave Status (SSTATUS) ANDed with the value of Slave Interrupt Set (SINTSET)). 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||0|||||||EVEN<br>T|CHAN<br>DLED|DDRM<br>ATC...|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|ERRW<br>ARN|CCC|DACH<br>G|TXSE<br>ND|RXPE<br>ND|STOP|MATC<br>HED|STAR<br>T|||||0||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2567 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Fields 

|Field|Function|
|---|---|
|31-19<br>—|Reserved|
|18<br>EVENT|EVENT Interrupt Mask|
|17<br>CHANDLED|CHANDLED Interrupt Mask|
|16|DDRMATCHED Interrupt Mask|
|DDRMATCHED||
|15<br>ERRWARN|ERRWARN Interrupt Mask|
|14<br>CCC|CCC Interrupt Mask|
|13<br>DACHG|DACHG Interrupt Mask|
|12<br>TXSEND|TXSEND Interrupt Mask|
|11<br>RXPEND|RXPEND Interrupt Mask|
|10<br>STOP|STOP Interrupt Mask|
|9<br>MATCHED|MATCHED Interrupt Mask|
|8<br>START|START interrupt mask|
|7-0<br>—|Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2568 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

### 70.6.9 Slave Errors and Warnings (SERRWARN) 

##### Offset 

|Register|Offset|
|---|---|
|SERRWARN|1Ch|



##### Function 

Contains errors and warnings from I3C/I2C protocol, which includes internal issues such as overrun and underrun, detected errors and conditions like parity errors, CRC errors, and read terminations by the Master. Related to SSTATUS[ERRWARN] bit and SINTSET[ERRWARN] interrupt. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2569-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>OWRI OREA<br>R 0 0 0<br>TE  D<br>W W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>INVST URUN<br>R 0 0 0 S0S1  HCRC  HPAR  SPAR  0 TERM  URUN  ORUN<br>ART  NACK<br>W W1C W1C W1C W1C W1C W1C W1C W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-22|Reserved|
|—||
|21|Reserved|
|—||
|20-18|Reserved|
|—||
|17|Over-write Error|
|OWRITE|The SWDATAB/BE register was written when FULL.|
|16|Over-read Error|
|OREAD|The SRDATAB register was read for more bytes than were available by the application. Likewise the<br>SRDATAH if enabled.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2569 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|15-14<br>—|Reserved|
|13<br>—|Reserved|
|12<br>—|Reserved|
|11<br>S0S1|S0 or S1 Error<br>A S0 or S1 error has occurred and the slave is locked and waiting for an HDR Exit Pattern. Writing<br>1 to S0S1 causes the module to release the lock, but that should be used with great care. S0S1<br>clears automatically when an Exit Pattern is detected. Therefore, writing 1 to S0S1 must be used under<br>controlled circumstances to avoid problems. Before starting to operate normally, the module then waits<br>for a START (or repeated START) or STOP.|
|10<br>HCRC|HDR-DDR CRC Error<br>HDR-DDR Cyclic Redundancy Check (CRC) error on a message from the master. This calls into<br>question the data from the whole DDR command frame.<br>This includes an HDR Restart or Exit being issued before an HDR-DDR message from master has finished.|
|9|HDR Parity Error|
|HPAR|HDR Parity error or framing error on a message from the master. Note that the corresponding command<br>or data that had the error will normally be in the Rx buffer (which can be read using the Slave Read Data<br>Byte Register (SRDATAB)).|
|8<br>SPAR|SDR Parity Error<br>SDR Parity error on a message from the master. This also sets the GETSTATUS Protocol Error sticky bit<br>(which is cleared after a GETSTATUS read).<br>For Read, this will be set if a Read Abort (timeout) occurs due to Master not driving clock for >100 µs during<br>an I3C SDR Read.|
|7-5<br>—|Reserved|
|4|Invalid Start Error|
|INVSTART|Invalid start with SCL falling while SDA = 1 is in a STOP condition.|
|3|Terminated Error|
|TERM|The master terminated a read from a slave when an END was not set (on the same or previous read).|
|2|Underrun and Not Acknowledged (NACKED) Error|
|URUNNACK|The internal to-bus buffer/FIFO was underrun in the read header and so the module NACKED the header.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2570 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|1|Underrun Error|
|URUN|The internal to-bus buffer/FIFO was underrun during data read (the application did not provide the data fast<br>enough). The END bit or register should be used if that was the last one.|
|0|Overrun Error|
|ORUN|The internal from-bus buffer/FIFO was overrun (too many characters are coming in and cannot be<br>processed by the the user application fast enough).|
||Cutoff the RX_FIFO too close to the boundary when DUT is slave for SDR write/HDR-DDR write can cause<br>an ORUN error to get set when FIFO is full.|



### 70.6.10 Slave DMA Control (SDMACTRL) 

##### Offset 

|Register|Offset|
|---|---|
|SDMACTRL|20h|



##### Function 

[DIP_I3C_00056]The DMA Control register allows for DMA to be used for inbound messages and outbound messages. The DMA Control register is limited in value for Slave use because the Slave has to be reactive. [end]Two common use models: 

- From-bus collection to avoid being overrun: The SCONFIG[MATCHSS] bit is set, and then the processor enables the interrupts for START, and STOP, as well as enabling the DMA to collect the data. The START or STOP interrupt only occurs after a message is directed to the Slave (MATCHED bit set), and the DMA copied data can then be examined. 

~~<mark>NOTE</mark>~~ 

Do not enable DMA after a transaction starts. DMA must be enabled only while enabling the slave and interrupts, to avoid any kind of RX FIFO overrun. 

- To-bus for larger reads: Because I3C and I2C reads are preceded by a write that indicates what will be read (or in response to an IBI from the Slave), the DMA can be used to push through the data. 

   - For I3C, the last value needs to be handled by the processor, unless the DMA moves wider words and is able to set the END bit (that is, 16-bit values when in byte mode or 32-bit values when in half-word mode). 

   - For I2C, the last value is determined by the Master, so the DMA may end early or may run out when the Master still wants more. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2571 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0||||||||
|W||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R<br>W|||||0||||0||DMAW|IDTH|DMA|TB|DMAFB|
|Reset|0|0|0|0|0|0|0|0|0|0|0|1|0|0|0<br>0|



##### Fields 

|Field|Function|
|---|---|
|31-8|Reserved|
|—<br>7-6|Reserved|
|—<br>5-4|Width of DMA Operations|
|DMAWIDTH|The width of DMA operations, if configured to allow half-word data access.<br>00b,01b - BYTE, Default = 1<br>10b - HALF_WORD. Half word (16 bits). This will make sure that 2 bytes are free/available in the<br>FIFO.<br>11b - Reserved|
|3-2<br>DMATB|DMA Write (To-bus) Trigger<br>If enabled with 1 or 2, DMATB starts a request DMA on a Tx trigger. See the Slave Data Control Register<br>(SDATACTRL). DMATB requests until full unless the DMA is set up as a trigger.<br>DMATB cancels on MSTATUS[ERRWARN].<br>00b - NOT_USED. DMA is not used<br>01b - ENABLE_ONE_FRAME. DMA is enabled for 1 Frame (ended by DMA or terminated).<br>DMATB auto-clears on a STOP or START (see the Match START or STOP bit<br>(SCONFIG[MATCHSS]).<br>10b - ENABLE. DMA is enabled until turned off. ENABLE must only be used with Master<br>Message mode.<br>11b - Reserved|
|1-0<br>DMAFB|DMA Read (From-bus) Trigger<br>If enabled with 1 or 2, DMAFB requests DMA on Rx trigger (see Slave Data Control Register<br>(SDATACTRL)). It requests until empty unless the DMA is set up as a trigger.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2572 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||DMAFB will cancel on SSTATUS[ERRWARN].|
||00b - DMA not used|
||01b - DMA is enabled for 1 frame. Auto-clears on STOP or repeated START. See the Match<br>START or STOP bit (SCONFIG[MATCHSS]).|
||10b - DMA Enable. DMA is enabled until it is turned off.|
||11b - Reserved|



### 70.6.11 Slave Data Control (SDATACTRL) 

##### Offset 

|Register|Offset|
|---|---|
|SDATACTRL|2Ch|



##### Function 

Assists in data control when no FIFO and FIFO when the FIFO is available (regardless of size). This allows some control over the FIFO behavior. In particular, it allows control of when to interrupt on fullness/emptiness and also controls behavior related to width, when not 1 byte wide. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2573-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>RXEM TXFUL<br>R 0 RXCOUNT  0 0 TXCOUNT<br>PTY  L<br>W<br>Reset 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>RXTRIG  TXTRIG<br>UNLO FLUS FLUS<br>W<br>CK  HFB  HTB<br>Reset 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Rx Is Empty|
|RXEMPTY|Default value is 1.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2573 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Rx is not empty<br>1b - Rx is empty|
|30<br>TXFULL|TX Is Full<br>0b - TX is not full<br>1b - TX is full|
|29|Reserved|
|—<br>28-24<br>RXCOUNT|Count Of Bytes In RX|
|23-22<br>—|Reserved|
|21<br>—<br>20-16|Reserved<br>Count Of Bytes In TX|
|TXCOUNT||
|15-8<br>—|Reserved|
|7-6<br>RXTRIG|Trigger Level For Rx FIFO Fullness<br>Affects interrupts and DMA (if enabled).<br>00b - Trigger on not empty<br>01b - Trigger on ¼ or more full<br>10b - Trigger on ½ or more full<br>11b - Trigger on 3/4 or more full|
|5-4<br>TXTRIG|Trigger Level For Tx FIFO Emptiness<br>Affects interrupts and DMA (if enabled). The default is Trigger on 1 less than full or less (=3).<br>00b - Trigger on empty<br>01b - Trigger on ¼ full or less<br>10b - Trigger on ½ full or less|
|3|11b - Trigger on 1 less than full or less (Default)<br>Unlock|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2574 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|UNLOCK|UNLOCK must be 1 in the same cycle while writing to TXTRIG or RXTRIG.<br>~~NOTE~~|
||0b - RXTRIG and TXTRIG fields cannot be changed on a write.|
||1b - RXTRIG and TXTRIG fields can be changed on a write.|
|2|Reserved|
|—||
|1|Flushes The From-bus Buffer/FIFO|
|FLUSHFB|Not normally used.|
|0|Flush The To-bus Buffer/FIFO|
|FLUSHTB|Used when the master terminates a to-bus (read) message prematurely.|



### 70.6.12 Slave Write Data Byte (SWDATAB) 

##### Offset 

|Register|Offset|
|---|---|
|SWDATAB|30h|



##### Function 

Write a byte of data, using the 9th bit to mark as the end (the last byte of the message). This register allows writing a byte to the bus (to Master) unless an external FIFO is used. This takes a byte and an end-of-data (last) marker bit. A byte should not be written unless there is room, as indicated by the TXNOTFULL bit being set in the SSTATUS register. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2575-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>END_<br>W<br>ALSO<br>Reset u u u u u u u u u u u u u u u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W END  DATA<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2575 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Fields 

|Field|Function|
|---|---|
|31-17|Reserved|
|—<br>16|End Also|
|END_ALSO|• If END_ALSO = 1, then this bit marks the last byte of the message<br>• If END_ALSO = 0, then there are more bytes in the message<br>END_ALSO is required to be used in I3C, but is optional in I2C.<br>For HDR-DDR, the byte with the END_ALSO must be an even byte (2nd, 4th, 6th, and so on.) because DDR<br>uses byte-pairs.|
|15-9<br>—|Reserved|
|8<br>END|End<br>• If END = 1, then this bit marks the last byte of the message.<br>• If END = 0, then there are more bytes in the message.<br>END is required to be used in I3C, but is optional in I2C.<br>For HDR-DDR, the byte with the END must be an even byte (2nd, 4th, 6th, and so on.) because DDR<br>uses byte-pairs.|
|7-0|Data|
|DATA|The data byte to send to the master.|



### 70.6.13 Slave Write Data Byte End (SWDATABE) 

##### Offset 

|Register|Offset|
|---|---|
|SWDATABE|34h|



##### Function 

Write a byte of data, which is the end (the last byte of the message). Write a byte just like SWDATAB, but mark as end-of-data (last byte). For HDR-DDR, the byte with the END must be an even (2nd, 4th, 6th，and so on) because DDR uses byte-pairs. A byte should not be written unless there is room, as indicated by SSTATUS[TXNOTFULL] = 1. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2576 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2577-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset u u u u u u u u u u u u u u u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W DATA<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-8<br>—|Reserved|
|7-0|Data|
|DATA|The data byte to send to the master.|



### 70.6.14 Slave Write Data Half-word (SWDATAH) 

##### Offset 

|Register|Offset|
|---|---|
|SWDATAH|38h|



##### Function 

Write a half-word of data, using the 16th bit to mark as the end (the last byte of the half-word is the end). This register allows writing a half-word (pair of bytes) to the bus unless an external FIFO is used. This takes a half-word, which will send out the Low byte and then the High byte. An end-of-data (last) marker bit is allowed (or must be 0). A half-word should not be written unless there is room for both, as indicated by the use of Tx FIFO level trigger or TXCOUNT available space in the SDATACTRL register. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2577 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W||||||||||||||||END|
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||||||||||||||
|W||||DA|TA1|||||||DA|TA0||||
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|



##### Fields 

|Field|Function|
|---|---|
|31-17|Reserved|
|—||
|16|End of message|
|END|• If END = 1, then END bit marks the last byte of the message<br>• If END = 0, then there are more bytes in the message<br>For this register, this always marks DATA1 as the end. END is required to be used in I3C, but is optional<br>in I2C.<br>For HDR-DDR (Double Data Rate), the byte with the END must be an even byte (2nd, 4th, 6th，and so on.)<br>because DDR uses byte-pairs.|
|15-8|Data 1|
|DATA1|The 2nd byte to send to the master.|
|7-0|Data 0|
|DATA0|The 1st byte to send to the master.|



### 70.6.15 Slave Write Data Half-word End (SWDATAHE) 

##### Offset 

|Register|Offset|
|---|---|
|SWDATAHE|3Ch|



##### Function 

Write a half word of data, which is the end (the last byte of the half word is the end). Write a half word (byte pair) just like MWDATAH, but mark the 2nd bytes as end-of-data (last byte). For HDR-DDR, the byte with the END must be an even (2nd, 4th, 6th，and so on) because DDR uses byte-pairs. A half word should not be written unless there is room for both, as indicated by the use of Tx FIFO level trigger or TXCOUNT available space in the SDATACTRL register. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2578 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2579-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset u u u u u u u u u u u u u u u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>W DATA1  DATA0<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16<br>—|Reserved|
|15-8|Data 1|
|DATA1|The 2nd byte to send to the master.|
|7-0|Data 0|
|DATA0|The 1st byte to send to the master.|



### 70.6.16 Slave Read Data Byte (SRDATAB) 

##### Offset 

|Register|Offset|
|---|---|
|SRDATAB|40h|



##### Function 

Read a byte of data. This register allows reading a byte from the bus (Master). A byte should not be read unless there is data waiting, as indicated by SSTATUS[RXPEND] = 1. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2579 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2580-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 DATA0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-8<br>—|Reserved|
|7-0|Data 0|
|DATA0|Byte read from the master.|



### 70.6.17 Slave Read Data Half-word (SRDATAH) 

##### Offset 

|Register|Offset|
|---|---|
|SRDATAH|48h|



##### Function 

Read a half word of data. This register allows reading a half word (byte pair) written by the Slave on an SDR Read or DAA or DDR. This is only used when using MCTRL to start the message. If MWMSG_SDR or MWMSG_DDR is used to start a message, that interface must be used exclusively. A half word should not be read unless there is at least 2 bytes of data waiting, as indicated the Rx FIFO level trigger or RXCOUNT available space in the SDATACTRL register. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2580 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2581-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset u u u u u u u u u u u u u u u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R MSB  LSB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16<br>—|Reserved|
|15-8|The 2nd byte read from the slave.|
|MSB||
|7-0|The 1st byte read from the slave.|
|LSB||



### 70.6.18 Slave Capabilities 2 (SCAPABILITIES2) 

##### Offset 

|Register|Offset|
|---|---|
|SCAPABILITIES2|5Ch|



##### Function 

Indicates which features are available and supported in this I3C module, including master and/or slave capabilities, HDR modes, and others. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2581 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2582-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>SSTW SSTS SLVR<br>R 0 AASA  0 GROUP  0<br>R  UB  ST<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>IBIXR I2CDE I2CRS I2C10<br>R 0 IBIEXT  0 MAPCNT<br>EG  VID  T  B<br>W<br>Reset 0 0 0 0 0 0 1 1 0 0 1 1 0 0 0 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-24<br>—|Reserved|
|23|Slave-Slave(s)-Tunnel Write Capable|
|SSTWR||
|22|Slave-Slave(s)-Tunnel Subscriber Capable|
|SSTSUB||
|21|Supports SETAASA|
|AASA|Set Static Address as Dynamic Address CCC|
|20|Reserved|
|—||
|19-18<br>GROUP|Group<br>GROUP is for v1.1 Group addressing. Groups use mapping, so MAPCNT must be same or greater than<br>GROUP value.<br>00b - Does not supports v1.1 Group addressing<br>01b - Supports one group<br>10b - Supports two groups<br>11b - Supports three groups|
|17|Slave Reset|
|SLVRST|Set to 1 if supports v1.1 Slave Reset<br>0b - Does not support Slave Reset|
||1b - Supports Slave Reset|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2582 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|16<br>—|Reserved|
|15-10<br>—|Reserved|
|9<br>IBIXREG|In-Band Interrupt Extended Register<br>The IBIEXT1 register is available. IBIEXT2 will be available if MAX in IBIEXT1 is >3.<br>0b - Does not support IBIXREG<br>1b - Supports IBIXREG|
|8<br>IBIEXT|In-Band Interrupt EXTDATA<br>Supports CTRL[EXTDATA] to allow data past MDB<br>0b - Does not support IBIEXT<br>1b - Supports IBIEXT|
|7<br>—|Reserved|
|6|I2C Device ID|
|I2CDEVID|Is 1 if I2C Device ID is supported<br>0b - Does not support I2CDEVID<br>1b - Supports I2CDEVID|
|5<br>I2CRST|I2C SW Reset<br>Is 1 if I2C SW Reset is supported<br>0b - Does not support I2CRST<br>1b - Supports I2CRST|
|4<br>I2C10B|I2C 10-bit Address<br>Is 1 if I2C 10-bit address is allowed in MAP 1 (so MAPCNT must be 1 or greater).<br>0b - Does not support I2C10B<br>1b - Supports I2C10B|
|3-0|Map Count|
|MAPCNT|Is 0 if no mapping ([DIP_I3C_00064]DYNADDR used to add more Static and/or Dynamic addresses to<br>act as virtual slaves[end]). Else, indicates how many are allowed.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2583 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

### 70.6.19 Slave Capabilities (SCAPABILITIES) 

##### Offset 

|Register|Offset|
|---|---|
|SCAPABILITIES|60h|



##### Function 

Indicates which features are available and supported in this I3C module, including master and/or slave capabilities, HDR modes, and others. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2584-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>TIMEC<br>R DMA  INT  FIFORX  FIFOTX  EXTFIFO  0 IBI_MR_HJ<br>TRL<br>W<br>Reset 1 1 1 1 1 1 0 0 0 0 1 1 1 1 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>MAST<br>R CCCHANDLE  SADDR  0 HDRSUPP  IDREG  IDENA<br>ER<br>W<br>Reset 1 1 1 1 1 1 1 0 0 1 1 1 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Direct Memory Access|
|DMA|0b - DMA is not supported<br>1b - DMA is supported|
|30|Interrupts|
|INT|0b - Interrupts are not supported<br>1b - Interrupts are supported|
|29-28|FIFO Receive|
|FIFORX|Indicates if Rx (from-bus) is enabled and what size it is.<br>00b - FIFO_2BYTE. 2 (or 3)-byte Rx FIFO, the default FIFO receive value (FIFORX)<br>01b - FIFO_4BYTE. 4-byte Rx FIFO<br>10b - FIFO_8BYTE. 8-byte Rx FIFO<br>11b - FIFO_16BYTE. 16-byte Rx FIFO or larger|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2584 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|27-26<br>FIFOTX|FIFO Transmit<br>Indicates if Tx (to-bus) is enabled and what size it is.<br>00b - FIFO_2BYTE. 2-byte Tx FIFO, the default FIFO transmit value (FIFOTX)<br>01b - FIFO_4BYTE: 4-byte Tx FIFO<br>10b - FIFO_8BYTE: 8-byte Tx FIFO<br>11b - FIFO_16BYTE: 16-byte Tx FIFO or larger|
|25-23<br>EXTFIFO|External FIFO<br>Indicates whether External FIFOs are enabled. If External FIFOs are not enabled, then check FIFOTX<br>and FIFORX for the internal FIFO.<br>000b - NO_EXT_FIFO. No external FIFO is available<br>001b - STD_EXT_FIFO. Standard available/free external FIFO<br>010b - REQUEST_EXT_FIFO. Request track external FIFO<br>011b - Reserved|
|22<br>—<br>21<br>TIMECTRL|Reserved<br>Time Control<br>Specifies if any time-control type is supported or not.<br>0b - NO_TIME_CONTROL_TYPE. No time control is enabled<br>1b - ATLEAST1_TIME_CONTROL. At least one time-control type is supported|
|20-16<br>IBI_MR_HJ|In-Band Interrupts, Master Requests, Hot-Join Events<br>Indicates which events (IBI, MR, and HJ) are allowed. For example, if this field is set to 00011b, it means<br>that IBI (bit 0) and IBI_HAS_DATA (bit 1) functionality are both enabled.<br>• Bit 0: IBI: Supports the application generating an IBI<br>• Bit 1: IBI_HAS_DATA: When bit 0 = 1, the IBI has data from the SCTRL register<br>• Bit 2: MASTER_REQUEST: Supports the application generating a Master Request for a secondary<br>master<br>• Bit 3: HOT_JOIN: Supports the application generating Hot-Join<br>• Bit 4: BAMATCH_FOR_BUS: Use the BAMATCH register for bus-available timing|
|15-12<br>CCCHANDLE|Common Command Codes Handling<br>Indicates who handles CCC between I3C module and the user application.<br>• Bit 0: BLOCK_HANDLE: The block (I3C module) handles events, activities, status, HDR, and if<br>enabled for it, ID and static address related things|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2585 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

Table continued from the previous page... 

|Field|Function<br>• Bit 1: MAX_READ_WRITE: The block handles maximum read and write lengths, and max data<br>speed<br>• Bit 2: PENDINT_ACTSTATE: GETSTATUS CCC (command code) returns the SCTRL register’s<br>Pending interrupt (PENDINT) and activity state (ACTSTATE) fields<br>• Bit 3: VENDINFO: GETSTATUS CCC returns the SCTRL register’s VENDINFO (vendor info) bits|
|---|---|
|11-10<br>SADDR|Static Address<br>Indicates how the static address is handled.<br>00b - NO_STATIC. No static address<br>01b - STATIC. Static address is fixed in hardware<br>10b - HW_CONTROL. Hardware controls the static address dynamically (for example, from the<br>pin strap)<br>11b - CONFIG. SCONFIG register supplies the static address|
|9<br>MASTER|Master<br>Specifies if a master capability is supported or not.<br>0b - MASTERNOTSUPPORTED. Master capability is not supported.<br>1b - MASTERSUPPORTED. Master capability is supported.|
|8<br>—|Reserved|
|7-6<br>HDRSUPP|High Data Rate Support<br>Indicates which HDR modes are supported.<br>• Bit 0 = 1: Double Data Rate<br>• Bit 1: Reserved|
|5-2<br>IDREG|ID Register<br>Bits indicate what is in the registers vs. what is in the hardware.<br>• Bit 0: ID_INSTANCE: ID Instance is a register, and is used if there is no PARTNO register.<br>• Bit 1: IDRAND: an ID Random field is available<br>• Bit 2: DCR: a Device Characteristic Register (DCR) is available<br>• Bit 3: BCR: a Bus Characteristics Register (BCR) is available|
|1-0<br>IDENA|ID 48b Handler<br>Indicates who handles the ID 48b value.<br>00b - APPLICATION. Application handles ID 48b<br>01b - HW. Hardware handles ID 48b|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2586 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||10b - HW_BUT. In hardware but the I3C module instance handles ID 48b.|
||11b - PARTNO. A part number register (PARTNO) handles ID 48b|



### 70.6.20 Slave Maximum Limits (SMAXLIMITS) 

##### Offset 

|Register|Offset|
|---|---|
|SMAXLIMITS|68h|



##### Function 

Indicates the limits set by the master (or the original requested limits). The maximum limits are not enabled in the hardware design, including maximum read and write lengths. If the maximum read/write lengths are enabled, then the current setting (including default request) shows up in this register (SMAXLIMITS). 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2587-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>MAXWR<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>MAXRD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-28|Reserved|
|—||
|27-16|Maximum Write Length|
|MAXWR|The maximum write length must be between 8 to 4095 (saturation). The application must not set the<br>maximum write length longer than what the master sets the maximum write length to. The application<br>should set the maximum write length to be less than what the master sets the maximum write length to.|
|15-12|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2587 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|11-0|Maximum Read Length|
|MAXRD|The maximum read length must be between 16 to 4095 (saturation). The application should not set the<br>maximum read length longer than what the master sets the maximum read length to. The application<br>should set the maximum read length to be less than what the master sets the maximum read length to.|



### 70.6.21 Slave ID Part Number (SIDPARTNO) 

##### Offset 

|Register|Offset|
|---|---|
|SIDPARTNO|6Ch|



##### Function 

Allows an application to write the ID part-number. The application must write a non-zero value into the PARTNO field, because 0 is not valid. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||PAR|TNO||||||||
|Reset|0|1|1|1|1|0|0|1|1|0|0|1|0|1|1|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||PAR|TNO||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|1|1|1|0|1|



##### Fields 

|Field|Function|
|---|---|
|31-0|Part number|
|PARTNO||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2588 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

### 70.6.22 Slave ID Extension (SIDEXT) 

##### Offset 

|Register|Offset|
|---|---|
|SIDEXT|70h|



##### Function 

Allows an application to write the ID extension of the Device Characteristic Register (DCR) and/or the Bus Characteristics Register (BCR). 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||||0|||||||BC|R||||
|Reset|0|0|0|0|0|0|0|0|0|1|1|0|0|1|1|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||D|CR||||0||0||||0||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-24|Reserved|
|—||
|23-16|Bus Characteristics Register|
|BCR|Set the Bus Characteristics Register (BCR) if configured for it. This controls features like Secondary<br>Master, slow speed requirements, and others.|
|15-8|Device Characteristic Register|
|DCR|Set the Device Characteristic Register (DCR) if configured for it.|
|7<br>—|Reserved|
|6-4<br>—|Reserved|
|3-0<br>—|Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2589 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

### 70.6.23 Slave Vendor ID (SVENDORID) 

##### Offset 

|Register|Offset|
|---|---|
|SVENDORID|74h|



##### Function 

Allows an application to write the Vendor ID. The default is set from the constant field and is the chip vendor ID. If using the chip vendor ID, the PARTNO does not collide with other uses. The MIPI Vendor ID is available to all companies (MIPI membership is not required) to get a vendor ID make a request at the mipi.org website. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2590-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>VID<br>W<br>Reset 0 0 0 0 0 0 0 1 0 0 0 1 1 0 1 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-15<br>—|Reserved|
|14-0|Vendor ID|
|VID|May be set to the 15-bit MIPI Vendor ID, if used.|



### 70.6.24 Slave Time Control Clock (STCCLOCK) 

##### Offset 

|Register|Offset|
|---|---|
|STCCLOCK|78h|



##### Function 

Allows an application to dynamically set the time control clock and accuracy information. The clock frequency and accuracy are constant set by the hardware. But, if the clock can be adjusted (that is, divided) or if the accuracy could vary with knowable information, then the clock may be set via this register. This register must be updated whenever the clock source is changed. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2590 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2591-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>FREQ  ACCURACY<br>W<br>Reset 0 0 1 1 0 0 0 0 0 0 0 0 1 0 1 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16|Reserved|
|—||
|15-8|Clock Frequency|
|FREQ|Clock frequency in 0.5-MHz steps. For example, 10 MHz is FREQ = 20. Default set by parameters if<br>configured.|
|7-0|Clock Accuracy|
|ACCURACY|Clock accuracy in 1/10ths of %. For example, 1.5% is 15. Default set by parameters if configured.|



### 70.6.25 Slave Message Map Address (SMSGMAPADDR) 

##### Offset 

|Register|Offset|
|---|---|
|SMSGMAPADDR|7Ch|



##### Function 

When the DYNADDR register is used to build a list of extra DAs or SAs to match, this register allows the software to determine which address was matched when STATUS[MATCHED]= 1. It holds the last 3 matches. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2591 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||0||||||||MAPL|ASTM2||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||0||||MAPLA|STM1|||0||LASTS<br>TA...||MAP|LAST||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-20|Reserved|
|—||
|19-16|Matched Previous Index 2|
|MAPLASTM2|0 for the base address.|
|15-12<br>—|Reserved|
|11-8|Matched Previous Address Index 1|
|MAPLASTM1|0 for the base address.|
|7-5<br>—|Reserved|
|4|Last Static Address Matched|
|LASTSTATIC|1 if last matched address was an I2C Static address vs. an I3C Dynamic Address.|
|3-0|Matched Address Index|
|MAPLAST|Matched address index for current or last matched message. 0 for the base address.|



### 70.6.26 Master Extended Configuration (MCONFIG_EXT) 

##### Offset 

|Register|Offset|
|---|---|
|MCONFIG_EXT|80h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2592 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Function 

Used for special extended configurations, including for I2C use. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||0|||||||I3C_CAS|R_DEL|I3C_CA|S_DEL|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||0||||0|||0||0|0||0|||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-20<br>—|Reserved|
|19-18<br>I3C_CASR_DE<br>L|I3C CAS Delay After Repeated START<br>Setting can be configured to delay the clock after a repeated START to provide more time for slow I3C<br>devices. Note that max may be less if internal clock is very fast.<br>00b - No Delay<br>01b - Increases SCL clock period by 1/2.<br>10b - Increases SCL clock period by 1.<br>11b - Increases SCL clock period by 1 1/2.|
|17-16<br>I3C_CAS_DEL|I3C CAS Delay after START<br>Setting can be configured to delay the clock after the START to be longer by increasing SCL clock<br>period. A Note that max may be less if internal clock is very fast.<br>00b - No Delay<br>01b - Increases SCL clock period by 1/2.<br>10b - Increases SCL clock period by 1.<br>11b - Increases SCL clock period by 1 1/2.|
|15-12<br>—<br>11-8<br>—|Reserved<br>Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2593 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|7-6<br>—|Reserved|
|5<br>—|Reserved|
|4<br>—|Reserved|
|3-0<br>—|Reserved|



### 70.6.27 Master Control (MCTRL) 

##### Offset 

|Register|Offset|
|---|---|
|MCTRL|84h|



##### Function 

Starts activities on the I3C or I2C bus. Also see the MWMSG register. A request cannot be changed when a message is in flight, the REQUEST field will go to 0 automatically. 

~~<mark>NOTE</mark>~~ 

If MCONFIG[MSTENA] is set for I2C Master mode (legacy I2C), then no REQUEST other than 1 or 2 are accepted. Likewise, fields are constrained to I2C supported fields. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2594-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>RDTERM<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>ADDR  DIR  IBIRESP  TYPE  REQUEST<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2594 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Fields 

|Field|Function|
|---|---|
|31-24<br>—|Reserved|
|23-16<br>RDTERM|Read Terminate<br>The termination counter for reads.<br>• For I2C, RDTERM controls when to NACK the read.<br>• For I3C, RDTERM can be use to terminate (end) a read that is too long.<br>— RDTERM = 0 has no effect<br>— RDTERM = 1 terminates after the next character<br>— RDTERM = 2 terminates after the next 2 characters<br>Supports up to 255 characters. If in Double Data Rate (DDR) mode, then RDTERM terminates the<br>read, based on word counts (for DDR) vs. byte counts (for SDR).<br>The value 1 may be written any time, but a number larger than 1 should normally be written<br>when starting the EmitStartAddress.<br>~~NOTE~~<br>Self clears on complete.|
|15-9<br>ADDR|Address<br>I3C Dynamic Address or I2C Static Address. Some values are not allowed depending on whether using<br>I3C or I2C bus.|
|8<br>DIR|Direction<br>0b - DIRWRITE: Write<br>1b - DIRREAD: Read|
|7-6<br>IBIRESP|In-Band Interrupt Response<br>The response to use when you get an IBI from START, and to force using a IBI ACK NACK request when<br>completing a manual IBI. Completion of a manual IBI means that the slave Dynamic Address (DA) is known,<br>and so the mandatory byte (or not) is specified by the application when ACKing.<br>Master Request and Hot-Join will always go to Manual and so the application will have<br>to decide.<br>~~NOTE~~<br>MIBIRESP register is also used when a message is emitted in Message Mode using the MWMSG_SDR or<br>MWMSG_DDR registers.<br>If an IBI with MDB (mandatory byte) is ACKED, the Master will limit to a max of 8 more bytes after the MDB.<br>RDTERM = 1 can be used with Request = None to terminate data from Slave sooner.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2595 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2596-03.png)


<!-- Start of picture text -->
Field Function<br>Value Meaning when REQUEST = 1 (EmitStartAddr) or  Meaning when REQUEST =<br>REQUEST = 7 (AutoIBI) 3 (IBIAckNack)<br>0 ACK. Mandatory byte (or not) is decided by Master In-band  ACK. No mandatory byte.<br>Interrupt Registry and Rules (MIBIRULES).<br>1 NACK NACK<br>2 ACK with mandatory byte ignores MIBIRULES. Do not use  ACK with mandatory byte.<br>unless only Slaves with a mandatory byte can cause an IBI.<br>3 Manual. Stop and wait for a decision using the  Reserved<br>IBIAckNack request.<br>00b - ACK. Acknowledge. A mandatory byte (or not) is decided by the Master In-band Interrupt<br>Registry and Rules Register (MIBIRULES). The meaning for Manual (IBI ACK NACK) mode is<br>that this setting is ACK with no mandatory byte.<br>01b - NACK. Not acknowledge<br>10b - ACK_WITH_MANDATORY. Acknowledge with mandatory byte (ignores the MIBIRULES<br>register). Acknowledge with mandatory byte should not be used, unless only slaves with a<br>mandatory byte can cause an IBI.<br>11b - MANUAL. Stop and wait for a decision using the IBI ACK NACK request. The meaning for<br>Manual (IBI ACK NACK) mode is that this setting is reserved.<br>5-4 Bus Type with EmitStartAddr<br>TYPE<br>Value Meaning when REQUEST = 1 (EmitStartAddr) Meaning when REQUEST = 6 (ForceExit)<br>0 I3C - SDR mode of I3C Exit Pattern<br>1 I2C - Standard I2C protocol Reserved<br>2 DDR - HDR-DDR mode of I3C. Enter DDR  Slave Reset<br>mode (7E and then ENTHDR0), if the module<br>is not in DDR mode. The 1st byte written to the<br>Tx FIFO must be a command and already in the<br>FIFO. To end DDR mode, use ForceExit.<br>3 BT - HDR-BT mode of I3C. If not already in  Reserved<br>HDR-BT, will automatically Enter BT (send 7E<br>and ENTHDR3). When using this, you must<br>also set the MHDRBTCFG register for multilane<br>and CMD rules.<br>Value Meaning - DAA processing TYPE (rules) when REQUEST = 4 (ProcessDAA)<br>0 DA comes from MWDATAB[VALUE], if not 1st time, continues to next 7E/R request.<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2596 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||Value<br>Meaning - DAA processing TYPE (rules) when REQUEST = 4 (ProcessDAA)|
||1<br>Reserved|
||2<br>DA comes from MWDATAB[VALUE], if not 1st time, STOPs after assignment.|
||3<br>Reserved|
||00b - I3C. When REQUEST = 1 (EmitStartAddr), the SDR mode of I3C. When REQUEST = 6<br>(ForceExit), the Exit pattern.<br>01b - I2C. When REQUEST = 1 (EmitStartAddr), the Standard I2C protocol.<br>10b - DDR. When REQUEST = 1 (EmitStartAddr), the HDR-DDR mode of I3C. Enter DDR mode<br>(7E and then ENTHDR0), if the module is not in DDR mode. The 1st byte written to the Tx<br>FIFO must be a command and already in the FIFO. To end DDR mode, use ForceExit. When<br>REQUEST = 6 (ForceExit), Slave Reset.<br>11b - Reserved|
|3<br>—<br>2-0<br>REQUEST|Reserved<br>Request<br>Emits the requested operation when doing in pieces vs. doing by message. TheMaster Status<br>(MSTATUS)should be checked because the state of the Master must be such that the request makes<br>sense. For example, the system cannot do SDR from DDR (but can do DDR from SDR since it enters),<br>cannot use an incorrect request if in DAA mode, and other similar situations.<br>000b - NONE. Returns to NONE when finished with any request. The MSTATUS register<br>indicates the master's state. See also AutoIBI mode. NONE is only written as 0: when setting<br>RDTERM to 1 (to stop a read in progress) or when setting IBI response field (IBIRESP) for MSG<br>use.<br>001b - EMITSTARTADDR. Emit START with address and direction from a stopped state or in the<br>middle of a Single Data Rate (SDR) message. If from a stopped state (IDLE), then emit start may<br>be prevented by an event (like IBI, MR, HJ), in which case the appropriate interrupt is signaled.<br>Emit START can be resubmitted.<br>010b - EMITSTOP. Emit a STOP on bus. Must be in Single Data Rate (SDR) mode. If in Dynamic<br>Address Assignment (DAA) mode, Emit stop will exit DAA mode.<br>011b - IBIACKNACK. Manual IBI ACK or NACK. When IBIRESP has indicated a hold on an IBI to<br>allow a manual decision, this request completes it. Uses IBIRESP to provide the information.<br>100b - PROCESSDAA. If not in Dynamic Address Assignment (DAA) mode now, will issue<br>START, 7E, ENTDAA, and then emits 7E/R to process first Slave. Stops just before the new<br>Dynamic Address (DA) is to be emitted. The DA is written using MWDATAB and then Process<br>DAA is requested again to write the new address, and then starts the next unless marked to<br>STOP. An MSTATUS indicating NACK means DA was not accepted (for example, parity error).<br>If PROCESSDAA is NACKED on the 7E/R, which means no more Slaves need a DA, then a|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2597 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||COMPLETE will be signaled (along with DONE) and a STOP issued. If TYPE = 2 or TYPE = 3,<br>the DA will be assigned and then it will emit a STOP vs. starting a new 7E/R request. If TYPE = 1<br>or TYPE = 3, then the DA is taken from the ADDR field (bits 6:0).<br>101b - Reserved|
||110b - Force Exit and Slave Reset. Emit an Exit Pattern from any state, but end Double Data<br>Rate (DDR) (including MSGDDR). If in DDR mode，include a STOP afterward. If TYPE == 2,<br>then it performs a Slave Reset action (RSTACT can prevent the reset in the slave). Slave Reset<br>may follow right after RSTACT CCC or after STOP.<br>111b - AUTOIBI. Hold in a stopped state, but auto-emit START, 7E when the slave is holding<br>down SDA to get an IBI. Actual IBI handling is defined by IBIRESP.|



### 70.6.28 Master Status (MSTATUS) 

##### Offset 

|Register|Offset|
|---|---|
|MSTATUS|88h|



##### Function 

Status for the master, including which events caused the interrupts. The peripherals share the IRQ (called Parallel-toSlave status). 

Because a peripheral can only be in a Master or Slave mode, but not be in both modes at the same time, then only one (Slave or Master peripheral) can be the cause of the IRQ. So, if there is an IRQ and the peripheral is a Master, then this register (MSTATUS) has the status. 

If there is an IRQ and the peripheral is a Slave, then the SSTATUS register has the status. 

##### Self clears on COMPLETE. 

If MCONFIG is set for I2C only, some states and bits will never be active (for example, DAA or IBI). 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18<br>17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|0||||IBIADDR||||||0||NOWM<br>AST...|0||
|W|||||||||||||W1C|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2<br>1|0|
|R|ERRW<br>ARN|0|IBIWO<br>N|TXNO<br>TFU...|RXPE<br>ND|COMP<br>LETE|MCTR<br>LDO...|SLVST<br>ART|IBITY|PE|NACK<br>ED|BETW<br>EEN|0|STATE||
|W|||W1C|||W1C|W1C|W1C||||||||
|Reset|0|0|0|1|0|0|0|0|0|0|0|0|0|0<br>0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2598 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Fields 

|Field|Function|
|---|---|
|31<br>|Reserved|
|—<br>30-24<br>IBIADDR|IBI Address<br>The address of the IBI (while IBITYPE = 1) or the Master Request (MR )(while IBITYPE = 2) or is 7’h2 if<br>Hot-Join (while IBITYPE = 3).|
|23-20<br>—|Reserved|
|19|Now Master (now this module is a master)|
|NOWMASTER|NOWMASTER = 1 if the module is now a master (it was previously a slave, acceptance was requested<br>from the previous master and it was accepted). Note that the reverse operation (master becomes a<br>slave) does not need an interrupt, because the application is granting it through the Common-Command-<br>Code status bit MSTATUS[CCC].|
|18-16<br>—|Reserved|
|15<br>ERRWARN|Error Or Warning<br>ERRWARN = 1, if an error occurred (like improper register use, overrun or underrun of FIFO/buffer,<br>invalid parity or CRC in DDR read, and others). See the Master Errors and Warnings Register<br>(MERRWARN).|
|14<br>—|Reserved|
|13<br>IBIWON|In-Band Interrupt (IBI) Won<br>IBIWON is set to 1 if IBI or MR or HJ won the arbitration on a header address, regardless of whether it was<br>NACKED or ACKED.<br>Note that this requires manual intervention for MR and HJ, and optionally requires it for IBI if the<br>MCTRL[IBIRESP] indicates Manual (is 3).|
|12<br>TXNOTFULL|TX buffer/FIFO not yet full<br>TXNOTFULL = 1 if TX buffer/FIFO or message register can accept another byte or half-word; FIFO will<br>use trigger level. If DMA enabled for TX, it will transfer data as long as not full. Default: 1.|
|11<br>RXPEND|RXPEND<br>The receiving message from a slave and byte(s) are in the input buffer/FIFO.<br>• If using a FIFO, this is one FIFO trigger’s worth.<br>• If DMA is enabled for Rx, then DMA will be signaled.<br>RXPEND will self-clear when the data is read.|
|10|Complete|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2599 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|COMPLETE|A message has completed:<br>• With MWMSG_SDR or MWMSG_DDR, this is count to 0.<br>• With MCTRL using EmitStartAddr, this is the end of write or read by terminate or end.<br>• With IBI (AutoIBI or EmitStartAddr), this is the end of IBI data (if any).|
|9|Master Control Done|
|MCTRLDONE|After the module completes an MCTRL request, MCTRLDONE is set to 1 . MCTRLDONE self-clears<br>when writing a new control, otherwise write to MCTRLDONE to clear it (MCTRLDONE).<br>• When MCTRL[REQUEST] = EmitStartAddr, MCTRLDONE fires (sets to 1) when the address went<br>out (and was ACKED or NACKED or ended in an IBI). However if ACKED, it then fires COMPLETE<br>when the write or read data has completed.<br>• When MCTRL[REQUEST] = ProcessDAA, this fires when the module is ready to emit the Dynamic<br>Address (DA) for the slave, or when no more slaves are ACKing. This can be determined using the<br>MSTATUS[BETWEEN] and MSTATUS[STATE] fields.|
|8|Slave Start|
|SLVSTART|If a slave is/was requesting a START by holding SDA low, SLVSTART is set to 1. Handling starts<br>automatically if MCTRL[REQUEST] = AutoIBI.|
|7-6<br>IBITYPE|In-Band Interrupt (IBI) Type<br>Indicates the type of In-Band Interrupt (IBI) of the last event that won the arbitration (whether the<br>interrupt is ACKED or NACKED or pending)<br>00b - NONE. Cleared when IBI Won bit (MSTATUS[IBIWON]) is cleared<br>01b - IBI. In-Band Interrupt<br>10b - MR. Master Request<br>11b - HJ. Hot-Join|
|5<br>NACKED|Not Acknowledged<br>If NACKED = 1, then the last Start and Address was NACKED (was not ACKED by the addressed slave).|
|4<br>BETWEEN<br>3|Between<br>Between messages or Dynamic Address Assignments (DAA)<br>Active if:<br>• STATE is MSGSDR, DDR, or DAA, the state is between messages/DAAs and so is expecting a new<br>messages/DAAs to start (or STOP or Exit).<br>• STATE is NORMACT, then the module is stuck waiting on the Tx FIFO to be not-empty or the Rx<br>FIFO to be not full.<br>0b - Inactive. For other cases.<br>1b - Active. If STATE is MSGSDR, DDR, DAA, or if STATE is NORMACT.<br>Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2600 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|2-0|State Of The Master|
|STATE|Indicates the current master state<br>000b - IDLE: the bus has Stopped.<br>001b - SLVREQ. (Slave Request state) the bus has Stopped but a slave is holding SDA low. If<br>using auto-emit IBI (MCTRL[AutoIBI]), then the master will not stay in the Slave Request state.<br>010b - MSGSDR. In Single Data Rate (SDR) Message state (from using MWMSG_SDR)<br>011b - NORMACT. Normal active Single Data Rate (SDR) state (from using MCTRL and<br>MWDATAn and MRDATAn registers). The master stays in the NORMACT state until a STOP<br>is issued.<br>100b - MSGDDR. In Double Data Rate (DDR) Message mode (from using MWMSG_DDR or<br>using the normal method with DDR). The master stays in the DDR state, until the master exits<br>using EXIT (emits the Exit pattern).<br>101b - DAA. In Enter Dynamic Address Assignment (ENTDAA) mode<br>110b - IBIACK. Waiting for an In-Band Interrupt (IBI) ACK/NACK decision<br>111b - IBIRCV. Receiving an In-Band Interrupt (IBI), this IBIRCV state is used after IBI/MR/HJ<br>has won the arbitration, and IBIRCV state is also used for IBI mandatory byte (if any) and any<br>bytes that follow.|



### 70.6.29 Master In-band Interrupt Registry and Rules (MIBIRULES) 

##### Offset 

|Register|Offset|
|---|---|
|MIBIRULES|8Ch|



##### Function 

Contains the rules for using IBI, and keeps a registry of the slaves that use the IBI byte. 

Allows defining the IBI mandatory byte rules for the Slaves. It allows defining the Slaves which do not have a mandatory byte or the ones which do (whichever is easier and fits). 

Concerning ADDRn fields: The address is 6 bits. Assuming that MIBIRULES[MSB0] = 1, then each address has its most significant bit = 0. This means that each address is 7 bits (usually written as A7 to A1) and the A7 must be 0. If the application does not use that optimal convention, then the Manual method of IBI ACK handling must be used (see MCTRL). 

- The default is that the ADDRn values indicate the slaves with a mandatory byte. 

- If MIBIRULES[NOBYTE] is set, then the ADDRn values indicate slaves that do not have a mandatory IBI byte. 

~~<mark>NOTE</mark>~~ 

A7 = 0 is only needed for Slaves that use IBI. For legacy I2C devices, A7 can use any valid value, because I2C devices cannot cause an IBI. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2601 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2602-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R NOBY<br>MSB0  ADDR4  ADDR3  ADDR2<br>W TE<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>ADDR2  ADDR1  ADDR0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|No IBI byte|
|NOBYTE|• If NOBYTE = 1, then the ADDRx fields refer to slaves without a mandatory IBI byte.<br>• If NOBYTE = 0, then the ADDRx fields refer to slaves with a mandatory IBI byte.|
|30|Set Most Significant address Bit to 0|
|MSB0|If MSB0 = 1, then all I3C dynamic addresses are assigned with the MSb==0 (most significant bit). This<br>allows the START header to be optimized.|
|29-24|ADDR4|
|ADDR4|Address of slave with or without Mandatory IBI byte. If 0, then the address does not apply.|
|23-18|ADDR3|
|ADDR3|Address of slave with or without Mandatory IBI byte. If 0, then the address does not apply.|
|17-12|ADDR2|
|ADDR2|Address of slave with or without Mandatory IBI byte. If 0, then the address does not apply.|
|11-6|ADDR1|
|ADDR1|Address of slave with or without Mandatory IBI byte. If 0, then the address does not apply.|
|5-0|ADDR0|
|ADDR0|Address of slave with or without Mandatory IBI byte. If 0, then the address does not apply.|



### 70.6.30 Master Interrupt Set (MINTSET) 

##### Offset 

|Register|Offset|
|---|---|
|MINTSET|90h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2602 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Function 

Set interrupt enables for select bits in MSTATUS. Reading the MINTSET register returns the status of the interrupt enables. 

- To activate an interrupt enable, write 1. 

- To disable an interrupt enable, write 1 to the appropriate bit in the Interrupt Clear Register (MINTCLR). Writing 0 to the interrupt enable in this register (MINTSET) does not disable the interrupt. 

The Interrupt registers allow masking interrupt sources, as well as checking which interrupts have activated in the MSTATUS register. The normal method is to enable an interrupt and then once that interrupt fires, the interrupt is either cleared by writing the MSTATUS register or cleared by action on the corresponding data register. The interrupt is level held, meaning that the interrupt stays set until the cause is cleared, by some method. The module prevents races so that if a new event comes in, that new event will not be lost. 

These interrupts are parallel to the Slave Interrupt Set (SINTSET)/Slave Interrupt Clear (SINTCLR) set, and only one interrupt set is active depending on state (Master or Slave operation). 

- MINTSET: Sets interrupt enables for MSTATUS bits. Reading MINTSET register returns the status of the interrupt enables. 

- MINTCLR: Clears interrupt enables for MSTATUS bits. 

- MINTMASKED: Returns the value of the MSTATUS bits ANDed with their interrupt enables. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||0|||||||NOWM||0||
|W|||||||||||||AST...||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|ERRW|0|IBIWO|TXNO|RXPE|COMP|MCTR|SLVST|||||0||||
|W|ARN||N|TFU...|ND|LETE|LDO...|ART|||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-20|Reserved|
|—||
|19|Now Master (now this I3C module is a master) Interrupt Enable|
|NOWMASTER||
|18-16<br>—|Reserved|
|15|Error or Warning (ERRWARN) Interrupt Enable|
|ERRWARN||
|14|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2603 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Table continued from the previous page... 

|Field<br>—|Function|
|---|---|
|13<br>IBIWON|In-Band Interrupt (IBI) Won Interrupt Enable|
|12<br>TXNOTFULL|TX buffer/FIFO is not full interrupt enable|
|11<br>RXPEND|Rx Pending Interrupt Enable|
|10<br>COMPLETE|Completed Message Interrupt Enable|
|9<br>MCTRLDONE|Master Control Done Interrupt Enable|
|8<br>SLVSTART|Slave Start Interrupt Enable|
|7-0<br>—|Reserved|



### 70.6.31 Master Interrupt Clear (MINTCLR) 

##### Offset 

|Register|Offset|
|---|---|
|MINTCLR|94h|



##### Function 

Clear interrupt enables for select Master Status (MSTATUS) bits. Writing a 1 clears the corresponding interrupt enable. Writing a 0 has no effect. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2604 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||0|||||||NOWM<br>AST...||0||
|W|||||||||||||W1C||||
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|ERRW<br>ARN|0|IBIWO<br>N|TXNO<br>TFU...|RXPE<br>ND|COMP<br>LETE|MCTR<br>LDO...|SLVST<br>ART|||||0||||
|W|W1C||W1C|W1C|W1C|W1C|W1C|W1C|||||||||
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|



##### Fields 

|Field|Function|
|---|---|
|31-20<br>—|Reserved|
|19<br>NOWMASTER|NOWMASTER Interrupt Enable Clear|
|18-16<br>—|Reserved|
|15<br>ERRWARN|ERRWARN Interrupt Enable Clear|
|14<br>—|Reserved|
|13<br>IBIWON|IBIWON Interrupt Enable Clear|
|12<br>TXNOTFULL|TXNOTFULL Interrupt Enable Clear|
|11<br>RXPEND|RXPEND Interrupt Enable Clear|
|10<br>COMPLETE|COMPLETE Interrupt Enable Clear|
|9|MCTRLDONE Interrupt Enable Clear|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2605 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|MCTRLDONE||
|8|SLVSTART Interrupt Enable Clear|
|SLVSTART||
|7-0<br>—|Reserved|



### 70.6.32 Master Interrupt Mask (MINTMASKED) 

##### Offset 

|Register|Offset|
|---|---|
|MINTMASKED|98h|



##### Function 

Returns the status of enabled interrupts (the value of Master Status (MSTATUS) ANDed with the value of Master Interrupt Set (MINTSET)). 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2606-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>NOWM<br>R 0 0<br>AST...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>ERRW IBIWO TXNO RXPE COMP MCTR SLVST<br>R 0 0<br>ARN  N  TFU... ND  LETE  LDO... ART<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-20<br>—|Reserved|
|19|NOWMASTER Interrupt Mask|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2606 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|NOWMASTER||
|18-16<br>—|Reserved|
|15<br>ERRWARN|ERRWARN Interrupt Mask|
|14<br>—|Reserved|
|13<br>IBIWON|IBIWON Interrupt Mask|
|12<br>TXNOTFULL|TXNOTFULL Interrupt Mask|
|11<br>RXPEND|RXPEND Interrupt Mask|
|10<br>COMPLETE|COMPLETE Interrupt Mask|
|9<br>MCTRLDONE|MCTRLDONE Interrupt Mask|
|8<br>SLVSTART|SLVSTART Interrupt Mask|
|7-0<br>—|Reserved|



### 70.6.33 Master Errors and Warnings (MERRWARN) 

##### Offset 

|Register|Offset|
|---|---|
|MERRWARN|9Ch|



##### Function 

Contains errors and warnings from I3C/I2C protocol. When any errors or warnings are not 0, then the MSTATUS[ERRWARN] bit will be set. 

##### Parallel-to-slave ERRWARN: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2607 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

- In Master mode, use this register (MERRWARN). 

- In Slave mode, use the slave register Slave Errors and Warnings (SERRWARN). 

The error bits in both registers (MERRWARN and SERRWARN) are similar in meaning. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||0|||||0|TIMEO<br>UT|INVRE<br>Q|MSGE<br>RR|OWRI<br>TE|OREA<br>D|
|W||||||||||||W1C|W1C|W1C|W1C|W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||0||0|0|HCRC|HPAR||0|||Reserv<br>ed|WRAB<br>T|NACK|Reserv<br>ed|0|
|W||||||W1C|W1C|||||W1C|W1C|W1C|W1C||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-22|Reserved|
|—<br>21|Reserved|
|—<br>20|Timeout Error|
|TIMEOUT|The module has stalled too long in a frame. This happens when:<br>• The Tx FIFO or Rx FIFO is not handled and the bus is stuck in the middle of a message,<br>• No STOP was issued and between messages,<br>• IBI manual is used and no decision was made.<br>The maximum stall period is 10 kHz or 100 µs.|
|19<br>INVREQ|Invalid Request Error<br>Invalid use of a request:<br>• Not using IBI ACK NACK when stopped in manual hold for IBI acknowledge.<br>• Using other than ForceStop or ForceExit while in a message. Others are OK when the message is<br>done.<br>• Other mismatched uses (for example, IBI ACK NACK when in normal states).|
|18|Message Error|
|MSGERR||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2608 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Table continued from the previous page... 

|Field|Function<br>• Trying to write to or read from MWMSG_SDR register when in a DDR message.<br>• Trying to write to or read from MWMSG_DDR register when in a SDR message.<br>• Trying to read from HRMSG_SDR or HRMSG_DDR registers when no message has yet started.|
|---|---|
|17<br>OWRITE|Over-write Error<br>Trying to write to the Master Write Data Byte Register (MWDATAB) when the FIFO is full.|
|16<br>OREAD|Over-read Error<br>Trying to read from the Master Read Data Byte Register (MRDATAB) when the FIFO is empty.|
|15-13<br>—<br>12<br>—|Reserved<br>Reserved|
|11<br>—|Reserved|
|10<br>HCRC|High Data Rate CRC Error<br>A Cyclic Redundancy Check (CRC) error occurred from a DDR read.|
|9<br>HPAR|High Data Rate Parity<br>• Parity error from a DDR read, this includes a bad preamble on a read.<br>• Does not stop the read, because it is not safe to terminate (because the read data may get mis-<br>framed).<br>• Will end on a run of 1 second.|
|8-5<br>—|Reserved|
|4<br>—<br>3<br>WRABT|Reserved<br>Write Abort Error<br>• The I2C slave NACKED the write data, terminating the message.<br>• WRABT self-clears if the MCTRL register is written.<br>For example, the Master is writing in I2C and the Slave NACKED the write.|
|2|Not Acknowledge Error|
|NACK|• The slave or slaves NACKED (not acknowledged) the last address.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2609 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2610-03.png)


<!-- Start of picture text -->
Field Function<br>• If 7E was the address, then all slaves NACKED the last address.<br>• NACK self-clears if the MCTRL register is written.<br>  NOTE<br>If HDR, it would be "not accept" (vs. NACK).<br>1 Reserved<br>—<br>0 Reserved<br>—<br><!-- End of picture text -->

### 70.6.34 Master DMA Control (MDMACTRL) 

##### Offset 

|Register|Offset|
|---|---|
|MDMACTRL|A0h|



##### Function 

[DIP_I3C_00063]The DMA Control register allows for DMA to be used for inbound and outbound messages. DMA is much more useful for a Master than for a Slave, because the Master is directing the bus traffic and actions, so setting up DMA is more natural for a Master.[end] DMA can be used with a Master in following ways: 

- Push or Pull data to go with an MCTRL[REQUEST] = EMITSTARTADDR request written by the processor. 

- Implementing a message mode, to be completely DMA-controlled. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2610-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>DMAWIDTH  DMATB  DMAFB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2610 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Fields 

|Field|Function|
|---|---|
|31-8|Reserved|
|—<br>7-6<br>—|Reserved|
|5-4<br>DMAWIDTH|DMA Width<br>Specifies the data width of DMA operations.<br>00b,01b - BYTE<br>10b - HALF_WORD. Half-word (16 bits). This makes sure that 2 bytes are free/available in FIFO.<br>11b - Reserved|
|3-2<br>DMATB|DMA To Bus<br>DMA Write (to-bus) trigger. If enabled with DMATB = 1 or DMATB = 2, then the I3C module starts request<br>DMA on TX trigger. See the Master Data Control Register (MDATACTRL). The I3C module requests until<br>full, unless DMA is set up as a trigger.<br>DMAFB cancels on MSTATUS[ERRWARN].<br>00b - NOT_USED. DMA is not used<br>01b - ENABLE_ONE_FRAME. DMA is enabled for 1 frame (ended by DMA or Terminated).<br>DMATB auto-clears on STOP or START. See MCONFIG[MATCHSS].<br>10b - ENABLE. DMA is enabled until DMA is turned off. Normally DMA ENABLE should only be<br>used in Master Message mode.<br>11b - Reserved|
|1-0<br>DMAFB|DMA From Bus<br>DMA Read (from-bus) trigger. If enabled with DMAFB = 1 or DMAFB = 2, then the I3C module requests DMA<br>on an Rx trigger (see MDATACTL register). The I3C module requests until empty, unless the DMA is set up<br>as a trigger.<br>DMAFB cancels on MSTATUS[ERRWARN].<br>00b - NOT_USED. DMA is not used<br>01b - ENABLE_ONE_FRAME. DMA is enabled for 1 frame. DMAFB auto-clears on STOP or<br>repeated START. See MCONFIG[MATCHSS].<br>10b - ENABLE. DMA is enabled until the DMA is turned off.<br>11b - Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2611 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

### 70.6.35 Master Data Control (MDATACTRL) 

##### Offset 

|Register|Offset|
|---|---|
|MDATACTRL|ACh|



##### Function 

The Data Control register (alias of the Slave one) assists in data control when there is no FIFO, and assists FIFO when FIFO is available (regardless of size). This allows some control over the FIFO behavior. In particular, it allows control of when to interrupt on fullness/emptiness and also controls behavior related to width, when not 1 byte wide. 

~~<mark>NOTE</mark>~~ 

If flushing a FIFO when DMA is in use, disable the DMA channel first. 

~~<mark>NOTE</mark>~~ 

FIFO flush should not be used when a message (in that direction) is in flight. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2612-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>RXEM TXFUL<br>R 0 RXCOUNT  0 0 TXCOUNT<br>PTY  L<br>W<br>Reset 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>RXTRIG  TXTRIG<br>UNLO FLUS FLUS<br>W<br>CK  HFB  HTB<br>Reset 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Receive Is Empty.|
|RXEMPTY|0b - Rx is not yet empty.|
||1b - Rx is empty.|
|30|Transmit Is Full.|
|TXFULL|Default value is 1.|
||0b - Tx is not yet full.|
||1b - Tx is full.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2612 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|29<br>—|Reserved|
|28-24<br>RXCOUNT|Receive Byte Count<br>The count of bytes in Rx|
|23-22<br>—|Reserved|
|21<br>—|Reserved|
|20-16|Transmit Byte Count|
|TXCOUNT|The count of bytes waiting in the TXFIFO. This means the number of bytes that the application has<br>written to the TxFIFO and have not yet gone onto the I3C bus.|
|15-8<br>—<br>7-6<br>RXTRIG|Reserved<br>Receive Trigger Level<br>Trigger level for Rx fullness when using a FIFO. Affects interrupt and DMA (if enabled).<br>00b - Trigger on not empty<br>01b - Trigger on 1/4 full or more<br>10b - Trigger on 1/2 full or more<br>11b - Trigger on 3/4 full or more|
|5-4<br>TXTRIG|Transmit Trigger Level<br>Trigger level for TX emptiness when using a FIFO. Affects interrupt and DMA (if enabled). The default is<br>3.<br>00b - Trigger on empty<br>01b - Trigger on 1/4 full or less<br>10b - Trigger on 1/2 full or less<br>11b - Default. Trigger on 1 less than full or less|
|3<br>UNLOCK|Unlock<br>UNLOCK must be 1 in the same cycle while writing to TXTRIG or RXTRIG.<br>~~NOTE~~<br>0b - RXTRIG and TXTRIG fields cannot be changed on a write.<br>1b - RXTRIG and TXTRIG fields can be changed on a write.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2613 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|2|Reserved|
|—||
|1|Flush From-bus Buffer/FIFO|
|FLUSHFB|Flushes the from-bus buffer/FIFO. FLUSHFB is not normally used.|
|0|Flush To-bus Buffer/FIFO|
|FLUSHTB|Flush the to-bus buffer/FIFO. Used when the master terminates a to-bus message (read) prematurely.|



### 70.6.36 Master Write Data Byte (MWDATAB) 

##### Offset 

|Register|Offset|
|---|---|
|MWDATAB|B0h|



##### Function 

Write a byte of data, possibly the last byte. The MWDATAB register is the alias of the Slave Write Data Byte (SWDATAB). The MWDATAB register allows writing bytes to send onto the bus. This is only used when using Master Control (MCTRL) to start the message. If MWMSG_SDR or MWMSG_DDR is used to start a message, that interface must be used exclusively. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2614-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>END_<br>W<br>ALSO<br>Reset u u u u u u u u u u u u u u u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W END  VALUE<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

Fields 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2614-12.png)


<!-- Start of picture text -->
Field Function<br>31-17 Reserved<br>—<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2614 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|16|End of Message Also|
|END_ALSO|End outbound message normally. Any message has to end indicates that it is the last message to go out.<br>This method can be used and also the MDATABE register.<br>• If END_ALSO = 1, this marks the last byte of the message.<br>• If END_ALSO = 0, it is assumed there are more bytes.<br>This is required to be used in I3C and is optional in I2C. For HDR-DDR, the byte with the END_ALSO<br>must be an even byte (2nd, 4th, 6th，and so on) because DDR uses byte-pairs.|
|15-9<br>—|Reserved|
|8<br>END|End of Message<br>• If END = 1, then the END bit marks the last byte of the message.<br>• If END = 0, then it is assumed there are more bytes.<br>This is required to be used in I3C and is optional in I2C. For HDR-DDR, the byte with the END must be<br>an even byte (2nd, 4th, 6th, and so on) because DDR uses byte-pairs.|
|7-0<br>VALUE|Data Byte<br>The byte that is sent to (written to) the slave (stored in TX FIFO).<br>• If I3C, the block will compute the parity.<br>• If I2C, the block will handle the ACK/NACK.|



### 70.6.37 Master Write Data Byte End (MWDATABE) 

##### Offset 

|Register|Offset|
|---|---|
|MWDATABE|B4h|



##### Function 

The MWDATABE register is the alias of the Slave Write Data Byte End (SWDATABE). The MWDATABE register allows writing the last byte to send onto the bus. This is only used when using MCTRL to start the message. If MWMSG_SDR or MWMSG_DDR is used to start a message, that interface must be used exclusively. Note that MWDATAB can also indicate END using bit 8. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2615 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2616-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset u u u u u u u u u u u u u u u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W VALUE<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-8<br>—|Reserved|
|7-0|Data|
|VALUE|The last byte that is sent to (written to) the slave (stored in TX FIFO).|
||• If I3C, the block computes the parity.|
||• If I2C, the block handles the ACK/NACK.|



### 70.6.38 Master Write Data Half-word (MWDATAH) 

##### Offset 

|Register|Offset|
|---|---|
|MWDATAH|B8h|



##### Function 

Write a halfword of data, possibly the last half word. The MWDATAH register is the alias of the Slave Write Data Half-word (SWDATAH). This Master Write Data Half-word register allows writing a half word (pair of bytes) to the bus, unless an external FIFO is used. This takes a halfword, which will send out the Low byte and then the High byte. An end-of-data (last) marker bit is allowed (or must be 0). A halfword should not be written unless there is room for both, as indicated by use of Tx FIFO level trigger or TXCOUNT available space in the MDATACTRL register. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2616 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W||||||||||||||||END|
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||||||||||||||
|W||||DA|TA1|||||||DA|TA0||||
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|



##### Fields 

|Field|Function|
|---|---|
|31-17|Reserved|
|—||
|16|End of message|
|END|• If END = 1, then END bit marks the last byte of the message.<br>• If END = 0, then there are more bytes in the message.<br>For this register, this always marks DATA1 as the end. END is required to be used in I3C, but is optional<br>in I2C.<br>For HDR-DDR, the byte with the END must be an even byte (2nd, 4th, 6th，and so on.) because DDR<br>uses byte-pairs.|
|15-8|Data Byte 1|
|DATA1|The 2nd byte that is sent to the slave (written to TX FIFO).|
|7-0|Data Byte 0|
|DATA0|The 1st byte that is sent to the slave (written to TX FIFO).|



### 70.6.39 Master Write Data Byte End (MWDATAHE) 

##### Offset 

|Register|Offset|
|---|---|
|MWDATAHE|BCh|



##### Function 

Write the last halfword of data. The MWDATAHE register is the alias of the Slave Write Data Half-word End (SWDATAHE). Write a halfword (byte pair) just like the MWDATAH register, but mark the 2nd byte as end-of-data (last byte). Note that for HDR-DDR, the byte with the END must be an even (2nd, 4th, 6th，and so on) because DDR uses byte-pairs. A halfword 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2617 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

should not be written unless there is room for both half-words, as indicated by use of Tx FIFO level trigger or TXCOUNT available space in the MDATACTRL register. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2618-04.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset u u u u u u u u u u u u u u u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>W DATA1  DATA0<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16<br>—|Reserved|
|15-8|Data Byte 1|
|DATA1|The 2nd byte that is sent to the slave (written to TX FIFO).|
|7-0|ata Byte 0|
|DATA0|The 1st byte that is sent to the slave (written to TX FIFO).|



### 70.6.40 Master Read Data Byte (MRDATAB) 

##### Offset 

|Register|Offset|
|---|---|
|MRDATAB|C0h|



##### Function 

Read a byte of data. The MRDATAB register is the alias of the Slave RDATAB register (SRDATAB). The MRDATAB register is used to read bytes written by the Slave on an SDR Read or DAA or DDR. This is only used when using MCTRL to start the message. If MWMSG_SDR or MWMSG_DDR is used to start a message, that interface must be used exclusively. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2618 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2619-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 VALUE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-8<br>—|Reserved|
|7-0|Value|
|VALUE|The byte read from the master (and written by the Slave).|



### 70.6.41 Master Read Data Half-word (MRDATAH) 

##### Offset 

|Register|Offset|
|---|---|
|MRDATAH|C8h|



##### Function 

MRDATAH allows reading a Half-word (byte pair) written by the Slave on an SDR Read or DAA or DDR. This is only used when using MCTRL to start the message. If MWMSG_SDR or MWMSG_DDR is used to start a message, that interface must be used exclusively. 

A Half-word should not be read unless there is at least 2 bytes of data waiting, as indicated the Rx FIFO level trigger or RXCOUNT available space in the DATACTRL register. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2619 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2620-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R MSB  LSB<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16<br>—|Reserved|
|15-8|MSB|
|MSB|The 2nd byte read from the master (and written by the Slave).|
|7-0|LSB|
|LSB|The 1st byte read from the master (and written by the Slave).|



### 70.6.42 Byte-only Write Byte Data (to bus) (MWDATAB1) 

##### Offset 

|Register|Offset|
|---|---|
|MWDATAB1|CCh|



##### Function 

The MWDATAB1 register allows writing bytes to send onto the bus, and is intended for DMAs which do not clear the upper bits of the word – it does not have the END bits. This is only used when using MCTRL to start the message. If MWMSG_SDR or MWMSG_DDR is used to start a message, that interface must be used exclusively. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2620 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2621-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W VALUE<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-8|Reserved|
|—||
|7-0|Value|
|VALUE|Is byte to write out. The block will compute the parity if I3C, or handle the ACK/NACK if I2C.|



### 70.6.43 Master Write Message in SDR mode (MWMSG_SDR_CONTROL) 

##### Offset 

|Register|Offset|
|---|---|
|MWMSG_SDR_CONTR<br>OL|D0h|



##### Function 

Set up and write 16-bit words in Single Data Rate (SDR) mode. The MWMSG_SDR_ register is modal and has 2 modes: control and data. 

- On the first write to set up a new message, this register functions as the MWSMSG_SDR_CONTROL register. 

- On subsequent writes, this register functions as the MWMSG_SDR_DATA register. 

When not in the middle of a message, the MWMSG_SDR_CONTROL register is used to start a new message (or emit a STOP). After starting a message, the MWMSG_SDR_DATA register is used until the Length (see LEN field) counts down, or until data with END = 1 is used. 

The MWMSG_SDR_CONTROL register is written with the 16-bit Control word if currently stopped or past the end of the previous message. If MSTATUS[STATE] is MSGSDR and MSTAT[BETWEEN] = 0, then the register (at this offset address) is functioning as the MWMSG_SDR_DATA register. Otherwise, this register (at this offset address) is functioning as the MWMSG_SDR_CONTRL register, as long as MSTATUS[STATE] is not in another mode. The control word contains the byte length (6-bit), the address, the direction, and how it ends (stop, ready for next, continuation with more length). Note that if START and if an event (IBI, MR, HJ) occurs, the MCTRL register’s IBIRESP field will be used to determine action, and the corresponding interrupt will occur. The message will be restarted in that case. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2621 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

The MWMSG_SDR_CONTROL and MWMSG_SDR_DATA registers are oriented to DMA operations, but the MWMSG_SDR_CONTROL register can also be written by the processor (instead of using MCTRL and MxDATAB). 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2622-04.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset u u u u u u u u u u u u u u u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W LEN  I2C  END  ADDR  DIR<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16<br>—|Reserved|
|15-11|Length|
|LEN|The byte length of the message. If LEN = 0, then only END is used (and it will not use the address if<br>Stopped). LEN = 1 must not be used. The minimal LEN size is 2 bytes (LEN = 2).|
|10|I2C|
|I2C|Specifies if the message is I2C or I3C.<br>0b - I3C message<br>1b - I2C message|
|9<br>—|Reserved|
|8<br>END|End of SDR Message<br>• If END = 1, then the single data rate message ends on STOP.<br>• If END = 0, then the single data rate message ends waiting for a new SDR message (will issue a<br>repeated START for a new message).<br>Sets MSTATUS[COMPLETE] when done. This can happen before LEN bytes are read in I3C if a slave<br>ends sooner or before LEN bytes are written in I2C if a slave NACKs.|
|7-1|Address|
|ADDR|Address to be written.|
|0|Direction|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2622 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|DIR|0b - Write|
||1b - Read|



### 70.6.44 Master Write Message Data in SDR mode (MWMSG_SDR_DATA) 

##### Offset 

|Register|Offset|
|---|---|
|MWMSG_SDR_DATA|D0h|



##### Function 

This is the 16-bit word to be written in Single Data Rate (SDR) mode. This register also functions as the MWMSG_SDR_CONTROL register. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2623-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>W DATA16B<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-17<br>—|Reserved|
|16<br>—|Reserved|
|15-0|Data|
|DATA16B||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2623 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

### 70.6.45 Master Read Message in SDR mode (MRMSG_SDR) 

##### Offset 

|Register|Offset|
|---|---|
|MRMSG_SDR|D4h|



##### Function 

Read 16-bit words from a slave in Single Data Rate (SDR) message mode. The MRMSG_SDR register is used to read 16-bit words from an active message started with MWMSG_SDR. These words are intended to be read by DMA. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2624-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DATA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16|Reserved|
|—||
|15-0|Data|
|DATA|DATA is the 16-bit word read from the slave.|
||• If the length (LEN) was an uneven number, then the upper byte is 0.<br>• If the slave ends before LEN is finished, then it treats the read as completed.<br>• If the slave is not done before LEN is finished and END is not a continuation, then the read is<br>terminated.|



### 70.6.46 Master Write Message in DDR mode (MWMSG_DDR_CONTROL) 

##### Offset 

|Register|Offset|
|---|---|
|MWMSG_DDR_CONTR|D8h|
|OL||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2624 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Function 

Set up and write 16-bit words in Double Data Rate (DDR) mode. The MWMSG_DDR_ register is modal and has 2 modes: control and data. 

- On the first write to set up a new message, this register functions as the MWSMSG_DDR_CONTROL register. 

- On subsequent writes, this register functions as the MWMSG_DDR_DATA register. 

When not in the middle of a message, the MWMSG_DDR_CONTROL register is used to start a new message (or emit a STOP). After starting a message, the MWMSG_DDR_DATA register is used until the Length (see LEN field) counts down or until data with END=1 is used. 

The MWMSG_DDR_CONTROL register is written with the 16-bit Control word if currently stopped or past the end of the previous message. If MSTATUS.STATE is MSGDDR and MSTAT[BETWEEN] = 0, then the register (at this offset address) is functioning as the MWMSG_DDR_DATA register. Otherwise, this register (at this offset address) is functioning as the MWMSG_DDR_CONTRL register, as long as MSTATUS[STATE] is not in another mode. The main control word contains the 16-bit word length and how it ends (stop, ready for next, continuation with more length). Then the 1st data word has the command and address for read or write. Note that if START and if an event (IBI, MR, HJ) occurs, then the MCTRL register’s IBIRESP field will be used to determine action, and the corresponding interrupt will occur. The message will be restarted in that case. Note that the module handles preamble, parity, and CRC. 

The MWMSG_DDR_CONTROL and MWMSG_DDR_DATA registers are oriented to DMA operations, but the MWMSG_DDR_CONTROL register can also be written by the processor (instead of using MCTRL and MxDATAB). 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|0||||0||||||||||||
|W||END|||||||||LE|N|||||
|Reset|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|



##### Fields 

|Field|Function|
|---|---|
|31-16|Reserved|
|—||
|15|Reserved|
|—||
|14|End of message|
|END|• If END = 1, then the double data rate message ends on HDR Exit.|
||• If END = 0, then the double data rate message ends waiting for a new DDR message (will issue a<br>HDR Restart for the new message).|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2625 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||Sets MSTATUS[COMPLETE] when done. This can happen before LEN bytes are read if the slave ends<br>sooner.|
|13-10|Reserved|
|—||
|9-0|Length of Message|
|LEN|The length of the message (including the command) in half-words, so up to 2046 bytes. If LEN = 0, then END<br>is applied only.|
||• For Read, +1 for the CRC. For example, to read 4 bytes, use 1 + 2 + 1 for CMD + 2 halves + CRC.|
||• For Write, LEN = 1 for command + number of halves of data byte.|



### 70.6.47 Master Write Message Data in DDR mode (MWMSG_DDR_DATA) 

##### Offset 

|Register|Offset|
|---|---|
|MWMSG_DDR_DATA|D8h|



##### Function 

This is the 16-bit word to be written in Double Data Rate (DDR) mode. This register also functions as the MWMSG_DDR_CONTROL register. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0||||||||0|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||||||||||||||
|W||||||||DAT|A16B||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function||
|---|---|---|
|31-17|Reserved||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2626 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2627-03.png)


<!-- Start of picture text -->
Field Function<br>—<br>16 Reserved<br>—<br>15-0 Data<br>DATA16B<br><!-- End of picture text -->

### 70.6.48 Master Read Message in DDR mode (MRMSG_DDR) 

##### Offset 

|Register|Offset|
|---|---|
|MRMSG_DDR|DCh|



##### Function 

Read 16-bit words from a slave in Double Data Rate (DDR) message mode. The MRMSG_DDR register is used to read 16-bit words from an active message started with MWMSG_DDR. This is intended to be read by DMA. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2627-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DATA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16<br>—|Reserved|
|15-0|Data|
|DATA||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2627 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||DATA is the 16-bit word read from a slave. The 1st byte is the LSB and the 2nd byte is the MSB. The 1st<br>byte is in DATA[7:0] and the 2nd byte is in DATA[15:8].|
||• If the slave ends before the entire length of the message (MWMSG_DDR[LEN]) is read, then<br>the module will consider the DATA read as completed. In I3C, the slave can indicate the end of<br>message (the last byte). Otherwise, the master would terminate the message if the message is more<br>than the master will accept.|
||• If the slave has not yet finished sending DATA before the entire length of the message<br>(MWMSG_DDR[LEN]) is read and END is not a continuation, then the DATA read will be terminated.|



### 70.6.49 Master Dynamic Address (MDYNADDR) 

##### Offset 

|Register|Offset|
|---|---|
|MDYNADDR|E4h|



##### Function 

Allows an I3C module to write its own Dynamic Address when the I3C module changes from master mode to slave mode. 

If this device is the Main Master (the Master at bus initialization), then this device may use this mechanism to assign itself its Dynamic Address. When the device hands off control to a secondary Master, it becomes a Slave itself. This must be written before switching to Slave mode and must not be changed once in Slave mode (it is not clock safe for that). It must be written with a valid address value in DADDR if DAVALID = 1. Note that the Main master also uses DEFSLVS to define the slave addresses, including itself; this is how secondary Masters know this address. If the Master is not the Main Master, then this should not be used. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||0|||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||0||||||||DADDR||||DAVAL<br>ID|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field<br>Function|
|---|
|31-8<br>Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2628 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Table continued from the previous page... 

|Field<br>—|Function|
|---|---|
|7-1|Dynamic address|
|DADDR|The assigned Dynamic Address when DAVALID = 1.|
|0|Dynamic address valid|
|DAVALID|DAVALID = 1 if a Dynamic Address is assigned.|



### 70.6.50 CCC Mask for Unhandled CCCs (SCCCMASK) 

##### Offset 

|Register|Offset|
|---|---|
|SCCCMASK|10Ch|



##### Function 

CCCMASK allows masking on or off Unhandled CCCs when enabled. Unhandled means not handled by hardware. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/070_Improved_Inter-Integrated_Circuit_-I3C-/S32K3XXRM_数据表.pdf-2629-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 VEND VEND MEXT MEXT BASE BASE<br>BASE<br>D  B  D  B  DX  BX<br>W<br>Reset 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-7|Reserved|
|—||
|6|VENDD|
|VENDD|If 1, any unhandled CCC in range 0xE4 to 0xFF are passed to app, else they are suppressed.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2629 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Unhandled CCC in given range suppressed<br>1b - Unhandled CCC in given range passed to application|
|5<br>VENDB|VENDB<br>If 1, any unhandled CCC in range 0x65 to 0x7F are passed to app, else they are suppressed.<br>0b - Unhandled CCC in given range suppressed<br>1b - Unhandled CCC in given range passed to application|
|4|MEXTD|
|MEXTD|If 1, any unhandled CCC in range 0xC0 to 0xE3 are passed to app, else they are suppressed.<br>0b - Unhandled CCC in given range suppressed<br>1b - Unhandled CCC in given range passed to application|
|3<br>MEXTB|MEXTB<br>If 1, any unhandled CCC in range 0x49 to 0x64 are passed to app, else they are suppressed.<br>0b - Unhandled CCC in given range suppressed<br>1b - Unhandled CCC in given range passed to application|
|2|BASEDX|
|BASEDX|If 1, any unhandled CCC in range 0xA0 to 0xBF are passed to app, else they are suppressed.<br>0b - Unhandled CCC in given range suppressed|
||1b - Unhandled CCC in given range passed to application|
|1|BASEBX|
|BASEBX|If 1, any unhandled CCC in the range of 0x20 to 0x48 are passed to app, else they are suppressed.<br>0b - Unhandled CCC in given range suppressed<br>1b - Unhandled CCC in given range passed to application|
|0|Base|
|BASE|If 1, any unhandled CCC in the range of 0 to 0x1F and 0x80 to 0x8F are passed to application, else they<br>are suppressed.<br>0b - Unhandled CCC in given range suppressed<br>1b - Unhandled CCC in given range passed to application|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2630 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

### 70.6.51 Slave Errors and Warnings Mask (SERRWARNMASK) 

##### Offset 

|Register|Offset|
|---|---|
|SERRWARNMASK|110h|



##### Function 

The Slave Errors and Warnings (SERRWARN) contains I3C protocol errors and issues detected on the line. If any are set, they set the SSTATUS[ERRWARN] bit (and interrupt if enabled). SERRWARNMASK allows masking them off so only some form the status bit. 

##### Diagram 

|Bits|31||30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||||||||0|||||||||
|Reset|0||0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15||14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||0||0||S0S1|HCRC|HPAR|SPAR||0||INVST<br>ART|TERM|URUN<br>NACK|URUN|ORUN|
|Reset|0||0|0|0|1|1|1|1|0|0|0|1|1|1|1|1|



##### Fields 

|Field|Function|
|---|---|
|31-14<br>—|Reserved|
|13-12<br>—|Reserved|
|11|S0S1 mask|
|S0S1|If 1, allows this ERRWARN bit to contribute. Reset to 1.|
|10|HCRC mask|
|HCRC|If 1, allows this ERRWARN bit to contribute. Reset to 1.|
|9|HPAR mask|
|HPAR|If 1, allows this ERRWARN bit to contribute. Reset to 1.|
|8|SPAR mask|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2631 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|SPAR|If 1, allows this ERRWARN bit to contribute. Reset to 1.|
|7-5<br>—|Reserved|
|4|INVSTART mask|
|INVSTART|If 1, allows this SERRWARN bit to contribute. Reset to 1.|
|3|TERM mask|
|TERM|If 1, allows this SERRWARN bit to contribute. Reset to 1.|
|2|URUNNACK mask|
|URUNNACK|If 1, allows this SERRWARN bit to contribute. Reset to 1.|
|1|URUN mask|
|URUN|If 1, allows this SERRWARN bit to contribute. Reset to 1.|
|0|ORUN mask|
|ORUN|If 1, allows this SERRWARN bit to contribute. Reset to 1.|



### 70.6.52 Map Feature Control 0 (SMAPCTRL0) 

##### Offset 

|Register|Offset|
|---|---|
|SMAPCTRL0|11Ch|



##### Function 

The MAPCTRLn registers are named MAPCTRL0, MAPCTRL1，and so on based on number of mapped addresses. MAPCTRL0 represents the Primary DA/SA with MAPCTRL1 onwards being the Mapped addresses. 

The features of the SMAPCTRLn registers depend on configurations. The MAPCTRL0 acts differently, as shown below. 

In general, this mechanism is intended to replace the DYNADDR register for all MAP related uses. 

Note that when using the Auto-MAP and DASA or AASA, the slot is changed from SA to DA. If the Master then issues RSTDAA, the application would need to rewrite the static addresses and enable them, as they will be marked disabled. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2632 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0||||||||0|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||0||||CAUSE|||||DA||||ENA|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-17<br>—|Reserved|
|16<br>—|Reserved|
|15-11<br>—<br>10-8|Reserved<br>Cause|
|CAUSE|The DA is last assigned and used with theSSTATUS[DACHG]bit/interrupt:<br>• 0 = No information. Is 0 if not configured to write DA.<br>• 1 = Set using ENTDAA<br>• 2 = Set using SETDASA or SETAASA or SETNEWDA<br>• 3 = Cleared using RSTDAA<br>• 4 = Auto MAP change happened last. This may have changed this DA as well (for example,<br>ENTDAA, and SETAASA), but at least one MAP entry auto changed after.<br>With MAP enabled.|
|7-1<br>DA|Dynamic Address<br>Primary Dynamic address if ENA = 1. Note that if ENA = 0, then static address would be used (but not<br>shown here).<br>With MAP enabled.|
|0|Enable|
|ENA|Is 1 if Primary Dynamic Address is enabled.<br>With MAP enabled.|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2633 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

### 70.6.53 Map Feature Control 1 (SMAPCTRL1) 

##### Offset 

|Register|Offset|
|---|---|
|SMAPCTRL1|120h|



##### Function 

The MAPCTRLn registers are named MAPCTRL0, MAPCTRL1，and so on based on number of mapped addresses. MAPCTRL0 represents the Primary DA/SA, with MAPCTRL1 onwards being the Mapped addresses. 

The features of the SMAPCTRLn registers depend on configurations. Note that MAPCTRL0 acts somewhat differently, as shown below. 

In general, this mechanism is intended to replace the DYNADDR register for all MAP related uses. 

Note that when using the Auto-MAP and DASA or AASA, the slot is changed from Static address to Dynamic address. If the Master then issues RSTDAA, the application would need to rewrite the static addresses and enable them, as they will be marked disabled. 

##### Diagram 

|Bits|31||30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||0||||||||0|||||
|W||||||||||||||||||
|Reset|0||0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15||14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||0||0|NACK||SA10B||MAPS<br>A||||ADDR||||ENA|
|Reset|0||0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-24<br>—|Reserved|
|23-14<br>—|Reserved|
|13<br>—|Reserved|
|12|No Acknowledge|
|NACK|If 1, messages to this address will be NACKED every time.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2634 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||If Enabled.|
|11-9|Static Address 10-bit Extension|
|SA10B|If MAPCTRL1, this is SA10B for 10-bit extended address. Is 0, if normal address, else is 10-bit extension.<br>If enabled for 10-bit.|
|8|MAP Static Address|
|MAPSA|IF ENA = 1, is 1 if Static Address (I2C style), else is I3C Dynamic Address.<br>With MAP enabled<br>0b - I3C Dynamic Address<br>1b - Static Address (I2C style)|
|7-1|Address|
|ADDR|If ENA = 1, is Static or Dynamic Address. See MAPSA to see which one.<br>With MAP enabled|
|0|Enable|
|ENA|Is 1 if MAP entry is enabled. This could be a static or dynamic address.<br>With MAP enabled|



### 70.6.54 Extended IBI Data 1 (IBIEXT1) 

##### Offset 

|Register|Offset|
|---|---|
|IBIEXT1|140h|



##### Function 

The CTRL register is used to submit IBI, MR, and HotJoin when enabled for It. If allowed, the IBI may have more bytes following the Mandatory Data byte (MDB). This is indicated by setting the CTRL[EXTDATA] bit. If set, the extra bytes are indicated using these 2 registers. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2635 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Diagram 

|Bits|31|30<br>29<br>28|27|26|25|24|23|22|21|20|19|18<br>17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||EX|T3|||||||EX|T2|||
|Reset|0|0<br>0<br>0|0|0|0|0|0|0|0|0|0|0<br>0|0|
|Bits|15|14<br>13<br>12|11|10|9|8|7|6|5|4|3|2<br>1|0|
|R||EX|T1||||0||MAX||0|CNT||
|W||||||||||||||
|Reset|0|0<br>0<br>0|0|0|0|0|0|1|1|1|0|0<br>0|0|
|Fields<br>|Field|Function||||||||||||
||31-24|Extra byte 3||||||||||||
||EXT3|3rd extra byte||||||||||||
||23-16|Extra byte 2||||||||||||
||EXT2|2nd extra byte||||||||||||
||15-8|Extra byte 1||||||||||||
||EXT1|1st extra byte||||||||||||
||7<br>—<br>6-4<br>MAX|Reserved<br>Maximum<br>Indicates the maxi|mum n|umber o|f extra|bytes al|lowed b|y configu|ration|or 0 if|none.|||
||3<br>—|Reserved||||||||||||
||2-0<br>CNT|Count<br>The number of ext|ra byte|s past th|e MDB|to be u|sed or|0 if none.||||||



##### Fields 

### 70.6.55 Extended IBI Data 2 (IBIEXT2) 

##### Offset 

|Register|Offset|
|---|---|
|IBIEXT2|144h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2636 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

##### Function 

The CTRL register is used to submit IBI, MR, and HotJoin, when enabled for It. If allowed, the IBI may have more bytes following the Mandatory Data byte (MDB). This is indicated by setting the CTRL[EXTDATA] bit. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||EX|T7|||||||EX|T6||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||EX|T5|||||||EX|T4||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-24|Extra byte 7|
|EXT7|7th extra byte|
|23-16|Extra byte 6|
|EXT6|6th extra byte|
|15-8|Extra byte 5|
|EXT5|5th extra byte|
|7-0|Extra byte 4|
|EXT4|4th extra byte|



## 70.7 Glossary 

|CCC|Common Command Codes|
|---|---|
|CDC|Clock-domain-crossing|
|CRC|Cyclic Redundancy Check|
|DDR|Double Data Rate|
|FM|Fast Mode|
|FM+|Fast Mode Plus|
|HDR|High Data Rate|
|HDR-BT|HDR Bulk Transfer|
|HDR-DDR|High Data Rate - Double Data Rate|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2637 / 4640 

NXP Semiconductors 

Improved Inter-Integrated Circuit (I3C) 

HJ Hot Join IBI In-Band interrupt IRQ Interrupt MR Master Request PIO Programmable I/O SDR Single Data Rate 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2638 / 4640 

