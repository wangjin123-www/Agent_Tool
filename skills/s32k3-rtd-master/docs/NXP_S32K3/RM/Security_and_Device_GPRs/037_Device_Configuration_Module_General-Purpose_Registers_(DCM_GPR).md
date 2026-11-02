NXP Semiconductors 

# Chapter 37 Device Configuration Module General-Purpose Registers (DCM_GPR) 

## 37.1 DCM controlled features and availability in product family 

Based on the chip features described in ‘Feature comparison’ section in ‘Introduction’ chapter, there are some features which are present only in specific parts in the S32K3xx product family. The following table summarizes the corresponding DCM register fields along with the parts wherein the corresponding register fields are available. In rest of the parts within the product family, the corresponding fields are reserved. 

Table 198. DCM controlled features and availability in product family 

|Register field|Register field abbreviation|Parts wherein this field is available|
|---|---|---|
|DCMRWD3[1]|CM7_1_LOCKUP_EN|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD3[3]|CM7_RCCU1_ALARM_EN|S32K358, S32K348, S32K344,<br>S32K342, S32K341,|
|DCMRWD3[4]|CM7_RCCU2_ALARM_EN|S32K358, S32K348, S32K344,<br>S32K342, S32K341,|
|DCMRWD3[5]|TCM_GSKT_ALARM_EN|S32K344, S32K324, S32K314,<br>S32K342, S32K341, S32K322,<br>S32K312, S32K311,|
|DCMRWD3[6]|DMA_SYS_GSKT_ALARM_EN|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|DCMRWD3[7]|DMA_PERIPH_GSKT_ALARM_EN|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|DCMRWD3[9]|DMA_AXBS_ALARM_EN|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|DCMRWD3[10]|SDHC_GSKT_ALARM_EN|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWD3[12]|QSPI_GSKT_ALARM_EN|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|DCMRWD3[14]|AIPS2_GSKT_ALARM_EN|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1067 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table 198. DCM controlled features and availability in product family (continued) 

|DCMRWD3[17]|TCM_AXBS_ALARM_EN|S32K344, S32K324, S32K314,<br>S32K342, S32K341, S32K322,|
|---|---|---|
|DCMRWD3[18]|EMAC_GSKT_ALARM_EN|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|DCMRWD3[19]|PERIPH_AXBS_ALARM_EN|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|DCMRWD3[20]|PF3_CODE_ECC_ERR_EN|S32K358, S32K338,|
|DCMRWD3[21]|PF3_DATA_ECC_ERR_EN|S32K358, S32K338,|
|DCMRWD3[23]|PRAM2_ECC_ERR_EN|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWD3[24]|PRAM1_ECC_ERR_EN|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314,|
|DCMRWD3[27]|CM7_1_DCDATA_ECC_ERR_EN|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD3[29]|CM7_1_DCTAG_ECC_ERR_EN|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD3[31]|CM7_1_ICDATA_ECC_ERR_EN|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD4[1]|CM7_1_ICTAG_ECC_ERR_EN|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD4[5]|CM7_1_ITCM_ECC_ERR_EN|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K342, S32K341, S32K322,|
|DCMRWD4[6]|CM7_1_DTCM0_ECC_ERR_EN|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K342, S32K341, S32K322,|
|DCMRWD4[7]|CM7_1_DTCM1_ECC_ERR_EN|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K342, S32K341, S32K322,|
|DCMRWD4[10]|PRAM1_FCCU_ALARM_EN|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314,|
|DCMRWD4[16]|PF2_CODE_ECC_ERR_EN|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD4[17]|PF2_DATA_ECC_ERR_EN|S32K338, S32K328, S32K324,<br>S32K322,|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1068 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table 198. DCM controlled features and availability in product family (continued) 

|DCMRWD4[23]|PRAM2_FCCU_ALARM_EN|S32K358, S32K348, S32K338,<br>S32K328,|
|---|---|---|
|DCMRWD4[28]|SDHC_RDATA_EDC_ERR_EN|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWD4[31]|CM7_2_LOCKUP_EN|S32K358, S32K338,|
|DCMRWD5[14]|TCM_RDATA_EDC_ERR_EN|S32K344, S32K324, S32K314,<br>S32K342, S32K341, S32K322,|
|DCMRWD5[15]|EMAC_RDATA_EDC_ERR_EN|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|DCMRWD5[18]|CM7_1_AHBP_RDATA_EDC_ERR_EN|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD5[19]|CM7_1_AHBM_RDATA_EDC_ERR_EN|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD5[23]|CM7_2_AHBP_RDATA_EDC_ERR_EN|S32K358, S32K338,|
|DCMRWD5[24]|CM7_2_AHBM_RDATA_EDC_ERR_EN|S32K358, S32K338,|
|DCMRWD5[25]|CM7_2_DCDATA_ECC_ERR_EN|S32K358, S32K338,|
|DCMRWD5[26]|CM7_2_DCTAG_ECC_ERR_EN|S32K358, S32K338,|
|DCMRWD5[27]|CM7_2_ICDATA_ECC_ERR_EN|S32K358, S32K338,|
|DCMRWD5[28]|CM7_2_ICTAG_ECC_ERR_EN|S32K358, S32K338,|
|DCMRWD5[29]|CM7_2_ITCM_ECC_ERR_EN|S32K358, S32K338,|
|DCMRWD5[30]|CM7_2_DTCM0_ECC_ERR_EN|S32K358, S32K338,|
|DCMRWD5[31]|CM7_2_DTCM1_ECC_ERR_EN|S32K358, S32K338,|
|DCMRWD6[6]|eMIOS2_DBG_DIS_CM7_0|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314,|
|DCMRWD6[9]|SWT1_DBG_DIS_CM7_0|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD6[11]|STM1_DBG_DIS_CM7_0|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|DCMRWD6[14]|PIT2_DBG_DIS_CM7_0|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|DCMRWD6[19]|LPSPI4_DBG_DIS_CM7_0|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314,|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1069 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table 198. DCM controlled features and availability in product family (continued) 

|DCMRWD6[20]|LPSPI5_DBG_DIS_CM7_0|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314,|
|---|---|---|
|DCMRWD6[27]|FLEXCAN3_DBG_DIS_CM7_0|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322, S32K312,|
|DCMRWD6[28]|FLEXCAN4_DBG_DIS_CM7_0|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K312,|
|DCMRWD6[29]|FLEXCAN5_DBG_DIS_CM7_0|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K312,|
|DCMRWD6[30]|SAI0_DBG_DIS_CM7_0|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|DCMRWD6[31]|SAI1_DBG_DIS_CM7_0|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|DCMRWD7[0]|I3C0_DBG_DIS_CM7_0|S32K358, S32K348, S32K338,<br>S32K328, S32K342, S32K341,<br>S32K322, S32K312, S32K311,|
|DCMRWD7[1]|FLEXCAN6_DBG_DIS_CM7_0|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWD7[2]|FLEXCAN7_DBG_DIS_CM7_0|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWD7[3]|STM2_DBG_DIS_CM7_0|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWD7[4]|SWT2_DBG_DIS_CM7_0|S32K358, S32K338,|
|DCMRWD8[0]|EDMA_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD8[1]|FCCU_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD8[2]|LCU0_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD8[3]|LCU1_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD8[4]|eMIOS0_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD8[5]|eMIOS1_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,<br>S32K322,|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1070 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table 198. DCM controlled features and availability in product family (continued) 

|DCMRWD8[6]|eMIOS2_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,|
|---|---|---|
|DCMRWD8[7]|RTC_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD8[8]|SWT0_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD8[9]|SWT1_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD8[10]|STM0_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD8[11]|STM1_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD8[12]|PIT0_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD8[13]|PIT1_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD8[14]|PIT2_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD8[15]|LPSPI0_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD8[16]|LPSPI1_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD8[17]|LPSPI2_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD8[18]|LPSPI3_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD8[19]|LPSPI4_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,|
|DCMRWD8[20]|LPSPI5_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,|
|DCMRWD8[21]|LPI2C0_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD8[22]|LPI2C1_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD8[23]|FLEXIO_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD8[24]|FLEXCAN0_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD8[25]|FLEXCAN1_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD8[26]|FLEXCAN2_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,<br>S32K322,|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1071 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table 198. DCM controlled features and availability in product family (continued) 

|DCMRWD8[27]|FLEXCAN3_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,<br>S32K322,|
|---|---|---|
|DCMRWD8[28]|FLEXCAN4_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,|
|DCMRWD8[29]|FLEXCAN5_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,|
|DCMRWD8[30]|SAI0_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD8[31]|SAI1_DBG_DIS_CM7_1|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWD9[0]|I3C0_DBG_DIS_CM7_1|S32K338, S32K328, S32K322,|
|DCMRWD9[1]|FLEXCAN6_DBG_DIS_CM7_1|S32K338, S32K328,|
|DCMRWD9[2]|FLEXCAN7_DBG_DIS_CM7_1|S32K338, S32K328,|
|DCMRWD9[3]|STM2_DBG_DIS_CM7_1|S32K338, S32K328,|
|DCMRWD9[4]|SWT2_DBG_DIS_CM7_1|S32K338,|
|DCMRWD12[0]|EDMA_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[1]|FCCU_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[2]|LCU0_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[3]|LCU1_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[4]|eMIOS0_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[5]|eMIOS1_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[6]|eMIOS2_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[7]|RTC_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[8]|SWT0_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[9]|SWT1_DBG_DIS_CM7_2|S32K338,|
|DCMRWD12[10]|STM0_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[11]|STM1_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[12]|PIT0_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[13]|PIT1_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[14]|PIT2_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[15]|LPSPI0_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[16]|LPSPI1_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[17]|LPSPI2_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[18]|LPSPI3_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[19]|LPSPI4_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[20]|LPSPI5_DBG_DIS_CM7_2|S32K358, S32K338,|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1072 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table 198. DCM controlled features and availability in product family (continued) 

|DCMRWD12[21]|LPI2C0_DBG_DIS_CM7_2|S32K358, S32K338,|
|---|---|---|
|DCMRWD12[22]|LPI2C1_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[23]|FLEXIO_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[24]|FLEXCAN0_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[25]|FLEXCAN1_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[26]|FLEXCAN2_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[27]|FLEXCAN3_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[28]|FLEXCAN4_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[29]|FLEXCAN5_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[30]|SAI0_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD12[31]|SAI1_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD13[0]|I3C0_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD13[1]|FLEXCAN6_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD13[2]|FLEXCAN7_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD13[3]|STM2_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD13[4]|SWT2_DBG_DIS_CM7_2|S32K358, S32K338,|
|DCMRWD14[3]|QSPI_FLASHA_ECC_ERR_EN|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWD14[26]|AIPS0_GSKT_ALARM_EN|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWD14[30]|TCM_PRAM_AXBS_ALARM_EN|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWD15[11]|VDD1P1_GNG2_ERR_EN|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWD15[12]|VDD2P5_GNG2_ERR_EN|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWD15[28]|CM7_0_AHBS_ALARM_EN|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWD15[29]|CM7_1_AHBS_ALARM_EN|S32K338, S32K328,|
|DCMRWD15[30]|CM7_2_AHBS_ALARM_EN|S32K358, S32K338,|
|DCMRWD16[0]|PRAM0_GSKT_ALARM_EN|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWD16[1]|PRAM1_GSKT_ALARM_EN|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWD16[2]|PRAM2_TCM_GSKT_ALARM_EN|S32K358, S32K348, S32K338,<br>S32K328,|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1073 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table 198. DCM controlled features and availability in product family (continued) 

|DCMRWF1[0]|CAN_TIMESTAMP_SEL|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|---|---|---|
|DCMRWF1[1]|CAN_TIMESTAMP_EN|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|DCMRWF1[6]|EMAC_CONF_SEL|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWF1[7]||S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|DCMRWF1[11]|I3C0_CLK_MUX_SEL|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWF1[15]|VDD_HV_B_IO_CTRL_LATCH|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|DCMRWF1[19]|EMAC_SB_END_CTRL|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWF1[26]|VDD_HV_B_VLT_DVDR_EN|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|DCMRWF1[27]|VDD_1_5_VLT_DVDR_EN|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|DCMRWF2[8]|PMOS_CTRL_GPIO_DATA|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWF2[12]|SUPPLY2_MON_EN|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWF2[13]|SUPPLY2_MON_SEL|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWF2[14]||S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWF2[15]||S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWF2[24]|PLL1_LOL_RST_EN|S32K358, S32K348, S32K338,<br>S32K328,|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1074 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table 198. DCM controlled features and availability in product family (continued) 

|DCMRWF2[25]|WKPU0_SRC_SELECT|S32K358, S32K348, S32K338,<br>S32K328,|
|---|---|---|
|DCMRWF2[26]|WKPU14_SRC_SELECT|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWF2[27]|WKPU15_SRC_SELECT|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWF2[28]|WKPU18_SRC_SELECT|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWF2[29]|WKPU27_SRC_SELECT|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWF2[30]|WKPU45_SRC_SELECT|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWF2[31]|WKPU8_SRC_SELECT|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMRWF4[0]|MUX_MODE_EN_ADC1_S18|S32K311,|
|DCMRWF4[5]|MUX_MODE_EN_ADC1_S22|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322, S32K312,|
|DCMRWF4[6]|MUX_MODE_EN_ADC1_S23|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322, S32K312,|
|DCMRWF4[7]|MUX_MODE_EN_ADC0_S12|S32K311,|
|DCMRWF4[8]|MUX_MODE_EN_ADC0_S13|S32K311,|
|DCMRWF4[9]|MUX_MODE_EN_ADC2_S8|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314,|
|DCMRWF4[10]|MUX_MODE_EN_ADC2_S9|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314,|
|DCMRWF4[11]|MUX_MODE_EN_ADC0_S14|S32K311,|
|DCMRWF4[12]|MUX_MODE_EN_ADC0_S17|S32K311,|
|DCMRWF4[18]|CM7_1_CPUWAIT|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMRWF4[19]|CM7_2_CPUWAIT|S32K358, S32K338,|
|DCMROD3[1]|CM7_1_LOCKUP|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMROD3[3]|CM7_RCCU1_ALARM|S32K358, S32K348, S32K344,<br>S32K342, S32K341,|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1075 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table 198. DCM controlled features and availability in product family (continued) 

|DCMROD3[4]|CM7_RCCU2_ALARM|S32K358, S32K348, S32K344,<br>S32K342, S32K341,|
|---|---|---|
|DCMROD3[5]|TCM_GSKT_ALARM|S32K344, S32K324, S32K314,<br>S32K342, S32K341, S32K322,<br>S32K312, S32K311,|
|DCMROD3[6]|DMA_SYS_GSKT_ALARM|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|DCMROD3[7]|DMA_PERIPH_GSKT_ALARM|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|DCMROD3[9]|DMA_AXBS_ALARM|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|DCMROD3[10]|SDHC_GSKT_ALARM|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMROD3[12]|QSPI_GSKT_ALARM|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|DCMROD3[14]|AIPS2_GSKT_ALARM|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|DCMROD3[17]|TCM_AXBS_ALARM|S32K344, S32K324, S32K314,<br>S32K342, S32K341, S32K322,|
|DCMROD3[18]|EMAC_GSKT_ALARM|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|DCMROD3[19]|PERIPH_AXBS_ALARM|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|DCMROD3[20]|PF3_CODE_ECC_ERR|S32K358, S32K338,|
|DCMROD3[21]|PF3_DATA_ECC_ERR|S32K358, S32K338,|
|DCMROD3[23]|PRAM2_ECC_ERR|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMROD3[24]|PRAM1_ECC_ERR<br>Table continues on the next page...|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314,|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1076 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table 198. DCM controlled features and availability in product family (continued) 

|DCMROD3[27]|CM7_1_DCDATA_ECC_ERR|S32K338, S32K328, S32K324,<br>S32K322,|
|---|---|---|
|DCMROD3[29]|CM7_1_DCTAG_ECC_ERR|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMROD3[31]|CM7_1_ICDATA_ECC_ERR|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMROD4[1]|CM7_1_ICTAG_ECC_ERR|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMROD4[5]|CM7_1_ITCM_ECC_ERR|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K342, S32K341, S32K322,|
|DCMROD4[6]|CM7_1_DTCM0_ECC_ERR|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K342, S32K341, S32K322,|
|DCMROD4[7]|CM7_1_DTCM1_ECC_ERR|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K342, S32K341, S32K322,|
|DCMROD4[10]|PRAM1_FCCU_ALARM|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314,|
|DCMROD4[16]|PF2_CODE_ECC_ERR|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMROD4[17]|PF2_DATA_ECC_ERR|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMROD4[23]|PRAM2_FCCU_ALARM|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMROD4[28]|SDHC_RDATA_EDC_ERR|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMROD4[31]|CM7_2_LOCKUP|S32K358, S32K338,|
|DCMROD5[14]|TCM_RDATA_EDC_ERR|S32K344, S32K324, S32K314,<br>S32K342, S32K341, S32K322,|
|DCMROD5[15]|EMAC_RDATA_EDC_ERR|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|DCMROD5[18]|CM7_1_AHBP_RDATA_EDC_ERR|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMROD5[19]|CM7_1_AHBM_RDATA_EDC_ERR|S32K338, S32K328, S32K324,<br>S32K322,|
|DCMROD5[23]|CM7_2_AHBP_RDATA_EDC_ERR|S32K358, S32K338,|
|DCMROD5[24]|CM7_2_AHBM_RDATA_EDC_ERR<br>Table continues on the next page...|S32K358, S32K338,|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1077 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table 198. DCM controlled features and availability in product family (continued) 

|DCMROD5[25]|CM7_2_DCDATA_ECC_ERR|S32K358, S32K338,|
|---|---|---|
|DCMROD5[26]|CM7_2_DCTAG_ECC_ERR|S32K358, S32K338,|
|DCMROD5[27]|CM7_2_ICDATA_ECC_ERR|S32K358, S32K338,|
|DCMROD5[28]|CM7_2_ICTAG_ECC_ERR|S32K358, S32K338,|
|DCMROD5[29]|CM7_2_ITCM_ECC_ERR|S32K358, S32K338,|
|DCMROD5[30]|CM7_2_DTCM0_ECC_ERR|S32K358, S32K338,|
|DCMROD5[31]|CM7_2_DTCM1_ECC_ERR|S32K358, S32K338,|
|DCMROD6[3]|QSPI_FLASHA_ECC_ERR|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMROD6[26]|AIPS0_GSKT_ALARM|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMROD6[30]|TCM_PRAM_AXBS_ALARM|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMROD7[11]|VDD1P1_GNG2_ERR|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMROD7[12]|VDD2P5_GNG2_ERR|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMROD7[28]|CM7_0_AHBS_ALARM|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMROD7[29]|CM7_1_AHBS_ALARM|S32K338, S32K328,|
|DCMROD7[30]|CM7_2_AHBS_ALARM|S32K358, S32K338,|
|DCMROD8[0]|PRAM0_GSKT_ALARM|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMROD8[1]|PRAM1_GSKT_ALARM|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMROD8[2]|PRAM2_TCM_GSKT_ALARM|S32K358, S32K348, S32K338,<br>S32K328,|
|DCMROF1[0]|EMAC_MDC_CHID_0|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|DCMROF1[1]|EMAC_MDC_CHID_1|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|DCMROF19[29]|LOCKSTEP_EN|S32K358, S32K348, S32K344,<br>S32K342, S32K341,|
|DCMROF20[1]|LMAUTO_DIS|S32K344, S32K324, S32K314,<br>S32K342, S32K341, S32K322,|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1078 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table 198. DCM controlled features and availability in product family (continued) 

|DCMROF20[3]|DMA_AXBS_IAHB_BYP|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|
|---|---|---|
|DCMROF20[5]|QSPI_IAHB_BYP|S32K358, S32K348, S32K338,<br>S32K328, S32K344, S32K324,<br>S32K314, S32K342, S32K341,<br>S32K322,|



## 37.2 DCM_GPR register descriptions 

You must access DCM after at least 92 AIPS_SLOW_CLK cycles of writing to MC_RGM.ERCTRL because the configuration of MC_RGM.ERCTRL takes several cycles to be effective. Also, the DCMRWn registers are synchronized; therefore, changes to them may take up to four CORE_CLK cycles to be effective. 

The DCM read-only registers are present in standby domain and retain values across Standby mode. Therefore, reading the status registers after standby exit may indicate a previously latched value. To read these status registers after a reset event or standby exit, you must first clear them. This clears the previous status or transient information because of reset event, and specifies the correct status. 

~~<mark>NOTE</mark>~~ 

Do not write to reserved locations, including reserved registers and register fields. Chip behavior is not guaranteed in case of such writes. 

### 37.2.1 DCM_GPR memory map 

DCM_GPR base address: 402A_C000h 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|200h|Read Only GPR On Destructive Reset 1 (DCMROD1)|32|W1C|0000_0000h|
|208h|Read Only GPR On Destructive Reset 3 (DCMROD3)|32|W1C|0000_0000h|
|20Ch|Read Only GPR On Destructive Reset 4 (DCMROD4)|32|W1C|0000_0000h|
|210h|Read Only GPR On Destructive Reset 5 (DCMROD5)|32|W1C|0000_0000h|
|21Ch|Read Only GPR On Destructive Reset Register (DCMROD8)|32|W1C|0000_0000h|
|300h|Read Only GPR On Functional Reset 1 (DCMROF1)|32|W1C|0000_0000h|
|304h|Read Only GPR On Functional Reset 2 (DCMROF2)|32|W1C|0000_0000h|
|308h|Read Only GPR On Functional Reset 3 (DCMROF3)|32|W1C|0000_0000h|
|30Ch|Read Only GPR On Functional Reset 4 (DCMROF4)|32|W1C|0000_0000h|
|310h|Read Only GPR On Functional Reset 5 (DCMROF5)|32|W1C|0000_0000h|
|314h|Read Only GPR On Functional Reset 6 (DCMROF6)|32|W1C|0000_0000h|
|318h|Read Only GPR On Functional Reset 7 (DCMROF7)|32|W1C|0000_0000h|
|31Ch|Read Only GPR On Functional Reset 8 (DCMROF8)|32|W1C|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1079 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Offset|Register|Width<br>(In bits)|Access|Reset value|
|---|---|---|---|---|
|320h|Read Only GPR On Functional Reset 9 (DCMROF9)|32|W1C|0000_0000h|
|324h|Read Only GPR On Functional Reset 10 (DCMROF10)|32|W1C|0000_0000h|
|328h|Read Only GPR On Functional Reset 11 (DCMROF11)|32|W1C|0000_0000h|
|32Ch|Read Only GPR On Functional Reset 12 (DCMROF12)|32|W1C|0000_0000h|
|330h|Read Only GPR On Functional Reset 13 (DCMROF13)|32|W1C|0000_0000h|
|334h|Read Only GPR On Functional Reset 14 (DCMROF14)|32|W1C|0000_0000h|
|338h|Read Only GPR On Functional Reset 15 (DCMROF15)|32|W1C|0000_0000h|
|33Ch|Read Only GPR On Functional Reset 16 (DCMROF16)|32|W1C|0000_0000h|
|340h|Read Only GPR On Functional Reset 17 (DCMROF17)|32|W1C|0000_0000h|
|348h|Read Only GPR On Functional Reset 19 (DCMROF19)|32|RO|4000_0000h|
|34Ch|Read Only GPR On Functional Reset 20 (DCMROF20)|32|RO|See<br>description|
|350h|Read Only GPR On Functional Reset 21 (DCMROF21)|32|RO|0000_0000h|
|400h|Read Write GPR On POR 1 (DCMRWP1)|32|RW|0000_0400h|
|408h|Read Write GPR On POR 3 (DCMRWP3)|32|RW|0000_0000h|
|504h|Read Write GPR On Destructive Reset 2 (DCMRWD2)|32|RW|0000_0000h|
|508h|Read Write GPR On Destructive Reset 3 (DCMRWD3)|32|RW|FFFD_FFDFh|
|50Ch|Read Write GPR On Destructive Reset 4 (DCMRWD4)|32|RW|FFFF_FFFFh|
|510h|Read Write GPR On Destructive Reset 5 (DCMRWD5)|32|RW|FFFF_BFFFh|
|514h|Read Write GPR On Destructive Reset 6 (DCMRWD6)|32|RW|0000_0000h|
|518h|Read Write GPR On Destructive Reset 7 (DCMRWD7)|32|RW|0000_0000h|
|51Ch|Read Write GPR On Destructive Reset 8 (DCMRWD8)|32|RW|0000_0000h|
|520h|Read Write GPR On Destructive Reset 9 (DCMRWD9)|32|RW|0000_0000h|
|52Ch|Read Write GPR On Destructive Reset 12 (DCMRWD12)|32|RW|0000_0000h|
|530h|Read Write GPR On Destructive Reset 13 (DCMRWD13)|32|RW|0000_0000h|
|538h|Read Write GPR On Destructive Reset 16 (DCMRWD16)|32|RW|F000_0000h|
|600h|Read Write GPR On Functional Reset 1 (DCMRWF1)|32|RW|0000_0000h|
|604h|Read Write GPR On Functional Reset 2 (DCMRWF2)|32|RW|0000_0000h|
|608h|Read Write GPR On Functional Reset 3 (DCMRWF3)|32|RW|0000_0000h|
|60Ch|Read Write GPR On Functional Reset 4 (DCMRWF4)|32|RW|0000_0000h|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1080 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Offset|Register|Width|Access|Reset value|
|---|---|---|---|---|
|||(In bits)|||
|610h|Read Write GPR On Functional Reset 5 (DCMRWF5)|32|RW|See<br>description|
|700h|Read Only GPR On PMCPOR Reset 1 (DCMROPP1)|32|W1C|0000_0000h|
|704h|Read Only GPR On PMCPOR Reset 2 (DCMROPP2)|32|W1C|0000_0000h|
|708h|Read Only GPR On PMCPOR Reset 3 (DCMROPP3)|32|W1C|0000_0000h|
|70Ch|Read Only GPR On PMCPOR Reset 4 (DCMROPP4)|32|W1C|0000_0000h|



