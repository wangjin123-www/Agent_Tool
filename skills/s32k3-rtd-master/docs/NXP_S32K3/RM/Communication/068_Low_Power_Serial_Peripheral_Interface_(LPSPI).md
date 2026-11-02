NXP Semiconductors 

# Chapter 68 Low Power Serial Peripheral Interface (LPSPI) 

## 68.1 Chip-specific LPSPI information 

### 68.1.1 LPSPI instances and configuration 

Table 377. LPSPI instances 

|Instance|S32K314/S32K324/S32K344/S32K358|S32K311/S32K312/S32K322/S32K342|
|---|---|---|
|LPSPI0|Yes|Yes|
|LPSPI1|Yes|Yes|
|LPSPI2|Yes|Yes|
|LPSPI3|Yes|Yes|
|LPSPI4|Yes|No|
|LPSPI5|Yes|No|



Table 378. LPSPI instances configuration 

|Instances|TX FIFO Size|RX FIFO Size|Chip Selects|
|---|---|---|---|
|LPSPI0|4x32 bit|4x32 bit|8|
|LPSPI1|4x32 bit|4x32 bit|6|
|LPSPI2|4x32 bit|4x32 bit|4|
|LPSPI3|4x32 bit|4x32 bit|4|
|LPSPI4|4x32 bit|4x32 bit|4|
|LPSPI5|4x32 bit|4x32 bit|4|



- S32K314, S32K324, S32K344, S32K322, and S32K342 supports data rate up to 20 Mbps, S32K312 and S32K311 supports data rate up to 15 Mbps. Only one LPSPI instance support 20 MHz in loopback mode that is LPSPI0 

- All LPSPIs supports a minimum a 10 MHz data rate on standard plus pads and 7.5 MHz on standard pads. 

- Low leakage and Wait modes are not supported in this device. 

The number of chip selects that each LPSPI instance supports varies. Because of that, in the Configuration Register 1 (CFGR1), the Peripheral Chip Select (PCS) field and the Peripheral Chip Select Polarity (PCSPOL) field also vary. See the next 2 tables. 

Table 379. LPSPI instances mapped against Peripheral Chip Select (PCS) field support 

|PCS supported in|PCS not supported in|
|---|---|
|LPSPI0_TCR[26-24]|—|
|LPSPI1_TCR[26-24]|—|
|LPSPI2_TCR[25–24]|LPSPI2_TCR[26]|
|LPSPI3_TCR[25–24]|LPSPI3_TCR[26]|
|LPSPI4_TCR[25–24]|LPSPI4_TCR[26]|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2421 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

Table 379. LPSPI instances mapped against Peripheral Chip Select (PCS) field support (continued) 

|PCS supported in|PCS not supported in|
|---|---|
|LPSPI5_TCR[25–24]|LPSPI5_TCR[26]|



Table 380. LPSPI instances mapped against Peripheral Chip Select Polarity (PCSPOL) field support 

|PCSPOL supported in|PCSPOL not supported in|
|---|---|
|LPSPI0_CFGR1[15-8]|—|
|LPSPI1_CFGR1[13–8]|LPSPI1_CFGR1[15–14]|
|LPSPI2_CFGR1[11–8]|LPSPI2_CFGR1[15–12]|
|LPSPI3_CFGR1[11–8]|LPSPI3_CFGR1[15–12]|
|LPSPI4_CFGR1[11–8]|LPSPI4_CFGR1[15–12]|
|LPSPI5_CFGR1[11–8]|LPSPI5_CFGR1[15–12]|



### 68.1.2 LPSPI HREQ considerations for S32K314, S32K324 and S32K344 

It is recommended that the HREQ pin (when PCS[1] is used as HREQ) should get de-asserted before the completion of frame transfer. In case if the HREQ state is still asserted and LPSPI returns to idle state after frame transfer completion, the HREQ state is internally latched and the next data is written to the transmit FIFO without waiting for the next HREQ assertion. 

This limitation is present only while using PCS[1] as HREQ and HREQ remains asserted throughout frame transfer. In case of using trigger input as HREQ, there is no issue. 

## 68.2 Overview 

LPSPI provides an efficient interface to a SPI bus, either as a master or slave. A SPI bus is a synchronous serial communication interface used in embedded systems. It is typically used to perform short distance communications between microcontrollers and peripheral devices, on printed circuit boards. Typical applications include interfacing to Secure Digital cards and LCD displays. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2422 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

### 68.2.1 Block diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/068_Low_Power_Serial_Peripheral_Interface_-LPSPI-/S32K3XXRM_数据表.pdf-2423-03.png)


<!-- Start of picture text -->
Internal chip External<br>peripheral bus LPSPI SPI Interface<br>Trigger<br>Configuration<br>registers<br>HREQ<br>SCK<br>Command/TX Control<br>FIFO Iogic<br>PCS[ n :0]<br>SCK and PCS[ n :0]<br>are inputs in Slave mode,<br>and are outputs in Master mode<br>RX<br>FIFO Shift<br>register<br>SIN<br>SOUT<br>Bus clock By default, SIN is input and SOUT is output,<br>Functional clock but SIN/SOUT can be configured differently.<br>Either SIN or SOUT can be used for single wire.<br>External clock<br><!-- End of picture text -->

Figure 361. Block diagram 

### 68.2.2 Features 

- Requires minimal CPU overhead, with DMA offloading of FIFO register accesses 

- Supports DMA accesses and generates DMA requests 

- 32-bit word size 

- Configurable clock polarity and phase 

- Master mode—supports 8 peripheral chip selects 

- Slave mode 

- 4-word transmit and command FIFO 

- 4-word receive FIFO 

- Flexible timing parameters in Master mode, including SCK frequency and duty cycle, and delays between PCS and SCK edges 

- Continuous transfer option to keep PCS asserted across multiple frames 

- Full-duplex transfers support 1-bit transmit and receive on each clock edge 

- Half-duplex transfers support: 

   - 1-bit transmit or receive on each clock edge 

   - 2-bit transmit or receive on each clock edge 

   - 4-bit transmit or receive on each clock edge 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2423 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

   - 8-bit transmit or receive on each clock edge 

- Can use host request to control the start of a SPI bus transfer 

## 68.3 Functional description 

### 68.3.1 Master mode 

#### 68.3.1.1 Transmit and command FIFO commands 

The transmit and command FIFO is a combined FIFO that includes both transmit data words and command words. 

- You store transmit data words to the transmit and command FIFO, by writing to Transmit Data (TDR). 

- You store command words to the transmit and command FIFO, by writing to Transmit Command (TCR). 

When a command word is at the top of the transmit and command FIFO, the actions that can occur depend upon whether the LPSPI module is busy or between frames. See TCR[CONT] and TCR[CONTC]. 

Table 381. Possible actions when a command word is at the top of the transmit and command FIFO 

|Condition|Action|
|---|---|
|LPSPI is enabled and idle|The command word is pulled from the FIFO, and that command word controls all<br>subsequent transfers.|
|LPSPI is busy and the Continuing<br>Command field (TCR[CONTC]) is 0|The SPI frame completes at the end of the existing word, ignoring<br>TCR[FRAMESZ]. The command word is then pulled from the FIFO and that<br>command word controls all subsequent transfers (or until the next update to<br>the command word). Note that a command word with TCR[CONTC] = 0 always<br>terminates the existing transfer regardless of the previous TCR[CONT] value.|
|LPSPI is busy, the existing TCR[CONT]<br>value is 1 and the new TCR[CONTC]<br>value is 1|The command word must be updated at the frame boundary. The command word<br>is pulled from the FIFO during the last SCK pulse of the existing frame (based<br>on the FRAMESZ value), and the frame continues using the new command value<br>for the rest of the frame (or until the next update to the command word). When<br>TCR[CONTC] = 1, only the lower 24-bits of the command word are updated. If the<br>command word is updated at a word boundary, then the transfer halts (stops) after<br>that word. TCR[CONTC] is ignored when not at a frame boundary, so the frame<br>ends prematurely.|



About TCR[CONT] and TCR[CONTC]: 

- TCR[CONT] = 1 keeps PCS asserted at end of frame, allowing the transfer to continue. 

- TCR[CONTC] = 1 specifies that this command word should not terminate the existing frame, and the transfer can continue using the new command word. 

TCR[CONTC] = 1 is restricted in the sense that the new command must load on a frame boundary, and the only way for a transfer to continue from a frame boundary is when the previous command has TCR[CONT] = 1. 

You can read the current state of the existing command word from Transmit Command (TCR). It requires at least 3 LPSPI functional clock cycles for TCR to update after TCR is written (assuming an empty FIFO), and LPSPI must be enabled (CR[MEN] = 1). 

Writing the TCR does not initiate a SPI bus transfer, unless the TCR[TXMSK] = 1. When the TCR[TXMSK] = 1, a new command word is not loaded until the end of the existing frame (based on the TCR[FRAMESZ] value); at the end of the transfer, TCR[TXMSK] transitions to 0. 

In Master mode, the LPSPI command word in TCR controls SPI attributes based on selections in register fields. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2424 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

Table 382. Command word in Master mode 

