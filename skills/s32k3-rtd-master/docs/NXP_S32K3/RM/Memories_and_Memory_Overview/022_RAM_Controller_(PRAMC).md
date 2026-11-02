NXP Semiconductors 

# Chapter 22 RAM Controller (PRAMC) 

## 22.1 Chip-specific PRAMC information 

### 22.1.1 PRAMC instances and configuration 

Table 98. PRAMC instances and configuration 

|Instance|SRAM array|Size (KB)|Applicability|
|---|---|---|---|
|PRAMC_0|SRAM 0|32|S32K3x4, S32K342, S32K312, S32K311|
||SRAM 0|128|S32K3x4 (128KB support)|
||||S32K342 (32KB support)|
||||S32K312 (64KB support)|
||SRAM 0|256|S32K358|
|PRAMC_1|SRAM 1|32|S32K3x4|
||SRAM 1|128|S32K3x4|
||SRAM 1|256|S32K358|
|PRAMC_2|SRAM 2|256|S32K358|



### 22.1.2 RAM initialization 

After chip power-on reset, you must initialize RAM to a known value using a 64-bit master before 32-bit masters can read or write to RAM. If you do not initialize RAM this way, any attempt to execute a 32-bit read or write access terminates with an uncorrectable ECC error event on this chip. 

### 22.1.3 SRAM0 behavior while XRDC is configured to block access to SRAM0 

While XRDC is configured to restrict access to SRAM0, the below behaviors should be considered: 

1. In case if XRDC is configured to restrict access to SRAM0 and a read transaction to SRAM0 is performed: To ensure faster SRAM0 accesses, the access is routed to SRAM0 and blocked by PRAMC if XRDC is configured to block access. In such a case, if an error is present on the SRAM0 data, (that is error on data or error injected by EIM), the same is latched by ERM as well. This data is not used by application core since PRAMC gives a bus error in this case. 

2. In case if XRDC is configured to restrict access to SRAM0 and a 32-bit write access is performed: Since SRAM is 64-bit wide, so a 32-bit write transaction is performed as a read-modify-write. In the read cycle, again as described in previous scenario, the PRAMC will initiate an error response. In this case also, if there is any error on SRAM0 data bus (i.e., error or error injected via EIM), the same is captured in ERM as well. 

## 22.2 Introduction 

The RAM controller is an interface between the system bus (AHB-Lite 2.v6) and the integrated system RAM. It converts the protocols between the system bus and the dedicated RAM array interface. 

The RAM controller supports one 64-bit AHB interface and a 64-bit RAM array interface. The AHB port provides a connection to the platform crossbar for direct RAM access from the various crossbar masters. Shown below in Figure 48 is a simplified block diagram depicting the position of the RAM controller within a typical platform architecture. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

734 / 4640 

NXP Semiconductors 

RAM Controller (PRAMC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/022_RAM_Controller_-PRAMC-/S32K3XXRM_数据表.pdf-0735-02.png)


<!-- Start of picture text -->
Platform<br>Core<br>PRAM_CTL RAM<br>Complex<br>AHB AXBS AHB<br>DMA2<br>Off-platform<br>master<br><!-- End of picture text -->

Figure 48. Simplified platform block diagram 

The following list summarizes the key features of the RAM controller: 

- System bus supports 64-bit data 

- Array interface supports a 64-bit data + 8-bit ECC interface 

- Late-write support via 64-bit data + 8-bit ECC storage buffer supports single-cycle write accesses 

- Configurable read access timing (zero or one wait state programmable) allowing use in large range of frequency targets 

- Read-modify-write operation supports array write size smaller than a doubleword 

- Hardware EDC after ECC feature to check the ECC logic. Detected errors are connected to the FCCU with configurable error reaction. 

The address path of the RAM controller contains a MUX that chooses among the addresses presented on the system bus for a read request—either the address from the temporary holding register or the address from the late-write buffer. The temporary holding register contains the address presented during the AHB address phase of the write request. The request is delayed when being presented to the RAM by one cycle. This step makes it possible to simultaneously present the address and associated write data, which is not valid until the AHB data phase. The late-write buffer holds write requests that are delayed to facilitate single-cycle response on the system bus. 

The read data path contains a MUX that chooses the source of the read data to be presented on the system bus on a read request. When a read request matches the contents of the late-write buffer, a RAM access is not required, and the late-write buffer contents are transferred to the read data bus. Otherwise, the read data is a result of a RAM access. 

