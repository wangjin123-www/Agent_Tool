NXP Semiconductors 

# Chapter 76 Low Power Universal Asynchronous Receiver/ Transmitter (LPUART) 

## 76.1 Chip-specific LPUART information 

### 76.1.1 LPUART instances and configuration 

Table 623. LPUART instances 

|Instance|S32K314/S32K324/S32K44/S32K358|S32K311/S32K322/S32K342|S32K312|
|---|---|---|---|
|LPUART_0|Yes|Yes|Yes|
|LPUART_1|Yes|Yes|Yes|
|LPUART_2|Yes|Yes|Yes|
|LPUART_3|Yes|Yes|Yes|
|LPUART_4|Yes|No|Yes|
|LPUART_5|Yes|No|Yes|
|LPUART_6|Yes|No|Yes|
|LPUART_7|Yes|No|Yes|
|LPUART_8|Yes|No|No|
|LPUART_9|Yes|No|No|
|LPUART_10|Yes|No|No|
|LPUART_11|Yes|No|No|
|LPUART_12|Yes|No|No|
|LPUART_13|Yes|No|No|
|LPUART_14|Yes|No|No|
|LPUART_15|Yes|No|No|



Table 624. LPUART Configuration 

|Feature||Configuration||
|---|---|---|---|
||S32K344<br>S32K312|S32K342|S32K358|
|TX FIFO size|4 Words|16 Words (for instance 0,1)|16 Words (for instance 0,1)|
|||4 Words (for instance 2,3)|4 Words (for instance 2 to 15)|
|RX FIFO size|4 Words|16 Words (for instance 0,1)|16 Words (for instance 0,1)|
|||4 Words (for instance 2,3)|4 Words (for instance 2 to 15)|
|Functionality supported|Standard LPUART functionality<br>with MODEM/IrDA|Standard LPUART functionali<br>MODBUS support.|ty with MODEM/IrDA and|
||L|IN master and slave operation||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4211 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

~~<mark>NOTE</mark>~~ 

LPUART instances are not available during Standby. 

LPUART[0:2]_trg_input is coming from TRGMUX and you should take care of the pulse width of trigger. It should follow the requirement mentioned in section "Peripheral Triggers". These triggers are not present in S32K314, S32K324, S32K344. 

## 76.2 Overview 

The Low Power Universal Asynchronous Receiver/Transmitter (LPUART) module provides asynchronous, serial communication capability with external devices. LPUART supports non-return-to-zero (NRZ) encoding format and IrDA compatible infrared (low-speed) SIR format. The LPUART can continue operating while the processor is in low-power mode if an appropriate peripheral clock is available. 

### 76.2.1 Block diagram 

The following figure shows the transmitter portion of the LPUART. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/076_Low_Power_Universal_Asynchronous_Receiver_Transmitter_-LPUART-/S32K3XXRM_数据表.pdf-4212-09.png)


<!-- Start of picture text -->
Internal Slave Peripheral Bus<br>(Write-Only)<br>LOOPS<br>ASYNCH<br>MODULE Transmit FIFO RSRC<br>CLOCK<br>Loop To Receive<br>BAUD M 11-BIT Transmit Shift Register Control Data In<br>Divider<br>To TxD Pin<br>OSR H 8 7 6 5 4 3 2 1 0 L<br>Divider<br>SHIFT DIRECTION<br>TXINV<br>T8<br>PE Parity<br>Generation<br>PT<br>LPUART Controls TxD<br>TE<br>SBK TO TxD<br>Transmit Control<br>TxD Direction Pin Logic<br>TXDIR<br>BRK13<br>TDRE<br>TIE<br>Tx Interrupt<br>TC<br>Request<br>TCIE<br>Figure 464. LPUART transmitter block diagram<br>Stop Start<br>lsb<br>Shift Enable Break (All 0s)<br>Load From FIFO Preamble (All 1s)<br><!-- End of picture text -->

The following figure shows the receiver portion of the LPUART. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4212 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/076_Low_Power_Universal_Asynchronous_Receiver_Transmitter_-LPUART-/S32K3XXRM_数据表.pdf-4213-02.png)


<!-- Start of picture text -->
INTERNAL SLAVE PERIPHERAL BUS<br>SBR12:0 RECEIVE FIFO<br>ASYNCH<br>MODULE BAUDRATE<br>CLOCK GENERATOR VARIABLE 12-BIT RECEIVE  M<br>SHIFT REGISTER M10<br>LBKDE<br>RE RECEIVE<br>MSBF<br>RAF CONTROL RXINV<br>SHIFT DIRECTION<br>RxD<br>LOOPS<br>RECEIVER<br>RSRC SOURCE<br>CONTROL<br>PE<br>PARITY WAKEUP<br>From Transmitter PT LOGIC LOGIC<br>RxD DMA Requests<br>ACTIVE EDGE IRQ / DMA<br>DETECT LOGIC IRQ Requests<br>STOP START<br><!-- End of picture text -->

Figure 465. LPUART receiver block diagram 

### 76.2.2 Features 

Following are the features of the LPUART module. 

- Full-duplex, standard non-return-to-zero (NRZ) format 

- Programmable baud rates(13-bit modulo divider) with configurable oversampling ratio from 4x to 32x 

- Asynchronous operation of transmit and receive baud rate with respect to the bus clock: 

   - Baud rate can be configured independently of the bus clock frequency 

   - Supports operation in low-power modes 

- Interrupt, DMA or polled operation: 

   - Transmit data register empty and transmission complete 

   - Receive data register full 

   - Receive overrun, parity error, framing error, and noise error 

   - Idle receiver detect 

   - Active edge on receive pin 

   - Break detect supporting LIN 

   - Receive data match 

- Hardware parity generation and checking 

- Programmable 7-bit, 8-bit, 9-bit or 10-bit character length 

- Programmable 1-bit or 2-bit stop bits 

- Support for three receiver wakeup methods: 

   - Idle line wakeup 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4213 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

   - Address mark wakeup 

   - Receive data match 

- Automatic address matching to reduce ISR overhead: 

   - Address mark matching 

   - Idle line address matching 

   - Address match start, address match end 

- Optional 13-bit/11-bit break character generation 

- Configurable idle length detection supporting 1, 2, 4, 8, 16, 32, 64, or 128 idle characters 

- Selectable transmitter output and receiver input polarity 

- Hardware flow control support for request to send (RTS) and clear to send (CTS) signals 

- Selectable IrDA 1.4 return-to-zero-inverted (RZI) format with programmable pulse width 

- Independent FIFO structure for transmit and receive 

   - Separate configurable watermark for receive and transmit requests 

   - Option for receiver to assert request after a configurable number of idle characters if receive FIFO is not empty 

## 76.3 Functional description 

The LPUART supports full-duplex, asynchronous, NRZ serial communication and comprises a baud rate generator, transmitter, and receiver block. The transmitter and receiver operate independently, although they use the same baud rate generator. The following describes each of the blocks of the LPUART. 

### 76.3.1 Low-power modes 

The LPUART remains functional during low power modes, provided the CTRL[DOZEEN] bit is clear and the LPUART functional clock remain enabled. The LPUART can generate an interrupt or DMA request to cause a wakeup from low power modes. 

The LPUART can be configured to be disabled in low power modes, when the CTRL[DOZEEN] bit is set. In this case the transmitter and receiver finish transmitting/receiving the current word. 

If the LPUART is disabled in low power modes, then it can generate a wakeup via the STAT[RXEDGIF] flag if the receiver detects an active edge. 

~~<mark>NOTE</mark>~~ 

See the chip-specific information to know the specific low-power modes available on your device. 

### 76.3.2 Debug mode 

The LPUART remains functional in debug mode. 

### 76.3.3 Baud rate generation 

A 13-bit modulus counter in the baud rate generator derives the baud rate for both the receiver and the transmitter. The value from 1 to 8191 written to BAUD[SBR] determines the baud clock divisor for the asynchronous LPUART baud clock. The baud rate clock drives the receiver, while the transmitter is driven by a bit clock which is generated from baud rate clock divided by the over sampling ratio (OSR). Depending on the over sampling ratio, the receiver has an acquisition rate of 4 to 32 samples per bit time. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4214 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/076_Low_Power_Universal_Asynchronous_Receiver_Transmitter_-LPUART-/S32K3XXRM_数据表.pdf-4215-02.png)


<!-- Start of picture text -->
Modulo Divide By OSR<br>(1 through 8191)<br>LPUART ASYNCH              Divide By  Tx Baud Rate<br>Module Clock            SBR[12:0] (OSR+1)<br>Baud Rate Generator  Rx Sampling Clock<br>Off If [SBR12:SBR0] =0 [(OSR+1) × Baud Rate]<br>LPUART ASYNCH Module Clock<br>Baud Rate =<br>SBR[12:0] × (OSR+1)<br><!-- End of picture text -->

Figure 466. LPUART baud rate generation 

Baud rate generation is subject to two sources of error: 

- Integer division of the asynchronous LPUART baud clock may not give the exact target frequency. 

- Synchronization with the asynchronous LPUART baud clock can cause phase shift. 

The baud rate generation is a free-running counter that continues whenever the transmitter or receiver is enabled. The transmitter bit clock continues whenever the transmitter is enabled; each transmitted character aligns to the next edge of the transmit bit clock. 

In general, configuring OSR for a higher oversampling ratio and/or sampling on both edges of the clock slightly improves the LPUART tolerance to baud rate mismatch between the received data and the LPUART configured baud rate. However, the three data samples in each bit will also be closer together which may impact noise sensitivity. 

### 76.3.4 Transmitter functional description 

This section describes the overall block diagram for the LPUART transmitter, as well as specialized functions for sending break and idle characters. 

The transmitter output (TXD) idle state defaults to logic high; the transmitter output is inverted by setting CTRL[TXINV]. CTRL[TXINV] is cleared following reset. The transmitter is enabled by setting the CTRL[TE] bit. This queues a preamble character that is one full character frame of the idle state. The transmitter then remains idle until data is available in the transmit FIFO. Programs store data into the transmit FIFO by writing to the DATA register. 

The central element of the LPUART transmitter is the transmit shift register that is 9-bit to 13-bit long depending on the setting in the CTRL[M], CTRL[M7], BAUD[M10] and BAUD[SBNS] control bits. For the remainder of this section, assume CTRL[M], CTRL[M7], BAUD[M10] and BAUD[SBNS] are cleared, selecting the normal 8-bit data mode. In 8-bit data mode, the shift register holds a start bit, eight data bits, and a stop bit. When the transmit shift register is available for a new character, the value waiting in the transmit data register is transferred to the transmit shift register, synchronized with the baud rate clock, and the transmit data register empty (STAT[TDRE]) status flag is set to indicate another character may be written to the transmit FIFO at the DATA register. 

If no new character is waiting in the transmit FIFO after a stop bit is shifted out of the TXD pin, the transmitter sets the transmit complete flag and enters an idle mode, with TXD high, waiting for more characters to transmit. 

Writing 0 to CTRL[TE] does not immediately disable the transmitter. The current transmit activity in progress must first be completed (that could include a data character, idle character or break character), although the transmitter does not start transmitting another character. 

#### 76.3.4.1 Send break and queued idle 

The CTRL[SBK] bit sends break characters originally used to gain the attention of old teletype receivers. Break characters are a full character time of logic 0, 9-bit to 12-bit times including the start and stop bits. A longer break of 13-bit times can be enabled by setting STAT[BRK13]. Normally, a program waits for STAT[TDRE] to become set to indicate the last character of a message has moved to the transmit shifter, write 1, and then write 0 to the CTRL[SBK] bit. This action queues a break character to be sent as soon as the shifter is available. If CTRL[SBK] remains 1 when the queued break moves into the shifter, synchronized to the baud rate clock, an additional break character is queued. When the LPUART is the receiving device, a break character is received as 0s in all data bits and a framing error (STAT[FE] = 1) is detected. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4215 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

A break character can also be transmitted by writing to the DATA register with DATA[FRETSC] set and the data bits clear. This supports transmitting the break character as part of the normal data stream and also allows the DMA to transmit a break character. 

When idle-line wakeup is used, a full character time of idle (logic 1) is needed between messages to wake up any sleeping receivers. Normally, a program waits for STAT[TDRE] to become set to indicate the last character of a message has moved to the transmit shifter, write 0, and then write 1 to the CTRL[TE] bit. This action queues an idle character to be sent as soon as the shifter is available. As long as the character in the shifter does not finish while CTRL[TE] is cleared, the LPUART transmitter never actually releases control of the TXD pin. 

An idle character can also be transmitted by writing to the DATA register with DATA[FRETSC] and DATA[T9] set, and all other bits cleared. This supports transmitting the idle character as part of the normal data stream and also allows the DMA to transmit a idle character. 

The length of the break character is affected by the STAT[BRK13], CTRL[M], CTRL[M7], BAUD[M10] and BAUD[SNBS] bits as shown below. 

Table 625. Break character length 

|BRK13|M|M10|M7|SBNS|Break character<br>length|
|---|---|---|---|---|---|
|0|0|0|0|0|10 bit times|
|0|0|0|0|1|11 bit times|
|0|0|0|1|0|9 bit times|
|0|0|0|1|1|10 bit times|
|0|1|0|X|0|11 bit times|
|0|1|0|X|1|12 bit times|
|0|X|1|X|0|12 bit times|
|0|X|1|X|1|13 bit times|
|1|0|0|0|0|13 bit times|
|1|0|0|0|1|13 bit times|
|1|0|0|1|0|12 bit times|
|1|0|0|1|1|12 bit times|
|1|1|0|X|0|14 bit times|
|1|1|0|X|1|14 bit times|
|1|X|1|X|0|15 bit times|
|1|X|1|X|1|15 bit times|



#### 76.3.4.2 Hardware flow control 

The transmitter supports hardware flow control by gating the transmission with the value of CTS_B. If the clear-to-send operation is enabled, the character is transmitted when CTS_B is asserted. If CTS_B is deasserted in the middle of a transmission with characters remaining in the transmitter FIFO, the character in the transmit shift register will be complete; any characters in the FIFO will wait for the CTS_B to assert again and TXD remains in the mark state (idle state) until CTS_B is reasserted. The CTS_B pin must assert for longer than one bit period to guarantee a new transmission is started when the transmitter is idle with data to send. 

If the clear-to-send operation is disabled, the transmitter ignores the state of CTS_B. 

The transmitter's CTS_B signal can be enabled even if the same LPUART receiver's RTS_B signal is disabled. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4216 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

#### 76.3.4.3 Transceiver driver enable 

The transmitter can use RTS_B as an enable signal for the driver of an external transceiver. See Transceiver driver enable using RTS_B for details. If the request-to-send operation is enabled, when a character is placed into an empty transmit shift register, RTS_B asserts one bit time before the start bit is transmitted. RTS_B remains asserted for the whole time that the transmit shift register has any characters. RTS_B deasserts one bit time after all characters in the transmit FIFO and shift register are completely sent, including the last stop bit. In other words, when RTS_B is used as a transceiver enable, the RTS_B asserts 1 bit time before the transmitter starts transmitting and negates 1 bit time after the transmitter goes idle. 

Transmitting a break character also asserts RTS_B, with the same assertion and deassertion timing as having a character in the transmit shift register. 

The transmitter's RTS_B signal asserts only when the transmitter is enabled. However, the transmitter's RTS_B signal is unaffected by its CTS_B signal. RTS_B remains asserted until the transfer is completed, even if the transmitter is disabled mid-way through a data transfer. 

The transmitter RTS_B negation can be delayed by up to 256 bit clock (baud rate) after the last stop bit by configuring the HDCR[RTSEXT] field to the desired length. 

#### 76.3.4.4 Transceiver driver enable using RTS_B 

RS-485 is a multiple drop communication protocol in which the LPUART transceiver's driver is 3-stated unless the LPUART is driving. The RTS_B signal can be used by the transmitter to enable the driver of a transceiver. The polarity of RTS_B can be matched to the polarity of the transceiver's driver enable signal. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/076_Low_Power_Universal_Asynchronous_Receiver_Transmitter_-LPUART-/S32K3XXRM_数据表.pdf-4217-09.png)


<!-- Start of picture text -->
LPUART      RS-485 TRANSCEIVER<br>TXD      DI      Y<br>TRANSMITTER     RTS_B      DE    DRIVER      Z<br>RXD      RO    A<br>RECEIVER      RE_B      RECEIVER      B<br><!-- End of picture text -->

Figure 467. Transceiver driver enable using RTS_B 

In the figure, the receiver enable signal is asserted. Another option for this connection is to connect RTS_B to both DE and RE_B. The transceiver's receiver is disabled while driving. A pullup can pull RXD to a non-floating value during this time. This option can be refined further by operating the LPUART in single wire mode, freeing the RXD pin for other uses. 

### 76.3.5 Receiver functional description 

In this section, the receiver block diagram is a guide for the overall receiver functional description. Next, the data sampling technique used to reconstruct receiver data is described in more detail. Finally, different variations of the receiver wakeup function are explained. 

The receiver input is inverted by setting STAT[RXINV]. The receiver is enabled by setting the CTRL[RE] bit. Character frames consist of a start bit of logic 0, seven to ten data bits (msb or lsb first), and one or two stop bits of logic 1. For information about 7-bit, 9-bit or 10-bit data mode, refer to Data Modes. For the remainder of this discussion, assume the LPUART is configured for normal 8-bit data mode. 