### 37.2.2 Read Only GPR On Destructive Reset 1 (DCMROD1) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROD1|200h|



#### Function 

Resets on destructive reset 1. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1081-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>KEY_R HSE_ PCU_I<br>R Reserved<br>ES... DCF... SO...<br>W W1C W1C W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-3<br>—|Reserved|
|2|Key Response Ready Status|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1081 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|KEY_RESP_RE<br>ADY|Specifies the SDA-AP key response status, whether the SDA-AP all key values are written to and<br>HSE_B can begin authentication.<br>0b - Key response not ready<br>1b - Key response ready|
|1|DCF Violation From HSE_B|
|HSE_DCF_VIO|Specifies whether a violation occurred from HSE_B DCF records while decoding.<br>0b - No<br>1b - Yes|
|0|PCU Input Isolation Status On Previous Standby Entry|
|PCU_ISO_STA<br>TUS|Specifies whether input isolation is enabled in the previous standby entry.<br>0b - No<br>1b - Yes|



### 37.2.3 Read Only GPR On Destructive Reset 3 (DCMROD3) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROD3|208h|



Function 

Resets on destructive reset 3. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|CM7_1<br>_I...|CM7_0<br>_I...|CM7_1<br>_D...|CM7_0<br>_D...|CM7_1<br>_D...|CM7_0<br>_D...|PRAM<br>0_E...|PRAM<br>1_E...|PRAM<br>2_E...|LC_<br>ERR|PF3_D<br>AT...|PF3_C<br>OD...|PERIP<br>H_...|EMAC<br>_GS...|TCM_<br>AXB...|DATA_<br>ED...|
|W|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|ADDR<br>_ED...|AIPS2<br>_G...|AIPS1<br>_G...|QSPI_<br>GS...|HSE_<br>GSK...|SDHC<br>_GS...|DMA_<br>AXB...|SYS_A<br>XB...|DMA_<br>PER...|DMA_<br>SYS...|TCM_<br>GSK...|CM7_<br>RCC...|CM7_<br>RCC...|HSE_L<br>OC...|CM7_1<br>_L...|CM7_0<br>_L...|
|W|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1082 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Fields 

|Field|Function|
|---|---|
|31|Cortex-M7_1 I-Cache Multi-Bit Error|
|CM7_1_ICDAT<br>A_ECC_ERR|Specifies whether the Cortex-M7_1 core's I-cache data memory detected a multi-bit ECC error.<br>Read this field to identify the reason of fault in case of FCCU NCF 2.<br>0b - No<br>1b - Yes|
|30<br>CM7_0_ICDAT<br>A_ECC_ERR|Cortex-M7_0 I-cache Data Memory<br>Specifies whether the Cortex-M7_0 core's I-cache data memory detected a multi-bit ECC error.<br>Read this field to identify the reason of fault in case of FCCU NCF 2.<br>0b - No<br>1b - Yes|
|29<br>CM7_1_DCTAG<br>_ECC_ERR|Cortex-M7_1 D-cache Tag ECC Error<br>Specifies whether the Cortex-M7_1 core's D-cache tag memory detected a multi-bit ECC error.<br>Read this field to identify the reason of fault in case of FCCU NCF 2.<br>0b - No<br>1b - Yes|
|28|Cortex-M7_0 D-cache Tag ECC Error|
|CM7_0_DCTAG<br>_ECC_ERR|Specifies whether the Cortex-M7_0 core's D-cache tag memory detected a multi-bit ECC error.<br>Read this field to identify the reason of fault in case of FCCU NCF 2.<br>0b - No<br>1b - Yes|
|27|Cortex-M7_1 D-cache Data Memory ECC Error|
|CM7_1_DCDAT<br>A_ECC_ERR|Specifies whether the Cortex-M7_1 core's D-cache data memory detected a multi-bit ECC error.<br>Read this field to identify the reason of fault in case of FCCU NCF 2.<br>0b - No<br>1b - Yes|
|26|Cortex-M7_0 D-cache Data Memory ECC Error|
|CM7_0_DCDAT<br>A_ECC_ERR|Specifies whether the Cortex-M7_0 core's D-cache data memory detected a multi-bit ECC error.<br>Read this field to identify the reason of fault in case of FCCU NCF 2.<br>0b - No<br>1b - Yes|
|25|Multi-Bit ECC Error From PRAM0<br>Specifies whether a multi-bit ECC error occurred from PRAM0.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1083 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|PRAM0_ECC_E<br>RR|Read this field to identify the reason of fault in case of FCCU NCF 2.<br>0b - No<br>1b - Yes|
|24<br>PRAM1_ECC_E<br>RR|Multi-Bit ECC Error From PRAM1<br>Specifies whether a multi-bit ECC error occurred from PRAM1.<br>Read this field to identify the reason of fault in case of FCCU NCF 2.<br>0b - No<br>1b - Yes|
|23<br>PRAM2_ECC_E<br>RR|Multi bit ECC error from SRAM2. Read this bit to identify the reason of fault in case of FCCU NCF 2.<br>0b - No multi-bit ECC error.<br>1b - Multi-bit ECC error.|
|22<br>LC_ERR|Error In Lifecycle Scanning<br>Specifies whether an error occurred during lifecycle scanning.<br>0b - No<br>1b - Yes|
|21|Program Flash Memory 3 Data ECC Uncorrectable Error|
|PF3_DATA_EC<br>C_ERR|Specifies whether FMU reported an uncorrectable error in the flash memory controller port 3 data memory.<br>The errors are reported from FMU and are connected to FCCU NCFs. These are also connected to ERM.<br>See the "Error Reporting Module (ERM)" chapter for memory errors and mapping onto ERM channels. Read<br>this field to identify the reason of fault in case of FCCU NCF 3. The path is from FMU to PFLASH controller,<br>and then from ERM to FCCU.<br>0b - No<br>1b - Yes|
|20|Flash Memory 3 Code ECC Uncorrectable Error|
|PF3_CODE_EC<br>C_ERR|Specifies whether FMU reported uncorrectable errors in the flash memory controller port 3 code memory.<br>The errors are reported from FMU and are connected to FCCU NCFs. These are also connected to ERM.<br>See the "Error Reporting Module (ERM)" chapter for memory errors and mapping onto ERM channels. Read<br>this field to identify the reason of fault in case of FCCU NCF 3. The path is from FMU to PFLASH controller,<br>and then from ERM to FCCU.<br>0b - No<br>1b - Yes|
|19<br>PERIPH_AXBS<br>_ALARM|Peripheral AXBS_Lite Safety Alarm Status<br>Specifies whether peripheral AXBS_Lite reported a safety alarm.<br>Read this field to identify the reason of fault in case of FCCU NCF 1.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1084 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - No<br>1b - Yes|
|18<br>EMAC_GSKT_<br>ALARM|EMAC IAHB Gasket Alarm Status<br>Specifies whether the EMAC IAHB gasket reported an alarm.<br>Read this field to identify the reason of fault in case of FCCU NCF 1.<br>0b - No<br>1b - Yes|
|17|TCM AHB Splitter Safety Alarm Status|
|TCM_AXBS_AL<br>ARM|Specifies whether the TCM AHB splitter reported a safety alarm.<br>Read this field to identify the reason of fault in case of FCCU NCF 1.<br>0b - No<br>1b - Yes|
|16|Data EDC Error|
|DATA_EDC_ER<br>R|Specifies whether an EDC error on data, for safety, occurred.<br>Read this field to identify the reason of fault in case of FCCU NCF 1.<br>0b - No<br>1b - Yes|
|15<br>ADDR_EDC_E<br>RR|Address EDC Error Status<br>Specifies whether an address EDC error, for safety, occurred .<br>Read this field to identify the reason of fault in case of FCCU NCF 1.<br>0b - No<br>1b - Yes|
|14|AIPS2 IAHB Gasket Alarm Status. Read this bit to identify the reason of fault in case of FCCU NCF 1.|
|AIPS2_GSKT_A<br>LARM|0b - No alarm indicated by AIPS2 IAHB gasket.<br>1b - Alarm indicated by AIPS2 IAHB gasket.|
|13|AIPS1 IAHB Gasket Alarm Status. Read this bit to identify the reason of fault in case of FCCU NCF 1.|
|AIPS1_GSKT_A<br>LARM|0b - No alarm indicated by AIPS1 IAHB gasket.<br>1b - Alarm indicated by AIPS1 IAHB gasket.|
|12|QuadSPI IAHB Gasket Alarm Status|
|QSPI_GSKT_A|Specifies whether the QuadSPI IAHB gasket reported an alarm.|
|LARM|Read this field to identify the reason of fault in case of FCCU NCF 1.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1085 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function<br>0b - No<br>1b - Yes|
|---|---|
|11<br>HSE_GSKT_AL<br>ARM|HSE IAHB Gasket Alarm Status<br>Specifies whether the HSE_B IAHB gasket reported an alarm.<br>Read this field to identify the reason of fault in case of FCCU NCF 1.<br>0b - No<br>1b - Yes|
|10|uSDHC IASHB Gasket Alarm Status. Read this bit to identify the reason of fault in case of FCCU NCF 1.|
|SDHC_GSKT_A<br>LARM|0b - No alarm indicated by uSDHC IAHB gasket.<br>1b - Alarm indicated by uSDHC IAHB gasket.|
|9|eDMA AXBS_Lite Safety Alarm Status|
|DMA_AXBS_AL<br>ARM|Specifies whether eDMA AXBS_Lite reported a safety alarm.<br>Read this field to identify the reason of fault in case of FCCU NCF 1.<br>0b - No<br>1b - Yes|
|8|System AXBS Safety Alarm Status|
|SYS_AXBS_AL<br>ARM|Specifies whether the system AXBS indicated a safety alarm.<br>Read this field to identify the reason of fault in case of FCCU NCF 1.<br>0b - No<br>1b - Yes|
|7|eDMA Peripheral Gasket Alarm Status|
|DMA_PERIPH_<br>GSKT_ALARM|Specifies the status of the IAHB gasket safety alarm from the eDMA peripheral AXBS IAHB gasket, whether<br>the eDMA peripheral AXBS IAHB gasket reported a safety alarm.<br>Read this field to identify the reason of fault in case of FCCU NCF 1.<br>0b - No<br>1b - Yes|
|6|eDMA System Gasket Alarm Status|
|DMA_SYS_GS<br>KT_ALARM|Specifies the status of the IAHB gasket safety alarm from the eDMA system AXBS IHAB gasket, whether<br>it reported a safety alarm.<br>Read this field to identify the reason of fault in case of FCCU NCF 1.<br>0b - No<br>1b - Yes|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1086 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|5|TCM IAHB Gasket Monitor Alarm Status|
|TCM_GSKT_AL<br>ARM|Specifies whether the TCM IAHB gasket reported an alarm. If the value of this field is 1, the gasket reports<br>a monitor alarm.<br>Read this field to identify the reason of fault in case of FCCU NCF 1.<br>0b - No<br>1b - Yes|
|4<br>CM7_RCCU2_A<br>LARM|Cortex-M7 Core Redundant Lockstep Error Status<br>Specifies whether RCCU reported a lockstep alarm.<br>Read this field to identify the reason of fault in case of FCCU NCF 0.<br>0b - No<br>1b - Yes|
|3|Cortex-M7 Core Lockstep Error Status|
|CM7_RCCU1_A<br>LARM|Specifies whether RCCU reported a lockstep alarm.<br>Read this field to identify the reason of fault in case of FCCU NCF 0.<br>0b - No<br>1b - Yes|
|2<br>HSE_LOCKUP|HSE_B Core Lockup Status<br>Specifies whether the HSE_B core is in the Lockup state.<br>Read this field to identify the reason of fault in case of FCCU NCF 0.<br>0b - No<br>1b - Yes|
|1<br>CM7_1_LOCKU<br>P|Cortex-M7_1 Core Lockup Status<br>Specifies whether the Cortex_M7_1 core is in the Lockup state.<br>Read this field to identify the reason of fault in case of FCCU NCF 0.<br>0b - No<br>1b - Yes|
|0<br>CM7_0_LOCKU<br>P|Cortex-M7_0 Core Lockup Status<br>Specifies whether the Cortex-M7_0 core is in the Lockup state.<br>Read this field to identify the reason of fault in case of FCCU NCF 0.<br>0b - No<br>1b - Yes|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1087 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

### 37.2.4 Read Only GPR On Destructive Reset 4 (DCMROD4) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROD4|20Ch|



#### Function 

Resets on destructive reset 4. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|Reserv<br>ed|TEST_<br>AC...|TEST_<br>AC...|SDHC<br>_RD...|VDD2<br>P5_...|VDD1<br>P1_...|Reserv<br>ed|FLAS<br>H_A...|PRAM<br>2_F...|FLAS<br>H_S...|FLAS<br>H_R...|FLAS<br>H_R...|FLAS<br>H_A...|FLAS<br>H_E...|PF2_D<br>AT...|PF2_C<br>OD...|
|W|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|PF1_D<br>AT...|PF1_C<br>OD...|PF0_D<br>AT...|PF0_C<br>OD...|HSE_<br>RAM...|PRAM<br>1_F...|PRAM<br>0_F...|DMA_<br>TCD...|CM7_1<br>_D...|CM7_1<br>_D...|CM7_1<br>_I...|CM7_0<br>_D...|CM7_0<br>_D...|CM7_0<br>_I...|CM7_1<br>_I...|CM7_0<br>_I...|
|W|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31|Reserved|
|—<br>30|Accidental Partial Test Activation 1 Error|
|TEST_ACTIVA<br>TION_1_ERR|Specifies whether the partial test is activated accidentally.<br>Read this field to identify the reason of fault in case of FCCU NCF 5.<br>0b - No|
||1b - Yes|
|29|Accidental Partial Test Activation 0 Error|
|TEST_ACTIVA<br>TION_0_ERR|Specifies whether the partial test is activated accidentally.<br>Read this field to identify the reason of fault in case of FCCU NCF 5.<br>0b - No<br>1b - Yes|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1088 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|28<br>SDHC_RDATA_<br>EDC_ERR|EDC(EDC) error on uSDHC read data for safety. Read this bit to identify the reason of fault in case of<br>FCCU NCF 1.<br>0b - No EDC error reported on uSDHC read data.<br>1b - EDC error reported on uSDHC read data.|
|27<br>VDD2P5_GNG_<br>ERR|Go/No-Go Indicator For VDD_HV_FLA<br>Specifies whether the VDD_HV_FLA (double-bond) supply going to XOSC and PLL is clean.<br>Read this field to identify the reason of fault in case of FCCU NCF 4.<br>If this field is 1, the "go" indication specifies a clean supply, and if this field is 0, the "no-go" indication<br>specifies an unclean supply with a fault in the double-bond connection or its routing within the chip.<br>0b - Yes<br>1b - No|
|26<br>VDD1P1_GNG_<br>ERR|Go/No-Go Indicator For VDD1PD1<br>Specifies whether the VDD1PD1 (double-bond) supply going to PLL is clean.<br>Read this field to identify the reason of fault in case of FCCU NCF 4.<br>If this field is 1, the "go" indication specifies a clean supply, and if this field is 0, the "no-go" indication<br>specifies an unclean supply with a fault in the double-bond connection or its routing within the chip.<br>0b - Yes<br>1b - No|
|25<br>—|Reserved|
|24|Transaction Monitor Mismatch Error From Flash Memory Controller|
|FLASH_ACCES<br>S_ERR|Specifies whether the flash memory controller detected a transaction monitor mismatch when compared to<br>the flash memory safety feedback output.<br>There is an indication in the flash memory to compare a reconstructed address with the address that invoked<br>flash memory access.<br>Read this field to identify the reason of fault in case of FCCU NCF 3.<br>0b - No<br>1b - Yes|
|23<br>PRAM2_FCCU_<br>ALARM|Status of PRAM2 safety alarm. This alarm is set on faulty SRAM2 read or read modify error. Read this<br>bit to identify the reason of fault in case of FCCU NCF 2.<br>0b - No safety alarm indicated by PRAM2.<br>1b - Safety alarm indicated by PRAM2.|
|22|Flash Memory Scan Error Status|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1089 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|FLASH_SCAN_<br>ERR|Specifies whether the flash memory encountered an error during the DCM flash scanning process because<br>of invalid data.<br>Read this field to identify the reason of fault in case of FCCU NCF 3.<br>0b - No<br>1b - Yes|
|21<br>FLASH_RST_E<br>RR|Flash Reset Error Status<br>Specifies whether the flash memory encountered a flash memory reset error during its reset reads.<br>Read this field to identify the reason of fault in case of FCCU NCF 3.<br>0b - No<br>1b - Yes|
|20|Flash Memory Reference Error Status|
|FLASH_REF_E<br>RR|Specifies whether the flash memory encountered a reference current loss or read voltage error during<br>previous read(s).<br>Read this field to identify the reason of fault in case of FCCU NCF 3.<br>0b - No<br>1b - Yes|
|19|Flash Memory Address Encode Error Status|
|FLASH_ADDR_<br>ENC_ERR|Specifies whether FMU reported an address encode error in the flash memory.<br>During address decoding, if multiple or no address line is selected, FMU reports an address encode error.<br>Read this field to identify the reason of fault in case of FCCU NCF 3.<br>0b - No<br>1b - Yes|
|18<br>FLASH_EDC_E<br>RR|Flash Memory EDC Error Status<br>Specifies whether FMU reported EDC after an ECC correction error in the flash memory.<br>Read this field to identify the reason of fault in case of FCCU NCF 3.<br>0b - No<br>1b - Yes|
|17<br>PF2_DATA_EC<br>C_ERR|Program Flash Memory 2 Data ECC Error Status<br>Specifies whether FMU reported uncorrectable errors in the flash memory controller port 2 data memory.<br>These errors are connected to FCCU NCFs and to ERM. See the "Error Reporting Module (ERM)" chapter<br>for memory errors and mapping onto ERM channels.<br>Read this field to identify the reason of fault in case of FCCU NCF 3.<br>0b - No<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1090 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function<br>1b - Yes|
|---|---|
|16|Program Flash Memory 2 Code ECC Error Status|
|PF2_CODE_EC<br>C_ERR|Specifies whether FMU reported uncorrectable errors in the flash memory controller port 2 code memory.<br>These errors are connected to FCCU NCFs and to ERM. See the "Error Reporting Module (ERM)" chapter<br>for memory errors and mapping onto ERM channels.<br>Read this field to identify the reason of fault in case of FCCU NCF 3.<br>0b - No<br>1b - Yes|
|15|Program Flash Memory 1 Data ECC Error Status|
|PF1_DATA_EC<br>C_ERR|Specifies whether FMU reported uncorrectable errors in the flash memory controller port 1 data memory.<br>These errors are connected to FCCU NCFs and to ERM. See the "Error Reporting Module (ERM)" chapter<br>for memory errors and mapping onto ERM channels.<br>Read this field to identify the reason of fault in case of FCCU NCF 3.<br>0b - No<br>1b - Yes|
|14|Program Flash Memory 1 Code ECC Error Status|
|PF1_CODE_EC<br>C_ERR|Specifies whether FMU reported uncorrectable errors in the flash memory controller port 1 code memory.<br>These errors are connected to FCCU NCFs and to ERM. See the "Error Reporting Module (ERM)" chapter<br>for memory errors and mapping onto ERM channels.<br>Read this field to identify the reason of fault in case of FCCU NCF 3.<br>0b - No<br>1b - Yes|
|13|Program Flash Memory 0 Data ECC Error Status|
|PF0_DATA_EC<br>C_ERR|Specifies whether FMU reported uncorrectable errors in the flash memory controller port 0 data memory.<br>These errors are connected to FCCU NCFs and to ERM. See the "Error Reporting Module (ERM)" chapter<br>for memory errors and mapping onto ERM channels.<br>Read this field to identify the reason of fault in case of FCCU NCF 3.<br>0b - No<br>1b - Yes|
|12|Program Flash Memory 0 Code ECC Error Status|
|PF0_CODE_EC<br>C_ERR|Specifies whether FMU reported uncorrectable errors in the flash memory controller port 0 code memory.<br>These errors are connected to FCCU NCFs and to ERM. See the "Error Reporting Module (ERM)" chapter<br>for memory errors and mapping onto ERM channels.<br>Read this field to identify the reason of fault in case of FCCU NCF 3.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1091 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - No<br>1b - Yes|
|11<br>HSE_RAM_EC<br>C_ERR|HSE_B RAM Uncorrectable ECC Status<br>Specifies whether HSE_B RAM reported an uncorrectable ECC error.<br>Read this field to identify the reason of fault in case of FCCU NCF 2.<br>0b - No<br>1b - Yes|
|10<br>PRAM1_FCCU_<br>ALARM|PRAM1 FCCU Alarm Status<br>Specifies whether PRAM1 reported a safety alarm.<br>This field specifies the status of the PRAM1 safety alarm, whether the alarm is set on faulty PRAM1 read<br>or read-modify error. Read this field to identify the reason of fault in case of FCCU NCF 2.<br>0b - No<br>1b - Yes|
|9<br>PRAM0_FCCU_<br>ALARM|PRAM0 FCCU Alarm Status<br>Specifies whether PRAM0 reported a safety alarm.<br>This field specifies the status of the PRAM0 safety alarm, whether the alarm is set on faulty PRAM0 read<br>or read-modify error. Read this field to identify the reason of fault in case of FCCU NCF 2.<br>0b - No<br>1b - Yes|
|8<br>DMA_TCD_RA<br>M_ECC_ERR|eDMA TCD RAM ECC Error<br>Specifies whether the eDMA_TCD memory detected an uncorrectable ECC error.<br>This uncorrectable ECC error consists of a multi-bit data ECC error and an address ECC error. Read this<br>field to identify the reason of fault in case of FCCU NCF 2.<br>0b - No<br>1b - Yes|
|7|Cortex-M7_1 DTCM 1 ECC Error|
|CM7_1_DTCM1<br>_ECC_ERR|Specifies whether the Cortex-M7_1 core's DTCM block 1 detected an uncorrectable ECC error.<br>This uncorrectable ECC error consists of a multi-bit data ECC error and an address ECC error. The<br>Cortex-M7_1 core's DTCM consists of two physical blocks. Read this field to identify the reason of fault in<br>case of FCCU NCF 2.<br>The Cortex-M7_1 core's DTCM 1 does not support address ECC errors in S32K324,<br>S32K344, and S32K314.<br>~~NOTE~~|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1092 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1093-03.png)


