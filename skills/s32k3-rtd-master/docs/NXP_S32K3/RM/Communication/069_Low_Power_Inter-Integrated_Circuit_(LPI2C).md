NXP Semiconductors 

# Chapter 69 Low Power Inter-Integrated Circuit (LPI2C) 

## 69.1 Chip-specific LPI2C information 

### 69.1.1 LPI2C instances and configuration 

This chip has two instances of LPI2C. 

Table 392. LPI2C instances 

|Instance|S32K311/S32K312/S32K322/S32K342/S32K314/S32K324/S32K344/S32K358|
|---|---|
|LPI2C_0|Yes|
|LPI2C_1|Yes|



Table 393. LPI2C configuration 

|Instances|TX FIFO Size|RX FIFO Size|SMBus<sup>1</sup>|Slave Mode Enable|
|---|---|---|---|---|
|LPI2C_0|4x11 bit|4x8 bit|Yes|Yes|
|LPI2C_1|4x11 bit|4x8 bit|Yes|Yes|



1. System Management Bus 

- LPI2C slave mode operation supports up to high speed mode = 3.4MHz (3.4 Mbps data rate; effective data rate reduces according to I2C protocol). 

- LPI2C master mode operation supports up to fast Mode = 400KHz (400 kbps data rate; effective data rate reduces according to I2C protocol). 

- The LPI2C module includes SMBus (System Management Bus) support and DMA support. 

- LPI2C RX FIFO is 8-bit and TX FIFO is 11-bit (8bit data + 3bit command) 

- LPI2C supports fast data communication as per I2C standard v3.0. 

## 69.2 Overview 

The LPI2C is a low power Inter-Integrated Circuit (I2C) module that supports an efficient interface to an I<sup>2</sup> C bus as a master and/or as a slave. 

- Implements logic support for standard-mode, fast-mode, fast-mode plus and ultra-fast modes of operation. 

- Uses little CPU overhead, with DMA offloading of FIFO register accesses. 

The LPI2C module also complies with the System Management Bus (SMBus) Specification, version 3. The SMBus is a single-ended simple two-wire bus, which is typically used for low bandwidth communications. 

~~<mark>NOTE</mark>~~ 

The I<sup>2</sup> C (Inter-Integrated Circuit) serial bus is multi-master, multi-slave, packet-switched, and single-ended, and is often used to attach microcontroller ICs to lower-speed peripheral ICs. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2471 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

### 69.2.1 Block diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/069_Low_Power_Inter-Integrated_Circuit_-LPI2C-/S32K3XXRM_数据表.pdf-2472-03.png)


<!-- Start of picture text -->
LPI2C<br>Trigger<br>Prescaler<br>Internal SoC HREQ<br>Peripheral<br>Bus<br>Command /<br>TX FIFO  Glitch SDA<br>Master<br>Filter<br>Logic<br>RX FIFO  SCL<br>Configuration<br>Registers<br>Master<br>Slave<br>TX<br>Data<br>SDAS<br>Slave Glitch<br>RX Data / Logic Filter<br>Address<br>SCLS<br>Configuration<br>Registers<br>Bus Clock External Clock Functional Clock<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/069_Low_Power_Inter-Integrated_Circuit_-LPI2C-/S32K3XXRM_数据表.pdf-2472-04.png)


<!-- Start of picture text -->
Clock Domains<br><!-- End of picture text -->

Figure 364. LPI2C block diagram 

### 69.2.2 Features 

The LPI2C supports: 

- Standard, Fast, Fast+ and Ultra Fast modes 

- High speed mode (HS) in slave mode 

- Multi-master support, including synchronization and arbitration. Multi-master means any number of master nodes can be present. Additionally, master and slave roles may be changed between messages (after a STOP is sent). 

- Clock stretching: Sometimes multiple I2C nodes may be driving the lines at the same time. If any I2C node is driving a line low, then that line will be low. I2C nodes that are starting to transmit a logical one (by letting the line float high) can detect that the line is low, and thereby know that another I2C node is active at the same time. 

   - When node detection is used on the SCL line, it is called clock stretching, and clock stretching is used as a I2C flow control mechanism. 

   - When node detection is used on the SDA line, it is called arbitration, and arbitration ensures that there is only one I2C node transmitter at a time. 

- General call, 7-bit and 10-bit addressing 

- Software reset, START byte and Device ID (also require software support) 

The LPI2C master supports: 

- Command/transmit FIFO of 4 words (8-bit transmit data + 3-bit command). 

- Receive FIFO of 4 words (8-bit receive data). 

- Command FIFO will wait for idle I2C bus before initiating transfer 

- Command FIFO can initiate (repeated) START and STOP conditions and one or more master-receiver transfers 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2472 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

- STOP condition can be generated from command FIFO, or generated automatically when the transmit FIFO is empty 

- Host request input to control the start time of an I2C bus transfer 

- Flexible receive data match can generate interrupt on data match and/or discard unwanted data 

- Flag and optional interrupt to signal Repeated START condition, STOP condition, loss of arbitration, unexpected NACK, and command word errors 

- Supports configurable bus idle timeout and pin-stuck-low timeout 

The LPI2C slave supports: 

- Separate I2C slave registers to minimize software overhead because of master/slave switching 

- Support for 7-bit or 10-bit addressing, address range, SMBus alert and general call address 

- Transmit data register that supports interrupt or DMA requests 

- Receive data register that supports interrupt or DMA requests 

- Software-controllable ACK or NACK, with optional clock stretching on ACK/NACK bit 

- Configurable clock stretching, to avoid transmit FIFO underrun and receive FIFO overrun errors 

- Flag and optional interrupt at end of packet, STOP condition, or bit error detection 

## 69.3 Functional description 

### 69.3.1 Master Mode 

The LPI2C master logic operates independently from the slave logic to perform all master mode transfers on the I2C bus. 

##### Transmit and Command FIFO commands 

The transmit FIFO stores command data to initiate the various I2C operations. The following operations can be initiated through commands in the transmit FIFO: 

- START or Repeated START condition with address byte and expecting ACK or NACK. 

- Transmit data (this is the default for zero extended byte writes to the transmit FIFO). 

- Receive 1-256 bytes of data (can also be configured to discard receive data and not store in receive FIFO). 

- STOP condition (can also be configured to send STOP condition when transmit FIFO is empty). 

Multiple transmit and receive commands can be inserted between the START condition and STOP condition; transmit and receive commands must not be interleaved (to comply with the I2C specification). The receive data command and the receive data and discard commands can be interleaved, to ensure that only the desired received data is stored in the receive FIFO (or compared with the data match logic). 

The LPI2C master automatically transmits a NACK on the last byte of a receive data command unless the next command in the FIFO is also a receive data command. A NACK is also automatically transmitted if the transmit FIFO is empty when a receive data command completes. 

The LPI2C master supports 10-bit addressing through a (repeated) START condition, followed by a transmit data byte containing the second address byte, followed by any number of data bytes with the master-transmit data. 

A START or Repeated START condition that is expecting a NACK (for example,HS-mode master code) must be followed by a STOP or (repeated) START condition. 

##### Master operations 

Whenever the LPI2C is enabled, it monitors the I2C bus to detect when the I2C bus is idle (MSR[BBF]). The I2C bus is no longer considered idle if either SCL or SDA are low, and the I2C bus becomes idle if a STOP condition is detected or if a bus idle timeout 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2473 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

is detected (as configured by MCFGR2[BUSIDLE]). After the I2C bus is idle, if the transmit FIFO is not empty, and the host request is either asserted or disabled, then the LPI2C master initiates a transfer on the I2C bus. This involves the following steps: 

- Wait the bus idle time equal to (MCCR0[CLKLO] + 1) multiplied by the prescaler (MCFGR1[PRESCALE]). 

- Transmit a START condition and address byte using the timing configuration in Master Clock Configuration 0 (MCCR0); if a high speed mode transfer is configured, then the timing configuration from Master Clock Configuration 1 (MCCR1) is used instead. 

- Perform master-transmit or master-receive transfers, as configured by the transmit FIFO. 

- Transmit NACK on the last byte of a master-receive transfer, unless the next command in the transmit FIFO is also a receive data command and the transmit FIFO is not empty. 

- Transmit a Repeated START or STOP condition as configured by the transmit FIFO and/or MCFGR1[AUTOSTOP]. A repeated START can change which timing configuration register is used. 

When the LPI2C master is disabled (either due to MCR[MEN] being clear or automatically due to mode entry), the LPI2C continues to empty the transmit FIFO until a STOP condition is transmitted. However, the LPI2C will no longer stall the I2C bus waiting for the transmit or receive FIFO, and after the transmit FIFO is empty, the LPI2C generates a STOP condition automatically. 

The LPI2C master can stall the I2C bus under certain conditions; this results in SCL pulled low continuously on the first bit of a byte, until the following conditions are removed: 

- LPI2C master is enabled and busy, the transmit FIFO is empty, and MCFGR1[AUTOSTOP] is clear. The LPI2C master will continue to stall the bus until the transmit FIFO is loaded with more data. 

- LPI2C master is enabled and receiving data, receive data is not being discarded (due to command or receive data match), and the receive FIFO is full. The LPI2C master will continue to stall the I2C bus until the receive FIFO is emptied. 

##### Receive FIFO and Data Matching 

The receive FIFO is used to store receive data during master-receiver transfers. LPI2C master can also be configured to discard receive data instead of storing in the receive FIFO; this is configured by the command word in the transmit FIFO. 

Receive data supports a receive data match function that can match received data against one of two bytes or against a masked data byte. The data match function can also be configured to compare only the first one or two received data words since the last (repeated) START condition. Receive data that is already discarded due to the command word cannot cause the data match to set, and delays the match on the first received data word until after the discarded data is received. The receiver match function can also be configured to discard all receive data until a data match is detected, using the MCFGR0[RDMO] control bit. When clearing the MCFGR0[RDMO] control bit following a data match, clear MCFGR0[RDMO] before clearing MSR[DMF], to allow all subsequent data to be received. 

##### Timing Parameters 

The following timing parameters can be configured by the LPI2C master. Parameters are configured separately for high speed mode (Master Clock Configuration 1 (MCCR1)) and other modes (Master Clock Configuration 0 (MCCR0)). This allows the high speed mode master code to be sent using the regular timing parameters, and then switch to the high speed mode timing (following a repeated START) until the next STOP condition. 

The LPI2C master timing parameters in LPI2C functional clock cycles are configured as follows. They must be configured to meet the I2C timing specification for the required mode. 

Table 394. Timing Parameters 

|I2C Specification Timing Parameter<br>SCL clock period|I2C Specification<br>Timing Symbol<br>tSCL|LPI2C Timing Parameter (LPI2C functional<br>clock cycles)<br>(CLKHI + CLKLO + 2 + SCL_LATENCY) x (2<br>^ PRESCALE)|
|---|---|---|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2474 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

Table 394. Timing Parameters (continued) 

|I2C Specification Timing Parameter|I2C Specification<br>Timing Symbol|LPI2C Timing Parameter (LPI2C functional<br>clock cycles)|
|---|---|---|
|hold time (repeated) START condition|tHD:STA|(SETHOLD +1) x (2 ^ PRESCALE)|
|LOW period of the SCL clock|tLOW|(CLKLO + 1) x (2 ^ PRESCALE)|
|HIGH period of the SCL clock|tHIGH|(CLKHI + 1 + SCL_LATENCY) x (2 ^ PRESCALE)|
|setup time for a repeated START<br>condition or STOP condition|tSU:STA, tSU:STO|(SETHOLD + 1 + SCL_LATENCY) x (2<br>^ PRESCALE)|
|data hold time|tHD:DAT|(DATAVD + 1) x (2 ^ PRESCALE)|
|data setup time|tSU:DAT|(SDA_LATENCY + 1) x (2 ^ PRESCALE)|
|bus free time between a STOP and<br>START condition|tBUF|(CLKLO + 1 + SDA_LATENCY) x (2 ^ PRESCALE)|
|data valid time, data valid<br>acknowledge time|tVD:DAT, tVD:ACK|(DATAVD + 1) x (2 ^ PRESCALE)|



