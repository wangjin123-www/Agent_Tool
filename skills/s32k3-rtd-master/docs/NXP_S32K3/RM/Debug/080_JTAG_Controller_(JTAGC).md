NXP Semiconductors 

# Chapter 80 JTAG Controller (JTAGC) 

## 80.1 Chip-specific JTAGC information 

The following figure shows the detailed TAP connectivity. SWD/JTAG SELECT, SWDP and JTAG-DP are part of ARM DAP 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Debug/080_JTAG_Controller_-JTAGC-/S32K3XXRM_数据表.pdf-4593-04.png)


<!-- Start of picture text -->
JTAGC ARM JTAG-DP<br>instruction loaded<br>JTAG-mode TCK<br>SWD-JTAG<br>SWITCHER TMS TDO<br>TDI<br>0<br>JTAG-DP TDO<br>TCK<br>1<br>TCK<br>TMS<br>TMS TDO<br>TDI TDI<br>SWD-DP<br>DBGCLK<br>DBGDI<br>DBGDOEN<br>DBGDO<br><!-- End of picture text -->

Figure 513. Test and Debug Access Port (TAP) connectivity 

The debug port comes out of reset in a standard JTAG mode. It is switched to SWD mode by the change sequences described in JTAG to SWD change sequence . Once the mode has been changed, unused debug pins can be reassigned to any of their alternative muxed functions 

JTAG-to-SWD change sequence: 

1. Send more than 50 TCK cycles with TMS (SWDIO) =1 

2. Send the 16-bit sequence on TMS (SWDIO) = 0111_1001_1110_0111 (MSB transmitted first) 

3. Send more than 50 TCK cycles with TMS (SWDIO) =1 

   - ~~<mark>NOTE</mark>~~ 

In case of any reset event, JTAGC is moved to Test Logic Reset (TLR) state first and then JTAGC should be used. 

- ~~<mark>NOTE</mark>~~ 

If JTAG pins are used for alternative functionality and reset event arrives, then these pins need to be reconfigured to required functionality before using it, in order to avoid unintentional entry in JTAG mode. 

## 80.2 Overview 

The JTAGC block provides the means to test chip functionality and connectivity while remaining transparent to system logic when not in test mode. Testing is performed via a boundary scan technique, as defined in the IEEE 1149.1-2001 standard. All data input to and output from the JTAGC block is communicated in serial format. 

### 80.2.1 Block diagram 

The following is a simplified block diagram of the JTAG Controller (JTAGC) block. See the chip-specific configuration information within this chapter as well as Register description for more information about the JTAGC registers. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4593 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Debug/080_JTAG_Controller_-JTAGC-/S32K3XXRM_数据表.pdf-4594-01.png)


<!-- Start of picture text -->
JTAG Controller (JTAGC)<br>Power-on reset<br>Test Access Port (TAP)<br>TMS Controller<br>TCK<br>1-bit Bypass Register<br>32-bit Device Identification Register<br>TDO<br>TDI Boundary Scan Register<br>TAP Instruction Decoder<br>TAP Instruction Register<br>Figure 514. JTAG (IEEE 1149.1) block diagram<br><!-- End of picture text -->

### 80.2.2 Features 

The JTAGC block is compliant with the IEEE 1149.1-2001 standard, and supports the following features: 

- IEEE 1149.1-2001 TAP interface 

   - Four pins (TDI, TMS, TCK, and TDO) 

- Instruction register that supports several IEEE 1149.1–2001 defined instructions as well as several public and private device-specific instructions (see JTAGC block instructions for a list of supported instructions). 

- Sharing of the TAP with other TAP controllers via ACCESS_AUX_x instructions 

- Bypass register, boundary scan register, and device identification register 

- TAP controller state machine that controls the operation of the data registers, instruction register, and associated circuitry 

## 80.3 Functional description 

This section explains the JTAGC functional description. 

### 80.3.1 Modes of operation 

The JTAGC block uses a power-on reset indication as its primary reset signals. Several IEEE 1149.1–2001 defined test modes are supported, as well as a bypass mode. 

#### 80.3.1.1 Reset 

The JTAGC block is placed in reset when: 

- Power-on reset is asserted 

