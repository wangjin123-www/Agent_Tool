NXP Semiconductors 

# Chapter 23 Clocking 

## 23.1 Introduction 

This chapter describes the clocking architecture and includes the following information: 

- System clock specifics 

- Clock sources 

- Clock architecture 

- Clock control registers 

- Clock monitoring 

- Clock gating 

- Module clocking 

This chapter discusses the clocks generated on the chip. Peripheral-specific protocol clocks are described in the corresponding peripheral chapters. 

## 23.2 Features 

- Multiple clock sources supported for clock generation: 

   - Fast internal RC oscillator (FIRC) 

   - Slow internal RC oscillator (SIRC) 

   - Fast external crystal oscillator (FXOSC) 

   - Slow external crystal oscillator (SXOSC) 

~~<mark>NOTE</mark>~~ 

SXOSC is not available in 100-MAX QFP and 48-pin LQFP packages. For details, see 'S32K3xx chip's feature comparison' table in Introduction chapter. 

   - Phase-locked loop (PLL) 

- Frequency-modulated PLL output clock to reduce electromagnetic emissions 

- Precise clocks for timers and communication functions 

- Glitchless clock switching Clock Generation module (MC_CGM) clock selectors 

- System clock progressive clock frequency switching (PCFS) 

- Clock monitoring units (CMU_FC, CMU_FM) to check clock integrity 

- Core and peripheral clock gating using the Mode Entry module's (MC_ME) partition process configuration registers 

## 23.3 Clocking overview 

The S32K3xx clocking architecture consists of multiple: 

- Clock sources 

- Monitors 

- Multiplexers 

- Dividers 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

740 / 4640 

NXP Semiconductors 

Clocking 

The blocks in the above bullet list provide the required clocking domains for the different functional blocks. 

The sections in the following list show the clocking configuration of the chip: 

- Clock source generation: PLL, FXOSC, FIRC, SIRC, and SXOSC 

- MC_CGM mux 0 clocks: MC_CGM mux 0 generated clocks (not including EMAC clock signals) 

- Clockout overview: CLKOUT_STANDBY and CLKOUT_RUN 

- Other clocks 

- EMAC clocking: Ethernet utilized clocking 

The figures shown in S32K344, S32K324, S32K314, S32K322, and S32K342 clock system diagram, S32K312 clock system diagram, and S32K311 clock system diagram show the overall clock tree for the different chip variants of the S32K3xx family, which are a combination of the sections mentioned in the bullet list above. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

741 / 4640 

NXP Semiconductors 

Clocking 

### 23.3.1 Clock source generation 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0742-03.png)


<!-- Start of picture text -->
PLLDIG<br>PLLDIG.PLLODIV_0[DIV]<br>1... 32 PLL_AUX_PHI0_CLK<br>PLLDIG.PLLDV[ODIV2]<br>PLLDIG.PLLODIV_1[DIV] Only available on:<br>VCO_CLK PLLODIV2_CLK - S32K358<br>PLL_AUX 1...63 1... 32 PLL_AUX_PHI1_CLK<br>1...32 PLL_AUX_PHI2_CLK<br>PLLDIG.PLLODIV_2[DIV]<br>PLLDIG<br>PLLDIG.PLLODIV_0[DIV]<br>PLLDIG.PLLDV[ODIV2]<br>1... 16 PLL_PHI0_CLK<br>VCO_CLK PLLODIV2_CLK<br>PLL 1...63<br>1...16 PLL_PHI1_CLK<br>PLLDIG.PLLODIV_1[DIV]<br>FIRC<br>3 CMU_FM_1<br>DIV16 2<br>FIRC FIRC_CLK<br>DIV2 1<br>DIV2 0<br>HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL]<br>CMU_FC_0<br>EXTAL<br>FXOSC FXOSC_CLK<br>XTAL<br>OSC32K_EXTAL Not available on:<br>SXOSC SXOSC_CLK - S32K311<br>OSC32K_XTAL<br>CMU_FM_2<br>SIRC SIRC_CLK<br>Figure 50. Clock source generation<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

742 / 4640 

NXP Semiconductors 

Clocking 

### 23.3.2 MC_CGM mux 0 clocks 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0743-03.png)


<!-- Start of picture text -->
MUX_0_DC_0[DIV] CMU_FC_3<br>1...8 CORE_CLK<br>MUX_0_DC_1[DIV] CMU_FC_4<br>1...8 AIPS_PLAT_CLK<br>MUX_0_DC_2[DIV]<br>1...16 AIPS_SLOW_CLK<br>MUX0_0_CSC[RAMPUP]<br>MUX0_0_CSC[RAMPDOWN]<br>MUX_0_DC_3[DIV] CMU_FC_5<br>PLL_PHI0_CLK 8<br>PCFS 1...8 HSE_CLK<br>FIRC_CLK 0<br>PCFS_SDUR[SDUR] MUX_0_DC_4[DIV]<br>MUX_0_CSC[SELCTL] 1...8 DCM_CLK<br>MUX_0_DC_5[DIV]<br>1...8 LBIST_CLK Not available on:<br>- S32K311<br>- S32K312<br>MUX_0_DC_6[DIV]<br>1...8 QSPI_MEM_CLK<br><!-- End of picture text -->

Figure 51. MC_CGM mux 0 clocks 

~~<mark>NOTE</mark>~~ 

The clock frequency relationship between TCK and HSE_CLK clocks for HSE_B must be a minimum ratio of 1:1.5. For example, if HSE_CLK equals 80 MHz, then TCK must be less than or equal to 53 MHz (80 MHz ÷ 1.5). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

743 / 4640 

NXP Semiconductors 

Clocking 

### 23.3.3 Clockout overview 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0744-03.png)


<!-- Start of picture text -->
MUX_6_CSC[SELCTL]<br>Not available on: EMAC_RX_CLK 25<br>- S32K311<br>- S32K312 EMAC_RMII_TX_CLK 24<br>AIPS_SLOW_CLK 23 Port<br>AIPS_PLAT_CLK 22<br>HSE_CLK 19 MUX_6_DC_0[DIV] SIUL2_MSCR n [OBE]<br>CORE_CLK 16<br>Only available on: PLL_AUX_PHI2_CLK 14 1...64 CLKOUT_RUN<br>- S32K358 PLL_AUX_PHI1_CLK 13<br>PLL_AUX_PHI0_CLK 12<br>PLL_PHI1_CLK 9<br>SIUL2_MSCR n [SSS]<br>PLL_PHI0_CLK 8<br>Not available on:<br>- S32K311 SXOSC_CLK 4<br>FXOSC_CLK 2<br>FIRC_CLK 1<br>SIRC_CLK 0<br>Port<br>MUX_5_DC_0[DIV] SIUL2_MSCR m [OBE]<br>AIPS_SLOW_CLK 23<br>Not available on:<br>- S32K311 SXOSC_CLK 4 1...8 CLKOUT_STANDBY<br>FXOSC_CLK 2<br>SIRC_CLK 1<br>FIRC_CLK 0<br>SIUL2_MSCR m [SSS]<br>MUX_5_CSC[SELCTL]<br>Figure 52. Clockout overview<br><!-- End of picture text -->


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0744-04.png)


<!-- Start of picture text -->
  NOTE<br>CLKOUT_RUN is not available during Standby mode.<br><!-- End of picture text -->

#### 23.3.3.1 SIUL2 options for CLKOUT_RUN 

Table 99. SIUL2 options for CLKOUT_RUN 

|Source|Destination|Port|MSCRn||MSCR fields||
|---|---|---|---|---|---|---|
|||||OBE|IBE|SSS|
|||PTB5|37|1|0|0101b|
|MUX_6_DC_0 divider<br>output|CLKOUT_RUN|PTD10|106|1|0|0110b|
|||PTD14|110|1|0|0111b|



#### 23.3.3.2 SIUL2 options for CLKOUT_STANDBY 

Table 100. SIUL2 options for CLKOUT_STANDBY 

|Source|Destination|Port|MSCRm||MSCR fields||
|---|---|---|---|---|---|---|
|||||OBE|IBE|SSS|
|MUX_5_DC_0 divider|CLKOUTSTANDBY|PTA12|12|1|0|0011b|
|output|_|PTE10|138|1|0|0101b|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

744 / 4640 

NXP Semiconductors 

Clocking 

### 23.3.4 Other clocks 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0745-03.png)


<!-- Start of picture text -->
MUX_1_CSC[SELCTL]<br>AIPS_PLAT_CLK 22 MUX_1_DC_0[DIV]<br>FXOSC_CLK 2 1...2 STM0_CLK<br>FIRC_CLK 0<br>MUX_2_CSC[SELCTL]<br>MUX_2_DC_0[DIV] Not available on:<br>22 - S32K314<br>- S32K312<br>2 1...2 STM1_CLK<br>- S32K311<br>0<br>MUX_3_CSC[SELCTL]<br>MUX_3_DC_0[DIV]<br>22<br>CORE_CLK 16<br>1...4 FLEXCAN0_PE_CLK<br>2<br>FLEXCAN1_PE_CLK<br>0<br>FLEXCAN2_PE_CLK<br>Not available on:<br>MUX_4_CSC[SELCTL] - S32K311<br>FLEXCAN3_PE_CLK<br>22 MUX_4_DC_0[DIV] FLEXCAN4_PE_CLK Not available on:<br>16 - S32K342<br>2 1...4 FLEXCAN5_PE_CLK - S32K312<br>0 FLEXCAN6_PE_CLK Only available on:<br>FLEXCAN7_PE_CLK - S32K358<br>MUX_10_CSC[SELCTL]<br>PLL_AUX_PHI0_CLK 12 MUX_10_DC_0[DIV] Not available on:<br>PLL_PHI1_CLK 9 - S32K312<br>2 1...8 QSPI_2xSFCK - S32K311<br>0 DIV-BY-2 QSPI_SFCK<br>MUX_11_CSC[SELCTL]<br>9 MUX_11_DC_0[DIV]<br>PLL_PHI0_CLK 8<br>1...8 TRACE_CLK<br>2<br>0<br>MUX_13_CSC[SELCTL]<br>MUX_13_DC_0[DIV]<br>22<br>2 1...2 STM2_CLK<br>0<br>Only available on:<br>- S32K358<br>MUX_14_CSC[SELCTL]<br>MUX_14_DC_0[DIV]<br>14<br>9<br>1...2 uSDHC_PER_CLK<br>2<br>0<br>JTAG_TCK/SWD_CLK TCK<br><!-- End of picture text -->

Figure 53. Other clocks 

~~S32K3xx Reference Manual, Rev. 4, 04/2022~~ Preliminary Information 

Reference Manual 

745 / 4640 

NXP Semiconductors 

Clocking 

### 23.3.5 S32K358 clock system diagram 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0746-03.png)


<!-- Start of picture text -->
MC_CGM<br>MUX_0_DC_0[DIV] CMU_FC_3<br>1...8 CORE_CLK<br>MUX_0_DC_1[DIV] CMU_FC_4<br>1...8 AIPS_PLAT_CLK<br>MUX_0_DC_2[DIV]<br>1...16 AIPS_SLOW_CLK<br>8 MUX_0_DC_3[DIV] CMU_FC_5<br>CMU with FXOSC reference PCFS 1...8 HSE_CLK<br>CMU with FIRC reference 0 MUX_0_DC_4[DIV]<br>MC_CGM_MUX0 1...8 DCM_CLK<br>MUX_0_DC_5[DIV]<br>1...8 LBIST_CLK<br>MUX_0_DC_6[DIV]<br>PLL_Aux only present in S32K358 1...8 QSPI_MEM_CLK<br>PLLDIG.PLLODIV_0[DIV] PLL_AUX_PHI0_CLK<br>PLLDIG.PLLDV[ODIV2] 1...32<br>PLL_AUX_PHI1_CLK<br>PLL_AUX VCO_CLK 1...63 PLLODIV2_CLK 1...32<br>PLLDIG.PLLODIV_1[DIV]<br>PLL_AUX_PHI2_CLK<br>1...32 22 MUX_1_DC_0[DIV]<br>2 1...2 STM0_CLK<br>PLLDIG.PLLODIV_2[DIV] 0<br>MC_CGM_MUX1<br>PLL VCO_CLKPLLDIG.PLLDV[ODIV2]1...63 PLLODIV2_CLKPLLDIG.PLLODIV_0[DIV] 1...16 PLL_PHI0_CLK 2220 MC_CGM_MUX2 MUX_2_DC_0[DIV]1...2 STM1_CLK<br>1...16 PLL_PHI1_CLK 22 MUX_3_DC_0[DIV]<br>PLLDIG.PLLODIV_1[DIV] 162 1...4 FLEXCAN[0:2]_PE_CLK<br>0<br>MC_CGM_MUX3<br>22 MUX_4_DC_0[DIV]<br>(48 MHz)FIRC ÷16÷2 213 FIRC_CLK 1602 MC_CGM_MUX4 1...4 FLEXCAN[3:7]_PE_CLK<br>÷2 0 CMU_FM_1<br>HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL] 23<br>MUX_5_DC_0[DIV]<br>1...8 CLKOUT_STANDBY<br>4<br>2<br>1<br>0<br>EXTAL FXOSC FXOSC_CLK MC_CGM_MUX5<br>XTAL (8-40 MHz) CMU_FC_0 1916 1 12 13 222423254 MUX_6_DC_0[DIV]1...64 CLKOUT_RUN<br>9<br>OSC32K_EXTAL SXOSC (32 KHZ)  842<br>OSC32K_XTAL 1<br>0<br>MC_CGM_MUX6<br>25 MUX_7_DC_0[DIV]<br>1224 1...64 EMAC_CLK_RX<br>8<br>0 MC_CGM_MUX7<br>1224 MUX_8_DC_0[DIV]1...64 EMAC_CLK_TX<br>8<br>SIRC SIRC_CLK 0 MC_CGM_MUX8<br>(32 kHz) CMU_FM_2 12252482 MUX_9_DC_0[DIV]1...64 EMAC_CLK_TS<br>0<br>MC_CGM_MUX9<br>12<br>EMAC_MII_RX_CLK 920 .div-by-2 MUX_10_DC_0[DIV]1...8 QSPI_2XSFIF<br>EMAC_MII_RMII_TX_CLK MC_CGM_MUX10 .div-by-2 QSPI_SFCK<br>129 MUX_11_DC_0[DIV]<br>8 1...8 TRACE_CLK<br>2<br>1<br>0<br>MC_CGM_MUX11<br>128 MUX_12_DC_0[DIV]<br>2 1...64 EMAC_CLK_TX_RMII<br>0<br>MC_CGM_MUX12<br>22 MUX_13_DC_0[DIV]<br>2 1...2 STM2_CLK<br>0<br>MC_CGM_MUX13<br>14 MUX_14_DC_0[DIV]<br>92 1...2 uSDHC_CLK<br>0<br>MC_CGM_MUX14<br>RTC<br>0<br>1 1<br>23 23 RTC_CLK<br>RTC.RTCC[CLKSEL]<br>JTAG_TCK/SWD_CLK TCK<br><!-- End of picture text -->

Figure 54. S32K358 clock system diagram S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

746 / 4640 

NXP Semiconductors 

Clocking 

### 23.3.6 S32K344, S32K324, S32K314, S32K322, and S32K342 clock system diagram 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0747-03.png)


<!-- Start of picture text -->
S32K3xx<br>MC_CGM MUX_0_DC_0[DIV] CMU_FC_3<br>1...8 CORE_CLK<br>MUX_0_DC_1[DIV] CMU_FC_4<br>1...8 AIPS_PLAT_CLK<br>MUX_0_DC_2[DIV]<br>1...16 AIPS_SLOW_CLK<br>8 MUX_0_DC_3[DIV] CMU_FC_5<br>PCFS 1...8 HSE_CLK<br>0 MUX_0_DC_4[DIV]<br>MC_CGM_MUX0 1...8 DCM_CLK<br>MUX_0_DC_5[DIV]<br>1...8 LBIST_CLK<br>MUX_0_DC_6[DIV]<br>1...8 QSPI_MEM_CLK<br>CMU with FXOSC reference<br>CMU with FIRC reference<br>22 MUX_1_DC_0[DIV]<br>2 1...2 STM0_CLK<br>0<br>MC_CGM_MUX1<br>22 MUX_2_DC_0[DIV]<br>PLL VCO_CLKPLLDIG.PLLDV[ODIV2]1...63 PLLODIV2_CLKPLLDIG.PLLODIV_0[DIV] 1...16 PLL_PHI0_CLK 20 MC_CGM_MUX2 1...2 STM1_CLK Not available onthe S32K314<br>1...16 PLL_PHI1_CLK 22 MUX_3_DC_0[DIV]<br>PLLDIG.PLLODIV_1[DIV] 2 1...4 FLEXCAN[0:2]_PE_CLK<br>0<br>MC_CGM_MUX3<br>(48 MHz)FIRC ÷16÷2 213 FIRC_CLK 2220 MC_CGM_MUX4 MUX_4_DC_0[DIV]1...4 FLEXCAN[3:5]_PE_CLK OnlyFLEXCAN[3]_PE_CLKis available on the S32K322 and S32K342<br>÷2 0 CMU_FM_1<br>HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL] 23<br>MUX_5_DC_0[DIV]<br>1...8 CLKOUT_STANDBY<br>4<br>2<br>1<br>0<br>EXTAL FXOSC FXOSC_CLK MC_CGM_MUX5<br>XTAL (8-40 MHz) 25<br>CMU_FC_0 24<br>23<br>22<br>9 MUX_6_DC_0[DIV]<br>19 1...64 CLKOUT_RUN<br>16<br>8<br>4<br>2<br>1<br>OSC32K_EXTALOSC32K_XTAL (32 kHz)SXOSC SXOSC_CLK 0 MC_CGM_MUX6<br>25 MUX_7_DC_0[DIV]<br>24 1...64 EMAC_CLK_RX<br>0<br>MC_CGM_MUX7<br>24 MUX_8_DC_0[DIV]<br>1...64 EMAC_CLK_TX<br>0<br>SIRC SIRC_CLK MC_CGM_MUX8<br>(32 kHz) CMU_FM_2 25248 MUX_9_DC_0[DIV]1...64 EMAC_CLK_TS<br>2<br>0<br>MC_CGM_MUX9<br>9 MUX_10_DC_0[DIV]<br>2 1...8 QSPI_SFCK<br>EMAC_MII_RX_CLK 0<br>EMAC_MII_RMII_TX_CLK MC_CGM_MUX10<br>9 MUX_11_DC_0[DIV]<br>8 1...8 TRACE_CLK<br>2<br>1<br>0<br>MC_CGM_MUX11<br>RTC<br>0<br>12 RTC_CLK<br>3<br>RTC.RTCC[CLKSEL]<br>JTAG_TCK/SWD_CLK TCK<br><!-- End of picture text -->

Figure 55. S32K344, S32K324, S32K314, S32K322, and S32K342 clock system diagram 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

747 / 4640 

NXP Semiconductors 

Clocking 

### 23.3.7 S32K312 clock system diagram 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0748-03.png)


