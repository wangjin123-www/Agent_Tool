NXP Semiconductors 

# Chapter 63 Trigger MUX (TRGMUX) 

## 63.1 Chip-specific TRGMUX information 

### 63.1.1 TRGMUX input output configuration and instances 

This chip has 1 instance of TRGMUX module. 

Table 367. TRGMUX instance 

|Instance|S32K311/S32K312/S32K322/S32K342/S32K314/S32K324/S32K344/S32K358|
|---|---|
|TRGMUX|Yes|



The device supports the triggering scheme between peripherals. For the supported trigger sources and destination, see the TRGMUX connectivity file attached to this document. 

This device has 16 pads (SIUL2) mapped from TRGMUX inputs and TRGMUX outputs are mapped to the eMIOS channels, hence two timers channels can use a single pin of the device to do input capture. 

While using TRGMUX, below points need to be taken care: 

- User must ensure the minimum pulse of 100 ns on SIUL2 pads when using them as trigger source on TRGMUX. 

- Pulses which are visible on pads depends on the pad type. Different pad supports different frequencies. For more details on pad types and their respective bandwidth, see section "IO signal table" in "Signal Multiplexing" chapter. 

- End of conversion (EOC) signals of ADC modules are mapped on TRGMUX inputs as trigger sources. The EOC signal is asserted after ADC conversion regardless whether conversion is signaled by polling flags, interrupt or DMA transfer. The signal shall not be used to start injected conversion on same ADC channel as it will overwrite current result register. 

- The minimum pulse length requirement is 1.5X of destination clock, so that it gets properly sampled at the destination IP connected to TRGMUX outputs, otherwise there are chances of missing the triggers generated from source. For example, the trigger generated from PAD for ADC conversion should be kept high/low for at least 1.5X of ADC clock so that it gets sampled in ADC clock domain. To ensure this, pulse strechers have been placed before some of the hardware modules mapped on TRGMUX outputs. 

- Some PADS are being shared by both ADC and TRGMUX. It is recommended that trigger initiated from such PADS should not be used to trigger a conversion on the ADC channel mapped on same PAD. Failing to do this will cause congestion on same PAD. 

- Out of all the pads mapped on TRGMUX, first four pads have glitch filters. For details, see the TRGMUX connectivity file attached to this document. The trigger pulse width should honour the pulse width requirement as per Glitch Filter specifications. The same signal can be observed at output pin if the pulse width of the input data signal is more than 400ns and no output signal should be observed if the pulse width of the input data signal is less than 20ns. A signal with a pulse width that is between 20ns and 400 ns should not be applied as the behavior is not guaranteed. 

- Trigger outputs are grouped peripheral-wise and have a common lock bit based on TRGMUX REGx. For instance, normal_trigger, injected_trigger and external_sync of ADC_0 are grouped onto TRGMUX_REG0 and have a common lock bit. 

### 63.1.2 Pulse strechers in TRGMUX 

TRGMUX has some hardware modules on its input side running at faster clock than some of the IPs present on output side. For instance, eMIOS reload outputs running at 160 MHz can trigger LPI2C trigger input clocked at 40 MHz, in that case there is a high chance that trigger from eMIOS will be missed. Following Pulse strechers are added for the IPs on output side of TRGMUX. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2300 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

Table 368. Pulse strechers in TRGMUX 

|Evaluation<br>Parameter|ADC_0/1/2<br>external trigger<br>to sync the start<br>pulse|BCTU trigger<br>23/47/71|FlexIO trigger<br>input_0/1/2/3<sup>1</sup>|LPI2C_0<br>Trigger input|LPSPI_0/1/2<br>Trigger input|CM7_0/1/2<br>RXEV|
|---|---|---|---|---|---|---|
|IP expects|Synchronized<br>single cycle<br>pulse|Synchronized<br>pulse|IP requirement<br>is to have 2<br>cycle pulse of<br>flexio_clk|IP requirement<br>is to have 2<br>cycle pulse of<br>lpi2c_clk|IP requirement<br>is to have 2<br>cycle pulse of<br>lpspi_clk|Single cycle<br>pulse|
|Frequency|CORE_CLK|CORE_CLK|CORE_CLK|AIPS_SLOW_C<br>LK|LPSPI_0 -<br>PLAT_AIPS_CL<br>K<br>LPSPI_1/2/3 -<br>AIPS_SLOW_C<br>LK|CORE_CLK|
|Inside IP|Used as combo<br>signal|Flopped inside<br>IP and clear<br>after ADC<br>conversion<br>completed|Synchronized<br>inside IP|Synchronized<br>inside IP|Synchronized<br>inside IP|-|
|At SoC|Since it an<br>ASYNC signal<br>and IP required<br>synchronized<br>single cycle<br>pulse, so a pulse<br>stretcher is<br>added to convert<br>pulse from any<br>frequency<br>domain into a<br>signle cycle<br>pulse of<br>CORE_CLK|Since slow IP<br>such as LPCMP<br>or from PAD can<br>also trigger<br>BCTU and<br>BCTU wants<br>that trigger<br>should clear<br>after the ADC<br>conversion. So a<br>pulse stretcher<br>is added which<br>convert any size<br>of pulse to a<br>single cycle<br>pulse of BCTU<br>clock<br>(CORE_CLK)|Pulse stretcher<br>is added to<br>convert any<br>pulse into a two<br>cyle pulse of<br>FLEXIO_CLK|Pulse stretcher<br>is added to<br>convert any<br>pulse into a two<br>cyle pulse of<br>LPI2C_CLK|Pulse stretcher<br>is added to<br>convert any<br>pulse into a two<br>cyle pulse of<br>LPSPI_CLK|Pulse stretcher<br>is added to<br>convert any<br>pulse into a<br>single cyle pulse<br>of CORE_CLK|
|Output slot at<br>which pulse<br>stretcher is<br>added|2, 6, 10|24, 25, 26|64, 65, 66, 67|84|88, 92, 96|156, 157, 158<sup>2</sup>|



1. These pulse stretchers are available in S32K314, S32K324 and S32K344 variants only. 

2. CM7_2 is applicable for S32K358 only. 

~~<mark>NOTE</mark>~~ 

The trigger outputs which have pulse stretcher before them, there should be atleast a gap of 5 cycle of destination clock for back to back trigger. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2301 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

### 63.1.3 Trigger monitor 

A trigger monitor is added before the TRGMUX inputs ADC12_0_EOC, ADC12_1_EOC and ADC12_2_EOC. You can configure the UDR registers in SIUL2 to select which trigger needs to propagate to the above TRGMUX inputs. By default after coming out of reset, all the enables are 0. Hence no trigger will be coming to these 3 TRGMUX inputs. 

~~<mark>NOTE</mark>~~ Trigger monitor is not present in S32K314, S32K324 and S32K344. 

## 63.2 Introduction 

The trigger multiplexer (TRGMUX) module allows software to configure the trigger inputs for various peripherals. 

## 63.3 Features 

The TRGMUX module allows software to select the trigger source for peripherals. The block diagram below shows the trigger selection logic of the TRGMUX module. 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2302-09.png)