The write data path contains the MUX that chooses the source of the write data, as well as the control logic for generating read-modify-write operations on writes less than 64 bits in size. A write operation can be performed to empty the contents of the late-write buffer. In the case of back-to-back writes, the write may be forced to bypass the late-write buffer and instead be stored directly in RAM. 

## 22.3 Functional description 

This section describes the functions of the RAM controller. 

### 22.3.1 Read and write operations 

The RAM controller processes read and write requests to on-chip RAM and provides a register interface for access to performance tuning functions. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

735 / 4640 

NXP Semiconductors 

RAM Controller (PRAMC) 

~~<mark>NOTE</mark>~~ 

The RAM controller register interface is accessible only in supervisor mode. Accesses in user mode return a transfer error. 

#### 22.3.1.1 Reads 

Read transfers, of any size, can be configured to complete with a zero or one additional wait state response on the system bus. 

#### 22.3.1.2 Optional read wait state 

The RAM controller can be optionally programmed to register RAM read data prior to returning it on the system bus. Setting the PRCRx[FT_DIS] field inserts a register in the read data path for use when operating the controller at high frequencies. The state of PRCRx[FT_DIS] field has no effect on writes. 

A random, initial access takes two clock cycles (2T) to complete if PRCRx[FT_DIS]=0, and a WRAP4 burst will have an access time of 2-2-2-2. A random, initial access takes three clock cycles (3T) to complete if PRCRx[FT_DIS]=1, and a WRAP4 burst has an access time of 3-2-2-2. 

~~<mark>NOTE</mark>~~ 

The number of cycles taken for a RAM access can vary ±1 clock cycle depending on the RAM speed relative to the PRAMC controller clock frequency. If system RAM is running at the same frequency as the PRAMC controller, a random initial access takes two clock cycles. If system RAM is running at a slower frequency, a random initial access may take 3 clock cycles. Subsequent burst beats take either one or two cycles depending on RAM speed relative to the PRAMC controller clock frequency. 

### 22.3.2 Writes 

This section discusses various write operations of the RAM controller. 

#### 22.3.2.1 64-bit writes 

Aligned 64-bit writes execute in a single AHB data phase cycle, resulting in zero wait states on back-to-back writes of these sizes. If, during the data phase of a write, a read is requested on the AHB, the write is registered in the late-write buffer, enabling the read to take place without a wait state. The valid buffered or late-write data is stored on the next available array address phase. 

Back-to-back 64-bit writes execute slightly differently. The first write bypasses the late-write buffer—the write data is stored directly to the array in the same cycle in which it is valid on the AHB. 

#### 22.3.2.2 Less than 64-bit writes 

Writes of size less than 64 bits incur a read-modify-write action as a consequence of the ECC coding scheme's 64-bit granularity. In the case of a read-modify-write action, the RAM controller performs SEC/DED on the read data. The write data is merged into the appropriate byte lanes along with the potentially corrected read data. A new codeword is generated based on the newly formed doubleword. This doubleword and its associated checkbits are subsequently written to RAM. Figure 49 provides details on the read-modify-write data path. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

736 / 4640 

NXP Semiconductors 

RAM Controller (PRAMC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Memories_and_Memory_Overview/022_RAM_Controller_-PRAMC-/S32K3XXRM_数据表.pdf-0737-02.png)


<!-- Start of picture text -->
Write data<br>Corrected read data<br>Single-bit error Sy ndrome<br>Multi-bit error D ecode<br>Checkbit<br>Encode<br>Read data ECC bits ECC bits Data<br>from array<br><!-- End of picture text -->

Figure 49. Read-modify-write data path 

On a read-modify-write operation, the array read data is registered after it is decoded and before it is merged with the AHB write data. Therefore, writes of size less than 64 bits require the insertion of one wait state before the data phase can be completed. 

#### 22.3.2.3 Unaligned writes 

The RAM controller is compliant with the AMBA-AHB2.v6 Extensions specification with regard to byte strobes. The size of the transfer is sufficient to cover all bytes being written, and covers more bytes in the case of an unaligned transfer. The address of the transfer is rounded down to the nearest boundary of the size of the transaction. 