<!-- Start of picture text -->
S32K3xx<br>MC_CGM MUX_0_DC_0[DIV] CMU_FC_3<br>1...8 CORE_CLK<br>MUX_0_DC_1[DIV] CMU_FC_4<br>1...8 AIPS_PLAT_CLK<br>MUX_0_DC_2[DIV]<br>1...16 AIPS_SLOW_CLK<br>8 MUX_0_DC_3[DIV] CMU_FC_5<br>PCFS 1...8 HSE_CLK<br>0 MUX_0_DC_4[DIV]<br>MC_CGM_MUX0 1...8 DCM_CLK<br>CMU with FXOSC reference<br>CMU with FIRC reference<br>22 MUX_1_DC_0[DIV]<br>2 1...2 STM0_CLK<br>0<br>PLLDIG.PLLODIV_0[DIV]<br>PLLDIG.PLLDV[ODIV2] 1...16 PLL_PHI0_CLK<br>PLL VCO_CLK 1...63 PLLODIV2_CLK<br>1...16 PLL_PHI1_CLK 22 MUX_3_DC_0[DIV]<br>PLLDIG.PLLODIV_1[DIV] 2 1...4 FLEXCAN[0:2]_PE_CLK<br>0<br>MC_CGM_MUX3<br>22 MUX_4_DC_0[DIV]<br>(48 MHz)FIRC ÷16÷2 213 FIRC_CLK 20 MC_CGM_MUX4 1...4 FLEXCAN[3:5]_PE_CLK<br>÷2 0 CMU_FM_1<br>HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL] 23<br>MUX_5_DC_0[DIV]<br>1...8 CLKOUT_STANDBY<br>4<br>2<br>1<br>0<br>EXTAL FXOSC FXOSC_CLK MC_CGM_MUX5<br>XTAL (8-40 MHz) 25<br>CMU_FC_0 24<br>23<br>22<br>9 MUX_6_DC_0[DIV]<br>19 1...64 CLKOUT_RUN<br>16<br>8<br>4<br>2<br>1<br>OSC32K_EXTALOSC32K_XTAL (32 kHz)SXOSC SXOSC_CLK 0 MC_CGM_MUX6<br>SIRC SIRC_CLK<br>(32 kHz)<br>CMU_FM_2<br>MC_CGM_MUX10<br>9 MUX_11_DC_0[DIV]<br>8 1...8 TRACE_CLK<br>2<br>1<br>0<br>MC_CGM_MUX11<br>RTC<br>0<br>12 RTC_CLK<br>3<br>RTC.RTCC[CLKSEL]<br>JTAG_TCK/SWD_CLK TCK<br><!-- End of picture text -->

Figure 56. S32K312 clock system diagram 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

748 / 4640 

NXP Semiconductors 

Clocking 

### 23.3.8 S32K311 clock system diagram 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0749-03.png)


<!-- Start of picture text -->
S32K3xx<br>MC_CGM MUX_0_DC_0[DIV] CMU_FC_3<br>1...8 CORE_CLK<br>MUX_0_DC_1[DIV] CMU_FC_4<br>1...8 AIPS_PLAT_CLK<br>MUX_0_DC_2[DIV]<br>1...16 AIPS_SLOW_CLK<br>8 MUX_0_DC_3[DIV] CMU_FC_5<br>PCFS 1...8 HSE_CLK<br>0 MUX_0_DC_4[DIV]<br>MC_CGM_MUX0 1...8 DCM_CLK<br>CMU with FXOSC reference<br>CMU with FIRC reference<br>22 MUX_1_DC_0[DIV]<br>2 1...2 STM0_CLK<br>0<br>PLLDIG.PLLODIV_0[DIV]<br>PLLDIG.PLLDV[ODIV2] 1...16 PLL_PHI0_CLK<br>PLL VCO_CLK 1...63 PLLODIV2_CLK<br>1...16 PLL_PHI1_CLK 22 MUX_3_DC_0[DIV]<br>PLLDIG.PLLODIV_1[DIV] 2 1...4 FLEXCAN[0:2]_PE_CLK<br>0<br>MC_CGM_MUX3<br>3<br>FIRC ÷16 2 FIRC_CLK<br>(48 MHz) ÷2 1<br>÷2 0 CMU_FM_1<br>HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL] 23<br>MUX_5_DC_0[DIV]<br>1...8 CLKOUT_STANDBY<br>2<br>1<br>0<br>EXTAL FXOSC FXOSC_CLK MC_CGM_MUX5<br>XTAL (8-40 MHz) 25<br>CMU_FC_0 24<br>23<br>22<br>9 MUX_6_DC_0[DIV]<br>19 1...64 CLKOUT_RUN<br>16<br>8<br>2<br>1<br>0<br>MC_CGM_MUX6<br>SIRC SIRC_CLK<br>(32 kHz)<br>CMU_FM_2<br>MC_CGM_MUX10<br>9 MUX_11_DC_0[DIV]<br>8 1...8 TRACE_CLK<br>2<br>1<br>0<br>MC_CGM_MUX11<br>RTC<br>11<br>2323 RTC_CLK<br>RTC.RTCC[CLKSEL]<br>JTAG_TCK/SWD_CLK TCK<br><!-- End of picture text -->

Figure 57. S32K311 clock system diagram 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

749 / 4640 

NXP Semiconductors 

Clocking 

## 23.4 Clock sources 

### 23.4.1 Introduction 

The chip contains the following clock sourcing modules: 

- FIRC 

   - FIRC_CLK is the default system clock source. 

- SIRC 

- PLL 

- FXOSC 

- SXOSC (not available on the S32K311) 

The following list shows some of the clock system features: 

- All clock sources support software configurability for enabling or disabling.<sup>[34]</sup> 

- All clock sources, except SXOSC_CLK, are initialized to their default state on functional reset. 

- The SXOSC_CLK supports RTC applications across functional reset and is reset on destructive reset. 

Only SIRC_CLK and FIRC_CLK are enabled out of reset and are enabled on any functional reset. The other clock sources are disabled on reset. 

#### 23.4.1.1 Chip clock sources 

Table 101. Chip clock sources 

|Clock source|Divider|Default<br>state|Reset|Uses|
|---|---|---|---|---|
|FIRC_CLK<br>(48 MHz)|1, 2, 16|On|POR(enabled on functional and<br>destructive reset)<br>POR assertion - FIRC_CLK<br>disabled asynchronously<br>POR deassertion -<br>FIRC_CLK enabled|• Boot clock<br>• Default system clock source<br>• Safe clock for safety modules FCCU<br>and FOSU<br>• SIUL2 filter clock<br>• MC_RGM clock source|
|PLL_PHIn_CLK<br>(640-1280 MHz)|1...16|Off|Functional (disabled on functional<br>reset)|• Optional system clock source<br>• Communication modules (FlexCAN,<br>EMAC, QuadSPI, and so on)|
|FXOSC_CLK<br>(8-40 MHz)|—|Off|Functional (disabled on functional<br>reset)|• Reference clock source for PLL<br>• Communication modules (FlexCAN,<br>EMAC, QuadSPI, and so on)|
|SXOSC_CLK<br>(32.768 KHz)|—|Off|Destructive (disabled on<br>destructive reset)|• RTC source for operation across<br>functional reset (SXOSC_CLK is not<br>available on the S32K311)|



Table continues on the next page... 

[3] FIRC_CLK and SIRC_CLK cannot be disabled during Run mode. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

750 / 4640 

NXP Semiconductors 

Clocking 

Table 101. Chip clock sources (continued) 

|Clock source|Divider|Default<br>state|Reset|Uses|
|---|---|---|---|---|
|SIRC_CLK<br>(32 KHz)|—|On|POR (enabled on functional reset)|• Safe clock along with FIRC_CLK<br>• SWT clock source<br>• POR_WDG source clock|



### 23.4.2 Chip input clocks 

Table 102. Chip input clocks 

|Pin|Description|
|---|---|
|XTAL|FXOSC crstal ins|
|EXTAL|y p|
|OSC32K_XTAL|SXOSC crstal ins (not available on the S32K311)|
|OSC32K_EXTAL|y p|
|EMAC_MII_RMII_TX_CLK|EMAC transmitter clock/EMAC RMII clock (not availalble on the S32K311 or S32K312)|
|EMAC_MII_RX_CLK|EMAC receiver clock (not availalble on the S32K311 or S32K312)|
|JTAG_TCLK/SWD_CLK|JTAG/SWD clock|
|SAIn_MCLK|SAI_n clock in slave mode (not availalble on the S32K311 or S32K312)|
|SAIn_BCLK|SAI_n bit clock in slave mode (not availalble on the S32K311 or S32K312)|
|LPSPIn_SCK|LPSPIn serial clock in slave mode|
|LPI2Cn_SCL|LPI2C_n clock|
|LPI2Cn_SCLS|LPI2C_n secondary clock|



### 23.4.3 Chip output clocks 

Table 103. Chip output clocks 

|Pin|Description|
|---|---|
|CLKOUT_RUN|Available during Run mode, unavailable during Standby mode|
|CLKOUT_STANDBY|Available during both Run and Standby modes|
|LPSPIn_SCK|LPSPIn serial clock in master mode|
|LPI2Cn_SCL|LPI2C_n clock|
|LPI2Cn_SCLS|LPI2C_n secondary clock|
|EMAC_MII_RMII_MDC|EMAC clock for control data transfer to PHY (not availalble on S32K311 or S32K312)|
|EMAC_MII_RMII_TX_CLK|EMAC transmit clock (not availalble on S32K311 or S32K312)|
|TRACE_ETM_CLKOUT|ETM trace clock (not availalble on S32K311, S32K312, or S32K342)|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

751 / 4640 

NXP Semiconductors 

Clocking 

##### Table 103. Chip output clocks (continued) 

|Pin|Description|
|---|---|
|SAIn_BCLK|SAI_n bit clock in master mode (not availalble on S32K311 or S32K312)|
|QuadSPI_SCKFA|QuadSPI serial clock for serial flash device A (fast) (not availalble on S32K311 or<br>S32K312)|



### 23.4.4 Fast internal RC oscillator (FIRC) 

The chip has an FIRC with the following features: 

- Acts as the system clock source on power-up and after any reset event. 

   - Important to detect FIRC_CLK failure and recovery 

- Acts as the chip's safe clock for safety-relevant applications. 

- Is always enabled in Run mode and can be optionally enabled in Standby mode. 

- Used as clock source for the following: 

   - MC_RGM 

   - FCCU and FOSU 

   - SIUL2 filters 

#### 23.4.4.1 FIRC failure detection 

The FIRC_CLK is the safe clock source used as the FCCU and FOSU clock source. The chip supports FIRC_CLK failure detection and recovery by the mechanisms described in the following cases: 

- Case 1 - FIRC_CLK not used as system clock and goes out of range: 

   - CMU_FM_1 continuously measures the FIRC_CLK clock frequency using FXOSC_CLK as the reference. On each metering window completion, CMU_FM_1 asserts an interrupt (if configured, CMU_FM_1.IER[FMCIE] is 1). You store a configured reference clock count CMU_FM_1.RCCR[REF_CNT] (for example, number of FXOSC_CLK cycles in metering window). Your software checks the FIRC_CLK clock counts by reading CMU_FM_1.SR[MET_CNT]. 

   - In the event FIRC_CLK goes out of range, the software detects the frequency variation after the subsequent metering window by checking CMU_FM_1.SR[MET_CNT] and takes necessary action by either of the recommended options: 

      - SBC-driven power cycle: The SBC receives indication from the chip (through GPIO toggle, QuadSPI communication, and so on). The SBC initiates a power cycle sequence. 

      - ◦Software-driven functional reset: The chip executes a functional reset as configured by your software. 

- Case 2 - FIRC_CLK not used as system clock and fails (becomes stuck): 

   - CMU_FM_1 continuously measures the FIRC_CLK frequency with FXOSC_CLK as the reference. Application software must check FIRC_CLK after a defined time limit by reading CMU_FM_1.SR[MET_CNT] and CMU_FM_1.SR[FMTO]. 

   - If there is an FIRC_CLK failure, the CMU_FM_1 writes a 1 to the timeout status flag CMU_FM_1.SR[FMTO]. 

   - When CMU_FM_1.SR[FMTO] is 1, application software takes necessary action by an SBC-driven power cycle wherein the chip provides an indication to the SBC (through GPIO toggle, QuadSPI communication, and so on). The SBC then initiates a power cycle sequence. 

- Case 3 - FIRC_CLK used as system clock and goes out of range or fails (becomes stuck): 

   - CMU_FC_3, CMU_FC_4, and CMU_FC_5 continuously monitor the system clock nodes with FXOSC_CLK as reference for FLL or FHH events. 

   - In the event of FIRC_CLK failure (when FIRC_CLK acts as the system clock source), these CMUs report the FLL event, acting as a destructive reset source. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

752 / 4640 

NXP Semiconductors 

Clocking 

- The system then undergoes the reset sequence, during which the FIRC_CLK is reinitialized. 

- The MC_RGM.DES fields indicate the source of the reset event. 

- In addition, CMU_FM_1 monitors FIRC_CLK. If the software is not able to service the CMU_FM_1 interrupt before POR_WDG timeout, POR_WDG treats this as a critical FIRC_CLK failure and initiates a POR_WDG recovery. Therefore, you must ensure that, if enabled, the CMU_FM_1 interrupt must be serviced within the POR_WDG timeout duration. 

#### 23.4.4.2 FIRC_CLK behavior in Standby mode 

FIRC_CLK can be optionally enabled in Standby mode by configuring FIRC.STDBY_ENABLE[STDBY_EN]. 

When the PMC acknowledges the Standby mode entry, the FIRC_CLK switches from the On state to the Standby mode configuration selected by the FIRC.STDBY_ENABLE[STDBY_EN] configuration. On wakeup from Standby mode, the FIRC_CLK configuration switches from the Standby mode configured state to the On state. 

~~<mark>NOTE</mark>~~ 

When the trims are being applied, the FIRC will appear as momentarily disabled as shown in Reset timing diagram in the Reset overview chapter. 

### 23.4.5 SIRC 

The chip has a SIRC having the following features: 

- Is always enabled in Run mode and can be optionally enabled in Standby mode. Having the SIRC always enabled improves system robustness by ensuring that a clock is always available for various SWTs when reducing the chip power consumption in Standby mode. 

- Used as clock source for the following: 

   - SWT 

   - POR_WDG 

#### 23.4.5.1 SIRC failure detection 

Like the FIRC_CLK, the SIRC_CLK is a safe clock for the design. The SIRC_CLK is used as clock source for SWTs and POR_WDG and therefore it is important to detect SIRC failure and ensure its recovery. The chip supports SIRC_CLK failure detection and recovery by the mechanism described below. 

- Case 1 - SIRC_CLK goes out of range: 

   - CMU_FM_2 continuously measures the SIRC_CLK clock frequency with FXOSC_CLK as reference. On each metering window completion, the CMU_FM_2 raises an interrupt. The software checks the SIRC clock counts by CMU_FM_2.SR[MET_CNT] with respect to the reference clock counts CMU_FM_2.RCCR[REF_CNT]. 

   - In the event of clock going out of range, the software detects the frequency variation after the subsequent metering window by checking CMU_FM_2.SR[MET_CNT] and takes necessary action by either of the recommended options: 

      1. SBC-driven power cycle. The chip gives an indication to the SBC (through GPIO toggle, QuadSPI communication, and so on.). The SBC then initiates a power cycle sequence. 

      2. SW-driven functional reset. The chip executes a functional reset by software. 

- Case 2 - SIRC_CLK fails (becomes stuck): 

   - CMU_FM_2 continuously measures the SIRC clock frequency with FXOSC_CLK as reference. Software needs to check this reference after a predefined time by checking CMU_FM_2.SR[MET_CNT] and CMU_FM_2.SR[FMTO]. 

   - In the event of SIRC_CLK clock failure, the CMU_FM_2 writes 1 to the timeout status flag field in its status register, namely, CMU_FM_2.SR[FMTO]. 

   - When CMU_FM_2.SR[FMTO] is 1, the software takes necessary action by either of the recommended options: 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

753 / 4640 

NXP Semiconductors 

Clocking 

1. SBC-driven power cycle: The chip gives an indication to the SBC (through GPIO toggle, QuadSPI communication, and so on). The SBC then initiates a power cycle sequence. 

2. Software-driven functional reset: User software executes a functional reset. 

#### 23.4.5.2 SIRC behavior in Standby mode 

SIRC can optionally be enabled in Standby mode by configuring SIRC.MISCELLANEOUS_IN[STANDBY_ENABLE]. 

When PMC acknowledges the Standby mode entry, the SIRC switches from the On state to the standby configuration selected by SIRC.MISCELLANEOUS_IN[STANDBY_ENABLE] configuration. On wake-up from Standby mode, the SIRC configuration switches back from the standby-configured state to the On state. 

~~<mark>NOTE</mark>~~ 

When the trims are being applied, the SIRC will appear as momentarily disabled similar to FIRC, as shown in section Reset timing diagram. 

### 23.4.6 FXOSC 

The chip supports an 8–40 MHz fast crystal oscillator which has following features: 

- Acts as the reference for PLL. 

- Supports crystal input mode and bypass mode if using an external oscillator. 

- Acts as a clock source for communication modules: 

   - FlexCAN 

   - QuadSPI<sup>[35]</sup> 

   - EMAC (EMAC_CLK_TS)<sup>[35]</sup> 

### 23.4.7 SXOSC 

The chip supports a slow crystal oscillator (SXOSC) which has the following features (not available on the S32K311): 

- Supports crystal input mode and bypass mode. 

- Acts as a clock source for RTC. As SXOSC is not affected by functional reset, it supports RTC operation across functional reset. SXOSC is only reset on destructive reset. 

### 23.4.8 PLL 

The chip contains up to two PLL to provide precision clock source with the following features: 

- Optional system clock source (in high performance applications) 

- System clock source in safety applications 

- Can be used as clock source for communication modules, when configured as system clock source: 

   - FlexCAN (in SYNC mode operation) 

   - EMAC (not available on S32K311 or S32K312) 

   - QuadSPI (not available on S32K311 or S32K312) 

   - LPSPI 

   - LPI2C 

   - FlexIO 

- [4] Not present in K311 & K312. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

754 / 4640 

NXP Semiconductors 

Clocking 

##### — LPUART 

- Supports frequency modulation 

- Contains lock status monitoring logic which supports loss-of-lock indication 

In case of a loss of lock after lock has been acquired, the Second PLL will generate a loss of lock flag. At Power-Up, the Second PLL shall be disabled. It will be up to the application software to enable it when needed. The default reaction of loss of lock flag from the Second PLL will be an interrupt. The reaction of a loss of lock from the Second PLL will be optionally configured as a functional reset, controlled by GPR. 

The Second PLL supports a clock output frequency of up to 250MHz (nominal), for the FXOSC input frequencies. 

~~<mark>NOTE</mark>~~ 

See PLL Digital Interface (PLLDIG) for PLL configuration details. See the S32K3xx Data Sheet for PLL limitations. 

#### 23.4.8.1 PLL configurations 

The PLL output predivider frequency depends on the PLLDIG.PLLDV[RDIV] and PLLDIG.PLLDV[MFI] configurations. The PLL VCO clock can be divided further by configuring PLLDIG.PLLODIV_0[DIV] for PLL_PHI0_CLK and PLLDIG_PLLODIV_1[DIV] for PLL_PHI1_CLK (see the PLL Digital Interface (PLLDIG) chapter for configuration details). 

#### 23.4.8.1.1 PLL configuration sequence 

Before enabling the PLL, you must enable FXOSC_CLK and wait until it is stable. FXOSC.STAT[OSC_STAT] must be monitored to determine the FXOSC_CLK status. 

To disable the PLL, the software must disable PLL first and only then disable FXOSC (if required). 

### 23.4.9 Chip clock outputs 

The chip supports two CLKOUT_x pins for allowing viewing of some internal clocks as follows: 

- CLKOUT_STANDBY 

   - Used for showing clocks available in Run and Standby modes. 

- CLKOUT_RUN 

   - Used for showing only Run mode clocks. 

See the Clockout overview section and the Clock Generation Module (MC_CGM) chapter for details on available clocks and configuration. 

~~<mark>NOTE</mark>~~ 

The CLKOUT_STANDBY registers are latched when the chip enters Standby mode and are reset in Standby mode sequence. Therefore, the CLKOUT_STANDBY signal needs to be reconfigured on Standby mode exit. 

~~<mark>NOTE</mark>~~ 

CLKOUT_STANDBY is available on two pads GPIO[12] and GPIO[138] but CLKOUT across functional reset and standby is supported only on GPIO[12] and OBE(output buffer enable) is controlled by DCM GPR bit. Please refer to DCMRWP1[3] bit for detail. 

## 23.5 MC_CGM 