|Transmit|Command (TCR)|Description|Can this field<br>|
|---|---|---|---|
|Field|Name||be modified<br>during a data<br>transfer?|
|CPOL|Clock polarity|Specifies the polarity of the SCK pin. Any change of CPOL value causes<br>a transition on the SCK pin.|N|
|CPHA|Clock phase|Specifies the clock phase of the transfer.|N|
|PRESCALE|Prescaler value|Specifies a prescaler used to divide the LPSPI functional clock, to<br>generate the timing parameters of the SPI bus transfer. Changing<br>PRESCALE in conjunction with PCS enables the LPSPI module to<br>connect to different slave devices at different frequencies.|N|
|PCS|Peripheral chip<br>select|Specifies which PCS pin asserts for the transfer; the polarity of PCS is<br>static and specified byCFGR1[PCSPOL].<br>IfCFGR1[PCSCFG]= 1, do not select PCS[3:2].|N|
|LSBF|LSB first|Specifies whether LSB (bit 0) or MSB (bit 31 for a 32-bit word) is<br>transmitted or received first.|Y|
|BYSW|Byte swap|Enables byte swap on each 32-bit word when transmitting and receiving<br>data. Byte swapping can be useful when interfacing to devices that<br>organize data as big-endian.|Y|
|CONT|Continuous transfer|Configures LPSPI for a continuous transfer that keeps PCS asserted<br>between frames (as specified by FRAMESZ). You must write a new<br>command word to cause PCS to negate. Also supports changing the<br>command word at the frame size boundaries.|Y|
|CONTC|Continuing<br>command|Indicates that this is a new command word for the existing continuous<br>transfer. When CONTC = 1, the command word must only be written to<br>the transmit and command FIFO on a frame boundary.|Y|
|RXMSK|Receive data mask|Masks the receive data and does not store the masked receive data to<br>the receive FIFO or perform receive data matching. This option is useful<br>for half-duplex transfers or to specify which fields are compared during<br>receive data matching.|Y|
|TXMSK|Transmit data mask|Masks the transmit data; masked transmit data is not pulled from the<br>transmit FIFO, and the output data pin is 3-stated (unless otherwise<br>configured byCFGR1[OUTCFG]). This option is useful for half-duplex<br>transfers.|Y|
|WIDTH|Transfer width|Specifies the number of bits shifted on each SCK pulse.<br>• 1-bit transfers support traditional SPI bus transfers in either half-<br>duplex or full-duplex data formats.<br>• 2-bit and 4-bit half-duplex transfers are useful for interfacing to<br>QuadSPI memory devices, and either TXMSK or RXMSK must also<br>be 1.<br>• 8-bit half-duplex transfers are useful for interfacing to OctelSPI<br>memory devices, and at least one of TXMSK or RXMSK must also<br>be 1.<br>Table continues on the next page...|Y|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2425 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

##### Table 382. Command word in Master mode (continued) 

|Transmit C|ommand (TCR)|Description|Can this field<br>|
|---|---|---|---|
|Field|Name||be modified<br>during a data<br>transfer?|
|FRAMESZ|Frame size|Configures the frame size in number of bits equal to (FRAMESZ + 1).<br>• The minimum frame size is 8 bits, or 16 bits for an 8-bit transfer.<br>• If the frame size is larger than 32 bits, then the frame is divided<br>into multiple words of 32 bits; each word is loaded from the transmit<br>FIFO and stored in the receive FIFO separately.<br>• If the size of the frame is not divisible by 32, then the last load of the<br>transmit FIFO and store of the receive FIFO contains the remaining<br>bits. For example, a 72-bit transfer consists of 3 words: the first and<br>second words are 32 bits, and the third word is 8 bits.|Y|



#### 68.3.1.1.1 SPI bus transfers 

LPSPI initiates a SPI bus transfer when all of the following conditions are true: 

- Data is written to the transmit FIFO. 

- The HREQ pin is asserted (or the HREQ function is disabled). 

- LPSPI is enabled. 

To perform the SPI bus transfer, LPSPI uses the attributes configured in Transmit Command (TCR) and uses the timing parameters in Clock Configuration (CCR). 

The SPI bus transfer ends after the number of bits indicated by the FRAMESZ value have been transferred (provided CONT = 0), or at the end of a word when a new transmit command word is at the top of the transmit and command FIFO. When LPSPI is disabled, the SPI bus transfers end after the transmit FIFO is empty and LPSPI is idle. 

The HREQ input is only checked when PCS is negated. 

#### 68.3.1.1.2 Circular FIFO 

The transmit and command FIFO supports a circular FIFO feature. This feature enables the LPSPI master to (periodically) repeat a short data transfer that fits within the transmit and command FIFO, without requiring additional FIFO accesses. When the circular FIFO is enabled (CFGR0[CIRFIFO] = 1), the current state of the FIFO read pointer is saved and the status flags do not update. After the FIFO is empty and LPSPI is idle, the FIFO read pointer is restored with the saved version, so the contents of the transmit and command FIFO are not permanently pulled from the FIFO while Circular FIFO mode is enabled. 

#### 68.3.1.2 Receive FIFO and data match 

The receive FIFO stores received data during SPI bus transfers. When TCR[RXMSK] = 1, the received data is discarded instead of being stored in the receive FIFO. 

- Received data is written to the receive FIFO when the last bit of the word is sampled. 

- If the transmit FIFO is empty during a multiple-word or continuous transfer, then the receive data is written to the receive FIFO before the transfer stalls (assuming CFGR1[NOSTALL] = 0) while waiting for new transmit data or for a command word to be written. 

LPSPI provides a receive data match function that can match received data against one of two words in DMR0 and DMR1, or against a masked data word. The received data match function can also be configured to compare only the first one or two received data words since the start of the frame. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2426 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

- Received data that is already discarded due to the TCR[RXMSK] field cannot cause the data match flag to set, and delays the receive data match on the first received data word, until all discarded data is received. 

- You can configure the receive data match function to discard all received data until a data match is detected, using CFGR0[RDMO]. 

- After a receive data match, to allow all subsequent data to be received, write 0 to the CFGR0[RDMO] field, then write 0 to SR[DMF]. 

#### 68.3.1.3 Timing parameters 

The timing parameters that are used for all SPI bus transfers are relative to the LPSPI functional clock divided by the TCR[PRESCALE] selection. Although you cannot change Clock Configuration (CCR) when the LPSPI module is busy, to support interfacing to different slave devices at different frequencies, you can change the TCR[PRESCALE] selection between SPI bus transfers using Transmit Command (TCR). 

~~<mark>NOTE</mark>~~ 

The minimum value below is the minimum counter value, but the clock configuration register values must also satisfy the data sheet specs based on the LPSPI functional clock frequency and prescaler value. 

Table 383. Timing parameters 

|Clock Confi|guration (CCR)|Description|Min|Max|
|---|---|---|---|---|
|Clock Config<br>|uration 1 (CCR1)<br>||||
|Field|Name||||
|SCKSET|SCK setup<br>phase|Configures the SCK setup phase to (SCKSET + 1)<br>cycles. The setup phase is the SCK high period<br>when either CPHA = 0 and CPOL = 1, or<br>CPHA = 1 and CPOL = 0. Otherwise, it is the<br>SCK low period. The SCK period is defined as<br>(SCKSET + SCKHLD + 2) and the duty cycle is the<br>difference between SCKSET and SCKHLD.|0 (1 cycle)|255 (256<br>cycles)|
|SCKHLD|SCK hold phase|Configures the SCK hold phase to (SCKHLD + 1)<br>cycles. The hold phase is the SCK low period when<br>either CPHA = 0 and CPOL = 1, or CPHA = 1 and<br>CPOL = 0. Otherwise, it is the SCK high period. The<br>SCK period is defined as (SCKSET + SCKHLD + 2)<br>and the duty cycle is the difference between<br>SCKSET and SCKHLD.|0 (1 cycle)|255 (256<br>cycles)|
|PCSPCS|PCS-to-PCS<br>delay|Configures the minimum delay between PCS<br>negation and the next PCS assertion to<br>(PCSPCS + PCSPCS + 2) cycles. When the<br>command word is updated between transfers, there<br>is a minimum of (PCSPCS + 1) cycles between the<br>command word update and any change on PCS<br>pins.|0 (2 cycles)|255 (512<br>cycles)|
|SCKSCK|SCK-to-SCK<br>delay|Configures the delay during a continuous transfer<br>between the last SCK edge of a frame and the first<br>SCK edge of the continuing frame to (SCKSCK + 1)<br>cycles. This is useful when the external slave|0 (1 cycle)|255 (256<br>cycles)|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2427 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

##### Table 383. Timing parameters (continued) 

|Clock Config|uration (CCR)|Description|Min|Max|
|---|---|---|---|---|
|Clock Configu|ration 1 (CCR1)||||
|Field|Name||||
|||requires a large delay between different words of an<br>SPI bus transfer.|||
|PCSSCK|PCS-to-SCK<br>delay|Configures the minimum delay between PCS<br>assertion and the first SCK edge to (PCSSCK + 1)<br>cycles.|0 (1 cycle)|255 (256<br>cycles)|
|SCKPCS|SCK-to-PCS<br>delay|Configures the minimum delay between the last<br>SCK edge and the PCS negation to (SCKPCS + 1)<br>cycles.|0 (1 cycle)|255 (256<br>cycles)|



This figure shows the timing settings controlled by: 

- TCR[CPHA] 

- TCR[CPOL] 

- CCR[SCKPCS] 

- CCR[PCSSCK] 

- CCR1[SCKSET] 

- CCR1[SCKHLD] 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2428 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/068_Low_Power_Serial_Peripheral_Interface_-LPSPI-/S32K3XXRM_数据表.pdf-2429-01.png)


<!-- Start of picture text -->
Low Power Serial Peripheral Interface (LPSPI)<br>SCK SCK SCK<br>CPHA = 0 PCSSCK SET HLD PCS<br>(CPOL = 0) SCK<br>(CPOL = 1) SCK<br>PCS<br>SDO MSB LSB<br>SDI MSB LSB<br>Data frame<br>Data is sampled internally<br>on odd clock edges.<br>SCK SCK SCK<br>CPHA = 1 PCSSCK SET HLD PCS<br>(CPOL = 0) SCK<br>(CPOL = 1) SCK<br>PCS<br>SDO MSB LSB<br>SDI MSB LSB<br>Data frame<br>Data is sampled internally<br>on even clock edges.<br>Figure 362. Clock phase (TCR[CPHA]) timing diagram example<br><!-- End of picture text -->

#### 68.3.1.4 Pin configuration 

- To swap directions or support half-duplex transfers on the same pin, you can configure the SIN and SOUT pins using CFGR1[PINCFG]. 