<!-- Start of picture text -->
TRGMUX<br>Trigger disabled<br>...000<br>Trigger input 1 ...001<br>Trigger input 2 ...010<br>Trigger input 3 ...011 output x To peripheral<br>Trigger input 4 ...100 trigger inputs<br>Trigger input 5 ...101<br>Trigger input 6 ...110 Up to four outputs per peripheral<br>Trigger input 7 ...111<br>[SEL0] selects the trigger for output 0<br>Trigger input N* [SEL1] selects the trigger for output 1<br>[SEL2] selects the trigger for output 2<br>[SEL3] selects the trigger for output 3<br>[SELx]<br>* Up to 255 trigger inputs may be available for SEL0, SEL1, and SEL2. For SEL3, up to 127<br>   trigger inputs may be available. When the number of trigger inputs is 255, SEL3 is not<br>   available and becomes reserved. See the chip-specific TRGMUX information for the<br>   maximum number of trigger inputs supported on this device.<br><!-- End of picture text -->

Figure 352. TRGMUX block diagram 

Each peripheral has its own dedicated TRGMUX register. See each peripheral's TRGMUX register for details. 

## 63.4 Memory map and register definition 

The TRGMUX registers contain fields for selecting trigger sources for peripheral modules. 

TRGMUX registers can be written only in supervisor mode. 

### 63.4.1 TRGMUX register descriptions 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2302 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

#### 63.4.1.1 TRGMUX memory map 

Table 369. Select Bit Fields 

|Field|Description|
|---|---|
|SELx|This read/write field is used to configure the MUX select for the peripheral trigger inputs.<br>0000_0000 - (0x00) LOGIC 0 (VSS)<br>0000_0001 - (0x01) LOGIC 1 (VDD)<br>0000_0010 - (0x02) ADC12_0_EOC<br>0000_0011 - (0x03) ADC12_1_EOC<br>0000_0100 - (0x04) ADC12_2_EOC<br>0000_0101 - (0x05) LPCMP_0_COUT output<br>0000_0110 - (0x06) LPCMP_1_COUT output<br>0000_0111 - (0x07) LPCMP_2_COUT output<br>0000_1000 - (0x08) eDMA_eDMA_0 DONE<br>0000_1001 - (0x09) eDMA_eDMA_1 DONE<br>0000_1010 - (0x0A) eDMA_eDMA_16 DONE|
||0000_1011 - (0x0B) eDMA_eDMA_17 DONE<br>0000_1100 - (0x0C) eMIOS_0_RELOAD_OUT_CH[23]<br>0000_1101 - (0x0D) eMIOS_0_RELOAD_OUT_CH[22]<br>0000_1110 - (0x0E) eMIOS_0_RELOAD_OUT_CH[8]<br>0000_1111 - (0x0F) eMIOS_0_RELOAD_OUT_CH[0]<br>0001_0000 - (0x10) eMIOS_0_IPP_DO_eMIOS_CH[0]|
||0001_0001 - (0x11) eMIOS_0_IPP_DO_eMIOS_CH[1]<br>0001_0010 - (0x12) eMIOS_0_IPP_DO_eMIOS_CH[2]<br>0001_0011 - (0x13) eMIOS_0_IPP_DO_eMIOS_CH[3]<br>0001_0100 - (0x14) eMIOS_0_IPP_DO_eMIOS_CH[4]<br>0001_0101 - (0x15) eMIOS_0_IPP_DO_eMIOS_CH[5]<br>0001_0110 - (0x16) eMIOS_0_IPP_DO_eMIOS_CH[6]|
||0001_0111 - (0x17) eMIOS_0_IPP_DO_eMIOS_CH[7]|
||0001_1000 - (0x18) eMIOS_0_IPP_DO_eMIOS_CH[8]|
||0001_1001 - (0x19) eMIOS_0_IPP_DO_eMIOS_CH[9]|
||0001_1010 - (0x1A) eMIOS_0_IPP_DO_eMIOS_CH[10]|
||0001_1011 - (0x1B) eMIOS_0_IPP_DO_eMIOS_CH[11]|
||0001_1100 - (0x1C) eMIOS_0_IPP_DO_eMIOS_CH[12]|
||0001_1101 - (0x1D) eMIOS_0_IPP_DO_eMIOS_CH[13]|
||0001_1110 - (0x1E) eMIOS_0_IPP_DO_eMIOS_CH[14]|
||0001_1111 - (0x1F) eMIOS_0_IPP_DO_eMIOS_CH[15]|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2303 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

Table 369. Select Bit Fields 

|Field|Description||
|---|---|---|
||0010_0000 -|(0x20) eMIOS_0_IPP_DO_eMIOS_CH[22]|
||0010_0001 -|(0x21) eMIOS_0_IPP_DO_eMIOS_CH[23]|
||0010_0010 -|(0x22) eMIOS_1_RELOAD_OUT_CH[23]|
||0010_0011 -|(0x23) eMIOS_1_RELOAD_OUT_CH[22]|
||0010_0100 -|(0x24) eMIOS_1_RELOAD_OUT_CH[8]|
||0010_0101 -|(0x25) eMIOS_1_RELOAD_OUT_CH[0]|
||0010_0110 -|(0x26) eMIOS_1_IPP_DO_eMIOS_CH[0]|
||0010_0111 -|(0x27) eMIOS_1_IPP_DO_eMIOS_CH[1]|
||0010_1000 -|(0x28) eMIOS_1_IPP_DO_eMIOS_CH[2]|
||0010_1001 -|(0x29) eMIOS_1_IPP_DO_eMIOS_CH[3]|
||0010_1010 -|(0x2A) eMIOS_1_IPP_DO_eMIOS_CH[4]|
||0010_1011 -|(0x2B) eMIOS_1_IPP_DO_eMIOS_CH[5]|
||0010_1100 -|(0x2C) eMIOS_1_IPP_DO_eMIOS_CH[6]|
||0010_1101 -|(0x2D) eMIOS_1_IPP_DO_eMIOS_CH[7]|
||0010_1110 -|(0x2E) eMIOS_1_IPP_DO_eMIOS_CH[8]|
||0010_1111 -|(0x2F) eMIOS_1_IPP_DO_eMIOS_CH[9]|
||0011_0000 -|(0x30) eMIOS_1_IPP_DO_eMIOS_CH[10]|
||0011_0001 -|(0x31) eMIOS_1_IPP_DO_eMIOS_CH[11]|
||0011_0010 -|(0x32) eMIOS_1_IPP_DO_eMIOS_CH[12]|
||0011_0011 -|(0x33) eMIOS_1_IPP_DO_eMIOS_CH[13]|
||0011_0100 -|(0x34) eMIOS_1_IPP_DO_eMIOS_CH[14]|
||0011_0101 -|(0x35) eMIOS_1_IPP_DO_eMIOS_CH[15]|
||0011_0110 -|(0x36) eMIOS_1_IPP_DO_eMIOS_CH[22]|
||0011_0111 -|(0x37) eMIOS_1_IPP_DO_eMIOS_CH[23]|
||0011_1000 -|(0x38) FlexIO_External Output Trigger 0|
||0011_1001 -|(0x39) FlexIO_External Output Trigger 1|
||0011_1010 -|(0x3A) FlexIO_External Output Trigger 2|
||0011_1011 -|(0x3B) FlexIO_External Output Trigger 3|
||0011_1100 -|(0x3C) SIUL_TRGMUX_IN0|
||0011_1101 -|(0x3D) SIUL_TRGMUX_IN1|
||0011_1110 -|(0x3E) SIUL_TRGMUX_IN2|
||0011_1111 -|(0x3F) SIUL_TRGMUX_IN3|
||0100_0000 -|(0x40) SIUL_TRGMUX_IN4|
||0100_0001 -|(0x41) SIUL_TRGMUX_IN5|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2304 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table 369. Select Bit Fields 