The latency parameters are defined in the following table, these parameters assume the risetime is less than one LPI2C functional clock cycle. The risetime depends on a number of factors, including the I/O propagation delay, the I2C bus loading and the external pull-up resistor sizing. A larger rise time increases the number of cycles that the signal takes to propagate through the synchronizer (and glitch filter), which increases the latency. 

Table 395. Synchronization Latency 

|Timing Parameter|Timing Definition|
|---|---|
|SCL_LATENCY|ROUNDDOWN ( (2 + FILTSCL + SCL_RISETIME) / (2 ^ PRESCALE) )|
|SDA_LATENCY|ROUNDDOWN ( (2 + FILTSDA + SDA_RISETIME) / (2 ^ PRESCALE) )|



The following timing restrictions must be enforced to avoid unexpected START or STOP conditions on the I2C bus, or to avoid unexpected START or STOP conditions detected by the LPI2C master. The timing restrictions can be summarized as SDA cannot change when SCL is high outside of a transmitted (repeated) START or STOP condition . 

Table 396. LPI2C Timing Parameter Restrictions 

|Timing Parameter|Minimum|Maximum|Comment|
|---|---|---|---|
|CLKLO|0x03|-|Also: CLKLO x (2 ^ PRESCALE) ><br>SCL_LATENCY|
|CLKHI|0x01|-|Configure CLKHI to meet the duty cycle<br>requirements in the I2C specification|
|SETHOLD|0x02|-|Also: SETHOLD x (2 ^ PRESCALE) ><br>SDA_LATENCY|
|DATAVD|0x01|CLKLO - SDA_LATENCY<br>- 1|Configure DATAVD to meet the data<br>hold requirement in the I2C specification|
|FILTSCL|0x00|[CLKLO x (2 ^<br>PRESCALE)] - 3|FILTSCL and FILTSDA are the only<br>parameters not multiplied by (2 ^<br>PRESCALE)|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2475 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

Table 396. LPI2C Timing Parameter Restrictions (continued) 

|Timing Parameter|Minimum|Maximum|Comment|
|---|---|---|---|
|FILTSDA|FILTSCL|[CLKLO x (2 ^<br>PRESCALE)] - 3|Configuring FILTSDA greater than<br>FILTSCL can delay the SDA input to<br>compensate for board level skew|
|BUSIDLE|(CLKLO+SETHOLD+2) x<br>2|-|Must also be greater than (CLKHI+1)|



The timing parameters must be configured to meet the requirements of the I2C specification; this depends on the mode being supported and the LPI2C functional clock frequency. When switching between two modes using the different clock configuration registers (for example, Fast and HS-mode), the PRESCALE factor must remain constant between the modes. Some example timing configurations are provided below. 

Table 397. LPI2C Example Timing Configurations 

|I2C Mode|Clock<br>Frequency|Baud Rate|PRESCALE|FILTSCL /<br>FILTSDA|SETHOLD|CLKLO|CLKHI|DATAVD|
|---|---|---|---|---|---|---|---|---|
|Fast|8 MHz|400 kbps|0x0|0x0/0x0|0x04|0x0B|0x05|0x02|
|Fast+|8 MHz|1 Mbps|0x0|0x0/0x0|0x02|0x03|0x01|0x01|
|Fast|48 MHz|400 kbps|0x0|0x1/0x1|0x1D|0x3E|0x35|0x0F|
|Fast|48 MHz|400 kbps|0x2|0x1/0x1|0x07|0x11|0x0B|0x03|
|Fast+|48 MHz|1 Mbps|0x2|0x1/0x1|0x03|0x06|0x04|0x04|
|HS-mode|48 MHz|3.2 Mbps|0x0|0x0/0x0|0x07|0x08|0x03|0x01|
|Fast|60 MHz|400 kbps|0x1|0x2/0x2|0x11|0x28|0x1F|0x08|
|Fast+|60 MHz|1 Mbps|0x1|0x2/0x2|0x07|0x0F|0x0B|0x01|
|HS-mode|60 MHz|3.33 Mbps|0x1|0x0/0x0|0x04|0x04|0x02|0x01|



##### Error Conditions 

The LPI2C master monitors for errors while it is active. The following conditions generate an error flag and block a new START condition from being sent, until the flag is cleared by software: 

- A START or STOP condition is detected and is not generated by the LPI2C master (sets MSR[ALF]). 

- Transmitting data on SDA and different values are being received (sets MSR[ALF]). 

- NACK is detected when transmitting data, and MCFGR1[IGNACK] is clear (sets MSR[NDF]). 

- NACK is detected and is expecting ACK for the address byte, and MCFGR1[IGNACK] is clear (sets MSR[NDF]). 

- ACK is detected and is expecting NACK for the address byte, and MCFGR1[IGNACK] is clear (sets MSR[NDF]). 

- Transmit FIFO is requesting to transmit or receive data without a START condition (sets MSR[FEF]). 

- SCL (or SDA if MCFGR1[TIMECFG] is set) is low for (MCFGR2[TIMELOW] * 256) prescaler cycles without a pin transition (sets MSR[PLTF]). 

Software must respond to the MSR[PLTF] flag to terminate the existing command either cleanly (by clearing MCR[MEN]), or abruptly (by setting MCR[RST]). 

The MCFGR2[BUSIDLE] field can be used to force the I2C bus to be considered idle when SCL and SDA remain high for (BUSIDLE+1) prescaler cycles. The I2C bus is normally considered idle when the LPI2C master is first enabled, but when 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2476 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

BUSIDLE is configured greater than zero then SCL and/or SDA must be high for (BUSIDLE+1) prescaler cycles before the I2C bus is first considered idle. 

Pin Configuration 

- Open-drain support: The LPI2C master defaults to open-drain configuration of the SDA and SCL pins. Support for true open drain depends on the specific device, and requires the pins where LPI2C pins are muxed to support true open drain. 

- High Speed mode support: Support for high speed mode also depends on the specific device, and requires the SCL pin to support the current source pull-up required in the I2C specification. 

- Ultra-Fast mode support: The LPI2C master also supports the output-only push-pull function required for I2C ultra-fast mode using the SDA and SCL pins. Support for ultra-fast mode also requires the MCFGR1[IGNACK] bit to be set. 

- Push-pull 2-wire support: A push-pull 2-wire configuration is also available to the LPI2C master that may support a partial high speed mode, if the LPI2C is the only master and all I2C pins on the bus are at the same voltage. This configures the SCL pin as push-pull for every clock except the 9th clock pulse, to allow high speed mode compatible slaves to perform clock stretching. In this mode, the SDA pin is tristated for master-receive data bits and master-transmit ACK/NACK bits, and is configured as push-pull at other times. To avoid the risk of contention when SDA is push-pull, the pin can be configured for open-drain operation, as part of the device-specific configuration. 

- Push-pull 4-wire support: The push-pull 4-wire configuration separates the SCL input data and output data into separate pins, and separates the SDA input data and output data into separate pins. The SCL/SDA pins are used for input data; the SCLS/SDAS pins are used for output data, with configurable polarity. This simplifies external connections when connecting the LPI2C to the I2C bus through external level shifters or discrete components. When using this 4-wire configuration, the LPI2C master logic and LPI2C slave logic are not able to connect to separate I2C buses. 

### 69.3.2 Slave Mode 

To perform all slave mode transfers on the I2C bus, the LPI2C slave logic operates independently from the LPI2C master logic. 

##### Address Matching 

The LPI2C slave can be configured: 

- To match one of two addresses, using either 7-bit or 10-bit addressing modes for each address 

- To match a range of addresses in either 7-bit or 10-bit addressing modes 

- To match the General Call Address, and generate appropriate flags 

- To match the SMBus Alert Address, and generate appropriate flags 

- To detect the high speed mode master code, and to disable the digital filters and output valid delay time until the next STOP condition is detected 

After a valid address is matched, the LPI2C slave automatically performs slave-transmit or slave-receive transfers until: 

- A NACK is detected (unless SCFGR1[IGNACK] is set) 

- A bit error is detected (the LPI2C slave is driving SDA, but a different value is sampled) 

- A (repeated) START or STOP condition is detected 

##### Transmit and Receive Data 

- The Transmit and Receive Data registers are double-buffered and only update during a slave-transmit and slave-receive transfer, respectively. 

- The slave address that was received can be configured to be read from either the Receive Data register (for example, when using DMA to transfer data), or from the Address Status register. 

- The Transmit Data register can be configured to only request data after a slave-transmit transfer is detected, or to request new data whenever the Transmit Data register is empty. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2477 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

- The Transmit Data register should only be written when the Transmit Data flag (SSR[TDF]) is set. 

- The Receive Data register should only be read when the Received Data flag (SSR[RDF]) is set (or the Address Valid flag is set and SCFGR1[RXCFG] = 1). 

- The Address Status register should only be read when the Address Valid flag is set. 

##### Clock Stretching 

The LPI2C slave supports many configurable options for when clock stretching is performed. The following conditions can be configured to perform clock stretching: 

- During the 9th clock pulse of the address byte and the Address Valid flag is set. 

- During the 9th clock pulse of a slave-transmit transfer and the Transmit Data flag is set. 

- During the 9th clock pulse of a slave-receive transfer and the Receive Data flag is set. 

- During the 8th clock pulse of an address byte or a slave-receive transfer and the Transmit ACK flag is set. In high speed mode, this is disabled. 

- Clock stretching can also be extended for CLKHOLD cycles, to allow additional setup time to sample the SDA pin externally. In high speed mode, this is disabled. 

Unless extended by the CLKHOLD configuration, clock stretching extends for one peripheral bus clock cycle after SDA updates when clock stretching is enabled. 

##### Timing Parameters 

The LPI2C slave can configure the following timing parameters. These parameters are disabled when SCR[FILTEN] is clear, when SCR[FILTDZ] is set in Doze mode, and when LPI2C slave detects high speed mode. When disabled, the LPI2C slave is clocked directly from the I2C bus, and may not satisfy all timing requirements of the I2C specification (such as SDA minimum hold time in Standard/Fast mode). 

- SDA data valid time from SCL negation to SDA update 

- SCL hold time when clock stretching is enabled to increase setup time when sampling SDA externally 

- SCL glitch filter time 

- SDA glitch filter time 

The LPI2C slave imposes the following restrictions on the timing parameters. 

- FILTSDA must be configured to greater than or equal to FILTSCL (unless compensating for board level skew between SDA and SCL). 

- DATAVD must be configured less than the minimum SCL low period. 

##### Error Conditions 

The LPI2C slave can detect the following error conditions: 

- Bit error flag sets when the LPI2C slave is driving SDA, but samples a different value than what is expected. 

- FIFO error flag sets due to a transmit data underrun or a receive data overrun. To eliminate the possibility of underrun and overrun occurring, enable clock stretching. 

- FIFO error flag also sets due to an address overrun when SCFGR1[RXCFG] is set, otherwise an address overrun is not flagged. To eliminate the possibility of overrun occurring, enable clock stretching. 

