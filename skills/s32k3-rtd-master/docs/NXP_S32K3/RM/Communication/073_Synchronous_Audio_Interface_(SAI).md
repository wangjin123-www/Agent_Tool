NXP Semiconductors 

# Chapter 73 Synchronous Audio Interface (SAI) 

## 73.1 Chip-specific SAI information 

### 73.1.1 SAI instances and configuration 

Table 484. SAI instances 

|Instance|S32K322/S32K342/S32K314/S32K324/S32K344/S32K358|S32K311/S32K312|
|---|---|---|
|SAI_0|Yes|No|
|SAI_1|Yes|No|



##### Table 485. SAI configuration 

|Chip|Instances|Synchrono<br>us<br>operation<br>between<br>instances|DMA<br>support|Data Rate/<br>channel|No. of<br>Channels|Frame<br>Synchroni<br>zation|Master<br>Clock<br>Frequency|FIFO<br>size(TX/R<br>X)/<br>Channel|No. of<br>words/<br>frame|
|---|---|---|---|---|---|---|---|---|---|
|S32K322,<br>S32K342,<br>S32K314,<br>S32K324,<br>S32K344,<br>S32K358|SAI_0<br>SAI_1|No|Yes|12.288<br>Mbps|4<br>1|I2S, AC97,<br>and<br>CODEC/D<br>SP<br>interfaces|24.576<br>external<br>audio|8X32 bit|8-16 words|



~~<mark>NOTE</mark>~~ 

The SAI_BCLK (SAI_TX_BCLK, SAI_RX_BCLK), SAI_SYNC (SAI_TX_SYNC, SAI_RX_SYNC), and SAI_DATA (SAI_TX_DATA, SAI_RX_DATA) pins are shared between each module instance's (SAI_0, SAI_1) receiver and transmitter. See the IOMUX file attached to this document for details. At any specific time, either the SAI receiver or the SAI transmitter should be active or they should operate synchronously (only one active at a time). The SAI transmitter and SAI receiver should not be configured to operate simultaneously with inconsistent configurations. 

~~<mark>NOTE</mark>~~ 

Timing specification of SAI master and SAI slave may limit maximum frequency. 

## 73.2 Overview 

The Synchronous Audio Interface (SAI) provides an interface that supports full-duplex serial interfaces with frame synchronization formats such as I<sup>2</sup> S, AC97, TDM, and codec/DSP interfaces. 

### 73.2.1 Block diagram 

The following block diagram also shows the module clocks. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2892 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/073_Synchronous_Audio_Interface_-SAI-/S32K3XXRM_数据表.pdf-2893-02.png)


<!-- Start of picture text -->
Write Read Shift<br>TDRn FIFO FIFO FIFO Register TX_DATA[n]<br>Control Control<br>Write Read Shift<br>TDR0 ControlFIFO FIFO ControlFIFO Register TX_DATA[0]<br>Bus Bit TX_BCLK<br>Clock Clock<br>Control Bit Clock Frame<br>Registers Generation Sync TX_SYNC<br>Control<br>Transmitter<br>Master<br>Synchronous Mode<br>Clock<br>Receiver<br>Control Bit Clock Frame<br>Registers Generation Sync RX_SYNC<br>Control<br>Bus Bit<br>Clock Clock RX_BCLK<br>Read Write<br>Shift<br>RDR0 FIFO FIFO FIFO RX_DATA[0]<br>Control Control Register<br>Read Write<br>Shift<br>RDRn FIFO FIFO FIFO RX_DATA[n]<br>Control Control Register<br>n = Number of Channels<br><!-- End of picture text -->

Figure 391. SAI block diagram 

### 73.2.2 Features 

Some of the features are not supported across all SAI instances; see the chip-specific SAI information in the first section of this chapter. 

- Transmitter with independent bit clock and frame sync supporting 4 data lines 

- Receiver with independent bit clock and frame sync supporting 4 data lines 

- Each data line can support a maximum frame size of 16 words 

- 8- to 32-bit word size 

- Word size configured separately for the first word and remaining words in a frame 

- Asynchronous 8 x 32-bit FIFO for each transmit and receive data line supporting: 

   - Graceful restart after FIFO error 

   - Automatic restart after FIFO error without software intervention 

   - 8-bit and 16-bit data packing into each 32-bit FIFO word 

   - Multiple data line FIFOs combining into single data line FIFO 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2893 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

## 73.3 Functional description 

This section provides a complete functional description of the block. 

### 73.3.1 Modes of operation 

Module power modes include Run mode, and Debug mode. 

##### Run mode 

In Run mode, the SAI transmitter and receiver operate normally. 

##### Debug mode 

In Debug mode, the SAI transmitter and/or receiver continues operating if the Debug Enable bit is set. When TCSR[DBGE] or RCSR[DBGE] bit is clear and Debug mode is entered, SAI is disabled after completing the current transmit or receive frame. Debug mode does not affect the transmitter and receiver bit clocks. 

### 73.3.2 Synchronous modes 

The SAI transmitter and receiver can operate synchronously to each other. 

##### Synchronous mode 

The SAI transmitter and receiver can be configured to operate with synchronous bit clock and frame sync. 

If both the transmitter and receiver use the transmitter bit clock and frame sync: 

- Configure the transmitter for asynchronous operation and the receiver for synchronous operation. 

- Enable the receiver in synchronous mode only after both the transmitter and receiver are enabled. 

- Enable the transmitter last and disable the transmitter first. 

If both the transmitter and receiver use the receiver bit clock and frame sync: 

- Configure the receiver for asynchronous operation and the transmitter for synchronous operation. 

- Enable the transmitter in synchronous mode only after both the receiver and transmitter are enabled. 

- Enable the receiver last and disable the receiver first. 

When operating in synchronous mode, the transmitter and receiver share only the bit clock, frame sync, and transmitter/receiver enable. Otherwise, the transmitter and receiver operate independently, although the configuration registers must be configured consistently across both the transmitter and receiver. 

### 73.3.3 Frame sync configuration 

When enabled, the SAI continuously transmits and/or receives frames of data. Each frame consists of a fixed number of words and each word consists of a fixed number of bits. Within each frame, any given word can be masked causing the receiver to ignore that word and the transmitter to tri-state for the duration of that word. 

The frame sync signal indicates the start of each frame. A valid frame sync requires a rising edge (if active high) or falling edge (if active low) to be detected and the transmitter or receiver cannot be busy with a previous frame. A valid frame sync is also ignored (slave mode) or not generated (master mode) for the first four bit clock cycles after enabling the transmitter or receiver. 

The transmitter and receiver frame sync can be configured independently with any of the following options: 

- Generate externally or internally 

- Require active high or active low 

- Assert with the first bit in frame or assert one bit early 

- Assert for a duration of between 1 bit clock and the first word length 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2894 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

- Set frame length from 1 to 16 words per frame 

- Support word length of 8 to 32 bits per word 

   - First word length and remaining word lengths can be configured separately 

- Transmit/Receive words MSB first or LSB first 

These configuration options cannot be changed after enabling the SAI transmitter or receiver. 

### 73.3.4 Data FIFO 

Each transmit and receive channel includes a 8 x 32-bit size FIFO. To access the FIFO data use the SAI Transmit/Receive Data Registers. 

#### 73.3.4.1 Data alignment 

Data in the FIFO can be aligned anywhere within the 32-bit wide register through the use of the First Bit Shifted configuration field, which selects the bit index (between 31 and 0) of the first bit shifted. 

Examples of supported data alignment and the required First Bit Shifted configuration are illustrated in Figure 392 for LSB First configurations and Figure 393 for MSB First configurations. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/073_Synchronous_Audio_Interface_-SAI-/S32K3XXRM_数据表.pdf-2895-12.png)


<!-- Start of picture text -->
How data is written to the FIFO, using First Bit Shifted field (FBT)<br>FBT values LSB first<br>for<br>LSB first 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>00000 DATA[31:0]<br>00000 DATA[23:0]<br>01000 DATA[23:0]<br>00000 DATA[19:0]<br>01100 DATA[19:0]<br>00000 DATA[15:0]<br>10000 DATA[15:0]<br>00000 DATA[11:0]<br>10100 DATA[11:0]<br>00000 DATA[7:0]<br>11000 DATA[7:0]<br>Number of bits being transferred<br>shown above:<br>First Bit Shifted (FBT) First Bit Shifted (FBT)<br>24-bit data 12-bit data<br>TCR5[FBT] Or RCR5[FBT] 20-bit data   8-bit data<br>16-bit data<br>TX Config 5 Register RX Config 5 Register<br><!-- End of picture text -->

Figure 392. SAI first bit shifted, LSB first 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2895 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/073_Synchronous_Audio_Interface_-SAI-/S32K3XXRM_数据表.pdf-2896-02.png)


<!-- Start of picture text -->
How data is written to the FIFO, using First Bit Shifted field (FBT)<br>FBT values MSB first<br>for<br>MSB first 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>11111 DATA[31:0]<br>10111 DATA[23:0]<br>11111 DATA[23:0]<br>10011 DATA[19:0]<br>11111 DATA[19:0]<br>01111 DATA[15:0]<br>11111 DATA[15:0]<br>01011 DATA[11:0]<br>11111 DATA[11:0]<br>00111 DATA[7:0]<br>11111 DATA[7:0]<br>Number of bits being transferred<br>shown above:<br>First Bit Shifted (FBT) First Bit Shifted (FBT)<br>24-bit data 12-bit data<br>TCR5[FBT] Or RCR5[FBT] 20-bit data   8-bit data<br>16-bit data<br>TX Config 5 Register RX Config 5 Register<br><!-- End of picture text -->