After receiving the stop bit into the receive shifter, and provided the receive data register is not already full, the data character is transferred to the receive data register and the receive data register full (STAT[RDRF]) status flag is set. If [RDRF] was already set indicating the receive data register (buffer) was already full, the overrun (OR) status flag is set and the new data is lost. 

Since the LPUART receiver is separate from the receive FIFO, the receive shift register can be receiving the next word when the receive FIFO is full and it is only at the end of the character that the next data is written into the receive FIFO, potentially triggering the overrun flag if FIFO is full. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4217 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

When a program detects that the receive data register is full (STAT[RDRF] = 1), it gets the data from the receive data register by reading the DATA register. Refer to Interrupts and status flags for details about flag clearing. 

#### 76.3.5.1 Data sampling technique 

The LPUART receiver supports a configurable oversampling rate of between 4× and 32× of the baud rate clock for sampling. The receiver starts by taking logic level samples at the oversampling rate times the baud rate to search for a falling edge on the RXD serial data input pin. A falling edge is defined as a logic 0 sample after three consecutive logic 1 samples. The oversampling baud rate clock divides the bit time into 4 to 32 segments from 1 to OSR (where OSR is the configured oversampling ratio). When a falling edge is located, three more samples are taken at (OSR/2), (OSR/2)+1, and (OSR/2)+2 to make sure this was a real start bit and not merely noise. If at least two of these three samples are 0, the receiver assumes it is synchronized to a received character. If another falling edge is detected before the receiver is considered synchronized, the receiver restarts the sampling from the first segment. 

The receiver then samples each bit time, including the start and stop bits, at (OSR/2), (OSR/2)+1, and (OSR/2)+2 to determine the logic level for that bit. The logic level is interpreted to be that of the majority of the samples taken during the bit time. If any sample in any bit time, including the start and stop bits, in a character frame fails to agree with the logic level for that bit, the noise flag (STAT[NF]) is set when the received character is transferred to the receive FIFO. 

When the LPUART receiver is configured to sample on both edges of the baud rate clock (that is, when BAUD[BOTHEDGE]=1), the number of segments in each received bit is effectively doubled (from 1 to OSR×2). The start and data bits are then sampled at OSR, OSR+1 and OSR+2. Sampling on both edges of the clock must be enabled for oversampling rates of 4× to 7× and is optional for higher oversampling rates. 

The "synchronization" is a feature of the LPUART module to synchronize the internal oversampling counter with detected falling edge on Rx signal, and to adjust the data sampling window. The falling edge detection needs three consecutive '1' prior to '1'->'0' transition. After the initial falling edge detection for the start bit, the circuit continuously monitors the next falling edge, and resets the counter once another falling edge is detected. This is called "resynchronization". 

- When LPUART_BAUD[RESYNCDIS] = 0, this falling edge detection and resynchronization is performed not only for the start bit but also for the rest of character reception after the start bit. 

- When LPUART_BAUD[RESYNCDIS] = 1, the falling edge detection and resynchronization is performed only for the start bit. The use case for disabling the resynchronization is protocols that require this (for example, LIN 2.1 prohibits resynchronization within a byte). 

See the following table and figure. 

Table 626. LPUART resynchronization 

|Resynchronization|LPUART_BAUD[RESYNCDIS]=0|LPUART_BAUD[RESYNCDIS]=1|
|---|---|---|
|For the starting bit falling<br>edge|Yes|Yes|
|For every falling edges after<br>the start bit|Yes|No|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4218 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/076_Low_Power_Universal_Asynchronous_Receiver_Transmitter_-LPUART-/S32K3XXRM_数据表.pdf-4219-02.png)


Figure 468. LPUART resynchronization 

#### 76.3.5.2 Receiver wakeup operation 

Receiver wakeup and receiver address matching is a hardware mechanism that allows an LPUART receiver to ignore the characters in a message intended for a different receiver. 

During receiver wakeup, all receivers evaluate the first character(s) of each message, and as soon as they determine the message is intended for a different receiver, they write logic 1 to the receiver wake up control bit (CTRL[RWU]). When CTRL[RWU] and STAT[RWUID] bit are set, the status flags associated with the receiver, with the exception of the idle bit, STAT[IDLE], are inhibited from setting, thus eliminating the software overhead for handling the unimportant message characters. At the end of a message, all receivers automatically force CTRL[RWU] to 0 so all receivers wake up in time to look at the first character(s) of the next message. 

During receiver address matching, the address matching is performed in hardware and the LPUART receiver ignores all characters that do not meet the address match requirements. 

Table 627. Receiver Wakeup Options 

|RWU|MA1 | MA2|MATCFG|WAKE:RWUID|Receiver Wakeup|
|---|---|---|---|---|
|0|0|X|X|Normal operation|
|1|0|00|00|Receiver wakeup on<br>idle line, IDLE flag not<br>set|
|1|0|00|01|Receiver wakeup on<br>idle line, IDLE flag set|
|1|0|00|10|Receiver wakeup on<br>address mark|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4219 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

Table 627. Receiver Wakeup Options (continued) 

|RWU|MA1 | MA2|MATCFG|WAKE:RWUID|Receiver Wakeup|
|---|---|---|---|---|
|1|1|11|10|Receiver wakeup on<br>data match|
|0|1|00|X0|Address mark address<br>match, IDLE flag not<br>set for discarded<br>characters|
|0|1|00|X1|Address mark address<br>match, IDLE flag set for<br>discarded characters|
|0|1|01|X0|Idle line address match|
|0|1|10|X0|Match On and Match<br>Off, IDLE flag not<br>set for discarded<br>characters|
|0|1|10|X1|Match On and Match<br>Off, IDLE flag set for<br>discarded characters|



#### 76.3.5.2.1 Idle-line wakeup 

When CTRL[WAKE] is cleared, the receiver is configured for idle-line wakeup. In this mode, CTRL[RWU] is cleared automatically when the receiver detects a full character time of the idle-line level. The CTRL[M], CTRL[M7], and BAUD[M10] control bits select 7-bit to 10-bit data mode and the BAUD[SBNS] bit selects 1-bit or 2-bit stop bit number that determines how many bit times of idle are needed to constitute a full character time, 9 to 13 bit times because of the start and stop bits. 

When CTRL[RWU] is 1 and STAT[RWUID] is 0, the idle condition that wakes up the receiver does not set the STAT[IDLE] flag. The receiver wakes up and waits for the first data character of the next message that sets the STAT[RDRF] flag and generates an interrupt if enabled. When STAT[RWUID] is 1, any idle condition sets the STAT[IDLE] flag and generates an interrupt if enabled, regardless of whether CTRL[RWU] is 0 or 1. 

The idle-line type (CTRL[ILT]) control bit selects one of two ways to detect an idle line. 

- When CTRL[ILT] is cleared, the idle bit counter starts after the start bit so the stop bit and any logic 1s at the end of a character count toward the full character time of idle. 

- When CTRL[ILT] is set, the idle bit counter does not start until after the stop bit time, so the idle detection is not affected by the data in the last character of the previous message. 

#### 76.3.5.2.2 Address-mark wakeup 

When CTRL[WAKE] is set, the receiver is configured for address-mark wakeup. In this mode, CTRL[RWU] is cleared automatically when the receiver detects a logic 1 in the most significant bit of the received character. When parity is enabled, the second most significant bit is used for address-mark wakeup. 

Address-mark wakeup allows messages to contain idle characters, but requires one bit be reserved for use in address frames. The logic 1 in the most significant bit (or second most significant bit when parity is enabled) of an address frame clears the CTRL[RWU] bit and sets the STAT[RDRF] flag. In this case, the character with the address-mark bit is received even though the receiver was sleeping during most of this character time. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4220 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

#### 76.3.5.2.3 Data match wakeup 

When CTRL[RWU] is set, CTRL[WAKE] is set and BAUD[MATCFG] equals 11, the receiver is configured for data match wakeup. In this mode, CTRL[RWU] is cleared automatically when the receiver detects a character that matches MATCH[MA1] field when BAUD[MAEN1] is set, or that matches MATCH[MA2] when BAUD[MAEN2] is set. 

#### 76.3.5.2.4 Address Match operation 

Address match operation is enabled when the BAUD[MAEN1] or BAUD[MAEN2] bit is set and BAUD[MATCFG] is equal to 00. In this function, a character received by the RXD pin with a logic 1 in the most significant bit (or second most significant bit when parity is enabled) is considered an address and is compared with the associated MATCH[MA1] or MATCH[MA2] field. The character is only transferred to the receive buffer, and STAT[RDRF] is set, if the comparison matches. All subsequent characters received with a logic 0 in the most significant bit (or second most significant bit when parity is enabled) are considered to be data associated with the address and are transferred to the receive FIFO. If no marked address match occurs then no transfer is made to the receive FIFO, and all following characters with logic zero in the most significant bit (or second most significant bit when parity is enabled) are also discarded. If both the BAUD[MAEN1] and BAUD[MAEN2] bits are negated, the receiver operates normally and all data received is transferred to the receive FIFO. 

Address match operation functions in the same way for both MATCH[MA1] and MATCH[MA2] fields. 

- If only one of BAUD[MAEN1] and BAUD[MAEN2] is asserted, a marked address is compared only with the associated match register field and data is transferred to the receive FIFO only on a match. 

- If BAUD[MAEN1] and BAUD[MAEN2] are asserted, a marked address is compared with both match registers and data is transferred only on a match with either of the MATCH[MA1] or MATCH[MA2] fields. 

#### 76.3.5.2.5 Idle Match operation 

Idle match operation is enabled when the BAUD[MAEN1] or BAUD[MAEN2] bit is set and BAUD[MATCFG] is equal to 01. In this function, the first character received by the RXD pin after an idle line condition is considered an address and is compared with the associated MATCH[MA1] or MATCH[MA2] field. The character is transferred only to the receive buffer, and STAT[RDRF] is set, if the comparison matches. All subsequent characters are considered to be data associated with the address and are transferred to the receive FIFO until the next idle line condition is detected. If no address match occurs then no transfer is made to the receive FIFO, and all following frames until the next idle condition are also discarded. If both the BAUD[MAEN1] and BAUD[MAEN2] bits are negated, the receiver operates normally and all data received is transferred to the receive FIFO. 

Idle match operation functions in the same way for both MATCH[MA1] or MATCH[MA2] fields. 

- If only one of BAUD[MAEN1] and BAUD[MAEN2] is asserted, the first character after an idle line is compared only with the associated match register and data is transferred to the receive FIFO only on a match. 

- If BAUD[MAEN1] and BAUD[MAEN2] are asserted, the first character after an idle line is compared with both MATCH[MA1] or MATCH[MA2] fields and data is transferred only on a match with either of the fields. 

#### 76.3.5.2.6 Match On Match Off operation 

Match on, match off operation is enabled when both BAUD[MAEN1] and BAUD[MAEN2] are set and BAUD[MATCFG] is equal to 10. In this function, a character received by the RXD pin that matches MATCH[MA1] is received and transferred to the receive buffer, and STAT[RDRF] is set. All subsequent characters are considered to be data and are also transferred to the receive FIFO, until a character is received that matches MATCH[MA2] field. The character that matches MATCH[MA2] and all following characters are discarded; this continues until another character that matches MATCH[MA1] is received. If both the BAUD[MAEN1] and BAUD[MAEN2] bits are negated, the receiver operates normally and all data received is transferred to the receive FIFO. 

~~<mark>NOTE</mark>~~ Match on, match off operation requires both BAUD[MAEN1] and BAUD[MAEN2] to be asserted. 

#### 76.3.5.3 Hardware flow control 

To support hardware flow control, the receiver can be programmed to automatically deassert and assert RTS_B. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4221 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

- RTS_B remains asserted until the transfer is complete, even if the transmitter is disabled midway through a data transfer. See Transceiver driver enable using RTS_B for more details. 

- If the receiver request-to-send functionality is enabled, the receiver automatically deasserts RTS_B if the number of characters in the receiver data register is full or a start bit is detected that causes the receiver data register to be full. 

- The receiver asserts RTS_B when the number of characters in the receiver data register is not full and has not detected a start bit that causes the receiver data register to be full. It is not affected if STAT[RDRF] is asserted. 

- Even if RTS_B is deasserted, the receiver continues to receive characters until the receive FIFO is overrun. 

- If the receiver request-to-send functionality is disabled, the receiver RTS_B remains deasserted. 

### 76.3.6 Additional LPUART functions 

The following sections describe additional LPUART functions. 

#### 76.3.6.1 Data Modes 

The LPUART transmitter and receiver can be configured to operate in 7-bit data mode by setting CTRL[M7], 9-bit data mode by setting the CTRL[M] or 10-bit data mode by setting BAUD[M10]. In 9-bit mode, there is a ninth data bit and in 10-bit mode, there is a tenth data bit. 

When performing 8-bit writes to the transmit FIFO, the 9th and 10th bit are pushed into the FIFO from CTRL[T8] and CTRL[T9]. For coherent 8-bit writes, write to CTRL[T8] and CTRL[T9] before writing to DATA[7:0], but if values in CTRL[T8] or CTRL[T9] do not need to change then it is not necessary to update CTRL[T8] and CTRL[T9] before every 8-bit write to the DATA register. 

When performing 16-bit or 32-bit writes to the transmit FIFO, all 10-bits are pushed into the transmit FIFO from the write data. 

When performing 8-bit reads of the receive FIFO, the 9th and 10th bit are held in CTRL[R8] and CTRL[R9] but should be read before reading the DATA register. A 16-bit or 32-bit read of the receive FIFO will return all 10-bits in the DATA register. 

The 9-bit data mode is typically used with parity to allow eight bits of data plus the parity in the ninth bit, or it is used with address-mark wakeup so the ninth data bit can serve as the wakeup bit. The 10-bit data mode is typically used with parity and address-mark wakeup so the ninth data bit can serve as the wakeup bit and the tenth bit as the parity bit. In custom protocols, the ninth and/or tenth bits can also serve as software-controlled markers. 

#### 76.3.6.2 Idle length 

An idle character is a character where the start bit, all data bits and stop bits are in the mark position (idle state, generally logic 1). The CTRL[ILT] bit can be configured to start detecting an idle character from the previous start bit (any data bits and stop bits count towards the idle character detection) or from the previous stop bit. 

The number of idle characters that must be received before an idle line condition is detected can also be configured using the CTRL[IDLECFG] field. This field configures the number of idle characters that must be received before the STAT[IDLE] flag is set, the STAT[RAF] flag is cleared and the DATA[IDLINE] flag is set with the next received character. 

Idle-line wakeup and idle match operation are also affected by the CTRL[IDLECFG] field. When address match or match on/off operation is enabled, setting the STAT[RWUID] bit causes any discarded characters to be treated as if they were idle characters. 

When the extended idle time is enabled for the receiver, an idle line condition can be configured using a 14-bit idle length register that specifies the number of bits (baud rate) since the last stop bit that is required for an idle condition to be detected. This replaces the ILT and IDLECFG configuration. 

The extended idle time can also be enabled for the transmitter, in this case any idle character queued through the transmit FIFO will force the transmitter to have idled for the configured number of bit clocks before the idle character is read from the FIFO and the transmitter continues. Note that when the transmitter extended idle time is enabled, the transmitter does not automatically queue an idle character whenever it is enabled. 

#### 76.3.6.3 Loop mode 

When CTRL[LOOPS] is set, the CTRL[RSRC] bit chooses between loop mode (CTRL[RSRC] = 0) or single-wire mode (CTRL[RSRC] = 1). Loop mode is sometimes used to check software, independent of connections in the external system, to help 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4222 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

isolate system problems. In this mode, the transmitter output is internally connected to the receiver input and the RXD pin is not used by the LPUART. 

Loop mode will also internally connect the RTS_B output to the CTS_B input and the DTR_B output to the DSR_B input. 

#### 76.3.6.4 Single-wire operation 

When CTRL[LOOPS] is set, the CTRL[RSRC] bit chooses between loop mode (CTRL[RSRC] = 0) or single-wire mode (CTRL[RSRC] = 1). Single-wire mode implements a half-duplex serial connection. The receiver is internally connected to the transmitter output and to the TXD pin (the RXD pin is not used). 

In single-wire mode, the CTRL[TXDIR] bit controls the direction of serial data on the TXD pin. When CTRL[TXDIR] is cleared, the TXD pin is an input to the receiver and the transmitter is temporarily disconnected from the TXD pin so an external device can send serial data to the receiver. When CTRL[TXDIR] is set, the TXD pin is an output driven by the transmitter, the internal loop back connection is disabled, and as a result the receiver cannot receive characters that are sent out by the transmitter. 

The Half Duplex Control Register replaces the CTRL[LOOPS] and CTRL[RSRC] implementation and can be used to configure various options for both single-wire operation or for half-duplex operation using independent RXD and TXD pins: 

- HDCR[TXSTALL] replaces the CTRL[TXDIR] functionality and prevents the transmitter from becoming busy or asserting transmitter RTS_B when STATUS[RAF] is set. 

