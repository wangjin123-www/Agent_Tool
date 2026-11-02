NXP Semiconductors 

# Chapter 78 Ultra Secured Digital Host Controller (uSDHC) 

## 78.1 Chip-specific uSDHC information 

### 78.1.1 uSDHC instances and configuration 

This chip supports up to one instance of uSDHC module. 

Table 676. uSDHC instances 

|Instance|S32K358|S32K3x2/ S32K3x4/ S32K3x1|
|---|---|---|
|uSDHC|Yes|No|



Table 677. Features supported 

|Features|Notes|
|---|---|
|MMC|• System specification version 4.2/4.3/4.4/4.41/4.5/5.0/5.1<br>• Bit Widths x1/x4/x8<br>• Full Speed Mode upto 25MHz<br>• High Speed SDR upto 50MHz<br>• High Speed DDR mode (50MHz both edges)|
|SD/ SDIO|• Card Specification version 2.0/3.0<br>• Bit Widths x1/x4<br>• Full Speed Mode upto 25MHz<br>• High Speed Mode upto 50MHz|
|FIFO|128 x 32 external FIFO supported|
|External DMA|Supported|
|Write Protect WP system implementation|Supported|
|Voltage support|3.3 V|



~~<mark>NOTE</mark>~~ 

Card clock pin should have weak pull down enabled when configured for uSDHC function. 

This chip doesn’t support the following features: 

- MMC HS400 MODE 

- Card Detection (CD) System Implementation 

- LED control (LCTL) output signal 

- IO power Voltage selection Signal (VSELECT) 

- Input clock for eMMC HS400 mode (STROBE) 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4430 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4431-02.png)


Figure 483. System connection of uSDHC 

## 78.2 Overview 

The Ultra Secured Digital Host Controller (uSDHC) provides the interface between the host system and the eMMC, SD card, and SDIO card as shown in Figure 485. The module acts as a bridge, passing host bus transactions to the eMMC, SD card, and SDIO card by sending commands and performing data accesses to/from the cards. It handles the SD card/SDIO card/eMMC protocols at the transmission level. 

### 78.2.1 Block diagram 

The following figure illustrates the block diagram for uSDHC. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4431 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4432-02.png)


<!-- Start of picture text -->
CMD<br>hclk<br>Dual port channel CRCCRC<br>ipg_clk SRAM CTRL CMD<br>Async fifo<br>Sync TX buffer<br>Register<br>IPS bus  bank buffer Data channel<br>controller CTRL CRC DATAn<br>RX b u ffer<br>SD-CLK Control<br>AHB master port DMA DLL<br>CLK<br>CD_B<br>IRQ Interrupt WP<br>generator MISC<br>ipg_clk_perclk Clock divider<br>RESET_B<br><!-- End of picture text -->

Figure 484. uSDHC block diagram 

The figure below shows the System connection of uSDHC: 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4432-05.png)


<!-- Start of picture text -->
eMMC/SD/SDIO<br>eMMC<br>Host controller<br>SD card<br>Transceiver<br>Card SDIO card<br>DMA interface IP bus slot<br>Power supply<br>AHB bus IP bus<br><!-- End of picture text -->

Figure 485. System connection of uSDHC 

The following are brief descriptions of the cards supported by uSDHC: 

- The Embedded MultiMediaCard (eMMC) is a universal low-cost data storage and communication media designed to cover a wide array of applications including mobile video and gaming. Previous eMMC were based on a 7-pin serial bus with a single data pin, while the new high speed eMMC communication is based on an advanced 11-pin serial bus designed to operate in the low-voltage range. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4432 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

- The Secure Digital Card (SD) is an evolution of the old eMMC technology. It is specifically designed to meet the security, capacity, performance, and environmental requirements inherent in newly emerging audio and video consumer electronic devices. The physical form factor, pin assignment, and data transfer protocol are backward compatible with the old eMMC (with some additions). 

- Under the SD protocol, system connection can be categorized into memory card, I/O card, and combo card, which have both memory and I/O functions. The memory card invokes a copyright protection mechanism that complies with the security of the SDMI standard. The I/O card, which is also known as SDIO card, provides high-speed data I/O with low-power consumption for mobile electronic devices. 

### 78.2.2 Features 

The list given below shows the features of the uSDHC module: 

- Conforms to the SD Host Controller Standard Specification version 2.0 

- Compatible with the eMMC System Specification version 4.2/4.3/4.4/4.41 

- Compatible with the SD Memory Card Specification version 3.0 and supports the Extended Capacity SD Memory Card 

- Compatible with the SDIO Card Specification version 2.0 

- Designed to work with SD Memory, miniSD Memory, SDIO, miniSDIO, SD Combo, eMMC, eMMC plus, and eMMC RS cards 

- Card bus clock frequency up to 104 MHz 

- Supports 1-bit/4-bit SD and SDIO modes, and 1-bit/4-bit/8-bit eMMC modes 

   - Up to 200 Mbps of data transfer for SDIO cards using four parallel data lines in the Single Data Rate (SDR) mode 

   - Up to 400 Mbps of data transfer for SDIO card using four parallel data lines in the Dual Data Rate (DDR) mode 

   - Up to 200 Mbps of data transfer for SDXC cards using four parallel data lines in the Single Data Rate (SDR) mode 

   - Up to 400 Mbps of data transfer for SDXC card using four parallel data lines in the Dual Data Rate (DDR) mode 

   - Up to 416 Mbps of data transfer for eMMC using eight parallel data lines in the Single Data Rate (SDR) mode 

   - Up to 832 Mbps of data transfer for eMMC using eight parallel data lines in the Dual Data Rate (DDR) mode 

- Supports single block/multi-block read and write 

- Supports block sizes of 1 ~ 4096 bytes 

- Supports the write protection switch for write operations 

- Supports both synchronous and asynchronous abort 

- Supports pause during the data transfer at block gap 

- Supports SDIO Read Wait and Suspend Resume operations 

- Supports Auto CMD12 for multi-block transfer 

- Host can initiate non-data transfer command while data transfer is in progress 

- Allows cards to interrupt the host in 1-bit and 4-bit SDIO modes; also supports interrupt period 

- Embodies a fully configurable 128x32-bit FIFO for read/write data 

- Supports internal and external DMA capabilities 

- Supports voltage selection by configuring vendor-specific register bit 

- Supports Advanced DMA to perform linked memory access 

~~<mark>NOTE</mark>~~ 

This block can support all the above-listed speed mode and maximum data throughput. However, these may be specific to the device. See the corresponding chip-specific information or the device data sheet for accurate details. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4433 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

## 78.3 Functional description 

The following sections provide a brief functional description of the major system blocks, including the data buffer, DMA AHB interface, register bank as well as IP Bus interface, dual-port memory wrapper, data/command controller, clock and reset manager, and clock generator. 

### 78.3.1 Modes and operations 

#### 78.3.1.1 Data transfer modes 

The uSDHC module can select the following modes for data transfer: 

- SD 1-bit 

- SD 4-bit 

- eMMC 1-bit 

- eMMC 4-bit 

- eMMC 8-bit 

- Identification mode (up to 400 kHz) 

- eMMC full-speed mode (up to 26 MHz) 

- eMMC high-speed mode (up to 52 MHz) 

- eMMC DDR mode (52 MHz both edges) 

- SD or SDIO cards full-speed mode (up to 25 MHz) 

- SD or SDIO cards high-speed mode (up to 50 MHz) 

~~<mark>NOTE</mark>~~ 

This block can support all the above listed speed mode and maximum clock frequency. However, these may be specific to the device. See the corresponding chip-specific information or the device data sheet for accurate details. 

### 78.3.2 Data buffer 

The uSDHC module uses one configurable data buffer to transfer data between the system bus (IP bus or advanced high-performance bus (AHB) bus) and the SD card in an optimized manner, maximizing throughput between the two clock domains (IP peripheral clock and the master clock). The buffer is used as a temporary storage for transferring data between the host system and the card. The watermark levels for read and write are both configurable and can range between 1 to 128 words. The burst lengths for read and write are also configurable and can range between 1 to 31 words. The next figure provides the uSDHC buffer scheme as buffer control and buffer RAM wrapper. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4434-22.png)


<!-- Start of picture text -->
dma_req<br>uSDHC registers Status sync<br>uSDHC_irq<br>IP bus<br>I/F<br>Buffer control SD bus<br>TX/RX I/F<br>FIFO<br>Buffer<br>AHB Internal RAM Sync<br>bus DMA FIFOs<br>wrapper<br><!-- End of picture text -->

Figure 486. uSDHC buffer scheme 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4434 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

Here are 3 transfer modes to access the data buffer: 

- CPU polling mode: 

   - For a host-read operation, when the number of words received in the buffer meets or exceeds the RD_WML watermark value, by polling the BRR bit, the host driver can read the Buffer Data Port register to fetch the amount of words set in the RD_WML register from the buffer. The write operation is similar. For more information on the process of writing operation, see Write operation sequence. 

- External DMA mode: 

   - For a read operation, when there are more words received in the buffer than the amount set in WTMK_LVL[RD_WML], a DMA request is sent out to inform the external DMA to fetch the data. The request will be immediately de-asserted when there is an access on the Data Buffer Access Port (DATA_BUFF_ACC_PORT). If the number of words in the buffer after the current burst meets or exceeds RD_WML value, the DMA request is asserted again. For instance, if there are twice as many words in the buffer as there are in the RD_WML value, there are two successive DMA requests with only one cycle of de-assertion between. The write operation is similar. Note the accesses CPU polling mode and external DMA mode both use the IP bus, and if the external DMA is enabled, in both modes an external DMA request is sent when the buffer is ready. 

- Internal DMA mode (includes simple and advanced DMA accesses): 

   - The internal DMA access, either by simple or advanced DMA, is over the AHB bus. For internal DMA access mode, the external DMA request will never be sent out. 

For a read operation, when there are more words in the buffer than the amount set in WTMK_LVL[RD_WML], the internal DMA starts fetching data over the AHB bus. Except for INCR4 and INCR8, the burst type is always the INCR mode and the burst length depends on the shortest of the following factors: 

- Burst length configured in the burst length field of the Watermark Level register 

- Watermark level boundary 

- Block size boundary 

- Data boundary configured in the current descriptor (if the ADMA is active) 

- 1 KB address boundary defined in the AHB protocol 

The Write operation functions in a similar manner—sequential and contiguous access is necessary to ensure that the pointer address value is correct. Random or skipped access is not possible. The byte order, by reset, is little endian mode. The actual byte order is swapped inside the buffer, according to the endian mode configured by software (see the following figures). For a host write operation, the byte order is swapped after the data is fetched from the buffer and ready to send to the SD Bus. For a host read operation, the byte order is swapped before the data is stored in the buffer. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4435-16.png)


<!-- Start of picture text -->
System IP bus or system AHB bus 31-24 23-16 15-8 7-0<br>uSDHC data buffer 7-0 15-8 23-16 31-24<br><!-- End of picture text -->

Figure 487. Data swap between system bus and uSDHC data buffer in the byte little endian mode 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4435-18.png)


<!-- Start of picture text -->
System IP bus or system AHB bus 15-8 7-0 31-24 23-16<br>uSDHC data buffer 7-0 15-8 23-16 31-24<br><!-- End of picture text -->

Figure 488. Data swap between system bus and uSDHC data buffer in half word big endian mode 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4435 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

#### 78.3.2.1 Write operation sequence 

There are 3 ways to write data into the buffer when the user transfers data to the card: 

- External DMA through the uSDHC DMA request signal 

- Processor core polling through the BWR bit in the Interrupt Status register (interrupt or polling) 

- Internal DMA 

When the internal DMA is not used, the DMAEN bit in the Transfer Type register is not set when the command is sent, uSDHC asserts a DMA request when the amount of buffer space exceeds the value set in WTMK_LVL[WR_WML] and is ready for receiving new data. At the same time, uSDHC sets the BWR bit. The buffer write ready interrupt is generated if it is enabled by software. 

When internal DMA is used, uSDHC does not inform the system before all the required number of bytes are transferred (if no error is encountered). When an error occurs during the data transfer, uSDHC aborts the data transfer and abandons the current block. The host driver should read the contents of the DMA System Address register to obtain the starting address of the abandoned data block. If the current data transfer is in multi-block mode, uSDHC does not automatically send CMD12, even though the AC12EN bit in the Transfer Type register is set. The host driver sends CMD12 in this scenario and restarts the write operation from that address. It is recommended that a software reset for Data be applied before the transfer is restarted. 

The uSDHC module does not start data transmission until the buffer has been filled with the number of words set in the WR_WML register. If the buffer is empty and the host system does not write data in time, uSDHC stops the CLK to avoid the data buffer underrun situation. 

#### 78.3.2.2 Read operation sequence 

There are 3 ways to read data from the buffer when the data is received from the card: 

- External DMA through uSDHC DMA request signal 

- Processor core polling through the BRR bit in the Interrupt Status register (interrupt or polling) 

- Internal DMA 

When internal DMA is not used (DMAEN bit in Transfer Type register is not set when the command is sent), uSDHC asserts a DMA request when the amount of data exceeds the value set in the RD_WML register, which is available and ready for system fetching data. At the same time, uSDHC sets the BRR bit. The buffer read ready interrupt is generated if it is enabled by the software. 

When internal DMA is used, uSDHC does not inform the system before all the required number of bytes are transferred (if no error is encountered). When an error occurs during the data transfer, uSDHC aborts the data transfer and abandons the current block. The host driver should read the content of the DMA System Address register to get the starting address of the abandoned data block. If the current data transfer is in multi-block mode, uSDHC does not automatically send CMD12, even though the AC12EN bit in the Transfer Type register is set. The host driver sends CMD12 in this scenario and restarts the read operation from that address. It is recommended that a software reset (in register RSTD) for data be applied before the transfer is restarted. 

For any read transfer mode, uSDHC does not start data transmission until the number of words set in the RD_WML register are in buffer. If the buffer is full and the host system does not read data in time, uSDHC stops the CLK to avoid the data buffer overrun situation. 

#### 78.3.2.3 Data buffer and block size 

In the uSDHC module, the data buffer can hold up to 128 words (32-bit) and the watermark levels for write and read can be configured accordingly. The user needs to know the buffer size for the buffer operation during a data transfer to utilize it in the most optimized way. For both read and write, the watermark level can range between 1 to 128 words. For both read and write, the burst length can range between from 1 to 31 words. The host driver may configure the value according to the system and requirement. 

During a multi-block data transfer, the block length can be set to any value between 1 and 4096 bytes, satisfying the requirements of the external card. The only restriction is from the external card, which can be limited in size or support of a partial block access (which is not the integer times of 512 bytes). 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4436 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

As uSDHC treats each block individually, for block sizes which are not multiples of four (not word-aligned), stuffed bytes are required at the end of each block. For example, if the block size is 7 bytes and there are 12 blocks to write, the software side must write twice for each block. For each block, the ending byte is abandoned by uSDHC because it only sends 7 bytes to the card and picks data from the following system write, resulting in 24 beats of write access in total. 

#### 78.3.2.4 Dividing large data transfer 

This SDIO command CMD53 definition limits the maximum data size of data transfers according to the following formula: 

Max data size = Block size x Block count 

The length of a multiple block transfer needs to be in multiples of block size. If the total data length cannot be divided evenly into a multiple of the block size, then there are two options to transfer the data. These two options depend on the function and the card design. Option 1 is for the host driver to split the transaction. The remainder of the block size data is then transferred by using a single block command at the end. Option 2 is to add dummy data in the last block to fill the block size. For option 2, the card must manage the removal of the dummy data. 

See the figure below for an example showing the division of large data transfers, assuming a kind of WLAN SDIO card that only supports a block size of up to 64 bytes. Although uSDHC supports a block size of up to 4096 bytes, the SDIO can only accept a block size of less than 64 bytes, so the data must be divided (see the example below). 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4437-08.png)


<!-- Start of picture text -->
544 Bytes WLAN Frame<br>802.11<br>MAC Header IV Frame Body ICV FCS<br>WLAN Frame is divided equally into 64 byte blocks plus the remainder 32 bytes<br>64 bytesData 64 bytesData ----- 64 bytesData 32 bytesData<br>SDIO Datablock #1 SDIO Datablock #2 ----- SDIO Datablock #8 SDIO Data32 bytes<br>Eight 64 byte blocks are sent in Block Transfer mode and the<br>remainder 32 bytes are sent in Byte Transfer mode<br>CMD 53 SDIO Data SDIO Data ----- SDIO Data CMD 53 SDIO Data<br>block #1 block #2 block #8 32 bytes<br><!-- End of picture text -->

Figure 489. Example for dividing large data transfers 

#### 78.3.2.5 External DMA request 

When the internal DMA is not in use and external DMA is enabled, the Data Buffer will generate a DMA request to the system. During a write operation, when the number of WR_WML words can be held in the buffer free space, the signal uSDHC_dreq_b is asserted to 0, informing the Host System of a DMA write. 

The BWR bit in the Interrupt Status register is also set, as long as the BWRSEN bit in the Interrupt Status Enable register is set. The DMA request is de-asserted after several accesses to the Data Buffer Access Port (DATA_BUFF_ACC_PORT) are made while the buffer's free space can't meet the watermark condition (free space> write watermark level). 

On read operation, when the number of RD_WML words are already in the buffer, the signal uSDHC_dreq_b is asserted to 0, informing the Host System for a DMA read. The BRR bit in the Interrupt Status register is also set, as long as the BRRSEN bit in 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4437 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

the Interrupt Status Enable register is set. The DMA request is de-asserted after several accesses to the Data Port register are made while the buffer's data can't meet the watermark condition (the number of data in buffer > read watermark level). 

If the DMA burst length can't change during a data transfer for an external DMA transfer, the watermark level (read or write) must be a divisor of the block size. If it is not, transferring the block may cause buffer under-run (read operation) or over-run (write operation). For example, if the block size is 512 bytes, the watermark level of read (or write) must be a power of two between 1 and 128. For processor core polling access there is no such issue, as the last access in the block transfer can be controlled by software. The watermark level can be any value, even larger than the block size (but no greater than 128 words) because the actual number of bytes transferred by the software can be controlled and does not exceed the block size in each transfer. 

The uSDHC also supports non-word aligned block size, as long as the card supports that block size. In this case, the watermark level should be set as the number of words. For example, if the block size is 31 bytes, the watermark level can be set to any number of words. For this case, the BLK_ATT[BLKSIZE] will be set as 1fh. For the CPU polling access, the burst length can be 1 to 128 words, without restriction. This is because the software will transfer 8 words, and the uSDHC will also set the BWR or BRR bits when the remaining data does not violate data buffer. See DMA burst length for more details about the dynamic watermark level of the data buffer. 

For the above example, even though 8 words are transferred via Data Buffer Access Port (DATA_BUFF_ACC_PORT), the uSDHC will transfer only 31 bytes over the SD Bus, as required by the BLK_ATT[BLKSIZE] fields. In this data transfer, with non-word aligned block size, the endian mode should be set cautiously or invalid data will be transferred to and from the card. 

### 78.3.3 DMA AHB interface 

The internal DMA implements a DMA engine and the AHB master. When the internal DMA is enabled, but the BWR and BRR bits are set if the BWRSEN and BRRSEN bits have been set in the Interrupt Status Enable register. See the figure below for an illustration of the DMA AHB interface block. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4438-08.png)


<!-- Start of picture text -->
AHB System Address<br>Interface<br>uSDHC Registers<br>R/W Indication<br>Master<br>Logic<br>Error Indication<br>AHB signal<br>cluster<br>Burst Length<br>DMA Buffer Control<br>Engine Data Exchange<br>DMA Request<br><!-- End of picture text -->

Figure 490. DMA AHB interface block 

#### 78.3.3.1 Internal DMA request 

If the watermark level requirement is met in data transfer or if the last data of current block is ready in the data buffer, and the Internal DMA is enabled, the data buffer block sends a DMA request to AHB interface. Meanwhile, the external DMA request signal (uSDHC_dreq_b) is disabled. 

The delay in response from the internal DMA engine depends on the system AHB bus loading and the priority assigned to uSDHC. The DMA engine does not respond to the request during its burst transfer, but is ready to serve as soon as the burst is over. The data buffer de-asserts the request if the data buffer space (for write) or bytes in data buffer is smaller than the watermark level. Upon access to the buffer by internal DMA, the data buffer updates its internal buffer pointer, and when the watermark level is satisfied or the last data of the current block is ready in the data buffer, another DMA request is sent. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4438 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

The data transfer is in the block unit, and the subsequent watermark level is always automatically set as the remaining number of words. For instance, for a multi block data read with each block size of 31 bytes, and the burst length set to six words (24 bytes). After the first burst transfer, if there are greater than or equal to two words in the buffer, which might contain some data of the next block), another DMA request is sent. This is because the remaining number of words to transfer for the current block is ceiling((31 - 6 * 4) / 4) = 2. The uSDHC module reads two words out of the buffer, with seven valid bytes and one stuffed byte. 

#### 78.3.3.2 DMA burst length 

Just like a CPU polling access, the DMA burst length for the internal DMA engine can range between 1 to 16 words. The actual burst length for the DMA depends on the lesser of the configured burst length or the remaining words of the current block. See the example in Internal DMA request. After six words are read, the burst length is two words, then the next burst length is six words. This is because the next block starts, which is 31 bytes, more than six words. The host driver may take this variable burst length into account. It is also acceptable to configure the burst length as the divisor of the block size, so that each time the burst length is the same. 

#### 78.3.3.3 AHB master interface 

It is possible that the internal AHB DMA engine could fail during the data transfer. Upon detection of an AHB bus error during DMA transfer, the DMA engine stops the transfer and goes to the idle state. At that point, the internal data buffer stops receiving incoming data and sending out data. The DMAE bit in the Interrupt Status register is generated to host CPU to report a bus error condition. 

After the DMAE interrupt is received, the software sends a CMD12 to abort the current transfer and read the DS_ADDR bits of the DMA System Address register to get the starting address of the corrupted block. After the DMA error is fixed, the software should apply a data reset and restart the transfer from this address to recover the corrupted block. 

#### 78.3.3.4 ADMA engine 

In the SD host controller standard, a new DMA transfer algorithm called the Advanced DMA (ADMA) is defined. For simple DMA, after the page boundary is reached, a DMA interrupt is generated and the new system address is programmed by the host driver. The ADMA defines the programmable descriptor table in the system memory. The host driver can calculate the system address at the page boundary and program the descriptor table before executing ADMA. It reduces the frequency of interrupts to the host system. Therefore, higher speed DMA transfers could be realized because the host MCU intervention is not be needed during long DMA-based data transfers. 

There are two types of ADMA in host controller: ADMA1 and ADMA2. ADMA1 can support data transfer of 4KB aligned data in system memory, and ADMA2 eliminates the restriction so that the data of any location and any size can be transferred in system memory. Their formats of Descriptor Table are different. 

ADMA can recognize all kinds of descriptors defined in SD host controller Standard, and if the "End" flag is detected in the descriptor, ADMA stops after this descriptor is processed. 

#### 78.3.3.4.1 ADMA concept and descriptor format 

ADMA1 includes the following descriptors: 

- Valid/invalid descriptor 

- Nop descriptor 

- Set data length descriptor 

- Set data address descriptor 

- Link descriptor 

- Interrupt flag and end flag in descriptor 

ADMA2 includes the following descriptors: 

- Valid/invalid descriptor 

- Nop descriptor 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4439 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

- Rsv descriptor (new in ADMA2) 

- Set data length and address descriptor 

- Link descriptor 

- Interrupt flag and end flag in descriptor 

ADMA starts read/write operation after it reaches the tran state, using the data length and data address analyzed from most recent descriptor(s). 

For ADMA1, the valid data length descriptor is the last set type descriptor before the tran type descriptor. Every tran type descriptor triggers a transfer, and the transfer data length is extracted from the most recent set type descriptor. If there is no set type descriptor after the previous Trans descriptor, the data length is the value for previous transfer, or 0 if no set descriptor is ever met. 

For ADMA2, the tran type descriptor contains both data length and transfer data address, so the tran type descriptor itself can start a data transfer. 

See the figure below for the format of the descriptor table for ADMA1. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4440-10.png)


<!-- Start of picture text -->
Address/ Page Field      Address/ Page Field      Attribute Field<br>31  12 11 6 5 4 3 2 1 0<br>Address or Data Length      000000      Act 2    Act 1    0 Int  End   Valid<br>Act 2      Act1    Symbol      Comment      31- 28     27- 12<br>0 0 Nop   No Operation      Don't Care<br>0 1 Set   Set Data Length      0000    Data Length<br>1 0 Tran      Transfer Data      Data Address<br>1 1 Link   Link Descriptor      Descriptor Address<br>Valid    Valid = 1 indicates this line of descriptor is effective. If Valid = 0 generate ADMA Error Interrupt and stop ADMA.<br>End   End = 1 indicates current descriptor is the ending one.<br>Int  Int = 1 generates DMA Interrupt when this descriptor is processed.<br><!-- End of picture text -->

Figure 491. Format of the ADMA1 descriptor table 

See the figure below for the concept and access method of the descriptor table for ADMA1. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4440 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4441-02.png)


<!-- Start of picture text -->
System Address Register points to<br>the head node of Descriptor Table<br>Advanced DMA System Memory<br>Descriptor Table<br>Address/Length Attribute<br>System Address Register<br>Address Tran<br>Address Link<br>Data Length (internal)<br>Address/Length Attribute<br>Data Length Set<br>Data Address (internal)<br>Addr es s Tran, End<br>DMA Interrupt<br>Page Data<br>Flags<br>SDMA Transfer Complete<br>State<br>Page Data<br>Machine Block Gap Event<br><!-- End of picture text -->

Figure 492. Concept and access method of the ADMA1 descriptor table 

The figure below explains the ADMA2 format. ADMA2 deals with the lower 32-bit first, and then the higher 32-bit. If the 'Valid' flag of descriptor is 0, it ignores the higher 32-bit. The Address field should be set to word aligned (lower 2-bit is always set to 0). Data length is in byte unit. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4441 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4442-02.png)


<!-- Start of picture text -->
Address Field      Length      Reserved      Attribute Field<br>63  32 31 16 15  06  05  04  03  02  01  00<br>32-bit Address      16-bit length      0000000000      Act 2    Act 1    0 Int  End   Valid<br>Act 2      Act1    Symbol      Comment      Operation<br>0 0 Nop   No Operation      Don't Care<br>0 1 Rsv   Reserved      Same as Nop. Read this line and go to next one<br>1 0 Tran      Transfer Data      Transfer data with address and length<br>set in this descriptor line<br>1 1 Link   Link Descriptor      Link to another descriptor<br>Valid    Valid = 1 indicates this line of descriptor is effective. If Valid = 0 generate ADMA Error Interrupt and stop ADMA.<br>End   End = 1 indicates current descriptor is the ending one.<br>Int  Int = 1 generates DMA Interrupt when this descriptor is processed.<br><!-- End of picture text -->

Figure 493. Format of the ADMA2 descriptor table 

See the figure below for the concept and access method of the descriptor table for ADMA2. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4442 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4443-02.png)


<!-- Start of picture text -->
System Address Register points to<br>the head node of Descriptor Table<br>Advanced DMA System Memory<br>Descriptor Table<br>Address Length Attribute<br>System Address Register<br>Address1 Length1 Tran<br>Address2 Length2 Tran<br>Data Length (internal)<br>Address - Link<br>Address Length Attribute<br>Data Address (internal)<br>Address3 Length3 Tran<br>Address4 Length4 Tran, End<br>DMA Interrupt<br>Flags<br>SDMA Transfer Complete<br>State<br>Machine<br>ADMA Error<br>Data 4<br>Data 3<br>Data 2<br>Data 1<br><!-- End of picture text -->

Figure 494. Concept and access method of the ADMA2 descriptor table 

#### 78.3.3.4.2 ADMA interrupt 

If the interrupt flag descriptor is set, ADMA generates an interrupt according to various types of descriptors. For ADMA1: 

- Set type of descriptor: interrupt is generated when data length is set. 

- Tran type descriptor: interrupt is generated when this transfer is complete. 

- Link type of descriptor: interrupt is generated when new descriptor address is set. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4443 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

- Nop type of descriptor: interrupt is generated just after this descriptor is fetched. 

For ADMA2: 

- Tran type of descriptor: interrupt is generated when this transfer is complete. 

- Link type of descriptor: interrupt is generated when new descriptor address is set. 

- Nop/Rsv type of descriptor: interrupt is generated just after this descriptor is fetched. 