Figure 393. SAI first bit shifted, MSB first 

#### 73.3.4.2 FIFO pointers 

When writing to a Transmit Data Register (TDRn), the Write FIFO Pointer (WFP) of the corresponding Transmit FIFO Register (TFRn) increments after each valid write. The SAI supports 8-bit, 16-bit, and 32-bit writes to the Transmit Data Register and the FIFO pointer increments after each individual write. Note that 8-bit writes should only be used when transmitting up to 8-bit data; 16-bit writes should only be used when transmitting up to 16-bit data. 

- If the Transmit FIFO is full, writes to a Transmit Data Register are ignored. 

- If the Transmit FIFO is empty, to avoid a FIFO underrun, write to the Transmit Data Register at least 3 bit clocks before the start of the next unmasked word. 

- Before enabling the transmitter, initialize the Transmit FIFO with data (because after enabling the transmitter, the transmitter starts a new frame, and if no data is in the FIFO, then the transmitter immediately give an error). 

When reading a Receive Data Register (RDRn), the Read FIFO Pointer (RFP) of the corresponding >Receive FIFO Register (RFRn) increments after each valid read. The SAI supports 8-bit, 16-bit, and 32-bit reads from the RDR and the FIFO pointer will increment after each individual read. Note that 8-bit reads should only be used when receiving up to 8-bit data; 16-bit reads should only be used when receiving up to 16-bit data. 

- If the Receive FIFO is empty, reads from a Receive Data Register are ignored. 

- If the Receive FIFO is full, to avoid a FIFO overrun, read the Receive Data Register at least 3 bit clocks before the end of an unmasked word. 

#### 73.3.4.3 FIFO packing 

FIFO packing supports storing multiple 8-bit or 16-bit data words in one 32-bit FIFO word for the transmitter and/or receiver. While this can be emulated by adjusting the number of bits per word and number of words per frame (for example, one 32-bit word per frame versus two 16-bit words per frame), FIFO packing does not require even multiples of words per frame and fully supports word masking. When FIFO packing is enabled, the FIFO pointers only increment when the full 32-bit FIFO word has been 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2896 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

written (transmit) or read (receive) by software, supporting scenarios where different words within each frame are loaded/stored in different areas of memory. 

Using 16-bit FIFO packing for transmit, the transmit shift register loads at the start of each frame and after every second unmasked transmit word. The first word transmitted is taken from 16-bit word at byte offset 0x0 (the first bit is selected by TCR5[FBT] and must be configured within this 16-bit word). The second word transmitted is taken from the 16-bit word at byte offset 0x2 (the first bit is selected by TCR5[FBT][3:0]). The transmitter transmits logic zero until the start of the next word once the 16-bit word has been transmitted. 

Using 16-bit FIFO packing for receive, the receive shift register is stored after every second unmasked received word, and at the end of each frame if there is an odd number of unmasked-received words in each frame. The first word received is stored in the 16-bit word at byte offset 0x0 (the first bit is selected by RCR5[FBT] and must be configured within this 16-bit word). The second word received is stored in the 16-bit word at byte offset 0x2 (the first bit is selected by RCR5[FBT][3:0]). The receiver ignores received data until the start of the next word once the 16-bit word has been received. 

The 8-bit FIFO packing is similar to 16-bit packing except four words are loaded or stored into each 32-bit FIFO word. The first word is loaded/stored in byte offset 0x0, second word in byte offset 0x1, third word in byte offset 0x2, and fourth word in byte offset 0x3. The TCR5[FBT] and/or RCR5[FBT] must be configured within byte offset 0x0. 

#### 73.3.4.4 FIFO Combine 

FIFO Combining mode allows the separate FIFOs for multiple data channels to be used as a single FIFO for either software accesses or a single data channel or both. Note that the enabled data channels must be contiguous and data channel 0 must be enabled when using FIFO Combine mode. 

Combining FIFOs for software access (writing transmit FIFO registers, reading receive FIFO registers) allows a DMA controller or software to read or write multiple FIFOs without incrementing the address that is accessed. Once enabled, the first software access to a FIFO register accesses the first enabled channel FIFO, while the second access to a FIFO register accesses the second enabled channel FIFO. This continues until software accesses the last enabled channel FIFO and the pointer resets back to the first enabled channel FIFO. To reset the pointer manually, software can reset the FIFOs or disable FIFO combining on software accesses. 

Combining FIFOs for transmit data channels allows one data channel to use the FIFOs of all enabled channel FIFOs, with identical data output on each enabled data channel. The transmit shift registers for all enabled data channels load at the start of each frame and every N unmasked words (where N is the number of enabled data channels). The first word transmitted loads from the first enabled channel FIFO, while the second word transmitted loads from the second enabled channel FIFO, and so on until the end of the frame. Because the first word in each frame always loads from the first enabled data channel, it is recommended that the number of unmasked words in each frame is evenly divisible by the number of enabled data channels. 

Combining FIFOs for receive data channels allows one data channel to use the FIFOs of all enabled channel FIFOs, with received data from channel 0 stored into each enabled data channel. The receive shift register for all enabled data channels are stored after every N unmasked words (where N is the number of enabled data channels). The first word received stores to the first enabled channel FIFO, while the second word received stores to the second enabled channel FIFO, and so on until the end of the frame. Because the first word in each frame always stores to the first enabled data channel, it is recommended that the number of unmasked words in each frame is evenly divisible by the number of enabled data channels. 

Note that combining FIFOs for data channels loads or stores each channel FIFO at the same time. This means that FIFO error conditions are only checked every N words (where N is the number of enabled data channels) and that the FIFO warning and request flags assert if any of the enabled data channel meets the warning flag or request flag conditions. 

### 73.3.5 Word mask register 

The SAI transmitter and receiver each contain a word mask register (Transmit Mask (TMR) and Receive Mask (RMR)) that can be used to mask any word in the frame. Because the word mask register is double buffered, software can update it before the end of each frame to mask a particular word in the next frame. 

The TMR causes the Transmit Data pin to be tri-stated for the length of each selected word and the transmit FIFO is not read for masked words. 

The RMR causes the received data for each selected word to be discarded and not written to the receive FIFO. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2897 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

### 73.3.6 Interrupts and DMA requests 

The SAI transmitter and receiver generate separate interrupts and separate DMA requests, but support the same status flags. Asynchronous interrupts are only generated when the system clock is gated provided the corresponding BCLK continues. 

#### 73.3.6.1 FIFO request flag 

The FIFO request flag sets based on the number of entries in the FIFO and the FIFO watermark configuration. 

The transmit FIFO request flag sets when the number of entries in any of the enabled transmit FIFOs is less than or equal to the transmit FIFO watermark configuration and clears when the number of entries in each enabled transmit FIFO is greater than the transmit FIFO watermark configuration. 

The receive FIFO request flag sets when the number of entries in any of the enabled receive FIFOs is greater than the receive FIFO watermark configuration and clears when the number of entries in each enabled receive FIFO is less than or equal to the receive FIFO watermark configuration. 

The FIFO request flag can generate an interrupt or a DMA request. 

#### 73.3.6.2 FIFO warning flag 

The FIFO warning flag sets based on the number of entries in the FIFO. 

The transmit warning flag sets when the number of entries in any of the enabled transmit FIFOs is empty and clears when the number of entries in each enabled transmit FIFO is not empty. 

The receive warning flag sets when the number of entries in any of the enabled receive FIFOs is full and clears when the number of entries in each enabled receive FIFO is not full. 

The FIFO warning flag can generate an Interrupt or a DMA request. 

#### 73.3.6.3 FIFO error flag 

The Transmit FIFO Error Flag (TCSR[FEF] = 1]) sets when any of the enabled transmit FIFOs underrun. After the error flag sets, all enabled transmit channels transmit zero data before TCSR[FEF] clears. 

When FIFO Continue on Error is enabled (TCR4[FCONT] = 1), the FIFO continues transmitting data following an underrun without software intervention. To ensure that data transmits in the correct order, the transmitter continues from the same word number in the frame that caused the FIFO to underrun, but only after new data writes to the transmit FIFO. Software should still clear the TCSR[FEF] flag, but without reinitializing the transmit FIFOs. 

The Receive FIFO Error Flag sets (RCSR[FEF] = 1) when any of the enabled receive FIFOs overflow. After the flag is set, all enabled receive channels discard received data until RCSR[FEF] clears and the next receive frame starts. Empty all enabled receive FIFOs before RCSR[FEF] clears. 

When Receive FIFO Continue on Error is enabled (RCR4[FCONT] = 1), the FIFO continues receiving data following an overflow without software intervention. To ensure that data is received in the correct order, the receiver continues from the same word number in the frame that caused the FIFO to overflow, but only after data has been read from the receive FIFO. Software should still clear the RCSR[FEF] flag, but without emptying the receive FIFOs. 

The FIFO Error Flag can generate only an interrupt. 