The LPI2C slave does not implement a timeout due to SCL and/or SDA being stuck low. If this detection is required, then the LPI2C master logic should be used and so software can reset the LPI2C slave when this condition is detected. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2478 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

### 69.3.3 Low power modes 

Table 398. LPI2C low power modes 

||Mode|LPI2C Operation|
|---|---|---|
|Run||Normal operations|
|Stop||Can continue operating in Stop mode if the Doze Enable bit is clear (MCR[DOZEN]=<br>0) and LPI2C uses an external or internal clock source that remains operating during<br>Stop mode. LPI2C can generate an interrupt or DMA request to cause a wakeup from<br>Stop mode.|



### 69.3.4 Debug mode 

Table 399. LPI2C Debug mode 

||Mode|LPI2C Operation|
|---|---|---|
|Debug||Can continue operating in Debug mode if the Debug Enable bit is set<br>(MCR[DBGEN]= 1).|



### 69.3.5 Interrupts and DMA requests 

Depending on the configuration, interrupts and DMA requests can be combined: 

- The LPI2C master and slave interrupts are combined 

- The LPI2C master and slave transmit DMA requests are combined 

- The LPI2C master and slave receive DMA requests are combined 

##### Master mode 

The next table lists the master mode sources that can generate LPI2C master interrupts and LPI2C master transmit/receive DMA requests. 

Table 400. Master Interrupts and DMA Requests 

|Master|Status (MSR)|Description||Can generate||
|---|---|---|---|---|---|
|Flag|Name||Interrupt?|DMA<br>Request?|Low Power<br>Wakeup?|
|TDF|Transmit<br>Data Flag|Data can be written to Transmit FIFO, as<br>configured by the Transmit FIFO Watermark<br>MFCR[TXWATER]|Y|TX|Y|
|RDF|Receive Data<br>Flag|Data can be read from the Receive FIFO, as<br>configured by the Receive FIFO Watermark<br>MFCR[RXWATER]|Y|RX|Y|
|EPF|End Packet<br>Flag|Master has transmitted a Repeated START<br>or STOP condition|Y|N|Y|
|SDF|STOP Detect<br>Flag|Master has transmitted a STOP condition|Y|N|Y|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2479 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

Table 400. Master Interrupts and DMA Requests (continued) 

|Master S|tatus (MSR)|Description||Can generate||
|---|---|---|---|---|---|
|Flag|Name||Interrupt?|DMA<br>Request?|Low Power<br>Wakeup?|
|NDF|NACK Detect<br>Flag|• During an address byte, the master<br>expected an ACK but detected a NACK<br>• During an address byte, the master<br>expected a NACK but detected an ACK<br>• During a master-transmitter data byte,<br>the master detected a NACK|Y|N|Y|
|ALF|Arbitration<br>Lost Flag|• The master lost arbitration due to a<br>START/STOP condition detected at the<br>wrong time<br>• Or the master was transmitting data but<br>received different data than the data that<br>was transmitted|Y|N|Y|
|FEF|FIFO Error<br>Flag|The master is expecting a START condition<br>in the Command FIFO, but the next entry in<br>the Command FIFO is not a START condition|Y|N|Y|
|PLTF|Pin Low<br>Timeout Flag|Pin low timeout is enabled and SCL (or<br>SDA if configured) is low for longer than the<br>configured timeout|Y|N|Y|
|DMF|Data Match<br>Flag|The received data matches the configured<br>data match, but the received data is not<br>discarded due to a command FIFO entry|Y|N|Y|
|MBF|Master Busy<br>Flag|LPI2C master is busy transmitting/receiving<br>data|N|N|N|
|BBF|Bus Busy<br>Flag|LPI2C master is enabled and activity is<br>detected on the I2C bus, but a STOP<br>condition has not been detected and a bus<br>idle timeout (if enabled) has not occurred.|N|N|N|



##### Slave mode 

The next table lists the slave mode sources that can generate LPI2C slave interrupts and the LPI2C slave transmit/receive DMA requests. 

Table 401. Slave Interrupts and DMA Requests 

|Slave St|atus (SSR)|Description||Can generate||
|---|---|---|---|---|---|
|Flag|Name||Interrupt?|DMA|Low Power|
|||||Request?|Wakeup?|
|TDF|Transmit<br>Data Flag|Data can be written to theSlave Transmit<br>Data (STDR)|Y|TX|Y|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2480 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

Table 401. Slave Interrupts and DMA Requests (continued) 

|Slave S|tatus (SSR)|Description||Can generate||
|---|---|---|---|---|---|
|Flag|Name||Interrupt?|DMA<br>Request?|Low Power<br>Wakeup?|
|RDF|Receive Data<br>Flag|Data can be read from theSlave Receive<br>Data (SRDR)|Y|RX|Y|
|AVF|Address Valid<br>Flag|Address can be read from theSlave Address<br>Status (SASR)|Y|RX|Y|
|TAF|Transmit ACK<br>Flag|ACK/NACK can be written to theSlave<br>Transmit ACK (STAR)|Y|N|Y|
|RSF|Repeated<br>Start Flag|Slave has detected an address match<br>followed by a Repeated START condition|Y|N|Y|
|SDF|STOP Detect<br>Flag|Slave has detected an address match<br>followed by a STOP condition|Y|N|Y|
|BEF|Bit Error Flag|Slave was transmitting data, but received<br>different data than what was transmitted|Y|N|Y|
|FEF|FIFO Error<br>Flag|• Transmit data underrun<br>• Receive data overrun<br>• Address status overrun (when Receive<br>Data ConfigurationSCFGR1[RXCFG]=<br>1).<br>FEF flag can only set when clock stretching is<br>disabled.|Y|N|Y|
|AM0F|Address<br>Match 0 Flag|Slave detected an address match with<br>SAMR[ADDR0]field|Y|N|N|
|AM1F|Address<br>Match 1 Flag|Slave detected an address match with<br>SAMR[ADDR1]field or using an address<br>range|Y|N|N|
|GCF|General Call<br>Flag|Slave detected an address match with the<br>General Call address|Y|N|N|
|SARF|SMBus Alert<br>Response<br>Flag|Slave detected an address match with the<br>SMBus Alert address|Y|N|N|
|SBF|Slave Busy<br>Flag|LPI2C slave is busy receiving an address<br>byte or is transmitting/receiving data|N|N|N|
|BBF|Bus Busy<br>Flag|LPI2C slave is enabled and a START<br>condition is detected on I2C bus, but a STOP<br>condition has not been detected|N|N|N|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2481 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

### 69.3.6 Clocks 

Table 402. LPI2C clocks 

|LPI2C Functional clock|The LPI2C functional clock is asynchronous to the bus clock and can remain enabled in low power<br>modes to support I2C bus transfers by the LPI2C master. The functional clock is also used by the<br>LPI2C slave to support digital filter and data hold time configurations. The LPI2C master divides the<br>functional clock by a prescaler and the resulting frequency must be at least 8 times faster than the<br>I2C bus bandwidth.|
|---|---|
|External clock|The LPI2C slave logic is clocked directly from the external pins SCL and SDA (or SCLS and SDAS<br>if master and slave are implemented on separate pins). This allows the LPI2C slave to remain<br>operational, even when the LPI2C functional clock is disabled.<br>The LPI2C slave digital filter must be disabled if the LPI2C functional clock is disabled,<br>and this can affect compliance with some of the timing parameters of the I2C<br>specification, such as the data hold time.<br>~~NOTE~~|
|Bus clock|The bus clock is only used for bus accesses to the control and configuration registers. The bus<br>clock frequency must be sufficient to support the data bandwidth requirements of the LPI2C master<br>and slave registers.|



For device-specific clocking information, refer to the Clocking chapter. 

### 69.3.7 Resets 

Table 403. LPI2C Resets 

|Chip reset|The logic and registers for the LPI2C master and slave are reset to their default state on a chip<br>reset.|
|---|---|
|Software reset|• The LPI2C master implements a software reset bit in its Control Register. TheMCR[RST]bit<br>resets all master logic and registers to their default state, except for the MCR register itself.<br>• The LPI2C slave implements a software reset bit in its Control Register. TheSCR[RST]bit<br>resets all slave logic and registers to their default state, except for the SCR register itself.|
|FIFO reset|• The LPI2C master implements write-only control bits that reset the transmit FIFO (MCR[RTF])<br>and receive FIFO (MCR[RRF]). After a FIFO is reset, that FIFO is empty.|
||• The LPI2C slave implements write-only control bits that reset the transmit data register<br>(SCR[RTF]and receive data register (SCR[RRF]). After a data register is reset, that data<br>register is empty.|



### 69.3.8 Peripheral Triggers 

The connection of the LPI2C peripheral triggers to other peripherals depend upon the specific device being used. 

Table 404. LPI2C Triggers 

|Trigger|Description|
|---|---|
|Master Output Trigger|The LPI2C master generates an output trigger that can be connected to other peripherals on the<br>device. The master output trigger asserts on both a Repeated START or STOP condition, and<br>the master output trigger remains asserted for one cycle of the LPI2C functional clock divided by<br>the prescaler.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2482 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

Table 404. LPI2C Triggers (continued) 

|Trigger|Description|
|---|---|
|Slave Output Trigger|The LPI2C slave generates an output trigger that can be connected to other peripherals on the<br>device. The slave output trigger asserts on both a Repeated START or STOP condition that occurs<br>after a slave address match, and the slave output trigger remains asserted until the next slave SCL<br>pin negation.|
|Input Trigger|To control the start of a LPI2C bus transfer, the LPI2C input trigger can be selected instead of the<br>HREQinput. The input trigger is synchronized and to be detected, the input trigger must assert for at<br>least 2 cycles of the LPI2C functional clock divided by the PRESCALE configuration. When the LPI2C<br>is busy, the HREQ input (and therefore the input trigger) is ignored.|



## 69.4 External signals 

Table 405. Signals 

|Signal|Name|2-Wire Scheme|4-Wire Scheme|I/O|
|---|---|---|---|---|
|SCL|LPI2C clock<br>line|SCL|In 4-wire mode, this is the SCL input pin.|I/O|
|SDA|LPI2C data<br>line|SDA|In 4-wire mode, this is the SDA input pin.|I/O|
|SCLS|Secondary<br>I2C clock line|Not used|In 4-wire mode, this is the SCLS output pin.<br>If LPI2C master/slave are configured to use<br>separate pins, then this is the LPI2C slave<br>SCL pin.|I/O|
|SDAS|Secondary<br>I2C data line|Not used|In 4-wire mode, this is the SDAS output pin.<br>If LPI2C master/slave are configured to use<br>separate pins, then this is the LPI2C slave<br>SDA pin.|I/O|
|HREQ|Host request|If host request is assert<br>master transfer.<br>HREQ is an additional p|ed and the I2C bus is idle, then it initiates an LPI2C<br>in separate from the 2-wire or 4-wire scheme.|I|



The I<sup>2</sup> C 2-wire serial bus diagram shows the 2 signal connection. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2483 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/069_Low_Power_Inter-Integrated_Circuit_-LPI2C-/S32K3XXRM_数据表.pdf-2484-02.png)


<!-- Start of picture text -->
I²C (Inter-Integrated Circuit) 2-Wire Serial Bus<br>Data (SDA)<br>MCU<br>Clock (SCL)<br>Microcontroller<br>2-wire  2-wire  2-wire<br> peripheral  peripheral  peripheral<br> device #1  device #2  device #3<br>Slave Slave Slave<br><!-- End of picture text -->