- HDCR[RXSEL] configures for single-wire operation by selecting the TXD pin as the source for the receiver. When RXSEL is set, the TXD pin should be configured for open drain operation. 

- HDCR[RXMSK] masks the receiver input when the transmitter RTS_B is asserted (this applies even when the transmitter RTS_B is not configured as an output). 

- HDCR[RXWRMSK] blocks storing receive data to the receive FIFO when the transmitter RTS_B is asserted. The receiver idle functionality is not affected by this setting. 

- HDCR[RTSEXT] delays the negation of the trasmitter RTS_B by the configured number of bit clocks (baud rate). 

#### 76.3.6.5 Timeout Counter 

The LPUART implements 4 general purpose timeout counters, counters 0 and 1 are used to monitor the receiver and counters 2 and 3 are used to monitor the transmitter. When enabled, each counter can be configured to monitor one of the following conditions: 

- Idle time in number of bits, starting to increment when first enabled and an idle condition is detected. Counter restarts whenever a character is received/transmitted. 

- Idle time in number of bits, starting to increment after the next character is received/transmitted. Counter restarts whenever a character is received/transmitted. 

- Idle time is more than the timeout interval in number of bits, but less than the extended idle timout. Counter restarts whenever a character is received/transmitted. Can be used to detect a gap between characters that is greater than a threshold (timeout) but less than the configured extended idle time. This configuration requires the extended idle feature for the transmitter or receiver to be enabled for proper operation. 

- Number of characters received/transmitted is equal to the configured timeout. Will assert at the start of the character that equals the timeout value. 

The timeout counters restart counting whenever the counter is disabled and then enabled. The timeout counters are disabled while the corresponding timeout status flag is set. If the timeout enable is still set after the status flag is cleared, then the timeout counter will restart as if the counter had been disabled and then enabled. Idle time is measured in bit times from the end of the last stop bit and until a start bit has been validated. 

### 76.3.7 Infrared interface 

The LPUART provides the capability of transmitting narrow pulses to an IR LED and receiving narrow pulses and transforming them to serial bits, which are sent to the LPUART. The IrDA physical layer specification defines a half-duplex infrared 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4223 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

communication link for exchanging data. The full standard includes data rates up to 16 Mbits/s. The LPUART IrDA support is limited to SIR mode which supports data rates only between 2.4 kbits/s and 115.2 kbits/s. 

The LPUART has an infrared transmit encoder and receive decoder. The infrared decoder converts the received character from the IrDA format to the NRZ format used by the receiver. It also has a OSR oversampling baud rate clock counter that filters noise and indicates when a 1 is received. The LPUART transmits serial bits of data that are encoded by the infrared submodule to transmit a narrow pulse for every zero bit. No pulse is transmitted for every one bit. When receiving data, the IR pulses are detected using an IR photo diode (external to LPUART) and transformed to CMOS levels by the IR receive decoder. The narrow pulses are then stretched by the infrared receive decoder to get back to a serial bit stream to be received by the LPUART. The polarity of transmitted pulses and expected receive pulses can be inverted so that a direct connection can be made to external IrDA transceiver modules that use active high pulses. 

The infrared submodule receives its clock sources from the LPUART. One of these two clocks are selected in the infrared submodule to generate either 1/OSR, 2/OSR, 3/OSR, or 4/OSR narrow pulses during transmission. 

#### 76.3.7.1 Infrared transmit encoder 

The infrared transmit encoder converts serial bits of data from transmit shift register to the TXD signal. A narrow pulse is transmitted for a 0 bit and no pulse for a 1 bit. The narrow pulse is sent at the start of the bit with a duration of 1/OSR, 2/OSR, 3/OSR, or 4/OSR of a bit time. A narrow low pulse is transmitted for a 0 bit when CTRL[TXINV] is cleared, while a narrow high pulse is transmitted for a 0 bit when CTRL[TXINV] is set. 

#### 76.3.7.2 Infrared receive decoder 

The infrared receive block converts data from the RXD signal to the receive shift register. A narrow pulse is expected for each 0 received and no pulse is expected for each 1 received. A narrow low pulse is expected for a 0 bit when STAT[RXINV] is cleared, while a narrow high pulse is expected for a 0 bit when STAT[RXINV] is set. This receive decoder meets the edge jitter requirement as defined by the IrDA serial infrared physical layer specification. 

#### 76.3.7.3 Start bit detection 

When STAT[RXINV] is cleared, the first falling edge of the received character corresponds to the start bit. The infrared decoder resets its counter. At this time, the receiver also begins its start bit detection process. After the start bit is detected, the receiver synchronizes its bit times to this start bit time. For the rest of the character reception, the infrared decoder's counter and the receiver's bit time counter count independently from each other. 

#### 76.3.7.4 Noise filtering 

Any further rising edges detected during the first half of the infrared decoder counter are ignored by the decoder. Any pulses less than one oversampling baud clock can be undetected by it regardless of whether it is seen in the first or second half of the count. 

#### 76.3.7.5 Low-bit detection 

During the second half of the decoder count, a rising edge is decoded as a 0, which is sent to the receiver. The decoder counter is also reset. 

#### 76.3.7.6 High-bit detection 

At OSR oversampling baud rate clocks after the previous rising edge, if a rising edge is not seen, then the decoder sends a 1 to the receiver. 

If the next bit is a 0, which arrives late, then a low-bit is detected according to Low-bit detection. The value sent to the receiver is changed from 1 to a 0. Then, if a noise pulse occurs outside the receiver's bit time sampling period, then the delay of a 0 is not recorded as noise. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4224 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

### 76.3.8 Interrupts and status flags 

The LPUART transmitter has two status flags that can optionally generate hardware interrupt requests. Transmit Data Register Empty (STAT[TDRE]) indicates when there is room in the transmit FIFO to write another transmit character to the DATA register. If the Transmit Interrupt Enable (CTRL[TIE]) bit is set, a hardware interrupt is requested when STAT[TDRE] is set. Transmit complete (STAT[TC]) indicates that the transmitter is finished transmitting all data, preamble, and break characters and is idle with TXD at the inactive level. This flag is often used in systems with modems to determine when it is safe to turn off the modem. If the transmit complete interrupt enable (CTRL[TCIE]) bit is set, a hardware interrupt is requested when STAT[TC] is set. Instead of hardware interrupts, software polling may be used to monitor the STAT[TDRE] and STAT[TC] status flags if the corresponding CTRL[TIE] or CTRL[TCIE] local interrupt masks are cleared. 

When a program detects that the receive data register is full (STAT[RDRF] = 1), it gets the data from the receive data register by reading the DATA register. The STAT[RDRF] flag is cleared by reading the DATA register. 

The IDLE status flag includes logic that prevents it from getting set repeatedly when the RXD line remains idle for an extended period of time. IDLE is cleared by writing 1 to the STAT[IDLE] flag. After STAT[IDLE] has been cleared, it cannot become set again until the receiver has received at least one new character and has set STAT[RDRF]. 

If the associated error is detected in the received character that caused STAT[RDRF] to be set, the error flags — noise flag (STAT[NF]), framing error (STAT[FE]), and parity error flag (STAT[PF]) — are set at the same time as STAT[RDRF]. These flags are not set in overrun cases. 

If STAT[RDRF] is already set when a new character is ready to be transferred from the receive shifter to the receive FIFO, the overrun (STAT[OR]) flag is set instead of the data along with any associated STAT[NF], STAT[FE], or STAT[PF] condition is lost. 

If the received character matches the contents of MATCH[MA1] and/or MATCH[MA2] then the STAT[MA1F] and/or STAT[MA2F] flags are set at the same time that STAT[RDRF] is set. 

At any time, an active edge on the RXD serial data input pin causes the STAT[RXEDGIF] flag to set. The STAT[RXEDGIF] flag is cleared by writing a 1 to it. This function depends on the receiver being enabled (CTRL[RE] = 1). 

The MODEM Status Register can generate an interrupt from a configured status flag, this is indicated by STAT[MSF]. 

The Timeout Status Register can generate an interrupt from a configured status flag, this is indicated by STAT[TSF]. 

#### 76.3.8.1 DMA Burst Support 

To support efficient DMA transfers to the transmit FIFO, two alias regions are implemented to support incrementing 8-bit, 16-bit or 32-bit write accesses to the transmit FIFO. 

- Transmit Command Burst Register is a 512-byte region that supports pushing 16-bit DATA into the transmit FIFO 

- Transmit Data Burst Register is a 1024-byte region that supports pushing zero extended 8-bit DATA into the transmit FIFO 

The two regions are contiguous, so a DMA transfer can start in the TCBR region to initialize the transfer including address mark, idle word or break character, and then complete the transfer in the TDBR region with the data to transmit, without changing the transfer size. 

The transmit FIFO will block writes that overflow the FIFO, but this does not signal an error. Do not perform 32-bit writes to the TDBR unless there are 4 empty slots in the transmit FIFO. Do not perform 16-bit writes to the TDBR unless there are 2 empty slots in the transmit FIFO. 

### 76.3.9 Peripheral Triggers 

The connection of the LPUART peripheral triggers with other peripherals are device specific. 

##### Output Triggers 

The LPUART generates the following output triggers that can be connected to other peripherals on the device. 

- The transmit word trigger asserts at the end of each transmitted word, it negates after one bit period. 

- The transmit data trigger is identical to the TXD pin output, but without support for input trigger modulation. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4225 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

- The receive word trigger asserts at the end of each received word that is written to the receive FIFO, for one oversampling clock period. 

- The receive idle trigger asserts when the idle flag would set, and negates when the next valid start bit is detected. 

##### Input Trigger 

The LPUART supports one peripheral input trigger, that can be configured in one of the following ways. 

- The CTS function must be enabled. The input trigger can be connected in place of the CTS_B pin input. The input trigger must assert for longer than one bit clock period when the transmitter is idle with data to send to guarantee a new transmission. 

- The input trigger can modulate the transmit data output (trigger is logically ANDed with the TXD output). The input trigger is expected to be a free running clock (carrier signal) generated from a timer or PWM source with a frequency that is greater than the bit clock frequency. The carrier signal must not toggle faster than the maximum supported bit time. 

- The input trigger can be connected in place of the RXD pin input. The input trigger is expected to be generated from a receive data source, such as analog comparator or external pin. 

## 76.4 Clocking and Resets 

Table 628. Clocks 

|LPUART Functional<br>clock|The LPUART functional clock is asynchronous to the bus clock and can remain enabled in low<br>power modes to support transmit and/or receive, including low power wakeups.|
|---|---|
|Bus clock|The bus clock is only used for bus accesses to the control and configuration registers. The bus<br>clock frequency must be sufficient to support the data bandwidth requirements of the LPUART<br>transmit and receive registers, including the FIFOs.|



Table 629. Resets 

|Chip reset|The logic and registers for the LPUART transmitter and receiver are reset to their default state on a<br>chip reset.|
|---|---|
|Software reset|Resets the LPUART logic and registers to their default state, except for the Global Register. The<br>LPUART software reset is in the Global Register GLOBAL[RST].|
|FIFO reset|The LPUART implements write-only control bits that reset the transmit FIFO (FIFO[TXFLUSH]) and<br>receive FIFO (FIFO[RXFLUSH]). After a FIFO is reset, that FIFO is empty.|



## 76.5 External signals 

Table 630. 

|Signal|Description|I/O|
|---|---|---|
|TXD|Transmit data. This pin is normally<br>an output, but is an input (tristated)<br>in single wire mode whenever the<br>transmitter is disabled or transmit<br>direction is configured for receive data.|I/O|
|RXD|Receive data.|I|
|CTS_B|Clear to send.|I|
|RTS_B|Request to send.|O|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4226 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

Table 630. (continued) 

|Signal|Description|I/O|
|---|---|---|
|DTR_B|Data Terminal Ready.|O|
|DSR_B|Data Set Ready.|I|
|DCD_B|Data Carrier Detect.|I|
|RIN_B|Ring Indicator.|I|



## 76.6 Register definition 

The LPUART includes registers to control baud rate, select options, report status, and store transmit/receive data. Access to an address outside the valid memory map generates a bus error. 

~~<mark>NOTE</mark>~~ 

Writing a Read-Only (RO) register or reading a Write-Only (WO) register can cause bus errors. This module does not check if programmed values in the registers are correct; the application software must ensure that valid programmed values are being written. 

### 76.6.1 LPUART register descriptions 

76.6.1.1 LPUART memory map 

LPUART_0 base address: 4032_8000h LPUART_1 base address: 4032_C000h LPUART_2 base address: 4033_0000h LPUART_3 base address: 4033_4000h LPUART_4 base address: 4033_8000h LPUART_5 base address: 4033_C000h LPUART_6 base address: 4034_0000h LPUART_7 base address: 4034_4000h LPUART_8 base address: 4048_C000h LPUART_9 base address: 4049_0000h LPUART_10 base address: 4049_4000h LPUART_11 base address: 4049_8000h LPUART_12 base address: 4049_C000h LPUART_13 base address: 404A_0000h LPUART_14 base address: 404A_4000h LPUART_15 base address: 404A_8000h 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4227 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|0h|Version ID Register (VERID)|32|RO|See<br>description|
|4h|Parameter Register (PARAM)|32|RO|See<br>description|
|8h|LPUART Global Register (GLOBAL)|32|RW|0000_0000h|
|Ch|LPUART Pin Configuration Register (PINCFG)|32|RW|0000_0000h|
|10h|LPUART Baud Rate Register (BAUD)|32|RW|0F00_0004h|
|14h|LPUART Status Register (STAT)|32|RW|00C0_0000h|
|18h|LPUART Control Register (CTRL)|32|RW|0000_0000h|
|1Ch|LPUART Data Register (DATA)|32|RW|0000_1000h|
|20h|LPUART Match Address Register (MATCH)|32|RW|0000_0000h|
|24h|LPUART Modem IrDA Register (MODIR)|32|RW|0000_0000h|
|28h|LPUART FIFO Register (FIFO)|32|RW|See<br>description|
|2Ch|LPUART Watermark Register (WATER)|32|RW|0000_0000h|
|30h|Data read-only Register (DATARO)|32|RO|0000_1000h|
|40h|MODEM Control Register (MCR)|32|RW|0000_0000h|
|44h|MODEM Status Register (MSR)|32|W1C|0000_0000h|
|48h|Receiver Extended Idle Register (REIR)|32|RW|0000_0000h|
|4Ch|Transmitter Extended Idle Register (TEIR)|32|RW|0000_0000h|
|50h|Half Duplex Control Register (HDCR)|32|RW|0000_0000h|
|58h|Timeout Control Register (TOCR)|32|RW|0000_0000h|
|5Ch|Timeout Status Register (TOSR)|32|W1C|0000_000Fh|
|60h - 6Ch|Timeout N Register (TIMEOUT0 - TIMEOUT3)|32|RW|0000_0000h|
|200h - 3FCh|Transmit Command Burst Register (TCBR0 - TCBR127)|32|WO|0000_0000h|
|400h - 7FCh|Transmit Data Burst Register (TDBR0 - TDBR255)|32|WO|0000_0000h|



#### 76.6.1.2 Version ID Register (VERID) 

##### Offset 

|Register|Offset|
|---|---|
|VERID|0h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4228 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Function 

The Version ID register indicates the version integrated for this instance on the device and also indicates inclusion/exclusion of several optional features. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/076_Low_Power_Universal_Asynchronous_Receiver_Transmitter_-LPUART-/S32K3XXRM_数据表.pdf-4229-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R MAJOR  MINOR<br>W<br>Reset See Register reset values.<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R FEATURE<br>W<br>Reset See Register reset values.Register reset values..<br><!-- End of picture text -->

See Register reset values.Register reset values.. 

##### Register reset values 

|Register|Reset value|
|---|---|
|VERID|LPUART_0,LPUART_1: 0404_0007h|
||LPUART_2–LPUART_15: 0404_0003h|



##### Fields 

|Field|Function|
|---|---|
|31-24|Major Version Number|
|MAJOR|This read-only field returns the major version number for the module specification.|
|23-16|Minor Version Number|
|MINOR|This read-only field returns the minor version number for the module specification.|
|15-0|Feature Identification Number|
|FEATURE|This read-only field returns the feature set number.<br>0000_0000_0000_0001b - Standard feature set.|
||0000_0000_0000_0011b - Standard feature set with MODEM/IrDA support.<br>0000_0000_0000_0111b - Enhanced feature set with full MODEM, IrDA and enhanced idle<br>detection.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4229 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

#### 76.6.1.3 Parameter Register (PARAM) 

##### Offset 

|Register|Offset|
|---|---|
|PARAM|4h|



##### Function 

The Parameter register indicates the parameter configuration for this instance on the device. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/076_Low_Power_Universal_Asynchronous_Receiver_Transmitter_-LPUART-/S32K3XXRM_数据表.pdf-4230-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset See Register reset values.<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RXFIFO  TXFIFO<br>W<br>Reset See Register reset values.<br><!-- End of picture text -->

##### Register reset values 

|Register|Reset value|
|---|---|
|PARAM|LPUART_0,LPUART_1: 0000_0404h|
||LPUART_2–LPUART_15: 0000_0202h|



##### Fields 