<!-- Start of picture text -->
Field Function<br>0b - No<br>1b - Yes<br>6 Cortex-M7_1 DTCM 0 ECC Error<br>CM7_1_DTCM0 Specifies whether the Cortex-M7_1 core's DTCM block 0 detected an uncorrectable ECC error.<br>_ECC_ERR<br>This uncorrectable ECC error consists of a multi-bit data ECC error and an address ECC error. The<br>Cortex-M7_1 core's DTCM consists of two physical blocks. Read this field to identify the reason of fault in<br>case of FCCU NCF 2.<br>  NOTE<br>The Cortex-M7_1 core's DTCM 0 does not support address ECC errors in S32K324,<br>S32K344, and S32K314.<br>0b - No<br>1b - Yes<br>5 Cortex-M7_1 ITCM ECC Error<br>CM7_1_ITCM_ Specifies whether the Cortex-M7_1 core's ITCM detected an uncorrectable ECC error.<br>ECC_ERR<br>This uncorrectable ECC error consists of a multi-bit data ECC error and an address ECC error. Read this<br>field to identify the reason of fault in case of FCCU NCF 2.<br>  NOTE<br>The Cortex-M7_1 core's ITCM does not support address ECC errors in S32K324, S32K344,<br>and S32K314.<br>0b - No<br>1b - Yes<br>4 Cortex-M7_0 DTCM 1 ECC Error<br>CM7_0_DTCM1 Specifies whether the Cortex-M7_0 core's DTCM block 1 detected an uncorrectable ECC error.<br>_ECC_ERR<br>This uncorrectable ECC error consists of a multi-bit data ECC error and an address ECC error. The<br>Cortex-M7_0 core's DTCM consists of two physical blocks. Read this field to identify the reason of fault in<br>case of FCCU NCF 2.<br>  NOTE<br>The Cortex-M7_0 core's DTCM 1 does not support address ECC errors in S32K324,<br>S32K344, and S32K314.<br>0b - No<br>1b - Yes<br>3 Cortex-M7_0 DTCM 0 ECC Error<br>CM7_0_DTCM0 Specifies whether the Cortex-M7_0 core's DTCM block 0 detected an uncorrectable ECC error.<br>_ECC_ERR<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1093 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||This uncorrectable ECC error consists of a multi-bit data ECC error and an address ECC error. The<br>Cortex-M7_0 core's DTCM consists of two physical blocks. Read this field to identify the reason of fault in<br>case of FCCU NCF 2.<br>The Cortex-M7_0 core's DTCM 0 does not support address ECC errors in S32K324,<br>S32K344, and S32K314.<br>~~NOTE~~|
||0b - No<br>1b - Yes|
|2<br>CM7_0_ITCM_<br>ECC_ERR|Cortex-M7_0 ITCM ECC Error<br>Specifies whether the Cortex-M7_0 core's ITCM detected an uncorrectable ECC error.<br>This uncorrectable ECC error consists of a multi-bit data ECC error and an address ECC error. Read this<br>field to identify the reason of fault in case of FCCU NCF 2.<br>The Cortex-M7_0 core's ITCM does not support address ECC errors in S32K324, S32K344,<br>and S32K314.<br>~~NOTE~~|
||0b - No<br>1b - Yes|
|1<br>CM7_1_ICTAG_<br>ECC_ERR|Cortex-M7_1 I-cache Tag ECC Error<br>Specifies whether the Cortex-M7_1 core's I-cache tag memory detected a multi-bit ECC error.<br>Read this field to identify the reason of fault in case of FCCU NCF 2.<br>0b - No<br>1b - Yes|
|0<br>CM7_0_ICTAG_<br>ECC_ERR|Cortex-M7_0 I-cache Tag ECC Error<br>Specifies whether the Cortex-M7_0 core's I-cache tag memory detected a multi-bit ECC error.<br>Read this field to identify the reason of fault in case of FCCU NCF 2.<br>0b - No<br>1b - Yes|



### 37.2.5 Read Only GPR On Destructive Reset 5 (DCMROD5) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROD5|210h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1094 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Function 

#### Resets on destructive reset 5. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|CM7_2<br>_D...|CM7_2<br>_D...|CM7_2<br>_I...|CM7_2<br>_I...|CM7_2<br>_I...|CM7_2<br>_D...|CM7_2<br>_D...|CM7_2<br>_A...|CM7_2<br>_A...|HSE_<br>RDA...|CM7_0<br>_A...|CM7_0<br>_A...|CM7_1<br>_A...|CM7_1<br>_A...|DMA_<br>RDA...|Reserv<br>ed|
|W|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|EMAC<br>_RD...|TCM_<br>RDA...|DEBU<br>G_A...|MTR_<br>BUS...|STCU<br>_BI...|MBIST<br>_A...|STCU<br>_NCF|SW_N<br>CF_3|SW_N<br>CF_2|SW_N<br>CF_1|SW_N<br>CF_0|INTM_<br>3_...|INTM_<br>2_...|INTM_<br>1_...|INTM_<br>0_...|Reserv<br>ed|
|W|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31|Cortex-M7_2 DTCM 1 ECC Error|
|CM7_2_DTCM1<br>_ECC_ERR|Specifies whether the Cortex-M7_2 core's DTCM block 1 detected an uncorrectable ECC error.<br>This uncorrectable ECC error consists of a multi-bit data ECC error and an address ECC error. The<br>Cortex-M7_2 core's DTCM consists of two physical blocks. Read this field to identify the reason of fault in<br>case of FCCU NCF 2.|
||The Cortex-M7_2 core's DTCM 1 does not support address ECC errors in S32K324,<br>S32K344, and S32K314.<br>~~NOTE~~|
||0b - No<br>1b - Yes|
|30|Cortex-M7_2 DTCM 0 ECC Error|
|CM7_2_DTCM0<br>_ECC_ERR|Specifies whether the Cortex-M7_2 core's DTCM block 0 detected an uncorrectable ECC error.<br>This uncorrectable ECC error consists of a multi-bit data ECC error and an address ECC error. The<br>Cortex-M7_2 core's DTCM consists of two physical blocks. Read this field to identify the reason of fault in<br>case of FCCU NCF 2.|
||The Cortex-M7_2 core's DTCM 0 does not support address ECC errors in S32K324,<br>S32K344, and S32K314.<br>~~NOTE~~|
||0b - No|
||1b - Yes|
|29|Cortex-M7_2 ITCM ECC Error|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1095 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|CM7_2_ITCM_<br>ECC_ERR|Specifies whether the Cortex-M7_2 core's ITCM detected an uncorrectable ECC error.<br>This uncorrectable ECC error consists of a multi-bit data ECC error and an address ECC error. Read this<br>field to identify the reason of fault in case of FCCU NCF 2.<br>The Cortex-M7_2 core's ITCM does not support address ECC errors in S32K324, S32K344,<br>and S32K314.<br>~~NOTE~~<br>0b - No<br>1b - Yes|
|28<br>CM7_2_ICTAG_<br>ECC_ERR|Cortex-M7_2 I-cache Tag ECC Error<br>Specifies whether the Cortex-M7_2 core's I-cache tag memory reported a multi-bit ECC error.<br>Read this field to identify the reason of fault in case of FCCU NCF 2.<br>0b - No<br>1b - Yes|
|27<br>CM7_2_ICDAT<br>A_ECC_ERR|Cortex-M7_2 I-cache Data ECC Error<br>Specifies whether the Cortex-M7_2 core's I-cache data memory reported a multi-bit ECC error.<br>Read this field to identify the reason of fault in case of FCCU NCF 2.<br>0b - No<br>1b - Yes|
|26<br>CM7_2_DCTAG<br>_ECC_ERR|Cortex-M7_2 D-cache Tag ECC Error<br>Specifies whether the Cortex-M7_2 core's D-cache tag memory detected a multi-bit ECC error.<br>Read this field to identify the reason of fault in case of FCCU NCF 2.<br>0b - No<br>1b - Yes|
|25<br>CM7_2_DCDAT<br>A_ECC_ERR|Cortex-M7_2 D-cache Data ECC Error<br>Specifies whether the Cortex-M7_2 core's D-cache data memory detected a multi-bit ECC error.<br>Read this field to identify the reason of fault in case of FCCU NCF 2.<br>0b - No<br>1b - Yes|
|24|Cortex-M7_2 AHBM Read Data EDC Error|
|CM7_2_AHBM_<br>RDATA_EDC_E<br>RR|Specifies whether an EDC error is reported on the Cortex-M7_2 core's main read data for safety.<br>Read this field to identify the reason of fault in case of FCCU NCF 1.<br>0b - No<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1096 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function<br>1b - Yes|
|---|---|
|23<br>CM7_2_AHBP_<br>RDATA_EDC_E<br>RR|Cortex-M7_2 AHBP Read Data EDC Error<br>Specifies whether an EDC error is reported on the Cortex-M7_2 core's peripheral read data for safety.<br>Read this field to identify the reason of fault in case of FCCU NCF 1.<br>0b - No<br>1b - Yes|
|22<br>HSE_RDATA_E<br>DC_ERR|HSE_B Read Data EDC Error<br>Specifies whether an EDC error is reported on HSE_B read data for safety.<br>Read this field to identify the reason of fault in case of FCCU NCF 1.<br>0b - No<br>1b - Yes|
|21|Cortex-M7_0 AHBM Read Data EDC Error|
|CM7_0_AHBM_<br>RDATA_EDC_E<br>RR|Specifies whether an EDC error is reported on the Cortex-M7_0 core's main read data for safety.<br>Read this field to identify the reason of fault in case of FCCU NCF 1.<br>0b - No<br>1b - Yes|
|20<br>CM7_0_AHBP_<br>RDATA_EDC_E<br>RR|Cortex-M7_0 AHBP Read Data EDC Error<br>Specifies whether an EDC error is reported on the Cortex-M7_0 core's peripheral read data for safety.<br>Read this field to identify the reason of fault in case of FCCU NCF 1.<br>0b - No<br>1b - Yes|
|19<br>CM7_1_AHBM_<br>RDATA_EDC_E<br>RR|Cortex-M7_1 AHBM Read Data EDC Error<br>Specifies whether an EDC error is reported on the Cortex-M7_1 core's main read data for safety.<br>Read this field to identify the reason of fault in case of FCCU NCF 1.<br>0b - No<br>1b - Yes|
|18<br>CM7_1_AHBP_<br>RDATA_EDC_E<br>RR|Cortex-M7_1 AHBP Read Data EDC Error<br>Specifies whether an EDC error is reported on the Cortex-M7_1 core's peripheral read data for safety.<br>Read this field to identify the reason of fault in case of FCCU NCF 1.<br>0b - No<br>1b - Yes<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1097 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|17|eDMA Read Data EDC Error|
|DMA_RDATA_<br>EDC_ERR|Specifies whether an EDC error is reported on eDMA read data for safety.<br>Read this field to identify the reason of fault in case of FCCU NCF 1.<br>0b - No<br>1b - Yes|
|16<br>—|Reserved|
|15<br>EMAC_RDATA<br>_EDC_ERR|EMAC Read Data EDC Error<br>Specifies whether an EDC error is reported on EMAC read data for safety.<br>Read this field to identify the reason of fault in case of FCCU NCF 1.<br>0b - No<br>1b - Yes|
|14<br>TCM_RDATA_E<br>DC_ERR|TCM Read Data EDC Error<br>Specifies whether an EDC error is reported on TCM read data for safety.<br>Read this field to identify the reason of fault in case of FCCU NCF 1.<br>0b - No<br>1b - Yes|
|13|Debug Activation Error|
|DEBUG_ACTIV<br>ATION_ERR|Specifies whether an unintended debug is activated.<br>This field monitors unintended debug activation. The field displays 1 as its value when the core is in halted<br>state with the application debug or debugger request not enabled. Read this field to identify the reason of<br>fault in case of FCCU NCF 5.<br>0b - No<br>1b - Yes|
|12<br>MTR_BUS_ER<br>R|MTR Bus Error<br>Specifies whether MTR reported a transfer error.<br>A fault is reported because of illegal access to MTR. This fault is reported via a transfer error indication to<br>the system. Read this field to identify the reason of fault in case of FCCU NCF 5.<br>0b - No<br>1b - Yes|
|11|STCU2 BIST User CF|
|STCU_BIST_U<br>SER_CF|Specifies whether LBIST or MBIST is enabled accidentally when the fault condition is detected in<br>Run mode .<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1098 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||Read this field to identify the reason of fault in case of FCCU NCF 5.<br>0b - No<br>1b - Yes|
|10|MBIST Activation Error|
|MBIST_ACTIVA<br>TION_ERR|Specifies whether an accidental backdoor access is enabled on memories.<br>DCMRWD5[MBIST_ACTIVATION_ERR_EN] needs to be disabled on FCCU when performing a<br>fault injection.<br>Read this field to identify the reason of fault in case of FCCU NCF 5.<br>0b - No<br>1b - Yes|
|9<br>STCU_NCF|STCU2 NCF Result Error<br>Specifies whether STCU2 NCF, which is BIST result error, is reported.<br>Read this field to identify the reason of fault in case of FCCU NCF 5.<br>0b - No<br>1b - Yes|
|8<br>SW_NCF_3|Software NCF3 Status<br>Specifies whether DCMRWF1[FCCU_SW_NCF3] is enabled.<br>Read this field to identify the reason of fault in case of FCCU NCF 7.<br>0b - No<br>1b - Yes|
|7<br>SW_NCF_2|Software NCF2 Status<br>Specifies whether DCMRWF1[FCCU_SW_NCF2] is enabled.<br>Read this field to identify the reason of fault in case of FCCU NCF 7.<br>0b - No<br>1b - Yes|
|6<br>SW_NCF_1|Software NCF1 Status<br>Specifies whether DCMRWF1[FCCU_SW_NCF1] is enabled.<br>Read this field to identify the reason of fault in case of FCCU NCF 7.<br>0b - No<br>1b - Yes|
|5|Software NCF 0 Status|
|SW_NCF_0|Specifies whether DCMRWF1[FCCU_SW_NCF0] is enabled.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1099 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||Read this field to identify the reason of fault in case of FCCU NCF 7.<br>0b - No<br>1b - Yes|
|4<br>INTM_3_ERR|INTM_3 Error<br>Specifies whether INTM_3 reported an error.<br>The reported error reflects in INTM.INTM_STATUS3. See the "Functional description" section of the<br>"Interrupt Monitor (INTM)" chapter for details.<br>Read this field to identify the reason of fault in case of FCCU NCF 6.<br>0b - No<br>1b - Yes|
|3<br>INTM_2_ERR|INTM_2 Error<br>Specifies whether INTM_2 reported an error.<br>The reported error reflects in INTM.INTM_STATUS2. See the "Functional description" section of the<br>"Interrupt Monitor (INTM)" chapter for details.<br>Read this field to identify the reason of fault in case of FCCU NCF 6.<br>0b - No<br>1b - Yes|
|2<br>INTM_1_ERR|INTM_1 Error<br>Specifies whether INTM_1 reported an error.<br>The reported error reflects in INTM.INTM_STATUS1. See the "Functional description" section of the<br>"Interrupt Monitor (INTM)" chapter for details.<br>Read this field to identify the reason of fault in case of FCCU NCF 6.<br>0b - No<br>1b - Yes|
|1<br>INTM_0_ERR|INTM_0 Error<br>Specifies whether INTM_0 reported an error.<br>The reported error reflects in INTM.INTM_STATUS0. See the "Functional description" section of the<br>"Interrupt Monitor (INTM)" chapter for details.<br>Read this field to identify the reason of fault in case of FCCU NCF 6.<br>0b - No<br>1b - Yes|
|0<br>—|Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1100 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

### 37.2.6 Read Only GPR On Destructive Reset Register (DCMROD8) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROD8|21Ch|



#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||Rese|rved||||||||
|W||||||||W|1C||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||Rese|rved||||||PRAM<br>2_G...|PRAM<br>2_T...|PRAM<br>1_G...|PRAM<br>0_G...|
|W||||||W1|C||||||W1C|W1C|W1C|W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-4<br>—|Reserved|
|3<br>PRAM2_GSKT_<br>ALARM|PRAM2 IAHB Gasket monitor alarm status. Read this bit to identify the reason of fault in case of FCCU<br>NCF 1.<br>0b - No alarm reported from PRAM2 IAHB gasket.<br>1b - Monitor alarm reported from PRAM2 IAHB gasket.|
|2<br>PRAM2_TCM_<br>GSKT_ALARM|PRAM2_TCM IAHB Gasket monitor alarm status. Read this bit to identify the reason of fault in case of<br>FCCU NCF 1.<br>0b - No alarm reported from PRAM2_TCM IAHB gasket.<br>1b - Monitor alarm reported from PRAM2_TCM IAHB gasket.|
|1<br>PRAM1_GSKT_<br>ALARM|PRAM1 IAHB Gasket monitor alarm status. Read this bit to identify the reason of fault in case of FCCU<br>NCF 1.<br>0b - No alarm reported from PRAM1 IAHB gasket.<br>1b - Monitor alarm reported from PRAM1 IAHB gasket.|
|0<br>PRAM0_GSKT_<br>ALARM|PRAM0 IAHB Gasket monitor alarm status. Read this bit to identify the reason of fault in case of FCCU<br>NCF 1.<br>0b - No alarm reported from PRAM0 IAHB gasket.<br>1b - Monitor alarm reported from PRAM0 IAHB gasket.|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1101 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

### 37.2.7 Read Only GPR On Functional Reset 1 (DCMROF1) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROF1|300h|



#### Function 

Resets on functional reset 1. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||Rese|rved||||||||
|W||||||||W|1C||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||||Rese|rved|||||||EMAC<br>_MD...|EMAC<br>_MD...|
|W|||||||W1|C|||||||W1C|W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-2|Reserved|
|—||
|1|EMAC eDMA Channel ID1 Status|
|EMAC_MDC_C<br>HID_1|Specifies whether channel ID1 is the current transfer channel ID.<br>0b - No|
||1b - Yes|
|0|EMAC eDMA Channel ID0 Status|
|EMAC_MDC_C<br>HID_0|Specifies whether channel ID0 is the current transfer channel ID.<br>0b - No<br>1b - Yes|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1102 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

### 37.2.8 Read Only GPR On Functional Reset 2 (DCMROF2) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROF2|304h|



#### Function 

#### Resets on functional reset 2. 

This register specifies the SDID0 contents that DCM scans from the flash memory. 

~~<mark>NOTE</mark>~~ 

See the DCF clients file attached to this document for more information. The DCF clients in the Utest sector contain chip-configurable ID information, captured as status on read-only GPR in functional reset. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||||DCF_|SDID0||||||||
|W||||||||W|1C||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R||||||||DCF_|SDID0||||||||
|W||||||||W|1C||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-0|DCF Client SDID 0 Configuration|
|DCF_SDID0||



### 37.2.9 Read Only GPR On Functional Reset 3 (DCMROF3) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROF3|308h|



#### Function 

Resets on functional reset 3. 

This register specifies the SDID1 contents that DCM scans from the flash memory. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1103 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

~~<mark>NOTE</mark>~~ 

See the DCF clients file attached to this document for more information. The DCF clients in the Utest sector contain chip-configurable ID information, captured as status on read-only GPR in functional reset. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1104-05.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R DCF_SDID1<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DCF_SDID1<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-0|DCF Client SDID 1 Configuration|
|DCF_SDID1||



### 37.2.10 Read Only GPR On Functional Reset 4 (DCMROF4) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROF4|30Ch|



#### Function 

#### Resets on functional reset 4. 

This register specifies the SDID2 contents that DCM scans from the flash memory. 

~~<mark>NOTE</mark>~~ 

See the DCF clients file attached to this document for more information. The DCF clients in the Utest sector contain chip-configurable ID information, captured as status on read-only GPR in functional reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1104 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1105-01.png)


<!-- Start of picture text -->
Device Configuration Module General-Purpose Registers (DCM_GPR)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R DCF_SDID2<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DCF_SDID2<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Diagram 

#### Fields 

|Field|Function|
|---|---|
|31-0|DCF Client SDID 2 Configuration|
|DCF_SDID2||



### 37.2.11 Read Only GPR On Functional Reset 5 (DCMROF5) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROF5|310h|



#### Function 

Resets on functional reset 5. 

This register specifies the SDID3 contents that DCM scans from the flash memory. 

~~<mark>NOTE</mark>~~ 

See the DCF clients file attached to this document for more information. The DCF clients in the Utest sector contain chip-configurable ID information, captured as status on read-only GPR in functional reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1105 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1106-01.png)


<!-- Start of picture text -->
Device Configuration Module General-Purpose Registers (DCM_GPR)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R DCF_SDID3<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DCF_SDID3<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Diagram 

#### Fields 

|Field|Function|
|---|---|
|31-0|DCF Client SDID 3 Configuration|
|DCF_SDID3||



### 37.2.12 Read Only GPR On Functional Reset 6 (DCMROF6) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROF6|314h|



#### Function 

Resets on functional reset 6. 

This register specifies the SDID4 contents that DCM scans from the flash memory. 

~~<mark>NOTE</mark>~~ 

See the DCF clients file attached to this document for more information. The DCF clients in the Utest sector contain chip-configurable ID information, captured as status on read-only GPR in functional reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1106 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1107-01.png)


<!-- Start of picture text -->
Device Configuration Module General-Purpose Registers (DCM_GPR)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R DCF_SDID4<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DCF_SDID4<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Diagram 

#### Fields 

|Field|Function|
|---|---|
|31-0|DCF Client SDID 4 Configuration|
|DCF_SDID4||



### 37.2.13 Read Only GPR On Functional Reset 7 (DCMROF7) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROF7|318h|



#### Function 

Resets on functional reset 7. 

This register specifies the SDID5 contents that DCM scans from the flash memory. 

~~<mark>NOTE</mark>~~ 

See the DCF clients file attached to this document for more information. The DCF clients in the Utest sector contain chip-configurable ID information, captured as status on read-only GPR in functional reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1107 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1108-01.png)


<!-- Start of picture text -->
Device Configuration Module General-Purpose Registers (DCM_GPR)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R DCF_SDID5<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DCF_SDID5<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Diagram 

#### Fields 

|Field|Function|
|---|---|
|31-0|DCF Client SDID 5 Configuration|
|DCF_SDID5||



### 37.2.14 Read Only GPR On Functional Reset 8 (DCMROF8) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROF8|31Ch|



#### Function 

Resets on functional reset 8. 

This register specifies the SDID6 contents that DCM scans from the flash memory. 

~~<mark>NOTE</mark>~~ 

See the DCF clients file attached to this document for more information. The DCF clients in the Utest sector contain chip-configurable ID information, captured as status on read-only GPR in functional reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1108 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1109-01.png)


<!-- Start of picture text -->
Device Configuration Module General-Purpose Registers (DCM_GPR)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R DCF_SDID6<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DCF_SDID6<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Diagram 

#### Fields 

|Field|Function|
|---|---|
|31-0|DCF Client SDID 6 Configuration|
|DCF_SDID6||



### 37.2.15 Read Only GPR On Functional Reset 9 (DCMROF9) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROF9|320h|



#### Function 

Resets on functional reset 9. 

This register specifies the SDID7 contents that DCM scans from the flash memory. 

~~<mark>NOTE</mark>~~ 

See the DCF clients file attached to this document for more information. The DCF clients in the Utest sector contain chip-configurable ID information, captured as status on read-only GPR in functional reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1109 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1110-01.png)


<!-- Start of picture text -->
Device Configuration Module General-Purpose Registers (DCM_GPR)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R DCF_SDID7<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DCF_SDID7<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Diagram 

#### Fields 

|Field|Function|
|---|---|
|31-0|DCF Client SDID 7 Configuration|
|DCF_SDID7||



### 37.2.16 Read Only GPR On Functional Reset 10 (DCMROF10) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROF10|324h|



#### Function 

Resets on functional reset 10. 

This register specifies the SDID8 contents that DCM scans from the flash memory. 

~~<mark>NOTE</mark>~~ 

See the DCF clients file attached to this document for more information. The DCF clients in the Utest sector contain chip-configurable ID information, captured as status on read-only GPR in functional reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1110 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1111-01.png)


<!-- Start of picture text -->
Device Configuration Module General-Purpose Registers (DCM_GPR)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R DCF_SDID8<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DCF_SDID8<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Diagram 

#### Fields 

|Field|Function|
|---|---|
|31-0|DCF Client SDID 8 Configuration|
|DCF_SDID8||



### 37.2.17 Read Only GPR On Functional Reset 11 (DCMROF11) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROF11|328h|



#### Function 

Resets on functional reset 11. 

This register specifies the SDID9 contents that DCM scans from the flash memory. 

~~<mark>NOTE</mark>~~ 

See the DCF clients file attached to this document for more information. The DCF clients in the Utest sector contain chip-configurable ID information, captured as status on read-only GPR in functional reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1111 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1112-01.png)


<!-- Start of picture text -->
Device Configuration Module General-Purpose Registers (DCM_GPR)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R DCF_SDID9<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DCF_SDID9<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Diagram 

#### Fields 

|Field|Function|
|---|---|
|31-0|DCF Client SDID 9 Configuration|
|DCF_SDID9||



### 37.2.18 Read Only GPR On Functional Reset 12 (DCMROF12) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROF12|32Ch|



#### Function 

Resets on functional reset 12. 

This register specifies the SDID10 contents that DCM scans from the flash memory. 

~~<mark>NOTE</mark>~~ 

See the DCF clients file attached to this document for more information. The DCF clients in the Utest sector contain chip-configurable ID information, captured as status on read-only GPR in functional reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1112 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1113-01.png)


<!-- Start of picture text -->
Device Configuration Module General-Purpose Registers (DCM_GPR)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R DCF_SDID10<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DCF_SDID10<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Diagram 

#### Fields 

|Field|Function|
|---|---|
|31-0|DCF Client SDID 10 Configuration|
|DCF_SDID10||