- TMS input is held high for enough consecutive rising edges of TCK to sequence the TAP controller state machine into the Test-Logic-Reset state 

Holding TMS high for five consecutive rising edges of TCK guarantees entry into the Test-Logic-Reset state regardless of the current TAP controller state. Asserting power-on reset results in asynchronous entry into the reset state. 

When in reset, the following actions occur: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4594 / 4640 

NXP Semiconductors 

JTAG Controller (JTAGC) 

- The TAP controller is forced into the Test-Logic-Reset state, thereby disabling the test logic and allowing normal operation of the on-chip system logic to continue unhindered. 

- The instruction register is loaded with the IDCODE instruction. 

#### 80.3.1.2 IEEE 1149.1–2001 defined test modes 

The JTAGC block supports several IEEE 1149.1–2001 defined test modes. A test mode is selected by loading the appropriate instruction into the instruction register when the JTAGC is enabled. Supported test instructions include EXTEST, HIGHZ, CLAMP, SAMPLE, and SAMPLE/PRELOAD. 

Each instruction defines the set of data register(s) that may operate and interact with the on-chip system logic when the instruction is current. Only one test data register path is enabled to shift data between TDI and TDO for each instruction. 

The boundary scan register is enabled for serial access between TDI and TDO when the EXTEST, SAMPLE, or SAMPLE/ PRELOAD instructions are active. The single-bit bypass register shift stage is enabled for serial access between TDI and TDO when the following instructions are active: 

- BYPASS 

- HIGHZ 

- CLAMP 

The functionality of each test mode is explained in more detail in JTAGC block instructions. 

#### 80.3.1.3 Bypass mode 

When no test operation is required, the BYPASS instruction can be loaded to place the JTAGC block into bypass mode. When in bypass mode, the single-bit bypass shift register is used to provide a minimum-length serial path to shift data between TDI and TDO. 

### 80.3.2 JTAGC reset configuration 

When in reset, the TAP controller is forced into the Test-Logic-Reset state, thus disabling the test logic and allowing normal operation of the on-chip system logic. In addition, the instruction register is loaded with the IDCODE instruction. 

### 80.3.3 IEEE 1149.1-2001 (JTAG) TAP 

The JTAGC block uses the IEEE 1149.1-2001 TAP for accessing registers. This port can be shared with other TAP controllers on the MCU. Ownership of the port is determined by the value of the currently loaded instruction. For more detail on TAP sharing via JTAGC instructions, see ACCESS_AUX_x instructions . 

Data is shifted between TDI and TDO through the selected register starting with the least significant bit, as illustrated in the following figure. This applies for the instruction register, test data registers, and the bypass register. 

|MSB||LSB||
|---|---|---|---|
|TDI||||
|TCK|Selected register||TDO|
|Figure 515. Shifting data through a register||||



### 80.3.4 TAP controller state machine 

The TAP controller is a synchronous state machine that interprets the sequence of logical values on the TMS pin. 

The following figure shows the machine's states. The value shown next to each state is the value of the TMS signal sampled on the rising edge of the TCK signal. As the figure shows, holding TMS at logic 1 when clocking TCK through a sufficient number of rising edges also causes the state machine to enter the Test-Logic-Reset state. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4595 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Debug/080_JTAG_Controller_-JTAGC-/S32K3XXRM_数据表.pdf-4596-01.png)


<!-- Start of picture text -->
JTAG Controller (JTAGC)<br>TEST LOGIC<br>RESET<br>1<br>0<br>1 1 1<br>RUN-TEST/IDLE SELECT-DR-SCAN SELECT-IR-SCAN<br>0<br>0 0<br>1 1<br>CAPTURE-DR CAPTURE-IR<br>0 0<br>SHIFT-DR SHIFT-IR<br>0 0<br>1 1<br>1 1<br>EXIT1-DR EXIT1-IR<br>0 0<br>PAUSE-DR PAUSE-IR<br>0 0<br>1 1<br>0 0<br>EXIT2-DR EXIT2-IR<br>1<br>1<br>UPDATE-DR UPDATE-IR<br>1 1<br>0 0<br>The value shown adjacent to each state transition in this figure represents the value of TMS at the time<br>of a rising edge of TCK.<br>Figure 516. IEEE 1149.1-2001 TAP controller finite state machine<br><!-- End of picture text -->