|Field|Description||
|---|---|---|
||0100_0010 -|(0x42) SIUL_TRGMUX_IN6|
||0100_0011 -|(0x43) SIUL_TRGMUX_IN7|
||0100_0100 -|(0x44) SIUL_TRGMUX_IN8|
||0100_0101 -|(0x45) SIUL_TRGMUX_IN9|
||0100_0110 -|(0x46) SIUL_TRGMUX_IN10|
||0100_0111 -|(0x47) SIUL_TRGMUX_IN11|
||0100_1000 -|(0x48) SIUL_TRGMUX_IN12|
||0100_1001 -|(0x49) SIUL_TRGMUX_IN13|
||0100_1010 -|(0x4A) SIUL_TRGMUX_IN14|
||0100_1011 -|(0x4B) SIUL_TRGMUX_IN15|
||0100_1100 -|(0x4C) LPI2C_0_Master trigger output|
||0100_1101 -|(0x4D) LPI2C_0_Slave trigger output|
||0100_1110 -|(0x4E) LPSPI_0_End of frame trigger|
||0100_1111 -|(0x4F) LPSPI_0_Receive data trigger|
||0101_0000 -|(0x50) LPSPI_1_End of frame trigger|
||0101_0001 -|(0x51) LPSPI_1_Receive data trigger|
||0101_0010 -|(0x52) LPSPI_2_End of frame trigger|
||0101_0011 -|(0x53) LPSPI_2_Receive data trigger|
||0101_0100 -|(0x54) LPUART_0_trg_txword|
||0101_0101 -|(0x55) LPUART_0_trg_rxword|
||0101_0110 -|(0x56) LPUART_0_trg_rxidle|
||0101_0111 -|(0x57) LPUART_1_trg_txword|
||0101_1000 -|(0x58) LPUART_1_trg_rxword|
||0101_1001 -|(0x59) LPUART_1_trg_rxidle|
||0101_1010 -|(0x5A) LPUART_2_trg_txword|
||0101_1011 -|(0x5B) LPUART_2_trg_rxword|
||0101_1100 -|(0x5C) LPUART_2_trg_rxidle|
||0101_1101 -|(0x5D) LCU_0_LC1_out_i1|
||0101_1110 -|(0x5E) LCU_0_LC1_out_i2|
||0101_1111 -|(0x5F) LCU_0_LC1_out_i3|
||0110_0000 -|(0x60) LCU_0_LC1_out_i4|
||0110_0001 -|(0x61) LCU_0_LC2_out_i1|
||0110_0010 -|(0x62) LCU_0_LC2_out_i2|
||0110_0011 -|(0x63) LCU_0_LC2_out_i3|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2305 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table 369. Select Bit Fields 

|Field|Description||
|---|---|---|
||0110_0100 -|(0x64) LCU_0_LC2_out_i4|
||0110_0101 -|(0x65) LCU_0_LC3_out_i1|
||0110_0110 -|(0x66) LCU_0_LC3_out_i2|
||0110_0111 -|(0x67) LCU_0_LC3_out_i3|
||0110_1000 -|(0x68) LCU_0_LC3_out_i4|
||0110_1001 -|(0x69) LCU_1_LC1_out_i1|
||0110_1010 -|(0x6A) LCU_1_LC1_out_i2|
||0110_1011 -|(0x6B) LCU_1_LC1_out_i3|
||0110_1100 -|(0x6C) LCU_1_LC1_out_i4|
||0110_1101 -|(0x6D) LCU_1_LC2_out_i1|
||0110_1110 -|(0x6E) LCU_1_LC2_out_i2|
||0110_1111 -|(0x6F) LCU_1_LC2_out_i3|
||0111_0000 -|(0x70) LCU_1_LC2_out_i4|
||0111_0001 -|(0x71) LCU_1_LC3_out_i1|
||0111_0010 -|(0x72) LCU_1_LC3_out_i2|
||0111_0011 -|(0x73) LCU_1_LC3_out_i3|
||0111_0100 -|(0x74) LCU_1_LC3_out_i4|
||0111_0101 -|(0x75) PIT0_PIT0 CH0|
||0111_0110 -|(0x76) PIT0_PIT0 CH1|
||0111_0111 -|(0x77) PIT0_PIT0 CH2|
||0111_1000 -|(0x78) PIT0_PIT0 CH3|
||0111_1001 -|(0x79) PIT0_PIT0 CH4 RTI|
||0111_1010 -|(0x7A) PIT1_PIT1 CH0|
||0111_1011 -|(0x7B) PIT1_PIT1 CH1|
||0111_1100 -|(0x7C) PIT1_PIT1 CH2|
||0111_1101 -|(0x7D) PIT1_PIT1 CH3|
||0111_1110 -|(0x7E) CM7_0_TXEV|
||0111_1111 -|(0x7F) CM7_2_TXEV|