#### 78.3.3.4.3 ADMA error 

The ADMA stops whenever an error is encountered. These errors include: 

- Fetching descriptor error 

- AHB response error 

- Data length mismatch error 

An ADMA descriptor error is generated when it fails to detect a "valid" flag in the descriptor. If an ADMA descriptor error occurs, the interrupt is not generated even if the "Interrupt" flag of this descriptor is set. 

When BLKCNTEN bit is set, data length set in register BLK_ATT must be equal to the whole data length set in descriptor, otherwise data length mismatch error is generated. 

When BLKCNTEN bit is not set, then the whole data length set in descriptor is a multiple of block lengths; otherwise, when data set in the descriptor nodes are not performed at block boundaries, then data mismatch errors occur. 

### 78.3.4 Register bank with IP bus interface 

Register accesses through the IP bus interface are on the register bank. See the figure below for the block diagram. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4444-17.png)


<!-- Start of picture text -->
Register Bank<br>Control Signals<br>ips_xfr_err to other modules<br>"0"<br>Software<br>ips_xfr_wait Visible<br>"0" Registers<br>Status Signals<br>from other modules<br>Control/ Status<br>Signals<br>Write 1 Clear Control/ Status<br>Function Signals<br>Array with other domains Synchronizer<br>IP Bus<br>Signals<br>Data Port Buffer Control<br>Figure 495. Register bank diagram<br><!-- End of picture text -->

Only a 32-bit access is allowed, and no partial read/write is supported; therefore, all accesses are word aligned. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4444 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

Access to an unimplemented address within the register memory map space does not generate a transfer error. 

#### 78.3.4.1 SD protocol unit 

The SD protocol unit deals with all SD protocol affairs. 

The SD protocol unit performs the following functions: 

- Acts as the bridge between the internal buffer and the SD bus 

- Sends the command data as well as its argument serially 

- Stores the serial response bit stream into corresponding registers 

- Detects the bus state on the CMD/DAT lines 

- Monitors the interrupt from the SDIO card 

- Asserts the read wait signal 

- Gates off the SD clock when buffer is announcing danger status 

- Detects the write protect state 

The SD protocol unit consists of four submodules: 

- SD control misc 

- Command control 

- Data control 

- Clock control 

#### 78.3.4.2 SD control misc 

In the SD control misc unit: 

- The card detection (including CD_B and DATA3 for card detection) and card interrupt are implemented. 

- The module monitors the signal level on all the eight data lines and the command lines. It directly routes the level values into the register bank. 

- The module also detects the Write Protect (WP) line. If WP is active, writes to memory and combo cards are ignored. 

#### 78.3.4.3 SD clock control 

If the internal data buffer is near full (for read) or near empty (for write), the SD clock must be gated off to avoid buffer over/under-run. This module asserts the gate of the output SD clock to shut the clock off. After the buffer has space (for read) or has data (for write), the clock gate of this module opens, and the SD clock is active again. 

#### 78.3.4.4 Command control 

The Command Control module deals with the transactions on the CMD line. 

See the figure below for an illustration of the structure for the Command CRC shift register. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4445 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4446-01.png)


<!-- Start of picture text -->
Ultra Secured Digital Host Controller (uSDHC)<br>CLR_CRC<br>ZERO<br>CRC_IN<br>CRC     CRC     CRC     CRC     CRC     CRC     CRC<br>Bus [0]      Bus [1]      Bus [2]      Bus [3]      Bus [4]      Bus [5]      Bus [6]<br>CRC OUT<br>Figure 496. Command CRC shift register<br><!-- End of picture text -->

The CRC polynomials for the CMD are as follows: 

```
Generator polynomial: G(x) = x7 + x3 + 1
M(x) = (first bit) * xn + (second bit) * xn-1 +...+ (last bit) * x0
CRC[6:0] = Remainder [(M(x) * x7) / G(x)]
```

#### 78.3.4.5 Data control 

The data agent deals with the transactions on the eight data lines. Moreover, this module also detects the busy state on the DATA0 line and generates the read wait state by the request from the transceiver. 

The CRC polynomials for the data are as follows: 

```
Generator polynomial: G(x) = x16 + x12 + x5 +1
M(x) = (first bit) * xn + (second bit) * xn-1 +...+ (last bit) * x0
CRC[15:0] = Remainder [(M(x) * x16) / G(x)]
```

### 78.3.5 Card insertion and removal detection 

The uSDHC module uses either the DATA3 pin or the CD_B pin to detect card insertion or removal. When there is no card on the eMMC/SD bus, the DATA3 is pulled to a low voltage level by default. 

When any card is inserted to or removed from the socket, uSDHC detects the logic value changes on the DATA3 pin and generates an interrupt. When the DATA3 pin is not used for card detection (for example, it is implemented in GPIO), the CD_B pin must be connected for card detection. Whether DATA3 is configured for card detection or not, the CD_B pin is always a reference for card detection. Whether the DATA3 pin or the CD_B pin is used to detect card insertion, uSDHC sends an interrupt (if enabled) to inform the Host system that a card is inserted. 

### 78.3.6 Power management and wakeup events 

When there is no operation between uSDHC and the card through the SD bus, the user can completely disable the peripheral clock and base clock in the chip-level clock control module to save power. When the user needs to use uSDHC to communicate with the card, it can enable the clock and start the operation. 

In some circumstances, when the clocks to uSDHC are disabled, for instance, when the system is in low-power mode, there are some events for which the user needs to enable the clock and handle the event. These events are called wakeup interrupts. The uSDHC module can generate these interrupts even when there are no clocks enabled. The three interrupts that can be used as wakeup events are these: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4446 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

- Card removal interrupt 

- Card insertion interrupt 

- Interrupt from SDIO card (not available in multiple block data transfers) 

These three wakeup events (or wakeup interrupts) can also be used to wakeup the system from low-power modes. 

~~<mark>NOTE</mark>~~ 

To make the interrupt a wakeup event, when all the clocks to uSDHC are disabled or when the entire system is in low power mode, the corresponding wakeup enabled bit needs to be set. Refer to Protocol Control (PROT_CTRL) for more information on the uSDHC Protocol Control register. 

#### 78.3.6.1 Setting wakeup events 

For uSDHC to respond to a wakeup event, the software must set the respective wakeup enable bit before the CPU enters the sleep mode. Before the software disables the host clock, it should ensure that all the following conditions have been met: 

- No read or write transfer is active 

- Data and command lines are not active 

- No interrupts are pending 

- Internal data buffer is empty 

### 78.3.7 eMMC fast boot 

The Embedded MultiMediaCard (eMMC4.3) specification adds a fast boot feature that requires hardware support. There are two types of fast boot modes in the eMMC4.3 specification: boot operation and alternative boot operation. Each type also has with-acknowledge and without-acknowledge modes. 

In the boot operation mode, the master (MultiMediaCard host) can read boot data from the slave (eMMC device) by keeping CMD line low after power-on, or sending CMD0 with argument + 0xFFFFFFFA (optional for slave), before issuing CMD1. 

~~<mark>NOTE</mark>~~ 

For the eMMC4.3 setting, please see the eMMC4.3 specification. 

#### 78.3.7.1 Boot operation 

If the CMD line is held low for 74 clock cycles and more after power-up before the first command is issued, the slave recognizes that boot mode is being initiated and starts preparing boot data internally. 

Within one second after the CMD line goes low, the slave starts to send the first boot data to the master on the DATA line(s). The master must keep the CMD line low to read all of the boot data. 

~~<mark>NOTE</mark>~~ 

For the purposes of this documentation, fast boot is called "normal fast boot mode". 

If boot acknowledge is enabled, the slave has to send acknowledge pattern '010' to the master within 50ms after the CMD line goes low. If boot acknowledge is disabled, the slave does not send out acknowledge pattern '010'. 

The master can terminate the boot mode with the CMD line high. 

The boot operation is terminated when all the contents of the enabled boot data are sent to the master. After the boot operation is executed, the slave gets ready for the CMD1 operation and the master needs to start a normal eMMC initialization sequence by sending CMD1. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4447 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4448-02.png)


<!-- Start of picture text -->
CLK<br>CMD CMD1 RESP CMD2 RESP CMD3 RESP<br>DATA0 S 010 E S 512 bytes E S 512 bytes E<br>+CRC +CRC<br>Boot terminated<br>50 ms max<br>Min 8 clocks + 48 clocks =56 clocks required from CMD signal high to next eMMC command<br>1 sec. max<br><!-- End of picture text -->

Figure 497. Embedded MultiMediaCard state diagram (normal boot mode) 

#### 78.3.7.2 Alternative boot operation 

This boot function is optional for the device. If bit 0 in the extended CSD byte[228] is set to '1', the device supports the alternative boot operation. 

After power-up, if the host issues CMD0 with the argument of 0xFFFFFFFA after 74 clock cycles, before CMD1 is issued or the CMD line goes low, the slave recognizes that boot mode is being initiated and starts preparing boot data internally. 

Within one second after CMD0 with the argument of 0xFFFFFFFA is issued, the slave starts to send the first boot data to the master on the DATA line(s). 

If boot acknowledge is enabled, the slave must send the acknowledge pattern '010' to the master within 50ms after the CMD0 with the argument of 0xFFFFFFFA is received. If boot acknowledge is disabled, the slave does not send out acknowledge pattern '010'. 

The master can terminate the boot mode by issuing CMD0 (Reset). 

Boot operation is terminated when all the contents of the enabled boot data are sent to the master. After the boot operation is executed, the slave gets ready for the CMD1 operation and the master needs to start a normal eMMC initialization sequence by sending CMD1. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4448-11.png)


<!-- Start of picture text -->
CLK<br>CMD CMD0 1 CMD0/Reset CMD1 RESP CMD2 RESP CMD3 RESP<br>512 BYTES 512 BYTES<br>DATA0 S 010 E S E S E<br>+CRC +CRC<br>50 ms<br>max<br>Min 74 clocks<br>required after<br>power is stable 1 sec. max<br>to start boot<br>command.<br><!-- End of picture text -->

NOTE 1: CMD0 with argument 0xFFFFFFFA 

Figure 498. Embedded MultiMediaCard state diagram (alternative boot mode) 

### 78.3.8 Commands for SD card, SDIO card, and eMMC 

A table containing the list of commands for the eMMC/SD card/SDIO card is provided here. 

Refer to the corresponding specifications for more details about the command information. 

There are four kinds of commands defined to control the eMMC: 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4448 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

- Broadcast commands (bc), no response 

- Broadcast commands with response (bcr), response from all cards simultaneously 

- Addressed (point-to-point) commands (ac), no data transfer on the DATA 

- Addressed (point-to-point) data transfer commands (adtc) 

Response: A response is a token that is sent from the card to the host as an answer to a previously received command. A response is transferred serially on the CMD line. 

Table 678. Commands for eMMC/SD card/SDIO card 

|CMD INDEX|Type|Argument|Response<br>type|Abbreviation|Description|
|---|---|---|---|---|---|
|CMD0|bc|[31:0] stuff bits|-|GO_IDLE_STATE|Resets all eMMC and SD memory<br>cards to idle state.|
|CMD1|bcr|[31:0] OCR<br>without busy|R3|SEND_OP_COND|Asks all eMMC and SD Memory<br>cards in idle state to send<br>their operation conditions register<br>contents in the response on the<br>CMD line.|
|CMD2|bcr|[31:0] stuff bits|R2|ALL_SEND_CID|Asks all cards to send their CID<br>numbers on the CMD line.|
|CMD3<sup>1</sup>|ac|[31:6] RCA<br>[15:0] stuff bits|R1<br>R6 (SDIO)|SET/<br>SEND_RELATIVE_AD<br>DR|Assigns relative address to<br>the card.|
|CMD4|bc|[31:0] DSR<br>[15:0] stuff bits|-|SET_DSR|Programs the DSR of all cards.|
|CMD5|bc|[31:0] OCR<br>without busy|R4|IO_SEND_OP_COND|Asks all SDIO cards in idle state<br>to send them operation conditions<br>register contents in the response on<br>the CMD line.|
|CMD6<sup>2</sup>|adtc|[31] Mode<br>0: Check function<br>1: Switch function<br>[30:8] Reserved for<br>function groups 6 ~ 3<br>(All 0 or 0xFFFF)<br>[7:4] Function group1<br>for command system<br>[3:0] Function group2<br>for access mode|R1|SWITCH_FUNC|Checks switch ability (mode 0) and<br>switch card function (mode 1). Refer<br>to "SD Physical Specification V1.1"<br>for more details.|
|CMD6<sup>3</sup>|ac|[31:26] Set to 0<br>[25:24] Access|R1b|SWITCH|Switches the mode of operation of<br>the selected card or modifies the<br>EXT_CSD registers. Refer to "The|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4449 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

Table 678. Commands for eMMC/SD card/SDIO card (continued) 

|CMD INDEX|Type|Argument|Response<br>type|Abbreviation|Description|
|---|---|---|---|---|---|
|||[23:16] Index<br>[15:8] Value<br>[7:3] Set to 0<br>[2:0] Cmd Set|||Embedded MultiMediaCard System<br>Specification Version 4.0 Final draft<br>2" for more details.|
|CMD7|ac|[31:6] RCA<br>[15:0] stuff bits|R1b|SELECT/<br>DESELECT_CARD|Toggles a card between the stand-<br>by and transfer states or between<br>the programming and disconnect<br>states. In both cases, the card is<br>selected by its own relative address<br>and gets deselected by any other<br>address. Address 0 deselects all.|
|CMD8|adtc|[31:0] stuff bits|R1|SEND_EXT_CSD|The card sends its EXT_CSD<br>register as a block of data, with a<br>block size of 512 bytes.|
|CMD9|ac|[31:6] RCA<br>[15:0] stuff bits|R2|SEND_CSD|Addressed card sends its card-<br>specific data (CSD) on the<br>CMD line.|
|CMD10|ac|[31:6] RCA<br>[15:0] stuff bits|R2|SEND_CID|Addressed card sends its card-<br>identification (CID) on the CMD line.|
|CMD11|adtc|[31:0] data address|R1|READ_DAT_UNTIL_S<br>TOP|Reads data stream from the card,<br>starting at the given address, until a<br>STOP_TRANSMISSION follows.|
|CMD12|ac|[31:0] stuff bits|R1b|STOP_TRANSMISSIO<br>N|Forces the card to<br>stop transmission.|
|CMD13|ac|[31:6] RCA<br>[15:0] stuff bits|R1|SEND_STATUS|Addressed card sends its<br>status register.|
|CMD14|Reserv|ed||||
|CMD15|ac|[31:6] RCA<br>[15:0] stuff bits|-|GO_INACTIVE_STAT<br>E|Sets the card to inactive<br>state in order to protect<br>the card stack against<br>communication breakdowns.|
|CMD16|ac|[31:0] block length|R1|SET_BLOCKLEN|Sets the block length (in bytes) for<br>all following block commands (read<br>and write). Default block length is<br>specified in the CSD.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4450 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

Table 678. Commands for eMMC/SD card/SDIO card (continued) 

|CMD INDEX|Type|Argument|Response<br>type|Abbreviation|Description|
|---|---|---|---|---|---|
|CMD17|adtc|[31:0] data address|R1|READ_SINGLE_BLO<br>CK|Reads a block of the size selected<br>by the SET_BLOCKLEN command.|
|CMD18|adtc|[31:0] data address|R1|READ_MULTIPLE_BL<br>OCK|Continuously transfers data blocks<br>from card to host until interrupted by<br>a stop command.|
|CMD19|Reserv|ed||||
|CMD20|adtc|[31:0] data address|R1|WRITE_DAT_UNTIL_<br>STOP|Writes data stream from the host,<br>starting at the given address, until a<br>STOP_TRANSMISION follows.|
|CMD21|Reserv|ed||||
|CMD22-23|Reserv|ed||||
|CMD24|adtc|[31:0] data address|R1|WRITE_BLOCK|Writes a block of the size selected<br>by the SET_BLOCKLEN command.|
|CMD25|adtc|[31:0] data address|R1|WRITE_MULTIPLE_B<br>LOCK|Continuously writes blocks<br>of data until a<br>STOP_TRANSMISSION follows.|
|CMD26|adtc|[31:0] stuff bits|R1|PROGRAM_CID|Programming of the card<br>identification register. This<br>command is issued only once per<br>card. The card contains hardware<br>to prevent this operation after<br>the first programming. Normally<br>this command is reserved for<br>the manufacturer.|
|CMD27|adtc|[31:0] stuff bits|R1|PROGRAM_CSD|Programming of the programmable<br>bits of the CSD.|
|CMD28|ac|[31:0] data address|R1b|SET_WRITE_PROT|If the card has write protection<br>features, this command sets the<br>write protection bit of the addressed<br>group. The properties of write<br>protection are coded in the card<br>specific data (WP_GRP_SIZE).|
|CMD29|ac|[31:0] data address|R1b|CLR_WRITE_PROT|If the card provides write protection<br>features, this command clears<br>the write protection bit of the<br>addressed group.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4451 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

Table 678. Commands for eMMC/SD card/SDIO card (continued) 

|CMD INDEX|Type|Argument|Response<br>type|Abbreviation|Description|
|---|---|---|---|---|---|
|CMD30|adtc|[31:0] write protect<br>data address|R1|SEND_WRITE_PROT|If the card provides write protection<br>features, this command asks the<br>card to send the status of the write<br>protection bits.|
|CMD31|Reserv|ed||||
|CMD32|ac|[31:0] data address|R1|TAG_SECTOR_STAR<br>T|Sets the address of the first sector<br>of the erase group.|
|CMD33|ac|[31:0] data address|R1|TAG_SECTOR_END|Sets the address of the last sector<br>in a continuous range within the<br>selection of a single sector to be<br>selected for erase.|
|CMD34|ac|[31:0] data address|R1|UNTAG_SECTOR|Removes one previously selected<br>sector from the erase selection.|
|CMD35|ac|[31:0] data address|R1|TAG_ERASE_GROUP<br>_START|Sets the address of the first erase<br>group within a range to be selected<br>for erase.|
|CMD36|ac|[31:0] data address|R1|TAG_ERASE_GROUP<br>_END|Sets the address of the last erase<br>group within a continuous range to<br>be selected for erase.|
|CMD37|ac|[31:0] data address|R1|UNTAG_ERASE_GR<br>OUP|Removes one previously<br>selected erase group from the<br>erase selection.|
|CMD38|ac|[31:0] stuff bits|R1b|ERASE|Erase all previously<br>selected sectors.|
|CMD39|ac|[31:0] RCA<br>[15] register write flag<br>[14:8]<br>register address<br>[7:0] register data|R4|FAST_IO|Used to write and read 8-bit<br>(register) data fields. The command<br>addresses a card, and a register,<br>and provides the data for writing<br>if the write flag is set. The R4<br>response contains data read from<br>the address register. This command<br>accesses application dependent<br>registers which are not defined in<br>the eMMC standard.|
|CMD40<br>CMD41|bcr<br>Reserv|[31:0] stuff bits<br>ed|R5|GO_IRQ_STATE|Sets the system into interrupt mode.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4452 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

Table 678. Commands for eMMC/SD card/SDIO card (continued) 

|CMD INDEX|Type|Argument|Response<br>type|Abbreviation|Description|
|---|---|---|---|---|---|
|CDM42|adtc|[31:0] stuff bits|R1b|LOCK_UNLOCK|Used to set/reset the password<br>or lock/unlock the card. The size<br>of the data block is set by the<br>SET_BLOCK_LEN command.|
|CMD43~51|Reserv|ed||||
|CMD52|ac|[31:0] stuff bits|R5|IO_RW_DIRECT|Access a single register within the<br>total 128k of register space in any<br>I/O function.|
|CMD53|ac|[31:0] stuff bits|R5|IO_RW_EXTENDED|Accesses a multiple I/O register<br>with a single command. Allows the<br>reading or writing of a large number<br>of I/O registers.|
|CMD54|Reserv|ed||||
|CMD55|ac|[31:16] RCA<br>[15:0] stuff bits|R1|APP_CMD|Indicates to the card that the<br>next command is an application<br>specific command rather than a<br>standard command.|
|CMD56|adtc|[31:1] stuff bits<br>[0]: RD/WR|R1b|GEN_CMD|Used either to transfer a data block<br>to the card or to get a data block<br>from the card for general purpose /<br>application specific commands. The<br>size of the data block is set by the<br>SET_BLOCK_LEN command.|
|CMD57-59|Reserv|ed||||
|CMD60|adtc|[31] WR<br>[30:24] stuff bits<br>[23:16] address<br>[15:8] stuff bits<br>[7:0] byte count|R1b|RW_MULTIPLE_REGI<br>STER|These registers are used to<br>control the behavior of the device<br>and to retrieve status information<br>regarding the operation of the<br>device. All Status and Control<br>registers are WORD (32-bit) in<br>size and are WORD aligned.<br>CMD60 is used to read and write<br>these registers.|
|CMD61<br>CMD62-63|adtc<br>Reserv|[31] WR<br>[30:16] stuff bits<br>[15:0] data unit count<br>ed|R1b|RW_MULTIPLE_BLO<br>CK|The host issues a<br>RW_MULTIPLE_BLOCK (CMD61)<br>to begin the data transfer.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4453 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

Table 678. Commands for eMMC/SD card/SDIO card (continued) 

|CMD INDEX|Type|Argument|Response<br>type|Abbreviation|Description|
|---|---|---|---|---|---|
|ACMD6<sup>4</sup>|ac|[31:2] stuff bits<br>[1:0] bus width|R1|SET_BUS_WIDTH|Defines the data bus width<br>('00'=1bit or '10'=4bit bus) to be<br>used for data transfer. The allowed<br>data bus widths are given in<br>SCR register.|
|ACMD13<sup>4</sup>|adtc|[31:0] stuff bits|R1|SD_STATUS|Send the SD Memory Card status.|
|ACMD22<sup>4</sup>|adtc|[31:0] stuff bits|R1|SEND_NUM_WR_SE<br>CTORS|Send the number of the written<br>sectors (without errors). Responds<br>with 32-bit plus the CRC data block.|
|ACMD23<sup>4</sup>|ac|[31:23] stuff bits<br>[22:0] Number<br>of blocks|R1|SET_WR_BLK_ERAS<br>E_COUNT|Set the number of write blocks to<br>be pre-erased before writing (to<br>be used for fast Multiple Block<br>WR command). "1"=default(one<br>write block).|
|ACMD41<sup>4</sup>|bcr|[31:0] OCR|R3|SD_APP_OP_COND|Asks the accessed card to send its<br>operating condition register (OCR)<br>contents in the response on the<br>CMD line.|
|ACMD42<sup>4</sup>|ac|[31:1] stuff bits<br>[0] set_cd|R1|SET_CLR_CARD_DE<br>TECT|Connect(1)/Disconnect(0) the<br>50KOhm pull-up resistor on CD_B/<br>DATA3 of the card.|
|ACMD51<sup>4</sup>|adtc|[31:0] stuff bits|R1|SEND_SCR|Reads the SD Configuration<br>Register (SCR).|



1. CMD3 differs for eMMC and SD cards. For eMMC, it is referred to as SET_RELATIVE_ADDR, with a response type of R1. For SD cards, it is referred to as SEND_RELATIVE_ADDR, with a response type of R6 (with RCA inside). 

2. CMD6 differs completely between high speed eMMC and high-speed SD cards. Command SWITCH_FUNC is for highspeed SD cards. 

3. Command SWITCH is for high speed eMMC. The Index field can contain any value from 0-255, but only values 0-191 are valid. If the Index value is in the 192-255 range the card does not perform any modification and the SWITCH_ERROR status bit in the EXT_CSD register is set. The Access Bits are shown in Table 679. 

4. ACMDs is preceded with the APP_CMD command. Commands listed are used for SD only, other SD commands not listed are not supported on this module. 

The access bits for the EXT_CSD access modes are listed in the following table. 

Table 679. EXT_CSD access modes 

|Bits|Access name|Operation|
|---|---|---|
|00|Command set|The command set is changed according to the Cmd Set field of the argument.|
|01|Set bits|The bits in the pointed byte are set, according to the bits set to 1 in the Value field.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4454 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

Table 679. EXT_CSD access modes (continued) 

|10|Clear bits|The bits in the pointed byte are cleared, according to the bits set to 1 in the Value field.|
|---|---|---|
|11|Write byte|The Value field is written into the pointed byte.|



### 78.3.9 Clocks 

The table found here describes the clock sources for uSDHC. For more information on clocking, see the Clocking chapter. 

Table 680. Clocks 

|Clock name|Description|
|---|---|
|hclk|Bus clock|
|ipg_clk|Peripheral clock|
|ipg_clk_s|Peripheral access clock for register access|
|ipg_clk_perclk|Base clock|



### 78.3.10 Clock and reset manager 

This module controls all four kinds reset signals within uSDHC: 

- Hardware reset 

- Software reset for all logic 

- Software reset for the data logic 

- Software reset for the command logic 

All these signals are fed into this module and stable signals are generated inside the module to reset all other modules. The module also gates off all the inside signals. 

### 78.3.11 Clock generator 

The clock generator generates the card CLK by peripheral source clock in two stages. The clock divisor can be configured through register SYS_CTRL[SDCLKFS] for prescaler configuration while the [DVS] for divisor configuration. Details can be found in the register function description. See the following figure for the structure of the divider. The term "Base" represents the frequency of peripheral source clock. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4455-17.png)


<!-- Start of picture text -->
card_clk<br>Base      1st divisor 2nd divisor CLK<br>DIV<br>by 1, 2, 3, ..., 16      by (1*), 2, 4, ..., 256<br>/2<br>DDR_EN<br><!-- End of picture text -->

##### Figure 499. Two stages of the clock divider 

The first stage outputs an intermediate clock (DIV) that can be Base, Base/2, Base/3, ..., or Base/16. 

The second stage is a prescaler and outputs the actual internal working clock (card_clk). This clock is the driving clock for all the sub modules of the SD protocol unit, and helps in syncing FIFOs (see Figure 486) to synchronize with the data rate from the internal data buffer. The frequency of the clock output from this stage can be DIV, DIV/2, DIV/4,..., or DIV/256. Therefore, the highest frequency of the card_clk is base, and the next highest is Base/2, while the lowest frequency is Base/4096. If the duty cycle of the base clock is 50%, the duty cycle of card_clk is also 50%, even when the compound divisor is an odd value. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4455 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

~~<mark>NOTE</mark>~~ 

###### CLK is different for the SDR and DDR modes. 

- In the SDR mode, CLK is equal to the internal working clock (card_clk). 

- In the DDR mode, CLK is equal to card_clk/2. 

### 78.3.12 SDIO card interrupt 

Information on interrupts in 1-bit mode, interrupts in 4-bit mode, and card interrupt handling are detailed in the sections below. 

#### 78.3.12.1 Interrupts in 1-bit mode 

In this case, the DATA1 pin provides the interrupt function. An interrupt is asserted by pulling the DATA1 low from the SDIO card, until the interrupt service is finished to clear the interrupt. 

#### 78.3.12.2 Interrupt in 4-bit mode 

As the interrupt and data line 1 share pin 8 in a 4-bit mode, an interrupt is only sent by the card and recognized by the host during a specific time. This is known as the interrupt period. The uSDHC module only provides samples the level on pin 8 during the interrupt period. At all other times, the host treats it as the data signal. The definition of the interrupt period is different for operations with single block and multiple block data transfers. 

In the case of normal single data block transmissions, the interrupt period becomes active two clock cycles after the completion of a data packet. This interrupt period lasts until after the card receives the end bit of the next command that has a data block transfer associated with it. 

For multiple block data transfers in a 4-bit mode, there is only a limited period of time that the interrupt period can be active because of the limited period of data line availability between the multiple blocks of data. This requires stricter definition of the interrupt period. For this case, the interrupt period is limited to two clock cycles. This begins two clocks after the end bit of the previous data block. During this 2-clock cycle interrupt period, if an interrupt is pending, the DATA1 line holds low for one clock cycle, then pulls high for the next clock cycle . On completion of the interrupt period, the card releases the DATA1 line into the high Z state. The uSDHC module provides sample of the DATA1 during the interrupt period when the IABG bit in the Protocol Control register is set. 

Refer to SDIO Card Specification v1.10 for further information about the SDIO card interrupt. 

#### 78.3.12.3 Card interrupt handling 

When the CINTIEN bit in the Interrupt Signal Enable Register is set to 0, uSDHC clears the interrupt request to the host system. The host driver should clear this bit before servicing the SDIO interrupt, and should set this bit again after all interrupt requests from the card are cleared to prevent inadvertent interrupts. 