### 37.2.19 Read Only GPR On Functional Reset 13 (DCMROF13) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROF13|330h|



#### Function 

Resets on functional reset 13. 

This register specifies the SDID11 contents that DCM scans from the flash memory. 

~~<mark>NOTE</mark>~~ 

See the DCF clients file attached to this document for more information. The DCF clients in the Utest sector contain chip-configurable ID information, captured as status on read-only GPR in functional reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1113 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1114-01.png)


<!-- Start of picture text -->
Device Configuration Module General-Purpose Registers (DCM_GPR)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R DCF_SDID11<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DCF_SDID11<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Diagram 

#### Fields 

|Field|Function|
|---|---|
|31-0|DCF Client SDID 11 Configuration|
|DCF_SDID11||



### 37.2.20 Read Only GPR On Functional Reset 14 (DCMROF14) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROF14|334h|



#### Function 

Resets on functional reset 14. 

This register specifies the SDID12 contents that DCM scans from the flash memory. 

~~<mark>NOTE</mark>~~ 

See the DCF clients file attached to this document for more information. The DCF clients in the Utest sector contain chip-configurable ID information, captured as status on read-only GPR in functional reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1114 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1115-01.png)


<!-- Start of picture text -->
Device Configuration Module General-Purpose Registers (DCM_GPR)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R DCF_SDID12<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DCF_SDID12<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Diagram 

#### Fields 

|Field|Function|
|---|---|
|31-0|DCF Client SDID 12 Configuration|
|DCF_SDID12||



### 37.2.21 Read Only GPR On Functional Reset 15 (DCMROF15) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROF15|338h|



#### Function 

Resets on functional reset 15. 

This register specifies the SDID13 contents that DCM scans from the flash memory. 

~~<mark>NOTE</mark>~~ 

See the DCF clients file attached to this document for more information. The DCF clients in the Utest sector contain chip-configurable ID information, captured as status on read-only GPR in functional reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1115 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1116-01.png)


<!-- Start of picture text -->
Device Configuration Module General-Purpose Registers (DCM_GPR)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R DCF_SDID13<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DCF_SDID13<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Diagram 

#### Fields 

|Field|Function|
|---|---|
|31-0|DCF Client SDID 13 Configuration|
|DCF_SDID13||



### 37.2.22 Read Only GPR On Functional Reset 16 (DCMROF16) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROF16|33Ch|



#### Function 

Resets on functional reset 16. 

This register specifies the SDID14 contents that DCM scans from the flash memory. 

~~<mark>NOTE</mark>~~ 

See the DCF clients file attached to this document for more information. The DCF clients in the Utest sector contain chip-configurable ID information, captured as status on read-only GPR in functional reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1116 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1117-01.png)


<!-- Start of picture text -->
Device Configuration Module General-Purpose Registers (DCM_GPR)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R DCF_SDID14<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DCF_SDID14<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Diagram 

#### Fields 

|Field|Function|
|---|---|
|31-0|DCF Client SDID 14 Configuration|
|DCF_SDID14||



### 37.2.23 Read Only GPR On Functional Reset 17 (DCMROF17) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROF17|340h|



#### Function 

Resets on functional reset 17. 

This register specifies the SDID15 contents that DCM scans from the flash memory. 

~~<mark>NOTE</mark>~~ 

See the DCF clients file attached to this document for more information. The DCF clients in the Utest sector contain chip-configurable ID information, captured as status on read-only GPR in functional reset. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1117 / 4640 

NXP Semiconductors 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1118-01.png)


<!-- Start of picture text -->
Device Configuration Module General-Purpose Registers (DCM_GPR)<br>Diagram<br>Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R DCF_SDID15<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DCF_SDID15<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Diagram 

#### Fields 

|Field|Function|
|---|---|
|31-0|DCF Client SDID 15 Configuration|
|DCF_SDID15||



### 37.2.24 Read Only GPR On Functional Reset 19 (DCMROF19) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROF19|348h|



#### Function 

Resets on functional reset 19. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1118-11.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>FCCU DCM_ LOCK<br>R Reserved<br>_EO... DONE  STE...<br>W<br>Reset 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1118 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Fields 

|Field|Function|
|---|---|
|31<br>FCCU_EOUT_<br>DEDICATED|FCCU EOUT Status<br>Specifies the status of FCCU_EOUT pins on GPIO_2 and GPIO_3 as configured in the DCF record,<br>UTEST_MISC[FCCU_EOUT_DEDICATED].<br>0b - General purpose, supporting all functions<br>1b - Dedicated EOUT pins|
|30<br>DCM_DONE|Flash Memory Scanning Status<br>Specifies the status of flash memory scanning by DCM.<br>0b - Incomplete<br>1b - Complete|
|29<br>LOCKSTEP_EN|Lockstep Enable<br>Specifies the current chip operation mode as configured in the DCF record,<br>UTEST_MISC[LOCKSTEP_EN].<br>0b - Decoupled operation of Cortex-M7_0 and Cortex-M7_1<br>1b - Lockstep operation of Cortex-M7_0 and Cortex-M7_1|
|28-0<br>—|Reserved|



### 37.2.25 Read Only GPR On Functional Reset 20 (DCMROF20) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROF20|34Ch|



#### Function 

#### Resets on functional reset 20. 

This register specifies the information of chip destructive reset escalation support for destructive reset sources as configured in the DCF record, DEST_RST_ESC[13:0]. See the DCF clients file attached to this document for the mapping of corresponding destructive reset events. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1119 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1120-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>Reserv Reserv<br>R DCF_DEST_RST_ESC<br>ed  ed<br>W<br>Reset u 1 u u u u u u u u u u u u u 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>POR_<br>AIPS_I QSPI_I Reserv DMA_ Reserv LMAU<br>R Reserved  Reserved  WDG..<br>A... A... ed  AXB... ed  TO_...<br>.<br>W<br>Reset 0 0 0 0 0 0 0 0 0 u 2 u 1 0 u 2 0 u 1 u 1<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1120-04.png)


<!-- Start of picture text -->
1. The reset value of this register is dependent on the DCF client's default value.<br><!-- End of picture text -->


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1120-05.png)


<!-- Start of picture text -->
2. The reset value of this register is dependent on DCF client default value.<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-18|DCF Destructive Reset Escalation|
|DCF_DEST_RS<br>T_ESC|Enables the destructive reset escalation feature for the corresponding destructive reset event.<br>00_0000_0000_0000b - Disables<br>00_0000_0000_0001b - Enables|
|17<br>—|Reserved|
|16<br>—|Reserved|
|15-12<br>—|Reserved|
|11-7<br>—|Reserved|
|6<br>AIPS_IAHB_BY<br>P|Status of AIPS1/2 IAHB gasket as configured in DCF record, UTEST_MISC[AIPS_IAHB_BYP].<br>0b - Register wall enabled.<br>1b - Register wall bypassed.|
|5|QuadSPI IAHB Bypass Status|
|QSPI_IAHB_BY<br>P|Specifies the status of the QuadSPI IAHB gasket as configured in the DCF record,<br>UTEST_MISC[QSPI_IAHB_BYP].|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1120 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Register wall enabled<br>1b - Register wall bypassed|
|4<br>—<br>3|Reserved<br>Status of DMA AXBS IAHB gasket as configured in DCF record, UTEST_MISC[DMA_AXBS_IAHB_BYP].|
|DMA_AXBS_IA<br>HB_BYP|0b - Register wall enabled.<br>1b - Register wall bypassed.|
|2<br>—|Reserved|
|1<br>LMAUTO_DIS|Last Mile Auto Support<br>Specifies whether the PMC last-mile automatic crossover from the boot regulation feature is supported<br>for the chip.<br>0b - Yes<br>1b - No|
|0<br>POR_WDG_EN|POR Watchdog (POR_WDG) Status<br>Specifies the status of POR_WDG as configured in the DCF record, UTEST_MISC[POR_WDG_EN]. The<br>POR_WDG is enabled by default.<br>0b - Disabled<br>1b - Enabled|



### 37.2.26 Read Only GPR On Functional Reset 21 (DCMROF21) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROF21|350h|



#### Function 

Resets on functional reset 21 and specifies the information of chip destructive reset escalation support for destructive reset sources as configured in the DCF record, DEST_RST_ESC[31:14]. 

See the DCF clients file attached to this document for the mapping of corresponding destructive reset events. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1121 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R||||||Reserved||||||HSE_CL<br>E_O|K_MOD<br>P...|Reserv<br>ed|DCF_DE<br>T_E|ST_RS<br>SC|
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|||||||DC|F_DEST|_RST_ES|C|||||||
|W|||||||||||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-21|Reserved|
|—||
|20-19|HSE_B Clock Mode Option|
|HSE_CLK_MO<br>DE_OPTION|Specifies the applicable clocking options.<br>• If the value of this field is 0b, the ratio of 1:2 between the HSE_B IPS interface clock<br>(AIPS_SLOW_CLK), HSE_B module clock (HSE_CLK), and HSE_IAHB gasket is enabled.<br>• If the value of this field is 1b, the ratio of 1:2 between the HSE_B IPS interface clock<br>(AIPS_SLOW_CLK), HSE_B module clock (HSE_CLK), and HSE_IAHB gasket is bypassed.<br>• If the value of this field is 10b or 11b, the ratio of 1:4 between the HSE_B IPS interface clock<br>(AIPS_SLOW_CLK), HSE_B module clock (HSE_CLK), and HSE_IAHB gasket is enabled.<br>00b - Option A<br>01b - Options C, D, E, E2, and F<br>10b - Option B<br>11b - Option B|
|18|Reserved|
|—<br>17-0|DCF Destructive Reset Escalation|
|DCF_DEST_RS<br>T_ESC|Enables the destructive reset escalation feature for the corresponding destructive reset event.<br>00_0000_0000_0000_0000b - Disables|
||00_0000_0000_0000_0001b - Enables|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1122 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

### 37.2.27 Read Write GPR On POR 1 (DCMRWP1) 

#### Offset 

|Register|Offset|
|---|---|
|DCMRWP1|400h|



Function Resets on POR 1. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||Rese|rved||||Rese|rved|||Reser|ved|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|||Reserved|||POR_W<br>RI|DOG_T<br>M|STAN<br>BDY...|Reserv<br>ed|Reserv<br>ed|Rese|rved|CLKO<br>UT_...|Rese|rved|Reserv<br>ed|
|Reset|0|0|0|0|0|1|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-24<br>—|Reserved|
|23-22<br>—|Reserved|
|21-11<br>—|Reserved|
|10-9<br>POR_WDOG_T<br>RIM|POR_WDG Trim<br>Specifies the trims for the POR_WDG timeout value.<br>00b - POR_WDG timeout = 06.25 ms<br>01b - POR_WDG timeout = 12.50 ms<br>10b - POR_WDG timeout = 25.00 ms<br>11b - POR_WDG timeout = 50.00 ms|
|8|Standby POR_WDG Disable<br>Disables the standby entry and exit monitoring window of POR_WDG.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1123 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|STANBDY_PW<br>DOG_DIS|0b - Enables<br>1b - Disables|
|7<br>—|Reserved|
|6<br>—|Reserved|
|5-4<br>—|Reserved|
|3<br>CLKOUT_STAN<br>DBY|Clockout Standby Expose Over Functional And Destructive Reset<br>Specifies whether the CLKOUT_STANDBY function is available during functional or destructive reset<br>on PTA12.<br>This field controls the CLKOUT_STANDBY function availability during functional or destructive reset<br>on PTA12.<br>0b - No<br>1b - Yes|
|2-1<br>—|Reserved|
|0<br>—|Reserved|



### 37.2.28 Read Write GPR On POR 3 (DCMRWP3) 

#### Offset 

|Register|Offset|
|---|---|
|DCMRWP3|408h|



Function 

Resets on POR 3. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1124 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1125-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R DEST_<br>Reserved  Reserved<br>W RS...<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-10<br>—|Reserved|
|9|Destructive Reset 9|
|DEST_RST9_A<br>S_IPI|Configures a destructive reset to interrupt.<br>0b - Destructive reset|
||1b - PLL LOL interrupt|
|8-0<br>—|Reserved|



### 37.2.29 Read Write GPR On Destructive Reset 2 (DCMRWD2) 

#### Offset 

|Register|Offset|
|---|---|
|DCMRWD2|504h|



Function Resets on destructive reset 2. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1125 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||||Res|erved||||||||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||Rese|rved||||EOUT<br>_ST...|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-8|Reserved|
|—<br>7<br>EOUT_STAT_D<br>UR_STEST|Controls the EOUT state during self-test. If this field is 0, the EOUT state changes to high Z post self-test<br>when the chip is under reset, and if this field is 1, the EOUT state remains in Fault state until the field<br>becomes 0.<br>0b - Changes to high Z<br>1b - Remains in Fault state|
|6<br>—|Reserved|
|5<br>—|Reserved|
|4<br>—|Reserved|
|3<br>—<br>2<br>—<br>1<br>—|Reserved<br>Reserved<br>Reserved|
|0<br>—|Reserved|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1126 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

### 37.2.30 Read Write GPR On Destructive Reset 3 (DCMRWD3) 

#### Offset 

|Register|Offset|
|---|---|
|DCMRWD3|508h|



#### Function 

Includes fault disable fields and resets on destructive reset. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|CM7_1<br>_I...|CM7_0<br>_I...|CM7_1<br>_D...|CM7_0<br>_D...|CM7_1<br>_D...|CM7_0<br>_D...|PRAM<br>0_E...|PRAM<br>1_E...|PRAM<br>2_E...|LC_ER<br>R_...|PF3_D<br>AT...|PF3_C<br>OD...|PERIP<br>H_...|EMAC<br>_GS...|TCM_<br>AXB...|DATA_<br>ED...|
|Reset|1|1|1|1|1|1|1|1|1|1|1|1|1|1|0|1|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|ADDR<br>_ED...|AIPS2<br>_G...|AIPS1<br>_G...|QSPI_<br>GS...|HSE_<br>GSK...|SDHC<br>_GS...|DMA_<br>AXB...|SYS_A<br>XB...|DMA_<br>PER...|DMA_<br>SYS...|TCM_<br>GSK...|CM7_<br>RCC...|CM7_<br>RCC...|Reserv<br>ed|CM7_1<br>_L...|CM7_0<br>_L...|
|Reset|1|1|1|1|1|1|1|1|1|1|0|1|1|1|1|1|



#### Fields 

|Field|Function|
|---|---|
|31|Cortex-M7_1 I-cache ECC Error Enable|
|CM7_1_ICDAT<br>A_ECC_ERR_E<br>N|Specifies whether the Cortex-M7_1 core's I-cache data memory detected a multi-bit ECC error.<br>The field enables fault monitoring at FCCU noncritical fault (NCF) 2 for this: multi-bit ECC error from the<br>Cortex-M7_1 core's I-cache data memory.<br>0b - No|
||1b - Yes|
|30|Cortex-M7_0 I-cache ECC Error Enable|
|CM7_0_ICDAT<br>A_ECC_ERR_E<br>N|Specifies whether the Cortex-M7_0 core's I-cache data memory detected a multi-bit ECC error.<br>The field enables fault monitoring at FCCU NCF 2 for this fault: multi-bit ECC error from the Cortex-M7_0<br>core's I-cache data memory.<br>0b - No<br>1b - Yes|
|29|Cortex-M7_1 D-cache Tag ECC Error Enable|
|CM7_1_DCTAG<br>_ECC_ERR_EN|Specifies whether the Cortex-M7_1 core's D-cache tag memory detected a multi-bit ECC error.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1127 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function<br>The field enables fault monitoring at FCCU NCF 2 for this fault: multi-bit ECC error from the Cortex-M7_1<br>core's D-cache tag memory.<br>0b - No<br>1b - Yes|
|---|---|
|28|Cortex-M7_0 D-cache Tag ECC Error Enable|
|CM7_0_DCTAG<br>_ECC_ERR_EN|Specifies whether the Cortex-M7_0 core's D-cache tag memory detected a multi-bit ECC error.<br>The field enables fault monitoring at FCCU NCF 2 for this fault: multi-bit ECC error from the Cortex-M7_0<br>core's D-cache tag memory.<br>0b - No<br>1b - Yes|
|27|Cortex-M7_1 D-cache Data ECC Error Enable|
|CM7_1_DCDAT<br>A_ECC_ERR_E<br>N|Specifies whether the Cortex-M7_1 core's D-cache data memory detected a multi-bit ECC error.<br>The field enables fault monitoring at FCCU NCF 2 for this fault: multi-bit ECC error from the Cortex-M7_1<br>core's D-cache data memory.<br>0b - No<br>1b - Yes|
|26|Cortex-M7_0 D-cache Data ECC Error Enable|
|CM7_0_DCDAT<br>A_ECC_ERR_E<br>N|Specifies whether the Cortex-M7_0 core's D-cache data memory detected a multi-bit ECC error.<br>The field enables fault monitoring at FCCU NCF 2 for this fault: multi-bit ECC error from the Cortex-M7_0<br>core's D-cache data memory.<br>0b - No<br>1b - Yes|
|25<br>PRAM0_ECC_E<br>RR_EN|PRAM0 ECC Error Enable<br>Specifies whether a multi-bit ECC error occurred from PRAM0.<br>The field enables fault monitoring at FCCU NCF 2 for this fault: multi-bit ECC error from PRAM0.<br>0b - No<br>1b - Yes|
|24<br>PRAM1_ECC_E<br>RR_EN|PRAM1 ECC Error Enable<br>Specifies whether a multi-bit ECC error occurred from PRAM1.<br>The field enables fault monitoring at FCCU NCF 2 for this fault: multi-bit ECC error from PRAM1.<br>0b - No<br>1b - Yes|
|23|Enable bit for enabling the fault monitoring at FCCU NCF 2 for the fault: Multi bit ECC error from SRAM1.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1128 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|PRAM2_ECC_E<br>RR_EN|0b - No multi-bit ECC error.<br>1b - Multi-bit ECC error.|
|22<br>LC_ERR_EN|Lifecycle Scanning Error Enable<br>Specifies whether an error is encountered during lifecycle scanning.<br>The field enables fault monitoring at FCCU NCF 3 for this fault: error in lifecycle scanning.|
||On any POR or destructive reset event, because this field becomes 0, the field has no effect.<br>A lifecycle error (in case it is present) is not disabled.<br>~~NOTE~~|
||0b - No<br>1b - Yes|
|21|Program Flash Memory 3 Data ECC Error Enable|
|PF3_DATA_EC<br>C_ERR_EN|Specifies whether FMU reported an uncorrectable error in flash memory controller port 3 data memory.<br>The field enables fault monitoring at FCCU NCF 3 for this fault: program flash memory 3 data ECC<br>uncorrectable error. The path is from FMU to PFLASH controller and then ERM to FCCU.<br>0b - No<br>1b - Yes|
|20|Program Flash Memory 3 Code ECC Error Enable|
|PF3_CODE_EC<br>C_ERR_EN|Specifies whether FMU reported an uncorrectable error in the flash memory controller port 3 code memory.<br>The field enables fault monitoring at FCCU NCF 3 for this fault: program flash memory 3 code ECC<br>uncorrectable error. The path is from FMU to PFLASH controller and then ERM to FCCU.<br>0b - No<br>1b - Yes|
|19|Peripheral AXBS Alarm Enable|
|PERIPH_AXBS<br>_ALARM_EN|Specifies whether peripheral AXBS_Lite reported a safety alarm.<br>The field enables sbit for enabling fault monitoring at FCCU NCF 1 for this fault: peripheral AXBS_Lite<br>safety alarm.<br>0b - No<br>1b - Yes|
|18|EMAC Gasket Alarm Enable|
|EMAC_GSKT_<br>ALARM_EN|Specifies whether the EMAC IAHB gasket reported an alarm.<br>The field enables fault monitoring at FCCU NCF 1 for this fault: EMAC IAHB gasket alarm.<br>0b - No<br>1b - Yes|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1129 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|17|TCM AXBS Alarm Enable|
|TCM_AXBS_AL<br>ARM_EN|Specifies whether the TCM AHB splitter reported a safety alarm.<br>The field enables fault monitoring at FCCU NCF 1 for this fault: TCM AHB splitter safety alarm.<br>0b - No<br>1b - Yes|
|16|Data EDC Error Enable|
|DATA_EDC_ER<br>R_EN|Specifies whether a data EDC error occurred.<br>The field enables fault monitoring at FCCU NCF 1 for this fault: EDC error on data for safety.<br>0b - No<br>1b - Yes|
|15<br>ADDR_EDC_E<br>RR_EN|Address EDC Error Enable<br>Specifies whether an address integrity (EDC) error occurred.<br>The field enables fault monitoring at FCCU NCF 1 for this fault: EDC error on address for safety.<br>0b - No<br>1b - Yes|
|14|Enable bit for enabling the fault monitoring at FCCU NCF 1 for the fault: AIPS2 IAHB gasket alarm.|
|AIPS2_GSKT_A<br>LARM_EN|0b - No alarm indicated by AIPS2 IAHB gasket.<br>1b - Alarm indicated by AIPS2 IAHB gasket.|
|13|Enable bit for enabling the fault monitoring at FCCU NCF 1 for the fault: AIPS1 IAHB gasket alarm.|
|AIPS1_GSKT_A<br>LARM_EN|0b - No alarm indicated by AIPS1 IAHB gasket.<br>1b - Alarm indicated by AIPS1 IAHB gasket.|
|12|QuadSPI Gasket Alarm Enable|
|QSPI_GSKT_A<br>LARM_EN|Specifies whether the QuadSPI IAHB gasket reported an alarm.<br>The field enables fault monitoring at FCCU NCF 1 for this fault: QuadSPI IAHB gasket alarm.<br>0b - No<br>1b - Yes|
|11|HSE_B Gasket Alarm Enable|
|HSE_GSKT_AL<br>ARM_EN|Specifies whether the HSE_B IAHB gasket reported an alarm.<br>The field enables fault monitoring at FCCU NCF 1 for this fault: HSE_B IAHB gasket alarm.<br>0b - No<br>1b - Yes|
|10|Enable bit for enabling the fault monitoring at FCCU NCF 1 for the fault: uSDHC IAHB gasket alarm..<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1130 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|SDHC_GSKT_A<br>LARM_EN|0b - No alarm indicated by uSDHC IAHB gasket.<br>1b - Alarm indicated by uSDHC IAHB gasket.|
|9|DMA AXBS Alarm Enable|
|DMA_AXBS_AL<br>ARM_EN|Specifies whether eDMA AXBS_Lite reported a safety alarm.<br>The field enables fault monitoring at FCCU NCF 1 for this fault: eDMA AXBS_Lite safety alarm.<br>0b - No<br>1b - Yes|
|8|System AXBS Alarm Enable|
|SYS_AXBS_AL<br>ARM_EN|Specifies whether the system AXBS reported a safety alarm.<br>The field enables fault monitoring at FCCU NCF 1 for this fault: system AXBS safety alarm.<br>0b - No<br>1b - Yes|
|7|TCM Gasket Alarm Enable|
|DMA_PERIPH_<br>GSKT_ALARM_<br>EN|Specifies whether the eDMA-peripheral AXBS IAHB gasket reported a safety alarm.<br>The field enables fault monitoring at FCCU NCF 1 for this fault: IAHB gasket safety alarm from the eDMA<br>peripheral AXBS IAHB gasket.<br>0b - No<br>1b - Yes|
|6|DMA System Gasket Alarm Enable|
|DMA_SYS_GS<br>KT_ALARM_EN|Specifies whether the eDMA-system AXBS IAHB gasket reported a safety alarm.<br>The field enables fault monitoring at FCCU NCF 1 for this fault: IAHB gasket safety alarm from the<br>eDMA-system AXBS IHAB gasket.<br>0b - No<br>1b - Yes|
|5<br>TCM_GSKT_AL<br>ARM_EN|TCM Gasket Alarm Enable<br>Specifies whether the TCM IAHB gasket reported an alarm. If this field is 1, the gasket reports a<br>monitor alarm.<br>The field enables fault monitoring at FCCU NCF 1 for this fault: TCM IAHB gasket monitor alarm.<br>0b - No<br>1b - Yes|
|4|Cortex-M7 RCCU2 Alarm Enable|
|CM7_RCCU2_A<br>LARM_EN|Specifies whether a redundant RCCU reported a lockstep alarm.<br>The field enables fault monitoring at FCCU NCF 0 for this error fault: Cortex-M7 core redundant lockstep.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1131 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - No<br>1b - Yes|
|3<br>CM7_RCCU1_A<br>LARM_EN|Cortex-M7 RCCU1 Alarm Enable<br>Specifies whether RCCU reported a lockstep alarm.<br>The field enables fault monitoring at FCCU NCF 0 for this error fault: Cortex-M7 core lockstep.<br>0b - No<br>1b - Yes|
|2|Reserved|
|—||
|1|Cortex-M7_1 Lockup Enable|
|CM7_1_LOCKU<br>P_EN|Specifies whether the Cortex-M7_1 core is in the Lockup state.<br>The field enables fault monitoring at FCCU NCF 0 for this fault: Cortex-M7_1 core lockup.<br>0b - No<br>1b - Yes|
|0<br>CM7_0_LOCKU<br>P_EN|Cortex-M7 Lockup Enable<br>Specifies whether the Cortex-M7_0 core is in the Lockup state.<br>The field enables fault monitoring at FCCU NCF 0 for this fault: Cortex-M7_0 core lockup.<br>0b - No<br>1b - Yes|