##### TRGMUX base address: 4008_0000h 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|0h|TRGMUX ADC12_0 Register (ADC12_0)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2306 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|4h|TRGMUX ADC12_1 Register (ADC12_1)|32|RW|0000_0000h|
|8h|TRGMUX ADC12_2 Register (ADC12_2)|32|RW|0000_0000h|
|Ch|TRGMUX LPCMP_0 Register (LPCMP_0)|32|RW|0000_0000h|
|10h|TRGMUX LPCMP_1 Register (LPCMP_1)|32|RW|0000_0000h|
|14h|TRGMUX LPCMP_2 Register (LPCMP_2)|32|RW|0000_0000h|
|18h|TRGMUX BCTU Register (BCTU)|32|RW|0000_0000h|
|1Ch|TRGMUX eMIOS012_ODIS Register (eMIOS012_ODIS)|32|RW|0000_0000h|
|20h|TRGMUX eMIOS0_0 Register (eMIOS0_0)|32|RW|0000_0000h|
|24h|TRGMUX eMIOS0_1 Register (eMIOS0_1)|32|RW|0000_0000h|
|28h|TRGMUX eMIOS0_2 Register (eMIOS0_2)|32|RW|0000_0000h|
|2Ch|TRGMUX eMIOS0_3 Register (eMIOS0_3)|32|RW|0000_0000h|
|30h|TRGMUX eMIOS1_0 Register (eMIOS1_0)|32|RW|0000_0000h|
|34h|TRGMUX eMIOS1_1 Register (eMIOS1_1)|32|RW|0000_0000h|
|38h|TRGMUX eMIOS1_2 Register (eMIOS1_2)|32|RW|0000_0000h|
|3Ch|TRGMUX eMIOS1_3 Register (eMIOS1_3)|32|RW|0000_0000h|
|40h|TRGMUX FlexIO Register (FlexIO)|32|RW|0000_0000h|
|44h|TRGMUX SIUL_OUT0 Register (SIUL_OUT0)|32|RW|0000_0000h|
|48h|TRGMUX SIUL_OUT1 Register (SIUL_OUT1)|32|RW|0000_0000h|
|4Ch|TRGMUX SIUL_OUT2 Register (SIUL_OUT2)|32|RW|0000_0000h|
|50h|TRGMUX SIUL_OUT3 Register (SIUL_OUT3)|32|RW|0000_0000h|
|54h|TRGMUX LPI2C_0 Register (LPI2C_0)|32|RW|0000_0000h|
|58h|TRGMUX LPSPI_0 Register (LPSPI_0)|32|RW|0000_0000h|
|5Ch|TRGMUX LPSPI_1 Register (LPSPI_1)|32|RW|0000_0000h|
|60h|TRGMUX LPSPI_2 Register (LPSPI_2)|32|RW|0000_0000h|
|64h|TRGMUX LPUART_0 Register (LPUART_0)|32|RW|0000_0000h|
|68h|TRGMUX LPUART_1 Register (LPUART_1)|32|RW|0000_0000h|
|6Ch|TRGMUX LPUART_2 Register (LPUART_2)|32|RW|0000_0000h|
|70h|TRGMUX LPUART_3 Register (LPUART_3)|32|RW|0000_0000h|
|74h|TRGMUX LCU0_SYNC Register (LCU0_SYNC)|32|RW|0000_0000h|
|78h|TRGMUX LCU0_FORCE Register (LCU0_FORCE)|32|RW|0000_0000h|
|7Ch|TRGMUX LCU0_0 Register (LCU0_0)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2307 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

Table continued from the previous page... 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|80h|TRGMUX LCU0_1 Register (LCU0_1)|32|RW|0000_0000h|
|84h|TRGMUX LCU0_2 Register (LCU0_2)|32|RW|0000_0000h|
|88h|TRGMUX LCU1_SYNC Register (LCU1_SYNC)|32|RW|0000_0000h|
|8Ch|TRGMUX LCU1_FORCE Register (LCU1_FORCE)|32|RW|0000_0000h|
|90h|TRGMUX LCU1_0 Register (LCU1_0)|32|RW|0000_0000h|
|94h|TRGMUX LCU1_1 Register (LCU1_1)|32|RW|0000_0000h|
|98h|TRGMUX LCU1_2 Register (LCU1_2)|32|RW|0000_0000h|
|9Ch|TRGMUX CM7_RXEV Register (CM7_RXEV)|32|RW|0000_0000h|



#### 63.4.1.2 TRGMUX ADC12_0 Register (ADC12_0) 

##### Offset 

|Register|Offset|
|---|---|
|ADC12_0|0h|



##### Function 

This register is for the ADC12_0 module. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2308-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0<br>LK  SEL2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>SEL1  SEL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2308 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>—|This read-only bit field is reserved and always has the value 0.|
|23<br>—<br>22-16<br>SEL2|This read-only bit field is reserved and always has the value 0.<br>Trigger MUX Input 2 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 2. For the field setting<br>definitions, seeMemory map and register definition.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|
|14-8<br>SEL1|Trigger MUX Input 1 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7<br>—|This read-only bit field is reserved and always has the value 0.|
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



#### 63.4.1.3 TRGMUX ADC12_1 Register (ADC12_1) 

##### Offset 

|Register|Offset|
|---|---|
|ADC12_1|4h|



##### Function 

This register is for the ADC12_1 module. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2309 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2310-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0<br>LK  SEL2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>SEL1  SEL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>—<br>23<br>—<br>22-16|This read-only bit field is reserved and always has the value 0.<br>This read-only bit field is reserved and always has the value 0.<br>Trigger MUX Input 2 Source Select|
|SEL2|This read/write bit field is used to configure the MUX select for peripheral trigger input 2. For the field setting<br>definitions, seeMemory map and register definition.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|
|14-8<br>SEL1|Trigger MUX Input 1 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7<br>—<br>6-0|This read-only bit field is reserved and always has the value 0.<br>Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2310 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

#### 63.4.1.4 TRGMUX ADC12_2 Register (ADC12_2) 

##### Offset 

|Register|Offset|
|---|---|
|ADC12_2|8h|



##### Function 

This register is for the ADC12_2 module. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|LK||||0||||0||||SEL2||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|0||||SEL1||||0||||SEL0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>—|This read-only bit field is reserved and always has the value 0.|
|23<br>—|This read-only bit field is reserved and always has the value 0.|
|22-16|Trigger MUX Input 2 Source Select|
|SEL2|This read/write bit field is used to configure the MUX select for peripheral trigger input 2. For the field setting<br>definitions, seeMemory map and register definition.|
|15|This read-only bit field is reserved and always has the value 0.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2311 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|14-8|Trigger MUX Input 1 Source Select|
|SEL1|This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7|This read-only bit field is reserved and always has the value 0.|
|—||
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



#### 63.4.1.5 TRGMUX LPCMP_0 Register (LPCMP_0) 

##### Offset 

|Register|Offset|
|---|---|
|LPCMP_0|Ch|



##### Function 

This register is for the LPCMP_0 module. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2312-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0 0<br>LK<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 0<br>SEL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function||
|---|---|---|
|31|TRGMUX register lock.||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2312 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>—|This read-only bit field is reserved and always has the value 0.|
|23<br>—|This read-only bit field is reserved and always has the value 0.|
|22-16<br>—|This read-only bit field is reserved and always has the value 0.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|
|14-8<br>—|This read-only bit field is reserved and always has the value 0.|
|7<br>—|This read-only bit field is reserved and always has the value 0.|
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



#### 63.4.1.6 TRGMUX LPCMP_1 Register (LPCMP_1) 

##### Offset 

|Register|Offset|
|---|---|
|LPCMP_1|10h|



##### Function 

This register is for the LPCMP_1 module. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2313 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|LK||||0||||0||||0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|0||||0||||0||||SEL0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>—|This read-only bit field is reserved and always has the value 0.|
|23<br>—|This read-only bit field is reserved and always has the value 0.|
|22-16<br>—|This read-only bit field is reserved and always has the value 0.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|
|14-8<br>—<br>7<br>—|This read-only bit field is reserved and always has the value 0.<br>This read-only bit field is reserved and always has the value 0.|
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2314 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

#### 63.4.1.7 TRGMUX LPCMP_2 Register (LPCMP_2) 

##### Offset 

|Register|Offset|
|---|---|
|LPCMP_2|14h|



##### Function 