#### 73.3.6.4 Sync error flag 

The Sync Error Flag (TCSR[SEF] or RCSR[SEF]) sets, when configured for an externally generated frame sync and the external frame sync asserts when the transmitter or receiver is busy with the previous frame. The external frame sync assertion is ignored and the sync error flag sets. When the Sync Error Flag sets, the transmitter or receiver continues checking for frame sync assertion when idle or at the end of each frame. 

The Sync Error Flag can only generate an interrupt. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2898 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

#### 73.3.6.5 Word start flag 

The Word Start Flag sets (TCSR[WSF] = 1) at the start of the second bit clock for the selected word, as configured by the Word Flag Configuration field (TCR3[WDFL]). 

The Word Start Flag can generate an interrupt only. 

### 73.3.7 Clocking 

The SAI clocks include: 

- Audio master clock 

- Bit clock 

- Bus clock 

##### Audio master clock 

The audio master clock generates the bit clock when the receiver or transmitter is configured for an internally generated bit clock. The transmitter and receiver can independently select between the bus clock and up to three audio master clocks to generate the bit clock. 

The audio master clock generation and selection is chip-specific. Refer to chip-specific clocking information about how the audio master clocks are generated. 

##### Bit clock 

The SAI transmitter and receiver support asynchronous free-running bit clocks that can be generated internally from an audio master clock or supplied externally. There is also the option for synchronous bit clock and frame sync operation between the receiver and transmitter or between multiple SAI peripherals. 

- If both transmitter and receiver are configured for asynchronous operation, then the transmitter and receiver each use their own bit clock and frame sync. 

- If the transmitter is configured for asynchronous mode and the receiver is configured for synchronous mode, then both transmitter and receiver use the transmitter bit clock and frame sync. 

- If the receiver is configured for asynchronous mode and the transmitter is configured for synchronous mode, then both transmitter and receiver use the receiver bit clock and frame sync. 

Note that the software configures synchronous or asynchronous mode, and that choice selects the bit clock/frame sync used. 

Externally generated bit clocks must be: 

- Enabled, before the SAI transmitter or receiver is enabled 

- Disabled, after the SAI transmitter or receiver is disabled and completes its current frames 

If the SAI transmitter or receiver uses an externally generated bit clock in asynchronous mode and that bit clock is generated by an SAI that is disabled in Stop mode, then the transmitter or receiver should be disabled by software before entering stop mode. This issue does not apply when the transmitter or receiver is in a synchronous mode because all synchronous SAIs are enabled and disabled simultaneously. 

##### Bus clock 

The bus clock is used by the control and configuration registers and to generate synchronous interrupts and DMA requests. 

~~<mark>NOTE</mark>~~ 

Although there is no minimum bus clock frequency specified, the bus clock frequency must be fast enough (relative to the bit clock frequency) to ensure that the FIFOs can be serviced, without generating either a transmitter FIFO underrun or receiver FIFO overflow condition. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2899 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

### 73.3.8 Reset 

The SAI is asynchronously reset on system reset. The SAI has a software reset and a FIFO reset. 

##### Software reset 

The SAI transmitter includes a software reset that resets all transmitter internal logic, including the bit clock generation, status flags, and FIFO pointers. This software reset does not reset the configuration registers. The software reset remains asserted until cleared by software. 

The SAI receiver includes a software reset that resets all receiver internal logic, including the bit clock generation, status flags, and FIFO pointers. This software reset does not reset the configuration registers. The software reset remains asserted until cleared by software. 

##### FIFO reset 

The SAI transmitter includes a FIFO reset that synchronizes the FIFO write pointer to the same value as the FIFO read pointer. This FIFO reset empties the FIFO contents and is used after TCSR[FEF] is set, and before the FIFO is re-initialized and TCSR[FEF] is cleared. The FIFO reset is asserted for one cycle only. 

The SAI transmitter can also reset the FIFO of individual data channels by setting the appropriate TCR3[CFR] bit. Use only when the corresponding TCR3[TCE] is clear. 

The SAI receiver includes a FIFO reset that synchronizes the FIFO read pointer to the same value as the FIFO write pointer. This FIFO reset empties the FIFO contents. Use after the RCSR[FEF] is set and any remaining data has been read from the FIFO, and before the RCSR[FEF] is cleared. The FIFO reset is asserted for one cycle only. 

The SAI receiver can also reset the FIFO of individual data channels by setting the appropriate RCR3[RCE] bit. Use this reset only when the corresponding RCR3[RCE] bit is clear. 

## 73.4 External signals 

|Name|Function|I/O|
|---|---|---|
|TX_BCLK|Transmit Bit Clock. The bit clock is an input<br>when externally generated and an output when<br>internally generated.|I/O|
|TX_SYNC|Transmit Frame Sync. The frame sync is<br>an input sampled synchronously by the bit<br>clock when externally generated and an output<br>generated synchronously by the bit clock when<br>internally generated.|I/O|
|TX_DATA[3:0]|Transmit Data. The transmit data is generated<br>synchronously by the bit clock and is tristated<br>whenever not transmitting a word.|O|
|RX_BCLK|Receive Bit Clock. The bit clock is an input<br>when externally generated and an output when<br>internally generated.|I/O|
|RX_SYNC|Receive Frame Sync. The frame sync is an input<br>sampled synchronously by the bit clock when<br>externally generated and an output generated<br>synchronously by the bit clock when internally<br>generated.|I/O|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2900 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Table continued from the previous page... 

|Name|Function|I/O|
|---|---|---|
|RX_DATA[3:0]|Receive Data. The receive data is sampled|I|
||synchronously by the bit clock.||



## 73.5 Memory map and register definition 

A read or write access to an address from offset 0x100 and above will result in a bus error. 

### 73.5.1 SAI register descriptions 

#### 73.5.1.1 SAI memory map 

SAI_0 base address: 4036_C000h 

SAI_1 base address: 404D_C000h 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|0h|Version ID (VERID)|32|RO|0301_0000h|
|4h|Parameter (PARAM)|32|RO|See<br>description|
|8h|Transmit Control (TCSR)|32|RW|0000_0000h|
|Ch|Transmit Configuration 1 (TCR1)|32|RW|0000_0000h|
|10h|Transmit Configuration 2 (TCR2)|32|RW|0000_0000h|
|14h|Transmit Configuration 3 (TCR3)|32|RW|0000_0000h|
|18h|Transmit Configuration 4 (TCR4)|32|RW|0000_0000h|
|1Ch|Transmit Configuration 5 (TCR5)|32|RW|0000_0000h|
|20h - 2Ch|Transmit Data (TDR0 - TDR3)|32|WORZ|See<br>description|
|40h - 4Ch|Transmit FIFO (TFR0 - TFR3)|32|RO|See<br>description|
|60h|Transmit Mask (TMR)|32|RW|0000_0000h|
|88h|Receive Control (RCSR)|32|RW|0000_0000h|
|8Ch|Receive Configuration 1 (RCR1)|32|RW|0000_0000h|
|90h|Receive Configuration 2 (RCR2)|32|RW|0000_0000h|
|94h|Receive Configuration 3 (RCR3)|32|RW|0000_0000h|
|98h|Receive Configuration 4 (RCR4)|32|RW|0000_0000h|
|9Ch|Receive Configuration 5 (RCR5)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2901 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Table continued from the previous page... 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|A0h - ACh|Receive Data (RDR0 - RDR3)|32|RO|See<br>description|
|C0h - CCh|Receive FIFO (RFR0 - RFR3)|32|RO|See<br>description|
|E0h|Receive Mask (RMR)|32|RW|0000_0000h|



#### 73.5.1.2 Version ID (VERID) 

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
|Reset|0|0|0|0|0|0|1|1|0|0|0|0|0|0|0|1|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||FEAT|URE||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-24|Major Version Number|
|MAJOR|This read only field returns the major version number for the specification.|
|23-16|Minor Version Number|
|MINOR|This read only field returns the minor version number for the specification.|
|15-0|Feature Specification Number|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2902 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|FEATURE|This read only field returns the feature set number.|
||0000_0000_0000_0000b - Standard feature set.|



#### 73.5.1.3 Parameter (PARAM) 

##### Offset 

|Register|Offset|
|---|---|
|PARAM|4h|



##### Function 

Contains parameter values that were implemented in the module. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/073_Synchronous_Audio_Interface_-SAI-/S32K3XXRM_数据表.pdf-2903-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 FRAME<br>W<br>Reset See Register reset values.<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 FIFO  0 DATALINE<br>W<br>Reset See Register reset values.<br><!-- End of picture text -->

##### Register reset values 

|Register|Reset value|
|---|---|
|PARAM|SAI_0: 0004_0304h|
||SAI_1: 0004_0301h|



##### Fields 

|Field|Function|
|---|---|
|31-20<br>—|Reserved|
|19-16|Frame Size|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2903 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|FRAME|The maximum number of slots per frame is 2^FRAME.|
|15-12<br>—|Reserved|
|11-8|FIFO Size|
|FIFO|The number of words in each FIFO is 2^FIFO.|
|7-4<br>—|Reserved|
|3-0|Number of Datalines|
|DATALINE|The number of datalines implemented.|



#### 73.5.1.4 Transmit Control (TCSR) 

##### Offset 