### 37.2.31 Read Write GPR On Destructive Reset 4 (DCMRWD4) 

#### Offset 

|Register|Offset|
|---|---|
|DCMRWD4|50Ch|



Function 

Resets on destructive reset 4. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1132 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|Reserv<br>ed|TEST_<br>AC...|TEST_<br>AC...|SDHC<br>_RD...|VDD2<br>P5_...|VDD1<br>P1_...|Reserv<br>ed|FLAS<br>H_A...|PRAM<br>2_F...|FLAS<br>H_S...|FLAS<br>H_R...|FLAS<br>H_R...|FLAS<br>H_A...|FLAS<br>H_E...|PF2_D<br>AT...|PF2_C<br>OD...|
|Reset|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|PF1_D<br>AT...|PF1_C<br>OD...|PF0_D<br>AT...|PF0_C<br>OD...|HSE_<br>RAM...|PRAM<br>1_F...|PRAM<br>0_F...|DMA_<br>TCD...|CM7_1<br>_D...|CM7_1<br>_D...|CM7_1<br>_I...|CM7_0<br>_D...|CM7_0<br>_D...|CM7_0<br>_I...|CM7_1<br>_I...|CM7_0<br>_I...|
|Reset|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|



#### Fields 

|Field|Function|
|---|---|
|31<br>—|Reserved|
|30|Test Activation 1 Error Enable|
|TEST_ACTIVA<br>TION_1_ERR_E<br>N|Specifies whether a partial test is activated accidentally.<br>The field enables fault monitoring at FCCU NCF 5 for this fault: accidental partial test activation.<br>0b - No<br>1b - Yes|
|29|Test Activation 0 Error Enable|
|TEST_ACTIVA<br>TION_0_ERR_E<br>N|Specifies whether accidental partial test activation occurred.<br>The field enables fault monitoring at FCCU NCF 5 for this fault: accidental partial test activation.<br>0b - No<br>1b - Yes|
|28<br>SDHC_RDATA_<br>EDC_ERR_EN|Enable bit for enabling the fault monitoring at FCCU NCF 1 for the fault: Integrity (EDC) error on uSDHC<br>read data for safety.<br>0b - No integrity error reported on uSDHC read data.<br>1b - Integrity error reported on uSDHC read data.|
|27|VDD2P5 Go/Nogo Error Enable|
|VDD2P5_GNG_<br>ERR_EN|Specifies whether the VDD2P5 (double bond) supply is clean.<br>The field enables fault monitoring at FCCU NCF 4 for this fault: go/no go for VDD_HV_FLA (double bond)<br>going to FXOSC and PLL.<br>0b - Go indication that the supply is clean<br>1b - No go indication that the supply is unclean and there is a fault in double-bond connection or<br>its routing within the chip<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1133 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field<br>26<br>VDD1P1_GNG_<br>ERR_EN|Function<br>VDD1PD1 Go/Nogo Error Enable<br>Specifies whether the VDD1PD1 (double bond) supply is clean.<br>The field enables fault monitoring at FCCU NCF 4 for this fault: go/no go indicator for VDD1PD1 (double<br>bond) supply going to PLL.<br>0b - Go indication that the supply is clean<br>1b - No go indication that the supply is unclean and there is a fault in the double-bond connection<br>or its routing within the chip|
|---|---|
|25<br>—|Reserved|
|24<br>FLASH_ACCES<br>S_ERR_EN|Flash Memory Access Error Enable<br>Specifies whether a transaction monitor mismatch error occurred from the flash memory controller.<br>The field enables fault monitoring at FCCU NCF 3 for this fault: transaction monitor mismatch error from the<br>flash memory controller. The alarm indicates that the flash memory controller detected a transaction monitor<br>mismatch when compared to the flash memory safety feedback output. The flash memory specifies where<br>the reconstructed address is compared with the address that invoked the flash memory access.<br>0b - No<br>1b - Yes|
|23<br>PRAM2_FCCU_<br>ALARM_EN|Enable bit for enabling the fault monitoring at FCCU NCF 2 for the fault: PRAM2 safety alarm. This alarm<br>is set on faulty SRAM1 read or read modify error.<br>0b - No safety alarm indicated by PRAM2.<br>1b - Safety alarm indicated by PRAM2.|
|22<br>FLASH_SCAN_<br>ERR_EN|Flash Memory Scanning Error Enable<br>Specifies whether an error occurred during DCM flash memory scanning.<br>The field enables fault monitoring at FCCU NCF 3 for this fault: error during the DCM flash memory scanning<br>process because of invalid data.<br>On a POR or destructive reset event, because this field becomes 0, the field has no effect.<br>A lifecycle error (in case it is present) is not disabled.<br>~~NOTE~~<br>0b - No<br>1b - Yes|
|21|Flash Memory Reset Error Enable|
|FLASH_RST_E<br>RR_EN|Specifies whether a flash memory reset error occurred.<br>The field enables fault monitoring at FCCU NCF 3 for this fault: flash memory reset error. This error<br>indication is set when the flash memory encounters errors during its reset reads.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1134 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - No<br>1b - Yes|
|20<br>FLASH_REF_E<br>RR_EN|Flash Memory Reference Error Encode<br>Specifies whether a reference current loss or read voltage error occurred during previous read(s).<br>The field enables fault monitoring at FCCU NCF 3 for this fault: flash memory reference current loss or read<br>voltage error during previous read(s).<br>0b - No<br>1b - Yes|
|19|Flash Memory Address Encode Error Enable|
|FLASH_ADDR_<br>ENC_ERR_EN|Specifies whether an address encode error occurred in the flash memory.<br>The field enables fault monitoring at FCCU NCF 3 for this fault: flash memory address encode error. During<br>address decoding, if multiple or no address line is selected, FMU reports an address encode error.<br>0b - No<br>1b - Yes|
|18|Flash Memory EDC Error Enable|
|FLASH_EDC_E<br>RR_EN|Specifies whether EDC after ECC error is reported in the flash memory.<br>The field enables fault monitoring at FCCU NCF 3 for this fault: flash memory ECC correction error via EDC<br>reported by FMU.<br>0b - No<br>1b - Yes|
|17|PF2 Data ECC Error Enable|
|PF2_DATA_EC<br>C_ERR_EN|Specifies whether FMU reported an uncorrectable error in flash memory controller port 2 data memory.<br>The field enables fault monitoring at FCCU NCF 3 for this fault: Flash2 data ECC uncorrectable error.<br>0b - No<br>1b - Yes|
|16|PF2 Code ECC Error Enable|
|PF2_CODE_EC<br>C_ERR_EN|Specifies whether FMU reported an uncorrectable error in flash memory controller port 2 code memory.<br>The field enables fault monitoring at FCCU NCF 3 for this fault: Flash2 code ECC uncorrectable error.<br>0b - No<br>1b - Yes|
|15|PF1 Data ECC Error Enable|
|PF1_DATA_EC<br>C_ERR_EN|Specifies whether FMU reported an uncorrectable error in flash memory controller port 1 data memory.<br>The field enables fault monitoring at FCCU NCF 3 for this fault: Flash1 data ECC uncorrectable error.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1135 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function<br>0b - No<br>1b - Yes|
|---|---|
|14<br>PF1_CODE_EC<br>C_ERR_EN|PF1 Code ECC Error Enable<br>Specifies whether FMU reported an uncorrectable error in flash memory controller port 1 code memory.<br>The field enables fault monitoring at FCCU NCF 3 for this fault: Flash1 code ECC uncorrectable error.<br>0b - No<br>1b - Yes|
|13<br>PF0_DATA_EC<br>C_ERR_EN|PF0 Data ECC Error Enable<br>Specifies whether FMU reported an uncorrectable error in flash memory controller port 0 data memory.<br>The field enables fault monitoring at FCCU NCF 3 for this fault: Flash0 data ECC uncorrectable error.<br>0b - No<br>1b - Yes|
|12<br>PF0_CODE_EC<br>C_ERR_EN|PF0 Code ECC Error Enable<br>Specifies whether FMU reported an uncorrectable error in flash memory controller port 0 code memory.<br>The field enables fault monitoring at FCCU NCF 3 for this fault: Flash0 code ECC uncorrectable error.<br>0b - No<br>1b - Yes|
|11<br>HSE_RAM_EC<br>C_ERR_EN|HSE_B RAM ECC Error Enable<br>Specifies whether HSE_B RAM reported an uncorrectable ECC.<br>The field enables fault monitoring at FCCU NCF 2 for this fault: HSE_B RAM uncorrectable ECC.<br>0b - No<br>1b - Yes|
|10|PRAM1 FCCU Alarm Enable|
|PRAM1_FCCU_<br>ALARM_EN|Specifies whether PRAM0 reported a safety alarm.<br>The field enables fault monitoring at FCCU NCF 2 for this fault: PRAM1 safety alarm. This alarm is set on<br>faulty SRAM1 read or read modify error.<br>0b - No<br>1b - Yes|
|9<br>PRAM0_FCCU_<br>ALARM_EN|PRAM0 FCCU Alarm Enable<br>Specifies whether PRAM0 reported a safety alarm.<br>The field enables fault monitoring at FCCU NCF 2 for this fault: PRAM0 safety alarm. This alarm is set to<br>faulty SRAM0 read or read modify error.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1136 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - No<br>1b - Yes|
|8<br>DMA_TCD_RA<br>M_ECC_ERR_E<br>N|eDMA TCD RAM ECC Error Enable<br>Specifies whether uncorrectable ECC error detection is enabled at FCCU.<br>The field enables fault monitoring at FCCU NCF 2 for this fault: uncorrectable ECC error reported from<br>eDMA_TCD memory. This uncorrectable ECC error consists of a multi-bit data ECC error and an address<br>ECC error.<br>0b - No<br>1b - Yes|
|7<br>CM7_1_DTCM1<br>_ECC_ERR_EN|Cortex-M7_1 DTCM 1 ECC Error Enable<br>Specifies whether uncorrectable ECC error detection is enabled at FCCU.<br>The field enables fault monitoring at FCCU NCF 2 for this fault: uncorrectable ECC error from the<br>Cortex-M7_1 core's DTCM block 1. This uncorrectable ECC error consists of a multi-bit data ECC error and<br>an address ECC error.<br>The Cortex-M7_1 core's DTCM 1 consists of two physical blocks.|
||The Cortex-M7_1 core's DTCM 1 does not support address ECC errors in S32K324,<br>S32K344, and S32K314.<br>~~NOTE~~|
||0b - No<br>1b - Yes|
|6|Cortex-M7_1 DTCM 0 ECC Error Enable|
|CM7_1_DTCM0<br>_ECC_ERR_EN|Specifies whether uncorrectable ECC error detection is enabled at FCCU. This uncorrectable ECC error<br>consists of a multi-bit data ECC error and an address ECC error. The Cortex-M7_1 core's DTCM consists<br>of two physical blocks.<br>This field enables fault monitoring at FCCU NCF 2 for this fault: uncorrectable ECC error from the<br>Cortex-M7_1 core's DTCM block 0.<br>The Cortex-M7_1 core's DTCM 0 does not support address ECC errors in S32K324,<br>S32K344, and S32K314.<br>~~NOTE~~|
||0b - No<br>1b - Yes|
|5|Cortex-M7_1 ITCM ECC Error Enable|
|CM7_1_ITCM_<br>ECC_ERR_EN|Specifies whether uncorrectable ECC error detection is enabled at FCCU.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1137 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1138-03.png)


<!-- Start of picture text -->
Field Function<br>The field enables fault monitoring at FCCU NCF 2 for this fault: uncorrectable ECC error from the<br>Cortex-M7_1 core's ITCM. This uncorrectable ECC error consists of a multi-bit data ECC error and an<br>address ECC error.<br>  NOTE<br>The Cortex-M7_1 core's ITCM does not support address ECC errors in S32K324, S32K344,<br>and S32K314.<br>0b - No<br>1b - Yes<br>4 Cortex-M7_0 DTCM 1 ECC Error Enable<br>CM7_0_DTCM1 Specifies whether uncorrectable ECC error detection is enabled at FCCU.<br>_ECC_ERR_EN<br>The field enables fault monitoring at FCCU NCF 2 for this fault: uncorrectable ECC error from the<br>Cortex-M7_0 core's DTCM block 1. This uncorrectable ECC error consists of a multi-bit data ECC error and<br>an address ECC error. The Cortex-M7_0 core's DTCM consists of two physical blocks.<br>  NOTE<br>The Cortex-M7_0 core's DTCM 1 does not support address ECC errors in S32K324,<br>S32K344, and S32K314.<br>0b - No<br>1b - Yes<br>3 Cortex-M7_0 DTCM 0 ECC Error Enable<br>CM7_0_DTCM0 Specifies whether uncorrectable ECC error detection is enabled at FCCU.<br>_ECC_ERR_EN<br>The field enables fault monitoring at FCCU NCF 2 for this fault: uncorrectable ECC error from the<br>Cortex-M7_0 core's DTCM block 0. This uncorrectable ECC error consists of a multi-bit data ECC error and<br>an address ECC error. The Cortex-M7_0 core's DTCM consists of two physical blocks.<br>  NOTE<br>The Cortex-M7_0 core's DTCM 0 does not support address ECC errors in S32K324,<br>S32K344, and S32K314.<br>0b - No<br>1b - Yes<br>2 Cortex-M7 ITCM ECC Error Enable<br>CM7_0_ITCM_ Specifies whether uncorrectable ECC error detection is enabled at FCCU.<br>ECC_ERR_EN<br>The field enables fault monitoring at FCCU NCF 2 for this fault: uncorrectable ECC error from the<br>Cortex-M7_0 core's ITCM. This uncorrectable ECC error consists of a multi-bit data ECC error and an<br>address ECC error.<br>  NOTE<br>The Cortex-M7_0 core's ITCM does not support address ECC errors in S32K324, S32K344,<br>and S32K314.<br>Table continues on the next page...<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1138 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - No<br>1b - Yes|
|1|Cortex-M7_1 I-cache Tag ECC Error Enable|
|CM7_1_ICTAG_<br>ECC_ERR_EN|Specifies whether the Cortex-M7_1 core's I-cache tag memory detected a multi-bit ECC error.<br>This field enables fault monitoring at FCCU NCF 2 for this fault: multi-bit ECC error from the Cortex-M7_1<br>core's I-cache tag memory.<br>0b - No<br>1b - Yes|
|0|Cortex-M7_0 I-cache Tag ECC Error Enable|
|CM7_0_ICTAG_<br>ECC_ERR_EN|Specifies whether the Cortex-M7_0 core's I-cache tag memory detected a multi-bit ECC error.<br>The field enables fault monitoring at FCCU NCF 2 for this fault: multi-bit ECC error from the Cortex-M7_0<br>core's I-cache tag memory.<br>0b - No<br>1b - Yes|



### 37.2.32 Read Write GPR On Destructive Reset 5 (DCMRWD5) 

#### Offset 

|Register|Offset|
|---|---|
|DCMRWD5|510h|



#### Function 

Resets on destructive reset 5. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|CM7_2<br>_D...|CM7_2<br>_D...|CM7_2<br>_I...|CM7_2<br>_I...|CM7_2<br>_I...|CM7_2<br>_D...|CM7_2<br>_D...|CM7_2<br>_A...|CM7_2<br>_A...|HSE_<br>RDA...|CM7_0<br>_A...|CM7_0<br>_A...|CM7_1<br>_A...|CM7_1<br>_A...|DMA_<br>RDA...|Reserv<br>ed|
|Reset|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|EMAC<br>_RD...|TCM_<br>RDA...|DEBU<br>G_A...|MTR_<br>BUS...|STCU<br>_BI...|MBIST<br>_A...|STCU<br>_NC...|SW_N<br>CF_...|SW_N<br>CF_...|SW_N<br>CF_...|SW_N<br>CF_...|INTM_<br>3_...|INTM_<br>2_...|INTM_<br>1_...|INTM_<br>0_...|Reserv<br>ed|
|Reset|1|0|1|1|1|1|1|1|1|1|1|1|1|1|1|1|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1139 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Fields 

|Field|Function|
|---|---|
|31|Cortex-M7_2 DTCM 1 ECC Error Enable|
|CM7_2_DTCM1<br>_ECC_ERR_EN|Specifies whether uncorrectable ECC error detection is enabled at FCCU from the Cortex-M7_2 core's<br>DTCM block 1.<br>The field enables fault monitoring at FCCU NCF 2 for this fault: uncorrectable ECC error from the<br>Cortex-M7_2 core's DTCM block 1. This uncorrectable ECC error consists of a multi-bit data ECC error and<br>an address ECC error. The Cortex-M7_2 core's DTCM consists of two physical blocks.<br>The Cortex-M7_2 core's DTCM 1 does not support address ECC errors in S32K324,<br>S32K344, and S32K314.<br>~~NOTE~~|
||0b - No<br>1b - Yes|
|30|Cortex-M7_2 DTCM 0 ECC Error Enable|
|CM7_2_DTCM0<br>_ECC_ERR_EN|Specifies whether uncorrectable ECC error detection is enabled at FCCU from the Cortex-M7_2 core's<br>DTCM block 0.<br>The field enables fault monitoring at FCCU NCF 2 for this fault: uncorrectable ECC error from the<br>Cortex-M7_2 core's DTCM block 0. This uncorrectable ECC error consists of a multi-bit data ECC error and<br>an address ECC error. The Cortex-M7_2 core's DTCM consists of two physical blocks.|
||The Cortex-M7_2 core's DTCM 0 does not support address ECC errors in S32K324,<br>S32K344, and S32K314.<br>~~NOTE~~|
||0b - No<br>1b - Yes|
|29|Cortex-M7_2 ITCM ECC Error Enable|
|CM7_2_ITCM_<br>ECC_ERR_EN|Specifies whether uncorrectable ECC error detection is enabled at FCCU from the Cortex-M7_2<br>core's ITCM.<br>The field enables fault monitoring at FCCU NCF 2 for this fault: uncorrectable ECC error from the<br>Cortex-M7_2 core's ITCM. This uncorrectable ECC error consists of a multi-bit data ECC error and an<br>address ECC error.<br>The Cortex-M7_2 core's ITCM does not support address ECC errors in S32K324, S32K344,<br>and S32K314.<br>~~NOTE~~<br>0b - No<br>1b - Yes|
|28|Cortex-M7_2 I-cache Tag ECC Error Enable|
|CM7_2_ICTAG_<br>ECC_ERR_EN|Specifies whether the Cortex-M7_2 core's I-cache tag memory detected a multi-bit error.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1140 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function<br>The field enables fault monitoring at FCCU NCF 2 for this fault: multi-bit ECC error from the Cortex-M7_2<br>core's I-cache tag memory.<br>0b - No<br>1b - Yes|
|---|---|
|27<br>CM7_2_ICDAT<br>A_ECC_ERR_E<br>N|Cortex-M7_2 I-cache Data ECC Error Enable<br>Specifies whether the Cortex-M7_2 core's I-cache data memory detected a multi-bit ECC error.<br>The field enables fault monitoring at FCCU NCF 2 for this fault: multi-bit ECC error from the Cortex-M7_2<br>core's I-cache data memory.<br>0b - No<br>1b - Yes|
|26|Cortex-M7_2 D-cache Tag ECC Error Enable|
|CM7_2_DCTAG<br>_ECC_ERR_EN|Specifies whether the Cortex-M7_2 core's D-cache tag memory detected a multi-bit ECC error.<br>The field enables fault monitoring at FCCU NCF 2 for this fault: multi-bit ECC error from the Cortex-M7_2<br>core's D-cache tag memory.<br>0b - No<br>1b - Yes|
|25|Cortex-M7_2 D-cache Data ECC Error Enable|
|CM7_2_DCDAT<br>A_ECC_ERR_E<br>N|Specifies whether the Cortex-M7_2 core's D-cache data memory detected a multi-bit ECC error.<br>The field enables fault monitoring at FCCU NCF 2 for this fault: multi-bit ECC error from the Cortex-M7_2<br>core's D-cache data memory.<br>0b - No<br>1b - Yes|
|24<br>CM7_2_AHBM_<br>RDATA_EDC_E<br>RR_EN|Cortex-M7_2 AHBM Read Data EDC Error Enable<br>Specifies whether an EDC error is reported on the Cortex-M7_2 core's main read data.<br>The field enables fault monitoring at FCCU NCF 1 for this fault: EDC error on the Cortex-M7_2 core's main<br>read data for safety.<br>0b - No<br>1b - Yes|
|23|Cortex-M7_2 AHBP Read Data EDC Error Enable|
|CM7_2_AHBP_<br>RDATA_EDC_E<br>RR_EN|Specifies whether an EDC error is reported on the Cortex-M7_2 core's peripheral read data.<br>The field enables fault monitoring at FCCU NCF 1 for this fault: EDC error on Cortex-M7_2 peripheral read<br>data for safety.<br>0b - No<br>1b - Yes<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1141 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|22|HSE_B Read Data EDC Error Enable|
|HSE_RDATA_E<br>DC_ERR_EN|Specifies whether an EDC error is reported on HSE_B read data.<br>The field enables fault monitoring at FCCU NCF 1 for this fault: EDC error on HSE_B read data for safety.<br>0b - No<br>1b - Yes|
|21|Cortex-M7_0 AHBM Read Data EDC Error Enable|
|CM7_0_AHBM_<br>RDATA_EDC_E<br>RR_EN|Specifies whether an EDC error is reported on the Cortex-M7_0 core's main read data.<br>The field enables fault monitoring at FCCU NCF 1 for this fault: EDC error on the Cortex-M7_0 core's main<br>read data for safety.<br>0b - No<br>1b - Yes|
|20|Cortex-M7_0 AHBP Read Data EDC Error Enable|
|CM7_0_AHBP_<br>RDATA_EDC_E<br>RR_EN|Specifies whether an EDC error is reported on the Cortex-M7_0 core's peripheral read data.<br>The field enables fault monitoring at FCCU NCF 1 for this fault: EDC error on the Cortex-M7_0 core's<br>peripheral read data for safety.<br>0b - No<br>1b - Yes|
|19|Cortex-M7_1 AHBM Read Data EDC Error Enable|
|CM7_1_AHBM_<br>RDATA_EDC_E<br>RR_EN|Specifies whether an EDC error is reported on the Cortex-M7_1 core's main read data.<br>The field enables fault monitoring at FCCU NCF 1 for this fault: EDC error on the Cortex-M7_1 core's main<br>read data for safety.<br>0b - No<br>1b - Yes|
|18|Cortex-M7_1 AHBP Read Data EDC Error Enable|
|CM7_1_AHBP_<br>RDATA_EDC_E<br>RR_EN|Specifies whether an EDC error is reported on the Cortex-M7_1 core's peripheral read data.<br>The field enables fault monitoring at FCCU NCF 1 for this fault: EDC error on the Cortex-M7_1 core's<br>peripheral read data for safety.<br>0b - No<br>1b - Yes|
|17<br>DMA_RDATA_<br>EDC_ERR_EN|eDMA Read Data EDC Error Enable<br>Specifies whether an EDC error is reported on eDMA read data.<br>The field enables fault monitoring at FCCU NCF 1 for this fault: EDC error on eDMA read data for safety.<br>0b - No<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1142 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function<br>1b - Yes|
|---|---|
|16<br>—|Reserved|
|15<br>EMAC_RDATA<br>_EDC_ERR_EN|EMAC Read Data EDC Error Enable<br>Specifies whether an EDC error is reported on EMAC read data.<br>The field enables fault monitoring at FCCU NCF 1 for this fault: EDC error on EMAC read data for safety.<br>0b - No<br>1b - Yes|
|14<br>TCM_RDATA_E<br>DC_ERR_EN|TCM Read Data EDC Error Enable<br>Specifies whether an EDC error is reported on TCM read data.<br>The field enables fault monitoring at FCCU NCF 1 for this fault: EDC error on TCM read data for safety.<br>0b - No<br>1b - Yes|
|13<br>DEBUG_ACTIV<br>ATION_ERR_E<br>N|Debug Activation Error Enable<br>Specifies whether unintended debug is activated.<br>The field enables fault monitoring at FCCU NCF 5 for this fault: monitoring of unintended debug activation.<br>The value of this field is 1 when the core is in the Halted state with application debug not enabled or debugger<br>request not enabled.<br>While the debugger is connected, DCM.DCMRWD5[DEBUG_ACTIVATION_ERR_EN]<br>must be configured as 0 to disable debug activation error monitoring because the debugger<br>is intentionally connected to the chip.<br>~~NOTE~~|
||0b - No<br>1b - Yes|
|12<br>MTR_BUS_ER<br>R_EN|MTR Bus Error Enable<br>Specifies whether a transfer error is reported from MTR.<br>The field enables fault monitoring at FCCU NCF 5 for this fault: fault reported because of illegal access on<br>MTR. This fault is reported via a transfer error indication to the system.<br>0b - No<br>1b - Yes|
|11|STCU2 BIST User CF Enable|
|STCU_BIST_U<br>SER_CF_EN|Specifies whether LBIST or MBIST is enabled accidentally (a fault condition is detected in Run mode).<br>The field enables fault monitoring at FCCU NCF 5 for this fault: LBIST or MBIST enabled accidentally.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1143 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - No<br>1b - Yes|
|10<br>MBIST_ACTIVA<br>TION_ERR_EN|MBIST Activation Error Enable<br>Specifies whether accidental backdoor is enabled on memories.<br>The field enables fault monitoring at FCCU NCF 5 for this fault: accidental backdoor access on memories.<br>This monitor needs to be disabled on FCCU when performing a fault injection.<br>0b - No<br>1b - Yes|
|9<br>STCU_NCF_EN|STCU2 NCF Enable<br>Enables fault monitoring at FCCU NCF 5 for this fault: STCU2 NCF, that is, BIST result error.<br>0b - Disables<br>1b - Enables|
|8<br>SW_NCF_3_EN|Software NCF 3 Enable<br>Enables fault monitoring at FCCU NCF 7 for this fault: software NCF3 (DCMRWF1[FCCU_SW_NCF3]).<br>0b - Disables<br>1b - Enables|
|7<br>SW_NCF_2_EN|Software NCF 2 Enable<br>Enables fault monitoring at FCCU NCF 7 for this fault: software NCF2 (DCMRWF1[FCCU_SW_NCF2]).<br>0b - Disables<br>1b - Enables|
|6<br>SW_NCF_1_EN|Software NCF 1 Enable<br>Enables fault monitoring at FCCU NCF 7 for this fault: software NCF1 (DCMRWF1[FCCU_SW_NCF1]).<br>0b - Disables<br>1b - Enables|
|5<br>SW_NCF_0_EN|Software NCF 0 Enable<br>Enables fault monitoring at FCCU NCF 7 for this fault: software NCF0 (DCMRWF1[FCCU_SW_NCF0]).<br>0b - Disables<br>1b - Enables|
|4|INTM 3 Error Enable|
|INTM_3_ERR_<br>EN|Specifies whether interrupt monitor 3 reported an error.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1144 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||The field enables fault monitoring at FCCU NCF 6 for this fault: interrupt monitor 3 error reported by INTM.<br>This error is also reflected in INTM.INTM_STATUS3. See the "Functional description" section in the INTM<br>chapter for details.<br>0b - No<br>1b - Yes|
|3<br>INTM_2_ERR_<br>EN|INTM 2 Error Enable<br>Specifies whether interrupt monitor 2 reported an error.<br>The field enables fault monitoring at FCCU NCF 6 for this fault: interrupt monitor 2 error reported by INTM.<br>This error is also reflected in INTM.INTM_STATUS2. See the "Functional description" section in the INTM<br>chapter for details.<br>0b - No<br>1b - Yes|
|2<br>INTM_1_ERR_<br>EN|INTM 1 Error Enable<br>Specifies whether interrupt monitor 1 reported an error.<br>The field enables fault monitoring at FCCU NCF 6 for this fault: interrupt monitor 1 error reported by INTM.<br>This error is also reflected in INTM.INTM_STATUS1. See the "Functional description" section in the INTM<br>chapter for details.<br>0b - No<br>1b - Yes|
|1|INTM 0 Error Enable|
|INTM_0_ERR_<br>EN|Specifies whether interrupt monitor 0 reported an error.<br>The field enables fault monitoring at FCCU NCF 6 for this fault: interrupt monitor 0 error reported by INTM.<br>This error is also reflected in INTM.INTM_STATUS0. See the "Functional description" section in the INTM<br>chapter for details.<br>0b - No<br>1b - Yes|
|0<br>—|Reserved|