The SDIO Card Interrupt Status can be cleared by writing 1 to this bit. But as the interrupt source from the SDIO card does not clear, this bit is set again. To clear this bit, it is required to reset the interrupt source from the external card followed by writing 1 to this bit. In a 1-bit mode, uSDHC detects the SDIO interrupt with or without the SD clock (to support wakeup). In a 4-bit mode, the interrupt signal is sampled during the interrupt period, so there are some sample delays between the interrupt signal from the SDIO card and the interrupt to the Host System Interrupt Controller. When the SDIO status is set and the host driver needs to service this interrupt, the SDIO bit in the Interrupt Control Register of SDIO card is cleared. This is required to clear the SDIO interrupt status latched in uSDHC and to stop driving the interrupt signal to the System Interrupt Controller. The host driver must issue a CMD52 to clear the card interrupt. After completion of the card interrupt service, the SDIO Interrupt Status Enable bit is set to 1 and uSDHC starts sampling the interrupt signal again. 

See the figure below for an illustration of the SDIO card interrupt scheme and for the sequences of software and hardware events that take place during a card interrupt handling procedure. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4456 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4457-02.png)


<!-- Start of picture text -->
IP Bus<br>IRQ to CPUm<br>Start<br>Enable card IRQ in Host<br>uSDHC Registers<br>SDIO IRQ Status      Command/<br>Detect and steer card IRQ<br>Response<br>Handling<br>SDIO IRQ Enable<br>Read IRQ Status Register<br>Disable Card Interrupt Status enable in Host,<br>THEN write 1 to clear Card Interrupt status<br>IRQ Detecting & Steering<br>Interrogate and Service Card IRQ<br>SD Host<br>SDIO Card<br>Response  Yes<br>Error ?<br>SDIO Card No<br>IRQ Routing<br>Clear Card IRQ in Card<br>IRQ0      IRQ1<br>Enable card IRQ in Host<br>Function 0 Function 1<br>Clear IRQ0      Clear IRQ1      End<br><!-- End of picture text -->

Figure 500. Card interrupt scheme, card interrupt detection, and handling procedure 

## 78.4 External signals 

The following table describes the uSDHC external signals: 

##### Table 681. uSDHC external signals 

|Signal|Description|Direction|
|---|---|---|
|CLK|Clock for eMMC/SD card/SDIO card|O|
|CMD|CMD line connect to card|I/O|
|DATA7|DAT7 line in the 8-bit mode —|I/O|
||Not used in other modes||
|DATA6|DAT6 line in the 8-bit mode —|I/O|
||Not used in other modes||
|DATA5|DAT5 line in the 8-bit mode —|I/O|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4457 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

Table 681. uSDHC external signals (continued) 

|Signal|Description|Direction|
|---|---|---|
||Not used in other modes||
|DATA4|DAT4 line in the 8-bit mode —<br>Not used in other modes|I/O|
|DATA3|DAT3 line in the 4/8-bit mode or configured as card detection<br>pin.<br>The bit may be configured as card detection pin in the 1-<br>bit mode.|I/O|
|DATA2|DAT2 line or Read Wait in the 4-bit mode<br>Read Wait in 1-bit mode|I/O|
|DATA1|DAT1 line in the 4/8-bit mode<br>Also, used to detect interrupt in 1/4-bit mode|I/O|
|DATA0|DAT0 line in all the modes<br>Also, used to detect busy state|I/O|
|CD_B|Card detection pin<br>If not used (for the embedded memory), tie low to indicate that<br>there is a card attached.|I|
|WP|Card write protect detect<br>If not used (for the embedded memory), tie low to indicate that<br>it is not write protected.|I|
|RESET_B|Card hardware reset signal, active low|O|



### 78.4.1 Signals overview 

uSDHC has 14 associated I/O signals. 

- The CLK is an internally generated clock used to drive the eMMC, SD card, and SDIO card. 

- The CMD I/O is used to send commands and receive responses to and from the card. Eight data lines (DAT7~DAT0) are used to perform data transfers between the uSDHC module and the card. 

- The CD is card detection signal directly routed from the socket. This signal is active low (0). A low on CD# means that a card is inserted. It is optional for system implementation. 

- The WP is write protection signals directly routed from the socket. This signal is active low (0). A high on WP means that the write protect switch is active. It is optional for system implementation. 

- RST is an output signal used to reset the eMMC. 

If uSDHC needs to support a 4-bit data transfer, DAT7~DAT4 can also be optional and tied to high. 

## 78.5 Application of uSDHC 

All communication between the system and cards are controlled by the host. The host sends commands of two types: broadcast and addressed (point-to-point). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4458 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

Broadcast commands are intended for all cards, such as GO_IDLE_STATE, SEND_OP_COND, and ALL_SEND_CID. In the Broadcast mode, all cards are in the open-drain mode to avoid bus contention. Refer to Commands for SD card, SDIO card, and eMMC for the commands of bc and bcr categories. 

After the broadcast command CMD3 is issued, the cards enter the standby mode. Addressed type commands are used from this point. In this mode, the CMD/DATA I/O pads turns to the push-pull mode to have the driving capability for maximum frequency operation. Refer to Commands for SD card, SDIO card, and eMMC for the commands of ac and adtc categories. 

### 78.5.1 Command send and response receive basic operation 

Assuming that the data type WORD is an unsigned 32-bit integer, the flow indicated below presents a guideline for sending a command to the card(s): 

```
send_command(cmd_index, cmd_arg, other requirements)
{
WORD wCmd; // 32-bit integer to make up the data to write into Transfer Type register, it is
recommended to implement in a bit-field manner
wCmd = (<cmd_index> & 0x3f) << 24; // set the first 8 bits as '00'+<cmd_index>
set CMDTYP, DPSEL, CICEN, CCCEN, RSTTYP, DTDSEL according to the command index;
if (internal DMA is used) wCmd |= 0x1;
if (multi-block transfer) {
          set MSBSEL bit;
          if (finite block number) {
                    set BCEN bit;
                    if (auto12 command is to use) set AC12EN bit;
          }
}
write_reg(CMDARG, <cmd_arg>); // configure the command argument
write_reg(XFERTYP, wCmd); // set Transfer Type register as wCmd value to issue the command
}
wait_for_response(cmd_index)
{
while (CC bit in IRQ Status register is not set); // wait until Command Complete bit is set
read IRQ Status register and check if any error bits about Command are set
if (any error bits are set) report error;
write 1 to clear CC bit and all Command Error bits;
```

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4459 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

###### `}` 

For the sake of simplicity, the function wait_for_response is implemented here by means of polling. For an effective and formal way, the response is usually checked after the Command Complete Interrupt is received. When doing this, make sure that the corresponding interrupt status bits are enabled. 

For some scenarios, the response time-out is expected. For instance, after all cards respond to CMD3 and move to the Standby state no response to the Host when CMD2 is sent. The host driver deals with "fake" errors like this with caution. 

### 78.5.2 Card identification mode 

When a card is inserted to the socket or the card is reset by the host, the host needs to validate the operation voltage range, identify the cards, request the cards to publish the Relative Card Address (RCA) or to set the RCA for eMMC. 

#### 78.5.2.1 Card detect 

See the figure below for a flow diagram showing the detection of eMMC, SD card, and SDIO card using uSDHC. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4460-09.png)


<!-- Start of picture text -->
Enable card detection irq      (1)<br>Wait for uSDHC interrupt<br>No cards present<br>Check CINS bit<br>Yes cards present<br>(2)<br>Clear CINSIEN to disable<br>card detection irq<br>Voltage validation<br>Figure 501. Flow diagram for card detection<br><!-- End of picture text -->

Here is the card detect sequence: 

- Set the CINSIEN bit to enable card detection interrupt. 

- When an interrupt from uSDHC is received, check the CINS bit in the Interrupt Status register to see if it was caused by card insertion. 

- Clear the CINSIEN bit to disable the card detection interrupt and ignore all card insertion interrupts afterwards. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4460 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

#### 78.5.2.2 Reset 

The host consists of three types of resets: 

- Hardware reset (Card and Host) that is driven by Power On Reset (POR). 

- Software reset (Host only) is initiated by the write operation on the RSTD, RSTC, or RSTA bits of the System Control register to reset the data part, command part, or all parts of the host controller, respectively. 

- Card reset (Card only): The command, "Go_Idle_State" (CMD0), is the software reset command for all types of eMMC and SD memory cards. This command sets each card into the idle state regardless of the current card state. For an SDIO card, CMD52 is used to write an I/O reset in CCCR. The cards are initialized with a default relative card address (RCA=0x0000) and with a default driver stage register setting (lowest speed, highest driving current capability). 

After the card is reset, the host needs to validate the voltage range of the card. See the figure below for the software flow to reset both uSDHC and the card. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4461-08.png)


<!-- Start of picture text -->
write "1" to RSTA bit to reset uSDHC<br>Send 80 clocks to card<br>Send CMD0/ CMD52 to card to reset card<br>Voltage Validation<br><!-- End of picture text -->

Figure 502. Flow chart for resetting uSDHC and SD I/O card 

```
software_reset() {
set_bit(SYSCTRL, RSTA); // software reset the Host set DTOCV and SDCLKFS bit fields to get the CLK of
frequency around 400kHz
                        //configure IO pad to set the power voltage of external card to around 3.0V
poll bits CIHB and CDIHB
                        //bits of PRSSTAT to wait both bits are cleared
set_bit(SYSCTRL, INTIA); // send 80 clock ticks for card to power up
send_command(CMD_GO_IDLE_STATE, <other parameters>); // reset the card with CMD0 or
send_command(CMD_IO_RW_DIRECT, <other parameters>);
}
```

#### 78.5.2.3 Voltage validation 

All cards should be able to establish communication with the host using any operation voltage in the maximum allowed voltage range specified in the card specification. However, the supported minimum and maximum values for VDD are defined in the Operation Conditions Register (OCR) and may not cover the whole range. Cards that store the CID and CSD data in the preload memory are only able to communicate this information under data transfer VDD conditions. This means that if the host and card have non-common VDD ranges, the card is neither able to complete the identification cycle nor able to send CSD data. 

Therefore, special commands Send_Op_Cont (CMD1 for eMMC), SD_Send_Op_Cont (ACMD41 for SD Memory), and IO_Send_Op_Cont (CMD5 for SD I/O) are used. The voltage validation procedure is designed to provide a mechanism to identify and reject cards that do not match the VDD range(s) desired by the host. This is accomplished when the host sends the desired VDD voltage window as the operand of this command. Cards that cannot perform the data transfer in the specified range 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4461 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

must discard themselves from further bus operations and go into the Inactive state. By omitting the voltage range in the command, the host can query each card and determine the common voltage range before sending out-of-range cards into the Inactive state. This query should be used if the host is able to select a common voltage range or if a notification is sent to the system when a non-usable card in the stack is detected. 

The following steps show how to perform voltage validation when a card is inserted: 

```
voltage_validation(voltage_range_argument) {
    label the card as UNKNOWN;
    send_command(IO_SEND_OP_COND, 0x0, <other parameters are omitted>); // CMD5, check SDIO operation
voltage, command argument is zero
    if (RESP_TIMEOUT != wait_for_response(IO_SEND_OP_COND)) { // SDIO command is accepted
        if (0 < number of IO functions) {
            label the card as SDIO;
            IORDY = 0;
            while (!(IORDY in IO OCR response)) { // set voltage range for each IO function
                send_command(IO_SEND_OP_COND, <voltage range>, <other parameter>);
                wait_for_response(IO_SEND_OP_COND);
            } // end of while ...
        } // end of if (0 < ...
        if (memory part is present inside SDIO card)
            Label the card as SDCombo; //this is an SD-Combo card
    } // end of if (RESP_TIMEOUT ...
    if (the card is labelled as SDIO card)
        return; // card type is identified and voltage range is set, so exit the function;
    send_command(APP_CMD, 0x0, <other parameters are omitted>); // CMD55, Application specific CMD
prefix
    if (no error calling wait_for_response(APP_CMD, <...>) { // CMD55 is accepted
        send_command(SD_APP_OP_COND, <voltage range>, <...>); // ACMD41, to set voltage range for
memory part or SD card
        wait_for_response(SD_APP_OP_COND); // voltage range is set
        if (card type is UNKNOWN)
            label the card as SD;
        return; //
    } // end of if (no error ...
    else if (errors other than time-out occur) { // command/response pair is corrupted
        deal with it by program specific manner;
    } // of else if (response time-out
    else { // CMD55 is refuse, it must be eMMC
        if (card is already labelled as SDCombo) { // change label re-label the card as SDIO;
            ignore the error or report it;
            return; // card is identified as SDIO card
        } //of if (card is ...
        send_command(SEND_OP_COND, <voltage range>, <...>);
        if(RESP_TIMEOUT == wait_for_response(SEND_OP_COND)) { // CMD1 is not accepted, either label
the card as UNKNOWN;
            return;
        } // of if (RESP_TIMEOUT ...
    } // of else
}
```

#### 78.5.2.4 Card registry 

This section briefly describes the registry flow. For details, please refer to the card specifications. Card registry for the eMMC and SD/SDIO/SD combo cards are different. For the SD card, the identification process starts at a clock rate lower than 400 kHz and the power voltage higher than 2.7 V (as defined by the card spec). Currently, the CMD line output drives are push-pull drivers instead of open-drain. After the bus is activated, the host requests the card to send their valid operation conditions. The response to ACMD41 is the operation condition register of the card. The same command is sent to all the new cards in the system. Incompatible cards are put into the Inactive state. The host then issues the command, All_Send_CID (CMD2), to each 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4462 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

card to get its unique card identification (CID) number. Cards that are currently unidentified (in the Ready state), send their CID number as the response. After the CID is sent by the card, the card goes into the Identification state. 

The host then issues Send_Relative_Addr (CMD3), requesting the card to publish a new relative card address (RCA) that is shorter than the CID. This RCA is used to address the card for future data transfer operations. After the RCA is received, the card changes its state to the Standby state. At this point, if the host wants the card to have an alternative RCA number, it may ask the card to publish a new number by sending another Send_Relative_Addr command to the card. The last published RCA is the actual RCA of the card. 

The host repeats the identification process with CMD2 and CMD3 for each card in the system until the last CMD2 gets no response from any of the cards in the system. 

For eMMC operation, the host starts the card identification process in the open-drain mode with the identification clock rate lower than 400 kHz and the power voltage higher than 2.7 V. The open drain driver stages on the CMD line to allow parallel card operation during card identification. After the bus is activated, the host requests the cards to send their valid operation conditions (CMD1). The response to CMD1 is the "wired AND " operation on the condition restrictions of all cards in the system. Incompatible cards are sent into the Inactive state. The host then issues the broadcast command All_Send_CID (CMD2), asking all cards for their unique card identification (CID) number. All unidentified cards (the cards in the Ready state) simultaneously start sending their CID numbers serially, while bit-wise monitoring their outgoing bit stream. Those cards, whose outgoing CID bits do not match the corresponding bits on the command line in any one of the bit periods, stop sending their CID immediately and must wait for the next identification cycle. As the CID is unique for each card, only one card can be successfully sent its full CID to the host. This card then goes into the Identification state. Thereafter, the host issues Set_Relative_Addr (CMD3) to assign a relative card address (RCA) to the card. After the RCA is received, the state of the card changes to standby, and the card does not react in further identification cycles. Also, its output driver switches from open-drain to push-pull. The host repeats the process, mainly CMD2 and CMD3, until the host receives a time-out condition to recognize the completion of the identification process. 

The following steps show how to perform an operation using eMMC: 

```
card_registry() {
    do { // decide RCA for each card until response time-out
        if(card is labelled as SDCombo or SDIO) { // for SDIO card like device
            send_command(SET_RELATIVE_ADDR, 0x00, <...>); // ask SDIO card to publish its RCA
            retrieve RCA from response;
        } // end if (card is labelled as SDCombo ...
        else if (card is labelled as SD) { // for SD card
            send_command(ALL_SEND_CID, <...>);
            if(RESP_TIMEOUT == wait_for_response(ALL_SEND_CID))
                break;
            send_command(SET_RELATIVE_ADDR, <...>);
            retrieve RCA from response;
        } // else if (card is labelled as SD ...
        else if (card is labelled as eMMC) {
            send_command(ALL_SEND_CID, <...>);
            rca = 0x1; //arbitrarily set RCA, 1 here for example
            send_command(SET_RELATIVE_ADDR, 0x1 << 16, <...>); // send RCA at upper 16 bits
        } // end of else if (card is labelled as eMMC...
    } while (response is not time-out);
}
```

### 78.5.3 Card access 

Information about Block Write, Block Read, Suspense Resume, ADMA Usage, Transfer Error, and Card Interrupt are detailed in the sections below. 

#### 78.5.3.1 Block write 

Information on Normal Write, DDR Write, and Write with Pause are detailed in the sections below. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4463 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

#### 78.5.3.1.1 Normal Write 

During a block write (CMD24 - 27, CMD60, CMD61), one or more blocks of data are transferred from the host to the card with a CRC appended to the end of each block by the host. If the CRC fails, the card indicates that the failure on the DATA line. The transferred data is discarded and not written, and all further transmitted blocks (in multiple block write mode) are ignored. 

If the host uses partial blocks whose accumulated length is not block aligned and block misalignment is not allowed (CSD parameter WRITE_BLK_MISALIGN is not set), the card detects the block misalignment error and aborts the programming before the beginning of the first misaligned block. The card sets the ADDRESS_ERROR error bit in the status register, and while ignoring all further data transfer, waits in the Receive-data-State for a stop command. The write operation is also aborted if the host tries to write over a write-protected area. 

For eMMC and SD cards, programming of the CID and CSD registers does not require a previous block length setting. The transferred data is also CRC protected. If a part of the CSD or CID register is stored in ROM, then this unchangeable part must match the corresponding part of the receive buffer. If this match fails, then the card reports an error and does not change any register contents. 

For all types of cards, some may require long and unpredictable periods of time to write a block of data. After receiving a block of data and completing the CRC check, the card begins writing and holds the DATA line low if its write buffer is full and unable to accept new data from a new WRITE_BLOCK command. The host may poll the status of the card with a SEND_STATUS command (CMD13) or other means for SDIO cards at any time, and the card responds with its status. The responded status indicates whether the card can accept new data or whether the write process is still in progress. The host may deselect the card by issuing a CMD7 (to select a different card) to place the card into the Standby state and release the DATA line without interrupting the write operation. When re-selecting the card, it reactivates the busy indication by pulling data to low if the programming is still in progress and the write buffer is unavailable. 