This register is for the LPCMP_2 module. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|LK||||0||||0||||0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|0||||0||||0||||SEL0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>—|This read-only bit field is reserved and always has the value 0.|
|23<br>—|This read-only bit field is reserved and always has the value 0.|
|22-16<br>—|This read-only bit field is reserved and always has the value 0.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2315 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|14-8|This read-only bit field is reserved and always has the value 0.|
|—||
|7|This read-only bit field is reserved and always has the value 0.|
|—||
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



#### 63.4.1.8 TRGMUX BCTU Register (BCTU) 

##### Offset 

|Register|Offset|
|---|---|
|BCTU|18h|



##### Function 

This register is for the BCTU module. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2316-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0<br>LK  SEL2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>SEL1  SEL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2316 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>—|This read-only bit field is reserved and always has the value 0.|
|23<br>—|This read-only bit field is reserved and always has the value 0.|
|22-16|Trigger MUX Input 2 Source Select|
|SEL2|This read/write bit field is used to configure the MUX select for peripheral trigger input 2. For the field setting<br>definitions, seeMemory map and register definition.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|
|14-8|Trigger MUX Input 1 Source Select|
|SEL1|This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7<br>—|This read-only bit field is reserved and always has the value 0.|
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



#### 63.4.1.9 TRGMUX eMIOS012_ODIS Register (eMIOS012_ODIS) 

##### Offset 

|Register|Offset|
|---|---|
|eMIOS012_ODIS|1Ch|



Function 

This register is for the eMIOS012_ODIS module. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2317 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2318-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>LK  SEL3  SEL2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>SEL1  SEL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>SEL3|Trigger MUX Input 3 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 3. For the field setting<br>definitions, seeMemory map and register definition.|
|23<br>—<br>22-16<br>SEL2|This read-only bit field is reserved and always has the value 0.<br>Trigger MUX Input 2 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 2. For the field setting<br>definitions, seeMemory map and register definition.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|
|14-8<br>SEL1|Trigger MUX Input 1 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7<br>—|This read-only bit field is reserved and always has the value 0.|
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2318 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

#### 63.4.1.10 TRGMUX eMIOS0_0 Register (eMIOS0_0) 

##### Offset 

|Register|Offset|
|---|---|
|eMIOS0_0|20h|



##### Function 

This register is for the eMIOS0_0 module. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2319-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>LK  SEL3  SEL2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>SEL1  SEL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>SEL3|Trigger MUX Input 3 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 3. For the field setting<br>definitions, seeMemory map and register definition.|
|23<br>—|This read-only bit field is reserved and always has the value 0.|
|22-16|Trigger MUX Input 2 Source Select|
|SEL2|This read/write bit field is used to configure the MUX select for peripheral trigger input 2. For the field setting<br>definitions, seeMemory map and register definition.|
|15|This read-only bit field is reserved and always has the value 0.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2319 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|14-8|Trigger MUX Input 1 Source Select|
|SEL1|This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7|This read-only bit field is reserved and always has the value 0.|
|—||
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



#### 63.4.1.11 TRGMUX eMIOS0_1 Register (eMIOS0_1) 

##### Offset 

|Register|Offset|
|---|---|
|eMIOS0_1|24h|



##### Function 

This register is for the eMIOS0_1 module. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2320-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>LK  SEL3  SEL2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>SEL1  SEL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|



|Table continues on the next page...|
|---|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2320 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>SEL3|Trigger MUX Input 3 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 3. For the field setting<br>definitions, seeMemory map and register definition.|
|23<br>—|This read-only bit field is reserved and always has the value 0.|
|22-16<br>SEL2|Trigger MUX Input 2 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 2. For the field setting<br>definitions, seeMemory map and register definition.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|
|14-8<br>SEL1|Trigger MUX Input 1 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7<br>—|This read-only bit field is reserved and always has the value 0.|
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



#### 63.4.1.12 TRGMUX eMIOS0_2 Register (eMIOS0_2) 

##### Offset 

|Register|Offset|
|---|---|
|eMIOS0_2|28h|



Function 

This register is for the eMIOS0_2 module. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2321 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2322-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>LK  SEL3  SEL2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>SEL1  SEL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>SEL3|Trigger MUX Input 3 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 3. For the field setting<br>definitions, seeMemory map and register definition.|
|23<br>—<br>22-16<br>SEL2|This read-only bit field is reserved and always has the value 0.<br>Trigger MUX Input 2 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 2. For the field setting<br>definitions, seeMemory map and register definition.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|
|14-8<br>SEL1|Trigger MUX Input 1 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7<br>—|This read-only bit field is reserved and always has the value 0.|
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2322 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

#### 63.4.1.13 TRGMUX eMIOS0_3 Register (eMIOS0_3) 

##### Offset 

|Register|Offset|
|---|---|
|eMIOS0_3|2Ch|



##### Function 

This register is for the eMIOS0_3 module. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|LK||||0||||0||||0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|0||||SEL1||||0||||SEL0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>—|This read-only bit field is reserved and always has the value 0.|
|23<br>—|This read-only bit field is reserved and always has the value 0.|
|22-16<br>—|This read-only bit field is reserved and always has the value 0.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2323 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|14-8|Trigger MUX Input 1 Source Select|
|SEL1|This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7|This read-only bit field is reserved and always has the value 0.|
|—||
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



#### 63.4.1.14 TRGMUX eMIOS1_0 Register (eMIOS1_0) 

##### Offset 

|Register|Offset|
|---|---|
|eMIOS1_0|30h|



##### Function 

This register is for the eMIOS1_0 module. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|LK||||SEL3||||0||||SEL2||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|0||||SEL1||||0||||SEL0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2324 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>SEL3|Trigger MUX Input 3 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 3. For the field setting<br>definitions, seeMemory map and register definition.|
|23<br>—|This read-only bit field is reserved and always has the value 0.|
|22-16<br>SEL2|Trigger MUX Input 2 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 2. For the field setting<br>definitions, seeMemory map and register definition.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|
|14-8<br>SEL1|Trigger MUX Input 1 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7<br>—|This read-only bit field is reserved and always has the value 0.|
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



#### 63.4.1.15 TRGMUX eMIOS1_1 Register (eMIOS1_1) 

##### Offset 

|Register|Offset|
|---|---|
|eMIOS1_1|34h|



Function 

This register is for the eMIOS1_1 module. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2325 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2326-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>LK  SEL3  SEL2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>SEL1  SEL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>SEL3|Trigger MUX Input 3 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 3. For the field setting<br>definitions, seeMemory map and register definition.|
|23<br>—<br>22-16<br>SEL2|This read-only bit field is reserved and always has the value 0.<br>Trigger MUX Input 2 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 2. For the field setting<br>definitions, seeMemory map and register definition.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|
|14-8<br>SEL1|Trigger MUX Input 1 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7<br>—|This read-only bit field is reserved and always has the value 0.|
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2326 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

#### 63.4.1.16 TRGMUX eMIOS1_2 Register (eMIOS1_2) 

##### Offset 

|Register|Offset|
|---|---|
|eMIOS1_2|38h|



##### Function 