- To specify whether an output data pin (SOUT, for example) 3-states when PCS is negated, or if the output data pin retains the last value, use CFGR1[OUTCFG]. 

- When configuring for half-duplex transfers, you must configure the output data pins to 3-state when PCS is negated (CFGR1[OUTCFG] = 1). 

- When performing half-duplex 2-bit transfers, you can set CFGR1[PCSCFG] to any value. 

- When performing half-duplex 4-bit transfers, you must set CFGR1[PCSCFG] to 1h. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2429 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

#### 68.3.1.5 Clock loopback 

Configure the LPSPI master to use one of the following clocks to sample the input data: 

- The SCK output clock 

- A delayed version of the SCK output clock 

The delayed version of the SCK is chosen by the SCK pin output delay, plus the SCK pin input delay, and is selected by writing 1 to CFGR1[SAMPLE]. Enabling the loopback version of the SCK can improve the setup time of the input data from the slave. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/068_Low_Power_Serial_Peripheral_Interface_-LPSPI-/S32K3XXRM_数据表.pdf-2430-07.png)


<!-- Start of picture text -->
LPSPI master SPI slave<br>SIN<br>MISO<br>SCK<br>SCK input<br>0<br>delayed SCK<br>1<br>CFGR1[SAMPLE]<br><!-- End of picture text -->

Figure 363. Clock loopback 

See the chip data sheet for the specific input setup time in Master Loopback mode. 

### 68.3.2 Slave mode 

LPSPI slave mode: 

- Uses the same shift register and logic that master mode uses. 

- Does not use Clock Configuration Register (CCR). 

- Requires that Transmit Command (TCR) remain static (unchanging) during SPI bus transfers. 

#### 68.3.2.1 Transmit and command FIFO commands 

Before enabling LPSPI in Slave mode, initialize Transmit Command (TCR), although TCR does not update until after LPSPI is enabled. After LSPI is enabled, only change TCR when LPSPI is idle. In Slave mode, the LPSPI command word in TCR controls SPI attributes. Before the PCS input asserts, the transmit FIFO must be filled with transmit data, or the transmit error flag sets. 

Table 384. Command word in Slave mode 

|Transmit C|ommand (TCR)|Description|
|---|---|---|
|Field|Name||
|CPOL|Clock polarity|Specifies the polarity of the external SCK input.|
|CPHA|Clock phase|Specifies the clock phase of transfer.|
|PRESCALE|Prescaler value|Specifies the LPSPI functional clock prescaler.|
|PCS|Peripheral chip<br>select|Specifies which PCS is used. The polarity of PCS is static and configured<br>byCFGR1[PCSPOL].|
|||IfCFGR1[PCSCFG]is not equal to zero, then do not select the PCS[3:2] pins.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2430 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

Table 384. Command word in Slave mode (continued) 

|Transmit<br>Field|Command (TCR)<br>Name|Description|
|---|---|---|
|LSBF|LSB first|Specifies whether LSB (bit 0) or MSB (bit 31 for a 32-bit word) is transmitted or<br>received first.|
|BYSW|Byte swap|Enables byte swap on each 32-bit word when transmitting and receiving data. Byte<br>swapping can be useful when interfacing to devices that organize data as big-endian.|
|CONT|Continuous transfer|When continuous transfer is selected in Slave mode, after the number of bits indicated<br>by FRAMESZ are transferred, the LPSPI will passthrough and transmit the received<br>data until the next PCS negation. Whatever is shifted in on the receive data is shifted<br>out as transmit data as if there were a 32-bit shift register.|
|CONTC|Continuing<br>command|When continuing command is enabled in Slave mode, after the number of bits indicated<br>by FRAMESZ are transferred, then RXMSK is considered equal to 1 and TXMSK is<br>considered equal to 0 until the next PCS negation. CONTC can be used to change the<br>direction of a transfer after the number of bits indicated by FRAMESZ.|
|RXMSK|Receive data mask|Masks the receive data; LPSPI does not store masked receive data to the receive FIFO<br>or perform receive data matching. This option is useful for half-duplex transfers or to<br>specify which fields are compared during receive data matching.|
|TXMSK|Transmit data mask|Masks the transmit data, so that the masked transmit data is not pulled from<br>transmit FIFO, and the output data pin is 3-stated (unless otherwise specified by<br>CFGR1[OUTCFG]). This option is useful for half-duplex transfers.|
|WIDTH|Transfer width|Specifies the number of bits shifted on each SCK pulse.<br>• 1-bit transfers support traditional SPI bus transfers in either half-duplex or full-<br>duplex data formats.<br>• 2-bit and 4-bit half-duplex transfers are useful for interfacing to QuadSPI memory<br>devices, and at least one of TCR[TXMSK] or TCR[RXMSK] must be 1.<br>• 8-bit half-duplex transfers are useful for interfacing to OctelSPI memory devices,<br>and at least one of Transmit Data Mask (TCR[TXMSK] or Receive Data Mask<br>TCR[RXMSK]) must also be 1.|
|FRAMESZ|Frame size|Specifies the frame size in number of bits equal to (FRAMESZ + 1).<br>• The minimum frame size is 8 bits, or 16 bits for an 8-bit parallel transfer.<br>• If the frame size is larger than 32 bits, then the frame is divided into multiple words<br>of 32 bits; each word is loaded from the transmit FIFO and stored in the receive<br>FIFO separately.<br>• If the size of the frame is not divisible by 32, then the last load of the transmit FIFO<br>and store of the receive FIFO contain the remainder bits. For example, a 72-bit<br>transfer consists of 3 words: the first and second words are 32 bits, and the third<br>word is 8 bits.|



#### 68.3.2.2 Receive FIFO and data match 

The receive FIFO stores receive data during SPI bus transfers. When TCR[RXMSK] = 1, the received data is discarded instead of storing the received data in the receive FIFO. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2431 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

Receive data supports a receive data match function that can match received data against one of two words in the DMR0 and DMR1 registers or against a masked data word. The data match function can also be configured to compare only the first one or two received data words since the start of the frame. 

- Received data that is already discarded because TCR[RXMSK] = 1 cannot cause the data match to set, and delays the match on the first received data word, until all discarded data is received. 

- The receiver match function can also be configured to discard all received data until a data match is detected, using the CFGR0[RDMO] bit. 

- After a receive data match, to allow all subsequent data to be received, first clear the CFGR0[RDMO] bit, then clear the SR[DMF] bit. 

#### 68.3.2.3 Partial received word 

When the PCS pin deasserts and the receive shift register has shifted in a partial word, the receive shift register can be configured to either discard the partial word or to store it in the receive FIFO. You specify this using CFGR1[PARTIAL]. 

A partial word is defined as less than FRAMESZ bits (when FRAMESZ is equal or less than 32 bits, or it is the last word in a multi-word frame) or less than 32 bits (when FRAMESZ is greater than 32 bits and not the last word in a multi-word frame). 

A single-bit frame is not supported. A partial received word of 1 bit is fine, but a partial received frame of 1 bit is not supported. 

#### 68.3.2.4 Clocked interface 

LPSPI supports interfacing to external masters that provide only clock and data pins (PCS is not required). This interface requires: 

- Writing 1 to TCR[CPHA] (data is changed on the leading edge of SCK and captured on the following edge). 

- Configuring the PCS input to be always asserted (CFGR1[PCSPOLn] = 1). For example, to configure PCS[0] to be always asserted, write 1 to PCSPOL[0], and do not configure PCS[0] in the pin muxing. The chip-level drives PCS to a certain value (ideally 1), CFGR1[PCSPOLn] could be used to invert that value. 

- Writing 1 to CFGR1[AUTOPCS] to enable automatic PCS generation. When CFGR1[AUTOPCS] = 1, a minimum of four LPSPI functional clock cycles (divided by the TCR[PRESCALE] selection) is required between the last SCK edge of one word and the first SCK edge of the next word. 

### 68.3.3 Low-power modes 

Table 385. Low-power modes 

||Chip mode||LPSPI operation|
|---|---|---|---|
|Run||Normal operation||



### 68.3.4 Debug mode 

Table 386. Debug mode 

|Chip mode|LPSPI operation|
|---|---|
|Debug (the core is in Debug/<br>Halted mode)|Can continue operating in Debug mode, if theCR[DBGEN]= 1.|



### 68.3.5 Interrupts and DMA requests 

The following table lists the Slave mode sources (status flags) that can generate LPSPI interrupts and LPSPI slave transmit and receive DMA requests. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2432 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

Table 387. Interrupts and DMA requests 

|Statu|s (SR)|Description||Can generate||
|---|---|---|---|---|---|
|Status flag|Name||Interrupt?|DMA<br>request?|Low-power<br>wake-up?|
|TDF|Transmit data<br>flag|Data can be written to transmit FIFO, as<br>configured by the transmit FIFO watermark<br>FCR[TXWATER]|Y|TX|Y|
|RDF|Receive data<br>flag|Data can be read from the receive FIFO, as<br>configured by the receive FIFO watermark<br>FCR[RXWATER]|Y|RX|Y|
|WCF|Word<br>complete flag|Word is complete, the last bit of the word has<br>been sampled|Y|N|Y|
|FCF|Frame<br>complete flag|Frame is complete, and PCS has deasserted|Y|N|Y|
|TCF|Transfer<br>complete flag|Transfer is complete, PCS has deasserted,<br>and the transmit and command FIFO is<br>empty|Y|N|Y|
|TEF|Transmit<br>error flag|Indicates a transmit and command<br>FIFO underrun. In Master mode when<br>CFGR1[NOSTALL]= 0 (transfers stall when<br>transmit FIFO is empty), the Transmit Error<br>Flag cannot set.|Y|N|Y|
|REF|Receive error<br>flag|Indicates a receive FIFO overflow. In Master<br>mode when CFGR1[NOSTALL] = 0 (transfers<br>stall when receive FIFO is full), the Receive<br>Error Flag cannot set.|Y|N|Y|
|DMF|Data match<br>flag|Indicates that the received data has matched<br>the configured data match value|Y|N|Y|
|MBF|Module busy<br>flag|LPSPI is busy performing a SPI bus transfer|N|N|N|