The software flow to write to a card that incorporates the internal DMA and the write operation is a multi-block write with the Auto CMD12 enabled. For the other two methods (by means of external DMA or CPU polling status with different transfer methods, the internal DMA parts should be removed and the alternative steps should be straightforward. 

The software flow to write to a card is described below: 

1. Check the card status, wait until the card is ready for data. 

2. Set the card block length/size: 

   - For eMMC and SD cards, use SET_BLOCKLEN (CMD16). 

   - For SDIO cards or the I/O portion of SDCombo cards, use IO_RW_DIRECT (CMD52) to set the I/O Block Size bit field in the CCCR register (for function 0) or FBR register (for functions 1~7). 

3. Set the uSDHC block length register to be the same as the block length set for the card in step 2. 

4. Set the uSDHC number block register (NOB), where nob is 5, for instance. 

5. Disable the buffer write ready interrupt, configure the DMA settings and enable the uSDHC DMA when sending the command with data transfer. The AC12EN bit should also be set. 

6. Wait for the Transfer Complete interrupt. 

7. Check the status bit to see if a write CRC error occurred, or another error that occurred during the auto12 command sending and response receiving. 

#### 78.5.3.1.2 DDR write 

uSDHC supports the dual data rate mode. 

The software flow to write to a card in the DDR mode is described as below: 

1. Check the card status and wait until the card is ready for data. 

~~<mark>NOTE</mark>~~ 

For eMMC, block length only can be set to 512byte. 

2. Set the uSDHC number block register (NOB), where nob is 5, for instance. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4464 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

3. Set the eMMC to high-speed mode and use SWITCH(CMD6). 

4. Set the eMMC bus with 4-bit/8-bit DDR mode and use SWITCH(CMD6). 

5. Disable the buffer write ready interrupt, configure the DMA settings and enable the uSDHC DMA when sending the command with data transfer. The DDR_EN and AC12EN bits should be set. 

6. Wait for the Transfer Complete interrupt. 

7. Check the status bit to see if a write CRC error occurred or another error that occurred during the auto12 command sending and response receiving. 

#### 78.5.3.1.3 Write with Pause 

The write operation can be paused during the transfer. Instead of stopping the CLK at any time to pause all the operations, which is also inaccessible to the host driver, the driver can set the Stop At Block Gap Request (SABGREQ) bit in the Protocol Control register to pause the transfer between the data blocks. As there is no time-out condition in a write operation during the data blocks, a write to all types of cards can be paused in this way, and if the DATA0 line is not required to de-assert to release the busy state, no suspend command is needed. 

Similar to the flow described in Normal Write, the write with pause is shown with the same kind of write operation: 

1. Check the card status and wait until the card is ready for data. 

2. Set the card block length/size: 

   - For eMMC and SD cards, use SET_BLOCKLEN (CMD16). 

   - For SDIO cards or the I/O portion of SDCombo cards, use IO_RW_DIRECT(CMD52) to set the I/O Block Size bit field in the CCCR register (for function 0) or FBR register (for functions 1~7). 

3. Set the uSDHC block length register to be the same as the block length set for the card in step 2. 

4. Set the uSDHC number block register (NOB), where nob is 5, for instance. 

5. Disable the buffer write ready interrupt, configure the DMA settings and enable the uSDHC DMA when sending the command with data transfer. The AC12EN bit should also be set. 

6. Set the SABGREQ bit. 

7. Wait for the Transfer Complete interrupt. 

8. Clear the SABGREQ bit. 

9. Check the status bit to see if a write CRC error occurred. 

10. Set the CREQ bit to continue the write operation. 

11. Wait for the Transfer Complete interrupt. 

12. Check the status bit to see if a write CRC error occurred or some another error that occurred during the auto12 command sending and response receiving. 

The number of blocks left during the data transfer is accessible by reading the contents of the BLKCNT field in the Block Attribute register. As the data transfer and the setting of the SABGREQ bit are concurrent, and the delay of register read and the register setting, the actual number of blocks left may not be exactly the value read earlier. The host driver reads the value of BLKCNT after the transfer is paused and the Transfer Complete interrupt is received. 

It is also possible that the last block has begun when the Stop At Block Gap Request is sent to the buffer. In this case, the next block gap is the end of the transfer. These types of requests are ignored, the driver should treat these as a non-pause transfer, and deal with it as a common write operation. 

When the write operation is paused, the data transfer inside the host system is not stopped, and the transfer is active until the data buffer is full. Because of this, it is recommended to avoid using the Suspend command for the SDIO card. This is because when such a command is sent, uSDHC interprets the system that switches to another function on the SDIO card and flush the data buffer. uSDHC takes the Resume command as a normal command with data transfer, and it is left for the host driver to set all the relevant registers before the transfer is resumed. If there is only one block to send when the transfer is resumed, the MSBSEL and 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4465 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

BCEN bits of the Transfer Type register are set as well as the AC12EN bit. However, the uSDHC module automatically sends a CMD12 to mark the end of the multi-block transfer. 

#### 78.5.3.2 Block read 

Information about Normal read, DDR read, Read with Pause, and Delay Line (DLL) in Read Path are detailed in the sections below. 

#### 78.5.3.2.1 Normal read 

For block reads, the basic unit of data transfer is a block whose maximum size is stored in areas defined by the corresponding card specification. A CRC is appended to the end of each block, ensuring data transfer integrity. The CMD17, CMD18, CMD53, CMD60, CMD61, and so on, can initiate a block read. After completing the transfer, the card returns to the Transfer state. For multi blocks read, data blocks are continuously transferred until a stop command is issued. 

The software flow to read from a card that incorporates the internal DMA and the read operation is a multi-block read with the Auto CMD12 enabled. For the other two methods (by means of external DMA or CPU polling status with different transfer methods, the internal DMA parts should be removed and the alternative steps should be straightforward. 

The software flow to read from a card is described below: 

1. Check the card status and wait until card is ready for data. 

2. Set the card block length/size: 

   - For eMMC and SD cards, use SET_BLOCKLEN (CMD16). 

   - For SDIO cards or the I/O portion of SDCombo cards, use IO_RW_DIRECT(CMD52) to set the I/O Block Size bit field in the CCCR register (for function 0) or FBR register (for functions 1~7). 

3. Set the uSDHC block length register to be the same as the block length set for the card in step 2. 

4. Set the uSDHC number block register (NOB), where nob is 5, for instance. 

5. Disable the buffer read ready interrupt, configure the DMA settings, and enable the uSDHC DMA when sending the command with data transfer. The AC12EN bit should also be set. 

6. Wait for the Transfer Complete interrupt. 

7. Check the status bit to see if a read CRC error occurred, or another error occurred during the auto12 command sending and response receiving. 

#### 78.5.3.2.2 DDR read 

The uSDHC module supports dual data rate mode. 

The software flow to write to a card in the DDR mode is described below: 

1. Check the card status and wait until the card is ready for data. 

~~<mark>NOTE</mark>~~ 

For eMMC, block length can be set to only 512 bytes. 

2. Set the uSDHC number block register (NOB) where nob is 5, for instance. 

3. Set the eMMC to high-speed mode and use SWITCH (CMD6). 

4. Set the eMMC bus with 4-bit /8-bit DDR mode and use SWITCH(CMD6). 

5. Disable the buffer write ready interrupt, configure the DMA settings, and enable the uSDHC DMA when sending the command with data transfer. The DDR_EN and AC12EN bits should be set. 

6. Wait for the Transfer Complete interrupt. 

7. Check the status bit to see if a write CRC error occurred, or another error that occurred during the auto12 command sending and response receiving. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4466 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

#### 78.5.3.2.3 Read with Pause 

The read operation is not generally able to pause. Only the SDIO card (and SDCombo card working under I/O mode) supporting the Read Wait feature can pause during the read operation. If the SDIO card supports Read Wait (SRW bit in CCCR register is 1), the host driver can set the SABGREQ bit in the Protocol Control register to pause the transfer between the data blocks. Before setting the SABGREQ bit, ensure that the RWCTL bit in the Protocol Control register is set, otherwise uSDHC does not assert the Read Wait signal during the block gap and data corruption occurs. It is recommended to set the RWCTL bit after the Read Wait capability of the SDIO card is recognized. 

Similar to the flow described in Normal read, the read with pause is shown with the same kind of read operation: 

1. Check the SRW bit in the CCR register on the SDIO card to confirm that the card supports the Read Wait mode. 

2. Set the RWCTL bit. 

3. Check the card status and wait until the card is ready for data. 

4. Set the card block length/size: 

   - For eMMC and SD cards, use SET_BLOCKLEN (CMD16). 

   - For SDIO cards or the I/O portion of SDCombo cards, use IO_RW_DIRECT(CMD52) to set the I/O Block Size bit field in the CCCR register (for function 0) or FBR register (for functions 1~7). 

5. Set the uSDHC block length register to be the same as the block length set for the card in step 2. 

6. Set the uSDHC number block register (NOB), where nob is 5, for instance. 

7. Disable the buffer read ready interrupt, configure the DMA setting, and enable the uSDHC DMA when sending the command with data transfer. The AC12EN bit should also be set. 

8. Set the SABGREQ bit. 

9. Wait for the Transfer Complete interrupt. 

10. Clear the SABGREQ bit. 

11. Check the status bit to see if read CRC error occurred. 

12. Set the CREQ bit to continue the read operation. 

13. Wait for the Transfer Complete interrupt. 

14. Check the status bit to see if a read CRC error occurred, or another error occurred during the auto12 command sending and response receiving. 

Similar to the Write operation, it is possible to meet the ending block of the transfer when paused. In this case, uSDHC ignores the Stop At Block Gap Request and treats it as a command read operation. 

Unlike the write operation, there is no remaining data inside the buffer when the transfer is paused. All data received before the pause is transferred to the host system. No matter if the Suspend command is sent or not, the internal data buffer is not flushed. 

If the Suspend command is sent and the transfer is later resumed by means of a Resume command, uSDHC takes the command as a normal one accompanied with data transfer. It is left for the host driver to set all the relevant registers before the transfer is resumed. If there is only one block to send when the transfer is resumed, the MSBSEL and BCEN bits of the Transfer Type register are set, as well as the AC12EN bit. However, the uSDHC automatically sends CMD12 to mark the end of multi-block transfer. 

#### 78.5.3.2.4 Delay Line (DLL) in read path 

The DLL is newly added to assist in sampling read data. The DLL provides the ability to programmatically select a quantized delay (in fractions of the clock period) regardless of on-chip variations such as process, voltage, and temperature (PVT). 

The reasons why DLL is needed for uSDHC are these: 

- The path of read data traveling from card to host varies. 

- In the eMMC and SD cards DDR mode, the minimum input setup and hold time are both at 2.5 ns. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4467 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

The data sampling window is so small that the delay of loopback clock needs to be accurate and consistent regardless of PVT. The DLL takes the divided card_clk as the reference clock and loopback clock as the input clock. It then generates a delayed version of the input clock according to the programmed target delay. 

The DLL can be disabled or bypassed, and it can also be manually set for a fixed delay in the override mode. The override value set is the number of delay cells. In the override mode, there is no need to set the DLL_enable. Another DLL mode is target value mode. In this mode, the DLL automatically adjusts the number of delay cells according to the target value set by the user and PVT changes. Be aware that the target value is in units of 1/32 of the clock reference period. If the card_clk is 100Mhz, then the reference clock period is 10ns; setting target value of 16 means 5ns =(16/32)*10ns. The software can disable automatic update by the setting dll_gate_update bit. 

As you might change the frequency of card_clk from time to time by changing SDCLKFS[7:0]/DVS[3:0], the software must adjust the delay value to ensure it works correctly when the reference clock (card_clk) is changed. If DLL is to be used, make sure SDCLKFS is used (at least be set to divided by 2) so that the REF_CLK generated are the same frequency as card_clk. There are two DLLs, PARTS DLL and STROBE DLL. 

Step 1: Set the DLL_CTRL_RESET and DLL_CTRL_ENABLE fields 

Step 2: Configure the SDCLKFS[7:0] and DVS[3:0] 

Step 3: Wait until SDSTB is asserted 

Step 4: Clear the DLL_CTRL_RESET field 

Step 5: Wait until both the DLL_STS_SLV_LOCK and DLL_STS_REF_LOCK are asserted 

Step 6: Set the DLL_CTRL_SLV_FORCE_UPD 

Step 7: Clear the DLL_CTRL_SLV_FORCE_UPD 

~~<mark>NOTE</mark>~~ 

The software should make sure that the DLL_CTRL_SLV_FORCE_UPD lasts for at least one card_clk. So, the software may need to add some delay between step 6 and step 7. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4468-14.png)


<!-- Start of picture text -->
uSDHC SD/eMMC<br>8<br>Read Data Async DATA 3<br>Buffer<br>6 5 4<br>ipp_card_clk_in_dll<br>Card_clk Delay Line<br>ipp_card_clk_in<br>card_clk_pad<br>/2 1 2<br>DDR_EN<br><!-- End of picture text -->

Figure 503. DLL in read path 

#### 78.5.3.3 Suspend Resume 

The uSDHC module supports the Suspend Resume operations of SDIO cards, although slightly different than the suggested implementation of Suspend in the SDIO card specification. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4468 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

#### 78.5.3.3.1 Suspend 

After setting the SABGREQ bit, the host driver may send a Suspend command to switch to another function of the SDIO card. The uSDHC module does not monitor the content of the response, so it does not know if the Suspend command succeeded or not. Accordingly, it does not de-assert Read Wait for read pause. To solve this problem, the host driver does not mark the Suspend command as "Suspend", (that is, setting the CMDTYP bits to 01). Instead, the driver sends this command as if it were a normal command, and only when the command succeeds, and the BS bit is set in the response, can the Driver send another command marked as "Suspend" to inform uSDHC that the current transfer is suspended. Here is the sequence for the Suspend operation: 

1. Set the SABREQ bit to pause the current data transfer at block gap. 

2. After the BGE bit is set, send the Suspend command to suspend the active function. The CMDTYP bit field must be 2'b00. 

3. Check the BS bit of the CCCR in the response. If it is 1, repeat this step until the BS bit is cleared or abandon the suspend operation according to the Driver strategy. 

4. Send another normal I/O command to the suspended function. The CMDTYP of this command must be 2'b01, so uSDHC can detect this special setting and be informed that the paused operation has successfully suspended. If the paused transfer is a read operation, uSDHC stops driving DATA2 and goes to the idle state. 

5. Save the context registers in the system memory for later use, including the DMA System Address Register (for internal DMA operation), and the Block Attribute Register. 

6. Begin operation for another function on the SDIO card. 

#### 78.5.3.3.2 Resume 

To resume the data transfer, a Resume command is issued: 

1. To resume the suspended function, restore the context register with the saved value in step #5 of the Suspend operation. 

2. Send the Resume command: In the Transfer Type register, all the bit fields are set to the value as if this were another ordinary data transfer instead of a transfer resume (except the CMDTYP is set to 2'b10). 

3. If the Resume command has responded, the data transfer is resumed. 

#### 78.5.3.4 ADMA usage 

To use the ADMA in a data transfer, the host driver must prepare the correct descriptor chain prior to sending the read/write command. The steps to prepare the correct descriptor chain are these: 

1. Create a descriptor to set the data length that the current descriptor group is about to transfer. The data length should be even numbers of the block size. 

2. Create another descriptor to transfer the data from the address setting in this descriptor. The data address must be at a page boundary (4KB address aligned). 

3. If necessary, create a Link descriptor containing the address of the next descriptor. The descriptor group is created in steps 1 ~ 3. 

4. Repeat steps 1 ~ 3 until all descriptors are created. 

5. In the last descriptor, set the End flag to 1 and make sure the total length of all descriptors matches the product of the block size and block number configured in the Block Attribute Register. 

6. Set the ADMA System Address Register to the address of the first descriptor and set the DMAS field in the Protocol Control Register to 01 to select the ADMA. 

7. Issue a write or read command with the DMAEN bit set to 1 in the Transfer Type Register. 

Steps 1 ~ 5 are independent of step 6, so step 6 can finish before steps 1 ~ 5. Regarding the descriptor configuration, it is recommended not to use the Link descriptor as it requires extra system memory access. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4469 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

#### 78.5.3.5 Transfer error 

Information about CRC, Internal DMA, Transfer ADMA, and Auto CMD12 errors are detailed in the sections below. 

#### 78.5.3.5.1 CRC error 

It is possible at the end of a block transfer that a write CRC status error or read CRC error occurs. For this type of error, the latest block received is discarded. This is because the integrity of the data block is not guaranteed. It is recommended to discard the following data blocks and re-transfer the block from the corrupted one. For a multi-block transfer, the host driver issues a CMD12 to abort the current process and start the transfer by a new data command. In this scenario, even when the AC12EN and BCEND bits are set, uSDHC does not automatically send a CMD12 because the last block is not transferred. On the other hand, if it is within the last block that the CRC error occurs, an Auto CMD12 is sent by uSDHC. In this case, the host driver re-sends or re-obtains the last block with a single block transfer. 

#### 78.5.3.5.2 Internal DMA error 

During the data transfer with internal Simple DMA, if the DMA engine encounters an error on the AHB bus, the DMA operation is aborted, and the DMA error interrupt is sent to the host system. When acknowledged by such an interrupt, the host driver calculates the start address of data block in which the error occurs. The start address can be calculated by either: 

- Reading the DMA System Address register: The error occurs during the previous burst. Considering the block size, the previous burst length and the start address of the next burst transfer, it is straight forward to obtain the start address of the corrupted block. 

- Reading the BLKCNT field of the Block Attribute register: Considering the number of blocks left, the total number to transfer, the start address of transfer, and the size of each block, the start address of corrupted block can be determined.To use this method, MIX_CTRL[BCEN] bit has to be set to enable Block Attribute register update. 

When a DMA error occurs, it is recommended to abort the current transfer by means of a CMD12 (for multi block transfer), apply a reset for data, and restart the transfer from the corrupted block to recover from the error. 

#### 78.5.3.5.3 Transfer ADMA error 

There are three kinds of possible ADMA errors: The AHB transfer, invalid descriptor, and data-length mismatch. Whenever these errors occur, the DMA transfer stops and the corresponding error status bit is set. For acknowledging the status, the host driver should recover the error as shown below and re-transfer from the place of interruption. 

- AHB transfer error: Such errors may occur during data transfer or descriptor fetch. For either scenario, it is recommended to retrieve the transfer context, reset for the data part and re-transfer the block that was corrupted, or to the next block if no block is corrupted. 

- Invalid descriptor error: For such errors, it is recommended to retrieve the transfer context, reset for the data part and recreate the descriptor chain from the invalid descriptor and issue a new transfer. As the data to transfer now may be less than the previous setting, the data length configured in the new descriptor chain should match the new value. 

- Data-length mismatch error: It is similar to recover from this error. The Host Driver polls relating registers to retrieve the transfer context, apply a reset for the data part, configure a new descriptor chain and make another transfer if there is data left. Like the previous scenario of the invalid descriptor error, the data length must match the new transfer. 

#### 78.5.3.5.4 Auto CMD12 error 

After the last block of the multi-block transfer is sent or received, and the AC12EN bit is set when the data transfer is initiated by the data command, uSDHC automatically sends a CMD12 to the card to stop the transfer. When errors with this command occur, it is recommended to the host driver to deal with the situations in the following manner: 

- Auto CMD12 response time-out: It is not certain whether the command is accepted by the card or not. The host driver clears the auto CMD12 error status bits and re-send CMD12 until it is accepted by the card. 

- Auto CMD12 response CRC error: As the card responds to CMD12, it aborts the transfer. The host driver may ignore the error and clear the error status bit. 

- Auto CMD12 conflict error or not sent: The command is not sent; therefore, the host driver sends a CMD12 manually. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4470 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

#### 78.5.3.6 Card interrupt 

The external cards can inform the host controller by means of some special signals. For the SDIO card, it can be the low-level on the DATA1 line during some special period. The uSDHC module only monitors the DATA1 line and supports the SDIO interrupt. When the SDIO interrupt is captured by uSDHC, and the host system is informed by uSDHC asserting the uSDHC interrupt line, the interrupt service from the host driver is called. 

As the interrupt source is controlled by the external card, the interrupt from the SDIO card must be serviced before the CINT bit is cleared. Refer to Card interrupt handling for the card interrupt handling flow. 

### 78.5.4 Switch function 

A switch command is issued by the host driver to enable new features added to the eMMC and SD cards. The eMMC and SD cards can transfer data at bus widths other than 1-bit. Different speed modes are also defined. To enable these features, a switch command is issued by the host driver. 

For SDIO cards, the high-speed mode/DDR50/SDR50/SDR104 are enabled by writing the EHS bit in the CCCR register after the SHS bit is confirmed as high. For SD cards, the high-speed mode/DDR50/SDR50/SDR104 are queried and enabled by a CMD6 (with the mnemonic symbol as SWITCH_FUNC). For eMMC, the high-speed mode is queried by a CMD8 and enabled by a CMD6 (with the mnemonic symbol as SWITCH). 

The SDR4-bit, SDR8-bit, DDR4-bit, and DDR8-bit width of eMMC is also enabled by the SWITCH command, but with a different argument. 

These new functions can also be disabled by a software reset. For SDIO cards, it can be done by setting the RES bit in the CCCR register. For other cards, it can be accomplished by issuing a CMD0. This method of restoring to the normal mode is not recommended because a complete identification process is needed before the card is ready for data transfer. 

For the sake of simplicity, the following pseudocode examples do not show current capability check, which is recommended in the function switch process. 

#### 78.5.4.1 Query, enable, and disable SDIO high-speed mode 

```
enable_sdio_high_speed_mode(void)
{
send CMD52 to query bit SHS at address 0x13;
if (SHS bit is '0') report the SDIO card does not support high speed mode and return;
send CMD52 to set bit EHS at address 0x13 and read after write to confirm EHS bit is set;
change clock divisor value or configure the system clock feeding into uSDHC to generate the
card_clk of around 50MHz;
(data transactions like normal peers)
}
disable_sdio_high_speed_mode(void)
{
send CMD52 to clear bit EHS at address 0x13 and read after write to confirm EHS bit is cleared;
change clock divisor value or configure the system clock feeding into uSDHC to generate the
card_clk of the desired value below 25MHz;
(data transactions like normal peers)
}
```

#### 78.5.4.2 Query, enable, and disable SD high-speed mode/DDR50/SDR50/SDR104 

```
enable_sd_speed_mode(void)
{
set BLKCNT field to 1 (block), set BLKSIZE field to 64 (bytes);
send CMD6, with argument 0xFFFFFx and read 64 bytes of data accompanying the R1 response;(high speed
mode,x=1; SDR50,x=2; SDR104,x=3; DDR50,x=4;)
wait data transfer done bit is set;
check if the bit x of received 512 bits is set;
```

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4471 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

```
if (bit 401 is '0') report the SD card does not support high speed mode and return;
if (bit 402 is '0') report the SD card does not support SDR50 mode and return;
if (bit 403 is '0') report the SD card does not support SDR104 mode and return;
if (bit 404 is '0') report the SD card does not support DDR50 mode and return;
send CMD6, with argument 0x80FFFFFx and read 64 bytes of data accompanying the R1 response;(high
speed mode,x=1; SDR50,x=2; SDR104 x=3; DDR50 x=4;)
check if the bit field 379~376 is 0xF;
if (the bit field is 0xF) report the function switch failed and return;
change clock divisor value or configure the system clock feeding into uSDHC to generate the card_clk
of around 50MHz for high speed mode, 100MHz for SDR50, 200MHz for SDR104, 50MHz for DDR50;
(data transactions like normal peers)
}
disable_sd_speed_mode(void)
{
set BLKCNT field to 1 (block), set BLKSIZE field to 64 (bytes);
send CMD6, with argument 0x80FFFFF0 and read 64 bytes of data accompanying the R1 response;
check if the bit field 379~376 is 0xF;
if (the bit field is 0xF) report the function switch failed and return;
change clock divisor value or configure the system clock feeding into uSDHC to generate the
card_clk of the desired value below 25MHz;
(data transactions like normal peers)
}
```

#### 78.5.4.3 Query, enable, and disable eMMC high-speed mode 

```
enable_mmc_high_speed_mode(void)
{
send CMD9 to get CSD value of eMMC;
check if the value of SPEC_VER field is 4 or above;
if (SPEC_VER value is less than 4) report the eMMC does not support high speed mode and return;
set BLKCNT field to 1 (block), set BLKSIZE field to 512 (bytes);
send CMD8 to get EXT_CSD value of eMMC;
extract the value of CARD_TYPE field to check the 'high speed mode' in this eMMC is 26MHz or
52MHz;
send CMD6 with argument 0x1B90100;
send CMD13 to wait card ready (busy line released);
send CMD8 to get EXT_CSD value of eMMC;
check if HS_TIMING byte (byte number 185) is 1;
if (HS_TIMING is not 1) report eMMC switching to high speed mode failed and return;
change clock divisor value or configure the system clock feeding into uSDHC to generate the
card_clk of around 26MHz or 52MHz according to the CARD_TYPE;
(data transactions like normal peers)
}
disable_mmc_high_speed_mode(void)
{
send CMD6 with argument 0x2B90100;
set BLKCNT field to 1 (block), set BLKSIZE field to 512 (bytes);
send CMD8 to get EXT_CSD value of eMMC;
check if HS_TIMING byte (byte number 185) is 0;
if (HS_TIMING is not 0) report the function switch failed and return;
change clock divisor value or configure the system clock feeding into uSDHC to generate the
card_clk of the desired value below 20MHz;
(data transactions like normal peers)
}
```

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4472 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

#### 78.5.4.4 Set eMMC bus width 

```
change_mmc_bus_width(void)
{
send CMD9 to get CSD value of eMMC;
check if the value of SPEC_VER field is 4 or above;
if (SPEC_VER value is less than 4) report the eMMC does not support multiple bit width and return;
send CMD6 with argument 0x3B70x00; (8-bit(dual data rate), x=6; 4-bit(dual data rate), x=5;8-bit,
x=2; 4-bit, x=1; 1-bit, x=0)
send CMD13 to wait card ready (busy line released);
(data transactions like normal peers)
}
```

### 78.5.5 ADMA operation 

Here are the codes for the ADMA1 and ADMA2 operations. 

#### 78.5.5.1 ADMA1 operation 

```
Set_adma1_descriptor
{
if (to start data transfer) {
// Make sure the address is 4KB align.
Set 'Set' type descriptor;
{
Set Act bits to 01;
Set [31:12] bits data length (byte unit);
}
Set 'Tran' type descriptor;
{
Set Act bits to 10;
Set [31:12] bits address (4KB align);
}
}
else if (to fetch descriptor at non-continuous address) {
Set Act bits to 11;
Set [31:12] bits the next descriptor address (4KB aligned);
}
else { // other types of descriptor
Set Act bits accordingly
}
if (this descriptor is the last one) {
Set End bit to 1;
}
if (to generate interrupt for this descriptor) {
Set Int bit to 1;
}
Set Valid bit to 1;
}
```

#### 78.5.5.2 ADMA2 operation 

```
Set_adma2_descriptor
{
if (to start data transfer) {
// Make sure the address is a 32-bit boundary (lower 2-bit are always '00').
Set higher 32-bit of descriptor for this data transfer initial address;
Set [31:16] bits data length (byte unit);
```

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4473 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

```
Set Act bits to '10';
}
else if (to fetch descriptor at non-continuous address) {
Set Act bits to '11';
// Make sure the address is 32-bit boundary (lower 2-bit are always set to '00').
Set higher 32-bit of descriptor for the next descriptor address;
}
else { // other types of descriptor
Set Act bits accordingly
}
if (this descriptor is the last one) {
Set 'End' bit '1';
}
if (to generate interrupt for this descriptor) {
Set 'Int' bit '1';
}
Set the 'Valid' bit to '1';
}
```

### 78.5.6 Fast boot operation 

#### 78.5.6.1 Normal fast boot flow 

Here are the steps for normal fast boot flow: 

1. Software must configure the SYS_CTRL[INITA] bit to make sure that 74 card clocks are finished. 

2. Software must configure the eMMC Boot Register (offset 0xc4) bit 6 to 1 (enable boot), and bit 5 to 0 (normal fast boot), and bit 4 to select the ack mode. If the data is sent through the DMA mode, the software should configure bit 7 to enable the automatic stop at block gap feature, and configure bit 3-bit 0 to select the ack timeout value according to the SD CLK frequency. 

3. Software then needs to configure the Block Attributes Register to set the block size and count. If in DDR fast boot mode, the block size only can be configured to 512 bytes. 

4. Software must configure the Protocol control register to set Data Transfer Width (DTW). If in the DDR fast boot mode, DTW only can be configured to 4-bit/8-bit dataline mode. 

5. Software needs to configure the Command Argument Register to set argument if needed (no need in normal fast boot). 

6. Software must configure the Transfer Type Register to start the boot process. In normal boot mode, CMDINX, CMDTYP, RSPTYP, CICEN, CCCEN, AC12EN, BCEN and DMAEN retain the default value, where DPSEL bit is set to 1, DTDSEL is set to 1 and MSBSEL is set to 1. 

7. DMAEN should be configured as 0 in the polling mode and if BCEN is configured as 1, it is recommended to configure the number of blocks in the Block Attributes Register to the maximum value. If in DDR fast boot mode, DDR_EN needs to be set to 1. 

8. When step 6 is configured, the boot process begins. The software needs to poll the data buffer ready status to read the data from the buffer in time. If a boot timeout happens (ack times out or the first data read times out), an interrupt is triggered, and the software must configure eMMC Boot Register to bit 6 to 0 to disable boot. This makes CMD high, then after at least 56 clocks, it is ready to begin a normal initialization process. 

9. If there is no timeout, software needs to determine when the data read is finished and then configure eMMC Boot Register bit 6 to 0 to disable boot. This render CMD line high and command completed asserted. After at least 56 clocks, it is ready to begin the normal initialization process. 

10. You must reset the host and begin the normal process. 

#### 78.5.6.2 Alternative fast boot flow 

Here are the steps for alternative fast boot flow: 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4474 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

1. Software needs to configure SYS_CTRL[INITA] to make sure 74 card clocks are finished. 

2. Software needs to configure eMMC Boot Register (offset 0xc4) bit 6 to 1 (enable boot), and bit 5 to 1 (alternative boot), and bit 4 to select the ack mode or not. If data needs to be sent through the DMA mode, then configure bit 7 to enable the automatic stop at block gap feature. Software should also configure bit 3-bit 0 to select the ack timeout value according to the SD clock frequency. 

3. Software then needs to configure the Block Attributes Register to set the block size and count. If in the DDR fast boot mode, the block size only can be configured to 512 bytes. 

4. Software needs to configure the Protocol control register to set the data transfer width (DTW). If in the DDR fast boot mode, DTW only can be configured to 4-bit/8-bit dataline mode. 

5. Software needs to configure Command Argument Register to set argument to 0xFFFFFFFA. 

6. Software needs to configure the Transfer Type Register to start the boot process by CMD0 with the 0xFFFFFFFA argument. In alternative boot, CMDINX, CMDTYP, RSPTYP, CICEN, CCCEN, AC12EN, BCEN, and DMAEN retain the default value. DPSEL bit is set to 1, DTDSEL is set to 1, and MSBSEL is set to 1. Note DMAEN should be configured as 0 in the polling mode, and if BCEN is configured as 1 in polling mode, it is recommended to configure the block count in the Block Attributes Register to the maximum value. If in the DDR fast boot mode, DDR_EN needs to be set to 1. 

7. When step 6 is configured, the boot process begins. Software needs to poll the data buffer ready status to read the data from the buffer in time. If there is a boot timeout (ack data timeout in 50ms or data timeout in 1s), the host sends out the interrupt and the software needs to send CMD0 with reset and then configure the boot enable bit to 0 to stop this process. 

8. If there is no time out, the software needs to decide when to stop the boot process, and send out the CMD0 with reset and then after the command is completed, configure the eMMC Boot Register bit 6 to stop the process. After 8 clocks from the command completion, the slave (card) is ready for the identification step. 

9. You must reset the host and begin the normal process. 

#### 78.5.6.3 Fast boot application case (in DMA mode) 

In the boot application case, because the image destination and the image size are contained in the beginning of the image, it is necessary to switch DMA parameters on the fly during eMMC fast boot. 

In fast boot, the host can use Advanced DMA2 (ADMA2) with two destinations. 

The detailed flow is described below: 

1. The software needs to configure INIT_ACTIVE bit (system control register bit 27) to make sure that 74 card clocks are finished. 

2. The software needs to configure the eMMC Boot Register (offset 0xc4) bit 6 to 1 (enable boot); and bit 5 to 0 (normal fast boot) or 1 (alternative boot); and bit 4 to select the ack mode. In DMA mode, configure bit 7 to 1 to enable the automatic stop at block gap feature. Also configure bits[31-16] to set the (BLK_CNT - VALUE1). Here VALUE1 is the value of the block count that needs to transfer the first time, so that the host stops at the block gap when the uSDHC controller gets VAULE1 blocks from the device. Also, configure bits[3-0] to select the ack timeout value according to the SD clock frequency. 

3. The software then needs to configure the Block Attributes Register to set block size and count. If in DDR fast boot mode, the block size only can be configured to 512 bytes. In DMA mode, it is recommended to set the block count (BLK_CNT) to the max value (16'hffff). 

4. The software needs to configure Protocol Control Register to set DTW (data transfer width). If in DDR fast boot mode, the DTW only can be configured to 4-bit/8-bit dataline mode. 

5. Software enable ADMA2 by configuring Protocol Control Register bits [9-8]. 

6. The software needs to set at least three pairs of ADMA2 descriptor in boot memory (that is, in IRAM, at least six words). The first pair descriptor defines the start address (that is, IRAM) and data length (that is,512byte*VALUE1) of the first part boot code. The software also needs to set the second pair descriptor, the second start address (any value that 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4475 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

is writable), and data length is suggested to set 1~2word (record as VALUE2). Note that the second couple desc also transfers useful data even at lease 1 word, because our ADMA2 cannot support 0 data_length data transfer descriptor. 

7. The software needs to configure Command Argument Register to set argument to 0xFFFFFFFA in alternative fast boot and do not need to be set in normal fast boot. 

8. The software needs to configure Transfer Type Register to start the boot process. CMDINX, CMDTYP, RSPTYP, CICEN, CCCEN, AC12EN, BCEN, and DMAEN retain the default value. DPSEL bit is set to 1, DTDSEL is set to 1, and MSBSEL is set to 1. DMAEN is configured as 1 in the DMA mode. And, if BCEN is configured as 1, then configure blk no in Bock Attributes Register to the max value. And, if in the DDR fast boot mode, DDR_EN needs to be set to 1. 

9. When step 8 is configured, boot process begins, the first VALUE1 block number data gets transferred. The software needs to poll the TC bit (bit1 in Interrupt Status Register) to determine first transfer is ended. Also, the software needs to polling the BGE bit (bit2 in Interrupt Status Register) to determine if the first transfer stops at the block gap. 

10. When TC and BGE bits are set to 1, the software can analyze the first code of VALUE1 block, initializes the new memory device, if required, and sets the third pair of descriptors to define the start address and length of the remaining part of the boot code (VALUE3, the remain boot code block). Remember to set the last descriptor with END. 

11. The software needs to configure the eMMC Boot Register (offset 0xc4) again. Set bit 6 to 1 (enable boot); and bit 5 to 0 (normal fast boot), to 1 (alternative boot); and bit 4 to select the ack mode or not. In the DMA mode, configure bit 7 to 1 for enabling the automatically stop at block gap feature. Also, configure bit31-bit16 to set the (BLK_CNT - (VALUE1+1+VALUE3)), that host stops at block gap when the uSDHC controller gets (VALUE1+1+VALUE3)) blocks from device totally include the blocks received in step 9. And need to configure bit 3-bit0 to select the ack timeout value according to the sd clk frequency. Note that the software does not need to configure the BLK_CNT again, because it is counted down automatically by the uSDHC controller. 

12. The software needs to clear the TC and BGE bits and the software needs to clear SABGREQ (bit 16 in the Protocol control register) and set CREQ (bit17 in the Protocol control register) to 1 to resume the data transfer. Host transfers the VALUE2 and VALUE3 data to the destination that is set by descriptor. 

13. The software needs to do poll BGE bit to determine if the fast boot is over. 

Note: 

- When ADMA boot flow starts, for uSDHC, it is like a normal ADMA read operation. So, set ADMA2 descriptor as the normal ADMA2 transfer. 

- Need a few words length memory to keep descriptor. 

- For the 1~2-word data in second descriptor setting, it is a useful data, so the software needs to deal the data because of the application case. 

## 78.6 Software restrictions 

### 78.6.1 Initialization active 

The driver cannot set INITA bit in System Control register when any of the command line or data lines are active, so the driver must ensure both CDIHB and CIHB bits are cleared. 

### 78.6.2 Software polling procedure 

For polling read or write, after the software begins a buffer read or write, it must access exactly the number of times as the values set in the Watermark Level Register; moreover, if the block size is not a multiple of the value in the Watermark Level Register (read and write respectively), the software must access exactly the remaining number of words at the end of each block. For example, for a read operation, if the RD_WML is 4, indicating the watermark level is 16 bytes, block size is 40 bytes, and the block number is 2, then the access times for the burst sequence in the whole transfer process must be 4, 4, 2, 4, 4, 2. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4476 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

### 78.6.3 Suspend operation 

To suspend the data transfer, the software must inform uSDHC that the suspend command is successfully accepted. To achieve this, after the Suspend command is accepted by the SDIO card, software must send another normal command marked as suspend command (CMDTYP bits set as '01') to inform uSDHC that the transfer is suspended. 

If software needs to resume the suspended transfer, it should read the value in BLKCNT register to save the remaining number of blocks before sending the normal command marked as suspend, otherwise on sending such a 'suspend' command, uSDHC treats the current transfer is aborted and change the BLKCNT register to its original value, instead of retaining the remaining number of blocks. 

### 78.6.4 Data length setting 

For either ADMA (ADMA1 or ADMA2) transfer, the data in the data buffer must be word aligned, so the data length set in the descriptor must be a multiple of 4. 

ADMA1 is 4KB aligned. 

### 78.6.5 (A)DMA address setting 

To configure the ADMA1/ADMA2/DMA address register, when TC bit is set, the register always updates itself with the internal address value to support dynamic address synchronization, so the software must ensure that the TC bit is cleared prior to configuring the ADMA1/ADMA2/DMA address register. 

### 78.6.6 Data port access 

Data port does not support parallel access. For example, during an internal DMA access, it is not allowed to write any data to the data port by CPU; or during a CPU read operation, it is also prohibited to write any data to the data port, by either CPU or internal DMA. Otherwise the data is corrupted inside the uSDHC buffer. 

### 78.6.7 Change clock frequency 

The uSDHC module does not automatically gate off the card clock when the host driver changes the clock frequency. To prevent possible glitch on the card clock, clear the FRC_SDCLK_ON bit when changing the clock divisor value (SDCLKFS or DVS in System Control Register) or setting the RSTA bit. 

Also, before changing the clock divisor value, the host driver should make sure that the SDSTB bit is high. 

### 78.6.8 Multi-block read 

For pre-defined multi-block read operation, that is, the number of blocks to read has been defined by previous CMD23 for eMMC, or pre-defined number of blocks in CMD53 for SDIO/SDCombo, or whatever multi-block read without abort command at card side, an abort command, either automatic or manual CMD12/CMD52, is still required by uSDHC after the pre-defined number of blocks are done, to drive the internal state machine to idle mode. In this case, the card may not respond to this extra abort command and uSDHC gets response timeout. It is recommended to manually send an abort command with RSPTYP[1:0] both bits cleared. 

## 78.7 uSDHC memory map/register definition 

### 78.7.1 uSDHC register descriptions 

This section includes the module memory map and detailed descriptions of all registers. 

See the table below for the register memory map of uSDHC. All these registers only support 32-bit accesses. 

~~<mark>NOTE</mark>~~ 

The uSDHC registers are 32-bit wide and only support 32-bit access. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4477 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

#### 78.7.1.1 uSDHC memory map 

usdhc base address: 404E_4000h 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|0h|DMA System Address (DS_ADDR)|32|RW|0000_0000h|
|4h|Block Attributes (BLK_ATT)|32|RW|0001_0000h|
|8h|Command Argument (CMD_ARG)|32|RW|0000_0000h|
|Ch|Command Transfer Type (CMD_XFR_TYP)|32|RW|0000_0000h|
|10h|Command Response0 (CMD_RSP0)|32|RO|0000_0000h|
|14h|Command Response1 (CMD_RSP1)|32|RO|0000_0000h|
|18h|Command Response2 (CMD_RSP2)|32|RO|0000_0000h|
|1Ch|Command Response3 (CMD_RSP3)|32|RO|0000_0000h|
|20h|Data Buffer Access Port (DATA_BUFF_ACC_PORT)|32|RW|0000_0000h|
|24h|Present State (PRES_STATE)|32|RO|See<br>description|
|28h|Protocol Control (PROT_CTRL)|32|RW|0880_0020h|
|2Ch|System Control (SYS_CTRL)|32|RW|0080_800Fh|
|30h|Interrupt Status (INT_STATUS)|32|W1C|0000_0000h|
|34h|Interrupt Status Enable (INT_STATUS_EN)|32|RW|0000_0000h|
|38h|Interrupt Signal Enable (INT_SIGNAL_EN)|32|RW|0000_0000h|
|3Ch|Auto CMD12 Error Status (AUTOCMD12_ERR_STATUS)|32|RW|0000_0000h|
|40h|Host Controller Capabilities (HOST_CTRL_CAP)|32|RW|07F3_B407h|
|44h|Watermark Level (WTMK_LVL)|32|RW|0810_0810h|
|48h|Mixer Control (MIX_CTRL)|32|RW|8000_0000h|
|50h|Force Event (FORCE_EVENT)|32|WORZ|0000_0000h|
|54h|ADMA Error Status (ADMA_ERR_STATUS)|32|RO|0000_0000h|
|58h|ADMA System Address (ADMA_SYS_ADDR)|32|RW|0000_0000h|
|60h|DLL (Delay Line) Control (DLL_CTRL)|32|RW|0000_0000h|
|64h|DLL Status (DLL_STATUS)|32|RO|0000_0200h|
|68h|CLK Tuning Control and Status (CLK_TUNE_CTRL_STATUS)|32|RW|0000_0000h|
|C0h|Vendor Specific Register (VEND_SPEC)|32|RW|3000_7809h|
|C4h|eMMC Boot (MMC_BOOT)|32|RW|0000_0000h|
|C8h|Vendor Specific 2 Register (VEND_SPEC2)|32|RW|0001_9006h|
|CCh|Tuning Control (TUNING_CTRL)|32|RW|0021_2800h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4478 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

#### 78.7.1.2 DMA System Address (DS_ADDR) 

##### Offset 

|Register|Offset|
|---|---|
|DS_ADDR|0h|



##### Function 

This register contains the physical system memory address used for DMA transfers. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||DS_A|DDR||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||||||DS_A|DDR|||||||Res|erved|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-2|DMA system address|
|DS_ADDR|This field contains the memory address for a DMA transfer. Because the address must be word (4 bytes)<br>aligned, the least 2 bits are reserved, always 0. When uSDHC stops a DMA transfer, this field points to<br>the system address of the next contiguous data position. It can be accessed only when no transaction is<br>executing (that is, after a transaction has stopped). Read operation during transfers may return an invalid<br>value. The host driver initializes this field before starting a DMA transaction. After DMA has stopped, the<br>system address of the next contiguous data position can be read from this field.<br>This field is protected during a data transfer. When data lines are active, write to this field is ignored. The<br>host driver waits until the DLA field in the Present State register is cleared, before writing to this field.<br>The uSDHC internal DMA does not support a virtual memory system. It only supports continuous physical<br>memory access. Also, because AHB burst limitations, if the burst must cross the 1 KB boundary, uSDHC<br>automatically changes SEQ burst type to NSEQ.<br>Because this field supports dynamic address reflecting, when TC field is set, it automatically alters the value<br>of internal address counter, so the software cannot change this field when TC field is set. Such restriction<br>is also listed inSoftware restrictions.|
|1-0<br>—|Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4479 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

#### 78.7.1.3 Block Attributes (BLK_ATT) 

##### Offset 

|Register|Offset|
|---|---|
|BLK_ATT|4h|



##### Function 

This register is used to configure the number of data blocks and the number of bytes in each block. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4480-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>BLKCNT<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>BLKSIZE<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-16|Blocks count for current transfer|
|BLKCNT|This field is enabled when the Block Count Enable field in the Transfer Mode register is set to 1 and is valid<br>only for multiple block transfers. For single block transfer, this field always reads as 1. The host driver sets<br>this field to a value between 1 and the maximum block count. The uSDHC module decrements the block<br>count after each block transfer and stops when the count reaches zero. Setting the block count to zero<br>results in no data blocks being transferred.|
||This field should be accessed only when no transaction is executing (that is, after transactions are<br>stopped). During data transfer, read operations on this field may return an invalid value and write operations<br>are ignored.|
||When saving transfer content because of a Suspend command, the number of blocks yet to be transferred<br>can be determined by reading this field. The reading of this field should be applied after transfer is paused<br>by stop at block gap operation and before sending the command marked as suspend. This is because when<br>the Suspend command is sent out, uSDHC treats the current transfer as aborted and change the BLKCNT<br>field back to its original value instead of keeping the dynamical indicator of the remaining block count.<br>When restoring transfer content prior to issuing a Resume command, the host driver restores the previously<br>saved block count.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4480 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||Although the BLKCNT field is 0 after reset, the read of reset value is 0x1. This is because<br>when MSBSEL field is indicating a single block transfer, the read value of BLKCNT is<br>always 1.<br>~~NOTE~~|
||0000_0000_0000_0000b - Stop count<br>0000_0000_0000_0001b - 1 block<br>0000_0000_0000_0010b - 2 blocks<br>1111_1111_1111_1111b - 65535 blocks|
|15-13<br>—|Reserved|
|12-0|Transfer block size|
|BLKSIZE|This field specifies the block size for block data transfers. Values ranging from 1 byte up to the<br>maximum buffer size can be set. It can be accessed only when no transaction is executing (that is,<br>after a transaction has stopped). Read operations during transfers may return an invalid value, and write<br>operations are ignored.<br>0_0000_0000_0000b - No data transfer<br>0_0000_0000_0001b - 1 byte<br>0_0000_0000_0010b - 2 bytes<br>0_0000_0000_0011b - 3 bytes<br>0_0000_0000_0100b - 4 bytes<br>0_0001_1111_1111b - 511 bytes<br>0_0010_0000_0000b - 512 bytes<br>0_1000_0000_0000b - 2048 bytes|
||1_0000_0000_0000b - 4096 bytes|



#### 78.7.1.4 Command Argument (CMD_ARG) 

##### Offset 

|Register|Offset|
|---|---|
|CMD_ARG|8h|



##### Function 

This register contains the SD/eMMC command argument. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4481 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4482-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>CMDARG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>CMDARG<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Command argument|
|CMDARG|The SD/eMMC command argument is specified as bits 39-8 of the command format in the SD or eMMC<br>specification. This field is write protected when the Command Inhibit (CMD) field in the Present State<br>register is set.|



#### 78.7.1.5 Command Transfer Type (CMD_XFR_TYP) 

##### Offset 

|Register|Offset|
|---|---|
|CMD_XFR_TYP|Ch|



##### Function 

This register is used to control the operation of data transfers. The host driver sets this register before issuing a command followed by a data transfer or before issuing a Resume command. To prevent data loss, uSDHC prevents writing to the bits, which are involved in the data transfer of this register, when data transfer is active. These fields are DPSEL, MBSEL, DTDSEL, AC12EN, BCEN, and DMAEN. 

The host driver checks the Command Inhibit DAT field (PRES_STATE[CDIHB]) and the Command Inhibit CMD field (PRES_STATE[CIHB]) in the Present State register before writing to this register. When the CDIHB field in the Present State register is set, any attempt to send a command with data by writing to this register is ignored; when the CIHB field is set, any write to this register is ignored. 

On sending commands with data transfer involved, it is mandatory that the block size is non-zero. Block count must also be non-zero, or indicated as a single block transfer (bit 5 of this register is '0' when written), or block count is disabled (bit 1 of this register is '0' when written), otherwise uSDHC ignores the sending of this command and do nothing. For write command, with all above restrictions, it is also mandatory that the write protect switch is not active (PRES_STATE[WPSPL] field of Present State register is '1'); otherwise, uSDHC also ignores the command. 

If the commands with data transfer do not receive the response in 64 clock cycles, that is, if response time-out happens, uSDHC treats the external device, does not accept the command, and aborts the data transfer. In this scenario, the driver should issue the command again to retry the transfer. It is also possible that for some reason the card responds to the command but uSDHC 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4482 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

does not receive the response, and if it is internal DMA (either simple DMA or ADMA) read operation, the external system memory is over-written by the internal DMA with data sent back from the card. 

The table below shows the summary of how register settings determine the type of data transfer. 

Table 682. Transfer type register setting for various transfer types 

|Multi/single block select|Block count enable|Block count|Function|
|---|---|---|---|
|0|Do not care|Do not care|Single transfer|
|1|0|Do not care|Infinite transfer|
|1|1|Positive number|Multiple transfer|
|1|1|Zero|No data transfer|



The table below shows the relationship between the Command Index Check Enable and the Command CRC Check Enable, regarding the Response Type bits as well as the name of the response type. 

Table 683. Relationship between parameters and the name of the response type 

|Response type|Index check enable|CRC check enable|Name of response type|
|---|---|---|---|
|00|0|0|No response|
|01|0|1|R2|
|10|0|0|R3, R4|
|10|1|1|R1, R5, R6|
|11|1|1|R1b,R5b|



- In the SDIO specification, response type notation for R5b is not defined. R5 includes R5b in the SDIO specification, but R5b is defined in this specification to specify that uSDHC checks the busy status after receiving a response. For example, usually CMD52 is used with R5, but the I/O abort command is used with R5b. 

- The CRC fields for R3 and R4 are expected to be all 1 bits. The CRC check is disabled for these response types. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4483-12.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 DPSE CCCE Reserv<br>CMDINX  CMDTYP  CICEN  RSPTYP<br>W L  N  ed<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 AC23E NIBBL MSBS DTDS DDR_ AC12E DMAE<br>BCEN<br>W N  E_... EL  EL  EN  N  N<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4483 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Fields 

|Field<br>31-30<br>—|Function<br>Reserved|
|---|---|
|29-24<br>CMDINX|Command index<br>These fields are set to the command number that is specified in bits 45-40 of the command-format in the SD<br>Memory Card Physical Layer Specification and SDIO Card Specification.|
|23-22<br>CMDTYP|Command type<br>There are three types of special commands: Suspend, Resume, and Abort. These fields are set to 00b for<br>all other commands.<br>• Suspend command: If the Suspend command succeeds, uSDHC assumes that the card bus has<br>been released and that it is possible to issue the next command that uses the DATA line. Because<br>uSDHC does not monitor the content of command response, it does not know if the Suspend<br>command succeeded or not. It is the host driver's responsibility to check the status of the Suspend<br>command and send another command marked as Suspend to inform uSDHC that a Suspend<br>command was successfully issued. SeeSuspend Resumefor more details. After the end bit of<br>command is sent, uSDHC deasserts Read Wait for read transactions and stops checking busy for<br>write transactions. In a 4-bit mode, the interrupt cycle starts. If the Suspend command fails, uSDHC<br>maintains its current state, and the host driver restarts the transfer by setting the Continue Request<br>field in the Protocol Control register.<br>• Resume command: The host driver re-starts the data transfer by restoring the registers saved before<br>sending the Suspend command and then sends the Resume command. The uSDHC module checks<br>for a pending busy state before starting write transfers.<br>• Abort command: If this command is set when executing a read transfer, uSDHC stops reads to the<br>buffer. If this command is set when executing a write transfer, uSDHC stops driving the DATA line.<br>After issuing the Abort command, the host driver should issue a software reset (Abort Transaction).<br>00b - Normal other commands<br>01b - Suspend CMD52 for writing bus suspend in CCCR<br>10b - Resume CMD52 for writing function select in CCCR<br>11b - Abort CMD12, CMD52 for writing I/O Abort in CCCR|
|21<br>DPSEL|Data present select<br>This field is set to 1 to indicate that data is present and is transferred using the DATA line. It is set to 0 for<br>the following:<br>• Commands using only the CMD line (for example, CMD52)<br>• Commands with no data transfer, but using the busy signal on DATA0 line (R1b or R5b (for<br>example, CMD38))<br>In resume command, this field is set, and other bits in this register is set the same as when<br>the transfer was initially launched. When the write protect switch is on, (that is, the WPSPL<br>field is active as '0'), any command with a write operation ignored. When this field is set,<br>while the DTDSEL field is 0, writes to the register Transfer Type are ignored.<br>~~NOTE~~|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4484 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - No data present<br>1b - Data present|
|20<br>CICEN|Command index check enable<br>If this field is set to 1, uSDHC checks the Index field in the response to see if it has the same value as the<br>command index. If it is not, it is reported as a Command Index Error. If this field is set to 0, the Index field<br>is not checked.<br>0b - Disable command index check<br>1b - Enables command index check|
|19<br>CCCEN|Command CRC check enable<br>If this field is set to 1, uSDHC checks the CRC field in the response. If an error is detected, it is reported as<br>a Command CRC Error. If this field is set to 0, the CRC field is not checked. The number of bits checked<br>by the CRC field value changes according to the length of the response. See RSPTYP[1:0] andCommand<br>Transfer Type (CMD_XFR_TYP).<br>0b - Disables command CRC check<br>1b - Enables command CRC check|
|18<br>—|Reserved|
|17-16<br>RSPTYP|Response type select<br>00b - No response<br>01b - Response length 136<br>10b - Response length 48<br>11b - Response length 48, check busy after response|
|15-8<br>—|Reserved|
|7<br>AC23EN|AC23EN<br>This field is read/write whenVEND_SPEC[CMD_BYTE_EN]is enabled; otherwise, this field is read-only.<br>When this field is set to 1, the host controller issues a CMD23 automatically before issuing a command<br>specified in the Command Register.<br>0b - Disable<br>1b - Enable|
|6|NIBBLE_POS|
|NIBBLE_POS|This field indicates the nibble position in the DDR 4-bit mode. This field is read/write when<br>VEND_SPEC[CMD_BYTE_EN]is enabled; otherwise, this field is read-only. 0- the sequence is 'odd<br>high nibble -> even high nibble -> odd low nibble -> even low nibble'; 1- the sequence is 'odd high nibble -><br>odd low nibble -> even high nibble -> even low nibble'.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4485 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Disable<br>1b - Enable|
|5|MSBSEL|
|MSBSEL|This field enables multiple block DATA line data transfers. This field is read/write when<br>VEND_SPEC[CMD_BYTE_EN]is enabled; otherwise, this field is read-only. For any other commands, this<br>field can be set to 0. If this field is 0, it is not necessary to set the Block Count register. SeeCommand<br>Transfer Type (CMD_XFR_TYP).<br>0b - Disable<br>1b - Enable|
|4|DTDSEL|
|DTDSEL|This field defines the direction of DATA line data transfers. This field is read/write when<br>VEND_SPEC[CMD_BYTE_EN]is enabled; otherwise, this field is read-only. The field is set to 1 by<br>the host driver to transfer data from the SD card to uSDHC and is set to 0 for all other commands.<br>0b - Disable<br>1b - Enable|
|3<br>DDR_EN|DDR_EN<br>Dual data rate mode selection. This field is read/write whenVEND_SPEC[CMD_BYTE_EN]is enabled;<br>otherwise, this field is read-only.<br>0b - Disable<br>1b - Enable|
|2|AC12EN|
|AC12EN|Multiple block transfers for memory require a CMD12 to stop the transaction. This field is read/write when<br>VEND_SPEC[CMD_BYTE_EN]is enabled; otherwise, this field is read-only. When this field is set to 1,<br>uSDHC issues a CMD12 automatically when the last block transfer has completed. The host driver is not set<br>this field to issue commands that do not require CMD12 to stop a multiple block data transfer. In particular,<br>secure commands defined in File Security Specification (see reference list) do not require CMD12. In single<br>block transfer, uSDHC ignores this field no matter it is set or not.<br>0b - Disable<br>1b - Enable|
|1<br>BCEN|BCEN<br>This field is used to enable the Block Count register, which is only relevant for multiple block transfers. This<br>field is read/write whenVEND_SPEC[CMD_BYTE_EN]is enabled; otherwise, this field is read-only. When<br>this field is 0, the internal counter for block is disabled, which is useful in executing an infinite transfer.<br>0b - Disable<br>1b - Enable|
|0|DMAEN|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4486 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|DMAEN|This field enables DMA functionality. This field is read/write whenVEND_SPEC[CMD_BYTE_EN]is<br>enabled; otherwise, this field is read-only. If this field is set to 1, a DMA operation begins when the host driver<br>sets the DPSEL field of this register. Whether the simple DMA or the advanced DMA is active depends on<br>the DMA Select field of the Protocol Control register.|
||0b - Disable|
||1b - Enable|



#### 78.7.1.6 Command Response0 (CMD_RSP0) 

##### Offset 

|Register|Offset|
|---|---|
|CMD_RSP0|10h|



##### Function 

This register is used to store part 0 of the response bits from the card. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||CMD|RSP0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||CMD|RSP0||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-0|Command response 0|
|CMDRSP0|SeeCommand Response3 (CMD_RSP3)for the mapping of command responses from the SD bus to this<br>field for each response type.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4487 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

#### 78.7.1.7 Command Response1 (CMD_RSP1) 

##### Offset 

|Register|Offset|
|---|---|
|CMD_RSP1|14h|



##### Function 

This register is used to store part 1 of the response bits from the card. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4488-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R CMDRSP1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R CMDRSP1<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Command response 1|
|CMDRSP1|SeeCommand Response3 (CMD_RSP3)for the mapping of command responses from the SD bus to this<br>field for each response type.|



#### 78.7.1.8 Command Response2 (CMD_RSP2) 

##### Offset 

|Register|Offset|
|---|---|
|CMD_RSP2|18h|



##### Function 

This register is used to store part 2 of the response bits from the card. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4488 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4489-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R CMDRSP2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R CMDRSP2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-0|Command response 2|
|CMDRSP2|SeeCommand Response3 (CMD_RSP3)for the mapping of command responses from the SD bus to this<br>field for each response type.|



#### 78.7.1.9 Command Response3 (CMD_RSP3) 

##### Offset 

|Register|Offset|
|---|---|
|CMD_RSP3|1Ch|



##### Function 

This register is used to store part 3 of the response bits from the card. 

The table below describes the mapping of command responses from the SD bus to Command Response registers for each response type. In this table, R[ ] refers to a bit range within the response data as transmitted on the SD bus. 

Table 684. Response bit definition for each response type 

|Response type|Meaning of response|Response field|Response register|
|---|---|---|---|
|R1,R1b (normal response)|Card status|R[39:8]|CMDRSP0|
|R1b (auto CMD12 response)|Card status for auto CMD12|R[39:8]|CMDRSP3|
|R2 (CID, CSD register)|CID/CSD register [127:8]|R[127:8]|{CMDRSP3[23:0],<br>CMDRSP2,<br>CMDRSP1,<br>CMDRSP0}|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4489 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

Table 684. Response bit definition for each response type (continued) 

|Response type|Meaning of response|Response field|Response register|
|---|---|---|---|
|R3 (OCR register)|OCR register for memory|R[39:8]|CMDRSP0|
|R4 (OCR register)|OCR register for I/O etc.|R[39:8]|CMDRSP0|
|R5, R5b|SDIO response|R[39:8]|CMDRSP0|
|R6 (publish RCA)|New published RCA[31:16]<br>and card status[15:0]|R[39:9]|CMDRSP0|



This table shows that most responses with a length of 48 (R[47:0]) have 32-bits of the response data (R[39:8]) stored in the CMDRSP0 register. Responses of type R1b (Auto CMD12 responses) have response data bits (R[39:8]) stored in the CMDRSP3 register. Responses with length 136 (R[135:0]) have 120-bits of the response data (R[127:8]) stored in the CMDRSP0, 1, 2, and 3 registers. 

To be able to read the response status efficiently, uSDHC only stores part of the response data in the Command Response registers. This enables the host driver to efficiently read 32-bits of response data in one read cycle on a 32-bit bus system. Parts of the response, the Index field and the CRC, are checked by uSDHC (as specified by the Command Index Check Enable and the Command CRC Check Enable bits in the Transfer Type register) and generate an error interrupt if any error is detected. The bit range for the CRC check depends on the response length. If the response length is 48, uSDHC checks R[47:1], and if the response length is 136 the uSDHC checks R[119:1]. 

Because uSDHC may have a multiple block data transfer executing concurrently with a CMD_wo_DAT command, uSDHC stores the Auto CMD12 response in the CMDRSP3 register. The CMD_wo_DAT response is stored in CMDRSP0. This allows uSDHC to avoid overwriting the Auto CMD12 response with the CMD_wo_DAT and vice versa. When uSDHC modifies part of the Command Response registers, as shown in the table above, it preserves the unmodified bits. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||CMD|RSP3||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||CMD|RSP3||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function|
|---|---|
|31-0|Command response 3|
|CMDRSP3|SeeCommand Response3 (CMD_RSP3)for the mapping of command responses from the SD bus to this<br>field for each response type.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4490 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

#### 78.7.1.10 Data Buffer Access Port (DATA_BUFF_ACC_PORT) 

##### Offset 

|Register|Offset|
|---|---|
|DATA_BUFF_ACC_POR<br>T|20h|



##### Function 

The Buffer Data Port register is for 32-bit data access by the Arm platform or the external DMA. When the internal DMA is enabled, any write to this field is ignored, and any read from this field always yields 0s. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||DATC|ONT||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||||DATC|ONT||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-0|Data content|
|DATCONT|This field is used to access the internal buffer.|



#### 78.7.1.11 Present State (PRES_STATE) 

##### Offset 

|Register|Offset|
|---|---|
|PRES_STATE|24h|



##### Function 

The host driver can get status of uSDHC from this 32-bit read only register. 

The host driver can issue CMD0, CMD12, CMD13 (for memory) and CMD52 (for SDIO) when the DATA lines are busy during a data transfer. These commands can be issued when Command Inhibit (CMD) is set to zero. Other commands are issued when Command Inhibit (DATA) is set to zero. Possible changes to the SD Physical Specification may add other commands to this list in the future. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4491 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

~~<mark>NOTE</mark>~~ 

The reset value of Present State register depends on board connectivity. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4492-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>WPSP<br>R DLSL  CLSL  0 CDPL  0 CINST<br>L<br>W<br>Reset u u u u u u u u u 0 0 0 u u 0 u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>SDST<br>R TSCD  0 RTR  BREN  BWEN  RTA  WTA  Reserved  DLA  CDIHB  CIHB<br>B<br>W<br>Reset 1 0 0 0 0 0 0 0 1 0 0 0 u 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-24|DATA[7:0] line signal level|
|DLSL|This field is used to check the DATA line level to recover from errors, and for debugging. This is especially<br>useful in detecting the busy signal level from DATA0. The reset value is affected by the external pull-up /<br>pull-down resistors. By default, the read value of this field after reset is 8'b11110111, when DATA3 is pulled<br>down and the other lines are pulled up.<br>0000_0000b - Data 0 line signal level<br>0000_0001b - Data 1 line signal level<br>0000_0010b - Data 2 line signal level|
||0000_0011b - Data 3 line signal level<br>0000_0100b - Data 4 line signal level<br>0000_0101b - Data 5 line signal level<br>0000_0110b - Data 6 line signal level<br>0000_0111b - Data 7 line signal level|
|23|CMD line signal level|
|CLSL|This field is used to check the CMD line level to recover from errors, and for debugging. The reset value is<br>affected by the external pull-up / pull-down resistor, by default, the read value of this field after reset is 1'b1,<br>when the command line is pulled up.|
|22-20<br>—|Reserved|
|19|Write protect switch pin level|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4492 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|WPSPL|The Write Protect switch is supported for memory and combo cards. This field reflects the inverted value of<br>the WP pin of the card socket. A software reset does not affect this field. The reset value is affected by the<br>external write protect switch. If the WP pin is not used, it should be tied low, so that the reset value of this<br>field is high and write is enabled.<br>0b - Write protected (WP = 1)<br>1b - Write enabled (WP = 0)|
|18<br>CDPL|Card detect pin level<br>This field reflects the inverse value of the CD_B pin for the card socket. Debouncing is not performed on this<br>field. This field may be valid, but is not guaranteed, because of propagation delay. Use of this field is limited<br>to testing because it must be debounced by software. A software reset does not affect this field. A write to<br>the Force Event Register does not affect this field. The reset value is affected by the external card detection<br>pin. This field shows the value on the CD_B pin (that is, when a card is inserted in the socket, it is 0 on the<br>CD_B input, and consequently, the CDPL reads 1.<br>0b - No card present (CD_B = 1)<br>1b - Card present (CD_B = 0)|
|17<br>—|Reserved|
|16<br>CINST|Card inserted<br>This field indicates whether a card has been inserted. The uSDHC module debounces this signal so that<br>the host driver does not need to wait for it to stabilize. Changing from a 0 to 1 generates a Card Insertion<br>interrupt in the Interrupt Status register. Changing from a 1 to 0 generates a Card Removal interrupt in the<br>Interrupt Status register. A write to the Force Event Register does not affect this field.<br>The Software Reset For All in the System Control register does not affect this field. A software reset does<br>not affect this field.<br>0b - Power on reset or no card<br>1b - Card inserted|
|15<br>TSCD|Tap select change done<br>This field indicates the delay setting is effective after write CLK_TUNE_CTRL_STATUS register.<br>0b - Delay cell select change is not finished.<br>1b - Delay cell select change is finished.|
|14-13<br>—|Reserved|
|12<br>RTR|Re-Tuning Request (only for SD3.0 SDR104 mode)<br>Host controller may request host driver to execute re-tuning sequence by setting this field when the data<br>window is shifted by temperature drift and a tuned sampling point does not have a good margin to receive<br>correct data.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4493 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function<br>This field is cleared when a command is issued with setting Execute Tuning field in MIX_CTRL register.<br>Changing of this field from 0 to 1 generates Re-Tuning Event. See Interrupt status registers for more detail.<br>This field isn't set to 1 if Sampling Clock Select in the MIX_CTRL register is set to 0 (using fixed<br>sampling clock).<br>0b - Fixed or well tuned sampling clock<br>1b - Sampling clock needs re-tuning|
|---|---|
|11<br>BREN|Buffer read enable<br>This status field is used for non-DMA read transfers. The uSDHC module implements an internal buffer to<br>transfer data efficiently. This read only flag indicates that valid data exists in the host side buffer. If this field<br>is high, valid data greater than the watermark level exist in the buffer. A change of this field from 1 to 0 occurs<br>when some reads from the buffer (read DATPORT (Base + 0x20)) are made and the buffer hasn't valid data<br>greater than the watermark level. A change of this field from 0 to1 occurs when there is enough valid data<br>ready in the buffer and the Buffer Read Ready interrupt has been generated and enabled.<br>0b - Read disable<br>1b - Read enable|
|10<br>BWEN|Buffer write enable<br>This status field is used for non-DMA write transfers. The uSDHC module implements an internal buffer to<br>transfer data efficiently. This read only flag indicates if space is available for write data. If this field is 1, valid<br>data greater than the watermark level can be written to the buffer. A change of this field from 1 to 0 occurs<br>when some writes to the buffer (write DATPORT (Base + 0x20)) are made and the buffer hasn't valid space<br>greater than the watermark level. A change of this field from 0 to 1 occurs when the buffer can hold valid<br>data greater than the write watermark level and the Buffer Write Ready interrupt is generated and enabled.<br>0b - Write disable<br>1b - Write enable|
|9<br>RTA|Read transfer active<br>This status field is used for detecting completion of a read transfer.<br>This field is set for either of the following conditions:<br>• After the end field of the read command<br>• When writing a 1 to the Continue Request field in the Protocol Control register to restart a read<br>transfer<br>A transfer complete interrupt is generated when this field changes to 0. This field is cleared for either of the<br>following conditions:<br>• When the last data block as specified by block length is transferred to the System, that is, all data<br>are read away from uSDHC internal buffer.<br>• When all valid data blocks have been transferred from uSDHC internal buffer to the System and no<br>current block transfers are being sent because of the Stop At Block Gap Request being set to 1.<br>0b - No valid data|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4494 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function<br>1b - Transferring data|
|---|---|
|8<br>WTA|Write transfer active<br>This status field indicates a write transfer is active. If this field is 0, it means no valid write data exists<br>in uSDHC.<br>This field is set in either of the following cases:<br>• After the end field of the write command<br>• When writing 1 to the Continue Request field in the Protocol Control register to restart a write<br>transfer<br>This field is cleared in either of the following cases:<br>• After getting the CRC status of the last data block as specified by the transfer count (Single and<br>Multiple)<br>• After getting the CRC status of any block where data transmission is about to be stopped by a Stop<br>At Block Gap Request<br>During a write transaction, a Block Gap Event interrupt is generated when this field is changed to 0, as result<br>of the Stop At Block Gap Request being set. This status is useful for the host driver in determining when to<br>issue commands during Write Busy state.<br>0b - No valid data<br>1b - Transferring data|
|7-4<br>—|Reserved|
|3<br>SDSTB|SD clock stable<br>This status field indicates that the internal card clock is stable. This field is for the host driver to poll clock<br>status when changing the clock frequency. It is recommended to clear FRC_SDCLK_ON field in System<br>Control register to remove glitches on the card clock when the frequency is changing.<br>Before changing clock divisor value (SDCLKFS or DVS), host driver should make sure the SDSTB field<br>is high.<br>0b - Clock is changing frequency and not stable.<br>1b - Clock is stable.|
|2<br>DLA|Data line active<br>This status field indicates whether one of the DATA lines on the SD bus is in use.<br>In the case of read transactions:<br>This status indicates if a read transfer is executing on the SD bus. Changes in this value from 1 to 0, between<br>data blocks, generates a Block Gap Event interrupt in the Interrupt Status register.<br>This field is set in either of the following cases:<br>• After the end field of the read command|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4495 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function<br>• When writing a 1 to the Continue Request field in the Protocol Control register to restart a read<br>transfer<br>This field is cleared in either of the following cases:<br>• When the end field of the last data block is sent from the SD bus to uSDHC.<br>• When the Read Wait state is stopped by a Suspend command and the DATA2 line is released.<br>The uSDHC module waits at the next block gap by driving Read Wait at the start of the interrupt cycle. If the<br>Read Wait signal is already driven (data buffer cannot receive data), uSDHC can wait for a current block<br>gap by continuing to drive the Read Wait signal. It is necessary to support Read Wait to use the suspend /<br>resume function. This field remains 1 during Read Wait.<br>In the case of write transactions:<br>This status indicates that a write transfer is executing on the SD bus. Changes in this value from 1 to 0<br>generate a Transfer Complete interrupt in the Interrupt Status register.<br>This field is set in either of the following cases:<br>• After the end field of the write command<br>• When writing to 1 to the Continue Request field in the Protocol Control register to continue a write<br>transfer<br>This field is cleared in either of the following cases:<br>• When the SD card releases Write Busy of the last data block, uSDHC also detects if the output is<br>not busy. If the SD card does not drive the busy signal after the CRC status is received, uSDHC<br>assumes the card drive "Not Busy".<br>• When the SD card releases write busy, prior to waiting for write transfer, and because of a Stop At<br>Block Gap Request.<br>In the case of command with busy pending:<br>This status indicates that a busy state follows the command and the data line is in use. This field is cleared<br>when the DATA0 line is released.<br>0b - DATA line inactive|
|---|---|
||1b - DATA line active|
|1<br>CDIHB|Command Inhibit Data (DATA)<br>This status field is generated if either the DAT Line Active or the Read Transfer Active is set to 1. If this<br>field is 0, it indicates that uSDHC can issue the next SD / eMMC Command. Commands with a busy signal<br>belong to Command Inhibit (DATA) (for example. R1b, R5b type). Changing from 1 to 0 generates a Transfer<br>Complete interrupt in the Interrupt Status register.|
||The SD host driver can save registers for a suspend transaction after this field has changed<br>from 1 to 0.<br>~~NOTE~~|
||0b - Can issue command that uses the DATA line<br>1b - Cannot issue command that uses the DATA line|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4496 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|0|Command inhibit (CMD)|
|CIHB|If this status bit is 0, it indicates that the CMD line is not in use and uSDHC can issue a SD / eMMC command<br>using the CMD line.|
||This field is set also immediately after the Transfer Type register is written. This field is cleared when the<br>command response is received. Even if the Command Inhibit (DATA) is set to 1, commands using only the<br>CMD line can be issued if this field is 0. Changing from 1 to 0 generates a Command Complete interrupt in<br>the Interrupt Status register. If uSDHC cannot issue the command because of a command conflict error (see<br>Command CRC Error) or because of a Command Not Issued By Auto CMD12 Error, this field remains 1 and<br>the Command Complete is not set. The Status of issuing an auto CMD12 does not show on this field.<br>0b - Can issue command using only CMD line<br>1b - Cannot issue command|



#### 78.7.1.12 Protocol Control (PROT_CTRL) 

##### Offset 

|Register|Offset|
|---|---|
|PROT_CTRL|28h|



##### Function 

This register controls three cases to restart the transfer after stop at the block gap. Which case is appropriate depends on whether uSDHC issues a Suspend command or the SD card accepts the Suspend command. 

- If the host driver does not issue a Suspend command, the Continue request is used to restart the transfer. 

- If the host driver issues a Suspend command and the SD card accepts it, a Resume command is used to restart the transfer. 

- If the host driver issues a Suspend command and the SD card does not accept it, the Continue request is used to restart the transfer. 

Any time stop at block gap request stops the data transfer, the host driver waits for a Transfer Complete (in the Interrupt Status register), before attempting to restart the transfer. When restarting the data transfer by Continue Request, the host driver clears the Stop At Block Gap Request before or simultaneously. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4497 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|Reserv<br>ed|NON_<br>EXA...|BUR|ST_LEN|_EN|WECR<br>M|WECI<br>NS|WECI<br>NT||Reserved||RD_D<br>ONE...|IABG|RWCT<br>L|CREQ|SABG<br>REQ|
|Reset|0|0|0|0|1|0|0|0|1|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||0||||DMA|SEL|CDSS|CDTL|EM|ODE|D3CD|DT|W|Reserv<br>ed|
|Reset|0|0|0|0|0|0|0|0|0|0|1|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|Reserved|
|—|Always write as 0|
|30|Non-exact block read|
|NON_EXACT_B<br>LK_RD|Current block read is non-exact block read. It is only used for SDIO.<br>0b - The block read is exact block read. Host driver does not need to issue abort command to<br>terminate this multi-block read.<br>1b - The block read is non-exact block read. Host driver needs to issue abort command to<br>terminate this multi-block read.|
|29-27|BURST length enable for INCR, INCR4 / INCR8 / INCR16, INCR4-WRAP / INCR8-WRAP / INCR16-WRAP|
|BURST_LEN_E<br>N|This field is used to enable or disable the burst length for the external AHB2AXI bridge. It is useful especially<br>for INCR transfer because without burst length indicator, the AHB2AXI bridge does not know the burst length<br>in advance. Without burst length indicator, AHB INCR transfers can only be converted to SINGLEs on the<br>AXI side.<br>1xxb - Burst length is enabled for INCR4-WRAP / INCR8-WRAP / INCR16-WRAP.<br>x1xb - Burst length is enabled for INCR4 / INCR8 / INCR16.<br>xx1b - Burst length is enabled for INCR.|
|26<br>WECRM|Wakeup event enable on SD card removal<br>This field enables a wakeup event, via a card removal, in the Interrupt Status register. FN_WUS (Wakeup<br>Support) in CIS does not affect this field. When this field is set, the Card Removal Status and uSDHC<br>interrupt can be asserted without CLK toggling. When the wakeup feature is not enabled, the CLK must be<br>active to assert the Card Removal Status and uSDHC interrupt.<br>0b - Disables wakeup event enable on SD card removal<br>1b - Enables wakeup event enable on SD card removal|
|25|Wakeup event enable on SD card insertion|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4498 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|WECINS|This field enables a wakeup event, via a card insertion, in the Interrupt Status register. FN_WUS (Wakeup<br>Support) in CIS does not affect this field. When this field is set, the Card Insertion Status and uSDHC<br>interrupt can be asserted without CLK toggling. When the wakeup feature is not enabled, the CLK must be<br>active to assert the Card Insertion Status and uSDHC interrupt.<br>0b - Disable wakeup event enable on SD card insertion<br>1b - Enable wakeup event enable on SD card insertion|
|24<br>WECINT|Wakeup event enable on card interrupt<br>This field enables a wakeup event, via a card interrupt, in the Interrupt Status register. This field can be set<br>to 1 if FN_WUS (Wakeup Support) in CIS is set to 1. When this field is set, the Card Interrupt Status and<br>uSDHC interrupt can be asserted without CLK toggling. When the wakeup feature is not enabled, the CLK<br>must be active to assert the Card Interrupt Status and uSDHC interrupt.<br>0b - Disables wakeup event enable on card interrupt<br>1b - Enables wakeup event enable on card interrupt|
|23-21<br>—|Reserved<br>Always write as 3'b100|
|20|Read performed number 8 clock|
|RD_DONE_NO<br>_8CLK|According to the SD/eMMC spec, for read data transaction, 8 clocks are needed after the end field of the<br>last data block. So, by default(RD_DONE_NO_8CLK=0), eight clocks are active after the end field of the last<br>read data transaction.<br>However, these 8 clocks should not be active if user wants to use stop at block gap (include the auto stop at<br>block gap in boot mode) feature for read and the RWCTL field (bit18) is not enabled. In this case, software<br>should set RD_DONE_NO_8CLK to avoid these 8 clocks. Otherwise, the device might send extra data to<br>uSDHC while uSDHC ignores these data.<br>In a summary, this field should be set only if the use case needs to use stop at block gap feature while the<br>device can't support the read wait feature.|
|19<br>IABG|Interrupt at block gap<br>This field is valid only in 4-bit mode, of the SDIO card, and selects a sample point in the interrupt cycle.<br>Setting to 1 enables interrupt detection at the block gap for a multiple block transfer. Setting to 0 disables<br>interrupt detection during a multiple block transfer. If the SDIO card cannot signal an interrupt during a<br>multiple block transfer, this field should be set to 0 to avoid an inadvertent interrupt. When the host driver<br>detects an SDIO card insertion, it sets this field according to the CCCR of the card.<br>0b - Disables interrupt at block gap<br>1b - Enables interrupt at block gap|
|18<br>RWCTL|Read wait control<br>The read wait function provided by this field is optional for SDIO cards. If the card supports read wait, set this<br>field to enable use of the read wait protocol to stop read data using the DATA2 line. Otherwise, uSDHC has<br>to stop the SD clock to hold read data, which restricts commands generation. When the host driver detects<br>an SDIO card insertion, it sets this field according to the CCCR of the card. If the card does not support<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4499 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function<br>read wait, this field should never be set to 1; otherwise, DATA line conflicts might occur. If this field is set<br>to 0, stop at block gap during read operation is also supported, but uSDHC stops the SD clock to pause<br>reading operation.<br>0b - Disables read wait control and stop SD clock at block gap when SABGREQ field is set<br>1b - Enables read wait control and assert read wait without stopping SD clock at block gap when<br>SABGREQ field is set|
|---|---|
|17<br>CREQ|Continue request<br>This field is used to restart a transaction which was stopped using the stop at block gap request. When a<br>suspend operation is not accepted by the card, it is also by setting this field to restart the paused transfer. To<br>cancel stop at the block gap, set stop at block gap request to 0 and set this field to 1 to restart the transfer.<br>The uSDHC module automatically clears this field, therefore it is not necessary for the host driver to set this<br>field to 0. If both stop at block gap request and this field are 1, the continue request is ignored.<br>0b - No effect<br>1b - Restart|
|16|Stop at block gap request|
|SABGREQ|This field is used to stop executing a transaction at the next block gap for both DMA and non-DMA transfers.<br>Until the transfer complete is set to 1, indicating a transfer completion, the host driver leaves this field set<br>to 1. Clearing both the stop at block gap request and continue request does not cause the transaction to<br>restart. Read Wait is used to stop the read transaction at the block gap. The uSDHC module supports the<br>stop at block gap request for write transfers, but for read transfers it requires that the SDIO card support read<br>wait. Therefore, the host driver does not set this field during read transfers unless the SDIO card supports<br>Read Wait and has set the read wait control to 1; otherwise, uSDHC stops the SD bus clock to pause the<br>read operation during block gap. In the case of write transfers in which the host driver writes data to the Data<br>Port register, the host driver sets this field after all block data is written. If this field is set to 1, the host driver<br>does not write data to the Data Port register after a block is sent. Once this field is set, the host driver does<br>not clear this field before the Transfer Complete field in Interrupt Status register is set, otherwise uSDHC's<br>behavior is undefined.<br>This field effects read transfer active, write transfer active, DATA Line Active and Command Inhibit (DATA)<br>in the Present State register.<br>0b - Transfer<br>1b - Stop|
|15-10<br>—|Reserved|
|9-8<br>DMASEL|DMA select<br>This field is valid while DMA (SDMA or ADMA) is enabled and selects the DMA operation.<br>00b - No DMA or simple DMA is selected.<br>01b - ADMA1 is selected.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4500 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||10b - ADMA2 is selected.<br>11b - Reserved|
|7<br>CDSS|Card detect signal selection<br>This field selects the source for the card detection.<br>0b - Card detection level is selected (for normal purpose).<br>1b - Card detection test level is selected (for test purpose).|
|6<br>CDTL|Card detect test level<br>This field is enabled while the card detection signal selection is set to 1 and it indicates card insertion.<br>0b - Card detect test level is 0, no card inserted<br>1b - Card detect test level is 1, card inserted|
|5-4<br>EMODE|Endian mode<br>This field supports all three endian modes in data transfer. SeeData bufferfor more details.<br>00b - Big endian mode<br>01b - Half word big endian mode<br>10b - Little endian mode<br>11b - Reserved|
|3<br>D3CD|DATA3 as card detection pin<br>If this field is set, DATA3 should be pulled down to act as a card detection pin. Be cautious when using this<br>feature, because DATA3 is also a chip-select for the SPI mode. A pull-down on this pin and CMD0 might<br>set the card into the SPI mode, which uSDHC does not support.<br>0b - DATA3 does not monitor card insertion<br>1b - DATA3 as card detection pin|
|2-1<br>DTW|Data transfer width<br>This field selects the data width of the SD bus for a data transfer. The host driver sets it to match the data<br>width of the card. Possible data transfer width is 1-bit, 4-bits or 8-bits.<br>00b - 1-bit mode<br>01b - 4-bit mode<br>10b - 8-bit mode<br>11b - Reserved|
|0<br>—|Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4501 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

#### 78.7.1.13 System Control (SYS_CTRL) 

##### Offset 

|Register|Offset|
|---|---|
|SYS_CTRL|2Ch|



##### Function 

This register provides control of the system. See detail in the field description. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4502-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv<br>R 0 0<br>RSTT  INITA  RSTD  RSTC  RSTA  IPP_R ed  Reserv DTOCV<br>ST... ed<br>W<br>Reset 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R<br>SDCLKFS  DVS  Reserved<br>W<br>Reset 1 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-29|Reserved|
|—||
|28|Reset tuning|
|RSTT|When set this field to 1, it resets tuning circuit. After tuning circuits are reset, bit value is 0. Clearing<br>execute_tuning field in AUTOCMD12_ERR_STATUS also sets this field to 1 to reset tuning circuit|
|27|Initialization active|
|INITA|When this field is set, 80 SD-clocks are sent to the card. After the 80 clocks are sent, this field is self cleared.<br>This field is very useful during the card power-up period when 74 SD-clocks are needed and the clock auto<br>gating feature is enabled. Writing 1 to this bit when this field is already 1 has no effect. Writing 0 to this field<br>at any time has no effect. When either of the CIHB and CDIHB fields in the Present State register are set,<br>writing 1 to this field is ignored (that is, when command line or data lines are active, write to this field is not<br>allowed). On the other-hand, when this field is set, that is, during initialization active period, it is allowed to<br>issue command, and the command bit stream appears on the CMD pad after all 80 clock cycles are done.<br>So, when this command ends, the driver can make sure the 80 clock cycles are sent out. This is very useful<br>when the driver needs to send 80 cycles to the card and does not want to wait till this field is self cleared.|
|26|Software reset for data line|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4502 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|RSTD|Only part of the data circuit is reset. DMA circuit is also reset. After this field is set, the software waits<br>for self-clear.<br>The following registers and bits are cleared by this field:<br>• Data Port register<br>— Buffer is cleared and initialized<br>• Present State register<br>— Buffer read enable<br>— Buffer write enable<br>— Read transfer active<br>— Write transfer active<br>— DATA line active<br>— Command Inhibit (DATA)<br>• Protocol Control register<br>— Continue request<br>• Interrupt Status register<br>— Buffer read ready<br>— Buffer write ready<br>— DMA interrupt<br>— Block gap event<br>— Transfer complete<br>When reset, the software must make sure there is no incomplete data transferring. If there<br>is data transfer going on, the software needs to wait TC or DC INT_STATUS register is set.<br>~~NOTE~~|
||0b - No reset<br>1b - Reset|
|25<br>RSTC|Software reset for CMD line<br>Only part of the command circuit is reset. After this field is set, the software waits for self-clear.<br>The following registers and bits are cleared by this field:<br>• Present State Register<br>— Command Inhibit (CMD)<br>• Interrupt Status Register<br>— Command Complete<br>0b - No reset<br>1b - Reset|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4503 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field<br>24<br>RSTA|Function<br>Software reset for all<br>This reset affects the entire host controller except for the card detection circuit. RSTA resets all the registers<br>that can be reset by RSTC/RSTD. During its initialization, the host driver is set this field to 1 to reset uSDHC.<br>The uSDHC module resets this field to 0 when the capabilities registers are valid and the host driver can<br>read them. Additional use of Software Reset For All does not affect the value of the capabilities registers.<br>After this field is set, it is recommended that the host driver reset the external card and re-initialize it. After<br>this field is set, the software should wait for self-clear.<br>In tuning process, after every CMD19 is finished, this field is set to retest uSDHC.<br>When reset, the software must make sure there is no incomplete data transferring. If there<br>is data transfer going on, the software needs to wait TC or DC INT_STATUS register is set.<br>~~NOTE~~<br>0b - No reset<br>1b - Reset|
|---|---|
|23<br>IPP_RST_N|Hardware reset<br>This field's value is output to card through pad directly to hardware reset pin of the card if the card supports<br>this feature.|
|22<br>—|Reserved|
|21<br>—|Reserved|
|20<br>—<br>19-16<br>DTOCV|Reserved<br>Data timeout counter value<br>This value determines the interval by which DAT line timeouts are detected. See the Data Timeout Error<br>field in the Interrupt Status register for information on factors that dictate time-out generation. Time-out clock<br>frequency is generated by dividing the base clock SDCLK value by this value.<br>The host driver can clear the Data Timeout Error Status Enable (in the Interrupt Status Enable register) to<br>prevent inadvertent time-out events.<br>0000b - SDCLK x 2<sup>14</sup><br>0001b - SDCLK x 2<sup>15</sup><br>0010b - SDCLK x 2<sup>16</sup><br>0011b - SDCLK x 2<sup>17</sup><br>0100b - SDCLK x 2<sup>18</sup><br>0101b - SDCLK x 2<sup>19</sup>|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4504 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0110b - SDCLK x 2<sup>20</sup><br>0111b - SDCLK x 2<sup>21</sup><br>1000b - SDCLK x 2<sup>22</sup><br>1001b - SDCLK x 2<sup>23</sup><br>1010b - SDCLK x 2<sup>24</sup><br>1011b - SDCLK x 2<sup>25</sup><br>1100b - SDCLK x 2<sup>26</sup><br>1101b - SDCLK x 2<sup>27</sup><br>1110b - SDCLK x 2<sup>28</sup>|
||1111b - SDCLK x 2<sup>29</sup>|
|15-8|SDCLK frequency select|
|SDCLKFS|This field is used to select the frequency of the SDCLK pin. The frequency is not programmed directly,<br>rather this field holds the prescaler (of this register) and divisor (next register) of the Base Clock<br>Frequency register.|
||In Single Data Rate mode (DDR_EN field of MIXERCTRL is '0')<br>Only the following settings are allowed:|
||80h) Base clock divided by 256|
||40h) Base clock divided by 128<br>20h) Base clock divided by 64<br>10h) Base clock divided by 32|
||08h) Base clock divided by 16|
||04h) Base clock divided by 8|
||02h) Base clock divided by 4|
||01h) Base clock divided by 2|
||00h) Base clock divided by 1|
||While in Dual Data Rate mode (DDR_EN field of MIXERCTRL is '1')<br>Only the following settings are allowed:<br>80h) Base clock divided by 512|
||40h) Base clock divided by 256|
||20h) Base clock divided by 128|
||10h) Base clock divided by 64|
||08h) Base clock divided by 32|
||04h) Base clock divided by 16|
||02h) Base clock divided by 8|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4505 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||01h) Base clock divided by 4<br>00h) Base clock divided by 2<br>When the software changes the DDR_EN field, SDCLKFS might need to be changed also.<br>In Single Data Rate mode, setting 00h bypasses the frequency prescaler of the SD clock.<br>Multiple bits must not be set, or the behavior of this prescaler is undefined. The two default divider values<br>can be calculated by the frequency of ipg_perclk and the following Divisor bits.<br>The frequency of SDCLK is set by the following formula:<br>Clock Frequency = (Base Clock) / (prescaler x divisor)<br>For example, in Single Data Rate mode, if the Base Clock Frequency is 96 MHz, and the target frequency is<br>25 MHz, then choosing the prescaler value of 01h and divisor value of 1h yields 24 MHz, which is the nearest<br>frequency less than or equal to the target. Similarly, to approach a clock value of 400 kHz, the prescaler<br>value of 08h and divisor value of eh yields the exact clock value of 400 kHz.<br>The reset value of this field is 80h, so if the input Base Clock (ipg_perclk) is about 96 MHz, the default SD<br>clock after reset is 375 kHz.<br>Before changing clock divisor value (SDCLKFS or DVS), host driver should make sure the SDSTB field<br>is high.<br>If setting SDCLKFS and DVS can generate the same clock frequency,(for example, in SDR mode,<br>SDCLKFS = 01h is same as DVS = 01h.), SDCLKFS is highly recommended.|
|7-4|Divisor|
|DVS|This field is used to provide a more exact divisor to generate the desired SD clock frequency. Note the<br>divider can even support odd divisors without deterioration of duty cycle.<br>Before changing clock divisor value (SDCLKFS or DVS), Host driver should make sure the SDSTB field<br>is high.<br>The settings are as follows:|
||0000b - Divide-by-1|
||0001b - Divide-by-2<br>1110b - Divide-by-15|
||1111b - Divide-by-16|
|3-0|Reserved|
|—|Always write as 1.|