|Field|Function|
|---|---|
|31-16<br>—|Reserved|
|15-8|Receive FIFO Size|
|RXFIFO|The number of characters in the receive FIFO is 2^RXFIFO.|
|7-0|Transmit FIFO Size|
|TXFIFO|The number of characters in the transmit FIFO is 2^TXFIFO.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4230 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

#### 76.6.1.4 LPUART Global Register (GLOBAL) 

##### Offset 

|Register|Offset|
|---|---|
|GLOBAL|8h|



##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||||||0||||||||RST|0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-2|Reserved|
|—||
|1|Software Reset|
|RST|Resets all internal logic and registers, except the Global Register. The reset takes effect immediately<br>and remains asserted until negated by software. There is no minimum delay required before clearing the<br>software reset.|
||0b - Module is not reset.|
||1b - Module is reset.|
|0<br>—|Reserved|



#### 76.6.1.5 LPUART Pin Configuration Register (PINCFG) 

##### Offset 

|Register|Offset|
|---|---|
|PINCFG|Ch|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4231 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0||||||||
|W||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R<br>W||||||||0|||||||TRGSEL|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



##### Fields 

|Field|Function|
|---|---|
|31-2|Reserved|
|—||
|1-0|Trigger Select|
|TRGSEL|Configures the input trigger usage. This field should be changed only when the transmitter and receiver<br>are both disabled.|
||00b - Input trigger is disabled.<br>01b - Input trigger is used instead of RXD pin input.<br>10b - Input trigger is used instead of CTS_B pin input.<br>11b - Input trigger is used to modulate the TXD pin output. The TXD pin output (after TXINV<br>configuration) is internally ANDed with the input trigger.|



#### 76.6.1.6 LPUART Baud Rate Register (BAUD) 

##### Offset 

|Register|Offset|
|---|---|
|BAUD|10h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4232 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/076_Low_Power_Universal_Asynchronous_Receiver_Transmitter_-LPUART-/S32K3XXRM_数据表.pdf-4233-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R MAEN MAEN M10  OSR  TDMA 0 RDMA ed  MATCFG  BOTH RESY<br>1  2  E  E  EDGE  NCD...<br>W 0<br>Reset 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R LBKDI RXED<br>SBNS  SBR<br>W E  GIE<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Match Address Mode Enable 1|
|MAEN1|0b - Normal operation.<br>1b - Enables automatic address matching or data matching mode for MATCH[MA1].|
|30|Match Address Mode Enable 2|
|MAEN2|0b - Normal operation.<br>1b - Enables automatic address matching or data matching mode for MATCH[MA2].|
|29|10-bit Mode select|
|M10|The M10 bit causes a tenth bit to be part of the serial transmission. This bit should be changed only<br>when the transmitter and receiver are both disabled.<br>0b - Receiver and transmitter use 7-bit to 9-bit data characters.<br>1b - Receiver and transmitter use 10-bit data characters.|
|28-24<br>OSR|Oversampling Ratio<br>This field configures the oversampling ratio for the receiver. This field should be changed only when the<br>transmitter and receiver are both disabled.<br>0_0000b - Writing 0 to this field results in an oversampling ratio of 16<br>0_0001b - Reserved|
||0_0010b - Reserved|
||0_0011b - Oversampling ratio of 4, requires BOTHEDGE to be set.<br>0_0100b - Oversampling ratio of 5, requires BOTHEDGE to be set.|
||0_0101b - Oversampling ratio of 6, requires BOTHEDGE to be set.|
||0_0110b - Oversampling ratio of 7, requires BOTHEDGE to be set.|
||0_0111b - Oversampling ratio of 8.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4233 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0_1000b - Oversampling ratio of 9.<br>0_1001b - Oversampling ratio of 10.<br>0_1010b - Oversampling ratio of 11.<br>0_1011b - Oversampling ratio of 12.<br>0_1100b - Oversampling ratio of 13.<br>0_1101b - Oversampling ratio of 14.<br>0_1110b - Oversampling ratio of 15.<br>0_1111b - Oversampling ratio of 16.|
||1_0000b - Oversampling ratio of 17.|
||1_0001b - Oversampling ratio of 18.|
||1_0010b - Oversampling ratio of 19.|
||1_0011b - Oversampling ratio of 20.|
||1_0100b - Oversampling ratio of 21.|
||1_0101b - Oversampling ratio of 22.|
||1_0110b - Oversampling ratio of 23.|
||1_0111b - Oversampling ratio of 24.|
||1_1000b - Oversampling ratio of 25.<br>1_1001b - Oversampling ratio of 26.<br>1_1010b - Oversampling ratio of 27.<br>1_1011b - Oversampling ratio of 28.<br>1_1100b - Oversampling ratio of 29.<br>1_1101b - Oversampling ratio of 30.|
||1_1110b - Oversampling ratio of 31.|
||1_1111b - Oversampling ratio of 32.|
|23<br>TDMAE|Transmitter DMA Enable<br>TDMAE configures the transmit data register empty flag, STAT[TDRE], to generate a DMA request.<br>0b - DMA request disabled.|
||1b - DMA request enabled.|
|22<br>—|Reserved|
|21|Receiver Full DMA Enable|
|RDMAE|RDMAE configures the receiver data register full flag, STAT[RDRF], to generate a DMA request.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4234 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - DMA request disabled.<br>1b - DMA request enabled.|
|20<br>—|Reserved|
|19-18<br>MATCFG|Match Configuration<br>Configures the match addressing mode used. This field should be changed only when the transmitter<br>and receiver are both disabled.<br>00b - Address Match Wakeup<br>01b - Idle Match Wakeup<br>10b - Match On and Match Off<br>11b - Enables RWU on Data Match and Match On/Off for transmitter CTS input|
|17<br>BOTHEDGE|Both Edge Sampling<br>Enables sampling of the received data on both edges of the baud rate clock, effectively doubling the<br>number of times the receiver samples the input data for a given oversampling ratio. This bit must be set<br>for oversampling ratios between x4 and x7 and is optional for higher oversampling ratios. This bit should<br>be changed only when the receiver is disabled.<br>0b - Receiver samples input data using the rising edge of the baud rate clock.<br>1b - Receiver samples input data using the rising and falling edge of the baud rate clock.|
|16|Resynchronization Disable|
|RESYNCDIS|When set, this field disables the resynchronization of the received data word when a data one followed<br>by data zero transition is detected. This bit should be changed only when the receiver is disabled.<br>0b - Resynchronization during received data word is supported.<br>1b - Resynchronization during received data word is disabled.|
|15<br>LBKDIE|LIN Break Detect Interrupt Enable<br>LBKDIE enables the LIN break detect flag, STAT[LBKDIF], to generate interrupt requests.<br>0b - Hardware interrupts from STAT[LBKDIF] flag are disabled (use polling).<br>1b - Hardware interrupt is requested when STAT[LBKDIF] flag is 1.|
|14|RX Input Active Edge Interrupt Enable|
|RXEDGIE|Enables the receive input active edge, STAT[RXEDGIF], to generate interrupt requests. Changing<br>CTRL[LOOPS] or CTRL[RSRC] when RXEDGIE is set can cause the STAT[RXEDGIF] flag to set.<br>0b - Hardware interrupts from STAT[RXEDGIF] are disabled.<br>1b - Hardware interrupt is requested when STAT[RXEDGIF] flag is 1.|
|13|Stop Bit Number Select|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4235 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|SBNS|SBNS determines whether data characters have one or two stop bits. This bit should be changed only<br>when the transmitter and receiver are both disabled.<br>0b - One stop bit.|
||1b - Two stop bits.|
|12-0|Baud Rate Modulo Divisor.|
|SBR|The 13 bits in SBR[12:0] set the modulo divide rate for the baud rate generator. When SBR is 1 - 8191,<br>the baud rate equals "baud clock / ((OSR+1) * SBR)". The 13-bit baud rate setting [SBR12:SBR0] must<br>be updated only when the transmitter and receiver are both disabled (CTRL[RE] and CTRL[TE] are both<br>0).|



#### 76.6.1.7 LPUART Status Register (STAT) 

##### Offset 

|Register|Offset|
|---|---|
|STAT|14h|



##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/076_Low_Power_Universal_Asynchronous_Receiver_Transmitter_-LPUART-/S32K3XXRM_数据表.pdf-4236-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>LBKDI RXED<br>R F  GIF  MSBF  RXINV  RWUI BRK13  LBKD RAF  TDRE  TC  RDRF  IDLE  OR  NF  FE  PF<br>D  E<br>W W1C W1C W1C W1C W1C W1C W1C<br>Reset 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R MA1F  MA2F  0 TSF  MSF  0<br>AME  LBKFE<br>W W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|LIN Break Detect Interrupt Flag|
|LBKDIF|LBKDIF is set when the LIN break detect circuitry is enabled and a LIN break character is detected.<br>Writing a 1 clears the LBKDIF field.|
||0b - No LIN break character has been detected.|
||1b - LIN break character has been detected.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4236 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|30<br>RXEDGIF|RXD Pin Active Edge Interrupt Flag<br>RXEDGIF is set whenever the receiver is enabled and an active edge (falling if RXINV = 0, rising if<br>RXINV=1,) on the RXD pin occurs. To clear RXEDGIF, write a 1 to the RXEDGIF field.<br>0b - No active edge on the receive pin has occurred.<br>1b - An active edge on the receive pin has occurred.|
|29<br>MSBF|MSB First<br>Setting this bit reverses the order of the bits that are transmitted and received on the wire. This bit does<br>not affect the polarity of the bits, the location of the parity bit, or the location of the start or stop bits. This<br>bit should be changed only when the transmitter and receiver are both disabled.<br>0b - LSB (bit0) is the first bit that is transmitted following the start bit. Further, the first bit received<br>after the start bit is identified as bit0.<br>1b - MSB (identified as bit9, bit8, bit7 or bit6) is the first bit that is transmitted following the start bit<br>depending on the setting of CTRL[M], CTRL[PE] and BAUD[M10]. .|
|28<br>RXINV|Receive Data Inversion<br>Setting this bit reverses the polarity of the received data input. This bit should be changed only when the<br>receiver is disabled.<br>Setting RXINV inverts the RXD input for all cases: data bits, start and stop bits, break,<br>and idle.<br>~~NOTE~~<br>0b - Receive data not inverted.<br>1b - Receive data inverted.|
|27<br>RWUID|Receive Wake Up Idle Detect<br>For RWU on idle character, RWUID controls whether the idle character that wakes up the receiver sets<br>the IDLE bit. For address match wakeup, RWUID controls if the IDLE bit is set when the address does<br>not match. This bit should be changed only when the receiver is disabled.<br>0b - During receive standby state (RWU = 1), the IDLE bit does not get set upon detection of an<br>idle character. During address match wakeup, the IDLE bit does not set when an address does<br>not match.<br>1b - During receive standby state (RWU = 1), the IDLE bit gets set upon detection of an idle<br>character. During address match wakeup, the IDLE bit does set when an address does not<br>match.|
|26<br>BRK13|Break Character Generation Length<br>BRK13 selects a longer transmitted break character length. The state of this bit does not affect the<br>detection of a framing error. This bit should be changed only when the transmitter is disabled. A break<br>character can be sent by setting CTRL[SBK] or by writing the transmit FIFO with DATA[FRETSC] set<br>and DATA[R9T9] clear.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4237 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Field|Function<br>0b - Break character is transmitted with length of 9 to 13 bit times.<br>1b - Break character is transmitted with length of 12 to 15 bit times.|
|---|---|
|25<br>LBKDE|LIN Break Detection Enable<br>LBKDE selects a longer break character detection length. While LBKDE is set, receive data is not stored<br>in the receive FIFO.<br>~~NOTE~~|
||The LBKDE bit enables the LIN break detect circuit and disables writing receive data to<br>FIFO. So it essentially ignores all characters except a LIN break.|
||0b - LIN break detect is disabled, normal break character can be detected.<br>1b - LIN break detect is enabled. LIN break character is detected at length of 11 bit times (if M =<br>0) or 12 (if M = 1) or 13 (M10 = 1).|
|24<br>RAF|Receiver Active Flag<br>RAF is set when the receiver detects the beginning of a valid start bit, and RAF is cleared automatically<br>when the receiver detects an idle line.<br>0b - LPUART receiver idle waiting for a start bit.<br>1b - LPUART receiver active (RXD input not idle).|
|23<br>TDRE|Transmit Data Register Empty Flag<br>When the transmit FIFO is enabled, TDRE is set when the number of datawords in the transmit FIFO is equal<br>to or less than the number indicated by WATER[TXWATER]. To clear TDRE, write to the DATA register<br>until the number of words in the transmit FIFO is greater than the number indicated by WATER[TXWATER].<br>When the transmit FIFO is disabled, TDRE is set when the transmit DATA register is empty. To clear TDRE,<br>write to the DATA register.<br>TDRE is not affected by a character that is in the process of being transmitted; it is updated at the start of<br>each transmitted character.<br>0b - Transmit FIFO level is greater than watermark.|
||1b - Transmit FIFO level is equal or less than watermark.|
|22|Transmission Complete Flag|
|TC|TC is cleared when there is a transmission in progress or when a preamble or break character is<br>loaded. TC is set when the transmit buffer is empty and no data, preamble, or break character is being<br>transmitted. When TC is set, the transmit data output signal becomes idle (logic 1). TC is cleared by<br>writing to the DATA register to transmit new data, queuing a preamble by clearing and then setting<br>CTRL[TE], queuing a break character by writing 1 to CTRL[SBK].<br>0b - Transmitter active (sending data, a preamble, or a break).<br>1b - Transmitter idle (transmission activity complete).|
|21<br>RDRF|Receive Data Register Full Flag|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4238 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Field|Function<br>When the receive FIFO is enabled, RDRF is set when the number of datawords in the receive buffer<br>is greater than the number indicated by WATER[RXWATER]. To clear RDRF, read the DATA register<br>until the number of datawords in the receive FIFO is equal to or less than the number indicated by<br>WATER[RXWATER]. When the receive FIFO is disabled, RDRF is set when the receive buffer (the DATA<br>register) is full. To clear RDRF, read the DATA register.<br>A character that is in the process of being received does not cause a change in RDRF until the entire<br>character is received. Even if RDRF is set, the character continues to be received until an overrun condition<br>occurs once the entire character is received.<br>0b - Receive FIFO level is less than watermark.<br>1b - Receive FIFO level is equal or greater than watermark.|
|---|---|
|20<br>IDLE|Idle Line Flag<br>IDLE is set when the LPUART receive line becomes idle for a full character time after a period of activity.<br>When CTRL[ILT] is cleared, the receiver starts counting idle bit times after the start bit. If the receive<br>character is all 1s, these bit times and the stop bits time count toward the full character time of logic high,<br>10 to 13 bit times, needed for the receiver to detect an idle line. When CTRL[ILT] is set, the receiver doesn't<br>start counting idle bit times until after the stop bits. The stop bits and any logic high bit times at the end of the<br>previous character do not count toward the full character time of logic high needed for the receiver to detect<br>an idle line.<br>To clear IDLE, write logic 1 to the IDLE flag. After IDLE has been cleared, it cannot be set again until after<br>a new character is stored in the receive buffer or a LIN break character has set the LBKDIF flag . IDLE is<br>set only once even if the receive line remains idle for an extended period.<br>0b - No idle line detected.<br>1b - Idle line is detected.|
|19<br>OR|Receiver Overrun Flag<br>OR is set when software fails to prevent the receive data register from overflowing with data. The OR bit is<br>set immediately after the stop bit has been completely received for the dataword that overflows the buffer<br>and all the other error flags (FE, NF, and PF) are prevented from setting. The data in the shift register is lost,<br>but the data already in the LPUART data registers is not affected. If LBKDE is enabled and a LIN Break is<br>detected, the OR field asserts if LBKDIF is not cleared before the next data character is received.<br>While the OR flag is set, no additional data is stored in the receive FIFO even if sufficient room exists. To<br>clear OR, write logic 1 to the OR flag.<br>0b - No overrun.<br>1b - Receive overrun (new LPUART data lost).|
|18<br>NF|Noise Flag<br>The advanced sampling technique used in the receiver takes three samples in each of the received bits.<br>If any of these samples disagrees with the rest of the samples within any bit time in the frame then noise<br>is detected for that character. NF is set whenever the next character to be read from the DATA register is<br>received with noise detected within the character. To clear NF, write logic 1 to the NF field.<br>0b - No noise detected.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4239 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Field|Function<br>1b - Noise detected in the received character in the DATA register.|
|---|---|
|17<br>FE|Framing Error Flag<br>FE is set whenever the next character to be read from the DATA register is received with logic 0<br>detected where a stop bit was expected. To clear FE, write logic 1 to the FE field.<br>0b - No framing error detected. This does not guarantee the framing is correct.<br>1b - Framing error.|
|16<br>PF|Parity Error Flag<br>PF is set whenever the next character to be read from the DATA register is received when parity is<br>enabled (PE = 1) and the parity bit in the received character does not agree with the expected parity<br>value. To clear PF, write a logic 1 to the PF field.<br>0b - No parity error.<br>1b - Parity error.|
|15<br>MA1F|Match 1 Flag<br>MA1F is set whenever the next character to be read from the DATA register matches MA1. To clear<br>MA1F, write a logic 1 to the MA1F field.<br>0b - Received data is not equal to MA1<br>1b - Received data is equal to MA1|
|14<br>MA2F|Match 2 Flag<br>MA2F is set whenever the next character to be read from the DATA register matches MA2. To clear<br>MA2F, write a logic 1 to the MA2F field.<br>0b - Received data is not equal to MA2<br>1b - Received data is equal to MA2|
|13-10<br>—|Reserved|
|9<br>TSF|Timeout Status Flag<br>Indicates that a flag in the Timeout Status Register is set and configured to generate an interrupt.<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>~~NOTE~~|
||Instance<br>Field supported in<br>Field not supported in|
||LPUART_0<br>STAT<br>—|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4240 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Field|Function|||
|---|---|---|---|
||Instance|Field supported in|Field not supported in|
||LPUART_1|STAT|—|
||LPUART_2|—|STAT|
||LPUART_3|—|STAT|
||LPUART_4|—|STAT|
||LPUART_5|—|STAT|
||LPUART_6|—|STAT|
||LPUART_7|—|STAT|
||LPUART_8|—|STAT|
||LPUART_9|—|STAT|
||LPUART_10|—|STAT|
||LPUART_11|—|STAT|
||LPUART_12|—|STAT|
||LPUART_13|—|STAT|
||LPUART_14|—|STAT|
||LPUART_15|—|STAT|
||0b - Flag is clear<br>1b - Flag is set|||
|8<br>MSF|MODEM Status Flag<br>Indicates that a flag in the MODE<br>This field is not suppor<br>supported registers.|M Status Register is set and conf<br>ted in every instance. The following ta<br>~~NOTE~~|igured to generate an interrupt.<br>ble includes only|
||Instance|Field supported in|Field not supported in|
||LPUART_0|STAT|—|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4241 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Field|Function||
|---|---|---|
||Instance<br>Field supported in|Field not supported in|
||LPUART_1<br>STAT|—|
||LPUART_2<br>—|STAT|
||LPUART_3<br>—|STAT|
||LPUART_4<br>—|STAT|
||LPUART_5<br>—|STAT|
||LPUART_6<br>—|STAT|
||LPUART_7<br>—|STAT|
||LPUART_8<br>—|STAT|
||LPUART_9<br>—|STAT|
||LPUART_10<br>—|STAT|
||LPUART_11<br>—|STAT|
||LPUART_12<br>—|STAT|
||LPUART_13<br>—|STAT|
||LPUART_14<br>—|STAT|
||LPUART_15<br>—|STAT|
||0b - Flag is clear<br>1b - Flag is set||
|7-2<br>—|Reserved||
|1<br>AME|Address Mark Enable<br>Configures the location of the address mark when configured for MS<br>effect when configured for LSB first. This bit should be changed only<br>are both disabled.<br>0b - Address mark in character is MSB.<br>1b - Address mark in character is last bit before stop bit (or p<br>DATA register at MSB (or MSB-1 when parity bit enabled).<br>Table continues on the next page...|B first transfers. This bit has no<br>when the transmitter and receiver<br>arity bit when enabled) and stored in|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4242 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|0|LIN Break Flag Enable|
|LBKFE|Enables the LIN Break Flag to assert whenever a LIN break character is detected. Unlike LBKDE, this does<br>not impact data being stored in the receive data buffer, but does cause LBKDIF to assert whenever a LIN<br>break is detected.|
||Since a LIN break is longer than a normal character, the LIN break will trigger a write to the receive data<br>register with the data bits clear and the Framing Error set. The character following the LIN break has the<br>LINBRK flag set to indicate the previous character was a LIN break.<br>This bit should be changed only when the transmitter and receiver are both disabled.<br>0b - LIN break detect is disabled.|
||1b - LIN break detect is enabled. LIN break character is detected at length of 11 bit times (if M =<br>0) or 12 (if M = 1) or 13 (M10 = 1).|