### 68.3.6 Clocks 

Table 388. LPSPI clocks 

|LPSPI functional clock|• Asynchronous to the bus clock.|
|---|---|
||• If the LPSPI functional clock remains enabled in low-power modes, then LPSPI can perform<br>SPI bus transfers and low-power wakeups, in both Master and Slave modes.<br>• LPSPI divides the functional clock by a prescaler; the resulting frequency must be at least 2<br>times faster than the SPI external clock frequency (SCK).|
|External clock|• The LPSPI shift register is clocked directly by the SCK clock.|
||• How the SCK clock is generated or supplied depends upon the mode (Master or Slave):|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2433 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

Table 388. LPSPI clocks (continued) 

||— In Master mode: the SCK clock is generated internally.<br>— In Slave mode: the SCK clock is supplied externally.|
|---|---|
|Bus clock|The bus clock is only used for bus accesses to the LPSPI control and configuration registers. The<br>bus clock frequency must be high enough to support the data bandwidth requirements of the LPSPI<br>registers, including the FIFOs.|



For chip-specific clocking information, see the Clocking chapter. 

### 68.3.7 Resets 

Table 389. Resets 

|Chip reset|Resets the LPSPI logic and registers to their default state.|
|---|---|
|Software reset|• Resets the LPSPI logic and registers to their default state, except for the Control Register.<br>• The LPSPI software reset is controlled usingCR[RST].|
|FIFO resets|• Resets the transmit and command FIFO and the receive FIFO.|
||• The Reset Transmit FIFO field,CR[RTF], and the Reset Receive FIFO field,CR[RRF], are<br>write only.|
||• After being reset, a FIFO is empty.|



### 68.3.8 Peripheral triggers 

The connection of the LPSPI peripheral triggers to other peripherals depend upon the specific device being used. 

Table 390. Peripheral triggers 

|Trigger|Description|Notes|
|---|---|---|
|Frame output trigger|The frame output trigger:<br>• Asserts at the end of each frame (when PCS deasserts)<br>• Remains asserted for one cycle of LPSPI functional clock divided by the<br>PRESCALE configuration|LPSPI generates two<br>output triggers that can<br>be connected to other<br>peripherals on the chip.|
|Word output trigger|The word output trigger:<br>• Asserts at the end of each received word<br>• Remains asserted for one cycle of LPSPI functional clock divided by the<br>PRESCALE configuration||
|Input trigger|To control the start of an LPSPI bus transfer, the LPSPI input trigger can be<br>selected instead of the HREQ input.<br>• The LPSPI input trigger is synchronized, and must assert for at least<br>2 cycles of the LPSPI functional clock divided by the PRESCALE<br>configuration, so that the input trigger can be detected.||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2434 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

Table 390. Peripheral triggers (continued) 

|Trigger|Description|Notes|
|---|---|---|
||• When the LPSPI module is busy, the HREQ input (and therefore the<br>LPSPI input trigger) is ignored.||
||• Both HREQ and the LPSPI input trigger are ignored when the module is<br>busy. They are used to start a new transfer when the module is idle.||



## 68.4 Signals 

Table 391. Signals 

|Signal|Name|Description|I/O|
|---|---|---|---|
|SCK|Serial clock|• Input in Slave mode<br>• Output in Master mode|I/O|
|PCS[0]|Peripheral chip select|• Input in Slave mode<br>• Output in Master mode|I/O|
|PCS[1] / HREQ|Peripheral chip select<br>or<br>host request|Host request pin is selected when<br>CFGR0[HREN]= 1 andCFGR0[HRSEL]= 0<br>• Input in either Slave mode or when used as<br>master host request<br>• Output in either Master mode or when used as<br>slave host request|I/O|
|PCS[2] /<br>DATA[2]|Peripheral chip select or data pin<br>2 during parallel data transfers|WhenCFGR1[PCSCFG]= 0:<br>• Input in Slave mode<br>• Output in Master mode<br>WhenCFGR1[PCSCFG]= 1:<br>• Input in half-duplex parallel data receive<br>transfers<br>• Output in half-duplex parallel data transmit<br>transfers|I/O|
|PCS[3] /<br>DATA[3]|Peripheral chip select or data pin<br>3 during parallel data transfers|When CFGR1[PCSCFG] = 0:<br>• Input in Slave mode<br>• Output in Master mode<br>When CFGR1[PCSCFG] = 1:<br>• Input in half-duplex parallel data receive<br>transfers<br>• Output in half-duplex parallel data transmit<br>transfers|I/O|
|PCS[4] /<br>DATA[4]|Peripheral chip select or data pin<br>4 during parallel data transfers|When CFGR1[PCSCFG] = 0:|I/O|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2435 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

Table 391. Signals (continued) 

|Signal|Name|Description|I/O|
|---|---|---|---|
|||• Input in Slave mode<br>• Output in Master mode<br>When CFGR1[PCSCFG] = 11b:<br>• Input in half-duplex parallel data receive<br>transfers<br>• Output in half-duplex parallel data transmit<br>transfers||
|PCS[5] /<br>DATA[5]|Peripheral chip select or data pin<br>5 during parallel data transfers|When CFGR1[PCSCFG] = 0:<br>• Input in Slave mode<br>• Output in Master mode<br>When CFGR1[PCSCFG] = 11b:<br>• Input in half-duplex parallel data receive<br>transfers<br>• Output in half-duplex parallel data transmit<br>transfers|I/O|
|PCS[6] /<br>DATA[6]|Peripheral chip select or data pin<br>6 during parallel data transfers|When CFGR1[PCSCFG] = 0:<br>• Input in Slave mode<br>• Output in Master mode<br>When CFGR1[PCSCFG] = 11b:<br>• Input in half-duplex parallel data receive<br>transfers<br>• Output in half-duplex parallel data transmit<br>transfers|I/O|
|PCS[7] /<br>DATA[7]|Peripheral chip select or data pin<br>7 during parallel data transfers|When CFGR1[PCSCFG] = 0:<br>• Input in Slave mode<br>• Output in Master mode<br>When CFGR1[PCSCFG] = 11b:<br>• Input in half-duplex parallel data receive<br>transfers<br>• Output in half-duplex parallel data transmit<br>transfers|I/O|
|SOUT /<br>DATA[0]|Serial data output|Can be configured as serial data input signal<br>• Used as data pin 0 in half-duplex parallel data<br>transfers|I/O|
|SIN / DATA[1]|Serial data input|Can be configured as serial data output signal|I/O|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2436 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

##### Table 391. Signals (continued) 

|Signal|Name|Description|I/O|
|---|---|---|---|
|||• Used as data pin 1 in half-duplex parallel data<br>transfers||



## 68.5 Memory map and registers 

~~<mark>NOTE</mark>~~ 

- Writing to a read-only register or reading a write-only register can cause bus errors. 

- LPSPI does not check values programmed in registers for validity, so you must take care to write valid values only. 

### 68.5.1 LPSPI register descriptions 

#### 68.5.1.1 LPSPI memory map 

LPSPI_0 base address: 4035_8000h LPSPI_1 base address: 4035_C000h LPSPI_2 base address: 4036_0000h LPSPI_3 base address: 4036_4000h LPSPI_4 base address: 404B_C000h LPSPI_5 base address: 404C_0000h 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|0h|Version ID (VERID)|32|RO|0200_0004h|
|4h|Parameter (PARAM)|32|RO|See<br>description|
|10h|Control (CR)|32|RW|0000_0000h|
|14h|Status (SR)|32|W1C|0000_0001h|
|18h|Interrupt Enable (IER)|32|RW|0000_0000h|
|1Ch|DMA Enable (DER)|32|RW|0000_0000h|
|20h|Configuration 0 (CFGR0)|32|RW|0000_0000h|
|24h|Configuration 1 (CFGR1)|32|RW|0000_0000h|
|30h|Data Match 0 (DMR0)|32|RW|0000_0000h|
|34h|Data Match 1 (DMR1)|32|RW|0000_0000h|
|40h|Clock Configuration (CCR)|32|RW|0000_0000h|
|44h|Clock Configuration 1 (CCR1)|32|RW|0000_0000h|
|58h|FIFO Control (FCR)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2437 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|5Ch|FIFO Status (FSR)|32|RO|0000_0000h|
|60h|Transmit Command (TCR)|32|RW|0000_001Fh|
|64h|Transmit Data (TDR)|32|WO|0000_0000h|
|70h|Receive Status (RSR)|32|RO|0000_0002h|
|74h|Receive Data (RDR)|32|RO|0000_0000h|
|78h|Receive Data Read Only (RDROR)|32|RO|0000_0000h|
|3FCh|Transmit Command Burst (TCBR)|32|WO|0000_0000h|
|400h - 5FCh|Transmit Data Burst (TDBR0 - TDBR127)|32|WO|0000_0000h|
|600h - 7FCh|Receive Data Burst (RDBR0 - RDBR127)|32|RO|0000_0000h|



#### 68.5.1.2 Version ID (VERID) 

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
|Reset|0|0|0|0|0|0|1|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||FEAT|URE||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|1|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2438 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

##### Fields 

|Field|Function|
|---|---|
|31-24|Major Version Number|
|MAJOR|Indicates the major version number for the module specification.|
|23-16|Minor Version Number|
|MINOR|Indicates the minor version number for the module specification.|
|15-0|Module Identification Number|
|FEATURE|Indicates the feature set number.|
||0000_0000_0000_0100b - Standard feature set supporting a 32-bit shift register.|
||All other values are reserved.|



#### 68.5.1.3 Parameter (PARAM) 

##### Offset 

|Register|Offset|
|---|---|
|PARAM|4h|