|Register|Offset|
|---|---|
|TCSR|8h|



##### Function 

Contains transmitter enable fields including resets, error and interrupt enable fields, and error flag fields. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|TE|Reserv|DBGE|BCE||0|0|SR||0||WSF|SEF|FEF|FWF|FRF|
|W||ed|||||FR|||||W1C|W1C|W1C|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||0||WSIE|SEIE|FEIE|FWIE|FRIE||0|||0||FWDE|FRDE|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2904 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Fields 

|Field|Function|
|---|---|
|31|Transmitter Enable|
|TE|Enables/disables the transmitter. When software clears this field, the transmitter remains enabled, and<br>this bit remains set, until the end of the current frame.<br>0b - Transmitter is disabled.<br>1b - Transmitter is enabled, or transmitter has been disabled and has not yet reached end of<br>frame.|
|30|Reserved Software should only write zero to this reserved bit.|
|—<br>29<br>DBGE|Debug Enable<br>Enables/disables transmitter operation in Debug mode. The transmit bit clock is not affected by debug<br>mode.<br>0b - Transmitter is disabled in Debug mode, after completing the current frame.<br>1b - Transmitter is enabled in Debug mode.|
|28<br>BCE|Bit Clock Enable<br>Enables the transmit bit clock, separately from the TE. This field is automatically set whenever TE is set.<br>When software clears this field, the transmit bit clock remains enabled, and this bit remains set, until the<br>end of the current frame.<br>0b - Transmit bit clock is disabled.<br>1b - Transmit bit clock is enabled.|
|27-26<br>—|Reserved|
|25<br>FR|FIFO Reset<br>Empties the FIFO, and sets the FIFO read and write pointers to the same value, which may or may not<br>be zero.<br>The FIFO reset is asserted for one cycle only.<br>~~NOTE~~<br>Reading this field always returns zero. Reset FIFO pointers when the transmitter is disabled or the FIFO<br>error flag is set.<br>0b - No effect.<br>1b - FIFO reset.|
|24<br>SR|Software Reset<br>When set, resets the internal transmitter logic including the FIFO read and write pointers.<br>Software-visible registers are not affected, except for the status registers.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2905 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Table continued from the previous page... 

|Field|Function<br>The software reset remains asserted until cleared by software. Software clears the bit by<br>writing 0.<br>~~NOTE~~<br>0b - No effect<br>1b - Software reset|
|---|---|
|23-21<br>—|Reserved|
|20<br>WSF|Word Start Flag<br>Indicates that the start of the configured word has been detected. Write a logic 1 to this field to clear this<br>flag.<br>0b - Start of word not detected.<br>1b - Start of word detected.|
|19<br>SEF|Sync Error Flag<br>Indicates that an error in the externally-generated frame sync has been detected. Write a logic 1 to this<br>field to clear this flag.<br>0b - Sync error not detected.<br>1b - Frame sync error detected.|
|18<br>FEF|FIFO Error Flag<br>Indicates that an enabled transmit FIFO has underrun. Write a logic 1 to this field to clear this flag.<br>0b - Transmit underrun not detected.<br>1b - Transmit underrun detected.|
|17<br>FWF|FIFO Warning Flag<br>Indicates that an enabled transmit FIFO is empty.<br>0b - No enabled transmit FIFO is empty.<br>1b - Enabled transmit FIFO is empty.|
|16<br>FRF|FIFO Request Flag<br>Indicates that the number of words in an enabled transmit channel FIFO is less than or equal to the<br>transmit FIFO watermark.<br>0b - Transmit FIFO watermark has not been reached.<br>1b - Transmit FIFO watermark has been reached.|
|15-13<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2906 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|12|Word Start Interrupt Enable|
|WSIE|Enables/disables word start interrupts.|
||0b - Disables interrupt.<br>1b - Enables interrupt.|
|11<br>SEIE|Sync Error Interrupt Enable<br>Enables/disables sync error interrupts.<br>0b - Disables interrupt.<br>1b - Enables interrupt.|
|10<br>FEIE|FIFO Error Interrupt Enable<br>Enables/disables FIFO error interrupts.<br>0b - Disables the interrupt.<br>1b - Enables the interrupt.|
|9<br>FWIE|FIFO Warning Interrupt Enable<br>Enables/disables FIFO warning interrupts.<br>0b - Disables the interrupt.<br>1b - Enables the interrupt.|
|8<br>FRIE|FIFO Request Interrupt Enable<br>Enables/disables FIFO request interrupts.<br>0b - Disables the interrupt.<br>1b - Enables the interrupt.|
|7-5<br>—|Reserved|
|4-2<br>—|Reserved|
|1|FIFO Warning DMA Enable|
|FWDE|Enables/disables DMA warning.|
||0b - Disables the DMA warning.|
||1b - Enables the DMA warning.|
|0|FIFO Request DMA Enable|
|FRDE|Enables/disables DMA requests.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2907 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Disables the DMA request.|
||1b - Enables the DMA request.|



#### 73.5.1.5 Transmit Configuration 1 (TCR1) 

##### Offset 

|Register|Offset|
|---|---|
|TCR1|Ch|



##### Function 

Configures the watermark level for all enabled transmit channels. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||0|||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||||||0||||||||TFW||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-3<br>—|Reserved|
|2-0|Transmit FIFO Watermark|
|TFW|Number of 32-bit FIFO words|
||000b - 1 FIFO word|
||001b - 2 FIFO words|
||010b-110b - (TFW +1) FIFO words|
||111b - 8 FIFO words|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2908 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

#### 73.5.1.6 Transmit Configuration 2 (TCR2) 

##### Offset 

|Register|Offset|
|---|---|
|TCR2|10h|



##### Function 

Contains the SYNC mode and clock setting fields. 

~~<mark>NOTE</mark>~~ 

This register must not be altered when TCSR[TE] is set. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/073_Synchronous_Audio_Interface_-SAI-/S32K3XXRM_数据表.pdf-2909-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R 0 0<br>SYNC  ed  BCI  MSEL  BCP  BCD  BYP<br>W 0<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>DIV<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Reserved|
|—||
|30|Synchronous Mode|
|SYNC|Configures between asynchronous and synchronous modes of operation. When configured for a<br>synchronous mode of operation, the receiver must be configured for asynchronous operation.<br>0b - Asynchronous mode.|
||1b - Synchronous with receiver.|
|29|Reserved|
|—||
|28|Bit Clock Input|
|BCI||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2909 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Table continued from the previous page... 

|Field|Function<br>When this field is set and using an internally generated bit clock in either synchronous or asynchronous<br>mode, the bit clock actually used by the transmitter is delayed by the pad output delay (the transmitter is<br>clocked by the pad input as if the clock was externally generated). This has the effect of decreasing the data<br>input setup time, but increasing the data output valid time.<br>The slave mode timing from the datasheet should be used for the transmitter when this bit is set. In<br>synchronous mode, this bit allows the transmitter to use the slave mode timing from the datasheet, while the<br>receiver uses the master mode timing. This field has no effect when configured for an externally generated<br>bit clock .<br>When BCI=1 both the input buffer and output buffer must be enabled for the BCLK pad.<br>~~NOTE~~<br>0b - No effect.<br>1b - Internal logic is clocked as if bit clock was externally generated.|
|---|---|
|27-26<br>MSEL|MCLK Select<br>Selects the audio Master Clock option used to generate an internally generated bit clock. This field has<br>no effect when configured for an externally generated bit clock.<br>~~NOTE~~|
||Depending on the device, some Master Clock options might not be available. See the<br>chip-specific information for the meaning of each option.|
||00b - Bus Clock selected.<br>01b - Master Clock (MCLK) 1 option selected.<br>10b - Master Clock (MCLK) 2 option selected.<br>11b - Master Clock (MCLK) 3 option selected.|
|25<br>BCP|Bit Clock Polarity<br>Configures the polarity of the bit clock.<br>0b - Bit clock is active high with drive outputs on rising edge and sample inputs on falling edge.<br>1b - Bit clock is active low with drive outputs on falling edge and sample inputs on rising edge.|
|24|Bit Clock Direction|
|BCD|Configures the direction of the bit clock.<br>0b - Bit clock is generated externally in Slave mode.<br>1b - Bit clock is generated internally in Master mode.|
|23|Bit Clock Bypass|
|BYP|Bypasses the bit clock divider, internal bit clock is divide by 1 of the audio master clock.<br>0b - Internal bit clock is generated from bit clock divider.<br>1b - Internal bit clock is divide by one of the audio master clock.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2910 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|22-8|Reserved|
|—||
|7-0|Bit Clock Divide|
|DIV|Divides down the audio master clock to generate the bit clock when configured for an internal bit clock.<br>The division value is (DIV + 1) * 2.|



#### 73.5.1.7 Transmit Configuration 3 (TCR3) 

##### Offset 

|Register|Offset|
|---|---|
|TCR3|14h|



##### Function 

Contains the transmit channel settings. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||0||||0<br>CFR||||0||||TCE|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||0||||||||WDFL|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-28|Reserved|
|—||
|27-24|Channel FIFO Reset|
|CFR|Resets the FIFO pointers for a specific channel. Reading this field always returns zero. FIFO pointers should<br>only be reset when a channel is disabled or the FIFO error flag is set.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2911 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/073_Synchronous_Audio_Interface_-SAI-/S32K3XXRM_数据表.pdf-2912-03.png)