#### 76.6.1.8 LPUART Control Register (CTRL) 

##### Offset 

|Register|Offset|
|---|---|
|CTRL|18h|



##### Function 

This read/write register controls various optional features of the LPUART system. This register should only be altered when the transmitter and receiver are both disabled. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/076_Low_Power_Universal_Asynchronous_Receiver_Transmitter_-LPUART-/S32K3XXRM_数据表.pdf-4243-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>R8T9  R9T8  TXDIR  TXINV  ORIE  NEIE  FEIE  PEIE  TIE  TCIE  RIE  ILIE  TE  RE  RWU  SBK<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 LOOP DOZE<br>MA1IE  MA2IE  M7  IDLECFG  RSRC  M  WAKE  ILT  PE  PT<br>W S  EN<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4243 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Fields 

|Field<br>31<br>R8T9|Function<br>Receive Bit 8 / Transmit Bit 9<br>R8 is the ninth data bit received when the LPUART is configured for 9-bit or 10-bit data formats. When<br>reading 9-bit or 10-bit data, read R8 before reading the DATA register.<br>T9 is the tenth data bit transmitted when the LPUART is configured for 10-bit data formats. When writing<br>10-bit data, write T9 before writing the DATA register. If T9 does not need to change from its previous value,<br>such as when it is used to generate address mark or parity, then it need not be written each time the DATA<br>register is written.<br>R8 is a read-only bit and T9 is a write-only bit, the value read is different from the<br>value written.<br>~~NOTE~~|
|---|---|
|30<br>R9T8|Receive Bit 9 / Transmit Bit 8<br>R9 is the tenth data bit received when the LPUART is configured for 10-bit data formats. When reading 10-bit<br>data, read R9 before reading the DATA register<br>T8 is the ninth data bit transmitted when the LPUART is configured for 9-bit or 10-bit data formats. When<br>writing 9-bit or 10-bit data, write T8 before writing the DATA register. If T8 does not need to change from its<br>previous value, such as when it is used to generate address mark or parity, then it need not be written each<br>time the DATA register is written.<br>R9 is a read-only bit and T8 is a write-only bit, the value read is different from the<br>value written.<br>~~NOTE~~|
|29<br>TXDIR|TXD Pin Direction in Single-Wire Mode<br>When the LPUART is configured for single-wire half-duplex operation (LOOPS = RSRC = 1), this bit<br>determines the direction of data at the TXD pin. When clearing TXDIR, the transmitter finishes receiving<br>the current character (if any) before the receiver starts receiving data from the TXD pin.<br>0b - TXD pin is an input in single-wire mode.<br>1b - TXD pin is an output in single-wire mode.|
|28<br>TXINV|Transmit Data Inversion<br>Setting this bit reverses the polarity of the transmitted data output.<br>Setting TXINV inverts the TXD output for all cases: data bits, start and stop bits, break,<br>and idle.<br>~~NOTE~~<br>0b - Transmit data not inverted.<br>1b - Transmit data inverted.|
|27|Overrun Interrupt Enable|
|ORIE|This bit enables the overrun flag (OR) to generate hardware interrupt requests.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4244 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - OR interrupts disabled; use polling.<br>1b - Hardware interrupt is requested when OR is set.|
|26<br>NEIE|Noise Error Interrupt Enable<br>This bit enables the noise flag (NF) to generate hardware interrupt requests.<br>0b - NF interrupts disabled; use polling.<br>1b - Hardware interrupt is requested when NF is set.|
|25<br>FEIE|Framing Error Interrupt Enable<br>This bit enables the framing error flag (FE) to generate hardware interrupt requests.<br>0b - FE interrupts disabled; use polling.<br>1b - Hardware interrupt is requested when FE is set.|
|24<br>PEIE|Parity Error Interrupt Enable<br>This bit enables the parity error flag (PF) to generate hardware interrupt requests.<br>0b - PF interrupts disabled; use polling).<br>1b - Hardware interrupt is requested when PF is set.|
|23|Transmit Interrupt Enable|
|TIE|Enables STAT[TDRE] to generate interrupt requests.<br>0b - Hardware interrupts from TDRE disabled.<br>1b - Hardware interrupt is requested when TDRE flag is 1.|
|22|Transmission Complete Interrupt Enable for|
|TCIE|TCIE enables the transmission complete flag, TC, to generate interrupt requests.<br>0b - Hardware interrupts from TC disabled.<br>1b - Hardware interrupt is requested when TC flag is 1.|
|21|Receiver Interrupt Enable|
|RIE|Enables STAT[RDRF] to generate interrupt requests.<br>0b - Hardware interrupts from RDRF disabled.<br>1b - Hardware interrupt is requested when RDRF flag is 1.|
|20|Idle Line Interrupt Enable|
|ILIE<br>19|ILIE enables the idle line flag, STAT[IDLE], to generate interrupt requests.<br>0b - Hardware interrupts from IDLE disabled; use polling.<br>1b - Hardware interrupt is requested when IDLE flag is 1.<br>Transmitter Enable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4245 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|TE|Enables the LPUART transmitter. TE can also be used to queue an idle preamble by clearing and then<br>setting TE. When TE is cleared, this register bit reads as 1 until the transmitter has completed the current<br>character and the TXD pin is tristated.<br>A single idle character can also be queued by writing to the transmit FIFO with DATA[FRETSC] set and<br>DATA[R9T9] set.<br>0b - Transmitter disabled.<br>1b - Transmitter enabled.|
|18<br>RE|Receiver Enable<br>Enables the LPUART receiver. When RE is written to 0, this register bit reads as 1 until the receiver<br>finishes receiving the current character (if any).<br>0b - Receiver disabled.|
||1b - Receiver enabled.|
|17|Receiver Wakeup Control|
|RWU|This field can be set to place the LPUART receiver in a standby state. RWU automatically clears when<br>an RWU event occurs, that is, an IDLE event when CTRL[WAKE] is clear or an address match when<br>CTRL[WAKE] is set and STAT[RWUID] is clear.<br>RWU must be set only with CTRL[WAKE] = 0 (wakeup on idle) if the channel is currently not<br>idle. This can be determined by STAT[RAF]. If the flag is set to wake up an IDLE event and<br>the channel is already idle, it is possible that the LPUART will discard data. This is because<br>the data must be received or a LIN break detected after an IDLE is detected before IDLE is<br>allowed to be reasserted.<br>~~NOTE~~|
||0b - Normal receiver operation.<br>1b - LPUART receiver in standby waiting for wakeup condition.|
|16<br>SBK|Send Break<br>Writing a 1 and then a 0 to SBK queues a break character in the transmit data stream. Additional break<br>characters of 9 to 13 bits, or 12 to 15 bits if STAT[BRK13] is set, bit times of logic 0 are queued as long as<br>SBK is set. Depending on the timing of the set and clear of SBK relative to the character currently being<br>transmitted, a second break character may be queued before software clears SBK. If software takes too long<br>to clear SBK (for example, it is not cleared by the end of the 1st break character), then a 2nd break character<br>is sent. This is compared to queuing a break character through the transmit FIFO which guarantees only one<br>is sent.<br>A single break character can also be queued by writing to the transmit FIFO with DATA[FRETSC] set and<br>DATA[R9T9] clear.<br>0b - Normal transmitter operation.<br>1b - Queue break character(s) to be sent.|
|15|Match 1 Interrupt Enable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4246 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|MA1IE|0b - MA1F interrupt disabled<br>1b - MA1F interrupt enabled|
|14<br>MA2IE|Match 2 Interrupt Enable<br>0b - MA2F interrupt disabled<br>1b - MA2F interrupt enabled|
|13-12<br>—|Reserved|
|11<br>M7|7-Bit Mode Select<br>This bit should be changed only when the transmitter and receiver are both disabled.<br>0b - Receiver and transmitter use 8-bit to 10-bit data characters.<br>1b - Receiver and transmitter use 7-bit data characters.|
|10-8<br>IDLECFG|Idle Configuration<br>Configures the number of idle characters that must be received before the IDLE flag is set.<br>000b - 1 idle character<br>001b - 2 idle characters<br>010b - 4 idle characters<br>011b - 8 idle characters<br>100b - 16 idle characters<br>101b - 32 idle characters<br>110b - 64 idle characters<br>111b - 128 idle characters|
|7<br>LOOPS|Loop Mode Select<br>When LOOPS is set, the RXD pin is disconnected from the LPUART and the transmitter output is<br>internally connected to the receiver input. The transmitter and the receiver must be enabled to use the<br>loop function.<br>0b - Normal operation - RXD and TXD use separate pins.<br>1b - Loop mode or single-wire mode where transmitter outputs are internally connected to<br>receiver input (see RSRC bit).|
|6|Doze Enable|
|DOZEEN|0b - LPUART is enabled in Doze mode.|
|5|1b - LPUART is disabled in Doze mode , but remains active when not in Doze mode .<br>Receiver Source Select|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4247 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Field<br>RSRC|Function<br>This field has no mea<br>determines the sourc|ning or effect unless the LOOPS field is set. When LOOPS is set, the RSRC field<br>e for the receiver shift register input.<br>The descriptions of the field settings vary by module instance.<br>~~NOTE~~|
|---|---|---|
||Instance|Field value and description|
||LPUART_0|0b - Provided LOOPS is set, RSRC is cleared, selects internal loop back<br>mode and the LPUART does not use the RXD pin. The CTS_B pin is not<br>used and internally driven by the RTS_B output. The DSR_B pin is not<br>used and internally driven by the DTR_B output.<br>1b - Single-wire LPUART mode where the TXD pin is connected to the<br>transmitter output and receiver input.|
||LPUART_1|0b - Provided LOOPS is set, RSRC is cleared, selects internal loop back<br>mode and the LPUART does not use the RXD pin. The CTS_B pin is not<br>used and internally driven by the RTS_B output. The DSR_B pin is not<br>used and internally driven by the DTR_B output.<br>1b - Single-wire LPUART mode where the TXD pin is connected to the<br>transmitter output and receiver input.|
||LPUART_2|0b - Provided LOOPS is set, RSRC is cleared, selects internal loop back<br>mode and the LPUART does not use the RXD pin. The CTS_B pin is not<br>used and internally driven by the RTS_B output.<br>1b - Single-wire LPUART mode where the TXD pin is connected to the<br>transmitter output and receiver input.|
||LPUART_3|0b - Provided LOOPS is set, RSRC is cleared, selects internal loop back<br>mode and the LPUART does not use the RXD pin. The CTS_B pin is not<br>used and internally driven by the RTS_B output.<br>1b - Single-wire LPUART mode where the TXD pin is connected to the<br>transmitter output and receiver input.|
||LPUART_4|0b - Provided LOOPS is set, RSRC is cleared, selects internal loop back<br>mode and the LPUART does not use the RXD pin. The CTS_B pin is not<br>used and internally driven by the RTS_B output.<br>1b - Single-wire LPUART mode where the TXD pin is connected to the<br>transmitter output and receiver input.|
||LPUART_5|0b - Provided LOOPS is set, RSRC is cleared, selects internal loop back<br>mode and the LPUART does not use the RXD pin. The CTS_B pin is not<br>used and internally driven by the RTS_B output.<br>1b - Single-wire LPUART mode where the TXD pin is connected to the<br>transmitter output and receiver input.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4248 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Field<br>Function||
|---|---|
|Instance|Field value and description|
|LPUART_6|0b - Provided LOOPS is set, RSRC is cleared, selects internal loop back<br>mode and the LPUART does not use the RXD pin. The CTS_B pin is not<br>used and internally driven by the RTS_B output.<br>1b - Single-wire LPUART mode where the TXD pin is connected to the<br>transmitter output and receiver input.|
|LPUART_7|0b - Provided LOOPS is set, RSRC is cleared, selects internal loop back<br>mode and the LPUART does not use the RXD pin. The CTS_B pin is not<br>used and internally driven by the RTS_B output.<br>1b - Single-wire LPUART mode where the TXD pin is connected to the<br>transmitter output and receiver input.|
|LPUART_8|0b - Provided LOOPS is set, RSRC is cleared, selects internal loop back<br>mode and the LPUART does not use the RXD pin. The CTS_B pin is not<br>used and internally driven by the RTS_B output.<br>1b - Single-wire LPUART mode where the TXD pin is connected to the<br>transmitter output and receiver input.|
|LPUART_9|0b - Provided LOOPS is set, RSRC is cleared, selects internal loop back<br>mode and the LPUART does not use the RXD pin. The CTS_B pin is not<br>used and internally driven by the RTS_B output.<br>1b - Single-wire LPUART mode where the TXD pin is connected to the<br>transmitter output and receiver input.|
|LPUART_10|0b - Provided LOOPS is set, RSRC is cleared, selects internal loop back<br>mode and the LPUART does not use the RXD pin. The CTS_B pin is not<br>used and internally driven by the RTS_B output.<br>1b - Single-wire LPUART mode where the TXD pin is connected to the<br>transmitter output and receiver input.|
|LPUART_11|0b - Provided LOOPS is set, RSRC is cleared, selects internal loop back<br>mode and the LPUART does not use the RXD pin. The CTS_B pin is not<br>used and internally driven by the RTS_B output.<br>1b - Single-wire LPUART mode where the TXD pin is connected to the<br>transmitter output and receiver input.|
|LPUART_12|0b - Provided LOOPS is set, RSRC is cleared, selects internal loop back<br>mode and the LPUART does not use the RXD pin. The CTS_B pin is not<br>used and internally driven by the RTS_B output.<br>1b - Single-wire LPUART mode where the TXD pin is connected to the<br>transmitter output and receiver input.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4249 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||Instance<br>Field value and description|
||LPUART_13<br>0b - Provided LOOPS is set, RSRC is cleared, selects internal loop back<br>mode and the LPUART does not use the RXD pin. The CTS_B pin is not<br>used and internally driven by the RTS_B output.<br>1b - Single-wire LPUART mode where the TXD pin is connected to the<br>transmitter output and receiver input.|
||LPUART_14<br>0b - Provided LOOPS is set, RSRC is cleared, selects internal loop back<br>mode and the LPUART does not use the RXD pin. The CTS_B pin is not<br>used and internally driven by the RTS_B output.<br>1b - Single-wire LPUART mode where the TXD pin is connected to the<br>transmitter output and receiver input.|
||LPUART_15<br>0b - Provided LOOPS is set, RSRC is cleared, selects internal loop back<br>mode and the LPUART does not use the RXD pin. The CTS_B pin is not<br>used and internally driven by the RTS_B output.<br>1b - Single-wire LPUART mode where the TXD pin is connected to the<br>transmitter output and receiver input.|
|4<br>M|9-Bit or 8-Bit Mode Select<br>0b - Receiver and transmitter use 8-bit data characters.<br>1b - Receiver and transmitter use 9-bit data characters.|
|3<br>WAKE|Receiver Wakeup Method Select<br>Determines which condition wakes the LPUART when RWU=1 and MATCFG=00 (WAKE must be set<br>when MATCFG=11):<br>• Address mark in the bit preceding the stop bit (or bit preceding the parity bit when parity is enabled)<br>of the received data character.<br>• An idle condition on the receive pin input signal.<br>0b - Configures RWU for idle-line wakeup.<br>1b - Configures RWU with address-mark wakeup.|
|2<br>ILT|Idle Line Type Select<br>Determines when the receiver starts counting logic 1s as idle character bits. The count begins either<br>after a valid start bit or after the stop bit. If the count begins after the start bit, then a string of logic 1s<br>preceding the stop bit can cause false recognition of an idle character. Beginning the count after the stop<br>bit avoids false idle character recognition, but requires properly synchronized transmissions.<br>In case the LPUART is programmed with ILT = 1, a logic 0 is automatically shifted after a<br>received stop bit, therefore resetting the idle count.<br>~~NOTE~~|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4250 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Idle character bit count starts after start bit.<br>1b - Idle character bit count starts after stop bit.|
|1<br>PE|Parity Enable<br>Enables hardware parity generation and checking. When parity is enabled, the bit immediately before the<br>stop bit is treated as the parity bit.<br>0b - No hardware parity generation or checking.<br>1b - Parity enabled.|
|0<br>PT|Parity Type<br>Provided parity is enabled (PE = 1), this bit selects even or odd parity. Odd parity means the total<br>number of logic 1 bits in the data character, including the parity bit, is odd. Even parity means the total<br>number of 1s in the data character, including the parity bit, is even.<br>0b - Even parity.<br>1b - Odd parity.|