Function 

Contains: 

- Number of PCS pins 

- Receive FIFO size 

- Transmit FIFO size 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/068_Low_Power_Serial_Peripheral_Interface_-LPSPI-/S32K3XXRM_数据表.pdf-2439-13.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 PCSNUM<br>W<br>Reset See Register reset values.<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXFIFO  TXFIFO<br>W<br><!-- End of picture text -->

Reset 

See Register reset values. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2439 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

##### Register reset values 

|Register|Reset value|
|---|---|
|PARAM|LPSPI_0: 0008_0202h|
||LPSPI_1: 0006_0202h|
||LPSPI_2–LPSPI_5: 0004_0202h|



##### Fields 

|Field|Function|
|---|---|
|31-24|Reserved|
|—||
|23-16|PCS Number|
|PCSNUM|Indicates the number of PCS pins supported.|
|15-8|Receive FIFO Size|
|RXFIFO|Indicates the maximum number of words in the receive FIFO. The maximum number of words is 2<sup>RXFIFO</sup>.|
|7-0|Transmit FIFO Size|
|TXFIFO|Indicates the maximum number of words in the transmit FIFO. The maximum number of words is<br>2<sup>TXFIFO</sup>.|



#### 68.5.1.4 Control (CR) 

##### Offset 

|Register|Offset|
|---|---|
|CR|10h|



##### Function 

##### Contains fields that control module operation. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/068_Low_Power_Serial_Peripheral_Interface_-LPSPI-/S32K3XXRM_数据表.pdf-2440-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 DBGE Reserv<br>RST  MEN<br>W RRF  RTF  N  ed<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2440 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

##### Fields 

|Field|Function|
|---|---|
|31-10<br>—|Reserved|
|9<br>RRF|Reset Receive FIFO<br>Deletes all entries in the receive FIFO. This field always reads zero.<br>0b - No effect<br>1b - Reset|
|8<br>RTF|Reset Transmit FIFO<br>Deletes all entries in the transmit FIFO. This field always reads 0.<br>0b - No effect<br>1b - Reset|
|7-4<br>—|Reserved|
|3|Debug Enable|
|DBGEN|Enables LPSPI in when the CPU is in Debug mode. When this field is 0, LPSPI is disabled when the CPU<br>is halted; the PCS pin is deasserted after the transmit FIFO is empty regardless of the state ofTransmit<br>Command (TCR).<br>Update this field only when the LPSPI module is disabled (MEN= 0).<br>0b - Disable<br>1b - Enable|
|2<br>—|Reserved|
|1<br>RST|Software Reset<br>Resets all internal logic and registers, exceptControl (CR). The reset takes effect immediately and<br>remains asserted until you write 0 to it. There is no minimum delay required before clearing the software<br>reset by writing 0.<br>0b - Not reset|
||1b - Reset|
|0|Module Enable|
|MEN|0b - Disable<br>1b - Enable|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2441 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

#### 68.5.1.5 Status (SR) 

##### Offset 

|Register|Offset|
|---|---|
|SR|14h|



##### Function 

##### Contains data flow status. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/068_Low_Power_Serial_Peripheral_Interface_-LPSPI-/S32K3XXRM_数据表.pdf-2442-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 MBF  0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 DMF  REF  TEF  TCF  FCF  WCF  0 RDF  TDF<br>W W1C W1C W1C W1C W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-25|Reserved|
|—||
|24|Module Busy Flag|
|MBF|In Master mode, indicates that there is data to transmit and LPSPI is able to transmit (for example, HREQ<br>is asserted). It deasserts after the PCS pin deasserts and the LPSPI master has waited half theCCR[DBT]<br>time with no new data to transmit.<br>Slave mode asserts this flag when LPSPI is enabled and PCS is asserted.<br>0b - LPSPI is idle<br>1b - LPSPI is busy|
|23-14<br>—|Reserved|
|13|Data Match Flag|
|DMF|Indicates that received data matchesDMR0[MATCH0]and/orDMR1[MATCH1](as configured by<br>CFGR1[MATCFG]).|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2442 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - No match<br>1b - Match|
|12<br>REF|Receive Error Flag<br>Indicates a receive FIFO overflow error. When this flag is set:<br>1. End the transfer.<br>2. Empty the Receive FIFO.<br>3. Clear this flag.<br>4. Restart the transfer from the beginning.<br>0b - No overflow<br>1b - Overflow|
|11<br>TEF|Transmit Error Flag<br>Indicates a Transmit FIFO underrun error. When this flag is set:<br>1. End the transfer.<br>2. Clear this flag.<br>3. Restart the transfer from the beginning.<br>0b - No underrun<br>1b - Underrun|
|10<br>TCF|Transfer Complete Flag<br>In Master mode, indicates that all transfers have completed and that LPSPI has returned to Idle state<br>and the transmit FIFO is empty.<br>0b - Not complete<br>1b - Complete|
|9<br>FCF|Frame Complete Flag<br>Indicates that a frame transfer has completed, when the PCS deasserts.<br>0b - Not complete<br>1b - Complete|
|8<br>WCF|Word Complete Flag<br>Indicates that the last bit of a received word is sampled.<br>0b - Not complete<br>1b - Complete|
|7-2<br>—|Reserved<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2443 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|1|Receive Data Flag|
|RDF|Indicates that the number of words in the receive FIFO is greater than the value inFCR[RXWATER].<br>0b - Receive data not ready|
||1b - Receive data is ready|
|0|Transmit Data Flag|
|TDF|Indicates that the number of words in the transmit FIFO is equal to or less than the value in<br>FCR[TXWATER].|
||0b - Transmit data not requested|
||1b - Transmit data is requested|



#### 68.5.1.6 Interrupt Enable (IER) 

##### Offset 

|Register|Offset|
|---|---|
|IER|18h|



##### Function 

Enables interrupts based on data flow and errors. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/068_Low_Power_Serial_Peripheral_Interface_-LPSPI-/S32K3XXRM_数据表.pdf-2444-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>DMIE  REIE  TEIE  TCIE  FCIE  WCIE  RDIE  TDIE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-14<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2444 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

##### Table continued from the previous page... 

|Field<br>13|Function<br>Data Match Interrupt Enable|
|---|---|
|DMIE|0b - Disable<br>1b - Enable|
|12|Receive Error Interrupt Enable|
|REIE|0b - Disable<br>1b - Enable|
|11|Transmit Error Interrupt Enable|
|TEIE|0b - Disable<br>1b - Enable|
|10|Transfer Complete Interrupt Enable|
|TCIE|0b - Disable<br>1b - Enable|
|9<br>FCIE|Frame Complete Interrupt Enable<br>0b - Disable<br>1b - Enable|
|8|Word Complete Interrupt Enable|
|WCIE|0b - Disable<br>1b - Enable|
|7-2<br>—|Reserved|
|1|Receive Data Interrupt Enable|
|RDIE|0b - Disable<br>1b - Enable|
|0|Transmit Data Interrupt Enable|
|TDIE|0b - Disable<br>1b - Enable|



#### 68.5.1.7 DMA Enable (DER) 

##### Offset 

|Register|Offset|
|---|---|
|DER|1Ch|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2445 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

##### Function 

##### Enables DMA data flow. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/068_Low_Power_Serial_Peripheral_Interface_-LPSPI-/S32K3XXRM_数据表.pdf-2446-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>RDDE  TDDE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-2<br>—|Reserved|
|1|Receive Data DMA Enable|
|RDDE|0b - Disable|
||1b - Enable|
|0|Transmit Data DMA Enable|
|TDDE|0b - Disable|
||1b - Enable|



#### 68.5.1.8 Configuration 0 (CFGR0) 

##### Offset 

|Register|Offset|
|---|---|
|CFGR0|20h|



##### Function 

Includes fields to configure LPSPI. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2446 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||0||||RDMO|CIRFIF||0|||HRDIR|HRSE|HRPO|HREN|
|W||||||||O||||||L|L||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-10<br>|Reserved|
|—||
|9<br>RDMO|Receive Data Match Only<br>When enabled, all received data that does not cause the Data Match Flag (SR[DMF]) to assert is discarded.<br>• Write 1 to this field when LPSPI is idle andSR[DMF]= 0.<br>• AfterSR[DMF]= 1, this field is ignored.<br>• To ensure that no receive data is lost when disabling RDMO, write 0 to this field before<br>clearingSR[DMF].<br>SeeCFGR1[MATCFG]for the received data matching options. When disabled, all received data is stored<br>in the receive FIFO.<br>0b - Disable<br>1b - Enable|
|8<br>CIRFIFO|Circular FIFO Enable<br>When enabled, the transmit FIFO read pointer is saved to a temporary register. The transmit FIFO is<br>emptied as in normal operation, but when LPSPI is idle and the transmit FIFO is empty, the read pointer<br>value is restored from the temporary register.<br>This restoring of the read pointer causes the contents of the transmit FIFO to be cycled through repeatedly.<br>The read pointer is restored for as long as this field is 1. Writing additional words to the FIFO<br>when this field is 1 adds them to the end of the FIFO, up to the size of the transmit FIFO.<br>~~NOTE~~<br>0b - Disable<br>1b - Enable|
|7-4<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2447 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|3<br>HRDIR|Host Request Direction<br>Specifies the direction of the HREQ pin. Only configure the HREQ pin as an output when LPSPI is in<br>Slave mode. The HREQ pin direction must be an input for Master mode.<br>0b - Input<br>1b - Output|
|2|Host Request Select|
|HRSEL|Specifies the source of the host request input. When the host request function is enabled with the HREQ<br>pin, the PCS[1] function is disabled.<br>0b - HREQ pin<br>1b - Input trigger|
|1|Host Request Polarity|
|HRPOL|Specifies the polarity of the HREQ pin or input trigger.<br>0b - Active high<br>1b - Active low|
|0<br>HREN|Host Request Enable<br>In Master mode, allows LPSPI to start a new SPI bus transfer only if the host request input is asserted. When<br>LPSPI is busy, the host request input is ignored.<br>In Slave mode, causes the HREQ output pin to assert when data is available to be transmitted.<br>0b - Disable|
||1b - Enable|