The MC_CGM controls the clock functionality of the chip. See the Clock Generation Module (MC_CGM) chapter for details on MC_CGM clocking controls. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

755 / 4640 

NXP Semiconductors 

Clocking 

### 23.5.1 MC_CGM clock multiplexer types 

In this chip, CLKOUT_RUN, CLKOUT_STANDBY, and TRACE_CLK multiplexers are software-controlled multiplexers. The rest are hardware-controlled multiplexers (see the Clock Generation Module (MC_CGM) chapter for details on software and hardware multiplexers). 

### 23.5.2 MC_CGM clock multiplexers for S32K311 and S32K312 

Table 104. MC_CGM clock multiplexers for S32K311 and S32K312 

|Clock mux|Register description|Source inputs<sup>1</sup>|Register|Selector<br>output|Divider output|
|---|---|---|---|---|---|
||Select Control|FIRC_CLK|MUX_0_CSC|||
||Select Status|PLL_PHI0_CLK|MUX_0_CSS||—|
||Divider 0 Control||MUX_0_DC_0||CORE_CLK|
|Clock mux 0|Divider 1 Control||MUX_0_DC_1|—|AIPS_PLAT_CLK|
||Divider 2 Control|—|MUX_0_DC_2||AIPS_SLOW_CLK|
||Divider 3 Control||MUX_0_DC_3||HSE_CLK|
||Divider 4 Control||MUX_0_DC_4||DCM_CLK|
||Select Control|FIRC_CLK|MUX_3_CSC|||
|Clock mux 3|Select Status|FXOSC_CLK<br>AIPS_PLAT_CLK|MUX_3_CSS|—|—|
||Divider 0 Control|—|MUX_3_DC_0||FLEXCAN0_PE_CLK<br>FLEXCAN1_PE_CLK<br>FLEXCAN2_PE_CLK|
||Select Control|FIRC_CLK|MUX_4_CSC|||
|Clock mux 4<sup>2</sup>|Select Status|FXOSC_CLK<br>AIPS_PLAT_CLK|MUX_4_CSS|—|—|
||Divider 0 Control|—|MUX_4_DC_0||FLEXCAN3_PE_CLK<br>FLEXCAN4_PE_CLK<br>FLEXCAN5_PE_CLK|
||Select Control|FIRC_CLK|MUX_5_CSC|||
|Clock mux 5<sup>3</sup>|Select Status|SIRC_CLK<br>FXOSC_CLK<br>SXOSC_CLK<br>AIPS_SLOW_CLK|MUX_5_CSS|—|—|
||Divider 0 Control|—|MUX_5_DC_0||CLKOUT_STANDBY|
||Select Control|FIRC_CLK|MUX_6_CSC|||
|||SIRC_CLK||||
|Clock mux 6<sup>4</sup>|Select Status|FXOSC_CLK<br>SXOSC_CLK<br>PLL_PHI0_CLK|MUX_6_CSS|—|—|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

756 / 4640 

NXP Semiconductors 

Clocking 

Table 104. MC_CGM clock multiplexers for S32K311 and S32K312 (continued) 

|Clock mux|Register description|Source inputs<sup>1</sup>|Register|Selector<br>output|Divider output|
|---|---|---|---|---|---|
|||PLL_PHI1_CLK<br>CORE_CLK<br>HSE_CLK<br>AIPS_PLAT_CLK<br>AIPS_SLOW_CLK<br>EMAC_RMII_TX_CLK<br>EMAC_RX_CLK||||
||Divider 0 Control|—|MUX_6_DC_0||CLKOUT_RUN|
||Select Control|FIRC_CLK|MUX_11_CSC|||
|Clock mux 11|Select Status|FXOSC_CLK<br>PLL_PHI0_CLK<br>PLL_PHI1_CLK|MUX_11_CSS|—|—|
||Divider 0 Control|—|MUX_11_DC_0||TRACE_CLK|



1. The default clock selected for all clock mux selectors is FIRC_CLK (out of reset). 

2. Clock mux 4 and FLEXCAN[3:5]_PE_CLK are not available on the S32K311. 

3. SXOSC as source for clock mux 5 is not available on the S32K311. 

4. SXOSC as source for clock mux 6 is not available on the S32K311. 

### 23.5.3 MC_CGM clock multiplexers (excluding S32K311 and S32K312) 

Table 105. MC_CGM clock multiplexers (excluding S32K311 and S32K312) 

|Clock mux|Register description|Source inputs<sup>1</sup>|Register|Selector<br>output|Divider output|
|---|---|---|---|---|---|
||Select Control|FIRC_CLK|MUX_0_CSC|||
||Select Status|PLL_PHI0_CLK|MUX_0_CSS||—|
||Divider 0 Control||MUX_0_DC_0||CORE_CLK|
||Divider 1 Control||MUX_0_DC_1||AIPS_PLAT_CLK|
|Clock mux 0|Divider 2 Control||MUX_0_DC_2|—|AIPS_SLOW_CLK|
||Divider 3 Control|—|MUX_0_DC_3||HSE_CLK|
||Divider 4 Control||MUX_0_DC_4||DCM_CLK|
||Divider 5 Control||MUX_0_DC_5||LBIST_CLK|
||Divider 6 Control||MUX_0_DC_6||QSPI_MEM_CLK|
||Select Control|FIRC_CLK|MUX_1_CSC|||
|Clock mux 1|Select Status|FXOSC_CLK<br>AIPS_PLAT_CLK|MUX_1_CSS|—|—|
||Divider 0 Control|—|MUX_1_DC_0||STM0_CLK|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

757 / 4640 

NXP Semiconductors 

Clocking 

Table 105. MC_CGM clock multiplexers (excluding S32K311 and S32K312) (continued) 

|Clock mux|Register description|Source inputs<sup>1</sup>|Register|Selector<br>output|Divider output|
|---|---|---|---|---|---|
||Select Control|FIRC_CLK|MUX_2_CSC|||
|Clock mux 2|Select Status|FXOSC_CLK<br>AIPS_PLAT_CLK|MUX_2_CSS|—|—|
||Divider 0 Control|—|MUX_2_DC_0||STM1_CLK<sup>2</sup>|
||Select Control|FIRC_CLK|MUX_3_CSC|||
|Clock mux 3|Select Status|FXOSC_CLK<br>AIPS_PLAT_CLK<br>CORE_CLK<sup>3</sup>|MUX_3_CSS|—|—|
||Divider 0 Control|—|MUX_3_DC_0||FLEXCAN0_PE_CLK<br>FLEXCAN1_PE_CLK<br>FLEXCAN2_PE_CLK|
||Select Control|FIRC_CLK|MUX_4_CSC|||
||Select Status|FXOSC_CLK<br>AIPS_PLAT_CLK<br>CORE_CLK<sup>3</sup>|MUX_4_CSS||—|
|Clock mux 4|Divider 0 Control|—|MUX_4_DC_0|—|FLEXCAN3_PE_CLK<br>FLEXCAN4_PE_CLK<sup>4</sup><br>FLEXCAN5_PE_CLK<sup>4</sup><br>FLEXCAN6_PE_CLK<sup>3</sup><br>FLEXCAN7_PE_CLK<sup>3</sup>|
||Select Control|FIRC_CLK|MUX_5_CSC|||
|Clock mux 5|Select Status|SIRC_CLK<br>FXOSC_CLK<br>SXOSC_CLK<br>AIPS_SLOW_CLK|MUX_5_CSS|—|—|
||Divider 0 Control|—|MUX_5_DC_0||CLKOUT_STANDBY|
||Select Control|FIRC_CLK|MUX_6_CSC|||
|Clock mux 6|Select Status|SIRC_CLK<br>FXOSC_CLK<br>SXOSC_CLK<br>PLL_PHI0_CLK<br>PLL_PHI1_CLK<br>PLL_AUX_PHI0_CLK<sup>3</sup><br>PLL_AUX_PHI1_CLK<sup>3</sup><br>PLL_AUX_PHI2_CLK<sup>3</sup><br>CORE_CLK<br>HSE_CLK<br>AIPS_PLAT_CLK<br>AIPS_SLOW_CLK|MUX_6_CSS|—|—|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

758 / 4640 

NXP Semiconductors 

Clocking 

Table 105. MC_CGM clock multiplexers (excluding S32K311 and S32K312) (continued) 

|Clock mux|Register description|Source inputs<sup>1</sup>|Register|Selector<br>output|Divider output|
|---|---|---|---|---|---|
|||EMAC_RMII_TX_CLK<br>EMAC_RX_CLK||||
||Divider 0 Control|—|MUX_6_DC_0||CLKOUT_RUN|
||Select Control|FIRC_CLK|MUX_7_CSC|||
|Clock mux 7|Select Status|EMAC_RMII_MII_TX_<br>CLK (pin)<br>EMAC_RX_CLK (pin)|MUX_7_CSS|—|—|
||Divider 0 Control|—|MUX_7_DC_0||EMAC_RX_CLK|
||Select Control|FIRC_CLK|MUX_8_CSC|||
|Clock mux 8|Select Status|EMAC_RMII_MII_TX_<br>CLK (pin)|MUX_8_CSS|—|—|
||Divider 0 Control|—|MUX_8_DC_0||EMAC_TX_CLK|
||Select Control|FIRC_CLK|MUX_9_CSC|||
|Clock mux 9|Select Status|EMAC_RMII_MII_TX_<br>CLK (pin)<br>EMAC_RX_CLK (pin)|MUX_9_CSS|—|—|
||Divider 0 Control|—|MUX_9_DC_0||EMAC_TS_CLK|
||Select Control|FIRC_CLK|MUX_10_CSC|||
|Clock mux 10|Select Status|FXOSC_CLK<br>PLL_PHI0_CLK<br>PLL_PHI1_CLK<br>PLL_AUX_PHI0_CLK<sup>3</sup><br>EMAC_RMII_MII_TX_<br>CLK (pin)<br>EMAC_RX_CLK (pin)|MUX_10_CSS|—|—|
||Divider 0 Control|—|MUX_10_DC_0||QSPI_SFCK|
||Select Control|FIRC_CLK<br>FXOSC_CLK|MUX_11_CSC||—|
|Clock mux 11|Select Status|PLL_PHI0_CLK<br>PLL_PHI1_CLK|MUX_11_CSS|—||
||Divider 0 Control|—|MUX_11_DC_0||TRACE_CLK|
||Select Control|AIPS_PLAT_CLK|MUX_13_CSC|||
|||FXOSC_CLK|||—|
|Clock mux 13<sup>3</sup>|Select Status|FIRC_CLK|MUX_13_CSS|—||
||Divider 0 Control|—|MUX_13_DC_0||STM2_CLK|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

759 / 4640 

NXP Semiconductors 

Clocking 

Table 105. MC_CGM clock multiplexers (excluding S32K311 and S32K312) (continued) 

|Clock mux|Register description|Source inputs<sup>1</sup>|Register|Selector<br>output|Divider output|
|---|---|---|---|---|---|
||Select Control|FIRC_CLK|MUX_14_CSC|||
|Clock mux 14<sup>3</sup>|Select Status|FXOSC_CLK<br>PLL_AUX_PHI0_CLK<br>PLL_AUX_PHI1_CLK|MUX_14_CSS|—|—|
||Divider 0 Control|—|MUX_14_DC_0||uSDHC_PER_CLK|



1. The default clock selected for all clock mux selectors is FIRC_CLK (out of reset). 

2. STM1_CLK is not available on the S32K314. 

3. For S32K358 only. 

4. FLEXCAN[4:5]_PE_CLK are not available on the S32K322 and S32K342. 

### 23.5.4 MC_CGM clock sources mapping 

Table 106. MC_CGM clock sources mapping 

|Clock selector index<sup>1</sup>|MC_CGM clock source|Clock source|
|---|---|---|
|0|clk_src_0|FIRC_CLK|
|1|clk_src_1|SIRC_CLK|
|2|clk_src_2|FXOSC_CLK|
|3|Reserved|Reserved|
|4|clk_src_4|SXOSC_CLK<sup>2</sup>|
|5–7|Reserved|Reserved|
|8|clk_src_8|PLL_PHI0_CLK|
|9|clk_src_9|PLL_PHI1_CLK|
|10–11|Reserved|Reserved|
|12|clk_src_12|PLL_AUX_PHI0_CLK<sup>3</sup>|
|13|clk_src_13|PLL_AUX_PHI1_CLK<sup>3</sup>|
|14|clk_src_14|PLL_AUX_PHI2_CLK<sup>3</sup>|
|15|Reserved|Reserved|
|16|clk_src_16|CORE_CLK|
|17–18|Reserved|Reserved|
|19|clk_src_19|HSE_CLK|
|20–21|Reserved|Reserved|
|22|clk_src_22|AIPS_PLAT_CLK|
|23|clk_src_23|AIPS_SLOW_CLK|
|24|clk_src_24|EMAC_RMII_TX_CLK<sup>4</sup>|
|25|clk_src_25|EMAC_RX_CLK<sup>4</sup>|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

760 / 4640 

NXP Semiconductors 

Clocking 

Table 106. MC_CGM clock sources mapping (continued) 

|Clock selector index<sup>1</sup>|MC_CGM clock source|Clock source|
|---|---|---|
|26–49|Reserved|Reserved|
|50|clk_src_50|CLKOUT_RUN|



1. All clock selector indexes not shown are reserved. 

2. SXOSC_CLK is not available on the S32K311. 

3. PLL_AUX_PHIn_CLK is available in S32K358 only. 

4. EMAC_RMII_TX_CLK and EMAC_RX_CLK are not available on the S32K311 or S32K312. 

## 23.6 Peripheral clocking 

The module clocking diagrams for the peripherals are shown in the following subsections (see Peripheral clock gating for peripheral clock gating possibilities). 

### 23.6.1 Module clocking 

The following sections show how the chip modules use MODULE_CLK and REG_INTF_CLK to control their functionality. 

#### 23.6.1.1 Communication modules 

Figure 58 shows the REG_INTF_CLK and MODULE_CLK connections, and Table 107 shows the REG_INTF_CLK and MODULE_CLK signals used by these modules. Any module diagram that does not explicitly show a REG_INTF_CLK uses the same source for REG_INTF_CLK as used by MODULE_CLK. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0761-14.png)


<!-- Start of picture text -->
Module<br>See REG_INTF_CLK<br>REG_INTF_CLK<br>and MODULE_CLK<br>columns in table below } MODULE_CLK<br><!-- End of picture text -->

Figure 58. Communication module clocks 

Table 107. Communication module clocking 

|Module|MODULE_CLK|REG_INTF_CLK|
|---|---|---|
|LPSPI|SeeLPSPIn clocking.||
|LPI<sup>2</sup>C|SeeLPI2C_n clocking.||
|FlexIO|SeeFlexIO clocking.||
|FlexCAN|SeeFlexCAN_n clocking.||
|SAI|SeeSAI_n clocking.||
|EMAC|SeeEMAC clocking.||
|LPUART_[0,8]|AIPS_PLAT_CLK|AIPS_PLAT_CLK|
|LPUART_[1:7,9:15]|AIPS_SLOW_CLK|AIPS_SLOW_CLK|
|QuadSPI|SeeQuadSPI clocking.||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

761 / 4640 

NXP Semiconductors 

Clocking 

#### 23.6.1.1.1 FlexCAN_n clocking 

The figure below shows the FlexCAN_n clocking. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0762-04.png)


<!-- Start of picture text -->
FlexCAN_[0... n ]<br>AIPS_PLAT_CLK MODULE_CLK<br>REG_INTF_CLK<br>CAN_CHI_CLK<br>FLEXCAN_ n n _PE_CLK CAN_PE_CLK<br><!-- End of picture text -->

Figure 59. FlexCAN_n clocking 

FlexCAN has the following unique clocks: 

- CAN_CHI_CLK—FlexCAN controller host interface clock 

- CAN_PE_CLK—FlexCAN protocol engine clock 

FlexCAN supports up to an 8 Mbps data rate using a 40 MHz CAN_PE_CLK. With a 16 MHz crystal source, 3.2 Mbps is achievable for baud rate calculations (see the section Protocol timing in the "CAN (FlexCAN)" chapter for details). 

For S32K312, the maximum data rate supported in FlexCAN_0 instance is 5.7 Mbps. 

~~<mark>NOTE</mark>~~ 

See Feature comparison for details on this module's availability on your chip variant. 

#### 23.6.1.1.1.1 FlexCAN timestamp implementation 

The following figure shows the FlexCAN timestamping implementation. The related table shows the timestamp sources and corresponding clock nodes. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0762-15.png)


<!-- Start of picture text -->
TS0_CNT_IN<br>TS0_CLK TS_CNT_OUT<br>TS1_CNT_IN<br>TS1_CLK<br>TS_OUT_CLK_SEL D Q D Q<br>DCM.DCMRWF1[0] clk clk<br>TS_OUT_CLK<br><!-- End of picture text -->

Figure 60. FlexCAN timestamping 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

762 / 4640 

NXP Semiconductors 

Clocking 

Table 108. Timestamp sources and clock nodes 

|Timestamp|Module|TS clock domain|
|---|---|---|
|TS0_CLK|EMAC|TS0_CLK—EMAC_TS_CLK|
|TS1_CLK|STM0|TS1_CLK—AIPS_PLAT_CLK|
|TS_OUT_CLK|FlexCAN_n|TS_OUT_CLK—EMAC_TS_CLK|



~~<mark>NOTE</mark>~~ 

The timestamp clock (TS_OUT_CLK, EMAC_TS_CLK for S32K3xx) must be greater than or equal to FLEXCAN_n_PE_CLK. When using STM0 as the timestamp source, the FlexCAN timestamp clock (TS_OUT_CLK, EMAC_TS_CLK for S32K3xx) must be greater than or equal to STM0_CLK. 

#### 23.6.1.1.2 LPI2C_n clocking 

The following figure shows LPI2C_n clocking, and the related table shows the LPI2C SIUL2 configuration. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0763-08.png)


<!-- Start of picture text -->
LPI2C_ n<br>AIPS_SLOW_CLK MODULE_CLK<br>REG_INTF_CLK<br>LPI2C_CLK<br>Port SIUL2_IMCR b [SSS]<br>SIUL2_MSCR a [IBE]<br>SCL<br>LPI2C n _SCL<br>SIUL2_MSCR a [OBE]<br>SIUL2_MSCR a [SSS]<br><!-- End of picture text -->

Figure 61. LPI2C clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0763-10.png)


<!-- Start of picture text -->
  NOTE<br><!-- End of picture text -->

See Feature comparison for details on this module's availability on your chip variant. 

Table 109. SIUL2 options for LPI2Cn_SCL clock 

|I<sup>2</sup>C_n signal|I<sup>2</sup>C<br>mode|I/O signal|Port|MSCRa|<br>OBE|MSCR field<br>IBE|s<br>SSS|IMCRb|IMCR[SSS]|
|---|---|---|---|---|---|---|---|---|---|
||Slave||PTC8|72|0|1|X||0001b|
|I2C0SCL|Master|LPI2C0SCL|||1|0|001b|212|X|
|__|Slave|_|PTD14|110|0|1|X||0010b|
||Master||||1|0|100b||X|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

763 / 4640 

NXP Semiconductors 

Clocking 

Table 109. SIUL2 options for LPI2Cn_SCL clock (continued) 

|I<sup>2</sup>C_n signal|I<sup>2</sup>C<br>|I/O signal|Port|MSCRa||MSCR field|s|IMCRb|IMCR[SSS]|
|---|---|---|---|---|---|---|---|---|---|
||mode||||OBE|IBE|SSS|||
||Slave||PTF20<sup>1</sup>|180|0|1|X||0011b|
||Master||||1|0|100b||X|
|I2C_0_SCL|Slave|LPI2C0SCLS|PTB1|33|0|1|X|213|0001b|
|S|Master|_|||1|0|001b||X|
||Slave||PTC7|71|0|1|X||0001b|
||Master||||1|0|011b||X|
||Slave||PTC15|79|0|1|X||0110b|
||Master||||1|0|111b||X|
|I2C1SCL|Slave|LPI2C1SCL|PTC28|92|0|1|X|217|0100b|
|__|Master|_|||1|0|101b||X|
||Slave||PTD9|105|0|1|X||0010b|
||Master||||1|0|010b||X|
||Slave||PTF7<sup>2</sup>|167|0|1|X||0101b|
||Master||||1|0|011b||X|
|I2C_1_SCL|Slave|LPI2C1SCLS|PTC17|81|0|1|X|218|0010b|
|S|Master|_|||1|0|100b||X|