#### 80.3.4.1 Enabling the TAP controller 

The JTAGC TAP controller is enabled by setting the JTAGC enable to a logic 1 value. 

#### 80.3.4.2 Selecting an IEEE 1149.1-2001 register 

Access to the JTAGC data registers is achieved by loading the instruction register with any of the JTAGC block instructions when the JTAGC is enabled. Instructions are shifted in via the Select-IR-Scan path and loaded in the Update-IR state. At this point, all data register access is performed via the Select-DR-Scan path. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4596 / 4640 

NXP Semiconductors 

JTAG Controller (JTAGC) 

The Select-DR-Scan path is used to read or write the register data by shifting in the data (LSB first) during the Shift-DR state. When reading a register, the register value is loaded into the IEEE 1149.1-2001 shifter during the Capture-DR state. When writing a register, the value is loaded from the IEEE 1149.1-2001 shifter to the register during the Update-DR state. When reading a register, there is no requirement to shift out the entire register contents. Shifting may be terminated after the required number of bits have been acquired. 

### 80.3.5 JTAGC block instructions 

The JTAGC implements instructions defined in IEEE 1149.1-2001. See the chip-specific JTAGC information for the JTAGC instructions implemented on this chip. See the IEEE 1149.1-2001 standard for additional information. All undefined opcodes are reserved. 

#### 80.3.5.1 IDCODE instruction 

IDCODE selects the 32-bit device identification register as the shift path between TDI and TDO. This instruction allows interrogation of the MCU to determine its version number and other part identification data. IDCODE is the instruction placed into the instruction register when the JTAGC block is reset. 

#### 80.3.5.2 SAMPLE/PRELOAD instruction 

The SAMPLE/PRELOAD instruction has two functions: 

- The SAMPLE portion of the instruction obtains a sample of the system data and control signals present at the MCU input pins, and just before the boundary scan register cells at the output pins. This sampling occurs on the rising edge of TCK in the Capture-DR state when the SAMPLE/PRELOAD instruction is active. The sampled data is viewed by shifting it through the boundary scan register to the TDO output during the Shift-DR state. Both the data capture and the shift operation are transparent to system operation. 

- The PRELOAD portion of the instruction initializes the boundary scan register cells before selecting the EXTEST or CLAMP instructions to perform boundary scan tests. This is achieved by shifting in initialization data to the boundary scan register during the Shift-DR state. The initialization data is transferred to the parallel outputs of the boundary scan register cells on the falling edge of TCK in the Update-DR state. The data is applied to the external output pins by the EXTEST or CLAMP instruction. System operation is not affected. 

#### 80.3.5.3 SAMPLE instruction 

The SAMPLE instruction obtains a sample of the system data and control signals present at the MCU input pins, and just before the boundary scan register cells at the output pins. This sampling occurs on the rising edge of TCK in the Capture-DR state when the SAMPLE instruction is active. The sampled data is viewed by shifting it through the boundary scan register to the TDO output during the Shift-DR state. There is no defined action in the Update-DR state. Both the data capture and the shift operation are transparent to system operation. 

#### 80.3.5.4 EXTEST external test instruction 

EXTEST selects the boundary scan register as the shift path between TDI and TDO. It allows testing of off-chip circuitry and board-level interconnections by driving preloaded data contained in the boundary scan register onto the system output pins. Typically, the preloaded data is loaded into the boundary scan register using the SAMPLE/PRELOAD instruction before the selection of EXTEST. EXTEST asserts the internal system reset for the MCU to force a predictable internal state when performing external boundary scan operations. 

#### 80.3.5.5 TEST_LEAKAGE instruction 

The TEST_LEAKAGE instruction forces the jtag_leakage output signal to high. It is intended to tristate all output pad buffers and disable all of the part's pad input buffers except JCOMP and TEST. The jtag_leakage signal is asserted at the falling edge of TCK following the TAP controller state machine transition from the Update-IR state to the Run-Test-Idle state. When asserted, the part disables TCK, TMS, and TDI inputs and forces them to a logic 1. The TAP controller state machine remains in the Run-Test-Idle state until the JCOMP input is set to a value other than the JTAGC enable encoding. TEST_LEAKAGE also asserts the internal system reset for the MCU to force a predictable internal state. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