~~<mark>NOTE</mark>~~ Unaligned writes always generate read-modify-write operations in the RAM controller in order to preserve the validity of the ECC codeword. 

## 22.4 Initialization/application information 

Each memory address must be written to a known value before it is read, to initialize the ECC. This includes reads generated from the read-modify-write operation that occurs when a write transfer of less than 64 bits or an unaligned write is requested. Without first writing an address to a known value, a read from the address will most likely generate an uncorrectable ECC event. 

## 22.5 PRAMC register descriptions 

The RAM controller module provides an IPS programming model mapped to a standard on-platform peripheral slot. 

~~<mark>NOTE</mark>~~ 

1. The programming model can only be referenced using a 32-bit (word) access. Attempted references using different access sizes or to undefined (reserved) addresses generate an IPS error termination. 

2. Attempted updates to the PRAMC programming model while a PRAMC operation is in progress will result in non-deterministic behavior. Software must be architected to avoid this scenario by ensuring that PRAMC configuration changes are made only during system boot or when only one master is enabled. In multi-core devices, update the PRAMC configuration only when one core is active and no other masters, for example, DMA or communications modules, are enabled. Move any instruction execution or memory references outside the system RAM while updating the PRAMC configuration, for example, to the core local memory space. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

737 / 4640 

NXP Semiconductors 

RAM Controller (PRAMC) 

### 22.5.1 PRAMC memory map 

PRAMC_0 base address: 4026_4000h 

PRAMC_1 base address: 4046_4000h 

PRAMC_2 base address: 4046_8000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|Platform RAM Configuration register 1 (PRCR1)|32|RW|0000_0100h|



### 22.5.2 Platform RAM Configuration register 1 (PRCR1) 

##### Offset 

|Register|Offset|
|---|---|
|PRCR1|0h|



##### Function 

The Platform RAM Configuration register 1 (PRCR1) is used to specify operation of the RAM controller. 

~~<mark>NOTE</mark>~~ This register is accessible only in supervisor mode. Accesses in user mode return a transfer error. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|||||||||0||||||||
|Reset<br>Bits|0<br>15|0<br>14|0<br>13|0<br>12|0<br>11|0<br>10|0<br>9|0<br>8|0<br>7|0<br>6|0<br>5|0<br>4|0<br>3|0<br>2|0<br>1|0<br>0|
|R|||0||||Rese|rved|Reserv|P0_BO|||0|||FT_|
|W|||||||||ed|_D...||||||DIS|
|Reset|0|0|0|0|0|0|0|1|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31-10<br>—|Reserved|
|9-8|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

738 / 4640 

NXP Semiconductors 

RAM Controller (PRAMC) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—<br>7|Reserved|
|—<br>6|Port p0 read burst optimization disable.|
|P0_BO_DIS|The number of cycles taken for a RAM access can vary ± 1 clock cycle depending on the<br>RAM speed relative to the PRAMC controller clock frequency. If system RAM is running at<br>the same frequency as the PRAMC controller, a random initial access takes 2 clock cycles.<br>If system RAM is running at a slower frequency, a random initial access may take 3 clock<br>cycles. Subsequent burst beats take either 1 or 2 cycles depending on RAM speed relative<br>to the PRAMC controller clock frequency.<br>~~NOTE~~<br>0b - 64-bit WRP4 read bursts are optimized such that the controller returns a 2-1-1-1 response<br>when PRCR1[FT_DIS ]=1<br>1b - 64-bit WRP4 read bursts are not optimized; the controller returns a 2-2-2-2 response when<br>PRCR1[FT_DIS ]=1|
|5-1<br>—<br>0<br>FT_DIS|Reserved<br>Flow-through disabled<br>This field defines the AHB response on reads. The state of this field has no impact on the response<br>latency on writes. This bit is cleared by hardware reset.<br>Do not change the FT_DIS bit value while accessing system RAM. Relocate code<br>programming the FT_DIS bit to another memory area, for example, local core memory.<br>~~NOTE~~<br>0b - RAM read data is passed directly to the system bus, incurring no additional latency<br>1b - RAM read data is registered prior to returning on the system bus, incurring one extra cycle of<br>latency|



## 22.6 Glossary 

|AHB|Arm advanced high-performance bus|
|---|---|
|DED|Double error detection|
|DMA|Direct memory access|
|MUX|Multiplexer|
|SEC|Single error correction|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

739 / 4640 