#### 68.5.1.9 Configuration 1 (CFGR1) 

##### Offset 

|Register|Offset|
|---|---|
|CFGR1|24h|



##### Function 

Includes fields to configure LPSPI. Write to this register only when LPSPI is disabled. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2448 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||0||PCS|CFG|OUTC<br>FG|PIN|CFG|||0||||MATCFG||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||PCS|POL|||||0||PARTI<br>AL|NOST<br>ALL|AUTO<br>PCS|SAMP<br>LE|MAST<br>ER|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function||
|---|---|---|
|31-29<br>—<br>28-27|Reserved<br>Peripheral Chip Select Configuration||
|PCSCFG|Specifies the PCS pin configuration. When performing parallel tran<br>enable the desired transfer.<br>This field is not supported in every instance. The following ta<br>supported registers.<br>~~NOTE~~|sfers, this field must be configured to<br>ble includes only|
||Instance<br>Field supported in|Field not supported in|
||LPSPI_0<br>CFGR1|—|
||LPSPI_1<br>CFGR1[27]|CFGR1[28]|
||LPSPI_2<br>CFGR1[27]|CFGR1[28]|
||LPSPI_3<br>CFGR1[27]|CFGR1[28]|
||LPSPI_4<br>CFGR1[27]|CFGR1[28]|
||LPSPI_5<br>CFGR1[27]|CFGR1[28]|
||00b - PCS[7:2] are configured for chip select function<br>01b - PCS[3:2] are configured for half-duplex 4-bit transfers<br>11b - PCS[7:2] are configured for half-duplex 4-bit and 8-bit|(PCS[3:2] = DATA[3:2])<br>transfers (PCS[7:2] = DATA[7:2])|



26 Output Configuration OUTCFG Specifies whether the output data is 3-stated between accesses (when PCS is deasserted). When performing half-duplex transfers, this field must be 1. 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2449 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

##### Table continued from the previous page... 

|Field|Function<br>0b - Output data retai<br>1b - Output data is 3-|ns last value.<br>stated.|
|---|---|---|
|25-24<br>PINCFG|Pin Configuration<br>Specifies the pins used for i<br>performing parallel transfers<br>00b - SIN is used for<br>01b - SIN is used for<br>10b - SOUT is used f<br>supported.<br>11b - SOUT is used f|nput and output data during serial transfers. This field is ignored when<br>.<br>input data; SOUT is used for output data.<br>both input and output data. Only half-duplex serial transfers are supported.<br>or both input and output data. Only half-duplex serial transfers are<br>or input data; SIN is used for output data.|
|23-19<br>—|Reserved||
|18-16|Match Configuration||
|MATCFG|Specifies the condition that c|ausesSR[DMF]to assert.|
||Condition|Description|
||Match first data word with<br>compare word|Match if first data word equalsMATCH0logically ORed withMATCH1<br>first_data_word == (MATCH0 || MATCH1)|
||Match any data word with<br>compare word|Match if any data word equals MATCH0 logically ORed with MATCH1<br>any_data_word == (MATCH0 || MATCH1)|
||Sequential match, first<br>data word|Match if first data word equals MATCH0, and second data word<br>equals MATCH1<br>(first_data_word == MATCH0) && (second_data_word == MATCH1)|
||Sequential match, any<br>data word|Match if any data word equals MATCH0, and the next data word<br>equals MATCH1<br>(any_data_word == MATCH0) && (next_data_word == MATCH1)|
||Match first data word<br>(masked) with compare<br>word (masked)|Match if first data word logically ANDed with MATCH1 equals MATCH0<br>logically ANDed with MATCH1<br>(first_data_word && MATCH1) == (MATCH0 && MATCH1)|
||Match any data word<br>(masked) with compare<br>word (masked)|Match if any data word logically ANDed with MATCH1 equals MATCH0<br>logically ANDed with MATCH1<br>(any_data_word && MATCH1) == (MATCH0 && MATCH1)|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2450 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

##### Table continued from the previous page... 

Field Function Condition Description 000b - Match is disabled 001b - Reserved 010b - Match first data word with compare word 011b - Match any data word with compare word 100b - Sequential match, first data word 101b - Sequential match, any data word 110b - Match first data word (masked) with compare word (masked) 111b - Match any data word (masked) with compare word (masked) 15-8 Peripheral Chip Select Polarity PCSPOL Specifies the polarity of each PCS pin. Bit n in this field (the least-significant bit is bit 0) corresponds to PCS[n]. For each PCSPOL bit: 0b – PCS[n] pin is active low 1b – PCS[n] pin is active high ~~<mark>NOTE</mark>~~ The entire PCSPOL field is not fully supported in every LPSPI module instance. See the LSPI chip-specific information. ~~<mark>NOTE</mark>~~ This field is not supported in every instance. The following table includes only supported registers. Instance Field supported in Field not supported in LPSPI_0 CFGR1 — LPSPI_1 CFGR1[13–8] CFGR1[15–14] LPSPI_2 CFGR1[11–8] CFGR1[15–12] LPSPI_3 CFGR1[11–8] CFGR1[15–12] LPSPI_4 CFGR1[11–8] CFGR1[15–12] LPSPI_5 CFGR1[11–8] CFGR1[15–12] 7-5 Reserved 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2451 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|4<br>PARTIAL|Partial Enable<br>Specifies whether LSPI, when in Slave mode, stores a partial received word in the receive FIFO, or<br>discards it, when PCS deasserts.<br>0b - Discard<br>1b - Store|
|3<br>NOSTALL|No Stall<br>Disables a normal operating feature that causes LSPI, when in Master mode, to stall transfers when the<br>transmit FIFO is empty or when the receive FIFO is full. This feature prevents transmit FIFO underruns<br>and receive FIFO overruns. Writing 1 to this field disables this functionality.<br>0b - Disable<br>1b - Enable|
|2|Automatic PCS|
|AUTOPCS|Enables automatic PCS generation. For correct operation in Slave mode, LPSPI requires the PCS signal to<br>deassert between frames. Writing 1 to this field generates an internal PCS signal at the end of each transfer<br>word whenTCR[CPHA]= 1.<br>When this field is 1, SCK must remain idle for at least 4 LPSPI functional clock cycles, divided by the<br>prescaler selected (seeTCR[PRESCALE]) between each word, to ensure correct operation.<br>This field is ignored in Master mode.<br>0b - Disable<br>1b - Enable|
|1<br>SAMPLE|Sample Point<br>Specifies the SCK clock edge on which LSPI, when in Master mode, samples input data. Writing 1 to this<br>field causes LSPI to sample input data on a delayed loopback SCK clock edge, which improves the setup<br>time when sampling data (seeClock loopback). In this configuration. The input data setup time in Master<br>mode is equal to the input data setup time in Slave mode.<br>In Slave mode, this field is ignored.<br>0b - SCK edge<br>1b - Delayed SCK edge|
|0<br>MASTER|Master Mode<br>Specifies the LPSPI operating mode—either Master or Slave. This field directly controls the direction of<br>the SCK and PCS pins.<br>0b - Slave mode<br>1b - Master mode|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2452 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

#### 68.5.1.10 Data Match 0 (DMR0) 

##### Offset 

|Register|Offset|
|---|---|
|DMR0|30h|



##### Function 

Specifies match data to be used when data matching is enabled. See CFGR1[MATCFG] for the received data matching options. 

~~<mark>NOTE</mark>~~ Do not change the value in this register while CFGR0[RDMO] = 1. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/068_Low_Power_Serial_Peripheral_Interface_-LPSPI-/S32K3XXRM_数据表.pdf-2453-09.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>MATCH0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>MATCH0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Match 0 Value|
|MATCH0|MATCH0 value to be compared against received data.|



#### 68.5.1.11 Data Match 1 (DMR1) 

##### Offset 

|Register|Offset|
|---|---|
|DMR1|34h|



##### Function 

Specifies match data to be used when data matching is enabled. See CFGR1[MATCFG] for the received data matching options. 

~~<mark>NOTE</mark>~~ 

Do not change the value in this register while CFGR0[RDMO] = 1. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2453 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/068_Low_Power_Serial_Peripheral_Interface_-LPSPI-/S32K3XXRM_数据表.pdf-2454-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>MATCH1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>MATCH1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Match 1 Value|
|MATCH1|MATCH1 value to be compared against received data.|



#### 68.5.1.12 Clock Configuration (CCR) 

##### Offset 

|Register|Offset|
|---|---|
|CCR|40h|



##### Function 

Contains clock configuration fields. These fields are only used in Master mode and you can only change them when LPSPI is disabled (CR[MEN] = 0). 

~~<mark>Warning</mark>~~ 

Writing a 32-bit value to this register overwrites Clock Configuration 1 (CCR1); DBT and SCKDIV always read 0. 

To avoid overwriting CCR1: 

- Either write all 4 CCR register fields simultaneously and only once in a 32-bit data. 

- Or to modify SCKPCS and/or PCSSCK values, write only these 2 upper bytes in a 16-bit data or one of them in an 8-bit data. 