4597 / 4640 

NXP Semiconductors 

JTAG Controller (JTAGC) 

#### 80.3.5.6 HIGHZ instruction 

HIGHZ selects the bypass register as the shift path between TDI and TDO. When HIGHZ is active all output drivers are placed in an inactive drive state (for example, high impedance). HIGHZ also asserts the internal system reset for the MCU to force a predictable internal state. 

#### 80.3.5.7 CLAMP instruction 

CLAMP allows the state of signals driven from MCU pins to be determined from the boundary scan register when the bypass register is selected as the serial path between TDI and TDO. CLAMP enhances test efficiency by reducing the overall shift path to a single bit (the bypass register) when conducting an EXTEST type of instruction through the boundary scan register. CLAMP also asserts the internal system reset for the MCU to force a predictable internal state. 

#### 80.3.5.8 ACCESS_AUX_x instructions 

The JTAGC is configurable to allow other TAP controllers on the device to share the port with it. This is done by providing ACCESS_AUX_x instructions for each of these TAP controllers. 

When this instruction is loaded, control of the JTAG pins is transferred to the selected TAP controller. Any data input via TDI and TMS is passed to the selected TAP controller, and any TDO output from the selected TAP controller is sent back to the JTAGC to be output on the pins. 

The JTAGC regains control of the JTAG port during the UPDATE-DR state if the PAUSE-DR state was entered. Auxiliary TAP controllers are held in RUN-TEST/IDLE when they are inactive. Instructions not used to access an auxiliary TAP controller on a device are treated like the BYPASS instruction. 

#### 80.3.5.9 BYPASS instruction 

BYPASS selects the bypass register, creating a single-bit shift register path between TDI and TDO. BYPASS enhances test efficiency by reducing the overall shift path when no test operation of the MCU is required. This allows more rapid movement of test data to and from other components on a board that are required to perform test functions. When the BYPASS instruction is active the system logic operates normally. 

### 80.3.6 Boundary scan 

The boundary scan technique allows signals at component boundaries to be controlled and observed through the shift-register stage associated with each pad. Each stage is part of a larger boundary scan register cell, and cells for each pad are interconnected serially to form a shift-register chain around the border of the design. The boundary scan register consists of this shift-register chain, and is connected between TDI and TDO when the EXTEST, SAMPLE, or SAMPLE/PRELOAD instructions are loaded. The shift-register chain contains a serial input and serial output, as well as clock and control signals. 

## 80.4 External signal description 

The JTAGC consists of a set of signals that connect to off-chip development tools and allow access to test support functions. The JTAGC signals are outlined in the following table and described in the following sections. 

Table 708. JTAG signal properties 

|Name|I/O|Function|Reset state|
|---|---|---|---|
|TCK|Input|Test clock|Weak pulldown|
|TDI|Input|Test data in|Weak pullup|
|TDO|Output|Test data out|High Z<sup>1</sup>|
|TMS|Input|Test mode select|Weak pullup|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4598 / 4640 

NXP Semiconductors 

JTAG Controller (JTAGC) 

1. TDO output buffer enable is negated when the JTAGC is not in the Shift-IR or Shift-DR states. A weak pull may be implemented at the TDO pad for use when JTAGC is inactive. 

### 80.4.1 Test clock input (TCK) 

Test Clock Input (TCK) is an input pin used to synchronize the test logic and control register access through the TAP. 

### 80.4.2 Test data input (TDI) 

Test Data Input (TDI) is an input pin that receives serial test instructions and data. TDI is sampled on the rising edge of TCK. 

### 80.4.3 Test data output (TDO) 

Test Data Output (TDO) is an output pin that transmits serial output for test instructions and data. TDO is tristateable and is actively driven only in the Shift-IR and Shift-DR states of the TAP controller state machine, which is described in TAP controller state machine. 

### 80.4.4 Test mode select (TMS) 

Test Mode Select (TMS) is an input pin used to sequence the IEEE 1149.1-2001 test control state machine. TMS is sampled on the rising edge of TCK. 

## 80.5 Initialization/application information 