#### 78.7.1.14 Interrupt Status (INT_STATUS) 

##### Offset 

|Register|Offset|
|---|---|
|INT_STATUS|30h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4506 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Function 

An interrupt is generated when the normal interrupt signal enable is enabled and at least one of the status fields is set to 1. For all fields, writing 1 to a bit clears it; writing to 0 keeps the bit unchanged. More than one status can be cleared with a single register write. For card interrupt, before writing 1 to clear, it is required that the card stops asserting the interrupt, meaning that when the card driver services the interrupt condition; otherwise, the CINT field is asserted again. 

The table below shows the relationship between the command timeout error and the command complete. 

Table 685. uSDHC status for command timeout error/command complete bit combinations 

|Command complete|Command timeout error|Meaning of the status|
|---|---|---|
|0|0|X|
|X|1|Response not received within 64 SDCLK cycles|
|1|0|Response received|



The table below shows the relationship between the transfer complete and the data timeout error. 

Table 686. uSDHC status for data timeout error/transfer complete bit combinations 

|Transfer complete|Data timeout error|Meaning of the status|
|---|---|---|
|0|0|X|
|0|1|Timeout occurred during transfer|
|1|X|Data transfer complete|



The table below shows the relationship between the command CRC error and command timeout error. 

Table 687. uSDHC status for command CRC error/command timeout error bit combinations 