- Or to modify CCR1[PCSPCS] and CCR1[SCKSCK] fields only or CCR1[SCKSET] and CCR1[SCKHLD] fields only, write respectively CCR[DBT] or CCR[SCKDIV] in 8-bit data 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2454 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||SCK|PCS|||||||PCSS|CK||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||0||||||||0|||||
|W||||DB|T|||||||SCK|DIV||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-24|SCK-to-PCS Delay|
|SCKPCS|In Master mode: configures the delay from the last SCK edge to the PCS negation.<br>• The delay is equal to (SCKPCS + 1) cycles of the LPSPI functional clock divided by the prescaler<br>selected (seeTCR[PRESCALE]).<br>• The minimum delay is 1 cycle.<br>SeeFigure 362.|
|23-16|PCS-to-SCK Delay|
|PCSSCK|In Master mode: configures the delay from the PCS assertion to the first SCK edge.<br>• The delay is equal to (PCSSCK + 1) cycles of the LPSPI functional clock divided by the prescaler<br>selected (seeTCR[PRESCALE]).<br>• The minimum delay is 1 cycle.<br>SeeFigure 362.|
|15-8|Delay Between Transfers|
|DBT|Writing this field updates the contents ofCCR1[PCSPCS]andCCR1[SCKSCK].|
|7-0|SCK Divider|
|SCKDIV|Writing this field updates the contents ofCCR1[SCKSET]andCCR1[SCKHLD].|



#### 68.5.1.13 Clock Configuration 1 (CCR1) 

##### Offset 

|Register|Offset|
|---|---|
|CCR1|44h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2455 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

##### Function 

Contains clock configuration fields. These fields are only used in Master mode and you can only change them when LPSPI is disabled (CR[MEN] = 0). 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||SCK|SCK|||||||PCS|PCS||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||SCK|HLD|||||||SCK|SET||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-24|SCK Inter-Frame Delay|
|SCKSCK|In Master mode:<br>• Configures the delay from the last SCK pulse of a frame and the first SCK pulse of the following<br>frame, in a continuous transfer.<br>• The delay is equal to (SCKSCK + 1) cycles of the LPSPI functional clock divided by the prescaler<br>selected (seeTCR[PRESCALE]).<br>• The minimum delay is 1 cycle.<br>For backward compatibility, writing CCR[DBT] updates CCR1[SCKSCK] with the<br>value written.<br>~~NOTE~~|
|23-16|PCS to PCS delay|
|PCSPCS|In Master mode:<br>• Configures the delay from the PCS negation to the next PCS assertion.<br>• The delay is equal to (PCSPCS + PCSPCS + 2) cycles of the LPSPI functional clock divided by the<br>prescaler selected (seeTCR[PRESCALE]).<br>• The minimum delay is 2 cycles.<br>• Half of the delay (PCSPCS + 1) occurs before PCS assertion and the other half of the delay<br>(PCSPCS + 1) occurs after PCS negation. If the command word is updated between 2 transfers,<br>then the command word is updated halfway between the PCS negation of the last transfer and PCS<br>assertion of the next transfer.<br>• The command word specifies which PCS signal is used, the polarity and phase of the SCK signal,<br>and the prescaler selected.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2456 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||For backward compatibility, writingCCR[DBT]updates this field with (DBT÷2) rounded up.<br>~~NOTE~~|
|15-8<br>SCKHLD|SCK Hold<br>In Master mode, this field configures the hold phase of the SCK pin.<br>• The hold phase is the delay between the SCK edge that samples the receive data and the SCK<br>edge that drives the transmit data.<br>• This is the SCK low period when CPHA = 0 and CPOL = 1, or CPHA = 1 and CPOL = 0. This is the<br>SCK high period when CPHA = 0, CPOL = 0 and CPHA = 1, CPOL = 1.<br>• The SCK hold phase delay is equal to (SCKHLD + 1) cycles of the LPSPI functional clock divided by<br>the prescaler selected (seeTCR[PRESCALE]).<br>• The minimum delay is 1 cycle.<br>• The SCK period is equal to (SCKSET + SCKHLD + 2) cycles of the LPSPI functional clock divided<br>by the prescaler selected (seeTCR[PRESCALE]).<br>• The SCK duty cycle is based on the difference between SCKSET and SCKHLD. Configure both<br>fields to the same value for 50/50 duty cycle.<br>SeeFigure 362.<br>For backward compatibility, writingCCR[SCKDIV]updates this field with (SCKDIV ÷ 2)<br>rounded down.<br>~~NOTE~~|
|7-0<br>SCKSET|SCK Setup<br>In Master mode, the SCK Setup configures the setup phase of the SCK pin.<br>• The setup phase is the delay between the SCK edge that drives the transmit data and the SCK edge<br>that samples the receive data.<br>• This is the SCK high period when CPHA = 0 and CPOL = 1, or CPHA = 1 and CPOL = 0. This is the<br>SCK low period when CPHA = 0 and CPOL = 0, or CPHA = 1 and CPOL = 1.<br>• The SCK setup phase delay is equal to (SCKSET + 1) cycles of the LPSPI functional clock divided<br>by the prescaler selected (seeTCR[PRESCALE]).<br>• The minimum delay is 1 cycle.<br>• The SCK period is equal to (SCKSET + SCKHLD + 2) cycles of the LPSPI functional clock divided<br>by the prescaler selected (see TCR[PRESCALE]).<br>• The SCK duty cycle is based on the difference between SCKSET and SCKHLD, configure both<br>fields to the same value for 50/50 duty cycle.<br>SeeFigure 362.<br>For backward compatibility, writingCCR[SCKDIV]updates this field with (SCKDIV ÷ 2)<br>rounded up.<br>~~NOTE~~|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2457 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

#### 68.5.1.14 FIFO Control (FCR) 

##### Offset 

|Register|Offset|
|---|---|
|FCR|58h|



##### Function 

Contains the receive FIFO and transmit FIFO watermark values. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||||0||||||0||||RXWATER|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R<br>W|||||0||||||0||||TXWATER|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



##### Fields 

|Field|Function|
|---|---|
|31-24|Reserved|
|—<br>23-18|Reserved|
|—||
|17-16|Receive FIFO Watermark|
|RXWATER|Causes LPSPI to set the Receive Data Flag (SR[RDF]) when the number of words in the receive FIFO is<br>greater than RXWATER. Writing a value equal or greater than the FIFO size truncates the written value.|
|15-8<br>—|Reserved|
|7-2<br>—|Reserved|
|1-0|Transmit FIFO Watermark|
|TXWATER|Causes LPSPI to set the Transmit Data Flag (SR[TDF]) when the number of words in the transmit FIFO<br>is equal or less than TXWATER. Writing a value equal or greater than the FIFO size truncates the written<br>value.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2458 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

#### 68.5.1.15 FIFO Status (FSR) 

##### Offset 

|Register|Offset|
|---|---|
|FSR|5Ch|



##### Function 

Contains fields that indicate the number of words currently stored in the receive FIFO and transmit FIFO. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18<br>17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||0||||||0|||RXCOUNT|
|W|||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2<br>1<br>0|
|R|||||0||||||0|||TXCOUNT|
|W|||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0<br>0|



##### Fields 

|Field|Function|
|---|---|
|31-24<br>—|Reserved|
|23-19<br>—<br>18-16|Reserved<br>Receive FIFO Count|
|RXCOUNT|Indicates the number of words currently stored in the receive FIFO.|
|15-8<br>—<br>7-3<br>—|Reserved<br>Reserved|
|2-0|Transmit FIFO Count|
|TXCOUNT|Indicates the number of words currently stored in the transmit FIFO.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2459 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

#### 68.5.1.16 Transmit Command (TCR) 

##### Offset 

|Register|Offset|
|---|---|
|TCR|60h|



##### Function 

Writes to either this register or Transmit Data (TDR) push the data into the transmit FIFO, in the order written. Only write to this register using 32-bit writes. Writes are tagged and cause the command register to update, after that entry reaches the top of the FIFO and the LPSPI is enabled. This allows changes to the command word and the transmit data itself to be interleaved. That is, the writes to the two registers can be interleaved (write command word, then data word, then command word, and so on). Changing the command word causes all subsequent SPI bus transfers to be performed using the new command word. 

- In Master mode, writing a new command word does not initiate a new transfer, unless TXMSK is 1. Transfers are initiated by transmit data in the transmit FIFO, or by a new command word (with TXMSK = 1). Hardware writes 0 to TXMSK when the PCS deasserts. 

- In Master mode, if the command word is changed before an existing frame has completed, then the existing frame terminates and the command word then updates. The command word can be changed during a continuous transfer, if CONTC of the new command word is 1 and the command word is written on a frame size boundary. 

- In Slave mode, the command word should be changed only when LPSPI is idle and there is no SPI bus transfer. 

Avoid resetting the Transmit FIFO after writing to the Transmit Command Register, wait for the command register to update from the FIFO first. 

Avoid register reading problems: Reading the Transmit Command Register returns the current state of the command register. Reading the Transmit Command Register at the same time that the Transmit Command Register is loaded from the transmit FIFO, can return an incorrect Transmit Command Register value. It is recommended to: 

- Read the Transmit Command Register when the transmit FIFO is empty, 

- Read the Transmit Command Register more than once and then compare the returned values. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|CPOL|CPHA||PRESCAL|E||PCS||LSBF|BYSW|CONT|CONT<br>C|RXMS<br>K|TXMS<br>K|WIDTH|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R<br>W||Reserv<br>0|ed|||||||FRAM|ESZ|||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1<br>1|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2460 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

##### Fields 

|Field|Function|
|---|---|
|31<br>CPOL|Clock Polarity<br>Specifies the value of SCK when it is idle. This field can only be updated when PCS deasserted.<br>SeeFigure 362.<br>0b - Inactive low<br>1b - Inactive high|
|30<br>CPHA|Clock Phase<br>This field can only be updated when PCS deasserted.<br>SeeFigure 362.<br>0b - Captured. Data is captured on the leading edge of SCK and changed on the following edge<br>of SCK<br>1b - Changed. Data is changed on the leading edge of SCK and captured on the following edge<br>of SCK|
|29-27<br>PRESCALE|Prescaler Value<br>For all SPI bus transfers, this value is applied toClock Configuration (CCR)clock. This field can only be<br>updated when PCS deasserted.<br>000b - Divide by 1<br>001b - Divide by 2<br>010b - Divide by 4<br>011b - Divide by 8|
||100b - Divide by 16<br>101b - Divide by 32<br>110b - Divide by 64|
||111b - Divide by 128|
|26-24<br>PCS|Peripheral Chip Select<br>Configures the peripheral chip select used for the transfer. The Peripheral Chip Select field is only<br>updated when PCS deasserted.<br>The entire PCS field is not fully supported in every LPSPI module instance. See the<br>chip-specific LPSPI information.<br>~~NOTE~~|
||This field is not supported in every instance. The following table includes only<br>supported registers.<br>~~NOTE~~|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2461 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