> 1. PTF20 pad is not present in K311, K312 and K342. 

2. PTF7 pad is not present in K311, K312 and K342. 

#### 23.6.1.1.3 I3C_0 clocking 

The following figure shows I3C_0 clocking, and the related table shows the I3C_0 SIUL2 configuration. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

764 / 4640 

NXP Semiconductors 

Clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0765-02.png)


<!-- Start of picture text -->
FCLK* 1<br>I3C_CLK I3C<br>Reserved 0<br>~PCTL & DCM GPR bit (default: 0)<br>AIPS_SLOW_CLK MODULE_CLK<br>REG_INTF_CLK<br>Port SIUL2_IMCR b [SSS]<br>SIUL2_MSCR a [IBE]<br>I3C0_SCL<br>SCL<br>I3C0_SCL<br>SIUL2_MSCR a [OBE]<br>SIUL2_MSCR a [SSS]<br>* For S32K358, FCLK is AIPS_PLAT_CLK.<br>  For S32K311, S32K312 and S32K342, FCLK is CORE_CLK.<br><!-- End of picture text -->

Figure 62. I3C_0 clocking 

The I3C module FCLK is clocked by one of the following options, defined by a GPR bit: 

1. AIPS_PLAT_CLK 

2. CORE_CLK 

Table 110. SIUL2 options for I3C0_SCL clock 

|I<sup>3</sup>C_n signal|I<sup>3</sup>C<br>|I/O signal|Port|MSCRa||MSCR fiel|ds|IMCRb|IMCR[SSS]|
|---|---|---|---|---|---|---|---|---|---|
||mode||||OBE|IBE|SSS|||
||Slave||PTC16|80|0|1|X||0010b|
||Master||||1|0|0101b||X|
|I3C0SCL|Slave|I3C0SCL|PTD9|105|0|1|X|371|0001b|
|_<br>|Master|_|||1|0|0101b||X|
||Slave||PTC28<sup>1</sup>|92|0|1|X||0011b|
||Master||||1|0|0111b||X|



1. PTC28 is not available on the S32K311. 

Table 111. I3C baud rate calculation 

|Chip|CORE_CLK/<br>FCLK|Internal divider in I3C|Duration of first half of SCL|Baud rate (SDR|
|---|---|---|---|---|
|K312/K311/K358|120 MHz|Divide by 5 (PPBAUD = 4)|41.66 ns (1/24mbps)|12.00 mbps|
|K342|160 MHz|Divide by 7 (PPBAUD = 6)|43.75 ns (1/22.86mbps)|11.43 mbps|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

765 / 4640 

NXP Semiconductors 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0766-01.png)


<!-- Start of picture text -->
Clocking<br><!-- End of picture text -->

#### 23.6.1.1.4 EMAC clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0766-03.png)


<!-- Start of picture text -->
MC_CGM EMAC<br>RMII_CLK<br>SIUL2 MUX_7_CSC[SELCTL]<br>MUX_7_DC_0[DIV]<br>25<br>EMAC_RX_CLK<br>24 1...64 RX_CLK<br>IMCR300[SSS] 0<br>AIPS_PLAT_CLK CSR_CLK<br>EMAC_MII_RX_CLK<br>MUX_8_DC_0[DIV]<br>24<br>EMAC_TX_CLK<br>IMCR296[SSS] 1...64 TX_CLK<br>0<br>EMAC_RMII_MII_TX_CLK MUX_8_CSC[SELCTL]<br>25 MUX_9_DC_0[DIV]<br>24 EMAC_TS_CLK<br>PLL_PHI0_CLK 8 1...64 TS_CLK<br>FXOSC_CLK 2<br>FIRC_CLK 0<br>MUX_9_CSC[SELCTL]<br>Figure 63. EMAC clocking<br><!-- End of picture text -->

~~<mark>NOTE</mark>~~ 

EMAC operates only in Clock options A and B, since the module clock becomes lower than the protocol clock (RMII/MII clocks) in other modes. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0766-06.png)


<!-- Start of picture text -->
  NOTE<br><!-- End of picture text -->

See Feature comparison for details on this module's availability on your chip variant. 

PLL_AUX should operate in integer mode to meet the RGMII clock accuracy requirements. 

PLL_AUX will be a clock source for the GMAC TX and TS clocks, to support 1 GBps Ethernet operation. 

#### 23.6.1.1.4.1 EMAC RMII clocking 

The following table shows the EMAC RMII clocking, and the related table shows the SIUL2 clock signal configuration for RMII. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

766 / 4640 

NXP Semiconductors 

Clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0767-02.png)


<!-- Start of picture text -->
MC_CGM EMAC<br>RMII_CLK<br>SIUL2 MUX_7_CSC[SELCTL]<br>MUX_7_DC_0[DIV]<br>EMAC_RX_CLK<br>24 1...64 RX_CLK<br>IMCR300[SSS]<br>AIPS_PLAT_CLK CSR_CLK<br>EMAC_MII_RX_CLK<br>MUX_8_DC_0[DIV]<br>24<br>EMAC_TX_CLK<br>IMCR296[SSS] 1...64 TX_CLK<br>EMAC_RMII_MII_TX_CLK MUX_8_CSC[SELCTL]<br>25 MUX_9_DC_0[DIV]<br>24 EMAC_TS_CLK<br>PLL_PHI0_CLK 8 1...64 TS_CLK<br>FXOSC_CLK 2<br>FIRC_CLK 0<br>MUX_9_CSC[SELCTL]<br><!-- End of picture text -->

Figure 64. EMAC RMII clocking 

##### Table 112. EMAC RMII clock configuration 

|||||||SIUL2|||
|---|---|---|---|---|---|---|---|---|
|Source clock|Destination clock|Port|MSCRa|MS|CR fiel|ds|IMCRb|IMCR[SSS]|
|||||OBE|IBE|SSS|||
||EMAC_RX_CLK<br>EMAC_TX_CLK|PTC0|64|0|1|X||0100b|
|EMACRMIIMIITXCLK|EMAC_TX_CLK<br>EMAC_RX_CLK|PTD6|102|0|1|X|296|0010b|
|____|EMAC_TX_CLK<br>EMAC_RX_CLK|PTD11|107|0|1|X||0001b|
||EMAC_TX_CLK<br>EMAC_RX_CLK|PTD12|108|0|1|X||0011b|
|||PTC0|64|0|1|X||0100b|
|EMAC_RMII_MII_TX_CLK<br>MCCGMMUX9CSCS|EMACTSCLK|PTD6|102|0|1|X|296|0010b|
|(_.__[<br>ELCTL] = 18h)|__|PTD11|107|0|1|X||0001b|
|||PTD12|108|0|1|X||0011b|
|EMAC_MII_RX_CLK||PTC1|65|0|1|X||0011b|
|(MC_CGM.MUX_9_CSC[S|EMAC_TS_CLK|PTD5|101|0|1|X|300|0010b|
|ELCTL] = 19h)||PTD10|106|0|1|X||0001b|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

767 / 4640 

NXP Semiconductors 

Clocking 

~~<mark>NOTE</mark>~~ 

The EMAC time-stamp clock (EMAC_TS_CLK) can use either of the source clocks show in the table above, but can also select other clocks as selected in MC_CGM.MUX_9_CSC[SELCTL]. 

#### 23.6.1.1.4.2 EMAC MII clocking 

The following figure shows the EMAC MII clocking, and the related table shows the SIUL2 clock signal configuration for MII. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0768-06.png)


<!-- Start of picture text -->
MC_CGM EMAC<br>RMII_CLK<br>SIUL2 MUX_7_CSC[SELCTL]<br>MUX_7_DC_0[DIV]<br>25<br>EMAC_RX_CLK<br>1...64 RX_CLK<br>IMCR300[SSS]<br>AIPS_PLAT_CLK CSR_CLK<br>EMAC_MII_RX_CLK<br>MUX_8_DC_0[DIV]<br>24<br>EMAC_TX_CLK<br>IMCR296[SSS] 1...64 TX_CLK<br>EMAC_RMII_MII_TX_CLK MUX_8_CSC[SELCTL]<br>25 MUX_9_DC_0[DIV]<br>24 EMAC_TS_CLK<br>PLL_PHI0_CLK 8 1...64 TS_CLK<br>FXOSC_CLK 2<br>FIRC_CLK 0<br>MUX_9_CSC[SELCTL]<br><!-- End of picture text -->

Figure 65. EMAC MII clocking 

Table 113. SIUL2 EMAC MII clock configuration 

|||||||SIUL2|||
|---|---|---|---|---|---|---|---|---|
|Source clock|Destination|Port|MSCRa|MS|CR fie|lds|IMCRb|IMCR[SSS]|
|||||OBE|IBE|SSS|||
|||PTC0|64|0|1|X||0100b|
|EMACRMIIMIITXCLK|EMACTXCLK|PTD6|102|0|1|X|296|0010b|
|____|__|PTD11|107|0|1|X||0001b|
|||PTD12|108|0|1|X||0011b|
|||PTC1|65|0|1|X||0011b|
|EMAC_MII_RX_CLK|EMAC_RX_CLK|PTD5|101|0|1|X|300|0010b|
|||PTD10|106|0|1|X||0001b|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

768 / 4640 

NXP Semiconductors 

Clocking 

##### Table 113. SIUL2 EMAC MII clock configuration (continued) 

|||||||SIUL2|||
|---|---|---|---|---|---|---|---|---|
|Source clock|Destination|Port|MSCRa|MS|CR fiel|ds|IMCRb|IMCR[SSS]|
|||||OBE|IBE|SSS|||
|||PTC0|64|0|1|X||0100b|
|EMAC_RMII_MII_TX_CLK<br>MCCGMMUX9CSCS|EMACTSCLK|PTD6|102|0|1|X|296|0010b|
|(_.__[<br>ELCTL] = 18h)|__|PTD11|107|0|1|X||0001b|
|||PTD12|108|0|1|X||0011b|
|EMACMIIRXCLK||PTC1|65|0|1|X||0011b|
|___<br>(MC_CGM.MUX_9_CSC[S<br>|EMAC_TS_CLK|PTD5|101|0|1|X|300|0010b|
|ELCTL] = 19h)||PTD10|106|0|1|X||0001b|



###### ~~<mark>NOTE</mark>~~ 

The EMAC time-stamp clock (EMAC_TS_CLK) can use any of the signals shown in the figure above which includes either EMAC_RX_CLK or EMAC_RMII_MII_TX_CLK source clocks. MC_CGM.MUX_9_CSC[SELCTL] selects the specific source clock for EMAC_TS_CLK. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

769 / 4640 

NXP Semiconductors 

Clocking 

#### 23.6.1.1.5 LPSPIn clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0770-03.png)


<!-- Start of picture text -->
LPSPI0<br>AIPS_PLAT_CLK MODULE_CLK<br>REG_INTF_CLK<br>Port SIUL2_IMCR b [SSS] LPSPI_CLK<br>SIUL2_MSCR a [IBE]<br>LPSPI0_SCK SCK<br>SIUL2_MSCR a [OBE]<br>SIUL2_MSCR a [SSS]<br>LPSPI[1...5]<br>AIPS_SLOW_CLK MODULE_CLK<br>REG_INTF_CLK<br>Port SIUL2_IMCR b [SSS] LPSPI_CLK<br>SIUL2_MSCR a [IBE]<br>LPSPI n _SCK SCK<br>SIUL2_MSCR a [OBE]<br>SIUL2_MSCR a [SSS]<br>Figure 66. LPSPIn clocking<br><!-- End of picture text -->


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0770-04.png)


<!-- Start of picture text -->
  NOTE<br><!-- End of picture text -->

See Feature comparison for details on this module's availability on your chip variant. 

Table 114. SIUL2 options for LPSPIn SCK 

|Source|Destination|SPI|Port|MSCR a||MSCR fiel|ds|IMCR b|IMCR[SSS]|
|---|---|---|---|---|---|---|---|---|---|
|||mode|||OBE|IBE|SSS|||
|||Slave|PTC8|72|0|1|X||0001b|
|LPSPI0_SCK|LPSPI0 SCK|Master|||1|0|0110b|229|X|
|||Slave|PTD11|107|0|1|X||0101b|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

770 / 4640 

NXP Semiconductors 

Clocking 

Table 114. SIUL2 options for LPSPIn SCK (continued) 

|Source|Destination|SPI<br>mode|Port|MSCR a|OBE|MSCR fiel<br>IBE|ds<br>SSS|IMCR b|IMCR[SSS]|
|---|---|---|---|---|---|---|---|---|---|
|||Master|||1|0|0110b||X|
|||Slave|PTD15|111|0|1|X||0011b|
|||Master|||1|0|0100b||X|
|||Slave|PTE1|129|0|1|X||0010b|
|||Master|||1|0|0010b||X|
|||Slave|PTA3|3|0|1|X||0001b|
|||Master|||1|0|0011b||X|
|||Slave|PTA19|19|0|1|X||0011b|
|LPSPI1SCK|LPSPI1 SCK|Master|||1|0|0100b|238|X|
|_||Slave|PTA28|28|0|1|X||0100b|
|||Master|||1|0|0011b||X|
|||Slave|PTB14|46|0|1|X||0010b|
|||Master|||1|0|0011b||X|
|||Slave|PTB29|61|0|1|X||0011b|
|||Master|||1|0|0101b||X|
|||Slave|PTC15|79|0|1|X||0010b|
|LPSPI2SCK|LPSPI2 SCK|Master|||1|0|0011b|245|X|
|_||Slave|PTE15|143|0|1|X||0001b|
|||Master|||1|0|0011b||X|
|||Slave|PTF0|160|0|1|X||0100b|
|||Master|||1|0|011b||X|
|||Slave|PTC1|1|0|1|X||0011b|
|||Master|7|8|1|0|0001b||X|
|||Slave|||0|1|X||0001b|
|LPSPI3SCK|LPSPI3 SCK|Master|PTD1|97|1|0|0011b|252|X|
|_||Slave|||0|1|X||0010b|
|||Master|PTE7|135|1|0|0110b||X|
|||Slave|||0|1|X||0100b|
|||Master|PTF13|173|1|0|0100b||X|
|LPSPI4_SCK|LPSPI4 SCK|Slave|PTB10|42|0|1|X|259|0010b|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

771 / 4640 

NXP Semiconductors 

Clocking 

Table 114. SIUL2 options for LPSPIn SCK (continued) 

|Source<br>Destination|SPI|Port|MSCR a||MSCR fiel|ds<br>IMCR b|IMCR[SSS]|
|---|---|---|---|---|---|---|---|
||mode|||OBE|IBE|SSS||
||Master|||1|0|0001b|X|
||Slave|PTC27|91|0|1|X|0001b|
||Master|||1|0|0111b|X|
||Slave|PTE22|150|0|1|X|0011b|
||Master|||1|0|0110b|X|
||Slave|PTA3|3|0|1|X|0010b|
||Master|||1|0|0111b|X|
|LPSPI5SCK<br>LPSPI5 SCK|Slave|PTD14|110|0|1|266<br>X|0001b|
|_<br>|Master|||1|0|0001b|X|
||Slave|PTD26|122|0|1|X|0011b|
||Master|||1|0|0110b|X|



#### 23.6.1.1.6 LPUART clocking 

The following figure shows the LPUART clocking configuration, and the related table shows LPUART use case baud rates. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0772-06.png)


<!-- Start of picture text -->
LPUART_[0,8]<br>AIPS_PLAT_CLK MODULE_CLK<br>REG_INTF_CLK<br>LPUART_[1:7, 9:15]<br>AIPS_SLOW_CLK MODULE_CLK<br>REG_INTF_CLK<br>Figure 67. LPUART clocking<br><!-- End of picture text -->

~~<mark>NOTE</mark>~~ 

See Feature comparison for details on this module's availability on your chip variant. 

LPUART_0 and LPUART_1 is clocked by AIPS_PLAT_CLK, to support up to 12 Mbps while the core is running at 120 MHz. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

772 / 4640 

NXP Semiconductors 

Clocking 

##### Table 115. LPUART baud rate calculation 

|Required baud rate<br>(bps)|LPUART_CLK<br>(MHz)|OSR|SBR[12:0]|Calculated baud rate<br>(bps)<sup>1</sup>|
|---|---|---|---|---|
|8192|40|4|976|8196|
|8192|80|15|610|8196|
|8192|48|15|366|8196|
|115200|48|15|26|115384|
|115200|40|7|43|116279|
|19200|80|4|833|19207|
|19200|40|7|260|19230|
|38400|40|7|130|38461|



1. MODULE_CLK ÷ (LPUART.BAUD[SBR] × (LPUART.BAUD[OSR] + 1)) 

#### 23.6.1.1.7 FlexIO clocking 

The following figure shows the FlexIO clocking interface. The related two tables show the FlexIO baud rate use cases. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0773-07.png)


<!-- Start of picture text -->
FlexIO<br>AIPS_PLAT_CLK MODULE_CLK<br>REG_INTF_CLK<br>CORE_CLK FLEXIO_CLK<br>Figure 68. FlexIO clocking<br><!-- End of picture text -->

~~<mark>NOTE</mark>~~ 

See Feature comparison for details on this module's availability on your chip variant. 

Table 116. FlexIO baud rate calculation (FlexIO.TIMCFGn[TIMDEC] = 101b) 

|FLEXIO_CLK<br>(CORE_CLK)|Required baud<br>rate|TIMCM<br>Hex|Pn[CMP]<br>Decimal|Theoretical<br>baud rate<sup>1</sup>|Bit duration|Observed baud<br>rate|
|---|---|---|---|---|---|---|
|88 MHz|9600|0010h|16|10110.29|101.33 μs|9868|
|88 MHz|19200|0007h|7|21484.37|47.44 μs|21079|
|88 MHz|57600|0001h|1|85937.50|11.66 μs|85763|
|88 MHz|115200|0000h|0|171875.00|5.88 μs|170068|



> 1. Theoretical baud rate = Frequency ÷ (256 × 2 × (TIMCMPn[CMP] + 1)) 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

773 / 4640 

NXP Semiconductors 

Clocking 

Table 117. FlexIO baud rate calculation (FlexIO.TIMCFGn[TIMDEC] = 100b) 

|FLEXIO_CLK<br>(CORE_CLK)|Required baud<br>rate|TIMCM<br>Hex|Pn[CMP]<br>Decimal|Theoretical<br>baud rate<sup>1</sup>|Bit duration|Observed baud<br>rate|
|---|---|---|---|---|---|---|
|88 MHz|9600|—|—|—|—|—|
|88 MHz|19200|8Eh|142|19230.77|51.88 μs|19275|
|88 MHz|57600|2Eh|46|58510.64|16.89 μs|59206|
|88 MHz|115200|16h|22|119565.21|8.44 μs|118483|



#### 23.6.1.1.8 QuadSPI clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0774-05.png)


<!-- Start of picture text -->
QuadSPI<br>AIPS_PLAT_CLK MODULE_CLK<br>REG_INTF_CLK<br>AHB_CLK<br>PTD10 QSPI_2xSFIF 2xSFIF_CLK<br>QSPI_SFCK<br>QuadSPI_SCKFA 7 SF_IF_X_CLK<br>SFCK<br>SIUL2_MSCR106[OBE]<br>SIUL2_MSCR106[SSS]<br>QSPI_RAM<br>QSPI_MEM_CLK QSPI_RAM_CLK<br>QSPI_TX<br>QSPI_TX_MEM_CLK<br>Figure 69. QuadSPI clocking<br>  NOTE<br>See Feature comparison for details on this module's availability on your chip variant.<br><!-- End of picture text -->