### 37.2.33 Read Write GPR On Destructive Reset 6 (DCMRWD6) 

#### Offset 

|Register|Offset|
|---|---|
|DCMRWD6|514h|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1145 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Function 

#### Resets on destructive reset 6. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|SAI1_<br>DB...|SAI0_<br>DB...|FLEX<br>CAN...|FLEX<br>CAN...|FLEX<br>CAN...|FLEX<br>CAN...|FLEX<br>CAN...|FLEX<br>CAN...|FLEXI<br>O_...|LPI2C<br>1_...|LPI2C<br>0_...|LPSPI<br>5_...|LPSPI<br>4_...|LPSPI<br>3_...|LPSPI<br>2_...|LPSPI<br>1_...|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|LPSPI<br>0_...|PIT2_<br>DB...|PIT1_<br>DB...|PIT0_<br>DB...|STM1_<br>DB...|STM0_<br>DB...|SWT1<br>_DB...|SWT0<br>_DB...|RTC_<br>DBG...|EMIO<br>S2_...|EMIO<br>S1_...|EMIO<br>S0_...|LCU1_<br>DB...|LCU0_<br>DB...|FCCU<br>_DB...|EDMA<br>_DB...|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31|SAI1 debug disable bit for CM7_0. Set this bit 1 to disable the debug of IP.|
|SAI1_DBG_DIS<br>_CM7_0|0b - SAI1 enters debug mode when CM7_0 enters debug mode.<br>1b - SAI1 remains functional and is not impacted when CM7_0 enters debug mode.|
|30<br>SAI0_DBG_DIS<br>_CM7_0|SAI0 debug disable bit for CM7_0. Set this bit 1 to disable the debug of IP.<br>0b - SAI0 enters debug mode when CM7_0 enters debug mode.<br>1b - SAI0 remains functional and is not impacted when CM7_0 enters debug mode.|
|29<br>FLEXCAN5_DB<br>G_DIS_CM7_0|FlexCAN_5 Debug Disable Cortex-M7_0<br>Specifies whether FlexCAN_5 enters Debug mode or remains functional and unimpacted when the<br>Cortex-M7_0 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|28<br>FLEXCAN4_DB<br>G_DIS_CM7_0|FlexCAN_4 Debug Disable Cortex-M7_0<br>Specifies whether FlexCAN_4 enters Debug mode or remains functional and unimpacted when the<br>Cortex-M7_0 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|27<br>FLEXCAN3_DB<br>G_DIS_CM7_0|FlexCAN_3 Debug Disable Cortex-M7_0<br>Specifies whether FlexCAN_3 enters Debug mode or remains functional and unimpacted when the<br>Cortex-M7_0 core enters Debug mode.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1146 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|---|---|
|26<br>FLEXCAN2_DB<br>G_DIS_CM7_0|FlexCAN_2 Debug Disable Cortex-M7_0<br>Specifies whether FlexCAN_2 enters Debug mode or remains functional and unimpacted when the<br>Cortex-M7_0 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|25|FlexCAN_1 Debug Disable Cortex-M7_0|
|FLEXCAN1_DB<br>G_DIS_CM7_0|Specifies whether FlexCAN_1 enters Debug mode or remains functional and unimpacted when the<br>Cortex-M7_0 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|24|FlexCAN_0 Debug Disable Cortex-M7_0|
|FLEXCAN0_DB<br>G_DIS_CM7_0|Specifies whether FlexCAN_0 enters Debug mode or remains functional and unimpacted when the<br>Cortex-M7_0 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|23|FlexIO Debug Disable Cortex-M7_0|
|FLEXIO_DBG_<br>DIS_CM7_0|Specifies whether FlexIO enters Debug mode or remains functional and unimpacted when the Cortex-M7_0<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|22|LPI2C_1 Debug Disable Cortex-M7_0|
|LPI2C1_DBG_D<br>IS_CM7_0|Specifies whether LPI2C_1 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_0 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1147 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|21|LPI2C_0 Debug Disable Cortex-M7_0|
|LPI2C0_DBG_D<br>IS_CM7_0|Specifies whether LPI2C_0 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_0 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|20|LPSPI_5 Debug Disable Cortex-M7_0|
|LPSPI5_DBG_<br>DIS_CM7_0|Specifies whether LPSPI_5 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_0 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|19|LPSPI_4 Debug Disable Cortex-M7_0|
|LPSPI4_DBG_<br>DIS_CM7_0|Specifies whether LPSPI_4 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_0 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|18|LPSPI_3 Debug Disable Cortex-M7_0|
|LPSPI3_DBG_<br>DIS_CM7_0|Specifies whether LPSPI_3 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_0 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|17|LPSPI_2 Debug Disable Cortex-M7_0|
|LPSPI2_DBG_<br>DIS_CM7_0|Specifies whether LPSPI_2 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_0 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|16|LPSPI_1 Debug Disable Cortex-M7_0|
|LPSPI1_DBG_<br>DIS_CM7_0|Specifies whether LPSPI_1 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_0 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1148 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|15<br>LPSPI0_DBG_<br>DIS_CM7_0|LPSPI_0 Debug Disable Cortex-M7_0<br>Specifies whether LPSPI_0 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_0 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|14|PIT_2 Debug Disable Cortex-M7_0|
|PIT2_DBG_DIS<br>_CM7_0|Specifies whether PIT_2 enters Debug mode or remains functional and unimpacted when the Cortex-M7_0<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|13|PIT_1 Debug Disable Cortex-M7_0|
|PIT1_DBG_DIS<br>_CM7_0|Specifies whether PIT_1 enters Debug mode or remains functional and unimpacted when the Cortex-M7_0<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|12|PIT_0 Debug Disable Cortex-M7_0|
|PIT0_DBG_DIS<br>_CM7_0|Specifies whether PIT_0 enters Debug mode or remains functional and unimpacted when the Cortex-M7_0<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|11|STM_1 Debug Disable Cortex-M7_0|
|STM1_DBG_DI<br>S_CM7_0|Specifies whether STM_1 enters Debug mode or remains functional and unimpacted when the Cortex-M7_0<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode|
||1b - Remains functional and unimpacted|
|10|STM_0 Debug Disable Cortex-M7_0|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1149 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|STM0_DBG_DI<br>S_CM7_0|Specifies whether STM_0 enters Debug mode or remains functional and unimpacted when the Cortex-M7_0<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|9|SWT_1 Debug Disable Cortex-M7_0|
|SWT1_DBG_DI<br>S_CM7_0|Specifies whether SWT_1 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_0 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|8|SWT_0 Debug Disable Cortex-M7_0|
|SWT0_DBG_DI<br>S_CM7_0|Specifies whether SWT_0 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_0 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|7|RTC Debug Disable Cortex-M7_0|
|RTC_DBG_DIS<br>_CM7_0|Specifies whether RTC enters Debug mode or remains functional and unimpacted when the Cortex-M7_0<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|6|EMIOS2 debug disable bit for CM7_0. Set this bit 1 to disable the debug of IP.|
|EMIOS2_DBG_|0b - eMIOS2 enters debug mode when CM7_0 enters debug mode.|
|DIS_CM7_0|1b - eMIOS2 remains functional and is not impacted when CM7_0 enters debug mode.|
|5|EMIOS1 debug disable bit for CM7_0. Set this bit 1 to disable the debug of IP.|
|EMIOS1_DBG_<br>DIS_CM7_0|0b - eMIOS1 enters debug mode when CM7_0 enters debug mode.<br>1b - eMIOS1 remains functional and is not impacted when CM7_0 enters debug mode.|
|4|eMIOS_0 Debug Disable Cortex-M7_0|
|EMIOS0_DBG_<br>DIS_CM7_0|Specifies whether eMIOS_0 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_0 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1150 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|3<br>LCU1_DBG_DI<br>S_CM7_0|LCU_1 Debug Disable Cortex-M7_0<br>Specifies whether LCU_1 enters Debug mode or remains functional and unimpacted when the Cortex-M7_0<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|2|LCU_0 Debug Disable Cortex-M7_0|
|LCU0_DBG_DI<br>S_CM7_0|Specifies whether LCU_0 enters Debug mode or remains functional and unimpacted when the Cortex-M7_0<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|1|FCCU Debug Disable Cortex-M7_0|
|FCCU_DBG_DI<br>S_CM7_0|Specifies whether FCCU enters Debug mode or remains functional and unimpacted when the Cortex-M7_0<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|0<br>EDMA_DBG_DI<br>S_CM7_0|eDMA Debug Disable Cortex-M7_0<br>Specifies whether eDMA enters Debug mode or remains functional and unimpacted when the Cortex-M7_0<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|



### 37.2.34 Read Write GPR On Destructive Reset 7 (DCMRWD7) 

#### Offset 

|Register|Offset|
|---|---|
|DCMRWD7|518h|



Function 

Resets on destructive reset 7. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1151 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||Reserved||||||Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|SWT2<br>_DB...|STM2_<br>DB...|FLEX<br>CAN...|FLEX<br>CAN...|I3C_D<br>BG...|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-21<br>—|Reserved|
|20<br>—|Reserved|
|19<br>—|Reserved|
|18<br>—|Reserved|
|17<br>—|Reserved|
|16<br>—|Reserved|
|15<br>—|Reserved|
|14<br>—|Reserved|
|13<br>—|Reserved|
|12<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1152 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field<br>11<br>—|Function<br>Reserved|
|---|---|
|10<br>—|Reserved|
|9<br>—|Reserved|
|8<br>—|Reserved|
|7<br>|Reserved|
|—<br>6<br>—<br>5<br>|Reserved<br>Reserved|
|—<br>4<br>SWT2_DBG_DI<br>S_CM7_0|SWT_2 Debug Disable Cortex-M7_0<br>Specifies whether SWT_2 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_0 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|3|STM_2 Debug Disable Cortex-M7_0|
|STM2_DBG_DI<br>S_CM7_0|Specifies whether STM_2 enters Debug mode or remains functional and unimpacted when the Cortex-M7_0<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|2|FLEXCAN7 debug disable bit for CM7_0. Set this bit 1 to disable the debug of module.|
|FLEXCAN7_DB<br>G_DIS_CM7_0|0b - FLEXCAN7 enters debug mode when CM7_0 enters debug mode.<br>1b - FLEXCAN7 remains functional and is not impacted when CM7_0 enters debug mode.|
|1|FLEXCAN6 debug disable bit for CM7_0. Set this bit 1 to disable the debug of module.<br>0b - FLEXCAN6 enters debug mode when CM7_0 enters debug mode.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1153 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|FLEXCAN6_DB<br>G_DIS_CM7_0|1b - FLEXCAN6 remains functional and is not impacted when CM7_0 enters debug mode.|
|0|I3C Debug Disable Cortex-M7_0|
|I3C_DBG_DIS_<br>CM7_0|Specifies whether I3C enters Debug mode or remains functional and unimpacted when the Cortex-M7_0<br>core enters Debug mode.|
||Write 1 to this field to disable debug.|
||0b - Enters Debug mode|
||1b - Remains functional and unimpacted|



### 37.2.35 Read Write GPR On Destructive Reset 8 (DCMRWD8) 

#### Offset 

|Register|Offset|
|---|---|
|DCMRWD8|51Ch|



Function 

Resets on destructive reset 8. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|Reserv<br>ed|Reserv<br>ed|FLEX<br>CAN...|FLEX<br>CAN...|FLEX<br>CAN...|FLEX<br>CAN...|FLEX<br>CAN...|FLEX<br>CAN...|FLEXI<br>O_...|LPI2C<br>1_...|LPI2C<br>0_...|LPSPI<br>5_...|LPSPI<br>4_...|LPSPI<br>3_...|LPSPI<br>2_...|LPSPI<br>1_...|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|LPSPI<br>0_...|PIT2_<br>DB...|PIT1_<br>DB...|PIT0_<br>DB...|STM1_<br>DB...|STM0_<br>DB...|SWT1<br>_DB...|SWT0<br>_DB...|RTC_<br>DBG...|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|LCU1_<br>DB...|LCU0_<br>DB...|FCCU<br>_DB...|EDMA<br>_DB...|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31<br>—|Reserved|
|30|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1154 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field<br>|Function|
|---|---|
|—<br>29<br>FLEXCAN5_DB<br>G_DIS_CM7_1|FlexCAN_5 Debug Disable Cortex-M7_1<br>Specifies whether FlexCAN_5 enters Debug mode or remains functional and unimpacted when the<br>Cortex-M7_1 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|28<br>FLEXCAN4_DB<br>G_DIS_CM7_1|FlexCAN_4 Debug Disable Cortex-M7_1<br>Specifies whether FlexCAN_4 enters Debug mode or remains functional and unimpacted when the<br>Cortex-M7_1 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|27<br>FLEXCAN3_DB<br>G_DIS_CM7_1|FlexCAN_3 Debug Disable Cortex-M7_1<br>Specifies whether FlexCAN_3 enters Debug mode or remains functional and unimpacted when the<br>Cortex-M7_1 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|26<br>FLEXCAN2_DB<br>G_DIS_CM7_1|FlexCAN_2 Debug Disable Cortex-M7_1<br>Specifies whether FlexCAN_2 enters Debug mode or remains functional and unimpacted when the<br>Cortex-M7_1 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|25<br>FLEXCAN1_DB<br>G_DIS_CM7_1|FlexCAN_1 Debug Disable Cortex-M7_1<br>Specifies whether FlexCAN_1 enters Debug mode or remains functional and unimpacted when the<br>Cortex-M7_1 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|24|FlexCAN_0 Debug Disable Cortex-M7_1<br>Specifies whether FlexCAN_0 enters Debug mode or remains functional and unimpacted when the<br>Cortex-M7_1 core enters Debug mode.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1155 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|FLEXCAN0_DB<br>G_DIS_CM7_1|Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|23|FlexIO Debug Disable Cortex-M7_1|
|FLEXIO_DBG_<br>DIS_CM7_1|Specifies whether FlexIO enters Debug mode or remains functional and unimpacted when the Cortex-M7_1<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|22<br>LPI2C1_DBG_D<br>IS_CM7_1|LPI2C_1 Debug Disable Cortex-M7_1<br>Specifies whether LPI2C_1 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_1 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|21|LPI2C_0 Debug Disable Cortex-M7_1|
|LPI2C0_DBG_D<br>IS_CM7_1|Specifies whether LPI2C_0 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_1 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|20<br>LPSPI5_DBG_<br>DIS_CM7_1|LPSPI_5 Debug Disable Cortex-M7_1<br>Specifies whether LPSPI_5 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_1 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|19|LPSPI_4 Debug Disable Cortex-M7_1|
|LPSPI4_DBG_<br>DIS_CM7_1|Specifies whether LPSPI_4 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_1 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1156 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|18|LPSPI_3 Debug Disable Cortex-M7_1|
|LPSPI3_DBG_<br>DIS_CM7_1|Specifies whether LPSPI_3 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_1 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|17<br>LPSPI2_DBG_<br>DIS_CM7_1|LPSPI_2 Debug Disable Cortex-M7_1<br>Specifies whether LPSPI_2 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_1 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|16|LPSPI_1 Debug Disable Cortex-M7_1|
|LPSPI1_DBG_<br>DIS_CM7_1|Specifies whether LPSPI_1 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_1 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|15<br>LPSPI0_DBG_<br>DIS_CM7_1|LPSPI_0 Debug Disable Cortex-M7_1<br>Specifies whether LPSPI_0 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_1 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|14<br>PIT2_DBG_DIS<br>_CM7_1|PIT_2 Debug Disable Cortex-M7_1<br>Specifies whether PIT_2 enters Debug mode or remains functional and unimpacted when the Cortex-M7_1<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|13<br>PIT1_DBG_DIS<br>_CM7_1|PIT_1 Debug Disable Cortex-M7_1<br>Specifies whether PIT_1 enters Debug mode or remains functional and unimpacted when the Cortex-M7_1<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1157 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|12<br>PIT0_DBG_DIS<br>_CM7_1|PIT_0 Debug Disable Cortex-M7_1<br>Specifies whether PIT_0 enters Debug mode or remains functional and unimpacted when the Cortex-M7_1<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|11|STM_1 Debug Disable Cortex-M7_1|
|STM1_DBG_DI<br>S_CM7_1|Specifies whether STM_1 enters Debug mode or remains functional and unimpacted when the Cortex-M7_1<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|10|STM_0 Debug Disable Cortex-M7_1|
|STM0_DBG_DI<br>S_CM7_1|Specifies whether STM_0 enters Debug mode or remains functional and unimpacted when the Cortex-M7_1<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|9|SWT_1 Debug Disable Cortex-M7_1|
|SWT1_DBG_DI<br>S_CM7_1|Specifies whether SWT_1 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_1 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|8|SWT_0 Debug Disable Cortex-M7_1|
|SWT0_DBG_DI<br>S_CM7_1|Specifies whether SWT_0 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_1 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|7|RTC Debug Disable Cortex-M7_1|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1158 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|RTC_DBG_DIS<br>_CM7_1|Specifies whether RTC enters Debug mode or remains functional and unimpacted when the Cortex-M7_1<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|6<br>—<br>5<br>|Reserved<br>Reserved|
|—<br>4<br>—<br>3|Reserved<br>LCU_1 Debug Disable Cortex-M7_1|
|LCU1_DBG_DI<br>S_CM7_1|Specifies whether LCU_1 enters Debug mode or remains functional and unimpacted when the Cortex-M7_1<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|2<br>LCU0_DBG_DI<br>S_CM7_1|LCU_0 Debug Disable Cortex-M7_1<br>Specifies whether LCU_0 enters Debug mode or remains functional and unimpacted when the Cortex-M7_1<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|1|FCCU Debug Disable Cortex-M7_1|
|FCCU_DBG_DI<br>S_CM7_1|Specifies whether FCCU enters Debug mode or remains functional and unimpacted when the Cortex-M7_1<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|0|eDMA Debug Disable Cortex-M7_1|
|EDMA_DBG_DI<br>S_CM7_1|Specifies whether eDMA enters Debug mode or remains functional and unimpacted when the Cortex-M7_1<br>core enters Debug mode.<br>Write 1 to this field to disable debug.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1159 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Enters Debug mode|
||1b - Remains functional and unimpacted|



### 37.2.36 Read Write GPR On Destructive Reset 9 (DCMRWD9) 

#### Offset 

|Register|Offset|
|---|---|
|DCMRWD9|520h|



Function 

Resets on destructive reset 9. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||Reserved||||||||Reserved|||
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||Reserved||||||SWT2<br>_DB...|STM2_<br>DB...|FLEXC<br>AN...|FLEXC<br>AN...|I3C_D<br>BG...|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-21|Reserved|
|—||
|20-5|Reserved|
|—||
|4|SWT_2 Debug Disable Cortex-M7_1|
|SWT2_DBG_DI<br>S_CM7_1|Specifies whether SWT_2 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_1 core enters Debug mode.|
||Write 1 to this field to disable debug.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1160 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|3<br>STM2_DBG_DI<br>S_CM7_1|STM_2 Debug Disable Cortex-M7_1<br>Specifies whether STM_2 enters Debug mode or remains functional and unimpacted when the Cortex-M7_1<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|2<br>FLEXCAN7_DB<br>G_DIS_CM7_1|FLEXCAN7 debug disable bit for CM7_1. Set this bit 1 to disable the debug of module.<br>0b - FLEXCAN7 enters debug mode when CM7_1 enters debug mode.<br>1b - FLEXCAN7 remains functional and is not impacted when CM7_1 enters debug mode.|
|1<br>FLEXCAN6_DB<br>G_DIS_CM7_1|FLEXCAN6 debug disable bit for CM7_1. Set this bit 1 to disable the debug of module.<br>0b - FLEXCAN6 enters debug mode when CM7_1 enters debug mode.<br>1b - FLEXCAN6 remains functional and is not impacted when CM7_1 enters debug mode.|
|0<br>I3C_DBG_DIS_<br>CM7_1|I3C Debug Disable Cortex-M7_1<br>Specifies whether I3C enters Debug mode or remains functional and unimpacted when the Cortex-M7_1<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|



### 37.2.37 Read Write GPR On Destructive Reset 12 (DCMRWD12) 

#### Offset 

|Register|Offset|
|---|---|
|DCMRWD12|52Ch|