|Command CRC error|Command timeout error|Meaning of the status|
|---|---|---|
|0|0|No error|
|0|1|Response timeout error|
|1|0|Response CRC error|
|1|1|CMD line conflict|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4507 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|0|0||DMAE|0|TNE|0|AC12E|0|DEBE|DCE|DTOE|CIE|CEBE|CCE|CTOE|
|W||||W1C||W1C||W1C||W1C|W1C|W1C|W1C|W1C|W1C|W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|ERR_I<br>NT...|TP|0|RTE|0|Rese|rved|CINT|CRM|CINS|BRR|BWR|DINT|BGE|TC|CC|
|W||W1C||W1C||W1|C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31<br>—|Reserved|
|30-29<br>—<br>28<br>DMAE|Reserved<br>DMA error<br>Occurs when an Internal DMA transfer has failed. This field is set to 1, when some error occurs in the data<br>transfer. This error can be caused by either simple DMA or ADMA, depending on which DMA is in use.<br>The value in DMA System Address register is the next fetch address where the error occurs. Because any<br>error corrupts the whole data block, the host driver restarts the transfer from the corrupted block boundary.<br>The address of the block boundary can be calculated either from the current DS_ADDR value or from the<br>remaining number of blocks and the block size.<br>0b - No error<br>1b - Error|
|27<br>—<br>26<br>TNE|Reserved<br>Tuning error: (only for SD3.0 SDR104 mode)<br>This field is set when an unrecoverable error is detected in a tuning circuit. By detecting Tuning Error, host<br>driver needs to abort a command executing and perform tuning. This field is relevant in combination with the<br>bus error only and must be cleared prior to all the write and read transactions.|
|25<br>—<br>24<br>AC12E|Reserved<br>Auto CMD12 error|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4508 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function<br>Occurs when detecting that one of the fields in the Auto CMD12 Error Status register has changed from 0<br>to 1. This field is set to 1, not only when the errors in Auto CMD12 occur, but also, when the Auto CMD12<br>is not executed due to the previous command error.<br>0b - No error<br>1b - Error|
|---|---|
|23<br>—|Reserved|
|22<br>DEBE|Data end bit error<br>Occurs either when detecting 0 at the end field position of read data that uses the DATA line, or at the end<br>field position of the CRC.<br>This field is not asserted in tuning process.<br>0b - No error<br>1b - Error|
|21<br>DCE|Data CRC error<br>Occurs when detecting a CRC error when transferring read data that uses the DATA line, or when detecting<br>the Write CRC status having a value other than 010.<br>This field is not asserted in tuning process.<br>0b - No error<br>1b - Error|
|20<br>DTOE|Data timeout error<br>Occurs when detecting one of following time-out conditions.<br>• Busy time-out for R1b, R5b type<br>• Busy time-out after Write CRC status<br>• Read Data time-out.<br>This field is not asserted in tuning process.<br>0b - No error<br>1b - Time out|
|19<br>CIE|Command index error<br>Occurs if a command index error occurs in the command response.<br>This field is not asserted in tuning process.<br>0b - No error<br>1b - Error|
|18|Command end bit error|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4509 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|CEBE|Occurs when detecting that the end field of a command response is 0.<br>This field is not asserted in tuning process.<br>0b - No error<br>1b - End bit error generated|
|17<br>CCE|Command CRC error<br>Command CRC Error is generated in two cases.<br>• If a response is returned and the Command Timeout Error is set to 0 (indicating no time-out), this<br>field is set when detecting a CRC error in the command response.<br>• The uSDHC module detects a CMD line conflict by monitoring the CMD line when a command is<br>issued. If uSDHC drives the CMD line to 1, but detects 0 on the CMD line at the next SDCLK edge,<br>then uSDHC aborts the command (Stop driving CMD line) and set this bit to 1. The Command<br>Timeout Error should also be set to 1 to distinguish CMD line conflict.<br>This field is not asserted in tuning process.<br>0b - No error<br>1b - CRC error generated|
|16<br>CTOE|Command timeout error<br>Occurs only if no response is returned within 64 SDCLK cycles from the end field of the command. If uSDHC<br>detects a CMD line conflict, in which case a Command CRC Error is also be set (as shown inInterrupt<br>Status (INT_STATUS)), this field is set without waiting for 64 SDCLK cycles. This is because the command<br>is aborted by uSDHC.<br>This field is not asserted in tuning process.<br>0b - No error<br>1b - Time out|
|15<br>ERR_INT_STA<br>TUS|Error Interrupt Status<br>This bit is set when any of the error status bit DMAE, AC12E, DEBE, DCE, DTOE, CIE, CEBE, CCE and<br>CTOE is set.|
|14<br>TP|Tuning pass:(only for SD3.0 SDR104 mode)<br>Current CMD19 transfer is done successfully. That is, current sampling point is correct.|
|13<br>—|Reserved|
|12<br>RTE|Re-tuning event: (only for SD3.0 SDR104 mode)<br>This status is set if Re-Tuning Request in the Present State register changes from 0 to 1. host controller<br>requests host driver to perform re-tuning for next data transfer. Current data transfer (not large block count)<br>can be completed without re-tuning.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4510 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function<br>0b - Re-tuning is not required.<br>1b - Re-tuning should be performed.|
|---|---|
|11<br>—|Reserved|
|10-9<br>—|Reserved|
|8<br>CINT|Card interrupt<br>This status field is set when an interrupt signal is detected from the external card. In 1-bit mode, uSDHC<br>detects the Card Interrupt without the SD clock to support wakeup. In 4-bit mode, the card interrupt signal<br>is sampled during the interrupt cycle, so the interrupt from card can only be sampled during interrupt cycle,<br>introducing some delay between the interrupt signal from the SDIO card and the interrupt to the host system.<br>Writing this field to 1 can clear this field, but as the interrupt source from the SDIO card does not clear, this<br>field is set again. to clear this field, it is required to reset the interrupt source from the external card followed<br>by a writing 1 to this field.<br>When this status has been set, and the host driver needs to service this interrupt, the Card Interrupt Signal<br>Enable in the Interrupt Signal Enable register should be 0 to stop driving the interrupt signal to the host<br>system. After completion of the card interrupt service (It should reset the interrupt sources in the SDIO card<br>and the interrupt signal might not be asserted), write 1 to clear this field, set the Card Interrupt Signal Enable<br>to 1, and start sampling the interrupt signal again.<br>0b - No card interrupt<br>1b - Generate card interrupt|
|7<br>CRM|Card removal<br>This status field is set if the Card Inserted field in the Present State register changes from 1 to 0. When the<br>host driver writes this field to 1 to clear this status, the status of the Card Inserted in the Present State register<br>should be confirmed. Because the card state might possibly be changed when the host driver clears this field<br>and the interrupt event might not be generated. When this field is cleared, it is set again if no card is inserted.<br>to leave it cleared, clear the Card Removal Status Enable field in Interrupt Status Enable register.<br>0b - Card state unstable or inserted<br>1b - Card removed|
|6<br>CINS|Card insertion<br>This status field is set if the Card Inserted field in the Present State register changes from 0 to 1. When the<br>host driver writes this field to 1 to clear this status, the status of the Card Inserted in the Present State register<br>should be confirmed. Because the card state might possibly be changed when the host driver clears this field<br>and the interrupt event might not be generated. When this field is cleared, it is set again if a card is inserted.<br>to leave it cleared, clear the Card Inserted Status Enable field in Interrupt Status Enable register.<br>0b - Card state unstable or removed<br>1b - Card inserted|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4511 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field<br>5<br>BRR|Function<br>Buffer read ready<br>This status field is set if the Buffer Read Enable field, in the Present State register, changes from 0 to 1. See<br>the Buffer Read Enable field in the Present State register for additional information.<br>This field indicates that cmd19 is finished in tuning process.<br>0b - Not ready to read buffer<br>1b - Ready to read buffer|
|---|---|
|4<br>BWR|Buffer write ready<br>This status field is set if the Buffer Write Enable field, in the Present State register, changes from 0 to 1. See<br>the Buffer Write Enable field in the Present State register for additional information.<br>0b - Not ready to write buffer<br>1b - Ready to write buffer|
|3<br>DINT|DMA interrupt<br>Occurs only when the internal DMA finishes the data transfer successfully. Whenever errors occur during<br>data transfer, this field does not be set. Instead, the DMAE field is set. Either Simple DMA or ADMA finishes<br>data transferring, this field is set.<br>0b - No DMA interrupt<br>1b - DMA interrupt is generated.|
|2|Block gap event|
|BGE|If the Stop At Block Gap Request field in the Protocol Control register is set, this field is set when a read or<br>write transaction is stopped at a block gap. If Stop At Block Gap Request is not set to 1, this field is not set<br>to 1.<br>In the case of a Read Transaction: This field is set at the falling edge of the DATA Line Active Status (When<br>the transaction is stopped at SD bus timing). The Read Wait must be supported to use this function.<br>In the case of Write Transaction: This field is set at the falling edge of Write Transfer Active Status (After<br>getting CRC status at SD Bus timing).<br>0b - No block gap event<br>1b - Transaction stopped at block gap|
|1<br>TC|Transfer complete<br>This field is set when a read or write transfer is completed.<br>In the case of a Read Transaction: This field is set at the falling edge of the Read Transfer Active Status.<br>There are two cases in which this interrupt is generated. The first is when a data transfer is completed as<br>specified by the data length (after the last data has been read to the host system). The second is when data<br>has stopped at the block gap and completed the data transfer by setting the Stop At Block Gap Request field<br>in the Protocol Control register (after valid data has been read to the host system).<br>In the case of a Write Transaction: This field is set at the falling edge of the DATA Line Active Status. There<br>are two cases in which this interrupt is generated. The first is when the last data is written to the SD card as<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4512 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||specified by the data length and the busy signal is released. The second is when data transfers are stopped<br>at the block gap, by setting the Stop At Block Gap Request field in the Protocol Control register, and the data<br>transfers are completed. (after valid data is written to the SD card and the busy signal released).<br>In the case of a command with busy, this field is set when busy is deasserted.<br>This field is not asserted in tuning process.<br>0b - Transfer does not complete<br>1b - Transfer complete|
|0|Command complete|
|CC|This field is set when you receive the end field of the command response (except auto CMD12). See the<br>Command Inhibit (CMD) in the Present State register.<br>This field is not asserted in tuning process.<br>0b - Command not complete<br>1b - Command complete|