For S32K358, QSPI_SFCK will be generated by a fixed 1:2 divider from the QSPI_2xSFIF_CLK. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

774 / 4640 

NXP Semiconductors 

Clocking 

Table 118. QuadSPI clocking 

|Clock option|AIPS_PLAT_CLK|QSPI_SFCK|QSPI_MEM_CLK|
|---|---|---|---|
|SeeOption A - High Performance mode (CORE_CLK @ 160<br>MHz)|80 MHz|120 MHz|160 MHz|
|SeeOption B - Reduced Speed mode (CORE_CLK @ 120<br>MHz)|60 MHz|120 MHz or 80<br>MHz|120 MHz|
|SeeOption F - Operation in 1:1 mode with CORE_CLK and<br>AXBS_CLK at same speed|80 MHz|80 MHz|160 MHz|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

775 / 4640 

NXP Semiconductors 

Clocking 

#### 23.6.1.1.9 SAI_n clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0776-03.png)


<!-- Start of picture text -->
AIPS_SLOW_CLK<br>FXOSC_CLK<br>SIUL2<br>SIUL2_IMCR315[SSS]<br>SIUL2_MSCR76[IBE]<br>SAI_0<br>0001<br>MODULE_CLK/<br>SAI0_BCLK REG_INTF_CLK<br>111 BCLK<br>SIUL2_MSCR76[OBE]<br>00<br>SIUL2_MSCR76[SSS]<br>01<br>SIUL2_IMCR320[SSS] 10<br>SIUL2_MSCR35[IBE] 11<br>0001<br>SAI_0. x CR2[MSEL]<br>SAI0_MCLK<br>SIUL2_MSCR35[OBE]<br>SIUL2_MSCR35[SSS]<br>SIUL2_IMCR263[SSS]<br>SIUL2_MSCR136[IBE]<br>0001<br>SAI_1<br>SAI1_BCLK<br>MODULE_CLK/<br>REG_INTF_CLK<br>110<br>SIUL2_MSCR136[OBE] BCLK<br>SIUL2_MSCR136[SSS]<br>00<br>SIUL2_IMCR324[SSS]<br>01<br>SIUL2_MSCR110[IBE]<br>10<br>0001 11<br>SAI1_MCLK<br>SAI_1. x CR2[MSEL]<br>SIUL2_MSCR110[OBE]<br>Figure 70. SAI_n clocking<br><!-- End of picture text -->

~~<mark>NOTE</mark>~~ 

See Feature comparison for details on this module's availability on your chip variant. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

776 / 4640 

NXP Semiconductors 

Clocking 

Table 119. SIUL2 options for SAI_n 

|Source|Destination|Port|MSCR a||MSCR fie|lds|IMCR b|IMCR[SSS]|
|---|---|---|---|---|---|---|---|---|
|||||OBE|IBE|SSS|||
||SAI_0.xCR2[MSEL] =|||0|1|X||0001b|
|SAI0_MCLK|01b<br>SAI_1.xCR2[MSEL] =<br>11b|PTB3|35|—|—|Not<br>available|320|X|
||SAI_0.xCR2[MSEL] =|||0|1|X||0001b|
|SAI1_MCLK|11b<br>SAI_1.xCR2[MSEL] =<br>01b|PTD14|110|1|0|Not<br>available|324|X|
|SAI0_BCLK|SAI0 BCLK|PTC12|76|0|1|X|315|0001b|
|SAI0 BCLK|SAI0_BCLK|||1|0|111b||X|
|SAI1_BCLK|SAI1 BCLK|PTE8|136|0|1|X|322|0001b|
|SAI1 BCLK|SAI1_BCLK|||1|0|110b||X|



Internally generated MCLK is not supported on the S32K3xx chip family. 

#### 23.6.1.2 System modules 

Figure 71 shows the REG_INTF_CLK and MODULE_CLK connections, and Table 120 shows the REG_INTF_CLK and MODULE_CLK signals used by these modules. Any module diagram that does not explicitly show a REG_INTF_CLK uses the same source for REG_INTF_CLK as used by MODULE_CLK. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0777-07.png)


<!-- Start of picture text -->
Module<br>See REG_INTF_CLK<br>REG_INTF_CLK<br>and MODULE_CLK<br>columns in table below } MODULE_CLK<br><!-- End of picture text -->

Figure 71. System module clocks 

Table 120. System module clocking 

|Module|MODULE_CLK|REG_INTF_CLK|
|---|---|---|
|MSCM|AIPS_PLAT_CLK|AIPS_PLAT_CLK|
|MCM|AIPS_SLOW_CLK|AIPS_SLOW_CLK|
|SIUL2|SeeSIUL2 clocking.||
|VIRT_WRAPPER|AIPS_SLOW_CLK|AIPS_SLOW_CLK|
|AXBS|CORE_CLK|AIPS_PLAT_CLK|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

777 / 4640 

NXP Semiconductors 

Clocking 

Table 120. System module clocking (continued) 

|Module|MODULE_CLK|REG_INTF_CLK|
|---|---|---|
|DMAMUX|CORE_CLK|CORE_CLK|
|eDMA|CORE_CLK|AIPS_PLAT_CLK|
|INTM|AIPS_PLAT_CLK|AIPS_PLAT_CLK|
|SEMA42|AIPS_PLAT_CLK|AIPS_PLAT_CLK|
|XBIC|CORE_CLK|AIPS_PLAT_CLK|
|XRDC|CORE_CLK|AIPS_PLAT_CLK|



#### 23.6.1.2.1 SIUL2 clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0778-05.png)


<!-- Start of picture text -->
SIUL2<br>AIPS_SLOW_CLK MODULE_CLK<br>REG_INTF_CLK<br>FIRC_CLK FILTER_CLK<br>Figure 72. SIUL2 clocking<br><!-- End of picture text -->

#### 23.6.1.3 Clocking modules 

Figure 73 shows the REG_INTF_CLK and MODULE_CLK connections, and Table 121 shows the REG_INTF_CLK and MODULE_CLK signals used by these modules. Any module diagram that does not explicitly show a REG_INTF_CLK uses the same source for REG_INTF_CLK as used by MODULE_CLK. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0778-08.png)


<!-- Start of picture text -->
Module<br>See REG_INTF_CLK<br>REG_INTF_CLK<br>and MODULE_CLK<br>columns in table below } MODULE_CLK<br><!-- End of picture text -->

Figure 73. Clocking module clocks 

Table 121. Clocking module clocking 

||Module|MODULE_CLK|REG_INTF_CLK|
|---|---|---|---|
|FXOSC||SeeFXOSC clocking.||
|SXOSC||SeeSXOSC clocking.||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

778 / 4640 

NXP Semiconductors 

Clocking 

##### Table 121. Clocking module clocking (continued) 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0779-03.png)


<!-- Start of picture text -->
Module MODULE_CLK REG_INTF_CLK<br>SIRC See SIRC clocking.<br>FIRC See FIRC clocking.<br>PLLDIG See PLLDIG clocking.<br>—<br>MC_CGM AIPS_SLOW_CLK<br><!-- End of picture text -->

#### 23.6.1.3.1 FIRC clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0779-05.png)


<!-- Start of picture text -->
FIRC<br>AIPS_SLOW_CLK REG_INTF_CLK<br>3<br>÷16 2<br>Oscillator FIRC_CLK<br>÷2 1<br>÷2 0<br>HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL]<br>Figure 74. FIRC clocking<br><!-- End of picture text -->

#### 23.6.1.3.2 SIRC clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0779-07.png)


<!-- Start of picture text -->
SIRC<br>Oscillator SIRC_CLK<br>AIPS_SLOW_CLK REG_INTF_CLK<br>Figure 75. SIRC clocking<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

779 / 4640 

NXP Semiconductors 

Clocking 

#### 23.6.1.3.3 FXOSC clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0780-03.png)


<!-- Start of picture text -->
FXOSC<br>AIPS_SLOW_CLK REG_INTF_CLK<br>EXTAL<br>FXOSC_CLK<br>XTAL<br>Figure 76. FXOSC clocking<br><!-- End of picture text -->

#### 23.6.1.3.4 SXOSC clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0780-05.png)


<!-- Start of picture text -->
SXOSC<br>AIPS_SLOW_CLK REG_INTF_CLK<br>OSC32K_EXTAL<br>SXOSC_CLK<br>OSC32K_XTAL<br>Figure 77. SXOSC clocking<br><!-- End of picture text -->

#### 23.6.1.3.5 PLLDIG clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0780-07.png)


<!-- Start of picture text -->
PLLDIG<br>FXOSC_CLK Reference PLL_PHI0_CLK<br>clock<br>AIPS_SLOW_CLK REG_INTF_CLK PLL_PHI1_CLK<br>Figure 78. PLLDIG clocking<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

780 / 4640 

NXP Semiconductors 

Clocking 

#### 23.6.1.4 Reset modules 

Figure 79 shows the REG_INTF_CLK and MODULE_CLK connections, and Table 122 shows the REG_INTF_CLK and MODULE_CLK signals used by these modules. Any module diagram that does not explicitly show a REG_INTF_CLK uses the same source for REG_INTF_CLK as used by MODULE_CLK. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0781-04.png)


<!-- Start of picture text -->
Module<br>See REG_INTF_CLK<br>REG_INTF_CLK<br>and MODULE_CLK<br>columns in table below } MODULE_CLK<br><!-- End of picture text -->

Figure 79. Reset module clocks 

Table 122. Reset module clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0781-07.png)


<!-- Start of picture text -->
Module MODULE_CLK REG_INTF_CLK<br>MC_RGM FIRC_CLK FIRC_CLK<br><!-- End of picture text -->

#### 23.6.1.5 Security modules 

Figure 80 shows the REG_INTF_CLK and MODULE_CLK connections, and Table 123 shows the REG_INTF_CLK and MODULE_CLK signals used by these modules. Any module diagram that does not explicitly show a REG_INTF_CLK uses the same source for REG_INTF_CLK as used by MODULE_CLK. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0781-10.png)


<!-- Start of picture text -->
Module<br>See REG_INTF_CLK<br>REG_INTF_CLK<br>and MODULE_CLK<br>columns in table below } MODULE_CLK<br><!-- End of picture text -->

Figure 80. Security module clocks 

Table 123. Security module clocking 

||Module|MODULE_CLK|REG_INTF_CLK|
|---|---|---|---|
|HSE_B||SeeHSE_B clocking.||
|MU_n||AIPS_SLOW_CLK|AIPS_SLOW_CLK|
|DCM||DCM_CLK|DCM_CLK|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

781 / 4640 

NXP Semiconductors 

Clocking 

#### 23.6.1.5.1 HSE_B clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0782-03.png)


<!-- Start of picture text -->
HSE_B<br>HSE_CLK PLL (MODULE_CLK)<br>DCM_CLK DCF_clk<br>AIPS_SLOW_CLK HSE_B_IPS<br>PLL standby<br>SIRC_CLK Slow 32k clk<br>TCK TCK<br>TCK_n<br>HSE_MU0<br>MODULE_CLK<br>REG_INTF_CLK<br>HSE_MU1<br>MODULE_CLK<br>REG_INTF_CLK<br><!-- End of picture text -->


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0782-04.png)


<!-- Start of picture text -->
Figure 81. HSE_B clocking<br><!-- End of picture text -->

#### 23.6.1.6 Power-management modules 

Figure 82 shows the REG_INTF_CLK and MODULE_CLK connections, and Table 124 shows the REG_INTF_CLK and MODULE_CLK signals used by these modules. Any module diagram that does not explicitly show a REG_INTF_CLK uses the same source for REG_INTF_CLK as used by MODULE_CLK. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0782-07.png)


<!-- Start of picture text -->
Module<br>See REG_INTF_CLK<br>REG_INTF_CLK<br>and MODULE_CLK<br>columns in table below } MODULE_CLK<br><!-- End of picture text -->

Figure 82. Power-management module clocks 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

782 / 4640 

NXP Semiconductors 

Clocking 

Table 124. Power-management module clocking 

||Module|MODULE_CLK|REG_INTF_CLK|
|---|---|---|---|
|PMC||AIPS_SLOW_CLK|AIPS_SLOW_CLK|
|MC_ME||AIPS_SLOW_CLK|AIPS_SLOW_CLK|
|MC_PCU||FIRC_CLK|FIRC_CLK|
|WKPU||AIPS_SLOW_CLK|AIPS_SLOW_CLK|



#### 23.6.1.7 Safety modules 

Figure 83 shows the REG_INTF_CLK and MODULE_CLK connections, and Table 125 shows the REG_INTF_CLK and MODULE_CLK signals used by these modules. Any module diagram that does not explicitly show a REG_INTF_CLK uses the same source for REG_INTF_CLK as used by MODULE_CLK. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0783-06.png)


<!-- Start of picture text -->
Module<br>See REG_INTF_CLK<br>REG_INTF_CLK<br>and MODULE_CLK<br>columns in table below } MODULE_CLK<br><!-- End of picture text -->

Figure 83. Safety module clocks 

Table 125. Safety module clocking 

|Module|MODULE_CLK|REG_INTF_CLK|
|---|---|---|
|EIM|AIPS_PLAT_CLK|AIPS_PLAT_CLK|
|ERM|SeeERM clocking.||
|FCCU|SeeFCCU clocking.||
|STCU2|SeeSTCU2 clocking.||
|REG_PROT|AIPS_SLOW_CLK|AIPS_SLOW_CLK|
|CMU_FC|AIPS_SLOW_CLK|AIPS_SLOW_CLK|
|CMU_FM|AIPS_SLOW_CLK|AIPS_SLOW_CLK|
|CRC|AIPS_PLAT_CLK|AIPS_PLAT_CLK|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

783 / 4640 

NXP Semiconductors 

Clocking 

#### 23.6.1.7.1 FCCU clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0784-03.png)


<!-- Start of picture text -->
FCCU<br>AIPS_PLAT_CLK MODULE_CLK<br>REG_INTF_CLK<br>FIRC_CLK SAFE_CLK<br>Figure 84. FCCU clocking<br><!-- End of picture text -->

#### 23.6.1.7.2 STCU2 clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0784-05.png)


<!-- Start of picture text -->
STCU2<br>AIPS_SLOW_CLK CORE_CLK<br>REG_INTF_CLK<br>JTAG_TCK SHIFT_CLK<br>Figure 85. STCU2 clocking<br><!-- End of picture text -->

#### 23.6.1.7.3 ERM clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0784-07.png)


<!-- Start of picture text -->
ERM<br>AIPS_PLAT_CLK MODULE_CLK<br>CORE_CLK MEM_CLK[ n ]<br>Figure 86. ERM clocking<br><!-- End of picture text -->

~~<mark>NOTE</mark>~~ 

MEM_CLK[20:23] are not used. Source clock for MEM_CLK[0:19] is CORE_CLK. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

784 / 4640 

NXP Semiconductors 

Clocking 

#### 23.6.1.8 ADC and motor control modules 

Figure 87 shows the REG_INTF_CLK and MODULE_CLK connections, and Table 126 shows the REG_INTF_CLK and MODULE_CLK signals used by these modules. Any module diagram that does not explicitly show a REG_INTF_CLK uses the same source for REG_INTF_CLK as used by MODULE_CLK. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0785-04.png)


<!-- Start of picture text -->
Module<br>See REG_INTF_CLK<br>REG_INTF_CLK<br>and MODULE_CLK<br>columns in table below } MODULE_CLK<br><!-- End of picture text -->

Figure 87. Motor control module clocks 

Table 126. Motor control module clocking 

||Module|MODULE_CLK|REG_INTF_CLK|
|---|---|---|---|
|ADC||SeeADC_n clocking.||
|LCU||CORE_CLK||
|eMIOS||SeeeMIOS_n clocking.||
|BCTU||SeeBCTU clocking.||
|TRGMUX||AIPS_SLOW_CLK||
|TSPC||AIPS_SLOW_CLK||



#### 23.6.1.8.1 ADC_n clocking 

The following figure shows ADC_n clocking configuration. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0785-10.png)


<!-- Start of picture text -->
ADC_ n<br>REG_INTF_CLK<br>MODULE_CLK<br>CORE_CLK<br>00<br>÷2 01 AD_CLK<br>÷4 10<br>Available in K358  ÷8 11<br>and K311 only<br>ADC.MCR[ADCLKSEL]<br><!-- End of picture text -->

Figure 88. ADC_n clocking 

~~<mark>NOTE</mark>~~ 

See Feature comparison for details on this module's availability on your chip variant. 

The prescaler can be bypassed when using FIRC_CLK as the source (see MC_CGM mux 0 clocks for FIRC_CLK use details). The prescaler must be controlled such that the AD_CLK frequency is less than or equal to 120 MHz for S32K358/S32K312/S32K311. For other S32K3XX products the frequency is 80 MHz. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

785 / 4640 

NXP Semiconductors 

Clocking 

The minimum operating speed of AD_CLK is 6 MHz using the following configuration: 

1. Use FIRC_CLK (48 MHz) as clock source (MC_CGM.MUX_0_CSC[SELCTL] equal to 0000b). 

2. Divide FIRC_CLK by 2 for CORE_CLK speed (MC_CGM.MUX_0_DC_0[DIV] equal to 1 (FIRC_CLK divide by 2 = 24 MHz)). 

3. Write ADC.MCR[ADCCLKSEL] equal to 10b to divide the FIRC_CLK further by 4 (AD_CLK = 6 MHz). 

However, at this lower speed, the ADC_n results will be degraded. 

#### 23.6.1.8.2 eMIOS_n clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0786-08.png)


<!-- Start of picture text -->
eMIOS_ n<br>CORE_CLK MODULE_CLK<br>REG_INTF_CLK<br>EMIOS_CLK<br>EMIOS_CH[0:23]_CLK<br><!-- End of picture text -->

Figure 89. eMIOS_n clocking 

~~<mark>NOTE</mark>~~ 

See Feature comparison for details on this module's availability on your chip variant. 

#### 23.6.1.8.3 BCTU clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0786-13.png)


<!-- Start of picture text -->
BCTU<br>CORE_CLK MODULE_CLK<br>REG_INTF_CLK<br>BCTU_CLK<br>Figure 90. BCTU clocking<br><!-- End of picture text -->

#### 23.6.1.9 Timer modules 

Figure 91 shows the REG_INTF_CLK and MODULE_CLK connections, and Table 127 shows the REG_INTF_CLK and MODULE_CLK signals used by these modules. Any module diagram that does not explicitly show a REG_INTF_CLK uses the same source for REG_INTF_CLK as used by MODULE_CLK. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

786 / 4640 

NXP Semiconductors 

Clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0787-02.png)


<!-- Start of picture text -->
Module<br>See REG_INTF_CLK<br>REG_INTF_CLK<br>and MODULE_CLK<br>columns in table below } MODULE_CLK<br><!-- End of picture text -->

Figure 91. Timer module clocks 

Table 127. Timer module clocking 

||Module|MODULE_CLK|REG_INTF_CLK|
|---|---|---|---|
|PIT||SeePIT_n clocking.||
|SWT||SeeSWT_n clocking.||
|STM_n||STM0_CLK|STM0_CLK|
|RTC||SeeRTC clocking.||



#### 23.6.1.9.1 PIT_n clocking 

The following figure shows the PIT_n clocking configuration. The related tables show the use case configuration. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

787 / 4640 

NXP Semiconductors 

Clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0788-02.png)


<!-- Start of picture text -->
PIT_0<br> AIPS_SLOW_CLK MODULE_CLK<br>Timer 0<br>REG_INTF_CLK<br>PIT_CLK<br>Timer 1<br>Timer 2<br>Timer 3<br>RTI_CLK<br>SIRC_CLK RTI<br>PIT_[1,2]<br> AIPS_SLOW_CLK MODULE_CLK<br>Timer 0<br>REG_INTF_CLK<br>PIT_CLK<br>Timer 1<br>Timer 2<br>Timer 3<br>Figure 92. PIT_n clocking<br><!-- End of picture text -->