##### Table continued from the previous page... 

|Field|Function||
|---|---|---|
||Instance<br>Field supported in|Field not supported in|
||LPSPI_0<br>TCR|—|
||LPSPI_1<br>TCR|—|
||LPSPI_2<br>TCR[25–24]|TCR[26]|
||LPSPI_3<br>TCR[25–24]|TCR[26]|
||LPSPI_4<br>TCR[25–24]|TCR[26]|
||LPSPI_5<br>TCR[25–24]|TCR[26]|
||000b - Transfer using PCS[0]<br>001b - Transfer using PCS[1]<br>010b - Transfer using PCS[2]<br>011b - Transfer using PCS[3]<br>100b - Transfer using PCS[4]<br>101b - Transfer using PCS[5]<br>110b - Transfer using PCS[6]<br>111b - Transfer using PCS[7]||
|23<br>LSBF|LSB First<br>0b - Data is transferred MSB first<br>1b - Data is transferred LSB first||
|22<br>BYSW|Byte Swap<br>Swaps the contents of [31:24] with [7:0] and [23:16] with [15:8] for<br>FIFO and for each received data word stored to the FIFO (or comp<br>0b - Disabled<br>1b - Enabled|each transmit data word read from the<br>ared with match registers).|
|21<br>CONT|Continuous Transfer<br>• In Master mode, CONT keeps the PCS asserted at the end of<br>is received that starts a new frame.<br>• In Slave mode, when CONT is enabled, LPSPI only transmits t<br>LPSPI transmits received data (assuming a 32-bit shift register<br>0b - Continuous transfer is disabled<br>1b - Continuous transfer is enabled<br>Table continues on the next page...|the frame size, until a command word<br>he first FRAMESZ bits; after which<br>) until the next PCS negation.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2462 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|20|Continuing Command|
|CONTC|In Master mode, this field enables the command word to be changed within a continuous transfer.<br>• The initial command word must enable continuous transfer (CONT = 1).<br>• The continuing command must have CONTC = 1.<br>• The continuing command word must be loaded on a frame size boundary.<br>For example, if the continuous transfer has a frame size of 64-bits, then a continuing command word must<br>be loaded on a 64-bit boundary.<br>In Slave mode, the Continuing Command bit modifies the internal RXMSK/TXMSK configuration after the<br>first FRAMESZ bits and until the PCS negation.<br>• Receive data is discarded after the first FRAMESZ bits. If CONT is also 1 this does not block the<br>transmission of received data.<br>• Transmit data is not masked after the first FRAMESZ bits, this allows the first FRAMESZ bits to be<br>received and a response transmitted.<br>0b - Command word for start of new transfer<br>1b - Command word for continuing transfer|
|19|Receive Data Mask|
|RXMSK|Masks receive data (receive data is not stored in receive FIFO).<br>0b - Normal transfer<br>1b - Receive data is masked|
|18|Transmit Data Mask|
|TXMSK|Masks transmit data (no data is loaded from transmit FIFO and the output pin is 3-stated). In Master<br>mode, TXMSK initiates a new transfer which cannot be aborted by another command word. TXMSK<br>automatically transitions to 0 at the end of the transfer.<br>0b - Normal transfer<br>1b - Mask transmit data|
|17-16<br>WIDTH|Transfer Width<br>Configures serial (1-bit) or parallel transfers. For half-duplex parallel transfers, either Receive Data Mask<br>(RXMSK) or Transmit Data Mask (TXMSK) must be 1.<br>The descriptions of the field settings vary by module instance.<br>~~NOTE~~|
||Instance<br>Field value and description|
||LPSPI_0<br>00b - 1-bit transfer<br>01b - 2-bit transfer|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2463 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

##### Table continued from the previous page... 

|Field|Function||
|---|---|---|
||Instance|Field value and description|
|||10b - 4-bit transfer<br>11b - 8-bit transfer|
||LPSPI_1|00b - 1-bit transfer<br>01b - 2-bit transfer<br>10b - 4-bit transfer<br>11b - Reserved|
||LPSPI_2|00b - 1-bit transfer<br>01b - 2-bit transfer<br>10b - 4-bit transfer<br>11b - Reserved|
||LPSPI_3|00b - 1-bit transfer<br>01b - 2-bit transfer<br>10b - 4-bit transfer<br>11b - Reserved|
||LPSPI_4|00b - 1-bit transfer<br>01b - 2-bit transfer<br>10b - 4-bit transfer<br>11b - Reserved|
||LPSPI_5|00b - 1-bit transfer<br>01b - 2-bit transfer<br>10b - 4-bit transfer<br>11b - Reserved|
|15-12<br>—|Reserved||
|11-0<br>FRAMESZ|Frame Size<br>Configures the frame size<br>• The minimum frame<br>• If the frame size is lar<br>word is loaded from t|in number of bits equal to (FRAMESZ + 1).<br>size is 8 bits, or 16 bits for an 8-bit transfer<br>ger than 32 bits, then the frame is divided into multiple words of 32 bits; each<br>he transmit FIFO and stored in the receive FIFO separately.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2464 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

##### Table continued from the previous page... 

- Field Function • If the size of the frame is not divisible by 32, then the last load of the transmit FIFO and store of the receive FIFO contains the remainder bits. For example, a 72-bit transfer consists of 3 words: the first and second words are 32 bits, and the third word is 8 bits. 

#### 68.5.1.17 Transmit Data (TDR) 

##### Offset 

|Register|Offset|
|---|---|
|TDR|64h|



##### Function 

Writes to either Transmit Command (TCR) or this register push the data into the transmit FIFO, in the order that the data is written. You can write to TDR using 32-, 16-, or 8-bit writes, but each write pushes data into the FIFO with zero pushed in unwritten bytes. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/068_Low_Power_Serial_Peripheral_Interface_-LPSPI-/S32K3XXRM_数据表.pdf-2465-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>W DATA<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>W DATA<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Transmit Data|
|DATA|Both 8- and 16-bit writes of transmit data zero-extend the data written and push the data into the transmit<br>FIFO. To zero-extend 8- and 16-bit writes (to 32 bits), means that the higher order (most significant)<br>empty parts of the 8-bit and 16-bit writes are filled with zeroes.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2465 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

#### 68.5.1.18 Receive Status (RSR) 

##### Offset 

|Register|Offset|
|---|---|
|RSR|70h|



##### Function 

Contains data flow status fields for receive FIFO. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||||0||||||||RXEM<br>PTY|SOF|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|0|



##### Fields 

|Field|Function|
|---|---|
|31-2|Reserved|
|—<br>1|RX FIFO Empty|
|RXEMPTY|0b - Not empty|
||1b - Empty|
|0|Start Of Frame|
|SOF|Indicates that this is the first data word received after PCS assertion.|
||0b - Subsequent data word|
||1b - First data word|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2466 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

#### 68.5.1.19 Receive Data (RDR) 

##### Offset 

|Register|Offset|
|---|---|
|RDR|74h|



##### Function 

Reading this register pulls the first entry from the receive FIFO. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/068_Low_Power_Serial_Peripheral_Interface_-LPSPI-/S32K3XXRM_数据表.pdf-2467-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R DATA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DATA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-0|Receive Data|
|DATA||



#### 68.5.1.20 Receive Data Read Only (RDROR) 

##### Offset 

|Register|Offset|
|---|---|
|RDROR|78h|



##### Function 

Returns the first entry in the receive FIFO, but does not remove the data from the FIFO. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2467 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/068_Low_Power_Serial_Peripheral_Interface_-LPSPI-/S32K3XXRM_数据表.pdf-2468-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R DATA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DATA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Receive Data|
|DATA||



#### 68.5.1.21 Transmit Command Burst (TCBR) 

##### Offset 

|Register|Offset|
|---|---|
|TCBR|3FCh|



##### Function 

Supports burst transfers of command data to the transmit FIFO for use with the DMA controller. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||||||||||||
|W||||||||DA|TA||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||||||||||||||
|W||||||||DA|TA||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2468 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

##### Fields 

|Field|Function|
|---|---|
|31-0|Command Data|
|DATA|Data is written to the Transmit Command Register.|



#### 68.5.1.22 Transmit Data Burst (TDBR0 - TDBR127) 

##### Offset 

For n = 0 to 127: 

|Register<br>TDBRn|Offset<br>400h + (n × 4h)|
|---|---|



##### Function 

Supports burst transfers of data to the transmit FIFO for use with the DMA controller. The size of this register is 512 bytes. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/068_Low_Power_Serial_Peripheral_Interface_-LPSPI-/S32K3XXRM_数据表.pdf-2469-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>W DATA<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>W DATA<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Data|
|DATA|Data is written toTransmit Data (TDR).|



#### 68.5.1.23 Receive Data Burst (RDBR0 - RDBR127) 

##### Offset 

For n = 0 to 127: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2469 / 4640 

NXP Semiconductors 

Low Power Serial Peripheral Interface (LPSPI) 

|Register<br>RDBRn|Offset<br>600h + (n × 4h)|
|---|---|



##### Function 

Supports burst transfers of data from the receive FIFO. The size of this register is 512 bytes. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/068_Low_Power_Serial_Peripheral_Interface_-LPSPI-/S32K3XXRM_数据表.pdf-2470-06.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R DATA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DATA<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Data|
|DATA|Data is read from the Receive Data Register.|



## 68.6 Glossary 

PCS Peripheral chip select SCK Serial clock SDI Slave data in SDO Slave data out SS Slave select 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2470 / 4640 