#### 78.7.1.15 Interrupt Status Enable (INT_STATUS_EN) 

##### Offset 

|Register|Offset|
|---|---|
|INT_STATUS_EN|34h|



##### Function 

Setting any bit in this register to 1 enables the corresponding interrupt status be requested to the system. If any bit is set to 0, the corresponding interrupt request gets blocked. 

- Depending on IABG field setting, uSDHC might be programmed to sample the card interrupt signal during the interrupt period and hold its value in the flip-flop. There are some delays on the Card Interrupt, asserted from the card, to the time the host system is informed. 

- To detect a CMD line conflict, the host driver must set both Command Timeout Error Status Enable and Command CRC Error Status Enable to 1. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4513 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|0|Reser|ved|DMAE|0|TNES|0|AC12E|0|DEBE|DCES|DTOE|CIESE|CEBE|CCES|CTOE|
|W||||SEN||EN||SEN||SEN|EN|SEN|N|SEN|EN|SEN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|0|TPSE|0|RTES|0|Rese|ved|CINTS|CRMS|CINSS|BRRS|BWRS|DINTS|BGES|TCSE|CCSE|
|W||N||EN||||EN|EN|EN|EN|EN|EN|EN|N|N|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31<br>—|Reserved|
|30-29<br>—|Reserved|
|28<br>DMAESEN|DMA error status enable<br>0b - Masked<br>1b - Enabled|
|27<br>—|Reserved|
|26<br>TNESEN|Tuning error status enable<br>0b - Masked<br>1b - Enabled|
|25<br>—|Reserved|
|24<br>AC12ESEN|Auto CMD12 error status enable<br>0b - Masked<br>1b - Enabled|
|23<br>|Reserved|
|—<br>22<br>DEBESEN|Data end bit error status enable<br>0b - Masked|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4514 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function<br>1b - Enabled|
|---|---|
|21<br>DCESEN|Data CRC error status enable<br>0b - Masked<br>1b - Enabled|
|20|Data timeout error status enable|
|DTOESEN|0b - Masked<br>1b - Enabled|
|19<br>CIESEN|Command index error status enable<br>0b - Masked<br>1b - Enabled|
|18|Command end bit error status enable|
|CEBESEN|0b - Masked<br>1b - Enabled|
|17<br>CCESEN|Command CRC error status enable<br>0b - Masked<br>1b - Enabled|
|16|Command timeout error status enable|
|CTOESEN|0b - Masked<br>1b - Enabled|
|15<br>—|Reserved|
|14<br>TPSEN|Tuning pass status enable<br>0b - Masked<br>1b - Enabled|
|13<br>—|Reserved|
|12|Re-tuning event status enable|
|RTESEN|0b - Masked<br>1b - Enabled|
|11<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4515 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|10-9<br>—|Reserved|
|8<br>CINTSEN|Card interrupt status enable<br>If this field is set to 0, uSDHC clears the interrupt request to the system. The Card Interrupt detection is<br>stopped when this field is cleared and restarted when this field is set to 1. The host driver should clear<br>the Card Interrupt Status Enable before servicing the Card Interrupt and should set this field again after all<br>interrupt requests from the card are cleared to prevent inadvertent interrupts.<br>0b - Masked<br>1b - Enabled|
|7|Card removal status enable|
|CRMSEN|0b - Masked<br>1b - Enabled|
|6|Card insertion status enable|
|CINSSEN|0b - Masked<br>1b - Enabled|
|5|Buffer read ready status enable|
|BRRSEN|0b - Masked<br>1b - Enabled|
|4|Buffer write ready status enable|
|BWRSEN|0b - Masked<br>1b - Enabled|
|3|DMA interrupt status enable|
|DINTSEN|0b - Masked<br>1b - Enabled|
|2|Block gap event status enable|
|BGESEN|0b - Masked<br>1b - Enabled|
|1|Transfer complete status enable|
|TCSEN|0b - Masked<br>1b - Enabled|
|0|Command complete status enable|
|CCSEN|0b - Masked|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4516 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||1b - Enabled|



#### 78.7.1.16 Interrupt Signal Enable (INT_SIGNAL_EN) 

##### Offset 

|Register|Offset|
|---|---|
|INT_SIGNAL_EN|38h|



##### Function 

This register is used to select which interrupt status is indicated to the host system as the interrupt. These status fields all share the same interrupt lines. Setting any of these fields to 1 enables interrupt generation. The corresponding Status register field generates an interrupt when the corresponding interrupt signal enable field is set. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|0|Reser|ved|DMAEI|0|TNEIE|0|AC12E|0|DEBEI|DCEIE|DTOEI|CIEIE|CEBEI|CCEIE|CTOEI|
|W||||EN||N||IEN||EN|N|EN|N|EN|N|EN|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|0|TPIEN|0|RTEIE|0|Rese|ved|CINTI|CRMI|CINSI|BRRIE|BWRI|DINTI|BGEIE|TCIEN|CCIEN|
|W||||N||||EN|EN|EN|N|EN|EN|N|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31<br>—|Reserved|
|30-29<br>—|Reserved|
|28|DMA error interrupt enable|
|DMAEIEN|0b - Masked|
||1b - Enable|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4517 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|27<br>—|Reserved|
|26<br>TNEIEN|Tuning error interrupt enable<br>0b - Masked<br>1b - Enabled|
|25<br>—|Reserved|
|24|Auto CMD12 error interrupt enable|
|AC12EIEN|0b - Masked<br>1b - Enabled|
|23<br>—|Reserved|
|22<br>DEBEIEN|Data end bit error interrupt enable<br>0b - Masked<br>1b - Enabled|
|21<br>DCEIEN|Data CRC error interrupt enable<br>0b - Masked<br>1b - Enabled|
|20<br>DTOEIEN|Data timeout error interrupt enable<br>0b - Masked<br>1b - Enabled|
|19<br>CIEIEN|Command index error interrupt enable<br>0b - Masked<br>1b - Enabled|
|18|Command end bit error interrupt enable|
|CEBEIEN|0b - Masked<br>1b - Enabled|
|17<br>CCEIEN|Command CRC error interrupt enable<br>0b - Masked<br>1b - Enabled|
|16|Command timeout error interrupt enable<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4518 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|CTOEIEN|0b - Masked<br>1b - Enabled|
|15<br>—|Reserved|
|14<br>TPIEN|Tuning Pass interrupt enable<br>0b - Masked<br>1b - Enabled|
|13<br>—|Reserved|
|12<br>RTEIEN|Re-tuning event interrupt enable<br>0b - Masked<br>1b - Enabled|
|11<br>—|Reserved|
|10-9<br>—|Reserved|
|8<br>CINTIEN|Card interrupt enable<br>0b - Masked<br>1b - Enabled|
|7<br>CRMIEN|Card removal interrupt enable<br>0b - Masked<br>1b - Enabled|
|6<br>CINSIEN|Card insertion interrupt enable<br>0b - Masked<br>1b - Enabled|
|5|Buffer read ready interrupt enable|
|BRRIEN|0b - Masked<br>1b - Enabled|
|4|Buffer write ready interrupt enable|
|BWRIEN|0b - Masked<br>1b - Enabled<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4519 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|3|DMA interrupt enable|
|DINTIEN|0b - Masked<br>1b - Enabled|
|2|Block gap event interrupt enable|
|BGEIEN|0b - Masked<br>1b - Enabled|
|1|Transfer complete interrupt enable|
|TCIEN|0b - Masked<br>1b - Enabled|
|0|Command complete interrupt enable|
|CCIEN|0b - Masked<br>1b - Enabled|



#### 78.7.1.17 Auto CMD12 Error Status (AUTOCMD12_ERR_STATUS) 

##### Offset 

|Register|Offset|
|---|---|
|AUTOCMD12_ERR_STA|3Ch|
|TUS||



##### Function 

When the Auto CMD12 Error Status field in the Status register is set, the host driver checks this register to identify what kind of error the Auto CMD12 / CMD 23 indicated. Auto CMD23 errors are indicated in field 04-01. This register is valid only when the Auto CMD12 Error status field is set. 

The table below shows the relationship between the Auto CMGD12 CRC Error and the Auto CMD12 Command Timeout Error. 

Table 688. Relationship between command CRC error and command timeout error for auto CMD12 

|Auto CMD12 CRC error|Auto CMD12 timeout error|Type of error|
|---|---|---|
|0|0|No error|
|0|1|Response timeout error|
|1|0|Response CRC error|
|1|1|CMD line conflict|



Changes in Auto CMD12 Error Status register can be classified in three scenarios: 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4520 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

- When uSDHC is going to issue an Auto CMD12 

   - Set field 0 to 1 if the Auto CMD12 cannot be issued due to an error in the previous command 

   - Set field 0 to 0 if the Auto CMD12 is issued 

- At the end field of an Auto CMD12 response 

   - Check errors correspond to fields 1-4 

   - Set fields 1-4 corresponding to detected errors 

   - Clear fields 1-4 corresponding to detected errors 

- Before reading the Auto CMD12 Error Status field 7 

   - Set field 7 to 1 if there is a command that can't be issued 

   - Clear field 7 if there is no command to issue 

The timing for generating the Auto CMD12 Error and writing to the Command register are asynchronous. After that, field 7 is sampled when the driver is not writing to the Command register. So, it is suggested to read this register only when the AC12E field in Interrupt Status register is set. An Auto CMD12 Error Interrupt is generated when one of the error fields (0-4) is set to 1. The Command Not Issued By Auto CMD12 Error does not generate an interrupt. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4521-14.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 SMP_ EXEC 0<br>W CLK... UTE...<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>CNIBA AC12I AC12E AC12C AC12T AC12N<br>R 0 0<br>C1... E  BE  E  OE  E<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31-24|Reserved|
|—||
|23|Sample clock select|
|SMP_CLK_SEL|This field is used to select sampling clock to receive CMD and DATA. This field is functional<br>only whenTUNING_CTRL[STD_TUNING_EN]is set. Otherwise, this field is reserved. This<br>field is controlled by re-tuning procedure and is valid after the tuning procedure is complete<br>(AUTOCMD12_ERR_STATUS[EXECUTE_TUNING]=0). A value of '1' means that tuning has been<br>completed successfully and a value of '0' implies the tuning has failed. Writing '1' to this field is meaningless<br>and ignored when the tuning has failed. The tuning circuit is reset by writing '0' to this field. This field can be<br>cleared by setting AUTOCMD12_ERR_STATUS[EXECUTE_TUNING]=1. Once the tuning circuit is reset,<br>it takes time to complete tuning sequence. Therefore, host driver should keep this field as 1 to perform|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4521 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||the re-tuning sequence in a short time. This field cannot be changed while the Host controller is receiving<br>response or a read data block.<br>0b - Fixed clock is used to sample data<br>1b - Tuned clock is used to sample data|
|22|Execute tuning|
|EXECUTE_TU<br>NING|This field is used to start the tuning procedure. This field is functional only when<br>TUNING_CTRL[STD_TUNING_EN]is set. Otherwise, this field is reserved. This field is set to start tuning<br>procedure and automatically cleared when tuning procedure is completed. The result of tuning is indicated<br>to AUTOCMD12_ERR_STATUS[SMP_CLK_SEL].<br>0b - Tuning procedure is aborted<br>1b - Start tuning procedure|
|21-8<br>—|Reserved|
|7<br>CNIBAC12E|Command not issued by Auto CMD12 error<br>Setting this field to 1 means CMD_wo_DAT is not executed due to an Auto CMD12 error (D04-D01) in<br>this register.<br>0b - No error<br>1b - Not issued|
|6-5<br>—|Reserved|
|4<br>AC12IE|Auto CMD12 / 23 index error<br>Occurs if the command index error occurs in response to a command.<br>0b - No error<br>1b - Error, the CMD index in response is not CMD12/23|
|3<br>AC12EBE|Auto CMD12 / 23 end bit error<br>Occurs when detecting that the end field of command response is 0 which should be 1.<br>0b - No error<br>1b - End bit error generated|
|2<br>AC12CE|Auto CMD12 / 23 CRC error<br>Occurs when detecting a CRC error in the command response.<br>0b - No CRC error<br>1b - CRC error met in Auto CMD12/23 response|
|1|Auto CMD12 / 23 timeout error<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4522 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|AC12TOE|Occurs if no response is returned within 64 SDCLK cycles from the end field of the command. If this field is<br>set to1, the other error status fields (2-4) have no meaning.<br>0b - No error<br>1b - Time out|
|0|Auto CMD12 not executed|
|AC12NE|If memory multiple block data transfer is not started, due to a command error, this field is not set because it is<br>not necessary to issue an Auto CMD12. Setting this field to 1 means uSDHC cannot issue the Auto CMD12<br>to stop a memory multiple block data transfer due to some error. If this field is set to 1, other error status fields<br>(1-4) have no meaning.<br>0b - Executed<br>1b - Not executed|



#### 78.7.1.18 Host Controller Capabilities (HOST_CTRL_CAP) 

##### Offset 

|Register|Offset|
|---|---|
|HOST_CTRL_CAP|40h|



##### Function 

This register provides the host driver with information specific to uSDHC implementation. The value in this register is the power-on-reset value and does not change with a software reset. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4523-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>ADMA<br>R 0 VS18  VS30  VS33  SRS  DMAS  HSS  0 MBL<br>S<br>W<br>Reset 0 0 0 0 0 1 1 1 1 1 1 1 0 0 1 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv Reserv Reserv Reserv<br>R USE_T ed  Reserved  ed  ed  ed<br>Reserved  Reserved<br>UN...<br>W<br>Reset 1 0 1 1 0 1 0 0 0 0 0 0 0 1 1 1<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4523 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Fields 

|Field|Function|
|---|---|
|31-27<br>—|Reserved|
|26<br>VS18|Voltage support 1.8 V<br>This field depends on the host system ability.<br>0b - 1.8 V not supported<br>1b - 1.8 V supported|
|25|Voltage support 3.0 V|
|VS30|This field depends on the host system ability.<br>0b - 3.0 V not supported|
||1b - 3.0 V supported|
|24|Voltage support 3.3 V|
|VS33|This field depends on the host system ability.<br>0b - 3.3 V not supported<br>1b - 3.3 V supported|
|23|Suspend / resume support|
|SRS|This field indicates whether uSDHC supports Suspend / Resume functionality. If this field is 0, the Suspend<br>and Resume mechanism, as well as the read wait, are not supported, and the host driver does not issue<br>either Suspend or Resume commands.<br>0b - Not supported<br>1b - Supported|
|22<br>DMAS|DMA support<br>This field indicates whether uSDHC can use the internal DMA to transfer data between system memory and<br>the data buffer directly.<br>0b - DMA not supported<br>1b - DMA supported|
|21<br>HSS|High speed support<br>This field indicates whether uSDHC supports High Speed mode and the host system can supply a SD clock<br>frequency from 25 MHz to 50 MHz.<br>0b - High speed not supported|
||1b - High speed supported|
|20|ADMA support|
|ADMAS|This field indicates whether uSDHC supports the ADMA feature.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4524 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Advanced DMA not supported<br>1b - Advanced DMA supported|
|19<br>—|Reserved|
|18-16<br>MBL|Max block length<br>This field indicates the maximum block size that the host driver can read and write to the buffer in uSDHC.<br>The buffer transfers block size without wait cycles.<br>000b - 512 bytes<br>001b - 1024 bytes<br>010b - 2048 bytes<br>011b - 4096 bytes|
|15-14<br>—|Reserved|
|13<br>USE_TUNING_<br>SDR50|Use Tuning for SDR50<br>This field is used to enable tuning for SDR50 mode<br>0b - SDR50 does not support tuning<br>1b - SDR50 supports tuning|
|12<br>—<br>11-8<br>—|Reserved<br>Reserved|
|7-3<br>—|Reserved|
|2<br>—|Reserved|
|1<br>—|Reserved|
|0<br>—|Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4525 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

#### 78.7.1.19 Watermark Level (WTMK_LVL) 

##### Offset 

|Register|Offset|
|---|---|
|WTMK_LVL|44h|



##### Function 

This register indicates configurability of write and read watermark levels (FIFO threshold). Their value can range from 1 to 128 words. Both write and read burst lengths are also configurable. Their value can range from 1 to 31 words. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4526-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>WR_BRST_LEN  WR_WML<br>W<br>Reset 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0<br>RD_BRST_LEN  RD_WML<br>W<br>Reset 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-29|Reserved|
|—||
|28-24|Write burst length due to system restriction, the actual burst length might not exceed 16|
|WR_BRST_LE<br>N|This field indicates the number of words uSDHC writes in a single burst. The write burst length must be less<br>than or equal to the write watermark level, and all bursts within a watermark level transfer is in back-to-back<br>mode. On reset, this field is 8. Writing 0 to this field results in '01000' (that is, it is not able to clear this field).|
|23-16|Write watermark level|
|WR_WML|This field indicates the number of words used as the watermark level (FIFO threshold) in a DMA write<br>operation. Also, the number of words as a sequence of write bursts in back-to-back mode. The maximum<br>legal value for the write watermark level is 128.|
|15-13<br>—|Reserved|
|12-8|Read burst length due to system restriction, the actual burst length might not exceed 16|
|RD_BRST_LEN||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4526 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||This field indicates the number of words uSDHC reads in a single burst. The read burst length must be less<br>than or equal to the read watermark level, and all bursts within a watermark level transfer is in back-to-back<br>mode. On reset, this field is 8. Writing 0 to this field results in '01000' (that is, it is not able to clear this field).|
|7-0|Read watermark level|
|RD_WML|This field indicates the number of words used as the watermark level (FIFO threshold) in a DMA read<br>operation. Also, the number of words as a sequence of read bursts in back-to-back mode. The maximum<br>legal value for the read water mark level is 128.|



#### 78.7.1.20 Mixer Control (MIX_CTRL) 

##### Offset 

|Register|Offset|
|---|---|
|MIX_CTRL|48h|



##### Function 

This register is used to DMA and data transfer. To prevent data loss, the software should check if data transfer is active before writing this register. These fields are DPSEL, MBSEL, DTDSEL, AC12EN, BCEN, and DMAEN. 

Table 689. Transfer type register setting for various transfer types 

|Multi/single block select|Block count enable|Block count|Function|
|---|---|---|---|
|0|Do not care|Do not care|Single transfer|
|1|0|Do not care|Infinite transfer|
|1|1|Positive number|Multiple transfer|
|1|1|Zero|No data transfer|



##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|Reserv|Reserv|Reserv|0|0|0|||0|||||0|||
|W|ed|ed|ed||||||||||||||
|Reset|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||0|||||AC23E|NIBBL|MSBS|DTDS|DDR_|AC12E|BCEN|DMAE|
|W|||||||||N|E_...|EL|EL|EN|N||N|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4527 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Fields 

|Field|Function|
|---|---|
|31<br>—|Reserved<br>Always write as 1.|
|30<br>—|Reserved<br>Always write as 0.|
|29<br>—|Reserved<br>Always write as 0.|
|28|Reserved|
|—<br>27<br>—|Reserved|
|26<br>—<br>25-22<br>—|Reserved<br>Reserved|
|21-8<br>—|Reserved|
|7<br>AC23EN|Auto CMD23 enable<br>This field is read/write whenVEND_SPEC[CMD_BYTE_EN]is disabled; otherwise, this field is read-only.<br>When this field is set to 1, the host controller issues a CMD23 automatically before issuing a command<br>specified in the Command Register.|
|6|Nibble position indication|
|NIBBLE_POS|This field indicates the nibble position in the DDR 4-bit mode. This field is read/write when<br>VEND_SPEC[CMD_BYTE_EN]is disabled; otherwise, this field is read-only. 0- the sequence is 'odd<br>high nibble -> even high nibble -> odd low nibble -> even low nibble'; 1- the sequence is 'odd high nibble -><br>odd low nibble -> even high nibble -> even low nibble'.|
|5<br>MSBSEL|Multi / Single block select<br>This field enables multiple block DATA line data transfers. This field is read/write when<br>VEND_SPEC[CMD_BYTE_EN]is disabled; otherwise, this field is read-only. For any other commands, this<br>field can be set to 0. If this field is 0, it is not necessary to set the Block Count register. SeeCommand<br>Transfer Type (CMD_XFR_TYP).<br>0b - Single block<br>1b - Multiple blocks|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4528 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|4|Data transfer direction select|
|DTDSEL|This field defines the direction of DATA line data transfers. This field is read/write when<br>VEND_SPEC[CMD_BYTE_EN]is disabled; otherwise, this field is read-only. The field is set to 1 by<br>the host driver to transfer data from the SD card to uSDHC and is set to 0 for all other commands.<br>0b - Write (Host to card)<br>1b - Read (Card to host)|
|3<br>DDR_EN|Dual data rate mode selection<br>This field is read/write whenVEND_SPEC[CMD_BYTE_EN]is disabled; otherwise, this field is read-only.|
|2<br>AC12EN|Auto CMD12 enable<br>Multiple block transfers for memory require a CMD12 to stop the transaction. This field is read/write when<br>VEND_SPEC[CMD_BYTE_EN]is disabled; otherwise, this field is read-only. When this field is set to 1,<br>uSDHC issues a CMD12 automatically when the last block transfer has completed. The host driver is not set<br>this field to issue commands that do not require CMD12 to stop a multiple block data transfer. In particular,<br>secure commands defined in File Security Specification (see reference list) do not require CMD12. In single<br>block transfer, uSDHC ignores this field no matter it is set or not.<br>0b - Disable<br>1b - Enable|
|1<br>BCEN|Block count enable<br>This field is used to enable the Block Count register, which is only relevant for multiple block transfers. This<br>field is read/write whenVEND_SPEC[CMD_BYTE_EN]is disabled; otherwise, this field is read-only. When<br>this field is 0, the internal counter for block is disabled, which is useful in executing an infinite transfer.<br>0b - Disable<br>1b - Enable|
|0<br>DMAEN|DMA enable<br>This field enables DMA functionality. This field is read/write whenVEND_SPEC[CMD_BYTE_EN]is<br>disabled; otherwise, this field is read-only. If this field is set to 1, a DMA operation begins when the host driver<br>sets the DPSEL field of this register. Whether the simple DMA or the advanced DMA is active depends on<br>the DMA Select field of the Protocol Control register.<br>0b - Disable<br>1b - Enable|