#### 76.6.1.9 LPUART Data Register (DATA) 

##### Offset 

|Register|Offset|
|---|---|
|DATA|1Ch|



##### Function 

~~<mark>NOTE</mark>~~ 

This register is two separate registers. Reads return the contents of the read-only receive FIFO and writes go to the write-only transmit FIFO. 

Reads and writes of this register are also involved in the automatic flag clearing mechanisms for some of the LPUART status flags. This register can be written using 8-bit, 16-bit or 32-bit writes. An 8-bit write to DATA[7:0] will push { R8T9, R9T8, DATA[7:0] } the transmit FIFO with TSC clear. A 16-bit or 32-bit write will push the data written into the FIFO and does not update the value in R8T9 or R9T8. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4251 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/076_Low_Power_Universal_Asynchronous_Receiver_Transmitter_-LPUART-/S32K3XXRM_数据表.pdf-4252-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>PARIT RXEM IDLIN LINBR<br>R NOISY  YE  FRET PT  E  K<br>R9T9  R8T8  R7T7  R6T6  R5T5  R4T4  R3T3  R2T2  R1T1  R0T0<br>SC<br>W<br>Reset 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16|Reserved|
|—||
|15|Noisy Data Received|
|NOISY|The current received dataword contained in DATA[R9:R0] is received with noise.<br>0b - The dataword is received without noise.<br>1b - The data is received with noise.|
|14|Parity Error|
|PARITYE|The current received dataword contained in DATA[R9:R0] is received with a parity error.<br>0b - The dataword is received without a parity error.<br>1b - The dataword is received with a parity error.|
|13<br>FRETSC|Frame Error / Transmit Special Character<br>For reads, indicates the current received dataword contained in DATA[R9:R0] was received with a frame<br>error. For writes, indicates a break or idle character is to be transmitted instead of the contents in<br>DATA[T9:T0]. T9 is used to indicate a break character when 0 and a idle character when 1, the contents<br>of DATA[T8:T0] should be zero.<br>0b - The dataword is received without a frame error on read, or transmit a normal character on<br>write.<br>1b - The dataword is received with a frame error, or transmit an idle or break character on<br>transmit.|
|12|Receive Buffer Empty|
|RXEMPT|Asserts when there is no data in the receive buffer. This field does not take into account data that is in<br>the receive shift register.<br>0b - Receive buffer contains valid data.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4252 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

Table continued from the previous page... 

|Field|Function<br>1b - Receive buffer is empty, data returned on read is not valid.|
|---|---|
|11|Idle Line|
|IDLINE|Indicates the receiver line was idle before receiving the character in DATA[9:0]. Unlike the IDLE flag, this<br>bit can set for the first character received when the receiver is first enabled.<br>0b - Receiver was not idle before receiving this character.<br>1b - Receiver was idle before receiving this character.|
|10<br>LINBRK|LIN Break<br>Indicates the receiver line detected a LIN break before receiving the character in DATA[9:0]. This flag<br>requires LBKDF to be set.<br>0b - Receiver did not detect LIN break before this character, or LIN break detect circuitry disabled.<br>1b - Receiver detected a LIN break before receiving this character.|
|9|R9T9|
|R9T9|Read receive FIFO bit 9 or write transmit FIFO bit 9.|
|8|R8T8|
|R8T8|Read receive FIFO bit 8 or write transmit FIFO bit 8.|
|7|R7T7|
|R7T7|Read receive FIFO bit 7 or write transmit FIFO bit 7.|
|6|R6T6|
|R6T6|Read receive FIFO bit 6 or write transmit FIFO bit 6.|
|5|R5T5|
|R5T5|Read receive FIFO bit 5 or write transmit FIFO bit 5.|
|4|R4T4|
|R4T4|Read receive FIFO bit 4 or write transmit FIFO bit 4.|
|3|R3T3|
|R3T3|Read receive FIFO bit 3 or write transmit FIFO bit 3.|
|2|R2T2|
|R2T2|Read receive FIFO bit 2 or write transmit FIFO bit 2.|
|1|R1T1|
|R1T1|Read receive FIFO bit 1 or write transmit FIFO bit 1.|
|0|R0T0|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4253 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|R0T0|Read receive FIFO bit 0 or write transmit FIFO bit 0.|



#### 76.6.1.10 LPUART Match Address Register (MATCH) 

Offset 

|Register|Offset|
|---|---|
|MATCH|20h|



Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/076_Low_Power_Universal_Asynchronous_Receiver_Transmitter_-LPUART-/S32K3XXRM_数据表.pdf-4254-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>MA2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>MA1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-26|Reserved|
|—||
|25-16|Match Address 2|
|MA2|The MA1 and MA2 fields are compared to input data addresses when the most significant bit is set and<br>the associated BAUD[MAEN] bit is set. If a match occurs, the following data is transferred to the DATA<br>register. If a match fails, the following data is discarded. Software should only write a MAx field when the<br>associated BAUD[MAEN] bit is clear.|
|15-10<br>—|Reserved|
|9-0|Match Address 1|
|MA1|The MA1 and MA2 fields are compared to input data addresses when the most significant bit is set and<br>the associated BAUD[MAEN] bit is set. If a match occurs, the following data is transferred to the DATA<br>register. If a match fails, the following data is discarded. Software should only write a MAx field when the<br>associated BAUD[MAEN] bit is clear.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4254 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

#### 76.6.1.11 LPUART Modem IrDA Register (MODIR) 

##### Offset 

|Register|Offset|
|---|---|
|MODIR|24h|



##### Function 

The MODIR register controls options for setting the modem configuration. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||||||0|||||||IREN|T|NP|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||0||||RTSW|ATER||0||TXCT|TXCT|RXRT|TXRT|TXRT|TXCT|
|W|||||||||||SSRC|SC|SE|SPOL|SE|SE|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-19|Reserved|
|—||
|18|Infrared enable|
|IREN|Enables/disables the infrared modulation/demodulation. This bit should be changed only when the<br>transmitter and receiver are both disabled.<br>0b - IR disabled.<br>1b - IR enabled.|
|17-16|Transmitter narrow pulse|
|TNP|Configures whether the LPUART transmits a 1/OSR, 2/OSR, 3/OSR or 4/OSR narrow pulse when IR is<br>enabled. This bit should be changed only when the transmitter and receiver are both disabled.<br>The IR pulse width should be configured to less than half of the oversampling ratio. Common pulse widths<br>are 3/16, 1/16, 1/32 or 1/4 of the bit length. These can be configured by selecting the appropriate oversample<br>ratio and pulse width.<br>00b - 1/OSR.<br>01b - 2/OSR.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4255 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Field|Function<br>10b - 3/OSR.<br>11b - 4/OSR.|||
|---|---|---|---|
|15-12<br>—|Reserved|||
|11-8<br>RTSWATER|Receive RTS Configuration<br>Configures the assertion and neg<br>number of empty words in the rec<br>to zero, RTS_B negates when the<br>of words in the receive FIFO upda<br>RTS_B negation and the externa<br>matching is enabled, then RTS_B<br>This field should be changed only<br>This field is not suppor<br>supported registers.|ation of the RX RTS_B output. Th<br>eive FIFO is greater or equal to RT<br>receive FIFO is full. For the purpos<br>tes when a start bit is detected. Th<br>l transmitter ceasing transmission.<br>could assert at the end of a chara<br>when the receiver is disabled.<br>ted in every instance. The following tab<br>~~NOTE~~|e RX RTS_B output negates when the<br>SWATER. If RTSWATER is configured<br>e of RX RTS_B generation, the number<br>is supports additional latency between<br>If both RX RTS_B and address/data<br>cter if there is not a match.<br>le includes only|
||Instance|Field supported in|Field not supported in|
||LPUART_0|MODIR|—|
||LPUART_1|MODIR|—|
||LPUART_2|MODIR[9–8]|MODIR[11–10]|
||LPUART_3|MODIR[9–8]|MODIR[11–10]|
||LPUART_4|MODIR[9–8]|MODIR[11–10]|
||LPUART_5|MODIR[9–8]|MODIR[11–10]|
||LPUART_6|MODIR[9–8]|MODIR[11–10]|
||LPUART_7|MODIR[9–8]|MODIR[11–10]|
||LPUART_8|MODIR[9–8]|MODIR[11–10]|
||LPUART_9|MODIR[9–8]|MODIR[11–10]|
||LPUART_10|MODIR[9–8]|MODIR[11–10]|
||LPUART_11|MODIR[9–8]|MODIR[11–10]|
||LPUART_12|MODIR[9–8]|MODIR[11–10]|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4256 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||Instance<br>Field supported in<br>Field not supported in|
||LPUART_13<br>MODIR[9–8]<br>MODIR[11–10]|
||LPUART_14<br>MODIR[9–8]<br>MODIR[11–10]|
||LPUART_15<br>MODIR[9–8]<br>MODIR[11–10]|
|7-6<br>—|Reserved|
|5<br>TXCTSSRC|Transmit CTS Source<br>Configures the source of the CTS input.<br>0b - CTS input is the CTS_B pin.<br>1b - CTS input is an internal connection to the receiver address match result.|
|4<br>TXCTSC|Transmit CTS Configuration<br>Configures if the CTS state is checked at the start of each character or only when the transmitter is idle.<br>0b - CTS input is sampled at the start of each character.<br>1b - CTS input is sampled when the transmitter is idle.|
|3<br>RXRTSE|Receiver request-to-send enable<br>Allows the RTS output to control the CTS input of the transmitting device to prevent receiver overrun.<br>This bit should be changed only when the receiver is disabled.<br>Do not set both RXRTSE and TXRTSE.<br>~~NOTE~~<br>0b - The receiver has no effect on RTS.<br>1b - RTS is deasserted if the receiver data register is full or a start bit has been detected that<br>would cause the receiver data register to become full. RTS is asserted if the receiver data register<br>is not full and has not detected a start bit that would cause the receiver data register to become<br>full.|
|2<br>TXRTSPOL|Transmitter request-to-send polarity<br>Controls the polarity of the transmitter RTS. TXRTSPOL does not affect the polarity of the receiver RTS.<br>RTS remains negated in the active low state unless TXRTSE is set. This bit should be changed only<br>when the transmitter is disabled.<br>0b - Transmitter RTS is active low.<br>1b - Transmitter RTS is active high.|
|1|Transmitter request-to-send enable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4257 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|TXRTSE|Controls RTS before and after a transmission. This bit should be changed only when the transmitter is<br>disabled.<br>0b - The transmitter has no effect on RTS.<br>1b - When a character is placed into an empty transmit shift register, RTS asserts one bit time<br>before the start bit is transmitted. RTS deasserts one bit time after all characters in the transmitter<br>FIFO and shift register are completely sent, including the last stop bit.|
|0|Transmitter clear-to-send enable|
|TXCTSE|TXCTSE controls the operation of the transmitter. TXCTSE can be set independently from the state of<br>TXRTSE and RXRTSE.<br>0b - CTS has no effect on the transmitter.|
||1b - Enables clear-to-send operation. The transmitter checks the state of CTS each time it is<br>ready to send a character. If CTS is asserted, the character is sent. If CTS is deasserted, the<br>signal TXD remains in the mark state and transmission is delayed until CTS is asserted. Changes<br>in CTS as a character is being sent do not affect its transmission.|



#### 76.6.1.12 LPUART FIFO Register (FIFO) 

##### Offset 

|Register|Offset|
|---|---|
|FIFO|28h|



##### Function 

This register provides the ability for the programmer to turn on and off FIFO functionality. It also provides the size of the FIFO that has been implemented. This register may be read at any time. This register must be written only when CTRL[RE] and CTRL[TE] are cleared/not set and when the FIFO is empty. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/076_Low_Power_Universal_Asynchronous_Receiver_Transmitter_-LPUART-/S32K3XXRM_数据表.pdf-4258-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>TXEM RXEM<br>R 0 0 TXOF  RXUF<br>PT  PT<br>W W1C W1C<br>Reset See Register reset values.<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 0 TXFIFOSIZE  RXFIFOSIZE<br>TXOF RXUF<br>RXIDEN  TXFE  RXFE<br>TXFLU RXFL E  E<br>W<br>SH  USH<br>Reset See Register reset values.Register reset values..<br><!-- End of picture text -->

See Register reset values.Register reset values.. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4258 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Register reset values 

|Register|Reset value|
|---|---|
|FIFO|LPUART_0,LPUART_1: 00C0_0033h|
||LPUART_2–LPUART_15: 00C0_0011h|



##### Fields 