Function Resets on destructive reset 12. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1161 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|SAI1_<br>DB...|SAI0_<br>DB...|FLEX<br>CAN...|FLEX<br>CAN...|FLEX<br>CAN...|FLEX<br>CAN...|FLEX<br>CAN...|FLEX<br>CAN...|FLEXI<br>O_...|LPI2C<br>1_...|LPI2C<br>0_...|LPSPI<br>5_...|LPSPI<br>4_...|LPSPI<br>3_...|LPSPI<br>2_...|LPSPI<br>1_...|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|LPSPI<br>0_...|PIT2_<br>DB...|PIT1_<br>DB...|PIT0_<br>DB...|STM1_<br>DB...|STM0_<br>DB...|SWT1<br>_DB...|SWT0<br>_DB...|RTC_<br>DBG...|eMIOS<br>2_...|eMIOS<br>1_...|eMIOS<br>0_...|LCU1_<br>DB...|LCU0_<br>DB...|FCCU<br>_DB...|EDMA<br>_DB...|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31|SAI1 debug disable bit for CM0+(HSE_B). Set this bit 1 to disable the debug of module.|
|SAI1_DBG_DIS<br>_CM7_2|0b - SAI1 enters debug mode when CM7_2 enters debug mode.<br>1b - SAI1 remains functional and is not impacted when CM7_2 enters debug mode.|
|30<br>SAI0_DBG_DIS<br>_CM7_2|SAIO debug disable bit for CM0+(HSE_B). Set this bit 1 to disable the debug of module.<br>0b - SAIO enters debug mode when CM7_2 enters debug mode.<br>1b - SAIO remains functional and is not impacted when CM7_2 enters debug mode.|
|29<br>FLEXCAN5_DB<br>G_DIS_CM7_2|FlexCAN5 Debug Disable For Cortex M0+ (HSE_B)<br>Specifies whether FlexCAN5 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_2 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|28<br>FLEXCAN4_DB<br>G_DIS_CM7_2|FlexCAN4 Debug Disable For Cortex M0+ (HSE_B)<br>Specifies whether FlexCAN4 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_2 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|27<br>FLEXCAN3_DB<br>G_DIS_CM7_2|FlexCAN3 Debug Disable For Cortex M0+ (HSE_B)<br>Specifies whether FlexCAN3 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_2 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1162 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function<br>1b - Remains functional and unimpacted|
|---|---|
|26<br>FLEXCAN2_DB<br>G_DIS_CM7_2|FlexCAN2 Debug Disable For Cortex M0+ (HSE_B)<br>Specifies whether FlexCAN2 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_2 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|25<br>FLEXCAN1_DB<br>G_DIS_CM7_2|FlexCAN1 Debug Disable For Cortex M0+ (HSE_B)<br>Specifies whether FlexCAN1 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_2 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|24<br>FLEXCAN0_DB<br>G_DIS_CM7_2|FlexCAN0 Debug Disable For Cortex M0+ (HSE_B)<br>Specifies whether FlexCAN0 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_2 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|23<br>FLEXIO_DBG_<br>DIS_CM7_2|FlexIO Debug Disable For Cortex M0+ (HSE_B)<br>Specifies whether FlexIO enters Debug mode or remains functional and unimpacted when the Cortex-M7_2<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|22<br>LPI2C1_DBG_D<br>IS_CM7_2|LPI2C1 Debug Disable For Cortex M0+ (HSE_B)<br>Specifies whether LPI2C1 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_2 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|21|LPI2C0 Debug Disable For Cortex M0+ (HSE_B)<br>Specifies whether LPI2C0 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_2 core enters Debug mode.|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1163 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|LPI2C0_DBG_D<br>IS_CM7_2|Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|20<br>LPSPI5_DBG_<br>DIS_CM7_2|LPSPI5 Debug Disable For Cortex M0+ (HSE_B)<br>Specifies whether LPSPI5 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_2 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|19|LPSPI4 Debug Disable For Cortex M0+ (HSE_B)|
|LPSPI4_DBG_<br>DIS_CM7_2|Specifies whether LPSPI4 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_2 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|18|LPSPI3 Debug Disable For Cortex M0+ (HSE_B)|
|LPSPI3_DBG_<br>DIS_CM7_2|Specifies whether LPSPI3 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_2 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|17<br>LPSPI2_DBG_<br>DIS_CM7_2|LPSPI2 Debug Disable For Cortex M0+ (HSE_B)<br>Specifies whether LPSPI2 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_2 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|16|LPSPI1 Debug Disable For Cortex M0+ (HSE_B)|
|LPSPI1_DBG_<br>DIS_CM7_2|Specifies whether LPSPI1 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_2 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1164 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|15<br>LPSPI0_DBG_<br>DIS_CM7_2|LPSPI0 Debug Disable For Cortex M0+ (HSE_B)<br>Specifies whether LPSPI0 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_2 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|14|PIT2 Debug Disable For Cortex M0+ (HSE_B)|
|PIT2_DBG_DIS<br>_CM7_2|Specifies whether PIT2 enters Debug mode or remains functional and unimpacted when the Cortex-M7_2<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|13|PIT1 Debug Disable For Cortex M0+ (HSE_B)|
|PIT1_DBG_DIS<br>_CM7_2|Specifies whether PIT1 enters Debug mode or remains functional and unimpacted when the Cortex-M7_2<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|12<br>PIT0_DBG_DIS<br>_CM7_2|PIT0 Debug Disable For Cortex M0+ (HSE_B)<br>Specifies whether PIT0 enters Debug mode or remains functional and unimpacted when the Cortex-M7_2<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|11<br>STM1_DBG_DI<br>S_CM7_2|STM1 Debug Disable For Cortex M0+ (HSE_B)<br>Specifies whether STM1 enters Debug mode or remains functional and unimpacted when the Cortex-M7_2<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|10<br>STM0_DBG_DI<br>S_CM7_2|STM0 Debug Disable For Cortex M0+ (HSE_B)<br>Specifies whether STM0 enters Debug mode or remains functional and unimpacted when the Cortex-M7_2<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1165 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|9|SWT1 Debug Disable For Cortex M0+ (HSE_B)|
|SWT1_DBG_DI<br>S_CM7_2|Specifies whether SWT1 enters Debug mode or remains functional and unimpacted when the Cortex-M7_2<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|8|SWT0 Debug Disable For Cortex M0+ (HSE_B)|
|SWT0_DBG_DI<br>S_CM7_2|Specifies whether SWT0 enters Debug mode or remains functional and unimpacted when the Cortex-M7_2<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|7|RTC Debug Disable For Cortex M0+ (HSE_B)|
|RTC_DBG_DIS<br>_CM7_2|Specifies whether RTC enters Debug mode or remains functional and unimpacted when the Cortex-M7_2<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|6|eMIOS2 debug disable bit for CM0+(HSE_B). Set this bit 1 to disable the debug of module.|
|eMIOS2_DBG_<br>DIS_CM7_2|0b - eMIOS2 enters debug mode when CM7_2 enters debug mode.<br>1b - eMIOS2 remains functional and is not impacted when CM7_2 enters debug mode.|
|5|eMIOS1 debug disable bit for CM0+(HSE_B). Set this bit 1 to disable the debug of module.|
|eMIOS1_DBG_|0b - eMIOS1 enters debug mode when CM7_2 enters debug mode.|
|DIS_CM7_2|1b - eMIOS1 remains functional and is not impacted when CM7_2 enters debug mode.|
|4|eMIOS0 Debug Disable For Cortex M0+ (HSE_B)|
|eMIOS0_DBG_<br>DIS_CM7_2|Specifies whether eMIOS0 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_2 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode|
||1b - Remains functional and unimpacted|
|3|LCU1 Debug Disable For Cortex M0+ (HSE_B)|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1166 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|LCU1_DBG_DI<br>S_CM7_2|Specifies whether LCU1 enters Debug mode or remains functional and unimpacted when the Cortex-M7_2<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|2<br>LCU0_DBG_DI<br>S_CM7_2|LCU0 Debug Disable For Cortex M0+ (HSE_B)<br>Specifies whether LCU0 enters Debug mode or remains functional and unimpacted when the Cortex-M7_2<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|1<br>FCCU_DBG_DI<br>S_CM7_2|FCCU Debug Disable For Cortex M0+ (HSE_B)<br>Specifies whether FCCU enters Debug mode or remains functional and unimpacted when the Cortex-M7_2<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|0<br>EDMA_DBG_DI<br>S_CM7_2|eDMA Debug Disable For Cortex M0+ (HSE_B)<br>Specifies whether eDMA enters Debug mode or remains functional and unimpacted when the Cortex-M7_2<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode|
||1b - Remains functional and unimpacted|



### 37.2.38 Read Write GPR On Destructive Reset 13 (DCMRWD13) 

#### Offset 

|Register|Offset|
|---|---|
|DCMRWD13|530h|



Function Resets on destructive reset 13. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1167 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||Reserved||||||Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|SWT2<br>_DB...|STM2_<br>DB...|FLEX<br>CAN...|FLEX<br>CAN...|I3C0_<br>DB...|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-21<br>—|Reserved|
|20<br>—|Reserved|
|19<br>—|Reserved|
|18<br>—|Reserved|
|17<br>—|Reserved|
|16<br>—|Reserved|
|15<br>—|Reserved|
|14<br>—|Reserved|
|13<br>—|Reserved|
|12<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1168 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|11|Reserved|
|—<br>10<br>—<br>9<br>—|Reserved<br>Reserved|
|8<br>—<br>7|Reserved<br>Reserved|
|—<br>6<br>—|Reserved|
|5<br>—|Reserved|
|4|SWT2 Debug Disable For Cortex-M7_2|
|SWT2_DBG_DI<br>S_CM7_2|Specifies whether SWT2 enters Debug mode or remains functional and unimpacted when the Cortex-M7_2<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|3<br>STM2_DBG_DI<br>S_CM7_2|STM2 Debug Disable For Cortex-M7_2<br>Specifies whether STM2 enters Debug mode or remains functional and unimpacted when the Cortex-M7_2<br>core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|2|FLEXCAN7 debug disable bit for CM7_2. Set this bit 1 to disable the debug of module.|
|FLEXCAN7_DB<br>G_DIS_CM7_2|0b - FLEXCAN7 enters debug mode when CM7_2 enters debug mode.<br>1b - FLEXCAN7 remains functional and is not impacted when CM7_2 enters debug mode.|
|1|FlexCAN6 Debug Disable For Cortex-M7_2|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1169 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|FLEXCAN6_DB<br>G_DIS_CM7_2|Specifies whether FlexCAN6 enters Debug mode or remains functional and unimpacted when the Cortex-<br>M7_2 core enters Debug mode.<br>Write 1 to this field to disable debug.<br>0b - Enters Debug mode<br>1b - Remains functional and unimpacted|
|0|I3C0 Debug Disable For Cortex-M7_2|
|I3C0_DBG_DIS<br>_CM7_2|Specifies whether I3C0 enters Debug mode or remains functional and unimpacted when the Cortex-M7_2<br>core enters Debug mode.<br>Write 1 to this field to disable debug.|
||0b - Enters Debug mode|
||1b - Remains functional and unimpacted|



### 37.2.39 Read Write GPR On Destructive Reset 16 (DCMRWD16) 

#### Offset 

|Registe|r|||Offset|||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|DCMR<br>Diagram|WD16<br>|||538h|||||||||||||
|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|R<br>W||||||||Rese|rved||||||||
|Reset|1|1|1|1|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W||||||Rese|rved||||||PRAM<br>2_G...|PRAM<br>2_T...|PRAM<br>1_G...|PRAM<br>0_G...|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Diagram 

#### Fields 

|Field|Function||
|---|---|---|
|31-4<br>—|Reserved|Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1170 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|3<br>PRAM2_GSKT_<br>ALARM_EN|Enable bit for enabling the fault monitoring at FCCU NCF 1 for the fault: PRAM2 IAHB Gasket monitor<br>alarm.<br>0b - No alarm reported from PRAM2 IAHB gasket.<br>1b - Monitor alarm reported from PRAM2 IAHB gasket.|
|2<br>PRAM2_TCM_<br>GSKT_ALARM_<br>EN|Enable bit for enabling the fault monitoring at FCCU NCF 1 for the fault: PRAM2_TCM IAHB Gasket<br>monitor alarm.<br>0b - No alarm reported from PRAM2_TCM IAHB gasket.<br>1b - Monitor alarm reported from PRAM2_TCM IAHB gasket.|
|1<br>PRAM1_GSKT_<br>ALARM_EN|Enable bit for enabling the fault monitoring at FCCU NCF 1 for the fault: PRAM1 IAHB Gasket monitor<br>alarm.<br>0b - No alarm reported from PRAM1 IAHB gasket.<br>1b - Monitor alarm reported from PRAM1 IAHB gasket.|
|0<br>PRAM0_GSKT_<br>ALARM_EN|Enable bit for enabling the fault monitoring at FCCU NCF 1 for the fault: PRAM0 IAHB Gasket monitor<br>alarm.<br>0b - No alarm reported from PRAM0 IAHB gasket.<br>1b - Monitor alarm reported from PRAM0 IAHB gasket.|



### 37.2.40 Read Write GPR On Functional Reset 1 (DCMRWF1) 

#### Offset 

|Register|Offset|
|---|---|
|DCMRWF1|600h|



#### Function 

Resets on functional reset 1. 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|Reserv<br>ed||Reserved||VDD_1<br>_5...|VDD_<br>HV_...|VDD_<br>HV_...|VSS_L<br>V_...|SUPP|LY_MON|_SEL|SUPP<br>LY_...|Rese|rved|Reserv<br>ed|STAN<br>DBY...|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|VDD_<br>HV_...|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|I3C0_<br>CL...|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|RMII_<br>MI...|EMAC<br>_SB...|FCCU<br>_SW...|FCCU<br>_SW...|FCCU<br>_SW...|FCCU<br>_SW...|CAN_<br>TIM...|CAN_<br>TIM...|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1171 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Fields 

|Field|Function|
|---|---|
|31<br>—|Reserved|
|30-28<br>—|Reserved|
|27<br>VDD_1_5_VLT_<br>DVDR_EN|VDD1P5 Voltage Divider Enable<br>Enables the VDD1P5 2:1 divider for voltage measurement using the supply voltage that ADC monitors.<br>0b - Disables<br>1b - Enables|
|26<br>VDD_HV_B_VL<br>T_DVDR_EN|VDD_HV_B Voltage Divider Enable<br>Enables the VDD_HV_B 2:1 divider for voltage measurement by using the supply voltage that ADC<br>monitors.<br>0b - Disables<br>1b - Enables|
|25|VDD_HV_A Voltage Divider Enable|
|VDD_HV_A_VL<br>T_DVDR_EN|Enables the VDD_HV_A 2:1 divider for voltage measurement by using supply voltage that ADC monitors.<br>0b - Disables<br>1b - Enables|
|24|VSS_LV Monitoring Enable|
|VSS_LV_ANMU<br>X_EN|Enables VSS_LV monitoring.<br>You must write 1 to this field (with DCMRWF1[SUPPLY_MON_EN] = 1b0 for VSS_LV<br>monitoring by ADC0).<br>~~NOTE~~<br>0b - Disables<br>1b - Enables|
|23-21<br>SUPPLY_MON<br>_SEL|Supply Monitoring Select<br>Selects the source of voltage that ADC uses for supply monitoring.<br>• The SUPPLY_MON_SEL configurations are effective only when SUPPLY_MON_EN is<br>configured as 1b1.<br>• When SUPPLY_MON_EN is configured as 0 and VSS_LV_ANMUX_EN is configured<br>as 1, VSS_LV is monitored.<br>~~NOTE~~<br>000b - VDD_HV_A_DIV|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1172 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||001b - VDD_HV_B_DIV<br>010b - VDD_1.5_DIV<br>011b - VDD_2.5_OSC<br>100b - VDD1.1_PD1_HOT_POINT<br>101b - VDD1.1_PD1_COLD_POINT<br>110b - VDD1.1_PLL<br>111b - VDD1.1_PD0|
|20|Supply Monitoring Enable|
|SUPPLY_MON<br>_EN|Enables the ADC supply voltage monitoring.<br>0b - Disables<br>1b - Enables|
|19-18<br>|Reserved|
|—<br>17<br>—|Reserved|
|16<br>STANDBY_IO_<br>CONFIG|Standby I/O Configuration<br>Controls the I/O state in Standby mode:<br>• For standby I/O configuration standby entry, you must write 0 to this field before performing I/O<br>configurations in standby entry sequence.<br>• For standby I/O configuration standby exit, you must write 1 to this field after performing I/O<br>configurations on standby exit.<br>0b - Standby I/O configuration standby entry<br>1b - Standby I/O configuration standby exit|
|15<br>VDD_HV_B_IO_<br>CTRL_LATCH|VDD_HV_B I/O Control Latch<br>Specifies whether VDD_HV_B domain pins function as normal or are latched.<br>This field manages I/O control latching in low-frequency Run mode to reduce power consumption on the<br>VDD_HV_B domain pins.<br>This field must remain 0, except in FIRC 3 MHz and FIRC 187.5 kHz operation modes.<br>~~NOTE~~<br>0b - Function as normal|
||1b - Are latched|
|14|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1173 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|—<br>13|Reserved|
|—<br>12<br>—|Reserved|
|11|I3C0 Clock Mux Select|
|I3C0_CLK_MU<br>X_SEL|Selects the clock source of I3C0.<br>0b - I3C0 runs with CORE_CLK as FCLK. This configuration is to be used in other clock modes<br>apart from A+.<br>1b - I3C0 runs with AIPS_PLAT_CLK as FCLK. This configuration is to be used in clock mode A+<br>(240 MHz). In clock mode A+, DCMRWF1[11] as 1'b0 is not supported by the device.|
|10<br>—|Reserved|
|9<br>—|Reserved|
|8<br>—|Reserved|
|7<br>RMII_MII_SEL|RMII MII Select<br>Selects either MII or RMII mode of Ethernet.<br>0b - MII<br>1b - RMII|
|6|EMAC Sideband Data Endianness Control.|
|EMAC_SB_EN<br>D_CTRL|0b - The EMAC sideband data is transferred in little-endian mode.<br>1b - The EMAC sideband data is transferred in big-endian mode.|
|5<br>FCCU_SW_NC<br>F3|FCCU Software NCF 3<br>Specifies whether NCF 3 to FCCU is generated. For the exact FCCU slot, see the "Fault Collection and<br>Control Unit (FCCU)" chapter.<br>0b - Not generated<br>1b - Generated|
|4<br>FCCU_SW_NC<br>F2|FCCU Software NCF 2<br>Specifies whether NCF 2 to FCCU is generated. For the exact FCCU slot, see the "Fault Collection and<br>Control Unit (FCCU)" chapter.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1174 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Not generated<br>1b - Generated|
|3<br>FCCU_SW_NC<br>F1|FCCU Software NCF 1<br>Specifies whether NCF 1 to FCCU is generated. For the exact FCCU slot, see the "Fault Collection and<br>Control Unit (FCCU)" chapter.<br>0b - Not generated<br>1b - Generated|
|2<br>FCCU_SW_NC<br>F0|FCCU Software NCF 0<br>Specifies whether NCF0 to FCCU is generated. For the exact FCCU slot, see the "Fault Collection and<br>Control Unit (FCCU)" chapter.<br>0b - Not generated<br>1b - Generated|
|1|FlexCAN Timestamp Enable|
|CAN_TIMESTA<br>MP_EN|Enables the FlexCAN timestamping feature.<br>0b - Disables<br>1b - Enables|
|0|FlexCAN Timestamp Select|
|CAN_TIMESTA<br>MP_SEL|Selects either EMAC or STM for FlexCAN timestamping.<br>0b - EMAC<br>1b - STM0|



### 37.2.41 Read Write GPR On Functional Reset 2 (DCMRWF2) 

#### Offset 

|Register|Offset|
|---|---|
|DCMRWF2|604h|



Function 

Resets on functional reset 2. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1175 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W|WKPU<br>8_S...|WKPU<br>45_...|WKPU<br>27_...|WKPU<br>18_...|WKPU<br>15_...|WKPU<br>14_...|WKPU<br>0_S...|PLL1_<br>LO...|Rese|rved|PGOO<br>D_P...|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|HSE_<br>GSK...|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|SUPP|LY2_MON|_SEL|SUPP<br>LY2...|SAI_M<br>CL...|Rese|rved|PMOS<br>_CT...|Reserv<br>ed|SIRC_<br>TR...|PMC_<br>TRI...|FIRC_<br>TR...|DCM_<br>SCA...|Res|erved|Reserv<br>ed|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31|WKPU[8] Source Select|
|WKPU8_SRC_<br>SELECT|Controls and specifies the source of WKPU[8].<br>0b - GPIO[34]<br>1b - GPIO[231]|
|30<br>WKPU45_SRC_<br>SELECT|WKPU[45] Source Select<br>Controls and specifies the source of WKPU[45].<br>0b - GPIO[89]<br>1b - GPIO[217]|
|29<br>WKPU27_SRC_<br>SELECT|WKPU[27] Source Select<br>Controls and specifies the source of WKPU[27].<br>0b - GPIO[130]<br>1b - GPIO[233]|
|28<br>WKPU18_SRC_<br>SELECT|WKPU[18] Source Select<br>Controls and specifies the source of WKPU[18].<br>0b - GPIO[75]<br>1b - GPIO[235]|
|27|Controls the source of WKPU[15].|
|WKPU15_SRC_<br>SELECT|0b - GPIO[6] is used as source of WKPU[15].<br>1b - GPIO[227] is used as source of WKPU[15].|
|26|Controls the source of WKPU[14].|
|WKPU14_SRC_|0b - GPIO[49] is used as source of WKPU[14].|
|SELECT|1b - GPIO[229] is used as source of WKPU[14].|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1176 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|25|Controls the source of WKPU[0].|
|WKPU0_SRC_<br>SELECT|0b - GPIO[2] is used as source of WKPU[0].<br>1b - GPIO[225] is used as source of WKPU[0].|
|24|PLL1 LOL Reset Enable|
|PLL1_LOL_RST<br>_EN|Controls the functional reset or interrupt behavior of the PLL1 LOL event.<br>0b - PLL1 LOL event results in an interrupt<br>1b - PLL1 LOL event results in a reset|
|23-22<br>—<br>21|Reserved<br>PGOOD Polarity|
|PGOOD_POLA<br>RITY|Selects the PGOOD polarity.<br>See the PMIC documentation before performing this configuration.<br>0b - Active-high signal<br>1b - Active-low signal|
|20|Reserved|
|—||
|19<br>—|Reserved|
|18<br>—|Reserved|
|17<br>—|Reserved|
|16<br>HSE_GSKT_BY<br>PASS|HSE_B Gasket Bypass<br>Enables the HSE_B IAHB gasket behavior out of Standby mode.<br>• If you write 0 to this field, the DCF client controls the HSE_B IAHB gasket bypass configuration. The<br>system must continue to run on FIRC, and if intended to run on PLL, a functional reset must be<br>asserted.<br>• If you write 1 to this field, the HSE_B IAHB gasket is bypassed out of standby.<br>0b - Bypass configuration controlled by the DCF client<br>1b - Bypassed out of standby|
|15-13|Supply 2 Monitoring Select|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1177 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|SUPPLY2_MO<br>N_SEL|Selects the source of voltage that ADC uses for supply monitoring.<br>The SUPPLY2_MON_SEL configurations are effective only when SUPPLY2_MON_EN is<br>configured as 1b1.<br>~~NOTE~~<br>000b - VDD2P5_PLL2<br>001b - VDD1P1_PLL2<br>010b - Reserved<br>011b - Reserved|
|12<br>SUPPLY2_MO<br>N_EN|Supply 2 Monitoring Enable<br>Enables supply voltage that ADC monitors to makes use of another ANAMUX.<br>0b - Disables<br>1b - Enables|
|11<br>SAI_MCLK2_S<br>EL|SAI MCLK2 Select<br>Controls the dataout from the PMOS_CTRL pad when PMC.CONFIG[LMSMPSEN] is configured as 1'b0.<br>PMOS_CTRL_GPIO_DATA is not impacted if PMC.CONFIG[LMSMPSEN] is configured as 1'b1.<br>0b - Data from the PMOS_CTRL pad is 1'b0<br>1b - Data from the PMOS_CTRL pad is 1'b1|
|10-9<br>—|Reserved|
|8|PMOS Control GPIO Data|
|PMOS_CTRL_<br>GPIO_DATA|Controls the dataout from the PMOS_CTRL pad when PMC.CONFIG[LMSMPSEN] is configured as 1'b0.<br>PMOS_CTRL_GPIO_DATA is not impacted if PMC.CONFIG[LMSMPSEN] is configured as 1'b1.<br>0b - Data from the PMOS_CTRL pad is 1'b0<br>1b - Data from the PMOS_CTRL pad is 1'b1|
|7<br>—<br>6<br>SIRC_TRIM_BY<br>P_STDBY_EXT|Reserved<br>SIRC Trim Bypass Standby Exit<br>Controls the bypassing of SIRC trimming on standby exit.<br>0b - Not bypassed<br>1b - Bypassed|
|5|PMC Trim MC_RGM DCF Bypass Standby Exit<br>Controls the bypassing of PMC trimming and MC_RGM loading on standby exit.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1178 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|PMC_TRIM_RG<br>M_DCF__BYP_<br>STDBY_EXT|0b - Not bypassed<br>1b - Bypassed|
|4<br>FIRC_TRIM_BY<br>P_STDBY_EXT|FIRC Trim Bypass Standby Exit<br>Controls the bypassing of FIRC trimming on standby exit.<br>0b - Not bypassed<br>1b - Bypassed|
|3<br>DCM_SCAN_B<br>YP_STDBY_EX<br>T|DCM Scan Bypass Standby Exit<br>Controls the bypassing of DCM scanning on standby exit.<br>0b - Not bypassed<br>1b - Bypassed|
|2-1<br>—|Reserved|
|0<br>—|Reserved|