<!-- Start of picture text -->
Field Function<br>The width of CFR field = the number of transmit channels (call it N). For example, if CFR is 2 bits wide, then<br>bit position 24 refers to transmit channel 1 FIFO pointer and bit position 25 refers to transmit channel 2 FIFO<br>pointer. Setting bit 24 resets transmit channel 1 FIFO pointer, and setting bit 25 enables transmit channel<br>2 FIFO pointer. Setting bit N will reset transmit channel N FIFO pointer.<br>  NOTE<br>When there is only a single channel, there is no need for individual channel FIFO reset<br>(TCR3[CFR]). In the case of a single channel, use the global FIFO reset (TCSR[FR]).<br>0b - No effect.<br>1b - Transmit data channel N FIFO is reset.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>SAI_0 TCR3 —<br>SAI_1 — TCR3<br>23-20 Reserved<br>—<br>19-16 Transmit Channel Enable<br>TCE Enables the corresponding data channel for transmit operation. Changing TCE field will take effect<br>immediately for generating the FIFO request and warning flags, but at the end of each frame for<br>transmit operation.<br>The width of TCE field = the number of transmit channels (call it N). For example, if TCE field is 2 bits wide,<br>then bit position 16 refers to transmit channel 1 and bit position 17 refers to transmit channel 2. Setting bit 16<br>enables transmit channel 1, and setting bit 17 enables transmit channel 2. Setting bit N will enable transmit<br>channel N.<br>0b - Transmit data channel N is disabled.<br>1b - Transmit data channel N is enabled.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>SAI_0 TCR3 —<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2912 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/073_Synchronous_Audio_Interface_-SAI-/S32K3XXRM_数据表.pdf-2913-03.png)


<!-- Start of picture text -->
Field Function<br>Instance Field supported in Field not supported in<br>SAI_1 TCR3[16] TCR3[19–17]<br>15-4 Reserved<br>—<br>3-0 Word Flag Configuration<br>WDFL Configures which word sets the start of word flag. The value written must be one less than the word number.<br>For example, writing 0 configures the first word in the frame. When configured to a value greater than<br>TCR4[FRSZ], then the start of word flag is never set.<br><!-- End of picture text -->

#### 73.5.1.8 Transmit Configuration 4 (TCR4) 

##### Offset 

|Register|Offset|
|---|---|
|TCR4|18h|



##### Function 

Contains the transmit fields for FIFO Combine Mode, FIFO Packing Mode, and frame sync settings. 

~~<mark>NOTE</mark>~~ This register must not be altered when TCSR[TE] is set. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/073_Synchronous_Audio_Interface_-SAI-/S32K3XXRM_数据表.pdf-2913-10.png)


<!-- Start of picture text -->
Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 FCON 0<br>FCOMB  FPACK  FRSZ<br>T<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 CHMO ONDE<br>SYWD  MF  FSE  FSP  FSD<br>D  M<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2913 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Fields 

|Field|Function|
|---|---|
|31-29<br>—|Reserved|
|28<br>FCONT|FIFO Continue on Error<br>Configures when the SAI will continue transmitting after a FIFO error has been detected.<br>0b - On FIFO error, the SAI will continue from the start of the next frame after the FIFO error flag<br>has been cleared.<br>1b - On FIFO error, the SAI will continue from the same word that caused the FIFO error to set<br>after the FIFO warning flag has been cleared.|
|27-26<br>FCOMB|FIFO Combine Mode<br>When FIFO combine mode is enabled for FIFO writes, software writing to any FIFO data register will<br>alternate the write among the enabled data channel FIFOs. For example, if two data channels are enabled<br>then the first write will be performed to the first enabled data channel FIFO and the second write will be<br>performed to the second enabled data channel FIFO. Reseting the FIFO or disabling FIFO combine mode<br>for FIFO writes will reset the pointer back to the first enabled data channel.<br>When FIFO combine mode is enabled for FIFO reads from the transmit shift registers, the transmit data<br>channel output will alternate between the enabled data channel FIFOs. For example, if two data channels<br>are enabled then the first unmasked word will be transmitted from the first enabled data channel FIFO and<br>the second unmasked word will be transmitted from the second enabled data channel FIFO. Since the first<br>word of the frame is always transmitted from the first enabled data channel FIFO, it is recommended that<br>the number of unmasked words per frame is evenly divisible by the number of enabled data channels.<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>~~NOTE~~|
||Instance<br>Field supported in<br>Field not supported in|
||SAI_0<br>TCR4<br>—|
||SAI_1<br>—<br>TCR4<br>00b - FIFO combine mode disabled.<br>01b - FIFO combine mode enabled on FIFO reads (from transmit shift registers).|



10b - FIFO combine mode enabled on FIFO writes (by software). 

11b - FIFO combine mode enabled on FIFO reads (from transmit shift registers) and writes (by software). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2914 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Table continued from the previous page... 

|Field<br>25-24|Function<br>FIFO Packing Mode|
|---|---|
|FPACK|Enables packing of 8-bit data or 16-bit data into each 32-bit FIFO word. If the word size is greater than 8-bit<br>or 16-bit then only the first 8-bit or 16-bits are loaded from the FIFO. The first word in each frame always<br>starts with a new 32-bit FIFO word and the first bit shifted must be configured within the first packed word.<br>When FIFO packing is enabled, the FIFO write pointer will only increment when the full 32-bit FIFO word<br>has been written by software.<br>00b - FIFO packing is disabled.<br>01b - Reserved<br>10b - 8-bit FIFO packing is enabled.<br>11b - 16-bit FIFO packing is enabled.|
|23-20<br>—|Reserved|
|19-16<br>FRSZ|Frame size<br>Configures the number of words in each frame. The value written must be one less than the number of<br>words in the frame. For example, write 0 for one word per frame. The maximum supported frame size is<br>16 words.|
|15-13<br>—|Reserved|
|12-8|Sync Width|
|SYWD|Configures the length of the frame sync in number of bit clocks. The value written must be one less than<br>the number of bit clocks. For example, write 0 for the frame sync to assert for one bit clock only. The<br>sync width cannot be configured longer than the first word of the frame.|
|7-6<br>—|Reserved|
|5<br>CHMOD|Channel Mode<br>Configures if transmit data pins are configured for TDM mode or Output mode.<br>0b - TDM mode, transmit data pins are tri-stated when slots are masked or channels are disabled.<br>1b - Output mode, transmit data pins are never tri-stated and will output zero when slots are<br>masked or channels are disabled.|
|4<br>MF|MSB First<br>Configures whether the LSB or the MSB is transmitted first.<br>0b - LSB is transmitted first.<br>1b - MSB is transmitted first.|
|3|Frame Sync Early|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2915 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|FSE|0b - Frame sync asserts with the first bit of the frame.<br>1b - Frame sync asserts one bit before the first bit of the frame.|
|2<br>ONDEM|On Demand Mode<br>When set, and the frame sync is generated internally, a frame sync is only generated when the FIFO<br>warning flag is clear.<br>0b - Internal frame sync is generated continuously.<br>1b - Internal frame sync is generated when the FIFO warning flag is clear.|
|1<br>FSP|Frame Sync Polarity<br>Configures the polarity of the frame sync.<br>0b - Frame sync is active high.<br>1b - Frame sync is active low.|
|0<br>FSD|Frame Sync Direction<br>Configures the direction of the frame sync.<br>0b - Frame sync is generated externally in Slave mode.<br>1b - Frame sync is generated internally in Master mode.|



#### 73.5.1.9 Transmit Configuration 5 (TCR5) 

##### Offset 

|Register|Offset|
|---|---|
|TCR5|1Ch|



##### Function 

Contains transmit word width and bit index settings. 

~~<mark>NOTE</mark>~~ 

This register must not be altered when TCSR[TE] is set. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2916 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/073_Synchronous_Audio_Interface_-SAI-/S32K3XXRM_数据表.pdf-2917-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0<br>WNW  W0W<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>FBT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-29<br>—|Reserved|
|28-24<br>WNW|Word N Width<br>Configures the number of bits in each word, for each word except the first in the frame. The value written<br>must be one less than the number of bits per word. Word width of less than 8 bits is not supported.<br>Bit settings 0 – 6 (0b - 0_0110b) not supported.<br>0_0111b - 8 bits per word<br>0_1000b - 9 bits per word<br>0_1001b-1_1110b - (WNW value + 1) bits per word<br>1_1111b - 32 bits per word|
|23-21<br>—|Reserved|
|20-16<br>W0W|Word 0 Width<br>Configures the number of bits in the first word in each frame. The value written must be one less than the<br>number of bits in the first word. Word width of less than 8 bits is not supported if there is only one word<br>per frame.<br>Bit settings 0 – 6 (0b - 0_0110b) not supported.<br>0_0111b - 8 bits per word<br>0_1000b - 9 bits per word<br>0_1001b-1_1110b - (W0W value + 1) bits per word<br>1_1111b - 32 bits per word|
|15-13<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2917 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|12-8|First Bit Shifted|
|FBT|Configures the bit index for the first bit transmitted for each word in the frame. If configured for MSB First,<br>the index of the next bit transmitted is one less than the current bit transmitted. If configured for LSB First,<br>the index of the next bit transmitted is one more than the current bit transmitted. The value written must be<br>greater than or equal to the word width when configured for MSB First. The value written must be less than<br>or equal to 31-word width when configured for LSB First.<br>SeeData alignment.<br>0_0000b - Bit index is 0.<br>0_0001b-1_1110b - Bit index is FBT value.<br>1_1111b - Bit index is 31.|
|7-0<br>—|Reserved|