|Field|Function|
|---|---|
|31-24|Reserved|
|—||
|23<br>TXEMPT|Transmit FIFO/Buffer Empty<br>Asserts when there is no data in the Transmit FIFO/Buffer. This field does not take into account data that<br>is in the transmit shift register.<br>0b - Transmit buffer is not empty.<br>1b - Transmit buffer is empty.|
|22<br>RXEMPT|Receive FIFO/Buffer Empty<br>Asserts when there is no data in the Receive FIFO/Buffer. This field does not take into account data that<br>is in the receive shift register.<br>0b - Receive buffer is not empty.<br>1b - Receive buffer is empty.|
|21-18<br>—<br>17<br>TXOF|Reserved<br>Transmitter FIFO Overflow Flag<br>Indicates that more data has been written to the transmit FIFO than it can hold. This field asserts<br>regardless of the value of TXOFE. However, an interrupt is issued to the host only if TXOFE is set. Write<br>1 to clear this flag.<br>0b - No transmit FIFO overflow has occurred since the last time the flag was cleared.<br>1b - At least one transmit FIFO overflow has occurred since the last time the flag was cleared.|
|16<br>RXUF|Receiver FIFO Underflow Flag<br>Indicates that more data has been read from the receive FIFO than was present. This field asserts<br>regardless of the value of RXUFE. However, an interrupt is issued to the host only if RXUFE is set. Write<br>a logic 1 to clear RXUF.<br>0b - No receive FIFO underflow has occurred since the last time the flag was cleared.<br>1b - At least one receive FIFO underflow has occurred since the last time the flag was cleared.|
|15<br>TXFLUSH|Transmit FIFO Flush|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4259 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||Writing to this field causes all data that is stored in the transmit FIFO to be flushed. This does not affect<br>data that is in the transmit shift register.<br>0b - No flush operation occurs.<br>1b - All data in the transmit FIFO is cleared out.|
|14<br>RXFLUSH|Receive FIFO Flush<br>Writing to this field causes all data that is stored in the receive FIFO to be flushed. This does not affect<br>data that is in the receive shift register.<br>0b - No flush operation occurs.<br>1b - All data in the receive FIFO/buffer is cleared out.|
|13<br>—<br>12-10<br>RXIDEN|Reserved<br>Receiver Idle Empty Enable<br>When set, enables the assertion of RDRF when the receiver is idle for a number of idle characters and<br>the FIFO is not empty. This feature is not supported when the receiver extended idle time is enabled.<br>000b - Disable RDRF assertion due to partially filled FIFO when receiver is idle.<br>001b - Enable RDRF assertion due to partially filled FIFO when receiver is idle for 1 character.<br>010b - Enable RDRF assertion due to partially filled FIFO when receiver is idle for 2 characters.<br>011b - Enable RDRF assertion due to partially filled FIFO when receiver is idle for 4 characters.<br>100b - Enable RDRF assertion due to partially filled FIFO when receiver is idle for 8 characters.<br>101b - Enable RDRF assertion due to partially filled FIFO when receiver is idle for 16 characters.<br>110b - Enable RDRF assertion due to partially filled FIFO when receiver is idle for 32 characters.<br>111b - Enable RDRF assertion due to partially filled FIFO when receiver is idle for 64 characters.|
|9<br>TXOFE|Transmit FIFO Overflow Interrupt Enable<br>When this field is set, the TXOF flag generates an interrupt to the host.<br>0b - TXOF flag does not generate an interrupt to the host.<br>1b - TXOF flag generates an interrupt to the host.|
|8<br>RXUFE|Receive FIFO Underflow Interrupt Enable<br>When this field is set, the RXUF flag generates an interrupt to the host.<br>0b - RXUF flag does not generate an interrupt to the host.<br>1b - RXUF flag generates an interrupt to the host.|
|7|Transmit FIFO Enable|
|TXFE|When this field is set, the built-in FIFO structure for the transmit buffer is enabled. The size of the FIFO<br>structure is indicated by TXFIFOSIZE. If this field is not set, the transmit buffer operates as a FIFO of<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4260 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Field|Function<br>depth one dataword regardless of the value in TXFIFOSIZE. Both CTRL[TE] and CTRL[RE] must be<br>cleared prior to changing this field.<br>0b - Transmit FIFO is not enabled. Buffer depth is 1.<br>1b - Transmit FIFO is enabled. Buffer depth is indicated by TXFIFOSIZE.|
|---|---|
|6-4<br>TXFIFOSIZE|Transmit FIFO Buffer Depth<br>The maximum number of transmit datawords that can be stored in the transmit buffer. This field is<br>read-only.<br>000b - Transmit FIFO/Buffer depth = 1 dataword.<br>001b - Transmit FIFO/Buffer depth = 4 datawords.<br>010b - Transmit FIFO/Buffer depth = 8 datawords.<br>011b - Transmit FIFO/Buffer depth = 16 datawords.<br>100b - Transmit FIFO/Buffer depth = 32 datawords.<br>101b - Transmit FIFO/Buffer depth = 64 datawords.<br>110b - Transmit FIFO/Buffer depth = 128 datawords.<br>111b - Transmit FIFO/Buffer depth = 256 datawords|
|3<br>RXFE|Receive FIFO Enable<br>When this field is set, the built-in FIFO structure for the receive buffer is enabled. The size of the FIFO<br>structure is indicated by the RXFIFOSIZE field. If this field is not set, the receive buffer operates as a<br>FIFO of depth one dataword regardless of the value in RXFIFOSIZE. Both CTRL[TE] and CTRL[RE]<br>must be cleared prior to changing this field.<br>0b - Receive FIFO is not enabled. Buffer depth is 1.<br>1b - Receive FIFO is enabled. Buffer depth is indicted by RXFIFOSIZE.|
|2-0<br>RXFIFOSIZE|Receive FIFO Buffer Depth<br>The maximum number of receive datawords that can be stored in the receive buffer before an overrun<br>occurs. This field is read-only.<br>000b - Receive FIFO/Buffer depth = 1 dataword.<br>001b - Receive FIFO/Buffer depth = 4 datawords.<br>010b - Receive FIFO/Buffer depth = 8 datawords.<br>011b - Receive FIFO/Buffer depth = 16 datawords.<br>100b - Receive FIFO/Buffer depth = 32 datawords.<br>101b - Receive FIFO/Buffer depth = 64 datawords.<br>110b - Receive FIFO/Buffer depth = 128 datawords.<br>111b - Receive FIFO/Buffer depth = 256 datawords.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4261 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

#### 76.6.1.13 LPUART Watermark Register (WATER) 

##### Offset 

|Register|Offset|
|---|---|
|WATER|2Ch|



##### Function 

This register provides the ability to set a programmable threshold for notification of needing additional transmit data. This register may be read at any time but must be written only when CTRL[TE] is not set. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||0||||RXCOUNT||||0||||RXW|ATER||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||0||||TXCOUNT||||0||||TXW|ATER||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|||
|---|---|---|---|
|31-29|Reserved|||
|—||||
|28-24|Receive Counter|||
|RXCOUNT|The value in this register indicate<br>dataword is being received, that i<br>may be used in conjunction with<br>FIFO/buffer.|s the number of datawords that a<br>s, in the receive shift register, it is<br>FIFO[RXFIFOSIZE] to calculate h|re in the receive FIFO/buffer. If a<br>not included in the count. This value<br>ow much room is left in the receive|
||This field is not suppor<br>supported registers.|ted in every instance. The following ta<br>~~NOTE~~|ble includes only|
||Instance|Field supported in|Field not supported in|
||LPUART_0|WATER|—|
||LPUART_1|WATER|—|
||LPUART_2|WATER[26–24]|WATER[28–27]|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4262 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

|Field|Function|||
|---|---|---|---|
||Instance|Field supported in|Field not supported in|
||LPUART_3|WATER[26–24]|WATER[28–27]|
||LPUART_4|WATER[26–24]|WATER[28–27]|
||LPUART_5|WATER[26–24]|WATER[28–27]|
||LPUART_6|WATER[26–24]|WATER[28–27]|
||LPUART_7|WATER[26–24]|WATER[28–27]|
||LPUART_8|WATER[26–24]|WATER[28–27]|
||LPUART_9|WATER[26–24]|WATER[28–27]|
||LPUART_10|WATER[26–24]|WATER[28–27]|
||LPUART_11|WATER[26–24]|WATER[28–27]|
||LPUART_12|WATER[26–24]|WATER[28–27]|
||LPUART_13|WATER[26–24]|WATER[28–27]|
||LPUART_14|WATER[26–24]|WATER[28–27]|
||LPUART_15|WATER[26–24]|WATER[28–27]|
|23-20<br>—|Reserved|||
|19-16|Receive Watermark|||
|RXWATER|When the number of datawords i<br>interrupt or a DMA request is gen<br>less than the receive FIFO/buffer<br>This field is not suppor<br>supported registers.|n the receive FIFO/buffer is greate<br>erated. For proper operation, the<br>size as indicated by FIFO[RXFIF<br>ted in every instance. The following ta<br>~~NOTE~~|r than the value in this register field, an<br>value in RXWATER must be set to be<br>OSIZE] and FIFO[RXFE].<br>ble includes only|
||Instance|Field supported in|Field not supported in|
||LPUART_0|WATER|—|
||LPUART_1|WATER|—|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4263 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Field|Function|||
|---|---|---|---|
||Instance|Field supported in|Field not supported in|
||LPUART_2|WATER[17–16]|WATER[19–18]|
||LPUART_3|WATER[17–16]|WATER[19–18]|
||LPUART_4|WATER[17–16]|WATER[19–18]|
||LPUART_5|WATER[17–16]|WATER[19–18]|
||LPUART_6|WATER[17–16]|WATER[19–18]|
||LPUART_7|WATER[17–16]|WATER[19–18]|
||LPUART_8|WATER[17–16]|WATER[19–18]|
||LPUART_9|WATER[17–16]|WATER[19–18]|
||LPUART_10|WATER[17–16]|WATER[19–18]|
||LPUART_11|WATER[17–16]|WATER[19–18]|
||LPUART_12|WATER[17–16]|WATER[19–18]|
||LPUART_13|WATER[17–16]|WATER[19–18]|
||LPUART_14|WATER[17–16]|WATER[19–18]|
||LPUART_15|WATER[17–16]|WATER[19–18]|
|15-13<br>—|Reserved|||
|12-8<br>TXCOUNT|Transmit Counter<br>The value in this register indicate<br>dataword is being transmitted, th<br>value may be used in conjunction<br>transmit FIFO/buffer.<br>This field is not suppor<br>supported registers.|s the number of datawords that a<br>at is, in the transmit shift register,<br>with FIFO[TXFIFOSIZE] to calcu<br>ted in every instance. The following ta<br>~~NOTE~~|re in the transmit FIFO/buffer. If a<br>it is not included in the count. This<br>late how much room is left in the<br>ble includes only|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4264 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Field|Function||
|---|---|---|
||Instance<br>Field supported in|Field not supported in|
||LPUART_0<br>WATER|—|
||LPUART_1<br>WATER|—|
||LPUART_2<br>WATER[10–8]|WATER[12–11]|
||LPUART_3<br>WATER[10–8]|WATER[12–11]|
||LPUART_4<br>WATER[10–8]|WATER[12–11]|
||LPUART_5<br>WATER[10–8]|WATER[12–11]|
||LPUART_6<br>WATER[10–8]|WATER[12–11]|
||LPUART_7<br>WATER[10–8]|WATER[12–11]|
||LPUART_8<br>WATER[10–8]|WATER[12–11]|
||LPUART_9<br>WATER[10–8]|WATER[12–11]|
||LPUART_10<br>WATER[10–8]|WATER[12–11]|
||LPUART_11<br>WATER[10–8]|WATER[12–11]|
||LPUART_12<br>WATER[10–8]|WATER[12–11]|
||LPUART_13<br>WATER[10–8]|WATER[12–11]|
||LPUART_14<br>WATER[10–8]|WATER[12–11]|
||LPUART_15<br>WATER[10–8]|WATER[12–11]|
|7-4<br>—|Reserved||
|3-0|Transmit Watermark||
|TXWATER|When the number of datawords in the transmit FIFO/buffer is equal<br>field, an interrupt or a DMA request is generated. For proper operati<br>to be less than the size of the transmit buffer/FIFO size as indicated b<br>This field is not supported in every instance. The following ta<br>supported registers.<br>~~NOTE~~|to or less than the value in this register<br>on, the value in TXWATER must be set<br>y FIFO[TXFIFOSIZE] and FIFO[TXFE].<br>ble includes only|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4265 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Field<br>Function|||
|---|---|---|
|Instance|Field supported in|Field not supported in|
|LPUART_0|WATER|—|
|LPUART_1|WATER|—|
|LPUART_2|WATER[1–0]|WATER[3–2]|
|LPUART_3|WATER[1–0]|WATER[3–2]|
|LPUART_4|WATER[1–0]|WATER[3–2]|
|LPUART_5|WATER[1–0]|WATER[3–2]|
|LPUART_6|WATER[1–0]|WATER[3–2]|
|LPUART_7|WATER[1–0]|WATER[3–2]|
|LPUART_8|WATER[1–0]|WATER[3–2]|
|LPUART_9|WATER[1–0]|WATER[3–2]|
|LPUART_10|WATER[1–0]|WATER[3–2]|
|LPUART_11|WATER[1–0]|WATER[3–2]|
|LPUART_12|WATER[1–0]|WATER[3–2]|
|LPUART_13|WATER[1–0]|WATER[3–2]|
|LPUART_14|WATER[1–0]|WATER[3–2]|
|LPUART_15|WATER[1–0]|WATER[3–2]|



#### 76.6.1.14 Data read-only Register (DATARO) 

##### Offset 

|Register|Offset|
|---|---|
|DATARO|30h|



##### Function 

Returns the first entry in the receive FIFO, but does not pull the data from the FIFO. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4266 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/076_Low_Power_Universal_Asynchronous_Receiver_Transmitter_-LPUART-/S32K3XXRM_数据表.pdf-4267-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DATA<br>W<br>Reset 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16|Reserved|
|—||
|15-0|Receive Data|
|DATA|Returns first entry from the receive FIFO, the bit definition is the same as the DATA register.|



#### 76.6.1.15 MODEM Control Register (MCR) 

##### Offset 

|Register|Offset|
|---|---|
|MCR|40h|



##### Function 

Controls the operation of the MODEM pins. 

~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

||Instance||Register supported|Register not supported|
|---|---|---|---|---|
|LPUART_0||MCR||—|
|LPUART_1||MCR||—|
|LPUART_2||—||MCR|
|LPUART_3||—||MCR|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4267 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Instance||Register supported|Register not supported|
|---|---|---|---|
|LPUART_4|—||MCR|
|LPUART_5|—||MCR|
|LPUART_6|—||MCR|
|LPUART_7|—||MCR|
|LPUART_8|—||MCR|
|LPUART_9|—||MCR|
|LPUART_10|—||MCR|
|LPUART_11|—||MCR|
|LPUART_12|—||MCR|
|LPUART_13|—||MCR|
|LPUART_14|—||MCR|
|LPUART_15|—||MCR|



##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/076_Low_Power_Universal_Asynchronous_Receiver_Transmitter_-LPUART-/S32K3XXRM_数据表.pdf-4268-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>RTS  DTR  DCD  RIN  DSR  CTS<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-10<br>—|Reserved|
|9|Request To Send|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4268 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|RTS|Configures the default state of RTS_B pin when function is disabled.<br>0b - Default state of RTS_B is logic one<br>1b - Default state of RTS_B is logic zero|
|8<br>DTR|Data Terminal Ready<br>Configures the default state of DTR_B pin.<br>0b - Default state of DTR_B is logic one<br>1b - Default state of DTR_B is logic zero|
|7-4<br>—|Reserved|
|3|Data Carrier Detect|
|DCD|Configures interrupt for change of state of the DCD_B.<br>0b - The DCD_B interrupt disabled<br>1b - The DCD_B interrupt enabled|
|2<br>RIN|Ring Indicator<br>Configures interrupt for change of state on the RIN_B pin.<br>0b - The RIN_B interrupt disabled<br>1b - The RIN_B interrupt enabled|
|1|Data Set Ready|
|DSR|Configures interrupt for change of state on DSR_B pin.<br>0b - The DSR_B interrupt disabled<br>1b - The DSR_B interrupt enabled|
|0|Clear To Send|
|CTS|Configures interrupt for change of state on CTS_B pin.<br>0b - The CTS_B interrupt disabled<br>1b - The CTS_B interrupt enabled|



#### 76.6.1.16 MODEM Status Register (MSR) 

##### Offset 

|Register|Offset|
|---|---|
|MSR|44h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4269 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Function 

##### Returns the status of the MODEM pins. 

###### ~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

|Instance|Register supported|Register not supported|
|---|---|---|
|LPUART_0|MSR|—|
|LPUART_1|MSR|—|
|LPUART_2|—|MSR|
|LPUART_3|—|MSR|
|LPUART_4|—|MSR|
|LPUART_5|—|MSR|
|LPUART_6|—|MSR|
|LPUART_7|—|MSR|
|LPUART_8|—|MSR|
|LPUART_9|—|MSR|
|LPUART_10|—|MSR|
|LPUART_11|—|MSR|
|LPUART_12|—|MSR|
|LPUART_13|—|MSR|
|LPUART_14|—|MSR|
|LPUART_15|—|MSR|



##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/076_Low_Power_Universal_Asynchronous_Receiver_Transmitter_-LPUART-/S32K3XXRM_数据表.pdf-4270-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 DCD  RIN  DSR  CTS  DDCD  DRI  DDSR  DCTS<br>W W1C W1C W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4270 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Fields 

|Field|Function|
|---|---|
|31-8<br>—|Reserved|
|7<br>DCD|Data Carrier Detect<br>Returns the state of the DCD_B pin.<br>0b - The DCD_B pin is logic one<br>1b - The DCD_B pin is logic zero|
|6|Ring Indicator|
|RIN|Returns the state of the RIN_B pin.<br>0b - The RIN_B pin is logic one<br>1b - The RIN_B pin is logic zero|
|5<br>DSR|Data Set Ready<br>Returns the state of the DSR_B pin.<br>0b - The DSR_B pin is logic one<br>1b - The DSR_B pin is logic zero|
|4<br>CTS|Clear To Send<br>Returns the state of the CTS_B.<br>0b - The CTS_B pin is logic one<br>1b - The CTS_B pin is logic zero|
|3<br>DDCD|Delta Data Carrier Detect<br>This flag indicates that the DCD_B pin changed state since the last time the flag was cleared.<br>0b - The DCD_B pin has not changed state<br>1b - The DCD_B pin has changed state|
|2<br>DRI|Delta Ring Indicator<br>This flag indicates that the RIN_B pin changed state since the last time the flag was cleared.<br>0b - The RIN_B pin has not changed state<br>1b - The RIN_B pin has changed state|
|1<br>DDSR|Delta Data Set Ready<br>This flag indicates that the DSR_B pin changed state since the last time the flag was cleared.<br>0b - The DSR_B pin has not changed state<br>1b - The DSR_B pin has changed state|
|0|Delta Clear To Send|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4271 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|DCTS|This flag indicates that the CTS_B pin changed state since the last time the flag was cleared.|
||0b - The CTS_B pin has not changed state|
||1b - The CTS_B pin has changed state|