This register is for the eMIOS1_2 module. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2327-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>LK  SEL3  SEL2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>SEL1  SEL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>SEL3|Trigger MUX Input 3 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 3. For the field setting<br>definitions, seeMemory map and register definition.|
|23<br>—|This read-only bit field is reserved and always has the value 0.|
|22-16|Trigger MUX Input 2 Source Select|
|SEL2|This read/write bit field is used to configure the MUX select for peripheral trigger input 2. For the field setting<br>definitions, seeMemory map and register definition.|
|15|This read-only bit field is reserved and always has the value 0.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2327 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|14-8|Trigger MUX Input 1 Source Select|
|SEL1|This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7|This read-only bit field is reserved and always has the value 0.|
|—||
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



#### 63.4.1.17 TRGMUX eMIOS1_3 Register (eMIOS1_3) 

##### Offset 

|Register|Offset|
|---|---|
|eMIOS1_3|3Ch|



##### Function 

This register is for the eMIOS1_3 module. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2328-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0 0<br>LK<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>SEL1  SEL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function||
|---|---|---|
|31|TRGMUX register lock.||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2328 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>—<br>23<br>—<br>22-16<br>—|This read-only bit field is reserved and always has the value 0.<br>This read-only bit field is reserved and always has the value 0.<br>This read-only bit field is reserved and always has the value 0.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|
|14-8<br>SEL1|Trigger MUX Input 1 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7<br>—<br>6-0|This read-only bit field is reserved and always has the value 0.<br>Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



#### 63.4.1.18 TRGMUX FlexIO Register (FlexIO) 

##### Offset 

|Register|Offset|
|---|---|
|FlexIO|40h|



##### Function 

This register is for the FlexIO module. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2329 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2330-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>LK  SEL3  SEL2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>SEL1  SEL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>SEL3|Trigger MUX Input 3 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 3. For the field setting<br>definitions, seeMemory map and register definition.|
|23<br>—<br>22-16<br>SEL2|This read-only bit field is reserved and always has the value 0.<br>Trigger MUX Input 2 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 2. For the field setting<br>definitions, seeMemory map and register definition.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|
|14-8<br>SEL1|Trigger MUX Input 1 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7<br>—|This read-only bit field is reserved and always has the value 0.|
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2330 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

#### 63.4.1.19 TRGMUX SIUL_OUT0 Register (SIUL_OUT0) 

##### Offset 

|Register|Offset|
|---|---|
|SIUL_OUT0|44h|



##### Function 

This register is for the SIUL_OUT0 module. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2331-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>LK  SEL3  SEL2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>SEL1  SEL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>SEL3|Trigger MUX Input 3 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 3. For the field setting<br>definitions, seeMemory map and register definition.|
|23<br>—|This read-only bit field is reserved and always has the value 0.|
|22-16|Trigger MUX Input 2 Source Select|
|SEL2|This read/write bit field is used to configure the MUX select for peripheral trigger input 2. For the field setting<br>definitions, seeMemory map and register definition.|
|15|This read-only bit field is reserved and always has the value 0.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2331 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|14-8|Trigger MUX Input 1 Source Select|
|SEL1|This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7|This read-only bit field is reserved and always has the value 0.|
|—||
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



#### 63.4.1.20 TRGMUX SIUL_OUT1 Register (SIUL_OUT1) 

##### Offset 

|Register|Offset|
|---|---|
|SIUL_OUT1|48h|



##### Function 

This register is for the SIUL_OUT1 module. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2332-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>LK  SEL3  SEL2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>SEL1  SEL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2332 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>SEL3|Trigger MUX Input 3 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 3. For the field setting<br>definitions, seeMemory map and register definition.|
|23<br>—|This read-only bit field is reserved and always has the value 0.|
|22-16<br>SEL2|Trigger MUX Input 2 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 2. For the field setting<br>definitions, seeMemory map and register definition.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|
|14-8<br>SEL1|Trigger MUX Input 1 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7<br>—|This read-only bit field is reserved and always has the value 0.|
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



#### 63.4.1.21 TRGMUX SIUL_OUT2 Register (SIUL_OUT2) 

##### Offset 

|Register|Offset|
|---|---|
|SIUL_OUT2|4Ch|



Function 

This register is for the SIUL_OUT2 module. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2333 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2334-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>LK  SEL3  SEL2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>SEL1  SEL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>SEL3|Trigger MUX Input 3 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 3. For the field setting<br>definitions, seeMemory map and register definition.|
|23<br>—<br>22-16<br>SEL2|This read-only bit field is reserved and always has the value 0.<br>Trigger MUX Input 2 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 2. For the field setting<br>definitions, seeMemory map and register definition.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|
|14-8<br>SEL1|Trigger MUX Input 1 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7<br>—|This read-only bit field is reserved and always has the value 0.|
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2334 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

#### 63.4.1.22 TRGMUX SIUL_OUT3 Register (SIUL_OUT3) 

##### Offset 

|Register|Offset|
|---|---|
|SIUL_OUT3|50h|



##### Function 

This register is for the SIUL_OUT3 module. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2335-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>LK  SEL3  SEL2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>SEL1  SEL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>SEL3|Trigger MUX Input 3 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 3. For the field setting<br>definitions, seeMemory map and register definition.|
|23<br>—|This read-only bit field is reserved and always has the value 0.|
|22-16|Trigger MUX Input 2 Source Select|
|SEL2|This read/write bit field is used to configure the MUX select for peripheral trigger input 2. For the field setting<br>definitions, seeMemory map and register definition.|
|15|This read-only bit field is reserved and always has the value 0.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2335 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|14-8|Trigger MUX Input 1 Source Select|
|SEL1|This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7|This read-only bit field is reserved and always has the value 0.|
|—||
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



#### 63.4.1.23 TRGMUX LPI2C_0 Register (LPI2C_0) 

##### Offset 

|Register|Offset|
|---|---|
|LPI2C_0|54h|



##### Function 

This register is for the LPI2C_0 module. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2336-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0 0<br>LK<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 0<br>SEL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function||
|---|---|---|
|31|TRGMUX register lock.||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2336 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>—|This read-only bit field is reserved and always has the value 0.|
|23<br>—|This read-only bit field is reserved and always has the value 0.|
|22-16<br>—|This read-only bit field is reserved and always has the value 0.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|
|14-8<br>—|This read-only bit field is reserved and always has the value 0.|
|7<br>—|This read-only bit field is reserved and always has the value 0.|
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



#### 63.4.1.24 TRGMUX LPSPI_0 Register (LPSPI_0) 

##### Offset 

|Register|Offset|
|---|---|
|LPSPI_0|58h|



##### Function 

This register is for the LPSPI_0 module. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2337 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|LK||||0||||0||||0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|0||||0||||0||||SEL0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>—|This read-only bit field is reserved and always has the value 0.|
|23<br>—|This read-only bit field is reserved and always has the value 0.|
|22-16<br>—|This read-only bit field is reserved and always has the value 0.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|
|14-8<br>—<br>7<br>—|This read-only bit field is reserved and always has the value 0.<br>This read-only bit field is reserved and always has the value 0.|
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2338 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