~~<mark>NOTE</mark>~~ 

See Feature comparison for details on this module's availability on your chip variant. 

Table 128. PIT_0 modes of operation 

|MC_ME.PRTN0_COFB1_C<br>LKEN[REQ44]|PIT_0.MCR[MDI<br>S]|PIT_0.MCR[MDI<br>S_RTI]|Mode|Application|
|---|---|---|---|---|
|0|X|X|PIT_0 clock gated<br>(minimum power)|Module clock gated and<br>unused / Standby mode,<br>PIT and RTI unused|
|1|0|0|Both PIT and RTI enabled|Run mode|
|1|0|1|PIT running, RTI disabled|Run mode with only PIT<br>active|
|1|1|0|PIT disabled, RTI enabled|Standby mode with RTI<br>enabled|
|1|1|1|Both PIT and RTI disabled|Standby mode with RTI<br>disabled|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

788 / 4640 

NXP Semiconductors 

Clocking 

Table 129. PIT_[1,2] modes of operation 

|MC_ME.PRTNn_C<br>OFB1_CLKEN[RE<br>Q[45,63]]<sup>1</sup>|PIT_[1,2].MCR[MD<br>IS]|Mode|Application|
|---|---|---|---|
|0|X|PIT_[1,2] clock gated (minimum power)|Module clock gated and unused,<br>Standby mode|
|1|0|PIT_[1,2] enabled|Run mode|
|1|0|PIT_[1,2] running|Run mode with PIT active|
|1|1|PIT_[1,2] disabled|Standby mode|



1. PIT_1 and PIT_2 MC_ME partition registers used are: 

   - PIT_1 - MC_ME.PRTN0_COFB1_CLKEN[REQ45] 

   - PIT_2 - MC_ME.PRTN1_COFB1_CLKEN[REQ63] 

#### 23.6.1.9.2 SWT_n clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0789-08.png)


<!-- Start of picture text -->
SWT_ n<br>AIPS_SLOW_CLK MODULE_CLK<br>SIRC_CLK COUNTER_CLK<br>Figure 93. SWT_n clocking<br><!-- End of picture text -->

~~<mark>NOTE</mark>~~ 

See Feature comparison for details on this module's availability on your chip variant. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

789 / 4640 

NXP Semiconductors 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0790-01.png)


<!-- Start of picture text -->
Clocking<br><!-- End of picture text -->


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0790-02.png)


<!-- Start of picture text -->
23.6.1.9.3 RTC clocking<br><!-- End of picture text -->


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0790-03.png)


<!-- Start of picture text -->
RTC<br>AIPS_SLOW_CLK MODULE_CLK/REG_INTF_CLK<br>RTC.RTCC[SELCTL]<br>Not available on: Clock source 0<br>- S32K311 SXOSC_CLK 0 RTC.RTCC[DIV512EN]<br>Clock source 1<br>SIRC_CLK 1 RTC_CLK RTC.RTCC[CNTEN]<br>0<br>FIRC_CLK Clock source 2 2 0<br>÷512 1 32-bit counter<br>FXOSC_CLK Clock source 3 3 ÷32 1<br>To other modules<br>RTC.RTCC[DIV32EN]<br>Figure 94. RTC clocking<br><!-- End of picture text -->

~~<mark>NOTE</mark>~~ 

The RTC is available in Standby mode. Although bus clock is gated, the RTC can run on FIRC_CLK, SIRC_CLK, FXOSC_CLK, or SXOSC_CLK. 

#### 23.6.1.10 Debug modules 

Figure 95 shows the REG_INTF_CLK and MODULE_CLK connections, and Table 130 shows the REG_INTF_CLK and MODULE_CLK signals used by these modules. Any module diagram that does not explicitly show a REG_INTF_CLK uses the same source for REG_INTF_CLK as used by MODULE_CLK. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0790-08.png)


<!-- Start of picture text -->
Module<br>See REG_INTF_CLK<br>REG_INTF_CLK<br>and MODULE_CLK<br>columns in table below } MODULE_CLK<br><!-- End of picture text -->

Figure 95. Debug module clocks 

Table 130. Debug module clocking 

|Module|MODULE_CLK|REG_INTF_CLK|
|---|---|---|
|JTAGC|SeeJTAGC clocking.||
|JDC|SeeJDC clocking.||



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

790 / 4640 

NXP Semiconductors 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0791-01.png)


<!-- Start of picture text -->
Clocking<br><!-- End of picture text -->

#### 23.6.1.10.1 JTAGC clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0791-03.png)


<!-- Start of picture text -->
JTAGC<br>JTAG_TCK/SWD_CLK TCK_P<br>TCK_N<br>Figure 96. JTAGC clocking<br><!-- End of picture text -->

#### 23.6.1.10.2 JDC clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0791-05.png)


<!-- Start of picture text -->
JDC<br>AIPS_SLOW_CLK MODULE_CLK<br>REG_INTF_CLK<br>JTAG_TCK/SWD_CLK TCK_P<br>TCK_N<br>Figure 97. JDC clocking<br><!-- End of picture text -->

#### 23.6.1.11 Analog modules 

Figure 98 shows the REG_INTF_CLK and MODULE_CLK connections, and Table 131 shows the REG_INTF_CLK and MODULE_CLK signals used by these modules. Any module diagram that does not explicitly show a REG_INTF_CLK uses the same source for REG_INTF_CLK as used by MODULE_CLK. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0791-08.png)


<!-- Start of picture text -->
Module<br>See REG_INTF_CLK<br>REG_INTF_CLK<br>and MODULE_CLK<br>columns in table below } MODULE_CLK<br><!-- End of picture text -->


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0791-09.png)


<!-- Start of picture text -->
Figure 98. Analog module clocks<br><!-- End of picture text -->

Table 131. Analog module clocking 

|Module|MODULE_CLK|REG_INTF_CLK|
|---|---|---|
|LPCMP|SeeLPCMP_n clocking.||
|Temperature Sensor|AIPS_SLOW_CLK|AIPS_SLOW_CLK|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

791 / 4640 

NXP Semiconductors 

Clocking 

#### 23.6.1.11.1 LPCMP_n clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0792-03.png)


<!-- Start of picture text -->
DAC<br>AIPS_SLOW_CLK MODULE_CLK<br>REG_INTF_CLK<br>LPCMP_ n<br>AIPS_SLOW_CLK MODULE_CLK<br>REG_INTF_CLK<br>RTC_CLK ROUND_ROBIN_CLK<br>Figure 99. LPCMP_n clocking<br>  NOTE<br><!-- End of picture text -->

See Feature comparison for details on this module's availability on your chip variant. 

#### 23.6.1.12 Memory modules 

Figure 100 shows the REG_INTF_CLK and MODULE_CLK connections, and Table 132 shows the REG_INTF_CLK and MODULE_CLK signals used by these modules. Any module diagram that does not explicitly show a REG_INTF_CLK uses the same source for REG_INTF_CLK as used by MODULE_CLK. 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0792-07.png)


<!-- Start of picture text -->
Module<br>See REG_INTF_CLK<br>REG_INTF_CLK<br>and MODULE_CLK<br>columns in table below } MODULE_CLK<br><!-- End of picture text -->

Figure 100. Memory module clocks 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

792 / 4640 

NXP Semiconductors 

Clocking 

Table 132. Memory module clocking 

|Module|MODULE_CLK|REG_INTF_CLK|
|---|---|---|
|PFLASH/ FLASH|CORE_CLK|AIPS_SLOW_CLK|
|PRAM/ SRAM|CORE_CLK|AIPS_SLOW_CLK|



### 23.6.2 Peripheral data rates 

Table 133. Peripheral data rates 

|Peripheral|Maximum|data rate|
|---|---|---|
||S32K322, S32K342, S32K314, S32K324, S32K358<br>and S32K344|S32K311 and S32K312|
|ADC|See the S32K3xx Data Sheet for details.|See the S32K3xx Data Sheet for details.|
|eMIOS<sup>1</sup>|Able to shift PWM edge by 1 ÷ (160 MHz) = 6.25 ns.|Able to shift PWM edge by 1 ÷ (120 MHz) = 8.33 ns.|
|BCTU<sup>2</sup>|BCTU to generate triggers at 160 MHz.|BCTU to generate triggers at 120 MHz.|
|LCU|Same domain as EMIOS and BCTU.|Same domain as EMIOS and BCTU.|
|QuadSPI|• Flash memory interface: SDR 120 MHz<br>• DDR and hyperflash not supported|• Flash memory interface: SDR 120 MHz<br>• DDR and hyperflash not supported|
|EMAC|See the sectionEMAC instance and configurationin<br>the "Ethernet Media Access Controller (EMAC)" chapter<br>for details.|See the sectionEMAC instance and configurationin<br>the "Ethernet Media Access Controller (EMAC)" chapter<br>for details.|
|FlexCAN<sup>3</sup>|8 Mbps|8 Mbps|
|LPI2C<sup>4</sup>|400 Kbps in fast mode.|400 Kbps in fast mode.|
|LPSPI<sup>5</sup>|• LPSPI0 is to have a high clock rate of 20 Mbps<br>• LPSPI1–LPSPI5 can be 10 Mbps|• LPSPI0 is to have a high clock rate of 15 Mbps<br>• LPSPI1–LPSPI3 can be 7.5 Mbps|
|SAI0/SAI1<br>(I2S)<sup>6</sup>|• Bit rate = 12.288 MHz (12.288 Mbps—bit clock<br>frequency governs the bit rate)<br>• Master clock = 24.576 MHz<br>• SAI0 and SAI1 operate asynchronously to<br>each other|• Bit rate = 12.288 MHz (12.288 Mbps—bit clock<br>frequency governs the bit rate)<br>• Master clock = 24.576 MHz<br>• SAI0 and SAI1 operate asynchronously to<br>each other|
|LPUART<sup>7</sup>|See the sectionBaud rate generationin the "Low<br>Power Universal Asynchronous Receiver/ Transmitter<br>(LPUART)" chapter andTable 115for details|See the sectionBaud rate generationin the "Low<br>Power Universal Asynchronous Receiver/ Transmitter<br>(LPUART)" chapter andTable 115for details|
|FlexIO<sup>8</sup>|The different protocol data rates supported by FlexIO<br>are listed below. For master mode, max baud rate is<br>FLEXIO_CLK ÷ 4. For slave mode, max baud rate<br>is FLEXIO_CLK ÷ 6. The baud rate is controlled by<br>TIMCMP (lower 8 bits in 8-bit mode and 16 bits in<br>16-bit mode).<br>• UART: 19200 bps|The different protocol data rates supported by FlexIO<br>are listed below. For master mode, max baud rate is<br>FLEXIO_CLK ÷ 4. For slave mode, max baud rate<br>is FLEXIO_CLK ÷ 6. The baud rate is controlled by<br>TIMCMP (lower 8 bits in 8-bit mode and 16 bits in<br>16-bit mode).<br>• UART: 19200 bps|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

793 / 4640 

NXP Semiconductors 

Clocking 

##### Table 133. Peripheral data rates (continued) 

|Peripheral|Maximum|data rate|
|---|---|---|
||S32K322, S32K342, S32K314, S32K324, S32K358<br>and S32K344|S32K311 and S32K312|
||• I2C: 400 Kbps|• I2C: 400 Kbps|
||• SPI: 10 Mbps|• SPI: 7.5 Mbps|
||• I2S: 12.288 Mbps|• I2S: 12.288 Mbps|
|Trace|• Fast-speed pins: 120 MHz|• SWO trace|
||• Medium-speed pins: 48 MHz||
|I3C|See "I3C_0 clocking" section for details|See "I3C_0 clocking" section for details|
|uSDHC<sup>9</sup>|320 Mbps|-|



1. See section Global clock prescaler (GCP) in the "Enhanced Modular IO Subsystem (eMIOS)" chapter for details. 

2. See section Triggers in the "Enhanced Modular IO Subsystem (eMIOS)" chapter. 

3. See the section Protocol timing in the "CAN (FlexCAN)" chapter for data rate calculation details. 

4. See the section Clocks in the "Low Power Inter-Integrated Circuit (LPI2C)" chapter for LPI2C_CLK frequency details. 

5. See the section Clocks in the "Low Power Serial Peripheral Interface (LPSPI)" chapter. 

6. See the section Clocking in the "Synchronous Audio Interface (SAI)" chapter and SAI_n clocking for details. 

7. At least one pair of LPUART instances (LPUART0 and LPUART1) support up to 12 Mbps. 

8. See the section Application Information and FlexIO instances and configuration in the "Flexible I/O (FlexIO)" chapter and FlexIO clocking for baud configuration details. 

9. uSDHC is present in S32K358 only. 

### 23.6.3 Core and peripheral clock control 

The chip provides provisions for core and peripheral clock gating. The next sections describe the details on clock gating possibilities and controls (see Power Management Controller (PMC) and Mode Entry Module (MC_ME) for details). 

#### 23.6.3.1 Clock gating 

Application core clocks are gated by individual MC_ME core clock enable bits. Additionally, application cores can be clock gated by executing WFI (see the "Mode Entry Module (MC_ME)" chapter for details). 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0794-17.png)


<!-- Start of picture text -->
APP DEBUGEN<br>DAP-PWRUP REQUEST<br>MDMAPCTL[CM7_ n _CORE_ACCESS] FCLKEN<br>CLKEN<br>Cortex-M7_ n  CCTL gating<br>Cortex-M7_ n<br>HCLKEN<br>MC_ME_PCTL | (CORE CM7 CCTL & !CORE SLEEPING)<br>CLKIN<br>CORE_CLK<br><!-- End of picture text -->

Figure 101. Cortex-M7 core clock gating 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

794 / 4640 

NXP Semiconductors 

Clocking 

To support core debug across functional reset, challenge response done (application debug enable) gating is done so that the debugger can access core debug logic. When the debugger completes its programming with core debug logic, it must program the MDM_AP DAP control bit to shift the control of CLKIN and FCLK to CCTL. 

There are two cases in which other masters can access the TCM of each core: 

- When the TCM is used as system memory—HCLK will always remain on if TCM PCTL is 1. 

- In applications where TCM is not used as system memory, TCM PCTL is written to 0. TCM will then function as the core's memory and HCLK will be gated on WFI. 

See the section "MDM_AP register descriptions" in the Debug Subsystem chapter and the Memory Map chapter for details. 

#### 23.6.3.2 Peripheral clock gating 

See the tables in section "Peripheral clock gating" for the chip partitions, plus peripheral initialization and shutdown details. 

## 23.7 Clocking details 

### 23.7.1 System clock frequency limitations 

Table 134. System clock frequency limitations 

|System clock node|System clock divider|Maximum frequency allowed|Remarks|
|---|---|---|---|
|CORE_CLK|MC_CGM.MUX_0_DC_0[DIV]|• 240 MHz: S32K358<br>• 160 MHz: S32K344,<br>S32K324, S32K314,<br>S32K322, and S32K342<br>• 120 MHz: S32K311<br>and S32K312|CORE_CLK is always greater than or<br>equal to AIPS_PLAT_CLK.|
|AIPS_PLAT_CLK|MC_CGM.MUX_0_DC_1[DIV]|80 MHz|AIPS_PLAT_CLK is always less than<br>or equal to CORE_CLK.|
|AIPS_SLOW_CLK|MC_CGM.MUX_0_DC_2[DIV]|40 MHz|AIPS_SLOW_CLK is always less<br>than or equal to AIPS_PLAT_CLK.|
|HSE_CLK|MC_CGM.MUX_0_DC_3[DIV]|120 MHz|When CORE_CLK is equal to or<br>less than 120 MHz, HSE_CLK<br>can be equal to CORE_CLK.<br>When CORE_CLK is higher than<br>120 MHz, HSE_CLK must be half of<br>the CORE_CLK.|
|DCM_CLK|MC_CGM.MUX_0_DC_4[DIV]|48 MHz|DCM_CLK|
|LBIST_CLK|MC_CGM.MUX_0_DC_5[DIV]|48 MHz|LBIST clock|
|QSPI_MEM_CLK|MC_CGM.MUX_0_DC_6[DIV]|160 MHz|QSPI_MEM_CLK is always equal to<br>CORE_CLK except in 1:1 mode (see<br>Option F - Operation in 1:1 mode<br>with CORE_CLK and AXBS_CLK at<br>same speed).|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

795 / 4640 

NXP Semiconductors 

Clocking 

~~<mark>NOTE</mark>~~ 

The chip supports 1:1 clocking mode, whereby the core(s) are clocked at the same frequency as the slave ports (flash memory, PRAM controller, AIPS controller). Option F - Operation in 1:1 mode with CORE_CLK and AXBS_CLK at same speed supports this requirement. 

The frequencies in the table above are maximum frequencies for a specific clock. However, any clock frequency selected must adhere to the same clock divider ratios shown in System clocking configurations. 

### 23.7.2 System clocking configurations 

The chip supports the clocking modes shown in Table 135. All clock configurations are implemented by appropriate register settings. 

Table 135. System clocking configurations 