#### 73.5.1.10 Transmit Data (TDR0 - TDR3) 

##### Offset 

|Register|Offset|
|---|---|
|TDR0|20h|
|TDR1|24h|
|TDR2|28h|
|TDR3|2Ch|



##### Function 

Writes to this register when the transmit FIFO is not full will push the data written into the transmit data FIFO. Writes to this register when the transmit FIFO is full are ignored. 

~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

||Instance|Register supported|Register not supported|
|---|---|---|---|
|SAI_0||TDR0–TDR3|—|
|SAI_1||TDR0|TDR1–TDR3|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2918 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/073_Synchronous_Audio_Interface_-SAI-/S32K3XXRM_数据表.pdf-2919-01.png)


<!-- Start of picture text -->
Synchronous Audio Interface (SAI)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W TDR<br>Reset See Register reset values.<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>W TDR<br>Reset See Register reset values.<br><!-- End of picture text -->

##### Diagram 

##### Register reset values 

|Register|Reset value|
|---|---|
|TDR0|SAI_0,SAI_1: 0000_0000h|
|TDR1–TDR3|0000_0000h|



##### Fields 

|Field|Function|
|---|---|
|31-0|Transmit Data Register|
|TDR||



#### 73.5.1.11 Transmit FIFO (TFR0 - TFR3) 

##### Offset 

|Register|Offset|
|---|---|
|TFR0|40h|
|TFR1|44h|
|TFR2|48h|
|TFR3|4Ch|



##### Function 

The MSB of the read and write pointers is used to distinguish between FIFO full and empty conditions. If the read and write pointers are identical, then the FIFO is empty. If the read and write pointers are identical except for the MSB, then the FIFO is full. 

~~<mark>NOTE</mark>~~ 

Each module instance supports a different number of registers. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2919 / 4640 

NXP Semiconductors 

###### Synchronous Audio Interface (SAI) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/073_Synchronous_Audio_Interface_-SAI-/S32K3XXRM_数据表.pdf-2920-02.png)


<!-- Start of picture text -->
Instance Register supported Register not supported<br>SAI_0 TFR0–TFR3 —<br>SAI_1 TFR0 TFR1–TFR3<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R WCP  0 WFP<br>W<br>Reset See Register reset values.<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 RFP<br>W<br>Reset See Register reset values.<br><!-- End of picture text -->

##### Register reset values 

|Register|Reset value|
|---|---|
|TFR0|SAI_0,SAI_1: 0000_0000h|
|TFR1–TFR3|0000_0000h|



##### Fields 

|Field|Function|||
|---|---|---|---|
|31|Write Channel Pointer|||
|WCP|When FIFO Combine mode is en<br>written.|abled for writes, indicates that thi|s data channel is the next FIFO to be|
||This field is not suppor<br>supported registers.|ted in every instance. The following ta<br>~~NOTE~~|ble includes only|
||Instance|Field supported in|Field not supported in|
||SAI_0|TFR0–TFR3|—|
||SAI_1|—|TFR0|



0b - No effect. 

1b - FIFO combine is enabled for FIFO writes and this FIFO will be written on the next FIFO write. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2920 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|30-20<br>—|Reserved|
|19-16|Write FIFO Pointer|
|WFP|FIFO write pointer for transmit data channel.|
|15-4<br>—|Reserved|
|3-0|Read FIFO Pointer|
|RFP|FIFO read pointer for transmit data channel.|



#### 73.5.1.12 Transmit Mask (TMR) 

##### Offset 

|Register|Offset|
|---|---|
|TMR|60h|



##### Function 

This register is double-buffered and updates: 

1. When TCSR[TE] is first set 

2. At the end of each frame 

This allows the masked words in each frame to change from frame to frame. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||||0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||TW|M||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2921 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Fields 

|Field|Function|
|---|---|
|31-16|Reserved|
|—||
|15-0|Transmit Word Mask|
|TWM|Configures whether the transmit word is masked (transmit data pins are tri-stated or drive zero and<br>transmit data not read from FIFO) for the corresponding word in the frame.|
||0000_0000_0000_0000b - Word N is enabled.|
||0000_0000_0000_0001b - Word N is masked. The transmit data pins are tri-stated or drive zero<br>when masked.|



#### 73.5.1.13 Receive Control (RCSR) 

##### Offset 

|Register|Offset|
|---|---|
|RCSR|88h|



##### Function 

Contains receiver enable fields including resets, error and interrupt enable fields, and error flag fields. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/073_Synchronous_Audio_Interface_-SAI-/S32K3XXRM_数据表.pdf-2922-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0 0 WSF  SEF  FEF  FWF  FRF<br>Reserv<br>RE  DBGE  BCE  SR<br>W ed  FR  W1C W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 0<br>WSIE  SEIE  FEIE  FWIE  FRIE  FWDE  FRDE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Receiver Enable|
|RE|Enables/disables the receiver. When software clears this field, the receiver remains enabled, and this bit|
||remains set, until the end of the current frame.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2922 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Table continued from the previous page... 

|Field|Function<br>0b - Receiver is disabled.<br>1b - Receiver is enabled, or receiver has been disabled and has not yet reached end of frame.|
|---|---|
|30<br>—|Reserved Software should only write zero to this reserved bit.|
|29<br>DBGE|Debug Enable<br>Enables/disables receiver operation in Debug mode. The receive bit clock is not affected by Debug<br>mode.<br>0b - Receiver is disabled in Debug mode, after completing the current frame.<br>1b - Receiver is enabled in Debug mode.|
|28<br>BCE|Bit Clock Enable<br>Enables the receive bit clock, separately from RE. This field is automatically set whenever RE is set.<br>When software clears this field, the receive bit clock remains enabled, and this field remains set, until the<br>end of the current frame.<br>0b - Receive bit clock is disabled.<br>1b - Receive bit clock is enabled.|
|27-26<br>—|Reserved|
|25<br>FR|FIFO Reset<br>Empties the FIFO, and sets the FIFO read and write pointers to the same value, which may or may not be<br>zero. Reading this field will always return zero.<br>The FIFO reset is asserted for one cycle only.<br>~~NOTE~~<br>FIFO pointers should only be reset when the receiver is disabled or the FIFO error flag is set.<br>0b - No effect.<br>1b - FIFO reset.|
|24<br>SR|Software Reset<br>Resets the internal receiver logic including the FIFO pointers. Software-visible registers are not affected,<br>except for the status registers.<br>The software reset remains asserted until cleared by software. Software clears the bit by<br>writing 0.<br>~~NOTE~~|
||0b - No effect.<br>1b - Software reset.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2923 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|23-21<br>—|Reserved|
|20<br>WSF|Word Start Flag<br>Indicates that the start of the configured word has been detected. Write a logic 1 to this field to clear this<br>flag.<br>0b - Start of word not detected.<br>1b - Start of word detected.|
|19<br>SEF|Sync Error Flag<br>Indicates that an error in the externally-generated frame sync has been detected. Write a logic 1 to this<br>field to clear this flag.<br>0b - Sync error not detected.<br>1b - Frame sync error detected.|
|18<br>FEF|FIFO Error Flag<br>Indicates that an enabled receive FIFO has overflowed. Write a logic 1 to this field to clear this flag.<br>0b - Receive overflow not detected.<br>1b - Receive overflow detected.|
|17<br>FWF|FIFO Warning Flag<br>Indicates that an enabled receive FIFO is full.<br>0b - No enabled receive FIFO is full.<br>1b - Enabled receive FIFO is full.|
|16<br>FRF|FIFO Request Flag<br>Indicates that the number of words in an enabled receive channel FIFO is greater than the receive FIFO<br>watermark.<br>0b - Receive FIFO watermark not reached.<br>1b - Receive FIFO watermark has been reached.|
|15-13<br>—|Reserved|
|12|Word Start Interrupt Enable|
|WSIE|Enables/disables word start interrupts.<br>0b - Disables interrupt.<br>1b - Enables interrupt.|
|11|Sync Error Interrupt Enable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2924 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|SEIE|Enables/disables sync error interrupts.<br>0b - Disables interrupt.<br>1b - Enables interrupt.|
|10<br>FEIE|FIFO Error Interrupt Enable<br>Enables/disables FIFO error interrupts.<br>0b - Disables the interrupt.<br>1b - Enables the interrupt.|
|9<br>FWIE|FIFO Warning Interrupt Enable<br>Enables/disables FIFO warning interrupts.<br>0b - Disables the interrupt.<br>1b - Enables the interrupt.|
|8<br>FRIE|FIFO Request Interrupt Enable<br>Enables/disables FIFO request interrupts.<br>0b - Disables the interrupt.<br>1b - Enables the interrupt.|
|7-5<br>—|Reserved|
|4-2<br>—|Reserved|
|1<br>FWDE|FIFO Warning DMA Enable<br>Enables/disables DMA warnings.<br>0b - Disables the DMA warnings.<br>1b - Enables the DMA warnings.|
|0|FIFO Request DMA Enable|
|FRDE|Enables/disables DMA requests.<br>0b - Disables the DMA request.<br>1b - Enables the DMA request.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2925 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