The test logic is a static logic design, and TCK can be stopped in either a high or low state without loss of data. However, the system clock is not synchronized to TCK internally. Any mixed operation using both the test logic and the system functional logic requires external synchronization. 

To initialize the JTAGC block and enable access to registers, the following sequence is required: 

1. Place the JTAGC in reset through TAP controller state machine transitions controlled by TMS. 

2. Load the appropriate instruction for the test or action to be performed. 

## 80.6 Register description 

This section provides a detailed description of the JTAGC block registers accessible through the TAP interface, including data registers and the instruction register. Individual bit-level descriptions and reset states of each register are included. These registers are not memory-mapped and can only be accessed through the TAP. 

### 80.6.1 Instruction register 

The JTAGC block uses a 8-bit instruction register as shown in the following figure. 

The instruction register allows instructions to be loaded into the block to select the test to be performed, or the test data register to be accessed, or both. Instructions are shifted in through TDI when the TAP controller is in the Shift-IR state, and latched on the falling edge of TCK in the Update-IR state. The latched instruction value can only be changed in the Update-IR and Test-Logic-Reset TAP controller states. 

Synchronous entry into the Test-Logic-Reset state results in the IDCODE instruction being loaded on the falling edge of TCK. Asynchronous entry into the Test-Logic-Reset state results in asynchronous loading of the IDCODE instruction. During the Capture-IR TAP controller state, the instruction shift register is loaded with the value 0b1, making this value the register's read value when the TAP controller is sequenced into the Shift-IR state. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4599 / 4640 

NXP Semiconductors 

JTAG Controller (JTAGC) 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Debug/080_JTAG_Controller_-JTAGC-/S32K3XXRM_数据表.pdf-4600-02.png)


Figure 517. Instruction register 

### 80.6.2 Bypass register 

The bypass register is a single-bit shift register path selected for serial data transfer between TDI and TDO when the following instructions are active: 

- BYPASS 

- HIGHZ 

- CLAMP 

After entry into the Capture-DR state, the single-bit shift register is set to a logic 0. Therefore, the first bit shifted out after selecting the bypass register is always a logic 0. 

### 80.6.3 Device identification register 

The device identification (JTAG ID) register, shown in the following figure, allows the revision number, part number, manufacturer, and design center responsible for the design of the part to be determined through the TAP. 

The device identification register is selected for serial data transfer between TDI and TDO when the IDCODE instruction is active. Entry into the Capture-DR state when the device identification register is selected loads the IDCODE into the shift register to be shifted out on TDO in the Shift-DR state. No action occurs in the Update-DR state. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Debug/080_JTAG_Controller_-JTAGC-/S32K3XXRM_数据表.pdf-4600-13.png)


Figure 518. Device identification register 

The following table describes the device identification register functions. The device identification register values are described in the chip-specific JTAGC information. 

Table 709. Device identification register field descriptions 

|Field|Function|
|---|---|
|PRN|Part revision number|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4600 / 4640 

NXP Semiconductors 

JTAG Controller (JTAGC) 

Table 709. Device identification register field descriptions (continued) 

|Field|Function|
|---|---|
||Contains the revision number of the part.|
|DC|Design center|
||Indicates the design center.|
|PIN|Part identification number<br>Contains the part number of the device.|
|MIC|Manufacturer identity code|
||Contains the reduced Joint Electron Device Engineering Council (JEDEC) ID .|
|IDCODE ID|IDCODE register ID<br>Identifies this register as the device identification register and not the bypass register. Always set to 1.|



### 80.6.4 Boundary scan register 

The boundary scan register is connected between TDI and TDO when the EXTEST, SAMPLE, or SAMPLE/PRELOAD instructions are active. It is used to: 

- Capture input pin data 

- Force fixed values on output pins 

- Select a logic value and direction for bidirectional pins 

Each bit of the boundary scan register represents a separate boundary scan register cell, as described in the IEEE 1149.1-2001 standard and discussed in Boundary scan. The size of the boundary scan register and bit ordering is device-dependent and can be found in the device BSDL file. 

## 80.7 Glossary 

|TAP|Test access port|
|---|---|
|TCK|Test clock|
|TDI|Test data in|
|TDO|Test data out|
|TMS|Test mode select|
|JCOMP|JTAG compliancy|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

4601 / 4640 