|Clocking<br>options|Option A<br>High-<br>performanc<br>e mode|Option B<br>Reduced<br>speed<br>mode|Option C<br>Boot<br>(default)<br>Standby<br>configuratio<br>n (for low<br>dynamic<br>current<br>consumptio<br>n)|Option D<br>FIRC<br>divider<br>bypassed|Option E<br>Low speed<br>Run mode,<br>clocked by<br>divided<br>FIRC|Option E2<br>Very low<br>speed Run<br>mode, clock<br>by divided<br>FIRC|Option F<br>Operation in<br>1:1 mode<br>with core<br>and AXBS<br>at same<br>speed|Option G<br>PLL<br>providing 48<br>MHz (test<br>bench use<br>case)|
|---|---|---|---|---|---|---|---|---|
|System<br>clock<br>source<br>(SYS_CLK)|PLL_PHI0_<br>CLK|PLL_PHI0_<br>CLK|FIRC_CLK<br>÷ 2|FIRC_CLK|FIRC_CLK<br>÷ 2|FIRC_CLK<br>÷ 16|PLL_PHI0_<br>CLK|PLL_PHI0_<br>CLK|
|PLL VCO<br>frequency|480 MHz|480 MHz|—|—|—|—|480 MHz|480 MHz|
|PLL_PHI1_<br>CLK|K344: 240<br>MHz<br>(VCO ÷ 2)<br>K342: 160<br>MHz<br>(VCO ÷ 3)|K344: 240<br>MHz<br>(VCO ÷ 2)<br>K342: 160<br>MHz<br>(VCO ÷ 3)|—|—|—|—|K344: 240<br>MHz<br>(VCO/2)<br>K342: 160<br>MHz<br>(VCO/3)|—|
|PLL_PHI0_<br>CLK|160 MHz<br>(VCO ÷ 3)|120 MHz<br>(VCO ÷ 4)|—|—|—|—|160 MHz<br>(VCO ÷ 3)|96 MHz<br>(VCO ÷ 5)|
|CORE_CLK<br>(application<br>cores,<br>AXBS,<br>SRAM,<br>AIPS0,<br>flash<br>memory<br>controller<br>port clock,|160 MHz<br>(SYS_CLK)|120 MHz<br>(SYS_CLK)|24 MHz<br>(FIRC_CLK<br>÷ 2)|48 MHz<br>(FIRC)|3 MHz<br>((FIRC ÷ 2)<br>÷ 8)|187.5 kHz<br>((FIRC ÷<br>16) ÷ 16)|80 MHz<br>(SYS_CLK<br>÷ 2)|48 MHz<br>(SYS_CLK<br>÷ 2)|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

796 / 4640 

NXP Semiconductors 

Clocking 

Table 135. System clocking configurations (continued) 

|Clocking<br>options|Option A<br>High-<br>performanc<br>e mode|Option B<br>Reduced<br>speed<br>mode|Option C<br>Boot<br>(default)<br>Standby<br>configuratio<br>n (for low<br>dynamic<br>current<br>consumptio<br>n)|Option D<br>FIRC<br>divider<br>bypassed|Option E<br>Low speed<br>Run mode,<br>clocked by<br>divided<br>FIRC|Option E2<br>Very low<br>speed Run<br>mode, clock<br>by divided<br>FIRC|Option F<br>Operation in<br>1:1 mode<br>with core<br>and AXBS<br>at same<br>speed|Option G<br> <br>PLL<br>providing 48<br>MHz (test<br>bench use<br>case)|
|---|---|---|---|---|---|---|---|---|
|QSPI<br>memory<br>clock, fast-<br>speed<br>peripherals<br>clock)|||||||||
|QSPI mem<br>clock|160 MHz|120 MHz|—|—|—|—|160 MHz|—|
|AIPS_PLAT<br>_CLK<br>(medium-<br>speed<br>peripheral<br>clock|80 MHz|60 MHz|24 MHz|48 MHz|3 MHz|187.5 kHz|80 MHz|48 MHz|
|AIPS_SLO<br>W_CLK<br>(slow-speed<br>peripheral<br>clock)|40 MHz|30 MHz|12 MHz|24 MHz|1.5 MHz|93.75 kHz|40 MHz|24 MHz|
|DCM/<br>DCF_CLK|40 MHz|30 MHz|24 MHz|48 MHz|3 MHz|187.5 kHz|40 MHz|48 MHz|
|HSE_CLK|80 MHz|K34x:<br>60/120 MHz<br>K31x:<br>60/120 MHz|24 MHz|48 MHz|3 MHz|187.5 kHz|80 MHz|48 MHz|
|LBIST_CLK|40 MHz|30 MHz|—|—|—|—|40 MHz|—|
|QSPI_SFC<br>K|K344: 120<br>MHz (QSPI<br>only)<br>80 MHz<br>(QSPI +<br>ENET RMII)<br>K342: 80<br>MHz|K344: 120<br>MHz (QSPI<br>only)<br>80 MHz<br>(QSPI +<br>ENET RMII)<br>K342: 80<br>MHz|—|—|—|—|K344: 120<br>MHz (QSPI<br>only)<br>80 MHz<br>(QSPI +<br>ENET RMII)|—|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

797 / 4640 

NXP Semiconductors 

Clocking 

###### ~~<mark>NOTE</mark>~~ 

In system clocking configurations where CORE_CLK and AIPS_PLAT_CLK are configured for operation at same frequency, the RAM wait states and flash memory read/write wait cycles need to be configured. See Clock Option B in Gasket Configurations section for RAM wait states and gasket configurations for clocking options. 

The PLL should only be enabled if it is used as the system clock source. When the FIRC is used directly as the system clock, the PLL must be disabled. 

While enabling PLL, the PMC last mile regulator should be enabled first, by configuring PMC_CONFIG[LMEN] and PMC_CONFIG[LMBCTLEN] (in case of external BJT). The last mile regulator should be disabled after PLL is disabled. 

PLL can be locked at minimum 640 MHz and then 8 MHz can be achieved with dividers in series - PLL divider(divide 

by 16) and CGM divider(divide by 5). 

#### 23.7.2.1 Option A+ - Very High Performance mode (CORE_CLK @ 240 MHz) 

Table 136. Option A+ - High Performance mode (CORE_CLK @ 240 MHz) 

|Clocking options|C|lock frequencie|s|
|---|---|---|---|
|||S32K358<sup>1</sup>||
|PLL VCO frequency||960 MHz||
|PLLODIV2_CLK<br>(PLLDIG.PLLDV[ODIV2])||480 MHz<br>(02h)||
|FIRC_CLK<br>(HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL])<br>PLL_PHI1_CL|K-related clocks <sup>2</sup>|—||
|PLL_PHI1_CLK<br>(PLLDIG.PLLODIV_1[DIV])|240 MHz<br>(0001b)||160 MHz<br>(0010b)|
|QSPI_SFCK<br>(MC_CGM.MUX_10_DC_0[DIV])|125 MHz<br>(0001b)||125 MHz<br>(0001b)|
|||For fast pads||
|TRACE_CLK|125 MHz<br>(0001b)||125 MHz<br>(0001b)|
|(MC_CGM.MUX_11_DC_0[DIV])|F|or medium pad|s|
||48 MHz<br>(0100b)||40 MHz<br>(011b)|
|PLL_PHI0_CL|K-related clocks <sup>3</sup>|||
|PLL_PHI0_CLK<br>(PLLDIG.PLLODIV_0[DIV])||240 MHz<br>(0010b)||
|CORE_CLK||240 MHz<br>(0000b)||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

798 / 4640 

NXP Semiconductors 

Clocking 

Table 136. Option A+ - High Performance mode (CORE_CLK @ 240 MHz) (continued) 

|Clocking options|Clock frequencies|
|---|---|
||S32K358<sup>1</sup>|
|• Application cores<br>• AXBS<br>• SRAM<br>• Flash memory controller port clock<br>• AIPS0 (high-speed peripheral clock)<br>(MC_CGM.MUX_0_DC_0[DIV])||
|QSPI_MEM_CLK<br>(MC_CGM.MUX_0_DC_6[DIV])|240 MHz<br>(0000b)|
|AIPS_PLAT_CLK (medium-speed peripheral clock)<br>(MC_CGM.MUX_0_DC_1[DIV])|120 MHz<br>(0001b)|
|AIPS_SLOW_CLK (slow-speed peripheral clock)<br>(MC_CGM.MUX_0_DC_2[DIV])|60 MHz<br>(0011b)|
|DCM_CLK<br>(MC_CGM.MUX_0_DC_4[DIV])|60 MHz<br>(0011b)|
|HSE_CLK<br>(MC_CGM.MUX_0_DC_3[DIV])|120 MHz<br>(0001b)|
|LBIST_CLK|60 MHz|
|(MC_CGM.MUX_0_DC_5[DIV])|(0011b)|



1. This table is only applicable for S32K358. 

2. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] must equal 1001b. 

3. MC_CGM.MUX_0_CSC[SELCTL] must equal 1000b. 

#### 23.7.2.2 Option A - High Performance mode (CORE_CLK @ 160 MHz) 

Table 137. Option A - High Performance mode (CORE_CLK @ 160 MHz) 

|Clocking options|Clock frequencies<br>S32K344, S32K324, S32K314, S32K342, and S32K322<sup>1</sup>|
|---|---|
|PLL VCO frequency|960 MHz|
|PLLODIV2_CLK|480 MHz|
|(PLLDIG.PLLDV[ODIV2])|(02h)|
|FIRC_CLK||
|(HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL])|—|



PLL_PHI1_CLK-related clocks<sup>2</sup> 

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

799 / 4640 

NXP Semiconductors 

Clocking 

##### Table 137. Option A - High Performance mode (CORE_CLK @ 160 MHz) (continued) 

|Clocking options||Clock frequencies||
|---|---|---|---|
||S32K344, S32K324,|S32K314, S32K|342, and S32K322<sup>1</sup>|
|PLL_PHI1_CLK<br>(PLLDIG.PLLODIV_1[DIV])|240 MHz<br>(0001b)||160 MHz<br>(0010b)|
|QSPI_SFCK<br>(MC_CGM.MUX_10_DC_0[DIV])|120 MHz<br>(0001b)||80 MHz<br>(0001b)|
|||For fast pads||
|TRACE_CLK|120 MHz<br>(0001b)||80 MHz<br>(0001b)|
|(MC_CGM.MUX_11_DC_0[DIV])||For medium pads||
||48 MHz<br>(0100b)||40 MHz<br>(011b)|
|PLL_PHI0_|CLK-related clocks <sup>3</sup>|||
|PLL_PHI0_CLK<br>(PLLDIG.PLLODIV_0[DIV])||160 MHz<br>(0010b)||
|CORE_CLK<br>• Application cores<br>• AXBS<br>• SRAM<br>• Flash memory controller port clock<br>• AIPS0 (high-speed peripheral clock)<br>(MC_CGM.MUX_0_DC_0[DIV])||160 MHz<br>(0000b)||
|QSPI_MEM_CLK<br>(MC_CGM.MUX_0_DC_6[DIV])||160 MHz<br>(0000b)||
|AIPS_PLAT_CLK (medium-speed peripheral clock)<br>(MC_CGM.MUX_0_DC_1[DIV])||80 MHz<br>(0001b)||
|AIPS_SLOW_CLK (slow-speed peripheral clock)<br>(MC_CGM.MUX_0_DC_2[DIV])||40 MHz<br>(0011b)||
|DCM_CLK<br>(MC_CGM.MUX_0_DC_4[DIV])||40 MHz<br>(0011b)||
|HSE_CLK||80 MHz||
|(MC_CGM.MUX_0_DC_3[DIV])||(0001b)||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

800 / 4640 

NXP Semiconductors 

Clocking 

Table 137. Option A - High Performance mode (CORE_CLK @ 160 MHz) (continued) 

|Clocking options|Clock frequencies<br>S32K344, S32K324, S32K314, S32K342, and S32K322<sup>1</sup>|
|---|---|
|LBIST_CLK|40 MHz|
|(MC_CGM.MUX_0_DC_5[DIV])|(0011b)|



1. This table does not apply to S32K311 or S32K312. 

2. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] must equal 1001b. 

3. MC_CGM.MUX_0_CSC[SELCTL] must equal 1000b. 

#### 23.7.2.3 Option B - Reduced Speed mode (CORE_CLK @ 120 MHz) 

Table 138. Option B - Reduced Speed mode (CORE_CLK @ 120 MHz) 

||Clock frequ|encies|
|---|---|---|
|Clocking options|S32K344, S32K324, S32K314,<br>S32K342, and S32K322|S32K311 and S32K312|
|PLL VCO frequency|960 MHz|960 MHz|
|PLLODIV2_CLK<br>(PLLDIG.PLLDV[ODIV2])|480 MHz<br>(02h)|240 MHz<br>(04h)|
|FIRC_CLK<br>(HSE_B.CONFIG_REG_GPR[FIRC_DIV<br>_SEL])|—||
||PLL_PHI1_CLK-related clocks <sup>1</sup>,<sup>2</sup>||
|PLL_PHI1_CLK<br>(PLLDIG.PLLODIV_1[DIV])|240 MHz<br>(0001b)<br>160 MHz<br>(0010b)|48 MHz)<br>(0100b)|
|QSPI_SFCK<br>(MC_CGM.MUX_10_DC_0[DIV])|120 MHz<br>(001b)<br>80 MHz<br>(001b)|—|
||For fast pads|—|
|TRACE_CLK|120 MHz<br>(001b)<br>80 MHz<br>(001b)|—|
|(MC_CGM.MUX_11_DC_0[DIV])|For medium pads|—|
||48 MHz<br>(100b)<br>40 MHz<br>(011b)<br>PLL_PHI0_CLK-related clocks <sup>3</sup>|—|
|PLL_PHI0_CLK|120 MHz|120 MHz|
|(PLLDIG.PLLODIV_0[DIV])|(011b)|(001b)|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

801 / 4640 

NXP Semiconductors 

Clocking 

##### Table 138. Option B - Reduced Speed mode (CORE_CLK @ 120 MHz) (continued) 

||Clock fre|quencies||
|---|---|---|---|
|Clocking options|S32K344, S32K324, S32K314,<br>S32K342, and S32K322|S32K311 and S3|2K312|
|CORE_CLK<br>• Application cores<br>• AXBS<br>• SRAM<br>• Flash memory controller port clock<br>• AIPS0 (high-speed peripheral clock)<br>(MC_CGM.MUX_0_DC_0[DIV])|120 MHz<br>(000b)|120 MHz<br>(000b)||
|QSPI_MEM_CLK<br>(MC_CGM.MUX_0_DC_6[DIV])|120 MHz<br>(000b)|—||
|AIPS_PLAT_CLK (medium-speed<br>peripheral clock)<br>(MC_CGM.MUX_0_DC_1[DIV])|60 MHz<br>(001b)|60 MHz<br>(001b)||
|AIPS_SLOW_CLK (slow-speed<br>peripheral clock)<br>(MC_CGM.MUX_0_DC_2[DIV])|30 MHz<br>(011b)|30 MHz<br>(011b)||
|DCM_CLK<br>(MC_CGM.MUX_0_DC_4[DIV])|30 MHz<br>(011b)|30 MHz<br>(011b)||
|HSE_CLK|120 MHz<br>60 MHz|120 MHz|60 MHz|
|(MC_CGM.MUX_0_DC_3[DIV])|(000b)<br>(001b)|(000b)|(001b)|
|LBIST_CLK|30 MHz|30 MHz||
|(MC_CGM.MUX_0_DC_5[DIV])|(011b)|(011b)||



1. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] must equal 1001b. 

2. Do not use the combination of different frequencies mentioned below across the 2x2 matrix. The values shown in each cell are valid and must not be clubbed with the values mentioned in any other cells. 

3. MC_CGM.MUX_0_CSC[SELCTL] must equal 1000b. 

#### 23.7.2.4 Option C - Boot Standby mode (CORE_CLK @ 24 MHz) 

Table 139. Option C - Boot Standby mode (CORE_CLK @ 24 MHz) 

|Clocking options|Clock frequencies<br>S32K3xx|
|---|---|
|PLL VCO frequency|—|
|PLLODIV2_CLK|—|
|(PLLDIG.PLLDV[ODIV2])||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

802 / 4640 

NXP Semiconductors 

Clocking 

Table 139. Option C - Boot Standby mode (CORE_CLK @ 24 MHz) (continued) 

|Clocking options<br>Clock frequencies<br>S32K3xx|
|---|
|FIRC_CLK<br>(HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL])<br>24 MHz<sup>1</sup><br>(00b)|
|PLL_PHI1_CLK-related clocks <sup>2</sup>|
|PLL_PHI1_CLK<br>(PLLDIG.PLLODIV_1[DIV])<br>—|
|QSPI_SFCK<br>(MC_CGM.MUX_10_DC_0[DIV])<br>—|
|TRACE_CLK<br>(MC_CGM.MUX_11_DC_0[DIV])<br>—|
|PLL_PHI0_CLK-related clocks <sup>3</sup>|
|PLL_PHI0_CLK<br>(PLLDIG.PLLODIV_0[DIV])<br>—|
|LBIST_CLK<br>(MC_CGM.MUX_0_DC_5[DIV])<br>—|
|QSPI_MEM_CLK<br>(MC_CGM.MUX_0_DC_6[DIV])<br>—|
|CORE_CLK<br>• Application cores<br>• AXBS<br>• SRAM<br>• Flash memory controller port clock<br>• AIPS0 (high-speed peripheral clock)<br>(MC_CGM.MUX_0_DC_0[DIV])<br>24 MHz<br>(0000b)|
|AIPS_PLAT_CLK (medium-speed peripheral clock)<br>(MC_CGM.MUX_0_DC_1[DIV])<br>24 MHz<br>(0000b)|
|AIPS_SLOW_CLK (slow-speed peripheral clock)<br>(MC_CGM.MUX_0_DC_2[DIV])<br>12 MHz<br>(0001b)|
|DCM_CLK<br>(MC_CGM.MUX_0_DC_4[DIV])<br>24 MHz<br>(0000b)|
|HSE_CLK<br>(MC_CGM.MUX_0_DC_3[DIV])<br>24 MHz<br>(0000b)|



S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

803 / 4640 

NXP Semiconductors 

Clocking 

1. The FIRC_DIV_SEL is configured by the sBAF code. It is set to 11b after reset or normal standby exit and FIRC_CLK is 48 MHz. In case of fast standby exit, FIRC_DIV_SEL is 00b and FIRC_CLK is 24 MHz. 

2. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] values are don't care since QSPI_SFCK and TRACE_CLK are not used in this use case. 

3. MC_CGM.MUX_0_CSC[SELCTL] must equal 0. 

#### 23.7.2.5 Option D - Low-Speed RUN mode (CORE_CLK @ 48 MHz) 

Table 140. Option D - Low-Speed RUN mode (CORE_CLK @ 48 MHz) 

|Clocking options|Clock frequencies|
|---|---|
|(SYS_CLK = FIRC_CLK)|S32K3xx|
|PLL VCO frequency|—|
|PLLODIV2_CLK<br>(PLLDIG.PLLDV[ODIV2])|—|
|FIRC_CLK<br>(HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL])|48 MHz<br>(11b)|
|PLL_PHI1_CLK-related clocks <sup>1</sup>||
|PLL_PHI1_CLK<br>(PLLDIG.PLLODIV_1[DIV])|—|
|QSPI_SFCK<br>(MC_CGM.MUX_10_DC_0[DIV])|—|
|TRACE_CLK<br>(MC_CGM.MUX_11_DC_0[DIV])|—|
|PLL_PHI0_CLK-related clocks <sup>2</sup>||
|PLL_PHI0_CLK<br>(PLLDIG.PLLODIV_0[DIV])|—|
|LBIST_CLK<br>(MC_CGM.MUX_0_DC_5[DIV])|—|
|QSPI_MEM_CLK<br>(MC_CGM.MUX_0_DC_6[DIV])|—|
|CORE_CLK<br>• Application cores<br>• AXBS<br>• SRAM<br>• Flash memory controller port clock<br>• AIPS0 (high-speed peripheral clock)<br>(MC_CGM.MUX_0_DC_0[DIV])|48 MHz<br>(0000b)|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

804 / 4640 

NXP Semiconductors 

Clocking 

Table 140. Option D - Low-Speed RUN mode (CORE_CLK @ 48 MHz) (continued) 

|Clocking options|Clock frequencies|
|---|---|
|(SYS_CLK = FIRC_CLK)|S32K3xx|
|AIPS_PLAT_CLK (medium-speed peripheral clock)<br>(MC_CGM.MUX_0_DC_1[DIV])|48 MHz<br>(0000b)|
|AIPS_SLOW_CLK (slow-speed peripheral clock)<br>(MC_CGM.MUX_0_DC_2[DIV])|24 MHz<br>(0001b)|
|DCM_CLK|48 MHz|
|(MC_CGM.MUX_0_DC_4[DIV])|(0000b)|
|HSE_CLK|48 MHz|
|(MC_CGM.MUX_0_DC_3[DIV])|(0000b)|



1. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] values are don't care since QSPI_SFCK and TRACE_CLK are not used in this use case. 

2. MC_CGM.MUX_0_CSC[SELCTL] must equal 0. 

#### 23.7.2.6 Option E - Low-Speed Run mode (CORE_CLK @ 3 MHz) 

Table 141. Option E - Low-Speed Run mode (CORE_CLK @ 3 MHz) 

|Clki ti|Clock frequencies|
|---|---|
|ocng opons|S32K3xx|
|PLL VCO frequency|—|
|PLLODIV2_CLK<br>(PLLDIG.PLLDV[ODIV2])|—|
|FIRC_CLK<br>(HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL])|3 MHz<br>(10b)|
|PLL_PHI1_CLK-related clocks <sup>1</sup>||
|PLL_PHI1_CLK<br>(PLLDIG.PLLODIV_1[DIV])|—|
|QSPI_SFCK<br>(MC_CGM.MUX_10_DC_0[DIV])|—|
|TRACE_CLK<br>(MC_CGM.MUX_11_DC_0[DIV])|—|
|PLL_PHI0_CLK-related clocks <sup>2</sup>||
|PLL_PHI0_CLK<br>(PLLDIG.PLLODIV_0[DIV])|—|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

805 / 4640 

NXP Semiconductors 

Clocking 

Table 141. Option E - Low-Speed Run mode (CORE_CLK @ 3 MHz) (continued) 