#### 63.4.1.25 TRGMUX LPSPI_1 Register (LPSPI_1) 

##### Offset 

|Register|Offset|
|---|---|
|LPSPI_1|5Ch|



##### Function 

This register is for the LPSPI_1 module. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|LK||||0||||0||||0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|0||||0||||0||||SEL0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>—|This read-only bit field is reserved and always has the value 0.|
|23<br>—|This read-only bit field is reserved and always has the value 0.|
|22-16<br>—|This read-only bit field is reserved and always has the value 0.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2339 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|14-8|This read-only bit field is reserved and always has the value 0.|
|—||
|7|This read-only bit field is reserved and always has the value 0.|
|—||
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



#### 63.4.1.26 TRGMUX LPSPI_2 Register (LPSPI_2) 

##### Offset 

|Register|Offset|
|---|---|
|LPSPI_2|60h|



##### Function 

This register is for the LPSPI_2 module. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2340-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0 0<br>LK<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 0<br>SEL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2340 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>—|This read-only bit field is reserved and always has the value 0.|
|23<br>—|This read-only bit field is reserved and always has the value 0.|
|22-16<br>—|This read-only bit field is reserved and always has the value 0.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|
|14-8<br>—|This read-only bit field is reserved and always has the value 0.|
|7<br>—|This read-only bit field is reserved and always has the value 0.|
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



#### 63.4.1.27 TRGMUX LPUART_0 Register (LPUART_0) 

##### Offset 

|Register|Offset|
|---|---|
|LPUART_0|64h|



##### Function 

This register is for the LPUART_0 module. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2341 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|LK||||0||||0||||0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|0||||0||||0||||SEL0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>—|This read-only bit field is reserved and always has the value 0.|
|23<br>—|This read-only bit field is reserved and always has the value 0.|
|22-16<br>—|This read-only bit field is reserved and always has the value 0.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|
|14-8<br>—<br>7<br>—|This read-only bit field is reserved and always has the value 0.<br>This read-only bit field is reserved and always has the value 0.|
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2342 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

#### 63.4.1.28 TRGMUX LPUART_1 Register (LPUART_1) 

##### Offset 

|Register|Offset|
|---|---|
|LPUART_1|68h|



##### Function 

This register is for the LPUART_1 module. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|LK||||0||||0||||0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|0||||0||||0||||SEL0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>—|This read-only bit field is reserved and always has the value 0.|
|23<br>—|This read-only bit field is reserved and always has the value 0.|
|22-16<br>—|This read-only bit field is reserved and always has the value 0.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2343 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|14-8|This read-only bit field is reserved and always has the value 0.|
|—||
|7|This read-only bit field is reserved and always has the value 0.|
|—||
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



#### 63.4.1.29 TRGMUX LPUART_2 Register (LPUART_2) 

##### Offset 

|Register|Offset|
|---|---|
|LPUART_2|6Ch|



##### Function 

This register is for the LPUART_2 module. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2344-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0 0<br>LK<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0 0<br>SEL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2344 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>—|This read-only bit field is reserved and always has the value 0.|
|23<br>—|This read-only bit field is reserved and always has the value 0.|
|22-16<br>—|This read-only bit field is reserved and always has the value 0.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|
|14-8<br>—|This read-only bit field is reserved and always has the value 0.|
|7<br>—|This read-only bit field is reserved and always has the value 0.|
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



#### 63.4.1.30 TRGMUX LPUART_3 Register (LPUART_3) 

##### Offset 

|Register|Offset|
|---|---|
|LPUART_3|70h|



##### Function 

This register is for the LPUART_3 module. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2345 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|LK||||0||||0||||0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|0||||0||||0||||SEL0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>—|This read-only bit field is reserved and always has the value 0.|
|23<br>—|This read-only bit field is reserved and always has the value 0.|
|22-16<br>—|This read-only bit field is reserved and always has the value 0.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|
|14-8<br>—<br>7<br>—|This read-only bit field is reserved and always has the value 0.<br>This read-only bit field is reserved and always has the value 0.|
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2346 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

#### 63.4.1.31 TRGMUX LCU0_SYNC Register (LCU0_SYNC) 

##### Offset 

|Register|Offset|
|---|---|
|LCU0_SYNC|74h|



##### Function 

This register is for the LCU0_SYNC module. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|LK||||0||||0||||0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|0||||SEL1||||0||||SEL0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>—|This read-only bit field is reserved and always has the value 0.|
|23<br>—|This read-only bit field is reserved and always has the value 0.|
|22-16<br>—|This read-only bit field is reserved and always has the value 0.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2347 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|14-8|Trigger MUX Input 1 Source Select|
|SEL1|This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7|This read-only bit field is reserved and always has the value 0.|
|—||
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



#### 63.4.1.32 TRGMUX LCU0_FORCE Register (LCU0_FORCE) 

##### Offset 

|Register|Offset|
|---|---|
|LCU0_FORCE|78h|



##### Function 

This register is for the LCU0_FORCE module. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|LK||||0||||0||||SEL2||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|0||||SEL1||||0||||SEL0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



##### Fields 

|Field|Function||
|---|---|---|
|31|TRGMUX register lock.||
|LK|||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2348 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
||This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>—|This read-only bit field is reserved and always has the value 0.|
|23<br>—<br>22-16<br>SEL2|This read-only bit field is reserved and always has the value 0.<br>Trigger MUX Input 2 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 2. For the field setting<br>definitions, seeMemory map and register definition.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|
|14-8<br>SEL1|Trigger MUX Input 1 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7<br>—|This read-only bit field is reserved and always has the value 0.|
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



#### 63.4.1.33 TRGMUX LCU0_0 Register (LCU0_0) 

##### Offset 

|Register|Offset|
|---|---|
|LCU0_0|7Ch|



Function 

This register is for the LCU0_0 module. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2349 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2350-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>LK  SEL3  SEL2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>SEL1  SEL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>SEL3|Trigger MUX Input 3 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 3. For the field setting<br>definitions, seeMemory map and register definition.|
|23<br>—<br>22-16<br>SEL2|This read-only bit field is reserved and always has the value 0.<br>Trigger MUX Input 2 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 2. For the field setting<br>definitions, seeMemory map and register definition.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|
|14-8<br>SEL1|Trigger MUX Input 1 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7<br>—|This read-only bit field is reserved and always has the value 0.|
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2350 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

#### 63.4.1.34 TRGMUX LCU0_1 Register (LCU0_1) 

##### Offset 

|Register|Offset|
|---|---|
|LCU0_1|80h|



##### Function 

This register is for the LCU0_1 module. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2351-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>LK  SEL3  SEL2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>SEL1  SEL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>SEL3|Trigger MUX Input 3 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 3. For the field setting<br>definitions, seeMemory map and register definition.|
|23<br>—|This read-only bit field is reserved and always has the value 0.|
|22-16|Trigger MUX Input 2 Source Select|
|SEL2|This read/write bit field is used to configure the MUX select for peripheral trigger input 2. For the field setting<br>definitions, seeMemory map and register definition.|
|15|This read-only bit field is reserved and always has the value 0.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2351 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|14-8|Trigger MUX Input 1 Source Select|
|SEL1|This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7|This read-only bit field is reserved and always has the value 0.|
|—||
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