#### 73.5.1.14 Receive Configuration 1 (RCR1) 

##### Offset 

|Register|Offset|
|---|---|
|RCR1|8Ch|



##### Function 

Configures the watermark level for all enabled receiver channels. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/073_Synchronous_Audio_Interface_-SAI-/S32K3XXRM_数据表.pdf-2926-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>RFW<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-3<br>—|Reserved|
|2-0|Receive FIFO Watermark|
|RFW|Number of 32-bit FIFO words|
||000b - 1 FIFO word|
||001b - 2 FIFO words|
||010b-110b - (RFW value + 1) FIFO words|
||111b - 8 FIFO words|



#### 73.5.1.15 Receive Configuration 2 (RCR2) 

##### Offset 

|Register|Offset|
|---|---|
|RCR2|90h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2926 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Function 

##### Contains the SYNC mode and clock setting fields. 

~~<mark>NOTE</mark>~~ 

This register must not be altered when RCSR[RE] is set. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/073_Synchronous_Audio_Interface_-SAI-/S32K3XXRM_数据表.pdf-2927-07.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R 0 0<br>SYNC  ed  BCI  MSEL  BCP  BCD  BYP<br>W 0<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>DIV<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Reserved|
|—||
|30|Synchronous Mode|
|SYNC|Configures between asynchronous and synchronous modes of operation. When configured for a<br>synchronous mode of operation, the transmitter must be configured for asynchronous operation.<br>0b - Asynchronous mode.<br>1b - Synchronous with transmitter.|
|29<br>—|Reserved|
|28<br>BCI|Bit Clock Input<br>When this field is set and using an internally generated bit clock in either synchronous or asynchronous<br>mode, the bit clock actually used by the receiver is delayed by the pad output delay (the receiver is clocked<br>by the pad input as if the clock was externally generated). This has the effect of decreasing the data input<br>setup time, but increasing the data output valid time.<br>The slave mode timing from the datasheet should be used for the receiver when this bit is set. In<br>synchronous mode, this bit allows the receiver to use the slave mode timing from the datasheet, while<br>the transmitter uses the master mode timing. This field has no effect when configured for an externally<br>generated bit clock .|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2927 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Table continued from the previous page... 

|Field|Function<br>When BCI=1 both the input buffer and output buffer must be enabled for the BCLK pad.<br>~~NOTE~~<br>0b - No effect.<br>1b - Internal logic is clocked as if bit clock was externally generated.|
|---|---|
|27-26<br>MSEL|MCLK Select<br>Selects the audio Master Clock option used to generate an internally generated bit clock. This field has<br>no effect when configured for an externally generated bit clock.<br>Depending on the device, some Master Clock options might not be available. See the<br>chip-specific information for the availability and chip-specific meaning of each option.<br>~~NOTE~~|
||00b - Bus Clock selected.<br>01b - Master Clock (MCLK) 1 option selected.<br>10b - Master Clock (MCLK) 2 option selected.<br>11b - Master Clock (MCLK) 3 option selected.|
|25<br>BCP|Bit Clock Polarity<br>Configures the polarity of the bit clock.<br>0b - Bit Clock is active high with drive outputs on rising edge and sample inputs on falling edge.<br>1b - Bit Clock is active low with drive outputs on falling edge and sample inputs on rising edge.|
|24<br>BCD|Bit Clock Direction<br>Configures the direction of the bit clock.<br>0b - Bit clock is generated externally in Slave mode.<br>1b - Bit clock is generated internally in Master mode.|
|23<br>BYP|Bit Clock Bypass<br>Bypasses the bit clock divider, internal bit clock is divide by 1 of the audio master clock.<br>0b - Internal bit clock is generated from bit clock divider.<br>1b - Internal bit clock is divide by one of the audio master clock.|
|22-8<br>—|Reserved|
|7-0|Bit Clock Divide|
|DIV|Divides down the audio master clock to generate the bit clock when configured for an internal bit clock.<br>The division value is (DIV + 1) * 2.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2928 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

#### 73.5.1.16 Receive Configuration 3 (RCR3) 

##### Offset 

|Register|Offset|
|---|---|
|RCR3|94h|



##### Function 

Contains the receive channel settings. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18<br>17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||0||||0<br>CFR||||0||||RCE||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2<br>1|0|
|R<br>W||||||0||||||||WDFL||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|0|



##### Fields 

|Field|Function|
|---|---|
|31-28|Reserved|
|—||
|27-24|Channel FIFO Reset|
|CFR|Resets the FIFO pointers for a specific channel. Reading this field will always return zero. FIFO pointers<br>should only be reset when a channel is disabled or the FIFO error flag is set.<br>The width of CFR field = the number of receive channels (call it N). For example, if CFR is 2 bits wide, then<br>bit position 24 refers to receive channel 1 FIFO pointer and bit position 25 refers to receive channel 2 FIFO<br>pointer. Setting bit 24 resets receive channel 1 FIFO pointer, and setting bit 25 enables receive channel 2<br>FIFO pointer. Setting bit N will reset receive channel N FIFO pointer.<br>0b - No effect.<br>1b - Receive data channel N FIFO is reset.|
||This field is not supported in every instance. The following table includes only<br>supported registers.<br>~~NOTE~~|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2929 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/073_Synchronous_Audio_Interface_-SAI-/S32K3XXRM_数据表.pdf-2930-03.png)


<!-- Start of picture text -->
Field Function<br>Instance Field supported in Field not supported in<br>SAI_0 RCR3 —<br>SAI_1 — RCR3<br>23-20 Reserved<br>—<br>19-16 Receive Channel Enable<br>RCE Enables the corresponding data channel for receive operation. Changing this field will take effect<br>immediately for generating the FIFO request and warning flags, but at the end of each frame for<br>receive operation.<br>The width of RCE field = the number of receive channels (call it N). For example, if RCE field is 2 bits wide,<br>then bit position 16 refers to receive channel 1 and bit position 17 refers to receive channel 2. Setting bit 16<br>enables receive channel 1, and setting bit 17 enables receive channel 2. Setting bit N will enable receive<br>channel N.<br>  NOTE<br>When there is only a single channel, there is no need for individual channel FIFO reset<br>(RCR3[CFR]). In the case of a single channel, use the global FIFO reset (RCSR[FR]).<br>0b - Receive data channel N is disabled.<br>1b - Receive data channel N is enabled.<br>  NOTE<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>Instance Field supported in Field not supported in<br>SAI_0 RCR3 —<br>SAI_1 RCR3[16] RCR3[19–17]<br>15-4 Reserved<br>—<br>3-0 Word Flag Configuration<br>WDFL Configures which word the start of word flag is set. The value written should be one less than the word<br>number (for example, write zero to configure for the first word in the frame). When configured to a value<br>greater than the Frame Size field, then the start of word flag is never set.<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2930 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0000b - Word 1|
||0001b - Word 2|
||0010b-1110b - Word (WDFL value + 1)|
||1111b - Word 16|



#### 73.5.1.17 Receive Configuration 4 (RCR4) 

##### Offset 

|Register|Offset|
|---|---|
|RCR4|98h|



##### Function 

Contains the receive fields for FIFO Combine Mode, FIFO Packing Mode, and frame sync settings. 

~~<mark>NOTE</mark>~~ This register must not be altered when RCSR[RE] is set. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/073_Synchronous_Audio_Interface_-SAI-/S32K3XXRM_数据表.pdf-2931-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 FCON 0<br>FCOMB  FPACK  FRSZ<br>T<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>Reserv ONDE<br>SYWD  MF  FSE  FSP  FSD<br>W ed  M<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-29<br>—|Reserved|
|28|FIFO Continue on Error|
|FCONT|Configures when the SAI will continue receiving after a FIFO error has been detected.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2931 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Table continued from the previous page... 