#### 76.6.1.17 Receiver Extended Idle Register (REIR) 

##### Offset 

|Register|Offset|
|---|---|
|REIR|48h|



##### Function 

This register configures the receiver extended idle functionality. Software should not change this value when the receiver is enabled. 

~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

|Instance||Register supported|Register not supported|
|---|---|---|---|
|LPUART_0|REIR||—|
|LPUART_1|REIR||—|
|LPUART_2|—||REIR|
|LPUART_3|—||REIR|
|LPUART_4|—||REIR|
|LPUART_5|—||REIR|
|LPUART_6|—||REIR|
|LPUART_7|—||REIR|
|LPUART_8|—||REIR|
|LPUART_9|—||REIR|
|LPUART_10|—||REIR|
|LPUART_11|—||REIR|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4272 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Instance||Register supported|Register not supported|
|---|---|---|---|
|LPUART_12|—||REIR|
|LPUART_13|—||REIR|
|LPUART_14|—||REIR|
|LPUART_15|—||REIR|



##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/076_Low_Power_Universal_Asynchronous_Receiver_Transmitter_-LPUART-/S32K3XXRM_数据表.pdf-4273-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>IDTIME<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-14|Reserved|
|—||
|13-0|Idle Time|
|IDTIME|The extended idle feature is disabled when set to zero. Otherwise configures the idle length in number<br>of bits (baud rate) since the end of the last stop bit. This affects the behavior of the idle wakeup, the<br>STAT[IDLE] flag, DATA[IDLINE] flag and STAT[RAF] flag. The minimum supported extended idle time is<br>equal to one idle character.|



#### 76.6.1.18 Transmitter Extended Idle Register (TEIR) 

##### Offset 

|Register|Offset|
|---|---|
|TEIR|4Ch|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4273 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Function 

This register configures the transmitter extended idle functionality. Software should not change this value when the transmitter is enabled. 

###### ~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

|Instance|Register supported|Register not supported|
|---|---|---|
|LPUART_0|TEIR|—|
|LPUART_1|TEIR|—|
|LPUART_2|—|TEIR|
|LPUART_3|—|TEIR|
|LPUART_4|—|TEIR|
|LPUART_5|—|TEIR|
|LPUART_6|—|TEIR|
|LPUART_7|—|TEIR|
|LPUART_8|—|TEIR|
|LPUART_9|—|TEIR|
|LPUART_10|—|TEIR|
|LPUART_11|—|TEIR|
|LPUART_12|—|TEIR|
|LPUART_13|—|TEIR|
|LPUART_14|—|TEIR|
|LPUART_15|—|TEIR|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4274 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/076_Low_Power_Universal_Asynchronous_Receiver_Transmitter_-LPUART-/S32K3XXRM_数据表.pdf-4275-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>IDTIME<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-14|Reserved|
|—||
|13-0|Idle Time|
|IDTIME|The extended idle feature is disabled when set to zero. Otherwise configures the transmitter idle<br>time in number of bits (baud rate) whenever an idle character is queued through the transmit FIFO.<br>When transmitter extended idle is enabled, an idle character is not automatically queued whenever the<br>transmitter is enabled. The minimum supported extended idle time is equal to one idle character.|



#### 76.6.1.19 Half Duplex Control Register (HDCR) 

##### Offset 

|Register|Offset|
|---|---|
|HDCR|50h|



##### Function 

This register provides control for half duplex related operations. This register can be used in place of the LOOPS, RSRC and TXDIR functions, although LOOPS can be used to loop-back the transmitter outputs to the receiver. 

~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

||Instance|Register supported|Register not supported|
|---|---|---|---|
|LPUART_0||HDCR|—|
|LPUART_1||HDCR|—|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4275 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Instance||Register supported|Register not supported|
|---|---|---|---|
|LPUART_2|—||HDCR|
|LPUART_3|—||HDCR|
|LPUART_4|—||HDCR|
|LPUART_5|—||HDCR|
|LPUART_6|—||HDCR|
|LPUART_7|—||HDCR|
|LPUART_8|—||HDCR|
|LPUART_9|—||HDCR|
|LPUART_10|—||HDCR|
|LPUART_11|—||HDCR|
|LPUART_12|—||HDCR|
|LPUART_13|—||HDCR|
|LPUART_14|—||HDCR|
|LPUART_15|—||HDCR|



##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/076_Low_Power_Universal_Asynchronous_Receiver_Transmitter_-LPUART-/S32K3XXRM_数据表.pdf-4276-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 RXMS RXWR RXSE TXSTA<br>RTSEXT<br>W K  MSK  L  LL<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4276 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Fields 

|Field|Function|
|---|---|
|31-16<br>—|Reserved|
|15-8<br>RTSEXT|RTS Extended<br>The transmit RTS_B will remain asserted for (RTSEXT+1) bit times after the end of the last stop bit.<br>This applies even when the transmitter RTS_B output is disabled and only used internally to mask the<br>receiver.|
|7-4<br>—<br>3<br>RXMSK|Reserved<br>Receive Mask<br>When enabled, the receive data pin is masked by the transmitter RTS_B.<br>0b - Receive data pin is not masked by the transmitter RTS_B<br>1b - Receive data pin is masked by the transmitter RTS_B|
|2<br>RXWRMSK|Receive FIFO Write Mask<br>When enabled, writes to the receive FIFO are masked by the transmitter RTS_B, but idle flag is not<br>affected.<br>0b - Receive FIFO writes are not masked<br>1b - Receive FIFO writes are masked by the transmitter RTS_B|
|1<br>RXSEL|Receive Select<br>When enabled, the receive data is sourced from TXD.<br>0b - Receive data pin is RXD<br>1b - Receive data pin is TXD|
|0<br>TXSTALL|Transmit Stall<br>When enabled, the transmitter does not become busy or assert transmitter RTS_B while the receiver is<br>active (STAT[RAF] = 1).<br>0b - No effect<br>1b - Transmitter will not become busy when receiver is active|



#### 76.6.1.20 Timeout Control Register (TOCR) 

##### Offset 

|Register|Offset|
|---|---|
|TOCR|58h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4277 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Function 

This register configures the behavior of the timeout logic. Timeout 0 and 1 are used to monitor the receiver and timeout 2 and 3 are used to monitor the transmitter. 

###### ~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

|Instance|Register supported|Register not supported|
|---|---|---|
|LPUART_0|TOCR|—|
|LPUART_1|TOCR|—|
|LPUART_2|—|TOCR|
|LPUART_3|—|TOCR|
|LPUART_4|—|TOCR|
|LPUART_5|—|TOCR|
|LPUART_6|—|TOCR|
|LPUART_7|—|TOCR|
|LPUART_8|—|TOCR|
|LPUART_9|—|TOCR|
|LPUART_10|—|TOCR|
|LPUART_11|—|TOCR|
|LPUART_12|—|TOCR|
|LPUART_13|—|TOCR|
|LPUART_14|—|TOCR|
|LPUART_15|—|TOCR|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4278 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18||17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0||||||||||
|W||||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0||0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2||1|0|
|R<br>W||0||||TOI|E|||0||||TO|EN|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0||0|0|



##### Fields 

|Field|Function|
|---|---|
|31-12|Reserved|
|—||
|11-8|Timeout Interrupt Enable|
|TOIE|When asserted, enables the corresponding timeout flag to generate an interrupt.|
|7-4|Reserved|
|—<br>3-0|Timeout Enable|
|TOEN|When asserted, enables the corresponding timeout counter.|



#### 76.6.1.21 Timeout Status Register (TOSR) 

##### Offset 

|Register|Offset|
|---|---|
|TOSR|5Ch|



##### Function 

This register returns the status of the timeout logic. Timeout 0 and 1 are used to monitor the receiver and timeout 2 and 3 are used to monitor the transmitter. 

~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4279 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

|Instance|Register supported|Register not supported|
|---|---|---|
|LPUART_0|TOSR|—|
|LPUART_1|TOSR|—|
|LPUART_2|—|TOSR|
|LPUART_3|—|TOSR|
|LPUART_4|—|TOSR|
|LPUART_5|—|TOSR|
|LPUART_6|—|TOSR|
|LPUART_7|—|TOSR|
|LPUART_8|—|TOSR|
|LPUART_9|—|TOSR|
|LPUART_10|—|TOSR|
|LPUART_11|—|TOSR|
|LPUART_12|—|TOSR|
|LPUART_13|—|TOSR|
|LPUART_14|—|TOSR|
|LPUART_15|—|TOSR|



##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18||17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0||||||||||
|W||||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0||0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2||1|0|
|R||0||||TO|F|||0||||TO|Z|||
|W||||||W1|C|||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|1|1||1|1|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4280 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Fields 

|Field|Function|
|---|---|
|31-12|Reserved|
|—||
|11-8|Timeout Flag|
|TOF|When asserted, indicates the corresponding timeout occurred. The timeout counter is disabled while the<br>timeout flag is set.|
|7-4|Reserved|
|—||
|3-0|Timeout Zero|
|TOZ|When asserted, indicates that the corresponding timeout counter equals zero.|



#### 76.6.1.22 Timeout N Register (TIMEOUT0 - TIMEOUT3) 

##### Offset 

|Register|Offset|
|---|---|
|TIMEOUT0|60h|
|TIMEOUT1|64h|
|TIMEOUT2|68h|
|TIMEOUT3|6Ch|



##### Function 

Configures the corresponding timeout counter and status flag. Timeout 0 and 1 are used to monitor the receiver and timeout 2 and 3 are used to monitor the transmitter. Timeout register should only be written when the corresponding timeout is disabled or while the corresponding timeout flag is set. 

~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

|Instance|Register supported|Register not supported|
|---|---|---|
|LPUART_0|TIMEOUT0–TIMEOUT3|—|
|LPUART_1|TIMEOUT0–TIMEOUT3|—|
|LPUART_2|—|TIMEOUT0–TIMEOUT3|
|LPUART_3|—|TIMEOUT0–TIMEOUT3|
|LPUART_4|—|TIMEOUT0–TIMEOUT3|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4281 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

Table continued from the previous page... 

|Instance||Register supported|Register not supported|
|---|---|---|---|
|LPUART_5|—||TIMEOUT0–TIMEOUT3|
|LPUART_6|—||TIMEOUT0–TIMEOUT3|
|LPUART_7|—||TIMEOUT0–TIMEOUT3|
|LPUART_8|—||TIMEOUT0–TIMEOUT3|
|LPUART_9|—||TIMEOUT0–TIMEOUT3|
|LPUART_10|—||TIMEOUT0–TIMEOUT3|
|LPUART_11|—||TIMEOUT0–TIMEOUT3|
|LPUART_12|—||TIMEOUT0–TIMEOUT3|
|LPUART_13|—||TIMEOUT0–TIMEOUT3|
|LPUART_14|—||TIMEOUT0–TIMEOUT3|
|LPUART_15|—||TIMEOUT0–TIMEOUT3|



##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/076_Low_Power_Universal_Asynchronous_Receiver_Transmitter_-LPUART-/S32K3XXRM_数据表.pdf-4282-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>CFG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>TIMEOUT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-30|Idle Configuration|
|CFG|Configures the behavior of the timeout flag.|
||00b - Flag sets after TIMEOUT characters are received|
||01b - Flag sets when idle for TIMEOUT bit clocks|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4282 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||10b - Flag sets when idle for TIMEOUT bit clocks following the next character|
||11b - Flag sets when idle for at least TIMEOUT bit clocks, but new character is detected before<br>extended idle timeout is reached|
|29-14|Reserved|
|—||
|13-0|Timeout Value|
|TIMEOUT|Configures the timeout value.|



#### 76.6.1.23 Transmit Command Burst Register (TCBR0 - TCBR127) 

##### Offset 

For a = 0 to 127: 

|Register<br>TCBRa|Offset<br>200h + (a × 4h)|
|---|---|



##### Function 

The Transmit Command Burst Register is an alias of the DATA Register designed to support incrementing burst transfers to the transmit FIFO by a DMA controller using aligned 8-bit, 16-bit or 32-bit writes. The size of the Transmit Command Burst Register is 512-bytes. 

- An aligned 32-bit write in this region will push one entry into the transmit FIFO 

- An aligned 16-bit write in this region to TCBRx[15:0] will push one entry into the transmit FIFO 

- An 8-bit write in this region to TCBRx[7:0] will update DATA[7:0], but does not push the data into the transmit FIFO 

- An 8-bit write in this region to TCBRx[15:8] will push the data written to DATA[15:8] plus the previously written DATA[7:0] into the transmit FIFO 

- An 8-bit or 16-bit write in this region to TXBRx[31:16] will be ignored 

~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

|Instance|Register supported|Register not supported|
|---|---|---|
|LPUART_0|TCBR0–TCBR127|—|
|LPUART_1|TCBR0–TCBR127|—|
|LPUART_2|—|TCBR0–TCBR127|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4283 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

Table continued from the previous page... 

|Instance||Register supported|Register not supported|
|---|---|---|---|
|LPUART_3|—||TCBR0–TCBR127|
|LPUART_4|—||TCBR0–TCBR127|
|LPUART_5|—||TCBR0–TCBR127|
|LPUART_6|—||TCBR0–TCBR127|
|LPUART_7|—||TCBR0–TCBR127|
|LPUART_8|—||TCBR0–TCBR127|
|LPUART_9|—||TCBR0–TCBR127|
|LPUART_10|—||TCBR0–TCBR127|
|LPUART_11|—||TCBR0–TCBR127|
|LPUART_12|—||TCBR0–TCBR127|
|LPUART_13|—||TCBR0–TCBR127|
|LPUART_14|—||TCBR0–TCBR127|
|LPUART_15|—||TCBR0–TCBR127|



##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/076_Low_Power_Universal_Asynchronous_Receiver_Transmitter_-LPUART-/S32K3XXRM_数据表.pdf-4284-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>W Reserved<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>W DATA<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function||
|---|---|---|
|31-16<br>—|Reserved||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4284 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|15-0|Data|
|DATA|Data is written to the DATA register.|



#### 76.6.1.24 Transmit Data Burst Register (TDBR0 - TDBR255) 

Offset 

For a = 0 to 255: 

|Register<br>TDBRa|Offset<br>400h + (a × 4h)|
|---|---|



##### Function 

The Transmit Data Burst Register is an alias of the DATA Register designed to support incrementing burst transfers to the transmit FIFO by a DMA controller using 8-bit, 16-bit or 32-bit writes. The size of the Transmit Data Burst Register is 1024-bytes. 

- An aligned 32-bit write in this region will push four DATA byte entries into the transmit FIFO (DATA0 byte first). Note that the register access is extended by 3 wait states. 

- An aligned 16-bit write in this region to either half of a 32-bit word will push two DATA byte entries into the transmit FIFO (DATA0 or DATA2 first). Note that the register access is extended by 1 wait state. 

- An 8-bit write in this region will push one DATA byte entry into the tranmit FIFO. 

Note that byte writes to the DATA register will use the contents of R9T8 for the ninth data bit, R8T9 for the tenth data bit and zero extend the FRETSC bit. 

~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

|Instance|Register supported|Register not supported|
|---|---|---|
|LPUART_0|TDBR0–TDBR255|—|
|LPUART_1|TDBR0–TDBR255|—|
|LPUART_2|—|TDBR0–TDBR255|
|LPUART_3|—|TDBR0–TDBR255|
|LPUART_4|—|TDBR0–TDBR255|
|LPUART_5|—|TDBR0–TDBR255|
|LPUART_6|—|TDBR0–TDBR255|
|LPUART_7|—|TDBR0–TDBR255|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4285 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

Table continued from the previous page... 

|Instance||Register supported|Register not supported|
|---|---|---|---|
|LPUART_8|—||TDBR0–TDBR255|
|LPUART_9|—||TDBR0–TDBR255|
|LPUART_10|—||TDBR0–TDBR255|
|LPUART_11|—||TDBR0–TDBR255|
|LPUART_12|—||TDBR0–TDBR255|
|LPUART_13|—||TDBR0–TDBR255|
|LPUART_14|—||TDBR0–TDBR255|
|LPUART_15|—||TDBR0–TDBR255|



##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||||||||||||
|W||||DA|TA3|||||||DAT|A2||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||||||||||||||
|W||||DA|TA1|||||||DAT|A0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-24|Data|
|DATA3|Data is written to DATA register.|
|23-16|Data|
|DATA2|Data is written to DATA register.|
|15-8|Data|
|DATA1|Data is written to DATA register.|
|7-0|Data|
|DATA0|Data is written to DATA register.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4286 / 4640 

NXP Semiconductors 

Low Power Universal Asynchronous Receiver/Transmitter (LPUART) 

## 76.7 Glossary 

Baud rate Number of bits transmitted or received per second by the LPUART Break character Break character is generated when the transmitter is holding the data line at the space level for at least 1 character time 

Oversampling Number of times the receive circuitry samples the receive input per baud period (i.e. per data bit) 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4287 / 4640 