Figure 365. I<sup>2</sup> C 2-wire serial bus 

The I<sup>2</sup> C 4-wire serial bus diagram shows a possible 4 signal connection. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/069_Low_Power_Inter-Integrated_Circuit_-LPI2C-/S32K3XXRM_数据表.pdf-2484-05.png)


<!-- Start of picture text -->
simple line drivers<br>Vdd<br>SDA SDA<br>SDAS<br>Microcontroller<br>side SCL SCL<br>SCLS<br><!-- End of picture text -->

Figure 366. I<sup>2</sup> C 4-wire serial bus 

## 69.5 Memory Map and Registers 

~~<mark>NOTE</mark>~~ 

Writing a Read-Only (RO) register or reading a Write-Only (WO) register can cause bus errors. This module will not check if programmed values in the registers are correct; the application software must ensure that valid programmed values are being written. 

### 69.5.1 LPI2C register descriptions 

69.5.1.1 LPI2C memory map 

LPI2C_0 base address: 4035_0000h LPI2C_1 base address: 4035_4000h 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2484 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|0h|Version ID (VERID)|32|RO|0102_0003h|
|4h|Parameter (PARAM)|32|RO|0000_0202h|
|10h|Master Control (MCR)|32|RW|0000_0000h|
|14h|Master Status (MSR)|32|W1C|0000_0001h|
|18h|Master Interrupt Enable (MIER)|32|RW|0000_0000h|
|1Ch|Master DMA Enable (MDER)|32|RW|0000_0000h|
|20h|Master Configuration 0 (MCFGR0)|32|RW|0000_0000h|
|24h|Master Configuration 1 (MCFGR1)|32|RW|0000_0000h|
|28h|Master Configuration 2 (MCFGR2)|32|RW|0000_0000h|
|2Ch|Master Configuration 3 (MCFGR3)|32|RW|0000_0000h|
|40h|Master Data Match (MDMR)|32|RW|0000_0000h|
|48h|Master Clock Configuration 0 (MCCR0)|32|RW|0000_0000h|
|50h|Master Clock Configuration 1 (MCCR1)|32|RW|0000_0000h|
|58h|Master FIFO Control (MFCR)|32|RW|0000_0000h|
|5Ch|Master FIFO Status (MFSR)|32|RO|0000_0000h|
|60h|Master Transmit Data (MTDR)|32|WO|0000_0000h|
|70h|Master Receive Data (MRDR)|32|RO|0000_4000h|
|110h|Slave Control (SCR)|32|RW|0000_0000h|
|114h|Slave Status (SSR)|32|W1C|0000_0000h|
|118h|Slave Interrupt Enable (SIER)|32|RW|0000_0000h|
|11Ch|Slave DMA Enable (SDER)|32|RW|0000_0000h|
|124h|Slave Configuration 1 (SCFGR1)|32|RW|0000_0000h|
|128h|Slave Configuration 2 (SCFGR2)|32|RW|0000_0000h|
|140h|Slave Address Match (SAMR)|32|RW|0000_0000h|
|150h|Slave Address Status (SASR)|32|RO|0000_4000h|
|154h|Slave Transmit ACK (STAR)|32|RW|0000_0000h|
|160h|Slave Transmit Data (STDR)|32|WO|0000_0000h|
|170h|Slave Receive Data (SRDR)|32|RO|0000_4000h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2485 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

#### 69.5.1.2 Version ID (VERID) 

##### Offset 

|Register|Offset|
|---|---|
|VERID|0h|



##### Function 

Contains version numbers for the module design and feature set. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||MA|JOR|||||||MIN|OR||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|1|0|0|0|0|0|0|1|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||FEAT|URE||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|1|



##### Fields 

|Field|Function|
|---|---|
|31-24|Major Version Number|
|MAJOR|Returns the major version number for the module design specification. Read-only field.|
|23-16|Minor Version Number|
|MINOR|Returns the minor version number for the module design specification. Read-only field.|
|15-0|Feature Specification Number|
|FEATURE|Returns the feature set number. Read-only field.|
||0000_0000_0000_0010b - Master only, with standard feature set|
||0000_0000_0000_0011b - Master and slave, with standard feature set|



#### 69.5.1.3 Parameter (PARAM) 

##### Offset 

|Register|Offset|
|---|---|
|PARAM|4h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2486 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Function 

Contains parameter values that were implemented in the module. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||0||||MRX|FIFO|||0||||MTX|FIFO||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|1|0|0|0|0|0|0|0|1|0|



##### Fields 

|Field|Function|
|---|---|
|31-16|Reserved|
|—<br>15-12|Reserved|
|—||
|11-8|Master Receive FIFO Size|
|MRXFIFO|Configures the number of words in the master receive FIFO to 2<sup>MRXFIFO</sup>|
|7-4|Reserved|
|—<br>3-0|Master Transmit FIFO Size|
|MTXFIFO|Configures the number of words in the master transmit FIFO to 2<sup>MTXFIFO</sup>|



#### 69.5.1.4 Master Control (MCR) 

##### Offset 

|Register|Offset|
|---|---|
|MCR|10h|



##### Function 

The MCR register contains resets, debug enable, and other master control settings. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2487 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||0||||0|0||0|||DBGE|DOZE|RST|MEN|
|W|||||||RRF|RTF|||||N|N|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-10<br>—|Reserved|
|9<br>RRF|Reset Receive FIFO<br>Resets the Receive FIFO.<br>0b - No effect<br>1b - Receive FIFO is reset|
|8<br>RTF|Reset Transmit FIFO<br>Resets the Transmit FIFO.<br>0b - No effect<br>1b - Transmit FIFO is reset|
|7-4<br>—|Reserved|
|3|Debug Enable|
|DBGEN|Enables the Master in Debug mode.<br>0b - Master is disabled in debug mode<br>1b - Master is enabled in debug mode|
|2|Doze mode enable|
|DOZEN|Enables or disables the master in Doze mode.<br>0b - Master is enabled in Doze mode<br>1b - Master is disabled in Doze mode|
|1|Software Reset|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2488 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/069_Low_Power_Inter-Integrated_Circuit_-LPI2C-/S32K3XXRM_数据表.pdf-2489-03.png)


<!-- Start of picture text -->
Field Function<br>RST Resets all internal master logic and registers, except the Master Control (MCR) register. RST remains<br>set until cleared by software. The reset takes effect immediately and remains asserted until negated by<br>software. There is no minimum delay required before clearing the software reset.<br>0b - Master logic is not reset<br>1b - Master logic is reset<br>0 Master Enable<br>MEN Enables the Master logic.<br>0b - Master logic is disabled<br>1b - Master logic is enabled<br><!-- End of picture text -->

#### 69.5.1.5 Master Status (MSR) 

##### Offset 

|Register|Offset|
|---|---|
|MSR|14h|



##### Function 