|Field|Function<br>0b - On FIFO error, the SAI will continue from the start of the next frame after the FIFO error flag<br>has been cleared.<br>1b - On FIFO error, the SAI will continue from the same word that caused the FIFO error to set<br>after the FIFO warning flag has been cleared.|
|---|---|
|27-26<br>FCOMB|FIFO Combine Mode<br>When FIFO combine mode is enabled for FIFO reads, software reading any FIFO data register will alternate<br>the read among the enabled data channel FIFOs. For example, if two data channels are enabled then the<br>first read will be performed to the first enabled data channel FIFO and the second read will be performed to<br>the second enabled data channel FIFO. Reseting the FIFO or disabling FIFO combine mode for FIFO reads<br>will reset the pointer back to the first enabled data channel.<br>When FIFO combine mode is enabled for FIFO writes from the receive shift registers, the first enabled data<br>channel input will alternate between the enabled data channel FIFOs. For example, if two data channels are<br>enabled, then the first unmasked received word will be stored in the first enabled data channel FIFO and<br>the second unmasked received word will be stored in the second enabled data channel FIFO. Since the first<br>word of the frame is always stored in the first enabled data channel FIFO, it is recommended that the number<br>of unmasked words per frame is evenly divisible by the number of enabled data channels.<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>~~NOTE~~|
||Instance<br>Field supported in<br>Field not supported in|
||SAI_0<br>RCR4<br>—|
||SAI_1<br>—<br>RCR4|
||00b - FIFO combine mode disabled.<br>01b - FIFO combine mode enabled on FIFO writes (from receive shift registers).<br>10b - FIFO combine mode enabled on FIFO reads (by software).<br>11b - FIFO combine mode enabled on FIFO writes (from receive shift registers) and reads (by<br>software).|
|25-24<br>FPACK|FIFO Packing Mode<br>Enables packing of 8-bit data or 16-bit data into each 32-bit FIFO word. If the word size is greater than 8-bit<br>or 16-bit then only the first 8-bit or 16-bits are stored to the FIFO. The first word in each frame always starts<br>with a new 32-bit FIFO word and the first bit shifted must be configured within the first packed word. When<br>FIFO packing is enabled, the FIFO read pointer will only increment when the full 32-bit FIFO word has been<br>read by software.<br>00b - FIFO packing is disabled<br>01b - Reserved.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2932 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||10b - 8-bit FIFO packing is enabled<br>11b - 16-bit FIFO packing is enabled|
|23-20<br>—|Reserved|
|19-16<br>FRSZ|Frame Size<br>Configures the number of words in each frame. The value written must be one less than the number of words<br>in the frame. For example, write 0 for one word per frame. The maximum supported frame size is 16 words.<br>0000b - 1 word per frame<br>0001b - 2 words per frame<br>0010b-1110b - (FRSZ value + 1) words per frame<br>1111b - 16 words per frame|
|15-13<br>—|Reserved|
|12-8<br>SYWD|Sync Width<br>Configures the length of the frame sync in number of bit clocks. The value written must be one less than<br>the number of bit clocks. For example, write 0 for the frame sync to assert for one bit clock only. The<br>sync width cannot be configured longer than the first word of the frame.<br>0_0000b - 1 bit clock<br>0_0001b - 2 bit clocks<br>0_0010b-1_1110b - (SYWD value + 1) bit clocks<br>1_1111b - 32 bit clocks|
|7-6|Reserved|
|—<br>5<br>—|Reserved Software should only write zero to this bit.|
|4|MSB First|
|MF|Configures whether the LSB or the MSB is received first.<br>0b - LSB is received first.<br>1b - MSB is received first.|
|3<br>FSE|Frame Sync Early<br>0b - Frame sync asserts with the first bit of the frame.<br>1b - Frame sync asserts one bit before the first bit of the frame.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2933 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|2|On Demand Mode|
|ONDEM|When set, and the frame sync is generated internally, a frame sync is only generated when the FIFO<br>warning flag is clear.<br>0b - Internal frame sync is generated continuously.<br>1b - Internal frame sync is generated when the FIFO warning flag is clear.|
|1<br>FSP|Frame Sync Polarity<br>Configures the polarity of the frame sync.<br>0b - Frame sync is active high.<br>1b - Frame sync is active low.|
|0|Frame Sync Direction|
|FSD|Configures the direction of the frame sync.<br>0b - Frame Sync is generated externally in Slave mode.|
||1b - Frame Sync is generated internally in Master mode.|



#### 73.5.1.18 Receive Configuration 5 (RCR5) 

##### Offset 

|Register|Offset|
|---|---|
|RCR5|9Ch|



##### Function 

Contains receive word and bit index settings. 

~~<mark>NOTE</mark>~~ This register must not be altered when RCSR[RE] is set. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||0||||WNW||||0||||W0W|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||0||||FBT||||||0|||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2934 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Fields 

|Field<br>31-29<br>—|Function<br>Reserved|
|---|---|
|28-24<br>WNW|Word N Width<br>Configures the number of bits in each word, for each word except the first in the frame. The value written<br>must be one less than the number of bits per word. Word width of less than 8 bits is not supported.<br>Bit settings 0 – 6 (0b - 0_0110b) not supported.<br>0_0111b - 8 bits per word<br>0_1000b - 9 bits per word<br>0_1001b-1_1110b - (WNW value + 1) bits per word<br>1_1111b - 32 bits per word|
|23-21<br>—|Reserved|
|20-16<br>W0W|Word 0 Width<br>Configures the number of bits in the first word in each frame. The value written must be one less than the<br>number of bits in the first word. Word width of less than 8 bits is not supported if there is only one word<br>per frame.<br>0_0000b - 1 bit per word<br>0_0001b - 2 bits per word<br>0_0010b-1_1110b - (W0W value + 1) bits per word<br>1_1111b - 32 bits per word|
|15-13<br>—|Reserved|
|12-8<br>FBT|First Bit Shifted<br>Configures the bit index for the first bit received for each word in the frame. If configured for MSB First, the<br>index of the next bit received is one less than the current bit received. If configured for LSB First, the index<br>of the next bit received is one more than the current bit received. The value written must be greater than<br>or equal to the word width when configured for MSB First. The value written must be less than or equal to<br>31-word width when configured for LSB First.<br>SeeData alignment.<br>0_0000b - Bit index is 0.<br>0_0001b-1_1110b - Bit index is FBT value.<br>1_1111b - Bit index is 31.|
|7-0<br>—|Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2935 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

#### 73.5.1.19 Receive Data (RDR0 - RDR3) 

##### Offset 

|Register|Offset|
|---|---|
|RDR0|A0h|
|RDR1|A4h|
|RDR2|A8h|
|RDR3|ACh|



##### Function 

Reads from this register when the receive FIFO is not empty return the data from the top of the receive FIFO. Reads from this register when the receive FIFO is empty are ignored. 

~~<mark>NOTE</mark>~~ Each module instance supports a different number of registers. 

||Instance|Register supported|Register not supported|
|---|---|---|---|
|SAI_0||RDR0–RDR3|—|
|SAI_1||RDR0|RDR1–RDR3|



##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/073_Synchronous_Audio_Interface_-SAI-/S32K3XXRM_数据表.pdf-2936-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R RDR<br>W<br>Reset See Register reset values.<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RDR<br>W<br>Reset See Register reset values.<br><!-- End of picture text -->

##### Register reset values 

|Register|Reset value|
|---|---|
|RDR0|SAI_0,SAI_1: 0000_0000h|
|RDR1–RDR3|0000_0000h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2936 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Fields 

|Field|Function|
|---|---|
|31-0|Receive Data Register|
|RDR||



#### 73.5.1.20 Receive FIFO (RFR0 - RFR3) 

##### Offset 

|Register|Offset|
|---|---|
|RFR0|C0h|
|RFR1|C4h|
|RFR2|C8h|
|RFR3|CCh|



##### Function 

The MSB of the read and write pointers is used to distinguish between FIFO full and empty conditions. If the read and write pointers are identical, then the FIFO is empty. If the read and write pointers are identical except for the MSB, then the FIFO is full. 

~~<mark>NOTE</mark>~~ Each module instance supports a different number of registers. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/073_Synchronous_Audio_Interface_-SAI-/S32K3XXRM_数据表.pdf-2937-10.png)


<!-- Start of picture text -->
Instance Register supported Register not supported<br>SAI_0 RFR0–RFR3 —<br>SAI_1 RFR0 RFR1–RFR3<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 WFP<br>W<br>Reset See Register reset values.<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R RCP  0 RFP<br>W<br>Reset See Register reset values.<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2937 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Register reset values 

|Register|Reset value|
|---|---|
|RFR0|SAI_0,SAI_1: 0000_0000h|
|RFR1–RFR3|0000_0000h|



##### Fields 

|Field|Function|
|---|---|
|31-20|Reserved|
|—||
|19-16|Write FIFO Pointer|
|WFP|FIFO write pointer for receive data channel.|
|15|Receive Channel Pointer|
|RCP|When FIFO Combine mode is enabled for reads, indicates that this data channel is the next FIFO to be<br>read.<br>This field is not supported in every instance. The following table includes only<br>supported registers.<br>~~NOTE~~|
||Instance<br>Field supported in<br>Field not supported in|
||SAI_0<br>RFR0–RFR3<br>—|
||SAI_1<br>—<br>RFR0|
||0b - No effect.<br>1b - FIFO combine is enabled for FIFO reads and this FIFO will be read on the next FIFO read.|
|14-4<br>—|Reserved|
|3-0|Read FIFO Pointer|
|RFP|FIFO read pointer for receive data channel.|



#### 73.5.1.21 Receive Mask (RMR) 

##### Offset 

|Register|Offset|
|---|---|
|RMR|E0h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2938 / 4640 

NXP Semiconductors 

Synchronous Audio Interface (SAI) 

##### Function 

This register is double-buffered and updates: 

1. When RCSR[RE] is first set 

2. At the end of each frame 

This allows the masked words in each frame to change from frame to frame. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|||||||||0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||R|WM||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-16|Reserved|
|—||
|15-0|Receive Word Mask|
|RWM|Configures whether the receive word is masked (received data ignored and not written to receive FIFO)<br>for the corresponding word in the frame.|
||0000_0000_0000_0000b - Word N is enabled.|
||0000_0000_0000_0001b - Word N is masked.|



## 73.6 Glossary 

FIFO First-in first-out LSB Least significant bit MSB Most significant bit 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2939 / 4640 