#### 78.7.1.21 Force Event (FORCE_EVENT) 

##### Offset 

|Register|Offset|
|---|---|
|FORCE_EVENT|50h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4529 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Function 

This register is not a physically implemented register. Rather, it is an address at which the Interrupt Status register can be written if the corresponding field of the Interrupt Status Enable Register is set. This register is a write only register and writing 0 to it has no effect. Writing 1 to this register sets the corresponding field of Interrupt Status register. A read from this register always results in 0's. to change the corresponding status fields in the Interrupt Status register, make sure to set IPGEN field in System Control Register so that peripheral clock is always active. 

Forcing a card interrupt generates a short pulse on the DATA1 line, and the driver might treat this interrupt as a normal interrupt. The interrupt service routine might skip polling the card interrupt factor as the interrupt is self cleared. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4530-06.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>FEVT FEVT FEVTT FEVT FEVT FEVT FEVT FEVT FEVT FEVT FEVT<br>W<br>CINT  DMAE  NE  AC1... DEBE  DCE  DTOE  CIE  CEBE  CCE  CTOE<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 0 0 0 0 0 0<br>FEVT FEVTA FEVTA FEVTA FEVTA FEVTA<br>W<br>CNI... C1... C1... C1... C1... C1...<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|Force event card interrupt|
|FEVTCINT|Writing 1 to this field generates a short low-level pulse on the internal DATA1 line, as if a self-clearing<br>interrupt was received from the external card. If enabled, the CINT field is set and the interrupt service<br>routine might treat this interrupt as a normal interrupt from the external card.|
|30-29<br>—|Reserved|
|28|Force event DMA error|
|FEVTDMAE|Forces the DMAE field of Interrupt Status register to be set|
|27<br>—|Reserved|
|26|Force tuning error|
|FEVTTNE|Forces the TNE field of Interrupt Status register to be set|
|25<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4530 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|24<br>FEVTAC12E|Force event Auto Command 12 error<br>Forces the AC12E field of Interrupt Status register to be set|
|23<br>—|Reserved|
|22<br>FEVTDEBE|Force event data end bit error<br>Forces the DEBE field of Interrupt Status register to be set|
|21<br>FEVTDCE|Force event data CRC error<br>Forces the DCE field of Interrupt Status register to be set|
|20<br>FEVTDTOE|Force event data time out error<br>Force the DTOE field of Interrupt Status register to be set|
|19<br>FEVTCIE|Force event command index error<br>Forces the CCE field of Interrupt Status register to be set|
|18<br>FEVTCEBE|Force event command end bit error<br>Forces the CEBE field of Interrupt Status register to be set|
|17<br>FEVTCCE|Force event command CRC error<br>Forces the CCE field of Interrupt Status register to be set|
|16<br>FEVTCTOE|Force event command time out error<br>Forces the CTOE field of Interrupt Status register to be set|
|15-8<br>—|Reserved|
|7|Force event command not executed by Auto Command 12 error|
|FEVTCNIBAC1<br>2E|Forces the CNIBAC12E field in the Auto Command12 Error Status register to be set|
|6-5<br>—|Reserved|
|4<br>FEVTAC12IE|Force event Auto Command 12 index error<br>Forces the AC12IE field in the Auto Command12 Error Status register to be set|
|3|Force event Auto Command 12 end bit error|
|FEVTAC12EBE|Forces the AC12EBE field in the Auto Command12 Error Status register to be set|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4531 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|2|Force event auto command 12 CRC error|
|FEVTAC12CE|Forces the AC12CE field in the Auto Command12 Error Status register to be set|
|1|Force event auto command 12 time out error|
|FEVTAC12TOE|Forces the AC12TOE field in the Auto Command12 Error Status register to be set|
|0|Force event auto command 12 not executed|
|FEVTAC12NE|Forces the AC12NE field in the Auto Command12 Error Status register to be set|



#### 78.7.1.22 ADMA Error Status (ADMA_ERR_STATUS) 

##### Offset 

|Register|Offset|
|---|---|
|ADMA_ERR_STATUS|54h|



##### Function 

When an ADMA Error Interrupt has occurred, the ADMA error sates field in this register holds the ADMA state and the ADMA System Address register holds the address around the error descriptor. 

For recovering from this error, the host driver requires the ADMA state to identify the error descriptor address as follows: 

- ST_STOP: Previous location set in the ADMA System Address register is the error descriptor address. 

- ST_FDS: Current location set in the ADMA System Address register is the error descriptor address. 

- ST_CADR: This state is never set because it only increments the descriptor pointer and does not generate an ADMA error. 

- ST_TFR: Previous location set in the ADMA System Address register is the error descriptor address. 

In case of a write operation, the host driver should use the ACMD22 to get the number of the written block, rather than using this information, because unwritten data might exist in the host controller. 

The host controller generates the ADMA Error Interrupt when it detects invalid descriptor data (Valid=0) in the ST_FDS state. The host driver can distinguish this error by reading the Valid field of the error descriptor. 

Table 690. ADMA error state coding 

|D01-D00|ADMA error state (when error<br>has occurred)|Contents ofADMA System<br>Address register|
|---|---|---|
|00|ST_STOP (Stop DMA)|Holds the address of the next executable<br>descriptor command|
|01|ST_FDS (Fetch descriptor)|Holds the valid descriptor address|
|10|ST_CADR (Change address)|No ADMA error is generated|
||Table continues on the next page...||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4532 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table 690. ADMA error state coding (continued) 

|D01-D0|0|||||ADMA er<br>has occu|ror stat<br>rred)|e (when|error||Con<br>Add|tents o<br>ress re|fADMA<br>gister|System|||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|11||||||ST_TFR|(Transf|er data)|||Hold<br>desc|s the a<br>riptor|ddress<br>comman|of the ne<br>d|xt exe|cutable|
|Diagram<br>Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||0|||||||ADMA<br>DCE|ADMA<br>LME|ADM|AES|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Diagram 

##### Fields 

|Field|Function|
|---|---|
|31-4|Reserved|
|—||
|3|ADMA descriptor error|
|ADMADCE|This error occurs when invalid descriptor fetched by ADMA.<br>0b - No error<br>1b - Error|
|2|ADMA length mismatch error|
|ADMALME|This error occurs in the following two cases:<br>• While the block count enable is being set, the total data length specified by the descriptor table is<br>different from that specified by the block count and block length.<br>• Total data length cannot be divided by the block length.<br>0b - No error<br>1b - Error|
|1-0<br>ADMAES|ADMA error state (when ADMA error is occurred)<br>This field indicates the state of the ADMA when an error has occurred during an ADMA data transfer. See<br>ADMA Error Status (ADMA_ERR_STATUS)for more details.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4533 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

#### 78.7.1.23 ADMA System Address (ADMA_SYS_ADDR) 

##### Offset 

|Register|Offset|
|---|---|
|ADMA_SYS_ADDR|58h|



##### Function 

This register holds the word address of the executing command in the Descriptor table. At the start of ADMA, the host driver sets the start address of the Descriptor table. The ADMA engine increments this register address whenever fetching a Descriptor command. When the ADMA is stopped at the Block Gap, this register indicates the address of the next executable Descriptor command. When the ADMA Error Interrupt is generated, this register holds the valid Descriptor address depending on the ADMA state. The lower 2 bits of this register is tied to '0' so the ADMA address is always word aligned. 

Because this register supports dynamic address reflecting, when TC field is set, it automatically alters the value of internal address counter, so the software cannot change this register when TC field is set. Such restriction is also listed in Software restrictions. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||ADS_|ADDR|||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1<br>0|
|R<br>W|||||||ADS_|ADDR|||||||0|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>0|



##### Fields 

|Field|Function|
|---|---|
|31-2|ADMA system address|
|ADS_ADDR|This field contains the physical system memory address used for ADMA transfers.|
|1-0<br>—|Reserved|



#### 78.7.1.24 DLL (Delay Line) Control (DLL_CTRL) 

##### Offset 

|Register|Offset|
|---|---|
|DLL_CTRL|60h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4534 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Function 

This register contains control fields for DLL. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|DLL_C|TRL_REF|_UPDAT|E_INT|||DLL_|CTRL_SL|V_UPDAT|E_INT|||0|DLL_C|TRL_SLV<br>ARGET1|_DLY_T<br>|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||DLL_|CTRL_|SLV_OVE|RRIDE_V|AL||DLL_C<br>TR...|DLL_C<br>TR...|DLL_CT|RL_SLV_|DLY_TA|RGET0|DLL_C<br>TR...|DLL_C<br>TR...|DLL_C<br>TR...|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-28|DLL control loop update interval|
|DLL_CTRL_RE<br>F_UPDATE_IN<br>T|The interval cycle is (2 + REF_UPDATE_INT) * REF_CLOCK. By default, the DLL control loop updates every<br>two REF_CLOCK cycles. It should be noted that increasing the reference delay-line update interval reduces<br>the ability of the DLL to adjust to fast changes in conditions that might effect the delay (such as voltage<br>and temperature)|
|27-20|Slave delay line update interval|
|DLL_CTRL_SL|If default 0 is used, it means 256 cycles of REF_CLOCK. A value of 0x0f results in 15 cycles and so on. Note|
|V_UPDATE_IN<br>T|that software can always cause an update of the slave-delay line using the SLV_FORCE_UPDATE register.<br>Note that the slave delay line also updates automatically when the reference DLL transitions to a locked<br>state (from an un-locked state).|
|19|Reserved|
|—||
|18-16|DLL slave delay target1|
|DLL_CTRL_SL<br>V_DLY_TARGE<br>T1|See DLL_CTRL_SLV_DLY_TARGET0 below.|
|15-9|DLL slave override val|
|DLL_CTRL_SL<br>V_OVERRIDE_<br>VAL|When SLV_OVERRIDE = 1, this field is used to select 1 of 128 physical taps manually. A value of 0 selects<br>tap 1, and a value of 0x7f selects tap 128.|
|8|DLL slave override|
|DLL_CTRL_SL<br>V_OVERRIDE||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4535 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||Set this field to 1 to Enable manual override for slave delay chain using SLV_OVERRIDE_VAL; to set 0 to<br>disable manual override. This feature does not require the DLL to be enabled using the ENABLE field. In<br>fact to reduce power, if SLV_OVERRIDE is used, it is recommended to disable the DLL with ENABLE = 0|
|7|DLL gate update|
|DLL_CTRL_GA<br>TE_UPDATE|Set this field to 1 to prevent the DLL from updating (because when clock_in exists, glitches might appear<br>during DLL updates). This field might be used by software if such a condition occurs. Clear the bit to 0 to<br>allow the DLL to update automatically.|
|6-3|DLL slave delay target0|
|DLL_CTRL_SL<br>V_DLY_TARGE<br>T0|The delay target for uSDHC loopback read clock can be programmed in 1/16th increments of an<br>ref_clock half-period. The delay is (({DLL_CTRL_SLV_DLY_TARGET1,DLL_CTRL_SLV_DLY_TARGET0}<br>+1)* REF_CLOCK / 2) / 16 So the input read-clock can be delayed relative input data from (REF_CLOCK /<br>2) / 16 to REF_CLOCK * 4.<br>For the restrictions of delay cell implementation, the delay target must be set between<br>REF_CLOCK/16 and REF_CLOCK*2 when REF_CLOCK is running at 200 MHz. When<br>REF_CLOCK frequency is slower than 100 MHz, the maximum delay target might not<br>reach REF_CLOCK*2.<br>~~NOTE~~|
|2|DLL slave delay line|
|DLL_CTRL_SL<br>V_FORCE_UP<br>D|Setting this field to 1, forces the slave delay line to update to the DLL calibrated value immediately. The slave<br>delay line updates automatically based on the SLV_UPDATE_INT interval or when a DLL lock condition is<br>sensed. Subsequent forcing of the slave-line update can only occur if SLV_FORCE_UP is set back to 0 and<br>then asserted again (edge triggered). Be sure to use it when uSDHC is idle. This function might not work<br>when uSDHC is working on data / cmd / response.|
|1|DLL reset|
|DLL_CTRL_RE<br>SET|Setting this field to 1 force a reset on DLL. This causes the DLL to lose lock and re-calibrate to detect<br>an REF_CLOCK half period phase shift. This signal is used by the DLL as edge-sensitive, so to create a<br>subsequent reset, RESET must be taken low and then asserted again.|
|0|DLL and delay chain|
|DLL_CTRL_EN<br>ABLE|Set this field to 1 to enable the DLL and delay chain; otherwise; set to 0 to bypasses DLL. Note that using the<br>slave delay line override feature with SLV_OVERRIDE and SLV_OVERRIDE VAL, the DLL does not need<br>to be enabled.|



#### 78.7.1.25 DLL Status (DLL_STATUS) 

##### Offset 

|Register|Offset|
|---|---|
|DLL_STATUS|64h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4536 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Function 

This register contains the DLL status information. All fields are read only and reads the same as the power-reset value. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||0|||||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||DLL_|STS_REF|_SEL|||||DLL_S|TS_SLV|_SEL|||DLL_S<br>TS...|DLL_S<br>TS...|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|1|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-16|Reserved|
|—||
|15-9|Reference delay line select taps|
|DLL_STS_REF<br>_SEL|This is encoded by 7 fields for 127 taps.|
|8-2|Slave delay line select status|
|DLL_STS_SLV_<br>SEL|This is the instant value generated from reference chain. Because the reference chain can only be updated<br>when REF_CLOCK is detected, this value should be the right value to be updated when the reference<br>is locked.|
|1|Reference DLL lock status|
|DLL_STS_REF<br>_LOCK|This signifies that the DLL has detected and locked to a half-phase ref_clock shift, allowing the slave<br>delay-line to perform programmed clock delays|
|0|Slave delay-line lock status|
|DLL_STS_SLV_<br>LOCK|This signifies that a valid calibration has been set to the slave-delay line and that the slave-delay line is<br>implementing the programmed delay value|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4537 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

#### 78.7.1.26 CLK Tuning Control and Status (CLK_TUNE_CTRL_STATUS) 

##### Offset 

|Register|Offset|
|---|---|
|CLK_TUNE_CTRL_STA|68h|
|TUS||



##### Function 

This register contains the Clock Tuning Control status information. This register is added to support SD3.0 UHS-I SDR104 mode. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23<br>22|21|20|19<br>18|17<br>16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|PRE_<br>ERR|||TA|P_SEL_P|RE|||TAP_SE|L_OUT||TAP_S|EL_POST|
|W||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0<br>0|0|0|0<br>0|0<br>0|
|Bits|15|14|13|12|11|10|9|8|7<br>6|5|4|3<br>2|1<br>0|
|R<br>W|NXT_<br>ERR|||DLY_C|ELL_SET|_PRE|||DLY_CELL|_SET_OUT||DLY_CELL|_SET_POST|
|Reset|0|0|0|0|0|0|0|0|0<br>0|0|0|0<br>0|0<br>0|



##### Fields 

|Field|Function|
|---|---|
|31|PRE error|
|PRE_ERR|PRE error which means the number of delay cells added on the feedback clock is too small. It is valid only<br>when SMP_CLK_SEL of Mix control register (bit23 of 0x48) is enabled.|
|30-24|TAP_SEL_PRE|
|TAP_SEL_PRE|Reflects the number of delay cells added on the feedback clock between the feedback clock and CLK_PRE.<br>When AUTO_TUNE_EN (bit24 of 0x48) is disabled, TAP_SEL_PRE is always equal<br>to DLY_CELL_SET_PRE.<br>When AUTO_TUNE_EN (bit24 of 0x48) is enabled, TAP_SEL_PRE is updated automatically according to<br>the status of the auto tuning circuit to adjust the sample clock phase.|
|23-20|Delay cells added on the feedback clock between CLK_PRE and CLK_OUT|
|TAP_SEL_OUT|Reflects the number of delay cells added on the feedback clock between CLK_PRE and CLK_OUT.|
|19-16|Delay cells added on the feedback clock between CLK_OUT and CLK_POST<br>Reflects the number of delay cells added on the feedback clock between CLK_OUT and CLK_POST.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4538 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|TAP_SEL_POS<br>T||
|15|NXT error|
|NXT_ERR|NXT error which means the number of delay cells added on the feedback clock is too large. It's valid only<br>when SMP_CLK_SEL of Mix control register (bit23 of 0x48) is enabled.|
|14-8|delay cells on the feedback clock between the feedback clock and CLK_PRE|
|DLY_CELL_SE<br>T_PRE|Set the number of delay cells on the feedback clock between the feedback clock and CLK_PRE.|
|7-4|Delay cells on the feedback clock between CLK_PRE and CLK_OUT|
|DLY_CELL_SE<br>T_OUT|Set the number of delay cells on the feedback clock between CLK_PRE and CLK_OUT.|
|3-0|Delay cells on the feedback clock between CLK_OUT and CLK_POST|
|DLY_CELL_SE<br>T_POST|Set the number of delay cells on the feedback clock between CLK_OUT and CLK_POST.|



#### 78.7.1.27 Vendor Specific Register (VEND_SPEC) 

##### Offset 

|Register|Offset|
|---|---|
|VEND_SPEC|C0h|



##### Function 

This register contains the vendor specific control/status register. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4539-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved<br>CMD_ Reserv Reserv Reserv<br>Reserved<br>W BYT... ed  ed  ed<br>Reset 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>Reserv<br>R 0 0 0<br>CRC_ ed  Reserv FRC_ Reserv Reserv AC12_ CONF Reserv EXT_D<br>CHK... ed  SDC... ed  ed  WR... LIC... ed  MA...<br>W<br>Reset 0 1 1 1 1 0 0 0 0 0 0 0 1 0 0 1<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4539 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Fields 

|Field<br>31<br>CMD_BYTE_E<br>N|Function<br>Register byte access for CMD_XFR_TYP<br>This field controls the register byte access forCommand Transfer Type (CMD_XFR_TYP). If this field is<br>enabled, the register can be configured through byte write enable. IPS_bus can write only one byte once for<br>one write operation.<br>0b - Disable. MIX_CTRL[7:0] is read/write and CMD_XFR_TYP[7:0] is read-only.<br>1b - Enable. MIX_CTRL[7:0] is read-only and CMD_XFR_TYP[7:0] is read/write.|
|---|---|
|30<br>—|Reserved<br>Always write as 0.|
|29<br>—|Reserved<br>Always write as 1|
|28<br>—|Reserved<br>Always write as 0.|
|27-24<br>—|Reserved<br>Always write as 4'b0000.|
|23-16<br>—|Reserved<br>Always write as 8'h00.|
|15<br>CRC_CHK_DIS|CRC Check Disable<br>0b - Check CRC16 for every read data packet and check CRC fields for every write data packet<br>1b - Ignore CRC16 check for every read data packet and ignore CRC fields check for every write<br>data packet|
|14-11<br>—|Reserved<br>Reserved|
|10<br>—|Reserved<br>Always write as 0.|
|9<br>—|Reserved<br>Always write as 0.|
|8<br>FRC_SDCLK_O<br>N|Force CLK<br>Force CLK output active<br>Do not set this bit to 1 unless it is necessary. Also, make sure that this bit is cleared when uSDHC’s clock<br>is about to be changed (frequency change, clock source change, or delay chain tuning).<br>0b - CLK active or inactive is fully controlled by the hardware.<br>1b - Force CLK active|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4540 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|7<br>—|Reserved|
|6<br>—<br>5<br>—<br>4|Reserved<br>Reserved<br>Reserved|
|—<br>3|Check busy enable|
|AC12_WR_CH<br>KBUSY_EN|Check busy enable after auto CMD12 for write data packet<br>0b - Do not check busy after auto CMD12 for write data packet<br>1b - Check busy after auto CMD12 for write data packet|
|2|Conflict check enable|
|CONFLICT_CH<br>K_EN|It is not implemented in uSDHC IP.<br>0b - Conflict check disable<br>1b - Conflict check enable|
|1<br>—<br>0<br>EXT_DMA_EN|Reserved<br>External DMA request enable<br>Enable the request to external DMA. When the internal DMA (either Simple DMA or Advanced DMA) is not<br>in use, and this field is set, uSDHC sends out DMA request when the internal buffer is ready. This field is<br>particularly useful when transferring data by Arm platform polling mode, and it is not allowed to send out the<br>external DMA request. By default, this field is set.<br>0b - In any scenario, uSDHC does not send out external DMA request.<br>1b - When internal DMA is not active, the external DMA request is sent out.|



#### 78.7.1.28 eMMC Boot (MMC_BOOT) 

##### Offset 

|Register|Offset|
|---|---|
|MMC_BOOT|C4h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4541 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Function 

This register contains the eMMC Fast Boot control register. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||BOOT_B|LK_CNT||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||0||||DISAB<br>LE...|AUTO<br>_SA...|BOOT<br>_EN|BOOT<br>_MO...|BOOT<br>_ACK||DTOC|V_ACK||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-16|Stop At Block Gap value of automatic mode|
|BOOT_BLK_CN<br>T|The value defines the Stop At Block Gap value of automatic mode. When received, card block cnt is equal<br>to (BLK_CNT - BOOT_BLK_CNT) and AUTO_SABG_EN is 1, then Stop At Block Gap.<br>Here, BLK_CNT is defined in the Block Attributes Register, field 31 - 16 of 0x04.|
|15-9<br>—|Reserved|
|8|Time out|
|DISABLE_TIME<br>_OUT|When this field is set, there is no timeout check no matter whether BOOT_EN is set or not.<br>~~NOTE~~|
||0b - Enable time out|
||1b - Disable time out|
|7|Auto stop at block gap|
|AUTO_SABG_E<br>N|During boot, enable auto stop at block gap function. This function is triggered, and host stops at block gap<br>when received card block cnt is equal to (BLK_CNT - BOOT_BLK_CNT).|
|6|Boot enable|
|BOOT_EN|Boot mode enable<br>0b - Fast boot disable|
||1b - Fast boot enable|
|5|Boot mode|
|BOOT_MODE|Boot mode select|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4542 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Normal boot|
||1b - Alternative boot|
|4<br>BOOT_ACK|BOOT ACK<br>Boot ACK mode select<br>0b - No ack|
||1b - Ack|
|3-0|Boot ACK time out|
|DTOCV_ACK|Boot ACK time out counter value.<br>0000b - SDCLK x 2^14|
||0001b - SDCLK x 2^15|
||0010b - SDCLK x 2^16|
||0011b - SDCLK x 2^17|
||0100b - SDCLK x 2^18|
||0101b - SDCLK x 2^19|
||0110b - SDCLK x 2^20|
||0111b - SDCLK x 2^21|
||1110b - SDCLK x 2^28|
||1111b - SDCLK x 2^29|



#### 78.7.1.29 Vendor Specific 2 Register (VEND_SPEC2) 

##### Offset 

|Register|Offset|
|---|---|
|VEND_SPEC2|C8h|



##### Function 

This register contains the vendor specific control 2 register. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4543 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Diagram 

|Bits<br>R<br>W|31|30|29|28|27|26|25|24<br>Rese|23<br>rved|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|Reserv|Reserv|Reserv|Reserv|Rese|rved|0||0|TUNIN|TUNIN|TUNIN|CARD||0||
|W|ed|ed|ed|ed||||||G_...|G_...|G_...|_IN...||||
|Reset|1|0|0|1|0|0|0|0|0|0|0|0|0|1|1|0|



##### Fields 

|Field|Function|
|---|---|
|31-15|Reserved|
|—||
|14|Reserved|
|—<br>13|Reserved|
|—||
|12|Reserved|
|—||
|11-10|Reserved|
|—<br>9<br>—|Reserved|
|8-7<br>—<br>6|Reserved<br>Tuning command enable|
|TUNING_CMD_<br>EN|Enable the auto tuning circuit to check the CMD line.<br>0b - Auto tuning circuit does not check the CMD line.<br>1b - Auto tuning circuit checks the CMD line.|
|5|Tuning 1bit enable|
|TUNING_1bit_E<br>N|Enables the auto tuning circuit to check the DATA0 only. It is used with the TUNING_8bit_EN together.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4544 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|4<br>TUNING_8bit_E<br>N|Tuning 8bit enable<br>Enable the auto tuning circuit to check the DATA[7:0]. It is used with the TUNING_1bit_EN together.<br>0b00 - Tuning circuit only checks the DATA[3:0]<br>0b01 - Tuning circuit only checks the DATA0<br>0b10 - Tuning circuit checks the whole DATA[7:0]<br>0b11 - Invalid<br>The format of these two fields are [TUNNING_8bit_EN:TUNNING_1bit_EN].<br>~~NOTE~~|
||In SDIO mode, auto-tuning only supports 1-bit [DATA(0)] tuning and the 4-bit [DATA(3:0)]<br>autotuning in not supported for SDIO mode. SD mode supports 1-bit/4-bit [DATA(0)] and<br>[DATA(3:0)] auto tuning. SD mode supports 1-bit/4-bit/8-bit [DATA(0)], [DATA(3:0)], and<br>[DATA(7:0)] auto tuning.<br>~~NOTE~~|
|3<br>CARD_INT_D3_<br>TEST|Card interrupt detection test<br>This field is used only for debugging.<br>0b - Check the card interrupt only when DATA3 is high.<br>1b - Check the card interrupt by ignoring the status of DATA3.|
|2-0<br>—|Reserved|



#### 78.7.1.30 Tuning Control (TUNING_CTRL) 

##### Offset 

|Register|Offset|
|---|---|
|TUNING_CTRL|CCh|



##### Function 

The register contains configuration of tuning circuit. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4545 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Communication/078_Ultra_Secured_Digital_Host_Controller_-uSDHC-/S32K3XXRM_数据表.pdf-4546-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv Reserv<br>R Reserved  STD_T ed  TUNING_WINDOW  ed  TUNING_STEP<br>UN...<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DIS_C<br>TUNING_COUNTER  TUNING_START_TAP<br>W MD...<br>Reset 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31-25<br>—|Reserved|
|24|Standard tuning circuit and procedure enable|
|STD_TUNING_<br>EN|This field is used to enable standard tuning circuit and procedure.|
|23|Reserved|
|—<br>22-20|Data window|
|TUNING_WIND<br>OW|Select data window value for auto tuning|
|19|Reserved|
|—<br>18-16|TUNING_STEP|
|TUNING_STEP|The increasing delay cell steps in tuning procedure.|
|15-8|Tuning counter|
|TUNING_COU<br>NTER|The MAX repeat CMD19 times in tuning procedure.|
|7|Disable command check for standard tuning|
|DIS_CMD_CHK<br>_FOR_STD_TU<br>NING|Writing 1 to this field disables command check (command CRC, CMD end bit error, and CMD index error<br>or CMD timeout error) for standard tuning flow after each tuning command is sent.|
|6-0|Tuning start|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4546 / 4640 

NXP Semiconductors 

Ultra Secured Digital Host Controller (uSDHC) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|TUNING_STAR<br>T_TAP|The start delay cell point when send first CMD19 in tuning procedure.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4547 / 4640 