### 37.2.42 Read Write GPR On Functional Reset 3 (DCMRWF3) 

#### Offset 

|Register|Offset|
|---|---|
|DCMRWF3|608h|



Function 

Resets on functional reset 3. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1179-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>Reserved  Reserved  Reserved<br>W<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R MAC_ MAC_RX_CLK_<br>Reserved<br>W TX_... MUX_...<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1179 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Fields 

|Field|Function|
|---|---|
|31-24<br>—|Reserved|
|23-22<br>—|Reserved|
|21-16<br>—|Reserved|
|15<br>MAC_TX_CLK_<br>MUX_BYPASS|Bypasses the MAC_TX_CLK mux MC_CGM_MUX8 and the TX_CLK arrives without MC_CGM_MUX8 to<br>the MAC in case of external clock source.<br>0b - The MAC_RX_CLK is derived from MC_CGM_MUX7..<br>1b - The MAC_TX_CLK is derived from MC_CGM_MUX8.|
|14-13<br>MAC_RX_CLK_<br>MUX_BYPASS|Bypasses the MAC_RX_CLK mux MC_CGM_MUX7 and the RX_CLK arrives without MC_CGM_MUX7<br>to the MAC in case of external clock source.<br>00b - The MAC_RX_CLK is derived from MC_CGM_MUX7..<br>01b - The MAC_RX_CLK arrives directly from the RX_CLK pin.|
|12-0<br>—|Reserved|



### 37.2.43 Read Write GPR On Functional Reset 4 (DCMRWF4) 

#### Offset 

|Register|Offset|
|---|---|
|DCMRWF4|60Ch|



Function Resets on functional reset 4. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1180 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R<br>W||||||Rese|rved||||||CM7_2<br>_C...|CM7_1<br>_C...|CM7_0<br>_C...|GLITC<br>H_...|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R<br>W|GLITC<br>H_...|GLITC<br>H_...|GLITC<br>H_...|Rese|rved|MUX_<br>MOD...|MUX_<br>MOD...|Rese|rved|MUX_<br>MOD...|MUX_<br>MOD...|MUX_<br>MOD...|MUX_<br>MOD...|MUX_<br>MOD...|MUX_<br>MOD...|Reserv<br>ed|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31-20<br>—|Reserved|
|19<br>CM7_2_CPUW<br>AIT|Cortex-M7_2 CPU Wait<br>Defines the configuration to place the Cortex-M7_2 core into Wait mode.<br>0b - Disables CPUWAIT for Cortex-M7_2<br>1b - Places Cortex-M7_2 into Wait mode using CPUWAIT|
|18<br>CM7_1_CPUW<br>AIT|Cortex-M7_1 CPU Wait<br>Defines the configuration to place the Cortex-M7_1 core into Wait mode.<br>0b - Disables CPUWAIT for Cortex-M7_1<br>1b - Places Cortex-M7_1 into Wait mode using CPUWAIT|
|17<br>CM7_0_CPUW<br>AIT|Cortex-M7_0 CPU Wait<br>Defines the configuration to place the Cortex-M7_0 core in CPU Wait mode.<br>0b - Disables CPUWAIT for Cortex-M7_0<br>1b - Places Cortex-M7_0 in Wait mode using CPUWAIT|
|16|Glitch Filter TRGMUX Input 3 Bypass|
|GLITCH_FIL_T<br>RG_IN3_BYP|Selects whether to bypass or filter out the pulse.<br>0b - Enables glitch filter on TRGMUX input 60<br>1b - Bypasses glitch filter on TRGMUX input 60|
|15|Glitch Filter TRGMUX Input 2 Bypass|
|GLITCH_FIL_T<br>RG_IN2_BYP|Selects whether to bypass or filter out the pulse.<br>0b - Enables glitch filter on TRGMUX input 61|
||1b - Bypasses glitch filter on TRGMUX input 61|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1181 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|14|Glitch Filter TRGMUX Input 1 Bypass|
|GLITCH_FIL_T<br>RG_IN1_BYP|Selects whether to bypass or filter out the pulse.<br>0b - Enables glitch filter on TRGMUX input 62<br>1b - Bypasses glitch filter on TRGMUX input 62|
|13<br>GLITCH_FIL_T<br>RG_IN0_BYP|Glitch Filter TRGMUX Input 0 Bypass<br>Selects whether to bypass or filter out the pulse.<br>0b - Enables glitch filter on TRGMUX input 63<br>1b - Bypasses glitch filter on TRGMUX input 63|
|12-11<br>—|Reserved|
|10|Mux Mode Enable ADC2 Standard Channel 9|
|MUX_MODE_E<br>N_ADC2_S9|Controls the selection of GPIOs to drive ADC_2 standard channel 9.<br>0b - Selects GPIO_132 as ADC2_S9<br>1b - Selects GPIO_46 as ADC2_S9|
|9<br>MUX_MODE_E<br>N_ADC2_S8|Mux Mode Enable ADC2 Standard Channel 8<br>Controls the selection of GPIOs to drive ADC_2 standard channel 8.<br>0b - Selects GPIO_133 as ADC2_S8<br>1b - Selects GPIO_45 as ADC2_S8|
|8-7<br>—|Reserved|
|6<br>MUX_MODE_E<br>N_ADC1_S23|Mux Mode Enable ADC_1 Standard Channel 23<br>Controls the selection of GPIOs to drive ADC_1 standard channel 23.<br>0b - Selects GPIO_125 as ADC1_S23<br>1b - Selects GPIO_146 as ADC1_S23|
|5|Mux Mode Enable ADC_1 Standard Channel 22|
|MUX_MODE_E<br>N_ADC1_S22|Controls the selection of GPIOs to drive ADC_1 standard channel 22.<br>0b - Selects GPIO_124 as ADC1_S22<br>1b - Selects GPIO_145 as ADC1_S22|
|4|Mux Mode Enable ADC_1 Standard Channel 15|
|MUX_MODE_E<br>N_ADC1_S15|Controls the selection of GPIOs to drive ADC_1 standard channel 15.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1182 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - Selects GPIO_4 as ADC1_S15<br>1b - Selects GPIO_33 as ADC1_S15|
|3<br>MUX_MODE_E<br>N_ADC1_S14|Mux Mode Enable ADC_1 Standard Channel 14<br>Controls the selection of GPIOs to drive ADC_1 standard channel 14.<br>0b - Selects GPIO_69 as ADC1_S14<br>1b - Selects GPIO_32 as ADC1_S14|
|2<br>MUX_MODE_E<br>N_ADC0_S9|Mux Mode Enable ADC_0 Standard Channel 9<br>Controls the selection of GPIOs to drive ADC_0 standard channel 9.<br>0b - Selects GPIO_1 as ADC0_S9<br>1b - Selects GPIO_46 as ADC0_S9|
|1<br>MUX_MODE_E<br>N_ADC0_S8|Mux Mode Enable ADC_0 Standard Channel 8<br>Controls the selection of GPIOs to drive ADC_0 standard channel 8.<br>0b - Selects GPIO_0 as ADC0_S8<br>1b - Selects GPIO_45 as ADC0_S8|
|0<br>—|Reserved|



### 37.2.44 Read Write GPR On Functional Reset 5 (DCMRWF5) 

#### Offset 

|Register|Offset|
|---|---|
|DCMRWF5|610h|



#### Function 

#### Resets on functional reset 5. 

The reset value is undefined on reset and is loaded from the flash memory contents at the end of the reset sequence. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1183 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1184-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R<br>BOOT_ADDRESS<br>W<br>Reset u u u u u u u u u u u u u u u u<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>R BOOT<br>BOOT_ADDRESS<br>W _MO...<br>Reset u u u u u u u u u u u u u u u u<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-1|Boot Address|
|BOOT_ADDRE<br>SS|Specifies the Cortex-M7_0 base address of the vector table to be used after exiting Standby mode (only<br>to be considered in Fast Standby mode).|
|0|Boot Mode|
|BOOT_MODE|Selects the type of Boot mode after exiting Standby mode.<br>0b - Normal|
||1b - Fast Standby|



### 37.2.45 Read Only GPR On PMCPOR Reset 1 (DCMROPP1) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROPP1|700h|



#### Function 

Resets on PMCPOR reset 1 and captures the status of the functional reset sequence process when POR_WDG overflows. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1184 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Diagram 

|Bits|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R|POR_<br>WDG..<br>.|POR_<br>WDG..<br>.|POR_<br>WDG..<br>.|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|POR_<br>WDG..<br>.|Reserv<br>ed|Reserv<br>ed|POR_<br>WDG..<br>.|Reserv<br>ed|
|W|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|Bits|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|R|Reserv<br>ed|POR_<br>WDG..<br>.|Reserv<br>ed|Reserv<br>ed|POR_<br>WDG..<br>.|POR_<br>WDG..<br>.|Reserv<br>ed|Reserv<br>ed|Reserv<br>ed|POR_<br>WDG..<br>.|POR_<br>WDG..<br>.|POR_<br>WDG..<br>.|POR_<br>WDG..<br>.|POR_<br>WDG..<br>.|POR_<br>WDG..<br>.|POR_<br>WDG..<br>.|
|W|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|W1C|
|Reset|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



#### Fields 

|Field|Function|
|---|---|
|31|POR_WDG Status 31|
|POR_WDG_ST<br>AT31|Captures the status of the MC_RGM reset event (if occurred) while the chip is in Standby mode.<br>This field is used only for standby sequence monitoring.<br>~~NOTE~~|
||0b - Event not detected or no reset event arrived<br>1b - Event detected|
|30|POR_WDG Status 30|
|POR_WDG_ST<br>AT30|Captures the status of standby exit acknowledgement by MC_PCU when POR_WDG overflows.<br>This field is used only for standby sequence monitoring.<br>~~NOTE~~|
||0b - Not acknowledged<br>1b - Acknowledged|
|29|POR_WDG Status 29|
|POR_WDG_ST<br>AT29|Captures the status of the MC_ME standby entry request that MC_ME initiates when POR_WDG overflows.<br>This field is used only for standby sequence monitoring.<br>~~NOTE~~|
||0b - Active<br>1b - Inactive|
|28|Reserved|
||Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1185 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|—<br>27|Reserved|
|—<br>26|Reserved|
|—<br>25<br>—|Reserved|
|24<br>—|Reserved|
|23<br>—|Reserved|
|22<br>—|Reserved|
|21<br>—<br>20<br>POR_WDG_ST<br>AT20|Reserved<br>POR_WDG Status 20<br>Specifies the status of the functional reset sequence process, DEST0, when POR_WDG overflows.<br>0b - Inactive<br>1b - Active|
|19<br>—<br>18<br>—|Reserved<br>Reserved|
|17<br>POR_WDG_ST<br>AT17|POR_WDG Status 10<br>Specifies the status of the functional reset sequence process, FUNC10, when POR_WDG overflows.<br>0b - Inactive<br>1b - Active|
|16<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1186 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|15<br>—|Reserved|
|14<br>POR_WDG_ST<br>AT14|POR_WDG Status 9<br>Specifies the status of the functional reset sequence process, FUNC9, when POR_WDG overflows.<br>0b - Inactive<br>1b - Active|
|13<br>—<br>12<br>—<br>11<br>POR_WDG_ST<br>AT11|Reserved<br>Reserved<br>POR_WDG Status 8<br>Specifies the status of the functional reset sequence process, FUNC8, when POR_WDG overflows.<br>0b - Inactive<br>1b - Active|
|10<br>POR_WDG_ST<br>AT10|POR_WDG Status 7<br>Specifies the status of the functional reset sequence process, FUNC7, when POR_WDG overflows.<br>0b - Inactive<br>1b - Active|
|9<br>—|Reserved|
|8<br>—|Reserved|
|7<br>—|Reserved|
|6<br>POR_WDG_ST<br>AT6|POR_WDG Status 6<br>Specifies the status of the functional reset sequence process, FUNC6, when POR_WDG overflows.<br>0b - Inactive<br>1b - Active|
|5|POR_WDG Status 5<br>Specifies the status of the functional reset sequence process, FUNC5, when POR_WDG overflows.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1187 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|POR_WDG_ST<br>AT5|0b - Inactive<br>1b - Active|
|4|POR_WDG Status 4|
|POR_WDG_ST<br>AT4|Specifies the status of the functional reset sequence process, FUNC4, when POR_WDG overflows.<br>0b - Inactive<br>1b - Active|
|3<br>POR_WDG_ST<br>AT3|POR_WDG Status 3<br>Specifies the status of the functional reset sequence process, FUNC3, when POR_WDG overflows.<br>0b - Inactive<br>1b - Active|
|2|POR_WDG Status 2|
|POR_WDG_ST<br>AT2|Specifies the status of the functional reset sequence process, FUNC2, when POR_WDG overflows.<br>0b - Inactive<br>1b - Active|
|1<br>POR_WDG_ST<br>AT1|POR_WDG Status 1<br>Specifies the status of the functional reset sequence process, FUNC1, when POR_WDG overflows.<br>0b - Inactive<br>1b - Active|
|0|POR_WDG Status 0|
|POR_WDG_ST<br>AT0|Specifies the status of the functional reset sequence process, FUNC0, when POR_WDG overflows.<br>0b - Inactive<br>1b - Active|



### 37.2.46 Read Only GPR On PMCPOR Reset 2 (DCMROPP2) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROPP2|704h|



#### Function 

Resets on PMCPOR reset 2 and captures the MC_RGM functional or external event status when POR_WDG overflows. 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1188 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1189-03.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>POR_ POR_ POR_ POR_<br>Reserv Reserv Reserv Reserv Reserv Reserv Reserv Reserv Reserv Reserv Reserv Reserv<br>R WDG.. WDG.. WDG.. WDG..<br>ed  ed  ed  ed  ed  ed  ed  ed  ed  ed  ed  ed<br>. . . .<br>W W1C W1C W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>POR_ POR_ POR_ POR_ POR_ POR_ POR_<br>Reserv Reserv Reserv Reserv Reserv Reserv Reserv Reserv Reserv<br>R WDG.. WDG.. WDG.. WDG.. WDG.. WDG.. WDG..<br>ed  ed  ed  ed  ed  ed  ed  ed  ed<br>. . . . . . .<br>W W1C W1C W1C W1C W1C W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31<br>—|Reserved|
|30|POR_WDG Status 62|
|POR_WDG_ST<br>AT62|Specifies the value of MC_RGM.FES[DEBUG_FUNC] when POR_WDG overflows.<br>0b - 0|
||1b - 1|
|29|POR_WDG Status 61|
|POR_WDG_ST<br>AT61|Specifies the value of MC_RGM.FES[SW_FUNC] when POR_WDG overflows.<br>0b - 0|
||1b - 1|
|28|Reserved|
|—||
|27<br>—<br>26<br>—|Reserved<br>Reserved|
|25<br>—|Reserved|
|24|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1189 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|—<br>23<br>|Reserved|
|—<br>22<br>|Reserved|
|—<br>21<br>—|Reserved|
|20<br>POR_WDG_ST<br>AT52|POR_WDG Status 52<br>Specifies the value of MC_RGM.FES[HSE_BOOT_RST] when POR_WDG overflows.<br>0b - 0<br>1b - 1|
|19<br>—|Reserved|
|18<br>—<br>17<br>—|Reserved<br>Reserved|
|16<br>POR_WDG_ST<br>AT48|POR_WDG Status 48<br>Specifies the value of MC_RGM.FES[HSE_SWT_RST] when POR_WDG overflows.<br>0b - 0<br>1b - 1|
|15<br>—|Reserved|
|14|Reserved|
|—<br>13<br>—|Reserved|
|12<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1190 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|11<br>|Reserved|
|—<br>10<br>—|Reserved|
|9<br>POR_WDG_ST<br>AT41|POR_WDG Status 41<br>Specifies the value of MC_RGM.FES[JTAG_RST] when POR_WDG overflows.<br>0b - 0<br>1b - 1|
|8<br>POR_WDG_ST<br>AT40|POR_WDG Status 40<br>Specifies the value of MC_RGM.FES[Reserved] when POR_WDG overflows.<br>0b - 0<br>1b - 1|
|7<br>POR_WDG_ST<br>AT39|POR_WDG Status 39<br>Specifies the value of MC_RGM.FES[SWT1_RST] when POR_WDG overflows.<br>0b - 0<br>1b - 1|
|6|POR_WDG Status 38|
|POR_WDG_ST<br>AT38|Specifies the value of MC_RGM.FES[SWT0_RST] when POR_WDG overflows.<br>0b - 0<br>1b - 1|
|5<br>—|Reserved|
|4<br>POR_WDG_ST<br>AT36|POR_WDG Status 36<br>Specifies the value of MC_RGM.FES[ST_DONE] when POR_WDG overflows.<br>0b - 0<br>1b - 1|
|3<br>POR_WDG_ST<br>AT35|POR_WDG Status 35<br>Specifies the value of MC_RGM.FES[FCCU_RST] when POR_WDG overflows.<br>0b - 0<br>1b - 1|
|2|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1191 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|—<br>1|Reserved|
|—<br>0|POR_WDG Status 32|
|POR_WDG_ST<br>AT32|Specifies the value of MC_RGM.FES[F_EXR] when POR_WDG overflows.<br>0b - 0|
||1b - 1|



### 37.2.47 Read Only GPR On PMCPOR Reset 3 (DCMROPP3) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROPP3|708h|



#### Function 

Resets on PMCPOR reset 3 and captures the MC_RGM destructive event status when POR_WDG overflows. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1192-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>POR_ POR_ POR_ POR_ POR_<br>Reserv Reserv Reserv Reserv Reserv Reserv Reserv Reserv Reserv Reserv Reserv<br>R WDG.. WDG.. WDG.. WDG.. WDG..<br>ed  ed  ed  ed  ed  ed  ed  ed  ed  ed  ed<br>. . . . .<br>W W1C W1C W1C W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>POR_ POR_ POR_ POR_ POR_ POR_ POR_ POR_ POR_ POR_<br>Reserv Reserv Reserv Reserv Reserv Reserv<br>R WDG.. WDG.. WDG.. WDG.. WDG.. WDG.. WDG.. WDG.. WDG.. WDG..<br>ed  ed  ed  ed  ed  ed<br>. . . . . . . . . .<br>W W1C W1C W1C W1C W1C W1C W1C W1C W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field<br>Function|
|---|
|31<br>Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1192 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|—<br>30<br>POR_WDG_ST<br>AT94|POR_WDG Status 94<br>Specifies the value of MC_RGM.DES[DEBUG_DEST] when POR_WDG overflows.<br>0b - 0<br>1b - 1|
|29<br>POR_WDG_ST<br>AT93|POR_WDG Status 93<br>Specifies the value of MC_RGM.DES[SW_DEST] when POR_WDG overflows.<br>0b - 0<br>1b - 1|
|28<br>—|Reserved|
|27<br>—<br>26<br>—|Reserved<br>Reserved|
|25<br>—|Reserved|
|24<br>—|Reserved|
|23<br>—|Reserved|
|22<br>—|Reserved|
|21<br>—|Reserved|
|20<br>—|Reserved|
|19<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1193 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
|18<br>POR_WDG_ST<br>AT82|POR_WDG Status 82<br>Specifies the value of MC_RGM.DES[HSE_SNVS_RST] when POR_WDG overflows.<br>0b - 0<br>1b - 1|
|17<br>POR_WDG_ST<br>AT81|POR_WDG Status 81<br>Specifies the value of MC_RGM.DES[HSE_TMPR_RST] when POR_WDG overflows.<br>0b - 0<br>1b - 1|
|16<br>POR_WDG_ST<br>AT80|POR_WDG Status 80<br>Specifies the value of MC_RGM.DES[CM7_CORE_CLK_FAIL] when POR_WDG overflows.<br>0b - 0<br>1b - 1|
|15<br>POR_WDG_ST<br>AT79|POR_WDG Status 79<br>Specifies the value of MC_RGM.DES[SYS_DIV_FAIL] when POR_WDG overflows.<br>0b - 0<br>1b - 1|
|14<br>POR_WDG_ST<br>AT78|POR_WDG Status 78<br>Specifies the value of MC_RGM.DES[HSE_CLK_FAIL] when POR_WDG overflows.<br>0b - 0<br>1b - 1|
|13<br>—|Reserved|
|12<br>POR_WDG_ST<br>AT76|POR_WDG Status 76<br>Specifies the value of MC_RGM.DES[AIPS_PLAT_CLK_FAIL] when POR_WDG overflows.<br>0b - 0<br>1b - 1|
|11<br>—|Reserved|
|10<br>POR_WDG_ST<br>AT74|POR_WDG Status 74<br>Specifies the value of MC_RGM.DES[CORE_CLK_FAIL] when POR_WDG overflows.<br>Table continues on the next page...|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1194 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

Table continued from the previous page... 

|Field|Function|
|---|---|
||0b - 0<br>1b - 1|
|9<br>POR_WDG_ST<br>AT73|POR_WDG Status 73<br>Specifies the value of MC_RGM.DES[PLL_LOL] when POR_WDG overflows.<br>0b - 0<br>1b - 1|
|8<br>POR_WDG_ST<br>AT72|POR_WDG Status 72<br>Specifies the value of MC_RGM.DES[SWT2_RST] when POR_WDG overflows.<br>0b - 0<br>1b - 1|
|7<br>—|Reserved|
|6<br>POR_WDG_ST<br>AT70|POR_WDG Status 70<br>Specifies the value of MC_RGM.DES[MC_RGM_FRE] when POR_WDG overflows.<br>0b - 0<br>1b - 1|
|5<br>—|Reserved|
|4<br>POR_WDG_ST<br>AT68|POR_WDG Status 68<br>Specifies the value of MC_RGM.DES[STCU_URF] when POR_WDG overflows.<br>0b - 0<br>1b - 1|
|3<br>POR_WDG_ST<br>AT67|POR_WDG Status 67<br>Specifies the value of MC_RGM.DES[FCCU_FTR] when POR_WDG overflows.<br>0b - 0<br>1b - 1|
|2<br>—|Reserved|
|1<br>—|Reserved|



Table continues on the next page... 

S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1195 / 4640 

NXP Semiconductors 

Device Configuration Module General-Purpose Registers (DCM_GPR) 

#### Table continued from the previous page... 

|Field|Function|
|---|---|
|0|POR_WDG Status 64|
|POR_WDG_ST<br>AT64|Specifies the value of MC_RGM.DES[F_POR] when POR_WDG overflows.<br>0b - 0|
||1b - 1|



### 37.2.48 Read Only GPR On PMCPOR Reset 4 (DCMROPP4) 

#### Offset 

|Register|Offset|
|---|---|
|DCMROPP4|70Ch|



#### Function 

Resets on PMCPOR reset 4 and captures the POR_WDG reset event if POR_WDG initiates a POR sequence. 

#### Diagram 


![](D:/wnagjin/Compay_Project/CDC_7255/cdc_7255/.agents/skills/s32k3-rtd-master/docs/NXP_S32K3/images_RM/Security_and_Device_GPRs/037_Device_Configuration_Module_General-Purpose_Registers_-DCM_GPR-/S32K3XXRM_数据表.pdf-1196-10.png)


<!-- Start of picture text -->
Bits 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16<br>R Reserved<br>W W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>Bits 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0<br>POR_<br>R Reserved<br>WDG...<br>W W1C W1C<br>Reset 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br><!-- End of picture text -->

#### Fields 

|Field|Function|
|---|---|
|31-1|Reserved|
|—||
|0|POR_WDG Status|
|POR_WDG_ST<br>AT96|Specifies the status of POR_WDG.<br>See POR_WDG_STAT[95:0] for the chip status when POR_WDG overflows.|
||0b - Inactive|
||1b - Active (detected a stuck scenario and raised the chip POR event)|



S32K3xx Reference Manual, Rev. 4, 04/2022 

Reference Manual 

Preliminary Information 

1196 / 4640 