#### 63.4.1.35 TRGMUX LCU0_2 Register (LCU0_2) 

##### Offset 

|Register|Offset|
|---|---|
|LCU0_2|84h|



##### Function 

This register is for the LCU0_2 module. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2352-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>LK  SEL3  SEL2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>SEL1  SEL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|



|Table continues on the next page...|
|---|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2352 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>SEL3|Trigger MUX Input 3 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 3. For the field setting<br>definitions, seeMemory map and register definition.|
|23<br>—|This read-only bit field is reserved and always has the value 0.|
|22-16<br>SEL2|Trigger MUX Input 2 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 2. For the field setting<br>definitions, seeMemory map and register definition.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|
|14-8<br>SEL1|Trigger MUX Input 1 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7<br>—|This read-only bit field is reserved and always has the value 0.|
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



#### 63.4.1.36 TRGMUX LCU1_SYNC Register (LCU1_SYNC) 

##### Offset 

|Register|Offset|
|---|---|
|LCU1_SYNC|88h|



Function 

This register is for the LCU1_SYNC module. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2353 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2354-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0 0<br>LK<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>SEL1  SEL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>—<br>23<br>—<br>22-16<br>—<br>15<br>—|This read-only bit field is reserved and always has the value 0.<br>This read-only bit field is reserved and always has the value 0.<br>This read-only bit field is reserved and always has the value 0.<br>This read-only bit field is reserved and always has the value 0.|
|14-8<br>SEL1|Trigger MUX Input 1 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7<br>—|This read-only bit field is reserved and always has the value 0.|
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

2354 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

#### 63.4.1.37 TRGMUX LCU1_FORCE Register (LCU1_FORCE) 

##### Offset 

|Register|Offset|
|---|---|
|LCU1_FORCE|8Ch|



##### Function 

This register is for the LCU1_FORCE module. 

##### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|LK||||0||||0||||SEL2||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|0||||SEL1||||0||||SEL0||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>—|This read-only bit field is reserved and always has the value 0.|
|23<br>—|This read-only bit field is reserved and always has the value 0.|
|22-16|Trigger MUX Input 2 Source Select|
|SEL2|This read/write bit field is used to configure the MUX select for peripheral trigger input 2. For the field setting<br>definitions, seeMemory map and register definition.|
|15|This read-only bit field is reserved and always has the value 0.|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2355 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|14-8|Trigger MUX Input 1 Source Select|
|SEL1|This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7|This read-only bit field is reserved and always has the value 0.|
|—||
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



#### 63.4.1.38 TRGMUX LCU1_0 Register (LCU1_0) 

##### Offset 

|Register|Offset|
|---|---|
|LCU1_0|90h|



##### Function 

This register is for the LCU1_0 module. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2356-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>LK  SEL3  SEL2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>SEL1  SEL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2356 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>SEL3|Trigger MUX Input 3 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 3. For the field setting<br>definitions, seeMemory map and register definition.|
|23<br>—|This read-only bit field is reserved and always has the value 0.|
|22-16<br>SEL2|Trigger MUX Input 2 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 2. For the field setting<br>definitions, seeMemory map and register definition.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|
|14-8<br>SEL1|Trigger MUX Input 1 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7<br>—|This read-only bit field is reserved and always has the value 0.|
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



#### 63.4.1.39 TRGMUX LCU1_1 Register (LCU1_1) 

##### Offset 

|Register|Offset|
|---|---|
|LCU1_1|94h|



Function 

This register is for the LCU1_1 module. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2357 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2358-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>LK  SEL3  SEL2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>SEL1  SEL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

##### Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>SEL3|Trigger MUX Input 3 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 3. For the field setting<br>definitions, seeMemory map and register definition.|
|23<br>—<br>22-16<br>SEL2|This read-only bit field is reserved and always has the value 0.<br>Trigger MUX Input 2 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 2. For the field setting<br>definitions, seeMemory map and register definition.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|
|14-8<br>SEL1|Trigger MUX Input 1 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7<br>—|This read-only bit field is reserved and always has the value 0.|
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2358 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

#### 63.4.1.40 TRGMUX LCU1_2 Register (LCU1_2) 

##### Offset 

|Register|Offset|
|---|---|
|LCU1_2|98h|



##### Function 

This register is for the LCU1_2 module. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2359-08.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0<br>LK  SEL3  SEL2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>SEL1  SEL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function|
|---|---|
|31|TRGMUX register lock.|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>SEL3|Trigger MUX Input 3 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 3. For the field setting<br>definitions, seeMemory map and register definition.|
|23<br>—|This read-only bit field is reserved and always has the value 0.|
|22-16|Trigger MUX Input 2 Source Select|
|SEL2|This read/write bit field is used to configure the MUX select for peripheral trigger input 2. For the field setting<br>definitions, seeMemory map and register definition.|
|15|This read-only bit field is reserved and always has the value 0.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2359 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|—||
|14-8|Trigger MUX Input 1 Source Select|
|SEL1|This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7|This read-only bit field is reserved and always has the value 0.|
|—||
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



#### 63.4.1.41 TRGMUX CM7_RXEV Register (CM7_RXEV) 

##### Offset 

|Register|Offset|
|---|---|
|CM7_RXEV|9Ch|



##### Function 

This register is for the CM7_RXEV module. 

##### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Real-time_control/063_Trigger_MUX_-TRGMUX-/S32K3XXRM_数据表.pdf-2360-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R 0 0<br>LK  SEL2<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R 0 0<br>SEL1  SEL0<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

Fields 

|Field|Function||
|---|---|---|
|31|TRGMUX register lock.||
|||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2360 / 4640 

NXP Semiconductors 

Trigger MUX (TRGMUX) 

##### Table continued from the previous page... 

|Field|Function|
|---|---|
|LK|This bit shows whether the register can be written or not. The LK bit can only be written once after any<br>system reset. Once LK is set, the SELx bits in this TRGMUX register cannot be changed until the next<br>system reset clears LK.<br>0b - Register can be written.<br>1b - Register cannot be written until the next system Reset.|
|30-24<br>—|This read-only bit field is reserved and always has the value 0.|
|23<br>—<br>22-16<br>SEL2|This read-only bit field is reserved and always has the value 0.<br>Trigger MUX Input 2 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 2. For the field setting<br>definitions, seeMemory map and register definition.|
|15<br>—|This read-only bit field is reserved and always has the value 0.|
|14-8<br>SEL1|Trigger MUX Input 1 Source Select<br>This read/write bit field is used to configure the MUX select for peripheral trigger input 1. For the field setting<br>definitions, seeMemory map and register definition.|
|7<br>—|This read-only bit field is reserved and always has the value 0.|
|6-0|Trigger MUX Input 0 Source Select|
|SEL0|This read/write bit field is used to configure the MUX select for peripheral trigger input 0. For the field setting<br>definitions, seeMemory map and register definition.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

2361 / 4640 