|Clocking options|Clock frequencies|
|---|---|
||S32K3xx|
|LBIST_CLK<br>(MC_CGM.MUX_0_DC_5[DIV])|—|
|QSPI_MEM_CLK<br>(MC_CGM.MUX_0_DC_6[DIV])|—|
|CORE_CLK<br>• Application cores<br>• AXBS<br>• SRAM<br>• Flash memory controller port clock<br>• AIPS0 (high-speed peripheral clock)<br>(MC_CGM.MUX_0_DC_0[DIV])|3 MHz<br>(0000b)|
|AIPS_PLAT_CLK (medium-speed peripheral clock)<br>(MC_CGM.MUX_0_DC_1[DIV])|3 MHz<br>(0000b)|
|AIPS_SLOW_CLK (slow-speed peripheral clock)<br>(MC_CGM.MUX_0_DC_2[DIV])|1.5 MHz<br>(0001b)|
|DCM_CLK<br>(MC_CGM.MUX_0_DC_4[DIV])|3 MHz<br>(0000b)|
|HSE_CLK|3 MHz|
|(MC_CGM.MUX_0_DC_3[DIV])|(0000b)|



1. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] values are don't care since QSPI_SFCK and TRACE_CLK are not used in this use case. 

2. MC_CGM.MUX_0_CSC[SELCTL] must equal 0. 

###### ~~<mark>NOTE</mark>~~ 

For FIRC_CLK frequency modes less than 24 MHz, safety modules like the CMU_Fx_n must be disabled for safety applications, because safety applications are to run on the PLL clocks. The CMU_Fx_n will cause erroneous FHH events if not disabled. 

#### 23.7.2.7 Option E2 - Very-Low-Speed Run mode (CORE_CLK @ 750 kHz) 

Table 142. Option E2 - Very-Low-Speed Run mode (CORE_CLK @ 750 kHz) 

|Clocking options|Clock frequencies|
|---|---|
|(SYS_CLK = (FIRC_CLK ÷ 8) ÷ 8)|S32K3xx|
|PLL VCO frequency|—|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

806 / 4640 

NXP Semiconductors 

Clocking 

##### Table 142. Option E2 - Very-Low-Speed Run mode (CORE_CLK @ 750 kHz) (continued) 

|Clocking options|Clock frequencies|
|---|---|
|(SYS_CLK = (FIRC_CLK ÷ 8) ÷ 8)|S32K3xx|
|PLLODIV2_CLK<br>(PLLDIG.PLLDV[ODIV2])|—|
|FIRC_CLK<br>(HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL])|3 MHz<br>(10b)|
|PLL_PHI1_CLK-related clocks <sup>1</sup>||
|PLL_PHI1_CLK<br>(PLLDIG.PLLODIV_1[DIV])|—|
|QSPI_SFCK<br>(MC_CGM.MUX_10_DC_0[DIV])|—|
|TRACE_CLK<br>(MC_CGM.MUX_11_DC_0[DIV])|—|
|PLL_PHI0_CLK-related clocks <sup>2</sup>||
|PLL_PHI0_CLK<br>(PLLDIG.PLLODIV_0[DIV])|—|
|LBIST_CLK<br>(MC_CGM.MUX_0_DC_5[DIV])|—|
|QSPI_MEM_CLK<br>(MC_CGM.MUX_0_DC_6[DIV])|—|
|CORE_CLK<br>• Application cores<br>• AXBS<br>• SRAM<br>• Flash memory controller port clock<br>• AIPS0 (high-speed peripheral clock)<br>(MC_CGM.MUX_0_DC_0[DIV])|750 KHz<br>(0011b)|
|AIPS_PLAT_CLK (medium-speed peripheral clock)<br>(MC_CGM.MUX_0_DC_1[DIV])|750 KHz<br>(0011b)|
|AIPS_SLOW_CLK (slow-speed peripheral clock)<br>(MC_CGM.MUX_0_DC_2[DIV])|375 KHz<br>(0111b)|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

807 / 4640 

NXP Semiconductors 

Clocking 

Table 142. Option E2 - Very-Low-Speed Run mode (CORE_CLK @ 750 kHz) (continued) 

|Clocking options|Clock frequencies|
|---|---|
|(SYS_CLK = (FIRC_CLK ÷ 8) ÷ 8)|S32K3xx|
|DCM_CLK|750 KHz|
|(MC_CGM.MUX_0_DC_4[DIV])|(0011b)|
|HSE_CLK|750 KHz|
|(MC_CGM.MUX_0_DC_3[DIV])|(0011b)|



1. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] values are don't care since QSPI_SFCK and TRACE_CLK are not used in this use case. 

2. MC_CGM.MUX_0_CSC[SELCTL] must equal 0. 

~~<mark>NOTE</mark>~~ 

For FIRC_CLK frequency modes less than 24 MHz, safety modules like the CMU_Fx_n must be disabled for safety applications, because safety applications are to run on the PLL clocks. The CMU_Fx_n will cause erroneous FHH events if not disabled. 

#### 23.7.2.8 Option F - Operation in 1:1 mode with CORE_CLK and AXBS_CLK at same speed 

Table 143. Option F - Operation in 1:1 mode with CORE_CLK and AXBS_CLK at same speed 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0808-10.png)


<!-- Start of picture text -->
Clock frequencies<br>Clocking options S32K344, S32K324, S32K314, S32K342, and  S32K311 and<br>S32K322 S32K312<br>PLL VCO frequency 960 MHz 960 MHz<br>PLLODIV2_CLK 480 MHz 240 MHz<br>(PLLDIG.PLLDV[ODIV2]) (02h) (04h)<br>FIRC_CLK(HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL]) —<br>PLL_PHI1_CLK-related clocks 1<br>PLL_PHI1_CLK 240 MHz 160 MHz 48 MHz<br>(PLLDIG.PLLODIV_1[DIV]) (0001b) (0010b) (0100b)<br>QSPI_SFCK(MC_CGM.MUX_10_DC_0[DIV]) 120 MHz(001b) 80 MHz(001b) —<br>—<br>For fast pads<br>120 MHz 80 MHz —<br>(001b) (001b)<br>TRACE_CLK<br>(MC_CGM.MUX_11_DC_0[DIV]) —<br>For medium pads<br>48 MHz 40 MHz —<br>(100b) (011b)<br><!-- End of picture text -->

Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

808 / 4640 

NXP Semiconductors 

Clocking 

Table 143. Option F - Operation in 1:1 mode with CORE_CLK and AXBS_CLK at same speed (continued) 

||Clock frequencies||
|---|---|---|
|Clocking options|S32K344, S32K324, S32K314, S32K342, and<br>S32K322|S32K311 and<br>S32K312|
|PLL|_PHI0_CLK-related clocks <sup>2</sup>||
|PLL_PHI0_CLK<br>(PLLDIG.PLLODIV_0[DIV])|160 MHz<br>(010b)|80 MHz<br>(010b)|
|CORE_CLK<br>• Application cores<br>• AXBS<br>• SRAM<br>• Flash memory controller port clock<br>• AIPS0 (high-speed peripheral clock)<br>(MC_CGM.MUX_0_DC_0[DIV])|80 MHz<br>(001b)|80 MHz<br>(000b)|
|QSPI_MEM_CLK<br>(MC_CGM.MUX_0_DC_6[DIV])|160 MHz<br>(000b)|—|
|AIPS_PLAT_CLK (medium-speed peripheral<br>clock)<br>(MC_CGM.MUX_0_DC_1[DIV])|80 MHz<br>(001b)|80 MHz<br>(000b)|
|AIPS_SLOW_CLK (slow-speed peripheral clock)<br>(MC_CGM.MUX_0_DC_2[DIV])|40 MHz<br>(011b)|40 MHz<br>(001b)|
|DCM_CLK<br>(MC_CGM.MUX_0_DC_4[DIV])|40 MHz<br>(011b)|40 MHz<br>(001b)|
|HSE_CLK<br>(MC_CGM.MUX_0_DC_3[DIV])|80 MHz<br>(001b)|80 MHz<br>(000b)|
|LBIST_CLK|40 MHz|40 MHz|
|(MC_CGM.MUX_0_DC_5[DIV])|(011b)|(001b)|



1. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] must equal 1001b. 

2. MC_CGM.MUX_0_CSC[SELCTL] must equal 1000b. 

### 23.7.3 Gasket configurations in various clocking modes 

Table 144. Gasket configurations in various clocking modes (for S32K3x4, S32K342 and S32K322) 

|Gasket<br>configurations|Option A<sup>1</sup>|Option B<sup>2</sup>|Option C<sup>3</sup>|Option D<sup>4</sup>|Option E<sup>5</sup>|Option E2<sup>6</sup>|Option F<sup>7</sup>|
|---|---|---|---|---|---|---|---|
|eDMA (S0)|1:1|||Byp|ass|||



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

809 / 4640 

NXP Semiconductors 

Clocking 

Table 144. Gasket configurations in various clocking modes (for S32K3x4, S32K342 and S32K322) (continued) 

|Gasket<br>configurations|Option A<sup>1</sup><br>Option B<sup>2</sup>|Option C<sup>3</sup>|Option D<sup>4</sup>|Option E<sup>5</sup>|Option E2<sup>6</sup>|Option F<sup>7</sup>|
|---|---|---|---|---|---|---|
|eDMA (S1)|||Bypass||||
|HSE_B|1:2<br>1:1, 1:2|||Bypass|||
|AIPS1/AIPS2|2:1|||Bypass|||
|QuadSPI|2:1|||Bypass|||
|PRAM/SRAM|WS enabled|||WS disabled|||
|EMAC 32:64|||1:1||||
|BDRAM 64:32|||1:1||||



1. See Option A - High Performance mode (CORE_CLK @ 160 MHz) for details. 

2. See Option B - Reduced Speed mode (CORE_CLK @ 120 MHz) for details. 

3. See Option C - Boot Standby mode (CORE_CLK @ 24 MHz) for details. 

4. See Option D - Low-Speed RUN mode (CORE_CLK @ 48 MHz) for details. 

5. See Option E - Low-Speed Run mode (CORE_CLK @ 3 MHz) for details. 

6. See Option E2 - Very-Low-Speed Run mode (CORE_CLK @ 750 kHz) for details. 

7. See Option F - Operation in 1:1 mode with CORE_CLK and AXBS_CLK at same speed for details. 

Table 145. Gasket configurations in various clocking modes (for S32K311 and S32K312) 

|Gasket configurations|Option B<sup>1</sup>|Option C<sup>2</sup>|Option D<sup>3</sup><br>Option E<sup>4</sup>|Option E2<sup>5</sup>|Option F<sup>6</sup>|
|---|---|---|---|---|---|
|HSE_B|1:1, 1:2||Bypass|||
|AIPS1|2:1||Bypass|||
|PRAM/SRAM|||WS disabled|||
|BDRAM 64:32 (TCM<br>WS)|||1:1|||



1. See Option B - Reduced Speed mode (CORE_CLK @ 120 MHz) for details. 

2. See Option C - Boot Standby mode (CORE_CLK @ 24 MHz) for details. 

3. See Option D - Low-Speed RUN mode (CORE_CLK @ 48 MHz) for details. 

4. See Option E - Low-Speed Run mode (CORE_CLK @ 3 MHz) for details. 

5. See Option E2 - Very-Low-Speed Run mode (CORE_CLK @ 750 kHz) for details. 

6. See Option F - Operation in 1:1 mode with CORE_CLK and AXBS_CLK at same speed for details. 

### 23.7.4 Default clock configuration 

At reset recovery, the chip runs on the FIRC_CLK as the default configuration as shown in Option C - Boot Standby mode (CORE_CLK @ 24 MHz). Clocking configuration Option_C is the default configuration out of reset with the HSE_B core as the boot core. The Cortex-M7_n application core clocks are gated by default. You need to enable the core clocks by the configuring the corresponding core clock enable bits shown in Core Clock Gating. 

### 23.7.5 PCFS 

The chip supports software-controllable PCFS for MC_CGM MUX_0 (see section "Progressive Clock Frequency Switching (PCFS)" in the "Clock Generation Module (MC_CGM)" chapter for details). PCFS increases and decreases the frequency in steps, avoiding any overshoots or undershoots. When a functional reset event occurs with PCFS enabled, the PCFS process runs and is then followed by the divider configuration updates. 

S32K3xx Reference Manual, Rev. 4, 04/2022 Preliminary Information 

Reference Manual 

810 / 4640 

NXP Semiconductors 

Clocking 

### 23.7.6 Updating dividers: crossbar halt handshake 

The clock divider update process consists of the crossbar halt handshake sequence (see section "Clock dividers update" in the "Clock Generation Module (MC_CGM)" chapter for the clock divider update process). A divider update asserts a request to the crossbar switch to halt any transaction that is in process. The dividers are updated when the crossbar switch acknowledges the request for halt. The halt request disables the crossbar switch gaskets in the following order: 

1. Core gaskets (HSE_B gaskets) 

2. Crossbar switch (AXBS) 

3. Flash AXBS bridge 

4. PRAM/SRAM gasket 

Dividers are updated after the gaskets acknowledge the halt request. 

### 23.7.7 Changing system clock configurations 

Software sequence for switching clock configurations from FIRC to PLL or PLL to PLL: 

1. Before changing the system clock dividers or before system clock switching, the communication modules working on the system clock should be disabled by the software to avoid any erroneous communication during the clock transition. 

2. The peripherals working on the system clock should be clock-gated used the MC_ME.PRTNx_COFBy_CLKEN configurations. The peripherals working on non-system clocks which are not being switched, can continue to operate. 

3. All cores must be clock-gated, except the core being used to control the clock switching. 

4. MC_CGM divider configurations can be done to change divider values as described above. The requisite system divider frequency relations must be ensured. 

5. Configure MC_CGM_MUX_0_DIV_TRIG_CTRL (enable HHEN and TCTL). 

6. Configure MC_CGM_MUX_0_DIV_TRIG. 

7. System clock switching can be done by configuration of MC_CGM_MUX_0_CSC[SELCTL] 

Software sequence for switching clock configurations from PLL to FIRC clock switching: 

1. Before changing the system clock dividers or before system clock switching, the communication modules working on the system clock should be disabled by the software to avoid any erroneous communication during the clock transition. 

2. The peripherals working on the system clock should be clock-gated used the MC_ME.PRTNx_COFBy_CLKEN configurations. The peripherals working on non-system clocks which are not being switched, can continue to operate. 

3. All cores must be clock-gated, except the core being used to control the clock switching. 

4. System clock switching can be done by configuration of MC_CGM_MUX_0_CSC[SELCTL]. 

5. MC_CGM divider configurations can be done to change divider values as described above. The requisite system divider frequency relations must be ensured. 

6. Configure MC_CGM_MUX_0_DIV_TRIG_CTRL (enable HHEN and TCTL). 

7. Configure MC_CGM_MUX_0_DIV_TRIG. 

~~<mark>NOTE</mark>~~ 

When enabling PLL, the PMC last mile regulator should be enabled first by configuring PMC_CONFIG[LMEN] and PMC_CONFIG[LMBCTLEN] (if using an external BJT). The last mile regulator must be disabled after PLL is disabled. 

## 23.8 Clock monitoring 

The chip contains an independent clock monitoring mechanism which signals malfunctions in the clocking system. This chip consists of six Clock Monitoring Units (CMU_Fx_[0:5]) for monitoring system clock and clocking module outputs. Figure 102 and 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

811 / 4640 

NXP Semiconductors 

Clocking 

Figure 103 show a lower-level view of the clocking monitoring system. Table 146 describes each CMU instance. Each CMU instance provides an independent interrupt or reset indication when the clock signal is out of range or lost. The CMU_FM_n provides a timeout indication in case there is a loss of metered clock. Your software must periodically check the CMU_FM_1 and CMU_FM_2 status within the chip FTTI (as specified in the Safety Manual). 

|~~NOTE~~|
|---|



You must disable the CMU corresponding to the system clocks if the application changes the system clock source or changes the system clock divider configuration. 

You must disable the CMU monitoring a clock source before disabling the clock source, then enable it after enabling the clock source. 

The CMUs should be turned ON only after device has moved to PLL source (wherein LMR is ON). 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

812 / 4640 

NXP Semiconductors 

Clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0813-02.png)


<!-- Start of picture text -->
CMU_FC_4<br>CMU_FC_4.IER[FHHAIE]<br>CMU_FC_4.SR[FHH]<br>CMU_FC_4.GCR[FCE]<br>AIPS_PLAT_CLK monitored-clk<br>CMU_FC_4 destructive reset<br>FIRC_CLK reference-clk<br>CMU_FC_4.SR[FLL]<br>CMU_FC_4.IER[FLLAIE]<br>CMU_FC_5<br>CMU_FC_5.IER[FHHAIE]<br>CMU_FC_5.SR[FHH]<br>CMU_FC_5.GCR[FCE]<br>HSE_CLK monitored-clk<br>CMU_FC_5 destructive reset<br>FIRC_CLK reference-clk<br>CMU_FC_5.SR[FLL]<br>CMU_FC_5.IER[FLLAIE]<br>CMU_FC_3<br>CMU_FC_3.IER[FHHAIE]<br>CMU_FC_3.SR[FHH]<br>CMU_FC_3.GCR[FCE]<br>CORE_CLK monitored-clk<br>CMU_FC_3 destructive reset<br>FXOSC_CLK reference-clk<br>CMU_FC_3.SR[FLL]<br>CMU_FC_3.IER[FLLAIE]<br>CMU_FC_0<br>CMU_FC_0.IER[FHHAIE]<br>CMU_FC_0.SR[FHH]<br>CMU_FC_0.GCR[FCE]<br>CMU_FC_0 destructive reset<br>CMU_FC_0.IER[FHHIE]<br>FXOSC_CLK monitored-clk<br>CMU_FC_0.IER[FLLAIE]<br>FIRC_CLK reference-clk<br>CMU_FC_0.SR[FLL]<br>CMU_FC_0 interrupt<br>CMU_FC_0.IER[FLLIE]<br>Figure 102. Frequency checking (FC) instances<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

813 / 4640 

NXP Semiconductors 

Clocking 


![](.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Clocking/023_Clocking/S32K3XXRM_数据表.pdf-0814-02.png)


<!-- Start of picture text -->
CMU_FM_1<br>FIRC_CLK metered-clk<br>FXOSC_CLK reference-clk<br>CMU_FM_1.IER[FMCIE]<br>CMU_FM_1 frequency meter<br>CMU_FM_1.SR[FMC]<br>complete interrupt<br>CMU_FM_2<br>SIRC_CLK metered-clk<br>FXOSC_CLK reference-clk<br>CMU_FM_2.IER[FMCIE]<br>CMU_FM_2 frequency meter<br>CMU_FM_2.SR[FMC]<br>complete interrupt<br><!-- End of picture text -->

Figure 103. Frequency metering (FM) instances 

Table 146. System clock monitors 

|CMU|Reference<br>clock|Monitored or<br>metered clock|Failure<br>reaction|Monitoring type description|
|---|---|---|---|---|
|CMU_FC_0|FIRC_CLK|FXOSC_CLK|Destructive<br>reset or<br>interrupt|Precision over and under frequency|
|CMU_FM_1|FXOSC_CLK|FIRC_CLK|Interrupt|Current frequency measurement periodically triggered<br>by software|
|CMU_FM_2|FXOSC_CLK|SIRC_CLK|Interrupt|Current frequency measurement periodically triggered<br>by software|
|CMU_FC_3|FXOSC_CLK|CORE_CLK|Destructive<br>reset|Precision over and under frequency|
|CMU_FC_4|FIRC_CLK|AIPS_PLAT_CLK|Destructive<br>reset|Precision over and under frequency|
|CMU_FC_5|FIRC_CLK|HSE_CLK|Destructive<br>reset|Precision over and under frequency|



## 23.9 Glossary 

MODULE_CLK Module operating clock REG_INTF_CLK Module register interface clock used for register read and write PCFS Progressive Clock Frequency Switching (see section PCFS for details) POR Power On Reset SBC System Basis Chip (see NXP SBC portfolio) FLL Frequency lower than low frequency reference FHH Frequency higher than high frequency reference 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

814 / 4640 

NXP Semiconductors 

Clocking 

##### FTTI 

##### Fault Tolerance Time Interval 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

815 / 4640 