MSR contains status flags for transmit and receive data; Start and Stop conditions; and bus and master busy or idle status. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/069_Low_Power_Inter-Integrated_Circuit_-LPI2C-/S32K3XXRM_数据表.pdf-2489-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 BBF  MBF  0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 DMF  PLTF  FEF  ALF  NDF  SDF  EPF  0 RDF  TDF<br>W W1C W1C W1C W1C W1C W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-26<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2489 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|25|Bus Busy Flag|
|BBF|Indicates that the I2C bus is busy.<br>0b - I2C Bus is idle<br>1b - I2C Bus is busy|
|24<br>MBF|Master Busy Flag<br>Indicates that the I2C Master is busy.<br>0b - I2C Master is idle<br>1b - I2C Master is busy|
|23-16<br>—|Reserved|
|15<br>—|Reserved|
|14|Data Match Flag|
|DMF|Indicates that the received data has matched theMDMR[MATCH0]and/orMDMR[MATCH1]fields (as<br>configured byMCFGR1[MATCFG]. Received data that is discarded due to CMD field does not cause<br>DMF to set.<br>0b - Have not received matching data<br>1b - Have received matching data|
|13<br>PLTF|Pin Low Timeout Flag<br>Sets when the SCL and/or SDA input is low for more than PINLOW cycles (Pin Low Timeout,<br>MCFGR3[PINLOW]), even when the LPI2C master is idle.<br>• Software is responsible for resolving the pin low condition.<br>• PLTF cannot be cleared as long as the pin low timeout continues.<br>• Before the LPI2C can initiate a START condition, the PLTF must be cleared.<br>SeeMCFGR1[TIMECFG]for the SCL and/or SDA timeout settings.<br>0b - Pin low timeout has not occurred or is disabled<br>1b - Pin low timeout has occurred|
|12<br>FEF|FIFO Error Flag<br>Detects an attempt to send or receive data without first generating a (repeated) START condition. This<br>can occur if the transmit FIFO underflows whenMCFGR1[AUTOSTOP]= 1. When FEF is set, the LPI2C<br>master sends a STOP condition (if busy), and does not initiate a new START condition until FEF has<br>been cleared.<br>0b - No error|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2490 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Table continued from the previous page... 

|Field|Function<br>1b - Master sending or receiving data without a START condition|
|---|---|
|11<br>ALF|Arbitration Lost Flag<br>Set if either of these conditions exist:<br>• The LPI2C master transmits a logic one and detects a logic zero on the I2C bus<br>• The LPI2C master detects a START or STOP condition while the LPI2C master is transmitting data<br>When ALF sets, the LPI2C master releases the I2C bus (goes idle), and the LPI2C master does not<br>initiate a new START condition until the ALF has been cleared.<br>0b - Master has not lost arbitration<br>1b - Master has lost arbitration|
|10<br>NDF|NACK Detect Flag<br>Set if the LPI2C master detects a NACK it was not expecting when transmitting an address or data. When<br>set, the master does not initiate a new START condition until NDF has been cleared. If a NACK is expected<br>for a given address (as configured by the command word), then the NDF sets if a NACK is not generated.<br>When NDF is set, the LPI2C master automatically transmits a STOP condition ifMCFGR1[AUTOSTOP]=<br>1, or the transmit FIFO is not empty.<br>0b - Unexpected NACK was not detected<br>1b - Unexpected NACK was detected|
|9<br>SDF|STOP Detect Flag<br>Set when the LPI2C master generates a STOP condition.<br>0b - Master has not generated a STOP condition<br>1b - Master has generated a STOP condition|
|8|End Packet Flag|
|EPF|Set when the LPI2C master generates either a repeated START condition or a STOP condition. Does<br>not set when the master first generates a START condition.<br>0b - Master has not generated a STOP or Repeated START condition<br>1b - Master has generated a STOP or Repeated START condition|
|7-2<br>—|Reserved|
|1<br>RDF|Receive Data Flag<br>RDF sets whenever the number of words in the receive FIFO is greater thanMFCR[RXWATER].<br>0b - Receive Data is not ready<br>1b - Receive data is ready|
|0|Transmit Data Flag|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2491 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|TDF|TDF sets whenever the number of words in the transmit FIFO is equal or less thanMFCR[TXWATER].|
||0b - Transmit data is not requested|
||1b - Transmit data is requested|



#### 69.5.1.6 Master Interrupt Enable (MIER) 

##### Offset 

|Register|Offset|
|---|---|
|MIER|18h|



##### Function 

MIER contains transmit and receive data interrupt enables; START, STOP, and NACK detect interrupt enables; and DMA interrupt enables. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/069_Low_Power_Inter-Integrated_Circuit_-LPI2C-/S32K3XXRM_数据表.pdf-2492-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>DMIE  PLTIE  FEIE  ALIE  NDIE  SDIE  EPIE  RDIE  TDIE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16<br>—|Reserved|
|15<br>—|Reserved|
|14|Data Match Interrupt Enable|
|DMIE|Enables interrupt for data match.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2492 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Disabled<br>1b - Enabled|
|13|Pin Low Timeout Interrupt Enable|
|PLTIE|Enables interrupt for pin low timeout.<br>0b - Disabled<br>1b - Enabled|
|12|FIFO Error Interrupt Enable|
|FEIE|Enables interrupt for FIFO error.<br>0b - Disabled<br>1b - Enabled|
|11<br>ALIE|Arbitration Lost Interrupt Enable<br>Enables interrupt for arbitration lost.<br>0b - Disabled<br>1b - Enabled|
|10|NACK Detect Interrupt Enable|
|NDIE|Enables interrupt for NACK detect.|
||0b - Disabled<br>1b - Enabled|
|9|STOP Detect Interrupt Enable|
|SDIE|Enables interrupt for STOP detect.|
||0b - Disabled|
||1b - Enabled|
|8|End Packet Interrupt Enable|
|EPIE|Enables interrupt for end packet.|
||0b - Disabled|
||1b - Enabled|
|7-2<br>—|Reserved|
|1|Receive Data Interrupt Enable|
|RDIE|Enables interrupt for receive data.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2493 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Disabled|
||1b - Enabled|
|0|Transmit Data Interrupt Enable|
|TDIE|Enables interrupt for transmit data.|
||0b - Disabled|
||1b - Enabled|



#### 69.5.1.7 Master DMA Enable (MDER) 

##### Offset 

|Register|Offset|
|---|---|
|MDER|1Ch|



##### Function 

MDER contains DMA transmit, request, and receive enables. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/069_Low_Power_Inter-Integrated_Circuit_-LPI2C-/S32K3XXRM_数据表.pdf-2494-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>RDDE  TDDE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-2<br>—|Reserved|
|1|Receive Data DMA Enable|
|RDDE|Enables DMA receive data.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2494 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - DMA request is disabled|
||1b - DMA request is enabled|
|0|Transmit Data DMA Enable|
|TDDE|Enables DMA transmit data.|
||0b - DMA request is disabled|
||1b - DMA request is enabled|



#### 69.5.1.8 Master Configuration 0 (MCFGR0) 

##### Offset 

|Register|Offset|
|---|---|
|MCFGR0|20h|



##### Function 

MCFGR0 contains host settings and other receive and transfer settings. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||0||||||||0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||0||||RDMO|CIRFIF||0|||0|HRSE|HRPO|HREN|
|W||||||||O||||||L|L||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function|
|---|---|
|31-18<br>—|Reserved|
|17-16<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2495 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Table continued from the previous page... 

|Field<br>15-10<br>—|Function<br>Reserved|
|---|---|
|9<br>RDMO|Receive Data Match Only<br>When enabled, all received data that does not cause the Data Match Flag (MSR[DMF]) to set is<br>discarded. AfterMSR[DMF]is set, the RDMO configuration is ignored. When disabling RDMO, clear<br>RDMO before clearingMSR[DMF], to ensure that no receive data is lost.<br>0b - Received data is stored in the receive FIFO<br>1b - Received data is discarded unless the the Data Match Flag (MSR[DMF]) is set|
|8<br>CIRFIFO|Circular FIFO Enable<br>When enabled, the transmit FIFO read pointer is saved to a temporary register. The transmit FIFO<br>empties as normal, but after the LPI2C master is idle and the transmit FIFO is empty, then the read<br>pointer value will be restored from the temporary register. This causes the contents of the transmit<br>FIFO to be cycled through repeatedly. IfMCFGR1[AUTOSTOP]is set, then a STOP condition is sent<br>whenever the transmit FIFO is empty and the read pointer is restored.<br>0b - Circular FIFO is disabled<br>1b - Circular FIFO is enabled|
|7-4<br>—<br>3<br>—<br>2<br>HRSEL|Reserved<br>Reserved<br>Host Request Select<br>Selects the source of the host request input. When host request is enabled, HRSEL should remain static<br>(the Host Request Select should not change).<br>0b - Host request input is pin HREQ<br>1b - Host request input is input trigger|
|1<br>HRPOL|Host Request Polarity<br>Configures the polarity of the host request input. When host request is enabled, HRPOL should remain<br>static (Host Request Polarity should not change).<br>0b - Active low<br>1b - Active high|
|0|Host Request Enable|
|HREN|When enabled, the LPI2C master only initiates a START condition if the host request input is asserted<br>and the bus is idle. A repeated START is not affected by the host request.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2496 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Host request input is disabled|
||1b - Host request input is enabled|



#### 69.5.1.9 Master Configuration 1 (MCFGR1) 

Offset 

|Register|Offset|
|---|---|
|MCFGR1|24h|



##### Function 

The MCFGR1 should only be written when the I2C Master is disabled. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18<br>17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||0|||FRCH<br>S||PINCFG||||0|||MATCFG||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2<br>1|0|
|R||0|||0|TIMEC|IGNAC|AUTO|||0|||PRESCALE||
|W||||||FG|K|STOP||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|0|



##### Fields 

|Field|Function|
|---|---|
|31-28|Reserved|
|—||
|27|Force HS-mode|
|FRCHS|When set, forces the LPI2C pin state into HS-mode. Setting this does not impact the digital filter<br>configuration or digital timing parameters.|
||0b - No effect|
||1b - LPI2C pin state forced into HS-mode.|
|26-24|Pin Configuration|
|PINCFG|Configures the pin mode for LPI2C.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2497 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

|Field|Function<br>Table 406. 2-|pin / 4-pin pin configurations for masters and sl|aves|
|---|---|---|---|
||PINCFG|SCL / SDA pins|SCLS / SDAS pins|
||000|Bi-directional open drain for master<br>and slave|Not used|
||001|Output-only (ultra-fast mode) open drain for<br>master and slave|Not used|
||010|Bi-directional push-pull for master and slave|Not used|
||011|Input only for master and slave|Output-only push-pull for master and slave|
||100|Bi-directional open drain for master|Bi-directional open drain for slave|
||101|Output-only (ultra-fast mode) open drain<br>for master|Output-only open drain for slave|
||110|Bi-directional push-pull for master|Bi-directional push-pull for slave|
||111|Input only for master and slave|Inverted output-only push-pull for master<br>and slave|
||000b<br>001b<br>010b<br>011b<br>100b<br>101b<br>110b<br>111b|- 2-pin open drain mode<br>- 2-pin output only mode (ultra-fast mode)<br>- 2-pin push-pull mode<br>- 4-pin push-pull mode<br>- 2-pin open drain mode with separate LPI2C sl<br>- 2-pin output only mode (ultra-fast mode) with<br>- 2-pin push-pull mode with separate LPI2C sla<br>- 4-pin push-pull mode (inverted outputs)|ave<br>separate LPI2C slave<br>ve|
|23-19<br>—|Reserved|||
|18-16<br>MATCFG|Match Config<br>Configures th<br>000b<br>001b<br>010b<br>011b<br>100b<br>MDM<br>101b<br>MDM|uration<br>e condition that causesMSR[DMF]to set. See<br>- Match is disabled<br>- Reserved<br>- Match is enabled (1st data word equals MDM<br>- Match is enabled (any data word equals MDM<br>- Match is enabled (1st data word equals MDM<br>R[MATCH1)<br>- Match is enabled (any data word equals MDM<br>R[MATCH1)<br>Table continues on the next page.|Master Data Match (MDMR).<br>R[MATCH0] OR MDMR[MATCH1])<br>R[MATCH0] OR MDMR[MATCH1])<br>R[MATCH0] AND 2nd data word equals<br>R[MATCH0] AND next data word equals<br>..|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2498 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

|Field|Function|
|---|---|
||110b - Match is enabled (1st data word AND MDMR[MATCH1] equals MDMR[MATCH0] AND<br>MDMR[MATCH1])<br>111b - Match is enabled (any data word AND MDMR[MATCH1] equals MDMR[MATCH0] AND<br>MDMR[MATCH1])|
|15-13<br>—|Reserved|
|12-11<br>—|Reserved|
|10<br>TIMECFG|Timeout Configuration<br>TIMECFG configures the timeout settings for the Pin Low Timeout Flag field (MSR[PLTF]).<br>0b - MSR[PLTF] sets if SCL is low for longer than the configured timeout<br>1b - MSR[PLTF] sets if either SCL or SDA is low for longer than the configured timeout|
|9<br>IGNACK|Ignore NACK<br>When set, the received NACK field is ignored and assumed to be ACK. IGNACK bit is required to be set<br>in Ultra-Fast Mode.<br>0b - No effect<br>1b - LPI2C Master treats a received NACK as if it (NACK) was an ACK|
|8|Automatic STOP Generation|
|AUTOSTOP|When enabled, a STOP condition is generated whenever the LPI2C master is busy and the transmit<br>FIFO is empty. The STOP condition can also be generated using a transmit FIFO command.<br>0b - No effect<br>1b - STOP condition is automatically generated whenever the transmit FIFO is empty and the<br>LPI2C master is busy|
|7-3<br>—|Reserved|
|2-0<br>PRESCALE|Prescaler<br>Configures the clock prescaler used for all LPI2C master logic, except for the digital glitch filters.<br>000b - Divide by 1<br>001b - Divide by 2<br>010b - Divide by 4<br>011b - Divide by 8<br>100b - Divide by 16<br>101b - Divide by 32<br>110b - Divide by 64|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2499 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

|Field|Function|
|---|---|
||111b - Divide by 128|



#### 69.5.1.10 Master Configuration 2 (MCFGR2) 

##### Offset 

|Register|Offset|
|---|---|
|MCFGR2|28h|



##### Function 

The Master Configuration Register 2 should only be written when the I2C Master is disabled. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/069_Low_Power_Inter-Integrated_Circuit_-LPI2C-/S32K3XXRM_数据表.pdf-2500-09.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0<br>FILTSDA  FILTSCL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>BUSIDLE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-28|Reserved|
|—||
|27-24|Glitch Filter SDA|
|FILTSDA|Configures the I2C master digital glitch filters for SDA input.<br>• A configuration of 0 disables the glitch filter<br>• Glitches equal to or less than FILTSDA cycles long are filtered out and ignored<br>• The latency through the glitch filter is equal to FILTSDA cycles, and must be configured to be less<br>than the minimum SCL low or high period<br>• The glitch filter cycle count is not affected by the PRESCALE configuration, and the glitch filter cycle<br>count is automatically bypassed in High Speed mode|
|23-20|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2500 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|19-16<br>FILTSCL|Glitch Filter SCL<br>Configures the I2C master digital glitch filters for SCL input.<br>• A configuration of 0 disables the glitch filter<br>• Glitches equal to or less than FILTSCL cycles long are filtered out and ignored. The FILTSCL cycles<br>are based on the functional clock.<br>• The latency through the glitch filter is equal to FILTSCL cycles, and must be configured to be less<br>than the minimum SCL low or high period<br>• The glitch filter cycle count is not affected by the PRESCALE configuration, and the glitch filter cycle<br>count is automatically bypassed in High Speed mode|
|15-12<br>—|Reserved|
|11-0<br>BUSIDLE|Bus Idle Timeout<br>Configures the bus idle timeout period in clock cycles.<br>• If both SCL and SDA are high for longer than BUSIDLE cycles, then the I2C bus is assumed to be<br>idle and the master can generate a START condition<br>• When Bus Idle Timeout is set to zero, the Bus Idle Timeout is disabled|



#### 69.5.1.11 Master Configuration 3 (MCFGR3) 

##### Offset 

|Register|Offset|
|---|---|
|MCFGR3|2Ch|



##### Function 

The MCFGR3 should only be written when the I2C Master is disabled. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2501 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||0||||||||PIN|LOW||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||PINL|OW|||||||0|||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-20|Reserved|
|—||
|19-8|Pin Low Timeout|
|PINLOW|Configures the pin low timeout flag in clock cycles.<br>• If SCL or, either SCL or SDA (selected byMCFGR1[TIMECFG]) is low for longer than (PINLOW *<br>256) cycles, thenMSR[PLTF]is set.<br>• When Pin Low Timeout is set to zero, the Pin Low Timeout feature is disabled|
|7-0<br>—|Reserved|



#### 69.5.1.12 Master Data Match (MDMR) 

##### Offset 

|Register|Offset|
|---|---|
|MDMR|40h|



##### Function 

The MDMR should only be written when the I2C Master is disabled or idle. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2502 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||||0|||||||MAT|CH1||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||||0|||||||MAT|CH0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-24|Reserved|
|—||
|23-16|Match 1 Value|
|MATCH1|Compared against the received data when receive data match is enabled.|
|15-8|Reserved|
|—||
|7-0|Match 0 Value|
|MATCH0|Compared against the received data when receive data match is enabled.|



#### 69.5.1.13 Master Clock Configuration 0 (MCCR0) 

##### Offset 

|Register|Offset|
|---|---|
|MCCR0|48h|



##### Function 

The MCCR0 cannot be changed when the I2C master is enabled and is used for standard, fast, fast-mode plus and ultra-fast transfers. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2503 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/069_Low_Power_Inter-Integrated_Circuit_-LPI2C-/S32K3XXRM_数据表.pdf-2504-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0<br>DATAVD  SETHOLD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>CLKHI  CLKLO<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29-24|Data Valid Delay|
|DATAVD|Minimum number of cycles (minus one) that is used as the data hold time for SDA. Must be configured<br>less than the minimum SCL low period.|
|23-22|Reserved|
|—<br>21-16|Setup Hold Delay|
|SETHOLD|Minimum number of cycles (minus one) that is used by the master for these conditions:<br>• Hold time for a START<br>• Setup and hold time for a repeated START<br>• Setup time for a STOP<br>The setup time is extended by the time it takes to detect a rising edge on the external SCL pin. Ignoring<br>any additional board delay due to external loading, this time is equal to (2 + FILTSCL) / 2^PRESCALE<br>cycles.|
|15-14<br>—|Reserved|
|13-8<br>CLKHI|Clock High Period<br>Minimum number of cycles (minus one) that the SCL clock is driven high by the master. The SCL<br>high time is extended by the time it takes to detect a rising edge on the external SCL pin. Ignoring<br>any additional board delay due to external loading, this time is equal to (2 + FILTSCL) / 2^PRESCALE<br>cycles.|
|7-6|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2504 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|5-0|Clock Low Period|
|CLKLO|Minimum number of cycles (minus one) that the SCL clock is driven low by the master. The Clock Low<br>Period value is also used for the minimum bus free time between a STOP and a START condition; this<br>is extended by the time it takes to detect a rising edge on the external SCL pin. Ignoring any additional<br>board delay due to external loading, this time is equal to (2 + FILTSCL) / 2^PRESCALE cycles.|



#### 69.5.1.14 Master Clock Configuration 1 (MCCR1) 

##### Offset 

|Register|Offset|
|---|---|
|MCCR1|50h|



##### Function 

The MCCR1 cannot be changed when the I2C master is enabled and is used for high speed mode transfers. The separate clock configuration for high speed mode allows arbitration to take place in Fast mode (with timing configured by Master Clock Configuration 0 (MCCR0)), before switching to high speed mode (with timing configured by MCCR1). 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/069_Low_Power_Inter-Integrated_Circuit_-LPI2C-/S32K3XXRM_数据表.pdf-2505-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0<br>DATAVD  SETHOLD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>CLKHI  CLKLO<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-30<br>—|Reserved|
|29-24|Data Valid Delay|
|DATAVD||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2505 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||Minimum number of cycles (minus one) that is used as the data hold time for SDA. The DATAVD must<br>be configured to be less than the minimum SCL low period.|
|23-22<br>—|Reserved|
|21-16<br>SETHOLD|Setup Hold Delay<br>Minimum number of cycles (minus one) that is used by the master for these conditions:<br>• Hold time for a START condition<br>• Setup and hold time for a repeated START condition<br>• Setup time for a STOP condition<br>The setup time is extended by the time it takes to detect a rising edge on the external SCL pin. Ignoring<br>any additional board delay due to external loading, this time is equal to (2 + FILTSCL) / 2^PRESCALE<br>cycles.|
|15-14<br>—|Reserved|
|13-8<br>CLKHI|Clock High Period<br>Minimum number of cycles (minus one) that the SCL clock is driven high by the master. The SCL<br>high time is extended by the time it takes to detect a rising edge on the external SCL pin. Ignoring<br>any additional board delay due to external loading, this time is equal to (2 + FILTSCL) / 2^PRESCALE<br>cycles.|
|7-6<br>—<br>5-0<br>CLKLO|Reserved<br>Clock Low Period<br>Minimum number of cycles (minus one) that the SCL clock is driven low by the master. The CLKLO<br>value is also used for the minimum bus free time between a STOP and a START condition; this is<br>extended by the time it takes to detect a rising edge on the external SCL pin. Ignoring any additional<br>board delay due to external loading, this time is equal to (2 + FILTSCL) / 2^PRESCALE cycles.|



#### 69.5.1.15 Master FIFO Control (MFCR) 

##### Offset 

|Register|Offset|
|---|---|
|MFCR|58h|



##### Function 

The Master FIFO control register is only used in Stop mode when the MFCR register is static (that is, the MFCR register is not changing). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2506 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||||||0||||||||RXWATER|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R<br>W|||||||0||||||||TXWATER|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



##### Fields 

|Field|Function|
|---|---|
|31-18|Reserved|
|—||
|17-16|Receive FIFO Watermark|
|RXWATER|The Receive Data Flag (SSR[RDF]) is set whenever the number of words in the receive FIFO is greater<br>than RXWATER. Writing a value equal to or greater than the FIFO size truncates the value.|
|15-2|Reserved|
|—||
|1-0|Transmit FIFO Watermark|
|TXWATER|The Transmit Data Flag (SSR[TDF]) is set whenever the number of words in the transmit FIFO is equal<br>or less than TXWATER. Writing a value equal to or greater than the FIFO size truncates the value.|



#### 69.5.1.16 Master FIFO Status (MFSR) 

##### Offset 

|Register|Offset|
|---|---|
|MFSR|5Ch|



##### Function 

MFSR gives the number of words in the transmit and receive FIFO. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2507 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18<br>17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||0|||||||RXCOUNT|
|W|||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2<br>1<br>0|
|R|||||||0|||||||TXCOUNT|
|W|||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0<br>0|



##### Fields 

|Field|Function|
|---|---|
|31-19<br>—|Reserved|
|18-16|Receive FIFO Count|
|RXCOUNT|Returns the number of words in the receive FIFO.|
|15-3<br>—|Reserved|
|2-0|Transmit FIFO Count|
|TXCOUNT|Returns the number of words in the transmit FIFO.|



#### 69.5.1.17 Master Transmit Data (MTDR) 

##### Offset 

|Register|Offset|
|---|---|
|MTDR|60h|



##### Function 

- An 8-bit write to the CMD field is ignored and does not increment the FIFO write pointer. 

- An 8-bit write to the DATA field zero-extends the CMD field and increments the FIFO write pointer. 

- A 16-bit or 32-bit writes both the CMD and DATA fields and increments the FIFO write pointer. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2508 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/069_Low_Power_Inter-Integrated_Circuit_-LPI2C-/S32K3XXRM_数据表.pdf-2509-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>W 0<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>W 0 CMD  DATA<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-11|Reserved|
|—||
|10-8<br>CMD|Command Data<br>000b - Transmit DATA[7:0]<br>001b - Receive (DATA[7:0] + 1) bytes<br>010b - Generate STOP condition<br>011b - Receive and discard (DATA[7:0] + 1) bytes<br>100b - Generate (repeated) START and transmit address in DATA[7:0]<br>101b - Generate (repeated) START and transmit address in DATA[7:0]. This transfer expects a<br>NACK to be returned.<br>110b - Generate (repeated) START and transmit address in DATA[7:0] using high speed mode<br>111b - Generate (repeated) START and transmit address in DATA[7:0] using high speed mode.<br>This transfer expects a NACK to be returned.|
|7-0|Transmit Data|
|DATA|Performing an 8-bit write to DATA zero-extends the CMD field.|



#### 69.5.1.18 Master Receive Data (MRDR) 

Offset 

|Register|Offset|
|---|---|
|MRDR|70h|



Function 

Reading the Receive Data register returns the data received by the I2C master that has not been discarded. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2509 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|0|RXEM<br>PTY||||0||||||DA|TA||||
|W|||||||||||||||||
|Reset|0|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-15|Reserved|
|—||
|14|Receive Empty|
|RXEMPTY|RXEMPTY gives the empty status of the Master receive data FIFO.<br>0b - Receive FIFO is not empty<br>1b - Receive FIFO is empty|
|13-8|Reserved|
|—||
|7-0|Receive Data|
|DATA|Receive data can be discarded due to the CMD field, or the master can be configured to discard<br>non-matching data.|



#### 69.5.1.19 Slave Control (SCR) 

##### Offset 

|Register|Offset|
|---|---|
|SCR|110h|



##### Function 

SCR contains resets and other slave control settings. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2510 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||0||||0|0|0||FILTD|FILTE|0||RST|SEN|
|W|||||||RRF|RTF|||Z|N|||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-10<br>—|Reserved|
|9<br>RRF|Reset Receive FIFO<br>Resets the receive FIFO to b be empty.<br>0b - No effect<br>1b - Receive Data Register is now empty|
|8<br>RTF|Reset Transmit FIFO<br>Resets the transmit FIFO to be empty.<br>0b - No effect<br>1b - Transmit Data Register is now empty|
|7-6<br>—|Reserved|
|5<br>FILTDZ|Filter Doze Enable<br>FILTDZ should only be updated when the I2C Slave is disabled.<br>0b - Filter remains enabled in Doze mode<br>1b - Filter is disabled in Doze mode|
|4<br>FILTEN|Filter Enable<br>FILTEN should only be updated when the I2C Slave is disabled.<br>0b - Disable digital filter and output delay counter for slave mode<br>1b - Enable digital filter and output delay counter for slave mode|
|3-2|Reserved<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2511 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|1|Software Reset|
|RST|The reset takes effect immediately and remains asserted until negated by software. There is no minimum<br>delay required before clearing the software reset.|
||0b - Slave mode logic is not reset|
||1b - Slave mode logic is reset|
|0|Slave Enable|
|SEN|Enables the I2C Slave mode.|
||0b - I2C Slave mode is disabled|
||1b - I2C Slave mode is enabled|



#### 69.5.1.20 Slave Status (SSR) 

##### Offset 

|Register|Offset|
|---|---|
|SSR|114h|



##### Function 

SSR contains status flags for transmit and receive data; error conditions; and bus and slave busy or idle status. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||0||||BBF|SBF|||||0||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|SARF|GCF|AM1F|AM0F|FEF|BEF|SDF|RSF||0|||TAF|AVF|RDF|TDF|
|W|||||W1C|W1C|W1C|W1C|||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2512 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Fields 

|Field|Function|
|---|---|
|31-26<br>—|Reserved|
|25<br>BBF|Bus Busy Flag<br>Indicates if an I2C bus is idle or busy.<br>0b - I2C Bus is idle<br>1b - I2C Bus is busy|
|24<br>SBF|Slave Busy Flag<br>Indicates if an I2C slave is idle or busy.<br>0b - I2C Slave is idle<br>1b - I2C Slave is busy|
|23-16<br>—|Reserved|
|15<br>SARF|SMBus Alert Response Flag<br>• SARF is cleared by reading theSlave Address Status (SASR)register<br>• SARF cannot generate an asynchronous wakeup<br>0b - SMBus Alert Response is disabled or not detected<br>1b - SMBus Alert Response is enabled and detected|
|14<br>GCF|General Call Flag<br>Indicates whether a slave has detected the General Call Address.<br>• General Call Flag is cleared by reading theSlave Address Status (SASR)register<br>• General Call Flag cannot generate an asynchronous wakeup<br>0b - Slave has not detected the General Call Address or the General Call Address is disabled<br>1b - Slave has detected the General Call Address|
|13<br>AM1F|Address Match 1 Flag<br>Indicates that the received address has matched the ADDR1 field or ADDR0 to ADDR1 range as<br>configured bySCFGR1[ADDRCFG].<br>• Address Match 1 Flag is cleared by reading theSlave Address Status (SASR)register<br>• Address Match 1 Flag cannot generate an asynchronous wakeup<br>0b - Have not received an ADDR1 or ADDR0/ADDR1 range matching address<br>1b - Have received an ADDR1 or ADDR0/ADDR1 range matching address|
|12|Address Match 0 Flag|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2513 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|AM0F|Indicates that the received address has matched the ADDR0 field as configured by<br>SCFGR1[ADDRCFG].<br>• AM0F is cleared by reading theSlave Address Status (SASR)register<br>• AM0F cannot generate an asynchronous wakeup<br>0b - Have not received an ADDR0 matching address<br>1b - Have received an ADDR0 matching address|
|11<br>FEF|FIFO Error Flag<br>FEF can only be set when clock stretching is disabled.<br>0b - FIFO underflow or overflow was not detected<br>1b - FIFO underflow or overflow was detected|
|10<br>BEF|Bit Error Flag<br>BEF sets if the LPI2C slave transmits a logic one and detects a logic zero on the I2C bus. The slave<br>ignores the rest of the transfer until the next (repeated) START condition.<br>0b - Slave has not detected a bit error<br>1b - Slave has detected a bit error|
|9<br>SDF|STOP Detect Flag<br>SDF sets when the LPI2C slave detects a STOP condition and if the LPI2C slave matched the last<br>address byte.<br>0b - Slave has not detected a STOP condition<br>1b - Slave has detected a STOP condition|
|8<br>RSF|Repeated Start Flag<br>RSF sets when the LPI2C slave detects a repeated START condition and if the LPI2C slave matched the<br>last address byte. The RSF does not set when the slave first detects a START condition.<br>0b - Slave has not detected a Repeated START condition<br>1b - Slave has detected a Repeated START condition|
|7-4<br>—|Reserved|
|3<br>TAF|Transmit ACK Flag<br>TAF is cleared by writing to theSlave Transmit ACK (STAR)register.<br>0b - Transmit ACK/NACK is not required<br>1b - Transmit ACK/NACK is required|
|2<br>AVF|Address Valid Flag|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2514 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||AVF is cleared by reading theSlave Address Status (SASR)register. WhenSCFGR1[RXCFG]= 1,<br>SSR[AVF]is also cleared by reading theSlave Receive Data (SRDR)register.<br>0b - Address Status Register is not valid<br>1b - Address Status Register is valid|
|1|Receive Data Flag|
|RDF|RDF is cleared by reading theSlave Receive Data (SRDR)register. WhenSCFGR1[RXCFG]= 1, RDF<br>is not cleared when reading theSlave Receive Data (SRDR)register and ifSSR[AVF]is set.<br>0b - Receive data is not ready<br>1b - Receive data is ready|
|0|Transmit Data Flag|
|TDF|TDF is cleared by writing the to theSlave Transmit Data (STDR)register. WhenSCFGR1[TXCFG]= 0<br>and if a NACK or a Repeated START or STOP condition is detected, then TDF is also cleared.<br>0b - Transmit data not requested<br>1b - Transmit data is requested|



#### 69.5.1.21 Slave Interrupt Enable (SIER) 

##### Offset 

|Register|Offset|
|---|---|
|SIER|118h|



##### Function 

SIER contains transmit and receive data interrupt enables; Start and Stop detect interrupt enables; and other slave interrupt enables. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/069_Low_Power_Inter-Integrated_Circuit_-LPI2C-/S32K3XXRM_数据表.pdf-2515-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>SARIE  GCIE  AM1IE  AM0IE  FEIE  BEIE  SDIE  RSIE  TAIE  AVIE  RDIE  TDIE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2515 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Fields 

|Field|Function|
|---|---|
|31-16<br>—|Reserved|
|15<br>SARIE|SMBus Alert Response Interrupt Enable<br>Enables interrupt for SMBus alert response.<br>0b - Disabled<br>1b - Enabled|
|14<br>GCIE|General Call Interrupt Enable<br>Enables interrupt for general call.<br>0b - Disabled<br>1b - Enabled|
|13|Address Match 1 Interrupt Enable|
|AM1IE|Enables interrupt for address match 1.<br>0b - Disabled<br>1b - Enabled|
|12|Address Match 0 Interrupt Enable|
|AM0IE|Enables interrupt for address match 0.<br>0b - Disabled<br>1b - Enabled|
|11<br>FEIE|FIFO Error Interrupt Enable<br>Enables interrupt for FIFO error.<br>0b - Disabled<br>1b - Enabled|
|10<br>BEIE|Bit Error Interrupt Enable<br>Enables interrupt for bit error.<br>0b - Disabled<br>1b - Enabled|
|9<br>SDIE|STOP Detect Interrupt Enable<br>Enables interrupt for STOP detect.<br>0b - Disabled<br>1b - Enabled|
|8|Repeated Start Interrupt Enable<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2516 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|RSIE|Enables interrupt for repeated start.<br>0b - Disabled<br>1b - Enabled|
|7-4<br>—|Reserved|
|3<br>TAIE|Transmit ACK Interrupt Enable<br>Enables interrupt for transmit ACK.<br>0b - Disabled<br>1b - Enabled|
|2<br>AVIE|Address Valid Interrupt Enable<br>Enables interrupt for valid address.<br>0b - Disabled<br>1b - Enabled|
|1<br>RDIE|Receive Data Interrupt Enable<br>Enables interrupt for receive data.<br>0b - Disabled<br>1b - Enabled|
|0<br>TDIE|Transmit Data Interrupt Enable<br>Enables interrupt for transmit data.<br>0b - Disabled<br>1b - Enabled|



#### 69.5.1.22 Slave DMA Enable (SDER) 

##### Offset 

|Register|Offset|
|---|---|
|SDER|11Ch|



##### Function 

SDER contains the transmit, request, and receive enables for DMA. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2517 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||||||0|||||||AVDE|RDDE|TDDE|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-3|Reserved|
|—||
|2|Address Valid DMA Enable|
|AVDE|The Address Valid DMA request is shared with the Receive Data DMA request. If both Address Valid<br>DMA request and Receive Data DMA request are enabled, then setSCFGR1[RXCFG]= 1, to allow the<br>DMA to read the address from theSlave Receive Data (SRDR)register.<br>0b - DMA request is disabled<br>1b - DMA request is enabled|
|1<br>RDDE|Receive Data DMA Enable<br>Enables receive data for DMA.<br>0b - DMA request is disabled<br>1b - DMA request is enabled|
|0|Transmit Data DMA Enable|
|TDDE|Enables transmit data for DMA.<br>0b - DMA request is disabled<br>1b - DMA request is enabled|



#### 69.5.1.23 Slave Configuration 1 (SCFGR1) 

##### Offset 

|Register|Offset|
|---|---|
|SCFGR1|124h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2518 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Function 

The Slave Configuration Register 1 should only be written when the I2C Slave is disabled. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||0||||0||||0||||ADDRCF|G|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|0||HSME|IGNAC|RXCF|TXCF|SAEN|GCEN||0||0|ACKS|TXDS|RXST|ADRS|
|W|||N|K|G|G|||||||TALL|TALL|ALL|TALL|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27|Reserved|
|—<br>26-24<br>—|Reserved|
|23-19<br>—<br>18-16<br>ADDRCFG|Reserved<br>Address Configuration<br>Configures the condition that causes an address to match.<br>000b - Address match 0 (7-bit)<br>001b - Address match 0 (10-bit)<br>010b - Address match 0 (7-bit) or Address match 1 (7-bit)<br>011b - Address match 0 (10-bit) or Address match 1 (10-bit)<br>100b - Address match 0 (7-bit) or Address match 1 (10-bit)<br>101b - Address match 0 (10-bit) or Address match 1 (7-bit)<br>110b - From Address match 0 (7-bit) to Address match 1 (7-bit)<br>111b - From Address match 0 (10-bit) to Address match 1 (10-bit)|
|15-14<br>—<br>13|Reserved<br>High Speed Mode Enable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2519 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|HSMEN|Enables detection of the High-Speed Mode master code of slave address 0000_1XX, but does not cause<br>an address match on this code. When set and any HS-mode master code is detected,SCR[FILTEN]and<br>SCFGR1[ACKSTALL]bits are ignored until the next STOP condition is detected.<br>0b - Disables detection of HS-mode master code<br>1b - Enables detection of HS-mode master code|
|12<br>IGNACK|Ignore NACK<br>When Ignore NACK is set, the LPI2C slave continues transfers after a NACK is detected. Ignore NACK<br>bit is required to be set in Ultra-Fast mode.<br>0b - Slave ends transfer when NACK is detected<br>1b - Slave does not end transfer when NACK detected|
|11<br>RXCFG|Receive Data Configuration<br>0b - Reading the Receive Data register returns received data and clears the Receive Data flag.<br>SeeMSR[RDF].<br>1b - Reading the Receive Data register when the Address Valid flag (SSR[AVF]) is set, returns<br>the Address Status register and clear the Address Valid flag. Reading the Receive Data register<br>when the Address Valid flag is clear, returns received data and clears the Receive Data flag<br>(MSR[RDF]). SeeSSR[AVF]andMSR[RDF].|
|10|Transmit Flag Configuration|
|TXCFG|The transmit data flag always asserts before a NACK is detected at the end of a slave-transmit transfer. This<br>can cause an extra word to be written to the transmit data FIFO.<br>• When TXCFG = 0, the Transmit Data register is automatically emptied when a slave-transmit<br>transfer is detected. This causes the transmit data flag to assert whenever a slave-transmit transfer<br>is detected, and causes the transmit data flag to negate at the end of the slave-transmit transfer.<br>• When TXCFG = 1, the Transmit Data flag asserts whenever the Transmit Data register is empty, and<br>the Transmit Data flag negates when the Transmit Data register is full. This allows the Transmit Data<br>register to be filled before a slave-transmit transfer is detected, but can cause the Transmit Data<br>register to be written before a NACK is detected on the last byte of a slave transmit transfer.<br>0b - Transmit Data Flag only asserts during a slave-transmit transfer when the Transmit Data<br>register is empty<br>1b - Transmit Data Flag asserts whenever the Transmit Data register is empty|
|9|SMBus Alert Enable|
|SAEN|Enables a match on an SMBus alert.<br>0b - Disables match on SMBus Alert<br>1b - Enables match on SMBus Alert|
|8|General Call Enable|
|GCEN|Enables a general call address.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2520 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - General Call address is disabled<br>1b - General Call address is enabled|
|7-5|Reserved|
|—<br>4|Reserved|
|—<br>3|ACK SCL Stall|
|ACKSTALL|Enables SCL clock stretching during slave-transmit address byte(s) and slave-receiver address and data<br>byte(s), to allow software to write theSlave Transmit ACK (STAR)register before the ACK or NACK is<br>transmitted. Clock stretching occurs when transmitting the 9th bit, and is therefore not compatible with High<br>Speed mode.<br>When ACKSTALL is enabled, there is no need to set either RX SCL Stall (SCFGR1[RXSTALL]) or Address<br>SCL Stall (SCFGR1[ADRSTALL]).<br>When ACKSTALL is enabled and there is an address match on the first byte of a 10-bit address,<br>SSR[AVF]sets allowing software to read the Received Address before writing to theSlave Transmit ACK<br>(STAR)register.<br>0b - Clock stretching is disabled<br>1b - Clock stretching is enabled|
|2|TX Data SCL Stall|
|TXDSTALL|Enables SCL clock stretching when theSSR[TDF]= 1 during a slave-transmit transfer. Clock stretching<br>occurs following the 9th bit, and is therefore compatible with High Speed mode.<br>0b - Clock stretching is disabled<br>1b - Clock stretching is enabled|
|1<br>RXSTALL|RX SCL Stall<br>Enables SCL clock stretching whenSSR[RDF]= 1 during a slave-receive transfer. Clock stretching<br>occurs following the 9th bit, and is therefore compatible with High Speed mode.<br>0b - Clock stretching is disabled<br>1b - Clock stretching is enabled|
|0|Address SCL Stall|
|ADRSTALL|Enables SCL clock stretching whenSSR[AVF]= 1. Clock stretching only occurs following the 9th bit, and<br>is therefore compatible with High Speed mode.<br>0b - Clock stretching is disabled<br>1b - Clock stretching is enabled|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2521 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

#### 69.5.1.24 Slave Configuration 2 (SCFGR2) 

##### Offset 

|Register|Offset|
|---|---|
|SCFGR2|128h|



##### Function 

The Slave Configuration Register 2 should only be written when the I2C Slave is disabled. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/069_Low_Power_Inter-Integrated_Circuit_-LPI2C-/S32K3XXRM_数据表.pdf-2522-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0<br>FILTSDA  FILTSCL<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>DATAVD  CLKHOLD<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-28|Reserved|
|—||
|27-24|Glitch Filter SDA|
|FILTSDA|Configures the I2C slave digital glitch filters for SDA input.<br>• A configuration of 0 disables the glitch filter<br>• Glitches equal to or less than FILTSDA cycles long are filtered out and ignored<br>• The latency through the glitch filter is equal to FILTSDA+3 cycles, and must be configured to be less<br>than the minimum SCL low or high period.<br>• The glitch filter cycle count is not affected by the PRESCALE configuration, and the glitch filter cycle<br>count is disabled in High Speed mode|
|23-20<br>—|Reserved|
|19-16|Glitch Filter SCL|
|FILTSCL|Configures the I2C slave digital glitch filters for SCL input.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2522 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||• A configuration of 0 disables the glitch filter<br>• Glitches equal to or less than FILTSCL cycles long are filtered out and ignored<br>• The latency through the glitch filter is equal to FILTSCL+3 cycles, and must be configured to be less<br>than the minimum SCL low or high period<br>• The glitch filter cycle count is not affected by the PRESCALE configuration, and the glitch filter cycle<br>count is disabled in High Speed mode|
|15-14<br>—|Reserved|
|13-8<br>DATAVD|Data Valid Delay<br>Configures the SDA data valid delay time for the I2C slave, which is equal to FILTSCL+DATAVD+3<br>cycles.<br>• The data valid delay must be configured to be less than the minimum SCL low period<br>• The I2C slave data valid delay time is not affected by the PRESCALE configuration, and the I2C<br>slave data valid delay time is disabled in High Speed mode|
|7-4<br>—<br>3-0|Reserved<br>Clock Hold Time|
|CLKHOLD|Configures the minimum clock hold time for the I2C slave, when clock stretching is enabled.<br>• The minimum hold time is equal to CLKHOLD+3 cycles<br>• The I2C slave clock hold time is not affected by the PRESCALE configuration, and the I2C slave<br>clock hold time is disabled in high speed mode|



#### 69.5.1.25 Slave Address Match (SAMR) 

##### Offset 

|Register|Offset|
|---|---|
|SAMR|140h|



##### Function 

The SAMR should only be written when the I2C Slave is disabled. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2523 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||0|||||||ADD|R1|||||0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||0|||||||ADD|R0|||||0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-27<br>—|Reserved|
|26-17<br>ADDR1|Address 1 Value<br>Compared against the received address to detect the Slave Address.<br>• In 10-bit mode, the first address byte is compared to { 11110, ADDR1[26:25] } and the second<br>address byte is compared to ADDR1[24:17]<br>• In 7-bit mode, the address is compared to ADDR1[23:17]|
|16-11<br>—|Reserved|
|10-1<br>ADDR0|Address 0 Value<br>Compared against the received address to detect the Slave Address.<br>• In 10-bit mode, the first address byte is compared to { 11110, ADDR0[10:9] } and the second<br>address byte is compared to ADDR0[8:1]<br>• In 7-bit mode, the address is compared to ADDR0[7:1]<br>•|
|0<br>—|Reserved|



#### 69.5.1.26 Slave Address Status (SASR) 

##### Offset 

|Register|Offset|
|---|---|
|SASR|150h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2524 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Function 

##### SASR contains the read-only RADDR and ANV fields. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|0|ANV||0|||||||RADDR||||||
|W|||||||||||||||||
|Reset|0|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-15|Reserved|
|—<br>14<br>ANV|Address Not Valid<br>0b - Received Address (RADDR) is valid<br>1b - Received Address (RADDR) is not valid|
|13-11<br>—|Reserved|
|10-0|Received Address|
|RADDR|The Received Address updates wheneverSSR[AM0F]orSSR[AM1F]are set. SSR[AM0F] or<br>SSR[AM1F] are cleared by reading the Slave Address Status register.<br>• In 7-bit mode, the address byte is stored in RADDR[7:0]<br>• In 10-bit mode, the first address byte is { 11110, RADDR[10:9], RADDR[0] } and the second address<br>byte is RADDR[8:1]. The R/W bit is therefore always stored in RADDR[0]<br>• WhenSCFGR1[ACKSTALL]is set, if the first address byte matches in 10-bit mode, then the first<br>address byte is stored in RADDR[7:0] so software can read the Received Address before writing<br>the Transmit ACK. The Received Address then updates with the full 10-bit address if the second<br>address byte matches.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2525 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

#### 69.5.1.27 Slave Transmit ACK (STAR) 

##### Offset 

|Register|Offset|
|---|---|
|STAR|154h|



##### Function 

STAR can only be written when the ACK SCL Stall bit is set (SCFGR1[ACKSTALL]). 

- The SCFGR1[ACKSTALL] bit enables clock stretching during the ACK/NACK bit slot, and during this time, the STAR register can be written by software. 

- The logic ensures that the clock stretching continues for at least 1 bus clock cycle after the STAR register is updated. 

- This clock stretching time can be extended more using the Clock Hold Time field (SCFGR2[CLKHOLD]). 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/069_Low_Power_Inter-Integrated_Circuit_-LPI2C-/S32K3XXRM_数据表.pdf-2526-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 TXNA<br>W CK<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-1|Reserved|
|—||
|0|Transmit NACK|
|TXNACK|After receiving each word, software can transmit either an ACK (logic 0) or a NACK (logic 1); Transmit<br>NACK selects which to use: ACK or NACK.<br>• WhenSCFGR1[ACKSTALL]is set, a Transmit NACK must be written once for each matching<br>address byte and each received word. ACKSTALL must be set, because that stalls the data transfer<br>until software reads the received word (and decides whether to respond with an ACK or NACK).<br>• To configure the default ACK/NACK, Transmit NACK can also be written when LPI2C Slave is<br>disabled or idle.|
||0b - Write a Transmit ACK for each received word|
||1b - Write a Transmit NACK for each received word|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2526 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

#### 69.5.1.28 Slave Transmit Data (STDR) 

##### Offset 

|Register|Offset|
|---|---|
|STDR|160h|



##### Function 

Clock stretching (enabled or disabled) affects when the transmit data is transferred. The SCFGR1[TXDSTALL] bit enables clock stretching during the 1st data bit of a slave-transmit transfer. 

- If clock stretching is enabled (SCFGR1[TXDSTALL] = 1) , then the transmit data transfer is stalled until the STDR is updated. Clock stretching is extended by at least 1 bus clock cycle after STDR is updated, and clock stretching can be delayed even more using the Clock Hold Time field (SCFGR2[CLKHOLD]. 

- If clock stretching is disabled (SCFGR1[TXDSTALL] = 0) , then the transmit data should be written before the start of the slave-transmit transfer; otherwise (that is, if the transmit data is not written before the start of the slave-transmit transfer), the FIFO Error Flag (SSR[FEF]) sets. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/069_Low_Power_Inter-Integrated_Circuit_-LPI2C-/S32K3XXRM_数据表.pdf-2527-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>W 0<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>W 0 DATA<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-8|Reserved|
|—||
|7-0|Transmit Data|
|DATA|Writing to the Slave Transmit Data Register (STDR) stores I2C slave transmit data in the Slave Transmit<br>Data Register|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2527 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

#### 69.5.1.29 Slave Receive Data (SRDR) 

##### Offset 

|Register|Offset|
|---|---|
|SRDR|170h|



##### Function 

Reading the Slave Receive Data Register returns the data received by the I2C slave. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/069_Low_Power_Inter-Integrated_Circuit_-LPI2C-/S32K3XXRM_数据表.pdf-2528-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>RXEM<br>R SOF  0 RADDR  DATA<br>PTY<br>W<br>Reset 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16|Reserved|
|—||
|15|Start Of Frame|
|SOF|Indicates whether this is the first data word.<br>0b - Indicates this is not the first data word since a (repeated) START or STOP condition<br>1b - Indicates this is the first data word since a (repeated) START or STOP condition|
|14|Receive Empty|
|RXEMPTY|Gives the empty status of the receive data register.<br>0b - The Receive Data Register is not empty<br>1b - The Receive Data Register is empty|
|13-11<br>—|Reserved|
|10-8|Received Address|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2528 / 4640 

NXP Semiconductors 

Low Power Inter-Integrated Circuit (LPI2C) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|RADDR|When bothSCFGR1[RXCFG]andSSR[AVF]are set, theAddress Status Register (SASR[RADDR])bits<br>[10:8] are returned. Otherwise this field returns zero.|
|7-0|Receive Data|
|DATA|Contains data received by the I2C slave. When bothSCFGR1[RXCFG]andSSR[AVF]are set, theAddress<br>Status Register (SASR[RADDR])bits [7:0] are returned.|



## 69.6 Glossary 

HREQ Host request SCL Serial clock line SCLS Secondary serial clock line SDA Serial data line SDAS Secondary serial data line 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2529 / 4640 

